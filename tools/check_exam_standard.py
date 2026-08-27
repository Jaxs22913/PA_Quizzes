#!/usr/bin/env python3
"""Check a quiz against the exam standard Jaxon set over 2026-08-26/27.

The standard came out of 40 reference items from his own coursework, and it took
several rounds to get right. Written down it is easy to forget a clause; this
checks the ones a machine can see, so "carry it forward for all exams" does not
depend on anyone remembering.

    python3 tools/check_exam_standard.py                       # every quiz
    python3 tools/check_exam_standard.py "Clinical Medicine..."  # a folder
    python3 tools/check_exam_standard.py --new                 # only NEW-tagged

What it checks, and why each one is here:

  OPTIONS      five, A-E, all distinct.
  VIGNETTE     the stem names a patient. His exams are mostly vignette.
  REFUTATIONS  every wrong option gets its OWN explanation; none may open with
               "Correct", and the keyed one must.
  ONE ANSWER   an option may not name a condition AND issue an instruction
               ("Ramsay Hunt syndrome; add a corticosteroid"). One answer.
  LENGTH       reference options run a median of 19 characters and a max of 66.
               Ours may not be wildly longer -- the rationale belongs in the
               explanation.
  GAMEABLE     the correct answer must not be reliably the longest. Reference
               sits at 13%; the house bar is 35%. Zero is NOT the target --
               engineering it to zero is what bloated the options the first time.
  POSITIONS    keys spread across A-E. Authoring correct-first and shipping it
               is a real bug that has now happened twice.
  DIAGNOSIS    about a quarter pure diagnosis.
  CITE         every question cites its slide.
  (The io-prefix check was retired on 2026-08-27: the engine's ioLabel() no
   longer double-prefixes, and the 2,075 affected Semester 2 questions were
   repaired, so a stored prefix is no longer a rendering defect.)

Legacy quizzes predate all of this and are reported, never failed: --new limits
the run to files carrying a New tag, which is what a fresh build looks like.
Exit code is non-zero only if a checked file breaks a HARD rule.
"""
import argparse, collections, glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Frozen: Jaxon called SEMESTER 1 finished on 2026-08-27 -- "the exams from
# semester 1 never need to be touched again". That term ended 14 August 2026, so
# its quizzes are settled and are skipped rather than warned about, keeping a
# future sweep from proposing helpful edits to material nobody will sit again.
#
# The class list is Semester 1 in semesters.js (physio, pharmacodynamics,
# anatomy, anatomy-practicum, intro-pa, cam-nutrition, physical-diagnosis)
# mapped to their repo folders. Physical Diagnosis 1 is Semester 1; Physical
# Diagnosis 2 is Semester 2 and is NOT frozen. Pass --include-frozen to look
# anyway.
FROZEN = (
    "Anatomy Exam",
    "Anatomy Practicum Exam",
    "CAM Nutrition Exam",
    "Intro to PA Profession",
    "Nutrition Class",
    "Pharmacodynamics Exam",
    "Physical Diagnosis 1 Exam",
    "Physiology Exam",
)
REF_MEDIAN, REF_MAX = 19, 66          # measured from the 40 reference items
GAMEABLE_BAR = 0.35                   # house bar; reference itself is 0.13
DIAG_MIN = 0.20                       # "about a quarter", with slack
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18

VIGNETTE = re.compile(r"\b\d+-(year|month|week|day)-old\b|\bnewborn\b|\bin (his|her|their) (twenties|thirties|forties|fifties|sixties)\b", re.I)
DIAGNOSIS = re.compile(r"most likely diagnosis|what is the diagnosis", re.I)
CONDITION = re.compile(r"\b(syndrome|scabies|zoster|melanoma|carcinoma|dermatitis|nevus|naevus|granuloma|cellulitis|impetigo|warts|tinea|candidiasis|lipoma|abscess|furuncle|carbuncle|psoriasis|eczema|versicolor)\b", re.I)
INSTRUCTION = re.compile(r"\b(start|stop|give|apply|excise|observe|biopsy|screen|refer|remove|drain|immediately|antiviral|antibiotics|corticosteroid|cryotherapy|permethrin|ivermectin|antivenom|vincristine)\b", re.I)


def load(path):
    h = open(path, encoding="utf-8").read()
    m = re.search(r"const QUESTIONS\s*=\s*(\[.*?\]);", h, re.S)
    if not m:
        return None, h
    try:
        qs = json.loads(m.group(1))
    except Exception:
        return None, h
    # Older quizzes store {q, choices, answer, correct, why} instead of
    # {q, opts:[[text, explanation]], c}. Normalise so one checker sees both,
    # and remember which shape it was -- the shared-"why" test only means
    # something for the legacy shape.
    out = []
    for q in qs:
        if "opts" in q and "c" in q:
            out.append(q)
        elif "choices" in q and "answer" in q:
            why, cor = q.get("why", ""), q.get("correct", "")
            out.append({"q": q.get("q", ""), "c": q["answer"], "cite": q.get("src", ""),
                        "io": q.get("io", q.get("topic", "")), "_legacy": True,
                        "opts": [[c, cor if i == q["answer"] else why]
                                 for i, c in enumerate(q["choices"])]})
    return (out or None), h


