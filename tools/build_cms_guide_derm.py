#!/usr/bin/env python3
"""Add the dermatology block sections to the CMS I Exam 1 study guide.

Adds sections for Lectures 2, 3, 4, 5 and 8 -- the five Exam 1 lectures posted so
far -- and renumbers "How this course is built" to sit last.

Instructional Objectives are quoted VERBATIM from the PAJ 5500 syllabus, per the
guide verbatim-IO rule, and each subsection answers one objective in order.
Lecture numbering follows the syllabus order, so the guide skips 6, 7 and 9
until those decks are posted.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
GUIDE = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1",
                     "cms-exam-1-study-guide.html")

# The one objective every dermatology lecture in this block opens with, quoted
# verbatim from the syllabus. Only the trailing noun phrase changes.
IO_MAIN = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical "
           "manifestations, differential diagnosis, diagnostic testing (including ordering and "
           "interpretation), management (acute and chronic, including applicable rehabilitative "
           "and palliative care), appropriate referrals, patient education, and prognosis of the "
           "following %s:")


def io_box(items):
    lis = "\n".join("      <li>%s</li>" % x for x in items)
    return ('  <div class="io-box">\n    <h3>Instructional Objectives</h3>\n'
            '    <ol type="a">\n%s\n    </ol>\n  </div>\n' % lis)


def lst(items):
    return "<ol>%s</ol>" % "".join("<li>%s</li>" % i for i in items)


SECTIONS = []

# ---------------------------------------------------------------- Lecture 2
SECTIONS.append(dict(
    num=2, sid="general-derm-1", title="General Dermatology I",
    toc=[("gd1-anatomy", "2.1 Objectives a &amp; b &mdash; Anatomy &amp; physiology of the skin"),
         ("gd1-eczema", "2.2 Objective c &mdash; The eczema and dermatitis family"),
         ("gd1-bullous", "2.3 Objective c &mdash; Vesiculobullous disease"),
         ("gd1-papulo", "2.4 Objective c &mdash; Papulosquamous disease"),
         ("gd1-alopecia", "2.5 Objective c &mdash; Alopecia")],
    ios=["Review anatomy of the integumentary system",
         "Review physiology of the integumentary system",
         IO_MAIN % "dermatological conditions" + " " +
         lst(["Eczema", "Diaper", "Nummular", "Periorbital", "Dyshidrosis", "Dermatitis",
              "Atopic", "Diaper", "Stasis", "Contact", "Seborrheic", "Perioral", "Xeroderma",
              "Vesiculobullous disease", "Bullous pemphigoid", "Pemphigus", "Psoriasis",
              "Pityriasis rosea", "Lichen planus and lichen simplex dermatitis", "Alopecia",
              "Areata", "Androgenetic"])],
    body="""
  <h3 class="sub" id="gd1-anatomy">2.1 &middot; Objectives a &amp; b &mdash; Review anatomy and physiology of the integumentary system</h3>
  <p>The skin is the largest organ of the body, and everything in this block rests on knowing which
  layer a disease sits in. The three layers, outermost first:</p>
  <table>
    <tr><th>Layer</th><th>What is in it</th><th>Why it matters clinically</th></tr>
    <tr><td><strong>Epidermis</strong></td>
        <td>Keratinocytes in five strata, melanocytes, Langerhans cells, Merkel cells. Avascular &mdash; fed by diffusion from the dermis.</td>
        <td>Impetigo, pemphigus and the superficial fungal infections live here. Loss of this layer alone means no scarring.</td></tr>
    <tr><td><strong>Dermis</strong></td>
        <td>Collagen and elastin, blood vessels, nerves, hair follicles, sebaceous and sweat glands.</td>
        <td>Erysipelas, cellulitis and bullous pemphigoid involve this layer. Damage here scars.</td></tr>
    <tr><td><strong>Subcutaneous tissue</strong></td>
        <td>Fat, larger vessels, the base of the follicles.</td>
        <td>Furuncles, abscesses and panniculitis such as erythema nodosum sit at this depth.</td></tr>
  </table>
  <div class="callout"><strong>The layer question answers half the differentials in this block.</strong>
  Impetigo is epidermal, erysipelas is upper dermis with lymphatic involvement, cellulitis is deeper
  dermis and subcutaneous tissue, necrotizing fasciitis is below all of it. That single axis separates
  four conditions that otherwise all present as a red, warm leg.</div>
  <p><strong>Physiology.</strong> The skin provides a barrier against water loss, chemicals and
  microorganisms; regulates temperature through vasodilation, vasoconstriction and sweating; carries
  the sensory apparatus for touch, pressure, temperature and pain; synthesises vitamin D under
  ultraviolet B; and performs immune surveillance through Langerhans cells.</p>

  <h3 class="sub" id="gd1-eczema">2.2 &middot; Objective c &mdash; The eczema and dermatitis family</h3>
  <p>Eczema and dermatitis name the same reaction pattern. What distinguishes the members is
  <em>distribution</em>, <em>trigger</em> and <em>age</em> rather than the appearance of an individual
  lesion.</p>
  <table>
    <tr><th>Condition</th><th>Who and where</th><th>The defining feature</th></tr>
    <tr><td>Atopic dermatitis</td><td>Infants on cheeks and extensors; children and adults in flexures</td><td>Personal or family atopy &mdash; asthma, hay fever, food allergy</td></tr>
    <tr><td>Contact dermatitis</td><td>Anywhere the contactant touched</td><td>Sharp margins in the shape of the exposure; patch testing identifies it</td></tr>
    <tr><td>Seborrheic dermatitis</td><td>Scalp, eyebrows, nasolabial folds, ears, central chest</td><td>Greasy yellow scale on erythema in sebum-rich sites</td></tr>
    <tr><td>Nummular eczema</td><td>Extremities, often older adults</td><td>Discrete coin-shaped plaques</td></tr>
    <tr><td>Dyshidrotic eczema</td><td>Palms, soles, sides of fingers</td><td>Deep-seated tapioca-like vesicles, intensely itchy</td></tr>
    <tr><td>Stasis dermatitis</td><td>Lower legs, gaiter area, bilateral</td><td>Venous insufficiency with oedema and haemosiderin pigmentation</td></tr>
    <tr><td>Diaper dermatitis</td><td>Convex surfaces of the napkin area</td><td>Spares the skin folds; candidal overgrowth involves them with satellite lesions</td></tr>
    <tr><td>Perioral dermatitis</td><td>Around the mouth, sparing the vermilion border</td><td>Often follows topical corticosteroid use on the face</td></tr>
    <tr><td>Periorbital dermatitis</td><td>Eyelids and around the eyes</td><td>Thin skin, so potent steroids are avoided</td></tr>
    <tr><td>Xeroderma</td><td>Shins and forearms, worse in winter</td><td>Dry cracked skin from impaired barrier function</td></tr>
  </table>
  <div class="pearl"><strong>Stasis dermatitis versus cellulitis</strong> is the mistake that lands
  patients on unnecessary antibiotics. Stasis dermatitis is bilateral, chronic, itchy and afebrile.
  Cellulitis is unilateral, acute, tender and often febrile. &ldquo;Bilateral cellulitis&rdquo; is
  almost always stasis dermatitis.</div>

  <h3 class="sub" id="gd1-bullous">2.3 &middot; Objective c &mdash; Vesiculobullous disease</h3>
  <table>
    <tr><th></th><th>Bullous pemphigoid</th><th>Pemphigus vulgaris</th></tr>
    <tr><td>Age</td><td>Elderly</td><td>Middle-aged</td></tr>
    <tr><td>Split level</td><td>Subepidermal &mdash; below the whole epidermis</td><td>Intraepidermal &mdash; within the epidermis</td></tr>
    <tr><td>Bullae</td><td>Tense, do not rupture easily</td><td>Flaccid, rupture easily leaving erosions</td></tr>
    <tr><td>Nikolsky sign</td><td>Negative</td><td>Positive</td></tr>
    <tr><td>Mucosal involvement</td><td>Uncommon</td><td>Common, often the first site</td></tr>
    <tr><td>Prognosis</td><td>Better</td><td>Worse; was frequently fatal before corticosteroids</td></tr>
  </table>
  <div class="callout"><strong>Deeper split, tougher blister.</strong> Bullous pemphigoid separates
  <em>below</em> the epidermis, so the roof of the blister is the full thickness of epidermis and the
  blister is tense. Pemphigus separates <em>within</em> the epidermis, so the roof is a few cell layers
  and the blister collapses. That one fact generates the tense-versus-flaccid difference and the
  Nikolsky sign together.</div>

  <h3 class="sub" id="gd1-papulo">2.4 &middot; Objective c &mdash; Papulosquamous disease</h3>
  <table>
    <tr><th>Condition</th><th>Lesion</th><th>Distribution and course</th></tr>
    <tr><td>Psoriasis</td><td>Well-demarcated plaques with thick silvery scale; Auspitz sign on removal</td><td>Extensor surfaces, scalp, nails; chronic and relapsing</td></tr>
    <tr><td>Pityriasis rosea</td><td>Herald patch first, then smaller oval lesions with a collarette of scale</td><td>Christmas-tree pattern along skin lines on the trunk; self-limiting over 6 to 8 weeks</td></tr>
    <tr><td>Lichen planus</td><td>Purple, polygonal, pruritic, planar papules; Wickham striae on the surface</td><td>Flexor wrists, ankles, oral mucosa</td></tr>
    <tr><td>Lichen simplex chronicus</td><td>Thickened lichenified plaque with accentuated skin markings</td><td>Wherever the patient can reach to scratch; the itch-scratch cycle sustains it</td></tr>
  </table>
  <p>The <strong>six Ps</strong> for lichen planus &mdash; purple, polygonal, pruritic, planar, papules
  and plaques &mdash; is worth memorising because the description alone is close to diagnostic.</p>

  <h3 class="sub" id="gd1-alopecia">2.5 &middot; Objective c &mdash; Alopecia</h3>
  <table>
    <tr><th></th><th>Alopecia areata</th><th>Androgenetic alopecia</th></tr>
    <tr><td>Pattern</td><td>Discrete smooth round patches of complete loss</td><td>Gradual thinning &mdash; temporal recession and vertex in men, widened part in women</td></tr>
    <tr><td>Mechanism</td><td>Autoimmune attack on the hair follicle</td><td>Androgen-driven follicular miniaturisation with a genetic component</td></tr>
    <tr><td>Clue on examination</td><td>Exclamation point hairs at the edge of a patch</td><td>Preserved follicular openings with progressively finer hairs</td></tr>
    <tr><td>Scarring</td><td>Non-scarring &mdash; regrowth is possible</td><td>Non-scarring, but the miniaturisation is progressive</td></tr>
    <tr><td>Treatment</td><td>Intralesional or topical corticosteroid; associated with other autoimmune disease</td><td>Topical minoxidil; finasteride in men</td></tr>
  </table>
