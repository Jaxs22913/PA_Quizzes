#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the CMS I Exam 2 Ophthalmology Comparison Chart.

The Exam 2 counterpart to the Exam 1 dermatology chart: every condition in the
ophthalmology block in one sortable table, read left to right.

IMAGES ARE USED AND CITED, per the standing rule in [[media_asset_licensing]]:
any image in a course PowerPoint may be used as long as the slide is cited.
Several of this deck's photographs carry marks baked into the pixels --
EYEROUNDS.ORG, the University of Michigan Kellogg Eye Center, "(c) 2011 Logical
Images, Inc." -- and those are LEFT VISIBLE on purpose. They ride along as part
of citing the slide. Every picture cell prints its slide number.

EVERY IMAGE WAS VIEWED BEFORE BEING ASSIGNED. This deck labels several pictures
"DDX" in its own captions, and two would have been outright factual errors in a
chart cell:
  * slide 29 image 1 is a HYPHAEMA, captioned as a differential -- not the
    subconjunctival haemorrhage that row is about
  * slide 27 image 3 is CONJUNCTIVAL INTRAEPITHELIAL NEOPLASIA, the fan-shaped
    differential -- not the pterygium
Both are in REJECTED below and the exclusion is asserted, so a later edit
cannot quietly reintroduce them.

THE ONE DIFFERENCE FROM THE DERM CHART IS A REFERRAL URGENCY COLUMN. In dermatology the useful axis was first-line
   against second-line treatment. In ophthalmology the decision that actually
   changes an outcome is how fast the patient is seen, and the deck ends with
   an explicit emergent / same-day / urgent / routine table. That column is the
   one to read down when a stem is in front of you.

