# -*- coding: utf-8 -*-
"""Lecture 23 Valvular Heart Disease (Carter) -- scope for the guarded CMS Exam 4 partition.

The deck, the verbatim syllabus objectives, and everything the partition must
refuse for this lecture. Taught Fri 2026-09-25 (two recordings). The content
map is work/cms-carter/l24-valvular-heart-disease-map.md -- labeled "l24" but
this is Lecture 23 on the calendar. Errata and emphasis:
work/audio-carter/l23-errata.md and l23-valvular-emphasis.md.

HIS STATED CORRECTIONS WIN over the slide (the one exception to "the slide wins"):
  E1  slide 28   the aortic regurgitation murmur is a high-pitched blowing DIASTOLIC
                 murmur -- "Holosystolic" is struck ("It's not holosystolic because
                 it's diastolic. So cross that out."). Holosystolic may only ever be
                 a distractor for aortic regurgitation (it is mitral and tricuspid
                 regurgitation).
  E2  slide 29   echo determines the cause of AORTIC regurgitation (root dilation,
                 dissection) -- "cause of MR" is read as AR ("That should be an A").

UNKEYED (Jaxon may override later -- each is one SCOPE_BANNED line below):
  E3  slide 29   which leaflet flutters on echo. Carter struck "anterior mitral
                 leaflet" and said aortic; the textbook (and his own first answer)
                 says mitral. Key neither.
  I1  slide 64   pulmonic regurgitation "Almost always congenital, no treatment
                 required" -- the most common cause is IATROGENIC (slide 61, said
                 three times). "Pulmonary hypertension is our number one cause"
                 (spoken, overridden by him 40 s later) is never keyed either.
  I2  slide 74   valve type by age ("TAVR/TMVR ... <55", "Mechanical ... <70") --
                 contradicts what he taught in part 1. Only what both agree on is
                 keyed: mechanical = lifelong anticoagulation; bioprosthetic = none
                 beyond the immediate postoperative period, preferred if
                 anticoagulation is contraindicated.
  s38            mitral stenosis "Increased with Valsalva" -- contested and
                 internally inconsistent; NO mitral stenosis maneuver is keyed.
  s40            overlapping mild/moderate mitral stenosis bands -- key SEVERE only
                 (<1.0 cm2, mean gradient >10 mmHg, peak velocity >3.0 m/s).

DECK ERRORS HE DID NOT MENTION -- never keyed as printed:
  s44  "Mitral Stenosis:" label on the mitral regurgitation definition (the
       definition itself -- backflow into the left atrium -- is keyed as MR)
  s52  "Percutaneous Aortic Balloon Valvuloplasty" for children on the MR slide
       (stays keyed for aortic stenosis, slide 21)
  s53  "MS" on the MR referral slide -- the slide is excluded
  s65  tricuspid stenosis inflow "from the LA" -- key slide 66, right atrium to
       right ventricle
  s31  dobutamine listed as a vasodilator -- key IV diuretics + nitroprusside only
  I7   s69 "Mild to Moderate" tricuspid stenosis heading with nothing under it

SCOPE CAPS (his words; emphasis report section 2):
  C1  no audio -- murmurs are written descriptions
  C2  severity grading only for aortic stenosis and mitral stenosis; for aortic
      and mitral regurgitation only "severe = regurgitant fraction 50% or more";
      pulmonic and tricuspid stenosis grading tables (58, 68) are out
  C3  the suffusion sign is out ("I'm not going to test you on it")
  C4  low-flow / low-gradient pseudo-severe aortic stenosis is out
  C6  electrocardiogram findings are recognition only (no tracings)
  Carter program rules: no dosing, no mechanism-of-action questions, generic
  names only, no bare acronyms.

WEIGHTING: "When it comes to the test, you will just as likely have a tricuspid
valve question as you will an aortic valve question." Questions are spread
roughly EQUALLY across the nine lesions (each lesion is its own verbatim
syllabus objective, so the Set 1 objective-coverage term enforces the spread);
airtime only ranks facts within a lesion.
"""

DECK = "Valvular Heart Disease - Carter.pptx"
C = lambda *n: "%s, Slide%s %s" % (DECK, "s" if len(n) > 1 else "", ", ".join(str(x) for x in n))

# Syllabus page 14 of 26, verbatim (checked with PyMuPDF 2026-09-25). The
# syllabus numbers the disease list 2-11 as though each were an objective, and
# objective 13 names no populations (the list is missing in the syllabus).
IO_1 = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing (including ordering and interpretation), management "
        "(acute and chronic, including applicable rehabilitative and palliative care), appropriate "
        "referrals, patient education, prevention, and prognosis for valvular heart disease")