"""))

# ---------------------------------------------------------------- Lecture 3
SECTIONS.append(dict(
    num=3, sid="general-derm-2", title="Dermatology II",
    toc=[("gd2-reactive", "3.1 Objective a &mdash; Reactive and immune-mediated conditions"),
         ("gd2-systemic", "3.2 Objective a &mdash; Lesions that signal systemic disease"),
         ("gd2-sjsten", "3.3 Objective a &mdash; Stevens-Johnson syndrome and toxic epidermal necrolysis"),
         ("gd2-photo", "3.4 Objective a &mdash; Photoreactions and photodermatology")],
    ios=[IO_MAIN % "dermatological conditions" + " " +
         lst(["Erythema multiforme", "Dermatitis herpetiformis", "Acanthosis nigricans",
              "Epidermolysis bullosa", "Urticaria", "Erythema nodosum", "Granuloma annulare",
              "Pyoderma gangrenosum", "Acne rosacea", "Hyperhidrosis", "Drug Eruptions",
              "Steven Johnson Syndrome", "Toxic epidermal necrolysis", "Photoreactions",
              "Sunburn", "Photosensitivity &mdash; drug-induced, photodermatitis, polymorphous light eruption",
              "Solar lentigo, keratosis", "Dermatoheliosis"])],
    body="""
  <h3 class="sub" id="gd2-reactive">3.1 &middot; Objective a &mdash; Reactive and immune-mediated conditions</h3>
  <table>
    <tr><th>Condition</th><th>Defining feature</th><th>The one thing to carry into the exam</th></tr>
    <tr><td>Erythema multiforme</td><td>Target lesions with three zones, acral distribution</td><td>Herpes simplex virus triggers over 50% of cases</td></tr>
    <tr><td>Urticaria</td><td>Wheals that individually resolve within 24 hours</td><td>A wheal persisting beyond 24 hours means biopsy for urticarial vasculitis</td></tr>
    <tr><td>Erythema nodosum</td><td>Tender bilateral anterior shin nodules that do not ulcerate</td><td>Sarcoidosis, inflammatory bowel disease, tuberculosis, streptococcus, drugs</td></tr>
    <tr><td>Granuloma annulare</td><td>Annular ring of papules with <em>no scale</em> on the border</td><td>Absent scale is what separates it from tinea</td></tr>
    <tr><td>Pyoderma gangrenosum</td><td>Rapidly enlarging ulcer with an undermined violaceous border</td><td>Pathergy &mdash; debridement makes it worse, so do not debride</td></tr>
    <tr><td>Acne rosacea</td><td>Central facial erythema with flushing and telangiectasias, no comedones</td><td>Absence of comedones separates it from acne vulgaris</td></tr>
    <tr><td>Hyperhidrosis</td><td>Primary is bilateral, focal, adolescent onset, absent in sleep</td><td>Generalised or nocturnal sweating means look for a secondary cause</td></tr>
  </table>
  <div class="pearl"><strong>Pyoderma gangrenosum is the one that punishes the reflex.</strong> Every
  instinct with a necrotic ulcer says debride. Here debridement enlarges it. The bowel disease history
  and the undermined violaceous border are the signals to stop and think.</div>

  <h3 class="sub" id="gd2-systemic">3.2 &middot; Objective a &mdash; Lesions that signal systemic disease</h3>
  <table>
    <tr><th>Skin finding</th><th>What to screen for</th></tr>
    <tr><td>Dermatitis herpetiformis</td><td>Coeliac disease in all patients; autoimmune thyroid disease; T-cell lymphoma</td></tr>
    <tr><td>Acanthosis nigricans</td><td>Type 2 diabetes, polycystic ovarian syndrome, metabolic syndrome; gastrointestinal malignancy where onset is sudden in an adult</td></tr>
    <tr><td>Erythema nodosum</td><td>Chest radiograph, antistreptolysin O titre, tuberculin or interferon gamma testing, colonoscopy</td></tr>
    <tr><td>Pyoderma gangrenosum</td><td>Inflammatory bowel disease in 25 to 50%; haematologic malignancy; monoclonal gammopathy; rheumatoid arthritis</td></tr>
    <tr><td>Generalised granuloma annulare</td><td>Diabetes, thyroid disease, dyslipidaemia; lymphoma in adults over fifty</td></tr>
    <tr><td>Secondary hyperhidrosis</td><td>Phaeochromocytoma, hyperthyroidism, lymphoma, menopause</td></tr>
  </table>
  <p><strong>Dermatitis herpetiformis</strong> is diagnosed by perilesional direct immunofluorescence
  showing <em>granular immunoglobulin A</em> deposits at the dermal papillae. Treatment is dapsone for
  rapid symptom control plus a lifelong gluten-free diet, which is what allows dapsone to be tapered.</p>
  <p><strong>Epidermolysis bullosa</strong> is diagnosed by transmission electron microscopy with
  immunofluorescence antigen mapping, supported by a genetic panel.</p>

  <h3 class="sub" id="gd2-sjsten">3.3 &middot; Objective a &mdash; Stevens-Johnson syndrome and toxic epidermal necrolysis</h3>
  <table>
    <tr><th></th><th>Stevens-Johnson syndrome</th><th>Overlap</th><th>Toxic epidermal necrolysis</th></tr>
    <tr><td>Epidermal detachment</td><td>Under 10% body surface</td><td>10 to 30%</td><td>Over 30%</td></tr>
    <tr><td>Mortality</td><td>1 to 5%</td><td>Intermediate</td><td>30 to 35%</td></tr>
  </table>
  <p>Both are severe type IV hypersensitivity reactions, drug-induced in over 80% of cases. The leading
  culprits are the <strong>aromatic anticonvulsants</strong> (carbamazepine, phenytoin, lamotrigine,
  phenobarbital), <strong>sulfonamide antibiotics</strong>, <strong>allopurinol</strong> (the commonest
  cause worldwide and in Asia), oxicam nonsteroidal anti-inflammatory drugs and nevirapine. Mycoplasma
  pneumoniae and herpes simplex virus are the infectious triggers, especially in children.</p>
  <table>
    <tr><th colspan="2">SCORTEN &mdash; each variable scores one point, calculated within 24 hours and repeated on day 3</th></tr>
    <tr><td>Age over 40</td><td>Malignancy present</td></tr>
    <tr><td>Heart rate over 120</td><td>Initial detachment over 10% body surface</td></tr>
    <tr><td>Blood urea nitrogen over 28 mg/dL</td><td>Bicarbonate under 20 mEq/L</td></tr>
    <tr><td colspan="2">Glucose over 252 mg/dL</td></tr>
    <tr><th colspan="2">Predicted mortality: 0&ndash;1 &rarr; 3.2% &middot; 2 &rarr; 12% &middot; 3 &rarr; 35% &middot; 4 &rarr; 58% &middot; 5 or more &rarr; 90%</th></tr>
  </table>
  <div class="callout"><strong>The single action that changes survival is stopping the drug.</strong>
  Earlier withdrawal is strongly associated with better outcome and each day of delay worsens the
  prognosis. Everything else &mdash; burn unit, fluids, cyclosporine, intravenous immunoglobulin,
  daily ophthalmology &mdash; follows that. Avoid silver sulfadiazine, because of the sulfonamide
  cross-reaction. Antibiotic prophylaxis is <em>not</em> recommended.</div>
  <p>Human leukocyte antigen associations matter for prescribing: <strong>HLA-B*15:02</strong> with
  carbamazepine, <strong>HLA-B*58:01</strong> with allopurinol. Survivors need lifelong avoidance of the
  drug class, a medical alert bracelet, and first-degree relatives counselled about shared genetic risk.</p>

  <h3 class="sub" id="gd2-photo">3.4 &middot; Objective a &mdash; Photoreactions and photodermatology</h3>
  <table>
    <tr><th></th><th>Phototoxicity</th><th>Photoallergy</th></tr>
    <tr><td>Mechanism</td><td>Non-immunologic, dose-dependent</td><td>Immunologic type IV, dose-independent</td></tr>
    <tr><td>First exposure</td><td>Reacts on it</td><td>Sensitises; reaction on re-exposure</td></tr>
    <tr><td>Timing</td><td>Within hours</td><td>Delayed</td></tr>
    <tr><td>Appearance</td><td>Exaggerated sunburn, confined to exposed skin</td><td>Eczematous and itchy, extending beyond exposed skin</td></tr>
    <tr><td>Drugs</td><td>Tetracyclines (doxycycline), fluoroquinolones, amiodarone, thiazides, furosemide, voriconazole</td><td>Sunscreen chemicals (oxybenzone), sulfonamides, topical antihistamines, phenothiazines</td></tr>
    <tr><td>Test</td><td>Minimal erythema dose testing</td><td>Photopatch testing &mdash; the gold standard</td></tr>
  </table>
  <p><strong>Photopatch reading:</strong> a reaction on the irradiated patch <em>only</em> is
  photoallergy; a reaction on <em>both</em> patches is ordinary contact allergy.</p>
  <table>
    <tr><th>Condition</th><th>The hook</th></tr>
    <tr><td>Sunburn</td><td>Ultraviolet B at 290 to 320 nm, direct DNA damage, onset 3 to 5 hours, peak at 12 to 24 hours</td></tr>
    <tr><td>Phytophotodermatitis</td><td>Furanocoumarins from limes, celery, parsley, fig plus ultraviolet A &rarr; streaked hyperpigmentation</td></tr>
    <tr><td>Polymorphous light eruption</td><td>Commonest idiopathic photodermatosis; spring onset, spares chronically exposed skin, hardens by late summer</td></tr>
    <tr><td>Solar lentigo</td><td>Uniform pigment, moth-eaten border on dermoscopy; lentigo maligna is the lesion to exclude</td></tr>
    <tr><td>Actinic keratosis</td><td>Sandpaper texture; TP53 mutation; field cancerization, so field-directed therapy for confluent disease</td></tr>
    <tr><td>Dermatoheliosis</td><td>Solar elastosis is the histological hallmark; tretinoin is the only agent approved for photoaging</td></tr>
  </table>
  <div class="pearl"><strong>Know the millimetres.</strong> This lecture and the CMS block use a
  <strong>1 cm</strong> threshold for macule versus patch and papule versus plaque, while Clinical
  Pathophysiology uses <strong>5 mm</strong>. Both are correct in their own course &mdash; answer with
  the number the course in front of you uses.</div>
