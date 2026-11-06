# -*- coding: utf-8 -*-
"""Lecture 17 guide fragment (helminths): 17.20-17.41, slides 78-131, plus objective 2 (17.41) for every organism of
the lecture, protozoa and helminths. Joined by _micro_e3_guide_l17.py.

Every slide 78-131 was viewed as a 1920-pixel render and every picture extracted at full size. Picture-only or
picture-led slides in this range: 80-83 (life cycles A-D), 84 (Table 23.4, transcribed), 87 (Table 23.5,
transcribed), 88 (colonoscopy pictures), 90, 95, 97, 98, 102, 105, 109, 114, 117, 120, 122, 123 (life cycles and
specimens), 129 (Table 23.6, transcribed), 131 (the five arthropods). Left out: slide 78 (section title), slide 115
(a padlock on snails: a joke), slide 127 (the journal article page; one line on it in 17.39). Slide 88's four
pictures carry no labels, so their captions describe what is visible and do not pair them with a worm.

17.41 draws its protozoa cells from slides 4-8, 13 and 16-77 (deck text plus the renders of the picture tables).
"""
from _micro_e3_guide_l17_figs import fig, MH, CDC  # noqa: F401

TOC = """
  <a class="sub-link" href="#par-helminths">17.20 Objective 1 &mdash; Helminths: biology, hosts and the four life cycles</a>
  <a class="sub-link" href="#par-helm-path">17.21 Objective 1 &mdash; Pathology, defense, diagnosis and antihelminthic drugs</a>
  <a class="sub-link" href="#par-ascaris">17.22 Objective 1 &mdash; Nematodes and <em>Ascaris lumbricoides</em></a>
  <a class="sub-link" href="#par-trichuris">17.23 Objective 1 &mdash; <em>Trichuris trichiura</em> (whipworm)</a>
  <a class="sub-link" href="#par-enterobius">17.24 Objective 1 &mdash; <em>Enterobius vermicularis</em> (pinworm)</a>
  <a class="sub-link" href="#par-hookworm">17.25 Objective 1 &mdash; Hookworms: <em>Necator</em> and <em>Ancylostoma</em></a>
  <a class="sub-link" href="#par-angio">17.26 Objective 1 &mdash; <em>Angiostrongylus cantonensis</em> (rat lungworm)</a>
  <a class="sub-link" href="#par-strongy">17.27 Objective 1 &mdash; <em>Strongyloides stercoralis</em> (threadworm)</a>
  <a class="sub-link" href="#par-trichinella">17.28 Objective 1 &mdash; <em>Trichinella spiralis</em> and trichinellosis</a>
  <a class="sub-link" href="#par-wuchereria">17.29 Objective 1 &mdash; Tissue nematodes and <em>Wuchereria bancrofti</em></a>
  <a class="sub-link" href="#par-oncho">17.30 Objective 1 &mdash; <em>Onchocerca volvulus</em> and river blindness</a>
  <a class="sub-link" href="#par-loa">17.31 Objective 1 &mdash; <em>Loa loa</em>, the African eye worm</a>
  <a class="sub-link" href="#par-toxocara">17.32 Objective 1 &mdash; <em>Toxocara canis</em> and <em>Toxocara cati</em></a>
  <a class="sub-link" href="#par-dirofilaria">17.33 Objective 1 &mdash; <em>Dirofilaria</em> (heartworm)</a>
  <a class="sub-link" href="#par-schisto">17.34 Objective 1 &mdash; Trematodes and <em>Schistosoma</em> (blood flukes)</a>
  <a class="sub-link" href="#par-flukes">17.35 Objective 1 &mdash; Liver and lung flukes: <em>Opisthorchis</em> and <em>Paragonimus</em></a>
  <a class="sub-link" href="#par-fasciola">17.36 Objective 1 &mdash; <em>Fasciola hepatica</em></a>
  <a class="sub-link" href="#par-tsaginata">17.37 Objective 1 &mdash; Cestodes and <em>Taenia saginata</em> (beef tapeworm)</a>
  <a class="sub-link" href="#par-tsolium">17.38 Objective 1 &mdash; <em>Taenia solium</em> (pork tapeworm) and cysticercosis</a>
  <a class="sub-link" href="#par-echino">17.39 Objective 1 &mdash; <em>Echinococcus</em> and echinococcosis</a>
  <a class="sub-link" href="#par-arthropods">17.40 Objective 1 &mdash; The arthropod vectors</a>
  <a class="sub-link" href="#par-transmission">17.41 Objective 2 &mdash; How humans acquire every parasite in this lecture</a>"""

