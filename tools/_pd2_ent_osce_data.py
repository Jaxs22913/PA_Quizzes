# -*- coding: utf-8 -*-
"""OSCE fields for the ENT chart -- the parts the CMS chart does not carry.

Jaxon, 2026-09-08, for the ENT OSCE: "for each disease process I need how the
patient describes it/common complaint, clinical manifestations/what we see on
inspection, physical exams to do to rule in or out, differential diagnosis
(top 3), tests to rule it in/tests to rule out the differentials,
treatment/referals, patient education."

Three of those already exist, audited and slide-cited, in the CMS ENT chart
modules: inspection findings, treatment with referral urgency, and patient
education. Restating them here would create two sources that drift, so this
file carries ONLY the four that are new, and the builder joins them:

    says     what the patient actually says, in their words rather than ours
    exam     the manoeuvres performed to rule the diagnosis in or out
    ddx      the top three differentials, each with what separates it
    tests    (rule it IN, rule the differentials OUT) -- a pair, because the
             question "what confirms this" and "what excludes the others" have
             different answers and the OSCE asks both

EVERY TEST NAMES ITS FINDING. Jaxon, same day: "with the tests describe what we
would see on what we order. for example: order CBC - above 40 is positive."
Naming the investigation is the easy half and the half that does not help in a
station -- "order a CT" is worth nothing if you cannot say what makes it
positive. So each entry reads ORDER -> WHAT A POSITIVE LOOKS LIKE, and the
rule-out column says which finding on which test sends you to a different
diagnosis.

Keyed by the condition name exactly as it appears in the CMS chart rows, so a
rename there fails the build rather than silently dropping a row.
"""

def E(says, exam, ddx, rule_in, rule_out):
    assert len(ddx) == 3, "top three differentials, got %d" % len(ddx)
    return {"says": says, "exam": exam, "ddx": ddx,
            "rule_in": rule_in, "rule_out": rule_out}


