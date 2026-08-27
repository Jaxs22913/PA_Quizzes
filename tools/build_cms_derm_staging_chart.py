#!/usr/bin/env python3
"""Build the CMS I Dermatology Staging & Grading Chart.

Jaxon, 2026-08-27: "look through all the derm ppts and make a chart with all the
stage things -- ulcer staging, burn staging, etc." Then: "keep the classes
separate, CMS content only," and "Fitzpatrick scale needs to be included."
Then: "Add images to the staging and grading chart, and also make the chart
fullscreen for pc."

SCOPE IS THE NINE CMS EXAM 1 DECKS ONLY. Physical Diagnosis 2 teaches pressure
ulcer staging too, and its wording differs (Beck: Stage III "may extend to but
not through underlying muscle"; the CMS deck: Stage 3 "adipose tissue is
visible"). Clinical Pathophysiology gives wound-healing phases with day ranges
the CMS deck omits. Neither is here -- mixing classes would leave him revising a
version his CMS examiner never taught.

IMAGE-ONLY SLIDES ARE WHY THIS CHART GREW. Per [[image_only_slides]] every slide
whose text extracts as empty was opened and read as a picture. That is how the
pressure injury table (Benign Skin Lesions 33-34) was recovered on the first
build, and on this pass it turned up three whole staging systems the text sweep
could never have found: Clark levels (Pre-malignant & Malignant 50), the
melanoma stage 0-IV figure (53) and the TNM table (54). All three slides
extract as literally nothing.

EVERY FIGURE WAS VIEWED BEFORE IT WAS ASSIGNED. Slide 50 of Benign Skin Lesions
is a photograph of an erupting volcano -- the lecturer's analogy for a
crateriform keratoacanthoma. Dropped into a clinical row it would read as a
lesion photograph, so it is not used.

Slide images are used with the slide cited, per [[media_asset_licensing]].
Marks baked into the pixels (DermNet, NPIAP, McGraw-Hill/Fitzpatrick's source
lines) are left visible on purpose -- they ride along as part of citing.
"""
import os, subprocess, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FOLDER = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 1")
OUT = os.path.join(FOLDER, "cms-derm-staging-chart.html")
IMGDIR = "cms-derm-staging-images"

L2 = "General Dermatology I"
L3 = "Dermatology II"
L4 = "Cutaneous Bacterial Infections"
L6 = "Fungal &amp; Viral Skin Infections"
L7 = "Benign Skin Lesions"
L8 = "Dermatological Infestations"
L10 = "Pre-malignant &amp; Malignant"

