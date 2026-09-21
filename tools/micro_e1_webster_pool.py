"""Microbiology Exam 1 — all six lectures, written the way Webster asks.

WHY THIS POOL IS DIFFERENT from mb_l1/mb_l2/micro_l3-l6. Those cover the
syllabus objectives evenly. This one is shaped by her own Exam 1 review
(11 September 2026, the last seventeen minutes of the Nonspecific Immunity
lecture) in two separate ways:

  WEIGHTING. She walked her objectives for the three lectures she taught
  (1, 2 and 5) and graded them. Her "know cold" items get the most questions
  here; her two explicit skips get one apiece. She did NOT review Lectures 3,
  4 and 6, and said so, so those are weighted evenly rather than lightly --
  silence is not a de-emphasis.

  QUESTION SHAPE. Four habits recur in how she asks, and every question here
  uses one of them:
    1. Several demands in one breath -- "What causes fever? Why is fever
       good? Why is fever bad?" -- so the key has to carry all the parts.
    2. Reason FORWARD from structure to consequence. On Gram staining she
       refused to let the class recite the wall and made them go on to what
       would and would not kill the organism.
    3. Mechanism, not the list. For inflammation she asked for the four signs
       AND "how is it that we have the redness, the heat, the pain?"
    4. She answers her own question when she expects it to be got wrong --
       the interferon correction is the clearest case.

  Two calculations are confirmed examinable: the therapeutic index and the
  decimal reduction time. "Yes, calculation, but the math won't be hard."

Stems are self-contained: the review sets the weighting, the DECKS supply
every fact, and nothing here cites a lecture or a lecturer.
"""

L1 = "Lecture 1  Dr. Webster -  Review of General Microbiology .pptx"
L2 = "Lecture Number 2  - Antibiotics and Resistance - Dr. Webster.pptx"
L3 = "PAJ5200.Microbe-human-interactions(1).pptx"
L4 = "PAJ5200.Transmission_of_microbes-2.pptx"
L5 = "Lecture 5  Dr. Webster Nonspecific Immunity.pptx"
L6 = "PAJ5200.Specific_Immunity-2.pptx"

