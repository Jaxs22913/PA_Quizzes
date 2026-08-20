# Clinical Pathophysiology I, Lecture 3 (Abnormal Cell Growth and Differentiation)
# — pool A. Objectives a, b, c and k: molecular mechanisms, the non-neoplastic
# abnormalities of cell growth, what a neoplasm is, and histological grading.
#
# SCOPE GUARD: this class is pathophysiology only. Every question asks what is
# happening in the tissue and why. No management, no drug of choice, no next
# step -- a question that would sit equally well in a Clinical Medicine and
# Surgery exam is pitched wrong for this one. The partition script asserts it.
#
# Correct answers kept SHORT wherever the content enumerates; the detail goes in
# the explanation the student reads after answering. That is one edit per
# question against three, measured on CMS Lecture 7.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "Abnormal Cell Growth for posting.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Objective a — Describe the molecular mechanisms of abnormal cell growth and differentiation"
IOB = "Objective b — Describe non-neoplastic abnormalities of cell growth"
IOC = "Objective c — Describe neoplastic abnormalities of cell growth"
IOK = "Objective k — Describe the histological grading of cancer"

POOL_A = [
 dict(topic="Agenesis", io=IOB,
   q="What is agenesis?",
   opts=[
     ["Complete absence of an organ, because the primordial tissue never formed",
      "Correct — the failure is at the very first step, before there is anything to develop."],
     ["Complete absence of an organ, although the primordial tissue formed normally",
      "That is aplasia: the tissue exists but fails to mature."],
     ["Partial development of an organ, resulting in a functional deficiency",
      "That is hypoplasia."],
     ["Shrinkage of an organ that had already formed and matured normally",
      "That is atrophy."]],
   c=0, cite=c(3)),

 dict(topic="Aplasia", io=IOB,
   q="How does aplasia differ from agenesis?",
   opts=[
     ["The primordial tissue exists but fails to develop into the mature organ",
      "Correct — in agenesis the primordial tissue never formed at all."],
     ["The primordial tissue never forms, so the organ is completely absent",
      "That is agenesis, which is the condition being contrasted."],
     ["The organ develops only partially, leaving a functional deficiency",
      "That is hypoplasia."],
     ["The organ enlarges because its individual cells enlarge",
      "That is hypertrophy."]],
   c=0, cite=c(3)),

 dict(topic="Hypoplasia", io=IOB,
   q="What is hypoplasia, and what does it produce?",
   opts=[
     ["Partial development of an organ, resulting in a functional deficiency",
      "Correct — some organ forms, but not enough of it to work properly."],
     ["Complete absence of an organ from failure of primordial tissue formation",
      "That is agenesis."],
     ["Shrinkage of a tissue or organ that formed and matured normally",
      "That is atrophy, which happens after normal development."],
     ["Change of one mature cell type into another mature cell type",
      "That is metaplasia."]],
   c=0, cite=c(3)),

 dict(topic="Atrophy", io=IOB,
   q="What distinguishes atrophy from hypoplasia?",
   opts=[
     ["Atrophy is shrinkage of a tissue or organ that had already formed and matured normally",
      "Correct — the timing is what separates them: hypoplasia is a developmental failure."],
     ["Atrophy is partial development of an organ that never reached mature size",
      "That is hypoplasia, a failure during development rather than a loss afterwards."],
     ["Atrophy is enlargement of an organ because its individual cells enlarge",
      "That is hypertrophy, and it is the opposite direction."],
     ["Atrophy is disordered growth of epithelial cells with variation in size and shape",
      "That is dysplasia."]],
   c=0, cite=c(3)),

 dict(topic="Hypertrophy", io=IOB,
   q="What causes an organ to enlarge in hypertrophy, and where is it especially important?",
   opts=[
     ["Enlargement of the individual cells; especially important in permanent tissues such as skeletal and cardiac muscle",
      "Correct — it may also occur in other tissues as part of adaptive growth."],
     ["An increase in the number of cells; especially important in labile tissues such as epithelium and bone marrow",
      "That describes hyperplasia rather than hypertrophy."],
     ["Replacement of one mature cell type by another; especially important at epithelial junctions",
      "That describes metaplasia."],
     ["Autonomous proliferation of a clone of cells; especially important in glandular tissue",
      "That describes a neoplasm."]],
   c=0, cite=c(3)),

 dict(topic="Metaplasia", io=IOB,
   q="What is metaplasia, and what provokes it?",
   opts=[
     ["Change of one cell type to another under chronic irritation or injury",
      "Correct — it involves a change in differentiation. The example on the slide is bladder transitional epithelium becoming squamous."],
     ["Disordered growth of epithelial cells with variation in size and shape and loss of architectural orientation",
      "That is dysplasia, which is the next step along and is precancerous."],
     ["Enlargement of an organ because its individual cells enlarge under increased demand",
      "That is hypertrophy."],
     ["Autonomous growth of an abnormal mass of tissue derived from a single genetically altered cell",
      "That is a neoplasm."]],
   c=0, cite=c(4)),

 dict(topic="Dysplasia", io=IOB,
   q="Which four features define dysplasia?",
   opts=[
     ["Disordered epithelial growth, varied cell size and shape, lost architecture, darker larger nuclei",
      "Correct — and it may progress to cancer, which is why dysplasia is called precancerous."],
     ["Orderly growth, typically mesenchymal; uniform cell size; preserved architecture; nuclei of normal size and staining",
      "Every one of these is the opposite of what dysplasia shows."],
     ["Complete replacement of one mature epithelium by another mature epithelium, with normal architecture retained",
      "That is metaplasia, in which differentiation changes but order is kept."],
     ["Invasion through the basement membrane with spread to regional lymph nodes",
      "That is invasive cancer, which is past the point dysplasia describes."]],
   c=0, cite=c(4)),

 dict(topic="Dysplasia", io=IOB,
   q="Why is dysplasia described as precancerous?",
   opts=[
     ["It may progress to cancer",
      "Correct — the deck states this directly. Dysplasia is disordered growth, not yet malignancy."],
     ["It has already invaded through the basement membrane",
      "Invasion through the basement membrane is what carcinoma in situ has not done and invasive cancer has."],
     ["It always metastasizes if left untreated for long enough",
      "Dysplasia does not metastasize; it may progress."],
     ["It arises from a single genetically altered cell and grows autonomously",
      "That is the definition of a neoplasm."]],
   c=0, cite=c(4)),

 dict(topic="Metaplasia", io=IOA,
   q="On the deck's metaplasia figure, which epithelium changes into which?",
   opts=[
     ["Bladder transitional epithelium becoming squamous epithelium",
      "Correct — squamous metaplasia, driven by chronic irritation."],
     ["Bladder squamous epithelium becoming transitional epithelium",
      "This reverses the direction shown."],
     ["Oesophageal squamous epithelium becoming columnar epithelium",
      "That is a real example of metaplasia, but it is not the figure in this deck."],
     ["Cervical columnar epithelium becoming glandular epithelium",
      "This is not what the figure shows."]],
   c=0, cite=c(5)),

 dict(topic="Neoplasm", io=IOC,
   q="What defines a neoplasm?",
   opts=[
     ["An abnormal mass of tissue growing autonomously, self-perpetuating without physiologic growth stimuli",
      "Correct — and the term is interchangeable with tumor."],
     ["An abnormal mass of tissue that enlarges only while a physiologic growth stimulus is present",
      "Dependence on a stimulus is exactly what a neoplasm does not have."],
     ["An enlargement of an organ produced by enlargement of its individual cells",
      "That is hypertrophy, which is non-neoplastic."],
     ["A change of one differentiated cell type into another under chronic irritation",
      "That is metaplasia, which is also non-neoplastic."]],
   c=0, cite=c(10)),

 dict(topic="Neoplasm", io=IOC,
   q="From how many cells is the proliferating population of a neoplasm derived?",
   opts=[
     ["One cell, which underwent a genetic alteration",
      "Correct — the whole population is clonal."],
     ["Many cells, each of which underwent an independent genetic alteration",
      "The deck describes a single cell of origin, not many."],
     ["Two cells, one parenchymal and one stromal",
      "Parenchyma and stroma are the components of the mass, not two origins."],
     ["A variable number, depending on the tissue in which it arises",
      "The deck states the derivation from one cell without qualification."]],
   c=0, cite=c(10)),

 dict(topic="Neoplasm", io=IOC,
   q="What are the two components of a neoplasm?",
   opts=[
     ["Parenchyma, the proliferating neoplastic cells; and stroma, the connective tissue and blood vessels",
      "Correct — the stroma is host tissue supporting the tumour, not part of the clone."],
     ["Parenchyma, the connective tissue and blood vessels; and stroma, the proliferating neoplastic cells",
      "This reverses the two definitions."],
     ["Initiator cells and promoter cells, in equal proportion",
      "Initiation and promotion are steps in chemical carcinogenesis, not components of a mass."],
     ["A proliferative pool and a maturation pool, which are always equal in size",
      "Those pools describe stem cell kinetics, and they are not equal in cancer."]],
   c=0, cite=c(10)),

 dict(topic="Cancer", io=IOC,
   q="What is cancer, and where does the word come from?",
   opts=[
     ["A malignant neoplasm; from the Latin for crab",
      "Correct — so named because it adheres to any tissue it seizes upon and reaches out with claws, invading surrounding tissue."],
     ["Any neoplasm at all; from the Latin for growth, because the mass enlarges without a stimulus",
      "Cancer is specifically the malignant subset, and the derivation is the crab."],
     ["A neoplasm that has metastasized; from the Greek for wandering, because cells migrate",
      "Metastasis is a feature many cancers develop, not the definition of the word."],
     ["A precancerous lesion; from the Latin for disorder, because architecture is lost",
      "Loss of architecture describes dysplasia, which is not cancer."]],
   c=0, cite=c(11)),

 dict(topic="Metastasis", io=IOC,
   q="What is a metastasis?",
   opts=[
     ["A portion of a cancer that has migrated from the primary site to other sites",
      "Correct — the primary remains where it began; the metastasis is what has left."],
     ["A second, unrelated primary cancer arising in another organ",
      "A metastasis is derived from the original cancer, not independent of it."],
     ["Local invasion of a cancer into the tissue immediately surrounding it",
      "That is invasion; metastasis means reaching a distant site."],
     ["A benign nodule that develops in the tissue draining a cancer",
      "Metastatic deposits are malignant, being part of the original cancer."]],
   c=0, cite=c(11)),

 dict(topic="Differentiation", io=IOK,
   q="What does the degree of differentiation of a neoplasm measure?",
   opts=[
     ["How closely it resembles comparable normal cells in appearance and function",
      "Correct — this is the basis of histological grading."],
     ["How far it has spread from the primary site within the patient",
      "That is staging, which is a different question from grading."],
     ["How rapidly the tumour mass is enlarging over time",
      "Growth rate is a feature of malignancy, but it is not what differentiation measures."],
     ["How many of its cells are in the proliferative pool at any moment",
      "The proliferative fraction is a matter of stem cell kinetics."]],
   c=0, cite=c(12)),

 dict(topic="Differentiation", io=IOK,
   q="What are the four grades of neoplastic differentiation, from most to least resemblance?",
   opts=[
     ["Well differentiated, moderately differentiated, poorly differentiated, anaplasia",
      "Correct — anaplasia is the complete lack of differentiation."],
     ["Anaplasia, poorly differentiated, moderately differentiated, well differentiated",
      "This is the correct sequence in reverse."],
     ["In situ, microinvasive, invasive, metastatic",
      "That is a progression of invasion rather than a grading of differentiation."],
     ["Stage I, stage II, stage III, stage IV",
      "Those are stages, which measure extent of spread rather than resemblance."]],
   c=0, cite=c(12)),

 dict(topic="Differentiation", io=IOK,
   q="What does anaplasia mean?",
   opts=[
     ["Lack of differentiation",
      "Correct — the extreme of the grading scale, with no resemblance to the normal cell."],
     ["Close resemblance to the comparable normal cell",
      "That is well differentiated, the opposite end of the scale."],
     ["Failure of a primordial tissue to develop into a mature organ",
      "That is aplasia, which is a non-neoplastic developmental abnormality."],
     ["Disordered growth of epithelium with retained architecture",
      "That is closer to dysplasia, and dysplasia does lose architectural orientation."]],
   c=0, cite=c(12)),

 dict(topic="Stem cells", io=IOA,
   q="Which properties define a stem cell?",
   opts=[
     ["Unlimited capacity for self-renewal and cellular immortality, but a relatively low rate of proliferation",
      "Correct — it can also differentiate into the mature cells that give the organ its function."],
     ["Unlimited capacity for self-renewal together with a very high rate of proliferation at all times",
      "The proliferation rate is described as relatively low, which is the counter-intuitive part."],
     ["A limited life-span and a high rate of proliferation once committed to differentiation",
      "Those are the properties of the differentiated progeny rather than the stem cell."],
     ["Autonomous growth without physiologic stimuli, derived from a single genetic alteration",
      "That is a neoplasm."]],
   c=0, cite=c(21)),

 dict(topic="Stem cells", io=IOA,
   q="What happens to proliferation once a cell has committed to differentiation?",
   opts=[
     ["It can be dramatic, but those cells have a limited life-span",
      "Correct — the stem cell itself proliferates slowly; the committed progeny do the expansion, and then die."],
     ["It stops entirely, and the differentiated cells become immortal",
      "Immortality belongs to the stem cell; differentiated cells have a limited life-span."],
     ["It stays at the same relatively low rate as the stem cell",
      "The deck describes the proliferation after commitment as dramatic."],
     ["It becomes autonomous and no longer requires physiologic stimuli",
      "Autonomy is a property of neoplasia, not of normal differentiation."]],
   c=0, cite=c(21)),

 dict(topic="Stem cell kinetics", io=IOA,
   q="What does abnormal differentiation of cancer cells do to the cell pools?",
   opts=[
     ["It puts a greater percentage of cells in the proliferative pool, at the expense of the maturation pool",
      "Correct — this is the lesson the deck draws from stem cell kinetics."],
     ["It puts a greater percentage of cells in the maturation pool, at the expense of the proliferative pool",
      "This reverses the shift; cancers accumulate proliferating cells."],
     ["It leaves both pools unchanged but shortens the cell cycle in each",
      "The deck describes a shift between pools rather than a faster cycle alone."],
     ["It empties both pools by driving cells into apoptosis",
      "Apoptosis is what is lost in cancer rather than what increases."]],
   c=0, cite=c(22)),

 dict(topic="Stem cell kinetics", io=IOA,
   q="Why does a tumour mass grow faster than normal tissue?",
   opts=[
     ["A higher proliferative fraction together with a lower rate of cell loss",
      "Correct — both halves matter; it is not only that cells divide faster."],
     ["A higher proliferative fraction together with a higher rate of cell loss",
      "A higher loss rate would offset the gain; the deck says loss is lower."],
     ["A lower proliferative fraction together with a lower rate of cell loss",
      "A lower proliferative fraction would slow growth rather than accelerate it."],
     ["An unchanged proliferative fraction with a shorter individual cell cycle",
      "The proliferative fraction is exactly what the deck says changes."]],
   c=0, cite=c(22)),

 dict(topic="Malignant histology", io=IOK,
   q="Which four histological features move a tumour from the benign end towards the malignant end?",
   opts=[
     ["Pleomorphism, abnormal nuclei, mitoses, and abnormal differentiation",
      "Correct — the deck lays these out as a spectrum rather than a switch."],
     ["Encapsulation, uniform nuclei, absent mitoses, and normal differentiation",
      "These are the benign features, at the opposite end of the same spectrum."],
     ["Invasion, lymphatic spread, haematogenous spread, and seeding",
      "Those are behaviours and routes of spread rather than histological features."],
     ["Initiation, promotion, progression, and metastasis",
      "Those are stages of carcinogenesis rather than what the slide grades."]],
   c=0, cite=c(23)),

 dict(topic="Abnormal growth", io=IOA,
   q="What two abnormalities does the deck contrast between a normal cell and a tumour cell?",
   opts=[
     ["Abnormal regulation of cell growth, and abnormal cell-cell interactions",
      "Correct — the same slide also contrasts a normal stem cell with a cancer stem cell."],
     ["Abnormal apoptosis, and abnormal deoxyribonucleic acid repair",
      "Both are genuinely important in carcinogenesis, but they are not the pair on this slide."],
     ["Abnormal vascular supply, and abnormal stromal composition",
      "Stroma and vessels are components of a neoplasm rather than this contrast."],
     ["Abnormal differentiation, and abnormal cell size",
      "Differentiation is graded separately; cell size alone is not the contrast drawn."]],
   c=0, cite=c(19)),

 dict(topic="Stem cells", io=IOA,
   q="How does the deck qualify the cancer stem cell idea?",
   opts=[
     ["As a conceptual framework rather than an absolute explanation",
      "Correct — the slide is explicit that this is a model, not a settled account."],
     ["As a fully established mechanism proven for every solid tumour",
      "The deck deliberately avoids claiming this."],
     ["As a hypothesis that has since been disproved",
      "It is presented as a useful framework, not as discredited."],
     ["As applicable only to haematological malignancies",
      "No such restriction is placed on it here."]],
   c=0, cite=c(21)),

 dict(topic="Dysplasia", io=IOA,
   q="On the deck's dysplasia diagram, what separates severe dysplasia from invasive cancer?",
   opts=[
     ["The basement membrane",
      "Correct — carcinoma in situ sits above it and invasive cancer has broken through. The diagram runs normal, mild, moderate, severe, carcinoma in situ, then invasive cancer."],
     ["The degree of nuclear enlargement, which is greater in invasive cancer",
      "Nuclear change is part of the grading, but the diagram turns on the basement membrane."],
     ["The presence of mitoses, which appear only once invasion has occurred",
      "Mitoses appear well before invasion on this spectrum."],
     ["Involvement of the regional lymph nodes",
      "Nodal involvement is a staging question, and comes after invasion."]],
   c=0, cite=c(8)),

 dict(topic="Abnormal growth", io=IOA,
   q="On the deck's abnormal tissue growth figure, what is the sequence from normal to cancer?",
   opts=[
     ["Normal, hyperplasia, mild dysplasia, carcinoma in situ, cancer",
      "Correct — carcinoma in situ is labelled as severe dysplasia on that figure."],
     ["Normal, metaplasia, atrophy, carcinoma in situ, cancer",
      "Atrophy is a non-neoplastic loss and does not sit on this progression."],
     ["Normal, hypertrophy, hyperplasia, dysplasia, cancer",
      "Hypertrophy is not a step on the figure's sequence."],
     ["Normal, aplasia, hypoplasia, dysplasia, cancer",
      "Aplasia and hypoplasia are developmental failures, not steps towards cancer."]],
   c=0, cite=c(9)),
]