# (title, lecture, slides, note, [(level, detail), ...], [(file, caption), ...])
SYSTEMS = [

("Pressure injury staging", L7, "33&ndash;34",
 "The deck presents this as the National Pressure Injury Advisory Panel table, shown for both lightly and darkly pigmented skin. <b>Both slides are images &mdash; the text does not extract</b>, so this is transcribed from the pictures. Stage 1 is the one to know cold: the erythema is <b>non-blanchable</b> and the skin is <b>intact</b>.",
 [("Stage 1", "Localised area of <b>non-blanchable erythema</b> of <b>intact</b> skin."),
  ("Stage 2", "<b>Partial-thickness</b> skin loss with exposed dermis. Wound bed is viable, pink or red, and can be moist, shiny or dry."),
  ("Stage 3", "<b>Full thickness</b> skin loss. <b>Adipose (fat) tissue is visible.</b>"),
  ("Stage 4", "Full thickness skin <b>and tissue</b> loss. <b>Exposed fascia, muscle, tendon, ligament, cartilage or bone.</b>"),
  ("Unstageable", "Obscured full thickness skin and tissue loss. Extent <b>cannot be determined because it is obscured by slough or eschar</b>."),
  ("Deep Tissue", "Persistent <b>non-blanchable deep red / purple discolouration</b>. Skin can be <b>intact or non-intact</b>.")],
 [("npiap-stages-1-3.jpg", "Stages 1&ndash;3, each shown in lightly and darkly pigmented skin. Slide 33 &mdash; this table is the entire slide, as an image."),
  ("npiap-stage4-unstageable-dti.jpg", "Stage 4, Unstageable and Deep Tissue Injury. Slide 34, likewise an image with no extractable text.")]),

("Sunburn &mdash; degree", L3, "91&ndash;95",
 "Only first and second degree are taught for sunburn. <b>Blistering is the line between them.</b> Systemic features are graded separately rather than as a third degree.",
 [("First degree", "Erythema, warmth, tenderness. <b>Confined to the epidermis. No blistering.</b> Resolves in <b>3&ndash;5 days</b> with desquamation."),
  ("Second degree", "<b>Blistering</b>, intense pain, oedema. <b>Partial dermal</b> involvement. Takes <b>1&ndash;2 weeks</b>; risk of secondary infection."),
  ("Systemic (&ldquo;sun poisoning&rdquo;)", "Fever, chills, nausea and vomiting, dehydration, headache, tachycardia &mdash; particularly with large body surface area involvement.")],
 [("sunburn-acute-and-48h.jpg", "The deck's own before-and-after: <b>A</b> acute sunburn, sharply demarcated at the clothing line; <b>B</b> the same back 48 hours later, now blistered and desquamating. Slide 92.")]),

("Stevens-Johnson syndrome &rarr; toxic epidermal necrolysis", L3, "82, 88, 126",
 "One disease spectrum split by <b>body surface area of epidermal detachment</b>. This percentage is the whole distinction &mdash; mucosal involvement, drug trigger and prodrome occur in both and separate nothing.",
 [("Stevens-Johnson syndrome", "<b>Less than 10%</b> body surface area detachment, with mucosal erosions. Hospitalise; stop the drug."),
  ("Overlap", "<b>10&ndash;30%</b> &mdash; the decks define SJS and TEN by their thresholds and treat the middle as the overlap band."),
  ("Toxic epidermal necrolysis", "<b>More than 30%</b> body surface area. Positive Nikolsky sign, &ldquo;wet parchment&rdquo; appearance, severe mucosal erosion. <b>Mortality up to 30&ndash;35%.</b> Burn unit or intensive care is mandatory.")],
 [("sjs-mucosal-erosions.jpg", "Mucosal erosions and haemorrhagic crusting of the lips &mdash; present across the spectrum, so it does <i>not</i> tell you which end you are at. Slide 80."),
  ("ten-epidermal-detachment.jpg", "Sheets of detaching epidermis, the &ldquo;wet parchment&rdquo; appearance. Extent of this is what sets the diagnosis. Slide 86.")]),

("SCORTEN &mdash; severity of illness score for toxic epidermal necrolysis", L3, "89",
 "Calculated <b>within 24 hours of admission and repeated on day 3</b>. <b>Each variable scores one point.</b>",
 [("The seven variables", "Age <b>&gt;40 years</b> &middot; malignancy <b>present</b> &middot; heart rate <b>&gt;120/min</b> &middot; initial body surface area detachment <b>&gt;10%</b> &middot; serum urea nitrogen <b>&gt;10&nbsp;mmol/L (28&nbsp;mg/dL)</b> &middot; serum bicarbonate <b>&lt;20&nbsp;mEq/L</b> &middot; serum glucose <b>&gt;14&nbsp;mmol/L (252&nbsp;mg/dL)</b>"),
  ("Score 0&ndash;1", "Predicted mortality <b>3.2%</b>"),
  ("Score 2", "Predicted mortality <b>12%</b>"),
  ("Score 3", "Predicted mortality <b>35%</b>"),
  ("Score 4", "Predicted mortality <b>58%</b>"),
  ("Score 5 or more", "Predicted mortality <b>90%</b>")],
 []),

("Fitzpatrick skin type", L3, "122",
 "Predicts <b>baseline ultraviolet sensitivity</b> and guides photoprotection counselling. <span class=warn>It grades how skin <i>responds</i> to ultraviolet light &mdash; burning and tanning history &mdash; not what colour it is.</span> The deck is emphatic that <b>all six types are susceptible</b> to cumulative ultraviolet damage, photoaging and skin cancer &mdash; risk varies, it does not disappear. <span class=warn>Types IV&ndash;VI are not immune; delayed diagnosis is common because the index of suspicion is lower, and melanoma in darker-skinned people is frequently diagnosed at an advanced stage.</span>",
 [("Type I", "Very fair, red or blonde hair, freckles, blue or green eyes. <b>Always burns, never tans.</b> Skin cancer risk: <b>highest</b>."),
  ("Type II", "Fair skin, light hair, blue or hazel eyes. <b>Usually burns, sometimes tans.</b> Risk: <b>very high</b>."),
  ("Type III", "Medium skin, brown hair, hazel or brown eyes. <b>Sometimes burns, always tans.</b> Risk: <b>high</b>."),
  ("Type IV", "Olive or light brown skin, dark hair and eyes. <b>Rarely burns, tans easily.</b> Risk: <b>moderate</b>."),
  ("Type V", "Brown skin, dark hair and eyes. <b>Minimally burns, tans deeply.</b> Risk: <b>lower &mdash; not absent</b>."),
  ("Type VI", "Deeply pigmented dark brown or black skin. <b>Never burns, deeply pigmented.</b> Risk: <b>lowest &mdash; not absent</b>.")],
 "SWATCH"),

("Epidermolysis bullosa &mdash; type by level of cleavage", L3, "29",
 "Four inherited types, separated by <b>how deep in the skin the split occurs</b> &mdash; listed here from most superficial to deepest. Combined prevalence is <b>8&ndash;19 per million live births</b>. <b>EB acquisita is the odd one out: autoimmune (anti-COL7A1 immunoglobulin G), not genetic.</b>",
 [("EB Simplex (EBS)", "<b>Intraepidermal</b> cleavage. Keratin 5/14 mutations; autosomal dominant. <b>Most common, about 70% of cases.</b>"),
  ("Junctional EB (JEB)", "<b>Lamina lucida</b> cleavage. Laminin-332 or &alpha;6&beta;4 integrin mutations; autosomal recessive. <b>Highest mortality</b>, especially the Herlitz subtype."),
  ("Dystrophic EB (DEB)", "<b>Sub-lamina densa</b> cleavage. COL7A1 (type VII collagen) mutations; autosomal dominant or recessive."),
  ("Kindler EB", "<b>Mixed cleavage planes.</b> FERMT1 mutation; autosomal recessive.")],
 []),

("Lyme disease &mdash; stage", L8, "71&ndash;76",
 "Three stages defined by <b>how long after the tick bite</b>, not by severity.",
 [("Stage 1 &mdash; early localised", "<b>Erythema migrans</b>: expanding erythematous round or oval lesion <b>&gt;5&nbsp;cm</b> with central clearing and often a darker punctate centre at the bite. <b>About 1 week after the bite.</b> Fever, myalgia, arthralgia, fatigue, lymphadenopathy."),
  ("Stage 2 &mdash; early disseminated", "<b>Days to weeks later.</b> Skin, central nervous system, cardiac, musculoskeletal, eyes. Cranial nerve palsies, meningitis, radiculopathies; arthralgias and arthritis; headache, stiff neck, fatigue, malaise."),
  ("Stage 3 &mdash; late persistent", "<b>Months to years later.</b> Classic manifestation is <b>monoarticular or oligoarticular arthritis of the knee or weight-bearing joints</b>. Subacute encephalopathy with memory loss, mood change, sleep disturbance. Acrodermatitis chronica atrophicans.")],
 [("lyme-erythema-migrans.jpg", "Stage 1: erythema migrans, with the expanding ring and central clearing. Slide 73."),
  ("lyme-acrodermatitis-chronica-atrophicans.jpg", "Stage 3: acrodermatitis chronica atrophicans &mdash; atrophic, translucent skin with veins showing through. Slide 76, the picture that follows the Stage 3 slide.")]),

("Herpes zoster &mdash; three clinical phases", L6, "97&ndash;99, 102",
 "The deck labels these explicitly as the three phases of the disease.",
 [("Pre-eruptive (prodromal)", "<b>Dysesthesia or pain within the affected dermatome.</b> Lesions appear by <b>48&ndash;72 hours</b>. May have malaise, myalgia, headache, photophobia, rarely fever."),
  ("Acute eruptive", "Erythematous macules and papules &rarr; <b>grouped herpetiform vesicles on an erythematous base</b>. New lesions over <b>3&ndash;5 days</b>. Vesicles cloud, rupture, ulcerate, crust, dry. <b>Infectious until the lesions have dried.</b> Resolves over <b>10&ndash;15 days</b>; complete healing may take a month."),
  ("Chronic &mdash; postherpetic neuralgia", "Pain persisting <b>90 days or more after rash onset</b>. Burning, aching, stabbing, electric shock-like, or evoked by light touch (allodynia).")],
 [("zoster-grouped-vesicles.jpg", "The acute eruptive phase: grouped herpetiform vesicles on an erythematous base, the classic finding. Slide 101.")]),

("Varicella &mdash; lesions in several stages at once", L6, "84, 89",
 "Every individual lesion walks the same sequence, but the diagnostic point is that <b>they do not walk it in step</b>. Seeing several stages side by side at one moment is the finding.",
 [("The sequence", "<b>Macule &rarr; papule &rarr; vesicle &rarr; crust.</b>"),
  ("The hallmark", "<b>Several stages appear simultaneously</b> in the same patient &mdash; a generalised pruritic eruption &ldquo;in multiple stages of healing&rdquo;."),
  ("Distribution", "Concentrated on the <b>trunk, scalp and face</b>."),
  ("Infectious period", "From <b>1&ndash;2 days before the rash until all lesions crust</b>. In breakthrough disease without crusts, <b>until no new lesions appear for 24 hours</b>. <span class=warn>The lesions define this, not the fever.</span>"),
  ("Higher complication risk", "Adults, pregnancy, newborn age, and immunocompromise.")],
 [("varicella-day-2-3-5-10.jpg", "One lesion followed from day 2 to day 10. In a real patient lesions at each of these points are present at the same time. Slide 85.")]),

("Wound healing &mdash; four phases", L7, "11",
 "The deck names four phases and one mechanism for increasing strength.",
 [("1. Hemostasis", "The first phase."),
  ("2. Inflammation", ""),
  ("3. Proliferation", ""),
  ("4. Remodeling", "As the scar matures, <b>tensile strength improves through progressive cross-linking of collagen fibres</b> &mdash; it is not fixed at closure.")],
 [("wound-healing-four-phases.jpg", "The four phases with the deck's own time bands: seconds to hours, hours to days, days to weeks, weeks to months. Slide 11.")]),

("Infantile hemangioma &mdash; growth phases", L7, "65&ndash;66",
 "A biphasic natural history, which is what separates it from a vascular malformation that never involutes.",
 [("Earliest sign", "<b>Blanching</b> of the involved skin, then fine <b>telangiectasias</b>, then a red or crimson macule."),
  ("Proliferative", "Rapid growth during the neonatal period (birth to 4 weeks); <b>most growth in the first 4&ndash;6 months</b>."),
  ("Involution", "A subsequent <b>slower involution phase</b>.")],
 [("hemangioma-growth-3days-5months.jpg", "The proliferative phase in one infant from 3 days to 5 months &mdash; the growth curve the parents are being counselled about. Slide 68.")]),

("Keratoacanthoma &mdash; triphasic pattern", L7, "50",
 "The deck calls this triphasic, and it is why the lesion is mistaken for benign.",
 [("1. Rapid growth", "Within <b>6&ndash;8 weeks</b>."),
  ("2. Stabilisation", ""),
  ("3. Regression", "After <b>3&ndash;6 months</b>. <span class=warn>It may instead continue growing or rarely metastasise, and it cannot be told from squamous cell carcinoma clinically &mdash; biopsy is the only reliable method.</span>")],
 [("keratoacanthoma-crateriform.jpg", "The crateriform nodule with its central keratin plug. Slide 49.")]),

("Eczema &mdash; stage of the reaction", L2, "46",
 "Eczema changes appearance over time, so the same condition looks different depending on when it is seen.",
 [("Acute", "Erythema, oedema, papules, vesicles, oozing and crusting."),
  ("Subacute", "Scaling, erythema, papules and excoriations."),
  ("Chronic", "Xerosis, fissuring, <b>lichenification</b> and pigment alteration.")],
 [("eczema-chronic-lichenification.jpg", "Chronic-stage hands: thickened, fissured, lichenified skin with accentuated skin markings. Slide 46.")]),

("Topical corticosteroid potency", L2, "41&ndash;42",
 "Potency is selected <b>by site and severity</b> &mdash; low potency or a non-steroid on the face and eyelids, low to medium on the body. Usual application is <b>twice daily for two weeks</b>. Prolonged use causes atrophy, striae, telangiectasia and hypopigmentation.",
 [("Mild", "Hydrocortisone, all strengths &mdash; 0.1%, 0.5%, 1%, 2.5%"),
  ("Moderate", "Betamethasone valerate 0.025%"),
  ("Medium to high", "Triamcinolone acetonide 0.1% &middot; betamethasone valerate 0.1% &middot; betamethasone dipropionate 0.05%"),
  ("High", "Clobetasol propionate 0.05%")],
 [("topical-steroid-ladder.jpg", "The ladder as the deck shows it, mild at the bottom to very potent at the top, with the sites each band is appropriate for. Slide 41.")]),

("Acne vulgaris &mdash; severity to treatment", L4, "11&ndash;13, 32&ndash;33",
 "<span class=warn>The deck states there is &ldquo;no universal classification system due to the extensive variety of clinical presentations,&rdquo; then says an acne grading system may be helpful and lists what one should account for</span> &mdash; number of lesions, type of lesions, disease severity, anatomical sites, scarring, quality of life. <b>No numbered grades appear anywhere in the deck.</b> Treatment is then given by severity band per the American Academy of Dermatology 2016 guideline, and those bands are the examinable ladder.",
 [("Comedonal (non-inflammatory)", "<b>Topical retinoid.</b> If not tolerated, azelaic acid or salicylic acid."),
  ("Mild papulopustular / mixed", "<b>Topical antimicrobial</b> (benzoyl peroxide alone, or with a topical antibiotic) <b>AND topical retinoid</b> &mdash; or benzoyl peroxide AND a topical antibiotic if a retinoid cannot be tolerated."),
  ("Moderate papulopustular / mixed", "<b>Topical retinoid AND oral antibiotic AND topical benzoyl peroxide.</b>"),
  ("Severe (e.g. nodular)", "<b>Topical retinoid AND oral antibiotic AND topical benzoyl peroxide &mdash; OR oral isotretinoin monotherapy.</b>")],
 [("acne-comedonal-whiteheads-blackheads.jpg", "Comedonal: closed comedones (whiteheads) and open comedones (blackheads). Non-inflammatory. Slide 13."),
  ("acne-papule-pustule.jpg", "The deck's labelled papule and pustule &mdash; the inflammatory lesions that move a patient off the comedonal rung. Slide 11."),
  ("acne-severe-nodular.jpg", "Severe inflammatory and nodular disease, the band where isotretinoin monotherapy becomes an option. Slide 13.")]),

("Melanoma &mdash; Clark level (anatomic depth)", L10, "50",
 "<b>This slide is a figure with no text at all</b>, so the levels below are read off the diagram's own anatomy. Clark level grades melanoma by <b>which layer of skin it has reached</b>. <span class=warn>It has largely been superseded by Breslow thickness, which is the deck's stated dominant prognostic variable</span> &mdash; but Clark levels still appear on pathology reports, so the ladder is worth recognising.",
 [("Level I", "Confined to the <b>epidermis</b>, above the basement membrane &mdash; melanoma in situ."),
  ("Level II", "Invades into the <b>papillary dermis</b>."),
  ("Level III", "<b>Fills and expands the papillary dermis</b>, down to the papillary&ndash;reticular interface."),
  ("Level IV", "Invades the <b>reticular dermis</b>."),
  ("Level V", "Invades the <b>subcutaneous tissue</b>.")],
 [("melanoma-clark-levels.jpg", "Levels I&ndash;V against epidermis, papillary dermis, reticular dermis and subcutaneous tissue. Slide 50 &mdash; the entire slide is this image.")]),

("Melanoma &mdash; Breslow thickness thresholds", L10, "51&ndash;52, 55",
 "<b>Breslow thickness is the dominant prognostic variable</b> and must be measured accurately on the initial biopsy &mdash; which is why a shave that transects the base compromises staging. Ulceration and mitotic rate modify stage-based prognosis.",
 [("Re-excision &mdash; in situ", "<b>0.5&ndash;1&nbsp;cm</b> margin"),
  ("Re-excision &mdash; under 1&nbsp;mm", "<b>1&nbsp;cm</b> margin"),
  ("Re-excision &mdash; over 1&nbsp;mm", "<b>1&ndash;2&nbsp;cm</b> margin"),
  ("Sentinel lymph node biopsy", "Offered or discussed at <b>&ge;1.0&nbsp;mm</b> Breslow thickness, <b>or &ge;0.8&nbsp;mm with additional histologic risk factors</b> (ulceration, high mitotic rate, lymphovascular invasion). It is a <b>staging</b> procedure."),
  ("Expert-centre referral", "Melanoma <b>deeper than 1&nbsp;mm</b>, or with lymph-node or other-site spread.")],
 [("melanoma-survival-by-breslow.jpg", "Five-year survival falling across the same thickness bands, then again with nodal and disseminated disease. Slide 55.")]),

("Melanoma &mdash; overall stage 0 to IV", L10, "53",
 "<b>Another slide that is nothing but a picture.</b> This is the plain-language version of the staging table below it: thickness carries you from 0 to II, and <b>spread</b> is what makes it III or IV.",
 [("Stage 0", "&ldquo;Melanoma confined to epidermal region of skin.&rdquo;"),
  ("Stage I", "&ldquo;Localized disease, only in skin and very thin.&rdquo;"),
  ("Stage II", "&ldquo;Localized disease, thicker than Stage I.&rdquo;"),
  ("Stage III", "&ldquo;Spread to lymph nodes.&rdquo;"),
  ("Stage IV", "&ldquo;Spread to other organs.&rdquo;")],
 [("melanoma-stages-0-4.jpg", "Stages 0 through IV drawn against epidermis, dermis and subcutaneous tissue. Slide 53, image-only. The stage captions above are quoted from this figure.")]),

("Melanoma &mdash; TNM staging table", L10, "54",
 "<b>Image-only slide, transcribed.</b> In this table <b>T</b> is primary tumour thickness, <b>N</b> the number of tumour-involved regional lymph nodes, and <b>M</b> the number of metastases at a distant site. Note the shape of it: <b>every stage from 0 to IIC is N0 M0</b> &mdash; node-negative &mdash; and <b>every stage III subgroup is M0 with positive nodes</b>. Anything M1 is stage IV regardless of the tumour.",
 [("0", "Tis &middot; N0 &middot; M0"),
  ("IA", "T1a or T1b &middot; N0 &middot; M0"),
  ("IB", "T2a &middot; N0 &middot; M0"),
  ("IIA", "T2b or T3a &middot; N0 &middot; M0"),
  ("IIB", "T3b or T4a &middot; N0 &middot; M0"),
  ("IIC", "T4b &middot; N0 &middot; M0"),
  ("IIIA", "T1a/b or T2a &middot; N1a or N2a &middot; M0"),
  ("IIIB", "T0 with N1b or N1c &middot; T1a/b or T2a with N1b/c or N2b &middot; T2b or T3a with N1a/b/c or N2a/b &middot; all M0"),
  ("IIIC", "T0 with N2b/c or N3b/c &middot; T1a/b, T2a/b or T3a with N2c or N3a/b/c &middot; T3b or T4a with any N &ge;N1 &middot; T4b with N1a/b/c or N2a/b/c &middot; all M0"),
  ("IIID", "T4b &middot; N3a/b/c &middot; M0"),
  ("IV", "Any T, Tis &middot; any N &middot; <b>M1</b>")],
 [("melanoma-tnm-table.jpg", "The full table as the deck gives it. Slide 54 &mdash; the slide has no text; this picture is all of it.")]),

("Primary lesion size thresholds", L2, "9&ndash;15",
 "Not staging, but the graded size cut-offs that decide which word is correct. <b>1&nbsp;cm is the cut-off in three of the four pairs.</b>",
 [("Macule &rarr; patch", "Flat, no elevation or depression. <b>Macule &lt;1&nbsp;cm; patch &gt;1&nbsp;cm.</b>"),
  ("Papule &rarr; nodule", "Elevated and solid. <b>Papule &lt;1&nbsp;cm; nodule &gt;1&nbsp;cm.</b>"),
  ("Vesicle &rarr; bulla", "Fluid filled. <b>Vesicle up to &lt;1&nbsp;cm; bulla &gt;1&nbsp;cm.</b>"),
  ("Petechiae &rarr; purpura", "Deposits of blood. <b>Petechiae 1&ndash;2&nbsp;mm; purpura &ge;4&nbsp;mm.</b> <span class=warn>Purpura is a medical emergency until proven otherwise.</span>")],
 [("primary-lesion-morphology.jpg", "The six primary lesions the size rules are applied to. Slide 9."),
  ("petechiae-purpura.jpg", "Blood deposits &mdash; the pair separated by millimetres rather than by a centimetre. Slide 15.")]),
]

