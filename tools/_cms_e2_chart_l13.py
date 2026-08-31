# -*- coding: utf-8 -*-
"""Lecture 13 rows for the ophthalmology comparison chart.

Chronic Vision Loss & Tumors, 31 August. Same shape as _cms_e2_chart_l1112:
  ROWS_L13  (name, group, giveaway, presentation, testing, treatment,
             urgency, education, slides, deck)
  DIFF_L13  name -> (pain, laterality, key exam abnormality)
  IMGS_L13  name -> (filename, slide)

Primary open-angle glaucoma is DELIBERATELY ABSENT: Lecture 12 already carries
"Chronic open-angle glaucoma" and two rows for one disease would be worse than
none. Lecture 13's extra detail on it lives in the guide instead.

Every image here was resolved against its slide's own A/B/C/D or ABOVE/BELOW
label by geometry, not by extraction order -- see _cms_e2_l13_figures.py. On
slide 11 the extraction order maps to labels A, D, C, B, so soft drusen is _1
and the neovascular haemorrhage is _3.
"""
CVL = "Chronic vision loss"
REF = "Refractive"
TUM = "Ocular tumors"
D13 = "Chronic Vision Loss & Tumors"

ROWS_L13 = [
 ("Idiopathic intracranial hypertension", CVL,
  "<b>Overweight woman of childbearing age</b> &middot; <b>pulsatile tinnitus</b> &middot; transient greyouts",
  "Intractable headache of variable character, <b>transient visual obscuration</b>, intracranial noises, pain behind the eyes, mild pain on eye movement.",
  "<b>MRI brain with MR venography FIRST</b> to exclude a mass and a venous sinus thrombosis, <b>then lumbar puncture: elevated opening pressure</b>. Ophthalmology for formal perimetry and optic nerve photography.",
  "<b>Acetazolamide promptly</b>, plus a supervised <b>weight reduction</b> programme. Surgical CSF diversion (optic nerve sheath fenestration or shunt) only if medical therapy fails.",
  "Urgent",
  "<b>Weight loss is the only durable fix</b>; medication covers the patient while that happens. Followed jointly by ophthalmology and neurology.",
  "4&ndash;5", D13),

 ("Age-related macular degeneration &mdash; dry", CVL,
  "<b>Central</b> blur with <b>distortion</b> &middot; <b>drusen</b> &middot; gradual",
  "<b>80% of cases.</b> Blurred central vision with a central scotoma. Non-exudative: <b>drusen, pigmentary change and atrophy</b>.",
  "<b>Amsler grid for home monitoring</b> and serial slit lamp examination.",
  "<b>STOP SMOKING.</b> <b>AREDS2</b> supplement: vitamins C and E, zinc, copper, lutein, zeaxanthin.",
  "Routine",
  "Treatment <b>slows progression but does not reverse</b> vision already lost. The original AREDS used high-dose beta carotene, dropped because it <b>raised lung cancer risk in smokers</b>.",
  "11, 14", D13),

 ("Age-related macular degeneration &mdash; wet", CVL,
  "<b>Sudden</b> worsening of a <b>central</b> blur &middot; <b>neovascular</b>",
  "<b>20% of cases.</b> Exudative: <b>choroidal neovascularisation bleeds into the retina</b> and organises into a disciform scar. Rapid change on a background of dry disease.",
  "As for dry, plus <b>fluorescein angiography</b> and <b>optical coherence tomography</b>.",
  "<b>Intravitreal anti-VEGF injection</b>, thermal laser photocoagulation, photodynamic therapy.",
  "Same day",
  "A sharp change in central vision in known dry disease means <b>conversion to wet</b> until proven otherwise.",
  "11, 14", D13),

 ("Cataract &mdash; nuclear", CVL,
  "<b>Brown central lens</b> &middot; <b>distance worse than near</b> &middot; myopic shift",
  "Acquired, age-related. Central brown discoloration of the lens. <b>Blurs distance more than near &mdash; a myopic shift</b>, so some patients read without glasses again.",
  "Early: slit lamp. Advanced: <b>loss of the red reflex</b> on ophthalmoscopy.",
  "<b>Surgery is the only treatment</b> &mdash; lens extraction with implant, deferred until it interferes with daily activities.",
  "Routine",
  "<b>A cataract alone never causes a relative afferent pupillary defect.</b> If one is present, something else is going on.",
  "36&ndash;37", D13),

 ("Cataract &mdash; cortical", CVL,
  "<b>Spoke-like</b> peripheral opacities &middot; <b>GLARE</b> once central",
  "Radial spoke-like opacities from the lens periphery inward. <b>Asymptomatic until the opacity reaches the centre</b>, at which point <b>glare is the commonest complaint</b>.",
  "Slit lamp examination; red reflex dulled when advanced.",
  "Lens extraction when it interferes with function.",
  "Routine",
  "Glare in bright sun or from oncoming headlights that <b>was not there before</b> is the history that matters.",
  "36&ndash;37", D13),

 ("Cataract &mdash; posterior subcapsular", CVL,
  "<b>Under 50</b> &middot; <b>steroids or diabetes</b> &middot; <b>better after dilation</b>",
  "Plate-like opacity at the back of the lens. <b>Glare and trouble reading</b>, and characteristically <b>symptoms improve once dilated</b>. <b>More rapid onset, classically under 50 years old.</b>",
  "Slit lamp: a <b>dark shadow against the red reflex</b>.",
  "Lens extraction. Review the steroid burden where that is the cause.",
  "Routine",
  "The one to suspect in a younger patient <b>on corticosteroids or with diabetes</b>.",
  "36", D13),

 ("Cataract &mdash; pediatric", CVL,
  "<b>Zonular is commonest</b> &middot; <b>leukocoria</b> &middot; may have nystagmus",
  "<b>Zonular</b>: white opacity round the nucleus, the commonest paediatric type. <b>Polar</b>: less common but central, so caught earlier. Infants may be visually inattentive if bilateral; the affected eye may be smaller.",
  "<b>Red reflex screening</b> in every infant. Dim, disrupted or absent reflex, or frank <b>leukocoria</b>.",
  "<b>Surgery is NOT deferred in a neonate</b> &mdash; it is done early to prevent amblyopia.",
  "Emergent",
  "An absent red reflex in a newborn is <b>retinoblastoma or congenital cataract until proven otherwise</b>. Both need ophthalmology now.",
  "36, 38", D13),

 ("Myopia", REF,
  "<b>Long eyeball</b> &middot; distance blurred, near clear",
  "Excessive refractive power focuses distant objects <b>in front of the retina</b>. Family history and prolonged near work are risk factors; trauma displacing the lens forward can cause it.",
  "Refraction. Refer isolated refractive error to <b>optometry</b>.",
  "<b>Concave (negative dioptre) lens</b> &mdash; scatters light and moves focus back onto the retina.",
  "Routine",
  "Blur that <b>corrects fully with lenses</b> is refractive; blur that does not is not.",
  "18", D13),

 ("Hyperopia", REF,
  "<b>Short eyeball</b> &middot; near blurred",
  "Insufficient refractive power focuses distant objects <b>behind the retina</b>. Caused by anything shortening axial length &mdash; trauma displacing the lens backwards, or a mass behind the globe.",
  "Refraction, via optometry for isolated error.",
  "<b>Convex (positive dioptre) lens</b> &mdash; converges light forward onto the retina.",
  "Routine",
  "New hyperopia in an adult should prompt a thought about <b>mass effect behind the eye</b>.",
  "19", D13),

 ("Astigmatism", REF,
  "<b>Multiple focal points</b> &middot; blur at <b>every</b> distance",
  "Uneven curvature of cornea or lens means <b>no single point focus</b> forms on the retina. Risk factors largely unknown.",
  "Refraction.",
  "<b>Toric lens.</b>",
  "Routine",
  "Patients often assume everyone sees this way, because they always have.",
  "20", D13),

 ("Strabismus", CVL,
  "<b>Binocular</b> diplopia &mdash; <b>gone when either eye is covered</b>",
  "Misalignment from disorder of brain, cranial nerves, neuromuscular junction or the muscles themselves. One eye fails to track or fixate; <b>corneal light reflex displaced</b> in larger deviations.",
  "<b>Cover test</b> elicits fixation of the misaligned eye. Assess cranial nerves three, four and six.",
  "Treat the cause; ophthalmology referral. Untreated in a child it <b>causes amblyopia</b>.",
  "Urgent",
  "In an adult, <b>new</b> binocular diplopia needs a cause found. Pupil-involving third nerve palsy is an emergency.",
  "25, 29", D13),

 ("Amblyopia", CVL,
  "<b>Commonest cause of vision loss in children</b> &middot; unequal eyes",
  "The brain favours one eye and the other fails to develop. Three routes: <b>strabismus</b>, <b>anisometropia</b> (unequal refraction), and <b>deprivation</b> (cataract, ptosis, corneal opacity). Affects 3&ndash;5% of children.",
  "<b>Occlusion objection test</b> &mdash; the child objects when the GOOD eye is covered. Unilateral amblyopia is a <b>2-line or greater</b> difference in best corrected acuity. <b>Screen all children under 5.</b>",
  "<b>Patch or atropinise the GOOD eye</b> to force the weaker one to work. Treat the underlying cause.",
  "Urgent",
  "Outcome is good treated <b>before 7, better before 5</b>. Corrected late, acuity can recover but <b>stereo vision does not</b> &mdash; these patients struggle with 3D and with judging distance.",
  "30, 32&ndash;33", D13),

 ("Retinoblastoma", TUM,
  "<b>LEUKOCORIA</b> in a young child &middot; white pupil in photographs",
  "Rare, almost exclusively young children, from a genetic mutation that is often recessive and so easily missed on family history. May present with poor vision or a turned eye.",
  "<b>Dilated examination plus imaging. NO BIOPSY &mdash; it risks seeding the tumour.</b> Primary care contribution is the <b>red reflex</b> at every well-child check.",
  "Multimodal therapy under ocular oncology, with genetic counselling. Enucleation for large tumours.",
  "Emergent",
  "<b>Untreated it is close to 100% fatal; treated, five-year survival is over 95%.</b> No recurrence at five years counts as <b>cured</b>. Known family history: seen by an experienced ophthalmologist <b>within the first 8 weeks of life</b>.",
  "41&ndash;42", D13),

 ("Uveal melanoma", TUM,
  "<b>Commonest eye cancer in adults</b> &middot; <b>feeder vessel</b> &middot; usually found incidentally",
  "From melanocytes of the <b>choroid, ciliary body or iris</b> &mdash; distinct from cutaneous and from conjunctival melanoma. Iris lesions: slow-growing dark or translucent mass, <b>inferior half</b>, unilateral, <b>&gt;3 mm base and &gt;1 mm deep</b>, may distort the pupil (corectopia).",
  "Ophthalmology, then ocular oncology. <b>Fine needle aspiration is for molecular prognostic testing, not to make the diagnosis.</b>",
  "<b>Radiation therapy</b> is now the commonest treatment; enucleation is less often needed.",
  "Urgent",
  "<b>The liver is the commonest site of metastasis.</b> Ten-year mortality about 32% overall, but <b>iris melanoma only 4&ndash;10%</b> &mdash; it is visible, so it is found earlier.",
  "44&ndash;46", D13),

 ("Iris nevus", TUM,
  "<b>Flat</b>, &lt;3 mm, <b>avascular</b> &middot; inferior iris &middot; stable",
  "A freckle of the iris, usually apparent around puberty. Asymptomatic, typically does not grow, flat or minimally elevated, <b>not vascular</b>. May distort the pupil.",
  "Refer to ophthalmology to document and monitor; <b>melanoma has to be excluded</b>.",
  "Surveillance. More frequent initially to establish it is not growing, then annual dilated review.",
  "Routine",
  "<b>The discriminators are growth, size and its own blood supply.</b> A freckle has no feeder vessel; a cancer builds one.",
  "48&ndash;49", D13),

 ("Conjunctival melanoma", TUM,
  "<b>Raised and vascular</b> pigmented conjunctival lesion",
  "Distinct from uveal melanoma. A raised, often vascular pigmented lesion, in contrast to a <b>conjunctival nevus</b>, which is flat and characteristically contains <b>clear cysts</b>.",
  "Ophthalmology referral for any pigmented conjunctival lesion that is <b>growing</b>.",
  "Specialist management under ocular oncology.",
  "Urgent",
  "Differentials include <b>primary acquired melanosis</b> (flat, patchy, can be premalignant) and <b>racial melanosis</b> (bilateral and symmetric).",
  "52&ndash;54", D13),
]

