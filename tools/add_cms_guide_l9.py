#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Lecture 9 (Pre-Malignant and Malignant Cutaneous Lesions) section.

Lecture 9 is the LAST derm lecture, so it becomes section 9 and only "How this
course is built" shifts, 9 -> 10.

Instructional Objectives quoted VERBATIM from the PAJ 5500 syllabus, including
its flat auto-numbering (1, then the nine lesion types, then 11 and its two
populations) reproduced as written rather than tidied into a/b.

THE SLIDE IS AUTHORITATIVE -- Jaquith's deck.

PHOTOGRAPH STRIPS reuse the comparison chart's images in place, so no new bytes
and the two artifacts cannot drift. Every one was audited at full size; see the
guard sets in build_cms_derm_chart.py for what that audit rejected in this deck,
including a new class -- schematic diagrams and data tables that ARE content but
are not what a lesion looks like.

Idempotent: fenced in <!--CMSL9--> and stripped before re-inserting.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
GUIDE = os.path.join(DIR, "cms-exam-1-study-guide.html")
IMGDIR = os.path.join(DIR, "cms-derm-chart-images")
OPEN, CLOSE = "<!--CMSL9-->", "<!--/CMSL9-->"
TOC_OPEN, TOC_CLOSE = "<!--CMSL9TOC-->", "<!--/CMSL9TOC-->"


def fig(stem, name, caption, slide):
    cand = [f for f in os.listdir(IMGDIR) if f.rsplit(".", 1)[0] == stem]
    assert cand, "no chart image for %r -- run build_cms_derm_chart.py first" % stem
    return ('<figure><img src="cms-derm-chart-images/%s" decoding="async" alt="%s &mdash; %s">'
            '<figcaption><span class="fg-name">%s</span>%s'
            '<span class="fg-cite">Lecture 9 &middot; Slide %d</span></figcaption></figure>'
            % (cand[0], name, caption, name, caption, slide))


def grid(items):
    return ('  <p class="figgrid-h">What these look like</p>\n  <div class="figgrid">'
            + "".join(fig(*i) for i in items) + "</div>\n")


