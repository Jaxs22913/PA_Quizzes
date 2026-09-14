#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Microbiology Exam 1 review guide from Professor Webster's own review.

On 11 September 2026 Professor Webster spent the last seventeen minutes of the
Nonspecific Immunity lecture walking the class through what to study. She went
objective by objective through the three lectures SHE taught -- Lecture 1
(Review of General Microbiology), Lecture 2 (Antibiotics and Resistance) and
Lecture 5 (Host Defenses: Nonspecific Mechanisms) -- and she did two things that
no syllabus does:

  1. She said which objectives to skip. Three of them, in her own words: the
     molecular-mechanisms overview ("we cover it in other ways so don't spend a
     lot of time there"), the health implications of nucleic acid mutations
     ("don't worry about that too much"), and the history ("don't spend a lot of
     time, but you know, major names").
  2. She confirmed a calculation is examinable. Therapeutic index: "yes,
     calculation, but the math won't be hard."

That weighting is the whole value of this page, so it is the organising
principle rather than a decoration -- every item carries the tier she put it in,
and her actual words are quoted next to it so the tier can be checked rather
than trusted.

WHERE THE CONTENT COMES FROM. The recording says WHAT is examinable; it is not
the source for the facts themselves. Every answer on this page is taken from the
three PowerPoint decks and cited to a slide number, per the standing
slides-only rule. The recording is quoted only for her instructions about
weighting, never for content. This matters because she is reviewing from memory
at speed -- in the review she says penicillin comes "from the Penicillium mold",
while the deck names the species, and the deck wins.

The one place the page departs from her list is flagged in the text rather than
silently: she told the class not to spend time on the health implications of
nucleic acid mutations, but the three mechanisms in that objective
(transformation, conjugation, transduction) reappear inside the resistance
objective in Lecture 2, which she emphasised heavily. A student who skips the
first will be missing the second. That is called out where it arises.

Scope: Lectures 1, 2 and 5 only. Lectures 3, 4 and 6 are another lecturer's and
she did not review them -- the page says so rather than leaving a silent gap,
because a review guide that looks complete and is not is worse than none.
"""
import os
import re

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
DONOR = os.path.join(ROOT, "Microbiology Exam 1/micro-exam-1-study-guide.html")
OUT = os.path.join(ROOT, "Microbiology Exam 1/micro-exam-1-webster-review.html")

# --------------------------------------------------------------------------
# Tiers. The label is hers; the wording under it is her actual instruction.
# --------------------------------------------------------------------------
COLD = ("cold", "Know cold")
KNOW = ("know", "Know it")
LIGHT = ("light", "Light touch")


def item(anchor, num, title, tier, asked, body):
    """One review item: her prompt, then the answer from the slides."""
    cls, label = tier
    asked_html = ""
    if asked:
        asked_html = ('<div class="asked"><span class="asked-label">She asked</span>'
                      '<p>%s</p></div>\n  ' % asked)
    return ('<h3 class="sub" id="%s">%s &middot; %s '
            '<span class="tier tier-%s">%s</span></h3>\n  %s%s\n'
            % (anchor, num, title, cls, label, asked_html, body))


def flag(body):
    return ('<div class="prof-flag"><span class="prof-flag-label">&#9733; '
            'Professor emphasized</span>\n  %s</div>\n' % body)


def src(text):
    return '<span class="src">%s</span>' % text


# --------------------------------------------------------------------------
# Section 1 -- Lecture 1, Review of General Microbiology
# --------------------------------------------------------------------------
S1 = []

S1.append(item("w-molecular", "1.1", "Molecular mechanisms in health and disease", LIGHT,
  "&ldquo;Describe an overview of molecular mechanisms related to micro that influence health "
  "and disease. We cover it in other ways so don&rsquo;t spend a lot of time there.&rdquo;",
  """<p>Her one explicit skip in this lecture. The material is real but it is taught again
  elsewhere, so read it once and move on.</p>
  <p>Pathogen surface proteins bind specific host receptors &mdash; influenza uses
  haemagglutinin to bind sialic acid receptors. <strong>Virulence factors</strong> are pathogen
  molecules that enhance the ability to cause disease: toxins, adhesins and invasins, which
  between them handle colonisation, invasion and evasion of the host immune response.
  Adhesion is the initial attachment (<em>Escherichia coli</em> type I fimbriae binding mannose
  receptors, colonising the urinary tract); invasion allows entry into cells
  (<em>Salmonella enterica</em> injects effector proteins into gut cells to establish a niche
  for replication). Host immune status often determines the outcome, and environmental
  factors &mdash; temperature and humidity, where vectors can flourish, hygiene, vaccination
  rates and travel &mdash; sit on top of all of it. %s</p>
  <div class="pearl"><p>Worth noticing even on a light read: the signalling example on these
  slides is PAMPs being recognised by white blood cell PRRs. That is the same recognition
  system Lecture 5 builds on, so this paragraph is not wasted.</p></div>""" % src("Lecture 1, Slides 10&ndash;12.")))

S1.append(item("w-pathogens", "1.2", "Types of infectious pathogens", KNOW,
  "&ldquo;The general types being bacteria, viruses, fungi, protozoa &mdash; but we also talked "
  "about some specific types of bacteria &hellip; go back and review those types and what makes "
  "them unique. Why are mycoplasmas special?&rdquo;",
  """<p>The general division first: <strong>prokaryotic</strong> &mdash; bacteria.
  <strong>Eukaryotic</strong> &mdash; fungi, protozoa, helminths.
  <strong>Noncellular</strong> &mdash; viruses, and alongside them prions and viroids. %s</p>

  <table>
    <tr><th>Prokaryotic</th><th>Eukaryotic</th></tr>
    <tr><td>Simple cells, no defined nuclear membrane</td><td>Complex cells, genetic material within a defined nuclear membrane</td></tr>
    <tr><td>Few organelles</td><td>Many organelles</td></tr>
    <tr><td>Circular chromosome of &ldquo;naked&rdquo; DNA</td><td>Linear chromosomes of DNA and histone proteins</td></tr>
    <tr><td>Cell walls of peptidoglycan</td><td>Cell walls carbohydrate based</td></tr>
    <tr><td>70S ribosomes</td><td>80S ribosomes</td></tr>
  </table>
  <p>%s</p>

  <h4 class="subsub">The specialized bacteria &mdash; her actual question</h4>
  <p>She asked the class directly why mycoplasmas are special and let the silence sit. The
  answer is on the slide: <strong>they lack a cell wall.</strong> Everything else follows from
  that &mdash; no wall means nothing for the Gram stain to hold and nothing for a cell-wall
  antibiotic to attack.</p>
  <table>
    <tr><th>Group</th><th>What makes it unique</th><th>Examples</th></tr>
    <tr><td><strong>Chlamydias</strong></td><td>Tiny obligate intracellular pathogens; <em>not</em> transmitted by arthropod vectors</td><td><em>Chlamydia trachomatis</em>, <em>Chlamydia psittaci</em></td></tr>
    <tr><td><strong>Rickettsias</strong></td><td>Tiny obligate intracellular pathogens; transmitted by fleas, ticks and lice</td><td><em>Rickettsia rickettsii</em>, <em>Rickettsia prowazekii</em>, <em>Coxiella burnetii</em></td></tr>
    <tr><td><strong>Mycoplasmas</strong></td><td>Tiny pleomorphic organisms that <strong>lack a cell wall</strong></td><td><em>Mycoplasma pneumoniae</em></td></tr>
  </table>
  <p>%s She added in the review that these atypicals have a different lifestyle
  because they are intracellular parasites, and named <em>Mycoplasma pneumoniae</em> as the cause
  of walking pneumonia &mdash; hard to diagnose.</p>

  <h4 class="subsub">The eukaryotic microbes</h4>
  <p><strong>Fungi</strong> &mdash; around 100,000 species, divided into two groups and
  differentiated by the spores they produce. Macroscopic (mushrooms, puffballs, gill fungi) and
  microscopic: <strong>yeasts</strong> are unicellular (<em>Saccharomyces cerevisiae</em>,
  <em>Candida albicans</em>), <strong>molds</strong> are multicellular and filamentous
  (<em>Penicillium notatum</em>). %s</p>
  <p><strong>Protozoa</strong> &mdash; around 65,000 species, mostly unicellular, differentiated
  by motility: flagella, cilia, pseudopods, or nonmotile. Many have two forms, a motile feeding
  <strong>trophozoite</strong> and a dormant resistant <strong>cyst</strong>. The groups:
  Mastigophora (flagellates &mdash; <em>Trypanosoma</em>, Chagas disease), Sarcodina (amoebas
  &mdash; <em>Entamoeba</em>, amoebic dysentery), Ciliophora (ciliates &mdash;
  <em>Balantidium</em>), Apicomplexa (essentially nonmotile, unique reproductive structures
  &mdash; <em>Plasmodium</em>, malaria). %s</p>
  <p><strong>Helminths</strong> &mdash; flatworms are flat with no definite body cavity, a blind
  digestive pouch and simple excretory and nervous systems, and include cestodes (tapeworms) and
  trematodes or flukes (flattened, nonsegmented, sucking mouthparts). Roundworms (nematodes) are
  round with a complete digestive tract, a protective surface cuticle, spines and hooks on the
  mouth, and poorly developed excretory and nervous systems. %s</p>"""
  % (src("Lecture 1, Slide 13."), src("Lecture 1, Slide 14."), src("Lecture 1, Slide 15."),
     src("Lecture 1, Slide 17."), src("Lecture 1, Slides 18&ndash;19."), src("Lecture 1, Slide 20."))))

S1.append(item("w-structures", "1.3", "Bacterial cell structures, especially those that enhance pathogenicity", KNOW,
  "&ldquo;Definitely go through those structures, especially those that enhance pathogenicity, "
  "because we talked about things which will enhance pathogenicity.&rdquo;",
  """<p>&ldquo;Definitely&rdquo; was the strongest word she used in Lecture 1. She then named
  three structures unprompted, which makes those three the ones to have cold.</p>

  <table>
    <tr><th>Structure</th><th>What it is</th><th>Why it enhances pathogenicity</th></tr>
    <tr><td><strong>Capsule</strong> (glycocalyx &mdash; capsule or slime layer)</td>
        <td>Outer layer involved in biofilm production</td>
        <td><strong>Prevents phagocytosis</strong> &mdash; named on the slide as a factor of pathogenicity. Also prevents desiccation. <em>Streptococcus pneumoniae</em></td></tr>
    <tr><td><strong>Endospores</strong></td>
        <td>Genetic material surrounded by a resistant spore coat, with a very low level of metabolism; produced as a survival mechanism by <em>Bacillus</em> and <em>Clostridium</em></td>
        <td>Extremely resistant &mdash; her framing was &ldquo;why are they good? because they&rsquo;re very resistant to a lot of things.&rdquo; Spores have been recovered from salt crystals 250 million years old</td></tr>
    <tr><td><strong>Plasmids</strong></td>
        <td>Small circular double-stranded DNA, free or integrated into the chromosome, duplicated and passed to offspring, <strong>not essential to growth and metabolism</strong></td>
        <td>May encode <strong>antibiotic resistance</strong>, tolerance to toxic metals, enzymes and toxins</td></tr>
  </table>
  <p>%s</p>

  <h4 class="subsub">The rest of the structures</h4>
  <p><strong>Projections from the wall</strong> &mdash; the flagellum gives true directional
  motility; the pilus is coded by a plasmid and used in bacterial conjugation; fimbriae are used
  for adhesion to membrane surfaces. All three are specialized features. %s</p>
  <p><strong>Internal structures</strong> &mdash; cytoplasm, organelles performing specific
  metabolic functions, a nuclear area with a circular chromosome of DNA, 70S ribosomes, and
  inclusions holding storage or waste products such as phosphate and oil droplets. %s</p>
  <p><strong>Peptidoglycan itself</strong> &mdash; a polymer of alternating
  <em>N</em>-acetylglucosamine and <em>N</em>-acetylmuramic acid crosslinked by a short peptide
  bridge, between the terminal D-alanine and the penultimate diamino-containing amino acid.
  The crosslinking is catalysed by <strong>transpeptidases, which are also the target of the
  beta-lactam antibiotics</strong> &mdash; the single fact that ties this lecture to the next
  one. Crosslinking can be direct or indirect through a pentaglycine spacer, as in
  <em>Staphylococcus aureus</em>. %s</p>"""
  % (src("Lecture 1, Slides 28, 38, 39, 40."), src("Lecture 1, Slide 27."),
     src("Lecture 1, Slide 37."), src("Lecture 1, Slide 29."))))

S1.append(item("w-gram", "1.4", "Gram-positive versus Gram-negative", COLD,
  "&ldquo;Why do they stain differently and what does that have to do with the wall structure? "
  "So, for example, Gram-positive, what&rsquo;s that wall look like? &hellip; So what is that wall "
  "good for? If you were trying to control organisms, what&rsquo;s it going to be susceptible to? "
  "What&rsquo;s it going to be resistant to?&rdquo;",
  """<p>She spent longer here than on anything else in the review, and she did not ask the class
  to recite the wall &mdash; she made them reason forward from it, twice, to what would and
  would not kill the organism. Build the answer in that direction.</p>

  <table>
    <tr><th></th><th>Gram-positive</th><th>Gram-negative</th></tr>
    <tr><td><strong>Wall</strong></td>
        <td>One thick homogeneous sheath of peptidoglycan, 20&ndash;80&nbsp;nm, with tightly bound acidic polysaccharides including teichoic and lipoteichoic acid and surface proteins, over the cytoplasmic membrane</td>
        <td>An outer membrane (asymmetric bilayer, outermost layer lipopolysaccharide), a periplasmic space, a <em>thin</em> shell of peptidoglycan, and an inner cytoplasmic membrane</td></tr>
    <tr><td><strong>Stain</strong></td>
        <td>Retains crystal violet &rarr; stains purple</td>
        <td>Loses crystal violet &rarr; stains red from the safranin counterstain</td></tr>
    <tr><td><strong>The slide&rsquo;s own summary</strong></td>
        <td><strong>Physically strong</strong> &mdash; resistant to stresses like temperature, pH, osmotic pressure</td>
        <td><strong>Chemically strong</strong> &mdash; resistant to disinfectants and antibiotics</td></tr>
    <tr><td><strong>So: physical control</strong> (heat, pH, osmotic pressure)</td>
        <td>Resistant &mdash; it is a thick physical layer and physical methods do little to it</td>
        <td>Susceptible &mdash; only a thin peptidoglycan layer to damage</td></tr>
    <tr><td><strong>So: chemical, enzymatic and cell-wall antibiotics</strong></td>
        <td>Susceptible &mdash; the wall is the whole structure and it is exposed</td>
        <td>Resistant to many &mdash; the outer membrane is the barrier, so specialized agents are needed</td></tr>
    <tr><td><strong>So: lysozyme</strong></td>
        <td>Strips the whole wall off</td>
        <td>The fatty outer membrane blocks it &mdash; takes little pieces out, <strong>may not kill</strong></td></tr>
  </table>
  <p>%s The lysozyme contrast is the one she worked through live, having just covered lysozyme
  that morning as a first-line chemical defence.</p>

  <h4 class="subsub">What is in the outer membrane</h4>
  <p>Lipopolysaccharide has three parts: <strong>Lipid A</strong>, which carries the endotoxin
  activity; the <strong>core polysaccharide</strong>; and the <strong>O-polysaccharide</strong>,
  used in bacterial classification. Only Gram-negatives have this membrane, which is why only
  Gram-negatives carry endotoxin. %s</p>

  <h4 class="subsub">The stain itself</h4>
  <ol>
    <li>Flood with crystal violet, 1 minute; wash.</li>
    <li>Flood with Gram&rsquo;s iodine, 1 minute; wash.</li>
    <li><strong>Decolorize carefully with acetone alcohol</strong> until the thinnest parts of the smear are colourless, about 10 seconds; wash. The slide calls this <strong>the most critical step</strong> and the one most affected by technical variation in timing and reagents.</li>
    <li>Flood with safranin, 1 minute; wash, then air dry or blot.</li>
  </ol>
  <p>%s Morphology sits alongside this &mdash; cocci (spherical), bacilli (rod) and spiral
  (helical, comma, twisted rod, spirochete) &mdash; and the slide answers its own question about
  why shape matters: identification. %s</p>

  %s"""
  % (src("Lecture 1, Slides 33&ndash;34."), src("Lecture 1, Slide 34."),
     src("Lecture 1, Slide 31."), src("Lecture 1, Slide 22."),
     flag("""<p>This is the reasoning chain she built aloud, and the single place she spent the
     most time in the whole review. She does not want the two walls memorised as pictures. She
     wants the chain run in one direction: <strong>wall structure &rarr; why it stains that way
     &rarr; which control method it will survive.</strong> Both of her worked examples ran that
     way round, and the lysozyme case is the one that catches people, because the intuitive
     guess &mdash; that the tougher-looking Gram-positive wall resists the enzyme &mdash; is
     backwards.</p>"""))))

S1.append(item("w-identification", "1.5", "Methods of bacterial identification and the culture media", KNOW,
  "&ldquo;Methods used in bacterial identification, we talked about that a little bit. Culture "
  "media, we talked about different kinds of culture media &hellip; selective culture media that "
  "have something which will select for the growth of something, inhibit the rest &hellip; "
  "differential culture media that give you a visual distinction.&rdquo;",
  """<p><strong>Identification methods:</strong> microscopic morphology; macroscopic morphology
  (colony appearance); physiological and biochemical characteristics; chemical analysis;
  serological analysis; and genetic and molecular analysis &mdash; guanine-plus-cytosine base
  composition, DNA analysis using genetic probes, and nucleic acid sequencing with ribosomal RNA
  analysis. %s</p>

  <table>
    <tr><th>Medium</th><th>What defines it</th></tr>
    <tr><td>Synthetic (chemically defined)</td><td>Pure organic and inorganic compounds in an exact chemical formula</td></tr>
    <tr><td>Complex or nonsynthetic</td><td>Contains at least one ingredient that is not chemically definable</td></tr>
    <tr><td>General purpose</td><td>Grows a broad range of microbes; usually nonsynthetic</td></tr>
    <tr><td>Enriched</td><td>Contains complex organic substances &mdash; blood, serum, haemoglobin, or special growth factors required by fastidious microbes</td></tr>
    <tr><td><strong>Selective</strong></td><td>Contains one or more agents that <strong>inhibit</strong> growth of some microbes and encourage growth of the desired ones</td></tr>
    <tr><td><strong>Differential</strong></td><td>Allows several types to grow and <strong>displays visible differences</strong> among desired and undesired microbes</td></tr>
  </table>
  <p>%s</p>
  <div class="callout"><p>The two examples that are <em>both</em>, which is what the exam can
  hang a question on: <strong>blood agar is enriched and differential</strong> (gamma, beta and
  alpha haemolysis &mdash; her &ldquo;different degrees of digestion of the haemoglobin&rdquo;),
  and <strong>mannitol salt agar is selective and differential</strong>. Triple sugar iron is
  the third worked example. %s</p></div>
  <p>Growth requirements sit behind all of this &mdash; chemically: water, energy nutrients
  (carbohydrates, proteins, lipids), vitamins, minerals and oxygen levels; physically:
  temperature, pH and osmotic pressure. %s</p>"""
  % (src("Lecture 1, Slide 41."), src("Lecture 1, Slides 43&ndash;44."),
     src("Lecture 1, Slides 45&ndash;47."), src("Lecture 1, Slide 42."))))

S1.append(item("w-growth", "1.6", "The bacterial growth curve", KNOW,
  "&ldquo;Go back and review the bacterial growth curve, what happens in each one.&rdquo;",
  """<p>Growth means an increase in <strong>number</strong>, not size, by <strong>binary
  fission</strong> &mdash; which is why it is exponential rather than arithmetic. %s</p>
  <table>
    <tr><th>Phase</th><th>What is happening</th></tr>
    <tr><td><strong>Lag</strong></td><td>A flat period of adjustment and enlargement; little growth</td></tr>
    <tr><td><strong>Exponential growth</strong></td><td>Maximum growth, continuing as long as cells have adequate nutrients and a favourable environment. <strong>Most vulnerable to control methods at this time</strong> &mdash; the slide's example is penicillin</td></tr>
    <tr><td><strong>Stationary</strong></td><td>Rate of cell growth equals rate of cell death, caused by depleted nutrients and oxygen and the excretion of organic acids and pollutants</td></tr>
    <tr><td><strong>Death</strong></td><td>As limiting factors intensify, cells die exponentially in their own wastes</td></tr>
  </table>
  <p>%s</p>
  <div class="pearl"><p>The vulnerability line in the exponential row is the one worth carrying:
  a cell-wall agent needs cells that are actively building wall, so a population that is not
  dividing is a population that is harder to kill. That idea returns in Lecture 2 as part of why
  biofilm organisms resist treatment.</p></div>"""
  % (src("Lecture 1, Slide 48."), src("Lecture 1, Slide 50."))))

S1.append(item("w-phage", "1.7", "Phage replication &mdash; lytic versus lysogenic", KNOW,
  "&ldquo;Go back and review the differences between lytic and lysogenic. Remember in the "
  "lysogenic, you actually will be incorporating that viral DNA into the host chromosome, which "
  "then gives a lot of different characteristics.&rdquo;",
  """<p>The six steps first, because both cycles share the opening:
  <strong>adsorption</strong> (binding of virus to a specific molecule on the host cell),
  <strong>penetration</strong> (genome enters), <strong>replication</strong> (viral components
  produced), <strong>assembly</strong>, <strong>maturation</strong> and <strong>release</strong>.
  %s</p>
  <table>
    <tr><th>Lytic</th><th>Lysogenic</th></tr>
    <tr><td>Rapid takeover of bacterial metabolism</td><td><strong>Integration of viral genes as a prophage</strong></td></tr>
    <tr><td>Production of multiple copies of virus</td><td>Viral genes replicated along with the host cell</td></tr>
    <tr><td>Destruction of the host cell</td><td>Cell is immune to reinfection</td></tr>
    <tr><td><strong>Generalized</strong> transduction &mdash; random pieces of host DNA may be transmitted to other bacteria</td><td><strong>Specialized</strong> transduction &mdash; all cells carry the same DNA from the host</td></tr>
    <tr><td>&mdash;</td><td><strong>May acquire new traits &mdash; such as the ability to make a toxin</strong></td></tr>
  </table>
  <p>%s The last row is the one she pointed at: integration is not a quieter version of
  infection, it is how a bacterium inherits a new weapon without ever looking infected.</p>"""
  % (src("Lecture 1, Slide 55."), src("Lecture 1, Slide 57."))))

S1.append(item("w-animalvirus", "1.8", "Phage replication compared with animal virus replication", KNOW,
  "&ldquo;Remember in animal virus replication, that whole virion goes in, and so what do you "
  "have to do first before it can do anything? You have to un-coat it &hellip; and then how is "
  "that animal virus typically released? You don&rsquo;t burst the cell like in bacteria, you "
  "push it through, you bud it through, and you can get an envelope that way.&rdquo;",
  """<p>Three differences, and she asked for all three in sequence. %s</p>
  <ul>
    <li>The <strong>entire virion is engulfed</strong>, rather than only the genome entering.</li>
    <li>It therefore <strong>requires uncoating</strong> to release the genetic material &mdash; driven by the difference between the pH of the cytoplasm and that of extracellular fluid.</li>
    <li><strong>Release is by budding</strong> rather than lysis, and budding may assist in the acquisition of an envelope.</li>
  </ul>
  <p>Structure sits underneath this: all viruses have <strong>capsids</strong>, protein coats
  that enclose and protect their nucleic acid, in helical, icosahedral or complex (phage) form.
  They contain DNA <em>or</em> RNA, and may have an envelope or spikes. %s</p>"""
  % (src("Lecture 1, Slide 58."), src("Lecture 1, Slide 52."))))

S1.append(item("w-cpe", "1.9", "Cytopathic effects of viruses", KNOW,
  "&ldquo;We talked about various cytopathic effects of viruses &mdash; kind of go review those.&rdquo;",
  """<p>Cytopathic effects are virus-induced damage to cells: changes in size and shape;
  cytoplasmic inclusion bodies; nuclear inclusion bodies; fusion of cells into multinucleated
  cells; cell lysis; alteration of DNA which <strong>may activate oncogenes</strong> &mdash; the
  slide notes radiation and chemical exposure can do the same &mdash; and transformation of
  cells into cancerous cells. %s</p>
  <p>The other noncellular infectious agents sit beside these: <strong>prions</strong> are
  misfolded proteins containing no nucleic acid, causing spongiform encephalopathies (holes in
  the brain) &mdash; scrapie in sheep and goats, bovine spongiform encephalopathy or mad cow
  disease, and Creutzfeldt&ndash;Jakob disease in humans. <strong>Viroids</strong> are short
  pieces of RNA with no protein coat, identified only in plants so far. %s</p>"""
  % (src("Lecture 1, Slide 59."), src("Lecture 1, Slide 60."))))

S1.append(item("w-mutations", "1.10", "Health implications of nucleic acid mutations", LIGHT,
  "&ldquo;Health implications of nucleic acid mutations &mdash; don&rsquo;t worry about that too "
  "much.&rdquo;",
  """<p>Her second explicit skip. Read it once for the shape of it: mutations occur naturally at
  a low level but may be induced by radiation, chemicals and viruses, and may be beneficial,
  neutral or deleterious to the organism. %s</p>
  <div class="callout"><p><strong>One caution before you skip it.</strong> The three mechanisms
  by which bacteria acquire new information &mdash; <strong>transformation</strong> (taking up
  naked DNA from the environment), <strong>conjugation</strong> (cell-to-cell transmission of DNA
  from a plasmid) and <strong>transduction</strong> (transmission by viral vector) &mdash; appear
  again inside the resistance objective in Lecture 2, which she emphasised heavily. Skip the
  health-implications framing if you like; do not skip the three mechanisms. %s</p></div>
  <p>For completeness: in viruses, high mutation rates change surface antigens, which can weaken
  or eliminate immunity from vaccination or previous exposure, and can let animal viruses cross
  to humans who have no immunity to them at all. In human hosts, chemical or radiation exposure
  and oncogenic viruses may transform normal cells into cancer cells, and viruses may affect
  cells of the immune system. %s</p>"""
  % (src("Lecture 1, Slide 61."), src("Lecture 1, Slide 62."), src("Lecture 1, Slides 62&ndash;63."))))

S1.append(item("w-control", "1.11", "Mechanisms of microbial control and the death curve", KNOW,
  "&ldquo;Mechanisms of microbial control &mdash; what are the basic mechanisms? And then "
  "what&rsquo;s the difference between a disinfectant and an antiseptic? And then the bacterial "
  "death curve &mdash; remember the rate of death is constant, we did that little problem, so go "
  "back and review that.&rdquo;",
  """<p>Start with the two definitions the slide separates: <strong>aseptic or sterile</strong>
  means removal of <em>all</em> forms of microbial contamination; <strong>disinfection</strong>
  means elimination of <em>some</em>. Depending on circumstances, lowering numbers rather than
  total elimination may be good enough. %s</p>
  <p><strong>The basic mechanisms</strong> &mdash; there are only two, which is why she asked for
  them as a short list: <strong>alteration of membrane permeability</strong> and
  <strong>denaturation of proteins and nucleic acids</strong>. The <em>types</em> are physical,
  chemical, and clinical (antimicrobial chemotherapeutic agents). %s</p>

  <table>
    <tr><th>Physical control</th><th>Detail</th></tr>
    <tr><td>Temperature</td><td>High can kill; <strong>low will not</strong> &mdash; refrigeration and freezing only slow growth</td></tr>
    <tr><td>Dry heat</td><td>Dry heat ovens, hot air ovens</td></tr>
    <tr><td>Wet heat</td><td>Boiling, autoclave, pasteurization</td></tr>
    <tr><td>pH</td><td>Most pathogens prefer neutral pH, so acid or base inhibits &mdash; pickling</td></tr>
    <tr><td>Osmotic pressure</td><td>Increased sugar or salt concentration</td></tr>
    <tr><td>Filtration</td><td>For heat-sensitive solutions &mdash; vaccines, sera, beer</td></tr>
    <tr><td>Radiation</td><td>Ionizing (X-ray, gamma ray) and non-ionizing (ultraviolet)</td></tr>
  </table>
  <p>%s</p>

  <h4 class="subsub">Disinfectant versus antiseptic &mdash; she asked for this by name</h4>
  <p><strong>Disinfectants are used on inanimate objects</strong> &mdash; the slide's example is
  Lysol. <strong>Antiseptics are used on tissues</strong> &mdash; Listerine mouthwash. There are
  very few true chemical sterilants: ethylene oxide (plastics, spices) and beta-propiolactone
  (vaccines, tissue grafts, surgical instruments). Sometimes control is adequate for the purpose,
  using halogens such as chlorine or bromine, or alcohol. %s</p>

  <h4 class="subsub">The death curve, and her worked problem</h4>
  <p>When a microbial control method is used on a bacterial population, <strong>the rate of death
  is constant</strong>. The <strong>decimal reduction time</strong> is the time it takes to kill
  90&nbsp;per&nbsp;cent of the organisms &mdash; that is, to drop the count by one power of ten.
  %s</p>
  %s"""
  % (src("Lecture 1, Slide 65."), src("Lecture 1, Slide 67."), src("Lecture 1, Slide 68."),
     src("Lecture 1, Slide 69."), src("Lecture 1, Slide 66."),
     flag("""<p>She pointed at a specific worked problem, so here it is with the working shown.
     The slide asks: <em>if you expose a culture containing 4,865,321 organisms to a control
     method and the decimal reduction time is 10 minutes, how long will it take to kill the
     culture?</em></p>
     <p>Each decimal reduction removes 90&nbsp;per&nbsp;cent, so each one divides the count by
     ten:</p>
     <table>
       <tr><th>Elapsed</th><th>Organisms remaining</th></tr>
       <tr><td>0 min</td><td>4,865,321</td></tr>
       <tr><td>10 min</td><td>486,532</td></tr>
       <tr><td>20 min</td><td>48,653</td></tr>
       <tr><td>30 min</td><td>4,865</td></tr>
       <tr><td>40 min</td><td>487</td></tr>
       <tr><td>50 min</td><td>49</td></tr>
       <tr><td>60 min</td><td>5</td></tr>
       <tr><td><strong>70 min</strong></td><td><strong>Below one organism</strong></td></tr>
     </table>
     <p><strong>Seventy minutes.</strong> The shortcut is to count the digits: a number just
     under ten million needs seven decimal reductions to fall below one, and seven reductions at
     ten minutes each is seventy minutes. Do not stop at the last whole organism &mdash; the
     count has to pass below one, which is why it is seven steps and not six.</p>
     <p>Note the shape of the answer rather than the number. Because the rate is constant, the
     starting population barely matters: ten times as many organisms costs one extra decimal
     reduction, not ten times the time.</p>"""))))

# --------------------------------------------------------------------------
# Section 2 -- Lecture 2, Antibiotics and Resistance
# --------------------------------------------------------------------------
S2 = []

S2.append(item("w-history", "2.1", "Major historical events and names", LIGHT,
  "&ldquo;Major historical events, major names &mdash; don&rsquo;t spend a lot of time, but you "
  "know, major names. Who do we think of as being kind of the father of chemotherapy, that you "
  "can watch a movie about on TV? Selective toxicity, Magic Bullet, Ehrlich. And then Fleming, "
  "Florey and Chain for antibiotics.&rdquo;",
  """<p>Her third explicit skip &mdash; but she named four people while skipping it, which
  effectively tells you the four to know. Learn these and let the rest of the timeline go.</p>
  <table>
    <tr><th>Name</th><th>Year</th><th>What for</th></tr>
    <tr><td><strong>Paul Ehrlich</strong></td><td>1909</td><td>Postulated that drugs could be developed to serve as <strong>&ldquo;magic bullets&rdquo;</strong> targeting infectious organisms without harm to the host &mdash; the selective toxicity idea. Worked with a team to develop arsphenamine (salvarsan) against <em>Treponema pallidum</em>, the cause of syphilis</td></tr>
    <tr><td><strong>Alexander Fleming</strong></td><td>1928</td><td>Working with plates of <em>Staphylococcus</em>, observed inhibition of the bacterium on plates contaminated with <em>Penicillium</em> mold</td></tr>
    <tr><td><strong>Howard Florey and Ernst Chain</strong></td><td>1939</td><td>Did the investigation and research to produce a <strong>stable form of penicillin</strong> that could be used in clinical therapy</td></tr>
    <tr><td>All three</td><td>1945</td><td>Fleming, Florey and Chain shared the Nobel Prize in Medicine</td></tr>
  </table>
  <p>%s</p>
  <div class="pearl"><p>One name she did not mention but which earns its place because it
  underpins her <em>next</em> point: <strong>Selman Waksman</strong>, 1943, discovered that
  <em>Streptomyces</em> species produce antibiotics, coined the term
  <strong>antibiotics</strong>, discovered over twenty of them, and won the Nobel Prize in 1952.
  %s</p></div>

  <h4 class="subsub">The terminology these names hang on</h4>
  <ul>
    <li><strong>Chemotherapy</strong> &mdash; the use of drugs to treat a disease.</li>
    <li><strong>Antimicrobial drugs</strong> &mdash; interfere with the growth of microbes within a host.</li>
    <li><strong>Antibiotic</strong> &mdash; a substance <em>produced by a microbe</em> that, in small amounts, inhibits another microbe.</li>
    <li><strong>Selective toxicity</strong> &mdash; a drug that kills harmful microbes without damaging the host.</li>
  </ul>
  <p>%s</p>"""
  % (src("Lecture 2, Slides 7&ndash;8."), src("Lecture 2, Slide 10."), src("Lecture 2, Slide 4."))))

S2.append(item("w-eukaryote", "2.2", "Criteria for drug selection &mdash; prokaryotes versus eukaryotes", KNOW,
  "&ldquo;Why do we have so many different antimicrobials for bacteria and so few for eukaryotic "
  "organisms? We are eukaryotic organisms, and so you have a lot more toxicity, so you have to "
  "look for a specific metabolic or structural feature that we find on the invader and not on "
  "us.&rdquo;",
  """<p>She gave the answer in the question, and it is exactly the slide&rsquo;s: there are not
  as many drugs in the pharmacopeia against eukaryotic pathogens because treatment is more
  difficult &mdash; <strong>their cell structure and some physiology is like that of the human
  host</strong>, so there is a great possibility of toxic side effects. Selective toxicity needs
  a target the invader has and we do not, and against a fellow eukaryote there are far fewer
  such targets. %s</p>
  <p>The properties a good antimicrobial should have, which is the same objective from the other
  direction: %s</p>
  <ul>
    <li><strong>Selective toxicity</strong> &mdash; achieved by interfering with processes or structures found in the pathogen's cells and not in host cells.</li>
    <li><strong>Bactericidal</strong> (kills organisms directly; <strong>minimal bactericidal concentration</strong> is the minimum level that kills 99.9&nbsp;per&nbsp;cent of test organisms) versus <strong>bacteriostatic</strong> (inhibits growth; <strong>minimal inhibitory concentration</strong> is the minimum level that inhibits growth).</li>
    <li>Favourable pharmacokinetics &mdash; reaching the target site at an effective concentration, which depends on distribution, crossing barriers, metabolism and excretion.</li>
    <li>Spectrum of activity &mdash; broad (large range of organisms) or narrow (small range).</li>
    <li>Lack of side effects &mdash; low direct toxicity, low potential for hypersensitivity.</li>
    <li>A good therapeutic index, and little resistance development.</li>
  </ul>
  <p>There is <strong>no perfect drug</strong> &mdash; the slide opens with that line, and the
  list above is a set of trade-offs rather than a specification anything actually meets.</p>"""
  % (src("Lecture 2, Slide 38."), src("Lecture 2, Slides 12&ndash;13."))))

S2.append(item("w-ti", "2.3", "Therapeutic index", COLD,
  "&ldquo;Therapeutic index &mdash; go back and look at the calculation of therapeutic index. And "
  "yes, calculation. But the math won&rsquo;t be hard.&rdquo;",
  """<p>The <strong>therapeutic window</strong> is the range of plasma concentrations spanning the
  minimum concentration for clinical efficacy and the concentration at which toxicity begins.</p>
  <p>The <strong>therapeutic index</strong> is a calculation used to assess the safety and
  efficacy of a drug. The slide gives it two ways:</p>
  <div class="callout">
    <p style="text-align:center;margin:4px 0;"><strong>TI &nbsp;=&nbsp;
      maximum tolerated dose &nbsp;&divide;&nbsp; minimum inhibitory concentration</strong></p>
    <p style="text-align:center;margin:4px 0;"><strong>TI &nbsp;=&nbsp;
      TD<sub>50</sub> &divide; ED<sub>50</sub></strong>
      &nbsp;&mdash;&nbsp; median toxic dose over median effective dose</p>
  </div>
  <p>%s</p>
  <p><strong>How to read the number.</strong> The toxic quantity is on top, so a
  <strong>larger</strong> therapeutic index means a wider margin of safety. A small index means
  the effective and toxic doses sit close together, so dosing has to be precise and monitored.</p>
  %s"""
  % (src("Lecture 2, Slide 15."),
     flag("""<p>She confirmed twice over that this one is calculated, not just defined &mdash;
     &ldquo;and yes, calculation&rdquo; &mdash; and then reassured the class that
     &ldquo;the math won&rsquo;t be hard.&rdquo; Taken together that describes a question that
     gives you two numbers and asks for one division.</p>
     <p>The thing to have straight going in is <strong>which quantity goes on top</strong>. Toxic
     dose over effective dose. If you invert it you will still produce a number, the arithmetic
     will still be easy, and the answer will still be wrong &mdash; and it will be wrong in the
     direction of calling a dangerous drug safe.</p>"""))))

S2.append(item("w-clearance", "2.4", "Drug clearance and the dosage schedule", KNOW,
  "&ldquo;We looked at the effect of drug clearance on dosage schedules &mdash; remember I showed "
  "you that. And what do you have to make sure your drug stays above? The minimum inhibitory "
  "concentration. So you need to schedule your doses so it&rsquo;s always going to stay above "
  "that.&rdquo;",
  """<p><strong>Drug clearance = renal clearance + hepatic clearance + clearance from all other
  tissues.</strong> That total is what determines the dosage schedule, and the rule the slide
  states is the one she asked the class to say back: <strong>you do not want to go below the
  minimum inhibitory concentration</strong>. The slide adds a second timing point that is easy to
  miss &mdash; it takes time for the drug to enter the system in the first place, so the trough
  between doses is not the only place the concentration can fall short. %s</p>
  <div class="pearl"><p>This is the practical consequence of the bacteriostatic definition two
  items up. If a drug inhibits rather than kills, then every interval spent below the minimum
  inhibitory concentration is an interval in which the surviving population is free to resume
  growing &mdash; which is also one of the drivers of resistance she lists below.</p></div>"""
  % src("Lecture 2, Slide 15.")))

S2.append(item("w-druglines", "2.5", "Antibiotics and the organisms of the major drug lines", KNOW,
  "&ldquo;Go back and review kind of the three major genera that produce antimicrobial agents "
  "&mdash; like <em>Penicillium</em>, <em>Bacillus</em>, <em>Streptomyces</em>. And what do you "
  "remember about <em>Streptomyces</em>? Makes a lot of different ones &mdash; a whole range, many "
  "of which work by doing what? Protein synthesis inhibitors, in many different ways.&rdquo;",
  """<p>She asked for three genera and one pattern, so take those first and treat the full table
  as reference: <strong><em>Penicillium</em>, <em>Bacillus</em> and <em>Streptomyces</em></strong>
  are the producers, and <strong><em>Streptomyces</em> makes a whole range of them, many of which
  are protein synthesis inhibitors.</strong></p>
  <table>
    <tr><th>Producing organism</th><th>Drug</th><th>How it works</th></tr>
    <tr><td><em>Penicillium chrysogenum</em>, now <em>P. notatum</em></td><td>Penicillin</td><td>Cell wall</td></tr>
    <tr><td><em>Bacillus subtilis</em></td><td>Bacitracin</td><td>Cell wall</td></tr>
    <tr><td><em>Cephalosporium acremonium</em></td><td>Cephalosporins</td><td>Cell wall</td></tr>
    <tr><td><em>Amycolatopsis orientalis</em></td><td>Vancomycin</td><td>Cell wall</td></tr>
    <tr><td><strong><em>Streptomyces venezuelae</em></strong></td><td>Chloramphenicol</td><td>Protein synthesis, 50S</td></tr>
    <tr><td><strong><em>Streptomyces griseus</em></strong></td><td>Streptomycin</td><td>Protein synthesis, 30S</td></tr>
    <tr><td><strong><em>Streptomyces fradiae</em></strong></td><td>Neomycin</td><td>Protein synthesis, 30S</td></tr>
    <tr><td><strong><em>Streptomyces aurofaciens</em></strong></td><td>Tetracycline</td><td>Protein synthesis, tRNA attachment</td></tr>
    <tr><td><strong><em>Streptomyces</em> species</strong></td><td>Streptogramins</td><td>Protein synthesis, 50S</td></tr>
    <tr><td><em>Micromonospora purpurea</em></td><td>Gentamicin</td><td>Protein synthesis, 30S</td></tr>
    <tr><td><em>Saccharopolyspora erythraea</em></td><td>Erythromycin</td><td>Protein synthesis, 50S</td></tr>
    <tr><td><em>Paenibacillus polymyxa</em></td><td>Polymyxin B</td><td>Plasma membrane</td></tr>
    <tr><td><em>Amycolatopsis rifamycinica</em></td><td>Rifamycin</td><td>Nucleic acid &mdash; RNA polymerase</td></tr>
    <tr><td><em>Streptomyces nodosus</em></td><td>Amphotericin B</td><td>Antifungal &mdash; ergosterol</td></tr>
    <tr><td><em>Streptomyces noursei</em></td><td>Nystatin</td><td>Antifungal &mdash; ergosterol</td></tr>
  </table>
  <p>%s Five of the protein synthesis inhibitors in that table come from <em>Streptomyces</em>,
  which is the pattern she wanted rather than the rows themselves.</p>
  <div class="callout"><p>Note that the sulfonamides and the quinolones are <em>not</em> in this
  table, and that is the point of it. They are <strong>synthetic</strong> &mdash; the sulfa drugs
  were made from coal tar dyes &mdash; so they have no producing organism. An antibiotic is made
  by a microbe; an antimicrobial need not be. %s</p></div>"""
  % (src("Lecture 2, Slides 19&ndash;33, 40."), src("Lecture 2, Slides 33&ndash;34, 70."))))

S2.append(item("w-mechanisms", "2.6", "Basic mechanisms of action, with examples", COLD,
  "&ldquo;If you remember the basic mechanisms of how these antibiotics work &mdash; they can work "
  "against the cell wall, like bacitracin or penicillin. They can work against the cell membrane. "
  "They can work against protein synthesis, and there are lots of different ways to inhibit that. "
  "They can work against nucleic acids &mdash; a lot of your antivirals work against nucleic "
  "acids. They can block the kinds of metabolic reactions.&rdquo;",
  """<p>She listed all five without pausing, which is the clearest signal in the lecture that the
  five-way division is the thing being tested. The objective asks for examples of each, so each
  row below carries them.</p>

  <h4 class="subsub">1 &middot; Inhibitors of cell wall synthesis</h4>
  <p>Bacteria constantly remodel their walls, which is what makes the wall a target at all.</p>
  <ul>
    <li><strong>Penicillins</strong> &mdash; interfere with cell walls in three ways: binding <strong>penicillin-binding proteins</strong> (inactivating membrane proteins involved in wall synthesis and maintenance), <strong>inhibition of transpeptidase</strong> (blocking formation of the peptide cross-links), and <strong>production of autolysins</strong> (breaking down wall without accompanying synthesis). Natural, semisynthetic and extended-spectrum forms exist. The beta-lactam family also includes penicillinase-resistant penicillins, penicillins combined with beta-lactamase inhibitors, carbapenems (a carbon substituted for a sulfur, plus a double bond) and monobactams (a single ring).</li>
    <li><strong>Cephalosporins</strong> &mdash; mechanism similar to the transpeptidase activity of penicillin. First generation is narrow spectrum and Gram-positive; second extends to Gram-negatives; third includes pseudomonads and is injected; fourth is oral.</li>
    <li><strong>Bacitracin</strong> &mdash; interferes with bactoprenol, the membrane transporter that moves peptidoglycan monomers across the membrane to the growing wall, preventing it from being dephosphorylated so no new monomers are inserted. The wall weakens and the bacterium bursts from osmotic lysis. <strong>Topical only</strong> &mdash; too toxic for parenteral use. Against Gram-positives.</li>
    <li><strong>Vancomycin</strong> &mdash; a glycopeptide that binds the NAG and NAM subunits and prevents their incorporation into the wall. An important <strong>&ldquo;last line&rdquo;</strong> against antibiotic-resistant <em>Staphylococcus aureus</em>.</li>
    <li><strong>Antimycobacterial agents</strong> &mdash; mycobacteria have different cell walls. Isoniazid inhibits mycolic acid synthesis; ethambutol inhibits its incorporation.</li>
  </ul>
  <p>%s</p>

  <h4 class="subsub">2 &middot; Injury to the plasma membrane</h4>
  <p><strong>Polymyxin B</strong> disrupts both the outer membrane of Gram-negative cells and the
  inner membrane by attaching to lipid components. Topical &mdash; combined with bacitracin and
  neomycin in over-the-counter preparations. %s</p>

  <h4 class="subsub">3 &middot; Inhibitors of protein synthesis</h4>
  <table>
    <tr><th>Drug</th><th>Target</th><th>Spectrum</th></tr>
    <tr><td>Chloramphenicol</td><td>Binds 50S; inhibits peptide bond formation</td><td>Broad</td></tr>
    <tr><td>Aminoglycosides (streptomycin, neomycin, gentamicin)</td><td>Change the shape of the 30S subunit, preventing accurate reading of mRNA codons</td><td>Broad</td></tr>
    <tr><td>Tetracyclines</td><td>Interfere with tRNA attachment</td><td>Broad</td></tr>
    <tr><td>Streptogramins</td><td>Two components working together to bind 50S and inhibit translation</td><td>Gram-positives</td></tr>
    <tr><td>Erythromycin</td><td>Binds 50S; prevents amino acid translocation from the tRNA to the binding site</td><td>Gram-positives</td></tr>
  </table>
  <p>%s Her &ldquo;lots of different ways to inhibit that&rdquo; is literally this table &mdash;
  five drugs, five distinct points of attack on one process.</p>

  <h4 class="subsub">4 &middot; Inhibitors of nucleic acid synthesis</h4>
  <ul>
    <li><strong>Rifamycin</strong> &mdash; inhibits RNA synthesis by inhibiting RNA polymerase. An antituberculosis medication.</li>
    <li><strong>Quinolones and fluoroquinolones</strong> &mdash; artificially produced. Nalidixic acid was first generation; later generations are ciprofloxacin, levofloxacin and moxifloxacin. They <strong>inhibit DNA gyrase</strong>, preventing DNA from unwinding. Used for urinary tract infections and hospital-acquired infections.</li>
  </ul>
  <p>%s Her aside that &ldquo;a lot of your antivirals work against nucleic acids&rdquo; points at
  the nucleoside and nucleotide analogs &mdash; remdesivir, for instance, binds viral
  RNA-dependent RNA polymerase and terminates transcription prematurely. %s</p>

  <h4 class="subsub">5 &middot; Competitive inhibitors &mdash; blocking metabolic reactions</h4>
  <p><strong>Sulfonamides</strong> (sulfa drugs) are synthetic, made from coal tar dyes by Domagk
  in 1935. They are <strong>similar to PABA</strong> and so inhibit folic acid synthesis. Broad
  spectrum. %s</p>

  <h4 class="subsub">And how you pick one</h4>
  <p>The <strong>disk-diffusion (Kirby&ndash;Bauer) method</strong>, where the reading chart
  corrects for concentration, molecular weight and other factors affecting diffusion; and the
  <strong>E test</strong> (epsilometer test, or &ldquo;MIC on a stick&rdquo;), where the minimum
  inhibitory concentration is read in micrograms per millilitre at the point where the zone of
  inhibition meets the strip. %s</p>"""
  % (src("Lecture 2, Slides 18&ndash;25."), src("Lecture 2, Slide 32."),
     src("Lecture 2, Slides 27&ndash;31."), src("Lecture 2, Slide 33."),
     src("Lecture 2, Slide 53."), src("Lecture 2, Slide 34."),
     src("Lecture 2, Slides 36&ndash;37."))))

S2.append(item("w-resistance", "2.7", "Mechanisms of drug resistance", COLD,
  "&ldquo;When we&rsquo;re talking about resistance, we&rsquo;re talking about something that is "
  "initially a natural phenomenon &mdash; because in a population of organisms you are always "
  "going to have some that are more resistant than others. But then you will expose them to the "
  "selective factor &hellip; the ones that are susceptible will die, but the ones that are "
  "resistant will live on, and under the right conditions may start to proliferate, so that then "
  "the major component of that population are the resistant ones instead of susceptible "
  "ones.&rdquo;",
  """<p>She spent more words on this than on any other item in Lecture 2, and she spent them on
  the <em>framing</em> rather than the list. Get the framing first.</p>
  %s

  <h4 class="subsub">The definition</h4>
  <p>Resistance is the ability of a microorganism to avoid the harmful effects of an antibiotic by
  <strong>destroying it</strong>, <strong>transporting it out of the cell</strong>, or
  <strong>undergoing changes that block its effects</strong>. Those three verbs map onto the
  biochemical mechanisms below. %s</p>

  <h4 class="subsub">Genetic mechanisms &mdash; how a cell acquires resistance</h4>
  <ul>
    <li>Random genetic mutation.</li>
    <li><strong>Plasmid swapping during conjugation.</strong></li>
    <li>Movement of transposons to plasmids or chromosomes.</li>
    <li><strong>Transduction</strong> by bacteriophages.</li>
    <li><strong>Transformation</strong> &mdash; acquisition of resistance genes from a recently killed cell, incorporated into a chromosome or plasmid.</li>
    <li>Binary fission can then share any of the above.</li>
  </ul>
  <p>%s These are the same three mechanisms flagged back in item 1.10 &mdash; which is why that
  &ldquo;skip&rdquo; needs the caveat attached to it.</p>

  <h4 class="subsub">Cellular and biochemical mechanisms &mdash; how resistance actually works</h4>
  <table>
    <tr><th>Strategy</th><th>Mechanism</th><th>Drugs affected</th></tr>
    <tr><td rowspan="3"><strong>Drug does not reach the active site</strong></td><td>Decreased permeability</td><td>Beta-lactams, quinolones</td></tr>
    <tr><td>Decreased transport</td><td>Aminoglycosides</td></tr>
    <tr><td>Increased efflux</td><td>Tetracyclines, quinolones</td></tr>
    <tr><td><strong>Drug inactivation</strong></td><td>Enzymes</td><td>Beta-lactamases; aminoglycoside-modifying enzymes</td></tr>
    <tr><td><strong>Target modification</strong></td><td>Gyrase modification</td><td>Quinolones</td></tr>
    <tr><td><strong>Bypass of target</strong></td><td>Alternative pathway</td><td>vanA, vanB; trimethoprim resistance</td></tr>
  </table>
  <p>%s</p>

  <h4 class="subsub">What makes it worse &mdash; her list</h4>
  <p>Resistance is natural, but it increases when antibiotics are used carelessly: %s</p>
  <ul>
    <li>Misuse or overuse of antibiotics; exposure to too many.</li>
    <li>Using outdated or weakened antibiotics.</li>
    <li><strong>Using antibiotics for viral infections and other inappropriate conditions</strong> &mdash; her words: &ldquo;it&rsquo;s not going to do anything and only help develop resistance.&rdquo;</li>
    <li>The wrong dosage schedule, and failing to complete the prescribed regimen.</li>
    <li><strong>Using someone else&rsquo;s leftover prescription</strong> &mdash; &ldquo;when you&rsquo;re taking your friend&rsquo;s antibiotic.&rdquo;</li>
    <li><strong>Antibiotics in animal feed</strong> &mdash; she raised this one unprompted and at length: if you eat meat that is not organically grown, you may be exposed to antibiotics that were in the animals&rsquo; feed. %s</li>
  </ul>
  <p>Beyond individual behaviour, the slides add environmental warming, and possible correlations
  with pesticide use in food production and microplastic contamination. Trends are tracked by the
  National Antimicrobial Resistance Monitoring System for Enteric Bacteria, an interagency
  partnership monitoring humans, retail meats and food animals. %s</p>

  <h4 class="subsub">What the data show</h4>
  <p>Increased antibiotic use means increased resistance; longer treatment means increased
  colonisation; resistance is more prevalent in healthcare facilities than in the community; areas
  of higher antibiotic use have the highest resistance; and antibiotic use correlates with
  infection by resistant strains during outbreaks. %s</p>

  <h4 class="subsub">Biofilms</h4>
  <p>A biofilm is a physical and chemical barrier that limits dissemination and
  <strong>sequesters antibiotics</strong>; organisms within it are metabolically less active and
  therefore less susceptible; and the close spatial relationship <strong>enhances resistance gene
  transfer</strong>. The clinically relevant producers are the <strong>ESKAPE</strong> organisms
  &mdash; <em>Enterococcus faecium</em>, <em>Staphylococcus aureus</em>, <em>Klebsiella
  pneumoniae</em>, <em>Acinetobacter baumannii</em>, <em>Pseudomonas aeruginosa</em> and
  <em>Enterobacter</em> species &mdash; which colonise urinary catheters, ventilators, prosthetic
  joints and cardiac implants, along with chronic wounds and the lungs of cystic fibrosis
  patients, promoting persistent infection. %s</p>"""
  % (flag("""<p><strong>Resistance is not created by antibiotics. It is selected by them.</strong>
     Genetic variation means some members of any population are already less susceptible than
     others; the presence of the antibiotic then selects for the resistant organisms that were
     there all along. The population shifts because the susceptible members are removed, not
     because the survivors changed in response.</p>
     <p>She built the entire explanation on that distinction and returned to it twice. Any answer
     that describes bacteria &ldquo;becoming&rdquo; or &ldquo;learning to be&rdquo; resistant in
     response to exposure has the mechanism backwards. Fleming himself put it as microbes being
     &ldquo;educated to resist penicillin&rdquo; by too-small doses &mdash; a vivid phrase on the
     slide, and a misleading one if taken literally.</p>"""),
     src("Lecture 2, Slide 62."), src("Lecture 2, Slide 68."), src("Lecture 2, Slide 70."),
     src("Lecture 2, Slide 73."), src("Lecture 2, Slide 74."), src("Lecture 2, Slide 75."),
     src("Lecture 2, Slide 64."), src("Lecture 2, Slide 71."))))

S2.append(item("w-problems", "2.8", "Other problems with antimicrobial therapy", KNOW,
  "&ldquo;Superinfection &mdash; when you&rsquo;re taking like a broad spectrum antibiotic, "
  "it&rsquo;s going to kill good guys, the good commensals, and then allow other things to "
  "flourish. We talked about hypersensitivities. We talked about a number of things that have "
  "direct toxicities &hellip; and then our ways that we can control those things &mdash; maybe you "
  "want to take a cocktail of different antibiotics, because some of them are going to be "
  "synergistic.&rdquo;",
  """<p>Four problems on the slide: <strong>superinfection, direct toxicity, hypersensitive
  reactions and resistance.</strong> Resistance has its own item above; the other three
  follow. %s</p>

  <h4 class="subsub">Superinfection</h4>
  <p>Secondary infections acquired, often, following the use of broad spectrum antibiotics
  &mdash; the antibiotics reduce normal flora and allow opportunistic infections to take hold.
  Predisposing conditions include corticosteroid therapy, leukemia, human immunodeficiency virus,
  systemic lupus and diabetes. Typical organisms: <em>Candida albicans</em>,
  <em>Clostridioides difficile</em>, hepatitis C virus, human immunodeficiency virus,
  <em>Aspergillus</em>, and resistant staphylococci. %s</p>

  <h4 class="subsub">Direct toxicity</h4>
  <p>High serum levels of some antibiotics may be directly toxic. The slide gives eight, and the
  pairings are the kind of thing that matches cleanly onto an exam question: %s</p>
  <table>
    <tr><th>Drug</th><th>Toxicity</th></tr>
    <tr><td>Aminoglycosides</td><td>Renal and auditory toxicity</td></tr>
    <tr><td>Sulfamethoxazole</td><td>Hyperkalemia</td></tr>
    <tr><td>Ciprofloxacin</td><td>Seizures</td></tr>
    <tr><td>Doxycycline</td><td>Esophageal ulceration</td></tr>
    <tr><td>Tetracycline</td><td>Tooth discoloration &mdash; binds with calcium during tooth development</td></tr>
    <tr><td>Chloramphenicol</td><td>Aplastic anemia</td></tr>
    <tr><td>Amphotericin B</td><td>Renal and hepatic toxicity</td></tr>
    <tr><td>Chloroquine</td><td>Cardiovascular effects and electrolyte derangements with dysrhythmias</td></tr>
  </table>

  <h4 class="subsub">Hypersensitivity</h4>
  <p>Most often seen with the <strong>beta-lactams</strong> &mdash; penicillins and cephalosporins
  &mdash; and also with quinolones. Reactions may be immediate or delayed, and may range from
  hives to anaphylactic shock. %s</p>

  <h4 class="subsub">Drug combinations &mdash; her &ldquo;cocktail&rdquo;</h4>
  <p>One approach to resistant organisms is a cocktail of different drugs. Combining them
  produces one of three effects: %s</p>
  <ul>
    <li><strong>Indifference</strong> &mdash; no interaction between the drugs.</li>
    <li><strong>Synergism</strong> &mdash; the effect of two drugs together is <em>greater</em> than the effect of either alone. This is the one she named.</li>
    <li><strong>Antagonism</strong> &mdash; the effect of two drugs together is <em>less</em> than the effect of either alone.</li>
  </ul>"""
  % (src("Lecture 2, Slide 58."), src("Lecture 2, Slide 59."), src("Lecture 2, Slide 60."),
     src("Lecture 2, Slide 61."), src("Lecture 2, Slides 78&ndash;79."))))

# --------------------------------------------------------------------------
# Section 3 -- Lecture 5, Host Defenses: Nonspecific Mechanisms
# --------------------------------------------------------------------------
S3 = []

S3.append(item("w-lines", "3.1", "The three lines of defense", COLD,
  "&ldquo;And then from today &mdash; okay, you need to know those three lines. First line, second "
  "line, third line, and know what belongs in each.&rdquo;",
  """<p>&ldquo;You need to know&rdquo; was the most direct instruction in the entire review, and
  it was about this. The three-line structure is the frame every other item in Lecture 5 hangs
  on.</p>
  <table>
    <tr><th>Line</th><th>What it is</th><th>Specific?</th></tr>
    <tr><td><strong>First</strong></td><td>Physical, chemical, microbiological and genetic barriers that block invasion <strong>at the portal of entry</strong></td><td><strong>Nonspecific</strong></td></tr>
    <tr><td><strong>Second</strong></td><td>Protective cells, physiological processes and antimicrobial substances</td><td><strong>Nonspecific</strong></td></tr>
    <tr><td><strong>Third</strong></td><td>Acquired with exposure to foreign substances (antigens); produces protective antibodies or defensive cell lines; creates <strong>immunological memory</strong></td><td><strong>Specific</strong></td></tr>
  </table>
  <p>%s</p>
  <div class="callout"><p>The dividing line that matters is between the second and the third, not
  between the first and the second. The first two are both nonspecific &mdash; the whole of this
  lecture. The third is the specific one, and it is the next lecture's subject.</p></div>"""
  % src("Lecture 5, Slide 4.")))

