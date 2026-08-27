# Clinical Pathophysiology I, Lecture 3 (Abnormal Cell Growth and Differentiation)
# — pool C. Objectives g, h, i, j and l: the four categories of gene alteration,
# chemical carcinogenesis, the microbial causes, heredity, and TNM staging.
#
# The p53 / retinoblastoma pair runs through this whole pool and is asked from
# several directions, because three separate microbes converge on it: human
# papillomavirus E6 blocks p53 and E7 blocks retinoblastoma protein, and
# hepatitis B encodes a protein that binds p53. Knowing what each gene DOES is
# what makes those mechanisms make sense rather than being three facts.
#
# SLIDE 43 IS AN IMAGE -- a lung-cancer-specific 7th-edition TNM table. Nothing
# here asks for its lung-specific T and N cut-offs, because the deck's own point
# on slide 42 is that TNM definitions are CANCER-SPECIFIC. The image illustrates
# that point; it is not a memorisation target, and treating it as one would be
# inventing scope.
#
# SCOPE GUARD: pathophysiology only. The one place management is mentioned in
# the deck -- eradicating Helicobacter pylori -- is asked as what eradication
# does to RISK, which is the mechanism, not as a treatment recommendation.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "Abnormal Cell Growth for posting.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOG = "g — Compare and contrast the categories of gene alterations in carcinogenesis"
IOH = "h — Describe the steps of chemical carcinogenesis"
IOI = "i — Describe microorganisms' role in carcinogenesis"
IOJ = "j — Compare and contrast the theories of heredity and carcinogenesis"
IOL = "l — Describe the tumor, nodes, metastases (TNM) staging system"

