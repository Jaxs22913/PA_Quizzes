"""Length-bias remediation for Principles of Diagnostic Medicine I, Lecture 4.

This deck is the most enumeration-heavy of the four so far -- "which four
indices", "which five cell types", "which causes of increased neutrophils" --
and a correct answer that must name six causes is unavoidably longer than a
wrong one naming four. The tell is created by the question type, not by careless
writing, so PADDING is the repair throughout. Trimming would delete the very
items the question asks the student to recall.

Keys are (index into the concatenated pool A + B + C + D, index of the WRONG
option to rewrite). Indices rather than string matching, because option strings
recur across questions in a deck this repetitive -- and in Lecture 3 a string
replace silently hit a distractor in one question and the CORRECT answer in
another. The applier asserts a fix never lands on the correct answer.

Pools are APPENDED, never prepended, so these indices stay valid. The partition
script asserts each offset below still matches the real pool lengths.
"""
A = 0    # pool A starts the concatenation

FIXES = {
 (A + 1,  1): "Mean corpuscular volume, hemoglobin concentration, hematocrit percentage, and the red blood cell distribution width",
 (A + 3,  3): "Tissue histiocytes, Kupffer cells, dendritic cells and alveolar macrophages",
 (A + 6,  1): "To work up a suspected bacterial infection by checking neutrophils and bands",
 (A + 9,  1): "Fight infection, transport oxygen to the peripheral tissues, produce antibodies, and maintain vascular integrity",
 (A + 11, 3): "Pallor, dyspnoea on exertion, palpitations, dizziness and cold intolerance",
 (A + 12, 1): "Monocytes and lymphocytes, which have distinctive cytoplasmic granules too",
 (A + 16, 1): "The body's main defense against parasites and its primary defense against allergens, by releasing granule contents",
 (A + 17, 1): "Immature neutrophils, normally fifteen per cent or less, with three or four fully separated nuclear lobes",
 (A + 20, 2): "Immature cells survive considerably longer in the circulation than the fully mature ones do",
 (A + 21, 1): "Bacterial infection, radiation exposure, severe burns, benzene and other toxic chemicals, and an overwhelming systemic infection",
 (A + 22, 1): "They stimulate the bone marrow to produce and release far more neutrophils daily",
 (A + 23, 1): "Bacterial infection, myocardial infarction, burns, steroid therapy, rheumatoid arthritis, and pregnancy or labor",
 (A + 31, 1): "Neutrophils or eosinophils, found in the bone marrow, the blood and inflamed tissue",
 (A + 33, 2): "Antibody production in response to an antigen presented by a tissue macrophage",
 (A + 36, 2): "Increased by parasitic infections and allergy; decreased by an acute allergic reaction",
 (A + 39, 2): "Eosinophil seven hours, basophil three days, and monocyte eight to twelve days",
}

# ---- pool B ----------------------------------------------------------------
# Pool A is 43 questions.
B = 43

FIXES.update({
 (B + 0,  2): "They are far more reproducible between different laboratories than raw percentages are",
 (B + 1,  1): "The total white cell count divided by that cell type's reported percentage",
 (B + 11, 1): "Coagulation, oxygen transport to the tissues, inflammation and rapid wound healing",
 (B + 15, 1): "Trauma, acute hemorrhage, iron deficiency and recent orthopaedic surgery",
 (B + 16, 3): "The proportion of immature platelets, and a marker of platelet consumption",
 (B + 23, 1): "The average amount of hemoglobin in a single red cell, from the hemoglobin concentration and the red cell count",
 (B + 24, 1): "Iron deficiency anemia, thalassemia and other hypochromic red cell states",
 (B + 28, 2): "Hemoglobin in grams per decilitre, multiplied by one hundred, divided by the hematocrit percentage",
 (B + 30, 1): "It is the single most accurate measure of the blood's oxygen carrying capacity that is available anywhere on the panel today",
 (B + 32, 3): "Chronic kidney disease, cancer and dilution by intravenous fluid",
 (B + 33, 1): "Polycythemia vera, chronic hypoxia, dehydration, smoking, trauma and iron deficiency anemia",
})

