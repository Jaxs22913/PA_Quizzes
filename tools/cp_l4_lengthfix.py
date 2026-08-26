# -*- coding: utf-8 -*-
"""Length-bias fixes for the Clinical Pathophysiology I Lecture 4 pool.

A question is gameable when the correct option is the uniquely longest AND is
at least 8 characters and 18 per cent longer than the runner-up. This pool
started at 50.4 per cent -- the worst of any on the site -- because a
pathophysiology answer is a MECHANISM and a mechanism takes a clause, while a
wrong answer is usually just the name of a different disease.

THE RULE IS PAD, NEVER TRIM. Shortening these correct answers would delete the
mechanism, which is the entire content of a Clinical Pathophysiology question.
So each runner-up distractor is lengthened to carry its own mechanism, which
also makes it a better distractor: "That is cataract" tests nothing, while
"opacification of the crystalline lens from crystallin aggregation" makes the
student actually discriminate.

KEYS ARE (question index, option index) INTO THE CONCATENATED POOL, never the
option string -- option strings recur across questions. cp_l4_partition.py
asserts no fix targets a correct option.
"""
FIXES = {
 (13, 1): "About 120 million, concentrated in the peripheral retina rather than the fovea",
 (14, 3): "Generating the action potentials, relaying them to the thalamus, and modulating contrast",
 (17, 3): "By the retinal pigment epithelium, pumping it into the subretinal space behind the retina",
 (20, 1): "Water and dissolved electrolytes only, acting purely as a transparent space-filler behind the lens",
 (29, 3): "Loss of lens elasticity with age, so the lens can no longer change shape",
 (30, 3): "It causes progressive optic nerve damage and a loss of peripheral field",
 (31, 2): "Only glaucoma, through a sustained rise in intraocular pressure over years",
 (32, 2): "The cornea flattens progressively with age, reducing its refractive contribution",
 (33, 1): "Inability to focus on distant objects, so distance vision blurs first",
 (36, 1): "Reduced best-corrected visual acuity arising from abnormal visual development",
 (39, 2): "Raised intraocular pressure with progressive optic disc cupping and field loss",
 (40, 1): "Ocular misalignment arising from extraocular muscle imbalance or nerve palsy",
 (43, 2): "Any time in childhood or adulthood, because the deficit is purely optical and correctable",
 (45, 1): "Osmotic swelling of the lens driven by sorbitol accumulating inside it",
 (48, 3): "Gradual central distortion in which straight lines begin to appear bent or wavy",
 (49, 3): "A pale, swollen optic disc with blurred margins and no visible cup",
 (50, 3): "Only at the equator of the lens, where the suspensory zonules attach to it",
 (52, 1): "The sclera itself, deep to the episclera",
 (54, 3): "The orbital soft tissue lying behind the globe, posterior to the septum",
 (55, 2): "It is limited to the anterior segment and spares the vitreous",
 (58, 1): "A vision-threatening emergency with severe deep boring pain and scleral melting",
 (62, 1): "Rheumatoid arthritis, granulomatosis with polyangiitis and systemic vasculitis",
 (65, 3): "Optic disc cupping with progressive peripheral field loss",
 (67, 1): "Erythema and oedema of the lid alone, held forward by the orbital septum",
 (68, 2): "The tear film continuously washes the infection away, so the globe is spared",
 (69, 2): "Aqueous tear production falls because the lacrimal gland itself is inflamed",
 (70, 1): "Bacterial and viral infection of the ocular surface, both causing purulent discharge",
 (71, 3): "A wedge of fibrovascular tissue growing across and over the corneal limbus",
 (73, 1): "A vesicle on the eyelid margin, indicating that the meibomian glands are involved",
 (74, 3): "Rupture of the episcleral capillaries, leaking blood beneath the conjunctiva",
 (76, 1): "An acute, tender, focal abscess of a gland sitting at the eyelid margin",
 (80, 3): "The circular junction where the conjunctiva meets the edge of the cornea",
 (82, 1): "An abrasion involves the stroma, while an ulcer is limited to the epithelium",
 (84, 2): "The abrasion is always sterile while the ulcer is always secondarily infected",
 (85, 3): "Both involve the nasolacrimal duct itself, differing only in the causative organism",
 (87, 1): "Leakage of aqueous humour out of the anterior chamber into the subconjunctival space",
 (88, 1): "Chronic ultraviolet light, wind and airborne dust exposure over many years",
 (89, 3): "Recurrent by definition, so it requires long-term ophthalmology follow-up",
 (90, 1): "Cholesterol-filled plaques deposited around the lids, associated with hyperlipidaemia",
 (91, 3): "Fibrovascular conjunctival tissue, associated with chronic ultraviolet exposure",
 (92, 2): "Raised pressure detaches the neurosensory retina from the underlying pigment epithelium",
 (94, 1): "The iridocorneal angle narrows anatomically and blocks aqueous outflow suddenly",
 (95, 1): "It presents abruptly with severe pain, headache and vomiting",
 (96, 3): "Vascular endothelial growth factor drives fragile new vessel formation on the disc",
 (98, 2): "Flashing lights, a sudden shower of floaters, and a curtain falling across the field",
 (100, 1): "Fibrovascular membranes grow across the retinal surface and pull the retina forward",
 (101, 2): "Breakdown of the blood-retinal barrier lets fluid collect in the subretinal space",
 (102, 1): "A full-thickness retinal tear admits liquefied vitreous fluid beneath the retina",
 (105, 3): "Chronic corticosteroid use, Down syndrome and ultraviolet light exposure",
 (106, 3): "Slow loss of central detail with progressive distortion of straight lines",
 (108, 1): "Choroidal neovascularisation breaching upward into the subretinal space",
 (110, 2): "Loss of peripheral vision first, with the central field spared until late",
 (111, 1): "Extracellular lipofuscin debris accumulating beneath the retinal pigment epithelium",
 (113, 1): "Progressive optic disc cupping with tunnel vision and peripheral loss",
 (116, 1): "Raised intraocular pressure mechanically compresses the retinal vessels",
 (117, 1): "Neovascularisation growing on the optic disc and across the retinal surface",
 (118, 2): "Accumulation of lipofuscin and apolipoprotein beneath the pigment epithelium",
 (119, 1): "Hard exudates are nerve fibre layer infarcts, while cotton-wool spots are lipid deposits",
 (120, 2): "Lens opacification with progressive loss of the red reflex",
 (121, 1): "United States adults aged over seventy-five years",
 (123, 3): "Optic nerve, chiasm, optic radiation, lateral geniculate nucleus, then occipital cortex",
 (124, 3): "Contralateral superior quadrantanopsia, or pie in the sky",
 (126, 1): "The lesion damages the temporal retinal fibres instead, and those carry nasal vision",
 (129, 1): "Contralateral inferior quadrantanopsia instead",
 (130, 1): "Contralateral homonymous hemianopsia with no macular sparing at all",
 (131, 2): "Peripheral vision on both sides, because the two visual fields overlap entirely",
 (132, 2): "Posterior cerebral artery occlusion in the occipital lobe",
}
