# -*- coding: utf-8 -*-
"""Section 10 of the Microbiology Exam 2 guide -- Gram-Positive Bacilli of Medical Importance (Dr. Webster).

Same shape as tools/_micro_e2_guide_l7.py and _l8.py (FIG, DECK, fig(), TOC, SECTION, TEST), plus IMAGES in
the build_micro_e2_guide.py tuple shape. tools/micro_e2/l10_guide.html is rendered from this file
(python3 tools/micro_e2/_micro_e2_guide_l10.py), so edit here, not there.

Attribution: Dr. Webster, from the deck file name ("Lecture 9 Dr. Webster Gram positive Bacilli.pptx") and the
recording (she refers to Dr. Fair in the third person and names her own next lecture, Epidemiology, which
the calendar gives to Dr. Webster). The title slide names no lecturer. The file name's "Lecture 9" is the
deck's own numbering; the calendar row (2 October 2026) makes it Lecture 10.

Instructional objectives are VERBATIM from the syllabus (Micro.pdf, page 4): the two numbered objectives
under "Gram Positive Bacilli of Medical Importance".

AUDIO: both parts of the 2 October 2026 recording (46:25 + 43:40) read in BOTH transcripts (local
faster-whisper medium.en and Notability's) and diffed 2026-10-08; quotes appear in both unless marked,
cited by the local transcript's timestamps. The recording starts at slide 6.
"""
import os

FIG = "micro-exam-2-study-guide-images"
DECK = "Lecture 9 Dr. Webster Gram positive Bacilli.pptx"
INBOX_DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Microbiology Inbox/Exam 2/Lecture 9 Dr. Webster Gram positive Bacilli.pptx")

# (slide, picture index on that slide, published file name) -- add to IMAGES in build_micro_e2_guide.py
# as (DECK10, slide, index, name). Each was viewed at full size before it was captioned.
IMAGES = [
    (5, 1, "l10-s05-differentiation-scheme.png"),
    (8, 2, "l10-s08-anthracis-central-spores.png"),
    (11, 1, "l10-s11-cutaneous-anthrax-eschar.png"),
    (25, 1, "l10-s25-gas-gangrene-muscle.png"),
    (28, 1, "l10-s28-tetani-terminal-spores.jpg"),
    (30, 1, "l10-s30-tetanus-spinal-neuron.png"),
    (36, 1, "l10-s36-botulin-neuromuscular-junction.jpg"),
    (38, 1, "l10-s38-floppy-baby.png"),
    (47, 2, "l10-s47-pseudomembranous-colitis.png"),
    (54, 1, "l10-s54-listeria-cycle.png"),
    (60, 1, "l10-s60-diphtheriae-stain.png"),
    (63, 1, "l10-s63-diphtheria-pseudomembrane.png"),
    (73, 1, "l10-s73-tubercle.jpg"),
    (84, 1, "l10-s84-leprosy-polar-forms.jpg"),
    (88, 1, "l10-s88-feather-test.png"),
]


def fig(name, w, h, alt, cap, slide, mh=False):
    note = "Copyright &copy; The McGraw-Hill Companies. " if mh else ""
    return ('<figure class="fig"><img width="%d" height="%d" loading="lazy" src="%s/%s" alt="%s">'
            '<figcaption>%s <span class="src">%sSource: %s, Slide %d.</span></figcaption></figure>'
            % (w, h, FIG, name, alt, cap, note, DECK, slide))


TOC = """
  <a class="top-link" href="#gram-positive-bacilli">10 &middot; Gram-Positive Bacilli of Medical Importance</a>
  <a class="sub-link" href="#gpb-audio">&#9733; What the recording adds</a>
  <a class="sub-link" href="#gpb-sorting">10.1 Objective 1 &mdash; Sorting the Gram-positive bacilli</a>
  <a class="sub-link" href="#gpb-anthracis">10.2 Objective 1 &mdash; <em>Bacillus anthracis</em> and anthrax</a>
  <a class="sub-link" href="#gpb-cereus">10.3 Objective 1 &mdash; <em>Bacillus cereus</em></a>
  <a class="sub-link" href="#gpb-perfringens">10.4 Objective 1 &mdash; <em>Clostridium perfringens</em></a>
  <a class="sub-link" href="#gpb-tetani">10.5 Objective 1 &mdash; <em>Clostridium tetani</em> and tetanus</a>
  <a class="sub-link" href="#gpb-botulinum">10.6 Objective 1 &mdash; <em>Clostridium botulinum</em> and botulism</a>
  <a class="sub-link" href="#gpb-difficile">10.7 Objective 1 &mdash; <em>Clostridioides difficile</em></a>
  <a class="sub-link" href="#gpb-regular">10.8 Objective 1 &mdash; <em>Lactobacillus</em> and <em>Listeria</em></a>
  <a class="sub-link" href="#gpb-diphtheria">10.9 Objective 1 &mdash; <em>Corynebacterium diphtheriae</em></a>
  <a class="sub-link" href="#gpb-cutibacterium">10.10 Objective 1 &mdash; <em>Cutibacterium acnes</em></a>
  <a class="sub-link" href="#gpb-tuberculosis">10.11 Objective 1 &mdash; Mycobacteria and tuberculosis</a>
  <a class="sub-link" href="#gpb-leprosy">10.12 Objective 1 &mdash; <em>Mycobacterium leprae</em> and leprosy</a>
  <a class="sub-link" href="#gpb-actinomycetes">10.13 Objective 1 &mdash; <em>Actinomyces</em> and <em>Nocardia</em></a>
  <a class="sub-link" href="#gpb-transmission">10.14 Objective 2 &mdash; Modes of transmission</a>
  <a class="sub-link" href="#gpb-truth">10.15 Where the slide, the recording and current practice differ</a>
"""

