#!/usr/bin/env python3
"""Add the three Pharmacology I Lecture 1 Arcade decks to arcade.js.

One deck per topic, matching the topic split used for the quizzes:
antibacterials, antivirals, antifungals.

Content follows the Arcade policy rather than the quiz schema. `cards` feed
Study, Learn and Sprint, so each tests ONE atomic fact in a single clause of
roughly 10 to 20 words -- a compound answer joined by "and" gets split into two
cards, because Sprint reads them under an eight-second clock. `matchCards` feed
Match, which is pure recognition, so the term is a name and the definition is a
compressed identity tag rather than an explanation.

No dosages anywhere, per Dr. Wood. No bare abbreviations either -- the standing
rule is to write the full term, or ABBREVIATION (full term) on first use.
"""
import json, os, re

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"

ICON_ABX = '<path d="M4 12a8 8 0 0 1 16 0"/><path d="M8 12v6M16 12v6"/><circle cx="12" cy="8" r="2"/>'
ICON_AVR = '<path d="M12 3v18M3 12h18"/><circle cx="12" cy="12" r="5"/>'
ICON_AFG = '<path d="M12 21v-7"/><path d="M5 11a7 7 0 0 1 14 0z"/>'

DECKS = [
 dict(id="pharm-antibacterials", name="Antibacterials", color="accent2", icon=ICON_ABX, cards=[
  ["What does the beta-lactam ring mimic?", "Two D-alanine residues on the peptidoglycan peptide."],
  ["What happens to the penicillin-binding protein once penicillin binds it?", "It is covalently inactivated at its active site."],
  ["With most penicillin-binding proteins inactive, what can the cell still do?", "Synthesize peptidoglycan chains, but form no new cross-links."],
  ["How does vancomycin block cell wall cross-linking?", "It binds the two terminal D-alanine residues, covering the substrate."],
  ["What single change confers vancomycin resistance?", "D-lactate replaces the terminal D-alanine, so vancomycin no longer binds."],
  ["What is the mechanism of penicillin resistance?", "Beta-lactamase cleaves the beta-lactam ring."],
  ["What defines a beta-lactamase inhibitor?", "No antibacterial activity of its own; it irreversibly inactivates the enzyme."],
  ["What does adding a beta-lactamase inhibitor buy in coverage?", "Bacteroides and methicillin-susceptible Staphylococcus aureus."],
  ["What is the cephalosporin generation rule?", "More Gram-negative activity, less Gram-positive, as generations advance."],
  ["What is the exception to the cephalosporin generation rule?", "The fourth generation gains Gram-negative without sacrificing Gram-positive."],
  ["Which cephalosporin covers methicillin-resistant Staphylococcus aureus?", "Ceftaroline, a fifth generation agent."],
  ["What is the approximate penicillin cross-sensitivity rate with cephalosporins?", "Under one percent."],
  ["What is aztreonam's defining clinical advantage?", "No cross-reactivity with other beta-lactams, so it is usable in true penicillin allergy."],
  ["Which carbapenem lacks Pseudomonas coverage?", "Ertapenem."],
  ["Which carbapenem is specifically watched for seizures?", "Imipenem."],
  ["Which antibacterial cannot be used in pneumonia?", "Daptomycin."],
  ["Which ribosomal subunit do macrolides bind?", "The 50S subunit, blocking transpeptidation."],
  ["Which ribosomal subunit do tetracyclines bind?", "The 30S subunit, preventing transfer RNA from occupying the A site."],
  ["What is the bacterial ribosome, against the mammalian one?", "Bacterial 70S versus mammalian 80S."],
  ["What is clindamycin's notable coverage gap?", "Gram-negative aerobes."],
  ["Why did aminoglycoside dosing move to once daily?", "A post-antibiotic effect plus concentration-dependent killing."],
  ["Which two toxicities define the aminoglycosides?", "Nephrotoxicity and ototoxicity."],
  ["Which fluoroquinolone must not be used for urinary tract infection?", "Moxifloxacin."],
  ["What is the fluoroquinolone dual mechanism?", "Inhibition of DNA gyrase and of topoisomerase IV."],
  ["Which musculoskeletal injury do fluoroquinolones cause?", "Tendonitis and Achilles tendon rupture."],
  ["Which class carries this lecture's only explicit black box warnings?", "The polymyxins."],
  ["What are the polymyxin black box warnings?", "Nephrotoxicity, neurotoxicity and neuromuscular blockade."],
  ["What must a patient on metronidazole avoid?", "Ethanol, because of a disulfiram-like reaction."],
  ["What does linezolid risk when combined with a serotonergic drug?", "Serotonin syndrome."],
  ["What distinguishes bacteriostatic from bactericidal?", "Bacteriostatic inhibits growth; bactericidal disrupts function enough to kill."],
  ["What governs killing for a time-dependent agent?", "Time above the minimal inhibitory concentration, targeting 40 to 70 percent of the interval."],
  ["When is a vancomycin trough drawn?", "Fifteen to thirty minutes before the next scheduled dose."],
 ], matchCards=[
  ["Penicillins", "Beta-lactam, inactivates penicillin-binding proteins"],
  ["Vancomycin", "Glycopeptide, binds D-alanine, Gram-positive only"],
  ["Aztreonam", "Monobactam, Gram-negative only, no beta-lactam cross-reactivity"],
  ["Carbapenems", "Very broad, for resistant Gram-negatives"],
  ["Macrolides", "50S binder, covers atypicals"],
  ["Tetracyclines", "30S binder, bacteriostatic, chelates cations"],
  ["Aminoglycosides", "Gram-negative, nephrotoxic and ototoxic"],
  ["Fluoroquinolones", "Inhibit DNA gyrase and topoisomerase IV"],
  ["Clindamycin", "Lincosamide, anaerobes, no Gram-negative aerobes"],
  ["Linezolid", "Oxazolidinone, for resistant Gram-positives"],
  ["Metronidazole", "Nitroimidazole, anaerobes and parasites"],
  ["Polymyxins", "Polypeptide, detergent-like, black box warnings"],
  ["Daptomycin", "Lipopeptide, depolarizes, never for pneumonia"],
 ]),

 dict(id="pharm-antivirals", name="Antivirals", color="accent3", icon=ICON_AVR, cards=[
  ["How is acyclovir selectively activated?", "Viral thymidine kinase phosphorylates it, so only infected cells activate it."],
  ["Why does acyclovir terminate the viral DNA chain?", "It is a guanine analog lacking the sugar moiety, so elongation cannot continue."],
  ["Which viruses do acyclovir and valacyclovir treat?", "Herpes simplex and varicella-zoster."],
  ["Which virus needs ganciclovir rather than acyclovir?", "Cytomegalovirus."],
  ["Why does valacyclovir absorb better than acyclovir?", "It is a prodrug, converted after absorption."],
  ["What is acyclovir's characteristic renal effect?", "It crystallises in the renal tubule, so hydration must be maintained."],
  ["Which central nervous system effects does acyclovir cause?", "Seizures, delirium and tremor."],
  ["What does acyclovir achieve if started within 24 hours of chickenpox?", "It shortens the acute illness but does not cure the infection."],
  ["Which haematologic effects limit ganciclovir?", "Neutropenia and thrombocytopenia."],
  ["What proportion must stop intravenous ganciclovir for side effects?", "About a third of patients."],
  ["What is oseltamivir's mechanism?", "It inhibits neuraminidase, so budding progeny cannot be cleaved free."],
  ["Within what window must oseltamivir be started?", "Within 48 hours of symptom onset."],
  ["Which viruses does oseltamivir target?", "Influenza A and influenza B."],
  ["Which sites does herpes simplex type 1 affect?", "Mouth, face, skin, esophagus or brain."],
  ["Which sites does herpes simplex type 2 affect?", "Genitals, rectum, hands or meninges."],
  ["What does varicella-zoster virus cause?", "Chickenpox and shingles."],
  ["Which manifestations does cytomegalovirus cause?", "Retinitis, esophagitis and colitis."],
  ["Which four antivirals here are prodrugs?", "Valacyclovir, famciclovir, valganciclovir and oseltamivir."],
  ["Which of penciclovir and famciclovir is the oral prodrug?", "Famciclovir."],
  ["Which antiviral approach does oseltamivir represent?", "Inhibiting viral release."],
  ["Which antiviral approach does the acyclovir family represent?", "Inhibiting nucleic acid synthesis."],
 ], matchCards=[
  ["Acyclovir", "Guanine analog for herpes simplex and varicella-zoster"],
  ["Valacyclovir", "Prodrug of acyclovir, better absorbed"],
  ["Famciclovir", "Oral prodrug of penciclovir"],
  ["Ganciclovir", "Guanine analog for cytomegalovirus"],
  ["Valganciclovir", "Better-absorbed oral prodrug of ganciclovir"],
  ["Oseltamivir", "Neuraminidase inhibitor for influenza"],
  ["Viral thymidine kinase", "Enzyme that activates acyclovir"],
  ["Neuraminidase", "Frees budding progeny from the host cell"],
  ["Herpes simplex type 1", "Mouth, face, skin, esophagus, brain"],
  ["Herpes simplex type 2", "Genitals, rectum, hands, meninges"],
  ["Varicella-zoster", "Chickenpox and shingles"],
  ["Cytomegalovirus", "Retinitis, esophagitis, colitis"],
 ]),

 dict(id="pharm-antifungals", name="Antifungals", color="accent4", icon=ICON_AFG, cards=[
  ["Which sterol does the fungal cell membrane use?", "Ergosterol."],
  ["What is the fungal cell wall made of?", "Chitin and glucans, with no peptidoglycan."],
  ["Which antifungal class targets the cell wall?", "The echinocandins."],
  ["What enzyme do echinocandins inhibit?", "1,3-beta-D-glucan synthase."],
  ["Why is glucan synthase the cleanest antifungal target?", "Mammalian cells have no cell wall at all."],
  ["How do the polyenes work?", "They bind ergosterol already present and form channels through the membrane."],
  ["What leaks out once a polyene opens a membrane channel?", "Potassium and magnesium."],
  ["What enzyme do the azoles inhibit?", "Lanosterol demethylase, a fungal cytochrome P450 enzyme."],
  ["What enzyme do the allylamines inhibit?", "Squalene epoxidase."],
  ["Why do azoles interact with so many other drugs?", "Their target is a cytochrome P450 enzyme, and they inhibit human ones too."],
  ["Which azole penetrates the central nervous system?", "Fluconazole, used in cryptococcal meningitis."],
  ["Which azole treats systemic aspergillosis?", "Voriconazole."],
  ["What is voriconazole's characteristic adverse effect?", "Visual disturbance, in about thirty percent of patients."],
  ["Which azole is the only one effective against the Zygomycetes?", "Posaconazole."],
  ["Why is ketoconazole rarely used?", "It does not enter the central nervous system and strongly inhibits cytochrome P450 3A4."],
  ["Which electrolyte disturbances does amphotericin B cause?", "Hypokalaemia and hypomagnesaemia."],
  ["How is amphotericin B renal injury mitigated?", "Hydration with normal saline."],
  ["Why do lipid formulations of amphotericin B exist?", "Reduced toxicity, at twenty to fifty times the cost."],
  ["Why does nystatin have few systemic effects?", "It is poorly absorbed, so it is used topically and orally."],
  ["How does griseofulvin work?", "It interrupts mitotic spindles, halting cell division in dermatophytes."],
  ["Where is griseofulvin deposited?", "In keratin precursor cells of skin, hair and nails."],
  ["Which organism does griseofulvin fail to cover?", "Candida."],
  ["What increases griseofulvin absorption?", "A high-fat meal."],
  ["Why is flucytosine selective for fungal cells?", "Cytosine deaminase converts it, and human cells lack that enzyme."],
  ["Which adverse effect limits flucytosine?", "Bone marrow suppression."],
  ["What is tinea unguium also called?", "Onychomycosis, affecting the nails."],
  ["What is tinea corporis commonly called?", "Ringworm."],
  ["What is tinea cruris commonly called?", "Jock itch."],
  ["What is tinea pedis commonly called?", "Athlete's foot."],
  ["Which predisposing factor does antibiotic use represent?", "Suppression of competing organisms."],
 ], matchCards=[
  ["Ergosterol", "The fungal membrane sterol"],
  ["Chitin", "A fungal cell wall component"],
  ["Echinocandins", "Inhibit 1,3-beta-D-glucan synthase"],
  ["Polyenes", "Bind ergosterol and form membrane channels"],
  ["Azoles", "Inhibit lanosterol demethylase"],
  ["Allylamines", "Inhibit squalene epoxidase"],
  ["Griseofulvin", "Mitotic inhibitor for dermatophytes"],
  ["Flucytosine", "Converted by cytosine deaminase, blocks thymidylate synthase"],
  ["Amphotericin B", "Polyene, nephrotoxic, electrolyte wasting"],
  ["Fluconazole", "Azole entering the central nervous system"],
  ["Voriconazole", "Azole for systemic aspergillosis"],
  ["Posaconazole", "The only azole for Zygomycetes"],
  ["Tinea unguium", "Onychomycosis of the nails"],
 ]),
]