"""))

# ---------------------------------------------------------------- Lecture 4
SECTIONS.append(dict(
    num=4, sid="cutaneous-bacterial", title="Cutaneous Bacterial Infections",
    toc=[("cbi-acne", "4.1 Objective a &mdash; Acne vulgaris"),
         ("cbi-follicular", "4.2 Objective a &mdash; Follicular and glandular infections"),
         ("cbi-spreading", "4.3 Objective a &mdash; Impetigo, erysipelas, cellulitis and abscess"),
         ("cbi-nailnec", "4.4 Objective a &mdash; Paronychia and necrotizing fasciitis"),
         ("cbi-mrsa", "4.5 Objectives b, c &amp; d &mdash; MRSA, primary vs secondary, and age")],
    ios=[IO_MAIN % "cutaneous bacterial infections" + " " +
         lst(["Acne vulgaris", "Impetigo", "Cellulitis", "Erysipelas", "Erythrasma", "Folliculitis",
              "Furuncles", "Carbuncles", "Abscess", "Paronychia/felon", "Hidradenitis suppurativa",
              "Necrotizing fasciitis"]),
         "Discuss unique considerations of methicillin-resistant staphylococcus aureus (MRSA) skin "
         "infections, including risk factors, presentation, and treatment.",
         "Differentiate primary from secondary bacterial infection of the skin.",
         "Identify medical care strategies for cutaneous bacterial infections in the lecture topic "
         "list for the following populations " + lst(["infant", "child", "adolsecent", "adult", "elderly"])],
    body="""
  <h3 class="sub" id="cbi-acne">4.1 &middot; Objective a &mdash; Acne vulgaris</h3>
  <p>Four factors, temporal sequence not fully understood: <strong>follicular
  hyperkeratinisation</strong>, <strong>increased sebum</strong>, <strong>Cutibacterium acnes</strong>
  (an anaerobic Gram-positive rod, formerly Propionibacterium acnes) and <strong>inflammation</strong>
  from the immune response to it. The hallmark lesion is the <strong>comedone</strong>; its absence is
  what rules acne out and rosacea in.</p>
  <table>
    <tr><th>Severity</th><th>2016 American Academy of Dermatology recommendation</th></tr>
    <tr><td>Comedonal</td><td>Topical retinoid; switch to azelaic or salicylic acid if not tolerated</td></tr>
    <tr><td>Mild papulopustular and mixed</td><td>Topical antimicrobial plus topical retinoid, <em>or</em> benzoyl peroxide plus a topical antibiotic</td></tr>
    <tr><td>Moderate papulopustular and mixed</td><td>Topical retinoid <em>and</em> oral antibiotic <em>and</em> topical benzoyl peroxide</td></tr>
    <tr><td>Severe (nodular)</td><td>The same triple combination, <em>or</em> oral isotretinoin as monotherapy</td></tr>
  </table>
  <p><strong>Benzoyl peroxide goes with every antibiotic</strong>, topical or oral, to reduce resistance.
  Oral tetracyclines are kept to three to four months for the same reason.</p>
  <div class="callout"><strong>Isotretinoin safety is examinable in detail.</strong> Negative pregnancy
  tests before starting, monthly during, and five weeks after. iPledge enrolment. One month dispensed at
  a time. Two forms of contraception preferred, one a barrier method. No blood donation while taking it.</div>
  <p><strong>Patient education:</strong> separate tretinoin and benzoyl peroxide by at least three hours;
  wash no more than twice daily with a gentle cleanser and warm water; use non-comedogenic products;
  expect four to six weeks for improvement and three to four months on the back and chest. Scarring out
  of proportion to lesion count suggests the patient is picking.</p>

  <h3 class="sub" id="cbi-follicular">4.2 &middot; Objective a &mdash; Follicular and glandular infections</h3>
  <table>
    <tr><th>Condition</th><th>What it is</th><th>Key discriminator</th></tr>
    <tr><td>Folliculitis</td><td>Inflammation of the follicle wall and ostia &mdash; a follicular pustule</td><td>Pustule pierced by a central hair; Staphylococcus aureus commonest</td></tr>
    <tr><td>Pseudomonas folliculitis</td><td>Pseudomonas aeruginosa from inadequately chlorinated water</td><td>8 hours to 5 days after a hot tub; spares face, neck, palms, soles; self-limiting in 2 to 10 days</td></tr>
    <tr><td>Pseudofolliculitis barbae</td><td>Foreign body reaction to a cut hair re-entering the skin</td><td>Not an infection. Change the shaving, do not just treat the papules</td></tr>
    <tr><td>Furuncle</td><td>Deep abscess of a follicle and adjacent subcutaneous tissue</td><td>Single opening; no antibiotic if afebrile with one lesion under 5 mm</td></tr>
    <tr><td>Carbuncle</td><td>Two or more confluent furuncles with separate heads</td><td>Sieve-like openings, systemic symptoms, and incision and drainage is the mainstay</td></tr>
    <tr><td>Hidradenitis suppurativa</td><td>Inflammation of apocrine glands</td><td>Three criteria: typical lesions, axilla and groin distribution, recurrence more than twice in six months</td></tr>
    <tr><td>Erythrasma</td><td>Corynebacterium minutissimum in the upper stratum corneum</td><td>Coral-red fluorescence under a Wood's lamp</td></tr>
  </table>
  <p><strong>Recurrent folliculitis or furunculosis</strong> means looking for nasal carriage of
  Staphylococcus aureus &mdash; mupirocin ointment in the nasal vestibule twice daily for five days
  &mdash; alongside obesity and diabetes.</p>
  <p><strong>Hidradenitis suppurativa</strong> is the one with a real treatment ladder: prevention
  (smoking cessation is essential, weight loss, avoid heat and friction), topical steroid with topical
  antibiotic, intralesional triamcinolone, oral retinoid, spironolactone or combined oral contraceptive,
  infliximab for severe disease, and <strong>wide excision</strong> for the best chance of cure.</p>

  <h3 class="sub" id="cbi-spreading">4.3 &middot; Objective a &mdash; Impetigo, erysipelas, cellulitis and abscess</h3>
  <table>
    <tr><th></th><th>Impetigo</th><th>Erysipelas</th><th>Cellulitis</th></tr>
    <tr><td>Depth</td><td>Superficial epidermis</td><td>Upper dermis and superficial lymphatics</td><td>Deeper dermis and subcutaneous tissue</td></tr>
    <tr><td>Organism</td><td>Staphylococcus aureus or Streptococcus pyogenes</td><td>Group A streptococcus</td><td>Group A streptococcus or Staphylococcus aureus</td></tr>
    <tr><td>Border</td><td>Crusted erosion</td><td><strong>Raised, sharply demarcated</strong></td><td><strong>Not raised, not demarcated</strong></td></tr>
    <tr><td>Treatment</td><td>Mupirocin topically; cephalexin orally, the drug of choice in children</td><td>Penicillin V; clindamycin if penicillin allergic</td><td>Dicloxacillin or cephalexin; cover MRSA if purulent</td></tr>
  </table>
  <p>Impetigo comes in three forms: <strong>non-bullous</strong> (commonest, honey-coloured adherent
  crust, lymphadenopathy common), <strong>bullous</strong> (exclusively Staphylococcus aureus through
  epidermolytic toxins, tense bullae leaving collarettes, lymphadenopathy uncommon) and
  <strong>ecthyma</strong> (ulcerates into the dermis, thick grey-yellow crust, heals slowly with a scar).</p>
  <div class="callout"><strong>Acute post-streptococcal glomerulonephritis can follow impetigo, and
  antibiotics do not prevent it</strong> &mdash; the immune activation usually precedes treatment.
  Especially in three to seven year olds: sudden oedema, tea-coloured urine, proteinuria, hypertension.</div>
  <p>An <strong>abscess</strong> follows traumatic inoculation, whereas a furuncle arises from an
  infected follicle. If it does not drain spontaneously, incise and drain it.</p>
  <p><strong>The cellulitis pitfall:</strong> tense, cyanotic, bronzed or blanched tissue is
  devitalised. It is not perfused, so antibiotics never reach it, and it needs surgical debridement.
  Expect the leg to look worse on day one, fever gone by 24 hours, inflammation settling over one to two
  weeks. Fever beyond 48 hours means change the antibiotic, guided by culture.</p>

  <h3 class="sub" id="cbi-nailnec">4.4 &middot; Objective a &mdash; Paronychia and necrotizing fasciitis</h3>
  <table>
    <tr><th></th><th>Acute paronychia</th><th>Chronic paronychia</th></tr>
    <tr><td>Cause</td><td>Bacterial, Staphylococcus aureus or Streptococcus pyogenes</td><td>Inflammatory reaction to irritants; Candida albicans commonest</td></tr>
    <tr><td>Trigger</td><td>Manicure, ingrown nail, hangnail, nail biting</td><td>Repeated water immersion &mdash; cleaners, cooks, bartenders, dishwashers, swimmers</td></tr>
    <tr><td>Timing</td><td>2 to 5 days after trauma</td><td>At least 6 weeks</td></tr>
    <tr><td>Treatment</td><td>Warm soaks; incision and drainage if purulent. Clindamycin if nail biting, for oral flora</td><td>Keep hands dry; topical antifungal; oral fluconazole if severe</td></tr>
  </table>
  <div class="pearl"><strong>Necrotizing fasciitis: unrelenting pain out of proportion to
  examination.</strong> Patients are commonly diagnosed with cellulitis, sent home, and return worse.
  No response at 48 hours is the other clue. Later the area stops being tender, because the superficial
  nerves have been destroyed &mdash; that is progression, not improvement. Laboratory tests and imaging
  <em>must not delay</em> surgical debridement. Gas on imaging suggests Clostridium perfringens; Group A
  streptococcus produces none.</div>

  <h3 class="sub" id="cbi-mrsa">4.5 &middot; Objectives b, c &amp; d &mdash; MRSA, primary versus secondary infection, and care across the age range</h3>
  <p><strong>Methicillin-resistant Staphylococcus aureus.</strong> Three oral agents recur across this
  entire lecture: <strong>trimethoprim-sulfamethoxazole, clindamycin and doxycycline</strong>, with
  linezolid and ciprofloxacin in particular settings. The methicillin-sensitive agents are dicloxacillin
  and cephalexin. Culture the material from any drained lesion. Risk groups named include health-care
  workers and teachers, and nasal carriage sustains recurrence.</p>
  <p><strong>Primary versus secondary infection.</strong> A primary infection arises in previously normal
  skin &mdash; impetigo through a minor cut, cellulitis through tinea pedis. A secondary infection arises
  in skin already damaged by another condition &mdash; bullous impetigo invading eczema, or acne lesions
  becoming fluctuant and purulent.</p>
  <table>
    <tr><th>Population</th><th>What changes</th></tr>
    <tr><td>Infant and child</td><td>Impetigo predominates; cephalexin is the drug of choice; doxycycline only over eight years; isolate 24 to 48 hours after starting treatment</td></tr>
    <tr><td>Adolescent</td><td>Acne vulgaris is more common and more severe in males; pseudofolliculitis barbae begins with shaving</td></tr>
    <tr><td>Adult</td><td>Post-adolescent acne is more common in women over 25; hidradenitis suppurativa presents here</td></tr>
    <tr><td>Elderly</td><td>Cellulitis and necrotizing fasciitis carry higher risk; comorbidity and immunosuppression lower the threshold for workup and admission</td></tr>
  </table>
