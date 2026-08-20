#!/usr/bin/env python3
"""Add the Lecture 7 (Benign Skin Lesions) topics to the CMS I Exam 1 cram sheet.

Same colour-coded topic/table structure as build_cms_cram_derm.py, and the same
job: the guide carries the explanation, this carries only what has to be
recallable cold the night before.

Inserted BEFORE the pigmented-lesions section so the sheet follows syllabus
order. Idempotent: exits without writing if the sections are already present.
"""
import os, re, sys, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1",
                    "cms-exam-1-cram-sheet.html")

TOPICS = [
 ("benign-mechanical", "Corns, Calluses & Abnormal Wound Healing", "#5d6f2f", "#eaefdf", "#f4f7ee", "#48561f", [
   ("Corn vs callus vs wart", "CORN: focal pressure, CENTRAL KERATIN CORE, <1.5 cm, well defined, hurts on DIRECT DOWNWARD pressure, skin lines RUN THROUGH. CALLUS: broad pressure, diffuse, NO core, larger and irregular, PAINLESS, skin lines run through. WART: human papillomavirus, cauliflower with BLACKENED CENTRE, INTERRUPTS skin lines, hurts on SIDE pressure, not confined to pressure areas."),
   ("Hard vs soft corn", "HARD (clavus durum) = dorsal/lateral FIFTH TOE. SOFT (clavus mollum) = 4th-to-5th WEB SPACE, soft because moisture MACERATES it."),
   ("Corn/callus treatment", "1st REMOVE THE PRESSURE — padding, better footwear. 2nd over-the-counter keratolytics: every product in the deck's table is SALICYLIC ACID, 12.6–40%. DIABETIC → REFER TO PODIATRY."),
   ("Wound healing phases", "HEMOSTASIS → INFLAMMATION → PROLIFERATION → REMODELING. Tensile strength comes from PROGRESSIVE CROSS-LINKING OF COLLAGEN FIBERS."),
   ("KELOID vs HYPERTROPHIC SCAR — the one to know", "KELOID: develops SLOWLY, may appear MONTHS after trauma; EXTENDS BEYOND the wound; enlarges for months–years, NO regression, recurs; EAR LOBE / SHOULDERS / STERNAL NOTCH, rarely across joints; RARE; ASSOCIATED WITH DARK SKIN; often WORSENED by surgery. HYPERTROPHIC: within FOUR WEEKS, soon after surgery; CONFINED to the wound; stable then REGRESSES; where scars cross joints/creases at a RIGHT ANGLE; FREQUENT; NO skin-colour association; IMPROVES with appropriate surgery."),
   ("Keloid treatment numbers", "Silicone sheets 12–24 h/day up to a YEAR. Compression 25 mmHg, 24 h/day, 6–12 MONTHS. Surgical excision alone = 50–100% RECURRENCE, often LARGER → always follow with intralesional steroid. Radiation only in the FIRST TWO WEEKS after excision. Cryotherapy → HYPOPIGMENTATION. Intralesional steroid → TISSUE ATROPHY. Laser best COMBINED with intralesional steroid. Fluorouracil INHIBITS FIBROBLAST PROLIFERATION."),
   ("Both scars: diagnosis", "CLINICAL. BIOPSY ONLY IF GENUINE DOUBT — it may INDUCE NEW SCARRING. Differential for each: the other one, dermatofibroma, foreign-body granuloma."),
   ("Keloid prevention", "THE MOST IMPORTANT TREATMENT. Avoid cosmetic procedures such as ear piercing. Treat adolescent acne EARLY — greatly increases the chance of scar-free healing. Post-op: no stretching, no hot baths, keep clean."),
 ]),
 ("benign-pressure", "Cutaneous Horn, Skin Tags, Pressure Injury & Pilonidal", "#8a4a2c", "#f4e7e0", "#faf3ef", "#6d3921", [
   ("Cutaneous horn — the whole point", "It is NOT a diagnosis. Keratin projection ARISING FROM ANOTHER LESION: actinic keratosis, wart, seborrheic keratosis, keratoacanthoma, basal or squamous cell carcinoma. THE PROCESS AT THE BASE IS WHAT MATTERS. Often NO clinical feature separates benign from malignant → DEEP SHAVE BIOPSY. Caucasians >50, head/neck/upper extremities."),
   ("Acrochordon (skin tag)", "Fibroepithelial PEDUNCULATED PAPILLOMA — narrow stalk, broad tip, 1–10 mm. Females and obese; FRICTION SITES (neck, axilla, groin). 60% OF PEOPLE BY AGE 70. Scissor excision, cryotherapy or electrodesiccation — ANESTHESIA NOT NECESSARY. NEVER cut or pull one off at home: they bleed."),
   ("PRESSURE INJURY STAGING (slides 33–34 are IMAGES)", "1 = NON-BLANCHABLE ERYTHEMA of INTACT skin. 2 = PARTIAL thickness, EXPOSED DERMIS, viable pink/red bed. 3 = FULL thickness, ADIPOSE TISSUE VISIBLE. 4 = full thickness skin AND tissue loss, EXPOSED FASCIA/MUSCLE/TENDON/LIGAMENT/CARTILAGE/BONE. UNSTAGEABLE = obscured by SLOUGH or ESCHAR. DEEP TISSUE = persistent non-blanchable DEEP RED/PURPLE, skin intact or not."),
   ("Pressure injury prevention", "THE BEST MEASURE. Frequent skin assessment · nutrition assessment · moisture control and skin care · REPOSITION EVERY TWO HOURS · manage pain · improve mobility · specialty mattresses. Note the staging tables show every stage in LIGHTLY AND DARKLY pigmented skin — stage 1 erythema is hardest to see on darker skin."),
   ("Pressure injury management", "Depends on STAGE. REFER TO A WOUND CARE SPECIALIST. Control infection. Silicone and hydrocolloid dressings. Surgical referral for DEBRIDEMENT — removes necrotic tissue, eschar and slough, which PROMOTE INFECTION, DELAY GRANULATION and IMPEDE HEALING — and for wound closure."),
   ("Pilonidal cyst", "Pit over the coccyx draws in HAIR AND DEBRIS → follicular plugging → abscess. MALE:FEMALE 3:1. Now believed ACQUIRED, not congenital. Recurrence common. Risks: obesity, local trauma, sedentary, INCREASED HAIR DENSITY IN THE NATAL CLEFT, family history."),
   ("Pilonidal: acute vs chronic", "ACUTE ABSCESS: sudden pain and swelling, warm/tender/erythematous, may be FLUCTUANT (wave-like fluid shift on palpation) → INCISION AND DRAINAGE. CHRONIC: recurrent drainage from SINUS TRACTS, hair may protrude → REFER TO SURGEON for excision. NO diagnostic testing usually needed."),
   ("SINUS vs FISTULA (slide 42 is an IMAGE)", "SINUS = a BLIND track. FISTULA = a track CONNECTING TWO EPITHELIUM-LINED SURFACES. Both usually arise from a preceding abscess."),
 ]),
 ("benign-nodules", "Nodules That Must Be Told From a Cancer", "#4a5f8a", "#e3e8f1", "#f1f4f8", "#3a4b6e", [
   ("Dermatofibroma", "Dermal FIBROBLASTS in dense clusters, 0.5–1 cm. LEGS most common, then arms. F:M 2:1. May follow trauma, viral infection or INSECT BITE. DIMPLE SIGN — retracts beneath the skin on LATERAL compression. Brown halo, pink hue, raised scaly centre. MOST COMMON PAINFUL SKIN TUMOUR. Dermoscopy: PERIPHERAL PIGMENT NETWORK WITH CENTRAL WHITE MASS. Small lesions: shave or punch biopsy is BOTH DIAGNOSTIC AND THERAPEUTIC. Differential includes MELANOMA."),
   ("Keratoacanthoma", "From the PILOSEBACEOUS UNIT. ARGUED TO BE A VARIANT OF INVASIVE SQUAMOUS CELL CARCINOMA. TRIPHASIC: rapid growth in 6–8 WEEKS → stabilization → regression after 3–6 MONTHS. Dome with a CENTRAL KERATIN-FILLED CRATER. Risks: age >40, sun, very fair skin, male, RED TATTOO INK, SKIN TRAUMA (lasers, surgery, cryotherapy), human papillomavirus. BIOPSY IS THE ONLY RELIABLE DIAGNOSIS. EXCISE OR DESTROY — 5 mm MARGINS; MOHS for large, recurrent or cosmetically sensitive. Intralesional METHOTREXATE before excision to shrink it."),
   ("Epidermoid cyst", "Epithelium enclosed in dermis filling with KERATIN. NOT A SEBACEOUS CYST despite the name. M:F 2:1; face, scalp, neck, trunk. CENTRAL PORE/PUNCTUM; expresses cream-coloured pasty material smelling of RANCID CHEESE. Lab tests usually unnecessary. IF INFLAMED: POSTPONE excision, intralesional TRIAMCINOLONE, antibiotics if needed. Standard of care = REMOVE THE ENTIRE CAPSULE when NOT inflamed; 1–3 cm can be punched and emptied."),
   ("Syringoma", "Benign neoplasms of ECCRINE DUCTS. Appear at PUBERTY, females > males. Multiple 1–2 mm papules on EYELIDS and UPPER CHEEKS. Cosmesis only: drugs (oral isotretinoin) → INCREASED RECURRENCE; procedures → POSSIBLE POOR COSMETIC RESULT. Differential: MILIA, XANTHELASMA, basal cell carcinoma."),
 ]),
 ("benign-vascular", "Vascular Lesions — Congenital vs Acquired", "#8f3f5c", "#f3e3ea", "#f9f1f4", "#702e46", [
   ("Sort them this way first", "CONGENITAL: infantile hemangioma, nevus flammeus, nevus simplex. ACQUIRED: cherry angioma, telangiectasia, nevus araneus, pyogenic granuloma. Then within congenital, ask: DOES IT INVOLUTE?"),
   ("Infantile hemangioma", "MOST COMMON TUMOUR OF INFANCY. PROLIFERATION of endothelial cells. Preterm, FEMALE 3:1, Caucasian. Head/neck 60%, trunk 25%, extremities 15%. Earliest sign: BLANCHING → fine telangiectasias → red/crimson macule. Rapid growth birth–4 weeks, most in first 4–6 MONTHS. INVOLUTION 50% BY 5, 70% BY 7, 90% BY 9. Superficial = commonest, bright red (once 'strawberry'); deep = least common, pale/blue."),
   ("Hemangioma treatment", "Serial observation unless: COSMETIC, FUNCTIONAL INVOLVEMENT, DEEP ULCERATION, INFECTION. FIRST LINE = BETA-BLOCKERS (oral propranolol, topical timolol) AND CORTICOSTEROIDS. Pulsed dye laser depth ~1.2 mm. Refer to a VASCULAR ANOMALIES SPECIALIST if the diagnosis is in question."),
   ("Nevus flammeus (port-wine stain)", "DILATION of dermal capillaries through the FULL DEPTH, with NO ENDOTHELIAL PROLIFERATION — which is WHY IT NEVER INVOLUTES. Present at birth, grows with the child, DARKENS AND THICKENS. Blanchable, usually UNILATERAL with SHARP MIDLINE CUTOFF; darkens with crying, fever or overheating. No treatment; tinted waterproof makeup; PULSED DYE LASER."),
   ("Nevus simplex (stork bite)", "More SUPERFICIAL variant of nevus flammeus. Head and neck, more noticeable when crying. FADES WITHIN A YEAR, or persists on the NECK."),
   ("Cherry angioma", "ACQUIRED, capillary/venule PROLIFERATION, cause unknown, INCREASES WITH AGE (once 'senile angioma'). TRUNK, <5 mm, smooth firm deep red, BLANCH. Treat only if it bothers the patient. NEW LESIONS WILL KEEP DEVELOPING AND CANNOT BE PREVENTED."),
   ("Telangiectasia", "Permanently DILATED capillary <1 mm, BLANCHABLE, single/grouped/central punctum. Primary or secondary; ASSOCIATED WITH NUMEROUS DISEASES — the work-up follows the suspected cause."),
   ("Nevus araneus (spider angioma)", "DILATION of preexisting vessels, NO proliferation. ESTROGEN EXCESS: pregnancy or oral contraceptives (RESOLVE after delivery / stopping), CIRRHOSIS and LIVER FAILURE. Hands and fingers in CHILDREN; face, neck, upper trunk, arms in ADULTS. <10 mm, blanches. ASK about pregnancies, hormones, ALCOHOL, hepatotoxic drugs."),
   ("Pyogenic granuloma", "MISNAMED — NEITHER INFECTIOUS NOR GRANULOMATOUS. Response to INJURY or HORMONAL factors; children, young adults, PREGNANCY. Head, neck, FINGERS. Bright red EXOPHYTIC papule, MOIST surface, EPITHELIAL COLLARETTE at base, BLEEDS. Average 6.5 mm. Differential: cherry angioma, MELANOMA, SQUAMOUS CELL CARCINOMA. SURGICAL EXCISION = lowest recurrence, HIGHEST SCARRING, gives histopathology."),
 ]),
 ("benign-nf-other", "Neurofibromatosis, Xanthelasma, Lipoma & the Rest", "#3f6b5a", "#e2ede8", "#f1f6f4", "#2f5344", [
   ("Neurofibromatosis genes", "Von Recklinghausen disease. NF1 = NF1 gene, CHROMOSOME 17. NF2 = NF2 gene, CHROMOSOME 22. Schwannomatosis (NF3) = SMARCB1 and LZTR1, CHROMOSOME 22."),
   ("NF1 — the four skin signs", "CAFÉ AU LAIT SPOTS · CUTANEOUS NEUROFIBROMAS · INTERTRIGINOUS FRECKLING · PLEXIFORM NEUROFIBROMAS."),
   ("Café au lait spots", ">5 mm PREPUBERTAL, >15 mm POSTPUBERTAL. Often the FIRST manifestation; at birth or in the first year; grow in proportion with the child. SIX OR MORE ARE DIAGNOSTIC — BUT THE MACULES ALONE DO NOT ESTABLISH THE DIAGNOSIS."),
   ("Crowe's sign", "INTERTRIGINOUS FRECKLING, freckles <5 mm — SMALLER than café au lait spots. Grouped, more prominent with sun. AXILLARY and INGUINAL; under the breasts is NOT a diagnostic site."),
   ("Neurofibromas", "CUTANEOUS: benign NERVE SHEATH tumours from peripheral nerves; BEGIN AT PUBERTY, increase with age; a few to hundreds. PLEXIFORM: tumour in the tissue COVERING nerves, anywhere EXCEPT brain and spinal cord, large and extensive, MAY BE LOCALLY INVASIVE. Management = SURVEILLANCE with a cutaneous exam at EVERY visit. Education = national and regional SUPPORT GROUPS."),
   ("Xanthelasma", "Soft YELLOW CHOLESTEROL PLAQUES — LIPID-LADEN MACROPHAGES — on the MEDIAL EYELIDS. SCREEN FOR HYPERLIPIDEMIA; MAY SIGNIFY INCREASED CARDIAC RISK. Laser or excision; RECURRENCE COMMON. This is the one benign lesion here where blood work is the point."),
   ("Lipoma", "THE MOST COMMON SOFT TISSUE TUMOUR. Benign overgrowth of SUBCUTANEOUS FAT. Soft, painless, RUBBERY, usually <5 cm; asymptomatic unless adjoining structures invaded. Observe if asymptomatic; excise if COSMETICALLY DEFORMING or the DIAGNOSIS IS UNCERTAIN. Differential: epidermal cyst, dermatofibroma, abscess."),
   ("Digital mucous cyst", "A PSEUDO-CYST — NO CELLULAR LINING. Mucin extruded from a JOINT SPACE compacts dermal cells into something that only MIMICS a capsule. Females > males; ASSOCIATED WITH OSTEOARTHRITIS; over the DISTAL INTERPHALANGEAL joint; may cause a LONGITUDINAL GROOVE in the nail. Observe, or excise if symptomatic or causing nail dystrophy."),
   ("Sebaceous hyperplasia", "SEBOCYTE TURNOVER SLOWS WITH AGE → crowding → gland enlarges. NO KNOWN POTENTIAL FOR MALIGNANT TRANSFORMATION. IMMUNOSUPPRESSION HIGH RISK. Whitish-yellow soft papules 2–9 mm with CENTRAL UMBILICATION, on the face. Differential = BASAL CELL CARCINOMA, and DERMOSCOPY CAN DISTINGUISH THEM. No treatment needed — recurs, and treatment risks scarring; light electrocautery if wanted."),
   ("General education, any benign lesion", "In a sun-exposed area, use the visit to counsel on SUNSCREEN, avoiding direct sun at PEAK HOURS, and PERIODIC SKIN EXAMINATION. Before cosmetic removal, warn about the RISK OF PIGMENTARY CHANGES and the CHANCE OF RECURRENCE."),
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
    if 'id="benign-mechanical"' in s:
        sys.exit("Lecture 7 cram sections already present -- nothing to do")

    # Jump links: insert before the pigmented-lesions link so the rail follows
    # syllabus order rather than the order sections happened to be built in.
    pig = re.search(r'      <a href="#pigmented[^"]*"[^>]*>.*?</a>\n', s, re.S)
    assert pig, "pigmented jump link not found"
    links = "".join(
        '      <a href="#%s" style="color:%s"><span class="dot" style="background:%s"></span>%s</a>\n'
        % (t[0], t[5], t[2], t[1]) for t in TOPICS)
    s = s[:pig.start()] + links + s[pig.start():]

    # Sections: before the pigmented section, same reason.
    j = s.index('<section class="topic" id="pigmented')
    j = s.rindex("\n", 0, j)
    s = s[:j] + "".join(section(t) for t in TOPICS) + s[j:]

    open(CRAM, "w", encoding="utf-8").write(s)

    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th"):
        o, c = len(re.findall(r"<%s[ >]" % tag, s)), s.count("</%s>" % tag)
        assert o == c, "%s: %d open, %d close" % (tag, o, c)
    ids = set(re.findall(r'id="([^"]+)"', s))
    dangling = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a not in ids]
    assert not dangling, "dangling jump links: %r" % dangling
    assert "**" not in s, "markdown emphasis left in a cram row -- the template renders plain text"
    print("Lecture 7 cram topics added: %d (%d rows)" % (len(TOPICS), sum(len(t[6]) for t in TOPICS)))
    print("tag balance and jump links verified")


if __name__ == "__main__":
    main()
