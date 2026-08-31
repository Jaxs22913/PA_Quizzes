#!/usr/bin/env python3
"""Fail any question that cites its own source.

A question has to stand on its own: a student reading it should never need to
know which lecture, deck, slide, syllabus or professor it came from.  Deleting
the attribution is the fix — relabelling it "the material" was tried and
rejected.  Deletion strands verbs and genitives, so rewrite the sentence rather
than snipping the phrase out.

  python3 tools/check_self_contained.py                 # every quiz on the site
  python3 tools/check_self_contained.py "Some Exam 2"   # one folder
  python3 tools/check_self_contained.py --review        # also list pronoun
                                                        # candidates to eyeball

Only Semester 2 and forward are in scope; Semester 1 exams are frozen.
"""
import glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _selfcontain_rx import RX, REVIEW_RX

SKIP = ("guide", "cram", "chart", "atlas", "practicum")
FROZEN = ("Anatomy", "Physiology", "Physical Diagnosis 1", "Medical Literature")


def questions(path):
    m = re.search(r'const QUESTIONS\s*=\s*(\[.*?\]);\s*\n',
                  open(path, encoding="utf8").read(), re.S)
    return json.loads(m.group(1)) if m else None


def scan(roots, review=False):
    bad = files = scanned = 0
    for root in roots:
        for path in sorted(glob.glob(os.path.join(root, "**", "*.html"), recursive=True)):
            name = os.path.basename(path).lower()
            if any(k in name for k in SKIP):
                continue
            try:
                qs = questions(path)
            except Exception:
                continue
            if not qs:
                continue
            scanned += 1
            hits = []
            for i, q in enumerate(qs):
                if not isinstance(q, dict) or "q" not in q or "opts" not in q:
                    continue                       # older schemas, e.g. matching decks
                fields = [("stem", q["q"])]
                for j, o in enumerate(q["opts"]):
                    fields.append(("option %d" % j, o[0]))
                    if len(o) > 1:
                        fields.append(("explanation %d" % j, o[1]))
                for label, text in fields:
                    for m in RX.finditer(text):
                        hits.append((i, label, m.group(0), text))
                    if review:
                        for m in REVIEW_RX.finditer(text):
                            hits.append((i, label + " [review]", m.group(0), text))
            if hits:
                files += 1
                print("\n%s" % path)
                for i, label, frag, text in hits:
                    bad += 1
                    print("  #%-3d %-16s \"%s\"\n       %s" % (i, label, frag, text[:150]))
    print("\n%d quiz file(s) scanned | %d citation(s) in %d file(s)" % (scanned, bad, files))
    return bad


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--review"]
    roots = args or [d for d in glob.glob("*") if os.path.isdir(d)
                     and not d.startswith(".") and not any(f in d for f in FROZEN)]
    sys.exit(1 if scan(roots, review="--review" in sys.argv) else 0)