BODY = """
  <h3 class="sub" id="par-helminths">17.20 &middot; Objective 1 &mdash; Helminths: biology, hosts and the four life cycles</h3>
  <p><strong>Helminths are worms.</strong> <strong>Adults are large, multicellular animals with specialized tissues
  and organs.</strong> Adult worms mate and produce fertilized eggs that hatch; the larvae then mature in several
  stages to adults. The sexes may be separate or <strong>hermaphroditic</strong>. <strong>Sources of
  infection</strong>: contaminated food, soil, water, or infected animals. There are <strong>four basic patterns of
  life and transmission</strong> (cycles A to D, below).</p>
  <table>
    <tr><th>Host</th><th>What happens there (slide 79)</th></tr>
    <tr><td><strong>Definitive host</strong></td><td><mark class="prof-highlight"><strong>Adulthood and mating occur in
    the definitive host.</strong></mark> &#9733; Starred on the slide.</td></tr>
    <tr><td><strong>Intermediate host</strong></td><td>Larval development occurs here</td></tr>
    <tr><td><strong>Transport host</strong></td><td>Experiences <strong>no parasitic development</strong>. Slide 108
    calls it a <strong>paratenic host</strong>: &ldquo;a form of host in which the organism does not grow&mdash;transport
    host to definitive host&rdquo; (17.32).</td></tr>
  </table>
  <h4 class="subsub">The four life-cycle patterns (slides 80&ndash;83)</h4>
  <table>
    <tr><th>Cycle</th><th>What happens</th><th>Organisms the slides assign to it</th></tr>
    <tr><td><strong>A</strong><br>eggs swallowed</td><td>The human host <strong>ingests the mature egg in contaminated
    food or water</strong>. Larvae hatch and burrow through tissue; they may go to the lungs, then the pharynx, and be
    swallowed. The reproductive cycle is completed in the intestine, and eggs released in the feces complete the
    cycle.</td><td><em>Ascaris lumbricoides</em> (slide 91), <em>Trichuris trichiura</em> (slide 93); <em>Taenia
    saginata</em> is &ldquo;Cycle C and modified A&rdquo; (slide 119)</td></tr>
    <tr><td><strong>B</strong><br>larvae through the skin</td><td><strong>Infective larvae penetrate the skin</strong>,
    migrate through tissue to the lungs and pharynx and are swallowed. They reproduce in the intestine; eggs are
    released into the soil with feces, and the <strong>infective larvae are in the soil</strong> to complete the
    cycle.</td><td>The hookworms <em>Necator americanus</em> and <em>Ancylostoma duodenale</em> (slides 96&ndash;97),
    <em>Strongyloides stercoralis</em> (slide 100)</td></tr>
    <tr><td><strong>C</strong><br>encysted worm in meat</td><td>The human <strong>consumes the encysted worm in muscle
    (undercooked meat)</strong>. Gastric passage releases the larva from the cyst; worms mature and produce eggs that
    are released in the feces. A food animal grazes on grass contaminated with feces, the worm encysts in its muscle
    tissue, and the encysted forms are in the meat when the animal is slaughtered.</td><td><em>Trichinella
    spiralis</em> (slide 101); the cestodes (&ldquo;Flatworms&mdash;Cycle C&rdquo;, slide 118): <em>Taenia
    saginata</em> (slide 119) and <em>Taenia solium</em></td></tr>
    <tr><td><strong>D</strong><br>an intermediate host</td><td><strong>Involves an intermediate host.</strong>
    Infective larvae penetrate the skin or are consumed; they migrate through tissue to the lungs and pharynx and are
    swallowed, or go directly to the intestinal tract, and reproduce in the intestine. Eggs are released into water
    with feces, or the larval stage goes into the host&rsquo;s blood. The first larval stage infects intermediate
    hosts; these release <strong>second-stage larvae, which are infective, into water</strong>, or, if the intermediate
    hosts are <strong>biting insects, transmit to a new host through the bite</strong>.</td><td><em>Wuchereria
    bancrofti</em> and <em>Onchocerca volvulus</em> (&ldquo;with vector as intermediate host&rdquo;, slides 104 and
    106), <em>Loa loa</em> (slide 107), <em>Schistosoma</em> (slide 112), and the liver and lung flukes
    <em>Opisthorchis</em> and <em>Paragonimus</em> (&ldquo;Zoonotic&mdash;Cycle D&rdquo;, slide 116)</td></tr>
  </table>
  <p>The slides give no cycle letter for <em>Enterobius</em>, <em>Angiostrongylus</em>, <em>Toxocara</em>
  (&ldquo;complex life cycle with direct and indirect transmission&rdquo;), <em>Dirofilaria</em>, <em>Fasciola</em>
  or <em>Echinococcus</em>.</p>
  """ + fig(80, 1, "l17-s080-cycle-a.jpg",
      "A circular diagram split into a human half and an environment half: a face eating food and water, larvae hatching and entering tissue, a male and female worm symbol at the intestine, an embryonic egg and a mature egg.",
      "<b>Cycle A.</b> Food, water &rarr; larvae hatch, enter tissue &rarr; adults (male and female) in the "
      "intestine &rarr; an embryonic egg leaves in the feces and becomes a mature egg in the environment, which is "
      "swallowed again.") + """
  """ + fig(81, 1, "l17-s081-cycle-b.jpg",
      "A circular diagram: a bare foot with a larva entering it, larvae migrating, male and female symbols at the intestine, an egg, an early larva and an infective larva in the environment.",
      "<b>Cycle B.</b> An infective larva in the soil enters the bare foot, the larvae enter tissue and migrate, the "
      "adults reproduce in the intestine, and the egg passed into the environment hatches an early larva that "
      "becomes the infective larva.") + """
  """ + fig(82, 1, "l17-s082-cycle-c.jpg",
      "A circular diagram with human, food animal and environment sectors: a face eating meat, a stomach where a cyst releases larvae, the intestine with male and female symbols, eggs on the ground, a grazing cow, and a muscle with encysted larvae.",
      "<b>Cycle C.</b> Meat &rarr; the cyst releases larvae in the stomach &rarr; adults in the intestine &rarr; eggs "
      "in the environment &rarr; a grazing food animal &rarr; encystment in muscle &rarr; meat.") + """
  """ + fig(83, 1, "l17-s083-cycle-d.jpg",
      "A circular diagram with human, intermediate host and environment sectors: a face and a foot, an organ such as intestine or bladder, eggs and a first larval stage in the environment, intermediate hosts, a second larval stage, and animal flesh.",
      "<b>Cycle D.</b> Adults in an <b>organ such as the intestine or bladder</b> release eggs; the <b>first larval "
      "stage</b> in the environment infects the <b>intermediate host(s)</b>, which release the <b>second larval "
      "stage</b>; people are infected through the skin (the foot) or by eating it (animal flesh).") + """
  <h4 class="subsub">Table 23.4: Major helminths of humans and their modes of transmission (slide 84)</h4>
  <table>
    <tr><th>Classification</th><th>Common name of disease or worm</th><th>Life cycle requirement</th><th>Spread to humans by</th></tr>
    <tr><td colspan="4"><strong>Nematodes (Roundworms)</strong></td></tr>
    <tr><td><strong>Intestinal Nematodes</strong></td><td></td><td></td><td>Oral-fecal means</td></tr>
    <tr><td colspan="4">Infective in egg (embryo) stage</td></tr>
    <tr><td><em>Trichuris trichiura</em></td><td>Whipworm</td><td>Humans</td><td>Fecal pollution of soil with eggs</td></tr>
    <tr><td><em>Ascaris lumbricoides</em></td><td>Ascariasis</td><td>Humans</td><td>Fecal pollution of soil with eggs</td></tr>
    <tr><td><em>Enterobius vermicularis</em></td><td>Pinworm</td><td>Humans</td><td>Close contact and fomites</td></tr>
    <tr><td colspan="4">Infective in larval stage</td></tr>
    <tr><td><em>Necator americanus</em></td><td>New World hookworm</td><td>Humans</td><td>Fecal pollution of soil with eggs</td></tr>
    <tr><td><em>Ancylostoma duodenale</em></td><td>Old World hookworm</td><td>Humans</td><td>Fecal pollution of soil with eggs</td></tr>
    <tr><td><em>Strongyloides stercoralis</em></td><td>Threadworm</td><td>Humans; may live free</td><td>Fecal pollution of soil with eggs</td></tr>
    <tr><td><em>Trichinella spiralis</em></td><td>Trichina worm</td><td>Pigs, wild mammals</td><td>Consumption of meat containing larvae</td></tr>
    <tr><td><strong>Tissue Nematodes</strong></td><td></td><td></td><td>Burrowing of larva into tissue</td></tr>
    <tr><td><em>Wuchereria bancrofti</em></td><td>Filariasis</td><td>Humans, mosquitoes</td><td>Mosquito bite</td></tr>
    <tr><td><em>Onchocerca volvulus</em></td><td>River blindness</td><td>Humans, black flies</td><td>Fly bite</td></tr>
    <tr><td><em>Loa loa</em></td><td>Eye worm</td><td>Humans, mangrove flies, or deer flies</td><td>Fly bite</td></tr>
    <tr><td colspan="4"><strong>Trematodes</strong></td></tr>
    <tr><td><em>Schistosoma japonicum</em></td><td>Blood fluke</td><td>Humans and snails</td><td>Ingestion of fresh water containing larval stage</td></tr>
    <tr><td><em>S. mansoni</em></td><td>Blood fluke</td><td>Humans and snails</td><td>Ingestion of fresh water containing larval stage</td></tr>
    <tr><td><em>S. haematobium</em></td><td>Blood fluke</td><td>Humans and snails</td><td>Ingestion of fresh water containing larval stage</td></tr>
    <tr><td><em>Opisthorchis sinensis</em></td><td>Chinese liver fluke</td><td>Humans, snails, fish</td><td>Consumption of fish</td></tr>
    <tr><td><em>Fasciola hepatica</em></td><td>Sheep liver fluke</td><td>Herbivores (sheep, cattle)</td><td>Consumption of water and water plants</td></tr>
    <tr><td><em>Paragonimus westermani</em></td><td>Oriental lung fluke</td><td>Humans, mammals, snails, freshwater crabs</td><td>Consumption of crabs</td></tr>
    <tr><td colspan="4"><strong>Cestodes</strong></td></tr>
    <tr><td><em>Taenia saginata</em></td><td>Beef tapeworm</td><td>Humans, cattle</td><td>Consumption of undercooked or raw beef</td></tr>
    <tr><td><em>T. solium</em></td><td>Pork tapeworm</td><td>Humans, swine</td><td>Consumption of undercooked or raw pork</td></tr>
    <tr><td><em>Diphyllobothrium latum</em></td><td>Fish tapeworm</td><td>Humans, fish</td><td>Consumption of undercooked or raw fish</td></tr>
    <tr><td><em>Hymenolepis nana</em></td><td>Dwarf tapeworm</td><td>Humans</td><td>Oral-fecal; close contact</td></tr>
  </table>
  <div class="callout"><strong>One cell in this table disagrees with the rest of the deck.</strong> Table 23.4 says
  people get <em>Schistosoma</em> by &ldquo;ingestion of fresh water containing larval stage&rdquo;; slides 8 and
  112&ndash;114 say the larva (cercaria) <strong>penetrates the skin</strong> during contact with the snail&rsquo;s water.
  The guide teaches skin penetration and flags the table (17.34, 17.42).</div>
  """ + fig(84, 1, "l17-s084-table-23-4.jpg",
      "A textbook table titled Table 23.4, Major Helminths of Humans and Their Modes of Transmission, with sections for nematodes, trematodes and cestodes.",
      "<b>Table 23.4</b> as it appears on the slide (transcribed above).") + """

  <h3 class="sub" id="par-helm-path">17.21 &middot; Objective 1 &mdash; Pathology, defense, diagnosis and antihelminthic drugs</h3>
  <table>
    <tr><th>Adaptations to parasitism</th><th>Pathology arises from</th><th>Effects</th></tr>
    <tr><td>Specialized <strong>mouthparts for attachment</strong><br>Enzymes to <strong>hydrolyze tissue</strong><br><strong>Cuticle</strong>
    for protection against immune defense<br><strong>Reduction of organ systems</strong></td>
    <td><mark class="prof-highlight">Worms <strong>feeding on and migrating through tissues</strong><br><strong>Accumulation of worms in organs, causing
    blockages</strong><br><strong>Toxic worm secretions</strong></mark></td>
    <td><mark class="prof-highlight">Enlargement and swelling of organs<br>Hemorrhage<br>Weight loss<br>Anemia</mark></td></tr>
  </table>
  <p>&#9733; Dr. Webster on the middle and right columns: &ldquo;Why do we have pathology for worms? This is something you
  should know. ... This is an important thing.&rdquo; She called Table 23.4 (slide 84) and Table 23.5 (slide 87, below) charts
  she is not asking you to memorize.</p>
  <ul>
    <li><strong>Defense against worms: eosinophils.</strong> Worms are often difficult to eliminate completely without
    drugs.</li>
    <li><strong>Diagnosis</strong> is based on the <strong>blood cell count (eosinophilia)</strong>, <strong>serological
    tests</strong>, and <strong>eggs, larvae, or adult worms in feces</strong>; sputum, urine, blood, or tissue
    biopsies.</li>
    <li><strong>Antihelminthic drugs</strong> suppress a helminthic metabolic process that differs from the human
    process, inhibit the worm&rsquo;s movement, prevent it from holding position, and act locally in the intestine.
    <strong>Many antihelminthic drugs have toxic side effects.</strong></li>
  </ul>
  <h4 class="subsub">Table 23.5: Antihelminthic therapeutic agents and indications for their use (slide 87)</h4>
  <table>
    <tr><th>Drug</th><th>Effect</th><th>Used for</th></tr>
    <tr><td><strong>Albendazole</strong></td><td>Blocks key step in worm metabolism</td><td>Filariasis, ascariasis</td></tr>
    <tr><td><strong>Diethylcarbamazine</strong></td><td>Unknown, but kills microfilariae; does not kill adult worm</td><td>Filariasis, loiasis</td></tr>
    <tr><td><strong>Ivermectin</strong></td><td>Blocks nerve transmission</td><td>Onchocerciasis, ascariasis, strongyloidiasis</td></tr>
    <tr><td><strong>Mebendazole</strong></td><td>Blocks key step in worm metabolism</td><td>Trichuriasis (whipworm), ascariasis, hookworm, trichinosis</td></tr>
    <tr><td><strong>Metrifonate</strong></td><td>Paralyzes worm</td><td>Schistosomiasis</td></tr>
    <tr><td><strong>Niclosamide</strong></td><td>Inhibits ATP (adenosine triphosphate) formation in worm; destroys proglottids but not eggs</td><td>Tapeworm</td></tr>
    <tr><td><strong>Niridazole</strong></td><td>Alters worm metabolism</td><td>Schistosomiasis</td></tr>
    <tr><td><strong>Piperazine</strong></td><td>Paralyzes worm so it can be expelled in feces</td><td>Ascariasis, pinworm, hookworm</td></tr>
    <tr><td><strong>Praziquantel</strong></td><td>Interferes with worm metabolism</td><td>Schistosomiasis, other flukes, tapeworm</td></tr>
    <tr><td><strong>Pyrantel</strong></td><td>Paralyzes worm so it can be expelled in feces</td><td>Pinworm, hookworm, trichinosis</td></tr>
    <tr><td><strong>Thiabendazole</strong></td><td>Blocks key step in worm metabolism</td><td>Strongyloidiasis, guinea worm, hookworm trichinosis</td></tr>
  </table>
  """ + fig(87, 1, "l17-s087-table-23-5.jpg",
      "A textbook table titled Table 23.5, Antihelminthic Therapeutic Agents and Indications for Their Use, with columns Drug, Effect and Used For.",
      "<b>Table 23.5</b> as it appears on the slide (transcribed above). Each organism section below gives the "
      "drugs its own slide names.") + """
  <h4 class="subsub">Colonoscopy surprises (slide 88)</h4>
  <p>Four intestinal worms the slide lists as things found on colonoscopy, each with its common name:
  <strong><em>Ascaris lumbricoides</em>, roundworm</strong>; <strong><em>Trichuris trichiura</em>, whipworm</strong>;
  <strong><em>Enterobius vermicularis</em>, pinworms</strong>; <strong><em>Taenia solium</em>, tapeworm</strong>. The
  four pictures beside the list are not labeled with a worm&rsquo;s name.</p>
  """ + fig(88, 1, "l17-s088-intestine-worm-mass.jpg",
      "An illustration of a translucent human torso with a magnified circle showing a dense mass of pale worms packed inside the intestine.",
      "<b>Colonoscopy surprises.</b> An illustration beside the <em>Ascaris</em> line: a mass of pale worms packed "
      "inside the intestine (slide 92: heavy worm loads can cause intestinal obstruction).") + """
  """ + fig(88, 2, "l17-s088-many-small-worms.jpg",
      "A close view of red bowel lining with many small, curled, white worms and white specks scattered over it.",
      "<b>Colonoscopy surprises.</b> Many small, curled white worms on the red lining of the bowel.") + """
  """ + fig(88, 3, "l17-s088-single-white-worm.jpg",
      "A colonoscopy view of pink bowel lining with a single slender white worm curving across it.",
      "<b>Colonoscopy surprises.</b> A single slender white worm on the pink lining of the bowel.") + """
  """ + fig(88, 4, "l17-s088-flat-worm-in-lumen.jpg",
      "A colonoscopy view down the bowel lumen with a long, flat, pale, ribbon-like worm lying along the wall.",
      "<b>Colonoscopy surprises.</b> A long, flat, ribbon-like worm in the bowel lumen, the picture beside the "
      "<em>Taenia solium</em> (tapeworm) line.") + """

  <h3 class="sub" id="par-ascaris">17.22 &middot; Objective 1 &mdash; Nematodes and <em>Ascaris lumbricoides</em></h3>
  <h4 class="subsub">Nematodes (roundworms), slide 89</h4>
  <p>One of the <strong>most abundant animal groups</strong>; <strong>50 species affect humans</strong>.
  <strong>Elongated, cylindrical worms with protective cuticles, circular muscles, a complete digestive tract, and
  separate sexes.</strong> They are divided into <strong>intestinal nematodes</strong> (17.22&ndash;17.28) and
  <strong>tissue nematodes</strong> (17.29&ndash;17.31).</p>
  <h4 class="subsub"><em>Ascaris lumbricoides</em> (ascariasis), slides 90&ndash;92</h4>
  <ul>
    <li><strong>Morphology:</strong> a <strong>large intestinal roundworm</strong> (the common name on slides 6 and 88:
    roundworm).</li>
    <li><strong>Where and hosts:</strong> <strong>indigenous to humans</strong>; it spends its larval and adult stages
    in humans. Most cases in the United States occur in the <strong>southeastern states</strong>.</li>
    <li><strong>How people acquire it (Life Cycle A):</strong> embryonic eggs are released in feces and spread to other
    humans through <strong>food, drink, or contaminated objects</strong> (Table 23.4: fecal pollution of soil with
    eggs). <strong>Ingested eggs hatch into larvae, burrow through the intestine into the circulation, travel to the
    lungs and pharynx, and are swallowed.</strong> Adult worms complete the cycle in the intestine and reproduce:
    <strong>200,000 eggs a day</strong>.</li>
    <li><strong>Disease:</strong> the worms <strong>retain motility and do not attach</strong>. <strong>Severe
    inflammatory reactions mark the migratory route</strong>, and allergic reactions can occur. <strong>Heavy worm
    loads can cause abdominal pain and intestinal obstruction.</strong> Lung migration may cause pulmonary symptoms:
    <strong>eosinophilic pneumonitis</strong>. It may <strong>retard physical and mental development</strong>.</li>
    <li><strong>Diagnosis:</strong> microscopic or macroscopic analysis.</li>
    <li><strong>Treatment:</strong> albendazole with mebendazole, ivermectin, and nitazoxanide, for 1&ndash;3 days
    (slide 92). Table 23.5 lists albendazole, ivermectin, mebendazole and piperazine for ascariasis.</li>
  </ul>
  """ + fig(90, 1, "l17-s090-ascaris-adults-eggs.jpg",
      "Above, two long, smooth, cream-colored worms on a dark background; below, two oval eggs with thick, irregular outer coats on a yellow background.",
      "<b><em>Ascaris lumbricoides</em>.</b> Above, adult worms: large, smooth, cylindrical roundworms. Below, two "
      "eggs, each with a thick outer coat.", crop=(0, 0, 490, 598)) + """
  """ + fig(90, 2, "l17-s090-ascaris-cycle.jpg",
      "A numbered life-cycle diagram: a human outline with lungs and intestine, a male and female worm in a box, fertilized and unfertilized eggs passing in feces to soil, eggs developing and an infective egg being swallowed.",
      "<b>The <em>Ascaris</em> life cycle (Cycle A).</b> (1) Adult female and male worms in the intestine; (2) "
      "<b>fertilized eggs</b> and <b>unfertilized eggs</b> (which will not undergo biological development) pass in the "
      "feces (both are the diagnostic stage); (3) the fertilized egg develops in the soil to the <b>infective "
      "stage</b>, which is swallowed (4); the larva (5) travels to the lungs (6) and up the airway to be swallowed "
      "(7), as slide 91 describes.", CDC) + """

  <h3 class="sub" id="par-trichuris">17.23 &middot; Objective 1 &mdash; <em>Trichuris trichiura</em> (whipworm)</h3>
  <ul>
    <li><strong>Common name:</strong> whipworm (trichuriasis).</li>
    <li><strong>Hosts and where:</strong> <strong>humans are the sole host</strong>. Trichuriasis has its highest
    incidence in the <strong>tropics</strong>; in the United States, in the <strong>South</strong>.</li>
    <li><strong>How people acquire it (Life Cycle A):</strong> eggs (Table 23.4: fecal pollution of soil with eggs)
    are swallowed and <strong>hatch in the intestines; the larvae attach, penetrate the outer wall and develop into
    adults</strong>. Females lay <strong>3,000&ndash;5,000 eggs daily</strong>.</li>
    <li><strong>Disease:</strong> worms can <strong>pierce capillaries and cause localized hemorrhage</strong>.
    <strong>Heavy infestations can cause dysentery and rectal prolapse</strong>, and can be fatal in children.</li>
    <li><strong>Treatment:</strong> <strong>mebendazole is the drug of choice</strong>, with albendazole as an
    alternative (Table 23.5: mebendazole for trichuriasis).</li>
  </ul>
  """ + fig(93, 1, "l17-s093-trichuris-egg.jpg",
      "A micrograph of a single brown, oval, barrel-shaped egg with a clear knob at each end and a granular center.",
      "<b><em>Trichuris trichiura</em> egg</b>, the picture on the whipworm slide: oval and barrel-shaped, with a "
      "knob at each end.") + """

  <h3 class="sub" id="par-enterobius">17.24 &middot; Objective 1 &mdash; <em>Enterobius vermicularis</em> (pinworm)</h3>
  <ul>
    <li><strong>Common names:</strong> <strong>pinworm or seatworm</strong> (enterobiasis).
    <mark class="prof-highlight"><strong>Enterobiasis is the most common worm disease of children in temperate
    zones.</strong></mark> &#9733; Starred on the slide. Slide 6: <strong>very common in daycare
    situations</strong>. &#9733; Dr. Webster: &ldquo;the one that you will almost surely see in your clinical life&rdquo;,
    &ldquo;the scourge of the daycare center&rdquo;.</li>
    <li><strong>How people acquire it:</strong> <strong>eggs are picked up from the surroundings and swallowed</strong>;
    slide 6 and Table 23.4: transmission by <strong>direct (close) contact and fomites</strong>. <strong>Self-inoculation
    is common.</strong></li>
    <li><strong>Life cycle:</strong> after hatching in the small intestine, the eggs develop into adults. <strong>Anal
    itching occurs when mature females emerge from the intestine to release eggs.</strong></li>
    <li><strong>Diagnosis:</strong> the <strong>tape test</strong> (slide 6: &ldquo;Diagnosed with Scotch tape
    test&rdquo;).</li>
    <li><strong>Treatment:</strong> <strong>pyrantel pamoate</strong> (Table 23.5: pyrantel and piperazine for
    pinworm).</li>
  </ul>
  """ + fig(95, 2, "l17-s095-pinworm-adults.jpg",
      "Three thin, white, thread-like worms with pointed tails lying on dark blue cloth.",
      "<b><em>Enterobius vermicularis</em> adults</b>: small, thin, white worms with pointed ends.") + """
  """ + fig(95, 3, "l17-s095-pinworm-eggs.jpg",
      "A micrograph of three clear oval eggs side by side, each with a thin shell and granular contents.",
      "<b>Pinworm eggs</b>, the stage the tape test picks up from the perianal folds.") + """
  """ + fig(95, 1, "l17-s095-pinworm-cycle.jpg",
      "A numbered life-cycle diagram: eggs on the perianal folds, embryonated eggs swallowed by a human, larvae hatching in the small intestine, adult male and female worms in the cecum, and a gravid female migrating to the perianal region.",
      "<b>The pinworm life cycle.</b> (1) <b>Eggs on perianal folds</b>; larvae inside the eggs mature within 4 to 6 "
      "hours (diagnostic stage). (2) <b>Embryonated eggs ingested by human</b> (infective stage). (3) Larvae hatch in "
      "the small intestine. (4) Adults in the lumen of the cecum. (5) The <b>gravid female migrates to the perianal "
      "region at night to lay eggs</b>.", CDC) + """

  <h3 class="sub" id="par-hookworm">17.25 &middot; Objective 1 &mdash; Hookworms: <em>Necator americanus</em> and <em>Ancylostoma duodenale</em></h3>
  <ul>
    <li><strong>Morphology:</strong> <strong>characteristic curved ends and hooked mouths</strong>. Two species:
    <em>Necator americanus</em> (the New World hookworm) and <em>Ancylostoma duodenale</em> (the Old World hookworm),
    Table 23.4.</li>
    <li><strong>How people acquire it (Life Cycle B):</strong> humans shed eggs in feces, which hatch into
    <strong>filariform larvae</strong> that <strong>burrow into the skin of bare feet</strong> (slide 6:
    &ldquo;transmitted through skin on soles of feet&rdquo;). The larvae travel from the blood to the lungs, proceed up
    the bronchi and throat and are swallowed; the worms mature and reproduce in the small intestine and complete the
    cycle.</li>
    <li><strong>Disease:</strong> may cause <strong>pneumonia, nausea, vomiting, cramps, and bloody diarrhea</strong>.
    <strong>Blood loss is significant: anemia.</strong></li>
    <li><strong>Treatment:</strong> albendazole, mebendazole or pyrantel pamoate (Table 23.5 also lists piperazine and
    thiabendazole for hookworm).</li>
  </ul>
  """ + fig(97, 1, "l17-s097-hookworm-adults-mouth.jpg",
      "Left, drawings of a male and a larger female hookworm beside a millimeter scale, and two oval eggs beside a micrometer scale labeled egg stages in feces; right, two micrographs of a worm's head with a large mouth lined with teeth.",
      "<b>The hookworms.</b> (a) Adult male and female against a 0&ndash;15&nbsp;mm scale, and the <b>egg stages in "
      "feces (diagnostic stage)</b> against a micrometer scale. (b) The <b>hooked mouths</b>: the head end of the "
      "worm, with teeth visible in the mouth.", "&copy; R. Calentine/Visuals Unlimited.") + """
  """ + fig(97, 2, "l17-s097-hookworm-cycle.jpg",
      "A numbered life-cycle diagram: eggs in feces, a rhabditiform larva hatching, a filariform larva, the larva penetrating the skin of a foot, and adults in the small intestine of a human outline with lungs highlighted.",
      "<b>The hookworm life cycle (Cycle B).</b> (1) <b>Eggs in feces</b> (diagnostic stage); (2) a rhabditiform "
      "larva hatches; (3) it becomes the <b>filariform larva</b>; (4) the <b>filariform larva penetrates skin</b> "
      "(infective stage); the larvae pass through the lungs to the gut; (5) adults in the small intestine.", CDC) + """

  <h3 class="sub" id="par-angio">17.26 &middot; Objective 1 &mdash; <em>Angiostrongylus cantonensis</em> (rat lungworm)</h3>
  <ul>
    <li><strong>What it is:</strong> the <strong>rat lungworm</strong>, a <strong>nematode that causes eosinophilic
    meningitis</strong>. <strong>Snails are intermediate hosts.</strong></li>
    <li><strong>How people acquire it:</strong> by <strong>ingesting contaminated snails, water, or vegetables</strong>
    (slide 7: &ldquo;acquired by eating larvae in snails or contaminated water or vegetables&rdquo;).</li>
    <li><strong>Disease:</strong> incubation period <strong>1 day to 6 weeks</strong>. Symptoms of bacterial
    meningitis: nausea, vomiting, headaches, <strong>stiff neck</strong>.</li>
    <li><strong>Diagnosis:</strong> <strong>lumbar puncture shows elevated eosinophils instead of
    neutrophils</strong>.</li>
    <li><strong>Outcome:</strong> some patients recover on their own, because the parasite does not survive long in
    the human body; others experience coma and death. The slides name no treatment.</li>
    <li><strong>Prevention:</strong> <strong>snail and slug control</strong> and <strong>washing contaminated fruits and
    vegetables</strong>.</li>
  </ul>
  """ + fig(98, 2, "l17-s098-angiostrongylus-worm.jpg",
      "A drawing of a long, coiled worm with a dark spiral stripe wound along its body, under the heading Angiostrongylus cantonensis, with a printed caption.",
      "<b>Adult female worm of <em>Angiostrongylus cantonensis</em></b> with its characteristic <b>barber-pole "
      "appearance</b> (anterior end of the worm is to the top; scale bar 1&nbsp;mm), as printed on the picture.") + """
  """ + fig(98, 1, "l17-s098-angiostrongylus-cycle.jpg",
      "A diagram with lettered arrows: a rat at the top, snails and a slug below it, arrows from the snails to frogs, a crab, shrimp and a lizard, to lettuce and fruit, and to a human figure whose brain is colored red.",
      "<b>The rat lungworm cycle.</b> Larvae pass between the <b>rat</b> (A) and <b>snails and slugs</b> (B, C). From "
      "the snails, arrows run to <b>frogs, crabs, shrimp and a lizard</b> (D), straight to a <b>person</b> (E), and onto "
      "<b>vegetables and fruit</b> (G); arrows F and H carry larvae from those animals and that produce to the person, "
      "whose <b>brain</b> is highlighted; arrow I returns to the rat. The letters have no key on the slide.") + """

  <h3 class="sub" id="par-strongy">17.27 &middot; Objective 1 &mdash; <em>Strongyloides stercoralis</em> (threadworm)</h3>
  <ul>
    <li><strong>Morphology and where:</strong> the <strong>threadworm</strong>: tiny roundworms that complete the life
    cycle <strong>in humans or in moist soil</strong> (Table 23.4: humans; may live free).</li>
    <li><strong>How people acquire it (Life Cycle B):</strong> <strong>larvae penetrate the skin</strong>, migrate to
    the lungs, are swallowed, and complete development in the intestine. <strong>It can reinfect the same host
    without leaving the body.</strong></li>
    <li><strong>Disease:</strong> heavy worm loads can cause <strong>pneumonitis and eosinophilia</strong>, bloody
    diarrhea, liver enlargement, bowel obstruction, and malabsorption.</li>
    <li><strong>Treatment:</strong> <strong>ivermectin</strong>, with albendazole as the alternative (Table 23.5:
    ivermectin and thiabendazole for strongyloidiasis).</li>
  </ul>
  """ + fig(100, 1, "l17-s100-strongyloides-in-tissue.jpg",
      "A pink-stained tissue section with a slender, purple-stained worm lying among the fibers.",
      "<b><em>Strongyloides stercoralis</em></b>: a slender threadworm (stained purple) in tissue.") + """

  <h3 class="sub" id="par-trichinella">17.28 &middot; Objective 1 &mdash; <em>Trichinella spiralis</em> and trichinellosis</h3>
  <ul>
    <li><strong>Names:</strong> trichinellosis; slide 7 and Table 23.5 say <strong>trichinosis</strong>, Table 23.4
    the <strong>trichina worm</strong>.</li>
    <li><strong>Hosts:</strong> the <strong>life cycle is entirely within the mammalian host</strong> (Table 23.4: pigs,
    wild mammals). The slide assigns it <strong>Life Cycle C</strong>.</li>
    <li><strong>How people acquire it:</strong> from <strong>eating undercooked pork or bear meat</strong> (Table
    23.4: consumption of meat containing larvae).</li>
    <li><strong>In the body:</strong> larvae migrate from the intestine to the blood vessels, <strong>muscle, heart,
    and brain, where they form cysts</strong>. Slide 7: &ldquo;encystment in muscle will cause symptoms&rdquo;.</li>
    <li><strong>Disease:</strong> first symptoms flulike, with diarrhea; second symptoms <strong>muscle and joint
    pain</strong>, shortness of breath, <strong>pronounced eosinophilia</strong>. Occasional life-threatening
    manifestations: <strong>myocarditis, central nervous system involvement, and pneumonitis</strong>.</li>
    <li><strong>Treatment:</strong> <strong>steroids, plus mebendazole or albendazole</strong>. <mark class="prof-highlight"><strong>No cure after
    the larvae have encysted.</strong></mark> &#9733; Dr. Webster said it twice (&ldquo;You cannot cure it. You cannot
    cure it.&rdquo;) and: &ldquo;Do not eat your pork rare.&rdquo; (Table 23.5 lists mebendazole, pyrantel and thiabendazole for trichinosis.)</li>
  </ul>
  """ + fig(101, 1, "l17-s101-trichinella-muscle.jpg",
      "A stained section of muscle fibers with several coiled larvae, each inside an oval cyst between the fibers.",
      "<b><em>Trichinella spiralis</em> in muscle</b>: coiled larvae, each in its cyst between the muscle fibers "
      "(slide 7 shows the same picture).") + """
  """ + fig(102, 1, "l17-s102-trichinellosis-cycle.jpg",
      "A woman with the stomach and intestine drawn in, a ham, a pig with a Trichinella cyst marked in its muscle, a magnified intestinal lining, and a circle showing a coiled larva in a muscle biopsy, with four labeled boxes.",
      "<b>The cycle of trichinellosis.</b> (a) <b>Larvae encysted in animal muscle are the infective stage</b> (the "
      "<em>Trichinella</em> cyst in the pig, eaten as meat). (b) When ingested, cysts hatch and mature in the intestinal "
      "lining. (c) Adults reproduce and form new larvae, which burrow through the intestine and enter the circulation. "
      "(d) Larvae eventually form <b>cysts in skeletal muscle that can remain for years</b>; the circle shows a biopsy "
      "of human skeletal muscle infected with the coiled larvae of <em>Trichinella spiralis</em>.") + """
  <h4 class="subsub">The intestinal nematodes side by side</h4>
  <table>
    <tr><th>Worm</th><th>Cycle</th><th>How people acquire it</th><th>Disease to know</th><th>Diagnosis</th><th>Treatment named on its slide</th></tr>
    <tr><td><em>Ascaris lumbricoides</em> (roundworm)</td><td>A</td><td>Eggs in food, drink, contaminated objects</td><td>Lung migration (eosinophilic pneumonitis); intestinal obstruction; retarded development</td><td>Microscopic or macroscopic analysis</td><td>Albendazole with mebendazole, ivermectin, nitazoxanide</td></tr>
    <tr><td><em>Trichuris trichiura</em> (whipworm)</td><td>A</td><td>Eggs swallowed; humans sole host</td><td>Localized hemorrhage; dysentery, rectal prolapse</td><td>&mdash;</td><td>Mebendazole (albendazole alternative)</td></tr>
    <tr><td><em>Enterobius vermicularis</em> (pinworm)</td><td>&mdash;</td><td>Eggs from surroundings; close contact, fomites; self-inoculation</td><td>Anal itching; most common worm disease of children in temperate zones &#9733;</td><td>Tape test</td><td>Pyrantel pamoate</td></tr>
    <tr><td>Hookworms (<em>Necator</em>, <em>Ancylostoma</em>)</td><td>B</td><td>Filariform larvae through the skin of bare feet</td><td>Pneumonia, bloody diarrhea; blood loss and anemia</td><td>&mdash;</td><td>Albendazole, mebendazole or pyrantel pamoate</td></tr>
    <tr><td><em>Strongyloides stercoralis</em> (threadworm)</td><td>B</td><td>Larvae through the skin; can reinfect the same host</td><td>Pneumonitis, eosinophilia, malabsorption</td><td>&mdash;</td><td>Ivermectin (albendazole alternative)</td></tr>
    <tr><td><em>Trichinella spiralis</em></td><td>C</td><td>Undercooked pork or bear meat</td><td>Muscle cysts; myocarditis; pronounced eosinophilia</td><td>&mdash;</td><td>Steroids plus mebendazole or albendazole</td></tr>
    <tr><td><em>Angiostrongylus cantonensis</em> (rat lungworm)</td><td>&mdash;</td><td>Snails, water, vegetables</td><td>Eosinophilic meningitis</td><td>Lumbar puncture: eosinophils instead of neutrophils</td><td>None named</td></tr>
  </table>

  <h3 class="sub" id="par-wuchereria">17.29 &middot; Objective 1 &mdash; Tissue nematodes and <em>Wuchereria bancrofti</em></h3>
  <h4 class="subsub">Tissue nematodes (slide 103)</h4>
  <p>Tissue nematodes <strong>complete their life cycle in human blood, lymphatics, or skin</strong>. They are
  <strong>filarial worms</strong>: elongate, filamentous bodies, <strong>spread by biting arthropods</strong>. They
  <strong>cause chronic, deforming disease</strong>:</p>
  <table>
    <tr><th>Worm</th><th>Disease</th></tr>
    <tr><td><em>Wuchereria bancrofti</em></td><td><strong>Elephantiasis</strong></td></tr>
    <tr><td><em>Onchocerca volvulus</em></td><td><strong>River blindness</strong></td></tr>
    <tr><td><em>Loa loa</em></td><td><strong>Eye worm</strong></td></tr>
  </table>
  <h4 class="subsub"><em>Wuchereria bancrofti</em> and bancroftian filariasis (slides 104&ndash;105)</h4>
  <ul>
    <li><strong>Where and vector:</strong> a <strong>tropical infection spread by mosquitoes</strong>; <strong>Life
    Cycle D with the vector as intermediate host</strong>. Table 23.6: <em>Anopheles</em>/<em>Culex</em> mosquitoes,
    worldwide in the tropics.</li>
    <li><strong>How people acquire it:</strong> the <strong>vector deposits larvae, which move into the lymphatics and
    develop into adults</strong> (Table 23.4: mosquito bite).</li>
    <li><strong>Disease:</strong> chronic infection causes <strong>blockage of the lymphatic circulation and
    elephantiasis, massive swelling in the extremities</strong>.</li>
    <li><strong>Treatment:</strong> albendazole, and &ldquo;mectizan (only for filarial stage)&rdquo; (slide 104).
    Table 23.5: albendazole and diethylcarbamazine for filariasis; diethylcarbamazine kills microfilariae but does
    not kill the adult worm.</li>
  </ul>
  """ + fig(105, 1, "l17-s105-bancroftian-filariasis.jpg",
      "Left, a stained blood smear with a long, slender, thread-like worm curving among scattered blood cells; right, a person's legs and feet, both massively swollen with thickened, folded skin.",
      "<b>Bancroftian filariasis.</b> Left, a long, slender filarial worm among scattered cells in a stained smear. "
      "Right, <b>elephantiasis</b>: massive swelling of both legs where the lymphatic circulation is blocked.") + """

  <h3 class="sub" id="par-oncho">17.30 &middot; Objective 1 &mdash; <em>Onchocerca volvulus</em> and river blindness</h3>
  <ul>
    <li><strong>Vector:</strong> <strong>transmitted by biting black flies</strong>; <strong>Life Cycle D with the vector
    as intermediate host</strong>. Table 23.6: black fly, onchocerciasis, nematode, Africa and Latin America.</li>
    <li><strong>In the body:</strong> larvae develop into adults in the <strong>subcutaneous tissues</strong>. Adult
    females migrate via the blood to the eyes, provoking inflammatory reactions.</li>
    <li><strong>Why blindness:</strong> <strong>coinfection with <em>Wolbachia</em> bacteria causes river
    blindness</strong>. The bacteria are an <strong>endosymbiont</strong>, and the bacterial antigens stimulate an
    inflammation that <strong>damages the cornea, retina and optic nerve</strong>. (Slide 8: &ldquo;Spread by black
    flies. Bacterial coinfection.&rdquo;)</li>
    <li><strong>Treatment:</strong> <strong>tetracycline and ivermectin</strong> (Table 23.5: ivermectin for
    onchocerciasis).</li>
  </ul>

  <h3 class="sub" id="par-loa">17.31 &middot; Objective 1 &mdash; <em>Loa loa</em>, the African eye worm</h3>
  <ul>
    <li><strong>Vector:</strong> <strong>spread by the bite of small flies</strong> (Table 23.4: humans, mangrove flies,
    or deer flies; fly bite). <strong>Life Cycle D.</strong></li>
    <li><strong>Disease:</strong> a <strong>temperature-sensitive worm that migrates around and under the skin and may
    enter the eye</strong>.</li>
    <li><strong>Treatment:</strong> <strong>pull the worm from a small hole in the conjunctiva</strong>, or
    <strong>diethylcarbamazine</strong> (Table 23.5: diethylcarbamazine for filariasis and loiasis).</li>
  </ul>
  """ + fig(107, 1, "l17-s107-loa-loa-eye.jpg",
      "A close-up of an eye held open with a metal instrument, with a thin white worm being drawn out from the red conjunctiva.",
      "<b><em>Loa loa</em> removed from the eye</b>: the worm is pulled out through a small hole in the "
      "conjunctiva.") + """
  <h4 class="subsub">The filarial worms side by side</h4>
  <table>
    <tr><th>Worm</th><th>Vector (the intermediate host)</th><th>Where the adults live</th><th>Disease</th><th>Treatment named on its slide</th></tr>
    <tr><td><em>Wuchereria bancrofti</em></td><td>Mosquitoes</td><td>Lymphatics</td><td>Bancroftian filariasis: lymphatic blockage, elephantiasis</td><td>Albendazole, &ldquo;mectizan&rdquo;</td></tr>
    <tr><td><em>Onchocerca volvulus</em></td><td>Black flies</td><td>Subcutaneous tissues; females migrate to the eyes</td><td>River blindness (with <em>Wolbachia</em>)</td><td>Tetracycline and ivermectin</td></tr>
    <tr><td><em>Loa loa</em></td><td>Small flies (mangrove or deer flies)</td><td>Around and under the skin; may enter the eye</td><td>African eye worm</td><td>Pull it out through the conjunctiva, or diethylcarbamazine</td></tr>
    <tr><td><em>Dirofilaria</em> (17.33)</td><td>&ldquo;Vector-borne&rdquo; (vector not named)</td><td>Dogs: causes heartworm. Humans: suboptimal hosts (lungs, skin)</td><td>Lung coin lesions; skin nodules</td><td>None named</td></tr>
  </table>

  <h3 class="sub" id="par-toxocara">17.32 &middot; Objective 1 &mdash; <em>Toxocara canis</em> and <em>Toxocara cati</em> (toxocariasis)</h3>
  <ul>
    <li><strong>What they are:</strong> the <strong>dog and cat roundworms</strong>. The slide&rsquo;s title tags
    toxocariasis &ldquo;(NPI)&rdquo;: it is one of the five neglected parasitic infections of the Centers for Disease
    Control and Prevention on slide 10 (with Chagas disease, cysticercosis, toxoplasmosis and trichomoniasis).</li>
    <li><strong>Life cycle:</strong> complex, with <strong>direct and indirect transmission</strong>.</li>
    <li><strong>How people acquire it:</strong> <strong>humans are accidental hosts</strong>, infected by
    <strong>ingesting infective eggs from feces</strong>, or by <strong>consuming the undercooked meat of a paratenic
    host</strong> (a host in which the organism does not grow: a transport host to the definitive host). Slide 8:
    &ldquo;ingestion of feces or undercooked alternate host (waterfowl)&rdquo;.</li>
    <li><strong>Disease:</strong> the <strong>larvae migrate through the tissues</strong>. <strong>Ocular
    toxocariasis</strong>: migration to the eye, which may lead to visual impairment and total blindness.
    <strong>Visceral toxocariasis</strong>: inflammation and severe damage to the liver. The slides name no
    treatment.</li>
  </ul>
  """ + fig(108, 1, "l17-s108-toxocariasis-eye.jpg",
      "A close-up of an eye with an arrow pointing to a pale, raised lesion inside it.",
      "<b>Toxocariasis</b>, the picture beside the slide&rsquo;s title: an arrow on a pale lesion inside the eye "
      "(ocular toxocariasis is migration of larvae to the eye).") + """
  """ + fig(109, 1, "l17-s109-toxocara-cycle.jpg",
      "A numbered life-cycle diagram titled Toxocara spp.: a dog and a cat with adult worms, eggs developing in a box labeled external environment, a puppy and kitten, a duck and a rabbit as paratenic hosts, and a human outline with larvae migrating in its tissues.",
      "<b>The <em>Toxocara</em> life cycle.</b> (1) Eggs passed in feces of dogs (<em>T. canis</em>) and cats "
      "(<em>T. cati</em>); (2) in the external environment the unembryonated egg becomes an embryonated egg with an L3 "
      "larva; (3) ingestion of eggs by a dog or cat; (4) adults in the small intestine of the definitive host; "
      "(5) <b>vertical transmission</b> to puppies and kittens; (6) adults in the small intestine of the offspring; "
      "(7) eggs eaten by a <b>paratenic host</b> (a duck, a rabbit), which carries L3 larvae in its tissue; (8) "
      "ingestion of the paratenic host by a dog. In people: (9) <b>ingestion of eggs</b> and (10) <b>foodborne "
      "transmission</b> from the paratenic host (both infective); (11) L3 larvae migrate in the tissues (diagnostic "
      "stage).", CDC) + """

  <h3 class="sub" id="par-dirofilaria">17.33 &middot; Objective 1 &mdash; <em>Dirofilaria</em> (heartworm)</h3>
  <ul>
    <li><strong>What it is:</strong> a <strong>vector-borne filarial nematode</strong>.</li>
    <li><strong>In dogs:</strong> it causes <strong>heartworm</strong>.</li>
    <li><strong>In humans:</strong> humans are <strong>suboptimal hosts</strong>.
      <ul>
        <li><strong>Pulmonary dirofilariasis:</strong> the worms produce <strong>coin lesions in the lungs</strong> that
        <strong>can be mistaken for malignancies</strong>.</li>
        <li><strong>Subcutaneous dirofilariasis:</strong> the worms produce <strong>nodules</strong>, most often in
        exposed areas of the body.</li>
      </ul></li>
  </ul>
  """ + fig(110, 1, "l17-s110-dirofilaria-section.jpg",
      "A pink-stained tissue section with several round and oval worm cross-sections, each with a pale rim, surrounded by inflamed tissue.",
      "<b><em>Dirofilaria</em></b>, the picture beside the slide&rsquo;s title: several round, worm-like "
      "cross-sections in a stained tissue section.") + """
  """ + fig(110, 2, "l17-s110-heartworm-dog-heart.jpg",
      "An opened animal heart with a tangle of many thin white worms spilling out of it.",
      "<b>Heartworm</b>: a tangle of thin white worms in an opened heart (in dogs, <em>Dirofilaria</em> causes "
      "heartworm).") + """

  <h3 class="sub" id="par-schisto">17.34 &middot; Objective 1 &mdash; Trematodes and <em>Schistosoma</em> (blood flukes)</h3>
  <h4 class="subsub">Trematodes or flukes (slide 111)</h4>
  <p><strong>Flatworms with ovoid, leaflike bodies.</strong> They have <strong>digestive, excretory, neuromuscular,
  and reproductive systems</strong> but <strong>lack circulatory and respiratory systems</strong>. <strong>Animals
  such as snails or fish are usually the intermediate hosts, and humans are the definitive hosts.</strong></p>
  <h4 class="subsub"><em>Schistosoma</em> and schistosomiasis (slides 112&ndash;114)</h4>
  <ul>
    <li><strong>Species and where:</strong> <em>Schistosoma mansoni</em>, <em>S. japonicum</em> and <em>S.
    haematobium</em>, the <strong>blood flukes</strong>. Schistosomiasis is a <strong>prominent parasitic
    disease</strong> of Africa, South America, the Middle East and the Far East: <strong>100 million
    people</strong>.</li>
    <li><strong>Life Cycle D:</strong> adult flukes live in humans, who <strong>release eggs into water</strong>. The
    early larva (<strong>miracidium</strong>) develops in a <strong>freshwater snail</strong> into a second larva
    (<strong>cercaria</strong>).</li>
    <li><strong>How people acquire it:</strong> <strong>the cercaria penetrates human skin</strong> and moves into the
    liver to mature (slide 8: individuals acquire it <strong>by contact with water in which the snail lives</strong>).
    The adults migrate to the <strong>intestine or bladder</strong>, feed on blood, and <strong>shed eggs into urine
    and feces</strong>. Table 23.4 (slide 84) instead says &ldquo;ingestion of fresh water containing larval
    stage&rdquo; (17.42).</li>
    <li><strong>Symptoms:</strong> <strong>itchiness at the entry site</strong>, fever, chills, diarrhea, cough,
    <strong>enlargement and inflammation of the liver, spleen and bladder</strong>.</li>
    <li><strong>Treatment:</strong> <strong>praziquantel</strong>, oxamniquine (Table 23.5: metrifonate, niridazole and
    praziquantel for schistosomiasis).</li>
    <li><strong>Prevention:</strong> <strong>snail control</strong>.</li>
  </ul>
  """ + fig(114, 2, "l17-s114-schistosoma-cycle.jpg",
      "A numbered life-cycle diagram titled Schistosoma spp.: eggs of three species, miracidia, snails, sporocysts, free-swimming cercariae, a human outline with the bowel and bladder marked A, B and C, and a paired male and female worm.",
      "<b>The <em>Schistosoma</em> life cycle.</b> (1) <b>Eggs shed from the infected human in feces or in urine</b> "
      "(diagnostic stage; the eggs drawn are <em>S. mansoni</em> (B), <em>S. japonicum</em> and <em>S. mekongi</em> "
      "(A) and <em>S. haematobium</em> (C)). (2) Eggs hatch and release <b>miracidia</b>; (3) miracidia penetrate snail "
      "tissue; (4) sporocysts develop in the snail (successive generations); (5) <b>free-swimming cercariae are "
      "released from the snail into water</b> (infective stage); (6) <b>cercariae penetrate skin</b>; (7) they lose "
      "their tails during penetration and become schistosomulae; (8) circulation; (9) migration to the portal blood "
      "in the liver and maturation into adults; (10) <b>paired adult worms migrate to the mesenteric venules of the "
      "bowel or rectum</b> (A, B: eggs circulate to the liver and are shed in stools) <b>or the venous plexus of the "
      "bladder</b> (C: eggs shed in urine).", CDC) + """
  """ + fig(114, 1, "l17-s114-schistosoma-stages.jpg",
      "Three micrographs: two pink, oval, ciliated larvae; a forked-tailed larva in a scanning electron micrograph; and a false-colored electron micrograph of a thick worm holding a thinner worm in a groove.",
      "<b>Stages of <em>Schistosoma</em>.</b> (a) The <b>miracidium</b> phase, which infects the snail (300&times;). "
      "(b) The <b>cercaria</b> phase, which is released by snails and <b>burrows into the human host</b> "
      "(5,000&times;). (c) An electron micrograph of the normal mating position of adult worms: the larger male holds "
      "the female in a groove on his ventral surface (2,000&times;).") + """

  <h3 class="sub" id="par-flukes">17.35 &middot; Objective 1 &mdash; Liver and lung flukes: <em>Opisthorchis sinensis</em> and <em>Paragonimus westermani</em></h3>
  <p>Both are <strong>zoonotic, Cycle D</strong> (slide 116).</p>
  <h4 class="subsub">Liver fluke: <em>Opisthorchis</em> (<em>Clonorchis</em>) <em>sinensis</em>, the Chinese liver fluke</h4>
  <ul>
    <li><strong>Hosts:</strong> cycles between <strong>mammals, snails and fish</strong> (Table 23.4: humans, snails,
    fish).</li>
    <li><strong>How people acquire it:</strong> by <strong>eating inadequately cooked fish containing
    cercariae</strong> (Table 23.4: consumption of fish; slide 8: &ldquo;don&rsquo;t eat freshwater sushi&rdquo;).</li>
    <li><strong>In the body:</strong> the larvae <strong>crawl into the bile duct</strong>, mature, and shed eggs into the
    feces; the feces go into water and snails are infected.</li>
    <li><strong>Treatment (slide 116):</strong> triclabendazole, with bithionol as an alternative.</li>
  </ul>
  <h4 class="subsub">Lung fluke: <em>Paragonimus westermani</em>, the Oriental lung fluke</h4>
  <ul>
    <li><strong>Hosts:</strong> cycles between <strong>carnivorous animals, snails, and crustaceans</strong> (Table 23.4:
    humans, mammals, snails, freshwater crabs).</li>
    <li><strong>How people acquire it:</strong> by <strong>eating undercooked crustaceans</strong> (Table 23.4:
    consumption of crabs); the worms <strong>migrate to the lungs</strong>.</li>
    <li><strong>Disease:</strong> <strong>cough, pleural pain, abscess</strong>.</li>
    <li><strong>Treatment:</strong> <strong>praziquantel</strong>.</li>
  </ul>

  <h3 class="sub" id="par-fasciola">17.36 &middot; Objective 1 &mdash; <em>Fasciola hepatica</em></h3>
  <ul>
    <li><strong>Disease:</strong> <strong>fascioliasis</strong>; Table 23.4 calls it the <strong>sheep liver
    fluke</strong>.</li>
    <li><strong>Hosts:</strong> cycles between <strong>herbivores, snails, and aquatic plants</strong> (Table 23.4:
    herbivores, sheep and cattle).</li>
    <li><strong>How people acquire it:</strong> by <strong>eating raw aquatic plants</strong> (Table 23.4: consumption
    of water and water plants).</li>
    <li><strong>In the body:</strong> the <strong>fluke lodges in the liver</strong>.</li>
    <li><strong>Acute phase:</strong> nonspecific symptoms such as abdominal pain, nausea, vomiting. <strong>Chronic
    phase</strong>, months or years later: <strong>inflammation or blockage of the bile duct, gall bladder, or
    pancreas</strong>. The slide names no treatment.</li>
  </ul>
  """ + fig(117, 1, "l17-s117-fasciola-adult.jpg",
      "A stained, leaf-shaped flat worm with labels for the oral sucker at its tip, the ovary, the testis and the digestive gland.",
      "<b>Adult <em>Fasciola hepatica</em></b>: the flat, leaflike fluke body, labeled <b>oral sucker</b>, "
      "<b>ovary</b>, <b>testis</b> and <b>digestive gland</b>.") + """
  """ + fig(117, 2, "l17-s117-fasciola-cycle.jpg",
      "A numbered life-cycle diagram titled Fasciola spp.: eggs in water, miracidia entering a snail, sporocysts, rediae and cercariae, cercariae encysting on a water plant, a cow and a sheep, and a human outline with adult flukes in the bile ducts.",
      "<b>The <em>Fasciola</em> life cycle.</b> (1) Unembryonated eggs are passed in feces (diagnostic stage); (2) eggs "
      "become embryonated in water; (3) miracidia hatch and seek out the snail intermediate host; (4) miracidia "
      "penetrate the snail, where sporocysts, rediae and cercariae develop; (5) <b>free-swimming cercariae encyst on "
      "aquatic vegetation</b>; (6) <b>metacercariae on vegetation are ingested by the definitive host</b> (infective "
      "stage); (7) immature flukes excyst in the duodenum, penetrate the intestinal wall and migrate through the liver "
      "to the biliary ducts; (8) <b>adult flukes in the hepatic biliary ducts</b>. Ruminants are the typical definitive "
      "hosts.", CDC) + """
  <h4 class="subsub">The flukes side by side</h4>
  <table>
    <tr><th>Fluke</th><th>Where the adult lives</th><th>Hosts it cycles through</th><th>How people acquire it</th><th>Disease</th><th>Treatment named on its slide</th></tr>
    <tr><td><em>Schistosoma</em> (blood flukes)</td><td>Blood vessels of the intestine or bladder</td><td>Humans and freshwater snails</td><td>Cercariae penetrate the skin in snail water (Table 23.4: ingestion of fresh water)</td><td>Itchy entry site; liver, spleen, bladder inflammation; eggs in urine and feces</td><td>Praziquantel, oxamniquine</td></tr>
    <tr><td><em>Opisthorchis sinensis</em> (Chinese liver fluke)</td><td>Bile duct</td><td>Mammals, snails, fish</td><td>Inadequately cooked fish</td><td>&mdash;</td><td>Triclabendazole (bithionol alternative)</td></tr>
    <tr><td><em>Paragonimus westermani</em> (lung fluke)</td><td>Lungs</td><td>Carnivorous animals, snails, crustaceans</td><td>Undercooked crustaceans (crabs)</td><td>Cough, pleural pain, abscess</td><td>Praziquantel</td></tr>
    <tr><td><em>Fasciola hepatica</em> (sheep liver fluke)</td><td>Liver</td><td>Herbivores, snails, aquatic plants</td><td>Raw aquatic plants</td><td>Acute nonspecific; chronic bile duct, gall bladder or pancreas blockage</td><td>None named</td></tr>
  </table>

  <h3 class="sub" id="par-tsaginata">17.37 &middot; Objective 1 &mdash; Cestodes and <em>Taenia saginata</em> (beef tapeworm)</h3>
  <h4 class="subsub">Cestode (tapeworm) infestations, slide 118</h4>
  <ul>
    <li><strong>Flatworms, Cycle C.</strong></li>
    <li><strong>Long, very thin, ribbonlike bodies</strong> composed of sacs (<strong>proglottids</strong>) and a
    <strong>scolex that grips the intestine</strong>.</li>
    <li><strong>No mouth</strong>: nutrients are absorbed through the body. <strong>Each proglottid is an independent
    unit</strong> adapted to absorbing food and making and releasing eggs.</li>
    <li><strong>Humans are the definitive host, animals the intermediate host.</strong> The two named:
    <em>Taenia saginata</em> and <em>Taenia solium</em>. (The slide also links a video.)</li>
  </ul>
  <h4 class="subsub"><em>Taenia saginata</em>, slide 119</h4>
  <ul>
    <li><strong>The beef tapeworm, Cycle C and modified A</strong>; it causes <strong>taeniasis</strong>.</li>
    <li><strong>Morphology:</strong> <strong>very large, up to 2,000 proglottids</strong>.</li>
    <li><strong>Hosts:</strong> <strong>humans are the definitive host</strong>. Animals are infected by grazing on land
    contaminated with human feces.</li>
    <li><strong>How people acquire it:</strong> <strong>eating raw beef in which the larval form has encysted</strong>
    (Table 23.4: consumption of undercooked or raw beef). In humans, the larva attaches to the small intestine and
    becomes an adult.</li>
    <li><strong>Disease:</strong> <strong>few symptoms</strong>: vague abdominal pain and nausea; <strong>proglottids in
    the stool</strong>. Slide 8 instead says it &ldquo;causes weight loss and wasting in host&rdquo; (17.42); it also
    says the beef tapeworm absorbs food directly through the cuticle and reproduces via proglottids.</li>
    <li><strong>Treatment:</strong> <strong>praziquantel</strong> (Table 23.5: niclosamide and praziquantel for
    tapeworm).</li>
  </ul>
  """ + fig(120, 1, "l17-s120-tapeworm-in-humans.jpg",
      "Three panels: a magnified tapeworm head with four round suckers and a ring of hooklets; a very long tapeworm coiled in a spiral on a black background beside a ruler; and a cycle diagram from beef muscle to a person, a proglottid, an egg and a grazing cow.",
      "<b>Tapeworm infestation in humans.</b> (a) A tapeworm <b>scolex showing sucker and hooklets</b>. (b) Adult "
      "<em>Taenia saginata</em>: the arrow points to the scolex; the rest of the tape, called the <b>strobila</b>, has a "
      "total length of <b>5 meters</b>. (c) The life cycle of the beef tapeworm <em>T. saginata</em>: the <b>encysted "
      "larva (cysticercus) in beef muscle</b> is ingested; proglottids and eggs leave the person; the egg reaches a "
      "grazing cow.",
      "&copy; Stanley Flegler/Visuals Unlimited; &copy; From Katz et al., Parasitic Diseases, Springer Verlag.") + """

  <h3 class="sub" id="par-tsolium">17.38 &middot; Objective 1 &mdash; <em>Taenia solium</em> (pork tapeworm) and cysticercosis</h3>
  <ul>
    <li><strong>The pork tapeworm.</strong> It causes two diseases, depending on what is swallowed:
      <ul>
        <li><strong>Taeniasis</strong> if a person <strong>ingests contaminated meat</strong> (Table 23.4: undercooked or
        raw pork; slide 8: &ldquo;Taeniasis if ingest undercooked meat&rdquo;). The <strong>cysts release larvae, which
        develop into tapeworms that attach to the intestine and may remain for years</strong>.</li>
        <li><strong>Cysticercosis</strong> if a person <strong>ingests embryonated eggs</strong> (from contaminated food
        or water). The <strong>eggs hatch in the intestine, releasing tapeworm larvae that migrate to all tissues and
        encyst</strong>. Cysticercosis is one of the five neglected parasitic infections on slide 10.</li>
      </ul></li>
    <li><strong>Disease:</strong> the cysts are <strong>most damaging if they lodge in heart muscle, eye, or
    brain</strong>; they <strong>may cause seizures and psychiatric disturbances</strong>. Slide 8: the larvae migrate to
    the musculature or brain, producing lesions.</li>
    <li><strong>Treatment:</strong> <strong>antiparasitic drugs in combination with anti-inflammatory
    drugs</strong>.</li>
  </ul>
  """ + fig(122, 1, "l17-s122-taenia-solium-cycle.jpg",
      "A numbered life-cycle diagram titled Taenia solium: eggs and a gravid proglottid in feces, a pig, cysticerci in pork muscle, a human with an adult tapeworm and scolex in the small intestine, and a boxed section labeled cysticercosis with cysticerci in human tissue.",
      "<b>The <em>Taenia solium</em> life cycle: two diseases.</b> <b>Taeniasis</b>: (1) eggs or gravid proglottids in "
      "feces pass into the environment; (2) embryonated eggs and/or gravid proglottids are ingested by the normal "
      "intermediate host (swine); (3) oncospheres hatch, penetrate the intestinal wall and circulate to the "
      "musculature; (4) they develop into cysticerci; (5) <b>humans acquire intestinal tapeworm infection by eating "
      "cysticerci in meat</b>; (6) adults (with the scolex) in the small intestine. <b>Cysticercosis</b>: (7) "
      "<b>embryonated eggs ingested by the human host</b>; (8) oncospheres hatch, penetrate the intestinal wall and "
      "circulate to the musculature; (9) <b>cysticerci may develop in any organ, most commonly in subcutaneous "
      "tissues, brain, and eyes</b>.", CDC) + """
  """ + fig(123, 2, "l17-s123-cysticercosis-brain-slice.jpg",
      "A slice of brain with several dark, round cystic cavities in the tissue.",
      "<b>Cysticercosis</b>: a slice of brain with several cysts.") + """
  """ + fig(123, 1, "l17-s123-neurocysticercosis-scans.jpg",
      "Two brain scans one above the other on black: the upper labeled healthy brain, the lower labeled brain of a patient with neurocysticercosis, speckled with many small bright spots.",
      "<b>Healthy brain</b> (above) and the <b>brain of a patient with neurocysticercosis</b> (below), speckled with "
      "many small cysts.", "Courtesy of Medscape Reference (printed on the picture).") + """
  """ + fig(123, 3, "l17-s123-cysticercosis-eye.jpg",
      "Three panels: an eye with a raised pink lump on its surface (A), a small red cyst beside a millimeter ruler (B), and a stained section of the cyst (C).",
      "<b>Cysticercosis of the eye</b>: (A) a cyst raised on the eye, (B) the cyst removed, beside a ruler, (C) its "
      "stained section.") + """
  """ + fig(123, 4, "l17-s123-cysticercosis-heart.jpg",
      "A whole heart studded with dozens of small, pale, rounded cysts over its surface.",
      "<b>Cysticercosis of the heart</b>: a heart studded with many small cysts (slide 121: most damaging in heart "
      "muscle, eye, or brain).") + """
  """ + fig(123, 5, "l17-s123-cysticercosis-arm-scan.jpg",
      "A gray scan of an upper arm with several dark, rounded pockets in the muscle and an arrow labeled right triceps abscess.",
      "<b>Cysticercosis in muscle</b>: a scan of the upper arm with an arrow on the cystic pockets, labeled "
      "&ldquo;right triceps abscess&rdquo;.") + """

  <h3 class="sub" id="par-echino">17.39 &middot; Objective 1 &mdash; <em>Echinococcus</em> and echinococcosis</h3>
  <p>Echinococcosis is a parasitic disease caused by infection with <strong>tiny tapeworms of the genus
  <em>Echinococcus</em></strong>. Two forms:</p>
  <table>
    <tr><th></th><th>Cystic echinococcosis (hydatid disease)</th><th>Alveolar echinococcosis</th></tr>
    <tr><td><strong>The worm</strong></td><td>A <strong>2&ndash;7&nbsp;mm</strong> long tapeworm</td><td>The <strong>larval
    state</strong> of a <strong>1&ndash;4&nbsp;mm</strong> long tapeworm</td></tr>
    <tr><td><strong>Definitive hosts</strong></td><td><strong>Dogs</strong></td><td><strong>Foxes, coyotes, and dogs</strong></td></tr>
    <tr><td><strong>Intermediate hosts</strong></td><td>Sheep, cattle, goats, pigs</td><td>&mdash;</td></tr>
    <tr><td><strong>Disease</strong></td><td><strong>Slowly enlarging cysts in the liver and lungs</strong></td><td><strong>Parasitic
    tumors in the lungs, liver, brain</strong>; human cases rare; <strong>untreated can be fatal</strong></td></tr>
  </table>
  <ul>
    <li><strong>How people acquire it:</strong> typically from <strong>handling dogs that have the infection</strong>
    (slide 8: &ldquo;Acquired from dogs&rdquo;). It is <strong>most prevalent where dogs interact with intermediate
    hosts</strong>.</li>
    <li><strong>Immunity:</strong> it has been <strong>shown to reduce the activity of natural killer cells</strong>.</li>
    <li><strong>Treatment:</strong> often <strong>surgical removal of the parasitic masses</strong>, but chemotherapy is
    also used (slide 8: hydatid cysts &ldquo;may need to be surgically removed&rdquo;).</li>
  </ul>
  """ + fig(124, 1, "l17-s124-echinococcus-adult.jpg",
      "A stained, pink, tiny tapeworm with a rounded head and a few segments on a yellow background, and beside it a close view of a head with suckers and a crown of hooks.",
      "<b><em>Echinococcus</em></b>: a tiny tapeworm of only a few segments, and its scolex.") + """
  """ + fig(125, 1, "l17-s125-hydatid-cyst-surgery.jpg",
      "An opened abdomen at surgery with a large, smooth, white cystic mass bulging from the tissue next to dark red liver.",
      "<b>A parasitic mass at surgery</b>: a large white cyst exposed in the abdomen (treatment often involves "
      "surgical removal of parasitic masses).") + """
  <p><strong>One more tapeworm (slides 126&ndash;127):</strong> a 2015 <em>New England Journal of Medicine</em> report,
  &ldquo;Malignant Transformation of <em>Hymenolepis nana</em> in a Human Host&rdquo;, described tapeworm cells
  behaving like cancer in a man infected with the human immunodeficiency virus. <em>Hymenolepis nana</em> is the dwarf
  tapeworm of Table 23.4 (oral-fecal; close contact).</p>
  <h4 class="subsub">The tapeworms side by side</h4>
  <table>
    <tr><th>Tapeworm</th><th>Definitive host</th><th>Intermediate host</th><th>How people acquire it</th><th>Disease</th><th>Treatment named on its slide</th></tr>
    <tr><td><em>Taenia saginata</em> (beef)</td><td>Humans</td><td>Cattle</td><td>Raw or undercooked beef with encysted larvae</td><td>Taeniasis: few symptoms, proglottids in stool</td><td>Praziquantel</td></tr>
    <tr><td><em>Taenia solium</em> (pork)</td><td>Humans</td><td>Swine (and humans who swallow eggs)</td><td>Cysts in pork: taeniasis. Embryonated eggs in food or water: cysticercosis</td><td>Cysts in heart, eye, brain: seizures, psychiatric disturbances</td><td>Antiparasitic plus anti-inflammatory drugs</td></tr>
    <tr><td><em>Echinococcus</em></td><td>Dogs (alveolar: foxes, coyotes, dogs)</td><td>Sheep, cattle, goats, pigs</td><td>Handling infected dogs</td><td>Hydatid cysts in liver and lungs; alveolar parasitic tumors</td><td>Surgical removal; chemotherapy</td></tr>
  </table>

  <h3 class="sub" id="par-arthropods">17.40 &middot; Objective 1 &mdash; The arthropod vectors</h3>
  <p><strong>Arthropods</strong> have an <strong>exoskeleton and jointed legs</strong>; the group includes arachnids
  and crustaceans. Many must <strong>feed on the blood and tissue fluid of a host</strong> during the life cycle:
  they are <strong>ectoparasites</strong>. Those of medical importance <strong>transmit infectious microbes in the
  process of feeding</strong>: they are <strong>biological vectors</strong>.</p>
  <table>
    <tr><th>Arthropod (slide 130)</th><th>Traits</th><th>Diseases the slide names</th></tr>
    <tr><td colspan="3"><strong>Insects</strong></td></tr>
    <tr><td><strong>Mosquitoes</strong></td><td>Require an <strong>aquatic habitat</strong>; <strong>females take the blood
    meal</strong></td><td>Malaria, filariasis, dengue fever</td></tr>
    <tr><td><strong>Fleas</strong></td><td>Highly motile, flattened bodies; feed on warm-blooded animals; carry
    <strong>zoonotic</strong> diseases</td><td>Plague, murine typhus</td></tr>
    <tr><td><strong>Lice</strong></td><td>Small, soft; attach to head and body hair, feeding inconspicuously on blood and
    tissue fluid; <strong>release feces that contaminate the wound</strong></td><td>Epidemic typhus, relapsing fever</td></tr>
    <tr><td colspan="3"><strong>Arachnids</strong></td></tr>
    <tr><td><strong>Ticks</strong></td><td>Cling on vegetation and attach to the host on contact; larvae, nymph and
    adults get a blood meal by piercing the host&rsquo;s skin</td><td>&mdash;</td></tr>
    <tr><td><strong>Hard (ixodid) ticks</strong></td><td>Small, compact, rigid bodies</td><td>Bacterial, rickettsial and viral diseases</td></tr>
    <tr><td><strong>Soft (argasid) ticks</strong></td><td>Flexible outer bodies</td><td>Relapsing fever</td></tr>
  </table>
  <h4 class="subsub">Table 23.6: Common arthropods that are biological vectors of disease (slide 129)</h4>
  <table>
    <tr><th>Insect vectors</th><th>Diseases transmitted</th><th>Type of microbe</th><th>Distribution/Location of vector/disease</th></tr>
    <tr><td colspan="4"><strong>Mosquitoes</strong></td></tr>
    <tr><td><em>Anopheles</em></td><td>Malaria</td><td>Apicomplexa protozoan</td><td>In a band around the equator</td></tr>
    <tr><td><em>Anopheles</em>/<em>Culex</em></td><td>Filariasis</td><td>Nematode</td><td>Worldwide in tropics</td></tr>
    <tr><td><em>Culex</em></td><td>Dengue Fever</td><td>Arbovirus</td><td>Asia, Africa, Europe, Americas</td></tr>
    <tr><td><em>Culex</em></td><td>West Nile Fever</td><td>Arbovirus</td><td>Africa, Middle east, Americas</td></tr>
    <tr><td><em>Aedes</em></td><td>Yellow Fever</td><td>Arbovirus</td><td>Tropics; subtropics</td></tr>
    <tr><td>Various</td><td>Encephalitides</td><td>Arboviruses</td><td>Worldwide</td></tr>
    <tr><td colspan="4"><strong>Fleas</strong></td></tr>
    <tr><td><em>Xenopsylla</em></td><td>Bubonic plague</td><td>Gram-negative bacteria</td><td>Worldwide</td></tr>
    <tr><td><em>Ctenocephalides</em></td><td>Murine typhus</td><td>Rickettsia</td><td>Worldwide</td></tr>
    <tr><td><strong>Body lice</strong></td><td>Epidemic typhus</td><td>Rickettsia</td><td>Worldwide</td></tr>
    <tr><td><em>Pediculus</em></td><td>Trench fever</td><td>Bartonella bacteria</td><td>Asia, Africa, Europe</td></tr>
    <tr><td></td><td>Relapsing fever</td><td>Borrelia spirochetes</td><td>Asia, Africa</td></tr>
    <tr><td colspan="4"><strong>Biting flies</strong></td></tr>
    <tr><td>Tsetse</td><td>African trypanosomiasis</td><td>Flagellated protozoan</td><td>Central Africa</td></tr>
    <tr><td>Sand fly</td><td>Leishmaniasis</td><td>Flagellated protozoan</td><td>Africa, India, Latin America</td></tr>
    <tr><td>Black fly</td><td>Onchocerciasis</td><td>Nematode</td><td>Africa, Latin America</td></tr>
    <tr><td colspan="4"><strong>Biting Bugs</strong></td></tr>
    <tr><td><em>Triatoma</em></td><td>Chagas disease</td><td>Flagellated protozoan</td><td>Central and South America</td></tr>
    <tr><th>Arachnid vectors</th><th>Diseases transmitted</th><th>Type of microbe</th><th>Distribution; Description of disease</th></tr>
    <tr><td colspan="4"><strong>Hard ticks</strong></td></tr>
    <tr><td rowspan="7"><em>Dermacentor</em>, <em>Ixodes</em>, <em>Amblyomma</em> (several ticks can be vectors of the
    same disease)</td><td>Rocky Mountain spotted fever</td><td>Rickettsia</td><td>North, Central, and South America</td></tr>
    <tr><td>Q fever</td><td>Rickettsia</td><td>Europe, Africa, Asia, N.&nbsp;America</td></tr>
    <tr><td>Human erhlichosis</td><td>Rickettsia</td><td>North America</td></tr>
    <tr><td>Lyme disease</td><td>Borrelia spirochetes</td><td>Worldwide</td></tr>
    <tr><td>Tularemia</td><td>Gram-negative bacteria</td><td>United States</td></tr>
    <tr><td>Babesiosis</td><td>Apicomplex protozoan</td><td>Eastern/Midwestern United States</td></tr>
    <tr><td>Various arboviruses</td><td></td><td>Europe, Africa, Asia</td></tr>
    <tr><td colspan="4"><strong>Soft ticks</strong></td></tr>
    <tr><td><em>Ornithodoros</em></td><td>Relapsing fever</td><td>Borrelia spirochete</td><td>Africa, Asia, Europe, Americas</td></tr>
  </table>
  <p>Each distribution on the slide carries a small symbol whose key is not on the slide; the symbols are left out
  here. Most vectors of this lecture&rsquo;s parasites are in it: <em>Anopheles</em> (malaria), <em>Anopheles</em>
  and <em>Culex</em> (filariasis), the tsetse fly (African trypanosomiasis), the sand fly (leishmaniasis), the black
  fly (onchocerciasis), <em>Triatoma</em> (Chagas disease) and the hard ticks (babesiosis). The mangrove and deer
  flies that carry <em>Loa loa</em> (Table 23.4) are not.</p>
  """ + fig(129, 1, "l17-s129-table-23-6.jpg",
      "A textbook table titled Table 23.6, Common Arthropods That Are Biological Vectors of Disease, listing insect vectors and arachnid vectors with diseases, microbe types and distributions.",
      "<b>Table 23.6</b> as it appears on the slide (transcribed above).") + """
  """ + fig(131, 1, "l17-s131-arthropod-vectors.jpg",
      "Five close-up photographs: a mosquito feeding on skin, its abdomen full of blood; a flea; two lice; a dark, flat hard tick on skin; and a rounded, leathery soft tick.",
      "<b>Arthropod vectors.</b> (a) Mosquito, (b) flea, (c) lice, (d) hard tick, (e) soft tick.",
      crop=(0, 0, 916, 466)) + """

  <h3 class="sub" id="par-transmission">17.41 &middot; Objective 2 &mdash; How humans acquire every parasite in this lecture</h3>
  <p>Every organism of the lecture, protozoa and helminths, grouped by route. Each cell is from the slides (slide
  numbers in brackets); an organism appears under every route its slides give. Where the slides disagree, the cell
  says so.</p>
  <table>
    <tr><th>Route</th><th>Protozoa</th><th>Helminths</th></tr>
    <tr><td><strong>Swallowing cysts, oocysts or eggs</strong> in fecally contaminated food or water, or picked up
    from the surroundings (fecal-oral)</td>
    <td><em>Entamoeba histolytica</em>: fecal-oral route; cysts swallowed; source human, water and food; epidemics
    where water supplies are polluted (prisons, hospitals, juvenile care institutions) [4, 13, 16&ndash;19].
    <em>Balantidium coli</em>: cyst-containing food or water; zoonotic in pigs, with pigs and cattle as alternate hosts
    [4, 13, 33]. <em>Giardia lamblia</em>: cysts usually ingested with water and food; reservoirs beavers, cattle,
    coyotes, cats and humans; common in campers [4, 13, 39]. <em>Cryptosporidium</em>: oocysts in water in
    recreational settings, contaminated water, ice, foodstuffs; tolerates chlorine in pools [6, 13, 72&ndash;73].
    <em>Trypanosoma cruzi</em>: foodstuffs contaminated by triatomine urine or feces, which typically gives more
    severe cases and higher mortality [49]. <em>Isospora belli</em>: fecally contaminated food or drink [74] (slide 13 gives its source as &ldquo;Dogs, other
    mammals&rdquo;). <em>Cyclospora cayetanensis</em>: oral-fecal, fresh produce and water; the 2026 iceberg lettuce
    outbreak [13, 75&ndash;76].</td>
    <td><em>Ascaris lumbricoides</em>: eggs in food, drink, contaminated objects (Cycle A) [91]. <em>Trichuris
    trichiura</em>: eggs (Cycle A) [93]. Table 23.4: fecal pollution of soil with eggs for both [84].
    <em>Enterobius vermicularis</em>: eggs picked up from surroundings and swallowed; close contact and fomites;
    self-inoculation [6, 84, 94]. <em>Taenia solium</em> (cysticercosis): embryonated eggs in contaminated food or water
    [121]. <em>Hymenolepis nana</em>: oral-fecal; close contact [84].</td></tr>
    <tr><td><strong>Eating larvae or cysts</strong> in undercooked meat, fish, crustaceans or snails, or on raw water
    plants and vegetables</td>
    <td><em>Toxoplasma gondii</em>: raw meats [64]. <em>Sarcocystis</em>: undercooked meat of cattle (<em>S.
    hominis</em>) or pigs (<em>S. suihominis</em>) [71].</td>
    <td><em>Trichinella spiralis</em>: undercooked pork or bear meat (Cycle C) [7, 84, 101]. <em>Taenia
    saginata</em>: raw or undercooked beef [84, 119]. <em>Taenia solium</em> (taeniasis): contaminated, undercooked
    or raw pork [8, 84, 121]. <em>Diphyllobothrium latum</em>: undercooked or raw fish [84].
    <em>Opisthorchis sinensis</em>: inadequately cooked fish [8, 84, 116]. <em>Paragonimus westermani</em>: undercooked
    crustaceans, crabs [84, 116]. <em>Fasciola hepatica</em>: raw aquatic plants [117] (Table 23.4: water and water
    plants). <em>Angiostrongylus cantonensis</em>: snails, water or vegetables [7, 99]. <em>Toxocara</em>:
    undercooked meat of a paratenic host (waterfowl) [8, 108].</td></tr>
    <tr><td><strong>Larvae penetrating the skin</strong></td>
    <td>&mdash;</td>
    <td>Hookworms (<em>Necator americanus</em>, <em>Ancylostoma duodenale</em>): filariform larvae through the skin of
    bare feet (Cycle B) [6, 96&ndash;97]. <em>Strongyloides stercoralis</em>: larvae penetrate the skin (Cycle B) and can
    reinfect the same host [100]. Table 23.4 gives &ldquo;fecal pollution of soil with eggs&rdquo; for these [84].
    <em>Schistosoma</em>: <strong>cercariae penetrate the skin</strong> in water where the snail lives [8,
    112&ndash;114]. <strong>The slides disagree:</strong> Table 23.4 says &ldquo;ingestion of fresh water containing
    larval stage&rdquo; [84].</td></tr>
    <tr><td><strong>Insect or tick vectors</strong></td>
    <td><em>Plasmodium</em>: female <em>Anopheles</em> mosquito [5, 56, 129]. <em>Trypanosoma brucei</em>: tsetse fly
    bite [5, 45&ndash;46]. <em>Trypanosoma cruzi</em>: reduviid (kissing) bug, its feces inoculated into a cutaneous
    portal [5, 49]. <em>Leishmania</em>: female sand flies (dogs alternate hosts) [5, 52]. <em>Babesia
    microti</em>: the blacklegged deer tick [77; Table 23.6, 129]. <em>Toxoplasma</em>: slide 13 lists &ldquo;Zoonotic/vector-borne&rdquo;,
    while slides 64&ndash;65 name only cats, raw meat and the placenta.</td>
    <td><em>Wuchereria bancrofti</em>: mosquitoes [8, 84, 104]. <em>Onchocerca volvulus</em>: black flies [8, 84, 106].
    <em>Loa loa</em>: small flies (mangrove or deer flies) [8, 84, 107]. <em>Dirofilaria</em>: &ldquo;vector-borne&rdquo;,
    vector not named [110].</td></tr>
    <tr><td><strong>Nasal contact with water</strong>, or a break in the skin</td>
    <td><em>Naegleria fowleri</em>: nasal contact with water: diving, waterskiing, jetskiing, an indoor surfing
    facility, rinsing sinuses even with tap water, neti pots [24&ndash;28]. <em>Acanthamoeba</em>: through a break in
    the skin or the nasal passages (granulomatous amebic encephalitis); keratitis in contact lens wearers; freshwater
    lakes, hot tubs, swimming pools [4, 31].</td>
    <td>&mdash;</td></tr>
    <tr><td><strong>Sexual contact</strong></td>
    <td><em>Trichomonas vaginalis</em>: a sexually transmitted disease; reservoir the human urogenital tract; cannot
    survive long outside the host [4, 13, 37]. <em>Entamoeba histolytica</em>: sometimes sexually transmitted
    [17].</td>
    <td>&mdash;</td></tr>
    <tr><td><strong>Mother to fetus, transfusion, transplant</strong></td>
    <td><em>Toxoplasma gondii</em>: transplacental, 33% chance [5, 65]. <em>Trypanosoma cruzi</em>: congenitally (up to
    108 congenital infections a year in the United States), transfusions, organ transplants [48&ndash;49].
    <em>Plasmodium</em>: blood transfusions, mother to fetus [56].</td>
    <td>&mdash;</td></tr>
    <tr><td><strong>Dogs and cats</strong></td>
    <td><em>Toxoplasma gondii</em>: oocysts in cat feces; substances contaminated by cat feces; pregnant women should
    not clean the catbox [5, 64].</td>
    <td><em>Toxocara canis</em> and <em>Toxocara cati</em>: infective eggs from dog and cat feces [8, 108&ndash;109].
    <em>Echinococcus</em>: handling infected dogs [8, 125].</td></tr>
  </table>
"""

