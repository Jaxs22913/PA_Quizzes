# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 16 — Food Safety (Dr. Fair, 30 October 2026), pool A: slides 2-21 and 30-31:
# microbes in food production (bread, beer and wine, pickling, milk and dairy, microbes as food, fungi), the burden
# of foodborne illness (agents, agencies, symptoms, under-reporting), food intoxication against food infection,
# Escherichia coli, Salmonella and Campylobacter jejuni. Pool B (tools/micro_l16_pool_b.py) holds Listeria onward
# (slides 22-36) and the tracking items.
#
# DECK: "PAJ5200.FoodSafety-micro.pptx", title slide "Significant Microorganisms in Food Safety", 36 slides.
#
# PHASE 1, FROM THE SLIDES ALONE (the recording is not yet transcribed). Every key and every explanation is from
# the VISIBLE slides, text and pictures; the speaker notes (slides 2, 6, 8, 16, 18, 25) are never used.
# Picture-only content used: slide 10 (the symptom set), slide 12 (food intoxication against food infection:
# can of food -> cells and toxin -> ingestion -> target organs, brain and muscle; poultry -> improper cooking
# technique -> bacteria multiply in food -> ingestion -> intestinal infection), slide 14 (the eosin methylene
# blue plate, quiz picture l16-fig-01.jpg), slide 20 (the Mary Mallon poster: warned, given an explanation,
# persisted, caused multiple deadly outbreaks; she is drawn cooking), slide 21 (the Campylobacter cycle:
# chickens -> water -> cattle -> milk -> people; water -> people; chickens -> poultry meat -> people).
#
# Four options throughout. Keys short, explanations full (EXPLAIN_DEEP.md). Every key is authored at position 0
# with the only "Correct." opener; the partition rotates positions per set. `mis` names the misconception each
# distractor stands for (review metadata; the renderer strips it). No numeric (ordered) option sets.
#
# OBJECTIVE 3 ("public concern and antibiotic resistant strains") has no slide content: no item is written for it.
#
# DELIBERATELY NOT ASKED (held), and why:
#   - every count and percentage as a key: 250 pathogens, 75 million cases, 5000 deaths (slide 9, whose
#     "worldwide" label is disputed), 7% of spinach (slide 16), the 500-cell figure is used only as "a very low
#     infectious dose" (slide 21, the blueprint's own fact).
#   - outbreak and recall DATES and BRAND or COMPANY names (slides 16, 18, 22): the foods are asked, never the year
#     or the brand. The beer history (6000 BCE) and the 5000-year cheese history (slides 5, 7) are trivia.
#   - the Salmonella species list and the city-named strains (slide 17): not keyed. The deck's "S. enteriditis" is
#     never written.
#   - slide 11 (two bismuth subsalicylate packages and a black tongue, no text): brand product, no stated fact.
#   - slide 20's two agar plates (unlabeled; no stated medium or organism).
#   - the brewing steps (malting, mashing, wort and hops, lagering, filtration, slide 5): a process list with no
#     stated microbial role per step.
#   - Lactobacillus sanfrancisco (slide 4) is not keyed (outdated species name).
# SPELLING: "mould" never appears; US spelling throughout.
SRC = "PAJ5200.FoodSafety-micro.pptx"


def c(*n):
    return f"{SRC}, Slide " + (str(n[0]) if len(n) == 1 else ", ".join(map(str, n[:-1])) + " and " + str(n[-1]))


def ci(img, *n):
    """cite with a picture slide: c(n...) + ' and image on Slide img'"""
    return (c(*n) + f" and image on Slide {img}") if n else f"{SRC}, image on Slide {img}"


IO1 = "1 — Identify sources of microbial contamination in global food supply"
IO2 = ("2 — Correlate associations between contaminated foods with the increasing numbers of diagnosed food-borne "
       "illnesses and mortality worldwide")
IO4 = ("4 — Correlate associations between improved laboratory analytical methods with respect to near-daily "
       "announcements of food recalls and food-related illness")
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

# ============================================================== MICROBES IN FOOD PRODUCTION (slides 3-8, 31)
Q("Microbes in food production", IO1,
  "Which of these is a beneficial effect of microbes on food?",
  ("Fermentation that improves its texture",
   "Correct. Beneficial effects are those in which food is fermented or otherwise chemically changed by microbes "
   "or their products to alter or improve its flavor, taste or texture. Fermentation that improves texture fits "
   "that description, whereas spoilage and microbial toxins are detrimental effects."),
  [("Spoilage that gives it an off smell",
    "Spoilage is a detrimental effect, not a beneficial one: it renders food unfit to eat through undesirable "
    "flavors, appearance or smell. A beneficial effect is a change that improves the food, such as fermentation "
    "that alters its flavor, taste or texture.", "detrimental effect mistaken for a benefit"),
   ("Presence that leaves the food unchanged",
    "Microbes that neither cause disease nor change the nature of the food are a neutral effect: they are just "
    "there and are eaten with the food. A beneficial effect changes the food for the better, as fermentation "
    "does.", "neutral effect confused with a beneficial one"),
   ("A toxin produced while it is stored",
    "A microbial toxin in food is a detrimental effect that leads to food intoxication; it does not improve the "
    "food. The beneficial category is fermentation or another microbial change that improves flavor, taste or "
    "texture.", "food intoxication mistaken for a benefit")],
  c(3, 9)),

Q("Microbes in food production", IO1,
  "In bread making, what do microbial enzymes acting on gluten give the dough?",
  ("Elasticity that makes it workable",
   "Correct. Conditioning is one of the three microbial functions in bread making: microbial enzymes act on "
   "gluten to give the dough elasticity, making it pliable and workable. Leavening (by gases) and flavor and "
   "aroma (by organic acids and alcohols) are the other two functions."),
  [("Rise from carbon dioxide gas",
    "Rise is leavening, a separate function driven mainly by carbon dioxide and other gases, not by enzymes "
    "acting on gluten. The enzymes condition the dough instead, giving it elasticity so it is pliable and "
    "workable.", "leavening confused with conditioning"),
   ("Flavor from organic acids",
    "Flavor and aroma come from organic acids and alcohols, the second microbial function in bread making. "
    "Enzyme action on gluten is the third function, conditioning, which gives the dough its elasticity.",
    "flavor function confused with conditioning"),
   ("Preservation, as a salt brine does",
    "Salt brine preserves vegetable material in pickling; preservation is not one of the bread-making functions. "
    "In bread, microbial enzymes acting on gluten condition the dough, giving it elasticity so it can be worked.",
    "pickling fact borrowed into bread making")],
  c(4, 6)),

Q("Microbes in food production", IO1,
  "When yeast ferments glucose to make beer or wine, which two products form?",
  ("Ethanol and carbon dioxide",
   "Correct. In the fermentation equation for alcoholic beverages, one glucose molecule fermented by yeast gives "
   "two ethanol molecules and two carbon dioxide molecules. Ethanol is the alcohol in beer and wine; carbon "
   "dioxide is also the main gas that leavens bread dough."),
  [("Lactic acid and carbon dioxide",
    "Lactic acid belongs to pickling, where it may be present in the salt brine with vinegar and spices; it is "
    "not a product of the brewing equation. Yeast fermentation of glucose yields ethanol and carbon dioxide.",
    "pickling product placed in alcoholic fermentation"),
   ("Ethanol and oxygen",
    "Oxygen is not a product of the equation. Yeast turns glucose into ethanol and carbon dioxide, and carbon "
    "dioxide is the gas given off, the same gas that does most of the leavening in bread dough.",
    "wrong gas in the fermentation equation"),
   ("Organic acids and water",
    "Organic acids, with alcohols, are what microbes add to the flavor and aroma of bread dough, and water does "
    "not appear in the brewing equation. Yeast fermentation of glucose gives ethanol and carbon dioxide.",
    "bread flavor products confused with brewing products")],
  c(4, 5, 6)),

