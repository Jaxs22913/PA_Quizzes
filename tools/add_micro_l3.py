#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Microbiology Lecture 3 to the guide, the cram sheet and the Arcade.

Additive and fenced everywhere, with a SEPARATE fence pair per insertion point
-- one shared pair caused the CMS guide splice to drop its sections inside
<nav> and delete the table of contents.
"""
import io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _micro_guide_l3 import SECTION, TOC, TEST

GUIDE = os.path.join(ROOT, "Microbiology Exam 1", "micro-exam-1-study-guide.html")
CRAM = os.path.join(ROOT, "Microbiology Exam 1", "micro-exam-1-cram-sheet.html")
ARCADE = os.path.join(ROOT, "arcade.js")

FENCES = {"toc": ("<!--MICROL3-TOC-->", "<!--/MICROL3-TOC-->"),
          "body": ("<!--MICROL3-BODY-->", "<!--/MICROL3-BODY-->"),
          "cram": ("<!--MICROL3-CRAM-->", "<!--/MICROL3-CRAM-->")}


def splice(text, key, block, before):
    op, cl = FENCES[key]
    fenced = op + block + cl
    pat = re.compile(re.escape(op) + ".*?" + re.escape(cl), re.S)
    if pat.search(text):
        return pat.sub(lambda _: fenced, text, count=1)
    assert text.count(before) == 1, "anchor not unique: %r" % before[:40]
    return text.replace(before, fenced + before)


# --------------------------------------------------------------- cram sheet
CRAM_ROWS = [
 ("L3 · Flora & the Two Definitions", "#3f8a55", [
   ("INFECTION vs DISEASE", "INFECTION = microbes PENETRATE HOST DEFENCES, ENTER TISSUES AND MULTIPLY. DISEASE = ANY DEVIATION FROM HEALTH, microbial or not. Disease is the BROADER term."),
   ("RESIDENT FLORA", "Bacteria, fungi, protozoa, viruses AND ARTHROPODS. Most areas in contact with the outside environment carry them."),
   ("HIGHEST NUMBERS", "LARGE INTESTINE — mainly STRICT or FACULTATIVE ANAEROBES. Bacteria are 10–30% OF FAECAL VOLUME."),
   ("Skin flora", "STAPHYLOCOCCI, CORYNEBACTERIUM, PROPIONIBACTERIUM, YEASTS, MYCOBACTERIUM SMEGMATIS."),
   ("Oral flora", "AEROBIC STREPTOCOCCI are the most common oral residents."),
   ("Respiratory flora", "STAPH. AUREUS, NEISSERIA MENINGITIDIS. The LOWER RESPIRATORY TRACT IS ESSENTIALLY STERILE."),
   ("STERILE SITES", "Heart and blood vessels · kidneys and bladder · brain and spinal column · middle and inner ear · interior of the eyes · BLOOD AND CSF (cerebrospinal fluid) · urine in the kidneys and bladder · AMNIOTIC FLUID."),
   ("The numbers", "~30 TRILLION human cells vs ~38 TRILLION non-human. ~50% of the human genome is NON-HUMAN genetic material."),
 ]),
 ("L3 · Pathogens, Dose & Adhesion", "#1f4d2b", [
   ("TRUE (FRANK) PATHOGEN", "Causes disease in HEALTHY people with NORMAL defences. INFLUENZA, RABIES, PLAGUE BACTERIUM, MALARIAL PROTOZOAN."),
   ("OPPORTUNISTIC PATHOGEN", "Causes disease when defences are COMPROMISED, or when it grows somewhere UNNATURAL to it. SOMETIMES IT IS THE PATIENT'S OWN FLORA."),
   ("WEAKENS HOST DEFENCES", "AGE (elderly, young children, premature infants) · genetic/acquired immunological defects · IMMUNOSUPPRESSING DRUGS AND ORGAN TRANSPLANTS · STRESS · chronic conditions (liver disease, diabetes) · INFLAMMATION · primary infections. Write them as COMORBIDITIES."),
   ("PORTALS OF ENTRY", "SKIN · GASTROINTESTINAL · RESPIRATORY · UROGENITAL · CONJUNCTIVA · PREGNANCY AND BIRTH. EXOGENOUS (outside) or ENDOGENOUS (within)."),
   ("INFECTIOUS DOSE (ID50)", "MINIMUM microbes needed to infect 50% of a population. SMALL ID50 = GREATER VIRULENCE."),
   ("The ID50 range", "MEASLES 1 PARTICLE · TB 10 bacteria · smallpox 10–100 · plague 100–500 · SARS-CoV-1 ~280 · influenza A ~790 · gonorrhoea 1,000 · CHOLERA 100,000,000."),
   ("ADHESION MECHANISMS", "FIMBRIAE (attachment pili) · FLAGELLA · ADHESIVE SLIMES/CAPSULES (dextran slime, glycocalyx) · SUCTION DISKS of protozoans · VIRAL SPIKE or CAPSID PROTEINS · HOOKS AND BARBS of helminths and insect larvae."),
 ]),
 ("L3 · ★ ENDOTOXIN vs EXOTOXIN", "#c2903a", [
   ("ENDOTOXIN — what", "LIPID A OF THE LIPOPOLYSACCHARIDE."),
   ("ENDOTOXIN — who", "GRAM-NEGATIVE ONLY. It is part of their outer membrane."),
   ("ENDOTOXIN — released how", "FROM LYSED OR DAMAGED bacteria — i.e. when the organism DIES."),
   ("EXOTOXIN — what", "PROTEINS."),
   ("EXOTOXIN — who", "Certain GRAM-POSITIVE AND GRAM-NEGATIVE bacteria."),
   ("EXOTOXIN — released how", "SECRETED BY LIVING bacteria."),
   ("The one-liner", "ENDO = STRUCTURAL LIPID FROM A DEAD GRAM-NEGATIVE. EXO = PROTEIN SECRETED BY A LIVING ORGANISM, EITHER GRAM."),
   ("EXOENZYMES", "Attack host defences to allow DEEPER INVASION: MUCINASE, HYALURONIDASE, COAGULASE, BACTERIAL KINASES."),
   ("TOXIGENICITY", "Capacity to produce toxins, grouped by TISSUE TARGETED: NEUROTOXINS, ENTEROTOXINS, HEMOTOXINS, NEPHROTOXINS."),
   ("ANTIPHAGOCYTIC FACTORS", "LEUKOCIDINS destroy leukocytes (-cidin = to kill). CAPSULES avoid phagocytosis or resist digestion inside the phagocyte."),
 ]),
 ("L3 · Patterns & Manifestations", "#3f8a55", [
   ("LOCALIZED", "Confined to a specific tissue. BOILS, WARTS."),
   ("SYSTEMIC", "Spreads to SEVERAL SITES via the bloodstream. MEASLES, CHICKEN POX, ANTHRAX, RABIES."),
   ("FOCAL", "An agent BREAKS LOOSE from a local site and spreads."),
   ("MIXED", "SEVERAL MICROBES growing SIMULTANEOUSLY at one site."),
   ("PRIMARY / SECONDARY", "PRIMARY = the initial infection. SECONDARY = a DIFFERENT microbe complicating it, e.g. bacterial lung infection on top of a viral URI."),
   ("SUPERINFECTION", "A secondary infection from DISRUPTION OF THE NATURAL MICROFLORA. Classic: ANTIBIOTICS FOR STREP THROAT → VAGINAL YEAST INFECTION. IF THE STEM MENTIONS ANTIBIOTICS, IT IS A SUPERINFECTION."),
   ("SIGN", "OBJECTIVE evidence noted by an OBSERVER; often more precise and MAY BE MEASURED. Example: INFLAMED PHARYNX."),
   ("SYMPTOM", "SUBJECTIVE evidence SENSED AND DESCRIBED BY THE PATIENT. Example: SORE THROAT."),
   ("SEQUELAE", "LONG-TERM OR PERMANENT damage: PARALYSIS from polio · BLINDNESS from gonococcal conjunctivitis · STERILITY from syphilis · DEAFNESS from meningitis · ARTHRITIS from Lyme disease."),
   ("PORTAL OF EXIT", "How pathogens DEPART the host — and therefore how they reach the next one."),
 ]),
 ("L3 · Reservoirs & Transmission", "#1f4d2b", [
   ("RESERVOIR", "The PRIMARY HABITAT from which a pathogen ORIGINATES. Living or nonliving."),
   ("Living reservoirs", "Someone with an OBVIOUS ACTIVE INFECTION is likely contagious. ASYMPTOMATIC CARRIERS may be HUMANS OR ANIMALS."),
   ("PASSIVE CARRIERS", "MEDICAL OR DENTAL PERSONNEL — carrying it without being infected."),
   ("VECTORS", "A LIVE ANIMAL that transmits disease: MOSQUITOES, FLEAS, TICKS; also FLIES, FRUIT FLIES, COCKROACHES."),
   ("NONLIVING RESERVOIRS", "SOIL AND WATER."),
   ("ZOONOSIS", "Animal infections spread to humans and vice versa. Can be BACTERIAL, VIRAL, FUNGAL OR PROTOZOAN. CANNOT BE ELIMINATED WITHOUT ERADICATING THE ANIMAL RESERVOIR."),
   ("DIRECT transmission", "HORIZONTAL (kissing, sexual) · VERTICAL (MOTHER TO CHILD, transplacental or vaginal birth) · DROPLET (saliva, vomit, faeces, blood) · BIOLOGICAL VECTORS."),
   ("INDIRECT transmission", "VEHICLES and FOMITES (inanimate objects), and AIRBORNE DROPLET NUCLEI."),
 ]),
 ("L3 · ★ NOSOCOMIAL INFECTIONS", "#c2903a", [
   ("DEFINITION", "HAI = HOSPITAL-ACQUIRED INFECTION. ACQUIRED OR DEVELOPING DURING A HOSPITAL STAY. May PROLONG THE STAY OR END IN DEATH."),
   ("MOST COMMON SITES", "URINARY TRACT · RESPIRATORY TRACT · SURGICAL INCISIONS."),
   ("MOST COMMON ORGANISMS", "Gram-negative: E. COLI, PSEUDOMONAS, KLEBSIELLA. Gram-positive: STAPHYLOCOCCI, STREPTOCOCCI. Fungi: YEASTS. The wider list goes by ESKAPE."),
   ("MITIGATION — the answer", "UNIVERSAL PRECAUTIONS for sample collection and patient care, based on the assumption that ALL PATIENT SPECIMENS ARE POSSIBLY INFECTIOUS. You do not decide which to be careful with."),
   ("The fomite link", "An INANIMATE OBJECT carries the organism between patients — which is why the same few organisms keep reappearing."),
 ]),
 ("L3 · Epidemiology & Koch", "#3f8a55", [
   ("EPIDEMIOLOGY", "Study of the FREQUENCY AND DISTRIBUTION of disease in human populations."),
   ("REPORTABLE / NOTIFIABLE", "Must be reported to PUBLIC HEALTH AUTHORITIES. In the US the CDC publishes the MORBIDITY AND MORTALITY WEEKLY REPORT."),
   ("PREVALENCE", "TOTAL EXISTING cases against the entire population, usually A PERCENTAGE."),
   ("INCIDENCE", "NEW cases OVER A TIME PERIOD, against the general healthy population."),
   ("MORTALITY RATE", "DEATHS due to a disease, PER 100,000."),
   ("MORBIDITY RATE", "CASES — people afflicted — PER 100,000."),
   ("THE 100-YEAR TREND", "DEATH RATE DROPPED while MORBIDITY REMAINED RELATIVELY HIGH. People stopped DYING of these; they did not stop GETTING them."),
   ("ENDEMIC", "STEADY frequency over a long period in a particular LOCATION, often because the RESERVOIR IS PRESENT."),
   ("SPORADIC", "OCCASIONAL cases at IRREGULAR intervals."),
   ("EPIDEMIC", "Prevalence INCREASING BEYOND WHAT IS EXPECTED for that population."),
   ("PANDEMIC", "A GLOBAL epidemic."),
   ("KOCH'S POSTULATES (1880s)", "1. FIND the microbe in EVERY CASE. 2. ISOLATE and CULTIVATE IT ARTIFICIALLY. 3. INOCULATE a susceptible healthy subject. 4. RE-ISOLATE from the new subject."),
   ("WHERE KOCH FAILS", "Organisms that CANNOT BE CULTIVATED ARTIFICIALLY — M. LEPRAE and LEGIONELLA PNEUMOPHILA. VIRUSES AND PRIONS break all the old rules."),
   ("MOLECULAR KOCH (Falkow, 1988)", "1. The PROPERTY should ASSOCIATE WITH PATHOGENIC STRAINS. 2. INACTIVATING the gene should cause MEASURABLE LOSS OF VIRULENCE. 3. REVERTING it should RESTORE pathogenicity. The shift is FROM THE ORGANISM TO THE GENE."),
 ]),
]


def cram_section(title, colour, rows, sid):
    body = "\n".join('          <tr><td class="h">%s</td><td>%s</td></tr>' % (a, b)
                     for a, b in rows)
    return """
  <section class="topic" id="%s" style="--acc:%s;--acc-bg:#e8f4ea;--acc-zebra:#f2f9f4;--acc-ink:#1f4d2b">
    <div class="shead"><span class="dot" style="background:%s"></span><h2>%s</h2></div>
    <div class="scroll">
      <table>
        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>
        <tbody>
