# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 15 — Fungi of Medical Importance (Dr. Fair, 30 October 2026), pool A: deck slides
# 3-37 — fungal pathogenicity, thermal dimorphism, the World Health Organization fungal priority list,
# epidemiology and portals of entry, diagnosis, antifungal control (amphotericin B), and the four true (primary)
# fungal pathogens: Histoplasma, Coccidioides, Blastomyces and Paracoccidioides. Pool B (tools/micro_l15_pool_b.py)
# holds the subcutaneous, cutaneous and superficial mycoses and the opportunists (slides 38-65, plus slide 9).
#
# PHASE 1, FROM THE SLIDES ALONE (the recording is not yet transcribed). Every key and every explanation is from
# the VISIBLE slides, text and pictures; the speaker notes are not used. Picture-only content used: slide 6 (the
# dimorphism cycle: natural habitat below 30 C, saprobic mold; animal habitat 35-40 C, parasitic yeast; the
# conditions of each conversion), 13/25/29/32/36 (the same distribution map), 17 (the identification flowchart and
# its two footnotes), 18 (stains: Aspergillus branched septate hyphae, germinating Candida), 23 (levels of
# invasion), 27 (Histoplasma colonies at two temperatures; the quiz picture l15-fig-01.jpg), 28 (the Histoplasma
# cycle), 31 (the Coccidioides cycle), 35 (cutaneous blastomycosis). Facts from slides 38-65 appear only inside
# explanations, as the replacing fact for a distractor.
#
# Four options throughout. KEYS SHORT and explanations FULL. Every key is authored at position 0 with the only
# "Correct." opener; the partition rotates positions per set (the one QO item is ordered and never rotated).
# `mis` names the misconception each distractor stands for (review metadata; the renderer strips it).
#
# DELIBERATELY NOT ASKED (held), and why:
#   - amphotericin B's routes (slide 20 lists oral and intramuscular; current practice differs).
#   - percentages and counts (0.3%, 300 of 100,000 species, about 10% of nosocomial infections, 10-100 conidia,
#     1 million and 5 million bacterial deaths, the list's dates): trivia; a few appear only as context.
#   - WHICH or HOW MANY true pathogens leave lasting immunity: slide 15 says "a few", slide 24 says "all of the
#     diseases caused by the true fungal pathogens can result in immunity in a competent host". Only the
#     true-versus-opportunist contrast (reinfection highly likely with opportunists) is asked.
#   - which drug treats which true pathogen (azoles, ketoconazole, sulfa drugs): amphotericin B itself is asked
#     (source, mechanism, toxicity, side effects); drug choice per organism is not.
#   - Histoplasma against Blastomyces by REGION: Histoplasma's "eastern and central" United States and the map's
#     Histoplasma dots overlap Blastomyces' "midwestern and southeastern" range, so neither is ever a distractor for
#     the other on geography (the Blastomyces vignette leaves Histoplasma out of the options).
#   - temperature boundaries: slide 5 says mold at 30 C, slide 6 says below 30 C, slide 27 says below 35 C. The one
#     numeric item keys 37 C (yeast), on which all three agree, and every distractor is at or below 30 C.
#   - the Blastomyces picture (slide 34) has no labels; it is cited only for "dimorphic".
SRC = "PAJ5200.Fungi of Medical importance.pptx"


def c(*n):
    return f"{SRC}, Slide " + (str(n[0]) if len(n) == 1 else ", ".join(map(str, n[:-1])) + " and " + str(n[-1]))


def ci(img, *n):
    """cite with a picture slide: c(n...) + ' and image on Slide img'"""
    return (c(*n) + f" and image on Slide {img}") if n else f"{SRC}, image on Slide {img}"


IO1 = ("1 — Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases, "
       "clinical manifestations, methods of treatment, and prevention of fungi of medical importance")
IO2 = "2 — Describe the modes of transmission by which humans acquire fungi of medical importance"
IMG = "micro-exam-3-quiz-images"


def Q(topic, io, q, key, wrong, cite, **kw):
    """key = (text, explanation); wrong = [(text, explanation, misconception), x3]. Key authored at 0."""
    assert len(wrong) == 3, q
    d = dict(topic=topic, io=io, q=q,
             opts=[[key[0], key[1]]] + [[t, e] for t, e, _ in wrong],
             mis={t: m for t, _, m in wrong}, c=0, cite=cite)
    d.update(kw)
    return d


def QO(topic, io, q, options, key_index, cite, **kw):
    """ORDERED (numeric) options, listed ASCENDING: options = [(text, explanation, misconception or None) x4];
    the key's misconception is None. Never rotated by the partition."""
    assert len(options) == 4 and options[key_index][2] is None, q
    d = dict(topic=topic, io=io, q=q, opts=[[t, e] for t, e, _ in options],
             mis={t: m for i, (t, _, m) in enumerate(options) if i != key_index}, c=key_index, cite=cite,
             ordered=True)
    d.update(kw)
    return d


