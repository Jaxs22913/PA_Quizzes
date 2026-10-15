#!/usr/bin/env python3
"""Round-trip test for tools/blind_review.py with a HAND-MADE fake judge (2026-10-15). No model is called.

Takes 3 real questions from a real quiz page, exports them, writes fake verdicts (one with a wrong quote,
one with a too-long justification), and checks: import accepts exactly the good ones and rejects the bad,
the audit export is REFUSED before any blind record exists, the audit export carries the key, and a wrong
audit quote is rejected. Uses a temp records file and a temp export dir OUTSIDE the repo; the real
tools/blind_review.json is never touched. Needs the Semester 2 inbox (decks) on this machine; skips otherwise.

    python3 tools/test_blind_review.py
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import blind_review as R

FOLDER, FILES = "Clinical Medicine and Surgery I Exam 4", "heart-failure-quiz.html"


def run(*args):
    p = subprocess.run([sys.executable, os.path.join(HERE, "blind_review.py"), "--records", REC] + list(args),
                       capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr


def first_quote(text):
    for line in text.split("\n"):
        if len(line.split()) >= 6 and not line.startswith("==="):
            return line
    raise SystemExit("no quotable line in evidence")


def main():
    if not os.path.isdir(R.INBOX):
        print("test_blind_review: SKIPPED (no Semester 2 inbox on this machine)")
        return 0
    global REC
    tmp = tempfile.mkdtemp(prefix="blind_review_test_", dir=os.path.expanduser("~/.cache"))
    REC = os.path.join(tmp, "records.json")
    d1, d2 = os.path.join(tmp, "blind"), os.path.join(tmp, "audit")
    try:
        # 1. the audit pass is refused before any blind record exists
        rc, out = run("export", "--pass", "audit", "--folder", FOLDER, "--files", FILES, "--sample", "3", "--out", d2)
        assert rc == 1 and "REFUSED" in out, (rc, out)
        # 2. an export directory inside the repo is refused
        rc, out = run("export", "--pass", "blind", "--folder", FOLDER, "--out", os.path.join(R.ROOT, "tools", "_nope"))
        assert rc != 0 and "refusing --out inside the repo" in out, out
        assert not os.path.exists(os.path.join(R.ROOT, "tools", "_nope"))
        # 3. blind export: 3 items, no key / explanations / mis anywhere in the batch
        rc, out = run("export", "--pass", "blind", "--folder", FOLDER, "--files", FILES, "--sample", "3", "--seed", "4", "--out", d1)
        assert rc == 0 and "exported 3 item(s)" in out, out
        batch = json.load(open(os.path.join(d1, "judge-001.json")))
        blob = json.dumps(batch)
        for forbidden in ('"key"', '"explanations"', '"mis"', "Correct."):
            assert forbidden not in blob, "blind batch leaks " + forbidden
        items = batch["items"]
        assert len(items) == 3 and all(sorted(i["options"]) == list("ABCD") for i in items)
        man = json.load(open(os.path.join(d1, "manifest.json")))
        ev = {k: man["items"][k]["evidence"] for k in man["items"]}
        good = lambda i: first_quote(list(ev[items[i]["id"]].values())[1])      # a real line from the cited slide
        # 4. fake judge: item 0 good, item 1 WRONG QUOTE, item 2 good but 'why' too long
        verdicts = [
            {"id": items[0]["id"], "pick": "B", "cover_answer": "monitor electrolytes and renal function", "why": "The slide says so.",
             "quote": good(0), "alt": None, "missing": None, "conflict": None, "clue": None},
            {"id": items[1]["id"], "pick": "A", "cover_answer": "x", "why": "Because.",
             "quote": "this sentence is certainly not on any slide of this deck", "alt": None, "missing": None, "conflict": None, "clue": None},
            {"id": items[2]["id"], "pick": "C", "cover_answer": "x", "why": " ".join(["word"] * 41),
             "quote": good(2), "alt": None, "missing": None, "conflict": None, "clue": None},
        ]
        json.dump(verdicts, open(os.path.join(d1, "verdict-001.json"), "w"))
        rc, out = run("import", "--pass", "blind", d1, "--judge", "fake-judge")
        assert rc == 1 and "'accepted': 1" in out and "'rejected': 2" in out, out
        repair = json.load(open(os.path.join(d1, "repair.json")))
        assert {r["id"] for r in repair} == {items[1]["id"], items[2]["id"]}
        assert "not verbatim" in [r["why"] for r in repair if r["id"] == items[1]["id"]][0]
        rec = json.load(open(REC))
        assert list(rec) == [items[0]["id"]] and rec[items[0]["id"]]["passes"]["blind"]["judge"] == "fake-judge"
        assert rec[items[0]["id"]]["passes"]["blind"]["pick_text"] == items[0]["options"]["B"]
        # 5. audit export now carries ONLY the reviewed item, with key + explanations + the judge's own result
        rc, out = run("export", "--pass", "audit", "--folder", FOLDER, "--files", FILES, "--sample", "3", "--seed", "4", "--only-reviewed", "--out", d2)
        assert rc == 0, out
        ab = json.load(open(os.path.join(d2, "judge-001.json")))
        assert [i["id"] for i in ab["items"]] == [items[0]["id"]]
        it = ab["items"][0]
        assert set(it["explanations"]) == set("ABCD") and it["key"] in "ABCD" and it["your_blind_result"]["pick"] == "B"
        # 6. audit verdicts: a pass with a defect is rejected; a revise with a wrong quote is rejected; a good revise is kept
        aman = json.load(open(os.path.join(d2, "manifest.json")))["items"][items[0]["id"]]
        q = list(aman["evidence"].values())[1]
        bad1 = {"id": it["id"], "verdict": "pass", "defects": [{"field": "A", "reason": "r", "quote": first_quote(q)}], "fix": None}
        bad2 = {"id": it["id"], "verdict": "revise", "defects": [{"field": "A", "reason": "r", "quote": "an invented sentence about nothing at all"}], "fix": "f"}
        for bad in (bad1, bad2):
            json.dump([bad], open(os.path.join(d2, "verdict-001.json"), "w"))
            rc, out = run("import", "--pass", "audit", d2, "--judge", "fake-judge")
            assert rc == 1 and "'accepted': 0" in out, out
        ok = {"id": it["id"], "verdict": "revise", "defects": [{"field": "explanation B", "reason": "claim not on slide", "quote": first_quote(q)}],
              "fix": "Delete the unsupported claim."}
        json.dump([ok], open(os.path.join(d2, "verdict-001.json"), "w"))
        rc, out = run("import", "--pass", "audit", d2, "--judge", "fake-judge")
        assert rc == 0 and "'accepted': 1" in out, out
        # 7. report and check: scope is empty (nothing fails); --all fails and names the item
        rc, out = run("report", "--folder", FOLDER)
        assert rc == 0 and "AUDIT REVISE: 1" in out, out
        rc, out = run("check", "--folder", FOLDER)
        assert rc == 0 and "0 question(s) in scope" in out, out
        rc, out = run("check", "--folder", FOLDER, "--all")
        assert rc == 1 and "FAIL" in out, out
        # 7b. with the page in scope, check fails on the unreviewed questions and counts the denominator
        sc = os.path.join(tmp, "scope.json")
        json.dump({"globs": [FOLDER + "/" + FILES]}, open(sc, "w"))
        rc, out = run("--scope", sc, "check", "--folder", FOLDER)
        assert rc == 1 and "0/30 in-scope" in out, out
        # 8. an edit invalidates records: same stem, one option changed -> a different hash
        a = R.item_hash("S?", ["a", "b", "c", "d"])
        assert a == R.item_hash("S?", ["d", "c", "b", "a"]) and a != R.item_hash("S?", ["a", "b", "c", "e"])
        print("test_blind_review: all checks passed (exit 0)")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
