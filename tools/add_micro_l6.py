#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Microbiology Lecture 6 to the guide, the cram sheet and the Arcade.

Additive and fenced everywhere, with a SEPARATE fence pair per insertion point
-- one shared pair caused the CMS guide splice to drop its sections inside
<nav> and delete the table of contents.

ELEVEN OBJECTIVES, 93 SLIDES. The cram sheet is split by objective group rather
than by slide range, so the small objectives -- the differential count, the
genetic defense, the effects of fever -- get their own rows instead of being
swallowed by complement.
"""
import io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _micro_guide_l6 import SECTION, TOC, TEST

GUIDE = os.path.join(ROOT, "Microbiology Exam 1", "micro-exam-1-study-guide.html")
CRAM = os.path.join(ROOT, "Microbiology Exam 1", "micro-exam-1-cram-sheet.html")
ARCADE = os.path.join(ROOT, "arcade.js")

FENCES = {"toc": ("<!--MICROL6-TOC-->", "<!--/MICROL6-TOC-->"),
          "body": ("<!--MICROL6-BODY-->", "<!--/MICROL6-BODY-->"),
          "cram": ("<!--MICROL6-CRAM-->", "<!--/MICROL6-CRAM-->")}


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
 ("L6 · The Four Kinds of Acquired Immunity", "#3f8a55", [
   ("THE TWO AXES", "ACTIVE (you make it) vs PASSIVE (you receive it) × NATURAL vs ARTIFICIAL. Four boxes — place the scenario."),
   ("NATURAL ACTIVE", "Recovery from infection, INCLUDING subclinical or asymptomatic."),
   ("NATURAL PASSIVE", "MATERNAL ANTIBODY — placenta, then milk. <b>99% is acquired IN UTERO.</b>"),
   ("ARTIFICIAL ACTIVE", "VACCINATION. Degree and duration vary by disease."),
   ("ARTIFICIAL PASSIVE", "IMMUNOTHERAPY — pooled serum (gamma globulin) or donor antibody. Hepatitis A, rabies, tetanus."),
   ("SPECIES IMMUNITY", "A special type of INNATE immunity — illnesses we cannot get BECAUSE we are human."),
   ("ANTIBODY TITRES", "What tells you whether a vaccine on your record is still effective, or whether you need a booster."),
 ]),
 ("L6 · Leukocytes & MHC", "#3f8a55", [
   ("★ THE MNEMONIC", "“NEVER LET MONKEYS EAT BANANAS” — Neutrophils, Lymphocytes, Monocytes, Eosinophils, Basophils. HIGHEST to LOWEST."),
   ("The figures (from L5)", "Neutrophils 55–90% · Lymphocytes 20–35% · Monocytes 3–7% · Eosinophils 1–3% · Basophils 0.5%."),
   ("MHC = ?", "MAJOR HISTOCOMPATIBILITY COMPLEX, also called <b>HUMAN LEUKOCYTE ANTIGEN (HLA)</b>."),
   ("★ WHERE MHC IS NOT", "On ALL cells EXCEPT <b>RED BLOOD CELLS</b>."),
   ("★ WHICH CHROMOSOME", "<b>CHROMOSOME 6</b>, in a multi-gene complex of classes I, II, III."),
   ("MHC does two jobs", "RECOGNITION OF SELF, and REJECTION OF FOREIGN TISSUE."),
   ("★ CLASS I", "Displays self molecules. Read by <b>CYTOTOXIC (Tc) T CELLS</b>."),
   ("★ CLASS II", "The IMMUNE REGULATORY receptors. On MACROPHAGES, APCs and B CELLS. REQUIRED for an APC to activate a <b>T HELPER (CD4)</b> cell."),
   ("Why transplants work at all", "Each MHC profile is unique but can be CLOSE ENOUGH to another’s."),
 ]),
 ("L6 · Clonal Selection", "#3f8a55", [
   ("How many genes", "MORE THAN 500 are used to build lymphocyte receptors."),
   ("★ SELF-REACTIVE CLONES", "ELIMINATED before the fetus is harmed. A defect here = inherited autoimmune disorder such as <b>SCID</b>."),
   ("How big is the naive pool", "10<sup>14</sup> to 10<sup>18</sup> variations — <b>UP TO A QUINTILLION</b>."),
   ("★ THE POINT TO HOLD", "SPECIFICITY EXISTS <b>BEFORE</b> THE ANTIGEN DOES. It is pre-programmed. Antigen SELECTS a clone; it does NOT instruct one. Getting this backwards is the classic error."),
 ]),
 ("L6 · The Two Receptors", "#3f8a55", [
   ("B-CELL RECEPTOR", "= IMMUNOGLOBULIN. <b>FOUR</b> chains: 2 identical HEAVY + 2 identical LIGHT. Y-shaped. Variable + constant regions. SECRETED as antibody."),
   ("T-CELL RECEPTOR", "<b>TWO</b> parallel chains. Small — “one fork” of the Y. <b>NEVER SECRETED.</b> Recognizes antigen ONLY with MHC."),
   ("Young vs mature B cell", "YOUNG carries a small <b>IgM</b>; MATURE carries <b>IgD</b>."),
   ("Variable region genes", "LOCKED IN for the life of the cell AND its progeny, including memory cells."),
   ("B-cell maturation", "BONE MARROW STROMAL CELLS → migrate to lymph nodes, spleen, GALT."),
   ("T-cell maturation", "The <b>THYMUS</b> and its hormones — which is why the thymus unites the immune and endocrine systems."),
   ("★ CD MARKERS", "CD = CLUSTER OF DIFFERENTIATION. <b>CD4 = T HELPER. CD8 = T CYTOTOXIC.</b>"),
 ]),
 ("L6 · Antigens", "#3f8a55", [
   ("EPITOPE", "= ANTIGENIC DETERMINANT. The small molecular group actually recognized. One antigen may carry MANY."),
   ("★ SIZE DECIDES", "Most antigenic: foreign cells and molecules <b>OVER 100,000 MW</b>, usually large proteins."),
   ("★ HAPTEN", "<b>UNDER 1,000 MW</b> — NOT antigenic unless attached to a LARGER CARRIER. Drugs, metals, industrial chemicals. This is how occupational LATEX allergy arises."),
   ("AUTOANTIGEN", "Self tissue for which TOLERANCE IS INADEQUATE → some autoimmune disorders."),
   ("ALLOANTIGEN", "A marker of one individual antigenic to ANOTHER OF THE SAME SPECIES → the <b>BLOOD GROUPS</b> and the MHC profile. Incompatibility → transfusion reaction or graft-versus-host disease."),
   ("HETEROPHILIC", "From an UNRELATED SPECIES with similar determinants. Mammalian heart muscle × group A strep cell wall."),
   ("★ SUPERANTIGEN", "A potent T-CELL STIMULATOR → <b>CYTOKINE STORM</b>. Staph toxins: toxic shock syndrome toxin, enterotoxin."),
   ("ALLERGEN", "Any antigen provoking allergy = <b>TYPE I HYPERSENSITIVITY</b>. Classified by <b>PORTAL OF ENTRY</b>: inhaled · ingested · injected · contact."),
 ]),
 ("L6 · Presentation & the Interleukins", "#3f8a55", [
   ("The three-way collaboration", "An <b>APC</b> + a <b>T HELPER CELL</b> + an antigen-specific <b>B or T CELL</b>."),
   ("What the APC does", "ALTERS the antigen and attaches it to its <b>CLASS II MHC</b> receptor."),
   ("★ INTERLEUKIN 1", "From the <b>APC</b>. Activates the T helper cell. ALSO an <b>ENDOGENOUS PYROGEN</b> → fever and inflammation."),
   ("★ INTERLEUKIN 2", "From the <b>ACTIVATED T HELPER</b>. Activates B cells and other T cells. Its <b>DYSREGULATION</b> → LUPUS and RHEUMATOID ARTHRITIS."),
   ("Swapping these two", "Is the easy mistake. IL-1 comes FROM the APC; IL-2 comes FROM the helper."),
   ("B-cell expansion gives", "<b>PLASMA CELLS</b> (secrete antibody) + <b>MEMORY CELLS</b>."),
   ("★ MEMORY CELLS", "They <b>PAUSE PARTWAY THROUGH MITOSIS</b> — which is why the secondary response is so fast."),
   ("The naming", "B-cell responses = ANTIBODY-MEDIATED (AMI) or HUMORAL-MEDIATED (HMI). T-cell responses = CELL-MEDIATED (CMI)."),
 ]),
 ("L6 · ★ THE FIVE IMMUNOGLOBULINS", "#b8860b", [
   ("Structure", "Y-shaped, FOUR chains. <b>Fab</b> = antigen-binding (two of them). <b>Fc</b> = crystallizable, binds immune cells AND allows the SWIVEL."),
   ("★ IgG", "MONOMER. <b>MOST PREVALENT.</b> The <b>ONLY</b> one crossing the PLACENTA. <b>LONG-TERM IMMUNITY.</b> Huge titre in SECONDARY responses."),
   ("★ IgA", "MONOMER <b>or DIMER</b>. <b>SECOND most prevalent.</b> MUCOSAL — saliva, tears, colostrum, mucus. Local immunity: enteric, respiratory, genitourinary."),
   ("★ IgM", "<b>PENTAMER</b> — by far the LARGEST, so <b>TOO BIG for the placenta</b>. <b>FIRST RESPONDER</b> of the primary response. Important COMPLEMENT FIXER. Binds B cells."),
   ("★ IgD", "MONOMER. HIGH titre in <b>NEWBORNS</b>, very LOW in adults/children. Binds B cells — trigger for activation AND regulation."),
   ("★ IgE", "MONOMER. <b>LEAST common</b> in serum and <b>SHORTEST-LIVED</b>. ALLERGENS and PARASITIC WORMS. Binds <b>MAST CELLS and BASOPHILS</b> → asthma, anaphylaxis, via histamine."),
   ("Which two bind B cells?", "<b>IgM and IgD.</b>"),
   ("THE FOUR ANTIBODY ACTIONS", "AGGLUTINATION · OPSONIZATION · COMPLEMENT FIXATION · NEUTRALIZATION."),
   ("OPSONIZATION", "Coating so phagocytes can engulf. Matters most for SLIPPERY envelopes, WAXY capsules, SLIME layers. Greek: something cooked with food — a coating."),
   ("NEUTRALIZATION", "Blocking the virus’s <b>ATTACHMENT SPIKE PROTEINS</b> so it cannot enter — and making it easier to phagocytose."),
   ("★ AGGLUTINATION", "CROSS-LINKING adjacent cells. <b>IgM is best — its pentamer has TEN binding sites.</b>"),
   ("COMPLEMENT FIXATION", "Antibody binds, complement proteins bind the remaining sites and use <b>PERFORINS</b> to lyse the envelope."),
 ]),
 ("L6 · Primary vs Secondary, and T Cells", "#3f8a55", [
   ("PRIMARY response", "<b>IgM and IgG</b>, with a GRADUAL rise in titre. Plus MEMORY B CELLS."),
   ("★ SECONDARY response", "RAPID and STRONGER, because of MEMORY CELLS. A much higher titre of <b>IgG</b>, then gradual IgM."),
   ("Also called", "The <b>ANAMNESTIC RESPONSE</b>."),
   ("Titre unit", "<b>BAU</b> — binding antibody units."),
   ("Does titre reach zero?", "In a healthy person with robust responses, <b>NO</b>."),
   ("T cells need", "Activation by <b>SOME TYPE OF MHC MOLECULE</b>. All T cells produce CYTOKINES."),
   ("★ THE FOUR T CELLS", "<b>TH (CD4)</b> conducts · <b>TC (CD8)</b> lyses virally infected, cancer and foreign cells · <b>TD</b> delayed hypersensitivity (allergy HOURS to DAYS later) · <b>TS</b> suppressor, limits other T and B cells."),
   ("Sensitized T cells become", "LONG-LASTING <b>MEMORY T CELLS</b>."),
 ]),
 ("L6 · Applications", "#3f8a55", [
   ("PASSIVE immunization lasts", "<b>TWO TO THREE MONTHS.</b>"),
   ("HORSE SERUM", "Early antitoxins for tetanus and diphtheria. STILL used for diphtheria, botulism, spider/snake bites. Risks: <b>SERUM SICKNESS, ANAPHYLAXIS</b>."),
   ("POOLED GAMMA GLOBULIN", "Hepatitis A, hepatitis B, HIV, measles, generally immunodeficient patients."),
   ("★ -mab", "MONOCLONAL ANTIBODY (a protein)."),
   ("★ -omab", "<b>MOUSE.</b>"),
   ("★ -ximab", "<b>CHIMERIC.</b>"),
   ("★ -zumab", "<b>HUMANIZED.</b>"),
   ("★ -umab", "ENTIRELY <b>HUMAN</b>."),
   ("Two examples", "ADALIMUMAB (Humira) — RA, psoriatic arthritis, Crohn, plaque psoriasis. PEMBROLIZUMAB (Keytruda) — melanoma, lung cancer."),
   ("VACCINATION is", "Deliberate exposure to material that is <b>ANTIGENIC BUT NOT PATHOGENIC</b>."),
   ("The history", "LADY MONTAGU brought it to England · <b>JENNER</b> gave the first effective human vaccination (COWPOX → SMALLPOX) · PASTEUR later did RABIES."),
   ("★ AN EFFECTIVE VACCINE", "Low toxicity · protects on exposure · stimulates <b>BOTH AMI AND CMI</b> · produces MEMORY B and T cells · generally NOT many doses · cheap, easy, long shelf-life."),
   ("STERILIZING vaccine", "The best option — the target is rendered NON-FUNCTIONING and UNABLE TO MUTATE."),
   ("Vaccine contents", "Killed whole cells / inactivated virus · LIVE ATTENUATED · acellular or subunit antigens · <b>TOXOIDS</b> · genetically engineered."),
   ("★ MARROW DONATION", "Requires a close <b>CLASS I MHC</b> match plus DNA testing. Harvested from <b>STERNUM, FEMUR or ILIAC CREST</b>. Peripheral stem cells by <b>APHERESIS</b> after a mobilizing drug. The RECIPIENT gets drug and radiation therapy first, TO REDUCE REJECTION RISK."),
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
DECK_ID = "mb-specific-immunity"
ICON = ('<path d="M12 3l7 3v6c0 4-3 7.5-7 9-4-1.5-7-5-7-9V6z"/><path d="M9 12l2 2 4-4"/>')
CARDS = [
  ["What distinguishes SPECIFIC from innate immunity?", "It is adaptive, acquired through contact with infectious agents. Innate immunity is what we are born with."],
  ["What is species immunity?", "A form of innate immunity — illnesses we cannot contract because we are human."],
  ["Recovery from an infection gives which immunity?", "Natural active."],
  ["Maternal antibody across the placenta is which immunity?", "Natural passive."],
  ["Vaccination gives which immunity?", "Artificial active."],
  ["Pooled gamma globulin gives which immunity?", "Artificial passive."],
  ["What proportion of natural passive immunity is acquired in utero?", "About 99 percent."],
  ["What tells you whether a vaccine on your record is still effective?", "Antibody titres."],
  ["Give the leukocyte mnemonic, highest to lowest.", "Never let monkeys eat bananas: neutrophils, lymphocytes, monocytes, eosinophils, basophils."],
  ["Where do all leukocytes originate?", "The bone marrow."],
  ["What is MHC also called?", "Human leukocyte antigen."],
  ["Which cells lack MHC receptors?", "Red blood cells."],
  ["Which chromosome carries the MHC genes?", "Chromosome 6."],
  ["What are the two roles of MHC?", "Recognition of self, and rejection of foreign tissue."],
  ["Which MHC class do cytotoxic T cells read?", "Class I."],
  ["Which MHC class is on macrophages, APCs and B cells?", "Class II."],
  ["What is required for an APC to activate a T helper cell?", "A class II MHC receptor."],
  ["What does an activated T helper cell produce?", "Interleukin 2 — called the boss of the immune system."],
  ["How many genes do lymphocytes use to build their receptors?", "More than 500."],
  ["What happens to lymphocyte clones specific for self?", "They are eliminated before the fetus is harmed. A defect gives severe combined immunodeficiency."],
  ["How large is the naive lymphocyte pool?", "Ten to the fourteenth up to ten to the eighteenth variations — up to a quintillion."],
  ["When is lymphocyte specificity determined?", "Before any antigen arrives. It is pre-programmed genetically, and antigen SELECTS rather than instructs."],
  ["How many chains make up an immunoglobulin?", "Four — two identical heavy and two identical light."],
  ["Which immunoglobulin is on a young B cell, and which on a mature one?", "A small IgM on young cells; IgD on mature ones."],
  ["How does the T-cell receptor differ structurally?", "Two parallel chains, small — one fork of the Y — and never secreted."],
  ["What directs B-cell maturation?", "Bone marrow stromal cells."],
  ["What directs T-cell maturation?", "The thymus and its hormones."],
  ["What does CD stand for, and what is the condition on recognition?", "Cluster of differentiation, and they recognize antigen only when presented with MHC."],
  ["Which CD marker is on helper cells, and which on cytotoxic?", "CD4 on helper, CD8 on cytotoxic."],
  ["What is an epitope?", "The antigenic determinant — the small molecular group recognized by lymphocytes."],
  ["What size of molecule is most antigenic?", "Over 100,000 molecular weight, usually a large protein."],
  ["What is a hapten, and how does it become antigenic?", "Under 1,000 molecular weight, antigenic only when attached to a larger carrier."],
  ["What is an autoantigen?", "Self tissue for which tolerance is inadequate."],
  ["What is an alloantigen, and what does it give rise to?", "A marker antigenic to another of the same species — it gives the blood groups and the MHC profile."],
  ["What is a heterophilic antigen?", "A molecule from an unrelated species bearing similar determinants."],
  ["What is a superantigen, and what can it cause?", "A potent T-cell stimulator that can drive a cytokine storm."],
  ["How are allergens classified?", "By portal of entry: inhaled, ingested, injected, contact."],
  ["Allergy is which type of hypersensitivity?", "Type I."],
  ["Which three cells collaborate in antigen presentation?", "An APC, a T helper cell, and an antigen-specific B or T cell."],
  ["Which interleukin does the APC secrete?", "Interleukin 1 — which is also an endogenous pyrogen."],
  ["Which interleukin comes from the activated T helper cell?", "Interleukin 2."],
  ["Dysregulation of which interleukin is linked to lupus and rheumatoid arthritis?", "Interleukin 2."],
  ["What two cells arise from B-cell clonal expansion?", "Plasma cells and memory cells."],
  ["What is distinctive about memory cell formation?", "They pause partway through mitosis."],
  ["What are B-cell responses called?", "Antibody-mediated immunity, or humoral-mediated immunity."],
  ["What are T-cell responses called?", "Cell-mediated immunity."],
  ["Which antibody fragment binds antigen?", "Fab, the antigen-binding fragment."],
  ["What does the Fc fragment do?", "Binds cells of the immune system, and allows the molecule to swivel."],
  ["Which immunoglobulin is most prevalent?", "IgG."],
  ["Which is the only immunoglobulin crossing the placenta?", "IgG."],
  ["Which immunoglobulin is a pentamer?", "IgM — by far the largest, and too big to cross the placenta."],
  ["Which immunoglobulin is the first responder of the primary response?", "IgM."],
  ["Which immunoglobulin is second most prevalent and lines the mucosa?", "IgA — in saliva, tears, colostrum and mucus."],
  ["In which forms does IgA occur?", "Monomer or dimer."],
  ["Which immunoglobulin is high in newborns and low in adults?", "IgD."],
  ["Which immunoglobulin is least common and shortest-lived?", "IgE."],
  ["Which cells does IgE bind?", "Mast cells and basophils."],
  ["Which two immunoglobulins bind B cells?", "IgM and IgD."],
  ["Name the four antibody-antigen reactions.", "Agglutination, opsonization, complement fixation and neutralization."],
  ["What is opsonization, and when does it matter most?", "Coating so phagocytes can engulf — especially for slippery envelopes, waxy capsules and slime layers."],
  ["How does antibody neutralize a virus?", "By blocking its attachment spike proteins."],
  ["Which immunoglobulin agglutinates best, and why?", "IgM — its pentamer carries ten binding sites."],
  ["How does antibody lead to complement lysis?", "It binds, leaving sites for complement proteins, which use perforins."],
  ["Which antibodies appear in the primary response?", "IgM and IgG, with a gradual rise in titre."],
  ["What makes the secondary response faster?", "Memory cells, which paused partway through mitosis."],
  ["What is the secondary response also called?", "The anamnestic response."],
  ["Which unit measures antibody titre?", "Binding antibody units."],
  ["Does antibody titre fall to zero between exposures?", "Not in a healthy individual with robust responses."],
  ["What do T cells require before acting?", "Activation by some type of MHC molecule."],
  ["Which T cell lyses virally infected and cancer cells?", "The cytotoxic T cell, CD8."],
  ["Which T cell causes allergy hours or days after contact?", "The delayed hypersensitivity cell."],
  ["Which T cell limits other T and B cells?", "The T suppressor cell."],
  ["How long does passive immunization protect?", "Two to three months."],
  ["What are the risks of horse serum immunotherapy?", "Serum sickness or anaphylaxis."],
  ["What is pooled gamma globulin used for?", "Hepatitis A, hepatitis B, HIV, measles and generally immunodeficient patients."],
  ["What does -omab signify?", "Mouse-derived protein."],
  ["What does -ximab signify?", "Chimeric protein."],
  ["What does -zumab signify?", "Humanized protein."],
  ["What does -umab signify?", "Entirely human protein."],
  ["What does adalimumab treat?", "Rheumatoid and psoriatic arthritis, Crohn disease, plaque psoriasis."],
  ["What does pembrolizumab treat?", "Melanoma, lung cancer and others."],
  ["What is vaccination, in principle?", "Deliberate exposure to material that is antigenic but not pathogenic."],
  ["Who gave the first effective human vaccination, and against what?", "Jenner, using cowpox against smallpox."],
  ["Which responses should an effective vaccine stimulate?", "Both antibody-mediated and cell-mediated immunity."],
  ["What would a sterilizing vaccine achieve?", "It renders the target non-functioning and unable to mutate."],
  ["Name the vaccine compositions.", "Killed whole cells, live attenuated, acellular or subunit antigens, toxoids, and genetically engineered organisms."],
  ["What match does marrow donation require?", "A close class I MHC match, plus DNA compatibility testing."],
  ["From where is marrow harvested?", "The sternum, femur or iliac crest."],
  ["How are peripheral stem cells collected?", "By apheresis, after a mobilizing drug."],
  ["Why does the marrow recipient get drug and radiation therapy first?", "To reduce the risk of rejecting the donor cells."],
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
    if "    specificimmunity: [" not in t:
        t = t.replace(anchor, anchor + TEST)
    io.open(GUIDE, "w", encoding="utf-8").write(t)
    nav_a, nav_b = t.index('<nav class="toc">'), t.index("</nav>")
    main_a, main_b = t.index("<main>"), t.index("</main>")
    i = t.index('<section class="deck" id="specific-immunity"')
    assert main_a < i < main_b and not (nav_a < i < nav_b), "section landed outside <main>"
    assert nav_a < t.index('href="#si-acquired"') < nav_b, "toc link outside <nav>"
    assert 'href="#gm-molecular"' in t and 'href="#hd-lines"' in t, "earlier toc lost"
    assert "TEST_YOURSELF.specificimmunity" in t, (
        "this section registers a TEST_YOURSELF.specificimmunity bank but no button opens "
        "it -- four guides shipped with unreachable banks before this was checked")
    print("guide %d -> %d bytes" % (n0, len(t)))

    # ---- cram ----
    c = io.open(CRAM, encoding="utf-8").read()
    n0 = len(c)
    blocks = "".join(cram_section(ti, col, rows, "micro-l6-%d" % k)
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
        deck = ('  { id: "%s", name: "Specific Immunity", color: "accent3",\n'
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
