# -*- coding: utf-8 -*-
"""Section 18 of the Microbiology Exam 3 guide -- DNA Viruses of Medical Importance (Dr. Webster, 13 November 2026).

Same contract as _micro_e3_guide_l17.py (FIG, DECK, IMAGES, extract(), TOC, SECTION, TEST) so
tools/build_micro_e3_guide.py splices it like the others. The deck is 106 slides and 17 syllabus viruses, so the body
is written in two parts:
  this module                        the head, the recording box, 18.1 (her chart, slides 3-7) and objectives 1-3
                                     (18.2-18.6, slides 8-29), 18.27 (where the slides disagree) and the Test-yourself
                                     bank
  _micro_e3_guide_l18_viruses.py     objective 4 virus by virus (18.7-18.25, slides 30-106) and objective 5 drawn
                                     together (18.26); exports TOC, BODY, TEST, NOTES
Figures are declared inline with fig() (_micro_e3_guide_l18_figs.py), which records the picture for extract() and
writes the true width and height into the <img>. Fifteen of them are PROTECTED (the Webster review page shows them).

Attribution: Dr. Webster (she/her). The deck file is "Lecture 18  Dr. Webster -  DNA viruses of medical
importance.pptx"; the calendar and the syllabus call it Lecture 18 (13 November 2026).

Instructional objectives are VERBATIM from the syllabus (whitespace normalized); the deck's objective slide (slide 2)
matches. They are answered in order: objective 1 in 18.2-18.4, objective 2 in 18.5, objective 3 in 18.6, objective 4
virus by virus in 18.7-18.25, objective 5 in 18.26.

Content is from the VISIBLE slides only, text and pictures (speaker notes do not count). Every slide was viewed as a
1920-pixel render and every placed picture at full size. Picture-only slides that carry content: 4-7 (her chart, a
picture of a table: transcribed row for row in 18.1), 10, 11, 17, 21-23, 27, 30, 33, 56, 61, 65, 67, 70, 73, 76,
80, 82, 84, 89, 95, 98, 100, 105. Pictures left out: slide 1 (a title collage, decoration; its micrograph repeats on
slide 86), slide 39 (an 18th-century cartoon, decoration), slides 50-51's maps (case tallies, not taught).

The recording (inbox flags file micro-l18-dna-viruses-2026-11-13.flags.md, OUTSIDE the repo) weights and stars;
it adds no content. Her emphasis is starred in place (&#9733; plus her words next to the slide line she stressed).
Drug names are listed as the slides give them; she does not test specific treatments (standing rule from Lectures
10, 14 and 17) and the quizzes do not ask them.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from _micro_e3_guide_l18_figs import FIG, DECK, DECK_HTML, IMAGES, fig, extract, MH  # noqa: F401

import _micro_e3_guide_l18_viruses as V      # noqa: E402  (calls fig() at import)


TOC = """
  <a class="top-link" href="#dna-viruses">18 &middot; Deoxyribonucleic Acid (DNA) Viruses of Medical Importance</a>
  <a class="sub-link" href="#dna-audio">&#9733; What the recording adds</a>
  <a class="sub-link" href="#dna-chart">18.1 Her chart: the DNA viruses at a glance</a>
  <a class="sub-link" href="#dna-structure">18.2 Objective 1 &mdash; Viruses in human disease and viral structure</a>
  <a class="sub-link" href="#dna-phage">18.3 Objective 1 &mdash; Phage replication: lytic, lysogenic and chronic cycles</a>
  <a class="sub-link" href="#dna-animal">18.4 Objective 1 &mdash; Animal virus replication and how it differs from phages</a>
  <a class="sub-link" href="#dna-infections">18.5 Objective 2 &mdash; Acute (lytic), persistent chronic and persistent latent infections</a>
  <a class="sub-link" href="#dna-onco">18.6 Objective 3 &mdash; Oncogenic versus teratogenic viruses</a>""" + V.TOC + """
  <a class="sub-link" href="#dna-notes">18.27 Where the slides disagree, and where current practice differs</a>
"""

SECTION_HEAD = """
<section class="deck" id="dna-viruses">
  <h2 class="deck-title">18 &middot; Deoxyribonucleic Acid (DNA) Viruses of Medical Importance</h2>
  <p class="lecturer">Dr. Webster &middot; Lecture 18 &middot; 13 November 2026</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Recall the steps of DNA virus replication.</li>
      <li>Compare and contrast the characteristics of a lytic viral infection versus a persistent chronic or
      persistent latent infection.</li>
      <li>Differentiate between oncogenic and teratogenic viruses.</li>
      <li>Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases, clinical
      manifestations, methods of treatment, and prevention of DNA viruses of medical importance.</li>
      <li>Compare and contrast the mode of transmission, clinical manifestations, and availability of a vaccine for
      DNA viruses of medical importance.</li>
    </ol>
  </div>

  <div class="callout"><strong>Three families wear an envelope, four do not.</strong> The DNA viruses that infect
  humans sort by <strong>envelope</strong> and <strong>strandedness</strong>: <strong>enveloped double-stranded</strong>
  (the <strong>poxviruses</strong>, <strong>herpesviruses</strong> and <strong>hepadnaviruses</strong>),
  <strong>nonenveloped double-stranded</strong> (<strong>adenoviruses</strong>, <strong>polyomaviruses</strong>,
  <strong>papillomaviruses</strong>) and <strong>nonenveloped single-stranded</strong> (<strong>parvoviruses</strong>).
  Learn first how a virus replicates (in a bacterium, then in an animal cell: 18.3&ndash;18.4), the three kinds of
  infection it can set up (acute, persistent chronic, persistent latent: 18.5) and which viruses cause cancer or birth
  defects (18.6); then, for each of the 17 viruses on slide 3, its disease, how it spreads and whether a vaccine
  exists (18.7&ndash;18.26). Her chart (18.1) is that last part on four slides.</div>

