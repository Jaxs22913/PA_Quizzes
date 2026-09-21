"""Microbiology Exam 1 - one paper sized to the timetable, not to the objectives.

WEIGHTING comes from the printed academic calendar. The exam is 65 questions
and the course allots five questions per scheduled lecture hour, so the six
Exam 1 lectures carry their own contact time:

    L1 General Microbiology      2 h   10
    L2 Antibiotics & Resistance  2 h    9
    L3 Microbe-Human             3 h   14
    L4 Transmission              2 h    9
    L5 Nonspecific Defenses      2 h    9
    L6 Specific Immunity         3 h   14

The six blocks total FOURTEEN scheduled hours, which at five per hour predicts
seventy rather than sixty-five. The gap of one hour is unexplained by the
syllabus, which states no such rule; these counts apportion the real 65 across
the verified hours rather than inventing the missing five.

TOPIC SELECTION inside each lecture comes from what the lecturer actually spent
time on, measured from the recordings as the number of distinct MINUTES a term
is spoken in -- a word repeated ten times in one breath is one minute of
teaching, a word touched across twelve separate minutes is a theme. So L2 leans
on resistance (17 minutes), L4 on water and food (14 and 13), L5 on
inflammation and the white count (14 and 13), L6 on antibodies and antigens
(22 and 17).

TWO EMPHASES ARE DELIBERATELY NOT FOLLOWED. The Lecture 6 lecturer spent about
twenty minutes on allergy and eleven on bone marrow donation, which would make
them the largest themes in that lecture. Allergy is not in the Lecture 6 deck
at all -- it is Lecture 7 material, outside this exam -- and the bone marrow
passage is a personal appeal to donate rather than content. Time spoken is a
weighting signal, not a licence to leave the deck.

Every stem asks exactly ONE thing. Stems are self-contained, and nothing here
cites a lecture, a lecturer or a slide in its text.
"""

L1 = "Lecture 1  Dr. Webster -  Review of General Microbiology .pptx"
L2 = "Lecture Number 2  - Antibiotics and Resistance - Dr. Webster.pptx"
L3 = "PAJ5200.Microbe-human-interactions(1).pptx"
L4 = "PAJ5200.Transmission_of_microbes-2.pptx"
L5 = "Lecture 5  Dr. Webster Nonspecific Immunity.pptx"
L6 = "PAJ5200.Specific_Immunity-2.pptx"

