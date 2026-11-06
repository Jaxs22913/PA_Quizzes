# -*- coding: utf-8 -*-
"""Lecture 17 guide fragment (protozoa): 17.1-17.19, slides 1-77 of
"Lecture 16 Dr. Webster Parasites of Medical Importance.pptx".

Exports TOC, BODY, TEST, NOTES for _micro_e3_guide_l17.py. Content is from the visible slides only (the deck has no
speaker notes); every slide 1-77 was viewed as a 1920-pixel render and every picture at full size.

Pictures left out: slide 1 (a title collage of unlabeled parasite photographs: decoration), slide 69 (cat-lady
cartoons). Slide 30's picture is cropped to its Medication and Route columns so that no dose is reproduced. Slide
24's Florida page is cropped where the slide crops it (the map only). Credits: MH only where the McGraw-Hill line
is printed on the picture (slides 34, 40); CDC on the DPDx life cycle (slide 32); printed credits as printed.
"""
from _micro_e3_guide_l17_figs import fig, MH, CDC  # noqa: F401

TOC = """
  <a class="sub-link" href="#par-overview">17.1 Objective 1 &mdash; Parasitology and the organisms at a glance</a>
  <a class="sub-link" href="#par-protozoa">17.2 Objective 1 &mdash; Protozoa: groups, life cycles and drugs</a>
  <a class="sub-link" href="#par-entamoeba">17.3 Objective 1 &mdash; <em>Entamoeba histolytica</em> and amebiasis</a>
  <a class="sub-link" href="#par-naegleria">17.4 Objective 1 &mdash; <em>Naegleria fowleri</em> and amebic meningoencephalitis</a>
  <a class="sub-link" href="#par-acanth">17.5 Objective 1 &mdash; <em>Acanthamoeba</em>: keratitis and granulomatous amebic encephalitis</a>
  <a class="sub-link" href="#par-balantidium">17.6 Objective 1 &mdash; <em>Balantidium coli</em>, the intestinal ciliate</a>
  <a class="sub-link" href="#par-trichomonas">17.7 Objective 1 &mdash; <em>Trichomonas vaginalis</em> and trichomoniasis</a>
  <a class="sub-link" href="#par-giardia">17.8 Objective 1 &mdash; <em>Giardia lamblia</em> and giardiasis</a>
  <a class="sub-link" href="#par-hemoflag">17.9 Objective 1 &mdash; The hemoflagellates and their stages</a>
  <a class="sub-link" href="#par-tbrucei">17.10 Objective 1 &mdash; <em>Trypanosoma brucei</em> and African sleeping sickness</a>
  <a class="sub-link" href="#par-tcruzi">17.11 Objective 1 &mdash; <em>Trypanosoma cruzi</em> and Chagas disease</a>
  <a class="sub-link" href="#par-leish">17.12 Objective 1 &mdash; <em>Leishmania</em> and leishmaniasis</a>
  <a class="sub-link" href="#par-plasmodium">17.13 Objective 1 &mdash; <em>Plasmodium</em> and malaria</a>
  <a class="sub-link" href="#par-toxo">17.14 Objective 1 &mdash; <em>Toxoplasma gondii</em> and toxoplasmosis</a>
  <a class="sub-link" href="#par-sarco">17.15 Objective 1 &mdash; <em>Sarcocystis</em> and sarcocystosis</a>
  <a class="sub-link" href="#par-crypto">17.16 Objective 1 &mdash; <em>Cryptosporidium</em></a>
  <a class="sub-link" href="#par-isospora">17.17 Objective 1 &mdash; <em>Isospora belli</em> and coccidiosis</a>
  <a class="sub-link" href="#par-cyclospora">17.18 Objective 1 &mdash; <em>Cyclospora cayetanensis</em> and cyclosporiasis</a>
  <a class="sub-link" href="#par-babesia">17.19 Objective 1 &mdash; <em>Babesia</em> and babesiosis</a>"""

