# Clinical Pathophysiology I, Lecture 3 — pool D.
#
# WRITTEN FROM THE 2026-08-20 LECTURE RECORDING, not from the deck.
#
# This lecture SIGNPOSTS NOTHING -- 84 minutes across two independent
# transcriptions with no statement about what is or is not on the exam. So these
# are not re-weighting questions. They are the teaching that never reaches a
# slide: the clinical example Professor Rappa attaches to each term, and the one
# link the deck does not make at all (falling differentiation means a MORE
# AGGRESSIVE tumour).
#
# SCOPE still holds: pathophysiology, never management. The partition asserts it.
#
# Appended, never prepended.
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "Abnormal Cell Growth for posting.pptx"
REC = "2026-08-20 lecture recording"
def c(n): return f"{SRC}, Slide {n}"
def r(t): return f"{REC}, {t}"

IOA = "Objective a — Describe the molecular mechanisms of abnormal cell growth and differentiation"
IOB = "Objective b — Describe non-neoplastic abnormalities of cell growth"
IOD = "Objective d — Compare and contrast the routes of tumor spread"
IOF = "Objective f — Compare and contrast the different types of malignant tumors according to origin"
IOK = "Objective k — Describe the histological grading of cancer"

POOL_D = [
 dict(topic="Metaplasia", io=IOB,
   q="Which clinical example did Professor Rappa give for metaplasia, and what changes into what?",
   opts=[
     ["Barrett's oesophagus — squamous becomes columnar under chronic acid reflux",
      "Correct — the lower oesophagus is squamous and cannot resist acid, so chronic reflux drives the change."],
     ["Barrett's oesophagus — columnar becomes squamous under chronic acid reflux",
      "The direction is reversed; the oesophagus starts squamous."],
     ["Cervical dysplasia — squamous becomes columnar under human papillomavirus infection",
      "Cervical dysplasia was his DYSPLASIA example, and dysplasia is not a change of cell type."],
     ["Endometrial hyperplasia — glandular becomes squamous under excess oestrogen",
      "He used endometrial hyperplasia to illustrate hyperplasia, not metaplasia."]],
   c=0, cite=r("7:45")),

 dict(topic="Metaplasia", io=IOB,
   q="A sample from an oesophageal carcinoma shows COLUMNAR cells. What did Professor Rappa say that implies?",
   opts=[
     ["It is secondary to reflux disease",
      "Correct — squamous cells would indicate a primary cancer, since the lower oesophagus is normally squamous."],
     ["It is a primary oesophageal cancer",
      "Squamous cells would suggest that, because squamous is the native epithelium there."],
     ["It is a metastasis from a gastrointestinal primary",
      "That is not the inference he drew from the cell type."],
     ["It is a benign adenoma rather than a carcinoma",
      "The question already establishes it is a carcinoma."]],
   c=0, cite=r("8:47")),

 dict(topic="Dysplasia", io=IOB,
   q="Which example did Professor Rappa give for dysplasia, and what usually causes it?",
   opts=[
     ["Cervical dysplasia, usually caused by human papillomavirus",
      "Correct — he added that it might become archival one day because of the vaccine."],
     ["Barrett's oesophagus, usually caused by chronic acid reflux",
      "That was his metaplasia example."],
     ["Endometrial hyperplasia, usually caused by excess oestrogen",
      "That was his hyperplasia example."],
     ["Skeletal muscle hypertrophy, usually caused by resistance training",
      "That was his hypertrophy example."]],
   c=0, cite=r("10:47")),

 dict(topic="Hypertrophy", io=IOB,
   q="How did Professor Rappa explain skeletal muscle hypertrophy?",
   opts=[
     ["Striated muscle cells do not divide, so each fibre gets larger instead",
      "Correct — protein and resistance build more actin and myosin within the existing cells. Bigger fibres, not more fibres, which is the whole distinction from hyperplasia."],
     ["Resistance training recruits satellite cells, so the number of muscle fibres increases",
      "An increase in cell number would be hyperplasia; he was explicit that these cells do not divide."],
     ["Protein intake causes fluid retention within the muscle, so the organ appears larger",
      "Fluid was not the mechanism he described."],
     ["Resistance training converts slow fibres to fast fibres, changing the tissue type",
      "A change of cell type would be metaplasia."]],
   c=0, cite=r("2:54")),

 dict(topic="Permanent tissues", io=IOA,
   q="What principle did Professor Rappa give for which tissues can proliferate?",
   opts=[
     ["The more specialized the tissue, the less it can proliferate — skeletal muscle and neurons being the examples",
      "Correct — which is why hypertrophy is the only growth response available to them."],
     ["The more vascular the tissue, the less it can proliferate — cartilage and cornea being the examples",
      "Vascularity was not the principle he gave."],
     ["The more superficial the tissue, the less it can proliferate — epidermis being the example",
      "Epithelium proliferates constantly; he made that point directly."],
     ["The larger the cells, the less the tissue can proliferate — adipose being the example",
      "Cell size was not the principle."]],
   c=0, cite=r("6:08")),

 dict(topic="Differentiation", io=IOK,
   q="What does falling differentiation mean for the behaviour of a tumour, according to Professor Rappa?",
   opts=[
     ["It becomes more aggressive",
      "Correct — an anaplastic carcinoma is very aggressive compared with a well differentiated one. The deck gives grading as a scale of resemblance and stops there; he attaches the prognosis to it."],
     ["It becomes less aggressive, because poorly differentiated cells divide more slowly",
      "He said the opposite, and poorly differentiated cells are not slower."],
     ["Aggressiveness is unrelated to differentiation and depends only on stage",
      "Staging and grading are separate, but he explicitly linked grade to aggressiveness."],
     ["It becomes more aggressive only once the basement membrane has been breached",
      "Invasion is a separate matter from the grade."]],
   c=0, cite=r("24:08")),

 dict(topic="Differentiation", io=IOK,
   q="What is anaplasia also called, and what is differentiation judged against?",
   opts=[
     ["Also called atypia; differentiation is judged against the parent cell",
      "Correct — the pathologist compares the specimen with the tissue it came from."],
     ["Also called dysplasia; differentiation is judged against the basement membrane",
      "Dysplasia is a separate, non-neoplastic entity, and the membrane is a matter of invasion."],
     ["Also called pleomorphism; differentiation is judged against the tumour's own average cell",
      "Pleomorphism is one histological feature rather than another name for anaplasia."],
     ["Also called metaplasia; differentiation is judged against the surrounding stroma",
      "Metaplasia is a change of cell type in a non-neoplastic setting."]],
   c=0, cite=r("22:08")),

 dict(topic="Grading", io=IOK,
   q="Who did Professor Rappa say is the only one who can diagnose cancer?",
   opts=[
     ["The pathologist",
      "Correct — he said it twice. Grading is a histological judgement made on tissue."],
     ["The radiologist",
      "Imaging can suggest a cancer, but the diagnosis is histological."],
     ["The surgeon who obtains the specimen",
      "Obtaining tissue is not the same as diagnosing it."],
     ["The oncologist who stages the disease",
      "Staging follows a diagnosis that has already been made."]],
   c=0, cite=r("22:36")),

 dict(topic="Metastasis", io=IOD,
   q="Professor Rappa asked why lung cancer metastasizes to the brain. What is the vascular explanation?",
   opts=[
     ["Cells enter the left heart and leave by the carotids",
      "Correct — the lung sits downstream of the pulmonary circulation, so its cells reach the systemic arterial side and the internal carotid takes them to the brain."],
     ["Cells from the lung enter the portal vein, which carries them to the brain",
      "The portal vein carries gastrointestinal blood to the liver."],
     ["Cells from the lung travel retrogradely up the inferior vena cava",
      "The inferior vena cava carries blood towards the heart from below."],
     ["Cells from the lung follow lymphatic drainage into the subarachnoid space",
      "That would be seeding rather than haematogenous spread."]],
   c=0, cite=r("53:38")),

 dict(topic="Metastasis", io=IOD,
   q="What did Professor Rappa say knowing the vasculature lets you do?",
   opts=[
     ["Predict where metastases may form",
      "Correct — a gastrointestinal primary drains by the portal vein, so the liver; the lung drains to the left heart, so the brain."],
     ["Predict how quickly the primary tumour will grow",
      "Growth rate is a matter of the proliferative fraction rather than the vasculature."],
     ["Predict the histological grade of the metastasis",
      "Grade is judged on the specimen, not on the route."],
     ["Predict whether the tumour is benign or malignant",
      "Benign tumours do not metastasize at all."]],
   c=0, cite=r("53:48")),

 dict(topic="Carcinoma in situ", io=IOA,
   q="Which mnemonic did Professor Rappa give for carcinoma in situ, and what does it turn on?",
   opts=[
     ["Carcinoma 'in sight' — the cells are there, but not through the membrane",
      "Correct — they have not broken through the basement membrane. Once they do, it is an invasive carcinoma."],
     ["Carcinoma 'in situ-ation' — the cancer is confined to one clinical situation",
      "Not the mnemonic he gave, and not what the term means."],
     ["Carcinoma 'in size' — the lesion is below a size threshold",
      "Size is not what defines carcinoma in situ."],
     ["Carcinoma 'in stage' — the lesion has not yet been staged",
      "In situ is a defined stage, not an unstaged one."]],
   c=0, cite=r("13:41")),

 dict(topic="Nomenclature", io=IOF,
   q="What is the correct plural of carcinoma, according to Professor Rappa?",
   opts=[
     ["Carcinomata",
      "Correct — he called adding an s a misnomer, while allowing that most people do it."],
     ["Carcinomas",
      "He named this specifically as the mistaken form."],
     ["Carcinomae",
      "Not the form he gave."],
     ["Carcinomi",
      "Not the form he gave."]],
   c=0, cite=r("34:36")),

 dict(topic="Nomenclature", io=IOF,
   q="What do the prefixes leio- and rhabdo- mean in a sarcoma's name?",
   opts=[
     ["Leio- is smooth muscle; rhabdo- is skeletal muscle",
      "Correct — and adeno- means glandular, while the suffix -oma simply means tumour."],
     ["Leio- is skeletal muscle; rhabdo- is smooth muscle",
      "The two prefixes are reversed here."],
     ["Leio- is bone; rhabdo- is cartilage",
      "Neither prefix refers to bone or cartilage."],
     ["Leio- is glandular; rhabdo- is squamous",
      "Adeno- is the glandular prefix, and squamous has no such prefix."]],
   c=0, cite=r("14:43")),

 dict(topic="Epithelium", io=IOA,
   q="Why do the outermost cells of an epithelium slough off, as Professor Rappa explained it?",
   opts=[
     ["Epithelial tissue is avascular, so they are furthest from nutrients",
      "Correct — he used this to establish what a NORMAL epithelium looks like before showing a dysplastic one."],
     ["They are pushed off mechanically by the cells dividing beneath them",
      "Division below does displace them, but the reason he gave was the blood supply."],
     ["They undergo programmed apoptosis on a fixed schedule",
      "Apoptosis is not the explanation he gave here."],
     ["They are removed by Langerhans cells performing immune surveillance",
      "Immune surveillance is a different function of the skin."]],
   c=0, cite=r("13:13")),
]
