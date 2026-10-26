# -*- coding: utf-8 -*-
"""Arcade decks for Pharmacology I Exam 1, Lecture 2 (Dermatology Medications) and Lecture 3 (Principles of
Autonomic Nervous System Pharmacology), drafted 2026-10-26.

Imported by add_pharm_e1_arcade.py. Lecture 1 already has its three decks (pharm-antibacterials,
pharm-antivirals, pharm-antifungals, built by build_pharm_arcade.py); these nine fill Lectures 2 and 3.

Split, per [[arcade_content_policy]] (one deck per topic, about 20 atomic cards at most, all cards in a deck
confusable with each other): the homepage has one dermatology quiz and two ANS quizzes (cholinergic,
adrenergic), but both decks are far denser than 20 cards, so each is split into sub-topic decks the way the
Exam 2 and Exam 3 decks are:
    Lecture 2 (58 slides)  -> acne; vehicles + topical steroids + atopic dermatitis; topical anti-infectives
    Lecture 3 (124 slides) -> ANS organization + receptors; cholinergic agonists; antimuscarinics;
                              ganglionic + neuromuscular blockers; adrenergic agonists; adrenergic antagonists

Rules carried: atomic question -> short answer cards, deck facts from the VISIBLE slides only (speaker notes
do not count), no doses or strengths (Dr. Wood), US spelling, no bare abbreviations, never a citation inside
card text. Weighting follows Dr. McInnis: indications, patient education, adverse effects and
contraindications alongside mechanism.

Every card is written with C(deck, question, answer, slide(s), verify...) and every Match pair with
M(deck, term, tag, slide(s), verify...). The adder PROVES each one: every verify substring must be on the
cited slide's visible text (table cells included) or in that slide's PICTURE transcription below.

Deliberately NOT carried: every strength and percentage on the potency chart; the slide's
"trimethoprim/sulfacetamide (Bactrim)" (a misprint for sulfamethoxazole, so nothing turns on it); the
dicyclomine analog/nonanalog row of the antimuscarinic table (its column mapping is ambiguous); durations of
therapy (azole 2 to 3 weeks, exacerbation steroids 1 to 2 weeks); the acne type I to IV care-plan table
(a textbook table pasted as a picture, its regimens border on dosing).

Keyed to the SLIDE where a textbook differs (slides win on conflict): gastric parietal cells under M1 (slide 23;
textbooks put them at M3), azoles and allylamines "preventing cell wall" formation (slides 51, 53; truly the
ergosterol of the membrane), the ointment as "water in oil" (slide 8), halothane as the named malignant
hyperthermia trigger (slide 70). Questions are worded so no card's answer is ambiguous against the textbook
version either (bethanechol is asked as the choline ester without nicotinic activity, not the only
esterase-resistant agonist; the central nervous system card contrasts physostigmine with neostigmine only).

Fact-checked 2026-10-26 by one Sonnet reader against the extracted slide text and the pictures: 290 items,
11 confirmed problems (a compound answer, two unsupported words in stems, one incomplete answer, five Match tags
that also fitted another term in the deck, glycopyrronium duplicating glycopyrrolate), all fixed here.
"""
REG = []      # (kind "card"|"match", deck id, front, [(slide, [verify])])

L2, L3 = "L2", "L3"

ACNE, VEHI, DINF = "pharm-derm-acne", "pharm-derm-steroids", "pharm-derm-antiinfectives"
ANSP, CHAG, AMUS = "pharm-ans-principles", "pharm-ans-cholinergic-agonists", "pharm-ans-antimuscarinics"
NMBK, ADAG, ADAN = "pharm-ans-nm-blockers", "pharm-ans-adrenergic-agonists", "pharm-ans-adrenergic-antagonists"
LECTURE = {ACNE: L2, VEHI: L2, DINF: L2, ANSP: L3, CHAG: L3, AMUS: L3, NMBK: L3, ADAG: L3, ADAN: L3}


def _pairs(slide, verify):
    return [(slide, list(verify))] if isinstance(slide, int) else [(s, list(v)) for s, v in slide]


def C(deck, q, a, slide, verify=()):
    REG.append(("card", deck, q, _pairs(slide, verify)))
    return (q, a)


def M(deck, term, tag, slide, verify=()):
    REG.append(("match", deck, term, _pairs(slide, verify)))
    return (term, tag)


# Text read off picture-only (or picture-carrying) slides, transcribed after VIEWING each picture
# (2026-10-26; Vision OCR of the embedded images agreed). Only the slides a card cites are here.
PICTURE = {
    (L3, 10): ("Sympathetic vs. parasympathetic table. Sympathetic: sites of origin thoracic and lumbar region of "
               "the spinal cord (thoracolumbar); length of fibers short preganglionic long postganglionic; location "
               "of ganglia close to spinal cord; preganglionic fiber branching extensive; distribution wide; type of "
               "response diffuse. Parasympathetic: sites of origin brain and sacral area of spinal cord "
               "(craniosacral); length of fibers long preganglionic short postganglionic; location of ganglia within "
               "or near effector organs; preganglionic fiber branching minimal; distribution limited; type of "
               "response discrete."),
    (L3, 14): ("Autonomic and somatic efferent diagram. Sympathetic innervation of adrenal medulla: ganglionic "
               "transmitter acetylcholine at nicotinic receptor; epinephrine and norepinephrine released into the "
               "blood to adrenergic receptor. Sympathetic: ganglionic transmitter acetylcholine at nicotinic "
               "receptor; postganglionic neuroeffector transmitter norepinephrine at adrenergic receptor. "
               "Parasympathetic: ganglionic transmitter acetylcholine at nicotinic receptor; postganglionic "
               "neuroeffector transmitter acetylcholine at muscarinic receptor. Somatic: no ganglia; acetylcholine "
               "at nicotinic receptor on skeletal muscle."),
    (L3, 21): ("Synthesis of acetylcholine: transport of choline is inhibited by hemicholinium. Uptake into storage "
               "vesicles: acetylcholine is protected from degradation in the vesicle. Release of neurotransmitter: "
               "release is blocked by botulinum toxin; spider venom causes release of acetylcholine. Binding to the "
               "receptor: postsynaptic receptor is activated by binding of the neurotransmitter. Degradation of "
               "acetylcholine: acetylcholine is rapidly hydrolyzed by acetylcholinesterase in the synaptic cleft. "
               "Recycling of choline: choline is taken up by the neuron."),
    (L3, 41): ("Summary of cholinergic agonists. Bethanechol: used in treatment of urinary retention; binds "
               "preferentially at muscarinic receptors. Carbachol: produces miosis during ocular surgery; used "
               "topically to reduce intraocular pressure in open-angle or narrow-angle glaucoma, particularly in "
               "patients who have become tolerant to pilocarpine. Pilocarpine: reduces intraocular pressure in "
               "open-angle and narrow-angle glaucoma; binds preferentially at muscarinic receptors; uncharged, "
               "tertiary amine that can penetrate the CNS. Physostigmine: increases intestinal and bladder motility; "
               "reduces intraocular pressure in glaucoma; reverses CNS and cardiac effects of tricyclic "
               "antidepressants; reverses CNS effects of atropine; uncharged, tertiary amine that can penetrate the "
               "CNS. Neostigmine: prevents postoperative abdominal distention and urinary retention; used in "
               "treatment of myasthenia gravis; used as an antidote for tubocurarine; has long duration of action. "
               "Edrophonium: for diagnosis of myasthenia gravis; as antidote for tubocurarine; has short duration "
               "of action. Rivastigmine, galantamine, donepezil: used as first-line treatments for Alzheimer "
               "disease, though confers modest benefit; can be used with memantine (N-methyl-D-aspartate "
               "antagonist) with moderate to severe disease. Echothiophate: used in treatment of open-angle "
               "glaucoma; has long duration of action (1 week). Acetylcholine: has no therapeutic uses."),
    (L3, 73): ("Adrenergic neuron. Synthesis of norepinephrine: hydroxylation of tyrosine is the rate-limiting step. "
               "Uptake into storage vesicles: dopamine enters a vesicle and is converted to norepinephrine; "
               "transport into the vesicle is inhibited by reserpine. Release of neurotransmitter: influx of "
               "calcium causes fusion of the vesicle with the cell membrane (exocytosis); release is blocked by "
               "guanethidine and bretylium. Removal of norepinephrine: reuptake is inhibited by cocaine and "
               "imipramine. Metabolism: norepinephrine is methylated by COMT and oxidized by MAO."),
    (L3, 76): ("Alpha-2 receptors: activation of the receptor decreases production of cAMP, leading to an inhibition "
               "of further release of norepinephrine from the neuron. Alpha-1 receptors: activation of the receptor "
               "increases production of DAG and IP3, leading to an increase in intracellular calcium ions."),
    (L3, 78): ("Adrenoceptors. Alpha-1: vasoconstriction; increased peripheral resistance; increased blood pressure; "
               "mydriasis; increased closure of internal sphincter of the bladder. Alpha-2: inhibition of "
               "norepinephrine release; inhibition of acetylcholine release; inhibition of insulin release. "
               "Beta-1: tachycardia; increased lipolysis; increased myocardial contractility; increased release of "
               "renin. Beta-2: vasodilation; decreased peripheral resistance; bronchodilation; increased muscle and "
               "liver glycogenolysis; increased release of glucagon; relaxed uterine smooth muscle."),
}

