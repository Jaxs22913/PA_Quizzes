# -*- coding: utf-8 -*-
# Principles of Diagnostic Medicine I, Lecture 3
# (Diagnostic Testing for Dermatologic, Ophthalmologic, and ENT Disorders) -- pool A.
# Test-selection principles, bedside microscopy and potassium hydroxide preparations.
# Syllabus objectives a and c.
#
# PROFESSOR REYNOLDS' RULES, carried from her Lecture 1 recording and asserted in
# the partition script:
#   - A number never appears without the scale that makes it readable.
#   - "We're not gonna do math." No question asks the student to calculate.
#
# THIS IS THE STUDENT VERSION OF THE DECK and its licensed figures have been
# stripped: slides 7, 21, 23, 28-30, 33 and 38 have titles and speaker notes but
# no picture at all. Where the notes describe the missing figure -- the optic
# disc cupping figure on 23 and the facial fracture figure on 38 are both
# described in full -- that description is the source and is cited as notes.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "3. svDerm, ENT, Ophtho.pptx"
def c(n): return f"{SRC}, Slide {n}"
def cn(n): return f"{SRC}, Slide {n} (speaker notes)"

IOA = "a — Discuss indications, advantages, and limitations of common diagnostic tests used in dermatologic disorders"
IOC = "c — Interpret potassium hydroxide (KOH) preparations"