S3.append(item("w-firstline", "3.2", "First line &mdash; which are physical, chemical, microbiological, genetic", COLD,
  "&ldquo;First line &mdash; know which things are physical, which are chemical, which are "
  "microbiological.&rdquo;",
  """<p>She named three categories. The syllabus objective names <strong>chemical, genetic and
  physical</strong>, and the lecture slide names <strong>physical, chemical, microbiological and
  genetic</strong>. All four are below, since between her list and the objective every one of
  them is asked for somewhere.</p>

  <h4 class="subsub">Physical</h4>
  <ul>
    <li><strong>Intact skin</strong> &mdash; stratified squamous epithelium; <strong>rapid desquamation</strong> physically removes transient flora; <strong>keratin</strong>, which most pathogens cannot digest because they lack keratinase; keratinocytes produce antimicrobial peptides incorporated into lamellar bodies and secreted into a waterproof lipid layer.</li>
    <li><strong>Mucous membranes</strong> &mdash; line the gastrointestinal, respiratory and urogenital tracts, with a much greater area than skin. Thin, permeable, <strong>not keratinized</strong>, and therefore not as physically tough &mdash; they have to be, because communication with the external environment happens through them. Covered by mucus of glycoproteins, proteoglycans, peptides and enzymes; <strong>mucins</strong> are the gigantic glycoproteins that give mucus its protective properties.</li>
    <li><strong>Ciliary escalator.</strong></li>
    <li><strong>Lacrimal apparatus</strong> &mdash; produces and drains tears, washing the eye surface.</li>
    <li><strong>Nasal hairs; saliva</strong> (mechanically protects oral mucosa); <strong>urine</strong> (mechanically flushes, plus high osmolality and inhibitory pH); <strong>sweat</strong> (mechanical flush); <strong>defecation</strong>; and <strong>expulsion mechanisms</strong> &mdash; coughing, sneezing, vomiting.</li>
  </ul>
  <p>%s</p>

  <h4 class="subsub">Chemical</h4>
  <p>Sebum; the <strong>acid mantle</strong> of the skin; <strong>lysozyme, which acts on
  peptidoglycan</strong> (in tears as well as elsewhere &mdash; and the reason Gram-positives lose
  their whole wall to it while Gram-negatives do not, from item 1.4); lactic acid and electrolytes
  in sweat; digestive secretions; semen (spermine, lysozyme, lactoferrin, phospholipase); and
  vaginal secretions (lactic acid, beta-defensin, hydrogen peroxide). %s</p>

  <h4 class="subsub">Microbiological</h4>
  <p><strong>Normal flora</strong>, which begins colonisation after birth. On the epidermis,
  <em>Staphylococcus epidermidis</em>, other coagulase-negative staphylococci and coryneform
  bacteria. They work two ways at once: <strong>competing for living space and nutrients</strong>
  (a physical barrier) and <strong>producing antimicrobial substances</strong> that inhibit
  pathogens (a chemical barrier). In atopic dermatitis the balance is altered
  (<strong>dysbiosis</strong>) with fewer antimicrobial peptides &mdash; and when subjects were
  colonised with coagulase-negative staphylococci, colonisation by <em>Staphylococcus aureus</em>
  was diminished. Gut commensals prevent colonisation by pathogens, digest substances we cannot
  and provide vitamins, and assist in the development of gut-associated lymphoid tissue. %s</p>

  <h4 class="subsub">Genetic</h4>
  <p><strong>Defensin gene copy number.</strong> There are 2&ndash;14 copies of the genes coding
  alpha-defensins and 2&ndash;12 coding beta-defensins, and <strong>copy number determines the
  amount of protein made</strong> &mdash; so how well defended you are is partly inherited. The
  slide names this explicitly as a genetic defense. %s</p>
  <p>Defensins themselves are the predominant family of antimicrobial peptides &mdash; 30 to 40
  amino acids, amphipathic, damaging cell membranes, which is how they kill bacteria, fungi and
  enveloped viruses. They are also the <strong>only innate immune components that can neutralise
  a broad range of microbial toxins</strong>, by unfolding them and changing their
  three-dimensional configuration &mdash; they are antichaperones. %s</p>"""
  % (src("Lecture 5, Slides 6&ndash;14."), src("Lecture 5, Slides 13, 18."),
     src("Lecture 5, Slides 15, 17."), src("Lecture 5, Slide 25."),
     src("Lecture 5, Slides 23, 25."))))