TEST = [
    '{q:"In a helminth life cycle, where do adulthood and mating occur?", choices:["The intermediate host","The definitive host","The transport host","The vector"],correct:1, explain:"Adulthood and mating occur in the definitive host. Larval development is in the intermediate host; a transport (paratenic) host has no parasitic development."}',
    '{q:"How do hookworm larvae enter the human body?", choices:["In undercooked pork","In swallowed eggs on vegetables","By burrowing through the skin of bare feet","Through a mosquito bite"],correct:2, explain:"Life Cycle B: eggs shed in feces hatch into filariform larvae that burrow into the skin of bare feet, pass through the lungs, are swallowed and mature in the small intestine. Blood loss causes anemia."}',
    '{q:"A child in daycare has anal itching at night. Which test finds the cause?", choices:["Tape test","Lumbar puncture","Blood smear","Muscle biopsy"],correct:0, explain:"Pinworm (Enterobius vermicularis): mature females emerge from the intestine to lay eggs, causing anal itching; the tape test picks up the eggs. Treatment is pyrantel pamoate."}',
    '{q:"After eating raw snails, a patient has a stiff neck and a lumbar puncture full of eosinophils instead of neutrophils. Which parasite?", choices:["Naegleria fowleri","Angiostrongylus cantonensis","Trichinella spiralis","Toxocara canis"],correct:1, explain:"The rat lungworm causes eosinophilic meningitis; snails are its intermediate hosts and people swallow it in snails, water or vegetables. Prevention is snail and slug control and washing produce."}',
    '{q:"Swallowing which stage of Taenia solium causes cysticercosis?", choices:["Encysted larvae in pork","Adult proglottids","Embryonated eggs","Cercariae in water"],correct:2, explain:"Embryonated eggs hatch in the intestine and the larvae migrate to all tissues and encyst, most damaging in heart muscle, eye or brain (seizures). Eating cysts in pork causes taeniasis instead."}',
    '{q:"Which worm, spread by black flies, causes river blindness through its Wolbachia bacteria?", choices:["Loa loa","Wuchereria bancrofti","Dirofilaria","Onchocerca volvulus"],correct:3, explain:"Onchocerca volvulus: Wolbachia antigens stimulate inflammation that damages the cornea, retina and optic nerve. Treatment is tetracycline and ivermectin. Loa loa is the eye worm spread by small flies; Wuchereria (mosquitoes) causes elephantiasis."}',
]

