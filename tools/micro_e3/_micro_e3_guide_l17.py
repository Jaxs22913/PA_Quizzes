# -*- coding: utf-8 -*-
"""Section 17 of the Microbiology Exam 3 guide -- Parasites of Medical Importance (Dr. Webster).

Same contract as _micro_e3_guide_l15.py (FIG, DECK, IMAGES, extract(), TOC, SECTION, TEST) so
tools/build_micro_e3_guide.py splices it like the others. Because the deck is 131 slides and 33 syllabus organisms,
the body is written in two fragments that this module joins:
  _micro_e3_guide_l17_protozoa.py   17.1-17.19  (slides 1-77: the overview, the protozoa)
  _micro_e3_guide_l17_helminths.py  17.20-17.41 (slides 78-131: the helminths, the arthropod vectors, and
                                                 objective 2 drawn together for every organism)
Each fragment exports TOC, BODY, TEST (a list of Test-yourself objects as JavaScript text) and NOTES (a list of
<li> items for 17.42, "where the slides disagree"). Figures are declared inline with fig() below, which records
the picture for extract() and writes the true width and height into the <img>.

Attribution: Dr. Webster. The deck file is "Lecture 16 Dr. Webster Parasites of Medical Importance.pptx" -- her own
count; the syllabus and the calendar (6 November 2026, 1-4 pm) call it LECTURE 17, and the site uses the syllabus
number. The title slide names no lecturer.

Instructional objectives are VERBATIM from the syllabus (Micro.pdf, page 5): the two numbered objectives under
"Parasites of Medical Importance -- see Appendix 2 for full list of organisms"; Appendix 2 (pages 9-10) lists 33
organisms, which slide 3 reproduces with the syllabus's spellings. The deck's objective slide (slide 2) matches.
Objective 1 is answered organism by organism (17.1-17.40); objective 2 is drawn together in 17.41.

Content is from the VISIBLE slides only, text and pictures (the deck has no speaker notes). Every slide was viewed
as a 1920-pixel render. Picture-only slides that carry content: 4-8 (her organism / disease / other information
table, a picture of a table), 13 (protozoa and their sources), 14 (Table 23.2, antiprotozoan drugs), 18 and 32
(life cycles), 27 (Naegleria statistics), 30 (a treatment table with doses: not reproduced), 43 (hemoflagellate
stages), 59 and 66 (life cycles), 84 (Table 23.4, helminths and their modes of transmission), 87 (Table 23.5,
antihelminthic drugs), 95, 97, 109, 114, 117, 122 (life cycles), 129 (Table 23.6, arthropod vectors).

PHASE 1 (6 November 2026): built from the slides while the recording was being transcribed. PHASE 2 (the same
evening): the three-part recording read (inbox flags file micro-l17-parasites-2026-11-06.flags.md); the MICROL17AUDIO
block now carries it, and her emphasis is starred in place (insert-only edits: &#9733; plus her words next to the
slide line she stressed).
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from _micro_e3_guide_l17_figs import FIG, DECK, IMAGES, fig, extract, MH, CDC  # noqa: F401

import _micro_e3_guide_l17_protozoa as P      # noqa: E402  (they call fig() at import)
import _micro_e3_guide_l17_helminths as H     # noqa: E402

TOC = """
  <a class="top-link" href="#parasites">17 &middot; Parasites of Medical Importance</a>
  <a class="sub-link" href="#par-audio">&#9733; What the recording adds</a>""" + P.TOC + H.TOC + """
  <a class="sub-link" href="#par-notes">17.42 Where the slides disagree, and where current practice differs</a>
"""

SECTION_HEAD = """
<section class="deck" id="parasites">
  <h2 class="deck-title">17 &middot; Parasites of Medical Importance</h2>
  <p class="lecturer">Dr. Webster &middot; Lecture 17 &middot; 6 November 2026</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases,
      clinical manifestations, methods of treatment, and prevention of parasites of medical importance.</li>
      <li>Describe the modes of transmission by which humans acquire parasites of medical importance.</li>
    </ol>
  </div>

  <div class="callout"><strong>Two kingdoms of parasite, sorted the same way.</strong> <em>Protozoa</em> are
  single-celled and sorted by how they move: <strong>amebas</strong> (pseudopods: <em>Entamoeba</em>,
  <em>Naegleria</em>, <em>Acanthamoeba</em>), the <strong>ciliate</strong> <em>Balantidium</em>, the
  <strong>flagellates</strong> (<em>Trichomonas</em>, <em>Giardia</em>, and the blood-borne hemoflagellates
  <em>Trypanosoma</em> and <em>Leishmania</em>) and the <strong>apicomplexans</strong>, which have no locomotor
  organelles (<em>Plasmodium</em>, <em>Toxoplasma</em>, <em>Cryptosporidium</em>, <em>Isospora</em>,
  <em>Cyclospora</em>). <em>Helminths</em> are multicellular worms: <strong>nematodes</strong> (roundworms,
  intestinal or tissue), <strong>trematodes</strong> (flukes) and <strong>cestodes</strong> (tapeworms), each
  following one of four life-cycle patterns. For every organism know its form, how it is found in the laboratory,
  the disease, and above all <strong>how people acquire it</strong> (objective 2, drawn together in 17.41). The
  syllabus points to its Appendix 2 list of 33 organisms for this lecture; slide 3 repeats it.</div>