S3.append(item("w-recognition", "3.3", "The recognition system &mdash; PRRs, PAMPs and DAMPs", COLD,
  "&ldquo;Recognition system. What do we call the receptors that the white blood cells have? "
  "That&rsquo;s the abbreviation we used. PRRs. And then what did they recognize? They recognized "
  "things on either the organisms or damaged tissue &mdash; the PAMPs and the DAMPs, pathogen "
  "associated molecular pattern, damage associated molecular pattern.&rdquo;",
  """<p>She asked for the abbreviation and then made the class expand both of the others, so know
  all three in both forms.</p>
  <table>
    <tr><th>Term</th><th>Stands for</th><th>What it is</th></tr>
    <tr><td><strong>PRR</strong></td><td>Pattern recognition receptor</td><td>The receptor. Recognises structural patterns from different types of pathogens</td></tr>
    <tr><td><strong>PAMP</strong></td><td>Pathogen associated molecular pattern</td><td>The structural pattern <strong>on a microbe</strong> that a PRR recognises</td></tr>
    <tr><td><strong>DAMP</strong></td><td>Damage associated molecular pattern</td><td>What other receptors recognise when <strong>cells have been damaged, stressed or invaded</strong> by pathogens such as viruses</td></tr>
  </table>
  <p>%s</p>
  <p>The receptors are expressed by <strong>all white blood cells</strong> and by some epithelial
  and endothelial cells, and they differentiate between healthy <strong>self</strong> tissue,
  <strong>non-self</strong> substances from microbes, and <strong>altered self</strong> &mdash;
  tissue damaged or altered by viruses or cancer. Each receptor recognises a pattern shared by a
  whole pathogen family, so a wide range of pathogens can be detected, and each cell carries a
  unique combination of receptors, which increases the likelihood of effective defence. Once they
  recognise non-self or altered self, they activate effector mechanisms. %s</p>
  <div class="pearl"><p>Two specialisations worth carrying, because they explain the division of
  labour later in the lecture: <strong>macrophages</strong> are very effective at recognising
  carbohydrates from bacteria and fungi using lectin receptors, and <strong>natural killer
  cells</strong> are very effective at recognising changes in cell surface proteins produced when
  a virus infects a cell. %s</p></div>

  <h4 class="subsub">The PRR families</h4>
  <p>Different families recognise different molecules and can sit on the plasma membrane, in the
  cytosol or in endosomes: %s</p>
  <ul>
    <li><strong>Toll-like receptors</strong> &mdash; recognise many pathogens; on the surface they stimulate inflammatory cytokines, in endosomes they stimulate interferon.</li>
    <li><strong>Scavenger receptors</strong> &mdash; eliminate microbes, or in the absence of infection clear cellular debris and cells that died by apoptosis.</li>
    <li><strong>Retinoic acid inducible gene</strong> &mdash; detects viral <em>RNA</em>, stimulates interferon.</li>
    <li><strong>Cyclic GMP cyclase</strong> &mdash; detects viral <em>DNA</em>, stimulates interferon.</li>
  </ul>"""
  % (src("Lecture 5, Slide 32."), src("Lecture 5, Slides 30&ndash;32."),
     src("Lecture 5, Slide 31."), src("Lecture 5, Slide 58."))))