POOL = [

# ─────────── Lecture 1 — Review of General Microbiology (12) ───────────

dict(topic="General Microbiology", io="1.4 — Gram-positive versus Gram-negative",
  q="A Gram-positive organism is isolated from a wound. Reasoning forward from what its wall is built like, what is it vulnerable to and what will it shrug off?",
  opts=[
    ["Vulnerable to detergents alone; protected by lipopolysaccharide",
     "Lipopolysaccharide sits in the Gram-negative outer membrane and is absent here, so it cannot be doing any protecting."],
    ["Vulnerable to polymyxin; protected by its thick peptidoglycan from lysozyme",
     "This reverses it. Polymyxin disrupts the outer membrane, which Gram-positive organisms lack, and the thick peptidoglycan is exactly what lysozyme digests."],
    ["Vulnerable to nothing that acts on the wall; protected by its periplasmic space",
     "The periplasmic space belongs to the Gram-negative envelope, and the exposed peptidoglycan makes wall-active agents more effective rather than less."],
    ["Vulnerable to lysozyme and penicillin; it has no outer membrane",
     "Correct. One thick exposed peptidoglycan layer is both the enzyme's substrate and the drug's target, and with no outer membrane there is no permeability barrier to overcome."]],
  c=3, cite=L1 + ", Slides 24-29"),

dict(topic="General Microbiology", io="1.4 — Gram-positive versus Gram-negative",
  q="Which wall feature explains why Gram-negative organisms resist many agents that kill Gram-positive ones, and what does that same feature release when the cell dies?",
  opts=[
    ["A waxy mycolic acid layer, which releases cord factor",
     "Mycolic acid is the acid-fast wall of mycobacteria, a separate group from the Gram-negative envelope."],
    ["A thick peptidoglycan layer, which releases teichoic acid",
     "Thick peptidoglycan with teichoic acid is the Gram-positive wall, and it confers no permeability barrier."],
    ["An outer membrane, which releases lipid A as endotoxin",
     "Correct. The outer membrane excludes large and hydrophobic molecules, and its lipopolysaccharide carries lipid A, the toxic portion freed when the cell lyses."],
    ["A capsule, which releases exotoxin",
     "A capsule resists phagocytosis rather than excluding drugs, and exotoxins are secreted by living cells rather than released on lysis."]],
  c=2, cite=L1 + ", Slides 26-29"),

dict(topic="General Microbiology", io="1.2 — Types of infectious pathogens",
  q="Mycoplasmas are singled out among bacteria. What makes them unusual, and what two consequences follow directly from it?",
  opts=[
    ["They lack a cell wall, so they cannot be Gram stained and penicillins do not work",
     "Correct. With no peptidoglycan there is nothing to retain crystal violet and nothing for a cell-wall-active drug to attack, so both the stain and the penicillins are useless."],
    ["They lack ribosomes, so they cannot make protein and need a host cell",
     "No bacterium lacks ribosomes; obligate intracellular dependence describes the chlamydias and rickettsias rather than mycoplasmas."],
    ["They lack deoxyribonucleic acid, so they need a host cell",
     "Every cellular organism carries deoxyribonucleic acid, and mycoplasmas can be grown on enriched artificial media rather than requiring a host cell."],
    ["They have two cell walls, so they stain unpredictably and resist lysozyme",
     "No bacterium has two walls; the feature that matters here is the complete absence of one."]],
  c=0, cite=L1 + ", Slides 14-18"),

dict(topic="General Microbiology", io="1.3 — Bacterial structures that enhance pathogenicity",
  q="Which structure lets a bacterium survive heat, drying and disinfectants for years, and which lets it resist being engulfed by a phagocyte?",
  opts=[
    ["The plasmid for survival; the fimbria for resisting phagocytosis",
     "A plasmid is extrachromosomal deoxyribonucleic acid rather than a protective structure, and fimbriae mediate adhesion rather than block phagocytosis."],
    ["The capsule for survival; the endospore for resisting phagocytosis",
     "This swaps them. The capsule is a surface layer that does not survive autoclaving, and the endospore is a dormancy structure rather than an antiphagocytic one."],
    ["The flagellum for survival; the pilus for resisting phagocytosis",
     "The flagellum provides motility and the pilus mediates attachment and conjugation; neither confers resistance to heat or to engulfment."],
    ["The endospore for survival; the capsule for resisting phagocytosis",
     "Correct. The endospore is a dormant dehydrated form that withstands extremes, while the capsule's slippery polysaccharide prevents a phagocyte gripping the cell."]],
  c=3, cite=L1 + ", Slides 30-36"),

dict(topic="General Microbiology", io="1.5 — Identification methods and culture media",
  q="Blood agar is both enriched and differential. What does each of those words buy you, and what are the three results you read off it?",
  opts=[
    ["Enriched suppresses unwanted growth, differential supplies nutrients; acid, gas and no change",
     "Suppressing unwanted growth is what a selective medium does, and acid and gas production is read on a fermentation medium rather than on blood agar."],
    ["Enriched supplies extra nutrients, differential shows visible differences; gamma, alpha and beta haemolysis",
     "Correct. The added blood feeds fastidious organisms and simultaneously acts as the indicator, since each organism digests haemoglobin to a different degree: none, partial, or complete."],
    ["Enriched selects one species, differential identifies it; coagulase, catalase and oxidase results",
     "No single medium selects one species, and those three are separate biochemical tests rather than readings from a plate."],
    ["Enriched raises the incubation temperature, differential lowers the pH; growth, no growth and partial growth",
     "Neither word refers to an incubation condition, and a simple growth or no-growth reading would make the medium selective rather than differential."]],
  c=1, cite=L1 + ", Slides 43-44"),

dict(topic="General Microbiology", io="1.5 — Identification methods and culture media",
  q="Mannitol salt agar is selective and differential at once. What is each property doing?",
  opts=[
    ["Both properties select, one for salt tolerance and one for sugar tolerance",
     "A medium that only selected would show growth or no growth; the colour change from mannitol fermentation is what makes it differential as well."],
    ["The mannitol selects fermenters; the salt differentiates by colony colour",
     "This reverses the two: salt does the selecting by excluding organisms that cannot tolerate it, and mannitol does the differentiating through the pH change."],
    ["The salt lyses red blood cells; the mannitol supplies iron",
     "Blood agar is where haemolysis is read, and mannitol is a sugar rather than an iron source."],
    ["The salt selects salt-tolerant organisms; mannitol then differentiates",
     "Correct. Only halotolerant organisms such as staphylococci grow at that salt concentration, and among those the pH indicator then separates the mannitol fermenters."]],
  c=3, cite=L1 + ", Slides 43-44"),

dict(topic="General Microbiology", io="1.6 — The bacterial growth curve",
  q="Bacterial growth means an increase in what, by what process, and why does that make the rise exponential rather than steady?",
  opts=[
    ["Increase in colony diameter, by migration, because motile cells spread outward",
     "Colony spread reflects motility on a plate rather than the growth of the population itself."],
    ["Increase in cell SIZE, by binary fission, because each cell grows at a constant rate",
     "Growth here means number rather than size, and constant enlargement would give arithmetic rather than exponential increase."],
    ["Increase in cell number, by budding, because daughter cells stay attached",
     "Budding is a yeast mechanism, and bacterial numbers rise by binary fission whether or not the daughters separate."],
    ["Increase in cell NUMBER, by binary fission, because each division doubles the population",
     "Correct. The cells do not enlarge; each one splits into two, so the population goes 2, 4, 8, 16 rather than climbing by a fixed amount each generation."]],
  c=3, cite=L1 + ", Slides 37-40"),

dict(topic="General Microbiology", io="1.6 — The bacterial growth curve",
  q="During which phase of the growth curve are bacteria most vulnerable to control methods, and why does that phase make them so?",
  opts=[
    ["Lag phase, because the cells have not yet adapted to the medium",
     "In lag phase the cells are synthesising enzymes but not dividing, so the targets that most antimicrobials attack are not yet active."],
    ["Log phase, because rapidly dividing cells are actively building wall and nucleic acid",
     "Correct. Agents that block cell wall synthesis or replication can only act where those processes are running, so the fastest-dividing population is the most exposed."],
    ["Stationary phase, because nutrients have run out and the cells are weakened",
     "Nutrient exhaustion slows division, which makes these cells harder rather than easier to kill with agents that need active growth."],
    ["Death phase, because the population is already declining",
     "A declining population reflects cells that have already died; the survivors are typically the most resistant rather than the most vulnerable."]],
  c=1, cite=L1 + ", Slides 37-40"),

dict(topic="General Microbiology", io="1.7 — Lytic versus lysogenic replication",
  q="In lysogeny the viral genome is incorporated into the host chromosome. What does the bacterium gain from that, and why does it matter clinically?",
  opts=[
    ["Loss of its plasmids, which removes resistance genes",
     "Lysogeny adds genetic material rather than removing it, and plasmid loss is unrelated to prophage integration."],
    ["Immediate lysis of neighbouring cells, which clears competing flora",
     "Lysis of the host is the lytic outcome; lysogeny is defined by the genome integrating and staying quiet."],
    ["New traits such as the ability to make a toxin, carried without any sign of infection",
     "Correct. The integrated prophage is replicated along with the chromosome, so a harmless-looking organism can acquire and pass on a toxin gene, which is how diphtheria and cholera toxins arise."],
    ["Permanent resistance to all further viral infection, with no other change",
     "Superinfection immunity to related phage does occur, but the consequence that matters is the new traits the prophage brings."]],
  c=2, cite=L1 + ", Slides 52-56"),

dict(topic="General Microbiology", io="1.8 — Animal virus versus phage replication",
  q="Animal virus replication differs from phage replication at entry, at the step that follows entry, and at release. What are those three differences?",
  opts=[
    ["The whole virion enters, it integrates immediately, and release is by lysis",
     "Integration is characteristic of lysogeny and of some animal viruses, but it is not the step that follows entry, and budding rather than bursting is the contrast being drawn."],
    ["Only the genome enters, uncoating follows, and release is by lysis",
     "Injecting the genome alone and lysing the host describes the phage, and a genome entering alone would need no uncoating."],
    ["The whole virion enters, must be uncoated, and leaves by budding",
     "Correct. A phage injects only its genome, so no uncoating is needed and the cell is lysed; an animal virus is engulfed entire, must shed its capsid, and can leave through the membrane acquiring an envelope."],
    ["Only the capsid enters, the genome stays outside, and release is by budding",
     "The genome must reach the cell interior to be replicated; a capsid alone would carry no genetic information."]],
  c=2, cite=L1 + ", Slide 58"),

dict(topic="General Microbiology", io="1.11 — Microbial control and the death curve",
  q="A disinfectant reduces a population of 10,000,000 organisms to 10,000. How many decimal reductions is that, and what does the shape of a microbial death curve tell you?",
  opts=[
    ["Three, and death proceeds at a constant proportion rather than a constant number",
     "Correct. Each decimal reduction removes ninety per cent of whatever remains, so 10,000,000 to 10,000 is three tenfold steps, and the logarithmic curve reflects a fixed fraction dying per interval."],
    ["Three, and death proceeds at a constant number of organisms per interval",
     "The count of reductions is right, but a constant number killed per interval would give a straight arithmetic decline rather than the logarithmic curve observed."],
    ["Four, and death proceeds at a constant proportion of the survivors",
     "The mechanism is right but the arithmetic is not: 10,000,000 to 10,000 is a thousandfold fall, which is three decimal reductions rather than four."],
    ["One thousand, and the death rate accelerates as the population falls",
     "A thousand is the fold-reduction rather than the number of decimal steps, and the proportion dying per interval stays constant."]],
  c=0, cite=L1 + ", Slides 62-68"),

dict(topic="General Microbiology", io="1.10 — Health implications of nucleic acid mutations",
  q="A high mutation rate in a virus carries which practical consequence for the people it infects?",
  opts=[
    ["Antibiotic therapy becomes effective against it",
     "Antibiotics act on bacterial structures that viruses do not possess, whatever the mutation rate."],
    ["The virus loses the ability to replicate inside host cells",
     "Mutation alters the virus rather than disabling it; a variant that could not replicate would simply disappear."],
    ["Changed surface proteins can defeat existing immunity",
     "Correct. Immunity recognises specific surface structures, so a virus that alters them is no longer matched by existing antibody, which is why some vaccines must be reformulated."],
    ["Transmission between people stops, though animal spread continues",
     "A high mutation rate is what allows some animal viruses to cross into humans rather than stopping human spread."]],
  c=2, cite=L1 + ", Slide 60"),

# ─────────── Lecture 2 — Antibiotics and Resistance (11) ───────────

dict(topic="Antibiotics and Resistance", io="2.3 — Therapeutic index",
  q="A drug has a toxic dose for half the population of 400 milligrams and an effective dose for half the population of 50 milligrams. What is its therapeutic index, and what does a larger value mean?",
  opts=[
    ["Three hundred and fifty, and a larger value means a safer drug",
     "Subtracting the doses rather than dividing them gives a figure that changes with the units used and cannot be compared between drugs."],
    ["Eight, and a larger value means a more potent drug",
     "The arithmetic is right but potency is about how small the effective dose is; the index measures the safety margin between working and toxic doses."],
    ["One-eighth, and a smaller value means a safer drug",
     "This inverts the ratio. Putting the effective dose on top yields a number below one for every usable drug and reverses the direction of safety."],
    ["Eight, and a larger value means a safer drug",
     "Correct. The index is the toxic dose divided by the effective dose, so 400 over 50 is 8, and the wider that gap the more room there is between a dose that works and one that harms."]],
  c=3, cite=L2 + ", Slides 18-20"),

dict(topic="Antibiotics and Resistance", io="2.7 — Mechanisms of drug resistance",
  q="An antibiotic course is followed by an infection that no longer responds to it. What has happened to the bacterial population?",
  opts=[
    ["The antibiotic caused the bacteria to develop resistance genes in response to it",
     "Exposure selects among existing variation rather than creating it; the mutations or acquired genes were present before the drug arrived."],
    ["Resistant organisms already present were selected for as the susceptible ones died",
     "Correct. The drug does not induce the trait; it removes the competition, so the few organisms that already carried resistance are left to multiply unopposed."],
    ["The bacteria learned to recognise the antibiotic and altered their behaviour",
     "Bacteria have no such adaptive capacity within a generation; what changes is which organisms survive to reproduce."],
    ["The host immune system destroyed the susceptible organisms and spared the rest",
     "The immune system does not discriminate by antibiotic susceptibility; it is the drug that removes the susceptible population."]],
  c=1, cite=L2 + ", Slides 45-52"),

dict(topic="Antibiotics and Resistance", io="2.7 — Mechanisms of drug resistance",
  q="Which resistance mechanism destroys the antibiotic molecule itself, and which keeps the drug out or pushes it back out?",
  opts=[
    ["Efflux pumps destroy it; enzymatic inactivation excludes it",
     "This swaps the two: a pump moves an intact molecule out, while an enzyme chemically breaks the drug apart."],
    ["Enzymatic inactivation destroys it; permeability and efflux exclude it",
     "Correct. Beta-lactamase cleaves the drug so it can no longer bind, whereas permeability changes and pumps never let a useful concentration accumulate inside the cell."],
    ["Target modification destroys it; enzymatic inactivation excludes it",
     "Target modification leaves the drug intact and changes the binding site instead, and enzymes act on the drug rather than on entry."],
    ["Biofilm formation destroys it; capsule production excludes it",
     "A biofilm impedes penetration rather than degrading the molecule, and the capsule resists phagocytosis rather than antibiotic entry."]],
  c=1, cite=L2 + ", Slides 45-52"),

dict(topic="Antibiotics and Resistance", io="2.6 — Mechanisms of action",
  q="Selective toxicity means finding a feature the invader has and we do not. Which target is genuinely absent from human cells, and which is present in both but different enough to exploit?",
  opts=[
    ["Deoxyribonucleic acid is absent from us; the mitochondrion is present in both",
     "Human cells contain deoxyribonucleic acid, and bacteria have no mitochondria."],
    ["The ribosome is absent from us; the cell wall is present in both but differs in composition",
     "Human cells certainly have ribosomes, and they have no cell wall at all, so this reverses both halves."],
    ["The plasma membrane is absent from us; the nucleus is present in both",
     "Every human cell has a plasma membrane, which is why membrane-active agents such as the polymyxins are comparatively toxic."],
    ["The peptidoglycan cell wall is absent from us; the ribosome is present in both but differs in size",
     "Correct. Nothing in a human cell corresponds to peptidoglycan, so wall-active drugs are very safe, whereas the 70S bacterial ribosome differs enough from our 80S one to be targeted with more care."]],
  c=3, cite=L2 + ", Slides 24-32"),

dict(topic="Antibiotics and Resistance", io="2.6 — Mechanisms of action",
  q="Which pairing correctly matches an antibiotic class to the step it blocks?",
  opts=[
    ["Sulfonamides block cell wall crosslinking; vancomycin blocks folate synthesis",
     "Sulfonamides mimic para-aminobenzoic acid to block folate synthesis, and vancomycin binds wall subunits directly."],
    ["Penicillins block protein synthesis; aminoglycosides block cell wall crosslinking",
     "The two are swapped: the beta-lactam ring acts at the wall and the aminoglycosides act at the ribosome."],
    ["Penicillins block cell wall crosslinking; aminoglycosides block protein synthesis",
     "Correct. The beta-lactam ring inactivates the transpeptidase that crosslinks peptidoglycan, while the aminoglycosides bind the bacterial ribosome and halt translation."],
    ["Fluoroquinolones block membrane integrity; polymyxins block nucleic acid replication",
     "These are reversed: the fluoroquinolones inhibit the enzymes that manage bacterial deoxyribonucleic acid, and the polymyxins disrupt membranes."]],
  c=2, cite=L2 + ", Slides 24-32"),

dict(topic="Antibiotics and Resistance", io="2.2 — Prokaryotic versus eukaryotic targets",
  q="Why are there fewer drugs available against fungal and protozoal infections than against bacterial ones?",
  opts=[
    ["Those infections resolve without treatment, so few drugs were developed",
     "Many are severe and even fatal untreated; the limitation is pharmacological rather than a lack of need."],
    ["Those pathogens reproduce too slowly for any drug to act on them",
     "Slow growth complicates treatment duration but is not why the pharmacopeia is thin; the shortage of safe targets is."],
    ["Those pathogens are prokaryotes with unusually tough cell walls",
     "Fungi and protozoa are eukaryotes, and it is precisely that which makes them difficult to treat."],
    ["Those pathogens are eukaryotes, so they share far more structure with our own cells",
     "Correct. Selective toxicity depends on a difference to exploit, and a eukaryotic pathogen's cell structure and physiology closely resemble ours, so the margin for harming it without harming us is much narrower."]],
  c=3, cite=L2 + ", Slides 12-16"),

dict(topic="Antibiotics and Resistance", io="2.4 — Drug clearance and the dosage schedule",
  q="What does drug clearance impose on the dosing schedule, and what happens if doses are spaced too far apart?",
  opts=[
    ["The level must stay above the minimal inhibitory concentration",
     "Correct. Clearance removes the drug continuously, so once the level falls below the inhibitory concentration the suppressed population resumes multiplying before the next dose arrives."],
    ["Only the loading dose matters, since clearance does not affect the interval",
     "Clearance determines how fast the level falls, which is precisely what sets the interval between doses."],
    ["Doses should be spaced as widely as the patient will tolerate to limit toxicity",
     "Widening the interval lets the concentration drop below the inhibitory level for too much of the cycle, allowing regrowth."],
    ["The drug reaches its target instantly, so only the total daily amount matters",
     "It takes time for a drug to enter the system and distribute, which is part of why both the amount and its timing matter."]],
  c=0, cite=L2 + ", Slides 21-23"),

dict(topic="Antibiotics and Resistance", io="2.6 — Bacteriostatic versus bactericidal",
  q="What separates a bacteriostatic from a bactericidal drug, and in which patient does that distinction become critical?",
  opts=[
    ["Static works on Gram-positive organisms and cidal on Gram-negative, which matters in sepsis",
     "Spectrum and killing are independent properties; both categories contain broad and narrow agents."],
    ["Static kills slowly and cidal kills quickly, which matters in the elderly patient",
     "The difference is whether the drug kills at all rather than how fast, and age is not what makes the distinction critical."],
    ["Static inhibits and needs host immunity; cidal kills, which matters if neutropenic",
     "Correct. A bacteriostatic agent only halts replication and leaves clearance to the immune system, so a patient without functioning neutrophils needs a drug that kills outright."],
    ["Static is oral and cidal is intravenous, which matters in the vomiting patient",
     "Route is unrelated: penicillins are bactericidal and available orally, tetracyclines bacteriostatic and available intravenously."]],
  c=2, cite=L2 + ", Slides 33-36"),

dict(topic="Antibiotics and Resistance", io="2.8 — Other problems with antimicrobial therapy",
  q="Which four problems accompany antimicrobial therapy, and what unites them?",
  opts=[
    ["Superinfection, direct toxicity, hypersensitivity and resistance — each a harm caused by treating",
     "Correct. Each is a different route by which treatment injures: killing protective flora, poisoning the host, provoking an immune reaction, or selecting organisms the drug can no longer touch."],
    ["Cost, availability, storage and palatability — each a barrier to obtaining treatment",
     "These are practical obstacles to access rather than harms arising from the therapy itself."],
    ["Superinfection, cost, resistance and slow onset — each a reason treatment fails",
     "Cost and onset speed are not among the four, and the grouping is about harm rather than failure."],
    ["Allergy, nausea, headache and rash — each a minor adverse effect",
     "These are individual symptoms rather than the four categories, and the grouping includes harms far beyond minor effects."]],
  c=0, cite=L2 + ", Slides 55-62"),

dict(topic="Antibiotics and Resistance", io="2.8 — Other problems with antimicrobial therapy",
  q="A patient develops profuse diarrhoea after a broad-spectrum antibiotic course. What has happened, and why did the antibiotic cause it?",
  opts=[
    ["Hypersensitivity, because the immune system reacted to the drug",
     "A hypersensitivity reaction produces rash, bronchospasm or anaphylaxis rather than an overgrowth of a resistant organism."],
    ["Direct toxicity, because the drug damaged the intestinal lining",
     "Some agents do irritate the gut, but an overgrowth following flora destruction is superinfection rather than a direct toxic effect."],
    ["Superinfection, because the drug removed the flora holding it in check",
     "Correct. Resident flora occupy the niche and compete for nutrients, so wiping them out leaves room for a resistant organism such as Clostridioides difficile to overgrow."],
    ["Resistance, because the organism causing the original infection stopped responding",
     "Resistance would mean the original infection persisting, not a new organism flourishing in the space left behind."]],
  c=2, cite=L2 + ", Slides 55-58"),

dict(topic="Antibiotics and Resistance", io="2.1 — Major historical events and names",
  q="Which pairing of name to contribution is correct?",
  opts=[
    ["Florey observed penicillin; Fleming and Chain made it usable as a drug",
     "The observation was Fleming's; Florey worked on turning it into a usable therapy."],
    ["Fleming observed penicillin; Florey and Chain made it usable as a drug",
     "Correct. Fleming noticed the inhibition around a contaminating mould, and it was Florey and Chain who purified the compound and demonstrated it could treat infection in patients."],
    ["Ehrlich observed penicillin; Fleming made it usable as a drug",
     "Ehrlich's contribution was the magic bullet concept and early chemotherapy, well before penicillin was observed."],
    ["Chain observed penicillin; Ehrlich and Florey made it usable as a drug",
     "Chain shared in the development work rather than the original observation, which was Fleming's."]],
  c=1, cite=L2 + ", Slides 5-10"),

# ─────────── Lecture 3 — Microbe-Human Interactions (8) ───────────
# NOT reviewed in class. She said so explicitly, so this is weighted evenly
# with the rest rather than treated as low yield.

dict(topic="Microbe-Human Interactions", io="1 — Define resident flora",
  q="Resident flora protect us. By what mechanism, and which two sites carry essentially none?",
  opts=[
    ["They raise body temperature to inhibit invaders; the lungs and liver are sterile",
     "Fever is a host response driven by cytokines rather than by flora, and protection comes from occupying the niche."],
    ["They secrete antibodies against pathogens; the large intestine and skin are sterile",
     "Antibody is produced by plasma cells rather than by bacteria, and the large intestine and skin are two of the most heavily colonised sites in the body."],
    ["They digest all ingested pathogens; the stomach and mouth are sterile",
     "Flora compete rather than digesting pathogens wholesale, and both the stomach and mouth carry their own populations."],
    ["They occupy the niche and prevent overgrowth; blood and spinal fluid are sterile",
     "Correct. Competition for space and nutrients is what keeps pathogens from establishing, and the internal compartments that no organism should reach are the blood and the cerebrospinal fluid."]],
  c=3, cite=L3 + ", Slides 8-16"),

dict(topic="Microbe-Human Interactions", io="1 — Define resident flora",
  q="What separates a true pathogen from an opportunist, and what two circumstances let an opportunist cause disease?",
  opts=[
    ["A true pathogen is always Gram-negative; an opportunist needs a breach in the skin or a foreign body",
     "Gram reaction has nothing to do with the distinction, and the defining feature is whether intact defences can be overcome."],
    ["A true pathogen sickens healthy people; an opportunist needs compromised defences or an unnatural site",
     "Correct. The true pathogen carries enough virulence to overcome intact defences, whereas an opportunist is usually harmless flora that causes disease only when immunity fails or it reaches somewhere it does not belong."],
    ["A true pathogen is acquired in hospital; an opportunist is acquired in the community",
     "This describes where infection is acquired rather than the organism's capacity to cause disease in a healthy host."],
    ["A true pathogen produces exotoxin; an opportunist needs antibiotic exposure or advanced age",
     "Toxin production is one virulence factor among many, and it is not what separates the two categories."]],
  c=1, cite=L3 + ", Slides 18-24"),

dict(topic="Microbe-Human Interactions", io="3 — Endotoxins versus exotoxins",
  q="How do endotoxin and exotoxin differ in origin, in when they are released, and in which organisms produce them?",
  opts=[
    ["Endotoxin is a protein secreted by living Gram-positive cells; exotoxin is released on lysis",
     "This reverses both halves: the secreted protein is the exotoxin, and endotoxin comes from the Gram-negative wall on lysis."],
    ["Endotoxin is lipid A released on lysis by Gram-negative organisms; exotoxin is secreted by living cells",
     "Correct. Endotoxin is a structural part of the Gram-negative outer membrane and only reaches the host when the cell breaks apart, whereas an exotoxin is a protein actively exported by a living bacterium."],
    ["Endotoxin is released by fungi; exotoxin by bacteria, both while growing",
     "Endotoxin is specifically the lipopolysaccharide of Gram-negative bacteria rather than a fungal product."],
    ["Both are proteins, differing only in whether they act locally or systemically",
     "Endotoxin is a lipid component of the wall rather than a protein, which is why it cannot be converted into a toxoid."]],
  c=1, cite=L3 + ", Slides 40-46"),

dict(topic="Microbe-Human Interactions", io="2 — Steps in the progression of infectious disease",
  q="Which virulence factor lets a bacterium attach to host tissue, and which lets it survive once a phagocyte has engulfed it?",
  opts=[
    ["Endotoxin for attachment; exotoxin for survival inside the phagocyte",
     "Toxins damage host tissue rather than anchoring the organism or protecting it within a phagocyte."],
    ["Capsule for attachment; fimbriae for survival inside the phagocyte",
     "The capsule resists engulfment rather than mediating attachment, and fimbriae have no role once the organism is inside a cell."],
    ["Fimbriae for attachment; resisting digestion inside the phagocyte for survival",
     "Correct. Fimbriae are the adhesins that anchor the organism to a specific host receptor, and some organisms then avoid being killed by blocking fusion with the lysosome or withstanding its enzymes."],
    ["Flagella for attachment; spores for survival inside the phagocyte",
     "Flagella provide motility toward a site, and sporulation is a response to environmental hardship rather than to phagocytosis."]],
  c=2, cite=L3 + ", Slides 30-38"),

dict(topic="Microbe-Human Interactions", io="4 — Stages in the course of an infection",
  q="A sign and a symptom are not the same thing. What separates them, and what is a sequela?",
  opts=[
    ["A sign is observed by the clinician and a symptom felt by the patient; a sequela is lasting damage afterwards",
     "Correct. The distinction is who perceives it, and a sequela is the long-term or permanent tissue or organ damage that remains once the acute illness has passed, such as blindness following gonococcal conjunctivitis."],
    ["A sign is felt by the patient and a symptom observed by the clinician; a sequela is a relapse",
     "The two are swapped, and a sequela is residual damage rather than a return of the original illness."],
    ["A sign appears early and a symptom late; a sequela is a secondary infection",
     "Timing does not define either term, and a secondary infection is a new infection rather than residual damage."],
    ["A sign is measurable and a symptom is not; a sequela is the incubation period",
     "Measurability overlaps but is not the definition, and the incubation period precedes illness rather than following it."]],
  c=0, cite=L3 + ", Slides 50-58"),

dict(topic="Microbe-Human Interactions", io="4 — Stages in the course of an infection",
  q="An infection confined to one area spreads through the bloodstream to distant organs. What is that called, and what is it called when a second organism takes hold after antibiotics disturb the flora?",
  opts=[
    ["Chronic infection; the second is a sequela",
     "Chronicity refers to duration rather than spread, and a sequela is residual damage rather than a new organism."],
    ["Superinfection; the second is a mixed infection",
     "Superinfection describes the flora-disruption case rather than dissemination, and a mixed infection means several organisms present from the start."],
    ["Secondary infection; the second is a latent infection",
     "A secondary infection follows a primary one but does not specifically describe bloodstream spread, and latency means a dormant organism rather than an overgrowth."],
    ["Systemic spread; the second is a superinfection",
     "Correct. A localised infection becomes systemic when the agent breaks loose and disseminates, while a superinfection follows disruption of the natural microflora that had been suppressing the newcomer."]],
  c=3, cite=L3 + ", Slides 50-58"),

dict(topic="Microbe-Human Interactions", io="1 — Define resident flora",
  q="Which body site carries the largest resident population, and which is sterile apart from a short segment?",
  opts=[
    ["The mouth carries the most; the large intestine is sterile",
     "The mouth is heavily colonised but the colon carries more, and the colon is certainly not sterile."],
    ["The stomach carries the most; the respiratory tract is sterile throughout",
     "Gastric acid keeps stomach numbers low, and the upper respiratory tract is colonised even though the lower tract is not."],
    ["The skin carries the most; the gastrointestinal tract is sterile below the stomach",
     "The skin is densely colonised but not to the extent of the colon, and the lower bowel is the most heavily populated site of all."],
    ["The large intestine carries the most; the urinary tract is sterile but for the distal urethra",
     "Correct. The colon holds by far the densest microbial population in the body, while urine and the urinary tract above the distal urethra should contain no organisms at all."]],
  c=3, cite=L3 + ", Slides 8-16"),

dict(topic="Microbe-Human Interactions", io="2 — Steps in the progression of infectious disease",
  q="What does the infectious dose for half a population measure, and what does a LOW value indicate about the organism?",
  opts=[
    ["The dose killing half those infected; a low value means lower virulence",
     "That describes a lethal rather than an infectious dose, and needing fewer organisms indicates more virulence, not less."],
    ["The dose infecting half those exposed; a low value means greater virulence",
     "Correct. It is the number of organisms required to establish infection in fifty per cent of a population, so needing very few to do so marks an organism as highly virulent."],
    ["The proportion of exposed people who fall ill; a low value means high transmissibility",
     "It is a dose rather than a proportion, and a low dose indicates virulence rather than transmissibility directly."],
    ["The time to symptom onset in half those infected; a low value means a short incubation",
     "That would be an incubation measure; this quantity counts organisms rather than time."]],
  c=1, cite=L3 + ", Slides 26-30"),

# ─────────── Lecture 4 — Transmission of Microorganisms (7) ───────────

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="The chain of infection has how many links, and which link do standard precautions such as hand hygiene attack?",
  opts=[
    ["Four links, and hand hygiene removes the reservoir",
     "The chain has six links, and washing hands interrupts spread rather than eliminating where the organism lives."],
    ["Six links, and hand hygiene breaks the mode of transmission",
     "Correct. The chain runs agent, reservoir, portal of exit, mode of transmission, portal of entry and susceptible host, and hand hygiene is aimed squarely at the transmission link because it is the one most readily interrupted."],
    ["Six links, and hand hygiene protects the susceptible host",
     "The count is right but the target is not: protecting the host describes vaccination or prophylaxis, while hand hygiene blocks transmission."],
    ["Eight links, and hand hygiene closes the portal of entry",
     "There are six links, and closing the portal of entry describes measures such as catheter care or wound dressing."]],
  c=1, cite=L4 + ", Slides 6-14"),

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="What separates a vector from a reservoir, and what separates an active carrier from a passive one?",
  opts=[
    ["A vector is always an insect and a reservoir always an animal; both carriers are infected",
     "Vectors and reservoirs are not restricted to those categories, and the passive carrier is by definition not infected."],
    ["The reservoir carries it and the vector harbours it; an active carrier shows symptoms, a passive one does not",
     "The first half is reversed, and the active carrier is defined by being infected rather than by showing symptoms."],
    ["The vector carries it and the reservoir harbours it; an active carrier is infected, a passive one is not",
     "Correct. A reservoir is where the organism normally lives and multiplies, a vector transports it to a host, and the passive carrier simply transfers organisms on the hands or clothing without being infected."],
    ["A vector is inanimate and a reservoir living; an active carrier is treated, a passive one is not",
     "An inanimate carrier is a fomite rather than a vector, and treatment status does not define either carrier type."]],
  c=2, cite=L4 + ", Slides 16-26"),

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="Why can a zoonotic infection not be eradicated the way smallpox was?",
  opts=[
    ["Zoonotic organisms are resistant to all available antimicrobials",
     "Many are treatable; the obstacle is that curing human cases leaves the reservoir untouched."],
    ["Zoonotic organisms mutate too quickly for any vaccine to remain effective",
     "Mutation rate complicates vaccine design for some agents, but the barrier to eradication is the animal reservoir."],
    ["Zoonotic infections are always viral, and viruses cannot be eradicated",
     "Zoonoses may be bacterial, viral, fungal or protozoan, and smallpox itself was a virus that was eradicated."],
    ["The animal reservoir persists even if every human case is cured",
     "Correct. Eradication requires removing every place the organism can live and multiply, and an infection maintained in animals continues regardless of what happens in the human population."]],
  c=3, cite=L4 + ", Slides 28-36"),

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="A fomite transmits infection. What is a fomite, and why do hospital keyboards and stethoscopes matter so much?",
  opts=[
    ["An airborne droplet nucleus; these stay suspended near equipment",
     "Droplet nuclei are airborne particles rather than objects, and fomite spread requires contact with a surface."],
    ["A living carrier that shows no symptoms; these move between patients unnoticed",
     "A symptomless living carrier is a carrier rather than a fomite, which is by definition non-living."],
    ["A contaminated non-living object; these are touched constantly and cleaned rarely",
     "Correct. A fomite is any inanimate object that carries organisms between people, and items handled many times a day but not included in routine cleaning become efficient relays."],
    ["A biofilm on a wet surface; these resist all disinfectants",
     "A biofilm may form on a fomite, but the fomite is the object itself, and biofilms are reduced rather than wholly resistant."]],
  c=2, cite=L4 + ", Slides 40-52"),

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="Which patients are most at risk from hospital-acquired infection, and which sites are most commonly involved?",
  opts=[
    ["The immunocompromised; urinary tract, lungs and surgical sites",
     "Correct. Impaired defences allow organisms of low virulence to establish, and the commonest sites are exactly those breached by catheters, ventilation and surgery."],
    ["The young and otherwise healthy; the skin and soft tissue",
     "Intact immunity is protective, and skin infection is less common than the device-related and surgical sites."],
    ["Patients on short admissions; the gastrointestinal tract alone",
     "Longer stays and more devices raise risk, and the gastrointestinal tract is one site among several rather than the only one."],
    ["Outpatients attending clinics; the bloodstream alone",
     "Hospital-acquired infection is defined by acquisition during admission, and bloodstream infection is one of several sites."]],
  c=0, cite=L4 + ", Slides 40-46"),

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="What determines whether a disinfectant actually works on a surface?",
  opts=[
    ["The brand of the product and the material of the cloth",
     "These are procurement details rather than determinants of kill; the active concentration and dwell time are what count."],
    ["Its smell and the temperature of the room",
     "Neither relates to antimicrobial activity; what matters is the concentration reaching the organisms and how long it acts."],
    ["Whether the surface looks clean before application",
     "A visibly clean surface may carry a biofilm, which is part of why appearance is misleading; concentration and contact time govern the result."],
    ["Its concentration and its contact time",
     "Correct. An agent applied too dilute or wiped off before its contact time has elapsed will not achieve the reduction it is rated for, however effective the chemical is in principle."]],
  c=3, cite=L4 + ", Slides 56-64"),

