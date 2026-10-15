# -*- coding: utf-8 -*-
"""Lecture 32 scope -- Infective Endocarditis (Reynolds), CMS I Exam 5.

Read by cms_e5_partition.py (guards) and imported by every Lecture 32 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Professor Lauren Reynolds, MSPA, PA-C. Title slide: "Presented by Professor L. Reynolds,
MSPA, PA-C, CMS I Fall 2026". The 2026-10-14 recording (three Notability segments, 5.3 + 39.9 + 57.9
min) is hers: she refers to "this morning's lecture" on the pericardium (her Lecture 31 the same day)
and to "Professor Reynolds" in her own example. calendar-data.js also names Reynolds: no conflict.

Built from the deck, with the Notability transcript read for SCOPE and EMPHASIS only (2026-10-15).
The recording adds no content the deck lacks (slides-only grounding).

WHAT SHE SAID ABOUT SCOPE (Notability, segment 1 and 3):
  Prophylaxis -- "you do need to know this is the prophylaxis stuff" ("I'm gonna expect you to know
      this"). REQUIRED below puts at least three prophylaxis stems in every form.
  Doses -- "Do I need you to know doses? No ... don't memorize doses" (adult regimens) and again for
      children: "You do not need to know the doses, still." Agents and routes are keyed, never doses.
  Duke criteria -- "I'm not gonna make you go into like the history ... What is it right now?"; the
      modified Duke criteria as taught, "very helpful, very important for how you can diagnose".
  Pediatrics -- "you will have dedicated peds content in CS3"; the pediatric slides are an
      introduction, and "unless otherwise specified ... I mean grown-ups".
  Emphasis (for the guide's stars, Phase 4): blood cultures before antibiotics ("I cannot say it
      clearly enough"), a high index of suspicion for methicillin-resistant Staphylococcus aureus
      "from the jump", injection drug use and the tricuspid valve, the clock for 4-6 weeks of
      antibiotics starting at the first NEGATIVE culture, infectious disease consult "period",
      heart failure from valve dysfunction as the commonest surgical indication.

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 17, "Infective Endocarditis", read with
PyMuPDF 2026-10-15), the syllabus's own numbering kept inline and only the leading "1." dropped.
Objectives 4, 5 and 6 are their own strings, punctuation included.

EXCLUDED_SLIDES (never cited):
  1, 9, 43   title, "Acute vs. Subacute" divider, "CASES" (cases were never given: "we ran out of time")
  38         Medicine at a Glance summary page: its organism shares (streptococci 50-70%) contradict
             slides 18-20 (Staphylococcus aureus now leads), and its "high risk" valve list (mitral or
             aortic regurgitation, ventricular septal defect, patent ductus) is risk of ENDOCARDITIS,
             not the prophylaxis indications of slides 36 and 42 -- a trap if cited.

CONTESTED on the slides, or slide vs audio, and how each is handled (truth wins):
  s13 layout: "Associated with acute infective endocarditis" sits in the JANEWAY box. True (Janeway
      lesions are the stigmata of acute, usually staphylococcal, disease) and keyed. Janeway "raised or
      macular": truth is flat (macular) and painless -- "raised" is never keyed. Osler "palms, soles,
      distal phalanges": truth is the pads of the fingers and toes -- Osler nodes are keyed on the
      finger and toe pads, never on the palms. Osler mechanism "septic emboli vs. immune complexes":
      keyed as IMMUNOLOGIC (slide 22's Duke table and slide 13's note); Janeway as vascular/embolic.
      Audio: "they both are related to septic emboli" -- not keyed.
  s12 splinter hemorrhages "can be painful": not keyed.
  s23 mnemonic says fever "> 38 C" and blood culture "positive > 2 times 12 hrs apart"; slide 22's
      table says ">= 38.0 C" and lists the full persistence rules. Stems use 38.6 C and above, never
      38.0; the major blood-culture criterion is keyed as the table gives it.
  s23 note: the 2023 Duke-ISCVID update (molecular, PET-CT, intraoperative findings). Not keyed: the
      slides teach the modified Duke criteria.
  s25 "Blood cultures x 3 sets ... within 24 h" vs its note (2023 criteria dropped the strict timing).
      Keyed: three sets from separate sites, drawn BEFORE antibiotics; the 24-hour window is never
      keyed as a diagnostic requirement.
  s37 mortality figures (Staphylococcus aureus 30% / 50% prosthetic / 5% injection drug use): keyed
      only qualitatively (most lethal organism; worst with a prosthetic valve; lower in people who
      inject drugs).
  s16 lists enterococci under BOTH acute and subacute: never used to tell the two apart.
  Audio vs s27: she said empiric therapy is "vancomycin, rifampin, and gentamicin"; s27 gives empiric
      vancomycin + ceftriaxone (native valve, subacute, prosthetic valve > 1 year) and vancomycin +
      gentamicin + cefepime (prosthetic valve <= 1 year). The triple she named is the Staphylococcus
      aureus PROSTHETIC valve regimen (s27, s28, s30). Keyed as the slides give it.
  Audio vs s35: "an IM injection of amoxicillin"; s35 and s36 give AMPICILLIN (or cefazolin or
      ceftriaxone) intramuscular or intravenous when oral is impossible. Keyed as the slides.
  Audio vs s34: she "kind of disagrees" with no prophylaxis for bronchoscopy; s34 and s36 (American
      Heart Association) say bronchoscopy without mucosal incision needs none. Keyed as the slides.
  Audio only (never keyed, slides-only): Streptococcus gallolyticus and colon cancer; VRE; PICC lines;
      trough levels; Coxiella and Bartonella regimens (s31, which she said was missing from the handout).
  s31 HACEK regimen: ceftriaxone (or ampicillin-sulbactam) is keyed; she also said ceftriaxone aloud.
"""