S3.append(item("w-leukocytes", "3.4", "The leukocytes &mdash; what each one does", COLD,
  "&ldquo;And then for each of the white blood cells, know what they do. Those white blood cells "
  "you mentioned &mdash; know what they do.&rdquo;",
  """<p>She said this twice in one breath, which is as close to an explicit instruction as the
  review gets. The percentages are on the slides and are worth carrying, because a differential
  count is only interpretable against them.</p>
  <table>
    <tr><th>Cell</th><th>Share</th><th>Appearance</th><th>What it does</th></tr>
    <tr><td><strong>Neutrophils</strong></td><td>55&ndash;90%%</td><td>Lobed nuclei, lavender granules</td><td>Phagocytes &mdash; the dedicated killers</td></tr>
    <tr><td><strong>Eosinophils</strong></td><td>1&ndash;3%%</td><td>Orange granules, bilobed nucleus</td><td>Destroy eukaryotic pathogens; a <em>minor</em> phagocyte. Tissue resident, with granules of antimicrobial molecules and enzymes released into the extracellular space; defend against parasites, particularly helminths</td></tr>
    <tr><td><strong>Basophils</strong></td><td>0.5%%</td><td>Constricted nuclei, dark blue granules</td><td>Release potent chemical mediators; circulate. Related to <strong>mast cells</strong>, which are nonmotile and bound to connective tissue</td></tr>
    <tr><td><strong>Monocytes and macrophages</strong></td><td>3&ndash;7%%</td><td>Largest of the white blood cells, kidney-shaped nucleus</td><td>Phagocytic; cellular housekeepers; <strong>present antigens to lymphocytes</strong>; secrete cytokines to enhance immunity. Macrophages are the final differentiation of monocytes, resident in tissues with special names in particular tissues</td></tr>
    <tr><td><strong>Lymphocytes</strong></td><td>20&ndash;35%%</td><td>&mdash;</td><td><strong>B cells</strong> (adaptive humoral &mdash; activated B cells produce antibodies); <strong>T cells</strong> (adaptive cell-mediated &mdash; modulate immune functions and kill foreign cells); <strong>non-B non-T</strong>, including <strong>natural killer cells</strong>, which are innate</td></tr>
  </table>
  <p>%s</p>
  <p>Two more that are not counted in the differential but belong in the answer:
  <strong>dendritic cells</strong> trap pathogens and phagocytose in order to collect and process
  antigens for presentation to T cells; and <strong>mast cells</strong> are tissue resident,
  respond to microbes and particularly parasites, and carry granules of inflammatory mediators
  such as histamine which help expel parasites. %s</p>
  <div class="callout"><p>The pattern underneath the table: the <strong>myeloid innate immune
  cells</strong> &mdash; macrophages, dendritic cells, neutrophils and monocytes &mdash; are
  effector cells driven by pattern recognition, cytokine signalling and cell-to-cell
  communication, and they kill microbes, remove debris and <strong>recruit help from the adaptive
  immune system</strong>. That last clause is what makes them the bridge to the third line. %s</p></div>"""
  % (src("Lecture 5, Slides 66&ndash;70."), src("Lecture 5, Slide 74."),
     src("Lecture 5, Slide 72."))))