DIFF_L13 = {
 "Idiopathic intracranial hypertension": ("<b>YES</b> &mdash; headache, pain behind the eyes", "<b>BILATERAL</b> papilledema",
   "<b>Papilledema</b> with visual field loss; <b>sixth nerve palsy</b>"),
 "Age-related macular degeneration &mdash; dry": ("<b>NO</b>", "Often bilateral",
   "<b>Drusen</b>, pigmentary change and atrophy; <b>central scotoma</b>"),
 "Age-related macular degeneration &mdash; wet": ("<b>NO</b>", "May start unilateral",
   "<b>Choroidal neovascularisation</b> with haemorrhage, then a disciform scar"),
 "Cataract &mdash; nuclear": ("<b>NO</b>", "Usually bilateral",
   "<b>Brown central lens</b>; <b>myopic shift</b>, distance worse than near"),
 "Cataract &mdash; cortical": ("<b>NO</b>", "Usually bilateral",
   "<b>Spoke-like</b> peripheral opacities; <b>glare</b> once central"),
 "Cataract &mdash; posterior subcapsular": ("<b>NO</b>", "May be unilateral",
   "Plate-like posterior opacity; <b>better after dilation</b>; <b>under 50</b>"),
 "Cataract &mdash; pediatric": ("<b>NO</b>", "Uni- or bilateral",
   "<b>Leukocoria</b> or an absent red reflex; <b>zonular</b> is commonest"),
 "Myopia": ("<b>NO</b>", "Usually bilateral", "Distance blur that <b>corrects with a concave lens</b>"),
 "Hyperopia": ("<b>NO</b>", "Usually bilateral", "Near blur that <b>corrects with a convex lens</b>"),
 "Astigmatism": ("<b>NO</b>", "Usually bilateral", "Blur at <b>all</b> distances; <b>toric lens</b> corrects"),
 "Strabismus": ("<b>NO</b> in itself", "One eye misaligned",
   "<b>Cover test</b> positive; displaced <b>corneal light reflex</b>"),
 "Amblyopia": ("<b>NO</b>", "Usually unilateral",
   "<b>2-line or greater</b> acuity difference; <b>objects when the GOOD eye is covered</b>"),
 "Retinoblastoma": ("<b>NO</b>", "Uni- or bilateral", "<b>LEUKOCORIA</b> &mdash; white pupillary reflex"),
 "Uveal melanoma": ("<b>NO</b> &mdash; usually asymptomatic", "Unilateral",
   "Pigmented mass with a <b>PROMINENT FEEDER VESSEL</b>; <b>&gt;3 mm</b>"),
 "Iris nevus": ("<b>NO</b>", "Usually unilateral", "<b>Flat, &lt;3 mm, avascular</b>, inferior iris"),
 "Conjunctival melanoma": ("<b>NO</b>", "Unilateral", "<b>Raised and vascular</b>; a nevus is flat with cysts"),
}

# Resolved by label geometry, never by extraction order. See _cms_e2_l13_figures.
IMGS_L13 = {
 "Age-related macular degeneration &mdash; dry": ("l13-s011_1.jpg", 11),   # label A, soft drusen
 "Age-related macular degeneration &mdash; wet": ("l13-s011_3.jpg", 11),   # label C, CNV haemorrhage
 "Cataract &mdash; nuclear": ("l13-s037_1.jpg", 37),                        # ABOVE
 "Cataract &mdash; cortical": ("l13-s037_2.jpg", 37),                       # BELOW
 "Cataract &mdash; pediatric": ("l13-s038_2.jpg", 38),                      # ABOVE, polar
 "Amblyopia": ("l13-s032_1.jpg", 32),
 "Retinoblastoma": ("l13-s041_1.jpg", 41),
 "Uveal melanoma": ("l13-s044_4.jpg", 44),                                  # label C, choroidal
 "Iris nevus": ("l13-s048_1.jpg", 48),                                      # label B, pigmented nevus
 "Conjunctival melanoma": ("l13-s052_1.jpg", 52),                           # ABOVE, melanoma
}