BODY = """
  <h3 class="sub" id="par-overview">17.1 &middot; Objective 1 &mdash; Parasitology and the organisms at a glance</h3>
  <p><strong>Parasitology</strong> is the study of <strong>eukaryotic parasites, protozoa and helminths</strong>.
  Parasites <strong>cause 20% of all infectious diseases</strong>. They are <strong>less prevalent in industrialized
  countries</strong>, and <strong>increasingly common in patients with human immunodeficiency virus infection and other
  immunocompromised patients</strong> (slide 9).</p>
  <h4 class="subsub">The neglected parasitic infections (slide 10)</h4>
  <p>The Centers for Disease Control and Prevention set <strong>priorities for public health action</strong> based on
  the <strong>number of people infected</strong>, the <strong>severity of illness</strong> and the <strong>ability to
  prevent and treat</strong>. Its list of neglected parasitic infections names <strong>five parasitic
  diseases</strong>:</p>
  <table>
    <tr><th>Neglected parasitic infection</th><th>Organism (from her table, slides 4&ndash;8)</th><th>Where in this guide</th></tr>
    <tr><td><strong>Chagas disease</strong></td><td><em>Trypanosoma cruzi</em></td><td>17.11</td></tr>
    <tr><td><strong>Cysticercosis</strong></td><td><em>Taenia solium</em> (pork tapeworm)</td><td>The tapeworms, later in this section</td></tr>
    <tr><td><strong>Toxocariasis</strong></td><td><em>Toxocara canis</em> and <em>Toxocara cati</em> (dog and cat roundworm)</td><td>The tissue nematodes, later in this section</td></tr>
    <tr><td><strong>Toxoplasmosis</strong></td><td><em>Toxoplasma gondii</em></td><td>17.14</td></tr>
    <tr><td><strong>Trichomoniasis</strong></td><td><em>Trichomonas vaginalis</em></td><td>17.7</td></tr>
  </table>

  <h4 class="subsub">The organism list (slide 3)</h4>
  <p>Slide 3 reproduces the syllabus&rsquo;s Appendix 2 list of <strong>33 organisms</strong> for this lecture
  (spellings corrected here; the slide&rsquo;s spellings are in 17.42). The deck also teaches two coccidians that are
  not on the list, <em>Sarcocystis</em> (17.15) and <em>Babesia</em> (17.19).</p>
  <table>
    <tr><th>Protozoa (14)</th><th>Helminths (19)</th></tr>
    <tr><td><em>Entamoeba histolytica</em><br><em>Naegleria fowleri</em><br><em>Acanthamoeba</em><br>
    <em>Balantidium coli</em><br><em>Giardia lamblia</em><br><em>Trichomonas vaginalis</em><br>
    <em>Trypanosoma brucei</em><br><em>Trypanosoma cruzi</em><br><em>Leishmania</em> sp.<br>
    <em>Plasmodium</em> sp.<br><em>Toxoplasma gondii</em><br><em>Cryptosporidium</em> sp.<br>
    <em>Isospora belli</em><br><em>Cyclospora cayetanensis</em></td>
    <td><em>Trichuris trichiura</em><br><em>Ascaris lumbricoides</em><br><em>Enterobius vermicularis</em><br>
    <em>Necator americanus</em><br><em>Angiostrongylus cantonensis</em><br><em>Strongyloides stercoralis</em><br>
    <em>Trichinella spiralis</em><br><em>Wuchereria bancrofti</em><br><em>Onchocerca volvulus</em><br>
    <em>Loa loa</em><br><em>Schistosoma</em> sp.<br><em>Toxocara canis</em><br><em>Toxocara cati</em><br>
    <em>Opisthorchis sinensis</em><br><em>Fasciola hepatica</em><br><em>Paragonimus westermani</em><br>
    <em>Taenia saginata</em><br><em>Taenia solium</em><br><em>Echinococcus</em></td></tr>
  </table>

  <h4 class="subsub">Her summary table: organism, disease, other information (slides 4&ndash;8)</h4>
  <p>Slides 4&ndash;8 are pictures of one table she built, with the columns <strong>Organism</strong>,
  <strong>Disease</strong>, <strong>Other information</strong> and <strong>Photo</strong>. It is transcribed below
  cell by cell, one table per slide, with the slide picture above each. Organism names are spelled correctly and
  abbreviations are written out (17.42 lists the slide&rsquo;s own spellings); an empty cell on the slide is shown as
  &mdash;. Use it as the one-page review: every protozoan row is taught in full in 17.3&ndash;17.19, every helminth
  row later in this section.</p>
  """ + fig(4, 1, "l17-s004-organism-table-amebas-flagellates.jpg",
      "A four-column table headed Organism, Disease, Other information, Photo, with rows for Entamoeba histolytica, Naegleria fowleri, Acanthamoeba, Balantidium coli, Giardia lamblia and Trichomonas vaginalis; photographs of purple-stained amebas, two oval cysts and two pear-shaped flagellates sit in the Photo column.",
      "<b>Her table, part 1: the amebas, the ciliate and two flagellates.</b> Look for the one-line hook in each row: "
      "fecal-oral route (<em>Entamoeba</em>), Florida&rsquo;s freshwater lakes (<em>Naegleria</em>), contact lens "
      "wearers (<em>Acanthamoeba</em>), pigs and cattle (<em>Balantidium</em>), campers (<em>Giardia</em>), the most "
      "common curable sexually transmitted disease in young women (<em>Trichomonas</em>).") + """
  <table>
    <tr><th>Organism</th><th>Disease</th><th>Other information</th><th>Photo</th></tr>
    <tr><td><em>Entamoeba histolytica</em></td><td>Amebiasis&mdash;amebic dysentery<br>Intestinal amebiasis<br>Extraintestinal amebiasis</td><td>Fecal oral route</td><td>&mdash;</td></tr>
    <tr><td><em>Naegleria fowleri</em></td><td>Primary Acute Meningoencephalitis</td><td>While only about 200 cases reported worldwide&mdash;is prevalent in Florida&rsquo;s freshwater lakes</td><td>Photo: purple-stained trophozoites (the picture on slide 28)</td></tr>
    <tr><td><em>Acanthamoeba</em></td><td>Granulomatous Amebic Encephalitis</td><td>Found in contact lens wearers</td><td>&mdash;</td></tr>
    <tr><td><em>Balantidium coli</em></td><td>Balantidiosis</td><td>Pigs and cattle as alternate hosts</td><td>&mdash;</td></tr>
    <tr><td><em>Giardia lamblia</em></td><td>Giardiasis</td><td>Common in campers</td><td>Photo: two oval stained cysts (the picture on slide 40)</td></tr>
    <tr><td><em>Trichomonas vaginalis</em></td><td>Trichomoniasis</td><td>Most common curable sexually transmitted disease in young women foul-smelling, green-to-yellow discharge; vulvitis; cervicitis; urinary frequency and pain</td><td>Photo: two pear-shaped flagellates (the picture on slide 38)</td></tr>
  </table>
  """ + fig(5, 1, "l17-s005-organism-table-blood-protozoa.jpg",
      "The same four-column table continued, with rows for Trypanosoma brucei, Trypanosoma cruzi, Leishmania, Plasmodium and Toxoplasma gondii; the Photo column holds a pink blood smear with two wavy purple flagellates and a smear of red blood cells with small rings inside them.",
      "<b>Her table, part 2: the blood and tissue protozoa.</b> Look for the vector in every row: tsetse fly "
      "(<em>T. brucei</em>), reduviid (kissing) bug (<em>T. cruzi</em>), sand fly with the dog as alternate host "
      "(<em>Leishmania</em>), <em>Anopheles</em> mosquito (<em>Plasmodium</em>); and for <em>Toxoplasma</em>, the cat "
      "box and the fetus.") + """
  <table>
    <tr><th>Organism</th><th>Disease</th><th>Other information</th><th>Photo</th></tr>
    <tr><td><em>Trypanosoma brucei</em></td><td>African sleeping sickness</td><td>Tsetse fly as vector</td><td>Photo, captioned &ldquo;Blood smear with flagellates swimming between cells&rdquo;</td></tr>
    <tr><td><em>Trypanosoma cruzi</em></td><td>Chagas disease</td><td>Reduviid (kissing) bug is vector and was a tropical disorder but it is becoming an issue in Southern United States as vector expands its range</td><td>&mdash;</td></tr>
    <tr><td><em>Leishmania</em> sp.</td><td>Leishmaniasis, Baghdad boil, Espundia, Kala azar</td><td>Dog alternate host, sand fly is vector</td><td>&mdash;</td></tr>
    <tr><td><em>Plasmodium</em> sp.</td><td>Malaria</td><td><em>Anopheles</em> Mosquito is the vector. Malaise, fatigue, aches, nausea Regular episodes of chills-fever-sweating</td><td>&ldquo;<em>Plasmodium</em> organism shown as ring form inside erythrocytes&rdquo;, with the photo (the picture on slide 60)</td></tr>
    <tr><td><em>Toxoplasma gondii</em></td><td>Toxoplasmosis</td><td>Danger to fetus&mdash;pregnant women should not clean catbox due to danger of transplacental transmission. Danger of central nervous system involvement for acquired immunodeficiency syndrome patients</td><td>&mdash;</td></tr>
  </table>
  """ + fig(6, 1, "l17-s006-organism-table-coccidia.jpg",
      "The table continued with three rows: Cryptosporidium, Isospora belli with empty cells, and Cyclospora cayetanensis.",
      "<b>Her table, part 3: the intestinal coccidians.</b> Only <em>Cryptosporidium</em> carries a hook: the Wisconsin "
      "outbreak from unpurified water, and bioterrorism. The <em>Isospora</em> row is empty on the slide (taught on slide "
      "74, 17.17).") + """
  <table>
    <tr><th>Organism</th><th>Disease</th><th>Other information</th><th>Photo</th></tr>
    <tr><td><em>Cryptosporidium</em> sp.</td><td>Gastroenteritis</td><td>Major outbreak in Wisconsin from unpurified water&mdash;agent for bioterrorism</td><td>&mdash;</td></tr>
    <tr><td><em>Isospora belli</em></td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td><em>Cyclospora cayetanensis</em></td><td>Cyclosporiasis</td><td>&mdash;</td><td>&mdash;</td></tr>
  </table>
  """ + fig(6, 2, "l17-s006-organism-table-intestinal-nematodes.jpg",
      "Under the heading Helminths, a table with rows for Trichuris trichiura, Ascaris lumbricoides, Enterobius vermicularis and Necator americanus; the Ascaris photo cell shows a pale adult worm on a dark background above two round eggs.",
      "<b>Her table, part 4 (headed Helminths on slide 6): the intestinal nematodes.</b> Look for the hooks: intestinal "
      "obstruction (<em>Ascaris</em>), daycare and the Scotch tape test (<em>Enterobius</em>), skin of the soles of "
      "the feet (<em>Necator</em>).") + """
  <table>
    <tr><th>Organism</th><th>Disease</th><th>Other information</th><th>Photo</th></tr>
    <tr><td><em>Trichuris trichiura</em></td><td>Whipworm</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td><em>Ascaris lumbricoides</em></td><td>Roundworm</td><td>abdominal pain and intestinal obstruction</td><td>Photos: an adult worm and two eggs</td></tr>
    <tr><td><em>Enterobius vermicularis</em></td><td>Pinworm</td><td>Very common in daycare situations&mdash;transmission by direct contact and fomites -- Diagnosed with Scotch tape test</td><td>&mdash;</td></tr>
    <tr><td><em>Necator americanus</em></td><td>Hookworm</td><td>Transmitted through skin on soles of feet. causes pneumonia, nausea, vomiting, cramps, and bloody diarrhea</td><td>&mdash;</td></tr>
  </table>
  """ + fig(7, 1, "l17-s007-organism-table-tissue-nematodes.jpg",
      "The table continued with rows for Angiostrongylus cantonensis, Strongyloides stercoralis and Trichinella spiralis; the photo cell for Angiostrongylus shows a long coiled worm with a dark spiral stripe, and the Trichinella cell a pink muscle section with small coiled larvae.",
      "<b>Her table, part 5: three more nematodes.</b> Look for the snail and the rat lungworm (<em>Angiostrongylus</em>, "
      "with its <b>barber-pole</b> adult female) and undercooked pork with encystment in muscle "
      "(<em>Trichinella</em>).") + """
  <table>
    <tr><th>Organism</th><th>Disease</th><th>Other information</th><th>Photo</th></tr>
    <tr><td><em>Angiostrongylus cantonensis</em></td><td>Eosinophilic meningitis (Rat lungworm)</td><td>Snails are intermediate hosts acquired by eating larvae in snails or contaminated water or vegetables</td><td>Photo, captioned &ldquo;Adult female worm of <em>Angiostrongylus cantonensis</em> with characteristic barber-pole appearance (anterior end of worm is to the top). Scale bar is 1 mm.&rdquo;</td></tr>
    <tr><td><em>Strongyloides stercoralis</em></td><td>Threadworm</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td><em>Trichinella spiralis</em></td><td>Trichinosis</td><td>acquired through ingestion of undercooked pork--encystment in muscle will cause symptoms</td><td>Photo: a muscle section</td></tr>
  </table>
  """ + fig(8, 1, "l17-s008-organism-table-filariae-flukes-tapeworms.jpg",
      "A wide table with columns Organism, Disease, Other Information, Photo, and rows for Wuchereria bancrofti, Onchocerca volvulus, Loa loa, Schistosoma, Toxocara canis and cati, Opisthorchis sinensis, Fasciola hepatica, Paragonimus westermani, Taenia saginata, Taenia solium and Echinococcus; three small photographs sit beside the tapeworm rows.",
      "<b>Her table, part 6: the filarial worms, the flukes and the tapeworms.</b> Look for how each is acquired: "
      "mosquito, black flies, fly bite, water where the snail lives, feces or undercooked waterfowl, freshwater fish "
      "(&ldquo;don&rsquo;t eat freshwater sushi&rdquo;), undercooked meat versus embryonated eggs, dogs.") + """
  <table>
    <tr><th>Organism</th><th>Disease</th><th>Other Information</th><th>Photo</th></tr>
    <tr><td><em>Wuchereria bancrofti</em></td><td>Bancroftian Filariasis--Elephantiasis</td><td>Spread by mosquito</td><td>&mdash;</td></tr>
    <tr><td><em>Onchocerca volvulus</em></td><td>River Blindness</td><td>Spread by black flies Bacterial coinfection</td><td>&mdash;</td></tr>
    <tr><td><em>Loa loa</em></td><td>Eye Worm</td><td>Spread by fly bite</td><td>&mdash;</td></tr>
    <tr><td><em>Schistosoma</em> sp.</td><td>Schistosomiasis</td><td>Blood fluke with alternate host of a freshwater snail. Individuals acquire by contact with water in which the snail lives</td><td>&mdash;</td></tr>
    <tr><td><em>Toxocara canis</em> and <em>cati</em></td><td>Toxocariasis</td><td>Dog and cat roundworm&mdash;ingestion of feces or undercooked alternate host (waterfowl)</td><td>&mdash;</td></tr>
    <tr><td><em>Opisthorchis sinensis</em></td><td>Chinese Liver Fluke</td><td>Cycles between humans and fish or snails&mdash;don&rsquo;t eat freshwater sushi</td><td>&mdash;</td></tr>
    <tr><td><em>Fasciola hepatica</em></td><td>Liver Fluke</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td><em>Paragonimus westermani</em></td><td>Lung Fluke</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td><em>Taenia saginata</em></td><td>Taeniasis</td><td>Beef tapeworm&mdash;Absorbs food directly through cuticle; reproduces via proglottids. Causes weight loss and wasting in host</td><td>Photo (pink, stained)</td></tr>
    <tr><td><em>Taenia solium</em></td><td>Taeniasis and Cysticercosis</td><td>Pork tapeworm&mdash;Taeniasis if ingest undercooked meat; Cysticercosis if ingest embryonated eggs&mdash;migrates to musculature or brain producing lesions</td><td>Photo</td></tr>
    <tr><td><em>Echinococcus</em></td><td>Echinococcosis and Hydatid Disease</td><td>Tiny tapeworm Acquired from dogs; produces hydatid cysts which may need to be surgically removed. Alveolar form causes parasitic tumors</td><td>Photo (red, surgical)</td></tr>
  </table>

  <h3 class="sub" id="par-protozoa">17.2 &middot; Objective 1 &mdash; Protozoa: groups, life cycles and drugs</h3>
  <p>Slide 11 opens the <strong>protozoan parasites</strong>. <strong>Typical protozoan pathogens</strong> are
  <strong>single-celled, animal-like microbes, most having some form of motility</strong>. There are an
  <strong>estimated 100,000 species</strong>, of which <strong>approximately 25 are important pathogens</strong>. In
  2014 the World Health Organization stressed the serious and increasing threat of <strong>vector-borne parasitic
  diseases</strong> with the slogan <strong>&ldquo;Small bite, big threat.&rdquo;</strong></p>
  <table>
    <tr><th>Group (slide 12)</th><th>How it moves (the deck&rsquo;s own words)</th><th>Organisms in this lecture</th></tr>
    <tr><td><strong>Ameboid</strong> (the amebas; slide 12 writes &ldquo;Amoeboid&rdquo;)</td><td>A trophozoite &ldquo;motile by means of pseudopods&rdquo; (slide 16)</td><td><em>Entamoeba histolytica</em>, <em>Naegleria fowleri</em>, <em>Acanthamoeba</em></td></tr>
    <tr><td><strong>Ciliated</strong></td><td>Cilia tufts on the trophozoite (slide 34 drawing)</td><td><em>Balantidium coli</em>, &ldquo;an intestinal ciliate&rdquo;</td></tr>
    <tr><td><strong>Flagellated</strong></td><td>Flagella, and in <em>Trichomonas</em> an undulating membrane (slide 36)</td><td><em>Trichomonas</em>, <em>Giardia</em>; the hemoflagellates <em>Trypanosoma</em> and <em>Leishmania</em></td></tr>
    <tr><td><strong>Apicomplexa</strong></td><td><strong>Lack locomotor organelles</strong> in the trophozoite state (slide 55)</td><td><em>Plasmodium</em>, <em>Toxoplasma</em>, <em>Cryptosporidium</em>; with <em>Sarcocystis</em>, <em>Isospora</em>, <em>Cyclospora</em> and <em>Babesia</em> among the coccidians (slide 63)</td></tr>
  </table>
  <p><strong>Life cycles vary.</strong></p>
  <ul>
    <li><strong>Most propagate by simple asexual cell division of the active feeding cell, the
    trophozoite.</strong></li>
    <li><strong>Many undergo formation of a cyst.</strong></li>
    <li>Others have a <strong>complex life cycle that includes asexual and sexual phases</strong>.</li>
  </ul>

  <h4 class="subsub">Major pathogenic protozoa, infections and primary sources (slide 13)</h4>
  """ + fig(13, 1, "l17-s013-protozoa-sources-table.jpg",
      "A textbook table titled Major Pathogenic Protozoa, Infections, and Primary Sources, with two columns, Protozoan/Disease and Reservoir/Source, grouped under Ameboid, Ciliated, Flagellated and Apicomplexan Protozoa.",
      "<b>Where each protozoan comes from.</b> Read the right-hand column: <b>human</b> (<em>Entamoeba</em>, "
      "<em>Trichomonas</em>, <em>Plasmodium</em>), <b>free-living in water</b> (<em>Naegleria</em>, "
      "<em>Acanthamoeba</em>), <b>zoonotic</b> (pigs for <em>Balantidium</em>; water and food for <em>Giardia</em>), "
      "and <b>vector-borne</b> (the hemoflagellates and malaria).") + """
  <table>
    <tr><th>Protozoan/Disease*</th><th>Reservoir/Source</th></tr>
    <tr><td colspan="2"><strong>Ameboid Protozoa</strong></td></tr>
    <tr><td>Amebiasis: <em>Entamoeba histolytica</em></td><td>Human/water and food</td></tr>
    <tr><td>Brain infection: <em>Naegleria</em>, <em>Acanthamoeba</em></td><td>Free-living in water</td></tr>
    <tr><td colspan="2"><strong>Ciliated Protozoa</strong></td></tr>
    <tr><td>Balantidiosis: <em>Balantidium coli</em></td><td>Zoonotic in pigs</td></tr>
    <tr><td colspan="2"><strong>Flagellated Protozoa</strong></td></tr>
    <tr><td>Giardiasis: <em>Giardia lamblia</em></td><td>Zoonotic/water and food</td></tr>
    <tr><td>Trichomoniasis: <em>Trichomonas vaginalis</em></td><td>Human</td></tr>
    <tr><td colspan="2">Hemoflagellates</td></tr>
    <tr><td>&nbsp;&nbsp;Trypanosomiasis: <em>Trypanosoma brucei</em>, <em>T. cruzi</em></td><td>Zoonotic/vector-borne</td></tr>
    <tr><td>&nbsp;&nbsp;Leishmaniasis: <em>Leishmania donovani</em>, <em>L. tropica</em>, <em>L. brasiliensis</em></td><td>Zoonotic/vector-borne</td></tr>
    <tr><td colspan="2"><strong>Apicomplexan Protozoa</strong></td></tr>
    <tr><td>Malaria: <em>Plasmodium vivax</em>, <em>P. falciparum</em>, <em>P. malariae</em></td><td>Human/vector-borne</td></tr>
    <tr><td>Toxoplasmosis: <em>Toxoplasma gondii</em></td><td>Zoonotic/vector-borne</td></tr>
    <tr><td>Cryptosporidiosis: <em>Cryptosporidium</em></td><td>Free-living/water, food</td></tr>
    <tr><td>Isosporosis: <em>Isospora belli</em></td><td>Dogs, other mammals</td></tr>
    <tr><td>Cyclosporiasis: <em>Cyclospora cayetanensis</em></td><td>Water/fresh produce</td></tr>
  </table>
  <p>The asterisk&rsquo;s footnote is not on the slide. Two cells disagree with later slides: this table lists
  <strong>three</strong> <em>Plasmodium</em> species where slide 56 lists four, and it calls toxoplasmosis
  vector-borne where slides 64&ndash;65 describe ingestion and transplacental spread (17.42).</p>

  <h4 class="subsub">Antiprotozoan drugs (slide 14)</h4>
  <ul>
    <li><mark class="prof-highlight"><strong>Relatively few in comparison with antibacterial agents</strong></mark> &#9733; Starred on the slide.</li>
    <li><strong>Work against eukaryotic cells</strong> (the parasite&rsquo;s cells are eukaryotic, like ours).</li>
    <li><mark class="prof-highlight"><strong>Toxicity problems, severe side effects</strong></mark> &#9733; Starred on the slide.</li>
  </ul>
  """ + fig(14, 1, "l17-s014-antiprotozoan-drugs-table.jpg",
      "Table 23.2, Guidelines for Antiprotozoan Drugs, on a yellow background, with columns Infectious Agent, Typical Infection, Drugs of Choice and Mechanism of Drug Action, rows for seven protozoa, and two footnotes.",
      "<b>Table 23.2, Guidelines for Antiprotozoan Drugs.</b> Look for the drug that recurs: <b>metronidazole</b> for "
      "<em>Entamoeba</em>, <em>Giardia</em> and <em>Trichomonas</em> (the anaerobic protozoa that lack mitochondria), "
      "and the hemoglobin-metabolism drugs for malaria. Melarsoprol is &ldquo;arsenic-based, very toxic&rdquo;.") + """
  <table>
    <tr><th>Infectious Agent</th><th>Typical Infection</th><th>Drugs of Choice</th><th>Mechanism of Drug Action</th></tr>
    <tr><td rowspan="3"><em>Entamoeba histolytica</em></td><td rowspan="3">Amebiasis</td><td>Metronidazole*</td><td>Specific for anaerobes; inhibits DNA repair</td></tr>
    <tr><td>Iodoquinol</td><td>Acts locally in intestine; unknown mode of action</td></tr>
    <tr><td>Chloroquine</td><td>Toxic to the parasite by interfering with hemoglobin metabolism in the food vacuole</td></tr>
    <tr><td rowspan="2"><em>Giardia lamblia</em></td><td rowspan="2">Giardiasis</td><td>Hetronidazole (as printed: metronidazole, the drug slide 41 names)</td><td>See above; selectively blocks parasite metabolism</td></tr>
    <tr><td>Quinacrine</td><td>Is a dye that inserts into DNA and disrupts its functions</td></tr>
    <tr><td rowspan="4"><em>Plasmodium</em></td><td rowspan="4">Malaria</td><td>Chloroquine</td><td>See above</td></tr>
    <tr><td>Quinine</td><td>Same as chloroquine, mefloquine</td></tr>
    <tr><td>Miefloquine (as printed: mefloquine)</td><td>Interferes with metabolism and use of hemoglobin</td></tr>
    <tr><td>Artemether</td><td>Redox reagent; produces reactive oxygen radicals</td></tr>
    <tr><td><em>Toxoplasma gondii</em></td><td>Toxoplasmosis</td><td>Pyrimethamine<br>Sulfadiazine</td><td>Together with sulfadiazine, inhibits enzymes in the pathway for folate synthesis</td></tr>
    <tr><td><em>Trichomonas vaginalis</em></td><td>Trichomoniasis</td><td>Metronidazole</td><td>See above</td></tr>
    <tr><td rowspan="4"><em>Trypanosoma brucei</em></td><td rowspan="4">Sleeping sickness</td><td>Suramin**</td><td>Inhibits NADH (reduced nicotinamide adenine dinucleotide) oxidation; blocks aerobic respiration</td></tr>
    <tr><td>Pentamidine</td><td>Blocks nucleic acid synthesis</td></tr>
    <tr><td>Eflomithine (as printed: eflornithine, as slide 47 spells it)</td><td>Inhibits deamination of amino acids</td></tr>
    <tr><td>Melarsoprol</td><td>Arsenic-based, very toxic, inhibits many enzymes</td></tr>
    <tr><td rowspan="2"><em>Trypanosoma cruzi</em></td><td rowspan="2">Chagas disease</td><td>Benzonidazole</td><td>Interferes with protein synthesis and microtubule formation</td></tr>
    <tr><td>Nifurtimox</td><td>Breaks up DNA and creates superoxide radicals</td></tr>
  </table>
  <p>* <strong>Metronidazole is also called flagyl.</strong> It is <strong>selectively toxic to anaerobic protozoa
  like <em>Entamoeba</em>, <em>Giardia</em>, and <em>Trichomonas</em>, which lack mitochondria.</strong><br>
  ** Available in the United States only from the Drug Service of the Centers for Disease Control and
  Prevention.</p>

  <h3 class="sub" id="par-entamoeba">17.3 &middot; Objective 1 &mdash; <em>Entamoeba histolytica</em> and amebiasis</h3>
  <p>Slide 15 opens the <strong>infective amebas</strong>: <em>Entamoeba histolytica</em> (this section),
  <em>Naegleria fowleri</em> (17.4) and <em>Acanthamoeba</em> (17.5).</p>
  """ + fig(15, 2, "l17-s015-amebas-in-tissue.jpg",
      "A purple-stained tissue section crowded with dark, irregular cells and a few larger round pale cells with visible nuclei.",
      "<b>Infective amebas</b> (slide 15&rsquo;s title), in a stained tissue section; the slide adds no labels.",
      "Courtesy of University of Minnesota - SVM.") + """
  """ + fig(15, 1, "l17-s015-infective-ameba.jpg",
      "A single blue-stained round cell with several dark dots inside and a small ring near its edge.",
      "<b>Infective amebas</b>: the second, smaller picture on slide 15, a single stained cell (unlabeled on the "
      "slide).") + """
  <h4 class="subsub">Morphology and hosts</h4>
  <ul>
    <li><em>Entamoeba histolytica</em> <strong>alternates between a large trophozoite, motile by means of
    pseudopods, and a smaller nonmotile cyst</strong>.</li>
    <li>The <strong>trophozoite has a large nucleus and lacks most other organelles</strong>.</li>
    <li>The name: <strong><em>histolytica</em> = <em>histo</em>, tissue + <em>lytica</em>, lysis</strong> (slide 19).</li>
    <li><strong>Humans are the primary hosts.</strong> It is <strong>ingested</strong>.</li>
    <li>It is <strong>carried by 10% of the world population, asymptomatically</strong>, and <strong>kills 100,000
    people per year</strong>.</li>
  </ul>
  """ + fig(17, 1, "l17-s017-trophozoite-and-cyst.jpg",
      "Two micrographs side by side with 10 micrometer scale bars: on the left an oval greenish cell with a dark ring-shaped nucleus, labeled Trophozoite; on the right a smaller round gray cell with dark spots, labeled Cyst.",
      "<b>The two forms of <em>Entamoeba histolytica</em></b>: (a) the larger, motile <b>trophozoite</b> and (b) the "
      "smaller, nonmotile <b>cyst</b> (both with a 10&nbsp;&micro;m scale bar).") + """
  <h4 class="subsub">How people acquire it, and where</h4>
  <ul>
    <li>By the <strong>fecal oral route</strong> (her table, slide 4): cysts are swallowed. The reservoir and source
    is <strong>human, water and food</strong> (slide 13).</li>
    <li><strong>Prevalent in tropical countries</strong>; related to <strong>fertilization practices and sewage
    treatment</strong>.</li>
    <li><strong>Epidemics</strong> sometimes occur in <strong>concentrated populations where water supplies are
    polluted: prisons, hospitals, juvenile care institutions</strong>.</li>
    <li><strong>Sometimes sexually transmitted.</strong></li>
  </ul>
  <h4 class="subsub">Life cycle (slides 18&ndash;19)</h4>
  <p><strong>Cysts are swallowed and arrive at the small intestine</strong>; the <strong>alkaline pH and digestive
  juices stimulate the cysts to release 4 trophozoites</strong>. The <strong>trophozoites attach, multiply, actively
  move about and feed</strong>. <strong>Cysts are produced after the active phase of disease</strong> (slide 23) and
  leave in the feces.</p>
  """ + fig(18, 1, "l17-s018-entamoeba-life-cycle.jpg",
      "Left, a cycle of drawings: an irregular trophozoite with a nucleus, karyosome and ingested red blood cells; a round mature cyst with nuclei and chromatoidals; excystment into a four-nucleate form; and small trophozoites released. Right, a human digestive tract with five numbered steps from mouth to rectum.",
      "<b>The <em>Entamoeba histolytica</em> life cycle.</b> (a) <b>Trophozoite</b>: nucleus, karyosome and "
      "<b>ingested red blood cells</b>. (b) <b>Mature cyst</b>: chromatoidals and nuclei. (c) <b>Excystment</b>, "
      "releasing trophozoites. (d) In the body: (1) <b>cysts are eaten</b>; (2) cysts pass through the stomach; (3) "
      "<b>trophozoites are released in the small intestine</b>; (4) <b>trophozoites encyst in the large "
      "intestine</b>; (5) <b>cysts are released in feces</b>.") + """
  <h4 class="subsub">Disease and clinical manifestations</h4>
  <p><strong>Asymptomatic in 90% of patients</strong>; severity is related to the <strong>strain, the amount of
  inoculum and host conditions</strong>. Amebiasis takes <strong>two forms, intestinal and extraintestinal</strong>
  (her table names the disease &ldquo;amebiasis&mdash;amebic dysentery&rdquo;).</p>
  <table>
    <tr><th></th><th>Intestinal amebiasis (slide 20)</th><th>Extraintestinal amebiasis (slide 21)</th></tr>
    <tr><td>Where</td><td><strong>Cecum, appendix, colon, rectum</strong></td><td>Amebas <strong>invade the viscera of the peritoneal cavity</strong>; <strong>most commonly the liver</strong>; can also infect the <strong>lungs</strong>, and the spleen, adrenals, kidneys, skin and brain</td></tr>
    <tr><td>What it does</td><td>The ameba may <strong>secrete enzymes that dissolve tissues</strong> and penetrate deeper layers of the mucosa</td><td>Produces <strong>abscesses with active trophozoites: amebic hepatitis</strong>; in the lungs, <strong>pulmonary amebiasis</strong></td></tr>
    <tr><td>Signs</td><td><strong>Dysentery</strong>, abdominal pain, fever, diarrhea and weight loss</td><td>Abscess (slide 22: an amebic abscess perforating the abdominal wall)</td></tr>
    <tr><td>Danger</td><td>Life-threatening: <strong>hemorrhage, perforation, appendicitis</strong>, and tumorlike growths, <strong>amebomas</strong></td><td>Severe forms of disease have a <strong>10% fatality rate</strong></td></tr>
  </table>
  """ + fig(20, 1, "l17-s020-intestinal-erosion.jpg",
      "A length of opened intestine on a blue background, its yellow-brown lining ridged and ragged, with a pointer labeled Erosion of intestine.",
      "<b>Intestinal amebiasis</b>: <b>erosion of the intestine</b> where the amebas have dissolved the lining.") + """
  """ + fig(20, 2, "l17-s020-ameboma.jpg",
      "A view inside the bowel: red, inflamed lining with pale patches and a lumpy mass, a pointer labeled ameboma.",
      "<b>An ameboma</b> (labeled &ldquo;Amoeboma&rdquo;), the tumorlike growth of intestinal amebiasis.") + """
  """ + fig(22, 1, "l17-s022-amebic-abscess.jpg",
      "Photograph of a thin patient lying on a green sheet, with a round open crater in the skin of the abdomen ringed with yellow-white tissue.",
      "<b>Amebic abscess with perforation of the abdominal wall</b> (slide 22&rsquo;s title): extraintestinal disease "
      "breaking through to the skin.") + """
  <h4 class="subsub">Diagnosis, treatment and prevention (slide 23)</h4>
  <ul>
    <li><strong>Diagnosis</strong>: the symptoms are <strong>similar to bacillary dysentery</strong>, so diagnosis rests on
    <strong>examination of a fecal smear</strong>, <strong>enzyme-linked immunosorbent assay with monoclonal
    antibodies</strong>, and the <strong>history</strong>.</li>
    <li><strong>Treatment</strong>: <strong>iodoquinol acts in feces</strong> (Table 23.2: &ldquo;acts locally in
    intestine&rdquo;); <strong>metronidazole (Flagyl), dehydroemetine and chloroquine act in tissues</strong>; plus
    antidiarrheals and fluid and electrolyte replacement.</li>
    <li><strong>Prevention</strong>: <mark class="prof-highlight"><strong>water treatment</strong></mark>; a <strong>vaccine is under
    development</strong>. &#9733; Dr. Webster said it twice: &ldquo;water treatment is the best prevention&rdquo;.</li>
  </ul>

  <h3 class="sub" id="par-naegleria">17.4 &middot; Objective 1 &mdash; <em>Naegleria fowleri</em> and amebic meningoencephalitis</h3>
  <p><strong>Amebic meningoencephalitis is caused by <em>Naegleria fowleri</em> and <em>Acanthamoeba</em></strong>
  (slide 24). Both <strong>ordinarily inhabit standing water with a high bacterial count</strong>: <strong>hot
  springs</strong>, <strong>lakes and streams</strong>, and <strong>unchlorinated swimming pools</strong>. Slide 13
  lists both as &ldquo;free-living in water&rdquo;, causing brain infection. It is a <strong>relatively rare
  disease&mdash;but</strong> (the slide breaks off there, and the case slides follow).</p>
  """ + fig(24, 1, "l17-s024-pam-case-map.jpg",
      "A map of the United States shaded by number of case reports: dark blue for 8 or more in California, Arizona, Texas, Florida and South Carolina; medium green for 4 to 7 in several southern and southeastern states; light green for 1 to 3 scattered across the South and Midwest; gray elsewhere.",
      "<b>Number of case reports of primary amebic meningoencephalitis caused by <em>Naegleria fowleri</em> "
      "(N&nbsp;=&nbsp;157) by state of exposure, United States, 1962&ndash;2022.</b> Look at where the 8-or-more states "
      "are: <b>California, Arizona, Texas, Florida and South Carolina</b>, all southern; the lighter states run into the "
      "Midwest.", "Map: Centers for Disease Control and Prevention.") + """
  """ + fig(24, 2, "l17-s024-florida-lakes-map.jpg",
      "A 1977 journal page headed Pathogenic Naegleria in Florida Lakes, showing an outline map of Florida with county lines and fractions written in several counties.",
      "<b>&ldquo;Pathogenic <em>Naegleria</em> in Florida lakes&rdquo;</b> (a 1977 journal page): the fractions mark, county "
      "by county, the lakes that yielded pathogenic <em>Naegleria</em>. Her table (slide 4) says it &ldquo;is prevalent "
      "in Florida&rsquo;s freshwater lakes&rdquo;, and slide 29 that over 46% of lakes in Florida have <em>N. "
      "fowleri</em>.", crop=(0, 0, 660, 438)) + """
  <h4 class="subsub">Morphology</h4>
  <p>The slides show <em>Naegleria</em> in <strong>three stages: a cyst stage, a trophozoite stage and a flagellated
  stage</strong> (slide 25&rsquo;s picture). It is the <strong>trophozoite that burrows through the nasal
  mucosa</strong> (slide 29).</p>
  """ + fig(25, 2, "l17-s025-naegleria-three-stages.jpg",
      "Three gray micrographs in a row labeled Cyst stage, a smooth round cell with a thick wall; Trophozoite stage, an irregular cell with blunt projections; and Flagellated stage, a smaller oval cell.",
      "<b>The three stages of <em>Naegleria</em></b>: <b>cyst</b> (round, walled), <b>trophozoite</b> (irregular, with "
      "pseudopods) and <b>flagellated</b> stage.") + """
  """ + fig(25, 1, "l17-s025-naegleria-illustration.jpg",
      "A colored three-dimensional illustration of several pink, lobed, translucent amebas with a dark central nucleus and many small dark granules, on a blurred green background.",
      "<b><em>Naegleria</em></b>, as illustrated on the recent-cases slide (slide 25): lobed amebas with a large "
      "central nucleus.") + """
  <h4 class="subsub">Cases (slides 25&ndash;27)</h4>
  <ul>
    <li><strong>1962&ndash;2023: 164 cases in the United States, 4 survivors.</strong></li>
    <li><strong>2 cases in Louisiana from neti pots</strong>; 1 case in Louisiana from <strong>tap water in a home water
    slide</strong>.</li>
    <li>Summer 2012, South Carolina, Lake Marion; 2019, a North Carolina water park; 2020, cases in Florida and Texas;
    2021, cases in Texas and California.</li>
    <li>2022: 3 confirmed cases in Iowa, Nebraska and Arizona. <strong>Most cases occur in the southern United
    States, but rising temperatures have created favorable environments farther north.</strong></li>
    <li>2023: 7 cases in California, Florida, Indiana, Georgia, Nevada, Texas and Arkansas. 2024: Texas
    (<strong>nasal rinsing from tap water in a recreational vehicle tank</strong>). 2025: Missouri (water skiing) and
    South Carolina (a pediatric case). 2026: Louisiana (swimming in Lake Claiborne).</li>
    <li>The Centers for Disease Control and Prevention estimates <strong>more are infected than reported</strong>:
    <strong>16 deaths per year</strong>, equally distributed between males and females.</li>
  </ul>
  """ + fig(27, 1, "l17-s027-pam-facts-table.jpg",
      "A two-column table of metrics and figures about brain-eating amebas in the United States, 2026.",
      "<b>Interesting facts about brain-eating amebas in the United States, 2026</b> (the first table on slide 27), "
      "transcribed below.") + """
  <table>
    <tr><th>Metric</th><th>Figure</th></tr>
    <tr><td>Total confirmed United States primary amebic meningoencephalitis cases, 1937&ndash;2025 (Centers for Disease Control and Prevention, updated March 2026)</td><td>180</td></tr>
    <tr><td>Total United States primary amebic meningoencephalitis cases by known state of exposure</td><td>173</td></tr>
    <tr><td>Cases with unknown location of exposure</td><td>7</td></tr>
    <tr><td>Typical annual case count in the United States</td><td>Fewer than 10</td></tr>
    <tr><td>Historical fatality rate</td><td>More than 97%</td></tr>
    <tr><td>Known United States survivors (of 167 cases, 1962&ndash;2022/2025 window)</td><td>4</td></tr>
    <tr><td>States with the most confirmed primary amebic meningoencephalitis cases</td><td>Texas and Florida</td></tr>
    <tr><td>Age/sex group with the highest case count</td><td>Males aged 10&ndash;14 (45 cases)</td></tr>
    <tr><td>Share of cases occurring in July and August</td><td>73%</td></tr>
    <tr><td>Estimated true annual United States case burden (Centers for Disease Control and Prevention 2017 research letter)</td><td>~16 per year (70&ndash;80% may go undiagnosed)</td></tr>
  </table>
  """ + fig(27, 2, "l17-s027-pam-survival-table.jpg",
      "A two-column table of death and survival statistics for brain-eating amebas in the United States, 2026.",
      "<b>Deaths and survival rate statistics for brain-eating amebas in the United States, 2026</b> (the second table "
      "on slide 27), transcribed "
      "below.") + """
  <table>
    <tr><th>Metric</th><th>Figure</th></tr>
    <tr><td>Historical case fatality rate</td><td>&gt;97%</td></tr>
    <tr><td>Known United States survivors (1962&ndash;2025 window)</td><td>4 (out of 167 cases)</td></tr>
    <tr><td>Survival rate implied by known survivors</td><td>~2.4%</td></tr>
    <tr><td>Global confirmed cases through 2018</td><td>381</td></tr>
    <tr><td>Global known survivors through 2018</td><td>7 (1.8%)</td></tr>
    <tr><td>Pediatric survival rate (global systematic review, 2000&ndash;2024)</td><td>22%</td></tr>
    <tr><td>Adult survival rate (global systematic review, 2000&ndash;2024)</td><td>7.1%</td></tr>
  </table>
  <p>The take-away from the numbers: <strong>rare, nearly always fatal (more than 97%), in summer, mostly in the
  South</strong>. The counts differ from slide to slide because each uses a different window (17.42).</p>
  <h4 class="subsub">How people acquire it (slide 28)</h4>
  <ul>
    <li><strong>Most cases are children and young adults</strong>, after exposure to <strong>freshwater lakes and
    streams</strong>.</li>
    <li><strong>Acquired through nasal contact with water</strong>: <strong>diving, waterskiing, jetskiing</strong>; a
    recent case in an <strong>indoor surfing facility</strong>; and <strong>rinsing sinuses, even with tap
    water</strong>.</li>
  </ul>
  """ + fig(28, 1, "l17-s028-naegleria-trophozoites.jpg",
      "Several small purple-blue stained cells with irregular outlines and a dark nucleus each, on a white background.",
      "<b><em>Naegleria</em> trophozoites</b>, stained: irregular amebas, each with a single dark nucleus (the same "
      "picture is in her table on slide 4).") + """
  <h4 class="subsub">Primary amebic meningoencephalitis (slide 29)</h4>
  <p>Slide 29&rsquo;s title calls the disease <strong>&ldquo;Primary Acute Meningoencephalitis&rdquo;</strong>, as does
  her table; slides 24 and 30 call it primary amebic meningoencephalitis (17.42). Same disease.</p>
  <ul>
    <li>The <strong>trophozoite burrows through the nasal mucosa</strong> and <strong>travels into the brain through
    the olfactory nerve</strong>.</li>
    <li><strong>Symptoms</strong>: <strong>headache, respiratory symptoms, fever, vomiting, stiff neck</strong>.</li>
    <li><strong>Rapid destruction of the brain and spinal cord</strong>: confusion, lack of balance, hallucinations,
    coma, <strong>death in 3&ndash;7 days</strong>.</li>
    <li><strong>Diagnosis</strong>: the slides give no laboratory test for <em>Naegleria</em>.</li>
    <li><strong>Prevention</strong>: <strong>over 46% of lakes in Florida have <em>N. fowleri</em></strong>;
    <strong>don&rsquo;t swim or dive in unchlorinated water</strong>; <strong>use nose plugs</strong>.</li>
    <li><mark class="prof-highlight"><strong>Treatment must be early.</strong></mark> &#9733; Dr. Webster: &ldquo;you have to
    treat it early if you want to have any chance whatsoever&rdquo;.</li>
  </ul>
  """ + fig(30, 1, "l17-s030-pam-treatment-medications.jpg",
      "The Medication and Route columns of a gray treatment table: amphotericin B intravenous, amphotericin B intrathecal, azithromycin intravenous or by mouth, dexamethasone intravenous, fluconazole intravenous or by mouth, miltefosine by mouth, rifampin intravenous or by mouth; a source line at the bottom.",
      "<b>&ldquo;Recommend treatment for primary amoebic meningoencephalitis caused by <em>Naegleria fowleri</em>&rdquo;</b> "
      "(slide 30, source: Centers for Disease Control and Prevention), cropped here to its medication and route "
      "columns; the doses and durations are on the slide and are not reproduced.", crop=(5, 135, 572, 1010)) + """
  <table>
    <tr><th>Medication (slide 30)</th><th>Route</th></tr>
    <tr><td>Amphotericin B</td><td>Intravenous</td></tr>
    <tr><td>Amphotericin B</td><td>Intrathecal</td></tr>
    <tr><td>Azithromycin</td><td>Intravenous or by mouth</td></tr>
    <tr><td>Dexamethasone</td><td>Intravenous</td></tr>
    <tr><td>Fluconazole</td><td>Intravenous or by mouth</td></tr>
    <tr><td>Miltefosine</td><td>By mouth</td></tr>
    <tr><td>Rifampin</td><td>Intravenous or by mouth</td></tr>
  </table>

  <h3 class="sub" id="par-acanth">17.5 &middot; Objective 1 &mdash; <em>Acanthamoeba</em>: keratitis and granulomatous amebic encephalitis</h3>
  <p><em>Acanthamoeba</em> species are <strong>distributed worldwide</strong> and <strong>found in freshwater lakes,
  hot tubs and swimming pools</strong> (slide 31); slide 13 lists them as free-living in water. Slide 31 separates
  two diseases:</p>
  <ul>
    <li><strong>Amebic keratitis</strong>: in <strong>contact lens wearers</strong>; <strong>eye pain, redness,
    irritation</strong>; <strong>does not typically disseminate</strong>.</li>
    <li><strong>Granulomatous amebic encephalitis</strong>: the ameba <strong>typically enters through a break in the
    skin or through the nasal passages</strong>; <strong>symptoms of meningitis, but a longer progression</strong>;
    <strong>survival rate only 2&ndash;3%</strong>.</li>
    <li><strong>Treatment</strong>: amphotericin B, rifampicin, trimethoprim-sulfamethoxazole, ketoconazole,
    fluconazole, sulfadiazine and albendazole are <strong>only tentatively successful</strong>.</li>
  </ul>
  <p>Her table (slide 4) compresses this into one row, &ldquo;Granulomatous Amebic Encephalitis, found in contact lens
  wearers&rdquo;; slide 31 keeps the contact lens with the keratitis (17.42).</p>
  """ + fig(32, 1, "l17-s032-acanthamoeba-life-cycle.jpg",
      "A Centers for Disease Control and Prevention life-cycle diagram for Acanthamoeba species: cysts and a spiky trophozoite in soil and water cycling through mitosis on the left; arrows into a box where amebae enter humans; arrows to the eye, through the nose to the lungs, and through broken skin; a human figure with brain and lungs; numbered footnotes at the bottom right.",
      "<b>The <em>Acanthamoeba</em> life cycle.</b> (1) <b>Cysts</b> and (2) <b>trophozoites</b> (the infective stage) "
      "live in soil and water and multiply by (3) mitosis. (4) <b>Amebae (cysts and trophozoites) can enter humans in "
      "various ways</b>: (5) <b>through the eye</b>, which <b>results in severe keratitis of the eye</b>; (6) "
      "<b>through the nasal passages to the lower respiratory tract</b>, which results in <b>granulomatous amebic "
      "encephalitis and/or disseminated disease in individuals with compromised immune systems</b>; (7) <b>through "
      "ulcerated or broken skin</b>, which results in granulomatous amebic encephalitis, disseminated disease or skin "
      "lesions in individuals with compromised immune systems. The diagnostic stage: <b>cysts and trophozoites in "
      "tissue</b>.", CDC) + """
  <h4 class="subsub">The two free-living amebas side by side</h4>
  <table>
    <tr><th></th><th><em>Naegleria fowleri</em> (slides 24&ndash;30)</th><th><em>Acanthamoeba</em> (slides 31&ndash;32)</th></tr>
    <tr><td>Where it lives</td><td>Standing water with a high bacterial count: hot springs, lakes and streams, unchlorinated pools; over 46% of Florida lakes</td><td>Worldwide: freshwater lakes, hot tubs, swimming pools; soil and water (slide 32)</td></tr>
    <tr><td>How it gets in</td><td><strong>Nasal contact with water</strong> (diving, waterskiing, jetskiing, sinus rinsing with tap water); trophozoite crosses the nasal mucosa and climbs the <strong>olfactory nerve</strong></td><td><strong>The eye</strong> (keratitis, contact lens wearers); <strong>a break in the skin or the nasal passages</strong> (encephalitis)</td></tr>
    <tr><td>Disease</td><td>Primary amebic meningoencephalitis, mostly children and young adults</td><td>Amebic keratitis; granulomatous amebic encephalitis and disseminated disease in compromised immune systems</td></tr>
    <tr><td>Course</td><td><strong>Rapid</strong>: death in 3&ndash;7 days; fatality more than 97%</td><td>Meningitis symptoms with a <strong>longer progression</strong>; survival only 2&ndash;3%</td></tr>
    <tr><td>Treatment</td><td>Must be early: amphotericin B (intravenous and intrathecal), azithromycin, dexamethasone, fluconazole, miltefosine, rifampin</td><td>Amphotericin B, rifampicin, trimethoprim-sulfamethoxazole, ketoconazole, fluconazole, sulfadiazine, albendazole: only tentatively successful</td></tr>
    <tr><td>Prevention</td><td>No swimming or diving in unchlorinated water; nose plugs</td><td>None given on the slides</td></tr>
  </table>

  <h3 class="sub" id="par-balantidium">17.6 &middot; Objective 1 &mdash; <em>Balantidium coli</em>, the intestinal ciliate</h3>
  <ul>
    <li><strong>An occupant of the intestines of domestic animals such as pigs and cattle</strong> (slide 13:
    &ldquo;zoonotic in pigs&rdquo;; her table: pigs and cattle as alternate hosts).</li>
    <li><strong>Acquired by ingesting cyst-containing food or water.</strong></li>
    <li>The <strong>trophozoite erodes the intestine</strong> and elicits intestinal symptoms: <strong>persistent
    diarrhea, occasionally dysentery, abdominal pain and weight loss</strong>. The disease is
    <strong>balantidiosis</strong>.</li>
    <li><strong>Healthy humans are resistant.</strong> It <strong>rarely penetrates the intestine or enters the
    blood</strong>.</li>
    <li><strong>Treatment</strong>: tetracycline, iodoquinol, nitrimidazine or metronidazole.</li>
    <li>The slides give no diagnostic test or prevention for <em>Balantidium</em>; slide 34 shows what it looks like
    under the microscope.</li>
  </ul>
  """ + fig(34, 1, "l17-s034-balantidium-drawing.jpg",
      "Drawings of an oval trophozoite fringed with cilia, containing many round vacuoles, a purple kidney-shaped macronucleus with a small micronucleus, and a funnel-shaped mouth; beside it a round mature cyst with a thick wall and a purple macronucleus.",
      "<b>Microscopic views of <em>Balantidium coli</em></b>: the <b>trophozoite</b> (macronucleus, micronucleus, "
      "vacuoles, cytostome, <b>cilia tufts</b>) and the <b>mature cyst</b> (cyst wall, macronucleus, vacuoles). The "
      "cilia make it the lecture&rsquo;s one ciliate.", MH, crop=(0, 16, 800, 408)) + """
  """ + fig(34, 2, "l17-s034-balantidium-trophozoite.jpg",
      "A micrograph of a large oval brownish cell with a granular interior and a fine fringe of hairs around its edge, on a speckled tan background.",
      "<b><em>Balantidium coli</em></b> under the microscope: a large oval cell with a <b>fringe of cilia</b> around its "
      "edge (unlabeled on the slide; compare the drawing above).") + """
  """ + fig(34, 3, "l17-s034-balantidium-cyst.jpg",
      "A micrograph of a round, pink-stained cell with a dark bean-shaped body in the center and pointers labeled cyst wall, oral apparatus of encysted troph, and macronucleus.",
      "<b>A <em>Balantidium coli</em> cyst</b>: the <b>cyst wall</b>, the oral apparatus of the encysted trophozoite, "
      "and the dark, bean-shaped <b>macronucleus</b>.") + """

  <h3 class="sub" id="par-trichomonas">17.7 &middot; Objective 1 &mdash; <em>Trichomonas vaginalis</em> and trichomoniasis</h3>
  <p>Slide 35 opens <strong>the flagellates</strong>: <em>Trichomonas</em>, <em>Giardia</em> (17.8) and the
  hemoflagellates (17.9&ndash;17.12).</p>
  <h4 class="subsub">Morphology (slide 36)</h4>
  <ul>
    <li>Trichomonads are <strong>small and pear-shaped</strong>, with <strong>4 anterior flagella and an undulating
    membrane</strong>.</li>
    <li>They <strong>exist only in the trophozoite form: no cyst</strong>.</li>
    <li><strong>Three infect humans</strong>: <em>T. vaginalis</em>, <em>T. tenax</em> and <em>T. hominis</em>.</li>
  </ul>
  """ + fig(36, 1, "l17-s036-trichomonas-drawing.jpg",
      "Three drawings of purple pear-shaped cells labeled (a), (b) and (c); the first is labeled with Flagella at the front, a dark Nucleus, a ruffled Undulating membrane along one side, and a rod, the Axostyle, running to a tail.",
      "<b>Trichomonads</b>: look for the <b>flagella</b> at the front, the <b>undulating membrane</b> along the side, "
      "the <b>nucleus</b> and the <b>axostyle</b> running through the cell.") + """
  <h4 class="subsub">Where it lives and how people acquire it</h4>
  <ul>
    <li>The <strong>reservoir is the human urogenital tract</strong> (slide 13: &ldquo;human&rdquo;).</li>
    <li>It is a <strong>strict parasite and cannot survive long outside the host</strong>: it is
    <strong>sexually transmitted</strong>. <em>Trichomonas vaginalis</em> <strong>causes the sexually transmitted
    disease trichomoniasis</strong>, the <strong>most common curable sexually transmitted disease in young, sexually
    active women</strong>. &#9733; Dr. Webster: &ldquo;one that I can almost guarantee that you will encounter in your
    clinical practice&rdquo;.</li>
    <li>7.4&ndash;8 million cases a year in North America, 124 million worldwide. <strong>60&ndash;70% of the infected are
    asymptomatic.</strong></li>
  </ul>
  <h4 class="subsub">Disease (slides 37&ndash;38)</h4>
  <table>
    <tr><th>Women</th><th>Men</th></tr>
    <tr><td><strong>Foul-smelling, green-to-yellow discharge</strong>; vulvitis; cervicitis; <strong>urinary frequency and pain</strong></td><td><strong>Urethritis</strong>; a <strong>thin, milky discharge</strong>; occasionally prostate infection</td></tr>
  </table>
  <ul>
    <li><strong>Incubation period</strong>: 4&ndash;28 days.</li>
    <li>It <strong>may predispose to other sexually transmitted diseases</strong>, <strong>raises cervical cancer risk
    2&ndash;3 times</strong>, and <strong>increases human immunodeficiency virus transmission by 50%</strong>.</li>
  </ul>
  <h4 class="subsub">Diagnosis and treatment (slide 38)</h4>
  <ul>
    <li><strong>Diagnosis by microscopic analysis of a vaginal smear.</strong></li>
    <li><strong>Treatment: metronidazole and tinidazole</strong>; <strong>4.3% of <em>Trichomonas</em> are resistant</strong>
    to the antimicrobials.</li>
  </ul>
  """ + fig(38, 1, "l17-s038-trichomonas-smear.jpg",
      "A micrograph on a pale green background of two purple pear-shaped cells, each with a dark nucleus and thin trailing flagella.",
      "<b><em>Trichomonas vaginalis</em></b> in a stained smear: <b>pear-shaped</b> trophozoites with a dark nucleus and "
      "flagella (the same picture is in her table on slide 4).") + """

  <h3 class="sub" id="par-giardia">17.8 &middot; Objective 1 &mdash; <em>Giardia lamblia</em> and giardiasis</h3>
  <h4 class="subsub">Morphology (slide 39)</h4>
  <ul>
    <li>A <strong>pathogenic flagellate</strong> with a <strong>unique symmetrical heart shape</strong> and a
    <strong>concave ventral surface that acts like a suction cup</strong>.</li>
    <li><strong>Cysts are small, compact and multinucleate.</strong></li>
  </ul>
  """ + fig(40, 1, "l17-s040-giardia-drawing.jpg",
      "Drawings of a pear-shaped trophozoite seen from the front with two nuclei like eyes and several pairs of flagella, the same cell seen from the side showing a hollow ventral depression, and an oval cyst with four nuclei.",
      "<b>Identification of trophozoites</b> (slide 40&rsquo;s title): the <em>Giardia</em> <b>trophozoite</b> with its "
      "<b>two nuclei</b> and, in side view, the <b>ventral depression</b> (the suction cup); the oval <b>cyst</b> with "
      "<b>several nuclei</b>.", MH) + """
  """ + fig(40, 2, "l17-s040-giardia-trophozoite-smear.jpg",
      "A stained smear on a blue-green and purple speckled background with a single small pear-shaped gray cell in the center.",
      "<b>A <em>Giardia</em> trophozoite</b> in a stained smear: the pear (heart) shape (unlabeled on the slide).") + """
  """ + fig(40, 3, "l17-s040-giardia-cysts-smear.jpg",
      "A stained smear showing two oval purple bodies with clear outlines and internal markings, among pink and blue debris.",
      "<b><em>Giardia</em> cysts</b> in a stained smear: small, compact, oval, with several nuclei inside (unlabeled on "
      "the slide; the same picture is in her table on slide 4).") + """
  <h4 class="subsub">Reservoirs and how people acquire it</h4>
  <ul>
    <li><strong>Reservoirs include beavers, cattle, coyotes, cats and humans</strong> (slide 13: zoonotic, water and
    food).</li>
    <li><strong>Cysts can survive for 2 months in the environment.</strong></li>
    <li><strong>Usually ingested with water and food</strong>; the <strong>infectious dose is 10 to 100 cysts</strong>.
    Her table: <mark class="prof-highlight"><strong>common in campers</strong></mark>. &#9733; Dr. Webster: &ldquo;this is the
    one that you will get going camping&rdquo;.</li>
  </ul>
  <h4 class="subsub">Disease, diagnosis, treatment, prevention (slide 41)</h4>
  <ul>
    <li><strong>Cysts enter the duodenum, germinate, and travel to the jejunum to feed and multiply.</strong></li>
    <li>Giardiasis: <strong>diarrhea, abdominal pain</strong>.</li>
    <li><strong>Diagnosis</strong>: microscopic diagnosis is <strong>difficult because the organism is shed in feces
    intermittently</strong>; <strong>polymerase chain reaction</strong> analysis.</li>
    <li><strong>Treatment</strong>: <strong>quinacrine or metronidazole</strong>, or <strong>nitazoxanide in
    children</strong>.</li>
    <li>The agent is <strong>killed by boiling, ozone and iodine</strong>.</li>
  </ul>

  <h3 class="sub" id="par-hemoflag">17.9 &middot; Objective 1 &mdash; The hemoflagellates and their stages</h3>
  <p><strong>Hemoflagellates are vector-borne blood parasites</strong> (slide 42):</p>
  <ul>
    <li><strong>Obligate parasites that live in the blood and tissues</strong> of the human host.</li>
    <li>They cause <strong>life-threatening and debilitating zoonoses</strong>.</li>
    <li>They are <strong>spread in specific tropical regions by blood-sucking insects that serve as intermediate
    hosts</strong>.</li>
    <li>They have <strong>complicated life cycles and undergo morphological changes</strong>, and are
    <strong>categorized according to their cellular and infective stages</strong>.</li>
  </ul>
  <table>
    <tr><th>Stage</th><th>Slide 42&rsquo;s definition</th></tr>
    <tr><td><strong>Amastigote</strong></td><td>The form <strong>lacking a free flagellum</strong></td></tr>
    <tr><td><strong>Promastigote</strong></td><td>The stage bearing a <strong>single, free, anterior flagellum</strong></td></tr>
    <tr><td><strong>Epimastigote</strong></td><td>The flagellate stage</td></tr>
    <tr><td><strong>Trypomastigote</strong></td><td>The <strong>large, fully formed stage</strong></td></tr>
  </table>
  """ + fig(43, 1, "l17-s043-hemoflagellate-stages-table.jpg",
      "A textbook table titled Cellular and Infective Stages of the Hemoflagellates, with small drawings of a round amastigote, a slender promastigote with a front flagellum, an epimastigote and a wavy trypomastigote above the columns, and rows for Leishmania, Trypanosoma brucei and Trypanosoma cruzi.",
      "<b>Cellular and infective stages of the hemoflagellates.</b> Read across each row for the stage marked "
      "<b>infective to humans</b>: the <b>promastigote</b> for <em>Leishmania</em>, the <b>trypomastigote</b> for "
      "both trypanosomes.") + """
  <table>
    <tr><th>Genus/Species</th><th>Amastigote</th><th>Promastigote</th><th>Epimastigote</th><th>Trypomastigote</th></tr>
    <tr><td><em>Leishmania</em></td><td>Intracellular in human macrophages</td><td>Found in sand fly gut; <strong>infective to humans</strong></td><td>Does not occur</td><td>Does not occur</td></tr>
    <tr><td><em>Trypanosoma brucei</em></td><td>Does not occur</td><td>Does not occur</td><td>Present in salivary gland of tsetse fly</td><td>In biting mouthparts of tsetse fly; <strong>infective to humans</strong></td></tr>
    <tr><td><em>Trypanosoma cruzi</em></td><td>Intracellular in human macrophages, liver, heart, spleen</td><td>Occurs</td><td>Present in gut of reduviid (kissing) bug</td><td>In feces of reduviid bug; <strong>transferred to humans</strong></td></tr>
  </table>

  <h3 class="sub" id="par-tbrucei">17.10 &middot; Objective 1 &mdash; <em>Trypanosoma brucei</em> and African sleeping sickness</h3>
  <p><strong><em>Trypanosoma</em> species are distinguished by their infective stage</strong>: the
  <strong>trypomastigote</strong>, an <strong>elongate, spindle-shaped cell with tapered ends and eel-like
  motility</strong>. There are <strong>two types of trypanosomiasis</strong> (slide 44): <em>T. brucei</em>,
  <strong>African sleeping sickness</strong>; and <em>T. cruzi</em>, <strong>Chagas disease</strong>, endemic to Central
  and South America (17.11).</p>
  <h4 class="subsub">Vector, reservoir and the two subspecies (slide 45)</h4>
  <ul>
    <li><strong>Spread by tsetse flies</strong>; <strong>harbored by reservoir mammals</strong>.</li>
    <li><strong>Two variants of disease, caused by two subspecies</strong>:</li>
  </ul>
  <table>
    <tr><th></th><th><em>T. b. gambiense</em></th><th><em>T. b. rhodesiense</em></th></tr>
    <tr><td>Strain</td><td>Gambian strain</td><td>Rhodesian strain</td></tr>
    <tr><td>Where</td><td><strong>West Africa</strong></td><td><strong>East Africa</strong></td></tr>
    <tr><td>Course (slide 46)</td><td><strong>Chronic</strong>, with brain symptoms <strong>years later</strong></td><td><strong>Acute</strong>, with brain symptoms <strong>within 3&ndash;4 weeks</strong></td></tr>
  </table>
  """ + fig(45, 1, "l17-s045-african-trypanosomiasis.jpg",
      "Top, a map of Africa with blue zones across West and central Africa and purple zones in East Africa; middle, a circle of blood with wavy blue trypanosomes among red cells, flanked by two tsetse flies; bottom, a woman's head with the brain exposed, and arrows looping between the flies, the blood and the brain.",
      "<b>African trypanosomiasis.</b> (a) The distribution: <b><em>T. b. gambiense</em></b> (blue) across West and "
      "central Africa, <b><em>T. b. rhodesiense</em></b> (purple) in East Africa. (b) <b>The saliva of a fly infected "
      "with <em>T. brucei</em> inoculates the human bloodstream</b>; the parasite matures and invades various organs, "
      "and in time its cumulative effects cause <b>central nervous system damage</b>. (c) The trypanosome is spread to "
      "other hosts through <b>another fly</b>, in whose alimentary tract the parasite completes a series of "
      "developmental stages. Look for the &ldquo;interval of years&rdquo; arrow.") + """
  <h4 class="subsub">How people acquire it, and the disease (slides 46&ndash;47)</h4>
  <ul>
    <li><strong>The biting fly inoculates the skin with trypomastigotes</strong>, which develops a <strong>primary
    chancre</strong>.</li>
    <li>The organism <strong>migrates into the lymphatics and disseminates in the blood</strong>.</li>
    <li>It <strong>evades the immune response by antigenic variation: over 100 different antigens</strong>.</li>
    <li>It <strong>multiplies in the blood and damages the spleen, lymph nodes and brain</strong>.</li>
    <li><strong>Early symptoms</strong>: <strong>fever, enlarged spleen, swollen lymph nodes and joint
    pain</strong>.</li>
    <li>As it <strong>moves to the central nervous system</strong>: <strong>personality and behavioral
    changes</strong>, then <strong>sleep disturbances, tremors, seizures, paralysis and coma</strong>.</li>
  </ul>
  """ + fig(46, 1, "l17-s046-trypanosomes-blood-smear.jpg",
      "A pink blood smear of round red cells with several thin, wavy, dark purple organisms between them.",
      "<b>Trypanosomes in blood</b>: slender, wavy flagellates <b>between</b> the red blood cells (her table&rsquo;s "
      "caption: &ldquo;blood smear with flagellates swimming between cells&rdquo;). &#9733; Dr. Webster: &ldquo;It would not "
      "be a bad thing for you to remember this lovely picture.&rdquo; She will not ask you to tell <em>T. cruzi</em> "
      "from <em>T. brucei</em> by the picture: &ldquo;as long as you knew trypanosoma&rdquo;.") + """
  <h4 class="subsub">Diagnosis, treatment and control (slide 47)</h4>
  <ul>
    <li><strong>Trypanosomes are readily demonstrated in blood, spinal fluid or lymph nodes.</strong></li>
    <li>The <strong>card agglutination test for trypanosomes</strong> gives a <strong>rapid diagnosis</strong>.</li>
    <li><mark class="prof-highlight"><strong>Treatment before neurological involvement</strong></mark>: <strong>melarsoprol, suramin,
    eflornithine</strong> (Table 23.2 adds pentamidine; suramin is available in the United States only from the
    Centers for Disease Control and Prevention).</li>
    <li><mark class="prof-highlight"><strong>Control involves eliminating the tsetse fly.</strong></mark> &#9733; Dr. Webster:
    &ldquo;vector control is one of the best ways of controlling these hemoflagellate diseases&rdquo;.</li>
  </ul>

  <h3 class="sub" id="par-tcruzi">17.11 &middot; Objective 1 &mdash; <em>Trypanosoma cruzi</em> and Chagas disease</h3>
  """ + fig(48, 1, "l17-s048-t-cruzi-smear.jpg",
      "A tiny micrograph of pale red cells with one curved purple organism among them.",
      "<b><em>Trypanosoma cruzi</em></b> in blood, the small picture beside slide 48&rsquo;s title: one curved "
      "trypomastigote among the red cells.") + """
  <ul>
    <li><em>T. cruzi</em> <strong>causes Chagas disease, or American trypanosomiasis</strong>.</li>
    <li><strong>Millions of cases in Latin America</strong>, but it is becoming more of an issue in the <strong>Southern
    United States</strong>: <mark class="prof-highlight"><strong>vector migration</strong></mark> &#9733; Starred on the
    slide. Dr. Webster: it is the one &ldquo;you are more likely to see in your clinical work&rdquo;, &ldquo;because of
    the migration of the vector. It&rsquo;s coming further north as things get warmer.&rdquo; Her table says the same: it &ldquo;was a tropical disorder but it is becoming an issue in Southern [United States] as vector
    expands its range&rdquo;.</li>
    <li>The National Institutes of Health estimates <strong>300,000 infected in the United States</strong>, including
    57,000 cardiomyopathy patients and 43,000 women of reproductive age, with up to 108 congenital infections per
    year.</li>
    <li>It is <strong>now considered by many to be endemic in the United States</strong>.</li>
  </ul>
  """ + fig(50, 1, "l17-s050-chagas-us-states-map.jpg",
      "A map titled States With Cases Of Chagas Disease: the southern half of the United States in shades of blue, Arkansas in purple, a band of states from Nevada and Utah to Pennsylvania in pink, and the northern states gray.",
      "<b>States with cases of Chagas disease</b> (source printed on the map: the Centers for Disease Control and "
      "Prevention). The legend: dark blue, <b>reported triatomines and autochthonous animal cases</b>; light blue, "
      "triatomines, autochthonous animal cases <b>and autochthonous human cases</b> (California, Arizona, Texas, "
      "Louisiana, Tennessee, Missouri among them); purple, triatomines and autochthonous human cases; pink, "
      "<b>reported triatomines</b> only. Look at how far north the pink reaches: the starred vector migration.") + """
  <h4 class="subsub">The vector and how people acquire it (slide 49)</h4>
  <ul>
    <li>The <strong>reduviid bug (kissing bug) is the vector</strong>.</li>
    <li><strong>Infection occurs when bug feces is inoculated into a cutaneous portal.</strong></li>
    <li>It <strong>may also be transmitted congenitally, through transfusions, organ transplants, or by ingestion of
    foodstuffs contaminated by triatomine urine or feces</strong>; the slide adds, in parentheses, that <strong>this
    manner of transmission typically results in more severe cases and higher mortality</strong>.</li>
  </ul>
  """ + fig(50, 2, "l17-s050-chagas-cycle-and-map.jpg",
      "A cycle diagram with a kitten, reduviid bugs, a human figure with an inset of a bug biting near the lips, an opossum and an armadillo; an inset of a wavy pink T. cruzi cell; a map of Central and South America with green patches; and a photograph of a brown bug feeding on skin.",
      "<b>American trypanosomiasis (Chagas disease).</b> Two cycles share the <b>reduviid bugs</b>: a <b>cycle in "
      "human habitats</b> (a cat, the bug, the <b>bite of the bug</b> on the face) and a <b>cycle in wild animals</b> "
      "(opossum, armadillo). Inset: the <b><em>T. cruzi</em> cell</b>. Green on the map marks the Latin American "
      "range; the photograph is the bug feeding.") + """
  <h4 class="subsub">Disease (slides 49 and 51)</h4>
  <ul>
    <li>A <strong>local lesion: Roma&ntilde;a&rsquo;s sign</strong>, also called a <strong>chagoma</strong>, a
    <strong>swelling of the eyelid with conjunctivitis</strong>; with fever and swelling of the lymph nodes, spleen and
    liver.</li>
    <li>The <strong>heart muscle and large intestine harbor masses of amastigotes</strong>.</li>
    <li><strong>Chronic inflammation</strong> occurs in the organs, <strong>especially the heart and brain</strong>;
    Chagas accounts for <strong>30&ndash;40% of heart disease in endemic regions</strong>.</li>
  </ul>
  """ + fig(51, 1, "l17-s051-chagas-conditions.jpg",
      "Three pictures: (a) a girl's face with one eyelid swollen nearly shut; (b) a whole heart on a black background; (c) a pink tissue section of muscle fibers with pointers to clustered dots labeled Amastigotes and to the fibers labeled Cardiac muscle fibers.",
      "<b>Conditions associated with Chagas disease.</b> (a) <b>Roma&ntilde;a&rsquo;s sign</b>, the swollen eyelid; (b) "
      "a heart (the slide&rsquo;s text: chronic inflammation, especially of the heart); (c) <b>amastigotes in cardiac "
      "muscle</b>, the clusters among the cardiac muscle fibers.") + """
  <h4 class="subsub">Treatment and control</h4>
  <ul>
    <li><strong>Treatment: nifurtimox and benznidazole</strong> (spelled &ldquo;benzonidazole&rdquo; on the slides),
    which <mark class="prof-highlight"><strong>must be administered early</strong></mark>.</li>
    <li><mark class="prof-highlight"><strong>Control is through control of the vector</strong></mark> (&#9733; Dr. Webster:
    &ldquo;once again, vector control is the best way to control this particular organism&rdquo;); a <strong>vaccine is under development</strong>
    (slide 51).</li>
    <li>Diagnosis: the slides give no test; slide 43 places the trypomastigote in the bug&rsquo;s feces and the
    amastigote inside human macrophages, liver, heart and spleen.</li>
  </ul>
  <h4 class="subsub">The two trypanosomes side by side</h4>
  <table>
    <tr><th></th><th><em>Trypanosoma brucei</em></th><th><em>Trypanosoma cruzi</em></th></tr>
    <tr><td>Disease</td><td>African sleeping sickness</td><td>Chagas disease (American trypanosomiasis)</td></tr>
    <tr><td>Where</td><td>Africa: <em>gambiense</em> West, <em>rhodesiense</em> East</td><td>Central and South America; spreading into the Southern United States (vector migration)</td></tr>
    <tr><td>Vector</td><td><strong>Tsetse fly</strong></td><td><strong>Reduviid (kissing) bug</strong></td></tr>
    <tr><td>How it enters</td><td>Fly&rsquo;s <strong>bite</strong> inoculates trypomastigotes (saliva); primary chancre</td><td>Bug&rsquo;s <strong>feces</strong> inoculated into a cutaneous portal; also congenital, transfusion, transplant, contaminated food</td></tr>
    <tr><td>Target</td><td>Blood, lymph nodes, spleen, then <strong>brain</strong> (sleep disturbances, coma)</td><td><strong>Heart</strong> muscle and large intestine (amastigotes); heart and brain inflammation</td></tr>
    <tr><td>Sign to know</td><td>Primary chancre; antigenic variation</td><td><strong>Roma&ntilde;a&rsquo;s sign</strong> (chagoma)</td></tr>
    <tr><td>Treatment</td><td>Melarsoprol, suramin, eflornithine (pentamidine in Table 23.2)</td><td>Nifurtimox, benznidazole: early</td></tr>
    <tr><td>Control</td><td>Eliminate the tsetse fly</td><td>Control the vector; vaccine under development</td></tr>
  </table>

  <h3 class="sub" id="par-leish">17.12 &middot; Objective 1 &mdash; <em>Leishmania</em> and leishmaniasis</h3>
  <ul>
    <li><strong>Leishmaniasis is a zoonosis transmitted among mammalian hosts by female sand flies that require a
    blood meal to produce eggs.</strong></li>
    <li><strong>Endemic to equatorial regions</strong>; the <strong>alternate hosts are dogs</strong> (her table: dog
    alternate host, sand fly is vector).</li>
    <li>98 countries affected, a global prevalence of 12 million cases and 2&ndash;2.5 million new cases a year.</li>
    <li>Species named on slide 13: <em>Leishmania donovani</em>, <em>L. tropica</em>, <em>L. brasiliensis</em>.</li>
  </ul>
  <h4 class="subsub">How people acquire it (slide 52)</h4>
  <p><strong>Promastigotes are injected with the sand fly bite</strong>, <strong>convert to amastigotes and
  multiply</strong>. <strong>If the macrophage does not migrate, the infection is localized; it is systemic if the
  macrophage migrates.</strong></p>
  """ + fig(54, 2, "l17-s054-leishmania-life-cycle.jpg",
      "A circular life cycle: a boy with a black dog at the top labeled Human, other mammalian host; at right a macrophage packed with small round bodies beside red blood cells; at the bottom a sand fly; at left slender flagellated cells in the gut of the sand fly.",
      "<b>Life cycle and pathology of <em>Leishmania</em> species.</b> The <b>human or other mammalian host</b> (the "
      "dog) carries <b>free and intracellular amastigotes in a macrophage</b>; the <b>sand fly</b> takes them up; "
      "<b>promastigote stages in the gut of the sand fly</b> are injected at the next bite.") + """
  <h4 class="subsub">The three forms of disease (slide 53)</h4>
  <table>
    <tr><th>Form</th><th>What the slide says</th></tr>
    <tr><td><strong>Cutaneous</strong>: oriental sore, <strong>Baghdad boil</strong></td><td>A <strong>localized ulcerated sore</strong></td></tr>
    <tr><td><strong>Espundia</strong></td><td><strong>Skin and mucous membrane infection of the head</strong>; a chronic infection which <strong>occurs after cutaneous</strong> disease</td></tr>
    <tr><td><strong>Systemic (visceral)</strong></td><td><strong>High intermittent fever</strong>; weight loss; <strong>enlarged spleen, liver and lymph nodes</strong>. <strong>Kala azar is the most severe form, and fatal if untreated</strong></td></tr>
  </table>
  """ + fig(54, 1, "l17-s054-baghdad-boil.jpg",
      "A small photograph of a man's face with a red sore on the cheek.",
      "<b>Baghdad boil</b>: the localized ulcerated sore of cutaneous leishmaniasis.") + """
  """ + fig(54, 3, "l17-s054-espundia.jpg",
      "A small photograph of a seated person whose face and body are covered with crusted, scarred lesions.",
      "<b>Espundia</b>: skin and mucous membrane infection of the head, after the cutaneous form.") + """
  <ul>
    <li><strong>Treatment</strong>: <strong>pentavalent antimony, pentamidine, amphotericin B</strong>.</li>
    <li><strong>Co-infection of leishmaniasis and malaria</strong> is an increasing issue and <strong>may make diagnosis
    difficult</strong>.</li>
  </ul>

  <h3 class="sub" id="par-plasmodium">17.13 &middot; Objective 1 &mdash; <em>Plasmodium</em> and malaria</h3>
  <h4 class="subsub">The apicomplexan parasites (slide 55)</h4>
  <ul>
    <li><strong>Sporozoans</strong> that <strong>lack locomotor organelles in the trophozoite state</strong>.</li>
    <li>They <strong>alternate between sexual and asexual phases and between different animal hosts</strong>.</li>
    <li>Most form <strong>specialized infective bodies</strong> that are transmitted by <strong>arthropod vectors, food,
    water or other means</strong>: <em>Plasmodium</em>, <em>Toxoplasma</em>, <em>Cryptosporidium</em>.</li>
  </ul>
  <h4 class="subsub"><em>Plasmodium</em>, the agent of malaria (slides 56&ndash;57)</h4>
  <ul>
    <li>Malaria is the <strong>dominant protozoan disease</strong>: it <strong>threatens 40% of the world&rsquo;s
    population</strong> each year.</li>
    <li><em>Plasmodium</em> is an <strong>obligate intracellular sporozoan</strong>.</li>
    <li><strong>Four species</strong> (slide 56): <em>P. malariae</em>, <em>P. vivax</em>, <em>P. falciparum</em> and
    <em>P. ovale</em> (slide 13 lists only the first three; 17.42).</li>
    <li><strong>The female <em>Anopheles</em> mosquito is the primary vector</strong>; malaria also spreads by
    <strong>blood transfusions</strong> and <strong>mother to fetus</strong>.</li>
    <li>300&ndash;500 million new cases each year (<strong>90% in Africa</strong>); 2 million deaths each year;
    1,000&ndash;2,000 cases a year in the United States.</li>
  </ul>
  """ + fig(57, 1, "l17-s057-malaria-belt.jpg",
      "A world map with a pink key labeled Distribution of Malaria; pink covers Central America, northern South America, most of Africa south of the Sahara, the Arabian Peninsula, South Asia and Southeast Asia.",
      "<b>The malaria belt</b>: pink marks the distribution of malaria, a band across the tropics of the Americas, "
      "<b>Africa</b> and southern Asia.") + """
  <h4 class="subsub">Life cycle: two distinct phases (slides 58&ndash;59)</h4>
  <table>
    <tr><th>Phase</th><th>Where</th><th>What happens</th></tr>
    <tr><td rowspan="3"><strong>Asexual phase</strong></td><td rowspan="3"><strong>Human host</strong></td><td><strong>Exoerythrocytic phase</strong>: the infected female mosquito <strong>injects the asexual sporozoite, which localizes in the liver</strong>; it undergoes <strong>schizogony</strong>, generating numerous <strong>merozoites</strong> that enter the circulation in <strong>5&ndash;16 days</strong>, depending on the species</td></tr>
    <tr><td><strong>Erythrocytic phase</strong>: <strong>merozoites attach to and enter red blood cells</strong>, convert to <strong>circular ring trophozoites</strong> and multiply; the <strong>red cell bursts, releasing merozoites</strong></td></tr>
    <tr><td><strong>Gametocytic phase</strong>: merozoites differentiate into gametes, which are now in the blood of the human host</td></tr>
    <tr><td><strong>Sexual phase</strong></td><td><strong>Female <em>Anopheles</em> mosquito</strong></td><td>The mosquito draws infected red blood cells; <strong>gametes fertilize, forming a diploid cell, which forms sporozoites in the stomach</strong>; the <strong>sporozoites lodge in the salivary glands</strong>, available to infect a human host</td></tr>
  </table>
  """ + fig(59, 1, "l17-s059-plasmodium-life-cycle.jpg",
      "A large diagram of a human silhouette with heart, liver and blood vessels, five numbered panels: a mosquito injecting sporozoites into a capillary, liver cells filling with merozoites, red blood cells with ring trophozoites bursting, red cells with gametocytes, and a mosquito feeding on blood.",
      "<b>The <em>Plasmodium</em> life cycle.</b> (1) <b>Asexual phase</b>: sporozoites enter a capillary with the "
      "saliva of a feeding mosquito. (2) <b>Exoerythrocytic phase</b>: sporozoites invade the cells of the "
      "<b>liver</b>, divide, and release large numbers of <b>merozoites</b>. (3) <b>Erythrocytic phase</b>: merozoites "
      "invade red blood cells; the prominent <b>ring trophozoite</b> forms, and schizogony produces more merozoites "
      "that burst out (look for the <b>Symptoms</b> arrow at the burst) and continue the cycle. (4) <b>Gametocyte "
      "phase</b>: some red cells give rise to male and female <b>gametocytes</b>, which infect another mosquito when it "
      "feeds. (5) <b>Sexual phase</b>: final development in the mosquito produces the infectious sporozoite.") + """
  <h4 class="subsub">Disease and diagnosis (slide 60)</h4>
  <ul>
    <li><strong>10&ndash;16 day incubation period.</strong></li>
    <li><strong>Malaise, fatigue, aches, nausea</strong>, then <strong>regular episodes of
    chills-fever-sweating</strong>.</li>
    <li><strong>Symptoms occur at 48&ndash;72 hour intervals as red blood cells rupture</strong>; the interval depends on
    the species.</li>
    <li><strong>Complications</strong>: <strong>anemia</strong>, and organ enlargement of the <strong>spleen, liver and
    kidneys</strong>.</li>
    <li><strong><em>P. falciparum</em> is the most malignant type</strong>, with the <strong>highest death rate in
    children</strong>.</li>
    <li><strong>Diagnosis by the presence of trophozoites in red blood cells</strong>, and by symptoms.</li>
  </ul>
  """ + fig(60, 1, "l17-s060-ring-trophozoites.jpg",
      "A micrograph of closely packed tan red blood cells, many containing a small dark ring with a dot, with pointers labeled Ring trophozoites and Red blood cell.",
      "<b>Ring trophozoites</b> inside <b>red blood cells</b>: the small rings are how malaria is diagnosed on a smear "
      "(her table: &ldquo;<em>Plasmodium</em> organism shown as ring form inside erythrocytes&rdquo;).") + """
  <h4 class="subsub">Resistance, treatment and prevention (slides 61&ndash;62)</h4>
  <ul>
    <li><strong>Some populations are naturally resistant: sickle cell trait.</strong></li>
    <li><strong>Increasing drug resistance.</strong></li>
    <li><strong>Most therapy is based on quinine</strong>, which <strong>prevents the parasite from processing hemoglobin
    in its food vacuoles</strong>.</li>
    <li><strong>Therapy is chloroquine, mefloquine, artemether</strong> (sometimes in combination).</li>
    <li><mark class="prof-highlight"><strong>Mosquito control is key.</strong></mark> &#9733; Dr. Webster: &ldquo;once again,
    vector control is what they do&rdquo;.</li>
    <li>United States cases: 2022, 1,620 (Florida 48); 2023, 2,120 (Florida 58, with <mark class="prof-highlight"><strong>8 non-travel cases of malaria
    in Florida</strong></mark>); 2024, 1,576 (Florida 57). &#9733; Dr. Webster: locally acquired cases in Florida, with no
    travel, &ldquo;so that&rsquo;s why you might see this one&rdquo;.</li>
    <li>A <strong>vaccine has just been approved by the World Health Organization for children</strong>. Its challenges:
    a complex regimen (3 doses before the rainy season, then booster doses before later rainy seasons); getting the
    vaccine to the areas; cost of vaccine and distribution, $325 million a year; and <strong>only about 30%
    effectiveness</strong>.</li>
  </ul>

  <h3 class="sub" id="par-toxo">17.14 &middot; Objective 1 &mdash; <em>Toxoplasma gondii</em> and toxoplasmosis</h3>
  <h4 class="subsub">The coccidian parasites (slide 63)</h4>
  <p>Coccidians are <strong>zoonotic in domestic animals and birds</strong> and <strong>exist in stages including dormant
  oocysts and pseudocysts</strong>. The examples: <em>Toxoplasma</em> (this section), <em>Sarcocystis</em> (17.15),
  <em>Cryptosporidium</em> (17.16), <em>Isospora</em> (17.17), <em>Cyclospora</em> (17.18) and <em>Babesia</em>
  (17.19); the end of 17.19 sets them side by side.</p>
  <h4 class="subsub">The organism and how people acquire it (slides 64&ndash;65)</h4>
  <ul>
    <li>An <strong>intracellular apicomplexan parasite</strong> with an extensive distribution, <strong>capable of
    infecting virtually all warm-blooded animals</strong>.</li>
    <li>Seroprevalence indicates that <strong>approximately one third of the human population worldwide has been
    exposed</strong>.</li>
    <li>It <strong>lives naturally in cats</strong>, which <strong>harbor oocysts in the gastrointestinal tract, released
    through feces</strong>; slide 70 calls the cat the <strong>feline definitive host</strong>.</li>
    <li><strong>Acquired by ingesting raw meats or substances contaminated by cat feces.</strong></li>
    <li><strong>Transplacental transmission to the fetus</strong> when a pregnant woman has toxoplasmosis:
    <strong>33% chance of transmission</strong>. Her table: <mark class="prof-highlight"><strong>pregnant women should not clean the cat box</strong></mark>
    because of the danger of transplacental transmission. &#9733; Dr. Webster: &ldquo;if you are with a patient who is
    pregnant and she has a cat, you tell her, get somebody else to clean the litter box&rdquo;.</li>
  </ul>
  """ + fig(66, 1, "l17-s066-toxoplasma-life-cycle.jpg",
      "A two-part diagram: (a) a kitten with a pseudocyst of tachyzoites, an arrow labeled Sexual phase to a circle showing sporogeny in feces and oocysts, and a mouse with a pseudocyst returning to the kitten; (b) oocysts in the environment passing to a cow, sheep and chicken, a pseudocyst in muscle, and arrows to a pregnant woman.",
      "<b>The life cycle and morphological forms of <em>Toxoplasma gondii</em>.</b> (a) In the <b>cat</b>: pseudocysts "
      "of <b>tachyzoites</b>, the <b>sexual phase</b>, &ldquo;sporogeny in feces&rdquo; and <b>oocysts</b>; a mouse "
      "with a pseudocyst carries it back to the cat. (b) <b>Oocysts in the environment</b> pass to cattle, sheep and "
      "chickens, whose meat holds <b>pseudocysts</b>; the <b>pregnant woman</b> is infected from the meat or from "
      "oocysts.") + """
  <h4 class="subsub">Disease</h4>
  <ul>
    <li><strong>Most cases go unnoticed</strong>, with mild symptoms: <strong>sore throat, fever, enlarged lymph
    nodes</strong>.</li>
    <li><strong>Serious complications in immunocompromised individuals</strong>, who can suffer <strong>brain and heart
    damage: toxoplasma encephalitis</strong> (her table: danger of central nervous system involvement for patients
    with acquired immunodeficiency syndrome).</li>
    <li><strong>Congenital</strong>: spontaneous abortion, stillbirth, or a spectrum of severe neurological and ocular
    manifestations in the newborn, including <strong>hydrocephalus, intracranial calcifications and
    chorioretinitis</strong>.</li>
  </ul>
  """ + fig(67, 1, "l17-s067-toxoplasmosis-brain.jpg",
      "Two black-and-white images: a brain scan with a bright ring-shaped lesion in one hemisphere, and a tissue section with two arrows pointing to clusters of small dots.",
      "<b>Toxoplasmosis in the brain of a patient with acquired immunodeficiency syndrome</b> (slide 67&rsquo;s "
      "caption): a <b>ring-shaped lesion</b> on the brain scan, and arrows to clusters in the brain tissue.") + """
  """ + fig(67, 2, "l17-s067-toxoplasmosis-chorioretinitis.jpg",
      "A photograph of the back of the eye: orange-red retina with blood vessels, a bright optic disc at the right, and a dark, irregular, pigmented scar below a pale white patch.",
      "<b>Toxoplasmosis chorioretinitis</b>: the dark, pigmented scar and pale patch on the retina.") + """
  <h4 class="subsub">Diagnosis, treatment and vaccines (slide 65)</h4>
  <ul>
    <li><strong>Diagnosed by serological tests, culture, histological analysis.</strong></li>
    <li><strong>Treatment: pyrimethamine and sulfadiazine, long-term administration</strong> (Table 23.2: together they
    inhibit enzymes in the pathway for folate synthesis).</li>
    <li>Vaccine development is in progress, but <strong>hampered by the genetic diversity of <em>T. gondii</em>
    strains</strong>, the complexity of a life cycle with many different stages, and the need to develop a robust and
    balanced TH1 (T helper 1) cellular immune response. A promising candidate is a <strong>genetically engineered live
    attenuated strain</strong> with a crucial transcription factor blocked.</li>
  </ul>
  <h4 class="subsub">Toxoplasmosis and mental disorders (slides 68 and 70)</h4>
  <ul>
    <li>Studies link <strong>cat ownership in childhood</strong> with later development of mental illness.</li>
    <li><strong>Acute</strong> toxoplasmosis can cause delusions and hallucinations; <strong>latent</strong> toxoplasmosis
    is a risk factor for <strong>schizophrenia</strong>, anxiety, and possibly obsessive compulsive disorder and
    addiction; <strong>chronic</strong> toxoplasmosis is linked to schizophrenia, mood disorders, psychosis and
    self-directed violence.</li>
    <li>One Dutch study showed <strong>twice the risk of developing schizophrenia</strong> if infected with
    <em>Toxoplasma</em>.</li>
    <li>Humans may not be the only animal whose mental state is affected: in hyena and lion observation studies,
    <em>Toxoplasma</em>-infected hyena cubs are <strong>bolder and more likely to get close to lions</strong>, and have a
    higher mortality rate. The hypothesis: boldness in hyena young <strong>furthers the distribution of
    <em>Toxoplasma</em> into the feline definitive host</strong>.</li>
  </ul>

  <h3 class="sub" id="par-sarco">17.15 &middot; Objective 1 &mdash; <em>Sarcocystis</em> and sarcocystosis</h3>
  <ul>
    <li><em>Sarcocystis</em> species are <strong>parasites of cattle, swine and sheep</strong>.</li>
    <li><strong>Two species infect humans</strong>: <strong><em>S. hominis</em> (from cattle)</strong> and
    <strong><em>S. suihominis</em> (from pigs)</strong> (her memory aid: &ldquo;that <em>sui</em> tells you the
    pig&rdquo;). <strong>Humans can be dead-end hosts for other
    species.</strong></li>
    <li><strong>Domestic animals are intermediate hosts</strong>: they pick up infective cysts while <strong>grazing on
    grass contaminated with human feces</strong>.</li>
    <li><strong>Humans are infected when the undercooked meat is consumed.</strong></li>
    <li><strong>Symptoms</strong>: <strong>diarrhea, nausea and abdominal pain</strong> with <em>S. hominis</em> and
    <em>S. suihominis</em>; but <strong>muscle cysts, myalgia, weakness and edema</strong> from other species.</li>
    <li><strong>Albendazole and corticosteroids</strong> are used to treat the <strong>muscular</strong>
    sarcocystosis.</li>
  </ul>

  <h3 class="sub" id="par-crypto">17.16 &middot; Objective 1 &mdash; <em>Cryptosporidium</em>: a newly recognized intestinal pathogen</h3>
  <ul>
    <li><strong>An intestinal pathogen</strong> that <strong>infects a variety of mammals, birds and reptiles</strong>
    (slide 13: free-living, water and food).</li>
    <li>It <strong>exists in tissue and oocyst phases</strong>.</li>
    <li>An infected person or animal can shed <strong>10&ndash;100 million parasites in a single bowel
    movement</strong>; the <strong>infectious dose is as little as 10 organisms</strong>.</li>
  </ul>
  <h4 class="subsub">How people acquire it</h4>
  <ul>
    <li>Most often by <strong>consuming water in recreational settings</strong>, or consuming <strong>contaminated water,
    ice or foodstuffs</strong>; it is the <mark class="prof-highlight"><strong>leading cause of recreational waterborne disease</strong></mark>. &#9733;
    Dr. Webster: &ldquo;this we&rsquo;re starting to hear more and more and more about&rdquo;.</li>
    <li>The <strong>organism can tolerate chlorine in swimming pools</strong>.</li>
    <li>In the 1990s, <strong>370,000 cases in Milwaukee, Wisconsin, from contaminated water</strong>; <strong>filtration
    is required for removal</strong> (her table: the major outbreak in Wisconsin from unpurified water).</li>
  </ul>
  <h4 class="subsub">Disease (slide 73)</h4>
  <ul>
    <li><strong>Ingestion of oocysts gives rise to sporozoites that penetrate intestinal cells.</strong></li>
    <li>It causes <strong>gastroenteritis</strong>, headache, sweating, vomiting, abdominal cramps and
    <strong>diarrhea</strong>.</li>
    <li>Patients with <strong>acquired immunodeficiency syndrome</strong> and other immunocompromised people may suffer
    <strong>chronic persistent diarrhea</strong>; <strong>young children and the elderly</strong> are likely to be
    infected.</li>
    <li><strong>Few effective drugs</strong>; it is <strong>considered a potential agent for bioterrorism</strong>.</li>
    <li>The largest hidden burden among United States diarrheal parasites: an estimated 748,000 a year, with fewer
    than 2% verified in surveillance data.</li>
  </ul>
  """ + fig(73, 1, "l17-s073-cryptosporidium-intestine.jpg",
      "A red and pink tissue section with a row of small green round bodies along the edge of the cells, pointers labeled Human intestinal cell and Cryptosporidium merozoites.",
      "<b><em>Cryptosporidium</em> merozoites</b> (green) sitting on the surface of <b>human intestinal cells</b>.") + """

  <h3 class="sub" id="par-isospora">17.17 &middot; Objective 1 &mdash; <em>Isospora belli</em> and coccidiosis</h3>
  <ul>
    <li>An <strong>intracellular intestinal parasite with an oocyst stage</strong>. Slide 13: isosporosis, from
    <strong>dogs and other mammals</strong>.</li>
    <li><strong>Transmitted in fecally contaminated food or drink.</strong></li>
    <li><strong>Infection is usually asymptomatic or self-limited.</strong></li>
    <li><strong>Symptoms</strong>: malaise, nausea and vomiting, <strong>diarrhea, fatty stools</strong>, abdominal
    cramping and weight loss.</li>
    <li><strong>Primarily associated with immunocompromised hosts.</strong></li>
    <li><strong>Treat with sulfadiazine and pyrimethamine</strong>, when required.</li>
  </ul>
  """ + fig(74, 1, "l17-s074-isospora-oocysts-drawing.jpg",
      "A drawing of two elongated, pale blue oval cells with tapered ends, labeled Oocysts; the left holds one large round speckled body, the right two.",
      "<b><em>Isospora belli</em> oocysts</b>: elongated oval walls with one or two rounded bodies inside.") + """
  """ + fig(74, 2, "l17-s074-isospora-oocyst-smear.jpg",
      "A small micrograph on a blue speckled background of an elongated oval body with purple contents.",
      "<b><em>Isospora belli</em></b> in a stained specimen (unlabeled on the slide): compare its elongated oval shape "
      "with the oocyst drawing.") + """

  <h3 class="sub" id="par-cyclospora">17.18 &middot; Objective 1 &mdash; <em>Cyclospora cayetanensis</em> and cyclosporiasis</h3>
  <ul>
    <li>An <strong>emerging protozoan pathogen</strong>; it causes <strong>cyclosporiasis</strong>.</li>
    <li><strong>Oral-fecal transmission</strong>: <strong>fresh produce and water</strong> (slide 13: water, fresh
    produce).</li>
    <li><strong>Oocysts enter the small intestine and invade the mucosa.</strong></li>
    <li><strong>Symptoms</strong>: <strong>watery diarrhea</strong>, stomach cramps, bloating, fever, muscle aches.</li>
    <li><strong>Diagnosis can be complicated: multiple stool samples must be tested.</strong> The slide 76 picture is
    <strong>an acid-fast stain of a fecal smear</strong>.</li>
    <li><strong>Treatment: trimethoprim and sulfamethoxazole.</strong></li>
    <li><strong>2026: a widespread outbreak linked to iceberg lettuce</strong>: from 1 May to 31 August, 20,996
    laboratory-confirmed cases, 1,161 hospitalizations, 2 deaths, 49 states reporting. In the same period of 2025
    there were only 1,180 cases; there were likely many more cases that were not tested or reported.</li>
  </ul>
  """ + fig(76, 1, "l17-s076-cyclospora-acid-fast.jpg",
      "A micrograph of a fecal smear on a blue and white background with scattered round pink-red bodies, pointers labeled Oocysts and Bacteria, and a 20 micrometer scale bar.",
      "<b><em>Cyclospora</em> in a fecal smear with acid-fast stain</b>: the <b>oocysts</b> stain pink-red; the "
      "<b>bacteria</b> stay blue (20&nbsp;&micro;m scale bar).") + """

  <h3 class="sub" id="par-babesia">17.19 &middot; Objective 1 &mdash; <em>Babesia</em> species and babesiosis (piroplasmosis)</h3>
  <ul>
    <li><em>Babesia</em> was the <strong>first protozoan found to cause a disease</strong>: <strong>redwater fever of
    cattle</strong> (also called bovine babesiosis, Texas fever, or tick fever).</li>
    <li>It was the <strong>first protozoan found to be associated with a vector: the tick</strong>.</li>
    <li><strong>Human babesiosis: <em>Babesia microti</em>, carried by the blacklegged deer tick</strong>. A
    <strong>relatively rare zoonosis</strong>.</li>
    <li><strong>Flu-like symptoms, but the parasite attacks red blood cells</strong>: <strong>hemolytic anemia</strong> can
    result.</li>
    <li><strong>Serious for those without a spleen</strong>, the immunocompromised, those with pre-existing liver or kidney
    disease, and those <strong>older than 50</strong>.</li>
    <li><strong>Treatment: clindamycin plus quinine, or atovaquone plus azithromycin.</strong></li>
  </ul>
  """ + fig(77, 1, "l17-s077-tick.jpg",
      "A close photograph of a tick with a dark front and an orange-red body, gripping a green blade of grass.",
      "<b>A tick</b>: human babesiosis, <em>Babesia microti</em>, is carried by the <b>blacklegged deer tick</b>.") + """
  <h4 class="subsub">The coccidian parasites side by side (slide 63&rsquo;s list)</h4>
  <table>
    <tr><th>Organism</th><th>Reservoir or host</th><th>How people acquire it</th><th>Disease</th><th>Diagnosis on the slides</th><th>Treatment on the slides</th></tr>
    <tr><td><em>Toxoplasma gondii</em></td><td><strong>Cats</strong> (feline definitive host); virtually all warm-blooded animals</td><td><strong>Raw meat or substances contaminated by cat feces</strong>; transplacental</td><td>Toxoplasmosis: mostly unnoticed; encephalitis in the immunocompromised; congenital hydrocephalus, calcifications, chorioretinitis</td><td>Serological tests, culture, histological analysis</td><td>Pyrimethamine and sulfadiazine, long-term</td></tr>
    <tr><td><em>Sarcocystis</em></td><td>Cattle, swine, sheep (intermediate hosts)</td><td><strong>Undercooked meat</strong> (<em>S. hominis</em> from cattle, <em>S. suihominis</em> from pigs)</td><td>Sarcocystosis: diarrhea, nausea, abdominal pain; muscle cysts, myalgia, weakness, edema from other species</td><td>None given</td><td>Albendazole and corticosteroids (muscular form)</td></tr>
    <tr><td><em>Cryptosporidium</em></td><td>Mammals, birds, reptiles</td><td><strong>Water</strong> (recreational, chlorine-tolerant), ice, food; infectious dose as low as 10</td><td>Gastroenteritis; chronic persistent diarrhea in acquired immunodeficiency syndrome</td><td>None given</td><td>Few effective drugs</td></tr>
    <tr><td><em>Isospora belli</em></td><td>Dogs, other mammals (slide 13)</td><td><strong>Fecally contaminated food or drink</strong></td><td>Coccidiosis: usually asymptomatic or self-limited; diarrhea, fatty stools; mainly immunocompromised hosts</td><td>None given</td><td>Sulfadiazine and pyrimethamine, when required</td></tr>
    <tr><td><em>Cyclospora cayetanensis</em></td><td>Water, fresh produce (slide 13)</td><td><strong>Oral-fecal: fresh produce and water</strong> (2026 iceberg lettuce outbreak)</td><td>Cyclosporiasis: watery diarrhea, cramps, bloating, fever</td><td>Multiple stool samples; acid-fast stain</td><td>Trimethoprim and sulfamethoxazole</td></tr>
    <tr><td><em>Babesia microti</em></td><td>Zoonosis (cattle: redwater fever)</td><td><strong>Blacklegged deer tick</strong></td><td>Babesiosis: flu-like, hemolytic anemia; serious without a spleen</td><td>None given</td><td>Clindamycin plus quinine, or atovaquone plus azithromycin</td></tr>
  </table>
"""