"""))

# ---------------------------------------------------------------- Lecture 5
SECTIONS.append(dict(
    num=5, sid="derm-infestations", title="Dermatological Infestations",
    toc=[("di-scabies", "5.1 Objective a &mdash; Scabies and lice"),
         ("di-bites", "5.2 Objective a &mdash; Bedbugs, fleas, stings and caterpillars"),
         ("di-larva", "5.3 Objective a &mdash; Cutaneous larva migrans and cercarial dermatitis"),
         ("di-spiders", "5.4 Objective a &mdash; Spider bites"),
         ("di-ticks", "5.5 Objective a &mdash; Tick-borne illness"),
         ("di-lesions", "5.6 Objectives b &amp; c &mdash; Primary vs secondary lesions, and age")],
    ios=[IO_MAIN % "dermatological infestations" + " " +
         lst(["Scabies (Sarcoptes scabei)", "Lice (Pediculus humanus capitis)",
              "Bedbugs (Cimex pilosellus)", "Fleas", "Mites", "Cutanea larvae migrans", "Fire ants",
              "Spider bites", "Ticks", "Caterpillar", "Bee stings", "Cercarial dermatitis"]),
         "Differentiate primary from secondary skin lesions",
         "Identify medical care strategies for common dermatological infestations in the lecture "
         "topic list for the following populations. " +
         lst(["infant", "child", "adolescent", "adult", "elderly"])],
    body="""
  <h3 class="sub" id="di-scabies">5.1 &middot; Objective a &mdash; Scabies and lice</h3>
  <p><strong>Scabies</strong> is caused by <em>Sarcoptes scabiei</em> variety hominis, transmitted by
  close physical contact for 15 to 20 minutes or through bedding and underclothing. The pathognomonic
  lesion is a <strong>thin thread-like linear or J-shaped burrow, 1 to 10 mm long</strong>, best seen in
  the interdigital webs and wrists.</p>
  <table>
    <tr><th></th><th>First infestation</th><th>Reinfestation</th></tr>
    <tr><td>Pruritus appears</td><td>4 to 6 weeks &mdash; many not for 3 months</td><td>2 to 3 days</td></tr>
  </table>
  <p>Distribution favours interdigital webs, sides of fingers, volar wrists, elbows, axillae, scrotum,
  penis, labia and areolae, with <strong>head and neck spared in healthy adults</strong>. In
  <strong>infants, the elderly and the immunocompromised</strong>, head and neck may be involved, and
  infants also get indurated crusted nodules on the trunk and intertriginous areas.</p>
  <div class="callout"><strong>Crusted (hyperkeratotic) scabies is the outbreak risk.</strong> Thick
  flaking scale containing millions of mites, thickened discoloured nails, and often <em>no itch at
  all</em>. These patients are highly infectious. Facility-associated scabies in long-term care is hard
  to eradicate once healthcare workers are infested.</div>
  <p><strong>Diagnosis</strong> is by microscopic identification of the organism, ova or faeces: skin
  scraping of an unexcoriated burrow with a number 15 blade and mineral oil, dermoscopy showing the
  <strong>delta-wing jet</strong> sign, or the burrow ink test (a zigzag line running away from the
  lesion).</p>
  <p><strong>Treatment</strong> is topical permethrin overnight to the <em>entire</em> skin surface with
  attention to creases, and <strong>a second application one week later</strong>. Wash bedding and
  clothing at 60&nbsp;degrees Celsius or bag it for 14 days, and treat all infested contacts. Ivermectin
  every two weeks for two to three doses is added for hyperkeratotic or immunosuppressed cases. Rash and
  itch may last four weeks after cure. Complications: staphylococcal superinfection, persistent
  post-scabietic papules, and psychological effects.</p>
  <table>
    <tr><th></th><th>Head lice</th><th>Body lice</th><th>Pubic lice</th></tr>
    <tr><td>Organism</td><td>Pediculus humanus capitis</td><td>Pediculus humanus humanus</td><td>Phthirus pubis</td></tr>
    <tr><td>Who</td><td>Children 3 to 12</td><td>Homeless, refugees, crowded conditions</td><td>All social levels; often a concurrent sexually transmitted infection</td></tr>
    <tr><td>Signs</td><td>Nits fixed to the hair shaft; excoriations, scaling</td><td>Linear excoriations on back, neck, shoulders, waist</td><td>Maculae caerulae &mdash; slate-grey macules about 1 cm; periumbilical papular urticaria</td></tr>
    <tr><td>Diagnosis</td><td>Wet combing for live lice</td><td>Examine clothing seams; shake over white paper</td><td>Nits at the base of hairs; microscopy of a plucked hair</td></tr>
  </table>
  <p><strong>Nits cannot be pulled off the hair shaft</strong> &mdash; that is what separates them from
  dandruff. A <strong>no-nit school policy is not recommended</strong> by the American Academy of
  Pediatrics, because nits persist for months after cure and exclusion costs school days.
  Fumigation is not recommended; bag or dry clothing and bedding and vacuum.</p>

  <h3 class="sub" id="di-bites">5.2 &middot; Objective a &mdash; Bedbugs, fleas, stings and caterpillars</h3>
  <table>
    <tr><th>Exposure</th><th>Presentation</th><th>Management</th></tr>
    <tr><td>Bedbugs (Cimex)</td><td>Painless bites in a linear row of three &mdash; &ldquo;breakfast, lunch and dinner&rdquo;; blood flecks on linen</td><td>Symptomatic; a <strong>professional exterminator is necessary</strong>. They survive a year without a meal</td></tr>
    <tr><td>Tungiasis (Tungidae)</td><td>Papules enlarging to a firm yellow translucent nodule on the feet, after barefoot beach exposure in endemic areas</td><td>Dermoscopy shows ovoid eggs; excision or cryotherapy, tetanus prophylaxis, systemic antibiotics</td></tr>
    <tr><td>Fleas (Pulicidae)</td><td>Clustered urticarial papules on the lower legs</td><td>Symptomatic. Rat fleas carry bubonic plague; cat fleas carry plague and endemic typhus</td></tr>
    <tr><td>Hymenoptera</td><td>Burning and local urticaria; severe local reaction lasts a week; systemic reaction in 0.4 to 3%</td><td><strong>Scrape</strong> a honeybee stinger off with a card edge. Epinephrine for anaphylaxis; auto-injector and desensitisation afterwards</td></tr>
    <tr><td>Caterpillars</td><td>Gypsy moth &rarr; papules in linear streaks. Asp or puss caterpillar (most poisonous) &rarr; intense pain, train-track purpura</td><td>Strip the hairs off with adhesive tape; antihistamines, steroids, narcotic analgesia, antivenom for some</td></tr>
  </table>

  <h3 class="sub" id="di-larva">5.3 &middot; Objective a &mdash; Cutaneous larva migrans and cercarial dermatitis</h3>
  <table>
    <tr><th></th><th>Cutaneous larva migrans</th><th>Cercarial dermatitis</th></tr>
    <tr><td>Organism</td><td>Animal hookworm larvae, mostly dog and cat</td><td>Cercarial form of parasitic flatworms, via snails</td></tr>
    <tr><td>Exposure</td><td>Sand or soil with animal faeces, tropical and subtropical</td><td>Fresh water &mdash; Great Lakes, rice paddies</td></tr>
    <tr><td>Lesion</td><td>Raised serpentine trail advancing <strong>2 to 3 cm a day</strong>, lasting 2 to 8 weeks</td><td>Prickling 30 minutes, itch at 10 to 12 hours, papules by 24 hours, peak at 48 to 72 hours</td></tr>
    <tr><td>Treatment</td><td>Albendazole 400 mg daily for 3 days, or ivermectin. <strong>No excision, no cryotherapy</strong></td><td>Symptomatic &mdash; antihistamines, oatmeal baths, aspirin, glucocorticoids</td></tr>
  </table>

  <h3 class="sub" id="di-spiders">5.4 &middot; Objective a &mdash; Spider bites</h3>
  <table>
    <tr><th></th><th>Black widow</th><th>Brown recluse</th><th>Hobo</th></tr>
    <tr><td>Identification</td><td>Red hourglass under the abdomen</td><td>Dark fiddle on the cephalothorax</td><td>Grey herringbone on the abdomen</td></tr>
    <tr><td>Range</td><td>All but the far north</td><td>Midwest and Southeast</td><td>Pacific Northwest</td></tr>
    <tr><td>Bite</td><td>Painful; sweating and piloerection within 30 minutes, then cramping abdominal pain and spasm</td><td>Red, white and blue sign; necrosis at 2 to 3 days, eschar at 5 to 7</td><td>Painless; induration and paraesthesia within 30 minutes, vesicles by 36 hours</td></tr>
    <tr><td>Venom</td><td>Alpha-latrotoxin, a neurotoxin</td><td>Local cytotoxic effect</td><td>Local, with systemic symptoms</td></tr>
    <tr><td>Treatment</td><td>Calcium gluconate, narcotics, muscle relaxants, benzodiazepines; check tetanus</td><td>Pain control, warm compresses; <strong>delay surgery until the wound is stable</strong></td><td>Supportive; heals over weeks, headache up to a week</td></tr>
  </table>
  <p><strong>Tarantulas</strong> shed urticating hairs that embed in skin and eyes &mdash; topical
  corticosteroid for the skin, ophthalmology for the eye.</p>

  <h3 class="sub" id="di-ticks">5.5 &middot; Objective a &mdash; Tick-borne illness</h3>
  <table>
    <tr><th></th><th>Lyme disease</th><th>Rocky Mountain spotted fever</th></tr>
    <tr><td>Organism</td><td>Borrelia burgdorferi, a spirochete</td><td>Rickettsia rickettsii</td></tr>
    <tr><td>Geography</td><td>Northeast and upper Midwest</td><td>Southeastern and south central states, spring and early summer</td></tr>
    <tr><td>Rash</td><td>Erythema migrans &mdash; over 5 cm, central clearing, about a week after the bite</td><td>Starts ankles and wrists, spreads <strong>centripetally</strong> over 6 to 18 hours, involves palms and soles, spares the face</td></tr>
    <tr><td>Diagnosis</td><td>Clinical if erythema migrans present. Otherwise enzyme-linked immunosorbent assay, C6 peptide, Western blot</td><td>Indirect immunofluorescence assay is the gold standard but rarely diagnostic before day 7</td></tr>
    <tr><td>Treatment</td><td>Doxycycline first line; <strong>amoxicillin</strong> in children and pregnancy; macrolide second line; 10 to 14 days</td><td><strong>Doxycycline for everyone</strong>, including pregnancy and children, with desensitisation where contraindicated; 5 to 10 days</td></tr>
  </table>
  <div class="pearl"><strong>The two tick illnesses diverge on the paediatric antibiotic.</strong> Lyme
  disease in a child gets amoxicillin. Rocky Mountain spotted fever in a child gets doxycycline anyway,
  because the risk of untreated disease outweighs tooth staining. <strong>Start by day 5</strong> &mdash;
  before the serology can help.</div>
  <p>Lyme stages: <strong>1</strong> early localised (erythema migrans, about a week);
  <strong>2</strong> early disseminated (days to weeks &mdash; cranial nerve palsies, meningitis,
  radiculopathy, arthralgia); <strong>3</strong> late persistent (months to years &mdash; monoarticular
  arthritis of a weight-bearing joint, subacute encephalopathy, acrodermatitis chronica atrophicans).
  Intravenous ceftriaxone, cefotaxime or penicillin G for arthritis and acrodermatitis. There is
  <strong>no human vaccine</strong>; there is one for dogs. Repellents: DEET, PMD, picaridin, reapplied
  about every two hours, plus pyrethrins on clothing. <strong>Prophylactic antibiotics after a tick bite
  are not recommended</strong> for Rocky Mountain spotted fever.</p>

  <h3 class="sub" id="di-lesions">5.6 &middot; Objectives b &amp; c &mdash; Primary versus secondary lesions, and care across the age range</h3>
  <p><strong>Primary lesions</strong> affect the epidermis and superficial dermis; <strong>secondary
  lesions</strong> infiltrate the dermis or subcutaneous tissue. Their combination determines the
  diagnostic category, also called the <em>reaction pattern</em>. Crusting or scaling tells you the
  epidermis has been affected. Once the reaction pattern is recognised, colour, shape, configuration
  and distribution narrow the differential further.</p>
  <table>
    <tr><th>Population</th><th>What changes</th></tr>
    <tr><td>Infant</td><td>Scabies involves head and neck and produces trunk nodules; permethrin remains the treatment</td></tr>
    <tr><td>Child</td><td>Head lice peak between 3 and 12 years; Lyme disease gets amoxicillin; the no-nit policy is not recommended</td></tr>
    <tr><td>Adolescent</td><td>Outdoor and water exposure drives hot tub folliculitis, cercarial dermatitis and tick bites</td></tr>
    <tr><td>Adult</td><td>Travel history opens tungiasis and cutaneous larva migrans; occupation opens body lice and cercarial dermatitis</td></tr>
    <tr><td>Elderly</td><td>Crusted scabies in long-term care; higher complication risk from black widow envenomation</td></tr>
  </table>
