// Class-wide cumulative "questions answered" counter. A single shared Firestore
// doc -- stats/global.questionsCompleted -- is incremented whenever anyone
// finishes a quiz, and the homepage subscribes to it live with an animated
// count-up. Built on the same Firebase project as cloud-sync.js / presence.js,
// and loaded by theme.js's Firebase bootstrap chain on every page. It only does
// work where relevant: it increments on a quiz page (by hooking the engines'
// shared markCompleted() finish signal) and displays on any page that has a
// #class-counter-value element (the homepage).
//
// Scoring here is client-trusted. The published rule on this doc is fully
// open -- verified 2026-07-27 by a successful UNAUTHENTICATED write, so it is
// `allow read, write: if true`, not the auth-gated form an earlier version of
// this comment claimed. That is deliberate: most quiz-page visitors are not
// signed in (Google sign-in is optional), so an auth gate would drop the
// majority of real increments. The tradeoff is that anyone can write any
// value with no credentials, which is acceptable for a casual engagement
// metric and would not be for anything load-bearing.
//   match /stats/global {
//     allow read: if true;
//     allow write: if request.resource.data.questionsCompleted is number;
//     allow delete: if false;
//   }
// It is shape-guarded rather than wide open: unauthenticated writes ARE
// allowed, but only ones that set questionsCompleted to a number, so the doc
// cannot be used as arbitrary storage. Anyone can still set the counter to any
// value without signing in.
// Until such a rule is published, writes/reads fail silently (counter stays 0).
//
// EVENT LOG, RETIRED 2026-10-10. From 2026-07-27 every increment also appended a row to stats_events
// (n, quiz path, a random per-tab id, a server timestamp) so a jump in the total could be traced. Jaxon's
// privacy rules for usage numbers (day-level granularity at most, never a per-event time) rule that out,
// and the collection was readable by anyone. The anonymous daily totals in metrics.js (metrics_daily,
// q_answered per day) now do the reconciling: summing them from a known day reproduces the growth of
// questionsCompleted. firestore.rules now refuses new rows and all reads of the old ones.
(function () {
  "use strict";

  var db = null;
  var ready = false;
  var pending = 0; // increments queued before Firebase is ready

  // Anonymous usage counts (metrics.js, 2026-10-10). A student who turned counting off in Settings, a
  // developer device or account (Jaxon's testing), an automated browser and a local preview add nothing
  // to the class total, its log or the class picks either: "off" means all counting. Checked when a count
  // is made AND when it is sent, so turning it off drops anything still waiting.
  function counting() {
    try { return !window.PAMetrics || !window.PAMetrics.allowed || window.PAMetrics.allowed(); } catch (e) { return true; }
  }
  function metric(field, n) {
    try { if (window.PAMetrics) window.PAMetrics.add(field, n); } catch (e) {}
  }

  function statRef() { return db.collection("stats").doc("global"); }

  function flush() {
    if (!counting()) { pending = 0; return; }
    if (!ready || pending <= 0) return;
    var n = pending;
    pending = 0;
    if (flushTimer) { clearTimeout(flushTimer); flushTimer = null; }
    statRef().set({
      questionsCompleted: firebase.firestore.FieldValue.increment(n),
      updatedAt: firebase.firestore.FieldValue.serverTimestamp()
    }, { merge: true }).catch(function () { /* permission-denied / offline -- drop silently */ });
  }

  // The practicums count one question per answer rather than a lump at the
  // finish, so a page can produce 30+ increments instead of one. Coalescing
  // them over a few seconds keeps that from becoming 30 Firestore writes and
  // 30 counter writes, and a pagehide flush means a half-finished attempt still
  // counts.
  var flushTimer = null;
  var COALESCE_MS = 4000;

  function flushSoon() {
    if (flushTimer) return;
    flushTimer = setTimeout(function () { flushTimer = null; flush(); }, COALESCE_MS);
  }

  // ---------------------------------------------------------------------
  // PER-OPTION RESPONSE DISTRIBUTION  (added 2026-08-27)
  //
  // Jaxon's reference exam items show, beside every choice, what share of the
  // class picked it -- which is the most useful thing on the page, because it
  // tells you which distractor fooled people rather than just that you were
  // wrong. The engine only ever recorded a right/wrong boolean, so we could not
  // reproduce it. These two calls store and read the distribution.
  //
  // OPT-IN BY CONSTRUCTION. Every quiz page bakes its own copy of the engine at
  // render time, so only pages rendered from tools/quiz-template on or after
  // this date call recordPick(). Existing quizzes never invoke it and are
  // completely unaffected -- which is what Jaxon asked for.
  //
  // One doc per question: answer_picks/<quizslug>__<hash of the stem>. Keying on
  // the stem rather than its index means re-rendering a quiz, or reshuffling a
  // master exam, does not orphan the counts.
  //
  // FIRST ANSWER PER DEVICE ONLY. The class total already has the problem that
  // Jaxon's own repeat testing inflates it. Here a localStorage marker means a
  // retake never re-counts, so the percentages stay a picture of what people
  // chose the first time -- which is the only reading that means anything.
  // ---------------------------------------------------------------------

  // ---------------------------------------------------------------------
  // HIDING THE CLASS NUMBERS  (added 2026-09-08)
  //
  // Jaxon asked for a Settings switch that hides class statistics in quizzes,
  // and for it to work on the quizzes already on the site as well as future
  // ones. Every quiz page bakes its own copy of the engine at render time, so
  // a check added to tools/quiz-template only ever reaches quizzes rendered
  // AFTER it -- the 83 pages already shipped would have gone on showing the
  // numbers until each was re-rendered. This file is shared by every page, so
  // the gate lives here instead: one switch, effective everywhere at once, no
  // re-render and no diff across 83 files.
  //
  // Both surfaces the engine draws hang off getPicks() -- the per-option
  // percentages, and the "You vs the class" panel on the results screen, which
  // only accumulates from getPicks results. Resolving null turns off both.
  //
  // Hiding is a DISPLAY preference, not an opt-out. The pick is still written,
  // so one student turning the numbers off does not thin them for everyone
  // else.
  // ---------------------------------------------------------------------
  var HIDE_KEY = "hideClassStats";

  function statsHidden() {
    try { return localStorage.getItem(HIDE_KEY) === "1"; } catch (e) { return false; }
  }

  var pickQueue = [];

  function flushPicks() {
    if (!db) return;
    var q = pickQueue; pickQueue = [];
    q.forEach(function (a) { writePick(a[0], a[1], a[2]); });
  }

  function writePick(qid, oi, nOpts) {
    if (!counting()) return;
    if (!db) { if (pickQueue.length < 200) pickQueue.push([qid, oi, nOpts]); return; }
    try {
      var patch = {
        total: firebase.firestore.FieldValue.increment(1),
        opts: nOpts
      };
      patch["c" + oi] = firebase.firestore.FieldValue.increment(1);
      db.collection("answer_picks").doc(qid)
        .set(patch, { merge: true })
        .catch(function () { /* rule not published yet -- quiz still works */ });
    } catch (e) { /* never let stats break a quiz */ }
  }

  window.ClassStats = {
    _odo: function (el, n) { animateTo(el, n); },   // test hook: drive the odometer without Firebase
    // Record n newly-completed questions toward the class total.
    record: function (n) {
      n = Math.max(0, Math.floor(+n || 0));
      if (!n || !counting()) return;
      metric("q_answered", n);
      pending += n;
      flush();
    },
    // Record a single answered question, batched. (`kind` used to tag the retired log row; callers
    // still pass it, so the argument stays.)
    recordAnswer: function (kind) {
      if (!counting()) return;
      metric("q_answered", 1);
      pending += 1;
      flushSoon();
    },

    // Returns true if this counted (first time this device answered this
    // question), so the caller can add its own +1 to what it displays without
    // waiting for the write to land.
    recordPick: function (qid, oi, nOpts) {
      if (!qid || typeof oi !== "number" || oi < 0) return false;
      // not counted: nothing is written, so the caller must not add this answer to the bars it draws
      if (!counting()) return false;
      var key = "ap:" + qid, fresh = true;
      try {
        fresh = !localStorage.getItem(key);
        if (fresh) localStorage.setItem(key, String(oi));
      } catch (e) { /* private mode -- fall through and count it */ }
      if (!fresh) return false;
      writePick(qid, oi, nOpts);
      // The caller adds its own +1 to the tally it is about to draw, so that
      // answering moves the bars without waiting for the write to land. When
      // the numbers are hidden it is about to be told the tally is zero --
      // returning true here would leave it drawing a lone 100% bar.
      return !statsHidden();
    },

    // Read and set the Settings switch. Kept on ClassStats rather than in
    // theme.js so the key has exactly one owner.
    isHidden: statsHidden,
    setHidden: function (on) {
      try { localStorage.setItem(HIDE_KEY, on ? "1" : "0"); } catch (e) { /* private mode */ }
      // Strip anything already drawn. Turning them back ON cannot repaint the
      // current question -- the engine only draws after an answer -- so the
      // numbers reappear from the next one.
      if (on && typeof document !== "undefined") {
        var n = document.getElementById("classpicks");
        if (n && n.parentNode) n.parentNode.removeChild(n);
        var kill = document.querySelectorAll(".pct, .pctbar, .vs");
        for (var i = 0; i < kill.length; i++) {
          if (kill[i].parentNode) kill[i].parentNode.removeChild(kill[i]);
        }
      }
    },

    // Resolves to {total, c0..cN} or null. Never rejects: a missing rule, an
    // offline device, a question nobody has answered, or the Settings switch
    // above all resolve null and the caller simply shows nothing.
    getPicks: function (qid) {
      if (!qid || statsHidden()) return Promise.resolve(null);
      return new Promise(function (resolve) {
        function go() {
          try {
            db.collection("answer_picks").doc(qid).get()
              .then(function (s) { resolve((s.exists && s.data()) || null); })
              .catch(function () { resolve(null); });
          } catch (e) { resolve(null); }
        }
        if (ready && db) return go();
        window.addEventListener("firebaseReady", function () { setTimeout(go, 0); }, { once: true });
        setTimeout(function () { if (!ready) resolve(null); }, 6000);
      });
    }
  };

  ["pagehide", "beforeunload"].forEach(function (evt) {
    window.addEventListener(evt, function () { flush(); });
  });
  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState === "hidden") flush();
  });

  // Hook the quiz engines: markCompleted(score, total, timeMs) is their shared
  // finish signal (a top-level function, so it's on window). Wrapping it here --
  // this file loads after the quiz page's own inline script has defined it --
  // means finishing a quiz adds its question count to the class total, with no
  // per-quiz edits. A quiz completed in the ~2s before this file loads is the
  // only miss, which is negligible since a quiz takes far longer than that.
  if (typeof window.markCompleted === "function") {
    var orig = window.markCompleted;
    window.markCompleted = function (score, total, timeMs) {
      // Pages that count per answer (the practicums) opt out of the lump sum
      // here, otherwise every attempt would be counted twice.
      try {
        if (counting()) metric("quiz_done", 1);
        if (!window.CLASS_STATS_PER_ANSWER) window.ClassStats.record(total);
        else flush();
      } catch (e) {}
      return orig.apply(this, arguments);
    };
  }

  // The homepage counter is an ODOMETER (2026-09-30, Jaxon: "do 4"): every digit is its own column
  // that rolls to its new value, right-most first, instead of the whole number being swapped.
  // The real number stays in a visually hidden span for screen readers and for aria-live; the
  // rolling digits are aria-hidden decoration. With reduced motion the digits simply jump.
  var reduceMotion = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  function digitCol(d) {
    var col = document.createElement("span"); col.className = "od";
    var roll = document.createElement("span"); roll.className = "odr";
    for (var k = 0; k < 10; k++) { var i = document.createElement("i"); i.textContent = k; roll.appendChild(i); }
    roll.style.setProperty("--d", d); col.appendChild(roll); return col;
  }
  function animateTo(el, target) {
    var start = parseInt(el.getAttribute("data-val") || "0", 10) || 0;
    var str = target.toLocaleString();
    var sr = el.querySelector(".sr"), od = el.querySelector(".odo");
    if (!sr) {
      el.textContent = "";
      sr = document.createElement("span"); sr.className = "sr"; el.appendChild(sr);
      od = document.createElement("span"); od.className = "odo"; od.setAttribute("aria-hidden", "true"); el.appendChild(od);
    }
    sr.textContent = str;
    var prevStr = start.toLocaleString();
    // rebuild the columns when the shape changes (a comma or a new digit appears), starting each
    // digit at its old value so it rolls from where it was
    var shapeKey = str.replace(/\d/g, "9");
    if (od.getAttribute("data-shape") !== shapeKey) {
      od.innerHTML = ""; od.setAttribute("data-shape", shapeKey);
      var pad = prevStr.length < str.length ? new Array(str.length - prevStr.length + 1).join("0") : "";
      var from = (pad + prevStr).slice(-str.length);
      for (var i = 0; i < str.length; i++) {
        var ch = str.charAt(i);
        if (/\d/.test(ch)) od.appendChild(digitCol(/\d/.test(from.charAt(i)) ? +from.charAt(i) : 0));
        else { var sep = document.createElement("span"); sep.className = "osep"; sep.textContent = ch; od.appendChild(sep); }
      }
    }
    var cols = od.querySelectorAll(".odr"), digits = str.replace(/\D/g, "");
    if (reduceMotion || target === start && el.getAttribute("data-val") !== null) {
      [].forEach.call(cols, function (c, n) { c.style.transition = "none"; c.style.setProperty("--d", digits.charAt(n)); });
    } else {
      // right-most digit first, each column a little later than the one to its right
      void od.offsetWidth;   // flush the starting digits so the roll is a transition, not a jump
      requestAnimationFrame(function () {
        [].forEach.call(cols, function (c, n) {
          c.style.transitionDelay = ((cols.length - 1 - n) * 70) + "ms";
          c.style.setProperty("--d", digits.charAt(n));
        });
      });
      var wrap = el.closest ? el.closest(".class-counter") : null;
      if (wrap && target > start && start > 0) { wrap.classList.remove("cc-bump"); void wrap.offsetWidth; wrap.classList.add("cc-bump"); }
    }
    el.setAttribute("data-val", target);
  }

  function boot() {
    db = firebase.firestore();
    ready = true;
    flush();
    flushPicks();

    var el = document.getElementById("class-counter-value");
    if (!el) return; // this page doesn't display the counter
    // Every increment anyone makes is pushed to every page listening, and each push is a billed read.
    // A hidden tab has nobody looking at the number, so it listens only while the page is on screen
    // (coming back to it costs one read and shows the current total).
    var unsub = null;
    function listen() {
      if (unsub) return;
      unsub = statRef().onSnapshot(function (snap) {
        var v = (snap.exists && snap.data() && snap.data().questionsCompleted) || 0;
        var wrap = document.getElementById("class-counter");
        if (wrap) wrap.classList.add("ready");
        animateTo(el, v);
      }, function () { /* offline / permission-denied -- leave the placeholder */ });
    }
    function unlisten() { if (unsub) { unsub(); unsub = null; } }
    if (document.visibilityState !== "hidden") listen();
    document.addEventListener("visibilitychange", function () {
      if (document.visibilityState === "hidden") unlisten(); else listen();
    });
  }

  if (window.__firebaseReady) boot();
  else window.addEventListener("firebaseReady", boot, { once: true });
})();
