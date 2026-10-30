# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 16 — Significant Microorganisms in Food Safety (Dr. Fair, 30 October 2026), pool B:
# slides 22-36 (Listeria, Clostridium, Bacillus cereus, Vibrio, fungi, protozoa and worms, foodborne viruses,
# tracking food safety, kitchen prevention), with slides 3, 6, 9, 12, 14, 17, 18, 20 and 21 used only as the
# replacing facts in explanations. Pool A (tools/micro_l16_pool_a.py) holds slides 2-21 and 30-31.
# PHASE 1, FROM THE SLIDES ALONE (the recording is not yet transcribed). Every key and every explanation rests on
# VISIBLE slide text or pictures; the speaker notes are never used. Picture content used: slide 12 (intoxication:
# toxin reaches target organs; infection: improper cooking, bacteria multiply in food, intestinal infection),
# slide 21 (the Campylobacter cycle), slide 24 (the Listeria spread diagram, quiz picture l16-fig-02.jpg),
# slide 26 (the raw honey label), slide 34 (the band-pattern image, quiz picture l16-fig-03.jpg).
#
# Four options throughout; every non-ordered key is authored at position 0 with the only "Correct." opener;
# `mis` names the misconception of each distractor. Objective 3 (public concern and antibiotic-resistant strains)
# has no slide content: no item asks it.
#
# DELIBERATELY NOT ASKED (held), and why:
#   - brand names, dates and places as keys (the 2016 ice cream recall brand, the 2019 poultry recall company and
#     town, "botox", Food Safety News and Food Safety Magazine, ServSafe): trivia. ServSafe and the recall
#     websites appear only as distractors or replacing facts.
#   - the 23 million norovirus cases a year (slide 33) and the Caliciviridae family name: a case count, and a
#     family name whose distractors would need outside knowledge.
#   - "grows easily at ... freezer temperatures" (slide 23): the same line gives the growth range as 1 to 40 C,
#     and a freezer is colder than 1 C, so the slide contradicts itself. Only the 1 to 40 C range and the
#     refrigerator and room temperatures are keyed; no item or explanation leans on freezer growth.
#   - "Foodborne and wound-borne botulism" as a which-routes item (slide 27): the slide names two forms and cannot
#     refute any other route a distractor would offer. Wound-borne botulism is used only as a replacing fact.
#   - the R-month rule as true (slide 29 says "maybe, maybe not"): keyed only as uncertain.
#   - Bacillus cereus heat stability, except the ONE item marked SLIDE-CONFLICT (slide 28 pairs the heat-stable
#     toxin with the diarrheal form and the heat-labile toxin with the emetic form; standard references give the
#     reverse). That item is keyed as the slide says, and its explanations say references differ.
# KEYED AS THE SLIDE SAYS (guide note where current figures differ): Listeria monocytogenes as the number one
# cause of food-related deaths in the United States (slide 23); 165 F on the meat thermometer (slide 36).
# SPELLING: Vibrio parahemolyticus (the deck's spelling) is never named; "E. coli" is written Escherichia coli.
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


