#!/usr/bin/env python3
"""Check a quiz against the exam standard Jaxon set over 2026-08-26/27.

The standard came out of 40 reference items from his own coursework, and it took
several rounds to get right. Written down it is easy to forget a clause; this
checks the ones a machine can see, so "carry it forward for all exams" does not
depend on anyone remembering.

    python3 tools/check_exam_standard.py                       # every quiz
    python3 tools/check_exam_standard.py "Clinical Medicine..."  # a folder
    python3 tools/check_exam_standard.py --new                 # only NEW-tagged
    python3 tools/check_exam_standard.py --new --days 3        # ...still showing

What it checks, and why each one is here:

  OPTIONS      FOUR, A-D, all distinct. A HARD rule since 2026-09-13 ("All
               should be 4 answer choices not 5"); the five-option shape of the
               2026-08-27 reference items was reversed site-wide.
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
  POSITIONS    keys spread across A-D. Authoring correct-first and shipping it
               is a real bug that has now happened twice.
  DIAGNOSIS    about a quarter pure diagnosis.
  CITE         every question cites its slide.
  (The io-prefix check was retired on 2026-08-27: the engine's ioLabel() no
   longer double-prefixes, and the 2,075 affected Semester 2 questions were
   repaired, so a stored prefix is no longer a rendering defect.)

Legacy quizzes predate all of this and are reported, never failed: --new limits
the run to files carrying a New tag, which is what a fresh build looks like.

--new reads the tag wherever index.html puts it. The convention written down on
2026-08-27 put the span INSIDE the link (<a ...>Form A<span class="quiz-tag
quiz-tag--new" ...></a>), and this matched only that. From 2026-08-29 index.html
put it AFTER </a> -- sometimes after a Drill span -- so --new went on checking
the same five CMS Exam 1 "Updated" forms and none of the 169 links tagged since
(audit of 2026-09-22). Both placements count now. The run prints how many
tagged links it found against how many New spans index.html holds, and FAILS if
any span could not be attached to a link, so a markup change cannot silently
shrink it again.

Exit code is non-zero if a checked file breaks a HARD rule, if a file carrying a
question bank cannot be parsed (it would otherwise drop out of the run without a
word), if FROZEN has drifted from semesters.js, or (--new) if a New span in
index.html could not be attached to a link.
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


def is_frozen(rel):
    """True for a repo-relative path inside a Semester 1 folder. The one place
    other checkers ask -- check_self_contained, check_leadin_present and
    check_truncated_keys import this rather than keep their own list (the
    self-contained checker's private copy had drifted: it skipped the Semester 2
    Medical Literature folder and scanned four Semester 1 ones)."""
    return rel.replace(os.sep, "/").startswith(FROZEN)


def frozen_drift(root=None):
    """FROZEN against semesters.js, the registry it is copied from.

    Returns [(folder, class, 'Semester 1 but not FROZEN' | 'FROZEN but not
    Semester 1')]. The same fact in two places always drifts; this is the guard
    between the two copies. Folders semesters.js does not classify (tools,
    audio, group-quizzes...) are ignored."""
    root = root or ROOT
    js = open(os.path.join(root, "semesters.js"), encoding="utf-8").read()
    m = re.search(r'id:\s*"summer-1-2026".*?classes:\s*\[([^\]]*)\]', js, re.S)
    if not m:
        return [("semesters.js", "?", "cannot find the summer-1-2026 class list")]
    s1 = set(re.findall(r'"([^"]+)"', m.group(1)))
    rules = [(re.compile(p, re.I if "i" in fl else 0), c)
             for p, fl, c in re.findall(r'\[\s*/(.+?)/([a-z]*)\s*,\s*"([^"]+)"\s*\]', js)]
    if not rules:
        return [("semesters.js", "?", "cannot find FOLDER_CLASS")]
    out = []
    for d in sorted(os.listdir(root)):
        if not os.path.isdir(os.path.join(root, d)) or d.startswith("."):
            continue
        cls = next((c for rx, c in rules if rx.search(d)), None)
        if cls is None:
            continue
        if cls in s1 and not is_frozen(d):
            out.append((d, cls, "Semester 1 but not FROZEN"))
        elif cls not in s1 and is_frozen(d):
            out.append((d, cls, "FROZEN but not Semester 1"))
    return out


REF_MEDIAN, REF_MAX = 19, 66          # measured from the 40 reference items
GAMEABLE_BAR = 0.35                   # house bar; reference itself is 0.13
DIAG_MIN = 0.20                       # "about a quarter", with slack
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18

VIGNETTE = re.compile(r"\b\d+-(year|month|week|day)-old\b|\bnewborn\b|\bin (his|her|their) (twenties|thirties|forties|fifties|sixties)\b", re.I)
DIAGNOSIS = re.compile(r"most likely diagnosis|what is the diagnosis", re.I)
CONDITION = re.compile(r"\b(syndrome|scabies|zoster|melanoma|carcinoma|dermatitis|nevus|naevus|granuloma|cellulitis|impetigo|warts|tinea|candidiasis|lipoma|abscess|furuncle|carbuncle|psoriasis|eczema|versicolor)\b", re.I)
INSTRUCTION = re.compile(r"\b(start|stop|give|apply|excise|observe|biopsy|screen|refer|remove|drain|immediately|antiviral|antibiotics|corticosteroid|cryotherapy|permethrin|ivermectin|antivenom|vincristine)\b", re.I)


class Unparseable(Exception):
    pass


def load(path):
    h = open(path, encoding="utf-8").read()
    m = re.search(r"const QUESTIONS\s*=\s*", h)
    if not m:
        return None, h
    # raw_decode reads exactly one JSON value and stops. The non-greedy
    # "(\[.*?\]);" this used to use stopped at the first "];" inside any
    # string, and the resulting JSON error was swallowed -- the file simply
    # dropped out of the run.
    try:
        qs = json.JSONDecoder().raw_decode(h, m.end())[0]
    except ValueError as e:
        raise Unparseable(str(e)[:80])
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

    # FOUR options, and this is a HARD rule now. Jaxon, 13 September 2026:
    # "All should be 4 answer choices not 5." The five-option shape came from the
    # 40 reference exemplars and only ever applied to CMS; every other class was
    # already four, so this warning used to fire on most of the site for being
    # correct. It is inverted and promoted: a five-option question is a defect.
    four = sum(1 for q in qs if len(q["opts"]) == 4)
    if four != n:
        counts = sorted({len(q["opts"]) for q in qs if len(q["opts"]) != 4})
        hard.append(f"{n-four}/{n} questions are not four-option (found {counts})")

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
    ap.add_argument("--days", type=int, default=None,
                    help="with --new: only tags added within this many days (home.js shows them for 3)")
    ap.add_argument("--include-frozen", action="store_true", help="also check folders marked FROZEN")
    args = ap.parse_args()

    drift = frozen_drift()
    for d, cls, why in drift:
        print(f"FROZEN DRIFT  {d} ({cls}): {why} -- fix FROZEN in this file")

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

    blind = False
    if args.new:
        index_html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
        tags = new_tags(index_html)
        spans = count_new_spans(index_html)
        inside = sum(1 for t in tags if t[2])
        print(f"New-tagged links in index.html: {len(tags)} of {spans} New span(s) "
              f"({inside} with the tag inside <a>, {len(tags) - inside} after </a>)")
        if len(tags) < spans:
            blind = True
            print(f"  TAG MISMATCH: {spans - len(tags)} New span(s) sit where the link pattern "
                  f"cannot attach them to a quiz -- fix new_tags() before trusting --new")
        if args.days is not None:
            import datetime
            today = datetime.date.today()
            tags = [t for t in tags if t[1] and
                    (today - datetime.date(*map(int, t[1].split("-")))).days <= args.days]
            print(f"  ...added within {args.days} day(s): {len(tags)}")
        tagged = {t[0] for t in tags}
        files = [f for f in files if os.path.relpath(f, ROOT) in tagged]
        missing = sorted(t for t in tagged if not os.path.exists(os.path.join(ROOT, t)))
        if missing:
            print(f"  {len(missing)} tagged link(s) point at no file: {missing[:5]}")

    checked = failed = 0
    unparseable = []
    for f in sorted(files):
        try:
            qs, html = load(f)
        except Unparseable as e:
            unparseable.append((os.path.relpath(f, ROOT), str(e)))
            continue
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
    for rel, err in unparseable:
        print(f"UNPARSEABLE  {rel}: {err} -- NOT CHECKED")
    print(f"checked {checked} quiz file(s); {failed} broke a hard rule; "
          f"{len(unparseable)} could not be parsed")
    return 1 if (failed or unparseable or drift or blind) else 0


def count_new_spans(index_html):
    """Every New-tag span in index.html, however it is placed. --new compares
    this with what new_tags() attached to links: a markup change that the link
    pattern cannot follow shows up as a shortfall and fails the run, rather
    than quietly shrinking the set of files checked."""
    return len(re.findall(r'<span\b[^>]*\bquiz-tag--new\b[^>]*>', index_html))


def new_tags(index_html):
    """[(repo-relative href, data-added or None, tag_inside_link)] for every
    quiz link carrying a New tag, whether the span sits inside the <a> or
    after </a> (optionally after other tag spans such as Drill)."""
    import urllib.parse
    out = []
    link = re.compile(r'<a\b[^>]*\bhref="([^"]+)"[^>]*>(.*?)</a>'
                      r'((?:\s*<span\b[^>]*>[^<]*</span>)*)', re.S)
    for m in link.finditer(index_html):
        inner, after = m.group(2), m.group(3)
        for part, is_inside in ((inner, True), (after, False)):
            t = re.search(r'<span\b[^>]*\bquiz-tag--new\b[^>]*>', part)
            if t:
                d = re.search(r'data-added="(\d{4}-\d{2}-\d{2})"', t.group(0))
                out.append((urllib.parse.unquote(m.group(1)), d.group(1) if d else None, is_inside))
                break
    return out


if __name__ == "__main__":
    sys.exit(main())