dict(topic="Transmission of Microorganisms", io="1 — Describe the chain of infection",
  q="Bacteria acquire resistance genes from each other by horizontal gene transfer. Which mechanism uses a virus as the carrier, and which picks up free genetic material from the surroundings?",
  opts=[
    ["Transformation uses a phage; transduction takes up free material",
     "The two names are swapped: the phage-mediated route is transduction."],
    ["Transduction uses a phage; transformation takes up free material",
     "Correct. In transduction a bacteriophage packages host genes and injects them into the next cell, whereas in transformation the recipient absorbs naked deoxyribonucleic acid released by a lysed neighbour."],
    ["Conjugation uses a phage; transduction requires direct cell contact",
     "Conjugation is the one requiring direct contact, through a pilus, and it does not involve a virus."],
    ["Transduction requires direct cell contact; conjugation takes up free material",
     "Direct contact defines conjugation, and free uptake defines transformation."]],
  c=1, cite=L4 + ", Slides 66-72"),

# ─────────── Lecture 5 — Nonspecific Host Defenses (14) ───────────
# Her heaviest lecture: nine of twelve objectives graded "know cold".

dict(topic="Nonspecific Host Defenses", io="3.1 — The three lines of defense",
  q="Of the three lines of defense, which is the specific one, and where does the real dividing line fall?",
  opts=[
    ["The third is specific; the line falls between the second and third",
     "Correct. The first two lines are both nonspecific, acting the same way against anything, and only the third is acquired through exposure to a particular antigen and carries memory of it."],
    ["The first is specific; the line falls between the first and second",
     "The first line is a set of barriers that block anything indiscriminately, which is the definition of nonspecific."],
    ["The second is specific; the line falls between the first and second",
     "The second line is protective cells and antimicrobial substances acting without regard to which organism is present, so it too is nonspecific."],
    ["All three are specific to differing degrees, so no single line divides them",
     "Only the third line recognises a particular antigen and remembers it; the other two do not discriminate at all."]],
  c=0, cite=L5 + ", Slide 4"),

