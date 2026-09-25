# -*- coding: utf-8 -*-
"""Lecture 25 Heart Failure (Carter) -- scope for the guarded CMS Exam 4 partition.

The deck, the verbatim syllabus objectives, and everything the partition must
refuse for this lecture.

WHAT IS OUT, and why (audio: work/audio-carter/l25-heart-failure-emphasis.md):
  slide 57   the "2026 changes" slide and its two pictures (ESC 2026 poster,
             stage-focus infographic). "This will not be on your test. You'll
             be tested on the 2022 guidelines." (C2, said twice)
  41-50      one mechanism-of-action picture each -- no mechanism questions
             (program rule relayed on the L21 recording, C11)
  36         the RAAS cartoon is inaccurate (map §2); the slide has nothing else
  slide 10's right heart catheterization PRESSURE TABLE -- "This I will not
             test on" (C1). The slide's other lines stay in.
  slide 16's small-font "Other Cardiomyopathies" block -- "it's little, so
             obviously I'm not testing it on this one" (C4)
  the slide 22 formulas -- "I don't expect you to know that mathematical
             equation" (C6); the concepts and normal values stay in

CONTESTED, so never keyed (deck vs the tested 2022 guideline, or deck vs itself):
  which calcium channel blocker subclass is worse (s40) -- only "avoid" is keyed
  individual beta blockers (s40 lists atenolol/propranolol) -- class only
  digitalis "ICU only" (s51) -- inotropes are keyed as dobutamine/milrinone
  "EF >40%" as the definition of preserved EF (s25/39/56) -- 2022 bands only
  Stage D "decompensated" (s24) vs "advanced" (s52) -- "advanced" only
  "moderately" reduced (s23) -- "mildly" (2022 and the syllabus)
  BNP versus NT-proBNP in kidney disease (audio self-contradicts, X7)
  exactly 40% or 50% in any stem (s23 leaves both boundaries unassigned)
"""

DECK = "HEART FAILURE Carter 2026 PP.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)

# Syllabus, pages 14-15, verbatim (the syllabus's own "dysfunction.." kept).
IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing (including ordering and interpretation), management "
        "(acute and chronic, including applicable rehabilitative and palliative care), appropriate "
        "referrals, patient education, prevention, and prognosis for heart failure.")
IO_B = "Differentiate between systolic dysfunction and diastolic dysfunction.."
IO_C = ("Define each class of the New York Heart Association (NYHA) symptomatic and functional "
        "classification of heart failure.")
IO_D = ("Define the following diagnostic and therapeutic groups of HF patients, and the treatment "
        "implications/recommendations for each group: a. HF with reduced EF (HFrEF) b. HF with mildly "
        "reduced EF (HFmrEF) c. HF with preserved EF (HFpEF)")
IO_E = ("Differentiate each stage of the American College of Cardiology/American Heart Association "
        "(ACC/AHA), natural history classification of heart failure, and associated treatment "
        "recommendations of each stage.")
IO_F = ("Compare and contrast precipitating factors, clinical manifestations, diagnosis (including role "
        "of B-type natriuretic peptide, BNP), and treatment of acute decompensated heart failure.")
IO_G = ("Identify medical care strategies for heart failure in the lecture topic list for the following "
        "populations. 1. infant 2. child 3. adolescent 4. adult 5. elderly")
IOS = [IO_A, IO_B, IO_C, IO_D, IO_E, IO_F, IO_G]

EXCLUDED_SLIDES = {36, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 57}

SCOPE_BANNED = [
    r"\b2026\b", r"\b2022\b", r"moderately reduced", r"foundational medical therapy",
    r"additional medical therapy", r"vericiguat", r"ivabradine", r"semaglutide", r"tirzepatide",
    r"intravenous iron", r"digitoxin", r"finerenone", r"\bdigoxin\b|\bdigitalis\b",
    r"atenolol", r"propranolol", r"dihydropyridine", r"nifedipine", r"nicardipine",
    r"wedge pressure", r"takotsubo", r"peripartum", r"amyloid", r"sarcoid", r"arrhythmogenic",
    r"stage D[^.?;]{0,40}decompensated", r"decompensated[^.?;]{0,20}stage D",
    r"torsemide", r"eccentric hypertrophy", r"end-systolic volume",
]

# Named findings in vignette stems carry their description in parentheses.
NAMED = {
    "orthopnea": "lying flat",
    "paroxysmal nocturnal dyspnea": "waking",
    "jugular venous distension": "neck vein",
    "s3": "early diastol",
    "s4": "late diastol",
    "kerley b": "horizontal",
    "cephalization": "upper",
    "opening snap": "diastolic rumble",
}

# His only "it'll be on your test" (L25 audio, Notability): a Stage A, at-risk
# patient with diabetes gets a sodium-glucose cotransporter 2 inhibitor first,
# not a beta blocker. Every form must carry at least one such question.
REQUIRED = [("Stage A diabetic -> sodium-glucose cotransporter 2 inhibitor first",
             r"(?<!no )(?<!without )diabet", r"sodium-glucose", 1)]
