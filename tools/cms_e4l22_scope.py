# -*- coding: utf-8 -*-
"""Lecture 22 scope -- Atherosclerosis and Lipid Disorders (Carter).

Read by cms_e4_partition.py (guards) and imported by every Lecture 22 pool.
Not a question bank: check_pool_cites does not glob it.

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf pp. 13-14), with
the syllabus's own broken inline numbering kept. Only the leading list letter
("a." / "b." / "5.") is dropped, as the Hypertension precedent does.

  IO_A  arteriosclerosis vs atherosclerosis. The deck never teaches
        arteriosclerosis or atheroma formation (the word occurs only on its own
        objectives slide 2), and the audio spends 0 minutes on it. Questions
        carry IO_A only where they test what the deck DOES teach about
        atherosclerosis: its risk factors (Framingham, slides 20-21), risk
        estimation (22-29) and its complications as major ASCVD events (27).
  IO_B  the four disorders.
  IO_POP the populations objective.

EXCLUDED_SLIDES: 70 (its right-hand picture is the "2026 guidelines"
infographic and slide 70 is otherwise a repeat of 96), 71 (PREVENT calculator),
119 (a statin dose-equivalency chart that is doses and prices only).
Carter: "For rotations, I want you to be aware of the 2026. For testing,
we're going to go on the 2018s." The 2018 primary-prevention flowchart is
cited from its copy on slide 96. Slide 80 may be cited for its intensity
headings (high ~50%, moderate 30-<50%, low <30%), never for a dose.
"""

DECK = "22. Atherosclerosis and Lipid Disorders 2026 Carter.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)

IO_A = ("Compare and contrast risk factors, management, and complications of "
        "arteriosclerosis and atherosclerosis.")
IO_B = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical "
        "manifestations, differential diagnosis, diagnostic testing (including ordering "
        "and interpretation), management (acute and chronic, including applicable "
        "rehabilitative and palliative care), appropriate referrals, patient education, "
        "and prognosis of the following atherosclerosis and lipid disorders: "
        "1. Hypertriglyceridemia 2. Hypercholesterolemia 3. HDL cholesterol "
        "4. LDL and VLDL cholesterol")
IO_POP = ("Identify medical care strategies for atherosclerosis and lipid disorders in the "
          "lecture topic list for the following populations. 6. infant 7. child "
          "8. adolescent 9. adult 10. elderly")
IOS = [IO_A, IO_B, IO_POP]

EXCLUDED_SLIDES = {70, 71, 119}

# The 2026 / PREVENT framework is rotation-only; mg doses are banned by the
# partition's own dosing guard. Brand names of fish oil are the deck's only
# names for it, so they are blocked here too.
SCOPE_BANNED = [r"\bPREVENT\b", r"\b2026\b", r"\bLovaza\b", r"\bOmacor\b", r"\bAccutane\b",
                r"\bnystatin\b", r"\bAmish\b"]

# Named findings: a vignette stem using the name must also carry the
# description, taken from the deck (slides 32-36, 44, 56 and their pictures).
NAMED = {
    "eruptive xanthoma": "papules",        # s44 "small yellowish-white papules clusters"
    "lipemia retinalis": "opalescen",      # s44 "opalescence of the retinal blood vessels"
    "tendon xanthoma": "nodul",            # s33 pictures: firm nodules over tendons
    "tendinous xanthoma": "nodul",
    "tuberous xanthoma": "nodules",        # s34 picture: large firm nodules
    "xanthelasma": "yellow",               # s35 "Yellow plaques" on the eyelids
    "corneal arcus": "ring",               # s36 "white or grey arc or ring around the cornea"
    "palmar xanthoma": "palm",             # s56 (name only in the deck)
}
