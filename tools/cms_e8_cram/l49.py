# -*- coding: utf-8 -*-
"""Lecture 49 (Hematologic Malignancies Part I, Gannon) cram topics, condensed from the slides.

CRITERIA: one table per criteria set, classification, cut-off or staging table on the slides (memory
cram_criteria_tables), each with a labeled memory aid. Cells are the slide wording; slide conflicts are note rows
(tools/cms_e8l49_scope.py: s31 "most common leukemia" vs Lecture 50; s62 chronic phase <5% vs "five to 6%" said aloud;
s38 the 10% exception; s63 vs s66 response/remission wording). The picture tables (s10 ECOG, s32 FAB, s64 milestones)
were read from the 1920 px renders.

The gold card leads with what Prof. Gannon flagged out loud (recording 2026-11-18, flags file
cms-l49-heme-malignancies-i-gannon-2026-11-18.flags.md), then the slides' own visual emphasis (bold, underline).
Slide typos corrected: megakaryocytic (s33), lysosomes (s36), allogeneic (s48), pruritus (s52), von Willebrand (s54),
hematopoiesis (s45, s46).
"""
L49C = "#46491c"

CRITERIA = [
{"id": "crit-l49-ecog", "label": "ECOG Performance Status", "color": L49C,
 "tag": "Score &middot; Lecture 49 &middot; slide 10 &#9733;",
 "cols": ["Grade", "Description of patient"], "widths": ["14%", "86%"], "rows": [
  ("<b>0</b>", "Fully active, able to carry on all predisease performance without restriction"),
  ("<b>1</b>", "Restricted in physically strenuous activity but ambulatory and able to carry out work of a light or sedentary nature, e.g., light housework, office work"),
  ("<b>2</b>", "Ambulatory and capable of all self-care but unable to carry out any work activities; <b>up and about more than 50% of waking hours</b>"),
  ("<b>3</b>", "Capable of only limited self-care; <b>confined to bed or chair more than 50% of waking hours</b>"),
  ("<b>4</b>", "Completely disabled; cannot carry on any self-care; totally confined to bed or chair"),
  ("<b>5</b>", "Dead"),
  {"note": "ECOG (Eastern Cooperative Oncology Group; the slide&rsquo;s picture credits &ldquo;Eastern Clinical Oncology Group&rdquo;). Prognosis is often dictated by fitness, particularly in older patients; ECOG is frequently part of clinical trial entry criteria (slide 10)."},
 ], "mnemonic": {"hook": "Count down the day: 0 Normal, 1 Office work, 2 Self-care but no work (up more than half the day), 3 In bed more than half the day, 4 In bed all day, 5 Dead.",
  "key": [["0 Normal", "fully active, no restriction"], ["1 Office", "no strenuous activity, light or sedentary work"],
          ["2 Up &gt;50%", "all self-care, no work, up and about more than 50% of waking hours"],
          ["3 Bed &gt;50%", "limited self-care, bed or chair more than 50% of waking hours"], ["4 Bed all day", "completely disabled"], ["5", "dead"]],
  "breaks": "The 50% line is about waking hours, and it splits 2 (up) from 3 (in bed or chair)."}},

{"id": "crit-l49-blasts", "label": "Blast Thresholds: ALL, AML, MDS and CML", "color": L49C,
 "tag": "Cut-offs &middot; Lecture 49 &middot; slides 25, 38, 47, 62 &#9733;",
 "cols": ["Disease", "Blast cut-off on the slide"], "widths": ["34%", "66%"], "rows": [
  ("<b>Acute lymphoblastic leukemia</b>", "Defined by blast cells of <b>lymphoid</b> origin <b>&ge; 20% in bone marrow</b> (slide 25)"),
  ("<b>Acute myeloid leukemia</b>", "Blast cells of <b>myeloid</b> origin; historically <b>&ge; 20%</b>; new guidelines: certain genetic mutations may allow the diagnosis with only <b>10% or higher</b> (slide 38)"),
  ("<b>Myelodysplastic syndrome</b>", "Higher risk MDS may have blasts but <b>&lt; 20% (otherwise AML)</b> (slide 47)"),
  ("CML chronic phase", "No or few blasts <b>(&lt;5%)</b> (slide 62)"),
  ("CML accelerated phase", "Often <b>10&ndash;19%</b> blasts (slide 62)"),
  ("CML blast phase/crisis", "No number on the slide: <b>behaves as an acute leukemia, usually AML-like</b> (slide 62)"),
  {"note": "Said aloud: &ldquo;20% or more for leukemias, remember that&rdquo;, and the drill &ldquo;10%? No. 15%? No.&rdquo; She also described chronic phase as &ldquo;five to 6% blast&rdquo; and blast phase as &ldquo;greater than 20%&rdquo;: learn the slide wording; the slides give no phase for 5&ndash;9%."},
 ], "mnemonic": {"hook": "Twenty is the line to Leukemia: at 20 it is acute leukemia, under 20 it is still MDS. CML climbs Five, Ten-to-Nineteen, then Blast.",
  "key": [["Twenty", "&ge; 20% marrow blasts = ALL (lymphoid) or AML (myeloid)"], ["Under 20", "higher-risk MDS (blasts &lt; 20%)"],
          ["Ten (AML only)", "certain genetic mutations: AML at &ge; 10%"], ["Five", "CML chronic phase &lt;5%"],
          ["Ten-to-Nineteen", "CML accelerated phase, often 10&ndash;19%"], ["Blast", "CML blast phase behaves like AML"]],
  "breaks": "The blast phase has no number on the slide; the 5&ndash;9% gap has no phase."}},

{"id": "crit-l49-fab", "label": "AML Subtypes: FAB M0&ndash;M7", "color": L49C,
 "tag": "Classification &middot; Lecture 49 &middot; slides 32&ndash;33",
 "cols": ["FAB", "Name", "What the slides add"], "widths": ["12%", "48%", "40%"], "rows": [
  ("M0", "Undifferentiated AML", ""),
  ("M1", "AML with minimal maturation", ""),
  ("M2", "AML with maturation", ""),
  ("<b>M3</b>", "<b>Acute promyelocytic leukemia (APL)</b>", "Discussed separately: DIC, ATRA + arsenic (slide 43)"),
  ("<b>M4</b>", "<b>Acute myelomonocytic leukemia</b>", "More <b>extramedullary involvement</b>; gum hyperplasia (slides 33, 35)"),
  ("<b>M5</b>", "<b>Acute monocytic leukemia</b>", "More <b>extramedullary involvement</b>; gum hyperplasia (slides 33, 35)"),
  ("M6", "Acute erythroid leukemia", "Very rare"),
  ("M7", "Acute megakaryocytic leukemia", "Very rare (slide 33 misspells it &ldquo;myelokaryocytic&rdquo;)"),
  {"note": "FAB = French-American-British: historically ~8 subtypes; the WHO (World Health Organization) now recognizes 18 (slide 33). Out loud: &ldquo;You don&rsquo;t have to know anything about this, really, except that you will hear a lot about APL.&rdquo;"},
 ], "mnemonic": {"hook": "Count the cells as they mature: 0-1-2 = myeloblasts with no, little, then some maturation; 3 = Promyelocyte (APL); 4-5 = Monocytes (the Mouth: gums); 6 = Erythroid; 7 = megaKaryocyte, the last stop.",
  "key": [["0-1-2", "undifferentiated, minimal maturation, with maturation"], ["3 = Promyelocyte", "M3 APL"],
          ["4-5 = Mouth", "M4 myelomonocytic, M5 monocytic: extramedullary, gum hyperplasia"], ["6 = Erythroid", "acute erythroid leukemia, very rare"],
          ["7 = Last stop", "acute megakaryocytic leukemia, very rare"]]}},

{"id": "crit-l49-philadelphia", "label": "Philadelphia Chromosome and Other Translocations", "color": L49C,
 "tag": "Genetics &middot; Lecture 49 &middot; slides 20, 27, 43, 52&ndash;57 &#9733;",
 "cols": ["Disease", "Genetic lesion on the slide", "What it means"], "widths": ["26%", "38%", "36%"], "rows": [
  ("<b>Acute lymphoblastic leukemia (adults)</b>", "<b>BCR-ABL</b>, translocation of chromosomes <b>9 and 22</b> (Philadelphia chromosome): the <b>most common adult mutation</b>", "Ph+ ALL: <b>tyrosine kinase inhibitors + chemotherapy</b>; Ph- ALL: pediatric-like regimens under 40 (slide 27)"),
  ("Acute lymphoblastic leukemia (children)", "<b>Hyperdiploidy</b> (excess copies of a chromosome)", "<b>Favorable</b> prognosis"),
  ("Acute lymphoblastic leukemia (1/3 of all ages)", "No chromosome abnormalities", "Need mutation analysis; relatively favorable"),
  ("<b>Chronic myelogenous leukemia</b>", "<b>Hallmark BCR-ABL</b>: fusion of chromosomes 22 and 9 &rarr; Philadelphia chromosome; BCR attaches to ABL1, a fusion protein enzyme that <b>promotes proliferation and reduces apoptosis</b>", "PCR for BCR-ABL1 <b>confirms the diagnosis</b> and <b>monitors treatment</b>; tyrosine kinase inhibitors (slides 56&ndash;57, 60, 63)"),
  ("<b>Acute promyelocytic leukemia</b>", "Translocation of chromosomes <b>15 and 17</b>: <b>PML-RARA</b> fusion", "ATRA (all-trans-retinoic acid) + arsenic trioxide (slide 43)"),
  ("<b>Polycythemia vera</b>", "<b>JAK2</b> mutation", "Phlebotomy, hydroxyurea (slide 52)"),
  ("Myelofibrosis; essential thrombocythemia", "<b>JAK-STAT pathway</b> mutations", "Myelofibrosis: JAK inhibitors (palliative); essential thrombocythemia: aspirin, hydroxyurea (slides 53&ndash;54)"),
 ], "mnemonic": {"hook": "Philadelphia is a 9-to-22 Bus with two stops: ALL (adults) and CML (the hallmark). APL rides the 15-17 to the Retinoic acid bar; the MPNs ride the JAK.",
  "key": [["9-to-22 Bus", "BCR-ABL, t(9;22), the Philadelphia chromosome"], ["Stop: ALL", "most common adult ALL mutation; TKI + chemotherapy"],
          ["Stop: CML", "the hallmark; PCR confirms and monitors"], ["15-17", "APL, PML-RARA; ATRA + arsenic"], ["JAK", "JAK2 in polycythemia vera; JAK-STAT in myelofibrosis and essential thrombocythemia"]],
  "breaks": "Hyperdiploidy (children, favorable) and the third of ALL with no chromosome change are not in the hook."}},

{"id": "crit-l49-mpn", "label": "The Myeloproliferative Neoplasms Compared", "color": L49C,
 "tag": "Comparison &middot; Lecture 49 &middot; slides 51&ndash;54",
 "cols": ["", "Polycythemia vera", "Myelofibrosis", "Essential thrombocythemia"], "widths": ["16%", "28%", "28%", "28%"], "min_width": "560px", "rows": [
  ("Too much", "<b>Red blood cells</b> (blood viscosity &uarr;)", "<b>All mature myeloid lines</b>, then marrow <b>fibrosis</b>", "<b>Platelets</b>"),
  ("Mutation", "<b>JAK2</b>", "JAK-STAT; elevated cytokines", "JAK-STAT; rarely inherited"),
  ("Presentation", "Fatigue, headaches, blurry vision; <b>classic: pruritus with warm baths or showers</b>", "Fatigue; <b>splenomegaly</b> symptoms (pain, early satiety, bloating); night sweats, fever, weight loss", "<b>Mostly asymptomatic</b>; clotting (headaches, fatigue, paresthesias, vision changes) or bleeding (acquired von Willebrand factor)"),
  ("Complications", "Thrombosis, splenomegaly, bleeding", "Severe splenomegaly, portal hypertension, bleeding, secondary AML", "Clotting: CVA (stroke), MI"),
  ("Treatment", "<b>Phlebotomy</b>, hydroxyurea", "JAK inhibitors (<b>palliative</b>)", "<b>Aspirin</b>, hydroxyurea"),
  ("Prognosis", "Excellent: ~14 years; leukemic transformation ~5%", "<b>Most aggressive</b>: low risk 10&ndash;15 years, high risk &lt; 2 years", "Excellent: normal life span"),
  ("Also", "Hematologist; stop smoking", "Hematologist at diagnosis", "Hematologist; stop smoking"),
 ], "mnemonic": {"hook": "Red, Scar, Plate: Polycythemia makes Red cells and Itches in the shower; Myelofibrosis Scars the marrow and swells the spleen; Thrombocythemia piles up Platelets that clot (or bleed).",
  "key": [["Red + Itch", "polycythemia vera: red cells, JAK2, pruritus after warm bath; phlebotomy"], ["Scar", "myelofibrosis: fibrosis, splenomegaly, most aggressive; JAK inhibitors palliative"],
          ["Plate", "essential thrombocythemia: platelets, clot (CVA, MI) or bleed; aspirin, hydroxyurea"]],
  "breaks": "Hydroxyurea is in both polycythemia vera and essential thrombocythemia; the survival numbers are not in the hook."}},

{"id": "crit-l49-cml-phases", "label": "CML Phases", "color": L49C,
 "tag": "Staging &middot; Lecture 49 &middot; slide 62",
 "cols": ["Phase", "Blasts", "Features", "Share"], "widths": ["22%", "18%", "44%", "16%"], "rows": [
  ("<b>Chronic (stable)</b>", "<b>No or few (&lt;5%)</b>", "Early proliferative phase; <b>excellent prognosis</b>", "<b>85&ndash;90%</b>"),
  ("<b>Accelerated</b>", "<b>Often 10&ndash;19%</b>", "May have dysplastic granulocytes and fibrosis; frequently <b>significant splenomegaly</b>", "~4&ndash;5%"),
  ("<b>Blast phase/crisis</b>", "No number on the slide", "<b>Behaves as an acute leukemia, usually AML-like</b>; unique chromosomal and mutational abnormalities; <b>AML-like regimens</b>, <b>poor responses to TKIs</b>", "~1&ndash;2%"),
  {"note": "Advanced CML (accelerated or blast phase) &ldquo;has different considerations&rdquo; (slide 63) and a median survival &lt; 12 months (slide 65). Out loud she said chronic phase is &ldquo;five to 6% blast&rdquo; and blast phase &ldquo;greater than 20%&rdquo;: learn the slide wording."},
 ], "mnemonic": {"hook": "Most stay Calm: Chronic is under 5 (and 85&ndash;90% of patients); Accelerated is Ten-to-nineteen with a big spleen; Blast crisis acts like AML and shrugs off the TKI.",
  "key": [["Calm", "chronic phase, &lt;5% blasts, 85&ndash;90%, excellent prognosis"], ["Ten-to-nineteen", "accelerated, often 10&ndash;19%, splenomegaly"],
          ["Acts like AML", "blast phase: AML-like regimens, poor TKI response, 1&ndash;2%"]]}},

{"id": "crit-l49-cml-milestones", "label": "CML Response Milestones (BCR-ABL1)", "color": L49C,
 "tag": "Cut-offs &middot; Lecture 49 &middot; slide 64 &#9733;",
 "cols": ["Milestone", "Failure", "Warning", "Optimal", "TFR"], "widths": ["16%", "20%", "22%", "22%", "20%"], "min_width": "520px", "rows": [
  ("<b>3 months</b>", "N.A.", "&gt; 10%", "<b>&lt; 10%</b>", "N.A."),
  ("<b>6 months</b>", "&gt; 10%", "1&ndash;10%", "<b>&lt; 1%</b>", "N.A."),
  ("<b>12 months</b>", "&gt; 1%", "0.1&ndash;1%", "<b>&lt; 0.1%</b>", "N.A."),
  ("<b>&gt; 18 months</b>", "&gt; 1%", "0.1&ndash;1%", "<b>&lt; 0.1%</b>", "<b>&lt; 0.01%</b>"),
  {"note": "Every cell is the BCR-ABL1 level. TFR = treatment-free remission. Slide 63: major molecular response (MMR) for 2 years may allow stopping TKIs, but 50% recur; slide 66 words it &ldquo;sustained major molecular remission x 2 years&rdquo;. Out loud: the level is checked about every 3 months, and warning or failure means a change of TKI or a resistance-mutation test."},
 ], "mnemonic": {"hook": "Ten, One, Point-one: the optimal level drops one log at each milestone (3, 6, 12 months), and Point-oh-one at 18 earns time off (TFR).",
  "key": [["Ten", "3 months: optimal &lt; 10%"], ["One", "6 months: optimal &lt; 1%"], ["Point-one", "12 and &gt; 18 months: optimal &lt; 0.1%"],
          ["Point-oh-one", "&gt; 18 months: &lt; 0.01% = treatment-free remission range"]],
  "breaks": "Failure lags one step behind optimal (&gt; 10% at 6 months, &gt; 1% at 12 and &gt; 18); there is no failure value at 3 months."}},
]

