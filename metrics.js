// Anonymous usage counts (added 2026-10-10). Jaxon wants to show truthfully how much the class uses
// the site ("N questions answered, M students") without recording anything about anyone. So this
// file keeps COUNTS ONLY, at day granularity, in our own Firestore:
//
//   metrics_daily/{YYYY-MM-DD}  ->  { q_answered: 412, quiz_done: 9, guide_open: 30, ... }
//
// Never stored, anywhere in it: question text, typed answers, names, emails, uids, IPs, device ids,
// page addresses, or the time of any single event. A day document is one row of integers.
//
// HOW COUNTING WORKS
//   PAMetrics.add(field, n)  adds n to a field for today. Nothing is sent: the number goes into a
//                            device-only buffer (localStorage "local:metrics:buf", which cloud-sync never
//                            uploads), keyed by day so a count always lands in the day it happened.
//   PAMetrics.mark(name)     "this device was active today" for a distinct count (active students per
//                            day, week and month; planner days). The buffer only remembers that it happened;
//                            when it is sent, the synced key "metrics:seen" (the newest day, ISO week and
//                            month already counted for that mark) decides which of the day / week / month
//                            counters get +1. That is how distinct students are counted WITHOUT storing who:
//                            each device adds 1 to "active this week" once per ISO week, and a signed-in
//                            student's devices share the marker through cloud-sync, so they count once.
//
// HOW IT IS SENT (the Firestore budget: the 2026-09-28 quota blowout came from per-load and per-event
// writes). The whole buffer goes out as ONE batched increment() write, at most once every 10 minutes
// while a page is open, or when the student leaves the tab (at most once every 2 minutes). Nothing is
// ever READ back: there is no metrics read on page load, and the rules forbid client reads entirely.
// A failed write (rules not published yet, offline) puts the counts back for the next try, so nothing
// is lost while the rules wait to be published. It is sent while the page is alive, never during
// unload, because a write cut off mid-flight could otherwise be counted twice or not at all; the
// buffer simply waits for the next page.
//
// WHO IS NEVER COUNTED (checked before anything is buffered AND again before anything is sent):
//   - a student who turned it off (synced "metrics:off" = "1": that device and their account)
//   - a developer device or account (synced "metrics:dev" = "1"; set it with ?metrics=dev, clear it
//     with ?metrics=on). Jaxon's account carries it, so his testing never inflates the numbers.
//   - automated browsers (navigator.webdriver), local previews (localhost) and file:// pages.
//
// The rules (firestore.rules, match /metrics_daily) accept a write only from a signed-in Firebase
// session (a student who never signed in with Google gets a silent anonymous one, exactly like Group
// Study), only on the listed fields, and only as small positive increments.
//
// Other features add their own families through PAMetrics.family(name, spec) (a collection, its fields
// with a per-write cap, and its distinct marks), so this file knows nothing about them.
// The report: python3 tools/usage_report.py (admin read, prints Markdown, applies the small-number rule).
(function () {
  "use strict";
  var shim = window.PAMetrics;
  if (shim && shim.__real) return;

  var BUF = "local:metrics:buf", LAST = "local:metrics:last", FAIL = "local:metrics:fail";
  var SEEN = "metrics:seen", OFF = "metrics:off", DEV = "metrics:dev", NOTICE = "metrics:notice";
  var GAP_MS = 10 * 60 * 1000, HIDDEN_GAP_MS = 2 * 60 * 1000, KEEP_DAYS = 30;

  // field -> the most one write may add (the rules enforce the same caps). A bigger buffered number is
  // sent in several writes. Distinct counters are capped at 1: one device, one +1 per day/week/month.
  var FAMILIES = {
    site: {
      coll: "metrics_daily",
      fields: { q_answered: 1000, quiz_done: 50, guide_open: 100, cram_open: 100, ref_open: 100,
                arcade_session: 100, review_drill: 50, planner_day: 1, active_d: 1, active_w: 1, active_m: 1 },
      marks: { active: { d: "active_d", w: "active_w", m: "active_m" }, planner: { d: "planner_day" } }
    }
  };

  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { if (v == null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) {} }
  function jget(k) { try { var v = JSON.parse(get(k)); return v && typeof v === "object" ? v : null; } catch (e) { return null; } }

  function excluded() {
    if (get(OFF) === "1" || get(DEV) === "1") return true;
    if (window.__PA_METRICS_TEST) return false;   // the fake-Firestore test rig only
    if (navigator.webdriver) return true;
    if (!/^https?:$/.test(location.protocol)) return true;
    return /^(localhost|127\.0\.0\.1|0\.0\.0\.0|\[::1\])$/.test(location.hostname);
  }

  // ------------------------------------------------------------------ days, ISO weeks, months
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function dayKey(d) { d = d || new Date(); return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate()); }
  function weekKey(day) {   // ISO 8601 week of a YYYY-MM-DD day, e.g. "2026-W41"
    var p = day.split("-"), d = new Date(+p[0], +p[1] - 1, +p[2]);
    d.setDate(d.getDate() - (d.getDay() + 6) % 7 + 3);   // the Thursday of its week names the week-year
    var y = d.getFullYear(), jan4 = new Date(y, 0, 4);
    return y + "-W" + pad(1 + Math.round(((d - jan4) / 864e5 - 3 + (jan4.getDay() + 6) % 7) / 7));
  }

  // ------------------------------------------------------------------ the buffer
  function readBuf() { return jget(BUF) || {}; }
  function saveBuf(b) { set(BUF, Object.keys(b).length ? JSON.stringify(b) : null); }
  function famOf(field) {
    for (var f in FAMILIES) if (FAMILIES[f].fields[field]) return f;
    return null;
  }
  function bump(b, day, fam, field, n) {
    var e = b[day] || (b[day] = {}), c = e[fam] || (e[fam] = {});
    c[field] = Math.min(1e6, (c[field] || 0) + n);
  }

  function add(field, n) {
    n = n == null ? 1 : Math.floor(+n || 0);
    if (n <= 0 || excluded()) return;
    var fam = famOf(field);
    if (!fam) return;
    var b = readBuf(); bump(b, dayKey(), fam, field, n); saveBuf(b);
    soon();
  }
  function mark(name) {
    if (excluded()) return;
    var b = readBuf(), d = dayKey(), e = b[d] || (b[d] = {});
    (e.marks || (e.marks = {}))[name] = 1;
    saveBuf(b);
    soon();
  }
  function family(name, spec) {
    if (!name || !spec || !spec.coll || !spec.fields || FAMILIES[name]) return;
    FAMILIES[name] = { coll: spec.coll, fields: spec.fields, marks: spec.marks || {} };
    soon();
  }
  function markSpec(name) {
    for (var f in FAMILIES) if (FAMILIES[f].marks && FAMILIES[f].marks[name]) return { fam: f, spec: FAMILIES[f].marks[name] };
    return null;
  }

  // ------------------------------------------------------------------ sending
  var db = null, auth = null, authKnown = false, hydrated = false, flushing = false, anonTried = false;

  function gap(hidden) {
    var fails = Math.min(8, +get(FAIL) || 0);
    return (hidden ? HIDDEN_GAP_MS : GAP_MS) * Math.pow(2, fails);
  }

  var soonT = null;
  function soon() { if (!soonT) soonT = setTimeout(function () { soonT = null; due(false); }, 0); }

  function due(hidden) {
    if (!db || !authKnown || !hydrated || flushing) return;
    if (excluded()) { saveBuf({}); return; }
    var b = readBuf();
    if (!Object.keys(b).length) return;
    var last = +get(LAST) || 0, now = Date.now();
    if (last <= now && now - last < gap(hidden)) return;
    if (!auth.currentUser) {
      // never signed in with Google: a silent anonymous session, the same as Group Study, so the rule can
      // require a signed-in client. Only after the first auth callback said nobody is signed in, because
      // signInAnonymously() would replace a Google session.
      if (!anonTried) { anonTried = true; auth.signInAnonymously().catch(function () {}); }
      return;   // onAuthStateChanged calls due() again when it lands
    }
    flush(b);
  }

  function flush(b) {
    flushing = true;
    set(LAST, String(Date.now()));
    var seen = jget(SEEN) || {}, seen0 = JSON.stringify(seen);
    var today = dayKey(), oldest = dayKey(new Date(Date.now() - KEEP_DAYS * 864e5));
    var writes = [], rest = {};

    Object.keys(b).sort().forEach(function (day) {
      if (!/^\d{4}-\d{2}-\d{2}$/.test(day) || day < oldest || day > today) return;   // outside what the rules accept
      var e = b[day], out = {};
      Object.keys(e).forEach(function (fam) {
        if (fam === "marks") return;
        var F = FAMILIES[fam], c = e[fam];
        Object.keys(c).forEach(function (field) {
          if (!F) { bump(rest, day, fam, field, c[field]); return; }   // its script is not on this page: keep it
          var cap = F.fields[field];
          if (!cap) return;
          var take = Math.min(c[field], cap);
          (out[fam] || (out[fam] = {}))[field] = take;
          if (c[field] > take) bump(rest, day, fam, field, c[field] - take);
        });
      });
      Object.keys(e.marks || {}).forEach(function (m) {
        var M = markSpec(m);
        if (!M) { var r = rest[day] || (rest[day] = {}); (r.marks || (r.marks = {}))[m] = 1; return; }
        [["d", day], ["w", weekKey(day)], ["m", day.slice(0, 7)]].forEach(function (pk) {
          var field = M.spec[pk[0]], sk = m + "." + pk[0];
          if (!field || (seen[sk] && seen[sk] >= pk[1])) return;
          seen[sk] = pk[1];
          var o = out[M.fam] || (out[M.fam] = {});
          o[field] = Math.min(FAMILIES[M.fam].fields[field] || 1, (o[field] || 0) + 1);
        });
      });
      Object.keys(out).forEach(function (fam) { writes.push({ coll: FAMILIES[fam].coll, fam: fam, day: day, counts: out[fam] }); });
    });

    saveBuf(rest);
    // the marker moves now: a distinct count resolved above is either sent below or, if the write fails,
    // put back as a plain count, so it is sent exactly once either way
    if (JSON.stringify(seen) !== seen0) set(SEEN, JSON.stringify(seen));
    if (!writes.length) { flushing = false; return; }

    var inc = firebase.firestore.FieldValue.increment, batch = db.batch();
    writes.forEach(function (w) {
      var patch = {};
      Object.keys(w.counts).forEach(function (f) { patch[f] = inc(w.counts[f]); });
      batch.set(db.collection(w.coll).doc(w.day), patch, { merge: true });
    });
    batch.commit().then(function () {
      flushing = false;
      set(FAIL, null);
      api._sent += writes.length;
    }).catch(function () {
      flushing = false;
      set(FAIL, String(Math.min(8, (+get(FAIL) || 0) + 1)));
      if (excluded()) return;
      var cur = readBuf();
      writes.forEach(function (w) { Object.keys(w.counts).forEach(function (f) { bump(cur, w.day, w.fam, f, w.counts[f]); }); });
      saveBuf(cur);
    });
  }

  function boot() {
    try { db = firebase.firestore(); auth = firebase.auth(); } catch (e) { return; }
    auth.onAuthStateChanged(function (u) {
      authKnown = true;
      // a Google account's devices share "metrics:seen" through cloud-sync, so wait until this page has
      // pulled the newest copy before deciding whether today is already counted
      hydrated = !u || u.isAnonymous || !!window.__cloudSyncHydrated;
      due(false);
    });
    setInterval(function () { if (document.visibilityState !== "hidden") due(false); }, 60000);
    document.addEventListener("visibilitychange", function () {
      // a short wait: a page that is unloading never runs it, so a write is only started on a live page
      if (document.visibilityState === "hidden") setTimeout(function () { due(true); }, 400);
    });
  }
  window.addEventListener("cloudSyncHydrated", function () { hydrated = true; due(false); });

  // ------------------------------------------------------------------ what every page counts by itself
  function oncePerTab(key) {
    try { var k = "metrics:tab:" + key; if (sessionStorage.getItem(k)) return false; sessionStorage.setItem(k, "1"); } catch (e) {}
    return true;
  }
  function countPage() {
    mark("active");
    var path = location.pathname, p = path.toLowerCase();
    try { p = decodeURIComponent(p); } catch (e) {}
    // once per tab per page, so a cloud-sync reload or going back to it does not count it again
    if (document.querySelector(".guide-back-bar") && oncePerTab("open:" + path)) {
      add(p.indexOf("cram-sheet") >= 0 ? "cram_open" : p.indexOf("study-guide") >= 0 ? "guide_open" : "ref_open");
    }
    if (/\/arcade-(study|learn|match|sprint)\.html$/.test(p) && oncePerTab("open:" + path + location.search)) add("arcade_session");
    if (/\/calendar\.html$/.test(p) && !/[?&](asof|now)=/.test(location.search)) mark("planner");
  }

  // ------------------------------------------------------------------ developer flag (?metrics=dev / ?metrics=on)
  function devParam() {
    var m = /[?&]metrics=(dev|on)\b/.exec(location.search);
    if (!m) return;
    set(DEV, m[1] === "dev" ? "1" : "0");
    if (m[1] === "dev") saveBuf({});
    try {
      var u = new URL(location.href); u.searchParams.delete("metrics");
      history.replaceState(history.state, "", u.pathname + u.search + u.hash);
    } catch (e) {}
    var say = function () {
      if (window.showToast) window.showToast(m[1] === "dev" ? "Developer device: nothing here is counted (and nothing on your account, once you're signed in)."
                                                           : "Developer flag off: this device counts like everyone else's.", 6000);
    };
    if (document.readyState === "complete") say(); else window.addEventListener("load", say);
  }

  // ------------------------------------------------------------------ the one-time note
  var NOTE = (shim && shim.note) || "";   // one copy of the wording, in theme.js (the Settings panel shows it too)

  function setOff(on) {
    set(OFF, on ? "1" : "0");
    if (on) saveBuf({});
  }

  function showNote() {
    if (!NOTE || excluded() || get(NOTICE) === "1" || document.getElementById("metrics-note")) return;
    // never over a quiz (its engine defines markCompleted): the note waits for the next page that is not one
    if (typeof window.markCompleted === "function" || window.CLASS_STATS_PER_ANSWER) return;
    var box = document.createElement("div");
    box.id = "metrics-note";
    box.setAttribute("role", "region");
    box.setAttribute("aria-label", "About anonymous usage counts");
    var p = document.createElement("p");
    p.textContent = NOTE;
    var row = document.createElement("div");
    row.className = "mn-row";
    var ok = document.createElement("button"); ok.type = "button"; ok.className = "mn-ok"; ok.textContent = "Got it";
    var off = document.createElement("button"); off.type = "button"; off.className = "mn-off"; off.textContent = "Turn off";
    row.appendChild(ok); row.appendChild(off);
    box.appendChild(p); box.appendChild(row);
    function close() { set(NOTICE, "1"); if (box.parentNode) box.parentNode.removeChild(box); }
    ok.addEventListener("click", close);
    off.addEventListener("click", function () {
      setOff(true); close();
      if (window.showToast) window.showToast("Counting is off on this device and your account. You can turn it back on in Settings.", 6000);
    });
    document.body.appendChild(box);
    requestAnimationFrame(function () { box.classList.add("in"); });
  }

  // ------------------------------------------------------------------ public surface
  var api = {
    __real: true,
    _sent: 0,
    add: add,
    mark: mark,
    family: family,
    allowed: function () { return !excluded(); },
    isOff: function () { return get(OFF) === "1"; },
    isDev: function () { return get(DEV) === "1"; },
    setOff: setOff,
    note: NOTE,
    _weekKey: weekKey   // test hook
  };
  window.PAMetrics = api;

  devParam();
  // calls made before this file loaded (theme.js keeps a small queue)
  ((shim && shim._q) || []).forEach(function (c) { try { api[c[0]].apply(null, c[1]); } catch (e) {} });

  function ready() {
    countPage();
    setTimeout(showNote, 1500);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", ready); else ready();

  if (window.__firebaseReady) boot();
  else window.addEventListener("firebaseReady", boot, { once: true });
})();