TEST = [
    '{q:"What does the antiprotozoan drugs slide star about these drugs?", '
    'choices:["Relatively few compared with antibacterial agents, with severe side effects",'
    '"More numerous than antibacterial agents, and well tolerated by patients","Aimed only at prokaryotic cells, so human cells are spared",'
    '"Free of side effects, because protozoa lack mitochondria"],correct:0, '
    'explain:"Antiprotozoan drugs are relatively few in comparison with antibacterial agents, and they have toxicity problems with '
    'severe side effects, and they work against eukaryotic cells."}',
    '{q:"A teenager develops headache, fever, vomiting and a stiff neck a few days after diving in a warm freshwater lake. '
    'How did the ameba reach the brain?", '
    'choices:["Through the bloodstream from the intestine","Through a break in the skin over several weeks",'
    '"Through the nasal mucosa and along the olfactory nerve","Through the cornea from a contact lens"],correct:2, '
    'explain:"Naegleria fowleri is acquired through nasal contact with water: the trophozoite burrows through the nasal mucosa '
    'and travels into the brain along the olfactory nerve, with death in 3 to 7 days. Skin and slow progression describe '
    'Acanthamoeba encephalitis; the contact lens is Acanthamoeba keratitis."}',
    '{q:"How does Trypanosoma cruzi usually enter a person?", '
    'choices:["Tsetse fly saliva injected during a bite","Reduviid (kissing) bug feces inoculated into a skin portal",'
    '"Promastigotes injected by a sand fly","Sporozoites injected by an Anopheles mosquito"],correct:1, '
    'explain:"Chagas disease: infection occurs when the kissing bug feces is inoculated into a cutaneous portal. The tsetse fly '
    'spreads T. brucei, the sand fly Leishmania, the Anopheles mosquito Plasmodium."}',
    '{q:"Which protozoan exists only as a trophozoite, with no cyst stage?", '
    'choices:["Giardia lamblia","Entamoeba histolytica","Balantidium coli","Trichomonas vaginalis"],correct:3, '
    'explain:"Trichomonads exist only in trophozoite form, with no cyst: a strict parasite that cannot survive long outside '
    'the host, so it spreads sexually. Giardia, Entamoeba and Balantidium all form cysts that are swallowed."}',
    '{q:"Pregnant women are told not to clean the cat box because of which parasite?", '
    'choices:["Toxoplasma gondii","Cryptosporidium","Babesia microti","Sarcocystis hominis"],correct:0, '
    'explain:"Cats harbor Toxoplasma oocysts and release them in feces; infection in pregnancy carries a 33% chance of '
    'transplacental transmission, with hydrocephalus, intracranial calcifications and chorioretinitis in the newborn."}',
    '{q:"In malaria, which stage leaves the liver and invades red blood cells?", '
    'choices:["Sporozoites","Gametocytes","Merozoites","Oocysts"],correct:2, '
    'explain:"The mosquito injects sporozoites, which localize in the liver and by schizogony generate merozoites; the '
    'merozoites enter red blood cells, become ring trophozoites, multiply and burst the cell. Gametocytes are taken up by the '
    'mosquito."}',
]

