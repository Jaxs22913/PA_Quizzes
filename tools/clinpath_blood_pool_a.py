# -*- coding: utf-8 -*-
"""Clinical Pathophysiology I, Lecture 10 -- Pathophysiology of Blood Disorders, part A (slides 3-28).

Blood composition and hematopoiesis, leukocytes and their counts, the individual white
cells, B-cell development and clonality, the bone marrow neoplasms, leukemia, the
lymphoid neoplasms and multiple myeloma. Part B carries the red cells, coagulation and
platelets.

SOURCE. "Pathophysiology of Blood Disorders SV Fall 2026.pptx" (51 slides), lectured by
Dr. Matthew Ward on 2026-11-10 (two-part Notability recording, 96 minutes). Every fact is
on a VISIBLE slide (text or picture, each picture viewed at 1920 px); the recording only
weights the split (minutes per topic, clinpath_blood_partition.py) and stars the guide.
His spoken asides that no slide carries (demargination, smudge cells, rouleaux, ferritin,
hepcidin, the hematocrit rule of thumb) are NOT asked.

SPOKEN SLIP, SLIDE KEYED: he twice said "essential thrombocytopenia" for the
myeloproliferative neoplasm the slides print as essential THROMBOCYTHEMIA (slides 18, 26).
The slide wording is keyed; immune thrombocytopenia is a distractor where it fits.

MECHANISM ONLY, per [[clin_path_exam_spec]]. KEYS ARE WRITTEN SHORT ON PURPOSE.
Each distractor carries its misconception as a third option element (WRITER.md rule 5);
numeric and ordered option sets are authored ascending (rule 8). Explanations follow
tools/question_writing/EXPLAIN_DEEP.md.
"""

D = "Pathophysiology of Blood Disorders SV Fall 2026.pptx"

IO_A = "Review the anatomy of the blood cells"
IO_B = "Review the functions of blood cells"
IO_C = "Describe the molecular mechanisms of blood disorders"
IO_D = ("Compare and contrast the etiologies and pathophysiological processes of white blood cell "
        "disorders")
IO_E = "Describe the process of bone marrow neoplasia"
IO_F = "Describe the etiologies and pathophysiological processes of myeloproliferative syndromes"
IO_G = "Describe the etiologies and pathophysiological processes of myelodysplastic syndromes"
IO_H = "Discuss the etiologies and pathophysiological processes of red blood cell disorders"
IO_I = "Describe the etiologies and pathophysiological processes of coagulation disorders"
IO_J = "Discuss the etiologies and pathophysiological processes of platelet disorders"

CD = "competing diagnosis"
WS = "wrong stage or severity"
RF = "ruled out by a stated finding"
CM = "confused mechanism or drug class"
AF = "adjacent fact"
RV = "reversed direction or value"
LB = "common lay belief"


def c(*n):
    return D + ", Slide %d" % n[0] if len(n) == 1 else \
        D + ", Slides " + ", ".join(str(x) for x in n)


def Q(topic, io, slot, q, opts, cite, **kw):
    d = {"topic": topic, "io": io, "slot": slot, "q": q, "opts": opts, "c": kw.pop("key", 0), "cite": cite}
    d.update(kw)
    return d


COMP = "Blood composition and hematopoiesis"
LEUK = "Leukocytes and their counts"
NEUT = "Neutrophils and bands"
MEB = "Monocytes, eosinophils and basophils"
BCEL = "B cells and clonality"
MARR = "Bone marrow neoplasms"
LEUKEMIA = "Leukemia"
LYMPH = "Lymphoid neoplasms"
RISK = "Risk factors and neoplasm lineages"
MYEL = "Multiple myeloma"

