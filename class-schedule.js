/* Exam roadmap for a class that has no quizzes yet.

   A new semester's tabs are empty for weeks -- the courses exist and the exam
   dates are known long before any lecture is posted. An empty tab reads as
   broken, so each one shows that course's exams from calendar-data.js until
   there is something to actually study.

   It stands aside the moment real content arrives: a panel containing an
   .exam-section is left completely alone, so adding the first quiz to a class
   retires its roadmap automatically, one class at a time. Nothing to remember
   to delete later. */
(function () {
  "use strict";

  var cal = window.CalendarData;
  if (!cal) return;

  /* The calendar prefixes every entry with its own course name ("CMS I -
     EXAM #2- Ophthalmology Block Exam"), which is redundant once the row is
     already inside that course's tab. Strip the prefix and tidy the spacing
     the school's typing leaves behind. */
  function shorten(title) {
    var t = title
      .replace(/^(CMS|PDM|PMD|Pharm|Clin(?:ical)?\s*Path(?:ophysiology)?|PD)\s*I{1,2}\b\s*[-–—:]?\s*/i, "")
      .replace(/^Microbiology\s*[-–—:]?\s*/i, "")
      .replace(/^Interpretation of Med(?:ical)?\s*Lit(?:erature)?\s*[-–—:]?\s*/i, "");
    /* Lecture ranges first: "(10-14)" -> "(10–14)". This has to run BEFORE the
       separator rule below, which would otherwise turn the range into
       "(10 — 14)" and leave nothing for this to match. The separator rule then
       deliberately lists only hyphen and em-dash, so it cannot undo the
       en-dash just inserted here. */
    t = t.replace(/(\d)\s*[-–]\s*(\d)/g, "$1–$2");
    // "EXAM #2- Ophthalmology" -> "Exam #2 — Ophthalmology"
    t = t.replace(/\s*[-—]\s*/g, " — ").replace(/#\s+/g, "#").replace(/\s{2,}/g, " ");
    t = t.replace(/\bEXAM\b/g, "Exam").replace(/\bRETEST\b/g, "Retest")
         .replace(/\bCOURSE REMEDIATION EXAM\b/gi, "Course Remediation Exam");
    return t.trim().replace(/^—\s*/, "");
  }

  function ymd(d) {
    return d.getFullYear() + "-" +
      String(d.getMonth() + 1).padStart(2, "0") + "-" +
      String(d.getDate()).padStart(2, "0");
  }

  function shortDate(iso) {
    var p = iso.split("-");
    var d = new Date(+p[0], +p[1] - 1, +p[2]);
    return d.toLocaleDateString("en-US", { weekday: "short", month: "short", day: "numeric" });
  }

  var today = ymd(new Date());

  document.querySelectorAll(".tab-panel[data-class]").forEach(function (panel) {
    // Real quizzes win. Also bail if something already rendered here.
    if (panel.querySelector(".exam-section") || panel.querySelector(".class-schedule")) return;

    var cls = panel.dataset.class;
    var mine = cal.all.filter(function (e) { return e.c === cls; });
    if (!mine.length) return;

    // Retests are excluded on purpose: every block exam has one, and listing
    // both doubles the roadmap with dates that only matter if you fail.
    var graded = mine.filter(function (e) { return e.k === "exam" || e.k === "remediation"; });
    if (!graded.length) return;

    var lectures = mine.filter(function (e) { return e.k === "lecture"; }).length;

    var wrap = document.createElement("div");
    wrap.className = "class-schedule";

    var lead = document.createElement("p");
    lead.className = "cs-lead";
    lead.innerHTML = "No quizzes yet — these appear as each lecture is posted. " +
      "<b>" + lectures + "</b> lecture" + (lectures === 1 ? "" : "s") +
      " and <b>" + graded.length + "</b> exam" + (graded.length === 1 ? "" : "s") +
      " are on the academic calendar for this course.";
    wrap.appendChild(lead);

    var list = document.createElement("ol");
    list.className = "cs-list";
    graded.forEach(function (e) {
      var li = document.createElement("li");
      li.className = "cs-row" + (e.d < today ? " past" : "");
      var dt = document.createElement("span");
      dt.className = "cs-date";
      dt.textContent = shortDate(e.d);
      var ti = document.createElement("span");
      ti.className = "cs-title";
      ti.textContent = shorten(e.t);
      li.appendChild(dt);
      li.appendChild(ti);
      list.appendChild(li);
    });
    wrap.appendChild(list);
    panel.appendChild(wrap);
  });
})();
