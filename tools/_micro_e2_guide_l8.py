# -*- coding: utf-8 -*-
"""Section 8 of the Microbiology Exam 2 guide -- Diagnosing Infections (Dr. Fair).

Attribution: the deck names no lecturer; the PAJ5200.* filename pattern and
the calendar row for 2026-09-18 both point to Dr. Fair (lecturer_profiles).

Instructional objectives are VERBATIM from the syllabus. They are the
COURSE-WIDE list the deck's own objective slide reproduces, and the lecture
itself is a survey of diagnostic METHODS. The guide still answers the seven
objectives in order, saying plainly where the deck gives an objective only a
sentence or nothing at all -- rather than inventing content to fill it.

AUDIO: 45 minutes, read in BOTH transcripts (local faster-whisper and
Notability's own); the quotes used here appear in both. The recording stops at
the break around slide 43, so slides 44-57 (complement fixation, fluorescent
antibody, immunoassays, in vivo testing, viruses) have no audio.
"""

FIG = "micro-exam-2-study-guide-images"
DECK = "PAJ5200.Diagnosing Infections-2.pptx"


def fig(name, w, h, alt, cap, slide):
    return ('<figure class="fig"><img width="%d" height="%d" loading="lazy" src="%s/%s" alt="%s">'
            '<figcaption>%s <span class="src">Copyright &copy; The McGraw-Hill Companies. Source: %s, Slide %d.</span></figcaption></figure>'
            % (w, h, FIG, name, alt, cap, DECK, slide))


TOC = """
  <a class="top-link" href="#diagnosing-infections">8 &middot; Diagnosing Infections</a>
  <a class="sub-link" href="#dx-audio">&#9733; What the recording adds</a>
  <a class="sub-link" href="#dx-agents">8.1 Objective 1 &mdash; Identifying the agent: three categories</a>
  <a class="sub-link" href="#dx-genotypic">8.2 Objective 1 &mdash; Genotypic methods</a>
  <a class="sub-link" href="#dx-serology">8.3 Objective 1 &mdash; Serology, agglutination &amp; precipitation</a>
  <a class="sub-link" href="#dx-immunoassays">8.4 Objective 1 &mdash; Blots, complement fixation, fluorescence, immunoassays</a>
  <a class="sub-link" href="#dx-physiology">8.5 Objective 2 &mdash; Physiology in the laboratory</a>
  <a class="sub-link" href="#dx-mechanisms">8.6 Objective 3 &mdash; Is it causing the disease?</a>
  <a class="sub-link" href="#dx-specimens">8.7 Objective 4 &mdash; Specimens, handling &amp; transmission risk</a>
  <a class="sub-link" href="#dx-sensitivity">8.8 Objectives 5 &amp; 6 &mdash; Sensitivity testing &amp; treatment</a>
  <a class="sub-link" href="#dx-prevention">8.9 Objective 7 &mdash; Prevention</a>
"""

