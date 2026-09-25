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

IOA = "a — Describe the molecular mechanisms of abnormal cell growth and differentiation"
IOB = "b — Describe non-neoplastic abnormalities of cell growth"
IOD = "d — Compare and contrast the routes of tumor spread"
IOF = "f — Compare and contrast the different types of malignant tumors according to origin"
IOK = "k — Describe the histological grading of cancer"

POOL_D = [
 dict(topic="Metaplasia", io=IOB,
   q="Which pairing gives a classic clinical example of metaplasia with the cell change involved?",
   opts=[
     ["Barrett's esophagus — squamous becomes columnar under chronic acid reflux",
      "Correct — the lower esophagus is squamous and cannot resist acid, so chronic reflux drives the change."],
     ["Barrett's esophagus — columnar becomes squamous under chronic acid reflux",
      "The direction is reversed: the lower esophagus is squamous and becomes columnar under chronic acid reflux."],
     ["Cervical dysplasia — squamous becomes columnar under human papillomavirus infection",
      "Cervical dysplasia is disordered epithelial growth, not a change of one cell type to another, so it is not metaplasia."],
     ["Endometrial hyperplasia — glandular becomes squamous under excess estrogen",
      "Hyperplasia is not a change of cell type; metaplasia replaces one cell type with another under chronic irritation."]],
   c=0, cite=r("7:45")),

 dict(topic="Metaplasia", io=IOB,
   q="A sample from an esophageal carcinoma shows COLUMNAR cells. What does that imply?",
   opts=[
     ["It is secondary to reflux disease",
      "Correct — squamous cells would indicate a primary cancer, since the lower esophagus is normally squamous."],
     ["It is a primary esophageal cancer",
      "Squamous cells would suggest that, because squamous is the native epithelium there."],
     ["It is a metastasis from a gastrointestinal primary",
      "Columnar cells in an esophageal carcinoma point to reflux-driven change, not to a metastasis from elsewhere."],
     ["It is a benign adenoma rather than a carcinoma",
      "An adenoma is benign, but the sample is already a carcinoma; columnar cells point to change secondary to reflux."]],
   c=0, cite=r("8:47")),

 dict(topic="Dysplasia", io=IOB,
   q="Which pairing gives an example of dysplasia with its usual cause?",
   opts=[
     ["Cervical dysplasia, usually caused by human papillomavirus",
      "Correct — high-risk human papillomavirus infects cervical epithelial cells, and the resulting uncontrolled proliferation raises the risk of progression from dysplasia to carcinoma."],
     ["Barrett's esophagus, usually caused by chronic acid reflux",
      "Chronic irritation changing one cell type into another is metaplasia, not dysplasia; high-risk human papillomavirus drives cervical dysplasia toward carcinoma."],
     ["Endometrial hyperplasia, usually caused by excess estrogen",
      "Hyperplasia is not dysplasia; dysplasia is disordered epithelial growth with loss of architectural orientation and darker, larger nuclei."],
     ["Skeletal muscle hypertrophy, usually caused by resistance training",
      "Skeletal muscle hypertrophy is enlargement of individual cells, not the disordered epithelial growth with variation in cell size and shape that defines dysplasia."]],
   c=0, cite=c(37)),

 dict(topic="Hypertrophy", io=IOB,
   q="Why does skeletal muscle hypertrophy rather than divide?",
   opts=[
     ["Striated muscle cells do not divide, so each fiber gets larger instead",
      "Correct — skeletal muscle is a permanent tissue, so it grows by enlarging each existing fiber, which is hypertrophy rather than hyperplasia."],
     ["Resistance training recruits satellite cells, so the number of muscle fibers increases",
      "More fibers would be hyperplasia; skeletal muscle is a permanent tissue whose cells enlarge rather than divide."],
     ["Protein intake causes fluid retention within the muscle, so the organ appears larger",
      "Fluid retention is not hypertrophy; hypertrophy is enlargement of a tissue due to enlargement of its individual cells."],
     ["Resistance training converts slow fibers to fast fibers, changing the tissue type",
      "A change of cell type would be metaplasia; hypertrophy keeps the same cells and enlarges each one."]],
   c=0, cite=c(3)),

 dict(topic="Permanent tissues", io=IOA,
   q="Which principle governs which tissues can proliferate?",
   opts=[
     ["The more specialized the tissue, the less it can proliferate — skeletal muscle and neurons being the examples",
      "Correct — skeletal and cardiac muscle are permanent tissues, so hypertrophy is the growth response available to them."],
     ["The more vascular the tissue, the less it can proliferate — cartilage and cornea being the examples",
      "Vascularity is not the governing principle; specialized permanent tissues such as skeletal muscle proliferate least."],
     ["The more superficial the tissue, the less it can proliferate — epidermis being the example",
      "Epithelium proliferates readily rather than poorly; it is specialized permanent tissue such as muscle that cannot divide."],
     ["The larger the cells, the less the tissue can proliferate — adipose being the example",
      "Cell size is not the governing principle; the more specialized the tissue, the less it can proliferate."]],
   c=0, cite=r("6:08")),

 dict(topic="Differentiation", io=IOK,
   q="What does falling differentiation mean for the behavior of a tumor?",
   opts=[
     ["It becomes more aggressive",
      "Correct — poorly differentiated cells stay in the proliferative pool, so the tumor grows faster; benign tumors are usually well differentiated and slow growing."],
     ["It becomes less aggressive, because poorly differentiated cells divide more slowly",
      "Poorly differentiated cells are not slower: abnormal differentiation puts a greater percentage of cells in the proliferative pool."],
     ["Aggressiveness is unrelated to differentiation and depends only on stage",
      "Staging and grading are separate measures, but falling differentiation by itself signals a more aggressive tumor."],
     ["It becomes more aggressive only once the basement membrane has been breached",
      "Invasion through the basement membrane is a separate matter; aggressiveness rises as differentiation falls, with or without it."]],
   c=0, cite=c(22)),

 dict(topic="Differentiation", io=IOK,
   q="What is anaplasia also called, and what is differentiation judged against?",
   opts=[
     ["Also called atypia; differentiation is judged against the parent cell",
      "Correct — the pathologist compares the specimen with the tissue it came from."],
     ["Also called dysplasia; differentiation is judged against the basement membrane",
      "Dysplasia is a separate, non-neoplastic entity, and the membrane is a matter of invasion."],
     ["Also called pleomorphism; differentiation is judged against the tumor's own average cell",
      "Pleomorphism is one histological feature rather than another name for anaplasia."],
     ["Also called metaplasia; differentiation is judged against the surrounding stroma",
      "Metaplasia is a change of cell type in a non-neoplastic setting."]],
   c=0, cite=r("22:08")),

 dict(topic="Grading", io=IOK,
   q="Who is the only one who can diagnose cancer?",
   opts=[
     ["The pathologist",
      "Correct — cancer is a histological diagnosis, judged on tissue by how closely the cells resemble comparable normal cells."],
     ["The radiologist",
      "Imaging can suggest a cancer, but the diagnosis is histological."],
     ["The surgeon who obtains the specimen",
      "Obtaining a specimen is not diagnosing it; the diagnosis is histological, made by the pathologist on the tissue."],
     ["The oncologist who stages the disease",
      "Staging follows a diagnosis already made; the pathologist establishes the diagnosis histologically on tissue."]],
   c=0, cite=r("22:36")),

 dict(topic="Metastasis", io=IOD,
   q="What is the vascular explanation for lung cancer metastasizing to the brain?",
   opts=[
     ["Cells enter the left heart and leave by the carotids",
      "Correct — the lung sits downstream of the pulmonary circulation, so its cells reach the systemic arterial side and the internal carotid takes them to the brain."],
     ["Cells from the lung enter the portal vein, which carries them to the brain",
      "Cancers entering the portal vein spread to the liver, not the brain; lung cells travel via the left heart and the carotids."],
     ["Cells from the lung travel retrogradely up the inferior vena cava",
      "Cancers entering the inferior vena cava spread to the lungs; lung cells reach the brain via the left heart and the carotids."],
     ["Cells from the lung follow lymphatic drainage into the subarachnoid space",
      "Spread into a body cavity or the subarachnoid space is seeding; lung cells reach the brain through the blood, via the left heart and carotids."]],
   c=0, cite=r("53:38")),

 dict(topic="Metastasis", io=IOD,
   q="What does knowledge of a tumor's vascular drainage allow?",
   opts=[
     ["Predict where metastases may form",
      "Correct — a gastrointestinal primary drains by the portal vein, so the liver; the lung drains to the left heart, so the brain."],
     ["Predict how quickly the primary tumor will grow",
      "Growth rate is a matter of the proliferative fraction rather than the vasculature."],
     ["Predict the histological grade of the metastasis",
      "Grade is judged on the specimen's differentiation, not predicted from the route of venous drainage."],
     ["Predict whether the tumor is benign or malignant",
      "Benign tumors do not metastasize at all, so vascular drainage cannot distinguish benign from malignant."]],
   c=0, cite=r("53:48")),

 dict(topic="Carcinoma in situ", io=IOA,
   q="Which mnemonic captures what defines carcinoma in situ?",
   opts=[
     ["Carcinoma 'in sight' — the cells are there, but not through the membrane",
      "Correct — they have not broken through the basement membrane. Once they do, it is an invasive carcinoma."],
     ["Carcinoma 'in situ-ation' — the cancer is confined to one clinical situation",
      "Carcinoma in situ is not about a clinical situation; it means the lesion has not invaded through the basement membrane."],
     ["Carcinoma 'in size' — the lesion is below a size threshold",
      "Size does not define carcinoma in situ; Tis means the lesion has not invaded through the basement membrane."],
     ["Carcinoma 'in stage' — the lesion has not yet been staged",
      "In situ is itself a defined stage, Tis, for a lesion that has not invaded through the basement membrane."]],
   c=0, cite=r("13:41")),

 dict(topic="Nomenclature", io=IOF,
   q="What is the classical plural of carcinoma?",
   opts=[
     ["Carcinomata",
      "Correct — carcinomata is the classical plural, although carcinomas, formed by simply adding an s, is what most people say."],
     ["Carcinomas",
      "Carcinomas, formed by simply adding an s, is the everyday English plural; the classical plural is carcinomata."],
     ["Carcinomae",
      "Carcinomae is not the classical plural; carcinoma takes the ending -ata, which gives carcinomata."],
     ["Carcinomi",
      "Carcinomi is not the classical plural either; carcinoma takes the ending -ata, which gives carcinomata."]],
   c=0, cite=r("34:36")),

 dict(topic="Nomenclature", io=IOF,
   q="What do the prefixes leio- and rhabdo- mean in a sarcoma's name?",
   opts=[
     ["Leio- is smooth muscle; rhabdo- is skeletal muscle",
      "Correct — and adeno- means glandular, while the suffix -oma simply means tumor."],
     ["Leio- is skeletal muscle; rhabdo- is smooth muscle",
      "The prefixes are reversed: leio- means smooth muscle and rhabdo- means skeletal, or striated, muscle."],
     ["Leio- is bone; rhabdo- is cartilage",
      "Bone and cartilage are mesenchymal tissues, but leio- means smooth muscle and rhabdo- means skeletal muscle."],
     ["Leio- is glandular; rhabdo- is squamous",
      "Adeno- is the glandular prefix, and squamous has no such prefix."]],
   c=0, cite=r("14:43")),

 dict(topic="Epithelium", io=IOA,
   q="Why do the outermost cells of an epithelium slough off?",
   opts=[
     ["Epithelial tissue is avascular, so they are furthest from nutrients",
      "Correct — epithelial tissue is avascular, so the outermost cells, furthest from the underlying blood supply, are lost first."],
     ["They are pushed off mechanically by the cells dividing beneath them",
      "Division beneath does displace them, but the underlying reason is distance from nutrients in an avascular tissue."],
     ["They undergo programmed apoptosis on a fixed schedule",
      "Programmed apoptosis is not the reason; the outer cells are furthest from nutrients because epithelium is avascular."],
     ["They are removed by Langerhans cells performing immune surveillance",
      "Langerhans cell surveillance is a separate skin function; the outer cells are lost because epithelium is avascular."]],
   c=0, cite=r("13:13")),
]
