/* Semester registry — the single source of truth for which class belongs to
   which term.

   The class list used to be restated in four places (index.html's tabs,
   guides.html's cards, arcade.js's DEMO_CLASSES, and the group-quizzes
   manifest). Semester lives here instead, and each of those reads it, so a new
   term is one edit rather than four that can drift apart.

   Adding a semester:
     1. Add an entry below, in chronological order.
     2. In index.html, add a matching <div class="semester" data-semester="ID">
        block with its own header, progress bar and tab strip.
     3. That's it — the switcher, the progress bar, search scoping, the guides
        page, Arcade's class tabs and the Group Study picker all follow.

   `classes` holds the tab ids used by index.html (data-tab / tab-panel id),
   arcade.js (DEMO_CLASSES id) and the group manifest's class field, so one
   name works everywhere. A class that runs across two terms is listed in both;
   an individual exam can override its semester with data-semester on the
   .exam-section, which is how a course like the Anatomy Practicum can carry
   Exams 2-3 in one term and 4+ in the next without being split in two. */
(function () {
  "use strict";

  var SEMESTERS = [
    {
      id: "summer-1-2026",
      label: "Summer Semester 1 – 2026",
      short: "Semester 1",
      start: "2026-05-18",
      // last real day of the semester: remediation exams happen ON Aug 14, so
      // the whole day still reads as "in progress"
      end: "2026-08-14",
      // last actual CLASS day — the Aug 10-14 exam/remediation week is not
      // class days, which is what "class days left" counts to
      lastClassDay: "2026-08-07",
      // the program counts this as a 12-week semester even though the calendar
      // span is ~12.6 weeks; trust the program's number over the date math
      totalWeeks: 12,
      classes: ["physio", "pharmacodynamics", "anatomy", "anatomy-practicum",
                "intro-pa", "cam-nutrition", "physical-diagnosis"]
    },

    /* Fall 2026 dates are REAL, taken from the Class of 2028 academic calendar
       (~/Desktop/Calendars/Fall Semester - 2026, five monthly PDFs), so the
       `estimated` flag is gone. Same shape as Summer I:
         start        Aug 17, the Start of Semester Talk and first lectures
         lastClassDay Dec 3, the last regular course final (Microbiology #3);
                      Dec 4-11 is retests and course remediation, which is not
                      class time — the same distinction Summer I draws
         end          Dec 11, the last remediation exam, so that day still
                      reads as "in progress"
       totalWeeks is 17 counted off the calendar (Aug 17 -> Dec 11). Summer I's
       note applies here too: if the syllabus states a different number, trust
       the program's over the date math. */
    {
      id: "fall-2026",
      label: "Fall Semester – 2026",
      short: "Semester 2",
      start: "2026-08-17",
      end: "2026-12-11",
      lastClassDay: "2026-12-03",
      totalWeeks: 17,
      /* Ordered by how much of the term each course actually takes up — CMS I
         is 51 lectures and eight block exams, Clin Path I is ten lectures and
         two. That puts the tab you reach for most first, the same way
         Physiology leads Summer I. */
      classes: ["cms-1", "pdm-1", "microbiology", "pharm-1",
                "physical-diagnosis-2", "clin-path-1", "med-lit"]
    },

    /* The last two didactic terms have no syllabus yet, so these dates are
       ESTIMATED from the usual academic calendar and are marked `estimated` —
       the UI says "dates to be confirmed" rather than stating them as fact.
       Replace them with the real ones (and drop the flag) as each calendar
       arrives; nothing else needs to change.

       `classes` is empty until a term's courses are known. A semester with no
       classes still appears in the switcher, showing an empty state, so the
       shape of the year is visible before any content exists for it. */
    {
      id: "spring-2027",
      label: "Spring Semester – 2027",
      short: "Semester 3",
      estimated: true,
      start: "2027-01-11",
      end: "2027-05-07",
      lastClassDay: "2027-04-30",
      totalWeeks: 16,
      classes: []
    },
    {
      id: "summer-2-2027",
      label: "Summer Semester 2 – 2027",
      short: "Semester 4",
      estimated: true,
      start: "2027-05-17",
      end: "2027-08-13",
      lastClassDay: "2027-08-06",
      totalWeeks: 12,
      classes: []
    }
  ];

  function startOf(s) { return parseLocal(s.start); }
  function endOf(s) { return parseLocal(s.end, true); }

  // Parse as LOCAL midnight. new Date("2026-05-18") parses as UTC, which lands
  // on the previous evening in US timezones and shifts every week number by a
  // day — the same date-only-string trap noted in the Bulk Tracker work.
  function parseLocal(str, endOfDay) {
    var p = String(str).split("-");
    return new Date(+p[0], +p[1] - 1, +p[2],
                    endOfDay ? 23 : 0, endOfDay ? 59 : 0, endOfDay ? 59 : 0);
  }

  /* The semester containing `now`; if none does (a gap between terms, or before
     the first), the nearest upcoming one, else the most recent. Never null so
     callers don't each need a fallback. */
  function current(now) {
    now = now || new Date();
    var i;
    for (i = 0; i < SEMESTERS.length; i++) {
      if (now >= startOf(SEMESTERS[i]) && now <= endOf(SEMESTERS[i])) return SEMESTERS[i];
    }
    for (i = 0; i < SEMESTERS.length; i++) {
      if (now < startOf(SEMESTERS[i])) return SEMESTERS[i];
    }
    return SEMESTERS[SEMESTERS.length - 1];
  }

  function byId(id) {
    for (var i = 0; i < SEMESTERS.length; i++) {
      if (SEMESTERS[i].id === id) return SEMESTERS[i];
    }
    return null;
  }

  /* Two surfaces spell the same class differently: the Arcade's tab id for
     Physiology is "physiology" while index.html's is "physio". Renaming either
     would strand the saved active tab in every existing visitor's
     localStorage, so the registry accepts both spellings instead. */
  var ALIASES = { physiology: "physio" };

  /* Which semester a class belongs to. Returns the FIRST match, so a class
     spanning two terms resolves to the earlier one unless an exam overrides. */
  function ofClass(classId) {
    var id = ALIASES[classId] || classId;
    for (var i = 0; i < SEMESTERS.length; i++) {
      if (SEMESTERS[i].classes.indexOf(id) !== -1) return SEMESTERS[i];
    }
    return null;
  }


  /* Repo folder -> class id. Several surfaces only know a quiz by its path
     (guides.html cards, the group manifest, the atlas), so the mapping lives
     here with everything else rather than being re-derived per page.
     Order matters: "Anatomy Practicum" must be tested before "Anatomy". */
  var FOLDER_CLASS = [
    [/^Anatomy Practicum/i, "anatomy-practicum"],
    [/^Anatomy/i, "anatomy"],
    [/^Physiology/i, "physio"],
    // Physical Diagnosis 2 must be tested before Physical Diagnosis, which
    // would otherwise swallow it and file every Fall folder under Summer I.
    [/^Physical Diagnosis 2/i, "physical-diagnosis-2"],
    [/^Physical Diagnosis/i, "physical-diagnosis"],
    [/^CAM.?Nutrition/i, "cam-nutrition"],
    [/^Nutrition Class/i, "cam-nutrition"],
    // Likewise Pharmacology I vs Pharmacodynamics: both start "Pharma".
    [/^Pharmacodynamics/i, "pharmacodynamics"],
    [/^Pharmacology/i, "pharm-1"],
    [/^Intro to PA/i, "intro-pa"],
    // Both spellings for the two courses the school abbreviates: content
    // folders use the full name, but the calendar and the school's own
    // paperwork say CMS and PDM, so either can turn up in a path.
    [/^Clinical Medicine( and | ?& ?)Surgery/i, "cms-1"],
    [/^CMS/i, "cms-1"],
    [/^Clinical Path/i, "clin-path-1"],
    [/^Principles of Diagnostic Medicine/i, "pdm-1"],
    [/^PDM/i, "pdm-1"],
    [/^Microbiology/i, "microbiology"],
    [/^Interpretation of Medical Literature/i, "med-lit"]
  ];

  function classOfPath(path) {
    var folder = decodeURIComponent(String(path || "")).split("/")[0];
    for (var i = 0; i < FOLDER_CLASS.length; i++) {
      if (FOLDER_CLASS[i][0].test(folder)) return FOLDER_CLASS[i][1];
    }
    return null;
  }

  window.Semesters = {
    all: SEMESTERS,
    current: current,
    byId: byId,
    ofClass: ofClass,
    classOfPath: classOfPath,
    semesterOfPath: function (p) { var c = classOfPath(p); return c ? ofClass(c) : null; },
    parseLocal: parseLocal,
    startOf: startOf,
    endOf: endOf,
    /* Semester id for one element, honouring a per-exam data-semester override
       and otherwise inheriting from the enclosing .semester block. */
    ofElement: function (el) {
      var override = el.closest ? el.closest("[data-semester]") : null;
      return override ? override.getAttribute("data-semester") : null;
    }
  };
})();
