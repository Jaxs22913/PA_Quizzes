# Pharmacology I Lecture 1 — Antivirals, pool part B
# Cross-comparison and application questions. The antiviral section is only
# eleven slides covering three drug groups, so this pool is deliberately
# smaller than the antibacterial and antifungal ones -- see the note in
# pharm_l1_avr_partition.py about set size.
SRC = "Antibiotics, Antivirals, and Antifungals.pptx"
def c(n): return f"{SRC}, Slide {n}"

IO5 = "5 — Antiviral classes"
IO6 = "6 — Anti-herpes agents"
IO7 = "7 — Anti-cytomegalovirus agents"
IO8 = "8 — Anti-influenza agents"

POOL_B = [
 dict(topic="Comparisons", io=IO5,
   q="A transplant recipient develops cytomegalovirus retinitis. Why is acyclovir not the answer?",
   opts=[
     ["Acyclovir's indications are herpes simplex and varicella-zoster; cytomegalovirus requires ganciclovir or valganciclovir",
      "Correct. All are guanine analogues, but the indications are drawn along virus lines rather than by drug family."],
     ["Acyclovir is only available intravenously and cannot be given to transplant recipients",
      "Acyclovir is available orally, and transplant status is not a contraindication to it."],
     ["Acyclovir causes neutropenia in a third of patients",
      "That poor tolerability belongs to intravenous ganciclovir."],
     ["Acyclovir has no antiviral activity at all in immunocompromised patients",
      "It retains activity; it simply does not cover cytomegalovirus."]],
   c=0, cite=c(125)),

 dict(topic="Comparisons", io=IO5,
   q="A patient presents on day 4 of an influenza-like illness. What does the lecture imply about oseltamivir?",
   opts=[
     ["The 48-hour window for starting treatment has passed",
      "Correct. Because the drug blocks release of new virus rather than clearing existing virus, starting late has little to act on."],
     ["Treatment should be started at a doubled dose to compensate",
      "No dose escalation strategy is described, and dosing is not tested."],
     ["Treatment is equally effective at any point in the illness",
      "The lecture is explicit that it must be started as soon as possible."],
     ["Acyclovir should be substituted",
      "Acyclovir has no activity against influenza."]],
   c=0, cite=c(126)),

 dict(topic="Comparisons", io=IO5,
   q="Three prodrug and parent pairs appear in the antiviral section. Which pairing is correct?",
   opts=[
     ["Valacyclovir with acyclovir, famciclovir with penciclovir, and valganciclovir with ganciclovir",
      "Correct. In each case the prodrug exists to solve poor oral absorption of the parent."],
     ["Valacyclovir with ganciclovir, famciclovir with acyclovir, and valganciclovir with penciclovir",
      "The pairings are scrambled; each prodrug belongs to its own parent."],
     ["Oseltamivir with acyclovir, valacyclovir with penciclovir, and famciclovir with ganciclovir",
      "Oseltamivir is a prodrug of its own carboxylate form, unrelated to the guanine analogues."],
     ["There are no prodrugs among the antivirals in this lecture",
      "Several are explicitly described as prodrugs."]],
   c=0, cite=c(124)),

 dict(topic="Comparisons", io=IO5,
   q="Which antiviral in this lecture does NOT act on viral nucleic acid?",
   opts=[
     ["Oseltamivir, which inhibits neuraminidase to block viral release",
      "Correct. The guanine analogues all terminate the nucleic acid chain; oseltamivir works at a completely different stage."],
     ["Acyclovir, which is incorporated into viral DNA",
      "Acyclovir does act on nucleic acid, by chain termination."],
     ["Ganciclovir, which inhibits in a manner similar to acyclovir",
      "Ganciclovir acts on nucleic acid like acyclovir."],
     ["Penciclovir, which has a mechanism similar to acyclovir",
      "Penciclovir also acts on viral nucleic acid."]],
   c=0, cite=c(126)),

 dict(topic="Comparisons", io=IO5,
   q="Which enzyme does each of acyclovir and oseltamivir depend on or target?",
   opts=[
     ["Acyclovir depends on viral thymidine kinase to be activated; oseltamivir targets viral neuraminidase",
      "Correct — one uses a viral enzyme to switch itself on, the other shuts a viral enzyme off."],
     ["Acyclovir targets neuraminidase; oseltamivir depends on thymidine kinase",
      "This reverses the two enzymes."],
     ["Both depend on viral thymidine kinase for activation",
      "Only the guanine analogues do."],
     ["Both target viral neuraminidase at different sites",
      "Only oseltamivir targets neuraminidase."]],
   c=0, cite=c(121)),

 dict(topic="Acyclovir", io=IO6,
   q="Why must renal function be watched during acyclovir therapy?",
   opts=[
     ["The drug crystallises in the renal tubule, so hydration must be maintained",
      "Correct — a physical rather than a toxic mechanism of renal injury."],
     ["The drug is nephrotoxic through direct tubular necrosis",
      "Direct tubular damage is amphotericin B's mechanism."],
     ["Its vehicle accumulates in renal impairment",
      "That is voriconazole's cyclodextrin."],
     ["It causes interstitial nephritis as a hypersensitivity reaction",
      "Interstitial nephritis is listed among the aminopenicillin effects."]],
   c=0, cite=c(123)),

 dict(topic="Ganciclovir", io=IO7,
   q="Compared with acyclovir, what makes ganciclovir the harder drug to tolerate?",
   opts=[
     ["Marked neutropenia and thrombocytopenia, with about a third of patients stopping intravenous treatment",
      "Correct. Acyclovir's bone marrow suppression is listed, but ganciclovir's is far more limiting."],
     ["Crystallisation in the renal tubule requiring aggressive hydration",
      "That is acyclovir's renal problem, not the reason ganciclovir is poorly tolerated."],
     ["Severe infusion reactions requiring premedication",
      "Premedication for infusion reactions belongs to amphotericin B."],
     ["A disulfiram-like reaction on any alcohol exposure",
      "That belongs to metronidazole."]],
   c=0, cite=c(125)),

 dict(topic="Oseltamivir", io=IO8,
   q="What happens to newly formed influenza virions when neuraminidase is inhibited?",
   opts=[
     ["They cannot be cleaved free of the host cell as budding progeny",
      "Correct — they remain tethered at the surface, so the infection cannot spread to new cells."],
     ["They cannot attach to the next host cell's receptor",
      "Attachment is a separate step, and blocking it is a different listed approach."],
     ["They cannot uncoat once inside the next cell",
      "Uncoating is another distinct approach in the list."],
     ["Their nucleic acid cannot be replicated",
      "Nucleic acid inhibition is the guanine analogues' approach."]],
   c=0, cite=c(126)),

 dict(topic="Principles", io=IO5,
   q="Which of the listed antiviral approaches works on the host rather than on the virus?",
   opts=[
     ["Stimulating the host immune system",
      "Correct — it is the only one of the eight aimed at the host side of the interaction."],
     ["Inhibiting specific viral enzymes",
      "That acts on the virus."],
     ["Blocking viral assembly",
      "That acts on the virus."],
     ["Inhibiting viral protein synthesis",
      "That acts on the virus."]],
   c=0, cite=c(118)),

 dict(topic="Herpesviruses", io=IO6,
   q="A patient has meningitis attributed to a herpes simplex virus. Which type does the lecture associate with the meninges?",
   opts=[
     ["Type 2",
      "Correct. Type 2 covers genitals, rectum, hands or meninges; type 1 covers mouth, face, skin, oesophagus or brain."],
     ["Type 1",
      "Type 1 is associated with the brain rather than the meninges in this lecture's split."],
     ["Neither type; meningitis is a cytomegalovirus manifestation",
      "Cytomegalovirus is associated with retinitis, oesophagitis and colitis."],
     ["Neither type; meningitis is caused by varicella-zoster only",
      "Varicella-zoster causes chickenpox and shingles here."]],
   c=0, cite=c(119)),

 dict(topic="Herpesviruses", io=IO6,
   q="A patient has encephalitis attributed to a herpes simplex virus. Which type does the lecture associate with the brain?",
   opts=[
     ["Type 1",
      "Correct — type 1 covers mouth, face, skin, oesophagus or brain."],
     ["Type 2",
      "Type 2 is associated with the meninges rather than the brain in this split."],
     ["Both types equally",
      "The lecture draws a distinction between them."],
     ["Neither; encephalitis is a cytomegalovirus manifestation",
      "Cytomegalovirus manifestations given are retinitis, oesophagitis and colitis."]],
   c=0, cite=c(119)),

 dict(topic="Comparisons", io=IO5,
   q="Which two antiviral agents in this lecture are given intravenously as the parent compound?",
   opts=[
     ["Penciclovir and ganciclovir, each with an oral prodrug available",
      "Correct — famciclovir and valganciclovir respectively are the better-absorbed oral forms."],
     ["Valacyclovir and famciclovir, each with an intravenous prodrug",
      "Those two are the oral prodrugs rather than intravenous parents."],
     ["Oseltamivir and acyclovir, neither having an oral form",
      "Oseltamivir is oral only, and acyclovir is available orally."],
     ["Valganciclovir and valacyclovir, given intravenously in transplant patients",
      "Both are oral prodrugs."]],
   c=0, cite=c(125)),

 dict(topic="Oseltamivir", io=IO8,
   q="Why is influenza treatment framed around a season in this lecture?",
   opts=[
     ["Flu season runs roughly October to March, which is when the illness is circulating",
      "Correct, and it frames when an influenza-like illness should raise suspicion in the first place."],
     ["The drug is only manufactured during those months",
      "Nothing about supply is described."],
     ["Resistance disappears outside the season",
      "Resistance is described as an increasing problem over time, not a seasonal one."],
     ["Renal dosing requirements change with the season",
      "Renal adjustment is not seasonal."]],
   c=0, cite=c(126)),

 dict(topic="Comparisons", io=IO5,
   q="Which statement correctly contrasts how acyclovir and oseltamivir achieve selectivity?",
   opts=[
     ["Acyclovir is activated only by a viral enzyme, whereas oseltamivir inhibits a viral enzyme that has no host equivalent",
      "Correct — two different routes to the same goal of acting on the virus and not the host."],
     ["Both rely on being concentrated inside infected cells by host transporters",
      "Neither mechanism is described that way."],
     ["Both bind host enzymes that infected cells overexpress",
      "Selectivity in both cases turns on viral rather than host enzymes."],
     ["Neither is selective; both rely on short courses to limit host toxicity",
      "Both have specific selectivity mechanisms described."]],
   c=0, cite=c(121)),
]
