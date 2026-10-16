# -*- coding: utf-8 -*-
"""Lecture 28 scope -- Cardiomyopathy (Carter).

Read by cms_e5_partition.py (guards) and imported by every Lecture 28 pool.
Not a question bank: check_pool_cites does not glob it.

Built SLIDES-ONLY (2026-09-25). The lecture is given on Zoom on 2026-10-01 and
no recording exists yet, so nothing here is weighted by audio.

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 16, checked
against the PDF with PyMuPDF on 2026-09-25), the syllabus's own numbering kept
inline: items 2-6 are the five cardiomyopathies of objective 1, item 7 is the
populations objective and 8-10 its list (adolescent, adult, elderly -- no infant
or child for this lecture). Slides 105-107 answer objective 7 directly.

EXCLUDED_SLIDES (never cited):
  4, 5      stroke volume / cardiac output / ejection fraction arithmetic. The
            numbers conflict with the heart failure lecture (cardiac output
            "4-6 liters" here vs 5-6 L/min there) and Carter said the formulas
            are not tested (L25 audio).
  7, 63     embedded YouTube videos with nothing else on the slide (not embedded
            or linked on the site -- the repo is public)
  14        the NYHA table, a repeat of the heart failure lecture (L25 owns it)
  80        video-only slide, titled "Myomectomy" (a different operation)
  108       references

CONTESTED or WRONG on the slides, so NEVER KEYED:
  DCM and hypertrophy: s18 "little or no cardiac wall hypertrophy" vs s37 ECG
      "may show left ventricular hypertrophy" -- neither is a discriminator.
  s76 heading "Arrhythmogenics for sudden cardiac death prevention" -- the
      wrong word; amiodarone is keyed from s78 ("proven to reduce ... sudden
      cardiac death") and called an antiarrhythmic.
  "Endocardial biopsy" (s41, DCM) vs "endomyocardial biopsy" (s55, s97) --
      the DCM biopsy is keyed only as "rarely useful / not routine".
  s98 calls verapamil and diltiazem "cardioselective" calcium channel blockers;
      its speaker notes call them non-dihydropyridines. Keyed by generic name.
  s103 picture says the octopus-trap shape is seen "on an X-ray" -- the deck's
      own tests are echo (apical and midsegment hypokinesis) and catheterization.
  s105 layout: "Medication management for symptomatic relief" and "ICD
      placement in select cases" sit un-dashed between the adolescent and adult
      lists, so neither is keyed to a population.
  Digoxin in DCM (s42 "second line"; notes: fewer admissions, no survival
      benefit) conflicts with the tested 2022 heart failure guideline as
      handled in L25 -- not keyed for DCM. Digoxin as a positive inotrope to
      AVOID in hypertrophic cardiomyopathy (s77) is keyed.
  DCM ejection fraction "<40%" (s38) vs the 2022 bands (<=40%) -- stems use an
      ejection fraction far from 40 (15-30%).
"""

DECK = "Cardiomyopathy - Carter.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)

IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing (including ordering and interpretation), management "
        "(acute and chronic, including applicable rehabilitative and palliative care), appropriate "
        "referrals, patient education, and prognosis of the following cardiomyopathies: 2. Restrictive "
        "cardiomyopathy 3. Hypertrophic cardiomyopathy 4. Dilated cardiomyopathy 5. Stress cardiomyopathy "
        "6. Myocarditis")
IO_POP = ("Identify medical care strategies for cardiomyopathies for the following populations. "
          "8. adolescent 9. adult 10. elderly")
IOS = [IO_A, IO_POP]

EXCLUDED_SLIDES = {4, 5, 7, 14, 63, 80, 108}

SCOPE_BANNED = [
    r"arrhythmogenic", r"myomectomy", r"endocardial biopsy",
    r"octopus[^?]{0,80}x-ray|x-ray[^?]{0,80}octopus",
    r"\b96\s?%|\bmL of (?:ethanol|alcohol)",
    r"cardioselective",
    r"\bNYHA\b|New York Heart Association",
    r"4\s?(?:-|to|–)\s?6 liters",
]

# Named findings in vignette stems carry their description in parentheses.
NAMED = {
    "kussmaul": "inspiration",                 # s92: JVP rises with inspiration
    "bisferiens": "double",                    # s67: double systolic peak
    "hepatojugular reflux": "liver",           # s33: firm pressure over the liver
    "kerley b": "horizontal",                  # s39: 1-2 cm horizontal lines
    "third heart sound": "early diastol",      # heart sounds glossed as in Exam 4
    "fourth heart sound": "late diastol",
    "systolic anterior motion": "leaflet",     # s62
    "orthopnea": "lying flat",
    "paroxysmal nocturnal dyspnea": "waking",
    "pulsus": "double",
    "low voltage": "small",
}