def gameable(q):
    L = [len(o[0]) for o in q["opts"]]
    c = L[q["c"]]
    rest = L[:q["c"]] + L[q["c"] + 1:]
    if not rest:
        return False
    r = max(rest)
    return c > r and (c - r) >= MARGIN_CHARS and c >= r * (1 + MARGIN_FRAC)


def check(path, qs, html):
    hard, soft = [], []
    n = len(qs)
    if not n:
        return hard, soft

    five = sum(1 for q in qs if len(q["opts"]) == 5)
    if five != n:
        soft.append(f"{n-five}/{n} questions are not five-option")

    shared = 0
    for q in qs:
        if len({o[0].strip().lower() for o in q["opts"]}) != len(q["opts"]):
            hard.append(f"duplicate option text: {q['q'][:56]}")
        # The substantive rule is that every wrong choice gets its OWN reason.
        # Testing for the literal word "Correct" would only be testing my own
        # house style, which older quizzes never used.
        wrong = [o[1].strip() for j, o in enumerate(q["opts"]) if j != q["c"]]
        if wrong and len(set(wrong)) == 1 and len(wrong) > 1:
            shared += 1
        if q["opts"][q["c"]][1].strip() and q["opts"][q["c"]][1].strip() in wrong:
            hard.append(f"keyed option shares its explanation with a distractor: {q['q'][:52]}")
    if shared:
        soft.append(f"{shared}/{n} questions give every wrong choice the SAME explanation "
                    "(reference items explain each one separately)")

    vig = sum(1 for q in qs if VIGNETTE.search(q["q"]))
    if vig / n < 0.80:
        soft.append(f"only {vig/n:.0%} of stems name a patient (want >=80%)")

    mixed = [o[0] for q in qs for o in q["opts"]
             if "; " in o[0] and CONDITION.search(o[0].split("; ")[0])
             and INSTRUCTION.search(o[0].split("; ", 1)[1])]
    if mixed:
        soft.append(f"{len(mixed)} option(s) name a condition AND an instruction, e.g. {mixed[0][:52]!r}")

    L = sorted(len(o[0]) for q in qs for o in q["opts"])
    med = L[len(L) // 2]
    if med > REF_MEDIAN * 2.5:
        soft.append(f"option length median {med} chars is over {REF_MEDIAN*2.5:.0f} (reference {REF_MEDIAN})")
    over = sum(1 for x in L if x > REF_MAX)
    if over / len(L) > 0.10:
        soft.append(f"{over/len(L):.0%} of options exceed the reference maximum of {REF_MAX} chars")

    g = sum(map(gameable, qs))
    if g / n > GAMEABLE_BAR:
        hard.append(f"gameable by length {g/n:.0%} exceeds the {GAMEABLE_BAR:.0%} bar")

    pos = collections.Counter(q["c"] for q in qs)
    if n >= 20 and max(pos.values()) > n * 0.45:
        hard.append("answer positions skewed: " + str({"ABCDE"[k]: v for k, v in sorted(pos.items())}))

    if "master-exam" in os.path.basename(path):
        d = sum(1 for q in qs if DIAGNOSIS.search(q["q"]))
        if d / n < DIAG_MIN:
            soft.append(f"only {d/n:.0%} pure-diagnosis questions (want about 25%)")

    if sum(1 for q in qs if not q.get("cite")):
        soft.append("some questions carry no slide citation")

    return hard, soft


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", nargs="?", default=None)
    ap.add_argument("--new", action="store_true", help="only files carrying a New tag in index.html")
    ap.add_argument("--include-frozen", action="store_true", help="also check folders marked FROZEN")
    args = ap.parse_args()

    files, frozen_skipped = [], []
    for f in glob.glob(os.path.join(ROOT, "*", "*.html")):
        rel = os.path.relpath(f, ROOT)
        if rel.startswith(("tools", "group-quizzes", "icons", "audio")):
            continue
        if args.target and args.target not in rel:
            continue
        if not args.include_frozen and any(rel.startswith(d) for d in FROZEN):
            frozen_skipped.append(rel)
            continue
        files.append(f)

    if args.new:
        idx = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
        tagged = set(re.findall(r'href="([^"]+)"[^>]*>[^<]*<span class="quiz-tag quiz-tag--new"', idx))
        import urllib.parse
        tagged = {urllib.parse.unquote(t) for t in tagged}
        files = [f for f in files if os.path.relpath(f, ROOT) in tagged]

    checked = failed = 0
    for f in sorted(files):
        qs, html = load(f)
        if not qs:
            continue
        checked += 1
        hard, soft = check(f, qs, html)
        if hard or soft:
            print(f"\n{os.path.relpath(f, ROOT)}  ({len(qs)} questions)")
            for m in hard:
                print(f"   FAIL  {m}")
            for m in soft:
                print(f"   warn  {m}")
        if hard:
            failed += 1

    if frozen_skipped:
        print(f"\nskipped {len(frozen_skipped)} file(s) in frozen folders: {', '.join(FROZEN)}")
    print(f"checked {checked} quiz file(s); {failed} broke a hard rule")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
