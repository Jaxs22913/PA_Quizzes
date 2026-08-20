#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Lecture 6 (Cutaneous Viral and Fungal Infections) topics to the CMS I Exam 1 cram sheet.

Same colour-coded topic/table structure as the other cram builders, and the same
job: the guide carries the explanation, this carries only what has to be
recallable cold the night before.

THE SLIDE IS AUTHORITATIVE (Jaxon, 2026-08-20) -- every row here comes from the
Jaquith deck, not from the lecture recording.

Inserted BEFORE the Lecture 7 sections so the sheet follows syllabus order.
Idempotent: exits without writing if the sections are already present.

VALIDATE BEFORE WRITING. add_cp_cram_l3.py tripped its own "no markdown" assert
AFTER it had already written the file, which left a corrupt cram sheet on disk
that needed a git checkout to recover. Everything below is checked against the
candidate string first; the file is opened for writing only once it passes.
"""
import os, re, sys, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1",
                    "cms-exam-1-cram-sheet.html")

TOPICS = [
 ("vf-koh-tinea", "KOH, the Dermatophytes & Tinea by Site", "#1f6f5c", "#dcefe9", "#eef7f4", "#175447", [
   ("What KOH does", "DISSOLVES KERATIN, leaves FUNGUS behind. DERMATOPHYTE = branching HYPHAE. MALASSEZIA = short hyphae + clusters of yeast, 'SPAGHETTI AND MEATBALLS'. CANDIDA = BUDDING YEAST + PSEUDOHYPHAE."),
   ("WHERE to sample — 3 rules", "TINEA: the ACTIVE BORDER, never the cleared centre. NAIL: the MOST PROXIMAL accessible diseased nail bed / subungual debris, after trimming the onycholytic nail. ID REACTION: BOTH sites — the diagnosis is the PATTERN (positive primary, NEGATIVE at the reaction)."),
   ("Wood lamp — both limits", "TINEA CAPITIS: may rapidly support MICROSPORUM, but T. TONSURANS (commonest in the US) USUALLY DOES NOT FLUORESCE — a negative lamp excludes NOTHING. PITYRIASIS VERSICOLOR: may show YELLOW-GOLD, but SENSITIVITY IS LIMITED."),
   ("Antifungal classes", "ALLYLAMINE ends in '-fine' (TERBINAFINE, NAFTIFINE) — DESTROYS THE CELL MEMBRANE. IMIDAZOLE ends in '-azole' (CLOTRIMAZOLE, KETOCONAZOLE) — BLOCKS ERGOSTEROL SYNTHESIS."),
   ("Dermatophytes: the defining fact", "Infect and survive ONLY ON DEAD KERATIN — stratum corneum, hair, nails. CANNOT SURVIVE ON MUCOUS MEMBRANES (this is what separates them from Candida). Three genera: MICROSPORUM, TRICHOPHYTON, EPIDERMOPHYTON. Classified BY BODY LOCATION."),
   ("Tinea capitis", "PREADOLESCENT CHILDREN — after puberty SEBUM FATTY ACID changes inhibit growth. Commonest fungal infection in children; T. TONSURANS commonest in the US. Grey ring patches, BLACK DOTS (hair fractured at the surface), LYMPHADENOPATHY OFTEN PRESENT. Fungal particles VIABLE FOR MONTHS. ORAL THERAPY REQUIRED — topicals DO NOT PENETRATE THE HAIR SHAFT."),
   ("Capitis drug pairing", "TERBINAFINE for TRICHOPHYTON. GRISEOFULVIN for MICROSPORUM. Baseline LIVER tests when indicated by agent/label/risk. Adjunct shampoo (selenium sulfide 1–2.5% or ketoconazole 2%) 2–3x weekly REDUCES SPORE SHEDDING but NEVER REPLACES ORAL THERAPY. School exclusion GENERALLY UNNECESSARY once effective therapy has begun."),
   ("Capitis differential", "FOLLICULITIS (perifollicular pustules). PSORIASIS (well demarcated, white/silver scale). SEBORRHEIC DERMATITIS (fine dry or greasy scale; hair LOST BUT NOT BROKEN). ALOPECIA AREATA (skin SMOOTH AND SHINY, no inflammation)."),
   ("Tinea barbae", "TRICHOPHYTON. INFLAMMATORY form = from ANIMALS, boggy pustular kerion-like, SCARRING ALOPECIA may occur. NONINFLAMMATORY = from ANOTHER PERSON, annular scaly or folliculitis-like. KEY SIGN: HAIRS ARE LOOSE AND EASILY REMOVED (unlike bacterial folliculitis). ORAL THERAPY REQUIRED — griseofulvin or terbinafine; shave/remove hair; warm compresses."),
   ("Tinea corporis", "T. RUBRUM. Circular, sharply circumscribed, dry scaly plaque with PROGRESSIVE CENTRAL CLEARING = 'RINGWORM'. KOH FROM THE ACTIVE BORDER. Culture if suspicion high and KOH negative. TOPICAL terbinafine/butenafine/azole applied TO THE LESION AND 1–2 cm BEYOND THE BORDER. Differential: PSORIASIS, NUMMULAR ECZEMA (commonly confused), DISCOID LUPUS, FIXED DRUG ERUPTION."),
   ("NEVER: combination steroid-antifungal", "Steroids MASK AND WORSEN dermatophytosis → TINEA INCOGNITO. Reconsider the diagnosis or test if atypical or failing appropriate therapy."),
   ("Resistant dermatophytosis", "SUSPECT when disease is WIDESPREAD, INTENSELY INFLAMMATORY, EPIDEMIOLOGICALLY LINKED, or FAILS AN ADEQUATE TERBINAFINE COURSE → get SPECIES IDENTIFICATION AND SUSCEPTIBILITY TESTING."),
   ("Tinea cruris", "'JOCK ITCH', CRURAL FOLD. MORE COMMON IN MEN; often coexists with TINEA PEDIS. T. RUBRUM and E. FLOCCOSUM. THE SCROTUM IS TYPICALLY SPARED. Risks: warm moist environment, OBESITY, DIABETES, TIGHT CLOTHING, SHARING CLOTHES. SCROTAL INVOLVEMENT → think CANDIDAL INTERTRIGO (satellite papules/pustules); ERYTHRASMA may fluoresce CORAL-RED."),
   ("Tinea pedis — 3 variants", "MOST COMMON DERMATOPHYTE INFECTION IN ADULTS, men>women. INTERDIGITAL (most common): maceration/erosion, 3rd & 4th INTERSPACES, fissures. HYPERKERATOTIC: plantar thickening in a SHOE DISTRIBUTION → ADD A KERATOLYTIC. VESICULOBULLOUS: the MOIST ACUTE form, pruritic AND PAINFUL, vesicles/bullae on erythema."),
   ("Tinea pedis: testing & education", "Add BACTERIAL STUDIES for marked maceration, malodor, erosion, drainage, ulceration or cellulitis. DRYING BETWEEN THE TOES AFTER BATHING IS ESSENTIAL. Antifungal foot powder in shoes; sandals in communal showers; change socks frequently. TREAT COEXISTING ONYCHOMYCOSIS."),
   ("Tinea manuum", "Associated with TINEA PEDIS, HIGH RECURRENCE. DORSAL hand = like tinea corporis (annular). PALM = like tinea pedis (hyperkeratotic). TWO FEET–ONE HAND SYNDROME: the hand used to SCRATCH the foot. Patients often think it is DRY SKIN OR HARD LABOUR. Treat AS FOR TINEA PEDIS."),
 ]),
 ("vf-nails-yeast", "Onychomycosis, Id Reaction, Incognito, Candida & Versicolor", "#8a5a1f", "#f3e8d8", "#faf4ec", "#6d4718", [
   ("Onychomycosis — the first rule", "CONFIRM FUNGUS BEFORE ORAL THERAPY — MANY DYSTROPHIC NAILS ARE NOT FUNGAL. Tests: KOH, PAS STAIN OF CLIPPINGS, culture, or PCR."),
   ("Onychomycosis facts", "DERMATOPHYTES, especially T. RUBRUM, cause most; yeast and molds also occur. Distal lateral disease → debris, ONYCHOLYSIS, thickening, discoloration, crumbling. Risks: TINEA PEDIS, AGE, DIABETES, TRAUMA, OCCLUSIVE FOOTWEAR, PSORIASIS, VASCULAR DISEASE."),
   ("Onychomycosis treatment + the numbers", "ORAL TERBINAFINE FIRST-LINE: usually 6 WEEKS FINGERNAILS, 12 WEEKS TOENAILS. Baseline LIVER tests per labeling/risk. ITRACONAZOLE is the alternative; FLUCONAZOLE IS OFF LABEL IN THE US. Limited disease: topical EFINACONAZOLE, TAVABOROLE, CICLOPIROX — LOWER CURE RATES. IMPROVEMENT REQUIRES NAIL GROWTH. Manage concomitant tinea pedis."),
   ("ID (dermatophytid) reaction", "Inflammatory dermatitis at a site DISTANT from the primary dermatophytosis, TINEA PEDIS common. Mechanism UNKNOWN, possibly DELAYED-TYPE HYPERSENSITIVITY. Occurs 1–2 WEEKS after the primary infection, EXTREMELY PRURITIC, papules/papulovesicles, COMMON ON THE FINGERS."),
   ("Id reaction — the 3 criteria", "(1) DERMATOPHYTE INFECTION ON ANOTHER PART OF THE BODY. (2) ABSENCE OF FUNGAL ELEMENTS FROM THE ID REACTION SITE. (3) RESOLUTION WHEN THE PRIMARY INFECTION IS TREATED. KOH: (+) primary, (–) id site. TREATMENT = TREAT THE PRIMARY INFECTION. Look for an ASYMPTOMATIC FISSURE OR MACERATION in the toe webs."),
   ("Tinea incognito", "Tinea with an ALTERED APPEARANCE due to INAPPROPRIATE TREATMENT, usually TOPICAL STEROIDS. Cycle: steroid settles it → stopping flares it → more steroid. STOP the corticosteroid/calcineurin inhibitor; KOH+culture FROM AN ACTIVE EDGE; WARN INFLAMMATION MAY REBOUND AFTER WITHDRAWAL. Topical for localized; SYSTEMIC for extensive, follicular or refractory."),
   ("Intertrigo — the ordering matters", "INTERTRIGO IS NOT PRIMARILY AN INFECTION: inflammatory rash from FRICTION, MOISTURE AND HEAT trapped in body folds — CANDIDA MAY SECONDARILY INFECT IT. So CORRECT THE ENVIRONMENT FIRST: dry folds gently, reduce friction/occlusion, moisture-wicking or absorbent material, address incontinence/hyperhidrosis."),
   ("Candida facts + sites + risks", "CANDIDA ALBICANS most common, OPPORTUNISTIC, MALES = FEMALES. YEASTS are UNICELLULAR fungi reproducing BY BUDDING. Sites: INFRAMAMMARY, AXILLARY, ABDOMINAL, INGUINAL, PERINEAL, INTERDIGITAL folds. Risks: obesity, diabetes, incontinence, occlusion, immobility, RECENT ANTIBIOTICS, immunosuppression."),
   ("Reading a fold rash", "SATELLITE PAPULES/PUSTULES SUPPORT CANDIDA. MALODOR, EROSIONS OR DRAINAGE → BACTERIAL COINFECTION. Well-demarcated erythematous patches; pruritus and burning pain."),
   ("NYSTATIN vs AZOLE — know the spectrum", "TOPICAL NYSTATIN TREATS CANDIDA ONLY. TOPICAL AZOLES TREAT CANDIDA AND MANY DERMATOPHYTES. Low-potency corticosteroid ONLY BRIEFLY for marked inflammation and ONLY with adequate antifungal. RECURRENT/EXTENSIVE → evaluate for DIABETES and IMMUNOSUPPRESSION."),
   ("Pityriasis versicolor", "OVERGROWTH of LIPID-DEPENDENT MALASSEZIA that NORMALLY INHABITS THE SKIN → NOT CONSIDERED CONTAGIOUS. More common with HEAT, HUMIDITY, OILY SKIN, SWEATING, IMMUNOSUPPRESSION, CORTICOSTEROID EXPOSURE. Velvety tan/pink/white finely scaling macules 4–5 mm to confluent; NECK, UPPER ARMS, TRUNK, GROIN. RECURRENCE COMMON in warm climates."),
   ("Versicolor: the pigment counselling point", "HYPOPIGMENTATION reflects ALTERED MELANOCYTE FUNCTION and reduced tanning; RECOVERY CAN LAG MONTHS after the yeast is cleared. COLOUR CHANGE ALONE DOES NOT PROVE TREATMENT FAILURE — look for SCALE or confirm with KOH."),
   ("Versicolor differential", "SEBORRHEIC DERMATITIS: erythematous YELLOWISH tint, SOFT GREASY scales. PITYRIASIS ROSEA: HERALD PATCH then CHRISTMAS-TREE distribution. VITILIGO: COMPLETELY WHITE (DEPIGMENTED), autoimmune."),
   ("Versicolor treatment + 2 drug traps", "TOPICAL IS FIRST-LINE: ketoconazole, selenium sulfide, zinc pyrithione, ciclopirox, topical terbinafine. Common selenium sulfide approach: DAILY FOR 7 DAYS, 10-MINUTE CONTACT TIME. ORAL TERBINAFINE IS INEFFECTIVE — inadequate levels IN SWEAT (topical works). DO NOT USE ORAL KETOCONAZOLE — HEPATIC AND ADRENAL TOXICITY outweigh benefit in superficial infection."),
 ]),
 ("vf-vzv", "Varicella, Herpes Zoster & Its Complications", "#6b3a7a", "#ece0f2", "#f6f1f9", "#542e60", [
   ("Varicella — the defining feature", "LESIONS IN MULTIPLE STAGES AT ONCE: macules → papules → vesicles → crusts, SEVERAL STAGES SIMULTANEOUSLY. Concentrate on TRUNK, SCALP, FACE. ADULTS, PREGNANCY, NEWBORN AGE, IMMUNOCOMPROMISE increase complication risk."),
   ("Varicella management", "Usually CLINICAL; LESION PCR preferred when confirmation needed. SUPPORTIVE CARE; AVOID ASPIRIN IN CHILDREN, caution with NSAIDs. Early oral antivirals for HIGHER-RISK patients; IV ACYCLOVIR for SEVERE/DISSEMINATED. Prompt consult for PREGNANCY, NEONATAL EXPOSURE, IMMUNOCOMPROMISE, SEVERE COMPLICATIONS."),
   ("Varicella contagion + precautions", "CONTAGIOUS FROM 1–2 DAYS BEFORE THE RASH UNTIL ALL LESIONS CRUST. Breakthrough disease without crusts: until NO NEW LESIONS FOR 24 HOURS. Healthcare: STANDARD + AIRBORNE + CONTACT precautions. Primary prevention = TWO-DOSE VARICELLA VACCINATION."),
   ("Zoster pathophysiology", "REACTIVATION of latent VZV. Latent in CRANIAL-NERVE OR DORSAL-ROOT GANGLIA; travels ALONG A SENSORY NERVE to the skin as cell-mediated immunity wanes. Risk rises with AGE and IMPAIRED CELL-MEDIATED IMMUNITY."),
   ("Zoster — 3 phases", "PRE-ERUPTIVE: DYSESTHESIA OR PAIN IN THE DERMATOME, lesions by 48–72 HOURS. ACUTE ERUPTIVE: macules/papules → GROUPED HERPETIFORM VESICLES ON AN ERYTHEMATOUS BASE (classic); new lesions over 3–5 DAYS; INFECTIOUS UNTIL LESIONS HAVE DRIED; resolves over 10–15 DAYS. CHRONIC: postherpetic neuralgia."),
   ("Zoster distribution — the numbers", "One or TWO ADJACENT dermatomes; STOPS ABRUPTLY AT THE MIDLINE — DOES NOT CROSS IT. THORACIC 55%, CRANIAL 20%, LUMBAR 15%, SACRAL 5%. ZOSTER SINE HERPETE = pain WITHOUT vesicular eruption. Scars only when DEEPER LAYERS are compromised by EXCORIATION OR SECONDARY INFECTION."),
   ("Can a contact catch shingles? NO", "A susceptible contact DOES NOT 'CATCH SHINGLES'. Exposure to VESICULAR FLUID, or AIRBORNE VIRUS FROM DISSEMINATED DISEASE, CAN CAUSE VARICELLA. Cover lesions, no scratching, hand hygiene, avoid SUSCEPTIBLE PREGNANT PEOPLE, PREMATURE INFANTS and IMMUNOCOMPROMISED PEOPLE UNTIL CRUSTED."),
   ("Zoster antivirals + the 72-hour rule", "VALACYCLOVIR, FAMCICLOVIR or ACYCLOVIR; adjust for RENAL function. START AS SOON AS POSSIBLE, IDEALLY WITHIN 72 HOURS. TREAT AFTER 72 HOURS WHEN: NEW LESIONS ARE FORMING, or OPHTHALMIC, NEUROLOGIC, DISSEMINATED, SEVERE or IMMUNOCOMPROMISED disease. IV ACYCLOVIR + specialist for severe disseminated, visceral, CNS or SIGHT-THREATENING disease."),
   ("Zoster testing", "Typical unilateral dermatomal vesicles = CLINICAL. PCR FROM VESICLE FLUID, SCAB, OR CELLS FROM THE LESION BASE preferred for ATYPICAL, DISSEMINATED, VACCINE-MODIFIED or IMMUNOCOMPROMISED presentations. Differential: HSV, contact dermatitis, impetigo, folliculitis, insect bites, dermatitis herpetiformis, varicella."),
   ("POSTHERPETIC NEURALGIA", "THE MOST COMMON COMPLICATION. PAIN PERSISTING 90 DAYS OR MORE AFTER RASH ONSET. Burning, aching, stabbing, ELECTRIC SHOCK-LIKE, or EVOKED BY LIGHT TOUCH (ALLODYNIA). Lasts MONTHS TO YEARS. Risk: AGE, SEVERE ACUTE PAIN, SEVERE RASH, OPHTHALMIC INVOLVEMENT, IMMUNOCOMPROMISE."),
   ("PHN treatment", "FIRST LINE: GABAPENTIN/PREGABALIN, an appropriate TRICYCLIC ANTIDEPRESSANT, or TOPICAL LIDOCAINE. CAPSAICIN PATCH may help. Individualize for KIDNEY FUNCTION, FALLS, ANTICHOLINERGIC BURDEN, INTERACTIONS. AVOID ROUTINE LONG-TERM OPIOIDS; refer severe/persistent/disabling pain."),
   ("STEROIDS AND PHN — say it as a sentence", "TOPICAL OR SYSTEMIC CORTICOSTEROIDS DO NOT PREVENT PHN AND SHOULD NEVER REPLACE ANTIVIRAL THERAPY. Systemic steroids require individualized risk–benefit assessment."),
   ("Herpes zoster ophthalmicus", "OPHTHALMIC DIVISION (V1) of CN V. HUTCHINSON SIGN = lesions on the TIP/SIDE OF THE NOSE, increases ocular risk — BUT ITS ABSENCE DOES NOT EXCLUDE EYE INVOLVEMENT. START SYSTEMIC ANTIVIRAL IMMEDIATELY. SAME-DAY OPHTHALMOLOGY for eye pain, visual symptoms, red eye, photophobia, Hutchinson sign, or eyelid/ocular involvement."),
   ("RAMSAY HUNT (herpes zoster oticus)", "PERIPHERAL FACIAL PALSY with PAINFUL VESICLES OF THE EAR CANAL/AURICLE OR OROPHARYNX; hearing loss, tinnitus or vertigo may occur. ANTIVIRAL PLUS SYSTEMIC CORTICOSTEROID EARLY when not contraindicated. Urgent ENT/NEUROLOGY. PROTECT THE CORNEA if eyelid closure is impaired."),
   ("SHINGRIX", "TWO DOSES for IMMUNOCOMPETENT ADULTS 50 AND OVER. TWO DOSES for ADULTS 19 AND OVER who ARE OR WILL BE immunodeficient/immunosuppressed. STANDARD INTERVAL 2–6 MONTHS; for IMMUNOCOMPROMISED the second dose may be given 1–2 MONTHS after the first when faster completion is beneficial."),
 ]),
 ("vf-hsv-warts", "Herpes Simplex, Whitlow, Molluscum & Warts", "#1f5f8a", "#dde9f2", "#eff5f9", "#17496b", [
   ("HSV — the assumption to drop", "EITHER TYPE CAN CAUSE ORAL OR GENITAL INFECTION — LESION LOCATION DOES NOT RELIABLY DETERMINE TYPE. HSV-1 GENITAL infection generally RECURS AND SHEDS LESS OFTEN than HSV-2 genital infection."),
   ("HSV transmission & virology", "Contact with infected ORAL/GENITAL SECRETIONS OR LESIONS — AND CAN OCCUR DURING ASYMPTOMATIC SHEDDING. DOUBLE-STRANDED DNA, HERPESVIRIDAE. NEUROVIRULENT — invades and replicates in the nervous system. LATENT BUT LIFELONG."),
   ("HSV presentation", "FIRST EPISODE more prominent and LONGER; RECURRENCES milder and shorter. Prodrome: tenderness, pain, paresthesias or burning — SOME HAVE NO PRODROME. Characteristic prodromal symptoms: LOCALIZED PAIN, TENDER LYMPHADENOPATHY, HEADACHE, GENERALIZED ACHING, FEVER. PE: GROUPED VESICLES ON AN ERYTHEMATOUS BASE breaking down to a SHALLOW PAINFUL ULCER; DYSURIA in women; last ~2 WEEKS; HEAL WITHOUT SCARRING. Triggers: STRESS, ILLNESS, MENSTRUATION, UV LIGHT."),
   ("HSV testing — 2 do's, 2 don'ts", "DO swab a FRESH vesicle, ulcer base or crust for TYPE-SPECIFIC NAAT/PCR — the PREFERRED test. KNOW culture is LESS SENSITIVE (especially healing/recurrent) and a NEGATIVE DOES NOT EXCLUDE; a negative OLDER-lesion swab does not exclude either because SHEDDING IS INTERMITTENT. DON'T use HSV IgM. DON'T routinely screen asymptomatic adults serologically. Confirm LOW-POSITIVE HSV-2 serology with a SECOND METHOD."),
   ("HSV differential", "CHANCROID: bacterial, HAEMOPHILUS DUCREYI, PAINFUL NECROTIZING ULCERS, INGUINAL LYMPHADENOPATHY. SYPHILIS: solitary raised papules that erode, USUALLY PAINLESS. Also TRAUMA and CANDIDIASIS. Evaluate genital ulcers for OTHER CAUSES INCLUDING SYPHILIS, based on risk."),
   ("HSV treatment & counselling", "TREAT EVERY FIRST CLINICAL EPISODE with oral ACYCLOVIR, VALACYCLOVIR or FAMCICLOVIR. Recurrent genital: PATIENT-INITIATED EPISODIC or DAILY SUPPRESSIVE. SUPPRESSIVE VALACYCLOVIR LOWERS HSV-2 TRANSMISSION; CONDOMS REDUCE BUT DO NOT ELIMINATE RISK. Avoid sexual/direct lesion contact DURING THE PRODROME OR ACTIVE LESIONS. TOPICAL ANTIVIRALS = MINIMAL BENEFIT for genital herpes."),
   ("HERPETIC WHITLOW", "PAINFUL HSV OF THE DISTAL FINGER, often INOCULATED THROUGH BROKEN SKIN. Prodromal burning/tingling → GROUPED VESICLES on an ERYTHEMATOUS SWOLLEN DIGIT; fever or lymphangitis may occur. Mimics BACTERIAL FELON/PARONYCHIA, CONTACT DERMATITIS, BLISTERING DACTYLITIS. Confirm atypical cases with NAAT/PCR from a fresh vesicle or lesion base."),
   ("WHITLOW: the one instruction", "DO NOT INCISE AND DRAIN — it DOES NOT TREAT HSV and CAN DELAY HEALING. Cover lesions, hand hygiene, avoid contact with MUCOSA/BROKEN SKIN UNTIL HEALED. Early oral antiviral may shorten symptoms; consider SUPPRESSION for frequent recurrence. Treat bacterial superinfection ONLY WHEN PRESENT."),
   ("Molluscum contagiosum", "BENIGN POXVIRUS. Discrete, smooth, firm, FLESH-COLOURED DOME-SHAPED PEARLY PAPULES, 3–5 mm average; CENTRAL UMBILICATION IS CHARACTERISTIC. Spread by DIRECT SKIN CONTACT, SHARED CONTAMINATED OBJECTS, AUTOINOCULATION; sexual contact common in adults with genital lesions. MOST CLEAR SPONTANEOUSLY but may take MONTHS TO SEVERAL YEARS. Differential: BASAL CELL CARCINOMA, SEBACEOUS HYPERPLASIA, CONDYLOMA ACUMINATUM. Clinical diagnosis; BIOPSY IF UNCERTAIN."),
   ("Molluscum treatment — the ages", "OBSERVATION APPROPRIATE FOR MANY — PROCEDURES MAY BLISTER, PIGMENT OR SCAR. BERDAZIMER 10.3% GEL (ZELSUVMI) once daily AT HOME, AGE 1 AND OVER. CANTHARIDIN 0.7% (YCANTH) applied BY A CLINICIAN, AGE 2 AND OVER. Also CURETTAGE or CRYOTHERAPY; TOPICAL RETINOIDS ARE OFF LABEL."),
   ("Molluscum: 3 higher-risk presentations", "GENITAL in ADOLESCENTS/ADULTS may be SEXUALLY TRANSMITTED — assess for STIs. GENITAL IN A CHILD requires CONTEXT-SENSITIVE ASSESSMENT — LOCATION ALONE DOES NOT PROVE ABUSE. EXTENSIVE OR GIANT FACIAL lesions → EVALUATE FOR IMMUNOSUPPRESSION, INCLUDING HIV when appropriate."),
   ("Warts — the anatomy point", "HUMAN PAPILLOMAVIRUS infecting KERATINOCYTES. CONFINED TO THE EPIDERMIS, but EXPANDS AND DISPLACES THE DERMIS, giving the impression it extends deeper. Underside is ROUND AND SMOOTH — NO ROOTS. Transmitted: SKIN-TO-SKIN, AUTOINOCULATION, CONTAMINATED SURFACES."),
   ("Verruca vulgaris", "Frequently AGES 5–20. Usually HANDS, favouring FINGERS/PALMS. PERIUNGUAL, LIPS & TONGUE more common in NAIL BITERS. Usually <1 cm, elevated round papules, ROUGH GREYISH surface. TINY RED/BLACK DOTS = THROMBOSED DILATED CAPILLARIES; TRIMMING THE SURFACE MAKES THEM MORE PROMINENT. Natural history: SPONTANEOUS RESOLUTION."),
   ("Verruca plana & plantaris", "PLANA (flat): multiple SMOOTH, slightly elevated, FLAT-TOPPED, skin-coloured to light-brown papules; FACE, FOREHEAD, DORSAL HANDS, SHINS; SHAVING SPREADS THEM BY AUTOINOCULATION; balance treatment against DYSPIGMENTATION AND SCARRING. PLANTARIS: WEIGHT-BEARING SURFACE; DO NOT REQUIRE THERAPY UNLESS PAINFUL; cluster into a MOSAIC WART; SALICYLIC ACID 40% or CRYOTHERAPY."),
   ("Wart diagnosis & referral", "CLINICAL. BIOPSY GENERALLY UNNECESSARY but may be appropriate for IMMUNOCOMPROMISED patients or LESIONS OF UNCERTAIN ETIOLOGY (ruling out SCC). Differential: SQUAMOUS CELL CARCINOMA, MOLLUSCUM CONTAGIOSUM, SEBORRHEIC KERATOSIS. BIOPSY/REFER ATYPICAL, BLEEDING, ULCERATED, GROWING or REFRACTORY lesions."),
   ("Wart treatment principles", "NO THERAPY ERADICATES HPV WITH CERTAINTY; RECURRENCE CAN OCCUR. Choose by LOCATION, SYMPTOMS, AGE, PREGNANCY STATUS, IMMUNE STATUS, RISK OF SCARRING/DYSPIGMENTATION. CRYOTHERAPY EVERY 2–3 WEEKS may cause PAIN, BLISTERING, PIGMENT CHANGE. AVOID EXCESSIVE FREEZING/DESTRUCTIVE THERAPY for benign lesions likely to resolve. REFER PERIUNGUAL, FACIAL, EXTENSIVE, RECALCITRANT, DIAGNOSTICALLY UNCERTAIN or IMMUNOCOMPROMISED cases."),
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
    if 'id="vf-koh-tinea"' in s:
        sys.exit("Lecture 6 cram sections already present -- nothing to do")

    # Jump links and sections go BEFORE Lecture 7's first block, so the sheet
    # follows syllabus order rather than build order.
    m = re.search(r'      <a href="#benign-mechanical"[^>]*>.*?</a>\n', s, re.S)
    assert m, "Lecture 7 jump link not found -- run add_cms_cram_l7.py first"
    links = "".join(
        '      <a href="#%s" style="color:%s"><span class="dot" style="background:%s"></span>%s</a>\n'
        % (t[0], t[5], t[2], t[1]) for t in TOPICS)
    s = s[:m.start()] + links + s[m.start():]

    j = s.index('<section class="topic" id="benign-mechanical"')
    j = s.rindex("\n", 0, j)
    s = s[:j] + "".join(section(t) for t in TOPICS) + s[j:]

    # ---- validate the CANDIDATE, before anything touches the disk ----
    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th"):
        o, c = len(re.findall(r"<%s[ >]" % tag, s)), s.count("</%s>" % tag)
        assert o == c, "%s: %d open, %d close" % (tag, o, c)
    ids = set(re.findall(r'id="([^"]+)"', s))
    dangling = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a not in ids]
    assert not dangling, "dangling jump links: %r" % dangling
    assert "**" not in s, "markdown emphasis left in a cram row -- the template renders plain text"
    for t in TOPICS:
        assert 'id="%s"' % t[0] in s, "section %s did not land" % t[0]

    open(CRAM, "w", encoding="utf-8").write(s)
    print("Lecture 6 cram topics added: %d (%d rows)" % (len(TOPICS), sum(len(t[6]) for t in TOPICS)))
    print("tag balance and jump links verified BEFORE writing")


if __name__ == "__main__":
    main()
