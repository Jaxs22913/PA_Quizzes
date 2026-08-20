#!/usr/bin/env python3
"""Add the CMS I Exam 1 dermatology Arcade decks.

One deck per lecture, atomic-fact cards per the Arcade content policy: each card
is a single question with a single answer, phrased so it works in Match, Study,
Learn and Sprint alike. No card depends on another, and no answer text is
duplicated within a deck (duplicate answers break Match).
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ARCADE = os.path.join(os.path.dirname(HERE), "arcade.js")

ICON_SKIN = ('<path d="M4 7c0-2 2-4 5-4h6c3 0 5 2 5 4v10c0 2-2 4-5 4H9c-3 0-5-2-5-4z"/>'
             '<path d="M8 9h.01"/><path d="M12 12h.01"/><path d="M15 8h.01"/><path d="M10 16h.01"/>')
ICON_SUN = ('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4"/>'
            '<path d="M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>')
ICON_BACT = ('<ellipse cx="12" cy="12" rx="4" ry="7" transform="rotate(35 12 12)"/>'
             '<path d="M7 6l-2-2M17 18l2 2M17 6l2-2M7 18l-2 2"/>')
ICON_BUG = ('<ellipse cx="12" cy="13" rx="4" ry="6"/><path d="M12 7V4"/>'
            '<path d="M8 9L4 6M16 9l4-3M8 13H3M16 13h5M8 17l-4 3M16 17l4 3"/>')
ICON_DOT = ('<circle cx="8" cy="8" r="2"/><circle cx="16" cy="10" r="1.5"/>'
            '<circle cx="11" cy="15" r="2.5"/><circle cx="17" cy="17" r="1.5"/>')

DECKS = [
 dict(id="cms-general-derm-1", name="General Dermatology I", color="accent", icon=ICON_SKIN, cards=[
  ("Which skin layer is avascular and fed by diffusion?", "The epidermis."),
  ("How many strata make up the epidermis?", "Five."),
  ("Which four cell types sit in the epidermis?", "Keratinocytes, melanocytes, Langerhans cells and Merkel cells."),
  ("Which layer contains collagen, elastin, vessels, nerves and glands?", "The dermis."),
  ("Damage confined to which layer leaves no scar?", "The epidermis — loss of it alone heals without scarring."),
  ("Which layer do furuncles and erythema nodosum involve?", "The subcutaneous tissue."),
  ("Which cell performs immune surveillance in the epidermis?", "The Langerhans cell."),
  ("Under which wavelength does skin synthesise vitamin D?", "Ultraviolet B."),
  ("Where does atopic dermatitis sit in an infant?", "The cheeks and extensor surfaces."),
  ("Where does atopic dermatitis sit in a child or adult?", "The flexures."),
  ("Which test identifies the cause of allergic contact dermatitis?", "Patch testing."),
  ("Which dermatitis produces greasy yellow scale in sebum-rich sites?", "Seborrheic dermatitis."),
  ("Which eczema produces coin-shaped plaques on the extremities?", "Nummular eczema."),
  ("Which eczema produces deep tapioca-like vesicles on palms and soles?", "Dyshidrotic eczema."),
  ("Which dermatitis is bilateral on the lower legs with haemosiderin pigmentation?", "Stasis dermatitis."),
  ("Which feature separates stasis dermatitis from cellulitis?", "Stasis dermatitis is bilateral, chronic and afebrile."),
  ("Which part of the napkin area does diaper dermatitis spare?", "The skin folds."),
  ("What does involvement of the napkin skin folds with satellite lesions suggest?", "Candidal overgrowth."),
  ("Which facial dermatitis spares the vermilion border and follows topical steroid use?", "Perioral dermatitis."),
  ("At which level does bullous pemphigoid split the skin?", "Subepidermal, below the whole epidermis."),
  ("At which level does pemphigus vulgaris split the skin?", "Intraepidermal, within the epidermis."),
  ("Which blistering disease produces tense bullae?", "Bullous pemphigoid, because the split is below the whole epidermis."),
  ("Which blistering disease produces flaccid bullae that rupture easily?", "Pemphigus vulgaris, because the split is within the epidermis."),
  ("In which blistering disease is the Nikolsky sign positive?", "Pemphigus vulgaris — lateral pressure slips the skin."),
  ("Which blistering disease commonly begins with mucosal involvement?", "Pemphigus vulgaris — the mouth is often the first site."),
  ("Which of the two main autoimmune blistering diseases affects the elderly?", "Bullous pemphigoid — pemphigus vulgaris affects the middle-aged."),
  ("Which papulosquamous disease shows the Auspitz sign?", "Psoriasis."),
  ("What is the first lesion of pityriasis rosea?", "The herald patch."),
  ("Which pattern does pityriasis rosea follow on the trunk?", "A Christmas-tree pattern along the skin lines."),
  ("Over how long does pityriasis rosea resolve?", "Six to eight weeks."),
  ("What are the six Ps of lichen planus?", "Purple, polygonal, pruritic, planar papules and plaques."),
  ("What are the fine white lines on a lichen planus lesion called?", "Wickham striae."),
  ("Which condition results from a sustained itch-scratch cycle?", "Lichen simplex chronicus."),
  ("Which alopecia shows exclamation-mark hairs at the patch edge?", "Alopecia areata."),
  ("What is the mechanism of alopecia areata?", "Autoimmune attack on the hair follicle."),
  ("What is the mechanism of androgenetic alopecia?", "Androgen-driven follicular miniaturisation."),
  ("Which topical agent treats androgenetic alopecia?", "Minoxidil."),
 ]),

 dict(id="cms-derm-2", name="Dermatology II", color="accent2", icon=ICON_SUN, cards=[
  ("What triggers over half of erythema multiforme cases?", "Herpes simplex virus."),
  ("How long does an individual urticarial wheal last?", "Less than twenty-four hours."),
  ("What does a wheal persisting beyond twenty-four hours suggest?", "Urticarial vasculitis, which needs a biopsy."),
  ("Which drug is approved for refractory chronic urticaria?", "Omalizumab."),
  ("Where does erythema nodosum appear?", "Bilaterally on the anterior shins."),
  ("Do erythema nodosum nodules ulcerate?", "No — ulceration points to nodular vasculitis instead."),
  ("What is Löfgren syndrome?", "Erythema nodosum, ankle arthritis and hilar lymphadenopathy in sarcoidosis."),
  ("What separates granuloma annulare from tinea corporis?", "Granuloma annulare has no scale on the border."),
  ("What should be screened for in generalised granuloma annulare in an adult?", "Diabetes, thyroid disease, dyslipidaemia and lymphoma."),
  ("What is pathergy?", "Worsening of a lesion after trauma, seen in pyoderma gangrenosum."),
  ("Why is a pyoderma gangrenosum ulcer never debrided?", "Because pathergy makes it larger."),
  ("Which biologic is approved for pyoderma gangrenosum in inflammatory bowel disease?", "Infliximab."),
  ("Which rosacea subtype is the most common?", "Erythematotelangiectatic rosacea."),
  ("Which topical agent is superior for Demodex-associated papulopustular rosacea?", "Ivermectin cream."),
  ("Which feature separates rosacea from acne vulgaris?", "Rosacea has no comedones."),
  ("What are the four defining features of primary focal hyperhidrosis?", "Bilateral, focal, adolescent onset and absent during sleep."),
  ("Which test investigates episodic sweating with headache and hypertension?", "Twenty-four hour urine metanephrines and catecholamines."),
  ("How long does botulinum toxin last in axillary hyperhidrosis?", "Three to six months."),
  ("What is the immunofluorescence finding in dermatitis herpetiformis?", "Granular immunoglobulin A at the dermal papillae."),
  ("What is the cornerstone of dermatitis herpetiformis treatment?", "A lifelong gluten-free diet."),
  ("What must every patient with dermatitis herpetiformis be screened for?", "Coeliac disease."),
  ("What does sudden acanthosis nigricans in an adult suggest?", "An underlying gastrointestinal malignancy."),
  ("What is the gold standard test for epidermolysis bullosa?", "Transmission electron microscopy with immunofluorescence antigen mapping."),
  ("What percentage of body surface detachment defines Stevens-Johnson syndrome?", "Less than ten percent."),
  ("What percentage of body surface detachment defines toxic epidermal necrolysis?", "More than thirty percent."),
  ("What range of detachment defines Stevens-Johnson and toxic epidermal necrolysis overlap?", "Ten to thirty percent."),
  ("Which drug does the deck name as the commonest cause of toxic epidermal necrolysis in Asia?", "Allopurinol."),
  ("Which human leukocyte antigen is linked to carbamazepine-induced Stevens-Johnson syndrome?", "HLA-B*15:02."),
  ("Which human leukocyte antigen is linked to allopurinol reactions?", "HLA-B*58:01."),
  ("Which single action most improves survival in Stevens-Johnson syndrome?", "Immediate withdrawal of the causative drug."),
  ("How many variables make up the SCORTEN score?", "Seven."),
  ("What predicted mortality does a SCORTEN of five or more carry?", "About ninety percent."),
  ("Which drug has the strongest evidence base in toxic epidermal necrolysis?", "Cyclosporine."),
  ("Which topical burn agent is avoided in Stevens-Johnson syndrome?", "Silver sulfadiazine, because of sulfonamide cross-reaction."),
  ("Is antibiotic prophylaxis recommended in toxic epidermal necrolysis?", "No — treat infections only when they are confirmed."),
  ("Which ultraviolet wavelength range causes sunburn?", "Ultraviolet B, 290 to 320 nanometres."),
  ("When does sunburn peak after exposure?", "At twelve to twenty-four hours."),
  ("Which mechanism is non-immunologic and dose-dependent?", "Phototoxicity."),
  ("Which mechanism requires prior sensitisation?", "Photoallergy."),
  ("What is the gold standard test for photoallergy?", "Photopatch testing."),
  ("What photopatch result confirms photoallergy?", "A reaction on the irradiated patch only."),
  ("Which plant chemicals cause phytophotodermatitis?", "Furanocoumarins, also called psoralens."),
  ("Which is the most common idiopathic photodermatosis?", "Polymorphous light eruption."),
  ("Which antibody panel is mandatory before accepting polymorphous light eruption?", "An antinuclear antibody panel including anti-Ro and anti-La."),
  ("What is the most effective prevention for polymorphous light eruption?", "Prophylactic narrow band ultraviolet B in spring."),
  ("Which dermoscopic features suggest solar lentigo?", "Finger-like projections and a moth-eaten border."),
  ("Which gene mutation is the critical event in actinic keratosis?", "TP53."),
  ("What is field cancerization?", "Clinically normal skin around a lesion already carrying subclinical mutations."),
  ("What is the histological hallmark of dermatoheliosis?", "Solar elastosis."),
  ("Which topical agent is the only one approved for photoaging?", "Tretinoin."),
  ("What is the classic marker of severe photoaging on the posterior neck?", "Cutis rhomboidalis nuchae."),
 ]),

 dict(id="cms-cutaneous-bacterial", name="Cutaneous Bacterial Infections", color="accent3", icon=ICON_BACT, cards=[
  ("Which four factors underlie acne vulgaris?", "Follicular hyperkeratinisation, increased sebum, Cutibacterium acnes and inflammation."),
  ("What kind of organism is Cutibacterium acnes?", "An anaerobic Gram-positive rod."),
  ("What was Cutibacterium acnes formerly called?", "Propionibacterium acnes."),
  ("What is the hallmark lesion of acne vulgaris?", "The comedone."),
  ("Which acne lesions are non-inflammatory?", "Open and closed comedones."),
  ("What is the first-line topical treatment for comedonal acne?", "A topical retinoid."),
  ("Which topical comedolytic suits patients who cannot tolerate a retinoid?", "Salicylic acid."),
  ("Why is benzoyl peroxide added to any acne antibiotic?", "To reduce antibiotic resistance."),
  ("How long are oral antibiotics given for acne?", "Three to four months."),
  ("Which oral antibiotics are most commonly used for acne?", "Doxycycline and minocycline."),
  ("For which acne pattern is oral isotretinoin highly effective?", "Recalcitrant nodular acne."),
  ("How long is a typical oral isotretinoin course?", "Sixteen to twenty weeks."),
  ("When must pregnancy tests be done on isotretinoin?", "Before starting, monthly during, and five weeks after."),
  ("Which programme must isotretinoin prescribers join?", "iPledge."),
  ("What is prohibited while taking oral isotretinoin?", "Donating blood."),
  ("How long should separate tretinoin from benzoyl peroxide?", "At least three hours."),
  ("How long does acne take to improve?", "Four to six weeks."),
  ("Which acne sites are slowest to respond?", "The back and chest, at three to four months."),
  ("What does scarring out of proportion to lesion count suggest?", "The patient is picking or squeezing lesions."),
  ("What is the characteristic finding in folliculitis?", "A pustule pierced by a central hair."),
  ("Which organism most commonly causes bacterial folliculitis?", "Staphylococcus aureus."),
  ("How is recurrent folliculitis in a carrier treated?", "Nasal mupirocin twice daily for five days."),
  ("Which organism causes hot tub folliculitis?", "Pseudomonas aeruginosa."),
  ("How soon after hot tub exposure does folliculitis appear?", "Eight hours to five days."),
  ("Which sites does hot tub folliculitis spare?", "Face, neck, palms and soles."),
  ("How long does hot tub folliculitis take to clear?", "Two to ten days."),
  ("What is pseudofolliculitis barbae?", "A foreign body reaction to a cut hair re-entering the skin."),
  ("What is a furuncle?", "A deep abscess of a hair follicle and adjacent subcutaneous tissue."),
  ("What is a carbuncle?", "Two or more confluent furuncles with separate heads."),
  ("When does a single furuncle need no antibiotic?", "When the patient is afebrile and the lesion is under five millimetres."),
  ("What is the mainstay of carbuncle treatment?", "Incision and drainage."),
  ("Which three factors predispose to recurrent furunculosis?", "Obesity, diabetes and nasal staphylococcal carriage."),
  ("Which glands are inflamed in hidradenitis suppurativa?", "The cutaneous apocrine glands."),
  ("Which three elements diagnose hidradenitis suppurativa?", "Typical lesions, axilla and groin distribution, and recurrence more than twice in six months."),
  ("Which lifestyle change is essential in hidradenitis suppurativa?", "Smoking cessation."),
  ("Which intervention gives the best chance of cure in hidradenitis suppurativa?", "Wide excision of the affected areas."),
  ("Which organism causes erythrasma?", "Corynebacterium minutissimum."),
  ("What colour does erythrasma fluoresce under a Wood's lamp?", "Coral-red."),
  ("Which skin layer does impetigo infect?", "The superficial epidermis."),
  ("Which impetigo type is exclusively staphylococcal?", "Bullous impetigo."),
  ("What produces the split in bullous impetigo?", "Staphylococcal epidermolytic toxins."),
  ("Which impetigo type ulcerates into the dermis and scars?", "Ecthyma."),
  ("Which topical agent is adequate for most impetigo?", "Mupirocin ointment."),
  ("Which oral antibiotic is the drug of choice for impetigo in children?", "Cephalexin."),
  ("When may a child with impetigo return to school?", "Twenty-four to forty-eight hours after starting treatment."),
  ("Which complication follows impetigo and is not prevented by antibiotics?", "Acute post-streptococcal glomerulonephritis."),
  ("Which layer does erysipelas involve?", "The upper dermis and superficial cutaneous lymphatics."),
  ("What is the defining physical finding of erysipelas?", "A raised plaque with a clear line of demarcation."),
  ("Which organism causes erysipelas?", "Group A streptococcus."),
  ("What is the treatment for erysipelas?", "Penicillin V, or clindamycin if penicillin allergic."),
  ("Which layers does cellulitis involve?", "The deeper dermis and subcutaneous tissue."),
  ("How do cellulitis borders differ from erysipelas?", "They are neither raised nor sharply demarcated."),
  ("What does purulence in cellulitis prompt?", "Antibiotic cover for methicillin-resistant Staphylococcus aureus."),
  ("Why does devitalised tissue need debridement?", "It is not perfused, so antibiotics cannot reach it."),
  ("When should cellulitis fever have resolved?", "Within twenty-four hours of antibiotics."),
  ("What does fever beyond forty-eight hours of cellulitis treatment mean?", "Change the antimicrobial therapy, guided by culture."),
  ("How does an abscess differ in origin from a furuncle?", "It follows traumatic inoculation rather than arising from a follicle."),
  ("What predisposes to acute paronychia?", "Manicure, ingrown nail, hangnail or nail biting."),
  ("Which oral antibiotic suits paronychia after nail biting?", "Clindamycin, for oral flora."),
  ("Which organism causes chronic paronychia?", "Candida albicans."),
  ("How long must chronic paronychia have been present?", "At least six weeks."),
  ("What is the clue for necrotizing fasciitis?", "Unrelenting pain out of proportion to the physical examination."),
  ("Why does necrotizing fasciitis stop being tender as it advances?", "The superficial nerves have been destroyed."),
  ("Should imaging delay surgery in necrotizing fasciitis?", "No, it is a surgical emergency."),
  ("Which organism produces gas in necrotizing fasciitis?", "Clostridium perfringens."),
  ("Which three oral agents cover methicillin-resistant Staphylococcus aureus here?", "Trimethoprim-sulfamethoxazole, clindamycin and doxycycline."),
  ("Which agents cover the methicillin-sensitive organism?", "Dicloxacillin and cephalexin."),
  ("What is a secondary bacterial skin infection?", "Infection arising in skin already damaged by another condition."),
 ]),

 dict(id="cms-derm-infestations", name="Dermatological Infestations", color="accent4", icon=ICON_BUG, cards=[
  ("Which organism causes scabies?", "Sarcoptes scabiei variety hominis."),
  ("How long must contact last to transmit scabies?", "Fifteen to twenty minutes."),
  ("What is the pathognomonic lesion of scabies?", "A thread-like linear or J-shaped burrow one to ten millimetres long."),
  ("How soon does itch appear after a first scabies infestation?", "Four to six weeks."),
  ("How soon does itch appear after scabies reinfestation?", "Two to three days."),
  ("Which body regions does scabies spare in healthy adults?", "The head and neck."),
  ("In which patients can scabies involve the head and neck?", "Infants, the elderly and the immunocompromised."),
  ("What characterises crusted scabies?", "Thick flaking scale with millions of mites and often no itch."),
  ("Which dermoscopic sign indicates a scabies mite?", "The delta-wing jet sign."),
  ("What is a positive burrow ink test?", "A zigzag line running across and away from the lesion."),
  ("How is topical permethrin applied for scabies?", "Overnight to the entire skin surface, with a second application one week later."),
  ("At what temperature must scabies bedding be washed?", "Sixty degrees Celsius."),
  ("How long may itch persist after successful scabies treatment?", "Up to four weeks."),
  ("Which organism causes head lice?", "Pediculus humanus capitis."),
  ("Which organism causes body lice?", "Pediculus humanus humanus."),
  ("Which organism causes pubic lice?", "Phthirus pubis."),
  ("Which age group is most affected by head lice?", "Children between three and twelve years."),
  ("What are maculae caeruleae?", "Slate-grey macules about one centimetre across representing haemorrhage in pubic lice."),
  ("How are nits distinguished from dandruff?", "Nits cannot be removed from the hair shaft."),
  ("How is body louse infestation diagnosed?", "By examining clothing seams and shaking clothing over white paper."),
  ("What is the position on a no-nit school policy?", "It is not recommended, because of the school absence it causes."),
  ("Is fumigation recommended for head lice?", "No — bag or dry clothing and bedding, and vacuum."),
  ("What is the classic pattern of bedbug bites?", "A linear row of three painless bites."),
  ("How long can a bedbug survive without a blood meal?", "Up to one year."),
  ("What is required to eradicate a bedbug infestation?", "A professional exterminator."),
  ("What is tungiasis?", "Infestation by an adult female flea penetrating the skin to lay eggs."),
  ("How is tungiasis diagnosed?", "Dermoscopy visualising ovoid eggs."),
  ("How is tungiasis treated?", "Surgical excision or cryotherapy with tetanus prophylaxis and antibiotics."),
  ("Which disease do rat fleas transmit?", "Bubonic plague."),
  ("How should a honeybee stinger be removed?", "By scraping with a card edge held parallel to the skin."),
  ("What does fire ant venom induce?", "Mast cell degranulation."),
  ("What proportion of Hymenoptera stings cause a generalised systemic reaction?", "Between 0.4 and three percent."),
  ("Which caterpillar is described as the most poisonous?", "The asp or puss caterpillar."),
  ("Which sign follows an asp caterpillar sting?", "A train-track pattern of purpura."),
  ("How are caterpillar hairs removed from skin?", "By stripping with adhesive tape."),
  ("What causes cutaneous larva migrans?", "Larvae of animal hookworms from contaminated sand or soil."),
  ("How fast does a cutaneous larva migrans trail advance?", "Two to three centimetres a day."),
  ("How is cutaneous larva migrans treated?", "Albendazole for three days, or ivermectin."),
  ("Which two procedures are not recommended for cutaneous larva migrans?", "Surgical excision and cryotherapy."),
  ("Which spider carries a red hourglass?", "The black widow spider."),
  ("Which neurotoxin is in black widow venom?", "Alpha-latrotoxin."),
  ("Which spider carries a dark fiddle marking?", "The brown recluse spider."),
  ("What is the hallmark sign of a brown recluse bite?", "The red, white and blue sign."),
  ("When does eschar form after a brown recluse bite?", "Between days five and seven."),
  ("Why is surgery delayed in a brown recluse wound?", "Until the wound has become stable."),
  ("Which spider predominates in the Pacific Northwest?", "The hobo spider."),
  ("How do tarantulas cause human disease?", "Shed hairs embed in the skin and eyes."),
  ("Which organism causes Lyme disease?", "Borrelia burgdorferi."),
  ("What is the stage 1 lesion of Lyme disease?", "Erythema migrans, over five centimetres with central clearing."),
  ("When does erythema migrans appear?", "About one week after the tick bite."),
  ("What defines stage 2 Lyme disease?", "Early disseminated infection days to weeks later."),
  ("What is the classic manifestation of stage 3 Lyme disease?", "Monoarticular arthritis of a weight-bearing joint."),
  ("What is first-line oral treatment for Lyme disease?", "Doxycycline."),
  ("Which agent replaces doxycycline for early Lyme disease in children and pregnancy?", "Amoxicillin."),
  ("Is there a human Lyme disease vaccine?", "No, only one for dogs."),
  ("Which organism causes Rocky Mountain spotted fever?", "Rickettsia rickettsii."),
  ("What is the clinical triad of Rocky Mountain spotted fever?", "Fever, headache and rash."),
  ("In what proportion is the Rocky Mountain spotted fever triad present?", "About sixty percent."),
  ("Where does the Rocky Mountain spotted fever rash begin?", "On the ankles and wrists."),
  ("Which body region does the Rocky Mountain spotted fever rash spare?", "The face."),
  ("What is the gold standard test for Rocky Mountain spotted fever?", "Indirect immunofluorescence assay."),
  ("By which day should Rocky Mountain spotted fever treatment start?", "By day five."),
  ("Which antibiotic treats Rocky Mountain spotted fever in children?", "Doxycycline, weight-based."),
  ("Is prophylaxis recommended after a tick bite in a Rocky Mountain spotted fever area?", "No — prevention rests on avoidance, clothing, tick checks and DEET."),
  ("What causes cercarial dermatitis?", "Penetration of the skin by cercarial larvae of parasitic flatworms."),
  ("How soon does severe itch begin in cercarial dermatitis?", "Ten to twelve hours after exposure."),
  ("What do primary skin lesions affect?", "The epidermis and superficial dermis."),
  ("What do secondary skin lesions affect?", "The dermis or subcutaneous tissue."),
  ("What does crusting or scaling on a lesion indicate?", "That the epidermis has been affected."),
 ]),

 dict(id="cms-pigmented-lesions", name="Pigmented Skin Lesions", color="accent5", icon=ICON_DOT, cards=[
  ("How are ephelides inherited?", "Autosomal dominant."),
  ("Which gene variant underlies ephelides?", "MCR-1."),
  ("What does MCR-1 receive as its ligand?", "Alpha-melanocyte-stimulating hormone."),
  ("Which pigment does reduced MCR-1 pathway activity promote?", "Pheomelanin, the yellow-red sulfur-containing pigment."),
  ("How large are ephelides?", "Three to five millimetres."),
  ("What happens to ephelides when sun exposure stops?", "They fade."),
  ("Which lesion is the main differential for ephelides?", "Lentigines."),
  ("Why is cryotherapy not used for ephelides?", "The lesions are too small for it to be practical."),
  ("Which topical depigmenting agents are used for ephelides?", "Hydroquinone, retinoids, alpha-hydroxy acids and botanicals."),
  ("What happens to lentigines when sun exposure stops?", "They do not fade."),
  ("How large is a lentigo simplex?", "Less than five millimetres."),
  ("What age distribution do lentigines follow?", "Bimodal, in early childhood or later life."),
  ("What are agminated lentigines?", "A grouping of small light brown macules."),
  ("When should an inherited disorder be considered with lentigines?", "When a partial or generalised lentigo is present."),
  ("What proportion of people have solar lentigines by age fifty?", "About ninety percent."),
  ("Where do solar lentigines coalesce?", "At sites of severe sunburn."),
  ("Into what can solar lentigines progress?", "Lichenoid keratoses."),
  ("Which sites do photochemotherapy-induced lentigines involve?", "Sun-protected sites such as buttocks and genitalia, as well as exposed skin."),
  ("How large are seborrheic keratoses?", "Two to twenty millimetres."),
  ("How do seborrheic keratoses feel and look?", "Velvety or warty, and stuck onto the skin."),
  ("Why do seborrheic keratoses matter clinically?", "They are easily mistaken for neoplasms."),
  ("When is cryotherapy used for a seborrheic keratosis?", "When the lesion is itchy or inflamed."),
  ("What is dermatosis papulosa nigrans identical to?", "Small seborrheic keratoses."),
  ("Where does dermatosis papulosa nigrans occur?", "On the face and neck."),
  ("What is the presumed origin of dermatosis papulosa nigrans?", "A genetic developmental defect of the hair follicle."),
  ("Why is cryotherapy avoided in dermatosis papulosa nigrans?", "Because of post-inflammatory hyperpigmentation."),
  ("What is the mechanism of vitiligo?", "T-cell mediated destruction of melanocytes."),
  ("Before what age does vitiligo usually start?", "Before the thirties."),
  ("What proportion of vitiligo patients present before age twenty?", "About half."),
  ("How do vitiligo lesions behave under a Wood's lamp?", "They fluoresce."),
  ("Which vitiligo variant is unilateral and does not cross the midline?", "The segmental variant."),
  ("Which laboratory tests accompany a vitiligo diagnosis?", "Complete blood count and antinuclear antibody."),
  ("Below what body surface involvement is topical therapy used in vitiligo?", "Five percent."),
  ("Which topical class suits the face and children in vitiligo?", "Topical calcineurin inhibitors, tacrolimus and pimecrolimus."),
  ("Which risks accompany topical steroids in vitiligo?", "Skin atrophy and raised intraocular pressure."),
  ("What is first-line phototherapy for vitiligo?", "Narrow band ultraviolet B."),
  ("Why is PUVA not preferred in vitiligo?", "It carries adverse effects including increased skin cancer risk."),
  ("When is surgical grafting used in vitiligo?", "Only in highly stable disease."),
  ("From where do acquired melanocytic naevi arise?", "Junctional melanocytes."),
  ("From where do congenital melanocytic naevi arise?", "Neural-crest derived melanocytic precursors."),
  ("What defines a dysplastic naevus?", "Atypical architectural and cytologic features."),
  ("What determines melanoma risk in a congenital melanocytic naevus?", "Its size — the larger the lesion the higher the risk."),
  ("Which condition follows congenital naevi of the head, neck and posterior midline?", "Neurocutaneous melanosis."),
  ("Which imaging is needed for a cranial or axial congenital melanocytic naevus?", "Magnetic resonance imaging of the brain, with or without total spine."),
  ("What does the background of a naevus spilus resemble?", "A café-au-lait spot."),
  ("What is the melanoma risk of naevus spilus?", "It rarely progresses to melanoma."),
  ("When does the number of common acquired naevi peak?", "In the thirties."),
  ("How large is a typical common acquired naevus?", "Less than six millimetres."),
  ("Which colour in a naevus on light skin is suspicious?", "Very dark brown or black."),
  ("What is a blue naevus composed of?", "Deeply pigmented spindle or epithelioid melanocytes in the dermis."),
  ("How large is a common blue naevus?", "Less than one centimetre."),
  ("Where do blue naevi occur?", "Dorsal hands and feet, scalp, buttocks or sacral region."),
  ("What is another name for pigmented spindle cell naevus?", "Reed naevus."),
  ("Where is a pigmented spindle cell naevus usually found?", "On the extremities, mainly the thigh."),
  ("How is a pigmented spindle cell naevus managed?", "Excision with negative margins."),
  ("What colour is a Spitz naevus?", "Pink or red."),
  ("Which sites does a Spitz naevus spare?", "Palms, soles and mucous membranes."),
  ("What do multiple Spitz naevi suggest?", "A familial cancer syndrome."),
  ("How is a Spitz naevus diagnosed?", "By biopsy or wide excision."),
  ("What is the minimum size of a dysplastic melanocytic naevus?", "Five millimetres."),
  ("How many naevi define dysplastic naevus syndrome?", "Over one hundred by adolescence."),
  ("What relationship links naevus count and melanoma?", "The higher the number of naevi, the higher the melanoma risk."),
  ("Which dysplastic naevi are biopsied?", "All changing or developing lesions."),
 ]),
]


def js_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def deck_js(d):
    cards = "\n".join("      [%s, %s]," % (js_str(q), js_str(a)) for q, a in d["cards"])
    cards = cards.rstrip(",")
    return ('  { id: "%s", name: "%s", color: "%s",\n'
            "    icon: '%s',\n"
            "    cards: [\n%s\n    ] },\n" % (d["id"], d["name"], d["color"], d["icon"], cards))


def main():
    s = open(ARCADE, encoding="utf-8").read()
    assert "cms-general-derm-1" not in s, "decks already added"

    # every card must be well formed and unique within its deck
    for d in DECKS:
        qs = [q for q, _ in d["cards"]]
        ans = [a for _, a in d["cards"]]
        assert len(set(qs)) == len(qs), "%s: duplicate question" % d["id"]
        assert len(set(ans)) == len(ans), ("%s: duplicate ANSWER -- this breaks Match: %r"
                                           % (d["id"], [a for a in ans if ans.count(a) > 1][:2]))
        for q, a in d["cards"]:
            assert q.endswith("?"), "%s: card is not a question: %r" % (d["id"], q)
            assert 0 < len(a) < 200, "%s: answer length %d: %r" % (d["id"], len(a), a)

    # insert the deck objects immediately after the existing CMS deck
    marker = '\n  { id: "cms-1", name: "Clinical Medicine and Surgery I", exams: ['
    assert s.count(marker) == 1, "group marker not found"
    end_of_decks = s.index(marker)
    # walk back to the end of the last deck literal before the groups block
    tail = s.rindex("] },\n", 0, end_of_decks) + len("] },\n")
    s = s[:tail] + "\n" + "".join(deck_js(d) for d in DECKS) + s[tail:]

    # register them on the Exam 1 group
    old_group = '{ id: "exam1", name: "Exam 1", deckIds: ["cms-clinical-reasoning"] }'
    assert s.count(old_group) == 1, "exam group not found"
    ids = ['"cms-clinical-reasoning"'] + ['"%s"' % d["id"] for d in DECKS]
    new_group = ('{ id: "exam1", name: "Exam 1", deckIds: [\n      %s\n    ] }'
                 % ", ".join(ids))
    s = s.replace(old_group, new_group)

    open(ARCADE, "w", encoding="utf-8").write(s)
    print("decks added: %d (%d cards)" % (len(DECKS), sum(len(d["cards"]) for d in DECKS)))


if __name__ == "__main__":
    main()