Q("Microbes in food production", IO1,
  "When plant material is chewed before it is brewed, what supplies the yeast for its fermentation?",
  ("Human saliva",
   "Correct. For some alcoholic beverages the source of the fermenting yeast is human saliva: the plant material "
   "is chewed (masticated) before the brewing. People themselves are then the source of the microbes that "
   "ferment the drink."),
  [("Human skin and nose",
    "Bacteria and fungi from human skin, nose and mouth are the likely accidental source of the first fermented "
    "dairy products, not of chewed-plant brewing. When plant material is chewed first, the yeast comes from the "
    "chewer's saliva.", "dairy contamination source borrowed into brewing"),
   ("Milking utensils",
    "Milking utensils introduce microbes into milk, which begins sterile; they play no part in brewing chewed "
    "plant material. In that process, the chewing step itself adds yeast from human saliva.",
    "milk contamination route borrowed into brewing"),
   ("Raw honey",
    "Honey is named as a place where spores of clostridia can be found, a food safety concern rather than a "
    "source of brewing yeast. Chewing the plant material before brewing supplies the yeast from human saliva.",
    "spore source confused with a fermentation source")],
  c(5, 7, 25)),

Q("Microbes in food production", IO1,
  "Milk begins as a sterile mixture. How do microbes first get into it?",
  ("On leaving the animal and from utensils",
   "Correct. Milk begins as a sterile mixture of water, minerals, protein, butterfat, lactose and other sugars; "
   "microbes are introduced as it exits the female mammal's body and by milking utensils. Once contaminated it is "
   "highly susceptible to microbial growth because of its nutrient density."),
  [("They are already present in the udder",
    "This contradicts the starting point: milk is a sterile mixture while still inside the animal. Microbes are "
    "introduced as it exits the female mammal's body and by milking utensils, and its nutrient density then lets "
    "them grow.", "milk assumed contaminated inside the animal"),
   ("From yeast in human saliva",
    "Saliva is the yeast source for some alcoholic beverages made from chewed plant material, not the route into "
    "fresh milk. Microbes enter milk as it exits the female mammal's body and from milking utensils.",
    "brewing yeast source borrowed into dairy"),
   ("When cheese molds are added to it",
    "Molds, with yeast and bacteria, are used in cheese-making, an induced fermentation that comes later; adding "
    "them is not how microbes first reach fresh milk. That happens as milk exits the body and from milking "
    "utensils.", "induced fermentation mistaken for the first contamination")],
  c(5, 7)),

Q("Microbes in food production", IO1,
  "Which of these fermented foods is a plant product rather than a fermented milk?",
  ("Soy sauce",
   "Correct. Soybeans and their extracts are fermented to make tofu and soy sauce (shoyu), so soy sauce is a "
   "fermented plant product, like pickled vegetables. Kefir, koumiss and buttermilk are fermented milk products, "
   "grouped with yogurt."),
  [("Kefir",
    "Kefir is a fermented milk product, named with koumiss and buttermilk as relatives of yogurt. The fermented "
    "plant product among these choices is soy sauce, made by fermenting soybeans or their extracts.",
    "unfamiliar dairy name taken for a plant product"),
   ("Koumiss",
    "Koumiss is a fermented milk product, grouped with kefir and buttermilk. Fermented plant products include soy "
    "sauce and tofu from soybeans, and vegetables pickled in salt brine.",
    "unfamiliar dairy name taken for a plant product"),
   ("Buttermilk",
    "Buttermilk is a fermented milk product, as its name suggests, grouped with kefir and koumiss. Soy sauce, "
    "made by fermenting soybeans or their extracts, is the plant product here.",
    "fermented dairy product misclassified")],
  c(6, 7)),

Q("Microbes in food production", IO1,
  "How does the acceptance of microbial additives differ between animal feed and human food?",
  ("Used in feed; slower to be accepted for people",
   "Correct. Microbial additives for animal feed are already used, but human versions are slower to be accepted. "
   "Single cell protein and other bacterial or fungal products are still being researched, although the "
   "cyanobacterium Spirulina is already added to some foods in the United States."),
  [("Used in human food; slower for animal feed",
    "This reverses the pattern. Microbial additives are already used in animal feed; it is the human versions "
    "that are slower to be accepted, with single cell protein and similar products still being researched.",
    "reversed direction of acceptance"),
   ("Accepted equally in both feed and food",
    "Acceptance is not equal. Additives for animal feed are already in use, while human versions lag behind and "
    "are slower to be accepted, although Spirulina is already added to smoothies and vitamin supplement gummies.",
    "assumes equal uptake"),
   ("Still being researched for both",
    "Research (for example on single cell protein) describes the human side; microbial additives for animal feed "
    "are already used. The two differ: feed has taken them up, while human versions are slower to be accepted.",
    "research stage applied to feed as well")],
  c(8)),

Q("Microbes in food production", IO1,
  "Spoilage of bread, cereals and acidic juices is associated with which group of microbes?",
  ("Fungi",
   "Correct. Fungi do not commonly cause disease, but they are associated with both food production and food "
   "spoilage, and the foods they spoil include bread, cereals and acidic juices. The same group gives mushrooms "
   "for food, penicillin for medicine and yeasts for fermenting many products."),
  [("Protozoa",
    "Protozoa such as Cryptosporidium, Cyclospora, Giardia and Entamoeba cause mild, usually self-limiting diarrhea "
    "from uncooked produce or drinking water; they are not the spoilers of bread and cereals. That role belongs "
    "to fungi.", "non-bacterial pathogen confused with a spoilage organism"),
   ("Clostridia",
    "Certain Clostridium species take part in bread making, and clostridial spores occur in soil, on plants and "
    "in honey; they are not the organisms associated with spoiling bread, cereals and acidic juices. Those are "
    "fungi.", "bread-making bacterium mistaken for a bread spoiler"),
   ("Cyanobacteria",
    "The cyanobacterium Spirulina is eaten as food, added to smoothies and vitamin supplement gummies; "
    "cyanobacteria are not linked to spoiling bread, cereals or acidic juices. Fungi are the spoilage organisms "
    "for those foods.", "microbe eaten as food confused with a spoiler")],
  c(4, 8, 25, 31, 32)),

Q("Microbes in food production", IO1,
  "Which bacteria are involved in turning milk into yogurt?",
  ("Lactobacillus and Streptococcus",
   "Correct. Yogurt is a type of fermented milk made with bacteria such as Lactobacillus and Streptococcus. "
   "Cheese-making, by contrast, draws on yeast, bacteria and molds (multicellular fungi), and kefir, koumiss and "
   "buttermilk are other fermented milks."),
  [("Saccharomyces and Clostridium",
    "Saccharomyces cerevisiae (baker's yeast, a fungus) and certain Clostridium species are microbes of bread "
    "making, not of yogurt. Yogurt fermentation involves bacteria such as Lactobacillus and Streptococcus.",
    "bread microbes borrowed into dairy"),
   ("Spirulina and other cyanobacteria",
    "Spirulina is a cyanobacterium eaten directly as food, in smoothies and vitamin supplement gummies; it is not "
    "used to ferment milk. The bacteria involved in yogurt are Lactobacillus and Streptococcus.",
    "microbe eaten as food confused with a fermenter"),
   ("Escherichia coli and Salmonella",
    "These are foodborne pathogens: Escherichia coli is an indicator organism of fecal contamination, and "
    "Salmonella is associated mainly with poultry and aquatic reptiles. Yogurt is made with Lactobacillus and "
    "Streptococcus.", "pathogens mistaken for fermenters")],
  c(4, 7, 8, 15, 17, 31)),

