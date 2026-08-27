# Pharmacology I Lecture 1 — Antifungals, pool part A
# Objective 9 (a-e) plus the fungal biology and mechanism-overview slides the
# class distinctions rest on. Polyenes, flucytosine, and the shared framework.
#
# Correct answer always written first; the partition script rotates.
# No dosage recall anywhere in this pool -- Dr. Wood does not test dosages.
SRC = "Antibiotics, Antivirals, and Antifungals.pptx"
def c(n): return f"{SRC}, Slide {n}"

IO9  = "9 — Antifungal classes"
IO9B = "9b — Polyenes"
IO2  = "2 — Common modes of action of antimicrobial agents"

POOL_A = [
 dict(topic="Fungal biology", io=IO2,
   q="Which features of fungal cells explain why antibacterial antibiotics do not treat them?",
   opts=[
     ["They are eukaryotic, with a rigid cell wall containing chitin, a cell membrane built on ergosterol, different ribosomes and a distinct nuclear membrane",
      "Correct. Every antifungal class in this lecture exploits one of these differences, which is also why selectivity is harder than with bacteria."],
     ["They are prokaryotic, with a peptidoglycan cell wall and a 70S ribosome that antibacterial agents cannot reach",
      "Fungi are eukaryotic; peptidoglycan and the 70S ribosome are bacterial features."],
     ["They lack a cell wall entirely and rely on a cholesterol membrane, so cell wall agents have no target",
      "Fungi do have a cell wall, of chitin, and the membrane sterol is ergosterol rather than cholesterol."],
     ["They replicate only inside host cells, so extracellular antibiotics never reach them",
      "Obligate intracellular replication describes viruses, not fungi."]],
   c=0, cite=c(90)),

 dict(topic="Fungal biology", io=IO2,
   q="Which sterol in the fungal cell membrane is the target of several antifungal classes?",
   opts=[
     ["Ergosterol",
      "Correct. Polyenes bind it, azoles and allylamines block its synthesis at different steps."],
     ["Cholesterol",
      "Cholesterol is the mammalian membrane sterol; targeting it would remove any selectivity."],
     ["Lanosterol",
      "Lanosterol is the precursor that azoles block the demethylation of, not the finished membrane sterol."],
     ["Squalene",
      "Squalene is further upstream, and is where the allylamines act via squalene epoxidase."]],
   c=0, cite=c(90)),

 dict(topic="Fungal biology", io=IO9,
   q="Which predisposing factors for fungal infection does the lecture list?",
   opts=[
     ["Loss of barriers, immunodeficiency, metabolic abnormalities, suppression of competing organisms, and a warm moist environment",
      "Correct. Note that antibiotic use appears here as suppression of competing organisms — treating a bacterial infection can create a fungal one."],
     ["Advanced age, malnutrition, smoking, alcohol use, and occupational exposure",
      "Those are general risk factors but not the five the lecture gives."],
     ["Recent travel, animal contact, contaminated water, insect bites, and crowding",
      "Those describe exposure routes for other infections rather than fungal predisposition."],
     ["Genetic polymorphisms, vaccination status, blood group, sex, and geography",
      "None of these appears on the predisposing factors slide."]],
   c=0, cite=c(91)),

 dict(topic="Fungal biology", io=IO9,
   q="A patient develops oral candidiasis after a course of broad-spectrum antibiotics. Which predisposing factor does this illustrate?",
   opts=[
     ["Suppression of competing organisms",
      "Correct. Removing the bacterial flora leaves the niche open, which is why antibiotic exposure is itself a fungal risk factor."],
     ["Loss of barriers",
      "Loss of barriers refers to burns, surgery and catheters breaching a physical boundary."],
     ["Metabolic abnormality",
      "That category is illustrated by diabetes rather than by antibiotic exposure."],
     ["Warm moist environment",
      "That category covers diaper rash and athlete's foot."]],
   c=0, cite=c(91)),

 dict(topic="Fungal biology", io=IO9,
   q="How does the lecture classify mycoses by the depth of tissue involved?",
   opts=[
     ["Systemic affecting internal organs, subcutaneous affecting skin layers, and superficial affecting hair, nails and mucous membranes",
      "Correct. Aspergillus and Cryptococcus sit in the systemic group; Epidermophyton, Microsporum and Trichophyton in the superficial."],
     ["Acute, subacute and chronic, according to the duration of infection",
      "That is a chronicity scheme rather than the anatomical one the lecture uses."],
     ["Primary, opportunistic and reactivated, according to host immune status",
      "Immune status appears among predisposing factors, not as the classification of mycoses."],
     ["Endemic, sporadic and epidemic, according to geographic distribution",
      "The lecture classifies by tissue depth, not by epidemiology."]],
   c=0, cite=c(92)),

 dict(topic="Mechanisms", io=IO2,
   q="Which antifungal classes act on the cell membrane, and which acts on the cell wall?",
   opts=[
     ["Membrane — polyenes, azoles and allylamines; cell wall — echinocandins",
      "Correct. That single split is the most efficient way to hold the whole class list, since griseofulvin and flucytosine sit outside both."],
     ["Membrane — echinocandins; cell wall — polyenes, azoles and allylamines",
      "This reverses the two groups."],
     ["Membrane — polyenes and echinocandins; cell wall — azoles and allylamines",
      "Azoles and allylamines both act on ergosterol, which is a membrane target."],
     ["All four classes act on the cell wall, differing only in which enzyme they inhibit",
      "Only the echinocandins target the wall."]],
   c=0, cite=c(94)),

 dict(topic="Mechanisms", io=IO2,
   q="Azoles and allylamines both reduce ergosterol. At which enzyme does each act?",
   opts=[
     ["Azoles inhibit lanosterol demethylase; allylamines inhibit squalene epoxidase",
      "Correct. Same pathway, different steps — which is why both end in decreased ergosterol."],
     ["Azoles inhibit squalene epoxidase; allylamines inhibit lanosterol demethylase",
      "This swaps the two enzymes."],
     ["Azoles inhibit 1,3-beta-D-glucan synthase; allylamines inhibit lanosterol demethylase",
      "Glucan synthase is the echinocandin target and sits in the cell wall, not the ergosterol pathway."],
     ["Both inhibit lanosterol demethylase, differing only in binding site",
      "They act at genuinely different enzymes in the pathway."]],
   c=0, cite=c(94)),

 dict(topic="Mechanisms", io=IO2,
   q="Which antifungal works by inhibiting microtubules and so stopping cell division?",
   opts=[
     ["Griseofulvin",
      "Correct, which is why it is the agent the syllabus calls a mitotic inhibitor."],
     ["Flucytosine",
      "Flucytosine acts on nucleic acid synthesis through thymidylate synthase."],
     ["Caspofungin",
      "Caspofungin is an echinocandin acting on the cell wall."],
     ["Terbinafine",
      "Terbinafine is an allylamine acting on squalene epoxidase."]],
   c=0, cite=c(95)),

 dict(topic="Polyenes", io=IO9B,
   q="What is amphotericin B's mechanism of action?",
   opts=[
     ["It forms channels in ergosterol-containing membranes that let potassium and magnesium leak out, and causes oxidative damage to the membrane",
      "Correct. The drug is derived from a soil Streptomycetaceae, and the leak is why electrolyte disturbance is such a prominent toxicity."],
     ["It inhibits lanosterol demethylase, reducing ergosterol synthesis",
      "That is the azole mechanism; amphotericin B binds ergosterol already present."],
     ["It inhibits 1,3-beta-D-glucan synthase, weakening the cell wall",
      "That is the echinocandin mechanism."],
     ["It is converted to a fluorinated nucleotide that blocks thymidylate synthase",
      "That describes flucytosine."]],
   c=0, cite=c(96)),

 dict(topic="Polyenes", io=IO9B,
   q="What advantage do the lipid formulations of amphotericin B offer, and at what cost?",
   opts=[
     ["Reduced toxicity, at 20 to 50 times the cost of the deoxycholate formulation",
      "Correct. The three named lipid products are the lipid complex, the colloidal suspension and the liposomal form."],
     ["Improved oral bioavailability, at a modest increase in cost",
      "Amphotericin B is given by intravenous infusion regardless of formulation."],
     ["A broader spectrum covering the Zygomycetes, at greater renal risk",
      "Broader Zygomycetes coverage is the property attributed to posaconazole among the azoles."],
     ["A shorter infusion time, at the expense of efficacy",
      "The infusion is given over four hours; formulation changes toxicity rather than duration."]],
   c=0, cite=c(97)),

 dict(topic="Polyenes", io=IO9B,
   q="Why are fever and chills expected during an amphotericin B infusion, and how are they managed?",
   opts=[
     ["They are driven by interleukin-1 and tumour necrosis factor, and patients are pretreated with acetaminophen, antihistamines and corticosteroids",
      "Correct. The reaction is a cytokine response rather than an allergy, which is why premedication works."],
     ["They reflect an immunoglobulin E mediated allergic reaction, and the drug must be stopped permanently",
      "The mechanism given is cytokine-mediated, and the reaction is managed by premedication rather than by discontinuation."],
     ["They are caused by rapid fungal lysis releasing endotoxin, and are prevented by slowing the infusion alone",
      "Endotoxin release is not the mechanism described, and premedication is the stated management."],
     ["They are a disulfiram-like reaction to the infusion vehicle, and are avoided by withholding alcohol",
      "The disulfiram-like reaction belongs to metronidazole."]],
   c=0, cite=c(98)),

 dict(topic="Polyenes", io=IO9B,
   q="Which electrolyte and renal effects accompany amphotericin B?",
   opts=[
     ["Hypokalaemia and hypomagnesaemia, hypotension, uraemia in about 80 percent with decreased filtration, and renal tubule damage mitigated by hydration with normal saline",
      "Correct. The saline hydration is the practical countermeasure worth remembering."],
     ["Hyperkalaemia and hypercalcaemia with a rising glomerular filtration rate",
      "The disturbances run in the opposite direction, and filtration falls rather than rises."],
     ["Isolated hepatotoxicity with no renal involvement",
      "Renal effects are the prominent ones for this agent."],
     ["Bone marrow suppression as the dose-limiting toxicity",
      "Bone marrow suppression is the flucytosine concern."]],
   c=0, cite=c(99)),

 dict(topic="Polyenes", io=IO9B,
   q="Why does nystatin have limited systemic side effects?",
   opts=[
     ["It is poorly absorbed, so it is used topically and orally for candidiasis with little systemic exposure",
      "Correct. Poor absorption is the reason it is safe locally and useless systemically."],
     ["It is rapidly metabolized by hepatic cytochrome P450 before reaching the circulation",
      "Poor absorption rather than first-pass metabolism is the explanation given."],
     ["It binds cholesterol rather than ergosterol, so human cells are unaffected",
      "Nystatin is a polyene acting on ergosterol like amphotericin B."],
     ["It is given only as a single intravenous dose",
      "It is available as oral preparations and a topical powder."]],
   c=0, cite=c(99)),

 dict(topic="Flucytosine", io=IO9,
   q="How does flucytosine achieve selectivity for fungal cells?",
   opts=[
     ["It is converted to 5-fluorouridine by cytosine deaminase, an enzyme human cells lack, and then inhibits thymidylate synthase",
      "Correct. The missing human enzyme is the whole basis of selectivity."],
     ["It binds ergosterol, which human membranes do not contain",
      "That selectivity argument belongs to the polyenes."],
     ["It inhibits a fungal cytochrome P450 enzyme with no human counterpart",
      "That is closer to the azole mechanism, and human cytochrome P450 enzymes do exist, which is why azoles interact with other drugs."],
     ["It is actively pumped into fungal cells by a transporter absent from human cells",
      "The lecture attributes selectivity to the converting enzyme, not to a transporter."]],
   c=0, cite=c(100)),

 dict(topic="Flucytosine", io=IO9,
   q="With which agents is flucytosine combined, and for what?",
   opts=[
     ["With amphotericin B in cryptococcal meningitis, and with itraconazole in chromoblastomycosis",
      "Correct. It is used in combination rather than alone, and its own indications are Cryptococcus neoformans and Candida."],
     ["With caspofungin in oesophageal candidiasis, and with terbinafine in onychomycosis",
      "Neither pairing appears in the lecture."],
     ["With griseofulvin in tinea capitis, and with nystatin in oral candidiasis",
      "Those are dermatophyte and topical indications unrelated to flucytosine."],
     ["With voriconazole in invasive aspergillosis, and with fluconazole in vaginal candidiasis",
      "The stated combinations are with amphotericin B and with itraconazole."]],
   c=0, cite=c(100)),

 dict(topic="Flucytosine", io=IO9,
   q="Which adverse effects limit flucytosine?",
   opts=[
     ["Bone marrow suppression, hepatotoxicity, gastrointestinal disturbance and rash",
      "Correct, and it is available orally only."],
     ["Nephrotoxicity and electrolyte wasting requiring saline hydration",
      "Those belong to amphotericin B."],
     ["Visual disturbance in about 30 percent of patients",
      "That is the voriconazole effect."],
     ["Tendon rupture and peripheral neuropathy",
      "Those are fluoroquinolone effects and are not antifungal concerns."]],
   c=0, cite=c(101)),

 dict(topic="Anthelmintics", io=IO9,
   q="What is the mechanism of the benzimidazoles albendazole and mebendazole?",
   opts=[
     ["They inhibit formation of helminth microtubules and block glucose uptake, leading to parasite death",
      "Correct. Note this content is taught in the deck but sits outside the syllabus objectives, which name only antibacterials, antivirals and antifungals."],
     ["They release acetylcholine and inhibit cholinesterase, acting as a depolarizing neuromuscular blocker",
      "That is pyrantel pamoate's mechanism."],
     ["They inhibit ergosterol synthesis in the helminth membrane",
      "Ergosterol is a fungal target; helminths are not addressed that way here."],
     ["They interact with parasite DNA to cause strand breakage",
      "That describes metronidazole's action."]],
   c=0, cite=c(115)),

 dict(topic="Anthelmintics", io=IO9,
   q="How does pyrantel pamoate kill its target parasites?",
   opts=[
     ["It releases acetylcholine and inhibits cholinesterase, acting as a depolarizing neuromuscular blocker that causes paralysis and death",
      "Correct, and it is used for pinworm and hookworm."],
     ["It inhibits formation of helminth microtubules and blocks glucose uptake",
      "That is the benzimidazole mechanism."],
     ["It inhibits squalene epoxidase, depleting the parasite membrane of ergosterol",
      "That is an antifungal mechanism and does not apply."],
     ["It blocks neuraminidase and prevents the parasite from leaving host cells",
      "Neuraminidase inhibition is oseltamivir's antiviral mechanism."]],
   c=0, cite=c(116)),
]