SECTION = """
<section class="deck" id="diagnosing-infections">
  <h2 class="deck-title">8 &middot; Diagnosing Infections</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Recall common infectious agents and the diseases that they cause.</li>
      <li>Recall microbial physiology including metabolism, regulation and replication.</li>
      <li>Describe the mechanisms by which an infectious agent causes disease.</li>
      <li>Describe the epidemiology and transmission of infectious agents.</li>
      <li>Discuss common mechanisms of antimicrobial action and resistance.</li>
      <li>Describe antimicrobial treatment strategies.</li>
      <li>Explain preventative interventions employed to prevent infectious diseases.</li>
    </ol>
  </div>

  <div class="callout"><strong>These objectives are the course-wide list, and this lecture is about
  diagnostic methods.</strong> The syllabus (and the deck&rsquo;s own objective slide) gives this lecture
  the seven objectives above, but its 57 slides are a survey of how an unknown microbe is identified.
  So most of the content answers objective 1 &mdash; <em>recognizing the agent</em> &mdash; and the
  sections below say plainly where the deck gives an objective only a sentence. Everything hangs on one
  three-way split: <strong>phenotypic, genotypic, immunological</strong>. Ask of every technique which of
  the three it is.</div>

<!--MICROL8AUDIO-->
  <div class="prof-flag" id="dx-audio"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 18 September 2026</span>
  <p>45 minutes, <b>both transcripts read and compared</b>; the quotes below appear in both. The
  recording <b>stops at the break, around slide 43</b> (&ldquo;this is a very logical place for us to
  pause&rdquo;), so complement fixation, fluorescent antibodies, immunoassays, in vivo testing and viral
  diagnosis have no audio. The lecture is taught through laboratory anecdote and gives almost no exam
  steer &mdash; the same pattern as this lecturer&rsquo;s Exam 1 lectures.</p>
  <table>
    <tr><th>What was said</th><th>What it means for you</th></tr>
    <tr><td><em>&ldquo;You don&rsquo;t have to bog down in a lot of the details&hellip; I highlighted some
    things for you. So blood agar is useful for detecting hemolysis&hellip; <mark class="prof-highlight">the
    take-home message is that the blood agar is useful for detecting hemolysis, especially for pathogenic
    Gram-positive bacteria</mark> like staph aureus or strep pyogenes.&rdquo;</em> [about minute 18]</td>
    <td>The one explicit priority in the recording. Know what each plate is <em>for</em> (slides
    17&ndash;20) rather than every reagent. <em>Staphylococcus</em> and <em>Streptococcus</em> return in the
    medically important cocci lecture.</td></tr>
    <tr><td>Southern, Northern, Western, Eastern: <em>&ldquo;Southern was the first, was actually a
    man&rsquo;s name, DNA [deoxyribonucleic acid]. RNA [ribonucleic acid] is Northern. Western is protein. And then Eastern is carbohydrates or other
    epitopes.&rdquo;</em> [about minute 42]</td>
    <td>A memory hook for slides 41&ndash;42: only &ldquo;Southern&rdquo; is a person (Edwin Southern);
    the other compass points are a joke on his name.</td></tr>
    <tr><td>Genotypic methods for organisms that are hard to grow: <em>Legionella</em> &ldquo;you have to use
    live amoeba&rdquo;; &ldquo;tuberculosis, leprosy, again, very, very difficult to grow.&rdquo; [about minute 9]</td>
    <td>Matches slide 8 (<em>Mycobacterium</em>, <em>Legionella</em>): culture-free methods earn their cost
    on slow or difficult organisms.</td></tr>
    <tr><td>&ldquo;This is relevant to Koch&rsquo;s postulates, but remember, not all organisms will work
    for Koch&rsquo;s postulates. So what if the infection turns out to&hellip; be viral?&rdquo; [about minute 27]</td>
    <td>Slide 24&rsquo;s caution: finding an organism is not proof it causes the disease.</td></tr>
  </table>
  <p class="muted"><b>One statement to hold loosely:</b> slide 18 and the recording both say chocolate agar
  is &ldquo;mainly used for anaerobic culturing,&rdquo; and the lecturer describes the candle jar
  that raises carbon dioxide. Learn it as the slide states it for this exam; it is flagged for review
  rather than silently changed.</p>
  </div>
<!--/MICROL8AUDIO-->

  <h3 class="sub" id="dx-agents">8.1 &middot; Objective 1 &mdash; Identifying the agent: the three categories</h3>
  <table>
    <tr><th>Category</th><th>What it examines</th><th>Needs culture?</th></tr>
    <tr><td><strong>Phenotypic</strong></td><td>Observable microscopic and macroscopic characteristics
    (phenotype = &ldquo;the physical expression of genes&rdquo;): morphology, physiology and biochemistry,
    chemical analysis, sensitivity to antimicrobial drugs</td><td>Usually &mdash; so may take
    <strong>longer</strong></td></tr>
    <tr><td><strong>Genotypic</strong></td><td>Genetic makeup: DNA and RNA sequence analysis, restriction fragment
    length polymorphism, specific gene sequencing to build phylogenies, electrophoresis</td><td><strong>Usually
    not</strong></td></tr>
    <tr><td><strong>Immunological</strong></td><td>Serology &mdash; antibody-antigen reactions:
    agglutination, precipitation, immunoelectrophoresis, complement fixation, immunofluorescence,
    immunoassays, in vivo allergy testing</td><td>May or may not &mdash; but always exploits antigen-antibody
    specificity</td></tr>
  </table>
  """ + fig("l8-s14-specimen-scheme.jpg", 581, 600,
      "Flow chart: a specimen goes either to direct testing (microscopic stains, direct antigen, gene probes) or to culture and isolation (biochemical tests, serotyping, antimicrobial sensitivity, gene probes, phage typing, animal inoculation); the patient supplies serological tests, in vivo tests and clinical signs.",
      "The two routes a specimen can take. <b>Direct testing</b> (left) looks at the specimen itself "
      "&mdash; stains, direct antigen, gene probes &mdash; and is fast. <b>Culture and isolation</b> (right) "
      "grows the organism first and then tests the isolate, which is slower but opens biochemical tests, "
      "serotyping and sensitivity testing. Notice gene probes appear on <em>both</em> sides, and that the "
      "patient contributes too: antibody titers, in vivo tests and the clinical picture.", 14) + """
  <p>Results come in two categories, <strong>presumptive</strong> or <strong>confirmatory</strong>. Immune
  tests are generally easier (and more accurate) than testing for the microbe itself: the rapid strep
  test takes <strong>10&ndash;15 minutes</strong> &mdash; but you need a hypothesis first to choose the
  test (fever, sore throat and pus pockets on the tonsils suggest strep throat).</p>

  <h3 class="sub" id="dx-genotypic">8.2 &middot; Objective 1 &mdash; Genotypic methods</h3>
  <p>Genotypic methods assess the organism&rsquo;s genetic makeup and <strong>need no culture</strong>
  &mdash; valuable for slow-growing <em>Mycobacterium</em> and hard-to-grow <em>Legionella</em>. Precise,
  automated methods give quick results, and faster, more accurate diagnosis means proper treatment
  begins in a timely manner.</p>
  <table>
    <tr><th>Technique</th><th>Key facts</th></tr>
    <tr><td>DNA probe hybridization / restriction fragment length polymorphism (&ldquo;DNA fingerprinting&rdquo;)</td>
    <td>Probes complementary to a microbe&rsquo;s specific sequences bind. Restriction enzymes cut DNA into
    fragments whose lengths differ between organisms</td></tr>
    <tr><td>Polymerase chain reaction</td><td>A <strong>thermal cycler</strong> amplifies specific pieces of DNA
    or RNA; basic concept invented by <strong>Kary Mullis</strong> and colleagues. Guanine plus cytosine
    content helps <em>taxonomic</em> determination, not necessarily a specific identification</td></tr>
    <tr><td>Ribosomal RNA sequencing</td><td>Compares base sequences to establish relationships:
    <strong>16S</strong> ribosomal RNA genes for bacteria (prokaryotes), <strong>18S</strong> for eukaryotes;
    builds phylogenetic trees (slide 29: the oral microflora)</td></tr>
  </table>

  <h3 class="sub" id="dx-serology">8.3 &middot; Objective 1 &mdash; Serology, agglutination and precipitation</h3>
  <p><strong>Serology</strong> is in vitro diagnostic testing of serum. Antibodies are extremely specific,
  so the methods are very sensitive. Visible results: precipitates, color changes, or released
  radioactivity. Tests identify antibody and measure how much is present &mdash; the
  <strong>titer</strong>, often reported in binding antibody units. A known antigen can test a
  patient&rsquo;s serum (serological diagnosis), or known antibody can identify an unknown microbe
  (<strong>serotyping</strong>).</p>
  <table>
    <tr><th></th><th>Agglutination</th><th>Precipitation</th></tr>
    <tr><td>Antigen</td><td><strong>Whole-cell or insoluble</strong></td><td><strong>Soluble</strong>, made insoluble by antibody</td></tr>
    <tr><td>What you see</td><td>Large visible clumps that sink</td><td>A visible precipitate; needs a <strong>gel or liquid matrix</strong></td></tr>
    <tr><td>Sensitivity</td><td>Generally <strong>more</strong> sensitive than precipitation; run on a card or slide</td><td>Very sensitive</td></tr>
    <tr><td>Uses</td><td>Blood typing; rapid syphilis diagnosis; cold agglutinins for mycoplasmas; Weil-Felix
    test for rickettsial disease; latex agglutination for pregnancy; <strong>color-changing rapid strep
    tests are a modified agglutination technique</strong></td><td>Tube precipitation; Ouchterlony
    double diffusion in agar gel; <strong>immunoelectrophoresis</strong> identifies which antibody
    class (immunoglobulin G, M and so on) binds antigen in serum</td></tr>
  </table>

  <h3 class="sub" id="dx-immunoassays">8.4 &middot; Objective 1 &mdash; Blots, complement fixation, fluorescence, immunoassays, in vivo tests and viruses</h3>
  <table>
    <tr><th>Blot</th><th>Detects</th><th>Notes</th></tr>
    <tr><td>Southern (about 1975)</td><td>Specific <strong>DNA</strong> sequences</td><td>The original, invented by Edwin Southern</td></tr>
    <tr><td>Northern (about 1977)</td><td><strong>RNA</strong> (gene expression)</td><td>Oncogenes; transplant rejection</td></tr>
    <tr><td><strong>Western</strong> (about 1981)</td><td><strong>Proteins</strong></td><td>Electrophoresis then an immunoassay; bands where antibody binds. <strong>Second test used to verify human immunodeficiency virus status</strong>; also bovine spongiform encephalopathy, Lyme disease, hepatitis B</td></tr>
    <tr><td>Eastern (about 1982)</td><td>Proteins, lipids, carbohydrate epitopes</td><td>Post-translational products</td></tr>
  </table>
  """ + fig("l8-s46-complement-fixation.jpg", 800, 578,
      "Two-row diagram of the complement fixation test. Top row: antibody in the patient's serum binds antigen and fixes complement, so sheep red cells with lysins do not lyse, a positive result. Bottom row: no antibody, complement stays free, is fixed by the lysins on the sheep cells and they hemolyze, a negative result.",
      "The counter-intuitive test, drawn so the logic shows. In the <b>top row</b> the patient&rsquo;s "
      "antibody meets antigen and uses up (&ldquo;fixes&rdquo;) the complement, so none is left to burst the "
      "sheep red cells: an intact red tube means antibody is <b>present</b>. In the <b>bottom row</b> there is "
      "no antibody, the complement stays free, the lysins on the sheep cells use it, and the tube turns clear "
      "with hemolysis: <b>negative</b>. Lysis is the negative result.", 46) + """
  <div class="pearl"><strong>Complement fixation</strong> (&ldquo;lysin-mediated hemolysis&rdquo;, now largely
  replaced by enzyme-linked immunosorbent assay) uses four components: antigen, antibody (lysin),
  complement and sensitized sheep red cells. <strong>Fixed complement &rarr; no hemolysis &rarr; the
  patient&rsquo;s serum is positive. Unfixed complement &rarr; hemolysis &rarr; negative.</strong></div>
  """ + fig("l8-s48-fluorescent-antibody.jpg", 577, 572,
      "Diagram of direct fluorescent antibody testing, where a dye-labeled antibody binds an unknown antigen, and indirect testing, where a patient's antibody binds a known antigen and a second fluorescent antibody reveals it.",
      "Direct versus indirect, which is the whole distinction. <b>Direct</b> (top): a fluorescent "
      "antibody binds the unknown organism or tissue itself, so it identifies the <em>antigen</em>. "
      "<b>Indirect</b> (bottom): the patient&rsquo;s serum is laid on a <em>known</em> antigen and a second, "
      "fluorescent anti-antibody shows whether the serum&rsquo;s antibody stuck, so it detects the "
      "patient&rsquo;s <em>antibody</em>. No antibody in the serum, nothing for the second antibody to bind, no glow.", 48) + """
  <table>
    <tr><th>Method</th><th>Key facts</th></tr>
    <tr><td>Fluorescent antibody testing</td><td>A <strong>monoclonal antibody labeled with a fluorescent dye</strong>
    shows cells or aggregates, by direct or indirect methods</td></tr>
    <tr><td>Immunoassays</td><td>Extremely sensitive &mdash; detect <strong>trace amounts</strong> of antigen or antibody.
    Radioimmunoassay: labeled with radioactive isotopes. Enzyme-linked immunosorbent assay: an enzyme-antibody
    complex produces a colored product (chromogen) when its substrate is added; run in 96-well plates</td></tr>
    <tr><td>In vivo testing</td><td>Antigen introduced <strong>into the body</strong> to detect antibody or
    sensitivity: tuberculin skin test, allergy testing</td></tr>
    <tr><td>Viruses</td><td>Special difficulty: they are not cells and need a specific host cell to replicate,
    so they are labor intensive to culture. Rapid point-of-care tests may use antigen-antibody reactions</td></tr>
  </table>
  """ + fig("l8-s51-elisa.jpg", 773, 900,
      "Diagrams of indirect and capture (sandwich) enzyme-linked immunosorbent assays, with a photograph of a 96-well microtiter plate screening for antibodies to the human immunodeficiency virus, yellow wells positive.",
      "Two designs, one readout. The <b>indirect</b> assay (left) coats the well with known antigen to "
      "catch a patient&rsquo;s <em>antibody</em> &mdash; the basis of human immunodeficiency virus screening, "
      "and the yellow wells in the plate are the positives. The <b>capture or sandwich</b> assay (right) "
      "coats the well with antibody to catch an <em>antigen</em> between two antibodies, used here for measles "
      "virus. In both, color appears only where the enzyme-linked antibody stayed bound.", 51) + """

  <h3 class="sub" id="dx-physiology">8.5 &middot; Objective 2 &mdash; Microbial physiology in the laboratory</h3>
  <p>Phenotypic identification reads the organism&rsquo;s physiology and metabolism.</p>
  <table>
    <tr><th>Method</th><th>What it looks at</th></tr>
    <tr><td>Microscopic morphology</td><td>Fresh or stained organisms: cell shape, size, stain reaction (Gram, flagellar,
    acid-fast), cell structures. Immediate direct examination also uses direct fluorescent antibody and
    direct antigen testing</td></tr>
    <tr><td>Macroscopic morphology</td><td>Colony appearance on test plates: texture, size, shape, pigment, growth requirements</td></tr>
    <tr><td>Physiological / biochemical</td><td>Presence or absence of particular enzymes or metabolic pathways &mdash; product formed means the enzyme is present</td></tr>
    <tr><td>Chemical analysis</td><td>Specific chemical composition: cell wall peptides, cell membrane lipids</td></tr>
  </table>
  <table>
    <tr><th>Common test or medium</th><th>What it shows</th></tr>
    <tr><td>Carbohydrate fermentation, amino acid utilization, hydrolysis of gelatin, starch or lipids, catalase, oxidase, coagulase, hemolysins</td><td>The common biochemical tests</td></tr>
    <tr><td><mark class="prof-highlight">Blood agar</mark></td><td><strong>Detects hemolytic activity</strong></td></tr>
    <tr><td>Chocolate agar</td><td>&ldquo;Mainly used for anaerobic culturing&rdquo; (the slide&rsquo;s wording)</td></tr>
    <tr><td>Mannitol salts agar</td><td><strong>Selects</strong> for salt tolerance and <strong>differentiates</strong> by the pH change of mannitol fermentation</td></tr>
    <tr><td>Simmons citrate</td><td>Citrate utilization; bromthymol blue turns <strong>blue as pH rises</strong></td></tr>
    <tr><td>Triple sugar iron slant</td><td>Several pH changes observable on one slant</td></tr>
    <tr><td>Urea broth</td><td>Urea hydrolysis raises pH; <strong>hot pink = urease present</strong></td></tr>
    <tr><td>Rapid test strips (API 20E)</td><td>Many biochemical tests on one strip</td></tr>
    <tr><td>Bacteriophage typing; animal inoculation</td><td>Phage susceptibility; growth in an animal (for example <em>Mycobacterium leprae</em>)</td></tr>
  </table>
  <p>Replication, the last part of this objective, appears once: viruses cannot be cultured like bacteria
  because they replicate only inside a specific host cell (slide 54).</p>

  <h3 class="sub" id="dx-mechanisms">8.6 &middot; Objective 3 &mdash; Is the organism causing the disease?</h3>
  <p>The deck does not teach disease mechanisms in this lecture. What it does say is the diagnostic form
  of the question: <strong>whether the microbe recovered is actually causing the disease, or whether you
  are simply detecting normal flora</strong> &mdash; the reasoning of Koch&rsquo;s postulates, traditional
  and molecular (slide 24). Some virulence enzymes are themselves the test: <strong>hemolysins</strong> on
  blood agar and <strong>coagulase</strong> appear among the common tests (slide 17).</p>

  <h3 class="sub" id="dx-specimens">8.7 &middot; Objective 4 &mdash; Specimens, handling and transmission risk</h3>
  <p>The deck&rsquo;s epidemiology here is the specimen itself. <strong>All specimens should be considered
  potentially infectious.</strong> Results depend on <strong>collection, handling, transport and
  storage</strong>; some specimens need a preservative or fixative, others cooling, heating or other special
  treatment. Aseptic procedures and universal precautions (gloves, face shields, masks)
  <strong>mitigate but do not eliminate</strong> the risk of transmission. Slides 11&ndash;12 show collection
  sites and methods (nasopharynx, throat, sputum, blood, cerebrospinal fluid, urine by clean catch or
  catheter, feces, skin, genital swabs); a specimen then goes to direct testing or to cultivation, isolation
  and identification.</p>

  <h3 class="sub" id="dx-sensitivity">8.8 &middot; Objectives 5 &amp; 6 &mdash; Antimicrobial sensitivity testing and treatment strategy</h3>
  <p>The Kirby-Bauer <strong>disk-diffusion</strong> test gives <strong>which drug is effective and at what
  dose</strong>, and may indicate which combinations can be used. <strong>Larger zones of inhibition</strong>
  mean a more effective agent. <strong>Minimum inhibitory concentration</strong> strips add the concentration
  needed. For treatment strategy the deck&rsquo;s point is speed: faster, more accurate (genotypic)
  diagnosis means <strong>proper treatment can begin in a timely manner</strong>. Mechanisms of action and
  resistance themselves were Lecture 2&rsquo;s subject.</p>

  <h3 class="sub" id="dx-prevention">8.9 &middot; Objective 7 &mdash; Preventative interventions</h3>
  <p>The deck offers one: <strong>aseptic procedure and universal precautions</strong> during specimen
  collection and handling, which mitigate but do not eliminate transmission (slide 10). Vaccination and
  other prevention are not in this deck.</p>

  <button type="button" class="test-yourself-btn" onclick="window.openTestYourself('Test yourself &mdash; Diagnosing Infections', TEST_YOURSELF.diagnosingInfections)">Test yourself! &rarr;</button>
  <p class="src">Source: <em>Diagnosing Infections</em> (PAJ5200.Diagnosing Infections-2.pptx), Slides 1&ndash;57,
  and the PAJ 5200 syllabus instructional objectives.</p>
</section>
"""