"""))

# ---------------------------------------------------------------- Lecture 8
SECTIONS.append(dict(
    num=6, sid="pigmented-lesions", title="Pigmented Skin Lesions",
    toc=[("psl-flat", "6.1 Objective a &mdash; Ephelides, lentigines and solar lentigo"),
         ("psl-keratoses", "6.2 Objective a &mdash; Seborrheic keratosis and dermatosis papulosa nigrans"),
         ("psl-vitiligo", "6.3 Objective a &mdash; Vitiligo"),
         ("psl-naevi", "6.4 Objective a &mdash; The melanocytic naevi"),
         ("psl-age", "6.5 Objective b &mdash; Care strategies in adults and the elderly")],
    ios=[IO_MAIN % "pigmented skin lesions" + " " +
         lst(["Ephelides", "Lentigines", "Seborrheic keratoses", "Dermatosis papulosis nigrans",
              "Nevi", "Vitiligo"]),
         "Identify medical care strategies for pigmented skin lesions in the lecture topic list for "
         "the following populations. " + lst(["adult", "elderly"])],
    body="""
  <div class="callout"><strong>This lecture is Lecture 8 in the syllabus order.</strong> Cutaneous
  Viral and Fungal Infections, Benign Skin Lesions, and Pre-Malignant and Malignant Cutaneous Lesions
  sit between it and Dermatological Infestations, and their sections will be added when those decks are
  posted.</div>

  <h3 class="sub" id="psl-flat">6.1 &middot; Objective a &mdash; Ephelides, lentigines and solar lentigo</h3>
  <table>
    <tr><th></th><th>Ephelides (freckles)</th><th>Lentigo simplex</th><th>Solar lentigo</th></tr>
    <tr><td>Inheritance or cause</td><td>Autosomal dominant; MCR-1 variant</td><td>Increased melanocyte density; melanin macroglobules</td><td>Chronic ultraviolet exposure; basal melanocyte proliferation</td></tr>
    <tr><td>Age</td><td>Young children, regress later in life</td><td>Bimodal &mdash; early childhood or later life</td><td>90% of people by age 50</td></tr>
    <tr><td>Appearance</td><td>Light brown symmetric macules 3 to 5 mm</td><td>Uniformly black or brown, well circumscribed, under 5 mm</td><td>Irregular borders, coalescing at sunburn sites, under 1 mm to several centimetres</td></tr>
    <tr><td>Sun behaviour</td><td><strong>Fade when exposure stops</strong>; darker in summer</td><td><strong>Do not fade</strong>; occur on protected skin too</td><td>Do not fade; associated with actinic keratosis and skin cancers</td></tr>
    <tr><td>Treatment</td><td>Sun protection, depigmenting agents, laser. <strong>Not cryotherapy</strong> &mdash; lesions too small</td><td>None needed; cryotherapy or quality-switched laser for cosmesis</td><td>None needed; retinoids, cryotherapy or laser for cosmesis</td></tr>
  </table>
  <div class="pearl"><strong>The whole ephelides-versus-lentigines question is one clinical fact:
  freckles fade when the sun goes, age spots do not.</strong> Everything else follows.</div>
  <p><strong>MCR-1</strong> is the receptor for alpha-melanocyte-stimulating hormone, activating
  melanogenesis through cyclic adenosine monophosphate. Reduced pathway activity promotes
  <strong>pheomelanin</strong>, the yellow-red sulfur-containing pigment &mdash; which is why the
  freckling phenotype travels with red hair and fair skin.</p>
  <p><strong>Photochemotherapy (PUVA) lentigines</strong> relate to the total number of treatments, male
  sex, fair skin and older age, and appear on <em>sun-protected</em> sites such as buttocks and
  genitalia as well as exposed skin. A partial or generalised lentigo raises the question of an
  inherited disorder such as LAMB or myxoma syndrome.</p>

  <h3 class="sub" id="psl-keratoses">6.2 &middot; Objective a &mdash; Seborrheic keratosis and dermatosis papulosa nigrans</h3>
  <table>
    <tr><th></th><th>Seborrheic keratosis</th><th>Dermatosis papulosa nigrans</th></tr>
    <tr><td>Appearance</td><td>Beige to black papules and plaques 2 to 20 mm, velvety or warty, look <strong>stuck on</strong></td><td>Smooth firm black or dark brown papules 1 to 5 mm &mdash; <em>identical to small seborrheic keratoses</em></td></tr>
    <tr><td>Site and group</td><td>Older adults, anywhere</td><td>Face and neck; African Americans, dark-skinned Asians, Polynesians; females more than males</td></tr>
    <tr><td>Origin</td><td>Benign epidermal proliferation</td><td>Genetic; a developmental defect of the hair follicle</td></tr>
    <tr><td>Management</td><td>Supportive; cryotherapy if itchy or inflamed, though it recurs</td><td>Best left untreated; excision, curettage or laser. <strong>Avoid cryotherapy</strong> &mdash; post-inflammatory hyperpigmentation</td></tr>
  </table>
  <p>Seborrheic keratoses are <strong>easily mistaken for neoplasms</strong>, which is exactly why they
  matter in an older adult presenting with a new dark growth.</p>

  <h3 class="sub" id="psl-vitiligo">6.3 &middot; Objective a &mdash; Vitiligo</h3>
  <p>An autoimmune disease causing depigmentation through <strong>T-cell mediated destruction of
  melanocytes</strong>. It can begin at any age but usually starts before the thirties &mdash; half
  before twenty, a third before twelve. Males and females are equally affected. Lesions are
  asymptomatic white non-scaly macules and patches with distinct margins that <strong>fluoresce under a
  Wood's lamp</strong> in a dark room.</p>
  <table>
    <tr><th></th><th>Non-segmental</th><th>Segmental</th></tr>
    <tr><td>Distribution</td><td>Well defined, <strong>symmetrical</strong>; prefers face (periorificial), genitals, acral areas</td><td><strong>Unilateral</strong>, does not cross the midline, block-like patterns</td></tr>
    <tr><td>Course</td><td>Progressive</td><td>Unpredictable cycles of flare and stabilisation</td></tr>
  </table>
  <table>
    <tr><th>Extent</th><th>Treatment</th></tr>
    <tr><td>Under 5% body surface</td><td>Topical steroid (cheap, effective; watch skin atrophy and intraocular pressure) <em>or</em> topical calcineurin inhibitor &mdash; tacrolimus, pimecrolimus &mdash; for face, neck, intertriginous areas and children (increased cancer risk), combined with phototherapy</td></tr>
    <tr><td>Over 5% body surface</td><td>Phototherapy first line: <strong>narrow band ultraviolet B</strong>, preferred over PUVA because PUVA raises skin cancer risk. Combination with topical therapy is ideal</td></tr>
    <tr><td>Highly stable disease only</td><td>Surgical tissue or cellular grafting</td></tr>
  </table>
  <div class="callout"><strong>Do not call it cosmetic.</strong> The lecture is explicit that vitiligo
  affects patients psychologically and socially through low self-esteem and poor body image, and that
  psychological intervention is part of management &mdash; not an optional extra.</div>
  <p>Investigations: Wood's lamp in a dark room, and a complete blood count and antinuclear antibody for
  the other autoimmune diseases associated with it.</p>

  <h3 class="sub" id="psl-naevi">6.4 &middot; Objective a &mdash; The melanocytic naevi</h3>
  <p>Melanocytic naevi divide by cell of origin: <strong>acquired</strong> naevi from junctional
  melanocytes, <strong>congenital</strong> naevi from neural-crest derived precursors migrating along
  neurovascular bundles. <strong>Dysplastic</strong> naevi are the group showing atypical architectural
  and cytologic features.</p>
  <table>
    <tr><th>Naevus</th><th>Appearance and who</th><th>What matters</th></tr>
    <tr><td>Congenital melanocytic</td><td>Flat brown patch or plaque at birth, sometimes pebbly or verrucous; trunk and extremities</td><td><strong>The larger the lesion the higher the melanoma risk.</strong> Head, neck or posterior midline &rarr; magnetic resonance imaging for <strong>neurocutaneous melanosis</strong></td></tr>
    <tr><td>Naevus spilus</td><td>Tan café-au-lait-like patch with scattered darker macules; trunk and extremities</td><td>Rarely progresses to melanoma. Observation and sun protection. Vascular, central nervous system and connective tissue anomalies can accompany it</td></tr>
    <tr><td>Common acquired (mole)</td><td>Under 6 mm, homogenous, round to oval, sharply demarcated; peaks in the thirties then declines</td><td><strong>Very dark brown or black on light skin is suspicious.</strong> Melanoma risk rises with the number</td></tr>
    <tr><td>Blue</td><td>Deeply pigmented dermal spindle or epithelioid melanocytes; women more than men, twenties; dorsal hands and feet, scalp, buttocks, sacrum</td><td>Common blue under 1 cm from adolescence; cellular blue over 1 cm before forty. Small lesions clinical, larger by biopsy</td></tr>
    <tr><td>Pigmented spindle cell (Reed)</td><td>Jet-black sharply circumscribed papule under 7 mm; thirties, females, thigh</td><td>Benign, but confirm by biopsy and <strong>excise with negative margins</strong></td></tr>
    <tr><td>Spitz</td><td>Solitary pink or red hairless firm dome-shaped lesion; growth phase then stable; spares palms, soles, mucosae</td><td><strong>Sometimes resembles melanoma</strong> &mdash; biopsy or wide excision. Multiple lesions can indicate a familial cancer syndrome</td></tr>
    <tr><td>Dysplastic</td><td>At least 5 mm, irregular indistinct borders, variable tan to brown, smooth or pebbly; sun-exposed skin</td><td>Commonest in Caucasians with a family history. Over 100 by adolescence defines the syndrome. <strong>May progress to melanoma</strong></td></tr>
  </table>
  <div class="pearl"><strong>Three naevi in this lecture get a knife rather than a follow-up
  appointment:</strong> pigmented spindle cell (excise with negative margins), Spitz (biopsy or wide
  excision, then excise) and any dysplastic naevus that is changing. The rest are observed.</div>

  <h3 class="sub" id="psl-age">6.5 &middot; Objective b &mdash; Care strategies in adults and the elderly</h3>
  <table>
    <tr><th>Population</th><th>What changes</th></tr>
    <tr><td>Adult</td><td>Naevus counts peak in the thirties, so this is when dysplastic naevus syndrome declares itself. Vitiligo usually begins before thirty and needs psychological support alongside therapy. Solar lentigines begin appearing and mark cumulative sun damage</td></tr>
    <tr><td>Elderly</td><td>Seborrheic keratoses are common and are easily mistaken for neoplasms &mdash; the clinical diagnosis is what avoids unnecessary biopsy. Solar lentigines are near-universal by 70 in fair skin, and sit alongside actinic keratosis and skin cancers. Naevus counts fall, so a <em>new</em> pigmented lesion in an older patient deserves more suspicion, not less</td></tr>
  </table>
  <p>Across both groups the same three things carry: daily broad-spectrum sun protection, annual
  full-body skin examination, and biopsy of anything that is changing.</p>
