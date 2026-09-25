# Clinical Pathophysiology I, Lecture 3 (Abnormal Cell Growth and Differentiation)
# — pool B. Objectives c, d, e and f: benign against malignant, the routes of
# tumour spread, and the classification of benign and malignant tumours by the
# tissue they originate from.
#
# The naming rule is the spine of objectives e and f, and it is asked several
# ways: MESENCHYMAL origin gives sarcoma when malignant; EPITHELIAL origin gives
# carcinoma. Adenoma/adenocarcinoma for glandular, papilloma for the finger-like
# epithelial projection, squamous cell carcinoma for squamous differentiation.
#
# SCOPE GUARD: pathophysiology only. No management anywhere.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "Abnormal Cell Growth for posting.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOC = "c — Describe neoplastic abnormalities of cell growth"
IOD = "d — Compare and contrast the routes of tumor spread"
IOE = "e — Compare and contrast the different types of benign tumors according to origin"
IOF = "f — Compare and contrast the different types of malignant tumors according to origin"

POOL_B = [
 dict(topic="Benign vs malignant", io=IOC,
   q="How do the borders of benign and malignant tumors differ?",
   opts=[
     ["Benign is well circumscribed and compresses; malignant is ragged and invades",
      "Correct — the benign tumor pushes surrounding tissue aside, the malignant one infiltrates and goes through it."],
     ["Benign has a ragged border and infiltrates surrounding tissue; malignant is well circumscribed and compresses it",
      "That reverses the two: a benign tumor is well circumscribed and compresses surrounding tissue, while a malignant one has a ragged border and infiltrates it."],
     ["Both have well circumscribed borders, and they are distinguished only by growth rate",
      "Only a benign tumor has a well circumscribed border; a malignant tumor's border is ragged and not easily discernible."],
     ["Both have ragged borders, and they are distinguished only by whether they metastasize",
      "Only a malignant tumor has a ragged border; a benign tumor is well circumscribed and often has a fibrous capsule."]],
   c=0, cite=c(13)),

 dict(topic="Benign vs malignant", io=IOC,
   q="Which set of features characterizes a benign tumor?",
   opts=[
     ["Circumscribed, compresses, often encapsulated, well differentiated, no metastasis, slow",
      "Correct — each has a malignant counterpart: a ragged border, infiltration and invasion, various degrees of differentiation, possible metastasis, and rapid growth."],
     ["Ragged border, infiltrates surrounding tissue, no capsule, variably differentiated, may metastasize, grows rapidly",
      "That is the malignant profile; a benign tumor is instead well circumscribed, often has a fibrous capsule, and does not metastasize."],
     ["Autonomous growth, clonal origin, parenchyma and stroma, a single genetic alteration, no stimulus needed",
      "Those describe any neoplasm, benign or malignant; a benign tumor specifically is well circumscribed, compresses surrounding tissue, and does not metastasize."],
     ["Pleomorphism, abnormal nuclei, mitoses, abnormal differentiation, and invasion",
      "Pleomorphism, abnormal nuclei, mitoses and abnormal differentiation mark the malignant end; a benign tumor is usually well differentiated."]],
   c=0, cite=c(13)),

 dict(topic="Benign vs malignant", io=IOC,
   q="How differentiated are malignant tumors?",
   opts=[
     ["Various degrees of differentiation",
      "Correct — malignancy does not mean uniformly poor differentiation. Benign tumors are usually well differentiated."],
     ["Always poorly differentiated",
      "Malignant tumors show various degrees of differentiation, so they are not always poorly differentiated."],
     ["Always anaplastic",
      "Anaplasia, the lack of differentiation, is only the extreme; malignant tumors show various degrees of differentiation."],
     ["Always well differentiated",
      "Usually well differentiated describes benign tumors; malignant tumors show various degrees of differentiation."]],
   c=0, cite=c(13)),

 dict(topic="Hematogenous spread", io=IOD,
   q="Through which vessels does hematogenous tumor spread typically occur?",
   opts=[
     ["Veins, especially the portal vein and the inferior vena cava",
      "Correct — which is why cancers often spread to liver and lungs respectively."],
     ["Arteries, especially the aorta and its major branches",
      "Arteries have thick muscular walls that tumor rarely penetrates; thin-walled veins are the usual route into the circulation."],
     ["Lymphatic vessels at the tumor margin",
      "That is lymphatic spread, which is a separate route."],
     ["Capillaries within the tumor stroma only",
      "The route described reaches distant organs through large veins."]],
   c=0, cite=c(14)),

 dict(topic="Hematogenous spread", io=IOD,
   q="Why do cancers spreading through the portal vein and the inferior vena cava reach the liver and the lungs?",
   opts=[
     ["Because those are the organs each vein drains into",
      "Correct — hematogenous spread is typically venous, so fragments in the portal vein reach the liver and those in the inferior vena cava reach the lungs."],
     ["Because liver and lung tissue are uniquely receptive to any tumor cell",
      "Specific receptors on tumor and endothelial cells do shape metastasis, but the liver and lung pattern follows the venous flow of the portal vein and inferior vena cava."],
     ["Because tumor cells preferentially enter arterial rather than venous blood",
      "Hematogenous tumor spread is typically through veins, especially the portal vein and inferior vena cava, not arteries."],
     ["Because lymphatic drainage from most organs terminates in the liver and lungs",
      "Lymphatic spread follows the natural route of lymphatic drainage from the tumor margin; the liver and lung pattern is venous."]],
   c=0, cite=c(14)),

 dict(topic="Hematogenous spread", io=IOD,
   q="What are the steps of hematogenous spread, in order?",
   opts=[
     ["Cells separate and degrade intercellular tissue with enzymes, invade the vessel, then travel",
      "Correct — multiple tumor fragments travel to other organs, so one organ may end up with several metastatic nodules."],
     ["Tumor cells adhere more tightly to each other; the mass compresses a vessel; a single fragment travels to one other organ",
      "Cells separate rather than adhere, and multiple fragments travel."],
     ["Tumor cells enter lymphatic vessels at the margin and follow the natural route of drainage",
      "Entering lymphatics at the tumor margin and following drainage is lymphatic spread, not spread through blood vessels."],
     ["Tumor invades through an organ surface into a body cavity and settles on the serosal membranes",
      "Invading through an organ surface into a cavity is seeding, which most commonly occurs in the peritoneal cavity."]],
   c=0, cite=c(14)),

 dict(topic="Lymphatic spread", io=IOD,
   q="What is the mechanism of lymphatic spread?",
   opts=[
     ["Cancer spreads into lymphatic vessels at the tumor margin and follows the natural route of lymphatic drainage",
      "Correct — the route is anatomically predictable, which is what makes nodal staging meaningful."],
     ["Cancer cells enter lymphatic vessels at the tumor center and travel against the direction of drainage",
      "Entry is at the margin, and the cells follow drainage rather than opposing it."],
     ["Cancer cells degrade intercellular tissue with enzymes and invade a vein",
      "That is the hematogenous mechanism."],
     ["Cancer invades through an organ surface into a serosal cavity",
      "That is seeding."]],
   c=0, cite=c(14)),

 dict(topic="Seeding", io=IOD,
   q="Which cavities are named for seeding, and how does it happen?",
   opts=[
     ["Pericardial, pleural, peritoneal and joint cavities, and the subarachnoid space",
      "Correct — the mechanism is invasion of tumor through an organ surface into the cavity, most commonly the peritoneal cavity."],
     ["Only the peritoneal cavity, and only by direct extension along the mesentery",
      "Several cavities are named, and the peritoneum is merely the commonest."],
     ["The venous system, by cells separating and degrading intercellular tissue with enzymes",
      "That is hematogenous spread."],
     ["The regional lymph node basins, by following the natural route of drainage",
      "That is lymphatic spread."]],
   c=0, cite=c(15)),

 dict(topic="Seeding", io=IOD,
   q="In which cavity does seeding most commonly occur?",
   opts=[
     ["The peritoneal cavity",
      "Correct — seeding most commonly occurs in the peritoneal cavity; the pericardial and pleural cavities and the subarachnoid space can also be seeded."],
     ["The pericardial cavity",
      "The pericardial cavity can be seeded, but seeding most commonly occurs in the peritoneal cavity."],
     ["The pleural cavity",
      "The pleural cavity can be seeded, but seeding most commonly occurs in the peritoneal cavity."],
     ["The subarachnoid space",
      "Seeding can reach the subarachnoid space, but it most commonly occurs in the peritoneal cavity."]],
   c=0, cite=c(15)),

 dict(topic="Seeding", io=IOD,
   q="How is a body cavity defined for the purposes of seeding?",
   opts=[
     ["By the membranes covering the organs and the cavity wall",
      "Correct — pericardium, pleura and peritoneum cover heart, lungs and abdominal organs respectively, and also line the cavity wall."],
     ["By the bony boundaries that enclose the space",
      "The definition given is the membranes rather than the skeleton."],
     ["By the lymphatic drainage basin that serves the organs within it",
      "Drainage basins define lymphatic spread, not the cavity."],
     ["By the venous return that leaves the organs within it",
      "Venous return is relevant to hematogenous spread."]],
   c=0, cite=c(15)),

 dict(topic="Benign classification", io=IOE,
   q="What are mesenchymal tumors derived from?",
   opts=[
     ["Supportive tissue: connective tissue, adipose tissue, cartilage, smooth and striated muscle, and bone",
      "Correct — the same origin gives sarcomas when the tumor is malignant."],
     ["Epithelial surfaces: skin, gastrointestinal lining, respiratory lining and glandular ducts",
      "That is epithelial origin, which gives adenomas and papillomas when benign."],
     ["Hematopoietic tissue: bone marrow, lymph nodes, spleen and thymus",
      "Hematopoietic tissue is not the mesenchymal category; mesenchymal tumors derive from supportive tissue such as bone and muscle."],
     ["Neural tissue: peripheral nerves, nerve sheaths and the central nervous system",
      "Mesenchymal does not mean neural; mesenchymal tumors derive from supportive tissue such as connective tissue, cartilage, and bone."]],
   c=0, cite=c(16)),

 dict(topic="Benign classification", io=IOE,
   q="What is an adenoma?",
   opts=[
     ["A benign epithelial tumor with a glandular pattern, or from a gland",
      "Correct — it sometimes secretes the hormone or hormones produced by its gland of origin."],
     ["A malignant epithelial tumor with a glandular growth pattern",
      "That is an adenocarcinoma."],
     ["A benign mesenchymal tumor derived from connective tissue",
      "Mesenchymal benign tumors are not called adenomas."],
     ["A benign epithelial tumor producing finger-like projections from a surface",
      "That is a papilloma."]],
   c=0, cite=c(16)),

 dict(topic="Benign classification", io=IOE,
   q="What can an adenoma sometimes do that reflects its origin?",
   opts=[
     ["Secrete the hormone or hormones produced by its gland of origin",
      "Correct — the tumor retains a function of the tissue it came from."],
     ["Invade through the basement membrane into surrounding tissue",
      "Invasion of surrounding tissue is a malignant behavior; an adenoma is a benign epithelial tumor, which compresses surrounding tissue instead."],
     ["Seed the peritoneal cavity through an organ surface",
      "Seeding is invasion of a tumor through an organ surface into a body cavity; an adenoma is benign, so it compresses rather than invades."],
     ["Produce finger-like projections from the epithelial surface",
      "Finger-like projections from an epithelial surface define a papilloma; an adenoma forms a glandular pattern or derives from a gland."]],
   c=0, cite=c(16)),

 dict(topic="Benign classification", io=IOE,
   q="What is a papilloma?",
   opts=[
     ["A tumor with finger-like or warty projections from an epithelial surface",
      "Correct — the projections are visible microscopically or macroscopically."],
     ["A tumor forming a glandular pattern or arising from a gland",
      "A glandular pattern or gland of origin defines an adenoma; a papilloma instead has finger-like or warty projections."],
     ["A malignant tumor arising from supportive, mesenchymal tissue",
      "A malignant tumor of supportive, mesenchymal tissue is a sarcoma; a papilloma is a benign tumor of an epithelial surface."],
     ["A malignant epithelial tumor showing squamous cell differentiation",
      "Malignant epithelium with squamous differentiation is squamous cell carcinoma; a papilloma is a benign epithelial tumor."]],
   c=0, cite=c(17)),

 dict(topic="Malignant classification", io=IOF,
   q="What is a malignant tumor of mesenchymal origin called?",
   opts=[
     ["A sarcoma",
      "Correct — mesenchymal means supportive tissue, and the malignant form is the sarcoma."],
     ["A carcinoma",
      "Carcinoma is the malignant tumor of epithelial origin; malignant tumors of supportive, mesenchymal tissue are sarcomas."],
     ["An adenoma",
      "An adenoma is a benign epithelial tumor with a glandular pattern; the malignant mesenchymal tumor is a sarcoma."],
     ["A papilloma",
      "A papilloma is benign and epithelial, with finger-like projections; the malignant mesenchymal tumor is a sarcoma."]],
   c=0, cite=c(18)),

 dict(topic="Malignant classification", io=IOF,
   q="What is a malignant tumor of epithelial origin called?",
   opts=[
     ["A carcinoma",
      "Correct — with adenocarcinoma for a glandular growth pattern and squamous cell carcinoma for squamous differentiation."],
     ["A sarcoma",
      "A sarcoma arises from supportive, mesenchymal tissue."],
     ["An adenoma",
      "An adenoma is the benign glandular epithelial tumor."],
     ["A papilloma",
      "A papilloma is benign."]],
   c=0, cite=c(18)),

 dict(topic="Malignant classification", io=IOF,
   q="What is a carcinoma with a glandular growth pattern called?",
   opts=[
     ["An adenocarcinoma",
      "Correct — a carcinoma is a malignant epithelial tumor, and one with a glandular growth pattern is an adenocarcinoma."],
     ["An adenoma",
      "An adenoma is the benign epithelial tumor with a glandular pattern; the malignant glandular carcinoma is an adenocarcinoma."],
     ["A squamous cell carcinoma",
      "Squamous cell carcinoma is the carcinoma with squamous cell differentiation, not a glandular growth pattern."],
     ["A sarcoma",
      "A sarcoma is a malignant tumor of mesenchymal, supportive tissue, not an epithelial carcinoma with glandular growth."]],
   c=0, cite=c(18)),

 dict(topic="Malignant classification", io=IOF,
   q="What is a carcinoma showing squamous cell differentiation called?",
   opts=[
     ["Squamous cell carcinoma",
      "Correct — a carcinoma with squamous cell differentiation is a squamous cell carcinoma; one with glandular growth is an adenocarcinoma."],
     ["An adenocarcinoma",
      "Adenocarcinoma is the carcinoma with a glandular growth pattern, not squamous cell differentiation."],
     ["A papilloma",
      "A papilloma is a benign epithelial tumor with finger-like projections; a carcinoma with squamous cell differentiation is a squamous cell carcinoma."],
     ["A sarcoma",
      "A sarcoma arises from mesenchymal, supportive tissue, so it cannot be a carcinoma with squamous differentiation."]],
   c=0, cite=c(18)),

 dict(topic="Naming rule", io=IOF,
   q="A malignant tumor arises from adipose tissue. Which category does it fall into?",
   opts=[
     ["Mesenchymal, so it is a sarcoma",
      "Correct — adipose tissue is listed among the supportive tissues."],
     ["Epithelial, so it is a carcinoma",
      "Adipose tissue is supportive rather than epithelial."],
     ["Epithelial with a glandular pattern, so it is an adenocarcinoma",
      "There is no gland involved in adipose tissue."],
     ["Epithelial with squamous differentiation, so it is a squamous cell carcinoma",
      "Squamous differentiation is an epithelial pattern."]],
   c=0, cite=c(18)),

 dict(topic="Invasion cascade", io=IOD,
   q="Which three hurdles are named for a tumor cell that has penetrated the vasculature?",
   opts=[
     ["Penetration of the vasculature, survival in the circulation, and survival in a new organ",
      "Correct — reaching the bloodstream is only the first of the three."],
     ["Penetration of the vasculature, evasion of apoptosis, and induction of angiogenesis",
      "Evading apoptosis and inducing angiogenesis are steps in becoming a tumor; the hurdles to metastasis are entering the circulation, surviving in it, and surviving at the destination."],
     ["Invasion of the basement membrane, entry into lymphatics, and nodal colonization",
      "That describes the lymphatic route rather than these three hurdles."],
     ["Initiation, promotion, and progression",
      "Those are the steps of chemical carcinogenesis."]],
   c=0, cite=c(26)),

 dict(topic="Metastatic pattern", io=IOD,
   q="What determines where a cancer metastasizes?",
   opts=[
     ["Venous blood flow, tumor and endothelial receptors, and genetic fitness",
      "Correct — metastatic spread is NOT random but determined by these three."],
     ["Chance alone, since circulating tumor cells lodge wherever the vessel first narrows",
      "Metastatic spread is not random; the pattern of venous blood flow, tumor and endothelial cell receptors, and genetic fitness decide where it lands."],
     ["The size of the primary lesion and the duration of the disease",
      "Primary lesion size feeds staging; where a cancer spreads is set by venous blood flow, specific receptors, and genetically determined fitness."],
     ["The histological grade of the tumor and its rate of mitosis",
      "Grade and mitotic rate describe the tumor itself; its destination is set by venous blood flow, specific receptors, and genetic fitness."]],
   c=0, cite=c(27)),

 dict(topic="Metastatic pattern", io=IOD,
   q="Is metastatic spread random?",
   opts=[
     ["No — it is determined by blood flow, receptors, and genetically determined fitness",
      "Correct — metastatic spread is not random but set by venous blood flow, tumor and endothelial receptors, and genetic fitness."],
     ["Yes — circulating cells lodge in whichever capillary bed they reach first",
      "Spread is not random; venous flow, specific receptors on tumor and endothelial cells, and genetic fitness determine it."],
     ["Yes for hematogenous spread, no for lymphatic spread",
      "The nonrandom pattern applies to metastatic spread generally, set by venous flow, receptors, and genetic fitness."],
     ["No — but only because lymphatic drainage is anatomically fixed",
      "Metastatic spread is nonrandom because of venous blood flow, tumor and endothelial receptors, and genetic fitness, not lymphatic anatomy."]],
   c=0, cite=c(27)),

 dict(topic="Invasion", io=IOD,
   q="Besides invasion into adjacent structures, which abnormal interaction is a step in invasion?",
   opts=[
     ["Abnormal cell-substratum interaction",
      "Correct — the cell's relationship with its own supporting matrix changes."],
     ["Abnormal cell-cycle checkpoint control",
      "Checkpoint loss is a gene alteration, as when the viral protein E7 inhibits the retinoblastoma protein; the step alongside invasion is abnormal cell-substratum interaction."],
     ["Abnormal apoptosis of neighbouring stromal cells",
      "Stromal cell apoptosis is not a step; invasion involves abnormal cell-substratum interaction and invasion into adjacent structures."],
     ["Abnormal lymphatic valve function",
      "Lymphatic valves play no part; the step alongside invasion into adjacent structures is abnormal cell-substratum interaction."]],
   c=0, cite=c(24)),

 dict(topic="Benign classification", io=IOE,
   q="A benign tumor arises from cartilage. Which category does it fall into?",
   opts=[
     ["Mesenchymal, since cartilage is supportive tissue",
      "Correct — mesenchymal tumors arise from supportive tissue: connective tissue, adipose tissue, cartilage, smooth and striated muscle, and bone."],
     ["Epithelial, since cartilage lines a surface",
      "Cartilage is supportive tissue rather than a lining epithelium."],
     ["Glandular, so it would be called an adenoma",
      "An adenoma is a benign epithelial tumor with a glandular pattern; cartilage is supportive tissue, so the tumor is mesenchymal."],
     ["Neither, since the classification covers only epithelial tumors",
      "Benign tumors are classified as mesenchymal or epithelial, and cartilage belongs to the mesenchymal, supportive group."]],
   c=0, cite=c(16)),
]
