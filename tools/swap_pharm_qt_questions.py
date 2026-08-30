# -*- coding: utf-8 -*-
"""Swap two low-yield antibacterial questions for the untested QT items.

QT prolongation is the standing rule Dr. Wood flagged first and restated, and it
spans macrolides, fluoroquinolones and posaconazole -- yet fluoroquinolone QT was
never tested and macrolide QT only appeared in one vignette. These two
replacements close that at constant quiz size, keeping the 30-question form and
the existing answer-key distribution (each new item reuses the key position of
the one it replaces, so 8/8/7/7 is preserved).
"""
import re, json, os
from collections import Counter

P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 "Pharmacology I Exam 1", "antibacterials-quiz.html")

NEW = {
 "Which macrolide regimen treats Helicobacter pylori?": {
   "topic": "Macrolides", "io": "4e — Macrolides/ketolides",
   "q": "What makes macrolide QT prolongation more dangerous?",
   "opts": [
     ["Class Ia and III antiarrhythmics, electrolyte abnormalities",
      "Correct. Each pushes repolarisation further, so the effects stack."],
     ["Iron, antacids, calcium or dairy taken at the same time",
      "Those chelate tetracyclines and fluoroquinolones, reducing absorption instead."],
     ["Large intravenous doses given in renal insufficiency",
      "That combination is what produces the transient hearing loss."],
     ["Use of the estolate salt in underlying liver disease",
      "The estolate salt is tied to cholestatic hepatitis instead."]],
   "c": 0,
   "cite": "Antibiotics, Antivirals, and Antifungals.pptx, Slide 57"},

 "What is the collateral consequence of fluoroquinolone overuse?": {
   "topic": "Fluoroquinolones", "io": "4k — Fluoroquinolones",
   "q": "Which cardiac risk do the fluoroquinolones carry?",
   "opts": [
     ["Bradycardia and atrioventricular block",
      "Not a listed effect; the cardiac entry is a repolarisation problem."],
     ["QT prolongation and torsades de pointes",
      "Correct. The same cardiac risk macrolides and posaconazole carry."],
     ["Cardiomyopathy after prolonged therapy",
      "The listed harms are tendon, nerve and central nervous system."],
     ["Hypertensive crisis with tyramine foods",
      "That belongs to the monoamine oxidase inhibitors."]],
   "c": 1,
   "cite": "Antibiotics, Antivirals, and Antifungals.pptx, Slide 79"},
}

src = open(P, encoding="utf8").read()
m = re.search(r'(const QUESTIONS\s*=\s*)(\[.*?\])(;\s*\n)', src, re.S)
qs = json.loads(m.group(2))
before_keys = Counter(q["c"] for q in qs)

swapped = 0
for i, q in enumerate(qs):
    if q["q"] in NEW:
        repl = NEW[q["q"]]
        assert repl["c"] == q["c"], "key position would move for %r" % q["q"]
        qs[i] = repl
        swapped += 1
assert swapped == 2, "expected 2 swaps, made %d" % swapped
assert len(qs) == 30, "quiz size changed to %d" % len(qs)
assert Counter(q["c"] for q in qs) == before_keys, "answer-key distribution changed"

out = src[:m.start(2)] + json.dumps(qs, ensure_ascii=False) + src[m.end(2):]
open(P, "w", encoding="utf8").write(out)
print("swapped %d question(s); size %d; keys %s"
      % (swapped, len(qs), sorted(before_keys.items())))