dict(topic="Nonspecific Host Defenses", io="3.2 — First line barriers",
  q="Intact skin, lysozyme in tears and the resident flora each block invasion. Which category does each belong to?",
  opts=[
    ["Skin is physical, lysozyme chemical, resident flora microbiological",
     "Correct. The first line divides into physical barriers that obstruct, chemical substances that attack, and microbiological competition from the normal flora that occupies the niche first."],
    ["Skin is chemical, lysozyme physical, resident flora genetic",
     "The skin obstructs mechanically and lysozyme is an enzyme, so the first two labels are reversed and flora are microbiological rather than genetic."],
    ["All three are physical barriers differing only in location",
     "Lysozyme digests peptidoglycan chemically and flora compete biologically; neither works by physical obstruction."],
    ["Skin is microbiological, lysozyme genetic, resident flora chemical",
     "Each label is misassigned; the skin is a physical barrier, lysozyme a chemical one and the flora a microbiological one."]],
  c=0, cite=L5 + ", Slides 6-18"),

dict(topic="Nonspecific Host Defenses", io="3.2 — First line barriers",
  q="Lysozyme in tears attacks peptidoglycan. Reasoning forward, which organisms does it strip of their whole wall, and why does the tougher-looking one fare worse?",
  opts=[
    ["Gram-negative organisms, because their thin peptidoglycan is easier to digest",
     "Their peptidoglycan is thinner but lies beneath an outer membrane that lysozyme cannot cross, so it is protected rather than exposed."],
    ["Gram-positive organisms, whose thick peptidoglycan lies exposed",
     "Correct. The intuition that a thicker wall must be sturdier is backwards here: the peptidoglycan is the enzyme's substrate, and in the Gram-positive organism it is the outermost layer with nothing shielding it."],
    ["Both equally, because peptidoglycan is chemically identical in each",
     "The chemistry is similar but access is not; the outer membrane of the Gram-negative envelope keeps the enzyme away from its substrate."],
    ["Neither, because lysozyme acts only on fungal cell walls",
     "Fungal walls are built on chitin and glucan rather than peptidoglycan, which is what lysozyme cleaves."]],
  c=1, cite=L5 + ", Slides 13-18"),