def js_deck(d):
    def pairs(rows):
        return "\n".join('      [%s, %s],' % (json.dumps(a, ensure_ascii=False),
                                              json.dumps(b, ensure_ascii=False)) for a, b in rows)
    return ('  { id: %s, name: %s, color: %s,\n'
            '    icon: \'%s\',\n'
            '    cards: [\n%s\n    ],\n'
            '    matchCards: [\n%s\n    ] },\n') % (
        json.dumps(d["id"]), json.dumps(d["name"]), json.dumps(d["color"]),
        d["icon"], pairs(d["cards"]), pairs(d["matchCards"]))


s = open(ARCADE, encoding="utf-8").read()
assert "pharm-antibacterials" not in s, "decks already present"

# validate against the Arcade content policy before writing anything
for d in DECKS:
    assert 8 <= len(d["cards"]), "%s: Sprint races 8 cards, needs at least 8" % d["id"]
    assert 10 <= len(d["matchCards"]) <= 14, "%s: matchCards outside the 10-13 target" % d["id"]
    for front, back in d["cards"]:
        assert len(back.split()) <= 26, "%s: card back too long for Sprint -> %s" % (d["id"], back)
    for term, definition in d["matchCards"]:
        assert len(definition.split()) <= 9, "%s: match definition too long -> %s" % (d["id"], definition)
    ids = [c[0] for c in d["cards"]]
    assert len(ids) == len(set(ids)), "%s: duplicate card front" % d["id"]

# splice the decks in before the DEMO_DECKS closing bracket
m = re.search(r"\n\];\n", s[s.index("var DEMO_DECKS"):])
end = s.index("var DEMO_DECKS") + m.start() + 1
s = s[:end] + "".join(js_deck(d) for d in DECKS) + s[end:]

# register the class, ordered as semesters.js lists Fall 2026 (pharm-1 after microbiology)
ANCHOR = '''  { id: "clin-path-1", name: "Clinical Pathophysiology I", exams: ['''
NEW = '''  { id: "pharm-1", name: "Pharmacology I", exams: [
    { id: "exam1", name: "Exam 1", deckIds: ["pharm-antibacterials", "pharm-antivirals", "pharm-antifungals"] }
  ]},

'''
assert s.count(ANCHOR) == 1
s = s.replace(ANCHOR, NEW + ANCHOR)

open(ARCADE, "w", encoding="utf-8").write(s)
print("added %d decks (%d cards, %d match pairs)" % (
    len(DECKS), sum(len(d["cards"]) for d in DECKS), sum(len(d["matchCards"]) for d in DECKS)))
for d in DECKS:
    print("   %-22s %2d cards  %2d match" % (d["id"], len(d["cards"]), len(d["matchCards"])))
