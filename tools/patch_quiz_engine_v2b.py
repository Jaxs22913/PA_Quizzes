#!/usr/bin/env python3
"""Flagging and jump-to-question become standard on every quiz.

Jaxon, 2026-08-19: "just make all quizzes include that going forward." So the
"Flag questions & jump between them" checkbox goes away and both are simply on.

That started as a narrower fix -- the one-page view already rendered flags and a
number palette, but the checkbox sat beside it implying they were optional, so a
student could pick that view, leave the box unticked, and reasonably expect no
flags. Making them standard everywhere removes the contradiction instead of
special-casing one view, and takes a decision off a start screen that had grown
to four options.

Also fixes two things the subsetting work exposed:
  - saved progress now records viewMode, so a one-page attempt resumes one-page
    rather than silently reopening paged with its flags nowhere to be seen
  - the resume banner counted against the full bank, so a 10-question attempt
    read "Question 3 of 30"
"""
import io, os, sys, glob

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
TARGETS = [os.path.join(ROOT, "tools/quiz-template/template.html")]
for d in ["Clinical Medicine and Surgery I Exam 1", "Microbiology Exam 1",
          "Pharmacology I Exam 1", "Physical Diagnosis 2 Exam 1",
          "Clinical Pathophysiology I Exam 1", "Principles of Diagnostic Medicine I Exam 1"]:
    TARGETS += sorted(glob.glob(os.path.join(ROOT, d, "*.html")))

EDITS = [
 # 1. retire the checkbox
 ("""    <label style="display:flex;align-items:center;gap:8px;font-size:14px;color:var(--muted);margin:0 0 8px;cursor:pointer">
      <input type="checkbox" id="flag-nav-toggle" style="width:16px;height:16px">
      Flag questions &amp; jump between them
    </label>
""", "", "remove flag-nav checkbox"),

 # 2. always on
 ("""  flagNav = !!(document.getElementById('flag-nav-toggle') && document.getElementById('flag-nav-toggle').checked);""",
  """  flagNav = true;   // standard on every quiz since 2026-08-19""",
  "force flagNav"),

 # 3. remember which view the attempt used
 ("""localStorage.setItem(PKEY, JSON.stringify({idx, score, answers, order, timerMs: currentElapsedMs(), deferFeedback, flagNav, hardCutoff, cutoffMs, flagged: Array.from(flagged), crossedOut: co}));""",
  """localStorage.setItem(PKEY, JSON.stringify({idx, score, answers, order, timerMs: currentElapsedMs(), deferFeedback, flagNav, hardCutoff, cutoffMs, viewMode, flagged: Array.from(flagged), crossedOut: co}));""",
  "save viewMode"),

 # 4. and come back into it
 ("""  document.getElementById('quiz').style.display='block';
  renderQ();
  window.scrollTo({top:0,behavior:'smooth'});
}""",
  """  document.getElementById('quiz').style.display='block';
  if(saved.viewMode) setView(saved.viewMode);
  if(viewMode==='scroll') renderScroll(); else renderQ();
  window.scrollTo({top:0,behavior:'smooth'});
}""",
  "resume into the saved view"),

 # 5. the resume banner counted against the whole bank, not the attempt
 ("""  document.getElementById('resume-text').textContent = 'Question '+(saved.idx+1)+' of '+QUESTIONS.length+' — Score: '+saved.score;""",
  """  document.getElementById('resume-text').textContent = 'Question '+(saved.idx+1)+' of '+((saved.order && saved.order.length) || QUESTIONS.length)+' — Score: '+saved.score;""",
  "resume banner counts the attempt"),
]

ok = fail = 0
for f in TARGETS:
    s = io.open(f, encoding="utf-8").read()
    if 'id="view-seg"' not in s:
        continue
    if 'id="flag-nav-toggle"' not in s:
        print("  skip (done): %s" % os.path.relpath(f, ROOT)); continue
    miss = []
    for old, new, why in EDITS:
        if s.count(old) != 1:
            miss.append("%s (%d)" % (why, s.count(old))); continue
        s = s.replace(old, new, 1)
    if miss:
        fail += 1; print("  FAIL %s -> %s" % (os.path.relpath(f, ROOT), ", ".join(miss))); continue
    io.open(f, "w", encoding="utf-8").write(s); ok += 1
print("\npatched %d, failed %d" % (ok, fail))
sys.exit(1 if fail else 0)
