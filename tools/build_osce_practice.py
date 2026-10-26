#!/usr/bin/env python3
"""Build the OSCE practice station file (2026-10-26).

Jaxon: "talk out loud back and forth with the site like it was a patient, using the info from our ppts ... and you
know all we have to do and ask so it can grade us."

One JSON per station, read by BOTH the practice page (osce-practice.html: the case list, the door form, the report)
and the private helper (the patient model plays the case, the grader grades against the rubric and the key):

  Physical Diagnosis 2 Exam 1/pd2-cardiac-osce-practice.json
    rubric   the Cardiac OSCE run-sheet (tools/build_pd2_osce.py CARDIAC), every item with an id ("s5.12"), its kind
             (say = graded on what is said, do = performed, credited when narrated), its group heading, and "auto"
             for the items only the page can judge (time at the door, the presentation's length) or the student
             (reading from notes)
    catalog  the maneuvers and their normal findings (tools/_osce_cardiac_catalog.py)
    cases    the cases (tools/_osce_cardiac_cases.py): door form, persona, facts, exam overrides, answer key

The helper's station list (superbrain/src/osce.ts STATIONS) names this path; renaming the file means changing both.

    python3 tools/build_osce_practice.py          # write the file
    python3 tools/build_osce_practice.py --check  # exit 1 if the file on disk is not what this would write
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import build_pd2_osce as runsheet            # noqa: E402
from _osce_cardiac_catalog import CATALOG    # noqa: E402
from _osce_cardiac_cases import CASES        # noqa: E402

OUT = os.path.join(ROOT, "Physical Diagnosis 2 Exam 1", "pd2-cardiac-osce-practice.json")

# Items the transcript cannot show. "door" and "length" the page measures; "self" the student ticks in the report.
AUTO = {
    "Reviews the chief complaint and vital signs on the form before entering the room": "door",
    "Keeps it to about one minute": "length",
    "Delivers it without reading from notes": "self",
}


def plain(s):
    """Run-sheet HTML -> plain text (tags out, entities decoded, spaces tidied)."""
    if s is None:
        return None
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s).replace(" ", " ")
    return re.sub(r"\s+", " ", s).strip()


def rubric():
    out = []
    for sec in runsheet.CARDIAC["sections"]:
        items, group, k = [], None, 0
        for kind, payload in sec["blocks"]:
            if kind == "h4":
                group = plain(payload)
            elif kind == "items":
                for it in payload:
                    k += 1
                    text = plain(it[1])
                    row = {"id": "%s.%d" % (sec["id"], k), "kind": it[0], "text": text}
                    if group:
                        row["group"] = group
                    if it[2]:
                        row["script"] = plain(it[2])
                    if text in AUTO:
                        row["auto"] = AUTO[text]
                    items.append(row)
        out.append({"id": sec["id"], "title": plain(sec["title"]), "items": items})
    return out


def check_case(c, catalog_ids):
    cid = c["id"]
    assert re.match(r"^[a-z0-9][a-z0-9-]{2,80}$", cid), cid
    assert c["door"]["sex"] in ("male", "female"), (cid, c["door"]["sex"])
    assert len(c["door"]["cc"]) < 90, (cid, "chief complaint over 90 characters")
    bad = [k for k in c["exam"] if k not in catalog_ids]
    assert not bad, (cid, "exam overrides for maneuvers not in the catalog", bad)
    for m in c["special"]:
        assert len(m) == 4 and m[0] not in catalog_ids, (cid, "special maneuver", m[0])


def build():
    catalog = {k: {"name": v[0], "does": v[1], "normal": v[2]} for k, v in CATALOG.items()}
    cases = []
    for c in CASES:
        check_case(c, catalog)
        cases.append({
            "id": c["id"],
            "condition": c["condition"],
            # the page puts the chief complaint in quotation marks itself
            "door": {**c["door"], "cc": c["door"]["cc"].strip().strip('"\u201c\u201d').strip(),
                     "vitals": [list(v) for v in c["door"]["vitals"]]},
            "persona": c["persona"],
            "opening": c["opening"],
            "facts": [list(f) for f in c["facts"]],
            "questions": list(c["questions"]),
            "exam": dict(c["exam"]),
            "special": [list(m) for m in c["special"]],
            "key": c["key"],
        })
    ids = [c["id"] for c in cases]
    assert len(ids) == len(set(ids)), "duplicate case id"
    return {
        "v": 1,
        "station": "cardiac",
        "title": "Cardiac OSCE",
        "minutes": {"door": 1, "room": 20},
        "rubric": rubric(),
        "catalog": catalog,
        "cases": cases,
    }


def main():
    text = json.dumps(build(), ensure_ascii=False, separators=(",", ":")) + "\n"
    if "--check" in sys.argv:
        same = os.path.exists(OUT) and open(OUT, encoding="utf-8").read() == text
        print("station file up to date" if same else "station file is STALE: run tools/build_osce_practice.py")
        sys.exit(0 if same else 1)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text)
    st = json.loads(text)
    n = sum(len(s["items"]) for s in st["rubric"])
    print("wrote %s: %d rubric items in %d sections, %d maneuvers, %d cases (%d bytes)" % (
        os.path.relpath(OUT, ROOT), n, len(st["rubric"]), len(st["catalog"]), len(st["cases"]), len(text.encode())))


if __name__ == "__main__":
    main()
