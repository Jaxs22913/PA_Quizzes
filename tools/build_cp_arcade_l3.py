#!/usr/bin/env python3
"""Add the Clin Path I Lecture 3 (Abnormal Cell Growth) Arcade deck to arcade.js.

One deck for one topic, joining the existing Clin Path Exam 1 group.

SCOPE: pathophysiology only, like the quizzes. Nothing here asks what you would
do about a cancer -- only what is happening in the tissue and why.
"""
import json, os, re, sys

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
# dividing cell: two nuclei separating inside a membrane
ICON = ('<circle cx="12" cy="12" r="9"/><circle cx="9" cy="12" r="2.2"/>'
        '<circle cx="15" cy="12" r="2.2"/>')

DECKS = [
 dict(id="cp-abnormal-cell-growth", name="Abnormal Cell Growth", color="accent4",
      icon=ICON, cards=[
  ["What is agenesis?", "Complete absence of an organ, because the primordial tissue never formed."],
  ["What is aplasia?", "The primordial tissue exists but fails to develop into the mature organ."],
  ["What is hypoplasia?", "Partial development of an organ, resulting in a functional deficiency."],
  ["What is atrophy?", "Shrinkage of a tissue or organ that had formed and matured normally."],
  ["What is hypertrophy?", "Enlargement of a tissue or organ due to enlargement of individual cells."],
  ["In which tissues is hypertrophy especially important?", "Permanent tissues: skeletal muscle and cardiac muscle."],
  ["What is metaplasia?", "Change of one cell type to another under chronic irritation or injury; a change in differentiation."],
  ["Which epithelial change does the deck use as its metaplasia example?", "Bladder transitional epithelium becoming squamous epithelium."],
  ["Which four features define dysplasia?", "Disordered epithelial growth, varied cell size and shape, lost architectural orientation, darker and larger nuclei."],
  ["Why is dysplasia called precancerous?", "It may progress to cancer."],
  ["What separates carcinoma in situ from invasive cancer?", "The basement membrane. Carcinoma in situ has not invaded through it."],
  ["What single word defines a neoplasm?", "Autonomously. It is self-perpetuating without physiologic growth stimuli."],
  ["From how many cells is a neoplasm derived?", "One cell, which underwent a genetic alteration. A tumour is a clone."],
  ["What are the two components of a neoplasm?", "Parenchyma, the proliferating neoplastic cells; and stroma, the connective tissue and blood vessels."],
  ["What is cancer?", "A malignant neoplasm."],
  ["Where does the word cancer come from?", "The Latin for crab, because it adheres to any tissue it seizes upon and reaches out with claws."],
  ["What is a metastasis?", "A portion of a cancer that has migrated from the primary site to other sites."],
  ["What does the degree of differentiation measure?", "How closely a neoplasm resembles comparable normal cells in appearance and function."],
  ["Name the four grades of differentiation.", "Well differentiated, moderately differentiated, poorly differentiated, anaplasia."],
  ["What does anaplasia mean?", "Lack of differentiation."],
  ["What is the difference between grading and staging?", "Grading asks what it looks like; staging asks how far it has got."],
  ["Name three features of a benign tumour's border and behaviour.", "Well circumscribed border, compresses surrounding tissue, often has a fibrous capsule."],
  ["How does a malignant tumour relate to surrounding tissue?", "It has a ragged border and infiltrates and invades, rather than compressing."],
  ["What does the deck say about differentiation in malignant tumours?", "Various degrees of differentiation, not uniformly poor."],
  ["Which four histological features move a tumour towards malignancy?", "Pleomorphism, abnormal nuclei, mitoses, and abnormal differentiation."],
  ["What are the defining properties of a stem cell?", "Unlimited self-renewal and cellular immortality, but a relatively low rate of proliferation."],
  ["What happens to proliferation after a cell commits to differentiation?", "It can be dramatic, but those differentiated cells have a limited life-span."],
  ["What does abnormal differentiation do to the cell pools in cancer?", "It puts more cells in the proliferative pool at the expense of the maturation pool."],
  ["Why does a tumour mass outgrow normal tissue?", "A higher proliferative fraction together with a lower rate of cell loss."],
  ["How does the deck qualify the cancer stem cell idea?", "As a conceptual framework rather than an absolute explanation."],
  ["Through which vessels does haematogenous spread typically occur?", "Veins, especially the portal vein and the inferior vena cava."],
  ["Why do portal vein and inferior vena cava spread reach liver and lungs?", "Because those are the organs each vein drains into."],
  ["What is the first step of haematogenous spread?", "Tumour cells separate from each other and degrade intercellular tissue with enzymes."],
  ["Where do tumour cells enter the lymphatic system?", "At the tumour margin, then they follow the natural route of lymphatic drainage."],
  ["Which cavities can be seeded by tumour?", "Pericardial, pleural, peritoneal and joint cavities, and the subarachnoid space."],
  ["In which cavity does seeding most commonly occur?", "The peritoneal cavity."],
  ["Is metastatic spread random?", "No. It is determined by venous blood flow, specific receptors, and genetically determined fitness."],
  ["Which three hurdles follow penetration of the vasculature?", "Penetration of vasculature, survival in the circulation, and survival in a new organ."],
  ["What tissues are mesenchymal tumours derived from?", "Supportive tissue: connective tissue, adipose, cartilage, smooth and striated muscle, bone."],
  ["What is a malignant tumour of mesenchymal origin called?", "A sarcoma."],
  ["What is a malignant tumour of epithelial origin called?", "A carcinoma."],
  ["What is an adenoma?", "A benign epithelial tumour with a glandular pattern, or derived from a gland."],
  ["What can an adenoma sometimes do?", "Secrete the hormone or hormones produced by its gland of origin."],
  ["What is a papilloma?", "A tumour producing visible finger-like or warty projections from an epithelial surface."],
  ["What is a carcinoma with a glandular growth pattern called?", "An adenocarcinoma."],
  ["What is a carcinoma with squamous cell differentiation called?", "A squamous cell carcinoma."],
  ["How does the deck characterise carcinogenesis overall?", "A multistep process, resulting from damage to multiple normal regulatory genes."],
  ["What do protooncogenes normally do?", "Promote regulated cell growth."],
  ["What kinds of proteins are protooncogenes?", "Growth factors, growth factor receptors, nuclear regulatory proteins, and signal transduction proteins."],
  ["What happens when a protooncogene mutates?", "It becomes an oncogene, encoding oncoproteins that promote continued uncontrolled growth."],
  ["What do tumour suppressor genes do?", "Inhibit cell growth."],
  ["Name four tumour suppressor genes from the deck.", "NF-1, NF-2, retinoblastoma, and adenomatous polyposis coli."],
  ["Which genes promote repair of damaged deoxyribonucleic acid?", "BRCA-1 and BRCA-2."],
  ["Why are apoptosis genes necessary?", "To stop the damage becoming permanent in dividing cells."],
  ["How many categories of gene alteration does the deck describe?", "Four: protooncogenes, tumour suppressors, repair genes, and apoptosis genes."],
  ["What do initiators do in chemical carcinogenesis?", "Cause permanent damage to deoxyribonucleic acid."],
  ["What do promoters do?", "Cause sustained or enhanced proliferation of cells already damaged by an initiator."],
  ["Which carcinogens come from the combustion of tobacco?", "Polycyclic aromatic hydrocarbons, causing bladder and lung cancer."],
  ["Which chemicals are emphasised in occupational bladder cancer?", "Aromatic amines."],
  ["Which human papillomavirus subtypes most commonly cause cervical cancer?", "Types 16 and 18."],
  ["What does human papillomavirus E6 block, and why does that matter?", "p53, which is needed to promote self destruction of mutated cells."],
  ["What does human papillomavirus E7 block, and why does that matter?", "Retinoblastoma protein, which is needed to inhibit cell growth."],
  ["How does human papillomavirus produce excess E6 and E7?", "It integrates its viral deoxyribonucleic acid into the host cell genome."],
  ["Besides cervical, which cancers is high-risk human papillomavirus associated with?", "Anal, vulvar, vaginal, penile, and oropharyngeal squamous cell carcinoma."],
  ["Which cancers is Epstein Barr virus associated with?", "Certain B cell lymphomas and nasopharyngeal carcinoma."],
  ["What does Epstein Barr virus do to B lymphocytes?", "Infects and immortalizes them."],
  ["What happens to Epstein Barr infection in a patient with normal immune function?", "No immortalization; they are asymptomatic or have self-limited infectious mononucleosis."],
  ["How does hepatitis B lead to hepatocellular carcinoma?", "Chronic injury drives continuous regeneration; it also encodes a protein that binds p53."],
  ["Which three concepts does the hepatitis B slide emphasise?", "Chronic inflammation, regenerative hyperplasia, and genomic instability."],
  ["In whom does hepatitis C associated liver cancer usually develop?", "Patients with cirrhosis, although it can occasionally occur without cirrhosis."],
  ["What kind of organism is Helicobacter pylori?", "A Gram-negative bacterium that colonizes the stomach."],
  ["What does Helicobacter pylori cause in the stomach?", "Chronic gastritis, which may lead to atrophic gastritis and intestinal metaplasia."],
  ["Which two malignancies is Helicobacter pylori associated with?", "Gastric adenocarcinoma and mucosa-associated lymphoid tissue lymphoma."],
  ["What does eradicating Helicobacter pylori do?", "Reduces gastric cancer risk, and may induce regression of some early lymphomas of mucosal lymphoid tissue."],
  ["Which forms of radiation are named as causes of cancer?", "Ultraviolet B, and ionizing radiation."],
  ["Which tumours follow an inherited retinoblastoma protein alteration?", "Retinoblastoma, a rare childhood eye tumour, and osteosarcoma."],
  ["Which inherited alteration is associated with malignant melanoma?", "p16, also called INK4a."],
  ["What happens in familial adenomatosis polyposis?", "Five hundred to two thousand five hundred premalignant polyps in the teens and twenties."],
  ["By what age do familial adenomatosis polyposis patients develop colon cancer?", "By age fifty."],
  ["What is inherited in xeroderma pigmentosum?", "Defective deoxyribonucleic acid repair genes, so ultraviolet B damage cannot be repaired."],
  ["Which breast cancer patients carry inherited BRCA mutations?", "A minority of them."],
  ["What do NF-1 and NF-2 alterations produce?", "Neurofibromatosis, with tumours of the central and peripheral nervous systems."],
  ["What are the three purposes of cancer staging?", "Indicating extent of spread, determining prognosis, and guiding management."],
  ["On what three things is staging based?", "Size of the primary lesion, spread to regional lymph nodes, and blood-borne metastases."],
  ["What does Tis mean?", "The lesion has not invaded through the tissue basement membrane; in situ."],
  ["What do T1 through T3 or higher indicate?", "Increasing size of the primary lesion and increasing depth of invasion."],
  ["What does Nx mean?", "Regional lymph nodes cannot be assessed."],
  ["What does N0 mean?", "No regional lymph node metastasis."],
  ["What does M1 mean?", "Distant metastasis is present."],
  ["What convention do the letters x and 0 follow in TNM?", "x means cannot be assessed; 0 means none found."],
  ["What caveat does the deck attach to TNM definitions?", "They are cancer-specific; for some cancers depth of invasion matters more than size."],
 ], matchCards=[
  ["Primordial tissue never formed", "Agenesis"],
  ["Tissue exists, never matures", "Aplasia"],
  ["Formed normally, then shrank", "Atrophy"],
  ["Bigger cells, not more cells", "Hypertrophy"],
  ["One mature cell type becomes another", "Metaplasia"],
  ["Disordered growth, precancerous", "Dysplasia"],
  ["Lack of differentiation", "Anaplasia"],
  ["Mesenchymal origin, malignant", "Sarcoma"],
  ["Epithelial origin, malignant", "Carcinoma"],
  ["Benign, glandular, may secrete hormone", "Adenoma"],
  ["E6 blocks this", "p53"],
  ["E7 blocks this", "Retinoblastoma protein"],
  ["The one bacterium", "Helicobacter pylori"],
  ["Not through the basement membrane", "Tis"],
 ]),
]