POOL = [

# ─────────── Lecture 1 — Review of General Microbiology (10) ───────────

dict(topic="General Microbiology", io="1.4 — Gram-positive versus Gram-negative",
  q="A Gram-positive organism is isolated from a wound. Which agent is it especially vulnerable to?",
  opts=[["Nothing that acts on the wall", "The exposed peptidoglycan makes wall-active agents more effective here rather than less."],
        ["Polymyxin", "Polymyxin disrupts the outer membrane, which Gram-positive organisms do not have, so there is nothing for it to act on."],
        ["An aminoglycoside alone", "Aminoglycosides act at the ribosome and are not the agent whose effect follows directly from a Gram-positive wall."],
        ["Lysozyme", "Correct. Its thick peptidoglycan is the enzyme's substrate and lies exposed as the outermost layer, with no outer membrane covering it."]],
  c=3, cite=L1 + ", Slides 24-29"),

dict(topic="General Microbiology", io="1.4 — Gram-positive versus Gram-negative",
  q="Which wall feature makes Gram-negative organisms resistant to many agents that kill Gram-positive ones?",
  opts=[["An outer membrane", "Correct. It acts as a permeability barrier, excluding large and hydrophobic molecules before they can reach the peptidoglycan beneath."],
        ["A thicker peptidoglycan layer", "Their peptidoglycan is thinner than a Gram-positive organism's, and thickness confers no permeability barrier in any case."],
        ["Teichoic acid", "Teichoic acid runs through the Gram-positive wall and is absent from the Gram-negative envelope."],
        ["A capsule", "A capsule resists phagocytosis rather than excluding drugs, and it is not restricted to Gram-negative organisms."]],
  c=0, cite=L1 + ", Slides 26-29"),

dict(topic="General Microbiology", io="1.4 — Gram-positive versus Gram-negative",
  q="What is released from a Gram-negative organism when the cell lyses?",
  opts=[["Exotoxin", "An exotoxin is a protein actively secreted by a living cell rather than a wall component freed on lysis."],
        ["Lipid A", "Correct. Lipid A is the toxic portion of the lipopolysaccharide built into the outer membrane, so it only reaches the host when the cell breaks apart."],
        ["Lysozyme", "Lysozyme is a host enzyme found in tears and secretions, not a bacterial product."],
        ["Teichoic acid", "Teichoic acid belongs to the Gram-positive wall and is not the toxic component released here."]],
  c=1, cite=L1 + ", Slides 26-29"),

dict(topic="General Microbiology", io="1.2 — Types of infectious pathogens",
  q="What makes mycoplasmas unusual among bacteria?",
  opts=[["They have two cell walls", "No bacterium has two walls, and what distinguishes mycoplasmas is having none."],
        ["They have no ribosomes", "No bacterium lacks ribosomes; they would be unable to make protein at all."],
        ["They have no cell wall", "Correct. The absence of peptidoglycan is the single feature from which everything else about them follows."],
        ["They have no genetic material", "Every cellular organism carries deoxyribonucleic acid, mycoplasmas included."]],
  c=2, cite=L1 + ", Slides 14-18"),

dict(topic="General Microbiology", io="1.3 — Bacterial structures that enhance pathogenicity",
  q="Which structure allows a bacterium to survive heat, drying and disinfectants for years?",
  opts=[["The plasmid", "A plasmid is extrachromosomal genetic material rather than a protective structure."],
        ["The capsule", "A capsule resists phagocytosis but is destroyed by heat and disinfectants along with the rest of the cell."],
        ["The flagellum", "The flagellum provides motility and confers no resistance to physical or chemical stress."],
        ["The endospore", "Correct. It is a dormant, dehydrated form with a tough protective coat that withstands conditions which kill the vegetative cell."]],
  c=3, cite=L1 + ", Slides 30-36"),

dict(topic="General Microbiology", io="1.3 — Bacterial structures that enhance pathogenicity",
  q="Which structure allows a bacterium to resist being engulfed by a phagocyte?",
  opts=[["The capsule", "Correct. Its slippery polysaccharide layer prevents the phagocyte from gripping the surface, so the cell cannot be taken up."],
        ["The endospore", "Sporulation is a response to environmental hardship rather than a defence against phagocytosis."],
        ["Fimbriae", "Fimbriae mediate attachment to host tissue and do nothing to prevent engulfment."],
        ["The ribosome", "The ribosome synthesises protein and has no role at the cell surface."]],
  c=0, cite=L1 + ", Slides 30-36"),

dict(topic="General Microbiology", io="1.5 — Identification methods and culture media",
  q="What does calling a medium 'selective' mean?",
  opts=[["It suppresses the growth of unwanted organisms", "Correct. Something in the medium, such as a high salt concentration, prevents organisms other than the ones sought from growing at all."],
        ["It shows visible differences between organisms", "That describes a differential medium, which lets everything grow but makes the colonies look different."],
        ["It supplies extra nutrients for fastidious organisms", "That describes an enriched medium, which supports demanding organisms rather than excluding others."],
        ["It maintains a constant incubation temperature", "Temperature is an incubation condition rather than a property of the medium itself."]],
  c=0, cite=L1 + ", Slides 43-44"),

dict(topic="General Microbiology", io="1.5 — Identification methods and culture media",
  q="Which three results are read from blood agar?",
  opts=[["Growth, no growth and partial growth", "A simple growth reading would make the medium selective; blood agar is differential because it shows how the blood is changed."],
        ["Acid, gas and no change", "Those are read from a carbohydrate fermentation medium rather than from blood agar."],
        ["Coagulase, catalase and oxidase", "Those are separate biochemical tests performed on an isolate rather than readings from a plate."],
        ["Gamma, alpha and beta haemolysis", "Correct. Each organism digests the haemoglobin to a different degree — none, partial, or complete — and the plate shows that difference directly."]],
  c=3, cite=L1 + ", Slides 43-44"),

dict(topic="General Microbiology", io="1.6 — The bacterial growth curve",
  q="Bacterial growth refers to an increase in what?",
  opts=[["Cell number", "Correct. The individual cells stay much the same size; what rises is how many of them there are, through repeated binary fission."],
        ["Cell size", "Cells enlarge only slightly before dividing, and growth is defined by the number of cells rather than their dimensions."],
        ["Colony diameter", "Colony spread on a plate reflects motility and available nutrient rather than defining growth itself."],
        ["Genome size", "The genome is copied faithfully at each division rather than enlarging."]],
  c=0, cite=L1 + ", Slides 37-40"),

dict(topic="General Microbiology", io="1.11 — Microbial control and the death curve",
  q="A disinfectant reduces a population from 10,000,000 organisms to 10,000. How many decimal reductions is that?",
  opts=[["One thousand", "A thousand is the fold-reduction achieved rather than the number of decimal steps it represents."],
        ["Four", "A fall from ten million to ten thousand is a thousandfold, which is three tenfold steps rather than four."],
        ["Six", "Six reductions would take ten million down to ten organisms rather than to ten thousand."],
        ["Three", "Correct. Each decimal reduction removes ninety per cent of whatever remains, so a thousandfold fall is three tenfold steps."]],
  c=3, cite=L1 + ", Slides 62-68"),

# ─────────── Lecture 2 — Antibiotics and Resistance (9) ───────────

dict(topic="Antibiotics and Resistance", io="2.3 — Therapeutic index",
  q="A drug has a toxic dose for half the population of 400 milligrams and an effective dose for half the population of 50 milligrams. What is its therapeutic index?",
  opts=[["350", "Subtracting the doses gives a figure that changes with the units used and cannot be compared between drugs."],
        ["0.125", "This inverts the ratio; putting the effective dose on top yields a value below one for every usable drug."],
        ["8", "Correct. The index is the toxic dose divided by the effective dose, so 400 over 50 gives 8."],
        ["450", "Adding the doses produces a number with no meaning; the index is a ratio."]],
  c=2, cite=L2 + ", Slides 18-20"),

dict(topic="Antibiotics and Resistance", io="2.3 — Therapeutic index",
  q="What does a LARGER therapeutic index tell you about a drug?",
  opts=[["It is more likely to be bactericidal", "Whether a drug kills or merely inhibits is independent of its safety margin."],
        ["It is safer", "Correct. A wide gap between the dose that works and the dose that harms leaves more room for error in dosing and for variation between patients."],
        ["It is more potent", "Potency describes how small the effective dose is; the index measures the margin between working and toxic doses."],
        ["It acts more quickly", "Onset depends on absorption and distribution rather than on the ratio between two doses."]],
  c=1, cite=L2 + ", Slides 18-20"),

dict(topic="Antibiotics and Resistance", io="2.7 — Mechanisms of drug resistance",
  q="An antibiotic course is followed by an infection that no longer responds to it. What has happened to the bacterial population?",
  opts=[["The immune system spared the resistant cells", "The immune system does not discriminate by antibiotic susceptibility; the drug is what removes the susceptible population."],
        ["The antibiotic caused resistance genes to form", "Exposure selects among variation that already exists; the mutations or acquired genes were present before the drug arrived."],
        ["The bacteria learned to avoid the drug", "Bacteria have no such adaptive capacity within a generation; what changes is which organisms survive to reproduce."],
        ["Resistant organisms already present were selected for", "Correct. The drug removes the susceptible competition rather than creating anything, so the few organisms that already carried resistance are left to multiply unopposed."]],
  c=3, cite=L2 + ", Slides 45-52"),

dict(topic="Antibiotics and Resistance", io="2.7 — Mechanisms of drug resistance",
  q="Which resistance mechanism destroys the antibiotic molecule itself?",
  opts=[["Target modification", "Modifying the binding site leaves the drug chemically unchanged and simply unable to attach."],
        ["An efflux pump", "A pump removes the drug intact rather than destroying it, keeping the internal concentration too low to act."],
        ["Enzymatic inactivation", "Correct. An enzyme such as beta-lactamase chemically cleaves the drug, so it can no longer bind its target however much of it is present."],
        ["Reduced permeability", "Reduced permeability keeps the drug out of the cell rather than breaking it apart."]],
  c=2, cite=L2 + ", Slides 45-52"),

dict(topic="Antibiotics and Resistance", io="2.7 — Mechanisms of drug resistance",
  q="Which resistance mechanism keeps the antibiotic from ever reaching a useful concentration inside the cell?",
  opts=[["Target modification", "An altered target allows the drug to accumulate normally but prevents it from binding."],
        ["Enzymatic inactivation", "An enzyme destroys the drug chemically rather than controlling how much of it is inside the cell."],
        ["Efflux pumping", "Correct. The pump exports the drug as fast as it enters, so it never accumulates to a level that would inhibit its target."],
        ["Biofilm formation", "A biofilm impedes penetration into the community rather than acting at the individual cell membrane."]],
  c=2, cite=L2 + ", Slides 45-52"),

dict(topic="Antibiotics and Resistance", io="2.6 — Mechanisms of action",
  q="Which bacterial target is completely absent from human cells?",
  opts=[["The peptidoglycan cell wall", "Correct. Nothing in a human cell corresponds to it, which is why drugs that attack it are among the safest antimicrobials available."],
        ["The ribosome", "Human cells have ribosomes too; they differ in size from the bacterial ones but are certainly present."],
        ["The plasma membrane", "Every human cell has a plasma membrane, which is why membrane-active agents such as the polymyxins are comparatively toxic."],
        ["Deoxyribonucleic acid", "Human cells carry deoxyribonucleic acid, so it cannot be exploited for selective toxicity on its own."]],
  c=0, cite=L2 + ", Slides 24-32"),

dict(topic="Antibiotics and Resistance", io="2.6 — Mechanisms of action",
  q="Which step do the penicillins block?",
  opts=[["Protein synthesis at the ribosome", "That is where the aminoglycosides, macrolides and tetracyclines act."],
        ["Crosslinking of the cell wall", "Correct. The beta-lactam ring inactivates the transpeptidase that links peptidoglycan strands, so the wall cannot be completed and the cell bursts."],
        ["Folate synthesis", "Folate synthesis is blocked by the sulfonamides and trimethoprim."],
        ["Deoxyribonucleic acid replication", "Replication is disrupted by the fluoroquinolones acting on bacterial gyrase."]],
  c=1, cite=L2 + ", Slides 24-32"),

dict(topic="Antibiotics and Resistance", io="2.2 — Prokaryotic versus eukaryotic targets",
  q="Why are there fewer drugs available against fungal and protozoal infections than against bacterial ones?",
  opts=[["Those pathogens are eukaryotes, like us", "Correct. Selective toxicity needs a difference to exploit, and a eukaryotic pathogen's structure and physiology closely resemble our own, so safe targets are scarce."],
        ["Those pathogens reproduce too slowly", "Slow growth complicates treatment duration but is not why the range of available drugs is narrow."],
        ["Those infections resolve on their own", "Many are severe and even fatal untreated, so the limitation is pharmacological rather than a lack of need."],
        ["Those pathogens have tougher cell walls", "Fungi do have walls, but the constraint is their eukaryotic cell biology rather than wall toughness."]],
  c=0, cite=L2 + ", Slides 12-16"),

dict(topic="Antibiotics and Resistance", io="2.6 — Bacteriostatic versus bactericidal",
  q="What does a bacteriostatic drug do?",
  opts=[["Kills the organism outright", "Killing outright defines a bactericidal agent; a bacteriostatic one only halts replication and waits on host immunity."],
        ["Inhibits growth without killing", "Correct. It halts replication and leaves the host's immune system to clear the organisms that are already there."],
        ["Blocks the organism from attaching to host cells", "Blocking attachment is a function of antibody rather than a category of antimicrobial action."],
        ["Prevents the organism from acquiring resistance genes", "No antimicrobial works by blocking gene transfer; a bacteriostatic drug simply inhibits growth without killing."]],
  c=1, cite=L2 + ", Slides 33-36"),

# ─────────── Lecture 3 — Microbe-Human Interactions (14) ───────────

dict(topic="Microbe-Human Interactions", io="1 — Define resident flora",
  q="By what mechanism does resident flora protect the host?",
  opts=[["It raises local temperature to inhibit invaders", "Fever is a host response driven by cytokines rather than anything the flora produce."],
        ["It secretes antibody against pathogens", "Antibody is produced by plasma cells of the host immune system rather than by bacteria."],
        ["It digests pathogens as they arrive", "Flora compete for space and nutrients rather than consuming newcomers, which is what denies a pathogen anywhere to establish."],
        ["It occupies the niche first", "Correct. Competition for space and nutrients means a newly arrived pathogen finds nowhere to establish and nothing left to consume."]],
  c=3, cite=L3 + ", Slides 8-16"),

dict(topic="Microbe-Human Interactions", io="1 — Define resident flora",
  q="Which body site carries the largest resident microbial population?",
  opts=[["Small intestine", "The small intestine carries a rising population along its length but stays far below the colon, partly because transit is quicker there."],
        ["Oral cavity", "The mouth is heavily colonised but does not approach the numbers found in the large intestine."],
        ["Nasal passages", "The nose carries a modest resident population, including the staphylococci that matter for surgical infection, but nothing near colonic numbers."],
        ["Large intestine", "Correct. The colon holds by far the densest population in the body, which is why disturbing it with antibiotics has such marked consequences."]],
  c=3, cite=L3 + ", Slides 8-16"),

dict(topic="Microbe-Human Interactions", io="1 — Define resident flora",
  q="Which of these is normally sterile?",
  opts=[["Conjunctiva", "The conjunctiva carries a sparse resident population despite the flushing action of tears."],
        ["Large intestine", "The colon is the most heavily colonised site in the body; the sterile compartments are blood and cerebrospinal fluid."],
        ["Distal urethra", "A short portion of the urethra carries flora, which is why a voided specimen is not sterile."],
        ["Cerebrospinal fluid", "Correct. It is an internal compartment that no organism should reach, which is why any growth from it is significant."]],
  c=3, cite=L3 + ", Slides 8-16"),

dict(topic="Microbe-Human Interactions", io="1 — Define resident flora",
  q="What defines a TRUE pathogen?",
  opts=[["It is always Gram-negative", "Gram reaction has no bearing on whether an organism can overcome normal defences."],
        ["It sickens a healthy person", "Correct. It carries enough virulence to overcome intact defences, which is precisely what an opportunist cannot do."],
        ["It always produces an exotoxin", "Toxin production is one virulence factor among many and is not what defines the category."],
        ["It is acquired only in hospital", "Where an organism is acquired describes the setting rather than its capacity to cause disease."]],
  c=1, cite=L3 + ", Slides 18-24"),

dict(topic="Microbe-Human Interactions", io="3 — Endotoxins versus exotoxins",
  q="When is endotoxin released?",
  opts=[["When the organism is phagocytosed intact", "Engulfment alone does not release it; the cell must be broken apart."],
        ["Continuously, secreted by the living cell", "Active secretion by a living cell describes an exotoxin; endotoxin is a wall component freed only when the cell lyses."],
        ["Only during sporulation", "Sporulation is a dormancy process unrelated to endotoxin release."],
        ["When the bacterial cell lyses", "Correct. It is a structural component of the Gram-negative outer membrane, so it only reaches the host once the cell breaks apart."]],
  c=3, cite=L3 + ", Slides 40-46"),

dict(topic="Microbe-Human Interactions", io="3 — Endotoxins versus exotoxins",
  q="Which organisms produce endotoxin?",
  opts=[["All bacteria equally", "Only the Gram-negative envelope carries the lipopolysaccharide from which endotoxin comes."],
        ["Gram-positive bacteria", "Gram-positive organisms have no outer membrane and therefore no lipopolysaccharide."],
        ["Fungi", "Fungal walls are built on chitin and glucan and contain no lipopolysaccharide."],
        ["Gram-negative bacteria", "Correct. Endotoxin is the lipid A portion of lipopolysaccharide, which is built into the Gram-negative outer membrane and found nowhere else."]],
  c=3, cite=L3 + ", Slides 40-46"),

dict(topic="Microbe-Human Interactions", io="2 — Steps in the progression of infectious disease",
  q="Which structure allows a bacterium to attach to host tissue?",
  opts=[["The capsule", "The capsule resists phagocytosis rather than mediating attachment."],
        ["Fimbriae", "Correct. They are the adhesins that anchor the organism to a specific receptor on the host cell, without which it would simply be washed away."],
        ["The endospore", "The endospore is a dormant survival form and plays no part in adhesion."],
        ["The ribosome", "The ribosome synthesises protein inside the cell; attachment to host tissue is mediated by surface fimbriae."]],
  c=1, cite=L3 + ", Slides 30-38"),

dict(topic="Microbe-Human Interactions", io="4 — Stages in the course of an infection",
  q="What distinguishes a sign from a symptom?",
  opts=[["A sign is treatable; a symptom is not", "Treatability has no bearing on the definition; what separates them is whether the finding is observed or felt."],
        ["A sign is felt by the patient; a symptom is observed", "This reverses them: the sign is what the clinician observes and the symptom is what the patient feels."],
        ["A sign appears early; a symptom appears late", "Timing does not define either term; the distinction is whether the finding is observed or reported."],
        ["A sign is observed; a symptom is felt by the patient", "Correct. The distinction is who perceives it, which is why a sign can be recorded objectively and a symptom must be reported."]],
  c=3, cite=L3 + ", Slides 50-58"),

dict(topic="Microbe-Human Interactions", io="4 — Stages in the course of an infection",
  q="What is a sequela?",
  opts=[["A second infection following the first", "A further infection following the first is a secondary infection; a sequela is lasting damage left behind."],
        ["Lasting damage after the illness", "Correct. It is the permanent tissue or organ injury left behind once the acute illness has resolved, such as blindness following gonococcal conjunctivitis."],
        ["The interval before symptoms appear", "That is the incubation period, which precedes illness rather than following it."],
        ["A relapse of the original illness", "A relapse is the same illness returning rather than lasting damage from it."]],
  c=1, cite=L3 + ", Slides 50-58"),

dict(topic="Microbe-Human Interactions", io="3.8 — Koch's postulates",
  q="Which step completes Koch's postulates once a laboratory isolate has produced disease in a healthy subject?",
  opts=[["Re-isolate it from the new subject", "Correct. The set closes by recovering the same organism from the newly infected subject, which is what ties the cultivated isolate to the disease it produced."],
        ["Sequence the isolate's genome", "Gene sequencing belongs to the molecular postulates published in the 1980s; the original four steps are cultural rather than genetic."],
        ["Show it is absent in healthy people", "The first postulate asks for evidence of the microbe in every case of the disease, not for proof that it is missing from the well."],
        ["Treat the subject and confirm recovery", "Recovery after treatment is not one of the four steps; the sequence ends by recovering the agent from the newly infected subject."]],
  c=0, cite=L3 + ", Slide 59"),

dict(topic="Microbe-Human Interactions", io="3.2 — Portals of entry",
  q="An infectious agent arising from the patient's own resident flora is described as which of the following?",
  opts=[["Endogenous", "Correct. The term means the agent originates from within the host, which is what happens when resident flora reach a site they do not normally occupy."],
        ["Exogenous", "This describes an agent acquired from outside the body, which is the opposite origin to the one in the question."],
        ["Zoonotic", "This describes an agent passed from an animal host, which says nothing about whether it arose within the patient."],
        ["Nosocomial", "This describes an infection acquired during a hospital stay, which is about where it was caught rather than where it came from."]],
  c=0, cite=L3 + ", Slide 25"),

dict(topic="Microbe-Human Interactions", io="3.2 — Infectious dose",
  q="What does a small infectious dose fifty indicate about an organism?",
  opts=[["Lower virulence", "The relationship runs the other way: needing fewer organisms marks a more virulent agent, not a less virulent one."],
        ["Greater virulence", "Correct. Fewer particles are needed to infect half of an exposed population, which is what a greater degree of pathogenicity means."],
        ["A longer incubation period", "Incubation measures the delay before signs appear and is not what the infectious dose figure describes."],
        ["A narrower host range", "Host range describes which species can be infected, which is independent of how many particles establish infection."]],
  c=1, cite=L3 + ", Slide 27"),

dict(topic="Microbe-Human Interactions", io="3.7 — Nosocomial infections",
  q="Which sites are most commonly involved in hospital-acquired infection?",
  opts=[["Mouth, oesophagus and stomach lining", "The upper digestive tract is not among the commonest sites, which are the urinary tract, the airway and surgical wounds."],
        ["Urinary tract, airway and surgical wounds", "Correct. Each of the three is routinely instrumented, so catheters, ventilation and surgery breach the barrier that would otherwise exclude organisms."],
        ["Bone, joint spaces and middle ear", "These infections do occur in hospital but are not among the three sites named as the commonest."],
        ["Liver, spleen and pancreatic duct", "Solid abdominal organs are not the usual sites; infection concentrates where a device or incision crosses a barrier."]],
  c=1, cite=L3 + ", Slide 50"),

dict(topic="Microbe-Human Interactions", io="3.5 — Signs versus symptoms",
  q="What distinguishes a sign from a symptom?",
  opts=[["A sign is reported by the patient", "That describes a symptom, which is the patient's own account; a sign is what someone else can see or measure."],
        ["A sign appears only in severe disease", "Severity does not decide the term, which turns on whether an observer rather than the patient detects it."],
        ["A sign is observed objectively", "Correct. It is objective evidence noted by an observer and can often be measured, which is what separates it from what the patient reports."],
        ["A sign appears before the incubation period", "Timing does not decide the term; signs are defined by being objectively observable, not by when they arrive."]],
  c=2, cite=L3 + ", Slide 38"),

# ─────────── Lecture 4 — Transmission of Microorganisms (9) ───────────

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="How many links make up the chain of infection?",
  opts=[["Eight", "Eight overstates it; the chain has six links, running from the agent through to the susceptible host."],
        ["Four", "Four omits several links; the chain runs from the agent through to the susceptible host in six steps."],
        ["Six", "Correct. Agent, reservoir, portal of exit, mode of transmission, portal of entry and susceptible host, and breaking any one of them interrupts spread."],
        ["Three", "Three is far too few to describe the route from reservoir to host."]],
  c=2, cite=L4 + ", Slides 6-14"),

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="Which link in the chain of infection does hand hygiene break?",
  opts=[["The susceptible host", "Protecting the host describes vaccination or prophylaxis rather than hand hygiene."],
        ["The reservoir", "Removing the reservoir would mean eliminating where the organism lives and multiplies, which hand hygiene does not do."],
        ["The mode of transmission", "Correct. Washing removes organisms from the hands that would otherwise carry them from one host to the next, which is the link most readily interrupted."],
        ["The portal of exit", "Closing the portal of exit would mean containing secretions, as a mask or dressing does."]],
  c=2, cite=L4 + ", Slides 6-14"),

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="What is a fomite?",
  opts=[["A contaminated non-living object", "Correct. It is any inanimate item that carries organisms from one person to another, such as a stethoscope or a keyboard."],
        ["A living carrier showing no symptoms", "A symptomless living carrier is a carrier rather than a fomite."],
        ["An airborne droplet nucleus", "A droplet nucleus is a suspended particle rather than an object."],
        ["An insect that transmits disease", "An insect that transmits disease is a vector, which is living."]],
  c=0, cite=L4 + ", Slides 40-52"),

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="What distinguishes a PASSIVE carrier from an active one?",
  opts=[["The passive carrier has been treated", "Treatment status defines neither category; the passive carrier is distinguished by never being infected at all."],
        ["The passive carrier shows no symptoms", "An active carrier may also be symptomless; the distinction is whether they are infected at all."],
        ["The passive carrier is not infected", "Correct. They simply transfer organisms on hands or clothing without the organism ever establishing in them, which is why hand hygiene matters so much among staff."],
        ["The passive carrier transmits only by air", "Route of transmission does not separate them; the passive carrier is simply never infected themselves."]],
  c=2, cite=L4 + ", Slides 16-26"),

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="What separates a vector from a reservoir?",
  opts=[["The vector carries the organism; the reservoir harbours it", "Correct. The reservoir is where the organism normally lives and multiplies, while the vector merely transports it to a new host."],
        ["The vector harbours the organism; the reservoir carries it", "This reverses them: the reservoir is where the organism lives and multiplies, and the vector merely transports it."],
        ["The vector is inanimate; the reservoir is living", "An inanimate carrier is a fomite; a vector is by definition living."],
        ["The vector is always an insect; the reservoir always an animal", "Neither is restricted to those categories; the distinction is whether the organism lives there or is merely carried."]],
  c=0, cite=L4 + ", Slides 16-26"),

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="Why can a zoonotic infection not be eradicated the way smallpox was?",
  opts=[["Zoonotic organisms resist all antimicrobials", "Many are readily treatable; the obstacle is the reservoir rather than resistance."],
        ["Zoonotic organisms mutate too quickly", "Mutation rate complicates vaccine design for some agents but is not the barrier to eradication here."],
        ["Zoonotic infections are always viral", "Zoonoses may be bacterial, viral, fungal or protozoan, and smallpox itself was a virus that was eradicated."],
        ["The animal reservoir persists", "Correct. Eradication requires removing every place the organism can live, and an infection maintained in animals continues however many human cases are cured."]],
  c=3, cite=L4 + ", Slides 28-36"),

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="Which patients are most at risk from hospital-acquired infection?",
  opts=[["Outpatients attending clinics", "Hospital-acquired infection is defined by acquisition during an admission."],
        ["The young and otherwise healthy", "Intact immunity is protective, making this group the least at risk."],
        ["The immunocompromised", "Correct. Impaired defences allow organisms of low virulence, including the patient's own flora, to establish infection they could not otherwise cause."],
        ["Patients on short admissions", "Longer stays with more devices carry higher risk than short ones."]],
  c=2, cite=L4 + ", Slides 40-46"),