# ---- pool C ----------------------------------------------------------------
# Pool A is 43, pool B is 37. The morphology pool ran 50% gameable raw, the
# worst of the whole build, because almost every question is "what does it look
# like AND what is it associated with" -- a two-part answer, against one-part
# distractors. Padding gives each wrong choice the same two-part shape.
C = 80

FIXES.update({
 (C + 0,  1): "Cell size, number in the circulation, average lifespan and total hemoglobin content",
 (C + 3,  1): "Central pallor of exactly one third of the cell diameter, with mean corpuscular hemoglobin of twenty-seven to thirty-three picograms per cell, and a normal red cell distribution width",
 (C + 5,  2): "Schistocytes, with mean corpuscular hemoglobin concentration above thirty-six grams per decilitre of packed cells",
 (C + 8,  1): "From mechanical shearing as the cells pass through fibrin strands in vessels",
 (C + 9,  3): "Perfectly round cells that are often smaller than normal with complete loss of central pallor, associated with hereditary spherocytosis",
 (C + 10, 2): "The acanthocyte occurs in chronic renal disease and the echinocyte in chronic liver disease, and neither one has central pallor",
 (C + 13, 1): "Usually macrocytic with prominent central pallor, associated with vitamin B12 or folate deficiency",
 (C + 15, 1): "Under high oxygen tension, when normal adult hemoglobin polymerises, causing brisk intravascular hemolysis",
 (C + 16, 1): "Thin and crescent shaped with a prominent central pallor, and markedly hypochromic throughout",
 (C + 19, 1): "A dark circle within the central area of pallor, from progressive loss of cell membrane, associated with hereditary spherocytosis",
 (C + 21, 1): "A drepanocyte, formed within the circulation under low oxygen tension, associated with sickle cell anemia",
 (C + 22, 1): "Dark purple dots of residual nuclear fragment, singly placed, associated with chronic lead poisoning",
 (C + 24, 1): "They are actively produced by the spleen and released directly into the peripheral circulation",
 (C + 29, 3): "Red cells fragmented into varied shapes, associated with mechanical prosthetic heart valves",
 (C + 30, 2): "The red cell membrane becomes redundant, which allows the cells to stack together into long columns of cells",
 (C + 31, 1): "Stacked chains rather than disorderly clumping, from antibody coating rather than raised serum proteins, associated with multiple myeloma rather than transfusion",
})

# ---- pool D ----------------------------------------------------------------
# Pool A is 43, B is 37, C is 32. Enumerations again -- "which five causes",
# "which three diagnoses does the algorithm give" -- plus the two picture-only
# tables, whose correct answers have to carry a whole table row.
D = 112

FIXES.update({
 (D + 2 , 3): "Determine the mean corpuscular volume, then the red cell distribution width, then the platelet count, and then refer on to hematology today",
 (D + 4 , 2): "Decreased suggests iron deficiency; increased suggests a vitamin B12 deficiency",
 (D + 5 , 3): "A direct antiglobulin test in every single case",
 (D + 11, 2): "Diagnose iron deficiency anemia and replete the iron",
 (D + 16, 1): "The bus is ferritin, which stores the iron; the bus stop is transferrin, which transports it",
 (D + 17, 1): "The home is ferritin, which can be measured directly; the percentage saturation is transferrin, the protein that carries iron in the blood",
 (D + 18, 2): "Iron deficiency, thalassemia, lead poisoning and the anemia of chronic renal disease",
 (D + 20, 1): "Vitamin B12 deficiency, folate deficiency, copper deficiency, and methotrexate or hydroxyurea therapy",
 (D + 22, 1): "Vitamin B12 deficiency and dietary folate deficiency",
 (D + 23, 1): "Into megaloblastic and non-megaloblastic marrow causes",
 (D + 26, 1): "Intrinsic is mechanical stress, immunologic destruction or inflammatory injury from outside the cell; extrinsic is a defect in the red cell itself",
 (D + 31, 3): "Iron deficiency, thalassemia, the anemia of chronic disease, and chronic lead poisoning",
 (D + 34, 1): "Thalassemia is diagnosed, so hemoglobin analysis is performed, especially where the microcytosis is severe, familial, or lifelong in duration",
 (D + 35, 1): "Iron studies in all individuals, with all subsequent testing based on the ferritin and on the transferrin saturation",
 (D + 36, 2): "Obtain a reticulocyte count and a full chemistry panel first",
})