DECK = "32. Infective Endocarditis FALL 2026 SV.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)

IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing (including ordering and interpretation), management "
        "(acute and chronic, including applicable rehabilitative and palliative care), appropriate "
        "referrals, patient education, and prognosis of the following: 2. Acute endocarditis "
        "3. Subacute endocarditis")
IO_PROPH = "Discuss prophylaxis for bacterial endocarditis."
IO_REGIMEN = "Discuss indications and antibiotic regimens for subacute bacterial endocarditis prophylaxis."
IO_DUKE = "Demonstrate understanding of modified Duke diagnostic criteria."
IO_POP = ("Identify medical care strategies for infective endocarditis for the following populations. "
          "8. infant 9. child 10. adolescent 11. adult 12. elderly")
IOS = [IO_A, IO_PROPH, IO_REGIMEN, IO_DUKE, IO_POP]

EXCLUDED_SLIDES = {1, 9, 38, 43}

SCOPE_BANNED = [
    r"2023 Duke|Duke-ISCVID|ISCVID",
    r"\b(?:50|60|70)\s?(?:-|to|–)\s?70\s?%",            # s38's streptococcal share
    r"colon cancer|colorectal|bovis",                   # audio-only association
    r"Coxiella|Bartonella|hydroxychloroquine",
    r"raised (?:or macular )?(?:hemorrhagic )?(?:lesion|macule)s? on the (?:palms|soles)",
    r"\bkg\b|per kilogram|milligrams? per",              # weight-based doses
    r"amoxicillin[^?.;]{0,40}intramuscular|intramuscular[^?.;]{0,40}amoxicillin",
]

# Named findings in vignette stems carry their description in parentheses,
# taken from the deck. Keys are matched case-insensitively against the stem.
NAMED = {
    "osler": "painful",                 # s13: PAINFUL, immunologic
    "janeway": "painless",              # s13: NONTENDER, embolic
    "roth spot": "white-centered",      # s12: white-centered retinal hemorrhage
    "splinter": "under the nail",       # s12: fingernails and toenails
    "petechia": "pinpoint",             # s12: minute hemorrhages
    "tumor plop": "diastolic",          # s21: "tumour plop" or mid-diastolic rumble
    "mycotic aneurysm": "infected",     # s10: ruptured mycotic aneurysm
    "libman-sacks": "non-infective",    # s21
}

# She said the prophylaxis material is expected knowledge: at least three per form.
REQUIRED = [("Prophylaxis", r"prophyla", r".", 3)]
