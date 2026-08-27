#!/usr/bin/env python3
"""Build the CMS I Dermatology Staging & Grading Chart.

Jaxon, 2026-08-27: "look through all the derm ppts and make a chart with all the
stage things -- ulcer staging, burn staging, etc." Then: "keep the classes
separate, CMS content only," and "Fitzpatrick scale needs to be included."

SCOPE IS THE NINE CMS EXAM 1 DECKS ONLY. Physical Diagnosis 2 teaches pressure
ulcer staging too, and its wording differs (Beck: Stage III "may extend to but
not through underlying muscle"; the CMS deck: Stage 3 "adipose tissue is
visible"). Clinical Pathophysiology gives wound-healing phases with day ranges
the CMS deck omits. Neither is here -- mixing classes would leave him revising a
version his CMS examiner never taught.

THE PRESSURE INJURY TABLE CAME OUT OF TWO IMAGES. Slides 33 and 34 of the Benign
Skin Lesions deck extract as nothing but their titles: the whole NPIAP table is a
picture. Per [[image_only_slides]] every empty-looking slide was opened and read
rather than assumed blank, which is the only reason the six stages are here at
all.

Every row cites its deck and slide. Where a deck names a system but never gives
its levels -- the acne grading system is named, its characteristics listed, but
no actual grades -- the chart says so instead of importing them from elsewhere.
"""
import os, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 1", "cms-derm-staging-chart.html")

L2 = "General Dermatology I"
L3 = "Dermatology II"
L4 = "Cutaneous Bacterial Infections"
L6 = "Fungal &amp; Viral Skin Infections"
L7 = "Benign Skin Lesions"
L8 = "Dermatological Infestations"
L10 = "Pre-malignant &amp; Malignant"

