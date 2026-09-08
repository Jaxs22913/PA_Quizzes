#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Every question stem must actually ask something.

A stem that states a scenario and stops is not a question -- the student has to
reverse-engineer what is being asked from the options, and two different
lead-ins over the same vignette have different correct answers
([[vignette_question_style]]: "lead-in decides the answer").

Written after 364 CMS Exam 3 stems shipped on 2026-09-08 with no lead-in at
all. Nothing caught it: the style contracts of the day checked explanation
depth, banned phrases and option length, and every one of those passed. Run
this on every quiz build.

A stem counts as asking something if it contains a question mark, an imperative
that names the task ("select", "choose", "identify", "which of"), OR if it is a
SENTENCE-COMPLETION stem -- one ending in a colon or ellipsis, as in "The
internal urethral sphincter is formed by:". Completion stems are a standard and
perfectly clear MCQ format and the first version of this check wrongly flagged
150 files' worth of them; what is being caught here is narrower, and worse: a
stem that ends in a full stop having asked nothing at all.

Picture-stem items are exempt: the photograph is the stem.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Question mark, an interrogative, or an IMPERATIVE that names the task. The
# imperative list is deliberately broad -- "Describe the appearance of a
# dysplastic naevus." and "Rank the following from fastest to slowest." both
# tell the student exactly what to do, and neither needs a question mark.
IMPERATIVE = re.compile(r"(?i)^\s*(select|choose|identify|describe|rank|place|"
                        r"order|list|predict|state|give|match|arrange|name|"
                        r"calculate|estimate|determine|explain|classify|"
                        r"interpret|indicate|specify)\b")


def asks(stem):
    """True if the stem asks the student something.

    Two legitimate shapes, and one defect:

      QUESTION    ends with "?", or opens with an imperative that names the
                  task ("Describe the appearance of...", "Rank the following").
      COMPLETION  does not end in a full stop -- the options finish the
                  sentence. "The internal urethral sphincter is formed by:" and
                  "The primary function of the kidneys is to" are both this.
      DEFECT      a grammatically complete sentence, ending in a full stop,
                  that asks nothing. The student must guess the question from
                  the options.

    Testing for the DEFECT directly is what makes this stable. Enumerating
    every way a completion stem can trail off was a losing game -- ":", "...",
    "is to", "approximately", "also called" -- and each miss was a false
    positive on frozen content.
    """
    t = stem
    t = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t)).strip()
    if not t:
        return True
    if "?" in t:                      # an explicit question
        return True
    if not t.endswith("."):           # completion stem: the options finish it
        return True
    if t.endswith("..."):             # ditto, ellipsis form
        return True
    return bool(IMPERATIVE.match(t))  # "Describe...", "Rank...", "List..."


def stems(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'"q"\s*:\s*"((?:[^"\\]|\\.)*)"', s):
        try:
            out.append(json.loads('"%s"' % m.group(1)))
        except ValueError:
            pass
    # A picture-stem question carries its stem in the image.
    has_img = '"img"' in s
    return out, has_img


def main(argv):
    prefix = argv[1] if len(argv) > 1 else ""
    files, bad, total, flagged = [], [], 0, 0
    for dirpath, _dirs, names in os.walk(ROOT):
        if os.sep + "." in dirpath or "group-quizzes" in dirpath or "tools" in dirpath:
            continue
        for n in names:
            if not n.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(dirpath, n), ROOT)
            if prefix and not rel.startswith(prefix):
                continue
            files.append(rel)

    for rel in sorted(files):
        qs, has_img = stems(os.path.join(ROOT, rel))
        if not qs:
            continue
        miss = [(i, q) for i, q in enumerate(qs) if not asks(q)]
        total += len(qs)
        if miss and not has_img:
            flagged += 1
            bad.append((rel, len(qs), miss))

    for rel, n, miss in bad:
        print("\n%s  (%d of %d stems ask nothing)" % (rel, len(miss), n))
        for i, q in miss[:3]:
            print("   #%-3d %s" % (i, re.sub(r"<[^>]+>", "", q)[:96]))
        if len(miss) > 3:
            print("   ... and %d more" % (len(miss) - 3))

    print("\n%d stems scanned across %d quiz file(s); %d file(s) contain a stem "
          "that asks nothing" % (total, len(files), flagged))
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
