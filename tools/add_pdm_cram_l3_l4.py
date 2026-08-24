#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Lecture 3 and Lecture 4 topics to the PDM I Exam 1 cram sheet.

Same colour-coded topic/table structure as build_pdm_cram.py: the guide carries
the explanation, this carries only what has to be recallable cold.

Lecture 4's three disputed reference ranges get their OWN row rather than being
quietly resolved, because the disagreement is itself the thing to know.

Appended after the Lecture 2 sections, in syllabus order. Idempotent.
"""
import os, re, sys, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1",
                    "pdm-exam-1-cram-sheet.html")

TOPICS = [
 ("l3-bedside", "KOH, Biopsy & the Melanoma Rule", "#2f6b4a", "#e0efe7", "#f0f7f3", "#235238", [
   ("The four test-selection factors", "COST · AVAILABILITY · INVASIVENESS · DIAGNOSTIC YIELD. And the closing rule: ALWAYS CHOOSE THE LEAST INVASIVE TEST THAT ANSWERS THE CLINICAL QUESTION."),
   ("Which test for which question", "INFECTION → potassium hydroxide or culture. NEOPLASM or PERSISTENT RASH → biopsy. ABSCESS vs CELLULITIS → point-of-care ultrasound."),
   ("KOH readings — the whole table", "NEGATIVE: no fungal elements. BRANCHING SEPTATE HYPHAE = DERMATOPHYTE. PSEUDOHYPHAE + BUDDING YEAST = CANDIDA. “SPAGHETTI AND MEATBALLS” = TINEA VERSICOLOR."),
   ("KOH procedure numbers", "20% potassium hydroxide, ONE drop. Survey at 10× with the CONDENSER LOWERED to reduce illumination (that is what makes epithelial cells visible), then 40× for anything suspicious. Blot excess with GAUZE. Sensitivity depends on ADEQUATE SCRAPING."),
   ("Biopsy techniques", "SHAVE: raised epidermal lesions, basal and squamous cell carcinoma, superficial rashes. PUNCH: FULL-THICKNESS, inflammatory rashes and small lesions. EXCISIONAL: entire lesion, PREFERRED FOR SUSPECTED MELANOMA."),
   ("THE MELANOMA RULE — she said it three times", "NARROW EXCISIONAL BIOPSY, 1–3 mm MARGINS, to a depth that AVOIDS TRANSECTING THE BASE so BRESLOW DEPTH can be measured. NOT a shave. NOT a punch. Acceptable excisional methods: fusiform/elliptical, punch, deep shave/saucerization — ALL must go BELOW the lesion."),
   ("1–3 mm vs 0.5–2 cm — do not mix these up", "1–3 MILLIMETRES is the DIAGNOSTIC biopsy margin here in PDM. 0.5–2 CENTIMETRES is the definitive RE-EXCISION margin in CMS I Lecture 9. Different procedure, different purpose."),
   ("When a partial shave is allowed", "ONLY WHEN SUSPICION IS LOW — and it MAY UNDERESTIMATE BRESLOW DEPTH. Facial, acral and very large lesions are named here."),
   ("Breslow / T categories", "Tis = IN SITU. T1 ≤1 mm. T2 >1 to 2 mm. T3 >2 to 4 mm. T4 >4 mm. T is DEPTH IN MILLIMETRES, not width."),
   ("Biopsy limitations", "SAMPLING ERROR, and procedural risks of BLEEDING, SCARRING, INFECTION. She added: THE TECHNIQUE ITSELF DETERMINES HOW EASILY THE SPECIMEN CAN BE EVALUATED."),
 ]),
 ("l3-soft-tissue", "Soft Tissue Infection, Cultures & the Red Flag", "#8a3f2c", "#f4e5df", "#faf2ef", "#6b3020", [
   ("POCUS — cellulitis vs abscess", "CELLULITIS: dermal thickening, increased echogenicity, COBBLESTONING (footnoted as non-specific — VENOUS STASIS does it too). ABSCESS: HYPOECHOIC/heterogeneous collection, possible debris or septations, POSTERIOR ACOUSTIC ENHANCEMENT."),
   ("★ THE RED FLAG she bolded AND said aloud", "HYPOTENSION + WHITE BLOOD CELL COUNT ≥15,000 + VIOLACEOUS (purple) SKIN → MUST be screened for NECROTIZING FASCIITIS. Her framing: a patient who looks TOO SICK FOR A SKIN INFECTION."),
   ("When to escalate past ultrasound", "DEEP-SPACE INFECTION · NECROTIZING INFECTION · FOREIGN BODY · GAS. CONTRAST MRI BEST DEFINES THE EXTENT OF TISSUE DAMAGE."),
   ("Skin/wound culture indications", "PURULENT LESIONS — pus from abscesses, carbuncles, furuncles. Empiric treatment WITHOUT culture is reasonable in TYPICALLY PRESENTING, UNCOMPLICATED cases. DO NOT CULTURE AN INFLAMED EPIDERMOID CYST."),
   ("Culture a chronic wound when", "IMMUNOCOMPROMISED · MRSA SUSPECTED · TREATMENT FAILURE."),
   ("THE LEVINE METHOD", "Clean with STERILE WATER OR SALINE, NOT AN ANTIMICROBIAL. Identify 1–2 cm of CLEAN wound tissue. ROTATE the applicator FIVE SECONDS with enough pressure to EXPRESS FLUID. DO NOT sample EXUDATE, ESCHAR or NECROTIC MATERIAL."),
   ("Culture: advantage vs limits", "ADVANTAGE: organism identification PLUS SUSCEPTIBILITIES. LIMITS: superficial swabs prone to CONTAMINATION AND COLONISATION, may NOT correlate with deep infection. Complex wounds (diabetic foot, pressure ulcers) → DEEPER TISSUE BIOPSY OR ASPIRATE gives higher yield."),
 ]),
 ("l3-eye", "The Four Ophthalmic Tests", "#3a4f8a", "#e1e6f2", "#f0f2f8", "#2c3d6e", [
   ("VVEEPP", "VISUAL ACUITY · VISUAL FIELDS · EXTERNAL EXAM · EXTRAOCULAR MOVEMENTS · PUPILS · PRESSURE."),
   ("Visual acuity", "INDICATION: EVERY EYE COMPLAINT. Snellen DISTANCE, Rosenbaum NEAR. Test BEST-CORRECTED; add PINHOLE if reduced. UNILATERAL loss → optic nerve/ocular. BILATERAL → systemic/intracranial."),
   ("Pinhole", "Blocks PERIPHERAL light, focuses CENTRAL rays on the retina. CORRECTS → REFRACTIVE. DOES NOT CORRECT OR WORSENS → EYE PATHOLOGY."),
   ("Visual field patterns", "CENTRAL SCOTOMA → macula/optic nerve. PERIPHERAL LOSS → GLAUCOMA. BITEMPORAL HEMIANOPIA → CHIASMAL (pituitary). HOMONYMOUS HEMIANOPIA → RETROCHIASMAL (?stroke). Bedside = CONFRONTATION; formal = PERIMETRY or AMSLER GRID."),
   ("Fluorescein", "Cobalt-BLUE light, AFTER a topical anesthetic. LINEAR → ABRASION. BRANCHING/DENDRITIC → HERPETIC KERATITIS. FIXED DENSE STAINING or OPACITY → ULCER, URGENT REFERRAL. Indications: eye pain, foreign-body sensation, trauma, contact lenses, red eye."),
   ("Tonometry", "Normal intraocular pressure 10–21 mm Hg. ACUTE ANGLE-CLOSURE GLAUCOMA IS AN OPHTHALMOLOGIC EMERGENCY. PRESSURE ALONE IS INSUFFICIENT — most OPEN-ANGLE glaucoma has NORMAL pressure, and readings vary with CORNEAL THICKNESS."),
   ("Optic disc cupping", "Normal cup-to-disc ~0.3; GLAUCOMATOUS >0.7. Glaucomatous disc is EXCAVATED, NOT MERELY PALE — that is what separates it from other optic atrophies. Lamina cribrosa collapse."),
   ("Ocular hypertension vs glaucoma", "OCULAR HYPERTENSION = raised pressure, NO optic damage, NORMAL fields — a RISK FACTOR. GLAUCOMA = raised pressure WITH OPTIC NERVE DAMAGE."),
 ]),
 ("l3-ent", "Throat, Hearing & the Tympanogram", "#7a4a8a", "#eee3f2", "#f7f2f9", "#5e3a6b", [
   ("Rapid strep vs throat culture", "RADT: fast, point-of-care, SENSITIVITY ONLY 70–90% → FALSE NEGATIVES. CULTURE: GOLD STANDARD, highest sensitivity, but DELAYED 24–48 HOURS."),
   ("The two pearls", "A NEGATIVE RADT IN A CHILD should be confirmed by CULTURE — NOT routinely required in adults. DO NOT USE ANTISTREPTOCOCCAL ANTIBODY (ASO) TITRES to diagnose ACUTE pharyngitis."),
   ("Audiometry", "Quantifies DEGREE AND TYPE — CONDUCTIVE vs SENSORINEURAL — AFTER abnormal physical exam. Indications: suspected/confirmed loss, PERSISTENT otitis media with effusion, ASYMMETRIC loss (to screen for RETROCOCHLEAR pathology)."),
   ("The two audiometry numbers", "AIR–BONE GAP ≥10 dB correlates with MIDDLE-EAR FLUID. Primary-care FAIL = >20 dB HL at ≥1 FREQUENCY."),
   ("Pure tone audiometry", "Screening presents at UPPER LIMITS OF NORMAL: 25–30 dB ADULTS, 15–20 dB CHILDREN. THRESHOLD = softest sound heard at each frequency 50% OF THE TIME. Audiogram: INTENSITY on the VERTICAL axis; RIGHT = RED CIRCLE, LEFT = BLUE X. Bone conduction vibrates through FOREHEAD or MASTOID. WE LOSE HIGH FREQUENCIES FIRST (presbycusis)."),
   ("Tympanometry mechanics", "Varies AIR PRESSURE IN THE EXTERNAL CANAL, measures REFLECTED ENERGY. THE LESS COMPLIANT THE SYSTEM, THE GREATER THE INTENSITY REFLECTED BACK. Pressure = HORIZONTAL axis, compliance = VERTICAL. Normal peak 50 mm H2O."),
   ("TYMPANOGRAM TYPES", "A = NORMAL (also typical of SENSORINEURAL loss with a normal middle ear). B = RESTRICTED MOBILITY. C = SIGNIFICANT NEGATIVE PRESSURE (eustachian tube dysfunction), significant for treatment BELOW −200 mm H2O. AS = normal pressure, REDUCED mobility (S = stiff/shallow; ossicular fixation, tympanosclerosis). AD = normal pressure, HYPERmobility (flaccid membrane, disarticulation)."),
   ("The flat tympanogram split", "FLAT + HIGH CANAL VOLUME → PERFORATION or PATENT TUBE. FLAT + NORMAL VOLUME → MIDDLE-EAR EFFUSION. That one number is the whole difference."),
   ("_skip_ — she said she will NOT ask this", "The ANIMAL HEARING RANGES figure. Verbatim at 1:00:43: “I’m not going to ask you to be like, what is the range of the killer whale.” It is there to show how wide human hearing is, nothing more."),
 ]),
 ("l3-imaging", "Head & Neck Imaging", "#2e6b78", "#dfeef0", "#eff7f8", "#22525c", [
   ("CT vs MRI — the two pearls", "THINK CT FOR BONE, TRAUMA AND SPEED. THINK MRI FOR SOFT TISSUE, NERVES, AND TUMOUR OR INTRACRANIAL EXTENSION."),
   ("Contrast CT strengths", "FIRST-LINE FOR MOST ACUTE HEAD AND NECK INFECTIONS. Shows ABSCESS, OEDEMA, GAS, BONE EROSION. Strengths: calcification/bone, sinuses, ACUTE TRAUMA and ORBITAL FRACTURES, FOREIGN BODIES, and the UNSTABLE OR CLAUSTROPHOBIC patient."),
   ("MRI strengths", "SUPERIOR SOFT-TISSUE CONTRAST, NO IONIZING RADIATION, INTRACRANIAL/ORBITAL EXTENSION, PERINEURAL SPREAD, SKULL BASE, TUMOURS."),
   ("NO IMAGING NEEDED", "UNCOMPLICATED ACUTE RHINOSINUSITIS · OTITIS · SIMPLE SOFT-TISSUE INFECTIONS."),
   ("Emergency imaging triggers", "FACIAL SWELLING · PROPTOSIS · EYE SIGNS · NEURO SIGNS → contrast CT of SINUSES AND ORBITS. Also complicated sinusitis or orbital cellulitis."),
   ("Neck mass vs deep neck infection", "NECK MASS → ULTRASOUND FIRST (superficial/cystic vs solid, size, VASCULARITY on Doppler). DEEP NECK INFECTION → CONTRAST CT NECK, and the deck says ULTRASOUND IS NOT HELPFUL. Do not swap these."),
   ("Deep neck infection — the 3 questions", "Is there a DRAINABLE ABSCESS · is the AIRWAY compromised · is it SPREADING TOWARDS THE MEDIASTINUM."),
   ("MRI adds value for", "INTRACRANIAL EXTENSION · VASCULAR THROMBOSIS (LEMIERRE) · OSTEOMYELITIS."),
   ("Acoustic neuroma", "MRI WITH CONTRAST — for suspected acoustic neuroma or ASYMMETRIC SENSORINEURAL HEARING LOSS."),
   ("CT findings by region", "SINUS: mucosal thickening, AIR-FLUID LEVELS, opacification. ORBIT: orbital cellulitis with FAT STRANDING, abscess, BLOWOUT FRACTURE, herniated orbital contents. NECK: abscess as a RIM-ENHANCING fluid collection, enlarged or NECROTIC nodes."),
   ("Blow-out vs tripod fracture", "BLOW-OUT: air in the orbit (ORBITAL EMPHYSEMA), fracture of the ORBITAL FLOOR, soft tissue extending into the TOP OF THE MAXILLARY SINUS. TRIPOD: DIASTASIS OF THE FRONTOZYGOMATIC SUTURE + orbital floor fracture with emphysema + fracture through the LATERAL WALL of the maxillary sinus (filled with blood)."),
 ]),
 ("l4-cbc-wbc", "CBC Components & the White Cell Lines", "#8a5a1f", "#f2e8d8", "#f9f4ec", "#6b4515", [
   ("★ THE DECK DISAGREES WITH ITSELF — 3 values", "LYMPHOCYTES: reference table 25–33%, teaching slide 24–44%. PLATELETS: table 150,000–400,000, slide 150,000–450,000. RDW: table 11–15%, slide 12–15%. A FOURTH set is on the labelled smear (slide 15) and matches neither. Everything else agrees across both."),
   ("With vs without differential", "WITHOUT: red cell count, red cell indices, TOTAL white count, platelets — for SCREENING/MONITORING anemia, leukocytosis/leukopenia, thrombocytopenia. WITH: adds NEUTROPHILS, LYMPHOCYTES, MONOCYTES, EOSINOPHILS, BASOPHILS — when the SPECIFIC LINE matters."),
   ("Which line for which problem", "BACTERIAL → NEUTROPHILS. VIRAL → LYMPHOCYTES. ALLERGY/PARASITES → EOSINOPHILS."),
   ("White cell count", "NORMAL 4,500–11,000 cells/μL. LEUKOPENIA below, LEUKOCYTOSIS above."),
   ("Granulocyte vs agranulocyte", "GRANULOCYTES (neutrophil, eosinophil, basophil): DISTINCTIVE CYTOPLASMIC GRANULES with enzymes, proteins, toxic substances. AGRANULOCYTES (monocyte, lymphocyte): NO granules, NON-LOBULAR nucleus."),
   ("Neutrophils", "54–62%, MOST ABUNDANT. 3–4 LOBED nucleus, granular cytoplasm. AKA polys, PMNs, segs. MAIN DEFENSE AGAINST BACTERIA by PHAGOCYTOSIS."),
   ("Bands & LEFT SHIFT", "BANDS = IMMATURE NEUTROPHILS, normal ≤5%, ONE OR TWO lobes separated by a THICK CHROMATIN BAND. NEUTROPHILS + BANDS = BACTERIAL INFECTION. LEFT SHIFT = increase in IMMATURE cells — neutrophils are CONSUMED faster than they can be replaced."),
   ("Neutrophils UP", "Bacterial infection · MYOCARDIAL INFARCTION · burns · STEROIDS · rheumatoid arthritis · physiologic (PREGNANCY/LABOR, SURGERY)."),
   ("Neutrophils DOWN", "Bone marrow damage · FOLATE AND B12 DEFICIENCY (both needed for MARROW FUNCTION) · radiation · TOXIC CHEMICALS (BENZENE) · OVERWHELMING infection · viral (MONONUCLEOSIS, HIV, HEPATITIS)."),
   ("Why steroids raise neutrophils", "DEMARGINATION — they cause neutrophils to DETACH FROM THE BLOOD VESSEL WALL and enter the main bloodstream. Not increased production."),
   ("Eosinophils / Basophils", "EOS 1–3%, TWO-LOBED, granules contain HISTAMINES. Up: PARASITES, ALLERGY, CANCER. BASO <1%, usually two-lobed, granules contain HEPARIN + histamine. Up: allergy, cancer. A NORMAL COUNT CAN BE ZERO for both."),
   ("Monocytes / Lymphocytes", "MONO 3–7%, LARGEST white cell, NO granules → MACROPHAGES or DENDRITIC CELLS (KUPFFER in liver, ALVEOLAR in lung, LANGERHANS in skin). Up: chronic inflammation, stress, viral. LYMPH: small, mononuclear, no granules; T, B and NK cells — THE CBC DOES NOT TELL THEM APART. Up: VIRAL. Down: HIV."),
   ("Cell lifespans (image-only)", "NEUTROPHIL 7 HOURS · EOSINOPHIL 8–12 DAYS · BASOPHIL a few hours to a few days · MONOCYTE 3 DAYS · B and T MEMORY CELLS MAY LIVE FOR YEARS."),
 ]),
 ("l4-anc-plt", "Absolute Counts, Platelets & the Indices", "#3f5f2f", "#e5ecdd", "#f2f6ee", "#2f481f", [
   ("★ ABSOLUTE NEUTROPHIL COUNT", "ANC = WBC × (%NEUTROPHILS + %BANDS) ÷ 100. BANDS COUNT WITH THE NEUTROPHILS — that is the trap. Alternative form when WBC is in thousands: 10 × WBC(thousands) × (%neuts + %bands)."),
   ("The deck's worked example", "6,000/μL with 40% neutrophils and 5% bands → 6,000 × 45 ÷ 100 = 2,700/μL. NOTE the slide prints “6,000 x (40 + 5/100)” which evaluates to 240,300 — the BRACKETS are a typo, the ANSWER of 2,700 is right."),
   ("★ NEUTROPENIA GRADES (image-only)", "MILD 1,000 to <1,500 cells/μL. MODERATE 500 to <1,000. SEVERE <500. NOT IN THE SLIDE TEXT AT ALL."),
   ("General absolute count", "ANY line: TOTAL WBC × THAT TYPE'S PERCENTAGE ÷ 100. A percentage means nothing without the total."),
   ("Platelets", "From MEGAKARYOCYTES in the BONE MARROW, break into FRAGMENTS — so NOT REALLY CELLS. Lifespan 7–10 DAYS. PRIMARY ROLE HEMOSTASIS. HEMORRHAGE RISK INCREASES BELOW 20,000."),
   ("Platelets UP / DOWN", "UP: trauma, acute hemorrhage, IRON DEFICIENCY, polycythemia vera. DOWN: MARROW SUPPRESSION — chemo, alcohol, radiation, aplastic anemia, drugs. Note IRON DEFICIENCY RAISES PLATELETS WHILE LOWERING RED CELLS."),
   ("Mean platelet volume", "7.5–12.5 fL, AVERAGE SIZE of platelets, a marker of FUNCTION AND ACTIVATION. UP = increase in IMMATURE platelets (recent blood loss). DOWN = bone marrow failure."),
   ("Hemoglobin vs hematocrit", "HEMOGLOBIN = amount of hemoglobin in a VOLUME of blood. HEMATOCRIT = PERCENTAGE of blood that is red cells (packed cell volume). RULE OF THUMB: HEMOGLOBIN × 3 = HEMATOCRIT."),
   ("The three that raise ALL of RBC/Hgb/Hct", "POLYCYTHEMIA VERA · CHRONIC HYPOXIA (COPD, sleep apnea, high altitude) · DEHYDRATION. Hematocrit adds SMOKING and HYPOVENTILATION; its decreased list adds HEMOLYSIS."),
   ("★ THE FOUR INDICES", "MCV = Hct(%) × 10 ÷ RBC — average VOLUME, 80–100 fL, MEASURED. MCH = Hgb × 10 ÷ RBC — hemoglobin PER CELL, 27–33 pg. MCHC = Hgb × 100 ÷ Hct — CONCENTRATION in packed cells, 32–36 g/dL. RDW = degree of ANISOCYTOSIS. MCH AND MCHC DIFFER ONLY IN THE DENOMINATOR."),
   ("MCHC's special job", "AUTOMATED SCREENING FLAG for HEREDITARY SPHEROCYTOSIS and other HYPERCHROMIC/DEHYDRATED red cell states."),
   ("Hypo / normo / hyperchromic", "HYPOchromic: central pallor >1/3 of the diameter, MCH <27, MCHC <32 — iron deficiency, thalassemia. NORMOchromic: pallor EXACTLY 1/3. HYPERchromic: MCH >33, MCHC >36 — SPHEROCYTES."),
   ("The red cell COUNT caveat", "It DOES NOT accurately measure OXYGEN CARRYING CAPACITY and is NOT directly used to diagnose anemia — though still used to evaluate it."),
 ]),
 ("l4-morphology", "Red Cell Morphology — Shape & Inclusions", "#8a3f5c", "#f3e2e9", "#f9f1f4", "#6b2e46", [
   ("The four categories", "SIZE · HEMOGLOBIN DISTRIBUTION · SHAPE VARIATION (POIKILOCYTOSIS) · INCLUSIONS AND CELL DISTRIBUTION."),
   ("★ ACANTHOCYTE vs ECHINOCYTE", "ACANTHOCYTE (spur, “acantha” = thorn): IRREGULAR spikes, NO central pallor → LIVER DISEASE. ECHINOCYTE (burr, sea urchin): REGULARLY distributed, LESS POINTED tips, CENTRAL PALLOR PRESERVED → RENAL DISEASE. Two features, two diseases."),
   ("Schistocytes", "FRAGMENTED red cells — helmet, horn, TRIANGULAR, MICROSPHEROCYTE (last two are IMAGE-ONLY). Usually MICROCYTIC, LACK central pallor. HEMOLYSIS, MECHANICAL TRAUMA (mechanical heart valves), MEDICATIONS (CYCLOSPORINE). ★ AUTOMATED COUNTERS MAY COUNT THEM AS PLATELETS."),
   ("Sickled cell (drepanocyte)", "THIN CRESCENT, NO central pallor, DENSE hemoglobin so NORMOCHROMIC TO HYPERCHROMIC. Forms UNDER LOW OXYGEN TENSION, causes SLUDGING in tissues."),
   ("Spherocyte", "PERFECTLY ROUND, LOSS OF CENTRAL PALLOR, often SMALLER than normal → HEREDITARY SPHEROCYTOSIS (mostly INHERITED; shortens red cell life)."),
   ("Target cell (codocyte)", "DARK CIRCLE INSIDE the central pallor = BULLSEYE. Due to REDUNDANT CELL MEMBRANE. POST SPLENECTOMY and LIVER DISEASE."),
   ("Teardrop cell (dacrocyte)", "Formed in BONE MARROW INFILTRATED BY SCAR TISSUE OR CANCEROUS CELLS → BONE MARROW DISEASE."),
   ("Basophilic stippling", "BLUE-BLACK dots of RIBOSOMAL RNA, EVENLY DISTRIBUTED through the cytoplasm → LEAD POISONING. The even distribution is the discriminator."),
   ("Howell-Jolly body", "A SINGLE dot-like DARK PURPLE RESIDUAL NUCLEAR FRAGMENT → POST SPLENECTOMY. Normally REMOVED BY THE SPLEEN, so finding one means SPLENIC DYSFUNCTION OR ASPLENIA. Target cells appear in the same field."),
   ("★ HEINZ BODIES — the easiest thing to miss", "DENATURED HEMOGLOBIN at the PERIPHERY of the cell → G6PD DEFICIENCY. THEY REQUIRE A SUPRAVITAL STAIN (NEW METHYLENE BLUE) — INVISIBLE ON THE ROUTINE WRIGHT STAIN, so nobody reports them unless you ask. This fact is ONLY inside the figure."),
   ("Rouleaux vs agglutination", "ROULEAUX: STACKED IN CHAINS, “ROWS OF COINS” — RAISED SERUM PROTEINS NEUTRALISE the red cells' NEGATIVE SURFACE CHARGE → MULTIPLE MYELOMA, LIVER DISEASE. AGGLUTINATION: DISORDERLY CLUMPING — ANTIBODIES COAT and BRIDGE the cells → TRANSFUSION REACTIONS."),
 ]),
 ("l4-anemia", "Working Up an Anemia", "#2f4f7a", "#e0e7f0", "#eff3f7", "#233c5e", [
   ("The four evaluation steps", "ASSESS CLINICAL PRESENTATION · CHECK CBC AND CHEMISTRY PANEL · DETERMINE THE MCV · CHECK THE RETICULOCYTE COUNT. Do them SIMULTANEOUSLY. Look at the PERIPHERAL SMEAR if you can get one."),
   ("Reticulocyte count", "Tells you whether the BONE MARROW IS FUNCTIONING. Most helpful when VERY ELEVATED OR VERY DECREASED. DECREASED = UNDERPRODUCTION. INCREASED = HEMOLYSIS OR BLOOD LOSS."),
   ("★ THE THREE MCV BANDS", "MICROCYTIC <80 fL · NORMOCYTIC 80–100 fL · MACROCYTIC >100 fL. Hemoglobin says there IS an anemia; MCV says WHICH ALGORITHM TO RUN."),
   ("Microcytic causes", "IRON DEFICIENCY (MOST COMMON CAUSE OF ANEMIA — MUST EVALUATE FOR OCCULT BLOOD LOSS, often the FIRST SIGN OF GI BLEEDING) · LEAD POISONING · ANEMIA OF CHRONIC DISEASE · THALASSEMIA · SIDEROBLASTIC ANEMIA."),
   ("★ IRON STUDIES — the two patterns", "IRON DEFICIENCY: FERRITIN ↓, IRON ↓, TIBC ↑. ANEMIA OF CHRONIC DISEASE: FERRITIN ↑, IRON ↓, TIBC ↓. Ferritin is an ACUTE PHASE REACTANT, so it RISES in inflammation even though the iron is unavailable."),
   ("All three normal in a microcytic anemia", "→ Is there BASOPHILIC STIPPLING? YES → obtain SERUM LEAD. NO → THALASSEMIA TRAIT."),
   ("Iron comparison table (image-only)", "THALASSAEMIA MINOR is the row where the MCV IS LOW AND EVERYTHING ELSE IS NORMAL. INFLAMMATORY ANAEMIA is the one with a NORMAL MCV. THALASSAEMIA MAJOR and SIDEROBLASTIC both have LOW MCV with RAISED FERRITIN."),
   ("Iron transport analogy", "BUS = TRANSFERRIN (transports). BUS STOP = FERRITIN (stores; MEASURABLE because it is outside the marrow). HOME = HEMOSIDERIN (CANNOT be measured). % SATURATION = TIBC (how many can sit on the bus). SCHOOL = the RED BLOOD CELL."),
   ("Macrocytic — megaloblastic vs not", "MEGALOBLASTIC: B12, FOLATE, DRUGS IMPAIRING DNA SYNTHESIS (METHOTREXATE, ANTIRETROVIRALS, HYDROXYUREA), COPPER. NON-MEGALOBLASTIC: ALCOHOL, LIVER DISEASE, HYPOTHYROIDISM, RETICULOCYTOSIS, primary marrow disorders, chronic kidney disease."),
   ("The megaloblastic smear finding", "MACROOVALOCYTES + HYPERSEGMENTED NEUTROPHILS. WITHOUT them → CHRONIC LIVER DISEASE or ACUTE HEMATOLOGIC MALIGNANCY."),
   ("Normocytic — the split", "HYPO-PROLIFERATIVE: aplastic anemia, anemia of chronic disease, MARROW INFILTRATION BY TUMOR, hypometabolic states. HEMOLYSIS/HEMORRHAGE: acute blood loss (HGB AND HCT START TO FALL WITHIN 2–3 DAYS), intrinsic and extrinsic hemolytic anemia, sickle cell."),
   ("Intrinsic vs extrinsic hemolysis", "INTRINSIC = a DEFECT IN THE RED CELL causing PREMATURE SPLENIC REMOVAL. EXTRINSIC = MECHANICAL STRESS, IMMUNOLOGIC DESTRUCTION or INFLAMMATORY INJURY FROM OUTSIDE."),
   ("★ The normocytic reticulocyte split", "HIGH RETICS → HEMOLYSIS, SICKLE CELL, ACUTE HEMORRHAGE. LOW RETICS + LOW WBC/PLATELETS → LEUKEMIA, METASTATIC MALIGNANCY, APLASTIC ANEMIA. LOW RETICS + NORMAL/HIGH WBC/PLATELETS → CHRONIC INFECTION/INFLAMMATION, MALIGNANCY, CHRONIC RENAL DISEASE, ENDOCRINE DYSFUNCTION."),
   ("Two things in the algorithm people walk past", "IRON DEFICIENCY APPEARS IN BOTH THE MICROCYTIC AND THE NORMOCYTIC BRANCH — which is why iron studies are obtained even with a normal MCV. And in the microcytic branch obtain IRON STUDIES IN ALL INDIVIDUALS, because CONCOMITANT IRON DEFICIENCY CAN AFFECT HEMOGLOBIN ANALYSIS and hide a thalassemia."),
   ("The fishbone", "WBC on the LEFT · HGB ABOVE the centre line · HCT BELOW it · PLATELETS on the RIGHT."),
 ]),
]


def section(t):
    tid, title, acc, bg, zeb, ink, rows = t
    body = "\n".join(
        '          <tr><td class="h">%s</td><td>%s</td></tr>' % (H.escape(a), H.escape(b))
        for a, b in rows)
    return ('\n  <section class="topic" id="%s" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">\n'
            '    <div class="shead"><span class="dot" style="background:%s"></span><h2>%s</h2></div>\n'
            '    <div class="scroll">\n      <table>\n'
            '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
            '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n'
            % (tid, acc, bg, zeb, ink, acc, H.escape(title), body))


def main():
    s = open(CRAM, encoding="utf-8").read()
    if 'id="l3-bedside"' in s:
        sys.exit("Lecture 3 and 4 cram sections already present -- nothing to do")

    used = set(re.findall(r"--acc:(#[0-9a-f]{6})", s))
    clash = sorted(used & {t[2] for t in TOPICS})
    assert not clash, "accent already used by another topic: %r" % clash
    mine = [t[2] for t in TOPICS]
    assert len(mine) == len(set(mine)), "two new topics share an accent"

    last = s.rindex('<section class="topic"')
    end = s.index("\n  </section>", last) + len("\n  </section>\n")
    links_anchor = s.rindex("</a>\n", 0, s.index("</nav>") if "</nav>" in s else len(s)) + len("</a>\n")

    links = "".join(
        '      <a href="#%s" style="color:%s"><span class="dot" style="background:%s"></span>%s</a>\n'
        % (t[0], t[5], t[2], t[1]) for t in TOPICS)
    s = s[:end] + "".join(section(t) for t in TOPICS) + s[end:]
    s = s[:links_anchor] + links + s[links_anchor:]

    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th", "div"):
        o, c = len(re.findall(r"<%s[ >]" % tag, s)), s.count("</%s>" % tag)
        assert o == c, "%s: %d open, %d close" % (tag, o, c)
    ids = set(re.findall(r'id="([^"]+)"', s))
    dangling = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a and a not in ids]
    assert not dangling, "dangling jump links: %r" % dangling
    assert "**" not in s, "markdown emphasis left in a cram row"
    order = re.findall(r'<section class="topic" id="([^"]+)"', s)
    assert order.index("imaging-lecture") < order.index("l3-bedside"), "Lecture 3 must follow Lecture 2"
    assert order.index("l3-imaging") < order.index("l4-cbc-wbc"), "Lecture 4 must follow Lecture 3"

    open(CRAM, "w", encoding="utf-8").write(s)
    print("Lecture 3 and 4 cram topics added: %d sections, %d rows"
          % (len(TOPICS), sum(len(t[6]) for t in TOPICS)))
    print("tag balance, jump links, accent uniqueness and syllabus order verified")


if __name__ == "__main__":
    main()
