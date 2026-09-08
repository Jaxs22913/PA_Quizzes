# -*- coding: utf-8 -*-
from _pd2_ent_osce_data import E
BATCH = {

"Thyroid nodule and mass": E(
  "&ldquo;I noticed a lump in the front of my neck&rdquo; &mdash; or it was found incidentally on a "
  "scan done for something else.",
  "Stand BEHIND the patient to palpate the thyroid, and <b>ask them to swallow &mdash; thyroid "
  "masses rise</b>. Assess size, consistency, mobility and whether it is single or multinodular. "
  "<b>Palpate cervical nodes</b>, listen to the voice, and check for tracheal deviation and "
  "stridor. Look for signs of over- or underactivity.",
  [("Multinodular goitre", "Several nodules in a diffusely enlarged gland; far lower risk"),
   ("Thyroid carcinoma", "Hard, fixed, growing, with hoarseness or nodes &mdash; the point of the workup"),
   ("Thyroglossal duct cyst", "Midline, rises with TONGUE protrusion as well as swallowing")],
  "<b>Thyroid stimulating hormone FIRST</b> &rarr; if SUPPRESSED, a radionuclide scan showing a "
  "<b>hot nodule</b>, which is almost never malignant and does not need aspiration. If normal or "
  "raised, <b>ultrasound</b> &rarr; suspicious features (microcalcification, taller-than-wide "
  "shape, irregular margins, hypoechogenicity) and then <b>fine needle aspiration</b> &rarr; the "
  "cytological diagnosis.",
  "A hot nodule on scintigraphy effectively excludes cancer; benign cytology with reassuring "
  "ultrasound allows surveillance; elevation on tongue protrusion redirects to a thyroglossal cyst."),

"Papillary thyroid carcinoma": E(
  "&ldquo;There&rsquo;s a painless lump in my neck&rdquo; &mdash; often noticed by someone else, in "
  "a younger patient.",
  "Palpate the nodule during swallowing; note firmness and mobility. <b>Palpate the cervical nodes "
  "carefully &mdash; it spreads by lymphatics and a node may be the presenting sign.</b> Assess the "
  "voice. Ask about childhood radiation exposure and family history.",
  [("Benign colloid nodule", "Soft, unchanging, benign cytology"),
   ("Follicular carcinoma", "Spreads by BLOOD rather than lymphatics, and cytology cannot call it"),
   ("Medullary carcinoma", "Raised calcitonin, with a familial syndrome to consider")],
  "<b>Fine needle aspiration</b> &rarr; the <b>nuclear features</b> that make this the one thyroid "
  "cancer cytology can diagnose confidently: <b>Orphan Annie nuclei, nuclear grooves and "
  "psammoma bodies</b>. <b>Ultrasound of neck and nodes</b> &rarr; the primary and nodal spread.",
  "Benign cytology with a reassuring ultrasound excludes it; a follicular pattern on cytology "
  "cannot be resolved without surgery; raised calcitonin redirects to medullary carcinoma."),

"Follicular thyroid carcinoma": E(
  "&ldquo;I&rsquo;ve had this lump for a while&rdquo; &mdash; or the presentation is a bone or lung "
  "metastasis in an older patient.",
  "Palpate the nodule with swallowing. <b>Cervical nodes are often NEGATIVE</b>, because spread is "
  "haematogenous &mdash; a normal neck does not reassure here. Check the voice. Examine for bone "
  "tenderness and take a respiratory history.",
  [("Follicular adenoma", "Cytologically IDENTICAL &mdash; only capsular or vascular invasion separates them"),
   ("Papillary carcinoma", "Nodal spread with diagnostic nuclear features on aspiration"),
   ("Multinodular goitre", "Multiple nodules, benign cytology, stable over years")],
  "<b>Fine needle aspiration</b> &rarr; a <b>follicular neoplasm &mdash; which CANNOT distinguish "
  "carcinoma from adenoma</b>. <b>Surgical excision with histology</b> &rarr; <b>capsular and "
  "vascular invasion</b>, which is the only thing that makes it a carcinoma. Imaging of chest and "
  "bone for metastases.",
  "Histology without invasion means an adenoma; papillary nuclear features on cytology redirect; "
  "raised calcitonin means medullary disease. <b>A follicular result on aspiration always goes to "
  "surgery &mdash; repeat aspiration cannot settle it.</b>"),

"Medullary thyroid carcinoma": E(
  "&ldquo;There&rsquo;s a lump in my thyroid&rdquo; &mdash; sometimes with diarrhoea or flushing, "
  "and sometimes a known family history.",
  "Palpate the thyroid and the cervical nodes. <b>Take a family history for multiple endocrine "
  "neoplasia</b> &mdash; and examine for its other components: <b>check blood pressure and ask "
  "about episodic sweating and palpitations for phaeochromocytoma</b>, and look for mucosal "
  "neuromas and a marfanoid habitus.",
  [("Papillary carcinoma", "Commoner, with nodal spread and characteristic cytology"),
   ("Anaplastic carcinoma", "Rapid growth in an older patient with compressive symptoms"),
   ("Parathyroid adenoma", "Hypercalcaemia rather than raised calcitonin")],
  "<b>Serum calcitonin</b> &rarr; markedly raised, and it is the tumour marker for follow-up. "
  "<b>Carcinoembryonic antigen</b> &rarr; also raised. <b>Fine needle aspiration</b> &rarr; "
  "amyloid stroma with spindle cells. <b>RET proto-oncogene testing</b> &rarr; a germline mutation, "
  "which triggers family screening.",
  "Normal calcitonin excludes it; <b>plasma metanephrines must be checked and a phaeochromocytoma "
  "excluded BEFORE any thyroid surgery</b> &mdash; operating first can be fatal. A negative RET "
  "test means sporadic disease."),

"Primary thyroid lymphoma": E(
  "&ldquo;My thyroid has grown quickly over a few weeks and it feels tight&rdquo; &mdash; often an "
  "older woman with known Hashimoto thyroiditis.",
  "Palpate a <b>rapidly enlarging, firm, diffuse goitre</b>. Assess for <b>stridor, tracheal "
  "deviation and compressive symptoms</b>. Palpate other nodal basins and the spleen. Check for "
  "hypothyroidism from the underlying thyroiditis.",
  [("Anaplastic carcinoma", "The critical distinction &mdash; same rapid growth, utterly different treatment"),
   ("Hashimoto thyroiditis", "The background condition; firm goitre but not rapidly growing"),
   ("Riedel thyroiditis", "Woody, fixed, fibrotic gland invading surrounding tissue")],
  "<b>CORE or OPEN biopsy</b> &rarr; lymphoma with immunohistochemistry to type it. <b>Fine needle "
  "aspiration is often insufficient</b>, because architecture matters. <b>Thyroid peroxidase "
  "antibodies</b> &rarr; raised, reflecting the Hashimoto background. <b>Staging imaging.</b>",
  "Anaplastic cytology on aspiration redirects to a very different pathway; <b>this distinction "
  "matters because lymphoma responds to chemotherapy and radiotherapy rather than surgery</b>; a "
  "stable goitre over years excludes it."),

"Leukoedema": E(
  "&ldquo;The inside of my cheeks looks greyish-white&rdquo; &mdash; usually noticed by a dentist, "
  "not the patient.",
  "Inspect the buccal mucosa bilaterally for a <b>diffuse grey-white filmy appearance</b>. "
  "<b>STRETCH the mucosa &mdash; the whiteness DISAPPEARS.</b> That single manoeuvre makes the "
  "diagnosis. Note that it is bilateral and symmetric.",
  [("Leukoplakia", "Does NOT disappear on stretching, and cannot be wiped off &mdash; and it is premalignant"),
   ("Oral candidiasis", "Wipes off leaving an erythematous base"),
   ("Lichen planus", "Lacy white striae in a defined pattern, often with erosions")],
  "<b>Clinical</b> &rarr; the whiteness resolving on stretching, bilateral and symmetric. "
  "<b>No biopsy is required.</b> It is a normal variant, commonest in darker-skinned individuals.",
  "Persistence on stretching means leukoplakia and warrants biopsy; a plaque that wipes off means "
  "candidiasis; unilateral or localised lesions are not leukoedema."),

"Fordyce granules": E(
  "&ldquo;There are little yellow spots inside my lip and cheek &mdash; are they normal?&rdquo;",
  "Inspect for <b>multiple small yellow-white papules on the buccal mucosa and vermilion "
  "border</b>. They are <b>painless, symmetric and do not ulcerate</b>. Palpate to confirm they are "
  "soft and superficial.",
  [("Oral candidiasis", "Wipes off; white rather than yellow, and often symptomatic"),
   ("Lichen planus", "Lacy striae rather than discrete papules"),
   ("Sebaceous hyperplasia or a small lipoma", "Discrete solitary lesion rather than a scattered field")],
  "<b>Clinical</b> &rarr; ectopic sebaceous glands, a normal variant present in most adults. "
  "<b>No investigation and no treatment are needed.</b>",
  "A lesion that wipes off is candida; anything ulcerating, growing or solitary is not a Fordyce "
  "granule and needs a closer look."),

"Physiologic pigmentation": E(
  "&ldquo;My gums have brown patches&rdquo; &mdash; usually long-standing and asymptomatic.",
  "Inspect for <b>symmetric brown pigmentation, most often on the attached gingiva</b>. <b>Confirm "
  "it is long-standing and stable</b> &mdash; that history does most of the work. Check for "
  "pigmentation elsewhere and review medications. <b>Note any single, growing or irregular lesion "
  "separately.</b>",
  [("Oral melanoma", "A single, irregular, growing pigmented lesion &mdash; rare but the reason to look carefully"),
   ("Smoker's melanosis", "Related to smoking and improves on cessation"),
   ("Addison disease or drug-induced pigmentation", "New, generalised, with systemic features or a culprit drug")],
  "<b>Clinical</b> &rarr; symmetric, stable, long-standing pigmentation, commonest in darker-skinned "
  "individuals. <b>Biopsy any lesion that is solitary, asymmetric, growing or newly appeared</b> "
  "&rarr; the histological diagnosis.",
  "<b>Morning cortisol and electrolytes</b> &rarr; excludes Addison disease if pigmentation is new "
  "and generalised; a medication review explains drug-induced change; benign histology excludes "
  "melanoma."),

"Aphthous stomatitis (canker sores)": E(
  "&ldquo;I keep getting painful ulcers in my mouth &mdash; they come and go and last about a "
  "week.&rdquo;",
  "Inspect for <b>shallow, round or oval ulcers with a grey-yellow base and an erythematous halo, "
  "on NON-KERATINISED mucosa</b> &mdash; buccal, labial, floor of mouth, not the hard palate or "
  "gingiva. Count and size them. <b>Look for genital ulcers and eye inflammation</b> before calling "
  "them simple.",
  [("Herpes simplex", "Vesicles first, on KERATINISED mucosa, clustered rather than solitary"),
   ("Behcet syndrome", "Oral ulcers PLUS genital ulcers and uveitis &mdash; the reason to ask"),
   ("Squamous cell carcinoma", "A single ulcer that does NOT heal in two weeks, with induration")],
  "<b>Clinical</b> &rarr; recurrent painful ulcers on non-keratinised mucosa healing within 7 to 14 "
  "days without scarring. <b>Full blood count, ferritin, folate, vitamin B12 and coeliac "
  "serology</b> if severe or frequent &rarr; a treatable deficiency or coeliac disease.",
  "<b>Any ulcer persisting beyond two weeks is biopsied to exclude carcinoma.</b> Vesicles on "
  "keratinised mucosa mean herpes; genital ulceration and eye disease redirect to Behcet syndrome."),

"Behcet syndrome": E(
  "&ldquo;I get mouth ulcers over and over, and I&rsquo;ve had sores on my genitals and trouble "
  "with my eyes.&rdquo;",
  "Inspect oral ulcers, then <b>examine the genitals and refer for a slit lamp examination of the "
  "eyes</b>. Look for skin lesions &mdash; erythema nodosum and pustules. <b>Pathergy test</b> "
  "&mdash; a needle prick producing a pustule at 24 to 48 hours. Examine joints and the nervous "
  "system.",
  [("Recurrent aphthous stomatitis", "Oral ulcers ALONE, with no genital, ocular or systemic disease"),
   ("Inflammatory bowel disease", "Oral ulcers with bowel symptoms rather than genital ulcers and uveitis"),
   ("Herpes simplex", "Vesicular, clustered, and it responds to antivirals")],
  "<b>Clinical criteria</b> &rarr; recurrent oral ulceration PLUS two of: recurrent genital "
  "ulceration, eye lesions, skin lesions, a positive pathergy test. <b>Slit lamp</b> &rarr; "
  "uveitis. <b>Inflammatory markers</b> &rarr; raised. There is no single confirmatory blood test.",
  "Isolated oral ulcers with no other system involved mean simple aphthous stomatitis; a positive "
  "viral swab means herpes; bowel investigation identifies inflammatory bowel disease instead."),

"Oral lichen planus": E(
  "&ldquo;There are white lacy lines inside my cheeks, and lately eating spicy food burns.&rdquo;",
  "Inspect for <b>Wickham striae &mdash; lacy white lines, usually BILATERAL on the buccal "
  "mucosa</b>. Note whether it is reticular (asymptomatic) or <b>erosive (painful, and the form "
  "that carries malignant risk)</b>. Examine skin, nails, scalp and genitals. Review medications "
  "for a lichenoid reaction.",
  [("Leukoplakia", "A homogeneous white patch without striae; also premalignant"),
   ("Candidiasis", "Wipes off; may also be superimposed on lichen planus"),
   ("Lichenoid drug reaction", "Looks identical &mdash; the medication history is what separates them")],
  "<b>Biopsy</b> &rarr; a <b>band-like lymphocytic infiltrate at the basement membrane with basal "
  "cell degeneration</b>. Direct immunofluorescence helps exclude the blistering diseases. Reticular "
  "disease with classic striae may be diagnosed clinically.",
  "A plaque that wipes off with hyphae on microscopy is candida; resolution after stopping a drug "
  "means a lichenoid reaction; <b>dysplasia on biopsy changes it from a chronic condition to a "
  "premalignant one and mandates surveillance</b>."),

"Systemic lupus erythematosus &mdash; oral": E(
  "&ldquo;I have ulcers on the roof of my mouth that don&rsquo;t hurt, and I&rsquo;ve been tired "
  "with sore joints and a rash.&rdquo;",
  "Inspect for <b>painless ulcers, characteristically on the HARD PALATE</b> &mdash; the painless "
  "quality and the palatal site are both unusual. Look for a malar rash and photosensitivity. "
  "Examine joints. Check blood pressure and look for signs of renal disease.",
  [("Aphthous ulcers", "PAINFUL and on non-keratinised mucosa &mdash; the opposite on both counts"),
   ("Lichen planus", "Lacy striae with a different distribution"),
   ("Herpes simplex", "Vesicular and painful, on keratinised mucosa")],
  "<b>Antinuclear antibody</b> &rarr; positive, the screening test. <b>Anti-double-stranded DNA and "
  "anti-Smith</b> &rarr; specific for lupus. <b>Complement C3 and C4</b> &rarr; low in active "
  "disease. <b>Full blood count</b> &rarr; cytopenias. <b>Urinalysis</b> &rarr; protein and casts "
  "in renal involvement.",
  "A negative antinuclear antibody makes lupus very unlikely; painful ulcers on non-keratinised "
  "mucosa with no systemic features mean aphthous stomatitis; a positive viral swab means herpes."),

"Herpes simplex ulcers": E(
  "&ldquo;I got a tingle first, then blisters that broke into ulcers &mdash; it happens whenever "
  "I&rsquo;m run down.&rdquo;",
  "Inspect for <b>clustered vesicles that rupture into shallow ulcers on KERATINISED mucosa</b> "
  "&mdash; hard palate, attached gingiva, vermilion border. <b>Primary infection gives a "
  "gingivostomatitis with fever</b>; recurrences are localised. Palpate for tender nodes. Check "
  "immune status if severe.",
  [("Aphthous ulcers", "NON-keratinised mucosa, no vesicles, no prodrome"),
   ("Herpangina or hand-foot-and-mouth", "Posterior oropharynx, in children, with a different pattern"),
   ("Erythema multiforme", "Target lesions on the skin with widespread mucosal erosions")],
  "<b>Clinical</b> &rarr; the prodrome, vesicles and site. <b>Polymerase chain reaction of a swab "
  "from a deroofed vesicle</b> &rarr; herpes simplex virus, and it is the most sensitive test. "
  "<b>Tzanck smear</b> &rarr; multinucleated giant cells, but it does not distinguish herpes "
  "simplex from varicella zoster.",
  "A negative polymerase chain reaction from a fresh vesicle excludes it; ulcers on non-keratinised "
  "mucosa without vesicles are aphthous; target lesions redirect to erythema multiforme."),

"Acute suppurative sialadenitis": E(
  "&ldquo;My cheek swelled up quickly, it&rsquo;s hot and painful, and there&rsquo;s a foul taste "
  "in my mouth.&rdquo; Often an elderly, dehydrated or postoperative patient.",
  "Palpate the gland for a <b>tender, warm, indurated swelling</b>. <b>Milk the duct &mdash; "
  "Stensen duct opposite the second upper molar for parotid, Wharton duct in the floor of mouth for "
  "submandibular &mdash; and look for PUS at the orifice.</b> That expressed pus is the finding. "
  "Assess hydration, trismus and the airway. <b>Check cranial nerve VII.</b>",
  [("Sialolithiasis", "Swelling that comes on WITH MEALS and settles between them, without pus"),
   ("Mumps parotitis", "Bilateral, viral, in an unvaccinated patient, with no purulent discharge"),
   ("Parotid neoplasm", "Painless, firm, progressive &mdash; and facial weakness means malignancy")],
  "<b>Milking the duct</b> &rarr; frank pus, which confirms it. <b>Culture</b> &rarr; usually "
  "<i>Staphylococcus aureus</i>. <b>Ultrasound or contrast computed tomography</b> &rarr; an "
  "abscess needing drainage, or a stone. <b>Avoid sialography in acute infection.</b>",
  "Clear saliva on milking with meal-related swelling means a stone; bilateral swelling without pus "
  "suggests mumps &mdash; <b>viral serology or polymerase chain reaction</b> confirms it; a "
  "painless progressive mass needs imaging and cytology for tumour."),

"Sialolithiasis": E(
  "&ldquo;Whenever I start to eat, my gland under the jaw swells up and aches &mdash; then it goes "
  "down again.&rdquo;",
  "<b>Bimanual palpation along the floor of the mouth</b>, back to front, to feel a stone in "
  "Wharton duct. <b>Milk the duct and observe the saliva</b> &mdash; reduced or absent flow rather "
  "than pus. Note the meal-related pattern. Palpate the gland for size and tenderness.",
  [("Acute suppurative sialadenitis", "Constant pain with PUS at the duct, not meal-related swelling"),
   ("Salivary neoplasm", "Painless, persistent, progressive &mdash; it does not fluctuate with meals"),
   ("Duct stricture", "The same obstructive pattern without a palpable stone")],
  "<b>Ultrasound</b> &rarr; an echogenic focus with acoustic shadowing, the first-line test. "
  "<b>Non-contrast computed tomography</b> &rarr; a radiopaque calculus; <b>about 80% of "
  "submandibular stones are radiopaque</b>. <b>Sialendoscopy</b> &rarr; direct visualisation, and "
  "it can treat at the same time.",
  "Pus at the duct redirects to acute infection; a persistent mass with no stone on imaging needs "
  "cytology for neoplasm; a stricture on sialendoscopy explains obstruction without a stone."),

"Parotitis": E(
  "&ldquo;Both sides of my face are swollen in front of my ears and it hurts to chew.&rdquo;",
  "Inspect for swelling that <b>obscures the angle of the mandible and lifts the earlobe outward "
  "and upward</b> &mdash; that is what makes it parotid rather than nodal. Palpate for tenderness. "
  "<b>Milk Stensen duct</b>. <b>Check cranial nerve VII.</b> Ask about immunisation and contacts, "
  "and examine the testes in a male.",
  [("Suppurative parotitis", "Unilateral with PUS from the duct"),
   ("Cervical lymphadenopathy", "Discrete nodes that do not lift the earlobe or obscure the mandibular angle"),
   ("Parotid neoplasm", "A discrete firm mass rather than diffuse gland swelling")],
  "<b>Clinical</b> &rarr; diffuse bilateral parotid swelling with the earlobe lifted. <b>Mumps "
  "polymerase chain reaction on a buccal swab, with immunoglobulin M serology</b> &rarr; confirms "
  "mumps. <b>Serum amylase</b> &rarr; raised from salivary origin. <b>Ultrasound</b> &rarr; "
  "distinguishes diffuse gland inflammation from a discrete mass or abscess.",
  "Pus on milking the duct means bacterial infection; a discrete mass on ultrasound needs aspiration "
  "for tumour; <b>facial nerve weakness is never inflammatory parotitis and points to malignancy</b>."),
}