# ============================================================== FOODBORNE ILLNESS BURDEN (slides 9, 10, 13, 30)
Q("Foodborne illness burden", IO1,
  "Which type of microbe is the most common among foodborne pathogens?",
  ("Bacteria",
   "Correct. Of the estimated 250 different foodborne pathogens, bacteria are the most common. Viruses, parasites "
   "and toxins produced by microorganisms are concerns as well, and fungi, protozoa and parasitic worms are the "
   "other organisms involved, but none of these outnumber the bacteria."),
  [("Viruses",
    "Viruses such as norovirus are a common foodborne agent, spread person to person and through contaminated "
    "shellfish, but they are not the most common type of foodborne pathogen. Bacteria are.",
    "a common foodborne virus taken as the commonest pathogen type"),
   ("Fungi",
    "Fungi do not commonly cause disease; they matter more in food production and in food spoilage (bread, "
    "cereals, acidic juices). Bacteria are the most common foodborne pathogens.",
    "spoilage organisms mistaken for the main pathogens"),
   ("Protozoa",
    "Protozoa such as Giardia and Cryptosporidium cause mild, usually self-limiting diarrhea from uncooked fruits "
    "and vegetables or drinking water, but they are not the most common foodborne pathogens. Bacteria hold that "
    "place.", "parasites overrated as the main foodborne cause")],
  c(9, 30, 31, 32, 33)),

Q("Foodborne illness burden", IO1,
  "A household eats no meat, eggs or dairy. Does that remove its risk of bacterial foodborne illness?",
  ("No; plant foods carry bacteria too",
   "Correct. The worry about bacteria covers food from both plant and animal sources. Escherichia coli outbreaks "
   "have come from bagged spinach and romaine lettuce, and Salmonella recalls have included watermelon, onions, "
   "cantaloupe and cucumbers, so avoiding animal foods does not remove the risk."),
  [("Yes; foodborne bacteria come from animal foods",
    "Animal foods are one source, but bacteria in plant foods are a concern too: Escherichia coli outbreaks have "
    "come from fecally contaminated vegetables such as spinach and romaine lettuce, and Salmonella recalls from "
    "onions and cucumbers.", "only meat, eggs and dairy carry foodborne bacteria"),
   ("Yes; produce carries protozoa, not bacteria",
    "Produce can carry protozoa (ready-to-eat salad bags are a common culprit), but it carries bacteria as well: "
    "Escherichia coli outbreaks from spinach and lettuce and Salmonella recalls of watermelon, onions and "
    "cucumbers.", "produce assumed to carry only parasites"),
   ("No; fungi on produce are the main risk",
    "Fungi do not commonly cause disease; they matter in food production and spoilage. The risk that remains on "
    "plant foods is bacterial, from organisms such as Escherichia coli and Salmonella, which have both caused "
    "produce outbreaks or recalls.", "spoilage fungi mistaken for the main hazard")],
  c(9, 15, 16, 18, 31, 32)),

Q("Foodborne illness burden", IO4,
  "Which food safety responsibility rests with the Food and Drug Administration and the United States "
  "Department of Agriculture rather than with local and state health departments?",
  ("Enforcing food safety law and policy",
   "Correct. Local and state health departments, the Centers for Disease Control and Prevention, the Food and "
   "Drug Administration and the United States Department of Agriculture all conduct surveillance and investigate "
   "outbreaks, but the Food and Drug Administration and the United States Department of Agriculture are in charge "
   "of law enforcement and policy enactment."),
  [("Conducting food safety surveillance",
    "Surveillance is shared: local and state health departments, the Centers for Disease Control and Prevention "
    "and other agencies are all tasked with it. What the Food and Drug Administration and the United States "
    "Department of Agriculture add is enforcing food safety law and enacting policy.",
    "shared surveillance role taken as the distinguishing one"),
   ("Investigating illness outbreaks",
    "Outbreak investigation is shared with local and state health departments and the Centers for Disease "
    "Control and Prevention. What sets the Food and Drug Administration and the United States Department of "
    "Agriculture apart is law enforcement and policy enactment.",
    "shared investigative role taken as the distinguishing one"),
   ("Hosting the PulseNet database",
    "PulseNet, the database of pulsed-field gel electrophoresis patterns for microbial isolates, is run through "
    "the Centers for Disease Control and Prevention, not these two agencies. The Food and Drug Administration and "
    "the United States Department of Agriculture enforce food safety law and enact policy.",
    "Centers for Disease Control and Prevention tool credited to the enforcing agencies")],
  c(9, 34, 35)),

Q("Foodborne illness burden", IO2,
  "How do recorded counts of foodborne illness compare with the true number of cases?",
  ("They are probably too low",
   "Correct. The yearly estimate of foodborne illness is described as probably an under-reported number, and "
   "Campylobacter jejuni illness in particular is very much under-reported. Many people who fall ill are never "
   "counted, so recorded counts likely understate the true burden."),
  [("They are probably too high",
    "The direction is reversed. Foodborne illness numbers are described as probably under-reported, meaning real "
    "cases outnumber recorded ones; Campylobacter jejuni illness is singled out as very much under-reported.",
    "reversed direction (over-counting)"),
   ("They match closely, thanks to surveillance",
    "Surveillance by health departments and federal agencies helps, and tracking reduces detection time and the "
    "number of cases, but the counts are still described as probably under-reported. The true number of cases is "
    "likely higher than the record.", "surveillance assumed to capture every case"),
   ("Low for viruses, accurate for bacteria",
    "Under-reporting is not limited to viruses: Campylobacter jejuni, a bacterium, is very much under-reported, "
    "and the overall foodborne count, in which bacteria are the most common pathogens, is probably "
    "under-reported as well.", "bacterial illness assumed to be fully counted")],
  c(9, 21, 34)),

Q("Foodborne illness burden", IO2,
  "Which set of complaints makes up the common symptoms of foodborne illness?",
  ("Diarrhea, cramps, nausea, vomiting and fever",
   "Correct. The symptoms of foodborne illness are diarrhea, abdominal cramps, nausea, vomiting and fever. "
   "Escherichia coli, for example, causes nausea, vomiting and diarrhea, and Bacillus cereus intoxication causes "
   "self-resolving vomiting and abdominal cramps."),
  [("Muscle paralysis and respiratory failure",
    "Paralysis of the muscles in the relaxed position, leading to respiratory failure, follows ingested "
    "botulinum toxin; it is a specific, severe outcome rather than the common picture. Foodborne illness "
    "typically brings diarrhea, abdominal cramps, nausea, vomiting and fever.",
    "a specific toxin's effect taken as the general picture"),
   ("Septicemia, shock and kidney dysfunction",
    "These are among the severe forms salmonellosis can take, alongside gastroenteritis and enteric fever; they "
    "are not the common symptom set. Foodborne illness typically brings diarrhea, abdominal cramps, nausea, "
    "vomiting and fever.", "severe complications taken as typical"),
   ("Infection of the placenta and fetus",
    "Spread from the intestine through the bloodstream to the placenta and fetus is the specific pathway of "
    "Listeria monocytogenes, which is why pregnant women are at greatest risk from it. The common symptoms are "
    "diarrhea, cramps, nausea, vomiting and fever.", "an invasive Listeria pathway taken as typical")],
  ci(10, 15, 17, 23, 24, 27, 28)),

Q("Foodborne illness burden", IO1,
  "Besides live bacteria, viruses and parasites, which microbial product in food is a food safety concern?",
  ("Toxins made by microorganisms",
   "Correct. Beyond bacteria in food from plant and animal sources, the concerns include viruses, parasites and "
   "toxins that can be produced by microorganisms. A toxin already formed in the food causes food intoxication, "
   "as staphylococcal toxin and Clostridium botulinum toxin do."),
  [("Lactic acid in a pickling brine",
    "Lactic acid may be present in the salt brine used for pickling, part of a beneficial fermentation that "
    "preserves vegetables. The microbial product named among food safety concerns is toxin, which can be produced "
    "by microorganisms in food.", "beneficial fermentation product mistaken for a hazard"),
   ("Enzymes that condition bread dough",
    "Microbial enzymes acting on gluten condition bread dough, giving it elasticity so it is pliable and "
    "workable; that is a beneficial effect. Toxins produced by microorganisms are the microbial product counted "
    "among food safety concerns.", "beneficial enzymes mistaken for a hazard"),
   ("Carbon dioxide from fermentation",
    "Carbon dioxide from yeast fermentation leavens bread and is a product of brewing; it is beneficial, not a "
    "hazard. The microbial product that threatens food safety is toxin, as with staphylococcal or botulinum "
    "toxin.", "beneficial fermentation gas mistaken for a hazard")],
  c(4, 5, 6, 9, 12)),