"""))


def build_section(sec):
    return ('\n<!-- ============ %d %s ============ -->\n'
            '<section class="deck" id="%s">\n'
            '  <h2 class="deck-title">%d &middot; %s</h2>\n'
            '%s%s'
            '</section>\n' % (sec["num"], sec["title"].upper(), sec["sid"], sec["num"],
                              sec["title"], io_box(sec["ios"]), sec["body"]))


def main():
    s = open(GUIDE, encoding="utf-8").read()
    assert "general-derm-1" not in s, "sections already added"

    # 1. header line
    old_hdr = ("<p>Covers Lecture 1, Clinical Reasoning and Problem Solving &middot; further sections "
               "are added as each Exam 1 lecture is posted &middot; Instructional Objectives (IOs) "
               "taken verbatim from the syllabus</p>")
    assert old_hdr in s, "header line not found"
    new_hdr = ("<p>Covers Lectures 1&ndash;5 and 8 &middot; further sections are added as each Exam 1 "
               "lecture is posted &middot; Instructional Objectives (IOs) taken verbatim from the "
               "syllabus</p>")
    s = s.replace(old_hdr, new_hdr)

    # 2. table of contents
    old_toc = ('  <a class="top-link" href="#how-course-works" style="color:#8a6508">2 &middot; '
               'How this course is built</a>\n')
    assert old_toc in s, "toc anchor not found"
    toc = ""
    for sec in SECTIONS:
        toc += '  <a class="top-link" href="#%s">%d &middot; %s</a>\n' % (sec["sid"], sec["num"], sec["title"])
        for aid, label in sec["toc"]:
            toc += '  <a href="#%s">%s</a>\n' % (aid, label)
    toc += ('  <a class="top-link" href="#how-course-works" style="color:#8a6508">7 &middot; '
            'How this course is built</a>\n')
    s = s.replace(old_toc, toc)

    # 3. the sections themselves, before the "how the course works" block
    marker = '<!-- ============ 2 HOW THE COURSE WORKS ============ -->'
    assert marker in s, "insert marker not found"
    s = s.replace(marker, "".join(build_section(sec) for sec in SECTIONS) + "\n" +
                  marker.replace("2 HOW", "7 HOW"))
    s = s.replace('<h2 class="deck-title">2 &middot; How this course is built</h2>',
                  '<h2 class="deck-title">7 &middot; How this course is built</h2>')

    # 4. the "why lecture 1 has no disease in it" callout now has company
    s = s.replace("From General Dermatology I onward each topic has a named disease list, and the "
                  "guide sections for those follow",
                  "From General Dermatology I onward each topic has a named disease list, and sections "
                  "2 to 6 above follow")

    open(GUIDE, "w", encoding="utf-8").write(s)

    # structural checks -- a stray closing tag is invisible in a browser
    for tag in ("style", "script", "section", "table", "div"):
        o, c = s.count("<%s" % tag), s.count("</%s>" % tag)
        if tag == "div":
            o = len(re.findall(r"<div[ >]", s))
        assert o == c, "%s: %d open, %d close" % (tag, o, c)
    print("sections added: %s" % ", ".join(str(x["num"]) for x in SECTIONS))
    print("tag balance verified: style, script, section, table, div")


if __name__ == "__main__":
    main()
