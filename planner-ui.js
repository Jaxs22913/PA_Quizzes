/* Study planner UI for calendar.html. All logic lives in planner-engine.js;
 * this file only reads the calendar, keeps the student's record in
 * localStorage ("planner:v1", which cloud-sync mirrors when signed in) and draws
 * the Today / Plan / Stats / Settings panels.
 *
 * Test hook: calendar.html?asof=2026-09-28&now=17:30 pretends it is that day and
 * time and keeps its record under a separate key, so tests never touch a real
 * student's streak.
 */
(function () {
  "use strict";
  var E = window.PlannerEngine, cal = window.CalendarData, reg = window.Semesters;
  if (!E || !cal || !reg) return;

  /* ------------------------------------------------------------ basics -- */
  var qs = new URLSearchParams(location.search);
  var TEST = /^\d{4}-\d{2}-\d{2}$/.test(qs.get("asof") || "");
  function realToday() { var d = new Date(); return E.fmt(d); }
  var TODAY = TEST ? qs.get("asof") : realToday();
  function nowMin() {
    if (TEST && /^\d{1,2}:\d{2}$/.test(qs.get("now") || "")) { var p = qs.get("now").split(":"); return +p[0] * 60 + +p[1]; }
    var d = new Date(); return d.getHours() * 60 + d.getMinutes();
  }
  var KEY = "planner:v1" + (TEST ? ":test" : "");
  var DOW = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  var DOWL = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  var COLORS = ["--a-blue", "--a-violet", "--a-amber", "--a-teal", "--a-green", "--a-crimson", "--muted"];
  var CLASS_COLOR = { "cms-1": 0, "pdm-1": 1, "microbiology": 2, "pharm-1": 3, "physical-diagnosis-2": 4, "clin-path-1": 5, "med-lit": 6 };

  function $(id) { return document.getElementById(id); }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function icon(n, s) { return window.SiteIcon ? window.SiteIcon(n, s || 16) : ""; }
  function hm(min) {
    min = Math.round(min);
    if (min < 60) return min + " min";
    var h = Math.floor(min / 60), m = min % 60;
    return h + " h" + (m ? " " + m + " min" : "");
  }
  function clock(min) {
    var h = Math.floor(min / 60) % 24, m = min % 60, ap = h >= 12 ? "pm" : "am";
    return ((h % 12) || 12) + ":" + (m < 10 ? "0" : "") + m + " " + ap;
  }
  function toMin(v) { var p = String(v).split(":"); return (+p[0]) * 60 + (+p[1] || 0); }
  function toTime(m) { return (m < 600 ? "0" : "") + Math.floor(m / 60) + ":" + (m % 60 < 10 ? "0" : "") + (m % 60); }
  function dLabel(d, long) {
    var dt = E.parse(d);
    return dt.toLocaleDateString("en-US", long ? { weekday: "long", month: "long", day: "numeric" } : { weekday: "short", month: "short", day: "numeric" });
  }
  function relDay(d) {
    var n = E.diff(TODAY, d);
    return n === 0 ? "today" : n === 1 ? "tomorrow" : n === -1 ? "yesterday" : n > 0 ? "in " + n + " days" : -n + " days ago";
  }

  /* ----------------------------------------------------------- storage -- */
  var store;
  function fresh() { return { v: 1, created: TODAY, settings: {}, ovr: {}, days: {}, results: {}, ui: {} }; }
  function load() {
    try { var s = JSON.parse(localStorage.getItem(KEY)); if (s && s.v === 1) { s.settings = s.settings || {}; s.ovr = s.ovr || {}; s.days = s.days || {}; s.results = s.results || {}; s.ui = s.ui || {}; return s; } } catch (e) {}
    return fresh();
  }
  /* Nothing is written until the student actually does something. A blank record
     written on first visit to a second device would carry a newer timestamp than
     the one in the cloud, and cloud-sync would then overwrite the real history. */
  var touched = false;
  try { touched = localStorage.getItem(KEY) != null; } catch (e) {}
  function save() { if (!touched) return; try { localStorage.setItem(KEY, JSON.stringify(store)); } catch (e) {} }
  store = load();
  function cfg() { return E.settingsWith(store.settings); }

  /* ------------------------------------------------------------ exams -- */
  var semId = (function () {
    var cur = reg.current && reg.current();
    if (cur && cal.forSemester(cur.id).length) return cur.id;
    var w = reg.all.filter(function (s) { return cal.forSemester(s.id).length; });
    return w.length ? w[w.length - 1].id : null;
  })();
  var EVENTS = semId ? cal.forSemester(semId) : [];
  var RES = {};
  function examsFrom(from, c) { return E.deriveExams(EVENTS, from, c || cfg()); }
  function nameOf(x) { return x.t.replace(/\s*\(.*$/, "").replace(/^RETEST:\s*/i, "Retest: ").replace(/\s*-\s*EXAM\s*#?\s*/i, " Exam ").replace(/\s+/g, " ").trim(); }
  function colorOf(c) { var i = CLASS_COLOR[c]; return "var(" + COLORS[(i == null ? 0 : i) % COLORS.length] + ")"; }
  function resKey(x) { return x.c + "|" + (x.osce || x.practical ? "osce" : x.num); }

  /* ------------------------------------------------------------- tasks -- */
  var VERB = { firstpass: "Learn", review: "Review", final: "Practice" };
  function unitText(us) {
    if (!us || !us.length) return "";
    var lec = us.filter(function (u) { return u.kind === "lec"; }).map(function (u) { return u.n; }).sort(function (a, b) { return a - b; });
    var lab = us.filter(function (u) { return u.kind === "lab"; }).map(function (u) { return u.n; }).sort(function (a, b) { return a - b; });
    function runs(a, w) {
      if (!a.length) return "";
      var out = [], s = a[0], p = a[0];
      for (var i = 1; i <= a.length; i++) {
        if (a[i] === p + 1) { p = a[i]; continue; }
        out.push(s === p ? "" + s : s + "–" + p); s = a[i]; p = a[i];
      }
      return w + (a.length > 1 || out[0].indexOf("–") > -1 ? "s " : " ") + out.join(", ");
    }
    return [runs(lec, "lecture"), runs(lab, "lab")].filter(Boolean).join(" and ");
  }
  function taskTitle(t) {
    if (t.custom) return t.name;
    var u = unitText(t.units);
    if (t.kind === "firstpass") return u ? "Learn " + u : "Start practicing";
    if (t.kind === "review") return u ? "Review " + u + " from memory" : "Practice the routine again";
    return t.osce ? "Full run-through, timed" : "Mixed practice questions across the whole exam";
  }
  function taskHow(t) {
    if (t.custom) return "";
    if (t.kind === "firstpass") return "Read your notes once, then close them and write what you can recall. Fix gaps in the study guide.";
    if (t.kind === "review") return "Answer questions or write it out from memory first; only then check the guide. Testing yourself beats rereading.";
    return t.osce ? "Say every step and finding aloud, in order, without the sheet." : "Take a master exam or mixed quiz, then send every miss back to the guide.";
  }
  function isRealTask(t) { return !t.custom; }

  /* Turn one engine day into stored tasks. */
  function taskList(planned, examsById, day) {
    var nm = {}, out = [];
    planned.forEach(function (c, i) {
      var x = examsById[c.exam] || {};
      out.push({
        id: day + "|" + i, exam: c.exam, kind: c.kind, minutes: c.minutes, units: (c.units || []).map(function (u) { return { kind: u.kind, n: u.n }; }),
        start: c.start, end: c.end, part: c.part || "", done: false, logged: 0,
        ex: { name: nameOf(x), d: x.d, c: x.c, key: x.c ? resKey(x) : null }, osce: !!(x.practical)
      });
    });
    return out;
  }
  function byId(list) { var o = {}; list.forEach(function (x) { o[x.id] = x; }); return o; }
  function offMap() { var o = {}; Object.keys(store.days).forEach(function (d) { if (store.days[d].off) o[d] = true; }); return o; }
  function doneBefore(day) {
    var sub = {}; Object.keys(store.days).forEach(function (d) { if (d < day) sub[d] = store.days[d]; });
    return E.doneByExam(sub);
  }

  function materialize(day, keepDone) {
    var c = cfg(), exams = examsFrom(day, c), isToday = day === TODAY;
    var done = doneBefore(day), used = {};
    var keep = [];
    if (keepDone && store.days[day]) {
      keep = store.days[day].tasks.filter(function (t) { return t.done || t.custom; });
      keep.forEach(function (t) { if (t.exam) done[t.exam] = (done[t.exam] || 0) + Math.max(t.minutes || 0, t.logged || 0); });
      used[day] = keep.filter(function (t) { return t.done; }).reduce(function (a, t) { return a + t.minutes; }, 0);
    }
    var off = offMap(); delete off[day];
    var p = E.plan(exams, day, c, store.ovr, done, off, used, isToday ? nowMin() : null, store.created);
    var fresh = taskList(p.days[day] || [], byId(exams), day);
    if (keepDone) {
      var nextI = keep.length;
      fresh.forEach(function (t, i) { t.id = day + "|r" + Date.now().toString(36) + i; });
      return keep.concat(fresh);
    }
    return fresh;
  }

  /* Days from first use up to today each get a record, so a day that passed with
     nothing ticked really counts as missed (spending a freeze) -- but only back
     to first use, and never more than two weeks. */
  function ensureDays() {
    var from = store.created > TODAY ? TODAY : store.created, floor = E.add(TODAY, -14);
    if (from < floor) from = floor;
    var changed = false;
    E.range(from, TODAY).forEach(function (d) {
      if (!store.days[d]) { store.days[d] = { tasks: materialize(d, false) }; changed = true; }
    });
    if (changed) save();
  }

  /* --------------------------------------------------- plan (future) ---- */
  var cache = null, openDayOnce = null;   // never persisted: accordions open closed
  function futurePlan() {
    if (cache) return cache;
    var c = cfg(), exams = examsFrom(TODAY, c);
    var done = E.doneByExam(store.days), used = {}, rec = store.days[TODAY];
    if (rec && !rec.off) {
      rec.tasks.forEach(function (t) { if (t.exam && !t.done) done[t.exam] = (done[t.exam] || 0) + t.minutes; });
    }
    if (rec) used[TODAY] = 99999;
    var off = offMap();
    var p = E.plan(exams, TODAY, c, store.ovr, done, off, used, nowMin(), store.created);
    // What the plan believes each exam still needs, ignoring today's frozen list.
    var clean = E.plan(exams, TODAY, c, store.ovr, E.doneByExam(store.days), off, {}, nowMin(), store.created);
    cache = { exams: exams, plan: p, info: clean.info, shortfall: clean.shortfall, cfg: c };
    return cache;
  }
  function invalidate() { cache = null; }

  /* ---------------------------------------------------------- streaks --- */
  function streakState() { return E.replayStreak(store.days, TODAY, {}); }
  function dayStatus(d, S) {
    var rec = store.days[d];
    if (d > TODAY) return rec && rec.off ? "off" : "future";
    if (!rec) return "rest";
    if (rec.off) return "off";
    var real = rec.tasks.filter(isRealTask);
    if (!real.length) return "rest";
    var all = real.every(function (t) { return t.done; });
    if (all) return "done";
    if (d === TODAY) return real.some(function (t) { return t.done; }) ? "part" : "todo";
    return S.frozen.indexOf(d) > -1 ? "frozen" : "missed";
  }

  /* ---------------------------------------------------------- resources -- */
  function linksFor(t) {
    if (t.custom || !t.ex || !t.ex.key) return "";
    var r = RES[t.ex.key];
    if (!r) return "";
    var a = [];
    function L(href, label) { a.push('<a class="pl-link" href="' + esc(encodeURI(href)) + '">' + label + "</a>"); }
    function short(t) { t = String(t).replace(/\s+/g, " "); return t.length > 34 ? t.slice(0, 33).replace(/\s+\S*$/, "") + "\u2026" : t; }
    if (t.kind === "final") {
      if (r.master) L(r.master, "Master exam");
      if (r.cram) L(r.cram, "Cram sheet");
      (r.refs || []).slice(0, 2).forEach(function (x) { L(x.href, esc(short(x.t))); });
    } else if (t.kind === "review") {
      if (r.guide) L(r.guide, "Study guide");
      L("index.html", "Quizzes");
    } else {
      if (r.guide) L(r.guide, "Study guide");
      if (r.cram && t.kind !== "firstpass") L(r.cram, "Cram sheet");
    }
    if (t.osce) (r.refs || []).slice(0, 3).forEach(function (x) { L(x.href, esc(short(x.t))); });
    return a.join("");
  }

  /* ======================================================== TODAY panel == */
  function ringSvg(pct, big) {
    var R = 42, C = 2 * Math.PI * R, off = C * (1 - Math.max(0, Math.min(1, pct)));
    return '<svg class="pl-ring" viewBox="0 0 100 100" aria-hidden="true"><circle cx="50" cy="50" r="' + R + '" class="t"></circle>' +
      '<circle cx="50" cy="50" r="' + R + '" class="f" style="stroke-dasharray:' + C.toFixed(1) + ";stroke-dashoffset:" + off.toFixed(1) + '"></circle></svg>';
  }
  function weekStrip(S) {
    var mon = E.mondayOf(TODAY), out = "";
    for (var i = 0; i < 7; i++) {
      var d = E.add(mon, i), st = dayStatus(d, S);
      var sym = { done: icon("check", 13), frozen: icon("snow", 13), missed: icon("x", 13), off: icon("moon", 13), rest: "–", part: "◐", todo: "", future: "" }[st] || "";
      out += '<div class="pl-wd st-' + st + (d === TODAY ? " is-today" : "") + '" title="' + esc(dLabel(d) + ": " + ({ done: "finished", frozen: "missed, saved by a freeze", missed: "missed", off: "day off", rest: "no plan", part: "in progress", todo: "not started", future: "upcoming" }[st])) + '"><span class="pl-wd-n">' + DOW[E.dow(d)].charAt(0) + '</span><span class="pl-wd-d">' + sym + "</span></div>";
    }
    return '<div class="pl-week" aria-label="This week">' + out + "</div>";
  }
  function streakCard(S) {
    var next = S.every - S.progress;
    var msg = S.streak === 0 ? "Finish today's plan to start a streak." : S.todayDone ? "Today is safe. Come back tomorrow." : "Finish today's plan to keep it going.";
    var fz = "";
    for (var i = 0; i < 2; i++) fz += '<span class="pl-frz' + (i < S.freezes ? " on" : "") + '" title="Streak freeze">' + icon("snow", 14) + "</span>";
    return '<div class="pl-streak"><div class="pl-flame">' + icon("flame", 26) + '</div><div class="pl-sbody"><div class="pl-snum">' + S.streak + ' <small>day' + (S.streak === 1 ? "" : "s") + '</small></div><div class="pl-ssub">' + esc(msg) + "</div></div>" +
      '<div class="pl-sside"><div class="pl-frzrow" aria-label="' + S.freezes + ' streak freezes banked">' + fz + '</div><div class="pl-ssub">' + (S.freezes >= 2 ? "Freezes full" : next + " more finished day" + (next === 1 ? "" : "s") + " for a freeze") + "</div></div></div>" + weekStrip(S) +
      '<p class="pl-fine">A day counts when every task in its plan is ticked. Rest days and days off never break it. If you miss a day, a banked freeze covers it; you earn one for every ' + S.every + " finished days (keep up to 2). Best streak: " + S.best + ".</p>";
  }

  function overloadBanner(fp) {
    var short = 0, names = [];
    Object.keys(fp.shortfall).forEach(function (id) {
      var x = fp.exams.filter(function (e) { return e.id === id; })[0];
      if (x && x.d <= E.add(TODAY, 21) && fp.shortfall[id] >= 30) { short += fp.shortfall[id]; names.push(nameOf(x)); }
    });
    if (short < 30) return "";
    return '<div class="pl-warn" role="status"><b>' + icon("target", 15) + " More is due than your hours allow.</b> About " + hm(short) + " of the plan cannot fit before its exam" + (names.length > 1 ? "s" : "") + " (" + esc(names.slice(0, 3).join(", ")) + (names.length > 3 ? ", …" : "") + "). Nearer exams are filled first. " +
      '<button class="pl-btn small" data-act="more30" type="button">Add 30 min a day</button> <button class="pl-btn small ghost" data-go="settings" type="button">Change hours</button></div>';
  }

  function taskRow(t, day, editable) {
    var tm = t.start != null ? clock(t.start) + "–" + clock(t.end) : "";
    var timer = timerState && timerState.day === day && timerState.tid === t.id;
    var logged = t.logged ? " · " + hm(t.logged) + " timed" : "";
    return '<li class="pl-task' + (t.done ? " done" : "") + (t.custom ? " custom" : "") + '" data-tid="' + esc(t.id) + '" style="--c:' + (t.ex ? colorOf(t.ex.c) : "var(--a-teal)") + '">' +
      '<label class="pl-check"><input type="checkbox" data-act="tick" data-day="' + day + '" data-tid="' + esc(t.id) + '"' + (t.done ? " checked" : "") + (editable ? "" : " disabled") + ' aria-label="Mark done: ' + esc(taskTitle(t)) + '"><span class="pl-box">' + icon("check", 15) + "</span></label>" +
      '<div class="pl-tmain"><div class="pl-ttitle">' + esc(taskTitle(t)) + (t.part ? ' <span class="pl-part">' + esc(t.part) + "</span>" : "") + "</div>" +
      '<div class="pl-tmeta">' + (t.ex ? '<span class="pl-exname">' + esc(t.ex.name) + "</span> · " : "") + '<b>' + hm(t.minutes) + "</b>" + (tm ? " · " + tm : "") + esc(logged) + (t.ex && t.ex.d ? " · exam " + relDay(t.ex.d) : "") + "</div>" +
      (t.custom ? "" : '<details class="pl-how"><summary>How to do it</summary><p>' + esc(taskHow(t)) + "</p></details>") +
      '<div class="pl-tlinks">' + linksFor(t) + "</div></div>" +
      '<div class="pl-tact">' + (editable && !t.done ? '<button class="pl-btn small' + (timer ? " on" : "") + '" type="button" data-act="timer" data-day="' + day + '" data-tid="' + esc(t.id) + '">' + icon(timer ? "timer" : "play", 13) + (timer ? " Timing" : " Start") + "</button>" : "") +
      (t.custom && editable ? '<button class="pl-x" type="button" data-act="deltask" data-day="' + day + '" data-tid="' + esc(t.id) + '" aria-label="Delete task">' + icon("x", 13) + "</button>" : "") + "</div></li>";
  }

  function renderToday() {
    var host = $("pl-today"), fp = futurePlan(), S = streakState(), rec = store.days[TODAY] || { tasks: [] };
    var c = fp.cfg, win = E.windowOf(TODAY, c, nowMin(), true), full = E.windowOf(TODAY, c, null, false);
    var real = rec.tasks.filter(isRealTask), plannedMin = real.reduce(function (a, t) { return a + t.minutes; }, 0);
    var doneMin = real.filter(function (t) { return t.done; }).reduce(function (a, t) { return a + t.minutes; }, 0);
    var pct = plannedMin ? doneMin / plannedMin : 0;
    var todayExams = E.deriveExams(EVENTS, TODAY, c).filter(function (x) { return x.d === TODAY; });
    var h = "";

    var hero;
    if (rec.off) hero = ["Day off", "You took today off. It won't break your streak."];
    else if (!real.length) hero = [full ? "Nothing planned" : "Rest day", full ? "Nothing is due yet, or your study window has already closed." : "This is one of your rest days. Rest is part of the plan."];
    else if (pct >= 1) hero = ["All done", "That's today's plan finished. Nice work."];
    else hero = [hm(plannedMin - doneMin) + " to go", "of " + hm(plannedMin) + " planned" + (full ? " between " + clock(win ? win.start : full.start) + " and " + clock(full.end) : "") + "."];
    h += '<div class="pl-hero"><div class="pl-ringwrap">' + ringSvg(pct) + '<div class="pl-ringtxt">' + (plannedMin ? Math.round(pct * 100) + '<small>%</small>' : "\u2013") + '</div></div><div><div class="pl-date">' + esc(dLabel(TODAY, true)) + '</div><div class="pl-h2">' + esc(hero[0]) + '</div><div class="pl-ssub">' + esc(hero[1]) + "</div></div></div>";

    todayExams.forEach(function (x) { h += '<div class="pl-note good"><b>Exam today:</b> ' + esc(nameOf(x)) + ". You've done the work; sleep and a calm morning matter more than one more pass.</div>"; });
    h += overloadBanner(fp);
    if (rec.tasks.some(function (t) { return t.catchup; })) h += "";

    h += '<div class="pl-cols"><div class="pl-colmain">';
    h += '<div class="pl-sect"><h3>' + icon("list", 16) + ' Today\'s tasks</h3><span class="pl-sect-r">';
    h += '<button class="pl-btn small ghost" type="button" data-act="replan">' + icon("refresh", 13) + " Re-plan</button> ";
    h += '<button class="pl-btn small ghost" type="button" data-act="dayoff">' + icon("moon", 13) + (rec.off ? " Undo day off" : " Take today off") + "</button></span></div>";
    h += '<div id="pl-timer"></div>';
    if (rec.tasks.length) h += '<ul class="pl-tasks">' + rec.tasks.map(function (t) { return taskRow(t, TODAY, true); }).join("") + "</ul>";
    else h += '<div class="pl-empty">' + (rec.off ? "Enjoy the day off." : "No study tasks today.") + " Use " + '<button class="pl-link-btn" type="button" data-act="replan">Re-plan</button>' + " if you changed your hours, or add your own task below.</div>";
    h += '<form class="pl-add" data-act="addform"><input name="name" type="text" maxlength="80" placeholder="Add your own task (does not affect your streak)" aria-label="Task name"><input name="min" type="number" min="5" max="240" step="5" value="30" aria-label="Minutes"><button class="pl-btn" type="submit">' + icon("plus", 14) + " Add</button></form>";
    h += "</div>";
    h += '<div class="pl-colside">' + streakCard(S) + "</div></div>";

    // Coming up: the next study days and the next exam.
    var upcoming = fp.exams.filter(function (x) { return x.d > TODAY; }).slice(0, 3);
    h += '<div class="pl-sect"><h3>' + icon("calendar", 16) + " Next few days</h3></div><div class=\"pl-mini\">";
    for (var i = 1; i <= 4; i++) {
      var d = E.add(TODAY, i), ts = (store.days[d] && store.days[d].off) ? null : (fp.plan.days[d] || []), tot = ts ? ts.reduce(function (a, t) { return a + t.minutes; }, 0) : 0;
      h += '<button type="button" class="pl-minirow" data-go="plan" data-day="' + d + '"><span class="pl-minid">' + esc(dLabel(d)) + '</span><span class="pl-minib">' + (ts === null ? "Day off" : tot ? hm(tot) + " · " + ts.length + " task" + (ts.length === 1 ? "" : "s") : "Rest") + "</span></button>";
    }
    h += "</div>";
    if (upcoming.length) h += '<div class="pl-chips">' + upcoming.map(function (x) { return '<span class="pl-chip" style="--c:' + colorOf(x.c) + '"><i></i>' + esc(nameOf(x)) + " · " + dLabel(x.d) + " (" + relDay(x.d) + ")</span>"; }).join("") + "</div>";
    host.innerHTML = h;
    renderTimerBox();
  }

  /* ===================================================== focus timer ==== */
  var TKEY = "planner:timer:v1" + (TEST ? ":test" : "");
  var timerState = null, tick = null;
  try { timerState = JSON.parse(localStorage.getItem(TKEY)); } catch (e) {}
  if (timerState && timerState.day !== TODAY) timerState = null;
  function saveTimer() { try { if (timerState) localStorage.setItem(TKEY, JSON.stringify(timerState)); else localStorage.removeItem(TKEY); } catch (e) {} }
  function elapsedMs() { return timerState ? timerState.acc + (timerState.running ? Date.now() - timerState.since : 0) : 0; }
  function findTask(day, tid) { var r = store.days[day]; return r ? r.tasks.filter(function (t) { return t.id === tid; })[0] : null; }
  function fmtClock(ms) { var s = Math.max(0, Math.round(ms / 1000)), m = Math.floor(s / 60); return m + ":" + (s % 60 < 10 ? "0" : "") + (s % 60); }
  function commitTimer(markDone) {
    if (!timerState) return;
    var t = findTask(timerState.day, timerState.tid);
    var mins = Math.round(elapsedMs() / 60000);
    if (t) { t.logged = (t.logged || 0) + mins; if (markDone) t.done = true; }
    timerState = null; saveTimer(); clearInterval(tick); tick = null; document.title = baseTitle;
    save(); invalidate(); renderAll();
  }
  function renderTimerBox() {
    var box = $("pl-timer"); if (!box) return;
    if (!timerState) { box.innerHTML = ""; return; }
    var t = findTask(timerState.day, timerState.tid);
    if (!t) { timerState = null; saveTimer(); box.innerHTML = ""; return; }
    var total = timerState.total * 60000, left = total - elapsedMs(), over = left <= 0;
    box.innerHTML = '<div class="pl-timerbox' + (over ? " over" : "") + '"><div class="pl-tt">' + icon("timer", 16) + " Focus timer</div><div class=\"pl-tname\">" + esc(taskTitle(t)) + '</div><div class="pl-tclock" id="pl-tclock" role="timer">' + fmtClock(over ? -left : left) + '</div><div class="pl-tsub" id="pl-tsub">' + (over ? "Time's up. Tick it when you're actually finished, or keep going." : timerState.running ? "Focus. Phone away." : "Paused.") + '</div><div class="pl-trow">' +
      (over ? "" : '<button class="pl-btn" type="button" data-act="tpause">' + icon(timerState.running ? "pause" : "play", 14) + (timerState.running ? " Pause" : " Resume") + "</button>") +
      '<button class="pl-btn ok" type="button" data-act="tdone">' + icon("check", 14) + " Mark task done</button>" +
      '<button class="pl-btn ghost" type="button" data-act="tstop">Stop</button></div><p class="pl-fine">After a block, rest for ' + cfg().breakMin + " minutes. Stopping saves the minutes you timed; it never ticks the task for you.</p></div>";
    startTick();
  }
  var baseTitle = document.title;
  function startTick() {
    if (tick) return;
    tick = setInterval(function () {
      if (!timerState) { clearInterval(tick); tick = null; return; }
      var left = timerState.total * 60000 - elapsedMs(), c = $("pl-tclock");
      if (c) c.textContent = fmtClock(left < 0 ? -left : left);
      if (timerState.running) document.title = (left > 0 ? fmtClock(left) : "Time's up") + " · " + baseTitle;
      if (left <= 0 && !timerState.fired) { timerState.fired = true; saveTimer(); renderTimerBox(); }
    }, 1000);
  }
  function startTimer(day, tid) {
    var t = findTask(day, tid); if (!t) return;
    if (timerState && (timerState.day !== day || timerState.tid !== tid)) commitTimer(false);
    if (timerState && timerState.tid === tid) return;
    timerState = { day: day, tid: tid, total: Math.max(5, t.minutes - (t.logged || 0)), acc: 0, since: Date.now(), running: true, fired: false };
    saveTimer(); renderToday();
    var tb = $("pl-timer"); if (tb && tb.scrollIntoView) tb.scrollIntoView({ block: "nearest", behavior: "smooth" });
  }

  /* ========================================================= PLAN panel == */
  function stackedChart(days, exams, cap, opts) {
    opts = opts || {};
    var N = days.length, W = 700, Hh = 150, pad = 22, bw = (W - 8) / N, max = 60;
    days.forEach(function (d) { max = Math.max(max, (cap[d] || 0), (d.tot || 0)); });
    var totals = days.map(function (d) { return (opts.plan[d] || []).reduce(function (a, t) { return a + t.minutes; }, 0); });
    max = Math.max.apply(null, [60].concat(totals, days.map(function (d) { return cap[d] || 0; })));
    max = Math.ceil(max / 60) * 60;
    var colorFor = {}; exams.forEach(function (x) { colorFor[x.id] = colorOf(x.c); });
    var s = '<svg class="pl-chart" viewBox="0 0 ' + W + " " + (Hh + pad) + '" role="img" aria-label="Planned study minutes per day">';
    for (var g = 0; g <= max; g += 60) { var y = Hh - g / max * (Hh - 8); s += '<line x1="0" x2="' + W + '" y1="' + y + '" y2="' + y + '" class="grid"/>' + (g ? '<text x="' + (W - 2) + '" y="' + (y - 2) + '" class="lbl r">' + g / 60 + ' h</text>' : ""); }
    days.forEach(function (d, i) {
      var x = 4 + i * bw, yy = Hh, ts = opts.plan[d] || [];
      var rest = !cap[d];
      ts.forEach(function (t) { var hgt = t.minutes / max * (Hh - 8); yy -= hgt; s += '<rect x="' + (x + 1) + '" y="' + yy.toFixed(1) + '" width="' + Math.max(1, bw - 2).toFixed(1) + '" height="' + Math.max(0.5, hgt - 0.6).toFixed(1) + '" rx="1.5" fill="' + (colorFor[t.exam] || "var(--a-teal)") + '"><title>' + esc(dLabel(d) + " · " + hm(t.minutes)) + "</title></rect>"; });
      if (cap[d]) { var cy = Hh - cap[d] / max * (Hh - 8); s += '<line x1="' + (x + 1) + '" x2="' + (x + bw - 1) + '" y1="' + cy + '" y2="' + cy + '" class="cap"/>'; }
      if (d === TODAY) s += '<rect x="' + x + '" y="' + (Hh + 2) + '" width="' + bw + '" height="3" class="today"/>';
      var ex = exams.filter(function (e) { return e.d === d; });
      ex.forEach(function (e) { s += '<path d="M' + (x + bw / 2) + " " + (Hh + 3) + " l-4 8 h8 z\" fill=\"" + colorOf(e.c) + '"><title>' + esc(nameOf(e) + " exam") + "</title></path>"; });
      if ((E.dow(d) === 1 || i === 0) && !ex.length) s += '<text x="' + (x + bw / 2) + '" y="' + (Hh + 18) + '" class="lbl c">' + (E.parse(d).getMonth() + 1) + "/" + E.parse(d).getDate() + "</text>";
    });
    return s + "</svg>";
  }

  function examStatus(x, fp) {
    var info = fp.info[x.id] || {}, short = fp.shortfall[x.id] || 0, unrel = x.units.filter(function (u) { return u.date > TODAY; });
    var st = { cls: "ok", text: "On track" };
    if (short >= 30 && x.d <= E.add(TODAY, 28)) st = { cls: "bad", text: "Over capacity by " + hm(short) };
    else if (info.behindMin >= 45) st = { cls: "warn", text: "Behind: " + hm(info.behindMin) + " of catch-up scheduled" };
    var note = "";
    if (unrel.length) note = unrel.length + " of " + x.units.length + " lectures not delivered yet (next " + dLabel(unrel[0].date) + "). Those are planned for the days after they arrive.";
    return { st: st, note: note, info: info };
  }

  function examCard(x, fp) {
    var c = fp.cfg, o = store.ovr[x.id] || {}, s = examStatus(x, fp), info = s.info;
    var done = info.doneMin || 0, left = info.pendingMin || 0, total = done + left, pct = total ? Math.min(1, done / total) : 0;
    var r = RES[resKey(x)], has = r && (r.guide || r.cram || (r.refs && r.refs.length));
    var days = E.diff(TODAY, x.d), lec = x.units.length ? unitText(x.units) : "";
    return '<article class="pl-exam' + (o.off ? " is-off" : "") + '" style="--c:' + colorOf(x.c) + '"><div class="pl-etop"><div><div class="pl-ename">' + esc(nameOf(x)) + '</div><div class="pl-emeta">' + dLabel(x.d) + " · " + days + " day" + (days === 1 ? "" : "s") + (lec ? " · " + esc(lec) : x.practical ? " · practical" : "") + '</div></div><span class="pl-badge ' + (o.off ? "off" : s.st.cls) + '">' + (o.off ? "Not planned" : esc(s.st.text)) + "</span></div>" +
      (o.off ? "" : '<div class="pl-ebar"><i style="width:' + Math.round(pct * 100) + '%"></i></div><div class="pl-emeta">' + hm(done) + " done \u00b7 " + hm(left) + " still planned" + (has ? "" : " · no study pages posted yet") + "</div>") +
      (s.note && !o.off ? '<div class="pl-enote">' + icon("clock", 13) + " " + esc(s.note) + "</div>" : "") +
      '<details class="pl-eopt"><summary>' + icon("sliders", 13) + " Adjust this exam</summary><div class=\"pl-eform\">" +
      '<label>Total hours<input type="number" min="1" max="60" step="0.5" data-ex="' + esc(x.id) + '" data-k="hours" value="' + (o.hours != null ? o.hours : "") + '" placeholder="auto (' + (Math.round(E.examHours(x, c, {}) * 10) / 10) + ')"></label>' +
      '<label>How hard is it?<select data-ex="' + esc(x.id) + '" data-k="difficulty">' + [[0.75, "Easier"], [1, "Normal"], [1.25, "Harder"], [1.5, "Very hard"]].map(function (v) { return '<option value="' + v[0] + '"' + ((o.difficulty || 1) === v[0] ? " selected" : "") + ">" + v[1] + "</option>"; }).join("") + "</select></label>" +
      '<label>Start studying on<input type="date" data-ex="' + esc(x.id) + '" data-k="start" value="' + (o.start || "") + '" max="' + E.add(x.d, -1) + '"></label>' +
      '<label class="row"><input type="checkbox" data-ex="' + esc(x.id) + '" data-k="fresh"' + (o.fresh ? " checked" : "") + '> I haven\'t started this one</label>' +
      '<label class="row"><input type="checkbox" data-ex="' + esc(x.id) + '" data-k="off"' + (o.off ? " checked" : "") + "> Don't plan this exam</label>" +
      '<button class="pl-btn small ghost" type="button" data-act="resetex" data-ex="' + esc(x.id) + '">Reset</button></div></details></article>';
  }

  function renderPlan() {
    var host = $("pl-plan"), fp = futurePlan(), c = fp.cfg, S = null;
    var view = store.ui.horizon || 28;
    var range = E.range(TODAY, E.add(TODAY, view - 1)), capMap = {};
    range.forEach(function (d) { capMap[d] = (store.days[d] && store.days[d].off) ? 0 : E.capOf(E.windowOf(d, c, nowMin(), d === TODAY), c); });
    var planDays = {}; range.forEach(function (d) { planDays[d] = (d === TODAY && store.days[TODAY]) ? store.days[TODAY].tasks.filter(isRealTask) : (fp.plan.days[d] || []); });
    var h = overloadBanner(fp);
    var cr = E.crunches(fp.exams.filter(function (x) { return !(store.ovr[x.id] && store.ovr[x.id].off); }), 5, 3);
    cr.slice(0, 2).forEach(function (k) { h += '<div class="pl-note"><b>' + icon("flag", 14) + " Crunch:</b> " + k.count + " graded dates between " + dLabel(k.from) + " and " + dLabel(k.to) + ". The plan starts these early and works on the nearest one first.</div>"; });

    h += '<div class="pl-sect"><h3>' + icon("chart", 16) + " Study load</h3><span class=\"pl-sect-r\">" + [14, 28, 56].map(function (n) { return '<button class="pl-seg' + (view === n ? " on" : "") + '" type="button" data-act="horizon" data-n="' + n + '">' + n / 7 + " wk</button>"; }).join("") + "</span></div>";
    h += stackedChart(range, fp.exams, capMap, { plan: planDays });
    h += '<div class="pl-legend">' + fp.exams.filter(function (x) { return x.d <= E.add(TODAY, view + 14); }).slice(0, 9).map(function (x) { return '<span class="pl-chip" style="--c:' + colorOf(x.c) + '"><i></i>' + esc(nameOf(x)) + "</span>"; }).join("") + '</div><p class="pl-fine">Bars are planned study time, coloured by exam; the dashed line is your daily limit from the study window in Settings; triangles mark exam dates.</p>';

    h += '<div class="pl-sect"><h3>' + icon("list", 16) + " Day by day</h3></div><div class=\"pl-days\">";
    range.slice(0, Math.min(view, 21)).forEach(function (d) {
      var rec = store.days[d], ts = planDays[d], off = rec && rec.off, tot = ts.reduce(function (a, t) { return a + t.minutes; }, 0);
      var win = E.windowOf(d, c, null, false);
      h += '<details class="pl-dayrow' + (d === TODAY ? " is-today" : "") + '" id="d-' + d + '"' + '><summary><span class="pl-dd">' + esc(dLabel(d)) + '</span><span class="pl-dtot">' + (off ? "Day off" : tot ? hm(tot) : win ? "Nothing due" : "Rest day") + '</span>' +
        '<span class="pl-dchips">' + ts.reduce(function (a, t) { if (a.indexOf(t.exam) < 0) a.push(t.exam); return a; }, []).slice(0, 4).map(function (id) { var x = fp.exams.filter(function (e) { return e.id === id; })[0]; return x ? '<i style="background:' + colorOf(x.c) + '"></i>' : ""; }).join("") + "</span></summary>";
      if (ts.length) {
        h += '<ul class="pl-plist">' + ts.map(function (t) {
          var x = fp.exams.filter(function (e) { return e.id === t.exam; })[0] || {};
          var tk = t.ex ? t : { exam: t.exam, kind: t.kind, minutes: t.minutes, units: t.units, start: t.start, end: t.end, part: t.part, ex: { name: nameOf(x) } };
          return '<li style="--c:' + colorOf(x.c || (t.ex && t.ex.c)) + '"><i></i><span><b>' + esc(taskTitle(tk)) + "</b> · " + esc(tk.ex.name) + '</span><span class="pl-t">' + hm(t.minutes) + (t.start != null ? " · " + clock(t.start) : "") + "</span></li>";
        }).join("") + "</ul>";
      }
      if (d >= TODAY) h += '<div class="pl-dayacts"><button class="pl-btn small ghost" type="button" data-act="dayoffd" data-day="' + d + '">' + icon("moon", 13) + (off ? " Undo day off" : " Take this day off") + "</button></div>";
      h += "</details>";
    });
    h += "</div>";

    h += '<div class="pl-sect"><h3>' + icon("target", 16) + " Your exams</h3><span class=\"pl-sect-r\"><button class=\"pl-btn small ghost\" type=\"button\" data-act=\"ics\">" + icon("download", 13) + " Add study blocks to my calendar</button></span></div>";
    h += '<div class="pl-exams">' + (fp.exams.filter(function (x) { return x.d > TODAY; }).map(function (x) { return examCard(x, fp); }).join("") || '<div class="pl-empty">No upcoming exams on the calendar.</div>') + "</div>";
    var skipped = fp.exams.filter(function (x) { return x.d > TODAY; }).length;
    if (!c.planRetests) h += '<p class="pl-fine">Retests and course remediation are shown on the calendar but not planned. Turn on "Plan for retests too" in Settings if you want them included.</p>';
    host.innerHTML = h;
    var jump = openDayOnce && $("d-" + openDayOnce); if (jump) jump.open = true;   // only after a "next few days" tap
  }

  /* ======================================================== STATS panel == */
  function renderStats() {
    var host = $("pl-stats"), S = streakState(), days = store.days;
    var weeks = E.weeklyMinutes(days, TODAY, 8), maxW = Math.max.apply(null, [60].concat(weeks.map(function (w) { return w.minutes; })));
    var total = 0, active = 0; Object.keys(days).forEach(function (d) { var m = E.doneMinutes(days[d]); total += m; if (m > 0) active++; });
    var thisWeek = weeks[weeks.length - 1].minutes, last = weeks.length > 1 ? weeks[weeks.length - 2].minutes : 0;
    var h = '<div class="pl-tiles">' + [["Current streak", S.streak + " d"], ["Best streak", S.best + " d"], ["This week", hm(thisWeek)], ["All time", hm(total)], ["Days studied", active], ["Freezes", S.freezes + " / 2"]].map(function (t) { return '<div class="pl-tile"><div class="pl-tn">' + t[1] + '</div><div class="pl-tl">' + t[0] + "</div></div>"; }).join("") + "</div>";
    h += '<div class="pl-sect"><h3>' + icon("chart", 16) + " Last 8 weeks</h3></div><div class=\"pl-wk\">" + weeks.map(function (w, i) { return '<div class="pl-wkc" title="' + esc("Week of " + dLabel(w.start) + ": " + hm(w.minutes)) + '"><div class="pl-wkbar"><i style="height:' + Math.round(w.minutes / maxW * 100) + '%"></i></div><span>' + (E.parse(w.start).getMonth() + 1) + "/" + E.parse(w.start).getDate() + "</span></div>"; }).join("") + "</div>";
    h += '<p class="pl-fine">' + (thisWeek >= last ? "This week is at or above last week." : "This week is behind last week so far.") + " Only ticked tasks and timed minutes count.</p>";

    // by exam
    var byEx = {}, names = {}, dates = {};
    Object.keys(days).forEach(function (d) { days[d].tasks.forEach(function (t) { if (!t.exam || !t.ex) return; byEx[t.exam] = (byEx[t.exam] || 0) + (t.done ? Math.max(t.minutes, t.logged || 0) : (t.logged || 0)); names[t.exam] = t.ex; }); });
    var ids = Object.keys(names).sort(function (a, b) { return names[a].d < names[b].d ? -1 : 1; });
    h += '<div class="pl-sect"><h3>' + icon("book", 16) + " Time by exam</h3></div>";
    if (!ids.length) h += '<div class="pl-empty">Nothing logged yet. Tick a task on the Today tab and it shows up here.</div>';
    else {
      h += '<div class="pl-results">' + ids.map(function (id) {
        var ex = names[id], past = ex.d <= TODAY, r = store.results[id];
        return '<div class="pl-resrow" style="--c:' + colorOf(ex.c) + '"><span class="pl-exname"><i></i>' + esc(ex.name) + '</span><span class="pl-emeta">' + dLabel(ex.d) + " · " + hm(byEx[id] || 0) + " studied</span>" +
          (past ? '<label class="pl-score">Score <input type="number" min="0" max="100" step="0.1" inputmode="decimal" data-res="' + esc(id) + '" value="' + (r ? r.score : "") + '" placeholder="%"></label>' : '<span class="pl-emeta">upcoming</span>') + "</div>";
      }).join("") + "</div>";
      var withScore = ids.filter(function (id) { return store.results[id] && store.results[id].score != null && byEx[id]; });
      if (withScore.length >= 2) {
        var rows = withScore.map(function (id) { return { h: byEx[id] / 60, s: +store.results[id].score }; });
        h += '<p class="pl-fine">' + rows.length + " exams logged. Hours per point is a rough guide only; exams differ in size and difficulty.</p>";
      } else h += '<p class="pl-fine">After an exam, enter your score. Once you have a few, this page shows how your hours related to your results.</p>';
    }
    host.innerHTML = h;
  }

  /* ===================================================== SETTINGS panel == */
  var FIELDS = [
    ["hoursPerLecture", "Hours per lecture", 0.5, 6, 0.25, "Total out-of-class study for each lecture or lab an exam covers, spread over the weeks before it."],
    ["minHours", "Least hours per exam", 1, 20, 0.5, "Even a short exam gets at least this much."],
    ["maxHours", "Most hours per exam", 4, 60, 1, "Caps very large exams."],
    ["startWeeks", "Start studying (weeks before)", 1, 10, 1, "Lectures already delivered are staggered across the start of this window, so far-off exams begin light."],
    ["firstPassShare", "Share right after each lecture", 0.05, 0.7, 0.05, "Fraction of a lecture's hours spent in the first days after it is delivered."],
    ["firstPassDays", "Days to finish first pass", 1, 7, 1, "How long after a lecture the first pass may slide."],
    ["reviewGapPct", "Review spacing", 0.05, 0.5, 0.05, "Gap between reviews as a fraction of the days left. 0.20 is the research-supported default for weeks-scale exams."],
    ["finalWeekShare", "Share kept for the final days", 0.05, 0.7, 0.05, "Hours reserved for whole-exam practice near the exam."],
    ["finalDays", "Final-phase length (days)", 2, 14, 1, "How many days before the exam count as the final phase."],
    ["rampPower", "Ramp shape", 1, 3, 0.1, "1 is flat; higher pushes more study toward the exam. 1.6 is a gentle ramp."],
    ["taperLastDayMin", "Day before the exam (min)", 0, 180, 15, "A short, light session so you arrive rested."],
    ["practicalHours", "Hours for a practical / OSCE", 2, 30, 1, "Practicals have no lecture list, so they get this total."],
    ["practicalLead", "Practical lead-in (days)", 7, 42, 1, "How many days before a practical to begin practicing."],
    ["maxBlock", "Longest task (min)", 20, 120, 5, "Longer work is split into sessions of this length or less."],
    ["minBlock", "Shortest task (min)", 5, 45, 5, ""],
    ["breakMin", "Break after each block (min)", 0, 30, 5, "Reserved out of your study window, so a 3-hour window holds less than 3 hours of focus."],
    ["dayMax", "Most focused minutes in a day", 60, 480, 15, "A hard ceiling, however long your window is."]
  ];

  function settingsPreviewData() {
    invalidate();
    var fp = futurePlan(), c = fp.cfg, range = E.range(TODAY, E.add(TODAY, 34)), capMap = {}, pd = {};
    range.forEach(function (d) { capMap[d] = (store.days[d] && store.days[d].off) ? 0 : E.capOf(E.windowOf(d, c, nowMin(), d === TODAY), c); pd[d] = (d === TODAY && store.days[TODAY]) ? store.days[TODAY].tasks.filter(isRealTask) : (fp.plan.days[d] || []); });
    var short = 0; Object.keys(fp.shortfall).forEach(function (k) { short += fp.shortfall[k]; });
    var planned = 0; range.forEach(function (d) { planned += pd[d].reduce(function (a, t) { return a + t.minutes; }, 0); });
    var week = 0; range.slice(0, 7).forEach(function (d) { week += pd[d].reduce(function (a, t) { return a + t.minutes; }, 0); });
    return { fp: fp, range: range, cap: capMap, plan: pd, short: short, week: week };
  }
  function renderPreview() {
    var box = $("pl-preview"); if (!box) return;
    var P = settingsPreviewData();
    box.innerHTML = stackedChart(P.range, P.fp.exams, P.cap, { plan: P.plan }) + '<p class="pl-fine"><b>Next 7 days: ' + hm(P.week) + " planned.</b> " + (P.short >= 30 ? "About " + hm(P.short) + " across all exams does not fit in your hours yet." : "Everything fits inside your hours.") + "</p>";
    var sums = document.querySelectorAll("[data-focus]");
    for (var i = 0; i < sums.length; i++) {
      var dw = +sums[i].getAttribute("data-focus"), w = cfg().win[dw];
      sums[i].textContent = w.on ? hm(E.capOf({ start: w.start, end: w.end }, cfg())) + " focus" : "rest day";
    }
  }
  function presetMatch() {
    var s = store.settings, keys = Object.keys(s).filter(function (k) { return k !== "win"; });
    if (!keys.length) return "balanced";
    var hit = null;
    Object.keys(E.PRESETS).forEach(function (id) {
      var p = E.PRESETS[id].p, pk = Object.keys(p);
      if (pk.length === keys.length && pk.every(function (k) { return s[k] === p[k]; })) hit = id;
    });
    return hit || "custom";
  }
  function renderSettings() {
    var host = $("pl-settings"), c = cfg(), cur = presetMatch();
    var h = '<div class="pl-sect"><h3>' + icon("sliders", 16) + " How the plan is built</h3></div><p class=\"pl-fine top\">Pick a style, then fine-tune anything. The chart at the bottom redraws with your next five weeks as you change things.</p>";
    h += '<div class="pl-presets">' + Object.keys(E.PRESETS).map(function (id) { var p = E.PRESETS[id]; return '<button type="button" class="pl-preset' + (cur === id ? " on" : "") + '" data-act="preset" data-id="' + id + '"><b>' + p.label + "</b><span>" + esc(p.note) + "</span></button>"; }).join("") + (cur === "custom" ? '<div class="pl-preset on"><b>Custom</b><span>Your own numbers.</span></div>' : "") + "</div>";

    h += '<div class="pl-sect"><h3>' + icon("clock", 16) + " When you study</h3></div><p class=\"pl-fine top\">Set the time you usually start and when you stop for the day. Tasks are placed inside this window, today's plan only uses the time still left in it, and the hours you can fit set how much can be scheduled.</p>";
    h += '<div class="pl-win">' + [1, 2, 3, 4, 5, 6, 0].map(function (dw) {
      var w = c.win[dw];
      return '<div class="pl-winrow' + (w.on ? "" : " off") + '"><label class="pl-winday"><input type="checkbox" data-win="' + dw + '" data-k="on"' + (w.on ? " checked" : "") + "> " + DOWL[dw] + '</label><label>Start<input type="time" step="300" data-win="' + dw + '" data-k="start" value="' + toTime(w.start) + '"></label><label>Quit<input type="time" step="300" data-win="' + dw + '" data-k="end" value="' + toTime(w.end) + '"></label><span class="pl-focus" data-focus="' + dw + '"></span></div>';
    }).join("") + "</div>";
    h += '<p class="pl-fine">Turn a day off to make it a rest day (recommended: one a week). Tick "Copy Monday to weekdays" to save typing.</p><button class="pl-btn small ghost" type="button" data-act="copymon">Copy Monday to all weekdays</button>';

    h += '<div class="pl-sect"><h3>' + icon("target", 16) + " Fine-tune the algorithm</h3></div><div class=\"pl-fields\">" + FIELDS.map(function (f) {
      var v = c[f[0]];
      return '<label class="pl-field"><span class="pl-fl">' + f[1] + '</span><input type="number" data-set="' + f[0] + '" min="' + f[2] + '" max="' + f[3] + '" step="' + f[4] + '" value="' + v + '"><span class="pl-fh">' + esc(f[5]) + "</span></label>";
    }).join("") + "</div>";
    h += '<label class="pl-toggle"><input type="checkbox" data-set="planRetests"' + (c.planRetests ? " checked" : "") + "> Plan for retests and remediation too</label>";

    h += '<div class="pl-sect"><h3>' + icon("chart", 16) + " Preview</h3></div><div id=\"pl-preview\"></div>";
    h += '<div class="pl-sect"><h3>' + icon("book", 16) + ' Why it works this way</h3></div><div class="pl-why"><ul>' +
      "<li><b>Study follows delivery.</b> Content arrives lecture by lecture, so nothing is scheduled before it exists. Each lecture gets a first pass soon after it is delivered, then spaced reviews. The last week is practice on the whole exam, since new material keeps arriving until then.</li>" +
      "<li><b>Spaced beats massed.</b> Spreading the same hours out is one of the best-supported ways to remember (Dunlosky et al. 2013); the best gap grows with the time to the test, roughly 20% of it for exams weeks away (Cepeda et al. 2008).</li>" +
      "<li><b>Testing beats rereading.</b> Reviews and final-week tasks are done as questions and recall first, guide second.</li>" +
      "<li><b>Light early, heavier late.</b> Far exams start with small sessions; the closest exam is served first. A short session the day before keeps you rested.</li>" +
      "<li><b>Forgiving streak.</b> One missed day barely changes how a habit forms (Lally et al. 2010), and harsh streaks make people quit after a break, so freezes and rest days protect it.</li>" +
      "<li><b>Honest limits.</b> No study proves a right number of hours for a PA exam. These are defaults you can change, and when the hours do not fit the plan says so instead of hiding it.</li></ul></div>";
    h += '<div class="pl-sect"><h3>Reset</h3></div><div class="pl-rowbtns"><button class="pl-btn small ghost" type="button" data-act="resetset">Reset settings to defaults</button><button class="pl-btn small ghost danger" type="button" data-act="resetall">Erase my planner history</button></div>';
    host.innerHTML = h;
    renderPreview();
  }

  /* ============================================================= .ics === */
  function icsExport() {
    var fp = futurePlan(), lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//PA Quizzes//Study planner//EN", "CALSCALE:GREGORIAN"];
    function stamp(d, m) { return d.replace(/-/g, "") + "T" + ("0" + Math.floor(m / 60)).slice(-2) + ("0" + m % 60).slice(-2) + "00"; }
    E.range(TODAY, E.add(TODAY, 20)).forEach(function (d) {
      var ts = (d === TODAY && store.days[TODAY]) ? store.days[TODAY].tasks.filter(function (t) { return isRealTask(t) && !t.done; }) : (fp.plan.days[d] || []);
      ts.forEach(function (t, i) {
        if (t.start == null) return;
        var x = fp.exams.filter(function (e) { return e.id === t.exam; })[0] || {}, tk = t.ex ? t : { exam: t.exam, kind: t.kind, units: t.units, minutes: t.minutes, ex: { name: nameOf(x) } };
        lines.push("BEGIN:VEVENT", "UID:" + d + "-" + i + "-" + String(t.exam).replace(/[^a-z0-9]/gi, "") + "@paquizzes", "DTSTAMP:" + stamp(TODAY, 0) + "Z", "DTSTART:" + stamp(d, t.start), "DTEND:" + stamp(d, t.end),
          "SUMMARY:" + ("Study: " + taskTitle(tk) + " (" + tk.ex.name + ")").replace(/[,;]/g, " "), "END:VEVENT");
      });
    });
    lines.push("END:VCALENDAR");
    var blob = new Blob([lines.join("\r\n")], { type: "text/calendar" }), a = document.createElement("a");
    a.href = URL.createObjectURL(blob); a.download = "study-plan.ics"; document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }

  /* ============================================================ events == */
  function setTab(id, focus) {
    var names = ["today", "plan", "calendar", "stats", "settings"];
    if (names.indexOf(id) < 0) id = "today";
    names.forEach(function (n) {
      var p = $("pl-panel-" + n), b = document.querySelector('[data-tab="' + n + '"]');
      if (p) p.hidden = n !== id;
      if (b) { b.classList.toggle("on", n === id); b.setAttribute("aria-selected", n === id ? "true" : "false"); if (n === id && b.scrollIntoView) b.scrollIntoView({ inline: "center", block: "nearest" }); }
    });
    store.ui.tab = id; try { history.replaceState(null, "", "#" + id + (TEST ? location.search : "")); } catch (e) {}
    if (id === "settings") renderSettings();
    if (id === "calendar" && window.PlannerCalendarHook) window.PlannerCalendarHook();
    window.scrollTo(0, 0);
  }
  function renderAll() {
    invalidate();
    renderToday(); renderPlan(); renderStats();
    if (!$("pl-panel-settings").hidden) renderSettings();
    if (window.PlannerCalendarHook) window.PlannerCalendarHook();
  }

  function findEx(id) { return futurePlan().exams.filter(function (x) { return x.id === id; })[0]; }
  function setOvr(id, k, v) {
    var o = store.ovr[id] = store.ovr[id] || {};
    if (v === "" || v == null || v === false || (k === "difficulty" && +v === 1)) delete o[k]; else o[k] = (k === "hours" || k === "difficulty") ? +v : v;
    if (!Object.keys(o).length) delete store.ovr[id];
  }
  function replan(keepDone) {
    var rec = store.days[TODAY] || (store.days[TODAY] = { tasks: [] });
    rec.tasks = materialize(TODAY, true);
    save();
  }

  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-act],[data-go],[data-tab]"); if (!t) return;
    if (t.hasAttribute("data-tab")) { setTab(t.getAttribute("data-tab")); return; }
    if (t.hasAttribute("data-go")) { if (t.getAttribute("data-day")) openDayOnce = t.getAttribute("data-day"); setTab(t.getAttribute("data-go")); if (t.getAttribute("data-day")) { renderPlan(); var el = $("d-" + t.getAttribute("data-day")); if (el) { el.open = true; el.scrollIntoView({ block: "center" }); } openDayOnce = null; } return; }
    var act = t.getAttribute("data-act");
    var day = t.getAttribute("data-day"), tid = t.getAttribute("data-tid");
    touched = true;
    if (act === "timer") { startTimer(day, tid); }
    else if (act === "tpause") { if (timerState) { if (timerState.running) { timerState.acc += Date.now() - timerState.since; timerState.running = false; } else { timerState.since = Date.now(); timerState.running = true; } saveTimer(); renderTimerBox(); } }
    else if (act === "tdone") commitTimer(true);
    else if (act === "tstop") commitTimer(false);
    else if (act === "deltask") { var r = store.days[day]; r.tasks = r.tasks.filter(function (x) { return x.id !== tid; }); save(); renderAll(); }
    else if (act === "replan") { replan(); renderAll(); }
    else if (act === "dayoff") { var rec = store.days[TODAY] || (store.days[TODAY] = { tasks: [] }); rec.off = !rec.off; if (!rec.off) rec.tasks = materialize(TODAY, true); save(); renderAll(); }
    else if (act === "dayoffd") { var rd = store.days[day]; if (!rd) rd = store.days[day] = { tasks: [] }; rd.off = !rd.off; if (!rd.off && !rd.tasks.length && day > TODAY) delete store.days[day]; save(); renderAll(); }
    else if (act === "horizon") { store.ui.horizon = +t.getAttribute("data-n"); save(); renderPlan(); }
    else if (act === "more30") { var c2 = cfg(), w = c2.win.map(function (x) { return { on: x.on, start: x.start, end: x.end }; }); w.forEach(function (x) { if (x.on) x.end = Math.min(1439, x.end + 30); }); store.settings.win = w; save(); replan(); renderAll(); }
    else if (act === "preset") { var p = E.PRESETS[t.getAttribute("data-id")].p, keep = store.settings.win; store.settings = {}; Object.keys(p).forEach(function (k) { store.settings[k] = p[k]; }); if (keep) store.settings.win = keep; save(); renderAll(); }
    else if (act === "copymon") { var cc = cfg(), m = cc.win[1], nw = cc.win.map(function (x, i) { return i >= 1 && i <= 5 ? { on: m.on, start: m.start, end: m.end } : { on: x.on, start: x.start, end: x.end }; }); store.settings.win = nw; save(); renderAll(); }
    else if (act === "resetset") { store.settings = {}; save(); renderAll(); }
    else if (act === "resetall") { if (confirm("Erase your streak, task history and settings? This can't be undone.")) { store = fresh(); save(); timerState = null; saveTimer(); ensureDays(); renderAll(); } }
    else if (act === "resetex") { delete store.ovr[t.getAttribute("data-ex")]; save(); renderAll(); }
    else if (act === "ics") icsExport();
  });
  document.addEventListener("change", function (e) {
    var t = e.target; touched = true;
    if (t.getAttribute("data-act") === "tick") {
      var tk = findTask(t.getAttribute("data-day"), t.getAttribute("data-tid")); if (!tk) return;
      var wasDone = streakState().todayDone;
      tk.done = t.checked; save(); renderAll();
      if (!wasDone && streakState().todayDone) celebrate();
    } else if (t.hasAttribute("data-set")) {
      var k = t.getAttribute("data-set"), v = t.type === "checkbox" ? t.checked : parseFloat(t.value);
      if (t.type !== "checkbox" && isNaN(v)) return;
      if (t.type !== "checkbox") v = Math.min(+t.max, Math.max(+t.min, v));
      if (v === E.DEFAULTS[k]) delete store.settings[k]; else store.settings[k] = v;
      save(); invalidate(); renderPreview(); renderPlan(); renderToday();
      var pr = document.querySelector(".pl-presets"); if (pr) { var cur = presetMatch(); [].forEach.call(pr.querySelectorAll(".pl-preset"), function (b) { b.classList.toggle("on", b.getAttribute("data-id") === cur); }); }
    } else if (t.hasAttribute("data-win")) {
      var dw = +t.getAttribute("data-win"), kk = t.getAttribute("data-k"), win = cfg().win.map(function (x) { return { on: x.on, start: x.start, end: x.end }; });
      if (kk === "on") win[dw].on = t.checked; else win[dw][kk] = toMin(t.value);
      if (win[dw].end <= win[dw].start + 10) { win[dw].end = Math.min(1439, win[dw].start + 60); var inp = document.querySelector('[data-win="' + dw + '"][data-k="end"]'); if (inp) inp.value = toTime(win[dw].end); }
      store.settings.win = win; save(); t.closest(".pl-winrow").classList.toggle("off", !win[dw].on); invalidate(); renderPreview();
      if (dw === E.dow(TODAY)) { renderToday(); }
      renderPlan();
    } else if (t.hasAttribute("data-ex")) {
      var kx = t.getAttribute("data-k"); setOvr(t.getAttribute("data-ex"), kx, (kx === "off" || kx === "fresh") ? t.checked : t.value); save(); renderAll();
    } else if (t.hasAttribute("data-res")) {
      var id = t.getAttribute("data-res"); if (t.value === "") delete store.results[id]; else store.results[id] = { score: Math.max(0, Math.min(100, +t.value)) }; save(); renderStats();
    }
  });
  document.addEventListener("submit", function (e) {
    var f = e.target; if (f.getAttribute("data-act") !== "addform") return; e.preventDefault(); touched = true;
    var name = f.name.value.trim(), min = +f.min.value; if (!name || !(min > 0)) return;
    var rec = store.days[TODAY] || (store.days[TODAY] = { tasks: [] });
    rec.tasks.push({ id: TODAY + "|c" + Date.now().toString(36), custom: true, name: name, minutes: min, done: false, logged: 0 });
    save(); renderAll();
  });

  function celebrate() {
    var S = streakState(), el = document.createElement("div");
    el.className = "pl-toast"; el.setAttribute("role", "status");
    el.innerHTML = icon("flame", 18) + " <b>Day complete.</b> " + S.streak + "-day streak" + (S.freezes ? " · " + S.freezes + " freeze" + (S.freezes > 1 ? "s" : "") + " banked" : "") + ".";
    document.body.appendChild(el);
    if (window.SiteConfetti) try { window.SiteConfetti(); } catch (x) {}
    setTimeout(function () { el.classList.add("out"); setTimeout(function () { el.remove(); }, 400); }, 3200);
  }

  /* ============================================================== boot == */
  function boot() {
    fetch("planner-resources.json").then(function (r) { return r.ok ? r.json() : {}; }).catch(function () { return {}; }).then(function (j) {
      RES = j || {}; ensureDays(); renderAll();
    });
    ensureDays(); renderAll();
    var h = (location.hash || "").replace("#", "");
    setTab(h || "today");
    if (timerState) { renderTimerBox(); }
    document.addEventListener("visibilitychange", function () { if (!document.hidden && !TEST && realToday() !== TODAY) location.reload(); });
  }
  window.PlannerUI = {
    dayInfo: function (d) {
      var rec = store.days[d]; if (rec && rec.tasks && rec.tasks.length) { var real = rec.tasks.filter(isRealTask); return { minutes: real.reduce(function (a, t) { return a + t.minutes; }, 0), done: real.length && real.every(function (t) { return t.done; }) }; }
      if (d >= TODAY) { var fp = futurePlan(), ts = fp.plan.days[d]; if (ts && ts.length) return { minutes: ts.reduce(function (a, t) { return a + t.minutes; }, 0), done: false, planned: true }; }
      return null;
    },
    setTab: setTab, hm: hm
  };
  boot();
})();