# ============================================================== INTOXICATION VS INFECTION (slide 12)
Q("Intoxication vs infection", IO2,
  "In food intoxication, what does a person swallow that causes the illness?",
  ("Toxin already formed in the food",
   "Correct. In food intoxication, bacteria in the food release toxin before it is eaten; the person ingests that "
   "preformed toxin, which passes from the gut to its target organs. Staphylococcal toxin and Clostridium "
   "botulinum toxin are the examples."),
  [("Live bacteria that then multiply in the gut",
    "That is food infection: live cells are ingested and cause an intestinal infection, as with Salmonella or "
    "Listeria. In intoxication the harm comes from toxin already present in the food when it is eaten.",
    "infection mechanism given for intoxication"),
   ("Viral particles shed by a food handler",
    "Viral particles, as with norovirus spread by feces and vomitus, are a viral foodborne route, not food "
    "intoxication. Intoxication means swallowing a microbial toxin already formed in the food, such as "
    "staphylococcal toxin.", "viral spread confused with intoxication"),
   ("Fungal spores that spoil the food",
    "Fungi are associated with food spoilage (bread, cereals, acidic juices) and do not commonly cause disease. "
    "Food intoxication is caused by a toxin already formed in the food, such as staphylococcal or botulinum "
    "toxin.", "spoilage confused with intoxication")],
  ci(12, 12, 31, 33)),

Q("Intoxication vs infection", IO2,
  "Which pairing lists a food intoxication agent first and a food infection agent second?",
  ("Staphylococcal toxin, then Salmonella",
   "Correct. Staphylococcal toxin is an example of food intoxication, in which a preformed toxin is ingested, and "
   "Salmonella is an example of food infection, in which live cells are ingested and cause an intestinal "
   "infection. The other pairings reverse the order or pair two agents of the same kind."),
  [("Listeria, then botulinum toxin",
    "This reverses the order: Listeria is a food infection agent (live cells ingested), and Clostridium botulinum "
    "toxin is a food intoxication agent (preformed toxin ingested). The intoxication agent has to come first.",
    "categories reversed"),
   ("Salmonella, then Listeria",
    "Both are food infection agents: live Salmonella or Listeria cells are eaten and cause an intestinal "
    "infection. Neither is an intoxication agent, so this pair cannot put one first.",
    "two infection agents"),
   ("Staphylococcal toxin, then botulinum toxin",
    "Both are food intoxication agents: staphylococcal toxin and Clostridium botulinum toxin are ingested already "
    "formed. The second agent should be a food infection agent, such as Salmonella or Listeria.",
    "two intoxication agents")],
  ci(12, 12)),

Q("Intoxication vs infection", IO2,
  "A chicken dish carrying Salmonella gives the diner gastroenteritis. Which kind of foodborne illness is this?",
  ("Food infection",
   "Correct. Salmonella is a named example of food infection: live cells in a food such as poultry are ingested "
   "and cause an intestinal infection, with improper cooking technique letting them multiply in the food first. "
   "Gastroenteritis is one of the forms salmonellosis can take."),
  [("Food intoxication",
    "Food intoxication is the ingestion of a toxin already formed in the food, as with staphylococcal or "
    "Clostridium botulinum toxin, which then acts on target organs. Salmonella is an example of the other kind: "
    "live cells that cause an intestinal infection.", "intoxication and infection confused"),
   ("Food spoilage",
    "Spoilage renders food unfit to eat through undesirable flavors, appearance or smell; it is not an illness. "
    "Live Salmonella eaten in a chicken dish and causing gastroenteritis is food infection.",
    "spoilage confused with illness"),
   ("A neutral microbial effect",
    "A neutral effect means microbes are present but neither cause disease nor change the food; they are simply "
    "eaten with it. This diner became ill from live Salmonella, which makes it a food infection.",
    "harmful microbe taken as a neutral one")],
  ci(12, 3, 12, 17)),

Q("Intoxication vs infection", IO2,
  "In the food infection pathway, which step lets bacteria multiply in the food before it is eaten?",
  ("Improper cooking technique",
   "Correct. In food infection, live cells in a food such as poultry come through improper cooking technique and "
   "multiply in the food; the larger number is then ingested and causes an intestinal infection. Salmonella and "
   "Listeria are the examples of this pattern."),
  [("Thorough cooking to 165 F",
    "Cooking meat thoroughly, checked with a meat thermometer at 165 F rather than by guessing, is a preventive "
    "step, not the one that lets bacteria multiply. In the infection pathway, improper cooking technique is what "
    "allows the cells to grow in the food.", "preventive step mistaken for the hazard"),
   ("Toxin release into the food",
    "Toxin release into the food is the intoxication pathway, in which the preformed toxin is ingested and "
    "reaches target organs. In food infection, live cells multiply in the food after improper cooking technique.",
    "intoxication step placed in the infection pathway"),
   ("Ingestion of the cooked food",
    "Ingestion comes after the bacteria have already multiplied; it delivers them to the intestine, where they "
    "cause infection. The step that lets them multiply in the food is improper cooking technique.",
    "sequence of steps confused")],
  ci(12, 12, 36)),

Q("Intoxication vs infection", IO2,
  "After a preformed toxin is swallowed in food intoxication, where does it act?",
  ("Target organs such as brain and muscle",
   "Correct. In food intoxication the ingested toxin passes through the gut to its target organs, such as the "
   "brain and the muscles. Botulinum toxin is an example: it paralyzes muscles in the relaxed position, which can "
   "lead to respiratory failure."),
  [("The intestine, where it starts an infection",
    "An intestinal infection is the end point of food infection, where live cells that multiplied in the food "
    "are ingested. A toxin swallowed in food intoxication is not an infection; it passes on to its target organs.",
    "infection end point given for intoxication"),
   ("The liver and spleen, via the blood",
    "Spread through the bloodstream to the liver, spleen, brain, placenta and fetus is the path of Listeria "
    "monocytogenes, a live-cell food infection. A preformed toxin acts on its target organs, such as the brain "
    "and muscles.", "Listeria spread borrowed"),
   ("Lymph nodes, after invading the gut wall",
    "Invasion of the intestinal wall with spread to the blood and lymph nodes describes typhoid fever, caused by "
    "live Salmonella typhi. A preformed toxin in food intoxication travels to target organs such as the brain and "
    "muscles.", "typhoid invasion borrowed")],
  ci(12, 12, 17, 24, 27)),

Q("Intoxication vs infection", IO2,
  "What must happen for a food infection, as opposed to a food intoxication, to occur?",
  ("Live bacterial cells must be ingested",
   "Correct. Food infection depends on live cells: bacteria in the food, which multiply there after improper "
   "cooking technique, are ingested and cause an intestinal infection, as with Salmonella or Listeria. "
   "Intoxication needs only the toxin that is already in the food."),
  [("A toxin must be formed before eating",
    "A toxin formed in the food before it is eaten defines food intoxication, as with staphylococcal or "
    "botulinum toxin. Food infection instead requires live bacterial cells to be ingested.",
    "intoxication requirement given for infection"),
   ("The toxin must reach target organs",
    "A toxin traveling from the gut to target organs such as the brain and muscles is the intoxication pathway. "
    "Food infection ends in an intestinal infection caused by the live cells that were ingested.",
    "intoxication end point given for infection"),
   ("Spores must germinate in the soil",
    "Spores of clostridia sit in soil, on plants and in honey, and germinating Clostridium botulinum spores can "
    "start producing toxin, which leads toward intoxication. Food infection requires live cells to be ingested.",
    "spore biology confused with infection")],
  ci(12, 12, 25, 27)),

