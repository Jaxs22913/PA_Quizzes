#!/usr/bin/env python3
"""Add the Lecture 3 (Abnormal Cell Growth) topics to the Clin Path I cram sheet.

Same colour-coded topic/table structure as the sections already there. The guide
carries the explanation; this carries only what has to be recallable cold.

Idempotent: exits without writing if the sections are already present.
"""
import os, re, sys, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 1",
                    "cp-exam-1-cram-sheet.html")

TOPICS = [
 ("acg-nonneo", "Non-Neoplastic Abnormalities of Growth", "#4a5f8a", "#e3e8f1", "#f1f4f8", "#3a4b6e", [
   ("Sort the seven into three groups", "FAILED TO DEVELOP: agenesis, aplasia, hypoplasia. CHANGED SIZE: atrophy, hypertrophy. CHANGED KIND: metaplasia, dysplasia."),
   ("Agenesis vs aplasia", "AGENESIS = complete absence, the PRIMORDIAL TISSUE NEVER FORMED. APLASIA = the primordial tissue EXISTS but fails to develop into the mature organ. A timing question."),
   ("Hypoplasia vs atrophy", "HYPOPLASIA = PARTIAL development, resulting in a FUNCTIONAL DEFICIENCY — it never got there. ATROPHY = shrinkage of a tissue or organ THAT HAD FORMED AND MATURED NORMALLY — it got there and shrank back."),
   ("Hypertrophy", "Enlargement due to enlargement of INDIVIDUAL CELLS. Especially important in PERMANENT TISSUES — skeletal and cardiac muscle — but may occur elsewhere as adaptive growth. Contrast hyperplasia: MORE cells, not BIGGER cells."),
   ("Metaplasia", "Change of ONE CELL TYPE TO ANOTHER in response to a CHRONICALLY IRRITATING OR INJURIOUS stimulus; involves a change in DIFFERENTIATION. The slide's example: bladder TRANSITIONAL epithelium → SQUAMOUS. Still orderly, still mature, NOT precancerous."),
   ("Dysplasia — four features", "DISORDERED GROWTH, typically EPITHELIAL. (1) variation in cellular SIZE AND SHAPE, (2) LOSS OF ARCHITECTURAL ORIENTATION, (3) nuclei may be DARKER AND LARGER, (4) MAY PROGRESS TO CANCER — PRECANCEROUS."),
   ("The line that matters", "Normal → mild → moderate → severe dysplasia → CARCINOMA IN SITU → INVASIVE CANCER. The BASEMENT MEMBRANE stays intact until the last panel. Everything up to and including carcinoma in situ is still above it — which is exactly what Tis means."),
 ]),
 ("acg-neoplasia", "Neoplasia, Grading & Benign vs Malignant", "#8f3f5c", "#f3e3ea", "#f9f1f4", "#702e46", [
   ("Neoplasm — the defining word", "An abnormal mass growing AUTONOMOUSLY — self-perpetuating WITHOUT PHYSIOLOGIC GROWTH STIMULI. That is what separates it from hyperplasia, which stops when the stimulus stops. Interchangeable with TUMOR."),
   ("Clonal origin", "The ENTIRE proliferating population is derived from ONE CELL that underwent a genetic alteration."),
   ("Two components", "PARENCHYMA = the proliferating neoplastic cells. STROMA = connective tissue and blood vessels. The stroma is host tissue, not part of the clone."),
   ("Cancer & metastasis", "CANCER = a MALIGNANT neoplasm. From the Latin for CRAB — 'adheres to any tissue it seizes upon', reaches out with claws. METASTASIS = the portion that has MIGRATED from the primary site."),
   ("Histological GRADING (objective k)", "Measures how closely the neoplasm RESEMBLES comparable normal cells in appearance and function. WELL differentiated (close) → MODERATELY → POORLY → ANAPLASIA (LACK of differentiation)."),
   ("GRADING vs STAGING", "GRADING asks WHAT DOES IT LOOK LIKE. STAGING asks HOW FAR HAS IT GOT. Different questions, both still used."),
   ("Benign vs malignant", "BENIGN: well circumscribed border · COMPRESSES surrounding tissue · often a FIBROUS CAPSULE · usually WELL differentiated · does NOT metastasize · SLOW growing. MALIGNANT: RAGGED border · INFILTRATES AND INVADES · VARIOUS degrees of differentiation · MAY metastasize · grows RAPIDLY."),
   ("Four histological features of malignancy", "PLEOMORPHISM · ABNORMAL NUCLEI · MITOSES · ABNORMAL DIFFERENTIATION."),
   ("Stem cell kinetics — why tumours outgrow tissue", "A stem cell has UNLIMITED SELF-RENEWAL and CELLULAR IMMORTALITY but a RELATIVELY LOW rate of proliferation; committed progeny proliferate dramatically but have a LIMITED LIFE-SPAN. In cancer, abnormal differentiation puts MORE cells in the PROLIFERATIVE pool at the expense of the MATURATION pool. Growth exceeds normal via a HIGHER PROLIFERATIVE FRACTION AND A LOWER RATE OF CELL LOSS — both halves."),
 ]),
 ("acg-spread-class", "Routes of Spread & Classification by Origin", "#3f6b5a", "#e2ede8", "#f1f6f4", "#2f5344", [
   ("Haematogenous spread", "Typically through VEINS — especially the PORTAL VEIN and INFERIOR VENA CAVA, so cancers often spread to LIVER and LUNGS respectively. Mechanism: cells SEPARATE from each other and DEGRADE INTERCELLULAR TISSUE WITH ENZYMES → invade the vessel → MULTIPLE fragments travel. One organ may carry several nodules."),
   ("Lymphatic spread", "Cancer spreads into lymphatic vessels AT THE TUMOUR MARGIN and follows the NATURAL ROUTE OF LYMPHATIC DRAINAGE. That predictability is what makes nodal staging meaningful."),
   ("Seeding", "Invasion of tumour THROUGH AN ORGAN SURFACE into a cavity. PERICARDIAL, PLEURAL, PERITONEAL cavities; JOINT cavities; SUBARACHNOID space. MOST COMMONLY THE PERITONEAL CAVITY. A cavity is defined by the membrane covering the organs plus the membrane covering the cavity wall."),
   ("Metastasis is NOT random", "Determined by: PATTERN OF VENOUS BLOOD FLOW · SPECIFIC RECEPTORS on tumour and endothelial cells · METASTATIC 'FITNESS' IS GENETICALLY DETERMINED."),
   ("The three hurdles after invasion", "PENETRATION OF VASCULATURE → SURVIVAL IN CIRCULATION → SURVIVAL IN A NEW ORGAN. Reaching the bloodstream is only the first."),
   ("THE NAMING RULE", "MESENCHYMAL (supportive tissue: connective tissue, adipose, cartilage, smooth and striated muscle, bone) → malignant = SARCOMA. EPITHELIAL → malignant = CARCINOMA."),
   ("Benign epithelial names", "ADENOMA = benign epithelial tumour with a GLANDULAR pattern or from a gland; sometimes SECRETES the hormone of its gland of origin. PAPILLOMA = visible FINGER-LIKE or WARTY projections from an epithelial surface."),
   ("Malignant epithelial names", "CARCINOMA. With glandular growth pattern = ADENOCARCINOMA. With squamous cell differentiation = SQUAMOUS CELL CARCINOMA."),
 ]),
 ("acg-carcinogenesis", "Gene Alterations, Chemicals, Microbes & Heredity", "#8a4a2c", "#f4e7e0", "#faf3ef", "#6d3921", [
   ("Carcinogenesis in one line", "A MULTISTEP process resulting from damage to MULTIPLE normal regulatory genes. Damage may be INHERITED and/or from CHEMICAL CARCINOGENS, ULTRAVIOLET AND IONIZING RADIATION, or MICROBIAL ORGANISMS (viruses and a bacterium)."),
   ("FOUR categories of gene alteration", "(1) PROTOONCOGENES — promote REGULATED growth (growth factors, their receptors, nuclear regulatory proteins, signal transduction proteins); mutation → ONCOGENES → ONCOPROTEINS → UNCONTROLLED growth. (2) TUMOUR SUPPRESSOR GENES — INHIBIT growth; NF-1, NF-2, RB, APC. (3) DNA REPAIR GENES — BRCA-1, BRCA-2. (4) APOPTOSIS GENES — make damaged cells self destruct, PREVENTING damage becoming permanent in dividing cells."),
   ("Chemical carcinogenesis — two steps", "INITIATION (initiators): chemicals cause PERMANENT DAMAGE TO DNA. PROMOTION (promoters): SUSTAINED OR ENHANCED PROLIFERATION of cells ALREADY DAMAGED, increasing the risk of successive mutations."),
   ("The two named chemicals", "POLYCYCLIC AROMATIC HYDROCARBONS — from COMBUSTION OF TOBACCO — bladder and lung cancer; among the MOST POWERFUL CARCINOGENS KNOWN. AROMATIC AMINES — classically emphasised in OCCUPATIONAL BLADDER CANCER."),
   ("HPV", "Types 16 AND 18 cause most CERVICAL cancer. INTEGRATES viral DNA into the host genome → excess E6 and E7. E6 BLOCKS p53 (needed for self destruction of mutated cells); E7 BLOCKS RB (needed to inhibit cell growth). Also anal, vulvar, vaginal, penile, and OROPHARYNGEAL squamous cell carcinoma."),
   ("Epstein Barr virus", "Certain B CELL LYMPHOMAS and NASOPHARYNGEAL CARCINOMA. Infects B lymphocytes and IMMORTALIZES them; also infects oropharyngeal epithelium. With NORMAL IMMUNE FUNCTION there is no immortalization → asymptomatic or SELF-LIMITED INFECTIOUS MONONUCLEOSIS."),
   ("Hepatitis B", "HEPATOCELLULAR CARCINOMA. Chronic infection and injury → CONTINUOUS REGENERATIVE ATTEMPTS → cells at risk of mutation. ALSO encodes a protein that BINDS p53. Emphasises: CHRONIC INFLAMMATION · REGENERATIVE HYPERPLASIA · GENOMIC INSTABILITY."),
   ("Hepatitis C", "HEPATOCELLULAR CARCINOMA via chronic hepatitis → repeated cycles of CELL DEATH AND PROLIFERATION. MOST develops in patients with CIRRHOSIS, although cancer can OCCASIONALLY OCCUR WITHOUT cirrhosis."),
   ("Helicobacter pylori — the one BACTERIUM", "GRAM-NEGATIVE, colonizes the stomach → CHRONIC GASTRITIS → may lead to ATROPHIC GASTRITIS and INTESTINAL METAPLASIA. Associated with GASTRIC ADENOCARCINOMA and MALT LYMPHOMA. ERADICATION can REDUCE gastric cancer risk and may INDUCE REGRESSION of some early MALT lymphomas."),
   ("Radiation", "ULTRAVIOLET — UVB. And IONIZING radiation."),
   ("Heredity — tumour suppressors", "Rb protein → RETINOBLASTOMA (rare childhood eye tumour) AND OSTEOSARCOMA. NF-1 and NF-2 → NEUROFIBROMATOSIS types 1 and 2, central and peripheral nervous system tumours. p16 (INK4a) → MALIGNANT MELANOMA. APC → FAMILIAL ADENOMATOSIS POLYPOSIS: 500–2500 premalignant adenomatous polyps in the TEENS AND TWENTIES, COLON CANCER BY AGE 50."),
   ("Heredity — repair genes", "BRCA-1 and BRCA-2: a MINORITY of breast cancer patients have an inherited mutation. XERODERMA PIGMENTOSUM: inherited DEFECTIVE DNA REPAIR GENES, cannot repair mutations caused by UVB → increased skin cancer in SUN-EXPOSED areas."),
 ]),
 ("acg-staging", "Cancer Staging & TNM", "#5d6f2f", "#eaefdf", "#f4f7ee", "#48561f", [
   ("Three purposes of staging", "INDICATES EXTENT OF SPREAD within the patient · DETERMINES PROGNOSIS · GUIDES MANAGEMENT."),
   ("Staging is based on three things", "SIZE OF PRIMARY LESION · EXTENT OF SPREAD TO REGIONAL LYMPH NODES · PRESENCE OR ABSENCE OF BLOOD-BORNE METASTASES. Which is exactly T, N and M."),
   ("T — primary lesion", "Tis = lesion HAS NOT INVADED THROUGH THE TISSUE BASEMENT MEMBRANE ('is' = IN SITU). T1–T3 or higher = increasing SIZE and increasing DEPTH OF INVASION."),
   ("N — regional lymph nodes", "Nx = nodes CANNOT BE ASSESSED. N0 = NO regional nodal metastasis. N1, N2 or higher = increasing NUMBER AND RANGE of nodes involved."),
   ("M — metastasis", "Mx = distant metastasis CANNOT BE ASSESSED. M0 = NO distant metastasis. M1 = DISTANT METASTASIS."),
   ("The convention, and the caveat", "x ALWAYS means cannot be assessed; 0 ALWAYS means none found. And: TNM DEFINITIONS ARE CANCER-SPECIFIC — for some cancers DEPTH OF INVASION IS MORE IMPORTANT THAN SIZE."),
 ]),
]