POOL_A = [

# ============================================================== FUNGAL PATHOGENICITY (slides 4, 5, 7, 15, 22)
Q("Fungal pathogenicity", IO1,
  "Which ability defines a true (primary) fungal pathogen?",
  ("Invading and growing in a healthy host",
   "Correct. A true or primary fungal pathogen can invade and grow in a healthy host. Its most striking adaptation "
   "is the switch from hyphal cells to yeast cells with the change to host temperature. An opportunist, by "
   "contrast, has little or no virulence of its own and needs impaired host defenses."),
  [("Needing impaired host defenses to infect",
    "Needing impaired defenses (human immunodeficiency virus infection, cancer, diabetes) describes an "
    "opportunistic fungal pathogen, which has little or no virulence of its own. A true pathogen needs no such "
    "help: it invades and grows in a healthy host.",
    "opportunist definition swapped in"),
   ("Spreading readily from person to person",
    "Most fungal pathogens do not need a host to complete their life cycles, so their infections are generally not "
    "communicable; the person-to-person spreaders are the dermatophytes and Candida, which live on the body. A true "
    "pathogen is defined by invading a healthy host.",
    "communicability confused with pathogenicity"),
   ("Staying a mold at human body temperature",
    "This reverses thermal dimorphism: these fungi grow as molds at 30 C but switch to yeasts at 37 C, human body "
    "temperature. The switch is their adaptation to the host; the defining ability is invading and growing in a "
    "healthy host.",
    "reversed dimorphism")],
  c(5, 7, 12)),

Q("Fungal pathogenicity", IO1,
  "A fungus with few, if any, virulence factors causes a systemic infection in a patient taking long-term "
  "corticosteroids. How is this mycosis best classified?",
  ("Opportunistic mycosis",
   "Correct. Few, if any, virulence factors plus a host weakened by corticosteroids is the picture of an "
   "opportunistic mycosis: these fungi usually start infection in immunocompromised hosts, and predisposing "
   "factors such as primary illness, corticosteroid use, diabetes and cancer should be considered."),
  [("True (primary) mycosis",
    "A true pathogen can invade and grow in a healthy host and does not depend on a weakened one. A fungus with "
    "few, if any, virulence factors striking a patient on corticosteroids is an opportunist; the tell is the "
    "impaired host.",
    "degree of pathogenicity reversed"),
   ("Subcutaneous mycosis",
    "Subcutaneous mycoses begin when trauma inoculates the fungus into the skin or nails, a level of invasion "
    "rather than a degree of pathogenicity. This infection is systemic and arose in a corticosteroid-weakened "
    "host from a low-virulence fungus, which marks it as opportunistic.",
    "level of invasion confused with pathogenicity"),
   ("Dermatophytosis",
    "Dermatophytoses are strictly confined to keratinized epidermis (skin, hair, scalp and nails), so they are not "
    "systemic. A low-virulence fungus causing systemic disease in a patient on corticosteroids is an opportunistic "
    "mycosis.",
    "superficial skin mycosis confused with systemic disease")],
  c(5, 7, 14, 22, 42)),

Q("Fungal pathogenicity", IO1,
  "Fungi are relatively nonpathogenic for humans. Of which hosts are they the most common pathogens?",
  ("Crops and other plants",
   "Correct. Fungi are the most common plant pathogens: potato blights and infected grape crops or fruit trees, "
   "with huge socio-economic losses such as the potato famines in Ireland and Eastern Europe. For humans they are "
   "relatively nonpathogenic; only a few hundred of about 100,000 fungal species are linked to human or animal "
   "disease."),
  [("Healthy humans",
    "Humans are relatively resistant to fungal infections as long as the immune system is competent, so healthy "
    "people are not where fungi dominate as pathogens. Fungi are the most common pathogens of plants, as in potato "
    "blights.",
    "overestimates human pathogenicity"),
   ("Hospitalized patients",
    "Mycoses are a rising share of nosocomial infections, an emerging concern, yet still a minority of them (about "
    "one in ten). The hosts in which fungi are the most common pathogens are plants: crops, vines and fruit "
    "trees.",
    "emerging concern taken for dominance"),
   ("Domestic animals",
    "Only a few hundred fungal species are linked to disease in humans and animals together, so fungi are "
    "relatively nonpathogenic for animals as well. The hosts in which they are the most common pathogens are "
    "plants, as with potato blights.",
    "animal disease overestimated")],
  c(4, 7)),

Q("Fungal pathogenicity", IO1,
  "Why are opportunistic mycoses described as an emerging medical concern?",
  ("Their share of nosocomial infections is rising",
   "Correct. Mycoses account for a growing share of nosocomial (hospital-acquired) infections, about one in ten "
   "and rising, which is why opportunistic fungi are an emerging concern. They need impaired host defenses (human "
   "immunodeficiency virus infection, cancer, diabetes, autoimmune disorders) and cause illness from superficial "
   "colonization to fatal systemic disease."),
  [("Healthy people now catch them easily",
    "Opportunists have little or no virulence of their own and need impaired host defenses; people with a "
    "competent immune system are relatively resistant to fungi. The emerging concern is their rising share of "
    "nosocomial infections.",
    "opportunist given true-pathogen reach"),
   ("A once-effective vaccine has stopped working",
    "There is no effective fungal vaccine to fail: immunization is typically ineffective against fungal infections "
    "because reinfection is exceedingly common. What makes opportunists an emerging concern is their rising share "
    "of nosocomial infections.",
    "assumes a fungal vaccine exists"),
   ("Spores are newly widespread in the air",
    "Molds and yeasts are already widely distributed in air, dust, fomites and the normal flora of humans, plants "
    "and animals, so exposure is nothing new. The change is a rising share of nosocomial infections in hosts with "
    "impaired defenses.",
    "exposure mistaken for the new factor")],
  c(4, 7, 19)),

Q("Fungal pathogenicity", IO1,
  "Dermatophytes, residents of human and animal skin, are flagged as an emerging fungal concern. Which change in "
  "them explains this?",
  ("They may be becoming true pathogens",
   "Correct. Dermatophytes live on human and animal skin and may be undergoing a gradual transformation to become "
   "true pathogens, fungi able to invade and grow in a healthy host. Today their infections stay strictly in the "
   "keratinized epidermis, spread by contact and fomites."),
  [("They have begun spreading through blood",
    "Dermatophytoses are strictly confined to keratinized epidermis: skin, hair, scalp and nails. Blood-borne "
    "spread belongs to systemic mycoses; the change flagged for dermatophytes is a gradual move toward becoming "
    "true pathogens.",
    "systemic spread misattributed"),
   ("They are now caught by inhaling spores",
    "Inhaled spores are the portal of the primary (systemic) mycoses. Dermatophytes spread by contamination of skin "
    "or hair, close person-to-person contact and fomites; the emerging change is that they may be becoming true "
    "pathogens.",
    "portal of entry confused"),
   ("Most now resist the azole drugs",
    "Dermatophytoses are still treated mainly with topical azoles applied for several weeks; azole resistance is "
    "described in Aspergillus and attributed to agricultural crop spraying. The change flagged for dermatophytes is "
    "a move toward becoming true pathogens.",
    "resistance story borrowed from Aspergillus")],
  c(5, 7, 12, 14, 42, 43, 45, 60)),

Q("Fungal pathogenicity", IO1,
  "Beyond intact skin, mucous membranes and respiratory cilia, which host defense is among the most important "
  "against fungi?",
  ("Cell-mediated immunity",
   "Correct. Skin, mucous membranes and cilia are the barriers; the most important defenses are cell-mediated "
   "immunity (T cells and their cytokines), phagocytosis and inflammation. That is why impaired immunity, as in "
   "human immunodeficiency virus infection or cancer, opens the door to opportunistic fungi."),
  [("Vaccine-induced antibody",
    "Immunization is typically ineffective against fungal infections because reinfection is exceedingly common, so "
    "vaccine antibody is not a defense to rely on. The most important defenses are cell-mediated immunity, "
    "phagocytosis and inflammation.",
    "assumes an effective fungal vaccine"),
   ("Immunity left by a past infection",
    "With opportunistic fungi reinfection is highly likely (think of repeated vaginal yeast infections or foot "
    "fungus), so a past infection is not a dependable shield. The defenses named as most important are "
    "cell-mediated immunity, phagocytosis and inflammation.",
    "overestimates acquired immunity"),
   ("An acidic, low-pH environment",
    "A low pH inhibits most bacteria but not fungi; that is exactly why Sabouraud dextrose agar is acidic, to grow "
    "fungi while holding bacteria back. Acidity is no antifungal defense; cell-mediated immunity, phagocytosis and "
    "inflammation are the most important.",
    "antibacterial condition assumed to work on fungi")],
  c(7, 15, 16, 19)),

Q("Fungal pathogenicity", IO1,
  "A woman has had several episodes of vaginal yeast infection over the years. Which statement about immunity to "
  "opportunistic fungi like this one is accurate?",
  ("Reinfection with them is highly likely",
   "Correct. Long-term immunity does not develop against opportunistic fungi, so reinfection with them is highly "
   "likely; repeated episodes of vaginal yeast infection or foot fungus are the familiar result. The same fact, "
   "that reinfection is exceedingly common, is why immunization against fungi is typically ineffective."),
  [("One episode leaves lasting immunity",
    "Long-term immunity does not follow infection with opportunistic fungi; reinfection is highly likely, which is "
    "why her episodes keep recurring. The recurrence itself is the tell that no protective immunity formed.",
    "assumes lasting immunity after infection"),
   ("Vaccination prevents further episodes",
    "Immunization is typically ineffective against fungal infections precisely because reinfection is exceedingly "
    "common. Control relies on antifungal drugs such as azoles and nystatin, not on vaccines.",
    "assumes an effective fungal vaccine"),
   ("Healthy people have no defense to them",
    "Humans are relatively resistant to fungi while the immune system is competent: skin, mucous membranes, cilia, "
    "cell-mediated immunity, phagocytosis and inflammation all defend. What is missing against opportunists is "
    "lasting immunity, so reinfection is likely.",
    "overstates susceptibility")],
  c(4, 15, 19)),

# ============================================================== THERMAL DIMORPHISM (slides 5, 6, 24, 27)
QO("Thermal dimorphism", IO1,
   "At which temperature does a thermally dimorphic fungus grow as unicellular yeast?",
   [("20 C",
     "20 C lies in the natural-habitat range (below 30 C), where the fungus grows as a saprobic, multicellular mold "
     "that reproduces by sporulation. The unicellular yeast form needs the warmth of an animal host: 37 C.",
     "natural-habitat temperature taken for host temperature"),
    ("25 C",
     "25 C is room temperature, used for selective agar cultures that show the mold phase when the laboratory "
     "demonstrates dimorphism. The unicellular yeast form appears at 37 C, human body temperature.",
     "room-temperature culture (mold phase)"),
    ("30 C",
     "30 C is the temperature at which dimorphic fungi grow as multicellular molds. They switch to unicellular "
     "yeasts at 37 C, human body temperature, inside the 35 to 40 C range of the animal habitat.",
     "mold temperature taken for yeast temperature"),
    ("37 C",
     "Correct. Thermally dimorphic fungi grow as multicellular molds at 30 C and as unicellular yeasts at 37 C, "
     "human body temperature; in the animal habitat (35 to 40 C) they live as parasitic, budding yeasts. Culturing "
     "at room temperature and at 37 C demonstrates the switch.",
     None)],
   3, ci(6, 5, 17)),

Q("Thermal dimorphism", IO1,
  "What switch in form is the most striking adaptation of true fungal pathogens to the human host?",
  ("From hyphal cells to yeast cells",
   "Correct. A true pathogen's most striking adaptation is switching from hyphal (multicellular) cells to yeast "
   "(unicellular) cells as the temperature rises to that of the host; spores that reach the lungs germinate into "
   "yeast or yeast-like cells. This is thermal dimorphism."),
  [("From yeast cells to hyphal cells",
    "This is the reverse switch: yeast cells that leave the animal host return to the environment and revert to the "
    "sporulating hyphal state. Inside the host the change runs from hyphae to yeasts.",
    "direction reversed"),
   ("From budding yeasts to germ tubes",
    "Germ tubes are tiny hyphal tubes that some yeasts sprout after 2 to 4 hours in serum, a laboratory "
    "identification test, not the host adaptation. True pathogens switch from hyphal cells to yeast cells at body "
    "temperature.",
    "laboratory test taken for the adaptation"),
   ("From spores to encapsulated cells",
    "Capsules are listed among fungal virulence factors, but making them is not the change of form that marks true "
    "pathogens. Their most striking adaptation is the switch from hyphal cells to yeast cells at host "
    "temperature.",
    "virulence factor taken for dimorphism")],
  ci(6, 5, 14, 17, 24)),

Q("Thermal dimorphism", IO1,
  "Besides a rise in temperature, which conditions accompany a dimorphic fungus's change to its yeast phase in an "
  "animal host?",
  ("Reduced oxygen and suboptimal nutrients",
   "Correct. Moving from the natural habitat into a warm-blooded animal brings increased temperature, reduced "
   "oxygen and suboptimal nutrients; the spores then germinate into yeasts and stay in that phase in the host. "
   "The opposite set of conditions reverses the change."),
  [("Optimal oxygen and improved nutrients",
    "These are the conditions of the return trip: decreased temperature, optimal oxygen and improved nutrients "
    "send yeast cells leaving the host back to the sporulating hyphal state. Entry into the host brings reduced "
    "oxygen and suboptimal nutrients.",
    "reverse conversion's conditions"),
   ("Reduced oxygen and improved nutrients",
    "Oxygen is right (it falls in the host) but nutrients are not: the move into an animal host brings suboptimal "
    "nutrients. Improved nutrients, with optimal oxygen and a lower temperature, go with reverting to hyphae.",
    "half-reversed set"),
   ("Optimal oxygen and suboptimal nutrients",
    "Nutrients are right (suboptimal in the host) but oxygen is not: it is reduced on entry into the warm-blooded "
    "animal. Optimal oxygen goes with the return to the environment and the sporulating hyphal state.",
    "half-reversed set")],
  ci(6)),

Q("Thermal dimorphism", IO1,
  "Yeast cells of a dimorphic fungus leave the animal host and return to the soil. What happens to them?",
  ("They revert to the sporulating hyphal form",
   "Correct. Yeast cells leaving the animal host return to the environment and revert to the sporulating hyphal "
   "state, helped by decreased temperature, optimal oxygen and improved nutrients. Outside a host the fungus lives "
   "as a saprobic, free-living mold below 30 C; the conversion can be shown on laboratory media."),
  [("They stay yeasts and bud in the soil",
    "Budding is how the yeast phase reproduces inside the animal host, at 35 to 40 C. In the natural habitat, below "
    "30 C, the fungus is a saprobic mold that reproduces by sporulation, so the yeasts revert to hyphae.",
    "host phase assumed to persist"),
   ("They form spherules filled with endospores",
    "Spherules with endospores are the form Coccidioides takes in the lungs, inside the host; its free-living stage "
    "is block-like arthroconidia. Yeasts that leave a host revert to the sporulating hyphal state.",
    "Coccidioides tissue form"),
   ("They die at the lower temperature",
    "Below 30 C is the natural habitat of the free-living mold, not a lethal condition. The yeasts revert to the "
    "sporulating hyphal state, a conversion that can even be demonstrated on artificial media in the laboratory.",
    "assumes cooling kills the fungus")],
  ci(6, 30)),

Q("Thermal dimorphism", IO1,
  "These two colonies are the same fungal pathogen grown on agar below 35 C (left) and at 37 C (right). Which "
  "property of the fungus do they demonstrate?",
  ("Thermal dimorphism",
   "Correct. One fungus forming a fuzzy, mold-like colony below 35 C and a different, yeast-like colony at 37 C, "
   "human body temperature, is thermal dimorphism: multicellular mold at the lower temperature, unicellular yeast "
   "at 37 C. Histoplasma capsulatum, the most common true fungal pathogen, shows exactly this."),
  [("Germ tube formation",
    "A germ tube is a tiny hyphal tube that some yeasts sprout after 2 to 4 hours in serum; it is read under the "
    "microscope, not as two colonies at two temperatures. Here the only variable is temperature, which is how "
    "dimorphism is demonstrated.",
    "yeast identification test confused with dimorphism"),
   ("Capsule production",
    "A capsule is a virulence factor shown by a negative stain of the cells, as with encapsulated budding yeast, "
    "not by comparing colonies grown at two temperatures. The change in colony form between below 35 C and 37 C is "
    "thermal dimorphism.",
    "virulence factor confused with dimorphism"),
   ("Spherule formation",
    "Spherules are giant sporangia full of endospores that Coccidioides forms in the lungs; they are seen in tissue, "
    "not as a colony on a plate. Two colony forms at two temperatures show thermal dimorphism.",
    "Coccidioides tissue form")],
  ci(27, 5, 14, 17, 26, 30, 31, 57),
  img=IMG + "/l15-fig-01.jpg",
  alt="Two fungal colonies on agar: on the left a fuzzy, cottony tan colony with a darker center; on the right a "
      "flat, cream-white colony with wrinkled, folded edges.",
  slide="Slide 27"),

# ============================================================== WHO PRIORITY LIST (slides 10, 11, 56, 60)
Q("WHO priority list", IO1,
  "Which pair of fungi both sit in the World Health Organization's critical priority group?",
  ("Candida albicans and Candida auris",
   "Correct. The critical priority group of the World Health Organization's fungal priority pathogens list is "
   "Cryptococcus neoformans, Aspergillus fumigatus, Candida albicans and Candida auris. Both Candida species named "
   "here are in it; other Candida species sit one tier lower, in the high group."),
  [("Candida auris and Histoplasma",
    "Candida auris is critical, but Histoplasma species are in the high priority group, with other Candida species, "
    "Fusarium, the eumycetoma agents and the Mucorales. The fully critical pair here is Candida albicans with "
    "Candida auris.",
    "one member from the high tier"),
   ("Aspergillus fumigatus and Fusarium",
    "Aspergillus fumigatus is critical (third on the list), but Fusarium species are in the high priority group, "
    "with Histoplasma and the Mucorales. Both Candida albicans and Candida auris are critical.",
    "one member from the high tier"),
   ("Cryptococcus neoformans and C. gattii",
    "Cryptococcus neoformans is critical, number one on the list, but Cryptococcus gattii is medium priority, with "
    "Coccidioides, Pneumocystis jirovecii and Paracoccidioides. The same genus does not mean the same tier.",
    "same genus assumed to share a tier")],
  c(11, 56, 60)),

Q("WHO priority list", IO1,
  "Which fungus does the World Health Organization rank as its number one critical fungal pathogen?",
  ("Cryptococcus neoformans",
   "Correct. Cryptococcus neoformans, an encapsulated yeast of soil around urban pigeon roosts and of soil with "
   "decaying wood, is the number one critical fungal pathogen on the World Health Organization's list. The other "
   "critical members are Aspergillus fumigatus, Candida albicans and Candida auris."),
  [("Aspergillus fumigatus",
    "Aspergillus fumigatus is critical, but it is number three on the list; it is the most common Aspergillus "
    "species in human disease. Number one is Cryptococcus neoformans, the encapsulated yeast of pigeon-roost soil.",
    "rank within the critical tier confused"),
   ("Candida auris",
    "Candida auris is critical and emerging, a cause of hospital outbreaks that are difficult to eradicate, but it "
    "is not ranked first. Cryptococcus neoformans holds the number one place on the critical list.",
    "emerging pathogen assumed top-ranked"),
   ("Histoplasma capsulatum",
    "Histoplasma capsulatum is the most common true fungal pathogen, but on the World Health Organization's list "
    "Histoplasma species are high priority, not critical. Number one critical is Cryptococcus neoformans.",
    "most common taken for most critical")],
  c(11, 26, 52, 56, 60)),

Q("WHO priority list", IO1,
  "How do fungal infections compare with bacterial and viral infections in research attention and funding?",
  ("Less attention and less money",
   "Correct. Fungal infections overall get little attention compared with bacterial or viral infections and, "
   "consequently, less money for research and development: detection, diagnosis, treatment and new drugs. The "
   "World Health Organization's fungal priority list was made to complement its earlier bacterial list."),
  [("More attention, as cases are rising",
    "Invasive fungal diseases are indeed increasing, especially among immunocompromised people, but attention has "
    "not followed: fungal infections still get less attention, and so less money, than bacterial or viral ones.",
    "rising cases assumed to bring attention"),
   ("Equal attention under a shared list",
    "The fungal priority list was issued separately, to complement the bacterial priority list of 2017; it is not "
    "one shared list. Fungal infections get less attention and less money than bacterial or viral infections.",
    "the two lists assumed to equalize attention"),
   ("Less attention but more money",
    "Attention is indeed lower, but money follows attention: because fungal infections get little attention, they "
    "also get less money for research and development (detection, diagnosis, treatment and new drugs), not more.",
    "half-reversed: funding decoupled from attention")],
  c(10, 11)),

Q("WHO priority list", IO1,
  "On the World Health Organization's fungal priority list, which fungus is ranked one tier above Coccidioides?",
  ("Histoplasma species",
   "Correct. Coccidioides is in the medium priority group; Histoplasma species are in the high priority group, one "
   "tier above, with other Candida species, Fusarium, the eumycetoma agents and the Mucorales. The critical group "
   "sits above both."),
  [("Paracoccidioides species",
    "Paracoccidioides species share the medium priority group with Coccidioides, Cryptococcus gattii and "
    "Pneumocystis jirovecii, so they sit level with it, not above. Histoplasma species are one tier up, in the high "
    "group.",
    "same tier taken for higher"),
   ("Pneumocystis jirovecii",
    "Pneumocystis jirovecii, the most prominent opportunistic infection in human immunodeficiency virus infection "
    "and acquired immunodeficiency syndrome, is nonetheless medium priority, level with Coccidioides. Histoplasma "
    "is one tier above.",
    "clinical prominence taken for list rank"),
   ("Cryptococcus gattii",
    "Cryptococcus gattii is medium priority, level with Coccidioides, even though its relative Cryptococcus "
    "neoformans tops the critical group. Histoplasma species sit one tier above Coccidioides, in the high group.",
    "genus rank carried over to the species")],
  c(11, 56, 58)),

# ============================================================== EPIDEMIOLOGY & PORTALS (slides 12, 14, 23, 24)
Q("Epidemiology & portals", IO2,
  "Why are most fungal infections generally not communicable from one person to another?",
  ("The fungi need no host for their life cycle",
   "Correct. Most fungal pathogens do not require a host to complete their life cycles: they live free in soil or "
   "other matter and infect when it is disturbed, so their infections are generally not communicable. The "
   "exceptions, dermatophytes and Candida, live on the body and do pass person to person."),
  [("The fungi die at human body temperature",
    "Body temperature does not kill true pathogens: at 37 C they switch from molds to yeasts and keep growing in the "
    "host. Their infections are not communicable because the fungi need no host to complete their life cycles.",
    "dimorphism misread as heat killing"),
   ("One infection leaves lasting immunity",
    "Reinfection is highly likely with opportunistic fungi, so immunity cannot be what stops spread between people. "
    "Most fungal infections are not communicable because the fungi need no host to complete their life cycles.",
    "immunity offered as the reason"),
   ("People rarely meet fungal spores",
    "Molds and yeasts are widely distributed in air, dust, fomites and normal flora, so exposure is common. Spread "
    "from person to person is uncommon because most fungi complete their life cycles without a host.",
    "underestimates exposure")],
  c(4, 5, 12, 15, 24)),

Q("Epidemiology & portals", IO2,
  "Which fungi naturally inhabit the human body and can pass person to person or by fomites such as shared "
  "exercise equipment?",
  ("Dermatophytes and Candida",
   "Correct. Unlike most fungal pathogens, which need no host and are generally not communicable, dermatophytes "
   "(literally 'skin plants') and Candida naturally inhabit the human body and are transmissible from person to "
   "person or by fomites such as shared exercise equipment."),
  [("Histoplasma and Blastomyces",
    "These are soil fungi: Histoplasma grows in moist soil rich in bird and bat guano, Blastomyces in forest soil, "
    "decaying wood and manure. Both are caught by inhaling conidia, and histoplasmosis is not transmitted person to "
    "person.",
    "soil true pathogens assumed contagious"),
   ("Coccidioides and Paracoccidioides",
    "Both live in soil (Coccidioides in alkaline, salty soil of hot, semiarid climates; Paracoccidioides in cool, "
    "humid soil) and are caught by inhaling spores or, for Paracoccidioides, inoculating them into skin. They are "
    "not residents of the body.",
    "soil true pathogens assumed contagious"),
   ("Aspergillus and Cryptococcus",
    "Aspergillus is an airborne soil fungus and Cryptococcus inhabits soil around pigeon roosts and soil with "
    "decaying wood; both come from the environment, not from other people. The body-dwelling, transmissible fungi "
    "are dermatophytes and Candida.",
    "environmental opportunists assumed to be body residents")],
  c(12, 26, 30, 33, 37, 56, 60)),

Q("Epidemiology & portals", IO2,
  "True fungal pathogens occur in predictable geographic patterns. What do these patterns ultimately follow?",
  ("Climate and soil requirements",
   "Correct. True fungal pathogens are distributed in predictable geographical patterns that ultimately coincide "
   "with climate and soil requirements, so each is restricted to certain endemic regions; Coccidioides, for "
   "example, lives in alkaline, salty soils of hot, semiarid climates."),
  [("Human population density",
    "These fungi live free in soil and need no host to complete their life cycles, so the crowding of people does "
    "not set their range. Their endemic regions coincide with climate and soil requirements.",
    "assumes a person-dependent fungus"),
   ("Travel routes of infected people",
    "Infections by most fungal pathogens are not communicable, so infected travelers do not carry an endemic zone "
    "with them. The zones coincide with the climate and soil each fungus requires.",
    "assumes person-to-person spread"),
   ("Bird and bat migration routes",
    "Bird and bat guano enriches the soil Histoplasma grows in, but the pattern of the true pathogens as a group "
    "follows climate and soil requirements, not animal migration; Coccidioides, for example, needs alkaline, salty, "
    "semiarid soil.",
    "one habitat detail generalized")],
  c(12, 24, 26, 30)),

Q("Epidemiology & portals", IO1,
  "Which fungal diseases are the most prevalent, with many cases going undiagnosed or misdiagnosed as skin "
  "allergies or autoimmune disorders?",
  ("Dermatophytoses",
   "Correct. Dermatophytoses, the 'ringworm' or 'tinea' infections of keratinized skin, hair and nails, are the "
   "most prevalent of the fungal diseases, and many cases go undiagnosed or are misdiagnosed as skin-related "
   "allergies or autoimmune disorders."),
  [("Histoplasmosis",
    "Histoplasma capsulatum is the most common true fungal pathogen, but histoplasmosis is a lung infection from "
    "inhaled conidia, not a skin disease mistaken for allergy. The most prevalent fungal diseases overall are the "
    "dermatophytoses.",
    "most common true pathogen taken for most prevalent overall"),
   ("Candidiasis",
    "Candida is the dominant opportunistic pathogen, a different ranking: the most prevalent fungal diseases "
    "overall are the dermatophytoses, whose skin lesions are often misdiagnosed as allergies or autoimmune "
    "disorders.",
    "dominant opportunist taken for most prevalent"),
   ("Aspergillosis",
    "Aspergillus fumigatus accounts for most lung infections among the opportunistic mycoses, a disease of "
    "compromised hosts, not a common skin disease. The dermatophytoses are the most prevalent fungal diseases and the ones mistaken for "
    "skin allergies.",
    "most common lung mycosis taken for most prevalent")],
  c(12, 26, 42, 51)),

Q("Epidemiology & portals", IO2,
  "What is the main portal of entry for the primary (systemic) mycoses?",
  ("Spores inhaled from the air",
   "Correct. The primary mycoses enter by the respiratory portal: spores in the air are inhaled when soil or animal "
   "waste containing conidia is disturbed, and they germinate in the lungs into yeast or yeast-like cells. From "
   "there infection can become systemic in some hosts."),
  [("Trauma that inoculates skin or nails",
    "Trauma that inoculates skin or nails is the portal of the subcutaneous mycoses. Spores of true pathogens can "
    "also be inoculated into broken skin, but the main portal of the primary mycoses is the respiratory tract.",
    "subcutaneous portal"),
   ("Contamination of skin or hair surfaces",
    "Surface contamination of skin or hair is the portal of the cutaneous and superficial mycoses, which stay in "
    "the outer layers. Primary (systemic) mycoses begin with spores inhaled from the air.",
    "cutaneous and superficial portal"),
   ("Shared exercise equipment",
    "Fomites such as shared exercise equipment spread dermatophytes and Candida, which live on the body. The "
    "primary mycoses are generally not communicable; their portal is the respiratory tract, by inhaled spores.",
    "fomite spread of skin fungi")],
  c(12, 14, 24)),

Q("Epidemiology & portals", IO1,
  "A fungal infection involves the stratum corneum and occasionally the upper dermis, but no deeper. What level of "
  "invasion is this?",
  ("Cutaneous",
   "Correct. Cutaneous involvement takes in the stratum corneum and occasionally the upper dermis. It is deeper than "
   "the extremely shallow epidermal colonization of superficial infection but stops short of the subcutaneous "
   "tissue reached after a puncture wound."),
  [("Superficial",
    "Superficial involvement is an extremely shallow colonization of the epidermis, the shallowest of the three skin "
    "depths. Reaching the stratum corneum and, at times, the upper dermis is one level deeper: cutaneous.",
    "depth underestimated"),
   ("Subcutaneous",
    "Subcutaneous involvement occurs after a puncture wound has carried the fungus deeper, into the subcutaneous "
    "tissue below the dermis. An infection that stops at the stratum corneum and upper dermis is cutaneous.",
    "depth overestimated"),
   ("Systemic",
    "In systemic (deep) mycoses the fungus spreads from the lungs or other sites into the circulation, and "
    "fungemia infects the brain, kidneys and other organs. An infection limited to the stratum corneum and upper "
    "dermis is cutaneous.",
    "local skin infection taken for disseminated disease")],
  ci(23, 14)),

# ============================================================== DIAGNOSIS (slides 16, 17, 18)
Q("Diagnosis", IO1,
  "Why does Sabouraud dextrose agar favor the growth of fungi over bacteria?",
  ("Its fairly low pH inhibits most bacteria",
   "Correct. Sabouraud dextrose agar has a fairly low pH, which inhibits most bacteria but not fungi, and specific "
   "chemicals may be added to block bacterial growth further. That makes it the commonly used selective medium for "
   "culturing fungi."),
  [("Its high pH inhibits most bacteria",
    "The pH runs the other way: Sabouraud dextrose agar is fairly acidic, and that low pH is what inhibits most "
    "bacteria while fungi keep growing. A high pH is not its selective feature.",
    "pH direction reversed"),
   ("Its low pH inhibits fungi, not bacteria",
    "This turns the selectivity around: the low pH of Sabouraud dextrose agar inhibits most bacteria but not fungi. "
    "A medium that held fungi back would be useless for culturing them; fungi tolerate the acidity.",
    "selectivity reversed"),
   ("Its dyes stain the fungal cell walls",
    "Dyes and brighteners are applied to specimens to make fungal elements stand out under the microscope; they are "
    "not what makes the agar selective. The agar favors fungi through its fairly low pH and added antibacterial "
    "chemicals.",
    "staining confused with selective culture")],
  ci(17, 16, 18)),

Q("Diagnosis", IO1,
  "A vaginal swab is treated with dilute potassium hydroxide before microscopy for yeast. What does this step "
  "accomplish?",
  ("Lyses human cells, leaving fungal cells intact",
   "Correct. Dilute potassium hydroxide lyses human epithelial cells but leaves fungal cells intact, because fungi "
   "have a thicker cell wall that human cells lack. What remains under the microscope is the fungus, for "
   "example germinating Candida albicans."),
  [("Lyses fungal cells, leaving human cells intact",
    "This is reversed: fungi survive potassium hydroxide because of their thicker cell wall, while human epithelial "
    "cells, which lack that wall, are lysed. The step clears away human cells, not fungi.",
    "reversed target"),
   ("Outlines the yeast capsule by negative staining",
    "A negative stain is a separate step, used for example on sputum to show encapsulated budding yeast such as "
    "Cryptococcus. Potassium hydroxide does not stain anything; it dissolves human epithelial cells.",
    "negative stain confused with potassium hydroxide"),
   ("Induces yeasts to sprout germ tubes",
    "Germ tubes sprout when some yeasts are incubated in serum for 2 to 4 hours, a separate identification test. "
    "Potassium hydroxide instead dissolves human epithelial cells so the fungal cells can be seen.",
    "germ tube test confused")],
  ci(17, 18, 57)),

Q("Diagnosis", IO1,
  "A yeast isolate incubated in serum for 2 to 4 hours grows short hyphal sprouts. Which identification test is "
  "this?",
  ("Germ tube test",
   "Correct. Some yeasts, when incubated in serum for 2 to 4 hours, sprout tiny hyphal tubes called germ tubes. The "
   "germ tube test sits among the identification tests for isolates from blood, cerebrospinal fluid, pus and "
   "vaginal secretions, alongside differential media and biochemical and antigen tests."),
  [("Hair infection test",
    "The hair infection test inoculates sterile hair with culture isolates from hair, skin and nail specimens; it "
    "does not use serum. Hyphal sprouts from yeasts in serum define the germ tube test.",
    "other named test"),
   ("Test for dimorphism",
    "Dimorphism is tested by growing an isolate at two temperatures (room temperature, 25 or 30 C, against 37 C) to "
    "show the mold and yeast forms, not by a few hours in serum. Short hyphal sprouts in serum are germ tubes.",
    "temperature test confused"),
   ("Periodic acid-Schiff stain",
    "Periodic acid-Schiff is a stain used on hair, skin and nail specimens; it colors fungal elements but makes "
    "nothing sprout. Hyphal tubes from yeasts in serum define the germ tube test.",
    "stain confused with a growth test")],
  ci(17)),

Q("Diagnosis", IO1,
  "In the laboratory workup of hair, skin and nail specimens for fungi, which method is applied directly to the "
  "hairs?",
  ("Examination under Wood's light",
   "Correct. For hair, skin and nail specimens the identification pathway uses Wood's light on the hairs, alongside "
   "a hot potassium hydroxide wet mount, brighteners and periodic acid-Schiff staining, before culture on selective "
   "media for 4 weeks and a hair infection test."),
  [("Negative stain for a capsule",
    "A negative stain for a capsule is used on sputum to show encapsulated yeasts such as Cryptococcus; it is not "
    "the direct examination of hairs. Hairs are examined under Wood's light.",
    "sputum method transferred"),
   ("Germ tube test in serum",
    "The germ tube test identifies yeasts that sprout hyphal tubes after 2 to 4 hours in serum, among the tests for "
    "blood, cerebrospinal fluid, pus and vaginal secretion isolates. Hairs are examined directly under Wood's light.",
    "yeast test transferred"),
   ("Inoculation of animals",
    "Animal inoculation is reserved for diagnosing systemic mycoses when other methods are unavailable or "
    "indeterminate, not for hair, skin or nail specimens. Hairs are examined directly under Wood's light.",
    "last-resort method applied to hair")],
  ci(17)),

Q("Diagnosis", IO1,
  "When is animal inoculation used in identifying a fungal pathogen?",
  ("For systemic mycoses when other methods fail",
   "Correct. Animal inoculation is performed only to help diagnose systemic mycoses when other methods are "
   "unavailable or indeterminate. Stains, culture on selective and differential media, and biochemical, antigen and "
   "serological tests come first."),
  [("As the first step for every sputum sample",
    "Sputum is first digested to remove debris, then examined by negative stain, potassium hydroxide mount and "
    "special stains, and cultured for up to 8 weeks. Animals are inoculated only for systemic mycoses when other "
    "methods fail.",
    "last resort taken for first step"),
   ("To demonstrate thermal dimorphism in culture",
    "Dimorphism is shown by culturing on selective agar at room temperature (25 or 30 C) and on blood agar at 37 C. "
    "Animal inoculation is for systemic mycoses when other methods are unavailable or indeterminate.",
    "culture method confused"),
   ("To diagnose superficial hair and nail infections",
    "Hair, skin and nail specimens are worked up with Wood's light, potassium hydroxide, brighteners, stains, "
    "culture and a hair infection test; no animals are used. Animal inoculation is for systemic mycoses when other "
    "methods fail.",
    "systemic method applied to superficial disease")],
  ci(17)),

Q("Diagnosis", IO1,
  "A dye-stained sputum specimen shows a mass of branched septate hyphae and no yeast cells. Which fungus does "
  "this fit?",
  ("Aspergillus species",
   "Correct. Branched septate hyphae in a sputum specimen are the picture of Aspergillus, an airborne soil fungus "
   "whose spores germinate in the lungs and can form fungal balls. Dyes amplify these fungal elements in tissue "
   "specimens."),
  [("Candida albicans",
    "Candida albicans appears as budding or germinating yeast cells with young hyphae or pseudohyphae, typically "
    "from an oral or vaginal swab. A sputum mass of branched septate hyphae with no yeast cells fits Aspergillus.",
    "germinating yeast confused with septate hyphae"),
   ("Cryptococcus neoformans",
    "Cryptococcus neoformans is an encapsulated budding yeast shown by a negative stain, not a mass of hyphae. "
    "Branched septate hyphae without any yeast cells point to Aspergillus, an airborne soil mold.",
    "encapsulated yeast confused with a mold"),
   ("Coccidioides immitis",
    "In the lungs Coccidioides forms spherules containing endospores, and in soil block-like arthroconidia; neither "
    "is a mass of branched septate hyphae in sputum. That pattern is Aspergillus.",
    "Coccidioides tissue form confused")],
  ci(18, 30, 55, 57, 60)),

# ============================================================== ANTIFUNGAL CONTROL (slides 19, 20, 21)
Q("Antifungal control", IO1,
  "Why is immunization typically ineffective for preventing fungal infections?",
  ("Reinfection is exceedingly common",
   "Correct. Immunization is typically ineffective against fungal infections because reinfection is exceedingly "
   "common. Control therefore relies on antifungal drugs (amphotericin B, flucytosine, azoles and nystatin), surgical "
   "removal of damaged tissue where needed, and limiting contact with spores."),
  [("Fungi cause too few human infections",
    "Fungi are relatively nonpathogenic, yet they still cause the dermatophytoses (the most prevalent fungal "
    "diseases), fatal systemic disease and a rising share of nosocomial infections. The stated reason vaccines fail "
    "is that reinfection is exceedingly common.",
    "rarity offered as the reason"),
   ("Fungi turn into yeasts inside the host",
    "Thermal dimorphism, the switch to yeasts at body temperature, is a survival adaptation of true pathogens, not "
    "the reason given for vaccine failure. Immunization is ineffective because reinfection is exceedingly common.",
    "dimorphism offered as the reason"),
   ("Antifungal drugs already prevent infection",
    "Antifungal drugs such as amphotericin B, flucytosine, azoles and nystatin treat infection; they are not the "
    "means of prevention. Prevention is limited to respirator masks and protective clothing, and vaccines fail "
    "because reinfection is so common.",
    "treatment taken for prevention")],
  c(4, 5, 7, 12, 19)),

Q("Antifungal control", IO2,
  "Which measure is the main way to prevent fungal infection by reducing contact with fungal spores?",
  ("High-quality respirator masks",
   "Correct. Methods of prevention are essentially limited to wearing high-quality respirator masks and protective "
   "clothing, with hygiene, to reduce contact with fungal spores; the primary mycoses are caught by inhaling spores "
   "from the air. Immunization is typically ineffective."),
  [("Routine antifungal vaccination",
    "Immunization is typically ineffective for fungal infections because reinfection is exceedingly common. "
    "Prevention relies on respirator masks, protective clothing and hygiene to cut contact with spores.",
    "assumes an effective fungal vaccine"),
   ("Preventive amphotericin B",
    "Amphotericin B is a highly toxic, often expensive treatment, nicknamed 'ampho-terrible' for its side effects, "
    "not a preventive measure. Prevention is limited to respirator masks, protective clothing and hygiene.",
    "treatment drug taken for prevention"),
   ("Isolating infected patients",
    "Most fungal infections are not communicable, because the fungi need no host to complete their life cycles, so "
    "isolating patients does little. Exposure to spores is reduced with respirator masks and protective clothing.",
    "assumes person-to-person spread")],
  c(12, 14, 19, 20)),

Q("Antifungal control", IO1,
  "From what source does the antifungal drug amphotericin B come?",
  ("A soil bacterium of the genus Streptomyces",
   "Correct. Amphotericin B is produced by a soil bacterium in the genus Streptomyces, yet it attacks fungal cells, "
   "which are eukaryotic. It is the highly toxic, often expensive drug of choice for many fungal infections."),
  [("A grain fungus of the genus Claviceps",
    "Claviceps fungi contaminate rye and other grains as ergot, the source of mind-altering lysergic acid: a fungal "
    "toxin, not a drug. Amphotericin B comes from a soil bacterium, Streptomyces.",
    "fungal toxin source taken for drug source"),
   ("A soil mold of the genus Aspergillus",
    "Aspergillus is a very common airborne soil fungus, the cause of aspergillosis and of fungal balls in the "
    "lungs, not the producer of this drug. Amphotericin B is made by a soil bacterium of the genus Streptomyces.",
    "assumes antifungals come from fungi"),
   ("A soil mold of the genus Rhizopus",
    "Rhizopus, with Mucor, is a Zygomycota mold that causes mucormycosis in people with diabetes, leukemia or "
    "malnutrition; amphotericin B is part of that infection's treatment, not a product of it. The drug comes from "
    "Streptomyces, a soil bacterium.",
    "assumes antifungals come from fungi")],
  c(20, 60, 63, 65)),

Q("Antifungal control", IO1,
  "How does amphotericin B damage fungal cells?",
  ("It binds membrane lipids, opening leaks",
   "Correct. Amphotericin B forms complexes with fungal cell membrane lipids, causing openings through which "
   "cytoplasmic ions seep out. The action is not selective enough to spare human cells, since fungi and humans are "
   "both eukaryotes, hence its toxicity."),
  [("It dissolves the thick fungal cell wall",
    "The thick cell wall is what lets fungi survive potassium hydroxide, which lyses human cells instead; it is not "
    "the drug's target. Amphotericin B acts on the cell membrane, complexing with its lipids so ions leak out.",
    "cell wall confused with cell membrane"),
   ("It blocks the mold-to-yeast switch",
    "Thermal dimorphism, the switch from hyphae to yeasts at 37 C, is a fungal virulence factor, but amphotericin B "
    "does not act on it. The drug complexes with membrane lipids so that cytoplasmic ions seep out.",
    "virulence factor taken as drug target"),
   ("It strips away the fungal capsule",
    "Capsules are a virulence factor of some fungi, shown by a negative stain, not the drug's target. Amphotericin B "
    "complexes with membrane lipids, opening the membrane so that cytoplasmic ions leak out.",
    "virulence factor taken as drug target")],
  c(14, 18, 20)),

Q("Antifungal control", IO1,
  "A patient receiving amphotericin B develops fever, weakness and an arrhythmia. Why does this drug also harm the "
  "patient's own cells?",
  ("Fungi and humans are both eukaryotes",
   "Correct. Amphotericin B complexes with cell membrane lipids, and because fungi and humans are both eukaryotes "
   "the action is not selective enough to attack only fungi. Fatigue, weakness, fever and arrhythmia are its "
   "potentially serious side effects, hence the nickname 'ampho-terrible'."),
  [("Its target is a cell wall humans share",
    "Humans have no such cell wall; the thicker fungal cell wall is what human cells lack, which is why potassium "
    "hydroxide lyses human cells and spares fungi. The drug acts on membrane lipids, which fungal and human cells, "
    "both eukaryotic, have in common.",
    "assumes humans have a cell wall"),
   ("It comes from a fungus, not a bacterium",
    "Amphotericin B is produced by a soil bacterium, Streptomyces, and its source is not what makes it toxic. The "
    "toxicity comes from its non-selective action on the membranes of eukaryotic cells, fungal and human alike.",
    "source confused and blamed"),
   ("It destroys the patient's normal flora",
    "Loss of normal flora is not the cause given for its toxicity; fever, weakness and arrhythmia are direct side "
    "effects. Amphotericin B attacks membrane lipids in eukaryotic cells, human as well as fungal.",
    "antibacterial side effect assumed")],
  c(18, 20)),

# ============================================================== HISTOPLASMA (slides 26, 27, 28)
Q("Histoplasma", IO2,
  "After shoveling soil thick with bird droppings beneath an old roost, a man develops a mild pneumonitis caused by "
  "a dimorphic fungus. How did he most likely acquire it?",
  ("Inhaling conidia stirred into the air",
   "Correct. This is the Histoplasma pattern: soil containing bird (or bat) droppings is whipped up, the microconidia "
   "are inhaled, and the patient develops a mild pneumonitis that might recur. Inhaled conidia produce the primary "
   "pulmonary infection."),
  [("Spores entering a cut on his hands",
    "Spores of true pathogens can be inoculated into broken skin, but the lung infection of histoplasmosis comes "
    "from inhaled conidia. Pneumonitis after disturbing dropping-rich soil points to inhalation, not to a cut.",
    "skin inoculation route"),
   ("Swallowing spores from his hands",
    "Ingestion is the route of fungal toxins (mycotoxicoses such as aflatoxin), not of Histoplasma. Its conidia reach "
    "the lungs by inhalation and cause the primary pulmonary infection, here a mild pneumonitis.",
    "ingestion route"),
   ("A peck or scratch from the birds",
    "The birds enrich the soil with nitrogen-rich droppings; the infection follows when that soil is disturbed and "
    "the conidia are inhaled. A lung infection after shoveling points to inhalation, not to a wound.",
    "animal bite or scratch")],
  ci(28, 24, 26, 37, 65)),

Q("Histoplasma", IO1,
  "Which fungus causes the disease nicknamed 'Ohio Valley fever'?",
  ("Histoplasma capsulatum",
   "Correct. Histoplasmosis, 'Ohio Valley fever', is caused by Histoplasma capsulatum, the most common true fungal "
   "pathogen. It is known in the eastern and central United States and is now recognized as endemic in parts of "
   "Latin America and Africa."),
  [("Coccidioides immitis",
    "Coccidioides immitis causes coccidioidomycosis, 'Valley fever' without the Ohio, mainly in the southwestern "
    "United States extending to Mexico and Central and South America. 'Ohio Valley fever' is histoplasmosis.",
    "the two Valley fevers confused"),
   ("Blastomyces dermatitidis",
    "Blastomyces dermatitidis causes North American blastomycosis, its own name, in the midwestern and southeastern "
    "United States and southern Canada. 'Ohio Valley fever' is the nickname of histoplasmosis.",
    "nickname given to a neighboring endemic fungus"),
   ("Paracoccidioides brasiliensis",
    "Paracoccidioides brasiliensis is endemic in Central and South America, the rarest of the primary mycoses, with "
    "no Ohio connection. 'Ohio Valley fever' is histoplasmosis, from Histoplasma capsulatum.",
    "other true pathogen")],
  c(26, 30, 33, 37)),

Q("Histoplasma", IO2,
  "Where does Histoplasma capsulatum grow in nature?",
  ("Moist, nitrogen-rich soil with guano",
   "Correct. Histoplasma capsulatum grows in moist soil with a high nitrogen content, especially soil containing "
   "bird and bat guano. When wind or digging disturbs that soil, the conidia become airborne and are inhaled."),
  [("Alkaline, salty soil of hot, dry land",
    "Alkaline, salty soil in semiarid, hot climates is the home of Coccidioides immitis, whose spread is boosted by "
    "drought, heavy rain and windstorms. Histoplasma needs moist, nitrogen-rich soil, especially with guano.",
    "Coccidioides habitat"),
   ("Cool, humid soils of South America",
    "Cool, humid soils of Brazil, Colombia, Venezuela, Argentina and Paraguay are where Paracoccidioides "
    "brasiliensis lives. Histoplasma grows in moist soil rich in nitrogen, especially with bird and bat guano.",
    "Paracoccidioides habitat"),
   ("Decaying plants, pine straw and hay",
    "Decaying plant matter, pine straw and hay bales are the haunts of Sporothrix schenckii, a saprobe that enters "
    "through puncture wounds. Histoplasma's home is moist, nitrogen-rich soil with bird and bat guano.",
    "Sporothrix habitat")],
  ci(28, 26, 30, 37, 39)),

Q("Histoplasma", IO1,
  "In the tissue phase of histoplasmosis, what happens to the fungus in the lungs?",
  ("Its yeasts are phagocytosed and bud inside",
   "Correct. In the tissue phase the yeast form develops, is phagocytosed, and multiplies by budding "
   "intracellularly. Most patients recover without complications; in some, phagocytes enter the blood and carry "
   "the infection to many organs."),
  [("It forms spherules that release endospores",
    "Spherules releasing endospores are the lung form of Coccidioides, which develop from inhaled arthrospores. "
    "Histoplasma's tissue phase is a yeast that is phagocytosed and then buds inside the phagocyte.",
    "Coccidioides tissue form"),
   ("It stays a mold of branched hyphae",
    "Branched septate hyphae in sputum are Aspergillus. Histoplasma is thermally dimorphic: at 37 C it grows as a "
    "yeast, which phagocytes engulf and inside which it multiplies by budding.",
    "dimorphism ignored"),
   ("Its yeasts are killed once phagocytosed",
    "Phagocytosis does not end the infection here: the yeasts multiply by budding inside the phagocytes, which in "
    "some cases enter the blood and cause disseminated disease in many organs.",
    "assumes phagocytosis is curative")],
  ci(28, 18, 26, 27, 30, 31)),

Q("Histoplasma", IO2,
  "A man is hospitalized with disseminated histoplasmosis, and his wife asks whether she could catch it from him. "
  "What is accurate?",
  ("She cannot catch it from him",
   "Correct. Histoplasmosis is not transmitted person to person. People acquire it by inhaling conidia from moist "
   "soil enriched with bird or bat guano, and in the body the fungus lives as a yeast inside phagocytes, not as an "
   "infective spore."),
  [("She could inhale spores he coughs",
    "The infective forms are conidia from soil; in the lungs the fungus lives as a yeast inside phagocytes. "
    "Histoplasmosis is not transmitted person to person, so his cough does not pass it on.",
    "assumes respiratory droplet spread"),
   ("She could catch it from his skin",
    "Skin-to-skin and fomite spread belong to dermatophytes and Candida, which naturally inhabit the human body. "
    "Histoplasmosis is not transmitted person to person by any route; it is caught by inhaling conidia from soil.",
    "dermatophyte-style contact spread"),
   ("She could if her immunity is weak",
    "A weakened immune system raises the risk of severe fungal disease, but it does not create a person-to-person "
    "route: histoplasmosis is not transmitted between people at all, whatever the contact's immune status.",
    "immune status confused with transmissibility")],
  ci(28, 12, 26)),

# ============================================================== COCCIDIOIDES (slides 30, 31)
Q("Coccidioides", IO1,
  "A 58-year-old African-American man who repairs roads in the southwestern United States develops a lung "
  "infection after a dust storm. Which fungus is the most likely cause?",
  ("Coccidioides immitis",
   "Correct. The southwestern United States, road repair and a dust storm are classic exposures for Coccidioides "
   "immitis (Valley fever), and African or African-American descent, increasing age (over 40 to 60 years) and "
   "occupational dust exposure are its significant risk factors. Inhaled arthrospores establish the lung "
   "infection."),
  [("Histoplasma capsulatum",
    "Histoplasma is acquired from moist, nitrogen-rich soil with bird and bat guano and is known in the eastern and "
    "central United States. Southwestern dust, road work and these risk factors point to Coccidioides.",
    "other inhaled true pathogen"),
   ("Blastomyces dermatitidis",
    "Blastomyces lives in forest soil, decaying wood and manure in the midwestern and southeastern United States and "
    "southern Canada, not in southwestern desert dust. The setting and risk factors fit Coccidioides.",
    "other inhaled true pathogen"),
   ("Paracoccidioides brasiliensis",
    "Paracoccidioides lives in cool, humid soils of Central and South America and strikes poorly nourished rural "
    "farm workers. A southwestern United States road worker exposed to dust fits Coccidioides.",
    "other true pathogen")],
  ci(31, 13, 26, 30, 33, 37)),

Q("Coccidioides", IO2,
  "Digging in soil releases an aerosol that carries Coccidioides into the lungs. In which form is it inhaled?",
  ("Block-like arthroconidia",
   "Correct. In its free-living stage Coccidioides forms block-like arthroconidia; digging or other dust-raising "
   "activity makes an aerosol of these arthrospores, which are inhaled and establish a lung infection. Only in the "
   "lungs does each develop into a spherule."),
  [("Spherules with endospores",
    "Spherules containing endospores are the tissue form that develops in the lungs after inhalation; the "
    "endospores are released there, not in soil. The inhaled form is the block-like arthroconidium.",
    "tissue form taken for infective form"),
   ("Microconidia from bird droppings",
    "Microconidia whipped up from soil containing bird droppings are the infective spores of Histoplasma, from "
    "moist, nitrogen-rich soil. Coccidioides is inhaled as block-like arthroconidia from dry, dusty soil.",
    "Histoplasma's infective form"),
   ("Encapsulated budding yeasts",
    "An encapsulated budding yeast is Cryptococcus neoformans, from soil around pigeon roosts. Coccidioides in its "
    "free-living stage forms block-like arthroconidia, and those are what is inhaled.",
    "Cryptococcus form")],
  ci(31, 28, 30, 56, 57)),

Q("Coccidioides", IO2,
  "Which weather pattern most enhances the spread of Coccidioides?",
  ("Drought, then heavy rain, then windstorms",
   "Correct. Coccidioides lives in alkaline, salty soils of semiarid, hot climates, and its spread is greatly "
   "enhanced by cycles of drought and heavy rains followed by windstorms that raise spore-laden dust. It remains "
   "dormant in winter and spring."),
  [("Cold, wet weather after a warm, dry spell",
    "Sporulation in colder, wetter weather after a warm, dry dormancy is the pattern of Blastomyces dermatitidis in "
    "the midwestern and southeastern United States. Coccidioides spreads with drought, heavy rain and then "
    "windstorms.",
    "Blastomyces pattern"),
   ("Steady rain through winter and spring",
    "Coccidioides remains dormant in winter and spring, so steady seasonal rain is not its spreading pattern. Its "
    "spread is driven by cycles of drought and heavy rain followed by windstorms that lift spore-laden dust.",
    "dormant season taken for active season"),
   ("Cool, humid conditions year-round",
    "Cool, humid soils are the setting of Paracoccidioides in Central and South America. Coccidioides belongs to "
    "hot, semiarid climates with alkaline, salty soil, spread by drought, heavy rain and windstorms.",
    "Paracoccidioides climate")],
  c(30, 33, 37)),

Q("Coccidioides", IO2,
  "Which community measure reduces inhalation of Coccidioides spores in an endemic area?",
  ("Oiling roads to keep down dust",
   "Correct. Coccidioides arthrospores are inhaled from dust, so prevention targets dust: oiling roads, planting to "
   "minimize erosion and using dust masks. Farming, road construction or repair, archaeological digs, landslides "
   "and dust storms all raise exposure."),
  [("Vaccinating outdoor workers",
    "Immunization is typically ineffective against fungal infections because reinfection is exceedingly common. "
    "Coccidioides is prevented by limiting dust: oiling roads, planting against erosion and dust masks.",
    "assumes an effective fungal vaccine"),
   ("Isolating Valley fever patients",
    "Coccidioides is caught from soil dust, and most fungal infections are not communicable, so isolating patients "
    "does nothing to stop exposure. Dust control, such as oiling roads, does.",
    "assumes person-to-person spread"),
   ("Clearing pigeon roosts from buildings",
    "Soil around urban pigeon roosts harbors Cryptococcus neoformans, and bird droppings enrich Histoplasma's soil. "
    "Coccidioides lives in alkaline, salty, semiarid soil and is prevented by dust control such as oiling roads.",
    "another fungus's reservoir")],
  c(12, 19, 26, 30, 56)),

Q("Coccidioides", IO1,
  "What does Coccidioides form in the lungs after its spores are inhaled?",
  ("Spherules that release endospores",
   "Correct. An inhaled arthrospore develops into a spherule (a giant sporangium) that produces endospores, which "
   "are released in the lungs; the free-living stage, by contrast, is block-like arthroconidia. Immunocompetent "
   "people usually fight the infection off, while compromised people can develop meningitis, osteomyelitis and "
   "skin granulomas."),
  [("Yeasts that bud inside phagocytes",
    "Yeasts that are phagocytosed and bud intracellularly are the tissue phase of Histoplasma, which is inhaled as "
    "microconidia. Coccidioides, after inhalation, forms spherules filled with endospores.",
    "Histoplasma tissue form"),
   ("Fungal balls of septate hyphae",
    "Fungal balls in the lungs and branched septate hyphae belong to Aspergillus, whose spores germinate in the "
    "lungs. Coccidioides, after inhalation, becomes spherules that release endospores.",
    "Aspergillus lung form"),
   ("Chains of block-like arthroconidia",
    "Block-like arthroconidia are the free-living stage in soil, the form that is inhaled, not the lung form. Once "
    "in the lungs each arthrospore develops into a spherule that releases endospores.",
    "infective form taken for tissue form")],
  ci(31, 18, 28, 30, 60)),

# ============================================================== BLASTOMYCES (slides 33, 34, 35)
Q("Blastomyces", IO2,
  "Blastomyces dermatitidis lives in forest soil, decaying wood and animal manure. How do people usually acquire "
  "it?",
  ("By inhaling its conidia",
   "Correct. People inhale the conidia when the soil is disturbed; the inhaled conidia (10 to 100) convert to "
   "yeasts and multiply in the lungs, causing cough, chest pain and fever. Chronic skin nodules and later bone and "
   "nervous system complications can follow."),
  [("From an infected person's cough",
    "Most fungal pathogens do not need a host to complete their life cycles, so their infections are generally not "
    "communicable. Blastomyces is acquired from its soil habitat by inhaling conidia.",
    "assumes person-to-person spread"),
   ("Through sexual contact",
    "Sexual contact is one way Candida albicans spreads, a yeast of the human body, not a soil fungus like "
    "Blastomyces dermatitidis. Its conidia are inhaled from soil, decaying wood or manure.",
    "Candida route"),
   ("By eating crops grown in it",
    "Ingestion is the route of fungal toxins (mycotoxicoses such as aflatoxin from grains, corn and peanuts), not of "
    "Blastomyces. Its conidia are inhaled and convert to yeasts in the lungs.",
    "mycotoxin route")],
  c(12, 24, 33, 52, 65)),

Q("Blastomyces", IO1,
  "A man from the midwestern United States has cough, chest pain and fever; a lung lesion on his chest X-ray is "
  "first taken for lung cancer, and his dog is sick with the same symptoms. Which fungus is the likely cause?",
  ("Blastomyces dermatitidis",
   "Correct. Blastomyces dermatitidis lives in the soil of the midwestern and southeastern United States; inhaled "
   "conidia multiply as yeasts in the lungs, the lesion may be mistaken for lung cancer on chest X-ray, and it "
   "causes cough, chest pain and fever in humans, dogs, cats and horses."),
  [("Coccidioides immitis",
    "Coccidioides is a southwestern United States fungus of alkaline, salty, semiarid soil that forms spherules in "
    "the lungs. A midwestern patient with a cancer-like lung lesion and a sick dog fits Blastomyces.",
    "other inhaled true pathogen"),
   ("Paracoccidioides brasiliensis",
    "Paracoccidioides is endemic in Central and South America and is usually a mild, self-limiting infection of "
    "rural farm workers. The midwestern setting, lung cancer mimic and sick dog point to Blastomyces.",
    "other true pathogen"),
   ("Aspergillus fumigatus",
    "Aspergillus fumigatus is an opportunist that threatens patients with human immunodeficiency virus infection, "
    "leukemia or transplants, forming fungal balls in the lungs. The midwestern setting, cancer-like lesion and "
    "sick dog fit Blastomyces.",
    "opportunistic lung fungus")],
  c(30, 33, 37, 60)),

Q("Blastomyces", IO2,
  "Blastomyces dermatitidis lies dormant in warm, dry weather. When does it sporulate?",
  ("In colder, wetter weather",
   "Correct. Blastomyces is dormant in warm, dry weather and sporulates in the colder, wetter weather that follows, "
   "releasing the conidia that people inhale. This cycle plays out in the soils of the midwestern and southeastern "
   "United States and southern Canada."),
  [("In hot, dry summer weather",
    "Warm, dry weather is when Blastomyces lies dormant, not when it sporulates; the season is reversed. "
    "Sporulation follows in colder, wetter weather across its midwestern, southeastern and southern Canadian "
    "range.",
    "reversed season"),
   ("After drought, rain and windstorms",
    "Cycles of drought and heavy rain followed by windstorms drive the spread of Coccidioides in hot, semiarid "
    "climates with alkaline, salty soil. Blastomyces sporulates in colder, wetter weather.",
    "Coccidioides pattern"),
   ("Inside the host at body heat",
    "At body temperature a dimorphic fungus is in its parasitic yeast phase, reproducing by budding; sporulation "
    "belongs to the mold phase of the natural habitat. In soil, Blastomyces sporulates in colder, wetter weather.",
    "host phase confused with sporulation")],
  ci(6, 30, 33)),

Q("Blastomyces", IO1,
  "Beyond the lungs, which progression is typical of chronic blastomycosis?",
  ("Skin nodules, later bone and nerve disease",
   "Correct. Blastomycosis can become chronic, with cutaneous nodules (for example on the hand and wrist) followed "
   "by complications in bone and the nervous system. The infection starts in the lungs, where inhaled conidia "
   "convert to yeasts."),
  [("Lymph node spread from a thorn wound",
    "A nodule at a puncture site that spreads to nearby lymph nodes is lymphocutaneous sporotrichosis, from "
    "Sporothrix schenckii. Blastomycosis produces chronic skin nodules and then bone and nervous system disease.",
    "Sporothrix pattern"),
   ("Fungal balls in sinuses and ear canals",
    "Fungal balls in the lungs and colonization of the sinuses, ear canals, eyelids and conjunctiva belong to "
    "Aspergillus. Chronic blastomycosis means skin nodules and later bone and nervous system complications.",
    "Aspergillus pattern"),
   ("Thick white growth in mouth and throat",
    "A thick, white, adherent growth on the mucous membranes of the mouth and throat is thrush, caused by Candida "
    "albicans. Chronic blastomycosis shows cutaneous nodules followed by bone and nervous system involvement.",
    "Candida pattern")],
  ci(35, 33, 39, 53, 60)),

Q("Blastomyces", IO1,
  "Into what form do inhaled Blastomyces conidia convert in the lungs?",
  ("Multiplying yeast cells",
   "Correct. Blastomyces is a dimorphic fungus, free-living in soil; its inhaled conidia convert to yeasts that "
   "multiply in the lungs, the yeast phase that dimorphic fungi adopt at body temperature in an animal host."),
  [("Spherules full of endospores",
    "Spherules filled with endospores are what Coccidioides forms in the lungs after its arthrospores are inhaled. "
    "Blastomyces conidia convert to yeasts instead, and the yeasts multiply there.",
    "Coccidioides tissue form"),
   ("Branched septate hyphae",
    "Hyphae are the mold form of the natural habitat below 30 C, and branched septate hyphae in sputum are typical "
    "of Aspergillus. At body temperature Blastomyces converts to multiplying yeasts.",
    "mold form assumed in the host"),
   ("Block-like arthroconidia",
    "Block-like arthroconidia are the free-living form of Coccidioides, the form inhaled from dust; they are not a "
    "lung form of either fungus. Inhaled Blastomyces conidia become yeasts that multiply in the lungs.",
    "Coccidioides free-living form")],
  ci(34, 6, 18, 30, 33)),

# ============================================================== PARACOCCIDIOIDES (slide 37; map 13/25/29/32/36)
Q("Paracoccidioides", IO2,
  "Paracoccidioides brasiliensis can infect the lungs or the skin. How does the skin infection arise?",
  ("Inoculation of spores into the skin",
   "Correct. Lung or skin infection with Paracoccidioides occurs through inhalation or inoculation of spores, "
   "respectively: inhaled spores infect the lungs, and spores inoculated into the skin infect the skin. Rural farm "
   "workers and harvesters are most at risk."),
  [("Inhalation of spores from soil dust",
    "Inhalation is the route to the lung infection, not the skin infection. The two routes map one to one: "
    "inhalation gives lung disease, and inoculation of spores into the skin gives skin disease.",
    "routes swapped"),
   ("Spread from an infected family member",
    "Most fungal pathogens need no host to complete their life cycles and are generally not communicable; "
    "person-to-person spread is a feature of dermatophytes and Candida. Paracoccidioides skin infection follows "
    "inoculation of spores.",
    "assumes person-to-person spread"),
   ("Eating crops from contaminated soil",
    "Ingestion is the route of fungal toxins (mycotoxicoses such as aflatoxin), not of Paracoccidioides. Its two "
    "routes are inhalation of spores (lung infection) and inoculation of spores (skin infection).",
    "mycotoxin route")],
  c(12, 37, 65)),

Q("Paracoccidioides", IO1,
  "Which person fits the risk profile for paracoccidioidomycosis?",
  ("Poorly nourished male farm worker over 40",
   "Correct. In the cool, humid soils of Central and South America, rural farm workers and harvesters are most at "
   "risk; poor nutrition is a predisposing factor, and male sex and age over 40 add to the risk. All of those clues "
   "are present here."),
  [("Shoeless male farmer aged 11 to 30",
    "A male farmer aged 11 to 30 who goes without shoes fits the eumycetoma profile, deep tissue infections of poor "
    "countries. Paracoccidioidomycosis strikes poorly nourished rural farm workers over 40.",
    "eumycetoma profile"),
   ("Rose gardener with a thorn puncture",
    "A thorn puncture in a gardener is the classic route of sporotrichosis, 'rose-gardener's disease'. The "
    "paracoccidioidomycosis profile is a poorly nourished male farm worker over 40.",
    "Sporothrix profile"),
   ("Older road worker in desert dust",
    "Increasing age and occupational dust exposure, as in road construction, are risk factors for Coccidioides in "
    "hot, semiarid climates. Paracoccidioides strikes poorly nourished male farm workers over 40 in cool, humid "
    "Central and South America.",
    "Coccidioides profile")],
  c(30, 37, 39, 64)),

Q("Paracoccidioides", IO1,
  "Which description fits paracoccidioidomycosis?",
  ("Rarest primary mycosis, usually mild",
   "Correct. Paracoccidioidomycosis, endemic in Central and South America (mainly the cool, humid soils of Brazil, "
   "Colombia, Venezuela, Argentina and Paraguay), is the rarest of the primary mycoses; systemic disease is not "
   "common, and infections are usually mild and self-limiting."),
  [("Commonest primary mycosis, usually mild",
    "Mildness is right, but rarity is reversed: the most common true fungal pathogen is Histoplasma capsulatum, "
    "cause of 'Ohio Valley fever', while Paracoccidioides causes the rarest of the primary mycoses.",
    "rarity reversed (Histoplasma's ranking)"),
   ("Rarest primary mycosis, usually systemic",
    "Rarity is right, but severity is overstated: systemic paracoccidioidomycosis is not common. Lung or skin "
    "infections, from inhaled or inoculated spores, are usually mild and self-limiting.",
    "severity overstated"),
   ("An opportunist needing impaired defenses",
    "Paracoccidioides is a primary (true) fungal pathogen of rural farm workers, not an opportunist defined by "
    "impaired defenses. It causes the rarest primary mycosis, usually mild and self-limiting.",
    "true pathogen taken for an opportunist")],
  ci(13, 5, 7, 26, 37)),

]