# ============================================================== ESCHERICHIA COLI (slides 14, 15, 16)
Q("Escherichia coli", IO4,
  "A water sample streaked on this eosin methylene blue plate produced the growth shown. Which organism are such "
  "plates often used to confirm in food and water samples?",
  ("Escherichia coli",
   "Correct. Eosin methylene blue plates are often used to confirm Escherichia coli in samples such as food and "
   "water. Finding it matters because Escherichia coli is an indicator organism associated with human and animal "
   "feces."),
  [("Salmonella",
    "Salmonella is associated mainly with poultry and aquatic reptiles and is traced through foods such as eggs, "
    "peanut butter and poultry products. The organism eosin methylene blue plates are used to confirm in food and "
    "water is Escherichia coli.", "another enteric foodborne pathogen"),
   ("Listeria monocytogenes",
    "Listeria monocytogenes is found in birds and mammals, persists in soil and grows from 1 to 40 C; it is not "
    "the organism these plates confirm. Eosin methylene blue plates are used to confirm Escherichia coli in food "
    "and water samples.", "another major foodborne pathogen"),
   ("Campylobacter jejuni",
    "Campylobacter jejuni is tied to raw poultry and its leftovers and has an infectious dose under 500 cells; it "
    "is not what these plates confirm. Eosin methylene blue plates confirm Escherichia coli in food and water "
    "samples.", "another poultry-linked foodborne pathogen")],
  ci(14, 14, 15, 17, 18, 21, 23),
  img=IMG + "/l16-fig-01.jpg",
  alt="A Petri dish of dark reddish-brown agar with several streaks of bacterial growth that show a metallic "
      "green sheen.",
  slide="Slide 14"),

Q("Escherichia coli", IO1,
  "Escherichia coli serves as an indicator organism. Contamination with what does its presence in a food or "
  "water sample signal?",
  ("Human or animal feces",
   "Correct. Escherichia coli is an indicator organism associated with human and animal feces, so finding it in "
   "food or water points to fecal contamination. Its sporadic outbreaks likewise come from fecally contaminated "
   "meats or vegetables."),
  [("Soil and plant material",
    "Soil and plants are where spores of clostridia are found, along with honey, and Listeria monocytogenes "
    "persists in soil. Escherichia coli as an indicator organism points instead to contamination with human or "
    "animal feces.", "spore-former habitat confused with the fecal indicator"),
   ("Ocean or estuarine water",
    "Salt-tolerant Vibrio species live in ocean and estuarine waters; that habitat is not what Escherichia coli "
    "indicates. As an indicator organism it is associated with human and animal feces.",
    "Vibrio habitat confused with the fecal indicator"),
   ("Spoiled bread or cereal",
    "Bread, cereals and acidic juices are foods that fungi spoil; Escherichia coli is not a spoilage marker. Its "
    "presence as an indicator organism signals contamination with human or animal feces.",
    "spoilage confused with fecal contamination")],
  c(14, 15, 23, 25, 29, 31)),

Q("Escherichia coli", IO1,
  "Escherichia coli is found everywhere, including inside healthy humans. What explains its presence without "
  "disease?",
  ("Not every strain is pathogenic",
   "Correct. Escherichia coli is found everywhere, including inside humans, but it is not always pathogenic and "
   "has many good traits too. Illness comes from the bad strains, which can carry numerous toxins (for example "
   "enterotoxigenic or enterohemorrhagic strains)."),
  [("It survives as dormant spores",
    "Spore formation belongs to the clostridia, Gram-positive rods whose spores are found in soil, on plants and "
    "in honey. Escherichia coli lives in healthy people because not every strain is pathogenic.",
    "spore biology borrowed from Clostridium"),
   ("Its illness takes weeks to appear",
    "An incubation that can last from hours to weeks is a feature of salmonellosis, not the reason Escherichia "
    "coli lives in healthy people. The explanation is that not every strain is pathogenic, and the organism has "
    "good traits too.", "Salmonella incubation borrowed"),
   ("It spoils food rather than infecting",
    "Escherichia coli is not a spoilage organism; fungi are the microbes associated with spoiling bread, cereals "
    "and acidic juices. As an infectious agent it causes nausea, vomiting and diarrhea, but only its bad strains "
    "are harmful.", "pathogen mistaken for a spoilage organism")],
  c(15, 17, 25, 31)),

Q("Escherichia coli", IO2,
  "Which illness picture does Escherichia coli typically cause as an infectious agent?",
  ("Nausea, vomiting and diarrhea",
   "Correct. As an infectious agent, Escherichia coli causes nausea, vomiting and diarrhea, the familiar "
   "gastrointestinal picture of foodborne illness. Its bad strains can carry numerous toxins, and the O157:H7 "
   "serotype is one of the worst culprits."),
  [("Muscle paralysis and respiratory failure",
    "Paralysis of muscles in the relaxed position, leading to respiratory failure, follows ingestion of "
    "Clostridium botulinum toxin. Escherichia coli as an infectious agent causes nausea, vomiting and diarrhea.",
    "botulism picture borrowed"),
   ("Enteric fever spreading to lymph nodes",
    "Enteric fever with invasion of the intestinal wall and spread to the blood and lymph nodes is typhoid fever, "
    "caused by Salmonella typhi. Escherichia coli as an infectious agent causes nausea, vomiting and diarrhea.",
    "typhoid picture borrowed"),
   ("Infection of a seawater-exposed wound",
    "Wound infection from water is one of the two routes of vibriosis, caused by salt-tolerant Vibrio species in "
    "ocean and estuarine waters. Escherichia coli as an infectious agent causes nausea, vomiting and diarrhea.",
    "Vibrio wound route borrowed")],
  c(15, 17, 27, 29)),

Q("Escherichia coli", IO2,
  "Which kinds of Escherichia coli strains carry numerous toxins that make them harmful?",
  ("Enterotoxigenic and enterohemorrhagic strains",
   "Correct. Escherichia coli is not always pathogenic, but its bad strains can carry numerous toxins; "
   "enterotoxigenic and enterohemorrhagic strains are the examples. The O157:H7 serotype is one of the worst "
   "culprits in outbreaks."),
  [("Spore-forming strains from soil and honey",
    "Spores found in soil, on plants and in honey belong to the clostridia, Gram-positive rods; they are not a "
    "kind of Escherichia coli. The toxin-carrying Escherichia coli strains are enterotoxigenic and "
    "enterohemorrhagic strains.", "Clostridium features borrowed"),
   ("Salt-tolerant strains from estuarine water",
    "Salt tolerance in ocean and estuarine waters describes Vibrio species, not harmful Escherichia coli. The bad "
    "Escherichia coli strains carrying numerous toxins are enterotoxigenic and enterohemorrhagic strains.",
    "Vibrio features borrowed"),
   ("Fermenting strains used in yogurt making",
    "Yogurt is made with bacteria such as Lactobacillus and Streptococcus, not Escherichia coli. The harmful "
    "Escherichia coli strains carrying numerous toxins are enterotoxigenic and enterohemorrhagic strains.",
    "beneficial fermenters confused with toxin strains")],
  c(7, 15, 25, 29)),

