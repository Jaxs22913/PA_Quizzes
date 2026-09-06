# -*- coding: utf-8 -*-
"""Section 4 of the Microbiology Exam 1 guide -- Transmission of Microorganisms.

Instructional objectives are VERBATIM from the Microbiology syllabus, which
numbers them, and each is answered in its own subsection in order. The deck's
own objective slide happens to match the syllabus word for word here -- worth
noting, because it does not always.

THIS LECTURE IS ROUGHLY HALF PUBLISHED STUDIES. The guide treats each as an
exhibit: what it found, and what its authors did NOT do. The birthday-cake
paper never identified the organisms it cultured, and the deck says so
explicitly -- that omission is more instructive than the result.

TWO FACTS COME FROM THE RECORDING RATHER THAN A SLIDE and are marked in place:
rabies is the commonest zoonosis in the United States while malaria leads
worldwide, and the colony-forming unit exists because a visible colony may have
started from one cell or from a thousand.
"""

SECTION = """
<section class="deck" id="transmission">
  <h2 class="deck-title">4 &middot; Transmission of Microorganisms</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Describe the chain of infection.</li>
      <li>Describe the relationship between fomite-transmission and nosocomial infections.</li>
      <li>Describe the relationship between fomite-transmission and antibiotic-resistant strains
      of bacteria and fungi.</li>
    </ol>
  </div>

  <div class="callout">
    <p><strong>Three objectives, and the second and third are both about fomites.</strong> That
    tells you where the weight sits: the chain of infection is the framework, and everything after
    slide 19 is an argument that non-living surfaces matter more than they look like they should.
    Roughly half the deck is published studies making that case.</p>
  </div>

  <h3 class="sub" id="tx-chain">4.1 &middot; The chain of infection</h3>
  <p>Six links, in order. Break any one and transmission stops &mdash; which is the whole point of
  infection control.</p>
  <ol class="chain">
    <li><strong>The infectious agent</strong> &mdash; and its traits, including whether it is
    already drug resistant.</li>
    <li><strong>The reservoir</strong>, known or unknown.</li>
    <li><strong>The portal of exit</strong> from the infected host.</li>
    <li><strong>The mode of transmission</strong> to other hosts.</li>
    <li><strong>The portal of entry</strong> into the new host.</li>
    <li><strong>A susceptible host</strong> &mdash; and susceptibility varies between people.</li>
  </ol>

  <h3 class="sub" id="tx-reservoirs">4.2 &middot; Reservoirs, and the four carrier states</h3>
  <p><strong>Living reservoirs:</strong> humans, animals, and &mdash; the deck marks both with a
  question mark &mdash; plants and fungi. <strong>Non-living reservoirs:</strong> soil, water, air,
  food, and <strong>fomites</strong>.</p>
  <p><strong>Human reservoirs come in four states</strong>, and the distinction that matters is
  whether the person is actually infected:</p>
  <ul>
    <li><strong>Symptomatic and infected</strong> &mdash; the obvious case.</li>
    <li><strong>Asymptomatic and infected.</strong></li>
    <li><strong>Active carriers</strong> &mdash; infected, and may or may not show symptoms.
    <strong>Mary Mallon, &ldquo;Typhoid Mary&rdquo;</strong>, carried <em>Salmonella typhi</em>
    without symptoms in the early 1900s.</li>
    <li><strong>Passive carriers</strong> &mdash; <strong>NOT infected</strong>, but still
    transmitting. The healthcare or food-service worker with poor hand hygiene.</li>
  </ul>
  <div class="callout">
    <p><strong>Active against passive is the distinction to hold.</strong> An active carrier has
    the organism in them; a passive carrier is merely carrying it on them. Both transmit.</p>
  </div>

  <h3 class="sub" id="tx-zoonoses">4.3 &middot; Zoonoses</h3>
  <p>Infections of animals that may spread to humans, <strong>and the reverse</strong>. They can be
  <strong>bacterial, viral, fungal or protozoan</strong>. Humans are often the
  <strong>accidental host</strong> &mdash; plague and anthrax are the examples given &mdash; with
  the lifecycle running through primary and secondary hosts.</p>
  <p><strong>Why they cannot be eradicated:</strong> you would have to eradicate the animal
  reservoir too, which is harder still when there are several. And a pathogen that lies dormant in
  an intermediate host as a <strong>fungal spore or protozoan cyst</strong> outlasts any campaign
  against the animal.</p>
  <p><strong>Occupational risk</strong> is named for veterinary medicine, farm work, landscaping,
  gardening, zookeeping and slaughterhouse or meat processing work.</p>
  <div class="tbl-wrap"><table class="zoo">
    <thead><tr><th>Pathogen</th><th>Reservoir</th><th>Transmission</th><th>Human to human?</th></tr></thead>
    <tbody>
      <tr><td><b>Rabies</b></td><td>Mammals</td><td>Bite / saliva</td>
          <td>Rare &mdash; organ transplantation</td></tr>
      <tr><td><b>Influenza</b></td><td>Birds, pigs</td><td>Respiratory droplet, contact</td>
          <td>Yes</td></tr>
      <tr><td><b>Ebola</b></td><td>Fruit bats, small primates</td><td>Body fluids</td>
          <td>Yes</td></tr>
      <tr><td><b>Marburg, Nipah</b></td><td>Fruit bats</td><td>Body fluids</td><td>Yes</td></tr>
    </tbody>
  </table></div>
  <div class="callout micro-audio">
    <p><strong>From the recording, not the slides.</strong> <strong>Rabies is the commonest
    zoonosis in the United States; malaria is the commonest worldwide</strong> &mdash; and there is
    almost no endemic malaria in the United States, though Hawaii has a bird form. Neither ranking
    appears on any slide, and both are the kind of fact a single question turns on.</p>
  </div>

  <h3 class="sub" id="tx-vectors">4.4 &middot; Vectors, and how they differ from reservoirs</h3>
  <p>A <strong>vector is a living thing capable of transmitting disease</strong> &mdash;
  mosquitoes, fleas and ticks; flies, fruit flies and cockroaches.</p>
  <div class="callout warn">
    <p><strong>Reservoir and vector are not the same thing, and the difference can be
    subtle.</strong> For malaria the <em>reservoir</em> may be birds while the <em>vector</em> is a
    particular species of mosquito. The reservoir <em>harbours</em>; the vector
    <em>delivers</em>.</p>
  </div>

  <h3 class="sub" id="tx-modes">4.5 &middot; The modes of transmission</h3>
  <p><strong>By contact.</strong> <em>Direct</em> splits into <strong>vertical</strong> (mother to
  child) and <strong>horizontal</strong> (usually mucous membrane contact &mdash; sexual contact,
  kissing), plus droplets from coughing, sneezing, saliva, blood, sweat and tears.
  <em>Indirect</em> contact is transmission onto inanimate surfaces first &mdash; that is
  <strong>fomite</strong> transmission, and it is where the rest of the lecture goes.</p>
  <p><strong>By vehicle.</strong> <strong>Food</strong> &mdash; gastrointestinal illness is the
  commonest result. <strong>Water</strong> &mdash; drinking water, and also pools, spas and water
  parks. <strong>Soil</strong> &mdash; contaminating produce, hands and fingernails; pinworms in
  children. <strong>Air</strong> &mdash; usually, though not always, an indoor phenomenon, which is
  why ventilation, filtration and crowding matter.</p>

  <h3 class="sub" id="tx-fomites">4.6 &middot; Fomites and hospital-acquired infection</h3>
  <p><strong>A fomite is a non-living surface or object</strong> that may transmit pathogens.
  <strong>Hospital-acquired infection (HAI)</strong> costs longer stays, long-term disability,
  preventable deaths, expense, and risk to both safety and quality of care. It is most threatening
  to the <strong>immunocompromised, paediatric, geriatric and HIV patients, and those with open
  wounds, burns or recent surgery</strong>.</p>
  <p><strong>Clinical fomites named:</strong> scalpels and syringes; <strong>catheters</strong>
  &mdash; a particular problem with biofilm-forming <em>Staphylococcus aureus</em> and
  <em>S. epidermidis</em>; bed rails and gurneys; telephones, remote controls, keyboards and
  electronic devices; floors, mops, polishers, brooms and dustpans; pillows, bedding, furniture and
  curtains; and stethoscopes, neckties, stuffed animals, greeting cards and flowers.</p>
  <p>And it is not only hospitals &mdash; a public restroom, hotel room, cruise ship cabin or
  aeroplane tray table is a fomite-filled room too.</p>

  <h3 class="sub" id="tx-studies">4.7 &middot; The studies, and what they did not do</h3>
  <div class="study">
    <h4>Birthday cake &mdash; Dawson and colleagues, 2017</h4>
    <p>Blowing out the candles put <strong>about fifteen times more bacteria</strong> on the
    frosting than the no-blow control. <strong>The authors never identified the organisms they
    cultured</strong>, though the discussion named several pathogenic genera &mdash; and they said
    nothing about fungi, yeasts or <strong>viruses</strong> in saliva. Droplet size is the link to
    face coverings: the <strong>candle test</strong> is trying to blow one out while wearing
    one.</p>
  </div>
  <div class="study">
    <h4>Keyboards &mdash; Ide and colleagues, 2019</h4>
    <p>A systematic review of <strong>75 published studies</strong>, swabbing keyboards, mice and
    pads, and portable tablets. Organisms cultured included <strong>coliforms such as
    <em>E. coli</em></strong> and <strong>MRSA</strong>.</p>
  </div>
  <div class="study">
    <h4>Viral fomites &mdash; Boone and Gerba, 2007</h4>
    <p>Pre-2007 figures: <strong>1.7 million deaths a year from diarrhoeal disease and 1.5 million
    from respiratory infection</strong>. <strong>Viruses cause about 60% of human
    infections</strong> &mdash; and <strong>viral disease cannot be cured with antibiotics</strong>,
    so prevention rests on vaccines and antivirals. <strong>Crowded indoor environments
    consistently increase morbidity and mortality</strong>: schools, daycare, nursing homes,
    offices, hotels, cruise ships and hospitals, especially paediatric wards.</p>
  </div>
  <div class="study">
    <h4>Patient-care items &mdash; Kanamori and colleagues, 2017</h4>
    <p>Soap and sanitiser dispensers, humidifiers, nebulisers, pressure transducers, stethoscopes,
    suction apparatus, thermometers, <strong>ultrasound probes and gel</strong>, blood pressure
    monitors, intravenous pumps and poles, telemetry boxes and wires.</p>
  </div>
  <div class="callout micro-audio">
    <p><strong>From the recording:</strong> results are reported as <strong>CFU &mdash;
    colony-forming units</strong> &mdash; because you cannot know whether a visible colony grew
    from one cell, a hundred or a thousand. The unit is <strong>CFU per gram or per millilitre</strong>,
    and serial dilution works for clinical specimens, urine, faeces, food, water and milk alike.</p>
  </div>

  <h3 class="sub" id="tx-disinfect">4.8 &middot; Disinfection, coatings and the history</h3>
  <p><strong>Five best practices</strong> for non-critical surfaces, in order: standardise cleaning
  policy; select <strong>EPA-registered</strong> hospital disinfectants; educate
  <strong>ALL</strong> staff <em>including environmental services</em>; monitor compliance with
  feedback; implement <strong>no-touch</strong> decontamination technology.</p>
  <p><strong>The history:</strong> <strong>Semmelweis in the 1840s</strong> &mdash; handwashing
  with <em>chlorine</em> solution by obstetricians. <strong>Lister in the 1860s</strong> &mdash;
  handwashing and wound treatment with <em>carbolic acid</em>.</p>
  <p><strong>Chemical agents</strong> &mdash; bleach, quaternary ammonium salts, phenolics &mdash;
  work only at the <strong>correct concentration and for adequate contact time</strong>, and they
  are toxic. Ozone, high-concentration hydrogen peroxide and steam <strong>require the room to be
  vacant</strong>, take time facilities may not have, and can damage surfaces and devices.</p>
  <p><strong>Coatings</strong> borrow from marine <em>anti-fouling</em> paint &mdash; copper,
  arsenic, mercury and tin compounds since the 1960s. <strong>Anti-fouling prevents attachment;
  antimicrobial kills.</strong> A hospital coating should be <strong>nontoxic, cost effective,
  commercially available, stable and durable</strong>: plastics, copper or silver alloys,
  photocatalytic coatings, specialised textiles, micro-patterned hydrophobic surfaces.</p>

  <h3 class="sub" id="tx-resistance">4.9 &middot; Fomites and antibiotic resistance</h3>
  <p><strong>Extensive antibiotic use has driven multi-drug resistance</strong>, and
  <strong>MDR, XDR and TDR</strong> strains &mdash; MRSA and carbapenem-resistant
  <em>Klebsiella pneumoniae</em> among them &mdash; are especially problematic in hospitals.
  <strong>Biofilms</strong> are polymicrobial networks resistant to cleaning, heat
  <em>and</em> drugs; <em>Staphylococcus</em> and <em>Pseudomonas</em> form them.</p>
  <p><strong>A fomite carrying a persistent pathogen cannot be told apart from a clean
  surface.</strong> That single sentence is the argument for the whole chapter.</p>
  <div class="study">
    <h4>Antiseptics in West Africa &mdash; Lompo and colleagues, 2023</h4>
    <p>Two tertiary hospitals in <strong>Burkina Faso and Benin</strong>. Contamination was highest
    in <strong>liquid soap &mdash; 51 of 69 samples</strong>. Risk factors: inconsistent
    preparation, <strong>recycled containers including used soft drink bottles</strong>, broken pump
    dispensers, and <strong>&ldquo;topping up&rdquo;</strong>. Counts above 10,000 CFU/mL were
    <strong><em>Klebsiella pneumoniae</em>, <em>Pseudomonas aeruginosa</em> and
    <em>Acinetobacter</em></strong> &mdash; all gram-negative &mdash; from
    <strong>maternity, neonatology, surgery and internal medicine</strong>.</p>
  </div>
  <div class="callout warn">
    <p><strong>How resistance moves between organisms.</strong>
    <strong>Conjugation</strong> is the big one: donor and recipient <strong>need not be the same
    genus or species</strong>, and once a cell gains a resistance plasmid <strong>every one of its
    offspring has it too</strong>. <strong>Transformation</strong> &mdash; competent cells taking
    up free DNA from the environment &mdash; matters less. <strong>Transduction</strong> requires a
    <strong>bacteriophage</strong> as the vector.</p>
    <p>Put the two halves together and the third objective answers itself: a contaminated surface
    keeps resistant organisms in circulation, and conjugation lets them hand that resistance to
    organisms of an entirely different species.</p>
  </div>
</section>"""

