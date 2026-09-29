/* Focus timer that follows the student around the site.
 *
 * The planner (calendar.html) starts a countdown for a task and keeps it in localStorage under
 * "planner:timer:v1". This file, loaded by theme.js on every page while that key exists, draws a
 * small pill in the top-left corner so the timer stays visible on quizzes, guides and the
 * homepage. It goes away when the timer runs out, when the student marks the task done, or when
 * they pause it (a paused timer is resumed from the Today tab of the planner).
 *
 * It only reads and writes the two planner keys; the planner page owns the rest (the streak, the
 * task list). When the planner page itself is open it registers window.PlannerTimer and this pill
 * hands its buttons to it, so nothing is written behind the planner's back. */
(function () {
  if (window.FocusTimer) return;
  var TKEY = "planner:timer:v1", SKEY = "planner:v1";
  var pill = null, tick = null, result = null, resultTimer = null;

  function readT() { try { return JSON.parse(localStorage.getItem(TKEY)); } catch (e) { return null; } }
  function readS() { try { return JSON.parse(localStorage.getItem(SKEY)); } catch (e) { return null; } }
  function elapsed(t) { return t.acc + (t.running ? Date.now() - t.since : 0); }
  function clock(ms) { var s = Math.max(0, Math.round(ms / 1000)), m = Math.floor(s / 60); return m + ":" + (s % 60 < 10 ? "0" : "") + (s % 60); }
  function icon(n, s) { return window.SiteIcon ? window.SiteIcon(n, s) : ""; }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function hooks() { return window.PlannerTimer || null; }
  function taskOf(store, t) { var r = store && store.days && store.days[t.day]; return r ? (r.tasks || []).filter(function (x) { return x.id === t.tid; })[0] : null; }
  function taskName(t) {
    if (t.title) return t.title;
    var task = taskOf(readS(), t); if (!task) return "";
    if (task.name) return task.name;
    return task.kind === "final" ? "Practice questions" : task.kind === "review" ? "Review" : "Study";
  }

  var CSS = "#ft-pill{position:fixed;top:max(10px,env(safe-area-inset-top));left:max(10px,env(safe-area-inset-left));z-index:9000;display:flex;align-items:center;gap:8px;" +
    "padding:5px 6px 5px 12px;border-radius:999px;background:#0f1115;color:#e8eaf0;border:1px solid #2a2f3a;box-shadow:0 6px 24px rgba(0,0,0,.35);" +
    "font:600 14px/1.2 system-ui,-apple-system,Segoe UI,sans-serif;max-width:calc(100vw - 20px)}" +
    "#ft-pill svg{flex:none;color:#35d6d8}#ft-pill button svg{color:inherit}" +
    "#ft-pill .ft-lbl{display:none}@media (min-width:640px){#ft-pill .ft-lbl{display:inline}}" +
    "#ft-pill .ft-clock{font-variant-numeric:tabular-nums;font-size:16px;font-weight:800;letter-spacing:.2px;min-width:3.2ch}" +
    "#ft-pill .ft-name{display:none;max-width:22ch;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:#a3abb8;font-weight:600}" +
    "@media (min-width:640px){#ft-pill .ft-name{display:block}}" +
    "#ft-pill button{font:inherit;cursor:pointer;flex:none;display:inline-flex;align-items:center;justify-content:center;gap:5px;min-width:34px;height:34px;padding:0 9px;border-radius:999px;" +
    "border:1px solid #343a48;background:transparent;color:#e8eaf0}" +
    "#ft-pill button:hover{background:#22262e}" +
    "#ft-pill button.ft-ok{background:#35d6d8;border-color:#35d6d8;color:#06282a}" +
    "#ft-pill button.ft-ok:hover{filter:brightness(.93);background:#35d6d8}" +
    "#ft-pill button:focus-visible{outline:3px solid #35d6d8;outline-offset:2px}" +
    "#ft-pill.ft-done{padding-left:12px}#ft-pill .ft-msg{font-weight:700}" +
    "@media print{#ft-pill{display:none}}";

  function ensureStyle() {
    if (document.getElementById("ft-style")) return;
    var st = document.createElement("style"); st.id = "ft-style"; st.textContent = CSS; document.head.appendChild(st);
  }
  function hide() { if (pill) { pill.remove(); pill = null; } }
  function box() { var b = document.getElementById("pl-timer"); return b && b.offsetParent !== null && b.children.length; }

  function commit(t, markDone, mins) {
    var s = readS(), task = taskOf(s, t);
    if (task) {
      task.logged = (task.logged || 0) + mins; if (markDone) task.done = true;
      try { localStorage.setItem(SKEY, JSON.stringify(s)); } catch (e) {}
    }
    try { localStorage.removeItem(TKEY); } catch (e) {}
  }
  function chime() {
    try {
      var A = window.AudioContext || window.webkitAudioContext; if (!A) return;
      var c = new A(), t0 = c.currentTime;
      [[660, 0], [880, 0.22]].forEach(function (n) {
        var o = c.createOscillator(), g = c.createGain(); o.type = "sine"; o.frequency.value = n[0];
        g.gain.setValueAtTime(0.0001, t0 + n[1]); g.gain.exponentialRampToValueAtTime(0.12, t0 + n[1] + 0.03); g.gain.exponentialRampToValueAtTime(0.0001, t0 + n[1] + 0.6);
        o.connect(g); g.connect(c.destination); o.start(t0 + n[1]); o.stop(t0 + n[1] + 0.7);
      });
      setTimeout(function () { try { c.close(); } catch (e) {} }, 1600);
    } catch (e) {}
  }

  function act(name) {
    var t = readT(); if (!t) return;
    var h = hooks();
    if (name === "pause") {
      if (h && h.pause) h.pause();
      else { t.acc += Date.now() - t.since; t.running = false; try { localStorage.setItem(TKEY, JSON.stringify(t)); } catch (e) {} }
    } else if (name === "done") {
      if (h && h.done) h.done();
      else commit(t, true, Math.round(Math.min(elapsed(t), t.total * 60000) / 60000));
    }
    update();
  }

  function showResult(t, mins) {
    ensureStyle(); hide();
    result = { day: t.day, tid: t.tid };
    pill = document.createElement("div"); pill.id = "ft-pill"; pill.className = "ft-done"; pill.setAttribute("role", "status");
    pill.innerHTML = icon("timer", 18) + '<span class="ft-msg">Time’s up · ' + mins + ' min logged</span>' +
      '<button type="button" class="ft-ok" data-ft="mark" aria-label="Mark the task done">' + icon("check", 15) + " Task done</button>" +
      '<button type="button" data-ft="close" aria-label="Dismiss">' + icon("x", 15) + "</button>";
    document.body.appendChild(pill);
    clearTimeout(resultTimer); resultTimer = setTimeout(function () { result = null; hide(); }, 15000);
  }

  function update() {
    var t = readT();
    if (result) return;                       // the "time's up" message is showing
    if (!t || !t.running) { hide(); return; } // gone, or paused (resumed from the planner)
    var s = readS();
    if (!s) { hide(); return; }               // no saved plan yet (or storage unavailable): show nothing, delete nothing
    if (!taskOf(s, t)) { hide(); if (!hooks()) { try { localStorage.removeItem(TKEY); } catch (e) {} } return; }
    if (box()) { hide(); return; }            // the planner's own timer card is on screen
    var left = t.total * 60000 - elapsed(t);
    if (left <= 0) {
      if (hooks()) { hide(); return; }        // the planner page settles it itself
      var mins = Math.round(t.total); commit(t, false, mins); chime(); showResult(t, mins); return;
    }
    ensureStyle();
    if (!pill) {
      pill = document.createElement("div"); pill.id = "ft-pill"; pill.setAttribute("role", "timer"); pill.setAttribute("aria-label", "Focus timer");
      pill.innerHTML = icon("timer", 18) + '<span class="ft-clock"></span><span class="ft-name"></span>' +
        '<button type="button" data-ft="pause" title="Pause (hides this timer; resume it in the planner)" aria-label="Pause the timer">' + icon("pause", 15) + "</button>" +
        '<button type="button" class="ft-ok" data-ft="done" title="Mark the task done" aria-label="Mark the task done">' + icon("check", 15) + '<span class="ft-lbl">Done</span></button>';
      document.body.appendChild(pill);
    }
    pill.querySelector(".ft-clock").textContent = clock(left);
    var nm = pill.querySelector(".ft-name"), name = taskName(t); if (nm.textContent !== name) nm.textContent = name;
  }

  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("#ft-pill [data-ft]"); if (!b) return;
    var k = b.getAttribute("data-ft");
    if (k === "pause" || k === "done") act(k);
    else if (k === "close") { result = null; clearTimeout(resultTimer); hide(); update(); }
    else if (k === "mark" && result) {
      var r = result, h = hooks(); result = null; clearTimeout(resultTimer);
      if (h && h.markDone) h.markDone(r.day, r.tid);
      else { var s = readS(), task = s && s.days && s.days[r.day] && (s.days[r.day].tasks || []).filter(function (x) { return x.id === r.tid; })[0]; if (task) { task.done = true; try { localStorage.setItem(SKEY, JSON.stringify(s)); } catch (er) {} } }
      hide();
    }
  });
  window.addEventListener("storage", function (e) { if (e.key === TKEY || e.key === SKEY || e.key === null) update(); });
  document.addEventListener("visibilitychange", function () { if (!document.hidden) update(); });
  tick = setInterval(update, 1000);
  window.FocusTimer = { update: update };
  update();
})();