The gold "Vignette giveaway" column is kept, and for the same reason: Prof.
Jaquith described this exam as "pretty much all clinical vignettes ... recognize
conditions by the vignette", and a vignette gives itself away in a handful of
words. Every phrase there is language the DECK itself uses.
"""
import os, re, sys, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
DONOR = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 1/cms-derm-comparison-chart.html")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 2/cms-ophtho-comparison-chart.html")

# Downscaled to 600 px wide and re-encoded as JPEG at quality 80. The chart
# displays them at 180 px, so this is well above what the page needs, and
# it takes the folder from 4.7 MB to 1.7 MB -- comparable, per image, with
# the derm chart's 153.
# HER OWN CHART INSTRUCTION, from the end of the 26 August lecture:
#   "My recommendation to you guys for those is again use your resources, MAKE A
#    CHART -- which ones cause PAIN, which ones don't cause pain. Which ones are
#    UNILATERAL, which ones are BILATERAL. Which ones will cause which PHYSICAL
#    EXAM ABNORMALITIES, like FIXED PUPILS for example. That's how you're gonna
#    differentiate these ... That's definitely gonna be on your exam. AT LEAST
#    TWO QUESTIONS MINIMUM."
# So those three are their own columns, placed immediately after the name, and
# the filter row lets you pull out just the painful ones or just the bilateral
# ones -- which is the comparison she actually asked for.
from cms_e2_ophtho_diff import DIFF, classify
# Lectures 11 and 12 were added on 2026-08-29. Their rows carry a tenth
# field naming the deck, because with three decks in this exam a bare
# slide number no longer identifies anything on its own.
from _cms_e2_chart_l1112 import ROWS_NEW, DIFF_NEW, IMGS_NEW
from _cms_e2_chart_l13 import ROWS_L13, DIFF_L13, IMGS_L13
# Lecture 14 (Ocular Trauma) added 2026-09-01. Its images are named by their
# READING-ORDER POSITION on the slide, not by relationship order, because this
# deck labels pictures positionally in notes that themselves do not map to
# slides by index -- see _cms_e2_chart_l14.py.
from _cms_e2_chart_l14 import ROWS_L14, DIFF_L14, IMGS_L14
DIFF = dict(DIFF, **DIFF_NEW)
DIFF = dict(DIFF, **DIFF_L13)
DIFF = dict(DIFF, **DIFF_L14)
IMGS = {'Entropion': ('s012_1.jpg', 12), 'Ectropion': ('s012_2.jpg', 12), 'Dermatochalasis': ('s014_1.jpg', 14), 'Xanthelasma': ('s016_1.jpg', 16), 'Blepharitis / Meibomitis': ('s018_1.jpg', 18), 'Chalazion': ('s020_5.jpg', 20), 'Hordeolum (stye)': ('s020_1.jpg', 20), 'Dacryoadenitis': ('s022_1.jpg', 22), 'Dacryocystitis': ('s024_1.jpg', 24), 'Pinguecula': ('s027_1.jpg', 27), 'Pterygium': ('s027_2.jpg', 27), 'Subconjunctival haemorrhage': ('s029_2.jpg', 29), 'Chemosis': ('s031_1.jpg', 31), 'Allergic conjunctivitis': ('s034_1.jpg', 34), 'Viral conjunctivitis': ('s036_1.jpg', 36), 'Bacterial conjunctivitis': ('s040_1.jpg', 40), 'Chlamydial conjunctivitis &mdash; adult inclusion': ('s042_1.jpg', 42), 'Episcleritis': ('s047_2.jpg', 47), 'Scleritis': ('s049_1.jpg', 49), 'Pre-septal (periorbital) cellulitis': ('s052_1.jpg', 52), 'Post-septal (orbital) cellulitis': ('s052_2.jpg', 52), 'Keratitis': ('s055_2.jpg', 55), 'Herpes simplex keratitis': ('s057_1.jpg', 57), 'Herpes zoster keratitis': ('s057_2.jpg', 57), 'Corneal ulcer': ('s060_1.jpg', 60), 'Anterior uveitis (iritis, iridocyclitis)': ('s062_4.jpg', 62), 'Posterior uveitis (choroiditis, retinitis)': ('s064_1.jpg', 64)}

# Viewed and REJECTED. These are the deck's OWN differential images -- filing
# one under the row's condition would be a factual error in the chart, not
# merely an ugly picture. See [[image_only_slides]].
REJECTED = {
  "s029_1.jpg": "a HYPHAEMA, captioned DDX on slide 29 -- not a subconjunctival haemorrhage",
  "s027_3.jpg": "CONJUNCTIVAL INTRAEPITHELIAL NEOPLASIA, the fan-shaped DDX on slide 27 -- not a pterygium",
}

# name, group, giveaway, presentation, testing, treatment, urgency, education, slides
ROWS = [
 ("Entropion", "Eyelid",
  "Lower lid margin turns IN &middot; &ldquo;foreign body sensation&rdquo; &middot; lashes touching the globe",
  "Foreign body sensation with conjunctival injection. Inward-turning lid margin with lashes pushed onto the globe (trichiasis).",
  "Slit lamp examination &mdash; the question is always whether the CORNEA has been involved.",
  "Preservative-free artificial tears by day, lubricating ointment at night, tape the exposed lid. <b>Surgery is definitive.</b>",
  "Routine", "The drops protect the surface; only surgery repositions the lid.", "12&ndash;13"),
 ("Ectropion", "Eyelid",
  "Lower lid margin turns OUT &middot; &ldquo;tearing&rdquo; &middot; inner lid surface visible",
  "Tearing with conjunctival injection. Outward-turning lid margin exposing the inner surface.",
  "Slit lamp examination for exposure keratopathy.",
  "Same as entropion: tears by day, ointment at night, taping. <b>Surgery is definitive.</b>",
  "Routine",
  "Ageing, scarring, congenital &mdash; and <b>seventh nerve palsy causes ectropion only</b>.", "12&ndash;13"),
 ("Dermatochalasis", "Eyelid",
  "&ldquo;Heaviness&rdquo; of the lids &middot; &ldquo;looking through my lashes&rdquo; &middot; friction on blinking",
  "Excess flaps or folds of skin, bilaterally. From ageing.",
  "<b>Examine the visual fields</b> &mdash; a demonstrated deficit is what gets surgery covered.",
  "Blepharoplasty.",
  "Routine",
  "Often covered by insurance <i>if a visual field defect is present</i>.", "14&ndash;15"),
 ("Xanthelasma", "Eyelid",
  "Oval <b>yellowish plaques</b> &middot; typically asymptomatic &middot; usually bilateral",
  "Oval yellowish plaques on the lids. Asymptomatic.",
  "Serum lipid profile, plus fasting glucose and haemoglobin A1C, plus liver function tests.",
  "<b>Treat the underlying metabolic issue.</b> Local: cryotherapy, laser ablation, chemical peel, surgical excision.",
  "Routine",
  "<b>Recurrences are common</b> even after effective local treatment. Many patients have normal lipids &mdash; the profile is still reasonable.", "16&ndash;17"),
 ("Blepharitis / Meibomitis", "Eyelid",
  "<b>Crusting and scaling at the LASH BASES</b> &middot; <b>toothpaste-like</b> meibomian secretion &middot; frothy tear film",
  "Burning, dryness, grittiness, itching, foreign body sensation, tearing, mild redness. Erythematous swollen lid margins; decreased or frothy tear film. Skin findings of rosacea or seborrhoeic dermatitis.",
  "Clinical. Associations: <b>rosacea, seborrhoeic dermatitis, Staphylococcus aureus</b>.",
  "<b>Lid hygiene first.</b> No better after <b>2 weeks</b> &rarr; topical antibiotics &rarr; then oral.",
  "Routine",
  "<b>Chronic &mdash; controlled rather than cured.</b> Refer to ophthalmology if several weeks of treatment fail.", "18&ndash;19"),
 ("Chalazion", "Eyelid",
  "<b>NON-tender</b> lid nodule &middot; builds over <b>days to weeks</b> &middot; points INSIDE the lid",
  "Focal eyelid swelling over days to weeks. Visible or palpable subcutaneous nodule, <b>not tender</b>.",
  "Clinical. It is a <b>STERILE obstruction</b> of a meibomian gland.",
  "Warm compresses with gentle massage. No spontaneous resolution &rarr; ophthalmology for <b>steroid injection or curettage</b>.",
  "Routine",
  "<b>Improvement may take months.</b> Recurrent, or persisting beyond 2&ndash;3 months &rarr; refer to <b>rule out sebaceous carcinoma</b>.", "20&ndash;21"),
 ("Hordeolum (stye)", "Eyelid",
  "<b>TENDER</b> lid nodule &middot; appears in <b>24 hours or overnight</b> &middot; at the lid margin",
  "Eyelid pain, redness and swelling over 24 hours. Tender subcutaneous nodule.",
  "Clinical. Acute infection, usually <b>staphylococcal</b> &mdash; meibomian gland (internal) or glands of Zeis or Moll (external).",
  "Warm compresses with gentle massage. Persistent (no improvement in <b>2 weeks</b>) &rarr; ophthalmology for incision and drainage.",
  "Routine",
  "If pre-septal cellulitis develops alongside it, treat on the <b>cellulitis</b> pathway with systemic antibiotics.", "20&ndash;21"),
 ("Dacryoadenitis", "Lacrimal",
  "Swelling over the <b>LATERAL ONE THIRD of the UPPER lid</b> &middot; ipsilateral preauricular node",
  "Unilateral pain, redness and swelling over the outer upper lid; tearing or discharge. Hyperaemic palpebral lobe of the lacrimal gland. May have preauricular lymphadenopathy, temporal injection, fever, leukocytosis.",
  "Contrast computed tomography of orbits and sinuses <b>when indicated</b> &mdash; not automatic. <b>Inflammatory is most common</b>; bacterial rare; viral usually bilateral.",
  "Inflammatory &rarr; <b>corticosteroids</b>. Viral &rarr; cool compresses. Cause unclear &rarr; empiric oral antibiotics 24 h then reassess. Analgesia as needed.",
  "Urgent",
  "<b>Do not start corticosteroids until infection is reasonably excluded.</b> Inflammatory disease should respond within <b>48 hours</b>. Monitor for orbital involvement.", "22&ndash;23"),
 ("Dacryocystitis", "Lacrimal",
  "Swelling over the <b>NASAL aspect of the LOWER lid</b>, BELOW the medial canthal tendon &middot; pus from the punctum",
  "Red, painful, swollen mound over the lacrimal sac at the inner lower lid; tearing, fever. Erythematous tender tense swelling. <b>Mucoid or purulent discharge expressible from the lower punctum.</b>",
  "From <b>nasolacrimal duct obstruction</b>. Contrast computed tomography reserved for suspected orbital extension, abscess, trauma, mass or atypical disease.",
  "Well, afebrile, reliable &rarr; <b>oral antibiotics 10 days</b>. Febrile, ill or unreliable &rarr; <b>admit, intravenous 48&ndash;72 h</b> then oral to complete 10&ndash;14 days. Warm compresses; consider drainage of an abscess.",
  "Urgent",
  "Improvement expected in <b>24&ndash;48 hours</b>. Afterwards, <b>probing and irrigation</b> are often needed to check the drainage system; surgery may follow. A mass <b>ABOVE</b> the tendon suggests a lacrimal sac tumour.", "24&ndash;25"),
 ("Pinguecula", "Surface",
  "Yellowish nodule at <b>3 or 9 o&rsquo;clock</b> &middot; <b>does NOT touch the cornea</b>",
  "Irritation, redness nasally or temporally, tearing. Classic appearance, almost always at 3 or 9 o&rsquo;clock, <b>not involving the cornea</b>.",
  "Clinical. From chronic <b>sunlight and wind</b> exposure.",
  "Sun, dust and wind protection; lubricating drops.",
  "Routine",
  "<b>Conservative management will not make it resolve.</b> &ldquo;Pterodactyls fly into the cornea; penguins can&rsquo;t.&rdquo;", "27&ndash;28"),
 ("Pterygium", "Surface",
  "Triangular <b>insect-wing</b> growth &middot; <b>EXTENDS ONTO THE CORNEA</b> &middot; &ldquo;surfer&rsquo;s eye&rdquo;",
  "As pinguecula, but the growth crosses the limbus onto the cornea. Can decrease vision.",
  "Slit lamp to assess the integrity of the adjacent cornea.",
  "Sun protection and lubricating drops. <b>Surgery if it grows into the cornea and distorts vision.</b>",
  "Routine &mdash; refer non-urgently if <b>growing</b> or <b>vision affected</b>",
  "Conservative care controls symptoms only. Protect from sun, dust and wind.", "27&ndash;28"),
 ("Subconjunctival haemorrhage", "Surface",
  "<b>Bright red patch, PAINLESS</b> &middot; vision, pupil and cornea all normal &middot; after a cough or strain",
  "Red eye, often asymptomatic unless chemosis is present. Blood underneath the conjunctiva.",
  "<b>History is the workup.</b> <b>Check the blood pressure if there is no explanation.</b> Ocular examination.",
  "Reassurance. Artificial tears if mildly irritated. Treat the underlying bleeding disorder or hypertension.",
  "Routine",
  "Resolves spontaneously in <b>2&ndash;4 weeks</b>. Recurrent with no culprit medication &rarr; medication review, blood pressure, targeted haematologic evaluation &mdash; not an automatic referral.", "29&ndash;30"),
 ("Chemosis", "Surface",
  "<b>Swelling of the conjunctiva itself</b> &middot; a sign, not a diagnosis",
  "Conjunctival oedema. Non-specific sign of irritation: allergy, infection, thyroid eye disease, angioedema, trauma, orbital cellulitis, impaired orbital venous drainage.",
  "Look for what is causing it.",
  "Treat the cause.",
  "<b>URGENT</b> if with proptosis, restricted movement, reduced vision or an afferent pupillary defect",
  "On its own it means irritation. With those four accompaniments it means something is filling the orbit.", "31"),
 ("Allergic conjunctivitis", "Conjunctivitis",
  "<b>ITCH</b> &middot; bilateral &middot; watery or <b>stringy</b> discharge &middot; <b>no preauricular node</b>",
  "Diffuse hyperaemia, itchy eyes, swollen lids, watery or stringy discharge. Bilateral. <b>Vision preserved.</b> Chemosis, conjunctival <b>papillae</b>, no node.",
  "Clinical. <b>Papillae</b> (red at surface, paler at base) &rarr; bacterial or allergic.",
  "Avoid the allergen; cool compresses, artificial tears, topical histamine blocker &plusmn; mast cell stabiliser (<b>olopatadine does both</b>), systemic antihistamine.",
  "Routine",
  "Symptoms often settle as allergen levels fall. If topical treatment fails, the diagnosis may be wrong &mdash; refer.", "34&ndash;35"),
 ("Viral conjunctivitis", "Conjunctivitis",
  "<b>Profuse WATERY discharge</b> &middot; <b>FOLLICLES</b> &middot; <b>TENDER preauricular node</b> &middot; one eye then the other &middot; recent cold",
  "Diffusely red conjunctiva, considerable tearing, swollen tight lids but <b>no pain</b>. Bilateral, often starting in one eye. Follicles especially inferiorly.",
  "Clinical. <b>Follicles</b> (pale at surface, redder at base) &rarr; chlamydial or viral.",
  "Cool compresses, artificial tears. <b>Contagious precautions and hand hygiene.</b>",
  "Routine &mdash; refer if &gt;3 weeks, or photophobia or vision loss after onset",
  "<b>Self-limiting, but often WORSE over the first week</b>, resolving in 2&ndash;3 weeks. Highly contagious.", "36&ndash;37"),
 ("Bacterial conjunctivitis", "Conjunctivitis",
  "<b>Thick yellow or white discharge</b> &middot; often <b>UNILATERAL</b> &middot; lids stuck together &middot; usually no node",
  "Diffusely red conjunctiva, thick discharge, soreness. Florid hyperaemia and chemosis, <b>papillae</b>, mild to moderate purulent discharge.",
  "Clinical. Risk: immunocompromised, elderly, paediatric, <b>contact lens wearers</b>.",
  "Immunocompetent adult &rarr; <b>topical broad-spectrum antibiotic</b> (e.g. fluoroquinolone). Contagious precautions.",
  "Routine &mdash; <b>URGENT</b> if immunocompromised, contact lens wearer, recent surgery, foreign body, corneal opacity, or <b>no improvement in 24 h</b>",
  "Prompt and total response is expected in a normal host. Poor response &rarr; refer.", "40&ndash;41"),
 ("Gonococcal conjunctivitis", "Conjunctivitis",
  "<b>SEVERE purulent discharge WITH a palpable preauricular node</b> &middot; <b>neonate</b>",
  "The exception to the no-node rule in bacterial disease. In neonates, the major concern.",
  "Cultures and Gram stain; test for chlamydia and disseminated infection.",
  "<b>Newborn: hospitalise, systemic ceftriaxone once, specialty consultation.</b>",
  "<b>EMERGENT</b>",
  "<b>Untreated risk is corneal perforation.</b>", "40&ndash;41"),
 ("Chlamydial conjunctivitis &mdash; adult inclusion", "Conjunctivitis",
  "<b>CHRONIC &mdash; a month or more</b> &middot; stringy mucoid discharge &middot; <b>follicles</b> &middot; <b>has not responded to topical medication</b>",
  "Chronic hyperaemia of the lower palpebral conjunctiva. Unilateral, sometimes bilateral. Often a concurrent asymptomatic urogenital infection.",
  "<b>Conjunctival nucleic acid amplification testing</b>, or direct fluorescent antibody stain of a scraping. Serotypes <b>D&ndash;K</b>.",
  "<b>Doxycycline 100 mg orally twice daily for 7 days.</b>",
  "Routine",
  "Avoid the sun; full glass of water, stay upright, separate from antacids and iron, calcium or magnesium. <b>Evaluate for other sexually transmitted infections and notify partners.</b>", "42&ndash;43"),
 ("Chlamydial conjunctivitis &mdash; neonatal", "Conjunctivitis",
  "Neonate &middot; maternal cervical infection &middot; may also have <b>pneumonia</b>",
  "Direct inoculation with infected genital secretions. Serotypes D&ndash;K.",
  "As above. Assess for pneumonia.",
  "<b>Erythromycin 50 mg/kg/day divided four times daily for 14 days.</b> Azithromycin 20 mg/kg daily for 3 days is an alternative with more limited data.",
  "Urgent",
  "<b>Monitor infants under 6 weeks for infantile hypertrophic pyloric stenosis</b> &mdash; erythromycin is a motilin receptor agonist. Often treated in hospital because of concomitant pneumonia.", "44"),
 ("Trachoma", "Conjunctivitis",
  "Poor sanitation &middot; <b>repeated childhood infections</b> &middot; scarred upper lid &middot; <b>lashes turned in</b>",
  "Most active cases are <b>asymptomatic</b>. If symptomatic: red eye, foreign body sensation, purulent discharge, follicles especially of the upper eyelid.",
  "Serotypes <b>A, B, C</b>. <b>The leading infectious cause of blindness worldwide.</b>",
  "Mass drug administration: <b>azithromycin 1 g orally as a single dose</b> where prevalence is <b>&ge;5%</b>. <b>Trichiasis requires surgery.</b>",
  "Urgent",
  "Treatment is usually curative but reinfection is common without better hygiene. Chain: <b>inflammation &rarr; lid scarring &rarr; entropion &rarr; trichiasis &rarr; blindness</b>.", "45&ndash;46"),
 ("Autoimmune conjunctivitis", "Conjunctivitis",
  "Recurrent or chronic redness &middot; <b>minimal pain, NO discharge</b> &middot; systemic complaints",
  "Diffuse hyperaemia, often recurrent. Malaise, fever, fatigue. Systemic autoimmune disease usually already identified.",
  "Associated with ocular mucous membrane pemphigoid, Stevens-Johnson syndrome, Sj&ouml;gren disease, graft-versus-host disease.",
  "Managed by ophthalmology alongside the systemic disease.",
  "Routine",
  "Ocular response depends on the underlying disorder.", "38&ndash;39"),
 ("Episcleritis", "Sclera",
  "<b>MILD</b> ache &middot; <b>sectoral</b> redness &middot; <b>no discharge, no photophobia</b> &middot; vessels MOVE",
  "Acute-onset mild pain and focal redness. Often sectoral. Episcleral vessels can be moved slightly with a cotton-tip applicator after anaesthesia.",
  "<b>2.5% phenylephrine, wait 15 minutes &mdash; the vessels BLANCH.</b> Often idiopathic, often no systemic association.",
  "Artificial tears and an <b>oral non-steroidal anti-inflammatory taken WITH FOOD</b>.",
  "Routine &mdash; refer if <b>no response in 2 days</b>",
  "Usually self-limited, resolving over 2&ndash;3 weeks. May recur in the same or the other eye.", "47&ndash;48"),
 ("Scleritis", "Sclera",
  "<b>SEVERE BORING pain, WORSE AT NIGHT</b>, radiating to the face &middot; <b>VIOLACEOUS hue</b> &middot; vessels do NOT move",
  "Severe deep pain radiating to face and periorbital region, often with diffuse hyperaemia. Characteristic violaceous hue &mdash; <b>choroid showing through thinned sclera</b>. Pain with eye movement.",
  "Slit lamp and ophthalmoscopy. <b>Work up the underlying systemic condition</b> &mdash; often autoimmune.",
  "Non-infectious anterior disease commonly <b>begins with systemic anti-inflammatories</b>; systemic corticosteroids and immunomodulators for severe, necrotising, posterior or refractory disease.",
  "<b>SAME DAY</b> &mdash; sclera at risk of perforation, may need a surgical patch",
  "<b>Decreased PAIN is the first sign of response</b>, even if the inflammation looks unchanged. Perforation risk is greatest in <b>necrotising</b> disease.", "49&ndash;50"),
 ("Pre-septal (periorbital) cellulitis", "Orbit",
  "Swollen red lid <b>but THE EYE ITSELF IS WHITE</b> &middot; movements full and painless &middot; vision normal",
  "Periocular pain, fever, chills, warmth. Diffuse balloon-like oedema, erythema and tenderness of lids and periorbital tissue; variable conjunctival injection.",
  "Direct extension from bacterial sinus, skin or dental infection. Contrast computed tomography <b>when orbital involvement cannot be excluded</b> &mdash; not automatic in clearly pre-septal disease. Complete blood count, blood cultures, wound Gram stain.",
  "Mild &rarr; <b>outpatient oral antibiotics 10&ndash;14 days</b> against Staphylococcus (including resistant strains) and Streptococcus.",
  "Urgent &mdash; <b>admit</b> if moderate-severe or toxic, poor compliance, <b>child &le;5 years</b>, or no improvement on orals",
  "Expect improvement in <b>24&ndash;48 hours</b>. In diabetic, elderly or immunocompromised patients consider <b>fungus</b>.", "51&ndash;53"),
 ("Post-septal (orbital) cellulitis", "Orbit",
  "<b>THE EYE ITSELF IS RED</b> &middot; <b>PROPTOSIS</b> &middot; <b>painful restricted eye movement</b> &middot; diplopia &middot; reduced vision",
  "All the pre-septal features plus significant conjunctival injection, proptosis, decreased and painful extraocular movement, possible afferent pupillary defect and decreased vision.",
  "<b>Contrast computed tomography of orbits and paranasal sinuses.</b> Complete ocular examination with fundoscopy, cultures, complete blood count, blood cultures.",
  "<b>Hospitalise &mdash; broad-spectrum intravenous antibiotics 48&ndash;72 h</b>, then oral for at least a week. May need ear-nose-throat, oral and maxillofacial surgery, or infectious disease consults.",
  "<b>EMERGENT</b>",
  "<b>Untreated &rarr; intracranial spread &rarr; meningitis or cavernous sinus thrombosis.</b>", "51&ndash;53"),
 ("Keratitis", "Cornea",
  "<b>Contact lens overwear</b> &middot; <b>corneal opacification</b> &middot; &ldquo;broken up&rdquo; corneal light reflection &middot; <b>CILIARY FLUSH</b>",
  "Eye pain, foreign body sensation, tearing, photophobia, redness especially at the corneal edge, blurred vision. Opacification of the cornea.",
  "Slit lamp with fluorescein. Risks: corneal trauma, dry eyes, contact lens overwear, topical ocular corticosteroids. <b>Classic ring infiltrate = Acanthamoeba</b>, in lens wearers who rinse lenses in tap water.",
  "Treat the underlying cause to prevent persistent inflammation and scarring, guided by ophthalmology.",
  "<b>SAME DAY</b> &mdash; urgent referral within 24 h",
  "<b>Undertreated &rarr; corneal scarring or perforation &rarr; endophthalmitis &rarr; possible removal of the eye.</b> Prognosis is worse for ulcers <b>inside the visual axis</b>.", "54&ndash;56"),
 ("Herpes simplex keratitis", "Cornea",
  "<b>TRUE DENDRITE</b> &mdash; tree-branching, elevated edges, <b>TERMINAL END BULBS</b> &middot; younger patient &middot; rash not dermatomal",
  "Painful red eye with photophobia. Fluorescein under cobalt blue shows the classic dendrite. Facial vesicles lack a dermatomal distribution and may not respect the midline.",
  "Fluorescein staining. <b>The true dendrite is pathognomonic for herpes simplex.</b>",
  "<b>Oral antivirals</b> (aciclovir, valaciclovir, famciclovir) for <b>10 days</b>.",
  "<b>SAME DAY</b>",
  "<b>NO TOPICAL GLUCOCORTICOIDS BY THE PRIMARY PROVIDER in active epithelial disease.</b> Benign and self-limited, but recurrences are common under physical or emotional stress.", "57&ndash;59"),
 ("Herpes zoster keratitis", "Cornea",
  "<b>PSEUDOdendrite</b> &mdash; no branch pattern, no elevated edges, <b>no end bulbs</b> &middot; older patient &middot; <b>dermatomal V1 rash respecting the midline</b>",
  "Pain, paraesthesia or discomfort in the affected skin, possibly preceded by headache, fever, malaise. Vesicles characteristically unilateral, often sparing the lower lid. Rash may precede ocular involvement by days to months.",
  "Fluorescein staining. <b>Hutchinson sign</b> &mdash; vesicle on the tip of the nose &rarr; nasociliary involvement &rarr; higher ocular risk.",
  "<b>Oral antivirals for 10 days</b>, ideally within <b>72 hours</b> of rash onset. Intravenous aciclovir for severe, disseminated, orbital, retinal, central nervous system or significantly immunocompromised disease.",
  "<b>SAME DAY</b>",
  "Recurrences common; <b>postherpetic neuralgia can be devastating</b>. Prevention: recombinant zoster vaccine at 50+, and 19+ if immunocompromised.", "57&ndash;59"),
 ("Corneal ulcer", "Cornea",
  "<b>Patient RESISTS OPENING the eye</b> &middot; <b>white spot on the cornea</b> &middot; contact lens wearer &middot; ciliary flush",
  "Painful eye, reluctance to open it from photophobia or foreign body sensation, tearing, blurred vision, red eye. Corneal defect.",
  "Slit lamp and fluorescein. <b>Swab central or large ulcers for culture.</b> <b>Contact lens use is the major risk factor.</b>",
  "<b>Broad-spectrum topical agent</b> (fourth-generation fluoroquinolone) to start; then agent-specific therapy per ophthalmology.",
  "<b>EMERGENT</b>",
  "<b>Steroid drops can worsen the infection if started too early</b>, especially fungal or herpetic &mdash; leave that decision to ophthalmology. Next-day follow-up; most heal in 2&ndash;3 weeks; may need a transplant if severe.", "60&ndash;61"),
 ("Anterior uveitis (iritis, iridocyclitis)", "Uvea",
  "<b>CONSENSUAL photophobia</b> &middot; <b>ciliary flush</b> &middot; <b>irregular pupil</b> stuck to lens or cornea &middot; <b>cells in the anterior chamber</b>",
  "Eye pain, redness especially at the corneal edge, photophobia. <b>Vision often preserved.</b> Variable pressure. <b>Keratic precipitates</b> &mdash; white cell deposits on the corneal endothelium.",
  "Slit lamp and dilated fundoscopy. Idiopathic or autoimmune.",
  "Infectious &rarr; treat the organism. Non-infectious &rarr; <b>topical corticosteroids</b>.",
  "<b>SAME DAY</b> &mdash; urgent within 24 h, because delay may cost vision",
  "Most acute cases respond dramatically within days to weeks. <b>Recurrent disease, or systemic features, needs a thorough systemic evaluation.</b>", "62&ndash;63"),
 ("Posterior uveitis (choroiditis, retinitis)", "Uvea",
  "<b>NO PAIN</b> &middot; floaters, scotomas, <b>metamorphopsia</b> &middot; <b>cells in the posterior vitreous</b> &middot; vitreous haze",
  "Blurred vision, floaters, scotomas, distortion of straight lines. No pain if isolated. Inflammation of retina or choroid.",
  "Slit lamp and dilated fundoscopy; possibly <b>fluorescein angiography</b> to separate active from inactive lesions. Idiopathic, autoimmune, or infectious &mdash; <b>toxoplasmosis, cytomegalovirus</b>.",
  "<b>Does NOT respond to topical treatment</b> &mdash; may require an <b>intraocular corticosteroid injection</b>.",
  "Urgent",
  "Develops far more slowly than anterior disease and may last several years. <b>Infection must be excluded before immunosuppression.</b>", "64&ndash;65"),
]

ROWS = ROWS + ROWS_NEW + ROWS_L13 + ROWS_L14
IMGS = dict(IMGS, **IMGS_NEW)
IMGS = dict(IMGS, **IMGS_L13)
IMGS = dict(IMGS, **IMGS_L14)

GROUP_COLOUR = {
 "Acute vision loss": "#b8860b", "Neuro-ophthalmology": "#5f3a8a",
 # Lecture 13. Chronic loss sits next to acute in hue but darker, so the two
 # read as a pair; tumours take the deepest tone on the chart because they are
 # the rows where getting it wrong costs the most.
 "Chronic vision loss": "#8a6a12", "Refractive": "#4a6b7a", "Ocular tumors": "#6b2233",
 "Eyelid": "#5566b5", "Lacrimal": "#2f6b5a", "Surface": "#7a5a2e",
 "Conjunctivitis": "#8f5aa8", "Sclera": "#a4502a", "Orbit": "#8a5a2b",
 "Cornea": "#2f7d76", "Uvea": "#7a2f5f",
 # Lecture 14. Trauma takes a distinct red-brown so it does not read as a
 # variant of any of the medical groups -- these are the rows where the
 # decision is surgical and the clock is running.
 "Ocular trauma": "#94371f",
}


# ---------------------------------------------------------------------------
# EXTERNALLY SOURCED IMAGES
#
# Jaxon, 2026-08-27: "if a disease process doesnt have an image for it find a
# reputable sourced images of it to include on charts/guides and cite your
# source." Four conjunctivitis rows had no picture on any slide.
#
# THE REPO IS PUBLIC, so committing these republishes them -- see
# [[media_asset_licensing]]. Every licence below was read on the asset's own
# page. That matters here: CDC's Public Health Image Library is NOT uniformly
# public domain. PHIL #15193, the classic chlamydial inclusion conjunctivitis
# photograph, states "This image is copyright protected", so it is NOT used --
# the open-access Cureus case report stands in for it instead. PHIL #3766
# (gonococcal) does carry the public-domain notice, and is used.
EXTERNAL = {
 "Gonococcal conjunctivitis": dict(
   file="ext-gonococcal-conjunctivitis.jpg",
   alt="Newborn with gonococcal ophthalmia neonatorum: marked bilateral lid oedema and copious purulent discharge",
   by="CDC / J. Pledger", where="Public Health Image Library #3766", lic="public domain",
   url="https://commons.wikimedia.org/wiki/File:Gonococcal_ophthalmia_neonatorum.jpg"),
 "Chlamydial conjunctivitis &mdash; neonatal": dict(
   file="ext-chlamydial-conjunctivitis-neonatal.jpg",
   alt="Neonate with chlamydial conjunctivitis: lid oedema, erythema and discharge at the lid margin",
   by="Nwokeji I, Ding K, Ketner S", where="Cureus 2024;16(7):e64463", lic="CC BY 4.0",
   url="https://pmc.ncbi.nlm.nih.gov/articles/PMC11318493/"),
 "Trachoma": dict(
   file="ext-trachoma-stages.jpg",
   alt="Four stages of trachoma: follicles, tarsal conjunctival scarring, entropion with trichiasis, and corneal opacity",
   by="Hu VH and colleagues", where="Trop Med Int Health 2010;15(6):673&ndash;91", lic="CC BY 2.5",
   url="https://commons.wikimedia.org/wiki/File:Trachoma_1.png"),
 "Autoimmune conjunctivitis": dict(
   file="ext-autoimmune-conjunctivitis-mmp.jpg",
   alt="Ocular mucous membrane pemphigoid: inflamed lower palpebral conjunctiva with subconjunctival fibrosis",
   by="Nguyen CDT, Cao J, Dominguez AR", where="JAAD Case Rep 2025;64:95&ndash;99", lic="CC BY 4.0",
   url="https://pmc.ncbi.nlm.nih.gov/articles/PMC12418853/"),
}

def main():
    donor = open(DONOR, encoding="utf-8").read()
    head = donor[:donor.index("</head>")]
    # Exam 1 is teal; Exam 2 is indigo, so the two charts are never confused.
    for old, new in (("#17494b", "#2d3f7a"), ("#3f7d7a", "#5566b5"),
                     ("#123c3d", "#1e2a52"), ("#cfdcdb", "#d3d8ea"),
                     ("#f7fbfa", "#f8f9fd"), ("#1b2b2a", "#1e2233"),
                     ("#eef5f4", "#eef0fa"), ("#4c5f5e", "#525c78"),
                     ("#5f7170", "#646d88"), ("#4a5f5e", "#4f5872")):
        head = head.replace(old, new)
    # The donor chart has 7 columns and can afford a 1180px floor; this one had
    # 12 and could not, which is what forced the sideways scroll. Nine columns
    # with percentage widths fit any container, so the floor goes.
    head = head.replace("min-width:1180px;", "")
    head = re.sub(r"<title>.*?</title>",
                  "<title>Ophthalmology Comparison Chart &mdash; CMS I Exam 2</title>",
                  head, count=1, flags=re.S)
    head = head.replace('href="cms-derm-comparison-chart.docx"',
                        'href="cms-ophtho-comparison-chart.docx"')

    groups = []
    for g in dict.fromkeys(r[1] for r in ROWS):
        groups.append('<button class="filt" data-g="%s" style="--g:%s">%s</button>'
                      % (H.escape(g), GROUP_COLOUR[g], H.escape(g)))

    imgdir = os.path.join(os.path.dirname(OUT), "cms-ophtho-chart-images")
    body_rows, n_pics, n_ext = [], 0, 0
    for row in ROWS:
        name, grp, give, pres, test, tx, urg, edu, slide = row[:9]
        urg_cls = ("emerg" if "EMERGENT" in urg else
                   "sameday" if "SAME DAY" in urg else
                   "urg" if urg.startswith("Urgent") or "URGENT" in urg else "rout")
        pic = IMGS.get(name)
        if pic:
            fn, sl = pic
            assert fn not in REJECTED, ("row %r uses %s, which is %s"
                                        % (name, fn, REJECTED[fn]))
            assert os.path.exists(os.path.join(imgdir, fn)), \
                "missing %s -- run extract_cms_e2_chart_images.py" % fn
            n_pics += 1
            cell = ('<img src="cms-ophtho-chart-images/%s" loading="lazy" '
                    'alt="%s, from the lecture slides."><span class="picite">Slide %d</span>'
                    % (fn, H.escape(re.sub("&[a-z]+;", " ", name)), sl))
        elif name in EXTERNAL:
            e = EXTERNAL[name]
            assert os.path.exists(os.path.join(imgdir, e["file"])), e["file"]
            n_ext += 1
            cell = ('<img src="cms-ophtho-chart-images/%s" loading="lazy" alt="%s">'
                    '<span class="picite">not on a slide &mdash; '
                    '<a href="%s" target="_blank" rel="noopener">%s</a>, %s &middot; %s</span>'
                    % (e["file"], H.escape(e["alt"]), e["url"], H.escape(e["by"]),
                       e["where"], e["lic"]))
        else:
            cell = '<span class="nopic">no image<br>on the slide</span>'
        deck = row[9] if len(row) > 9 else "CMS I Common Ophthalmological Disorders"
        lect = {"11. Neuro-Ophthalmology": "L11",
                "12. Acute Vision Loss": "L12"}.get(deck, "L10")
        slide = '<b class="lect">%s</b><br>%s' % (lect, slide)
        pain, side, sign = DIFF[name]
        # data-* attributes drive the filter row, so "show me only the painful
        # ones" is one click -- which is the comparison she actually asked for.
        painful, lat = classify(pain, side)
        body_rows.append(
            '<tr data-g="%s" data-pain="%s" data-lat="%s">'
            '<td class="pic">%s</td>'
            '<td class="nm"><b>%s</b><span class="grp" style="background:%s">%s</span>'
            '<span class="sl">%s</span></td>'
            '<td class="d pain">%s<span class="side">%s</span></td><td class="d sign">%s</td>'
            '<td class="gv">%s</td><td>%s</td><td>%s</td>'
            '<td>%s<span class="u %s">%s</span></td><td>%s</td></tr>'
            % (H.escape(grp), painful, lat, cell, name, GROUP_COLOUR[grp], H.escape(grp),
               slide, pain, side, sign, give, pres, test, tx, urg_cls, urg, edu))

    html = head + """</head><body>
