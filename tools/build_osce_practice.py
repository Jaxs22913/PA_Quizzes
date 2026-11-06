#!/usr/bin/env python3
"""Build the OSCE practice station files (cardiac 2026-10-26, pulmonary 2026-11-06).

Jaxon: "talk out loud back and forth with the site like it was a patient, using the info from our ppts ... and you
know all we have to do and ask so it can grade us."

One JSON per station, read by BOTH the practice page (osce-practice.html: the case list, the door form, the report)
and the private helper (the patient model plays the case, the grader grades against the rubric and the key):

  Physical Diagnosis 2 Exam 1/pd2-cardiac-osce-practice.json     (station "cardiac")
  Physical Diagnosis 2 Exam 2/pd2-pulm-osce-practice.json        (station "pulmonary")
    rubric   the station's OSCE run-sheet (tools/build_pd2_osce.py CARDIAC or PULMONARY), every item with an id
             ("s5.12"), its kind (say = graded on what is said, do = performed, credited when narrated), its group
             heading, and "auto" for the items only the page can judge (time at the door, the presentation's
             length) or the student (reading from notes)
    catalog  the maneuvers and their normal findings (tools/_osce_cardiac_catalog.py, tools/_osce_pulm_catalog.py)
    cases    the cases (tools/_osce_cardiac_cases.py, tools/_osce_pulm_cases.py): door form, persona, facts, exam
             overrides, answer key, and the tests a student can order for that case (results shown on screen; a
             test the setting can't do says so; anything not listed gets "unlisted", Jaxon: "they will say oh that
             machine is down but only with stuff that isnt relevant or isnt in where we are")

The helper's station list (superbrain/src/osce.ts STATIONS) names these paths; renaming a file means changing both.

    python3 tools/build_osce_practice.py                       # write both files
    python3 tools/build_osce_practice.py --station pulmonary   # just one (cardiac | pulmonary)
    python3 tools/build_osce_practice.py --check               # exit 1 if a file on disk is not what this would write
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import build_pd2_osce as runsheet                                   # noqa: E402
from _osce_cardiac_catalog import CATALOG as CARDIAC_CATALOG        # noqa: E402
from _osce_cardiac_cases import CASES as CARDIAC_CASES              # noqa: E402
from _osce_pulm_catalog import CATALOG as PULM_CATALOG              # noqa: E402
from _osce_pulm_cases import CASES as PULM_CASES, check as pulm_selfcheck   # noqa: E402
from _pd2_cardiac_osce_ecgs import IMAGES as ECG_IMAGES             # noqa: E402

UNLISTED = "That machine is down today."

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


def rubric(spec):
    out = []
    for sec in spec["sections"]:
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


def check_case(c, catalog_ids, st):
    cid = c["id"]
    assert re.match(r"^[a-z0-9][a-z0-9-]{2,80}$", cid), cid
    assert c["door"]["sex"] in ("male", "female"), (cid, c["door"]["sex"])
    assert len(c["door"]["cc"]) < 90, (cid, "chief complaint over 90 characters")
    bad = [k for k in c["exam"] if k not in catalog_ids]
    assert not bad, (cid, "exam overrides for maneuvers not in the catalog", bad)
    for m in c["special"]:
        assert len(m) == 4 and m[0] not in catalog_ids, (cid, "special maneuver", m[0])
    known = set(catalog_ids) | {m[0] for m in c["special"]}
    must = c.get("must_exam") or []
    assert 3 <= len(must) <= 6 and all(m in known for m in must), (cid, "must_exam", must)
    tests = c.get("tests") or []
    assert 3 <= len(tests) <= 14, (cid, "tests", len(tests))
    tids = [t["id"] for t in tests]
    assert len(tids) == len(set(tids)), (cid, "duplicate test id")
    for t in tests:
        assert set(t) <= {"id", "name", "aka", "result", "here", "img", "cap"}, (cid, t["id"], "unknown test field", set(t))
        assert re.match(r"^[a-z0-9][a-z0-9-]{1,30}$", t["id"]) and t["id"] != "other", (cid, "test id", t["id"])
        assert t["id"] not in known, (cid, t["id"], "a test id is also a maneuver id")
        assert 2 <= len(t["name"]) <= 80 and isinstance(t.get("aka", []), list), (cid, t["id"], "name/aka")
        assert all(isinstance(a, str) and 1 <= len(a) <= 60 for a in t.get("aka", [])), (cid, t["id"], "aka")
        assert 8 <= len(t["result"]) <= 600, (cid, t["id"], "result length")
        assert isinstance(t["here"], bool), (cid, t["id"], "here must be true or false")
        if t.get("img"):
            assert t["here"], (cid, t["id"], "a picture for a test the setting can't do")
            assert t["img"] in st["images"], (cid, t["id"], "picture not in the chart's vetted set", t["img"])
            assert os.path.exists(os.path.join(ROOT, st["folder"], st["img_dir"], t["img"])), (cid, t["id"], "missing picture")
            assert 10 <= len(t.get("cap") or "") <= 300, (cid, t["id"], "a picture needs a caption")
        else:
            assert not t.get("cap"), (cid, t["id"], "a caption with no picture")


def ecg_credit(fn):
    """The picture's credit, worded as on the Cardiac OSCE chart."""
    src, boxes = ECG_IMAGES[fn]
    if src["kind"] == "deck":
        return {"text": "Source: %s, Slide %d%s" % (src["deck"], src["slide"], "; yellow boxes added" if boxes else ""), "page": ""}
    assert src["lic"] and src["author"] and src["page"], fn
    return {"text": "Image: %s%s, Wikimedia Commons, %s; %s" % (src["author"], "; " + src["extra"] if src["extra"] else "", src["lic"],
                                                              "resized, yellow boxes added" if boxes else "resized"),
            "page": src["page"]}