NOTES = [
    '<li><strong>How <em>Schistosoma</em> gets in.</strong> Table 23.4 (slide 84) gives all three species as spread by '
    '&ldquo;Ingestion of fresh water containing larval stage&rdquo;. Slide 8 says &ldquo;Individuals acquire by contact with '
    'water in which the snail lives&rdquo;, slide 112 &ldquo;This larva penetrates human skin&rdquo;, slide 113 lists '
    '&ldquo;Itchiness at entry site&rdquo;, and slide 114&rsquo;s cycle says &ldquo;Cercariae penetrate skin&rdquo;. The guide '
    'teaches skin penetration (four slides and the diagram; current practice agrees: cercariae penetrate the skin '
    'during contact with fresh water). Know that the table says ingestion.</li>',
    '<li><strong><em>Taenia saginata</em> symptoms.</strong> Slide 8 says the beef tapeworm &ldquo;Causes weight loss and '
    'wasting in host&rdquo;; slide 119 says it &ldquo;Causes few symptoms; vague abdominal pain and nausea; proglottids in '
    'stool&rdquo;. The guide teaches slide 119, the organism&rsquo;s own slide.</li>',
    '<li><strong>Treating <em>Opisthorchis</em>.</strong> Slide 116 gives &ldquo;triclabendazole with bithionol as an '
    'alternative&rdquo; for the Chinese liver fluke; Table 23.5 (slide 87) lists neither drug and gives praziquantel for '
    '&ldquo;Schistosomiasis, other flukes, tapeworm&rdquo;, and slide 116 itself gives praziquantel for <em>Paragonimus</em>. '
    'In current practice praziquantel is the drug for <em>Opisthorchis</em>/<em>Clonorchis</em>, and triclabendazole is '
    'the drug for <em>Fasciola</em> (slide 117 names no treatment for <em>Fasciola</em>). Keyed as slide 116 says.</li>',
    '<li><strong>What is in the fish.</strong> Slide 116 says people eat fish &ldquo;containing cercariae&rdquo;. In slide '
    '117&rsquo;s <em>Fasciola</em> cycle the cercariae encyst and the stage eaten is the &ldquo;metacercariae&rdquo;; current '
    'references likewise call the stage in the fish a metacercaria (an encysted cercaria). Not asked.</li>',
    '<li><strong><em>Trichinella</em> and Cycle C.</strong> Slide 101 assigns <em>Trichinella</em> to Life Cycle C but also '
    'says its &ldquo;Life cycle [is] entirely within mammalian host&rdquo;. Slide 82&rsquo;s Cycle C has eggs released in '
    'feces and a food animal grazing on contaminated grass, while slide 102&rsquo;s trichinellosis cycle has no eggs: adults '
    'form new larvae that burrow into the circulation and encyst in muscle. For <em>Trichinella</em>, learn slides '
    '101&ndash;102; the shared point with Cycle C is the encysted larva in undercooked meat.</li>',
    '<li><strong>How the soil worms get in.</strong> Table 23.4 gives &ldquo;Fecal pollution of soil with eggs&rdquo; for the '
    'hookworms and <em>Strongyloides</em>, under its own heading &ldquo;Infective in larval stage&rdquo;; slides 96 and 100 '
    'say the larvae penetrate the skin. Both hold: feces put the eggs in the soil, and the larva that hatches is the '
    'infective stage. Slide 96 has the eggs hatch &ldquo;into filariform larvae&rdquo;; slide 97&rsquo;s cycle has a '
    'rhabditiform larva hatch first and become the filariform larva that penetrates the skin.</li>',
    '<li><strong>Who is the definitive host of a tapeworm.</strong> Slide 118 says of cestodes &ldquo;Humans definitive '
    'host, animals intermediate&rdquo;. That holds for <em>Taenia</em> taeniasis, but slide 124 makes <strong>dogs</strong> '
    '(and foxes and coyotes) the definitive hosts of <em>Echinococcus</em>, with people carrying the cysts, and in '
    'cysticercosis (slides 121&ndash;122) the person carries the larval cysts of <em>Taenia solium</em>.</li>',
    '<li><strong>Slide 116&rsquo;s <em>Paragonimus</em> line is garbled:</strong> &ldquo;humans worms migrate to lungs '
    'infected by eating undercooked crustaceans; intestinal&rdquo;. Read it as: humans are infected by eating undercooked '
    'crustaceans, and the worms migrate to the lungs. The trailing &ldquo;intestinal&rdquo; is not explained.</li>',
    '<li><strong>&ldquo;Mectizan&rdquo; (slide 104).</strong> The slide treats bancroftian filariasis with &ldquo;Albendazole, '
    'mectizan (only for filarial stage)&rdquo;. Mectizan is a brand name of ivermectin (not stated in the deck); Table 23.5 '
    'lists ivermectin for onchocerciasis, ascariasis and strongyloidiasis, and diethylcarbamazine (kills microfilariae, '
    'not the adult worm) for filariasis. Not asked.</li>',
    '<li><strong>Drug lists that read oddly.</strong> Slide 92&rsquo;s &ldquo;albendazole with mebendazole, ivermectin, and '
    'nitazoxanide&mdash;1-3 days&rdquo; for <em>Ascaris</em> reads as a list of options rather than a four-drug '
    'combination (current practice uses one drug, usually albendazole or mebendazole). Slide 113 gives praziquantel and '
    'oxamniquine for schistosomiasis while Table 23.5 gives metrifonate, niridazole and praziquantel; praziquantel is the '
    'drug both name, and the one used today.</li>',
    '<li><strong><em>Isospora</em>&rsquo;s source.</strong> Slide 13&rsquo;s table gives <em>Isospora belli</em> '
    '&ldquo;Dogs, other mammals&rdquo;; slide 74 says &ldquo;Transmitted in fecally contaminated food or drink&rdquo;. The '
    '17.41 table gives both.</li>',
    '<li><strong>Spellings and names.</strong> Organism names are written correctly here: slide 88&rsquo;s &ldquo;Trichuris '
    'trichuria&rdquo; (<em>Trichuris trichiura</em>), slide 98&rsquo;s &ldquo;Angiostronglylus&rdquo;, slide 104&rsquo;s '
    '&ldquo;Wuchereia&rdquo; and slides 3 and 8&rsquo;s &ldquo;Wucherica bancroft&rdquo; (<em>Wuchereria bancrofti</em>), slide '
    '107&rsquo;s &ldquo;Loa Loa&rdquo;, slide 124&rsquo;s &ldquo;Echinococcocus&rdquo;, slides 3 and 8&rsquo;s '
    '&ldquo;Shistosoma&rdquo; and &ldquo;Paragoniumus&rdquo;. Table 23.6 is transcribed as printed, including &ldquo;Human '
    'erhlichosis&rdquo; (ehrlichiosis) and &ldquo;Apicomplex protozoan&rdquo;. Table 23.5&rsquo;s &ldquo;trichinosis&rdquo; and '
    'slide 101&rsquo;s &ldquo;trichinellosis&rdquo; are the same disease.</li>',
]
