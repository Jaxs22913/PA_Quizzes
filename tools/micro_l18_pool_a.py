# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 18 — DNA Viruses of Medical Importance (Dr. Webster, 13 November 2026), pool A: the
# GENERAL VIROLOGY front of the deck, slides 1-30, plus the group lists on 31 (enveloped) and 92 (nonenveloped):
# viral structure (8-10), the phage (11) and its three replication cycles (13-18), phages in the gut and the
# immune system (19-21), animal virus replication (22-23), medical considerations and the course of viral disease
# (24-25, 29), acute against persistent chronic and persistent latent infections (26-27), oncogenic and teratogenic
# viruses and the diagnosis line (28), and the DNA virus groups (30-31, 92).
#
# FROM THE VISIBLE SLIDES ONLY (text and pictures; speaker notes not used). Picture-only content used: slide 10
# (naked nucleocapsid against enveloped virus, spikes on the envelope), slide 11 (the phage head, tail, sheath,
# plug and tail fibers), slide 17 (the three-cycle diagram: "Virulent phages: only lytic cycles", "Temperate
# phages: lysogenic cycles and lytic or chronic cycles"; the lysogenic bacterium reproduces normally), slide 22
# (the animal-virus diagram: adsorption by specific binding of spikes to cell receptors; penetration by
# endocytosis into a vesicle), slide 23 (the seven papovavirus steps: attachment, entry and uncoating, a portion
# of viral DNA transcribed to mRNA for "early" proteins, biosynthesis, late translation of capsid proteins,
# maturation, release), slide 27 (lytic infection, latent infection with recurrence, chronic infection,
# transformation to malignancy), slide 30 (DNA virus groups chart). No picture items in this pool.
#
# Four options throughout. KEYS SHORT, explanations full. Every key authored at position 0 with the only
# "Correct." opener; `mis` names each distractor's misconception.
#
# NOT DUPLICATED (an existing Webster-review quiz asks them): animal virus engulfed whole; uncoating as the step;
# lysogenic cycle identified from integration + shock; chronic cycle identified from extrusion; envelope from
# budding; all viruses have a capsid; HIV as the chronic example; latent infection defined; influenza as acute;
# episome as the latent form; hepatitis B with hepatic carcinoma; papillomavirus with cervical and penile cancer;
# the term teratogenic; rubella as teratogenic. Items here ask other facts or the other direction (what drives
# uncoating, how a prophage differs from an episome, Epstein-Barr virus -> which cancer, cytomegalovirus as
# teratogenic, hepatitis B as chronic, detectability as the chronic/latent divider).
#
# HELD, and why:
#   - slide 12 (total viral mass in blue whales; the three origin hypotheses): not asked; speculative, low yield.
#   - slide 13's "8% of human DNA is of viral origin" and the placental gene: numbers and side facts, not keyed.
#   - slide 21's specific cells and immunoglobulin classes (M cells, dendritic cells, IgA, IgG, interferon gamma):
#     pathway detail, used only inside explanations where needed; not keyed.
#   - slide 24's zoonoses examples (West Nile fever, hantavirus, viral encephalitis): RNA-virus examples, off-topic.
#   - slide 29's "fragile sites" theory and the epigenetic steps: a theory, not asked as fact.
#   - slide 16's Propionibacterium freudenreichii and Swiss cheese: trivia.
#   - transformation to malignancy and integration: slide 27 shows transformation as an outcome but no slide says
#     whether it involves integration; never offered where integration is the decider.
#   - hepatitis B as "chronic": slide 26 lists it as the chronic example; keyed as the slide says.
# CONFLICTS: chart slide 5 gives cervical and penile cancer to herpes simplex virus type 2, slide 28 to
#   papillomaviruses (brief rule): herpes simplex is never an option on the oncogenic items. Slide 6 lists
#   Epstein-Barr virus with nasopharyngeal carcinoma too: never an option on the Epstein-Barr item. Slide 7 gives
#   parvovirus B19 "hydrops fetalis ... from maternal transmission" and slide 5 "herpes of the newborn": neither is
#   offered on the teratogenic item, where slide 28 names only rubella and cytomegalovirus. Toxins appear under both
#   lysogenic (slide 18 "ability to make a toxin") and chronic ("toxins and biofilms"): no item keys a toxin to
#   one cycle alone.
# SPELLING: "Iscosahedral" -> icosahedral; "Cytomegaloviirus" -> cytomegalovirus; "sphenomegaly" -> splenomegaly;
#   US spelling throughout.
from micro_l18_common import *