dict(topic="Transmission of Microorganisms", io="4.1 — Transmission by vehicle",
  q="Contaminated drinking water spreads infection through which route?",
  opts=[["Direct contact", "Direct contact needs person-to-person transfer such as touching or kissing, with no intermediate substance carrying the organism."],
        ["Vehicle", "Correct. Water is one of the named vehicles, alongside food, soil and air, each carrying the agent to a host with no contact between people."],
        ["Vector", "A vector is a living thing that carries the agent, such as a mosquito or a tick, rather than a contaminated substance."],
        ["Fomite", "A fomite is a contaminated inanimate object; water is classed separately as a vehicle, with food, soil and air."]],
  c=1, cite=L4 + ", Slide 18"),

dict(topic="Transmission of Microorganisms", io="4.1 — Contact transmission",
  q="Person-to-person spread from a mother to her child is termed which of the following?",
  opts=[["Horizontal transmission", "Horizontal spread runs between people of one generation, typically across mucous membranes during sexual contact or kissing."],
        ["Indirect contact", "Indirect contact has droplets or body fluids land on an object first, which is not what passing from mother to child describes."],
        ["Vertical transmission", "Correct. Vertical transmission is the mother-to-child route, passing down a generation rather than between members of the same one."],
        ["Vehicle transmission", "Vehicle transmission works through food, water, soil or air rather than directly between two people."]],
  c=2, cite=L4 + ", Slide 17"),

