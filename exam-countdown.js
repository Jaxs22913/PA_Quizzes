/* "Next up" on the academic calendar: the next graded dates, each with a ring
 * that fills as the date closes in and a bar for how much of that block's
 * material has actually been drilled.
 *
 * It was on the homepage first and was wrong there twice over -- as its own card
 * it repeated the week widget and pushed the quiz list below the fold, and
 * folded into the week widget it was still answering a question the homepage had
 * already answered. This is the page about dates, so this is where it belongs.
 *
 * Counting "3 of 29 done" needs to know which quizzes exist. The homepage could
 * read that off its own links; the calendar has none, so quiz-index.json ships
 * the list. Everything else is derived: CalendarData for the events,
 * Semesters.classOfPath to tie a folder to a course, qc: keys for what is done.
 */
(function () {
  "use strict";
  var HORIZON = 21;      // days out at which the ring starts filling
  var SHOW = 4;

  function parseLocal(ymd) {              // local, not UTC -- a UTC parse shifts
    var p = String(ymd).split("-");       // every date a day west of here
    return new Date(+p[0], +p[1] - 1, +p[2]);
  }

  function daysUntil(d) {
    var t = new Date(); t.setHours(0, 0, 0, 0);
    return Math.round((parseLocal(d) - t) / 86400000);
  }

  function folderIndex(idxJson) {
    var reg = window.Semesters, out = {};
    Object.keys(idxJson).forEach(function (folder) {
      var files = idxJson[folder];
      var rec = { total: files.length, done: 0, cls: null, n: null };
      var m = folder.match(/Exam\s+(\d+)\s*$/i);
      rec.n = m ? +m[1] : null;
      if (reg && reg.classOfPath) rec.cls = reg.classOfPath(folder + "/x.html") || null;
      files.forEach(function (fn) {
        try {
          var v = localStorage.getItem("qc:/" + encodeURIComponent(folder) + "/" + fn);
          if (v) { var r = JSON.parse(v); if (r && r.total > 0) rec.done++; }
        } catch (e) {}
      });
      out[folder] = rec;
    });
    return out;
  }

  /* One course owns several folders, so an event has to match on the course id
     AND the exam number: "CMS I - EXAM # 2" belongs to Exam 2, not Exam 1. */
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
    var R = 19, C = 2 * Math.PI * R;
    var off = C * (1 - Math.max(0, Math.min(1, pct)));
    return '<svg class="nu-ring" viewBox="0 0 46 46" aria-hidden="true">' +
      '<circle cx="23" cy="23" r="' + R + '" class="nu-track"></circle>' +
      '<circle cx="23" cy="23" r="' + R + '" class="nu-fill" ' +
        'style="stroke-dasharray:' + C.toFixed(1) + ';stroke-dashoffset:' + off.toFixed(1) + '"></circle>' +
      '<text x="23" y="23" class="nu-d">' + days + '</text>' +
      '<text x="23" y="32" class="nu-u">' + (Math.abs(days) === 1 ? "day" : "days") + '</text></svg>';
  }

  function render(idxJson) {
    var host = document.getElementById("next-up");
    var list = document.getElementById("nu-list");
    var cal = window.CalendarData;
    if (!host || !list || !cal || !cal.graded) return;

    var soon = cal.graded()
      .filter(function (e) { return daysUntil(e.d) >= 0; })
      .sort(function (a, b) { return a.d < b.d ? -1 : a.d > b.d ? 1 : 0; })
      .slice(0, SHOW);
    if (!soon.length) return;

    var idx = folderIndex(idxJson || {}), html = "";
    soon.forEach(function (ev) {
      var days = daysUntil(ev.d);
      var folder = matchFolder(ev, idx);
      var rec = folder ? idx[folder] : null;
      var pct = rec && rec.total ? Math.round(rec.done / rec.total * 100) : null;
      var title = String(ev.t).replace(/\s*\([^)]*\)\s*$/, "");
      var when = days === 0 ? "today" : days === 1 ? "tomorrow"
               : parseLocal(ev.d).toLocaleDateString(undefined,
                   { weekday: "short", month: "short", day: "numeric" });
      html += '<div class="nu-row">' + ring(1 - Math.min(1, days / HORIZON), days) +
        '<div class="nu-body"><div class="nu-name">' + title + "</div>" +
        '<div class="nu-when">' + when + (ev.h ? " &middot; " + ev.h : "") + "</div>" +
        (pct === null ? '<div class="nu-none">no quizzes posted yet</div>'
          : '<div class="nu-bar"><i></i></div><div class="nu-pct">' + rec.done + " of " +
            rec.total + " quizzes done &middot; " + pct + "%</div>") +
        "</div></div>";
    });
    list.innerHTML = html;
    var note = document.getElementById("nu-note");
    if (note) note.textContent = "how ready you are";
    host.hidden = false;
    requestAnimationFrame(function () {
      var bars = list.querySelectorAll(".nu-bar i"), k = 0;
      soon.forEach(function (ev) {
        var folder = matchFolder(ev, idx), rec = folder ? idx[folder] : null;
        if (!rec || !rec.total) return;
        if (bars[k]) bars[k].style.width = Math.round(rec.done / rec.total * 100) + "%";
        k++;
      });
    });
  }

  function start() {
    if (!document.getElementById("next-up")) return;   // only the calendar page
    fetch("quiz-index.json")
      .then(function (r) { return r.ok ? r.json() : {}; })
      .catch(function () { return {}; })
      .then(render);
  }

  if (document.readyState !== "loading") start();
  else document.addEventListener("DOMContentLoaded", start);
})();
