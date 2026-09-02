#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cram rows for the gaps the Exam 2 slide scour turned up.

Companion to add_cms_e2_gapfill.py, which puts the reasoning in the guide. This
carries only what has to come back cold: the mimic lists, which are exactly the
kind of thing a vignette turns on and exactly what a disease-by-disease outline
leaves out. Additive, fenced, idempotent.
"""
import io, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2",
                    "cms-exam-2-cram-sheet.html")
OPEN, CLOSE = "<!--CMSE2-GAPFILL-CRAM-->", "<!--/CMSE2-GAPFILL-CRAM-->"


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


DX, DXBG, DXZ, DXINK = "#6b2233", "#f7e9ec", "#fcf4f6", "#571b29"
AN, ANBG, ANZ, ANINK = "#2f6b5a", "#e6f0ec", "#f0f6f3", "#22503f"

SECTIONS = "".join([

 sec("gap-anatomy", "THE EYE IN THREE LAYERS", AN, ANBG, ANZ, ANINK, [
  ("FIBROUS (outer)", "CORNEA &mdash; most of the FOCUSING POWER. SCLERA &mdash; shape + muscle attachment."),
  ("VASCULAR / UVEA (middle)", "IRIS &mdash; controls pupil size. CILIARY BODY &mdash; makes AQUEOUS + accommodation. CHOROID &mdash; NOURISHES THE RETINA."),
  ("NEURAL (inner)", "RETINA &mdash; rods and cones. MACULA &mdash; central vision. FOVEA &mdash; highest acuity. OPTIC DISC &mdash; blind spot."),
  ("Why the layer matters", "UVEITIS is MIDDLE-layer, which is why it takes iris + ciliary body + choroid together. Scleritis/episcleritis OUTER. Occlusions and detachments INNER."),
 ]),

 sec("gap-nystagmus", "NYSTAGMUS &mdash; THE TWO GROUPS", AN, ANBG, ANZ, ANINK, [
  ("JERK", "SLOW phase + FAST phase. Named for the FAST beat. INCREASES with gaze TOWARD the fast phase."),
  ("Most common jerk form", "HORIZONTAL &mdash; slow drift one way, quick snap back."),
  ("Horizontal jerk SUBTYPES", "Normal PHYSIOLOGIC GAZE-EVOKED &middot; INFANTILE &middot; SPASMUS NUTANS &middot; LATENT."),
  ("PENDULAR", "BOTH phases EQUAL velocity and amplitude &mdash; NO fast phase. Most often HORIZONTAL."),
  ("Pendular context", "CONGENITAL, or after PROLONGED BILATERAL BLINDNESS beginning in CHILDHOOD."),
  ("UPBEAT &mdash; the alarm", "ALWAYS ABNORMAL. CEREBELLAR or MEDULLARY lesion; less commonly DRUG INTOXICATION. Present only on UPWARD gaze."),
 ], star=True),

 sec("gap-ddx", "THE MIMIC LISTS", DX, DXBG, DXZ, DXINK, [
  ("MACULAR DYSTROPHIES mimicking AMD", "STARGARDT (yellow-white FLECKS) &middot; SORSBY (AUTOSOMAL DOMINANT, CNV like wet AMD) &middot; NORTH CAROLINA (congenital, NON-progressive) &middot; BEST / VITELLIFORM (LIPOFUSCIN mimics drusen)."),
  ("The tell for all four", "INHERITED, and they present YOUNGER than age-related degeneration."),
  ("LEUKOCORIA besides retinoblastoma", "COATS' (retinal TELANGIECTASIA with exudation) &middot; PERSISTENT FETAL VASCULATURE &middot; TOXOCARIASIS (granulomatous) &middot; RETINAL ASTROCYTOMA (glial, TUBEROUS SCLEROSIS) &middot; MEDULLOEPITHELIOMA (nonpigmented ciliary epithelium) &middot; CONGENITAL CATARACT &middot; OCULAR TOXOPLASMOSIS."),
  ("UVEAL MELANOMA by site", "IRIS (melanotic OR partly AMELANOTIC) &middot; CILIARY BODY &middot; CHOROID."),
  ("Two ciliary body signs", "SENTINEL VESSEL (dilated episcleral vessel over the tumour) and EXTRASCLERAL EXTENSION."),
  ("IRIS NEVUS", "INFERIOR half &middot; does NOT typically grow &middot; FLAT / under 1 mm &middot; not vascular &middot; may cause CORECTOPIA. Apparent around PUBERTY, ASYMPTOMATIC."),
  ("PIGMENTED IRIS differential", "FRECKLE (flat, no stromal involvement) &middot; LISCH NODULES (NF1) &middot; MELANOCYTOMA (granular; secondary glaucoma from PIGMENT DISPERSION) &middot; MELANOCYTOSIS (congenital, RAISES melanoma risk) &middot; COGAN-REESE / ICE (corneal ENDOTHELIAL abnormality) &middot; IRIS MELANOMA &middot; METASTATIC CARCINOMA."),
  ("Pushes an iris lesion toward MELANOMA", "INFERIOR location &middot; DIFFUSE configuration &middot; BLOOD in the anterior chamber."),
  ("NON-PIGMENTED CONJUNCTIVAL lesions", "SQUAMOUS CELL CARCINOMA (gelatinous/LEUKOPLAKIC; mistaken for AMELANOTIC melanoma) &middot; LYMPHOMA (SALMON-PINK, painless, fornix) &middot; KAPOSI SARCOMA (reddish-purple, HIV/AIDS) &middot; PYOGENIC GRANULOMA (rapidly growing red, after TRAUMA or SURGERY)."),
 ], star=True),
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
    assert blk.count("<section") == blk.count("</section>") == 3
    assert blk.count("<tr>") == blk.count("</tr>")
    assert t.index(CLOSE) < t.index("<footer>"), "block must sit above the footer"
    for need in ("<!--CMSE2L13-CRAM-->", "<!--CMSE2L14-CRAM-->"):
        assert need in t, "%s lost" % need
    print("verified: 3 sections, %d rows, above the footer, earlier blocks intact"
          % blk.count('<td class="h">'))


if __name__ == "__main__":
    main()