<div class="guide-back-bar">
  <a href="#" class="guide-back-link" onclick="event.preventDefault(); window.guideGoBack();">&larr; Back</a>
</div>
<div class="wrap">
<header class="top">
  <h1>Ophthalmology Comparison Chart</h1>
  <p>Clinical Medicine and Surgery I &middot; Exam 2 &middot; Class of 2028</p>
  <p>__N__ conditions from the Common Ophthalmological Disorders lecture</p>
  <p style="margin-top:10px;font-size:.82rem;color:var(--c-mute)">Use the <b>Download as PDF</b> button,
  top right, to keep this offline &mdash; it prints landscape with every row intact.</p>
</header>

<div class="howto"><b>How to use this.</b> Read it left to right for one condition:
<b>the words a question will use to hand it to you</b>, how it presents and what you find on
examination, what you order, what you give, <b>how fast the patient has to be seen</b>, and what you
tell them. Read it top to bottom down one column to compare across conditions.<br><br>
<b>The three grey columns are Professor Jaquith&rsquo;s own instruction.</b> At the end of the
26 August lecture she said: <i>&ldquo;My recommendation to you guys for those is again, use your
resources, <b>make a chart</b> &mdash; which ones cause pain, which ones don&rsquo;t cause pain?
Which ones are unilateral, which ones are bilateral? Which ones will cause which physical exam
abnormalities, like fixed pupils, for example. <b>That&rsquo;s how you&rsquo;re gonna differentiate
these</b> &mdash; particularly your pink eye &hellip; that&rsquo;s definitely gonna be on your exam,
<b>at least two questions minimum</b>.&rdquo;</i> So those three are their own columns, and the
buttons above let you pull out just the painful ones or just the bilateral ones and read down.<br><br>
<b>The gold &ldquo;Vignette giveaway&rdquo; column</b> is the one to scan when a stem is in front of you.
Professor Jaquith described this exam as <i>&ldquo;pretty much all clinical vignettes &hellip; recognize
conditions by the vignette&rdquo;</i>, and a vignette gives itself away in a handful of words &mdash;
<i>the eye itself is white</i>, <i>vessels do not move</i>, <i>terminal end bulbs</i>,
<i>resists opening the eye</i>. Every phrase there is language the lecture deck itself uses.<br><br>
<b>The &ldquo;How fast&rdquo; column</b> is the ophthalmology-specific one. In dermatology the useful
axis was first-line against second-line treatment; here the decision that changes an outcome is how
quickly the patient is seen, and the deck ends with an explicit emergent / same-day / urgent / routine
table. <span class="u emerg" style="padding:1px 6px">EMERGENT</span> means now.
<span class="u sameday" style="padding:1px 6px">SAME DAY</span> means before the end of the day.<br><br>
<b>Most pictures come from the lecture deck and cite their slide.</b> Some carry their source
stamped into the image &mdash; <i>EyeRounds.org</i>, the <i>Kellogg Eye Center</i>,
<i>&copy; Logical Images</i> &mdash; and those marks are left visible on purpose; they are part of
the citation.<br><br>
<b>The Slide column names the lecture.</b> This chart now spans three decks &mdash;
<b>L10</b> Common Ophthalmological Disorders, <b>L11</b> Neuro-Ophthalmology and <b>L12</b> Acute
Vision Loss &mdash; so a bare slide number no longer identifies anything on its own. Lecture 11 and
12 pictures are filed under <i>l11-</i> and <i>l12-</i> filenames for the same reason: the three
decks number their slides independently, and without the prefix four figures resolved to the wrong
Lecture 10 photographs.<br><br>
<b>Sixteen of the Lecture 11 and 12 rows have no picture.</b> Those decks illustrate the pathways
and the classic fundus findings rather than every named condition, so the rows that carry a
photograph are the ones the deck actually photographs &mdash; the glaucomatous disc, the detached
retina, the swollen papilledematous disc, the demyelinating lesions on MRI. Nothing was sourced
from outside those two decks.<br><br>
<b>Four Lecture 10 conditions have no picture anywhere in that deck</b> &mdash; gonococcal conjunctivitis,
neonatal chlamydial conjunctivitis, trachoma and autoimmune conjunctivitis. Each of those carries an
openly licensed photograph from elsewhere instead, credited by author, source and licence beneath the
picture. The classic CDC chlamydial conjunctivitis photograph is <i>not</i> among them: its own library
page marks it copyright protected, so an open-access case report stands in for it.<br><br>
<b>Two of the deck&rsquo;s pictures are deliberately NOT used.</b> Slide 29&rsquo;s first image is a
<b>hyphaema</b> and slide 27&rsquo;s third is <b>conjunctival intraepithelial neoplasia</b> &mdash;
both are captioned <i>DDX</i> on the slide itself. Putting either in a chart cell would say
&ldquo;this is what the condition looks like&rdquo; about a picture of something else.<br><br>
<b>Where a slide reads as an absolute and its own speaker notes soften it, the hedge is what is
written here</b> &mdash; imaging is not automatic for the lacrimal infections or for clearly
pre-septal cellulitis, and a recurrent subconjunctival haemorrhage does not mean an automatic
haematology referral.</div>

