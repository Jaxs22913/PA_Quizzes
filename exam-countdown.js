/* How much of an upcoming exam's material has actually been drilled, shown on
 * the row for that exam inside the "This week" widget.
 *
 * This was briefly its own "Next up" card and that was a mistake: it listed the
 * same exams the week widget already listed, in the middle column, which pushed
 * the semester card and the quiz list below the fold. The dates were never the
 * new information -- the readiness was. So only that moved in, onto the row that
 * was already there.
 *
 * Everything is derived from what the page already holds: CalendarData for the
 * events, Semesters.classOfPath to tie a repo folder to a course, the quiz links
 * in the DOM for what exists, and the qc: keys for what has been finished.
 */
(function () {
  "use strict";

  function parseLocal(ymd) {                 // local, not UTC -- a UTC parse
    var p = String(ymd).split("-");          // shifts every date a day west
    return new Date(+p[0], +p[1] - 1, +p[2]);
  }

  /* Which repo folder holds an exam's quizzes. The calendar says
     "CMS I - EXAM # 2- Ophthalmology Block Exam (10-14)"; the folder is
     "Clinical Medicine and Surgery I Exam 2". Match on the course id AND the
     exam number, because one course owns several folders. */
  function folderIndex() {
    var reg = window.Semesters, out = {};
    document.querySelectorAll('a.quiz-link[href]').forEach(function (a) {
      var raw = a.getAttribute("href") || "";
      var href = decodeURIComponent(raw);
      if (href.indexOf("/") === -1) return;
      var folder = href.split("/")[0];
      var rec = out[folder] || (out[folder] = { total: 0, done: 0, cls: null, n: null });
      rec.total++;
      if (rec.cls === null && reg && reg.classOfPath) rec.cls = reg.classOfPath(href) || null;
      if (rec.n === null) {
        var m = folder.match(/Exam\s+(\d+)\s*$/i);
        rec.n = m ? +m[1] : null;
      }
      try {
        var v = localStorage.getItem("qc:/" + raw);
        if (v) { var r = JSON.parse(v); if (r && r.total > 0) rec.done++; }
      } catch (e) {}
    });
    return out;
  }

  function matchFolder(ev, idx) {
    var m = String(ev.t).match(/EXAM\s*#?\s*(\d+)/i);
    var want = m ? +m[1] : null;
    var best = null;
    Object.keys(idx).forEach(function (f) {
      var r = idx[f];
      if (!r.cls || r.cls !== ev.c) return;
      if (want !== null && r.n !== null && r.n !== want) return;
      if (!best || r.total > idx[best].total) best = f;
    });
    return best;
  }

  function decorate() {
    var cal = window.CalendarData;
    var list = document.getElementById("week-list");
    if (!cal || !cal.graded || !list) return 0;
    var rows = list.querySelectorAll(".week-item:not(.has-drill)");
    if (!rows.length) return 0;

    var idx = folderIndex(), events = cal.graded(), n = 0;
    Array.prototype.forEach.call(rows, function (row) {
      var titleEl = row.querySelector(".week-item-title");
      if (!titleEl) return;
      var title = titleEl.textContent.trim();
      var ev = null;
      for (var i = 0; i < events.length; i++) {
        if (String(events[i].t).trim() === title) { ev = events[i]; break; }
      }
      if (!ev) return;
      var folder = matchFolder(ev, idx);
      var rec = folder ? idx[folder] : null;
      if (!rec || !rec.total) return;
      var pct = Math.round(rec.done / rec.total * 100);
      var box = document.createElement("div");
      box.className = "wk-drill";
      box.innerHTML = '<div class="wk-drill-bar"><i></i></div>' +
        '<div class="wk-drill-txt">' + rec.done + " of " + rec.total +
        " quizzes done &middot; " + pct + "%</div>";
      row.appendChild(box);
      row.classList.add("has-drill");
      requestAnimationFrame(function () {
        var fill = box.querySelector("i");
        if (fill) fill.style.width = pct + "%";
      });
      n++;
    });
    return n;
  }

  function start() {
    if (decorate()) return;
    /* home.js fills #week-list after this runs, and refills it when the week
       rolls over, so watch rather than guess at the timing. */
    var list = document.getElementById("week-list");
    if (!list || !window.MutationObserver) return;
    var pending = null;
    new MutationObserver(function () {
      if (pending) return;
      pending = requestAnimationFrame(function () { pending = null; decorate(); });
    }).observe(list, { childList: true, subtree: true });
  }

  if (document.readyState !== "loading") start();
  else document.addEventListener("DOMContentLoaded", start);
})();
