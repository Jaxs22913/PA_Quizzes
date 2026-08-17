# Pharmacology I Lecture 1 — Antifungals, pool part C
# Depth pass: the mycoses by tissue depth, amphotericin B indications, and the
# cross-class comparisons that separate agents sharing a target.
#
# Correct answer always written first; the partition script rotates.
# No dosage recall -- Dr. Wood does not test dosages.
SRC = "Antibiotics, Antivirals, and Antifungals.pptx"
def c(n): return f"{SRC}, Slide {n}"

IO9  = "Objective 9 — Antifungal classes"
IO9A = "Objective 9a — Echinocandins"
IO9B = "Objective 9b — Polyenes"
IO9C = "Objective 9c — Azoles"
IO9D = "Objective 9d — Allylamines"
IO9E = "Objective 9e — Mitotic inhibitors"
IO2  = "Objective 2 — Common modes of action of antimicrobial agents"

POOL_C = [
 dict(topic="Fungal biology", io=IO9,
   q="Which organisms does the lecture list as causes of systemic mycoses affecting internal organs?",
   opts=[
     ["Aspergillus, Blastomyces, Candida, Coccidioides, Cryptococcus, Histoplasma and Zygomycetes",
      "Correct. These are the organisms the systemic antifungals target, which is why amphotericin B's indication list closely mirrors this one."],
     ["Epidermophyton, Microsporum and Trichophyton",
      "Those three cause superficial mycoses of hair, nails and mucous membranes."],
     ["Chromomycosis, Pseudallescheriasis and Sporotrichosis",
      "Those are the subcutaneous mycoses affecting skin layers."],
     ["Mucor, Rhizopus and Pneumocystis only",
      "Mucor and Rhizopus are Zygomycetes within the systemic group, but the list is considerably broader."]],
   c=0, cite=c(92)),

 dict(topic="Fungal biology", io=IO9,
   q="Which organisms cause the superficial mycoses of hair, nails and mucous membranes?",
   opts=[
     ["Epidermophyton, Microsporum and Trichophyton",
      "Correct. These are the dermatophytes that griseofulvin and the allylamines treat."],
     ["Aspergillus, Cryptococcus and Histoplasma",
      "Those cause systemic mycoses of internal organs."],
     ["Chromomycosis, Pseudallescheriasis and Sporotrichosis",
      "Those are subcutaneous, affecting the skin layers rather than hair and nails."],
     ["Candida, Coccidioides and Blastomyces",
      "Those appear in the systemic group."]],
   c=0, cite=c(92)),

 dict(topic="Fungal biology", io=IO9,
   q="Which mycoses does the lecture place in the subcutaneous category?",
   opts=[
     ["Chromomycosis, Pseudallescheriasis and Sporotrichosis",
      "Correct — the middle tier, affecting skin layers rather than the surface or the internal organs."],
     ["Tinea pedis, tinea cruris and tinea corporis",
      "Those are superficial dermatophyte infections."],
     ["Aspergillosis, cryptococcosis and histoplasmosis",
      "Those are systemic."],
     ["Oral and vaginal candidiasis",
      "Those are surface infections of mucous membranes."]],
   c=0, cite=c(92)),

 dict(topic="Polyenes", io=IO9B,
   q="Which organisms is amphotericin B indicated against?",
   opts=[
     ["Cryptococcus, Blastomyces, Histoplasma, Candida, Coccidioides and Aspergillus, the last reserved for invasive infection",
      "Correct. Its breadth is why it remained the reference agent until voriconazole displaced it for aspergillosis."],
     ["Dermatophytes of the skin, hair and nails only",
      "Those are treated by griseofulvin and the allylamines; amphotericin B is a systemic agent."],
     ["Helminths including hookworm and pinworm",
      "Those are the anthelmintic targets."],
     ["Influenza A and B",
      "That is oseltamivir's target and is viral rather than fungal."]],
   c=0, cite=c(98)),

 dict(topic="Polyenes", io=IO9B,
   q="From what source is amphotericin B derived?",
   opts=[
     ["A soil Streptomycetaceae organism",
      "Correct, which places it alongside several antibacterials in being a natural product of a soil microbe."],
     ["Penicillium griseofulvum",
      "That is the source of griseofulvin."],
     ["Bacillus polymyxa",
      "That is the source of the polymyxins, which are antibacterial."],
     ["Amycolatopsis orientalis",
      "That organism produces vancomycin."]],
   c=0, cite=c(96)),

 dict(topic="Mechanisms", io=IO2,
   q="Two antifungal classes lower ergosterol and one binds it directly. Which is which?",
   opts=[
     ["Azoles and allylamines lower synthesis; polyenes bind ergosterol already in the membrane",
      "Correct. The distinction matters because binding existing sterol acts immediately, while blocking synthesis depends on turnover."],
     ["Polyenes and azoles lower synthesis; allylamines bind ergosterol already present",
      "Allylamines act on squalene epoxidase, which is a synthesis step."],
     ["Echinocandins and polyenes lower synthesis; azoles bind ergosterol",
      "Echinocandins act on the cell wall, not on ergosterol at all."],
     ["All three lower synthesis; none binds ergosterol directly",
      "Amphotericin B and nystatin bind ergosterol directly to form channels."]],
   c=0, cite=c(94)),

 dict(topic="Mechanisms", io=IO2,
   q="Which antifungal acts on nucleic acid synthesis rather than on the membrane or wall?",
   opts=[
     ["Flucytosine, through conversion to a fluorinated nucleotide that inhibits thymidylate synthase",
      "Correct. It and griseofulvin are the two agents outside the membrane-and-wall scheme."],
     ["Caspofungin, by inhibiting glucan synthesis",
      "Caspofungin is a cell wall agent."],
     ["Terbinafine, by inhibiting squalene epoxidase",
      "Terbinafine acts on the ergosterol pathway."],
     ["Nystatin, by forming membrane channels",
      "Nystatin is a polyene acting on the membrane."]],
   c=0, cite=c(95)),

 dict(topic="Azoles", io=IO9C,
   q="Which azole has the best oral absorption, and how is it eliminated?",
   opts=[
     ["Fluconazole, excreted in the urine",
      "Correct, and its urinary excretion is part of why a single dose treats vaginal candidiasis."],
     ["Ketoconazole, excreted in the bile",
      "Ketoconazole must be taken with meals and is the most limited of the group."],
     ["Itraconazole, excreted unchanged in the faeces",
      "Itraconazole is orally active with an active metabolite, but fluconazole is the one noted for best absorption."],
     ["Posaconazole, excreted by the lungs",
      "No such elimination route is described."]],
   c=0, cite=c(106)),

 dict(topic="Azoles", io=IO9C,
   q="Which azole is described as structurally related to itraconazole but more potent against 14-alpha-demethylase?",
   opts=[
     ["Posaconazole",
      "Correct, and that potency underlies its effectiveness in refractory infection and against the Zygomycetes."],
     ["Voriconazole",
      "Voriconazole is described as a fluconazole derivative."],
     ["Fluconazole",
      "Fluconazole is the parent of voriconazole rather than a relative of itraconazole."],
     ["Ketoconazole",
      "Ketoconazole is the older agent that itraconazole replaced."]],
   c=0, cite=c(105)),

 dict(topic="Azoles", io=IO9C,
   q="Voriconazole is derived from which other azole?",
   opts=[
     ["Fluconazole",
      "Correct — a fluconazole derivative introduced in 2002, which then took over systemic aspergillosis from amphotericin B."],
     ["Itraconazole",
      "Posaconazole, not voriconazole, is the agent related to itraconazole."],
     ["Ketoconazole",
      "Ketoconazole is the oldest of the group and is not voriconazole's parent."],
     ["Clotrimazole",
      "Clotrimazole is a topical imidazole derivative."]],
   c=0, cite=c(107)),

 dict(topic="Azoles", io=IO9C,
   q="Which adverse effects are listed for posaconazole?",
   opts=[
     ["QT prolongation, fever, diarrhoea, hypokalaemia, hypomagnesaemia and thrombocytopenia",
      "Correct. The QT effect places it alongside the macrolides and fluoroquinolones as a drug to watch in combination."],
     ["Visual disturbance in about 30 percent of patients",
      "That is voriconazole's characteristic effect."],
     ["Headache in about 15 percent with mental confusion and blurred vision",
      "That profile belongs to griseofulvin."],
     ["Bone marrow suppression and hepatotoxicity",
      "Those are flucytosine's effects."]],
   c=0, cite=c(105)),

 dict(topic="Azoles", io=IO9C,
   q="Why do the azoles interact with so many other drugs?",
   opts=[
     ["Their target is a fungal cytochrome P450 enzyme, and they inhibit human cytochrome P450 enzymes such as 3A4 as well",
      "Correct. Ketoconazole, itraconazole and fluconazole are all named as cytochrome P450 3A4 inhibitors."],
     ["They induce cytochrome P450 1A2 and 2C9, accelerating clearance of co-administered drugs",
      "That is griseofulvin, and it induces rather than inhibits."],
     ["They chelate divalent cations in the gut and block absorption",
      "Chelation is the tetracycline and fluoroquinolone interaction."],
     ["They displace other drugs from plasma protein binding",
      "Protein displacement is not the mechanism given."]],
   c=0, cite=c(103)),

 dict(topic="Azoles", io=IO9C,
   q="Which enzymes does voriconazole interact with?",
   opts=[
     ["Cytochrome P450 2C19, 2C9 and 3A4",
      "Correct — a broader set than the other azoles, which is part of why it needs care in combination."],
     ["Cytochrome P450 1A2 and 2C9 only, by induction",
      "Induction of those two is griseofulvin's interaction."],
     ["Cytochrome P450 3A4 only",
      "Ketoconazole is the agent named for 3A4 alone."],
     ["No cytochrome P450 enzymes; it is renally cleared unchanged",
      "Voriconazole interacts with several cytochrome P450 enzymes."]],
   c=0, cite=c(107)),

 dict(topic="Echinocandins", io=IO9A,
   q="Which three agents make up the echinocandin class?",
   opts=[
     ["Caspofungin, micafungin and anidulafungin",
      "Correct. All three inhibit 1,3-beta-D-glucan synthase in the cell wall."],
     ["Amphotericin B, nystatin and natamycin",
      "Those are the polyenes."],
     ["Naftifine, terbinafine and tolnaftate",
      "Naftifine and terbinafine are allylamines; tolnaftate acts differently again."],
     ["Fluconazole, voriconazole and posaconazole",
      "Those are triazoles."]],
   c=0, cite=c(109)),

 dict(topic="Polyenes", io=IO9B,
   q="Which three polyene agents does the lecture name?",
   opts=[
     ["Amphotericin B, nystatin and natamycin",
      "Correct. Amphotericin B is the systemic agent; nystatin is used topically and orally because it is poorly absorbed."],
     ["Caspofungin, micafungin and anidulafungin",
      "Those are echinocandins."],
     ["Ketoconazole, miconazole and clotrimazole",
      "Those are imidazoles."],
     ["Griseofulvin, terbinafine and naftifine",
      "Griseofulvin is a mitotic inhibitor and the other two are allylamines."]],
   c=0, cite=c(93)),

 dict(topic="Griseofulvin", io=IO9E,
   q="Which organism does griseofulvin fail to cover, and what is the nature of its action?",
   opts=[
     ["It is not effective against Candida, and it is fungistatic rather than fungicidal",
      "Correct. It is effective against numerous dermatophytes, which is a different target population entirely."],
     ["It is not effective against dermatophytes, and it is fungicidal",
      "Dermatophytes are precisely what it treats."],
     ["It is not effective against Aspergillus, and it is fungicidal against Candida",
      "Its gap is Candida, and its action is fungistatic."],
     ["It covers all fungi but only when given topically",
      "It is a systemic agent with a defined gap."]],
   c=0, cite=c(111)),

 dict(topic="Allylamines", io=IO9D,
   q="How long does terbinafine treatment take for fingernail and toenail infection?",
   opts=[
     ["Six to twelve weeks for fingernails and up to twelve months for toenails",
      "Correct. As with griseofulvin, the duration follows nail growth, which is the counselling point that keeps patients on therapy."],
     ["One week for fingernails and one month for toenails",
      "Those durations are far shorter than the lecture gives."],
     ["Six to nine months for fingernails and up to twelve months for toenails",
      "Those are griseofulvin's figures; terbinafine clears fingernails faster."],
     ["A single dose for both sites",
      "Single-dose therapy is described for vaginal candidiasis with fluconazole."]],
   c=0, cite=c(112)),

 dict(topic="Fungal biology", io=IO9,
   q="A patient with poorly controlled diabetes develops a fungal infection. Which predisposing category does this represent?",
   opts=[
     ["Metabolic abnormality",
      "Correct — diabetes is the lecture's own example for that category."],
     ["Immunodeficiency",
      "That category is illustrated by cancer, human immunodeficiency virus infection, organ transplant and chemotherapy."],
     ["Loss of barriers",
      "That covers burns, surgery and catheters."],
     ["Suppression of competing organisms",
      "That refers to antibiotic exposure clearing the bacterial flora."]],
   c=0, cite=c(91)),

 dict(topic="Mechanisms", io=IO2,
   q="Which antifungal target exists in the fungal cell wall and has no mammalian counterpart?",
   opts=[
     ["1,3-beta-D-glucan, whose synthase the echinocandins inhibit",
      "Correct. Mammalian cells have no cell wall at all, which makes this the cleanest selective target among the antifungals."],
     ["Ergosterol, which the polyenes bind",
      "Ergosterol sits in the membrane, and mammalian membranes contain the related sterol cholesterol."],
     ["Lanosterol demethylase, which the azoles inhibit",
      "That is a cytochrome P450 enzyme with human counterparts, which is exactly why azoles cause interactions."],
     ["Microtubules, which griseofulvin disrupts",
      "Mammalian cells have microtubules too."]],
   c=0, cite=c(94)),

 dict(topic="Flucytosine", io=IO9,
   q="Which organisms is flucytosine indicated against?",
   opts=[
     ["Cryptococcus neoformans and Candida",
      "Correct, and it is given in combination rather than alone because resistance develops readily."],
     ["Dermatophytes of the nails and scalp",
      "Those are treated by griseofulvin and the allylamines."],
     ["Aspergillus and the Zygomycetes",
      "Those require voriconazole and posaconazole respectively."],
     ["Helminths including roundworm and whipworm",
      "Those are anthelmintic targets."]],
   c=0, cite=c(100)),
]
