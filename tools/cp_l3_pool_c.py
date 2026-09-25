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
   q="How is carcinogenesis overall characterized?",
   opts=[
     ["A multistep process, resulting from damage to multiple normal regulatory genes",
      "Correct — a single mutation is not enough; the damage accumulates."],
     ["A single-step process, resulting from one mutation in one regulatory gene",
      "One mutation is not enough; a cell must lose growth control, escape apoptosis, evade immune recognition and acquire a blood supply, which requires several genes to fail."],
     ["A purely inherited process, requiring a germline mutation to begin",
      "Damaged genes may be inherited AND/OR acquired."],
     ["A purely environmental process, requiring an external carcinogen",
      "Inheritance is one of the named sources of damaged genes."]],
   c=0, cite=c(28)),

 dict(topic="Carcinogenesis", io=IOG,
   q="Where does the gene damage in carcinogenesis come from?",
   opts=[
     ["Inherited, and/or acquired from chemicals, radiation or microbes",
      "Correct — damaged genes may be inherited or develop from chemical carcinogens, ultraviolet and ionizing radiation, and microbes: viruses and one bacterium."],
     ["It is always inherited through the germline and never acquired during life",
      "Gene damage is not always inherited; chemical carcinogens, radiation, and microbes also damage regulatory genes during life."],
     ["It is always acquired during life and never inherited",
      "Gene damage is not always acquired; damaged regulatory genes may be inherited, as with BRCA-1 and BRCA-2."],
     ["It arises only from errors during deoxyribonucleic acid replication",
      "Gene damage may be inherited or come from chemical carcinogens, radiation, and microbes, not only from replication errors."]],
   c=0, cite=c(28)),

 dict(topic="Protooncogenes", io=IOG,
   q="What do protooncogenes normally do, and what are they?",
   opts=[
     ["They promote REGULATED cell growth",
      "Correct — the word to hold onto is regulated. They are growth factors, growth factor receptors, nuclear regulatory proteins, and proteins involved in signal transduction. Mutation removes the regulation."],
     ["They inhibit cell growth; they include neurofibromin, retinoblastoma protein and the adenomatous polyposis coli protein",
      "Those are tumor suppressor genes, the opposite category."],
     ["They repair damaged deoxyribonucleic acid; they include BRCA-1 and BRCA-2",
      "That is the third category, the repair genes."],
     ["They cause cells with damaged deoxyribonucleic acid to self destruct",
      "That is the fourth category, the apoptosis genes."]],
   c=0, cite=c(29)),

 dict(topic="Oncogenes", io=IOG,
   q="What happens when a protooncogene mutates?",
   opts=[
     ["It becomes an oncogene, which encodes oncoproteins that promote continued uncontrolled growth",
      "Correct — mutation converts a protooncogene to an oncogene, whose oncoproteins promote continued growth in an uncontrolled manner."],
     ["It becomes a tumor suppressor gene, which then inhibits cell growth excessively",
      "Tumor suppressor genes are a separate category that inhibits cell growth; a mutated protooncogene becomes an oncogene that drives uncontrolled growth."],
     ["It becomes a repair gene, which then introduces errors into the genome",
      "Genes promoting repair of damaged deoxyribonucleic acid are a separate category; a mutated protooncogene becomes an oncogene instead."],
     ["It becomes silent, so the cell loses its ability to grow at all",
      "Mutation does not silence growth; it converts the protooncogene to an oncogene that drives uncontrolled growth."]],
   c=0, cite=c(29)),

 dict(topic="Tumor suppressors", io=IOG,
   q="Which statement correctly describes tumor suppressor genes?",
   opts=[
     ["They inhibit cell growth; the examples are NF-1, NF-2, retinoblastoma and adenomatous polyposis coli",
      "Correct — losing them removes a brake rather than adding an accelerator."],
     ["They promote regulated cell growth; the examples are growth factors and their receptors",
      "Promoting regulated growth describes protooncogenes, such as growth factors and their receptors; tumor suppressor genes inhibit growth."],
     ["They repair damaged deoxyribonucleic acid; the examples are BRCA-1 and BRCA-2",
      "BRCA-1 and BRCA-2 are repair genes for damaged deoxyribonucleic acid; tumor suppressor genes inhibit cell growth."],
     ["They trigger apoptosis in damaged cells; no specific examples are named",
      "Genes promoting self destruction of damaged cells form a separate category; tumor suppressor genes inhibit cell growth."]],
   c=0, cite=c(29)),

 dict(topic="Repair genes", io=IOG,
   q="Which genes promote repair of damaged deoxyribonucleic acid?",
   opts=[
     ["BRCA-1 and BRCA-2",
      "Correct — a minority of breast cancer patients carry an inherited mutation in one of them."],
     ["NF-1 and NF-2",
      "NF-1 and NF-2 (neurofibromatosis types 1 and 2) are tumor suppressor genes, which inhibit cell growth rather than repair damaged deoxyribonucleic acid."],
     ["Retinoblastoma and adenomatous polyposis coli",
      "Retinoblastoma and adenomatous polyposis coli are tumor suppressor genes that inhibit cell growth; the repair genes are BRCA-1 and BRCA-2."],
     ["p16 and p53",
      "p16 is a tumor suppressor linked to malignant melanoma, and p53 is needed to promote self destruction of mutated cells; neither is a repair gene."]],
   c=0, cite=c(30)),

 dict(topic="Apoptosis genes", io=IOG,
   q="Why are genes promoting self destruction of cells with damaged deoxyribonucleic acid necessary?",
   opts=[
     ["To stop the damage becoming permanent in dividing cells",
      "Correct — apoptosis prevents a mutation being carried on into the daughter cells."],
     ["To limit the total number of cells an organ can contain",
      "Limiting organ size is not the purpose; apoptosis genes stop damage from becoming permanent in dividing cells."],
     ["To supply nutrients to neighboring cells as they proliferate",
      "Apoptosis genes have no nutrient role; their job is to make damaged cells self destruct before the damage becomes permanent."],
     ["To slow the rate at which stem cells commit to differentiation",
      "Commitment to differentiation belongs to stem cell kinetics; apoptosis genes make damaged cells self destruct so the damage is not continued in dividing cells."]],
   c=0, cite=c(30)),

 dict(topic="Gene categories", io=IOG,
   q="How many categories of gene alteration in carcinogenesis are there, and what are they?",
   opts=[
     ["Four",
      "Correct — protooncogenes, tumor suppressor genes, genes promoting repair of damaged deoxyribonucleic acid, and genes promoting apoptosis. Two are gains of function and two are losses."],
     ["Two: protooncogenes and tumor suppressor genes",
      "Those are the first two of four."],
     ["Three: protooncogenes, tumor suppressor genes, and repair genes",
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
      "Sustained or enhanced proliferation of damaged cells is promotion; initiators cause the permanent damage first."],
     ["They repair damage already caused by another carcinogen",
      "Initiators cause permanent deoxyribonucleic acid damage rather than repairing it; they start chemical carcinogenesis."],
     ["They trigger apoptosis in cells with damaged genomes",
      "Triggering apoptosis protects against damaged cells; initiators instead cause permanent deoxyribonucleic acid damage."]],
   c=0, cite=c(31)),

 dict(topic="Promotion", io=IOH,
   q="What do promoters do?",
   opts=[
     ["They drive proliferation of cells already damaged by an initiator",
      "Correct — sustained or enhanced proliferation raises the risk of successive mutations leading to cancer."],
     ["They cause the permanent deoxyribonucleic acid damage that starts the process",
      "Causing permanent deoxyribonucleic acid damage is initiation; promoters drive proliferation of cells already damaged."],
     ["They repair the deoxyribonucleic acid damage caused by initiators",
      "Promoters do not repair damage; they cause sustained or enhanced proliferation of cells an initiator has damaged."],
     ["They cause tumor cells to detach and enter the circulation",
      "Detachment and entry into the circulation belong to metastasis; promoters drive proliferation of initiated cells."]],
   c=0, cite=c(31)),

 dict(topic="Chemical carcinogens", io=IOH,
   q="Which statement correctly identifies the carcinogens produced by the combustion of tobacco?",
   opts=[
     ["Polycyclic aromatic hydrocarbons, causing bladder and lung cancer",
      "Correct — among the most powerful carcinogens known, and tobacco smoke contains numerous others besides."],
     ["Aromatic amines, causing bladder and lung cancer; among the most powerful carcinogens known",
      "Aromatic amines are classically emphasized in occupational bladder cancer; the tobacco combustion products are polycyclic aromatic hydrocarbons."],
     ["Nitrosamines, causing gastric and esophageal cancer",
      "The key tobacco combustion products are polycyclic aromatic hydrocarbons, which cause bladder and lung cancer rather than gastric cancer."],
     ["Aflatoxins, causing hepatocellular carcinoma",
      "Aflatoxin is not a tobacco combustion product; burning tobacco yields polycyclic aromatic hydrocarbons, among the most powerful carcinogens known."]],
   c=0, cite=c(31)),

 dict(topic="Chemical carcinogens", io=IOH,
   q="Which chemical carcinogens are classically emphasized in occupational bladder cancer?",
   opts=[
     ["Aromatic amines",
      "Correct — aromatic amines are classically emphasized in occupational bladder cancer, whereas tobacco supplies polycyclic aromatic hydrocarbons."],
     ["Polycyclic aromatic hydrocarbons",
      "Those are the tobacco combustion products, which also cause bladder cancer."],
     ["Alkylating agents",
      "Alkylating agents are not the classic occupational bladder carcinogen; aromatic amines are."],
     ["Asbestos fibers",
      "Asbestos fibers are not the classic occupational bladder carcinogen; aromatic amines are."]],
   c=0, cite=c(31)),

 dict(topic="Human papillomavirus", io=IOI,
   q="Which human papillomavirus subtypes most commonly cause cervical cancer?",
   opts=[
     ["Types 16 and 18",
      "Correct — of many genetic subtypes, these two cause the majority."],
     ["Types 6 and 11",
      "Types 6 and 11 are not the cervical cancer subtypes; high-risk types 16 and 18 cause the majority of cervical cancers."],
     ["Types 1 and 2",
      "Types 1 and 2 are not the cervical cancer subtypes; of many genetic subtypes, types 16 and 18 most commonly cause it."],
     ["Types 31 and 33",
      "Types 31 and 33 are not the leading cervical cancer subtypes; types 16 and 18 cause the majority of cervical cancers."]],
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
      "While the virus stays episomal the infection remains productive rather than transforming; it is integration that disrupts viral regulation and drives E6 and E7 overproduction."],
     ["It causes the host to amplify its own p53 and retinoblastoma genes",
      "The viral proteins block those host proteins rather than amplify them."],
     ["It induces chronic inflammation, which raises transcription of all viral genes",
      "Chronic inflammation is the mechanism emphasized for hepatitis B and Helicobacter."]],
   c=0, cite=c(32)),

 dict(topic="Human papillomavirus", io=IOI,
   q="Besides cervical cancer, which malignancies is high-risk human papillomavirus associated with?",
   opts=[
     ["Anal, vulvar, vaginal, penile and oropharyngeal cancer",
      "Correct — high-risk human papillomavirus is associated with all five in addition to cervical cancer, the oropharyngeal one being a squamous cell carcinoma."],
     ["Hepatocellular carcinoma and gastric adenocarcinoma",
      "Those belong to the hepatitis viruses and Helicobacter pylori respectively."],
     ["Nasopharyngeal carcinoma and certain B cell lymphomas",
      "Nasopharyngeal carcinoma and certain B cell lymphomas follow Epstein Barr virus, which immortalizes B lymphocytes."],
     ["Retinoblastoma and osteosarcoma",
      "Those are associated with the retinoblastoma protein under heredity."]],
   c=0, cite=c(37)),

 dict(topic="Epstein Barr virus", io=IOI,
   q="Which statement correctly describes Epstein Barr virus in carcinogenesis?",
   opts=[
     ["B cell lymphomas and nasopharyngeal carcinoma; it infects B lymphocytes",
      "Correct — it immortalizes them, which is the key step, and it also infects epithelial cells of the oropharynx."],
     ["Hepatocellular carcinoma; it infects hepatocytes and causes chronic injury with regeneration",
      "Chronic liver injury with regeneration leading to hepatocellular carcinoma describes hepatitis B and hepatitis C."],
     ["Cervical carcinoma; it infects cervical epithelium and integrates its genome",
      "Integrating into cervical epithelium and causing cervical cancer describes human papillomavirus, not Epstein Barr virus."],
     ["Gastric adenocarcinoma and mucosa-associated lymphoid tissue lymphoma; it colonizes the stomach",
      "Colonizing the stomach and causing gastric cancers describes Helicobacter pylori, a Gram-negative bacterium, not a virus."]],
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
      "The virus persists latently for life rather than being cleared; what normal immunity prevents is the immortalized B cells progressing to lymphoma."]],
   c=0, cite=c(33)),

 dict(topic="Hepatitis B", io=IOI,
   q="By what mechanism does hepatitis B virus lead to hepatocellular carcinoma?",
   opts=[
     ["Chronic injury drives regeneration; it also binds p53",
      "Correct — continuous hepatocyte death forces continuous regeneration, and every round of division risks a replication error, while the viral X protein additionally binds and disables p53."],
     ["It integrates its genome so as to overproduce E6 and E7",
      "Those are human papillomavirus proteins."],
     ["It infects and immortalizes B lymphocytes",
      "That is Epstein Barr virus."],
     ["It colonizes the stomach and causes atrophic gastritis",
      "That is Helicobacter pylori."]],
   c=0, cite=c(34)),

 dict(topic="Hepatitis B", io=IOI,
   q="Which three processes link chronic hepatitis B infection to hepatocellular carcinoma?",
   opts=[
     ["Chronic inflammation, regenerative hyperplasia, genomic instability",
      "Correct — chronic infection causes ongoing liver cell injury, stimulating continuous regenerative proliferation of liver cells that are at risk for genetic mutations."],
     ["Initiation, promotion, and progression",
      "Initiation and promotion are steps of chemical carcinogenesis; hepatitis B works through chronic injury and regeneration."],
     ["Pleomorphism, abnormal nuclei, and abnormal differentiation",
      "Pleomorphism, abnormal nuclei, and abnormal differentiation are histological features of malignancy, not the hepatitis B triad."],
     ["Self-renewal, immortality, and differentiation capacity",
      "Self-renewal, immortality, and differentiation capacity describe stem cells, not how hepatitis B causes liver cancer."]],
   c=0, cite=c(34)),

 dict(topic="Helicobacter pylori", io=IOI,
   q="Which statement correctly describes Helicobacter pylori?",
   opts=[
     ["A Gram-negative bacterium causing chronic gastritis",
      "Correct — it colonizes the stomach and may lead to atrophic gastritis and intestinal metaplasia. It is the one bacterium among the microbial causes of cancer."],
     ["A Gram-positive bacterium that colonizes the stomach, causing acute ulceration and perforation",
      "It is Gram-negative, and it causes chronic gastritis rather than acute ulceration and perforation."],
     ["A virus that integrates its genome into gastric epithelial cells",
      "Helicobacter pylori is not a virus; it is a Gram-negative bacterium that colonizes the stomach and causes chronic gastritis."],
     ["A fungus that colonizes the gastric mucosa in immunosuppressed patients",
      "Helicobacter pylori is not a fungus; it is a Gram-negative bacterium that colonizes the stomach and causes chronic gastritis."]],
   c=0, cite=c(35)),

 dict(topic="Helicobacter pylori", io=IOI,
   q="Which two malignancies is Helicobacter pylori associated with?",
   opts=[
     ["Gastric adenocarcinoma and mucosa-associated lymphoid tissue lymphoma",
      "Correct — chronic Helicobacter pylori gastritis is associated with gastric adenocarcinoma and MALT (mucosa-associated lymphoid tissue) lymphoma."],
     ["Hepatocellular carcinoma and cholangiocarcinoma",
      "Hepatocellular carcinoma follows chronic hepatitis B and hepatitis C infection; Helicobacter pylori is linked to gastric cancers."],
     ["Nasopharyngeal carcinoma and Burkitt lymphoma",
      "Nasopharyngeal carcinoma and B cell lymphomas follow Epstein Barr virus, which immortalizes B lymphocytes."],
     ["Cervical carcinoma and oropharyngeal squamous cell carcinoma",
      "Cervical cancer and oropharyngeal squamous cell carcinoma follow high-risk human papillomavirus, not Helicobacter pylori."]],
   c=0, cite=c(35)),

 dict(topic="Helicobacter pylori", io=IOI,
   q="What does eradicating Helicobacter pylori do to cancer risk?",
   opts=[
     ["It reduces gastric cancer risk, and some early MALT lymphomas regress",
      "Correct — eradicating Helicobacter pylori with antibiotics can reduce gastric cancer risk and may induce regression of some early MALT (mucosa-associated lymphoid tissue) lymphomas."],
     ["It has no effect on cancer risk once colonization has occurred",
      "Eradication of Helicobacter pylori with antibiotics can reduce the risk of gastric cancer, so colonization does not fix the risk for good."],
     ["It increases the risk, because the inflammatory response is protective",
      "Chronic inflammation raises epithelial cell turnover and the chance of acquiring mutations, so it drives cancer rather than protecting against it."],
     ["It reverses established gastric adenocarcinoma",
      "Eradication may induce regression of some early MALT (mucosa-associated lymphoid tissue) lymphomas, not of established gastric adenocarcinoma."]],
   c=0, cite=c(35)),

 dict(topic="Hepatitis C", io=IOI,
   q="How does hepatitis C lead to hepatocellular carcinoma, and in whom does it usually develop?",
   opts=[
     ["Repeated cell death and proliferation; usually, but not always, in cirrhosis",
      "Correct — chronic hepatitis causes ongoing injury, inflammation and regeneration, and the cycles accumulate mutations. Most cases arise in cirrhosis, but cancer can occasionally occur without it."],
     ["Repeated cycles of cell death and proliferation accumulate mutations; cirrhosis is an absolute prerequisite",
      "Cirrhosis is the usual setting but not an absolute prerequisite; cancer occasionally arises in a chronically inflamed liver that has not yet become cirrhotic."],
     ["The virus integrates its genome and overproduces oncoproteins; cirrhosis is irrelevant",
      "Genome integration with oncoprotein production is human papillomavirus."],
     ["The virus immortalizes hepatocytes directly, without chronic inflammation",
      "Chronic hepatitis with ongoing injury and regeneration is the described mechanism."]],
   c=0, cite=c(36)),

 dict(topic="Radiation", io=IOI,
   q="Which forms of radiation cause cancer?",
   opts=[
     ["Ultraviolet B, and ionizing radiation",
      "Correct — both ultraviolet B and ionizing radiation cause cancer; unrepaired ultraviolet B mutations explain the skin cancers of xeroderma pigmentosum."],
     ["Ultraviolet A only, together with infrared radiation",
      "The radiation forms that cause cancer are ultraviolet B and ionizing radiation; ultraviolet A and infrared are not among them."],
     ["Microwave and radiofrequency radiation",
      "The radiation forms that cause cancer are ultraviolet B and ionizing radiation, not microwave or radiofrequency radiation."],
     ["Ionizing radiation only, with no ultraviolet contribution",
      "Ultraviolet B causes cancer alongside ionizing radiation, as the skin cancers in sun-exposed areas of xeroderma pigmentosum show."]],
   c=0, cite=c(38)),

 dict(topic="Heredity", io=IOJ,
   q="Which tumors are associated with an inherited alteration of the retinoblastoma protein?",
   opts=[
     ["Retinoblastoma, a rare childhood tumor of the eye, and osteosarcoma",
      "Correct — the same tumor suppressor, two very different tumors."],
     ["Neurofibromatosis types 1 and 2, with tumors of the central and peripheral nervous system",
      "Nervous system tumors follow NF-1 and NF-2 (neurofibromatosis types 1 and 2), not retinoblastoma protein alteration."],
     ["Malignant melanoma",
      "Malignant melanoma follows inherited p16 (INK4a) alteration, not retinoblastoma protein alteration."],
     ["Familial adenomatous polyposis and colon cancer",
      "Familial adenomatous polyposis and colon cancer follow adenomatous polyposis coli, not the retinoblastoma protein."]],
   c=0, cite=c(39)),

 dict(topic="Heredity", io=IOJ,
   q="Which inherited tumor suppressor alteration is associated with malignant melanoma?",
   opts=[
     ["p16, also called INK4a",
      "Correct — p16 (INK4a) is an inherited tumor suppressor alteration associated with malignant melanoma."],
     ["Retinoblastoma protein",
      "Retinoblastoma protein alteration causes retinoblastoma and osteosarcoma; malignant melanoma follows p16 (INK4a)."],
     ["Adenomatous polyposis coli",
      "Adenomatous polyposis coli alteration causes familial adenomatosis polyposis; p16 (INK4a) is linked to malignant melanoma."],
     ["BRCA-1",
      "That is a deoxyribonucleic acid repair gene, associated with breast cancer."]],
   c=0, cite=c(39)),

 dict(topic="Heredity", io=IOJ,
   q="Which statement describes familial adenomatosis polyposis syndrome?",
   opts=[
     ["Hundreds to thousands of premalignant polyps young, then colon cancer by fifty",
      "Correct — five hundred to two thousand five hundred adenomatous polyps in the teens and twenties. The responsible gene is adenomatous polyposis coli."],
     ["Patients develop a single premalignant polyp in childhood, and colon cancer by age thirty",
      "Patients develop 500 to 2,500 premalignant adenomatous polyps in their teens and twenties, and colon cancer by age 50."],
     ["Patients develop multiple neurofibromas at puberty, and sarcoma by age forty",
      "Nervous system tumors follow neurofibromatosis types 1 and 2; this syndrome instead produces hundreds to thousands of colon polyps."],
     ["Patients develop skin cancer in sun-exposed areas from early childhood",
      "Skin cancer in sun-exposed areas is xeroderma pigmentosum, an inherited inability to repair mutations caused by ultraviolet B radiation."]],
   c=0, cite=c(39)),

 dict(topic="Heredity", io=IOJ,
   q="Which statement correctly describes the inherited defect in xeroderma pigmentosum?",
   opts=[
     ["Defective repair genes, so ultraviolet B damage cannot be repaired",
      "Correct — the consequence is an increased risk of skin cancer in sun-exposed areas. It is a repair-gene disease rather than a tumor suppressor one."],
     ["Defective tumor suppressor genes, so cell growth cannot be inhibited; increased risk of nervous system tumors",
      "Growth-inhibiting tumor suppressors such as NF-1 and NF-2 underlie nervous system tumors; xeroderma pigmentosum is a repair-gene defect."],
     ["Defective apoptosis genes, so damaged cells cannot self destruct; increased risk of lymphoma",
      "Xeroderma pigmentosum is a defect of repair genes, not apoptosis genes, and it raises skin cancer risk rather than lymphoma risk."],
     ["Defective protooncogenes, so growth signaling is lost; increased risk of aplasia",
      "Xeroderma pigmentosum involves defective repair genes; protooncogenes cause cancer when mutated into oncogenes, not when lost."]],
   c=0, cite=c(40)),

 dict(topic="Heredity", io=IOJ,
   q="Which cancer patients may carry an inherited mutation of BRCA-1 or BRCA-2?",
   opts=[
     ["A minority of breast cancer patients",
      "Correct — a minority of breast cancer patients have an inherited mutation of these deoxyribonucleic acid repair genes."],
     ["The majority of breast cancer patients",
      "Only a minority of breast cancer patients carry an inherited BRCA-1 or BRCA-2 mutation, not the majority."],
     ["All patients with familial adenomatous polyposis",
      "Familial adenomatous polyposis follows an inherited alteration of the adenomatous polyposis coli tumor suppressor gene."],
     ["All patients with xeroderma pigmentosum",
      "Xeroderma pigmentosum follows inherited defective repair genes that cannot fix ultraviolet B damage; BRCA-1 and BRCA-2 relate to breast cancer."]],
   c=0, cite=c(40)),

 dict(topic="Neurofibromatosis genes", io=IOJ,
   q="What do inherited alterations of NF-1 and NF-2 produce?",
   opts=[
     ["Neurofibromatosis, with nervous system tumors",
      "Correct — NF-1 gives type 1 and NF-2 gives type 2, and both are associated with a variety of tumors."],
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
     ["To measure how closely the tumor resembles the normal tissue it came from",
      "Resemblance to the normal tissue is histological grading; staging instead describes how far the cancer has spread within the patient."],
     ["To identify which gene alterations caused the tumor",
      "Staging describes extent, based on primary lesion size, regional lymph nodes, and blood-borne metastases, not what caused the tumor."],
     ["To determine whether the tumor is benign or malignant",
      "Benign versus malignant is settled first; staging then indicates extent of spread, determines prognosis, and guides management."]],
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
     ["The primary tumor cannot be assessed",
      "That would be Tx rather than Tis."],
     ["There is no evidence of a primary tumor",
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
      "The meanings of x and 0 are swapped, and distant metastasis is scored by M, as M1, never by N."],
     ["Nx, nodes not yet sampled; N0, one node involved; N1 upwards, two or more nodes",
      "N0 means no regional lymph node metastasis, not one node involved, and Nx means the nodes cannot be assessed."],
     ["Nx, nodes removed surgically; N0, nodes present but normal in size; N1 upwards, enlarged nodes",
      "N scores metastatic involvement, not node size or removal: Nx means the nodes cannot be assessed, and N0 means no regional lymph node metastasis."]],
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
   q="What important caveat attaches to TNM (tumor, nodes, metastases) definitions?",
   opts=[
     ["They are cancer-specific; for some cancers depth of invasion matters more than size",
      "Correct — which is why a staging table applies to one named cancer rather than all."],
     ["They are identical across every cancer, which is what makes the system universal",
      "The definitions are cancer-specific, not identical across cancers."],
     ["They apply only to epithelial malignancies and not to sarcomas",
      "TNM definitions are cancer-specific rather than limited to epithelial tumors; for some cancers depth of invasion outweighs size."],
     ["They replace histological grading, which is no longer used",
      "Staging measures the extent of spread, while histological grading measures differentiation; neither replaces the other."]],
   c=0, cite=c(42)),
]
