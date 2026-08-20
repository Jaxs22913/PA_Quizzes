#!/usr/bin/env python3
"""Add the Lecture 3 (Abnormal Cell Growth and Differentiation) section to the
Clinical Pathophysiology I Exam 1 study guide.

Instructional Objectives are quoted VERBATIM from the PAJ 5101 syllabus (a-l).

Four figures from the deck, NOT lazy -- a lazy figure is absent from the guide's
own Download-as-PDF unless the reader happened to scroll past it, which is why
theme.js now warms them before printing. New figures do not need that crutch.

Slide 43's TNM table is included as an ILLUSTRATION of the deck's own point that
TNM definitions are cancer-specific. Its caption says so explicitly, so nobody
tries to memorise lung-cancer cut-offs out of a general pathophysiology lecture.

Idempotent: fenced in <!--CPL3--> and stripped before re-inserting.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 1")
GUIDE = os.path.join(DIR, "cp-exam-1-study-guide.html")
IMG = "cp-exam-1-study-guide-images"
OPEN, CLOSE = "<!--CPL3-->", "<!--/CPL3-->"
TOC_OPEN, TOC_CLOSE = "<!--CPL3TOC-->", "<!--/CPL3TOC-->"

SRC = "Abnormal Cell Growth for posting.pptx"


def fig(fn, alt, cap, slide):
    return ('<figure class="fig"><img decoding="async" src="%s/%s" alt="%s">'
            '<figcaption>%s <span class="tag">Source: %s, Slide %d.</span></figcaption></figure>'
            % (IMG, fn, alt, cap, SRC, slide))


F_META = fig("020-acg-metaplasia.jpg",
  "Histology slide labelled Squamous Metaplasia, with arrows marking bladder transitional epithelium on one side changing to squamous epithelium on the other.",
  "<b>Metaplasia, caught in the act.</b> Bladder <b>transitional</b> epithelium becoming <b>squamous</b> epithelium. Nothing here is malignant &mdash; the tissue has swapped one mature, differentiated cell type for another in response to chronic irritation. That is the whole definition: a change in <em>differentiation</em>, not a loss of order.", 5)

F_DYS = fig("021-acg-dysplasia-spectrum.jpg",
  "Diagram of squamous epithelium across a spectrum, labelled normal, mild, moderate and severe dysplasia, then carcinoma in situ, then invasive cancer, with the basement membrane drawn as a line that only the invasive cancer crosses.",
  "<b>The single most important diagram in this lecture.</b> Read it left to right: normal squamous epithelium, then mild, moderate and severe <b>dysplasia</b>, then <b>carcinoma in situ</b>, then <b>invasive cancer</b>. Notice what changes and what does not. Cells get more pleomorphic and lose their orientation the whole way along &mdash; but the <b>basement membrane</b> stays intact until the very last panel. <b>Everything up to and including carcinoma in situ is still above that line</b>, which is exactly what <em>Tis</em> means in the TNM system.", 8)

F_GROWTH = fig("022-acg-tissue-growth.jpg",
  "Diagram of cell populations labelled normal, hyperplasia, mild dysplasia, carcinoma in situ described as severe dysplasia, and cancer, with the cells becoming progressively more disordered.",
  "<b>The same progression, counted rather than drawn in section:</b> normal &rarr; <b>hyperplasia</b> (more cells, still orderly) &rarr; <b>mild dysplasia</b> &rarr; <b>carcinoma in situ</b>, labelled here as severe dysplasia &rarr; <b>cancer</b>. Hyperplasia belongs on this line and hypertrophy does not: hyperplasia is more cells, hypertrophy is bigger cells, and only one of them is a step towards neoplasia.", 9)

F_TNM = fig("023-acg-tnm-example.jpg",
  "A detailed TNM staging table for lung cancer, seventh edition, listing T categories by tumour size and invasion, N categories by nodal station, M categories, and the resulting stage groupings.",
  "<b>Do not memorise this table.</b> It is here to make one point, which the previous slide states outright: <b>TNM definitions are cancer-specific</b>. This is the lung version, and its T categories turn on distances from the carina and involvement of named structures that mean nothing in, say, colon cancer &mdash; where depth of invasion through the bowel wall matters more than size. What transfers is the <em>grammar</em>: T for the primary, N for regional nodes, M for distant metastasis, x for cannot be assessed, 0 for none found.", 43)

BODY = '''<section class="deck" id="abnormal-cell-growth">
  <h2 class="deck-title">3 &middot; Abnormal Cell Growth and Differentiation</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Lecture 3 &mdash; Professor Hugh G. Rappa, MD</p>
    <ol type="a">
      <li>Describe the molecular mechanisms of abnormal cell growth and differentiation</li>
      <li>Describe non-neoplastic abnormalities of cell growth</li>
      <li>Describe neoplastic abnormalities of cell growth</li>
      <li>Compare and contrast the routes of tumor spread</li>
      <li>Compare and contrast the different types of benign tumors according to origin</li>
      <li>Compare and contrast the different types of malignant tumors according to origin</li>
      <li>Compare and contrast the categories of gene alterations in carcinogenesis</li>
      <li>Describe the steps of chemical carcinogenesis</li>
      <li>Describe microorganisms&rsquo; role in carcinogenesis</li>
      <li>Compare and contrast the theories of heredity and carcinogenesis</li>
      <li>Describe the histological grading of cancer</li>
      <li>Describe the tumor, nodes, metastases (TNM) staging system</li>
    </ol>
  </div>

  <h3 class="sub" id="acg-nonneoplastic">3.1 &middot; Objective b &mdash; Non-neoplastic abnormalities of cell growth</h3>
  <p>Seven terms, and they sort cleanly into <b>three that are developmental failures</b>, <b>two that
  are changes in size</b>, and <b>two that are changes in kind</b>. Learning them in those groups is
  far easier than as a list.</p>
  <table>
    <tr><th>Group</th><th>Term</th><th>What happened</th></tr>
    <tr><td rowspan="3"><b>Failed to develop</b></td><td><b>Agenesis</b></td><td>Complete absence &mdash; the <b>primordial tissue never formed</b></td></tr>
    <tr><td><b>Aplasia</b></td><td>The <b>primordial tissue exists</b> but fails to develop into the mature organ</td></tr>
    <tr><td><b>Hypoplasia</b></td><td><b>Partial</b> development, resulting in a functional deficiency</td></tr>
    <tr><td rowspan="2"><b>Changed size</b></td><td><b>Atrophy</b></td><td>Shrinkage of a tissue or organ that <b>had formed and matured normally</b></td></tr>
    <tr><td><b>Hypertrophy</b></td><td>Enlargement due to enlargement of <b>individual cells</b>; especially important in permanent tissues &mdash; skeletal and cardiac muscle</td></tr>
    <tr><td rowspan="2"><b>Changed kind</b></td><td><b>Metaplasia</b></td><td>One cell type becomes another under <b>chronic irritation or injury</b>; a change in <b>differentiation</b></td></tr>
    <tr><td><b>Dysplasia</b></td><td><b>Disordered growth</b>, typically epithelial: varied cell size and shape, <b>loss of architectural orientation</b>, darker and larger nuclei. <b>May progress to cancer &mdash; precancerous</b></td></tr>
  </table>
  <div class="pearl"><b>Agenesis versus aplasia is a timing question.</b> In agenesis there was never
  anything to work with. In aplasia the raw material was there and did not mature. And <b>atrophy is
  not hypoplasia</b>: hypoplasia never got there, atrophy got there and shrank back.</div>

  <h3 class="sub" id="acg-dysplasia">3.2 &middot; Objectives a &amp; b &mdash; Metaplasia, dysplasia, and the line that matters</h3>
  <p>Metaplasia and dysplasia are the two that carry towards cancer, and they are not the same
  thing. <b>Metaplasia swaps one orderly tissue for another orderly tissue.</b> <b>Dysplasia keeps
  the tissue type and loses the order.</b> Only the second is precancerous.</p>

  <h3 class="sub" id="acg-neoplasia">3.3 &middot; Objectives c &amp; k &mdash; Neoplasia and histological grading</h3>
  <p>A <b>neoplasm</b> is an abnormal mass of tissue growing <b>autonomously</b> &mdash;
  self-perpetuating <em>without physiologic growth stimuli</em>. That single word is what separates
  it from hyperplasia, which stops when the stimulus stops. The entire proliferating population is
  derived from <b>one cell</b> that underwent a genetic alteration, so a tumour is a clone. It has
  two components: <b>parenchyma</b>, the proliferating neoplastic cells, and <b>stroma</b>, the
  connective tissue and blood vessels supporting them. <em>Neoplasm</em> and <em>tumor</em> are
  interchangeable.</p>
  <p><b>Cancer</b> is a malignant neoplasm. The word comes from the Latin for crab, because it
  &ldquo;adheres to any tissue that it seizes upon&rdquo; and reaches out with claws into
  surrounding tissue. A <b>metastasis</b> is the portion of a cancer that has migrated from the
  primary site to other sites.</p>
  <table>
    <tr><th>Grade</th><th>Resemblance to the normal cell</th></tr>
    <tr><td><b>Well differentiated</b></td><td>Close resemblance</td></tr>
    <tr><td><b>Moderately differentiated</b></td><td>Intermediate resemblance</td></tr>
    <tr><td><b>Poorly differentiated</b></td><td>Poor resemblance</td></tr>
    <tr><td><b>Anaplasia</b></td><td><b>Lack of differentiation</b></td></tr>
  </table>
  <div class="pearl"><b>Grading and staging answer different questions, and the exam will test that
  you know which is which.</b> <b>Grading</b> asks <em>what does it look like</em> &mdash; how
  closely the neoplasm resembles comparable normal cells in appearance and function. <b>Staging</b>
  asks <em>how far has it got</em> &mdash; size, nodes, metastases.</div>
  <table>
    <tr><th></th><th>Benign tumour</th><th>Malignant tumour</th></tr>
    <tr><td><b>Border</b></td><td>Well circumscribed</td><td>Ragged, not easily discernable</td></tr>
    <tr><td><b>Relation to tissue</b></td><td><b>Compresses</b> surrounding tissue</td><td><b>Infiltrates and invades</b> it</td></tr>
    <tr><td><b>Capsule</b></td><td>Often has a fibrous capsule</td><td>&mdash;</td></tr>
    <tr><td><b>Differentiation</b></td><td>Usually well differentiated</td><td><b>Various degrees</b></td></tr>
    <tr><td><b>Metastasis</b></td><td>Does not metastasize</td><td>May metastasize</td></tr>
    <tr><td><b>Growth</b></td><td>Slow</td><td>Rapid</td></tr>
  </table>
  <p>Histologically, four features move a tumour along that spectrum: <b>pleomorphism</b>,
  <b>abnormal nuclei</b>, <b>mitoses</b>, and <b>abnormal differentiation</b>.</p>
  <p><b>Why does a tumour outgrow normal tissue?</b> The deck answers it from stem cell kinetics. A
  stem cell has unlimited self-renewal and <em>cellular immortality</em> but a relatively
  <b>low</b> rate of proliferation; once a cell commits to differentiation, proliferation can be
  dramatic, but those differentiated cells have a limited life-span. Abnormal differentiation in
  cancer puts <b>a greater percentage of cells in the proliferative pool at the expense of the
  maturation pool</b>, so the mass grows through <b>a higher proliferative fraction AND a lower rate
  of cell loss</b> &mdash; both halves, not just faster division. The deck is careful to call the
  cancer stem cell idea <em>a conceptual framework rather than an absolute explanation</em>.</p>

  <h3 class="sub" id="acg-spread">3.4 &middot; Objective d &mdash; Routes of tumour spread</h3>
  <table>
    <tr><th>Route</th><th>Mechanism</th><th>Where it goes</th></tr>
    <tr><td><b>Haematogenous</b></td><td>Cells <b>separate from each other</b> and degrade intercellular tissue with <b>enzymes</b>; cells invade the vessel; <b>multiple tumour fragments</b> travel</td><td>Typically through <b>veins</b> &mdash; especially the <b>portal vein</b> and the <b>inferior vena cava</b>, so cancers often spread to <b>liver</b> and <b>lungs</b> respectively. One organ may carry several nodules</td></tr>
    <tr><td><b>Lymphatic</b></td><td>Cancer spreads into lymphatic vessels <b>at the tumour margin</b></td><td>Follows the <b>natural route of lymphatic drainage</b> &mdash; which is why nodal staging is anatomically predictable</td></tr>
    <tr><td><b>Seeding</b></td><td>Invasion of tumour <b>through an organ surface</b> into a cavity</td><td><b>Pericardial, pleural, peritoneal</b> cavities, joint cavities, and the <b>subarachnoid space</b>. <b>Most commonly the peritoneal cavity</b></td></tr>
  </table>
  <p>A cavity here is defined by <b>the membrane covering the organs in it and the membrane covering
  the cavity wall</b> &mdash; pericardium, pleura and peritoneum over heart, lungs and abdominal
  organs respectively.</p>
  <div class="pearl"><b>Metastatic spread is NOT random.</b> The deck says so directly, and gives
  three determinants: the <b>pattern of venous blood flow</b>, <b>specific receptors on tumour and
  endothelial cells</b>, and <b>metastatic &ldquo;fitness&rdquo;, which is genetically
  determined</b>. Reaching the bloodstream is only the first hurdle &mdash; the cell must then
  achieve <b>survival in the circulation</b> and <b>survival in a new organ</b>.</div>

  <h3 class="sub" id="acg-classification">3.5 &middot; Objectives e &amp; f &mdash; Classifying tumours by origin</h3>
  <p>This is a naming rule, and once you have it, every tumour name in medicine decodes. <b>Two
  origins, and a suffix for each.</b></p>
  <table>
    <tr><th>Origin</th><th>Benign</th><th>Malignant</th></tr>
    <tr><td><b>Mesenchymal</b> &mdash; supportive tissue: connective tissue, adipose, cartilage, smooth and striated muscle, bone</td><td>Named for the tissue</td><td><b>Sarcoma</b></td></tr>
    <tr><td><b>Epithelial</b>, glandular pattern or from a gland</td><td><b>Adenoma</b> &mdash; sometimes secretes the hormone of its gland of origin</td><td><b>Adenocarcinoma</b></td></tr>
    <tr><td><b>Epithelial</b>, squamous differentiation</td><td>&mdash;</td><td><b>Squamous cell carcinoma</b></td></tr>
    <tr><td><b>Epithelial</b> surface, finger-like projections</td><td><b>Papilloma</b> &mdash; visible &ldquo;finger-like&rdquo; or warty projections, microscopically or macroscopically</td><td>&mdash;</td></tr>
  </table>
  <div class="pearl"><b>Mesenchymal &rarr; sarcoma. Epithelial &rarr; carcinoma.</b> If you can place
  the tissue of origin in one of those two buckets, you can name the malignancy. Adipose tissue is
  supportive, so a malignant fat tumour is a sarcoma, never a carcinoma.</div>

  <h3 class="sub" id="acg-genes">3.6 &middot; Objectives g &amp; h &mdash; Gene alterations and chemical carcinogenesis</h3>
  <p>Carcinogenesis is a <b>multistep process</b> resulting from damage to <b>multiple</b> normal
  regulatory genes. Those genes <b>may be inherited and/or</b> damaged by chemical carcinogens,
  ultraviolet and ionizing radiation, or microbial organisms &mdash; viruses and a bacterium.</p>
  <table>
    <tr><th>Category</th><th>Normal job</th><th>What goes wrong</th><th>Examples</th></tr>
    <tr><td><b>Protooncogenes</b></td><td>Promote <b>regulated</b> cell growth &mdash; growth factors, growth factor receptors, nuclear regulatory proteins, signal transduction proteins</td><td>Mutation converts them to <b>oncogenes</b>, encoding <b>oncoproteins</b> that promote continued <b>uncontrolled</b> growth</td><td>&mdash;</td></tr>
    <tr><td><b>Tumour suppressor genes</b></td><td><b>Inhibit</b> cell growth</td><td>Loss removes a brake</td><td><b>NF-1, NF-2, RB, APC</b></td></tr>
    <tr><td><b>Repair genes</b></td><td>Promote repair of damaged deoxyribonucleic acid</td><td>Loss lets mutations accumulate</td><td><b>BRCA-1, BRCA-2</b></td></tr>
    <tr><td><b>Apoptosis genes</b></td><td>Cause cells with damaged deoxyribonucleic acid to <b>self destruct</b></td><td>Loss lets damage be <b>continued in dividing cells and become permanent</b></td><td>&mdash;</td></tr>
  </table>
  <p><b>Chemical carcinogenesis has two named steps.</b> <b>Initiation</b>, caused by
  <em>initiators</em>: chemicals cause <b>permanent damage to deoxyribonucleic acid</b>.
  <b>Promotion</b>, caused by <em>promoters</em>: sustained or enhanced <b>proliferation of cells
  already damaged</b> by an initiating agent, raising the risk of successive mutations.</p>
  <table>
    <tr><th>Agent</th><th>Source</th><th>Cancer</th></tr>
    <tr><td><b>Polycyclic aromatic hydrocarbons</b></td><td>Combustion of <b>tobacco</b></td><td>Bladder and lung &mdash; <b>among the most powerful carcinogens known</b></td></tr>
    <tr><td><b>Aromatic amines</b></td><td>Occupational exposure</td><td>Classically emphasised in <b>occupational bladder cancer</b></td></tr>
  </table>

  <h3 class="sub" id="acg-microbes">3.7 &middot; Objective i &mdash; Microorganisms and carcinogenesis</h3>
  <p>Five organisms, and they divide into <b>two mechanisms</b>. Either the microbe <b>directly
  disables a tumour suppressor</b>, or it causes <b>chronic inflammation with repeated regeneration</b>
  and lets mutations accumulate. Sorting them that way turns five facts into two ideas.</p>
  <table>
    <tr><th>Organism</th><th>Cancer</th><th>Mechanism</th></tr>
    <tr><td><b>Human papillomavirus</b><br>types <b>16 and 18</b></td><td><b>Cervical</b> cancer; also anal, vulvar, vaginal, penile, and oropharyngeal squamous cell carcinoma</td><td><b>Direct.</b> Integrates its viral deoxyribonucleic acid into the host genome, causing excessive <b>E6</b> and <b>E7</b>. <b>E6 blocks p53</b> (needed to promote self destruction of mutated cells); <b>E7 blocks RB</b> (needed to inhibit cell growth)</td></tr>
    <tr><td><b>Epstein Barr virus</b></td><td>Certain <b>B cell lymphomas</b> and <b>nasopharyngeal carcinoma</b></td><td><b>Direct.</b> Infects B lymphocytes and <b>&ldquo;immortalizes&rdquo;</b> them; also infects oropharyngeal epithelial cells. In <b>normal immune function</b> this does not happen &mdash; the patient is asymptomatic or has self-limited infectious mononucleosis</td></tr>
    <tr><td><b>Hepatitis B virus</b></td><td><b>Hepatocellular carcinoma</b></td><td><b>Both.</b> Chronic infection and injury &rarr; continuous regenerative attempts &rarr; cells at risk of mutation. AND it encodes a protein that <b>binds p53</b>. Emphasises: <b>chronic inflammation, regenerative hyperplasia, genomic instability</b></td></tr>
    <tr><td><b>Hepatitis C virus</b></td><td><b>Hepatocellular carcinoma</b></td><td><b>Inflammatory.</b> Chronic hepatitis &rarr; repeated cycles of cell death and proliferation. <b>Most arises in cirrhosis, though cancer can occasionally occur without it</b></td></tr>
    <tr><td><b>Helicobacter pylori</b><br>the one <b>bacterium</b></td><td><b>Gastric adenocarcinoma</b> and <b>MALT lymphoma</b> (mucosa-associated lymphoid tissue)</td><td><b>Inflammatory.</b> Gram-negative, colonizes the stomach &rarr; chronic gastritis &rarr; atrophic gastritis and <b>intestinal metaplasia</b>. Chronic inflammation raises epithelial turnover and the chance of mutation</td></tr>
  </table>
  <div class="pearl"><b>Three separate organisms converge on p53 and RB.</b> Human papillomavirus E6
  and hepatitis B's encoded protein both take out <b>p53</b>, the apoptosis gate; human
  papillomavirus E7 takes out <b>RB</b>, the growth brake. If you know what those two proteins
  <em>do</em>, the viral mechanisms stop being three facts and become one idea told three ways.</div>
  <p><b>And the inflammatory mechanism has a testable consequence:</b> eradicating <em>Helicobacter
  pylori</em> can <b>reduce the risk of gastric cancer</b> and may <b>induce regression of some
  early MALT lymphomas</b>. That is the cleanest evidence in the lecture that the chronic
  inflammation is doing the carcinogenic work.</p>
  <p><b>Radiation</b> gets its own short slide: <b>ultraviolet radiation &mdash; UVB</b> &mdash; and
  <b>ionizing radiation</b>.</p>

  <h3 class="sub" id="acg-heredity">3.8 &middot; Objective j &mdash; Heredity and carcinogenesis</h3>
  <p>Inherited cancer risk comes through the same gene categories, just present from birth.</p>
  <table>
    <tr><th>Category</th><th>Gene</th><th>Disease</th></tr>
    <tr><td rowspan="4"><b>Tumour suppressor alterations</b></td><td><b>Rb protein</b></td><td><b>Retinoblastoma</b> (rare childhood eye tumour) and <b>osteosarcoma</b></td></tr>
    <tr><td><b>NF-1 and NF-2</b></td><td><b>Neurofibromatosis</b> types 1 and 2 &mdash; a variety of central and peripheral nervous system tumours</td></tr>
    <tr><td><b>p16 (INK4a)</b></td><td><b>Malignant melanoma</b></td></tr>
    <tr><td><b>APC</b></td><td><b>Familial adenomatosis polyposis</b> &mdash; <b>500 to 2500</b> premalignant adenomatous polyps in the teens and twenties; <b>colon cancer by age 50</b></td></tr>
    <tr><td rowspan="2"><b>Repair gene alterations</b></td><td><b>BRCA-1, BRCA-2</b></td><td>A <b>minority</b> of breast cancer patients carry an inherited mutation</td></tr>
    <tr><td>Defective repair genes</td><td><b>Xeroderma pigmentosum</b> &mdash; cannot repair mutations caused by <b>UVB</b>; increased skin cancer in sun-exposed areas</td></tr>
    <tr><td><b>Apoptosis gene alterations</b></td><td>&mdash;</td><td>Inherited failure to make mutated cells self destruct, so mutations propagate</td></tr>
  </table>

  <h3 class="sub" id="acg-staging">3.9 &middot; Objective l &mdash; TNM staging</h3>
  <p><b>Staging has three purposes:</b> it indicates the <b>extent of spread</b> within the patient,
  it <b>determines prognosis</b>, and it <b>guides management</b>. It is based on three things,
  which are exactly the three letters: the <b>size of the primary lesion</b>, the <b>extent of
  spread to regional lymph nodes</b>, and the <b>presence or absence of blood-borne metastases</b>.</p>
  <table>
    <tr><th>Letter</th><th>Category</th><th>Meaning</th></tr>
    <tr><td rowspan="2"><b>T</b> &mdash; primary lesion</td><td><b>Tis</b></td><td>Lesion has <b>not invaded through the tissue basement membrane</b>; <em>is</em> = in situ</td></tr>
    <tr><td><b>T1&ndash;T3</b> or higher</td><td>Increasing <b>size</b> of the primary lesion; increasing <b>depth of invasion</b></td></tr>
    <tr><td rowspan="3"><b>N</b> &mdash; regional nodes</td><td><b>Nx</b></td><td>Regional lymph nodes <b>cannot be assessed</b></td></tr>
    <tr><td><b>N0</b></td><td><b>No</b> regional lymph node metastasis</td></tr>
    <tr><td><b>N1, N2</b> or higher</td><td>Involvement of increasing <b>number and range</b> of lymph nodes</td></tr>
    <tr><td rowspan="3"><b>M</b> &mdash; metastasis</td><td><b>Mx</b></td><td>Distant metastasis <b>cannot be assessed</b></td></tr>
    <tr><td><b>M0</b></td><td><b>No</b> distant metastasis</td></tr>
    <tr><td><b>M1</b></td><td><b>Distant metastasis</b> present</td></tr>
  </table>
  <div class="pearl"><b>The convention generalises: x means cannot be assessed, 0 means none
  found.</b> And the caveat the deck states outright &mdash; <b>TNM definitions are
  cancer-specific</b>. For some cancers, <b>depth of invasion is more important than size</b>.</div>

  <button type="button" class="test-yourself-btn" style="--acc:#3b2a5e" onclick="window.openTestYourself('Test yourself &mdash; Abnormal Cell Growth', TEST_YOURSELF.abnormalgrowth)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>Abnormal Cell Growth for posting.pptx</em> (Professor Hugh
  G. Rappa, MD), Slides 1&ndash;43, and the PAJ 5101 syllabus instructional objectives a&ndash;l.
  Figures are reproduced from the lecture slides and each is cited to its slide.</footer>
</section>'''


TOC = '''%s
  <a class="top-link" href="#abnormal-cell-growth">3 &middot; Abnormal Cell Growth and Differentiation</a>
  <a href="#acg-nonneoplastic">3.1 Objective b &mdash; Non-neoplastic abnormalities</a>
  <a href="#acg-dysplasia">3.2 Objectives a &amp; b &mdash; Metaplasia vs dysplasia</a>
  <a href="#acg-neoplasia">3.3 Objectives c &amp; k &mdash; Neoplasia &amp; grading</a>
  <a href="#acg-spread">3.4 Objective d &mdash; Routes of tumour spread</a>
  <a href="#acg-classification">3.5 Objectives e &amp; f &mdash; Classifying by origin</a>
  <a href="#acg-genes">3.6 Objectives g &amp; h &mdash; Gene alterations &amp; chemical carcinogenesis</a>
  <a href="#acg-microbes">3.7 Objective i &mdash; Microorganisms</a>
  <a href="#acg-heredity">3.8 Objective j &mdash; Heredity</a>
  <a href="#acg-staging">3.9 Objective l &mdash; TNM staging</a>
%s''' % (TOC_OPEN, TOC_CLOSE)

TESTS = '''    abnormalgrowth: [
      {q:"An organ is completely absent because the primordial tissue never formed. Which term applies?",
       choices:["Agenesis","Aplasia","Hypoplasia","Atrophy"],correct:0,
       expl:"Agenesis is failure of primordial tissue FORMATION. In aplasia the primordial tissue exists but fails to develop into the mature organ. Hypoplasia is partial development with a functional deficiency; atrophy is shrinkage of something that had already matured normally."},
      {q:"What separates metaplasia from dysplasia?",
       choices:["Metaplasia swaps one orderly cell type for another; dysplasia keeps the type and loses the order","Metaplasia is precancerous; dysplasia is not","Metaplasia occurs in mesenchyme; dysplasia in epithelium","Metaplasia involves invasion; dysplasia does not"],correct:0,
       expl:"Metaplasia is a change in DIFFERENTIATION under chronic irritation. Dysplasia is disordered growth with varied cell size and shape, loss of architectural orientation, and darker larger nuclei \\u2014 and it MAY PROGRESS TO CANCER, which is why it is precancerous."},
      {q:"Which single word in the definition of a neoplasm separates it from hyperplasia?",
       choices:["Autonomously \\u2014 it grows without physiologic growth stimuli","Abnormal \\u2014 the cells look different","Mass \\u2014 it forms a discrete lump","Proliferating \\u2014 the cells divide"],correct:0,
       expl:"Hyperplasia stops when the stimulus stops; a neoplasm is self-perpetuating. The whole proliferating population is also derived from ONE cell that underwent a genetic alteration, so a tumour is a clone."},
      {q:"What are the two components of a neoplasm?",
       choices:["Parenchyma, the neoplastic cells; and stroma, the connective tissue and vessels","Initiators and promoters","Proliferative pool and maturation pool","Primary lesion and metastatic deposit"],correct:0,
       expl:"The stroma is host tissue supporting the tumour, not part of the malignant clone."},
      {q:"Anaplasia means what?",
       choices:["Lack of differentiation","Close resemblance to the normal cell","Failure of a primordial tissue to mature","Invasion through the basement membrane"],correct:0,
       expl:"The grading scale runs well differentiated, moderately differentiated, poorly differentiated, then anaplasia. Grading asks what it LOOKS like; staging asks how FAR it has got."},
      {q:"Why does a tumour mass outgrow normal tissue?",
       choices:["A higher proliferative fraction AND a lower rate of cell loss","A higher proliferative fraction alone","A shorter cell cycle alone","Increased apoptosis in surrounding normal cells"],correct:0,
       expl:"Abnormal differentiation puts a greater percentage of cells in the proliferative pool at the expense of the maturation pool. Both halves matter \\u2014 more dividing, and fewer dying."},
      {q:"Haematogenous spread is typically through which vessels, and where does that send tumour?",
       choices:["Veins \\u2014 especially the portal vein and inferior vena cava, so liver and lungs","Arteries \\u2014 especially the aorta, so brain and kidney","Lymphatics at the tumour margin, so regional nodes","Capillaries in the tumour stroma, so locally only"],correct:0,
       expl:"The portal vein delivers to the liver and the inferior vena cava to the right heart and then the lungs. And spread is NOT random: it is determined by venous flow, specific receptors on tumour and endothelial cells, and genetically determined metastatic fitness."},
      {q:"Seeding most commonly occurs in which cavity?",
       choices:["The peritoneal cavity","The pleural cavity","The pericardial cavity","The subarachnoid space"],correct:0,
       expl:"All four are named, but the peritoneum is singled out as commonest. A cavity here is defined by the membrane covering the organs plus the membrane covering the cavity wall."},
      {q:"A malignant tumour arises from adipose tissue. What is it called?",
       choices:["A sarcoma","A carcinoma","An adenocarcinoma","A papilloma"],correct:0,
       expl:"Adipose tissue is supportive, so mesenchymal, so sarcoma. Mesenchymal \\u2192 sarcoma; epithelial \\u2192 carcinoma. That one rule decodes most tumour names."},
      {q:"A benign epithelial tumour with a glandular pattern is called what?",
       choices:["An adenoma","An adenocarcinoma","A papilloma","A sarcoma"],correct:0,
       expl:"And it sometimes secretes the hormone produced by its gland of origin. A papilloma is the benign epithelial tumour with finger-like or warty projections from a surface."},
      {q:"What happens when a protooncogene mutates?",
       choices:["It becomes an oncogene encoding oncoproteins that drive uncontrolled growth","It becomes a tumour suppressor gene","It becomes a repair gene","It is silenced and the cell stops growing"],correct:0,
       expl:"Protooncogenes normally promote REGULATED growth \\u2014 growth factors, their receptors, nuclear regulatory proteins and signal transduction proteins. Mutation removes the regulation, not the machinery."},
      {q:"Which category do BRCA-1 and BRCA-2 belong to?",
       choices:["Genes promoting repair of damaged DNA","Tumour suppressor genes","Protooncogenes","Genes promoting apoptosis"],correct:0,
       expl:"Four categories in total: protooncogenes, tumour suppressor genes (NF-1, NF-2, RB, APC), repair genes (BRCA-1, BRCA-2), and apoptosis genes."},
      {q:"What is the difference between an initiator and a promoter in chemical carcinogenesis?",
       choices:["Initiators cause permanent DNA damage; promoters drive proliferation of already-damaged cells","Initiators drive proliferation; promoters cause DNA damage","Initiators are chemical; promoters are viral","Initiators act on epithelium; promoters on mesenchyme"],correct:0,
       expl:"Permanence is what defines initiation. Polycyclic aromatic hydrocarbons from tobacco combustion cause bladder and lung cancer; aromatic amines are classically emphasised in occupational bladder cancer."},
      {q:"Human papillomavirus E6 and E7 block which proteins?",
       choices:["E6 blocks p53; E7 blocks RB","E6 blocks RB; E7 blocks p53","Both block p53","Both block BRCA-1"],correct:0,
       expl:"p53 promotes self destruction of mutated cells; RB inhibits cell growth. So E6 removes apoptosis and E7 removes a growth brake. Hepatitis B also encodes a protein that binds p53 \\u2014 three organisms converging on two proteins."},
      {q:"Which organism in this lecture is a bacterium, and what does it cause?",
       choices:["Helicobacter pylori \\u2014 gastric adenocarcinoma and MALT lymphoma","Epstein Barr virus \\u2014 B cell lymphoma","Hepatitis B \\u2014 hepatocellular carcinoma","Human papillomavirus \\u2014 cervical cancer"],correct:0,
       expl:"Gram-negative, colonizes the stomach, causes chronic gastritis which may lead to atrophic gastritis and intestinal metaplasia. Eradication can REDUCE gastric cancer risk and may induce regression of some early MALT lymphomas."},
      {q:"What happens to Epstein Barr virus infection in a patient with normal immune function?",
       choices:["No immortalization of B lymphocytes \\u2014 asymptomatic or self-limited mononucleosis","B lymphocytes are immortalized but the lymphoma regresses","Nasopharyngeal carcinoma develops within years","The virus is completely cleared and cannot reinfect"],correct:0,
       expl:"The virus infects B lymphocytes and 'immortalizes' them, but normal immune function is what stops that becoming cancer."},
      {q:"Which inherited alteration causes 500 to 2500 premalignant colon polyps in the teens and twenties?",
       choices:["APC \\u2014 familial adenomatosis polyposis","RB \\u2014 retinoblastoma","p16 (INK4a) \\u2014 melanoma","BRCA-1 \\u2014 breast cancer"],correct:0,
       expl:"And those patients develop colon cancer by age 50. RB is associated with retinoblastoma AND osteosarcoma; p16 with malignant melanoma; NF-1 and NF-2 with neurofibromatosis."},
      {q:"What does Tis mean in the TNM system?",
       choices:["The lesion has not invaded through the basement membrane","The primary tumour cannot be assessed","There is no evidence of primary tumour","The tumour is too small to measure"],correct:0,
       expl:"'is' = in situ. It is the same threshold the dysplasia diagram turns on \\u2014 everything up to and including carcinoma in situ is still above the basement membrane."},
      {q:"What do Nx and N0 mean respectively?",
       choices:["Nodes cannot be assessed; no regional nodal metastasis","No nodal metastasis; nodes cannot be assessed","Nodes not sampled; one node involved","Nodes removed; nodes normal in size"],correct:0,
       expl:"The convention generalises across the whole system: x means cannot be assessed, 0 means none found. So Mx is distant metastasis cannot be assessed and M0 is no distant metastasis."},
      {q:"What caveat does the lecture attach to TNM definitions?",
       choices:["They are cancer-specific; for some cancers depth of invasion matters more than size","They are identical across all cancers","They apply only to carcinomas, not sarcomas","They have replaced histological grading"],correct:0,
       expl:"Which is why the deck's example table is for one named cancer rather than all of them. What transfers is the grammar: T, N, M, x and 0 \\u2014 not the specific cut-offs."}
    ],
'''


def main():
    src = open(GUIDE, encoding="utf-8").read()
    src = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), "", src, flags=re.S)
    src = re.sub(re.escape(TOC_OPEN) + r".*?" + re.escape(TOC_CLOSE), "", src, flags=re.S)
    src = re.sub(r"[ \t]*abnormalgrowth: \[.*?\n    \],\n", "", src, flags=re.S)

    body = BODY
    # figures go after the subsection they illustrate
    for anchor, f in (("acg-dysplasia", F_META + "\n  " + F_DYS + "\n  " + F_GROWTH),
                      ("acg-staging", F_TNM)):
        i = body.index('id="%s"' % anchor)
        nxt = min([x for x in (body.find("<h3", i + 1), body.find("<button", i + 1)) if x > 0])
        region = body[i:nxt]
        at = region.rfind("</div>") if anchor == "acg-staging" else region.rfind("</p>")
        at = i + at + (len("</div>") if anchor == "acg-staging" else len("</p>"))
        body = body[:at] + "\n  " + f + body[at:]
    body = OPEN + "\n\n" + body + "\n\n" + CLOSE

    j = src.index("</main>")
    src = src[:j] + body + "\n\n" + src[j:]

    k = src.index("</nav>")
    src = src[:k] + TOC + "\n" + src[k:]

    m = src.index("var TEST_YOURSELF = {")
    m = src.index("\n", m) + 1
    src = src[:m] + TESTS + src[m:]

    assert src.count(OPEN) == src.count(CLOSE) == 1
    assert not [t for t in re.findall(r"<img\b[^>]*>", body) if "lazy" in t]
    for fn in re.findall(r'src="%s/([^"]+)"' % IMG, body):
        assert os.path.exists(os.path.join(DIR, IMG, fn)), fn

    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added section 3 (%d figures, %d subsections, %d test-yourself questions)"
          % (body.count("<figure"), body.count('class="sub"'), TESTS.count("{q:")))


if __name__ == "__main__":
    main()
