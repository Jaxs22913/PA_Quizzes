#!/usr/bin/env python3
"""Emit calendar-data.js from the parsed academic-calendar events."""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from parse_calendar import parse

OUT = "/Users/jaxonluke/Developer/PA_Quizzes/calendar-data.js"

# Summer Semester 1 events before the Fall calendar's August page picks up.
# Carried over from the list that used to be inlined in home.js so nothing is
# lost; everything from 2026-08-01 on comes from the PDFs instead, which is why
# the August remediation dates below stop at July.
SUMMER_TAIL = [
    ("2026-07-02", "Patient-Centered Healthcare Quiz (Lectures 1-6)", "intro-pa", "exam"),
    ("2026-07-06", "Anatomy Practicum #2 (Labs 6-10)", "anatomy-practicum", "exam"),
    ("2026-07-08", "Pharmacodynamics - Exam #2 (Lectures 5-7)", "pharmacodynamics", "exam"),
    ("2026-07-10", "Physiology - Exam #3 (Lectures 11-17)", "physio", "exam"),
    ("2026-07-13", "PD I Practicum #4 - Thorax & Abdominal Exam", "physical-diagnosis", "exam"),
    ("2026-07-15", "Intro to PA Profession - Quiz", "intro-pa", "exam"),
    ("2026-07-15", "PD I - Practicum Retest (Practicum #1-3)", "physical-diagnosis", "retest"),
    ("2026-07-16", "PD I - Practicum Retest (Practicum #1-3)", "physical-diagnosis", "retest"),
    ("2026-07-17", "Anatomy - Exam #3 (Lectures 12-17)", "anatomy", "exam"),
    ("2026-07-22", "PD I Exam #2 (Lectures 7-15)", "physical-diagnosis", "exam"),
    ("2026-07-24", "Anatomy - Exam #4 (Lectures 18-21)", "anatomy", "exam"),
    ("2026-07-25", "RETEST: Anatomy Computer Exam #3", "anatomy", "retest"),
    ("2026-07-25", "RETEST: Physio #2", "physio", "retest"),
    ("2026-07-27", "PD I - Practicum #5 - Musculoskeletal", "physical-diagnosis", "exam"),
    ("2026-07-28", "RETEST: Anatomy Computerized Exam #2", "anatomy", "retest"),
    ("2026-07-29", "CAM/Nutrition - Exam #1 (1-8)", "cam-nutrition", "exam"),
    ("2026-07-31", "PD I - Neuro Practicum #6", "physical-diagnosis", "exam"),
]

# Courses the Fall parser does not tag because they belong to Summer I but
# still appear on the August page (its remediation and retest week).
SUMMER_COURSE = [
    (re.compile(r"\bPhysio", re.I),            "physio"),
    (re.compile(r"Anatomy Practicum", re.I),   "anatomy-practicum"),
    (re.compile(r"\bAnatomy\b", re.I),         "anatomy"),
    (re.compile(r"\bPD I\b", re.I),            "physical-diagnosis"),
    (re.compile(r"CAM/Nutrition", re.I),       "cam-nutrition"),
    (re.compile(r"Pharmacodynamics", re.I),    "pharmacodynamics"),
]

FALL_START = "2026-08-17"


def tidy(title):
    # The school writes PDM I as "PMD I" on three of its four exam entries.
    title = re.sub(r"\bPMD\s+I\b", "PDM I", title)
    # Screening entries carry a full street address; keep the school name only.
    title = re.sub(r"^(Hearing and Vision Screening)\s*-\s*([^,]+),.*$", r"\1 - \2", title)
    return title.strip()


# Changes the school announced in class but has not reprinted in the PDFs yet.
# Without this they survive exactly one regeneration and then silently revert to
# whatever the stale PDF says, which is worse than never having fixed them --
# the calendar would look authoritative and be wrong.
#
# Each entry is  (date_in_pdf, title_substring) -> {what to change}
# Delete an entry once the reprinted PDF carries the change itself.
MOVED = {
    ("2026-08-31", "Pharm I EXAM #1"): {
        "date": "2026-09-04",          # moved to the Friday, told to the class
        "start": "8:00AM", "end": "10:00AM",
        "why": "announced in class 2026-08-31; August PDF still prints the 31st",
    },
}