def section(t):
    tid, title, acc, bg, zeb, ink, rows = t
    body = "\n".join(
        '          <tr><td class="h">%s</td><td>%s</td></tr>' % (H.escape(a), H.escape(b))
        for a, b in rows)
    return ('\n  <section class="topic" id="%s" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">\n'
            '    <div class="shead"><span class="dot" style="background:%s"></span><h2>%s</h2></div>\n'
            '    <div class="scroll">\n      <table>\n'
            '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
            '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n'
            % (tid, acc, bg, zeb, ink, acc, H.escape(title), body))


def main():
    s = open(CRAM, encoding="utf-8").read()
    if 'id="acg-nonneo"' in s:
        sys.exit("Lecture 3 cram sections already present -- nothing to do")

    last = re.search(r'      <a href="#derm-cancer"[^>]*>.*?</a>\n', s, re.S)
    assert last, "derm-cancer jump link not found"
    links = "".join(
        '      <a href="#%s" style="color:%s"><span class="dot" style="background:%s"></span>%s</a>\n'
        % (t[0], t[5], t[2], t[1]) for t in TOPICS)
    s = s[:last.end()] + links + s[last.end():]

    foot = "  <footer>"
    assert s.count(foot) == 1, "footer not found"
    s = s.replace(foot, "".join(section(t) for t in TOPICS) + "\n" + foot)

    # Validate BEFORE writing. The first run of this script tripped its own
    # markdown guard AFTER the write, leaving the bad file on disk and forcing a
    # git checkout to undo it. Check first, then commit to disk.
    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th"):
        o, c = len(re.findall(r"<%s[ >]" % tag, s)), s.count("</%s>" % tag)
        assert o == c, "%s: %d open, %d close" % (tag, o, c)
    ids = set(re.findall(r'id="([^"]+)"', s))
    dangling = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a not in ids]
    assert not dangling, "dangling jump links: %r" % dangling
    assert "**" not in s, "markdown emphasis left in a row -- the template renders plain text"

    open(CRAM, "w", encoding="utf-8").write(s)
    print("Lecture 3 cram topics added: %d (%d rows)" % (len(TOPICS), sum(len(t[6]) for t in TOPICS)))
    print("tag balance and jump links verified")


if __name__ == "__main__":
    main()