FITZ = [("I", "#f6e0d2"), ("II", "#f0cba7"), ("III", "#e0ac7e"),
        ("IV", "#c68a52"), ("V", "#8f5a2f"), ("VI", "#4b2e1e")]


def dims(fname):
    """Real pixel size, so every figure reserves its box and nothing reflows."""
    path = os.path.join(FOLDER, IMGDIR, fname)
    try:
        out = subprocess.check_output(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", path],
            stderr=subprocess.DEVNULL).decode()
        w = h = 0
        for line in out.splitlines():
            line = line.strip()
            if line.startswith("pixelWidth:"):
                w = int(line.split(":")[1])
            elif line.startswith("pixelHeight:"):
                h = int(line.split(":")[1])
        return w, h
    except Exception:
        return 0, 0


def figures(figs):
    if figs == "SWATCH":
        chips = "".join(
            '<div class="chip"><span class="sw" style="background:%s"></span>'
            '<span class="ct">Type %s</span></div>' % (hexv, num)
            for num, hexv in FITZ)
        return ('<figure class="fig swatchfig"><div class="swatch">%s</div>'
                '<figcaption>Representative tones only. <b>Fitzpatrick type is decided by '
                'burning and tanning history, not by matching a colour</b> &mdash; the deck '
                'frames it as ultraviolet sensitivity. Slide 122 carries no figure.'
                '</figcaption></figure>' % chips)
    out = []
    for fname, capt in figs:
        w, h = dims(fname)
        size = ' width="%d" height="%d"' % (w, h) if w and h else ""
        out.append(
            '<figure class="fig"><img src="%s/%s" alt="%s" loading="lazy" '
            'decoding="async"%s><figcaption>%s</figcaption></figure>'
            % (IMGDIR, fname, H.escape(_plain(capt), quote=True), size, capt))
    return "".join(out)