S3.append(item("w-macneut", "3.5", "Macrophage versus neutrophil", COLD,
  "&ldquo;Know the difference between a macrophage and a neutrophil &mdash; our two major "
  "phagocytes. But how are they different?&rdquo;",
  """<p>She singled this pair out from the whole list, and the slide sets them side by side in
  exactly the form she asked for.</p>
  <table>
    <tr><th>Macrophage</th><th>Neutrophil</th></tr>
    <tr><td><strong>Long-lived</strong></td><td><strong>Short-lived</strong> dedicated killer</td></tr>
    <tr><td>Resides in tissues</td><td>Circulates in blood</td></tr>
    <tr><td>Has other functions besides killing</td><td>Dedicated to killing</td></tr>
    <tr><td><strong>Works as infection begins &mdash; raises the alarm</strong></td><td><strong>Waits for the macrophage alarm to enter tissue</strong></td></tr>
  </table>
  <p>%s The last row is the functional difference the rest follow from: the macrophage is the
  sentry already in place, the neutrophil is the response that has to be called in.</p>

  <h4 class="subsub">How the neutrophil kills &mdash; the respiratory burst</h4>
  <p>When the engulfed organism encounters the neutrophil granules, <strong>NADPH oxidase produces
  superoxide</strong>, which picks up hydrogen ions and <strong>raises the pH</strong> so that the
  digestive granules can break the organism down. %s</p>
  <p>Toxic oxygen species produced during the burst can diffuse out and damage host cells, so
  phagocytes synthesise enzymes to inactivate them &mdash; <strong>catalase</strong> degrades
  hydrogen peroxide into water and oxygen. %s</p>
  <div class="pearl"><p>Her question &ldquo;what happens to these neutrophils?&rdquo; has a
  three-part answer worth knowing, because it explains something clinically visible.
  <strong>Neutrophils cannot replenish their granule contents, so they die.</strong> Some are
  phagocytosed by macrophages. And dead organisms, dead neutrophils and dead tissue together
  <strong>form pus</strong>. Others undergo <strong>netosis</strong>, bursting so that their DNA
  and defensive proteins form a <strong>neutrophil extracellular trap</strong> that catches and
  kills microorganisms. %s</p></div>"""
  % (src("Lecture 5, Slide 75."), src("Lecture 5, Slides 76&ndash;77."),
     src("Lecture 5, Slide 78."), src("Lecture 5, Slide 78."))))