FACE_ICON = '<circle cx="12" cy="12" r="9"/><circle cx="9" cy="10" r="1"/><circle cx="15" cy="10" r="1"/><circle cx="12" cy="15" r="1"/>'
TUBE_ICON = '<rect x="8" y="3" width="8" height="13" rx="2"/><path d="M10 16v5h4v-5"/>'
SHIELD_ICON = '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>'
NEURON_ICON = '<circle cx="12" cy="12" r="3"/><path d="M12 3v6M12 15v6M3 12h6M15 12h6"/>'
AGONIST_ICON = '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'
BLOCK_ICON = '<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/>'

DECKS = [
 # ======================================================================= Lecture 2: Dermatology Medications
 (ACNE, "Acne Medications", "accent1", FACE_ICON, [
  C(ACNE, "Which kind of therapy suits mild to moderate acne?", "Topical therapy.", 17, ["Mild-moderate: topical therapy"]),
  C(ACNE, "Which kind of therapy suits moderate to severe acne?", "Systemic therapy.", 17, ["Moderate-severe: systemic therapy"]),
  C(ACNE, "Which drug class causes pustular acne on the trunk two to six weeks after starting?", "Systemic corticosteroids.", 15,
    ["Systemic corticosteroids", "Pustular inflammation on the trunk", "2-6 weeks after initiation of therapy"]),
  C(ACNE, "What does benzoyl peroxide become after it penetrates the stratum corneum?", "Benzoic acid.", 21,
    ["penetrates stratum corneum unchanged and is then converted to benzoic acid"]),
  C(ACNE, "Which acne drug can bleach hair and clothes?", "Benzoyl peroxide.", 21, ["Benzoyl Peroxide", "can bleach hair, clothes"]),
  C(ACNE, "Why should tretinoin not be applied with benzoyl peroxide?", "Benzoyl peroxide inactivates tretinoin.", 24, ["Benzoyl peroxide inactivates tretinoin"]),
  C(ACNE, "Which acne drug can cause hypopigmentation?", "Azelaic acid.", 22, ["Azelaic Acid", "Hypopigmentation"]),
  C(ACNE, "Which hormone conversion is azelaic acid thought to inhibit?", "Testosterone to dihydrotestosterone.", 22,
    ["inhibiting conversion of testosterone to dihydrotestosterone"]),
  C(ACNE, "What is first-line therapy for noninflammatory, comedonal acne?", "Topical retinoids.", 23,
    ["First line therapy for noninflammatory (comedonal) acne"]),
  C(ACNE, "Why is tretinoin applied at night?", "It is photolabile.", 24, ["Tretinoin", "Photolabile (apply nightly)"]),
  C(ACNE, "Which topical retinoid is stable in sunlight and with benzoyl peroxide?", "Adapalene.", 25,
    ["Adapalene", "Stable in sunlight, stable with benzoyl peroxide"]),
  C(ACNE, "Which third-generation retinoid treats both acne and psoriasis?", "Tazarotene.", 25,
    ["Tazarotene", "Third generation retinoid used for acne and psoriasis"]),
  C(ACNE, "Which topical antibiotic is the preferred agent for acne?", "Clindamycin.", 26, ["Clindamycin", "preferred agent"]),
  C(ACNE, "Which acne drug is tied to the iPledge program?", "Isotretinoin.", 27, ["Isotretinoin", "iPledge"]),
  C(ACNE, "In whom is isotretinoin contraindicated?", "Patients who are pregnant or breastfeeding.", 27, ["CONTRAINDICATED in pregnancy/breastfeeding"]),
  C(ACNE, "Which mood change must be watched for during isotretinoin therapy?", "Developing depression.", 27,
    ["Monitor for signs of developing depression"]),
  C(ACNE, "Which systemic antibiotic class is most commonly used for acne?", "Tetracyclines.", 28, ["Tetracyclines", "Most commonly used"]),
  C(ACNE, "Who should not receive tetracyclines for acne?", "Children under 8 years and pregnant women.", 28,
    ["Contraindicated in children < 8 years and pregnant women"]),
  C(ACNE, "Which antiandrogen is used for acne?", "Spironolactone.", 29, ["Antiandrogens", "Spironolactone"]),
  C(ACNE, "Which systemic risk do intralesional steroids carry?", "Adrenal suppression from systemic absorption.", 30,
    ["Intralesional steroids", "Systemic absorption can occur", "adrenal suppression"]),
 ], [
  M(ACNE, "Benzoyl peroxide", "Converted to benzoic acid in the skin", 21, ["converted to benzoic acid"]),
  M(ACNE, "Azelaic acid", "Straight-chain dicarboxylic acid", 22, ["Straight chain dicarboxylic acid"]),
  M(ACNE, "Tretinoin", "Photolabile retinoid, applied nightly", 24, ["Tretinoin", "Photolabile (apply nightly)"]),
  M(ACNE, "Adapalene", "Light-stable, less irritating retinoid", 25, ["Stable in sunlight", "Tends to be less irritating"]),
  M(ACNE, "Tazarotene", "Third-generation retinoid for acne and psoriasis", 25, ["Third generation retinoid used for acne and psoriasis"]),
  M(ACNE, "Alitretinoin", "Retinoid for Kaposi sarcoma", 25, ["Alitretinoin", "Used in Kaposi sarcoma"]),
  M(ACNE, "Bexarotene", "Retinoid for T-cell lymphoma", 25, ["Bexarotene", "Used in T-cell lymphoma"]),
  M(ACNE, "Clindamycin", "Preferred topical acne antibiotic", 26, ["Clindamycin", "preferred agent"]),
  M(ACNE, "Isotretinoin", "Systemic retinoid under iPledge", 27, ["Systemic Retinoids", "Isotretinoin", "iPledge"]),
  M(ACNE, "Doxycycline", "Systemic tetracycline for acne", 28, ["Tetracyclines", "doxycycline"]),
  M(ACNE, "Spironolactone", "Antiandrogen for acne", 29, ["Antiandrogens", "Spironolactone"]),
  M(ACNE, "Salicylic acid", "Keratolytic with mild anti-inflammatory activity", 29, ["Salicylic acid", "Keratinolytic", "Mild anti-inflammatory"]),
 ]),
 (VEHI, "Vehicles, Topical Steroids &amp; Atopic Dermatitis", "accent2", TUBE_ICON, [
  C(VEHI, "Which body regions are most permeable to topical drugs?", "Scrotum, face, axilla and scalp.", 4,
    ["Scrotum, face, axilla, scalp are more permeable"]),
  C(VEHI, "Which dermatologic vehicle is the most drying?", "Tinctures.", 7, ["Tinctures (most drying)"]),
  C(VEHI, "Which dermatologic vehicle is the least drying?", "Ointments.", 7, ["Ointments (least drying)"]),
  C(VEHI, "What is the physical basis of a cream?", "An oil-in-water emulsion.", 8, ["Cream", "Oil in water emulsion"]),
  C(VEHI, "What is the physical basis of an ointment?", "A water-in-oil base.", 8, ["Ointment", "Water in Oil"]),
  C(VEHI, "Which vehicle spreads and removes easily with no greasy feel?", "Creams.", 8, ["Spreads and removes easily, no greasy feel"]),
  C(VEHI, "Rank ointment, cream and lotion by occlusiveness.", "Ointment, then cream, then lotion.", 38, ["occlusiveness of the preparation (ointment > cream > lotion)"]),
  C(VEHI, "What is the gold standard therapy for atopic dermatitis?", "Topical corticosteroids.", 37, ["Topical corticosteroids are gold standard"]),
  C(VEHI, "Which steroid potency suits the face, intertriginous areas and infants?", "Low potency.", 37,
    ["Low potency steroids", "Suitable for face, intertriginous areas, infants"]),
  C(VEHI, "Which steroid potency is used on the body?", "Medium potency.", 37, ["Medium potency", "Used for the body"]),
  C(VEHI, "Which steroid potency is warranted in an atopic dermatitis exacerbation?", "Medium-high potency.", 37,
    ["Exacerbations", "Medium-high potency corticosteroids warranted"]),
  C(VEHI, "Name the local adverse effects of topical steroids.", "Skin atrophy, acne, rosacea and allergic dermatitis.", 38,
    ["Local: skin atrophy, acne, rosacea, allergic dermatitis"]),
  C(VEHI, "Which systemic adverse effect of topical steroids affects children?", "Growth retardation.", 38, ["growth retardation (in children)"]),
  C(VEHI, "Which potency class is clobetasol propionate?", "Class 1, superpotent.", 41, ["Class 1: Superpotent", "Clobetasol propionate"]),
  C(VEHI, "Which potency class is hydrocortisone?", "Class 7, least potent.", 42, ["Class 7: Least Potent", "Hydrocortisone"]),
  C(VEHI, "How do tacrolimus and pimecrolimus work?", "They inhibit activation of T cells, mast cells and keratinocytes.", 43,
    ["tacrolimus ointment", "pimecrolimus cream", "inhibit activation of T cells, mast cells, and keratinocytes"]),
  C(VEHI, "Where do topical immunomodulators fall in atopic dermatitis therapy?", "Second line, after topical steroids.", 43,
    ["Second line agents after topical steroids"]),
  C(VEHI, "Which possible risk comes with topical immunomodulators?", "Cancer.", 43, ["Possible cancer risk"]),
  C(VEHI, "Which sun advice goes with topical immunomodulators?", "Use a high sun protection factor sunscreen.", 43, ["Use high SPF sunscreen"]),
  C(VEHI, "Why must a short oral corticosteroid course for atopic dermatitis be tapered?", "To prevent a flare-up.", 44,
    ["Oral corticosteroids", "Need tapering dose to prevent flare-up"]),
 ], [
  M(VEHI, "Tinctures", "Most drying vehicle", 7, ["Tinctures (most drying)"]),
  M(VEHI, "Ointments", "Least drying, water-in-oil vehicle", [(7, ["Ointments (least drying)"]), (8, ["Water in Oil"])]),
  M(VEHI, "Creams", "Oil-in-water emulsion", 8, ["Oil in water emulsion"]),
  M(VEHI, "Gels and foams", "Greaseless, non-staining vehicle", 8, ["Gel/Foam", "Non-staining, greaseless"]),
  M(VEHI, "Clobetasol propionate", "Class 1 superpotent steroid", 41, ["Class 1: Superpotent", "Clobetasol propionate"]),
  M(VEHI, "Betamethasone dipropionate ointment", "Class 1 superpotent steroid", 41, ["Class 1: Superpotent", "Betamethasone dipropionate 0.05% ointment"]),
  M(VEHI, "Mometasone furoate ointment", "Class 3 upper mid-strength steroid", 41, ["Class 3: Upper mid-strength", "Mometasone furoate 0.1% ointment"]),
  M(VEHI, "Alclometasone dipropionate", "Class 6 mild steroid", 42, ["Class 6: Mild", "Alclometasone dipropionate"]),
  M(VEHI, "Hydrocortisone", "Class 7 least potent steroid", 42, ["Class 7: Least Potent", "Hydrocortisone"]),
  M(VEHI, "Tacrolimus", "Topical immunomodulator ointment", 43, ["Topical Immunomodulators", "tacrolimus ointment"]),
  M(VEHI, "Pimecrolimus", "Topical immunomodulator cream", 43, ["Topical Immunomodulators", "pimecrolimus cream"]),
  M(VEHI, "Topical corticosteroids", "Gold standard for atopic dermatitis", 37, ["Topical corticosteroids are gold standard"]),
 ]),
 (DINF, "Topical Antibiotics, Antifungals &amp; Antivirals", "accent3", SHIELD_ICON, [
  C(DINF, "How does bacitracin work?", "It prevents cell wall synthesis.", 46, ["Bacitracin", "prevents cell wall synthesis"]),
  C(DINF, "Which topical antibiotic has no systemic toxicity?", "Bacitracin.", 46, ["Bacitracin", "No systemic toxicity"]),
  C(DINF, "How does mupirocin work?", "It binds bacterial transfer ribonucleic acid, preventing protein synthesis.", 47,
    ["Binds to bacterial t-RNA preventing protein synthesis"]),
  C(DINF, "Which topical antibiotic eliminates nasal carriage of Staphylococcus aureus?", "Mupirocin.", 47,
    ["Mupirocin", "Used to eliminate nasal carriage of S. aureus"]),
  C(DINF, "Which resistant organism is mupirocin especially active against?", "Methicillin-resistant Staphylococcus aureus.", 47,
    ["most gram positive aerobes (esp. MRSA)"]),
  C(DINF, "How does polymyxin B work?", "It interrupts the cytoplasmic membrane.", 48, ["Polymyxin B", "interrupts cytoplasmic membrane"]),
  C(DINF, "Which organisms does topical polymyxin B cover?", "Gram-negative organisms such as Pseudomonas and Klebsiella.", 48,
    ["Effective against gram negative organisms", "Pseudomonas", "Klebsiella"]),
  C(DINF, "Why avoid high-dose polymyxin B on open wounds?", "Risk of neurotoxicity and nephrotoxicity.", 48,
    ["Avoid using on open wounds/denuded skin in high doses", "risk for neuro/nephrotoxicity"]),
  C(DINF, "Which topical aminoglycoside frequently causes sensitization?", "Neomycin.", 49, ["Neomycin frequently causes sensitization"]),
  C(DINF, "Name the topical azole antifungals.", "Clotrimazole, ketoconazole, miconazole and sertaconazole.", 51,
    ["clotrimazole, ketoconazole, miconazole, sertaconazole"]),
  C(DINF, "How do azole antifungals work?", "They inhibit fungal cytochrome P450, preventing cell wall formation.", 51,
    ["inhibits fungal P450 preventing cell wall formation"]),
  C(DINF, "Why are topical azoles sometimes combined with corticosteroids?", "For more rapid symptom relief.", 51,
    ["Sometimes combined with corticosteroids (more rapid symptom relief)"]),
  C(DINF, "Which antifungal is marketed as a nail lacquer for onychomycosis?", "Ciclopirox.", 52, ["Ciclopirox", "nail lacquer for onychomycosis"]),
  C(DINF, "How do allylamines such as terbinafine work?", "They inhibit ergosterol production, preventing cell wall synthesis.", 53,
    ["Naftifine and terbinafine", "inhibits production of ergosterol and prevents cell wall synthesis"]),
  C(DINF, "Which topical antifungal has no Candida activity?", "Tolnaftate.", 54, ["Tolnaftate", "No candida activity"]),
  C(DINF, "Which antifungal treats cutaneous and mucosal candidal infections?", "Nystatin.", 54,
    ["Nystatin - used for candidal infections (cutaneous and mucosal)"]),
  C(DINF, "What are topical acyclovir and penciclovir used for?", "Recurrent orolabial herpes simplex infection.", 56,
    ["Acyclovir (Zovirax), penciclovir (Denavir)", "Used for recurrent orolabial herpes simplex infection"]),
  C(DINF, "How does imiquimod work?", "It stimulates release of interferon-alpha, tumor necrosis factor-alpha and interleukins.", 57,
    ["immunomodulator", "stimulates peripheral mononuclear cells to release interferon-", "macrophages to produce TNF-", "and interleukins"]),
  C(DINF, "Name the indications for imiquimod.", "External and perianal warts, actinic keratoses and basal cell carcinoma.", 57,
    ["external and perianal warts, actinic keratoses, basal cell carcinoma"]),
  C(DINF, "What does the degree of imiquimod inflammation parallel?", "Its efficacy.", 57, ["degree of inflammation parallels efficacy"]),
 ], [
  M(DINF, "Bacitracin", "Peptide antibiotic, blocks cell wall synthesis", 46, ["Peptide antibiotic", "prevents cell wall synthesis"]),
  M(DINF, "Mupirocin", "Clears nasal Staphylococcus aureus carriage", 47, ["Used to eliminate nasal carriage of S. aureus"]),
  M(DINF, "Polymyxin B", "Gram-negative peptide, disrupts the membrane", 48, ["Peptide antibiotic", "interrupts cytoplasmic membrane", "gram negative"]),
  M(DINF, "Neomycin", "Aminoglycoside that often sensitizes", 49, ["Neomycin and gentamicin", "Neomycin frequently causes sensitization"]),
  M(DINF, "Clotrimazole", "Azole, inhibits fungal cytochrome P450", 51, ["clotrimazole", "inhibits fungal P450"]),
  M(DINF, "Ciclopirox", "Nail lacquer for onychomycosis", 52, ["Ciclopirox", "nail lacquer for onychomycosis"]),
  M(DINF, "Terbinafine", "Allylamine, inhibits ergosterol production", 53, ["Allylamines", "terbinafine", "inhibits production of ergosterol"]),
  M(DINF, "Tolnaftate", "Antifungal with no Candida activity", 54, ["Tolnaftate", "No candida activity"]),
  M(DINF, "Nystatin", "Candidal infections, no oral absorption", 54, ["Nystatin", "candidal infections", "No oral absorption"]),
  M(DINF, "Acyclovir", "Guanine analog for orolabial herpes", 56, ["Acyclovir", "Synthetic guanine analogs", "orolabial herpes"]),
  M(DINF, "Penciclovir", "Guanine analog for orolabial herpes", 56, ["penciclovir", "Synthetic guanine analogs", "orolabial herpes"]),
  M(DINF, "Imiquimod", "Immunomodulator for warts and actinic keratoses", 57, ["immunomodulator", "warts, actinic keratoses"]),
 ]),

 # ======================================================================= Lecture 3: ANS Pharmacology
 (ANSP, "ANS (Autonomic Nervous System) Organization &amp; Receptors", "accent4", NEURON_ICON, [
  C(ANSP, "Where does sympathetic outflow originate?", "The thoracic and lumbar spinal cord.", 10,
    ["Sympathetic: sites of origin thoracic and lumbar region of the spinal cord (thoracolumbar)"]),
  C(ANSP, "Where does parasympathetic outflow originate?", "The brain and the sacral spinal cord.", 10,
    ["Parasympathetic: sites of origin brain and sacral area of spinal cord (craniosacral)"]),
  C(ANSP, "Which fiber lengths does the sympathetic system have?", "Short preganglionic and long postganglionic fibers.", 10,
    ["thoracolumbar); length of fibers short preganglionic long postganglionic"]),
  C(ANSP, "Which fiber lengths does the parasympathetic system have?", "Long preganglionic and short postganglionic fibers.", 10,
    ["craniosacral); length of fibers long preganglionic short postganglionic"]),
  C(ANSP, "Which transmitter acts at every autonomic ganglion?", "Acetylcholine, at nicotinic receptors.", 14,
    ["Sympathetic: ganglionic transmitter acetylcholine at nicotinic receptor", "Parasympathetic: ganglionic transmitter acetylcholine at nicotinic receptor"]),
  C(ANSP, "Which transmitter do sympathetic postganglionic neurons release?", "Norepinephrine, at adrenergic receptors.", 14,
    ["postganglionic neuroeffector transmitter norepinephrine at adrenergic receptor"]),
  C(ANSP, "Which transmitter do parasympathetic postganglionic neurons release?", "Acetylcholine, at muscarinic receptors.", 14,
    ["postganglionic neuroeffector transmitter acetylcholine at muscarinic receptor"]),
  C(ANSP, "Which toxin blocks acetylcholine release?", "Botulinum toxin.", 21, ["release is blocked by botulinum toxin"]),
  C(ANSP, "Which muscarinic receptor is found on gastric parietal cells?", "The M1 receptor.", 23, ["M1: Neurons, gastric parietal cells"]),
  C(ANSP, "Which muscarinic receptor is found on cardiac cells?", "The M2 receptor.", 23, ["M2: Neurons, cardiac cells, smooth muscle"]),
  C(ANSP, "Which muscarinic receptor is found on the bladder and exocrine glands?", "The M3 receptor.", 23, ["M3: Neurons, bladder, exocrine glands"]),
  C(ANSP, "What kind of receptor is the nicotinic receptor?", "A ligand-gated ion channel.", 24, ["Functions as ligand-gated ion channel"]),
  C(ANSP, "Where are alpha-1 receptors located?", "On the postsynaptic membrane of the effector organ.", 76,
    ["Present on postsynaptic membrane of effector organ"]),
  C(ANSP, "Where are alpha-2 receptors located?", "On presynaptic nerve endings.", 76, ["Present on presynaptic nerve endings and other cells"]),
  C(ANSP, "What does alpha-2 receptor activation do to norepinephrine release?", "It inhibits further release.", 76,
    ["inhibition of further release of norepinephrine from the neuron"]),
  C(ANSP, "Stimulation of which adrenoceptor increases renin release?", "Beta-1.", 78, ["increased myocardial contractility; increased release of renin"]),
  C(ANSP, "Which adrenoceptor mediates bronchodilation?", "Beta-2.", 78, ["decreased peripheral resistance; bronchodilation"]),
  C(ANSP, "What is the rank order of agonist potency at beta receptors?", "Isoproterenol, then epinephrine, then norepinephrine.", 77,
    ["Isoproterenol > Epinephrine > Norepinephrine"]),
  C(ANSP, "Which enzyme inactivates catecholamines postsynaptically?", "Catechol-O-methyltransferase.", 79,
    ["Catechol-O-methyltransferase (COMT) postsynaptically"]),
  C(ANSP, "Which enzyme inactivates catecholamines inside the neuron?", "Monoamine oxidase.", 79, ["Monoamine oxidase (MAO) intraneuronally"]),
 ], [
  M(ANSP, "Sympathetic division", "Thoracolumbar outflow", 10, ["(thoracolumbar)"]),
  M(ANSP, "Parasympathetic division", "Craniosacral outflow", 10, ["(craniosacral)"]),
  M(ANSP, "Enteric nervous system", "Brain of the gut", 12, ["Enteric Neurons", "brain of the gut"]),
  M(ANSP, "M1 receptor", "Neurons and gastric parietal cells", 23, ["M1: Neurons, gastric parietal cells"]),
  M(ANSP, "M2 receptor", "Neurons, cardiac cells, smooth muscle", 23, ["M2: Neurons, cardiac cells, smooth muscle"]),
  M(ANSP, "M3 receptor", "Bladder and exocrine glands", 23, ["M3: Neurons, bladder, exocrine glands, smooth muscle"]),
  M(ANSP, "Nicotinic receptor", "Five-subunit ligand-gated ion channel", 24, ["Composed of five subunits", "Functions as ligand-gated ion channel"]),
  M(ANSP, "Alpha-1 receptor", "Vasoconstriction and mydriasis", 78, ["Alpha-1: vasoconstriction", "mydriasis"]),
  M(ANSP, "Alpha-2 receptor", "Inhibits norepinephrine release", 78, ["Alpha-2: inhibition of norepinephrine release"]),
  M(ANSP, "Beta-1 receptor", "Tachycardia and increased renin release", 78, ["Beta-1: tachycardia", "increased release of renin"]),
  M(ANSP, "Beta-2 receptor", "Bronchodilation and vasodilation", 78, ["Beta-2: vasodilation", "bronchodilation"]),
  M(ANSP, "Catechol-O-methyltransferase", "Postsynaptic catecholamine inactivation", 79, ["Catechol-O-methyltransferase (COMT) postsynaptically"]),
  M(ANSP, "Monoamine oxidase", "Intraneuronal catecholamine inactivation", 79, ["Monoamine oxidase (MAO) intraneuronally"]),
 ]),
 (CHAG, "Cholinergic Agonists", "accent1", AGONIST_ICON, [
  C(CHAG, "Which pupil effect is muscarinic?", "Miosis.", 28, ["Muscarinic Effects", "M - miosis"]),
  C(CHAG, "Which pupil effect is nicotinic?", "Mydriasis.", 29, ["Nicotinic Effects", "M - mydriasis"]),
  C(CHAG, "Which heart rate effect is muscarinic?", "Bradycardia.", 28, ["Muscarinic Effects", "B - bradycardia"]),
  C(CHAG, "Which heart rate effect is nicotinic?", "Tachycardia.", 29, ["Nicotinic Effects", "T - tachycardia"]),
  C(CHAG, "Which choline ester lacks nicotinic activity?", "Bethanechol.",
    [(26, ["Choline esters", "Acetylcholine", "Carbachol (synthetic)", "Bethanechol (synthetic)"]), (30, ["Lacks nicotinic activity"])]),
  C(CHAG, "What is bethanechol used for?", "Postpartum or postoperative atonic bladder.", 30, ["Stimulate postpartum or postoperative atonic bladder"]),
  C(CHAG, "Which direct agonist releases epinephrine from the adrenal medulla?", "Carbachol.", 32,
    ["Carbachol", "Causes release of epinephrine from adrenal medulla by nicotinic actions"]),
  C(CHAG, "What is carbachol used for clinically?", "Lowering intraocular pressure in glaucoma.", 32, ["Clinical uses: decrease intraocular pressure (glaucoma)"]),
  C(CHAG, "Which cholinergic agonist stimulates salivation in xerostomia?", "Pilocarpine.", 33,
    ["Pilocarpine", "May be used to stimulate salivation", "xerostomia (dry mouth)"]),
  C(CHAG, "How do indirect-acting cholinergic agents work?", "They inhibit acetylcholinesterase.", 34,
    ["increase activity of acetylcholine by inhibiting activity of acetylcholinesterase"]),
  C(CHAG, "Which short-acting acetylcholinesterase inhibitor diagnoses myasthenia gravis?", "Edrophonium.", 35,
    ["Edrophonium", "Prototype, short-acting AChE inhibitor", "Diagnosing myasthenia gravis"]),
  C(CHAG, "Which acetylcholinesterase inhibitor treats anticholinergic overdose?", "Physostigmine.", 36,
    ["Physostigmine", "Treatment of overdoses of anticholinergic drugs"]),
  C(CHAG, "Which enters the central nervous system, physostigmine or neostigmine?", "Physostigmine.",
    [(38, ["Neostigmine", "does not enter CNS"]), (41, ["Physostigmine: increases intestinal", "tertiary amine that can penetrate the CNS. Neostigmine"])]),
  C(CHAG, "Which drug is used for chronic management of myasthenia gravis?", "Pyridostigmine.", 39,
    ["Pyridostigmine", "Chronic management of myasthenia gravis"]),
  C(CHAG, "Name the acetylcholinesterase inhibitors used in Alzheimer disease.", "Donepezil, rivastigmine and galantamine.", 40,
    ["Alzheimer Agents", "Donepezil", "Rivastigmine", "Galantamine"]),
  C(CHAG, "Which adverse effect do the Alzheimer agents cause?", "Gastrointestinal distress.", 40, ["Adverse effects GI distress"]),
  C(CHAG, "Which drug reactivates inhibited acetylcholinesterase?", "Pralidoxime.", 42, ["Pralidoxime (Protopam) can reactivate inhibited AChE"]),
  C(CHAG, "Which inhibitors can pralidoxime not overcome?", "Reversible inhibitors such as physostigmine.", 42,
    ["Cannot overcome reversible AChE inhibitors such as physostigmine"]),
  C(CHAG, "What can physostigmine cause at high doses?", "Convulsions.", 37, ["Convulsions at high doses"]),
  C(CHAG, "Which cholinergic agonist has no therapeutic uses?", "Acetylcholine.", 41, ["Acetylcholine: has no therapeutic uses"]),
 ], [
  M(CHAG, "Bethanechol", "Muscarinic agonist for urinary retention", 41, ["Bethanechol: used in treatment of urinary retention; binds preferentially at muscarinic receptors"]),
  M(CHAG, "Carbachol", "Miosis during ocular surgery", 41, ["Carbachol: produces miosis during ocular surgery"]),
  M(CHAG, "Pilocarpine", "Natural alkaloid that lowers intraocular pressure", [(26, ["Naturally occurring alkaloids", "Pilocarpine"]), (33, ["Decreases intraocular pressure"])]),
  M(CHAG, "Edrophonium", "Short-acting test for myasthenia gravis", 35, ["Prototype, short-acting AChE inhibitor", "Diagnosing myasthenia gravis"]),
  M(CHAG, "Physostigmine", "Reverses anticholinergic overdose", 36, ["Physostigmine", "Treatment of overdoses of anticholinergic drugs"]),
  M(CHAG, "Neostigmine", "Long-acting antidote for tubocurarine", 41, ["used as an antidote for tubocurarine; has long duration of action"]),
  M(CHAG, "Pyridostigmine", "Chronic myasthenia gravis therapy", 39, ["Pyridostigmine", "Chronic management of myasthenia gravis"]),
  M(CHAG, "Donepezil", "Alzheimer acetylcholinesterase inhibitor", 40, ["Alzheimer Agents", "Donepezil"]),
  M(CHAG, "Echothiophate", "Week-long agent for open-angle glaucoma", 41, ["Echothiophate: used in treatment of open-angle glaucoma; has long duration of action (1 week)"]),
  M(CHAG, "Pralidoxime", "Reactivates inhibited acetylcholinesterase", 42, ["Pralidoxime (Protopam) can reactivate inhibited AChE"]),
  M(CHAG, "Acetylcholine", "No therapeutic uses", 41, ["Acetylcholine: has no therapeutic uses"]),
  M(CHAG, "Hemicholinium", "Inhibits choline transport", 21, ["transport of choline is inhibited by hemicholinium"]),
 ]),
 (AMUS, "Antimuscarinic Agents", "accent2", BLOCK_ICON, [
  C(AMUS, "Name the three main classes of cholinergic antagonists.", "Antimuscarinics, ganglionic blockers and neuromuscular blocking agents.", 44,
    ["Three main classes of agents", "Antimuscarinic agents", "Ganglionic blockers", "Neuromuscular blocking agents"]),
  C(AMUS, "Do antimuscarinic agents block nicotinic receptors?", "No, they do not block nicotinic receptors.", 46, ["Do not block nicotinic receptors"]),
  C(AMUS, "Name three plants atropine is extracted from.", "Deadly nightshade, Jimson weed and mandrake.", 48,
    ["Extracted from deadly nightshade (Atropa belladonna), Jimson weed (Datura stramonium), mandrake (Mandragora officinarum)"]),
  C(AMUS, "How does atropine act at the muscarinic receptor?", "It binds competitively and prevents acetylcholine binding.", 48,
    ["Binds competitively and prevents ACh binding"]),
  C(AMUS, "What does atropine do to the eye?", "Persistent mydriasis and cycloplegia.", 49, ["causes persistent mydriasis (dilation) and cycloplegia"]),
  C(AMUS, "Why is atropine given during a code blue?", "To treat bradycardia.", 49, ["Code Blues", "to treat bradycardia"]),
  C(AMUS, "What does atropine do to heart rate at higher doses?", "It causes tachycardia.", 49, ["Tachycardia at higher doses"]),
  C(AMUS, "Which poisonings is atropine an antidote for?", "Cholinesterase inhibitor insecticides and some mushroom poisonings.", 51,
    ["Antidote for cholinergic agonists", "cholinesterase inhibitor insecticides and some types of mushroom poisoning"]),
  C(AMUS, "Which anticholinergic effect is 'hot as Hades'?", "Hyperthermia.", 50, ["Hot as Hades Hyperthermia"]),
  C(AMUS, "Which anticholinergic effect is 'red as a beet'?", "Cutaneous flushing.", 50, ["Red as a beet Cutaneous flushing/redness"]),
  C(AMUS, "Which anticholinergic effect is 'blind as a bat'?", "Mydriasis and blurry vision.", 50, ["Blind as a bat Mydriasis, blurry vision"]),
  C(AMUS, "Which anticholinergic effects are 'mad as a hatter'?", "Sedation, anxiety, hallucinations and seizures.", 50,
    ["Mad as a hatter Sedation, anxiety, hallucinations, seizures"]),
  C(AMUS, "Which antimuscarinic prevents motion sickness?", "Scopolamine.", 54, ["Prevention of motion sickness (Transderm Scop)"]),
  C(AMUS, "How does scopolamine differ from atropine?", "It has greater central nervous system action at therapeutic doses.", 53,
    ["Peripheral effects similar to atropine", "Greater action on CNS at therapeutic doses"]),
  C(AMUS, "What should a patient do after placing a scopolamine patch?", "Wash hands thoroughly, because touching the eye afterward blurs vision.", 54,
    ["Instruct patients to wash hands thoroughly after placing patch", "Will cause blurred vision if touch eye after touching patch"]),
  C(AMUS, "Which inhaled antimuscarinics treat bronchospasm in chronic obstructive pulmonary disease?", "Ipratropium, tiotropium and glycopyrrolate.", 55,
    ["Ipratropium (Atrovent)", "Tiotropium (Spiriva)", "Glycopyrrolate (Robinul, Seebri Neohaler)",
     "Inhaled bronchodilators for maintenance treatment of bronchospasm associated with chronic obstructive pulmonary disease"]),
  C(AMUS, "Which antimuscarinic also reduces excessive drooling in cerebral palsy?", "Glycopyrrolate.", 55,
    ["Glycopyrrolate (Robinul) solution also used to", "Reduce excessive drooling caused by medical conditions such as cerebral palsy"]),
  C(AMUS, "Which active isomer of atropine relaxes the gastrointestinal tract and bladder?", "Hyoscyamine.", 51,
    ["Active isomer (hyoscyamine) used to relax GI tract and bladder"]),
  C(AMUS, "Which older bladder antimuscarinics cause confusion?", "Oxybutynin and tolterodine.", 56,
    ["Older agents (oxybutynin, tolterodine)", "Confusion"]),
  C(AMUS, "Why do newer bladder antimuscarinics have fewer central effects?", "They are designed not to cross the blood-brain barrier.", 56,
    ["Less CNS effects due to designed not to cross blood-brain barrier"]),
 ], [
  M(AMUS, "Atropine", "Antidote for cholinesterase inhibitor insecticides", 51, ["Antidote for cholinergic agonists", "overdoses of cholinesterase inhibitor insecticides"]),
  M(AMUS, "Scopolamine", "Transdermal patch for motion sickness", 54, ["Prevention of motion sickness (Transderm Scop)"]),
  M(AMUS, "Ipratropium", "Inhaled bronchodilator for chronic obstructive pulmonary disease", 55,
    ["Ipratropium (Atrovent)", "Inhaled bronchodilators", "chronic obstructive pulmonary disease"]),
  M(AMUS, "Tiotropium", "Inhaled bronchodilator for chronic obstructive pulmonary disease", 55,
    ["Tiotropium (Spiriva)", "Inhaled bronchodilators", "chronic obstructive pulmonary disease"]),
  M(AMUS, "Glycopyrrolate", "Inhaled bronchodilator for chronic obstructive pulmonary disease", 55,
    ["Glycopyrrolate (Robinul, Seebri Neohaler)", "Inhaled bronchodilators", "chronic obstructive pulmonary disease"]),
  M(AMUS, "Hyoscyamine", "Active atropine isomer, gut antispasmodic", 49, ["GI: Used as antispasmodic", "Active isomer hyoscyamine"]),
  M(AMUS, "Oxybutynin", "Older bladder agent, more confusion", 56, ["Older agents (oxybutynin, tolterodine)", "Confusion"]),
  M(AMUS, "Tolterodine", "Older bladder agent, more confusion", 56, ["Older agents (oxybutynin, tolterodine)", "Confusion"]),
  M(AMUS, "Hot as Hades", "Hyperthermia", 50, ["Hot as Hades Hyperthermia"]),
  M(AMUS, "Dry as a bone", "Decreased mucous membrane secretions", 50, ["Dry as a bone Decrease mucous membrane secretions"]),
  M(AMUS, "Heart runs alone", "Tachycardia", 50, ["Heart runs alone Tachycardia"]),
  M(AMUS, "Mad as a hatter", "Sedation, hallucinations, seizures", 50, ["Mad as a hatter Sedation, anxiety, hallucinations, seizures"]),
 ]),
 (NMBK, "Ganglionic &amp; Neuromuscular Blockers", "accent3", BLOCK_ICON, [
  C(NMBK, "What is the predominant sympathetic effect of ganglionic blockade?", "Vasodilation.", 58, ["Predominate sympathetic effect is vasodilation"]),
  C(NMBK, "Name the predominant parasympathetic effects of ganglionic blockade.", "Bladder and gut atony, cycloplegia, xerostomia and tachycardia.", 58,
    ["Predominate parasympathetic effects are atony of bladder and GI tract, cycloplegia, xerostomia, and tachycardia"]),
  C(NMBK, "Which ganglionic agent is not a nondepolarizing competitive antagonist?", "Nicotine.", 58,
    ["All agents except nicotine are nondepolarizing, competitive antagonists"]),
  C(NMBK, "What does nicotine do to autonomic ganglia?", "It first stimulates, then paralyzes them.", 59,
    ["Depolarizes autonomic ganglia", "Initially resulting in stimulation, then paralysis of all ganglia"]),
  C(NMBK, "Where do neuromuscular blocking drugs act?", "Nicotinic receptors on the skeletal muscle endplate.", 61,
    ["nicotinic receptors on neuromuscular endplate of skeletal muscle"]),
  C(NMBK, "Name the nondepolarizing blockers that replaced tubocurarine.", "Pancuronium, atracurium, cisatracurium, vecuronium and rocuronium.",
    [(62, ["Tubocurarine purified form", "Replaced by agents with fewer side effects"]), (63, ["Pancuronium", "Atracurium", "cisatracurium", "Vecuronium", "Rocuronium"])]),
  C(NMBK, "Why did cisatracurium replace atracurium?", "It has fewer adverse effects.", 63,
    ["Atracurium replaced by its isomer, cisatracurium (Nimbex) due to fewer adverse effects"]),
  C(NMBK, "How can a nondepolarizing blockade be reversed?", "With cholinesterase inhibitors such as neostigmine.", 64,
    ["Cholinesterase inhibitors such as neostigmine, pyridostigmine, and edrophonium may be given to reverse blockade"]),
  C(NMBK, "Which muscles do nondepolarizing blockers paralyze first?", "Small, rapidly contracting muscles of the face and eye.", 65,
    ["Small, rapidly contracting muscles of face and eye are most susceptible and paralyzed first"]),
  C(NMBK, "Which muscle do nondepolarizing blockers paralyze last?", "The diaphragm.", 65, ["Intercostals Diaphragm Muscles recover in reverse manner"]),
  C(NMBK, "Which nondepolarizing blocker can release histamine and lower blood pressure?", "Atracurium.", 65, ["atracurium) release histamine and can produce fall in BP"]),
  C(NMBK, "What is the only depolarizing neuromuscular blocker available?", "Succinylcholine.", 66, ["Succinylcholine only depolarizing agent available"]),
  C(NMBK, "Why does succinylcholine suit rapid sequence intubation?", "Its rapid onset and short duration of action.", 66,
    ["rapid onset and short duration of action", "rapid sequence intubation"]),
  C(NMBK, "Which enzyme breaks down succinylcholine?", "Plasma pseudocholinesterase.", 69, ["rapidly broken down by plasma pseudocholinesterase"]),
  C(NMBK, "What causes prolonged paralysis with succinylcholine?", "Genetically low or absent pseudocholinesterase.", 69,
    ["Genetic variants in which pseudocholinesterase levels are low or absent leads to prolonged paralysis"]),
  C(NMBK, "What helps prevent the fasciculations of succinylcholine?", "A small prior dose of a nondepolarizing blocker.", 69,
    ["Administering small dose of nondepolarizing neuromuscular blocker prior to succinylcholine helps decrease or prevent fasciculations"]),
  C(NMBK, "Which anesthetic given with succinylcholine can trigger malignant hyperthermia?", "Halothane.", 70,
    ["Administration with halothane occasionally causes malignant hyperthermia"]),
  C(NMBK, "Which drug treats malignant hyperthermia?", "Dantrolene.", 70, ["administering dantrolene (Dantrium)"]),
  C(NMBK, "How does dantrolene work?", "It blocks calcium release from the sarcoplasmic reticulum.", 70,
    ["blocks release of Ca++ from sarcoplasmic reticulum"]),
  C(NMBK, "Which electrolyte disturbance can succinylcholine cause?", "Hyperkalemia.", 70, ["Hyperkalemia", "Increases K+ release from intracellular stores"]),
 ], [
  M(NMBK, "Nicotine", "Depolarizing ganglionic agent", [(58, ["All agents except nicotine are nondepolarizing"]), (59, ["Depolarizes autonomic ganglia"])]),
  M(NMBK, "Tubocurarine", "Purified form of curare", 62, ["Tubocurarine purified form"]),
  M(NMBK, "Ganglionic blockers", "Block entire autonomic output at nicotinic receptors", 58, ["Block entire output of ANS at nicotinic receptor"]),
  M(NMBK, "Phase I block", "Sodium channel opening and depolarization", 67, ["Phase I: Opens Na+ channel which results in depolarization"]),
  M(NMBK, "Phase II block", "Resistance to further depolarization", 67, ["Phase II: Resistance to further depolarizations as a result of continued binding"]),
  M(NMBK, "Malignant hyperthermia", "Rigidity, acidosis, tachycardia, hyperpyrexia", 70,
    ["muscular rigidity, metabolic acidosis, tachycardia, and hyperpyrexia"]),
  M(NMBK, "Atracurium", "Releases histamine, lowering blood pressure", 65, ["atracurium) release histamine and can produce fall in BP"]),
  M(NMBK, "Cisatracurium", "Atracurium isomer with fewer adverse effects", 63, ["replaced by its isomer, cisatracurium (Nimbex) due to fewer adverse effects"]),
  M(NMBK, "Succinylcholine", "Only depolarizing neuromuscular blocker", 66, ["Succinylcholine only depolarizing agent available"]),
  M(NMBK, "Pseudocholinesterase", "Plasma enzyme that degrades succinylcholine", 69, ["rapidly broken down by plasma pseudocholinesterase"]),
  M(NMBK, "Dantrolene", "Treats malignant hyperthermia", 70, ["Treated by rapidly cooling patient and administering dantrolene"]),
  M(NMBK, "Halothane", "Malignant hyperthermia trigger with succinylcholine", 70, ["Administration with halothane occasionally causes malignant hyperthermia"]),
 ]),
 (ADAG, "Adrenergic Agonists", "accent4", AGONIST_ICON, [
  C(ADAG, "Name the four catecholamines.", "Epinephrine, norepinephrine, isoproterenol and dopamine.", 79,
    ["Catecholamines Epinephrine, norepinephrine, isoproterenol, dopamine"]),
  C(ADAG, "Name the mixed-action adrenergic agonists.", "Ephedrine and pseudoephedrine.", 103, ["Mixed-action Adrenergic Agonists", "Ephedrine", "Pseudoephedrine"]),
  C(ADAG, "Name the indirect-acting adrenergic agonists.", "Amphetamine, tyramine and cocaine.", 99,
    ["Indirect-acting Adrenergic Agonists", "Amphetamine", "Tyramine", "Cocaine"]),
  C(ADAG, "Which receptor effect predominates at low epinephrine doses?", "Beta effects, giving vasodilation.", 83, ["Low doses: β effects (vasodilation) predominates"]),
  C(ADAG, "Which receptor effect predominates at high epinephrine doses?", "Alpha effects, giving vasoconstriction.", 83, ["High doses: α effects (vasoconstriction) predominates"]),
  C(ADAG, "Which type of shock is epinephrine used for?", "Anaphylactic shock.", 85, ["Anaphylactic shock"]),
  C(ADAG, "Why is epinephrine added to local anesthetic solutions?", "It vasoconstricts the injection site, prolonging anesthesia.", 85,
    ["Greatly increases duration of local anesthesia", "Produces vasoconstriction at site of injection"]),
  C(ADAG, "Why is oral epinephrine ineffective?", "Intestinal enzymes inactivate it.", 86, ["Oral ineffective due to inactivated by intestinal enzymes"]),
  C(ADAG, "What happens when epinephrine is given with a beta blocker?", "Unopposed alpha effects raise peripheral resistance and blood pressure.", 88,
    ["β-blockers: prevent actions on β receptors which leave α effects unopposed", "increased peripheral resistance and increase in BP"]),
  C(ADAG, "Which heart rate response does norepinephrine provoke?", "Reflex bradycardia through the baroreceptor reflex.", 89,
    ["Baroreceptor reflex", "reflex rise in vagal activity which causes bradycardia"]),
  C(ADAG, "Which drug may be used to treat norepinephrine extravasation?", "Phentolamine.", 90,
    ["Extravasation may cause blanching and sloughing", "May be treated with α receptor antagonist phentolamine"]),
  C(ADAG, "Which types of shock is dopamine used for?", "Cardiogenic and septic shock.", 93, ["Cardiogenic and septic shock"]),
  C(ADAG, "Which synthetic beta-1 agonist increases cardiac output in acute heart failure?", "Dobutamine.", 94,
    ["Synthetic β1 receptor agonist", "Increase cardiac output in acute heart failure"]),
  C(ADAG, "Why is dobutamine used cautiously in atrial fibrillation?", "It increases atrioventricular conduction.", 94,
    ["Increases AV conduction (caution use in atrial fibrillation)"]),
  C(ADAG, "Which decongestant causes rebound congestion if used longer than three days?", "Oxymetazoline.", 95,
    ["Oxymetazoline", "Rhinitis medicamentosa (rebound congestion) may occur if used longer than three days"]),
  C(ADAG, "Which synthetic alpha-1 agonist causes reflex bradycardia?", "Phenylephrine.", 96, ["Synthetic α1 receptor agonist", "Induces reflex bradycardia"]),
  C(ADAG, "Which alpha-2 agonist causes rebound hypertension when stopped abruptly?", "Clonidine.", 97,
    ["Synthetic α2 receptor agonist", "Rebound hypertension with abrupt discontinuance"]),
  C(ADAG, "Which adverse effects does albuterol cause?", "Tremor, restlessness, apprehension and anxiety.", 98, ["Tremor, restlessness, apprehension, anxiety"]),
  C(ADAG, "With which drug class does tyramine cause serious vasopressor effects?", "Monoamine oxidase inhibitors.", 101,
    ["May cause serious vasopressor effects if patient taking MAOI"]),
  C(ADAG, "Why is pseudoephedrine kept behind the pharmacy counter?", "It can be converted to methamphetamine.", 104,
    ["Can be converted to methamphetamine, so now kept behind pharmacy counter"]),
 ], [
  M(ADAG, "Epinephrine", "Alpha and beta agonist for anaphylaxis", [(83, ["Interacts with α and β receptors"]), (85, ["Anaphylactic shock"])]),
  M(ADAG, "Norepinephrine", "Mostly alpha; raises vascular resistance in shock", [(89, ["α receptors most affected"]), (90, ["Shock: increases vascular resistance"])]),
  M(ADAG, "Isoproterenol", "Beta agonist to stimulate the heart in emergencies", 91, ["Predominately stimulates β1 and β2 receptors", "Stimulate heart in emergency"]),
  M(ADAG, "Dopamine", "Norepinephrine precursor for cardiogenic shock", [(92, ["Precursor to norepinephrine"]), (93, ["Cardiogenic and septic shock"])]),
  M(ADAG, "Dobutamine", "Synthetic beta-1 agonist", 94, ["Synthetic β1 receptor agonist"]),
  M(ADAG, "Oxymetazoline", "Alpha-1 and alpha-2 nasal decongestant", 95, ["Synthetic α1 and α2 receptor agonist", "Nasal decongestant"]),
  M(ADAG, "Phenylephrine", "Alpha-1 decongestant causing reflex bradycardia", 96, ["Synthetic α1 receptor agonist", "Induces reflex bradycardia", "Nasal decongestant"]),
  M(ADAG, "Clonidine", "Centrally acting alpha-2 agonist", 97, ["Synthetic α2 receptor agonist", "acts centrally"]),
  M(ADAG, "Albuterol", "Synthetic selective beta-2 bronchodilator", 98, ["Synthetic β2 receptor agonist", "Bronchodilation"]),
  M(ADAG, "Amphetamine", "Indirect agonist for narcolepsy", [(99, ["Amphetamine"]), (100, ["narcolepsy"])]),
  M(ADAG, "Tyramine", "Fermented-food amine that displaces norepinephrine", 101,
    ["Enters nerve terminal and displaces stored norepinephrine", "fermented foods"]),
  M(ADAG, "Cocaine", "Indirect agonist that is also a local anesthetic", [(99, ["Indirect-acting Adrenergic Agonists", "Cocaine"]), (102, ["Local anesthetic"])]),
  M(ADAG, "Pseudoephedrine", "Mixed-action decongestant kept behind the counter", 104,
    ["Pseudoephedrine used to relieve nasal and sinus congestion", "kept behind pharmacy counter"]),
 ]),
 (ADAN, "Adrenergic Antagonists", "accent1", BLOCK_ICON, [
  C(ADAN, "Which heart rate response do alpha blockers induce?", "Reflex tachycardia.", 107, ["α-Adrenergic Blocking Agents", "Induce reflex tachycardia"]),
  C(ADAN, "How does phenoxybenzamine block alpha receptors?", "Irreversibly and noncompetitively.", 108, ["Block is irreversible and non-competitive"]),
  C(ADAN, "What is epinephrine reversal?", "Alpha blockade leaves only epinephrine's beta-mediated vasodilation.", 109,
    ["Epinephrine reversal: Blocks vasoconstriction effects (α-agonist activity) of epinephrine, but not vasodilation"]),
  C(ADAN, "Which catecholamine-secreting tumor does phenoxybenzamine treat?", "Pheochromocytoma.", 109, ["Treatment of pheochromocytoma"]),
  C(ADAN, "Which alpha blocker prevents dermal necrosis after norepinephrine extravasation?", "Phentolamine.", 110,
    ["Phentolamine", "Locally to prevent dermal necrosis and extravasation due to norepinephrine"]),
  C(ADAN, "Phentolamine treats hypertensive crisis after abrupt withdrawal of which drug?", "Clonidine.", 110,
    ["Hypertensive crisis due to abrupt clonidine withdrawal"]),
  C(ADAN, "Which selective alpha-1 blockers treat benign prostatic hyperplasia?", "Tamsulosin and alfuzosin.", 111,
    ["Benign prostatic hyperplasia (Tamsulosin, alfuzosin)"]),
  C(ADAN, "Which selective alpha-1 blockers treat hypertension?", "Prazosin, terazosin and doxazosin.", 111, ["Hypertension (prazosin, terazosin, doxazosin)"]),
  C(ADAN, "What can the first dose of prazosin, terazosin or doxazosin cause?", "Syncope.", 111,
    ["Hypertension (prazosin, terazosin, doxazosin)", 'Cause "first-dose" syncope']),
  C(ADAN, "In which lung diseases is propranolol contraindicated?", "Chronic obstructive pulmonary disease and asthma.", 115,
    ["Contraindicated in patients with chronic obstructive pulmonary disease (COPD or asthma"]),
  C(ADAN, "What can follow abrupt propranolol withdrawal?", "Arrhythmias, from up-regulated beta receptors.", 117,
    ["Arrhythmias if stopped abruptly", "Secondary to up-regulation of β receptors"]),
  C(ADAN, "Name two non-cardiac indications for propranolol.", "Migraine prevention and hyperthyroidism.", 116, ["Migraine prevention", "Hyperthyroidism"]),
  C(ADAN, "Which nonselective beta blocker reduces aqueous humor in glaucoma?", "Timolol.", 119,
    ["Timolol reduces production of aqueous humor in eye", "Used in chronic open-angle glaucoma"]),
  C(ADAN, "Which beta blockers suit hypertension with impaired pulmonary function?", "Selective beta-1 antagonists such as metoprolol.", 120,
    ["Selective β1 Antagonists", "metoprolol", "Useful to treat hypertension in patients with impaired pulmonary function"]),
  C(ADAN, "Which beta blockers have intrinsic sympathomimetic activity?", "Acebutolol and pindolol.", 121,
    ["Acebutolol (β1-selective antagonist) and pindolol (nonselective β antagonist)", "Intrinsic sympathomimetic activity (ISA)"]),
  C(ADAN, "Which two drugs block alpha-1, beta-1 and beta-2 receptors?", "Labetalol and carvedilol.", 122, ["α1, β1, β2 Antagonist Activity", "Labetalol and carvedilol"]),
  C(ADAN, "Which alpha-beta blocker is given intravenously for hypertensive emergencies?", "Labetalol.", 122, ["Labetalol (IV) used to treat hypertensive emergencies"]),
  C(ADAN, "Which alpha-beta blocker prevents cardiovascular mortality in heart failure?", "Carvedilol.", 122,
    ["Carvedilol decreases lipid peroxidation", "Shown to prevent cardiovascular mortality in patients with heart failure"]),
  C(ADAN, "How does reserpine act?", "It blocks amine transport into storage vesicles, depleting them.", 123,
    ["Reserpine", "Depletes norepinephrine, dopamine, and serotonin action by blocking transport from cytoplasm into storage vesicles"]),
  C(ADAN, "How does guanethidine act?", "It blocks release of stored norepinephrine.", 123, ["Guanethidine", "Blocks release of stored norepinephrine"]),
 ], [
  M(ADAN, "Phenoxybenzamine", "Irreversible nonselective alpha blocker", 108, ["Nonselective α1 and α2-receptor blocker", "Block is irreversible"]),
  M(ADAN, "Phentolamine", "Competitive nonselective alpha blocker", 110, ["Competitive α1 and α2-receptor blocker"]),
  M(ADAN, "Prazosin", "Selective alpha-1 blocker for hypertension", 111, ["Selective, competitive α1-receptor blockers", "Hypertension (prazosin"]),
  M(ADAN, "Tamsulosin", "Selective alpha-1 blocker for prostatic hyperplasia", 111, ["Selective, competitive α1-receptor blockers", "Benign prostatic hyperplasia (Tamsulosin"]),
  M(ADAN, "Propranolol", "Nonselective beta blocker for migraine prevention", [(114, ["Non-selective β-antagonist"]), (116, ["Migraine prevention"])]),
  M(ADAN, "Timolol", "Nonselective beta blocker for glaucoma", 119, ["Nonselective β1 and β2 blockers", "Used in chronic open-angle glaucoma"]),
  M(ADAN, "Alfuzosin", "Selective alpha-1 blocker for prostatic hyperplasia", 111, ["Selective, competitive α1-receptor blockers", "Benign prostatic hyperplasia (Tamsulosin, alfuzosin)"]),
  M(ADAN, "Pindolol", "Nonselective beta blocker with partial agonism", 121, ["pindolol (nonselective β antagonist)", "Partial Agonist Activity"]),
  M(ADAN, "Acebutolol", "Beta-1-selective with partial agonist activity", 121, ["Acebutolol (β1-selective antagonist)", "Partial Agonist Activity"]),
  M(ADAN, "Labetalol", "Intravenous for hypertensive emergencies", 122, ["Labetalol (IV) used to treat hypertensive emergencies"]),
  M(ADAN, "Carvedilol", "Alpha-beta blocker for heart failure", 122, ["Labetalol and carvedilol", "prevent cardiovascular mortality in patients with heart failure"]),
  M(ADAN, "Reserpine", "Depletes stored norepinephrine, dopamine, serotonin", 123, ["Depletes norepinephrine, dopamine, and serotonin"]),
  M(ADAN, "Guanethidine", "Blocks release of stored norepinephrine", 123, ["Blocks release of stored norepinephrine"]),
 ]),
]
