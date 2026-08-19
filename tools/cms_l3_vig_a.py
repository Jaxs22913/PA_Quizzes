# CMS I Lecture 3 (Dermatology II) — SET 2, vignette pool A.
# Erythema multiforme, dermatitis herpetiformis, acanthosis nigricans,
# epidermolysis bullosa, urticaria.
#
# Options drafted at MATCHED LENGTHS from the outset — the practice that took
# the Lecture 3 objective pool from a projected 66% length-gameable to 24%.
#
# Lead-ins are varied deliberately and tracked across the three pools: diagnosis,
# next step, first-line treatment, initial test, confirmatory test and patient
# education all appear. Distractors are right-disease-wrong-phase, or a genuine
# lookalike from this same lecture.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "3. Dermatology  II.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Objective a — Etiologies, manifestations, diagnosis and management of dermatological conditions"

POOL_A = [
 dict(topic="Erythema multiforme", io=IOA,
   q="A 28-year-old man has a two-day history of a rash on his hands and forearms. Examination shows symmetric lesions on the palms and dorsal hands, each with a dusky centre, a pale swollen ring and an outer red halo. He had a cold sore ten days ago. There is no mucosal involvement. Which is the most likely diagnosis?",
   opts=[
     ["Erythema multiforme minor",
      "Correct. Three-zone target lesions on acral surfaces after herpes simplex, with skin involvement only."],
     ["Stevens-Johnson syndrome in its early phase",
      "That would involve mucosal erosions in over 90% and epidermal detachment with a positive Nikolsky sign."],
     ["Acute urticaria with an unusual annular pattern",
      "Wheals are migratory, blanch fully and each lasts under twenty-four hours without fixed targets."],
     ["Secondary syphilis involving the palms and soles",
      "This also affects palms and soles but is distinguished by serology and systemic features."]],
   c=0, cite=c(9)),

 dict(topic="Erythema multiforme", io=IOA,
   q="A 31-year-old woman has her fourth episode of target lesions on the hands in eighteen months. Each episode has followed an oral herpes outbreak. Which is the most appropriate long-term management?",
   opts=[
     ["Suppressive acyclovir 400 mg twice daily or valacyclovir 500 mg daily",
      "Correct — recurrent disease is strongly associated with recurrent herpes simplex, and suppression is the answer."],
     ["Dapsone titrated to response with regular blood count monitoring",
      "Right drug, wrong indication: dapsone is for refractory recurrent disease that is not herpes-associated."],
     ["Hydroxychloroquine 200 mg twice daily taken continuously",
      "Also reserved for refractory recurrent disease without a herpes trigger."],
     ["Acyclovir 400 mg five times daily during each acute episode only",
      "Treating episodes does not prevent them; suppression is what reduces recurrence."]],
   c=0, cite=c(12)),

 dict(topic="Erythema multiforme", io=IOA,
   q="A 24-year-old man has target lesions on the palms, and the clinical picture is not clear-cut. A punch biopsy is taken with direct immunofluorescence. Which result would support erythema multiforme?",
   opts=[
     ["Negative direct immunofluorescence with interface dermatitis on histology",
      "Correct — negativity is what distinguishes it from pemphigoid and pemphigus."],
     ["Granular immunoglobulin A within the dermal papillae on immunofluorescence",
      "That pattern is the gold standard for dermatitis herpetiformis."],
     ["Linear immunoglobulin G along the basement membrane zone",
      "That pattern indicates bullous pemphigoid."],
     ["Intercellular immunoglobulin G throughout the epidermal layer",
      "That pattern indicates pemphigus."]],
   c=0, cite=c(11)),

 dict(topic="Erythema multiforme", io=IOA,
   q="A 9-year-old boy develops target lesions and oral erosions two weeks after a persistent cough and fever. Which test should be ordered to identify the trigger?",
   opts=[
     ["Mycoplasma pneumoniae immunoglobulin M serology or polymerase chain reaction",
      "Correct — elevated Mycoplasma immunoglobulin M is characteristic in children and atypical presentations."],
     ["Herpes simplex virus polymerase chain reaction from a skin swab",
      "Herpes triggers most adult cases, but the respiratory prodrome here points elsewhere."],
     ["Antistreptolysin O titre with a throat culture for group A streptococcus",
      "That combination investigates erythema nodosum instead."],
     ["Serum immunoglobulin A anti-tissue transglutaminase antibodies",
      "That serology investigates dermatitis herpetiformis and coeliac disease."]],
   c=0, cite=c(11)),

 dict(topic="Dermatitis herpetiformis", io=IOA,
   q="A 34-year-old man reports months of intensely itchy, burning bumps on his elbows, knees and buttocks. Examination shows grouped papules and excoriations symmetrically distributed, with few intact vesicles. He has no gastrointestinal complaints. Which is the most likely diagnosis?",
   opts=[
     ["Dermatitis herpetiformis",
      "Correct — the symmetric extensor distribution with burning that precedes lesions, and gastrointestinal symptoms may be absent despite villous atrophy."],
     ["Scabies infestation of the trunk and extremities",
      "That would show burrows in the web spaces and a positive skin scraping."],
     ["Atopic dermatitis of adult onset",
      "That favours a flexural distribution with raised immunoglobulin E and no immunoglobulin A deposition."],
     ["Linear immunoglobulin A bullous dermatosis",
      "That shows linear rather than granular immunoglobulin A at the basement membrane."]],
   c=0, cite=c(17)),

 dict(topic="Dermatitis herpetiformis", io=IOA,
   q="A 36-year-old woman with suspected dermatitis herpetiformis is to have a biopsy. Which specimen and test confirm the diagnosis?",
   opts=[
     ["Perilesional skin for direct immunofluorescence, seeking granular immunoglobulin A in the dermal papillae",
      "Correct — this is the gold standard, and perilesional rather than lesional skin is the key detail."],
     ["Lesional skin for haematoxylin and eosin, seeking subepidermal blistering with neutrophils",
      "Histology supports the diagnosis but immunofluorescence is what settles it."],
     ["Small bowel mucosa on endoscopy, seeking villous atrophy of the duodenum",
      "That confirms coeliac disease rather than the skin diagnosis itself."],
     ["Serum sample for immunoglobulin A anti-endomysial antibody testing",
      "Serology supports the diagnosis but is not the gold standard test."]],
   c=0, cite=c(18)),

 dict(topic="Dermatitis herpetiformis", io=IOA,
   q="A 38-year-old man with newly confirmed dermatitis herpetiformis is about to start dapsone. Which is the most appropriate next step?",
   opts=[
     ["Check glucose-6-phosphate dehydrogenase status before the first dose",
      "Correct, then monitor the blood count for haemolytic anaemia and methaemoglobinaemia."],
     ["Check thyroid-stimulating hormone and anti-thyroid peroxidase antibodies",
      "Autoimmune thyroid disease is an association but not the pre-dapsone safety check."],
     ["Arrange small bowel biopsy before any treatment is commenced",
      "Gastroenterology evaluation matters but does not gate starting dapsone."],
     ["Perform HLA-DQ2 and HLA-DQ8 typing to confirm susceptibility",
      "Typing is used when serology is equivocal rather than before dapsone."]],
   c=0, cite=c(19)),

 dict(topic="Dermatitis herpetiformis", io=IOA,
   q="A 40-year-old woman with dermatitis herpetiformis is doing well on dapsone and asks whether she really needs to change her diet. Which is the most appropriate counselling point?",
   opts=[
     ["A strict lifelong gluten-free diet is the cornerstone and may allow dapsone to be reduced or stopped over one to two years",
      "Correct, and hidden gluten in medications, sauces and cross-contamination should be discussed."],
     ["Dapsone controls the disease fully, so dietary change is optional if symptoms are quiet",
      "Dapsone gives rapid symptom relief but does not address the underlying enteropathy."],
     ["The diet is needed only if she develops gastrointestinal symptoms in the future",
      "Nearly all patients have gluten-sensitive enteropathy even when gastrointestinally asymptomatic."],
     ["A reduced-gluten diet is sufficient provided she avoids obvious sources of wheat",
      "The diet must be strict; partial restriction does not achieve control."]],
   c=0, cite=c(19)),

 dict(topic="Acanthosis nigricans", io=IOA,
   q="A 15-year-old with a body mass index in the 97th percentile has velvety, darkened, thickened skin at the back of the neck and in both axillae. Which is the most appropriate initial testing?",
   opts=[
     ["Fasting glucose, haemoglobin A1c, fasting insulin and a lipid panel",
      "Correct — the finding is a visible marker of insulin resistance and warrants metabolic assessment."],
     ["Computed tomography of chest, abdomen and pelvis with upper endoscopy",
      "That workup is reserved for suspected malignant acanthosis nigricans."],
     ["Potassium hydroxide preparation of scrapings from the affected skin",
      "That would investigate tinea versicolor, one of the differentials."],
     ["Skin biopsy of the posterior neck for histological confirmation",
      "Biopsy is rarely needed since the diagnosis is primarily clinical."]],
   c=0, cite=c(24)),

 dict(topic="Acanthosis nigricans", io=IOA,
   q="A 61-year-old man with no obesity develops widespread velvety hyperpigmentation over eight weeks, involving the axillae, the oral mucosa and the palms, which have a thickened rugose appearance. Which is the most appropriate next step?",
   opts=[
     ["Urgent evaluation for an underlying malignancy, particularly of the gastrointestinal tract",
      "Correct — rapid onset, extensive involvement, mucosal change and tripe palms indicate malignant acanthosis nigricans."],
     ["Begin metformin to reduce insulin resistance and reassess in three months",
      "That addresses the benign insulin-resistant form, which this presentation is not."],
     ["Begin topical retinoids for cosmetic improvement of the affected areas",
      "Cosmetic treatment would delay the necessary malignancy workup."],
     ["Reassure and arrange routine follow-up with lifestyle advice in six months",
      "The tempo and distribution here demand urgent evaluation rather than reassurance."]],
   c=0, cite=c(23)),

 dict(topic="Acanthosis nigricans", io=IOA,
   q="A 17-year-old girl with acanthosis nigricans is embarrassed and has been scrubbing her neck daily, believing it is dirt. Which is the most appropriate counselling point?",
   opts=[
     ["The change is a metabolic warning sign rather than a hygiene problem, and 5 to 10% weight loss improves it",
      "Correct — the hygiene misconception is specifically addressed in the teaching."],
     ["The change is caused by friction from clothing and will settle with gentler fabrics",
      "Friction is not the mechanism; hyperinsulinaemia drives keratinocyte proliferation."],
     ["The change is permanent and no intervention will alter its appearance at all",
      "Treating the underlying cause and losing weight both improve the findings."],
     ["The change indicates an underlying cancer in most adolescent patients",
      "Malignant disease accounts for under 1% of cases and is rare at this age."]],
   c=0, cite=c(25)),

 dict(topic="Epidermolysis bullosa", io=IOA,
   q="A neonate develops blisters over the hands and feet after routine handling and nappy changes. There is no fever and the mother is well. Family history includes a father with similar childhood blistering that healed without scars. Which is the most likely diagnosis?",
   opts=[
     ["Epidermolysis bullosa simplex",
      "Correct — localised to palms and soles, healing without scarring, and autosomal dominant."],
     ["Staphylococcal scalded skin syndrome",
      "That is infectious and toxin-mediated, and would present with fever."],
     ["Junctional epidermolysis bullosa of the Herlitz subtype",
      "That is generalised with poor wound healing, nail dystrophy and the highest mortality."],
     ["Bullous pemphigoid of the neonatal period",
      "Bullous pemphigoid is an acquired autoimmune disease of older adults."]],
   c=0, cite=c(30)),

 dict(topic="Epidermolysis bullosa", io=IOA,
   q="An infant has generalised blistering from minimal trauma and the subtype is unclear. Which test determines the level of cleavage?",
   opts=[
     ["Skin biopsy with transmission electron microscopy",
      "Correct — the gold standard, with immunofluorescence antigen mapping localising the missing protein."],
     ["Skin biopsy with direct immunofluorescence for immunoglobulin G",
      "That identifies acquired autoimmune blistering rather than mapping an inherited cleavage plane."],
     ["Serum enzyme-linked immunosorbent assay for structural antibodies",
      "Inherited epidermolysis bullosa is not antibody-mediated."],
     ["Bacterial culture of blister fluid with sensitivity testing",
      "Culture addresses secondary infection rather than the diagnosis."]],
   c=0, cite=c(31)),

 dict(topic="Epidermolysis bullosa", io=IOA,
   q="A 12-year-old with recessive dystrophic epidermolysis bullosa attends for review. Which surveillance should now begin?",
   opts=[
     ["Annual squamous cell carcinoma surveillance, which starts after the age of ten",
      "Correct — the severe scarring of dystrophic disease carries a substantial carcinoma risk."],
     ["Annual colonoscopy to detect gastrointestinal involvement of the disease",
      "Endoscopy is performed if oesophageal stricture is suspected rather than for surveillance."],
     ["Annual echocardiography to monitor for the development of cardiomyopathy",
      "This is not among the described surveillance requirements."],
     ["Annual bone densitometry to monitor for treatment-related osteoporosis",
      "This is not among the described surveillance requirements."]],
   c=0, cite=c(31)),

 dict(topic="Epidermolysis bullosa", io=IOA,
   q="The parents of a child with severe Herlitz junctional epidermolysis bullosa ask what support is available. Which is the most appropriate response?",
   opts=[
     ["Early palliative care integration is appropriate, alongside genetics counselling and family support resources",
      "Correct — goals-of-care discussion, pain optimisation and psychosocial support are all indicated in this subtype."],
     ["Gene therapy will cure the condition once the child is old enough to receive it",
      "The approved topical gene therapy is for dystrophic disease and is not curative."],
     ["The condition improves substantially through childhood with wound care alone",
      "Junctional disease carries the highest mortality of the subtypes."],
     ["Genetic counselling is unnecessary since the condition arises sporadically",
      "Counselling is described as mandatory for all families."]],
   c=0, cite=c(32)),

 dict(topic="Urticaria", io=IOA,
   q="A 26-year-old woman has had itchy raised red patches coming and going for three days. Each individual patch fades within a few hours and blanches under pressure, leaving no mark. Which is the most likely diagnosis?",
   opts=[
     ["Acute urticaria",
      "Correct — lesions lasting under twenty-four hours and blanching fully is the key diagnostic feature."],
     ["Urticarial vasculitis",
      "There, lesions persist beyond twenty-four hours and leave bruising, with low complement."],
     ["Erythema multiforme in its early stage",
      "Target lesions are fixed, last more than twenty-four hours and favour acral surfaces."],
     ["The pre-bullous phase of bullous pemphigoid",
      "This can mimic urticaria but occurs in the elderly and needs biopsy with immunofluorescence."]],
   c=0, cite=c(37)),

 dict(topic="Urticaria", io=IOA,
   q="A 44-year-old woman has itchy wheals that persist for two to three days and fade leaving brownish discoloration. Which is the most appropriate next step?",
   opts=[
     ["Skin biopsy, since lesions persisting beyond twenty-four hours suggest urticarial vasculitis",
      "Correct — the persistence and residual bruising are what take this out of simple urticaria."],
     ["Increase the second-generation antihistamine to four times the standard dose",
      "Dose escalation is right for chronic urticaria but not before this atypical pattern is explained."],
     ["Measure complement C4 and C1-esterase inhibitor level and function",
      "That is indicated for recurrent angio-oedema occurring without wheals."],
     ["Begin omalizumab at 300 mg subcutaneously every four weeks",
      "That is reserved for refractory chronic urticaria after a diagnosis is established."]],
   c=0, cite=c(38)),

 dict(topic="Urticaria", io=IOA,
   q="A 33-year-old man has recurrent episodes of lip and periorbital swelling without any wheals. Which is the most appropriate initial testing?",
   opts=[
     ["Complement C4 with C1-esterase inhibitor level and function",
      "Correct — angio-oedema without wheals should raise hereditary angio-oedema."],
     ["Serum tryptase with a search for Darier's sign on examination",
      "That combination investigates mastocytosis."],
     ["Autologous serum skin test for autoimmune chronic urticaria",
      "That is used in chronic urticaria with wheals."],
     ["Thyroid-stimulating hormone with anti-thyroid peroxidase antibodies",
      "Those form part of the chronic urticaria workup rather than isolated angio-oedema."]],
   c=0, cite=c(38)),

 dict(topic="Urticaria", io=IOA,
   q="A 30-year-old woman has had daily wheals for four months despite a standard dose of cetirizine. She is otherwise well. Which is the most appropriate next step in management?",
   opts=[
     ["Increase the non-sedating antihistamine to up to four times the standard dose",
      "Correct — scheduled up-dosing is the next step before adding other agents."],
     ["Begin omalizumab at 300 mg subcutaneously every four weeks",
      "Right drug, wrong point: omalizumab is for refractory disease after antihistamine optimisation."],
     ["Begin cyclosporine with monitoring of blood pressure and renal function",
      "Cyclosporine is reserved for refractory autoimmune urticaria."],
     ["Prescribe a five-day course of prednisone at 40 to 60 mg daily",
      "Short steroid courses are used for severe acute urticaria rather than chronic disease."]],
   c=0, cite=c(39)),

 dict(topic="Urticaria", io=IOA,
   q="A 22-year-old man develops widespread wheals, lip swelling and audible wheeze twenty minutes after eating shellfish. Which is the most appropriate immediate treatment?",
   opts=[
     ["Intramuscular epinephrine 0.3 mg",
      "Correct — bronchospasm with angio-oedema is anaphylaxis, and epinephrine comes before anything else."],
     ["Intravenous diphenhydramine followed by oral cetirizine",
      "Antihistamines are adjuncts and do not treat airway or circulatory compromise."],
     ["Oral prednisone 40 to 60 mg as a single loading dose",
      "Steroids have a delayed effect and are not the immediate treatment."],
     ["Nebulised salbutamol with high-flow supplemental oxygen",
      "This addresses bronchospasm but not the underlying anaphylaxis."]],
   c=0, cite=c(39)),

 dict(topic="Urticaria", io=IOA,
   q="A 29-year-old woman has had chronic spontaneous urticaria for eight months and asks whether it will ever settle. Which is the most appropriate counselling point?",
   opts=[
     ["About half of chronic urticaria resolves spontaneously within a year, and over half of cases have no identifiable trigger",
      "Correct — this reframes the search for a cause that often does not exist."],
     ["A specific trigger can be identified in almost every case with sufficient testing",
      "More than half of chronic urticaria is idiopathic."],
     ["The condition is lifelong once it has persisted beyond six weeks in duration",
      "Spontaneous resolution occurs in about half within a year."],
     ["Complete avoidance of all common food allergens will resolve the condition",
      "Dietary avoidance does not address idiopathic or autoimmune chronic urticaria."]],
   c=0, cite=c(36)),
]