TEST = """    diagnosingInfections: [
      {q:"Which category of identification method usually needs no culture?",
       choices:["Phenotypic","Genotypic","Immunological","Biochemical"],correct:1,
       explain:"Genotypic methods read the organism's genes directly, so they suit slow-growing Mycobacterium and hard-to-grow Legionella. Biochemical testing is phenotypic and needs growth."},
      {q:"In the complement fixation test, the sheep red cells hemolyze. What does that mean?",
       choices:["The patient's serum is positive","The complement was inactive","The antigen was absent","The patient's serum is negative"],correct:3,
       explain:"Hemolysis means complement stayed free because no antibody-antigen complex fixed it, so the serum is negative. Fixed complement leaves the cells intact, a positive result."},
      {q:"Which blot detects proteins and is used as a second test for human immunodeficiency virus status?",
       choices:["Southern","Northern","Western","Eastern"],correct:2,
       explain:"The Western blot separates proteins by electrophoresis and then detects them with antibody. Southern detects DNA and Northern detects RNA."},
      {q:"Agglutination tests detect which kind of antigen?",
       choices:["Whole-cell or insoluble antigen","Soluble antigen","Only viral antigen","Only carbohydrate antigen"],correct:0,
       explain:"Agglutination crosslinks whole-cell or insoluble antigen into visible clumps. Precipitation is the test for soluble antigen, and it needs a gel or liquid matrix."},
      {q:"On a disk-diffusion plate, what does a larger zone of inhibition indicate?",
       choices:["A resistant organism","A contaminated plate","A slower-growing organism","A more effective agent"],correct:3,
       explain:"A larger clear zone means the agent inhibited growth over a wider area, so it is more effective against that organism."}
    ],
"""