POOL_A = [

# ---------------------------------------------------------------- Viral structure (4)
Q("Viral structure", IO4,
  "A bacteriophage has a head joined to a tail with a sheath and tail fibers. Which capsid type is this?",
  ("Complex",
   "Correct. Viral capsids come in three shapes: helical, icosahedral and complex, and the complex shape is the "
   "phage type. The head-and-tail build, with sheath, plug and tail fibers below a capsid head, is what makes a "
   "phage capsid complex rather than a simple rod or a many-sided solid."),
  [("Helical",
    "A helical capsid is a rod of capsid units wound around the nucleic acid, the nucleocapsid drawn as a single "
    "spiral column. A phage adds a tail, sheath and tail fibers to its head, which is the complex type.",
    "other capsid shape"),
   ("Icosahedral",
    "An icosahedral capsid is the many-sided solid seen in naked and enveloped animal viruses such as the "
    "papovavirus. The phage's head sits on a tail with sheath and fibers, so the whole capsid is complex.",
    "the head shape taken for the whole"),
   ("Enveloped",
    "An envelope is not a capsid shape at all: it is a membrane layer some animal viruses gain during budding, "
    "outside the capsid. Capsids are helical, icosahedral or complex, and the tailed phage is the complex one.",
    "envelope confused with capsid")],
  c(9, 11)),

Q("Viral structure", IO4,
  "Some animal viruses carry an envelope outside the capsid. What is the envelope thought to help the virus do?",
  ("Evade the immune system",
   "Correct. An animal virus may have an envelope or spikes; the envelope is obtained as the virus buds through "
   "the cell membrane and is described as a mechanism to assist in evading the immune system. The capsid, not the "
   "envelope, is the protein coat that encloses and protects the nucleic acid."),
  [("Inject its genome",
    "Injecting the genome is what a phage does: viral lysozyme and a tail pin breach the bacterial wall and inject "
    "the viral DNA (deoxyribonucleic acid). The envelope of an animal virus is instead a help in evading the "
    "immune system.",
    "phage penetration"),
   ("Burst the host cell",
    "Bursting the host is the last step of the phage lytic cycle, done by viral lysozyme on the cell wall. Enveloped "
    "animal viruses leave by budding, gaining the envelope that helps them evade the immune system.",
    "lytic release"),
   ("Enclose its nucleic acid",
    "Enclosing and protecting the nucleic acid is the job of the capsid, the protein coat every virus has. The "
    "envelope is an extra outer layer, present only in some animal viruses, that helps evade the immune system.",
    "capsid role given to envelope")],
  c(9, 10)),

Q("Viral structure", IO4,
  "Animal viruses are grouped by their nucleic acid, their capsid and which other feature?",
  ("Presence of an envelope",
   "Correct. Animal viruses are categorized according to nucleic acid, capsid, and presence or absence of an "
   "envelope. That is why the human DNA (deoxyribonucleic acid) virus groups split first into enveloped and nonenveloped viruses, then by "
   "double-stranded or single-stranded genome."),
  [("Their host cell type",
    "Host cell type is not among the features used to group animal viruses. Animal viruses are grouped by "
    "nucleic acid, capsid and whether an envelope is present.",
    "host range as classification"),
   ("Their mode of spread",
    "Mode of transmission is listed per virus (droplets, direct contact, blood) but is not how the families are "
    "built. The grouping uses nucleic acid, capsid and presence or absence of an envelope.",
    "transmission as classification"),
   ("Their tail structure",
    "A tail is a feature of the complex capsid of bacteriophages, viruses of bacteria, not an animal virus "
    "grouping feature. Animal viruses are grouped by nucleic acid, capsid and presence or absence of an "
    "envelope.",
    "phage anatomy")],
  c(8, 30)),

Q("Viral structure", IO4,
  "Nearly all RNA (ribonucleic acid) viruses are single-stranded. Which group is the exception?",
  ("Reoviruses",
   "Correct. All RNA (ribonucleic acid) viruses are single-stranded except for the double-stranded RNA (ribonucleic acid) "
   "reoviruses. DNA (deoxyribonucleic acid) viruses run the other way: most are double-stranded, with some "
   "single-stranded ones such as the parvoviruses."),
  [("Parvoviruses",
    "Parvoviruses are DNA (deoxyribonucleic acid) viruses, and the single-stranded exception among them: "
    "nonenveloped with a single-stranded genome. The double-stranded RNA (ribonucleic acid) exception is the "
    "reoviruses.",
    "the DNA (deoxyribonucleic acid)-side exception"),
   ("Poxviruses",
    "Poxviruses are enveloped double-stranded DNA (deoxyribonucleic acid) viruses, not RNA (ribonucleic acid) "
    "viruses at all. Among RNA (ribonucleic acid) viruses only the reoviruses are double-stranded.",
    "DNA (deoxyribonucleic acid) virus group"),
   ("Adenoviruses",
    "Adenoviruses are nonenveloped double-stranded DNA (deoxyribonucleic acid) viruses. The RNA (ribonucleic "
    "acid) viruses are single-stranded except the reoviruses, which carry double-stranded RNA (ribonucleic acid).",
    "DNA (deoxyribonucleic acid) virus group")],
  c(8, 30)),

# ---------------------------------------------------------------- Phage replication cycles (8)
Q("Phage replication cycles", IO1,
  "In the replication step of the phage lytic cycle, what does the virus make first?",
  ("Copies of its genome",
   "Correct. In replication the virus turns off normal bacterial metabolism and turns the bacterium into a viral "
   "factory, first replicating the viral DNA (deoxyribonucleic acid), then the capsid components. Assembly and "
   "maturation of new virions follow, then release."),
  [("Capsid components",
    "Capsid components are made in the replication step, but second: the viral DNA (deoxyribonucleic acid) is "
    "replicated first, then the capsid parts. Assembly then puts the new virions together.",
    "order reversed"),
   ("Viral lysozyme for release",
    "Viral lysozyme acts at the end, bursting the host wall to release virions, and at penetration to breach the "
    "wall. In the replication step the DNA (deoxyribonucleic acid) is copied first, then capsid parts.",
    "release step"),
   ("Copies of host chromosome",
    "The phage does not copy the host chromosome; it turns off normal metabolism and makes viral parts. Being "
    "copied along with the host chromosome is the prophage of the lysogenic cycle, not the lytic replication step.",
    "lysogenic replication")],
  c(14)),

Q("Phage replication cycles", IO1,
  "At the end of the phage lytic cycle, how are the new virions released?",
  ("Lysozyme bursts the wall",
   "Correct. Release is the last lytic step: viral lysozyme causes the host cell wall to burst, freeing the new "
   "virions and destroying the host cell. Destruction of the host cell is one of the defining features of the "
   "lytic cycle."),
  [("Extrusion without lysis",
    "Extrusion without lysis is the chronic cycle of filamentous phages: virions leave continuously and the host "
    "only grows more slowly. The lytic cycle ends with viral lysozyme bursting the wall and killing the host.",
    "chronic cycle release"),
   ("Budding off the membrane",
    "Budding is how animal viruses leave, which may give them an envelope. A phage in the lytic cycle frees its "
    "virions when viral lysozyme bursts the bacterial cell wall. To tell them apart: budding is the animal virus exit; lysozyme bursting is the phage exit.",
    "animal virus release"),
   ("Induction by a shock",
    "A shock induces a prophage to leave the bacterial chromosome and start a lytic cycle; it begins the cycle, it "
    "does not release virions. Release happens when viral lysozyme bursts the cell wall.",
    "lysogenic induction")],
  c(14, 15, 18, 22)),

Q("Phage replication cycles", IO1,
  "In the lysogenic cycle, what is the viral DNA (deoxyribonucleic acid) called once it has integrated into the "
  "bacterial chromosome?",
  ("A prophage",
   "Correct. Instead of turning off bacterial metabolism, the viral DNA (deoxyribonucleic acid) integrates into the "
   "host chromosome and becomes a prophage. The prophage is replicated with the host cell for generations until a "
   "shock induces it to leave and start a lytic cycle."),
  [("An episome",
    "An episome is the latent herpesvirus DNA (deoxyribonucleic acid) in an animal cell: in the nucleus but not "
    "integrated. Integrated phage DNA (deoxyribonucleic acid) in a bacterial chromosome is a prophage.",
    "latent animal form"),
   ("A virion",
    "A virion is a complete virus particle, made at assembly and maturation and released at the end of a lytic "
    "cycle. Viral DNA (deoxyribonucleic acid) sitting inside the bacterial chromosome is a prophage.",
    "free particle"),
   ("A nucleocapsid",
    "A nucleocapsid is the capsid with the nucleic acid inside it, a part of the virus particle. Once phage DNA (deoxyribonucleic acid) "
    "has integrated into the bacterial chromosome it is called a prophage.",
    "structural term")],
  c(15, 10, 26)),

Q("Phage replication cycles", IO1,
  "A bacterium carrying a prophage reproduces normally. Which other trait does the lysogenic state give it?",
  ("Immunity to reinfection",
   "Correct. Lysogenic features are integration of viral genes as a prophage, viral genes replicated with the host "
   "cell, possible new traits, and immunity to reinfection. The lysogenic bacterium reproduces normally rather than "
   "being destroyed."),
  [("Destruction by lysis",
    "Destruction of the host cell belongs to the lytic cycle, with rapid takeover of metabolism and many copies of "
    "virus. A lysogenic bacterium reproduces normally and is immune to reinfection.",
    "lytic outcome"),
   ("A slowed growth rate",
    "A slowed growth rate is the chronic cycle of filamentous phages, whose virions are extruded without lysis. A "
    "lysogenic bacterium with its prophage reproduces normally and is immune to reinfection.",
    "chronic outcome"),
   ("Uncoating of the phage",
    "Uncoating is a step of animal virus replication, releasing the genome from the engulfed virion. Phages inject "
    "their DNA (deoxyribonucleic acid); the lysogenic bacterium gains immunity to reinfection.",
    "animal virus step")],
  ci(17, 15, 18)),

Q("Phage replication cycles", IO1,
  "Which process carries random pieces of host DNA (deoxyribonucleic acid) from one bacterium to other bacteria?",
  ("Generalized transduction",
   "Correct. Generalized transduction, listed with the lytic cycle, means random pieces of the host DNA (deoxyribonucleic acid) "
   "may be transmitted to other bacteria. In specialized transduction, from the lysogenic "
   "cycle, all cells carry the same DNA (deoxyribonucleic acid) from the host."),
  [("Specialized transduction",
    "Specialized transduction belongs to the lysogenic cycle, and in it all cells carry the same DNA (deoxyribonucleic acid) "
    "from the host, not random pieces. Random pieces mark generalized transduction.",
    "the other transduction"),
   ("Lysogenic conversion",
    "Lysogenic conversion is one of the phage-bacterium interactions in the gut, a bacterium changed by its "
    "prophage, such as gaining a new trait. Random host pieces moved to other bacteria are generalized "
    "transduction.",
    "adjacent gut term"),
   ("Prophage induction",
    "Prophage induction is the shock that releases a prophage from the host chromosome to start a lytic cycle. "
    "Carrying random pieces of host DNA (deoxyribonucleic acid) to other bacteria is generalized transduction.",
    "adjacent gut term")],
  c(18, 15, 19)),

Q("Phage replication cycles", IO1,
  "Filamentous phages use no lysozyme. How do they get into their bacterial host?",
  ("Capsid-receptor protein match",
   "Correct. Filamentous phages attach to pili or walls without lysozyme; there appears to be a compatibility "
   "between virion capsid proteins and host receptor proteins, listed as penetration via protein compatibility. "
   "The exact way the DNA (deoxyribonucleic acid) enters is not yet fully understood."),
  [("A tail pin through the wall",
    "Lysozyme with a tail pin to breach the wall and inject the genome is lytic and lysogenic phage penetration. "
    "Filamentous phages of the chronic cycle skip lysozyme and rely on capsid-receptor protein compatibility.",
    "tailed phage entry"),
   ("Whole-virion engulfment",
    "Engulfment of the entire virion is how animal viruses enter, followed by uncoating. A filamentous phage enters "
    "its bacterium through compatibility between its capsid proteins and host receptor proteins.",
    "animal virus entry"),
   ("Uncoating by a pH change",
    "Uncoating driven by the pH of the cytoplasm against the extracellular fluid is an animal virus step after "
    "engulfment. Filamentous phage entry depends on capsid-receptor protein compatibility.",
    "animal virus step")],
  c(16, 18, 22)),

Q("Phage replication cycles", IO1,
  "What is the genome of a filamentous phage of the chronic cycle?",
  ("Single-stranded DNA (deoxyribonucleic acid)",
   "Correct. Filamentous phages are flexible rods containing single-stranded DNA (deoxyribonucleic acid) coding "
   "for about 10 genes. They mostly infect gram-negative bacteria and are extruded from the host without lysing "
   "it, only slowing its growth."),
  [("Double-stranded DNA (deoxyribonucleic acid)",
    "Double-stranded DNA (deoxyribonucleic acid) is the genome of most DNA (deoxyribonucleic acid) viruses, but the filamentous phages are "
    "flexible rods carrying single-stranded DNA (deoxyribonucleic acid) with about 10 genes.",
    "the usual DNA (deoxyribonucleic acid) virus"),
   ("Single-stranded RNA (ribonucleic acid)",
    "Single-stranded RNA (ribonucleic acid) describes nearly all RNA (ribonucleic acid) viruses. The filamentous phages of the "
    "chronic cycle carry single-stranded DNA (deoxyribonucleic acid) coding for about 10 genes.",
    "RNA (ribonucleic acid) virus genome"),
   ("Double-stranded RNA (ribonucleic acid)",
    "Double-stranded RNA (ribonucleic acid) is the reovirus exception among RNA (ribonucleic acid) viruses. Filamentous phages carry "
    "single-stranded DNA (deoxyribonucleic acid) coding for about 10 genes.",
    "reovirus genome")],
  c(16, 8)),

Q("Phage replication cycles", IO1,
  "A phage that can carry out only lytic cycles, never lysogenic ones, is described by which term?",
  ("Virulent",
   "Correct. Virulent phages carry out only lytic cycles, destroying their host each time. Temperate phages can "
   "enter lysogenic cycles as well as lytic or chronic cycles, so a phage limited to lysis is virulent."),
  [("Temperate",
    "Temperate phages can run lysogenic cycles as well as lytic or chronic ones, integrating as a prophage. A phage "
    "limited to lytic cycles is virulent. To tell them apart: a temperate phage has a choice of cycles, a virulent phage has only one.",
    "reversed term"),
   ("Filamentous",
    "Filamentous phages are the flexible rods of the chronic cycle, extruded without lysing the host. A phage "
    "limited to lytic cycles, always destroying the host, is called virulent. To tell them apart: filamentous names a shape.",
    "chronic cycle phage"),
   ("Lysogenic",
    "Lysogenic names the cycle in which the phage integrates as a prophage, the opposite of a lytic-only phage. "
    "Phages that only lyse are virulent; those able to integrate are temperate.",
    "cycle name for phage type")],
  ci(17, 13)),

# ---------------------------------------------------------------- Phages, the gut and immunity (2)
Q("Phages, the gut and immunity", IO1,
  "Why may phage therapy trials give relatively unpredictable results?",
  ("Complex phage-bacteria relationships",
   "Correct. Phages are bacterial strain specific, the gut environment protects some bacteria, interactions can be "
   "antagonistic or mutualistic and may change over time through evolution. These complex relationships may "
   "explain the relative unpredictability of phage therapy trials."),
  [("Phages infecting human cells",
    "The host cells of bacteriophages are bacterial cells, though phages may still affect human health. The "
    "unpredictability comes from complex phage-bacterium relationships, such as strain specificity and resistance.",
    "wrong host"),
   ("Phages lacking strain specificity",
    "This reverses the fact: phages are bacterial strain specific. That specificity, along with protected bacteria "
    "and shifting interactions, is part of the complex relationships that make therapy trials unpredictable.",
    "reversed fact"),
   ("Phages lacking nucleic acid",
    "Every virus contains genetic material, DNA (deoxyribonucleic acid) or RNA (ribonucleic acid), and phage "
    "nucleic acids may even stimulate an immune response. Trial unpredictability stems from complex phage-bacteria "
    "relationships.",
    "structure misread")],
  c(20, 19, 13, 9)),

Q("Phages, the gut and immunity", IO4,
  "Patients with Crohn disease or ulcerative colitis show a shift in gut virome composition. What does this shift "
  "establish?",
  ("A link, cause not proven",
   "Correct. Some studies show a shift in virome composition in inflammatory bowel disease, Crohn disease or "
   "ulcerative colitis, but this may or may not be a cause-and-effect relationship. It is an observed association, "
   "not proof that phages cause the disease."),
  [("Phages cause the disease",
    "No cause has been shown: the virome shift may or may not be a cause-and-effect relationship. Reading it as "
    "proof that phages cause inflammatory bowel disease goes beyond what the studies show.",
    "association read as cause"),
   ("The disease destroys phages",
    "The reverse direction is not shown either; the studies record only a change in virome composition, which may "
    "or may not be cause and effect. It is an association, cause not proven.",
    "reversed causation"),
   ("Phages protect the bowel",
    "No protective role is stated; phages may even compromise colonization of normal flora. The virome shift in "
    "inflammatory bowel disease is an association whose cause and effect is unproven.",
    "invented benefit")],
  c(20)),

# ---------------------------------------------------------------- Animal virus replication (6)
Q("Animal virus replication", IO1,
  "After an animal virus is engulfed, what drives the uncoating that frees its genetic material?",
  ("A difference in pH",
   "Correct. Animal viruses need uncoating to release their genetic material, and the trigger is the pH of the "
   "cytoplasm compared with the extracellular fluid. Phages need no uncoating because only their DNA (deoxyribonucleic acid) "
   "is injected."),
  [("Viral lysozyme",
    "Viral lysozyme is the phage's tool, used with the tail pin to breach the bacterial wall and later to burst it "
    "at release. Animal virus uncoating depends on the pH of the cytoplasm against the extracellular fluid.",
    "phage enzyme"),
   ("A shock to the cell",
    "A shock of some kind is what induces a prophage to leave the bacterial chromosome in the lysogenic cycle. "
    "Animal virus uncoating is driven by a pH difference between cytoplasm and extracellular fluid.",
    "prophage induction"),
   ("Receptor binding",
    "Binding of the virus's spikes to cell receptors is adsorption, the first step, before engulfment. Uncoating "
    "inside the cell is driven by the pH of the cytoplasm against the extracellular fluid.",
    "adsorption step")],
  c(22)),

Q("Animal virus replication", IO1,
  "An enveloped animal virus attaches to its host cell. Which viral structure binds the cell receptors?",
  ("Its spikes",
   "Correct. In adsorption the virus attaches to its host cell by specific binding of its spikes to cell "
   "receptors. This receptor fit is also why viruses are limited to a particular host or cell type. To tell them apart: tail fibers are phage parts; spikes are animal virus parts."),
  [("Its tail fibers",
    "Tail fibers are part of a bacteriophage, which adsorbs to bacteria and injects its genome. An enveloped animal "
    "virus attaches by specific binding of its envelope spikes to cell receptors.",
    "phage anatomy"),
   ("Its nucleic acid",
    "The nucleic acid lies inside the capsid and is freed only after uncoating, inside the cell. Attachment uses "
    "the spikes on the envelope, which bind specific cell receptors. To tell them apart: attachment is on the outside.",
    "inner part as attachment"),
   ("Its matrix",
    "The matrix is a layer inside the envelope, around the capsid, not on the surface. Surface spikes are what bind "
    "the cell receptors during adsorption. To tell them apart: only the spikes project from the envelope surface, where receptors sit.",
    "inner layer as attachment")],
  ci(22, 9, 10, 24)),

Q("Animal virus replication", IO1,
  "In the replication of a DNA (deoxyribonucleic acid) animal virus, which step comes right after entry and "
  "uncoating?",
  ("Transcription for early proteins",
   "Correct. After the virion enters and its DNA (deoxyribonucleic acid) is uncoated, a portion of the viral DNA (deoxyribonucleic acid) is "
   "transcribed, producing messenger RNA (ribonucleic acid) that encodes early viral proteins. Biosynthesis, late "
   "translation of capsid proteins, maturation and release follow."),
  [("Late translation of capsids",
    "Late translation, when capsid proteins are synthesized, comes after early transcription and biosynthesis of "
    "viral DNA (deoxyribonucleic acid). The step straight after uncoating is transcription for early proteins.",
    "late step moved early"),
   ("Maturation of virions",
    "Maturation is the sixth step, after capsid proteins are made, just before release. Directly after uncoating, "
    "part of the viral DNA (deoxyribonucleic acid) is transcribed for early proteins.",
    "late step moved early"),
   ("Release by budding",
    "Release of virions by budding is the last step of the seven. Directly after entry and uncoating, a portion of "
    "the viral DNA (deoxyribonucleic acid) is transcribed for early proteins.",
    "last step")],
  ci(23)),

Q("Animal virus replication", IO1,
  "In a DNA (deoxyribonucleic acid) animal virus, which proteins are made by late translation?",
  ("Capsid proteins",
   "Correct. Early transcription makes messenger RNA (ribonucleic acid) for early viral proteins; after the viral "
   "DNA (deoxyribonucleic acid) is replicated, late translation synthesizes the capsid proteins. The virions then "
   "mature and are released."),
  [("Early viral proteins",
    "Early viral proteins come from messenger RNA (ribonucleic acid) transcribed straight after uncoating, before "
    "DNA (deoxyribonucleic acid) replication. Late translation is when capsid proteins are made.",
    "early and late swapped"),
   ("Viral lysozyme",
    "Viral lysozyme is a phage enzyme, used to breach the bacterial wall and burst it at release. In a DNA (deoxyribonucleic acid) "
    "animal virus, late translation makes the capsid proteins.",
    "phage enzyme"),
   ("Host cell receptors",
    "Receptors belong to the host cell and are what the virus binds at attachment; the virus does not make them. "
    "Late translation in a DNA (deoxyribonucleic acid) animal virus makes capsid proteins.",
    "host part")],
  ci(23)),

Q("Animal virus replication", IO1,
  "Most DNA (deoxyribonucleic acid) viruses are budded off which part of the host cell?",
  ("The nucleus",
   "Correct. Most DNA (deoxyribonucleic acid) viruses are budded off the nucleus, while most RNA "
   "(ribonucleic acid) viruses multiply in and are released from the cytoplasm."),
  [("The cytoplasm",
    "Multiplying in and release from the cytoplasm describes most RNA (ribonucleic acid) viruses. Most DNA (deoxyribonucleic acid) "
    "viruses are budded off the nucleus.",
    "RNA (ribonucleic acid) virus pattern"),
   ("The cell wall",
    "A cell wall is the bacterial layer that phage lysozyme breaches and bursts. Animal cells are drawn with a cell "
    "membrane, and most DNA (deoxyribonucleic acid) viruses are budded off the nucleus.",
    "bacterial structure"),
   ("An endocytic vesicle",
    "An endocytic vesicle is how a virus enters: it is engulfed into a vesicle by endocytosis at penetration. Most "
    "DNA (deoxyribonucleic acid) viruses are budded off the nucleus. To tell them apart: entry, not exit.",
    "entry structure")],
  ci(23, 24, 22)),

# ---------------------------------------------------------------- Course of viral disease (3)
Q("Course of viral disease", IO1,
  "Why is a given virus limited to a particular host or cell type?",
  ("Receptor compatibility",
   "Correct. Viruses are limited to a particular host or cell type by compatibility of receptors and genetic "
   "material. At adsorption the virus attaches by specific binding of its spikes to the cell receptors, so cells "
   "without a matching receptor are not infected."),
  [("Genome size",
    "Genome size is not what limits the host; the limit is compatibility of receptors and genetic material, with "
    "spikes binding specific cell receptors at adsorption. To tell them apart: specificity is a lock-and-key fit at the cell surface, not a matter of size.",
    "irrelevant feature"),
   ("Presence of an envelope",
    "An envelope comes from budding and helps evade the immune system; it is a classification feature, not the "
    "host limit. Host and cell range depend on receptor compatibility. To tell them apart: the fit is at the receptor.",
    "envelope role"),
   ("Mode of transmission",
    "Transmission decides how a virus reaches a person, such as droplets or direct contact, not which cells it can "
    "infect. Host and cell type are set by compatibility of receptors and genetic material.",
    "transmission confused")],
  ci(22, 24)),

Q("Course of viral disease", IO5,
  "Why have some viruses been used as agents for vaccination?",
  ("Lifelong immunity often follows",
   "Correct. Body defenses against viruses, the combined action of interferon, antibodies, natural killer cells "
   "and cytotoxic T cells, frequently result in lifelong immunity. This is why some viruses have been used as "
   "agents for vaccination."),
  [("They stay latent in nerves",
    "Lifelong dormancy is a latent infection, which can reactivate and cause recurrent disease, a drawback rather "
    "than the basis of vaccination. Vaccination relies on the lifelong immunity infection frequently produces.",
    "latency confused"),
   ("They join the host chromosome",
    "Integration into the host chromosome is a feature that may occur in chronic infections such as hepatitis B "
    "virus. Viruses serve as vaccine agents because infection frequently results in lifelong immunity.",
    "chronic infection"),
   ("They cause no tissue damage",
    "Viral infections range from asymptomatic to life-threatening, and some viruses replicate locally with tissue "
    "disruption. Vaccine use rests on the lifelong immunity that infection frequently produces.",
    "harmlessness belief")],
  c(25, 24, 26)),

Q("Course of viral disease", IO4,
  "Through an autoimmune connection, viruses may be involved in which disorder?",
  ("Type 1 diabetes",
   "Correct. Viruses may be involved in disorders such as type 1 diabetes, multiple sclerosis and chronic fatigue "
   "syndrome through an autoimmune connection. The process starts with a genetically predisposed person exposed "
   "to infectious and other environmental agents."),
  [("Kaposi sarcoma",
    "Kaposi sarcoma is a cancer, linked to human herpesvirus 8 as an oncogenic virus, not an autoimmune disorder. "
    "Type 1 diabetes, multiple sclerosis and chronic fatigue syndrome carry the autoimmune connection.",
    "oncogenic outcome"),
   ("Hepatic carcinoma",
    "Hepatic carcinoma is the cancer linked to persistent hepatitis B virus, an oncogenic effect. The autoimmune "
    "connection is with type 1 diabetes, multiple sclerosis and chronic fatigue syndrome.",
    "oncogenic outcome"),
   ("Burkitt lymphoma",
    "Burkitt lymphoma is the Epstein-Barr virus tumor, an oncogenic effect. Viruses may be involved in type 1 "
    "diabetes, multiple sclerosis and chronic fatigue syndrome through an autoimmune connection.",
    "oncogenic outcome")],
  c(25, 28, 29)),

# ---------------------------------------------------------------- Acute, chronic and latent infections (5)
Q("Acute, chronic and latent infections", IO2,
  "Which type of infection does hepatitis B virus establish, with virus detectable in tissue and multiplying "
  "slowly?",
  ("Persistent chronic",
   "Correct. Chronic infections keep the virus detectable in tissue samples, multiplying at a slow rate, with mild "
   "or absent symptoms; hepatitis B virus and human immunodeficiency virus are the examples. Chronic infection may "
   "involve integration of viral genetic material into the host chromosome."),
  [("Persistent latent",
    "Latent infections, the herpesviruses' pattern, go dormant after a lytic cycle and are generally not "
    "detectable. Hepatitis B virus stays detectable and multiplies slowly, a chronic infection.",
    "latent confused"),
   ("Acute lytic",
    "Acute infections take a rapid lytic course, as in colds and flu, and do not persist for years. Hepatitis B "
    "virus persists, detectable and slowly multiplying: a chronic infection.",
    "acute confused"),
   ("Lysogenic",
    "Lysogenic is a phage cycle in bacteria, the prophage replicated with the host chromosome. In human viral "
    "infection, hepatitis B virus is the example of a persistent chronic infection.",
    "phage term")],
  c(26)),

Q("Acute, chronic and latent infections", IO2,
  "Which feature separates a persistent chronic infection from a persistent latent one?",
  ("Virus detectable in tissue",
   "Correct. In chronic infection the virus is detectable in tissue samples, multiplying at a slow rate. In latent "
   "infection the virus enters a dormant phase after a lytic cycle and is generally not detectable, until it "
   "reactivates."),
  [("Infection lasting for years",
    "Both kinds are persistent infections lasting many years or a lifetime, so duration does not separate them. "
    "Detectability does: chronic virus is detectable in tissue, latent virus generally is not.",
    "shared feature"),
   ("Reactivation with recurrences",
    "Reactivation causing recurrent infection is the mark of latent infection, as with the herpesviruses, not "
    "chronic. Chronic infection is set apart by virus detectable in tissue, multiplying slowly.",
    "latent feature"),
   ("Severe ongoing symptoms",
    "Chronic infection has mild or absent symptoms, and latent infection has none while dormant, so severity does "
    "not separate them. Chronic virus is detectable in tissue; latent virus generally is not.",
    "invented severity")],
  c(26)),

Q("Acute, chronic and latent infections", IO2,
  "Herpesviruses typically establish which kind of infection?",
  ("Persistent latent",
   "Correct. Herpesviruses are the example of latent infection: after a lytic cycle the virus enters a dormant "
   "phase, generally not detectable and without symptoms, and can reactivate to cause recurrent infections. Its "
   "DNA (deoxyribonucleic acid) stays in the nucleus without integrating."),
  [("Persistent chronic",
    "Chronic infection, detectable and slowly multiplying, is the pattern of human immunodeficiency virus and "
    "hepatitis B virus. Herpesviruses go dormant and reactivate: latent infection.",
    "chronic confused"),
   ("Acute only",
    "Acute infections run a rapid lytic course and end, like colds and flu. Herpesviruses begin with a lytic "
    "cycle but then persist dormant and can reactivate, a latent infection. To tell them apart: herpes recurs.",
    "first phase taken as whole"),
   ("Teratogenic",
    "Teratogenic describes viruses that cross the placenta and cause developmental defects, such as rubella and "
    "cytomegalovirus; it is not an infection course. Herpesviruses establish latent infection.",
    "category confused")],
  c(26, 28)),

Q("Acute, chronic and latent infections", IO2,
  "Which persistent infection may involve integration of viral genetic material into the host chromosome?",
  ("Chronic infection",
   "Correct. Chronic infections, such as human immunodeficiency virus and hepatitis B virus, may involve "
   "integration of genetic material into the host chromosome. In latent herpesvirus infection, by contrast, the "
   "viral DNA (deoxyribonucleic acid) is an episome, in the nucleus but not integrated."),
  [("Latent infection",
    "Latent herpesvirus DNA (deoxyribonucleic acid) is an episome: in the nucleus but not integrated. Integration "
    "into the host chromosome is noted for chronic infections. To tell them apart: latent means dormant but separate from the host chromosome.",
    "episome confused"),
   ("Acute infection",
    "Acute infection is a rapid lytic course, as in colds and flu, which destroys the cell rather than persisting. "
    "Integration into the host chromosome is noted for chronic infections.",
    "not persistent"),
   ("Recurrent infection",
    "Recurrent infection is what a latent virus causes when it reactivates, and latent viral DNA (deoxyribonucleic acid) "
    "is not integrated. Integration is noted for chronic infections.",
    "latent outcome")],
  ci(27, 26)),

Q("Acute, chronic and latent infections", IO2,
  "How does latent herpesvirus DNA (deoxyribonucleic acid) differ from a phage prophage?",
  ("It is not integrated",
   "Correct. A prophage is phage DNA (deoxyribonucleic acid) integrated into the bacterial chromosome. Latent "
   "herpesvirus DNA (deoxyribonucleic acid) is an episome, in the nucleus but not integrated, though both lie dormant and can later "
   "reactivate into active virus production."),
  [("It lies in the cytoplasm",
    "The latent herpesvirus episome sits in the nucleus, not the cytoplasm. Its difference from a prophage is that "
    "it is not integrated into the host chromosome. To tell them apart: both the episome and the prophage sit with the host genetic material; only one is joined to it.",
    "wrong location"),
   ("It can never reactivate",
    "Latent herpesvirus can reactivate and cause recurrent infection, much as a prophage can be induced. The "
    "difference is that the episome is not integrated into the chromosome. To tell them apart: dormant is not dead.",
    "reactivation denied"),
   ("It is detectable in tissue",
    "Latent virus is generally not detectable; being detectable in tissue marks chronic infection. The episome "
    "differs from a prophage in not being integrated. To tell them apart: detectability is the chronic-versus-latent divider, not the prophage comparison.",
    "chronic feature")],
  c(26, 15, 27)),

# ---------------------------------------------------------------- Oncogenic and teratogenic viruses (4)
Q("Oncogenic and teratogenic viruses", IO3,
  "Epstein-Barr virus is oncogenic. Which cancer is it linked with?",
  ("Burkitt lymphoma",
   "Correct. Among persistent oncogenic viruses, Epstein-Barr virus is linked with Burkitt lymphoma. The other "
   "pairings are human herpesvirus 8 with Kaposi sarcoma, hepatitis B virus with hepatic carcinoma, and "
   "papillomaviruses with cervical and penile cancer."),
  [("Kaposi sarcoma",
    "Kaposi sarcoma is the tumor of human herpesvirus 8, a different herpesvirus. Epstein-Barr virus is the one "
    "linked with Burkitt lymphoma. To tell them apart: Kaposi sarcoma shows as small painless discolored skin lumps, often in acquired immunodeficiency syndrome, not as a lymphoma.",
    "herpesvirus 8 pairing"),
   ("Hepatic carcinoma",
    "Hepatic carcinoma is linked with persistent hepatitis B virus, a hepadnavirus, not a herpesvirus. "
    "Epstein-Barr virus is paired with Burkitt lymphoma. To tell them apart: the liver cancer belongs to hepatitis B virus, the lymphoma to Epstein-Barr virus.",
    "hepatitis B pairing"),
   ("Cervical cancer",
    "Cervical and penile cancer are linked with the papillomaviruses, nonenveloped double-stranded viruses. "
    "Epstein-Barr virus, an enveloped herpesvirus, is linked with Burkitt lymphoma.",
    "papillomavirus pairing")],
  c(28, 6, 30)),

Q("Oncogenic and teratogenic viruses", IO3,
  "Besides rubella, which virus is teratogenic, able to cross the placenta and cause permanent defects?",
  ("Cytomegalovirus",
   "Correct. Several viruses cross the placenta, causing developmental disturbances and permanent defects; rubella "
   "and cytomegalovirus are the teratogenic examples. Fetuses infected with cytomegalovirus may show microcephaly, "
   "and survivors can have neurological, hearing and visual problems."),
  [("Epstein-Barr virus",
    "Epstein-Barr virus is oncogenic, linked with Burkitt lymphoma, not teratogenic. The teratogenic pair is rubella "
    "and cytomegalovirus. To tell them apart: a cancer link makes a virus oncogenic; a placental route to fetal defects makes it teratogenic.",
    "oncogenic virus"),
   ("Hepatitis B virus",
    "Hepatitis B virus is a chronic, oncogenic virus linked with hepatic carcinoma. Crossing the placenta to cause "
    "permanent defects is the teratogenic trait of rubella and cytomegalovirus.",
    "oncogenic virus"),
   ("Human herpesvirus 8",
    "Human herpesvirus 8 is oncogenic, linked with Kaposi sarcoma. The teratogenic viruses named are rubella and "
    "cytomegalovirus. To tell them apart: the tumor it causes makes it oncogenic; only rubella and cytomegalovirus are named as crossing the placenta to cause defects.",
    "oncogenic virus")],
  ci(5, 28)),

Q("Oncogenic and teratogenic viruses", IO3,
  "What does an oncogenic virus do to its host cell, unlike a teratogenic virus?",
  ("Transforms it to malignancy",
   "Correct. An oncogenic virus, always a persistent one in these examples, induces transformation of the host "
   "cell to malignancy, as with Epstein-Barr virus and Burkitt lymphoma. A teratogenic virus instead crosses the "
   "placenta and causes developmental defects."),
  [("Crosses the placenta",
    "Crossing the placenta to cause developmental disturbances and permanent defects is what teratogenic viruses "
    "such as rubella do. Oncogenic viruses transform the cell to malignancy.",
    "teratogenic trait"),
   ("Holds it as an episome",
    "An episome, viral DNA (deoxyribonucleic acid) in the nucleus but not integrated, is latent herpesvirus "
    "infection. The oncogenic outcome is transformation of the cell to malignancy.",
    "latent trait"),
   ("Lyses it to release virus",
    "Lysis with release of virus is the lytic outcome of an acute infection, which kills the cell. An oncogenic "
    "virus instead transforms the cell to malignancy. To tell them apart: lysis ends in release of virus, transformation ends in malignancy.",
    "lytic trait")],
  ci(27, 28)),

Q("Oncogenic and teratogenic viruses", IO4,
  "Viral diseases are diagnosed by symptoms, serologic tests and isolation of the virus in which setting?",
  ("Cell or animal culture",
   "Correct. Diagnosis of viral diseases uses symptoms, isolation in cell or animal culture, serological tests for "
   "antibodies and some tests for antigens. Viruses are obligate intracellular parasites, so isolating one needs "
   "living cells or an animal."),
  [("Cell-free nutrient broth",
    "Viruses are obligate intracellular parasites and cannot multiply without host cells, so a cell-free broth "
    "would not isolate one. Isolation is done in cell or animal culture.",
    "bacterial culture habit"),
   ("Blood agar plates",
    "Agar plates without living cells give a virus no host, since viruses are obligate intracellular parasites. "
    "Viral isolation is in cell or animal culture. To tell them apart: any medium without living cells fails for an obligate intracellular parasite.",
    "bacterial culture habit"),
   ("Plain chemical media",
    "A chemical medium with no living cells cannot grow a virus, which needs host cells as an obligate intracellular "
    "parasite. Viral diseases are isolated in cell or animal culture.",
    "nonliving medium")],
  c(28, 8)),

# ---------------------------------------------------------------- DNA (deoxyribonucleic acid) virus groups (3)
Q("DNA (deoxyribonucleic acid) virus groups", IO4,
  "Which DNA (deoxyribonucleic acid) virus group has a single-stranded genome?",
  ("Parvoviruses",
   "Correct. The DNA (deoxyribonucleic acid) viruses that infect humans fall into enveloped double-stranded, "
   "nonenveloped double-stranded and nonenveloped single-stranded groups. The parvoviruses are the single-stranded "
   "group, and they have no envelope."),
  [("Adenoviruses",
    "Adenoviruses are nonenveloped but double-stranded, grouped with the polyomaviruses and papillomaviruses. The "
    "single-stranded group is the parvoviruses. To tell them apart: of the four nonenveloped groups, only one is single-stranded.",
    "nonenveloped double-stranded"),
   ("Polyomaviruses",
    "Polyomaviruses are nonenveloped double-stranded DNA (deoxyribonucleic acid) viruses. Only the parvoviruses "
    "carry a single-stranded genome. To tell them apart: polyomaviruses share their double-stranded class with adenoviruses and papillomaviruses.",
    "nonenveloped double-stranded"),
   ("Herpesviruses",
    "Herpesviruses are enveloped double-stranded DNA (deoxyribonucleic acid) viruses, with poxviruses and "
    "hepadnaviruses. The single-stranded, nonenveloped group is the parvoviruses.",
    "enveloped double-stranded")],
  ci(30, 92)),

Q("DNA (deoxyribonucleic acid) virus groups", IO4,
  "Which of these DNA (deoxyribonucleic acid) virus groups is enveloped?",
  ("Poxviruses",
   "Correct. The enveloped DNA (deoxyribonucleic acid) viruses are the poxviruses, herpesviruses and "
   "hepadnaviruses, all double-stranded. Adenoviruses, polyomaviruses and papillomaviruses are nonenveloped "
   "double-stranded, and parvoviruses nonenveloped single-stranded."),
  [("Adenoviruses",
    "Adenoviruses are nonenveloped double-stranded DNA (deoxyribonucleic acid) viruses. The enveloped groups are "
    "poxviruses, herpesviruses and hepadnaviruses. To tell them apart: no nonenveloped group appears on the enveloped list.",
    "nonenveloped group"),
   ("Papillomaviruses",
    "Papillomaviruses are nonenveloped double-stranded DNA (deoxyribonucleic acid) viruses, listed with "
    "adenoviruses and polyomaviruses. Poxviruses carry an envelope. To tell them apart: papillomaviruses sit on the nonenveloped list.",
    "nonenveloped group"),
   ("Parvoviruses",
    "Parvoviruses are nonenveloped and single-stranded. The enveloped DNA (deoxyribonucleic acid) viruses are "
    "poxviruses, herpesviruses and hepadnaviruses. To tell them apart: the single-stranded group is also nonenveloped.",
    "nonenveloped group")],
  c(31, 30, 92)),

Q("DNA (deoxyribonucleic acid) virus groups", IO4,
  "How are the papillomaviruses classed among the DNA (deoxyribonucleic acid) viruses?",
  ("Nonenveloped, double-stranded",
   "Correct. Papillomaviruses sit with the adenoviruses and polyomaviruses as nonenveloped viruses with a "
   "double-stranded genome. The enveloped groups (poxviruses, herpesviruses, hepadnaviruses) are double-stranded "
   "too, and the parvoviruses are the nonenveloped single-stranded group."),
  [("Enveloped, double-stranded",
    "Enveloped double-stranded is the class of the poxviruses, herpesviruses and hepadnaviruses. Papillomaviruses "
    "have no envelope. To tell them apart: papillomaviruses are listed with adenoviruses and polyomaviruses, which are all nonenveloped.",
    "enveloped group"),
   ("Nonenveloped, single-stranded",
    "Nonenveloped single-stranded is the parvoviruses alone. Papillomaviruses, like adenoviruses and "
    "polyomaviruses, have a double-stranded genome. To tell them apart: only one group is single-stranded, and it is not the papillomaviruses.",
    "parvovirus class"),
   ("Enveloped, single-stranded",
    "No human DNA (deoxyribonucleic acid) virus group is enveloped and single-stranded; every enveloped group is "
    "double-stranded. Papillomaviruses are nonenveloped double-stranded.",
    "nonexistent class")],
  ci(30, 92)),
]

CLUSTERS_A = [
    # lytic release (lysozyme bursts the wall) is named in the filamentous-entry distractors and vice versa
    (1, ["At the end of the phage lytic cycle", "Filamentous phages use no lysozyme"]),
    # the hepatitis B chronic item and the chronic/latent divider share the "detectable in tissue" key fact
    (1, ["Which type of infection does hepatitis B", "Which feature separates a persistent chronic"]),
    # episome vs prophage: the integration item's latent explanation answers the prophage comparison
    (1, ["Which persistent infection may involve integration", "How does latent herpesvirus DNA (deoxyribonucleic acid)"]),
    # the three group items answer one another
    (1, ["Which DNA (deoxyribonucleic acid) virus group has", "How are the papillomaviruses classed"]),
]
