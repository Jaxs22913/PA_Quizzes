# -*- coding: utf-8 -*-
from _pd2_ent_osce_data import E
BATCH = {

"Branchial cleft cyst": E(
  "&ldquo;There&rsquo;s a soft lump on the side of my neck &mdash; it swells up whenever I get a "
  "cold.&rdquo;",
  "Palpate a <b>smooth, fluctuant, non-tender mass ANTERIOR to the sternocleidomastoid</b>, usually "
  "in the upper third. <b>It does NOT move with swallowing or tongue protrusion</b> &mdash; that is "
  "how it is separated from a thyroglossal cyst. Look for a skin pit or sinus opening. Transilluminate.",
  [("Thyroglossal duct cyst", "MIDLINE and rises with tongue protrusion"),
   ("Cystic metastatic node", "In an adult over 40 this must be excluded &mdash; a cystic node can look identical"),
   ("Lymphangioma", "Softer, multiloculated, transilluminates brightly, present in infancy")],
  "<b>Ultrasound</b> &rarr; a well-defined anechoic cystic lesion anterior to the "
  "sternocleidomastoid. <b>Computed tomography or magnetic resonance</b> &rarr; extent and its "
  "relation to the great vessels. <b>Fine needle aspiration in any adult</b> &rarr; benign cyst "
  "fluid rather than malignant cells.",
  "Midline position with elevation on swallowing means thyroglossal; <b>malignant cells on "
  "aspiration mean a cystic metastasis, and in an adult that possibility must be closed before "
  "excision is planned</b>."),

"Thyroglossal duct cyst": E(
  "&ldquo;There&rsquo;s a lump in the middle of my neck.&rdquo; A parent may report it appearing "
  "after a sore throat.",
  "Palpate a <b>MIDLINE mass, usually at or just below the hyoid</b>. <b>Ask the patient to "
  "swallow and then to protrude the tongue &mdash; it rises with both.</b> That elevation is the "
  "diagnostic manoeuvre. Palpate the thyroid gland itself.",
  [("Branchial cleft cyst", "Lateral, anterior to the sternocleidomastoid, and does not elevate"),
   ("Dermoid cyst", "Also midline, but it does NOT move with tongue protrusion"),
   ("Ectopic thyroid tissue", "May be the patient's ONLY thyroid &mdash; excising it would leave them athyreotic")],
  "<b>Ultrasound</b> &rarr; a midline cystic lesion, AND <b>confirmation that a normal thyroid "
  "gland is present in its usual place</b> &mdash; that second finding is the one that must never "
  "be skipped. <b>Thyroid function tests.</b>",
  "Absence of movement on tongue protrusion suggests a dermoid; a lateral position means branchial "
  "cleft; ultrasound showing no orthotopic thyroid means the mass is ectopic thyroid, not a cyst."),

"Laryngocele": E(
  "&ldquo;A lump comes up in my neck when I blow hard, and my voice goes husky.&rdquo; Often a wind "
  "player or glassblower.",
  "<b>Ask the patient to perform a Valsalva manoeuvre &mdash; the mass enlarges.</b> That "
  "reducibility is the finding. Palpate for a compressible mass at the thyrohyoid membrane. "
  "Auscultate for a hiss on decompression. Examine the larynx.",
  [("Branchial cleft cyst", "Does not change with Valsalva"),
   ("Laryngeal carcinoma", "Can OBSTRUCT the saccule and cause a secondary laryngocele &mdash; must be excluded"),
   ("Thyroid nodule", "Moves with swallowing rather than with Valsalva")],
  "<b>Computed tomography</b> &rarr; an <b>air-filled or fluid-filled sac continuous with the "
  "laryngeal ventricle</b>. <b>Laryngoscopy</b> &rarr; the saccular opening, and it excludes a "
  "tumour at the same time.",
  "A mass that does not change with Valsalva is not a laryngocele; a normal larynx on endoscopy "
  "excludes an obstructing carcinoma, which is the reason endoscopy is done at all."),

"Plunging ranula": E(
  "&ldquo;I had a swelling under my tongue and now there&rsquo;s a soft lump in my neck.&rdquo;",
  "<b>Bimanual examination &mdash; one hand in the floor of the mouth, one on the neck.</b> Look "
  "for a bluish translucent swelling in the floor of the mouth. Palpate the submandibular gland and "
  "check Wharton duct.",
  [("Simple ranula", "Confined to the floor of the mouth, not extending through mylohyoid"),
   ("Dermoid cyst of the floor of mouth", "Doughy, midline, without the bluish translucent quality"),
   ("Submandibular sialadenitis", "Painful gland with pus at the duct, worse with meals")],
  "<b>Magnetic resonance or computed tomography</b> &rarr; a <b>unilocular cystic lesion extending "
  "THROUGH the mylohyoid muscle into the neck</b> &mdash; that transit is what makes it plunging. "
  "Aspiration &rarr; thick, mucoid, saliva-like fluid.",
  "A cyst confined above mylohyoid is a simple ranula; pus from Wharton duct with meal-related "
  "pain means sialadenitis or a stone."),

"Lymphangioma (cystic hygroma)": E(
  "A parent says &ldquo;she was born with a soft swelling in her neck and it&rsquo;s getting "
  "bigger.&rdquo;",
  "Palpate a <b>soft, compressible, ill-defined mass, usually in the posterior triangle</b>. "
  "<b>Transilluminate &mdash; it glows brightly</b>, which is the classic finding. Assess airway "
  "and feeding. Watch for sudden enlargement after an infection or bleed.",
  [("Haemangioma", "Red or blue, blanches, and follows proliferate-then-involute growth"),
   ("Branchial cleft cyst", "Discrete and unilocular, anterior rather than posterior triangle"),
   ("Teratoma", "Contains solid elements and calcification; does not transilluminate uniformly")],
  "<b>Ultrasound</b> &rarr; a multiloculated cystic mass with thin septa. <b>Magnetic resonance</b> "
  "&rarr; extent and airway relationship, which is what surgery is planned from. Fluid levels "
  "suggest previous haemorrhage.",
  "Bright uniform transillumination with multiloculated cysts excludes a solid tumour; a blanching "
  "vascular lesion is a haemangioma; solid components with calcification mean teratoma."),

"Haemangioma": E(
  "&ldquo;It wasn&rsquo;t there at birth, then it appeared and grew fast for months &mdash; now "
  "it&rsquo;s fading.&rdquo;",
  "Inspect colour and depth &mdash; superficial lesions are bright red, deep ones bluish. "
  "<b>Compress it &mdash; it blanches and refills.</b> Note the growth phase. <b>Check for airway "
  "involvement if it is in a beard distribution</b>, and look for multiple lesions.",
  [("Vascular malformation", "Present AT birth and grows proportionately &mdash; it never involutes"),
   ("Lymphangioma", "Transilluminates, does not blanch, and is not red"),
   ("Pyogenic granuloma", "A small friable bleeding papule appearing rapidly at one point")],
  "<b>Clinical</b> &rarr; the proliferate-then-involute history with a blanching vascular lesion. "
  "<b>Ultrasound with Doppler</b> &rarr; a high-flow soft tissue mass. <b>Magnetic resonance</b> "
  "&rarr; extent, and airway involvement in segmental lesions.",
  "A lesion present at birth that grows only with the child is a malformation, not a haemangioma; "
  "absence of blanching excludes it; low flow on Doppler suggests a venous malformation."),

"Teratoma": E(
  "&ldquo;The baby was born with a large firm mass in the neck&rdquo; &mdash; often detected before "
  "birth on scan.",
  "Palpate a <b>firm, irregular mass containing both solid and cystic parts</b>. <b>Assess the "
  "airway immediately</b> &mdash; that is the priority. Look for tracheal deviation and check "
  "feeding. Examine the thyroid.",
  [("Lymphangioma", "Soft, compressible and transilluminates; purely cystic"),
   ("Goitre", "Moves with swallowing and is thyroid in origin"),
   ("Neuroblastoma", "Firm, may be associated with Horner syndrome and raised urinary catecholamines")],
  "<b>Ultrasound and magnetic resonance</b> &rarr; a heterogeneous mass with <b>fat, cystic areas "
  "and CALCIFICATION</b> &mdash; that mixed tissue content is what names it. <b>Alpha-fetoprotein</b> "
  "&rarr; a baseline, since a rise suggests a malignant germ cell component.",
  "A uniformly cystic transilluminating lesion is a lymphangioma; a mass moving with swallowing is "
  "thyroid; raised urinary catecholamines redirect to neuroblastoma."),

"Dermoid cyst": E(
  "&ldquo;There&rsquo;s a firm lump in the middle of my neck under my chin.&rdquo;",
  "Palpate a <b>midline, doughy, non-tender mass</b>. <b>Ask for tongue protrusion &mdash; it does "
  "NOT rise</b>, unlike a thyroglossal cyst. Bimanual examination of the floor of the mouth to see "
  "whether it sits above or below mylohyoid.",
  [("Thyroglossal duct cyst", "Rises with tongue protrusion &mdash; the single distinguishing test"),
   ("Plunging ranula", "Bluish, translucent, arising from the floor of the mouth"),
   ("Submental lymphadenopathy", "Multiple, tender, with an infective source in the mouth or lip")],
  "<b>Ultrasound or magnetic resonance</b> &rarr; a well-defined midline lesion with <b>fat "
  "content and the sack-of-marbles appearance</b> of keratin debris. It does not connect to the "
  "hyoid.",
  "Elevation on tongue protrusion with a tract to the hyoid means thyroglossal; a translucent "
  "bluish floor-of-mouth swelling means ranula; tender multiple nodes with a dental source mean "
  "adenopathy."),

"Thymic cyst": E(
  "&ldquo;There&rsquo;s a painless lump low in my child&rsquo;s neck.&rdquo; Usually found "
  "incidentally.",
  "Palpate a <b>soft cystic mass in the LOWER lateral neck, often left-sided</b>, sometimes "
  "extending toward the chest. Check whether it changes with position or Valsalva. Assess for "
  "airway or vascular compression.",
  [("Branchial cleft cyst", "Upper third of the neck rather than the lower"),
   ("Lymphangioma", "Multiloculated, transilluminates, posterior triangle"),
   ("Mediastinal extension of any cyst", "The reason chest imaging is part of the workup")],
  "<b>Ultrasound</b> &rarr; a cystic lower neck lesion. <b>Computed tomography or magnetic "
  "resonance including the CHEST</b> &rarr; continuity with the thymus or extension into the "
  "mediastinum, which changes the operation.",
  "An upper-neck cyst anterior to the sternocleidomastoid is branchial; imaging showing no "
  "mediastinal connection excludes extension; multiloculated cysts suggest lymphangioma."),

"Sternocleidomastoid tumour of infancy": E(
  "&ldquo;There&rsquo;s a hard lump in the baby&rsquo;s neck and she always turns her head to one "
  "side.&rdquo;",
  "Palpate a <b>firm, fusiform mass WITHIN the sternocleidomastoid muscle</b> &mdash; it moves with "
  "the muscle, not independently. <b>Assess head posture: the head tilts TOWARD and the chin turns "
  "AWAY from the affected side.</b> Test passive neck rotation. <b>Examine the hips</b> &mdash; "
  "dysplasia is associated.",
  [("Cervical lymphadenopathy", "Nodes are separate from the muscle and often multiple"),
   ("Branchial cleft cyst", "Cystic and anterior to the muscle rather than inside it"),
   ("Cervical spine anomaly", "Torticollis with restricted movement but no muscle mass")],
  "<b>Clinical</b> &rarr; a mass within the muscle with the characteristic head posture and a birth "
  "history of difficult delivery. <b>Ultrasound</b> &rarr; fusiform thickening of the muscle "
  "itself, no discrete node. <b>Hip ultrasound</b> &rarr; associated dysplasia.",
  "A mass separate from the muscle is a node; <b>cervical spine imaging</b> &rarr; excludes a bony "
  "anomaly if movement stays restricted; a normal muscle on ultrasound excludes it."),

"Reactive viral lymphadenopathy": E(
  "&ldquo;I got some sore lumps in my neck when I had that cold.&rdquo;",
  "Palpate <b>multiple, small, soft, MOBILE, mildly tender nodes</b>. Note size and site. "
  "<b>Examine the pharynx, ears, teeth and scalp for the source.</b> Palpate other nodal basins and "
  "the spleen &mdash; generalised adenopathy means something different.",
  [("Bacterial suppurative adenitis", "A single large, hot, fluctuant, very tender node"),
   ("Infectious mononucleosis", "Posterior cervical nodes, marked fatigue, splenomegaly"),
   ("Lymphoma", "Painless, rubbery, progressive, WITHOUT an infective source and with night sweats")],
  "<b>Clinical</b> &rarr; small mobile tender nodes with an identified infective source, "
  "<b>regressing within 2 to 4 weeks</b>. That regression is the confirmation. Investigate only if "
  "it persists.",
  "<b>Any node persisting beyond 4 to 6 weeks, over 1.5 centimetres, hard, fixed, or supraclavicular "
  "gets fine needle aspiration</b> &rarr; malignant cells would redirect entirely; a positive "
  "monospot means mononucleosis; fluctuance means suppuration."),

"HIV-associated cervical adenopathy": E(
  "&ldquo;I&rsquo;ve had swollen glands for months, along with night sweats and weight loss.&rdquo;",
  "Palpate <b>persistent, generalised, symmetric adenopathy in two or more sites</b>. Examine the "
  "mouth for candidiasis, hairy leukoplakia and Kaposi sarcoma. Palpate liver and spleen. Take a "
  "risk history.",
  [("Lymphoma", "Asymmetric, progressive, and much more likely in this same population"),
   ("Tuberculous adenitis", "Matted nodes that may fistulate; also commoner here"),
   ("Reactive adenopathy", "Follows an acute infection and resolves")],
  "<b>Human immunodeficiency virus serology with confirmatory testing</b> &rarr; positive, and "
  "<b>CD4 count with viral load</b> &rarr; degree of immunosuppression. <b>Excisional node biopsy "
  "if a node is dominant or growing</b> &rarr; distinguishes reactive hyperplasia from lymphoma or "
  "mycobacterial disease.",
  "Reactive hyperplasia on biopsy excludes lymphoma; acid-fast staining and culture exclude "
  "tuberculosis; resolution with treatment argues against malignancy. A dominant enlarging node in "
  "a patient with the virus is biopsied, not watched."),

"Suppurative bacterial lymphadenopathy": E(
  "&ldquo;This lump in my neck is hot, red and really painful, and I&rsquo;ve got a fever.&rdquo;",
  "Palpate a <b>single, large, hot, erythematous, exquisitely tender node; test for "
  "FLUCTUANCE</b> &mdash; that is what decides drainage. Find the source: teeth, tonsils, scalp, "
  "skin. Assess the airway and for deep neck extension.",
  [("Reactive viral adenopathy", "Multiple small mobile nodes, mildly tender, no fluctuance"),
   ("Deep neck abscess", "Trismus, dysphagia and toxicity; the escalation to exclude"),
   ("Infected congenital cyst", "A pre-existing lump that has become infected")],
  "<b>Clinical</b> &rarr; a hot, tender, fluctuant node with fever. <b>Ultrasound</b> &rarr; a "
  "hypoechoic collection with debris rather than a solid node &mdash; abscess versus cellulitis. "
  "<b>Contrast computed tomography</b> if deep extension is suspected &rarr; a rim-enhancing "
  "collection. <b>Aspiration culture</b> &rarr; the organism.",
  "A solid node without a collection on ultrasound is treated medically, not drained; trismus and "
  "airway compromise redirect to a deep neck space infection; a long-standing lump suggests an "
  "infected congenital cyst."),

"Toxoplasmosis": E(
  "&ldquo;I&rsquo;ve had swollen glands in my neck for weeks and I feel tired&rdquo; &mdash; often "
  "with a cat at home or a taste for undercooked meat.",
  "Palpate <b>painless or minimally tender posterior cervical nodes</b>. Look for splenomegaly and "
  "a rash. <b>Take an exposure history: cats, litter trays, undercooked meat.</b> Fundoscopy if "
  "vision is affected. <b>Pregnancy status matters enormously.</b>",
  [("Infectious mononucleosis", "The closest mimic &mdash; both give posterior nodes and fatigue"),
   ("Cat scratch disease", "A papule at the scratch with regional nodes, also cat-associated"),
   ("Lymphoma", "Progressive painless nodes with night sweats and weight loss")],
  "<b>Toxoplasma serology, immunoglobulin M and G with avidity testing</b> &rarr; acute infection; "
  "avidity distinguishes recent from remote. <b>Node histology if biopsied</b> &rarr; a "
  "characteristic reactive pattern.",
  "A positive monospot with atypical lymphocytes means mononucleosis; negative toxoplasma "
  "serology excludes it; <i>Bartonella</i> serology identifies cat scratch disease instead."),

"Tularemia": E(
  "&ldquo;I got a sore on my hand after skinning rabbits, and now my glands are up and I have a "
  "fever.&rdquo;",
  "Look for an <b>ulcer at the inoculation site with regional adenopathy</b> &mdash; the "
  "ulceroglandular pattern. Palpate the draining nodes for fluctuance. <b>Take the exposure "
  "history: rabbits, ticks, deerflies.</b> Examine the chest and eyes.",
  [("Cat scratch disease", "A papule with regional nodes but a cat rather than a rabbit or tick"),
   ("Suppurative bacterial adenitis", "Hot fluctuant node without an inoculation ulcer"),
   ("Plague or anthrax", "Other zoonoses with a similar pattern and different exposures")],
  "<b>Serology, acute and convalescent</b> &rarr; a fourfold rise in titre. <b>Culture</b> is "
  "possible but <b>the laboratory must be warned</b>, since it is a hazard to staff. <b>Polymerase "
  "chain reaction</b> on tissue &rarr; the organism.",
  "Negative serology on paired samples excludes it; <i>Bartonella</i> serology redirects to cat "
  "scratch; routine culture growing a common pyogenic organism means ordinary adenitis."),

"Brucellosis": E(
  "&ldquo;I&rsquo;ve had fevers that come and go, sweats and aching joints &mdash; I drink "
  "unpasteurised milk.&rdquo;",
  "Palpate cervical nodes, <b>liver and spleen</b>. Take temperature over time to show the "
  "undulant pattern. Examine joints and the spine. <b>Occupational and dietary history: farm work, "
  "abattoirs, unpasteurised dairy, travel.</b>",
  [("Tuberculosis", "Also chronic with fever and sweats; nodes matt and fistulate"),
   ("Lymphoma", "Fever, sweats and weight loss without an exposure history"),
   ("Infectious mononucleosis", "Acute, self-limiting, with a positive monospot")],
  "<b>Blood cultures held for prolonged incubation</b> &rarr; <i>Brucella</i> species; warn the "
  "laboratory. <b>Serum agglutination titres</b> &rarr; a raised or rising titre. <b>Bone marrow "
  "culture</b> has a higher yield when blood cultures are negative.",
  "Negative serology with negative prolonged cultures excludes it; acid-fast bacilli redirect to "
  "tuberculosis; node biopsy showing lymphoma changes the diagnosis entirely."),

"Cat scratch disease": E(
  "&ldquo;My kitten scratched me and about two weeks later the glands in my neck came up.&rdquo;",
  "Find the <b>inoculation papule or pustule at the scratch</b>, then palpate the <b>draining "
  "regional nodes</b>, which are tender and may suppurate. <b>Examine the eyes</b> &mdash; "
  "conjunctivitis with preauricular nodes is Parinaud oculoglandular syndrome. Palpate liver and "
  "spleen.",
  [("Tularemia", "The same ulcer-plus-node pattern with rabbit or tick exposure"),
   ("Atypical mycobacterial adenitis", "Violaceous overlying skin in a young child, no scratch history"),
   ("Lymphoma", "Painless progressive nodes with constitutional symptoms and no inoculation site")],
  "<b><i>Bartonella henselae</i> serology</b> &rarr; raised immunoglobulin G or M titres. "
  "<b>Polymerase chain reaction of node aspirate</b> &rarr; the organism. <b>Node histology</b> "
  "&rarr; stellate granulomas with necrosis, if biopsied.",
  "Negative <i>Bartonella</i> serology excludes it; tularemia serology covers the other zoonosis; "
  "acid-fast staining excludes mycobacterial disease; most cases resolve in 2 to 4 months, and "
  "failure to do so prompts a rethink."),

"Actinomycosis": E(
  "&ldquo;My jaw has been swollen and lumpy for months and it&rsquo;s started draining through the "
  "skin.&rdquo;",
  "Palpate a <b>firm, indurated, woody mass, usually at the angle of the jaw</b>. Look for "
  "<b>sinus tracts discharging sulphur granules</b>. Examine the dentition &mdash; poor dental "
  "hygiene or a recent extraction is the usual portal. <b>Note that it crosses tissue planes</b>, "
  "which infections usually do not.",
  [("Tuberculous adenitis", "Matted nodes that fistulate too, but without sulphur granules"),
   ("Osteomyelitis of the mandible", "Bone pain with sequestra on imaging"),
   ("Malignancy", "Hard, fixed, progressive &mdash; and it is why tissue is obtained")],
  "<b>Anaerobic culture, held for prolonged incubation</b> &rarr; <i>Actinomyces israelii</i>. "
  "<b>Microscopy of pus or granules</b> &rarr; <b>sulphur granules with branching filamentous "
  "gram-positive rods</b>. <b>Histology</b> &rarr; the same granules in tissue.",
  "Acid-fast bacilli redirect to tuberculosis; malignant cells on histology change the diagnosis; "
  "absence of granules with a routine pyogenic organism means ordinary infection."),

"Atypical mycobacteria": E(
  "A parent says &ldquo;he has a lump in his neck that isn&rsquo;t sore, and the skin over it has "
  "gone purple.&rdquo; Typically a well child under five.",
  "Palpate a <b>non-tender node with VIOLACEOUS thinning skin over it</b>. Note that the child is "
  "systemically WELL. Examine the chest. <b>Ask about tuberculosis contacts and travel</b>, since "
  "the differential is what matters. Check immune status.",
  [("Tuberculous adenitis", "Systemic symptoms, positive contact history and a positive interferon test"),
   ("Suppurative bacterial adenitis", "Hot, painful, red rather than cool and violaceous, with fever"),
   ("Lymphoma", "Progressive, firm, with constitutional symptoms")],
  "<b>Mycobacterial culture and polymerase chain reaction of aspirate or excised node</b> &rarr; a "
  "non-tuberculous species. <b>Interferon gamma release assay</b> &rarr; NEGATIVE, which is what "
  "separates it from tuberculosis. <b>Chest radiograph</b> &rarr; normal.",
  "A positive interferon assay with an abnormal chest film means tuberculosis, a different "
  "treatment entirely; a hot painful node with fever means pyogenic adenitis. <b>Incision and "
  "drainage is avoided &mdash; it produces a chronic sinus; complete excision is preferred.</b>"),

"Tuberculous adenitis (scrofula)": E(
  "&ldquo;I&rsquo;ve had swollen glands in my neck for months with fevers and night sweats, and "
  "I&rsquo;ve lost weight.&rdquo;",
  "Palpate <b>MATTED, firm nodes, classically in the posterior triangle</b>, which may fistulate "
  "to the skin. Examine the chest. Take a contact, travel and immune-status history. Look for "
  "adenopathy elsewhere.",
  [("Atypical mycobacterial adenitis", "A well young child, violaceous skin, negative interferon assay"),
   ("Lymphoma", "Rubbery discrete nodes rather than matted, with the same constitutional symptoms"),
   ("Metastatic carcinoma", "Hard and fixed, with a mucosal primary to be found")],
  "<b>Interferon gamma release assay or tuberculin skin test</b> &rarr; positive. <b>Node "
  "aspirate or biopsy for acid-fast staining, culture and polymerase chain reaction</b> &rarr; "
  "<i>Mycobacterium tuberculosis</i>; histology shows <b>caseating granulomas</b>. <b>Chest "
  "radiograph</b> &rarr; active or old pulmonary disease.",
  "A negative interferon assay with a non-tuberculous species on culture means atypical "
  "mycobacteria; non-caseating granulomas suggest sarcoidosis; malignant cells redirect to lymphoma "
  "or carcinoma."),

"Fungal neck infection": E(
  "&ldquo;These neck glands have been up for weeks and haven&rsquo;t responded to antibiotics&rdquo; "
  "&mdash; usually in an immunocompromised patient.",
  "Palpate the nodes and note induration or fistulation. <b>Assess immune status carefully</b> "
  "&mdash; it determines both likelihood and severity. Examine the mouth for candidiasis, the chest, "
  "and the skin. Take a travel and exposure history for endemic fungi.",
  [("Tuberculous adenitis", "The main mimic &mdash; chronic nodes in the same population"),
   ("Actinomycosis", "Woody induration with sulphur granules"),
   ("Lymphoma", "Progressive painless nodes with constitutional symptoms")],
  "<b>Fungal culture and staining of aspirate or biopsy</b> &rarr; the organism. <b>Histology with "
  "special stains</b> &rarr; fungal elements in tissue. <b>Serology or antigen testing</b> for "
  "endemic fungi &rarr; positive. Assess the immune deficiency itself.",
  "Acid-fast bacilli redirect to mycobacterial disease; sulphur granules mean actinomycosis; "
  "malignant cells mean lymphoma. Failure of antibacterial therapy is the trigger to send fungal "
  "studies, not to escalate antibiotics again."),
}
