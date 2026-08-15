#!/usr/bin/env python3
"""Turn the Class of 2028 Fall 2026 calendar PDFs into structured events.

The PDFs are an Outlook calendar print-out: a date heading, then for each event
a title (which may wrap over several lines) followed by a line giving the day,
date and time. Titles are accumulated until a time line closes them off.
"""
import fitz, re, json, sys, os

SRC = "/Users/jaxonluke/Desktop/Calendars/Fall Semester - 2026"
MONTHS = ["August.pdf", "September.pdf", "October.pdf", "November.pdf", "December.pdf"]

DATE_HEAD = re.compile(r"^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday), "
                       r"(\w+) (\d+), (\d{4})$")
TIME_LINE = re.compile(r"^(Mon|Tue|Wed|Thu|Fri|Sat|Sun) (\d+)/(\d+)/(\d{4})\s*"
                       r"(?:\((All day)\)|(\d+:\d+\s*[AP]M)\s*-\s*(\d+:\d+\s*[AP]M))")
MONTH_NUM = {m: i + 1 for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"])}

# Course detection. Order matters: "PD II" must beat a bare "PD", and the
# calendar itself misspells PDM I as "PMD I" on three of its four exam entries.
COURSES = [
    ("cms-1",        re.compile(r"\bCMS\s*I\b", re.I)),
    ("clin-path-1",  re.compile(r"\bClin(?:ical)?\s*Path(?:ophysiology)?\s*I\b", re.I)),
    ("pharm-1",      re.compile(r"\bPharm\s*I\b", re.I)),
    ("pdm-1",        re.compile(r"\bP[DM]M\s*I\b|\bPMD\s*I\b", re.I)),
    ("physical-diagnosis-2", re.compile(r"\bPD\s*II\b", re.I)),
    ("microbiology", re.compile(r"\bMicrobiology\b", re.I)),
    ("med-lit",      re.compile(r"\bInterpretation of Med(?:ical)?\s*Lit(?:erature)?\b", re.I)),
]

# Noise to drop outright: the lunch blocks, and a Zoom invitation that was
# pasted into one November event and dragged its whole boilerplate in with it.
NOISE = re.compile(r"^(Lunch|LUNCH)$|^Join Zoom|^Meeting ID|^Passcode|^One tap mobile|"
                   r"^Join by SIP|^Join instructions|^https?://|^<https?://|^\+\d|"
                   r"^[••â]|^-{3,}|^─+|^Lauren Reynolds is inviting")


def classify(title):
    t = title.lower()
    # "OSCE Prep Session" and the independent-study blocks read as exams to a
    # naive keyword match but nothing is graded in them.
    if re.search(r"osce prep|prep session", t):           return "activity"
    if re.search(r"\bretest\b", t):                       return "retest"
    if re.search(r"remediation", t):                      return "remediation"
    if re.search(r"\bexam\b|\bosce\b|block exam", t):     return "exam"
    if re.search(r"no classes|holiday|labor day|thanksgiving|veteran", t): return "holiday"
    if re.search(r"\blab\b|\blab #", t):                  return "lab"
    if re.search(r"simulation|small group|independent study|osce prep", t): return "activity"
    if re.search(r"\blecture\b", t):                      return "lecture"
    return "other"


def course_of(title):
    for cid, rx in COURSES:
        if rx.search(title):
            return cid
    return None


def parse():
    events = []
    for fn in MONTHS:
        doc = fitz.open(os.path.join(SRC, fn))
        lines = []
        for page in doc:
            lines += [l.rstrip() for l in page.get_text().split("\n")]

        cur_date = None
        buf = []
        for raw in lines:
            line = raw.strip()
            if not line:
                continue
            if NOISE.search(line):
                buf = []
                continue

            m = DATE_HEAD.match(line)
            if m:
                cur_date = "%04d-%02d-%02d" % (int(m.group(4)), MONTH_NUM[m.group(2)], int(m.group(3)))
                buf = []
                continue

            m = TIME_LINE.match(line)
            if m:
                title = " ".join(buf).strip()
                buf = []
                # Collapse the hyphenation the PDF introduces when a title wraps
                title = re.sub(r"\s+", " ", title).strip(" -–")
                if not title or title.lower() in ("lunch",):
                    continue
                date = "%04d-%02d-%02d" % (int(m.group(4)), int(m.group(2)), int(m.group(3)))
                # Groups: 1 dow, 2 month, 3 day, 4 year, 5 "All day", 6 start, 7 end
                events.append({
                    "date": date,
                    "title": title,
                    "start": (m.group(6) or "").replace(" ", "") or None,
                    "end": (m.group(7) or "").replace(" ", "") or None,
                    "allDay": m.group(5) == "All day",
                    "course": course_of(title),
                    "type": classify(title),
                })
                continue

            buf.append(line)
        doc.close()

    # De-duplicate: a few events are listed twice (same day, same title) because
    # they span a lunch break and Outlook printed each half.
    seen, out = set(), []
    for e in sorted(events, key=lambda e: (e["date"], e["start"] or "")):
        k = (e["date"], e["title"])
        if k in seen:
            continue
        seen.add(k)
        out.append(e)
    return out


if __name__ == "__main__":
    evs = parse()
    print("total events:", len(evs), file=sys.stderr)
    from collections import Counter
    print("by type:", Counter(e["type"] for e in evs), file=sys.stderr)
    print("by course:", Counter(e["course"] for e in evs), file=sys.stderr)
    print(json.dumps(evs, indent=1))
