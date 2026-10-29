# -*- coding: utf-8 -*-
"""Lecture 36 scope -- Chronic Obstructive Pulmonary Disease (Reynolds), CMS I Exam 6 (Respiratory Block
Exam I, 2026-11-06, Lectures 33-38).

Read by cms_e6l35_partition.py (guards) and imported by every Lecture 36 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Lauren Reynolds, MSPA, PA-C -- title slide, and the 2026-10-28 recording (Notability, four clips,
121 min, 15:11 to 17:23). calendar-data.js lists the lecture as #36 on 2026-10-28.

NUMBERING: the deck file is "37. svCOPD 2026.pptx" and the Oxygen Delivery deck is "35.", while the calendar
numbers those lectures 36 and 33; the deck numbers run 2 ahead of the calendar for this block. The syllabus
topic outline is unnumbered, so the calendar number (36) is used everywhere on the site.

Built from the DECK; the recording only sets emphasis and scope (slides-only grounding).

AUDIO SCOPE REMARKS (Notability transcript; ours is the second opinion):
  No topic was declared untestable.
  Grouping: the 2020 A-to-D grouping stays on the slides "because it may be what you're tested on in the
      boards"; the 2023/2026 A, B, E grouping is "probably what you'll be practicing in real life". Both are
      keyed, each named in the stem ("the 2020 four-group scheme", "the current three-group scheme").
  High exacerbation risk: the slides (s36, s37, s40) define it as 2 or more moderate exacerbations or 1
      leading to hospitalization in the past year. In the recording the lecturer says that under 2026 "any
      exacerbation makes the person high risk" ("You got one, moderate to severe, you're high risk"). Slides
      win, and no item puts a patient in the disputed zone: every stem has either 0 exacerbations, or 2 or
      more, or a hospitalization. Flagged to Jaxon.

SPEAKER NOTES ARE NOT SLIDE CONTENT (Jaxon, 2026-10-15).

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf, "Chronic Obstructive Pulmonary Disease (COPD) /
Chronic Obstructive Lung Disease (COLD)", read with pypdf on 2026-10-29), the leading letters dropped and the
sub-list numbering kept, as Lecture 31 does. The syllabus repeats "chronic obstructive lung disease (COLD)"
twice in the last objective; quoted as written.

EXCLUDED_SLIDES (never cited):
  1, 2       title, objectives
  3, 65      the lecture's worked case (never build on a lecture's worked example)
  32         unlabeled picture
  50, 51     medication review pictures (generic, trade and device names: brands)

CONTESTED or UNSAFE on the slides, so NEVER KEYED that way (the guide notes each):
  s36 "Typically GOLD 1 or GOLD 2 ..." per group -- the grade a group usually has is never keyed; groups are
      keyed only from symptoms and exacerbation history.
  s42 "ICS ... usually not used in severe disease" -- not keyed; the keyed facts are that an inhaled
      corticosteroid is never used alone in this disease and raises pneumonia risk.
  s48 pneumococcal vaccine product names (PPSV23 vs PCV) -- product names are never keyed; keyed: yearly
      influenza vaccine, pneumococcal vaccine at 65 or earlier with severe disease or cardiac comorbidity.
  s63 vs s64 oxygen threshold "SpO2 <88%" vs "SpO2 <=88%" -- stems use saturations clearly below 88%; the
      saturation target (societies disagree, s63) is never keyed.
  s52 BODE walk-distance row "250-249" (a typo for 250-349) -- stems use walk distances of 350 or more,
      150-249, or 149 or less, never 250-349.
  s26 "<12% improvement ... irreversible" -- keyed only together with the post-bronchodilator ratio below 0.70.
"""

DECK = "37. svCOPD 2026.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
CS = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
        "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
        "including applicable rehabilitative and palliative care), appropriate referrals, patient education, and "
        "prognosis of the following pulmonary conditions: 1. Chronic obstructive pulmonary disease / chronic "
        "obstructive lung disease a. Chronic bronchitis subtype b. Emphysema subtype")
IO_OBS = "Describe airflow obstruction in COLD and methods for assessing the severity of the obstruction"
IO_PFT = ("Describe how PFTs are utilized to aid in the diagnosis of pulmonary diseases and monitoring of "
          "patients with those diseases")
IO_POP = ("Identify medical care strategies for chronic obstructive lung disease (COLD)/ chronic obstructive "
          "lung disease (COLD) for the following populations. 1. adult 2. elderly")
IOS = [IO_A, IO_OBS, IO_PFT, IO_POP]

EXCLUDED_SLIDES = {1, 2, 3, 32, 50, 51, 65}

SCOPE_BANNED = [
    r"Pneumovax|PPSV|PCV|Prevnar",
    r"6% of Americans|third leading cause",
    r"250[- ]?(?:to[- ])?349",
    r"\b(?:88|90|92)% (?:to|-) ?(?:90|92)%",
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "pink puffer": "thin",                     # s14: thin, pursed-lip breathing, barrel chest
    "blue bloater": "cyanosis",                # s14: cough, sputum, rhonchi, possible cyanosis and edema
    "cor pulmonale": "heart",                  # s17, s14: right heart strain or failure
    "tripod": "lean",                          # s20: may lean forward (tripoding)
}
