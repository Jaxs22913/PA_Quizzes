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
   q="How do the borders of benign and malignant tumours differ?",
   opts=[
     ["Benign is well circumscribed and compresses; malignant is ragged and invades",
      "Correct — the benign tumour pushes surrounding tissue aside, the malignant one infiltrates and goes through it."],
     ["Benign has a ragged border and infiltrates surrounding tissue; malignant is well circumscribed and compresses it",
      "This reverses the two descriptions entirely."],
     ["Both have well circumscribed borders, and they are distinguished only by growth rate",
      "Border character is one of the listed differences, so growth rate is not the only one."],
     ["Both have ragged borders, and they are distinguished only by whether they metastasize",
      "The benign tumour is described as well circumscribed."]],
   c=0, cite=c(13)),

 dict(topic="Benign vs malignant", io=IOC,
   q="Which five features does the deck list for a benign tumour?",
   opts=[
     ["Circumscribed, compresses, often encapsulated, well differentiated, no metastasis, slow",
      "Correct — each has a malignant counterpart on the same slide: ragged border, infiltrates and invades, various degrees of differentiation, may metastasize, grows rapidly."],
     ["Ragged border, infiltrates surrounding tissue, no capsule, variably differentiated, may metastasize, grows rapidly",
      "That is the malignant list, which is the contrast being drawn."],
     ["Autonomous growth, clonal origin, parenchyma and stroma, a single genetic alteration, no stimulus needed",
      "Those are the features of a neoplasm generally, benign or malignant."],
     ["Pleomorphism, abnormal nuclei, mitoses, abnormal differentiation, and invasion",
      "Those are the histological features that move a tumour towards malignancy."]],
   c=0, cite=c(13)),

 dict(topic="Benign vs malignant", io=IOC,
   q="What does the deck say about differentiation in malignant tumours?",
   opts=[
     ["Various degrees of differentiation",
      "Correct — malignancy does not mean uniformly poor differentiation. Benign tumours are usually well differentiated."],
     ["Always poorly differentiated",
      "The deck describes a range rather than a single grade."],
     ["Always anaplastic",
      "Anaplasia is the extreme end, not the rule."],
     ["Always well differentiated",
      "That is what the deck says of benign tumours."]],
   c=0, cite=c(13)),

 dict(topic="Haematogenous spread", io=IOD,
   q="Through which vessels does haematogenous tumour spread typically occur?",
   opts=[
     ["Veins, especially the portal vein and the inferior vena cava",
      "Correct — which is why cancers often spread to liver and lungs respectively."],
     ["Arteries, especially the aorta and its major branches",
      "The deck names the venous side rather than the arterial."],
     ["Lymphatic vessels at the tumour margin",
      "That is lymphatic spread, which is a separate route."],
     ["Capillaries within the tumour stroma only",
      "The route described reaches distant organs through large veins."]],
   c=0, cite=c(14)),

 dict(topic="Haematogenous spread", io=IOD,
   q="Why do cancers spreading through the portal vein and the inferior vena cava reach the liver and the lungs?",
   opts=[
     ["Because those are the organs each vein drains into",
      "Correct — the portal vein delivers to the liver, the inferior vena cava to the right heart and then the lungs."],
     ["Because liver and lung tissue are uniquely receptive to any tumour cell",
      "Receptivity matters, but the deck explains this pair by the venous anatomy."],
     ["Because tumour cells preferentially enter arterial rather than venous blood",
      "The route described is venous."],
     ["Because lymphatic drainage from most organs terminates in the liver and lungs",
      "This is haematogenous rather than lymphatic spread."]],
   c=0, cite=c(14)),

 dict(topic="Haematogenous spread", io=IOD,
   q="What are the steps of haematogenous spread, in order?",
   opts=[
     ["Cells separate and degrade intercellular tissue with enzymes, invade the vessel, then travel",
      "Correct — multiple tumour fragments travel to other organs, so one organ may end up with several metastatic nodules."],
     ["Tumour cells adhere more tightly to each other; the mass compresses a vessel; a single fragment travels to one other organ",
      "Cells separate rather than adhere, and multiple fragments travel."],
     ["Tumour cells enter lymphatic vessels at the margin and follow the natural route of drainage",
      "That is lymphatic spread."],
     ["Tumour invades through an organ surface into a body cavity and settles on the serosal membranes",
      "That is seeding of body cavities and surfaces."]],
   c=0, cite=c(14)),

 dict(topic="Lymphatic spread", io=IOD,
   q="What is the mechanism of lymphatic spread?",
   opts=[
     ["Cancer spreads into lymphatic vessels at the tumour margin and follows the natural route of lymphatic drainage",
      "Correct — the route is anatomically predictable, which is what makes nodal staging meaningful."],
     ["Cancer cells enter lymphatic vessels at the tumour centre and travel against the direction of drainage",
      "Entry is at the margin, and the cells follow drainage rather than opposing it."],
     ["Cancer cells degrade intercellular tissue with enzymes and invade a vein",
      "That is the haematogenous mechanism."],
     ["Cancer invades through an organ surface into a serosal cavity",
      "That is seeding."]],
   c=0, cite=c(14)),

 dict(topic="Seeding", io=IOD,
   q="Which cavities are named for seeding, and how does it happen?",
   opts=[
     ["Pericardial, pleural, peritoneal and joint cavities, and the subarachnoid space",
      "Correct — the mechanism is invasion of tumour through an organ surface into the cavity, most commonly the peritoneal cavity."],
     ["Only the peritoneal cavity, and only by direct extension along the mesentery",
      "Several cavities are named, and the peritoneum is merely the commonest."],
     ["The venous system, by cells separating and degrading intercellular tissue with enzymes",
      "That is haematogenous spread."],
     ["The regional lymph node basins, by following the natural route of drainage",
      "That is lymphatic spread."]],
   c=0, cite=c(15)),

 dict(topic="Seeding", io=IOD,
   q="In which cavity does seeding most commonly occur?",
   opts=[
     ["The peritoneal cavity",
      "Correct — the pericardial and pleural cavities and the subarachnoid space are also named."],
     ["The pericardial cavity",
      "It is one of the named cavities but not the commonest."],
     ["The pleural cavity",
      "Also named, but not the commonest."],
     ["The subarachnoid space",
      "Named, but the deck singles out the peritoneum."]],
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
      "Venous return is relevant to haematogenous spread."]],
   c=0, cite=c(15)),

 dict(topic="Benign classification", io=IOE,
   q="What are mesenchymal tumours derived from, and what tissues does that include?",
   opts=[
     ["Supportive tissue: connective tissue, adipose tissue, cartilage, smooth and striated muscle, and bone",
      "Correct — the same origin gives sarcomas when the tumour is malignant."],
     ["Epithelial surfaces: skin, gastrointestinal lining, respiratory lining and glandular ducts",
      "That is epithelial origin, which gives adenomas and papillomas when benign."],
     ["Haematopoietic tissue: bone marrow, lymph nodes, spleen and thymus",
      "Haematopoietic tumours are not the category described here."],
     ["Neural tissue: peripheral nerves, nerve sheaths and the central nervous system",
      "Neural origin is not what mesenchymal means in this classification."]],
   c=0, cite=c(16)),

 dict(topic="Benign classification", io=IOE,
   q="What is an adenoma?",
   opts=[
     ["A benign epithelial tumour with a glandular pattern, or from a gland",
      "Correct — it sometimes secretes the hormone or hormones produced by its gland of origin."],
     ["A malignant epithelial tumour with a glandular growth pattern",
      "That is an adenocarcinoma."],
     ["A benign mesenchymal tumour derived from connective tissue",
      "Mesenchymal benign tumours are not called adenomas."],
     ["A benign epithelial tumour producing finger-like projections from a surface",
      "That is a papilloma."]],
   c=0, cite=c(16)),

 dict(topic="Benign classification", io=IOE,
   q="What can an adenoma sometimes do that reflects its origin?",
   opts=[
     ["Secrete the hormone or hormones produced by its gland of origin",
      "Correct — the tumour retains a function of the tissue it came from."],
     ["Invade through the basement membrane into surrounding tissue",
      "Invasion is a malignant behaviour, and an adenoma is benign."],
     ["Seed the peritoneal cavity through an organ surface",
      "Seeding requires malignant invasion through the organ surface."],
     ["Produce finger-like projections from the epithelial surface",
      "That describes a papilloma rather than an adenoma."]],
   c=0, cite=c(16)),

 dict(topic="Benign classification", io=IOE,
   q="What is a papilloma?",
   opts=[
     ["A tumour with finger-like or warty projections from an epithelial surface",
      "Correct — the projections are visible microscopically or macroscopically."],
     ["A tumour forming a glandular pattern or arising from a gland",
      "That is an adenoma."],
     ["A malignant tumour arising from supportive, mesenchymal tissue",
      "That is a sarcoma."],
     ["A malignant epithelial tumour showing squamous cell differentiation",
      "That is a squamous cell carcinoma."]],
   c=0, cite=c(17)),

 dict(topic="Malignant classification", io=IOF,
   q="What is a malignant tumour of mesenchymal origin called?",
   opts=[
     ["A sarcoma",
      "Correct — mesenchymal means supportive tissue, and the malignant form is the sarcoma."],
     ["A carcinoma",
      "Carcinoma is the malignant tumour of epithelial origin."],
     ["An adenoma",
      "An adenoma is benign and epithelial."],
     ["A papilloma",
      "A papilloma is benign and epithelial."]],
   c=0, cite=c(18)),

 dict(topic="Malignant classification", io=IOF,
   q="What is a malignant tumour of epithelial origin called?",
   opts=[
     ["A carcinoma",
      "Correct — with adenocarcinoma for a glandular growth pattern and squamous cell carcinoma for squamous differentiation."],
     ["A sarcoma",
      "A sarcoma arises from supportive, mesenchymal tissue."],
     ["An adenoma",
      "An adenoma is the benign glandular epithelial tumour."],
     ["A papilloma",
      "A papilloma is benign."]],
   c=0, cite=c(18)),

 dict(topic="Malignant classification", io=IOF,
   q="What is a carcinoma with a glandular growth pattern called?",
   opts=[
     ["An adenocarcinoma",
      "Correct — the prefix names the pattern, the suffix names the malignancy and the epithelial origin."],
     ["An adenoma",
      "That is the benign counterpart."],
     ["A squamous cell carcinoma",
      "That is the carcinoma showing squamous cell differentiation."],
     ["A sarcoma",
      "A sarcoma is mesenchymal rather than epithelial."]],
   c=0, cite=c(18)),

 dict(topic="Malignant classification", io=IOF,
   q="What is a carcinoma showing squamous cell differentiation called?",
   opts=[
     ["Squamous cell carcinoma",
      "Correct — the other named pattern is glandular, which gives adenocarcinoma."],
     ["An adenocarcinoma",
      "That is the glandular pattern."],
     ["A papilloma",
      "A papilloma is a benign epithelial tumour with finger-like projections."],
     ["A sarcoma",
      "A sarcoma comes from supportive tissue."]],
   c=0, cite=c(18)),

 dict(topic="Naming rule", io=IOF,
   q="A malignant tumour arises from adipose tissue. Which category does it fall into?",
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
   q="Which three hurdles does the deck name for a tumour cell that has penetrated the vasculature?",
   opts=[
     ["Penetration of the vasculature, survival in the circulation, and survival in a new organ",
      "Correct — reaching the bloodstream is only the first of the three."],
     ["Penetration of the vasculature, evasion of apoptosis, and induction of angiogenesis",
      "Both of those are real steps in carcinogenesis but are not the three on this slide."],
     ["Invasion of the basement membrane, entry into lymphatics, and nodal colonisation",
      "That describes the lymphatic route rather than these three hurdles."],
     ["Initiation, promotion, and progression",
      "Those are the steps of chemical carcinogenesis."]],
   c=0, cite=c(26)),

 dict(topic="Metastatic pattern", io=IOD,
   q="What determines where a cancer metastasizes, according to the deck?",
   opts=[
     ["Venous blood flow, tumour and endothelial receptors, and genetic fitness",
      "Correct — the deck states explicitly that metastatic spread is NOT random but determined by these three."],
     ["Chance alone, since circulating tumour cells lodge wherever the vessel first narrows",
      "The deck says directly that metastatic spread is NOT random."],
     ["The size of the primary lesion and the duration of the disease",
      "Those affect staging rather than the pattern of spread."],
     ["The histological grade of the tumour and its rate of mitosis",
      "Grade and mitotic rate describe the tumour, not where it goes."]],
   c=0, cite=c(27)),

 dict(topic="Metastatic pattern", io=IOD,
   q="Is metastatic spread random?",
   opts=[
     ["No — it is determined by blood flow, receptors, and genetically determined fitness",
      "Correct — the slide makes this the headline."],
     ["Yes — circulating cells lodge in whichever capillary bed they reach first",
      "The deck explicitly rejects this."],
     ["Yes for haematogenous spread, no for lymphatic spread",
      "The statement in the deck is not split this way."],
     ["No — but only because lymphatic drainage is anatomically fixed",
      "Lymphatic anatomy is one factor, but the slide is about spread in general."]],
   c=0, cite=c(27)),

 dict(topic="Invasion", io=IOD,
   q="Which abnormal interaction does the deck name as a step in invasion, besides invasion into adjacent structures?",
   opts=[
     ["Abnormal cell-substratum interaction",
      "Correct — the cell's relationship with its own supporting matrix changes."],
     ["Abnormal cell-cycle checkpoint control",
      "Checkpoint failure is a gene-alteration problem rather than this step."],
     ["Abnormal apoptosis of neighbouring stromal cells",
      "Stromal apoptosis is not the named step."],
     ["Abnormal lymphatic valve function",
      "No such mechanism is described."]],
   c=0, cite=c(24)),

 dict(topic="Benign classification", io=IOE,
   q="A benign tumour arises from cartilage. Which category does it fall into?",
   opts=[
     ["Mesenchymal, since cartilage is supportive tissue",
      "Correct — connective tissue, adipose, cartilage, smooth and striated muscle, and bone are all listed."],
     ["Epithelial, since cartilage lines a surface",
      "Cartilage is supportive tissue rather than a lining epithelium."],
     ["Glandular, so it would be called an adenoma",
      "There is no gland of origin."],
     ["Neither, since the classification covers only epithelial tumours",
      "The classification explicitly has a mesenchymal category."]],
   c=0, cite=c(16)),
]