SECTION = """
<section class="deck" id="gram-positive-bacilli">
  <h2 class="deck-title">10 &middot; Gram-Positive Bacilli of Medical Importance</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases,
      clinical manifestations, methods of treatment, and prevention of Gram-positive bacilli of medical
      importance.</li>
      <li>Describe the modes of transmission by which humans acquire Gram-positive bacilli of medical
      importance.</li>
    </ol>
  </div>

  <div class="callout"><strong>Two questions sort the whole lecture.</strong> First: <em>does it form
  endospores?</em> If yes, it is <em>Bacillus</em> (aerobic, catalase positive, <strong>central</strong>
  spore) or <em>Clostridium</em> (anaerobic, catalase negative, <strong>terminal</strong> spore). Second, for
  the non-spore-formers: <em>regular or irregular?</em> Regular rods stain uniformly and keep one shape
  (<em>Lactobacillus</em>, <em>Listeria</em>, <em>Erysipelothrix</em>); irregular rods are pleomorphic and
  stain unevenly (<em>Corynebacterium</em>, <em>Cutibacterium</em>, the acid-fast <em>Mycobacterium</em>,
  and the filamentous <em>Actinomyces</em> and <em>Nocardia</em>). The syllabus points to its Appendix 2
  organism list for this lecture (slide 3 reproduces it, with <em>Cutibacterium</em> and
  <em>Mycobacterium leprae</em> added). Objective 1 is answered organism by organism in 10.1&ndash;10.13,
  each against the objective&rsquo;s own headings; objective 2 is drawn together in 10.14.</div>

<!--MICROL10AUDIO-->
  <div class="prof-flag" id="gpb-audio"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 2 October 2026</span>
  <p>About 90 minutes with Dr. Webster, in two parts (46 and 44 minutes). <b>Both transcripts read and
  compared</b> (Notability&rsquo;s own and an independent local transcription); every quote below appears in
  both unless marked. The recording begins at slide 6, so the title, objective, organism-list and scheme
  slides (1&ndash;5) have no audio. Unlike her Exam 1 lectures, <b>this one signposts often</b> &mdash; and it
  states two rules that cut the scope of the whole lecture.</p>
  <table>
    <tr><th>What was said</th><th>What it means for you</th></tr>
    <tr><td><em>&ldquo;By the way <mark class="prof-highlight">I&rsquo;m not going to be testing you on the
    percentages</mark>. But you do need to know what is the most common, what&rsquo;s the deadliest, how the
    different things work.&rdquo;</em> [part 1, 12:34]</td>
    <td>Mortality rates, case counts and outbreak years are context, not exam material. What <em>is</em>
    examinable: the most common form, the deadliest form, and the mechanism.</td></tr>
    <tr><td><em>&ldquo;By the way, <mark class="prof-highlight">I&rsquo;m not going to be asking you what
    antibiotics to use</mark> to treat these things because that&rsquo;s what we have our PDRs [Physicians&rsquo;
    Desk References] for.&rdquo;</em> [part 2, 8:03]</td>
    <td>The drug names on the treatment slides are not examinable. The other treatment methods are:
    antitoxin, debridement, hyperbaric oxygen, ventilator support, fecal microbiota transplant, hardware
    removal, treatment length, and the vaccines.</td></tr>
    <tr><td><em>&ldquo;You need to know the different forms and what they do. So most cases of anthrax are
    cutaneous&hellip;&rdquo;</em> [part 1, 8:49] and of pulmonary anthrax: <em>&ldquo;this is <mark
    class="prof-highlight">the most deadly form of anthrax. You need to know that</mark>.&rdquo;</em> [part 1, 11:41]</td>
    <td>Cutaneous = most common; pulmonary (woolsorters&rsquo; disease) = most deadly (10.2).</td></tr>
    <tr><td><em>&ldquo;You do need to know that <mark class="prof-highlight">bacillus centrally located,
    Clostridium terminally located</mark>.&rdquo;</em> [part 1, 21:16]</td>
    <td>Spore position is a diagnostic characteristic (10.1). The <em>Clostridioides difficile</em>
    terminal spores &ldquo;look like a little tennis racket&rdquo; (Notability; the local transcript heard
    &ldquo;tennis ball&rdquo;). [part 1, 44:24]</td></tr>
    <tr><td>Gas gangrene: <em>&ldquo;caused by Clostridium perfringens most commonly and <mark
    class="prof-highlight">that would be the one I would want you to know</mark>.&rdquo;</em> [part 1, 20:48]
    Then <em>&ldquo;you need a mixed infection. You need a mixed infection&rdquo;</em> [part 1, 22:16] &mdash;
    prefaced in the local transcript by &ldquo;underline this&rdquo;.</td>
    <td>The organism, and why a mixed infection matters: aerobes use up the oxygen so the anaerobic
    spores can grow (10.4).</td></tr>
    <tr><td>The myonecrosis toxins: <em>&ldquo;at least 17 different ones and <mark
    class="prof-highlight">I&rsquo;m not going to ask you to name them</mark>, but look at the things they
    do.&rdquo;</em> [part 1, 24:39]</td>
    <td>Know the effects (red cells ruptured, white cells destroyed, connective tissue broken down by
    collagenase and hyaluronidase), not the toxin names.</td></tr>
    <tr><td><em>&ldquo;So, but <mark class="prof-highlight">remember floppy baby syndrome</mark>.&rdquo;</em>
    [part 1, 36:05]</td>
    <td>Infant botulism: ingested spores germinate in the infant gut; flaccid paralysis (10.6).</td></tr>
    <tr><td><em>Erysipelothrix</em>: <em>&ldquo;You&rsquo;re not going to need to worry too much about that
    one&rdquo;</em> [part 2, 0:24] and <em>&ldquo;this is the one I&rsquo;m not really going to worry too much
    about&rdquo;</em> [part 2, 9:11]. Notability hears the first as <em>&ldquo;I&rsquo;m not testing you on
    that&rdquo;</em>; the local transcript as &ldquo;not stressing you on that&rdquo;.</td>
    <td>Slides 57&ndash;58 are kept in 10.8 for completeness; no quiz question is built on them.</td></tr>
    <tr><td>Diphtheria: the pseudomembrane <em>&ldquo;is very characteristic of, for a diagnosis of this
    organism <mark class="prof-highlight">that you should know</mark>.&rdquo;</em> [part 2, 13:48]</td>
    <td>Pseudomembrane in the throat = respiratory diphtheria (10.9).</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">You need to know the new name</mark> because this has been
    relatively recently reclassified. Propionibacterium is now called Cutibacterium.&rdquo;</em>
    [part 2, 16:02] (She also said slide 59 still carries the old name and that she would correct and
    repost the deck.)</td>
    <td><em>Cutibacterium acnes</em> (10.10).</td></tr>
    <tr><td>The <em>Mycobacterium</em> species table (slide 68): <em>&ldquo;Another chart I am not asking
    you to memorize.&rdquo;</em> [part 2, 20:58]</td>
    <td>Know that many species exist and that non-tuberculous species trouble the immunosuppressed; do not
    learn the table.</td></tr>
    <tr><td><em>&ldquo;Clinical tuberculosis is divided into <mark class="prof-highlight">three different
    stages that you need to know</mark>.&rdquo;</em> [part 2, 24:39]</td>
    <td>Primary, secondary (reactivation or reinfection), disseminated (extrapulmonary) (10.11).</td></tr>
    <tr><td>The non-tuberculous mycobacteria (slide 90): <em>&ldquo;<mark class="prof-highlight">don&rsquo;t
    worry about being tested</mark> but just to show you&rdquo;</em> [part 2, 38:14]</td>
    <td>Slide 90 is context only; it is summarized in 10.11 and no question is built on it.</td></tr>
    <tr><td><em>Actinomyces israelii</em>: <em>&ldquo;this is one <mark class="prof-highlight">that you should
    know</mark> because it is normally it&rsquo;s a harmless organism because it&rsquo;s superficial; when it
    is no longer superficial is when you have an issue with it.&rdquo;</em> [part 2, 41:38]</td>
    <td>Disease follows access to deeper tissue (10.13).</td></tr>
  </table>
  <p><b>Things said that are not on a slide</b> &mdash; consistent with the deck, useful as hooks, each
  present in both transcripts:</p>
  <ul>
    <li><b>Hydrogen peroxide in a deep puncture wound</b>: flooded deep into the wound, the catalase in your
    tissues releases oxygen, which inhibits the anaerobic clostridia; on a surface wound it mostly lifts dirt
    by bubbling. [part 1, 23:16&ndash;23:50]</li>
    <li>The rusty nail: <b>&ldquo;the rust has nothing to do with it&rdquo;</b> &mdash; the danger is the
    puncture wound. [part 1, 27:51]</li>
    <li>Why boiling home-canned food for 10 minutes works: <b>the botulinum toxin is sensitive to heat even
    though the spore is not</b>. [part 1, 39:03]</li>
    <li>Why infants and not adults: the infant digestive system is immature, so swallowed spores meet the
    anaerobic conditions that let them germinate. [part 1, 34:20]</li>
    <li>The Mantoux test is read at 48&ndash;72 hours <b>because it is a type IV (delayed) hypersensitivity
    reaction</b> &mdash; the link back to Lecture 7. [part 2, 28:08]</li>
    <li><em>Cutibacterium</em>: routine cultures used to be read at one to two days and thrown away, so a
    growth that takes more than six days was missed. [part 2, 17:50]</li>
    <li>Leprosy spreads with prolonged close living, <b>not casual contact</b>. [part 2, 33:35]</li>
    <li><em>Actinomyces viscosus</em> in the mouth is why patients with heart conditions or implants take
    antibiotic prophylaxis before dental work. [part 2, 42:15]</li>
  </ul>
  <p class="muted"><b>One slip to ignore.</b> Summing up tetanus she said &ldquo;just blocking the release of
  the neuromuscular junction&rdquo; [part 1, 29:14] (both transcripts). That is botulism&rsquo;s mechanism.
  Tetanospasmin blocks the <em>inhibitory</em> transmitters from spinal neurons (slides 29&ndash;30), which is
  why tetanus is spastic and botulism flaccid. See 10.5.</p>
  </div>
<!--/MICROL10AUDIO-->

  <h3 class="sub" id="gpb-sorting">10.1 &middot; Objective 1 &mdash; Sorting the Gram-positive bacilli</h3>
  <p>The medically important Gram-positive bacilli divide into three general groups on two properties,
  <strong>the presence or absence of endospores and acid-fastness</strong>: the endospore-formers, the
  non-endospore-formers, and those of irregular shape and staining.</p>
  """ + fig("l10-s05-differentiation-scheme.png", 894, 385,
      "Flow chart: Gram-positive rods divide into sporeformers and non-sporeformers. Sporeformers split into aerobic or facultative anaerobes (Bacillus) and obligate anaerobes (Clostridium). Non-sporeformers split into regular shape and staining (Listeria, Erysipelothrix) and irregular, which divide into non-acid-fast (Corynebacterium, Propionibacterium), acid-fast (Mycobacterium) and filamentous branching cells (Actinomyces, Nocardia).",
      "The whole lecture on one slide (Table 19.1). Read it top down: <b>spores?</b> then, for the "
      "spore-formers, <b>oxygen</b> (aerobic or facultative <em>Bacillus</em> against obligately anaerobic "
      "<em>Clostridium</em>); for the non-spore-formers, <b>regular or irregular</b>, and for the irregular "
      "ones, <b>acid-fast or not, filamentous or not</b>. <em>Propionibacterium</em> is now "
      "<em>Cutibacterium</em>.", 5) + """
  <table>
    <tr><th></th><th>Genus <em>Bacillus</em></th><th>Genus <em>Clostridium</em></th></tr>
    <tr><td>Shape and stain</td><td>Gram-positive, endospore-forming, motile rods</td><td>Gram-positive, spore-forming rods</td></tr>
    <tr><td>Spore position</td><td><mark class="prof-highlight"><strong>Central</strong></mark> (a diagnostic characteristic)</td><td><mark class="prof-highlight"><strong>Terminal</strong></mark>; oval or spherical spores produced <strong>only under anaerobic conditions</strong></td></tr>
    <tr><td>Oxygen and catalase</td><td><strong>Aerobic</strong> (aerobic or facultatively anaerobic in the scheme), <strong>catalase positive</strong></td><td><strong>Anaerobic</strong>, <strong>catalase negative</strong></td></tr>
    <tr><td>Habitat and lifestyle</td><td>Mostly saprobic; primary habitat <strong>soil</strong>; versatile in degrading complex macromolecules</td><td>About 120 species; spores in soil, skin, intestine and vagina; opportunistic pathogens</td></tr>
    <tr><td>Products</td><td>Antibiotics: gramicidin, tyrocidine, <strong>bacitracin</strong>, mycobacillin, surfactin, bacilysin, subtilin</td><td>Organic acids, alcohols and <strong>exotoxins among the most toxic substances on earth</strong></td></tr>
    <tr><td>Infections</td><td>Two species of medical importance: <em>B. anthracis</em>, <em>B. cereus</em></td><td>Two types: <strong>wound and tissue infections</strong>, and <strong>food intoxications</strong></td></tr>
  </table>
  <p>The spore-forming genera are <em>Bacillus</em>, <em>Clostridium</em>, <em>Clostridioides</em> and
  <em>Sporolactobacillus</em> (not pathogenic; a potential probiotic).</p>
  """ + fig("l10-s08-anthracis-central-spores.png", 592, 407,
      "Left, a drawing of a chain of rods with a spore in the middle of each vegetative cell; right, a stained chain of rods in which the spores show as unstained ovals in the center of each cell.",
      "<b>Central spores, the <em>Bacillus</em> pattern.</b> <em>Bacillus anthracis</em> in chains: the vegetative "
      "cell takes up the stain and the spore, sitting in the middle of the cell, does not.", 8) + """
  """ + fig("l10-s28-tetani-terminal-spores.jpg", 642, 460,
      "Left, a drawing of rods with round spores swelling one end; right, stained rods on a yellow background, many with a red round spore at one end.",
      "<b>Terminal spores, the <em>Clostridium</em> pattern.</b> <em>Clostridium tetani</em>: the spore swells one end "
      "of the rod (the drumstick, or &ldquo;tennis racket&rdquo;). Compare the central spore above.", 28, mh=True) + """
  <p><strong>Regular</strong> non-spore-forming rods stain uniformly and do not assume pleomorphic shapes
  (<em>Lactobacillus</em>, <em>Listeria monocytogenes</em>, <em>Erysipelothrix rhusiopathiae</em>).
  <strong>Irregular</strong> ones are pleomorphic and stain unevenly; the deck says all produce catalase and
  their cell walls have mycolic acids and a unique peptidoglycan (<em>Corynebacterium</em>,
  <em>Propionibacterium</em>/<em>Cutibacterium</em>, <em>Mycobacterium</em>, <em>Actinomyces</em>,
  <em>Nocardia</em>) &mdash; see 10.15 for the exceptions. <strong>Corynebacterium and Mycobacterium share
  mycolic acids</strong> in the wall.</p>

  <h3 class="sub" id="gpb-anthracis">10.2 &middot; Objective 1 &mdash; <em>Bacillus anthracis</em> and anthrax</h3>
  <table>
    <tr><th>Heading</th><th><em>Bacillus anthracis</em></th></tr>
    <tr><td>Significance</td><td>The organism with which <strong>Koch&rsquo;s postulates</strong> were established (isolate it from every case, grow it in pure culture, reproduce the disease, re-isolate it)</td></tr>
    <tr><td>Morphology</td><td><strong>Large, block-shaped rods</strong> in chains, with <strong>central spores</strong></td></tr>
    <tr><td>Disease</td><td>Anthrax, a <strong>zoonotic</strong> infection</td></tr>
    <tr><td>Why it worries us</td><td><strong>Category A priority pathogen &mdash; a potential weapon of bioterrorism</strong>; an accidental release from a Soviet bioweapon facility in 1979 was highly fatal</td></tr>
    <tr><td>Virulence: capsule</td><td>A <strong>polypeptide capsule</strong> that makes the cell hard for phagocytes to engulf</td></tr>
    <tr><td>Virulence: the three-part exotoxin</td><td><strong>Protective antigen</strong> binds host cells and creates a <strong>receptor site for the other two components</strong>. <strong>Edema factor</strong> impairs phagocytosis and inhibits tumor necrosis factor and interleukin 6 production by monocytes. <strong>Lethal factor</strong>: at low levels it inhibits release of interleukin 1 and tumor necrosis factor alpha, damping the immune response; at <strong>high levels it lyses macrophages</strong>, releasing high levels of interleukin 1, tumor necrosis factor alpha and nitric oxide. <strong>Excessive release of these cytokines can trigger a massive inflammatory response and the shock cascade, like septic shock.</strong></td></tr>
  </table>
  <table>
    <tr><th>Form</th><th>How it is acquired</th><th>What happens</th></tr>
    <tr><td><mark class="prof-highlight"><strong>Cutaneous</strong> &mdash; the most common form</mark> (about 95% of human cases)</td><td>Spores enter through <strong>cuts or incisions in the skin</strong>, germinate in the tissue and grow</td><td>A <strong>painless papule</strong> that rapidly becomes an <strong>ulcer surrounded by vesicles</strong> and finally a <strong>black necrotic eschar</strong></td></tr>
    <tr><td>Injection</td><td>Injecting contaminated heroin; identified in addicts in northern Europe, not yet in the United States</td><td>Like cutaneous anthrax, but the infection is <strong>in the deep muscle where the drug was injected</strong>, so it spreads faster and is harder to recognize and treat</td></tr>
    <tr><td><mark class="prof-highlight"><strong>Pulmonary</strong> (woolsorters&rsquo; disease) &mdash; the most deadly form</mark></td><td><strong>Inhaling spores</strong> from infected animal products (wool of infected sheep) or soil</td><td>May be latent for two months or more. Alveolar macrophages engulf the spores and the <strong>exotoxins kill the macrophages en masse</strong>: cough, headache, fever, chills, vomiting, chest and abdominal pain, then worsening fever, edema, capillary thrombosis and cardiovascular shock; about half develop meningitis. Untreated, nearly always fatal within about three days of symptoms</td></tr>
    <tr><td>Gastrointestinal</td><td><strong>Eating meat from an infected animal</strong></td><td>Ulcers of the mouth and esophagus, localized lymphadenopathy; nausea, vomiting and malaise if the upper intestine is invaded; sepsis if the large intestine is invaded</td></tr>
    <tr><td>Meningitis</td><td>A complication of <strong>any</strong> form; up to half of pulmonary cases</td><td>Typical meningitis: altered mental status, headache, fever, nausea and vomiting, seizures</td></tr>
  </table>
  """ + fig("l10-s11-cutaneous-anthrax-eschar.png", 582, 430,
      "Two photographs of a man's jaw and neck with a large black crusted lesion over red, swollen skin.",
      "<b>The eschar.</b> Cutaneous anthrax at its end stage: the black necrotic crust over swollen, inflamed "
      "skin, which began as a painless papule at a cut.", 11) + """
  <p><strong>Treatment and prevention.</strong> Treated with antibiotics; <strong>pulmonary anthrax is also
  treated with antitoxin</strong> to neutralize the toxins. Livestock are protected with live spores and
  toxoid. The human vaccine, <strong>Biothrax, is a purified toxoid</strong> given to <strong>high-risk
  occupations and military personnel</strong>, not to anyone under 18 or over 65; a primary series with
  annual boosters, and a three-dose series with antibiotics after exposure. Its side effects have prompted
  research into alternative vaccines (see 10.15).</p>

  <h3 class="sub" id="gpb-cereus">10.3 &middot; Objective 1 &mdash; <em>Bacillus cereus</em></h3>
  <table>
    <tr><th>Heading</th><th><em>Bacillus cereus</em></th></tr>
    <tr><td>Disease</td><td><strong>Most commonly a foodborne illness</strong>; spores are very commonly airborne and dustborne</td></tr>
    <tr><td>Foods</td><td>Grows in rice, potatoes and meat; <strong>the spores survive cooking and reheating</strong> (the risk is cooked food left out before refrigerating)</td></tr>
    <tr><td>Toxins</td><td>Symptoms are due to exotoxin. <strong>Diarrheal form: a large molecular weight protein. Emetic (vomiting) form: a low molecular weight, heat-stable peptide.</strong></td></tr>
    <tr><td>Course and treatment</td><td>About <strong>24 hours</strong>; <strong>no treatment</strong></td></tr>
    <tr><td>Other infections</td><td>Severe eye infections, progressive pneumonia, nosocomial post-surgical infections; rare <strong>clinical sepsis from contaminated injection sites traced to contaminated alcohol prep pads</strong>. Increasingly reported in the immunosuppressed; may resist beta-lactam antibiotics; new, sometimes highly pathogenic strains in the <em>B. cereus</em> group can be misidentified, delaying treatment</td></tr>
    <tr><td>Welder&rsquo;s anthrax</td><td>A recently recognized disease of metal workers: <strong>anthrax toxins have been identified, but they are produced by <em>Bacillus cereus</em></strong>. Metal fume inhalation may predispose</td></tr>
  </table>

  <h3 class="sub" id="gpb-perfringens">10.4 &middot; Objective 1 &mdash; <em>Clostridium perfringens</em>: gas gangrene and food poisoning</h3>
  <table>
    <tr><th>Heading</th><th>Myonecrosis (anaerobic cellulitis) / gas gangrene</th></tr>
    <tr><td>Organism</td><td><mark class="prof-highlight"><strong><em>Clostridium perfringens</em> is the most common cause</strong></mark>; <em>C. novyi</em>, <em>C. septicum</em> and other species can also cause it</td></tr>
    <tr><td>Source</td><td>Spores in soil, human skin, intestine and vagina; about 90% of contaminated wounds carry the organism but only about 2% develop myonecrosis &mdash; <strong>host factors</strong></td></tr>
    <tr><td>Predisposing wounds</td><td>Surgical incisions, <strong>compound fractures</strong>, diabetic ulcers, septic abortions, puncture wounds, gunshot wounds</td></tr>
    <tr><td>Why a mixed infection</td><td><mark class="prof-highlight">Aerobic bacteria in the wound <strong>use up the oxygen</strong>, producing the low oxygen tension the anaerobes need to grow</mark></td></tr>
    <tr><td>Pathology</td><td><strong>Not highly invasive: it requires damaged, dead tissue and anaerobic conditions.</strong> These stimulate spore germination, vegetative growth and release of exotoxins and other virulence factors. <strong>Fermentation of muscle carbohydrates forms the gas</strong> and destroys more tissue</td></tr>
    <tr><td>Virulence factors</td><td>At least 17 toxins (names not examinable): one ruptures red blood cells and causes edema and tissue destruction, another destroys white blood cells. Enzymes: <strong>collagenase, hyaluronidase</strong> and deoxyribonuclease, which break down connective tissue and let the infection spread</td></tr>
    <tr><td>Extent</td><td><strong>Anaerobic cellulitis</strong>: gas and tissue damage, but it <strong>stays localized</strong>. <strong>True myonecrosis</strong>: the local infection leads to <strong>spreading tissue damage with fever, tachycardia and blackened necrotic tissue</strong></td></tr>
    <tr><td>Treatment</td><td>Debridement of diseased tissue (difficult if intestinal), possibly amputation, large doses of antibiotics, and <strong>hyperbaric oxygen</strong>, which floods the tissue with oxygen and <strong>inhibits the anaerobe</strong></td></tr>
    <tr><td>Prevention</td><td><strong>Immediate cleansing</strong> of dirty wounds, deep wounds, compound fractures and infected incisions. <strong>No vaccine is available.</strong></td></tr>
  </table>
  """ + fig("l10-s25-gas-gangrene-muscle.png", 647, 380,
      "A micrograph and matching drawing of muscle fibers separated by gas-filled spaces, with dark rod-shaped Clostridium cells among them.",
      "<b>Why it is called gas gangrene.</b> <em>Clostridium</em> rods between muscle fibers, with the "
      "gas-filled spaces left by fermentation of muscle carbohydrate.", 25, mh=True) + """
  <p><strong>Clostridial food poisoning compared.</strong> <em>Clostridium botulinum</em> causes a
  <strong>rare but severe</strong> intoxication, usually from home-canned food (10.6). <em>Clostridium
  perfringens</em> causes a <strong>mild intestinal illness</strong> and is a very common food poisoning.
  In <em>C. perfringens</em> gastroenteritis the foods most commonly involved are <strong>meat, fish and
  undercooked vegetables</strong>: spores survive cooking that was not thorough enough, germinate and
  multiply (especially if the food is unrefrigerated), and once eaten <strong>the toxin is produced in the
  intestine</strong>, acting on epithelial cells &mdash; acute abdominal pain, diarrhea and nausea, with
  <strong>rapid recovery</strong>.</p>

  <h3 class="sub" id="gpb-tetani">10.5 &middot; Objective 1 &mdash; <em>Clostridium tetani</em> and tetanus</h3>
  <table>
    <tr><th>Heading</th><th><em>Clostridium tetani</em></th></tr>
    <tr><td>Habitat and disease</td><td>A common resident of soil and the gastrointestinal tracts of animals; causes <strong>tetanus (lockjaw)</strong>, a neuromuscular disease. A <strong>strict anaerobe</strong>: low oxygen tension is needed to germinate the spores and make toxin</td></tr>
    <tr><td>Who gets it</td><td>Most commonly <strong>older (geriatric) patients and intravenous drug users</strong>; <strong>neonates in developing countries</strong></td></tr>
    <tr><td>Entry</td><td>Spores usually enter through <strong>accidental puncture wounds</strong>, also burns, <strong>umbilical stumps</strong> (neonatal tetanus), frostbite and crushed body parts</td></tr>
    <tr><td>Incubation</td><td>4&ndash;10 days; <strong>the shorter the incubation, the more serious the disease</strong>. Delayed care, short incubation and head wounds worsen the outlook</td></tr>
    <tr><td>Mechanism</td><td><strong>Tetanospasmin</strong>, a neurotoxin, enters at motor nerve endings and acts on the spinal inhibitory neurons, <strong>blocking release of the inhibitory transmitters gamma-aminobutyric acid and glycine</strong>, so <strong>muscles contract uncontrollably</strong> (risus sardonicus, arching spasms)</td></tr>
    <tr><td>Death</td><td>Most often from <strong>respiratory failure</strong>, as spasm of the breathing muscles and larynx stops effective breathing (the slide calls the toxin&rsquo;s effect paralysis; tetanus causes spasm, not flaccid paralysis)</td></tr>
    <tr><td>Treatment</td><td>Aimed at the toxemia and the infection and at maintaining homeostasis: <strong>antitoxin (human tetanus immune globulin) inactivates circulating toxin but does not counteract toxin already bound</strong>; antibiotics for the infection; muscle relaxants</td></tr>
    <tr><td>Prevention</td><td>A vaccine; <strong>a booster every 10 years</strong></td></tr>
  </table>
  """ + fig("l10-s30-tetanus-spinal-neuron.png", 761, 372,
      "Three panels: tetanospasmin traveling from a wound in the foot up a nerve to the spinal cord; a spinal cord cross-section with toxin molecules on a spinal inhibitory neuron supplying extensor and flexor muscles; a man with a fixed grin labeled risus sardonicus and tensed muscles.",
      "<b>The events in tetanus.</b> Toxin from the wound travels to the spinal cord and blocks the "
      "<em>regulatory</em> function of the spinal inhibitory neuron, so opposing muscles contract together "
      "&mdash; the fixed grin of risus sardonicus. Contrast botulism (10.6), where the block is at the "
      "neuromuscular junction itself.", 30) + """

  <h3 class="sub" id="gpb-botulinum">10.6 &middot; Objective 1 &mdash; <em>Clostridium botulinum</em> and botulism</h3>
  <p><strong>Botulism is an intoxication associated with inadequate food preservation.</strong> <em>C.
  botulinum</em> is a spore-forming anaerobe of soil and water. Foodborne botulism is <strong>most prevalent
  with low-acid, home-canned foods</strong> (green beans, corn), but meats, fish and dairy can carry it, and
  rarely commercial foods (the 2007 Castleberry chili sauce outbreak). <strong>Pathogenesis:</strong> spores
  are on the food when it is gathered; <strong>if reliable temperature and pressure are not achieved, the air
  is evacuated but the spores remain</strong>; anaerobic conditions favor germination and growth; the toxin,
  botulin, is released and carried to neuromuscular junctions, where <strong>it blocks the release of
  acetylcholine</strong>, needed for muscle contraction.</p>
  """ + fig("l10-s36-botulin-neuromuscular-junction.jpg", 433, 600,
      "Three-step drawing of a motor neuron end plate on a muscle cell: normal release of acetylcholine from vacuoles into the synapse, then botulin molecules at the presynaptic membrane with no acetylcholine released.",
      "<b>Botulin at the neuromuscular junction.</b> (a, b) Vacuoles normally release acetylcholine into the "
      "synapse; (c) botulin blocks the release, so the muscle cannot contract and the paralysis is "
      "<em>flaccid</em>.", 36, mh=True) + """
  <table>
    <tr><th>Heading</th><th>Botulism</th></tr>
    <tr><td>Symptoms</td><td><strong>Double or blurred vision, difficulty swallowing, dizziness</strong>; sometimes nausea and vomiting; <strong>descending muscular paralysis</strong>; respiratory compromise</td></tr>
    <tr><td>Outcome</td><td>Mortality has fallen <strong>because ventilators support breathing</strong> through the paralysis</td></tr>
    <tr><td>Diagnosis and treatment</td><td>Find the toxin in the food, intestinal contents or feces; give <strong>antitoxin with cardiac and respiratory support</strong></td></tr>
    <tr><td>Prevention</td><td>Proper preserving and handling of canned foods (sodium nitrite, salt or vinegar as preservatives); <strong>discard bulging cans</strong>; <strong>boil home-bottled foods for at least 10 minutes</strong></td></tr>
  </table>
  <table>
    <tr><th>Form</th><th>How it arises</th></tr>
    <tr><td><mark class="prof-highlight"><strong>Infant botulism</strong> &mdash; the most common form</mark> (up to 80% of cases each year; 66% in the 2021 national survey)</td><td><strong>Ingested spores germinate and release toxin</strong> in the infant gut; flaccid paralysis, <strong>&ldquo;floppy baby syndrome&rdquo;</strong>. Associated with <strong>honey</strong> or homemade baby food (honey pacifiers from Mexico, 2018; a contaminated baby formula outbreak, 2026)</td></tr>
    <tr><td>Foodborne</td><td>Eating toxin made in improperly preserved, usually home-canned, food</td></tr>
    <tr><td>Wound</td><td>Spores enter a wound and cause the food poisoning symptoms; <strong>intravenous drug users, often with black tar heroin</strong></td></tr>
    <tr><td>Iatrogenic</td><td><strong>Cosmetic or therapeutic procedures using botulinum toxin cause systemic intoxication</strong></td></tr>
    <tr><td>Intestinal colonization</td><td>A person <strong>over age 1</strong> harbors the toxin in the intestinal tract</td></tr>
  </table>
  """ + fig("l10-s38-floppy-baby.png", 255, 198,
      "An infant held face down over an adult's hand, arms and legs hanging limp.",
      "<b>Floppy baby syndrome.</b> Infant botulism: no muscle tone, the limbs hanging limp. The rigid, "
      "arched newborn of neonatal tetanus (slide 31) is its spastic opposite.", 38) + """

  <h3 class="sub" id="gpb-difficile">10.7 &middot; Objective 1 &mdash; <em>Clostridioides difficile</em></h3>
  <table>
    <tr><th>Heading</th><th><em>Clostridioides difficile</em></th></tr>
    <tr><td>Name</td><td>Formerly <em>Clostridium</em>, but <strong>differentiated by ribonucleic acid sequencing</strong> into its own genus</td></tr>
    <tr><td>Habitat</td><td>A <strong>normal resident of the colon in low numbers</strong>; relatively non-invasive</td></tr>
    <tr><td>Pathogenesis</td><td><strong>Broad-spectrum antibiotics kill the other bacteria</strong>, letting it overgrow; it <strong>produces enterotoxins that damage the intestines</strong></td></tr>
    <tr><td>Disease</td><td><em>C. difficile</em>-associated disease: <strong>antibiotic-associated (pseudomembranous) colitis, toxic megacolon, perforation of the colon</strong>. A <strong>major cause of diarrhea in hospitals</strong>; increasingly common in community-acquired diarrhea; a 2005 strain makes far more exotoxin; named one of the top three antibiotic-related threats (with carbapenem-resistant Enterobacterales and drug-resistant gonorrhea)</td></tr>
    <tr><td>Populations at risk</td><td>Antibiotic exposure (70% of cases used antibiotics in the prior 12 weeks); gastrointestinal surgery; long stays in healthcare settings; serious underlying illness; immunocompromise; advanced age; <strong>gastric acid inhibitors such as famotidine (Pepcid) and omeprazole (Prilosec)</strong>; trehalose sugar</td></tr>
    <tr><td>Progression</td><td>Watery diarrhea, fever, loss of appetite, nausea, abdominal pain and tenderness, then <strong>the intestinal lining becomes necrotic and sloughs off as the pseudomembrane</strong>, and the wall can perforate</td></tr>
    <tr><td>Treatment</td><td><strong>Mild cases: fluid and electrolyte replacement and withdrawal of the antimicrobial</strong> (withdrawing the inciting antimicrobial is part of managing every case). Severe cases: oral antibiotics (see 10.15). <strong>Fecal microbiota transplant</strong>: donor cultures by colonoscope or nasogastric tube, or as capsules, <strong>restoring the normal flora</strong> (as much as 90% effective)</td></tr>
    <tr><td>Prevention</td><td>Increased precautions to prevent spread</td></tr>
  </table>
  """ + fig("l10-s47-pseudomembranous-colitis.png", 269, 432,
      "Two colonoscopy views: above, a normal pink colon; below, colon lining dotted with raised yellow-white plaques marked by arrows.",
      "<b>Pseudomembranous colitis.</b> (a) Normal colon; (b) the raised yellow-white plaques of "
      "antibiotic-associated colitis &mdash; sloughed, necrotic intestinal lining.", 47) + """

  <h3 class="sub" id="gpb-regular">10.8 &middot; Objective 1 &mdash; Regular non-spore-formers: <em>Lactobacillus</em> and <em>Listeria</em></h3>
  <p><strong><em>Lactobacillus</em></strong> (<em>L. acidophilus</em>, <em>L. salivarius</em>, <em>L.
  fermentum</em>) is beneficial normal flora of the intestinal and vaginal tracts. <strong>It produces lactic
  acid, acetic acid, hydrogen peroxide and other antimicrobial substances that inhibit pathogens.</strong>
  <strong>Antibiotic therapy can interrupt its activity and allow a superinfection by an
  opportunist</strong> (the recording&rsquo;s example: a vaginal yeast infection).</p>
  <table>
    <tr><th>Heading</th><th><em>Listeria monocytogenes</em></th></tr>
    <tr><td>Morphology</td><td>Non-spore-forming Gram-positive, ranging <strong>from coccobacilli to long filaments</strong>; 1&ndash;4 flagella; <strong>no capsule</strong></td></tr>
    <tr><td>Hardiness</td><td>Resistant to cold, heat, salt, pH extremes and bile (but killed by pasteurization and cooking)</td></tr>
    <tr><td>Virulence</td><td>Induces phagocytosis and then <strong>replicates in the cytoplasm of host cells</strong>, which lets it <strong>avoid the humoral immune system</strong></td></tr>
    <tr><td>Reservoir</td><td>Primary reservoir <strong>soil and water</strong>; animal intestines</td></tr>
    <tr><td>Food</td><td>Contaminates foods and <strong>grows during refrigeration</strong>. Most listeriosis comes from <strong>dairy products, poultry and meat</strong> (found in 12% of ground beef and 15% of chicken tested); the most recent outbreak was dairy</td></tr>
    <tr><td>Disease</td><td>Often mild or subclinical in healthy adults (fever, diarrhea, sore throat). In <strong>immunocompromised patients, fetuses and neonates it affects the brain and meninges</strong>, with fetal loss and newborn deaths</td></tr>
    <tr><td>Diagnosis</td><td><strong>Culture requires a lengthy cold enrichment process</strong>; rapid tests by enzyme-linked immunosorbent assay, immunofluorescence and nucleic acid analysis</td></tr>
    <tr><td>Prevention</td><td><strong>Pasteurization and cooking</strong> (refrigeration does not stop it)</td></tr>
  </table>
  """ + fig("l10-s54-listeria-cycle.png", 335, 574,
      "Drawing of two intestinal cells: a rod is being engulfed at the surface, rods sit in vacuoles and free in the cytoplasm, and one rod pushes from one cell into the next.",
      "<b>How <em>Listeria</em> stays out of reach of antibody.</b> (a) It induces its own uptake, (b) escapes the "
      "vacuole, (c) multiplies in the cytoplasm, and (d) passes directly into the neighboring cell without "
      "ever leaving the cells.", 54) + """
  <p class="muted"><em>Erysipelothrix rhusiopathiae</em> (slides 57&ndash;58; de-emphasized in the recording):
  a Gram-positive rod of animals and the environment whose primary reservoir is <strong>the tonsils of healthy
  pigs</strong>; it enters through skin abrasions and produces erysipeloid, dark red lesions on the hand; rarely
  septicemia or endocarditis; pigs are vaccinated.</p>

  <h3 class="sub" id="gpb-diphtheria">10.9 &middot; Objective 1 &mdash; <em>Corynebacterium diphtheriae</em></h3>
  """ + fig("l10-s60-diphtheriae-stain.png", 558, 422,
      "Blue-stained, irregular club-shaped rods, labeled for pleomorphism, a palisade arrangement of rods lying side by side, and dark granules.",
      "<b>Irregular rods.</b> Pleomorphic cells, the <b>palisade</b> arrangement (rods lying side by side, like a "
      "fence, rather than end to end in a chain) and granules.", 60) + """
  <table>
    <tr><th>Heading</th><th>Diphtheria</th></tr>
    <tr><td>Reservoir</td><td><strong>Healthy human carriers</strong>, so the potential for diphtheria is always present; respiratory diphtheria is rare in the United States</td></tr>
    <tr><td>Who gets it</td><td><strong>Non-immunized children</strong> living in crowded, unsanitary conditions</td></tr>
    <tr><td>Transmission</td><td><strong>Respiratory droplets</strong> from carriers or actively infected people</td></tr>
    <tr><td>Forms</td><td>Respiratory (pharyngeal, tonsillar, laryngeal, nasal) or cutaneous (most common in the tropics)</td></tr>
    <tr><td>Stage 1: local infection</td><td>Upper respiratory inflammation: sore throat, nausea, vomiting, swollen lymph nodes. <mark class="prof-highlight">The <strong>pseudomembrane</strong>, from solidified inflammatory fluid, is characteristic</mark> and <strong>can cause asphyxiation</strong></td></tr>
    <tr><td>Stage 2: toxemia</td><td>Diphtherotoxin targets <strong>the heart</strong> (myocarditis, abnormal electrocardiogram) and <strong>the nerves</strong> (muscle weakness, paralysis)</td></tr>
    <tr><td>Diagnosis</td><td>Pseudomembrane and swelling; stain with <strong>alkaline methylene blue</strong>; conditions and history; serological assay</td></tr>
    <tr><td>Treatment</td><td><strong>Antitoxin in horse serum</strong> (since the 1890s), not usually given in non-respiratory cases; it <strong>does not neutralize bound toxin but neutralizes circulating toxin</strong>; antibiotics</td></tr>
    <tr><td>Prevention</td><td>A <strong>toxoid vaccine</strong> series (at 6&ndash;8 weeks, 15 months and school age) <strong>with boosters</strong></td></tr>
  </table>
  """ + fig("l10-s63-diphtheria-pseudomembrane.png", 368, 311,
      "An open mouth with a tongue depressor; a thick off-white membrane coats the back of the throat.",
      "<b>The pseudomembrane.</b> The gray-white membrane over the throat, with swelling, is indicative of "
      "respiratory diphtheria and can obstruct the airway.", 63) + """

  <h3 class="sub" id="gpb-cutibacterium">10.10 &middot; Objective 1 &mdash; <em>Cutibacterium acnes</em></h3>
  <table>
    <tr><th>Heading</th><th><em>Cutibacterium</em> (formerly <em>Propionibacterium</em>) <em>acnes</em></th></tr>
    <tr><td>Name</td><td><mark class="prof-highlight"><strong>The genus <em>Propionibacterium</em> is now <em>Cutibacterium</em></strong></mark>; <em>C. acnes</em> is the most common</td></tr>
    <tr><td>Morphology and growth</td><td>Gram-positive rods; aerotolerant or anaerobic; <strong>slow growing (more than 6 days)</strong>; <strong>nontoxigenic</strong></td></tr>
    <tr><td>Habitat and acne</td><td>A common resident of the <strong>pilosebaceous glands</strong>; causes acne <strong>via inflammatory mediators</strong>, not a toxin</td></tr>
    <tr><td>Implant infections</td><td>Implicated in chronic invasive, implant, endovascular and central nervous system shunt infections. <strong>It forms a biofilm on prosthetics</strong>, raising its tolerance to antibiotics and immune defense</td></tr>
    <tr><td>Diagnosis</td><td><strong>Hard, because it grows so slowly</strong>: fluid from an infected site may show nothing for days, so <strong>prolonged incubation under strict anaerobic conditions</strong> is needed</td></tr>
    <tr><td>Treatment</td><td><strong>The hardware may need to be removed</strong>, with aggressive <strong>debridement</strong>; prolonged antibiotics (often 3&ndash;6 months)</td></tr>
  </table>

  <h3 class="sub" id="gpb-tuberculosis">10.11 &middot; Objective 1 &mdash; Mycobacteria and tuberculosis</h3>
  <p><strong>Mycobacteria are acid-fast bacilli</strong>: Gram-positive irregular rods with <strong>mycolic acids
  and waxes in the wall</strong>, which is why the acid-fast stain (carbol fuchsin) needs heat to drive it in
  and why they Gram stain poorly. They are <strong>strict aerobes</strong>, produce catalase, <strong>form no
  capsules, flagella or spores</strong>, and grow slowly. Non-tuberculous mycobacteria are a problem in the
  immunosuppressed (the species table, slide 68, and the list on slide 90 are context only).</p>
  <table>
    <tr><th>Heading</th><th><em>Mycobacterium tuberculosis</em> (the tubercle bacillus)</th></tr>
    <tr><td>Virulence</td><td><strong>No exotoxins or enzymes</strong> that contribute to infectiousness; <strong>complex waxes and cord factor</strong> prevent destruction by lysosomes and macrophages</td></tr>
    <tr><td>Epidemiology</td><td>Predisposed by poor nutrition, a weakened immune system, poor access to care, lung damage and genetics; about a third of the world carries the bacillus; highest United States rate in recent immigrants. The bacillus is very resistant and is <strong>transmitted by airborne respiratory droplets</strong>; the <strong>infectious dose is about 10 cells</strong></td></tr>
    <tr><td>Infection versus disease</td><td>Only 5&ndash;10% of infected people develop clinical disease. <strong>Inactive (latent) tuberculosis is not contagious, can be detected by a blood or skin test, and may activate at any time.</strong> Untreated disease progresses slowly and mostly stays in the lungs</td></tr>
  </table>
  <table>
    <tr><th><mark class="prof-highlight">The three divisions of clinical tuberculosis</mark></th><th>What happens</th></tr>
    <tr><td><strong>Primary</strong></td><td>Bacilli are phagocytosed by alveolar macrophages and multiply inside them. After 3&ndash;4 weeks the immune system attacks, forming <strong>tubercles: granulomas of a central core of bacilli surrounded by white blood cells</strong>. If the center breaks down into necrotic <strong>caseous lesions, they gradually heal by calcification</strong>. Stimulates a cell-mediated response</td></tr>
    <tr><td><strong>Secondary</strong> (reactivation or reinfection)</td><td>If the patient does not recover, the bacilli reactivate; <strong>tubercles expand and drain into the bronchial tubes</strong> and upper respiratory tract: violent coughing, greenish or bloody sputum, fever, anorexia, weight loss, fatigue &mdash; <strong>&ldquo;consumption&rdquo;, because patients wasted away</strong></td></tr>
    <tr><td><strong>Disseminated</strong> (extrapulmonary)</td><td>Bacilli spread to <strong>regional lymph nodes, kidneys, long bones, the genital tract, brain and meninges</strong>; tuberculous meningitis is grave even when treated</td></tr>
  </table>
  """ + fig("l10-s73-tubercle.jpg", 605, 640,
      "Drawing of a tubercle: a yellow central area of caseous necrosis with bacilli, ringed by epithelioid cells and a multinucleate giant cell, inside a layer of granuloma fibroblast cells.",
      "<b>The tubercle.</b> Caseous necrosis with tubercle bacilli at the center, epithelioid cells and a "
      "multinucleate giant cell around it, walled off by granuloma (fibroblast) cells.", 73, mh=True) + """
  <table>
    <tr><th>Test</th><th>What it is</th></tr>
    <tr><td>Mantoux (tuberculin) test</td><td>Intradermal purified protein derivative; <strong>read at 48&ndash;72 hours</strong> for induration, interpreted by size and the patient&rsquo;s population factors (a delayed, type IV reaction)</td></tr>
    <tr><td>QuantiFERON-TB Gold</td><td>Blood incubated with mycobacterial proteins; measures <strong>release of gamma interferon</strong></td></tr>
    <tr><td>False results</td><td><strong>False positives: prior BCG (bacille Calmette-Guérin) vaccine</strong>, infection by other <em>Mycobacterium</em> species. <strong>False negatives: too early in infection; acquired immunodeficiency syndrome or other immunosuppression, where the patient cannot mount the response</strong></td></tr>
    <tr><td>Sputum and imaging</td><td>Acid-fast stain of sputum, <strong>Ziehl-Neelsen</strong> or fluorescent; laboratory cultivation; nucleic acid probes; chest X-ray for tubercles</td></tr>
  </table>
  <p><strong>Management and prevention.</strong> <strong>6&ndash;24 months of at least two drugs</strong> (a
  one-pill regimen combines three); preventive treatment for those at risk or latently infected. The vaccine
  used in other countries is <strong>the attenuated bacille Calmette-Guérin strain of <em>Mycobacterium
  bovis</em></strong>.</p>

  <h3 class="sub" id="gpb-leprosy">10.12 &middot; Objective 1 &mdash; <em>Mycobacterium leprae</em> and leprosy</h3>
  <table>
    <tr><th>Heading</th><th><em>Mycobacterium leprae</em> (Hansen&rsquo;s bacillus)</th></tr>
    <tr><td>Growth</td><td>A <strong>strict parasite</strong>: it has not been grown on artificial media or in tissue culture, <strong>so armadillos are used</strong>; the <strong>slowest growing</strong> of all species; it <strong>multiplies within host cells in large packets called globi</strong></td></tr>
    <tr><td>Disease</td><td>Leprosy (Hansen&rsquo;s disease), a chronic disease beginning in the skin and mucous membranes and progressing into the nerves</td></tr>
    <tr><td>Transmission</td><td><strong>The mechanism is not fully verified</strong>; <strong>zoonotic transmission from armadillos is possible</strong>. Not highly virulent: health, living conditions and possibly a genetic marker influence susceptibility. Most Florida cases are in Central Florida (the I-4 corridor)</td></tr>
    <tr><td>Course</td><td>Macrophages phagocytize the bacilli but a weakened macrophage or slow T cell response may not kill them. Incubation 2&ndash;5 years; untreated, the bacilli <strong>grow slowly in skin macrophages and the Schwann cells of peripheral nerves</strong></td></tr>
    <tr><td>Diagnosis</td><td>Symptoms, microscopy of lesions and history: <strong>numbness in hands and feet</strong>, loss of heat and cold sensitivity, muscle weakness, thickened earlobes, chronic stuffy nose; <strong>acid-fast bacilli in skin lesions</strong>, nasal discharge and tissue. Where care is scarce, the <strong>feather test</strong> checks skin sensation</td></tr>
    <tr><td>Treatment</td><td>Long-term combined therapy. The slide gives about <strong>6 months for tuberculoid</strong> leprosy and <strong>up to 2 years for lepromatous</strong>, followed by extended single-drug treatment; that is older United States practice. The current United States program uses about 12 months for tuberculoid and about 2 years for lepromatous disease, and the World Health Organization gives all three drugs for both forms (6 and 12 months)</td></tr>
    <tr><td>Prevention</td><td>Constant surveillance of high-risk populations; bacille Calmette-Guérin has limited efficacy; a subunit vaccine is in trials</td></tr>
  </table>
  <table>
    <tr><th></th><th>Tuberculoid</th><th>Lepromatous</th></tr>
    <tr><td>Lesions</td><td><strong>Shallow, asymmetrical</strong> lesions; nerve damage with <strong>local loss of pain reception</strong></td><td><strong>Deeply nodular</strong>, severely disfiguring the face and extremities; <strong>widespread dissemination</strong></td></tr>
    <tr><td>T helper response</td><td><strong>T helper 1</strong> favors it; normal T-cell responsiveness to the bacillus</td><td><strong>T helper 2</strong> favors it; <strong>low or absent T-cell responsiveness</strong></td></tr>
    <tr><td>Organisms and infectivity</td><td>Low to undetectable organisms; low infectivity; granulomas and local inflammation</td><td>Florid growth in macrophages; high infectivity; hypergammaglobulinemia</td></tr>
  </table>
  """ + fig("l10-s84-leprosy-polar-forms.jpg", 892, 1024,
      "Comparison chart of tuberculoid and lepromatous leprosy with tissue micrographs: tuberculoid has few organisms, low infectivity, granulomas and peripheral nerve damage, normal immunoglobulin and normal T-cell response; lepromatous has florid growth in macrophages, high infectivity, disseminated infection, hypergammaglobulinemia and low or absent T-cell response.",
      "<b>The two polar forms</b> (several intermediate forms exist). The severity of lepromatous leprosy "
      "follows from its failed T-cell response: the bacilli grow freely in macrophages.", 84) + """
  """ + fig("l10-s88-feather-test.png", 346, 428,
      "A health worker touches a feather to a boy's arm while the boy looks away.",
      "<b>The feather test.</b> A low-cost check for the lost skin sensation of leprosy where medical care "
      "is scarce: can the patient feel the feather?", 88) + """

  <h3 class="sub" id="gpb-actinomycetes">10.13 &middot; Objective 1 &mdash; <em>Actinomyces</em> and <em>Nocardia</em> (filamentous bacilli)</h3>
  <p>The genera <em>Actinomyces</em> and <em>Nocardia</em> are <strong>nonmotile filamentous bacteria related to
  the mycobacteria</strong>, and may cause chronic infection of skin and soft tissue.</p>
  <table>
    <tr><th>Organism</th><th>Key facts</th></tr>
    <tr><td><em>Actinomyces israelii</em></td><td>A normally harmless resident of the oral cavity, digestive tract and genital tract; <mark class="prof-highlight">it causes chronic, hard-to-diagnose infection <strong>when it gains access to deeper tissues</strong></mark>. <strong>Cervicofacial</strong> disease: a complication of <strong>oral infection</strong>. <strong>Thoracic</strong>: a necrotizing lung disorder. <strong>Abdominal</strong>: a complication of a <strong>burst appendix</strong>, gunshot wounds or ulcers. <strong>Uterine</strong>: a complication of <strong>intrauterine devices</strong>. Treated surgically and with antibiotics</td></tr>
    <tr><td><em>Actinomyces viscosus</em></td><td><strong>Dental caries</strong>, and some cases of <strong>endocarditis</strong></td></tr>
    <tr><td><em>Nocardia</em> (nocardiosis)</td><td>Pulmonary, cutaneous or subcutaneous infections. <strong>Pulmonary nocardiosis resembles tuberculosis</strong>, and lesions may extend through the chest wall and disseminate to the brain and kidneys. Also causes <strong>mycetoma: a granulomatous inflammatory response in the deep dermis and subcutaneous tissue</strong></td></tr>
  </table>

  <h3 class="sub" id="gpb-transmission">10.14 &middot; Objective 2 &mdash; Modes of transmission</h3>
  <table>
    <tr><th>Organism</th><th>How humans acquire it</th></tr>
    <tr><td><em>Bacillus anthracis</em></td><td>A zoonosis from spores: <strong>through a cut</strong> (cutaneous), <strong>inhaled from animal wool or soil</strong> (pulmonary), <strong>eaten in meat from an infected animal</strong> (gastrointestinal), <strong>injected with contaminated heroin</strong> (injection)</td></tr>
    <tr><td><em>Bacillus cereus</em></td><td><strong>Food</strong> (rice, potatoes, meat), from airborne and dustborne spores that survive cooking and reheating; contaminated alcohol prep pads at injection sites</td></tr>
    <tr><td><em>Clostridium perfringens</em></td><td>Spores from soil, skin, intestine or vagina in <strong>deep, dirty wounds with dead tissue</strong> (compound fractures, incisions, diabetic ulcers, septic abortions, puncture and gunshot wounds); <strong>undercooked meat and fish</strong> for food poisoning</td></tr>
    <tr><td><em>Clostridium tetani</em></td><td>Spores from soil through <strong>puncture wounds</strong>, burns, frostbite, crush injuries, and the <strong>umbilical stump</strong> in newborns</td></tr>
    <tr><td><em>Clostridium botulinum</em></td><td>Preformed toxin in <strong>low-acid, home-canned foods</strong>; <strong>swallowed spores</strong> in infants (honey, homemade baby food); spores in <strong>wounds</strong> (black tar heroin); medical use of the toxin</td></tr>
    <tr><td><em>Clostridioides difficile</em></td><td>Overgrowth of the patient&rsquo;s own colonic resident after <strong>broad-spectrum antibiotics</strong>; spread in <strong>hospitals and healthcare settings</strong>, where precautions prevent spread</td></tr>
    <tr><td><em>Listeria monocytogenes</em></td><td>From soil, water and animal intestines into <strong>food: dairy, poultry and meat</strong>, where it <strong>grows during refrigeration</strong></td></tr>
    <tr><td><em>Corynebacterium diphtheriae</em></td><td><strong>Respiratory droplets</strong> from healthy carriers or patients</td></tr>
    <tr><td><em>Cutibacterium acnes</em></td><td>The patient&rsquo;s own skin resident, onto <strong>implants and prosthetics</strong></td></tr>
    <tr><td><em>Mycobacterium tuberculosis</em></td><td><strong>Airborne respiratory droplets</strong>; an infectious dose of about 10 cells</td></tr>
    <tr><td><em>Mycobacterium leprae</em></td><td><strong>Not fully verified</strong>; possibly <strong>zoonotic from armadillos</strong>; prolonged close contact (recording)</td></tr>
    <tr><td><em>Actinomyces israelii</em></td><td>The patient&rsquo;s own oral, digestive or genital resident <strong>reaching deeper tissue</strong>: oral infection, burst appendix, gunshot wounds, ulcers, intrauterine devices</td></tr>
    <tr><td><em>Erysipelothrix rhusiopathiae</em></td><td>From pigs, through skin abrasions (de-emphasized)</td></tr>
  </table>

  <h3 class="sub" id="gpb-truth">10.15 &middot; Where the slide, the recording and current practice differ</h3>
  <p>The quizzes key what is medically true. Where a slide or the recording says something else, it is
  listed here rather than silently changed. <strong>None of these is the basis of a quiz question</strong>
  except where noted.</p>
  <ul>
    <li><strong>Tetanus mechanism (slides 29&ndash;30; recording part 1, 29:14).</strong> Slide 29 says
    tetanospasmin binds motor nerve endings and blocks gamma-aminobutyric acid and glycine; the recording
    once summarized it as blocking release at the neuromuscular junction. The toxin enters at motor nerve
    endings, travels back to the spinal cord and blocks the inhibitory transmitters there (slide 30).
    <em>Keyed:</em> it blocks gamma-aminobutyric acid and glycine; the neuromuscular junction is botulism.</li>
    <li><strong>Irregular rods (slide 59).</strong> &ldquo;All produce catalase&rdquo; and &ldquo;possess
    mycolic acids&rdquo; hold for <em>Corynebacterium</em>, <em>Mycobacterium</em> and <em>Nocardia</em>;
    <em>Actinomyces</em> is catalase negative and lacks mycolic acids, and <em>Cutibacterium</em> lacks
    mycolic acids. <em>Keyed</em> only as &ldquo;Corynebacterium and Mycobacterium share mycolic acids&rdquo;.</li>
    <li><strong><em>Nocardia</em> species (slide 94).</strong> The slide gives the tuberculosis-like lung
    disease to <em>N. brasiliensis</em>; pulmonary nocardiosis is mainly the <em>N. asteroides</em> complex,
    and <em>N. brasiliensis</em> is the classic cause of cutaneous disease and mycetoma. <em>Keyed</em> at genus
    level. The slide&rsquo;s &ldquo;often treated with cephalosporins&rdquo; is incomplete
    (trimethoprim-sulfamethoxazole is the usual first-line drug); antibiotic choice is not examined.</li>
    <li><strong>Anthrax vaccine (slide 16).</strong> &ldquo;Biothrax &mdash; only vaccine approved by
    FDA [Food and Drug Administration]&rdquo; and &ldquo;6 inoculations over 1.5 years&rdquo; are out of date: the current Biothrax schedule is
    five intramuscular doses with annual boosters, and a second, adjuvanted anthrax vaccine was licensed in
    2023 for use after exposure. Not keyed.</li>
    <li><strong>Infant botulism treatment (slide 40).</strong> &ldquo;Infectious botulism treated with
    penicillin&rdquo; applies to wound botulism (after antitoxin and debridement); antibiotics are not
    recommended for infant botulism, which is treated with botulism immune globulin. Not keyed.</li>
    <li><strong><em>C. difficile</em> treatment (slide 48).</strong> For severe disease, current guidelines
    prefer oral fidaxomicin or oral vancomycin; metronidazole is no longer recommended. And where the slide
    says mild cases respond to fluids and withdrawal of the antimicrobial, current guidelines also treat mild
    cases with an oral antibiotic. <em>Keyed</em> only as &ldquo;withdrawing the antimicrobial is part of
    managing even a mild case&rdquo;.</li>
    <li><strong>Tuberculosis regimens (slide 79).</strong> Drug-susceptible tuberculosis is standardly six
    months (four drugs for two months, then two for four), and the preferred latent regimens are now shorter
    rifamycin-based courses, with nine months of isoniazid an alternative. Only &ldquo;two or more drugs for
    months&rdquo; is keyed.</li>
    <li><strong>Leprosy (slide 89).</strong> The two-drug tuberculoid and three-drug lepromatous regimens
    match older United States practice; the current United States program uses about 12 months and about 2 years, and the World Health Organization now gives all three drugs for both forms
    (6 and 12 months). Only &ldquo;lepromatous is treated far longer&rdquo; is keyed. The 2017 subunit
    vaccine step was clearance to begin clinical trials, not licensure.</li>
    <li><strong>Honey.</strong> The recording advised no honey &ldquo;to any child under about four, just to
    make sure&rdquo;; the standard rule is no honey before 12 months. Not keyed.</li>
    <li><strong><em>Listeria</em> and heat (slide 53).</strong> &ldquo;Resistant to heat&rdquo; means it
    tolerates warmth better than most; pasteurization and cooking still kill it (slide 56). Not keyed.</li>
    <li><strong>Motility (slide 7).</strong> The genus <em>Bacillus</em> is described as motile; <em>B.
    anthracis</em> itself is nonmotile. Not keyed.</li>
    <li><strong>Myonecrosis mortality (slide 24).</strong> The recording said &ldquo;if you don&rsquo;t treat
    it, 20 to 30 percent&rdquo;, a slip for &ldquo;treated&rdquo;; percentages are not examined.</li>
  </ul>

  <button type="button" class="test-yourself-btn" onclick="window.openTestYourself('Test yourself &mdash; Gram-Positive Bacilli', TEST_YOURSELF.gramPositiveBacilli)">Test yourself! &rarr;</button>
  <p class="src">Source: <em>Gram Positive Bacilli of Medical Importance</em> (Lecture 9 Dr. Webster Gram positive
  Bacilli.pptx), Slides 1&ndash;94, the 2 October 2026 recording, and the PAJ 5200 syllabus instructional
  objectives.</p>
</section>
"""

