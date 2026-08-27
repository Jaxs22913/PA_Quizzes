# Pharmacology I Lecture 1 — Antifungals, pool part B
# Objectives 9a (echinocandins), 9c (azoles), 9d (allylamines), 9e (mitotic
# inhibitors), plus tolnaftate.
#
# Correct answer always written first; the partition script rotates.
# No dosage recall -- Dr. Wood does not test dosages. Duration of therapy for
# nail infections IS kept: it is counselling and prognosis, not a dose.
SRC = "Antibiotics, Antivirals, and Antifungals.pptx"
def c(n): return f"{SRC}, Slide {n}"

IO9  = "9 — Antifungal classes"
IO9A = "9a — Echinocandins"
IO9C = "9c — Azoles"
IO9D = "9d — Allylamines"
IO9E = "9e — Mitotic inhibitors"

POOL_B = [
 dict(topic="Azoles", io=IO9C,
   q="What enzyme do the imidazoles and triazoles inhibit?",
   opts=[
     ["Fungal cytochrome P450 14-alpha-demethylase, which converts lanosterol to ergosterol",
      "Correct. Because the target is a cytochrome P450 enzyme, this class interferes with human cytochrome P450 enzymes too, which is the source of its drug interactions."],
     ["Squalene epoxidase, early in the ergosterol pathway",
      "That is the allylamine target."],
     ["1,3-beta-D-glucan synthase in the cell wall",
      "That is the echinocandin target."],
     ["Thymidylate synthase, blocking DNA synthesis",
      "That is flucytosine's downstream effect."]],
   c=0, cite=c(102)),

 dict(topic="Azoles", io=IO9C,
   q="Which tinea infection affects the nails, and what is its other name?",
   opts=[
     ["Tinea unguium, also called onychomycosis",
      "Correct. Tinea pedis is athlete's foot, tinea corporis is ringworm, and tinea cruris is jock itch."],
     ["Tinea pedis, also called athlete's foot",
      "Tinea pedis affects the foot rather than the nail."],
     ["Tinea corporis, also called ringworm",
      "Tinea corporis affects the body surface."],
     ["Tinea cruris, also called jock itch",
      "Tinea cruris affects the groin."]],
   c=0, cite=c(102)),

 dict(topic="Azoles", io=IO9C,
   q="Why is ketoconazole rarely used now?",
   opts=[
     ["It does not enter the central nervous system and it inhibits cytochrome P450 3A4, producing significant drug interactions",
      "Correct, and itraconazole with its wider spectrum largely replaced it."],
     ["It is available only intravenously and causes severe infusion reactions",
      "Ketoconazole is oral, taken with meals, and also available topically."],
     ["It is the only azole ineffective against Candida",
      "Its problems are penetration and interactions rather than a Candida gap."],
     ["It causes visual disturbance in about 30 percent of patients",
      "That is voriconazole's characteristic effect."]],
   c=0, cite=c(103)),

 dict(topic="Azoles", io=IO9C,
   q="Which azole is the only one effective against the Zygomycetes such as Mucor and Rhizopus?",
   opts=[
     ["Posaconazole",
      "Correct. It is structurally related to itraconazole but more potent against 14-alpha-demethylase, and is useful in refractory fungal infection."],
     ["Fluconazole",
      "Fluconazole's strengths are central nervous system penetration and candidiasis."],
     ["Voriconazole",
      "Voriconazole's niche is systemic aspergillosis."],
     ["Ketoconazole",
      "Ketoconazole is the oldest and most limited of the group."]],
   c=0, cite=c(105)),

 dict(topic="Azoles", io=IO9C,
   q="Which azole penetrates the central nervous system and is therefore used in cryptococcal meningitis?",
   opts=[
     ["Fluconazole",
      "Correct. It also has the best oral absorption of the group and is excreted in the urine, which suits it to candidiasis."],
     ["Ketoconazole",
      "Ketoconazole explicitly does not enter the central nervous system."],
     ["Itraconazole",
      "Itraconazole's indications are blastomycosis, histoplasmosis and onychomycosis."],
     ["Caspofungin",
      "Caspofungin is an echinocandin, not an azole."]],
   c=0, cite=c(106)),

 dict(topic="Azoles", io=IO9C,
   q="Which azole replaced amphotericin B for systemic aspergillosis, and what is its characteristic adverse effect?",
   opts=[
     ["Voriconazole, with effects on vision in about 30 percent of patients",
      "Correct. It also affects liver and renal function, and its intravenous vehicle, cyclodextrin, accumulates in renal failure."],
     ["Posaconazole, with QT prolongation",
      "Posaconazole does prolong the QT interval, but the agent that displaced amphotericin B for aspergillosis is voriconazole."],
     ["Fluconazole, with hepatotoxicity",
      "Fluconazole is not the agent for systemic aspergillosis."],
     ["Itraconazole, with peripheral neuropathy",
      "Itraconazole is used in blastomycosis and histoplasmosis, and neuropathy is not its named effect."]],
   c=0, cite=c(107)),

 dict(topic="Azoles", io=IO9C,
   q="Why does voriconazole's intravenous formulation require caution in renal failure?",
   opts=[
     ["Its vehicle, cyclodextrin, accumulates when renal function is impaired",
      "Correct — the concern is the vehicle rather than the drug itself, which is an unusual reason to avoid a formulation."],
     ["The drug itself is cleared entirely by glomerular filtration and reaches toxic levels",
      "The stated problem is accumulation of the vehicle."],
     ["It crystallises in the renal tubule as acyclovir does",
      "Tubular crystallisation is an acyclovir effect."],
     ["It causes direct renal tubule damage requiring saline hydration",
      "That is amphotericin B's toxicity."]],
   c=0, cite=c(107)),

 dict(topic="Azoles", io=IO9C,
   q="Which azoles are noted as teratogenic?",
   opts=[
     ["Itraconazole, and fluconazole and voriconazole in animals",
      "Correct. Reproductive safety is a recurring caution across the azole group."],
     ["Ketoconazole and posaconazole only",
      "Teratogenicity is attributed to itraconazole, fluconazole and voriconazole in this deck."],
     ["None of the azoles carries a teratogenicity caution",
      "Several do."],
     ["Only the topical imidazole derivatives",
      "The topical agents are listed without that caution; the systemic ones carry it."]],
   c=0, cite=c(104)),

 dict(topic="Azoles", io=IO9C,
   q="Itraconazole is useful in which infections?",
   opts=[
     ["Blastomycosis, histoplasmosis, onychomycosis, and febrile neutropenic patients not responding to antibiotics",
      "Correct. It has an active metabolite and a wider spectrum than the ketoconazole it replaced."],
     ["Cryptococcal meningitis and prophylaxis in acquired immunodeficiency syndrome",
      "Those are fluconazole's indications, which follow from its central nervous system penetration."],
     ["Zygomycete infection including Mucor and Rhizopus",
      "Posaconazole is the azole named for the Zygomycetes."],
     ["Systemic aspergillosis as first-line therapy",
      "Voriconazole took that role from amphotericin B."]],
   c=0, cite=c(104)),

 dict(topic="Azoles", io=IO9C,
   q="Which of these is a topical imidazole derivative rather than a systemic azole?",
   opts=[
     ["Clotrimazole",
      "Correct. The topical group also includes econazole, miconazole, butoconazole, tioconazole, oxiconazole, sulconazole and sertaconazole."],
     ["Posaconazole",
      "Posaconazole is systemic, available intravenously and orally."],
     ["Voriconazole",
      "Voriconazole is systemic, available orally and intravenously."],
     ["Itraconazole",
      "Itraconazole is an orally active systemic agent."]],
   c=0, cite=c(108)),

 dict(topic="Echinocandins", io=IO9A,
   q="What is the echinocandin mechanism of action?",
   opts=[
     ["Inhibition of 1,3-beta-D-glucan synthase, lowering formation of 1,3-beta-D-glucan in the cell wall",
      "Correct. Caspofungin, micafungin and anidulafungin are the three agents, and the wall target is unique among the antifungals here."],
     ["Inhibition of lanosterol demethylase, reducing ergosterol in the membrane",
      "That is the azole mechanism, acting on the membrane rather than the wall."],
     ["Formation of membrane channels allowing potassium to leak from the cell",
      "That is amphotericin B."],
     ["Disruption of the mitotic spindle, halting cell division",
      "That is griseofulvin."]],
   c=0, cite=c(109)),

 dict(topic="Echinocandins", io=IO9A,
   q="Which indications does the lecture give for the echinocandins?",
   opts=[
     ["Oesophageal candidiasis, systemic aspergillosis not responding to itraconazole or amphotericin B, and febrile neutropenic patients not responding to antibiotics",
      "Correct — largely a salvage and neutropenic-fever role rather than first-line therapy."],
     ["Cryptococcal meningitis and prophylaxis in advanced human immunodeficiency virus infection",
      "Those are fluconazole indications."],
     ["Dermatophyte infection of the nails and scalp",
      "Those are treated with griseofulvin and the allylamines."],
     ["Zygomycete infection such as Mucor",
      "Posaconazole is the agent named for the Zygomycetes."]],
   c=0, cite=c(109)),

 dict(topic="Echinocandins", io=IO9A,
   q="Which adverse reactions are listed for the echinocandins?",
   opts=[
     ["Tachycardia, headache, insomnia, hypokalaemia, hypomagnesaemia and blood dyscrasias",
      "Correct. Note the electrolyte disturbances overlap with amphotericin B's, despite a completely different mechanism."],
     ["Visual disturbance and hepatic dysfunction",
      "Those belong to voriconazole."],
     ["Bone marrow suppression and hepatotoxicity as dose-limiting effects",
      "Those are flucytosine's effects."],
     ["Renal tubule damage requiring saline hydration",
      "That is amphotericin B."]],
   c=0, cite=c(109)),

 dict(topic="Griseofulvin", io=IO9E,
   q="How does griseofulvin reach the site of a dermatophyte infection?",
   opts=[
     ["It is deposited in keratin precursor cells in skin, hair and nails",
      "Correct. That is why treatment lasts as long as the keratin takes to grow out."],
     ["It is concentrated in sebum and delivered through the sebaceous glands",
      "The lecture describes deposition in keratin precursor cells."],
     ["It is actively transported across the dermis by macrophages",
      "No such mechanism is described."],
     ["It is applied topically and penetrates the nail plate directly",
      "Griseofulvin is given systemically; tolnaftate and naftifine are the topical agents."]],
   c=0, cite=c(110)),

 dict(topic="Griseofulvin", io=IO9E,
   q="How long does griseofulvin treatment take for scalp, fingernail and toenail infection?",
   opts=[
     ["About one month for the scalp, six to nine months for fingernails, and up to twelve months for toenails",
      "Correct. The gradient follows how slowly each keratin structure grows out, and it is the counselling point that keeps patients adherent."],
     ["About one week for the scalp, one month for fingernails, and three months for toenails",
      "These are far shorter than the durations given."],
     ["Three months for all three sites",
      "The durations differ markedly by site."],
     ["A single dose for the scalp, with topical therapy thereafter for nails",
      "Single-dose therapy is described for vaginal candidiasis with fluconazole, not here."]],
   c=0, cite=c(110)),

 dict(topic="Griseofulvin", io=IO9E,
   q="What should a patient be told about taking griseofulvin with food?",
   opts=[
     ["Absorption is increased by a high-fat meal, because the drug is very lipid soluble",
      "Correct, and it is effective against numerous dermatophytes but not Candida, acting fungistatically."],
     ["It must be taken on an empty stomach, since food chelates the drug",
      "Chelation with food is the tetracycline and fluoroquinolone problem."],
     ["Food has no effect on absorption",
      "A high-fat meal specifically increases absorption."],
     ["It should be taken with an antacid to reduce gastric irritation",
      "No such advice is given, and antacids interfere with other agents."]],
   c=0, cite=c(111)),

 dict(topic="Griseofulvin", io=IO9E,
   q="Which adverse effects and interactions accompany griseofulvin?",
   opts=[
     ["Headache in about 15 percent, mental confusion, fatigue and blurred vision, with induction of cytochrome P450 1A2 and 2C9",
      "Correct. Note it induces enzymes where the azoles inhibit them — opposite directions of interaction within the same broad category of drug."],
     ["Inhibition of cytochrome P450 3A4 with raised levels of co-administered substrates",
      "Griseofulvin induces rather than inhibits, which pushes substrate levels the other way."],
     ["Nephrotoxicity and electrolyte wasting",
      "Those belong to amphotericin B."],
     ["Visual disturbance in 30 percent with hepatic and renal effects",
      "That profile is voriconazole's."]],
   c=0, cite=c(111)),

 dict(topic="Allylamines", io=IO9D,
   q="Which allylamine is available both orally and topically, and which is topical only?",
   opts=[
     ["Terbinafine is oral and topical; naftifine is topical only",
      "Correct. Both inhibit squalene epoxidase and are used for superficial dermatophyte infection."],
     ["Naftifine is oral and topical; terbinafine is topical only",
      "This reverses the two agents."],
     ["Both are available only topically",
      "Terbinafine is orally active."],
     ["Both are available only orally",
      "Naftifine is a topical agent."]],
   c=0, cite=c(112)),

 dict(topic="Allylamines", io=IO9D,
   q="What is the allylamine mechanism of action?",
   opts=[
     ["Inhibition of squalene epoxidase, reducing ergosterol synthesis",
      "Correct. Same end point as the azoles, reached at an earlier step of the pathway."],
     ["Inhibition of lanosterol demethylase, reducing ergosterol synthesis",
      "That is where the azoles act."],
     ["Binding ergosterol already present and forming membrane channels",
      "That is the polyene mechanism."],
     ["Inhibition of glucan synthesis in the cell wall",
      "That is the echinocandin mechanism."]],
   c=0, cite=c(112)),

 dict(topic="Tolnaftate", io=IO9,
   q="What distinguishes tolnaftate's spectrum from the other topical antifungals?",
   opts=[
     ["It is effective against tinea pedis, tinea cruris and tinea corporis, but not tinea unguium",
      "Correct. It works by distorting hyphae and stunting mycelial growth, and is topical only."],
     ["It is effective against tinea unguium but not the other tineas",
      "The nail infection is precisely the one it does not treat."],
     ["It covers Candida but no dermatophytes",
      "Its activity is against cutaneous mycoses, and Candida is not its target."],
     ["It covers systemic mycoses when given orally",
      "It is available topically only."]],
   c=0, cite=c(113)),
]
