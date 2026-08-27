# Pharmacology I Lecture 1 — Antifungals, pool part D
# Final depth pass so the partition has real headroom to optimise against
# rather than being forced to take every question written.
SRC = "Antibiotics, Antivirals, and Antifungals.pptx"
def c(n): return f"{SRC}, Slide {n}"

IO9  = "9 — Antifungal classes"
IO9A = "9a — Echinocandins"
IO9B = "9b — Polyenes"
IO9C = "9c — Azoles"
IO9D = "9d — Allylamines"
IO9E = "9e — Mitotic inhibitors"
IO2  = "2 — Common modes of action of antimicrobial agents"

POOL_D = [
 dict(topic="Azoles", io=IO9C,
   q="Which tinea infection is commonly called ringworm?",
   opts=[
     ["Tinea corporis",
      "Correct. Despite the name there is no worm involved; it describes the annular appearance on the body surface."],
     ["Tinea pedis",
      "Tinea pedis is athlete's foot."],
     ["Tinea cruris",
      "Tinea cruris is jock itch, affecting the groin."],
     ["Tinea unguium",
      "Tinea unguium is onychomycosis, affecting the nails."]],
   c=0, cite=c(102)),

 dict(topic="Azoles", io=IO9C,
   q="Which tinea infection is commonly called jock itch?",
   opts=[
     ["Tinea cruris",
      "Correct, affecting the groin. The azoles are indicated across this whole tinea group."],
     ["Tinea corporis",
      "Tinea corporis is ringworm of the body."],
     ["Tinea pedis",
      "Tinea pedis is athlete's foot."],
     ["Tinea unguium",
      "Tinea unguium affects the nails."]],
   c=0, cite=c(102)),

 dict(topic="Polyenes", io=IO9B,
   q="Which amphotericin B formulation is the conventional, non-lipid one?",
   opts=[
     ["Amphotericin B deoxycholate, marketed as Fungizone",
      "Correct. The three lipid alternatives are the lipid complex, the colloidal suspension and the liposomal form."],
     ["Amphotericin B lipid complex, marketed as Abelcet",
      "That is one of the lipid formulations developed to reduce toxicity."],
     ["Liposomal amphotericin B, marketed as AmBisome",
      "That is the liposomal lipid formulation."],
     ["Amphotericin B colloidal suspension, marketed as Amphotec",
      "That is the colloidal lipid formulation."]],
   c=0, cite=c(97)),

 dict(topic="Polyenes", io=IO9B,
   q="Over what period is amphotericin B infused?",
   opts=[
     ["Four hours",
      "Correct, and its side effects are what limit treatment rather than any lack of efficacy."],
     ["Thirty minutes",
      "That is the infusion time given for several antibacterial agents, not for amphotericin B."],
     ["Sixty to ninety minutes",
      "That is levofloxacin's infusion time."],
     ["Given as a rapid intravenous push",
      "A rapid push would worsen the infusion reaction this drug is known for."]],
   c=0, cite=c(98)),

 dict(topic="Fungal biology", io=IO2,
   q="Why does the fungal cell wall present a target that the bacterial cell wall does not?",
   opts=[
     ["It contains chitin and glucans rather than peptidoglycan, so agents such as the echinocandins are needed",
      "Correct. Beta-lactams and vancomycin act on peptidoglycan, which fungi do not have — which is why antibacterials are useless against them."],
     ["It contains peptidoglycan in a thicker layer, so higher beta-lactam doses are required",
      "Fungi have no peptidoglycan at all."],
     ["It contains ergosterol, which the echinocandins bind",
      "Ergosterol is in the membrane, and it is bound by the polyenes."],
     ["It has no wall, so only membrane-active agents work",
      "Fungi do have a rigid cell wall."]],
   c=0, cite=c(90)),

 dict(topic="Azoles", io=IO9C,
   q="Which route and administration advice is given for ketoconazole?",
   opts=[
     ["Oral, taken with meals, and also available topically",
      "Correct, though it is rarely used now because it does not enter the central nervous system and inhibits cytochrome P450 3A4."],
     ["Intravenous only, infused over four hours",
      "That describes amphotericin B."],
     ["Topical only, as a cream or powder",
      "Ketoconazole is available topically but is also an oral agent."],
     ["Oral only, and specifically on an empty stomach",
      "It is taken with meals."]],
   c=0, cite=c(103)),

 dict(topic="Echinocandins", io=IO9A,
   q="An immunocompromised patient has systemic aspergillosis that has not responded to itraconazole or amphotericin B. Which class does the lecture position for this?",
   opts=[
     ["Echinocandins",
      "Correct — their listed role is largely salvage, in refractory aspergillosis, oesophageal candidiasis, and febrile neutropenia not responding to antibiotics."],
     ["Polyenes",
      "Amphotericin B is a polyene, and the question specifies it has already failed."],
     ["Allylamines",
      "Allylamines treat superficial dermatophyte infection, not systemic aspergillosis."],
     ["Mitotic inhibitors",
      "Griseofulvin treats dermatophytes and does not cover Aspergillus."]],
   c=0, cite=c(109)),

 dict(topic="Mechanisms", io=IO2,
   q="Griseofulvin and flucytosine sit outside the membrane-and-wall scheme. What does each target?",
   opts=[
     ["Griseofulvin targets cell division through microtubules; flucytosine targets nucleic acid synthesis",
      "Correct. Holding those two aside makes the remaining four classes easy to sort by membrane versus wall."],
     ["Griseofulvin targets nucleic acid synthesis; flucytosine targets cell division",
      "This swaps the two."],
     ["Both target nucleic acid synthesis at different steps",
      "Only flucytosine does."],
     ["Both target the mitotic spindle",
      "Only griseofulvin does."]],
   c=0, cite=c(95)),

 dict(topic="Allylamines", io=IO9D,
   q="What kind of infection are the allylamines used for?",
   opts=[
     ["Superficial dermatophyte infections",
      "Correct. Naftifine is topical and terbinafine is available orally and topically."],
     ["Systemic mycoses of the internal organs",
      "Those require amphotericin B, the systemic azoles, or the echinocandins."],
     ["Cryptococcal meningitis",
      "Fluconazole and amphotericin B with flucytosine are the agents for that."],
     ["Helminth infection",
      "Those are treated by the benzimidazoles and pyrantel pamoate."]],
   c=0, cite=c(112)),

 dict(topic="Polyenes", io=IO9B,
   q="Which polyene is used specifically for oral candidiasis?",
   opts=[
     ["Nystatin",
      "Correct, available as oral preparations and a topical powder, with systemic effects limited by poor absorption."],
     ["Amphotericin B deoxycholate",
      "That is the systemic intravenous agent."],
     ["Natamycin",
      "Natamycin is named among the polyenes but the oral candidiasis agent specified is nystatin."],
     ["Caspofungin",
      "Caspofungin is an echinocandin used for oesophageal candidiasis intravenously."]],
   c=0, cite=c(99)),

 dict(topic="Griseofulvin", io=IO9E,
   q="From which organism is griseofulvin derived?",
   opts=[
     ["Penicillium griseofulvum",
      "Correct — a mould product, like several of the antibacterials in this lecture."],
     ["Streptomycetaceae in soil",
      "That is amphotericin B's source."],
     ["Bacillus polymyxa",
      "That produces the polymyxins."],
     ["Streptomyces griseus",
      "That organism is associated with streptomycin, an antibacterial."]],
   c=0, cite=c(110)),

 dict(topic="Fungal biology", io=IO9,
   q="A patient develops athlete's foot after prolonged use of occlusive footwear. Which predisposing factor is this?",
   opts=[
     ["A warm moist environment",
      "Correct — the lecture's own examples for that category are diaper rash and athlete's foot."],
     ["Loss of barriers",
      "That covers burns, surgery and catheters breaching a physical boundary."],
     ["Immunodeficiency",
      "That covers cancer, human immunodeficiency virus infection, transplant and chemotherapy."],
     ["Metabolic abnormality",
      "That category is illustrated by diabetes."]],
   c=0, cite=c(91)),
]