SECTION = """
<section class="deck" id="malignant-lesions">
  <h2 class="deck-title">9 &middot; Pre-Malignant and Malignant Cutaneous Lesions</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis of the following pre-malignant and malignant cutaneous lesions:</li>
      <li>Precancerous lesions</li>
      <li>Actinic keratosis</li>
      <li>Skin cancer</li>
      <li>Squamous cell carcinoma</li>
      <li>Basal cell carcinoma</li>
      <li>Malignant melanoma</li>
      <li>Nail neoplastic conditions</li>
      <li>Kaposi&rsquo;s sarcoma</li>
      <li>Cutaneous T-cell lymphoma</li>
      <li>Identify medical care strategies for pre-malignant and malignant cutaneous lesions in the lecture topic list for the following populations.</li>
      <li>adult</li>
      <li>elderly</li>
    </ol>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Before you start</span>
  <p><b>Where the lecture audio and a slide disagree on a fact, THE SLIDE WINS.</b> Every fact in this
  section and in the four Lecture 9 quizzes comes from the PowerPoint.</p>
  <p><mark class="prof-highlight">Three slides in this deck carry content that exists ONLY as a
  picture</mark> and extract as blank text: the <b>Clark level</b> diagram, the <b>Stages of
  Melanoma</b> diagram, and the full <b>TNM staging table</b>. They are covered in 9.5 below and in
  the quizzes. If you revise from the slide text alone you will miss all three.</p>
  </div>

  <h3 class="sub" id="mal-approach">9.1 &middot; Objective 1 &mdash; Describe before you name</h3>
  <p>The deck opens with a discipline rather than a disease: <strong>characterise the lesion
  systematically before assigning a diagnosis</strong> &mdash; primary lesion type, colour, surface
  texture, border definition, size, distribution, palpability, ulceration, bleeding, induration, and
  temporal evolution.</p>
  <table>
    <tr><th>Examination priorities</th><th>Key history</th></tr>
    <tr><td>Good lighting; dermoscopy when trained; total-body skin survey when indicated<br>
      <b>Palms, soles and nails</b><br>
      <b>Oral mucosa when Kaposi sarcoma is possible</b><br>
      Regional lymph nodes for invasive or high-risk disease</td>
      <td>Onset and change; bleeding or non-healing; pain or pruritus<br>
      Sunburns, occupational or recreational ultraviolet exposure, tanning-bed use<br>
      <b>Prior skin cancer; immunosuppression or transplant; human immunodeficiency virus risk</b><br>
      <b>Chronic scars, wounds or radiation sites</b><br>
      Family history; the lesion the patient themselves has noticed</td></tr>
  </table>
  <p>Two of those are easy to skip and carry the most weight: the <strong>oral cavity</strong>, because
  a hard-palate lesion may be the presenting site of Kaposi sarcoma, and <strong>chronic scars or old
  radiation fields</strong>, because squamous cell carcinoma arises in them.</p>

  <h3 class="sub" id="mal-ak">9.2 &middot; Objective 1 &mdash; Actinic keratosis</h3>
  <p><strong>Premalignant, and on a biologic continuum with keratinocyte carcinoma &mdash; not a
  distinct separate entity.</strong> Chronic ultraviolet injury produces dysplastic keratinocytic
  change across a <em>field</em> of sun-damaged skin, which is the idea the whole management section
  turns on.</p>
  <p>Small <strong>0.2 to 0.6&nbsp;cm</strong> flesh-coloured, pink or slightly hyperpigmented papules
  with a <strong>sandpaper texture</strong>; a lesion <strong>may be more apparent by touch than by
  sight</strong>. Sun-exposed face, scalp, ears, forearms and dorsal hands.</p>
  <p><strong>About 1 in 1,000 lesions per year progresses to squamous cell carcinoma</strong> &mdash;
  and cumulative <em>field</em> risk matters more than the risk from any individual lesion, which is
  difficult to predict for a given patient.</p>
  <table>
    <tr><th>Lesion-directed</th><th>Field-directed</th></tr>
    <tr><td>Isolated or few lesions with clear borders<br><b>Liquid nitrogen cryotherapy</b> &mdash;
      the lesion crusts and disappears over <b>10 to 14 days</b></td>
      <td>Multiple lesions in one anatomic region (field cancerization)<br>
      Topical <b>fluorouracil</b> &middot; <b>imiquimod</b> &middot; <b>photodynamic therapy</b><br>
      Fluorouracil plus calcipotriene &mdash; possible benefit</td></tr>
  </table>
  <p><strong>What is NOT a typical actinic keratosis</strong>, and should trigger biopsy:
  <strong>bleeding, induration, ulceration or rapid enlargement</strong>. The most important
  distinction is early squamous cell carcinoma or carcinoma in situ, and the interpretation must
  separate the three, because invasion changes treatment, margins and risk substantially.</p>
  <p>Treatment reduces lesion burden but <strong>the surrounding field remains at risk</strong>, so
  surveillance continues even after a successful course.</p>
@@FIG_AK@@
  <h3 class="sub" id="mal-scc">9.3 &middot; Objective 1 &mdash; Squamous cell carcinoma</h3>
  <p>The <strong>second most common</strong> skin cancer, following <strong>prolonged cumulative</strong>
  sun exposure &mdash; contrast basal cell carcinoma, which follows <strong>intense intermittent</strong>
  exposure. It may arise from an actinic keratosis.</p>
  <p>Classically a <strong>small red, conical, hard nodule that may ulcerate</strong>; also a
  <strong>non-healing ulcer</strong>, a warty nodule, or an irregular pink plaque with haemorrhagic
  crust.</p>
  <table>
    <tr><td><b>Red flags</b></td><td>Rapid growth, pain, bleeding, ulceration, induration, fixation, palpable regional nodes</td></tr>
    <tr><td><b>High-risk sites</b></td><td>Mucosal surfaces, lip, ear, scalp, temple, nose, genitalia</td></tr>
    <tr><td><b>Tumour count</b></td><td><b>More than 10</b> means higher local recurrence and nodal metastasis</td></tr>
    <tr><td><b>Immunosuppression</b></td><td>Common and often aggressive after transplant, with multiple tumours typically at <b>about 5 years</b>. Chronic lymphocytic leukaemia and human immunodeficiency virus also raise risk and aggressiveness</td></tr>
    <tr><td><b>Chemoprevention</b></td><td><b>Nicotinamide 500&nbsp;mg orally twice daily</b> reduces new squamous cell carcinoma by <b>about 30%</b> in high-risk patients</td></tr>
  </table>
  <p>Use <strong>time course, firmness or induration, ulceration, site, immune status and
  pathology</strong> to separate it from its differential &mdash; not morphology alone.</p>
  <p><strong>Management by stage.</strong> In situ without high-risk features: imiquimod, topical
  fluorouracil, or curettage and electrodesiccation. Invasive: <strong>surgical excision or Mohs</strong>.
  Advanced or metastatic: <strong>programmed death 1 blockade; cetuximab</strong>.</p>
  <p><strong>Mohs indications</strong> &mdash; high-risk sites (lips, temples, ears, nose, genitalia);
  recurrent tumours; aggressive histology with perineural or perivascular invasion;
  <strong>lesions over 1&nbsp;cm on the face or over 2&nbsp;cm on trunk or extremities</strong>;
  immunosuppression; tumours within scars; genetic disease-associated tumours.</p>
  <p>Follow-up is <strong>at least annual skin AND lymph-node examination</strong>. Referral is urgent
  for high-risk site, size, recurrence, aggressive histology, immunosuppression,
  <strong>neurologic symptoms</strong> or nodal disease. Metastatic rate for actinically induced
  disease: <strong>3 to 7%</strong>.</p>
@@FIG_SCC@@
  <h3 class="sub" id="mal-bcc">9.4 &middot; Objective 1 &mdash; Basal cell carcinoma</h3>
  <p><strong>The most common form of cancer.</strong> The <strong>histologic</strong> subtype
  determines behaviour and dictates treatment &mdash; not the clinical appearance.</p>
  <table>
    <tr><th>Subtype</th><th>What you see</th></tr>
    <tr><td><b>Nodular</b></td><td>Papule or nodule with central erosion, slow growth over years to 1&ndash;2&nbsp;cm; <b>pearly or translucent with telangiectasias accentuated by STRETCHING the skin</b></td></tr>
    <tr><td><b>Pigmented</b></td><td>Stippled or focal pigmentation that <b>may mimic melanocytic disease</b>; the pearly border and slow growth discriminate</td></tr>
    <tr><td><b>Superficial</b></td><td>Reddish, shiny, scaly thin papules or plaques on <b>back or chest</b>; may have a thready pearly border and spotty edge pigmentation</td></tr>
    <tr><td><b>Morpheaform / sclerosing</b></td><td><b>Scar-like or ivory-white</b>, with clinically subtle extension beyond the visible pink segment &mdash; <b>higher risk of subclinical spread</b></td></tr>
  </table>
  <p><strong>Warning patterns:</strong> a pearly papule, an erythematous patch larger than 6&nbsp;mm, or
  a non-healing ulcer &mdash; commonly on face, trunk or lower legs.</p>
  <p><strong>Numbers worth holding.</strong> A second basal cell carcinoma develops in
  <strong>up to 50%</strong> of patients, so at least annual full-skin examination is mandatory.
  <strong>Nicotinamide 500&nbsp;mg twice daily reduces development by about 20%</strong> &mdash; note
  that is the 20%, against 30% for squamous cell carcinoma. <strong>Excision recurrence 5% or
  less; Mohs cure about 98%.</strong></p>
  <p>Selected superficial disease may be treated topically: <strong>imiquimod five nights weekly for
  6 to 10 weeks</strong>, or <strong>fluorouracil twice daily for up to 12 weeks</strong>, with
  <strong>clinical clearance confirmed afterwards</strong>. Advanced or metastatic disease:
  <strong>hedgehog pathway inhibitors &mdash; vismodegib or sonidegib</strong>.</p>
  <p>Prognosis is usually slow-growing and highly curable when treated early; the morbidity comes from
  <strong>local destruction</strong>, recurrence, delayed diagnosis and anatomically complex sites
  rather than from spread.</p>
@@FIG_BCC@@
  <h3 class="sub" id="mal-melanoma">9.5 &middot; Objective 1 &mdash; Malignant melanoma</h3>
  <p><strong>The 4th most common cancer in the United States and the leading cause of death due to
  skin disease.</strong> Incidence doubled over the preceding 30 years, while mortality has fallen
  with earlier detection and immunotherapy. 2023 figures: about <strong>97,610</strong> new invasive
  melanomas, about <strong>7,990</strong> deaths, roughly <strong>two-thirds of deaths in men</strong>.
  Lifetime risk about <strong>2% in white individuals</strong> and <strong>0.1 to 0.5% in persons of
  colour</strong> &mdash; lower, but not zero, which is why acral and nail sites still get checked.</p>
  <table>
    <tr><th>Subtype</th><th>Behaviour</th></tr>
    <tr><td><b>Superficial spreading</b> (~2/3)</td><td>Intermittently sun-exposed skin; evolves radially before vertical growth</td></tr>
    <tr><td><b>Lentigo maligna</b></td><td>Chronically sun-exposed skin of older adults; slow radial growth phase</td></tr>
    <tr><td><b>Nodular</b></td><td><b>Rapidly growing; often amelanotic; may LACK the classic features</b> &mdash; high-risk for exactly that reason</td></tr>
    <tr><td><b>Acral lentiginous</b></td><td>Palms, soles and nail units</td></tr>
  </table>
  <p><strong>ABCDE:</strong> <strong>A</strong>symmetry &middot; <strong>B</strong>order irregular,
  notched or poorly defined &middot; <strong>C</strong>olour variegation &mdash; brown, red, white,
  black, blue within one lesion &middot; <strong>D</strong>iameter greater than 6&nbsp;mm,
  <strong>though smaller lesions can be melanoma</strong> &middot; <strong>E</strong>volution.</p>
  <p class="prof-lead"><mark class="prof-highlight">The next three items exist only as pictures in the
  deck.</mark></p>
  <table>
    <tr><th>Clark level (slide 50)</th><th>What it means</th></tr>
    <tr><td>I</td><td>Confined to the <b>epidermis</b></td></tr>
    <tr><td>II</td><td>Into the <b>papillary dermis</b></td></tr>
    <tr><td>III</td><td><b>Filling</b> the papillary dermis</td></tr>
    <tr><td>IV</td><td>Into the <b>reticular dermis</b></td></tr>
    <tr><td>V</td><td>Into the <b>subcutaneous tissue</b></td></tr>
  </table>
  <p><strong>Clark level is an anatomic layer; Breslow thickness is a measurement &mdash; and Breslow
  is the dominant prognostic variable</strong>, which must be measured accurately at the initial
  biopsy. Ulceration and mitotic activity further modify stage-based prognosis.</p>
  <table>
    <tr><th>Stage (slide 53)</th><th>Meaning</th><th>TNM anchor (slide 54)</th></tr>
    <tr><td><b>0</b></td><td>Confined to the epidermal region of skin</td><td>Tis, N0, M0</td></tr>
    <tr><td><b>I</b></td><td>Localised, only in skin and very thin</td><td>T1&ndash;T2a, N0, M0</td></tr>
    <tr><td><b>II</b></td><td>Localised, thicker than stage I</td><td>T2b&ndash;T4b, N0, M0</td></tr>
    <tr><td><b>III</b></td><td><b>Spread to lymph nodes</b></td><td>Any N&ge;N1, M0</td></tr>
    <tr><td><b>IV</b></td><td><b>Spread to other organs</b></td><td>Any T, any N, <b>M1</b></td></tr>
  </table>
  <p>In the staging table, <strong>T is primary tumour thickness, N is the number of tumour-involved
  regional lymph nodes, and M is the number of metastases at a distant site</strong>.</p>
  <p><strong>Sentinel lymph node biopsy</strong> is offered or discussed at
  <strong>1.0&nbsp;mm or greater</strong> Breslow thickness, or <strong>0.8&nbsp;mm or greater</strong>
  with additional histologic risk factors &mdash; ulceration, high mitotic rate, or lymphovascular
  invasion. It is a <strong>staging procedure and may not itself improve overall survival</strong>,
  which is the honest thing to tell a patient.</p>
  <table>
    <tr><th>Re-excision margin</th><th>Thickness</th></tr>
    <tr><td>0.5 to 1&nbsp;cm</td><td>In situ</td></tr>
    <tr><td>1&nbsp;cm</td><td>Less than 1&nbsp;mm</td></tr>
    <tr><td>1 to 2&nbsp;cm</td><td>More than 1&nbsp;mm</td></tr>
  </table>
  <p><strong>Refer to an expert centre</strong> for melanoma deeper than 1&nbsp;mm, or with lymph-node
  or other-site spread. Patients perform <strong>monthly self-examination</strong> using ABCDE and
  ugly-duckling principles, <strong>including scalp, back, palms, soles and nails</strong>.</p>
@@FIG_MEL@@
  <h3 class="sub" id="mal-ks-ctcl">9.6 &middot; Objective 1 &mdash; Kaposi sarcoma and cutaneous T-cell lymphoma</h3>
  <p><strong>Kaposi sarcoma</strong> is caused by <strong>human herpesvirus 8 combined with a weakened
  immune system</strong>, arising in the cells lining blood and lymph vessels. Red or purple macules,
  plaques or nodules on skin <em>or mucous membranes</em>.</p>
  <table>
    <tr><th>Form</th><th>Population and course</th><th>First move</th></tr>
    <tr><td><b>Classic</b></td><td>Older men; chronic; rarely fatal</td><td>Palliative local therapy &mdash; intralesional vincristine, vinblastine or bleomycin, or radiation</td></tr>
    <tr><td><b>Endemic</b></td><td>Young Black men in equatorial Africa; often aggressive, can be rapidly fatal</td><td>As clinically indicated</td></tr>
    <tr><td><b>Iatrogenic</b></td><td>With immunosuppressive therapy</td><td><b>Reduce immunosuppressive doses where feasible &mdash; coordinate with the transplant team first</b></td></tr>
    <tr><td><b>Epidemic</b></td><td>Acquired immunodeficiency</td><td><b>Begin or optimise antiretroviral therapy</b> &mdash; immune restoration is the cornerstone</td></tr>
  </table>
  <p>Two examination points carry disproportionate weight. <strong>Oral examination is essential</strong>
  when Kaposi sarcoma is suspected, because hard-palate lesions are common and may be the presenting
  site. And <strong>marked oedema may occur with few or no visible skin lesions</strong> &mdash; so do
  not use oedema severity to gauge disease burden.</p>
  <p>Systemic first-line is <strong>liposomal doxorubicin and paclitaxel</strong>, and
  <strong>antiretroviral therapy plus chemotherapy is more effective than antiretroviral therapy
  alone</strong> in advanced disease.</p>
  <p><strong>Cutaneous T-cell lymphoma</strong> (mycosis fungoides) begins in the skin and
  <strong>may remain confined there for years or decades</strong>. Early: localised or generalised
  erythematous patches or scaly plaques, usually on the trunk, frequently larger than 5&nbsp;cm, and
  it <strong>resembles psoriasis, eczema or tinea</strong> &mdash; which is why it is diagnosed
  late.</p>
  <p><strong>Two clues to hold:</strong> <strong>itch out of proportion to the apparent inflammatory
  activity</strong>, and <strong>follicular involvement with hair loss</strong>. Folliculotropism is
  what discriminates it from routine eczema or psoriasis.</p>
  <p><strong>The management philosophy is the exam point.</strong> Early aggressive treatment
  <strong>has not been proven to cure disease or prevent progression</strong>, and overly aggressive
  therapy <strong>may cause complications and premature death</strong>. A stage-directed, skin-first
  approach suits most early disease: topical corticosteroids, topical mechlorethamine, bexarotene gel,
  ultraviolet phototherapy.</p>
@@FIG_KS@@
  <h3 class="sub" id="mal-nail">9.7 &middot; Objective 1 &mdash; Nail unit neoplasms</h3>
  <p>The deck calls <strong>diagnostic delay a recurring theme and a preventable harm</strong> in this
  module, and every item below is arranged around that.</p>
  <table>
    <tr><th>Tumour</th><th>Pattern</th></tr>
    <tr><td><b>Nail unit melanoma</b></td><td>Rare acral melanoma, most often from the <b>matrix</b>. <b>Not clearly ultraviolet-driven; any skin tone.</b> <b>Thumb and great toe</b>. New or evolving <b>longitudinal melanonychia in ONE digit</b>, increasing width, irregular colour/thickness/spacing, <b>proximal widening or triangular shape</b>, blurred borders, nail splitting, ulceration or subungual mass</td></tr>
    <tr><td><b>Nail unit squamous cell carcinoma / Bowen</b></td><td><b>The most common malignant nail tumour.</b> Chronic unilateral verrucous periungual papule or plaque, subungual hyperkeratosis, onycholysis, oozing, bleeding, nail-plate destruction, longitudinal erythronychia &mdash; <b>often repeatedly labelled a wart, paronychia or fungal infection</b>. Associations: high-risk human papillomavirus, immunosuppression, chronic inflammation or trauma, prior radiation, older age</td></tr>
    <tr><td><b>Nail unit basal cell carcinoma</b></td><td><b>Exceptionally uncommon</b> &mdash; consider it in a persistent ulcerated or pearly lesion of the nail fold or bed</td></tr>
    <tr><td><b>Glomus tumour</b></td><td>Small <b>red-blue subungual focus</b> with <b>severe paroxysmal pain, exquisite point tenderness and cold sensitivity</b>; the nail may look nearly normal. The triad suggests it but <b>does not replace imaging or specialist evaluation</b></td></tr>
    <tr><td><b>Onychopapilloma / onychomatricoma</b></td><td>A single nail with longitudinal <b>erythronychia or leukonychia</b>, distal subungual hyperkeratosis, splinter haemorrhages or localised plate abnormality</td></tr>
  </table>
  <p><strong>Hutchinson sign</strong> &mdash; periungual pigment extending onto the
  <strong>proximal nail fold</strong> &mdash; is highly concerning for nail unit melanoma and should
  prompt <strong>urgent expert evaluation regardless of other features</strong>. (Note this is a
  different sign of the same name from the zoster ophthalmicus one in Lecture 6.)</p>
  <p><strong>Amelanotic nail melanoma</strong> may be red, pink, eroded or mass-like <strong>with no
  dark band at all &mdash; the absence of pigment does NOT exclude melanoma</strong>. Consider biopsy
  for any unexplained, progressive single-nail lesion.</p>
  <p>Before you inspect: <strong>remove the polish</strong> and examine <em>every</em> nail, the
  periungual skin, palms and soles, and the regional nodes.</p>
  <p><strong>Amputation is not automatic.</strong> Contemporary care is digit-sparing wide excision or
  Mohs with immunostaining where margins can be reliably assessed; amputation is reserved for deep,
  extensive or bone-involving disease. For nail unit squamous cell carcinoma,
  <strong>complete margin-controlled surgery is preferred</strong> and partial destructive treatment
  carries a higher recurrence risk.</p>
@@FIG_NAIL@@
  <h3 class="sub" id="mal-age">9.8 &middot; Objective 11 &mdash; Care strategies in adults and the elderly</h3>
  <table>
    <tr><th>Population</th><th>What changes</th></tr>
    <tr><td><b>Adult</b></td><td>Cumulative and intermittent ultraviolet exposure both accumulate through working life. <b>Immunosuppression and transplant status</b> dominate risk: squamous cell carcinoma is common and aggressive after transplant, typically multiple at about 5 years, and <b>nicotinamide 500&nbsp;mg twice daily</b> is a real option. Melanoma self-examination is monthly and lifelong. Kaposi sarcoma in this group is usually epidemic or iatrogenic &mdash; treat the immune state first.</td></tr>
    <tr><td><b>Elderly</b></td><td>Actinic keratosis burden and <b>field cancerization</b> rise with cumulative exposure &mdash; favour field-directed therapy. Lentigo maligna arises on chronically sun-exposed skin of older adults. <b>Classic Kaposi sarcoma</b> is a disease of older men and is managed palliatively rather than aggressively. In cutaneous T-cell lymphoma, the deck's warning that overly aggressive therapy may cause <b>premature death</b> weighs most heavily here. Basal cell carcinoma&rsquo;s <b>up-to-50% second-primary rate</b> makes annual full-skin examination non-negotiable.</td></tr>
  </table>
  <p><strong>Immunosuppression cuts across both</strong> and moves every answer the same way: more
  disease, more aggressive disease, a lower threshold for biopsy and for Mohs, and earlier referral.</p>
</section>

"""

