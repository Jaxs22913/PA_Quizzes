#!/usr/bin/env python3
"""Add the dermatology block topics to the CMS I Exam 1 cram sheet.

One section per lecture-sized chunk, following the existing colour-coded
topic/table structure. Condensed from the study guide; the guide carries the
explanation and this carries only what has to be recallable cold.
"""
import os, re, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1",
                    "cms-exam-1-cram-sheet.html")

# (id, title, accent, accent-bg, accent-zebra, accent-ink, [(term, fact), ...])
TOPICS = [
 ("skin-layers", "Skin Layers & the Depth Ladder", "#146b5c", "#dcebe7", "#eef6f4", "#0f5548", [
   ("Epidermis", "Keratinocytes in five strata, melanocytes, Langerhans, Merkel. Avascular. Loss of this layer alone = no scar."),
   ("Dermis", "Collagen, elastin, vessels, nerves, follicles, glands. Damage here scars."),
   ("Subcutaneous", "Fat, larger vessels, base of follicles."),
   ("Depth ladder (memorise)", "Impetigo = epidermis. Erysipelas = upper dermis + lymphatics. Cellulitis = deeper dermis + subcutaneous. Necrotizing fasciitis = below all of it."),
   ("Skin functions", "Barrier · thermoregulation · sensation · vitamin D synthesis under ultraviolet B · immune surveillance."),
 ]),
 ("eczema-family", "Eczema, Bullous & Papulosquamous", "#2c7b76", "#e1edec", "#f0f6f5", "#22605c", [
   ("Atopic dermatitis", "Infants cheeks/extensors; children and adults flexures. Personal or family atopy."),
   ("Contact dermatitis", "Sharp margins in the shape of the exposure. Patch testing."),
   ("Seborrheic dermatitis", "Greasy yellow scale on erythema: scalp, brows, nasolabial folds, ears, central chest."),
   ("Dyshidrotic eczema", "Deep tapioca-like vesicles on palms, soles, sides of fingers."),
   ("Stasis vs cellulitis", "Stasis = BILATERAL, chronic, itchy, afebrile. Cellulitis = unilateral, acute, tender, often febrile. “Bilateral cellulitis” is almost always stasis."),
   ("Bullous pemphigoid", "Elderly · SUBepidermal split · TENSE bullae · Nikolsky NEGATIVE · mucosa uncommon · better prognosis."),
   ("Pemphigus vulgaris", "Middle-aged · INTRAepidermal split · FLACCID bullae · Nikolsky POSITIVE · mucosa common and often first."),
   ("Psoriasis", "Well-demarcated plaques, thick silvery scale, Auspitz sign. Extensors, scalp, nails."),
   ("Pityriasis rosea", "Herald patch, then collarette-scaled ovals in a Christmas-tree pattern. Self-limiting 6–8 weeks."),
   ("Lichen planus", "Six Ps: purple, polygonal, pruritic, planar papules and plaques. Wickham striae."),
   ("Alopecia areata vs androgenetic", "Areata = discrete smooth patches, exclamation point hairs, autoimmune. Androgenetic = gradual miniaturisation, temporal/vertex in men."),
 ]),
 ("derm2-reactive", "Dermatology II — Reactive & Systemic", "#c1873a", "#f6eee3", "#fbf7f1", "#97692d", [
   ("Erythema multiforme", "Target lesions, acral. Herpes simplex virus triggers OVER 50%."),
   ("Urticaria", "Individual wheal resolves within 24 h. Persisting past 24 h → BIOPSY for urticarial vasculitis."),
   ("Erythema nodosum", "Tender BILATERAL anterior shin nodules that do NOT ulcerate. Löfgren = EN + ankle arthritis + hilar nodes."),
   ("Granuloma annulare", "Annular papules with NO SCALE — that is what separates it from tinea."),
   ("Pyoderma gangrenosum", "Undermined violaceous border. PATHERGY — debridement makes it worse. Do not debride."),
   ("Acne rosacea", "Central facial erythema, flushing, telangiectasias, NO comedones. Ivermectin cream if Demodex."),
   ("Hyperhidrosis", "Primary = bilateral, focal, adolescent onset, ABSENT IN SLEEP. Generalised or nocturnal → secondary cause."),
   ("Dermatitis herpetiformis", "Perilesional direct immunofluorescence: GRANULAR immunoglobulin A. Dapsone + lifelong gluten-free diet. Screen all for coeliac."),
   ("Acanthosis nigricans", "Screen HbA1c, lipids. Sudden onset in an adult → gastrointestinal malignancy."),
   ("Epidermolysis bullosa", "Transmission electron microscopy + immunofluorescence antigen mapping."),
 ]),
 ("sjs-ten", "SJS / TEN & Photodermatology", "#a4502a", "#f2e6e1", "#f9f3f0", "#803e21", [
   ("The percentages", "SJS under 10% detachment · overlap 10–30% · TEN over 30%. Mortality 1–5% vs 30–35%."),
   ("Drugs", "Aromatic anticonvulsants (carbamazepine, phenytoin, lamotrigine, phenobarbital) · sulfonamides · ALLOPURINOL (the slide says commonest IN ASIA) · oxicam NSAIDs · nevirapine."),
   ("HLA", "B*15:02 with carbamazepine · B*58:01 with allopurinol."),
   ("SCORTEN (1 point each)", "Age over 40 · malignancy · heart rate over 120 · detachment over 10% · urea over 28 mg/dL · bicarbonate under 20 · glucose over 252. Score 5+ → 90% mortality."),
   ("The single action", "STOP THE DRUG. Earlier withdrawal = better survival; each day of delay worsens it."),
   ("Also", "Burn unit/ICU · cyclosporine 3–5 mg/kg has the strongest evidence in TEN · AVOID silver sulfadiazine · antibiotic prophylaxis NOT recommended · daily ophthalmology."),
   ("Phototoxic vs photoallergic", "Phototoxic = non-immunologic, dose-dependent, FIRST exposure, within hours, exaggerated sunburn. Photoallergic = type IV, needs sensitisation, eczematous, extends BEYOND exposed skin."),
   ("Photopatch reading", "Irradiated patch ONLY = photoallergy. BOTH patches = contact allergy."),
   ("Polymorphous light eruption", "Commonest idiopathic photodermatosis. Spring onset, spares chronically exposed skin, hardens by late summer. Antinuclear antibody is MANDATORY to exclude lupus. Prophylactic narrow band ultraviolet B in spring is the most effective prevention."),
   ("Actinic keratosis", "Sandpaper texture · TP53 · field cancerization → field therapy (5-fluorouracil, imiquimod, photodynamic therapy) for confluent disease."),
   ("Dermatoheliosis", "Solar elastosis is the histological hallmark. TRETINOIN is the only agent approved for photoaging."),
   ("Millimetres", "CMS uses 1 cm for macule/patch and papule/plaque. Clinical Pathophysiology uses 5 mm. Answer with the course in front of you."),
 ]),
 ("bacterial-acne", "Acne Vulgaris & Follicular Infection", "#3b5aa0", "#e4e8f2", "#f1f3f8", "#2e467d", [
   ("Four factors", "Follicular hyperkeratinisation · increased sebum · Cutibacterium acnes (anaerobic Gram-positive rod) · inflammation."),
   ("Hallmark", "The COMEDONE. Its absence rules acne out and rosacea in."),
   ("Guideline ladder", "Comedonal → topical retinoid. Mild papulopustular → topical antimicrobial + retinoid. Moderate → retinoid + oral antibiotic + benzoyl peroxide. Severe nodular → same, or isotretinoin monotherapy."),
   ("Benzoyl peroxide", "Add to EVERY antibiotic, topical or oral, to cut resistance. Oral tetracyclines 3–4 months only."),
   ("Isotretinoin safety", "Pregnancy tests before, MONTHLY during, and 5 WEEKS AFTER. iPledge. One month dispensed at a time. Two forms of contraception. NO blood donation."),
   ("Acne education", "Separate tretinoin and benzoyl peroxide by 3+ hours. Wash twice daily max. Improvement 4–6 weeks; back and chest 3–4 months."),
   ("Folliculitis", "Pustule pierced by a CENTRAL HAIR. Staphylococcus aureus. Recurrent → nasal mupirocin twice daily for 5 days."),
   ("Hot tub folliculitis", "Pseudomonas aeruginosa. 8 hours to 5 days after exposure. Spares face, neck, palms, soles. Clears in 2–10 days; dilute acetic acid compresses."),
   ("Pseudofolliculitis barbae", "FOREIGN BODY reaction, not infection. Single/double blade, mild angle, no lift-and-cut. Tretinoin, mild steroid, eflornithine, laser."),
   ("Furuncle vs carbuncle", "Furuncle = one follicle, single opening. Carbuncle = confluent furuncles, sieve-like openings, systemic symptoms, incision and drainage is the mainstay."),
   ("Furuncle antibiotics", "None if afebrile with ONE lesion under 5 mm. Give if over 5 mm, failed drainage, expanding cellulitis, immunocompromise, or endocarditis risk."),
   ("Hidradenitis suppurativa", "Three criteria: typical lesions + axilla/groin + recurrence over twice in 6 months. Smoking cessation essential. WIDE EXCISION for best chance of cure."),
   ("Erythrasma", "Corynebacterium minutissimum. CORAL-RED under Wood's lamp. Topical erythromycin/clindamycin; oral if widespread."),
 ]),
 ("bacterial-spreading", "Impetigo, Cellulitis & Necrotizing Fasciitis", "#8a4a9c", "#efe6f1", "#f7f2f8", "#6c3a7a", [
   ("Impetigo", "Superficial EPIDERMAL. Staphylococcus aureus or Streptococcus pyogenes. Mupirocin topically; CEPHALEXIN is the drug of choice in children."),
   ("Three types", "Non-bullous = honey crust, lymphadenopathy common. Bullous = EXCLUSIVELY staph, epidermolytic toxins, collarettes, nodes uncommon. Ecthyma = ulcerates into dermis, grey-yellow crust, scars."),
   ("Post-streptococcal glomerulonephritis", "Follows impetigo, esp. 3–7 year olds. ANTIBIOTICS DO NOT PREVENT IT. Oedema, tea-coloured urine, proteinuria, hypertension."),
   ("Erysipelas", "Upper dermis + superficial lymphatics. Group A strep. RAISED, SHARPLY DEMARCATED plaque. Penicillin V; clindamycin if allergic. No routine cultures — yield is extremely low."),
   ("Cellulitis", "Deeper dermis + subcutaneous. Borders NOT raised, NOT demarcated. Almost never bilateral. Dicloxacillin/cephalexin; cover MRSA if PURULENT."),
   ("Cellulitis course", "Worse on day 1 is expected. Fever gone by 24 h. Inflammation settles over 1–2 weeks. Fever past 48 h → change antibiotic."),
   ("The cellulitis pitfall", "Tense, cyanotic, bronzed, blanched = devitalised, NOT PERFUSED, antibiotics never reach it. Needs surgical debridement."),
   ("Abscess vs furuncle", "Abscess = traumatic inoculation. Furuncle = infected follicle. Abscess that won't drain → incision and drainage."),
   ("Acute paronychia", "2–5 days after manicure/hangnail/nail biting. Warm soaks; incision and drainage if purulent. CLINDAMYCIN if nail biting (oral flora)."),
   ("Chronic paronychia", "At least 6 weeks. Irritant/allergen reaction, CANDIDA commonest. Keep hands dry + topical antifungal; fluconazole if severe."),
   ("Necrotizing fasciitis", "UNRELENTING PAIN OUT OF PROPORTION. No response at 48 h. Area later goes NUMB (nerves destroyed) — that is progression. Tests must NOT delay debridement."),
   ("Gas on imaging", "Clostridium perfringens produces gas; Group A strep does NOT."),
   ("MRSA orals", "Trimethoprim-sulfamethoxazole · clindamycin · doxycycline (+ linezolid, ciprofloxacin in places). Sensitive = dicloxacillin, cephalexin."),
   ("Primary vs secondary", "Primary = previously normal skin (impetigo through a cut). Secondary = skin already damaged (impetigo invading eczema)."),
 ]),
 ("infestations-1", "Scabies, Lice, Bites & Stings", "#1d6b53", "#dfeae7", "#eff5f3", "#175341", [
   ("Scabies organism", "Sarcoptes scabiei var. hominis. Close contact 15–20 minutes, or bedding/underclothing."),
   ("Pathognomonic lesion", "Thread-like linear or J-shaped BURROW, 1–10 mm, interdigital webs and wrists."),
   ("Itch timing", "First infestation 4–6 weeks (some 3 months). REINFESTATION 2–3 DAYS."),
   ("Distribution", "Webs, finger sides, volar wrists, elbows, axillae, genitals, areolae. HEAD AND NECK SPARED in healthy adults — involved in infants, elderly, immunocompromised."),
   ("Crusted scabies", "Thick scale, MILLIONS of mites, thickened nails, OFTEN NO ITCH, highly infectious. The long-term care outbreak risk."),
   ("Diagnosis", "Skin scraping (number 15 blade + mineral oil, unexcoriated burrow) · dermoscopy DELTA-WING JET · burrow ink test = zigzag line."),
   ("Treatment", "Permethrin overnight to the ENTIRE skin surface + SECOND APPLICATION AT ONE WEEK. Wash at 60°C or bag 14 days. Treat all contacts. Ivermectin for crusted/immunosuppressed. Itch may last 4 weeks after cure."),
   ("Nits vs dandruff", "Nits CANNOT be removed from the hair shaft. Live lice = active; nits = past or present."),
   ("Lice sites", "Head = children 3–12, head-to-head. Body = homeless/crowded, clothing seams. Pubic = MACULAE CAERULAE, often a concurrent sexually transmitted infection."),
   ("School policy", "A NO-NIT POLICY IS NOT RECOMMENDED (American Academy of Pediatrics) — nits persist for months. Fumigation not recommended."),
   ("Bedbugs", "PAINLESS bites in a linear ROW OF THREE (breakfast, lunch, dinner). Blood flecks on linen. Survive a year without a meal. PROFESSIONAL EXTERMINATOR required."),
   ("Tungiasis", "Female flea burrows into the skin. Feet/web spaces after barefoot beach exposure. Dermoscopy shows ovoid eggs. Excision or cryotherapy + tetanus + antibiotics."),
   ("Hymenoptera", "SCRAPE the honeybee stinger off with a card edge. Systemic reaction in 0.4–3%. Severe LOCAL = oedema and induration up to a week. Auto-injector + desensitisation after anaphylaxis."),
   ("Caterpillars", "Gypsy moth → papules in linear streaks. Asp/puss (most poisonous) → intense pain, TRAIN-TRACK PURPURA. Strip hairs with ADHESIVE TAPE."),
 ]),
 ("infestations-2", "Spiders, Ticks & Water Exposure", "#8f3f52", "#f2e2e6", "#f9f0f2", "#71313f", [
   ("Black widow", "Red HOURGLASS. Alpha-latrotoxin. Painful bite; sweating and piloerection in 30 min, then CRAMPING ABDOMINAL PAIN and spasm. Calcium gluconate, narcotics, muscle relaxants, benzodiazepines, tetanus."),
   ("Brown recluse", "Dark FIDDLE on cephalothorax. Midwest and Southeast. RED, WHITE AND BLUE SIGN. Necrosis 2–3 days, eschar 5–7 days. DELAY SURGERY until the wound is stable."),
   ("Hobo spider", "Grey HERRINGBONE. Pacific Northwest, July–September. PAINLESS bite, induration and paraesthesia in 30 min, vesicles by 36 h. Supportive; heals over weeks."),
   ("Tarantula", "Shed hairs embed in skin and EYES. Topical steroid; OPHTHALMOLOGY for the eye."),
   ("Cutaneous larva migrans", "Animal hookworm from sand/soil with dog or cat faeces. Serpentine trail advancing 2–3 cm A DAY. Albendazole 400 mg × 3 days or ivermectin. NO excision, NO cryotherapy."),
   ("Cercarial dermatitis", "Swimmer's itch. Flatworm cercariae via snails. Prickling 30 min → itch 10–12 h → papules 24 h → peak 48–72 h. Symptomatic only."),
   ("Lyme disease", "Borrelia burgdorferi. ERYTHEMA MIGRANS over 5 cm with central clearing, about 1 week after the bite. Diagnose and TREAT CLINICALLY if the lesion is present."),
   ("Lyme stages", "1 early localised (erythema migrans) · 2 early disseminated days-to-weeks (cranial nerve palsy, meningitis, radiculopathy) · 3 late persistent months-to-years (MONOARTICULAR ARTHRITIS of a weight-bearing joint, encephalopathy, acrodermatitis chronica atrophicans)."),
   ("Lyme treatment", "DOXYCYCLINE first line; AMOXICILLIN in children and pregnancy; macrolide second line; 10–14 days. Intravenous ceftriaxone for arthritis and acrodermatitis. NO human vaccine (one for dogs)."),
   ("Rocky Mountain spotted fever", "Rickettsia rickettsii. Triad fever/headache/rash in only ~60%. Rash starts ANKLES AND WRISTS, spreads CENTRIPETALLY over 6–18 h, involves PALMS AND SOLES, SPARES THE FACE."),
   ("RMSF labs & treatment", "Thrombocytopenia, anaemia, mild hyponatraemia, transaminitis, normal white count with bands. Indirect immunofluorescence is the gold standard but rarely diagnostic before day 7 — TREAT BY DAY 5. DOXYCYCLINE FOR EVERYONE including children and pregnancy. Prophylaxis after a bite NOT recommended."),
   ("Primary vs secondary lesions", "Primary = epidermis and superficial dermis. Secondary = infiltrated into dermis or subcutaneous. Crust or scale means the EPIDERMIS is affected."),
 ]),
 ("pigmented", "Pigmented Skin Lesions", "#6b4f9e", "#e7e2f2", "#f2f0f8", "#543d7d", [
   ("Ephelides vs lentigines", "FRECKLES FADE WHEN THE SUN GOES; LENTIGINES DO NOT. That single fact is the whole differential."),
   ("Ephelides", "Autosomal dominant, MCR-1 variant → pheomelanin. 3–5 mm light brown symmetric macules. Sun protection + depigmenting agents + laser. NOT cryotherapy — lesions too small."),
   ("Lentigo simplex", "Uniformly black or brown, well circumscribed, under 5 mm. Sun-exposed AND protected skin. No treatment needed."),
   ("Solar lentigo", "90% of people by age 50. Irregular borders coalescing at sunburn sites. Associated with actinic keratosis, squamous and basal cell carcinoma, melanoma. Can become lichenoid keratoses."),
   ("PUVA lentigines", "Total treatments, male, fair skin, older age. Appear on BUTTOCKS AND GENITALIA as well as exposed sites."),
   ("Seborrheic keratosis", "Beige-to-black, velvety, look STUCK ON, 2–20 mm, older adults. Easily mistaken for neoplasms. Cryotherapy only if itchy or inflamed — and it recurs."),
   ("Dermatosis papulosa nigrans", "Identical to small seborrheic keratoses. Face and neck, African American / dark-skinned Asian / Polynesian, F > M. Genetic — hair follicle developmental defect. AVOID CRYOTHERAPY (post-inflammatory hyperpigmentation)."),
   ("Vitiligo", "T-cell destruction of melanocytes. Usually before 30; half before 20, a third before 12. White non-scaly macules with distinct margins, FLUORESCE under Wood's lamp in a DARK ROOM."),
   ("Segmental vs non-segmental", "Segmental = UNILATERAL, does not cross midline, block-like, unpredictable cycles. Non-segmental = symmetrical, prefers face, genitals, acral."),
   ("Vitiligo treatment", "Under 5% → topical steroid (atrophy, intraocular pressure) or calcineurin inhibitor (face/neck/children; cancer risk). Over 5% → NARROW BAND ULTRAVIOLET B first line, preferred over PUVA. Grafting ONLY for highly stable disease. Psychological intervention is part of management."),
   ("Congenital melanocytic naevus", "LARGER = HIGHER MELANOMA RISK. Head, neck or posterior midline → magnetic resonance imaging for NEUROCUTANEOUS MELANOSIS (seizures, hydrocephalus; poor prognosis)."),
   ("Naevus spilus", "Tan café-au-lait-like patch with scattered darker macules. RARELY progresses to melanoma. Observation + sun protection."),
   ("Common acquired naevus", "Under 6 mm, homogenous, sharply demarcated. Peaks in the THIRTIES then declines. VERY DARK BROWN OR BLACK ON LIGHT SKIN IS SUSPICIOUS."),
   ("Blue naevus", "Dermal spindle/epithelioid melanocytes. Women, twenties. Dorsal hands and feet, scalp, buttocks, sacrum. Common blue under 1 cm; cellular blue over 1 cm. Small = clinical, larger = biopsy."),
   ("Pigmented spindle cell (Reed)", "JET-BLACK papule under 7 mm, thirties, females, THIGH. Benign — but biopsy to confirm and EXCISE WITH NEGATIVE MARGINS."),
   ("Spitz naevus", "Solitary PINK/RED hairless dome-shaped. Growth phase then stable. SPARES palms, soles, mucosae. Resembles melanoma → biopsy or wide excision. Multiple → familial cancer syndrome."),
   ("Dysplastic naevus", "At least 5 mm, irregular indistinct borders, variable tan-to-brown, pebbly. Caucasians, family history. Over 100 by adolescence = the syndrome. MORE NAEVI = MORE MELANOMA RISK. Biopsy ALL changing lesions."),
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
    assert 'id="skin-layers"' not in s, "sections already added"

    # jump links
    anchor = ('      <a href="#counselling" style="color:#175341"><span class="dot" '
              'style="background:#1d6b53"></span>Counselling & Adherence</a>\n')
    assert s.count(anchor) == 1, "jump-link anchor not found"
    links = anchor + "".join(
        '      <a href="#%s" style="color:%s"><span class="dot" style="background:%s"></span>%s</a>\n'
        % (t[0], t[5], t[2], t[1]) for t in TOPICS)
    s = s.replace(anchor, links)

    # sections, before the footer
    foot = "  <footer>"
    assert s.count(foot) == 1, "footer not found"
    s = s.replace(foot, "".join(section(t) for t in TOPICS) + "\n" + foot)

    open(CRAM, "w", encoding="utf-8").write(s)

    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th"):
        o, c = len(re.findall(r"<%s[ >]" % tag, s)), s.count("</%s>" % tag)
        assert o == c, "%s: %d open, %d close" % (tag, o, c)
    ids = set(re.findall(r'id="([^"]+)"', s))
    dangling = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a not in ids]
    assert not dangling, "dangling jump links: %r" % dangling
    print("cram topics added: %d (%d rows)" % (len(TOPICS), sum(len(t[6]) for t in TOPICS)))
    print("tag balance and jump links verified")


if __name__ == "__main__":
    main()
