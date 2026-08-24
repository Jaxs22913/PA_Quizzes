#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Lecture 9 (Pre-Malignant and Malignant Cutaneous Lesions) cram topics.

Same structure as add_cms_cram_l7.py. Lecture 9 is LAST in syllabus order, so
these append AFTER the pigmented-lesions section rather than before it.

Three things this deck teaches ONLY as pictures -- the Clark level diagram, the
Stages of Melanoma diagram and the TNM table -- get their own rows, because a
student revising from extracted slide text will not have them at all.

Everything here is from the PowerPoint, not the lecture audio.

Idempotent: exits without writing if the sections are already present.
"""
import os, re, sys, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1",
                    "cms-exam-1-cram-sheet.html")

TOPICS = [
 ("mal-ak-scc", "Actinic Keratosis & Squamous Cell Carcinoma", "#a8452c", "#f6e4de", "#fbf2ef", "#84341f", [
   ("Actinic keratosis — what it IS", "PREMALIGNANT, and on a BIOLOGIC CONTINUUM with keratinocyte carcinoma — not a separate entity. Chronic ultraviolet injury across a FIELD of sun-damaged skin."),
   ("Actinic keratosis — appearance", "0.2–0.6 cm flesh-coloured, pink or slightly hyperpigmented papules with a SANDPAPER TEXTURE. MAY BE MORE APPARENT BY TOUCH THAN BY SIGHT. Face, scalp, ears, forearms, dorsal hands."),
   ("Actinic keratosis — the number", "ABOUT 1 IN 1,000 LESIONS PER YEAR progresses to squamous cell carcinoma. Cumulative FIELD risk matters more than any one lesion's risk."),
   ("Lesion-directed vs field-directed", "LESION-DIRECTED (isolated, clear borders) = LIQUID NITROGEN CRYOTHERAPY; crusts and disappears over 10–14 DAYS. FIELD-DIRECTED (multiple lesions in one region = field cancerization) = topical FLUOROURACIL, IMIQUIMOD, PHOTODYNAMIC THERAPY; fluorouracil + calcipotriene possible benefit."),
   ("When an actinic keratosis needs a BIOPSY", "BLEEDING · INDURATION · ULCERATION · RAPID ENLARGEMENT. Those are NOT typical. The interpretation must separate actinic keratosis from CARCINOMA IN SITU from INVASIVE squamous cell carcinoma, because invasion changes treatment, margins and risk. Treating lesions does NOT clear the field — surveillance continues."),
   ("Squamous cell carcinoma — exposure pattern", "SECOND most common skin cancer. PROLONGED CUMULATIVE sun exposure — contrast basal cell carcinoma's INTENSE INTERMITTENT exposure. May arise from an actinic keratosis."),
   ("Squamous cell carcinoma — appearance", "Small RED CONICAL HARD NODULE that MAY ULCERATE; also a NON-HEALING ULCER, a warty nodule, or an irregular pink plaque with haemorrhagic crust."),
   ("Squamous cell carcinoma — risk raisers", "HIGH-RISK SITES: mucosal surfaces, LIP, EAR, scalp, temple, nose, genitalia. MORE THAN 10 TUMOURS = higher local recurrence and nodal metastasis. Also chronic SCARS, wounds and old RADIATION sites."),
   ("Squamous cell carcinoma — immunosuppression", "Common and often AGGRESSIVE after transplant, with multiple tumours typically at ABOUT 5 YEARS. Chronic lymphocytic leukaemia and human immunodeficiency virus also raise risk and aggressiveness."),
   ("NICOTINAMIDE — the two numbers", "500 mg ORALLY TWICE DAILY both times. Reduces new SQUAMOUS cell carcinoma by ABOUT 30%; reduces BASAL cell carcinoma by ABOUT 20%. If you mix them up, remember the more dangerous cancer gets the bigger number."),
   ("Squamous cell carcinoma — treatment by stage", "IN SITU without high-risk features: imiquimod, topical fluorouracil, or curettage and electrodesiccation. INVASIVE: SURGICAL EXCISION OR MOHS. ADVANCED/METASTATIC: PROGRAMMED DEATH 1 BLOCKADE; CETUXIMAB."),
   ("MOHS indications", "High-risk sites (LIPS, TEMPLES, EARS, NOSE, GENITALIA) · recurrent tumours · aggressive histology with PERINEURAL or PERIVASCULAR invasion · OVER 1 cm ON THE FACE or OVER 2 cm on trunk/extremities · immunosuppression · tumours WITHIN SCARS · genetic disease-associated tumours."),
   ("Squamous cell carcinoma — follow-up and prognosis", "AT LEAST ANNUAL SKIN AND LYMPH-NODE EXAMINATION. Urgent referral for high-risk site/size, recurrence, aggressive histology, immunosuppression, NEUROLOGIC SYMPTOMS or nodal disease. Metastatic rate for actinically induced disease 3–7%."),
 ]),
 ("mal-bcc", "Basal Cell Carcinoma — Subtype Decides Everything", "#1f5f7a", "#dfeaf0", "#eff5f8", "#17495e", [
   ("The headline", "THE MOST COMMON FORM OF CANCER. The HISTOLOGIC subtype determines behaviour and dictates treatment — NOT the clinical appearance."),
   ("Nodular", "Papule/nodule with CENTRAL EROSION, slow growth over years to 1–2 cm. PEARLY OR TRANSLUCENT with TELANGIECTASIAS ACCENTUATED BY STRETCHING THE SKIN."),
   ("Pigmented", "Stippled or focal pigmentation that MAY MIMIC MELANOCYTIC DISEASE. The PEARLY BORDER and SLOW GROWTH are what discriminate."),
   ("Superficial", "Reddish, shiny, SCALY THIN papules or plaques on BACK OR CHEST; may have a thready pearly border and spotty edge pigmentation."),
   ("Morpheaform / sclerosing", "SCAR-LIKE OR IVORY-WHITE, with clinically subtle extension BEYOND the visible pink segment — HIGHER RISK OF SUBCLINICAL SPREAD."),
   ("Warning patterns", "A PEARLY PAPULE · an ERYTHEMATOUS PATCH LARGER THAN 6 mm · a NON-HEALING ULCER. Face, trunk, lower legs."),
   ("The recurrence number", "A SECOND basal cell carcinoma develops in UP TO 50% of patients → at least ANNUAL full-skin examination is mandatory. Excision recurrence 5% OR LESS; MOHS CURE ABOUT 98%."),
   ("Topical option for SELECTED superficial disease", "IMIQUIMOD FIVE NIGHTS WEEKLY FOR 6–10 WEEKS, or FLUOROURACIL TWICE DAILY FOR UP TO 12 WEEKS — with CLINICAL CLEARANCE CONFIRMED AFTERWARDS."),
   ("Advanced or metastatic", "HEDGEHOG PATHWAY INHIBITORS — VISMODEGIB or SONIDEGIB."),
   ("Prognosis", "Slow-growing and highly curable when treated early. The morbidity is LOCAL DESTRUCTION, recurrence, delayed diagnosis and anatomically complex sites — NOT spread."),
 ]),
 ("mal-melanoma", "Malignant Melanoma", "#2f4858", "#e2e8ec", "#f0f3f5", "#22343f", [
   ("The headline numbers", "4th MOST COMMON CANCER IN THE UNITED STATES and the LEADING CAUSE OF DEATH DUE TO SKIN DISEASE. Incidence doubled over 30 years; mortality FALLING with earlier detection and immunotherapy. 2023: ~97,610 new invasive melanomas, ~7,990 deaths, ~TWO-THIRDS OF DEATHS IN MEN."),
   ("Lifetime risk", "ABOUT 2% IN WHITE INDIVIDUALS; 0.1–0.5% IN PERSONS OF COLOUR. Lower but NOT zero — which is why palms, soles and nails are still examined."),
   ("Four subtypes", "SUPERFICIAL SPREADING ~2/3, intermittently sun-exposed skin, radial before vertical growth. LENTIGO MALIGNA, chronically sun-exposed skin of OLDER adults, slow radial phase. NODULAR, RAPIDLY GROWING, OFTEN AMELANOTIC, MAY LACK THE CLASSIC FEATURES. ACRAL LENTIGINOUS, palms/soles/nail units."),
   ("ABCDE", "ASYMMETRY · BORDER irregular, notched or poorly defined · COLOUR variegation (brown, red, white, black, blue in one lesion) · DIAMETER over 6 mm THOUGH SMALLER LESIONS CAN BE MELANOMA · EVOLUTION."),
   ("CLARK LEVELS (slide 50 is an IMAGE)", "I = confined to the EPIDERMIS. II = into the PAPILLARY dermis. III = FILLING the papillary dermis. IV = into the RETICULAR dermis. V = into the SUBCUTANEOUS TISSUE."),
   ("Clark vs Breslow", "CLARK = an anatomic LAYER. BRESLOW = a MEASUREMENT, and BRESLOW IS THE DOMINANT PROGNOSTIC VARIABLE — measure it accurately at the INITIAL BIOPSY. Ulceration and mitotic activity further modify stage-based prognosis."),
   ("STAGES (slide 53 is an IMAGE)", "0 = confined to the epidermal region of skin. I = localised, only in skin, VERY THIN. II = localised, THICKER than stage I. III = SPREAD TO LYMPH NODES. IV = SPREAD TO OTHER ORGANS."),
   ("TNM (slide 54 is an IMAGE TABLE)", "T = primary tumour THICKNESS. N = NUMBER OF TUMOUR-INVOLVED REGIONAL LYMPH NODES. M = NUMBER OF METASTASES AT A DISTANT SITE. Stage 0 = Tis N0 M0 · I = T1–T2a N0 M0 · II = T2b–T4b N0 M0 · III = any N ≥ N1, M0 · IV = ANY T, ANY N, M1."),
   ("Sentinel lymph node biopsy", "Offered or discussed at BRESLOW 1.0 mm OR GREATER, or 0.8 mm OR GREATER WITH ulceration, high mitotic rate or lymphovascular invasion. It is a STAGING PROCEDURE AND MAY NOT ITSELF IMPROVE OVERALL SURVIVAL."),
   ("Re-excision margins", "IN SITU → 0.5–1 cm. LESS THAN 1 mm → 1 cm. MORE THAN 1 mm → 1–2 cm."),
   ("Referral and education", "REFER TO AN EXPERT CENTRE for melanoma DEEPER THAN 1 mm, or with lymph-node or other-site spread. Patients do MONTHLY self-examination with ABCDE and ugly-duckling principles — INCLUDING SCALP, BACK, PALMS, SOLES AND NAILS."),
 ]),
 ("mal-ks-ctcl", "Kaposi Sarcoma & Cutaneous T-Cell Lymphoma", "#7a3f6b", "#efe0eb", "#f8f1f6", "#5e3053", [
   ("Kaposi sarcoma — cause", "HUMAN HERPESVIRUS 8 COMBINED WITH A WEAKENED IMMUNE SYSTEM, in the cells LINING BLOOD AND LYMPH VESSELS. Red or purple macules, plaques or nodules on skin OR MUCOUS MEMBRANES."),
   ("Four forms", "CLASSIC: older men, chronic, RARELY FATAL → palliative local therapy (intralesional vincristine, vinblastine or bleomycin, or radiation). ENDEMIC: young Black men in equatorial Africa, often aggressive, CAN BE RAPIDLY FATAL. IATROGENIC: with immunosuppressive therapy → REDUCE DOSES WHERE FEASIBLE, COORDINATE WITH THE TRANSPLANT TEAM FIRST. EPIDEMIC: acquired immunodeficiency → BEGIN OR OPTIMISE ANTIRETROVIRAL THERAPY."),
   ("The two examination points", "ORAL EXAMINATION IS ESSENTIAL — HARD-PALATE lesions are common and MAY BE THE PRESENTING SITE. And MARKED OEDEMA MAY OCCUR WITH FEW OR NO VISIBLE SKIN LESIONS — do not gauge disease burden from oedema."),
   ("Kaposi sarcoma — systemic therapy", "First line LIPOSOMAL DOXORUBICIN and PACLITAXEL. ANTIRETROVIRAL THERAPY PLUS CHEMOTHERAPY IS MORE EFFECTIVE THAN ANTIRETROVIRAL THERAPY ALONE in advanced disease."),
   ("Cutaneous T-cell lymphoma — course", "Mycosis fungoides. Begins in the skin and MAY REMAIN CONFINED THERE FOR YEARS OR DECADES."),
   ("Cutaneous T-cell lymphoma — appearance", "Localised or generalised erythematous PATCHES or scaly PLAQUES, usually TRUNK, frequently LARGER THAN 5 cm. RESEMBLES PSORIASIS, ECZEMA OR TINEA — which is why it is diagnosed late."),
   ("The two discriminating clues", "ITCH OUT OF PROPORTION to the apparent inflammatory activity, and FOLLICULAR INVOLVEMENT WITH HAIR LOSS. Folliculotropism is what separates it from routine eczema or psoriasis."),
   ("The management philosophy — this is the exam point", "Early AGGRESSIVE treatment HAS NOT BEEN PROVEN TO CURE DISEASE OR PREVENT PROGRESSION, and overly aggressive therapy MAY CAUSE COMPLICATIONS AND PREMATURE DEATH. Stage-directed, SKIN-FIRST: topical corticosteroids, topical mechlorethamine, bexarotene gel, ultraviolet phototherapy."),
 ]),
 ("mal-nail", "Nail Unit Neoplasms — Delay Is the Harm", "#5a5f2a", "#e9ebdc", "#f4f5ed", "#45491d", [
   ("The theme", "DIAGNOSTIC DELAY IS A RECURRING THEME AND A PREVENTABLE HARM. Every item below is arranged around it."),
   ("Nail unit melanoma", "Rare acral melanoma, most often from the MATRIX. NOT CLEARLY ULTRAVIOLET-DRIVEN; ANY SKIN TONE. THUMB AND GREAT TOE. New or evolving LONGITUDINAL MELANONYCHIA IN ONE DIGIT, increasing width, irregular colour/thickness/spacing, PROXIMAL WIDENING OR TRIANGULAR SHAPE, blurred borders, nail splitting, ulceration or subungual mass."),
   ("HUTCHINSON SIGN", "Periungual pigment extending onto the PROXIMAL NAIL FOLD → highly concerning for nail unit melanoma → URGENT EXPERT EVALUATION REGARDLESS OF OTHER FEATURES. (Different sign from the zoster ophthalmicus Hutchinson sign in Lecture 6.)"),
   ("AMELANOTIC nail melanoma", "May be red, pink, eroded or mass-like WITH NO DARK BAND AT ALL. THE ABSENCE OF PIGMENT DOES NOT EXCLUDE MELANOMA. Consider biopsy for any unexplained, progressive SINGLE-NAIL lesion."),
   ("Nail unit squamous cell carcinoma / Bowen", "THE MOST COMMON MALIGNANT NAIL TUMOUR. Chronic UNILATERAL verrucous periungual papule or plaque, subungual hyperkeratosis, onycholysis, oozing, bleeding, nail-plate destruction, longitudinal ERYTHRONYCHIA — OFTEN REPEATEDLY LABELLED A WART, PARONYCHIA OR FUNGAL INFECTION. Associations: high-risk human papillomavirus, immunosuppression, chronic inflammation or trauma, prior radiation, older age."),
   ("Nail unit basal cell carcinoma", "EXCEPTIONALLY UNCOMMON. Consider it in a persistent ULCERATED or PEARLY lesion of the nail fold or bed."),
   ("Glomus tumour", "Small RED-BLUE SUBUNGUAL focus with SEVERE PAROXYSMAL PAIN, EXQUISITE POINT TENDERNESS and COLD SENSITIVITY; THE NAIL MAY LOOK NEARLY NORMAL. The triad SUGGESTS it but DOES NOT REPLACE IMAGING OR SPECIALIST EVALUATION."),
   ("Onychopapilloma / onychomatricoma", "A SINGLE nail with longitudinal ERYTHRONYCHIA or LEUKONYCHIA, distal subungual hyperkeratosis, splinter haemorrhages or localised plate abnormality."),
   ("Before you inspect", "REMOVE THE POLISH. Examine EVERY nail, the periungual skin, PALMS AND SOLES, and the REGIONAL NODES."),
   ("AMPUTATION IS NOT AUTOMATIC", "Contemporary care is DIGIT-SPARING wide excision or MOHS with immunostaining where margins can be reliably assessed. Amputation is reserved for DEEP, EXTENSIVE OR BONE-INVOLVING disease. For nail unit squamous cell carcinoma, COMPLETE MARGIN-CONTROLLED SURGERY IS PREFERRED — partial destructive treatment carries higher recurrence."),
 ]),
 ("mal-approach-age", "Describe Before You Name · Adults & Elderly", "#7a5a1f", "#f1e8d7", "#f9f4ea", "#5e4515", [
   ("Characterise before you diagnose", "PRIMARY LESION TYPE · COLOUR · SURFACE TEXTURE · BORDER DEFINITION · SIZE · DISTRIBUTION · PALPABILITY · ULCERATION · BLEEDING · INDURATION · TEMPORAL EVOLUTION."),
   ("The two examination steps people skip", "THE ORAL CAVITY — a hard-palate lesion may be the presenting site of KAPOSI SARCOMA. And CHRONIC SCARS OR OLD RADIATION FIELDS — SQUAMOUS CELL CARCINOMA arises in them. Also palms, soles, NAILS, and regional nodes for invasive or high-risk disease."),
   ("History that changes the answer", "Onset and change · bleeding or non-healing · sunburns, occupational/recreational ultraviolet, TANNING BEDS · PRIOR SKIN CANCER · IMMUNOSUPPRESSION OR TRANSPLANT · human immunodeficiency virus risk · family history · the lesion THE PATIENT has noticed."),
   ("ADULT", "Cumulative AND intermittent ultraviolet exposure both accumulate through working life. IMMUNOSUPPRESSION AND TRANSPLANT STATUS DOMINATE RISK — squamous cell carcinoma common and aggressive, typically MULTIPLE AT ABOUT 5 YEARS, nicotinamide 500 mg twice daily is a real option. Melanoma self-examination monthly and lifelong. Kaposi sarcoma here is usually EPIDEMIC or IATROGENIC — treat the immune state first."),
   ("ELDERLY", "Actinic keratosis burden and FIELD CANCERIZATION rise with cumulative exposure → favour FIELD-DIRECTED therapy. LENTIGO MALIGNA arises on chronically sun-exposed skin of older adults. CLASSIC Kaposi sarcoma is a disease of older men, managed PALLIATIVELY. In cutaneous T-cell lymphoma the PREMATURE DEATH warning weighs most heavily here. Basal cell carcinoma's UP-TO-50% second-primary rate makes annual full-skin examination non-negotiable."),
   ("The cross-cutting rule", "IMMUNOSUPPRESSION MOVES EVERY ANSWER THE SAME WAY: more disease, more aggressive disease, a LOWER THRESHOLD for biopsy and for Mohs, and EARLIER referral."),
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
    if 'id="mal-ak-scc"' in s:
        sys.exit("Lecture 9 cram sections already present -- nothing to do")

    used = set(re.findall(r"--acc:(#[0-9a-f]{6})", s))
    clash = sorted(used & {t[2] for t in TOPICS})
    assert not clash, "accent already used by another topic: %r" % clash

    # Lecture 9 is LAST in syllabus order, so both the rail links and the
    # sections go AFTER pigmented rather than before it.
    pig = re.search(r'      <a href="#pigmented[^"]*"[^>]*>.*?</a>\n', s, re.S)
    assert pig, "pigmented jump link not found"
    links = "".join(
        '      <a href="#%s" style="color:%s"><span class="dot" style="background:%s"></span>%s</a>\n'
        % (t[0], t[5], t[2], t[1]) for t in TOPICS)
    s = s[:pig.end()] + links + s[pig.end():]

    j = s.index('<section class="topic" id="pigmented')
    j = s.index("\n  </section>", j) + len("\n  </section>\n")
    s = s[:j] + "".join(section(t) for t in TOPICS) + s[j:]

    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th", "div"):
        o, c = len(re.findall(r"<%s[ >]" % tag, s)), s.count("</%s>" % tag)
        assert o == c, "%s: %d open, %d close" % (tag, o, c)
    ids = set(re.findall(r'id="([^"]+)"', s))
    dangling = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a and a not in ids]
    assert not dangling, "dangling jump links: %r" % dangling
    assert "**" not in s, "markdown emphasis left in a cram row -- the template renders plain text"
    order = [m for m in re.findall(r'<section class="topic" id="([^"]+)"', s)]
    assert order.index("pigmented") < order.index("mal-ak-scc"), "Lecture 9 must follow pigmented"

    open(CRAM, "w", encoding="utf-8").write(s)
    print("Lecture 9 cram topics added: %d sections, %d rows"
          % (len(TOPICS), sum(len(t[6]) for t in TOPICS)))
    print("tag balance, jump links, accent uniqueness and syllabus order verified")


if __name__ == "__main__":
    main()
