#!/usr/bin/env python3
"""Build the Physical Diagnosis 2, Exam 1 cram sheet.

Condensed from the exam's own study guide -- nothing here is new material, it is
the guide compressed to what is worth reading the night before. Rows preserve
exact numbers and names verbatim (the one-centimetre hinges, the ulcer stages,
the 180 degree clubbing angle) because those are precisely what gets tested.

Six topics rather than two, because the two lectures split naturally: the
encounter and documentation on one side, and on the other the skin's structure,
the descriptive vocabulary, the abnormal findings, and the technique.
"""
import sys, os
sys.path.insert(0, "/Users/jaxonluke/Developer/PA_Quizzes/tools/cram-sheet-template")
from render import render

OUT = "/Users/jaxonluke/Developer/PA_Quizzes/Physical Diagnosis 2 Exam 1/pd2-exam-1-cram-sheet.html"

topics = [
 {"id": "encounter", "label": "The Encounter, Presentation & Documentation", "color": "#4a5c24",
  "rows": [
    ["Oral presentation — opening",
     "Open with the past medical history and the chief complaint. Then pertinent positives and negatives from BOTH history and physical. Follow mostly the order you obtained them. Try not to read your notes."],
    ["Oral presentation — the test",
     "A good presentation leads your facilitator to the same differential you formulated. It is a well-organised vignette, not the written note read aloud; the goal is to help listeners visualise the patient."],
    ["Focused vs comprehensive",
     "A focused encounter narrows BOTH the history and the examination — history of present illness, review of systems, past medical history, social history, family history, medications and allergies are all focused. It is not a comprehensive encounter written up more briefly."],
    ["Focused encounter — required output",
     "Differentials, laboratory and imaging studies, a diagnosis, and a treatment plan including patient education. Narrowing the data gathered does not narrow what you must conclude."],
    ["History and physical vs SOAP",
     "The history and physical is comprehensive (whole history, head-to-toe). The SOAP note is problem-focused: Subjective (what the patient said), Objective (what you found, always with a general impression), Assessment (what you concluded), Plan (what you will do)."],
    ["Documentation rules that cost marks",
     "Describe findings — never 'normal', 'abnormal' or 'unremarkable'. NO abbreviations, with no exceptions. Keep subjective and objective in their own sections. If you did not do it, document why — never invent a finding. Never write a note with another student."],
    ["Communication",
     "Adapt style and content for each patient. When someone else supplies the answers, ALWAYS look at and interact with the patient, not the person answering. Accept feedback and modify behaviour; different facilitators give different feedback, and that is expected."],
  ]},

 {"id": "skin-structure", "label": "Skin — Structure & Function", "color": "#6b7f35",
  "rows": [
    ["Five functions",
     "Protection of internal structures · prevention of entry of microorganisms · temperature regulation · excretion · production of vitamin D."],
    ["Sudoriferous (eccrine) glands", "Secrete sweat to maintain body temperature."],
    ["Apocrine glands", "Become active during PUBERTY; secrete pheromones."],
    ["Sebaceous glands", "Surround hair follicles; secrete sebum to keep hair and skin moist."],
    ["Vellus vs terminal hair",
     "Vellus is short, fine hair covering the body. Terminal is coarse — scalp, pubic, axillary, beard."],
  ]},

 {"id": "vocabulary", "label": "Descriptive Vocabulary — Distribution & Configuration", "color": "#8a7526",
  "rows": [
    ["Five features of any lesion",
     "Distribution (location) · configuration (shape) · morphology (form and structure) · colour · texture."],
    ["Distribution → diagnosis",
     "Generalised/diffuse = allergic reactions. Regional = tinea capitis. Sun-exposed (photodistribution) = skin cancers. Dermatome = herpes zoster. Extensor = psoriasis. Flexor = intertrigo. Intertriginous = skin creases and folds."],
    ["Configuration terms",
     "Annular = ring. Arciform = arcs or curves. Confluent = run together. Discrete = remain separate. Grouped = a cluster. Gyrate = twisted, coiled, spiral. Iris/target = bull's eye. Linear = line or stripe. Reticular = lacy or networked. Serpiginous = snake-like."],
    ["Herpetiform vs zosteriform",
     "Herpetiform = grouped papules or vesicles arranged as in herpes SIMPLEX. Zosteriform = clustered in a DERMATOMAL distribution, as in herpes zoster. The pair most often swapped."],
    ["Primary vs secondary lesion",
     "Primary forms first and results directly from the disease — identifying it is the key to the whole description. Secondary is a change in the primary over time, from disease progression, TREATMENT, or MANIPULATION (picking, scratching)."],
  ]},

 {"id": "morphology", "label": "Primary & Secondary Morphology", "color": "#8f5b2a",
  "rows": [
    ["The 1 cm hinge — three matched pairs",
     "Flat: macule (<1 cm) / patch (>1 cm). Solid elevated: papule (<1 cm) / plaque (>1 cm). Fluid-filled: vesicle (<1 cm) / bulla (>1 cm). Six terms from three pairs — this is why a ruler is on the equipment list."],
    ["Nodule vs papule vs tumor",
     "Nodule: elevated, firm, circumscribed, round or ellipsoid, DEEPER in the dermis than a papule, 1–2 cm (Bates: >0.5 cm). Tumor: solid mass >2 cm. Papule: solid, <1 cm."],
    ["Plaque",
     "Elevated, flat-topped, firm, rough; plateau-like, occupying a large area compared with its elevation; >1 cm; may be coalesced papules. Example: psoriasis."],
    ["Wheal, pustule, cyst",
     "Wheal: elevated irregular cutaneous edema, solid, TRANSIENT, variable diameter (the only transient one). Pustule: superficial elevation filled with PURULENT material, usually <1 cm. Cyst: elevated, circumscribed, ENCAPSULATED, in dermis or subcutis, liquid or semisolid (the only encapsulated one)."],
    ["Erosion vs ulcer",
     "Erosion: loss of superficial epidermis, does NOT involve dermis; moist but does NOT bleed. Ulcer: deeper loss of epidermis and/or dermis; MAY bleed and scar. Depth determines all three consequences at once."],
    ["Crust, fissure, scale, excoriation",
     "Crust: cellular debris, dried serum and blood — a scab; antecedent lesion usually a vesicle, bulla or pustule. Fissure: linear crack (athlete's foot). Scale: thin flake of exfoliated epidermis (dandruff). Excoriation: abrasion or scratch mark, linear or rounded."],
    ["Scar vs keloid",
     "Scar (cicatrix): fibrous tissue replacing destroyed tissue; hypertrophic = thick and pink, atrophic = thin and white; does NOT extend beyond the injured area. Keloid: a scar that GROWS BEYOND the wound."],
    ["Lichenification & collarette scale",
     "Lichenification: thickening with skin line accentuation from chronic irritation (atopic dermatitis). Collarette scale: fine scale peripherally attached and centrally detached at a lesion's edge (pityriasis rosea)."],
    ["Corn vs callus; warts",
     "Corn: smaller, usually over a NON-weight-bearing area of the foot, conical keratin pointing toward the dermis. Callus: thickened epidermal keratin, usually on the sole at ball or heel. Verrucae (warts) are caused by human papillomavirus."],
  ]},

 {"id": "abnormal", "label": "Abnormal Findings — Skin, Hair & Nails", "color": "#7d3f52",
  "rows": [
    ["Diascopy",
     "Press clear glass or plastic against the skin and look at the lesion under pressure. Colour FADES = vascular engorgement. Does NOT fade = hemorrhage in the skin."],
    ["Petechiae / purpura / ecchymosis",
     "Same finding at three sizes, NONE blanching. Petechiae <3 mm. Purpura 3 mm–1 cm. Ecchymosis >1 cm, purple or purplish-blue, fades over time."],
    ["Angiomas & telangiectasia",
     "Cherry angioma (Campbell De Morgan spots): dome shaped, bright red to violet/black, ± blanching. Telangiectasia: fine irregular vessels, blanches. Spider angioma: central red macule with radiating arms, blanches."],
    ["Triple response of Lewis",
     "Firm stroking (dermatographism) produces: initial red line (capillary dilatation) → reflex flare with broadening erythema (arteriolar dilatation) → linear wheal (transudation of fluid, i.e. edema)."],
    ["Pressure ulcer stages",
     "I: INTACT skin, erythema failing to blanch, plus change in temperature, consistency, sensation, colour. II: PARTIAL thickness loss (epidermis, dermis or both). III: FULL thickness, subcutaneous necrosis, may extend to but NOT through muscle. IV: full thickness with destruction of tissue, muscle and/or bone."],
    ["Tinea by site",
     "Corporis (body) · pedis (foot) · barbae (beard) · cruris (groin) · capitis (scalp) · unguium (nails). Pedis: dry/scaling or macerated fissuring of interdigital spaces. Corporis: sharply demarcated round plaques with CENTRAL CLEARING. Capitis: round scaling patches of alopecia, hairs broken off close to scalp."],
    ["Skin malignancies",
     "Basal cell carcinoma: face; translucent PEARLY nodule, depressed centre, raised borders; may ulcerate; non-healing ulcer. Squamous cell carcinoma: face and sun-exposed; red scaling, crusting nodule or plaque that ulcerates and bleeds. Melanoma: irregularly coloured plaque with sharp notches and pigment variation."],
    ["Melanoma warning letters",
     "A asymmetry or shape · B border irregularity · C colour variation · D diameter larger than 6 mm · E evolving, elevation · F family history · G growing."],
    ["Kaposi's sarcoma",
     "The most frequent neoplasm in patients with acquired immunodeficiency syndrome. Light-coloured lesions coalescing into darker ones; dark blue-purple macules, papules, nodules and plaques; widely disseminated on legs, trunk, arms, neck and head."],
    ["Patchy hair loss — three causes",
     "Tinea capitis: SCALING patches, hairs broken close to scalp. Alopecia areata: round patches, 'EXCLAMATION POINT' hairs, chronic inflammatory disease of follicles, associated with autoimmune disorders. Trichotillomania: from an urge to pull, single or multiple patches. Also: androgenic alopecia = male pattern baldness; hirsutism = increased hair in women in a male pattern."],
    ["Nail findings",
     "Koilonychia: spoon-shaped concave, plate thins and inverts. Onycholysis: PAINLESS separation of plate from bed starting DISTALLY (chemicals, immersion, fungal, psoriasis, tetracycline, trauma). Pitting: dystrophy of the plate. Terry's nails: proximal white, distal dark. Green = pseudomonas. Brown–black = MELANOMA."],
    ["Nail lines, hemorrhages, clubbing",
     "Beau's lines: transverse DEPRESSIONS — halfway up the nail suggests illness about 3 MONTHS ago. Mee's lines: transverse lines. Splinter hemorrhages: distal capillary loop. Subungual hematoma: hemorrhage to the nail plate. Clubbing: nail base-to-finger angle GREATER THAN 180°, fingertip rounded and bulbous. Paronychia: soft tissue infection at cuticle or nail fold; acute is painful and purulent."],
  ]},

 {"id": "technique", "label": "Performing the Skin Examination", "color": "#3f5b6b",
  "rows": [
    ["IPPA",
     "Inspection, palpation, percussion, auscultation — the same order for EVERY body system except the ABDOMINAL examination. Some systems do not use all four."],
    ["Equipment & environment",
     "Ruler, light source, magnifying lens, gloves for open lesions. Patient in a gown so hair, anterior and posterior surfaces, palms and soles, nails and interdigital spaces can all be inspected. Good light, preferably NATURAL — artificial light may distort skin tone."],
    ["Six characteristics assessed",
     "Colour · moisture (dryness, sweating, oiliness) · temperature (warmth, coolness) · texture (roughness, smoothness) · mobility and turgor · lesions."],
    ["Temperature technique",
     "Use the DORSAL aspect of the hands."],
    ["Mobility vs turgor",
     "Mobility: normal skin lifts with ease; reduced mobility = EDEMA. Turgor: normal skin quickly resumes its shape; skin that remains elevated = DEHYDRATION."],
    ["Central vs peripheral cyanosis",
     "Central: often inadequate oxygenation IN THE LUNGS. Peripheral: usually inadequate CIRCULATION. Same colour, different organ."],
    ["Hair & scalp",
     "Inspect colour, distribution and quantity; palpate for texture. Separate the hair into sections to see the scalp, and inspect BEHIND THE EARS and the OCCIPUT. Should be clean — no lesions, discolorations, flaking or parasites. A magnifying glass aids inspection for lice (nits are tiny white ovoid granules adherent to hairs)."],
    ["Pruritus is not a diagnosis",
     "It is the sensation causing the desire to scratch. Generalised itching with no obvious reason: dry skin, ageing, pregnancy, uremia, jaundice, lymphomas, leukemias, drug reaction, lice."],
    ["History — bugs, drugs, contact",
     "Bugs: family members or contacts with the same, travel. Drugs: systemic medications, over-the-counter AND prescription. Contact: allergens and irritants from hobbies, occupation, environment. Core questions: where it first appeared, what it looked like, how it progressed, associated symptoms, what treatment was tried."],
  ]},
]

html = render(
    title="Cram Sheet — Physical Diagnosis 2 Exam 1",
    kicker="Physical Diagnosis 2 Exam 1 · Class of 2028",
    h1="Physical Diagnosis 2 Exam 1 Cram Sheet",
    sub="The encounter, the oral presentation and documentation; then the skin — structure, the descriptive vocabulary, abnormal findings of skin, hair and nails, and the examination itself.",
    topics=topics,
    guide_href="pd2-exam-1-study-guide.html",
    footer_note="Condensed from the Physical Diagnosis 2 Exam 1 Study Guide (Class of 2028). Covers Lectures 1 and 2; Ophthalmology and ENT are added as those decks are posted. For the full explanation behind any of these, see the full guide.",
)
open(OUT, "w", encoding="utf-8").write(html)
rows = sum(len(t["rows"]) for t in topics)
print("wrote %s (%d KB, %d topics, %d rows)"
      % (os.path.basename(OUT), len(html) // 1024, len(topics), rows))