QUESTIONS = [

# ------------------------------------------------- blood composition and hematopoiesis (slides 3-5)
Q(COMP, IO_A, "anatomy",
  "Approximately what share of whole blood is plasma?",
  [["35 percent",
    "Too low. Whole blood is about 55 percent plasma and 45 percent formed elements, so 35 percent understates the fluid fraction by roughly 20 points.", RV],
   ["45 percent",
    "This is the share of the formed elements (red cells, white cells and platelets), not of plasma. Whole blood is about 55 percent plasma and 45 percent formed elements; the two figures are easy to swap.", AF],
   ["55 percent",
    "Correct. Whole blood is approximately 55 percent plasma and 45 percent formed elements, and plasma itself is about 90 to 92 percent water carrying electrolytes, nutrients, wastes and proteins."],
   ["65 percent",
    "Too high. Plasma is about 55 percent of whole blood, with the formed elements making up the remaining 45 percent. A 65 percent plasma share would leave the cells at only about a third.", RV]],
  c(3), key=2, ordered=True, core=True),

Q(COMP, IO_A, "anatomy",
  "What is the fluid that remains after blood has clotted?",
  [["Serum",
    "Correct. Serum is the fluid remaining after blood has clotted. Because the clotting proteins were used up in forming the clot, serum is plasma without its clotting factors."],
   ["Plasma",
    "Plasma is the fluid part of unclotted whole blood, about 55 percent of it, and it still carries albumin, globulins and the clotting factors. Once blood clots, the fluid left behind is serum.", AF],
   ["Lymph",
    "Lymph is not what is left in the tube after clotting. The fluid remaining after blood has clotted is serum: plasma that has given up its clotting factors to the clot.", AF],
   ["Interstitial fluid",
    "Interstitial fluid bathes the tissues outside the vessels; it is not produced by clotting a blood sample. The fluid remaining after blood has clotted is serum.", AF]],
  c(3)),

Q(COMP, IO_A, "anatomy",
  "In the healthy adult, where does almost all hematopoiesis occur?",
  [["Axial skeleton, proximal humerus and femur",
    "Correct. Most hematopoiesis occurs in the bone marrow, and in the healthy adult almost all of it is in the axial skeleton plus the proximal humerus and femur."],
   ["Distal radius, tibia and the small hand bones",
    "Wrong end of the limbs. Adult hematopoiesis occurs almost entirely in the axial skeleton and the PROXIMAL humerus and femur; the distal long bones and hand bones are not named as sites of adult blood production.", RV],
   ["The thymus and the peripheral lymph nodes",
    "The thymus is where T-cell precursors develop after leaving the marrow, not where blood cells are produced. Adult hematopoiesis takes place in the marrow of the axial skeleton and proximal humerus and femur.", AF],
   ["The spleen and the liver sinusoids",
    "Neither the spleen nor the liver is given as a site of adult blood production. Most hematopoiesis occurs in the bone marrow, almost all of it in the axial skeleton and proximal humerus and femur.", AF]],
  c(4), core=True),

Q(COMP, IO_A, "anatomy",
  "Which progenitor gives rise to megakaryocytes?",
  [["Myeloid progenitor",
    "Correct. In the simplified lineage model the multipotent stem cell gives myeloid and lymphoid progenitors, and the myeloid progenitor gives erythroid precursors, megakaryocytes (which make platelets), granulocytes and monocytes."],
   ["Lymphoid progenitor",
    "The lymphoid progenitor gives B cells, T cells and natural killer cells, none of which make platelets. Megakaryocytes sit on the myeloid branch with erythroid precursors, granulocytes and monocytes.", AF],
   ["Erythroid precursor",
    "The erythroid precursor is a sister product of the myeloid progenitor, and it matures into erythrocytes. Megakaryocytes come from the myeloid progenitor directly and make platelets.", AF],
   ["Granulocyte precursor",
    "The granulocyte line gives neutrophils, eosinophils and basophils. Megakaryocytes are a separate product of the myeloid progenitor, and they make platelets rather than granulocytes.", AF]],
  c(5)),

# ------------------------------------------------- leukocytes and their counts (slides 6-8)
Q(LEUK, IO_A, "distribution",
  "Which leukocyte normally makes up the largest share of the total white cell count?",
  [["Neutrophils",
    "Correct. Neutrophils are normally 40 to 60 percent of the total leukocyte count, the largest share, ahead of lymphocytes at 20 to 40 percent."],
   ["Lymphocytes",
    "Lymphocytes are the second-largest group, at 20 to 40 percent of the total leukocyte count. Neutrophils, at 40 to 60 percent, make up the largest share.", AF],
   ["Monocytes",
    "Monocytes are a small group, 2 to 8 percent of the total leukocyte count. Neutrophils, at 40 to 60 percent, make up the largest share.", RV],
   ["Eosinophils",
    "Eosinophils are only 1 to 4 percent of the total leukocyte count. Neutrophils, at 40 to 60 percent, make up the largest share; basophils are the smallest at 0.5 to 1 percent.", RV]],
  c(6)),

Q(LEUK, IO_D, "counts",
  "How is a relative white cell count converted to an absolute count?",
  [["Multiply the total white count by the cell's fraction",
    "Correct. The absolute count is the white blood cell count times the relative count expressed as a fraction: a total of 8,000 cells/µL with 25 percent neutrophils gives 2,000 neutrophils/µL."],
   ["Divide the cell's percentage by the total white count",
    "Dividing gives a meaningless small number. The conversion multiplies: total white blood cell count times the relative count as a fraction gives cells per microliter.", RV],
   ["Subtract the lymphocyte count from the total white count",
    "Subtraction would lump every non-lymphocyte together. Each cell's absolute count is found by multiplying the total white blood cell count by that cell's relative fraction.", CM],
   ["Read the cell's percentage straight off the differential",
    "The percentage is the relative count itself, not the absolute one. To get cells per microliter, multiply the total white blood cell count by that percentage as a fraction.", LB]],
  c(7), core=True),

Q(LEUK, IO_D, "counts",
  "Why must both the relative and the absolute white cell counts be read?",
  [["A fall in one type can falsely raise another's percentage",
    "Correct. Percentages are shares of one total, so an absolute decrease in one cell type can show an artificially increased relative count in another. Reading the absolute count shows whether that cell really rose."],
   ["The relative count gives the number of cells per microliter",
    "That describes the absolute count. The relative count is a percentage of the white cells; the absolute count, total white count times that fraction, is the number per microliter.", RV],
   ["Each cell's percentage is measured apart from the others",
    "The percentages are not independent: they are shares of one total, so when one cell type falls in absolute terms another's percentage can rise artificially. That is why both counts must be read.", RV],
   ["The absolute count ignores the total white blood cell count",
    "The absolute count is built from the total: white blood cell count times the cell's fraction. It is the relative percentage alone that can mislead when another cell type falls.", RV]],
  c(7)),

Q(LEUK, IO_D, "terminology",
  "What does agranulocytosis mean?",
  [["Profound neutropenia, below 200 neutrophils/µL",
    "Correct. Agranulocytosis is profound neutropenia, an absolute neutrophil count below 200 cells/µL, lower than even severe neutropenia (below 500 cells/µL)."],
   ["Reduced red cells, white cells and platelets",
    "That is pancytopenia, a fall in all three cell lines. Agranulocytosis is narrower and deeper: profound neutropenia with an absolute neutrophil count below 200 cells/µL.", AF],
   ["More immature neutrophils in the circulation",
    "That is bandemia, the left shift of infection or inflammatory stress. Agranulocytosis is the opposite problem: profound neutropenia, below 200 neutrophils/µL.", RV],
   ["Neutrophils of 500 to 1,000 cells/µL",
    "That range is moderate neutropenia. Agranulocytosis is far lower: an absolute neutrophil count below 200 cells/µL, beyond severe neutropenia (below 500).", WS]],
  c(8, 9)),

Q(LEUK, IO_D, "terminology",
  "Which term names a decreased lymphocyte count?",
  [["Lymphocytopenia",
    "Correct. A decreased lymphocyte count is lymphocytopenia; the suffix for a decrease is -penia, and for an increase -cytosis (lymphocytosis)."],
   ["Lymphocytosis",
    "Lymphocytosis is the increased lymphocyte count, the opposite direction. The decreased count is lymphocytopenia.", RV],
   ["Leukopenia",
    "Leukopenia is a decrease in TOTAL leukocytes, not in lymphocytes specifically. The term for a decreased lymphocyte count is lymphocytopenia.", AF],
   ["Neutropenia",
    "Neutropenia is a decreased absolute neutrophil count, a different cell population. The term for a decreased lymphocyte count is lymphocytopenia.", AF]],
  c(8)),

# ------------------------------------------------- neutrophils and bands (slides 9-10)
Q(NEUT, IO_D, "neutropenia",
  "Which absolute neutrophil count defines severe neutropenia?",
  [["Below 200 cells/µL",
    "That cut-off is agranulocytosis, deeper than severe neutropenia. Severe neutropenia is an absolute neutrophil count below 500 cells/µL.", WS],
   ["Below 500 cells/µL",
    "Correct. Neutropenia is graded by absolute neutrophil count: mild 1,000 to 1,500, moderate 500 to 1,000, severe below 500 cells/µL, and agranulocytosis below 200. Severe neutropenia increases the risk of serious infection."],
   ["500 to 1,000 cells/µL",
    "This range is moderate neutropenia. Severe neutropenia begins below 500 cells/µL.", WS],
   ["1,000 to 1,500 cells/µL",
    "This range is mild neutropenia. Severe neutropenia is an absolute neutrophil count below 500 cells/µL.", WS]],
  c(9), key=1, ordered=True, core=True),

Q(NEUT, IO_D, "neutropenia",
  "How is an absolute neutrophil count of 750 cells/µL graded?",
  [["Agranulocytosis",
    "Agranulocytosis needs a count below 200 cells/µL. At 750 the count sits in the moderate band, 500 to 1,000 cells/µL.", WS],
   ["Severe neutropenia",
    "Severe neutropenia is below 500 cells/µL. A count of 750 is above that line, in the moderate band of 500 to 1,000.", WS],
   ["Moderate neutropenia",
    "Correct. An absolute neutrophil count of 750 cells/µL falls in the moderate band, 500 to 1,000 cells/µL; severe is below 500 and mild is 1,000 to 1,500."],
   ["Mild neutropenia",
    "Mild neutropenia is 1,000 to 1,500 cells/µL. A count of 750 is below that band, in moderate neutropenia (500 to 1,000).", WS]],
  c(9), key=2, ordered=True, core=True),

Q(NEUT, IO_D, "neutrophilia",
  "Which white cell change often accompanies acute bacterial inflammation?",
  [["Neutrophilia",
    "Correct. Neutrophils are the first responders to infection, and neutrophilia often accompanies acute bacterial inflammation."],
   ["Eosinophilia",
    "Eosinophilia points first to allergy (especially asthma), parasites or a drug effect, not to acute bacterial inflammation, which raises the neutrophils.", CD],
   ["Basophilia",
    "Basophils are few on a normal count, and a rise should prompt thought of malignancy. Acute bacterial inflammation is accompanied by neutrophilia.", CD],
   ["Monocytosis",
    "A raised monocyte count points to chronic infections such as tuberculosis, autoimmune disease or chronic myelomonocytic leukemia. Acute bacterial inflammation brings neutrophilia.", WS]],
  c(9, 11, 12)),

Q(NEUT, IO_D, "bands",
  "What is bandemia?",
  [["More immature neutrophils in the blood",
    "Correct. Bandemia is an increase in immature (band) neutrophils, a left shift, which may accompany infection or other inflammatory stress."],
   ["More mature neutrophils in the blood",
    "A rise in mature neutrophils is neutrophilia. Bandemia specifically means more IMMATURE neutrophils, the band forms, in the circulation: a left shift.", WS],
   ["Fewer than 200 neutrophils/µL",
    "That is agranulocytosis, profound neutropenia. Bandemia is an increase, not a loss: more immature band neutrophils in the blood.", RV],
   ["More eosinophils from a drug effect",
    "A drug effect is one of the three things to think of with eosinophilia. Bandemia concerns neutrophils: an increase in their immature band forms.", AF]],
  c(10), core=True),

Q(NEUT, IO_A, "bands",
  "Which appearance identifies a band neutrophil on a smear?",
  [["Kidney-bean nucleus indented over half its width",
    "Correct. A band neutrophil has a kidney-bean nucleus with mature chromatin and no nucleoli, an indentation greater than half the diameter, and secondary granules only."],
   ["Two-lobed nucleus with large red secondary granules",
    "A nucleus with two lobes and red secondary granules is the eosinophil. The band neutrophil has a single kidney-bean nucleus indented more than half its width.", CD],
   ["Round nucleus with scant pale cytoplasm, no granules",
    "A round mature nucleus with clumped chromatin and scant light blue cytoplasm without granules is the lymphocyte. The band has a kidney-bean nucleus indented more than half its width.", CD],
   ["Two to three lobes hidden by dark granules",
    "A mature nucleus of two to three lobes obscured by numerous basophilic granules is the basophil. The band neutrophil has one kidney-bean nucleus indented more than half its width.", CD]],
  c(10, 12, 13, 14)),

Q(NEUT, IO_D, "bands",
  "How does the Sepsis-3 definition describe sepsis?",
  [["Life-threatening organ dysfunction from infection",
    "Correct. Sepsis-3 defines sepsis as infection-associated, life-threatening organ dysfunction; the band count above 10 percent was a historical criterion of the older systemic inflammatory response syndrome definition."],
   ["Immature bands above 10 percent of white cells",
    "A band count above 10 percent was a HISTORICAL criterion of systemic inflammatory response syndrome. Sepsis-3 defines sepsis by infection-associated, life-threatening organ dysfunction.", WS],
   ["Neutrophilia during acute bacterial inflammation",
    "Neutrophilia often accompanies acute bacterial inflammation, but a raised count is not the definition. Sepsis-3 defines sepsis as infection-associated, life-threatening organ dysfunction.", AF],
   ["Neutropenia below 500 cells/µL with infection",
    "Severe neutropenia increases the risk of serious infection, but it does not define sepsis. Sepsis-3 defines sepsis as infection-associated, life-threatening organ dysfunction.", AF]],
  c(10)),

# ------------------------------------------------- monocytes, eosinophils, basophils (slides 11-13)
Q(MEB, IO_B, "monocytes",
  "Which cell does a monocyte become?",
  [["Macrophage",
    "Correct. Monocytes are the precursors to macrophages; in the lineage model the monocyte line of the myeloid progenitor ends in the macrophage, which with the neutrophil is a phagocytic leukocyte."],
   ["Plasma cell",
    "Plasma cells come from activated, selected B cells on the lymphoid branch. A monocyte, a myeloid cell, is the precursor of the macrophage.", AF],
   ["Megakaryocyte",
    "The megakaryocyte is its own product of the myeloid progenitor and makes platelets. The monocyte is the precursor of the macrophage.", AF],
   ["Natural killer cell",
    "Natural killer cells come from the lymphoid progenitor with B and T cells. The monocyte, a myeloid cell, is the precursor of the macrophage.", AF]],
  c(5, 11)),

Q(MEB, IO_D, "monocytes",
  "Which neoplasm can raise the monocyte count?",
  [["Chronic myelomonocytic leukemia",
    "Correct. An increased monocyte count may indicate chronic myelomonocytic leukemia, as well as some autoimmune disorders and chronic infections such as tuberculosis."],
   ["Chronic lymphocytic leukemia",
    "Chronic lymphocytic leukemia is a neoplasm of mature B cells, a lymphoid cell, not a monocyte. The neoplasm named with a high monocyte count is chronic myelomonocytic leukemia.", CD],
   ["Acute lymphoblastic leukemia",
    "Acute lymphoblastic leukemia is a malignancy of precursor B or T cells (lymphoblasts). A raised monocyte count points to chronic myelomonocytic leukemia.", CD],
   ["Plasma-cell myeloma",
    "Plasma-cell myeloma is a malignancy of differentiated antibody-producing B-lineage cells in the marrow. A raised monocyte count points to chronic myelomonocytic leukemia.", CD]],
  c(11)),

Q(MEB, IO_D, "eosinophils",
  "Which three causes should a raised eosinophil count bring to mind first?",
  [["Allergy, parasites and drug effects",
    "Correct. Think of three things with increased eosinophils: allergy (especially asthma), a parasite, or a drug effect. Eosinophilia can rarely be neoplastic or autoimmune."],
   ["Chronic infections such as tuberculosis",
    "Chronic infections such as cytomegalovirus and tuberculosis are listed for a raised MONOCYTE count. For eosinophils the three first thoughts are allergy, parasites and drug effects.", CD],
   ["Acute bacterial inflammation and sepsis",
    "Acute bacterial inflammation goes with neutrophilia, and a band rise with infection. A raised eosinophil count points first to allergy, parasites or a drug effect.", CD],
   ["Marrow malignancy before anything else",
    "Eosinophilia can be neoplastic, but only rarely; malignancy is a consideration if BASOPHILS are elevated. For eosinophils, think first of allergy, parasites and drug effects.", WS]],
  c(12, 13)),

Q(MEB, IO_B, "basophils",
  "Which leukocyte binds IgE (immunoglobulin E)?",
  [["Basophil",
    "Correct. Basophils bind IgE (immunoglobulin E) and take part in the parasite response and allergy; few should be seen on a normal complete blood count, so a rise should prompt thought of malignancy."],
   ["Neutrophil",
    "Neutrophils are phagocytic first responders to infection, not the IgE-binding cell. The leukocyte that binds IgE (immunoglobulin E) is the basophil.", AF],
   ["Monocyte",
    "Monocytes are precursors to macrophages, raised in chronic infection or chronic myelomonocytic leukemia. The IgE (immunoglobulin E)-binding leukocyte is the basophil.", AF],
   ["Natural killer cell",
    "Natural killer cells are lymphocytes from the lymphoid progenitor. The leukocyte that binds IgE (immunoglobulin E) in allergy and the parasite response is the basophil.", AF]],
  c(13), core=True),

# ------------------------------------------------- B cells and clonality (slides 14-17)
Q(BCEL, IO_C, "B cells",
  "In V(D)J recombination, which gene segments do light chains use?",
  [["V and J",
    "Correct. Developing B cells rearrange their immunoglobulin genes in the marrow: heavy chains use V, D and J segments, while light chains use only V and J."],
   ["V, D and J",
    "All three segments are used by HEAVY chains. Light chains have no D segment in their rearrangement; they use V and J only.", AF],
   ["V and D",
    "Light chains do not use a D segment at all; D belongs only to the heavy-chain rearrangement (V, D and J). Light chains join V to J.", CM],
   ["D and J",
    "D and J both appear in the heavy-chain rearrangement, but light chains lack D. Light chains rearrange V with J.", CM]],
  c(15), core=True),

Q(BCEL, IO_C, "B cells",
  "What does somatic hypermutation in germinal centers produce after antigen activation?",
  [["Affinity maturation",
    "Correct. After antigen activation, B cells in germinal centers can undergo somatic hypermutation, and selection of the better-binding cells produces affinity maturation."],
   ["Immunoglobulin gene rearrangement",
    "Rearrangement (V(D)J recombination) happens earlier, as B cells develop in the bone marrow, before antigen. Somatic hypermutation after activation produces affinity maturation.", WS],
   ["Maturation arrest",
    "Maturation arrest is the primary defect of acute leukemia, a block in differentiation from acquired mutations. Somatic hypermutation in germinal centers produces affinity maturation.", CM],
   ["Proof of a malignant clone",
    "A clonal population is not proof of malignancy, and somatic hypermutation is a normal step of the response. Its product in germinal centers is affinity maturation.", LB]],
  c(15)),

Q(BCEL, IO_B, "B cells",
  "Into which cells do activated, selected B cells differentiate?",
  [["Plasma cells or memory B cells",
    "Correct. After antigen activation and selection, B cells differentiate into plasma cells (which produce antibody) or memory B cells."],
   ["T cells or natural killer cells",
    "T cells and natural killer cells are separate lymphoid lines from the lymphoid progenitor, not products of B-cell activation. Selected B cells become plasma cells or memory B cells.", AF],
   ["Lymphoblasts or myeloblasts",
    "Lymphoblasts and myeloblasts are the immature malignant cells of acute leukemia. Normal activated, selected B cells differentiate into plasma cells or memory B cells.", CM],
   ["Monocytes or macrophages",
    "Monocytes and their macrophages are myeloid cells. Activated, selected B cells differentiate into plasma cells or memory B cells.", AF]],
  c(15, 24)),

Q(BCEL, IO_E, "clonality",
  "Why does a clonal result alone not establish malignancy?",
  [["Reactive or premalignant cells can also be clonal",
    "Correct. A clone is a population descended from a common progenitor, and reactive or premalignant populations can also be clonal. The result must be interpreted with morphology, immunophenotype and clinical findings."],
   ["Clonal cells carry many different rearrangements",
    "A clonal lymphoid population shares ONE dominant receptor-gene rearrangement; that is what the test detects. The limit is that reactive or premalignant populations can be clonal too.", RV],
   ["PCR cannot detect receptor-gene rearrangements",
    "PCR (polymerase chain reaction) CAN determine whether a dominant receptor-gene rearrangement is present. The limit is that reactive or premalignant populations can also be clonal.", RV],
   ["Malignant lymphoid cells are usually polyclonal",
    "Lymphoid malignancies often share a dominant receptor-gene rearrangement, so they are clonal, not polyclonal. The limit is that reactive or premalignant populations can be clonal as well.", RV]],
  c(16, 17), core=True),

Q(BCEL, IO_E, "clonality",
  "What is a clone?",
  [["Cells descended from one common progenitor",
    "Correct. A clone is a cell population descended from a common progenitor, which is why lymphoid malignancies often share one dominant receptor-gene rearrangement."],
   ["Cells sharing one function but not one origin",
    "Shared function is not what defines a clone; origin is. A clone is a cell population descended from a common progenitor.", CM],
   ["Any cell population present in high numbers",
    "A high count does not make a population clonal, and clonal populations can be reactive. A clone is defined by descent from a common progenitor.", LB],
   ["Cells that have reached full maturation",
    "Maturity is not the test; immature and mature populations can both be clonal. A clone is a cell population descended from a common progenitor.", CM]],
  c(17)),

# ------------------------------------------------- bone marrow neoplasms (slide 18)
Q(MARR, IO_G, "MDS",
  "Which bone marrow neoplasm is defined by ineffective hematopoiesis with cytopenias and dysplasia?",
  [["Myelodysplastic neoplasm",
    "Correct. Myelodysplastic neoplasms (the World Health Organization's term; myelodysplastic syndromes remains in use elsewhere) show ineffective hematopoiesis with cytopenias and dysplasia, and they can progress to acute myeloid leukemia."],
   ["Myeloproliferative neoplasm",
    "Myeloproliferative neoplasms are clonal PROLIFERATION of myeloid cells: chronic myeloid leukemia, polycythemia vera, essential thrombocythemia and primary myelofibrosis. Ineffective hematopoiesis with dysplasia defines the myelodysplastic neoplasms.", CD],
   ["Acute myeloid leukemia",
    "Acute myeloid leukemia is a myeloid malignancy with impaired differentiation and abnormal blast proliferation, distinct from the dysplastic process. Ineffective hematopoiesis with cytopenias and dysplasia is the myelodysplastic neoplasm.", CD],
   ["Plasma-cell myeloma",
    "Myeloma is a clonal plasma-cell malignancy of the B lineage, not a myeloid neoplasm. Ineffective hematopoiesis with cytopenias and dysplasia defines the myelodysplastic neoplasms.", CD]],
  c(18), core=True),

Q(MARR, IO_F, "MPN",
  "Which process defines the myeloproliferative neoplasms?",
  [["Clonal proliferation of myeloid cells",
    "Correct. Myeloproliferative neoplasms are a clonal proliferation of myeloid cells: chronic myeloid leukemia, polycythemia vera, essential thrombocythemia and primary myelofibrosis."],
   ["Ineffective hematopoiesis with dysplasia",
    "Ineffective hematopoiesis with cytopenias and dysplasia defines the myelodysplastic neoplasms. The myeloproliferative neoplasms are a clonal proliferation of myeloid cells.", CD],
   ["Impaired differentiation with blast growth",
    "Impaired differentiation with abnormal blast proliferation is acute myeloid leukemia. The myeloproliferative neoplasms are a clonal proliferation of myeloid cells.", CD],
   ["Clonal growth of antibody-making B cells",
    "A clonal malignancy of differentiated antibody-producing B-lineage cells is plasma-cell myeloma, a lymphoid neoplasm. The myeloproliferative neoplasms are clonal proliferations of MYELOID cells.", CD]],
  c(18), core=True),

Q(MARR, IO_F, "MPN",
  "Which disorder is one of the myeloproliferative neoplasms?",
  [["Essential thrombocythemia",
    "Correct. The myeloproliferative neoplasms are chronic myeloid leukemia, polycythemia vera, essential thrombocythemia and primary myelofibrosis: clonal proliferations of myeloid cells."],
   ["Immune thrombocytopenia",
    "Immune thrombocytopenia is not among the myeloproliferative neoplasms, which are chronic myeloid leukemia, polycythemia vera, essential thrombocythemia and primary myelofibrosis. Watch the ending: thrombocythemia, not thrombocytopenia.", RV],
   ["Chronic lymphocytic leukemia",
    "Chronic lymphocytic leukemia is a mature B-cell neoplasm, a lymphoid disease. The myeloproliferative neoplasms are myeloid: chronic myeloid leukemia, polycythemia vera, essential thrombocythemia, primary myelofibrosis.", CD],
   ["Hereditary spherocytosis",
    "Hereditary spherocytosis is not among the myeloproliferative neoplasms (chronic myeloid leukemia, polycythemia vera, essential thrombocythemia, primary myelofibrosis). Essential thrombocythemia is the one listed here.", CD]],
  c(18)),

Q(MARR, IO_G, "MDS",
  "Myelodysplastic neoplasms can progress to which malignancy?",
  [["Acute myeloid leukemia",
    "Correct. Myelodysplastic neoplasms can progress to acute myeloid leukemia, although the two are distinct: dysplasia and ineffective hematopoiesis on one side, impaired differentiation with blast proliferation on the other."],
   ["Chronic lymphocytic leukemia",
    "Chronic lymphocytic leukemia is a mature B-cell (lymphoid) neoplasm, not the myeloid malignancy that myelodysplastic neoplasms progress to, which is acute myeloid leukemia.", CD],
   ["Polycythemia vera",
    "Polycythemia vera is a myeloproliferative neoplasm, a separate family of clonal myeloid proliferation. Myelodysplastic neoplasms can progress to acute myeloid leukemia.", CD],
   ["Plasma-cell myeloma",
    "Myeloma is a clonal plasma-cell (B-lineage) malignancy. The progression named for myelodysplastic neoplasms is to acute myeloid leukemia.", CD]],
  c(18)),

# ------------------------------------------------- leukemia (slides 19-22)
Q(LEUKEMIA, IO_E, "pathogenesis",
  "What is the primary pathogenic defect in acute leukemia?",
  [["Maturation arrest",
    "Correct. The primary pathogenic defect in acute leukemia is maturation arrest: acquired mutations in transcription factors block differentiation, and other mutations let the cells proliferate independently of growth factors."],
   ["Ineffective hematopoiesis",
    "Ineffective hematopoiesis with dysplasia defines the myelodysplastic neoplasms, which can progress to acute myeloid leukemia. The primary defect in acute leukemia is maturation arrest.", CD],
   ["Premature red-cell destruction",
    "Shortened red-cell survival is hemolysis, a red-cell disorder. The primary pathogenic defect in acute leukemia is maturation arrest of immature lymphoid or myeloid cells.", CM],
   ["Reactive bone marrow stimulation",
    "A reactive rise is a normal marrow answering a signal, not a malignant defect. Acute leukemia's primary pathogenic defect is maturation arrest from acquired mutations.", CM]],
  c(20), core=True),

Q(LEUKEMIA, IO_C, "pathogenesis",
  "In acute leukemia, acquired mutations in which genes block the differentiation of immature cells?",
  [["Transcription factor genes",
    "Correct. Acquired mutations in transcription factors, which regulate the differentiation of immature lymphoid or myeloid cells, produce the maturation arrest of acute leukemia."],
   ["Immunoglobulin genes",
    "Rearranging immunoglobulin genes is NORMAL B-cell development (V(D)J recombination in the marrow). Maturation arrest comes from acquired mutations in transcription factors.", CM],
   ["Coagulation factor genes",
    "Coagulation-factor genes are not tied to leukemic maturation arrest. In acute leukemia, the block in differentiation comes from acquired mutations in transcription factors.", AF],
   ["Red-cell membrane genes",
    "Red-cell membrane genes are not tied to leukemic maturation arrest. The block in differentiation of immature lymphoid or myeloid cells comes from acquired mutations in transcription factors.", AF]],
  c(20), core=True),

Q(LEUKEMIA, IO_E, "pathogenesis",
  "What are the immature malignant cells of acute leukemia called?",
  [["Lymphoblasts or myeloblasts",
    "Correct. The immature, malignant cells of acute leukemia are called lymphoblasts or myeloblasts depending on the lineage."],
   ["Plasma cells or memory cells",
    "Plasma cells and memory B cells are the normal end products of B-cell activation and selection. Acute leukemia's immature malignant cells are lymphoblasts or myeloblasts.", AF],
   ["Band forms of neutrophils",
    "Bands are immature neutrophils released in infection or inflammatory stress (a left shift), not malignant. Acute leukemia's cells are lymphoblasts or myeloblasts.", CD],
   ["Spherocytes or reticulocytes",
    "Spherocytes and reticulocytes are red-cell forms. The immature malignant cells of acute leukemia are lymphoblasts or myeloblasts, named for their lineage.", AF]],
  c(20)),

Q(LEUKEMIA, IO_E, "counts",
  "In leukemia, what can the peripheral white blood cell count be?",
  [["Low, normal or high",
    "Correct. The peripheral white blood cell count in leukemia may be low, normal or high, because marrow involvement can suppress normal blood-cell production while malignant cells may or may not spill into the blood."],
   ["High, because blasts spill into the blood",
    "Some leukemias do show a high count, even hyperleukocytosis, but a high count is not required. Marrow involvement can suppress normal production, so the count may be low, normal or high.", LB],
   ["Low, because blasts stay in the marrow",
    "Marrow suppression can lower the count, but it is not the only pattern: the peripheral count in leukemia may be low, normal or high.", WS],
   ["Normal until leukostasis develops",
    "Leukostasis is impaired microcirculation with organ injury, and a high count alone does not establish it. The peripheral count in leukemia may be low, normal or high from the start.", CM]],
  c(21, 22), core=True),

Q(LEUKEMIA, IO_E, "counts",
  "How can marrow involvement by leukemia cause cytopenias?",
  [["It suppresses normal blood-cell production",
    "Correct. Marrow involvement can suppress normal blood-cell production and cause cytopenias: insufficient production of normal white cells, red cells and platelets."],
   ["It speeds red-cell removal in the spleen",
    "Accelerated removal by macrophages is extravascular hemolysis, a mechanism of red-cell destruction. Leukemic cytopenias come from suppressed normal blood-cell production in the marrow.", CM],
   ["It expands the plasma volume",
    "A plasma-volume shift changes concentrations without changing cell mass (as dehydration does in reverse). Leukemic cytopenias come from marrow involvement suppressing normal production.", CM],
   ["It consumes platelets in fresh clots",
    "Platelet activation with thrombosis despite a falling count is immune heparin-induced thrombocytopenia. Leukemic cytopenias come from suppression of normal production in the involved marrow.", CM]],
  c(22, 25)),

Q(LEUKEMIA, IO_E, "leukostasis",
  "What is leukostasis?",
  [["Impaired microcirculation with organ injury",
    "Correct. Leukostasis is impaired microcirculation with organ injury, often in the lungs or brain. A high white count alone does not establish it."],
   ["A markedly elevated circulating white count",
    "A markedly elevated circulating count is hyperleukocytosis. Leukostasis is the consequence that a high count alone does not establish: impaired microcirculation with organ injury.", AF],
   ["Blasts arrested at one stage of maturation",
    "Maturation arrest is the primary pathogenic defect of acute leukemia, not leukostasis. Leukostasis is impaired microcirculation with organ injury, often in the lungs or brain.", CM],
   ["A falling count from marrow suppression",
    "Marrow suppression explains cytopenias in leukemia. Leukostasis is a microcirculatory problem: impaired flow with organ injury, often in the lungs or brain.", RV]],
  c(22)),

Q(LEUKEMIA, IO_E, "leukostasis",
  "Which organs does leukostasis often involve?",
  [["Lungs and brain",
    "Correct. Leukostasis is impaired microcirculation with organ injury, often involving the lungs or the brain."],
   ["Liver and spleen",
    "The liver and spleen are not the organs named for leukostasis. Its impaired microcirculation with organ injury often involves the lungs or the brain.", AF],
   ["Kidneys and bones",
    "Kidney injury and osteolytic bone lesions are consequences of multiple myeloma. Leukostasis often involves the lungs or the brain.", AF],
   ["Marrow and thymus",
    "The marrow and thymus are where blood cells and T-cell precursors develop. The microcirculatory organ injury of leukostasis often involves the lungs or the brain.", AF]],
  c(22)),

# ------------------------------------------------- lymphoid neoplasms (slides 23-24)
Q(LYMPH, IO_D, "classification",
  "Which two features classify the lymphoid neoplasms?",
  [["Cell lineage and stage of maturation",
    "Correct. Lymphoid neoplasms are classified by cell lineage and stage of maturation: precursor B or T cells, mature B cells, mature T and natural killer cells, and germinal-center B cells for classic Hodgkin lymphoma."],
   ["Blood count and marrow cellularity",
    "The peripheral count can be low, normal or high in the same disease, so it cannot classify. Lymphoid neoplasms are classified by lineage and stage of maturation.", CM],
   ["Clonality and the white count",
    "Clonality alone does not establish malignancy, and the count varies. Classification uses the cell's lineage and its stage of maturation.", CM],
   ["Patient age and cell size",
    "Neither age nor cell size is the classifier. Lymphoid neoplasms are classified by cell lineage (B, T or natural killer) and stage of maturation (precursor or mature).", LB]],
  c(23), core=True),

Q(LYMPH, IO_D, "classification",
  "Acute lymphoblastic leukemia is a malignancy of which cells?",
  [["Precursor B or T cells",
    "Correct. Acute lymphoblastic leukemia/lymphoma is a malignancy of precursor B or T cells (lymphoblasts): B-ALL/LBL from the B-cell precursor in the marrow, T-ALL/LBL from the T-cell precursor in the thymus."],
   ["Mature B cells",
    "A neoplasm of mature B cells is chronic lymphocytic leukemia/small lymphocytic lymphoma. Acute lymphoblastic leukemia is a malignancy of PRECURSOR B or T cells.", CD],
   ["Germinal-center B cells",
    "Germinal-center B cells give rise to classic Hodgkin lymphoma. Acute lymphoblastic leukemia arises from precursor B or T cells.", CD],
   ["Differentiated plasma cells",
    "Differentiated antibody-producing B-lineage cells give plasma-cell myeloma. Acute lymphoblastic leukemia arises from precursor B or T cells.", CD]],
  c(23, 28), core=True),

Q(LYMPH, IO_D, "classification",
  "Chronic lymphocytic leukemia is a neoplasm of which cells?",
  [["Mature B cells",
    "Correct. Chronic lymphocytic leukemia is a mature B-cell neoplasm, related to small lymphocytic lymphoma (CLL/SLL)."],
   ["Precursor B cells",
    "Precursor B cells (lymphoblasts) give B-cell acute lymphoblastic leukemia/lymphoma. Chronic lymphocytic leukemia is a neoplasm of MATURE B cells.", WS],
   ["Mature T cells",
    "Mature T and natural killer cells give their own distinct neoplasms. Chronic lymphocytic leukemia is a neoplasm of mature B cells.", CD],
   ["Plasma cells",
    "A malignancy of differentiated plasma cells is myeloma. Chronic lymphocytic leukemia arises from mature B cells and is related to small lymphocytic lymphoma.", WS]],
  c(23, 28), core=True),

Q(LYMPH, IO_D, "classification",
  "Classic Hodgkin lymphoma derives from which cells?",
  [["Germinal-center B cells",
    "Correct. Classic Hodgkin lymphoma is derived from germinal-center B cells, the site where activated B cells undergo somatic hypermutation."],
   ["Precursor T cells",
    "Precursor T cells give T-cell acute lymphoblastic leukemia/lymphoma. Classic Hodgkin lymphoma derives from germinal-center B cells.", CD],
   ["Natural killer cells",
    "Mature T and natural killer cells have their own distinct neoplasms. Classic Hodgkin lymphoma derives from germinal-center B cells.", CD],
   ["Myeloid progenitors",
    "Myeloid progenitors give the myeloid neoplasms (myelodysplastic, myeloproliferative, acute myeloid leukemia). Classic Hodgkin lymphoma is a B-cell lymphoma from germinal-center B cells.", CD]],
  c(23)),

Q(LYMPH, IO_A, "development",
  "Where do T-cell precursors develop?",
  [["Thymus",
    "Correct. The lymphoid progenitor branches into the B-cell precursor in the bone marrow and the T-cell precursor in the thymus, the origin of T-cell acute lymphoblastic leukemia/lymphoma."],
   ["Bone marrow",
    "The bone marrow is where the B-cell precursor develops. T-cell precursors develop in the thymus.", AF],
   ["Germinal centers",
    "Germinal centers are where activated B cells undergo somatic hypermutation and affinity maturation. T-cell precursors develop in the thymus.", AF],
   ["Spleen",
    "The spleen is not where T-cell precursors develop. The lymphoid progenitor branches into the B-cell precursor in the bone marrow and the T-cell precursor in the thymus.", AF]],
  c(24)),

# ------------------------------------------------- risk factors and lineages (slides 25-26)
Q(RISK, IO_E, "risk factors",
  "Which exposures are risk factors for hematologic neoplasms?",
  [["Chemical, viral and radiation mutagens",
    "Correct. Risk factors for hematologic neoplasms include exposure to chemical, viral and radiation mutagens, and immunodeficiency disorders."],
   ["Dehydration and high altitude",
    "Dehydration raises the hemoglobin relatively, and hypoxia drives a secondary erythrocytosis; neither is a mutagen. The risk factors for hematologic neoplasms are chemical, viral and radiation mutagens.", CM],
   ["Iron and vitamin B12 deficiency",
    "Iron deficiency causes microcytic anemia and vitamin B12 deficiency megaloblastic anemia; they limit production but are not neoplastic risks. Chemical, viral and radiation mutagens are.", CM],
   ["Heparin exposure and allergy",
    "Heparin can trigger immune heparin-induced thrombocytopenia and allergy raises eosinophils; neither is a mutagen. Risk factors for hematologic neoplasms are chemical, viral and radiation mutagens.", CM]],
  c(25)),

Q(RISK, IO_F, "lineages",
  "On the myeloid branch, which neoplasm arises from the red-cell line?",
  [["Polycythemia vera",
    "Correct. In the division of hematologic neoplasms by lineage, the red-cell line of the myeloid stem cell gives polycythemia vera and erythroid leukemia."],
   ["Essential thrombocythemia",
    "Essential thrombocythemia (and megakaryocytic leukemia) arises from the megakaryocyte line. Polycythemia vera arises from the red-cell line.", AF],
   ["Chronic lymphocytic leukemia",
    "Chronic lymphocytic leukemia is on the lymphoid branch, a mature B-cell neoplasm. On the myeloid branch, the red-cell line gives polycythemia vera.", CD],
   ["Monocytic leukemia",
    "Monocytic leukemia arises from the monocyte line of the myeloid branch. The red-cell line gives polycythemia vera and erythroid leukemia.", AF]],
  c(26), core=True),

# ------------------------------------------------- multiple myeloma (slides 27-28)
Q(MYEL, IO_E, "myeloma",
  "Multiple myeloma is a malignancy of which cells?",
  [["Clonal plasma cells",
    "Correct. Multiple myeloma is a clonal plasma-cell malignancy involving the bone marrow: a malignancy of differentiated, antibody-producing B-lineage cells."],
   ["Precursor B cells",
    "Precursor B cells (lymphoblasts) give B-cell acute lymphoblastic leukemia. Myeloma arises far later in the B pathway, from differentiated plasma cells.", WS],
   ["Mature B cells",
    "Mature B cells give chronic lymphocytic leukemia/small lymphocytic lymphoma. Myeloma is a malignancy of the differentiated end of the line, the plasma cell.", WS],
   ["Myeloid progenitors",
    "Despite the similar name, myeloma is not a myeloid neoplasm. It is a clonal plasma-cell malignancy of the B lineage.", LB]],
  c(27, 28), core=True),

Q(MYEL, IO_E, "myeloma",
  "How does multiple myeloma produce hypercalcemia?",
  [["Altered bone remodeling",
    "Correct. In myeloma, altered bone remodeling can produce osteolytic lesions and hypercalcemia; the monoclonal proteins and marrow infiltration separately cause renal injury, anemia and impaired immunity."],
   ["Renal injury from monoclonal proteins",
    "Monoclonal proteins injure the kidneys, but that is the renal consequence. Hypercalcemia comes from altered bone remodeling, the same process that makes osteolytic lesions.", AF],
   ["Marrow infiltration crowding red cells",
    "Marrow infiltration explains the anemia of myeloma. Hypercalcemia comes from altered bone remodeling with osteolytic lesions.", AF],
   ["Impaired immunity from abnormal antibodies",
    "Impaired immunity is another consequence of the monoclonal proteins and marrow infiltration. Hypercalcemia arises from altered bone remodeling.", AF]],
  c(27)),

Q(MYEL, IO_E, "myeloma",
  "What does active myeloma require?",
  [["A plasma-cell neoplasm plus a defining event",
    "Correct. Active myeloma requires a plasma-cell neoplasm plus a myeloma-defining event. Bone lesions are not required when another defining event is present."],
   ["Osteolytic lesions plus hypercalcemia",
    "Bone lesions are one possible defining event, not a requirement: they are not needed when another defining event is present. Active myeloma needs a plasma-cell neoplasm plus a myeloma-defining event.", RV],
   ["A clonal receptor-gene PCR result",
    "A clonal PCR (polymerase chain reaction) result alone does not establish malignancy. Active myeloma requires a plasma-cell neoplasm plus a myeloma-defining event.", AF],
   ["Monoclonal protein with healthy organs",
    "Active disease is defined by a plasma-cell neoplasm WITH a myeloma-defining event; the renal, anemic and bone consequences are among those events. Monoclonal protein without one does not meet it.", RV]],
  c(27)),

Q(MYEL, IO_E, "myeloma",
  "Which consequences do monoclonal proteins and marrow infiltration cause in myeloma?",
  [["Renal injury, anemia and impaired immunity",
    "Correct. In multiple myeloma, monoclonal proteins and marrow infiltration can cause renal injury, anemia and impaired immunity; altered bone remodeling adds osteolytic lesions and hypercalcemia."],
   ["Leukostasis in the lungs and brain",
    "Leukostasis is impaired microcirculation from a high white-cell burden, often in the lungs or brain. Myeloma's monoclonal proteins and marrow infiltration cause renal injury, anemia and impaired immunity.", CD],
   ["Thrombosis with a falling platelet count",
    "Thrombosis despite a falling platelet count is immune heparin-induced thrombocytopenia. Myeloma's proteins and marrow infiltration cause renal injury, anemia and impaired immunity.", CD],
   ["Raised hematocrit from plasma loss",
    "A hematocrit raised by reduced plasma volume is relative erythrocytosis. Myeloma's marrow infiltration causes anemia, along with renal injury and impaired immunity.", RV]],
  c(27)),
]
