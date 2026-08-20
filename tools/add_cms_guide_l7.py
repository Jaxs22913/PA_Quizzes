#!/usr/bin/env python3
"""Add the Lecture 7 (Benign Skin Lesions) section to the CMS I Exam 1 guide.

Lecture 7 sits BEFORE Lecture 8 in syllabus order, so it becomes section 6 and
everything after it shifts: Pigmented Skin Lesions 6 -> 7, and "How this course
is built" 7 -> 8. The renumber is done by explicit, asserted replacements rather
than a blind regex, because a sloppy pass here would silently renumber the
Lecture 2 subsections too.

Instructional Objectives are quoted VERBATIM from the PAJ 5500 syllabus, per the
guide verbatim-IO rule.

PHOTOGRAPH STRIPS. Per the standing rule that a visual subject gets pictures,
each subsection carries a `.figgrid` strip built the same way as the dermatology
sections already in this guide -- reusing the comparison chart's audited images
in place, so no new bytes and no chance of the two disagreeing. The chart images
for this lecture were audited at full size before being assigned, which caught a
photograph of corn on the cob, a photograph of a volcano and a photograph of a
doughnut sitting on slides with entirely ordinary titles.

Idempotent: fenced in <!--CMSL7--> and stripped before re-inserting.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
GUIDE = os.path.join(DIR, "cms-exam-1-study-guide.html")
OPEN, CLOSE = "<!--CMSL7-->", "<!--/CMSL7-->"
TOC_OPEN, TOC_CLOSE = "<!--CMSL7TOC-->", "<!--/CMSL7TOC-->"

IO_MAIN = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical "
           "manifestations, differential diagnosis, diagnostic testing (including ordering and "
           "interpretation), management (including applicable rehabilitative and palliative care), "
           "appropriate referrals, patient education, and prognosis for the following benign skin "
           "lesions:")

LESIONS = ["Clavus and callous", "Scars (hypertrophic, keloid)", "Cutaneous horn",
           "Skin tags (acrochordon, polyps)", "Pressure injury", "Pilonidal cyst",
           "Dermatofibroma", "Keratoacanthoma", "Epidermal cyst", "Syringoma",
           "Vascular lesions (nevi, hemangiomata, telangiectasia)", "Pyogenic granuloma",
           "Neurofibroma", "Xanthelasma", "Lipoma", "Mucous cyst", "Sebaceous hyperplasias"]

# Which chart conditions illustrate which subsection, in teaching order.
PLACEMENT = [
 ("bsl-mechanical", ["Clavus (corn) &mdash; hard", "Clavus (corn) &mdash; soft", "Callus"]),
 ("bsl-scars", ["Keloid", "Hypertrophic scar"]),
 ("bsl-keratotic", ["Cutaneous horn", "Acrochordon (skin tag)"]),
 ("bsl-pressure", ["Pressure injury (pressure ulcer)", "Pilonidal cyst"]),
 ("bsl-nodules", ["Dermatofibroma", "Keratoacanthoma", "Epidermoid (epidermal) cyst", "Syringoma"]),
 ("bsl-vascular", ["Infantile hemangioma", "Nevus flammeus (port-wine stain)",
                   "Nevus simplex (stork bite)", "Cherry angioma", "Telangiectasia",
                   "Nevus araneus (spider angioma)", "Pyogenic granuloma"]),
 ("bsl-other", ["Neurofibromatosis type 1", "Xanthelasma", "Lipoma", "Digital mucous cyst",
                "Sebaceous hyperplasia"]),
]

LOOK = {
 "Clavus (corn) &mdash; hard": "Cored, well defined, tender straight down; skin lines run through",
 "Clavus (corn) &mdash; soft": "Same lesion macerated white in the toe web space",
 "Callus": "Diffuse, irregular, painless thickening over a broad pressure area",
 "Keloid": "Grows out past the original wound margin and keeps going",
 "Hypertrophic scar": "Raised and red but stops exactly at the wound edge",
 "Cutaneous horn": "Keratin projection; what matters is the lesion at its base",
 "Acrochordon (skin tag)": "Soft pedunculated papules on a narrow stalk, in a friction site",
 "Pressure injury (pressure ulcer)": "Stages 1 to 3, shown in lightly and darkly pigmented skin",
 "Pilonidal cyst": "Sinus opening in the natal cleft, sometimes with a hair in it",
 "Dermatofibroma": "Firm brown-haloed nodule; dimples when squeezed from the sides",
 "Keratoacanthoma": "Dome with a central keratin crater, grown in six to eight weeks",
 "Epidermoid (epidermal) cyst": "Movable nodule with a central punctum",
 "Syringoma": "Crops of one to two millimetre papules around the eyes",
 "Infantile hemangioma": "Bright red papule that proliferates then involutes",
 "Nevus flammeus (port-wine stain)": "Unilateral, sharp midline cutoff, never involutes",
 "Nevus simplex (stork bite)": "Pink blanchable patch on the nape; usually fades within a year",
 "Cherry angioma": "Small firm deep red papules on the trunk, more with age",
 "Telangiectasia": "Permanently dilated capillary under a millimetre, blanchable",
 "Nevus araneus (spider angioma)": "Central arteriole with radiating vessels; think estrogen or liver",
 "Pyogenic granuloma": "Moist bright red exophytic nodule that bleeds; grew fast after injury",
 "Neurofibromatosis type 1": "Cutaneous neurofibromas, appearing at puberty and multiplying",
 "Xanthelasma": "Soft yellow plaques on the medial eyelids; check the lipids",
 "Lipoma": "Soft rubbery painless subcutaneous mass, no overlying pore",
 "Digital mucous cyst": "Translucent papule over the distal joint; grooves the nail",
 "Sebaceous hyperplasia": "Whitish-yellow papule with a central dell; not a basal cell carcinoma",
}

ROW = re.compile(
    r'<tr><td class="pic">(?:<figure><img src="cms-derm-chart-images/([^"]+)"[^>]*>'
    r'<figcaption>(.*?)<span class="deck">.*?</span></figcaption></figure>'
    r'|<div class="nopic">.*?</div>)</td><td class="name">(.*?)</td>', re.S)


def chart_images():
    src = open(os.path.join(DIR, "cms-derm-comparison-chart.html"), encoding="utf-8").read()
    out = {}
    for img, cite, name in ROW.findall(src):
        name = " ".join(re.sub(r"<[^>]+>", " ", name).split())
        out[name] = (img, cite) if img else None
    return out


def strip(fence_open, fence_close, s):
    return re.sub(re.escape(fence_open) + r".*?" + re.escape(fence_close), "", s, flags=re.S)


def build_strip(names, imgs):
    figs = []
    for n in names:
        entry = imgs.get(n)
        assert entry is not None, "no chart image for %r" % n
        fn, cite = entry
        look = LOOK[n]
        figs.append(
            '<figure><img src="cms-derm-chart-images/%s" decoding="async" alt="%s">'
            '<figcaption><span class="fg-name">%s</span>%s<span class="fg-cite">%s</span>'
            '</figcaption></figure>'
            % (fn, re.sub(r"&\w+;", "-", n), n, look, cite))
    return ('%s\n  <p class="figgrid-h">What these look like</p>\n  <div class="figgrid">%s</div>\n  %s'
            % ("<!--L7FIG-->", "".join(figs), "<!--/L7FIG-->"))


BODY = '''<section class="deck" id="benign-skin-lesions">
  <h2 class="deck-title">6 &middot; Benign Skin Lesions</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Lecture 7 &mdash; Professor Hugh E. Griffenkranz, MPAS, PA-C</p>
    <ol type="a">
      <li>@@IO_MAIN@@
        <ol>@@LESIONS@@</ol>
      </li>
      <li>Identify medical strategies for common benign skin lesions in infants, adolescent, adult, and elderly</li>
    </ol>
  </div>

  <div class="callout"><b>Four of this deck&rsquo;s slides are pictures of tables, and their content
  is in no text version of the file.</b> Slides 33 and 34 carry the entire pressure injury staging
  system; slide 24 compares keloid against hypertrophic scar; slide 42 defines sinus against
  fistula; slide 9 lists the keratolytic products. All four are reproduced or transcribed below. If
  you are revising from a text export of the deck rather than the slides themselves, those are the
  four you will be missing.</div>

  <h3 class="sub" id="bsl-mechanical">6.1 &middot; Objective a &mdash; Corns, calluses, and the wart that mimics them</h3>
  <p>All three are keratin responses to mechanical stress, and the exam question is which one you
  are looking at. Two features settle it: <b>whether the skin lines run through the lesion</b>, and
  <b>which direction of pressure hurts</b>.</p>
  <table>
    <tr><th></th><th>Clavus (corn)</th><th>Callus</th><th>Verruca vulgaris (wart)</th></tr>
    <tr><td><b>Cause</b></td><td>Focal pressure, e.g. ill-fitting shoes</td><td>Broad-area pressure and friction</td><td>Human papillomavirus</td></tr>
    <tr><td><b>Structure</b></td><td>Cone-shaped <b>central core</b> of hard keratin pointing in</td><td>Diffuse thickening, <b>no core</b></td><td>Cauliflower surface, <b>blackened centre</b></td></tr>
    <tr><td><b>Size &amp; shape</b></td><td>Well defined, &lt;1.5&nbsp;cm</td><td>Larger, irregular, poorly defined</td><td>Variable</td></tr>
    <tr><td><b>Skin lines</b></td><td>Run <b>through</b></td><td>Run <b>through</b></td><td><b>Interrupted</b></td></tr>
    <tr><td><b>Pain</b></td><td>On <b>direct downward</b> pressure</td><td>Usually painless</td><td>May hurt on <b>side</b> pressure</td></tr>
    <tr><td><b>Pressure areas?</b></td><td>Yes</td><td>Yes</td><td><b>Not specific to them</b></td></tr>
  </table>
  <p><b>Hard corn</b> (clavus durum) favours the dorsal and lateral fifth toe. <b>Soft corn</b>
  (clavus mollum) sits in the fourth-to-fifth web space and is soft because moisture between the
  toes macerates it. A callus that forms acutely and severely produces a <b>blister</b> instead.</p>
  <div class="pearl"><b>Management is the same idea for both: take the pressure off, then thin the
  keratin.</b> Padding and better footwear first, then over-the-counter keratolytics. The deck's
  product table is an image, and it collapses to one fact &mdash; <b>every single product is
  salicylic acid</b>, between 12.6% and 40%, as a disk, a liquid or a plaster. The brand names carry
  no information. <b>And the diabetic patient goes to podiatry.</b></div>

  <h3 class="sub" id="bsl-scars">6.2 &middot; Objective a &mdash; Abnormal wound healing: keloid and hypertrophic scar</h3>
  <p>Normal healing runs <b>hemostasis &rarr; inflammation &rarr; proliferation &rarr;
  remodeling</b>, and the maturing scar gains tensile strength through <b>progressive cross-linking
  of collagen fibers</b>. Abnormal healing is the loss of the control mechanisms that regulate that
  balance. Two things go wrong, and telling them apart is the highest-yield contrast in this
  lecture.</p>
  <table>
    <tr><th></th><th>Hypertrophic scar</th><th>Keloid</th></tr>
    <tr><td><b>Timing</b></td><td>Develops <b>within four weeks</b>, soon after surgery</td><td>Develops <b>slowly</b>, may appear <b>months</b> after the trauma</td></tr>
    <tr><td><b>Course</b></td><td>Stable, then <b>regresses and flattens</b></td><td><b>Enlarges for months to years</b>, rarely improves, tends to recur</td></tr>
    <tr><td><b>Margins</b></td><td><b>Confined to the wound</b></td><td><b>Extends beyond the wound</b></td></tr>
    <tr><td><b>Where</b></td><td>Where scars cross <b>joints or skin creases at a right angle</b></td><td><b>Ear lobe, shoulders, sternal notch</b>; rarely across joints</td></tr>
    <tr><td><b>Surgery</b></td><td><b>Improves</b> with appropriate surgery</td><td>Often <b>worsened</b> by surgery</td></tr>
    <tr><td><b>Incidence</b></td><td>Frequent</td><td>Rare</td></tr>
    <tr><td><b>Skin colour</b></td><td><b>No association</b></td><td><b>Associated with dark skin colour</b></td></tr>
  </table>
  <p class="tag">The last four rows come from slide 24, which is an image of a table and appears
  nowhere in the deck&rsquo;s text.</p>
  <div class="pearl"><b>The most important keloid treatment is prevention.</b> No single modality
  is best for all keloids and combination therapy has the best success rates &mdash; but the thing
  that actually works is not creating one. Advise high-risk patients to avoid cosmetic procedures
  such as ear piercing, and treat adolescent acne early, because that greatly increases the chance
  of scar-free healing.</div>
  <table>
    <tr><th>Keloid treatment</th><th>Detail worth remembering</th></tr>
    <tr><td>Silicone gel sheets</td><td>12&ndash;24&nbsp;h/day for up to a year; theory is raised scar temperature increasing collagenase activity</td></tr>
    <tr><td>Compression</td><td><b>25&nbsp;mmHg, 24&nbsp;h/day, 6&ndash;12 months</b>; possibly tissue hypoxia and fibroblast degeneration</td></tr>
    <tr><td>Intralesional steroid</td><td>Reduces collagen production, eventually flattens; may cause <b>tissue atrophy</b></td></tr>
    <tr><td>Surgical removal</td><td><b>50&ndash;100% recurrence, often larger</b> &mdash; always follow with intralesional steroid</td></tr>
    <tr><td>Radiation</td><td>Only in the <b>first two weeks after excision</b></td></tr>
    <tr><td>Cryotherapy</td><td>Flattens; causes <b>hypopigmentation</b></td></tr>
    <tr><td>Laser</td><td>Shrinks collagen or induces microvascular thrombosis; <b>best combined with intralesional steroid</b></td></tr>
    <tr><td>Intralesional fluorouracil</td><td>Antimetabolite; <b>inhibits fibroblast proliferation</b></td></tr>
  </table>
  <p>Both are diagnosed <b>clinically</b>, and for both, <b>biopsy only if there is genuine doubt,
  because it may induce new scarring</b>. Differential for each: the other one, dermatofibroma, and
  foreign-body granuloma.</p>

  <h3 class="sub" id="bsl-keratotic">6.3 &middot; Objective a &mdash; Cutaneous horn and skin tags</h3>
  <p><b>A cutaneous horn is not a diagnosis.</b> It is a hard conical keratin projection that
  <b>arises from the surface of another lesion</b> &mdash; actinic keratosis, wart, seborrheic
  keratosis, keratoacanthoma, or basal or squamous cell carcinoma. <b>The process at the base is
  what matters</b>, and <b>often no clinical feature distinguishes benign from malignant</b>. So the
  answer to &ldquo;what do you do with a cutaneous horn&rdquo; is always <b>deep shave biopsy to
  sample the underlying tissue</b>, and management follows whatever that shows.</p>
  <p>Epidemiology: Caucasians <b>over 50</b>, males equal to females, on head, neck and upper
  extremities &mdash; commonly the sun-exposed face, ears and hands.</p>
  <p><b>Acrochordon</b> is a <b>fibroepithelial pedunculated papilloma</b>: a narrow stalk with a
  broad tip, 1&nbsp;mm to 10&nbsp;mm, soft and skin-coloured. Increased in <b>females and obese
  patients</b>, in <b>friction sites</b> &mdash; neck, axilla, groin. Present in <b>60% of people by
  age 70</b>. Treatment is for cosmesis: scissor excision, cryotherapy or electrodesiccation, and
  <b>anesthesia is not necessary</b>.</p>
  <div class="pearl"><b>The skin tag counselling point patients actually need:</b> never cut or
  pull one off at home, because they bleed. And a new tag often forms in the same area after one is
  removed, so removal is not prevention.</div>

  <h3 class="sub" id="bsl-pressure">6.4 &middot; Objective a &mdash; Pressure injury and pilonidal disease</h3>
  <p>A pressure injury is <b>unrelieved pressure damaging underlying tissue</b>, generally soft
  tissue compressed <b>between a bony prominence and an external surface</b> for a prolonged time.
  The staging system below is transcribed from slides 33 and 34, which are images.</p>
  <table>
    <tr><th>Stage</th><th>Definition</th></tr>
    <tr><td><b>1</b></td><td>Localised area of <b>non-blanchable erythema of intact skin</b></td></tr>
    <tr><td><b>2</b></td><td><b>Partial-thickness</b> skin loss with <b>exposed dermis</b>; wound bed viable, pink or red, may be moist, shiny or dry</td></tr>
    <tr><td><b>3</b></td><td><b>Full thickness</b> skin loss; <b>adipose tissue is visible</b></td></tr>
    <tr><td><b>4</b></td><td>Full thickness skin <b>and tissue</b> loss; <b>exposed fascia, muscle, tendon, ligament, cartilage or bone</b></td></tr>
    <tr><td><b>Unstageable</b></td><td>Obscured full thickness loss; extent <b>cannot be determined because of slough or eschar</b></td></tr>
    <tr><td><b>Deep tissue</b></td><td>Persistent <b>non-blanchable deep red or purple discolouration</b>; skin can be intact or non-intact</td></tr>
  </table>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Worth noticing about the staging tables</span>
  <p>Both slides illustrate <mark class="prof-highlight">every stage in lightly pigmented AND darkly
  pigmented skin</mark>. That is not decoration. Stage 1 is defined by non-blanchable erythema, and
  erythema is exactly the finding that is hardest to see and easiest to miss on darker skin &mdash;
  which is the same point Professor Jaquith made about recognising dermatological disease across
  skin types.</p></div>
  <p><b>The best measure is prevention:</b> frequent skin assessment, nutrition assessment, moisture
  control and skin care (clean and dry, manage incontinence, barrier creams), <b>reposition every
  two hours</b>, manage pain, improve mobility, specialty mattresses. Management otherwise depends
  on stage: <b>refer to a wound care specialist</b>, control infection risk, silicone and
  hydrocolloid dressings, and surgical referral for <b>debridement</b> &mdash; which removes
  necrotic tissue, eschar and slough because they <b>promote infection, delay granulation and
  impede healing</b> &mdash; and for wound closure.</p>
  <p><b>Pilonidal disease</b> starts when disruption of the skin over the coccyx leaves a <b>pit</b>
  that draws in hair and debris, causing follicular plugging; ingrown hairs prevent drainage and
  promote abscess. <b>Male to female 3:1</b>; once thought congenital, now believed <b>acquired</b>;
  recurrence is common. Risk factors: obesity, local trauma or irritation, sedentary lifestyle,
  <b>increased hair density in the natal cleft</b>, family history.</p>
  <p><b>Acute abscess:</b> sudden pain and swelling in the gluteal cleft; warm, tender,
  erythematous, purulent or bloody drainage, possibly <b>fluctuant</b> &mdash; a wave-like fluid
  shift on palpation indicating the lesion is fluid filled. <b>Chronic:</b> recurrent drainage from
  one or more sinus tracts, sometimes with a hair protruding.</p>
  <div class="pearl"><b>Sinus versus fistula, from slide 42 &mdash; another image.</b> A <b>sinus is
  a blind track</b>. A <b>fistula connects two epithelium-lined surfaces</b>. Both usually arise
  from a preceding abscess. <b>No diagnostic testing is usually needed</b> for pilonidal disease:
  keep the area clean, consider hair removal, <b>incise and drain an acute abscess</b>, and refer
  chronic disease to a surgeon for excision.</div>

  <h3 class="sub" id="bsl-nodules">6.5 &middot; Objective a &mdash; The nodules that must be told from a cancer</h3>
  <p>These four sit opposite a malignancy in their differential, and that is what makes them
  examinable rather than trivia.</p>
  <table>
    <tr><th>Lesion</th><th>What it is</th><th>Key feature</th><th>Diagnosis &amp; management</th></tr>
    <tr><td><b>Dermatofibroma</b></td><td>Dermal fibroblasts in dense clusters; 0.5&ndash;1&nbsp;cm; legs then arms; F:M 2:1; may follow trauma, viral infection or insect bite</td><td><b>Dimple sign</b> &mdash; retracts beneath the skin on lateral compression. Brown halo, pink hue, raised scaly centre. <b>Most common painful skin tumour</b></td><td>Dermoscopy: <b>peripheral pigment network with central white mass</b>. Often no treatment; small lesions take a <b>shave or punch biopsy that is both diagnostic and therapeutic</b>. Differential includes <b>melanoma</b> and basal cell carcinoma</td></tr>
    <tr><td><b>Keratoacanthoma</b></td><td>From the pilosebaceous unit. <b>Argued to be a variant of invasive squamous cell carcinoma</b></td><td><b>Triphasic</b>: rapid growth in <b>6&ndash;8 weeks</b>, stabilization, regression after 3&ndash;6 months. Dome with a <b>central keratin-filled crater</b>. Risks: age &gt;40, sun, very fair skin, male, <b>red tattoo ink</b>, <b>skin trauma including lasers, surgery and cryotherapy</b>, human papillomavirus</td><td><b>Biopsy is the only reliable diagnosis.</b> <b>Excise or destroy</b> &mdash; standard of care because of possible malignancy. <b>5&nbsp;mm margins</b>; <b>Mohs</b> for large, recurrent or cosmetically sensitive lesions. Intralesional <b>methotrexate</b> before excision to shrink it</td></tr>
    <tr><td><b>Epidermoid cyst</b></td><td>Epithelium enclosed in the dermis filling with <b>KERATIN</b>. <b>Not a sebaceous cyst</b>, despite the name. M:F 2:1; face, scalp, neck, trunk</td><td>Firm, movable, round, with a <b>central pore or punctum</b>; expresses cream-coloured pasty material with the <b>odour of rancid cheese</b></td><td>Lab tests usually unnecessary. <b>If inflamed, POSTPONE excision</b>, settle it with intralesional triamcinolone, antibiotics if needed. <b>Standard of care: remove the entire capsule when it is not inflamed</b>; 1&ndash;3&nbsp;cm cysts can be punched and emptied</td></tr>
    <tr><td><b>Syringoma</b></td><td>Benign neoplasms of <b>eccrine ducts</b>. Appear at <b>puberty</b>; females &gt; males</td><td>Multiple <b>1&ndash;2&nbsp;mm</b> skin-coloured, pink or brown papules on the <b>eyelids and upper cheeks</b></td><td>Usually clinical; biopsy if malignancy is a concern. <b>Cosmesis only</b> &mdash; drugs (oral isotretinoin) risk <b>recurrence</b>, procedures risk <b>poor cosmetic results</b>. Differential: milia, xanthelasma, basal cell carcinoma</td></tr>
  </table>

  <h3 class="sub" id="bsl-vascular">6.6 &middot; Objective a &mdash; The vascular lesions</h3>
  <p>Sort them first by <b>congenital or acquired</b>, and within the congenital group by <b>whether
  the lesion involutes</b>. That single question separates the two the professor tested himself.</p>
  <table>
    <tr><th>Lesion</th><th>Congenital / acquired</th><th>Mechanism</th><th>Course</th></tr>
    <tr><td><b>Infantile hemangioma</b></td><td>Congenital</td><td><b>Proliferation of endothelial cells</b></td><td><b>Proliferates then INVOLUTES</b> &mdash; 50% by age 5, 70% by 7, 90% by 9</td></tr>
    <tr><td><b>Nevus flammeus</b></td><td>Congenital</td><td><b>Dilation</b> of dermal capillaries, <b>NO proliferation</b></td><td><b>Never involutes</b>; grows with the child, darkens and thickens</td></tr>
    <tr><td><b>Nevus simplex</b></td><td>Congenital</td><td>More superficial variant of nevus flammeus</td><td><b>Fades within a year</b>, or persists on the neck</td></tr>
    <tr><td><b>Cherry angioma</b></td><td>Acquired</td><td>Capillary/venule <b>proliferation</b></td><td>Increases with age; new ones keep coming</td></tr>
    <tr><td><b>Telangiectasia</b></td><td>Acquired</td><td>Permanently <b>dilated</b> capillary &lt;1&nbsp;mm</td><td>Primary or secondary; associated with numerous diseases</td></tr>
    <tr><td><b>Nevus araneus</b></td><td>Acquired</td><td><b>Dilation</b> of preexisting vessels, <b>no proliferation</b></td><td>Estrogen excess &mdash; resolves after delivery or stopping the pill; also cirrhosis</td></tr>
    <tr><td><b>Pyogenic granuloma</b></td><td>Acquired</td><td>Vascular overgrowth after <b>irritation, trauma or hormonal change</b></td><td>Grows fast, bleeds; may resolve over months to years</td></tr>
  </table>
  <div class="pearl"><b>The professor&rsquo;s own discussion question was hemangioma against nevus
  flammeus.</b> The answer is <em>present at birth; involution does not occur</em> &mdash; that is
  nevus flammeus. Hemangioma appears in the first days to weeks, proliferates hardest in the first
  4&ndash;6 months, and then goes away. Nevus flammeus is there from day one and never leaves.</div>
  <p><b>Infantile hemangioma</b> is the most common tumour of infancy: preterm, <b>female 3:1</b>,
  Caucasian; head and neck 60%, trunk 25%, extremities 15%. Earliest sign is <b>blanching, then fine
  telangiectasias, then a red or crimson macule</b>. <b>Superficial</b> is commonest (dermal vessels,
  bright red, once &ldquo;strawberry&rdquo;); <b>deep</b> is least common (deep dermis and subcutis,
  pale, skin-coloured, red or blue). Complications are <b>compression of vital structures</b> &mdash;
  vision, feeding, respiration, external auditory canal &mdash; plus extracutaneous lesions in liver,
  gastrointestinal tract, central nervous system and elsewhere.</p>
  <p><b>Treatment indications:</b> cosmetic, functional involvement, deep ulceration, infection.
  Otherwise serial observation. <b>First line is a beta-blocker</b> &mdash; oral propranolol or
  topical timolol, mechanism not well understood &mdash; <b>and corticosteroids</b>, topical,
  intralesional or oral. Pulsed dye laser reaches about <b>1.2&nbsp;mm</b>, so it is a superficial
  treatment. Refer to an <b>experienced vascular anomalies specialist</b> if the diagnosis is in
  question.</p>
  <p><b>Pyogenic granuloma is misnamed &mdash; neither infectious nor granulomatous.</b> Bright red
  exophytic papule with a <b>moist surface and an epithelial collarette</b>, average 6.5&nbsp;mm,
  common on head, neck and fingers, and common in pregnancy. Differential includes <b>melanoma and
  squamous cell carcinoma</b>. <b>Surgical excision has the lowest recurrence and the highest rate
  of scarring</b>, and provides histopathology.</p>

  <h3 class="sub" id="bsl-other">6.7 &middot; Objectives a &amp; b &mdash; Neurofibromatosis, and the remaining lesions</h3>
  <p><b>Neurofibromatosis</b>, also von Recklinghausen disease, is a common neurocutaneous genetic
  disorder. <b>NF1 &mdash; NF1 gene, chromosome 17. NF2 &mdash; NF2 gene, chromosome 22.
  Schwannomatosis (NF3) &mdash; SMARCB1 and LZTR1, chromosome 22.</b> The four NF1 skin
  manifestations:</p>
  <table>
    <tr><th>Sign</th><th>Detail</th></tr>
    <tr><td><b>Caf&eacute; au lait spots</b></td><td>Light tan to brown macules, <b>&gt;5&nbsp;mm prepubertal, &gt;15&nbsp;mm postpubertal</b>. Often the <b>first manifestation</b>; usually at birth or in the first year; grow in proportion with the child. <b>Six or more are diagnostic &mdash; but the macules alone do not establish the diagnosis</b></td></tr>
    <tr><td><b>Cutaneous neurofibromas</b></td><td>Benign nerve sheath tumours from peripheral nerves; sessile or pedunculated; <b>begin at puberty</b> and increase in number and size with age; a few to hundreds</td></tr>
    <tr><td><b>Plexiform neurofibromas</b></td><td>Tumour in the tissue covering nerves; anywhere <b>except brain and spinal cord</b>; large, extensive, and <b>may be locally invasive</b></td></tr>
    <tr><td><b>Intertriginous freckling (Crowe&rsquo;s sign)</b></td><td>Freckles <b>&lt;5&nbsp;mm</b>, <b>smaller</b> than caf&eacute; au lait spots, grouped, more prominent with sun. <b>Axillary and inguinal</b> &mdash; under the breasts is <em>not</em> a diagnostic site</td></tr>
  </table>
  <p>Management is <b>surveillance</b>: a cutaneous examination at every visit for new or progressing
  lesions. Education is to point patients at <b>national and regional support groups</b>.</p>
  <table>
    <tr><th>Lesion</th><th>What to know</th></tr>
    <tr><td><b>Xanthelasma</b></td><td>Soft yellow cholesterol plaques &mdash; <b>lipid-laden macrophages</b> &mdash; on the <b>medial eyelids</b>. <b>Screen for hyperlipidemia; may signify increased cardiac risk.</b> Laser or excision; <b>recurrence common</b></td></tr>
    <tr><td><b>Lipoma</b></td><td><b>The most common soft tissue tumour.</b> Benign overgrowth of subcutaneous fat; soft, painless, rubbery, usually &lt;5&nbsp;cm. Observe if asymptomatic; excise if deforming or the diagnosis is uncertain. Differential: epidermal cyst, dermatofibroma, abscess</td></tr>
    <tr><td><b>Digital mucous cyst</b></td><td>A <b>pseudo-cyst</b> &mdash; no cellular lining. Mucin extruded from a joint space compacts the dermal cells into something that only <b>mimics</b> a capsule. Females &gt; males, <b>associated with osteoarthritis</b>, over the <b>distal interphalangeal joint</b>; may groove the nail. Observe, or excise if symptomatic or causing nail dystrophy</td></tr>
    <tr><td><b>Sebaceous hyperplasia</b></td><td><b>Sebocyte turnover slows with age</b>, crowding cells and enlarging the gland. <b>No known potential for malignant transformation</b>; <b>immunosuppression is high risk</b>. Whitish-yellow soft papules 2&ndash;9&nbsp;mm with <b>central umbilication</b>, on the face. Differential is <b>basal cell carcinoma</b>, and <b>dermoscopy can distinguish them</b>. No treatment needed &mdash; lesions recur and treatment risks scarring; light electrocautery if wanted</td></tr>
  </table>
  <div class="pearl"><b>General education for any benign lesion in a sun-exposed area.</b> Use the
  visit to counsel on sunscreen, avoiding direct sun during peak hours, and periodic skin
  examination. And before any cosmetic removal, the patient must be told about the <b>risk of
  pigmentary changes and the chance of recurrence</b>.</div>

  <button type="button" class="test-yourself-btn" style="--acc:#17494b" onclick="window.openTestYourself('Test yourself &mdash; Benign Skin Lesions', TEST_YOURSELF.benignskin)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>7. Benign Skin Lesions Prof Griffenkranz 8-25-2025-2.pptx</em>
  (Professor Hugh E. Griffenkranz, MPAS, PA-C), Slides 1&ndash;117, and the PAJ 5500 syllabus
  instructional objectives. Figures are reproduced from the lecture slides and each is cited to its
  slide. Four slides in this deck &mdash; 9, 24, 33, 34 and 42 &mdash; exist only as images, and
  their content has been transcribed rather than extracted.</footer>
</section>'''


TOC = '''%s
  <a class="top-link" href="#benign-skin-lesions">6 &middot; Benign Skin Lesions</a>
  <a href="#bsl-mechanical">6.1 Objective a &mdash; Corns, calluses &amp; the wart that mimics them</a>
  <a href="#bsl-scars">6.2 Objective a &mdash; Keloid vs hypertrophic scar</a>
  <a href="#bsl-keratotic">6.3 Objective a &mdash; Cutaneous horn &amp; skin tags</a>
  <a href="#bsl-pressure">6.4 Objective a &mdash; Pressure injury &amp; pilonidal disease</a>
  <a href="#bsl-nodules">6.5 Objective a &mdash; Nodules to tell from a cancer</a>
  <a href="#bsl-vascular">6.6 Objective a &mdash; The vascular lesions</a>
  <a href="#bsl-other">6.7 Objectives a &amp; b &mdash; Neurofibromatosis &amp; the rest</a>
%s''' % (TOC_OPEN, TOC_CLOSE)

TESTS = '''    benignskin: [
      {q:"A keloid and a hypertrophic scar are both raised. Which single feature separates them?",
       choices:["Whether the scar extends beyond the original wound margin","Whether the scar is painful","Whether the scar is red or pale","Whether the patient had surgery or an accidental wound"],correct:0,
       expl:"A keloid extends BEYOND the wound margin; a hypertrophic scar stays confined to it. Everything else follows: the keloid develops slowly over months and does not regress, the hypertrophic scar appears within four weeks and flattens with time."},
      {q:"What is the recurrence rate after surgical excision of a keloid ALONE?",
       choices:["50 to 100%, and the lesion is often larger","Under 5%","About 20%","About 30%"],correct:0,
       expl:"Which is why excision is always followed by intralesional steroid. Combination therapy has the best success rates, and the single most important treatment is prevention."},
      {q:"A patient has a hard keratin horn on the ear. What is the next step?",
       choices:["Deep shave biopsy to sample the tissue at its base","Reassure, since a horn is benign keratin","Cryotherapy to the projection","Dermoscopy alone"],correct:0,
       expl:"A cutaneous horn arises from ANOTHER lesion, benign or malignant \\u2014 actinic keratosis, wart, seborrheic keratosis, keratoacanthoma, basal or squamous cell carcinoma. Often no clinical feature distinguishes them, and the process at the base is what matters."},
      {q:"A sacral wound shows full-thickness skin loss with adipose tissue visible, but no tendon or bone. Which stage?",
       choices:["Stage 3","Stage 2","Stage 4","Unstageable"],correct:0,
       expl:"Visible fat means stage 3. Stage 4 requires exposed fascia, muscle, tendon, ligament, cartilage or bone. Stage 2 is partial thickness with exposed dermis and no fat visible."},
      {q:"A pressure wound's base is covered entirely by thick eschar. Which stage?",
       choices:["Unstageable","Stage 4","Deep tissue pressure injury","Stage 3"],correct:0,
       expl:"Unstageable means full-thickness loss whose extent CANNOT be determined because slough or eschar obscures it. Deep tissue injury is a persistent non-blanchable deep red or purple discolouration, with skin intact or not."},
      {q:"What is the difference between a sinus and a fistula?",
       choices:["A sinus is a blind track; a fistula connects two epithelium-lined surfaces","A sinus connects two surfaces; a fistula is blind-ending","A sinus is lined by keratin; a fistula by granulation tissue","A sinus is congenital; a fistula is acquired"],correct:0,
       expl:"Both usually arise from a preceding abscess. This distinction is on slide 42, which is an image \\u2014 it appears nowhere in the deck's text."},
      {q:"Which sign is associated with dermatofibroma?",
       choices:["The dimple sign","Fluctuance","A positive Nikolsky sign","The collarette sign"],correct:0,
       expl:"The lesion retracts beneath the skin surface with lateral compression. Dermatofibroma is also described as the most common PAINFUL skin tumour."},
      {q:"Why is a keratoacanthoma excised rather than observed, given that most regress?",
       choices:["It is argued to be a variant of invasive squamous cell carcinoma","It always metastasises if left","Regression leaves an unacceptable scar","It is contagious"],correct:0,
       expl:"It is histopathologically similar to squamous cell carcinoma and strong arguments support classifying it as a variant of the invasive form. Biopsy is the only reliable diagnosis; excise with 5 mm margins, or Mohs for large, recurrent or cosmetically sensitive lesions."},
      {q:"What is actually inside an 'epidermoid cyst', often miscalled a sebaceous cyst?",
       choices:["Keratin","Sebum","Mucin","Lipid-laden macrophages"],correct:0,
       expl:"It is called sebaceous because the contents look like sebum, but the deck states outright that it is not a sebaceous cyst. Standard of care is removal of the ENTIRE capsule, when the cyst is not inflamed."},
      {q:"Which best describes a nevus flammeus?",
       choices:["Present at birth; involution does not occur","Appears six months after birth; quick proliferation and involution","Soft yellow plaques around the eyes associated with lipid disorders","Appears later in life; painless expanding lesion"],correct:0,
       expl:"This was the professor's own discussion question. Nevus flammeus is dilated dermal capillaries with NO endothelial proliferation, which is exactly why it never involutes \\u2014 unlike an infantile hemangioma, which proliferates and then goes away."},
      {q:"A 16-year-old has a moist, vascular, dome-shaped lesion on a finger pad that came up rapidly after injury and bleeds easily. Diagnosis?",
       choices:["Pyogenic granuloma","Cherry angioma","Telangiectasia","Syringoma"],correct:0,
       expl:"Also the professor's own question. Neither pyogenic nor granulomatous \\u2014 a benign vascular tumour responding to irritation, trauma or hormonal change, common in children, young adults and pregnancy."},
      {q:"Which benign lesion should prompt a blood test, and which one?",
       choices:["Xanthelasma \\u2014 screen for hyperlipidemia","Lipoma \\u2014 check thyroid function","Skin tags \\u2014 check haemoglobin A1c","Sebaceous hyperplasia \\u2014 check immunoglobulins"],correct:0,
       expl:"Xanthelasma is a collection of lipid-laden macrophages associated with lipid disorders, and may signify increased risk of cardiac disease. It is the one lesion in this lecture where the blood work is the point."},
      {q:"How many caf\\u00e9 au lait macules are diagnostic in neurofibromatosis type 1, and what is the caveat?",
       choices:["Six or more \\u2014 but the macules alone do not establish the diagnosis","Two or more \\u2014 and they establish it","Six or more \\u2014 and they establish it","Three or more, only after puberty"],correct:0,
       expl:"Over 5 mm prepubertal, over 15 mm postpubertal. Crowe's sign is the intertriginous freckling, and those freckles are SMALLER than 5 mm \\u2014 smaller than the caf\\u00e9 au lait spots."},
      {q:"A patient asks whether removing her cherry angiomas will stop new ones appearing. What do you say?",
       choices:["New lesions will likely develop and there is no way to prevent them","Removal prevents further lesions","They will fade within a year anyway","Each should be biopsied first"],correct:0,
       expl:"Cherry angiomas are acquired, increase with age, and the cause is unknown. Treatment is not necessary unless they bother the patient."},
      {q:"Every over-the-counter corn and callus product in the lecture's table contains which agent?",
       choices:["Salicylic acid","Urea","Trichloroacetic acid","Ammonium lactate"],correct:0,
       expl:"Six branded products, one agent, at 12.6 to 40%. The table is an image on slide 9 \\u2014 the brand names carry no information, the agent is the answer. And the diabetic patient goes to podiatry."}
    ],
'''


def main():
    src = open(GUIDE, encoding="utf-8").read()
    src = strip(OPEN, CLOSE, src)
    src = strip(TOC_OPEN, TOC_CLOSE, src)
    src = re.sub(r"[ \t]*benignskin: \[.*?\n    \],\n", "", src, flags=re.S)

    # ---- renumber what comes after: Pigmented 6 -> 7, How this course is built 7 -> 8
    renames = [
        ('<a class="top-link" href="#pigmented-lesions">6 &middot;',
         '<a class="top-link" href="#pigmented-lesions">7 &middot;'),
        ('<h2 class="deck-title">6 &middot; Pigmented Skin Lesions',
         '<h2 class="deck-title">7 &middot; Pigmented Skin Lesions'),
        ('<a class="top-link" href="#how-course-works" style="color:#8a6508">7 &middot;',
         '<a class="top-link" href="#how-course-works" style="color:#8a6508">8 &middot;'),
        ('<h2 class="deck-title">7 &middot; How this course is built',
         '<h2 class="deck-title">8 &middot; How this course is built'),
    ]
    # Idempotent: the renumber is a one-way move, so a second run finds the
    # NEW form already in place and leaves it alone. Anything else is a real
    # problem and still asserts.
    for old, new in renames:
        if src.count(new) == 1 and old not in src:
            continue                      # already renumbered by an earlier run
        assert src.count(old) == 1, "renumber anchor not unique or missing: %r" % old
        src = src.replace(old, new, 1)
    # subsection numbers 6.N -> 7.N, only inside the pigmented section's own ids
    for n in range(1, 9):
        for pat, rep in ((">6.%d " % n, ">7.%d " % n), (">6.%d &middot;" % n, ">7.%d &middot;" % n)):
            # only where the surrounding tag references a psl- anchor
            src = re.sub(r'(id="psl-[a-z]+">)6\.(%d)( )' % n, r'\g<1>7.\g<2>\g<3>', src)
            src = re.sub(r'(href="#psl-[a-z]+">)6\.(%d)( )' % n, r'\g<1>7.\g<2>\g<3>', src)

    # ---- insert the new section before the pigmented one
    imgs = chart_images()
    body = (BODY.replace("@@IO_MAIN@@", IO_MAIN)
                .replace("@@LESIONS@@", "".join("<li>%s</li>" % x for x in LESIONS)))
    for anchor, names in PLACEMENT:
        i = body.index('id="%s"' % anchor)
        nxt = min([x for x in (body.find("<h3", i + 1), body.find("</section>", i + 1)) if x > 0])
        region = body[i:nxt]
        at = region.rfind("</table>")
        at = i + at + len("</table>") if at >= 0 else nxt
        body = body[:at] + "\n\n  " + build_strip(names, imgs) + body[at:]
    body = OPEN + "\n\n" + body + "\n\n" + CLOSE

    j = src.index('<section class="deck" id="pigmented-lesions">')
    src = src[:j] + body + "\n\n" + src[j:]

    k = src.index('<a class="top-link" href="#pigmented-lesions">')
    src = src[:k] + TOC + "\n  " + src[k:]

    m = src.index("var TEST_YOURSELF = {")
    m = src.index("\n", m) + 1
    src = src[:m] + TESTS + src[m:]

    assert src.count(OPEN) == src.count(CLOSE) == 1
    assert not [t for t in re.findall(r"<img\b[^>]*>", body) if "lazy" in t]
    assert "@@" not in body, "unfilled placeholder survived"
    for fn in re.findall(r'src="cms-derm-chart-images/([^"]+)"', body):
        assert os.path.exists(os.path.join(DIR, "cms-derm-chart-images", fn)), fn

    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added section 6 (%d figures, %d subsections, %d test-yourself questions)"
          % (body.count("<figure"), body.count('class="sub"'), TESTS.count("{q:")))
    print("renumbered: Pigmented Skin Lesions 6 -> 7, How this course is built 7 -> 8")


if __name__ == "__main__":
    main()