# The stations. Test pictures come only from each station's OSCE Disease Chart, already vetted there: the Cardiac
# chart's 12-leads (sources and licences in _pd2_cardiac_osce_ecgs.py); the Pulmonary chart's pictures are not
# wired in yet, so no pulmonary test carries one.
STATIONS = {
    "cardiac": dict(folder="Physical Diagnosis 2 Exam 1", file="pd2-cardiac-osce-practice.json", title="Cardiac OSCE",
                    runsheet=runsheet.CARDIAC, catalog=CARDIAC_CATALOG, cases=CARDIAC_CASES,
                    img_dir="pd2-cardiac-osce-chart-images", images=ECG_IMAGES, credit=ecg_credit, selfcheck=None),
    "pulmonary": dict(folder="Physical Diagnosis 2 Exam 2", file="pd2-pulm-osce-practice.json", title="Pulmonary OSCE",
                      runsheet=runsheet.PULMONARY, catalog=PULM_CATALOG, cases=PULM_CASES,
                      img_dir="pd2-pulm-osce-images", images={}, credit=None, selfcheck=pulm_selfcheck),
}


def out_path(st):
    return os.path.join(ROOT, st["folder"], st["file"])


def test_out(t, st):
    o = {"id": t["id"], "name": t["name"], "aka": list(t.get("aka", [])), "result": t["result"], "here": t["here"]}
    if t.get("img"):
        o.update(img=st["img_dir"] + "/" + t["img"], cap=t["cap"], credit=st["credit"](t["img"]))
    return o


def build(key):
    st = STATIONS[key]
    if st["selfcheck"]:
        st["selfcheck"](st["cases"])   # the case module's own rules (the cardiac one runs as its own script)
    catalog = {k: {"name": v[0], "does": v[1], "normal": v[2]} for k, v in st["catalog"].items()}
    cases = []
    for c in st["cases"]:
        check_case(c, catalog, st)
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
            # the examinations specific to this condition: each one never performed costs a point (the page docks it)
            "must_exam": list(c["must_exam"]),
            "tests": [test_out(t, st) for t in c["tests"]],
            "key": c["key"],
        })
    ids = [c["id"] for c in cases]
    assert len(ids) == len(set(ids)), "duplicate case id"
    return {
        "v": 1,
        "station": key,
        "title": st["title"],
        "minutes": {"door": 1, "room": 20},
        "rubric": rubric(st["runsheet"]),
        "catalog": catalog,
        "unlisted": UNLISTED,
        "cases": cases,
    }


def main():
    args = sys.argv[1:]
    keys = list(STATIONS)
    if "--station" in args:
        i = args.index("--station")
        want = args[i + 1] if i + 1 < len(args) else ""
        if want not in STATIONS:
            sys.exit("--station must be one of: " + ", ".join(STATIONS))
        keys = [want]
    stale = 0
    for key in keys:
        out = out_path(STATIONS[key])
        text = json.dumps(build(key), ensure_ascii=False, separators=(",", ":")) + "\n"
        if "--check" in args:
            same = os.path.exists(out) and open(out, encoding="utf-8").read() == text
            print("%s station file up to date" % key if same else
                  "%s station file is STALE: run tools/build_osce_practice.py --station %s" % (key, key))
            stale += not same
            continue
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        j = json.loads(text)
        n = sum(len(s["items"]) for s in j["rubric"])
        print("wrote %s: %d rubric items in %d sections, %d maneuvers, %d cases (%d bytes)" % (
            os.path.relpath(out, ROOT), n, len(j["rubric"]), len(j["catalog"]), len(j["cases"]), len(text.encode())))
    sys.exit(1 if stale else 0)


if __name__ == "__main__":
    main()
