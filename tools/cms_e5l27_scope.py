# -*- coding: utf-8 -*-
"""Lecture 27 scope -- Arterial Occlusive Disease and Aortic Aneurysm (Carter).

Read by cms_e5_partition.py (guards) and imported by every Lecture 27 pool.
Not a question bank: check_pool_cites does not glob it.

Built SLIDES-ONLY (2026-09-25). The lecture is given on Zoom on 2026-10-01 and
no recording exists yet, so nothing here is weighted by audio. When the
recording lands, add REQUIRED / SCOPE_BANNED entries from what he says, the way
cms_e4l25_scope.py does.

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf pp. 15-16, checked
against the PDF with PyMuPDF on 2026-09-25), with the syllabus's own broken
inline numbering kept: items 2-6 are the disease list of objective 1, item 7 is
the second real objective and 8-12 its population list. Only the leading "1." /
"7." is dropped, as the Exam 4 precedent does.

  IO_A   the five conditions.
  IO_POP the populations objective. The deck has NO infant, child or adolescent
         content; questions carry IO_POP only where they test what the deck
         does say about age (PAD age thresholds s11, AAA sex ratio by age s80,
         dissection age s115, "advancing age" s86).

EXCLUDED_SLIDES (never cited):
  36, 44, 56, 103, 111   video poster frames with the video removed -- no content
  54                     no-text NEJM figure; stent types and restenosis options
                         are never named in the deck's text
  79                     flawed figure (misspelled labels, mispointed arrows)
  119                    files "dissecting" under TRUE aneurysms, while slide 114
                         presents dissection as its own entity -- contested
  120                    references

CONTESTED on the slides, so NEVER KEYED:
  Rutherford IIA arterial Doppler: "often audible" (s62 text) vs "often
      inaudible" (s65 table). IIA is keyed only on its prognosis and on the
      absence of sensory loss / weakness, never on its arterial Doppler.
  Slide 73's "What is the difference between a bruit and a murmur?" is asked
      and never answered.
  ABI "normal > 0.9-1.3" (s42) is a mixed notation; stems use values well
      inside a band (1.05, 0.62, 0.25, 1.45), never 0.4, 0.9 or 1.3.
  AAA thresholds are stated three ways (s95 elective repair >=5.0 cm women,
      ">5.5 cm or larger" men; s100 specialist referral >=4.5 cm; s101 consider
      surgery referral >=5.0 cm). Stems never sit on a boundary.
  AAA rapid growth is 0.5 cm in six months (s95, s99); TAA is >0.5 cm per YEAR
      (s109). Never swapped.
"""

DECK = "Arterial Occlusive Diseaase and Aneurysms - Carter.pptx"   # the filename's own spelling
C = lambda n: "%s, Slide %d" % (DECK, n)

IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing (including ordering and interpretation), management "
        "(acute and chronic, including applicable rehabilitative and palliative care), appropriate "
        "referrals, patient education, and prognosis of the following arterial occlusive disease and "
        "aortic aneurysm: 2. Arterial thrombosis/embolism 3. Peripheral artery disease 4. Carotid artery "
        "disease 5. Aortic aneurysms 6. Aortic dissection")
IO_POP = ("Identify medical care strategies for arterial occlusive disease and aortic aneurysm for the "
          "following populations. 8. infant 9. child 10. adolescent 11. adult 12. elderly")
IOS = [IO_A, IO_POP]

EXCLUDED_SLIDES = {36, 44, 54, 56, 79, 103, 111, 119, 120}

SCOPE_BANNED = [
    r"marginally threatened[^?.;]{0,80}arterial doppler", r"arterial doppler[^?.;]{0,80}marginally threatened",
    r"\bIIA\b[^?.;]{0,60}doppler",
    r"bruit[^?.;]{0,40}\bmurmur|\bmurmur[^?.;]{0,40}bruit",
    r"drug-eluting|drug-coated|covered stent|self-expanding|balloon-expandable",
    r"foam cell",
]

# Named findings in vignette stems carry their description in parentheses,
# taken from the deck. Keys are matched case-insensitively against the stem.
NAMED = {
    "dependent rubor": "red",                 # s29/s30: deep red when hanging down
    "grey turner": "flank",                   # s91: flank ecchymosis
    "amaurosis fugax": "curtain",             # s72 notes: like a curtain descending
    "leriche": "femoral pulses",              # s14 triad -- only if the stem names it
    "poikilothermia": "temperature",          # s34: difficulty regulating body temperature
    "livedo reticularis": "mottl",            # s68 names it but never describes it: keep it OUT of stems
    "buerger": "elevat",                      # s30: elevate the leg to 45 degrees
}