POOL_A = [
 dict(topic="Diagnostic approach", io=IOA, slot="first-line",
   q="How is most skin disease diagnosed?",
   opts=[
     ["By history and visual inspection, with office testing added for uncertain diagnoses",
      "Correct — testing supplements the clinical examination rather than replacing it."],
     ["By skin biopsy, with history and inspection used to choose the biopsy site",
      "Biopsy is reserved for specific indications, not routine diagnosis."],
     ["By culture, with history and inspection used to choose the transport medium",
      "Culture is indicated for purulent lesions, not for skin disease generally."],
     ["By dermoscopy, with history and inspection used to confirm the reading",
      "Dermoscopy refines the assessment of pigmented lesions rather than serving as the routine diagnostic route, which remains history and inspection."]],
   c=0, cite=c(3)),

 dict(topic="Diagnostic approach", io=IOA, slot="first-line",
   q="What should every diagnostic test you order do?",
   opts=[
     ["Answer a specific clinical question",
      "Correct — a test that cannot change what you do next adds cost and delay, so the question it answers must be identified before it is ordered."],
     ["Narrow the differential to a single diagnosis",
      "Few single tests do this, and it is not the stated principle."],
     ["Establish a baseline for future comparison",
      "Baseline documentation is occasionally useful, but a test ordered without a specific question to answer adds cost without changing management."],
     ["Exclude the most dangerous diagnosis first",
      "Excluding the dangerous diagnosis is often the specific question, but the governing principle is that every test must answer one."]],
   c=0, cite=c(4)),

 dict(topic="Diagnostic approach", io=IOA, slot="first-line",
   q="Which four factors govern test selection?",
   opts=[
     ["Cost, availability, invasiveness and diagnostic yield",
      "Correct — the four listed test-selection principles."],
     ["Cost, turnaround time, invasiveness and patient preference",
      "Turnaround time and preference are not on the list."],
     ["Sensitivity, specificity, prevalence and pretest probability",
      "Those describe how a test performs statistically; the selection factors here are cost, availability, invasiveness and diagnostic yield."],
     ["Cost, radiation dose, availability and reimbursement",
      "Radiation dose and reimbursement are not among the four."]],
   c=0, cite=c(4)),

 dict(topic="Diagnostic approach", io=IOA, slot="first-line",
   q="A patient has a lesion you suspect is a neoplasm, or a rash that has not resolved. Which test is indicated?",
   opts=[
     ["Biopsy",
      "Correct — neoplasm or a persistent rash routes to biopsy."],
     ["Potassium hydroxide preparation or culture",
      "That branch is for a suspected infection."],
     ["Point-of-care ultrasound",
      "That branch is for distinguishing abscess from cellulitis."],
     ["Gram stain of a surface swab",
      "A surface swab does not answer the neoplasm question."]],
   c=0, cite=c(4)),

 dict(topic="Diagnostic approach", io=IOA, slot="first-line",
   q="Which question does point-of-care ultrasound answer?",
   opts=[
     ["Abscess versus cellulitis",
      "Correct — that is the question the list assigns to point-of-care ultrasound."],
     ["Infection versus inflammation",
      "That is not the question assigned to ultrasound here."],
     ["Neoplasm versus persistent rash",
      "That branch routes to biopsy."],
     ["Dermatophyte versus yeast",
      "That is answered by potassium hydroxide microscopy."]],
   c=0, cite=c(4)),

 dict(topic="Bedside testing", io=IOA, slot="first-line",
   q="Which three tests are grouped together as bedside testing?",
   opts=[
     ["Potassium hydroxide preparation, Tzanck smear and Gram stain",
      "Correct — all three are performed and read in the room within minutes, giving an immediate answer about fungus, virus or bacteria."],
     ["Potassium hydroxide preparation, Wood lamp and Gram stain",
      "The Wood lamp is an examination aid rather than one of the three bedside tests, which are the potassium hydroxide preparation, Tzanck smear and Gram stain."],
     ["Tzanck smear, Gram stain and skin culture",
      "Culture is sent to the laboratory rather than performed at the bedside."],
     ["Potassium hydroxide preparation, Tzanck smear and dermoscopy",
      "Dermoscopy is not one of the three named."]],
   c=0, cite=c(5)),

 dict(topic="Bedside testing", io=IOA, slot="first-line",
   q="What are the stated benefits of bedside testing?",
   opts=[
     ["Quick, inexpensive, and both sensitive and specific",
      "Correct — the result arrives within minutes at negligible cost, and when performed properly these tests both detect the organism reliably and distinguish it from alternatives."],
     ["Quick, inexpensive, and reproducible between operators",
      "Operator skill is listed as a LIMITATION, not a benefit."],
     ["Sensitive, specific, and independent of sampling technique",
      "Sampling technique is a stated limitation."],
     ["Inexpensive, widely available, and interpretable without a microscope",
      "Two of the three bedside tests require a microscope."]],
   c=0, cite=c(5)),

 dict(topic="Bedside testing", io=IOA, slot="avoid",
   q="What are the two stated limitations of bedside testing?",
   opts=[
     ["Operator skill and sampling technique",
      "Correct — both tests depend entirely on the clinician: a poorly taken sample misses the organism, and an inexperienced reader misses it under the microscope."],
     ["Cost and turnaround time",
      "Bedside testing is listed as quick and inexpensive."],
     ["Poor sensitivity and poor specificity",
      "These tests are described as both sensitive and specific; what limits them is the operator's skill and the quality of the sample taken."],
     ["Availability and the need for special transport media",
      "Neither is given as a limitation of bedside testing."]],
   c=0, cite=c(5)),

 dict(topic="Potassium hydroxide", io=IOC, slot="initial test",
   q="What is the purpose of a potassium hydroxide preparation?",
   opts=[
     ["Direct microscopy for dermatophytes, covering Candida and tinea",
      "Correct — direct visualisation of fungal elements."],
     ["Culture of dermatophytes on a selective medium",
      "Potassium hydroxide microscopy is a direct-visualisation test, not a culture."],
     ["Detection of viral cytopathic change in fresh vesicle fluid",
      "That is the Tzanck smear."],
     ["Detection of bacteria and their Gram reaction in pus",
      "That is the Gram stain."]],
   c=0, cite=c(6)),

 dict(topic="Potassium hydroxide", io=IOC, slot="initial test",
   q="Which four conditions are listed as indications for potassium hydroxide testing?",
   opts=[
     ["Tinea corporis, pedis or cruris; onychomycosis; cutaneous candidiasis; intertrigo",
      "Correct — the four indications as listed."],
     ["Tinea corporis, herpes zoster, cutaneous candidiasis and bullous impetigo",
      "Herpes zoster and impetigo are not fungal and are not on the list."],
     ["Onychomycosis, intertrigo, scabies and pediculosis",
      "Scabies and pediculosis are infestations and are not on this list."],
     ["Tinea versicolor, seborrheic dermatitis, psoriasis and eczema",
      "Only tinea versicolor is fungal here; seborrhoeic dermatitis, psoriasis and eczema are inflammatory conditions that a potassium hydroxide preparation cannot diagnose."]],
   c=0, cite=c(6)),

 dict(topic="Potassium hydroxide", io=IOC, slot="test finding",
   q="A potassium hydroxide preparation shows branching, septate hyphae. What does this indicate?",
   opts=[
     ["A dermatophyte",
      "Correct — branching septate hyphae are the dermatophyte finding."],
     ["Candida",
      "Candida shows pseudohyphae together with budding yeast."],
     ["Tinea versicolor",
      "Tinea versicolor gives the short hyphae and spores described as spaghetti and meatballs."],
     ["A negative result",
      "A negative preparation shows no fungal elements at all."]],
   c=0, cite=c(6)),

 dict(topic="Potassium hydroxide", io=IOC, slot="test finding",
   q="Which potassium hydroxide finding indicates Candida?",
   opts=[
     ["Pseudohyphae together with budding yeast",
      "Correct — the combination is what identifies Candida."],
     ["Branching, septate hyphae",
      "That finding indicates a dermatophyte."],
     ["Short hyphae mixed with clusters of spores",
      "That is the spaghetti-and-meatballs pattern of tinea versicolor."],
     ["Multinucleated giant cells",
      "That is a Tzanck smear finding, not a potassium hydroxide one."]],
   c=0, cite=c(6)),

 dict(topic="Potassium hydroxide", io=IOC, slot="test finding",
   q="Which organism does the potassium hydroxide appearance described as spaghetti and meatballs indicate?",
   opts=[
     ["Tinea versicolor",
      "Correct — Malassezia produces both short curved hyphae and clusters of round yeast cells together, giving the mixed appearance that the description captures."],
     ["Candida",
      "Candida is pseudohyphae with budding yeast."],
     ["A dermatophyte causing tinea corporis",
      "Dermatophytes show branching septate hyphae."],
     ["Herpes simplex virus",
      "Herpes simplex is not seen on a potassium hydroxide preparation."]],
   c=0, cite=c(6)),

 dict(topic="Potassium hydroxide", io=IOC, slot="test finding",
   q="What does a normal or negative potassium hydroxide preparation show?",
   opts=[
     ["No fungal elements seen",
      "Correct — the negative result is simply the absence of fungal elements."],
     ["Epithelial cells without inflammatory cells",
      "Epithelial cells are expected in any adequate scraping; what makes the result negative is the absence of fungal elements among them."],
     ["Budding yeast without pseudohyphae",
      "Yeast forms are a positive finding, not a negative one."],
     ["Clear fields with no epithelial cells present",
      "Epithelial cells should be present, confirming the scraping was adequate; their absence means the sample was inadequate rather than the result negative."]],
   c=0, cite=c(6)),

 dict(topic="Potassium hydroxide", io=IOC, slot="avoid",
   q="What does the sensitivity of a potassium hydroxide preparation depend on?",
   opts=[
     ["Adequate scraping technique",
      "Correct — the stated limitation of the test."],
     ["The concentration of potassium hydroxide used",
      "Concentration is specified in the procedure but is not the stated limitation."],
     ["How long the slide is left before reading",
      "Timing affects how well the keratin clears, but the stated limitation is whether the scraping collected enough infected scale."],
     ["Whether the patient has used a topical antifungal",
      "Recent topical antifungal use does lower the yield clinically, but the limitation named here is the adequacy of the scraping."]],
   c=0, cite=c(6)),

 dict(topic="Potassium hydroxide", io=IOC, slot="avoid",
   q="What error is warned about when a fungal infection is diagnosed clinically alone?",
   opts=[
     ["Fungal infections can be misidentified",
      "Correct — psoriasis, eczema and other scaly eruptions closely resemble tinea, so treating on appearance alone risks weeks of antifungal therapy for an inflammatory condition."],
     ["Treatment is delayed while the culture is awaited",
      "Delay is a limitation of culture, not of clinical-only diagnosis."],
     ["The wrong antifungal class is chosen",
      "The error is diagnosing fungus where there is none, rather than picking the wrong antifungal for a confirmed infection."],
     ["Resistance develops to topical antifungals",
      "Resistance is not the concern; the risk is that a non-fungal eruption such as psoriasis or eczema is mistaken for tinea."]],
   c=0, cite=c(6)),

 dict(topic="Potassium hydroxide", io=IOC, slot="initial test",
   q="What concentration of potassium hydroxide is specified?",
   opts=[
     ["Twenty per cent",
      "Correct — one drop of twenty per cent potassium hydroxide is added to the specimen."],
     ["Ten per cent",
      "Ten per cent is a common alternative but is not the concentration in this procedure."],
     ["Five per cent",
      "Not the concentration given."],
     ["Forty per cent",
      "Not the concentration given."]],
   c=0, cite=c(8)),

 dict(topic="Potassium hydroxide", io=IOC, slot="initial test",
   q="Which two microscope objectives does the potassium hydroxide procedure require?",
   opts=[
     ["Ten times and forty times",
      "Correct — a low-power ten-times survey, then forty times for anything suspicious."],
     ["Four times and ten times",
      "The procedure names ten and forty, not four."],
     ["Forty times and one hundred times under oil",
      "Oil immersion is not part of this procedure."],
     ["Ten times and one hundred times",
      "The high-dry objective specified is forty times."]],
   c=0, cite=c(8)),

 dict(topic="Potassium hydroxide", io=IOC, slot="initial test",
   q="During the potassium hydroxide procedure, how are the epithelial cells made visible?",
   opts=[
     ["Reduce the illumination by lowering the condenser",
      "Correct — the step specified for the low-power examination."],
     ["Increase the illumination and open the iris diaphragm fully",
      "The procedure calls for reducing illumination, not increasing it."],
     ["Add a drop of methylene blue to the preparation",
      "No counterstain is used in this procedure."],
     ["Warm the slide gently over a flame before reading",
      "Warming is not one of the steps given."]],
   c=0, cite=c(8)),

 dict(topic="Potassium hydroxide", io=IOC, slot="initial test",
   q="How is the specimen for a potassium hydroxide preparation obtained, and what removes the excess solution?",
   opts=[
     ["A skin scraping taken with a small scalpel blade, with excess blotted using gauze",
      "Correct — both details come from the equipment and procedure lists."],
     ["A skin scraping taken with a small scalpel blade, with excess drawn off using filter paper",
      "The equipment list specifies gauze."],
     ["A swab rolled across the lesion, with excess blotted using gauze",
      "A swab is not the collection method for this preparation."],
     ["A punch biopsy of the lesion edge, with excess blotted using gauze",
      "A punch biopsy is a different test entirely."]],
   c=0, cite=c(8)),

 dict(topic="Potassium hydroxide", io=IOC, slot="initial test",
   q="Why is the cover glass pressed gently onto the potassium hydroxide slide?",
   opts=[
     ["To get rid of any air bubbles",
      "Correct — the stated reason in the procedure."],
     ["To crush the keratin so fungal elements are released",
      "The potassium hydroxide dissolves keratin; pressing is for air bubbles."],
     ["To spread the specimen into a monolayer",
      "Not the reason given."],
     ["To seal the preparation so it does not dry out",
      "Not the reason given."]],
   c=0, cite=c(8)),
]
