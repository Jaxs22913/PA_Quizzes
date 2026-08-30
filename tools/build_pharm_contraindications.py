#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Pharmacology I Exam 1 Contraindications quick reference.

Dr. McInnis's 2026-08-28 email said students over-study mechanism and
under-study indications, patient education, side effects and CONTRAINDICATIONS.
This page is the last of those, pulled out of all three decks into one place.

REFUSES TO WRITE unless check_pharm_contra.py passes -- every row is verified
against the slide it cites before the file is touched.

Named reactions and syndromes are bold AND underlined, per Jaxon's request, so
"Red Man Syndrome" style facts can be found by scanning rather than reading.
"""
import html as H
import os, re, subprocess, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _pharm_contra_data import ROWS, L1, L2, L3

OUT = os.path.join(ROOT, "Pharmacology I Exam 1", "pharm-exam-1-contraindications.html")

# Inherited from the Pharmacology I quizzes and guide so the exam reads as one thing.
NAVY, INDIGO, GOLD, ICE = "#6b3524", "#9c5230", "#c9a227", "#fbf1e6"

TIER = {
 "ABS":   ("Contraindicated", "#b3261e", "The deck uses the word <b>contraindicated</b>."),
 "BBW":   ("Black box", "#7c1d6f", "The deck says <b>black box warning</b>."),
 "AVOID": ("Avoid / do not use", "#a4502a", "The deck says avoid, do not use, cannot use, or teratogenic."),
 "NAMED": ("Named reaction", "#1f5d3a", "A named syndrome or reaction &mdash; <u><b>bold and underlined</b></u> in the tables."),
 "CAUT":  ("Caution", "#5b6472", "A stated caution, monitoring need or major adverse effect &mdash; <b>not</b> worded as a contraindication."),
 "EXCEPT": ("Safe exception", "#0f766e", "The deck says this one <b>can</b> be used where the class cannot &mdash; the flip side of a contraindication."),
}

SECTIONS = [
 ("betalactam", "Beta-lactams", L1, ["Aminopenicillins", "Penicillins", "Cephalosporins", "Ceftriaxone", "Aztreonam", "Carbapenems"]),
 ("vanco", "Vancomycin", L1, ["Vancomycin"]),
 ("protein", "Protein synthesis inhibitors", L1, ["Macrolides", "Tetracyclines", "Clindamycin", "Linezolid", "Aminoglycosides"]),
 ("fq", "Fluoroquinolones", L1, ["Fluoroquinolones", "Moxifloxacin"]),
 ("other-abx", "Other antibacterials", L1, ["Trimethoprim", "Metronidazole", "Polymyxin B and"]),
 ("antifungal", "Antifungals", L1, ["Amphotericin", "Itraconazole", "Fluconazole", "Voriconazole",
                                    "Posaconazole", "Ketoconazole", "Flucytosine", "Griseofulvin", "Echinocandins", "Allylamines"]),
 ("antiviral", "Antivirals and anthelminthics", L1, ["Acyclovir", "Ganciclovir", "Oseltamivir", "Albendazole"]),
 ("derm", "Dermatology medications", L2, None),
 ("chol", "Autonomic &mdash; cholinergic", L3, ["Cholinergic agonists", "Acetylcholinesterase", "Physostigmine",
                                                "Organophosphate", "Atropine", "Scopolamine", "Succinylcholine",
                                                "Atracurium"]),
 ("adren", "Autonomic &mdash; adrenergic", L3, ["Epinephrine", "Norepinephrine", "Dobutamine", "Clonidine",
                                                "Alpha-1", "Phenoxybenzamine", "Propranolol", "Selective beta-1",
                                                "Labetalol", "Nicotine"]),
]
DECK_TAG = {L1: "L1", L2: "L2", L3: "L3"}
DECK_NAME = {L1: "Antibiotics, Antivirals &amp; Antifungals",
             L2: "Dermatology Medications", L3: "ANS Pharmacology"}


def plain(s):
    return re.sub(r"<[^>]+>", "", s)


def rows_for(deck, prefixes):
    out = []
    for r in ROWS:
        if r[3] != deck:
            continue
        if prefixes is None or any(plain(r[0]).startswith(p) for p in prefixes):
            out.append(r)
    return out


def table(rows):
    body = []
    for drug, text, tier, deck, slide, _ in rows:
        label, colour, _d = TIER[tier]
        body.append(
            '<tr class="t-%s"><td class="dn">%s</td>'
            '<td><span class="pill" style="background:%s">%s</span></td>'
            '<td class="ct">%s</td>'
            '<td class="sl">%s<br><span class="g">slide %d</span></td></tr>'
            % (tier.lower(), drug, colour, label, text, DECK_TAG[deck], slide))
    return ('<div class="scroll"><table>'
            '<thead><tr><th class="dn-h">Drug or class</th><th class="p-h">Tier</th>'
            '<th>What it says</th><th class="sl-h">Source</th></tr></thead>'
            '<tbody>%s</tbody></table></div>' % "".join(body))


def main():
    r = subprocess.run([sys.executable, os.path.join(HERE, "check_pharm_contra.py")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout); sys.exit("fact-check failed -- refusing to write the page")
    print(r.stdout.strip().splitlines()[-1])

    used = set()
    secs = []
    for sid, title, deck, prefixes in SECTIONS:
        rs = rows_for(deck, prefixes)
        used.update(id(x) for x in rs)
        secs.append('<section id="%s"><div class="shead"><span class="dot"></span>'
                    '<h2>%s <span class="tag">%s</span></h2></div>%s</section>'
                    % (sid, title, DECK_NAME[deck], table(rs)))
    missed = [plain(r0[0]) for r0 in ROWS if id(r0) not in used]
    assert not missed, "rows not placed in any section: %s" % missed

    named = [r for r in ROWS if r[2] == "NAMED"]
    preg = [r for r in ROWS if re.search(r"pregnan|breastfeed|teratogen", plain(r[1]), re.I)]
    age = [r for r in ROWS if re.search(r"\b8 years|18 years|under 18|30 days of life|in children", plain(r[1]), re.I)]

    def minitable(rs, col1="Drug or class"):
        b = "".join('<tr><td class="dn">%s</td><td class="ct">%s</td>'
                    '<td class="sl">%s<br><span class="g">slide %d</span></td></tr>'
                    % (r[0], r[1], DECK_TAG[r[3]], r[4]) for r in rs)
        return ('<div class="scroll"><table><thead><tr><th class="dn-h">%s</th>'
                '<th>What it says</th><th class="sl-h">Source</th></tr></thead>'
                '<tbody>%s</tbody></table></div>' % (col1, b))

    counts = Counter(r[2] for r in ROWS)
    legend = "".join(
        '<span><span class="dot" style="background:%s"></span><b>%s</b> &mdash; %s</span>'
        % (c, lab, desc) for k, (lab, c, desc) in TIER.items())
    toc = "".join('<a href="#%s">%s</a>' % (sid, title) for sid, title, _, _ in SECTIONS)

    html = """<!DOCTYPE html>
