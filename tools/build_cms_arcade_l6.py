#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the CMS I Lecture 6 (Cutaneous Viral and Fungal Infections) Arcade deck.

One deck for one topic, joining the existing CMS Exam 1 group in syllabus order
-- before benign skin lesions, since Lecture 6 precedes Lecture 7.

THE SLIDE IS AUTHORITATIVE (Jaxon, 2026-08-20). Every card comes from the deck.

Cards are single atomic facts for Sprint's eight-second clock; matchCards are
recognition pairs with compressed identity tags. Nothing here needs a picture,
which matters because Arcade has no image support -- the recognition work lives
in the guide's photograph strips and the comparison chart.

DUPLICATE CHECK IS ON FRONTS. Two cards must never ask the same question, but a
repeated ANSWER is an engine concern, not a content one -- Match groups the
definitions column by text and Learn/Sprint exclude distractors equal to the
correct answer. Distorting a fact so that no two cards share a value would be
the wrong trade.
"""
import json, os, re, sys

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
# a spore with a hypha, for fungus
ICON = ('<circle cx="8" cy="8" r="3.2"/><path d="M10.4 10.4C13 13 15 14 18 14"/>'
        '<path d="M13 11.6c.6 1.8.4 3.4-.6 4.8"/><circle cx="18.5" cy="14.2" r="1.6"/>')

DECKS = [
 dict(id="cms-viral-fungal", name="Cutaneous Viral & Fungal Infections", color="accent2",
      icon=ICON, cards=[
  # --- KOH and the antifungal classes
  ["What does potassium hydroxide do to a skin scraping?", "Dissolves the keratin and leaves the fungus behind."],
  ["What does a dermatophyte look like on potassium hydroxide?", "Branching hyphae."],
  ["What does pityriasis versicolor look like on potassium hydroxide?", "Short hyphae with clusters of yeast, called spaghetti and meatballs."],
  ["What does Candida look like on potassium hydroxide?", "Budding yeast with pseudohyphae."],
  ["From where do you sample a suspected tinea lesion?", "The active border, never the cleared centre."],
  ["From where do you sample a nail for onychomycosis?", "The most proximal accessible diseased nail bed, after trimming the onycholytic nail."],
  ["Which antifungal class ends in -fine, and how does it work?", "The allylamines, such as terbinafine, which destroy the fungal cell membrane."],
  ["Which antifungal class ends in -azole, and how does it work?", "The imidazoles, such as ketoconazole, which block ergosterol synthesis."],
  # --- dermatophytes
  ["What tissue can dermatophytes survive on?", "Dead keratin only, meaning stratum corneum, hair and nails."],
  ["Where can dermatophytes not survive?", "On mucous membranes."],
  ["Name the three dermatophyte genera.", "Microsporum, Trichophyton and Epidermophyton."],
  ["Which age group gets tinea capitis, and why does it stop after puberty?", "Preadolescent children; changes in the fatty acid content of sebum are believed to inhibit growth."],
  ["Which dermatophyte species is commonest in tinea capitis in the United States?", "Trichophyton tonsurans."],
  ["What is black dot tinea capitis?", "Infection in which the hair fractures at the scalp surface, leaving visible black dots."],
  ["Why does tinea capitis require oral therapy?", "Topical agents do not penetrate the infected hair shaft."],
  ["Which oral agent is favored for Trichophyton scalp infection?", "Terbinafine."],
  ["Which oral agent is favored for Microsporum scalp infection?", "Griseofulvin."],
  ["How long do tinea capitis fungal particles stay viable on fomites?", "Months."],
  ["What is the role of antifungal shampoo in tinea capitis?", "It reduces viable spore shedding but never replaces oral therapy."],
  ["Must a treated child with tinea capitis stay off school?", "Generally no, once effective therapy has begun, though local policy applies."],
  ["What separates tinea barbae from bacterial folliculitis on examination?", "In tinea barbae the hairs are loose and easily removed."],
  ["Which form of tinea barbae comes from animals?", "The inflammatory form, with tender boggy pustular kerion-like plaques."],
  ["What produces the ring in tinea corporis?", "Progressive central clearing of a sharply circumscribed scaly plaque."],
  ["How far beyond the border should topical treatment for tinea corporis go?", "One to two centimetres."],
  ["Why must corticosteroid and antifungal combination products be avoided?", "Steroids mask and worsen dermatophytosis, producing tinea incognito."],
  ["Which condition is commonly confused with tinea corporis?", "Nummular eczema."],
  ["What single finding argues against tinea cruris in a groin rash?", "Scrotal involvement, which suggests candidal intertrigo instead."],
  ["Which fluoresces coral-red under a Wood lamp?", "Erythrasma."],
  ["What is the commonest dermatophyte infection in adults?", "Tinea pedis."],
  ["Which toe web spaces does interdigital tinea pedis favour?", "The third and fourth interspaces."],
  ["Which tinea pedis variant benefits from a keratolytic?", "The hyperkeratotic variant, with its shoe distribution."],
  ["Which tinea pedis variant is the moist acute painful one?", "The vesiculobullous variant."],
  ["What is the essential self-care measure in tinea pedis?", "Drying between the toes after bathing."],
  ["What is two feet-one hand syndrome?", "Tinea manuum affecting the hand used to scratch the infected foot."],
  # --- nails, id, incognito
  ["What must be established before starting oral therapy for a dystrophic nail?", "That the nail is actually fungal, because many dystrophic nails are not."],
  ["What is first-line for dermatophyte onychomycosis, and for how long?", "Oral terbinafine, usually six weeks for fingernails and twelve for toenails."],
  ["Which oral agent is off label for onychomycosis in the United States?", "Fluconazole."],
  ["Why does a treated nail still look abnormal at six weeks?", "Improvement requires nail growth, so appearance lags behind the treatment."],
  ["What is an id reaction?", "An inflammatory dermatitis at a site distant from a primary dermatophyte infection."],
  ["How long after the primary infection does an id reaction appear?", "One to two weeks."],
  ["What potassium hydroxide pattern establishes an id reaction?", "Positive at the primary site and negative at the reaction site."],
  ["How is an id reaction treated?", "By treating the primary dermatophyte infection."],
  ["What causes tinea incognito?", "Inappropriate treatment, usually with topical corticosteroids, altering the appearance."],
  ["What should you warn a patient about when stopping the steroid in tinea incognito?", "That inflammation may rebound after withdrawal."],
  # --- yeasts
  ["Is intertrigo primarily an infection?", "No. It is inflammation from friction, moisture and heat in a fold, which Candida may then infect."],
  ["What finding supports Candida in a fold rash?", "Satellite papules or pustules."],
  ["What does malodor, erosion or drainage in a fold suggest?", "Bacterial coinfection."],
  ["What is the spectrum difference between topical nystatin and a topical azole?", "Nystatin treats Candida only; azoles treat Candida and many dermatophytes."],
  ["What organism causes pityriasis versicolor?", "Overgrowth of lipid-dependent Malassezia species that normally inhabit the skin."],
  ["Is pityriasis versicolor contagious?", "No, because the organism already lives on normal skin."],
  ["Why do pale patches persist after pityriasis versicolor is cleared?", "Hypopigmentation reflects altered melanocyte function, and recovery can lag months behind."],
  ["Why is oral terbinafine ineffective for pityriasis versicolor?", "Adequate drug levels are not achieved in sweat, although topical terbinafine works."],
  ["Which oral agent must never be used for pityriasis versicolor, and why?", "Ketoconazole, because hepatic and adrenal toxicity outweigh benefit in superficial infection."],
  # --- varicella and zoster
  ["What is the defining feature of the varicella eruption?", "Lesions in several stages of healing present at the same time."],
  ["Which analgesic must be avoided in a child with varicella?", "Aspirin."],
  ["When does varicella contagiousness begin and end?", "One to two days before the rash, until all lesions have crusted."],
  ["Which precautions are used for varicella in hospital?", "Standard, airborne and contact precautions."],
  ["Where does varicella-zoster virus stay latent?", "In cranial-nerve or dorsal-root ganglia."],
  ["What is the classic finding of the acute eruptive phase of zoster?", "Grouped herpetiform vesicles on an erythematous base."],
  ["How far does a zoster eruption spread?", "One or two adjacent dermatomes, stopping abruptly at the midline."],
  ["Which dermatome group is involved most often in zoster?", "Thoracic, in about fifty-five per cent."],
  ["Can a susceptible contact catch shingles from someone with shingles?", "No. Exposure to vesicular fluid or airborne virus can cause varicella instead."],
  ["How long is a patient with zoster infectious?", "Until the lesions have dried."],
  ["What is zoster sine herpete?", "Dermatomal pain without any vesicular eruption."],
  ["Within what window should zoster antivirals ideally start?", "Seventy-two hours of rash onset."],
  ["Name one reason to treat zoster after seventy-two hours.", "New lesions are still forming."],
  ["How is postherpetic neuralgia defined?", "Pain persisting ninety days or more after rash onset."],
  ["What is allodynia?", "Pain evoked by light touch."],
  ["What is first-line for postherpetic neuralgia?", "Gabapentin or pregabalin, a tricyclic antidepressant, or topical lidocaine."],
  ["Do corticosteroids prevent postherpetic neuralgia?", "No, and they must never replace antiviral therapy."],
  ["What is the Hutchinson sign?", "Zoster lesions on the tip or side of the nose, raising ocular risk."],
  ["Does absence of the Hutchinson sign exclude eye involvement?", "No."],
  ["What defines Ramsay Hunt syndrome?", "Peripheral facial palsy with painful vesicles of the ear canal, auricle or oropharynx."],
  ["Which zoster complication is treated with an antiviral plus a systemic corticosteroid?", "Ramsay Hunt syndrome, started early when not contraindicated."],
  ["Who gets two doses of recombinant zoster vaccine?", "Immunocompetent adults fifty and over, and adults nineteen and over who are or will be immunosuppressed."],
  ["What is the standard interval between Shingrix doses?", "Two to six months."],
  # --- HSV, whitlow, molluscum, warts
  ["Does the site of a herpes simplex lesion tell you the viral type?", "No. Either type can cause oral or genital infection."],
  ["Can herpes simplex be transmitted with no visible lesion?", "Yes, during asymptomatic shedding."],
  ["What is the preferred test for herpes simplex?", "Type-specific amplification testing from a fresh vesicle, ulcer base or crust."],
  ["Which herpes simplex test does the deck tell you not to use?", "Immunoglobulin M serology."],
  ["Why can a negative swab from an older herpes lesion not exclude infection?", "Because viral shedding is intermittent."],
  ["Which first episodes of herpes simplex are treated?", "Every one of them."],
  ["Does suppressive valacyclovir eliminate transmission risk?", "No. It lowers it, and condoms reduce but do not eliminate it."],
  ["What is herpetic whitlow?", "A painful herpes simplex infection of the distal finger, often inoculated through broken skin."],
  ["What must never be done for herpetic whitlow?", "Incision and drainage, which does not treat the virus and can delay healing."],
  ["Which virus family causes molluscum contagiosum?", "A poxvirus."],
  ["What is the characteristic feature of a molluscum lesion?", "Central umbilication."],
  ["How long can molluscum take to clear on its own?", "Months to several years, although most immunocompetent patients do clear it."],
  ["Which molluscum treatment is applied at home, and from what age?", "Berdazimer ten point three per cent gel, from age one year."],
  ["Which molluscum treatment is applied by a clinician, and from what age?", "Cantharidin zero point seven per cent, from age two years."],
  ["Do genital molluscum lesions in a child prove abuse?", "No. Location alone does not prove it, and assessment must be context-sensitive."],
  ["What should extensive or giant facial molluscum prompt?", "Evaluation for immunosuppression, including human immunodeficiency virus where appropriate."],
  ["Which layer of skin does a wart occupy?", "The epidermis only, though it displaces the dermis and seems deeper."],
  ["What does the underside of a wart look like?", "Round and smooth, with no roots."],
  ["What are the tiny black dots in a common wart?", "Thrombosed dilated capillaries, made clearer by trimming the surface."],
  ["Who gets periungual, lip and tongue warts?", "Nail biters."],
  ["What spreads flat warts?", "Shaving, through autoinoculation."],
  ["When does a plantar wart require treatment?", "Only when it is painful."],
  ["What forms a mosaic wart?", "Plantar warts clustering together."],
  ["Does any therapy reliably eradicate human papillomavirus?", "No. No therapy eradicates it with certainty, and recurrence can occur."],
 ], matchCards=[
  ["Spaghetti and meatballs", "Pityriasis versicolor"],
  ["Budding yeast and pseudohyphae", "Candida"],
  ["Scrotum typically spared", "Tinea cruris"],
  ["Satellite papules and pustules", "Candidal intertrigo"],
  ["Two feet, one hand", "Tinea manuum"],
  ["Positive primary, negative distant site", "Id reaction"],
  ["Altered by topical steroid", "Tinea incognito"],
  ["Several stages at once", "Varicella"],
  ["Stops at the midline", "Herpes zoster"],
  ["Lesions on the nose tip", "Hutchinson sign"],
  ["Facial palsy with ear vesicles", "Ramsay Hunt syndrome"],
  ["Pain ninety days after the rash", "Postherpetic neuralgia"],
  ["Central umbilication", "Molluscum contagiosum"],
  ["Never incise and drain", "Herpetic whitlow"],
 ]),
]


def js_deck(d):
    def pairs(rows):
        return "\n".join('      [%s, %s],' % (json.dumps(a, ensure_ascii=False),
                                              json.dumps(b, ensure_ascii=False)) for a, b in rows)
    return ('  { id: %s, name: %s, color: %s,\n    icon: \'%s\',\n'
            '    cards: [\n%s\n    ],\n    matchCards: [\n%s\n    ] },\n') % (
        json.dumps(d["id"]), json.dumps(d["name"]), json.dumps(d["color"]),
        d["icon"], pairs(d["cards"]), pairs(d["matchCards"]))


s = open(ARCADE, encoding="utf-8").read()
if "cms-viral-fungal" in s:
    sys.exit("deck already present -- nothing to do")

for d in DECKS:
    assert 8 <= len(d["cards"])
    assert 10 <= len(d["matchCards"]) <= 14, "%s: matchCards outside target" % d["id"]
    for front, back in d["cards"]:
        assert len(back.split()) <= 26, "card back too long -> %s" % back
    for term, definition in d["matchCards"]:
        assert len(definition.split()) <= 9, "match definition too long -> %s" % definition
    # fronts must be unique; see the module docstring on why backs are not checked
    for coll in ("cards", "matchCards"):
        fronts = [x[0] for x in d[coll]]
        assert len(fronts) == len(set(fronts)), "duplicate front in %s of %s" % (coll, d["id"])

m = re.search(r"\n\];\n", s[s.index("var DEMO_DECKS"):])
end = s.index("var DEMO_DECKS") + m.start() + 1
s = s[:end] + "".join(js_deck(d) for d in DECKS) + s[end:]

# syllabus order: Lecture 6 comes before Lecture 7's benign lesions
OLD = '"cms-derm-infestations", "cms-benign-lesions"'
NEW = '"cms-derm-infestations", "cms-viral-fungal", "cms-benign-lesions"'
assert s.count(OLD) >= 1, "CMS exam group not found"
s = s.replace(OLD, NEW)

open(ARCADE, "w", encoding="utf-8").write(s)
print("added %d deck(s): %d cards, %d match pairs"
      % (len(DECKS), sum(len(d["cards"]) for d in DECKS), sum(len(d["matchCards"]) for d in DECKS)))
