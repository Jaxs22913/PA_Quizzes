# -*- coding: utf-8 -*-
"""Section 16 of the Microbiology Exam 3 guide -- Significant Microorganisms in Food Safety (Dr. Fair).

Same shape as _micro_e3_guide_l14.py (FIG, DECK, IMAGES, extract(), fig(), TOC, SECTION, TEST).

Attribution: Dr. Fair. The title slide names no lecturer; the deck file is "PAJ5200.FoodSafety-micro.pptx", her
PAJ5200.* naming, its file properties name Dianne Fair as last editor, and the calendar row for 30 October 2026
(3-5 pm, Lecture 16, "Food Safety") names Dr. Fair. The recording (Phase 2) confirms or corrects this.

Instructional objectives are VERBATIM from the syllabus (Micro.pdf, page 5, "Food Safety"): four numbered
objectives. The deck's objective slide (slide 2) matches them with small wording differences ("the global food
supply", "antibiotic-resistant"); the syllabus wording is used. Objective 1 is answered in 16.1-16.2 and in each
organism's "source" line, objective 2 in 16.3-16.13, objective 4 in 16.14. OBJECTIVE 3 (public concern and
antibiotic-resistant strains in the food supply) has NO slide in the deck: 16.15 says so rather than inventing
content, and no question asks it.

Content is from the VISIBLE slides only, text and pictures; speaker notes do not count (slides 2, 6, 8, 16, 18
and 25 carry notes: the home-brining recipe, the television show, the recall website, the turducken link and the
Clostridioides renaming are all notes and are left out). Every picture was viewed at full size. Picture-only slides:
10 (the symptom set), 11 (bismuth subsalicylate packaging and a black tongue, no text), 19 (peanut butter, eggs,
a turtle, a watermelon recall), 20 (Salmonella, two agar plates, the Mary Mallon poster), 24 (Listeria spread),
26 (a raw honey label). Slide 12's diagram is small (179 x 281 px) and is shown at that size.

PHASE 1 (30 October 2026): built from the slides while the lecture was being recorded. The MICROL16AUDIO block
is the placeholder the audio pass replaces.
"""
import io, os

FIG = "micro-exam-3-study-guide-images"
DECK = "PAJ5200.FoodSafety-micro.pptx"
INBOX_DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Microbiology Inbox/Exam 3/" + DECK)

# (slide, picture index in shape-tree order, published name). Slide 14: picture 1 is a drawing of a rod, picture 2
# the agar plate. Slide 20: picture 3 is the Mary Mallon poster (1 = rods, 2 = two plates). Slide 24: picture 2 is
# the spread diagram (1 = two rods). .jpg names for PNG blobs, or JPEGs over 250 KB or 900 px wide, are re-encoded.
IMAGES = [
    (10, 1, "l16-s010-symptoms.jpg"),
    (12, 1, "l16-s012-intoxication-infection.jpg"),
    (14, 2, "l16-s014-emb-plate.jpg"),
    (20, 3, "l16-s020-typhoid-mary.jpg"),
    (21, 1, "l16-s021-campylobacter-cycle.jpg"),
    (24, 2, "l16-s024-listeria-spread.jpg"),
    (25, 1, "l16-s025-clostridium-spores.jpg"),
    (34, 1, "l16-s034-pfge-gel.jpg"),
]
MAXW = 900


def _pictures(shapes):
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from _pictures(sh.shapes)
            continue
        try:
            sh.image
        except Exception:
            continue
        yield sh


def extract(imgdir):
    """Write IMAGES into imgdir from the deck (pictures, picture placeholders and grouped pictures)."""
    from pptx import Presentation
    from PIL import Image
    prs = Presentation(INBOX_DECK)
    os.makedirs(imgdir, exist_ok=True)
    for slide, k, name in IMAGES:
        pics = list(_pictures(prs.slides[slide - 1].shapes))
        assert len(pics) >= k, "%s slide %d has %d picture(s)" % (DECK, slide, len(pics))
        img = pics[k - 1].image
        ext = img.ext.replace("jpeg", "jpg")
        out = os.path.join(imgdir, name)
        if name.endswith(".jpg") and (ext != "jpg" or len(img.blob) > 250 * 1024
                                      or Image.open(io.BytesIO(img.blob)).width > MAXW):
            im = Image.open(io.BytesIO(img.blob)).convert("RGB")
            if im.width > MAXW:
                im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
            im.save(out, quality=85)
        else:
            assert name.endswith("." + ext), (name, ext)
            open(out, "wb").write(img.blob)
    return len(IMAGES)


def fig(name, w, h, alt, cap, slide, credit=""):
    note = (credit + " ") if credit else ""
    return ('<figure class="fig"><img width="%d" height="%d" loading="lazy" src="%s/%s" alt="%s">'
            '<figcaption>%s <span class="src">%sSource: %s, Slide %d.</span></figcaption></figure>'
            % (w, h, FIG, name, alt, cap, note, DECK, slide))


