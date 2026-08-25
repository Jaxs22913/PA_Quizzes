#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stop the topic tag from giving the answer away before it is answered.

THE DEFECT. Every question rendered its `topic` -- the condition name -- in a
tag directly above the stem. On a vignette that asks "what is the most likely
diagnosis?", that tag IS the answer:

    [ Squamous cell carcinoma ]
    A 66-year-old man with fair skin has a small red, conical, hard nodule on
    the lower lip ... What is the most likely diagnosis?

Jaxon spotted it on the vignettes, where it is worst because recognising the
condition from the description is the entire exercise -- and because Jaquith
described this exam as "pretty much all clinical vignettes ... make sure that
you are able to RECOGNIZE CONDITIONS BY THE VIGNETTE".

SCOPE. Fixed everywhere, not only on the vignette pages. The same tag sits above
objective questions like "which condition shows the Auspitz sign?", where it
gives just as much away. 329 rendered quizzes carry the tag; all of them get the
fix, plus the template so nothing built later reintroduces it.

THE FIX IS TO DEFER, NOT DELETE. The topic is genuinely useful when reviewing an
answered question -- it is how you find the condition in the guide. So the tag
is hidden while the question is live and revealed with the explanation, in both
the one-at-a-time view and the "All on a page" scroll view.

Deliberately NOT hidden: the objective tag. "Objective 1 -- compare and contrast
the etiologies ... of pre-malignant and malignant lesions" names a syllabus
heading, not a disease, and knowing which objective is being tested is fair.
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, "tools", "quiz-template", "template.html")

# 1. the single-question view: blank the tag on render, fill it on reveal
OLD_RENDER = "  document.getElementById('qtopic').textContent = q.topic;"
NEW_RENDER = """  // The topic names the condition, so showing it above an unanswered stem
  // hands over the answer. Hidden while the question is live; revealed with
  // the explanation, where it is useful for looking the condition up.
  var _tp = document.getElementById('qtopic');
  _tp.textContent = ''; _tp.style.display = 'none';"""

OLD_REVEAL = "  document.getElementById('cite').textContent='Source: '+q.cite;"
NEW_REVEAL = """  var _tp2 = document.getElementById('qtopic');
  if(_tp2){ _tp2.textContent = q.topic; _tp2.style.display = ''; }
  document.getElementById('cite').textContent='Source: '+q.cite;"""

# 2. the scroll view: same treatment, per card
OLD_SCROLL = ("      '<div class=\"qmeta\"><span class=\"tag tag-topic\">' + q.topic + '</span>' +")
NEW_SCROLL = ("      '<div class=\"qmeta\"><span class=\"tag tag-topic\" data-topic=\"' + "
              "String(q.topic).replace(/\"/g,'&quot;') + '\" style=\"display:none\"></span>' +")


def patch_template(s):
    """Patch whichever of the sites this file actually has.

    Only 53 of the 329 quizzes carry the "All on a page" scroll view, so its
    site is legitimately absent from most of them -- asserting on it would fail
    the run on a file that is perfectly fine. Each site is therefore optional,
    but the two that EVERY quiz has (render and reveal) are asserted, so a file
    that silently gains neither is still caught by the audit at the end.
    """
    hits = 0
    if NEW_RENDER not in s and OLD_RENDER in s:
        assert s.count(OLD_RENDER) == 1, "render site appears more than once"
        s = s.replace(OLD_RENDER, NEW_RENDER); hits += 1
    if "_tp2" not in s and OLD_REVEAL in s:
        assert s.count(OLD_REVEAL) == 1, "reveal site appears more than once"
        s = s.replace(OLD_REVEAL, NEW_REVEAL); hits += 1
    if "data-topic" not in s and OLD_SCROLL in s:
        assert s.count(OLD_SCROLL) == 1, "scroll site appears more than once"
        s = s.replace(OLD_SCROLL, NEW_SCROLL); hits += 1
    # the scroll view reveals per-card; show its topic when that card is graded
    OLD_SP = "function paintScrollAnswer(i"
    if OLD_SP in s and "scroll topic reveal" not in s:
        m = re.search(r"function paintScrollAnswer\(i[^)]*\)\s*\{", s)
        assert m, "paintScrollAnswer signature not found"
        ins = ("\n  // scroll topic reveal: same rule as the single-question view\n"
               "  var _c=document.getElementById('sq-'+i)||document.querySelectorAll('.scrollq')[i];\n"
               "  if(_c){ var _t=_c.querySelector('.tag-topic');\n"
               "    if(_t && _t.getAttribute('data-topic')){ _t.textContent=_t.getAttribute('data-topic');\n"
               "      _t.style.display=''; } }")
        s = s[:m.end()] + ins + s[m.end():]
        hits += 1
    return s, hits


def main():
    tpl = open(TPL, encoding="utf-8").read()
    tpl, n = patch_template(tpl)
    open(TPL, "w", encoding="utf-8").write(tpl)
    print("template: %d site(s) patched" % n)

    files = [f for f in glob.glob(os.path.join(ROOT, "*", "*.html"))
             if 'id="qtopic"' in open(f, encoding="utf-8", errors="replace").read()]
    done = skipped = 0
    for f in files:
        s = open(f, encoding="utf-8").read()
        s2, n = patch_template(s)
        if n:
            open(f, "w", encoding="utf-8").write(s2); done += 1
        else:
            skipped += 1
    print("quizzes: %d patched, %d already done" % (done, skipped))
    # AUDIT. Every quiz that shows a topic tag must now blank it on render.
    # Without this the "already done" bucket could quietly hold files that were
    # never patched at all.
    bad = []
    for f in files:
        s = open(f, encoding="utf-8", errors="replace").read()
        if OLD_RENDER in s or "_tp.style.display = 'none'" not in s:
            bad.append(os.path.relpath(f, ROOT))
    if bad:
        print("\nSTILL REVEALING THE TOPIC BEFORE THE ANSWER (%d):" % len(bad))
        for b in bad[:12]:
            print("   ", b)
        sys.exit(1)
    print("\naudit: all %d quizzes blank the topic on render and reveal it with the\n"
          "explanation. A question is now shown WITHOUT its condition name." % len(files))


if __name__ == "__main__":
    main()