# ─────────── Lecture 5 — Nonspecific Host Defenses (9) ───────────

dict(topic="Nonspecific Host Defenses", io="3.1 — The three lines of defense",
  q="Which of the three lines of defense is the specific one?",
  opts=[["All three equally", "Only the third line recognises a particular antigen and remembers it."],
        ["The first", "The first line is a set of barriers that block anything indiscriminately, which is the definition of nonspecific."],
        ["The second", "The second line is protective cells and antimicrobial substances acting without regard to which organism is present."],
        ["The third", "Correct. Only the third is acquired through exposure to a particular antigen and carries memory of it; the first two act identically against anything."]],
  c=3, cite=L5 + ", Slide 4"),

dict(topic="Nonspecific Host Defenses", io="3.2 — First line barriers",
  q="Into which first-line category does lysozyme fall?",
  opts=[["Microbiological", "The microbiological barrier is the resident flora competing for the niche."],
        ["Physical", "A physical barrier obstructs mechanically, as intact skin and the ciliary escalator do."],
        ["Chemical", "Correct. It is an enzyme that digests peptidoglycan, attacking the invader chemically rather than obstructing it."],
        ["Genetic", "The genetic barrier refers to inherited resistance rather than a secreted enzyme."]],
  c=2, cite=L5 + ", Slides 13-18"),