POOL_C = [
 dict(topic="Carcinogenesis", io=IOG,
   q="How does the deck characterise carcinogenesis overall?",
   opts=[
     ["A multistep process, resulting from damage to multiple normal regulatory genes",
      "Correct — a single mutation is not enough; the damage accumulates."],
     ["A single-step process, resulting from one mutation in one regulatory gene",
      "The deck is explicit that it is multistep and involves multiple genes."],
     ["A purely inherited process, requiring a germline mutation to begin",
      "Damaged genes may be inherited AND/OR acquired."],
     ["A purely environmental process, requiring an external carcinogen",
      "Inheritance is one of the named sources of damaged genes."]],
   c=0, cite=c(28)),

 dict(topic="Carcinogenesis", io=IOG,
   q="Where does the gene damage in carcinogenesis come from?",
   opts=[
     ["Inherited, and/or acquired from chemicals, radiation or microbes",
      "Correct — the named sources are chemical carcinogens, ultraviolet and ionizing radiation, and microbial organisms: viruses and one bacterium."],
     ["It is always inherited through the germline and never acquired during life",
      "The deck lists several acquired sources alongside inheritance."],
     ["It is always acquired during life and never inherited",
      "Inheritance is explicitly one of the sources."],
     ["It arises only from errors during deoxyribonucleic acid replication",
      "Replication error is not among the sources the deck names."]],
   c=0, cite=c(28)),

 dict(topic="Protooncogenes", io=IOG,
   q="What do protooncogenes normally do, and what are they?",
   opts=[
     ["They promote REGULATED cell growth",
      "Correct — the word to hold onto is regulated. They are growth factors, growth factor receptors, nuclear regulatory proteins, and proteins involved in signal transduction. Mutation removes the regulation."],
     ["They inhibit cell growth; they include neurofibromin, retinoblastoma protein and the adenomatous polyposis coli protein",
      "Those are tumour suppressor genes, the opposite category."],
     ["They repair damaged deoxyribonucleic acid; they include BRCA-1 and BRCA-2",
      "That is the third category, the repair genes."],
     ["They cause cells with damaged deoxyribonucleic acid to self destruct",
      "That is the fourth category, the apoptosis genes."]],
   c=0, cite=c(29)),

 dict(topic="Oncogenes", io=IOG,
   q="What happens when a protooncogene mutates?",
   opts=[
     ["It becomes an oncogene, which encodes oncoproteins that promote continued uncontrolled growth",
      "Correct — the same machinery, with the brake removed."],
     ["It becomes a tumour suppressor gene, which then inhibits cell growth excessively",
      "Tumour suppressor genes are a separate category, and they are lost rather than gained."],
     ["It becomes a repair gene, which then introduces errors into the genome",
      "Repair genes are a separate category, and mutation disables them."],
     ["It becomes silent, so the cell loses its ability to grow at all",
      "The result is uncontrolled growth, not loss of growth."]],
   c=0, cite=c(29)),

 dict(topic="Tumour suppressors", io=IOG,
   q="What do tumour suppressor genes do, and which examples does the deck give?",
   opts=[
     ["They inhibit cell growth; the examples are NF-1, NF-2, retinoblastoma and adenomatous polyposis coli",
      "Correct — losing them removes a brake rather than adding an accelerator."],
     ["They promote regulated cell growth; the examples are growth factors and their receptors",
      "That is the protooncogene category."],
     ["They repair damaged deoxyribonucleic acid; the examples are BRCA-1 and BRCA-2",
      "That is the repair-gene category."],
     ["They trigger apoptosis in damaged cells; no specific examples are named",
      "Apoptosis genes are the fourth category and are described separately."]],
   c=0, cite=c(29)),

 dict(topic="Repair genes", io=IOG,
   q="Which genes are named as promoting repair of damaged deoxyribonucleic acid?",
   opts=[
     ["BRCA-1 and BRCA-2",
      "Correct — a minority of breast cancer patients carry an inherited mutation in one of them."],
     ["NF-1 and NF-2",
      "Those are tumour suppressor genes."],
     ["Retinoblastoma and adenomatous polyposis coli",
      "Those are also tumour suppressor genes."],
     ["p16 and p53",
      "p16 is named under heredity as a tumour suppressor; p53 works in apoptosis."]],
   c=0, cite=c(30)),

 dict(topic="Apoptosis genes", io=IOG,
   q="Why does the deck say genes promoting self destruction of cells with damaged deoxyribonucleic acid are necessary?",
   opts=[
     ["To stop the damage becoming permanent in dividing cells",
      "Correct — apoptosis prevents a mutation being carried on into the daughter cells."],
     ["To limit the total number of cells an organ can contain",
      "Cell number control is not the reason given."],
     ["To supply nutrients to neighbouring cells as they proliferate",
      "No such metabolic role is described."],
     ["To slow the rate at which stem cells commit to differentiation",
      "That is a question of stem cell kinetics rather than apoptosis."]],
   c=0, cite=c(30)),

 dict(topic="Gene categories", io=IOG,
   q="How many categories of gene alteration in carcinogenesis does the deck describe, and what are they?",
   opts=[
     ["Four",
      "Correct — protooncogenes, tumour suppressor genes, genes promoting repair of damaged deoxyribonucleic acid, and genes promoting apoptosis. Two are gains of function and two are losses."],
     ["Two: protooncogenes and tumour suppressor genes",
      "Those are the first two of four."],
     ["Three: protooncogenes, tumour suppressor genes, and repair genes",
      "The apoptosis genes are the fourth."],
     ["Five, adding angiogenesis genes to the four described",
      "Angiogenesis genes are not one of the categories here."]],
   c=0, cite=c(29)),

 dict(topic="Initiation", io=IOH,
   q="What do initiators do in chemical carcinogenesis?",
   opts=[
     ["They cause permanent damage to deoxyribonucleic acid",
      "Correct — permanence is what distinguishes initiation from promotion."],
     ["They cause sustained or enhanced proliferation of already-damaged cells",
      "That is promotion, the second step."],
     ["They repair damage already caused by another carcinogen",
      "Initiators cause damage; they do not repair it."],
     ["They trigger apoptosis in cells with damaged genomes",
      "Apoptosis is the protective mechanism initiators help defeat."]],
   c=0, cite=c(31)),

 dict(topic="Promotion", io=IOH,
   q="What do promoters do?",
   opts=[
     ["They drive proliferation of cells already damaged by an initiator",
      "Correct — sustained or enhanced proliferation raises the risk of successive mutations leading to cancer."],
     ["They cause the permanent deoxyribonucleic acid damage that starts the process",
      "That is initiation."],
     ["They repair the deoxyribonucleic acid damage caused by initiators",
      "Promoters act in the opposite direction."],
     ["They cause tumour cells to detach and enter the circulation",
      "That is part of the invasion and metastasis cascade."]],
   c=0, cite=c(31)),

 dict(topic="Chemical carcinogens", io=IOH,
   q="Which carcinogens are produced by the combustion of tobacco, and what do they cause?",
   opts=[
     ["Polycyclic aromatic hydrocarbons, causing bladder and lung cancer",
      "Correct — among the most powerful carcinogens known, and tobacco smoke contains numerous others besides."],
     ["Aromatic amines, causing bladder and lung cancer; among the most powerful carcinogens known",
      "Aromatic amines are classically emphasised in OCCUPATIONAL bladder cancer."],
     ["Nitrosamines, causing gastric and oesophageal cancer",
      "Nitrosamines are not the agents this deck names."],
     ["Aflatoxins, causing hepatocellular carcinoma",
      "Aflatoxin is not among the chemical carcinogens listed here."]],
   c=0, cite=c(31)),

 dict(topic="Chemical carcinogens", io=IOH,
   q="Which chemical carcinogens are classically emphasised in occupational bladder cancer?",
   opts=[
     ["Aromatic amines",
      "Correct — polycyclic aromatic hydrocarbons come from tobacco combustion."],
     ["Polycyclic aromatic hydrocarbons",
      "Those are the tobacco combustion products, which also cause bladder cancer."],
     ["Alkylating agents",
      "Not among the named agents in this deck."],
     ["Asbestos fibres",
      "Not among the named agents in this deck."]],
   c=0, cite=c(31)),

 dict(topic="Human papillomavirus", io=IOI,
   q="Which human papillomavirus subtypes most commonly cause cervical cancer?",
   opts=[
     ["Types 16 and 18",
      "Correct — of many genetic subtypes, these two cause the majority."],
     ["Types 6 and 11",
      "Those are the low-risk types not named here for cervical cancer."],
     ["Types 1 and 2",
      "Not the subtypes this deck names."],
     ["Types 31 and 33",
      "The deck names 16 and 18 specifically."]],
   c=0, cite=c(32)),

 dict(topic="Human papillomavirus", io=IOI,
   q="What do the human papillomavirus proteins E6 and E7 each block?",
   opts=[
     ["E6 blocks p53; E7 blocks retinoblastoma protein",
      "Correct — p53 promotes self destruction of mutated cells and retinoblastoma protein inhibits cell growth, so one removes apoptosis and the other removes a growth brake."],
     ["E6 blocks retinoblastoma protein, which inhibits cell growth; E7 blocks p53, which promotes apoptosis",
      "This reverses the two targets."],
     ["E6 blocks BRCA-1 and E7 blocks BRCA-2, both of which repair damaged deoxyribonucleic acid",
      "The BRCA genes are not the targets of these viral proteins."],
     ["E6 and E7 both block p53, doubling the loss of apoptosis",
      "They act on two different targets, which is why both matter."]],
   c=0, cite=c(32)),

 dict(topic="Human papillomavirus", io=IOI,
   q="How does human papillomavirus produce excessive E6 and E7?",
   opts=[
     ["It integrates its viral genome into the host cell genome",
      "Correct — it lands in a location that results in excessive production of E6 and E7, and integration is the step that makes the infection oncogenic."],
     ["It remains entirely episomal and produces the proteins from a free viral plasmid",
      "The deck describes integration into the host genome."],
     ["It causes the host to amplify its own p53 and retinoblastoma genes",
      "The viral proteins block those host proteins rather than amplify them."],
     ["It induces chronic inflammation, which raises transcription of all viral genes",
      "Chronic inflammation is the mechanism emphasised for hepatitis B and Helicobacter."]],
   c=0, cite=c(32)),

 dict(topic="Human papillomavirus", io=IOI,
   q="Besides cervical cancer, which malignancies is high-risk human papillomavirus associated with?",
   opts=[
     ["Anal, vulvar, vaginal, penile and oropharyngeal cancer",
      "Correct — all five are listed alongside cervical cancer, the oropharyngeal one being a squamous cell carcinoma."],
     ["Hepatocellular carcinoma and gastric adenocarcinoma",
      "Those belong to the hepatitis viruses and Helicobacter pylori respectively."],
     ["Nasopharyngeal carcinoma and certain B cell lymphomas",
      "Those belong to Epstein Barr virus."],
     ["Retinoblastoma and osteosarcoma",
      "Those are associated with the retinoblastoma protein under heredity."]],
   c=0, cite=c(37)),

 dict(topic="Epstein Barr virus", io=IOI,
   q="Which cancers is Epstein Barr virus associated with, and which cells does it infect?",
   opts=[
     ["B cell lymphomas and nasopharyngeal carcinoma; it infects B lymphocytes",
      "Correct — it immortalizes them, which is the key step, and it also infects epithelial cells of the oropharynx."],
     ["Hepatocellular carcinoma; it infects hepatocytes and causes chronic injury with regeneration",
      "That is hepatitis B and hepatitis C."],
     ["Cervical carcinoma; it infects cervical epithelium and integrates its genome",
      "That is human papillomavirus."],
     ["Gastric adenocarcinoma and mucosa-associated lymphoid tissue lymphoma; it colonizes the stomach",
      "That is Helicobacter pylori."]],
   c=0, cite=c(33)),

 dict(topic="Epstein Barr virus", io=IOI,
   q="What happens in a patient with normal immune function who is infected with Epstein Barr virus?",
   opts=[
     ["No immortalization; they are asymptomatic or get mononucleosis",
      "Correct — a self-limited infectious mononucleosis. Normal immune function is what stops the immortalization becoming cancer."],
     ["Their B lymphocytes are immortalized, but the resulting lymphoma regresses spontaneously",
      "Immortalization resulting in cancer is what does NOT happen in the immunocompetent."],
     ["They develop nasopharyngeal carcinoma within a few years of infection",
      "That outcome is not what normal immune function produces."],
     ["They clear the virus completely and cannot be reinfected",
      "The deck describes asymptomatic infection or mononucleosis rather than sterilising clearance."]],
   c=0, cite=c(33)),

 dict(topic="Hepatitis B", io=IOI,
   q="By what mechanism does hepatitis B virus lead to hepatocellular carcinoma?",
   opts=[
     ["Chronic injury drives regeneration; it also binds p53",
      "Correct — chronic infection stimulates continuous regenerative attempts, putting cells at risk of mutation. The deck emphasises chronic inflammation, regenerative hyperplasia and genomic instability."],
     ["It integrates its genome so as to overproduce E6 and E7",
      "Those are human papillomavirus proteins."],
     ["It infects and immortalizes B lymphocytes",
      "That is Epstein Barr virus."],
     ["It colonizes the stomach and causes atrophic gastritis",
      "That is Helicobacter pylori."]],
   c=0, cite=c(34)),

 dict(topic="Hepatitis B", io=IOI,
   q="Which three concepts does the hepatitis B slide emphasise?",
   opts=[
     ["Chronic inflammation, regenerative hyperplasia, genomic instability",
      "Correct — the same triad also explains hepatitis C and Helicobacter pylori."],
     ["Initiation, promotion, and progression",
      "Those are the steps of chemical carcinogenesis."],
     ["Pleomorphism, abnormal nuclei, and abnormal differentiation",
      "Those are histological features of malignancy."],
     ["Self-renewal, immortality, and differentiation capacity",
      "Those are the properties of a stem cell."]],
   c=0, cite=c(34)),

 dict(topic="Helicobacter pylori", io=IOI,
   q="What kind of organism is Helicobacter pylori, and what does it cause in the stomach?",
   opts=[
     ["A Gram-negative bacterium causing chronic gastritis",
      "Correct — it colonizes the stomach and may lead to atrophic gastritis and intestinal metaplasia. It is the one bacterium among the microbial causes in this deck."],
     ["A Gram-positive bacterium that colonizes the stomach, causing acute ulceration and perforation",
      "It is Gram-negative, and the process described is chronic rather than acute."],
     ["A virus that integrates its genome into gastric epithelial cells",
      "The viral mechanisms belong to human papillomavirus, Epstein Barr and the hepatitis viruses."],
     ["A fungus that colonizes the gastric mucosa in immunosuppressed patients",
      "No fungal cause is described."]],
   c=0, cite=c(35)),

 dict(topic="Helicobacter pylori", io=IOI,
   q="Which two malignancies is Helicobacter pylori associated with?",
   opts=[
     ["Gastric adenocarcinoma and mucosa-associated lymphoid tissue lymphoma",
      "Correct — usually abbreviated to MALT lymphoma."],
     ["Hepatocellular carcinoma and cholangiocarcinoma",
      "Those relate to the hepatitis viruses rather than to Helicobacter."],
     ["Nasopharyngeal carcinoma and Burkitt lymphoma",
      "Those relate to Epstein Barr virus."],
     ["Cervical carcinoma and oropharyngeal squamous cell carcinoma",
      "Those relate to human papillomavirus."]],
   c=0, cite=c(35)),

 dict(topic="Helicobacter pylori", io=IOI,
   q="What does eradicating Helicobacter pylori do to cancer risk?",
   opts=[
     ["It reduces gastric cancer risk, and some early MALT lymphomas regress",
      "Correct — evidence that the chronic inflammation itself is the carcinogenic driver."],
     ["It has no effect on cancer risk once colonization has occurred",
      "The deck states that eradication reduces risk."],
     ["It increases the risk, because the inflammatory response is protective",
      "The inflammation is the problem rather than the protection."],
     ["It reverses established gastric adenocarcinoma",
      "Regression is described for some early MALT lymphomas, not for established carcinoma."]],
   c=0, cite=c(35)),

 dict(topic="Hepatitis C", io=IOI,
   q="How does hepatitis C lead to hepatocellular carcinoma, and in whom does it usually develop?",
   opts=[
     ["Repeated cell death and proliferation; usually, but not always, in cirrhosis",
      "Correct — chronic hepatitis causes ongoing injury, inflammation and regeneration, and the cycles accumulate mutations. Most cases arise in cirrhosis, but cancer can occasionally occur without it."],
     ["Repeated cycles of cell death and proliferation accumulate mutations; cirrhosis is an absolute prerequisite",
      "The deck says cancer can occasionally occur without cirrhosis."],
     ["The virus integrates its genome and overproduces oncoproteins; cirrhosis is irrelevant",
      "Genome integration with oncoprotein production is human papillomavirus."],
     ["The virus immortalizes hepatocytes directly, without chronic inflammation",
      "Chronic hepatitis with ongoing injury and regeneration is the described mechanism."]],
   c=0, cite=c(36)),

 dict(topic="Radiation", io=IOI,
   q="Which forms of radiation does the deck name as causes of cancer?",
   opts=[
     ["Ultraviolet B, and ionizing radiation",
      "Correct — ultraviolet B is the wavelength that damages deoxyribonucleic acid directly."],
     ["Ultraviolet A only, together with infrared radiation",
      "The ultraviolet form named is B, and infrared is not listed."],
     ["Microwave and radiofrequency radiation",
      "Neither is named as a carcinogen here."],
     ["Ionizing radiation only, with no ultraviolet contribution",
      "Ultraviolet B is named alongside ionizing radiation."]],
   c=0, cite=c(38)),

 dict(topic="Heredity", io=IOJ,
   q="Which tumours are associated with an inherited alteration of the retinoblastoma protein?",
   opts=[
     ["Retinoblastoma, a rare childhood tumour of the eye, and osteosarcoma",
      "Correct — the same tumour suppressor, two very different tumours."],
     ["Neurofibromatosis types 1 and 2, with tumours of the central and peripheral nervous system",
      "Those follow from NF-1 and NF-2."],
     ["Malignant melanoma",
      "That follows from p16, also called INK4a."],
     ["Familial adenomatous polyposis and colon cancer",
      "That follows from adenomatous polyposis coli."]],
   c=0, cite=c(39)),

 dict(topic="Heredity", io=IOJ,
   q="Which inherited tumour suppressor alteration is associated with malignant melanoma?",
   opts=[
     ["p16, also called INK4a",
      "Correct — one of five hereditary examples the deck lists."],
     ["Retinoblastoma protein",
      "That is associated with retinoblastoma and osteosarcoma."],
     ["Adenomatous polyposis coli",
      "That is associated with familial adenomatous polyposis."],
     ["BRCA-1",
      "That is a deoxyribonucleic acid repair gene, associated with breast cancer."]],
   c=0, cite=c(39)),

 dict(topic="Heredity", io=IOJ,
   q="What happens in familial adenomatosis polyposis syndrome, and by what age does cancer develop?",
   opts=[
     ["Hundreds to thousands of premalignant polyps young, then colon cancer by fifty",
      "Correct — five hundred to two thousand five hundred adenomatous polyps in the teens and twenties. The responsible gene is adenomatous polyposis coli."],
     ["Patients develop a single premalignant polyp in childhood, and colon cancer by age thirty",
      "The polyp burden described is in the hundreds to thousands."],
     ["Patients develop multiple neurofibromas at puberty, and sarcoma by age forty",
      "That describes the neurofibromatosis picture instead."],
     ["Patients develop skin cancer in sun-exposed areas from early childhood",
      "That is xeroderma pigmentosum."]],
   c=0, cite=c(39)),

 dict(topic="Heredity", io=IOJ,
   q="Which inherited defect underlies xeroderma pigmentosum, and what is the consequence?",
   opts=[
     ["Defective repair genes, so ultraviolet B damage cannot be repaired",
      "Correct — the consequence is an increased risk of skin cancer in sun-exposed areas. It is a repair-gene disease rather than a tumour suppressor one."],
     ["Defective tumour suppressor genes, so cell growth cannot be inhibited; increased risk of nervous system tumours",
      "That describes the neurofibromatosis genes."],
     ["Defective apoptosis genes, so damaged cells cannot self destruct; increased risk of lymphoma",
      "Apoptosis genes are a category, but this is not the disease attached to them here."],
     ["Defective protooncogenes, so growth signalling is lost; increased risk of aplasia",
      "Loss of protooncogene function would not produce cancer this way."]],
   c=0, cite=c(40)),

 dict(topic="Heredity", io=IOJ,
   q="Which cancer patients are described as sometimes carrying an inherited mutation of BRCA-1 or BRCA-2?",
   opts=[
     ["A minority of breast cancer patients",
      "Correct — the deck is careful to say a minority, not most."],
     ["The majority of breast cancer patients",
      "The deck specifies a minority."],
     ["All patients with familial adenomatous polyposis",
      "That syndrome follows from adenomatous polyposis coli."],
     ["All patients with xeroderma pigmentosum",
      "That follows from a different set of repair genes."]],
   c=0, cite=c(40)),

 dict(topic="Neurofibromatosis genes", io=IOJ,
   q="What do inherited alterations of NF-1 and NF-2 produce?",
   opts=[
     ["Neurofibromatosis, with nervous system tumours",
      "Correct — NF-1 gives type 1 and NF-2 gives type 2, and both are associated with a variety of tumours."],
     ["Retinoblastoma and osteosarcoma",
      "Those follow from the retinoblastoma protein."],
     ["Familial adenomatous polyposis and early colon cancer",
      "That follows from adenomatous polyposis coli."],
     ["Malignant melanoma",
      "That follows from p16."]],
   c=0, cite=c(39)),

 dict(topic="Staging", io=IOL,
   q="What are the purposes of cancer staging?",
   opts=[
     ["Extent of spread, prognosis, and guiding management",
      "Correct — all three. Staging answers a different question from histological grading."],
     ["To measure how closely the tumour resembles the normal tissue it came from",
      "That is grading rather than staging."],
     ["To identify which gene alterations caused the tumour",
      "Staging describes extent, not causation."],
     ["To determine whether the tumour is benign or malignant",
      "That question is answered before staging begins."]],
   c=0, cite=c(41)),

 dict(topic="Staging", io=IOL,
   q="On what three things is staging based?",
   opts=[
     ["Primary lesion size, regional nodal spread, and blood-borne metastases",
      "Correct — which is exactly what T, N and M stand for."],
     ["Degree of differentiation, mitotic rate, and nuclear pleomorphism",
      "Those are the components of histological grading."],
     ["Patient age, performance status, and duration of symptoms",
      "None of these is part of the staging basis described."],
     ["Tissue of origin, whether mesenchymal or epithelial, and the naming rule that follows",
      "That is classification rather than staging."]],
   c=0, cite=c(41)),

 dict(topic="TNM", io=IOL,
   q="What does Tis mean in the TNM system?",
   opts=[
     ["The lesion has not invaded through the basement membrane",
      "Correct — 'is' refers to in situ, and it is the same threshold the dysplasia diagram turns on."],
     ["The lesion is too small to be measured accurately",
      "Size categories are T1 upwards; Tis is about the basement membrane."],
     ["The primary tumour cannot be assessed",
      "That would be Tx rather than Tis."],
     ["There is no evidence of a primary tumour",
      "That would be T0."]],
   c=0, cite=c(42)),

 dict(topic="TNM", io=IOL,
   q="What do T1 through T3 or higher indicate?",
   opts=[
     ["Increasing size, and increasing depth of invasion",
      "Correct — and for some cancers depth of invasion matters more than size."],
     ["Increasing number of regional lymph nodes involved",
      "That is the N category."],
     ["Increasing number of distant metastatic deposits",
      "That is the M category."],
     ["Decreasing degree of differentiation",
      "Differentiation is graded, not staged."]],
   c=0, cite=c(42)),

 dict(topic="TNM", io=IOL,
   q="What do Nx, N0 and N1 to N2 or higher each mean?",
   opts=[
     ["Cannot be assessed; none; increasing number and range involved",
      "Correct — x always means cannot be assessed, 0 always means none found, and the numbers rise with the number and range of nodes involved."],
     ["Nx, no regional nodal metastasis; N0, nodes cannot be assessed; N1 upwards, distant metastasis",
      "The meanings of x and 0 are swapped, and N never denotes distant spread."],
     ["Nx, nodes not yet sampled; N0, one node involved; N1 upwards, two or more nodes",
      "N0 means no nodal metastasis rather than one node."],
     ["Nx, nodes removed surgically; N0, nodes present but normal in size; N1 upwards, enlarged nodes",
      "Nodal staging is about metastatic involvement, not node size or removal."]],
   c=0, cite=c(42)),

 dict(topic="TNM", io=IOL,
   q="What do Mx, M0 and M1 mean?",
   opts=[
     ["Mx, distant metastasis cannot be assessed; M0, no distant metastasis; M1, distant metastasis",
      "Correct — the same x-and-0 convention as the nodal category."],
     ["Mx, no distant metastasis; M0, metastasis cannot be assessed; M1, regional nodal metastasis",
      "The x and 0 meanings are swapped, and M never denotes regional nodes."],
     ["Mx, multiple metastases; M0, one metastasis; M1, no metastasis",
      "None of these matches the convention."],
     ["Mx, metastasis of unknown primary; M0, metastasis to one organ; M1, metastasis to several",
      "The categories are about whether distant metastasis is present, not how many organs."]],
   c=0, cite=c(42)),

 dict(topic="TNM", io=IOL,
   q="What important caveat does the deck attach to TNM definitions?",
   opts=[
     ["They are cancer-specific; for some cancers depth of invasion matters more than size",
      "Correct — which is why the slide's example table is for one named cancer rather than all."],
     ["They are identical across every cancer, which is what makes the system universal",
      "The deck says the opposite: the definitions are cancer-specific."],
     ["They apply only to epithelial malignancies and not to sarcomas",
      "No such restriction is stated."],
     ["They replace histological grading, which is no longer used",
      "Staging and grading answer different questions and both remain."]],
   c=0, cite=c(42)),
]