def _plain(s):
    for a, b in (("<b>", ""), ("</b>", ""), ("<i>", ""), ("</i>", ""),
                 ("&mdash;", "-"), ("&ndash;", "-"), ("&middot;", "-"),
                 ("&ldquo;", ""), ("&rdquo;", ""), ("&amp;", "&"),
                 ("&nbsp;", " "), ("&ge;", ">="), ("&lt;", "<"), ("&gt;", ">")):
        s = s.replace(a, b)
    return " ".join(s.split())


def build():
    rows = []
    n_figs = 0
    for i, (title, lec, slides, note, levels, figs) in enumerate(SYSTEMS):
        lv = "".join(
            '<tr><td class="lvl">%s</td><td class="det">%s</td></tr>'
            % (name, detail or "&mdash;") for name, detail in levels)
        fig_html = figures(figs)
        if figs == "SWATCH":
            n_figs += 1
        else:
            n_figs += len(figs)
        if not fig_html:
            body_cls = "sysbody nofig"
        elif figs != "SWATCH" and len(figs) > 1:
            body_cls = "sysbody multi"
        else:
            body_cls = "sysbody"
        figcol = '<div class="figcol">%s</div>' % fig_html if fig_html else ""
        rows.append("""
<section class="sys" id="sys%d">
  <h2>%s</h2>
  <p class="src">%s &middot; slide%s %s</p>
  <p class="note">%s</p>
  <div class="%s">
    <div class="tblcol"><table><tbody>%s</tbody></table></div>
    %s
  </div>
</section>""" % (i, title, lec,
                 "s" if ("&ndash;" in slides or "," in slides) else "",
                 slides, note, body_cls, lv, figcol))

    toc = "".join('<a href="#sys%d">%s</a>' % (i, t)
                  for i, (t, *_rest) in enumerate(SYSTEMS))
    n_levels = sum(len(s[4]) for s in SYSTEMS)

    html = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dermatology Staging &amp; Grading Chart &mdash; CMS I Exam 1</title>