dict(topic="Nonspecific Host Defenses", io="3.3 — Recognition: receptors and patterns",
  q="Host cells recognise trouble through pattern recognition receptors. What do those receptors bind, and what is the difference between the two kinds of signal?",
  opts=[
    ["Pathogen-associated and damage-associated molecular patterns",
     "Correct. Pathogen-associated patterns are conserved microbial structures we never make ourselves; damage-associated patterns are molecules released by our own injured cells, so one receptor system responds to both infection and tissue injury."],
    ["Specific antigens from microbes and antibodies from plasma cells",
     "Recognising a specific antigen is the job of the adaptive system; these receptors detect broad conserved patterns instead."],
    ["Complement fragments from serum and cytokines from leukocytes",
     "Those are downstream messengers of the response rather than the patterns that initiate recognition."],
    ["Only microbial patterns, since host molecules are always ignored",
     "Damage-associated patterns from our own injured cells are recognised too, which is how sterile injury provokes inflammation."]],
  c=0, cite=L5 + ", Slides 20-30"),

dict(topic="Nonspecific Host Defenses", io="3.4 — The leukocytes",
  q="Which leukocyte is the most numerous, and what is its job?",
  opts=[
    ["The monocyte, at roughly 55 to 90 per cent, and it releases histamine",
     "Monocytes make up only about 3 to 7 per cent, and histamine release belongs to basophils and mast cells."],
    ["The lymphocyte, at roughly 55 to 90 per cent, and it presents antigen to other cells",
     "Lymphocytes are second at about 20 to 35 per cent, and antigen presentation is chiefly a macrophage and dendritic cell function."],
    ["The neutrophil, at roughly 55 to 90 per cent, and it is the dedicated phagocytic killer",
     "Correct. Neutrophils dominate the differential count and arrive first at an infection, where they engulf and destroy organisms directly."],
    ["The eosinophil, at roughly 55 to 90 per cent, and it destroys bacteria",
     "Eosinophils are only 1 to 3 per cent and act chiefly against parasites, particularly helminths."]],
  c=2, cite=L5 + ", Slides 66-70"),