S3.append(item("w-differential", "3.6", "The white blood count with differential", KNOW,
  "&ldquo;We already talked about white blood cell with differential. What do we use it for? And "
  "what can it tell us?&rdquo;",
  """<p>Two questions, so two answers. <strong>What it does:</strong> totals the number of each
  type of white blood cell and determines whether the cells are in normal proportion &mdash; which
  is why the percentages in item 3.4 matter. <strong>What it can tell us:</strong> it is useful in
  the diagnosis of infection types, inflammation, allergies, immune disorders, leukemia, and
  myelodysplastic syndrome. %s</p>
  <div class="callout"><p>Note the phrasing on the slide: <em>normal proportion</em>, not normal
  total. A differential is a shape, not a count &mdash; which is why it distinguishes among
  <em>types</em> of infection rather than merely detecting that one is present.</p></div>"""
  % src("Lecture 5, Slide 71.")))

S3.append(item("w-inflammation", "3.7", "Inflammation &mdash; the characteristics and how they come about", COLD,
  "&ldquo;Inflammation &mdash; you need to know the major characteristics, and how do they come "
  "about? How is it that we have the redness, the heat, the pain?&rdquo;",
  """<p>Two separate demands in one question. The characteristics are a list; the
  <em>how</em> is a mechanism, and she asked for the mechanism specifically.</p>

  <h4 class="subsub">The characteristics</h4>
  <table>
    <tr><th>Latin</th><th>English</th></tr>
    <tr><td><strong>Rubor</strong></td><td>Redness</td></tr>
    <tr><td><strong>Calor</strong></td><td>Heat</td></tr>
    <tr><td><strong>Tumor</strong></td><td>Swelling</td></tr>
    <tr><td><strong>Dolor</strong></td><td>Pain</td></tr>
    <tr><td><strong>Functio laesa</strong></td><td>Loss of function</td></tr>
  </table>
  <p>%s Described as early as the first century by the Roman physician Celsus &mdash; and note
  that <em>functio laesa</em> is the one most often left off a four-item answer.</p>

  <h4 class="subsub">How they come about</h4>
  <ol>
    <li>Macrophages sense infection. Products of the pathogen stimulate formation of a protein structure called an <strong>inflammasome</strong>, which activates pro-interleukin-1&beta; into functional <strong>interleukin-1&beta;</strong> in large quantities.</li>
    <li>A second cascade forms pores in the macrophage membrane, letting the interleukin into the circulation. <strong>This kills the macrophage, by pyroptosis.</strong></li>
    <li>The interleukin activates other macrophages and creates a state of inflammation. %s</li>
    <li>Release of interleukin-1&beta; initiates further cytokine release. <strong>TNF-&alpha; dilates blood vessels to increase blood volume in the infected area &mdash; and that is what produces the heat, swelling, redness and pain.</strong> Interleukin-6 also increases temperature.</li>
    <li><strong>CXCL8, CCL2 and interleukin-12 act as chemokines</strong>, attracting other white blood cells to the area.</li>
    <li>Endothelial cells upregulate adhesion molecules to direct leukocytes to the area, and loosen the tight junctions between cells. %s</li>
  </ol>
  <div class="callout"><p>Step 4 is the literal answer to &ldquo;how is it that we have the
  redness, the heat, the pain&rdquo; &mdash; <strong>vasodilation by TNF-&alpha;</strong>,
  increasing blood volume locally. All four cardinal signs come from that one change.</p></div>

  <h4 class="subsub">Getting the cells out of the blood &mdash; extravasation</h4>
  <p>Leukocytes such as neutrophils have to leave the blood and enter infected tissue, using
  adhesion molecules on the endothelium and the leukocyte surface: <strong>L-selectin</strong> on
  the leukocyte binds <strong>vascular addressin CD34</strong> on the endothelium, and
  <strong>integrin LFA-1</strong> binds <strong>ICAM-1</strong>. Transient interactions make the
  neutrophil <strong>roll</strong> along the surface; chemokines then guide it to squeeze between
  endothelial cells &mdash; <strong>diapedesis</strong> &mdash; and migrate to the site. %s</p>

  <h4 class="subsub">Why local inflammation is good and systemic inflammation is catastrophic</h4>
  <p>Locally, TNF-&alpha; released by macrophages acts on venule endothelium to increase blood
  flow and permeability, increase endothelial adhesiveness for white cells and platelets, and
  <strong>cause blood in the venules to clot &mdash; which prevents the spread of infection to the
  blood.</strong> %s</p>
  <p>Systemically, when infection develops in the blood, release of TNF-&alpha; onto venule
  endothelium <strong>in all tissues simultaneously</strong> induces a state of <strong>shock,
  organ failure and death.</strong> %s</p>"""
  % (src("Lecture 5, Slide 29."), src("Lecture 5, Slide 34."), src("Lecture 5, Slide 35."),
     src("Lecture 5, Slides 36&ndash;37."), src("Lecture 5, Slide 39."),
     src("Lecture 5, Slide 40."))))

S3.append(item("w-fever", "3.8", "Fever &mdash; what causes it, why it is good, why it is bad", COLD,
  "&ldquo;What causes fever? Why is fever good? Why is fever bad?&rdquo;",
  """<p>Three questions in a row, so structure the answer in three parts.</p>

  <h4 class="subsub">What causes it</h4>
  <p><strong>Interleukin-1&beta;, interleukin-6 and TNF-&alpha;</strong> have multiple effects both
  locally and systemically, and <strong>the systemic effects include fever</strong>. The same
  three cytokines that produce local inflammation produce fever when they act at a distance.
  %s</p>

  <h4 class="subsub">Why it is good &mdash; five reasons on the slide</h4>
  <ul>
    <li><strong>Decreases replication of viral and bacterial pathogens</strong> &mdash; in bacteria, by starving them of iron.</li>
    <li>Increases production and activity of <strong>neutrophils</strong>.</li>
    <li>Enhances <strong>T cell proliferation</strong>.</li>
    <li>Enhances immune signalling.</li>
    <li>Enhances <strong>tissue resistance to the damaging effects of TNF-&alpha;</strong>.</li>
  </ul>
  <p>%s</p>

  <h4 class="subsub">Why it is bad</h4>
  <p>Worth knowing where this half of the answer actually lives, because the fever slide itself
  lists only benefits. The harm comes through the same cytokines, acting systemically: when
  infection reaches the blood, TNF-&alpha; released onto the endothelium of all tissues at once
  induces <strong>shock, organ failure and death</strong>. The febrile response and the
  catastrophic one are the same mechanism at different scales &mdash; which is why the deck
  presents fever's benefits and TNF-&alpha;'s systemic harms four slides apart rather than as two
  opposing lists. %s</p>"""
  % (src("Lecture 5, Slide 38."), src("Lecture 5, Slide 38."), src("Lecture 5, Slide 40."))))

