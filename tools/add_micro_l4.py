#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Microbiology Lecture 4 to the guide, the cram sheet and the Arcade.

Additive and fenced everywhere, with a SEPARATE fence pair per insertion point
-- one shared pair caused the CMS guide splice to drop its sections inside
<nav> and delete the table of contents.
"""
import io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _micro_guide_l4 import SECTION, TOC, TEST

GUIDE = os.path.join(ROOT, "Microbiology Exam 1", "micro-exam-1-study-guide.html")
CRAM = os.path.join(ROOT, "Microbiology Exam 1", "micro-exam-1-cram-sheet.html")
ARCADE = os.path.join(ROOT, "arcade.js")

FENCES = {"toc": ("<!--MICROL4-TOC-->", "<!--/MICROL4-TOC-->"),
          "body": ("<!--MICROL4-BODY-->", "<!--/MICROL4-BODY-->"),
          "cram": ("<!--MICROL4-CRAM-->", "<!--/MICROL4-CRAM-->")}


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
 ("L4 \u00b7 The Chain of Infection", "#3f8a55", [
   ("THE SIX LINKS, IN ORDER", "1. INFECTIOUS AGENT \u2192 2. RESERVOIR \u2192 3. PORTAL OF EXIT \u2192 4. MODE OF TRANSMISSION \u2192 5. PORTAL OF ENTRY \u2192 6. SUSCEPTIBLE HOST. Break ANY link and transmission stops."),
   ("LIVING reservoirs", "HUMANS, ANIMALS \u2014 and the deck marks PLANTS and FUNGI with a question mark."),
   ("NON-LIVING reservoirs", "SOIL, WATER, AIR, FOOD and FOMITES."),
   ("ACTIVE carrier", "IS INFECTED, may or may not show symptoms. TYPHOID MARY (Mary Mallon) carried SALMONELLA TYPHI asymptomatically."),
   ("PASSIVE carrier", "IS <b>NOT</b> INFECTED but still transmits \u2014 the healthcare or food worker with poor hand hygiene. THE DISTINCTION IS WHETHER THEY ARE INFECTED."),
 ]),
 ("L4 \u00b7 Zoonoses & Vectors", "#3f8a55", [
   ("ZOONOSIS", "An ANIMAL infection that spreads to humans AND THE REVERSE. Can be BACTERIAL, VIRAL, FUNGAL or PROTOZOAN \u2014 all four."),
   ("WHY THEY CANNOT BE ERADICATED", "You would have to eradicate the ANIMAL RESERVOIR too \u2014 harder with MULTIPLE reservoirs, and worse if the pathogen lies dormant as a FUNGAL SPORE or PROTOZOAN CYST."),
   ("HUMANS IN PLAGUE / ANTHRAX", "The ACCIDENTAL HOST."),
   ("RABIES", "Reservoir MAMMALS \u00b7 BITE/SALIVA \u00b7 human-to-human RARE (organ transplantation)."),
   ("INFLUENZA", "Reservoir BIRDS and PIGS \u00b7 respiratory droplet and contact \u00b7 human-to-human YES."),
   ("EBOLA / MARBURG / NIPAH", "Reservoir FRUIT BATS (Ebola also small primates) \u00b7 BODY FLUIDS \u00b7 human-to-human YES."),
   ("COMMONEST ZOONOSIS", "<b>RABIES in the UNITED STATES; MALARIA WORLDWIDE.</b> From the recording, not a slide."),
   ("VECTOR vs RESERVOIR", "VECTOR = a LIVING thing that TRANSMITS (mosquitoes, fleas, ticks, flies, cockroaches). RESERVOIR HARBOURS it. Malaria: birds may be the reservoir, MOSQUITOES the vector."),
 ]),
 ("L4 \u00b7 Modes of Transmission", "#3f8a55", [
   ("DIRECT \u2014 VERTICAL", "MOTHER TO CHILD."),
   ("DIRECT \u2014 HORIZONTAL", "Usually MUCOUS MEMBRANE contact \u2014 sexual contact, kissing. Droplets: coughing, sneezing, saliva, blood, sweat, tears."),
   ("INDIRECT contact", "Onto an INANIMATE SURFACE first \u2014 that is FOMITE transmission."),
   ("VEHICLE \u2014 FOOD", "GI ILLNESS is the commonest result."),
   ("VEHICLE \u2014 WATER", "Drinking water, plus POOLS, SPAS and WATER PARKS."),
   ("VEHICLE \u2014 SOIL", "Contaminates produce, HANDS and FINGERNAILS; pinworms in children."),
   ("VEHICLE \u2014 AIR", "Usually an INDOOR phenomenon. Ventilation, filtration and CROWDING matter."),
 ]),
 ("L4 \u00b7 Fomites & Nosocomial Infection", "#3f8a55", [
   ("FOMITE", "A NON-LIVING SURFACE OR OBJECT that may transmit pathogens."),
   ("HAI consequences", "LONGER STAYS, long-term disability, PREVENTABLE DEATHS, expense, risk to safety AND quality of care."),
   ("HIGHEST-RISK groups", "IMMUNOCOMPROMISED, paediatric, geriatric, HIV, OPEN WOUNDS or BURNS, surgical patients."),
   ("CATHETERS", "Indwelling devices are the problem because STAPH. AUREUS and STAPH. EPIDERMIDIS form BIOFILMS."),
   ("Clinical fomites", "Scalpels, syringes, CATHETERS, bed rails, gurneys, PHONES, remotes, KEYBOARDS, floors, mops, pillows, bedding, CURTAINS, STETHOSCOPES, NECKTIES, stuffed animals, greeting cards, FLOWERS."),
   ("NOT JUST HOSPITALS", "A public restroom, HOTEL ROOM, cruise ship cabin or AEROPLANE TRAY TABLE is a fomite-filled room too."),
 ]),
 ("L4 \u00b7 The Studies", "#3f8a55", [
   ("BIRTHDAY CAKE (Dawson 2017)", "Blowing out candles \u2192 <b>15\u00d7 MORE bacteria</b> on the frosting vs the no-blow control. <b>THEY NEVER IDENTIFIED THE ORGANISMS.</b> Said nothing about fungi or VIRUSES in saliva."),
   ("THE CANDLE TEST", "Try blowing out a candle WHILE WEARING a face covering \u2014 the droplet-size demonstration."),
   ("KEYBOARDS (Ide 2019)", "<b>75 studies</b> reviewed. Keyboards, mice/pads, tablets. Grew COLIFORMS (E. coli) and <b>MRSA</b>."),
   ("VIRAL FOMITES (Boone & Gerba 2007)", "1.7M deaths/yr diarrhoeal, 1.5M respiratory. <b>VIRUSES CAUSE ~60% OF HUMAN INFECTIONS</b> and CANNOT be cured with antibiotics. CROWDED INDOOR SPACES consistently INCREASE morbidity and mortality."),
   ("PATIENT ITEMS (Kanamori 2017)", "Soap/sanitiser dispensers, humidifiers, nebulisers, pressure transducers, STETHOSCOPES, suction, THERMOMETERS, ULTRASOUND PROBE AND GEL, BP monitors, IV pumps, telemetry wires."),
   ("CFU", "COLONY-FORMING UNIT \u2014 used because you cannot know if a colony began from ONE cell or a THOUSAND. Reported per GRAM or per mL."),
 ]),
 ("L4 \u00b7 Disinfection & History", "#3f8a55", [
   ("FIVE BEST PRACTICES, in order", "1. STANDARDISE cleaning policy \u00b7 2. Select <b>EPA-REGISTERED</b> disinfectants \u00b7 3. Educate <b>ALL</b> staff INCLUDING environmental services \u00b7 4. MONITOR compliance with feedback \u00b7 5. <b>NO-TOUCH</b> decontamination technology."),
   ("SEMMELWEIS, 1840s", "Handwashing with <b>CHLORINE</b> solution, by obstetricians."),
   ("LISTER, 1860s", "Handwashing and wound treatment with <b>CARBOLIC ACID</b>."),
   ("CHEMICAL AGENTS", "Bleach, quaternary ammonium salts, phenolics \u2014 work ONLY at the <b>CORRECT CONCENTRATION</b> and for <b>ADEQUATE CONTACT TIME</b>. They are toxic."),
   ("OZONE / H2O2 / STEAM", "<b>THE ROOM MUST BE VACANT</b> to reduce harm to humans. Time-consuming; can damage surfaces and devices."),
   ("COATINGS", "From MARINE ANTI-FOULING paint (copper, arsenic, mercury, tin since the 1960s). <b>ANTI-FOULING PREVENTS ATTACHMENT; ANTIMICROBIAL KILLS.</b> Must be NONTOXIC, cost effective, available, STABLE and DURABLE."),
 ]),
 ("L4 \u00b7 Fomites & Resistance", "#3f8a55", [
   ("WHAT DRIVES MDR", "<b>EXTENSIVE ANTIBIOTIC USE.</b> MDR, XDR and TDR strains \u2014 MRSA and CRKP \u2014 are especially problematic in hospitals."),
   ("BIOFILM", "A POLYMICROBIAL NETWORK resistant to CLEANING, HEAT <b>and</b> ANTIMICROBIAL DRUGS. Staphylococcus and Pseudomonas form them."),
   ("THE CORE ARGUMENT", "<b>A fomite carrying a persistent pathogen CANNOT BE TOLD APART FROM A CLEAN SURFACE.</b>"),
   ("ANTISEPTIC STUDY (Lompo 2023)", "Burkina Faso and Benin. <b>LIQUID SOAP most contaminated \u2014 51 of 69 samples.</b> Risks: inconsistent preparation, RECYCLED soft-drink bottles, broken pumps, <b>TOPPING UP</b>."),
   (">10,000 CFU/mL organisms", "<b>KLEBSIELLA PNEUMONIAE, PSEUDOMONAS AERUGINOSA, ACINETOBACTER</b> \u2014 all GRAM-NEGATIVE. From MATERNITY, NEONATOLOGY, SURGERY and INTERNAL MEDICINE."),
   ("CONJUGATION", "<b>Donor and recipient NEED NOT be the same genus or species.</b> Once a cell gains a resistance plasmid, <b>ALL its offspring have it</b>."),
   ("TRANSFORMATION", "COMPETENT cells take up DNA fragments FROM THE ENVIRONMENT. A lesser factor."),
   ("TRANSDUCTION", "Requires a <b>BACTERIOPHAGE</b> acting as the vector."),
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


DECK_ID = "mb-transmission"
CARDS = [
 ("How many links are in the chain of infection?", "Six."),
 ("What is the first link in the chain of infection?", "The infectious agent."),
 ("What is the last link in the chain of infection?", "A susceptible host."),
 ("Which link follows the portal of exit?", "The mode of transmission."),
 ("Name the non-living reservoirs of infection.", "Soil, water, air, food and fomites."),
 ("Name the living reservoirs of infection.", "Humans, animals, and possibly plants and fungi."),
 ("What is an active carrier?", "Someone infected, who may or may not have symptoms."),
 ("What is a passive carrier?", "Someone not infected who still transmits pathogens."),
 ("Which organism did Typhoid Mary carry?", "Salmonella typhi, without symptoms."),
 ("What is a zoonosis?", "An animal infection that can spread to humans, and the reverse."),
 ("Which four classes of organism cause zoonoses?", "Bacterial, viral, fungal and protozoan."),
 ("Why can zoonoses not be eradicated?", "The animal reservoir would have to go too."),
 ("What role do humans usually play in plague and anthrax?", "The accidental host."),
 ("Reservoir and transmission of rabies?", "Mammals; bite and saliva."),
 ("Reservoirs of influenza?", "Birds and pigs."),
 ("Reservoir of Ebola, Marburg and Nipah?", "Fruit bats."),
 ("Commonest zoonosis in the United States?", "Rabies."),
 ("Commonest zoonosis worldwide?", "Malaria."),
 ("What is a vector?", "A living thing that transmits disease."),
 ("How does a reservoir differ from a vector?", "The reservoir harbours it; the vector delivers it."),
 ("What is vertical transmission?", "Mother to child."),
 ("What is horizontal transmission?", "Usually mucous membrane contact."),
 ("What is indirect contact transmission?", "Onto a surface first - a fomite."),
 ("Commonest illness from food as a vehicle?", "Gastrointestinal illness."),
 ("Airborne transmission is usually what kind of phenomenon?", "An indoor one."),
 ("What is a fomite?", "A non-living surface or object that transmits pathogens."),
 ("What does HAI stand for?", "Hospital-acquired infection."),
 ("Why are indwelling catheters a problem?", "Staphylococci on them form biofilms."),
 ("What is a biofilm?", "A polymicrobial network resistant to cleaning, heat and drugs."),
 ("How much more bacteria after blowing out birthday candles?", "About fifteen times."),
 ("What did the birthday-cake authors fail to do?", "Identify the organisms they cultured."),
 ("What is the candle test?", "Blowing out a candle while wearing a face covering."),
 ("How many studies did the keyboard review cover?", "Seventy-five."),
 ("Which resistant organism grew from keyboards?", "MRSA."),
 ("What share of human infections are viral?", "About sixty per cent."),
 ("Effect of crowded indoor environments?", "They increase morbidity and mortality."),
 ("What does CFU stand for?", "Colony-forming unit."),
 ("Why is the unit CFU rather than cells?", "A colony may start from one cell or a thousand."),
 ("Which agency registers hospital disinfectants?", "The Environmental Protection Agency."),
 ("Who must be trained in cleaning policy?", "All staff, including environmental services."),
 ("What did Semmelweis introduce, and when?", "Chlorine handwashing, in the 1840s."),
 ("What did Lister use, and when?", "Carbolic acid, in the 1860s."),
 ("Two conditions for a chemical disinfectant to work?", "Correct concentration and adequate contact time."),
 ("Why must a room be empty for ozone or hydrogen peroxide?", "To reduce harm to humans."),
 ("Anti-fouling against antimicrobial coating?", "Anti-fouling prevents attachment; antimicrobial kills."),
 ("What drove the evolution of multi-drug resistance?", "Extensive antibiotic use."),
 ("Why are contaminated fomites so dangerous?", "They look exactly like clean surfaces."),
 ("Most contaminated product in the West African study?", "Liquid soap - 51 of 69 samples."),
 ("Which organisms grew above 10,000 CFU per millilitre?", "Klebsiella, Pseudomonas and Acinetobacter."),
 ("Why is conjugation so significant for resistance?", "Donor and recipient need not be the same species."),
 ("What happens to offspring of a cell with a resistance plasmid?", "All of them carry it too."),
 ("Which gene transfer needs a bacteriophage?", "Transduction."),
 ("What do competent cells do?", "Take up DNA fragments from the environment."),
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
    if "    transmission: [" not in t:
        t = t.replace(anchor, anchor + TEST)
    io.open(GUIDE, "w", encoding="utf-8").write(t)
    nav_a, nav_b = t.index('<nav class="toc">'), t.index("</nav>")
    main_a, main_b = t.index("<main>"), t.index("</main>")
    i = t.index('<section class="deck" id="transmission"')
    assert main_a < i < main_b and not (nav_a < i < nav_b), "section landed outside <main>"
    assert nav_a < t.index('href="#tx-chain"') < nav_b, "toc link outside <nav>"
    assert 'href="#gm-molecular"' in t and 'href="#ar-history"' in t, "original toc lost"
    print("guide %d -> %d bytes" % (n0, len(t)))

    # ---- cram ----
    c = io.open(CRAM, encoding="utf-8").read()
    n0 = len(c)
    blocks = "".join(cram_section(ti, col, rows, "micro-l4-%d" % k)
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
        deck = ('  { id: "%s", name: "Transmission of Microorganisms", color: "accent3",\n'
                "    icon: '%s',\n    cards: [\n%s\n    ]},\n\n"
                % (DECK_ID, ICON,
                   "\n".join('      ["%s", "%s"],' % (esc(q), esc(ans)) for q, ans in CARDS)))
        a = a.replace(anchor_deck, deck + anchor_deck)
    # Append to whatever the Microbiology exam1 deck list currently holds.
    # Lecture 3's adder matched a hard-coded two-deck list, which stopped being
    # true the moment Lecture 3 itself was added -- so this one reads the list.
    off = a.index('id: "microbiology"')
    m = re.search(r'(\{ id: "exam1", name: "Exam 1", deckIds: \[)([^\]]*)(\] \})', a[off:])
    assert m, "Microbiology exam1 deck list not found"
    if DECK_ID not in m.group(2):
        a = a[:off] + a[off:].replace(
            m.group(0), m.group(1) + m.group(2).rstrip() + ', "%s"' % DECK_ID + m.group(3), 1)
    io.open(ARCADE, "w", encoding="utf-8").write(a)
    assert '{ id: "%s",' % DECK_ID in a, "deck missing from the flat list"
    grp = a.split('name: "Microbiology"')[1][:400]
    assert DECK_ID in grp, "deck missing from the Microbiology grouping"
    print("arcade %d -> %d bytes (%d cards, in list and grouping)" % (n0, len(a), len(CARDS)))


if __name__ == "__main__":
    main()
