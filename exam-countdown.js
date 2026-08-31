/* "Next up" -- the next graded dates, each with how much of that block has
   actually been drilled.
 *
 * The week widget already answers "what is happening this week". This answers
 * the other question, which is whether you are ready for it: a ring that fills
 * as the date closes in, and a bar for the share of that exam's quizzes you
 * have finished at least once.
 *
 * Everything is derived from what the page already has -- CalendarData for the
 * dates, Semesters.classOfPath to tie a repo folder to a course, the quiz links
 * in the DOM for what exists, and the qc: keys for what has been done. No new
 * data source, and nothing to keep in sync by hand.
 */
(function () {
  "use strict";
  var HORIZON = 21;          // days out at which the ring starts filling
  var SHOW = 3;

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  function parseLocal(ymd) {
    var p = String(ymd).split("-");
    return new Date(+p[0], +p[1] - 1, +p[2]);   // local, not UTC -- a UTC parse
  }                                             // shifts the date a day west

  function daysUntil(d) {
    var t = new Date(); t.setHours(0, 0, 0, 0);
    return Math.round((parseLocal(d) - t) / 86400000);
  }

  /* Which repo folder holds an exam's quizzes. The calendar says
     "CMS I - EXAM # 2- Ophthalmology Block Exam (10-14)"; the folder is
     "Clinical Medicine and Surgery I Exam 2". Match on the course id plus the
     exam number, because one course owns several folders. */
  function folderIndex() {
    var reg = window.Semesters, out = {};
    document.querySelectorAll('a.quiz-link[href]').forEach(function (a) {
      var href = decodeURIComponent(a.getAttribute("href") || "");
      var folder = href.split("/")[0];
      if (!folder || href.indexOf("/") === -1) return;
      var rec = out[folder] || (out[folder] = { total: 0, done: 0, cls: null, n: null });
      rec.total++;
      if (rec.cls === null && reg && reg.classOfPath) rec.cls = reg.classOfPath(href) || null;
      if (rec.n === null) {
        var m = folder.match(/Exam\s+(\d+)\s*$/i);
        rec.n = m ? +m[1] : null;
      }
      try {
        var raw = localStorage.getItem("qc:/" + a.getAttribute("href"));
        if (raw) { var r = JSON.parse(raw); if (r && r.total > 0) rec.done++; }
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

  function ring(pct, days) {
    var R = 20, C = 2 * Math.PI * R;
    var off = C * (1 - Math.max(0, Math.min(1, pct)));
    return '<svg class="ec-ring" viewBox="0 0 48 48" aria-hidden="true">' +
      '<circle cx="24" cy="24" r="' + R + '" class="ec-track"></circle>' +
      '<circle cx="24" cy="24" r="' + R + '" class="ec-fill" ' +
        'style="stroke-dasharray:' + C.toFixed(1) + ';stroke-dashoffset:' + off.toFixed(1) + '"></circle>' +
      '<text x="24" y="24" class="ec-d">' + days + '</text>' +
      '<text x="24" y="33" class="ec-u">' + (Math.abs(days) === 1 ? "day" : "days") + '</text></svg>';
  }

  ready(function () {
    var host = document.getElementById("exam-countdown");
    var list = document.getElementById("ec-list");
    var cal = window.CalendarData;
    if (!host || !list || !cal || !cal.graded) return;

    var soon = cal.graded()
      .filter(function (e) { return daysUntil(e.d) >= 0; })
      .sort(function (a, b) { return a.d < b.d ? -1 : a.d > b.d ? 1 : 0; })
      .slice(0, SHOW);
    if (!soon.length) return;

    var idx = folderIndex(), html = "";
    soon.forEach(function (ev) {
      var days = daysUntil(ev.d);
      var folder = matchFolder(ev, idx);
      var rec = folder ? idx[folder] : null;
      var pct = rec && rec.total ? Math.round(rec.done / rec.total * 100) : null;
      var title = String(ev.t).replace(/\s*\([^)]*\)\s*$/, "");
      var when = days === 0 ? "today" : days === 1 ? "tomorrow"
               : parseLocal(ev.d).toLocaleDateString(undefined, { weekday: "short", month: "short", day: "numeric" });
      html += '<div class="ec-row">' +
        ring(1 - Math.min(1, days / HORIZON), days) +
        '<div class="ec-body">' +
          '<div class="ec-name">' + title + "</div>" +
          '<div class="ec-when">' + when + (ev.h ? " &middot; " + ev.h : "") + "</div>" +
          (pct === null ? '<div class="ec-none">no quizzes posted yet</div>'
            : '<div class="ec-bar"><i style="width:' + pct + '%"></i></div>' +
              '<div class="ec-pct">' + rec.done + " of " + rec.total + " quizzes done &middot; " + pct + "%</div>") +
        "</div></div>";
    });
    list.innerHTML = html;
    var note = document.getElementById("ec-note");
    if (note) note.textContent = soon.length + (soon.length === 1 ? " coming up" : " coming up");
    host.hidden = false;
  });
})();