<div class="filters"><button class="filt on" data-g="__all__">All</button>__GROUPS__</div>
<div class="filters filters2">
  <span class="flabel">Her three:</span>
  <button class="filt2" data-pain="yes">Painful</button>
  <button class="filt2" data-pain="no">Painless</button>
  <button class="filt2" data-lat="uni">Unilateral</button>
  <button class="filt2" data-lat="bi">Bilateral</button>
  <button class="filt2 on" data-clear="1">Show all</button>
</div>

<div class="tblwrap"><table>
<colgroup>
  <col style="width:11%"><col style="width:10%"><col style="width:9%"><col style="width:11%">
  <col style="width:12%"><col style="width:14%"><col style="width:12%"><col style="width:11%">
  <col style="width:10%">
</colgroup>
<thead><tr>
  <th>Picture</th>
  <th>Condition</th>
  <th class="d-h">Pain &amp; side</th>
  <th class="d-h">Key exam abnormality</th>
  <th class="gv-h">Vignette giveaway<br><span style="font-weight:400;opacity:.75">the words that hand it to you</span></th>
  <th>Presentation &amp; exam findings</th>
  <th>Testing &amp; what causes it</th>
  <th>Treatment &amp; how fast</th>
  <th>Patient education &amp; prognosis</th>
</tr></thead>
<tbody>
__ROWS__
</tbody></table></div>
</div>
<script src="../theme.js"></script>
<script>
  // Two independent filters: region (top row) and her three discriminators
  // (second row). Both apply at once, so "cornea AND painful" works.
  var curG = '__all__', curPain = null, curLat = null;
  function apply(){
    document.querySelectorAll('tbody tr').forEach(function(tr){
      var ok = (curG === '__all__' || tr.dataset.g === curG)
            && (!curPain || tr.dataset.pain === curPain)
            && (!curLat  || tr.dataset.lat === curLat || tr.dataset.lat === 'either');
      tr.style.display = ok ? '' : 'none';
    });
  }
  document.querySelectorAll('.filt').forEach(function(b){
    b.addEventListener('click', function(){
      document.querySelectorAll('.filt').forEach(function(x){x.classList.remove('on');});
      b.classList.add('on'); curG = b.dataset.g; apply();
    });
  });
  document.querySelectorAll('.filt2').forEach(function(b){
    b.addEventListener('click', function(){
      document.querySelectorAll('.filt2').forEach(function(x){x.classList.remove('on');});
      b.classList.add('on');
      curPain = b.dataset.pain || null;
      curLat  = b.dataset.lat  || null;
      apply();
    });
  });
