# -*- coding: utf-8 -*-
"""Question bank for "Guess that Disease" -- CMS I Exam 3, ear, nose and throat.

Same format as the ophthalmology and dermatology banks: a photograph, four bare
condition names, plausible distractors.

THE INCLUSION BAR, and why so much of this block is not here. All 218 pictures
in the five ENT decks were looked at in contact sheets, not just the 64 the
comparison chart had already picked. An item exists only when THE PHOTOGRAPH
ITSELF SHOWS THE FEATURE THAT NAMES THE DISEASE. That threw out the same three
categories the ophthalmology sweep did, and one new one:

  * Answer printed in the pixels. This block is the worst offender of the three
    so far. "Primary cholesteatoma" and "Early congenital cholesteatoma" on all
    three of the deck's cholesteatoma photographs; "Fungal otitis externa";
    "Nasal Polyp" written across the endoscopy; "Deviated nasal septum"; the
    "Streptococcal Pharyngitis | Viral Pharyngitis" side-by-side; "TONSILLITIS"
    with the swollen tonsil arrowed; "Right Tonsil / Displaced Uvula / Abscess"
    drawn on the peritonsillar abscess; "Epiglottitis (Thumb Sign) vs Normal
    Epiglottis"; "Normal Larynx / Papilloma"; "Acoustic Neuroma"; "Otosclerosis";
    "What is Ludwig's Angina?"; "Types of Dental Abscess"; "Stages Of Gum
    Disease". Where the same finding had a clean photograph elsewhere in the
    deck it was pulled instead -- see tools/extract_cms_e3_gtd_images.py --
    and where it did not, the condition is simply absent.

  * Diagrams, scans and equipment standing in for a finding. Most of Lecture 16
    is audiograms and tympanograms, and most of Lecture 18 is neck-triangle
    anatomy and staging tables. Neither is a photograph of a disease.

  * Pairs whose discriminator is not visible in a photograph:
      - Behcet syndrome vs aphthous stomatitis. Both are oral ulcers; what
        separates them is recurrence and the genital, ocular and skin
        involvement. Only aphthous stomatitis is asked, and Behcet is not
        offered against it.
      - Systemic lupus oral ulcers -- same problem, and the deck's picture is
        a non-specific erosion. Dropped.
      - Streptococcal vs viral pharyngitis. The deck's own side-by-side exists
        to make the point that they overlap. Only bacterial pharyngitis is
        asked, from a clean exudate photograph, and viral pharyngitis is never
        the distractor against it.
      - Acute otitis media vs otitis media with effusion IS asked both ways,
        because here the photographs genuinely differ -- bulging and
        erythematous against an air-fluid level with bubbles behind a retracted
        drum -- and the slide lists those as the exam findings.

  * NEW HERE: the deck files an image under the wrong heading. Slide 133 is
    Oral Leukoplakia, but two of its three pictures show a lacy reticular
    pattern, which is what Wickham striae look like in lichen planus. Only the
    homogeneous white plaque (pos3) is used, and lichen planus is asked from
    its own slides instead. Per [[slides_only_grounding]] the deck normally
    wins, but not when following it would teach the wrong appearance.

WHAT IS ABSENT AND WHY, so the gaps do not read as oversights:

  * Nasal polyps -- the deck's only endoscopy has "Nasal Polyp" written on it.
  * Cholesteatoma is asked from a black-and-white otoscopy with an arrowhead
    and arrow on it. Those markers point at the retraction and the debris; they
    do not name the condition. It is the only un-annotated picture of it.
  * The salivary gland conditions. The deck's parotid-swelling photograph sits
    on a section-title slide ("Salivary Gland Disorders") rather than on
    sialadenitis or sialolithiasis, and the picture on the acute suppurative
    sialadenitis slide shows a duct stone. Attributing either one confidently
    was not possible, so neither is asked.
  * Meniere disease, BPPV, vestibular neuritis, acoustic neuroma, presbycusis,
    otosclerosis -- none has a photographic finding at all. This is why Lecture
    16 contributes three items and Lecture 15 contributes twelve.

Four options, not five: this format is deliberately outside the CMS
[[exam_standard]], and check_exam_standard.py warns about it and about the
absence of a patient in the stem. Both are expected.

Length bias has a special case here ([[distractor_style_matching]]): disease
names are fixed, so where the key is long the DISTRACTORS are re-chosen at
comparable length rather than padded.
"""

