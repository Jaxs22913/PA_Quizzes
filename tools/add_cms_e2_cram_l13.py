#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Lecture 13 (Chronic Vision Loss & Tumors) to the CMS I Exam 2 cram sheet.

Additive, fenced and idempotent, like the Lecture 11/12 adder. The cram sheet is
the night-before sheet: reasoning stays in the guide, this carries only what has
to come back cold. Capitals mark the discriminator, matching house style.

Content is the deck plus what the 31 August recording added and the slides do
not carry -- the under-50 framing for posterior subcapsular cataract, zonular as
the commonest paediatric type, and the liver as the commonest metastatic site
for ocular melanoma.
"""
import io, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2",
                    "cms-exam-2-cram-sheet.html")
OPEN, CLOSE = "<!--CMSE2L13-CRAM-->", "<!--/CMSE2L13-CRAM-->"


def sec(sid, title, acc, bg, zebra, ink, rows, star=False):
    body = "\n".join(
        '          <tr><td class="h">%s</td><td>%s</td></tr>' % (a, b) for a, b in rows)
    return """
  <section class="topic" id="%s" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">
    <div class="shead"><span class="dot" style="background:%s"></span><h2>%s%s</h2></div>
    <div class="scroll">
      <table>
        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>
        <tbody>
%s
        </tbody>
      </table>
    </div>
  </section>