dict(topic="Nonspecific Host Defenses", io="3.4 — The leukocytes",
  q="Eosinophils and basophils are both rare. What does each of them actually do?",
  opts=[
    ["Eosinophils release histamine; basophils defend against helminths",
     "The two are swapped: mediator release is the basophil's role and antiparasitic defence the eosinophil's."],
    ["Eosinophils defend against parasites; basophils release mediators",
     "Correct. Eosinophil granules carry molecules toxic to organisms too large to phagocytose, particularly helminths, while basophils release mediators such as histamine that drive the inflammatory and allergic response."],
    ["Both present antigen to lymphocytes as their principal function",
     "Antigen presentation belongs to macrophages and dendritic cells; neither of these granulocytes is a professional presenter."],
    ["Both are the body's principal phagocytes against bacteria",
     "Neutrophils and macrophages fill that role; the eosinophil is at most a minor phagocyte."]],
  c=1, cite=L5 + ", Slides 66-70"),

dict(topic="Nonspecific Host Defenses", io="3.5 — Macrophage versus neutrophil",
  q="A macrophage and a neutrophil are both phagocytes. What does the macrophage do that the neutrophil does not?",
  opts=[
    ["It releases histamine to increase vascular permeability",
     "Histamine release is a basophil and mast cell function rather than a macrophage one."],
    ["It circulates in the bloodstream while the neutrophil stays in tissue",
     "This reverses them: neutrophils circulate and are recruited into tissue, while macrophages are the tissue-resident form."],
    ["It kills organisms directly while the neutrophil only marks them",
     "Both kill directly; the distinguishing capability is antigen presentation and cytokine secretion."],
    ["It presents antigen to lymphocytes and secretes cytokines",
     "Correct. The neutrophil kills and dies, whereas the macrophage additionally processes what it engulfs and displays it to lymphocytes, which is the bridge to the specific immune response."]],
  c=3, cite=L5 + ", Slides 66-72"),