<!--MICROL18AUDIO-->
  <div class="prof-flag" id="dna-audio"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 13 November 2026</span>
  <p>About an hour and three-quarters with Dr. Webster in two parts (Jaxon&rsquo;s recording): part 1, 49 minutes,
  from slide 9 (capsids) to slide 45 (smallpox eradicated), then the break; part 2, 55 minutes of lecture from
  molluscum contagiosum (slide 46) to adeno-associated virus (slide 106), after which she began her Exam 3 review
  (on its own page). <b>Slides 1&ndash;8 were not recorded</b> (the title, the objectives, the virus list and her
  chart on slides 4&ndash;7). <b>One transcript only</b>: Notability made none, so the quotes below are from a single
  machine transcription (misheard names are written correctly here). Every claim was checked against the deck; where
  the two differ, the slide is what this guide teaches.</p>
  <p><b>Minutes she spent</b> (about 93 of content; stories and asides, about 10&frac12; minutes, taken out): phage
  cycles about 9, smallpox history and variolation 8, mpox 5, hepatitis B 4&frac12;, cytomegalovirus and Epstein-Barr
  virus about 4 each, the three kinds of persistent infection about 4, animal virus replication, phages in the gut and
  immune system, and the polyomaviruses about 3 each; viral structure, varicella zoster virus, human papillomavirus,
  adenovirus, the herpes simplex shared facts, the herpesvirus family, herpes simplex 1 and the smallpox disease about
  2 to 2&frac12; each; 2 or less for each of the rest.</p>
  <table>
    <tr><th>What was said</th><th>What it means for you</th></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">Now, animal viruses, differences between those and phages. This you
    need to know.</mark>&rdquo;</em> &hellip; <em>&ldquo;You need to know these differences. Am I subtle
    enough?&rdquo;</em> [part 1, 19:03; 21:35]</td>
    <td>The strongest signpost of part 1, and the first line of her Exam 3 review: 18.4. The whole virion is
    engulfed; it must be uncoated; most DNA viruses replicate in the nucleus; release is by budding, which is where the
    envelope comes from.</td></tr>
    <tr><td><em>&ldquo;There are different kinds of viral infections that you need to know, okay?&rdquo;</em> [part 1,
    25:50]</td>
    <td>18.5: acute (colds, flu), persistent chronic (human immunodeficiency virus, hepatitis B virus), persistent
    latent (the herpesviruses), each with its example.</td></tr>
    <tr><td><em>Hepatitis B: &ldquo;this is a chronic, persistent infection, as opposed to the latent, which are the
    herpes viruses&rdquo;</em>; &ldquo;for healthcare workers, this is why you have to avoid the needle sticks&rdquo;.
    And: <em>&ldquo;hepatitis B, which is the DNA virus, you need to know that one&rdquo;</em>. [part 2, 35:17, 36:18,
    36:47]</td>
    <td>18.20 (slide 87: an issue for health care workers) and 18.5.</td></tr>
    <tr><td><em>Poxviruses are &ldquo;the kind of unusual ones with the DNA viruses because most of the DNA viruses
    multiply in the nucleus. But the pox viruses multiply in the cytoplasm.&rdquo;</em> [part 1, 34:22]</td>
    <td>18.8: they multiply in the cytoplasm in factory areas.</td></tr>
    <tr><td><em>Smallpox, the early rash: &ldquo;that&rsquo;s when you are most contagious. That&rsquo;s when you are most
    contagious.&rdquo;</em> And <em>&ldquo;this was really the first disease that was eradicated through vaccination
    efforts.&rdquo;</em> [part 1, 44:54; 48:31]</td>
    <td>18.9: slide 40&rsquo;s asterisk (the early rash is the stage of greatest contagion; contagious until every scab
    has fallen off) and her chart&rsquo;s &ldquo;first disease to be eliminated by vaccine&rdquo;.</td></tr>
    <tr><td><em>Mpox: the Centers for Disease Control and Prevention vaccine locator, the &ldquo;only one where you
    actually see that there&rsquo;s a vaccine locator tools&rdquo;</em>; JYNNEOS two doses 28 days apart; ACAM2000 a
    single dose with multiple needle pricks. [part 2, 6:27&ndash;7:28]</td>
    <td>18.12 (slide 52). Her review asked &ldquo;where do I find a vaccine against this one?&rdquo;.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">Put a star on this little slide.</mark>&rdquo;</em> [part 2, 11:15]</td>
    <td>Her only explicit star: slide 57, the eight human herpesviruses and their diseases (18.14). Her review: &ldquo;1
    through 8, what do each one of them do&rdquo;.</td></tr>
    <tr><td><em>&ldquo;Here&rsquo;s the fun part. It can be spread even if you cannot see visible lesions.&rdquo;</em>
    [part 2, 12:02]</td>
    <td>18.15: herpes simplex (slide 58), and genital herpes in the absence of lesions (slide 59).</td></tr>
    <tr><td><em>Varicella zoster virus: &ldquo;most infectious in the 24 to 48 hours before you ever see lesions&rdquo;;
    &ldquo;again it is most infectious before the lesions ever hit.&rdquo; &ldquo;If you have shingles you can infect a
    person who has not been vaccinated &hellip; they will not get shingles, they will get chicken pox.&rdquo;</em>
    [part 2, 20:31, 21:27, 22:20]</td>
    <td>18.16 (slides 68&ndash;69). Her review asked &ldquo;when you are contagious with that one&rdquo;.</td></tr>
    <tr><td><em>Cytomegalovirus: &ldquo;this is one of those viruses which is teratogenic, okay?&rdquo;; &ldquo;They call
    it an owl&rsquo;s eye effect, an owl&rsquo;s eye effect.&rdquo;</em> [part 2, 25:58, 26:26]</td>
    <td>18.6 (slide 28&rsquo;s teratogen list) and 18.17 (slide 73&rsquo;s picture).</td></tr>
    <tr><td><em>Human herpesvirus 8: &ldquo;probably the one that you&rsquo;d be most familiar with because it causes
    Kaposi&rsquo;s sarcoma&rdquo;.</em> [part 2, 33:26]</td>
    <td>18.19 (slides 57, 83, 84). Her review asked which herpesvirus is associated with Kaposi sarcoma.</td></tr>
    <tr><td><em>Human papillomavirus: &ldquo;this is why early detection is really important&rdquo;</em> (Pap smear
    screening). Parvovirus B19: <em>&ldquo;if a pregnant woman gets it, it can be very, very serious&rdquo;</em>.
    [part 2, 45:23; 53:47]</td>
    <td>18.22 (slide 99) and 18.24 (slide 104, hydrops fetalis).</td></tr>
  </table>
  <p><b>What she said not to need</b> (taught in this guide, not asked in the quizzes): slide 44&rsquo;s three stockpile
  vaccines (&ldquo;There are three different vaccines that you don&rsquo;t need but there are vaccines that are
  there.&rdquo;) and the other names of chronic fatigue syndrome on slide 78 (&ldquo;if you know chronic fatigue
  syndrome, I&rsquo;m good.&rdquo;). Hepatitis A and C (slide 85) and the vector-borne viruses (slide 24) are Dr.
  Fair&rsquo;s next week, as ribonucleic acid viruses. She did not restate it this lecture, but her standing rule from
  Lectures 10, 14 and 17 holds: &ldquo;I&rsquo;m not going to be asking you for specific treatments for the
  diseases&rdquo;. Drug names are listed below as the slides give them; the quizzes do not ask them (she named no
  smallpox drug aloud).</p>
  <p><b>Where her spoken words differ from the slide</b> (the slide is what this guide teaches, and no quiz asks the
  point): adenovirus &ldquo;shown to be oncogenic in animals and in humans&rdquo; (slide 93: oncogenic in animals,
  <strong>not in humans</strong>; likely a dropped &ldquo;not&rdquo;); Epstein-Barr virus &ldquo;50 to 90 days&rdquo;
  of incubation (slide 75: 30&ndash;50 days); a history of genital herpes means a scheduled cesarean section (slide 64:
  cesarean section <strong>if there is an outbreak at the time of birth</strong>); adeno-associated virus
  &ldquo;currently used for treating&rdquo; a list of diseases (slide 106: approved only for lipoprotein lipase
  deficiency, the rest in clinical trials); parvovirus &ldquo;distemper in cats and then cardiac disease in dogs and
  puppies&rdquo; (slide 103: enteric disease in dogs, fatal cardiac infection in puppies); and &ldquo;that vaccinia
  virus, the cowpox&rdquo; (slide 43: vaccinia is the smallpox vaccine virus; slide 53 teaches cowpox as its own
  virus; 18.27). She corrected no slide.</p>
  <p><b>Her chart</b> (slides 4&ndash;7, 18.1) was not discussed in the lecture; in the review she called it her study
  tool: &ldquo;for each of these, I&rsquo;ve given you this chart to help clue you in on. If you can associate what
  the viruses are and what they do, you should be OK.&rdquo; Where a chart-only line disagrees with a text slide
  (18.27), the text slide wins.</p>
  </div>