# (title, lecture, slides, note, [(level, detail), ...])
SYSTEMS = [
("Pressure injury staging", L7, "33&ndash;34", 
 "The deck presents this as the National Pressure Injury Advisory Panel table, shown for both lightly and darkly pigmented skin. <b>Both slides are images &mdash; the text does not extract</b>, so this is transcribed from the pictures. Stage 1 is the one to know cold: the erythema is <b>non-blanchable</b> and the skin is <b>intact</b>.",
 [("Stage 1", "Localised area of <b>non-blanchable erythema</b> of <b>intact</b> skin."),
  ("Stage 2", "<b>Partial-thickness</b> skin loss with exposed dermis. Wound bed is viable, pink or red, and can be moist, shiny or dry."),
  ("Stage 3", "<b>Full thickness</b> skin loss. <b>Adipose (fat) tissue is visible.</b>"),
  ("Stage 4", "Full thickness skin <b>and tissue</b> loss. <b>Exposed fascia, muscle, tendon, ligament, cartilage or bone.</b>"),
  ("Unstageable", "Obscured full thickness skin and tissue loss. Extent <b>cannot be determined because it is obscured by slough or eschar</b>."),
  ("Deep Tissue", "Persistent <b>non-blanchable deep red / purple discolouration</b>. Skin can be <b>intact or non-intact</b>.")]),

("Sunburn &mdash; degree", L3, "95",
 "Only first and second degree are taught for sunburn. <b>Blistering is the line between them.</b> Systemic features are graded separately rather than as a third degree.",
 [("First degree", "Erythema, warmth, tenderness. <b>Confined to the epidermis. No blistering.</b> Resolves in <b>3&ndash;5 days</b> with desquamation."),
  ("Second degree", "<b>Blistering</b>, intense pain, oedema. <b>Partial dermal</b> involvement. Takes <b>1&ndash;2 weeks</b>; risk of secondary infection."),
  ("Systemic (&ldquo;sun poisoning&rdquo;)", "Fever, chills, nausea and vomiting, dehydration, headache, tachycardia &mdash; particularly with large body surface area involvement.")]),

("Stevens-Johnson syndrome &rarr; toxic epidermal necrolysis", L3, "82, 88, 126",
 "One disease spectrum split by <b>body surface area of epidermal detachment</b>. This percentage is the whole distinction &mdash; mucosal involvement, drug trigger and prodrome occur in both and separate nothing.",
 [("Stevens-Johnson syndrome", "<b>Less than 10%</b> body surface area detachment, with mucosal erosions. Hospitalise; stop the drug."),
  ("Overlap", "<b>10&ndash;30%</b> &mdash; the decks define SJS and TEN by their thresholds and treat the middle as the overlap band."),
  ("Toxic epidermal necrolysis", "<b>More than 30%</b> body surface area. Positive Nikolsky sign, &ldquo;wet parchment&rdquo; appearance, severe mucosal erosion. <b>Mortality up to 30&ndash;35%.</b> Burn unit or intensive care is mandatory.")]),

("SCORTEN &mdash; severity of illness score for toxic epidermal necrolysis", L3, "89",
 "Calculated <b>within 24 hours of admission and repeated on day 3</b>. <b>Each variable scores one point.</b>",
 [("The seven variables", "Age <b>&gt;40 years</b> &middot; malignancy <b>present</b> &middot; heart rate <b>&gt;120/min</b> &middot; initial body surface area detachment <b>&gt;10%</b> &middot; serum urea nitrogen <b>&gt;10&nbsp;mmol/L (28&nbsp;mg/dL)</b> &middot; serum bicarbonate <b>&lt;20&nbsp;mEq/L</b> &middot; serum glucose <b>&gt;14&nbsp;mmol/L (252&nbsp;mg/dL)</b>"),
  ("Score 0&ndash;1", "Predicted mortality <b>3.2%</b>"),
  ("Score 2", "Predicted mortality <b>12%</b>"),
  ("Score 3", "Predicted mortality <b>35%</b>"),
  ("Score 4", "Predicted mortality <b>58%</b>"),
  ("Score 5 or more", "Predicted mortality <b>90%</b>")]),

("Fitzpatrick skin type", L3, "122",
 "Predicts <b>baseline ultraviolet sensitivity</b> and guides photoprotection counselling. The deck is emphatic that <b>all six types are susceptible</b> to cumulative ultraviolet damage, photoaging and skin cancer &mdash; risk varies, it does not disappear. <span class=warn>Types IV&ndash;VI are not immune; delayed diagnosis is common because the index of suspicion is lower, and melanoma in darker-skinned people is frequently diagnosed at an advanced stage.</span>",
 [("Type I", "Very fair, red or blonde hair, freckles, blue or green eyes. <b>Always burns, never tans.</b> Skin cancer risk: <b>highest</b>."),
  ("Type II", "Fair skin, light hair, blue or hazel eyes. <b>Usually burns, sometimes tans.</b> Risk: <b>very high</b>."),
  ("Type III", "Medium skin, brown hair, hazel or brown eyes. <b>Sometimes burns, always tans.</b> Risk: <b>high</b>."),
  ("Type IV", "Olive or light brown skin, dark hair and eyes. <b>Rarely burns, tans easily.</b> Risk: <b>moderate</b>."),
  ("Type V", "Brown skin, dark hair and eyes. <b>Minimally burns, tans deeply.</b> Risk: <b>lower &mdash; not absent</b>."),
  ("Type VI", "Deeply pigmented dark brown or black skin. <b>Never burns, deeply pigmented.</b> Risk: <b>lowest &mdash; not absent</b>.")]),

("Lyme disease &mdash; stage", L8, "71&ndash;75",
 "Three stages defined by <b>how long after the tick bite</b>, not by severity.",
 [("Stage 1 &mdash; early localised", "<b>Erythema migrans</b>: expanding erythematous round or oval lesion <b>&gt;5&nbsp;cm</b> with central clearing and often a darker punctate centre at the bite. <b>About 1 week after the bite.</b> Fever, myalgia, arthralgia, fatigue, lymphadenopathy."),
  ("Stage 2 &mdash; early disseminated", "<b>Days to weeks later.</b> Skin, central nervous system, cardiac, musculoskeletal, eyes. Cranial nerve palsies, meningitis, radiculopathies; arthralgias and arthritis; headache, stiff neck, fatigue, malaise."),
  ("Stage 3 &mdash; late persistent", "<b>Months to years later.</b> Classic manifestation is <b>monoarticular or oligoarticular arthritis of the knee or weight-bearing joints</b>. Subacute encephalopathy with memory loss, mood change, sleep disturbance. Acrodermatitis chronica atrophicans.")]),

("Herpes zoster &mdash; three clinical phases", L6, "97&ndash;99, 102",
 "The deck labels these explicitly as the three phases of the disease.",
 [("Pre-eruptive (prodromal)", "<b>Dysesthesia or pain within the affected dermatome.</b> Lesions appear by <b>48&ndash;72 hours</b>. May have malaise, myalgia, headache, photophobia, rarely fever."),
  ("Acute eruptive", "Erythematous macules and papules &rarr; <b>grouped herpetiform vesicles on an erythematous base</b>. New lesions over <b>3&ndash;5 days</b>. Vesicles cloud, rupture, ulcerate, crust, dry. <b>Infectious until the lesions have dried.</b> Resolves over <b>10&ndash;15 days</b>; complete healing may take a month."),
  ("Chronic &mdash; postherpetic neuralgia", "Pain persisting <b>90 days or more after rash onset</b>. Burning, aching, stabbing, electric shock-like, or evoked by light touch (allodynia).")]),

("Wound healing &mdash; four phases", L7, "11",
 "The deck names four phases and one mechanism for increasing strength.",
 [("1. Hemostasis", "The first phase."),
  ("2. Inflammation", ""),
  ("3. Proliferation", ""),
  ("4. Remodeling", "As the scar matures, <b>tensile strength improves through progressive cross-linking of collagen fibres</b> &mdash; it is not fixed at closure.")]),

("Infantile hemangioma &mdash; growth phases", L7, "65&ndash;66",
 "A biphasic natural history, which is what separates it from a vascular malformation that never involutes.",
 [("Earliest sign", "<b>Blanching</b> of the involved skin, then fine <b>telangiectasias</b>, then a red or crimson macule."),
  ("Proliferative", "Rapid growth during the neonatal period (birth to 4 weeks); <b>most growth in the first 4&ndash;6 months</b>."),
  ("Involution", "A subsequent <b>slower involution phase</b>.")]),

("Keratoacanthoma &mdash; triphasic pattern", L7, "50",
 "The deck calls this triphasic, and it is why the lesion is mistaken for benign.",
 [("1. Rapid growth", "Within <b>6&ndash;8 weeks</b>."),
  ("2. Stabilisation", ""),
  ("3. Regression", "After <b>3&ndash;6 months</b>. <span class=warn>It may instead continue growing or rarely metastasise, and it cannot be told from squamous cell carcinoma clinically &mdash; biopsy is the only reliable method.</span>")]),

("Eczema &mdash; stage of the reaction", L2, "46",
 "Eczema changes appearance over time, so the same condition looks different depending on when it is seen.",
 [("Acute", "Erythema, oedema, papules, vesicles, oozing and crusting."),
  ("Subacute", "Scaling, erythema, papules and excoriations."),
  ("Chronic", "Xerosis, fissuring, <b>lichenification</b> and pigment alteration.")]),

("Topical corticosteroid potency", L2, "42",
 "Potency is selected <b>by site and severity</b> &mdash; low potency or a non-steroid on the face and eyelids, low to medium on the body. Usual application is <b>twice daily for two weeks</b>. Prolonged use causes atrophy, striae, telangiectasia and hypopigmentation.",
 [("Mild", "Hydrocortisone, all strengths &mdash; 0.1%, 0.5%, 1%, 2.5%"),
  ("Moderate", "Betamethasone valerate 0.025%"),
  ("Medium to high", "Triamcinolone acetonide 0.1% &middot; betamethasone valerate 0.1% &middot; betamethasone dipropionate 0.05%"),
  ("High", "Clobetasol propionate 0.05%")]),

("Acne vulgaris &mdash; severity to treatment", L4, "12, 32&ndash;33",
 "<span class=warn>The deck names a grading system but never gives numbered grades.</span> It lists what a grading system should take into account &mdash; number of lesions, type of lesions, disease severity, anatomical sites, scarring, quality of life &mdash; and then treats by severity band per the American Academy of Dermatology 2016 guideline. Those bands are the examinable ladder.",
 [("Comedonal (non-inflammatory)", "<b>Topical retinoid.</b> If not tolerated, azelaic acid or salicylic acid."),
  ("Mild papulopustular / mixed", "<b>Topical antimicrobial</b> (benzoyl peroxide alone, or with a topical antibiotic) <b>AND topical retinoid</b> &mdash; or benzoyl peroxide AND a topical antibiotic if a retinoid cannot be tolerated."),
  ("Moderate papulopustular / mixed", "<b>Topical retinoid AND oral antibiotic AND topical benzoyl peroxide.</b>"),
  ("Severe (e.g. nodular)", "<b>Topical retinoid AND oral antibiotic AND topical benzoyl peroxide &mdash; OR oral isotretinoin monotherapy.</b>")]),

("Melanoma &mdash; Breslow thickness thresholds", L10, "51&ndash;52, 55",
 "<b>Breslow thickness is the dominant prognostic variable</b> and must be measured accurately on the initial biopsy &mdash; which is why a shave that transects the base compromises staging. Ulceration and mitotic rate modify stage-based prognosis.",
 [("Re-excision &mdash; in situ", "<b>0.5&ndash;1&nbsp;cm</b> margin"),
  ("Re-excision &mdash; under 1&nbsp;mm", "<b>1&nbsp;cm</b> margin"),
  ("Re-excision &mdash; over 1&nbsp;mm", "<b>1&ndash;2&nbsp;cm</b> margin"),
  ("Sentinel lymph node biopsy", "Offered or discussed at <b>&ge;1.0&nbsp;mm</b> Breslow thickness, <b>or &ge;0.8&nbsp;mm with additional histologic risk factors</b> (ulceration, high mitotic rate, lymphovascular invasion). It is a <b>staging</b> procedure."),
  ("Expert-centre referral", "Melanoma <b>deeper than 1&nbsp;mm</b>, or with lymph-node or other-site spread.")]),

("Primary lesion size thresholds", L2, "10, 12, 14, 15",
 "Not staging, but the graded size cut-offs that decide which word is correct. <b>1&nbsp;cm is the cut-off in three of the four pairs.</b>",
 [("Macule &rarr; patch", "Flat, no elevation or depression. <b>Macule &lt;1&nbsp;cm; patch &gt;1&nbsp;cm.</b>"),
  ("Papule &rarr; nodule", "Elevated and solid. <b>Papule &lt;1&nbsp;cm; nodule &gt;1&nbsp;cm.</b>"),
  ("Vesicle &rarr; bulla", "Fluid filled. <b>Vesicle up to &lt;1&nbsp;cm; bulla &gt;1&nbsp;cm.</b>"),
  ("Petechiae &rarr; purpura", "Deposits of blood. <b>Petechiae 1&ndash;2&nbsp;mm; purpura &ge;4&nbsp;mm.</b> <span class=warn>Purpura is a medical emergency until proven otherwise.</span>")]),
]