dict(topic="Nonspecific Host Defenses", io="3.4 — The leukocytes",
  q="Which leukocyte is the most numerous?",
  opts=[["The monocyte", "Monocytes account for only about 3 to 7 per cent; the neutrophil dominates the differential at 55 to 90 per cent."],
        ["The lymphocyte", "Lymphocytes come second at about 20 to 35 per cent, behind neutrophils at roughly 55 to 90 per cent."],
        ["The neutrophil", "Correct. Neutrophils make up roughly 55 to 90 per cent of the differential, which is why a raised total count so often reflects a neutrophil response."],
        ["The eosinophil", "Eosinophils are only 1 to 3 per cent of the differential; neutrophils make up 55 to 90 per cent."]],
  c=2, cite=L5 + ", Slides 66-70"),

dict(topic="Nonspecific Host Defenses", io="3.5 — Macrophage versus neutrophil",
  q="What can a macrophage do that a neutrophil cannot?",
  opts=[["Release histamine", "Histamine release belongs to basophils and mast cells rather than to either phagocyte."],
        ["Phagocytose bacteria", "Both are phagocytes, so engulfment does not separate them; only the macrophage presents antigen to lymphocytes."],
        ["Migrate towards a chemical signal", "Both move by chemotaxis toward infection; the macrophage is distinguished by presenting antigen to lymphocytes."],
        ["Present antigen to lymphocytes", "Correct. This is the step that recruits the specific immune system, which is why the macrophage bridges innate and adaptive defence while the neutrophil simply kills and dies."]],
  c=3, cite=L5 + ", Slides 66-72"),