TOC = """
  <a class="top-link" href="#food-safety">16 &middot; Significant Microorganisms in Food Safety</a>
  <a class="sub-link" href="#food-audio">&#9733; What the recording adds</a>
  <a class="sub-link" href="#food-production">16.1 Objective 1 &mdash; Microbes in food: production and spoilage</a>
  <a class="sub-link" href="#food-sources">16.2 Objective 1 &mdash; Where foodborne microbes come from</a>
  <a class="sub-link" href="#food-burden">16.3 Objective 2 &mdash; The size of the problem, and who watches it</a>
  <a class="sub-link" href="#food-intox">16.4 Objective 2 &mdash; Food intoxication versus food infection</a>
  <a class="sub-link" href="#food-ecoli">16.5 Objective 2 &mdash; <em>Escherichia coli</em></a>
  <a class="sub-link" href="#food-salmonella">16.6 Objective 2 &mdash; <em>Salmonella</em></a>
  <a class="sub-link" href="#food-campy">16.7 Objective 2 &mdash; <em>Campylobacter jejuni</em></a>
  <a class="sub-link" href="#food-listeria">16.8 Objective 2 &mdash; <em>Listeria monocytogenes</em></a>
  <a class="sub-link" href="#food-clostridium">16.9 Objective 2 &mdash; <em>Clostridium</em> and botulism</a>
  <a class="sub-link" href="#food-cereus">16.10 Objective 2 &mdash; <em>Bacillus cereus</em></a>
  <a class="sub-link" href="#food-vibrio">16.11 Objective 2 &mdash; <em>Vibrio</em></a>
  <a class="sub-link" href="#food-parasites">16.12 Objective 2 &mdash; Fungi, protozoa and parasitic worms</a>
  <a class="sub-link" href="#food-viruses">16.13 Objective 2 &mdash; Foodborne viruses</a>
  <a class="sub-link" href="#food-tracking">16.14 Objective 4 &mdash; Laboratory methods, tracking and recalls</a>
  <a class="sub-link" href="#food-resistance">16.15 Objective 3 &mdash; Antibiotic resistance (not in the slides)</a>
  <a class="sub-link" href="#food-prevention">16.16 What you can do: prevention</a>
  <a class="sub-link" href="#food-notes">16.17 Where the slides and current references differ</a>
"""

SECTION_HEAD = """
<section class="deck" id="food-safety">
  <h2 class="deck-title">16 &middot; Significant Microorganisms in Food Safety</h2>
  <p class="lecturer">Dr. Fair &middot; Lecture 16 &middot; 30 October 2026</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Identify sources of microbial contamination in global food supply.</li>
      <li>Correlate associations between contaminated foods with the increasing numbers of diagnosed food-borne
      illnesses and mortality worldwide.</li>
      <li>Analyze associations between public concern and antibiotic resistant strains of microbes in the food
      supply.</li>
      <li>Correlate associations between improved laboratory analytical methods with respect to near-daily
      announcements of food recalls and food-related illness.</li>
    </ol>
  </div>

  <div class="callout"><strong>Food, the microbe, the illness, the trace.</strong> Microbes are in food on purpose
  (bread, beer, cheese, yogurt), by accident (spoilage) or as passengers (16.1). The dangerous ones come from
  animals, feces, soil and water (16.2). Then the organism list, each with its food and its illness: the first
  split is <strong>intoxication</strong> (a preformed toxin: staphylococcal toxin, botulinum toxin) against
  <strong>infection</strong> (live cells that multiply: <em>Salmonella</em>, <em>Listeria</em>), 16.4. The seven
  bacteria are <em>Escherichia coli</em>, <em>Salmonella</em>, <em>Campylobacter jejuni</em>, <em>Listeria
  monocytogenes</em>, <em>Clostridium</em>, <em>Bacillus cereus</em> and <em>Vibrio</em> (16.5&ndash;16.11), then
  fungi, protozoa, worms and viruses (16.12&ndash;16.13). Last, how outbreaks are traced: pulsed-field gel
  electrophoresis patterns in the PulseNet database (16.14). Objective 3, antibiotic resistance, has no slide
  (16.15).</div>

<!--MICROL16AUDIO-->
  <div class="prof-flag" id="food-audio"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 30 October 2026</span>
  <p><b>Not read yet.</b> This lecture was recorded on 30 October and the recording is being transcribed (ours,
  plus Notability&rsquo;s own transcript as a second opinion). Until it has been read, this section is built from
  the slides alone, and the quizzes are weighted by slide count. When the recording has been read, this box will
  carry what Dr. Fair stressed, what she said to skip, whether she covered objective 3 (antibiotic resistance, which
  no slide teaches), and any correction of a slide (16.17 lists the ones worth listening for).</p>
  </div>
<!--/MICROL16AUDIO-->
"""