def build():
    rows = []
    for i, (title, lec, slides, note, levels) in enumerate(SYSTEMS):
        lv = "".join(
            f'<tr><td class="lvl">{lv_name}</td><td class="det">{detail or "&mdash;"}</td></tr>'
            for lv_name, detail in levels)
        rows.append(f"""
<section class="sys" id="sys{i}">
  <h2>{title}</h2>
  <p class="src">{lec} &middot; slide{"s" if "&ndash;" in slides or "," in slides else ""} {slides}</p>
  <p class="note">{note}</p>
  <table><tbody>{lv}</tbody></table>
</section>""")

    toc = "".join(f'<a href="#sys{i}">{t}</a>' for i, (t, *_rest) in enumerate(SYSTEMS))
    n_levels = sum(len(s[4]) for s in SYSTEMS)

    html = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dermatology Staging &amp; Grading Chart &mdash; CMS I Exam 1</title>
<link rel="stylesheet" href="../theme.css">
<style>
  /* Light palette only, deliberately -- theme.css already inverts the content
     wrapper for dark mode. A page that also ships its own dark palette gets
     both and they cancel. Same reasoning as the comparison chart. */
  :root{{
    --acc:#17494b; --acc2:#3f7d7a; --gold:#c08a2e;
    --c-line:#cfdcdb; --c-tbl:#fff; --c-zebra:#f7fbfa; --c-fg:#1b2b2a;
    --c-panel:#eef5f4; --c-warn:#8c3b12; --c-mute:#4c5f5e;
  }}
  body{{margin:0;}}
  .wrap{{max-width:1100px;margin:0 auto;padding:18px 16px 90px;color:var(--c-fg);}}
  header.top{{text-align:center;padding:14px 0 6px;}}
  header.top h1{{margin:0 0 6px;color:var(--acc);font-size:1.6rem;line-height:1.25;}}
  header.top p{{margin:0;color:var(--c-mute);font-size:.92rem;}}
  .panel{{background:var(--c-panel);border:1px solid var(--c-line);border-radius:12px;
         padding:14px 16px;margin:18px 0 10px;font-size:.93rem;line-height:1.55;}}
  .panel b{{color:var(--acc);}}
  nav.toc{{display:flex;flex-wrap:wrap;gap:7px;margin:14px 0 26px;}}
  nav.toc a{{font-size:.8rem;text-decoration:none;color:var(--acc);border:1px solid var(--c-line);
             background:#fff;border-radius:999px;padding:5px 11px;}}
  nav.toc a:hover{{background:var(--c-panel);}}
  section.sys{{margin:0 0 30px;}}
  section.sys h2{{color:var(--acc);font-size:1.16rem;margin:0 0 3px;}}
  p.src{{margin:0 0 8px;font-size:.78rem;color:var(--gold);font-weight:700;
        text-transform:uppercase;letter-spacing:.04em;}}
  p.note{{margin:0 0 10px;font-size:.9rem;line-height:1.55;color:var(--c-fg);}}
  table{{border-collapse:collapse;width:100%;background:var(--c-tbl);
         border:1px solid var(--c-line);border-radius:10px;overflow:hidden;}}
  td{{border-top:1px solid var(--c-line);padding:9px 12px;font-size:.9rem;line-height:1.5;vertical-align:top;}}
  tr:first-child td{{border-top:none;}}
  tr:nth-child(even) td{{background:var(--c-zebra);}}
  td.lvl{{width:210px;font-weight:700;color:var(--acc);white-space:nowrap;}}
  .warn{{color:var(--c-warn);font-weight:600;}}
  @media(max-width:620px){{
    td.lvl{{width:auto;display:block;white-space:normal;border-bottom:none;padding-bottom:0;}}
    td.det{{display:block;border-top:none;padding-top:4px;}}
  }}
</style>
</head><body>
<div class="wrap">
<header class="top">
  <h1>Dermatology Staging &amp; Grading Chart</h1>
  <p>Clinical Medicine and Surgery I &middot; Exam 1 &middot; every staged, graded or threshold system in the block</p>
</header>

<div class="panel">
  <b>{len(SYSTEMS)} systems, {n_levels} levels, all from the CMS Exam 1 dermatology decks.</b>
  Each section cites the lecture and slide it came from. Deliberately <b>CMS only</b> &mdash;
  Physical Diagnosis 2 also teaches pressure ulcer staging and words Stage III differently,
  and Clinical Pathophysiology gives wound-healing phases with day ranges these decks omit.
  Mixing them would have you revising a version your CMS examiner never taught.
  <br><br>
  The <b>pressure injury table came out of two pictures</b>: slides 33 and 34 of Benign Skin
  Lesions contain nothing but their titles as text, so the whole National Pressure Injury
  Advisory Panel table had to be read off the images.
  <br><br>
  Where a deck names a system but never gives its levels &mdash; the acne grading system is
  named and its inputs listed, but no numbered grades appear &mdash; that is said outright
  rather than filled in from outside the lectures.
</div>

<nav class="toc">{toc}</nav>
{''.join(rows)}
</div></body></html>"""

    open(OUT, "w", encoding="utf-8").write(html)
    print(f"wrote {os.path.basename(OUT)} — {len(SYSTEMS)} systems, {n_levels} levels, {len(html)//1024} KB")


if __name__ == "__main__":
    build()