dict(topic="Nonspecific Host Defenses", io="3.6 — White blood count with differential",
  q="What does the differential add that a total white cell count alone cannot give?",
  opts=[["Whether the cell types are in normal proportion", "Correct. A normal total can conceal a badly skewed mix, and it is the proportion that distinguishes a bacterial from a viral pattern."],
        ["The total number of white cells, more precisely", "The plain count already gives the total; the differential adds the proportion of each cell type."],
        ["The identity of the infecting organism", "It can suggest a pattern but cannot name an organism; that needs culture or molecular testing."],
        ["The antibody titre against the organism", "Antibody titres are a separate serological test; the differential reports the proportion of each white cell type."]],
  c=0, cite=L5 + ", Slides 70-74"),

dict(topic="Nonspecific Host Defenses", io="3.7 — Inflammation",
  q="Which set lists the four classical signs of inflammation?",
  opts=[["Swelling, pain, itching and scaling", "Itching and scaling are not classical signs; the four are redness, heat, swelling and pain."],
        ["Redness, heat, swelling and pain", "Correct. Rubor, calor, tumor and dolor, with loss of function sometimes added as a fifth."],
        ["Heat, swelling, bleeding and numbness", "Bleeding and numbness are not classical signs of inflammation."],
        ["Redness, heat, pus and fever", "Pus and fever are consequences of some inflammation rather than the classical four signs."]],
  c=1, cite=L5 + ", Slides 34-40"),