IO_ARF = "Acute rheumatic fever"
IO_AS = "Aortic stenosis"
IO_AR = "Aortic regurgitation"
IO_MS = "Mitral stenosis"
IO_MR = "Mitral regurgitation"
IO_MVP = "Mitral valve prolapse"
IO_TR = "Tricuspid regurgitation"
IO_TS = "Tricuspid stenosis"
IO_PS = "Pulmonic stenosis"
IO_PR = "Pulmonic regurgitation"
IO_12 = "Compare and contrast anticoagulation therapy for prosthetic heart valves."
IO_13 = ("Identify medical care strategies for valvular heart disease in the lecture topic list for the "
         "following populations.")
IOS = [IO_1, IO_ARF, IO_AS, IO_AR, IO_MS, IO_MR, IO_MVP, IO_TR, IO_TS, IO_PS, IO_PR, IO_12, IO_13]

# Topics (shared by every pool so the partition's topic terms line up).
T_MUR = "Murmur foundations"
T_ARF = "Rheumatic heart disease"
T_AS = "Aortic stenosis"
T_AR = "Aortic regurgitation"
T_MS = "Mitral stenosis"
T_MR = "Mitral regurgitation"
T_MVP = "Mitral valve prolapse"
T_PS = "Pulmonic stenosis"
T_PR = "Pulmonic regurgitation"
T_TS = "Tricuspid stenosis"
T_TR = "Tricuspid regurgitation"
T_PV = "Prosthetic valves and anticoagulation"

# 53: MR referral slide that says "MS" throughout. The pulmonic and tricuspid
# grading tables (58, 68) are handled by the "peak jet / peak gradient" ban
# below, so their electrocardiogram lines stay citable.
EXCLUDED_SLIDES = {53}

SCOPE_BANNED = [
    r"suffusion",                                             # C3
    r"low[- ]flow|low[- ]gradient|pseudo[- ]?severe",         # C4
    r"dobutamine",                                            # s31 deck error
    r"flutter",                                               # E3 leaflet (see the note below)
    r"no treatment (is )?required",                           # s64 / I1
    r"almost always congenital[^.?;]{0,60}regurg|regurg[^.?;]{0,60}almost always congenital",
    r"\b55\b|(mechanical|transcatheter|bioprosthetic|biological)[^.?;]{0,80}\b(younger|older|under|over) (than )?70\b",  # I2
    r"valsalva[^.?;]{0,90}mitral stenosis|mitral stenosis[^.?;]{0,90}valsalva",               # s38
    r"(mild|moderate)[^.?;]{0,40}mitral stenosis[^.?;]{0,60}(cm|mmHg|m/s)",                    # s40
    r"peak jet|peak gradient",                                # C2 pulmonic / tricuspid tables
    r"mL per beat|mL/beat|mL a beat|0\.(1|10|20|29|30|39|40) ?cm",   # C2 regurgitant area / volume columns
    r"aortic balloon valvuloplasty[^.?;]{0,80}mitral|mitral[^.?;]{0,80}aortic balloon valvuloplasty",  # s52
    r"from the left atrium and|left atrium and (the )?(superior|inferior)",                    # s65
    r"plastic|rubber|cancer of the valve|falling out of favor|age of death|austin flint",      # spoken asides / off-deck
    r"apixaban|rivaroxaban|dabigatran|edoxaban|enoxaparin",   # spoken only; slide 75 names VKA / heparin
]

# The tricuspid stenosis symptom on slide 67 is "fluttering discomfort in neck".
# It is written in questions as "a quivering discomfort in the neck" so the E3
# guard (r"flutter") can stay a blunt instrument.

# Named findings in vignette stems carry their description in parentheses.
NAMED = {
    "corrigan": "collapse",
    "water hammer": "collapse",
    "de musset": "head bob",
    "opening snap": "after the second heart sound",
    "carvallo": "inspiration",
    "graham steell": "diastolic",
    "ortner": "hoarse",
    "thrill": "palpable",
    "decubitus": "left side",
}

# Content he said WILL be tested, in every form of both sets (stem regex, key
# regex on the keyed option, minimum per form).
REQUIRED = [
    ("mechanical valve -> warfarin / vitamin K antagonist",
     r"mechanical", r"warfarin|vitamin K antagonist", 1),
]

# "Just as likely a tricuspid valve question as an aortic valve question": every
# form carries 2 to 4 questions on each of the nine lesions (the partition scores
# and asserts this). Murmur foundations, rheumatic heart disease and prosthetic
# valves are left free.
TOPIC_BAND = {t: (2, 4) for t in (T_AS, T_AR, T_MS, T_MR, T_MVP, T_PS, T_PR, T_TS, T_TR)}