TEST = """
    gramPositiveBacilli: [
      {q:"Where does the spore sit in a Clostridium cell?",
       choices:["In the center","At one end","Outside the cell","Clostridium forms no spores"],correct:1,
       explain:"Clostridium spores are terminal, swelling one end of the rod. Bacillus spores are central, a diagnostic characteristic."},
      {q:"Which form of anthrax is the most deadly?",
       choices:["Cutaneous","Gastrointestinal","Pulmonary","Injection"],correct:2,
       explain:"Pulmonary anthrax (woolsorters' disease) is the deadliest. Cutaneous anthrax, through a cut, is the most common."},
      {q:"Botulinum toxin blocks the release of which transmitter?",
       choices:["Glycine","Acetylcholine","Gamma-aminobutyric acid","Norepinephrine"],correct:1,
       explain:"Botulin blocks acetylcholine at the neuromuscular junction, so paralysis is flaccid and descending. Tetanospasmin blocks gamma-aminobutyric acid and glycine, so muscles contract uncontrollably."},
      {q:"Why does Listeria monocytogenes spread in food that is properly refrigerated?",
       choices:["Its spores survive cold","It grows during refrigeration","It needs an airless can","It forms a biofilm on food"],correct:1,
       explain:"Listeria grows in the cold, which is why it is cultured by cold enrichment and prevented by pasteurization and cooking rather than refrigeration."},
      {q:"Which T helper response favors lepromatous leprosy?",
       choices:["T helper 1","T helper 2","Regulatory T cells","Cytotoxic T cells"],correct:1,
       explain:"T helper 2 favors the lepromatous form, with low or absent T-cell responsiveness and disseminated disease. T helper 1 favors the shallow, nerve-damaging tuberculoid form."}
    ],
"""


