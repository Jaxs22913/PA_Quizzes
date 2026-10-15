#!/usr/bin/env python3
"""Render the CMS I Exam 5 (Cardiology Block Exam II) quizzes.

Palette continues the exam sequence by the same hue rotation the earlier exams
used -- Exam 1 teal (182), Exam 2 indigo (226), Exam 3 violet (259), Exam 4
plum (292), so Exam 5 is rose (325): the Exam 4 plum colors rotated +33 degrees
in hue. Four-option sets, per the exam standard.

    python3 render_cms_e5.py l27io | l27vig | l28io | l28vig | l26io | l26vig
    python3 render_cms_e5.py l29io | l29vig | l30io | l30vig | l31io | l31vig | l32io | l32vig
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 5")
PAL = dict(navy="#7a2d5a", indigo="#b4538c", gold="#c08a2e", ice="#faeef4")

SPEC = {
 "l27io": dict(sets="cms_e5l27_sets.json",
   files=["arterial-occlusive-aneurysm-quiz.html", "arterial-occlusive-aneurysm-quiz-version-2.html"],
   title="Arterial Occlusive Disease and Aortic Aneurysm Quiz %d — CMS I Exam 5",
   h1="Arterial Occlusive Disease &amp; Aortic Aneurysm &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 27",
   chips=["Peripheral artery disease", "Acute limb ischemia", "Carotid disease",
          "Aortic aneurysms", "Aortic dissection"]),
 "l27vig": dict(sets="cms_e5l27_vig_sets.json",
   files=["arterial-occlusive-aneurysm-vignettes.html", "arterial-occlusive-aneurysm-vignettes-version-2.html"],
   title="Arterial Occlusive Disease and Aortic Aneurysm Vignettes %d — CMS I Exam 5",
   h1="Arterial Occlusive Disease &amp; Aortic Aneurysm &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 27",
   chips=["Claudication", "Ankle-brachial index", "Acute limb ischemia", "Aneurysm size and repair",
          "Dissection"]),
 "l26io": dict(sets="cms_e5l26_sets.json",
   files=["venous-disorders-quiz.html", "venous-disorders-quiz-version-2.html"],
   title="Venous Disorders Quiz %d — CMS I Exam 5",
   h1="Venous Disorders &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 26",
   chips=["Deep vein thrombosis", "Wells criteria", "Chronic venous insufficiency", "Varicose veins",
          "Thrombophlebitis", "Arteriovenous fistula"]),
 "l26vig": dict(sets="cms_e5l26_vig_sets.json",
   files=["venous-disorders-vignettes.html", "venous-disorders-vignettes-version-2.html"],
   title="Venous Disorders Vignettes %d — CMS I Exam 5",
   h1="Venous Disorders &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 26",
   chips=["Leg swelling", "Virchow triad", "Wells score", "Venous ulcer", "Superficial phlebitis",
          "Dialysis fistula"]),
 "l28io": dict(sets="cms_e5l28_sets.json",
   files=["cardiomyopathy-quiz.html", "cardiomyopathy-quiz-version-2.html"],
   title="Cardiomyopathy Quiz %d — CMS I Exam 5",
   h1="Cardiomyopathy &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 28",
   chips=["Dilated", "Myocarditis", "Hypertrophic", "Restrictive", "Stress (Takotsubo)"]),
 "l29io": dict(sets="cms_e5l29_sets.json",
   files=["supraventricular-arrhythmias-quiz.html", "supraventricular-arrhythmias-quiz-version-2.html"],
   title="Arrhythmias I: Supraventricular Quiz %d — CMS I Exam 5",
   h1="Arrhythmias I: Supraventricular &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 29",
   chips=["Sinus rhythms", "Sick sinus syndrome", "Supraventricular tachycardia", "Atrial flutter",
          "Atrial fibrillation", "Premature beats"]),
 "l29vig": dict(sets="cms_e5l29_vig_sets.json",
   files=["supraventricular-arrhythmias-vignettes.html", "supraventricular-arrhythmias-vignettes-version-2.html"],
   title="Arrhythmias I: Supraventricular Vignettes %d — CMS I Exam 5",
   h1="Arrhythmias I: Supraventricular &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 29",
   chips=["Bradycardia", "Narrow-complex tachycardia", "Vagal maneuvers and adenosine", "Rate control",
          "Anticoagulation", "Accessory pathway"]),
 "l30io": dict(sets="cms_e5l30_sets.json",
   files=["blocks-ventricular-arrhythmias-quiz.html", "blocks-ventricular-arrhythmias-quiz-version-2.html"],
   title="Arrhythmias II: Blocks and Ventriculars Quiz %d — CMS I Exam 5",
   h1="Arrhythmias II: Blocks &amp; Ventriculars &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 30",
   chips=["Atrioventricular blocks", "Bundle branch blocks", "Premature ventricular beats",
          "Ventricular tachycardia", "Torsades de pointes", "Ventricular fibrillation"]),
 "l30vig": dict(sets="cms_e5l30_vig_sets.json",
   files=["blocks-ventricular-arrhythmias-vignettes.html", "blocks-ventricular-arrhythmias-vignettes-version-2.html"],
   title="Arrhythmias II: Blocks and Ventriculars Vignettes %d — CMS I Exam 5",
   h1="Arrhythmias II: Blocks &amp; Ventriculars &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 30",
   chips=["Heart block", "Pacing", "Wide-complex tachycardia", "QT prolongation", "Cardiac arrest"]),
 "l31io": dict(sets="cms_e5l31_sets.json",
   files=["pericardial-disease-quiz.html", "pericardial-disease-quiz-version-2.html"],
   title="Pericardial Disease Quiz %d — CMS I Exam 5",
   h1="Pericardial Disease &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 31",
   chips=["Acute pericarditis", "Recurrent pericarditis", "Constrictive pericarditis",
          "Pericardial effusion", "Cardiac tamponade"]),
 "l31vig": dict(sets="cms_e5l31_vig_sets.json",
   files=["pericardial-disease-vignettes.html", "pericardial-disease-vignettes-version-2.html"],
   title="Pericardial Disease Vignettes %d — CMS I Exam 5",
   h1="Pericardial Disease &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 31",
   chips=["Pleuritic chest pain", "Friction rub", "Constriction", "Tamponade", "Pericardiocentesis"]),
 "l32io": dict(sets="cms_e5l32_sets.json",
   files=["infective-endocarditis-quiz.html", "infective-endocarditis-quiz-version-2.html"],
   title="Infective Endocarditis Quiz %d — CMS I Exam 5",
   h1="Infective Endocarditis &mdash; Quiz %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 32",
   chips=["Acute vs subacute", "Organisms", "Modified Duke criteria", "Antibiotics", "Prophylaxis",
          "Pediatric endocarditis"]),
 "l32vig": dict(sets="cms_e5l32_vig_sets.json",
   files=["infective-endocarditis-vignettes.html", "infective-endocarditis-vignettes-version-2.html"],
   title="Infective Endocarditis Vignettes %d — CMS I Exam 5",
   h1="Infective Endocarditis &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 32",
   chips=["Fever and murmur", "Peripheral signs", "Blood cultures and echo", "Empiric therapy",
          "Prophylaxis", "Surgery"]),
 "l28vig": dict(sets="cms_e5l28_vig_sets.json",
   files=["cardiomyopathy-vignettes.html", "cardiomyopathy-vignettes-version-2.html"],
   title="Cardiomyopathy Vignettes %d — CMS I Exam 5",
   h1="Cardiomyopathy &mdash; Vignettes %d",
   sub="Clinical Medicine and Surgery I &middot; Exam 5 &middot; Lecture 28",
   chips=["Dilated", "Myocarditis", "Outflow obstruction", "Restrictive vs constrictive",
          "Stress (Takotsubo)"]),
}[sys.argv[1] if len(sys.argv) > 1 else "l27io"]

S = json.load(open(os.path.join(HERE, SPEC["sets"]), encoding="utf-8"))
for n, (key, fname) in enumerate(zip(("set1", "set2"), SPEC["files"]), start=1):
    # the sets keep each distractor's misconception tag as a third option element
    # (WRITER.md; tools/blind_review.py reads it there); the pages carry text + explanation only
    qs = [dict({k: v for k, v in q.items() if k not in ("mis", "ordered", "asc")},
               opts=[o[:2] for o in q["opts"]]) for q in S[key]]
    html = R.render(title=SPEC["title"] % n, h1=SPEC["h1"] % n, sub=SPEC["sub"],
                    pill="%d questions" % len(qs), chips=SPEC["chips"], intro="",
                    questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %-52s %d questions" % (fname, len(qs)))