BODY = """
  <h3 class="sub" id="food-production">16.1 &middot; Objective 1 &mdash; Microbes in food: production and spoilage</h3>
  <table>
    <tr><th>Effect of microbes on food</th><th>What it means</th></tr>
    <tr><td><strong>Beneficial</strong></td><td>Food <strong>fermented or otherwise chemically changed</strong> by added microbes or microbial products, to alter or improve its flavor, taste or texture</td></tr>
    <tr><td><strong>Detrimental</strong></td><td><strong>Food poisoning, food intoxication, food-borne illness and food spoilage</strong>: food unfit to eat because of undesirable flavors, appearance or smell</td></tr>
    <tr><td><strong>Neutral</strong></td><td>Microbes present that neither cause disease nor change the food: &ldquo;they&rsquo;re just there and we consume them with the food&rdquo;</td></tr>
  </table>
  <h4 class="subsub">Bread making</h4>
  <p>Microbes have <strong>three main functions</strong>: (1) <strong>leavening</strong> flour-based dough (mainly
  carbon dioxide and other gases); (2) <strong>imparting flavor and aroma</strong> (organic acids and alcohols); (3)
  <strong>conditioning</strong> the dough to make it pliable and workable (microbial enzymes act on gluten to give
  elasticity). Microbes involved: <strong><em>Saccharomyces cerevisiae</em> (baker&rsquo;s yeast)</strong>, certain
  <em>Clostridium</em> species, and certain <em>Lactobacillus</em> species (<strong><em>Lactobacillus
  sanfrancisco</em> in sourdough</strong>).</p>
  <h4 class="subsub">Beer, wine and other fermented products</h4>
  <ul>
    <li><strong>Glucose + yeast &rarr; 2 ethanol + 2 carbon dioxide</strong> (C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>
    &rarr; 2C<sub>2</sub>H<sub>5</sub>OH + 2CO<sub>2</sub>). Evidence of beer brewing since 6000 BCE in Sumeria, Egypt
    and Babylon. Steps: malting of the starch source, mashing, wort plus hops, lagering, filtration.</li>
    <li><strong>Wine</strong> usually starts with grapes, but other fruit and plant material can be used (apples,
    oranges, pineapples, peaches, plums).</li>
    <li>Sometimes the <strong>source of yeast for an alcoholic beverage is human saliva</strong>: chewing
    (mastication) of the plant material precedes the brewing.</li>
    <li><strong>Pickling</strong>: salt brine preserves vegetable material; lactic acid may also be present, with
    vinegar and spices. Cucumbers, cabbage, olives, okra, onions, ginger root and many more can be pickled.</li>
    <li><strong>Soybeans</strong> and their extracts are fermented into tofu and soy sauce (shoyu); also fermented fish
    sauce, mole (chocolate), tea and coffee.</li>
  </ul>
  <h4 class="subsub">Milk and dairy</h4>
  <ul>
    <li><strong>Milk begins sterile</strong>: water, minerals, protein, butterfat, lactose and other sugars.
    <strong>Microbes are introduced as it exits the female mammal&rsquo;s body and by milking utensils</strong>; it is
    <strong>highly susceptible to microbial growth because of its nutrient density</strong>.</li>
    <li>Fermentation of milk can be natural or induced (cheese or yogurt making). <strong>Cheese making</strong> is about
    5000 years old (cow, goat or sheep milk; some cultures horse or water buffalo). The <strong>first fermented dairy
    products were probably due to accidental contamination with human skin, nose or oral bacteria and fungi</strong>.
    Cheese making involves <strong>yeast, bacteria and molds</strong> (multicellular fungi).</li>
    <li><strong>Yogurt</strong> is a fermented milk made with bacteria such as <strong><em>Lactobacillus</em> and
    <em>Streptococcus</em></strong>; other fermented milks are kefir, koumiss and buttermilk.</li>
  </ul>
  <h4 class="subsub">Microbes as food, and fungi in food</h4>
  <ul>
    <li>Macroscopic fungi and algae are obvious foods: mushrooms, truffles, seaweed. <strong>Microbial additives for
    animal feed</strong> are already used; human versions are slower to be accepted. <strong>&ldquo;Single cell
    protein&rdquo;</strong> and bacterial or fungal products are being researched in the United Kingdom and elsewhere.
    In the United States the <strong>cyanobacterium <em>Spirulina</em></strong> is added to foods such as smoothies
    and vitamin supplement gummies.</li>
    <li><strong>Fungi do not commonly cause disease</strong> but are associated with both food production and food
    spoilage: importance in food (mushrooms), in medicine (<strong>they produce penicillin</strong>), and in
    industry (<strong>yeasts are fungi used to ferment many products</strong>). <strong>Fungal spoilage</strong>: bread,
    cereals and acidic juices.</li>
  </ul>

  <h3 class="sub" id="food-sources">16.2 &middot; Objective 1 &mdash; Where foodborne microbes come from</h3>
  <table>
    <tr><th>Source</th><th>Organisms and foods on the slides</th></tr>
    <tr><td><strong>Feces</strong> (human and animal)</td><td><em>Escherichia coli</em>, the <strong>indicator organism</strong> of feces: fecally contaminated meats or vegetables. Norovirus and hepatitis A and E: feces (and vomitus), shellfish from feces-contaminated water</td></tr>
    <tr><td><strong>Animals</strong>, especially poultry</td><td><em>Salmonella</em>: many animals, mainly <strong>poultry and aquatic reptiles</strong>. <em>Campylobacter</em>: raw poultry. <em>Listeria</em>: birds and mammals. Parasitic worms: venison, pork and other meat <strong>contaminated while the animal is still alive</strong>; domestic pet feces (tapeworm, roundworm)</td></tr>
    <tr><td><strong>Soil and plants</strong></td><td><em>Listeria</em> persists in soil. <em>Clostridium</em> spores: soils, plants, <strong>honey</strong></td></tr>
    <tr><td><strong>Water</strong></td><td><em>Vibrio</em>: salt-tolerant, in <strong>ocean and estuarine waters</strong>. Protozoa: drinking water and uncooked fruit and vegetables</td></tr>
    <tr><td><strong>People</strong></td><td>Norovirus person to person; the carrier cook (16.6); milk picks up microbes as it leaves the animal and from utensils</td></tr>
  </table>

  <h3 class="sub" id="food-burden">16.3 &middot; Objective 2 &mdash; The size of the problem, and who watches it</h3>
  <ul>
    <li>An estimated <strong>250 different foodborne pathogens</strong>, with <strong>bacteria the most
    common</strong>.</li>
    <li>The slide gives <strong>75 million cases a year &ldquo;worldwide&rdquo; (probably under-reported) and at least
    5000 deaths</strong>: a serious problem for global health (see 16.17).</li>
    <li>The worry is not only bacteria from plant and animal sources but also <strong>viruses, parasites and toxins
    produced by microorganisms</strong>.</li>
    <li><strong>Surveillance and outbreak investigation</strong>: local and state health departments, the Centers for
    Disease Control and Prevention, the Food and Drug Administration, the United States Department of Agriculture.
    <strong>Law enforcement and policy</strong>: the <strong>Food and Drug Administration and the United States
    Department of Agriculture</strong>.</li>
  </ul>
  """ + fig("l16-s010-symptoms.jpg", 768, 697,
      "Pictograms of five figures under the heading Symptoms: one on a toilet, one clutching the stomach, one with a hand over the mouth, one with a thermometer, and one vomiting.",
      "<b>The symptoms of foodborne illness</b>: diarrhea, abdominal cramps, nausea, fever and vomiting. (Slide 11, "
      "pictures only, shows bismuth subsalicylate packaging, an upset stomach reliever and antidiarrheal, beside "
      "a blackened tongue; it has no text.)", 10) + """
  <p>The better-known bacteria of the lecture (slide 13): <em>E. coli</em>, <em>Salmonella</em> species,
  <em>Campylobacter jejuni</em>, <em>Listeria monocytogenes</em>, <em>Clostridium</em> species, <em>Bacillus
  cereus</em>, and <em>Vibrio</em> species such as <em>vulnificus</em> or <em>parahaemolyticus</em>. Organisms other
  than bacteria (slide 30): <strong>fungi, protozoa, parasitic worms (in pork, venison, wild-caught fish) and
  viruses</strong>.</p>

  <h3 class="sub" id="food-intox">16.4 &middot; Objective 2 &mdash; Food intoxication versus food infection</h3>
  <table>
    <tr><th></th><th>Food intoxication</th><th>Food infection</th></tr>
    <tr><td>What is eaten</td><td>A <strong>preformed toxin</strong> made by the bacteria in the food (cells and toxin)</td><td><strong>Live bacterial cells</strong></td></tr>
    <tr><td>What happens</td><td>The toxin is ingested and reaches its <strong>target organs</strong> (the diagram shows the brain and muscles)</td><td><strong>Improper cooking</strong> lets the <strong>bacteria multiply in the food</strong>; after ingestion they cause an <strong>intestinal infection</strong></td></tr>
    <tr><td>Examples (slide 12)</td><td><strong>Staphylococcal toxin</strong>, <strong><em>Clostridium botulinum</em> toxin</strong></td><td><strong><em>Salmonella</em></strong>, <strong><em>Listeria</em></strong></td></tr>
  </table>
  """ + fig("l16-s012-intoxication-infection.jpg", 179, 281,
      "Two-column diagram: left, a can of beans, a circle of rod cells shedding toxin dots, the gut, and toxin reaching a head and an arm; right, a roast chicken, a circle of cells, a frying pan labeled improper cooking technique, bacteria multiplying in food, and an infected intestine.",
      "<b>(a) Food intoxication; (b) food infection.</b>", 12, "Copyright &copy; The McGraw-Hill Companies.") + """

  <h3 class="sub" id="food-ecoli">16.5 &middot; Objective 2 &mdash; <em>Escherichia coli</em></h3>
  <ul>
    <li><strong>EMB (eosin methylene blue) plates</strong> are often used to <strong>confirm <em>E. coli</em> in samples
    (food, water)</strong>.</li>
    <li>An <strong>&ldquo;indicator organism&rdquo; associated with human and animal feces</strong>.</li>
    <li>Found everywhere, including inside humans, but <strong>not always pathogenic</strong>; it has many good traits
    too.</li>
    <li>As an infectious agent it causes <strong>nausea, vomiting and diarrhea</strong>. The bad strains can carry
    numerous toxins (for example the <strong>enterotoxigenic or enterohemorrhagic</strong> strains).</li>
    <li><strong>Sporadic outbreaks</strong> originate from <strong>fecally contaminated meats or vegetables</strong>
    (the Jack in the Box hamburgers, bagged spinach). <strong>One of the worst culprits is the O157:H7
    serotype.</strong></li>
    <li>The outbreak and recall list (slide 16): hamburgers (1993), California bagged spinach (2006), refrigerated
    cookie dough (2009), romaine lettuce (2010, 2018 from Arizona, 2020&ndash;2021 from California), 7% of fresh
    spinach in grocery stores carrying <em>E. coli</em> (a 2013 report), beef products (2019), ground beef from
    packing companies (2023&ndash;2025), and <strong>raw milk cheese in the western United States
    (September&ndash;October 2026)</strong>.</li>
  </ul>
  """ + fig("l16-s014-emb-plate.jpg", 241, 209,
      "An agar plate with streaks of growth that shine metallic green.",
      "<b>An eosin methylene blue plate</b>: the growth with a green metallic sheen. These plates are used to "
      "confirm <em>E. coli</em> in food and water samples.", 14) + """

  <h3 class="sub" id="food-salmonella">16.6 &middot; Objective 2 &mdash; <em>Salmonella</em></h3>
  <ul>
    <li>The main species are <em>Salmonella typhi</em>, <em>S. enterica</em>, <em>S. enteritidis</em> and <em>S.
    typhimurium</em>; others are named for where they were first found (<em>S. miami</em>, <em>S. heidelberg</em>,
    <em>S. sandiego</em>).</li>
    <li><strong>Associated with many animals, mainly poultry and aquatic reptiles.</strong></li>
    <li><strong>Salmonellosis</strong> can appear as gastroenteritis, enteric fever, septicemia (blood infection),
    fever, shock and kidney dysfunction. <strong>Incubation can be as short as hours or as long as
    weeks.</strong></li>
    <li><strong>Young children and the elderly are at greatest risk.</strong></li>
    <li><strong>Typhoid fever (<em>S. typhi</em>) is the most severe enteric fever</strong>: the intestinal wall is
    invaded and the bacteria can spread to the <strong>blood and lymph nodes</strong>.</li>
  </ul>
  <p><strong>Sources (slide 18)</strong>: <strong>poultry products</strong> (chicken, turkey, duck), <strong>eggs</strong>,
  <strong>pet food</strong>, <strong>live poultry</strong> (such as backyard hens), <strong>peanut butter</strong> and
  <strong>sushi-grade seafood</strong>. Recalls have included peanuts and peanut butter (2009), hydrolyzed vegetable
  protein (2010), farm eggs (2010), ground turkey (2011), pre-cut watermelon (2018), turkey and pork products (2019),
  onions from Mexico (2021), pre-cut cantaloupe (2023), cucumbers from Florida and Mexico (2025) and jalapeno
  peppers (August 2026): <strong>produce, not just animal foods</strong>. Slide 19 pictures peanut butter jars, eggs, a
  pet turtle and a watermelon recall.</p>
  """ + fig("l16-s020-typhoid-mary.jpg", 900, 871,
      "A vintage-style poster of a woman cooking at a frying pan from which skulls fall, with the words Mary Mallon: she was warned, she was given an explanation, nevertheless she persisted, and caused multiple deadly outbreaks.",
      "<b>&ldquo;Typhoid Mary.&rdquo;</b> Mary Mallon, a cook: &ldquo;She was warned. She was given an explanation. "
      "Nevertheless, she persisted. And caused multiple deadly outbreaks.&rdquo; Slide 20 also shows "
      "<em>Salmonella</em> rods and two agar plates.", 20) + """

  <h3 class="sub" id="food-campy">16.7 &middot; Objective 2 &mdash; <em>Campylobacter jejuni</em></h3>
  <ul>
    <li><strong>A leading cause of bacterial diarrheal disease each year in the United States, especially in
    children.</strong></li>
    <li><strong>Fever, headache, dizziness and bloody diarrhea</strong>, usually <strong>rapid</strong> in onset.</li>
    <li>The <strong>infectious dose is less than 500 bacterial cells</strong>, so <strong>even one drop of raw poultry
    fluid can cause illness</strong>.</li>
    <li><strong>Very much under-reported.</strong> Be careful with Thanksgiving poultry and leftovers.</li>
  </ul>
  """ + fig("l16-s021-campylobacter-cycle.jpg", 655, 447,
      "Cycle diagram: chickens, a puddle of water with amoebae, a cow and a bucket, milk bottles, a roast chicken, and a human figure, with insets of curved bacteria in the mucus layer of the gut.",
      "<b>How <em>Campylobacter</em> reaches people</b>: chickens and water, cattle and milk, and poultry meat, "
      "all leading to the human gut.", 21, "Nature Reviews Microbiology.") + """

  <h3 class="sub" id="food-listeria">16.8 &middot; Objective 2 &mdash; <em>Listeria monocytogenes</em></h3>
  <ul>
    <li>Found in <strong>birds and mammals</strong>, and <strong>can persist in soil</strong>.</li>
    <li><strong>Large-scale food recalls</strong>: the big ice cream recall of 2016 (Blue Bell, slide 22),
    cantaloupes, frozen vegetables, poultry (2019).</li>
    <li><strong>Greatest risk of listeriosis</strong>: <strong>pregnant women, unborn children, premature babies,
    elderly people and the immunocompromised</strong>.</li>
    <li>The slide calls it <strong>&ldquo;the #1 cause of food-related deaths in the US&rdquo;</strong> (see
    16.17).</li>
    <li><strong>Most vulnerable foods</strong>: soft cheeses, raw fruit and vegetables, raw or undercooked meats, deli
    meats, seafood, smoked seafood, hot dogs, preserved meats.</li>
    <li><strong>Probably the biggest concern: it grows well from 1 to 40&nbsp;&deg;C</strong>, easily at refrigerator,
    room or freezer temperatures.</li>
  </ul>
  """ + fig("l16-s024-listeria-spread.jpg", 900, 559,
      "Diagram: contaminated food to the intestine, a lymph node and the bloodstream, which circulates to the liver and spleen, then on to the brain and across the placenta to a fetus.",
      "<b>Where <em>Listeria</em> goes</b>: contaminated food &rarr; intestine &rarr; lymph node &rarr; bloodstream "
      "(liver, spleen) &rarr; <b>brain</b>, and across the <b>placenta to the fetus</b>.", 24) + """

  <h3 class="sub" id="food-clostridium">16.9 &middot; Objective 2 &mdash; <em>Clostridium</em> and botulism</h3>
  <ul>
    <li><strong>Gram-positive rods, strict anaerobes, form spores.</strong></li>
    <li>Notable species: <strong><em>C. botulinum</em> and <em>C. perfringens</em></strong>; <em>C. tetani</em> (not
    food-related) and <em>C. difficile</em> (also not food-related).</li>
    <li><strong>Spores are found in soils, associated with plants, and even in honey</strong> (slide 26 shows a raw
    honey label).</li>
  </ul>
  """ + fig("l16-s025-clostridium-spores.jpg", 423, 425,
      "Micrograph of rod-shaped bacteria, many with a clear oval spore inside.",
      "<b><em>Clostridium</em></b>: rods carrying spores.", 25) + """
  <table>
    <tr><th><em>Clostridium botulinum</em></th><th>Slide 27</th></tr>
    <tr><td>Toxin</td><td>When <strong>spores germinate</strong> they can start producing toxin: <strong>botulinum toxin (&ldquo;botox&rdquo;)</strong></td></tr>
    <tr><td>Forms</td><td><strong>Foodborne and wound-borne botulism</strong> are known to occur</td></tr>
    <tr><td>Effect</td><td>Ingesting the toxin leads to <strong>paralysis of the muscles in the relaxed position</strong>, then <strong>respiratory failure and death</strong></td></tr>
    <tr><td>Dose</td><td><strong>Even if only a few bacteria are present, they can produce plenty of toxin</strong></td></tr>
  </table>

  <h3 class="sub" id="food-cereus">16.10 &middot; Objective 2 &mdash; <em>Bacillus cereus</em></h3>
  <ul>
    <li>A <strong>very common food poisoning agent, especially in summertime</strong>.</li>
    <li>Gastroenteritis from <em>B. cereus</em> is either <strong>diarrheal or emetic</strong>.</li>
    <li><strong>Intoxication has a rapid onset (6 hours or less)</strong> with <strong>self-resolving vomiting and
    abdominal cramps</strong>.</li>
    <li><strong>Keep hot foods hot and cold foods cold.</strong></li>
  </ul>
  <table>
    <tr><th>Form</th><th>Toxin, as the slide gives it</th><th>Food</th></tr>
    <tr><td><strong>Diarrheal</strong></td><td>Heat-stable toxin (see 16.17)</td><td><strong>Meat</strong></td></tr>
    <tr><td><strong>Emetic</strong></td><td>Heat-labile toxin (see 16.17)</td><td><strong>Rice</strong></td></tr>
  </table>

  <h3 class="sub" id="food-vibrio">16.11 &middot; Objective 2 &mdash; <em>Vibrio</em></h3>
  <ul>
    <li>Several species: <strong><em>Vibrio cholerae</em>, <em>V. vulnificus</em> and <em>V.
    parahaemolyticus</em></strong>.</li>
    <li><strong>Salt-tolerant</strong> bacteria of <strong>ocean and estuarine waters</strong>.</li>
    <li><strong>Two major routes</strong>: <strong>water</strong> (ingested, or <strong>wound infections</strong>) or
    <strong>foodborne</strong> (shellfish, crabs, raw seafood, oysters).</li>
    <li>The <strong>&ldquo;R-month&rdquo; rule</strong> (no oysters, clams or mussels in May, June, July and August):
    &ldquo;maybe, maybe not&rdquo;; <strong>aquaculture practices have advanced so much</strong> that there are fewer
    worries.</li>
  </ul>

  <h3 class="sub" id="food-parasites">16.12 &middot; Objective 2 &mdash; Fungi, protozoa and parasitic worms</h3>
  <ul>
    <li><strong>Fungi</strong>: rarely disease, mostly production and spoilage (16.1).</li>
    <li><strong>Protozoa</strong>: <em>Cryptosporidium</em>, <em>Cyclospora</em>, <em>Giardia</em>,
    <em>Entamoeba</em>. All can cause <strong>mild, usually self-limiting diarrhea</strong> associated with
    <strong>uncooked fruits and vegetables or drinking water</strong>. <strong>Ready-to-eat salad bags</strong> are a
    common culprit.</li>
    <li><strong>Parasitic worms</strong>: tapeworm, roundworm, trichinosis. <strong>Best killed by thorough
    cooking.</strong> Venison, pork and other meats can be <strong>contaminated while the animal is still
    alive</strong>: the muscle or organ meats may be suspect. <strong>Domestic pet feces</strong> can carry tapeworm and
    roundworm.</li>
  </ul>

  <h3 class="sub" id="food-viruses">16.13 &middot; Objective 2 &mdash; Foodborne viruses</h3>
  <table>
    <tr><th></th><th>Norovirus (Norwalk-like viruses, family Caliciviridae)</th><th>Hepatitis A and E</th></tr>
    <tr><td>How common</td><td>A common foodborne agent, upwards of 23 million cases a year</td><td>Hepatitis viruses A&ndash;E exist; <strong>A and E</strong> are the ones typically spread by the fecal-oral route</td></tr>
    <tr><td>Spread</td><td><strong>Person to person</strong>, by <strong>feces and vomitus</strong> (daycares, nursing homes, cruise ships); also <strong>contaminated shellfish</strong> (feces-contaminated water)</td><td><strong>Fecal-oral</strong>; <strong>not by kissing, sneezing, saliva or blood</strong></td></tr>
    <tr><td>Course</td><td><strong>Infectious dose only a few viral particles</strong>; <strong>rapid onset and short duration</strong>: nausea, vomiting, diarrhea, low-grade fever</td><td>A person is <strong>most contagious about two weeks BEFORE symptoms appear</strong></td></tr>
    <tr><td>Prevention</td><td colspan="2">Good <strong>handwashing and diaper hygiene</strong>; cook food thoroughly; clean drinking water. For hepatitis, <strong>a vaccine in case of suspected exposure</strong></td></tr>
  </table>

  <h3 class="sub" id="food-tracking">16.14 &middot; Objective 4 &mdash; Laboratory methods, tracking and recalls</h3>
  <ul>
    <li>A <strong>pulsed-field gel electrophoresis pattern</strong> for each microbial isolate is added to a
    <strong>database run through the Centers for Disease Control and Prevention: &ldquo;PulseNet&rdquo;</strong>.</li>
    <li>It can help <strong>determine the causes of outbreaks</strong> or even <strong>detect problems at food
    processing plants</strong>.</li>
    <li>This surveillance <strong>reduces the detection time and the number of cases of illness</strong>.</li>
    <li>In the laboratory, <strong>eosin methylene blue plates confirm <em>E. coli</em></strong> in food and water
    samples (16.5).</li>
    <li><strong>Online resources</strong>: Foodsafetynews.com, Foodsafetymagazine.com, the Centers for Disease Control
    and Prevention (PulseNet), the <strong>Food and Drug Administration</strong> (food and dietary supplement recalls,
    <strong>including pet food</strong>) and the <strong>United States Department of Agriculture</strong> (food recall
    information).</li>
  </ul>
  """ + fig("l16-s034-pfge-gel.jpg", 500, 383,
      "A gel image with fourteen lanes of dark bands: a 2005 patient for comparison, five patients, five environmental samples and three animal samples; the bands of the patients, environmental and animal isolates line up with one another.",
      "<b>Pulsed-field gel electrophoresis on <em>E. coli</em> O157 isolates</b> (Minnesota Department of Health, "
      "3 June 2010): the patient, environmental and animal isolates share one banding pattern, which ties the "
      "cases to a common source; the 2005 patient&rsquo;s pattern differs.", 34) + """

  <h3 class="sub" id="food-resistance">16.15 &middot; Objective 3 &mdash; Antibiotic-resistant strains in the food supply</h3>
  <p><strong>No slide teaches this objective.</strong> The deck&rsquo;s objective slide lists it, but none of its 36
  slides mentions antibiotic resistance, antibiotic use in food animals or resistant strains in food. Nothing is
  added here from outside the slides, and no quiz question asks it. If the recording covers it, the audio pass will
  say what was said; otherwise ask Dr. Fair whether it is examinable.</p>

  <h3 class="sub" id="food-prevention">16.16 &middot; What you can do: prevention</h3>
  <ul>
    <li>Good <strong>handwashing with hot, soapy water</strong>.</li>
    <li><strong>Wash fruits and vegetables.</strong></li>
    <li><strong>When in doubt, toss it out.</strong></li>
    <li>Clean kitchen surfaces and utensils with <strong>mild bleach</strong> cleaning solutions.</li>
    <li>When cooking meat, <strong>use a meat thermometer (165&nbsp;&deg;F)</strong> rather than guessing.</li>
    <li>Cutting board and knife materials; <strong>avoid cross-contamination of cutting boards and
    utensils</strong>.</li>
    <li>Proper use of <strong>disposable gloves</strong> in food service; <strong>hair coverings</strong> and food service
    attire; <strong>&ldquo;ServSafe&rdquo; training and certification</strong>.</li>
    <li>From the <em>Bacillus cereus</em> slide: <strong>keep hot foods hot and cold foods cold</strong>. From the
    viruses slide: <strong>handwashing and diaper hygiene, thorough cooking, clean drinking water</strong>.</li>
  </ul>

  <h3 class="sub" id="food-notes">16.17 Where the slides and current references differ</h3>
  <p>The quizzes key what the slides say (we are tested from the slides). These are the points where current
  references say something else; the recording may settle them.</p>
  <ul>
    <li><strong><em>Bacillus cereus</em> toxins (slide 28).</strong> The slide gives the <em>diarrheal</em> form a
    heat-stable toxin and the <em>emetic</em> form a heat-labile one. Standard references say the reverse: the emetic
    toxin (with rice) is the heat-stable one, and the diarrheal enterotoxin (with meat) is heat-labile. One quiz
    question asks this pairing, keyed as the slide says.</li>
    <li><strong>The case and death figures (slide 9).</strong> &ldquo;75 million cases per year worldwide&rdquo; and
    &ldquo;at least 5000 deaths&rdquo; match older United States estimates rather than worldwide ones; World Health
    Organization estimates for the world are far larger. Not asked.</li>
    <li><strong><em>Listeria</em> as the &ldquo;#1 cause of food-related deaths in the US&rdquo; (slide 23).</strong>
    National estimates rank nontyphoidal <em>Salmonella</em> above <em>Listeria</em> for total deaths;
    <em>Listeria</em> has one of the highest death rates per case. Keyed as the slide says.</li>
    <li><strong>165&nbsp;&deg;F (slide 36).</strong> Food-safety agencies give 165&nbsp;&deg;F for poultry, leftovers and
    casseroles, and lower internal temperatures for other meats (160&nbsp;&deg;F for ground meat, 145&nbsp;&deg;F for
    whole cuts with a rest). Keyed as the slide says.</li>
    <li><strong>Names.</strong> The deck&rsquo;s &ldquo;S. enteriditis&rdquo; is <em>S. enteritidis</em>;
    &ldquo;parahemolyticus&rdquo; is <em>parahaemolyticus</em>.</li>
  </ul>

  <button type="button" class="test-yourself-btn" onclick="window.openTestYourself('Test yourself &mdash; Food Safety', TEST_YOURSELF.foodSafety)">Test yourself! &rarr;</button>
  <p class="src">Source: <em>Significant Microorganisms in Food Safety</em> (PAJ5200.FoodSafety-micro.pptx), Slides
  1&ndash;36, and the PAJ 5200 syllabus instructional objectives.</p>
</section>
"""