<!--/MICROL18AUDIO-->
"""


def _rows(rows):
    """Table rows from (virus, disease, transmission, clinical, vaccine, other) tuples; '' is an empty cell."""
    out = []
    for r in rows:
        cells = ["<td><strong>%s</strong></td>" % r[0]] + ["<td>%s</td>" % (c or "&mdash;") for c in r[1:]]
        out.append("    <tr>" + "".join(cells) + "</tr>")
    return "\n".join(out)


_HEAD = ("    <tr><th>Virus</th><th>Disease</th><th>Transmission</th><th>Clinical Manifestations</th>"
         "<th>Vaccine Available</th><th>Other information</th></tr>")


def _chart(rows):
    return ('<div class="table-scroll" style="overflow-x:auto;-webkit-overflow-scrolling:touch">'
            '<table style="min-width:760px">\n' + _HEAD + "\n" + _rows(rows) + "\n  </table></div>")


CHART_4 = [
    ("Variola", "Smallpox", "Inhalation, Direct Contact, Fomites",
     "Fever, malaise, prostration, rash, possible toxemia, shock", "Yes&mdash;with vaccinia",
     "First disease to be eliminated by vaccine; No more routine vaccination except for front line"),
    ("Molluscum contagiosum", "Molluscum contagiosum", "Direct contact and Fomites",
     "Small, smooth waxy macules on genitals and thighs", "No",
     "Treatment typically by removal of individual lesions"),
    ("Monkeypox", "Monkeypox", "Contact with infected animals or humans", "Skin pocks, Fever, Swollen lymph nodes",
     "Yes&mdash;JYNNEOS became available April 2024", "Major outbreak United States 2022&ndash;2023"),
    ("Vaccinia", "Cowpox", "Contact with infected animals, (rarely humans)", "Skin pocks typically on hands",
     "Yes&mdash; used in Europe for animals", "Also found in rodents, cats, zoo and circus animals"),
    ("Herpes Simplex I<br>Herpes Virus Family", "Fever Blisters, Cold Sores", "Direct contact",
     "Lesions near lips and genitals, herpetic gingivostomatitis, herpetic keratitis, encephalitis occasionally in "
     "neonates", "No, but candidate vaccines in trials", ""),
]
CHART_5 = [
    ("Herpes Simplex II<br>Herpes Virus Family", "Genital Herpes", "Direct contact",
     "anorexia, fever, and bilateral swelling and tenderness in groin; clusters of sensitive vesicles on genitalia, "
     "perineum, and buttocks; urethritis, painful urination, cervicitis, itching, vesicles ulcerate",
     "No, research ongoing",
     "Association with Cervical and Penile cancer; often diagnosed with Pap smear; can visualize viral particles in "
     "infected cells"),
    ("Herpes Simplex I and II", "Herpetic Whitlow<br>Herpes of the newborn",
     "Direct contact<br>Transmission mother to child",
     "Pain and swelling on finger or thumb, blisters or sores and red streaks, sometimes fever<br>Lesions on mouth, "
     "skin, eyes, to central nervous system where potentially fatal", "No", ""),
    ("Varicella zoster<br>Herpes Virus Family", "Chickenpox<br>Shingles",
     "Respiratory droplets and contact with fluid from active skin lesions",
     "filled vesicles, malaise, fever<br>Reactivation of virus results in shingles with painful vesicles localized in "
     "distinctive areas of the skin on a nerve path&mdash;dermatomes", "Yes, vaccines for both chickenpox and shingles",
     "Shingles is infectious to those who have never been immunized&mdash;will manifest as chickenpox"),
    ("Cytomegalovirus<br>Herpes Virus Family",
     "Cytomegalovirus retinitis, cytomegalovirus encephalitis, cytomegalovirus intestinal tract inflammation",
     "Direct contact with infectious body fluids (saliva, blood, mucus, tears, breast milk, urine, semen, cervical "
     "secretions) or tissues",
     "blind spots<br>Encephalitis and intestinal tract&mdash;brain swelling, confusion, lethargy, enlarged liver and "
     "spleen, jaundice, capillary bleeding. Fetuses may exhibit microcephaly, Babies who survive develop neurological "
     "sequelae, hearing, visual disturbances and mental retardation. Infections may be fatal",
     "None currently available, but several in clinical trials",
     "A picture: an infected lung cell beside a normal one, labeled &ldquo;Nucleus with large inclusion&rdquo; and "
     "&ldquo;Owl&rsquo;s eye effect&rdquo; (slide 73). Severe complications with neonates, fetuses, transplant "
     "patients, human immunodeficiency virus patients and other immunocompromised hosts"),
]
CHART_6 = [
    ("Epstein Barr Virus<br>Herpes Virus Family",
     "Infectious mononucleosis; Burkitt&rsquo;s lymphoma; Nasopharyngeal carcinoma; Chronic fatigue syndrome "
     "(possible link)", "Direct oral contact or contact with fomites contaminated with saliva",
     "Sore throat, high fever, cervical lymphadenopathy, splenomegaly<br>Burkitt lymphoma&mdash;swollen lymph nodes, "
     "abdominal pain, fever, night sweats, weight loss<br>Nasopharyngeal carcinoma&mdash;lump in neck, hearing loss, "
     "blocked nasal passage",
     "No preventive vaccines but several therapeutic vaccines in clinical trials for Epstein-Barr virus related cancers",
     "Burkitt&rsquo;s lymphoma primarily affects African boys 5&ndash;7<br>Nasopharyngeal cancer primarily affects "
     "adults 30&ndash;60 with family history or who eat salt cured foods"),
    ("Human Herpes Virus 6<br>Herpes Virus Family", "Roseola", "Contact with saliva",
     "Acute febrile disease followed by rash", "None",
     "Possible connection with later development of multiple sclerosis, and multiple types of cancers"),
    ("Human Herpes Virus 7<br>Herpes Virus Family", "Roseola", "Contact with saliva",
     "Acute febrile disease followed by rash", "None",
     "Possible connection with later development of multiple sclerosis, and multiple types of cancers"),
    ("Human Herpes Virus 8<br>Herpes Virus Family", "Kaposi&rsquo;s sarcoma",
     "Saliva, sexual contact, blood transfusion, organ transplant",
     "Small painless discolored lumps on the skin&mdash;may affect internal organs", "None",
     "May also be related to some forms of Castleman disease and primary effusion lymphoma."),
    ("Hepatitis B", "Hepatitis B", "Contact with blood or serum, sexual contact",
     "Malaise, fever, chills, anorexia, abdominal discomfort, diarrhea, jaundice, rash, arthritis", "Yes",
     "May lead to cirrhosis and hepatic cancer; great risk to health care workers due to very low infective dose"),
]
CHART_7 = [
    ("Adenovirus",
     "50+ different types cause the common cold, pharyngitis, conjunctivitis, cystitis, infantile gastroenteritis. "
     "Some strains are associated with hepatitis in young children",
     "Droplet infection from respiratory and ocular secretions, Ingestion",
     "Upper respiratory symptoms, congestion, cough, fever; gastrointestinal symptoms and typical symptoms of hepatitis",
     "Vaccine for Types 4 and 7 for military personnel in training situations", ""),
    ("Human Papilloma Virus", "Warts and Genital Warts",
     "Direct contact including sexual contact or contact with fomites",
     "Tiny, flat inconspicuous bumps in the skin to extensive branching, cauliflower like masses",
     "Vaccines available for Genital Warts",
     "Nine human papillomavirus strains increase the risk for developing reproductive system cancers"),
    ("Polyoma Viruses including JC virus and BK virus",
     "JC virus&mdash;progressive multifocal leukoencephalopathy; BK virus&mdash;interstitial nephritis",
     "Exposure to body fluids, ingestion of contaminated food or water, JC in early childhood, BK in adolescence",
     "JC&mdash;demyelination of nerves leads to progressive neurological symptoms; BK&mdash;typically after "
     "transplant&mdash;renal complications, bloody urine", "None for humans",
     "Most prevalent in immunosuppressed populations"),
    ("Parvovirus B19",
     "Fifth disease; Hydrops fetalis, Polyarthropathy and cessation of red blood cell production", "Droplet infection",
     "Fifth disease&mdash;Slapped face rash, low grade fever; Hydrops fetalis&mdash;fatal anemia in fetus from maternal "
     "transmission; Polyarthropathy&mdash;massive joint swelling; Anemia from red blood cell cessation", "", ""),
]

CHART = """
  <h3 class="sub" id="dna-chart">18.1 &middot; Her chart: the DNA viruses at a glance (slides 3&ndash;7)</h3>
  <p>Slide 3 lists the <strong>17 DNA viruses that infect humans</strong> named in the syllabus for this lecture:
  <strong>variola</strong>, <strong>molluscum contagiosum</strong>, <strong>mpox</strong>, <strong>vaccinia</strong>,
  <strong>herpes simplex 1</strong>, <strong>herpes simplex 2</strong>, <strong>varicella zoster</strong>,
  <strong>cytomegalovirus</strong>, <strong>Epstein-Barr virus</strong>, <strong>human herpesviruses 6, 7 and
  8</strong>, <strong>hepatitis B</strong>, <strong>adenovirus</strong>, <strong>human papillomavirus</strong>,
  <strong>polyomavirus</strong> and <strong>parvovirus</strong>. The deck also teaches cowpox and orf (18.13) and
  adeno-associated virus (18.25).</p>
  <p>Slides 4&ndash;7 are pictures of one table she built, under the instruction: <em>&ldquo;For each of the viruses on
  the following tables, review disease states, modes of transmission, clinical manifestations, whether vaccines are
  available and any other pertinent information listed.&rdquo;</em> It is transcribed below row for row, one table per
  slide with the slide picture above it; spelling is corrected and abbreviations are written out; an empty cell on
  the slide is shown as &mdash;. On a phone, swipe the table sideways. Four of its lines disagree with the text slides
  (the herpes simplex 2 cancer line, the JYNNEOS date, the Vaccinia row&rsquo;s &ldquo;Cowpox&rdquo;, Burkitt&rsquo;s
  &ldquo;African boys&rdquo;): see 18.27, where the text slide wins.</p>
  """ + fig(4, 1, "l18-s004-virus-chart-pox-and-herpes-simplex-1.jpg",
      "A six-column table headed Virus, Disease, Transmission, Clinical Manifestations, Vaccine Available, Other information, with rows for Variola, Molluscum contagiosum, Monkeypox, Vaccinia and Herpes Simplex I.",
      "<b>Her chart, part 1: the poxviruses and herpes simplex 1.</b> Read across each row for the hook: smallpox "
      "&ldquo;first disease to be eliminated by vaccine&rdquo;, molluscum treated by removing the lesions, mpox "
      "with a vaccine (JYNNEOS), cowpox lesions on the hands.") + """
  """ + _chart(CHART_4) + """
  """ + fig(5, 1, "l18-s005-virus-chart-herpes-simplex-to-cytomegalovirus.jpg",
      "The same table continued with rows for Herpes Simplex II, Herpes Simplex I and II, Varicella zoster and Cytomegalovirus; the cytomegalovirus row carries a small pink micrograph of an infected lung cell labeled Owl's eye effect.",
      "<b>Her chart, part 2: herpes simplex 2, whitlow and the newborn, varicella zoster, cytomegalovirus.</b> Look "
      "for the vaccine column (only varicella zoster has one) and the cytomegalovirus row&rsquo;s owl&rsquo;s eye "
      "picture.") + """
  """ + _chart(CHART_5) + """
  """ + fig(6, 1, "l18-s006-virus-chart-epstein-barr-to-hepatitis-b.jpg",
      "The table continued with rows for Epstein Barr Virus, Human Herpes Virus 6, 7 and 8, and Hepatitis B.",
      "<b>Her chart, part 3: Epstein-Barr virus, human herpesviruses 6, 7 and 8, hepatitis B.</b> Look for saliva "
      "as the route of the first four, Kaposi&rsquo;s sarcoma for human herpesvirus 8, and hepatitis B as the one "
      "with a vaccine (&ldquo;Yes&rdquo;) and a great risk to health care workers.") + """
  """ + _chart(CHART_6) + """
  """ + fig(7, 1, "l18-s007-virus-chart-adenovirus-to-parvovirus.jpg",
      "The table continued with rows for Adenovirus, Human Papilloma Virus, Polyoma Viruses including JC virus and BK virus, and Parvovirus B19.",
      "<b>Her chart, part 4: the nonenveloped viruses.</b> Look for the vaccines (adenovirus types 4 and 7 for the "
      "military; human papillomavirus) against &ldquo;None for humans&rdquo; (polyomaviruses), and parvovirus "
      "B19&rsquo;s slapped face rash and hydrops fetalis.") + """
  """ + _chart(CHART_7) + """