D15 = "Disorders of the External and Middle Ear"
D16 = "Disorders of the Inner Ear"
D17 = "Nose and Paranasal Sinuses"
D18 = "Neoplasms and Neck Masses"
D19 = "Disorders of the Oral Cavity and Salivary Glands"

EAR = "Region: Ear"
NOSE = "Region: Nose and sinuses"
NECK = "Region: Neck"
ORAL = "Region: Oral cavity"
THROAT = "Region: Pharynx and larynx"

ITEMS = [
    # ---------------------------------------------------------------- ear
    dict(cond="Acute otitis media", img="l15-s016_pos1.jpg", slide=16, deck=D15, io=EAR,
         alt="Otoscopic view of a tympanic membrane that is uniformly red and bulging outward, with the normal landmarks obscured",
         why="The drum is erythematous and bulging outward. Those are the examination findings of acute otitis media, often with a purulent effusion visible behind the drum.",
         wrong=[("Otitis media with effusion", "That drum is retracted or neutral and dull, with an air-fluid level or bubbles behind it, not pushed outward."),
                ("Otitis externa", "That is redness and swelling of the canal wall; here the canal is clear and the drum itself is the abnormality."),
                ("Tympanic membrane perforation", "Perforation is a disruption in the drum, central or marginal; this membrane is intact, red and bulging outward instead.")]),

    dict(cond="Otitis media with effusion", img="l15-s016_pos2.jpg", slide=16, deck=D15, io=EAR,
         alt="Otoscopic view showing multiple rounded air bubbles and a fluid line behind an intact, non-bulging tympanic membrane",
         why="Air bubbles and a visible fluid level behind an intact drum that is not bulging — fluid without acute inflammation.",
         wrong=[("Acute otitis media", "That drum is red and bulging outward; this one is neither, and you can see through it."),
                ("Cholesteatoma", "That shows white keratin debris in a retraction pocket, not clear fluid and bubbles."),
                ("Barotrauma", "That drum is hemorrhagic and dark from blood in the middle ear, not clear serous fluid.")]),

    dict(cond="Cerumen impaction", img="l15-s026_pos2.jpg", slide=26, deck=D15, io=EAR,
         alt="Otoscopic view of the external canal completely filled by a dense brown-black waxy plug",
         why="The canal is occluded by wax. Nothing beyond it can be seen, which is what makes it an impaction rather than a normal finding.",
         wrong=[("Foreign body in the ear canal", "That is a discrete object with manufactured edges and color; this material is the ear's own secretion."),
                ("Otomycosis", "That shows fine filamentous fungal growth with black or white spores, not a solid homogeneous plug."),
                ("Exostoses", "Those are smooth bony swellings of the canal wall, skin-colored and hard, not occluding debris.")]),

    dict(cond="Cholesteatoma", img="l15-s034_pos1.jpg", slide=34, deck=D15, io=EAR,
         alt="Otoscopic view with a retraction pocket in the upper tympanic membrane filled with pale flaky keratin debris, marked by an arrowhead and an arrow",
         why="A retraction pocket of the drum containing squamous epithelium and keratin debris (arrowhead), with debris visible behind the drum (arrow), is the examination finding of cholesteatoma.",
         wrong=[("Otitis media with effusion", "That is clear fluid and bubbles behind an intact drum, with no retraction pocket and no white debris."),
                ("Tympanosclerosis", "That is a chalky white plaque within the drum itself, flat and scar-like, not debris sitting in a pocket."),
                ("Glomus tumor", "That is a red vascular mass behind the drum, not white keratin.")]),

    dict(cond="Tympanic membrane perforation", img="l15-s047_pos1.jpg", slide=47, deck=D15, io=EAR,
         alt="Otoscopic view of a tympanic membrane with a discrete dark hole through it and the middle ear visible beyond",
         why="There is a full-thickness defect in the drum — you can see through it into the middle ear.",
         wrong=[("Acute otitis media", "Acute otitis media gives an erythematous, bulging drum that is still intact; this one shows a disruption through it."),
                ("Cholesteatoma", "That is keratin debris in a retraction pocket, not an opening through the membrane."),
                ("Otitis media with effusion", "That drum is intact with fluid behind it, which is exactly what a perforation drains.")]),

    dict(cond="Foreign body in the ear canal", img="l15-s049_pos2.jpg", slide=49, deck=D15, io=EAR,
         alt="Otoscopic view of a smooth round blue object filling part of the external auditory canal",
         why="A smooth, round, manufactured blue object — color and shape no biological material has.",
         wrong=[("Cerumen impaction", "Wax is brown to black and irregular; nothing the body makes is this color or this smoothly spherical."),
                ("Otomycosis", "That is filamentous fungal growth with spores, not a solid discrete object."),
                ("Exostoses", "Those are bony swellings continuous with the canal wall, not something lying loose in the lumen.")]),

    dict(cond="Otitis externa", img="l15-s058_pos2.jpg", slide=58, deck=D15, io=EAR,
         alt="External ear with a red swollen canal opening and yellow crusted discharge over the concha",
         why="Erythema and edema of the external canal with visible discharge — the disease is in the canal, not behind the drum.",
         wrong=[("Acute otitis media", "That is a red bulging drum seen through a clear canal; here the canal itself is inflamed."),
                ("Necrotizing otitis externa", "That is the invasive form, with granulation tissue and bone involvement in a diabetic or immunocompromised patient."),
                ("Auricular cellulitis", "That would redden the whole auricle including the lobule; here the change centers on the canal.")]),

    dict(cond="Necrotizing otitis externa", img="l15-s061_pos1.jpg", slide=61, deck=D15, io=EAR,
         alt="Auricle and surrounding skin with extensive ulceration, granulation tissue and thick crusting extending beyond the canal",
         why="Infection has left the canal and destroyed the surrounding soft tissue — the invasive form that reaches the skull base.",
         wrong=[("Otitis externa", "The ordinary form stays in the canal; it does not ulcerate through into the surrounding tissue."),
                ("Auricular hematoma", "That is a smooth purple fluctuant swelling under intact skin, not ulceration."),
                ("Keloid", "That is a firm smooth overgrowth of scar tissue with intact skin over it.")]),

    dict(cond="Auricular hematoma", img="l15-s040_pos1.jpg", slide=40, deck=D15, io=EAR,
         alt="Auricle with a smooth tense purple swelling filling the scapha and antihelix so the normal ridges are lost",
         why="Blood collected under the perichondrium has filled in the normal ridges, so the cartilaginous landmarks are gone.",
         wrong=[("Relapsing polychondritis", "That is inflammation of the cartilage itself, sparing the lobule, and it recurs on both sides."),
                ("Auricular cellulitis", "That is diffuse redness and warmth of the skin, without a tense collection lifting the perichondrium."),
                ("Keloid", "That is firm scar tissue that grows slowly after trauma, not a fluctuant swelling appearing within hours.")]),

    dict(cond="Auricular laceration", img="l15-s043_pos2.jpg", slide=43, deck=D15, io=EAR,
         alt="Auricle with a full-thickness tear through the helix and antihelix, bleeding freely down the side of the face",
         why="A full-thickness break in the skin and cartilage — an open wound rather than a swelling.",
         wrong=[("Auricular hematoma", "That is a closed injury; the skin stays intact and the blood collects beneath it."),
                ("Necrotizing otitis externa", "That destroys tissue by infection over days to weeks, not by a single traumatic tear."),
                ("Perichondritis", "That is infection of the cartilage covering, with a red swollen but unbroken auricle.")]),

    dict(cond="Keloid", img="l15-s069_pos2.jpg", slide=69, deck=D15, io=EAR,
         alt="Two firm smooth rounded nodules on the earlobe with intact overlying skin, at a piercing site",
         why="Firm rounded overgrowths of scar tissue at a site of previous trauma, extending beyond the original wound.",
         wrong=[("Auricular hematoma", "That is a fluctuant collection of blood appearing within hours of blunt trauma, not firm scar."),
                ("Epidermoid cyst", "That is a single soft mobile lump with a central punctum, not firm scar at a piercing."),
                ("Basal cell carcinoma", "That is a pearly lesion with rolled borders and often central ulceration.")]),

    dict(cond="Exostoses", img="l16-s049_pos2.jpg", slide=49, deck=D16, io=EAR,
         alt="Otoscopic view of the canal narrowed by several smooth skin-covered bony swellings, labeled with the letter e, around a central tympanic membrane labeled tm",
         why="Multiple smooth bony swellings of the canal wall, narrowing the lumen but covered by normal skin.",
         wrong=[("Cerumen impaction", "That is soft brown occluding debris; these swellings are part of the canal wall itself."),
                ("Otitis externa", "That canal is red and edematous with discharge; this one is pale and structurally narrowed."),
                ("Cholesteatoma", "That sits at the tympanic membrane as keratin debris, not as bone in the canal wall.")]),

    dict(cond="Glomus tumor", img="l16-s051_pos1.jpg", slide=51, deck=D16, io=EAR,
         alt="Otoscopic view of a red vascular mass sitting behind the lower part of the tympanic membrane and showing through it",
         why="A red, highly vascular mass in the middle ear showing through the drum. These benign vascular growths cause a middle ear mass effect, pulsatile tinnitus and conductive hearing loss.",
         wrong=[("Barotrauma", "That is blood within the middle ear from unequalized pressure, dark and diffuse rather than a discrete mass."),
                ("Cholesteatoma", "That is white keratin debris in a retraction pocket, not a red vascular mass."),
                ("Acute otitis media", "That is a diffusely red bulging drum, not a discrete mass visible behind a clear membrane.")]),

    dict(cond="Barotrauma", img="l16-s059_pos1.jpg", slide=59, deck=D16, io=EAR,
         alt="Otoscopic view of a tympanic membrane that is uniformly dark blue-purple from blood filling the middle ear behind it",
         why="Blood in the middle ear behind an intact drum, giving it the dark blue color — the hemotympanum that follows unequalized pressure.",
         wrong=[("Acute otitis media", "That drum is red and bulging with pus behind it; this one is blue-black with blood."),
                ("Glomus tumor", "That is a discrete red vascular mass, not uniform discoloration of the whole drum."),
                ("Otitis media with effusion", "That fluid is clear or amber with visible bubbles, not blood.")]),

    # --------------------------------------------------------------- nose
    dict(cond="Septal hematoma", img="l17-s042_pos2.jpg", slide=42, deck=D17, io=NOSE,
         alt="Basal view of the nose with both nasal cavities narrowed by smooth red swellings bulging from either side of the septum",
         why="Bilateral smooth swellings arising from the septum itself and narrowing both airways — blood trapped under the perichondrium.",
         wrong=[("Nasal polyps", "Those are pale gray translucent masses arising from the lateral wall, not red swellings of the septum."),
                ("Deviated nasal septum", "That displaces the septum to one side; it does not produce a swelling on both sides."),
                ("Septal perforation", "A perforation is a hole through the septum, the opposite finding to this collection of blood between the septum and its perichondrium.")]),

    dict(cond="Septal perforation", img="l17-s038_pos1.jpg", slide=38, deck=D17, io=NOSE,
         alt="Two endoscopic views of the nasal cavity showing an opening through the septum with the opposite side visible through it",
         why="There is a defect straight through the septum, so the contralateral cavity can be seen through it.",
         wrong=[("Septal hematoma", "That bulges into the airway from the septum; this one is an absence of septum."),
                ("Deviated nasal septum", "That is a septum pushed to one side but still continuous — no hole."),
                ("Nasal polyps", "Those are pale masses filling the cavity, not an opening through its dividing wall.")]),

    dict(cond="Epistaxis", img="l17-s044_pos2.jpg", slide=44, deck=D17, io=NOSE,
         alt="Fresh bright red blood running from one nostril down the upper lip",
         why="Active bleeding from the nostril, with the external nose otherwise undeformed and unbruised.",
         wrong=[("Nasal fracture", "That shows deviation, swelling and periorbital bruising; bleeding alone does not make a fracture."),
                ("Septal hematoma", "That is a swelling inside the nose seen on examination, not blood running out of it."),
                ("Nasal foreign body", "That classically gives unilateral foul discharge rather than fresh blood.")]),

    dict(cond="Nasal foreign body", img="l17-s053_pos2.jpg", slide=53, deck=D17, io=NOSE,
         alt="Close view of a child's nostril occluded by a smooth bright green object",
         why="A smooth manufactured object of a color nothing biological is, sitting in one nostril.",
         wrong=[("Nasal polyps", "Those are pale gray and translucent, and they arise from the mucosa rather than lying loose."),
                ("Epistaxis", "Epistaxis is active bleeding from the nose; the finding here is a retained object sitting in the nasal cavity, not blood."),
                ("Rhinitis", "That gives swollen boggy turbinates and clear discharge, with nothing discrete in the airway.")]),

    dict(cond="Nasal fracture", img="l17-s058_pos3.jpg", slide=58, deck=D17, io=NOSE,
         alt="Face with the nasal bridge deviated to one side, swelling over the dorsum and dried blood at both nostrils",
         why="The external nose is deviated and swollen with blood at the nares — deformity, not just bleeding.",
         wrong=[("Epistaxis", "Bleeding on its own says nothing about the bones; here the bridge is visibly displaced."),
                ("Septal hematoma", "That is an internal finding seen on examination; it does not deviate the external nose."),
                ("Nasal cellulitis", "That is diffuse redness and warmth without displacement of the bony framework.")]),

    # --------------------------------------------------------------- neck
    dict(cond="Haemangioma", img="l18-s027_pos1.jpg", slide=27, deck=D18, io=NECK,
         alt="Bright red slightly raised soft plaque with a lobulated surface on the skin behind and below the ear of an infant",
         why="A red, soft, raised vascular lesion in an infant. These vascular malformations appear in the first few months of life as a red or bluish soft, compressible mass, and most involute on their own.",
         wrong=[("Branchial cleft cyst", "That is a smooth deep swelling along the anterior border of the sternocleidomastoid, with normal skin over it."),
                ("Thyroglossal duct cyst", "That sits in the midline near the hyoid and moves on swallowing; it does not color the skin."),
                ("Cystic hygroma", "That is a soft compressible deep swelling that transilluminates, not a red surface lesion.")]),

    # --------------------------------------------------------- oral cavity
    dict(cond="Leukoedema", img="l19-s009_pos1.jpg", slide=9, deck=D19, io=ORAL,
         alt="Buccal mucosa with a diffuse grayish-white translucent film and faint surface wrinkling, fading toward the commissure",
         why="A diffuse, grayish-white, semitransparent change of the buccal mucosa — a normal variant, not a discrete lesion.",
         wrong=[("Oral leukoplakia", "That is a discrete white plaque with definite borders that cannot be rubbed off, not a diffuse translucent film."),
                ("Oral candidiasis", "Those are creamy curd-like patches on an erythematous base, and they wipe away."),
                ("Oral lichen planus", "That shows lacy white striae in a definite pattern rather than an even haze.")]),

    dict(cond="Fordyce granules", img="l19-s010_pos2.jpg", slide=10, deck=D19, io=ORAL,
         alt="Buccal mucosa scattered with numerous discrete pinpoint white-yellow papules of even size",
         why="Multiple small, discrete, white to yellow papules a millimeter or two across — ectopic sebaceous glands.",
         wrong=[("Oral candidiasis", "Those are confluent creamy plaques on red mucosa, and they can be scraped off."),
                ("Aphthous stomatitis", "Those are painful ulcers with a yellow-gray base and a red rim, not intact papules."),
                ("Leukoedema", "That is a diffuse translucent film over the mucosa, not discrete raised spots.")]),

    dict(cond="Physiologic pigmentation", img="l19-s011_pos2.jpg", slide=11, deck=D19, io=ORAL,
         alt="Gingiva with symmetrical brown-black bands along the attached gum above the upper and lower teeth",
         why="Symmetrical brown banding of the attached gingiva from increased melanin — a normal finding in darker skin types.",
         wrong=[("Amalgam tattoo", "That is a single localized gray-blue patch next to a restored tooth, not a symmetrical band."),
                ("Oral melanoma", "That would be an irregular asymmetric expanding pigmented lesion, not even bilateral banding."),
                ("Addison disease", "That pigmentation is patchy and appears with systemic illness, not as a symmetrical gingival band.")]),

    dict(cond="Aphthous stomatitis", img="l19-s015_pos1.jpg", slide=15, deck=D19, io=ORAL,
         alt="Inner lip everted to show two shallow round ulcers with pale yellow bases and thin red halos on the labial mucosa",
         why="Shallow round ulcers with a yellow-gray base and an erythematous rim on freely moving, non-keratinized mucosa.",
         wrong=[("Herpes simplex ulcers", "Those begin as clustered vesicles and favor keratinized surfaces such as the hard palate and vermilion."),
                ("Oral candidiasis", "That is a removable white plaque on red mucosa, not an ulcer with a defined rim."),
                ("Oral leukoplakia", "Leukoplakia is a white plaque that cannot be scraped off, with an intact surface; this is a painful round ulcer with a red halo.")]),

    dict(cond="Oral lichen planus", img="l19-s021_pos1.jpg", slide=21, deck=D19, io=ORAL,
         alt="Buccal mucosa with a network of fine lacy white lines over a faintly red background, next to the lower molars",
         why="Fine lacy white lines forming a network on the buccal mucosa are Wickham striae, the reticular type of oral lichen planus.",
         wrong=[("Oral leukoplakia", "That is a solid homogeneous white plaque, not a lace-like network of lines."),
                ("Oral candidiasis", "That is creamy curd-like material that wipes off; striae are within the mucosa and do not."),
                ("Leukoedema", "That is a diffuse translucent haze without any defined linear pattern.")]),

    dict(cond="Herpes simplex ulcers", img="l19-s025_pos1.jpg", slide=25, deck=D19, io=ORAL,
         alt="Mouth held open showing small ulcers with red rims at both corners of the lips and on the vermilion border",
         why="Small painful ulcers at the vermilion and perioral area, where the lesions follow a vesicular stage.",
         wrong=[("Aphthous stomatitis", "Those occur on non-keratinized mucosa inside the mouth and spare the vermilion border."),
                ("Oral candidiasis", "That is white plaque on red mucosa rather than discrete ulcers at the lip margin."),
                ("Erythroplakia", "That is a persistent red velvety patch, not an acute painful ulcer.")]),

    dict(cond="Oral candidiasis", img="l19-s089_pos3.jpg", slide=89, deck=D19, io=ORAL,
         alt="Tongue coated with thick creamy white curd-like patches sitting on a red surface, with the plaque partly lifted at one edge",
         why="Creamy white curd-like patches on an erythematous base, of the kind that can be rubbed off.",
         wrong=[("Oral leukoplakia", "That plaque is fixed to the mucosa and cannot be scraped away; this material lifts."),
                ("Oral lichen planus", "That is a lacy striated pattern within the mucosa, not removable curd."),
                ("Hairy leukoplakia", "That forms corrugated white plaques on the lateral tongue that do not detach.")]),

    dict(cond="Oral leukoplakia", img="l19-s133_pos3.jpg", slide=133, deck=D19, io=ORAL,
         alt="Lower labial mucosa with a well-defined homogeneous white plaque with a slightly wrinkled surface, the lip retracted to show it",
         why="A discrete white plaque with definite borders that cannot be wiped off and does not fit another diagnosis.",
         wrong=[("Oral candidiasis", "That is removable creamy material on a red base; this plaque is fixed."),
                ("Erythroplakia", "That is a red velvety patch, which carries a far higher risk of dysplasia."),
                ("Leukoedema", "That is a diffuse translucent film over the whole buccal mucosa, not a discrete plaque.")]),

    dict(cond="Erythroplakia", img="l19-s135_pos2.jpg", slide=135, deck=D19, io=ORAL,
         alt="Well-demarcated red velvety patch on the buccal mucosa beside the upper molars, with the surrounding mucosa normal",
         why="A persistent, well-defined red velvety patch — the red counterpart of leukoplakia, and far more often dysplastic.",
         wrong=[("Oral leukoplakia", "That is white; the color is the whole distinction being drawn here."),
                ("Oral candidiasis", "That is white plaque on red mucosa, and the plaque is the finding rather than the redness."),
                ("Aphthous stomatitis", "That is an ulcer with a yellow-gray base, not an intact red patch.")]),

    dict(cond="Hairy leukoplakia", img="l19-s136_pos1.jpg", slide=136, deck=D19, io=ORAL,
         alt="Lateral border of the tongue protruded to show a white corrugated plaque with vertical folds running along the edge",
         why="A corrugated white plaque along the lateral border of the tongue, which does not rub off.",
         wrong=[("Oral candidiasis", "That is creamy curd-like plaque that can be wiped away, and it favors the dorsum and palate."),
                ("Oral leukoplakia", "That is a smooth homogeneous plaque without the vertical corrugated folds, and it has no viral association."),
                ("Oral lichen planus", "That is a lacy striated network, most often on the buccal mucosa.")]),

    dict(cond="Gingivitis", img="l19-s122_pos2.jpg", slide=122, deck=D19, io=ORAL,
         alt="Gum margins along the upper and lower teeth that are red, rounded and swollen, with the teeth themselves intact",
         why="Erythematous and edematous gingival margins with the teeth still well seated — inflammation without attachment loss.",
         wrong=[("Periodontitis", "That has lost attachment — the gums recede, the roots show, and the teeth loosen."),
                ("Physiologic pigmentation", "That is symmetrical brown banding of healthy gingiva, with no swelling or redness."),
                ("Aphthous stomatitis", "That is a discrete ulcer, not diffuse inflammation of the gum margin.")]),

    dict(cond="Periodontitis", img="l19-s122_pos3.jpg", slide=122, deck=D19, io=ORAL,
         alt="Severely inflamed bleeding gums receded away from several teeth so the long roots are exposed, with heavy calculus deposits",
         why="The gingiva has receded and attachment has been lost, exposing the roots — the stage beyond reversible gum inflammation.",
         wrong=[("Gingivitis", "That inflames the gum margin but does not destroy attachment; the roots stay covered."),
                ("Ludwig angina", "That is a spreading infection of the floor of the mouth and neck, not localized gum disease."),
                ("Oral leukoplakia", "That is a white mucosal plaque and has nothing to do with the periodontium.")]),

    dict(cond="Ludwig angina", img="l19-s109_pos1.jpg", slide=109, deck=D19, io=ORAL,
         alt="Neck and chin grossly swollen from beneath the jaw down to the front of the neck, with the submandibular contour lost and the skin tense",
         why="Brawny bilateral swelling of the submandibular and submental region, elevating the floor of the mouth.",
         wrong=[("Peritonsillar abscess", "That is inside the throat — a bulging tonsil and a deviated uvula — without this external neck swelling."),
                ("Sialadenitis", "That swells one salivary gland alone and stays confined to it."),
                ("Cervical lymphadenitis", "That gives discrete tender nodes you can define, not diffuse brawny swelling of the whole floor.")]),

    # ---------------------------------------------------- pharynx / larynx
    dict(cond="Bacterial pharyngitis", img="l19-s073_pos1.jpg", slide=73, deck=D19, io=THROAT,
         alt="Open mouth showing both tonsils enlarged and bright red with patchy white-yellow exudate across their surfaces",
         why="Tonsils symmetrically enlarged and inflamed with exudate on the surface.",
         wrong=[("Peritonsillar abscess", "That is asymmetric — one tonsil pushed toward the midline with the uvula deviated away."),
                ("Oral candidiasis", "That plaque is creamy and wipes off, and it sits on the mucosa rather than confined to the tonsils."),
                ("Ludwig angina", "That is a swelling of the floor of the mouth and neck, not a tonsillar finding.")]),

    dict(cond="Infectious mononucleosis", img="l19-s083_pos4.jpg", slide=83, deck=D19, io=THROAT,
         alt="Throat with markedly enlarged tonsils almost meeting in the midline, covered by a thick gray-white membranous exudate",
         why="Tonsils so enlarged that they nearly meet, under a thick gray-white membranous exudate.",
         wrong=[("Peritonsillar abscess", "That is one-sided, with the uvula pushed away from the swollen side."),
                ("Bacterial pharyngitis", "That exudate is patchy on merely enlarged tonsils; this is a confluent membrane on kissing tonsils."),
                ("Ludwig angina", "That involves the floor of the mouth and neck rather than the tonsils.")]),

    dict(cond="Peritonsillar abscess", img="l19-s097_pos1.jpg", slide=97, deck=D19, io=THROAT,
         alt="Throat with one tonsil and the soft palate above it bulging toward the midline, pushing the uvula across to the opposite side",
         why="Asymmetry is the finding: one side bulges medially and the uvula is displaced away from it.",
         wrong=[("Bacterial pharyngitis", "That is symmetric — both tonsils enlarge together and the uvula stays midline."),
                ("Infectious mononucleosis", "That also enlarges both tonsils symmetrically, under a membranous exudate."),
                ("Ludwig angina", "That swells the floor of the mouth and the neck externally, not one side of the soft palate.")]),

    dict(cond="Vocal cord papillomatosis", img="l19-s049_pos1.jpg", slide=49, deck=D19, io=THROAT,
         alt="Laryngoscopic view of the vocal folds carrying several pale irregular wart-like growths along their free edges",
         why="Exophytic warty lesions on the vocal folds. This benign, noncontagious condition, also called recurrent respiratory papillomatosis, is caused by human papilloma virus subtypes 6 and 11.",
         wrong=[("Vocal cord nodules", "Those are smooth symmetrical bumps at the junction of the anterior and middle thirds, not warty excrescences."),
                ("Vocal cord polyp", "A polyp is a single unilateral, pedunculated, fluid-filled lesion on one fold, not several warty growths."),
                ("Laryngeal carcinoma", "That is an infiltrating ulcerated mass that distorts the fold, not discrete pale warty growths.")]),
]
