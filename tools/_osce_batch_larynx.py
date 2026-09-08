# -*- coding: utf-8 -*-
from _pd2_ent_osce_data import E
BATCH = {

"Vocal cord nodules": E(
  "&ldquo;I&rsquo;m a teacher and my voice is hoarse by the end of every day &mdash; it&rsquo;s "
  "been months.&rdquo;",
  "Listen to voice quality and how it changes with use. <b>Ask about vocal demand and abuse: "
  "shouting, singing, professional voice use, smoking, reflux.</b> Palpate the neck. <b>Any "
  "hoarseness beyond two to three weeks gets the larynx VISUALISED</b> &mdash; that rule is what "
  "the station is testing.",
  [("Vocal cord polyp", "Usually UNILATERAL and often follows a single vocal injury"),
   ("Laryngeal carcinoma", "The reason hoarseness is never watched indefinitely &mdash; smoker, weight loss, otalgia"),
   ("Reflux laryngitis", "Diffuse posterior erythema and oedema without discrete lesions")],
  "<b>Laryngoscopy, flexible or with videostroboscopy</b> &rarr; <b>BILATERAL, symmetric lesions "
  "at the junction of the anterior and middle thirds</b> of the cords &mdash; that symmetry and "
  "site name them. Stroboscopy shows the mucosal wave impairment.",
  "A unilateral lesion is a polyp or a tumour, not a nodule; <b>an irregular, ulcerated or fixed "
  "cord goes to biopsy</b>; improvement with voice therapy alone supports the diagnosis."),

"Vocal cord polyps": E(
  "&ldquo;My voice went hoarse after I screamed at a match and it hasn&rsquo;t come back.&rdquo;",
  "Assess voice quality &mdash; often breathy and rough. Take the history of a single vocal event, "
  "smoking and reflux. <b>Visualise the larynx.</b> Palpate the neck for nodes.",
  [("Vocal cord nodules", "Bilateral and symmetric, from chronic rather than single abuse"),
   ("Laryngeal carcinoma", "Irregular, ulcerated, may fix the cord &mdash; must be excluded"),
   ("Reinke oedema", "Diffuse fusiform swelling of both cords in a smoker, not a discrete polyp")],
  "<b>Laryngoscopy with stroboscopy</b> &rarr; a <b>UNILATERAL, often pedunculated lesion</b> on "
  "the free edge of the cord. <b>Histology after excision</b> &rarr; benign, and it excludes "
  "carcinoma at the same time.",
  "Bilateral symmetric lesions mean nodules; diffuse cord swelling in a smoker means Reinke oedema; "
  "<b>benign histology is what formally excludes malignancy</b>, which clinical appearance alone "
  "cannot do."),

"Vocal cord papillomatosis": E(
  "A parent says &ldquo;his voice has been hoarse for months and now he makes a noise when he "
  "breathes.&rdquo; In adults, persistent hoarseness.",
  "Assess voice and <b>listen for STRIDOR &mdash; airway obstruction is the danger</b>. Visualise "
  "the larynx. Note that it <b>recurs after removal</b>. Ask about maternal history in a child.",
  [("Vocal cord nodules", "Smooth and symmetric; no airway compromise or recurrence"),
   ("Laryngeal carcinoma", "In adults, and papillomatosis can undergo malignant transformation"),
   ("Croup", "Acute, with a barking cough, rather than months of hoarseness")],
  "<b>Laryngoscopy</b> &rarr; <b>exophytic, wart-like, cauliflower lesions</b> on the cords and "
  "supraglottis. <b>Biopsy with human papillomavirus typing</b> &rarr; types 6 and 11 most often, "
  "and it excludes carcinoma.",
  "A smooth symmetric pair of lesions means nodules; <b>dysplasia or invasion on histology means "
  "malignant transformation</b> and changes management; an acute barking cough is croup, not this."),

"Vocal cord paralysis": E(
  "&ldquo;My voice is breathy and weak, and I cough when I drink.&rdquo; &mdash; often after neck "
  "or chest surgery.",
  "Assess voice and <b>test the cough &mdash; a weak, breathy cough suggests glottic "
  "incompetence</b>. Watch for aspiration on swallowing. <b>Listen for stridor, which means "
  "BILATERAL paralysis and an airway emergency.</b> Full cranial nerve examination. Palpate thyroid "
  "and neck; look for surgical scars.",
  [("Laryngeal carcinoma", "Fixes the cord mechanically rather than by nerve injury"),
   ("Cricoarytenoid joint fixation", "Cord immobile from the joint, not the nerve &mdash; separated at endoscopy"),
   ("Functional dysphonia", "Normal cord movement on examination despite an abnormal voice")],
  "<b>Laryngoscopy</b> &rarr; an <b>immobile cord, and whether it is unilateral or bilateral</b>. "
  "<b>Computed tomography from SKULL BASE to MEDIASTINUM</b> &rarr; a lesion anywhere along the "
  "recurrent laryngeal nerve; <b>the left nerve loops under the aortic arch, so the chest must be "
  "included</b>. <b>Thyroid ultrasound and function tests.</b>",
  "Normal cord movement excludes paralysis and suggests a functional cause; palpation of the "
  "arytenoid at endoscopy separates fixation from paralysis; a normal scan along the whole nerve "
  "course means idiopathic or postviral paralysis."),

"Acute laryngitis": E(
  "&ldquo;I lost my voice with this cold &mdash; it&rsquo;s been a few days.&rdquo;",
  "Assess voice and listen for <b>stridor, which would mean something more serious</b>. Examine the "
  "pharynx. Check for fever and lower respiratory signs. <b>Note the duration &mdash; under three "
  "weeks is the point.</b>",
  [("Chronic laryngitis", "Beyond three weeks, and it requires visualisation"),
   ("Epiglottitis", "Severe odynophagia, drooling, toxicity &mdash; the emergency to exclude"),
   ("Laryngeal carcinoma", "Persistent hoarseness with risk factors; excluded by time course here")],
  "<b>Clinical</b> &rarr; hoarseness with an upper respiratory infection, resolving within one to "
  "three weeks. <b>No investigation is needed if it settles.</b> Laryngoscopy if it does not.",
  "Drooling and severe odynophagia redirect urgently to supraglottitis; <b>hoarseness persisting "
  "beyond three weeks means laryngoscopy, which is what excludes carcinoma</b>; stridor changes the "
  "priority to the airway."),

"Chronic laryngitis": E(
  "&ldquo;My voice has been rough for a couple of months &mdash; I smoke and I get a lot of "
  "heartburn.&rdquo;",
  "Assess voice quality. <b>Take the risk factor history: smoking, alcohol, reflux, vocal abuse, "
  "inhaled corticosteroids.</b> <b>Palpate the neck for nodes</b> and ask about otalgia, weight "
  "loss and dysphagia. <b>Visualise the larynx &mdash; this is not optional at this duration.</b>",
  [("Laryngeal carcinoma", "The diagnosis this workup exists to exclude, in exactly this patient"),
   ("Reflux laryngitis", "Posterior erythema, oedema and granuloma with reflux symptoms"),
   ("Vocal cord lesions", "Discrete nodules or polyps rather than diffuse inflammation")],
  "<b>Laryngoscopy</b> &rarr; diffuse erythema and oedema WITHOUT a discrete mass, ulceration or "
  "cord fixation. <b>Biopsy of any suspicious area</b> &rarr; the histology, which is what settles "
  "it. Consider reflux testing.",
  "<b>A mass, ulcer or immobile cord means carcinoma until biopsy says otherwise</b>; discrete "
  "bilateral lesions at the anterior third mean nodules; improvement on antireflux therapy supports "
  "reflux laryngitis."),

"Viral pharyngitis": E(
  "&ldquo;My throat is sore, I&rsquo;ve got a cough and a runny nose.&rdquo;",
  "Inspect the pharynx for diffuse erythema, usually WITHOUT exudate. <b>Palpate anterior cervical "
  "nodes.</b> Check for fever. <b>Note the presence of cough, rhinorrhoea and hoarseness &mdash; "
  "these point AWAY from streptococcal infection.</b> Palpate the spleen if fatigue is prominent.",
  [("Streptococcal pharyngitis", "Exudate, tender anterior nodes, fever, and NO cough"),
   ("Infectious mononucleosis", "Posterior nodes, marked fatigue, splenomegaly, palatal petechiae"),
   ("Peritonsillar abscess", "Unilateral with trismus and uvular deviation")],
  "<b>Clinical</b> &rarr; sore throat with cough and coryza, and a <b>low Centor score</b>. "
  "<b>Rapid antigen test</b> if streptococcal disease is plausible &rarr; negative supports viral "
  "aetiology.",
  "<b>Centor criteria &mdash; fever, tonsillar exudate, tender anterior nodes, ABSENCE of cough</b> "
  "&mdash; score the likelihood; a positive rapid antigen or throat culture redirects to bacterial "
  "disease; a positive monospot with atypical lymphocytes means mononucleosis."),

"Bacterial pharyngitis (GABHS)": E(
  "&ldquo;My throat is agony to swallow, I&rsquo;ve got a fever, and I have NO cough.&rdquo;",
  "Inspect for <b>tonsillar erythema with exudate and palatal petechiae</b>. <b>Palpate tender "
  "ANTERIOR cervical nodes.</b> Measure temperature. <b>Apply the Centor criteria.</b> Check for "
  "trismus and uvular deviation, which would mean an abscess. Look for a scarlatiniform rash.",
  [("Viral pharyngitis", "Cough, coryza and hoarseness present; low Centor score"),
   ("Infectious mononucleosis", "POSTERIOR nodes and splenomegaly; giving amoxicillin causes a rash"),
   ("Peritonsillar abscess", "Unilateral, with trismus, uvular deviation and a muffled voice")],
  "<b>Rapid antigen detection test</b> &rarr; positive confirms it; <b>a NEGATIVE test in a child "
  "is backed up by throat culture</b>, which is the gold standard. <b>Centor score of 3 or 4</b> "
  "supports testing and treating.",
  "A positive monospot with atypical lymphocytes means mononucleosis &mdash; <b>and this matters "
  "because aminopenicillins cause a florid rash there</b>; cough and coryza suggest viral disease; "
  "trismus with uvular deviation redirects to quinsy."),

"Rheumatic fever": E(
  "&ldquo;A few weeks after a bad sore throat, my joints started hurting and moving from one to "
  "another, and I get short of breath.&rdquo;",
  "<b>Auscultate the heart carefully for a NEW murmur and a rub</b> &mdash; carditis is what causes "
  "lasting harm. Examine joints for a <b>MIGRATORY</b> arthritis. Look for <b>subcutaneous "
  "nodules over extensor surfaces and erythema marginatum on the trunk</b>. <b>Observe for "
  "Sydenham chorea.</b>",
  [("Septic arthritis", "One hot joint that does not migrate; aspiration settles it"),
   ("Juvenile idiopathic arthritis", "Persistent rather than migratory, without the preceding sore throat"),
   ("Reactive arthritis", "Follows a gastrointestinal or genitourinary infection instead")],
  "<b>Jones criteria</b> &rarr; two major, or one major plus two minor, WITH <b>evidence of "
  "preceding streptococcal infection: raised or rising antistreptolysin O titre</b> or a positive "
  "culture. <b>Echocardiography</b> &rarr; valvular regurgitation, most often mitral. "
  "<b>Electrocardiogram</b> &rarr; a prolonged PR interval. <b>Inflammatory markers</b> &rarr; raised.",
  "<b>No evidence of preceding streptococcal infection makes the diagnosis untenable</b> &mdash; "
  "that requirement is what excludes the mimics; joint aspiration excludes sepsis; a normal "
  "echocardiogram excludes carditis but not the diagnosis."),

"Chronic pharyngitis": E(
  "&ldquo;My throat feels scratchy and irritated all the time &mdash; it&rsquo;s been like this for "
  "months.&rdquo;",
  "Inspect the pharynx for diffuse erythema, granularity or <b>cobblestoning of the posterior "
  "wall</b>. <b>Look for the driver: postnasal drip, reflux, smoking, mouth breathing, dry "
  "environment.</b> Examine the nose. Palpate the neck. <b>Ask about the red flags &mdash; weight "
  "loss, otalgia, dysphagia, a neck mass.</b>",
  [("Laryngopharyngeal reflux", "Posterior laryngeal erythema and oedema with throat clearing"),
   ("Allergic rhinitis with postnasal drip", "Nasal itch, sneezing, boggy turbinates"),
   ("Oropharyngeal carcinoma", "The red-flag diagnosis &mdash; a persistent unilateral lesion or ulcer")],
  "<b>Clinical</b> &rarr; persistent symptoms with a diffusely irritated pharynx and an "
  "identifiable irritant. <b>Nasal endoscopy or laryngoscopy</b> if it persists or red flags "
  "appear &rarr; the underlying source, and it excludes a tumour.",
  "<b>Any persistent unilateral lesion or ulcer goes to biopsy</b>; response to antireflux measures "
  "supports reflux; treating rhinitis and seeing the throat settle confirms postnasal drip."),

"Infectious mononucleosis": E(
  "&ldquo;I&rsquo;ve had a sore throat for two weeks and I&rsquo;m exhausted &mdash; I can barely "
  "get out of bed.&rdquo;",
  "Inspect for <b>large tonsils with exudate and palatal petechiae</b>. <b>Palpate POSTERIOR "
  "cervical nodes</b> &mdash; the distribution is a real discriminator. <b>Palpate for "
  "splenomegaly, gently.</b> Check for hepatomegaly, jaundice and a rash. <b>Assess the airway if "
  "the tonsils are very large.</b>",
  [("Streptococcal pharyngitis", "Anterior nodes, no splenomegaly, shorter course"),
   ("Cytomegalovirus infection", "A very similar illness with a NEGATIVE monospot"),
   ("Acute HIV seroconversion", "Also mononucleosis-like &mdash; and it must be considered")],
  "<b>Monospot (heterophile antibody)</b> &rarr; positive, though <b>often falsely negative in the "
  "first week</b> and in young children. <b>Full blood count with film</b> &rarr; lymphocytosis "
  "with <b>atypical lymphocytes</b>. <b>Epstein-Barr specific serology</b> &rarr; confirms when the "
  "monospot is negative. <b>Liver function tests</b> &rarr; raised transaminases.",
  "A negative monospot with a compatible illness means sending Epstein-Barr serology, "
  "cytomegalovirus testing and <b>HIV testing</b>; a positive rapid streptococcal test explains a "
  "different illness. <b>Avoid aminopenicillins &mdash; they cause a florid rash here.</b>"),

"Oral candidiasis (thrush)": E(
  "&ldquo;I&rsquo;ve got white patches in my mouth and things taste odd&rdquo; &mdash; often after "
  "antibiotics or in an inhaler user.",
  "Inspect for <b>creamy white plaques</b>. <b>SCRAPE one with a tongue depressor &mdash; it "
  "comes off, leaving an erythematous, sometimes bleeding base.</b> That is the diagnostic "
  "manoeuvre. Examine denture-bearing areas and the angles of the mouth. <b>Ask why: inhaled "
  "steroids, antibiotics, diabetes, immunosuppression.</b>",
  [("Leukoplakia", "Does NOT scrape off &mdash; and it is premalignant"),
   ("Lichen planus", "Lacy striae that do not wipe away"),
   ("Hairy leukoplakia", "On the LATERAL TONGUE, does not scrape off, marks immunosuppression")],
  "<b>Clinical</b> &rarr; plaques that wipe off with an erythematous base. <b>Potassium hydroxide "
  "preparation or a swab</b> &rarr; <b>budding yeasts and pseudohyphae</b>. <b>Blood glucose and "
  "HIV testing</b> if there is no obvious cause &rarr; the underlying reason.",
  "A plaque that will not scrape off is leukoplakia and needs biopsy; lacy striae mean lichen "
  "planus; <b>unexplained thrush in an adult is a reason to look for immunosuppression, not just "
  "to prescribe an antifungal</b>."),

"Cervical adenitis": E(
  "&ldquo;My child has a fever and a swollen, tender lump on the side of the neck.&rdquo;",
  "Palpate for <b>size, tenderness, warmth, mobility and FLUCTUANCE</b>. <b>Search for the primary "
  "source: teeth, tonsils, ears, scalp, skin.</b> Assess trismus, torticollis, drooling and the "
  "airway &mdash; those signal deep neck extension. Palpate other nodal groups and the spleen.",
  [("Deep neck space abscess", "Trismus, torticollis, toxicity &mdash; the escalation to exclude"),
   ("Reactive viral adenopathy", "Multiple small mobile nodes, minimal tenderness, no fever"),
   ("Malignancy", "Hard, fixed, painless, progressive, or supraclavicular")],
  "<b>Clinical</b> &rarr; a tender enlarged node with an identified source. <b>Ultrasound</b> "
  "&rarr; a <b>solid inflamed node versus a hypoechoic collection</b>, which is the decision that "
  "matters. <b>Contrast computed tomography</b> if deep extension is suspected &rarr; a "
  "rim-enhancing abscess. <b>Full blood count and inflammatory markers.</b>",
  "A solid node without a collection is treated with antibiotics rather than drained; <b>a node "
  "that fails to settle in 4 to 6 weeks, or is hard and fixed, goes to aspiration or biopsy for "
  "malignancy</b>; mycobacterial studies if it becomes chronic."),

"Dental abscess": E(
  "&ldquo;This tooth has been killing me and now my face is swollen.&rdquo;",
  "<b>Percuss the suspect tooth &mdash; exquisite tenderness localises it.</b> Inspect for gingival "
  "swelling, a sinus tract, and caries. <b>Assess the floor of mouth, trismus, and the airway</b> "
  "&mdash; spread is the danger. Palpate cervical nodes. Check temperature.",
  [("Ludwig angina", "Bilateral firm floor-of-mouth elevation with tongue displacement &mdash; the emergency"),
   ("Periodontal abscess", "Arises from the periodontal pocket, tooth usually still vital"),
   ("Sialadenitis", "Gland swelling with pus at the duct, not tooth-related")],
  "<b>Clinical</b> &rarr; a percussion-tender tooth with localised swelling. <b>Periapical or "
  "panoramic radiograph</b> &rarr; a <b>radiolucency at the tooth apex</b>. <b>Contrast computed "
  "tomography</b> if there is facial swelling or trismus &rarr; the extent of spread and any deep "
  "space collection.",
  "<b>Raised, firm floor of mouth means Ludwig angina and a different urgency entirely</b>; pus "
  "from a salivary duct redirects to sialadenitis; a vital tooth with a pocket suggests periodontal "
  "rather than periapical origin."),

"Gingivitis and periodontitis": E(
  "&ldquo;My gums bleed when I brush and my breath is bad.&rdquo; Later, &ldquo;my teeth feel "
  "loose.&rdquo;",
  "Inspect gingivae for erythema, oedema and <b>bleeding on gentle probing</b>. <b>Assess tooth "
  "MOBILITY and look for gingival recession</b> &mdash; those separate periodontitis from "
  "gingivitis. Note plaque and calculus. <b>Ask about diabetes, smoking and medications</b> such as "
  "phenytoin and calcium channel blockers.",
  [("Necrotising ulcerative gingivitis", "Punched-out interdental papillae with severe pain and fetor"),
   ("Leukaemic gingival infiltration", "Boggy hypertrophied gums with bruising and systemic illness"),
   ("Drug-induced gingival hyperplasia", "Overgrowth linked to a specific medication")],
  "<b>Clinical with periodontal probing</b> &rarr; <b>gingivitis is inflammation with NO attachment "
  "loss and is REVERSIBLE; periodontitis shows pocket depths over 3 millimetres with attachment "
  "loss and is NOT</b>. <b>Dental radiographs</b> &rarr; alveolar bone loss confirming "
  "periodontitis. <b>Blood glucose and HbA1c.</b>",
  "Absence of pocketing and bone loss means gingivitis alone; <b>full blood count</b> &rarr; "
  "excludes leukaemia if the gums are boggy and the patient is unwell; a medication review "
  "explains drug-induced overgrowth."),

"Dental caries, pulpitis and periapical abscess": E(
  "Early: &ldquo;it&rsquo;s sensitive to cold but it settles quickly.&rdquo; Later: &ldquo;it "
  "throbs at night and keeps me awake.&rdquo;",
  "Inspect teeth for cavitation and discolouration. <b>Percussion tenderness</b> and <b>thermal "
  "testing</b> &mdash; <b>reversible pulpitis settles within seconds of removing the stimulus; "
  "irreversible pulpitis lingers and throbs</b>. Assess mobility, swelling and any sinus tract. "
  "Check trismus and the airway.",
  [("Reversible pulpitis", "Brief pain on stimulus only &mdash; the tooth is savable with a filling"),
   ("Irreversible pulpitis", "Lingering spontaneous pain &mdash; needs root canal treatment or extraction"),
   ("Periapical abscess", "Percussion tenderness with swelling and an apical radiolucency")],
  "<b>Thermal and percussion testing</b> &rarr; which stage it is, and therefore which treatment. "
  "<b>Periapical radiograph</b> &rarr; the carious lesion's depth and an <b>apical radiolucency</b> "
  "once an abscess has formed. Vitality testing &rarr; a non-vital tooth.",
  "A tooth responding briefly and normally to cold is reversible pulpitis, not an abscess; no "
  "apical radiolucency argues against a periapical collection; facial swelling with trismus means "
  "imaging for spread rather than another radiograph."),

"Impacted teeth": E(
  "&ldquo;My back gum is sore and swollen and I can&rsquo;t open my mouth properly&rdquo; &mdash; "
  "typically a young adult with wisdom teeth.",
  "Inspect the retromolar area for an <b>operculum &mdash; a flap of gum over a partially erupted "
  "tooth &mdash; with erythema and pus</b>. <b>Measure mouth opening.</b> Palpate for swelling and "
  "cervical nodes. <b>Assess the floor of mouth and the airway if swelling is significant.</b>",
  [("Pericoronitis", "Infection around the operculum &mdash; the usual complication"),
   ("Dental abscess", "Arises from a carious tooth with apical rather than pericoronal swelling"),
   ("Dentigerous cyst", "A painless expanding radiolucency around an unerupted crown")],
  "<b>Panoramic radiograph</b> &rarr; the <b>impacted tooth, its angulation, and its relation to "
  "the inferior alveolar canal</b> &mdash; that relation is what the surgeon plans around. It also "
  "shows any associated cyst.",
  "An apical radiolucency on a carious tooth means a periapical abscess instead; a well-defined "
  "pericoronal radiolucency over 3 millimetres suggests a dentigerous cyst; trismus with a raised "
  "floor of mouth means spread and changes urgency."),

"Malocclusion": E(
  "&ldquo;My teeth don&rsquo;t meet properly and it&rsquo;s hard to chew&rdquo; &mdash; or the "
  "concern is entirely about appearance.",
  "<b>Ask the patient to bite together and inspect the relationship of the molars and incisors.</b> "
  "Note overjet, overbite, crossbite and crowding. <b>Assess jaw opening and listen for "
  "temporomandibular joint clicking.</b> Check for mouth breathing and tongue thrust. Examine "
  "facial symmetry.",
  [("Temporomandibular joint disorder", "Pain, clicking and limited opening; often coexists"),
   ("Skeletal jaw discrepancy", "The mismatch is in the bones, not just the teeth &mdash; it changes the treatment"),
   ("Acquired malocclusion after fracture", "A traumatic history with a sudden change in bite")],
  "<b>Clinical bite assessment</b> &rarr; the Angle classification: <b>class I normal molar "
  "relationship, class II retrognathic, class III prognathic</b>. <b>Panoramic and cephalometric "
  "radiographs</b> &rarr; whether the discrepancy is dental or skeletal, which decides braces "
  "versus surgery. Study models.",
  "<b>A SUDDEN change in bite after trauma means a mandibular or maxillary fracture and needs "
  "computed tomography</b>, not an orthodontic referral; cephalometric analysis separates skeletal "
  "from dental causes; joint imaging addresses the temporomandibular component."),

"Temporomandibular joint disorders": E(
  "&ldquo;My jaw clicks and aches, especially in the morning, and sometimes it locks.&rdquo;",
  "<b>Palpate the joint just anterior to the tragus while the patient opens and closes</b>, and "
  "palpate the masseter and temporalis for tenderness. <b>Measure maximal opening &mdash; under "
  "about 40 millimetres is restricted.</b> <b>Note clicking, crepitus and deviation of the jaw on "
  "opening.</b> Examine the bite and check for bruxism wear facets. <b>Examine the ear, which is "
  "normal &mdash; this is a common cause of referred otalgia.</b>",
  [("Otitis media or externa", "Ear pain with an ABNORMAL ear examination; here the ear is normal"),
   ("Dental pathology", "A percussion-tender tooth localises the pain"),
   ("Giant cell arteritis", "Jaw CLAUDICATION on chewing in an older patient, with scalp tenderness")],
  "<b>Clinical</b> &rarr; joint or muscle tenderness with clicking, deviation and restricted "
  "opening. <b>Imaging is not routine</b>; <b>magnetic resonance</b> if it persists &rarr; disc "
  "displacement; <b>computed tomography</b> &rarr; degenerative or bony change.",
  "An abnormal ear examination redirects to ear disease; a percussion-tender tooth means dental "
  "pain; <b>in a patient over 50 with jaw pain on chewing, inflammatory markers to exclude giant "
  "cell arteritis</b> &mdash; missing that costs vision."),

"Oral leukoplakia": E(
  "&ldquo;There&rsquo;s a white patch in my mouth&rdquo; &mdash; usually painless and often found "
  "by a dentist.",
  "Inspect and <b>palpate the lesion &mdash; induration is worrying</b>. <b>Attempt to scrape it: "
  "it does NOT come off</b>, which is the definitional feature. Note site &mdash; <b>floor of "
  "mouth and ventral tongue carry the highest risk</b>. <b>Note whether it is homogeneous or "
  "SPECKLED</b>, the speckled form being far more dangerous. Take a tobacco and alcohol history and "
  "palpate the neck.",
  [("Candidiasis", "Wipes off, leaving an erythematous base"),
   ("Lichen planus", "Lacy striae rather than a homogeneous patch"),
   ("Squamous cell carcinoma", "Induration, ulceration or a mass &mdash; what the biopsy is looking for")],
  "<b>Clinical definition</b> &rarr; a white patch that cannot be wiped off and cannot be given "
  "another diagnosis &mdash; it is a diagnosis of EXCLUSION. <b>BIOPSY</b> &rarr; hyperkeratosis, "
  "dysplasia, or invasive carcinoma; <b>the degree of dysplasia is what determines management</b>.",
  "A patch that wipes off with yeasts on microscopy is candidiasis &mdash; and <b>a trial of "
  "antifungal treatment is a reasonable first step, but persistence means biopsy</b>; lacy striae "
  "mean lichen planus; benign hyperkeratosis excludes malignancy for now but not surveillance."),

"Hairy leukoplakia": E(
  "&ldquo;The side of my tongue has gone white and ridged&rdquo; &mdash; painless, and in a patient "
  "who may not know they are immunocompromised.",
  "Inspect the <b>LATERAL border of the tongue for white corrugated or hairy vertical folds</b>. "
  "<b>Attempt to scrape &mdash; it does NOT come off</b>, unlike candida. Examine for other markers "
  "of immunosuppression: candidiasis, Kaposi sarcoma, adenopathy, wasting. <b>Take a risk history.</b>",
  [("Oral candidiasis", "Wipes off; may coexist on top of it"),
   ("Leukoplakia", "Any site, and it is premalignant &mdash; hairy leukoplakia is not"),
   ("Lichen planus", "Lacy striae, usually bilateral buccal, with a different appearance")],
  "<b>Clinical appearance and site</b> &rarr; strongly suggestive. <b>Biopsy with Epstein-Barr "
  "virus testing</b> &rarr; the virus in epithelial cells, confirming it. <b>HIV testing with CD4 "
  "count</b> &rarr; the underlying immunosuppression, which is the real finding.",
  "A plaque that wipes off is candida; <b>the essential next step is not treating the tongue but "
  "testing for immunosuppression</b> &mdash; hairy leukoplakia is a marker, not a disease in its "
  "own right; it is not premalignant, which separates it from leukoplakia."),

"Salivary gland neoplasm": E(
  "&ldquo;There&rsquo;s a painless lump in front of my ear that&rsquo;s been slowly growing.&rdquo;",
  "Palpate the mass for <b>size, consistency, mobility and FIXATION</b>. <b>Test cranial nerve VII "
  "&mdash; facial weakness means malignancy until proven otherwise.</b> <b>Palpate cervical "
  "nodes.</b> Examine the mouth and the parapharyngeal space bimanually. Note pain, which also "
  "suggests malignancy. <b>Remember the rule: the SMALLER the gland, the HIGHER the chance the "
  "tumour is malignant.</b>",
  [("Pleomorphic adenoma", "The commonest, benign, mobile and painless &mdash; but it can transform"),
   ("Warthin tumour", "Benign, often bilateral, in older male smokers"),
   ("Mucoepidermoid or adenoid cystic carcinoma", "Fixed, painful, with facial weakness or nodes")],
  "<b>Ultrasound</b> &rarr; a solid mass and its position relative to the facial nerve plane. "
  "<b>Fine needle aspiration</b> &rarr; the cell type. <b>Magnetic resonance</b> &rarr; deep lobe "
  "extension and perineural spread &mdash; <b>adenoid cystic carcinoma spreads along nerves</b>. "
  "<b>Definitive histology comes from excision.</b>",
  "<b>Incisional biopsy is avoided in the parotid &mdash; it seeds tumour and risks the facial "
  "nerve</b>; benign cytology with a mobile painless mass and normal facial nerve function supports "
  "an adenoma; facial weakness, fixation or nodes mean malignancy regardless of what cytology says."),
}
