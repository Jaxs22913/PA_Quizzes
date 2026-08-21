#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Make "All on a page" hold grading until Submit.

Jaxon, 2026-08-20: "for the Exams 'all in one page' feature you should wait to
grade and give correct answers till the person hits submit."

He is right, and the page was already contradicting itself: the scroll view
ships a Submit button and a question palette -- it IS the exam-style layout --
yet it graded each question the instant you clicked, locked the answer so you
could not change your mind, and revealed the explanation. Submitting afterwards
was ceremonial.

The engine already has a deferFeedback flag for Exam Mode. This makes the scroll
view honour it unconditionally, via holdFeedback(), without touching the paged
view or the hard-time-limit behaviour, which are separate concerns.

Sites changed (feedback and scoring only):
  applyExamModeUI / syncScrollChrome  hide the running score
  chooseAt                            no grading, no lock, answers stay editable
  paintScrollAnswer                   selection styling only, no correct/wrong
  showResults                         compute the score at submit
  results block                       show the full review, as Exam Mode does

Left alone deliberately: renderQ, choose and the keyboard handler are paged-view
paths, and hardCutoff stays tied to real Exam Mode rather than to a layout choice.

The engine is inlined into every quiz page, so this patches the template AND
every built quiz. Idempotent.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HELPER = '''function holdFeedback(){
  // "All on a page" is the exam-style layout -- it has a Submit button and a
  // question palette -- so it always holds grading until submit, whether or not
  // Exam Mode is on. Grading live while showing a Submit button was incoherent,
  // and locking the answer meant you could not revise before submitting.
  return deferFeedback || viewMode === 'scroll';
}
'''

EDITS = [
    # running score pill
    ("  document.getElementById('scoretxt').classList.toggle('hidden', deferFeedback);",
     "  document.getElementById('scoretxt').classList.toggle('hidden', holdFeedback());"),
    ("  if(st){ st.textContent = 'Score ' + score; st.classList.toggle('hidden', deferFeedback); }",
     "  if(st){ st.textContent = 'Score ' + score; st.classList.toggle('hidden', holdFeedback()); }"),
    # chooseAt
    ("  if(!deferFeedback && answers[i]!==null) return;",
     "  if(!holdFeedback() && answers[i]!==null) return;"),
    ("  if(!deferFeedback && first && oi===q.c) score++;",
     "  if(!holdFeedback() && first && oi===q.c) score++;"),
    ("  if(!deferFeedback && typeof recordAnswerStat === 'function'){",
     "  if(!holdFeedback() && typeof recordAnswerStat === 'function'){"),
    # paintScrollAnswer
    ("    if(deferFeedback){ if(a===oi) b.classList.add('selected-exam'); return; }",
     "    if(holdFeedback()){ if(a===oi) b.classList.add('selected-exam'); return; }"),
    ("  if(ex && !deferFeedback && a!==null){",
     "  if(ex && !holdFeedback() && a!==null){"),
    # results
    ("  if(deferFeedback) score = answers.reduce((acc,a,i)=> acc + ((a!==null && a===QUESTIONS[order[i]].c) ? 1 : 0), 0);",
     "  if(holdFeedback()) score = answers.reduce((acc,a,i)=> acc + ((a!==null && a===QUESTIONS[order[i]].c) ? 1 : 0), 0);"),
    ("  const missBlock = deferFeedback ? examReviewHTML() : missCount===0",
     "  const missBlock = holdFeedback() ? examReviewHTML() : missCount===0"),
]

ANCHOR = "function chooseAt(i, oi){"


def patch(path):
    s = open(path, encoding="utf-8").read()
    if "function chooseAt(" not in s:
        return None                      # not an exam-navigator quiz page
    if "function holdFeedback()" in s:
        return "already"
    missing = [a for a, _ in EDITS if s.count(a) != 1]
    if missing:
        return "SKIP (%d anchor(s) not found exactly once)" % len(missing)
    for a, b in EDITS:
        s = s.replace(a, b, 1)
    assert s.count(ANCHOR) == 1
    s = s.replace(ANCHOR, HELPER + "\n" + ANCHOR, 1)
    # showResults must recompute the score before it is read; verify ordering
    assert s.index("function holdFeedback()") < s.index("if(holdFeedback()) score =")
    open(path, "w", encoding="utf-8").write(s)
    return "patched"


def main():
    targets = [os.path.join(ROOT, "tools", "quiz-template", "template.html")]
    for dirpath, dirnames, files in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", "group-quizzes", "node_modules", "tools")]
        for f in files:
            if f.endswith(".html"):
                targets.append(os.path.join(dirpath, f))
    counts = {}
    for t in targets:
        r = patch(t)
        if r is None:
            continue
        counts[r] = counts.get(r, 0) + 1
        if r.startswith("SKIP"):
            print("  %s  %s" % (r, os.path.relpath(t, ROOT)))
    for k, v in sorted(counts.items()):
        print("%-10s %d file(s)" % (k, v))


if __name__ == "__main__":
    main()