<!--MICROL17AUDIO-->
  <div class="prof-flag" id="par-audio"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 6 November 2026</span>
  <p>About two hours with Dr. Webster in three parts (Jaxon&rsquo;s recording): part 1, 46 minutes, from slide 9 to
  <em>Leishmania</em>; part 2, 48 minutes, from the apicomplexans (slide 55) to pinworm, then the break; part 3, 27
  minutes, from hookworms to the arthropod vectors. <b>Slides 1&ndash;8 were not recorded</b> (the title, the
  objectives, the organism list and her summary tables). <b>One transcript only</b>: Notability made none, so quotes
  below are from a single machine transcription (misheard names are written correctly here). Every claim was checked
  against the deck; where the two differ, the slide is what this guide teaches.</p>
  <p><b>The quizzes are weighted by the minutes she spent</b>, stories taken out (about 13 minutes: her amebic
  dysentery on a cruise, a friend&rsquo;s sleeping sickness, the hyena, the padlocked snail tank, the Food Network,
  the eye worm wound on a stick): malaria about 10&frac12; minutes, the helminth hosts and four life cycles about 9,
  <em>Entamoeba</em> and <em>Toxoplasma</em> 6 each, <em>Trypanosoma brucei</em> 5, <em>T. cruzi</em> and
  <em>Trichomonas</em> about 4&frac12; each, <em>Naegleria</em> and helminth pathology and diagnosis 4 each,
  <em>Cryptosporidium</em> 3, then 2&frac12; or less for each of the rest.</p>
  <table>
    <tr><th>What was said</th><th>What it means for you</th></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">Why do we have pathology for worms? This is something you should
    know.</mark> &hellip; This is an important thing.&rdquo;</em> [part 2, 37:25]</td>
    <td>The one plain &ldquo;you should know&rdquo; of the lecture: 17.21, where helminth pathology comes from
    (feeding on and migrating through tissue, worms accumulating in organs and blocking them, toxic secretions) and
    what it does (organ swelling, hemorrhage, weight loss, anemia). Every quiz set asks it.</td></tr>
    <tr><td><em>&ldquo;Water treatment is the best prevention, water treatment is the best prevention.&rdquo;</em>
    [part 1, 12:02]</td>
    <td>17.3: <em>Entamoeba</em>&rsquo;s prevention line on slide 23.</td></tr>
    <tr><td><em>&ldquo;Vector control is one of the best ways of controlling these hemoflagellate diseases&rdquo;</em>;
    &ldquo;once again, vector control is the best way&rdquo; (Chagas); &ldquo;once again, vector control is what
    they do&rdquo; (malaria). And treat early: <em>Naegleria</em>, <em>T. brucei</em> before the nervous system is
    involved, <em>T. cruzi</em>. [part 1, 18:31, 38:19, 43:07; part 2, 9:06]</td>
    <td>17.10, 17.11, 17.13: eliminate the tsetse fly, control the reduviid bug, mosquito control is key;
    17.4, 17.10, 17.11: treatment must be early.</td></tr>
    <tr><td><em>&ldquo;One that I can almost guarantee that you will encounter in your clinical practice&rdquo;</em>
    (<em>Trichomonas</em>); &ldquo;the one that you will almost surely see in your clinical life&rdquo; (pinworm,
    &ldquo;the scourge of the daycare center&rdquo;). [part 1, 23:09; part 2, 44:36]</td>
    <td>17.7 and 17.24 (slide 94&rsquo;s star: the most common worm disease of children in temperate zones).</td></tr>
    <tr><td><em>Chagas disease: &ldquo;the one that you are more likely to see in your clinical work &hellip; because
    of the migration of the vector. It&rsquo;s coming further north as things get warmer.&rdquo;</em> Malaria: cases in
    Florida &ldquo;where there was no travel involved whatsoever &hellip; So that&rsquo;s why you might see this
    one.&rdquo; [part 1, 32:28; part 2, 1:27]</td>
    <td>17.11 (slide 48&rsquo;s star; every set asks it) and 17.13 (slide 62&rsquo;s eight non-travel cases in
    Florida). The slides give vector migration as the reason for Chagas only.</td></tr>
    <tr><td><em>&ldquo;Pregnant women should never clean the litter box. So if you are with a patient who is pregnant
    and she has a cat, you tell her, get somebody else to clean the litter box.&rdquo;</em> [part 2, 13:54]</td>
    <td>17.14: transplacental transmission, a 33% chance. Every set asks it.</td></tr>
    <tr><td><em>&ldquo;This is the one that you will get going camping&rdquo;</em> (<em>Giardia</em>);
    <em>Cryptosporidium</em>, &ldquo;the leading cause of recreational waterborne diseases, the swimming pools, the
    water parks&rdquo;. [part 1, 27:31; part 2, 23:48]</td>
    <td>17.8 (her table: common in campers) and 17.16.</td></tr>
    <tr><td><em>&ldquo;It would not be a bad thing for you to remember this lovely picture&rdquo;</em> (the trypanosome
    blood smear); &ldquo;I would not ask you to differentiate between the picture of cruzi and gambiense. So as long
    as you knew trypanosoma, I would be a happy camper.&rdquo; [part 1, 35:52; 38:40]</td>
    <td>17.10&rsquo;s slide 46 picture: know it as <em>Trypanosoma</em>. One quiz set shows it.</td></tr>
    <tr><td><em>Trichinella: &ldquo;You cannot cure it. You cannot cure it&rdquo;</em> once the larvae have encysted;
    &ldquo;Do not eat your pork rare.&rdquo; Flukes and tapeworms: &ldquo;never eat freshwater fish as sushi&rdquo;,
    &ldquo;you get this theme of undercooked&rdquo;, &ldquo;cook your beef. Please, please.&rdquo; [part 3, 5:00,
    17:03, 18:01, 20:26]</td>
    <td>17.28, 17.35, 17.37: objective 2 for the meat- and fish-borne worms (17.41).</td></tr>
    <tr><td><em>&ldquo;That sui tells you the pig.&rdquo;</em> [part 2, 19:35]</td>
    <td>17.15: <em>Sarcocystis suihominis</em> comes from pigs, <em>S. hominis</em> from cattle.</td></tr>
  </table>
  <p><b>What she said not to memorize</b> (taught in this guide, not asked in the quizzes): slide 13&rsquo;s protozoa
  table and slide 14&rsquo;s Table 23.2 (&ldquo;a chart I am not asking you to memorize&rdquo;, though she repeated
  that antiprotozoan drugs are few and toxic), the <em>Naegleria</em> case lists and statistics (slides 25&ndash;27)
  and treatment table (slide 30), the four hemoflagellate stage names (&ldquo;I am not going to be asking about the
  names of these four stages&rdquo;), Table 23.4 (slide 84, &ldquo;it&rsquo;s just got lots of worms in it&rdquo;),
  Table 23.5 (slide 87) and Table 23.6 (slide 129); and, as in Lectures 10 and 14, &ldquo;I&rsquo;m not going to be
  asking you for specific treatments for the diseases&rdquo;.</p>
  <p>She corrected no slide. Slips: she said &ldquo;brucei&rdquo; once for <em>T. cruzi</em>, and &ldquo;cycle
  B&rdquo; for the fourth life-cycle pattern (D). On the beef tapeworm she backed slide 8 (&ldquo;this is, of course,
  why you lose weight when you have a tapeworm&rdquo;) while also giving slide 119&rsquo;s &ldquo;vague symptoms of
  abdominal pain and nausea&rdquo; (17.42). She read slide 118 (humans the definitive host of tapeworms) and slide 124
  (the dog the definitive host of <em>Echinococcus</em>) without reconciling them. She also taught
  <em>Dirofilaria</em> (17.33), which is not on the syllabus list.</p>
  </div>
<!--/MICROL17AUDIO-->
"""

NOTES = """
  <h3 class="sub" id="par-notes">17.42 Where the slides disagree, and where current practice differs</h3>
  <ul>
""" + "\n".join("    " + li for li in P.NOTES + H.NOTES) + """
  </ul>

  <button type="button" class="test-yourself-btn" onclick="window.openTestYourself('Test yourself &mdash; Parasites of Medical Importance', TEST_YOURSELF.parasites)">Test yourself! &rarr;</button>
  <p class="src">Source: <em>Parasites of Medical Importance</em> (Lecture 16 Dr. Webster Parasites of Medical
  Importance.pptx), Slides 1&ndash;131, and the PAJ 5200 syllabus instructional objectives.</p>
</section>
"""

SECTION = SECTION_HEAD + P.BODY + H.BODY + NOTES

TEST = """
    parasites: [
""" + ",\n".join("      " + t.strip() for t in P.TEST + H.TEST) + """
    ],
"""