OSCE = {

# ---------------------------------------------------------------- EMERGENT
"Malignant otitis externa": E(
  "&ldquo;My ear has been running for weeks and the pain keeps me awake &mdash; the drops did "
  "nothing.&rdquo;",
  "Otoscopy looking for <b>granulation tissue at the bony-cartilaginous junction</b>. Palpate the "
  "mastoid and TMJ. <b>Test all cranial nerves, especially VII</b> &mdash; a facial palsy marks "
  "skull base spread. Check glucose and immune status.",
  [("Ordinary otitis externa", "Responds to drops within days and has no granulation or night pain"),
   ("Otomycosis", "Itch dominates, visible hyphae or curd, no bone involvement"),
   ("Ear canal carcinoma", "Also treatment-resistant, but bleeds and is friable rather than "
                           "granulating at one point")],
  "<b>Computed tomography or magnetic resonance of the temporal bone</b> &rarr; bony erosion of the "
  "skull base. <b>Erythrocyte sedimentation rate</b> &rarr; markedly raised, and it is what "
  "treatment response is tracked against. <b>Canal culture</b> &rarr; <i>Pseudomonas "
  "aeruginosa</i>.",
  "Normal imaging and prompt response to topical therapy exclude it; biopsy of friable tissue "
  "excludes carcinoma; fungal culture excludes otomycosis."),

"Carcinoma of the ear canal": E(
  "&ldquo;It has been discharging for months, now there is blood in it and a deep ache.&rdquo;",
  "Otoscopy for <b>friable tissue and bloody otorrhoea</b>. Palpate for parotid and cervical "
  "nodes. Cranial nerve examination, particularly VII.",
  [("Malignant otitis externa", "Diabetic or immunocompromised, granulation rather than a friable mass"),
   ("Chronic suppurative otitis media", "Painless discharge through a perforation, no bleeding"),
   ("Cholesteatoma", "White keratin behind a retraction pocket, foul but not bloody")],
  "<b>Biopsy of the canal lesion</b> &rarr; squamous cell carcinoma on histology. <b>Computed "
  "tomography of the temporal bone</b> &rarr; bony erosion where infection alone would not.",
  "Imaging for bone involvement separates it from the infections; a normal biopsy with "
  "<i>Pseudomonas</i> on culture points back to necrotising otitis externa."),

"Sudden sensorineural hearing loss": E(
  "&ldquo;I woke up and one ear just wasn&rsquo;t working.&rdquo;",
  "<b>Otoscopy must be normal.</b> <b>Weber lateralises AWAY</b> to the good ear and <b>Rinne stays "
  "normal (air over bone) in both</b> &mdash; that pair is what proves it is sensorineural. Check "
  "cranial nerves and balance.",
  [("Cerumen impaction", "Wax visible; Weber would lateralise TOWARD the blocked ear"),
   ("Otitis media with effusion", "Amber drum with reduced mobility; conductive pattern"),
   ("Acoustic neuroma", "Gradual rather than sudden, with speech discrimination out of proportion")],
  "<b>Pure tone audiometry</b> &rarr; a sensorineural loss with NO air-bone gap, by definition at "
  "least 30 decibels across three contiguous frequencies. <b>Magnetic resonance with "
  "gadolinium</b> &rarr; an enhancing lesion in the internal auditory canal if a schwannoma is the "
  "cause.",
  "A normal otoscopy excludes wax and effusion; a normal tympanogram excludes a middle ear cause; "
  "normal imaging excludes a schwannoma."),

"Vertebrobasilar insufficiency or occlusion": E(
  "&ldquo;The room spins and my speech goes funny, and sometimes I see double.&rdquo;",
  "<b>Full cranial nerve and cerebellar examination</b> &mdash; the point is to find the signs that "
  "are NOT ear. Gait, finger-nose, heel-shin. Blood pressure in both arms; listen for carotid "
  "bruits; check rhythm for atrial fibrillation.",
  [("Vestibular neuronitis", "Sustained vertigo but NO other neurological sign and normal hearing"),
   ("Meniere disease", "Episodic vertigo with fluctuating low-frequency loss and fullness"),
   ("Positional vertigo", "Seconds only, provoked by position, fatigable nystagmus")],
  "<b>Magnetic resonance imaging and angiography of the posterior circulation</b> &rarr; stenosis "
  "or occlusion of the vertebral or basilar artery, with infarction in its territory.",
  "The presence of diplopia, dysarthria or limb signs is itself what excludes the peripheral "
  "causes; a normal Dix-Hallpike excludes positional vertigo."),

"Isolated cerebellar infarction": E(
  "&ldquo;Everything is spinning and I cannot sit up without falling over.&rdquo;",
  "<b>Truncal stability &mdash; can they sit unsupported?</b> A peripheral patient usually can. "
  "Look for <b>direction-changing nystagmus</b>, limb ataxia, and any focal deficit. Ask about "
  "headache.",
  [("Vestibular neuronitis", "Unidirectional nystagmus, can still sit, no headache"),
   ("Labyrinthitis", "Same as neuronitis but with hearing loss; still no central signs"),
   ("Positional vertigo", "Brief and positional; the patient is well between episodes")],
  "<b>Magnetic resonance imaging with diffusion weighting</b> &rarr; restricted diffusion in a "
  "cerebellar hemisphere. Computed tomography is often NORMAL early, so a normal scan does not "
  "exclude it.",
  "Unidirectional fatigable nystagmus with intact truncal stability and no headache points "
  "peripheral; normal imaging excludes infarction."),

"Sinusitis with urgent features": E(
  "&ldquo;My sinuses have been bad for a week and now my eye is swollen and I&rsquo;m seeing "
  "double.&rdquo;",
  "<b>Eye movements and pain on movement</b>, visual acuity, pupils for a relative afferent "
  "defect, and look for <b>proptosis</b>. Assess mental state. Palpate sinus tenderness.",
  [("Uncomplicated bacterial sinusitis", "Facial pain and purulence WITHOUT eye or neurological signs"),
   ("Pre-septal cellulitis", "Lid swelling but the eye is white, movements full and painless"),
   ("Allergic rhinitis", "Bilateral clear discharge with itch and a bluish boggy mucosa")],
  "<b>Contrast computed tomography of orbits and sinuses</b> &rarr; opacified sinuses PLUS fat "
  "stranding, a subperiosteal collection or proptosis &mdash; sinus opacity alone is present in "
  "ordinary sinusitis and proves nothing.",
  "Full painless eye movements with normal vision exclude orbital involvement; normal mental state "
  "and no headache argue against intracranial spread."),

"Epistaxis &mdash; posterior": E(
  "&ldquo;It won&rsquo;t stop, and I keep swallowing blood.&rdquo;",
  "<b>Assess circulation first</b> &mdash; pulse, blood pressure, conscious level. Then anterior "
  "rhinoscopy: if <b>no bleeding point is visible and blood runs down the pharynx</b>, it is "
  "posterior. Look in the throat.",
  [("Anterior epistaxis", "90% of cases; a visible spot on Kiesselbach plexus, stops with pressure"),
   ("Nasal foreign body", "Unilateral foul purulent discharge, usually a young child"),
   ("Nasopharyngeal tumour", "Recurrent bleeding with obstruction, a neck mass or cranial nerve signs")],
  "<b>Nasal endoscopy</b> &rarr; a bleeding point posterior to the middle turbinate, with no "
  "anterior source &mdash; often the only way to see it. <b>Full blood count</b> &rarr; the "
  "haematocrit, and <b>type and crossmatch</b> &rarr; blood ready if it continues. <b>Coagulation "
  "studies</b> &rarr; a raised international normalised ratio or low platelets driving it.",
  "A visible anterior bleeding point that stops with ten minutes of pressure excludes a posterior "
  "source; endoscopy excludes a tumour."),

"Nasopharyngeal carcinoma": E(
  "&ldquo;I found a lump in my neck, and lately I&rsquo;ve had double vision and my cheek feels "
  "numb.&rdquo;",
  "Palpate the neck systematically. <b>Cranial nerve examination</b> &mdash; especially VI for "
  "diplopia and V for facial numbness. Otoscopy for a middle ear effusion, which is often the "
  "first sign. Anterior rhinoscopy.",
  [("Chronic sinusitis", "Congestion and discharge without a neck mass or cranial nerve deficit"),
   ("Reactive lymphadenopathy", "Follows an infection and regresses within two weeks"),
   ("Lymphoma", "Rapid painless nodal growth with night sweats and weight loss")],
  "<b>Endoscopic guided biopsy</b> &rarr; carcinoma of the nasopharynx. <b>Magnetic resonance "
  "imaging</b> &rarr; a nasopharyngeal mass with skull base involvement. Epstein-Barr titres are "
  "supportive, not diagnostic.",
  "A normal nasopharynx on endoscopy excludes it; a node that regresses excludes malignancy; "
  "Epstein-Barr serology supports rather than confirms."),

"Neck neoplasm &mdash; general": E(
  "&ldquo;There&rsquo;s a lump in my neck that hasn&rsquo;t gone away.&rdquo;",
  "Characterise the mass: <b>site, size, consistency, mobility and tenderness</b>. Then the "
  "complete head and neck examination &mdash; <b>visualise every mucosal surface and palpate the "
  "oral and pharyngeal surfaces</b>. Palpate thyroid, other nodal basins, liver and spleen. "
  "Auscultate for a bruit.",
  [("Reactive lymphadenopathy", "Infective context, tender, regresses within two weeks"),
   ("Congenital cyst", "Present for years, fluctuant, lateral or midline by type"),
   ("Lymphoma", "Rapid growth WITHOUT infective symptoms, with night sweats and weight loss")],
  "<b>Fine needle aspiration, minimum four passes</b> &rarr; malignant cells, and which kind: "
  "squamous carcinoma against lymphoma. <b>Contrast computed tomography</b> &rarr; a solid, "
  "irregular, centrally necrotic node rather than a smooth cystic one.",
  "An identified infective source with resolution excludes malignancy; aspiration separates "
  "carcinoma from lymphoma; imaging separates solid from cystic."),

"Anaplastic thyroid carcinoma": E(
  "&ldquo;This lump in my throat has grown in a matter of weeks and now my voice has gone.&rdquo;",
  "Palpate the thyroid while the patient <b>swallows</b> &mdash; it should elevate. Assess for "
  "<b>stridor and tracheal deviation</b>. Listen to the voice; check for cervical nodes.",
  [("Papillary carcinoma", "Slow-growing in a younger patient with a far better outlook"),
   ("Primary thyroid lymphoma", "Also rapid in an older patient, but on a Hashimoto background"),
   ("Multinodular goitre", "Long-standing, soft, no hoarseness or compressive symptoms")],
  "<b>Fine needle aspiration</b> &rarr; undifferentiated small, giant and spindle cells. "
  "<b>Computed tomography</b> &rarr; a large infiltrative mass with tracheal compression.",
  "Cytology separates it from lymphoma, which needs an open biopsy; a long history with a stable "
  "gland excludes it."),

"Epiglottitis (supraglottitis)": E(
  "&ldquo;It hurts so much to swallow I can&rsquo;t even manage my own spit.&rdquo; A child may "
  "say nothing and simply sit forward.",
  "<b>Look, do not touch.</b> Observe posture (<b>tripod, neck extended, chin forward</b>), "
  "drooling, voice quality and work of breathing. <b>Do NOT perform an intraoral examination or "
  "venipuncture</b> &mdash; either can complete the obstruction.",
  [("Peritonsillar abscess", "Trismus with uvular deviation; the mouth CAN be examined"),
   ("Retropharyngeal abscess", "Neck stiffness with a widened prevertebral space on X-ray"),
   ("Croup", "Barking cough with a slower onset and a well-looking child")],
  "<b>Mirror or fiberoptic laryngoscopy, the gold standard</b> &rarr; a <b>cherry-red, swollen "
  "epiglottis</b>, performed only where the airway can be secured. <b>Lateral neck radiograph</b> "
  "&rarr; the <b>thumbprint sign</b>, a swollen epiglottis in profile &mdash; supportive, but a "
  "normal film does NOT exclude it, so it is never the reason to stand down.",
  "Direct visualisation of a normal supraglottis excludes it; a lateral neck film showing a "
  "widened prevertebral space redirects to retropharyngeal abscess."),

"Diphtheria": E(
  "&ldquo;My throat is a bit sore but I feel dreadful.&rdquo; &mdash; the malaise is out of "
  "proportion to the sore throat.",
  "Inspect the pharynx for a <b>tenacious grey membrane that bleeds when disturbed</b>. Palpate "
  "for a bull neck. <b>Cardiac and cranial nerve examination</b>, since the toxin causes "
  "myocarditis and neuropathy. Check immunisation status.",
  [("Streptococcal pharyngitis", "Exudate wipes away and does not bleed; no toxaemia"),
   ("Infectious mononucleosis", "Palatal petechiae with splenomegaly and marked fatigue"),
   ("Candidiasis", "Creamy patches that wipe off leaving an erythematous base")],
  "<b>Throat swab and culture on tellurite medium</b> &rarr; <i>Corynebacterium diphtheriae</i>. "
  "<b>Electrocardiogram</b> &rarr; heart block or arrhythmia from toxin-induced myocarditis.",
  "An exudate that wipes off without bleeding excludes it; a positive monospot points to "
  "mononucleosis; potassium hydroxide preparation confirms candida."),

"Peritonsillar abscess (quinsy)": E(
  "&ldquo;My throat is agony on one side, I can&rsquo;t open my mouth properly and I sound "
  "strange.&rdquo;",
  "Measure <b>mouth opening &mdash; trismus is the most reliable sign</b>. Inspect for "
  "<b>uvular deviation and medial displacement of the soft palate</b>. Listen for the hot potato "
  "voice. Palpate cervical nodes.",
  [("Severe tonsillitis", "Bilateral and symmetric with no palatal deviation or trismus"),
   ("Retropharyngeal abscess", "Neck stiffness and a widened prevertebral space; younger child"),
   ("Epiglottitis", "Drooling with tripod posture; the mouth cannot safely be examined")],
  "<b>Needle aspiration</b> &rarr; frank pus, which both confirms and treats. <b>Ultrasound</b> "
  "&rarr; a discrete hypoechoic collection rather than diffuse cellulitis. <b>Contrast computed "
  "tomography</b> &rarr; a rim-enhancing peritonsillar collection.",
  "Symmetric tonsils with a midline uvula exclude it; a normal lateral neck film excludes a "
  "retropharyngeal collection."),

"Retropharyngeal abscess": E(
  "A parent says &ldquo;she won&rsquo;t eat, she&rsquo;s drooling and she holds her neck "
  "stiff.&rdquo;",
  "Observe posture and drooling. Test <b>neck movement &mdash; stiffness and refusal to extend</b> "
  "is the pointer. Assess the airway. Avoid vigorous pharyngeal examination.",
  [("Epiglottitis", "Same drooling and posture but a much faster onset and no neck stiffness"),
   ("Peritonsillar abscess", "Trismus with uvular deviation; older patient"),
   ("Meningitis", "Neck stiffness with photophobia and altered consciousness rather than dysphagia")],
  "<b>Lateral neck radiograph</b> &rarr; a <b>widened prevertebral soft tissue space</b>, taken in "
  "full inspiration with the neck extended or it falsely appears widened. <b>Contrast computed "
  "tomography of the neck, the gold standard</b> &rarr; a <b>rim-enhancing collection</b> in the "
  "retropharyngeal space, which is what separates a drainable abscess from cellulitis.",
  "A normal prevertebral space excludes it; computed tomography separates abscess from adenitis, "
  "which is the decision that matters."),

"Ludwig angina": E(
  "&ldquo;My tooth was killing me and now my whole neck under the chin is swollen and I "
  "can&rsquo;t swallow.&rdquo;",
  "Inspect and palpate the <b>floor of the mouth &mdash; is it raised and firm?</b> Look for "
  "<b>tongue displacement upward and backward</b>. Assess airway and voice. Examine the dentition "
  "for the offending tooth.",
  [("Submandibular sialadenitis", "Swelling of the gland itself, pus from the duct, no floor elevation"),
   ("Dental abscess", "Localised to one tooth without spread across the floor of the mouth"),
   ("Peritonsillar abscess", "Intraoral and unilateral with trismus and uvular deviation")],
  "<b>Contrast computed tomography of the neck</b> &rarr; diffuse cellulitis and phlegmon of the "
  "submandibular and sublingual spaces, with or without a rim-enhancing collection; airway "
  "narrowing is the finding that decides the next hour.",
  "A soft floor of mouth with a normally positioned tongue excludes it; pus expressible from "
  "Wharton duct points to sialadenitis."),

"Erythroplakia": E(
  "&ldquo;There&rsquo;s a red patch in my mouth that won&rsquo;t go.&rdquo; &mdash; often "
  "asymptomatic and found incidentally.",
  "Inspect every mucosal surface with a good light. <b>Attempt to scrape the lesion &mdash; it "
  "does not come off.</b> Palpate the lesion and the neck nodes. Ask about tobacco and alcohol.",
  [("Leukoplakia", "White rather than red, and far less likely to be malignant"),
   ("Erythematous candidiasis", "Painful, denture-related, responds to antifungals"),
   ("Lichen planus", "Lacy white striae, often bilateral and symmetric")],
  "<b>Excisional biopsy</b> &rarr; dysplasia or frank carcinoma in about 90%, which is the figure "
  "that makes this urgent.",
  "A lesion that wipes off is candidiasis; resolution on antifungal therapy excludes it; biopsy "
  "settles the rest."),

"Oral cavity and oropharyngeal cancer": E(
  "&ldquo;This ulcer hasn&rsquo;t healed for weeks, and my ear aches on that side.&rdquo;",
  "Inspect and <b>palpate</b> every oral surface, including the floor of mouth and tongue base. "
  "Assess tongue mobility and trismus. <b>Palpate cervical nodes.</b> Examine the ear &mdash; it "
  "will be normal despite the pain.",
  [("Traumatic ulcer", "Resolves once the denture or sharp tooth is corrected"),
   ("Aphthous ulcer", "Heals in 7 to 10 days; on non-keratinised mucosa"),
   ("Erythroplakia or leukoplakia", "A patch rather than an ulcer, though either may harbour carcinoma")],
  "<b>Biopsy</b> &rarr; squamous cell carcinoma. <b>p16 immunohistochemistry or in situ "
  "hybridisation</b> &rarr; positive in human papillomavirus related oropharyngeal disease, which "
  "carries a better prognosis. <b>Computed tomography or magnetic resonance</b> &rarr; the primary "
  "and any nodal spread.",
  "Healing within two weeks after removing an irritant excludes malignancy; a normal ear "
  "examination with persistent otalgia is itself a pointer TOWARD it."),

"Primary neck tumours &mdash; the list": E(
  "Not a presentation &mdash; a reference list of what a primary neck tumour can be.",
  "As for any neck mass: characterise the lump, then a complete head and neck examination, and "
  "auscultate for a bruit before any needle is used.",
  [("Metastatic squamous carcinoma", "Far commoner than any primary neck tumour"),
   ("Lymphoma", "Rubbery, multiple, with constitutional symptoms"),
   ("Paraganglioma", "Pulsatile with a bruit &mdash; must not be biopsied blindly")],
  "<b>Fine needle aspiration</b> &rarr; the cell type, for solid masses only. <b>Computed "
  "tomography angiography FIRST if it pulsates</b> &rarr; an intensely enhancing mass splaying the "
  "carotid bifurcation, which is a paraganglioma and must not be needled.",
  "A bruit or pulsation excludes a safe blind biopsy and redirects to angiography."),
}


# ------------------------------------------------------------------ batches
# Authored in regional batches so each sitting stays coherent -- the ear
# differentials only make sense written next to each other. Merged here; the
# builder cross-checks the merged keys against the CMS chart, so a rename in
# either place fails the build instead of silently dropping a condition.
for _mod in ("_osce_batch_ear1", "_osce_batch_ear2", "_osce_batch_nose",
             "_osce_batch_neck1", "_osce_batch_thy_oral", "_osce_batch_larynx"):
    _b = __import__(_mod).BATCH
    _dupes = set(_b) & set(OSCE)
    assert not _dupes, "%s redefines %s" % (_mod, sorted(_dupes))
    OSCE.update(_b)