S3.append(item("w-interferon", "3.9", "Interferon", COLD,
  "&ldquo;When do we produce interferon? When do we produce interferon? What kind of invading "
  "organism helps us produce interferon? &mdash; Virus. Very good. And remember that it does not "
  "kill a virus, but it prevents the viral spread.&rdquo;",
  """<p>She asked the same question twice in a row before anyone answered, then supplied the
  correction herself. Both halves are the point.</p>
  %s
  <table>
    <tr><th>Interferon</th><th>Made by</th><th>What it does</th></tr>
    <tr><td><strong>Alpha</strong></td><td>Lymphocytes and macrophages</td><td><strong>Activates natural killer cells</strong></td></tr>
    <tr><td><strong>Beta</strong></td><td>Fibroblasts and epithelial cells</td><td>Assists B and T cell maturation and the inflammatory response</td></tr>
    <tr><td><strong>Gamma</strong></td><td>T cells</td><td>Inhibits cancer cells, stimulates B cells, <strong>activates macrophages</strong> and increases their effectiveness</td></tr>
  </table>
  <p>%s</p>
  <p>Interferons are small proteins produced by certain white blood cells and tissue cells, made
  <strong>in response to viruses, RNA, immune products and various antigens</strong>. They bind to
  cell surfaces and <strong>induce expression of antiviral proteins</strong>, and they also
  inhibit expression of cancer genes and suppress tumours. %s</p>
  <div class="pearl"><p><strong>Plasmacytoid dendritic cells</strong> are the professional
  interferon producers &mdash; they use pattern recognition receptors to detect viral infection,
  and within six hours of activation <strong>60&nbsp;per&nbsp;cent of the cell's transcription</strong>
  is making type I interferon to prevent systemic spread. %s</p></div>"""
  % (flag("""<p><strong>Interferon does not kill viruses. It stops spread to surrounding
     tissue.</strong> That sentence is on the slide almost word for word, and she repeated it in
     the review after supplying the answer to her own question &mdash; which is the pattern she
     uses for things she expects to be got wrong.</p>
     <p>The mechanism makes the distinction unavoidable: interferon acts on the <em>neighbouring
     uninfected</em> cells, inducing antiviral proteins in them. It does nothing to the virus and
     nothing to the cell already infected. An answer that has interferon destroying virus is
     describing the wrong target.</p>"""),
     src("Lecture 5, Slides 59, 61."), src("Lecture 5, Slides 59&ndash;60."),
     src("Lecture 5, Slide 80."))))

S3.append(item("w-complement", "3.10", "Complement", COLD,
  "&ldquo;And then complement. Complement &mdash; remember, one of the most important defensive "
  "mechanisms. And there were three different pathways that we can turn it on, all getting to the "
  "important component of C3. Which one&rsquo;s the first one? Which one is turned on immediately? "
  "The alternative. Then what comes? Then the lectin. And then finally, the classical.&rdquo;",
  """<p>The only item she drilled <em>twice</em> &mdash; once during the lecture itself, with a
  hand gesture for each pathway, and again in the review. Treat the activation order as the single
  most likely question in this lecture.</p>

  <h4 class="subsub">What complement is</h4>
  <p>One of the first immune system components to be activated; ubiquitous in blood and lymph;
  <strong>30 or more proteins</strong> working in concert to destroy bacteria, viruses and
  parasites. They circulate as inactive <strong>zymogens</strong> &mdash; soluble proteases
  &mdash; and are activated by cleavage in a cascade. A molecular defence that can be used
  immediately, deriving its activity from a unique <strong>high-energy thioester bond</strong>.
  %s</p>

  <h4 class="subsub">C3 and the thioester bond</h4>
  <p>Activation cleaves <strong>C3 into C3a and C3b</strong>. The cleavage exposes the thioester
  bond on C3b, which can either be attacked by water and become soluble, or react with a hydroxyl
  or amino group on a pathogen surface and attach to it &mdash; <strong>complement
  fixation</strong>, which marks the pathogen for destruction. Meanwhile
  <strong>C3a recruits phagocytes.</strong> %s</p>
  <p><strong>C3 is by far the most important molecule in the cascade</strong>, and the biggest
  difference between the three pathways is simply how they are activated &mdash; all three
  converge on cleaving it. %s</p>

  %s

  <h4 class="subsub">What the three pathways actually are</h4>
  <table>
    <tr><th>Order</th><th>Pathway</th><th>Specific?</th><th>Detail</th></tr>
    <tr><td><strong>1st</strong></td><td><strong>Alternative</strong></td><td>Nonspecific</td><td>The quickest of the three. Starts depositing C3b on the pathogen surface at the very beginning of infection</td></tr>
    <tr><td><strong>2nd</strong></td><td><strong>Lectin</strong></td><td>Nonspecific</td><td>Induced by infection &mdash; can begin as soon as infection is realised, but takes a little time to become effective</td></tr>
    <tr><td><strong>3rd</strong></td><td><strong>Classical</strong></td><td>Either</td><td>Part of both innate and adaptive responses. Activated by <strong>C-reactive protein</strong> (innate) or by <strong>antibody</strong> (adaptive) binding to the pathogen. <strong>This is the one that links to the third line of defense</strong></td></tr>
  </table>
  <p>%s</p>

  <h4 class="subsub">What happens once it is turned on &mdash; her three outputs</h4>
  <p>She asked &ldquo;once you do turn on complement, what happens?&rdquo; and answered in three
  parts. Keep them in that shape.</p>
  <ol>
    <li><strong>Opsonins enhance phagocytosis.</strong> The first defensive cells a pathogen meets are usually macrophages, and their efficiency is improved by opsonins &mdash; proteins bound to the pathogen surface that facilitate phagocytosis. <strong>C3b on a pathogen surface serves as an opsonin</strong>, and complement receptor 1 binds it. %s</li>
    <li><strong>The membrane attack complex.</strong> Going all the way down the cascade: C3b binding to existing C3bBb complexes forms the alternative C5 convertase, which cleaves <strong>C5 into C5a and C5b</strong>. <strong>C5b initiates the membrane attack complex, which punches holes in organism membranes.</strong> %s</li>
    <li><strong>Enhanced inflammation along the way.</strong> The smaller fragments <strong>C3a and C5a</strong> are ligands for receptors on phagocytes, endothelial cells and mast cells, and enhance the inflammatory response; in extreme cases they can induce anaphylactic shock. <strong>C5a recruits neutrophils</strong> to the infection site and is the <strong>most potent anaphylatoxin</strong>; it makes neutrophils and monocytes adhere to vessel walls, acts as a chemoattractant, and increases their phagocytic capacity. %s</li>
  </ol>

  <h4 class="subsub">Why it does not destroy us</h4>
  <p>Regulatory proteins control where C3b is deposited. In plasma, <strong>properdin (factor
  P)</strong> binds C3 convertase on microbial surfaces and <em>increases</em> activation, while
  <strong>factor H</strong> <em>reduces</em> it by making C3b susceptible to cleavage by factor I.
  On human cell surfaces, C3bBb is rapidly disrupted by <strong>decay accelerating factor</strong>
  or <strong>membrane cofactor protein</strong>. Human cells are protected from the membrane
  attack complex by S protein, clusterin and factor J, and by homologous restriction factor and
  <strong>CD59 (protectin)</strong>. %s</p>
  <div class="pearl"><p>And the evasion trick that turns that protection against us:
  <em>Streptococcus pyogenes</em> and <em>Staphylococcus aureus</em> can cover themselves in
  <strong>sialic acid</strong> &mdash; which factor H has a binding site for, because it is found
  on human cells &mdash; so C3b on their surfaces is readily inactivated. They are only resistant
  <strong>when no specific antibody is present</strong>, because antibody coats the surface and
  masks the sialic acid before complement binds. %s</p></div>"""
  % (src("Lecture 5, Slide 42."), src("Lecture 5, Slide 43."), src("Lecture 5, Slide 45."),
     flag("""<p><strong>Activation order: alternative, then lectin, then classical.</strong> She
     drilled this with a hand gesture for each &mdash; &ldquo;hand, hand, hand&rdquo; &mdash; in
     the lecture, and then made the class recite it again in the review.</p>
     <p><strong>The trap is that they were discovered in a different order.</strong> Classical was
     found first, which is why it is called classical; then alternative; then lectin. The whole
     system is called <em>complement</em> because it was thought to complement the specific
     immune system. So the names encode the discovery sequence and actively mislead about the
     activation sequence. She raised this explicitly &mdash; the naming is the reason the order
     has to be memorised rather than reasoned out.</p>"""),
     src("Lecture 5, Slides 44&ndash;45."), src("Lecture 5, Slide 48."),
     src("Lecture 5, Slides 49&ndash;50."), src("Lecture 5, Slides 53&ndash;54."),
     src("Lecture 5, Slides 46&ndash;47, 51."), src("Lecture 5, Slide 52."))))

S3.append(item("w-nk", "3.11", "Natural killer cells", KNOW,
  "&ldquo;What do natural killer cells do? Again, that&rsquo;s in that &mdash; what the different "
  "kinds of white blood cells do.&rdquo;",
  """<p>She folded this back into the leukocyte item, which tells you the expected answer is a
  functional description rather than the full nine slides the deck gives them.</p>
  <p><strong>The short answer:</strong> natural killer cells are cytotoxic lymphocytes that
  <strong>kill cells infected by viruses, bacteria or protozoan parasites</strong>, providing
  innate immunity against <em>intracellular</em> infection. They are large lymphocytes circulating
  in the blood with well-developed cytoplasm and cytotoxic granules, and they migrate from blood
  to the infection site in response to inflammatory cytokines. %s</p>
  <p>They have <strong>two effector functions</strong>: cell killing, particularly of virally
  infected cells (the CD56 dim subpopulation), and secretion of cytokines to maintain the
  inflammatory state (CD56 bright). %s</p>

  <h4 class="subsub">The balancing act</h4>
  <p>The one requirement of a natural killer cell receptor is that it must <strong>inhibit the
  cell from killing healthy self-cells</strong>. Killing is a balance between activating and
  inhibitory signals: when a cell is infected, malignant or traumatised, its protein expression
  changes so that <strong>activating signals exceed inhibitory signals</strong> &mdash; and then
  it is killed. %s</p>
  <p>The killing itself is by apoptosis: the natural killer cell contacts the target, releases
  cytotoxic granules, and the target shrinks, its chromatin condenses, and its contents are
  released &mdash; after which a macrophage does the clean-up. %s</p>

  <h4 class="subsub">Who activates them, and who they activate</h4>
  <p>Their base level of cytotoxicity is <strong>20 to 100-fold higher</strong> on exposure to the
  interferons produced in response to viral infection; type I interferons also induce their
  proliferation, and interleukin-12 and TNF-&alpha; from macrophages activate them too. %s</p>
  <p>The cooperation runs both ways, which is the part worth carrying: macrophages produce
  cytokines that recruit, activate and expand natural killer cells, and natural killer cells in
  turn produce <strong>interferon gamma, which enhances macrophage phagocytosis and cytokine
  secretion</strong>. %s</p>
  <p>And if they cannot cope: <strong>natural killer cells stimulate dendritic cells to migrate to
  secondary lymphoid tissue and turn on the adaptive response.</strong> %s</p>"""
  % (src("Lecture 5, Slides 81&ndash;82."), src("Lecture 5, Slide 82."),
     src("Lecture 5, Slide 87."), src("Lecture 5, Slide 89."), src("Lecture 5, Slide 84."),
     src("Lecture 5, Slide 90."), src("Lecture 5, Slide 91."))))

S3.append(item("w-coordination", "3.12", "Coordination of the innate and adaptive systems", KNOW,
  "&ldquo;You can&rsquo;t have an adaptive response without first having the innate response "
  "&hellip; If they are lacking innate immunity, the first and second line, you&rsquo;re toast, "
  "because there&rsquo;s no way of even passing things off to the adaptive immune system &hellip; "
  "If you lack only adaptive immunity, then you get some control by the innate system, but "
  "it&rsquo;s not really going to be able to clear it from the body. This is a very good little "
  "diagram to pay attention to.&rdquo;",
  """<p>She pointed at one diagram and told the class to pay attention to it, which is the only
  time in the whole review she singles out a single figure. Here is what it says, in three
  cases:</p>
  <table>
    <tr><th>Case</th><th>What happens to the infection</th></tr>
    <tr><td><strong>Normal individual</strong></td><td>Infection is <strong>cleared</strong> by the combined effects of innate and adaptive immunity</td></tr>
    <tr><td><strong>Lack of innate immunity</strong></td><td><strong>Uncontrolled infection</strong> &mdash; the adaptive immune response cannot be deployed at all</td></tr>
    <tr><td><strong>Lack of adaptive immunity</strong></td><td>Infection is <strong>initially controlled</strong> by innate immunity, but <strong>cannot be cleared</strong> from the body</td></tr>
  </table>
  <p>%s</p>
  <div class="callout"><p>The asymmetry is the examinable idea, and her &ldquo;you&rsquo;re
  toast&rdquo; is the right instinct for it. Losing adaptive immunity costs you
  <em>clearance</em>. Losing innate immunity costs you <em>everything</em>, because the adaptive
  response has no way to be switched on &mdash; the dendritic cell hand-off in item 3.11 is the
  mechanism that is missing.</p></div>
  <p>The deck closes on the same note: innate immunity is very effective &mdash; we carry vast
  populations of resident microbes and are well most of the time &mdash; and rare inheritable
  defects in innate mechanisms mean a substantial reduction in protection. %s</p>
  <p>Most of the time a third line is never needed, because natural killer cells and the rest of
  the innate system handle it. But the order cannot be reversed: <strong>there is no adaptive
  response without a preceding innate one.</strong></p>"""
  % (src("Lecture 5, Slide 93."), src("Lecture 5, Slide 92."))))


