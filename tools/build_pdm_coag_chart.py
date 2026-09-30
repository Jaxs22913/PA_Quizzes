#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the PDM I Exam 2 reference chart of the coagulation and hemostasis tests.

Lecture 10, Professor Lauren Reynolds. EVERY value and pattern is taken from the deck
("Coagulation Studies 2026.pptx") and cites its slide; nothing is added from outside it. Where the
deck's own figures disagree with its text or with current practice, the page says so in a note
rather than choosing silently (truth wins; see the guide, section 10).

Four tables:
  1. The tests: what each measures, its pathway or phase, the reference value, and what an abnormal
     result suggests.
  2. Patterns: the condition-by-test grids from slides 24, 29 and 30, typed from the pictures.
  3. The two algorithms (slides 27 and 28) as step tables.
  4. Platelet count tiers and platelet findings (slides 13, 25, 26, 34).

The page shell follows the Pharmacology reference charts (light palette only; theme.css inverts
body > .wrap in dark mode, so dark colors are NOT declared here).
"""
import html, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 2", "coagulation-tests-reference-chart.html")
NAVY, INDIGO, GOLD, ICE = "#7a2a2e", "#a1363a", "#b8862f", "#fbf1f0"
STAR = '<span class="star" title="Emphasized in the lecture recording">&#9733;</span>'
EMPH = {"platelet-count", "vwf", "inr", "ddimer", "dic", "uremia", "aptt"}   # rows the 30 September recording emphasized

CSS = r"""<style>
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
  .note{margin-top:14px;background:var(--ice);border:1px solid rgba(122,42,46,.18);
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
  .dn{font-weight:800;color:var(--ink)}
  .sl{font-size:12.5px;color:var(--muted);white-space:nowrap}
  .star{color:#8a5a00;font-weight:800;margin-right:3px}
  .up{font-weight:800;color:#8a1f1f}.dn2{font-weight:800;color:#1f5566}.nl{color:var(--muted)}
  footer{margin-top:34px;color:var(--muted);font-size:13.5px;text-align:center}
  /* NO dark palette on purpose: theme.css does dark mode by inverting body > .wrap. */
  @media(max-width:640px){h1{font-size:25px}.wrap{padding:18px 13px 60px}}
</style>"""

PAGE = """<!DOCTYPE html>
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
<title>Coagulation Tests Reference Chart &mdash; PDM I Exam 2</title>
__CSS__
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
    <div class="kicker">Principles of Diagnostic Medicine I &middot; Exam 2 &middot; Lecture 10</div>
    <h1>Coagulation Tests Reference Chart</h1>
    <p class="sub">Every test in the lecture in one place: what it measures, its pathway, its reference value, what an abnormal result suggests, and the patterns that tie results together. Every value comes from the lecture deck; the slide is cited on each row.</p>
    <div class="note"><b>Read this page as a way to interpret results, not as numbers to memorize.</b> Reference ranges vary by laboratory and are supplied on the exam. Nothing here is calculated.</div>
    <div class="note warn"><b>Where the deck and its own figures differ, this chart says which it teaches.</b> (1) The deck defines thrombocytopenia as a count below 100,000 per microliter although its adult reference starts at 140,000. (2) Bleeding time is listed as a screening test but is poorly reproducible and has largely given way to platelet function analysis. (3) Slide 22 titles fibrin monomers &ldquo;fibrin split products&rdquo;; fibrin degradation products come from plasmin, while the fibrin-monomer result reflects thrombin. (4) The slide 25 figure files hypersplenism under &ldquo;dilutional&rdquo;; it lowers the count by sequestration.</div>
  </header>

  <div class="toc"><a href="#tests">The tests</a><a href="#patterns">Patterns by condition</a><a href="#algorithms">The two algorithms</a><a href="#platelets">Platelet findings</a></div>

__BODY__

  <footer>
    Source: <em>Coagulation Studies 2026.pptx</em> (Professor Lauren Reynolds), slides cited on each row. Condensed from the Exam 2 study guide, section 10. &#9733; = emphasized in the 30 September 2026 lecture recording.
    <p style="text-align:center;margin-top:26px;"><a href="../index.html" style="color:inherit;font-weight:700;text-decoration:none;">&larr; Back to Homepage</a></p>
    <p style="text-align:center;font-size:13px;font-style:italic;">&#9733; <a href="#" style="color:inherit;text-decoration:underline;cursor:pointer" onclick="event.preventDefault(); window.reportMistake()">If you see any mistakes, click here to report it</a> &#9733;</p>
  </footer>
</div>
</body>
</html>
"""

# ------------------------------------------------------------------ data (all from the deck)
TESTS = [
  # key, test, measures, phase/pathway, reference, abnormal means, slide
  ("platelet-count", "Platelet count", "How many platelets there are (complete blood count)", "Primary hemostasis",
   "Adults 140,000&ndash;400,000 per microliter; children 150,000&ndash;450,000", "Low = thrombocytopenia (deck: below 100,000); high = thrombocytosis (deck: above 350,000). Below 50,000 bruises easily; below 20,000 spontaneous bleeding and petechiae; below 10,000 risk of intracranial bleeding.", "13, 26"),
  ("mpv", "Mean platelet volume", "Uniformity of platelet size", "Primary hemostasis",
   "7.4&ndash;10.4 femtoliters", "Used in the differential diagnosis of thrombocytopenia.", "13"),
  ("smear", "Peripheral blood smear", "Platelet morphology", "Primary hemostasis",
   "&mdash;", "Gray platelets (macrothrombocytopenia), neutrophil inclusions, clumps (spurious low count), schistocytes (thrombotic thrombocytopenic purpura).", "11, 14, 15, 34"),
  ("vwf", "von Willebrand studies", "von Willebrand factor antigen and activity, plus factor VIII level", "Primary hemostasis",
   "&mdash;", "Abnormal = von Willebrand disease, the most common inherited bleeding disorder.", "11"),
  ("pft", "Platelet function testing", "Whether platelets aggregate and work: light transmission aggregometry, lumiaggregometry, platelet function analyzer, flow cytometry", "Primary hemostasis",
   "&mdash;", "Abnormal with normal clotting times and bleeding = platelet dysfunction: von Willebrand types 2 and 3, uremia, drugs.", "11, 29, 34"),
  ("bt", "Bleeding time", "Minutes for a standardized skin puncture to stop bleeding (bedside)", "Primary hemostasis",
   "3&ndash;10 minutes (varies by method)", "Only useful if platelet count is above 100,000 per microliter; thrombocytopenia itself lengthens it.", "16, 17"),
  ("pt", "PT (prothrombin time)", "Time for a clot to form after tissue factor is added to plasma; prothrombin is liver-made and vitamin K dependent", "Secondary: extrinsic + common",
   "11&ndash;13 seconds (varies by laboratory)", "Prolonged: factor VII or common pathway deficiency, liver disease, vitamin K deficiency, warfarin.", "19"),
  ("inr", "INR (international normalized ratio)", "The PT expressed so it is comparable between laboratories", "Secondary: extrinsic + common",
   "0.8&ndash;1.2; on anticoagulation typical goal 2.0&ndash;3.0", "On warfarin: low = clot risk, high = bleeding risk. Off warfarin: bleeding disorder, clotting disorder, liver disease or vitamin K deficiency.", "20"),
  ("aptt", "aPTT (activated partial thromboplastin time)", "Time for a clot to form after a phospholipid activator is added to plasma", "Secondary: intrinsic + common",
   "21&ndash;35 seconds; above 70 seconds signifies spontaneous bleeding", "Prolonged: factor VIII, IX, XI deficiency; von Willebrand disease; heparin; dabigatran; inhibitor; lupus anticoagulant; factor XII.", "18"),
  ("tt", "Thrombin time", "Screening test of secondary hemostasis (the deck gives no definition)", "Secondary",
   "(no value given)", "Raised by heparin and dabigatran, in disseminated intravascular coagulation and with low or abnormal fibrinogen; normal in a simple factor deficiency.", "12, 24, 29"),
  ("fib", "Fibrinogen", "The substrate thrombin turns into fibrin; Clauss assay preferred over PT-derived", "Secondary",
   "2.0&ndash;4.0 grams per liter", "Low = bleed (below 0.5 g/L: hemorrhage after traumatic surgery). High = clot (above 7.0 g/L: coronary and cerebrovascular risk); raised in tissue damage or inflammation.", "12, 21"),
  ("mix", "Mixing study", "Patient plasma mixed with normal plasma, then the prolonged test repeated", "Secondary",
   "&mdash;", "Corrects = factor deficiency. Does not correct = inhibitor.", "12"),
  ("factor", "Factor assays", "Level of one specific factor", "Secondary",
   "&mdash;", "Confirm a deficiency; inherited or acquired; acquired can raise or lower factors.", "12, 21"),
  ("ddimer", "D-dimer", "Degradation product of cross-linked fibrin (plasmin acting on it)", "Fibrinolysis",
   "Below 250 micrograms per liter", "Raised = both thrombin and plasmin were generated; NONSPECIFIC (acute thrombosis, disseminated intravascular coagulation, pregnancy, many illnesses). A normal result helps exclude thrombosis.", "22, 23"),
  ("fm", "Fibrin monomers", "Thrombin activity on fibrinogen", "Fibrinolysis / intravascular coagulation",
   "&mdash;", "Positive = thrombin activity, consistent with intravascular coagulation; negative does NOT exclude it; also positive in severe liver disease and inflammation.", "22"),
]

UP, DOWN, NL = '<span class="up">&uarr; Up</span>', '<span class="dn2">&darr; Down</span>', '<span class="nl">Normal</span>'
def cell(v):
    return {"u": UP, "d": DOWN, "n": NL, "-": "&mdash;"}.get(v, v)

# slide 24 + 29 + 30 combined, typed
PATTERNS = [
  # key, condition, PT, aPTT, TT, fibrinogen, D-dimer, platelets, PFA, what to think, slide
  # "-" = the deck does not state it for this row (shown as a dash, never guessed)
  ("dic", "Acute DIC (disseminated intravascular coagulation)", "u", "u", "u", "d", "u", "d", "Abnormal", "Consumption: long clotting times, low fibrinogen and platelets, raised D-dimer and fibrin degradation products; protein C, antithrombin and protein S fall.", "24, 29, 30"),
  ("thrombosis", "Acute thrombosis", "n", "n", "-", "n", "u", "n", "&mdash;", "Only the D-dimer rises (nonspecific).", "24"),
  ("vka", "Vitamin K antagonist, liver disease, factor VII deficiency", "u", "n", "-", "n", "n", "n", "&mdash;", "Isolated long PT: extrinsic pathway and vitamin K dependent factors (an oral factor Xa inhibitor is also listed). Early liver failure: platelet function normal.", "24, 29, 32"),
  ("heparin", "Heparin or dabigatran", "n", "u", "u", "n", "n", "n", "&mdash;", "Long aPTT and thrombin time; with heparin the reptilase time stays normal and the mixing study does not correct.", "24, 29"),
  ("hemophilia", "Hemophilia A or B", "n", "u", "n", "-", "-", "n", "Normal", "Mixing study corrects. Low factor VIII with normal von Willebrand studies = hemophilia.", "29, 27"),
  ("vwd", "von Willebrand disease", "n", "u", "-", "-", "-", "n", "Abnormal", "aPTT rises through low factor VIII; platelet function is abnormal.", "29"),
  ("inhibitor", "Inhibitor (factor VIII, IX, XI, XII) or lupus anticoagulant", "n", "u", "n", "n", "n", "n", "&mdash;", "Mixing study does not correct. Lupus anticoagulant or factor XII deficiency: no bleeding history.", "24, 29"),
  ("lowfib", "Low fibrinogen", "u", "u", "u", "d", "-", "-", "&mdash;", "Both clotting times and the thrombin time rise; mixing corrects.", "29"),
  ("uremia", "Uremia, aspirin or nonsteroidal anti-inflammatory drugs", "n", "n", "-", "-", "-", "n", "Abnormal", "Platelet dysfunction: normal clotting times and count, abnormal platelet function analysis.", "29"),
  ("itp", "Immune thrombocytopenia, thrombotic thrombocytopenic purpura, hemolytic uremic syndrome, heparin-induced thrombocytopenia", "n", "n", "-", "-", "-", "d", "Normal", "A low platelet count with normal clotting times.", "29"),
  ("liver-late", "Liver failure, late or severe", "u", "u", "-", "-", "-", "d", "Abnormal", "Both clotting times rise and platelets fall.", "29"),
]

ALGO_PTT = [
  ("1", "Isolated prolonged aPTT", "Rule out heparin effect first.", "27"),
  ("2", "Measure fibrinogen activity", "High (above 100 mg/dL): mix. Low (below 100 mg/dL): fibrinogen antigen &rarr; low = hypofibrinogenemia, normal = dysfibrinogenemia.", "27"),
  ("3", "1:1 mixing study", "Corrects = factor deficiency; fails to correct = inhibitor.", "27"),
  ("4", "If it corrects", "Factor VIII assay. Low without an inhibitory curve &rarr; von Willebrand antigen and activity: abnormal = von Willebrand disease, normal = hemophilia. Normal factor VIII &rarr; assays for factors IX, XI, XII.", "27"),
  ("5", "If it fails to correct", "Phospholipid dependence (dilute Russell viper venom time): yes = lupus anticoagulant; no = specific factor inhibitor (inhibitor screen, Bethesda assay).", "27"),
]
ALGO_INH = [
  ("Screens normal", "Platelet disorders and mild von Willebrand disease", "Skin bruising, petechiae, mucous membrane bleeding", "Platelet function analyzer closure time or bleeding time, count and morphology, aggregation, von Willebrand studies", "28"),
  ("Screens normal", "Deficiency of inhibitors of the fibrinolytic system", "Severe bleeding: hemarthroses, hematoma after trauma or surgery", "Euglobulin clot lysis time; alpha-2 antiplasmin; plasminogen activator inhibitor 1", "28"),
  ("Screens normal", "Factor XIII deficiency", "Umbilical stump bleeding; lifelong severe bleeding of any tissue", "Clot stability test; factor XIII assay", "28"),
  ("PT only prolonged", "Factor VII deficiency", "Clotting factor deficiency: large palpable ecchymoses, deep bleeding into joints and muscles with hematoma", "Selective factor assays", "28"),
  ("aPTT only prolonged", "Factor VIII (hemophilia A), IX (hemophilia B) or XI; severe von Willebrand disease", "As above", "Selective factor assays", "28"),
  ("PT and aPTT prolonged", "Normal thrombin time: factor X, V or II. Prolonged thrombin time: hypofibrinogenemia or dysfibrinogenemia", "As above", "Fibrinogen activity and antigen assays", "28"),
]
TIERS = [
  ("Below 50,000 per microliter", "May bleed excessively with mild or moderate trauma and with surgery involving mucous membranes; bruises easily", "26"),
  ("Below 20,000", "Spontaneous bleeding; petechiae", "26"),
  ("Below 10,000", "Risk of spontaneous intracranial bleeding and serious hemorrhage", "26"),
]
FINDINGS = [
  ("Quantitative", "Thrombocytopenia and extreme thrombocythemia (above 1,000 &times; 10<sup>9</sup> per liter) can both cause bleeding. Confirm a low count in a citrated or heparinized tube to exclude pseudothrombocytopenia induced by ethylenediaminetetraacetic acid (clumping).", "34"),
  ("Morphology", "Macrothrombocytopenia (gray platelet syndrome); neutrophil inclusions (May-Hegglin anomaly, a myosin heavy chain 9 disorder); platelet clumps; schistocytes in thrombotic thrombocytopenic purpura.", "14, 15, 34"),
  ("Qualitative", "Normal PT and aPTT with bleeding suggests platelet dysfunction; abnormal platelet function testing points to von Willebrand types 2 and 3, uremia or drugs.", "34"),
  ("Causes of a low count", "Impaired production; increased destruction (immune mechanisms, microangiopathy such as thrombotic thrombocytopenic purpura and hemolytic uremic syndrome, consumptive coagulopathy such as DIC); dilution (massive transfusion); sequestration (hypersplenism).", "25, 36"),
]


def star(key, text):
    return (STAR if key in EMPH else "") + text


def table(head, rows, cls=""):
    th = "".join("<th>%s</th>" % h for h in head)
    return '<div class="scroll"><table%s><thead><tr>%s</tr></thead><tbody>\n%s\n</tbody></table></div>' % (cls, th, "\n".join(rows))


def section(sid, title, tag, body):
    return ('  <section id="%s">\n    <div class="shead"><span class="dot"></span><h2>%s</h2><span class="tag">%s</span></div>\n    %s\n  </section>\n'
            % (sid, title, tag, body))


def build():
    r1 = ['<tr><td class="dn">%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td class="sl">%s</td></tr>'
          % (star(k, t), m, p, ref, ab, sl) for k, t, m, p, ref, ab, sl in TESTS]
    t1 = table(["Test", "What it measures", "Phase / pathway", "Reference (varies by lab)", "Abnormal means", "Slide"], r1)
    r2 = ['<tr><td class="dn">%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td class="sl">%s</td></tr>'
          % (star(k, cond), cell(pt), cell(ap), cell(tt), cell(fb), cell(dd), cell(pl), pf, think, sl)
          for k, cond, pt, ap, tt, fb, dd, pl, pf, think, sl in PATTERNS]
    t2 = table(["Condition", "PT (prothrombin time)", "aPTT (activated partial thromboplastin time)", "Thrombin time", "Fibrinogen", "D-dimer", "Platelets", "Platelet function", "What to think", "Slide"], r2)
    t2 = t2.replace("min-width:760px", "min-width:1000px")
    r3 = ['<tr><td class="dn">%s</td><td>%s</td><td>%s</td><td class="sl">%s</td></tr>' % (n, a, b, sl) for n, a, b, sl in ALGO_PTT]
    t3 = table(["Step", "Do", "Result and next", "Slide"], r3)
    r4 = ['<tr><td class="dn">%s</td><td>%s</td><td>%s</td><td>%s</td><td class="sl">%s</td></tr>' % row for row in ALGO_INH]
    t4 = table(["Screens", "Think", "Clinical clue", "Next tests", "Slide"], r4)
    r5 = ['<tr><td class="dn">%s</td><td>%s</td><td class="sl">%s</td></tr>' % row for row in TIERS]
    t5 = table(["Platelet count", "Bleeding risk", "Slide"], r5)
    r6 = ['<tr><td class="dn">%s</td><td>%s</td><td class="sl">%s</td></tr>' % row for row in FINDINGS]
    t6 = table(["Kind", "Finding", "Slide"], r6)
    body = (section("tests", "The tests", "%d tests" % len(TESTS), t1)
            + section("patterns", "Patterns by condition", "slides 24, 29, 30", t2)
            + section("algorithms", "The two algorithms", "slides 27, 28",
                      "<p><b>Isolated prolonged aPTT (slide 27)</b></p>" + t3 + "<p style=\"margin-top:18px\"><b>Suspected inherited bleeding disorder (slide 28)</b></p>" + t4)
            + section("platelets", "Platelet findings", "slides 13, 25, 26, 34", t5 + "<p></p>" + t6))
    out = PAGE.replace("__CSS__", CSS.replace("__NAVY__", NAVY).replace("__INDIGO__", INDIGO)
                       .replace("__GOLD__", GOLD).replace("__ICE__", ICE)).replace("__BODY__", body)
    assert not re.search(r"(?i)ha[e]m|o[e]dem|tumo[u]r|colo[u]r|cent[r]e|ana[e]m", out)
    open(OUT, "w", encoding="utf-8").write(out)
    print("wrote %s (%d KB, %d tests, %d patterns)" % (os.path.basename(OUT), len(out) // 1024, len(TESTS), len(PATTERNS)))


if __name__ == "__main__":
    build()