Q("Escherichia coli", IO2,
  "Which group of foods has been linked to Escherichia coli outbreaks?",
  ("Ground beef, spinach and lettuce",
   "Correct. Sporadic Escherichia coli outbreaks originate from fecally contaminated meats or vegetables: "
   "hamburgers and ground beef, bagged spinach and romaine lettuce are among the recorded sources, along with "
   "cookie dough and raw milk cheese."),
  [("Peanut butter, eggs and pet food",
    "Peanut butter, eggs and pet food are sources of Salmonella, together with poultry products, live backyard "
    "poultry and sushi-grade seafood. Escherichia coli outbreaks have come from ground beef, spinach and romaine "
    "lettuce.", "Salmonella vehicles"),
   ("Fried rice and other rice dishes",
    "Rice is often associated with the emetic form of Bacillus cereus food poisoning, which has a rapid onset of "
    "6 hours or less. Escherichia coli outbreaks have come from fecally contaminated meats and vegetables such as "
    "ground beef and spinach.", "Bacillus cereus vehicle"),
   ("Ice cream and smoked seafood",
    "Ice cream recalls and smoked seafood point to Listeria monocytogenes, which grows well even at refrigerator "
    "temperatures. Escherichia coli outbreaks have come from ground beef, spinach and romaine lettuce.",
    "Listeria vehicles")],
  c(15, 16, 18, 23, 28)),

Q("Escherichia coli", IO2,
  "The O157:H7 serotype, one of the worst culprits in foodborne outbreaks, belongs to which organism?",
  ("Escherichia coli",
   "Correct. One of the worst Escherichia coli culprits is the O157:H7 serotype. The bad Escherichia coli strains "
   "can carry numerous toxins, and outbreaks arise from fecally contaminated meats or vegetables such as "
   "hamburgers and bagged spinach."),
  [("Salmonella enterica",
    "Salmonella enterica is one of the main Salmonella species; other Salmonella strains are named for the places "
    "where they were first found. O157:H7 is not a Salmonella designation but a serotype of Escherichia coli.",
    "another enteric pathogen"),
   ("Listeria monocytogenes",
    "Listeria monocytogenes is a major foodborne pathogen found in birds and mammals and persisting in soil, but "
    "O157:H7 is not one of its designations. That serotype belongs to Escherichia coli.",
    "another major foodborne pathogen"),
   ("Vibrio vulnificus",
    "Vibrio vulnificus is a salt-tolerant species of ocean and estuarine waters, acquired through water or from "
    "shellfish and raw seafood. The O157:H7 serotype, one of the worst outbreak culprits, is Escherichia coli.",
    "seafood pathogen")],
  c(15, 16, 17, 23, 29)),

Q("Escherichia coli", IO1,
  "Beyond meats and vegetables, which food has also been a source of an Escherichia coli outbreak?",
  ("Raw milk cheese",
   "Correct. Escherichia coli outbreaks usually come from fecally contaminated meats or vegetables, but raw milk "
   "cheese and cookie dough also appear among the recorded sources. Milk begins sterile but picks up microbes as "
   "it leaves the animal and from milking utensils."),
  [("Eggs",
    "Eggs are a Salmonella source, alongside poultry products, peanut butter and pet food; they do not appear among "
    "the Escherichia coli outbreak foods. Beyond meats and vegetables, those include raw milk cheese and cookie "
    "dough.", "Salmonella vehicle"),
   ("Pet food",
    "Pet food appears among Salmonella sources, along with live backyard poultry and eggs; it is not among the "
    "Escherichia coli outbreak foods. Raw milk cheese is, beside the usual fecally contaminated meats and "
    "vegetables.", "Salmonella vehicle"),
   ("Raw honey",
    "Honey is where spores of clostridia can be found, a concern tied to Clostridium rather than Escherichia coli. "
    "Raw milk cheese is the food beyond meats and vegetables linked to an Escherichia coli outbreak.",
    "Clostridium spore source")],
  c(7, 15, 16, 18, 25)),

# ============================================================== SALMONELLA (slides 17-20)
Q("Salmonella", IO1,
  "Which animals are the main reservoirs of Salmonella?",
  ("Poultry and aquatic reptiles",
   "Correct. Salmonella bacteria are associated with many animals, mainly poultry and aquatic reptiles. Matching "
   "sources include poultry products (chicken, turkey, duck), eggs and live poultry such as backyard hens."),
  [("Birds and mammals, persisting in soil",
    "Birds and mammals, with persistence in soil, describe Listeria monocytogenes, the organism behind recalls of "
    "ice cream and cantaloupes. Salmonella is associated with many animals, but mainly with poultry and aquatic "
    "reptiles.", "Listeria reservoir borrowed"),
   ("Cattle that drink contaminated water",
    "Cattle drinking contaminated water and passing the organism on in milk appear in the Campylobacter jejuni "
    "transmission cycle. Salmonella's main reservoirs are poultry and aquatic reptiles.",
    "Campylobacter cycle borrowed"),
   ("Pigs and deer carrying worms",
    "Pork and venison can be contaminated while the animal is still alive, but that concerns parasitic worms such "
    "as tapeworm, roundworm and trichinosis. Salmonella is associated mainly with poultry and aquatic reptiles.",
    "parasite source borrowed")],
  ci(21, 17, 18, 23, 32)),

Q("Salmonella", IO2,
  "Which presentation is among the forms salmonellosis can take?",
  ("Septicemia, a blood infection",
   "Correct. Salmonellosis can appear as gastroenteritis, enteric fever, septicemia (blood infection), fever, "
   "shock and kidney dysfunction. Its most severe enteric fever is typhoid fever, in which the bacteria invade "
   "the intestinal wall and spread to the blood and lymph nodes."),
  [("Paralysis of relaxed muscles",
    "Paralysis of the muscles in the relaxed position, leading to respiratory failure, is caused by ingested "
    "botulinum toxin, not by Salmonella. Salmonellosis appears as gastroenteritis, enteric fever, septicemia, "
    "fever, shock or kidney dysfunction.", "botulism borrowed"),
   ("Hepatitis from the fecal-oral route",
    "Hepatitis A and E viruses are the ones typically spread by the fecal-oral route; hepatitis is not among the "
    "forms of salmonellosis, which include gastroenteritis, enteric fever, septicemia and kidney dysfunction.",
    "viral hepatitis borrowed"),
   ("Spread across the placenta",
    "Spread through the bloodstream to the placenta and fetus is the Listeria monocytogenes pathway, which is why "
    "pregnant women are most at risk from it. Salmonellosis forms include gastroenteritis, enteric fever, "
    "septicemia and kidney dysfunction.", "Listeria pathway borrowed")],
  ci(24, 17, 23, 27, 33)),

Q("Salmonella", IO2,
  "Which description fits the incubation period of salmonellosis?",
  ("As short as hours or as long as weeks",
   "Correct. One challenge with salmonellosis is that incubation can be as short as hours or as long as weeks, "
   "so the food responsible may have been eaten long before the illness begins. Bacillus cereus intoxication, by "
   "contrast, begins within 6 hours."),
  [("Consistently six hours or less",
    "A rapid onset of 6 hours or less, with self-resolving vomiting and abdominal cramps, describes Bacillus "
    "cereus intoxication. Salmonellosis incubation varies far more, from hours to weeks.",
    "Bacillus cereus onset borrowed"),
   ("Fixed at about two weeks",
    "The two-week figure belongs to hepatitis A and E, whose carriers are most contagious about two weeks before "
    "their symptoms appear; it is not a Salmonella incubation. Salmonellosis incubation ranges from hours to "
    "weeks.", "hepatitis timing borrowed"),
   ("Rapid, as with norovirus illness",
    "Norovirus illness is usually rapid in onset and short in duration, with nausea, vomiting, diarrhea and "
    "low-grade fever. Salmonellosis is not reliably rapid: its incubation can be as short as hours or as long as "
    "weeks.", "norovirus onset borrowed")],
  c(17, 28, 33)),

