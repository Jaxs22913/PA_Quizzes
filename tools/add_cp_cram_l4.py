#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Lecture 4 (Ophthalmic Pathophysiology) topics to the Clin Path I cram sheet.

The guide carries the explanation; this carries only what has to be recallable
cold. Mechanism only -- CMS I Exam 2 covers this same condition list from the
management side.

THE FIRST SECTION IS HIS STATED EXAM LIST, verbatim, because that is the single
most useful thing on the sheet. Recovered from BOTH transcripts: Notability's
dropped glaucoma, faster-whisper's dropped cataracts.

NOTHING IS DRILLED ON THE NORMAL INTRAOCULAR PRESSURE -- the deck says 10-21 on
slide 24 and about 6-19 on slide 25. Guarded below.

Appended after the Lecture 3 sections, in syllabus order. Idempotent.
"""
import os, re, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 1",
                    "cp-exam-1-cram-sheet.html")

TOPICS = [
 ("l4-exam-list", "★ KNOW FOR EXAM — HE STATED THESE", "#b8860b", "#f7efd9", "#fbf7ec", "#7a5a08", [
   ("He opened with “This is for the test”", "CATARACTS · MACULAR DEGENERATION · THE VISUAL PATHWAY · REFRACTION ERRORS · RETINAL DETACHMENT CAUSES · GLAUCOMA · PRESBYOPIA (added after he said “that’s it”)."),
   ("Glaucoma — what exactly he asked", "“What’s the PATHOPHYSIOLOGICAL EXPLANATION for vision loss there?” Answer: raised pressure compresses GANGLION CELL AXONS → APOPTOSIS → DISC CUPPING. It is NERVE loss, not media opacity."),
   ("Visual pathway — SCOPED", "KNOW A, B, C: optic NERVE, optic CHIASM, optic TRACT. D (optic radiation) and E (occipital cortex) he DEFERRED TO NEUROLOGY — “you can know that if you want.” He also said “MEMORISE THIS: optic nerve, optic chiasm, optic tract.”"),
   ("Refraction errors — what he wants", "GLOBE GEOMETRY, not lens prescriptions. “Not that important, concave and convex for my purposes. MORE IMPORTANT is knowing the difference between MYOPIA, HYPEROPIA, and the GLOBE SHAPE.” He then contradicted himself on the lenses and corrected mid-sentence — trust the slide, expect the geometry."),
   ("Retinal detachment — what he wants", "“The DIFFERENT THINGS that can cause retinal detachment.” Three mechanisms, not one presentation."),
   ("Presbyopia — the one he came back for", "The lens is normally ELASTIC; with age it HARDENS, so it can no longer change shape → CANNOT ACCOMMODATE. Tied to the A in PERRLA (Pupils Equal, Round, Reactive to Light, ACCOMMODATION)."),
 ]),
 ("l4-anatomy", "Eye Anatomy & Vision Physiology", "#3b2a5e", "#e4e1e8", "#f1f0f4", "#2e2149", [
   ("The three tunics", "FIBROUS (outer): sclera + cornea. UVEA (vascular, middle): choroid + ciliary body + iris. RETINA (neurosensory, inner)."),
   ("Five unique features", "CORNEA AVASCULAR — oxygenated by AIR AND TEARS, ~70% OF REFRACTION. RETINA has the HIGHEST OXYGEN CONSUMPTION of any tissue, higher than cortex. Only place to see LIVE NEURAL TISSUE and NATIVE MICROCIRCULATION directly. ~83% of knowledge acquisition."),
   ("Three requirements for vision", "IMAGE FORMATION (cornea + lens onto retina) · PHOTORECEPTOR EXCITATION (photons → HYPERPOLARISING potentials) · NEURAL TRANSMISSION (optic nerve → occipital cortex)."),
   ("Rods vs cones", "RODS ~120 MILLION — dim light, PERIPHERAL retina. CONES ~6 MILLION — colour + sharp acuity, concentrated in the FOVEA CENTRALIS within the macula."),
   ("Retinal pigment epithelium — 3 jobs", "ABSORBS SCATTERED LIGHT · PHAGOCYTOSES outer photoreceptor segments · maintains the BLOOD-RETINAL BARRIER."),
   ("Retinal interneurons", "BIPOLAR, HORIZONTAL, AMACRINE modulate the signal → GANGLION CELLS, whose axons form the OPTIC NERVE."),
   ("Optic disc", "THE BLIND SPOT — no rods or cones."),
   ("Aqueous: made where, drains where", "MADE by the NON-PIGMENTED EPITHELIUM OF THE CILIARY BODY into the POSTERIOR chamber → through the pupil → ANTERIOR chamber (nourishes avascular LENS and CORNEA) → TRABECULAR MESHWORK → CANAL OF SCHLEMM → EPISCLERAL VEINS. That route is all of glaucoma."),
   ("Vitreous", "WATER + TYPE II COLLAGEN + HYALURONIC ACID. Shock absorber pressing retina onto RPE. Its age LIQUEFACTION is all of rhegmatogenous detachment."),
 ]),
 ("l4-refract", "Globe Shape & Age-Related", "#6a4fa3", "#eae6f2", "#f5f3f9", "#533e7f", [
   ("MYOPIA", "Axial globe TOO LONG → focal point IN FRONT of the retina. Near vision preserved."),
   ("HYPEROPIA", "Axial globe TOO SHORT → focal point BEHIND the retina. Distance vision preserved."),
   ("ASTIGMATISM", "IRREGULAR CORNEAL OR LENS CURVATURE → non-spherical focal points, so NOTHING focuses properly anywhere. Can STACK on myopia or hyperopia."),
   ("PRESBYOPIA", "LENS SCLEROSIS, loss of elasticity + loss of ciliary accommodation → cannot focus NEAR. “Readers”/bifocals."),
   ("STRABISMUS = MECHANICAL", "Visual axes fail to land on corresponding retinal points. ESOtropia in · EXOtropia out · HYPERtropia up · HYPOtropia down. From EOM IMBALANCE or CN III/IV/VI PALSY."),
   ("AMBLYOPIA = VISUAL DEFICIT", "Reduced BEST-CORRECTED acuity from abnormal visual processing in the CRITICAL DEVELOPMENTAL PERIOD. Causes: uncorrected strabismus, severe refractive error, DEPRIVATION (congenital cataract, ptosis)."),
   ("Amblyopia treatment window", "BEFORE AGE 7–8 — because that is when the visual system stops being plastic."),
 ]),
 ("l4-cat-glauc", "Cataract & Glaucoma", "#8f5aa8", "#efe8f3", "#f7f3f9", "#704683", [
   ("CATARACT — four mechanisms", "SENILE: insoluble aggregation of LENS CRYSTALLIN PROTEINS. DIABETES: glucose → SORBITOL → OSMOTIC SWELLING. DRUGS/TRAUMA: chronic CORTICOSTEROIDS, capsule rupture. CONGENITAL/ENVIRONMENTAL: DOWN SYNDROME, UV, oxidative damage."),
   ("Cataract presentation", "GRADUAL, PAINLESS, BILATERAL blurring · GLARE AROUND HEADLIGHTS AT NIGHT · MONOCULAR DIPLOPIA · altered colour. EXAM: LOSS OF THE RED REFLEX, leukocoria if severe. Usually PERIPHERAL in the lens; NUCLEAR is often post-TRAUMATIC."),
   ("GLAUCOMA — the hallmark (he asked for this)", "Raised IOP compresses RETINAL GANGLION CELL AXONS → GANGLION CELL APOPTOSIS → progressive OPTIC DISC CUPPING, cup-to-disc ratio > 0.5."),
   ("OPEN-ANGLE", "Angle stays OPEN; MICROSCOPIC RESISTANCE in the TRABECULAR MESHWORK impairs outflow → gradual rise. INSIDIOUS, PAINLESS, BILATERAL. PITFALL: ASYMPTOMATIC until severe PERIPHERAL loss (“tunnel vision”)."),
   ("ANGLE-CLOSURE", "MYDRIASIS displaces iris forward against cornea (IRIS BOMBÉ) → total outflow blockage → spike ABOVE 50 mmHg. SEVERE PAIN, HEADACHE, HALOS, CLOUDY CORNEA, FIXED MID-DILATED PUPIL, NAUSEA/VOMITING."),
   ("The deck contradicts itself on normal IOP", "Slide 24 says 10–21 mmHg; slide 25 says “about 6–19.” PD2’s deck independently says 10–21. NOTHING IS GRADED ON THIS. What is NOT disputed: the acute spike ABOVE 50."),
 ]),
 ("l4-retina", "Retina, Macula & Diabetic Cascade", "#2f7d76", "#e2edec", "#f0f6f5", "#25625c", [
   ("Why age matters first", "The VITREOUS LIQUEFIES with age. Liquefied vitreous is what can pass through a break."),
   ("RHEGMATOGENOUS", "FULL-THICKNESS TEAR → liquefied vitreous enters the SUBRETINAL SPACE and PEELS the retina off the RPE. Risks: PVD, AGE, SEVERE MYOPIA, TRAUMA, LATTICE DEGENERATION. Symptoms: PHOTOPSIA · SHOWER OF FLOATERS · CURTAIN FALLING."),
   ("TRACTIONAL", "Proliferative FIBROVASCULAR MEMBRANES on the retinal surface PHYSICALLY PULL the retina off. Chiefly PROLIFERATIVE DIABETIC RETINOPATHY; also prior trauma/surgery/vitrectomy scarring."),
   ("EXUDATIVE (SEROUS)", "Subretinal fluid with NO TEAR AND NO TRACTION — BLOOD-RETINAL BARRIER BREAKDOWN. Causes: SEVERE MALIGNANT HYPERTENSION, SARCOIDOSIS, CHOROIDAL MELANOMA."),
   ("DRY (ATROPHIC) AMD", "Slow bilateral degeneration of photoreceptors, RPE and choroid. HALLMARK: DRUSEN — yellow extracellular debris (LIPOFUSCIN, APOLIPOPROTEINS) beneath the RPE and BRUCH MEMBRANE. Slow central loss, METAMORPHOPSIA, SCOTOMA."),
   ("WET (NEOVASCULAR) AMD", "HYPOXIA + INFLAMMATION → CHOROIDAL NEOVASCULARISATION beneath the RPE into the subretinal space. Leak → RAPID central loss, DISCIFORM SCARRING, detachment. ~90% OF SEVERE AMD BLINDNESS."),
   ("Pathogenesis of AMD", "UNKNOWN — the deck says so for both forms."),
   ("Two blindness statistics — do not swap them", "DIABETIC RETINOPATHY: leading cause of new-onset blindness in US adults 20–74. MACULAR DEGENERATION: leading cause in US adults OVER 75."),
   ("Diabetic retinopathy cascade", "CHRONIC HYPERGLYCAEMIA damages capillaries + endothelial basement membranes → OCCLUSION + HYPOXIA. NON-PROLIFERATIVE: dilated veins, MICROANEURYSMS, dot/blot haemorrhages, HARD EXUDATES (lipid, OUTER PLEXIFORM layer), COTTON-WOOL SPOTS (NERVE FIBRE layer ischaemia), macular oedema. PROLIFERATIVE: ischaemia → VEGF → NEOVASCULARISATION → vitreous haemorrhage, traction, detachment."),
 ]),
 ("l4-fields", "Visual Field Deficits by Lesion Site", "#a4502a", "#f2e6e1", "#f9f3f0", "#803e21", [
   ("THE ONE FACT EVERYTHING FOLLOWS FROM", "NASAL retinal fibres — which carry the TEMPORAL visual fields — CROSS at the chiasm. TEMPORAL retinal fibres stay IPSILATERAL."),
   ("The pathway", "OPTIC DISC → OPTIC NERVE → CHIASM → OPTIC TRACT → LATERAL GENICULATE NUCLEUS → OPTIC RADIATION → OCCIPITAL CORTEX."),
   ("A — ipsilateral OPTIC NERVE", "MONOCULAR BLINDNESS. Causes: trauma, optic neuritis, ischaemic optic neuropathy."),
   ("B — OPTIC CHIASM (centre)", "BITEMPORAL HEMIANOPSIA — only the crossing NASAL fibres are cut, and they carry the TEMPORAL fields. Commonest cause: PITUITARY ADENOMA."),
   ("C — OPTIC TRACT / LGN", "CONTRALATERAL HOMONYMOUS HEMIANOPSIA. Stroke, tumour, demyelination."),
   ("D and E — HE DEFERRED THESE", "D temporal optic radiation → contralateral SUPERIOR quadrantanopsia (“pie in the sky”). E occipital cortex, PCA occlusion → contralateral homonymous hemianopsia WITH MACULAR SPARING (dual supply). “You can know that if you want.”"),
   ("Losing one eye", "Loses the BINOCULAR OVERLAP and therefore DEPTH PERCEPTION. Everything becomes flat."),
 ]),
]


def section(t):
    tid, title, acc, bg, zeb, ink, rows = t
    body = "\n".join(
        '          <tr><td class="h">%s</td><td>%s</td></tr>' % (H.escape(a), H.escape(b))
        for a, b in rows)
    return ('\n  <section class="topic" id="%s" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">\n'
            '    <div class="shead"><span class="dot" style="background:%s"></span><h2>%s</h2></div>\n'
            '    <div class="scroll">\n      <table>\n'
            '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
            '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n'
            % (tid, acc, bg, zeb, ink, acc, H.escape(title), body))


def main():
    s = open(CRAM, encoding="utf-8").read()
    for tid in [t[0] for t in TOPICS]:
        s = re.sub(r'\n  <section class="topic" id="%s".*?\n  </section>\n' % re.escape(tid),
                   "", s, flags=re.S)
        s = re.sub(r'      <a href="#%s"[^\n]*\n' % re.escape(tid), "", s)

    last = s.rindex('<section class="topic"')
    end = s.index("\n  </section>", last) + len("\n  </section>\n")
    links_anchor = s.rindex("</a>\n", 0, s.index("</nav>") if "</nav>" in s else len(s)) + len("</a>\n")
    links = "".join(
        '      <a href="#%s" style="color:%s"><span class="dot" style="background:%s"></span>%s</a>\n'
        % (t[0], t[5], t[2], t[1]) for t in TOPICS)
    s = s[:end] + "".join(section(t) for t in TOPICS) + s[end:]
    s = s[:links_anchor] + links + s[links_anchor:]

    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th", "div"):
        o, c = len(re.findall(r"<%s[ >]" % tag, s)), s.count("</%s>" % tag)
        assert o == c, "%s: %d open, %d close" % (tag, o, c)
    ids = set(re.findall(r'id="([^"]+)"', s))
    dangling = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a and a not in ids]
    assert not dangling, "dangling jump links: %r" % dangling
    assert "**" not in s, "markdown emphasis left in a cram row"

    # nothing may drill the disputed pressure except the row that IS the dispute
    rows = "".join(r[1] for t in TOPICS for r in t[6] if "contradicts" not in r[0])
    assert not re.search(r"\b10\s*[–-]\s*21\b|\b6\s*[–-]\s*19\b", rows), \
        "normal intraocular pressure is being drilled, but the deck states it two ways"

    # his seven must all be on the sheet
    sheet = "".join(r[0] + r[1] for t in TOPICS for r in t[6]).lower()
    for term in ("cataract", "macular degeneration", "visual pathway", "refraction error",
                 "retinal detachment", "glaucoma", "presbyopia"):
        assert term in sheet, "%r is on his stated exam list but not on the cram sheet" % term

    open(CRAM, "w", encoding="utf-8").write(s)
    print("Lecture 4 cram topics added: %d sections, %d rows"
          % (len(TOPICS), sum(len(t[6]) for t in TOPICS)))
    print("tag balance, jump links, disputed-pressure guard and exam-list coverage verified")


if __name__ == "__main__":
    main()