dict(topic="Nonspecific Host Defenses", io="3.6 — White blood count with differential",
  q="A white blood count with differential is ordered. What does it measure, and what can it tell you that a total count alone cannot?",
  opts=[
    ["It totals each type of white cell and shows whether they are in normal proportion",
     "Correct. A total count says how many cells there are, while the differential says which kinds, so a normal total can still conceal a badly skewed proportion pointing to bacterial or viral infection."],
    ["It measures only the total number of white cells, more precisely than a plain count",
     "That is what a plain count already does; the differential adds the breakdown by cell type."],
    ["It measures antibody levels against specific organisms",
     "Antibody titres are a separate serological measurement and are not part of a blood count."],
    ["It identifies which organism is causing the infection",
     "It can suggest a bacterial or viral pattern but cannot name an organism; that requires culture or molecular testing."]],
  c=0, cite=L5 + ", Slides 70-74"),

dict(topic="Nonspecific Host Defenses", io="3.7 — Inflammation",
  q="Inflammation has four classical signs. Name them, and say how the redness and heat actually come about.",
  opts=[
    ["Redness, heat, swelling and pain; the first two from vasoconstriction concentrating blood",
     "Constriction would reduce flow and make the area paler and cooler; it is dilation that produces redness and warmth."],
    ["Redness, heat, swelling and pain; the first two from vasodilation increasing blood flow to the area",
     "Correct. Rubor, calor, tumor and dolor are the four, and widening the arterioles brings more warm blood into the injured region, which produces both the redness and the heat."],
    ["Redness, heat, pus and fever; the first two from neutrophils releasing pigment",
     "Pus and fever are consequences rather than the four classical signs, and no pigment is involved in the redness."],
    ["Swelling, pain, itching and scaling; the first two from mast cell histamine alone",
     "Itching and scaling are not among the classical signs, and histamine is one mediator among several driving the vascular changes."]],
  c=1, cite=L5 + ", Slides 34-40"),

dict(topic="Nonspecific Host Defenses", io="3.8 — Fever",
  q="What causes fever, why is it beneficial, and why is it dangerous?",
  opts=[
    ["Dehydration raises core temperature; it conserves fluid, but causes confusion",
     "Fever is a regulated rise in the hypothalamic set point driven by cytokines rather than a consequence of fluid loss."],
    ["Bacterial endotoxin acts directly on the skin; it kills all pathogens outright, and carries no real risk",
     "Endotoxin acts by inducing host cytokines rather than directly on skin, fever inhibits rather than sterilises, and high fever genuinely does harm."],
    ["Cytokines reset the set point; it inhibits pathogens but high fever harms tissue",
     "Correct. Interleukin-1, interleukin-6 and tumour necrosis factor act systemically to raise the hypothalamic set point; the higher temperature slows microbial growth and accelerates host defence, yet sustained extremes denature host proteins and harm the patient."],
    ["Histamine from mast cells; it increases blood flow, but causes swelling",
     "Histamine drives the local vascular changes of inflammation rather than the systemic set-point change that produces fever."]],
  c=2, cite=L5 + ", Slides 40-46"),

dict(topic="Nonspecific Host Defenses", io="3.9 — Interferon",
  q="Which kind of organism prompts interferon production, and what exactly does interferon do to it?",
  opts=[
    ["A virus, and interferon does not kill it — it prevents spread to surrounding cells",
     "Correct. Interferon acts on neighbouring uninfected cells, inducing an antiviral state so the infection cannot propagate; the already-infected cell is not rescued and the virus is not destroyed."],
    ["A virus, and interferon destroys the viral particles directly",
     "Interferon has no direct virucidal action; it changes the state of nearby cells so that the virus cannot establish in them."],
    ["A bacterium, and interferon lyses it through the membrane attack complex",
     "The membrane attack complex belongs to complement, and interferon is produced in response to viral rather than bacterial infection."],
    ["A parasite, and interferon coats it so phagocytes can engulf it",
     "Coating a target for phagocytosis is opsonisation, performed by antibody and complement rather than interferon."]],
  c=0, cite=L5 + ", Slides 48-52"),

dict(topic="Nonspecific Host Defenses", io="3.10 — Complement",
  q="Three pathways can switch complement on. In what order are they activated, and what do all three converge on?",
  opts=[
    ["Lectin, then classical, then alternative, all converging on forming C1",
     "The sequence is wrong and C1 belongs to the start of the classical pathway rather than being the convergence point, which is C3."],
    ["Classical, then lectin, then alternative, all converging on cleaving C3",
     "This is the order in which the pathways were discovered, not the order in which they are activated; the classical pathway is the slowest because it needs antibody to be present."],
    ["Alternative, then lectin, then classical, all converging on cleaving C3",
     "Correct. The alternative pathway fires immediately with no prior recognition needed, the lectin pathway follows, and the classical pathway comes last because it waits on antibody; the difference between them is only how they start, since all three cleave C3."],
    ["Alternative, then classical, then lectin, all converging on forming antibody",
     "The lectin pathway precedes the classical one, and complement does not produce antibody; it is activated by it in one pathway only."]],
  c=2, cite=L5 + ", Slides 42-46"),

dict(topic="Nonspecific Host Defenses", io="3.10 — Complement",
  q="Cleaving C3 produces two fragments. What does each one do, and what makes the larger fragment able to stick to a pathogen?",
  opts=[
    ["C3b attaches and marks the surface; C3a recruits phagocytes; a thioester bond is exposed",
     "Correct. Cleavage exposes the thioester bond on C3b, which reacts with a hydroxyl or amino group on the pathogen surface to fix complement there, while C3a diffuses away as a chemoattractant."],
    ["C3a attaches to the surface and C3b recruits phagocytes, through an exposed disulphide bond",
     "The fragments are swapped, and the reactive group exposed by cleavage is a thioester rather than a disulphide bond."],
    ["Both fragments attach to the surface, held by hydrogen bonding",
     "Only C3b attaches; C3a is released into the surroundings, and hydrogen bonds would be far too weak to anchor it covalently."],
    ["C3b lyses the pathogen directly and C3a neutralises its toxins",
     "Lysis requires the membrane attack complex assembled later in the cascade, and toxin neutralisation is an antibody function."]],
  c=0, cite=L5 + ", Slides 42-45"),

dict(topic="Nonspecific Host Defenses", io="3.4 — The leukocytes",
  q="Neutrophils arrive at an infection and phagocytose bacteria. What happens to them afterwards, and what does the patient see as a result?",
  opts=[
    ["They mature into macrophages and remain in the tissue permanently",
     "Macrophages differentiate from monocytes rather than from neutrophils, which are a separate lineage."],
    ["They recycle their granules and return to the circulation, so no visible change occurs",
     "Neutrophils cannot restock their granules; the cell is consumed by the act of killing."],
    ["They cannot replenish their granules, so they die, and the accumulated dead cells appear as pus",
     "Correct. Each neutrophil has one load of granule contents and no means of making more, so it is spent after its work and the collected remains form the visible purulent material."],
    ["They release histamine and cause the swelling seen at the site",
     "Histamine comes from basophils and mast cells, and the swelling reflects increased vascular permeability rather than neutrophil contents."]],
  c=2, cite=L5 + ", Slides 76-78"),

# ─────────── Lecture 6 — Specific Immunity (8) ───────────
# Also not reviewed in class, and weighted evenly for the same reason.