TOC = """  <a class="top-link" href="#transmission">4 &middot; Transmission of Microorganisms</a>
  <a class="sub-link" href="#tx-chain">4.1 The chain of infection</a>
  <a class="sub-link" href="#tx-reservoirs">4.2 Reservoirs &amp; carriers</a>
  <a class="sub-link" href="#tx-zoonoses">4.3 Zoonoses</a>
  <a class="sub-link" href="#tx-vectors">4.4 Vectors</a>
  <a class="sub-link" href="#tx-modes">4.5 Modes of transmission</a>
  <a class="sub-link" href="#tx-fomites">4.6 Fomites &amp; nosocomial infection</a>
  <a class="sub-link" href="#tx-studies">4.7 The studies</a>
  <a class="sub-link" href="#tx-disinfect">4.8 Disinfection &amp; coatings</a>
  <a class="sub-link" href="#tx-resistance">4.9 Fomites &amp; resistance</a>
"""

TEST = """    transmission: [
      {q:"How many links are in the chain of infection?",
       o:["Six","Three","Four","Eight"],a:0,
       why:"Agent, reservoir, portal of exit, mode of transmission, portal of entry, susceptible host."},
      {q:"A food worker who is NOT infected but transmits pathogens is which kind of carrier?",
       o:["Passive","Active","Asymptomatic","Symptomatic"],a:0,
       why:"An active carrier is genuinely infected; a passive carrier merely carries it on them."},
      {q:"What is the difference between a reservoir and a vector?",
       o:["The reservoir harbours; the vector delivers","They are the same thing",
          "The reservoir is always non-living","The vector is always non-living"],a:0,
       why:"Birds may be a malaria reservoir while mosquitoes are the vector."},
      {q:"Which zoonosis is commonest in the United States?",
       o:["Rabies","Malaria","Ebola","Influenza"],a:0,
       why:"From the recording: rabies leads in the United States, malaria worldwide."},
      {q:"What did the birthday-cake authors NOT do?",
       o:["Identify the organisms they cultured","Use a control","Report counts","Publish"],a:0,
       why:"They counted colonies but never identified them, which the lecture makes a point of."},
      {q:"Why is conjugation so dangerous for resistance?",
       o:["Donor and recipient need not be the same species","It requires a bacteriophage",
          "It only works within one strain","It transfers only chromosomal DNA"],a:0,
       why:"And every daughter cell of the recipient inherits the plasmid."},
      {q:"Which transfer mechanism needs a bacteriophage?",
       o:["Transduction","Conjugation","Transformation","Binary fission"],a:0,
       why:"Transformation takes up free DNA; conjugation is cell to cell."},
      {q:"Which product was most often contaminated in the West African hospital study?",
       o:["Liquid soap","Bar soap","Alcohol rub","Surgical scrub"],a:0,
       why:"51 of 69 samples, with topping up and recycled bottles as risk factors."},
    ],
"""