Q("Salmonella", IO2,
  "Which groups are at greatest risk from salmonellosis?",
  ("Young children and the elderly",
   "Correct. Young children and the elderly are at greatest risk from salmonellosis, which can appear as "
   "gastroenteritis, enteric fever, septicemia, fever, shock and kidney dysfunction. Pregnant women head the "
   "at-risk list for a different organism, Listeria monocytogenes."),
  [("Pregnant women and unborn children",
    "Pregnant women and unborn children head the at-risk list for listeriosis, along with premature babies, "
    "elderly people and the immunocompromised. For salmonellosis the groups at greatest risk are young children "
    "and the elderly.", "Listeria risk groups borrowed"),
   ("People with seawater-exposed wounds",
    "Wound infection from water is a route of vibriosis, caused by salt-tolerant Vibrio species in ocean and "
    "estuarine waters. The groups at greatest risk from salmonellosis are young children and the elderly.",
    "Vibrio route borrowed"),
   ("Cooks who handle raw poultry",
    "Handling raw poultry exposes cooks, but cooks are not the group at greatest risk; a cook can instead spread "
    "infection to others through food. Young children and the elderly are at greatest risk from salmonellosis.",
    "exposure mistaken for susceptibility")],
  ci(20, 17, 23, 29)),

Q("Salmonella", IO2,
  "What makes typhoid fever the most severe enteric fever?",
  ("Invasion of the gut wall, then blood and nodes",
   "Correct. Typhoid fever, caused by Salmonella typhi, is the most severe enteric fever: the bacteria invade "
   "the intestinal wall and can spread to the blood and lymph nodes. Other forms of salmonellosis include "
   "gastroenteritis, septicemia, fever, shock and kidney dysfunction."),
  [("A preformed toxin that paralyzes muscles",
    "A preformed toxin that paralyzes muscles describes botulinum toxin in food intoxication. Typhoid fever is an "
    "invasive Salmonella infection: the intestinal wall is invaded and bacteria spread to the blood and lymph "
    "nodes.", "intoxication mechanism borrowed"),
   ("Growth even at refrigerator temperatures",
    "Growth from 1 to 40 C, including refrigerator temperatures, is the biggest concern with Listeria "
    "monocytogenes. Typhoid fever is severe because Salmonella typhi invades the intestinal wall and spreads to "
    "the blood and lymph nodes.", "Listeria growth range borrowed"),
   ("A tiny dose of a few particles",
    "An infectious dose of only a few viral particles describes norovirus, not typhoid fever. Typhoid fever's "
    "severity comes from invasion of the intestinal wall, with spread to the blood and lymph nodes.",
    "norovirus dose borrowed")],
  c(17, 23, 27, 33)),

Q("Salmonella", IO2,
  "An illness cluster is traced to eggs from one farm and to a batch of peanut butter. Which organism do these "
  "sources point to?",
  ("Salmonella",
   "Correct. Eggs and peanut butter are both Salmonella sources, along with poultry products, pet food, live "
   "backyard poultry and sushi-grade seafood, and Salmonella recalls have included peanuts and peanut butter and "
   "farm eggs."),
  [("Escherichia coli O157:H7",
    "Escherichia coli outbreaks come from fecally contaminated meats or vegetables, such as hamburgers, spinach "
    "and romaine lettuce, not from eggs and peanut butter. Those two foods point to Salmonella.",
    "best-known outbreak organism assumed"),
   ("Listeria monocytogenes",
    "Listeria monocytogenes is tied to soft cheeses, deli meats, hot dogs, raw produce and ice cream, and grows "
    "at refrigerator temperatures; eggs and peanut butter are not among its foods. They are Salmonella sources.",
    "another recall-prone organism assumed"),
   ("Bacillus cereus",
    "Bacillus cereus food poisoning is associated with meat (the diarrheal form) and rice (the emetic form), "
    "especially in summertime. Eggs and peanut butter point instead to Salmonella.",
    "common food-poisoning agent assumed")],
  c(15, 16, 18, 22, 23, 28)),

Q("Salmonella", IO2,
  "Which fresh produce items have been recalled because of Salmonella?",
  ("Watermelon, onions and cucumbers",
   "Correct. Salmonella recalls have included pre-cut watermelon, onions, pre-cut cantaloupe, cucumbers and "
   "jalapeno peppers, so produce can carry it as well as poultry, eggs and peanut butter. Bagged spinach and "
   "romaine lettuce, by contrast, are Escherichia coli outbreak foods."),
  [("Bagged spinach and romaine lettuce",
    "Bagged spinach and romaine lettuce are recorded sources of Escherichia coli outbreaks, from fecal "
    "contamination of vegetables. The Salmonella produce recalls include watermelon, onions, cantaloupe, "
    "cucumbers and jalapeno peppers.", "Escherichia coli produce vehicles"),
   ("Frozen vegetables and ice cream",
    "Ice cream and frozen vegetables, along with cantaloupes, are large-scale recalls attributed to Listeria "
    "monocytogenes. Salmonella produce recalls include watermelon, onions, cucumbers and jalapeno peppers.",
    "Listeria recalls"),
   ("Mushrooms and truffles",
    "Mushrooms and truffles are macroscopic fungi eaten as food in their own right, and fungi do not commonly "
    "cause disease. They are not among the Salmonella recalls, which include watermelon, onions, cantaloupe, "
    "cucumbers and jalapeno peppers.", "fungal foods confused with recalled produce")],
  c(8, 16, 18, 23, 31)),

Q("Salmonella", IO1,
  "Why is Mary Mallon, known as Typhoid Mary, remembered in food safety?",
  ("She kept cooking despite warnings, causing outbreaks",
   "Correct. Mary Mallon was warned and given an explanation, yet she persisted in preparing food and caused "
   "multiple deadly outbreaks. Typhoid fever, caused by Salmonella typhi, is the most severe enteric fever, so a "
   "single person handling food could spread it widely."),
  [("Her backyard hens spread Salmonella to others",
    "Live poultry such as backyard hens is a Salmonella source, but that is not her story. Typhoid Mary was "
    "warned and given an explanation, yet persisted in preparing food and caused multiple deadly outbreaks.",
    "animal source confused with a human source"),
   ("She was the first person to die of typhoid",
    "She is remembered as a source of infection, not as its first victim: despite warnings and an explanation, "
    "she persisted and caused multiple deadly outbreaks of typhoid fever, the most severe enteric fever.",
    "victim confused with spreader"),
   ("She traced Salmonella to poultry and reptiles",
    "Linking Salmonella mainly to poultry and aquatic reptiles is a reservoir fact, not her part in food safety. "
    "Typhoid Mary is remembered for persisting despite warnings and causing multiple deadly outbreaks.",
    "investigator confused with spreader")],
  ci(20, 17, 18, 20)),

Q("Salmonella", IO1,
  "Which household exposure is a known source of Salmonella?",
  ("Keeping live backyard hens",
   "Correct. Live poultry such as backyard hens is a Salmonella source alongside poultry products, eggs and pet "
   "food, which fits its association mainly with poultry and aquatic reptiles. Raw honey and garden soil, by "
   "contrast, are where clostridial spores are found."),
  [("Moldy bread left in the pantry",
    "Mold on bread is fungal spoilage, and fungi do not commonly cause disease; moldy bread is not a Salmonella "
    "source. Live backyard poultry is, along with poultry products, eggs and pet food.",
    "spoilage fungi confused with a pathogen source"),
   ("Digging in garden soil",
    "Soil holds clostridial spores, and Listeria monocytogenes can persist in it; garden soil is not a Salmonella "
    "exposure here. Keeping live backyard hens is, since Salmonella is associated mainly with poultry.",
    "soil organisms borrowed"),
   ("Raw honey kept in the pantry",
    "Raw honey is where spores of clostridia can be found, a Clostridium concern rather than a Salmonella one. "
    "The household Salmonella exposure is live poultry such as backyard hens, matching its main poultry "
    "reservoir.", "Clostridium spore source borrowed")],
  c(17, 18, 23, 25, 31)),