dict(topic="Nonspecific Host Defenses", io="3.8 — Fever",
  q="What causes fever?",
  opts=[["Endotoxin acting directly on the skin", "Endotoxin works by inducing host cytokines rather than acting on the skin."],
        ["Dehydration raising core temperature", "Fluid loss can raise temperature passively but fever is a regulated change in the set point."],
        ["Histamine released from mast cells", "Histamine drives the local vascular changes of inflammation rather than the systemic set-point change."],
        ["Cytokines reset the set point", "Correct. Interleukin-1, interleukin-6 and tumour necrosis factor act systemically on the hypothalamus, which then defends a higher target temperature."]],
  c=3, cite=L5 + ", Slides 40-46"),

dict(topic="Nonspecific Host Defenses", io="3.9 — Interferon",
  q="What does interferon do to a virus?",
  opts=[["It destroys viral particles directly", "Interferon has no direct virucidal action; it induces an antiviral state in neighbouring uninfected cells."],
        ["It prevents spread rather than killing the virus", "Correct. It acts on neighbouring uninfected cells, inducing an antiviral state so the infection cannot propagate; the already-infected cell is not rescued."],
        ["It coats the virus so phagocytes engulf it", "Coating a target for phagocytosis is opsonisation, performed by antibody and complement."],
        ["It lyses the infected cell immediately", "Killing infected cells is the work of cytotoxic T cells and natural killer cells."]],
  c=1, cite=L5 + ", Slides 48-52"),

dict(topic="Nonspecific Host Defenses", io="3.10 — Complement",
  q="In what order are the three complement pathways activated?",
  opts=[["Classical, then lectin, then alternative", "That is the order in which the pathways were discovered, which runs opposite to the order of activation."],
        ["Alternative, then lectin, then classical", "Correct. The alternative pathway fires immediately with no prior recognition needed, the lectin pathway follows, and the classical comes last because it waits on antibody."],
        ["Lectin, then alternative, then classical", "The alternative pathway is the one that can act immediately, so it comes first."],
        ["Classical, then alternative, then lectin", "The classical pathway is the slowest because it requires antibody to be present."]],
  c=1, cite=L5 + ", Slides 42-46"),

# ─────────── Lecture 6 — Specific Immunity (14) ───────────

dict(topic="Specific Immunity", io="1 — Relate innate and specific immunity",
  q="A newborn receives antibody across the placenta. Which type of immunity is that?",
  opts=[["Artificial passive", "Artificial passive immunity means receiving antibody as a deliberate treatment, such as an immunoglobulin injection."],
        ["Natural active", "Natural active immunity follows actually having the infection and mounting your own response."],
        ["Natural passive", "Correct. Nothing was engineered, so it is natural, and the infant receives ready-made antibody rather than producing it, so it is passive and temporary."],
        ["Artificial active", "Artificial active immunity is what vaccination produces, where the recipient makes their own response."]],
  c=2, cite=L6 + ", Slides 6-12"),

dict(topic="Specific Immunity", io="1 — Relate innate and specific immunity",
  q="Which type of immunity does vaccination produce?",
  opts=[["Artificial active", "Correct. The antigen is administered deliberately, so it is artificial, and the recipient mounts their own response and forms memory, so it is active."],
        ["Artificial passive", "Passive immunity means receiving preformed antibody, which confers no memory and fades."],
        ["Natural active", "Natural active immunity follows genuine infection rather than deliberate administration."],
        ["Natural passive", "Natural passive immunity is antibody received across the placenta or in breast milk."]],
  c=0, cite=L6 + ", Slides 6-12"),

dict(topic="Specific Immunity", io="4 — Antibody structure, class and function",
  q="How many chains make up an antibody monomer?",
  opts=[["Six", "Six exceeds the monomer, which is built from four chains: two heavy and two light."],
        ["Eight", "Eight would describe a larger assembly rather than the basic monomer."],
        ["Four", "Correct. Two identical heavy chains and two identical light chains form the Y-shaped molecule."],
        ["Two", "Two chains would be half a monomer; the complete unit has two heavy and two light."]],
  c=2, cite=L6 + ", Slides 40-48"),

dict(topic="Specific Immunity", io="4 — Antibody structure, class and function",
  q="Which antibody class appears first in a new infection?",
  opts=[["Immunoglobulin A", "Immunoglobulin A is secreted onto mucosal surfaces rather than leading the systemic response."],
        ["Immunoglobulin E", "Immunoglobulin E is present in trace amounts and is associated with allergy and parasites."],
        ["Immunoglobulin M", "Correct. It is produced first and is by far the largest, its ten binding sites making it highly effective at agglutinating antigen early on."],
        ["Immunoglobulin G", "Immunoglobulin G dominates later and in the secondary response rather than appearing first."]],
  c=2, cite=L6 + ", Slides 50-60"),

dict(topic="Specific Immunity", io="4 — Antibody structure, class and function",
  q="Which antibody class guards mucosal surfaces?",
  opts=[["Immunoglobulin M", "Immunoglobulin M is too large to be secreted efficiently onto surfaces."],
        ["Immunoglobulin A", "Correct. It is secreted across epithelium onto the mucous membranes of the gut, airway and urogenital tract, where it blocks attachment."],
        ["Immunoglobulin D", "Immunoglobulin D sits on the surface of naive B cells rather than guarding mucosa."],
        ["Immunoglobulin E", "Immunoglobulin E binds mast cells and basophils and mediates allergic responses."]],
  c=1, cite=L6 + ", Slides 50-60"),

dict(topic="Specific Immunity", io="3 — Antigens, antibodies and leukocytes",
  q="When are lymphocyte receptor specificities generated?",
  opts=[["After the antigen arrives, in response to it", "This is the discarded instructional model; receptors are made in advance."],
        ["Before any antigen has entered", "Correct. The repertoire is produced during lymphocyte development by gene rearrangement, so an arriving antigen selects a clone that already exists rather than instructing anything."],
        ["Only during an active infection", "The repertoire is laid down during development rather than generated afresh at each infection."],
        ["Continuously, in proportion to antigen exposure", "Diversity is generated independently of which antigens happen to be present."]],
  c=1, cite=L6 + ", Slides 30-38"),

