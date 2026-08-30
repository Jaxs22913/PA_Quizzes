# -*- coding: utf-8 -*-
"""Section 3 of the Microbiology Exam 1 guide -- Microbe-Human Interactions.

Instructional objectives are VERBATIM from the Microbiology syllabus, which
numbers them, and each is answered in its own subsection in order.

The lecture recording adds nothing here: three parts were transcribed and the
emphasis scan returned no exam signposting at all, so the deck stands alone as
the source. That is unusual for this course and worth knowing rather than
re-deriving.
"""

SECTION = """
<section class="deck" id="microbe-human">
  <h2 class="deck-title">3 &middot; Microbe-Human Interactions</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Define resident flora</li>
      <li>Summarize the steps in the progression of an infectious disease</li>
      <li>Differentiate between bacterial endo and exo toxins</li>
      <li>Diagram the stages in the course of an infection</li>
      <li>Differentiate between clinical manifestations of an infectious illness</li>
      <li>Describe reservoirs of disease</li>
      <li>Describe the common sources and mitigation methods related to nosocomial infections.</li>
    </ol>
  </div>

  <div class="pearl">Two definitions carry the whole lecture, and they are not the same thing.
  <strong>Infection</strong> is a condition in which pathogenic microbes <em>penetrate host
  defences, enter tissues and multiply</em> &mdash; best case, the immune system responds
  appropriately and we recover. <strong>Disease</strong> is <em>any deviation from health</em>, a
  disruption of a tissue or organ, which may or may not be caused by microbes. Every question that
  asks you to separate the two is asking about that scope difference.</div>

  <h3 class="sub" id="mh-flora">3.1 &middot; Objective 1 &mdash; Resident flora</h3>
  <p><strong>Resident flora includes bacteria, fungi, protozoa, viruses and arthropods.</strong>
  Most areas of the body in contact with the outside environment harbour resident microbes; the
  <strong>large intestine has the highest numbers</strong>, mainly strict or facultative
  anaerobes. Internal organs and tissues are a different matter.</p>
  <table>
    <tr><th>Region</th><th>What lives there</th></tr>
    <tr><td>Skin</td><td>Staphylococci, <em>Corynebacterium</em>, <em>Propionibacterium</em>, yeasts, <em>Mycobacterium smegmatis</em></td></tr>
    <tr><td>Mouth</td><td><strong>Aerobic streptococci are the most common oral residents</strong></td></tr>
    <tr><td>Large intestine</td><td>The highest bacterial numbers in the body &mdash; <strong>10&ndash;30% of faecal volume is bacteria</strong></td></tr>
    <tr><td>Respiratory tract</td><td><em>Staphylococcus aureus</em>, <em>Neisseria meningitidis</em>. <strong>The LOWER respiratory tract is essentially sterile</strong> &mdash; and if it is not, bad things happen</td></tr>
    <tr><td>Urogenital tract</td><td>In females the flora responds to hormonal change; the urinary tract <em>should</em> be sterile except a short portion of the urethra. Same in males</td></tr>
  </table>
  <p><strong>Normally sterile sites and fluids:</strong> heart and blood vessels &middot; kidneys
  and bladder &middot; brain and spinal column &middot; middle and inner ear &middot; interior of
  the eyes &middot; <strong>blood and cerebrospinal fluid</strong> &middot; urine in the kidneys
  and bladder &middot; amniotic fluid surrounding the fetus.</p>
  <div class="pearl">The deck opens with the arithmetic for a reason: roughly <strong>30 trillion
  human cells</strong> against roughly <strong>38 trillion non-human cells</strong>, and about
  <strong>half the human genome is non-human or foreign genetic material</strong> &mdash; viral
  remnants and transposons, with more than 100 of our genes suspected to have arrived that way.
  The flora is not a contaminant sitting on top of us.</div>

  <h3 class="sub" id="mh-progression">3.2 &middot; Objective 2 &mdash; The progression of an infectious disease</h3>
  <p>The sequence the deck builds, step by step:</p>
  <table>
    <tr><th>Step</th><th>What it means</th></tr>
    <tr><td><strong>1. A pathogen with the capacity to cause disease</strong></td><td><strong>True (frank) pathogens</strong> cause disease in healthy people with normal defences &mdash; influenza and rabies viruses, the plague bacterium, the malarial protozoan. <strong>Opportunistic pathogens</strong> cause disease when defences are compromised, or when they grow somewhere unnatural to them &mdash; sometimes it is the patient's own flora doing the attacking</td></tr>
    <tr><td><strong>2. A weakened host</strong></td><td>Age (elderly, young children, premature infants) &middot; genetic or acquired immunological defects &middot; <strong>immunosuppressing drugs and organ transplants</strong> &middot; stress &middot; chronic conditions such as liver disease or diabetes &middot; inflammation &middot; primary infections already present. Many of these are what you would write as <em>comorbidities</em></td></tr>
    <tr><td><strong>3. A portal of entry</strong></td><td>Skin &middot; gastrointestinal tract &middot; respiratory tract &middot; urogenital tract &middot; <strong>conjunctiva</strong> &middot; pregnancy and birth. Agents are <strong>exogenous</strong> (from outside) or <strong>endogenous</strong> (from within)</td></tr>
    <tr><td><strong>4. Enough of them</strong></td><td>The <strong>infectious dose</strong> &mdash; see below</td></tr>
    <tr><td><strong>5. Adhesion</strong></td><td>Fimbriae (attachment pili) &middot; flagella &middot; adhesive slimes or capsules (dextran slime, glycocalyx) &middot; <strong>suction disks of protozoans</strong> &middot; <strong>viral spike or capsid proteins</strong> &middot; <strong>hooks and barbs of helminths and insect larvae</strong></td></tr>
    <tr><td><strong>6. Virulence factors</strong></td><td>Exoenzymes, toxigenicity, antiphagocytic factors &mdash; see 3.3</td></tr>
    <tr><td><strong>7. A pattern of infection</strong></td><td>Localized, systemic, mixed, primary, secondary, superinfection &mdash; see 3.4</td></tr>
    <tr><td><strong>8. A portal of exit</strong></td><td>How the pathogen departs the host, and therefore how it reaches the next one</td></tr>
  </table>
  <p><strong>Infectious dose (ID)</strong> is the <em>minimum</em> number of microbes or viral
  particles required for infection, usually expressed as <strong>ID<sub>50</sub></strong> &mdash;
  the dose sufficient to infect 50% of a given population. <strong>A SMALL ID<sub>50</sub> means
  GREATER virulence</strong>, and therefore a greater degree of pathogenicity.</p>
  <table>
    <tr><th>Organism</th><th>Infectious dose</th></tr>
    <tr><td><strong>Measles</strong></td><td><strong>1 virus particle</strong></td></tr>
    <tr><td><em>Mycobacterium tuberculosis</em></td><td>10 bacteria</td></tr>
    <tr><td>Smallpox</td><td>10&ndash;100 viral particles</td></tr>
    <tr><td>Bubonic plague</td><td>100&ndash;500 bacterial cells</td></tr>
    <tr><td>SARS-CoV-1</td><td>about 280 viral particles (animal study)</td></tr>
    <tr><td>Influenza A</td><td>about 790 viral particles</td></tr>
    <tr><td>Gonorrhoea</td><td>1,000 bacterial cells</td></tr>
    <tr><td><strong>Cholera</strong></td><td><strong>100,000,000 bacterial cells</strong></td></tr>
  </table>
  <div class="pearl">Read that table as a virulence ranking, not a list of numbers. Measles needs
  <em>one</em> particle and cholera needs a hundred million &mdash; eight orders of magnitude, and
  it is the whole reason measles spreads through a room and cholera needs contaminated water.
  Generally, contact with fewer cells than the ID<sub>50</sub> should not produce infection.</div>

  <h3 class="sub" id="mh-toxins">3.3 &middot; Objective 3 &mdash; Endotoxins against exotoxins</h3>
  <table>
    <tr><th></th><th>ENDOtoxin</th><th>EXOtoxin</th></tr>
    <tr><td><strong>What it is</strong></td><td><strong>Lipid A of the lipopolysaccharide</strong></td><td><strong>Proteins</strong></td></tr>
    <tr><td><strong>Which bacteria</strong></td><td><strong>GRAM-NEGATIVE</strong> only &mdash; it is part of their outer membrane</td><td>Certain <strong>gram-positive AND gram-negative</strong> bacteria</td></tr>
    <tr><td><strong>Released how</strong></td><td>From <strong>LYSED or DAMAGED</strong> bacteria</td><td><strong>SECRETED by LIVING</strong> bacteria</td></tr>
  </table>
  <div class="pearl">The discriminator that answers the objective in one line: an <strong>endotoxin
  is a structural lipid released when a gram-negative organism dies</strong>; an <strong>exotoxin
  is a protein a living organism secretes on purpose</strong>. Dead versus alive, lipid versus
  protein, gram-negative-only versus either.</div>
  <p><strong>The three virulence factor groups the deck names:</strong></p>
  <table>
    <tr><th>Group</th><th>What it does</th><th>Examples</th></tr>
    <tr><td><strong>Exoenzymes</strong></td><td>Attack host defences to allow <strong>deeper invasion</strong></td><td>Mucinase, hyaluronidase, coagulase, bacterial kinases</td></tr>
    <tr><td><strong>Toxigenicity</strong></td><td>The capacity to <strong>produce toxins</strong>, grouped by the tissue targeted</td><td><strong>Neurotoxins, enterotoxins, hemotoxins, nephrotoxins</strong></td></tr>
    <tr><td><strong>Antiphagocytic factors</strong></td><td>Kill or avoid phagocytes</td><td><strong>Leukocidins</strong> (&ldquo;-cidin&rdquo; = to kill) destroy leukocytes; <strong>capsules</strong> let the pathogen avoid phagocytosis or resist digestion inside a phagocyte</td></tr>
  </table>

  <h3 class="sub" id="mh-patterns">3.4 &middot; Objective 4 &mdash; The stages in the course of an infection</h3>
  <table>
    <tr><th>Pattern</th><th>Definition</th><th>Example</th></tr>
    <tr><td><strong>Localized</strong></td><td>Microbes enter and <strong>remain confined</strong> to a specific tissue</td><td>Boils, warts</td></tr>
    <tr><td><strong>Systemic</strong></td><td>Spreads to <strong>several sites and tissue fluids</strong>, usually through the bloodstream</td><td>Measles, chicken pox, anthrax, rabies</td></tr>
    <tr><td><strong>Focal</strong></td><td>An agent <strong>breaks loose from a local site</strong> and spreads</td><td>&mdash;</td></tr>
    <tr><td><strong>Mixed</strong></td><td><strong>Several microbes grow simultaneously</strong> at the infection site</td><td>&mdash;</td></tr>
    <tr><td><strong>Primary</strong></td><td>The <strong>initial</strong> infection</td><td>&mdash;</td></tr>
    <tr><td><strong>Secondary</strong></td><td>Another infection by a <strong>different microbe</strong> complicating the first</td><td>A bacterial lung infection on top of a viral upper respiratory infection</td></tr>
    <tr><td><strong>Superinfection</strong></td><td>A secondary infection resulting from <strong>disruption of the natural microflora</strong></td><td><strong>Antibiotic therapy for strep throat that results in a vaginal yeast infection</strong></td></tr>
  </table>
  <div class="pearl"><strong>Secondary and superinfection are the pair that gets confused.</strong>
  Both are a second infection. Only the superinfection is caused by <em>your treatment wiping out
  the flora that was holding the second organism in check</em>. If the stem mentions antibiotics,
  it is a superinfection.</div>

  <h3 class="sub" id="mh-manifestations">3.5 &middot; Objective 5 &mdash; Clinical manifestations</h3>
  <table>
    <tr><th></th><th>Sign</th><th>Symptom</th></tr>
    <tr><td><strong>Whose evidence</strong></td><td><strong>OBJECTIVE</strong>, as noted by an observer</td><td><strong>SUBJECTIVE</strong>, as sensed and described by the patient</td></tr>
    <tr><td><strong>Precision</strong></td><td>Often more precise, and <strong>may be measured</strong> by a clinician</td><td>Reported, not measured</td></tr>
    <tr><td><strong>The deck's example</strong></td><td>An <strong>inflamed pharynx</strong></td><td>A <strong>sore throat</strong></td></tr>
  </table>
  <p><strong>Sequelae</strong> are <strong>long-term or permanent damage to tissues or
  organs</strong> &mdash; paralysis from polio, blindness from gonococcal conjunctivitis,
  sterility from syphilis or another genital infection, deafness from meningitis, arthritis from
  Lyme disease.</p>

  <h3 class="sub" id="mh-reservoirs">3.6 &middot; Objective 6 &mdash; Reservoirs of disease</h3>
  <p>A <strong>reservoir</strong> is the <strong>primary habitat from which a pathogen
  originates</strong>. It may be living or nonliving.</p>
  <table>
    <tr><th>Type</th><th>What the deck says</th></tr>
    <tr><td><strong>Living &mdash; symptomatic</strong></td><td>Someone with an obvious, active infection is <strong>likely contagious</strong></td></tr>
    <tr><td><strong>Asymptomatic carriers</strong></td><td>May be <strong>humans or animals</strong></td></tr>
    <tr><td><strong>Passive carriers</strong></td><td><strong>Medical or dental personnel</strong> &mdash; carrying the organism without being infected by it</td></tr>
    <tr><td><strong>Vectors</strong></td><td>A <strong>live animal that transmits</strong> infectious disease &mdash; mosquitoes, fleas and ticks; also flies, fruit flies and cockroaches</td></tr>
    <tr><td><strong>Nonliving</strong></td><td><strong>Soil and water</strong></td></tr>
  </table>
  <p><strong>Zoonosis</strong> (plural zoonoses): infections of animals may spread to humans, and
  vice versa. They can be <strong>bacterial, viral, fungal or protozoan</strong> in origin &mdash;
  the category is defined by the reservoir, not the organism. <strong>A zoonotic infection cannot
  be completely eliminated without also eradicating the animal reservoir.</strong></p>
  <table>
    <tr><th>Route</th><th>Examples</th></tr>
    <tr><td><strong>Direct &mdash; horizontal</strong></td><td>Direct personal contact: kissing or sexual</td></tr>
    <tr><td><strong>Direct &mdash; vertical</strong></td><td><strong>Mother to child</strong>, transplacental or during vaginal birth</td></tr>
    <tr><td><strong>Direct &mdash; droplet</strong></td><td>Close personal contact including saliva, vomit, faeces or blood</td></tr>
    <tr><td><strong>Direct &mdash; biological vectors</strong></td><td>Mosquitoes, fleas, ticks</td></tr>
    <tr><td><strong>Indirect</strong></td><td><strong>Vehicles and fomites</strong> (inanimate objects), and <strong>airborne droplet nuclei</strong></td></tr>
  </table>

  <h3 class="sub" id="mh-nosocomial">3.7 &middot; Objective 7 &mdash; Nosocomial infections</h3>
  <p><strong>Nosocomial infections</strong>, also written <strong>HAI (hospital-acquired
  infections)</strong>, are diseases <strong>acquired or developing during a hospital stay</strong>.
  They may <strong>prolong the stay, or end in death</strong>.</p>
  <table>
    <tr><th>Facet</th><th>Content</th></tr>
    <tr><td><strong>Most common sites</strong></td><td><strong>Urinary tract, respiratory tract, and surgical incisions</strong></td></tr>
    <tr><td><strong>Most common organisms</strong></td><td>Gram-negative: <em>Escherichia coli</em>, <em>Pseudomonas</em>, <em>Klebsiella</em>. Gram-positive: staphylococci and streptococci. Fungi: yeasts. The deck notes the wider list goes by the acronym <strong>ESKAPE</strong></td></tr>
    <tr><td><strong>Mitigation</strong></td><td><strong>Universal precautions</strong> for sample collection and patient care &mdash; based on the assumption that <strong>ALL patient specimens are possibly infectious</strong></td></tr>
  </table>
  <div class="pearl">That last line is the objective's &ldquo;mitigation methods&rdquo; answer, and
  it is a principle rather than a list: you do not decide which specimens to be careful with, you
  treat all of them as infectious. The fomite link matters too &mdash; an inanimate object carries
  the organism between patients, which is why the same few organisms keep appearing.</div>

  <h3 class="sub" id="mh-epi">3.8 &middot; Epidemiology and Koch's postulates</h3>
  <p>Not separate objectives, but taught in this deck and fair game. <strong>Epidemiology</strong>
  is the study of the frequency and distribution of disease and other health-related factors in
  human populations. <strong>Reportable (notifiable) diseases</strong> must be reported to public
  health authorities; in the United States the <strong>CDC (Centers for Disease Control and
  Prevention)</strong> publishes the <strong>Morbidity and Mortality Weekly Report</strong>.</p>
  <table>
    <tr><th>Measure</th><th>Counts</th><th>Expressed as</th></tr>
    <tr><td><strong>Prevalence</strong></td><td><strong>EXISTING</strong> cases, against the entire population</td><td>Usually a percentage</td></tr>
    <tr><td><strong>Incidence</strong></td><td><strong>NEW</strong> cases over a time period, against the general healthy population</td><td>A count over time</td></tr>
    <tr><td><strong>Mortality rate</strong></td><td><strong>DEATHS</strong> due to a certain disease</td><td>Per 100,000</td></tr>
    <tr><td><strong>Morbidity rate</strong></td><td><strong>CASES</strong> &mdash; people afflicted</td><td>Per 100,000</td></tr>
  </table>
  <p><strong>Over the last hundred years the death rate from infectious disease has dropped while
  morbidity has remained relatively high.</strong> People stopped dying of these illnesses; they
  did not stop getting them.</p>
  <table>
    <tr><th>Pattern</th><th>Definition</th></tr>
    <tr><td><strong>Endemic</strong></td><td>A relatively <strong>steady frequency</strong> over a long period in a particular geographic location &mdash; often because the reservoir is present</td></tr>
    <tr><td><strong>Sporadic</strong></td><td><strong>Occasional cases at irregular intervals</strong></td></tr>
    <tr><td><strong>Epidemic</strong></td><td>Prevalence <strong>increasing beyond what is expected</strong> for that population</td></tr>
    <tr><td><strong>Pandemic</strong></td><td>A <strong>global epidemic</strong></td></tr>
  </table>
  <p><strong>Koch's postulates (1880s):</strong></p>
  <ol>
    <li>Find evidence of a particular microbe in <strong>every case</strong> of a specific disease</li>
    <li>Isolate it from an infected subject and <strong>cultivate it artificially</strong> in the laboratory</li>
    <li><strong>Inoculate a susceptible healthy subject</strong> and observe the resultant disease</li>
    <li><strong>Re-isolate</strong> the agent from the newly infected subject</li>
  </ol>
  <p><strong>They do not work well for all pathogens.</strong> <em>Mycobacterium leprae</em> and
  <em>Legionella pneumophila</em> are the two the deck names &mdash; step 2 is the sticking point
  when an organism cannot be cultivated artificially. Today they are of limited use, though still
  applied to bacterial, fungal and protozoan pathogens.</p>
  <p><strong>Molecular Koch's postulates (Falkow, 1988)</strong> exist because <strong>viruses and
  prions routinely break all the old rules</strong>:</p>
  <ol>
    <li>The <strong>phenotype or property</strong> under investigation should be <strong>associated with pathogenic strains</strong> or species</li>
    <li><strong>Inactivating</strong> the gene or genes associated with the virulence trait should produce a <strong>measurable loss of pathogenicity</strong></li>
    <li><strong>Reverting</strong> the mutated gene should <strong>restore pathogenicity</strong></li>
  </ol>
  <div class="pearl">The shift is from <em>the organism</em> to <em>the gene</em>. Koch asked which
  microbe is present in every case; Falkow asks which piece of its genome makes it dangerous
  &mdash; which is testable for an agent you cannot grow in a dish.</div>
  <button type="button" class="test-yourself-btn" onclick="window.openTestYourself('Test yourself &mdash; Microbe-Human Interactions', TEST_YOURSELF.microbehuman)">Test yourself! &rarr;</button>
</section>
"""