TOC = """  <a class="top-link" href="#malignant-lesions">9 &middot; Pre-Malignant and Malignant Cutaneous Lesions</a>
  <a href="#mal-approach">9.1 Objective 1 &mdash; Describe before you name</a>
  <a href="#mal-ak">9.2 Objective 1 &mdash; Actinic keratosis</a>
  <a href="#mal-scc">9.3 Objective 1 &mdash; Squamous cell carcinoma</a>
  <a href="#mal-bcc">9.4 Objective 1 &mdash; Basal cell carcinoma</a>
  <a href="#mal-melanoma">9.5 Objective 1 &mdash; Malignant melanoma</a>
  <a href="#mal-ks-ctcl">9.6 Objective 1 &mdash; Kaposi sarcoma &amp; cutaneous T-cell lymphoma</a>
  <a href="#mal-nail">9.7 Objective 1 &mdash; Nail unit neoplasms</a>
  <a href="#mal-age">9.8 Objective 11 &mdash; Adults and the elderly</a>
"""

FIGS = {
 "@@FIG_AK@@": grid([("l9_s008_2", "Actinic keratosis", "Rough sandpaper papules on sun-exposed skin", 8)]),
 "@@FIG_SCC@@": grid([("l9_s019_1", "Squamous cell carcinoma", "Red conical hard nodule, often ulcerated", 19)]),
 "@@FIG_BCC@@": grid([
   ("l9_s029_1", "Basal cell carcinoma &mdash; nodular", "Pearly papule with central erosion and telangiectasias", 29),
   ("l9_s034_2", "Basal cell carcinoma &mdash; superficial", "Reddish shiny scaly thin plaque on back or chest", 34),
   ("l9_s030_2", "Basal cell carcinoma &mdash; pigmented", "Stippled pigment that mimics melanocytic disease", 30)]),
 "@@FIG_MEL@@": grid([
   ("l9_s044_2", "Acral melanoma", "Palms, soles and nail units &mdash; any skin tone", 44),
   ("l9_s045_1", "Nail unit melanoma", "Longitudinal melanonychia widening in a single digit", 45)]),
 "@@FIG_KS@@": grid([
   ("l9_s062_4", "Kaposi sarcoma &mdash; oral", "Hard palate lesions may be the presenting site", 62),
   ("l9_s072_1", "Cutaneous T-cell lymphoma", "Patches and plaques on the trunk, mistaken for eczema", 72)]),
 "@@FIG_NAIL@@": grid([
   ("l9_s082_1", "Nail unit squamous cell carcinoma", "Chronic periungual disease with nail-plate destruction", 82),
   ("l9_s087_1", "Longitudinal erythronychia", "A single nail &mdash; onychopapilloma or onychomatricoma", 87)]),
}