"""

OBJ123 = """
  <h3 class="sub" id="dna-structure">18.2 &middot; Objective 1 &mdash; Viruses in human disease and viral structure (slides 8&ndash;12)</h3>
  <p>Viruses in human infections and diseases (slide 8):</p>
  <ul>
    <li>Viruses are <strong>obligate intracellular parasites</strong>.</li>
    <li><strong>Animal viruses are categorized according to nucleic acid, capsid, and presence or absence of
    envelope.</strong></li>
    <li>There are multiple families of DNA and RNA viruses.</li>
    <li><strong>Most DNA viruses are double-stranded</strong>, but there are some single-stranded DNA viruses as
    well.</li>
    <li><strong>All RNA viruses are single-stranded except for the double-stranded RNA reoviruses.</strong></li>
  </ul>
  <h4 class="subsub">Viral structure (slide 9)</h4>
  <ul>
    <li><strong>All viruses have capsids</strong>: protein coats that enclose and protect their nucleic acid. Capsids
    are <strong>helical</strong>, <strong>icosahedral</strong> or <strong>complex</strong> (the phage).</li>
    <li>They contain genetic material: <strong>DNA or RNA</strong>.</li>
    <li>They <strong>may have an envelope or spikes</strong> (animal viruses).
      <ul>
        <li><mark class="prof-highlight"><strong>The envelope is obtained during budding of the virus through the cell
        membrane.</strong></mark> &#9733; Her Exam 3 review: &ldquo;Where do they get that envelope?&rdquo;</li>
        <li>The envelope is a <strong>mechanism to assist in evading the immune system</strong>.</li>
      </ul></li>
  </ul>
  """ + fig(10, 1, "l18-s010-naked-and-enveloped.jpg",
      "Left: a helical nucleocapsid, a coil of nucleic acid wrapped in stacked capsid units; right: a cutaway round virus with that helical nucleocapsid inside an envelope studded with spikes.",
      "<b>A helical virus, naked and enveloped.</b> Look for the labels: the <b>capsid</b> units around the "
      "<b>nucleic acid</b> make the <b>nucleocapsid</b>; the enveloped virus wraps the same nucleocapsid in an "
      "<b>envelope</b> (taken from the cell membrane at budding).") + """
  """ + fig(10, 2, "l18-s010-naked-icosahedral-and-enveloped.jpg",
      "Two drawings: (a) a naked nucleocapsid virus, an icosahedral capsid around coiled nucleic acid, and (b) an enveloped virus, the same capsid inside a matrix layer and an outer envelope with spikes.",
      "<b>Naked nucleocapsid virus (a) versus enveloped virus (b).</b> Look for what the enveloped virus adds outside "
      "the capsid: the <b>matrix</b>, the <b>envelope</b> and its <b>spikes</b>.", MH) + """
  <div class="pearl"><p><strong>Where viruses came from (slide 12; background, not tested).</strong> The total mass of
  viruses on earth is equivalent to 75 million blue whales. There is thought to be no one common ancestor: viruses may
  have evolved multiple times in the history of life on earth, and may do so again. Three ideas: they escaped or
  devolved from whole cells, ditching cellular machinery to live a simple life; they descended from independent genetic
  elements before cellular life evolved; or a hybrid, an independent genetic element that stole from primitive
  cells.</p></div>

  <h3 class="sub" id="dna-phage">18.3 &middot; Objective 1 &mdash; Phage replication: lytic, lysogenic and chronic cycles (slides 11, 13&ndash;21)</h3>
  """ + fig(11, 1, "l18-s011-phage-structure.jpg",
      "A drawing of a bacteriophage: a head made of a many-sided capsid holding the nucleic acid core, on a tail made of a sheath, a plug and spreading tail fibers.",
      "<b>Phage viruses: the complex capsid.</b> Look for the <b>head</b> (capsid around the nucleic acid core) and "
      "the <b>tail</b> (sheath, plug, tail fibers): the tail is what breaches the bacterial wall and injects the "
      "DNA.") + """
  <p>Viruses impact the genome of cellular life: phage viruses carry out <strong>transduction</strong> in bacteria.
  An estimated <strong>8% of human DNA is of viral origin</strong>: mammalian ancestors acquired a gene essential for
  placental development from a viral source. <strong>Bacteriophage viruses</strong> have bacterial host cells, but may
  impact human health. Their <strong>replication methods</strong> are the <strong>lytic cycle</strong>, the
  <strong>lysogenic cycle</strong> and the <strong>chronic cycle</strong> (filamentous phages) (slide 13).</p>
  <h4 class="subsub">The lytic cycle (slide 14)</h4>
  <table>
    <tr><th>Step</th><th>What happens</th></tr>
    <tr><td><strong>Adsorption</strong></td><td>The phage attaches to the surface of the bacterium.</td></tr>
    <tr><td><strong>Penetration</strong></td><td><strong>Viral lysozyme</strong> and a <strong>tail pin mechanism</strong>
    breach the wall and <strong>inject the viral DNA</strong> into the bacterial host.</td></tr>
    <tr><td><strong>Replication</strong></td><td>The virus <strong>turns off normal metabolism</strong> and turns the
    bacterium into a viral factory, first replicating the DNA, then the capsid components.</td></tr>
    <tr><td><strong>Assembly</strong></td><td>The virus begins to put new virions together.</td></tr>
    <tr><td><strong>Maturation</strong></td><td>Completion of viral formation.</td></tr>
    <tr><td><strong>Release</strong></td><td><strong>Viral lysozyme causes the host cell wall to burst</strong>,
    releasing the new virions.</td></tr>
  </table>
  <h4 class="subsub">The lysogenic cycle (slide 15)</h4>
  <ul>
    <li><strong>Adsorption and penetration are the same as in the lytic cycle</strong>, so the viral DNA is in the host
    cell.</li>
    <li>Instead of turning off bacterial metabolism, the <strong>viral DNA integrates into the bacterial host
    chromosome and becomes a prophage</strong>.</li>
    <li>The prophage-integrated bacterium may persist for an extended period, making generations of prophage
    bacteria.</li>
    <li>A <strong>shock of some kind induces the prophage to release</strong> from the host chromosome and start a lytic
    cycle, which goes through replication, assembly, maturation and release of new virions.</li>
  </ul>
  <h4 class="subsub">The chronic cycle (slide 16)</h4>
  <ul>
    <li><strong>Filamentous phages</strong>: flexible rods that contain <strong>single-stranded DNA</strong> coding for
    about 10 genes.</li>
    <li>They infect mostly Gram-negative bacteria, but have been found to infect the Gram-positive
    <em>Propionibacterium freudenreichii</em> (used in the manufacturing of Swiss cheese).</li>
    <li>They typically attach to pili or walls but <strong>do not use lysozyme</strong>; instead there appears to be a
    <strong>compatibility between virion capsid proteins and receptor proteins</strong> in the host. The actual mechanism
    of DNA entrance is yet to be fully understood.</li>
    <li>Once in the host, the DNA and capsid components are replicated and assembled into virions.</li>
    <li>Virions are <strong>extruded from the host cell but do not lyse the host</strong>, just slow its growth
    rate.</li>
    <li>A <strong>cooperative arrangement</strong>: the host delivers phages throughout the environment and the phage
    provides benefits to the host, <strong>toxin production</strong> and <strong>addition to biofilms</strong>.</li>
  </ul>
  """ + fig(17, 1, "l18-s017-phage-cycles.jpg",
      "A diagram of three phage cycles from one bacterium: the lytic cycle (brown arrows) ending in bacterial lysis and release of virions; the lysogenic cycle (pink) in which the phage becomes a prophage and the bacterium reproduces normally, with prophage induction back into a lytic or chronic cycle; and the chronic cycle (blue) in which filamentous phages are extruded from the bacterium.",
      "<b>The three cycles side by side.</b> Look for where each ends: <b>lysis</b> (lytic), a <b>prophage</b> "
      "passed on as the bacterium divides (lysogenic), and virions <b>extruded</b> while the bacterium lives on, "
      "its growth slowed (chronic). The key: virulent phages have only lytic cycles; temperate phages have lysogenic "
      "cycles and lytic or chronic cycles.") + """
  <table>
    <tr><th>Lytic</th><th>Lysogenic</th><th>Chronic</th></tr>
    <tr><td>Rapid takeover of bacterial metabolism</td><td>Integration of viral genes as <strong>prophage</strong></td>
    <td>Penetration via <strong>protein compatibility</strong></td></tr>
    <tr><td>Production of multiple copies of virus</td><td>May acquire new traits&mdash;ability to make a toxin</td>
    <td>Virions assembled and released chronically</td></tr>
    <tr><td><strong>Destruction of host cell</strong></td><td><strong>Immune to reinfection</strong></td>
    <td>Bacterial growth slowed</td></tr>
    <tr><td><strong>Generalized transduction</strong> (random pieces of the host DNA may be transmitted to other
    bacteria)</td><td>Viral genes replicated with host cell; <strong>specialized transduction</strong> (all cells
    carry the same DNA from the host)</td><td>Cooperative arrangement&mdash;the host gains benefits that contribute to
    pathogenicity: toxins and biofilms</td></tr>
  </table>
  <p class="src">The comparison table is slide 18.</p>
  <h4 class="subsub">Phages in the gut and the immune system (slides 19&ndash;21)</h4>
  <ul>
    <li><strong>Phages are bacterial strain specific</strong>; the gut environment protects some bacteria; both
    antagonistic and mutualistic interactions are possible; interactions may change over time due to evolution
    (prophage induction, lysogenic conversion, predation, and some bacteria are resistant) (slide 19).</li>
    <li>These complex relationships may explain the relative <strong>unpredictability of phage therapy trials</strong>.
    Phages may compromise colonization of normal flora; some studies have shown a shift in virome composition in
    patients with inflammatory bowel disease, Crohn&rsquo;s disease or ulcerative colitis, which may or may not be a
    cause-and-effect relationship (slide 20).</li>
    <li>Phages may interact with mucus on M cells and be taken in; may be taken in by epithelial cells and translocated;
    may be taken in directly by dendritic cells. Phage nucleic acids may stimulate an <strong>adaptive immune
    response</strong> with secretion of phage-specific immunoglobulin A and immunoglobulin G. T cell activation in
    Peyer&rsquo;s patches and lymph nodes produces cytokines such as interferon gamma (slide 21).</li>
  </ul>
  """ + fig(21, 1, "l18-s021-phage-immune-system.jpg",
      "A drawing of the gut lining: phage antigens cross an M cell and an epithelial cell from the lumen into the tissue below, where a dendritic cell takes them up and presents them to a B cell making immunoglobulin A and G and to a CD4 T cell releasing interferon gamma.",
      "<b>How phages meet the immune system.</b> Look for the numbered routes: through the <b>M cell</b> or an "
      "epithelial cell, into a <b>dendritic cell</b>, then to the <b>B cell</b> (immunoglobulin A in the gut, "
      "immunoglobulin G in serum) and the T cell (interferon gamma).") + """

  <h3 class="sub" id="dna-animal">18.4 &middot; Objective 1 &mdash; Animal virus replication and how it differs from phages (slides 22&ndash;24)</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Lecturer emphasized &mdash; &ldquo;This you need to know&rdquo;</span>
  <p>&ldquo;Now, animal viruses, differences between those and phages. This you need to know.&rdquo; &hellip; &ldquo;You
  need to know these differences. Am I subtle enough?&rdquo; [part 1, 19:03; 21:35]. Her Exam 3 review opened with
  it: &ldquo;you should know the difference between animal virus replication and phage virus replication.&rdquo;</p></div>
  <p><strong>Animal viruses: differences to phages</strong> (slide 22):</p>
  <ul>
    <li><mark class="prof-highlight"><strong>The entire virion is engulfed</strong></mark> (a phage injects only its
    deoxyribonucleic acid).</li>
    <li><mark class="prof-highlight"><strong>It requires uncoating to release the genetic material</strong></mark> (the pH
    of the cytoplasm against the extracellular fluid).</li>
    <li><mark class="prof-highlight"><strong>Release is by budding</strong></mark>, which <strong>may assist in acquisition
    of the envelope</strong> (a lytic phage bursts the cell wall with lysozyme).</li>
  </ul>
  <table>
    <tr><th></th><th>Phage (in a bacterium)</th><th>Animal virus</th></tr>
    <tr><td><strong>Entry</strong></td><td>Adsorption, then penetration: viral lysozyme and the tail pin breach the wall and
    <strong>inject the DNA</strong> (slide 14)</td><td><strong>Entire virion engulfed</strong> (slide 22)</td></tr>
    <tr><td><strong>Uncoating</strong></td><td>Not needed: only the DNA enters</td><td><strong>Required</strong> to release the
    genetic material (slide 22)</td></tr>
    <tr><td><strong>Where a DNA virus replicates</strong></td><td>In the bacterium turned &ldquo;viral factory&rdquo; (slide
    14)</td><td><strong>Most DNA viruses are budded off the nucleus</strong>; most RNA viruses multiply in and are released
    from the cytoplasm (slide 24). The exception: poxviruses multiply in the cytoplasm (18.8)</td></tr>
    <tr><td><strong>Release</strong></td><td>Lytic: viral lysozyme bursts the cell wall (slide 14); chronic: extruded
    without lysis (slide 16)</td><td><strong>Budding</strong>, which may give the envelope (slide 22)</td></tr>
  </table>
  """ + fig(22, 1, "l18-s022-animal-virus-entry.jpg",
      "A diagram of an enveloped animal virus at the edge of a host cell: it binds receptors with its spikes, is engulfed into a vesicle, is uncoated, its parts are made inside the cell, and new viruses bud off the membrane carrying an envelope with spikes.",
      "<b>An enveloped animal virus, start to finish.</b> Look for the numbered steps: 1 adsorption (spikes to "
      "receptors), 2&ndash;3 penetration and <b>uncoating</b>, 4 synthesis, 5 assembly, 6 <b>release by "
      "budding</b>, carrying away an envelope with the spikes.", MH) + """
  <p><strong>Non-phage DNA viral replication</strong> (slide 23; the picture shows a papovavirus, a typical
  DNA-containing virus that attacks animal cells):</p>
  <ol>
    <li><strong>Attachment</strong>: the virion attaches to the host cell.</li>
    <li><strong>Entry and uncoating</strong>: the virion enters the cell, and its DNA is uncoated.</li>
    <li>A portion of the viral DNA is <strong>transcribed</strong>, producing messenger RNA that encodes
    &ldquo;early&rdquo; viral proteins.</li>
    <li><strong>Biosynthesis</strong>: the viral DNA is replicated, and some viral proteins are made.</li>
    <li><strong>Late translation</strong>: capsid proteins are synthesized.</li>
    <li><strong>Maturation</strong>: virions mature.</li>
    <li><strong>Release</strong>: virions are released.</li>
  </ol>
  <p>The slide&rsquo;s note: <strong>the necessity for uncoating and release of virions by budding</strong>.</p>
  """ + fig(23, 1, "l18-s023-dna-virus-replication.jpg",
      "A circular diagram of seven numbered cells: a papovavirus attaches, enters and is uncoated, its DNA moves to the nucleus, early messenger RNA is made, the DNA is replicated, capsid proteins are made, virions mature in the nucleus and are released.",
      "<b>Non-phage DNA viral replication, seven steps.</b> Look for the <b>nucleus</b>: the viral DNA is replicated "
      "there and the new virions mature there, which is why most DNA viruses are budded off the nucleus.") + """
  <p><strong>Medical considerations</strong> (slide 24): viruses are <strong>limited to a particular host or cell
  type</strong> (compatibility of receptors and genetic material); viral infections range from asymptomatic to mild to
  life-threatening; many viruses are strictly human in origin, others are zoonoses transmitted by vectors (West Nile
  fever, hantavirus, viral encephalitis: next week&rsquo;s lecture).</p>

  <h3 class="sub" id="dna-infections">18.5 &middot; Objective 2 &mdash; Acute (lytic), persistent chronic and persistent latent infections (slides 25&ndash;27, 29)</h3>
  <p><strong>The course of viral disease</strong> (slide 25): invasion at the portal of entry and primary infection;
  some viruses <strong>replicate locally</strong> (tissue disruption), others <strong>enter the circulation and infect
  other tissues</strong>. Common manifestations: <strong>rashes, fever, muscle aches, respiratory involvement, swollen
  lymph nodes</strong>. Viruses may be involved in disorders such as type 1 diabetes, multiple sclerosis and chronic
  fatigue syndrome (an autoimmune connection). <strong>Body defenses</strong>: the combined action of interferon,
  antibodies, natural killer cells and cytotoxic T cells, which <strong>frequently results in lifelong
  immunity</strong>; this is why some viruses have been used as agents for vaccination.</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Lecturer emphasized &mdash; &ldquo;kinds of viral infections that you need to know&rdquo;</span>
  <p>&ldquo;There are different kinds of viral infections that you need to know, okay?&rdquo; [part 1, 25:50]. Her
  review asked for an example of each.</p></div>
  <table>
    <tr><th>Kind (slide 26)</th><th>What happens</th><th>The slide&rsquo;s examples</th></tr>
    <tr><td><strong>Acute</strong> (&ldquo;acute viral agent&rdquo;)</td><td>A <strong>rapid course</strong>; the
    <strong>lytic cycle</strong></td><td><strong>Colds, flu</strong></td></tr>
    <tr><td colspan="3"><em>Persistent infections</em>: some viruses establish <strong>long-term persistent
    infections</strong> that last many years or a lifetime. There are <strong>2 types</strong>:</td></tr>
    <tr><td><strong>Persistent chronic</strong></td><td>The virus <strong>is detectable in tissue samples</strong>,
    <strong>multiplying at a slow rate</strong>; <strong>symptoms mild or absent</strong>; may involve
    <strong>integration</strong> of the genetic material into the host chromosome</td>
    <td><strong>Human immunodeficiency virus</strong> and <mark class="prof-highlight"><strong>hepatitis B
    virus</strong></mark> &#9733; Dr. Webster: &ldquo;this is a chronic, persistent infection, as opposed to the
    latent, which are the herpes viruses&rdquo;</td></tr>
    <tr><td><strong>Persistent latent</strong></td><td><strong>After a lytic cycle</strong>, the virus enters a
    <strong>dormant phase</strong>; generally <strong>not detectable, no symptoms</strong>; can <strong>reactivate</strong>
    and result in <strong>recurrent infections</strong>. The viral DNA is an <strong>episome</strong>: in the nucleus but
    <strong>not integrated</strong></td><td><strong>Herpesviruses</strong></td></tr>
  </table>
  """ + fig(27, 1, "l18-s027-effects-on-host-cells.jpg",
      "A diagram of one infected cell with five numbered outcomes: viral multiplication and lytic infection ending in release of virus; a latent infection with recurrence back to lytic infection; a chronic infection in which the cell keeps releasing a few virions; and transformation of the cell to malignancy.",
      "<b>Possible effects of viral infections on host cells.</b> The slide says: <b>&ldquo;Think about the "
      "similarity of these cycles to the phage cycles&rdquo;</b>. Look for the matches: lytic infection (the lytic "
      "cycle), <b>latent infection</b> with recurrence (a prophage induced back into a lytic cycle), <b>chronic "
      "infection</b> releasing virus slowly (the chronic cycle), plus <b>transformation to malignancy</b> "
      "(18.6).") + """
  <table>
    <tr><th></th><th>Acute (lytic)</th><th>Persistent chronic</th><th>Persistent latent</th></tr>
    <tr><td><strong>Is the virus detectable?</strong></td><td>Yes, during the rapid course</td><td><strong>Yes</strong>,
    in tissue samples</td><td><strong>Generally not</strong></td></tr>
    <tr><td><strong>Multiplying?</strong></td><td>Rapidly; the host cell is destroyed</td><td><strong>At a slow
    rate</strong></td><td>No: dormant until it reactivates</td></tr>
    <tr><td><strong>Symptoms</strong></td><td>Yes (colds, flu)</td><td><strong>Mild or absent</strong></td><td>None while
    dormant; <strong>recurrent infections</strong> when it reactivates</td></tr>
    <tr><td><strong>Viral DNA</strong></td><td>&mdash;</td><td><strong>May integrate</strong> into the host chromosome</td>
    <td><strong>Episome</strong>: in the nucleus, not integrated</td></tr>
    <tr><td><strong>Phage cycle it resembles</strong> (slide 27)</td><td>Lytic</td><td>Chronic</td><td>Lysogenic
    (dormant, then induced)</td></tr>
    <tr><td><strong>Examples</strong></td><td>Colds, flu</td><td>Human immunodeficiency virus, hepatitis B virus</td>
    <td>Herpesviruses</td></tr>
  </table>
  <p>Slide 88 adds that most people infected with hepatitis B show few overt symptoms and <strong>eventually develop
  immunity</strong>; a small number develop chronic liver disease (18.20, 18.27).</p>
  <h4 class="subsub">Viruses and autoimmune disorders (slide 29)</h4>
  <p>Viruses may be involved in autoimmune disorders in a significant way: start with a <strong>genetically
  predisposed individual</strong>; add environmental exposure to components of diet, gut microbiota, chemicals and
  pollutants, and infectious agents; this causes <strong>cellular stress and genetic damage</strong>, complicated by
  the <strong>latency</strong> of some pathogens and the synergistic effect of multiple pathogens. The viruses
  <strong>disrupt the host cell&rsquo;s epigenetic control</strong>, leading to expression of previously sequestered
  gene alleles. One theory ties this to <strong>&ldquo;fragile sites&rdquo; on the X chromosome</strong>, areas
  particularly susceptible to nucleic acid insertion, which ultimately can degrade the cell&rsquo;s nucleolus and lead
  to the production of <strong>autoantigens</strong>.</p>

  <h3 class="sub" id="dna-onco">18.6 &middot; Objective 3 &mdash; Oncogenic versus teratogenic viruses (slide 28)</h3>
  <table>
    <tr><th></th><th>Oncogenic</th><th>Teratogenic</th></tr>
    <tr><td><strong>What it means</strong></td><td><strong>Some persistent viruses</strong> cause
    <strong>cancer</strong></td><td>Viruses that <strong>cross the placenta</strong>, causing <strong>developmental
    disturbances and permanent defects</strong></td></tr>
    <tr><td><strong>Who is harmed</strong></td><td>The infected person, years into a persistent infection</td><td>The
    <strong>fetus</strong></td></tr>
    <tr><td><strong>The slide&rsquo;s examples</strong></td><td>
      <strong>Epstein-Barr virus</strong> &mdash; Burkitt&rsquo;s lymphoma<br>
      <strong>Herpesvirus 8</strong> &mdash; Kaposi&rsquo;s sarcoma<br>
      <strong>Hepatitis B</strong> &mdash; hepatic carcinoma<br>
      <strong>Papillomaviruses</strong> &mdash; cervical and penile cancer</td>
      <td><strong>Rubella</strong><br><mark class="prof-highlight"><strong>Cytomegalovirus</strong></mark> &#9733; Dr.
      Webster: &ldquo;this is one of those viruses which is teratogenic, okay?&rdquo;</td></tr>
  </table>
  <p>The deck adds, virus by virus: adenoviruses are <strong>oncogenic in animals, not in humans</strong> (slide 93);
  polyomaviruses <strong>induce tumors in experimental animals</strong> (slide 101); papilloma and polyoma viruses
  cause <strong>persistent infections and tumors</strong> (slide 96); poxviruses can stimulate tumor formation (slide
  32); herpesviruses may be associated with cancers (slide 55). For the fetus and newborn: cytomegalovirus in the
  fetus and newborn (slide 72, 18.17), herpes of the newborn from the mother before or during birth (slide 64, 18.15)
  and parvovirus B19 passed from a pregnant woman to the fetus, causing hydrops fetalis (slide 104, 18.24).</p>
  <div class="pearl"><p><strong>Oncogenic</strong> = <em>onco-</em>, a tumor: a persistent virus that leads to
  cancer. <strong>Teratogenic</strong> = <em>terato-</em>, a malformation: a virus that crosses the placenta and
  leaves a permanent defect. Cytomegalovirus is the teratogen among this lecture&rsquo;s DNA viruses.</p></div>
  <p><strong>Diagnosis of viral diseases</strong> (slide 28): symptoms, <strong>isolation in cell or animal
  culture</strong>, <strong>serological tests for antibodies</strong>; some tests for antigens.</p>