HEADER = """<!--
  Microbiology Exam 2 study guide, SECTION 10: Gram-Positive Bacilli of Medical Importance (Dr. Webster).
  Fragment for the assembler, in the markup of tools/_micro_e2_guide_l7.py / _l8.py.
  GENERATED from tools/micro_e2/_micro_e2_guide_l10.py, which has the same shape as _micro_e2_guide_l8.py
  (TOC, SECTION, TEST, plus IMAGES): it can be copied to tools/ and added to SECTIONS in build_micro_e2_guide.py.

  Four blocks, each fenced by its own marker line:
    L10:TOC      the <a> lines for nav.toc (top-link + sub-links)
    L10:SECTION  the <section class="deck" id="gram-positive-bacilli"> body
    L10:TEST     the TEST_YOURSELF entry (JavaScript object member, trailing comma included)
  Figures: tools/micro_e2/l10_images.json lists (slide, picture index, file name, width, height) in the
  build_micro_e2_guide.py IMAGES shape; the 15 files are already extracted into
  Microbiology Exam 2/micro-exam-2-study-guide-images/ (raw slide blobs, l10- prefix).

  Deck: "Lecture 9 Dr. Webster Gram positive Bacilli.pptx" (94 slides). The file name says Lecture 9; the
  calendar row (2 October 2026) and the recording make it Lecture 10. Lecturer: Dr. Webster, from the deck
  file name and the recording (she refers to "Dr. Fair" in the third person twice, and names her own next
  lecture, Epidemiology, which is Lecture 12 on the calendar). The title slide names no lecturer.

  Instructional objectives: VERBATIM from the syllabus (Micro.pdf page 4), the two numbered objectives under
  "Gram Positive Bacilli of Medical Importance". The deck's own objective slide (slide 2) matches them.

  AUDIO: both parts of the 2 October 2026 recording (46:25 + 43:40) read in BOTH transcripts (local
  faster-whisper medium.en and Notability's), diffed 2026-10-08. Quotes appear in both unless marked.
  The recording starts at slide 6, so slides 1-5 have no audio.
-->
"""


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "l10_guide.html")
    html = (HEADER + "<!--L10:TOC-->" + TOC + "<!--/L10:TOC-->\n<!--L10:SECTION-->" + SECTION
            + "<!--/L10:SECTION-->\n<!--L10:TEST-->" + TEST + "<!--/L10:TEST-->\n")
    assert '""" +' not in html and "+ fig(" not in html
    open(out, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d figures)" % (out, len(html) // 1024, html.count('<figure class="fig">')))