def apply_moves(out):
    """Re-date events the school moved verbally. Loud if one stops matching."""
    unused = set(MOVED)
    for e in out:
        for key in list(unused):
            d, frag = key
            if e["date"] == d and frag.lower() in e["title"].lower():
                mv = MOVED[key]
                e["date"] = mv.get("date", e["date"])
                if mv.get("start"):
                    e["start"], e["end"] = mv["start"], mv.get("end")
                unused.discard(key)
                print("  moved: %s  %s -> %s  (%s)" % (frag, d, e["date"], mv["why"]))
    for d, frag in unused:
        # the PDF has caught up, or the title changed -- either way, look
        print("  NOTE: no event matched the override %r on %s; if the reprinted "
              "calendar now carries the change, delete it from MOVED." % (frag, d))
    return out


def main():
    evs = parse()
    out = []

    for d, t, c, ty in SUMMER_TAIL:
        out.append({"date": d, "title": t, "course": c, "type": ty,
                    "semester": "summer-1-2026", "start": None, "end": None})

    for e in evs:
        title = tidy(e["title"])
        course = e["course"]
        sem = "fall-2026" if e["date"] >= FALL_START else "summer-1-2026"
        if course is None:
            for rx, cid in SUMMER_COURSE:
                if rx.search(title):
                    course = cid
                    # A Summer I course exam sitting on the Fall calendar (the
                    # Physiology remediation on Aug 17) belongs to Summer I.
                    if e["type"] in ("retest", "remediation"):
                        sem = "summer-1-2026"
                    break
        out.append({"date": e["date"], "title": title, "course": course,
                    "type": e["type"], "semester": sem,
                    "start": e["start"], "end": e["end"]})

    # Sort each day chronologically. Sorting on the printed string instead puts
    # "10:00AM" before "8:00AM", which is how the first cut of the calendar page
    # showed Monday starting at ten and backtracking to eight.
    def minutes(t):
        if not t:
            return -1          # all-day entries lead the day
        m = re.match(r"(\d+):(\d+)([AP]M)", t)
        if not m:
            return -1
        h = int(m.group(1)) % 12
        if m.group(3) == "PM":
            h += 12
        return h * 60 + int(m.group(2))

    out = apply_moves(out)
    out.sort(key=lambda x: (x["date"], minutes(x["start"]), x["title"]))

    lines = []
    for e in out:
        parts = ['d:"%s"' % e["date"], 't:%s' % json.dumps(e["title"])]
        parts.append('c:%s' % (json.dumps(e["course"]) if e["course"] else "null"))
        parts.append('k:"%s"' % e["type"])
        parts.append('s:"%s"' % e["semester"])
        if e["start"]:
            parts.append('h:"%s"' % e["start"])
        if e["end"]:
            parts.append('e:"%s"' % e["end"])
        lines.append("    { " + ", ".join(parts) + " }")

    body = ",\n".join(lines)
    js = HEADER + body + FOOTER
    with open(OUT, "w") as f:
        f.write(js)
    print("wrote %s (%d events, %.1f KB)" % (OUT, len(out), len(js) / 1024.0))


HEADER = '''/* Academic calendar for the Class of 2028 — generated, do not hand-edit.

   Source: the printed academic calendar PDFs in
   ~/Desktop/Calendars/, one per month. Regenerate with
   tools/gen_calendar_data.py whenever the school revises the schedule.

   This exists because the exam list used to be a hand-typed array inside
   home.js, and the school moved three August dates without it being noticed —
   Physiology's course remediation slid from Aug 14 to Aug 17. Deriving the
   list from the PDFs instead means a revision is one regeneration, not a
   careful diff by eye.

   Each event is deliberately terse so the whole semester stays a small
   download:
     d  date, YYYY-MM-DD, local
     t  title, verbatim from the calendar apart from the fixes in tidy()
     c  class id from semesters.js, or null for holidays and admin dates
     k  kind: exam | retest | remediation | lecture | lab | activity |
             holiday | other
     s  semester id from semesters.js
     h  start time, e  end time — absent for all-day entries              */
(function () {
  "use strict";

  var EVENTS = [
'''

FOOTER = '''
  ];

  /* Kinds that mean "you are being graded that day". The week widget and the
     countdown both key off this rather than each restating the list. */
  var GRADED = { exam: 1, retest: 1, remediation: 1 };

  window.CalendarData = {
    all: EVENTS,
    graded: function () {
      return EVENTS.filter(function (e) { return GRADED[e.k]; });
    },
    forSemester: function (id) {
      return EVENTS.filter(function (e) { return e.s === id; });
    },
    onDate: function (ymd) {
      return EVENTS.filter(function (e) { return e.d === ymd; });
    },
    isGraded: function (e) { return !!GRADED[e.k]; }
  };
})();
'''

if __name__ == "__main__":
    main()
