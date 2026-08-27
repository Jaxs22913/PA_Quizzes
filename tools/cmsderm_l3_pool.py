# -*- coding: utf-8 -*-
"""Dermatology II -- question pool for the Updated CMS derm master exams."""
DECK = "3. Dermatology  II.pptx"
IO = ("a — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
      "differential diagnosis, diagnostic testing, management, appropriate referrals, patient education, "
      "and prognosis of dermatological conditions")

def Q(topic, q, opts, c, slide):
    return {"topic": topic, "io": IO, "q": q, "opts": opts, "c": c, "cite": f"{DECK}, Slide {slide}"}

QUESTIONS = [

Q("Erythema multiforme",
  "A 26-year-old man presents with a rash that began on the backs of his hands and spread toward the trunk over two "
  "days. Examination shows numerous lesions with three concentric zones — a dusky centre, a pale ring, and an "
  "erythematous outer rim — on the dorsal hands, forearms, and knees. Individual lesions have remained fixed in place "
  "for four days. He had a cold sore on his lip ten days ago. Less than 5 percent of his body surface is involved and "
  "there are no mucosal erosions. What is the most likely trigger?",
  [["Herpes simplex virus",
    "Correct. Over 50 percent of erythema multiforme cases are triggered by herpes simplex virus, making it the most "
    "common precipitant, and a history of recurrent infection is a listed risk factor. The cold sole ten days before "
    "the eruption supplies exactly that history."],
   ["Mycoplasma pneumoniae",
    "Mycoplasma pneumoniae is a genuine infectious cause and is the one most associated with mucosal disease, but the "
    "stem records no respiratory illness and no mucosal erosions. Herpes simplex virus remains the single most common "
    "precipitant."],
   ["A sulfonamide antibiotic",
    "Sulfonamides are among the recognised drug triggers along with non-steroidal anti-inflammatory drugs, "
    "penicillins, and anticonvulsants. No medication exposure is reported, and drug triggers account for a minority "
    "of cases."],
   ["Epstein-Barr virus",
    "Epstein-Barr virus appears among the other infectious causes alongside histoplasmosis and coxsackievirus, but "
    "these are uncommon relative to herpes simplex virus and nothing in the history points to a mononucleosis-like "
    "illness."],
   ["No identifiable trigger",
    "Idiopathic causes account for roughly 10 percent of cases, so this is possible in general but not here — a "
    "herpetic lesion ten days before the eruption is precisely the trigger the history was taken to find."]],
  0, 8),

Q("Erythema multiforme",
  "A clinician is distinguishing erythema multiforme from urticaria in a patient with an annular eruption. What "
  "feature most reliably separates them?",
  [["Urticarial wheals are migratory and individual lesions last less than 24 hours, whereas erythema multiforme "
    "produces fixed target lesions",
    "Correct. The differential states that urticarial wheals are pruritic, migratory, and blanch fully, with no fixed "
    "target lesions and individual lesions lasting less than 24 hours. Fixity over days is what identifies erythema "
    "multiforme."],
   ["Urticarial wheals are fixed for several days whereas erythema multiforme lesions migrate hourly",
    "This reverses the behaviour of the two eruptions. A clinician applying it would mark a migratory urticarial "
    "eruption as erythema multiforme and pursue an unnecessary search for a herpetic or mycoplasmal trigger."],
   ["Only erythema multiforme is pruritic",
    "Urticaria is characteristically pruritic, and erythema multiforme is managed in part with oral antihistamines "
    "for pruritus. Itch is present in both and separates neither."],
   ["Only urticaria involves the extremities",
    "Erythema multiforme is characteristically acral, favouring the dorsal hands, forearms, and knees. Distribution "
    "does not exclude urticaria, which can appear anywhere."],
   ["Only erythema multiforme blanches with pressure",
    "Urticarial wheals blanch fully, which is one of their listed features. Blanching is therefore a property of the "
    "alternative diagnosis rather than of erythema multiforme."]],
  0, 10),

Q("Dermatitis herpetiformis",
  "A 31-year-old man of Northern European ancestry presents with an intensely pruritic, burning eruption of grouped "
  "small vesicles and papules symmetrically distributed over the elbows, knees, and buttocks. Most lesions are "
  "excoriated. He has autoimmune thyroid disease. What direct immunofluorescence finding is expected on perilesional "
  "skin?",
  [["Granular immunoglobulin A deposits in the dermal papillae",
    "Correct. Dermatitis herpetiformis is caused by immunoglobulin A antibodies against epidermal transglutaminase in "
    "genetically susceptible individuals consuming gluten. The immune complexes deposit in the dermal papillae, and "
    "perilesional direct immunofluorescence showing granular immunoglobulin A is the gold standard test."],
   ["Linear immunoglobulin G and complement C3 at the basement membrane zone",
    "Linear immunoglobulin G and complement C3 at the basement membrane zone is the bullous pemphigoid pattern, and "
    "the differential states explicitly that direct immunofluorescence distinguishes the two. Bullous pemphigoid also "
    "produces tense blisters in the elderly rather than grouped excoriated vesicles on extensor surfaces."],
   ["Intercellular immunoglobulin G in a net-like pattern throughout the epidermis",
    "A net-like intercellular pattern is the pemphigus finding, reflecting antibodies against keratinocyte adhesion "
    "molecules. Pemphigus presents with flaccid bullae and mucosal erosions rather than a pruritic extensor "
    "eruption."],
   ["No immune deposits, with mites identified on skin scraping",
    "That describes scabies, which is on the differential because it also itches intensely. Scabies shows burrows in "
    "the web spaces and a positive skin scraping with no immunoglobulin A deposits."],
   ["Band-like lymphocytic infiltration of the upper dermis",
    "A band-like lymphocytic infiltrate is the histological signature of lichen planus, which produces pruritic "
    "violaceous flat-topped papules rather than grouped vesicles on extensor surfaces."]],
  0, 125),

Q("Dermatitis herpetiformis",
  "A patient is diagnosed with dermatitis herpetiformis and dapsone is planned for rapid symptom control. What must "
  "be checked before the drug is started, and what must be monitored afterwards?",
  [["Check glucose-6-phosphate dehydrogenase status beforehand, and monitor the complete blood count for haemolytic "
    "anaemia and methaemoglobinaemia",
    "Correct. Glucose-6-phosphate dehydrogenase deficiency must be checked before initiating dapsone, and the "
    "complete blood count is monitored for haemolytic anaemia and methaemoglobinaemia. Dapsone at 25 to 200 mg daily "
    "gives relief within days."],
   ["Check glucose-6-phosphate dehydrogenase status beforehand, and monitor renal function for nephrotoxicity",
    "The pre-treatment check is right, which makes this the closest wrong answer, but the monitoring target is wrong. "
    "Dapsone's characteristic toxicities are haematological, and following renal function instead would miss the "
    "haemolysis it is prescribed to detect."],
   ["Check thyroid function beforehand, and monitor the complete blood count for haemolytic anaemia",
    "Autoimmune thyroid disease is an associated condition worth screening for in its own right, but it is not the "
    "safety check that governs dapsone initiation."],
   ["Check liver function beforehand, and monitor for photosensitivity",
    "Neither is the specific safety pairing for dapsone. Photosensitivity is a consideration for topical retinoids "
    "and for drug-induced photosensitivity reactions rather than a dapsone concern."],
   ["No pre-treatment testing is required, and no specific monitoring is needed",
    "Omitting the glucose-6-phosphate dehydrogenase check exposes a deficient patient to severe haemolysis. This is "
    "the most dangerous option in the set."]],
  0, 19),

Q("Dermatitis herpetiformis",
  "A patient with dermatitis herpetiformis achieves rapid relief on dapsone and asks whether that is the whole "
  "treatment. What is the most important additional element of management?",
  [["A strict lifelong gluten-free diet, since the condition is intrinsically linked to gluten sensitivity",
    "Correct. Dapsone provides rapid symptom relief but the long-term management is a strict gluten-free diet, "
    "because the disease is driven by immunoglobulin A antibodies against epidermal transglutaminase in patients "
    "consuming dietary gluten. All patients should also be screened for celiac disease."],
   ["Indefinite dapsone monotherapy, since dietary change does not affect the skin disease",
    "This is directly contrary to the mechanism: removing gluten removes the antigenic drive. Committing the patient "
    "to indefinite dapsone with its haematological toxicity while leaving the cause in place is the wrong trade."],
   ["A strict gluten-free diet for six weeks, after which gluten may be reintroduced",
    "The dietary restriction is lifelong rather than a time-limited trial. Reintroducing gluten restores the antigen "
    "and with it the eruption and the celiac disease risk."],
   ["High-potency topical steroids as the sole long-term therapy",
    "Topical high-potency steroids are used for localised flares, not as the long-term strategy. They do nothing "
    "about the systemic gluten-driven process or the associated celiac disease."],
   ["Lifelong systemic corticosteroids",
    "Systemic corticosteroids are not part of the described management of this condition, and long-term use would "
    "add substantial toxicity without addressing the gluten drive."]],
  0, 19),

Q("Acanthosis nigricans",
  "A 68-year-old man who has lost 9 kg without trying is found to have new velvety hyperpigmented thickening of the "
  "axillae, neck, and, unusually, the palms and oral mucosa, which developed rapidly over three months. He is not "
  "obese and his fasting glucose is normal. What is the most appropriate concern?",
  [["Paraneoplastic acanthosis nigricans, particularly from a gastrointestinal malignancy",
    "Correct. Malignant acanthosis nigricans is paraneoplastic, especially with gastrointestinal adenocarcinoma. "
    "Rapid onset, unusual sites including the palms and mucosa, and the absence of obesity or insulin resistance in "
    "an older patient with weight loss all point away from the common benign form."],
   ["Insulin-resistant benign acanthosis nigricans",
    "This is the most common form, driven by hyperinsulinaemia stimulating keratinocyte and fibroblast proliferation, "
    "and it is the right answer in most patients. Here the normal glucose, absent obesity, rapid onset, and mucosal "
    "involvement all argue against it."],
   ["Confluent and reticulated papillomatosis",
    "Confluent and reticulated papillomatosis has a reticulate pattern and responds to minocycline. It does not "
    "involve the oral mucosa or carry a paraneoplastic association."],
   ["Postinflammatory hyperpigmentation",
    "Postinflammatory hyperpigmentation requires a history of prior inflammation at the affected site and produces "
    "flat pigment change rather than velvety thickening."],
   ["A medication effect from niacin or a systemic corticosteroid",
    "Niacin and systemic corticosteroids are listed among the drug causes, so a medication history should be taken. "
    "But no such drug is reported, and drug-induced disease does not explain mucosal and palmar involvement with "
    "weight loss."]],
  0, 22),

Q("Epidermolysis bullosa",
  "A neonate develops blisters at sites of handling and diapering. Genetic testing is planned. Which subtype carries "
  "the greatest long-term risk of squamous cell carcinoma and requires the most intensive multidisciplinary "
  "surveillance?",
  [["Dystrophic epidermolysis bullosa",
    "Correct. Dystrophic epidermolysis bullosa causes severe scarring, and the multidisciplinary team includes "
    "haematology and oncology specifically for squamous cell carcinoma surveillance. Scarring subtypes carry the "
    "malignancy risk."],
   ["Epidermolysis bullosa simplex",
    "Simplex disease results from keratin 5 and 14 mutations with intraepidermal cleavage, is localised to the palms "
    "and soles, and heals without scarring. Absence of scarring is why it does not carry the same malignancy "
    "burden."],
   ["Junctional epidermolysis bullosa",
    "Junctional disease is generalised with poor wound healing, nail dystrophy, and enamel defects, and it is severe. "
    "But the scarring that drives squamous cell carcinoma surveillance characterises the dystrophic form."],
   ["Kindler syndrome",
    "Kindler syndrome is a recognised form within the classification but is not the subtype singled out for scarring "
    "and squamous cell carcinoma surveillance in this lecture."],
   ["Acquired epidermolysis bullosa",
    "Epidermolysis bullosa acquisita is an autoimmune rather than inherited disease and falls outside the four "
    "inherited types classified by cleavage level."]],
  0, 30),

Q("Epidermolysis bullosa",
  "What diagnostic test is considered the gold standard for establishing the level of cleavage in epidermolysis "
  "bullosa?",
  [["Skin biopsy with transmission electron microscopy",
    "Correct. Skin biopsy with transmission electron microscopy is the gold standard for determining the cleavage "
    "plane. Immunofluorescence antigen mapping localises missing or reduced proteins, and genetic testing is "
    "confirmatory and guides prognosis and family counselling."],
   ["Immunofluorescence antigen mapping",
    "Immunofluorescence antigen mapping is genuinely part of the workup and localises missing or reduced proteins, "
    "which makes it the closest wrong answer. But the gold standard for the cleavage plane itself is electron "
    "microscopy."],
   ["Genetic testing alone",
    "Genetic testing is confirmatory and guides prognosis and family counselling, but it is not the test that "
    "establishes where in the skin the split occurs."],
   ["Direct immunofluorescence for immunoglobulin A deposits",
    "Granular immunoglobulin A in the dermal papillae is the finding of dermatitis herpetiformis. Epidermolysis "
    "bullosa is an inherited structural protein disorder rather than an immune deposition disease."],
   ["Potassium hydroxide preparation of blister fluid",
    "A potassium hydroxide preparation detects fungal elements and has no role in a mechanobullous genetic disorder."]],
  0, 31),

Q("Urticaria",
  "A 33-year-old woman presents with widespread itchy wheals that have been appearing and disappearing for three "
  "days. Individual lesions last a few hours, blanch fully, and leave no mark. There is no fever, no joint pain, and "
  "no bruising at resolved sites. What is the most appropriate first-line treatment?",
  [["A second-generation antihistamine such as cetirizine, loratadine, or fexofenadine",
    "Correct. Second-generation antihistamines are first-line for urticaria. Urticaria results from mast cell "
    "degranulation releasing histamine, prostaglandins, and leukotrienes, causing transient dermal oedema."],
   ["A short course of oral prednisone at 40 to 60 mg for five days",
    "A short prednisone course is reserved for severe acute urticaria. This eruption is uncomfortable but not severe, "
    "so beginning with a systemic corticosteroid escalates past the effective first-line agent."],
   ["Intramuscular epinephrine 0.3 mg",
    "Epinephrine is given immediately for anaphylaxis. There is no airway, respiratory, or circulatory compromise "
    "described here, so this treats a far more severe condition than the patient has."],
   ["A first-generation antihistamine such as diphenhydramine taken around the clock",
    "First-generation antihistamines are sedating, and the second-generation agents are the ones named as first line. "
    "Scheduled diphenhydramine imposes sedation without added benefit."],
   ["A skin biopsy before any treatment is started",
    "Biopsy is indicated when urticarial vasculitis is suspected — lesions persisting beyond 24 hours and leaving "
    "bruising. This patient's lesions last hours and leave no mark, so those features are specifically absent."]],
  0, 39),

Q("Urticaria",
  "A 40-year-old woman has had urticarial lesions for two months. Individual lesions persist for more than 24 hours "
  "and resolve leaving brownish discoloration. She reports arthralgia. What should be suspected, and what test "
  "supports it?",
  [["Urticarial vasculitis, supported by low complement and a biopsy showing leukocytoclastic vasculitis",
    "Correct. Urticarial vasculitis is distinguished by lesions persisting beyond 24 hours that leave bruising, with "
    "low complement levels and a biopsy showing leukocytoclastic vasculitis. Ordinary wheals blanch fully and last "
    "under 24 hours."],
   ["Ordinary chronic urticaria, supported by a normal complement level",
    "Chronic urticaria is common in women aged 20 to 40, which makes this tempting, but its individual lesions last "
    "less than 24 hours and leave no residual mark. The persistence and bruising are the findings that force a "
    "different diagnosis."],
   ["Hereditary angioedema, supported by low C4 and abnormal C1-esterase inhibitor function",
    "Hereditary angioedema is considered when angioedema occurs without wheals, and C4 with C1-esterase inhibitor "
    "level and function are the right tests for it. This patient has wheals, which points away from it."],
   ["Mastocytosis, supported by a positive Darier sign",
    "Mastocytosis is on the differential and Darier sign is its characteristic finding, but it does not produce "
    "lesions that resolve with bruising alongside arthralgia."],
   ["Anaphylaxis, supported by a raised serum tryptase",
    "Anaphylaxis is an acute systemic emergency rather than a two-month eruption. Nothing in this presentation "
    "suggests airway, respiratory, or circulatory involvement."]],
  0, 38),

Q("Erythema nodosum",
  "A 29-year-old woman presents with painful red lumps on both shins that appeared ten days ago. Examination shows "
  "bilateral tender erythematous nodules 1 to 5 cm on the anterior tibial surfaces. None has ulcerated, and several "
  "are fading to a bruise-like colour. She had a sore throat three weeks ago. What is the key distinguishing feature "
  "of this condition?",
  [["The nodules do not ulcerate",
    "Correct. That the nodules do not ulcerate is named as the key distinguishing feature. Erythema nodosum is a "
    "septal panniculitis without vasculitis, evolving over 3 to 6 weeks from bright red through the bruise-like "
    "colours the stem describes."],
   ["The nodules are located on the anterior shins",
    "The anterior tibial surface is the characteristic location and it supports the diagnosis, but the nodules may "
    "also appear on the thighs, forearms, and trunk. Site is typical rather than distinguishing."],
   ["The nodules are bilateral",
    "Bilateral involvement is characteristic and helps separate it from a unilateral infectious process, but many "
    "panniculitides and vasculitides are also bilateral."],
   ["The nodules are tender",
    "Tenderness is a defining symptom of the condition but is shared with cellulitis, thrombophlebitis, and other "
    "painful nodular processes of the leg."],
   ["The nodules followed a streptococcal infection",
    "Group A Streptococcus is the most common infectious trigger, and a throat culture with an antistreptolysin O "
    "titre is used to look for it. A trigger supports the diagnosis without being a feature of the lesions "
    "themselves."]],
  0, 43),

Q("Erythema nodosum",
  "A patient with biopsy-confirmed erythema nodosum has bilateral hilar lymphadenopathy on chest radiograph together "
  "with fever and arthralgia. What is the most appropriate referral?",
  [["Pulmonology or rheumatology, for probable Löfgren syndrome",
    "Correct. Löfgren syndrome is the association referred to pulmonology or rheumatology. The combination of "
    "erythema nodosum, bilateral hilar lymphadenopathy, fever, and arthralgia is its recognised presentation."],
   ["Gastroenterology, for probable inflammatory bowel disease",
    "Gastroenterology referral is appropriate when inflammatory bowel disease is suspected, and inflammatory bowel "
    "disease is a genuine systemic association. But it would not explain bilateral hilar lymphadenopathy."],
   ["Infectious disease, for probable endemic mycosis",
    "Infectious disease referral is for endemic mycoses or tuberculosis, both of which can cause erythema nodosum. "
    "The specific triad here names a different syndrome."],
   ["Dermatology, for repeat biopsy",
    "Dermatology referral is for atypical or biopsy-confirmed cases, and a biopsy has already been done. Repeating it "
    "would not address the systemic findings."],
   ["Haematology, for probable lymphoma",
    "Lymphoma is not among the listed associations of erythema nodosum, and the described triad has a specific "
    "recognised name that points elsewhere."]],
  0, 45),

Q("Granuloma annulare",
  "A 32-year-old woman has an asymptomatic ring of flesh-coloured to erythematous papules on the dorsum of her hand "
  "that has slowly enlarged over months. There is no scale. A potassium hydroxide preparation is negative. What "
  "finding on punch biopsy would confirm the diagnosis?",
  [["Palisading granulomas with central necrobiosis and mucin deposition",
    "Correct. Granuloma annulare shows palisading granulomas with central necrobiosis and mucin deposition, "
    "reflecting a type IV delayed hypersensitivity reaction forming granulomas around degenerating collagen."],
   ["Septal panniculitis without vasculitis, with Miescher's granulomas",
    "Septal panniculitis without vasculitis and Miescher's granulomas is the erythema nodosum biopsy finding. That "
    "condition produces tender non-ulcerating nodules in the subcutaneous fat rather than an annular ring of surface "
    "papules."],
   ["A dense dermal neutrophilic infiltrate without organisms",
    "A neutrophilic dermatosis without organisms suggests pyoderma gangrenosum, which produces rapidly expanding "
    "painful ulceration with undermined violaceous borders rather than an asymptomatic annular plaque."],
   ["Hyphae within the stratum corneum",
    "Hyphae would indicate tinea corporis, the principal clinical mimic of an annular plaque. The negative potassium "
    "hydroxide preparation and the absence of scale already argue against it."],
   ["Band-like lymphocytic infiltration of the upper dermis",
    "A band-like lymphocytic infiltrate is the lichen planus pattern, which produces pruritic violaceous flat-topped "
    "papules rather than an asymptomatic annular ring."]],
  0, 51),

Q("Granuloma annulare",
  "A patient is found to have hundreds of small papules over the trunk and extremities consistent with generalised "
  "granuloma annulare. What screening is most appropriate?",
  [["Fasting glucose and haemoglobin A1c to screen for diabetes",
    "Correct. Fasting glucose and haemoglobin A1c are used to screen for diabetes in generalised granuloma annulare, "
    "alongside a lipid panel and thyroid studies for associated systemic disease."],
   ["Chest radiograph to screen for bilateral hilar lymphadenopathy",
    "Bilateral hilar lymphadenopathy belongs to the erythema nodosum workup, where it raises Löfgren syndrome. It is "
    "not the screening priority for generalised granuloma annulare."],
   ["Immunoglobulin A tissue transglutaminase antibodies to screen for celiac disease",
    "Celiac screening is the high-priority association for dermatitis herpetiformis, where all patients should be "
    "screened. Granuloma annulare has a different set of associations."],
   ["Colonoscopy to screen for gastrointestinal malignancy",
    "Gastrointestinal malignancy screening is driven by malignant acanthosis nigricans, which is paraneoplastic. "
    "Granuloma annulare is a benign self-limiting granulomatous dermatosis."],
   ["No screening is indicated for any variant of the condition",
    "The localised variant is largely a clinical diagnosis needing little workup, but the generalised form carries "
    "specific screening recommendations. Applying the localised approach to disseminated disease would miss them."]],
  0, 51),

Q("Pyoderma gangrenosum",
  "A 44-year-old woman with ulcerative colitis develops a painful pustule on the shin that has enlarged over five "
  "days into a 6 cm ulcer with an undermined violaceous border. Wound cultures are negative. A surgical team proposes "
  "sharp debridement. What is the most important management principle?",
  [["Avoid debridement, because pathergy worsens the ulcer",
    "Correct. Debridement must be avoided in pyoderma gangrenosum because pathergy — worsening with trauma — is a "
    "defining feature. Wound care uses moist dressings and non-adherent contact layers instead."],
   ["Proceed with debridement to remove devitalised tissue and speed healing",
    "This is the intervention the lecture specifically warns against. Trauma to a pathergic ulcer enlarges it, so the "
    "operation intended to help is the thing most likely to cause harm."],
   ["Begin broad-spectrum intravenous antibiotics as definitive therapy",
    "Pyoderma gangrenosum is a neutrophilic dermatosis and is not infectious despite its name, and the cultures are "
    "negative. Antibiotics treat the secondary infection if one develops but are not the definitive therapy."],
   ["Obtain an ankle-brachial index and begin compression therapy",
    "Arterial and venous studies belong to the exclusion of vascular insufficiency ulcers, which is a reasonable part "
    "of the workup. But this ulcer's undermined violaceous border and rapid painful expansion in a patient with "
    "inflammatory bowel disease point elsewhere."],
   ["Apply a dry adherent dressing changed twice daily",
    "Wound care calls for moist dressings such as foam or hydrocolloid with non-adherent contact layers. Adherent "
    "dressings inflict repeated trauma at every change, which is the pathergic stimulus to avoid."]],
  0, 60),

Q("Pyoderma gangrenosum",
  "What is the most accurate description of how pyoderma gangrenosum is diagnosed?",
  [["It is a diagnosis of exclusion, requiring infectious, vascular, and other causes to be ruled out",
    "Correct. Pyoderma gangrenosum is explicitly a diagnosis of exclusion. Infectious ulcers, which are culture "
    "negative in pyoderma gangrenosum, and vascular insufficiency ulcers assessed by ankle-brachial index must be "
    "ruled out."],
   ["It is confirmed by a specific biopsy finding that establishes the diagnosis",
    "Biopsy supports the diagnosis and helps exclude alternatives, but there is no pathognomonic histological finding "
    "that confirms it. Treating a biopsy as confirmatory risks anchoring on the wrong diagnosis."],
   ["It is confirmed by wound culture growing a characteristic organism",
    "Cultures are negative in pyoderma gangrenosum, and that negativity is used to exclude infectious ulcers. Growth "
    "of an organism would point away from the diagnosis."],
   ["It is confirmed by a positive pathergy skin test in all patients",
    "Pathergy is a clinical feature — worsening with trauma or debridement — rather than a validated confirmatory "
    "test performed on every patient."],
   ["It is confirmed by the presence of inflammatory bowel disease",
    "Inflammatory bowel disease is a key associated condition, and it raises suspicion substantially, but the "
    "association is not diagnostic on its own."]],
  0, 59),

Q("Acne rosacea",
  "A 45-year-old fair-skinned woman reports facial flushing that worsens with sun exposure, hot drinks, and alcohol. "
  "Examination shows persistent central facial erythema with telangiectasias across the cheeks and nose, and she "
  "describes her skin as stinging easily. There are no papules, no pustules, and no comedones. What subtype does she "
  "have?",
  [["Erythematotelangiectatic rosacea",
    "Correct. The erythematotelangiectatic subtype produces persistent central facial erythema, flushing, and "
    "telangiectasias with sensitive stinging skin, and specifically no papules or pustules. It is the most common "
    "subtype."],
   ["Papulopustular rosacea",
    "The papulopustular subtype adds transient central facial papules and pustules on a background of erythema. The "
    "examination here records neither, which is the single finding separating the two subtypes."],
   ["Phymatous rosacea",
    "Phymatous rosacea produces tissue hypertrophy, classically rhinophyma of the nose, and is the subtype for which "
    "female sex is not a risk factor. No hypertrophic change is described."],
   ["Ocular rosacea",
    "Ocular rosacea affects the eyes and warrants urgent ophthalmology referral when there is keratitis, visual "
    "symptoms, or corneal involvement. No ocular symptoms are reported."],
   ["Acne vulgaris",
    "Acne vulgaris is distinguished by open and closed comedones in younger patients with a perioral and chin "
    "distribution, and it lacks persistent flushing. The absence of comedones is what excludes it."]],
  0, 66),

Q("Acne rosacea",
  "A patient with papulopustular rosacea has Demodex-associated disease that has not responded to topical "
  "metronidazole. What topical agent is described as superior for this situation?",
  [["Ivermectin 1 percent cream",
    "Correct. Ivermectin 1 percent cream is described as superior to metronidazole for Demodex-associated "
    "papulopustular rosacea, reflecting the contribution of Demodex folliculorum mite overgrowth to the "
    "pathogenesis."],
   ["Azelaic acid 15 to 20 percent",
    "Azelaic acid is effective for both papulopustular and erythematotelangiectatic rosacea through "
    "anti-inflammatory and anti-keratinising effects, so it is a legitimate option. But it is not the agent singled "
    "out for Demodex-associated disease."],
   ["Brimonidine gel",
    "Brimonidine is a topical vasoconstrictor aimed at the erythema of rosacea rather than at the inflammatory "
    "papules and pustules or the mite burden."],
   ["Metronidazole 0.75 to 1 percent gel at a higher frequency",
    "Metronidazole is the first-line topical for papulopustular disease, and it has already failed here. Increasing "
    "the frequency of an agent described as inferior for Demodex-associated disease does not address the reason it "
    "failed."],
   ["A high-potency topical corticosteroid",
    "Facial corticosteroids drive perioral dermatitis and can worsen rosacea, and they are not part of its "
    "management."]],
  0, 69),

Q("Hyperhidrosis",
  "A 17-year-old girl reports excessive sweating of both palms, soles, and axillae since early adolescence. She "
  "reports no sweating during sleep. Her father had the same problem. Thyroid studies and glucose are normal. What "
  "does this pattern indicate, and what is the appropriate first-line treatment?",
  [["Primary focal hyperhidrosis, treated first with topical aluminium chloride 20 percent applied nightly",
    "Correct. Absence of nocturnal sweating and symmetry favour primary hyperhidrosis, which begins in adolescence, "
    "is bilateral and focal, and often follows an autosomal dominant family pattern. Aluminium chloride 20 percent "
    "applied nightly to dry skin is first-line topical therapy."],
   ["Primary focal hyperhidrosis, treated first with botulinum toxin A injections",
    "The diagnosis is right but the treatment is out of sequence. Botulinum toxin A is a dermatology referral option "
    "for refractory disease rather than the first-line agent, and starting there skips an effective topical."],
   ["Secondary hyperhidrosis, requiring endocrine investigation",
    "Secondary hyperhidrosis is suggested by generalised sweating including at night and by underlying thyroid "
    "disease, diabetes, or menopause. Thyroid studies and glucose are normal and there is no nocturnal sweating, "
    "which are the two findings that exclude it."],
   ["Frey syndrome, treated with topical glycopyrronium",
    "Frey syndrome is unilateral facial sweating triggered by eating, occurring after parotidectomy or trauma. The "
    "distribution here is bilateral palms, soles, and axillae."],
   ["Anxiety disorder, treated with psychological therapy alone",
    "Anxiety and stress are listed as exacerbating rather than causative. Attributing the condition entirely to "
    "anxiety leaves an effective and simple topical treatment unoffered."]],
  0, 74),

Q("Stevens-Johnson syndrome",
  "A 58-year-old man taking allopurinol for three weeks develops fever, malaise, and painful swallowing, followed by "
  "erosions of the lips, mouth, and conjunctivae, and dusky skin lesions with detachment involving about 6 percent of "
  "his body surface area. What is the single most important immediate action?",
  [["Immediate withdrawal of all suspect medications",
    "Correct. Immediate causative drug withdrawal is the first step, and earlier withdrawal is strongly associated "
    "with improved survival — each day of delay worsens prognosis. Allopurinol is named as the most common trigger "
    "worldwide."],
   ["Admission to a burn unit or intensive care unit",
    "Supportive and burn-unit care is essential and follows immediately, which makes this the strongest competing "
    "answer. But it does not stop the ongoing injury, and the drug will continue to drive the reaction wherever the "
    "patient is admitted."],
   ["Administration of systemic corticosteroids",
    "Immunomodulation is debated and secondary in this setting. It does not substitute for removing the causative "
    "agent, which is the intervention with the clearest survival association."],
   ["Obtaining a skin biopsy to confirm full-thickness epidermal necrosis",
    "Biopsy supports the diagnosis but delays nothing that matters more than stopping the drug. Waiting for "
    "histology before withdrawing the culprit costs exactly the time that worsens prognosis."],
   ["Starting empiric broad-spectrum antibiotics",
    "Antibiotics are given for documented infection rather than prophylactically, and adding further drugs to a "
    "patient with a severe drug reaction risks compounding the problem."]],
  0, 83),

Q("Toxic epidermal necrolysis",
  "A patient is admitted with widespread painful erythema progressing to flaccid bullae and confluent epidermal "
  "detachment of about 40 percent of the body surface area, with a positive Nikolsky sign and severe mucosal "
  "erosions. What distinguishes this from Stevens-Johnson syndrome?",
  [["The extent of epidermal detachment, which exceeds 30 percent of the body surface area",
    "Correct. The two conditions sit on one spectrum and are separated by the percentage of body surface area "
    "involved: Stevens-Johnson syndrome has less than 10 percent detachment, and toxic epidermal necrolysis has more "
    "than 30 percent, with mortality up to 30 to 35 percent."],
   ["The presence of mucosal involvement, which does not occur in Stevens-Johnson syndrome",
    "Mucosal erosions occur in both conditions — they are among the defining features of Stevens-Johnson syndrome "
    "itself. Using mucosal involvement to separate them would misclassify most patients."],
   ["The presence of a drug trigger, since Stevens-Johnson syndrome is only infectious",
    "Both are most commonly drug triggered, and toxic epidermal necrolysis is drug-induced in more than 80 percent of "
    "cases. Stevens-Johnson syndrome shares the same causative agents."],
   ["The presence of a prodrome, which occurs only in toxic epidermal necrolysis",
    "A prodrome of fever and malaise occurs in both. In toxic epidermal necrolysis it includes high fever, stinging "
    "eyes, and painful swallowing 1 to 3 days before the skin findings, but its presence does not separate the two."],
   ["A positive Nikolsky sign, which is negative in Stevens-Johnson syndrome",
    "Nikolsky sign is a feature of epidermal detachment and appears across the spectrum. It is also used to "
    "distinguish these conditions from erythema multiforme rather than from one another."]],
  0, 88),

Q("Toxic epidermal necrolysis",
  "A patient with toxic epidermal necrolysis is admitted. What scoring system should be calculated within 24 hours "
  "and repeated on day three?",
  [["SCORTEN, the severity of illness score for toxic epidermal necrolysis",
    "Correct. SCORTEN should be calculated within 24 hours of admission and repeated on day 3. Each variable scores "
    "one point, including age over 40 years, presence of malignancy, heart rate over 120 beats per minute, and the "
    "initial extent of epidermal detachment."],
   ["The Parkland formula",
    "The Parkland formula estimates fluid resuscitation volumes and may be adapted for the fluid losses of toxic "
    "epidermal necrolysis. It guides therapy rather than scoring severity or prognosis."],
   ["The Fitzpatrick scale",
    "The Fitzpatrick scale classifies baseline ultraviolet sensitivity by skin type and guides photoprotection "
    "counselling. It has no role in grading a drug reaction."],
   ["The minimal erythema dose",
    "The minimal erythema dose is determined during phototesting for drug-induced photosensitivity and polymorphous "
    "light eruption. It is a photobiology measurement rather than a severity score."],
   ["The ankle-brachial index",
    "The ankle-brachial index assesses arterial adequacy before compression therapy and in the workup of vascular "
    "ulcers. It has no bearing on a mucocutaneous emergency."]],
  0, 89),

Q("Sunburn",
  "A 24-year-old man presents six hours after a day at the beach with painful erythema, warmth, and tenderness across "
  "the shoulders and back. There is no blistering. What is the most appropriate acute management?",
  [["Cool compresses, early non-steroidal anti-inflammatory drugs, oral hydration, and topical moisturisers",
    "Correct. Acute management is cool compresses and cool rather than cold water immersion, non-steroidal "
    "anti-inflammatory drugs started early to reduce prostaglandin-mediated inflammation and pain, oral hydration, "
    "and topical moisturisers. First-degree sunburn resolves in 3 to 5 days with desquamation."],
   ["Cold water immersion and delayed non-steroidal anti-inflammatory drugs once blistering appears",
    "Both halves are wrong in instructive ways: cool rather than cold water is specified, and the benefit of "
    "non-steroidal anti-inflammatory drugs depends on starting them early, before the prostaglandin cascade is "
    "established."],
   ["Immediate systemic corticosteroids",
    "Systemic corticosteroids are not part of the described management of uncomplicated sunburn. First-degree injury "
    "confined to the epidermis resolves with supportive care."],
   ["Topical anaesthetic preparations applied liberally to the whole area",
    "Topical anaesthetics on large areas of damaged skin carry sensitisation and absorption concerns and are not "
    "among the recommended measures."],
   ["Prophylactic oral antibiotics to prevent secondary infection",
    "Risk of secondary infection is associated with second-degree burns where blistering has occurred, and this "
    "patient has none. Prophylactic antibiotics are not recommended."]],
  0, 96),

Q("Photosensitivity",
  "A patient develops an exaggerated sunburn-like reaction on sun-exposed skin within hours of starting a new "
  "medication. The reaction is dose-dependent and occurred on the first exposure. What mechanism is responsible, and "
  "what test is the gold standard for the alternative mechanism?",
  [["Phototoxicity, which is non-immunologic and dose-dependent; photopatch testing is the gold standard for "
    "photoallergy",
    "Correct. Phototoxicity is non-immunologic and dose-dependent — the drug absorbs ultraviolet energy, generating "
    "reactive oxygen species and direct cellular damage that resembles an exaggerated sunburn. Photopatch testing is "
    "the gold standard for photoallergy, the other mechanism."],
   ["Photoallergy, which is immunologic and requires prior sensitisation; photopatch testing is the gold standard "
    "for phototoxicity",
    "The two mechanisms are swapped. A reaction on first exposure that is dose-dependent cannot be an immunologic "
    "photoallergy, which requires prior sensitisation, and photopatch testing is aimed at photoallergy rather than "
    "phototoxicity."],
   ["Phototoxicity, which is immunologic and dose-independent; minimal erythema dose testing is the gold standard "
    "for photoallergy",
    "The name is right but the mechanism description inverts it. Phototoxicity is specifically non-immunologic and "
    "dose-dependent, and minimal erythema dose testing measures ultraviolet sensitivity rather than confirming "
    "photoallergy."],
   ["Polymorphous light eruption, which appears 30 minutes to hours after exposure; antinuclear antibody testing is "
    "the gold standard",
    "Polymorphous light eruption is idiopathic rather than drug-induced, and antinuclear antibody testing is "
    "performed to exclude lupus rather than to confirm the eruption. The temporal link to a new medication points to "
    "a drug reaction."],
   ["Phytophotodermatitis from furanocoumarin contact; a thorough drug history is the gold standard",
    "Phytophotodermatitis follows contact with furanocoumarins in plants such as limes, celery, and parsley. It "
    "requires a chemical contactant rather than a systemic drug."]],
  0, 98),

Q("Polymorphous light eruption",
  "A 28-year-old woman develops an itchy eruption of 2 to 5 mm erythematous papules on the décolletage and forearms a "
  "few hours after her first sunny weekend of the spring. The face, which is exposed year-round, is unaffected. What "
  "additional test is considered mandatory?",
  [["An antinuclear antibody panel to exclude lupus",
    "Correct. An antinuclear antibody panel is mandatory to exclude lupus, particularly anti-Ro and anti-La "
    "antibodies. Polymorphous light eruption is otherwise largely a clinical diagnosis based on history and "
    "morphology."],
   ["Photopatch testing to identify a photoallergen",
    "Photopatch testing is the gold standard for photoallergy, which is a drug-induced mechanism. No drug exposure is "
    "described here, and the eruption follows the seasonal pattern characteristic of an idiopathic photodermatosis."],
   ["A potassium hydroxide preparation of the affected skin",
    "A potassium hydroxide preparation detects fungal elements. This eruption is provoked by ultraviolet exposure "
    "rather than by an organism."],
   ["Skin biopsy in every patient before treatment",
    "Diagnosis is largely clinical from history and morphology, with phototesting reproducing the eruption in only "
    "about 50 to 60 percent of cases. Routine biopsy is not required."],
   ["Serum tryptase to exclude mastocytosis",
    "Mastocytosis is on the urticaria differential and is identified by Darier sign. It is not part of the "
    "photodermatosis workup."]],
  0, 106),

Q("Actinic keratosis",
  "A 71-year-old man with a lifetime of outdoor work has multiple rough, scaly erythematous papules on the scalp and "
  "dorsal hands, each 2 to 8 mm, that feel like sandpaper when palpated. What molecular event is the critical step in "
  "their development?",
  [["Ultraviolet-induced mutation in the TP53 tumour suppressor gene",
    "Correct. Actinic keratoses are intraepidermal keratinocytic dysplasias induced by cumulative ultraviolet B "
    "exposure, and ultraviolet-induced mutations in TP53 are the critical molecular event. They represent a field "
    "cancerisation process."],
   ["Ultraviolet-induced proliferation of melanocytes within the epidermis",
    "Localised melanocyte proliferation within the epidermis produces solar lentigines, which are benign pigmented "
    "macules rather than keratinocytic dysplasias. Both follow chronic ultraviolet exposure, which is why this is the "
    "closest wrong answer."],
   ["Hyperinsulinaemia stimulating keratinocyte and fibroblast proliferation",
    "That mechanism produces insulin-resistant acanthosis nigricans through insulin-like growth factor 1 receptor "
    "cross-activation. It is unrelated to ultraviolet damage."],
   ["Immunoglobulin A immune complex deposition in the dermal papillae",
    "Immunoglobulin A deposition in the dermal papillae is the mechanism of dermatitis herpetiformis, a "
    "gluten-driven blistering disease."],
   ["Loss of elastic tissue from a congenital or acquired defect",
    "Loss of elastic tissue describes cutis laxa, which appears on the dermatoheliosis differential. It produces skin "
    "laxity rather than scaly keratotic papules."]],
  0, 112),

Q("Solar lentigo",
  "A 62-year-old woman has several uniformly tan-brown macules on the dorsal hands and face that have appeared "
  "gradually over years. One lesion is larger, asymmetric, and has irregular borders with darker areas within it. "
  "What should be done about that lesion?",
  [["Evaluate it with dermoscopy for lentigo maligna",
    "Correct. Lentigo maligna, which is melanoma in situ, is asymmetric with irregular border and colour and darker "
    "areas, and dermoscopy is described as essential. A solar lentigo that has diverged from its uniform neighbours "
    "requires that evaluation."],
   ["Reassure her that it is a solar lentigo like the others",
    "Solar lentigines are uniformly pigmented, so the asymmetry, irregular border, and internal colour variation are "
    "precisely the features that separate this lesion from the others. Reassurance here would delay a melanoma in "
    "situ diagnosis."],
   ["Treat it as a seborrheic keratosis and leave it alone",
    "Seborrheic keratoses have a stuck-on appearance with comedone-like openings on dermoscopy. Neither feature is "
    "described, and attributing an asymmetric irregular lesion to a benign growth without examination is the error "
    "the differential is designed to prevent."],
   ["Treat it as a café-au-lait macule and observe",
    "Café-au-lait macules are uniform tan patches, usually present from early life. A newly irregular lesion in an "
    "older adult with chronic sun exposure does not fit."],
   ["Apply a topical retinoid and review in six months",
    "Topical retinoids improve dyspigmentation in photoaging, but applying one to an atypical pigmented lesion "
    "delays diagnosis while the appearance is altered."]],
  0, 111),

Q("Dermatoheliosis",
  "A 66-year-old farmer has coarse deep wrinkles, leathery texture with deep rhomboidal furrowing of the posterior "
  "neck, mottled dyspigmentation, and several actinic keratoses. His sun-protected skin looks markedly younger. What "
  "distinguishes this from intrinsic chronological aging?",
  [["Intrinsic aging produces fine lines and dryness without hyperpigmentation or actinic keratoses, and affects "
    "sun-protected skin equally",
    "Correct. Intrinsic chronological aging produces fine lines, dry skin, and decreased elasticity without "
    "hyperpigmentation or actinic keratoses, and it affects sun-protected skin equally. The disparity between exposed "
    "and protected skin is what identifies photoaging."],
   ["Intrinsic aging produces coarse deep wrinkles while photoaging produces fine lines",
    "The wrinkle patterns are reversed. Coarse deep wrinkles are primarily ultraviolet A driven and belong to "
    "photoaging, whereas fine lines characterise intrinsic aging."],
   ["Intrinsic aging spares the posterior neck while photoaging spares the face",
    "Photoaging affects the most exposed surfaces including the face, neck, and forearms, and the deep rhomboidal "
    "furrowing of the posterior neck is a classic marker of severe photoaging rather than something it spares."],
   ["Intrinsic aging is driven by ultraviolet A penetration into the dermis",
    "Ultraviolet A penetration deep into the dermis generating reactive oxygen species is the mechanism of "
    "photoaging. Attributing it to intrinsic aging removes the distinction entirely."],
   ["Only intrinsic aging responds to topical tretinoin",
    "Tretinoin is the only agent approved for photoaging, where it stimulates collagen synthesis and reduces fine "
    "lines and dyspigmentation. Its indication is the photoaged skin rather than the intrinsically aged."]],
  0, 118),

Q("Photoprotection",
  "A patient asks how to use sunscreen correctly. What advice matches the guidance given?",
  [["Use a broad-spectrum product with sun protection factor of at least 30 daily, applying it 15 minutes before "
    "exposure and reapplying every 2 hours",
    "Correct. Broad-spectrum sun protection factor 30 or above is advised for daily use and 50 or above for "
    "prolonged outdoor exposure, applied 15 minutes before sun exposure and reapplied every 2 hours."],
   ["Use a broad-spectrum product with sun protection factor of at least 30 daily, applying it once at the start of "
    "the day",
    "The product choice is right but a single morning application is the commonest real-world failure. Reapplication "
    "every 2 hours is what maintains the protection the number implies."],
   ["Use a product with sun protection factor 15 and reapply only after swimming",
    "Sun protection factor 15 falls below the recommended minimum of 30 for daily use, and restricting reapplication "
    "to after swimming leaves long dry exposures unprotected."],
   ["Rely on physical barriers alone, since sunscreen provides no measurable benefit",
    "Physical barriers are recommended alongside sunscreen rather than instead of it. Discarding sunscreen removes "
    "one of the two components of photoprotection."],
   ["Apply sunscreen only to patients with Fitzpatrick skin types I to III",
    "All Fitzpatrick types are susceptible to cumulative ultraviolet damage, photoaging, and skin cancer, though "
    "absolute risk varies. Restricting advice to fair skin types leaves darker-skinned patients uncounselled."]],
  0, 123),
]