<link rel="stylesheet" href="../theme.css">
<style>
  /* Light palette only, deliberately -- theme.css already inverts the content
     wrapper for dark mode. A page that also ships its own dark palette gets
     both and they cancel. Same reasoning as the comparison chart. */
  :root{
    --acc:#17494b; --acc2:#3f7d7a; --gold:#c08a2e;
    --c-line:#cfdcdb; --c-tbl:#fff; --c-zebra:#f7fbfa; --c-fg:#1b2b2a;
    --c-panel:#eef5f4; --c-warn:#8c3b12; --c-mute:#4c5f5e;
  }
  body{margin:0;}
  /* Fullscreen on a desktop, per Jaxon 2026-08-27. The old 1100px cap left
     half a monitor empty and forced the figures under the table; the width is
     what lets each system read as table-beside-picture instead. Still capped,
     because a table line running the full width of an ultrawide is unreadable. */
  .wrap{max-width:min(2000px,96vw);margin:0 auto;padding:18px 20px 90px;color:var(--c-fg);}
  header.top{text-align:center;padding:14px 0 6px;}
  header.top h1{margin:0 0 6px;color:var(--acc);font-size:1.6rem;line-height:1.25;}
  header.top p{margin:0;color:var(--c-mute);font-size:.92rem;}
  .panel{background:var(--c-panel);border:1px solid var(--c-line);border-radius:12px;
         padding:14px 16px;margin:18px auto 10px;font-size:.93rem;line-height:1.55;max-width:1000px;}
  .panel b{color:var(--acc);}
  nav.toc{display:flex;flex-wrap:wrap;gap:7px;margin:14px 0 26px;justify-content:center;}
  nav.toc a{font-size:.8rem;text-decoration:none;color:var(--acc);border:1px solid var(--c-line);
             background:#fff;border-radius:999px;padding:5px 11px;}
  nav.toc a:hover{background:var(--c-panel);}
  section.sys{margin:0 0 34px;}
  section.sys h2{color:var(--acc);font-size:1.16rem;margin:0 0 3px;}
  p.src{margin:0 0 8px;font-size:.78rem;color:var(--gold);font-weight:700;
        text-transform:uppercase;letter-spacing:.04em;}
  p.note{margin:0 0 10px;font-size:.9rem;line-height:1.55;color:var(--c-fg);max-width:1050px;}

  /* One column until there is room for two; the table keeps the flexible
     track and the figures get a fixed one so photos never stretch. */
  .sysbody{display:grid;grid-template-columns:minmax(0,1fr);gap:18px;align-items:start;}
  @media(min-width:1150px){
    .sysbody:not(.nofig){grid-template-columns:minmax(0,1fr) 360px;}
    /* Sections carrying two or three figures get a wider column and flow them
       two-across. Stacked, a pair of slide captures runs ~800px tall against a
       four-row table and strands half a screen of white beside it; side by side
       they come in around the height of the table they belong to. */
    .sysbody.multi{grid-template-columns:minmax(0,1fr) 500px;}
    .sysbody.multi .figcol{display:grid;grid-template-columns:1fr 1fr;align-items:start;}
  }
  @media(min-width:1500px){
    .sysbody:not(.nofig){grid-template-columns:minmax(0,1fr) 460px;}
    .sysbody.multi{grid-template-columns:minmax(0,1fr) 640px;}
  }
  @media(min-width:1850px){
    .sysbody:not(.nofig){grid-template-columns:minmax(0,1fr) 560px;}
    .sysbody.multi{grid-template-columns:minmax(0,1fr) 780px;}
  }
  .tblcol{min-width:0;}
  .figcol{display:flex;flex-direction:column;gap:14px;min-width:0;}

  table{border-collapse:collapse;width:100%;background:var(--c-tbl);
         border:1px solid var(--c-line);border-radius:10px;overflow:hidden;}
  td{border-top:1px solid var(--c-line);padding:9px 12px;font-size:.9rem;line-height:1.5;vertical-align:top;}
  tr:first-child td{border-top:none;}
  tr:nth-child(even) td{background:var(--c-zebra);}
  td.lvl{width:210px;font-weight:700;color:var(--acc);white-space:nowrap;}
  .warn{color:var(--c-warn);font-weight:600;}

  figure.fig{margin:0;background:#fff;border:1px solid var(--c-line);border-radius:10px;
             overflow:hidden;transition:border-color .15s,box-shadow .15s;}
  figure.fig:hover{border-color:var(--acc2);box-shadow:0 2px 12px rgba(23,73,75,.14);}
  /* Capped, because the inline figure is corroboration and the transcribed table
     beside it is the content. Uncapped, two tall slide captures tower over a
     six-row table and leave half a screen of white. Detail lives one click away
     in the lightbox, so a thumbnail costs nothing here. */
  figure.fig img{display:block;width:100%;height:auto;max-height:330px;
                 object-fit:contain;background:#fff;}
  figure.fig figcaption{font-size:.78rem;line-height:1.5;color:var(--c-mute);
                        padding:8px 11px 10px;border-top:1px solid var(--c-line);}
  figure.fig figcaption b{color:var(--acc);}

  /* Fitzpatrick has no figure in the deck -- slide 122's only image is a 721-byte
     decoration -- so the swatch strip is drawn here rather than lifted. */
  .swatch{display:flex;}
  .swatch .chip{flex:1 1 0;text-align:center;}
  .swatch .sw{display:block;height:74px;}
  .swatch .ct{display:block;font-size:.72rem;font-weight:700;color:var(--c-mute);padding:5px 2px;}

  @media(max-width:620px){
    .wrap{padding:14px 12px 80px;}
    td.lvl{width:auto;display:block;white-space:normal;border-bottom:none;padding-bottom:0;}
    td.det{display:block;border-top:none;padding-top:4px;}
    .swatch .sw{height:56px;}
  }
</style>
</head><body>
<div class="wrap">
<header class="top">
  <h1>Dermatology Staging &amp; Grading Chart</h1>
  <p>Clinical Medicine and Surgery I &middot; Exam 1 &middot; every staged, graded or threshold system in the block</p>
</header>

<div class="panel">
  <b>{{NSYS}} systems, {{NLEV}} levels, {{NFIG}} figures, all from the CMS Exam 1 dermatology decks.</b>
  Each section cites the lecture and slide it came from, and <b>every photograph and
  table enlarges on click</b> &mdash; click to open, click again to magnify, arrow keys to
  step through, Esc or &times; to come back.
  Deliberately <b>CMS only</b> &mdash; Physical Diagnosis 2 also teaches pressure ulcer
  staging and words Stage III differently, and Clinical Pathophysiology gives
  wound-healing phases with day ranges these decks omit. Mixing them would have
  you revising a version your CMS examiner never taught.
  <br><br>
  <b>Four of these systems exist in the decks only as pictures</b>, spread across five
  slides: the pressure injury table (slides 33&ndash;34), Clark levels (50), the melanoma
  stage figure (53) and the TNM table (54). Every one of those slides extracts as no text
  at all &mdash; they had to be read off the images and typed out.
  <br><br>
  Where a deck names a system but never gives its levels &mdash; acne, where the deck
  says outright there is &ldquo;no universal classification system&rdquo; &mdash; that is said
  plainly rather than filled in from outside the lectures.
</div>

<nav class="toc">{{TOC}}</nav>
{{ROWS}}
</div>
<script src="../theme.js"></script>
</body></html>"""
    html = (html.replace("{{NSYS}}", str(len(SYSTEMS)))
                .replace("{{NLEV}}", str(n_levels))
                .replace("{{NFIG}}", str(n_figs))
                .replace("{{TOC}}", toc)
                .replace("{{ROWS}}", "".join(rows)))

    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s - %d systems, %d levels, %d figures, %d KB"
          % (os.path.basename(OUT), len(SYSTEMS), n_levels, n_figs, len(html) // 1024))


if __name__ == "__main__":
    build()