# ============================================================== CAMPYLOBACTER (slide 21)
Q("Campylobacter", IO2,
  "Which foodborne bacterium is a leading cause of bacterial diarrheal disease each year in the United States?",
  ("Campylobacter jejuni",
   "Correct. Campylobacter jejuni is a leading cause of bacterial diarrheal disease each year in the United "
   "States, especially in children, and the illness is very much under-reported. Its infectious dose is under "
   "500 bacterial cells."),
  [("Listeria monocytogenes",
    "Listeria monocytogenes is singled out as the number one cause of food-related deaths in the United States, "
    "not as a leading cause of bacterial diarrheal disease. That description belongs to Campylobacter jejuni.",
    "leading cause of death confused with leading cause of diarrhea"),
   ("Clostridium botulinum",
    "Clostridium botulinum causes botulism, in which ingested toxin paralyzes muscles in the relaxed position and "
    "can lead to respiratory failure; it is not a leading diarrheal cause. Campylobacter jejuni is.",
    "severe toxin illness confused with common diarrhea"),
   ("Vibrio vulnificus",
    "Vibrio vulnificus is a salt-tolerant species acquired from water (ingested or through wounds) or from "
    "shellfish and raw seafood; it is not the leading cause of bacterial diarrheal disease. Campylobacter jejuni "
    "is.", "seafood pathogen")],
  c(21, 23, 27, 29)),

Q("Campylobacter", IO2,
  "Which set of symptoms is typical of Campylobacter jejuni illness?",
  ("Fever, headache, dizziness, bloody diarrhea",
   "Correct. Campylobacter jejuni illness brings fever, headache, dizziness and bloody diarrhea, usually rapid in "
   "onset. Even one drop of raw poultry fluid can be enough, since the infectious dose is under 500 cells."),
  [("Self-resolving vomiting and cramps",
    "Rapid, self-resolving vomiting and abdominal cramps within 6 hours describe Bacillus cereus intoxication. "
    "Campylobacter jejuni instead brings fever, headache, dizziness and bloody diarrhea.",
    "Bacillus cereus picture borrowed"),
   ("Spread to the placenta and fetus",
    "Spread through the bloodstream to the placenta and fetus is the Listeria monocytogenes pathway, which puts "
    "pregnant women at greatest risk. Campylobacter jejuni causes fever, headache, dizziness and bloody diarrhea.",
    "Listeria pathway borrowed"),
   ("Muscle paralysis and respiratory failure",
    "Paralysis of muscles in the relaxed position with respiratory failure follows ingested botulinum toxin. "
    "Campylobacter jejuni illness is marked instead by fever, headache, dizziness and bloody diarrhea.",
    "botulism borrowed")],
  ci(24, 21, 23, 27, 28)),

Q("Campylobacter", IO2,
  "Why can a single drop of raw poultry fluid be enough to cause Campylobacter jejuni illness?",
  ("Its infectious dose is under 500 cells",
   "Correct. The infectious dose of Campylobacter jejuni is less than 500 bacterial cells, so even one drop of "
   "raw poultry fluid can cause illness. That is why holiday poultry and its leftovers call for careful "
   "handling."),
  [("Its toxin is already formed in the fluid",
    "A toxin already formed in the food is food intoxication, as with staphylococcal or botulinum toxin. "
    "Campylobacter jejuni causes illness because so few live cells are needed: its infectious dose is under 500 "
    "cells.", "intoxication mechanism borrowed"),
   ("It grows even at refrigerator temperatures",
    "Growth from 1 to 40 C, including refrigerator temperatures, is the concern with Listeria monocytogenes. One "
    "drop of raw poultry fluid suffices for Campylobacter jejuni because fewer than 500 cells can cause illness.",
    "Listeria growth range borrowed"),
   ("Its spores survive in the raw fluid",
    "Spores belong to the clostridia, found in soil, on plants and in honey; they are not why a drop of poultry "
    "fluid is dangerous. The reason is Campylobacter jejuni's infectious dose of under 500 cells.",
    "spore biology borrowed")],
  c(12, 21, 23, 25)),

Q("Campylobacter", IO1,
  "Which food calls for particular care to prevent Campylobacter jejuni illness?",
  ("Poultry, including its leftovers",
   "Correct. Campylobacter jejuni comes with poultry: even one drop of raw poultry fluid can cause illness, and "
   "holiday poultry and its leftovers deserve particular care. In its transmission cycle, chickens and poultry "
   "meat lead to people."),
  [("Bagged ready-to-eat salads",
    "Ready-to-eat salad bags are a common culprit for protozoa such as Cryptosporidium, Cyclospora and Giardia, "
    "which cause mild, self-limiting diarrhea. The kitchen concern for Campylobacter jejuni is raw poultry and "
    "its leftovers.", "protozoan vehicle borrowed"),
   ("Peanut butter and peanuts",
    "Peanut butter is a Salmonella source, with recalls of peanuts and peanut butter; it is not linked to "
    "Campylobacter jejuni, whose concern is poultry, including holiday birds and their leftovers.",
    "Salmonella vehicle borrowed"),
   ("Cooked rice and rice dishes",
    "Rice is often associated with the emetic form of Bacillus cereus, a rapid-onset intoxication. Campylobacter "
    "jejuni is tied to poultry instead: a single drop of raw poultry fluid can cause illness.",
    "Bacillus cereus vehicle borrowed")],
  ci(21, 18, 21, 28, 32)),

Q("Campylobacter", IO1,
  "Besides poultry meat, which routes carry Campylobacter jejuni to people in its transmission cycle?",
  ("Contaminated water and milk from cattle",
   "Correct. In the Campylobacter jejuni cycle the organism passes from chickens into water; people are reached "
   "by poultry meat, by that water directly, and by milk from cattle that drink it. Each route begins with "
   "infected chickens."),
  [("Vomitus and person-to-person contact",
    "Spread person to person through feces and vomitus, as in daycares, nursing homes and cruise ships, describes "
    "norovirus. The Campylobacter jejuni cycle reaches people through poultry meat, water and milk from cattle.",
    "norovirus route borrowed"),
   ("Spores in soil and raw honey",
    "Spores in soil, on plants and in honey belong to the clostridia. Campylobacter jejuni reaches people through "
    "poultry meat, contaminated water and milk from cattle that drank that water.",
    "Clostridium source borrowed"),
   ("Wounds exposed to seawater",
    "Wound infection from water is a Vibrio route, from salt-tolerant species in ocean and estuarine waters. The "
    "Campylobacter jejuni cycle links chickens to people through poultry meat, water and milk from cattle.",
    "Vibrio route borrowed")],
  ci(21, 25, 29, 33)),

Q("Campylobacter", IO2,
  "Campylobacter jejuni is a leading cause of bacterial diarrheal disease in the United States. Which group does "
  "it especially affect?",
  ("Children",
   "Correct. Campylobacter jejuni is a leading cause of bacterial diarrheal disease each year in the United "
   "States, especially in children. Its fever, headache, dizziness and bloody diarrhea usually begin rapidly."),
  [("Pregnant women",
    "Pregnant women and unborn children are at greatest risk for listeriosis, because Listeria monocytogenes can "
    "spread to the placenta and fetus. Campylobacter jejuni is singled out as especially affecting children.",
    "Listeria risk group borrowed"),
   ("Raw oyster eaters",
    "Raw oysters, shellfish and crabs carry foodborne Vibrio species, salt-tolerant bacteria of ocean and "
    "estuarine waters. Campylobacter jejuni diarrheal disease especially affects children.",
    "Vibrio exposure borrowed"),
   ("Food handlers and cooks",
    "Food handlers can spread infection to others, as Typhoid Mary spread typhoid fever, but they are not the "
    "group Campylobacter jejuni especially affects. Its diarrheal disease is most notable in children.",
    "spreaders confused with the affected group")],
  ci(24, 20, 21, 23, 29)),

]
