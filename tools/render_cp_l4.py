#!/usr/bin/env python3
"""Render the two Clinical Pathophysiology I Lecture 4 quizzes.

DEFAULT MODE IS SPLICE (2026-09-24). The shipped pages were rendered on
2026-08-26 from the quiz template as it stood then. The template has since
gained class picks, "You vs the class" and picture-stem styles, so a full
re-render no longer reproduces the shipped page: it would silently switch those
engine features on for this quiz (class picks are "new exams only") and restore
the build-time intro. So by default this script only replaces the
`const QUESTIONS = [...]` literal inside each existing page with the questions
from cp_l4_sets.json (json.dumps indent=2, the pages' own format), and asserts
the literal round-trips before touching it. Everything else on the page is
left byte-for-byte alone. Proof on 2026-09-24: splice(sets) == shipped page.

    python3 render_cp_l4.py          # splice sets into the existing pages
    python3 render_cp_l4.py --full   # full template re-render (engine changes!)

Chain: cp_l4_pool_[a-d].py -> cp_l4_partition.py -> cp_l4_sets.json -> this.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 1")
S = json.load(open(os.path.join(HERE, "cp_l4_sets.json"), encoding="utf-8"))
PAL = dict(navy="#3b2a5e", indigo="#6a4fa3", gold="#c08a2e", ice="#f2eefb")
CHIPS = ["Anatomy &amp; vision", "Refractive errors", "The &ldquo;-itises&rdquo;",
         "Glaucoma &amp; cataract", "Retina &amp; macula", "Visual fields"]
INTRO = ("Thirty questions on ophthalmic pathophysiology, drawn from the ten numbered "
         "instructional objectives. Covers the neurological anatomy of the eye and the three "
         "tunics, the physiology of vision, the molecular mechanisms behind the inflammatory "
         "&ldquo;-itises&rdquo; and the eyelid, corneal and lacrimal conditions, the refractive "
         "errors and the globe geometry that causes them, glaucoma and cataract, retinal "
         "detachment and macular degeneration, the diabetic retinopathy cascade, and visual field "
         "deficits by lesion site. "
         "<b>Pathophysiology only</b> &mdash; every question asks what is happening in the tissue "
         "and why, never what you would do about it. That line matters more than usual here: "
         "<b>CMS I Exam 2 covers almost this exact condition list from the management side</b>, "
         "so this is deliberately the other half. "
         "<b>The 26 August recording is folded in, and it changes the emphasis.</b> In the last "
         "two minutes the lecturer said <i>&ldquo;this is for the test&rdquo;</i> and named "
         "seven topics: <b>cataracts, macular degeneration, the visual pathway, refraction "
         "errors, retinal detachment causes, glaucoma</b> (specifically the pathophysiological "
         "explanation for the vision loss) and, added after he had already finished, "
         "<b>presbyopia</b>. Both of these quizzes cover all seven. "
         "He also cut scope out loud: of the visual-field lesion sites, <b>know the optic nerve, "
         "the chiasm and the optic tract</b> &mdash; the optic radiation and occipital cortex he "
         "deferred to neurology. And he de-emphasised which lens corrects which error, so no "
         "question asks it. "
         "<b>Two figures in this deck disagree with each other</b> on the normal intraocular "
         "pressure &mdash; slide 24 says 10&ndash;21 mmHg and slide 25 says about 6&ndash;19 "
         "&mdash; so nothing is graded on that value. Every question cites its slide.")
PFX = "const QUESTIONS = "


def splice(path, questions):
    txt = open(path, encoding="utf-8").read()
    assert txt.count(PFX) == 1, "expected exactly one QUESTIONS literal in %s" % path
    start = txt.index(PFX) + len(PFX)
    old, end = json.JSONDecoder().raw_decode(txt, start)
    assert txt[end] == ";", "QUESTIONS literal not terminated by ';' in %s" % path
    assert json.dumps(old, ensure_ascii=False, indent=2) == txt[start:end], (
        "QUESTIONS literal in %s is not in json.dumps(indent=2) form; refusing to splice" % path)
    new = txt[:start] + json.dumps(questions, ensure_ascii=False, indent=2) + txt[end:]
    if new != txt:
        open(path, "w", encoding="utf-8").write(new)
    return new != txt


if "--full" not in sys.argv:
    for n, key in ((1, "set1"), (2, "set2")):
        fn = "ophthalmic-pathophys-quiz.html" if n == 1 else "ophthalmic-pathophys-quiz-version-2.html"
        changed = splice(os.path.join(OUT, fn), S[key])
        print("spliced" if changed else "unchanged", fn, "(%d questions)" % len(S[key]))
    sys.exit(0)

for n, key in ((1, "set1"), (2, "set2")):
    fn = "ophthalmic-pathophys-quiz.html" if n == 1 else "ophthalmic-pathophys-quiz-version-2.html"
    html = render(title=f"Ophthalmic Pathophysiology Quiz {n} &mdash; Clin Path I Exam 1",
                  h1=f"Ophthalmic Pathophysiology &mdash; Quiz {n}",
                  sub="Clinical Pathophysiology I &middot; Exam 1 &middot; Lecture 4",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
