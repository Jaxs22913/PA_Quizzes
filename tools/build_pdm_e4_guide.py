#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Principles of Diagnostic Medicine I, Exam 4 study guide.

Exam 4 (Tuesday 1 December 2026) covers Lectures 17-21 and Labs 4-5. The guide grows lecture by
lecture: each per-lecture builder writes a fragment in tools/pdm_e4/l<N>_guide.html (verbatim syllabus
objectives, answered in order; figures from the decks with the slide cited), and this script
assembles whichever fragments exist. Lecture 17 (Pulmonary Imaging, Professor Fowler, guest) is the
first; Lecture 20 (Pulmonary Function Testing and Oxygenation, Professor Fowler; syllabus Topic Outline 18)
the second; Lecture 19 (Acid-Base Balance and Blood Gas Interpretation, Professor Finck; syllabus Topic
Outline 19) the third, placed in lecture order before 20. Labs: lecture content only for now (pdm_exam_spec); lab handling is decided with Jaxon.

Chrome and CSS come from the live Exam 3 guide (the class's current template) with the Exam 4
palette swapped in (film-viewer slate, x-ray blue, dark amber; tools/pdm_e4/palette.json, the same
hues as the Exam 4 quizzes). Added here: the contents sidebar generated from the fragments' own
headings, a "How this exam is written" box, a Test-yourself bank per lecture.

After building: tools/build_guide_docx.py "pdm-exam-4-study-guide.html", then the guide-link
procedure (CLAUDE.md section 7).
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import dark_tokens  # noqa: E402

DONOR = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 3/pdm-exam-3-study-guide.html")
OUTDIR = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 4")
OUT = os.path.join(OUTDIR, "pdm-exam-4-study-guide.html")
FRAG = os.path.join(HERE, "pdm_e4")
IMG = "pdm-exam-4-study-guide-images"
LECTURES = range(17, 22)

TY_KEYS = {17: ("pulmonaryimaging", "Pulmonary Imaging"), 19: ("acidbase", "Acid-Base and Blood Gases"),
           20: ("pulmonaryfunction", "Pulmonary Function Testing")}

# Exam 3 palette -> Exam 4 palette (same roles). Quizzes use navy #1c2733, indigo #3a6797,
# gold #c9873a; amber is too light for heading text, so the guide's third accent is the same hue,
# darker (#8a5a1c, about 5.6:1 on the paper).
ROLE = [
    ("--ink:#1f2024;", "--ink:#1b2129;"),
    ("--paper:#faf8f8;", "--paper:#f8f9fb;"),
    ("--accent:#33363d;      /* monitor charcoal */", "--accent:#26384a;      /* film-viewer slate */"),
    ("--accent2:#b23a48;      /* ECG red */", "--accent2:#3a6797;      /* x-ray blue */"),
    ("--accent3:#8a6420;      /* dark gold */", "--accent3:#8a5a1c;      /* dark amber */"),
    ("--line:#e3dee0;", "--line:#dde3ea;"),
    ("--soft:#5d5a5e;", "--soft:#56606b;"),
    ("linear-gradient(120deg,#1c1e22,var(--accent) 50%,#b23a48)",
     "linear-gradient(120deg,#141c25,var(--accent) 50%,#3a6797)"),
    ("color:#f3e6e8;", "color:#e4ecf5;"),
    ("background:#f2f0f1;", "background:#eff2f6;"),          # toc + figure panels
    ("background:#f5eef0;", "background:#eef2f7;"),          # objectives box
    ("background:#f6f0e3;", "background:#f7f0e6;"),          # callout (amber border)
    ("background:#f8eced;", "background:#ecf2f9;"),          # pearl (blue border)
    ("tr:nth-child(even) td{background:#f5f3f4;}", "tr:nth-child(even) td{background:#f3f5f8;}"),
    ("code{background:#ebe7e8;", "code{background:#e6eaf0;"),
    ("stroke: #b23a48;", "stroke: #3a6797;"),                # pull-refresh + footer mark
    (".footer-mark-ink { stroke: #1f2024; }", ".footer-mark-ink { stroke: #1b2129; }"),
    (".footer-mark-accent { stroke: #e8a3ac; }", ".footer-mark-accent { stroke: #a9c3e0; }"),
]
E3_HEXES = ("#1f2024", "#faf8f8", "#33363d", "#b23a48", "#8a6420", "#e3dee0", "#5d5a5e", "#1c1e22",
            "#f3e6e8", "#f2f0f1", "#f5eef0", "#f6f0e3", "#f8eced", "#f5f3f4", "#ebe7e8", "#e8a3ac")

HOW = '''<div class="prof-flag"><span class="prof-flag-label">&#9733; How this exam is written</span>
  <p>Exam 4 is the pulmonary block. The course rules below come from Professor Reynolds&rsquo; first lecture and hold for every exam in this class; the last rows are what they mean for imaging, for blood gases and for pulmonary function testing.</p>
  <table>
    <tr><th>The rule</th><th>What it means for you</th></tr>
    <tr><td><em>&ldquo;I&rsquo;m not going to just throw a random number at you and not give you context of whether that&rsquo;s high or low.&rdquo;</em> (Professor Reynolds, Lecture 1)</td><td><strong>Reference ranges are supplied.</strong> A creatinine or any other value in a stem comes with the range that reads it. Learn what a value <em>means</em>.</td></tr>
    <tr><td><em>&ldquo;It&rsquo;s going to likely be more related to the tests themselves rather than maybe the specific diagnosis.&rdquo;</em> (Lecture 1)</td><td>Which study, why, its cautions and what normal looks like on it carry most of the marks (17.7).</td></tr>
    <tr><td>Questions are vignette and next-best-test: <em>&ldquo;what would be the next test that you would order?&rdquo;</em></td><td>In imaging the next test is a study: the radiograph first; the angiogram first for a suspected pulmonary embolism; computed tomography when the radiograph is inconclusive; the ventilation/perfusion scan when contrast cannot be given (17.7).</td></tr>
    <tr><td>Images are in play: radiographs and scans alongside the vignette.</td><td>Expect a film or a slice. Read the technique first (17.6), then the structures (17.1&ndash;17.5), then the pattern (17.8).</td></tr>
    <tr><td>Blood gases: every pH, gas pressure, bicarbonate and electrolyte in a stem comes with its normal range. The anion gap is the one calculation: <em>&ldquo;I do want you to memorize and understand this equation&rdquo;</em> (Professor Finck, Lecture 19).</td><td>Read the gas step by step: the pH, then the values outside their range (the carbon dioxide for the lungs, the bicarbonate for the metabolic side), then whether the labs fit the patient (19.5). Know the four patterns and their compensation (19.5, 19.6). Work out the gap as sodium minus (chloride plus bicarbonate), with no potassium (19.7).</td></tr>
    <tr><td>Pulmonary function tests: a value comes with its reference (percent of predicted, or the report&rsquo;s own reference column).</td><td>Read a report in order: the ratio first, then the forced vital capacity, then the total lung capacity (20.6). Expect a tracing, a loop or a report: know the normal shapes and the scoop and the witch&rsquo;s hat (20.5). The next test: spirometry for obstruction, lung volumes for restriction, the diffusing capacity for a gas transfer problem (20.7).</td></tr>
  </table>
</div>'''

# Five short self-checks per lecture, written from the sections above (each fact is stated in its own
# section). Correct positions are spread on purpose: openTestYourself shows choices in the order given.
TY = {
 "pulmonaryimaging": [
  {"q": "Which chest radiograph view magnifies the heart?",
   "choices": ["Posteroanterior, standing", "Anteroposterior, supine", "Lateral", "Water's view"], "correct": 1,
   "explain": "The supine anteroposterior film magnifies the heart, so a large-looking heart on that view is not, by itself, an enlarged heart. The posteroanterior view is taken standing (ambulatory)."},
  {"q": "How is rotation best assessed on a frontal chest film?",
   "choices": ["From the tracheal shadow", "By counting posterior ribs", "Spinous processes to the clavicle borders", "From the height of the hila"], "correct": 2,
   "explain": "Measure the distance from the center spinous processes to the borders of the clavicles. Do not use the tracheal shadow: the trachea is a tube and looks the same when rotated. Counting ribs measures inspiration."},
  {"q": "Which study comes first for a suspected pulmonary embolism?",
   "choices": ["Computed tomography angiogram", "Chest radiograph", "Ventilation/perfusion scan", "Pulmonary ultrasound"], "correct": 0,
   "explain": "Suspected pulmonary embolism is the one case where computed tomography comes before the radiograph. The ventilation/perfusion scan is inferior and is used when contrast cannot be given."},
  {"q": "What causes Kerley B lines?",
   "choices": ["Air in the pleural space", "Fluid in the pleural space", "Fibrotic pull on the airways", "Thickened interlobular septa"], "correct": 3,
   "explain": "Kerley B lines are short, thin, horizontal lines at the outer edges of the lower lungs from thickening of the interlobular septa, a sign of pulmonary edema."},
  {"q": "What is the classic radiograph sign of a pleural effusion?",
   "choices": ["Jet-black space with a compressed lung", "Blunted costophrenic angles", "Honeycombing", "Cephalization of vessels"], "correct": 1,
   "explain": "The normally sharp costophrenic angles are blunted. Jet-black space with a compressed lung is a pneumothorax; honeycombing is interstitial lung disease; cephalization is edema."},
 ],
 "acidbase": [
  {"q": "Which value is looked at first in a step-wise read of a blood gas?",
   "choices": ["The carbon dioxide pressure", "The bicarbonate", "The pH", "The anion gap"], "correct": 2,
   "explain": "Step one is the pH (low is acidosis, high is alkalosis); then which values are outside the normal range; then whether the labs fit the clinical presentation."},
  {"q": "pH low, carbon dioxide high, bicarbonate normal: which disorder?",
   "choices": ["Acute respiratory acidosis", "Metabolic acidosis", "Chronic respiratory acidosis", "Respiratory alkalosis"], "correct": 0,
   "explain": "Acute respiratory acidosis: pH below 7.35, carbon dioxide high, bicarbonate normal, as with respiratory depression from opioids or barbiturates. A risen bicarbonate would mean the chronic, compensated form."},
  {"q": "How does the body compensate for a metabolic acidosis?",
   "choices": ["The kidneys raise the bicarbonate over days", "Breathing lowers the carbon dioxide", "Breathing raises the carbon dioxide", "The kidneys lower the bicarbonate"], "correct": 1,
   "explain": "Metabolic disorders are compensated by adjusting the ventilatory rate and carbon dioxide over minutes to hours: metabolic acidosis by a decrease in carbon dioxide. Kidney bicarbonate changes compensate respiratory disorders."},
  {"q": "In acidosis, which way does potassium move?",
   "choices": ["Into the cells: hypokalemia", "Into the urine only", "It does not move", "Out of the cells: hyperkalemia"], "correct": 3,
   "explain": "pH changes cause changes in serum potassium: acidosis shifts potassium into the extracellular space (hyperkalemia); alkalosis shifts it into the cells (hypokalemia)."},
  {"q": "Sodium 140, chloride 102, bicarbonate 24 (mEq/L): what is the anion gap?",
   "choices": ["14", "24", "38", "62"], "correct": 0,
   "explain": "Anion gap = sodium minus (chloride plus bicarbonate) = 140 minus 126 = 14, inside the normal 9 to 15. Forgetting the bicarbonate gives 38."},
 ],
 "pulmonaryfunction": [
  {"q": "Which value is assessed first when reading spirometry?",
   "choices": ["The forced vital capacity", "The ratio of the two forced values", "The total lung capacity", "The peak expiratory flow"], "correct": 1,
   "explain": "Assess the ratio (forced expiratory volume in one second over forced vital capacity) first, then the forced vital capacity. A low ratio is obstruction; a normal or high ratio with a low forced vital capacity is possible restriction."},
  {"q": "A ratio below which value indicates obstruction?",
   "choices": ["50%", "70%", "80%", "90%"], "correct": 1,
   "explain": "Below 70% indicates obstruction; a normal ratio is more than 80%. Restriction keeps the ratio normal or increased, 70% or more."},
  {"q": "What shape is the restrictive flow-volume loop?",
   "choices": ["Narrow and tall, like a witch's hat", "Scooped after the peak (coving)", "Wide with a long flat tail", "The same as normal"], "correct": 0,
   "explain": "The restrictive loop keeps the normal shape but everything is smaller: narrow, with a sharp point. A scoop in the loop (coving) is obstruction."},
  {"q": "Which standard test diagnoses pulmonary vascular disease?",
   "choices": ["Spirometry", "Lung volumes", "Peak flow", "Diffusing capacity for carbon monoxide"], "correct": 3,
   "explain": "The diffusing capacity measures the integrity of the alveolar-capillary membrane and diagnoses pulmonary vascular disease. Spirometry diagnoses obstruction and lung volumes restriction."},
  {"q": "Which volume can never be breathed out?",
   "choices": ["Expiratory reserve volume", "Residual volume", "Tidal volume", "Inspiratory reserve volume"], "correct": 1,
   "explain": "The residual volume is the air still in the lung after maximal expiration. Whole-body plethysmography measures it, with the total lung capacity, the functional residual capacity and airway resistance."},
 ],
}


def toc_for(n, frag):
    m = re.search(r'<section class="deck" id="([^"]+)">\s*<h2 class="deck-title"[^>]*>(.*?)</h2>', frag, re.S)
    assert m, "lecture %d: no section/deck-title" % n
    out = ['  <a class="top-link" href="#%s">%s</a>' % (m.group(1), m.group(2).strip())]
    for sid, txt in re.findall(r'<h3 class="sub" id="([^"]+)">(.*?)</h3>', frag, re.S):
        out.append('  <a href="#%s">%s</a>' % (sid, txt.strip()))
    return m.group(1), out


def section(n):
    frag = open(os.path.join(FRAG, "l%d_guide.html" % n), encoding="utf-8").read().strip()
    assert frag.startswith('<section class="deck"') and frag.endswith("</section>"), n
    assert frag.count("<section") == 1 and "<details" not in frag, n
    assert '<footer class="guide-foot">' in frag, "lecture %d: the fragment carries its own source footer" % n
    # The deck title gets its own id so the lecture's opening (frame, emphasis box) is its own
    # linkable section for build_guide_links.py.
    sid = re.search(r'<section class="deck" id="([^"]+)">', frag).group(1)
    frag = frag.replace('<h2 class="deck-title">', '<h2 class="deck-title" id="%s-top">' % sid, 1)
    key, title = TY_KEYS[n]
    btn = ('<button type="button" class="test-yourself-btn" style="--acc:#3a6797" '
           "onclick=\"window.openTestYourself('Test yourself &mdash; %s', TEST_YOURSELF.%s)\">"
           "Test yourself! &rarr;</button>\n" % (title, key))
    i = frag.rindex('<footer class="guide-foot">')
    return frag[:i] + btn + "  " + frag[i:]


def ty_script():
    for key, qs in TY.items():
        assert len(qs) == 5, key
        for q in qs:
            assert len(q["choices"]) == 4 and 0 <= q["correct"] < 4, q["q"]
            assert len(set(q["choices"])) == 4, q["q"]
    return ("<script>\n  // High-yield \"Test yourself\" question sets, one per lecture, fed to\n"
            "  // window.openTestYourself (theme.js) by each section's button.\n"
            "  var TEST_YOURSELF = " + json.dumps(TY, indent=2, ensure_ascii=False) + ";\n</script>")


def main():
    donor = open(DONOR, encoding="utf-8").read()
    head = donor[:donor.index('<div class="layout wrap" data-readable>')]
    tail = donor[donor.index("</script>", donor.index("var TEST_YOURSELF")) + len("</script>"):]
    head = head.replace("Principles of Diagnostic Medicine I &middot; Exam 3 &mdash; Study Guide",
                        "Principles of Diagnostic Medicine I &middot; Exam 4 &mdash; Study Guide")
    head = re.sub(r'\s*<link rel="alternate"[^>]*>\n', "\n", head)   # build_guide_docx.py adds ours
    head = re.sub(r"<header class=\"top\">.*?</header>", '''<header class="top">
  <h1>Principles of Diagnostic Medicine I &middot; Exam 4 &mdash; Study Guide</h1>
  <p>PAJ 5600 Principles of Diagnostic Medicine I &middot; Class of 2028 &middot; Exam Tuesday 1 December 2026</p>
  <p>Covers Lectures 17&ndash;21 and Labs 4&ndash;5 (lecture content; built lecture by lecture) &middot; Instructional Objectives (IOs) taken verbatim from the syllabus</p>
</header>''', head, flags=re.S)
    for a, b in ROLE:
        assert a in head, "donor changed, role not found: " + a
        head = head.replace(a, b)
    css = head[:head.index("</head>")]
    css_wo_tokens = re.sub(r"<!--DARK-TOKENS:BEGIN.*?DARK-TOKENS:END-->", "", css, flags=re.S).lower()
    left = [h for h in E3_HEXES if h in css_wo_tokens]
    assert not left, "Exam 3 colours left in the head: %r" % left

    toc = ['<nav class="toc">', "  <h2>Contents</h2>"]
    sections = []
    for n in LECTURES:
        if not os.path.exists(os.path.join(FRAG, "l%d_guide.html" % n)):
            continue
        frag = section(n)
        _sid, entries = toc_for(n, frag)
        toc += entries
        sections.append(frag)
    assert sections, "no lecture fragments"
    toc.append("</nav>")

    body = ('<div class="layout wrap" data-readable>\n' + "\n".join(toc) + "\n\n<main>\n" + HOW + "\n\n" +
            "\n\n".join(sections) + '''

<footer class="guide-foot">
  <p style="text-align:center;margin:0 0 10px;"><a href="../index.html" style="color:inherit;font-weight:700;text-decoration:none;">&larr; Back to Homepage</a></p>
  <p style="text-align:center;">Built from your PAJ 5600 lecture decks for personal study &middot; Class of 2028.</p>
  <p style="text-align:center;font-style:italic;">&#9733; <a href="#" style="color:inherit;text-decoration:underline;cursor:pointer" onclick="event.preventDefault(); window.reportMistake()">If you see any mistakes, click here to report it</a> &#9733;</p>
</footer>
</main>
</div>
''' + ty_script())
    html = head + body + tail
    html = dark_tokens.apply(html, "guide")

    # guards
    assert "guide-back-bar" in html and "window.reportMistake()" in html
    assert "data-audio-dir" not in html
    assert ("<" + "details") not in html
    ids = re.findall(r'\bid="([^"]+)"', html)
    dup = sorted({i for i in ids if ids.count(i) > 1})
    assert not dup, "duplicate ids %r" % dup
    for m in re.finditer(r'href="#([A-Za-z0-9_-]+)"', html):
        assert 'id="%s"' % m.group(1) in html, "dangling link #" + m.group(1)
    srcs = re.findall(r'src="(%s/[^"]+)"' % IMG, html)
    for s in srcs:
        assert os.path.exists(os.path.join(OUTDIR, s)), s
    on_disk = set(os.listdir(os.path.join(OUTDIR, IMG)))
    unused = on_disk - {s.split("/", 1)[1] for s in srcs}
    assert not unused, "guide images nobody uses: %r" % sorted(unused)
    for k in TY:
        assert "TEST_YOURSELF.%s)" % k in html, k
    brit = re.findall(r"(?i)\b\w*(?:haem|oedem|tumour|colour|centre|anaem|oesoph|isation|oris[ei]|ognis[ei]|emphasis[ei]|analys[ei]|optimis|visualis|characteris|memoris|summaris)\w*\b", body)
    brit = [w for w in brit if w.lower() not in ("haemophilus", "analysis", "analyses", "angioedema")]
    assert not brit, "British spelling: %r" % sorted(set(brit))
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d figures, %d sections, %d subsections, %d TOC links)" % (
        os.path.relpath(OUT, ROOT), len(html) // 1024, html.count('<figure class="fig">'),
        html.count('<section class="deck"'), html.count('<h3 class="sub"'), len(toc) - 3))


if __name__ == "__main__":
    main()