def js_deck(d):
    def pairs(rows):
        return "\n".join('      [%s, %s],' % (json.dumps(a, ensure_ascii=False),
                                              json.dumps(b, ensure_ascii=False)) for a, b in rows)
    return ('  { id: %s, name: %s, color: %s,\n    icon: \'%s\',\n'
            '    cards: [\n%s\n    ],\n    matchCards: [\n%s\n    ] },\n') % (
        json.dumps(d["id"]), json.dumps(d["name"]), json.dumps(d["color"]),
        d["icon"], pairs(d["cards"]), pairs(d["matchCards"]))


s = open(ARCADE, encoding="utf-8").read()
if "cp-abnormal-cell-growth" in s:
    sys.exit("deck already present -- nothing to do")

for d in DECKS:
    assert 8 <= len(d["cards"])
    assert 10 <= len(d["matchCards"]) <= 14, "%s: matchCards outside target" % d["id"]
    for front, back in d["cards"]:
        assert len(back.split()) <= 26, "card back too long -> %s" % back
    for term, definition in d["matchCards"]:
        assert len(definition.split()) <= 9, "match definition too long -> %s" % definition
    for coll in (("cards", 0), ("cards", 1), ("matchCards", 0), ("matchCards", 1)):
        vals = [x[coll[1]] for x in d[coll[0]]]
        assert len(vals) == len(set(vals)), "duplicate in %s[%d] of %s" % (coll[0], coll[1], d["id"])
    # pathophysiology scope, same line the quizzes hold
    txt = " ".join(a + " " + b for a, b in d["cards"]).lower()
    for bad in ("first-line", "drug of choice", "treatment of choice", "next step"):
        assert bad not in txt, "management-scope card in a pathophysiology deck: %r" % bad

m = re.search(r"\n\];\n", s[s.index("var DEMO_DECKS"):])
end = s.index("var DEMO_DECKS") + m.start() + 1
s = s[:end] + "".join(js_deck(d) for d in DECKS) + s[end:]

OLD = '"cp-inflammation", "cp-dermatology"'
NEW = '"cp-inflammation", "cp-dermatology", "cp-abnormal-cell-growth"'
assert s.count(OLD) == 1, "Clin Path exam group not found exactly once"
s = s.replace(OLD, NEW)

open(ARCADE, "w", encoding="utf-8").write(s)
print("added %d deck(s): %d cards, %d match pairs"
      % (len(DECKS), sum(len(d["cards"]) for d in DECKS), sum(len(d["matchCards"]) for d in DECKS)))