</script>
<style>
  .filters{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 10px;}
  .filt{font:inherit;font-size:.82rem;padding:5px 12px;border-radius:999px;cursor:pointer;
        border:1px solid var(--c-line);background:var(--c-btn-bg);color:var(--c-fg);}
  .filt.on{background:var(--acc);color:#fff;border-color:var(--acc);}
  table{table-layout:fixed;}
  td, th{overflow-wrap:break-word;}
  td.nm{white-space:normal;}
  td.nm .sl{display:block;margin-top:5px;font-size:.66rem;color:var(--c-mute);
            font-variant-numeric:tabular-nums;line-height:1.35;}
  td.nm .grp{display:block;margin-top:4px;font-size:.66rem;color:#fff;padding:1px 7px;
             border-radius:999px;width:fit-content;letter-spacing:.02em;}
  td.gv{background:var(--c-gv-bg);color:var(--c-gv-b);font-weight:600;}
  td.sl{text-align:center;color:var(--c-mute);white-space:nowrap;font-variant-numeric:tabular-nums;}
  td.pic{text-align:center;vertical-align:top;padding:8px;}
  td.pic img{width:100%;max-width:180px;height:auto;border-radius:6px;display:block;margin:0 auto;
             border:1px solid var(--c-line);}
  td.pic .picite{display:block;margin-top:4px;font-size:.66rem;color:var(--c-mute);}
  td.pic .nopic{display:inline-block;font-size:.7rem;color:var(--c-mute);line-height:1.3;}
  th.d-h{background:var(--c-panel);color:var(--c-panel-fg);}
  td.d{background:var(--c-panel);font-size:.82rem;}
  td.pain .side{display:block;margin-top:3px;opacity:.85;}
  td .u{display:block;margin-top:6px;}
  .filters2{margin-top:-4px;align-items:center;}
  .flabel{font-size:.8rem;color:var(--c-mute);margin-right:4px;}
  .filt2{font:inherit;font-size:.8rem;padding:4px 11px;border-radius:999px;cursor:pointer;
         border:1px solid var(--c-line);background:var(--c-btn-bg);color:var(--c-fg);}
  .filt2.on{background:var(--gold);color:#241a02;border-color:var(--gold);}
  td .u{font-weight:700;font-size:.78rem;}
  td .u.emerg{color:#8c1d12;} td .u.sameday{color:#8c4a12;}
  td .u.urg{color:#7a5a08;} td .u.rout{color:#3f5c46;font-weight:600;}
</style>
</body></html>"""
    html = (html.replace("__ROWS__", "\n".join(body_rows))
                .replace("__GROUPS__", "".join(groups))
                .replace("__N__", str(len(ROWS))))

    for tag in ("table", "thead", "tbody", "tr", "td", "th", "div", "p", "header"):
        o = len(re.findall(r"<%s[ >]" % tag, html)); c = html.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    for fn in re.findall(r'src="cms-ophtho-chart-images/([^"]+)"', html):
        if fn.startswith("ext-"):
            continue        # sourced outside the deck; REJECTED only lists slide blobs
        assert fn not in REJECTED, "a rejected DDX image reached the page: %s" % fn
        assert os.path.exists(os.path.join(imgdir, fn)), fn
    missing = [r[0] for r in ROWS if r[0] not in DIFF]
    assert not missing, ("every row needs her three discriminators -- pain, laterality "
                         "and the key exam sign: %r" % missing)
    names = [r[0] for r in ROWS]
    assert len(names) == len(set(names)), "duplicate condition row"
    for r in ROWS:
        assert r[1] in GROUP_COLOUR, "row %r has an unknown group" % r[0]
        assert all(str(x).strip() for x in r), "row %r has an empty cell" % r[0]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d conditions, %d with a picture, %d groups)"
          % (os.path.basename(OUT), len(html) // 1024, len(ROWS), n_pics, len(GROUP_COLOUR))
          + ("; %d sourced outside the deck and credited" % n_ext if n_ext else ""))
    print("rejected DDX images kept out: %s" % ", ".join(sorted(REJECTED)))


if __name__ == "__main__":
    main()
