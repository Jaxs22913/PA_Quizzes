# Pharmacology I Lecture 1 — Antibacterials, pool part C
# Objectives 4e-4i and 4k-4o: macrolides, lincosamides, tetracyclines,
# aminoglycosides, fluoroquinolones, oxazolidinones, polypeptides, folate
# synthesis inhibitors, nitroimidazoles.
#
# Correct answer always written first; the partition script rotates.
#
# Note on Septra strengths: the slide prints the double-strength tablet as
# 800/120 mg. The conventional figure is 800/160. Deliberately NOT asked --
# a printed number that contradicts a bedrock fact is more likely an error in
# the deck than a fact worth testing.
SRC = "Antibiotics, Antivirals, and Antifungals.pptx"
def c(n): return f"{SRC}, Slide {n}"

IO4E = "4e — Macrolides/ketolides"
IO4F = "4f — Lincosamides"
IO4H = "4h — Tetracyclines"
IO4I = "4i — Aminoglycosides"
IO4K = "4k — Fluoroquinolones"
IO4L = "4l — Oxazolidinones"
IO4M = "4m — Polypeptides"
IO4N = "4n — Folate synthesis inhibitors"
IO4O = "4o — Nitroimidazoles"
IO2 = "2 — Common modes of action of antimicrobial agents"

