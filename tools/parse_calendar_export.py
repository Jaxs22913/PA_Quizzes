#!/usr/bin/env python3
"""Parse the Outlook calendar *export* PDF (a table-style PDF made from the
Class of 2028 Academic Calendar, e.g. PA_Class_of_2028_Calendar_Fall2026.pdf).

Unlike the school's monthly Outlook print-outs (tools/parse_calendar.py), this
export lists, under "Full schedule, day by day", rows of
    [Day]  Time  TYPE  Event text (may wrap onto following lines)
where the Day cell appears only on a day's first row. Lunch is already left out.
Returns the same dicts as parse_calendar.parse(): date, title, start, end,
allDay, course, type.
"""
import re, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pymupdf as fitz
from parse_calendar import classify, course_of

DAY = re.compile(r"^(Mon|Tue|Wed|Thu|Fri|Sat|Sun) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{2})$")
TIME = re.compile(r"^(All day|(\d{1,2}:\d{2} [AP]M) - (\d{1,2}:\d{2} [AP]M))$")
TYPES = {"EXAM", "RETEST", "REMEDIATION", "LECTURE", "LAB/SIM", "OTHER", "DEADLINE", "NO CLASS"}
SKIP = re.compile(r"^(PA Class of 2028 Academic Calendar.*|Page \d+|Day|Date|Time|Type|Event|Week of .*)$")
MON = {m: i + 1 for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}


def parse(path, year=2026):
    doc = fitz.open(path)
    lines = []
    for page in doc:
        lines += [l.strip() for l in page.get_text().split("\n")]
    i = next(k for k, l in enumerate(lines) if l.startswith("Full schedule, day by day"))
    events, date, cur = [], None, None
    for l in lines[i + 1:]:
        if not l or SKIP.match(l):
            continue
        m = DAY.match(l)
        if m:
            date = "%04d-%02d-%02d" % (year, MON[m.group(2)], int(m.group(3)))
            continue
        m = TIME.match(l)
        if m:
            cur = {"date": date, "allDay": m.group(1) == "All day",
                   "start": m.group(2) and m.group(2).replace(" ", ""),
                   "end": m.group(3) and m.group(3).replace(" ", ""),
                   "xtype": None, "title": ""}
            events.append(cur)
            continue
        if cur is not None and cur["xtype"] is None and l in TYPES:
            cur["xtype"] = l
            continue
        if cur is not None:
            cur["title"] = (cur["title"] + " " + l).strip()
    for e in events:
        e["title"] = re.sub(r"\s+", " ", e["title"]).strip()
        e["course"] = course_of(e["title"])
        e["type"] = classify(e["title"])
    return events


if __name__ == "__main__":
    evs = parse(sys.argv[1])
    print(json.dumps(evs, indent=1))
    print(len(evs), "events", file=sys.stderr)