"""

NOTES = """
  <h3 class="sub" id="dna-notes">18.27 &middot; Where the slides disagree, and where current practice differs</h3>
  <ul>
    <li><strong>Who causes cervical and penile cancer.</strong> Her chart&rsquo;s herpes simplex 2 row (slide 5):
    &ldquo;Association with Cervical and Penile cancer; often diagnosed with Pap smear&rdquo;. Slide 28&rsquo;s oncogenic
    list gives cervical and penile cancer to the <strong>papillomaviruses</strong>, and slides 99&ndash;100 tie the Pap
    smear to human papillomavirus. In the lecture she tied cancer only to papillomaviruses. Learn slide 28; the chart
    line is not asked.</li>
    <li><strong>When JYNNEOS arrived.</strong> Chart (slide 4): JYNNEOS &ldquo;became available April 2024&rdquo;; slide
    44: Jynneos, &ldquo;live virus approved Septembe[r] 24, 2019&rdquo;. She gave no date and said slide 44&rsquo;s
    vaccines are not needed. Know the name and the dosing (two doses, 28 days apart: slide 52), not a date.</li>
    <li><strong>Vaccinia or cowpox?</strong> The chart&rsquo;s fourth row (slide 4) reads Virus &ldquo;Vaccinia&rdquo;,
    Disease &ldquo;Cowpox&rdquo;, with cowpox&rsquo;s facts (hands, rodents, cats, zoo and circus animals, a vaccine used
    in Europe for animals). Slide 43 teaches <strong>vaccinia</strong> as the virus of the <strong>smallpox
    vaccine</strong>, and slide 53 teaches <strong>cowpox</strong> as its own virus. She equated them aloud once (&ldquo;that
    vaccinia virus, the cowpox&rdquo;). This guide follows slides 43 and 53 (18.10, 18.13).</li>
    <li><strong>Burkitt lymphoma&rsquo;s patients.</strong> Chart (slide 6): &ldquo;primarily affects African boys
    5&ndash;7&rdquo;; slide 77: &ldquo;central African children 5&ndash;7 years old&rdquo;. Learn slide 77.</li>
    <li><strong>Two &ldquo;most common&rdquo; sexually transmitted diseases.</strong> Slide 46: molluscum contagiosum,
    &ldquo;in U.S. [the United States], most commonly an STD [sexually transmitted disease]&rdquo;; slide 97: genital warts,
    &ldquo;most common STD [sexually transmitted disease] in U.S. [the United States]&rdquo;. The two statements are about different things, but read together they are
    easy to confuse; neither is asked as &ldquo;the most common&rdquo;.</li>
    <li><strong>Hepatitis B as the chronic example.</strong> Slide 26 gives hepatitis B virus as the example of a
    persistent chronic infection, and slide 87 says &ldquo;chronic&rdquo; and &ldquo;can become a chronic
    infection&rdquo;; slide 88 says most people infected show few overt symptoms and <strong>eventually develop
    immunity</strong>, and only a small number develop chronic liver disease. Both hold: it is the chronic-infection
    example, chronic in some of those infected.</li>
    <li><strong>The adenovirus vaccine.</strong> Slide 94: an &ldquo;inactivated polyvalent vaccine against Types 4 and
    7&rdquo;, &ldquo;given as oral vaccine to personnel 17&ndash;50 years old&rdquo;. Current guidelines differ: the
    military adenovirus vaccine is a live oral vaccine. Answer from the slide.</li>
    <li><strong>Therapeutic vaccines for Epstein-Barr virus cancers.</strong> Slide 79: &ldquo;several therapeutic
    vaccines <em>available</em> for EBV [Epstein-Barr virus] related cancers&rdquo;; chart (slide 6): &ldquo;several therapeutic vaccines
    <em>in clinical trials</em>&rdquo;. Both agree there is <strong>no preventive vaccine</strong>.</li>
    <li><strong>Where herpes simplex 1 causes lesions.</strong> Chart (slide 5&rsquo;s first row, slide 4): herpes
    simplex 1, &ldquo;lesions near lips and genitals&rdquo;; slide 58: herpes simplex 1 usually on the oropharynx, herpes
    simplex 2 on the genitalia, possibly oral. Learn slide 58&rsquo;s usual sites.</li>
    <li><strong>Most DNA viruses replicate in the nucleus, but not the poxviruses.</strong> Slide 24: most DNA viruses
    are budded off the nucleus; slide 32: poxviruses multiply in the cytoplasm. Not a contradiction, the exception she
    stressed (18.8).</li>
    <li><strong>Numbers that are not asked.</strong> Slide 12&rsquo;s 75 million blue whales and slide 13&rsquo;s 8% of
    human DNA of viral origin are background; so are the case counts and dates of slides 34&ndash;38, 44, 47 and
    49&ndash;51.</li>
  </ul>