POOL_B = [

# ============================================================== LISTERIA (slides 22, 23, 24)
Q("Listeria", IO1,
  "Where is Listeria monocytogenes found in nature?",
  ("Birds and mammals; it persists in soil",
   "Correct. Listeria monocytogenes is found in birds and mammals and can persist in soil. The foods most "
   "vulnerable to it include soft cheeses, deli meats, hot dogs, raw or undercooked meats, seafood and raw fruit "
   "and vegetables."),
  [("Salty ocean and estuarine waters",
    "Salt tolerance in ocean and estuarine waters describes the Vibrio species, which reach people through water "
    "or seafood. Listeria monocytogenes is carried by birds and mammals and persists in soil; seawater and "
    "shellfish point to Vibrio instead.", "adjacent organism's habitat (Vibrio)"),
   ("Spores in soil, on plants and in honey",
    "Spores in soil, on plants and in honey belong to the clostridia, which form spores. Listeria "
    "monocytogenes does persist in soil, but its carriers are birds and mammals; the spores and the honey are the "
    "tell for Clostridium.", "adjacent organism's reservoir (clostridial spores)"),
   ("A human carrier who cooks for others",
    "A cook who carries the organism and spreads it through food is the typhoid story of Typhoid Mary, who was "
    "warned, persisted and caused deadly outbreaks. Listeria monocytogenes is carried by birds and mammals and "
    "persists in soil.", "the carrier-cook story of Salmonella typhi")],
  c(23, 29, 25, 17, 20)),

Q("Listeria", IO1,
  "Large-scale recalls of ice cream and frozen vegetables have been traced to which bacterium?",
  ("Listeria monocytogenes",
   "Correct. Large-scale food recalls have been attributed to Listeria monocytogenes, including a big ice cream "
   "recall, cantaloupes, frozen vegetables and poultry. It grows well from 1 to 40 C, so refrigerator "
   "temperatures do not hold it back."),
  [("Vibrio vulnificus",
    "The foodborne route of Vibrio species is seafood: shellfish, crabs, raw seafood and oysters from salty ocean "
    "and estuarine waters. The ice cream and frozen vegetable recalls were attributed to Listeria monocytogenes.",
    "seafood organism"),
   ("Campylobacter jejuni",
    "Campylobacter jejuni is a leading cause of bacterial diarrheal disease, spread by raw poultry fluid and "
    "poultry leftovers. Large-scale recalls of ice cream and frozen vegetables were attributed to Listeria "
    "monocytogenes instead.", "adjacent foodborne bacterium (poultry)"),
   ("Bacillus cereus",
    "Bacillus cereus is a common summertime food poisoning agent tied to meat (diarrheal form) and rice (emetic "
    "form). The ice cream and frozen vegetable recalls belong to Listeria monocytogenes, which grows well from 1 to "
    "40 C.", "adjacent foodborne bacterium (rice and meat)")],
  ci(22, 23, 29, 21, 28)),

Q("Listeria", IO2,
  "How does Listeria monocytogenes cause illness after a contaminated food is eaten?",
  ("Live cells are ingested and multiply",
   "Correct. Listeria is an example of food infection: live cells are ingested and multiply, often after improper "
   "cooking lets the bacteria multiply in the food, and the result is an intestinal infection. From the intestine "
   "it can spread through a lymph node and the bloodstream."),
  [("Its preformed toxin reaches target organs",
    "A toxin already formed in the food that travels to target organs is food intoxication, as with staphylococcal "
    "toxin or Clostridium botulinum toxin. Listeria causes food infection: the live cells are eaten and multiply.",
    "intoxication confused with infection"),
   ("Its spores germinate and make toxin",
    "Spores that germinate and start producing toxin describe Clostridium botulinum, whose spores are found in "
    "soil, on plants and in honey. Listeria monocytogenes causes illness as live cells that are eaten and multiply.",
    "Clostridium botulinum mechanism"),
   ("It spoils the food's flavor and smell",
    "Spoilage makes food unfit through undesirable flavors, appearance or smell; it is a separate detrimental "
    "effect from foodborne illness. Listeria monocytogenes causes disease as a food infection, with live cells "
    "that multiply.", "spoilage confused with illness")],
  ci(12, 12, 3, 24, 25, 27)),

Q("Listeria", IO2,
  "Which group is named among those at greatest risk for both salmonellosis and listeriosis?",
  ("Elderly people",
   "Correct. Young children and the elderly are at greatest risk for salmonellosis. Pregnant women, unborn "
   "children, premature babies, elderly people and immunocompromised people are at greatest risk for "
   "listeriosis. The elderly are the group on both lists."),
  [("Pregnant women",
    "Pregnant women are at greatest risk for listeriosis, but the groups at greatest risk for salmonellosis are "
    "young children and the elderly. The elderly, not pregnant women, appear on both lists.",
    "listeriosis-only risk group"),
   ("Young children",
    "Young children are at greatest risk for salmonellosis, but the listeriosis list names unborn children and "
    "premature babies rather than young children. The elderly are the group the two lists share.",
    "salmonellosis-only risk group"),
   ("Immunocompromised people",
    "Immunocompromised people are among those at greatest risk for listeriosis, but the salmonellosis list names "
    "young children and the elderly. The elderly are the shared group.", "listeriosis-only risk group")],
  c(17, 23)),

Q("Listeria", IO2,
  "Which ranking does Listeria monocytogenes hold among foodborne agents in the United States?",
  ("Number one cause of food-related deaths",
   "Correct. Listeria monocytogenes is the number one cause of food-related deaths in the United States. The "
   "groups at greatest risk for listeriosis are pregnant women, unborn children, premature babies, elderly "
   "people and immunocompromised people."),
  [("Leading cause of bacterial diarrheal disease",
    "Being a leading cause of bacterial diarrheal disease in the United States, especially in children, is the "
    "ranking of Campylobacter jejuni. Listeria monocytogenes ranks first for food-related deaths.",
    "Campylobacter's ranking"),
   ("Cause of the most severe enteric fever",
    "The most severe enteric fever is typhoid fever, caused by Salmonella typhi, which invades the intestinal wall "
    "and spreads to the blood and lymph nodes. Listeria monocytogenes holds a different title: number one cause of "
    "food-related deaths.", "typhoid's ranking"),
   ("Very common summertime food poisoner",
    "Being a very common food poisoning agent, especially in summertime, describes Bacillus cereus, with its rapid, "
    "self-resolving vomiting and cramps. Listeria monocytogenes is singled out as the number one cause of "
    "food-related deaths in the United States.", "Bacillus cereus's description")],
  c(23, 21, 17, 28)),

Q("Listeria", IO1,
  "Why does keeping deli meats chilled fail to protect against Listeria monocytogenes?",
  ("It grows well from 1 to 40 C",
   "Correct. Probably the biggest concern with Listeria monocytogenes is that it grows well from 1 to 40 C, so it "
   "multiplies easily at refrigerator and room temperatures. Deli meats, soft cheeses, hot dogs and smoked "
   "seafood are among the foods most vulnerable to it."),
  [("Its spores survive in the cold",
    "Spores belong to the clostridia, which are spore-forming strict anaerobes found in soil, on plants and in "
    "honey. Listeria monocytogenes is a problem in chilled food because it keeps growing: it grows well from 1 to "
    "40 C.", "clostridial spores borrowed"),
   ("Its toxin forms before chilling",
    "A toxin made in the food before it is eaten is food intoxication, as with staphylococcal or botulinum toxin. "
    "Listeria monocytogenes causes food infection, and its cells keep multiplying in chilled food because it grows "
    "well from 1 to 40 C.", "intoxication confused with infection"),
   ("Its infectious dose is under 500 cells",
    "An infectious dose of fewer than 500 cells, so that one drop of raw poultry fluid can cause illness, is the "
    "Campylobacter jejuni figure, and it says nothing about cold. Listeria monocytogenes defeats chilling because "
    "it grows well from 1 to 40 C.", "Campylobacter's infectious dose")],
  c(23, 25, 12, 21)),

Q("Listeria", IO1,
  "Which set of foods is most vulnerable to Listeria monocytogenes?",
  ("Soft cheeses, deli meats, hot dogs",
   "Correct. The foods most vulnerable to Listeria monocytogenes are soft cheeses, raw fruit and vegetables, raw "
   "or undercooked meats, deli meats, seafood, smoked seafood, hot dogs and preserved meats. It also grows well "
   "at refrigerator temperatures, anywhere from 1 to 40 C."),
  [("Rice dishes kept warm on summer days",
    "Rice, especially in summertime, is the setting for the emetic form of Bacillus cereus food poisoning, with "
    "rapid, self-resolving vomiting and cramps. Listeria monocytogenes targets soft cheeses, deli meats, hot dogs "
    "and smoked seafood.", "Bacillus cereus foods"),
   ("Eggs, peanut butter and pet food",
    "Eggs, peanut butter and pet food are Salmonella sources, along with poultry products, live backyard poultry "
    "and sushi-grade seafood. The foods most vulnerable to Listeria monocytogenes include soft cheeses, deli meats "
    "and hot dogs.", "Salmonella foods"),
   ("Bread, cereals and acidic juices",
    "Bread, cereals and acidic juices are foods that fungi spoil; fungi do not commonly cause disease. Listeria "
    "monocytogenes is a disease-causing bacterium, and its most vulnerable foods include soft cheeses, deli meats "
    "and hot dogs.", "fungal spoilage foods")],
  c(23, 28, 18, 31)),

Q("Listeria", IO2,
  "The heading of this diagram has been removed. Which foodborne bacterium does it trace from contaminated food "
  "through the body?",
  ("Listeria monocytogenes",
   "Correct. The path from contaminated food through the intestine, a lymph node and the bloodstream to the liver "
   "and spleen, then on to the brain and across the placenta to the fetus, is the spread of Listeria "
   "monocytogenes. It explains why pregnant women and unborn children are at greatest risk."),
  [("Salmonella typhi",
    "Typhoid fever from Salmonella typhi does invade the intestinal wall and spread to the blood and lymph nodes, "
    "but its greatest-risk groups are young children and the elderly. The branch through the placenta to the "
    "fetus matches Listeria monocytogenes.", "typhoid spread (also blood and lymph nodes)"),
   ("Campylobacter jejuni",
    "The Campylobacter cycle runs from chickens, water, cattle and milk, and poultry meat to people, and its "
    "illness is rapid fever, headache, dizziness and bloody diarrhea. A path to the brain and through the "
    "placenta belongs to Listeria monocytogenes.", "adjacent foodborne bacterium"),
   ("Clostridium botulinum",
    "Botulism is a food intoxication: preformed toxin, not the bacterium itself, reaches the target organs and "
    "paralyzes muscles. A diagram of live bacteria moving through a lymph node, the blood, liver and spleen to the "
    "placenta is the infection route of Listeria monocytogenes.", "intoxication confused with infection")],
  ci(24, 23, 12, 17, 21, 27),
  img=IMG + "/l16-fig-02.jpg",
  alt="Diagram with arrows: cheese wedges labeled contaminated food, then an intestine, a lymph node and a "
      "bloodstream loop past the liver and spleen, then branches to the brain and to a placenta and fetus.",
  slide="Slide 24"),

Q("Listeria", IO2,
  "Why are unborn children among those at greatest risk from Listeria monocytogenes?",
  ("It can cross the placenta to the fetus",
   "Correct. Listeria monocytogenes passes from contaminated food through the intestine and a lymph node into the "
   "bloodstream, reaches the liver and spleen, and can then cross the placenta to the fetus. That spread is why "
   "pregnant women, unborn children and premature babies are at greatest risk."),
  [("Its toxin paralyzes fetal muscles",
    "Paralysis of muscles in the relaxed position, with respiratory failure, follows ingested botulinum toxin, a "
    "food intoxication. Listeria monocytogenes is a food infection: the bacterium itself spreads through the "
    "bloodstream and across the placenta to the fetus.", "botulism mechanism borrowed"),
   ("Its spores lie dormant in the womb",
    "Spore formation belongs to the clostridia, whose spores are found in soil, on plants and in honey. Listeria "
    "monocytogenes reaches the fetus as live bacteria traveling from the intestine through the bloodstream and "
    "across the placenta.", "clostridial spores borrowed"),
   ("It enters through skin wounds at birth",
    "Wound entry is a route for Vibrio infections from water and for wound-borne botulism. The risk to unborn "
    "children from Listeria monocytogenes comes before birth, as the bacterium crosses from the bloodstream through "
    "the placenta to the fetus.", "wound route borrowed (Vibrio, botulism)")],
  ci(24, 23, 25, 27, 29)),

# ============================================================== CLOSTRIDIUM (slides 25, 26, 27; 12)
Q("Clostridium", IO1,
  "Which description fits the clostridia?",
  ("Gram-positive, spore-forming strict anaerobes",
   "Correct. Clostridia are Gram-positive rods that are strict anaerobes and form spores. Their spores can be "
   "found in soils, associated with plants, or even in honey, and the food species are Clostridium botulinum and "
   "Clostridium perfringens."),
  [("Gram-negative, spore-forming strict anaerobes",
    "The spore-forming and strict-anaerobe parts are right, but clostridia are Gram-positive rods, not "
    "Gram-negative. Their spores are found in soils, associated with plants and even in honey.",
    "reversed Gram reaction"),
   ("Gram-positive, spore-forming strict aerobes",
    "Clostridia are strict anaerobes, the reverse of strict aerobes; the Gram-positive and spore-forming parts are "
    "right. They are Gram-positive rods whose spores turn up in soil, on plants and in honey.",
    "reversed oxygen requirement"),
   ("Gram-positive, non-spore-forming anaerobes",
    "Clostridia do form spores, and those spores are found in soils, associated with plants and even in honey. "
    "The full description is Gram-positive rods that are strict anaerobes and form spores.",
    "spore formation denied")],
  ci(25, 25, 26)),

Q("Clostridium", IO1,
  "Which two Clostridium species are not food-related?",
  ("Clostridium tetani and Clostridium difficile",
   "Correct. Of the notable clostridia, Clostridium tetani and Clostridium difficile are the two marked as not "
   "food-related. Clostridium botulinum and Clostridium perfringens are the food species, botulinum through the "
   "toxin behind foodborne botulism."),
  [("Clostridium botulinum and Clostridium perfringens",
    "These are the two food-related species: botulinum toxin causes foodborne botulism, and perfringens is listed "
    "with it. The species set apart as not food-related are Clostridium tetani and Clostridium difficile.",
    "food species taken for non-food species"),
   ("Clostridium botulinum and Clostridium tetani",
    "Clostridium tetani is not food-related, but Clostridium botulinum is a food species whose toxin causes "
    "foodborne botulism. The non-food pair is Clostridium tetani and Clostridium difficile.",
    "one food species mixed in (botulinum)"),
   ("Clostridium perfringens and Clostridium difficile",
    "Clostridium difficile is not food-related, but Clostridium perfringens is listed with Clostridium botulinum "
    "among the food species. The non-food pair is Clostridium tetani and Clostridium difficile.",
    "one food species mixed in (perfringens)")],
  c(25, 27)),

Q("Clostridium", IO1,
  "Besides soil and plants, in which food can clostridial spores be found?",
  ("Honey",
   "Correct. Spores of clostridia can be found in soils, associated with plants, or even in honey, including raw "
   "honey. When those spores germinate, Clostridium botulinum can start producing its toxin, and even a few "
   "bacteria can make plenty of it."),
  [("Rice",
    "Rice is often associated with the emetic form of Bacillus cereus illness, a common summertime food "
    "poisoning. Clostridial spores are found in soil, on plants and even in honey, the food that carries them.",
    "Bacillus cereus food"),
   ("Oysters",
    "Oysters, clams and mussels carry salt-tolerant Vibrio species from ocean and estuarine waters, the subject of "
    "the old 'R-month' rule. Clostridial spores are found in soil, on plants and even in honey.",
    "Vibrio food"),
   ("Eggs",
    "Eggs are a Salmonella source, along with poultry products, pet food, live backyard poultry, peanut butter and "
    "sushi-grade seafood. Clostridial spores are found in soil, on plants and even in honey.",
    "Salmonella food")],
  ci(26, 25, 27, 28, 29, 18)),

Q("Clostridium", IO2,
  "At what point does Clostridium botulinum start producing its toxin?",
  ("When its spores germinate",
   "Correct. When Clostridium botulinum spores germinate, they can start producing toxin, the botulinum toxin. The "
   "spores come from soil, plants or honey, and even if only a few bacteria are present they can produce plenty "
   "of the toxin."),
  [("When its cells form spores",
    "Spore formation is the reverse step: spores are the form found in soil, on plants and in honey. Clostridium "
    "botulinum starts producing toxin when its spores germinate, and even a few bacteria can make plenty of it.",
    "reversed sequence (sporulation for germination)"),
   ("After live cells reach the gut",
    "Live cells multiplying after they are eaten is food infection, as with Salmonella or Listeria. Botulinum toxin "
    "is made once the spores germinate, and botulism from food is an intoxication in which the toxin itself is "
    "ingested.", "infection confused with intoxication"),
   ("When it invades the gut wall",
    "Invasion of the intestinal wall, with spread to the blood and lymph nodes, is typhoid fever from Salmonella "
    "typhi. Clostridium botulinum harms through a toxin that it starts producing when its spores germinate.",
    "typhoid mechanism borrowed")],
  c(27, 25, 12, 17)),

Q("Clostridium", IO2,
  "How does ingested botulinum toxin lead to death?",
  ("Relaxed paralysis, then respiratory failure",
   "Correct. Ingesting botulinum toxin leads to paralysis of the muscles in the relaxed position, followed by "
   "respiratory failure and death. The toxin is made when spores germinate, and even a few Clostridium botulinum "
   "cells can produce plenty of it."),
  [("Rigid muscle spasm, then respiratory failure",
    "This reverses the paralysis: botulinum toxin paralyzes muscles in the relaxed position, not in a rigid spasm. "
    "Respiratory failure and death follow from that relaxed paralysis.", "reversed muscle state"),
   ("Spread through the blood to the brain",
    "Spread from the intestine through the bloodstream to the brain is the infection route of Listeria "
    "monocytogenes. Botulism is an intoxication: the toxin causes paralysis of muscles in the relaxed position, "
    "then respiratory failure.", "Listeria spread borrowed"),
   ("Invasion of the gut wall and blood",
    "Invasion of the intestinal wall, with spread to the blood and lymph nodes, is typhoid fever from Salmonella "
    "typhi. Botulinum toxin acts on muscles instead, paralyzing them in the relaxed position until breathing "
    "fails.", "typhoid mechanism borrowed")],
  ci(24, 27, 17)),

Q("Clostridium", IO2,
  "Why can food holding only a few Clostridium botulinum cells still cause botulism?",
  ("Small numbers produce plenty of toxin",
   "Correct. Even if there are only a few Clostridium botulinum bacteria present, they can produce plenty of the "
   "toxin. Ingesting that toxin paralyzes muscles in the relaxed position and leads to respiratory failure, so a "
   "small number of cells is enough to be dangerous."),
  [("Its spores multiply in the gut",
    "Spores are the dormant form found in soil, on plants and in honey; they germinate rather than multiply. "
    "Foodborne botulism comes from ingested toxin, and even a few Clostridium botulinum cells can make plenty "
    "of it.", "spores confused with growing cells"),
   ("Its infectious dose is under 500 cells",
    "An infectious dose of fewer than 500 cells, as little as one drop of raw poultry fluid, describes "
    "Campylobacter jejuni, a food infection. Botulism follows from the toxin: even a few Clostridium botulinum "
    "cells can produce plenty of it.", "Campylobacter's infectious dose"),
   ("It grows well from 1 to 40 C",
    "Growth from 1 to 40 C, including refrigerator temperatures, is the biggest concern with Listeria "
    "monocytogenes. The danger of a few Clostridium botulinum cells is their toxin: even a few bacteria can "
    "produce plenty of it.", "Listeria's growth range")],
  c(27, 25, 21, 23)),

Q("Clostridium", IO2,
  "Foodborne botulism is classed as which kind of foodborne illness?",
  ("Food intoxication",
   "Correct. In food intoxication the toxin is ingested and travels to its target organs; Clostridium botulinum "
   "toxin and staphylococcal toxin are the examples. Botulinum toxin paralyzes muscles in the relaxed position, "
   "leading to respiratory failure."),
  [("Food infection",
    "In food infection, live cells such as Salmonella or Listeria are ingested and multiply, often after improper "
    "cooking, causing intestinal infection. Foodborne botulism comes instead from ingesting the toxin itself.",
    "infection confused with intoxication"),
   ("Food spoilage",
    "Food spoilage makes food unfit to eat through undesirable flavors, appearance or smell, a detrimental effect "
    "separate from illness. Botulism is a food intoxication, in which ingested toxin reaches its target organs.",
    "spoilage confused with illness"),
   ("A neutral microbial effect",
    "A neutral effect is when microbes in food neither cause disease nor change the food; botulism is a deadly "
    "disease. Ingested botulinum toxin makes it a food intoxication, with paralysis and respiratory failure.",
    "neutral microbial presence")],
  ci(12, 12, 3, 27)),

# ============================================================== BACILLUS CEREUS (slide 28)
# SLIDE-CONFLICT: keyed per slide 28
Q("Bacillus cereus", IO2,
  "How do the two forms of Bacillus cereus gastroenteritis differ in the heat stability of their toxins?",
  ("Diarrheal heat-stable; emetic heat-labile",
   "Correct. The diarrheal form of Bacillus cereus illness is attributed to a heat-stable toxin, usually with meat, "
   "and the emetic form to a heat-labile toxin, often with rice. Many references give the reverse pairing; the "
   "pairing keyed here is diarrheal heat-stable, emetic heat-labile."),
  [("Diarrheal heat-labile; emetic heat-stable",
    "This is the reverse of the pairing keyed here, which puts the heat-stable toxin with the diarrheal, "
    "meat-associated form and the heat-labile toxin with the emetic, rice-associated form. Many references do "
    "describe it this way round, so know that the two versions exist.",
    "the reverse pairing found in many references"),
   ("Both forms from heat-stable toxins",
    "The two forms do not share one toxin type: the diarrheal form comes from a heat-stable toxin and the emetic "
    "form from a heat-labile toxin. That difference, with meat for the diarrheal form and rice for the emetic form, "
    "separates them.", "one toxin type for both forms"),
   ("Both forms from heat-labile toxins",
    "A heat-labile toxin is given for the emetic, rice-associated form only; the diarrheal, meat-associated form is "
    "attributed to a heat-stable toxin. The two forms differ in their toxins.", "one toxin type for both forms")],
  c(28)),

Q("Bacillus cereus", IO2,
  "Within a few hours of a summer picnic, several guests who ate fried rice develop vomiting and abdominal "
  "cramps. Which organism is the likely cause?",
  ("Bacillus cereus",
   "Correct. Bacillus cereus is a very common food poisoning agent, especially in summertime. Its emetic form is "
   "often associated with rice, and the intoxication has a rapid onset (6 hours or less) with vomiting and "
   "abdominal cramps that resolve on their own."),
  [("Campylobacter jejuni",
    "Campylobacter jejuni causes rapid fever, headache, dizziness and bloody diarrhea, usually from raw poultry "
    "fluid or poultry leftovers. Vomiting and cramps within hours of eating rice point to the emetic form of "
    "Bacillus cereus.", "adjacent foodborne bacterium (poultry)"),
   ("Listeria monocytogenes",
    "Listeria monocytogenes threatens pregnant women, unborn children, the elderly and immunocompromised people "
    "through soft cheeses, deli meats, hot dogs and raw produce. A rice dish with rapid vomiting and cramps fits "
    "Bacillus cereus.", "adjacent foodborne bacterium (soft cheese, deli meats)"),
   ("Clostridium botulinum",
    "Clostridium botulinum toxin causes paralysis of the muscles in the relaxed position and respiratory failure, "
    "not vomiting and cramps that pass. Rice, summertime and a rapid onset of vomiting point to Bacillus cereus.",
    "other intoxication (botulism)")],
  c(28, 21, 23, 27)),

Q("Bacillus cereus", IO1,
  "Which food is the diarrheal form of Bacillus cereus illness usually associated with?",
  ("Meat",
   "Correct. Bacillus cereus gastroenteritis is either diarrheal or emetic, and each form has its usual food: the "
   "diarrheal form is usually associated with meat, and the emetic form is often associated with rice."),
  [("Rice",
    "Rice goes with the other form: the emetic form of Bacillus cereus illness is often associated with rice. The "
    "diarrheal form is usually associated with meat, so the food is the clue to which form a person has.",
    "the two forms' foods swapped"),
   ("Honey",
    "Honey is where clostridial spores can turn up, along with soil and plants. The diarrheal form of Bacillus "
    "cereus illness is usually associated with meat, and the emetic form with rice.", "clostridial source"),
   ("Oysters",
    "Oysters, clams and mussels carry salt-tolerant Vibrio species from ocean and estuarine waters. The diarrheal "
    "form of Bacillus cereus illness is usually associated with meat, while the emetic form follows rice.",
    "Vibrio food")],
  c(28, 25, 29)),

QO("Bacillus cereus", IO2,
   "How soon after eating does Bacillus cereus intoxication typically begin?",
   [("6 hours or less",
     "Correct. Bacillus cereus intoxication has a rapid onset, 6 hours or less, with vomiting and abdominal cramps "
     "that resolve on their own. A rapid onset after a rice or meat dish, especially in summertime, fits this "
     "organism.", None),
    ("About 1 to 2 days",
     "A delay of a day or more is too slow: Bacillus cereus intoxication begins within 6 hours or less, with "
     "self-resolving vomiting and abdominal cramps. The rapid onset is part of what marks it.",
     "onset overestimated"),
    ("About 2 weeks",
     "Two weeks is the hepatitis timing: with the fecal-oral hepatitis viruses, a person is most contagious about "
     "two weeks before symptoms appear. Bacillus cereus intoxication begins within 6 hours or less of eating.",
     "hepatitis timing borrowed"),
    ("4 to 6 weeks",
     "Salmonella incubation can stretch from hours to weeks, but Bacillus cereus intoxication has a rapid onset of "
     "6 hours or less, then vomiting and cramps that resolve on their own.",
     "Salmonella's long incubation borrowed")],
   0, c(28, 33, 17)),

Q("Bacillus cereus", IO2,
  "Which course is typical of Bacillus cereus intoxication?",
  ("Self-resolving vomiting and cramps",
   "Correct. Bacillus cereus intoxication has a rapid onset (6 hours or less) with vomiting and abdominal cramps "
   "that resolve on their own. Its gastroenteritis takes a diarrheal form, usually with meat, or an emetic form, "
   "often with rice."),
  [("Fever, dizziness and bloody diarrhea",
    "Fever, headache, dizziness and bloody diarrhea of rapid onset describe Campylobacter jejuni, often from raw "
    "poultry. Bacillus cereus intoxication brings vomiting and abdominal cramps that resolve on their own.",
    "Campylobacter illness"),
   ("Muscle paralysis and respiratory failure",
    "Paralysis of muscles in the relaxed position leading to respiratory failure is botulism from Clostridium "
    "botulinum toxin. Bacillus cereus intoxication is milder: rapid vomiting and abdominal cramps that resolve "
    "on their own.", "botulism"),
   ("Fever with spread to blood and lymph nodes",
    "Invasion of the intestinal wall with spread to the blood and lymph nodes is typhoid fever, the most severe "
    "enteric fever, from Salmonella typhi. Bacillus cereus causes self-resolving vomiting and abdominal cramps.",
    "typhoid fever")],
  c(28, 21, 27, 17)),

Q("Bacillus cereus", IO2,
  "Which food-handling rule is given for preventing Bacillus cereus food poisoning?",
  ("Keep hot foods hot and cold foods cold",
   "Correct. Bacillus cereus is a very common food poisoning agent, especially in summertime, and the rule given "
   "against it is to keep hot foods hot and cold foods cold. Its intoxication starts rapidly, within 6 hours or "
   "less, with vomiting and cramps."),
  [("Skip oysters in months without an R",
    "The 'R-month' rule concerns oysters, clams and mussels and Vibrio, and it is now uncertain because aquaculture "
    "practices have advanced. For Bacillus cereus, the rule is to keep hot foods hot and cold foods cold.",
    "Vibrio shellfish rule"),
   ("Get a vaccine after a suspected exposure",
    "A vaccine in case of suspected exposure belongs to the hepatitis viruses spread by the fecal-oral route. "
    "Bacillus cereus is prevented by holding temperatures: keep hot foods hot and cold foods cold.",
    "hepatitis prevention"),
   ("Preserve food in salt brine with vinegar",
    "Salt brine, often with lactic acid, vinegar and spices, is used to pickle and preserve vegetables; it is a "
    "food-production method. The rule given for Bacillus cereus is to keep hot foods hot and cold foods cold.",
    "pickling taken for prevention")],
  c(28, 29, 33, 6)),

# ============================================================== VIBRIO (slide 29)
Q("Vibrio", IO1,
  "Where are Vibrio species such as Vibrio cholerae and Vibrio vulnificus found?",
  ("Ocean and estuarine waters",
   "Correct. Vibrio species, including Vibrio cholerae and Vibrio vulnificus, are salt-tolerant bacteria found in "
   "ocean and estuarine waters. People acquire them from that water, swallowed or through wounds, or from seafood "
   "such as shellfish, crabs and oysters."),
  [("Birds, mammals and soil",
    "Birds and mammals, with persistence in soil, describe Listeria monocytogenes. Vibrio species are salt-tolerant "
    "and live in ocean and estuarine waters, so their sources are seawater and seafood such as shellfish and "
    "oysters.", "Listeria reservoir"),
   ("Soil, plants and honey",
    "Soil, plants and honey are where clostridial spores are found. Vibrio species are salt-tolerant bacteria of "
    "ocean and estuarine waters, reaching people through water or through seafood such as shellfish and "
    "oysters.", "clostridial reservoir"),
   ("Poultry and aquatic reptiles",
    "Salmonella is found mainly with poultry and aquatic reptiles; the reptiles live in water, which makes this "
    "tempting. Vibrio species are the salt-tolerant bacteria of ocean and estuarine waters, carried by shellfish, "
    "crabs and raw seafood.", "Salmonella reservoir")],
  c(29, 23, 25, 17)),

Q("Vibrio", IO1,
  "A person with an open cut on the leg wades in salty estuarine water and develops a wound infection. Which "
  "genus is the likely cause?",
  ("Vibrio",
   "Correct. Vibrio species are salt-tolerant bacteria of ocean and estuarine waters, and one of their two major "
   "routes is water, either ingested or entering through wounds. Wading with an open cut in estuarine water fits "
   "the wound route of vibriosis."),
  [("Bacillus",
    "Bacillus cereus causes food poisoning after rice or meat dishes, with rapid, self-resolving vomiting and "
    "abdominal cramps. A wound infection after wading in salty estuarine water fits the water route of the "
    "salt-tolerant Vibrio species.", "adjacent foodborne bacterium (food poisoning)"),
   ("Listeria",
    "Listeria is carried by birds and mammals, persists in soil and causes illness through foods such as soft "
    "cheeses and deli meats. A wound infection after wading in salty estuarine water points to Vibrio.",
    "adjacent foodborne bacterium"),
   ("Salmonella",
    "Salmonella reaches people through poultry, eggs, peanut butter, pet food and live backyard poultry, causing "
    "gastroenteritis and enteric fever. A wound infection after wading in salty estuarine water fits Vibrio's "
    "water route.", "adjacent foodborne bacterium")],
  c(29, 28, 23, 17, 18)),

Q("Vibrio", IO2,
  "A person develops foodborne vibriosis. Which food most likely carried it?",
  ("Raw oysters",
   "Correct. The foodborne route of vibriosis runs through seafood: shellfish, crabs, raw seafood and oysters. "
   "Vibrio species are salt-tolerant and live in ocean and estuarine waters, the source of those foods."),
  [("Soft cheese",
    "Soft cheese is among the foods most vulnerable to Listeria monocytogenes, along with deli meats, hot dogs and "
    "smoked seafood. Foodborne vibriosis comes from shellfish, crabs, raw seafood and oysters.", "Listeria food"),
   ("Fried rice",
    "Rice is often associated with the emetic form of Bacillus cereus food poisoning, which starts within 6 hours "
    "or less. Vibrio reaches people through seafood such as shellfish, crabs and raw oysters.",
    "Bacillus cereus food"),
   ("Peanut butter",
    "Peanut butter has been a source of Salmonella, along with poultry, eggs, pet food and live backyard poultry. "
    "The foodborne route of Vibrio is seafood: shellfish, crabs, raw seafood and oysters.", "Salmonella food")],
  c(29, 23, 28, 18)),

Q("Vibrio", IO1,
  "What is the current standing of the 'R-month' rule against eating oysters, clams and mussels in May through "
  "August?",
  ("Uncertain, as aquaculture has advanced",
   "Correct. The 'R-month' rule says no oysters in May, June, July and August. Whether it still applies is "
   "uncertain (maybe, maybe not), because aquaculture practices have advanced so much that there are fewer worries "
   "about Vibrio in shellfish."),
  [("Still firm for shellfish every summer",
    "The rule is no longer firm: aquaculture practices have advanced so much that there are fewer worries, so "
    "whether it still applies is uncertain. Oysters, clams and mussels remain a foodborne route for Vibrio species.",
    "the rule taken as settled"),
   ("Dropped, as Vibrio is not salt-tolerant",
    "Vibrio species are salt-tolerant and found in ocean and estuarine waters, so that cannot be the reason. The "
    "rule is uncertain because aquaculture practices have advanced so much that there are fewer worries.",
    "reversed habitat fact"),
   ("Extended to every month of the year",
    "Extending it year-round reverses the trend: advanced aquaculture practices have brought fewer worries about "
    "shellfish, so even the May-to-August rule is now uncertain. Nothing points toward a stricter, all-year ban on "
    "oysters, clams and mussels.", "reversed direction")],
  c(29)),

Q("Vibrio", IO1,
  "What are the two major routes of vibriosis?",
  ("Water (ingested or wounds) and seafood",
   "Correct. Two major routes of vibriosis are known: water, either ingested or through wound infections, and "
   "food, such as shellfish, crabs, raw seafood and oysters. Both trace back to the salt-tolerant Vibrio species of "
   "ocean and estuarine waters."),
  [("Person-to-person contact and raw shellfish",
    "Person-to-person spread through feces and vomitus, plus contaminated shellfish, is the pattern of norovirus. "
    "Vibrio's two routes are water, ingested or through wounds, and food such as shellfish, crabs and raw oysters.",
    "norovirus routes"),
   ("Soil spores and wound contamination",
    "Spores in soil and wound-borne illness belong to the clostridia, whose spores also turn up on plants and in "
    "honey. Vibrio lives in ocean and estuarine waters; its routes are water (ingested or via wounds) and seafood.",
    "clostridial routes"),
   ("Infected live animals and pet feces",
    "Meat contaminated while the animal was still alive and domestic pet feces are the sources of tapeworm and "
    "roundworm. Vibrio is a salt-tolerant bacterium of ocean and estuarine waters, acquired from water or seafood.",
    "parasitic worm sources")],
  c(29, 33, 25, 27, 32)),

# ============================================================== FUNGI, PROTOZOA & WORMS (slides 30, 31, 32)
Q("Fungi, protozoa & worms", IO1,
  "Which statement describes the place of fungi in food safety?",
  ("Rarely disease, but production and spoilage",
   "Correct. Fungi do not commonly cause disease, but they are associated with both food production and food "
   "spoilage: mushrooms as food, yeasts for fermenting many products, penicillin in medicine, and spoilage of "
   "bread, cereals and acidic juices."),
  [("The most common foodborne pathogens",
    "Bacteria, not fungi, are the most common foodborne pathogens. Fungi do not commonly cause disease; they matter "
    "in food production (mushrooms, yeasts for fermenting) and in spoilage of bread, cereals and acidic juices.",
    "bacteria's ranking given to fungi"),
   ("Parasites best killed by thorough cooking",
    "Thorough cooking is the best way to kill tapeworm, roundworm and trichinosis, the parasitic worms. Fungi do "
    "not commonly cause disease; they are associated with food production and with spoilage of bread, cereals and "
    "acidic juices.", "parasitic worms"),
   ("Agents of mild diarrhea from drinking water",
    "Mild, usually self-limiting diarrhea from drinking water or uncooked produce is caused by protozoans such as "
    "Giardia and Cryptosporidium. Fungi do not commonly cause disease; they matter in food production and "
    "spoilage.", "protozoans")],
  ci(31, 31, 9, 32)),

Q("Fungi, protozoa & worms", IO2,
  "Foodborne Cryptosporidium, Cyclospora or Giardia typically causes which illness?",
  ("Mild diarrhea that is usually self-limiting",
   "Correct. The common foodborne protozoans, Cryptosporidium, Cyclospora, Giardia and Entamoeba, can all cause "
   "mild diarrhea that is usually self-limiting. It is associated with uncooked fruits and vegetables or drinking "
   "water."),
  [("Usually rapid bloody diarrhea with fever",
    "Rapid fever, headache, dizziness and bloody diarrhea describe Campylobacter jejuni, a bacterium spread by raw "
    "poultry fluid. The foodborne protozoans cause milder diarrhea that usually resolves on its own.",
    "Campylobacter illness"),
   ("Enteric fever spreading to the blood",
    "Enteric fever with spread to the blood and lymph nodes is typhoid fever from Salmonella typhi, which invades "
    "the intestinal wall. Protozoans such as Giardia and Cyclospora cause mild, usually self-limiting diarrhea.",
    "typhoid fever"),
   ("Paralysis of muscles in the relaxed position",
    "Paralysis of muscles in the relaxed position, then respiratory failure, follows ingested botulinum toxin. "
    "Foodborne protozoans such as Cryptosporidium cause mild diarrhea that usually resolves without that danger.",
    "botulism")],
  c(32, 21, 17, 27)),

Q("Fungi, protozoa & worms", IO1,
  "Foodborne protozoan diarrhea is associated with which sources?",
  ("Uncooked produce and drinking water",
   "Correct. Protozoans such as Cryptosporidium, Cyclospora, Giardia and Entamoeba cause mild diarrhea associated "
   "with uncooked fruits and vegetables or drinking water. Ready-to-eat salad bags are a common culprit of "
   "foodborne illness."),
  [("Undercooked pork and wild venison",
    "Venison and pork carry tapeworm, roundworm and trichinosis when the animal's muscle or organs were "
    "contaminated while it was alive. The protozoans are linked to uncooked fruits and vegetables and drinking "
    "water.", "parasitic worm sources"),
   ("Raw shellfish from salty estuaries",
    "Raw shellfish and other seafood from ocean and estuarine waters carry salt-tolerant Vibrio species. The "
    "foodborne protozoans travel instead in uncooked fruits and vegetables and in drinking water.",
    "Vibrio source"),
   ("Raw honey and the soil around plants",
    "Soil, plants and honey are where clostridial spores are found. Protozoans such as Giardia and Cyclospora cause "
    "mild diarrhea associated with uncooked fruits and vegetables or drinking water.", "clostridial source")],
  c(32, 29, 25)),

Q("Fungi, protozoa & worms", IO2,
  "How are tapeworm, roundworm and trichinosis in meat best killed?",
  ("Thorough cooking",
   "Correct. Tapeworm, roundworm and trichinosis are best killed by thorough cooking. Venison, pork or other meats "
   "can be contaminated while the animal is still alive, so the muscle or organ meat itself may carry the "
   "worms."),
  [("A mild bleach rinse",
    "Mild bleach cleaning solutions are for kitchen surfaces and utensils, not meat. Tapeworm, roundworm and "
    "trichinosis are best killed by thorough cooking, since the meat may have been contaminated while the animal "
    "was alive.", "surface cleaning applied to food"),
   ("Washing in hot, soapy water",
    "Hot, soapy water is for handwashing. Worms in venison or pork can sit in the animal's muscle or organ meat, "
    "contaminated while it was alive, and they are best killed by thorough cooking.",
    "handwashing applied to food"),
   ("A vaccine after exposure",
    "A vaccine in case of suspected exposure is given for the fecal-oral hepatitis viruses. For tapeworm, roundworm "
    "and trichinosis, the best protection is thorough cooking of the meat.", "hepatitis prevention")],
  c(32, 36, 33)),

Q("Fungi, protozoa & worms", IO1,
  "Venison and pork can carry parasitic worms even when butchered and handled cleanly. Why?",
  ("The animal was infected while alive",
   "Correct. Venison, pork or other meats can be contaminated while the animal is still alive, so the animal's "
   "muscle or organ meats may be suspect however cleanly they are handled later. Thorough cooking is the best way "
   "to kill tapeworm, roundworm and trichinosis."),
  [("Soil spores germinate in the meat",
    "Germinating spores from soil, plants or honey describe Clostridium botulinum, which then makes toxin. Worms in "
    "venison or pork come from the living animal, whose muscle or organ meat may already be contaminated.",
    "clostridial spores"),
   ("Worms multiply in the refrigerator",
    "Growth at refrigerator temperatures, across 1 to 40 C, is the biggest concern with Listeria monocytogenes. "
    "Worms in venison or pork come from the living animal, whose muscle or organ meat may already be "
    "contaminated.", "Listeria's cold growth borrowed"),
   ("Infected handlers shed them in vomitus",
    "Spread through feces and vomitus from person to person is norovirus. Clean handling rules out a handler as the "
    "source here; venison, pork and other meats can be contaminated while the animal is still alive.",
    "norovirus spread borrowed")],
  c(32, 27, 25, 23, 33)),

Q("Fungi, protozoa & worms", IO1,
  "Which household source can carry tapeworm and roundworm?",
  ("Domestic pet feces",
   "Correct. Domestic pet feces can contain tapeworm, roundworm and other parasitic worms. The other route to "
   "these worms is meat such as venison or pork contaminated while the animal was alive, and thorough cooking is "
   "the best way to kill them."),
  [("Raw honey in the pantry",
    "Raw honey is a place clostridial spores can be found, along with soil and plants. Tapeworm and roundworm in "
    "the home come from domestic pet feces, and in food from meat contaminated while the animal was alive.",
    "clostridial source"),
   ("Live backyard hens",
    "Live poultry such as backyard hens are a Salmonella source, along with poultry products, eggs and pet food. "
    "Tapeworm and roundworm at home come from domestic pet feces, and in food from meat contaminated while the "
    "animal was alive.", "Salmonella source"),
   ("Leftover rice dishes",
    "Rice is often associated with the emetic form of Bacillus cereus food poisoning, a bacterial intoxication. "
    "Tapeworm and roundworm are parasitic worms, and at home they come from domestic pet feces.",
    "Bacillus cereus food")],
  c(32, 25, 26, 18, 28)),

# ============================================================== FOODBORNE VIRUSES (slide 33)
Q("Foodborne viruses", IO2,
  "A brief illness of rapid onset, with nausea, vomiting, diarrhea and low-grade fever, passes from person to "
  "person through vomitus and feces on a cruise ship. Which agent is most likely?",
  ("Norovirus",
   "Correct. Norovirus, a Norwalk-like virus, spreads person to person through feces and vomitus, typically in "
   "daycares, nursing homes and cruise ships. Illness is usually rapid in onset and duration, with nausea, "
   "vomiting, diarrhea and low-grade fever."),
  [("Bacillus cereus",
    "Bacillus cereus also brings rapid vomiting and cramps, but it is a food intoxication from rice or meat "
    "dishes, not an illness passed between people through vomitus and feces. That spread, on cruise ships and in "
    "daycares and nursing homes, is norovirus.", "other rapid vomiting illness"),
   ("Campylobacter jejuni",
    "Campylobacter jejuni causes fever, headache, dizziness and bloody diarrhea from raw poultry fluid and "
    "leftovers; nothing here is bloody. Person-to-person spread by vomitus and feces on a cruise ship is the "
    "pattern of norovirus.", "adjacent foodborne bacterium"),
   ("Vibrio vulnificus",
    "Vibrio species reach people through ocean water or seafood such as oysters, so a cruise ship might seem to "
    "fit. Spread from person to person by vomitus and feces, as on cruise ships and in daycares and nursing homes, "
    "marks norovirus.", "seafood setting taken for the route")],
  c(33, 28, 21, 29)),

Q("Foodborne viruses", IO2,
  "Why does norovirus spread so readily in daycares and nursing homes?",
  ("A few viral particles can infect",
   "Correct. The infectious dose of norovirus is only a few viral particles, and it spreads person to person "
   "through feces and vomitus. Together these drive outbreaks in daycares, nursing homes and cruise ships."),
  [("It grows well in chilled food",
    "Growth from 1 to 40 C, including refrigerator temperatures, is the concern with Listeria monocytogenes. "
    "Norovirus spreads person to person through feces and vomitus, and its infectious dose is only a few viral "
    "particles.", "Listeria's cold growth borrowed"),
   ("Its spores survive in soil",
    "Spores in soil, on plants and in honey belong to the clostridia. Norovirus spreads person to person through "
    "feces and vomitus in daycares and nursing homes, and only a few viral particles are needed to cause illness.",
    "clostridial spores borrowed"),
   ("Its toxin forms before it is eaten",
    "A toxin preformed in food is food intoxication, as with staphylococcal or botulinum toxin. Norovirus is a "
    "virus passed person to person through feces and vomitus, and only a few viral particles are needed to cause "
    "illness.", "intoxication confused with a viral infection")],
  c(33, 23, 25, 12)),

Q("Foodborne viruses", IO1,
  "How can shellfish come to carry norovirus?",
  ("From feces-contaminated water",
   "Correct. Norovirus spreads mainly person to person through feces and vomitus, but it can also be spread by "
   "contaminated shellfish, which come from feces-contaminated water. Good handwashing, thorough cooking and clean "
   "drinking water are part of prevention."),
  [("From spores in soil and on plants",
    "Spores in soil, on plants and in honey are the clostridial form, and germinating spores make botulinum toxin. "
    "Norovirus reaches shellfish through water contaminated with feces.", "clostridial spores borrowed"),
   ("By natural growth in salty seawater",
    "Salt-tolerant growth in ocean and estuarine waters describes Vibrio species, a bacterial hazard of shellfish. "
    "Norovirus is a virus that reaches shellfish through water contaminated with feces.",
    "Vibrio habitat borrowed"),
   ("From infected animals while alive",
    "Contamination while the animal is still alive is the route of tapeworm, roundworm and trichinosis in venison "
    "and pork. Norovirus gets into shellfish through feces-contaminated water.", "parasitic worm route borrowed")],
  c(33, 25, 27, 29, 32)),

Q("Foodborne viruses", IO1,
  "Which two hepatitis viruses are typically spread by the fecal-oral route?",
  ("Hepatitis A and hepatitis E",
   "Correct. Of the hepatitis viruses A through E, hepatitis A and hepatitis E are the ones typically spread by the "
   "fecal-oral route, which makes them food and water threats. They are not spread by kissing, sneezing, saliva "
   "or blood."),
  [("Hepatitis B and hepatitis C",
    "Of the hepatitis viruses A through E, the two typically spread by the fecal-oral route are A and E, not B and "
    "C. That route is why handwashing, diaper hygiene, thorough cooking and clean drinking water prevent them.",
    "wrong pair"),
   ("Hepatitis A and hepatitis B",
    "Hepatitis A is right, but its fecal-oral partner is hepatitis E, not B. With the A and E pair, a person is "
    "most contagious about two weeks before symptoms appear, and neither is spread by kissing, sneezing, saliva or "
    "blood.", "half-right pair (B for E)"),
   ("Hepatitis C and hepatitis E",
    "Hepatitis E is right, but its fecal-oral partner is hepatitis A, not C. The A and E pair is prevented by good "
    "handwashing, diaper hygiene, thorough cooking and clean drinking water.", "half-right pair (C for A)")],
  c(33)),

Q("Foodborne viruses", IO2,
  "When is a person with hepatitis A most contagious?",
  ("About two weeks before symptoms",
   "Correct. With the fecal-oral hepatitis viruses, a person is most contagious about two weeks before symptoms "
   "appear. That silent window is why handwashing, diaper hygiene, thorough cooking and clean drinking water "
   "matter, and a vaccine exists for suspected exposure."),
  [("On the very first day of symptoms",
    "The most contagious time comes earlier, about two weeks before symptoms appear, so a person can spread "
    "hepatitis A before feeling ill. Waiting for symptoms misses that window.", "contagion tied to symptom onset"),
   ("At the height of the symptoms",
    "Contagiousness peaks before illness is visible, about two weeks before symptoms appear, not at the worst of "
    "the symptoms. That is why handwashing and diaper hygiene matter even around people who seem well.",
    "contagion tied to severity"),
   ("About two weeks after symptoms",
    "This reverses the timing: a person with hepatitis A is most contagious about two weeks BEFORE symptoms "
    "appear, not after. The fecal-oral route spreads it during that earlier window.", "reversed timing")],
  c(33)),

Q("Foodborne viruses", IO1,
  "Which measure helps prevent hepatitis A from spreading?",
  ("Handwashing and diaper hygiene",
   "Correct. Hepatitis A and E spread by the fecal-oral route, so prevention means good handwashing and diaper "
   "hygiene, cooking food thoroughly and drinking clean water. They are not spread by kissing, sneezing, saliva "
   "or blood, and a vaccine exists for suspected exposure."),
  [("Avoiding kissing and shared drinks",
    "Hepatitis A and E are not spread by kissing, sneezing, saliva or blood, so avoiding kissing does not address "
    "their route. Prevention means good handwashing and diaper hygiene, thorough cooking and clean water.",
    "saliva route assumed"),
   ("Screening donated blood",
    "Hepatitis A and E are not spread by blood; they travel by the fecal-oral route. Good handwashing and diaper "
    "hygiene, thorough cooking and clean drinking water are what prevent them.", "blood route assumed"),
   ("Covering coughs and sneezes",
    "Hepatitis A and E are not spread by sneezing; their route is fecal-oral. Prevention means good handwashing "
    "and diaper hygiene, cooking food thoroughly and consuming clean drinking water.", "airborne route assumed")],
  c(33)),

# ============================================================== TRACKING FOOD SAFETY (slides 34, 35, 14)
Q("Tracking food safety", IO4,
  "These band patterns come from bacterial isolates in one outbreak: an earlier patient for comparison, five "
  "patients, five environmental samples and three animals. Which laboratory method produced them?",
  ("Pulsed-field gel electrophoresis",
   "Correct. A pulsed-field gel electrophoresis pattern is made for each microbial isolate and added to PulseNet. "
   "Here the patient, environmental and animal isolates share one band pattern while the earlier comparison patient "
   "differs, the kind of match that helps find an outbreak's cause."),
  [("Eosin methylene blue plate culture",
    "Eosin methylene blue plates are used to confirm Escherichia coli in samples such as food and water; the result is "
    "colonies on a plate, not a row of bands for each isolate. Band patterns matched across isolates come from "
    "pulsed-field gel electrophoresis.", "confirmation plate confused with typing"),
   ("A PulseNet database search",
    "PulseNet is the Centers for Disease Control and Prevention database the patterns are added to, not the method "
    "that makes them. Each isolate's band pattern is produced by pulsed-field gel electrophoresis and then entered "
    "into PulseNet.", "database confused with the method"),
   ("Gram staining of each isolate",
    "Gram staining shows cell traits such as the Gram-positive rods of the clostridia; it gives no band pattern "
    "for each isolate. Rows of bands matched across patients, environment and animals come from pulsed-field gel "
    "electrophoresis.", "staining confused with typing")],
  ci(34, 34, 14, 25),
  img=IMG + "/l16-fig-03.jpg",
  alt="Rows of dark vertical bands, one row per labeled isolate: a 2005 patient for comparison, Patients 1 to 5, "
      "Environmental 1 to 5 and Animals 1 to 3.",
  slide="Slide 34"),

Q("Tracking food safety", IO4,
  "What is collected in PulseNet for each microbial isolate?",
  ("Its pulsed-field gel electrophoresis pattern",
   "Correct. A pulsed-field gel electrophoresis pattern for each microbial isolate is added to PulseNet, a database "
   "through the Centers for Disease Control and Prevention. Matching patterns help determine the causes of "
   "outbreaks and detect problems at food processing plants."),
  [("Its eosin methylene blue plate result",
    "Eosin methylene blue plates are used to confirm Escherichia coli in samples such as food and water. PulseNet "
    "holds something else: the pulsed-field gel electrophoresis pattern of each isolate.",
    "confirmation test confused with typing"),
   ("Its food and dietary supplement recall notice",
    "Recall notices for food and dietary supplements, including pet food, are posted on the Food and Drug "
    "Administration website, and the United States Department of Agriculture also posts food recalls. PulseNet "
    "holds isolate patterns.", "recall listings confused with the database"),
   ("Its food handler certification record",
    "Training and certification of food service workers comes from programs such as ServSafe, part of kitchen "
    "prevention. PulseNet is a surveillance database of pulsed-field gel electrophoresis patterns of isolates.",
    "kitchen training confused with surveillance")],
  c(34, 14, 35, 36)),

Q("Tracking food safety", IO4,
  "How does comparing isolate patterns in PulseNet help food safety?",
  ("It traces outbreaks and plant problems",
   "Correct. With a pulsed-field gel electrophoresis pattern on file for each microbial isolate, PulseNet can help "
   "determine the causes of outbreaks and even detect problems at food processing plants. That surveillance "
   "shortens detection time and reduces the number of cases."),
  [("It enforces food safety law and policy",
    "Enforcing food safety law and enacting policy is the job of the Food and Drug Administration and the United "
    "States Department of Agriculture. PulseNet is a surveillance database that helps find outbreak causes and "
    "processing-plant problems.", "surveillance confused with enforcement"),
   ("It confirms Escherichia coli in water",
    "Confirming Escherichia coli in samples such as food or water is done on eosin methylene blue plates. PulseNet "
    "compares isolate patterns to find the causes of outbreaks and problems at food processing plants.",
    "confirmation test confused with typing"),
   ("It certifies food service workers",
    "ServSafe training and certification prepares food service workers, part of prevention in the kitchen. "
    "PulseNet is a database of isolate patterns that helps find outbreak causes and processing-plant problems.",
    "kitchen training confused with surveillance")],
  c(34, 9, 14, 36)),

Q("Tracking food safety", IO4,
  "What effect does PulseNet surveillance have on foodborne outbreaks?",
  ("Shorter detection time and fewer cases",
   "Correct. Adding a pulsed-field gel electrophoresis pattern for each isolate to PulseNet helps determine the "
   "causes of outbreaks and detect problems at food processing plants. This surveillance helps reduce both the "
   "detection time and the number of cases of illness."),
  [("Longer detection time but fewer cases",
    "Half reversed: the surveillance shortens detection time rather than lengthening it, and it does reduce the "
    "number of cases. Finding an outbreak's cause sooner is the point of matching isolate patterns.",
    "reversed effect on detection time"),
   ("Shorter detection time but more cases",
    "Faster detection might seem to add cases, but this surveillance helps reduce both the detection time and the "
    "number of cases of illness, by finding an outbreak's cause and processing-plant problems sooner.",
    "better detection taken to mean more illness"),
   ("No change in detection time or in cases",
    "Matching isolate patterns does change outcomes: PulseNet surveillance helps reduce both the detection time and "
    "the number of cases of illness, by revealing the causes of outbreaks and problems at food processing plants.",
    "surveillance seen as record-keeping only")],
  c(34)),

Q("Tracking food safety", IO4,
  "Which agency runs PulseNet?",
  ("Centers for Disease Control and Prevention",
   "Correct. The pulsed-field gel electrophoresis pattern of each microbial isolate is added to PulseNet, a "
   "database run through the Centers for Disease Control and Prevention and reached from its website. It helps "
   "find outbreak causes and problems at food processing plants."),
  [("Food and Drug Administration",
    "The Food and Drug Administration posts updated information on food and dietary supplement recalls, including "
    "pet food, and enforces food safety law. PulseNet, the database of isolate patterns, runs through the Centers "
    "for Disease Control and Prevention.", "recall agency confused with surveillance agency"),
   ("United States Department of Agriculture",
    "The United States Department of Agriculture also has food recall information and shares law enforcement and "
    "policy duties with the Food and Drug Administration. PulseNet belongs to the Centers for Disease Control and "
    "Prevention.", "recall agency confused with surveillance agency"),
   ("Local and state health departments",
    "Local and state health departments conduct food safety surveillance and outbreak investigations, but PulseNet, "
    "the pattern database, is run through the Centers for Disease Control and Prevention.",
    "local surveillance confused with the national database")],
  c(34, 35, 9)),

Q("Tracking food safety", IO4,
  "Which agency's website posts updated recalls of dietary supplements and pet food?",
  ("The Food and Drug Administration",
   "Correct. The Food and Drug Administration website has updated information about food and dietary supplement "
   "recalls, including pet food. The United States Department of Agriculture website also carries food recall "
   "information, and PulseNet sits with the Centers for Disease Control and Prevention."),
  [("The Centers for Disease Control and Prevention",
    "The Centers for Disease Control and Prevention website hosts PulseNet, the database of isolate patterns for "
    "tracking outbreaks. Recalls of dietary supplements and pet food are posted by the Food and Drug "
    "Administration.", "surveillance agency confused with recall agency"),
   ("Local and state health departments",
    "Local and state health departments conduct food safety surveillance and investigate outbreaks. Updated recall "
    "information for food and dietary supplements, including pet food, is on the Food and Drug Administration "
    "website.", "local surveillance confused with recall postings"),
   ("The ServSafe food safety program",
    "ServSafe provides food service training and certification, a kitchen prevention measure. Recalls of food and "
    "dietary supplements, including pet food, are posted on the Food and Drug Administration website.",
    "kitchen training confused with recall postings")],
  c(35, 34, 9, 36)),

Q("Tracking food safety", IO4,
  "A laboratory wants to confirm Escherichia coli in a water sample, not link it to other isolates. Which tool is "
  "often used?",
  ("Eosin methylene blue plates",
   "Correct. Eosin methylene blue plates are often used to confirm Escherichia coli in samples such as food and "
   "water. Escherichia coli is an indicator organism associated with human and animal feces, so confirming it "
   "points to fecal contamination."),
  [("Pulsed-field gel electrophoresis",
    "Pulsed-field gel electrophoresis makes a band pattern for each isolate so that isolates can be compared and "
    "outbreaks traced. The task here is confirming Escherichia coli in a sample, which eosin methylene blue plates "
    "do.", "typing confused with confirmation"),
   ("A PulseNet database search",
    "PulseNet is the Centers for Disease Control and Prevention database of isolate patterns, used to find "
    "outbreak causes. Confirming Escherichia coli in a water sample is done on eosin methylene blue plates.",
    "database confused with a laboratory test"),
   ("A federal food recall search",
    "Federal websites such as the Food and Drug Administration and United States Department of Agriculture sites "
    "list recalled foods. Confirming Escherichia coli in a water sample is a laboratory task done on eosin "
    "methylene blue plates.", "recall listings confused with a laboratory test")],
  c(14, 15, 34, 35)),

# ============================================================== KITCHEN PREVENTION (slide 36, with 28)
QO("Kitchen prevention", IO2,
   "When cooking meat products, what temperature should a meat thermometer confirm instead of guessing?",
   [("110 F",
     "110 F falls well short of the 165 F a meat thermometer should confirm. Improper cooking lets bacteria "
     "multiply in the food, the start of a food infection such as salmonellosis or listeriosis.",
     "undercooking target"),
    ("130 F",
     "130 F is still below the 165 F target for cooked meat products. Raw or undercooked meats are among the "
     "foods most vulnerable to Listeria monocytogenes, which is why the thermometer replaces guessing.",
     "undercooking target"),
    ("165 F",
     "Correct. When cooking meat products, the advice is to use a meat thermometer and confirm 165 F rather than "
     "guessing. Proper cooking matters because improper cooking lets bacteria in the food multiply, the route of "
     "food infection.", None),
    ("190 F",
     "190 F overshoots the figure given: the meat thermometer target for cooked meat products is 165 F. The point "
     "is to measure rather than guess, so the meat reliably reaches 165 F.", "overestimated target")],
   2, ci(12, 36, 23)),

Q("Kitchen prevention", IO1,
  "After cutting raw chicken, a cook rinses the knife in cold water and then slices salad vegetables on the same "
  "cutting board. Which kitchen rule does this break?",
  ("Avoid cross-contamination of utensils",
   "Correct. Raw chicken fluid left on the board and knife can reach the salad, which is cross-contamination of "
   "cutting boards and utensils. With Campylobacter jejuni the infectious dose is under 500 cells, so even one drop "
   "of raw poultry fluid can cause illness."),
  [("Keep hot foods hot and cold foods cold",
    "Holding temperatures matter for Bacillus cereus, but nothing here was left warm or cool too long. The fault "
    "is moving raw poultry fluid onto the salad through a shared board and knife, which is cross-contamination.",
    "holding-temperature rule misapplied"),
   ("Use a meat thermometer rather than guessing",
    "A meat thermometer checks that meat reaches 165 F, but the chicken's cooking is not the problem described. "
    "Using the same board and knife for raw chicken and salad is cross-contamination.",
    "cooking rule misapplied"),
   ("When in doubt, toss it out",
    "'When in doubt, toss it out' is for food of uncertain safety. Here the problem is plain: raw chicken fluid "
    "moving to salad vegetables on a shared board and knife, which is cross-contamination.",
    "discard rule misapplied")],
  c(36, 21, 28)),

Q("Kitchen prevention", IO1,
  "Which approach is advised for sanitizing kitchen surfaces and utensils?",
  ("Mild bleach cleaning solutions",
   "Correct. Kitchen surfaces and utensils should be cleaned with mild bleach cleaning solutions, alongside "
   "handwashing with hot, soapy water, washing fruits and vegetables and avoiding cross-contamination of cutting "
   "boards and utensils."),
  [("Undiluted bleach at full strength",
    "The cleaning solution is a mild bleach, not full-strength bleach. Mild bleach on surfaces and utensils, with "
    "hot, soapy handwashing and no cross-contamination of cutting boards, is the kitchen routine.",
    "reversed strength"),
   ("Salt brine with added vinegar",
    "Salt brine, often with lactic acid, vinegar and spices, is used to pickle and preserve vegetables, not to "
    "clean. Kitchen surfaces and utensils are cleaned with mild bleach cleaning solutions.",
    "pickling brine taken for a cleaner"),
   ("A cold-water rinse of each item",
    "Hot, soapy water is the handwashing advice, and kitchen surfaces and utensils call for mild bleach cleaning "
    "solutions; a cold-water rinse is neither. Cross-contamination of boards and utensils is the risk to avoid.",
    "plain rinsing assumed enough")],
  c(36, 6)),

Q("Kitchen prevention", IO2,
  "Leftover cooked chicken has sat in the refrigerator for an unknown time and smells normal. What should be done "
  "with it?",
  ("Toss it out rather than risk it",
   "Correct. When in doubt, toss it out. Refrigeration does not settle the question: Listeria monocytogenes grows "
   "well at refrigerator temperatures, and with Campylobacter jejuni from poultry even one drop of raw poultry "
   "fluid can cause illness."),
  [("Eat it, since it still smells normal",
    "A normal smell does not settle it: undesirable flavors, appearance or smell mark spoilage, which is separate "
    "from foodborne illness, and microbes can be present without changing the food. When in doubt, toss it out.",
    "smell taken as a safety test"),
   ("Taste a small bite first",
    "Tasting is not a safe test: the infectious dose of Campylobacter jejuni is under 500 cells, so a tiny amount "
    "can cause illness, and poultry leftovers call for care. When in doubt, toss it out.",
    "tasting taken as a safety test"),
   ("Rinse it, then serve it cold",
    "Washing is advised for fruits and vegetables, not as a fix for leftovers of unknown age. Listeria "
    "monocytogenes grows well at refrigerator temperatures, so the rule for doubtful food is to toss it out.",
    "produce washing misapplied")],
  c(36, 3, 21, 23)),

]