%s
        </tbody>
      </table>
    </div>
  </section>
""" % (sid, colour, colour, title, body)


# ------------------------------------------------------------------- arcade
DECK_ID = "mb-microbe-human-interactions"
CARDS = [
 ["Define infection.", "Pathogenic microbes penetrate host defences, enter tissues and multiply."],
 ["Define disease.", "Any deviation from health, which may or may not be caused by microbes."],
 ["Which is the broader term, infection or disease?", "Disease."],
 ["What does resident flora include?", "Bacteria, fungi, protozoa, viruses and arthropods."],
 ["Which body site has the highest bacterial numbers?", "The large intestine."],
 ["Which organisms dominate the large intestine?", "Strict and facultative anaerobes."],
 ["What share of faecal volume is bacteria?", "10 to 30 percent."],
 ["Most common oral residents?", "Aerobic streptococci."],
 ["Notable skin microflora?", "Staphylococci, Corynebacterium, Propionibacterium, yeasts and Mycobacterium smegmatis."],
 ["Which flora does the deck name in the respiratory tract?", "Staphylococcus aureus and Neisseria meningitidis."],
 ["Is the lower respiratory tract sterile?", "Essentially yes, and bad things happen if it is not."],
 ["Name two normally sterile fluids.", "Blood and cerebrospinal fluid."],
 ["Is amniotic fluid sterile?", "Yes, normally."],
 ["How many human cells in an average adult male body?", "About 30 trillion."],
 ["How many non-human cells?", "About 38 trillion."],
 ["What share of the human genome is foreign genetic material?", "About 50 percent, from viral remnants and transposons."],
 ["What is a true, or frank, pathogen?", "One capable of causing disease in healthy people with normal defences."],
 ["Give examples of true pathogens.", "Influenza and rabies viruses, the plague bacterium, and the malarial protozoan."],
 ["What is an opportunistic pathogen?", "One that causes disease when defences are compromised, or when it grows somewhere unnatural to it."],
 ["Which factor does the deck call a biggie for host defence?", "Immune status."],
 ["Which ages weaken host defences?", "The elderly, young children and premature infants."],
 ["What single word covers most of the host-weakening factors?", "Comorbidities."],
 ["List the portals of entry.", "Skin, gastrointestinal tract, respiratory tract, urogenital tract, conjunctiva, and pregnancy and birth."],
 ["What does exogenous mean for an infectious agent?", "It comes from outside the body."],
 ["What does endogenous mean for an infectious agent?", "It comes from within the body."],
 ["Define infectious dose.", "The minimum number of microbes or viral particles required for infection to occur."],
 ["What does ID50 mean?", "The dose sufficient to cause infection in 50 percent of a given population."],
 ["Does a small ID50 mean more or less virulence?", "More virulence, and a greater degree of pathogenicity."],
 ["Infectious dose for measles?", "One virus particle."],
 ["Infectious dose for tuberculosis?", "Ten bacteria."],
 ["Infectious dose for cholera?", "One hundred million bacterial cells."],
 ["Which adhesion structures are attachment pili?", "Fimbriae."],
 ["Which adhesion mechanism belongs to protozoans?", "Suction disks."],
 ["Which adhesion mechanism belongs to viruses?", "Spike or capsid proteins."],
 ["Which adhesion mechanism belongs to helminths and insect larvae?", "Hooks and barbs."],
 ["Name two bacterial adhesive slimes.", "Dextran slime and glycocalyx."],
 ["What do exoenzymes do?", "Attack host defences to allow deeper invasion."],
 ["Name four exoenzymes.", "Mucinase, hyaluronidase, coagulase and bacterial kinases."],
 ["What is toxigenicity?", "The capacity to produce toxins."],
 ["Which four toxin categories does the deck name?", "Neurotoxins, enterotoxins, hemotoxins and nephrotoxins."],
 ["What is an endotoxin, chemically?", "Lipid A of the lipopolysaccharide."],
 ["Which bacteria produce endotoxin?", "Gram-negative bacteria only."],
 ["How is endotoxin released?", "From lysed or damaged bacteria."],
 ["What is an exotoxin, chemically?", "A protein."],
 ["Which bacteria produce exotoxins?", "Certain living gram-positive and gram-negative bacteria."],
 ["How is exotoxin released?", "Secreted by living bacteria."],
 ["What do leukocidins do?", "Destroy leukocytes."],
 ["What does the suffix -cidin mean?", "To kill."],
 ["How do capsules help a pathogen?", "They allow it to avoid phagocytosis or resist digestion inside a phagocyte."],
 ["Define a localized infection.", "Microbes enter and remain confined to a specific tissue."],
 ["Give examples of localized infection.", "Boils and warts."],
 ["Define a systemic infection.", "It spreads to several sites and tissue fluids, usually through the bloodstream."],
 ["Give examples of systemic infection.", "Measles, chicken pox, anthrax and rabies."],
 ["Define a focal infection.", "An agent breaks loose from a local site and spreads."],
 ["Define a mixed infection.", "Several microbes grow simultaneously at the infection site."],
 ["Define a secondary infection.", "Another infection by a different microbe that complicates the initial one."],
 ["Define a superinfection.", "A secondary infection resulting from disruption of the natural microflora."],
 ["Give the classic superinfection example.", "Antibiotics for strep throat producing a vaginal yeast infection."],
 ["What is a sign?", "Objective evidence of disease noted by an observer, often measurable."],
 ["What is a symptom?", "Subjective evidence of disease sensed and described by the patient."],
 ["Give the deck's sign and symptom pair.", "An inflamed pharynx is the sign; a sore throat is the symptom."],
 ["What are sequelae?", "Long-term or permanent damage to tissues or organs."],
 ["Give three examples of sequelae.", "Paralysis from polio, deafness from meningitis, and arthritis from Lyme disease."],
 ["What is a portal of exit?", "How pathogens depart the host."],
 ["Define a reservoir of infection.", "The primary habitat from which a pathogen originates."],
 ["What is a passive carrier?", "Someone such as medical or dental personnel, carrying the organism without being infected."],
 ["Can asymptomatic carriers be animals?", "Yes, humans or animals."],
 ["What is a vector?", "A live animal that transmits infectious disease."],
 ["Name vectors from the deck.", "Mosquitoes, fleas, ticks, flies, fruit flies and cockroaches."],
 ["Name the nonliving reservoirs.", "Soil and water."],
 ["What is a zoonosis?", "An infection of animals that can spread to humans, and vice versa."],
 ["Can a zoonosis be eliminated?", "Not without also eradicating the animal reservoir."],
 ["Which organism types can cause zoonoses?", "Bacterial, viral, fungal or protozoan."],
 ["What is vertical transmission?", "Mother to child, transplacental or during vaginal birth."],
 ["What is horizontal transmission?", "Direct personal contact such as kissing or sexual contact."],
 ["What is a fomite?", "An inanimate object that carries infection."],
 ["Which transmission route are droplet nuclei?", "Airborne, and classed as indirect."],
 ["Define a nosocomial infection.", "A disease acquired or developing during a hospital stay."],
 ["What does HAI stand for?", "Hospital-acquired infection."],
 ["Which sites do nosocomial infections most commonly involve?", "Urinary tract, respiratory tract and surgical incisions."],
 ["Which gram-negative organisms are most common in nosocomial infection?", "Escherichia coli, Pseudomonas and Klebsiella."],
 ["Which acronym covers the wider nosocomial organism list?", "ESKAPE."],
 ["What assumption underlies universal precautions?", "That all patient specimens are possibly infectious."],
 ["What are the consequences of nosocomial infection?", "It may prolong the hospital stay or end in death."],
 ["Define epidemiology.", "The study of the frequency and distribution of disease in human populations."],
 ["What is a reportable disease?", "One that must be reported to public health authorities."],
 ["Who publishes the Morbidity and Mortality Weekly Report?", "The Centers for Disease Control and Prevention."],
 ["What does prevalence measure?", "Total existing cases against the entire population."],
 ["What does incidence measure?", "New cases over a certain time period."],
 ["What does mortality rate measure, and how is it expressed?", "Deaths due to a disease, per one hundred thousand."],
 ["What does morbidity rate measure, and how is it expressed?", "Cases of a disease, per one hundred thousand."],
 ["What has happened to death and morbidity rates over the last century?", "The death rate dropped while morbidity remained relatively high."],
 ["Define endemic.", "A relatively steady frequency over a long period in a particular geographic location."],
 ["Define sporadic.", "Occasional cases reported at irregular intervals."],
 ["Define epidemic.", "Prevalence increasing beyond what is expected for that population."],
 ["Define pandemic.", "A global epidemic."],
 ["First of Koch's postulates?", "Find evidence of the microbe in every case of the disease."],
 ["Second of Koch's postulates?", "Isolate it and cultivate it artificially in the laboratory."],
 ["Third of Koch's postulates?", "Inoculate a susceptible healthy subject and observe the disease."],
 ["Fourth of Koch's postulates?", "Re-isolate the agent from the newly infected subject."],
 ["Which two bacteria does the deck name as breaking Koch's postulates?", "Mycobacterium leprae and Legionella pneumophila."],
 ["Which agents routinely break all the old microbiology rules?", "Viruses and prions."],
 ["Who published the molecular Koch's postulates, and when?", "Stanley Falkow, in 1988."],
 ["First molecular Koch's postulate?", "The property should be associated with pathogenic strains or species."],
 ["Second molecular Koch's postulate?", "Inactivating the associated gene should cause a measurable loss of virulence."],
 ["Third molecular Koch's postulate?", "Reverting the mutated gene should restore pathogenicity."],
]

ICON = ('<circle cx="12" cy="12" r="9"/><circle cx="9" cy="10" r="1.5"/>'
        '<circle cx="15" cy="14" r="1.5"/><path d="M7 15c2-1 3-3 6-3"/>')


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def main():
    # ---- guide ----
    t = io.open(GUIDE, encoding="utf-8").read()
    n0 = len(t)
    t = splice(t, "toc", "\n" + TOC, "</nav>")
    t = splice(t, "body", "\n" + SECTION + "\n", "</main>")
    anchor = "  var TEST_YOURSELF = {\n"
    assert t.count(anchor) == 1
    if "    microbehuman: [" not in t:
        t = t.replace(anchor, anchor + TEST)
    io.open(GUIDE, "w", encoding="utf-8").write(t)
    nav_a, nav_b = t.index('<nav class="toc">'), t.index("</nav>")
    main_a, main_b = t.index("<main>"), t.index("</main>")
    i = t.index('<section class="deck" id="microbe-human"')
    assert main_a < i < main_b and not (nav_a < i < nav_b), "section landed outside <main>"
    assert nav_a < t.index('href="#mh-flora"') < nav_b, "toc link outside <nav>"
    assert 'href="#gm-molecular"' in t and 'href="#ar-history"' in t, "original toc lost"
    print("guide %d -> %d bytes" % (n0, len(t)))

    # ---- cram ----
    c = io.open(CRAM, encoding="utf-8").read()
    n0 = len(c)
    blocks = "".join(cram_section(ti, col, rows, "micro-l3-%d" % k)
                     for k, (ti, col, rows) in enumerate(CRAM_ROWS, 1))
    c = splice(c, "cram", blocks, "\n  <footer>")
    io.open(CRAM, "w", encoding="utf-8").write(c)
    blk = c[c.index(FENCES["cram"][0]):c.index(FENCES["cram"][1])]
    assert blk.count("<section") == blk.count("</section>") == len(CRAM_ROWS)
    assert c.index(FENCES["cram"][1]) < c.index("<footer>")
    print("cram %d -> %d bytes (%d sections, %d rows)"
          % (n0, len(c), len(CRAM_ROWS), blk.count('<td class="h">')))

    # ---- arcade ----
    a = io.open(ARCADE, encoding="utf-8").read()
    n0 = len(a)
    if '{ id: "%s",' % DECK_ID not in a:
        anchor_deck = '  { id: "mb-general-microbiology",'
        assert a.count(anchor_deck) == 1
        deck = ('  { id: "%s", name: "Microbe-Human Interactions", color: "accent3",\n'
                "    icon: '%s',\n    cards: [\n%s\n    ]},\n\n"
                % (DECK_ID, ICON,
                   "\n".join('      ["%s", "%s"],' % (esc(q), esc(ans)) for q, ans in CARDS)))
        a = a.replace(anchor_deck, deck + anchor_deck)
    old_g = '{ id: "exam1", name: "Exam 1", deckIds: ["mb-general-microbiology", "mb-antibiotics-resistance"] }'
    new_g = ('{ id: "exam1", name: "Exam 1", deckIds: ["mb-general-microbiology", '
             '"mb-antibiotics-resistance", "%s"] }' % DECK_ID)
    if old_g in a:
        a = a.replace(old_g, new_g)
    io.open(ARCADE, "w", encoding="utf-8").write(a)
    assert '{ id: "%s",' % DECK_ID in a, "deck missing from the flat list"
    grp = a.split('name: "Microbiology"')[1][:400]
    assert DECK_ID in grp, "deck missing from the Microbiology grouping"
    print("arcade %d -> %d bytes (%d cards, in list and grouping)" % (n0, len(a), len(CARDS)))


if __name__ == "__main__":
    main()