""" + ("\n".join("  " + n for n in V.NOTES) if V.NOTES else "") + """

  <button type="button" class="test-yourself-btn" onclick="window.openTestYourself('Test yourself &mdash; DNA Viruses of Medical Importance', TEST_YOURSELF.dnaviruses)">Test yourself! &rarr;</button>
  <p class="src">Source: <em>The DNA Viruses of Medical Importance</em> (""" + DECK_HTML + """), Slides
  1&ndash;106, and the PAJ 5200 syllabus instructional objectives.</p>
</section>
"""

SECTION = SECTION_HEAD + CHART + OBJ123 + V.BODY + NOTES

_TEST = [
    '{q:"How does an animal virus enter its host cell, compared with a bacteriophage?", '
    'choices:["It injects only its nucleic acid through the wall with a tail pin","The entire virion is engulfed, then uncoated",'
    '"It attaches to a pilus and extrudes its genome","It fuses with the nucleus before entering the cytoplasm"],correct:1, '
    'explain:"The entire animal virion is engulfed and must be uncoated to release its genetic material; a phage uses viral '
    'lysozyme and a tail pin to breach the wall and inject only its deoxyribonucleic acid."}',
    '{q:"Where does an animal virus get its envelope?", '
    'choices:["It synthesizes the envelope from viral lipids in the cytoplasm","From the bacterial cell wall it lyses",'
    '"From the host cell membrane as it buds out of the cell","From the capsid proteins made by late translation"],correct:2, '
    'explain:"The envelope is obtained during budding of the virus through the cell membrane, and it helps the virus evade the '
    'immune system."}',
    '{q:"Which describes a persistent latent viral infection?", '
    'choices:["Virus detectable in tissue, multiplying slowly, with mild or absent symptoms",'
    '"A rapid lytic course such as a cold or the flu","Viral genes always integrated into the host chromosome",'
    '"A dormant, generally undetectable virus that can reactivate, as in the herpesviruses"],correct:3, '
    'explain:"Latent: after a lytic cycle the virus goes dormant, generally not detectable and without symptoms, and can '
    'reactivate as recurrent infection; the viral deoxyribonucleic acid is an episome in the nucleus, not integrated. The first '
    'choice is a chronic infection (human immunodeficiency virus, hepatitis B virus); the second an acute infection."}',
    '{q:"Which deoxyribonucleic acid (DNA) virus is teratogenic?", '
    'choices:["Cytomegalovirus","Epstein-Barr virus","Human herpesvirus 8","Hepatitis B virus"],correct:0, '
    'explain:"Teratogenic viruses cross the placenta and cause developmental disturbances and permanent defects: rubella and '
    'cytomegalovirus. Epstein-Barr virus (Burkitt lymphoma), human herpesvirus 8 (Kaposi sarcoma) and hepatitis B virus '
    '(hepatic carcinoma) are the oncogenic examples."}',
    '{q:"Where do poxviruses multiply?", '
    'choices:["In the nucleus, like most deoxyribonucleic acid viruses","In the cytoplasm, in factory areas",'
    '"In the bacterial chromosome as a prophage","In sensory ganglia, as an episome"],correct:1, '
    'explain:"Poxviruses, the largest and most complex animal viruses, multiply in the cytoplasm in factory areas; most other '
    'deoxyribonucleic acid viruses are budded off the nucleus."}',
    '{q:"When is varicella zoster virus most infectious?", '
    'choices:["Once all the scabs have fallen off","Only while shingles vesicles are crusting",'
    '"24 to 48 hours before lesions develop","During the latent phase in the ganglia"],correct:2, '
    'explain:"Varicella zoster virus is most infectious 24 to 48 hours prior to the development of lesions, and spreads by '
    'respiratory droplets and fluid from active lesions. A person with shingles can give an unvaccinated child chickenpox, not '
    'shingles."}',
    '{q:"Which herpesvirus is linked with Kaposi sarcoma?", '
    'choices:["Human herpesvirus 6","Cytomegalovirus","Epstein-Barr virus","Human herpesvirus 8"],correct:3, '
    'explain:"Human herpesvirus 8, the Kaposi sarcoma-associated virus, is linked with the common tumor of patients with '
    'acquired immunodeficiency syndrome: small, painless, discolored lumps on the skin that may spread to internal organs. '
    'Human herpesviruses 6 and 7 cause roseola; Epstein-Barr virus causes infectious mononucleosis."}',
    '{q:"A cervical Pap smear shows koilocytes. Which virus is the cause?", '
    'choices:["Human papillomavirus","Herpes simplex virus type 2","Polyomavirus JC","Parvovirus B19"],correct:0, '
    'explain:"The koilocyte is the Pap smear finding in human papillomavirus infection; nine human papillomavirus types raise '
    'the risk of reproductive cancer, so early detection by Pap smear matters. The herpes simplex Pap smear shows a giant cell '
    'with multiple nuclei."}',
    '{q:"Why is hepatitis B an issue for health care workers?", '
    'choices:["It spreads by respiratory droplets in clinics","It is acquired by handling sheep and goats",'
    '"Minute amounts of blood can transmit it","Its vaccine is not offered to adults"],correct:2, '
    'explain:"Hepatitis B virus multiplies in the liver, which continuously seeds the blood with virus; minute amounts of '
    'blood and blood products can transmit it, so needle sticks matter. A vaccine from yeast-cloned surface antigen is the '
    'primary prevention, and hepatitis B immune globulin protects the exposed."}',
]

TEST = """
    dnaviruses: [
""" + ",\n".join("      " + t.strip() for t in _TEST + list(V.TEST)) + """
    ],
"""
