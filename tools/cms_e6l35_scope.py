# -*- coding: utf-8 -*-
"""Lecture 35 scope -- Asthma (Finck), CMS I Exam 6 (Respiratory Block Exam I, 2026-11-06, Lectures 33-38).

Read by cms_e6l35_partition.py (guards) and imported by every Lecture 35 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Megan B. Finck, MMS, PA-C -- title slide, and the 2026-10-28 recording (Notability, two clips,
95.8 min, 13:09 and 14:08). calendar-data.js lists "CMS I - LECTURE #35 - Asthma - Professor Finck". No
conflict. The deck file carries no lecture number.

Built from the DECK; the recording only sets emphasis and scope (slides-only grounding).

AUDIO SCOPE REMARKS (Notability transcript; ours is the second opinion):
  Ages: "The only ones you're responsible for for CMS1 are the ones for the adults. Don't worry about anybody
      that's younger than 12." -- every patient is 12 or older; the age-banded columns for children are never used.
  Rescue inhaler: the NAEPP (2020 update) slides say albuterol; GINA uses an inhaled corticosteroid plus a
      short-acting bronchodilator. "I'm not gonna ask you the question that has conflicting information" --
      the rescue inhaler is keyed only as the short-acting beta-2 agonist, and no item pits the two schemes.
  Epidemiology: "I'm not going to test you on epidemiologic statistics" -- no prevalence, visit or death
      number is keyed (slides 11, 15-22 are context only).
  Severity: "if I were to give you a description of a patient ... decide this patient has moderate persistent
      asthma, or this patient has intermittent asthma"; "focus in on the mild and moderate". The s62 table (12
      years and older) is keyed from patient descriptions. "I'm not going to ask you ... that the number I give
      you is normal for an 80-year-old, but not for a 20-year-old" -- the age-normal ratio column is never keyed.
  Drugs: "it's more important to understand the class of medication ... rather than the specific trade
      names" -- class-level items, generic names only, no brands, no doses.
  Monoclonal antibodies: "we're not going to spend much time talking about this" -- one fact only (s84:
      specialist use, reduce the need for corticosteroids).
  Emergency care: "The emergency management of asthma is not testable for CMS one." -- slides 97-105
      (Quick Reference cover, the three "Asthma in the Emergency Setting" slides and the five flowchart
      copies) are EXCLUDED.
  Patient education: "really important is the patient education" -- weighted up (action plan, inhaler
      technique, peak flow zones, rinse after inhaled corticosteroid, vaccination).

EMPHASIS (minutes, Notability segment timing): guideline framing ~9, definition/pathophysiology ~8, burden
  and epidemiology ~9 (context only), etiology and hygiene hypothesis ~10, intrinsic/extrinsic and other types
  ~6, triggers ~5, diagnosis steps/history/exam ~9, spirometry and other tests ~10, severity classification
  ~6 (stressed), differential and aspergillosis ~2, medications ~16, action plan and chronic care ~3,
  refractory/aspirin/exercise-induced ~3, emergency (not testable) ~5.

THE GUIDELINE PDFs: the lecturer called the assigned Asthma Care Quick Reference and the 2020 At-A-Glance
  guide "testable material" (adult columns). They are NOT slides, so nothing is keyed from them; s87 only
  points to their pages for step therapy. Step-numbered drug choices are therefore never keyed.

SPEAKER NOTES ARE NOT SLIDE CONTENT (Jaxon, 2026-10-15).

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 17-18, "Asthma", read with pypdf on
2026-10-29), the leading letters dropped and the sub-list numbering kept, as Lecture 31 does.

EXCLUDED_SLIDES (never cited):
  1, 2, 3        title, reading assignments, GINA homework
  6              blank (no text, no picture)
  16, 17, 21, 22 prevalence/death charts (epidemiology statistics: not tested)
  69             respiratory treatments poster (brands and doses)
  97-105         emergency management (not testable for CMS I) and the Quick Reference cover
  106, 107, 108  resources and references

CONTESTED or UNSAFE on the slides, so NEVER KEYED that way (the guide notes each):
  s68/s87 rescue inhaler: albuterol (NAEPP) vs inhaled corticosteroid plus short-acting agent (GINA) -- see above.
  s75 "Systemic side effects: Minimal with high-dose therapy" -- high-dose inhaled corticosteroids carry more
      systemic effect, not less; the line is never keyed. Only the local side effects and the rinse/spacer
      advice are.
  s78-s82 file mast cell stabilizers, the anticholinergic and theophylline under "Long-acting
      Bronchodilators"; cromolyn is not a bronchodilator. Items key what each slide says about the drug,
      never the heading.
  s86 pneumococcal "Pneumovax23" for adults 19-64: vaccine product names and age bands are never keyed; the
      keyed fact is that vaccination (influenza, pneumococcal) prevents exacerbations, with caution about the
      intranasal influenza vaccine.
  s53 bronchodilator response "FEV1 >=12% or >=10% improvement in predicted FEV1" -- keyed as 12 percent only.
  s84 "clinical trails" (typo) -- fact keyed as "reduced need for corticosteroids".
"""

DECK = "PAJ5500 CMSI Asthma MBF 2026sc.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
CS = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

IO_DEF = "Define asthma"
IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
        "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
        "including applicable rehabilitative and palliative care), patient education, and prognosis of asthma.")
IO_ASP = "Define, describe, and discuss aspergillosis as it relates to asthma."
IO_PLAN = "Develop a treatment plan for patients with asthma based on symptoms and physical examination."
IO_EDU = ("List the components of patient education in treating asthma, including use of peak flow meters, "
          "metered-dose inhalers, nebulizers.")
IO_PFT = ("Describe how PFTs are utilized to aid in the diagnosis of pulmonary diseases and monitoring of "
          "patients with those diseases")
IO_POP = ("Identify medical care strategies for patients with asthma in the following patient populations. "
          "1. adolescent 2. adult 3. elderly")
IOS = [IO_DEF, IO_A, IO_ASP, IO_PLAN, IO_EDU, IO_PFT, IO_POP]

EXCLUDED_SLIDES = {1, 2, 3, 6, 16, 17, 21, 22, 69, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108}

SCOPE_BANNED = [
    r"\bGINA\b|Global Initiative",
    r"262 million|461,000|7\.8%|3,624|61\.9",
    r"minimal with high[- ]dose",
    r"Pneumovax|PPSV|19[- ]64",
    r"\bstep (?:1|2|3|4|5|6|one|two|three|four|five|six)\b",
    r"emergency department|intensive care|intubat",
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "atopic triad": "rhinitis",                # s25: allergic rhinitis, asthma, atopic dermatitis
    "atopic dermatitis": "eczema",             # s49: atopic dermatitis/eczema
    "catamenial": "menstrual",                 # s36: symptoms at predictable times in the menstrual cycle
    "cardiac asthma": "heart failure",         # s36: wheezing caused by decompensated heart failure
}