SECTION = SECTION_HEAD + BODY

TEST = """
    foodSafety: [
      {q:"Which is a food INTOXICATION rather than a food infection?",
       choices:["Salmonella gastroenteritis","Listeriosis","Botulism from a preformed toxin","Campylobacter diarrhea"],correct:2,
       explain:"Intoxication = a preformed toxin is eaten (Clostridium botulinum toxin, staphylococcal toxin). Salmonella and Listeria are food infections: live cells multiply."},
      {q:"Why is Listeria monocytogenes such a concern in stored food?",
       choices:["It is killed only by freezing","It grows from 1 to 40 C, even in the refrigerator","It needs a living host to grow","It only contaminates canned goods"],correct:1,
       explain:"Listeria grows well from 1 to 40 C, at refrigerator, room or freezer temperatures."},
      {q:"Which organism is the 'indicator organism' of fecal contamination?",
       choices:["Escherichia coli","Vibrio vulnificus","Bacillus cereus","Clostridium perfringens"],correct:0,
       explain:"E. coli is associated with human and animal feces; eosin methylene blue plates confirm it in food and water samples."},
      {q:"What does PulseNet hold?",
       choices:["Recall notices for pet food","Pulsed-field gel electrophoresis patterns of microbial isolates","Vaccine records","Restaurant inspection scores"],correct:1,
       explain:"Each isolate's pulsed-field gel electrophoresis pattern goes into the Centers for Disease Control and Prevention's PulseNet database, which finds outbreak causes and cuts detection time."},
      {q:"When is a person with hepatitis A most contagious?",
       choices:["About two weeks before symptoms","Only while jaundiced","After symptoms resolve","Only during vomiting"],correct:0,
       explain:"With the fecal-oral hepatitis viruses (A and E), a person is most contagious about two weeks BEFORE symptoms appear."}
    ],
"""