TOC = """  <a class="top-link" href="#microbe-human">3 &middot; Microbe-Human Interactions</a>
  <a href="#mh-flora">3.1 Objective 1 &mdash; Resident flora</a>
  <a href="#mh-progression">3.2 Objective 2 &mdash; Progression of infection</a>
  <a href="#mh-toxins">3.3 Objective 3 &mdash; Endotoxins vs exotoxins</a>
  <a href="#mh-patterns">3.4 Objective 4 &mdash; Stages in the course of infection</a>
  <a href="#mh-manifestations">3.5 Objective 5 &mdash; Clinical manifestations</a>
  <a href="#mh-reservoirs">3.6 Objective 6 &mdash; Reservoirs of disease</a>
  <a href="#mh-nosocomial">3.7 Objective 7 &mdash; Nosocomial infections</a>
  <a href="#mh-epi">3.8 Epidemiology &amp; Koch's postulates</a>
"""

TEST = """    microbehuman: [
      {q:"What separates INFECTION from DISEASE?",
       choices:["Infection is any deviation from health","Infection means microbes penetrated defences, entered tissues and multiplied","Disease requires a microbe","They are synonyms"],correct:1,
       explain:"Disease is the broader term &mdash; ANY deviation from health, microbial or not. Infection is the specific event of a pathogen breaching defences and multiplying."},
      {q:"Which body site carries the highest bacterial numbers?",
       choices:["Skin","Mouth","Large intestine","Respiratory tract"],correct:2,
       explain:"Mainly strict or facultative anaerobes. Bacteria make up 10-30% of faecal volume."},
      {q:"An endotoxin is what, from which bacteria, released how?",
       choices:["A protein, secreted by living gram-positives","Lipid A of LPS, from lysed or damaged gram-NEGATIVES","A protein, from lysed gram-negatives","Lipid A, secreted by living gram-positives"],correct:1,
       explain:"Endotoxin is structural lipid released when the organism dies. Exotoxin is a protein a LIVING organism secretes, and can come from gram-positives or gram-negatives."},
      {q:"A small ID50 means what?",
       choices:["Lower virulence","Greater virulence","No relationship to virulence","The organism is non-pathogenic"],correct:1,
       explain:"Fewer organisms needed to infect means greater virulence and a greater degree of pathogenicity. Measles needs 1 particle; cholera needs 100 million cells."},
      {q:"Antibiotics for strep throat cause a vaginal yeast infection. What is this called?",
       choices:["Secondary infection","Superinfection","Mixed infection","Focal infection"],correct:1,
       explain:"A superinfection is a secondary infection resulting from disruption of the natural microflora. The antibiotic is the clue."},
      {q:"An inflamed pharynx is a sign; a sore throat is a symptom. What distinguishes them?",
       choices:["Signs are subjective, symptoms objective","Signs are objective and observer-noted; symptoms are subjective and patient-reported","Signs occur first","Symptoms are always measurable"],correct:1,
       explain:"Signs are objective evidence noted by an observer, often measurable. Symptoms are what the patient senses and describes."},
      {q:"Which is a PASSIVE carrier, per the deck?",
       choices:["Someone with an active infection","Medical or dental personnel","A mosquito","Soil"],correct:1,
       explain:"Passive carriers carry the organism without being infected by it. A mosquito is a vector, and soil is a nonliving reservoir."},
      {q:"Why can a zoonotic infection not be eliminated?",
       choices:["The organisms are drug resistant","Not without eradicating the animal reservoir","Vaccines do not exist","It only affects animals"],correct:1,
       explain:"The animal reservoir sustains it. Zoonoses can be bacterial, viral, fungal or protozoan &mdash; the reservoir defines the category, not the organism."},
      {q:"Which sites do nosocomial infections most commonly involve?",
       choices:["Skin and soft tissue","Urinary tract, respiratory tract and surgical incisions","Bloodstream and CNS","Gastrointestinal tract"],correct:1,
       explain:"Most common organisms are E. coli, Pseudomonas and Klebsiella, plus staphylococci, streptococci and yeasts."},
      {q:"What principle underlies universal precautions?",
       choices:["Only known-positive specimens are infectious","ALL patient specimens are possibly infectious","Only blood is infectious","Precautions apply only in the ICU"],correct:1,
       explain:"That assumption is the mitigation answer for objective 7 &mdash; you do not decide which specimens to be careful with."},
      {q:"Prevalence counts what?",
       choices:["New cases over a time period","Total EXISTING cases in the population","Deaths per 100,000","Cases per 100,000"],correct:1,
       explain:"Incidence counts NEW cases over time. Mortality counts deaths and morbidity counts cases, both per 100,000."},
      {q:"Which trend does the deck describe over the last century?",
       choices:["Both death and morbidity rates fell","Death rate fell while morbidity stayed relatively high","Both rose","Death rate rose while morbidity fell"],correct:1,
       explain:"People stopped dying of infectious disease; they did not stop getting it."},
      {q:"Why do Koch's postulates fail for some pathogens?",
       choices:["The organisms are too small to see","Some cannot be cultivated artificially","They have no symptoms","They only affect animals"],correct:1,
       explain:"M. leprae and Legionella pneumophila are the two named. Viruses and prions break the rules routinely, which is why the molecular postulates exist."},
      {q:"What do the molecular Koch's postulates test?",
       choices:["The infectious dose","Genes associated with pathogenicity","The portal of entry","The reservoir"],correct:1,
       explain:"Falkow, 1988: the property should associate with pathogenic strains, inactivating the gene should reduce virulence, and reverting it should restore pathogenicity."},
    ],
"""