TOPICS = [
{"id": "l49-emph", "label": "★ Emphasized — Hematologic Malignancies Part I", "color": "#b8860b", "rows": [
  ["What this card is", "First what <b>Prof. Gannon flagged out loud</b> (recording, 18 November); then the <b>slides&rsquo; own emphasis</b> (bold, underline). She gave few explicit cues and no &ldquo;on the exam&rdquo; line."],
  ["★ Said: Auer rods", "&ldquo;Highlight, star, underline ... Auer rods ... <b>pathognomonic for AML</b>&rdquo; (slides 31, 36). Auer rods are fused lysosomes; they confirm a myeloid leukemia."],
  ["★ Said: 20% blasts", "&ldquo;Write this down ... <b>20% or greater blast in the bone marrow</b>&rdquo; diagnoses leukemia (slides 25, 38); MDS blasts stay &lt; 20% (slide 47)."],
  ["★ Said: BCR-ABL in ALL", "&ldquo;Star, highlight, underline ... ALL is associated with this <b>BCR-ABL</b> mutation ... chromosome nine and 22&rdquo; (slide 20)."],
  ["★ Said: Reed-Sternberg", "&ldquo;If you&rsquo;re ever taking a test and you see a <b>Reed Sternberg cell</b> ... <b>Hodgkin lymphoma</b>&rdquo; (slide 15)."],
  ["★ Said: B symptoms", "&ldquo;Make sure you&rsquo;re writing down what are B symptoms&rdquo;: <b>fevers, night sweats, weight loss</b> (slides 15, 22)."],
  ["★ Said: hematopoiesis", "&ldquo;Ingrain this in your brains&rdquo;: stem cell &rarr; <b>myeloid</b> (megakaryocyte/platelets, eosinophil, basophil, erythrocytes, monocyte, neutrophil) and <b>lymphoid</b> (T, B, NK; B &rarr; plasma cell) (slide 5)."],
  ["★ Said: ALL", "<b>Bimodal</b>: children, then older adults (slide 18); <b>lumbar puncture</b>, &ldquo;the big one&rdquo;: CNS leukemia is common in ALL (slides 23, 25)."],
  ["★ Said: APL", "&ldquo;<b>Bleeding, DIC, coagulopathy</b>, and that it does not need chemotherapy. <b>ATRA and arsenic</b>&rdquo; (slide 43)."],
  ["★ Said: tests", "<b>Bone marrow biopsy and flow cytometry</b> = &ldquo;your backbone testing&rdquo; (slide 36). <b>JAK2</b> in polycythemia vera, &ldquo;you may come across this on your testing&rdquo; (slide 52). ECOG matters for treatment (slide 10)."],
  ["★ Said: CML milestones", "Optimal BCR-ABL1 <b>&lt; 10% at 3 months, &lt; 1% at 6, &lt; 0.1% at 12</b> (slide 64)."],
  ["Played down", "FAB subtypes except APL (slide 33); secondary-AML subgroup modifiers (slide 38); protocol pictures (slides 26, 39, a joke); flow markers; TKI side effects (slide 63)."],
  ["Slides underline", "Bone marrow biopsy and/or flow cytometry (slides 11, 23, 36); <b>most common malignancy under 15</b> = ALL (slide 18); <b>Auer rods confirm myeloid etiology</b> (slide 36); <b>splenomegaly</b> in CML (slide 59); <b>bone marrow biopsy and PCR for BCR-ABL1</b> (slide 60)."],
  ["Slides bold", "Ph+ ALL = <b>TKI + chemotherapy</b> (slide 27); <b>secondary AML</b> = poor outcome (slides 32, 38); <b>gum involvement</b> in M4/M5 (slide 35); fit 7+3 vs unfit low-intensity, <b>allogeneic transplant IF remission</b> (slide 40); MDS: <b>ESA for low risk + anemia</b>, <b>only cure = allogeneic transplant</b> (slide 48); PV <b>pruritus with warm baths</b> (slide 52); ET <b>aspirin, hydroxyurea</b> (slide 54); CML <b>now largely chronic</b> (slide 56)."],
]},
{"id": "l49-overview", "label": "Hematopoiesis &amp; the Malignancy Families", "color": L49C, "rows": [
  ["Clonality", "One <b>oncogenic mutation in a single somatic cell</b> gives a clonal advantage; the clone expands and gathers more alterations (slide 6)."],
  ["Definition", "Cancers of blood-forming tissues or the lymphatic system from a <b>monoclonal</b> hematologic clone; leukemias, lymphomas, plasma cell disorders; <b>cell of origin sets the type</b> (lymphoid or myeloid) (slide 7)."],
  ["Acute vs chronic", "<b>Acute</b> = immature progenitor white cells, rapid proliferation; <b>chronic</b> = mature malignant white cells. Crowding causes anemia, thrombocytopenia, most commonly leukocytosis (slide 14)."],
  ["Lymphoma", "Lymphoid tissue (nodes, spleen, thymus); &gt;100 subtypes; <b>non-Hodgkin 90%</b> (B and T cell), <b>Hodgkin 10%</b> (few <b>Reed-Sternberg cells</b> among immune cells); lymphadenopathy, night sweats, weight loss, fevers (slide 15)."],
  ["Myeloma", "Plasma cells (terminally differentiated B cells); one monoclonal antibody, the <b>M protein</b>; <b>CRAB</b>: hypercalcemia, renal dysfunction, anemia, bone pain; infections (slide 16)."],
  ["Epidemiology", "9.4% of new United States cancers (2025); ~1.8 million living with one; 9.1% of cancer deaths (slide 8)."],
  ["Risk factors", "Radiation, <b>benzene</b>; family history, <b>trisomies</b>; autoimmune disorders; <b>older age</b> (exceptions: ALL, some lymphomas) (slide 9)."],
  ["Presentation", "Non-specific: fatigue (anemia), bleeding (thrombocytopenia), swollen nodes (lymphoma), bone pain (myeloma); incidental cytopenias or high protein (myeloma). <b>Almost all need bone marrow biopsy and/or flow cytometry</b> (slide 11)."],
  ["Transplant", "HSCT = bone marrow transplant, after high-dose chemotherapy +/- radiation. <b>Allogeneic = donor</b> cells; <b>autologous = own</b> cells (&ldquo;stem cell rescue&rdquo;) (slide 12)."],
]},
{"id": "l49-all", "label": "Acute Lymphoblastic Leukemia (ALL)", "color": "#2f5d6b", "rows": [
  ["What", "Lymphoid progenitor/stem cell leukemia; very immature, rapidly proliferating; B-cell precursor (leukemic, marrow) or T-cell (rarer, lymphoma-like, <b>thymus</b>, mediastinal mass); lymphoblastic lymphoma subtype (slides 18&ndash;19, 22)."],
  ["Who", "<b>Bimodal</b>: most common malignancy <b>under 15</b> (5-year survival &gt;90%); adult peak ~50, poor over 40. Slide 21: children under 5, adults over 50; male (slides 18, 21)."],
  ["Risk factors", "Radiation (atomic bomb, prior treatment); benzene, chemotherapy; <b>EBV, HTLV-1</b> (Caribbean); <b>Down syndrome, Fanconi anemia</b>; male (slide 21)."],
  ["Genetics", "Children: <b>hyperdiploidy</b>, favorable. Adults: <b>BCR-ABL t(9;22)</b> (Philadelphia). 1/3: no chromosome change, relatively favorable (slide 20)."],
  ["Signs", "Anemia, bleeding (petechiae, purpura), infections, <b>B symptoms</b>, &gt;50% lymphadenopathy/hepatomegaly/splenomegaly, <b>bone or joint pain</b>. White count often <b>&gt; 30K</b> (30% neutropenic) (slide 22)."],
  ["Diagnose", "<b>Flow cytometry</b> (B or T) + <b>bone marrow biopsy</b>; imaging, labs, <b>lumbar puncture</b>. <b>Lymphoid blasts &ge; 20%</b> in marrow; diffuse marrow and blood involvement (aggressive lymphomas spare the marrow); <b>CNS involvement = adverse</b> (slides 23, 25)."],
  ["Differential", "AML, CLL, aggressive lymphomas, hairy cell leukemia; lymphoblastic lymphoma (treated alike); atypical lymphocytosis of <b>mononucleosis, pertussis</b> (not clonal on flow) (slide 24)."],
  ["Treat", "<b>Ph-</b>: pediatric-like regimens under 40 (induction, consolidation, maintenance). <b>Ph+: TKI + chemotherapy</b>. Allogeneic transplant for adverse risk or relapse (slide 27)."],
  ["Outcome", "Under 15: ~90% five-year survival, 2&ndash;5 years of chemotherapy; adults ~40%. Hematologist/oncologist, admission, life-long surveillance, trials (slides 28&ndash;29)."],
]},
{"id": "l49-aml", "label": "Acute Myeloid Leukemia (AML) &amp; APL", "color": "#7a3b2e", "rows": [
  ["What", "Myeloid progenitor/stem cell leukemia; <b>Auer rods pathognomonic</b>; mostly <b>over 60</b>; unusual in children outside neonates (slide 31)."],
  ["Risk groups", "Favorable, intermediate, poor. <b>Secondary AML</b> (from MDS, MPN, or after other cancer therapy) = poor outcomes (slides 32, 38)."],
  ["Risk factors", "Prior <b>high-dose</b> radiation; benzene, <b>petroleum</b>, <b>alkylators</b>; <b>HIV</b>; Down syndrome, Fanconi anemia; <b>over 60</b>; male (slide 34)."],
  ["Signs", "Anemia, bleeding, infections, B symptoms; <b>M4/M5: gum hyperplasia</b>, extramedullary disease. White count usually high; &gt; 200K rare; <b>&gt; 100K = emergent leukapheresis</b> (slides 33, 35)."],
  ["Diagnose", "<b>Flow cytometry</b> (vs ALL) + <b>bone marrow biopsy</b>; Auer rods confirm myeloid; mutation sequencing. <b>Myeloid blasts &ge; 20%</b> (10% with certain mutations) (slides 36, 38)."],
  ["Differential", "ALL, CML, MDS, myeloproliferative disorders; pancytopenia of infection, aplastic anemia, nutritional deficiency, drugs (slide 37)."],
  ["Treat", "<b>Fit: 7+3</b> (cytarabine + anthracycline). <b>Unfit: hypomethylating agents +/- venetoclax</b> (BCL-2 inhibitor). <b>Allogeneic transplant</b> for intermediate/high risk <b>once in remission</b> (slide 40)."],
  ["Outcome", "Relapse common; 48% at 1 year, 25&ndash;30% at 5; favorable risk ~2/3; <b>over 70: 5%</b>; adverse or secondary ~10% (slide 41)."],
  ["APL (M3)", "Arrest at the <b>promyelocyte</b>; <b>t(15;17) PML-RARA</b>; <b>DIC and bleeding</b>, high early mortality; <b>arsenic trioxide + ATRA</b>; &gt;90% cure if the presentation is survived (slide 43)."],
]},
{"id": "l49-mds", "label": "Myelodysplastic Syndrome (MDS)", "color": "#5a3a5e", "rows": [
  ["What", "Myeloid malignancies defined by <b>dysplasia</b> (abnormal-appearing myeloid cells); from <b>clonal hematopoiesis</b>; <b>hypercellular marrow, cells not functional</b> (slides 45&ndash;46)."],
  ["Who", "Older (<b>median 70</b>), <b>men</b>; often idiopathic; sometimes prior chemotherapy or radiation (slide 46)."],
  ["Picture", "Cytopenias, <b>most often anemia</b>; many asymptomatic, found incidentally; abnormal neutrophils; multinucleated red cells; higher risk: <b>blasts &lt; 20%</b> (otherwise AML) (slide 47)."],
  ["Treat", "<b>Low risk + anemia: ESA</b> (erythropoiesis-stimulating agents) + transfusions; neutropenia: myeloid growth factors (careful); higher risk: chemotherapy or hypomethylating agents; <b>only cure = allogeneic transplant</b> (slide 48)."],
  ["Outcome", "Lower risk: median survival &gt; 5 years. Very high risk: <b>median overall survival 9 months</b>, &gt; 80% AML within 5 years. Low risk goal: quality of life (slide 49)."],
]},
{"id": "l49-mpn", "label": "Myeloproliferative Neoplasms: PV, MF, ET", "color": "#4a5a2a", "rows": [
  ["What", "Rare myeloid malignancies with atypical proliferation of <b>mature</b> cell lines (slide 51)."],
  ["Polycythemia vera", "<b>JAK2</b>; red cells &uarr;, viscosity &uarr;; fatigue, headaches, blurry vision; <b>pruritus with warm baths or showers</b>; thrombosis, splenomegaly, bleeding; <b>phlebotomy</b>, hydroxyurea; ~14 years, ~5% leukemic; hematologist, stop smoking (slide 52)."],
  ["Myelofibrosis", "JAK-STAT, cytokines &uarr;, all myeloid lines &uarr;, then <b>marrow fibrosis</b>; <b>splenomegaly</b> (pain, early satiety, bloating), night sweats, fever, weight loss; <b>most aggressive MPN</b>; portal hypertension, secondary AML; <b>JAK inhibitors, palliative</b>; 10&ndash;15 years low risk, &lt; 2 high risk (slide 53)."],
  ["Essential thrombocythemia", "JAK-STAT; platelets &uarr;; mostly asymptomatic; clotting (headache, paresthesias, vision changes) or bleeding from <b>acquired von Willebrand factor</b> loss; CVA, MI; <b>aspirin, hydroxyurea</b>; normal life span; stop smoking (slide 54)."],
]},
{"id": "l49-cml", "label": "Chronic Myelogenous Leukemia (CML)", "color": "#5e4123", "rows": [
  ["What", "Stem cell leukemia making excess <b>granulocytes</b> (more mature than blasts); historically to acute leukemia in ~4&ndash;6 years; <b>BCR-ABL / Philadelphia chromosome</b> hallmark; now largely chronic (slide 56)."],
  ["Mechanism", "t(9;22): <b>BCR attaches to ABL1</b>; the fusion enzyme drives proliferation, blocks apoptosis: the cell &ldquo;can&rsquo;t turn off&rdquo; (slide 57)."],
  ["Who", "15&ndash;20% of leukemias; <b>median age 45&ndash;55</b>; slightly more men; radiation bomb victims; no other risk factors (slide 58)."],
  ["Signs", "<b>~50% asymptomatic</b> (leukocytosis on a blood count); fatigue; <b>splenomegaly</b> (abdominal swelling); B symptoms. <b>White count often &gt; 100K</b> (to 500K), <b>platelets high</b>, anemia, very low blasts (slide 59)."],
  ["Diagnose", "<b>Bone marrow biopsy + PCR for BCR-ABL1</b>; PCR in a patient with marked granulocytosis confirms and later monitors; marrow: granulocytic proliferation, myelocytes (slide 60)."],
  ["Differential", "Myelofibrosis (CML: normal red cell shape, normal hematocrit; BCR/ABL1+). <b>Reactive leukocytosis</b>: no splenomegaly, white count usually <b>&lt; 50K</b>, BCR/ABL1 negative (slide 61)."],
  ["Treat", "<b>Tyrosine kinase inhibitors</b> (6 agents) for chronic phase; stop after MMR for 2 years (50% recur, most recapture); allogeneic transplant for young healthy patients with TKI resistance or advanced disease (slides 63, 65)."],
  ["Outcome", "Most live normal lives on TKIs; accelerated or blast phase median survival <b>&lt; 12 months</b>; hematologist; treatment for life unless sustained remission x 2 years; trials for advanced phase (slides 65&ndash;66)."],
]},
{"id": "l49-ages", "label": "Ages &amp; Populations (Lecture 49)", "color": L49C, "rows": [
  ["Children", "ALL: most common malignancy under 15, peak under 5, hyperdiploidy favorable, ~90% survive; AML unusual outside neonates (slides 18, 20&ndash;21, 28, 31)."],
  ["Adults", "ALL second peak ~50, poor over 40; CML median 45&ndash;55 (slides 18, 58)."],
  ["Elderly", "Fitness (ECOG) drives prognosis; AML over 60, unfit &rarr; low-intensity therapy, over 70 only 5% at 5 years; MDS median 70 (slides 10, 31, 40&ndash;41, 46)."],
]},
]
