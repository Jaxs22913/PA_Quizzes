#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Microbiology Lecture 5 to the guide, the cram sheet and the Arcade.

Additive and fenced everywhere, with a SEPARATE fence pair per insertion point
-- one shared pair caused the CMS guide splice to drop its sections inside
<nav> and delete the table of contents.

ELEVEN OBJECTIVES, 93 SLIDES. The cram sheet is split by objective group rather
than by slide range, so the small objectives -- the differential count, the
genetic defence, the effects of fever -- get their own rows instead of being
swallowed by complement.
"""
import io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _micro_guide_l5 import SECTION, TOC, TEST

GUIDE = os.path.join(ROOT, "Microbiology Exam 1", "micro-exam-1-study-guide.html")
CRAM = os.path.join(ROOT, "Microbiology Exam 1", "micro-exam-1-cram-sheet.html")
ARCADE = os.path.join(ROOT, "arcade.js")

FENCES = {"toc": ("<!--MICROL5-TOC-->", "<!--/MICROL5-TOC-->"),
          "body": ("<!--MICROL5-BODY-->", "<!--/MICROL5-BODY-->"),
          "cram": ("<!--MICROL5-CRAM-->", "<!--/MICROL5-CRAM-->")}


def splice(text, key, block, before):
    op, cl = FENCES[key]
    fenced = op + block + cl
    pat = re.compile(re.escape(op) + ".*?" + re.escape(cl), re.S)
    if pat.search(text):
        return pat.sub(lambda _: fenced, text, count=1)
    assert text.count(before) == 1, "anchor not unique: %r" % before[:40]
    return text.replace(before, fenced + before)


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


# --------------------------------------------------------------- cram sheet
CRAM_ROWS = [
 ("L5 · ★ HE READ OUT THE EXAM LIST", "#b8860b", [
   ("How this list exists", "The last three minutes of the lecture are a revision plan. These are his words, in his order."),
   ("1. THE THREE LINES", "“Know those three lines — first, second, third — and KNOW WHAT BELONGS IN EACH. First line: know which are PHYSICAL, which are CHEMICAL, which are MICROBIOLOGICAL.”"),
   ("2. RECOGNITION", "“What do we call the receptors that the white blood cells have?” → <b>PATTERN RECOGNITION RECEPTORS (PRRs)</b>, detecting <b>PAMPs</b> and <b>DAMPs</b>."),
   ("3. MACROPHAGE vs NEUTROPHIL", "“Know the difference between a macrophage and a neutrophil, our two major phagocytes. But HOW are they different?”"),
   ("4. THE DIFFERENTIAL", "“What do we USE it for? And what can it TELL us?”"),
   ("5. INFLAMMATION", "“Know the major characteristics AND HOW DO THEY COME ABOUT? How is it that we have the redness, the heat, the pain?”"),
   ("6. FEVER", "“What CAUSES fever? Why is fever GOOD? Why is fever BAD?”"),
   ("7. INTERFERON", "“WHEN do we produce interferon? What kind of invading organism?” → <b>VIRUS</b>. And: “remember that IT DOES NOT KILL A VIRUS, but it prevents the viral spread.”"),
   ("8. COMPLEMENT", "“Three pathways, ALL GETTING TO C3. Which is first? THE ALTERNATIVE. Then the LECTIN. Then the CLASSICAL — and the classical is the one associated with the THIRD line of defence.”"),
   ("★ THE ORDER MATTERS", "“Organisms have to hit these barriers IN ORDER — physical and chemical first, then the white blood cell processes, and ONLY AFTER that can they start an adaptive response.” A sequence, not a menu."),
   ("✗ NOT asked to memorise (1)", "The TYPES OF MUCINS — only that different surfaces get different ones."),
   ("✗ NOT asked to memorise (2)", "The CHART OF TOXINS defensins can unfold."),
   ("✗ NOT asked to memorise (3)", "The proteins protecting human cells from the MEMBRANE ATTACK COMPLEX — “you don’t need to fuss about that one.”"),
   ("✗ NOT asked to memorise (4)", "The MAC ASSEMBLY CHART — just know it forms a PORE."),
   ("✗ NOT asked to memorise (5)", "The REFERENCE RANGES for the differential. The PROPORTIONS matter; the numbers do not."),
 ]),
 ("L5 · The Three Lines of Defense", "#3f8a55", [
   ("FIRST LINE", "PHYSICAL, CHEMICAL, MICROBIOLOGICAL and GENETIC barriers AT THE PORTAL OF ENTRY. <b>NONSPECIFIC.</b>"),
   ("SECOND LINE", "Protective CELLS, physiological processes, antimicrobial substances. <b>NONSPECIFIC.</b>"),
   ("THIRD LINE", "ACQUIRED on exposure to ANTIGENS — antibodies or defensive cell lines, and IMMUNOLOGICAL MEMORY. <b>SPECIFIC.</b>"),
   ("THE ONE-LINE VERSION", "TWO of the three lines are NONSPECIFIC. Only the THIRD is specific."),
   ("THE ORGANISING IDEA", "Innate immunity covers a huge range WITHOUT a receptor per organism — it recognises PATTERNS SHARED ACROSS PATHOGEN FAMILIES."),
 ]),
 ("L5 · First Line — Barriers", "#3f8a55", [
   ("EPIDERMIS", "STRATIFIED SQUAMOUS. RAPID DESQUAMATION sheds transient flora. KERATIN works because MOST PATHOGENS LACK KERATINASE."),
   ("KERATINOCYTES", "Make ANTIMICROBIAL PEPTIDES, packed into LAMELLAR BODIES, secreted into a WATERPROOF LIPID LAYER."),
   ("MUCOUS MEMBRANES", "MUCH GREATER AREA than skin. THIN, PERMEABLE, <b>NOT KERATINIZED</b> — the price of gas exchange and absorption."),
   ("MUCUS / MUCINS", "Glycoproteins, proteoglycans, peptides, enzymes. MUCINS = the GIGANTIC GLYCOPROTEINS. Made by the GUT GOBLET CELL."),
   ("LACRIMAL APPARATUS", "Washes the eye AND carries LYSOZYME — physical and chemical at once."),
   ("URINE", "Mechanical flush + HIGH OSMOLALITY + inhibitory pH."),
   ("LYSOZYME acts on", "<b>PEPTIDOGLYCAN.</b>"),
   ("SEMEN", "SPERMINE, LYSOZYME, LACTOFERRIN, PHOSPHOLIPASE."),
   ("VAGINAL SECRETIONS", "LACTIC ACID, BETA DEFENSIN, HYDROGEN PEROXIDE. (Easy to swap with the semen list — don’t.)"),
   ("NORMAL FLORA — BOTH barriers", "COMPETES for space and nutrients (PHYSICAL) <b>and</b> makes ANTIMICROBIAL SUBSTANCES (CHEMICAL). Colonisation begins AFTER BIRTH."),
   ("SKIN FLORA", "STAPH EPIDERMIDIS, other COAGULASE-NEGATIVE staphs, CORYNEFORM bacteria."),
   ("★ ATOPIC DERMATITIS", "DYSBIOSIS with LESS antimicrobial peptide. Colonising with COAGULASE-NEGATIVE STAPHS <b>DIMINISHED</b> STAPH AUREUS."),
   ("GUT COMMENSALS — 3 extras", "DIGEST what we cannot · PROVIDE VITAMINS · help develop GALT."),
 ]),
 ("L5 · Plasma Proteins & Defensins", "#3f8a55", [
   ("COAGULATION", "Clot LIMITS PATHOGEN MOBILITY, reduces blood/fluid loss."),
   ("KININ", "Produces BRADYKININ — dilates vessels, relaxes smooth muscle."),
   ("PROTEASE INHIBITORS", "Block MICROBIAL proteases. <b>ONE TENTH of all serum proteins.</b> Example: ALPHA-2 MACROGLOBULIN."),
   ("DEFENSINS — size & mechanism", "<b>30–40 AMINO ACIDS</b>, AMPHIPATHIC — they DAMAGE MEMBRANES."),
   ("DEFENSINS — range", "BACTERIA, FUNGI, and <b>ENVELOPED</b> VIRUSES (an envelope IS a membrane)."),
   ("DEFENSINS — ANTICHAPERONES", "The ONLY innate components that NEUTRALISE A BROAD RANGE OF TOXINS BY UNFOLDING THEM."),
   ("★ THE GENETIC DEFENCE", "GENE COPY NUMBER varies: <b>2–14</b> alpha, <b>2–12</b> beta. COPY NUMBER DETERMINES HOW MUCH PROTEIN."),
   ("ALPHA DEFENSIN LOCATIONS", "4 of 6 in NEUTROPHIL GRANULES; the other 2 from intestinal PANETH CELLS."),
   ("PENTRAXINS", "Bind pathogens and TARGET THEM FOR PHAGOCYTOSIS. SHORT = HEPATOCYTES (serum amyloid P, C-REACTIVE PROTEIN). LONG = myeloid/endothelial/epithelial."),
   ("ACUTE-PHASE — the signal", "Bacteria → MACROPHAGES make <b>IL-6</b> → LIVER raises defensive proteins and <b>LOWERS ALBUMIN</b>."),
   ("★ CRP and SERUM AMYLOID A", "Rise <b>OVER 100-FOLD</b>. That is why CRP is used for infection, inflammation and TISSUE DAMAGE. CRP is a PENTRAXIN OPSONIN."),
 ]),
 ("L5 · Recognition — PAMPs & DAMPs", "#3f8a55", [
   ("THREE things to sort", "HEALTHY SELF · NON-SELF · <b>ALTERED SELF</b> (virus-infected or cancerous)."),
   ("PRR", "PATTERN RECOGNITION RECEPTOR."),
   ("PAMP", "PATHOGEN ASSOCIATED MOLECULAR PATTERN — marks NON-SELF."),
   ("DAMP", "DAMAGE ASSOCIATED MOLECULAR PATTERN — marks ALTERED SELF."),
   ("WHY PATTERNS", "Each receptor sees a pattern shared by a pathogen FAMILY — that is how a limited set covers a wide range."),
   ("MACROPHAGES are best at", "BACTERIAL and FUNGAL CARBOHYDRATES, via LECTIN RECEPTORS."),
   ("NK CELLS are best at", "CHANGED CELL SURFACE PROTEINS on virus-infected cells."),
   ("★ TOLL-LIKE — location decides", "ON THE SURFACE → INFLAMMATORY CYTOKINES. IN ENDOSOMES → <b>INTERFERON</b>."),
   ("RIG (retinoic acid inducible gene)", "Detects VIRAL <b>RNA</b> → interferon."),
   ("CYCLIC GMP CYCLASE", "Detects VIRAL <b>DNA</b> → interferon."),
   ("SCAVENGER RECEPTORS", "Eliminate microbes — or, with NO infection, CELLULAR DEBRIS and APOPTOTIC CELLS."),
 ]),
 ("L5 · Inflammation & Fever", "#3f8a55", [
   ("FIVE CARDINAL SIGNS", "RUBOR (redness) · CALOR (heat) · TUMOR (swelling) · DOLOR (pain) · <b>FUNCTIO LAESA (loss of function)</b>."),
   ("INFLAMMASOME", "Macrophage senses infection → protein structure converts PRO IL-1β → FUNCTIONAL IL-1β in LARGE QUANTITIES."),
   ("★ HOW IL-1β GETS OUT", "PORES form in the macrophage membrane — and the cell DIES by <b>PYROPTOSIS</b>."),
   ("INFLAMMASOME MUTATIONS", "Cause AUTOINFLAMMATORY DISEASES."),
   ("TNF-α", "DILATES vessels → heat, swelling, redness, pain."),
   ("IL-6", "Increases TEMPERATURE."),
   ("CHEMOKINES", "CXCL8, CCL2, IL-12 — attract other white cells."),
   ("EXTRAVASATION — step 1 ROLLING", "<b>L-SELECTIN</b> (leukocyte) → <b>CD34</b> vascular addressin (endothelium)."),
   ("EXTRAVASATION — step 2 FIRM", "<b>LFA-1</b> integrin → <b>ICAM-1</b> immunoglobulin-like molecule."),
   ("EXTRAVASATION — step 3", "<b>DIAPEDESIS</b> — squeezing between endothelial cells, guided by chemokines."),
   ("FEVER — the three pyrogens", "IL-1β, IL-6, TNF-α."),
   ("★ FEVER — THE 5 BENEFITS", "(1) DECREASES viral and bacterial replication — in BACTERIA by <b>STARVING THEM OF IRON</b>. (2) MORE NEUTROPHILS. (3) MORE T CELL PROLIFERATION. (4) BETTER IMMUNE SIGNALLING. (5) <b>ENHANCES TISSUE RESISTANCE TO TNF-α DAMAGE.</b>"),
   ("★ TNF-α LOCAL vs SYSTEMIC", "LOCAL: clots blood in venules → <b>PREVENTS SPREAD TO THE BLOOD</b>. SYSTEMIC: all tissues at once → <b>SHOCK, ORGAN FAILURE, DEATH</b>."),
 ]),
 ("L5 · Complement", "#3f8a55", [
   ("THE BASICS", "<b>30+ PROTEINS</b>, ubiquitous in blood and lymph, circulating as inactive <b>ZYMOGENS</b>, activated by <b>CLEAVAGE</b> in a cascade."),
   ("WHAT MAKES IT WORK", "A unique HIGH-ENERGY <b>THIOESTER BOND</b>."),
   ("★ THE THIOESTER BOND", "C3 cleaved → C3a + C3b, exposing the bond on C3b. Attacked by WATER → soluble, useless. Reacts with a HYDROXYL or AMINO group on a pathogen → <b>COMPLEMENT FIXATION</b>."),
   ("C3a does", "RECRUITS PHAGOCYTES."),
   ("ORDER OF ACTIVATION", "<b>ALTERNATIVE (1st, quickest) → LECTIN (2nd) → CLASSICAL (last)</b>. DISCOVERED in a different order: classical, alternative, lectin."),
   ("ALL THREE CONVERGE ON", "CLEAVING <b>C3</b> — by far the most important molecule in the cascade."),
   ("★ CLASSICAL is BOTH", "Triggered by <b>C-REACTIVE PROTEIN (innate)</b> OR <b>ANTIBODY (adaptive)</b>."),
   ("PROPERDIN (factor P)", "<b>INCREASES</b> activation — binds C3 convertase on microbial surfaces."),
   ("FACTOR H + FACTOR I", "<b>REDUCE</b> activation — H makes C3b cleavable by I → <b>iC3b</b>, which cannot form a convertase."),
   ("MEMBRANE regulators", "<b>DECAY ACCELERATING FACTOR (DAF)</b> and <b>MEMBRANE COFACTOR PROTEIN (MCP)</b> disrupt C3bBb on HUMAN cells."),
   ("OPSONIN", "A protein bound to a pathogen that FACILITATES PHAGOCYTOSIS. <b>C3b is the opsonin.</b>"),
   ("CR1", "Binds C3b → phagocytosis; ALSO protects human cells by disrupting C3 convertase."),
   ("C5a", "RECRUITS NEUTROPHILS + <b>MOST POTENT ANAPHYLATOXIN</b>."),
   ("C5b", "INITIATES THE <b>MEMBRANE ATTACK COMPLEX</b>."),
   ("MAC protection", "S PROTEIN, CLUSTERIN, FACTOR J block C5b/C6/C7. <b>CD59 (PROTECTIN)</b> and HRF block <b>C9</b>."),
   ("★ THE EVASION — and its exception", "STREP PYOGENES and STAPH AUREUS coat in <b>SIALIC ACID</b>, which FACTOR H binds → their C3b is inactivated. <b>ANTIBODY MASKS THE SIALIC ACID</b> — so they resist complement <b>ONLY WHEN NO SPECIFIC ANTIBODY IS PRESENT</b>."),
   ("C3a and C5a in extremis", "ANAPHYLACTIC SHOCK."),
 ]),
 ("L5 · Interferon", "#3f8a55", [
   ("★ THE ONE THING", "<b>INTERFERON DOES NOT KILL VIRUSES.</b> It STOPS SPREAD TO SURROUNDING TISSUE."),
   ("ALPHA", "From LYMPHOCYTES and MACROPHAGES. <b>ACTIVATES NK CELLS.</b>"),
   ("BETA", "From FIBROBLASTS and EPITHELIAL CELLS. Assists B and T CELL MATURATION + inflammatory response."),
   ("GAMMA", "From <b>T CELLS</b>. INHIBITS CANCER CELLS, STIMULATES B CELLS, <b>ACTIVATES MACROPHAGES</b>."),
   ("HOW IT PROTECTS", "Binds cell surfaces → INDUCES ANTIVIRAL PROTEINS. Also INHIBITS CANCER GENES and SUPPRESSES TUMOURS."),
   ("PLASMACYTOID DENDRITIC CELLS", "Professional interferon producers — within 6 HOURS, <b>60% of transcription</b> is type 1 interferon."),
 ]),
 ("L5 · Leukocytes & the Differential", "#3f8a55", [
   ("★ NEUTROPHILS", "<b>55–90%</b> · LOBED nuclei, LAVENDER granules · PHAGOCYTES."),
   ("★ EOSINOPHILS", "<b>1–3%</b> · ORANGE granules, BILOBED · destroy EUKARYOTIC pathogens · MINOR phagocyte."),
   ("★ BASOPHILS", "<b>0.5%</b> · CONSTRICTED nuclei, DARK BLUE granules · release POTENT CHEMICAL MEDIATORS."),
   ("★ MONOCYTES/MACROPHAGES", "<b>3–7%</b> · <b>LARGEST</b> WBC, KIDNEY-SHAPED nucleus · phagocytic, HOUSEKEEPING, ANTIGEN PRESENTATION, cytokines."),
   ("★ LYMPHOCYTES", "<b>20–35%</b> · B (adaptive humoral) · T (adaptive cell-mediated) · <b>NON-B NON-T incl. NK = INNATE</b>."),
   ("MAST CELLS", "Related to basophils but NONMOTILE and CONNECTIVE-TISSUE BOUND. Common progenitor <b>UNSURE</b>."),
   ("MACROPHAGE origin", "FINAL DIFFERENTIATION OF A MONOCYTE, in tissue."),
   ("DIFFERENTIAL COUNT — what it does", "Totals EACH TYPE and asks whether they are in <b>NORMAL PROPORTION</b> — proportion, not just total."),
   ("DIFFERENTIAL — 6 USES", "INFECTION TYPES · INFLAMMATION · ALLERGIES · IMMUNE DISORDERS · LEUKAEMIA · MYELODYSPLASTIC SYNDROME."),
   ("MACROPHAGE vs NEUTROPHIL", "MACROPHAGE: LONG-LIVED, tissue-resident, WORKS FIRST and RAISES THE ALARM. NEUTROPHIL: SHORT-LIVED dedicated killer, circulates, WAITS FOR THE ALARM."),
   ("RESPIRATORY BURST", "<b>NADPH OXIDASE</b> → SUPEROXIDE → picks up H ions and <b>RAISES pH</b> so digestive granules can work."),
   ("LIMITING THE DAMAGE", "<b>CATALASE</b> degrades H2O2 → H2O + O2."),
   ("WHY NEUTROPHILS DIE", "They CANNOT REPLENISH GRANULE CONTENTS."),
   ("PUS", "DEAD ORGANISMS + DEAD NEUTROPHILS + DEAD TISSUE."),
   ("NETOSIS", "Neutrophil BURSTS — DNA and defensive proteins form a <b>NEUTROPHIL EXTRACELLULAR TRAP (NET)</b>."),
   ("DENDRITIC CELLS", "Patrol tissue, take antigen to the NEAREST LYMPH NODE. An <b>IMMATURE</b> one FAILS TO MAKE A GOOD CONNECTION for activation."),
 ]),
 ("L5 · NK Cells & Coordination", "#3f8a55", [
   ("NK CELLS kill", "Cells infected by VIRUSES, BACTERIA or PROTOZOAN PARASITES — INTRACELLULAR infection."),
   ("CD56 DIM vs BRIGHT", "DIM = <b>KILLING</b> virally infected cells. BRIGHT = <b>CYTOKINE SECRETION</b> to maintain inflammation."),
   ("UTERINE NK (uNK)", "CD56 BRIGHT — work with FETAL TROPHOBLASTS to enlarge the <b>SPIRAL ARTERIES</b>. <b>PREECLAMPSIA</b> postulated to involve abnormal KIR activity, MORE INHIBITORY than activating."),
   ("NK CYTOTOXICITY rises", "<b>20–100 FOLD</b> on exposure to type 1 interferons."),
   ("WHICH STIMULUS, WHICH FUNCTION", "IFN-α/β → favours <b>CYTOTOXICITY</b>. IL-12 → favours <b>CYTOKINE PRODUCTION</b>."),
   ("★ THE ONE REQUIREMENT", "NK receptors MUST <b>INHIBIT KILLING OF HEALTHY SELF-CELLS</b>. Killing happens when ACTIVATING > INHIBITORY."),
   ("HOW NK KILLS", "Releases CYTOTOXIC GRANULES → <b>APOPTOSIS</b>. Target shrinks, chromatin condenses. MACROPHAGE cleans up."),
   ("NK ↔ MACROPHAGE", "Macrophages RECRUIT and ACTIVATE NK; NK return <b>IFN-γ</b> which enhances macrophage phagocytosis."),
   ("IF NK CANNOT COPE", "They stimulate DENDRITIC CELLS → secondary lymphoid tissue → ADAPTIVE response. Control passes to T CELLS."),
   ("ILC1 / ILC2 / ILC3", "ILC1 = INTRACELLULAR (hold till NK arrive). ILC2 = MUCOSAL, LARGE EXTRACELLULAR PARASITES (worms). ILC3 = EXTRACELLULAR BACTERIA and FUNGI."),
   ("LTi CELLS", "LYMPHOID TISSUE INDUCER — facilitate development of SECONDARY LYMPHOID TISSUE."),
   ("PRIMARY lymphoid organs", "<b>THYMUS → T cells. BONE MARROW → B cells.</b>"),
   ("SECONDARY lymphoid", "SPLEEN, LYMPH NODES, SALT (skin), MALT (mucosal), <b>GALT (gut — PEYER’S PATCHES and APPENDIX)</b>, BALT (bronchial)."),
   ("LYMPHATICS reach everywhere EXCEPT", "<b>CNS, BONE, PLACENTA, THYMUS.</b>"),
   ("INDUCED INNATE RESPONSE", "<b>4 HOURS – 4 DAYS.</b> STILL NONSPECIFIC. Macrophages, neutrophils, dendritic cells."),
   ("★ THE CLOSING CONTRAST", "<b>NO INNATE</b> → infections UNCONTROLLED, and adaptive <b>CANNOT BE DEPLOYED</b>. <b>NO ADAPTIVE</b> → CONTROLLED at first but <b>NEVER CLEARED</b>. Innate is the PREREQUISITE, not the backup."),
 ]),
]


def cram_section(title, colour, rows, sid):
    body = "\n".join(
        '          <tr><td class="h">%s</td><td>%s</td></tr>' % (a, b) for a, b in rows)
    return ('\n  <section class="topic" id="%s" style="--acc:%s;--acc-bg:#e8f4ea;'
            '--acc-zebra:#f2f9f4;--acc-ink:#1f4d2b">\n'
            '    <div class="shead"><span class="dot" style="background:%s"></span><h2>%s</h2></div>\n'
            '    <div class="scroll">\n      <table>\n'
            '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
            '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n'
            % (sid, colour, colour, title, body))


# ------------------------------------------------------------------- arcade
DECK_ID = "mb-host-defenses"
ICON = ('<path d="M12 3l7 3v6c0 4-3 7.5-7 9-4-1.5-7-5-7-9V6z"/>')
CARDS = [
  ["How many lines of host defense are there, and which are nonspecific?", "Three. The first and second are nonspecific; only the third is specific."],
  ["What is the first line of defense?", "Physical, chemical, microbiological and genetic barriers at the portal of entry."],
  ["What is the second line based on?", "Protective cells, physiological processes and antimicrobial substances."],
  ["What does the third line create?", "Antibodies or defensive cell lines, and immunological memory."],
  ["Which tissue type is the epidermis?", "Stratified squamous epithelium."],
  ["Why does keratin stop most pathogens?", "Most pathogens lack keratinase."],
  ["What do keratinocytes secrete into the lipid layer?", "Antimicrobial peptides, packaged in lamellar bodies."],
  ["How do mucous membranes differ from skin?", "Thin, permeable, not keratinized — and a much greater surface area."],
  ["What are mucins?", "The gigantic glycoproteins that give mucus its protective properties."],
  ["Which gut cell makes protective mucus?", "The goblet cell."],
  ["What chemical defence do tears carry?", "Lysozyme."],
  ["What does lysozyme act on?", "Peptidoglycan."],
  ["How does urine defend beyond flushing?", "High osmolality and an inhibitory pH."],
  ["When does colonization by normal flora begin?", "After birth."],
  ["Which organisms are normal skin flora?", "Staphylococcus epidermidis, other coagulase-negative staphylococci, and coryneform bacteria."],
  ["How is normal flora BOTH a physical and a chemical barrier?", "It competes for space and nutrients, and it makes antimicrobial substances."],
  ["What did colonizing atopic skin with coagulase-negative staphylococci do?", "It diminished colonisation by Staphylococcus aureus."],
  ["What three extras do gut commensals provide?", "Digestion of what we cannot, vitamins, and development of gut-associated lymphoid tissue."],
  ["Which chemical defences are named for SEMEN?", "Spermine, lysozyme, lactoferrin and phospholipase."],
  ["Which chemical defences are named for VAGINAL secretions?", "Lactic acid, beta defensin and hydrogen peroxide."],
  ["How does the coagulation system limit infection?", "Clotting limits pathogen mobility and reduces blood and fluid loss."],
  ["What does the kinin system produce?", "Bradykinin, which dilates vessels and relaxes smooth muscle."],
  ["What fraction of serum proteins are protease inhibitors?", "About one tenth. Alpha-2 macroglobulin is the example."],
  ["How long are defensins, and how do they kill?", "30 to 40 amino acids; amphipathic, so they damage membranes."],
  ["What can defensins kill?", "Bacteria, fungi, and enveloped viruses — because an envelope is a membrane."],
  ["Why are defensins called antichaperones?", "They neutralise a broad range of microbial toxins by unfolding them."],
  ["Why is defensin production a GENETIC defence?", "Gene copy number varies between individuals — 2 to 14 alpha, 2 to 12 beta — and sets how much protein is made."],
  ["Where are the six alpha defensins?", "Four in neutrophil granules; two made by intestinal Paneth cells."],
  ["What do pentraxins do?", "Bind pathogen surfaces and target them for phagocytosis."],
  ["Which cells make the short pentraxins?", "Hepatocytes — serum amyloid P component and C-reactive protein."],
  ["Which cytokine drives the acute-phase response?", "Interleukin 6, made by macrophages, acting on the liver."],
  ["What happens to albumin in the acute-phase response?", "It decreases, while defensive plasma proteins increase."],
  ["By how much do C-reactive protein and serum amyloid A rise?", "Over a hundredfold."],
  ["What kind of molecule is C-reactive protein?", "A pentraxin opsonin that enhances phagocytosis."],
  ["What three things must recognition distinguish?", "Healthy self, non-self, and altered self."],
  ["What does PAMP stand for, and what does it mark?", "Pathogen Associated Molecular Pattern — it marks non-self."],
  ["What does DAMP stand for, and what does it mark?", "Damage Associated Molecular Pattern — it marks altered self."],
  ["Why can a limited set of receptors cover so many organisms?", "Each recognises a pattern shared by a whole pathogen family."],
  ["Which cells excel at recognizing bacterial carbohydrates?", "Macrophages, using lectin receptors."],
  ["Which cells excel at recognizing virus-infected cells?", "Natural killer cells, detecting changed surface proteins."],
  ["A Toll-like receptor on the SURFACE triggers what?", "Inflammatory cytokines."],
  ["A Toll-like receptor in an ENDOSOME triggers what?", "Interferon."],
  ["What detects viral RNA, and what does it trigger?", "Retinoic acid inducible gene — interferon."],
  ["What detects viral DNA, and what does it trigger?", "Cyclic GMP cyclase — interferon."],
  ["What do scavenger receptors do without an infection?", "Clear cellular debris and apoptotic cells."],
  ["Name the five cardinal signs of inflammation.", "Rubor, calor, tumor, dolor, functio laesa."],
  ["What does functio laesa mean?", "Loss of function."],
  ["What does the inflammasome do?", "Converts pro interleukin 1 beta into functional interleukin 1 beta, in large quantities."],
  ["How does interleukin 1 beta leave the macrophage?", "Through pores — and the macrophage dies by pyroptosis."],
  ["What do inflammasome gene mutations cause?", "Autoinflammatory diseases."],
  ["Which cytokine dilates vessels to give heat, swelling, redness and pain?", "Tumour necrosis factor alpha."],
  ["Which three molecules act as chemokines here?", "CXCL8, CCL2 and interleukin 12."],
  ["Which adhesion pair makes the leukocyte ROLL?", "L-selectin on the leukocyte to CD34 on the endothelium."],
  ["Which pair holds it FIRMLY?", "LFA-1 to ICAM-1."],
  ["What is diapedesis?", "Squeezing between endothelial cells to reach the infection."],
  ["Which three cytokines cause fever?", "Interleukin 1 beta, interleukin 6 and tumour necrosis factor alpha."],
  ["How does fever act against bacteria specifically?", "It starves them of iron."],
  ["Name three benefits of fever besides slowing replication.", "More neutrophils, more T cell proliferation, better immune signalling — and resistance to tumour necrosis factor damage."],
  ["What does LOCAL tumour necrosis factor alpha achieve?", "It clots blood in the venules, preventing spread of infection to the blood."],
  ["What does SYSTEMIC tumour necrosis factor alpha cause?", "Shock, organ failure and death."],
  ["How many complement proteins, and in what form do they circulate?", "More than thirty, as inactive zymogens."],
  ["What gives complement its activity?", "A high-energy thioester bond."],
  ["What are the two fates of the thioester bond on C3b?", "Attacked by water and made soluble, or reacting with a pathogen surface — complement fixation."],
  ["What does C3a do?", "Recruits phagocytes."],
  ["Name the complement pathways in ACTIVATION order.", "Alternative, then lectin, then classical."],
  ["In what order were the complement pathways DISCOVERED?", "Classical, then alternative, then lectin."],
  ["What do all three complement pathways converge on?", "Cleaving C3 into C3a and C3b."],
  ["Why is the classical pathway both innate and adaptive?", "It can be triggered by C-reactive protein or by antibody."],
  ["What does properdin do?", "Increases complement activation by binding C3 convertase on microbial surfaces."],
  ["How do factor H and factor I work together?", "H makes C3b cleavable by I, giving iC3b, which cannot form a convertase."],
  ["Which membrane proteins protect human cells from C3 convertase?", "Decay accelerating factor and membrane cofactor protein."],
  ["What is an opsonin, and which complement protein is one?", "A protein bound to a pathogen that facilitates phagocytosis — C3b."],
  ["What are the two roles of complement receptor 1?", "Binding C3b for phagocytosis, and protecting human cells by disrupting C3 convertase."],
  ["What are the two roles of C5a?", "Recruiting neutrophils, and acting as the most potent anaphylatoxin."],
  ["What does C5b initiate?", "The membrane attack complex."],
  ["Which proteins stop C5b, C6 and C7 joining human membranes?", "S protein, clusterin and factor J."],
  ["What does CD59 (protectin) prevent?", "C9 from joining a membrane complex that has attached."],
  ["How do Streptococcus pyogenes and Staphylococcus aureus evade complement?", "They coat in sialic acid, which factor H binds, so their C3b is inactivated."],
  ["Why does antibody defeat that evasion?", "It masks the sialic acid before complement binds."],
  ["What can C3a and C5a cause in extreme cases?", "Anaphylactic shock."],
  ["Which cells make interferon alpha?", "Lymphocytes and macrophages."],
  ["Which cells make interferon beta?", "Fibroblasts and epithelial cells."],
  ["Which cells make interferon gamma?", "T cells."],
  ["Does interferon kill viruses?", "No. It stops spread to surrounding tissue."],
  ["Which interferon activates natural killer cells?", "Interferon alpha."],
  ["What does interferon gamma do?", "Inhibits cancer cells, stimulates B cells, and activates macrophages."],
  ["What makes plasmacytoid dendritic cells professional interferon producers?", "Within six hours of activation, 60% of their transcription is type 1 interferon."],
  ["What percentage of white cells are neutrophils?", "55 to 90 per cent."],
  ["What percentage are eosinophils, and what do they kill?", "1 to 3 per cent; eukaryotic pathogens."],
  ["What percentage are basophils?", "0.5 per cent."],
  ["What percentage are monocytes and macrophages?", "3 to 7 per cent — and they are the largest white cells."],
  ["What percentage are lymphocytes?", "20 to 35 per cent."],
  ["Which lymphocytes belong to INNATE immunity?", "The non-B non-T lymphocytes, including natural killer cells."],
  ["What is a macrophage, developmentally?", "The final differentiation of a monocyte, in tissue."],
  ["What does a differential white count measure?", "The number of each type, and whether they are in normal proportion."],
  ["Name three uses of the differential white count.", "Infection types, inflammation and allergies — plus immune disorders, leukaemia and myelodysplastic syndrome."],
  ["How do macrophages and neutrophils divide the work?", "The macrophage is long-lived, tissue-resident and raises the alarm; the neutrophil is a short-lived circulating killer that answers it."],
  ["What does NADPH oxidase produce, and why does it help?", "Superoxide, which raises the pH so the digestive granules can work."],
  ["Which enzyme limits respiratory-burst damage?", "Catalase, degrading hydrogen peroxide."],
  ["Why do neutrophils die after phagocytosing?", "They cannot replenish their granule contents."],
  ["What is pus made of?", "Dead organisms, dead neutrophils and dead tissue."],
  ["What is netosis?", "A neutrophil bursting so its DNA and proteins form a trap that catches and kills microbes."],
  ["Why does dendritic cell maturity matter?", "An immature one reaching the lymph node fails to make a good connection for activation."],
  ["What do natural killer cells kill?", "Cells infected by viruses, bacteria or protozoan parasites."],
  ["What is the difference between CD56 dim and CD56 bright?", "Dim kills infected cells; bright secretes cytokines to maintain inflammation."],
  ["What do uterine natural killer cells do?", "Work with fetal trophoblasts to enlarge the spiral arteries and boost blood flow to the fetus."],
  ["What is preeclampsia postulated to involve?", "Abnormal killer-cell immunoglobulin-like receptor activity — more inhibitory than activating."],
  ["By how much does natural killer cytotoxicity rise with type 1 interferon?", "20 to 100 fold."],
  ["Which stimulus favours NK cytotoxicity, and which favours cytokine release?", "Interferons alpha and beta favour killing; interleukin 12 favours cytokines."],
  ["What is the one requirement of a natural killer receptor?", "It must inhibit the cell from killing healthy self-cells."],
  ["When does a natural killer cell kill?", "When activating signals outweigh inhibitory ones, because protein expression has changed."],
  ["How does a natural killer cell kill?", "Cytotoxic granules induce apoptosis; a macrophage clears the debris."],
  ["How do natural killer cells and macrophages cooperate?", "Macrophages recruit and activate them; they return interferon gamma, enhancing macrophage phagocytosis."],
  ["What happens if natural killer cells cannot contain an infection?", "They stimulate dendritic cells to start an adaptive response, and control passes to T cells."],
  ["What does ILC2 respond to?", "Large extracellular parasites like worms, at mucosal surfaces."],
  ["What do lymphoid tissue inducer cells do?", "Facilitate development of secondary lymphoid tissue."],
  ["Which are the primary lymphoid organs?", "Thymus for T cells, bone marrow for B cells."],
  ["What does GALT stand for, and what are its parts?", "Gut-associated lymphoid tissue — Peyer's patches and the appendix."],
  ["Where do lymphatic capillaries NOT reach?", "The central nervous system, bone, placenta and thymus."],
  ["Over what interval does the induced innate response operate?", "Four hours to four days."],
  ["Is the induced innate response specific?", "No — still nonspecific, but using more extensive pattern recognition."],
  ["What happens to infection with NO innate immunity?", "Infections are uncontrolled, and the adaptive response cannot be deployed at all."],
  ["What happens to infection with NO adaptive immunity?", "It is controlled at first by innate immunity, but never cleared."],
]

_p = [c[0] for c in CARDS]
assert len(_p) == len(set(_p)), "duplicate card prompt"
_MGMT = re.compile(r"first[- ]line therapy|drug of choice|what is the treatment", re.I)
assert not [c for c in CARDS if any(_MGMT.search(t) for t in c)], "management card"


def main():
    # ---- guide ----
    t = io.open(GUIDE, encoding="utf-8").read()
    n0 = len(t)
    t = splice(t, "toc", "\n" + TOC, "</nav>")
    t = splice(t, "body", "\n" + SECTION + "\n", "</main>")
    anchor = "  var TEST_YOURSELF = {\n"
    assert t.count(anchor) == 1
    if "    hostdefenses: [" not in t:
        t = t.replace(anchor, anchor + TEST)
    io.open(GUIDE, "w", encoding="utf-8").write(t)
    nav_a, nav_b = t.index('<nav class="toc">'), t.index("</nav>")
    main_a, main_b = t.index("<main>"), t.index("</main>")
    i = t.index('<section class="deck" id="host-defenses"')
    assert main_a < i < main_b and not (nav_a < i < nav_b), "section landed outside <main>"
    assert nav_a < t.index('href="#hd-lines"') < nav_b, "toc link outside <nav>"
    assert 'href="#gm-molecular"' in t and 'href="#tx-chain"' in t, "earlier toc lost"
    assert "TEST_YOURSELF.hostdefenses" in t, (
        "this section registers a TEST_YOURSELF.hostdefenses bank but no button opens "
        "it -- four guides shipped with unreachable banks before this was checked")
    print("guide %d -> %d bytes" % (n0, len(t)))

    # ---- cram ----
    c = io.open(CRAM, encoding="utf-8").read()
    n0 = len(c)
    blocks = "".join(cram_section(ti, col, rows, "micro-l5-%d" % k)
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
        deck = ('  { id: "%s", name: "Host Defenses: Nonspecific", color: "accent3",\n'
                "    icon: '%s',\n    cards: [\n%s\n    ]},\n\n"
                % (DECK_ID, ICON,
                   "\n".join('      ["%s", "%s"],' % (esc(q), esc(ans)) for q, ans in CARDS)))
        a = a.replace(anchor_deck, deck + anchor_deck)
    off = a.index('id: "microbiology"')
    m = re.search(r'(\{ id: "exam1", name: "Exam 1", deckIds: \[)([^\]]*)(\] \})', a[off:])
    assert m, "Microbiology exam1 deck list not found"
    if DECK_ID not in m.group(2):
        a = a[:off] + a[off:].replace(
            m.group(0), m.group(1) + m.group(2).rstrip() + ', "%s"' % DECK_ID + m.group(3), 1)
    io.open(ARCADE, "w", encoding="utf-8").write(a)
    assert '{ id: "%s",' % DECK_ID in a, "deck missing from the flat list"
    grp = a.split('name: "Microbiology"')[1][:500]
    assert DECK_ID in grp, "deck missing from the Microbiology grouping"
    print("arcade %d -> %d bytes (%d cards, in list and grouping)" % (n0, len(a), len(CARDS)))


if __name__ == "__main__":
    main()