dict(topic="Specific Immunity", io="3 — Antigens, antibodies and leukocytes",
  q="Class two major histocompatibility complex molecules present antigen to which cell?",
  opts=[["The helper T cell", "Correct. Class two is carried by antigen-presenting cells and displays engulfed material to the helper subset, which bears the matching cluster of differentiation 4 marker."],
        ["The cytotoxic T cell", "Cytotoxic T cells recognise antigen displayed on class one molecules instead."],
        ["The B cell", "B cells recognise antigen directly through their own surface receptor."],
        ["The natural killer cell", "Natural killer cells respond to the absence of class one rather than being presented to."]],
  c=0, cite=L6 + ", Slides 20-28"),

dict(topic="Specific Immunity", io="3 — Antigens, antibodies and leukocytes",
  q="What does opsonisation do?",
  opts=[["Coats the organism so phagocytes can engulf it", "Correct. The coating marks the target and gives the phagocyte a surface it can bind, which greatly increases the rate of engulfment."],
        ["Blocks the organism's attachment sites", "Blocking attachment sites is neutralisation; opsonisation coats the organism so phagocytes can grip it."],
        ["Clumps organisms together", "Clumping is agglutination, which immobilises antigen rather than marking it for uptake."],
        ["Punches holes in the organism's membrane", "Lysis requires the complement membrane attack complex; opsonisation merely coats the target for engulfment."]],
  c=0, cite=L6 + ", Slides 62-70"),

dict(topic="Specific Immunity", io="3 — Antigens, antibodies and leukocytes",
  q="How does a second exposure to the same antigen differ from the first?",
  opts=[["It is identical to the first", "The whole purpose of immunological memory is that the second response differs markedly."],
        ["It is slower and produces more immunoglobulin M", "Immunoglobulin M dominates the first response; the memory response is faster and rich in immunoglobulin G."],
        ["It is faster and produces far more immunoglobulin G", "Correct. Memory cells laid down by the first exposure are already present and pre-committed, so the response begins sooner, climbs higher and switches class."],
        ["It is weaker, because tolerance has developed", "Tolerance applies to self antigens; a repeated foreign antigen provokes a stronger response."]],
  c=2, cite=L6 + ", Slides 72-80"),

dict(topic="Specific Immunity", io="6.6 — Major histocompatibility complex",
  q="Which molecule must an antigen-presenting cell use to activate a helper T cell?",
  opts=[["Class one major histocompatibility complex", "Class one molecules mark self on nucleated cells and are what a cytotoxic T cell must engage, not the helper population."],
        ["Class two major histocompatibility complex", "Correct. These are the immune regulatory receptors carried by antigen-presenting cells, and they are required to bring bound antigen to a helper T cell."],
        ["Class three major histocompatibility complex", "Class three genes sit in the same cluster on chromosome six but do not act as the presenting receptor described here."],
        ["Surface immunoglobulin", "Surface immunoglobulin is the B cell's own antigen receptor and does not present antigen to a helper T cell."]],
  c=1, cite=L6 + ", Slide 16"),

dict(topic="Specific Immunity", io="6.7 — Cell mediated immunity",
  q="Which T lymphocyte destroys virally infected cells by secreting enzymes that lyse them?",
  opts=[["The cytotoxic T cell", "Correct. It lyses its targets directly and especially seeks out virally infected cells, cancer cells and cells from another individual."],
        ["The helper T cell", "The helper cell directs the response by releasing cytokines that activate other cells rather than killing targets itself."],
        ["The suppressor T cell", "The suppressor cell limits the activity of other T and B cells, restraining the response rather than destroying infected cells."],
        ["The delayed hypersensitivity cell", "This population produces reactions hours or days after contact and is not the one that lyses infected cells."]],
  c=0, cite=L6 + ", Slide 56"),

dict(topic="Specific Immunity", io="6.4 — Antibody production over time",
  q="Which antibody reaches a far higher level on a second exposure to the same antigen?",
  opts=[["Immunoglobulin M", "This class leads the primary response and rises only gradually in the secondary one, behind the dominant class."],
        ["Immunoglobulin A", "This class guards mucous surfaces and secretions and is not the one memory cells raise sharply on re-exposure."],
        ["Immunoglobulin E", "This class is bound to mast cells and is not the antibody whose level climbs steeply on a repeat encounter."],
        ["Immunoglobulin G", "Correct. Memory cells drive the secondary response and produce a much higher titre of this class, with immunoglobulin M rising slowly behind it."]],
  c=3, cite=L6 + ", Slide 53"),

dict(topic="Specific Immunity", io="6.9 — Vaccine composition",
  q="A vaccine made from a purified, inactivated bacterial toxin is described as which of the following?",
  opts=[["A toxoid", "Correct. A toxoid is built from purified antigenic components of a toxin, keeping the antigenicity while the toxic activity is destroyed."],
        ["A subunit preparation", "A subunit preparation uses antigenic molecules taken from the organism itself rather than from a treated toxin."],
        ["A live attenuated preparation", "A live attenuated preparation holds weakened whole organisms that still replicate, not an inactivated toxin."],
        ["A killed whole-cell preparation", "A killed whole-cell preparation holds the entire inactivated organism rather than a purified toxin product."]],
  c=0, cite=L6 + ", Slide 62"),

dict(topic="Specific Immunity", io="6.9 — Passive immunisation",
  q="Why does protection from donated antibodies last only a few months?",
  opts=[["The antibodies are destroyed by complement", "Antibody recruits complement rather than being cleared by it, and that is not why the protection fades."],
        ["No memory cells are produced", "Correct. The recipient is given finished antibody without ever mounting a response, so nothing remains to reproduce the protection once it decays."],
        ["The dose is too small to protect", "The dose protects immediately and well; the limit is that the protection is borrowed rather than generated by the recipient."],
        ["The recipient makes antibodies against them", "A reaction to donated serum can occur, but the protection is brief because no memory is laid down."]],
  c=1, cite=L6 + ", Slide 57"),

]
