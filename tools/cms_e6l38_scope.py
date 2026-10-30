# -*- coding: utf-8 -*-
"""Lecture 38 scope -- Mycobacterial Infections, Including Tuberculosis (Bobilin), CMS I Exam 6 (Respiratory
Block Exam I, 2026-11-06, Lectures 33-38).

Read by cms_e6_partition.py (guards) and imported by every Lecture 38 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Robert Bobilin, MS, MPAS, PA-C, Emeritus, guest lecturer -- title slide, and the 2026-10-29 Zoom
recording (the same file as Lecture 37; Lecture 38 runs 3:07:18 to 4:01:51, with about 4 minutes lost to a
video that would not play). calendar-data.js lists "CMS I - LECTURE #38 - Mycobacterial Infections, Including
Tuberculosis - Professor Bobilin GUEST LECTURER", 4-5 PM (1 hour). No conflict. Deck file "38. Mycobacterial
Infections including Tuberculosis - Bobilin - 10-29-2025 SV.pptx" (the "2025" in the file name is the file's
own; the title slide says October 29, 2026), 45 slides.

Built from the DECK; the recording only sets emphasis and scope (slides-only grounding).

AUDIO SCOPE REMARKS (Zoom transcript, speaker-labelled; ours is the second opinion):
  No topic was declared untestable. He framed the hour around three decisions: is TB disease plausible, may
      the patient be infectious, and which diagnostic and treatment pathway fits [3:09:00].
  Guidance promised: "I'm going to put out some guidance this weekend ... it'll have some guidance for the
      respiratory infections, it'll have some guidance for the mycobacterium and TB" [4:00:15]. Not on disk
      on 2026-10-30.
  He called fever and night sweats "pathognomonic" [3:34:55]; the slide (s16) lists them as manifestations
      only. The slide wins: never keyed as pathognomonic.
  The primary-and-secondary TB video (s11) would not play; he called it "not a pivotal thing" [3:25:47].

EMPHASIS (minutes, Zoom timestamps, the video glitch removed): biology and species ~3, epidemiology ~2,
  extrapulmonary ~2, stages and the s12 diagram ~9, transmission and exposure ~2, progression risk ~2,
  manifestations and exam ~3, differential ~2, tuberculin skin test, BCG and thresholds ~5, negative tests and
  IGRA ~5, sputum and imaging ~6, isolation and reporting ~2, treatment regimens and monitoring ~3, latent
  infection regimens ~1, nontuberculous mycobacteria ~2.

SPEAKER NOTES ARE NOT SLIDE CONTENT (Jaxon, 2026-10-15).

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 18-19, "Mycobacterial Infections, Including
Tuberculosis"), the syllabus's own numbering kept ("3. adult 4. elderly" is how the syllabus numbers the
population sub-list). The deck's own objectives slide (s2) is NOT the syllabus and is not quoted as an IO.

EXCLUDED_SLIDES (never cited):
  1, 2       title, the deck's own objectives
  3          link to a video on the history of the name
  6, 7       epidemiology statistics (context only; no number is keyed)
  11         video title picture (the video did not play)
  30, 31, 32 example films ("imaging alone cannot confirm TB"; the s32 text is a case description)
  41         lecture review questions (the lecturer's own worked answers)
  42-45      references

CONTESTED or UNSAFE on the slides, so NEVER KEYED that way:
  s36 "Eligible patients may receive 6-month BPaLM or BPaL regimens" -- the drug letters are never expanded
      on the slide; only "rifampin resistance needs rapid susceptibility testing and expert management" is
      keyed.
  s35 rifapentine-moxifloxacin eligibility beyond "age 12 or older with susceptible pulmonary TB" is "expert
      review" -- no other eligibility detail keyed.
"""

DECK = "38. Mycobacterial Infections including Tuberculosis - Bobilin - 10-29-2025 SV.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
CS = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
        "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
        "including applicable rehabilitative and palliative care), appropriate referrals, patient education, and "
        "prognosis of the following mycobacterial infections: a. Tuberculosis b. Atypical mycobacterial disease")
IO_POP = ("Identify medical care strategies for mycobacterial infections for the following populations. "
          "3. adult 4. elderly")
IOS = [IO_A, IO_POP]

EXCLUDED_SLIDES = {1, 2, 3, 6, 7, 11, 30, 31, 32, 41, 42, 43, 44, 45}

SCOPE_BANNED = [
    r"10\.7 million|1\.23 million|150,000|10,260|3\.0 per 100,000|77%|one quarter of the world",
    r"BPaLM|BPaL\b|bedaquiline|pretomanid",
    r"QuantiFERON|T-SPOT",
    r"pathognomonic",
    r"Moulin Rouge|Satine|Holliday|Kilmer",
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "miliary": "tiny nodules",             # s27: miliary disease can produce diffuse tiny nodules
}
# "meningismus" (s8) has no description anywhere on the slides, so no vignette stem names it.

# Every form carries at least one tuberculin skin test cut-off item (s22: the 5, 10 and 15 mm thresholds).
REQUIRED = [
    ("tuberculin cut-off", r"induration", r".", 1),
]