POOL_C = [
 dict(topic="Protein synthesis", io=IO2,
   q="Which antibiotic classes bind the 50S ribosomal subunit, and which bind the 30S?",
   opts=[
     ["50S — macrolides, clindamycin, chloramphenicol, streptogramins; 30S — aminoglycosides, tetracyclines",
      "Correct. The bacterial ribosome is 70S against the mammalian 80S, which is the basis for selectivity."],
     ["50S — aminoglycosides, tetracyclines; 30S — macrolides, clindamycin, chloramphenicol, streptogramins",
      "This reverses the two groups."],
     ["50S — fluoroquinolones, metronidazole; 30S — penicillins, cephalosporins",
      "None of those four is a protein synthesis inhibitor; they act on DNA or the cell wall."],
     ["50S — vancomycin, daptomycin; 30S — linezolid, tigecycline",
      "Vancomycin and daptomycin act at the cell wall and membrane rather than the ribosome."]],
   c=0, cite=c(53)),

 dict(topic="Protein synthesis", io=IO2,
   q="Why can high levels of a protein synthesis inhibitor produce host toxicity?",
   opts=[
     ["At high levels the drug may interact with mammalian 80S ribosomes rather than only the bacterial 70S ribosome",
      "Correct. Selectivity is a matter of degree, not an absolute barrier, which is why these agents have dose-related toxicity."],
     ["The drug is metabolized to a reactive intermediate that damages hepatocytes",
      "Reactive metabolite toxicity is not the explanation the lecture gives for this class."],
     ["Human cells lack the efflux pumps that protect bacteria from accumulation",
      "Efflux is not part of the reasoning here."],
     ["Mammalian mitochondria use a 90S ribosome that binds these drugs preferentially",
      "The lecture contrasts bacterial 70S with mammalian 80S; there is no 90S ribosome."]],
   c=0, cite=c(53)),

 dict(topic="Macrolides", io=IO4E,
   q="What is the macrolide mechanism of action?",
   opts=[
     ["Binding the 50S subunit and inhibiting protein synthesis by blocking transpeptidation",
      "Correct. Note transpeptidation is blocked at the ribosome here, quite separately from the cell wall transpeptidation penicillins target."],
     ["Binding the 30S subunit and preventing transfer RNA from occupying the A site",
      "That is the tetracycline mechanism."],
     ["Inhibiting bacterial DNA gyrase and topoisomerase IV",
      "That is the fluoroquinolone mechanism."],
     ["Binding the two D-alanine residues to block cell wall cross-linking",
      "That is vancomycin."]],
   c=0, cite=c(54)),

 dict(topic="Macrolides", io=IO4E,
   q="Which atypical organisms do macrolides cover?",
   opts=[
     ["Legionella species, Mycoplasma pneumoniae, Chlamydophila pneumoniae and Chlamydia trachomatis",
      "Correct, and this atypical coverage is what makes them a community-acquired pneumonia agent."],
     ["Pseudomonas aeruginosa, Acinetobacter and Stenotrophomonas",
      "Those are resistant Gram-negative organisms outside the macrolide spectrum."],
     ["Bacteroides fragilis and Clostridium perfringens",
      "The lecture states macrolides are not used clinically for anaerobes."],
     ["Rickettsiae, Borrelia burgdorferi and Brucella",
      "Those animal-borne organisms are the tetracycline strength."]],
   c=0, cite=c(55)),

 dict(topic="Macrolides", io=IO4E,
   q="Which cardiac adverse effect do macrolides carry, and what increases the risk?",
   opts=[
     ["QT prolongation and torsades de pointes, increased by class Ia and class III antiarrhythmics and by electrolyte abnormalities",
      "Correct. Fluoroquinolones and some azoles share this liability, so combinations compound it."],
     ["Bradycardia and heart block, increased by beta-blockers",
      "Conduction block is not the macrolide effect described."],
     ["Hypertensive crisis, increased by tyramine-containing foods",
      "That is the linezolid concern via monoamine oxidase inhibition."],
     ["Cardiomyopathy, increased by cumulative dose",
      "Cumulative-dose cardiomyopathy is not attributed to macrolides here."]],
   c=0, cite=c(57)),

 dict(topic="Macrolides", io=IO4E,
   q="How do macrolides interact with other drugs, and in what order of severity?",
   opts=[
     ["Metabolites bind CYP3A subclass enzymes forming an inactive complex, raising levels of substrates such as carbamazepine, cyclosporine, digoxin, midazolam and theophylline, with erythromycin greater than clarithromycin greater than azithromycin",
      "Correct. The ranking is the practical point: azithromycin is the one to reach for when interactions matter."],
     ["They induce CYP3A4, lowering levels of the same substrates, with azithromycin the strongest inducer",
      "The effect is inhibition through an inactive complex, not induction, and azithromycin is the weakest."],
     ["They chelate divalent cations, reducing absorption of co-administered drugs",
      "Chelation is the tetracycline and fluoroquinolone interaction."],
     ["They displace substrates from plasma protein binding sites",
      "Protein displacement is not the mechanism given."]],
   c=0, cite=c(59)),

 dict(topic="Macrolides", io=IO4E,
   q="Which macrolide-containing regimen is named for Helicobacter pylori?",
   opts=[
     ["Prevpac — clarithromycin, amoxicillin and lansoprazole",
      "Correct. A macrolide, a penicillin and a proton pump inhibitor together."],
     ["Clarithromycin with ethambutol and rifabutin",
      "That combination is for disseminated Mycobacterium avium complex."],
     ["Azithromycin with doxycycline",
      "That pairing is not the Helicobacter pylori regimen given here."],
     ["Erythromycin with metronidazole and omeprazole",
      "The lecture names clarithromycin, amoxicillin and lansoprazole specifically."]],
   c=0, cite=c(56)),

 dict(topic="Tetracyclines", io=IO4H,
   q="What is the tetracycline mechanism of action?",
   opts=[
     ["Binding 16S ribosomal RNA of the 30S subunit, preventing transfer RNA from binding in the A site",
      "Correct, and the result is bacteriostatic and broad-spectrum."],
     ["Binding the 50S subunit and blocking transpeptidation",
      "That is the macrolide mechanism."],
     ["Inhibiting dihydrofolate reductase and blocking folate synthesis",
      "That is trimethoprim."],
     ["Forming channels in the cell membrane that allow potassium to leak out",
      "That is the amphotericin B mechanism in fungi."]],
   c=0, cite=c(61)),

 dict(topic="Tetracyclines", io=IO4H,
   q="Which organisms does the lecture list as excellent tetracycline coverage?",
   opts=[
     ["Atypicals and animal-borne organisms — Yersinia pestis, Brucella, Borrelia burgdorferi and rickettsiae",
      "Correct. Poor coverage is specified for Pseudomonas and Clostridium difficile."],
     ["Pseudomonas aeruginosa and Clostridium difficile",
      "Those are named explicitly as poor coverage."],
     ["Enterococcus and Listeria monocytogenes only",
      "Enterococcus falls under good rather than excellent coverage, and the list is broader than this."],
     ["Anaerobes exclusively, with no aerobic activity",
      "Anaerobes appear under good coverage, and the class is broad-spectrum."]],
   c=0, cite=c(62)),

 dict(topic="Tetracyclines", io=IO4H,
   q="Why must tetracyclines be separated from iron and calcium-containing products?",
   opts=[
     ["They chelate with cations, which the lecture flags as an important food interaction",
      "Correct. The same chelation problem applies to the fluoroquinolones with antacids, dairy and multivitamins."],
     ["Cations induce the hepatic enzymes that metabolize tetracyclines",
      "Enzyme induction is not the mechanism; the interaction is chemical binding in the gut."],
     ["Cations raise gastric pH enough to destroy the drug",
      "Acid degradation is not what the lecture describes here."],
     ["Cations compete for the same renal transporter, accelerating elimination",
      "The interaction described is chelation, not competition at a transporter."]],
   c=0, cite=c(63)),

 dict(topic="Tetracyclines", io=IO4H,
   q="Which tetracycline precautions relate to children and pregnancy?",
   opts=[
     ["Discoloration of teeth and depression of skeletal growth — avoid under 8 years old and in the second and third trimesters",
      "Correct. Both follow from the drug binding calcium in developing bone and teeth."],
     ["Cartilage damage — avoid under 18 years old",
      "That caution belongs to the fluoroquinolones."],
     ["Kernicterus — avoid in the first 30 days of life",
      "The neonatal restriction in this lecture attaches to ceftriaxone."],
     ["Grey baby syndrome — avoid in all trimesters",
      "That is a chloramphenicol effect and is not the caution given here."]],
   c=0, cite=c(63)),

 dict(topic="Tetracyclines", io=IO4H,
   q="Tigecycline is a glycylcycline. What is its indication profile?",
   opts=[
     ["Complicated skin and complicated intra-abdominal infections, covering methicillin-resistant Staphylococcus aureus and Enterococcus faecalis but not vancomycin-resistant Enterococcus",
      "Correct. It binds the 30S subunit and is bacteriostatic, like the tetracyclines it derives from."],
     ["Uncomplicated urinary tract infection and outpatient sinusitis",
      "Its approved indications are the complicated skin and intra-abdominal ones."],
     ["Pseudomonal pneumonia and febrile neutropenia",
      "Those require antipseudomonal agents."],
     ["Clostridium difficile colitis by the oral route",
      "Oral vancomycin and metronidazole are the agents named for Clostridium difficile."]],
   c=0, cite=c(65)),

 dict(topic="Aminoglycosides", io=IO4I,
   q="Aminoglycosides are the drug of choice for which situations?",
   opts=[
     ["Febrile neutropenia, sepsis, and enterococcal synergy",
      "Correct, with Enterococcus covered only at synergy dosing rather than as monotherapy."],
     ["Community-acquired pneumonia and acute otitis media",
      "Those are macrolide, aminopenicillin and respiratory fluoroquinolone indications."],
     ["Methicillin-resistant Staphylococcus aureus skin infection",
      "Aminoglycoside activity is against Gram-negatives, not resistant Gram-positives."],
     ["Clostridium difficile colitis",
      "That is treated with metronidazole or oral vancomycin."]],
   c=0, cite=c(68)),

 dict(topic="Aminoglycosides", io=IO4I,
   q="Why did aminoglycoside dosing move from every 8 hours to every 24 hours?",
   opts=[
     ["They show a post-antibiotic effect, so killing persists after the level falls, and concentration-dependent killing favours a large single dose",
      "Correct. This is the clearest clinical application of the concentration-dependent pattern from earlier in the lecture."],
     ["They show time-dependent killing, so a longer interval keeps levels above the minimal inhibitory concentration",
      "Time-dependent killing argues for frequent or continuous dosing, which is the opposite."],
     ["Once-daily dosing eliminates the need for therapeutic drug monitoring",
      "Monitoring is still required; peaks and troughs are specified around the third or fourth dose."],
     ["Renal clearance is so rapid that more frequent dosing has no effect",
      "Renal toxicity, not rapid clearance, is the dosing consideration named."]],
   c=0, cite=c(68)),

 dict(topic="Aminoglycosides", io=IO4I,
   q="What are the once-daily doses and trough targets for the aminoglycosides in this lecture?",
   opts=[
     ["Tobramycin and gentamicin 7 milligrams per kilogram with a trough under 1; amikacin 15 milligrams per kilogram with a trough under 5",
      "Correct. Peaks are drawn 30 minutes after the end of the infusion and troughs 15 to 30 minutes before the next dose."],
     ["Tobramycin and gentamicin 15 milligrams per kilogram with a trough under 5; amikacin 7 milligrams per kilogram with a trough under 1",
      "This swaps the two agents' doses and targets."],
     ["All three at 5 milligrams per kilogram with a trough under 2",
      "The lecture separates amikacin from the other two."],
     ["Tobramycin and gentamicin 7 milligrams per kilogram with a trough of 15 to 20",
      "A trough of 15 to 20 is a vancomycin goal, not an aminoglycoside one."]],
   c=0, cite=c(69)),

 dict(topic="Aminoglycosides", io=IO4I,
   q="Which toxicities define the aminoglycoside class?",
   opts=[
     ["Renal toxicity and ototoxicity, requiring renal dose adjustment",
      "Correct, and vancomycin shares both, which is why the combination is watched carefully."],
     ["Hepatotoxicity and thrombocytopenia",
      "Thrombocytopenia is the linezolid concern; hepatic effects belong to other agents."],
     ["Tendon rupture and peripheral neuropathy",
      "Those are fluoroquinolone effects."],
     ["Serotonin syndrome and hypertensive crisis",
      "Those follow from linezolid's interactions."]],
   c=0, cite=c(68)),

 dict(topic="Oxazolidinones", io=IO4L,
   q="Linezolid is the drug of choice for which infections, and what does it not cover?",
   opts=[
     ["Hospital-acquired and community-acquired methicillin-resistant Staphylococcus aureus; it covers no Gram-negatives or anaerobes",
      "Correct. It also covers multidrug-resistant pneumococcus and vancomycin-resistant Enterococcus."],
     ["Pseudomonal and multidrug-resistant Gram-negative infection; it does not cover Gram-positives",
      "This inverts the spectrum entirely."],
     ["Anaerobic intra-abdominal infection; it does not cover aerobes",
      "Anaerobes are explicitly outside its coverage."],
     ["Atypical pneumonia; it does not cover Staphylococcus",
      "Staphylococcus, including resistant strains, is precisely what it is for."]],
   c=0, cite=c(71)),

 dict(topic="Oxazolidinones", io=IO4L,
   q="Which linezolid interactions can produce serotonin syndrome?",
   opts=[
     ["Selective serotonin reuptake inhibitors, tyramine-containing foods, and pseudoephedrine",
      "Correct, and platelets are monitored separately because of thrombocytopenia."],
     ["Warfarin, phenytoin and digoxin",
      "Those are the sulfamethoxazole/trimethoprim interactions."],
     ["Iron, calcium and dairy products",
      "Those chelate tetracyclines and fluoroquinolones rather than causing serotonin syndrome."],
     ["Ethanol, producing a disulfiram-like reaction",
      "That is metronidazole."]],
   c=0, cite=c(71)),

 dict(topic="Fluoroquinolones", io=IO4K,
   q="What is the dual mechanism of action of the fluoroquinolones?",
   opts=[
     ["Inhibition of bacterial DNA gyrase, also called topoisomerase II, forming a quinolone-DNA-gyrase complex with induced DNA cleavage, plus inhibition of topoisomerase IV",
      "Correct. The lecture notes the topoisomerase IV mechanism is poorly understood."],
     ["Inhibition of the 30S and 50S ribosomal subunits simultaneously",
      "Fluoroquinolones do not act at the ribosome."],
     ["Inhibition of dihydrofolate reductase and tetrahydropteroic acid synthetase",
      "That dual block is sulfamethoxazole with trimethoprim."],
     ["Inhibition of cell wall cross-linking and of beta-lactamase",
      "Neither applies to this class."]],
   c=0, cite=c(74)),

 dict(topic="Fluoroquinolones", io=IO4K,
   q="Which fluoroquinolone must not be used for urinary tract infection?",
   opts=[
     ["Moxifloxacin",
      "Correct. It also lacks Pseudomonas coverage, unlike levofloxacin, and needs no renal dose adjustment."],
     ["Ciprofloxacin",
      "Ciprofloxacin is a standard urinary tract agent with Gram-negative coverage."],
     ["Levofloxacin",
      "Levofloxacin is listed among the urinary tract options."],
     ["All three are equally suitable for urinary tract infection",
      "The lecture singles out moxifloxacin as the exception."]],
   c=0, cite=c(78)),

 dict(topic="Fluoroquinolones", io=IO4K,
   q="How do levofloxacin and moxifloxacin differ in coverage?",
   opts=[
     ["Levofloxacin has Pseudomonas coverage; moxifloxacin does not",
      "Correct. Both improve on ciprofloxacin's Gram-positive activity and both cover community-acquired pneumonia."],
     ["Moxifloxacin has Pseudomonas coverage; levofloxacin does not",
      "This reverses the two agents."],
     ["Levofloxacin covers atypicals; moxifloxacin does not",
      "Both are described as covering Streptococcus pneumoniae and atypicals."],
     ["Moxifloxacin requires renal adjustment; levofloxacin does not",
      "The reverse is stated — moxifloxacin has no dosing consideration listed while levofloxacin is renally adjusted."]],
   c=0, cite=c(77)),

 dict(topic="Fluoroquinolones", io=IO4K,
   q="Which musculoskeletal and neurologic adverse effects are listed for the fluoroquinolones?",
   opts=[
     ["Tendonitis and Achilles tendon rupture, peripheral neuropathies, and central nervous system toxicity, with caution under 18 years of age",
      "Correct, alongside QT prolongation, photosensitivity and complexing with cations."],
     ["Ototoxicity and nephrotoxicity requiring trough monitoring",
      "Those belong to the aminoglycosides and vancomycin."],
     ["Depression of skeletal growth and discoloration of teeth",
      "Those are tetracycline effects."],
     ["Thrombocytopenia and serotonin syndrome",
      "Those follow from linezolid."]],
   c=0, cite=c(79)),

 dict(topic="Fluoroquinolones", io=IO4K,
   q="What collateral consequence of fluoroquinolone overuse does the lecture emphasise?",
   opts=[
     ["High rates of resistance, and Clostridium difficile as collateral damage",
      "Correct. The slide states overuse equals resistance in capital letters, which is a deliberate emphasis."],
     ["Accelerated hepatic metabolism of co-administered drugs",
      "Fluoroquinolones inhibit CYP1A2 rather than inducing metabolism."],
     ["Permanent loss of Gram-positive coverage across the class",
      "Resistance is described in general terms, not as a loss of Gram-positive activity specifically."],
     ["Cross-resistance to all beta-lactams",
      "No such cross-resistance is claimed."]],
   c=0, cite=c(75)),

 dict(topic="Lincosamides", io=IO4F,
   q="What is clindamycin's coverage, and what is the notable gap?",
   opts=[
     ["Gram-positive aerobes including methicillin-resistant Staphylococcus aureus, plus Gram-positive and Gram-negative anaerobes, with no Gram-negative aerobic coverage",
      "Correct. The gap is Gram-negative aerobes, which is why it is combined with another agent for intra-abdominal infection."],
     ["Gram-negative aerobes only, with no Gram-positive activity",
      "This is the reverse of clindamycin's profile."],
     ["Atypical organisms only",
      "Atypical coverage belongs to macrolides, tetracyclines and fluoroquinolones."],
     ["Broad coverage with no significant gaps",
      "The lecture names a specific gap in Gram-negative aerobic coverage."]],
   c=0, cite=c(80)),

 dict(topic="Lincosamides", io=IO4F,
   q="Which adverse effects are listed for clindamycin?",
   opts=[
     ["Rash, neutropenia, thrombocytopenia, Clostridium difficile and pseudomembranous colitis",
      "Correct. The association with Clostridium difficile is the one clinicians reach for first with this drug."],
     ["Tendon rupture and photosensitivity",
      "Those belong to the fluoroquinolones."],
     ["Ototoxicity and nephrotoxicity",
      "Those belong to the aminoglycosides and vancomycin."],
     ["Disulfiram-like reaction with ethanol",
      "That belongs to metronidazole."]],
   c=0, cite=c(81)),

 dict(topic="Lincosamides", io=IO4F,
   q="Clindamycin is the drug of choice for which situations?",
   opts=[
     ["Toxin-mediated disease, skin and soft tissue infection, osteomyelitis, surgical prophylaxis in penicillin allergy, and as part of intra-abdominal combination therapy",
      "Correct. The toxin-mediated indication follows from inhibiting bacterial protein synthesis and therefore toxin production."],
     ["Pseudomonal pneumonia and febrile neutropenia",
      "It has no Gram-negative aerobic coverage at all."],
     ["Urinary tract infection and pyelonephritis",
      "Urinary indications belong to agents with Gram-negative coverage."],
     ["Meningitis requiring central nervous system penetration",
      "Central nervous system penetration is discussed for carbapenems and third generation cephalosporins."]],
   c=0, cite=c(80)),

 dict(topic="Folate inhibitors", io=IO4N,
   q="How do sulfamethoxazole and trimethoprim block folate synthesis at two different steps?",
   opts=[
     ["Sulfamethoxazole inhibits conversion of para-aminobenzoic acid to dihydrofolic acid via tetrahydropteroic acid synthetase; trimethoprim inhibits conversion of dihydrofolic acid to tetrahydrofolic acid via dihydrofolate reductase",
      "Correct. Two sequential steps in one pathway, which is what makes the combination synergistic."],
     ["Sulfamethoxazole inhibits dihydrofolate reductase; trimethoprim inhibits tetrahydropteroic acid synthetase",
      "This swaps the two enzymes."],
     ["Both inhibit dihydrofolate reductase, at different binding sites",
      "They act at different steps of the pathway, not the same enzyme."],
     ["Sulfamethoxazole blocks folate absorption from the gut; trimethoprim blocks its renal reabsorption",
      "Neither acts on absorption or reabsorption; both inhibit synthesis enzymes."]],
   c=0, cite=c(82)),

 dict(topic="Folate inhibitors", io=IO4N,
   q="Which infection is sulfamethoxazole/trimethoprim used for in both treatment and prophylaxis?",
   opts=[
     ["Pneumocystis jirovecii pneumonia",
      "Correct, alongside urinary tract infection, bacterial prostatitis, orchitis and epididymitis."],
     ["Mycobacterium avium complex",
      "That is treated with clarithromycin or azithromycin plus ethambutol."],
     ["Clostridium difficile colitis",
      "That is metronidazole or oral vancomycin."],
     ["Lyme disease",
      "Doxycycline is the tetracycline used for Lyme disease."]],
   c=0, cite=c(84)),

 dict(topic="Folate inhibitors", io=IO4N,
   q="Which drug interaction of sulfamethoxazole/trimethoprim involves cytochrome P450 2C9 inhibition?",
   opts=[
     ["A significant increase in the international normalised ratio in patients on warfarin",
      "Correct. Other interactions include raised phenytoin, rifampin and digoxin levels, reduced methotrexate clearance, and hypoglycaemia with sulfonylureas."],
     ["Reduced effectiveness of oral contraceptives through gut flora disruption",
      "That is the aminopenicillin interaction."],
     ["Serotonin syndrome with selective serotonin reuptake inhibitors",
      "That is linezolid."],
     ["Chelation reducing absorption of iron supplements",
      "Chelation belongs to tetracyclines and fluoroquinolones."]],
   c=0, cite=c(85)),

 dict(topic="Nitroimidazoles", io=IO4O,
   q="What is metronidazole's mechanism of action?",
   opts=[
     ["It interacts with bacterial DNA to cause loss of helical structure and strand breakage",
      "Correct, and its activity spans Gram-positive and Gram-negative anaerobes plus parasites."],
     ["It inhibits DNA gyrase and topoisomerase IV",
      "That is the fluoroquinolone mechanism."],
     ["It binds the 50S ribosome and blocks transpeptidation",
      "That is the macrolide mechanism."],
     ["It inhibits dihydrofolate reductase",
      "That is trimethoprim."]],
   c=0, cite=c(86)),

 dict(topic="Nitroimidazoles", io=IO4O,
   q="What must a patient starting metronidazole be counselled to avoid, and why?",
   opts=[
     ["Ethanol, because of a disulfiram-like reaction",
      "Correct. This is the class's signature counselling point, alongside headache, nausea and vomiting."],
     ["Dairy products, because of chelation reducing absorption",
      "Chelation applies to tetracyclines and fluoroquinolones."],
     ["Tyramine-containing foods, because of hypertensive crisis",
      "That caution belongs to linezolid."],
     ["Sun exposure, because of photosensitivity",
      "Photosensitivity is a tetracycline and fluoroquinolone effect."]],
   c=0, cite=c(86)),

 dict(topic="Polypeptides", io=IO4M,
   q="What are the black box warnings for the polymyxins?",
   opts=[
     ["Nephrotoxicity, neurotoxicity, and neuromuscular blockade",
      "Correct. These are the only warnings the lecture labels explicitly as black box, which is why they are worth holding separately from ordinary adverse effects."],
     ["Tendon rupture, peripheral neuropathy, and central nervous system effects",
      "Those are fluoroquinolone adverse effects and are not labelled black box in this deck."],
     ["Thrombocytopenia, serotonin syndrome, and hypertensive crisis",
      "Those are linezolid concerns."],
     ["Ototoxicity, red man syndrome, and phlebitis",
      "Those are vancomycin concerns."]],
   c=0, cite=c(88)),

 dict(topic="Polypeptides", io=IO4M,
   q="What is the polymyxin mechanism of action?",
   opts=[
     ["A detergent-like interaction with the lipopolysaccharide of the Gram-negative outer membrane, displacing magnesium and calcium and disrupting the membrane",
      "Correct, which is why the spectrum is broad Gram-negative coverage — the target only exists there."],
     ["Inhibition of 1,3-beta-D-glucan synthase in the cell wall",
      "That is the echinocandin mechanism in fungi."],
     ["Binding the 30S ribosomal subunit and preventing transfer RNA binding",
      "That is the tetracycline mechanism."],
     ["Covalent inactivation of penicillin-binding proteins",
      "That is the penicillin mechanism."]],
   c=0, cite=c(87)),

 dict(topic="Polypeptides", io=IO4M,
   q="Why is polymyxin resistance uncommon, and why is use expected to increase?",
   opts=[
     ["The class went largely unused for the last 50 years, and rising multidrug resistance is bringing it back despite optimal regimens not being well studied",
      "Correct. Low historical exposure is the reason resistance never developed widely."],
     ["The mechanism is impossible for bacteria to circumvent, and new formulations have removed the toxicity",
      "Proposed resistance mechanisms are listed, and the black box toxicities remain."],
     ["It is used only topically, so systemic resistance cannot emerge",
      "Route is not the explanation offered."],
     ["It is always combined with a beta-lactamase inhibitor that prevents resistance",
      "No such combination is described."]],
   c=0, cite=c(88)),
]