RENUMBER = [
 ('<h2 class="deck-title">9 &middot; How this course is built</h2>',
  '<h2 class="deck-title">10 &middot; How this course is built</h2>'),
 ('href="#how-course-works" style="color:#8a6508">9 &middot; How this course is built</a>',
  'href="#how-course-works" style="color:#8a6508">10 &middot; How this course is built</a>'),
]


def main():
    src = open(GUIDE, encoding="utf-8").read()
    for o, c in ((OPEN, CLOSE), (TOC_OPEN, TOC_CLOSE)):
        if o in src:
            src = re.sub(re.escape(o) + r".*?" + re.escape(c), "", src, flags=re.S)

    body = SECTION
    for token, html in FIGS.items():
        assert token in body, "figure token %s never used" % token
        body = body.replace(token, html)
    assert "@@" not in body

    for old, new in RENUMBER:
        if new in src and old not in src:
            continue
        assert src.count(old) == 1, "renumber target not found once: %r" % old
        src = src.replace(old, new, 1)

    toc_anchor = '  <a class="top-link" href="#how-course-works"'
    assert src.count(toc_anchor) == 1
    src = src.replace(toc_anchor, TOC_OPEN + "\n" + TOC + TOC_CLOSE + "\n" + toc_anchor, 1)

    sec_anchor = '  <h2 class="deck-title">10 &middot; How this course is built</h2>'
    i = src.index(sec_anchor)
    j = src.rindex("<section", 0, i)
    src = src[:j] + OPEN + body + CLOSE + "\n\n" + src[j:]

    assert src.count('id="malignant-lesions"') == 1
    assert 'loading="lazy"' not in "".join(re.findall(r"<img\b[^>]*>", src))
    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "li"):
        o = len(re.findall(r"<%s[ >]" % tag, src)); c = src.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d/%d" % (tag, o, c)
    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added section 9 (%d subsections, %d photographs); How this course is built 9 -> 10"
          % (len(re.findall(r'<h3 class="sub" id="mal-', src)),
             len(re.findall(r'<figure><img src="cms-derm-chart-images/l9_', src))))


if __name__ == "__main__":
    main()