dict(topic="Specific Immunity", io="1 — Relate innate and specific immunity",
  q="Immunity can be natural or artificial and active or passive. Which combination describes a person who receives antibody across the placenta?",
  opts=[
    ["Natural active",
     "Natural active immunity follows actually having the infection and mounting your own response, which produces memory."],
    ["Natural passive",
     "Correct. Nothing was engineered, so it is natural, and the recipient is given ready-made antibody rather than producing it, so it is passive and therefore temporary."],
    ["Artificial passive",
     "Artificial passive immunity means receiving antibody as a deliberate treatment, such as an immunoglobulin injection, rather than across the placenta."],
    ["Artificial active",
     "Artificial active immunity is what vaccination produces, where the recipient makes their own response to an administered antigen."]],
  c=1, cite=L6 + ", Slides 6-12"),

dict(topic="Specific Immunity", io="4 — Antibody structure, class and function",
  q="An antibody monomer is built from how many chains, and which fragment binds the antigen?",
  opts=[
    ["Two chains, one heavy and one light, with the constant fragment binding antigen",
     "A monomer has four chains, and the constant fragment binds host cells and complement rather than antigen."],
    ["Four chains, two heavy and two light, with the antigen-binding fragment at the variable ends",
     "Correct. Two identical heavy and two identical light chains form the Y, and the variable regions at the tips of the arms make up the fragment that binds antigen."],
    ["Four chains, all identical, with the stem binding antigen",
     "The heavy and light chains differ from one another, and the stem is the portion that interacts with immune cells."],
    ["Six chains, three heavy and three light, with the hinge binding antigen",
     "The monomer carries four chains, and the hinge provides flexibility rather than binding."]],
  c=1, cite=L6 + ", Slides 40-48"),

dict(topic="Specific Immunity", io="4 — Antibody structure, class and function",
  q="Which antibody class appears first in a new infection, which is the most abundant overall, and which guards mucosal surfaces?",
  opts=[
    ["Immunoglobulin M first, immunoglobulin G most abundant, immunoglobulin A at mucosal surfaces",
     "Correct. The pentameric immunoglobulin M is produced first and is by far the largest, immunoglobulin G dominates the circulating pool and crosses the placenta, and immunoglobulin A is secreted onto mucous membranes."],
    ["Immunoglobulin G first, immunoglobulin M most abundant, immunoglobulin E at mucosal surfaces",
     "Immunoglobulin G predominates in the secondary response rather than appearing first, and immunoglobulin E is associated with allergy and parasites."],
    ["Immunoglobulin A first, immunoglobulin E most abundant, immunoglobulin D at mucosal surfaces",
     "Immunoglobulin E is present in only trace amounts, and immunoglobulin D sits on naive B cell surfaces rather than guarding mucosa."],
    ["Immunoglobulin E first, immunoglobulin A most abundant, immunoglobulin M at mucosal surfaces",
     "Immunoglobulin E is the least abundant class, and immunoglobulin M is too large to be secreted efficiently onto surfaces."]],
  c=0, cite=L6 + ", Slides 50-60"),

dict(topic="Specific Immunity", io="3 — Antigens, antibodies and leukocytes",
  q="Clonal selection explains how the right antibody is produced. When are the receptor specificities generated?",
  opts=[
    ["Before any antigen has entered, so the antigen selects a clone that already exists",
     "Correct. The enormous repertoire is generated during lymphocyte development by gene rearrangement, so an arriving antigen does not instruct anything; it simply finds and expands the clone whose receptor already fits."],
    ["After the antigen arrives, which instructs the cell to build a matching receptor",
     "This is the discarded instructional model; receptors are made in advance and the antigen selects among them."],
    ["Only in the bone marrow during an active infection",
     "The repertoire is laid down during development rather than being generated afresh at each infection."],
    ["Continuously in the thymus in response to circulating antigen",
     "T cells mature in the thymus, but their receptor diversity is generated independently of whichever antigens happen to be present."]],
  c=0, cite=L6 + ", Slides 30-38"),

dict(topic="Specific Immunity", io="3 — Antigens, antibodies and leukocytes",
  q="Class one and class two major histocompatibility complex molecules present antigen to different cells. Which presents to which?",
  opts=[
    ["Class one presents to cytotoxic T cells; class two presents to helper T cells",
     "Correct. Class one is on nearly every nucleated cell and displays what is being made inside it to the cytotoxic subset, while class two is on antigen-presenting cells and displays engulfed material to helper cells."],
    ["Class one presents to helper T cells; class two presents to cytotoxic T cells",
     "The two are reversed: helper cells carry the cluster of differentiation 4 marker that binds class two."],
    ["Class one presents to B cells; class two presents to natural killer cells",
     "B cells recognise antigen directly through their own receptor, and natural killer cells respond to the ABSENCE of class one rather than being presented to."],
    ["Both present only to helper T cells, differing in the tissues that carry them",
     "They differ in which T cell subset they engage, not merely in distribution."]],
  c=0, cite=L6 + ", Slides 20-28"),

dict(topic="Specific Immunity", io="3 — Antigens, antibodies and leukocytes",
  q="Antibody protects in several ways. Which describes opsonisation, and which describes neutralisation?",
  opts=[
    ["Opsonisation clumps organisms together; neutralisation activates complement",
     "Clumping is agglutination and complement activation is fixation; both are separate antibody functions."],
    ["Opsonisation blocks attachment sites; neutralisation coats the organism for phagocytosis",
     "The two are swapped: coating for engulfment is opsonisation."],
    ["Opsonisation coats the organism so phagocytes engulf it; neutralisation blocks its attachment sites",
     "Correct. Coating marks the target and gives the phagocyte something to grip, while neutralisation works by occupying the structures a virus or toxin needs in order to bind host cells."],
    ["Opsonisation lyses the organism; neutralisation recruits neutrophils",
     "Lysis requires the complement membrane attack complex, and recruitment is driven by chemotactic fragments rather than by neutralisation."]],
  c=2, cite=L6 + ", Slides 62-70"),

dict(topic="Specific Immunity", io="3 — Antigens, antibodies and leukocytes",
  q="A patient meets the same antigen a second time. How does the response differ from the first, and what is it called?",
  opts=[
    ["It is weaker, because tolerance develops after the first exposure",
     "Tolerance applies to self antigens; a repeated foreign antigen provokes a stronger rather than a weaker response."],
    ["It is slower but produces a higher titre of immunoglobulin M; it is the primary response",
     "The primary response is the first encounter, and the memory response is faster with immunoglobulin G predominating."],
    ["It is identical to the first, since memory affects only cell-mediated immunity",
     "Memory operates in both arms, and the whole point of the second response is that it differs markedly."],
    ["It is faster and produces a much higher titre of immunoglobulin G; it is the anamnestic response",
     "Correct. Memory cells laid down by the first exposure are already present and pre-committed, so the second response begins sooner, climbs higher and is dominated by immunoglobulin G rather than immunoglobulin M."]],
  c=3, cite=L6 + ", Slides 72-80"),

dict(topic="Specific Immunity", io="1 — Relate innate and specific immunity",
  q="Which cell links the innate response to the specific one, and how does it do it?",
  opts=[
    ["The plasma cell, by detecting patterns on the pathogen surface",
     "Plasma cells are the end point of B cell activation and secrete antibody; pattern recognition is an innate function."],
    ["The neutrophil, by secreting antibody once it has phagocytosed an organism",
     "Neutrophils do not present antigen or produce antibody; they kill and then die."],
    ["The natural killer cell, by producing memory against the organism it destroys",
     "Natural killer cells are innate and generate no immunological memory of a specific antigen."],
    ["The antigen-presenting cell, by displaying processed antigen on class two molecules",
     "Correct. Macrophages and dendritic cells act within the nonspecific response but then present processed antigen to helper T cells, which is the step that recruits the specific system."]],
  c=3, cite=L6 + ", Slides 6-18"),
]