<html lang="en">
<head>
<script>document.documentElement.setAttribute('data-theme', localStorage.getItem('siteTheme') || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));</script>
<link rel="stylesheet" href="../theme.css">
<script src="../theme.js" defer></script>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-2K06TXC2KK"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-2K06TXC2KK');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contraindications Reference &mdash; Pharmacology I Exam 1 (Class of 2028)</title>
<style>
  :root{
    --ink:#161a24;--body:#2b3140;--muted:#6b7280;--line:#e4e7ef;--paper:#f6f7fb;--card:#fff;
    --navy:__NAVY__;--indigo:__INDIGO__;--gold:__GOLD__;--ice:__ICE__;
    --shadow:0 1px 2px rgba(20,22,40,.05),0 10px 30px rgba(20,22,40,.05);
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--paper);color:var(--body);
    font:400 15.5px/1.55 ui-sans-serif,"Segoe UI",system-ui,-apple-system,Roboto,Arial,sans-serif;
    -webkit-font-smoothing:antialiased}
  .wrap{max-width:1180px;margin:0 auto;padding:26px 20px 70px}
  .hero{background:var(--card);border:1px solid var(--line);border-radius:16px;
    padding:22px 22px 18px;box-shadow:var(--shadow);margin-bottom:18px}
  .kicker{font-size:12.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--indigo);font-weight:800}
  h1{margin:6px 0 8px;font-size:31px;line-height:1.15;color:var(--ink);letter-spacing:-.015em}
  .sub{margin:0 0 14px;color:var(--muted);font-size:15px}
  .legend{display:flex;flex-wrap:wrap;gap:10px 22px;font-size:13.5px;margin-top:6px}
  .legend .dot{width:9px;height:9px;border-radius:50%;display:inline-block;margin-right:6px;vertical-align:middle}
  .note{margin-top:14px;background:var(--ice);border:1px solid rgba(107,53,36,.18);
    border-radius:11px;padding:13px 15px;font-size:14.5px}
  .note.warn{background:#fff6f5;border-color:rgba(179,38,30,.22)}
  .toc{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px}
  .toc a{font-size:13px;font-weight:700;text-decoration:none;color:var(--navy);
    background:var(--card);border:1px solid var(--line);border-radius:999px;padding:6px 13px}
  .toc a:hover{background:var(--ice)}
  section{margin:0 0 26px}
  .shead{display:flex;align-items:center;gap:9px;margin:0 0 9px}
  .shead .dot{width:11px;height:11px;border-radius:50%;background:var(--indigo)}
  h2{margin:0;font-size:19.5px;color:var(--ink);letter-spacing:-.01em}
  .tag{font-size:12px;font-weight:600;color:var(--muted);background:var(--card);
    border:1px solid var(--line);border-radius:999px;padding:2px 9px;margin-left:6px;vertical-align:2px}
  .scroll{overflow-x:auto;background:var(--card);border:1px solid var(--line);
    border-radius:13px;box-shadow:var(--shadow)}
  table{border-collapse:collapse;width:100%;min-width:760px;font-size:14.5px}
  thead th{position:sticky;top:0;background:var(--navy);color:#fff;text-align:left;
    padding:10px 13px;font-size:12.5px;letter-spacing:.05em;text-transform:uppercase;font-weight:800}
  td{padding:11px 13px;border-top:1px solid var(--line);vertical-align:top}
  tbody tr:nth-child(even){background:#fbfbfd}
  .dn-h{width:20%}.p-h{width:12%}.sl-h{width:9%}
  .dn{font-weight:800;color:var(--ink)}
  .ct u{text-underline-offset:3px;text-decoration-thickness:2px}
  .sl{font-size:12.5px;color:var(--muted);white-space:nowrap}
  .g{color:var(--muted);font-weight:500;font-size:12.5px}
  .pill{display:inline-block;color:#fff;font-size:11px;font-weight:800;letter-spacing:.04em;
    text-transform:uppercase;border-radius:999px;padding:3px 9px;white-space:nowrap}
  tr.t-abs td,tr.t-bbw td{background:#fff6f5}
  tr.t-abs:nth-child(even) td,tr.t-bbw:nth-child(even) td{background:#fff1ef}
  footer{margin-top:34px;color:var(--muted);font-size:13.5px;text-align:center}
  :root[data-theme="dark"] body{background:#12141a;color:#d7dae3}
  :root[data-theme="dark"] .hero,:root[data-theme="dark"] .scroll,
  :root[data-theme="dark"] .toc a{background:#1a1d25;border-color:#2a2e39}
  :root[data-theme="dark"] h1,:root[data-theme="dark"] h2,:root[data-theme="dark"] .dn{color:#eef1f6}
  :root[data-theme="dark"] td{border-color:#2a2e39}
  :root[data-theme="dark"] tbody tr:nth-child(even){background:#1e2129}
  :root[data-theme="dark"] tr.t-abs td,:root[data-theme="dark"] tr.t-bbw td{background:#2a1a19}
  :root[data-theme="dark"] tr.t-abs:nth-child(even) td,
  :root[data-theme="dark"] tr.t-bbw:nth-child(even) td{background:#301d1c}
  :root[data-theme="dark"] .note{background:#241c16;border-color:#4a3324}
  :root[data-theme="dark"] .note.warn{background:#2a1a19;border-color:#5c2723}
  @media(max-width:640px){h1{font-size:25px}.wrap{padding:18px 13px 60px}}
</style>
</head>
<body>
<div id="pull-refresh">
  <svg viewBox="0 0 300 60" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0,30 L120,30 L135,8 L150,52 L165,30 L300,30" vector-effect="non-scaling-stroke" />
  </svg>
</div>
<div class="guide-back-bar">
  <a href="#" class="guide-back-link" onclick="event.preventDefault(); window.guideGoBack();">&larr; Back</a>
</div>
<div class="wrap">

  <header class="hero">
    <div class="kicker">Pharmacology I &middot; Exam 1 &middot; Class of 2028</div>
    <h1>Contraindications &amp; Must-Know Warnings</h1>
    <p class="sub">Every contraindication, prohibition and named reaction in the three Exam 1 decks, in one place.
    __N__ entries, each citing the slide it came from. Built after Dr. McInnis&rsquo;s email that students
    over-study mechanism and under-study <b>indications, patient education, side effects and contraindications</b>.</p>
    <div class="legend">__LEGEND__</div>
    <div class="note"><b>The tiers are not interchangeable, and that is the point.</b> These decks are uneven:
    only __NABS__ statements are actually worded &ldquo;contraindicated&rdquo;, one is a black box warning, and
    __NAVOID__ say avoid / do not use / teratogenic. Everything else is a stated caution or a major adverse
    effect. <b>Nothing here has been promoted a tier above what the slide says</b> &mdash; if a row is marked
    Caution, the deck did not call it a contraindication, however much it sounds like one.</div>
    <div class="note warn"><b>Two things this reference deliberately does NOT contain.</b>
    <b>1. Dosages.</b> Dr. Wood said drug dosages are not tested, so none are reproduced here.
    <b>2. Any race-based contraindication.</b> All 310 slides were searched: <b>there is no contraindication
    keyed to race or ethnicity anywhere in these three decks.</b> If a question offers one, it is not from this
    material. (Race does appear as a <em>risk factor</em> for glaucoma &mdash; but that is the CMS ophthalmology
    deck, a different exam.)
    <b>3. Streptogramins.</b> The Lecture 1 objectives slide names the class, but <b>the deck contains no
    streptogramin slide at all</b> &mdash; no drug, no contraindication. Nothing has been invented to fill
    that gap.</div>
  </header>

  <div class="toc">__TOC__</div>

  <section id="named">
    <div class="shead"><span class="dot" style="background:#1f5d3a"></span>
      <h2>The named reactions <span class="tag">learn these by name</span></h2></div>
    <div class="note">These are the ones a question can name directly &mdash; &ldquo;a patient develops flushing
    of the head and neck during an infusion&rdquo; is asking for one specific drug. Every named reaction on this
    page is <u><b>bold and underlined</b></u> wherever it appears.</div>
    __NAMEDTBL__
  </section>

  <section id="pregnancy">
    <div class="shead"><span class="dot" style="background:#b3261e"></span>
      <h2>Pregnancy, breastfeeding and teratogenicity <span class="tag">the highest-yield group</span></h2></div>
    __PREGTBL__
  </section>

  <section id="age">
    <div class="shead"><span class="dot" style="background:#a4502a"></span>
      <h2>Age-specific warnings <span class="tag">the numbers to memorise</span></h2></div>
    <div class="note"><b>Three numbers carry this section:</b> <b>30 days</b> (ceftriaxone in the newborn),
    <b>8 years</b> (tetracyclines &mdash; teeth and skeletal growth) and <b>18 years</b> (fluoroquinolones
    &mdash; tendon). If a stem gives you a child&rsquo;s age, it is usually testing one of those three. The
    last row is not an age limit but a paediatric-only consequence: topical steroids can retard growth.</div>
    __AGETBL__
  </section>

__SECTIONS__

  <footer>
    Every row cites the deck and slide it came from, and is checked against that slide by
    <code>tools/check_pharm_contra.py</code> before this page is written. Coverage is checked separately by
    <code>tools/check_pharm_contra_coverage.py</code>, which scans all 310 slides for anything a row missed.
    <p style="text-align:center;margin-top:26px;"><a href="../index.html" style="color:inherit;font-weight:700;text-decoration:none;">&larr; Back to Homepage</a></p>
    <p style="text-align:center;font-size:13px;font-style:italic;">&#9733; <a href="#" style="color:inherit;text-decoration:underline;cursor:pointer" onclick="event.preventDefault(); window.reportMistake()">If you see any mistakes, click here to report it</a> &#9733;</p>
  </footer>
</div>
</body>
</html>
"""
    for k, v in (("__NAVY__", NAVY), ("__INDIGO__", INDIGO), ("__GOLD__", GOLD), ("__ICE__", ICE),
                 ("__N__", str(len(ROWS))), ("__LEGEND__", legend), ("__TOC__", toc),
                 ("__NABS__", str(counts["ABS"])), ("__NAVOID__", str(counts["AVOID"])),
                 ("__NAMEDTBL__", minitable(named)), ("__PREGTBL__", minitable(preg)),
                 ("__AGETBL__", minitable(age)), ("__SECTIONS__", "\n".join(secs))):
        html = html.replace(k, v)

    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d rows, %d sections, %d named, %d pregnancy, %d age)"
          % (os.path.basename(OUT), len(html) // 1024, len(ROWS), len(SECTIONS),
             len(named), len(preg), len(age)))


if __name__ == "__main__":
    main()
