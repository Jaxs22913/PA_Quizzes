#!/usr/bin/env python3
"""Verify every <folder>/guide-links.json (the study-guide panel's data).

The panel is a study aid on graded material, so a stale or wrong link must fail
loudly here rather than quietly mislead someone. Checks, per Semester 2 quiz
folder:

  1. the file exists and is version 1 (a missing file is a console 404 on
     every quiz load);
  2. every link's guide file exists in the folder and its anchor id is really
     in that guide;
  3. every highlight snippet still occurs in the guide's text (whitespace
     ignored, exactly how the panel finds it), and a snippet's paragraph lies
     at/after its anchor;
  4. no link belongs to a question that no longer exists (orphans = the quiz
     was edited or rebuilt: re-run tools/build_guide_links.py);
  5. Semester 1 (frozen) folders carry NO guide-links.json.

Prints the denominator (questions and how many are linked) per folder.
Exit 1 on any failure.

--strict  (the STANDING RULE, Jaxon 2026-09-28: "all questions should link back
          to where the concept is explained"): also fail for any question whose
          link is only a 'closest section' guess, i.e. whose fact the class
          guide does not actually explain. Fix by adding the fact to the guide
          (tools/guide_additions/, tools/apply_guide_additions.py), then
          re-run tools/build_guide_links.py. Run this at the end of EVERY
          Semester 2 quiz or exam build.
"""
import glob
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_guide_links as B  # noqa: E402

ROOT = B._REPO
FROZEN = ("Anatomy Exam", "Anatomy Practicum Exam", "CAM Nutrition Exam", "Intro to PA", "Nutrition Class",
          "Pharmacodynamics", "Physical Diagnosis 1", "Physiology Exam")


def guide_text(path):
    s = open(path, encoding="utf-8").read()
    s = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)
    return s, re.sub(r"\s+", "", html.unescape(re.sub(r"<[^>]+>", "", s)))


def main():
    fails, total_q, total_l = [], 0, 0
    strict_near = []
    for d in sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, d)
        if not os.path.isdir(p):
            continue
        lf = os.path.join(p, "guide-links.json")
        if d.startswith(FROZEN):
            if os.path.exists(lf):
                fails.append("%s: Semester 1 folder must not carry guide-links.json" % d)
            continue
        quizzes = []
        for f in sorted(glob.glob(os.path.join(p, "*.html"))):
            Q = B.load_questions(f)
            if Q:
                quizzes.append(Q)
        if not quizzes:
            continue
        if not os.path.exists(lf):
            fails.append("%s: guide-links.json missing" % d)
            continue
        try:
            data = json.load(open(lf, encoding="utf-8"))
        except Exception as e:
            fails.append("%s: unreadable (%s)" % (d, e))
            continue
        if data.get("v") != 1 or "g" not in data or "l" not in data:
            fails.append("%s: wrong shape" % d)
            continue
        keys = {B.qkey(q) for Q in quizzes for q in Q}
        cache = {}
        bad = 0
        near = 0
        for k, row in data["l"].items():
            gi, anchor, title, snip = row[:4]
            near += 1 if len(row) > 4 else 0
            if k not in keys:
                fails.append("%s: orphan link %s (%s) - question edited/removed" % (d, k, title))
                bad += 1
                continue
            g = data["g"][gi]
            gp = os.path.join(p, g)
            if not os.path.exists(gp):
                fails.append("%s: guide %s missing" % (d, g)); bad += 1; continue
            if g not in cache:
                cache[g] = guide_text(gp)
            raw, flat = cache[g]
            m = re.search(r'id="%s"' % re.escape(anchor), raw)
            if not m:
                fails.append("%s: anchor #%s not in %s (%s)" % (d, anchor, g, title)); bad += 1; continue
            if snip:
                want = re.sub(r"\s+", "", snip)
                after = re.sub(r"\s+", "", html.unescape(re.sub(r"<[^>]+>", "", raw[m.start():])))
                if want not in after:
                    fails.append("%s: snippet not at/after #%s in %s: %r" % (d, anchor, g, snip[:50])); bad += 1
        nl = len(data["l"])
        strict_near.append((d, near))
        total_q += len(keys)
        total_l += nl
        print("%-46s %5d q, %5d linked (%3d%%; %d exact-source, %d closest-section)%s" % (
            d, len(keys), nl, round(100 * nl / max(1, len(keys))), nl - near, near, "  FAIL x%d" % bad if bad else ""))
    print("TOTAL %d questions, %d linked (%d%%)" % (total_q, total_l, round(100 * total_l / max(1, total_q))))
    if "--strict" in sys.argv:
        for d, n_near in strict_near:
            if n_near:
                fails.append("%s: %d question(s) have no passage that explains them (closest-section guess only)" % (d, n_near))
    if fails:
        print("\nFAIL (%d):" % len(fails))
        for f in fails[:40]:
            print(" -", f)
        sys.exit(1)
    print("OK: every link resolves.")


if __name__ == "__main__":
    main()
