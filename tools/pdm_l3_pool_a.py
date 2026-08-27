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
      "Dermoscopy is not presented as the routine diagnostic route in this lecture."]],
   c=0, cite=c(3)),

 dict(topic="Diagnostic approach", io=IOA, slot="first-line",
   q="What should every diagnostic test you order do?",
   opts=[
     ["Answer a specific clinical question",
      "Correct — the deck states this as the governing principle for test selection."],
     ["Narrow the differential to a single diagnosis",
      "Few single tests do this, and it is not the stated principle."],
     ["Establish a baseline for future comparison",
      "Useful sometimes, but not the principle the lecture states."],
     ["Exclude the most dangerous diagnosis first",
      "A reasonable clinical habit, but not what this slide says."]],
   c=0, cite=c(4)),

 dict(topic="Diagnostic approach", io=IOA, slot="first-line",
   q="Which four factors govern test selection?",
   opts=[
     ["Cost, availability, invasiveness and diagnostic yield",
      "Correct — the four listed test-selection principles."],
     ["Cost, turnaround time, invasiveness and patient preference",
      "Turnaround time and preference are not on the list."],
     ["Sensitivity, specificity, prevalence and pretest probability",
      "These are the Lecture 1 concepts, not this slide's four factors."],
     ["Cost, radiation dose, availability and reimbursement",
      "Radiation dose and reimbursement are not among the four."]],
   c=0, cite=c(4)),

 dict(topic="Diagnostic approach", io=IOA, slot="first-line",
   q="A patient has a lesion you suspect is a neoplasm, or a rash that has not resolved. Which test does the deck's decision list point to?",
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
   q="Which question does point-of-care ultrasound answer in the deck's decision list?",
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
   q="Which three tests does the deck group together as bedside testing?",
   opts=[
     ["Potassium hydroxide preparation, Tzanck smear and Gram stain",
      "Correct — the three bedside tests on the slide."],
     ["Potassium hydroxide preparation, Wood lamp and Gram stain",
      "The Wood lamp is not on this slide's bedside list."],
     ["Tzanck smear, Gram stain and skin culture",
      "Culture is sent to the laboratory rather than performed at the bedside."],
     ["Potassium hydroxide preparation, Tzanck smear and dermoscopy",
      "Dermoscopy is not one of the three named."]],
   c=0, cite=c(5)),

 dict(topic="Bedside testing", io=IOA, slot="first-line",
   q="What are the stated benefits of bedside testing?",
   opts=[
     ["Quick, inexpensive, and both sensitive and specific",
      "Correct — all three benefits as the slide lists them."],
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
      "Correct — both are limits the slide names explicitly."],
     ["Cost and turnaround time",
      "Bedside testing is listed as quick and inexpensive."],
     ["Poor sensitivity and poor specificity",
      "The slide states these tests are both sensitive and specific."],
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
      "The last three are not fungal indications on this slide."]],
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
      "Correct — the deck attaches that description to tinea versicolor."],
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
      "The slide defines the negative result by absent fungal elements."],
     ["Budding yeast without pseudohyphae",
      "Yeast forms are a positive finding, not a negative one."],
     ["Clear fields with no epithelial cells present",
      "Epithelial cells are expected on the slide; it is fungal elements that must be absent."]],
   c=0, cite=c(6)),

 dict(topic="Potassium hydroxide", io=IOC, slot="avoid",
   q="What does the sensitivity of a potassium hydroxide preparation depend on?",
   opts=[
     ["Adequate scraping technique",
      "Correct — the stated limitation of the test."],
     ["The concentration of potassium hydroxide used",
      "Concentration is specified in the procedure but is not the stated limitation."],
     ["How long the slide is left before reading",
      "Not the limitation this slide names."],
     ["Whether the patient has used a topical antifungal",
      "Plausible clinically, but not what the slide states."]],
   c=0, cite=c(6)),

 dict(topic="Potassium hydroxide", io=IOC, slot="avoid",
   q="What error does the deck warn about when a fungal infection is diagnosed clinically alone?",
   opts=[
     ["Fungal infections can be misidentified",
      "Correct — the slide's stated reason for confirming with microscopy."],
     ["Treatment is delayed while the culture is awaited",
      "Delay is a limitation of culture, not of clinical-only diagnosis."],
     ["The wrong antifungal class is chosen",
      "The slide does not make this claim."],
     ["Resistance develops to topical antifungals",
      "Resistance is not raised on this slide."]],
   c=0, cite=c(6)),

 dict(topic="Potassium hydroxide", io=IOC, slot="initial test",
   q="What concentration of potassium hydroxide does the deck's procedure specify?",
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