NOTES = [
    '<li><strong>How many <em>Plasmodium</em> species.</strong> Slide 13&rsquo;s table lists three (<em>P. vivax</em>, '
    '<em>P. falciparum</em>, <em>P. malariae</em>); slide 56 says &ldquo;4 species&rdquo; and adds <em>P. ovale</em>. '
    'Learn slide 56&rsquo;s four.</li>',
    '<li><strong>The name of <em>Naegleria</em>&rsquo;s disease.</strong> Slide 29&rsquo;s title is &ldquo;Primary Acute '
    'Meningoencephalitis&rdquo; (followed by its abbreviation), and her table on slide 4 says &ldquo;Primary Acute Meningoencephalitis&rdquo;; slide '
    '24&rsquo;s map and slide 27 say primary amebic meningoencephalitis, and slide 30&rsquo;s table &ldquo;primary amoebic '
    'meningoencephalitis&rdquo;. Primary amebic meningoencephalitis is the usual name; both are the same disease.</li>',
    '<li><strong><em>Acanthamoeba</em> and contact lenses.</strong> Her table on slide 4 gives one disease, '
    '&ldquo;Granulomatous Amoebic Encephalitis&rdquo;, with &ldquo;Found in contact lens wearers&rdquo;. Slide 31 separates '
    'two diseases: <strong>amebic keratitis</strong> in contact lens wearers (eye pain, redness, irritation; does not '
    'typically disseminate) and <strong>granulomatous amebic encephalitis</strong>, entering through a break in the skin or '
    'the nasal passages; slide 32&rsquo;s life cycle agrees with slide 31 (the eye gives keratitis; the nose and skin give '
    'the encephalitis). The contact lens belongs to the keratitis.</li>',
    '<li><strong><em>Naegleria</em> case counts.</strong> Slide 4: &ldquo;only about 200 cases reported worldwide&rdquo;; '
    'slide 27: 381 global confirmed cases through 2018. In the United States: slide 24&rsquo;s map, 157 cases '
    '(1962&ndash;2022); slide 25, 164 cases and 4 survivors (1962&ndash;2023); slide 27, 180 confirmed cases '
    '(1937&ndash;2025) and 4 survivors out of 167 cases (1962&ndash;2025). The windows differ; what agrees is rare, more '
    'than 97% fatal, 4 known United States survivors.</li>',
    '<li><strong>Who dies of <em>Naegleria</em>.</strong> Slide 26 says the estimated 16 deaths a year are &ldquo;equally '
    'distributed between males and females&rdquo;; slide 27&rsquo;s table gives males aged 10&ndash;14 as the group with the '
    'highest case count, and slide 28 says most cases are children and young adults. Slide 26 also calls the 16 a year '
    'deaths, where slide 27 calls about 16 a year the estimated true case burden and fewer than 10 the typical annual '
    'count.</li>',
    '<li><strong>Is <em>Toxoplasma</em> vector-borne?</strong> Slide 13&rsquo;s table gives its source as '
    '&ldquo;Zoonotic/vector-borne&rdquo;; slides 64&ndash;65 describe no vector: it is acquired by ingesting raw meats or '
    'substances contaminated by cat feces, and transplacentally. Learn slides 64&ndash;65. (Slide 13 also calls '
    '<em>Cryptosporidium</em> &ldquo;free-living&rdquo;, where slide 72 says it infects mammals, birds and reptiles.)</li>',
    '<li><strong>Gametes or gametocytes.</strong> Slide 58 says merozoites &ldquo;differentiate into gametes (Gametocytic '
    'phase)&rdquo;; slide 59&rsquo;s figure says some red blood cells give rise to male and female gametocytes, which infect '
    'the mosquito. Both describe the stage the mosquito picks up. Also: slide 58&rsquo;s 5&ndash;16 days is when merozoites '
    'enter the circulation; slide 60&rsquo;s 10&ndash;16 days is the incubation period.</li>',
    '<li><strong>Misspelled drug names in Table 23.2 (slide 14).</strong> &ldquo;Hetronidazole&rdquo; (for '
    '<em>Giardia</em>) is metronidazole: its mechanism cell says &ldquo;See above&rdquo;, pointing to metronidazole, and '
    'slide 41 names metronidazole. &ldquo;Miefloquine&rdquo; is mefloquine (spelled correctly in the next column and on slide '
    '61). &ldquo;Eflomithine&rdquo; is eflornithine (slide 47). &ldquo;Benzonidazole&rdquo; (Table 23.2 and slide 49) is '
    'benznidazole. Slide 31&rsquo;s &ldquo;trimethroprim&rdquo; and &ldquo;ketokonazole&rdquo; are trimethoprim and '
    'ketoconazole, and its rifampicin is slide 30&rsquo;s rifampin (two names for one drug). The tables above keep the '
    'printed spellings with the correct name beside them.</li>',
    '<li><strong>Other spellings.</strong> Slide 3 writes &ldquo;Tryponosoma&rdquo; (twice), &ldquo;Leishmani sp.&rdquo;, '
    '&ldquo;Trichuris trichura&rdquo;, &ldquo;Angiostroglylus cantonensis&rdquo;, &ldquo;Stronglyoides stercoralis&rdquo;, '
    '&ldquo;Wucherica Bancroft&rdquo;, &ldquo;Shistoma sp.&rdquo; and &ldquo;Paragoniumus westermani&rdquo;; her table '
    '(slides 4&ndash;8) writes &ldquo;Trichuris trichura&rdquo;, &ldquo;PInworm&rdquo;, &ldquo;Angiostronglylus '
    'Cantonensis&rdquo;, &ldquo;Tse tse fly&rdquo;, &ldquo;Wucherica bancroft&rdquo;, &ldquo;Shistosoma sp.&rdquo; and '
    '&ldquo;Paragoniumus westermani&rdquo;. They are <em>Trypanosoma</em>, <em>Leishmania</em>, <em>Trichuris '
    'trichiura</em>, pinworm, <em>Angiostrongylus cantonensis</em>, <em>Strongyloides stercoralis</em>, tsetse fly, '
    '<em>Wuchereria bancrofti</em>, <em>Schistosoma</em> and <em>Paragonimus westermani</em>, as written in this guide. '
    'Slide 49&rsquo;s &ldquo;Romana&rsquo;s sign&rdquo; is Roma&ntilde;a&rsquo;s sign; slide 71&rsquo;s '
    '&ldquo;sarcosystosis&rdquo; is sarcocystosis (as its title spells it). The deck&rsquo;s British spellings (&ldquo;amoebic&rdquo;, '
    '&ldquo;amoebomas&rdquo;) are written in American spelling here, and its abbreviations are written out in full.</li>',
    '<li><strong>African sleeping sickness drugs (slide 47).</strong> The slide lists &ldquo;Treatment before neurological '
    'involvement melarsoprol, suramin, eflornithine&rdquo;. In current practice suramin and pentamidine are the early-stage '
    'drugs, and melarsoprol and eflornithine are the drugs used once the central nervous system is involved. Learn the three '
    'names as the slide gives them, and that treatment should start before neurological involvement.</li>',
    '<li><strong><em>Isospora</em> treatment (slide 74).</strong> The slide gives sulfadiazine and pyrimethamine, the same '
    'pair as for toxoplasmosis. Current references (where the organism is now named <em>Cystoisospora belli</em>) use '
    'trimethoprim-sulfamethoxazole first, with pyrimethamine for people who cannot take sulfa drugs. Learn the slide&rsquo;s '
    'pair.</li>',
    '<li><strong>Malaria numbers (slide 56).</strong> 300&ndash;500 million new cases and 2 million deaths a year are older '
    'figures; recent World Health Organization reports give roughly 250 million cases and about 600,000 deaths a year, '
    'still mostly in Africa. The numbers are context; the 40% of the world threatened and 90% in Africa are the slide&rsquo;s '
    'points.</li>',
]