# --------------------------------------------------------------------------
# Page assembly
# --------------------------------------------------------------------------
TOC = """<nav class="toc">
  <h2>Contents</h2>
  <a class="top-link" href="#how-to-use">How to use this page</a>
  <a class="top-link" href="#lec1">1 &middot; Review of General Microbiology</a>
  <a href="#w-molecular">1.1 Molecular mechanisms</a>
  <a href="#w-pathogens">1.2 Types of infectious pathogens</a>
  <a href="#w-structures">1.3 Cell structures and pathogenicity</a>
  <a href="#w-gram">1.4 Gram-positive versus Gram-negative</a>
  <a href="#w-identification">1.5 Identification and culture media</a>
  <a href="#w-growth">1.6 The growth curve</a>
  <a href="#w-phage">1.7 Lytic versus lysogenic</a>
  <a href="#w-animalvirus">1.8 Phage versus animal virus</a>
  <a href="#w-cpe">1.9 Cytopathic effects</a>
  <a href="#w-mutations">1.10 Nucleic acid mutations</a>
  <a href="#w-control">1.11 Microbial control and the death curve</a>
  <a class="top-link" href="#lec2">2 &middot; Antibiotics and Resistance</a>
  <a href="#w-history">2.1 History and names</a>
  <a href="#w-eukaryote">2.2 Prokaryote versus eukaryote targets</a>
  <a href="#w-ti">2.3 Therapeutic index</a>
  <a href="#w-clearance">2.4 Clearance and dosage schedule</a>
  <a href="#w-druglines">2.5 The major drug lines</a>
  <a href="#w-mechanisms">2.6 Mechanisms of action</a>
  <a href="#w-resistance">2.7 Mechanisms of resistance</a>
  <a href="#w-problems">2.8 Other problems with therapy</a>
  <a class="top-link" href="#lec5">3 &middot; Host Defenses: Nonspecific</a>
  <a href="#w-lines">3.1 The three lines of defense</a>
  <a href="#w-firstline">3.2 First line by category</a>
  <a href="#w-recognition">3.3 PRRs, PAMPs and DAMPs</a>
  <a href="#w-leukocytes">3.4 The leukocytes</a>
  <a href="#w-macneut">3.5 Macrophage versus neutrophil</a>
  <a href="#w-differential">3.6 The differential count</a>
  <a href="#w-inflammation">3.7 Inflammation</a>
  <a href="#w-fever">3.8 Fever</a>
  <a href="#w-interferon">3.9 Interferon</a>
  <a href="#w-complement">3.10 Complement</a>
  <a href="#w-nk">3.11 Natural killer cells</a>
  <a href="#w-coordination">3.12 Innate and adaptive together</a>
  <a class="top-link" href="#closing">What she said about the exam</a>
</nav>"""

HOWTO = """<h2 id="how-to-use">How to use this page</h2>
<p>This is not a second study guide. It is a record of what Professor Webster told the class to
study, on 11 September 2026, in the last seventeen minutes of the Nonspecific Immunity lecture.
She went through her instructional objectives one at a time, said which ones to skip, asked the
questions she expected the class to be able to answer, and confirmed that one calculation is
examinable.</p>
<p>Each item below carries her actual words and then the answer from the slides. The tier badge on
each heading is her weighting, not an editorial guess &mdash; where she said to skip something the
badge says so, and her instruction is quoted next to it so you can check the call rather than
trust it.</p>
<table>
  <tr><th>Tier</th><th>What it means</th></tr>
  <tr><td><span class="tier tier-cold">Know cold</span></td>
      <td>She drilled it, asked the class to recite it, spent visible time on it, or confirmed it is calculated</td></tr>
  <tr><td><span class="tier tier-know">Know it</span></td>
      <td>She walked it and expected recall, without singling it out for extra weight</td></tr>
  <tr><td><span class="tier tier-light">Light touch</span></td>
      <td>She explicitly said not to spend much time on it</td></tr>
</table>
<div class="callout">
  <p><strong>Scope.</strong> She reviewed <strong>only the three lectures she taught</strong>
  &mdash; Lecture 1 (Review of General Microbiology), Lecture 2 (Antibiotics and Resistance) and
  Lecture 5 (Host Defenses: Nonspecific Mechanisms). Exam 1 covers <strong>Lectures
  1&ndash;6</strong>, so Lectures 3, 4 and 6 are examinable and are <em>not</em> on this page.
  Use the full <a href="micro-exam-1-study-guide.html">Exam 1 study guide</a> for those.</p>
</div>
<div class="prof-flag"><span class="prof-flag-label">&#9733; The three she said to skip</span>
  <p>Worth reading together, because knowing what is <em>not</em> coming is as useful as knowing
  what is:</p>
  <ul>
    <li><strong>Molecular mechanisms influencing health and disease</strong> &mdash; &ldquo;we cover it in other ways, so don&rsquo;t spend a lot of time there.&rdquo;</li>
    <li><strong>Health implications of nucleic acid mutations</strong> &mdash; &ldquo;don&rsquo;t worry about that too much.&rdquo; <em>One caveat, in item 1.10.</em></li>
    <li><strong>Major historical events in microbial control</strong> &mdash; &ldquo;don&rsquo;t spend a lot of time, but you know, major names.&rdquo; She then named four people, which is the actual instruction.</li>
  </ul>
</div>"""

CLOSING = """<h2 id="closing">What she said about the exam</h2>
<p>Three things are worth taking from the review beyond its contents.</p>
<p><strong>The objectives are the blueprint.</strong> She did not review by topic or by slide
order &mdash; she read down the instructional objective list for each of her lectures and
commented on each one in turn. If the review is built from the objectives, the exam is built from
them too.</p>
<p><strong>She expects to see the class again first.</strong> Her closing words:
&ldquo;I think I&rsquo;ll see you before you actually take that test. So if you go through that and
you have any questions, you can ask me. I think I&rsquo;m here next week on problems in the immune
system.&rdquo; Working through this page before that session is what turns it into a list of
questions to ask.</p>
<p><strong>The review was one-sided by design.</strong> She reviewed her own content and said so.
Nothing here should be read as a signal about the relative weight of Lectures 3, 4 and 6 on the
exam &mdash; she simply was not the one who taught them.</p>
<div class="callout">
  <p><strong>Next steps:</strong> the <a href="micro-exam-1-study-guide.html">full Exam 1 study
  guide</a> covers all six lectures, the <a href="micro-exam-1-cram-sheet.html">cram sheet</a>
  condenses them, and the five <a href="micro-exam-1-master-exam-form-a.html">master exam
  forms</a> draw from the whole block.</p>
</div>"""

EXTRA_CSS = """
  /* Tier badges. The review's whole value is the weighting, so the tier has to
     be legible at a glance in the heading rather than buried in prose. */
  .tier{
    display:inline-block;vertical-align:middle;margin-left:8px;
    font-size:.62rem;font-weight:700;letter-spacing:.4px;text-transform:uppercase;
    padding:3px 9px;border-radius:999px;border:1px solid;white-space:nowrap;
  }
  .tier-cold{background:#fdecec;color:#8f2020;border-color:#e0a5a5;}
  .tier-know{background:#eaf3ec;color:#1f4d2b;border-color:#a8c9b3;}
  .tier-light{background:#f1efe9;color:#6a6152;border-color:#cfc7b6;}
  :root[data-theme="dark"] .tier-cold{background:#3a1717;color:#f2b8b8;border-color:#7d3636;}
  :root[data-theme="dark"] .tier-know{background:#16301d;color:#a6d9b5;border-color:#3c6a4b;}
  :root[data-theme="dark"] .tier-light{background:#2a2721;color:#cdc4b2;border-color:#554e3f;}

  /* Her actual words, kept visually distinct from the slide-sourced answer so
     the two sources can never be confused for one another. */
  .asked{
    border-left:3px solid var(--accent);background:#f2f5f2;
    padding:10px 14px 10px 16px;margin:10px 0 14px;border-radius:0 8px 8px 0;
  }
  .asked-label{
    display:block;font-size:.66rem;font-weight:700;letter-spacing:.5px;
    text-transform:uppercase;color:var(--accent);margin-bottom:4px;
  }
  .asked p{margin:0;font-style:italic;color:#3f4a42;}
  :root[data-theme="dark"] .asked{background:#18211b;border-left-color:#a6d9b5;}
  :root[data-theme="dark"] .asked-label{color:#a6d9b5;}
  :root[data-theme="dark"] .asked p{color:#c8d3cb;}

  /* Professor-emphasised content -- same convention as the CMS and Clin Path
     guides so the star means the same thing site-wide. */
  .prof-flag{
    border:2px solid #d4a017;border-radius:10px;padding:16px 14px 6px;
    margin:22px 0 14px;position:relative;background:#fffdf5;
  }
  .prof-flag-label{
    position:absolute;top:-13px;left:14px;background:#fef3d4;color:#8a6205;
    font-size:.72rem;font-weight:700;padding:2px 10px;border-radius:8px;
    border:1px solid #d4a017;letter-spacing:.3px;
  }
  .prof-flag table{margin:6px 0 8px;}
  .prof-flag .callout,.prof-flag .pearl{margin-bottom:10px;}
  mark.prof-highlight{
    background:#fef3d4;color:#3a2c05;padding:0 3px;border-radius:3px;
    box-shadow:inset 0 0 0 1px #e8c766;
  }
  :root[data-theme="dark"] .prof-flag{background:#241f10;border-color:#a8801a;}
  :root[data-theme="dark"] .prof-flag-label{
    background:#3a2f12;color:#f0d98a;border-color:#a8801a;
  }
  :root[data-theme="dark"] mark.prof-highlight{
    background:#4a3a12;color:#f7ecc8;box-shadow:inset 0 0 0 1px #7a6220;
  }
  h4.subsub{margin:16px 0 6px;font-size:1rem;}
"""


def build():
    if not os.path.exists(DONOR):
        raise SystemExit("donor guide missing: %s" % DONOR)
    donor = open(DONOR, encoding="utf-8").read()

    # Lift the head (theme includes, analytics, palette) and the page chrome.
    head_end = donor.index("</style>")
    head = donor[:head_end]
    head = head.replace(
        "<title>Microbiology &middot; Exam 1 &mdash; Study Guide</title>",
        "<title>Microbiology &middot; Exam 1 &mdash; Professor Webster&rsquo;s Review</title>")
    head = head + EXTRA_CSS + "</style>\n</head>"

    # Chrome: everything from <body> up to the opening of the donor's header.
    body_start = donor.index("<body>")
    header_start = donor.index('<header class="top">')
    chrome = donor[body_start:header_start]

    # Footer and tail, taken SEPARATELY and re-ordered.
    #
    # Do not slice from the footer to the end of the donor. In that guide the
    # footer is stranded in the middle of the document -- Lectures 3 to 6 were
    # appended after it by later builders -- so `donor[foot_start:]` silently
    # carries 90 KB of another lecture's content into this page. It did exactly
    # that on the first build here, which is how the bug was found.
    foot_start = donor.index('<footer class="guide-foot"')
    foot_end = donor.index("</footer>", foot_start) + len("</footer>")
    footer_el = donor[foot_start:foot_end]
    tail = donor[donor.index("</main>"):]

    # The donor ships an unformatted placeholder in that footer; say what this
    # page was actually built from instead.
    footer_el = footer_el.replace(
        "Built from your %s lecture decks",
        "Built from Professor Webster&rsquo;s Exam 1 review and her three lecture decks")
    footer = footer_el + "\n" + tail

    header = (
        '<header class="top">\n'
        '  <h1>Microbiology &middot; Exam 1 &mdash; Professor Webster&rsquo;s Review</h1>\n'
        '  <p>PAJ 5200 Microbiology &middot; Class of 2028</p>\n'
        '  <p>What she told the class to study, walked objective by objective &middot; '
        'covers Lectures 1, 2 and 5 &mdash; the three she taught &middot; '
        'every answer cited to its slide</p>\n'
        '</header>\n')

    body = []
    body.append('<div class="layout wrap" data-readable>')
    body.append(TOC)
    body.append('<main>')
    body.append(HOWTO)
    body.append('<h2 id="lec1">1 &middot; Lecture 1 &mdash; Review of General Microbiology</h2>')
    body.extend(S1)
    body.append('<h2 id="lec2">2 &middot; Lecture 2 &mdash; Antibiotics and Resistance</h2>')
    body.extend(S2)
    body.append('<h2 id="lec5">3 &middot; Lecture 5 &mdash; Host Defenses: Nonspecific Mechanisms</h2>')
    body.extend(S3)
    body.append(CLOSING)

    html = head + "\n" + chrome + header + "\n".join(body) + "\n" + footer

    # The donor links a Word export that does not exist for this page.
    html = re.sub(r'\s*<link rel="alternate"[^>]*micro-exam-1-study-guide\.docx"[^>]*>', "", html)

    open(OUT, "w", encoding="utf-8").write(html)

    # Loud, checkable summary rather than a bare success line.
    tiers = {t: html.count('tier-%s"' % t) for t in ("cold", "know", "light")}
    print("wrote %s (%d KB)" % (os.path.basename(OUT), len(html) // 1024))
    print("  items: %d  |  cold %d / know %d / light %d"
          % (len(S1) + len(S2) + len(S3),
             tiers["cold"] - 1, tiers["know"] - 1, tiers["light"] - 1))
    print("  professor-emphasis blocks: %d" % html.count('class="prof-flag"'))
    print("  slide citations: %d" % html.count('class="src"'))
    print("  quoted prompts: %d" % html.count('class="asked"'))
    for probe in ("data-audio-dir", "<script>alert"):
        assert probe not in html, "unexpected %r in output" % probe
    assert html.count("<main>") == 1 and html.count("</main>") == 1
    assert "Lecture 1, Slide" in html and "Lecture 5, Slide" in html


if __name__ == "__main__":
    build()
