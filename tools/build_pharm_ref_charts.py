#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Indications & Patient Education and Side Effects reference charts.

Both use _pharm_ref_shell.page(), so the three Pharmacology I Exam 1 references
share one stylesheet and cannot drift apart.

REFUSES TO WRITE unless check_pharm_ref.py passes for that dataset.

    python3 build_pharm_ref_charts.py            # both
    python3 build_pharm_ref_charts.py indications
"""
import os, re, subprocess, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _pharm_ref_shell import page

OUTDIR = os.path.join(ROOT, "Pharmacology I Exam 1")
L1 = "Antibiotics, Antivirals, and Antifungals"
L2 = "02. Dermatology Medications"
L3 = "03. ANS Pharmacology"
DECK_TAG = {L1: "L1", L2: "L2", L3: "L3"}
DECK_NAME = {L1: "Antibiotics, Antivirals &amp; Antifungals",
             L2: "Dermatology Medications", L3: "ANS Pharmacology"}


def plain(s):
    return re.sub(r"<[^>]+>", "", s)


def build_table(rows, headers, keyfn, badge=None):
    body = []
    for r in rows:
        cells = keyfn(r)
        badge_html = ""
        if badge:
            label, colour = badge(r)
            badge_html = '<td><span class="pill" style="background:%s">%s</span></td>' % (colour, label)
        cls = ' class="t-%s"' % r[3].lower() if badge else ""
        body.append('<tr%s><td class="dn">%s</td>%s%s'
                    '<td class="sl">%s<br><span class="g">slide %d</span></td></tr>'
                    % (cls, r[0], badge_html,
                       "".join('<td class="ct">%s</td>' % c for c in cells),
                       DECK_TAG[r[-3]], r[-2]))
    th = "".join('<th%s>%s</th>' % (a, h) for h, a in headers)
    return ('<div class="scroll"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            % (th, "".join(body)))


def section(sid, title, tag, tbl, note=""):
    return ('<section id="%s"><div class="shead"><span class="dot"></span>'
            '<h2>%s <span class="tag">%s</span></h2></div>%s%s</section>'
            % (sid, title, tag, note, tbl))


# ------------------------------------------------------------------ indications
IND_TIER = {
 "DOC": ("Drug of choice", "#1f5d3a", "The deck literally says <b>&ldquo;drug of choice&rdquo;</b> for that indication &mdash; the most answerable phrase in Lecture 1."),
 "IND": ("Indication", "#5b6472", "A stated indication, use or coverage."),
 "EDU": ("Education-heavy", "#9c5230", "The row where the <b>counselling point</b> matters more than the indication."),
 "MON": ("Monitoring", "#7c1d6f", "A target level or laboratory goal."),
}
IND_SECTIONS = [
 ("i-beta", "Beta-lactams", L1, ["Penicillin G", "Aminopenicillins", "Amoxicillin/clav", "Piperacillin",
                                 "Nafcillin", "Cefazolin", "Ceftriaxone", "Cefepime", "Ceftaroline",
                                 "Ceftolozane", "Aztreonam", "Carbapenems"]),
 ("i-vanco", "Vancomycin", L1, ["Vancomycin"]),
 ("i-protein", "Protein synthesis inhibitors", L1, ["Macrolides", "Tetracyclines", "Tigecycline",
                                                    "Aminoglycosides", "Linezolid", "Clindamycin"]),
 ("i-fq", "Fluoroquinolones", L1, ["Fluoroquinolones", "Levofloxacin"]),
 ("i-other", "Other antibacterials", L1, ["Trimethoprim", "Metronidazole", "Polymyxin"]),
 ("i-fungal", "Antifungals", L1, ["Amphotericin", "Flucytosine", "Azoles", "Fluconazole", "Posaconazole",
                                  "Voriconazole", "Echinocandins", "Griseofulvin", "Terbinafine"]),
 ("i-viral", "Antivirals and anthelminthics", L1, ["Aciclovir", "Ganciclovir", "Oseltamivir", "Albendazole"]),
 ("i-derm", "Dermatology medications", L2, None),
 ("i-chol", "Autonomic &mdash; cholinergic", L3, ["Bethanechol", "Pilocarpine", "Carbachol", "Edrophonium",
                                                  "Neostigmine", "Physostigmine", "Donepezil", "Pralidoxime",
                                                  "Atropine", "Scopolamine", "Ipratropium", "Oxybutynin",
                                                  "Succinylcholine", "Nondepolarizing"]),
 ("i-adren", "Autonomic &mdash; adrenergic", L3, ["Epinephrine", "Norepinephrine", "Isoproterenol", "Dopamine",
                                                  "Dobutamine", "Albuterol", "Clonidine", "Oxymetazoline",
                                                  "Phenylephrine", "Pseudoephedrine", "Amphetamine",
                                                  "Tyramine", "Cocaine", "Phenoxybenzamine", "Phentolamine",
                                                  "Prazosin", "Propranolol", "Timolol", "Atenolol",
                                                  "Labetalol"]),
]

# ----------------------------------------------------------------- side effects
SE_SECTIONS = [
 ("s-abx", "Antibacterials", L1, ["Aminopenicillins", "Penicillins", "Piperacillin", "Nafcillin",
                                  "Cephalosporins", "Aztreonam", "Carbapenems", "Vancomycin", "Macrolides", "Tetracyclines", "Tigecycline",
                                  "Aminoglycosides", "Linezolid", "Fluoroquinolones", "Clindamycin",
                                  "Trimethoprim", "Metronidazole", "Polymyxin"]),
 ("s-fungal", "Antifungals", L1, ["Amphotericin", "Flucytosine", "Ketoconazole", "Posaconazole",
                                  "Voriconazole", "Echinocandins", "Griseofulvin"]),
 ("s-viral", "Antivirals and anthelminthics", L1, ["Aciclovir", "Ganciclovir", "Penciclovir", "Albendazole", "Pyrantel"]),
 ("s-derm", "Dermatology medications", L2, None),
 ("s-chol", "Autonomic &mdash; cholinergic", L3, ["Bethanechol", "Physostigmine", "Neostigmine", "Donepezil",
                                                  "Organophosphates", "Atropine", "Succinylcholine",
                                                  "Atracurium"]),
 ("s-adren", "Autonomic &mdash; adrenergic", L3, ["Epinephrine", "Catecholamines", "Norepinephrine",
                                                  "Dopamine", "Dobutamine", "Albuterol", "Clonidine",
                                                  "Oxymetazoline", "Phenylephrine", "Amphetamine",
                                                  "Tyramine", "Alpha-1", "Propranolol", "Labetalol",
                                                  "Nicotine"]),
]


def rows_for(ROWS, deck, prefixes):
    out = []
    for r in ROWS:
        if r[-3] != deck:
            continue
        if prefixes is None or any(plain(r[0]).startswith(p) for p in prefixes):
            out.append(r)
    return out


def assemble(ROWS, SECTIONS, headers, keyfn, badge=None):
    used, secs = set(), []
    for sid, title, deck, prefixes in SECTIONS:
        rs = rows_for(ROWS, deck, prefixes)
        used.update(id(x) for x in rs)
        secs.append(section(sid, title, DECK_NAME[deck],
                            build_table(rs, headers, keyfn, badge)))
    missed = [plain(r[0]) for r in ROWS if id(r) not in used]
    assert not missed, "rows not placed in any section: %s" % missed
    toc = "".join('<a href="#%s">%s</a>' % (sid, t) for sid, t, _, _ in SECTIONS)
    return "\n".join(secs), toc


def gate(key):
    r = subprocess.run([sys.executable, os.path.join(HERE, "check_pharm_ref.py"), key],
                       capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        sys.exit("fact-check failed for %s -- refusing to write the page" % key)


def build_indications():
    gate("indications")
    from _pharm_indications_data import ROWS
    headers = [("Drug or class", ' class="dn-h"'), ("Tier", ' class="p-h"'),
               ("Indications", ""), ("Patient education &amp; practical notes", ""),
               ("Source", ' class="sl-h"')]
    body, toc = assemble(ROWS, IND_SECTIONS, headers, lambda r: (r[1], r[2]),
                         badge=lambda r: (IND_TIER[r[3]][0], IND_TIER[r[3]][1]))
    counts = Counter(r[3] for r in ROWS)
    legend = "".join('<span><span class="dot" style="background:%s"></span><b>%s</b> &mdash; %s</span>'
                     % (c, lab, d) for lab, c, d in IND_TIER.values())
    notes = """    <div class="note"><b>Read the green rows first.</b> Lecture 1 says <b>&ldquo;drug of choice&rdquo;</b>
    outright for __NDOC__ indications, and that phrase is the most directly answerable thing in the deck &mdash;
    a stem that describes an infection is usually asking which drug the slide named for it.</div>
    <div class="note warn"><b>No dosages.</b> Dr. Wood said drug dosages are not tested, so routes, timings and
    durations appear here but milligram doses do not. Where the deck gives a <em>duration</em> &mdash; 48 hours
    for oseltamivir, 12 months for a toenail &mdash; that is education, not dosing, and it is kept.</div>"""
    html = page(
        title="Indications &amp; Patient Education &mdash; Pharmacology I Exam 1 (Class of 2028)",
        kicker="Pharmacology I &middot; Exam 1 &middot; Class of 2028",
        h1="Indications &amp; Patient Education",
        sub="What each drug is FOR, and what you tell the patient. %d entries across all three Exam 1 decks, "
            "each citing its slide. The second and third items on Dr. McInnis&rsquo;s list of what students "
            "under-study." % len(ROWS),
        legend=legend, notes=notes.replace("__NDOC__", str(counts["DOC"])), toc=toc, body=body,
        footer_note="Every row is checked against the slide it cites by <code>tools/check_pharm_ref.py</code> "
                    "before this page is written.")
    p = os.path.join(OUTDIR, "pharm-exam-1-indications.html")
    open(p, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d rows, %d drug-of-choice)"
          % (os.path.basename(p), len(html) // 1024, len(ROWS), counts["DOC"]))


def build_sideeffects():
    gate("sideeffects")
    from _pharm_sideeffects_data import ROWS
    headers = [("Drug or class", ' class="dn-h"'), ("Side effects", ""),
               ("Monitoring &amp; what to watch", ""), ("System", ' class="p-h"'),
               ("Source", ' class="sl-h"')]
    body, toc = assemble(ROWS, SE_SECTIONS, headers, lambda r: (r[1], r[2], r[3]))
    systems = Counter()
    for r in ROWS:
        for s in r[3].split(" / "):
            systems[s] += 1
    top = ", ".join("<b>%s</b> (%d)" % (k, v) for k, v in systems.most_common(6))
    legend = ('<span>Grouped by the <b>system the effect hits</b>, because that is how a question gives it to '
              'you &mdash; &ldquo;a patient on this drug develops ringing in the ears&rdquo; is an ototoxicity '
              'question, not a drug-name question.</span>')
    notes = """    <div class="note"><b>The recurring patterns are worth more than any single row.</b> Most
    common systems here: __TOP__. Four patterns repeat across unrelated classes and are the ones most likely to
    be asked: <b>QT prolongation and Torsades</b> (macrolides, fluoroquinolones, posaconazole),
    <b>ototoxicity plus nephrotoxicity</b> (vancomycin, aminoglycosides), <b>Stevens-Johnson and toxic
    epidermal necrolysis</b> (aminopenicillins, Bactrim, benzimidazoles), and <b>hypokalaemia with
    hypomagnesaemia</b> (amphotericin, posaconazole, echinocandins).</div>"""
    html = page(
        title="Side Effects &mdash; Pharmacology I Exam 1 (Class of 2028)",
        kicker="Pharmacology I &middot; Exam 1 &middot; Class of 2028",
        h1="Side Effects &amp; Monitoring",
        sub="%d entries across all three Exam 1 decks, each citing its slide, grouped by the system the effect "
            "hits. Companion to the contraindications and indications charts." % len(ROWS),
        legend=legend, notes=notes.replace("__TOP__", top), toc=toc, body=body,
        footer_note="Every row is checked against the slide it cites by <code>tools/check_pharm_ref.py</code> "
                    "before this page is written.")
    p = os.path.join(OUTDIR, "pharm-exam-1-side-effects.html")
    open(p, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d rows, %d systems)"
          % (os.path.basename(p), len(html) // 1024, len(ROWS), len(systems)))


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "both"
    if which in ("both", "indications"): build_indications()
    if which in ("both", "sideeffects"): build_sideeffects()