QUESTIONS += [

Q("Erythema multiforme",
  "A 30-year-old woman with erythema multiforme triggered by recurrent herpes simplex virus has had four episodes in "
  "twelve months. What management addresses the recurrences?",
  [["Suppressive oral acyclovir or valacyclovir",
    "Correct. Oral acyclovir or valacyclovir is used when the eruption is triggered by herpes simplex virus, and a "
    "prior episode is itself a risk factor for recurrence. Suppressing the trigger is what prevents the next "
    "episode."],
   ["Oral antihistamines taken continuously between episodes",
    "Oral antihistamines are used for pruritus during an acute episode. They relieve a symptom without touching the "
    "viral trigger, so the eruptions would continue at the same rate."],
   ["Topical corticosteroids applied continuously to previously affected sites",
    "Topical corticosteroids are used for localised lesions during an episode. Applying them prophylactically to "
    "clear skin exposes her to atrophy without preventing anything."],
   ["A short course of oral prednisone at the first sign of each episode",
    "Systemic corticosteroids are not the described approach, and treating each episode as it starts does nothing to "
    "reduce how often they occur."],
   ["Avoidance of non-steroidal anti-inflammatory drugs and sulfonamides",
    "Those drugs are genuine triggers in other patients and the history should be reviewed, but this woman's trigger "
    "is already identified as herpes simplex virus. Avoiding an unrelated exposure would not help."]],
  0, 12),

Q("Acanthosis nigricans",
  "A 34-year-old woman with obesity, type 2 diabetes, and polycystic ovary syndrome has velvety hyperpigmented "
  "plaques of the neck and axillae. What is the primary management?",
  [["Treat the underlying cause with weight loss and glycaemic control",
    "Correct. Primary management is treating the underlying cause through weight loss and glycaemic control, "
    "discontinuing any offending drug. Metformin reduces insulin resistance and may improve the skin findings."],
   ["Topical retinoids as the primary treatment",
    "Topical retinoids, salicylic acid, and ammonium lactate are used for cosmetic improvement. They address the "
    "appearance while leaving the insulin resistance that produced it untreated, which is why they are secondary."],
   ["Laser therapy or dermabrasion as the primary treatment",
    "Dermabrasion and laser are cosmetic measures listed alongside the topicals. Choosing a procedure over metabolic "
    "management treats the marker rather than the disease it marks."],
   ["Topical corticosteroids twice daily",
    "Acanthosis nigricans is a proliferative response to hyperinsulinaemia rather than an inflammatory dermatosis, so "
    "there is no inflammation for a corticosteroid to suppress."],
   ["Reassurance with no intervention, since the condition is purely cosmetic",
    "The lesion is a visible cutaneous marker of insulin resistance and underlying systemic disease. Treating it as "
    "purely cosmetic discards the diagnostic signal it carries."]],
  0, 25),

Q("Urticaria",
  "A 27-year-old man develops widespread wheals within 20 minutes of eating shellfish. What mechanism underlies this "
  "reaction, and what class of trigger does it represent?",
  [["Immunoglobulin E mediated mast cell degranulation, an immunologic trigger",
    "Correct. Urticaria results from mast cell degranulation releasing histamine, prostaglandins, and leukotrienes, "
    "producing transient dermal oedema. Immunologic immunoglobulin E mediated triggers include foods such as "
    "shellfish, nuts, and eggs, drugs including penicillin, and insect stings."],
   ["Immunoglobulin E mediated mast cell degranulation, a non-immunologic trigger",
    "The mechanism is right but the classification contradicts it — an immunoglobulin E mediated reaction is by "
    "definition immunologic. Non-immunologic triggers act on mast cells directly without antibody involvement."],
   ["A delayed type IV hypersensitivity reaction to a food antigen",
    "A delayed cell-mediated reaction takes days rather than 20 minutes and produces dermatitis rather than "
    "transient wheals. That mechanism belongs to allergic contact dermatitis."],
   ["Immune complex deposition in dermal vessels",
    "Immune complex deposition with vessel damage describes urticarial vasculitis, whose lesions persist beyond 24 "
    "hours and leave bruising. This reaction is immediate and transient."],
   ["Complement deficiency causing bradykinin-mediated swelling",
    "C1-esterase inhibitor deficiency produces hereditary angioedema, which is considered when angioedema occurs "
    "without wheals. This patient has wheals."]],
  0, 36),

Q("Erythema nodosum",
  "A patient with tender pretibial nodules undergoes a deep incisional biopsy. What finding confirms the diagnosis?",
  [["Septal panniculitis without vasculitis, with Miescher's granulomas",
    "Correct. Biopsy shows septal panniculitis without vasculitis and Miescher's granulomas. A deep incisional "
    "biopsy is needed because the pathology lies in the subcutaneous fat."],
   ["Lobular panniculitis with vasculitis",
    "The pattern is inverted on both counts. Erythema nodosum is specifically a septal panniculitis and specifically "
    "without vasculitis, which is how it is distinguished from other panniculitides."],
   ["Palisading granulomas with central necrobiosis and mucin",
    "Palisading granulomas around degenerating collagen with mucin deposition is the granuloma annulare finding. That "
    "condition produces annular surface plaques rather than deep tender nodules."],
   ["A dense dermal neutrophilic infiltrate with no organisms",
    "A sterile neutrophilic dermatosis suggests pyoderma gangrenosum, which ulcerates. Erythema nodosum nodules "
    "characteristically do not ulcerate."],
   ["Full-thickness epidermal necrosis",
    "Full-thickness epidermal necrosis is the biopsy finding of Stevens-Johnson syndrome and toxic epidermal "
    "necrolysis. It is an epidermal process rather than a disease of the subcutaneous fat."]],
  0, 44),

Q("Granuloma annulare",
  "A patient has a single annular ring of flesh-coloured papules on the dorsum of the foot. It is asymptomatic. What "
  "proportion of cases does this variant represent, and what is the expected course?",
  [["About 75 percent of cases, and the condition is benign and self-limiting",
    "Correct. The localised variant accounts for about 75 percent of cases, presenting as flesh-coloured to "
    "erythematous papules in an annular ring on the dorsal hands, feet, and ankles, and is asymptomatic. Granuloma "
    "annulare is a benign, self-limiting granulomatous dermatosis."],
   ["About 75 percent of cases, and the condition progresses to malignancy without treatment",
    "The proportion is right, which makes this the closest wrong answer, but granuloma annulare is benign and "
    "self-limiting. An oncology referral is considered only if lymphoma is separately suspected."],
   ["About 25 percent of cases, and the condition is benign and self-limiting",
    "The course is right but the proportion is reversed — localised disease is the common form at about 75 percent, "
    "and the generalised or disseminated variant is the minority."],
   ["About 75 percent of cases, and lifelong systemic immunosuppression is required",
    "Systemic therapy and phototherapy are reserved for generalised or treatment-resistant disease through a "
    "dermatology referral. Committing localised asymptomatic disease to systemic immunosuppression is far beyond what "
    "it needs."],
   ["About 50 percent of cases, and the condition invariably recurs after clearing",
    "Neither figure nor course matches. The condition is described as self-limiting rather than invariably "
    "recurrent."]],
  0, 50),

Q("Pyoderma gangrenosum",
  "What systemic conditions are most closely associated with pyoderma gangrenosum?",
  [["Inflammatory bowel disease, inflammatory arthritis, and haematologic disorders",
    "Correct. Pyoderma gangrenosum is a neutrophilic dermatosis with dysregulated innate immune activation, and "
    "inflammatory bowel disease heads the list of key associated conditions alongside inflammatory arthritis and "
    "haematologic disease."],
   ["Celiac disease and autoimmune thyroid disease",
    "Celiac disease and autoimmune thyroid disease are the high-priority associations of dermatitis herpetiformis, "
    "for which all patients should be screened for celiac disease."],
   ["Type 2 diabetes, polycystic ovary syndrome, and gastrointestinal malignancy",
    "That set belongs to acanthosis nigricans, where the skin change is a marker of insulin resistance and, in the "
    "malignant form, of gastrointestinal adenocarcinoma."],
   ["Chronic venous insufficiency and peripheral arterial disease",
    "Vascular insufficiency causes ulcers that must be excluded before pyoderma gangrenosum is diagnosed, using "
    "ankle-brachial index testing. They are differential diagnoses rather than associations."],
   ["Sarcoidosis and streptococcal infection",
    "Sarcoidosis, in the form of Löfgren syndrome, and group A streptococcal infection are the associations of "
    "erythema nodosum."]],
  0, 57),

Q("Acne rosacea",
  "A patient newly diagnosed with rosacea asks which trigger is most important to control. What is the most accurate "
  "answer?",
  [["Sun exposure, described as the most universal trigger",
    "Correct. Sun exposure is named as the most universal trigger of rosacea, alongside heat, alcohol, spicy foods, "
    "and stress. Chronic ultraviolet exposure is also a listed risk factor."],
   ["Alcohol, described as the most universal trigger",
    "Alcohol is a genuine and commonly reported trigger, which makes this the closest wrong answer, but sun exposure "
    "is the one identified as most universal. Focusing counselling on alcohol alone would leave the dominant exposure "
    "unaddressed."],
   ["Dairy products, which drive Demodex overgrowth",
    "Demodex folliculorum overgrowth contributes to the pathogenesis, but dairy is not a listed trigger and does not "
    "drive the mite burden."],
   ["Topical corticosteroid use, which is the primary cause",
    "Topical corticosteroid exposure is the most important modifiable association of perioral dermatitis rather than "
    "of rosacea, and steroids can worsen rosacea rather than cause it."],
   ["Cold weather, which is the dominant environmental trigger",
    "Heat rather than cold appears among the common triggers. Advising avoidance of cold would misdirect the "
    "patient's efforts."]],
  0, 67),

Q("Acne rosacea",
  "A patient with known rosacea reports a gritty foreign-body sensation, blurred vision, and photophobia. What is the "
  "most appropriate action?",
  [["Urgent ophthalmology referral",
    "Correct. Ocular rosacea with keratitis, visual symptoms, or corneal involvement warrants urgent ophthalmology "
    "referral. Visual symptoms and photophobia raise exactly those concerns."],
   ["Routine ophthalmology referral within three months",
    "The referral destination is right but the urgency is wrong, and the delay is the harm. Corneal involvement can "
    "threaten sight, which is why the referral is specified as urgent."],
   ["Begin topical metronidazole and reassess in six weeks",
    "Topical metronidazole is first-line for papulopustular skin disease. It does not treat ocular involvement, and "
    "six weeks of observation with visual symptoms risks permanent corneal damage."],
   ["Begin oral isotretinoin",
    "Isotretinoin initiation is a dermatology referral matter for refractory disease, and it carries its own ocular "
    "adverse effects including dryness. It is not the response to acute visual symptoms."],
   ["Reassure the patient that ocular symptoms are unrelated to rosacea",
    "Ocular rosacea is a recognised subtype with potential corneal complications. Dismissing the connection is the "
    "error most likely to result in vision loss."]],
  0, 70),

Q("Stevens-Johnson syndrome",
  "A patient presents with widespread superficial skin peeling and a positive Nikolsky sign but entirely normal "
  "mucous membranes. What diagnosis does the preserved mucosa most suggest?",
  [["Staphylococcal scalded skin syndrome",
    "Correct. Staphylococcal scalded skin syndrome spares the mucosa and is toxin-mediated, which is exactly how it "
    "is separated from Stevens-Johnson syndrome on the differential."],
   ["Stevens-Johnson syndrome",
    "Mucosal erosions are a defining feature of Stevens-Johnson syndrome — the presentation includes erosions of the "
    "lips, mouth, and conjunctivae. Entirely normal mucosa argues against it."],
   ["Toxic epidermal necrolysis",
    "Toxic epidermal necrolysis produces severe mucosal erosions alongside detachment of more than 30 percent of the "
    "body surface area. Preserved mucosa does not fit."],
   ["Erythema multiforme major",
    "Erythema multiforme major has target lesions, is usually associated with herpes simplex virus, and has less "
    "mucosal involvement than Stevens-Johnson syndrome — but it still involves mucosa and produces fixed targets "
    "rather than diffuse peeling."],
   ["Drug reaction with eosinophilia and systemic symptoms",
    "That syndrome presents with rash, fever, eosinophilia, and internal organ involvement rather than superficial "
    "epidermal peeling with a positive Nikolsky sign."]],
  0, 82),

Q("Stevens-Johnson syndrome",
  "Which human leukocyte antigen association should prompt caution before prescribing carbamazepine?",
  [["Human leukocyte antigen B*15:02",
    "Correct. Human leukocyte antigen B*15:02 is the risk allele associated with carbamazepine, while human "
    "leukocyte antigen B*58:01 is associated with allopurinol. Both are listed risk factors for Stevens-Johnson "
    "syndrome."],
   ["Human leukocyte antigen B*58:01",
    "That allele is the allopurinol association. The two are frequently confused because both appear together as "
    "risk factors, but pairing them with the wrong drug would misdirect the screening entirely."],
   ["Human leukocyte antigen B27",
    "Human leukocyte antigen B27 is frequently associated with psoriatic arthritis and the spondyloarthropathies. It "
    "has no role in predicting severe cutaneous drug reactions."],
   ["Human leukocyte antigen Cw6",
    "Human leukocyte antigen Cw6 is seen in 90 percent of early-onset psoriasis and 50 percent of late-onset cases. "
    "It is a psoriasis susceptibility marker."],
   ["Human leukocyte antigen DQ2",
    "Human leukocyte antigen DQ2, with DQ8, confers susceptibility to dermatitis herpetiformis and celiac disease."]],
  0, 80),

Q("Toxic epidermal necrolysis",
  "What is the mandatory disposition for a patient with confirmed toxic epidermal necrolysis?",
  [["Admission to a burn unit or intensive care unit",
    "Correct. Burn unit or intensive care admission is mandatory for all cases of toxic epidermal necrolysis, "
    "together with immediate discontinuation of all suspect drugs, fluid resuscitation estimated as for major burns, "
    "and non-adhesive biological dressings."],
   ["Admission to a general medical ward with dermatology consultation",
    "A general ward cannot provide the fluid resuscitation, wound care, and temperature and infection control this "
    "condition demands. With mortality up to 30 to 35 percent, the level of care is not discretionary."],
   ["Outpatient management with daily wound review",
    "Outpatient management of a condition with epidermal detachment exceeding 30 percent of the body surface area "
    "and mortality up to 35 percent is not tenable at any level of follow-up."],
   ["Admission to a surgical ward for debridement of detached epidermis",
    "Wound care uses non-adhesive biological dressings such as biobrane or porcine xenograft. Aggressive surgical "
    "debridement is not the described approach."],
   ["Observation in the emergency department until the eruption stabilises",
    "The eruption progresses over days, so waiting for stabilisation in an emergency department delays the "
    "resuscitative and wound care that determine survival."]],
  0, 90),

Q("Sunburn",
  "A patient has painful erythema and warmth of the shoulders with no blistering, confined to the epidermis. How is "
  "this classified, and what course should be expected?",
  [["First degree, resolving in 3 to 5 days with desquamation",
    "Correct. First-degree sunburn produces erythema, warmth, and tenderness confined to the epidermis without "
    "blistering, and resolves in 3 to 5 days with desquamation."],
   ["First degree, resolving in 1 to 2 weeks with risk of secondary infection",
    "The classification is right but the course belongs to second-degree injury, which involves blistering, intense "
    "pain, and partial dermal involvement, takes 1 to 2 weeks, and carries an infection risk."],
   ["Second degree, resolving in 3 to 5 days with desquamation",
    "Second-degree injury requires blistering and partial dermal involvement, both absent here. The timeline given "
    "belongs to first-degree burn."],
   ["Second degree, requiring prophylactic antibiotics",
    "This misclassifies the depth and adds an intervention that is not recommended even for genuine second-degree "
    "sunburn."],
   ["Third degree, requiring surgical referral",
    "Third-degree injury implies full-thickness damage, which is not a feature of ordinary sunburn confined to the "
    "epidermis."]],
  0, 95),

Q("Photodermatitis",
  "A 22-year-old bartender develops streaky, bizarrely shaped erythema and blistering on the forearms two days after "
  "an outdoor shift squeezing limes. The affected areas later become hyperpigmented. What is the most likely "
  "diagnosis?",
  [["Phytophotodermatitis",
    "Correct. Phytophotodermatitis follows contact with furanocoumarins, also called psoralens, found in limes, "
    "celery, parsley, and related plants, followed by ultraviolet exposure. The streaky shapes trace where the juice "
    "ran, and postinflammatory hyperpigmentation follows."],
   ["Ordinary sunburn",
    "Sunburn occurs without a chemical contactant history and follows the pattern of exposure rather than the drip "
    "marks of a liquid. The differential lists it precisely on the grounds of that missing contactant."],
   ["Allergic contact dermatitis to citrus",
    "Allergic contact dermatitis is a delayed hypersensitivity requiring prior sensitisation, and it does not need "
    "ultraviolet light to appear. The interaction of the chemical with light is what defines this reaction."],
   ["Polymorphous light eruption",
    "Polymorphous light eruption produces 2 to 5 mm papules on the décolletage and forearms within 30 minutes to "
    "hours of the first sunny days of spring. It is idiopathic and does not follow a chemical contactant in streaks."],
   ["Drug-induced phototoxicity",
    "Drug-induced phototoxicity resembles an exaggerated sunburn across sun-exposed skin in a patient taking a "
    "systemic drug. No medication is reported, and the streaky distribution reflects topical contact."]],
  0, 100),

Q("Actinic keratosis",
  "A patient has multiple actinic keratoses scattered across a bald scalp. The clinician explains that treating "
  "individual visible lesions may be insufficient. What concept does this reflect?",
  [["Field cancerisation, in which the surrounding sun-damaged skin also carries mutations",
    "Correct. Actinic keratoses represent a field cancerisation process, meaning the ultraviolet-induced mutations "
    "extend through the surrounding skin rather than being confined to the visible lesions."],
   ["Pathergy, in which trauma to the skin provokes new lesions",
    "Pathergy is the worsening of pyoderma gangrenosum with trauma or debridement. It has no bearing on "
    "ultraviolet-induced keratinocytic dysplasia."],
   ["Koebner phenomenon, in which lesions arise at sites of trauma",
    "Koebner phenomenon occurs in psoriasis and lichen planus, where new lesions develop where the skin has been "
    "injured. It is not what makes actinic keratoses multifocal."],
   ["Photoallergy, in which sensitisation spreads to unexposed skin",
    "Photoallergy is an immunologic drug-induced mechanism confirmed by photopatch testing. It is unrelated to the "
    "distribution of premalignant keratinocytic lesions."],
   ["Paraneoplastic change, in which an internal malignancy drives the skin findings",
    "Paraneoplastic cutaneous change describes malignant acanthosis nigricans. Actinic keratoses arise from direct "
    "cumulative ultraviolet damage to the skin itself."]],
  0, 112),

Q("Dermatoheliosis",
  "A 55-year-old woman asks about treatment for photoaging. What topical agent is approved for this indication, and "
  "what should she be told to expect?",
  [["Tretinoin, with initial retinoid dermatitis expected and a minimum of 6 to 12 months of use",
    "Correct. Tretinoin 0.025 to 0.1 percent is the only approved topical agent for photoaging. It stimulates "
    "collagen synthesis, inhibits matrix metalloproteinase activity, and reduces fine lines and dyspigmentation; "
    "therapy is started low and titrated, with initial retinoid dermatitis expected."],
   ["Tretinoin, with results expected within two weeks and no initial irritation",
    "The agent is right but the expectations are wrong in both directions. Promising rapid results without warning "
    "about retinoid dermatitis is the counselling failure that makes patients stop before the minimum 6 to 12 months "
    "of use required."],
   ["Hydroquinone, which reverses the structural changes of photoaging",
    "Pigment-directed agents address dyspigmentation but do not reverse the dermal structural damage. Tretinoin is "
    "the agent named for the photoaging indication."],
   ["Topical corticosteroids applied nightly",
    "Prolonged topical corticosteroid use causes atrophy, striae, and telangiectasia, which would compound rather "
    "than treat photoaged skin."],
   ["Calcipotriene, a vitamin D analogue",
    "Calcipotriene is a first-line topical for plaque psoriasis with a caution regarding nephrotoxicity. It has no "
    "role in photoaging."]],
  0, 119),

Q("Photoprotection",
  "What does the Fitzpatrick skin type classification predict, and how should it guide counselling?",
  [["It predicts baseline ultraviolet sensitivity and guides photoprotection counselling, though all types remain "
    "susceptible to cumulative damage",
    "Correct. Fitzpatrick skin type predicts baseline ultraviolet sensitivity and guides photoprotection "
    "counselling. All types are susceptible to cumulative ultraviolet damage, photoaging, and skin cancer, though "
    "absolute risk varies."],
   ["It predicts baseline ultraviolet sensitivity, and types V and VI require no photoprotection counselling",
    "The first half is right, which is what makes this the closest wrong answer, but exempting darker skin types "
    "from counselling contradicts the statement that all types are susceptible. This is the assumption that leads to "
    "later diagnosis of skin cancer in darker-skinned patients."],
   ["It predicts the likelihood of developing rosacea and guides trigger avoidance",
    "Fitzpatrick types I to III are a risk factor for rosacea, so the scale is referenced there, but predicting "
    "rosacea is not what the classification is for."],
   ["It grades the severity of a sunburn once it has occurred",
    "Sunburn severity is graded by degree — first degree confined to the epidermis, second degree with blistering "
    "and partial dermal involvement. Fitzpatrick type describes baseline sensitivity before any exposure."],
   ["It determines the required sun protection factor, with no other measures needed",
    "Broad-spectrum sun protection factor 30 or above is advised for daily use across the board, and physical "
    "barriers are recommended alongside sunscreen rather than instead of it."]],
  0, 122),
]