""" % (sid, acc, bg, zebra, ink, acc, "&#9733; " if star else "", title, body)


CVL, CVLBG, CVLZ, CVLINK = "#8a6a12", "#f5f0dd", "#faf8ee", "#6d5410"
TUM, TUMBG, TUMZ, TUMINK = "#6b2233", "#f7e9ec", "#fcf4f6", "#571b29"
REF, REFBG, REFZ, REFINK = "#4a6b7a", "#e9eff2", "#f5f8fa", "#3a5561"

SECTIONS = "".join([

 sec("cvl-most", "THE &ldquo;MOST COMMON&rdquo; LIST SHE KEPT REPEATING", CVL, CVLBG, CVLZ, CVLINK, [
  ("Vision loss in CHILDREN", "AMBLYOPIA. 3&ndash;5% of kids."),
  ("EYE CANCER in ADULTS", "UVEAL MELANOMA &mdash; melanocytes of CHOROID, CILIARY BODY or IRIS."),
  ("Form of GLAUCOMA", "PRIMARY OPEN-ANGLE."),
  ("PAEDIATRIC cataract type", "ZONULAR."),
  ("Metastatic site for OCULAR MELANOMA", "THE LIVER."),
  ("Treatment for uveal melanoma", "RADIATION THERAPY &mdash; enucleation is now less common."),
  ("AMD split", "80% DRY · 20% WET."),
 ], star=True),

 sec("cvl-cataract", "CATARACT &mdash; TELL THE TYPES APART", CVL, CVLBG, CVLZ, CVLINK, [
  ("NUCLEAR", "BROWN central lens. Distance worse than near &mdash; a MYOPIC SHIFT, so they may read without glasses again."),
  ("CORTICAL", "SPOKE-like opacities from the PERIPHERY. Silent until central, then GLARE is the commonest complaint."),
  ("POSTERIOR SUBCAPSULAR", "Plate-like, BEHIND the lens. Faster onset, classically UNDER 50, on CORTICOSTEROIDS or DIABETIC. Symptoms BETTER after dilation."),
  ("PAEDIATRIC &mdash; ZONULAR", "COMMONEST paediatric type. White opacity round the nucleus."),
  ("PAEDIATRIC &mdash; POLAR", "Less common but CENTRAL, so caught earlier."),
  ("The rule", "A CATARACT ALONE NEVER CAUSES A RELATIVE AFFERENT PUPILLARY DEFECT. If there is one, something else is wrong."),
  ("Advanced sign", "LOSS OF RED REFLEX · leukocoria · pupil looks grey or white."),
  ("Treatment", "SURGERY ONLY. Deferred until it interferes with daily life &mdash; EXCEPT a NEONATE, operated early to prevent AMBLYOPIA."),
  ("Clouds again years later", "POSTERIOR CAPSULE OPACIFICATION. Treated with YAG LASER. The lens cannot regrow."),
 ]),

 sec("cvl-amd", "MACULAR DEGENERATION", CVL, CVLBG, CVLZ, CVLINK, [
  ("Where the vision goes", "CENTRAL, with DISTORTION. Glaucoma takes the PERIPHERY &mdash; that is the split."),
  ("DRY (non-exudative)", "80%. DRUSEN, pigmentary change, atrophy."),
  ("WET (exudative)", "20%. CHOROIDAL NEOVASCULARISATION bleeds into retina &rarr; DISCIFORM SCAR."),
  ("Home monitoring", "AMSLER GRID."),
  ("Confirming wet", "FLUORESCEIN ANGIOGRAPHY · OPTICAL COHERENCE TOMOGRAPHY."),
  ("Dry treatment", "STOP SMOKING. AREDS2: vitamins C and E, zinc, copper, lutein, zeaxanthin."),
  ("Why not beta carotene", "Original AREDS used it; dropped because it RAISED LUNG CANCER RISK IN SMOKERS."),
  ("Wet treatment", "INTRAVITREAL ANTI-VEGF · laser · photodynamic therapy."),
  ("Prognosis", "SLOWS progression. Does NOT reverse loss."),
 ]),

 sec("cvl-amblyopia", "AMBLYOPIA &amp; STRABISMUS", CVL, CVLBG, CVLZ, CVLINK, [
  ("Amblyopia in one line", "Brain FAVOURS one eye; the other never develops."),
  ("Three routes in", "STRABISMUS · ANISOMETROPIA (unequal refraction) · DEPRIVATION (cataract, ptosis, corneal opacity)."),
  ("Occlusion objection test", "Child OBJECTS when the GOOD eye is covered. Calm when the BAD eye is covered."),
  ("Numeric definition", "TWO LINES or more difference on best corrected acuity."),
  ("Screening", "ALL children UNDER 5."),
  ("Treatment", "PATCH or ATROPINISE THE GOOD EYE. Never the weak one."),
  ("Timing", "Good before 7, BETTER BEFORE 5."),
  ("Treated late", "Acuity can recover; STEREO VISION DOES NOT. They struggle with 3D and judging distance."),
  ("Strabismus giveaway", "BINOCULAR diplopia &mdash; GONE when either eye is covered."),
  ("Test", "COVER TEST · displaced CORNEAL LIGHT REFLEX in larger deviations."),
 ]),

 sec("cvl-tumors", "OCULAR TUMORS", TUM, TUMBG, TUMZ, TUMINK, [
  ("RETINOBLASTOMA giveaway", "LEUKOCORIA &mdash; white pupil, classically noticed in a PHOTOGRAPH."),
  ("Who", "Young children, almost exclusively. Genetic mutation, often RECESSIVE so family history misleads."),
  ("NO BIOPSY", "Risks SEEDING the tumour. Diagnosis is EXAM + IMAGING."),
  ("Primary care job", "RED REFLEX at every well-child check."),
  ("Family history", "Seen by an experienced ophthalmologist WITHIN THE FIRST 8 WEEKS OF LIFE."),
  ("Prognosis", "UNTREATED close to 100% FATAL. TREATED &gt;95% five-year survival. NO RECURRENCE AT 5 YEARS = CURED."),
  ("UVEAL MELANOMA", "Commonest ADULT eye cancer. Choroid, ciliary body or iris. Usually found INCIDENTALLY."),
  ("Melanoma vs freckle", "FEEDER VESSEL. A cancer builds its own blood supply; a freckle has none. Plus &gt;3 mm base, &gt;1 mm deep, GROWING."),
  ("Fine needle aspiration", "For MOLECULAR PROGNOSTIC TESTING, not to make the diagnosis."),
  ("Spread", "LIVER. Ten-year mortality ~32% overall; IRIS melanoma only 4&ndash;10% because it is VISIBLE and found early."),
  ("IRIS NEVUS", "FLAT, under 3 mm, AVASCULAR, inferior iris, stable. Low transformation risk but still monitored."),
  ("LISCH NODULES", "Tan, bilateral, multifocal &mdash; NEUROFIBROMATOSIS TYPE 1."),
  ("CONJUNCTIVAL MELANOMA", "RAISED and VASCULAR. A conjunctival NEVUS is FLAT with CLEAR CYSTS."),
 ], star=True),

 sec("cvl-iih", "IDIOPATHIC INTRACRANIAL HYPERTENSION", CVL, CVLBG, CVLZ, CVLINK, [
  ("Who", "OVERWEIGHT WOMAN OF CHILDBEARING AGE."),
  ("Symptoms", "Intractable HEADACHE · PULSATILE TINNITUS · TRANSIENT visual obscuration · pain behind the eyes."),
  ("Signs", "PAPILLEDEMA · visual field loss · CN6 (ABDUCENS) PALSY."),
  ("Order first", "MRI BRAIN + MR VENOGRAPHY &mdash; exclude a mass AND a venous sinus thrombosis."),
  ("Then", "LUMBAR PUNCTURE: ELEVATED OPENING PRESSURE. That is the confirmation."),
  ("Not the same as", "SYSTEMIC hypertension. Blood pressure may be normal."),
  ("Treatment", "ACETAZOLAMIDE promptly + WEIGHT REDUCTION programme."),
  ("The durable fix", "WEIGHT LOSS. Everything else buys time."),
  ("Last resort", "CSF diversion &mdash; optic nerve sheath fenestration or shunt."),
 ]),

 sec("cvl-refract", "REFRACTIVE ERRORS &amp; THE BLURRY-VISION DIFFERENTIAL", REF, REFBG, REFZ, REFINK, [
  ("MYOPIA", "LONG eyeball. Focus IN FRONT of retina. CONCAVE (negative) lens."),
  ("HYPEROPIA", "SHORT eyeball. Focus BEHIND retina. CONVEX (positive) lens."),
  ("ASTIGMATISM", "UNEVEN curvature &rarr; MULTIPLE focal points. TORIC lens."),
  ("Who to refer to", "Isolated refractive error &rarr; OPTOMETRY. Medical eye disease &rarr; OPHTHALMOLOGY."),
  ("Corneal opacity vs cataract", "OPACITY is on the CORNEA; CATARACT is the LENS."),
  ("Refractive vs everything else", "Refractive blur CORRECTS FULLY WITH LENSES. Nothing else here does."),
  ("The colour clue", "OPTIC NEUROPATHY is the one that takes COLOUR VISION. Think of it first if colours look washed out."),
  ("Functional visual loss", "NORMAL exam, NORMAL pressure, CLEAR lens, symptoms that do not fit anatomy."),
 ]),
])


def main():
    t = io.open(CRAM, encoding="utf-8").read()
    before = len(t)
    anchor = "\n  <footer>"
    fenced = OPEN + SECTIONS + CLOSE
    pat = re.compile(re.escape(OPEN) + ".*?" + re.escape(CLOSE), re.S)
    if pat.search(t):
        t = pat.sub(lambda _: fenced, t, count=1)
    else:
        assert t.count(anchor) == 1, "footer anchor not unique"
        t = t.replace(anchor, fenced + anchor)
    io.open(CRAM, "w", encoding="utf-8").write(t)
    print("cram %d -> %d bytes (+%d)" % (before, len(t), len(t) - before))

    blk = t[t.index(OPEN):t.index(CLOSE)]
    assert blk.count("<section") == blk.count("</section>") == 7, blk.count("<section")
    assert blk.count("<table>") == blk.count("</table>") == 7
    assert blk.count("<tr>") == blk.count("</tr>")
    assert t.index(CLOSE) < t.index("<footer>"), "block must sit above the footer"
    print("verified: 7 sections, %d rows, all above the footer" % blk.count('<td class="h">'))


if __name__ == "__main__":
    main()
