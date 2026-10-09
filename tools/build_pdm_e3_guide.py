#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Principles of Diagnostic Medicine I, Exam 3 study guide.

Exam 3 (Wednesday 14 October 2026) covers Lectures 11-16, the electrocardiography
block, all six given by Scott Mathis (EMS educator, First Response Training Group;
named on each deck's title slide and confirmed by the recordings; the calendar's
"Professor Elwaya" is only the scheduled name). Lab 3 is deliberately absent:
Jaxon decided "Lectures only" for this exam (2026-10-08).

The six lecture sections are written by the per-lecture builders as fragments in
tools/pdm_e3/l<N>_guide.html (verbatim syllabus objectives, answered in order;
figures cropped from the decks with the slide cited). This script only assembles:
chrome and CSS from the live Exam 2 guide (the class's current template), a fresh
per-exam palette that matches the Exam 3 quizzes (charcoal monitor, ECG red, dark
gold), the contents sidebar generated from the fragments' own headings, a
"How this exam is written" box, a Test-yourself bank per lecture, and a source
footer for the sections whose fragment carries none.

After building: tools/apply_guide_additions.py (the "Also tested" blocks),
tools/build_guide_docx.py "pdm-exam-3-study-guide.html", then the guide-link
procedure (CLAUDE.md section 7).
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import dark_tokens  # noqa: E402

DONOR = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 2/pdm-exam-2-study-guide.html")
OUTDIR = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 3")
OUT = os.path.join(OUTDIR, "pdm-exam-3-study-guide.html")
FRAG = os.path.join(HERE, "pdm_e3")
IMG = "pdm-exam-3-study-guide-images"

LECTURER = "Scott Mathis, EMS (emergency medical services) educator, First Response Training Group"
DECKS = {
    11: "11. Rhythm Analysis and Sinus Rhythm.pptx",
    12: "12. Ectopy, Escape Rhythms and Supraventricular Dysrhythmias.pptx",
    13: "13. Ventricular Dysrhythmias and Atrioventricular Blocks.pptx",
    14: "14. EKG Axis, BBB.pptx",
    15: "15. EKG Ischemia and Infarction.pptx",
    16: "16. EKG Pericarditis Electrolytes and Other Abnormalities.pptx",
}
# Footers for the fragments that end without one (13 and 14 carry their own).
FOOTERS = {
    11: "Emphasis quoted from the 5 October 2026 recording (three segments; our transcript read against Notability&rsquo;s). Every strip above was viewed at full size and cites its slide.",
    12: "Emphasis quoted from the 5 October 2026 recording (three segments, about 84 minutes; our transcript read against Notability&rsquo;s). Every strip above was viewed at full size and cites its slide.",
    15: "Emphasis quoted from the 7 October 2026 recording (three segments, about 109 minutes; our transcript read against Notability&rsquo;s). Every tracing above was viewed at full size and cites its slide.",
    16: "Emphasis quoted from the 7 October 2026 recording (two segments, about 83 minutes; our transcript read against Notability&rsquo;s). Every tracing above was viewed at full size and cites its slide.",
}
TY_KEYS = {11: ("sinusrhythms", "Rhythm Analysis &amp; Sinus Rhythms"),
           12: ("ectopy", "Ectopy, Escape &amp; Supraventricular Rhythms"),
           13: ("ventricularblocks", "Ventricular Dysrhythmias &amp; Blocks"),
           14: ("axisbbb", "Axis, Bundle Branch Blocks &amp; Enlargement"),
           15: ("ischemia", "Ischemia, Injury &amp; Infarction"),
           16: ("pericardial", "Pericarditis, Electrolytes &amp; Special Patterns")}

# Exam 2 palette -> Exam 3 palette (same roles; quizzes use navy #33363d,
# indigo #b23a48, gold #c79a3a from tools/pdm_e3/palette.json). Gold is too
# light for heading text, so the guide's third accent is the same hue, darker.
ROLE = [
    ("--ink:#221c1c;", "--ink:#1f2024;"),
    ("--paper:#fbf7f6;", "--paper:#faf8f8;"),
    ("--accent:#a1363a;      /* rose plum */", "--accent:#33363d;      /* monitor charcoal */"),
    ("--accent2:#2b6f86;      /* warm gold */", "--accent2:#b23a48;      /* ECG red */"),
    ("--accent3:#7a4d1f;      /* muted violet */", "--accent3:#8a6420;      /* dark gold */"),
    ("--line:#eadcd9;", "--line:#e3dee0;"),
    ("--soft:#665a58;", "--soft:#5d5a5e;"),
    ("linear-gradient(120deg,#5a1c20,var(--accent) 55%,#c0605a)",
     "linear-gradient(120deg,#1c1e22,var(--accent) 50%,#b23a48)"),
    ("color:#fbe7e5;", "color:#f3e6e8;"),
    ("background:#f4ecea;", "background:#f2f0f1;"),          # toc + figure panels
    ("background:#f5ebe9;", "background:#f5eef0;"),          # objectives box
    ("background:#e8f1f4;", "background:#f6f0e3;"),          # callout (gold border)
    ("background:#f8f0e2;", "background:#f8eced;"),          # pearl (red border)
    ("tr:nth-child(even) td{background:#f6efed;}", "tr:nth-child(even) td{background:#f5f3f4;}"),
    ("code{background:#eee2df;", "code{background:#ebe7e8;"),
    ("stroke: #a1363a;", "stroke: #b23a48;"),                # pull-refresh + footer mark
    (".footer-mark-ink { stroke: #221c1c; }", ".footer-mark-ink { stroke: #1f2024; }"),
    (".footer-mark-accent { stroke: #e6a9a5; }", ".footer-mark-accent { stroke: #e8a3ac; }"),
]
E2_HEXES = ("#a1363a", "#2b6f86", "#7a4d1f", "#5a1c20", "#c0605a", "#fbe7e5", "#f4ecea",
            "#f5ebe9", "#e8f1f4", "#f8f0e2", "#f6efed", "#eee2df", "#e6a9a5", "#221c1c")

HOW = '''<div class="prof-flag"><span class="prof-flag-label">&#9733; How this exam is written</span>
  <p>Exam 3 is the electrocardiography block. The course rules below come from Professor Reynolds&rsquo; first lecture and hold for every exam in this class; the last row is the lecturer&rsquo;s own scope for these six lectures.</p>
  <table>
    <tr><th>The rule</th><th>What it means for you</th></tr>
    <tr><td><em>&ldquo;I&rsquo;m not going to just throw a random number at you and not give you context of whether that&rsquo;s high or low.&rdquo;</em> (Professor Reynolds, Lecture 1)</td><td><strong>Reference ranges are supplied.</strong> A heart rate, an interval or a potassium in a stem comes with the range that reads it. Learn what a value <em>means</em>.</td></tr>
    <tr><td><em>&ldquo;Although a heart rhythm can be a diagnosis, you also need to be able to interpret an EKG (electrocardiogram) by naming the rhythm.&rdquo;</em> (Lecture 1)</td><td><strong>This is the exam where that lands.</strong> Expect a rhythm strip or a 12-lead with the vignette, asking the rhythm, the finding or the next step. Read every strip the same way: rate, regularity, P waves, PR interval, QRS.</td></tr>
    <tr><td>Questions are vignette and next-best-test: <em>&ldquo;what would be the next test that you would order?&rdquo;</em></td><td>In this block the next test is often another lead: posterior leads V7&ndash;V9 for isolated ST depression in V1&ndash;V4, V4R for an inferior infarction with hypotension (15.6).</td></tr>
    <tr><td>Treatment is left out of the rhythm lectures: Lecture 12 is <em>&ldquo;solely about rhythm interpretation and diagnosis&rdquo;</em>.</td><td>Know what a tracing shows and what it means for the patient, not how it is treated.</td></tr>
  </table>
</div>'''

# Five short self-checks per lecture, written from the sections above (each fact
# is stated in its own section). Correct positions are spread on purpose:
# openTestYourself shows choices in the order given.
TY = {
 "sinusrhythms": [
  {"q": "Which pacemaker fires at 40 to 60 per minute when the sinoatrial node fails?",
   "choices": ["The Purkinje network", "The atrioventricular node", "Bachmann's bundle", "The bundle branches"], "correct": 1,
   "explain": "The sinoatrial node fires at 60 to 100, the atrioventricular node (the backup) at 40 to 60, and the Purkinje network at 20 to 40 per minute."},
  {"q": "On standard paper at 25 millimeters per second, how long is one small box?",
   "choices": ["0.04 seconds", "0.2 seconds", "0.4 seconds", "0.02 seconds"], "correct": 0,
   "explain": "One small box (1 millimeter) is 0.04 seconds and one large box (5 millimeters) is 0.2 seconds."},
  {"q": "Which rate method still works when the rhythm is irregular?",
   "choices": ["Dividing 1500 by the small boxes", "Counting down 300, 150, 100", "Dividing 300 by the large boxes", "Counting complexes in six seconds"], "correct": 3,
   "explain": "The six-second method counts every QRS in six seconds and multiplies by 10, so it averages an irregular rhythm; the box methods measure one R to R interval and need a regular rhythm."},
  {"q": "A strip at 72 per minute (normal 60 to 100) has an upright P wave before every narrow QRS and a constant PR interval, but the R to R interval shortens and lengthens with breathing. What is the rhythm?",
   "choices": ["Normal sinus rhythm", "Sinus exit block", "Sinus arrhythmia", "Sick sinus syndrome"], "correct": 2,
   "explain": "Sinus arrhythmia meets every sinus criterion except regularity: on inspiration vagal tone is suppressed and the rate rises. It is benign and most common in children."},
  {"q": "After a gap with no P wave, QRS or T wave, the next P wave falls exactly where the original timing predicted. What is this?",
   "choices": ["Sinus pause", "Sinus exit block", "Sinus arrest", "Sinus bradycardia"], "correct": 1,
   "explain": "In exit block the node keeps firing on time but the impulse is blocked, so the P to P interval marches out; a pause or an arrest resets the cycle and does not march out."},
 ],
 "ectopy": [
  {"q": "Which beat arrives early with a wide QRS, no P wave and a T wave pointing opposite the QRS?",
   "choices": ["A premature ventricular complex", "A premature atrial complex", "A premature junctional complex", "A junctional escape beat"], "correct": 0,
   "explain": "A premature ventricular complex is early and wide (typically over 0.12 seconds), has no P wave, and its T wave is opposite the QRS. Atrial and junctional premature beats are narrow."},
  {"q": "A narrow beat arrives late, after a pause in the sinus rhythm. What is it?",
   "choices": ["A premature atrial complex", "A ventricular escape complex", "A junctional escape beat", "A premature junctional complex"], "correct": 2,
   "explain": "Escape beats are late: they appear after a pause because the pacemaker above failed or slowed. A late narrow beat is junctional; a late wide beat means both nodes failed (ventricular escape)."},
  {"q": "A regular rhythm at 30 per minute (normal 60 to 100) has wide QRS complexes and no P waves. What is the rhythm?",
   "choices": ["Junctional escape rhythm", "Accelerated junctional rhythm", "Ventricular tachycardia", "Idioventricular rhythm"], "correct": 3,
   "explain": "Idioventricular rhythm is the Purkinje network pacing: 20 to 40 per minute, regular, wide, no P waves. Junctional rhythms run at 40 to 60 or faster and are usually narrow."},
  {"q": "Which pattern is pathognomonic of atrial flutter?",
   "choices": ["Irregularly irregular R waves", "Sawtooth flutter waves", "Three or more P wave shapes", "Inverted P waves before the QRS"], "correct": 1,
   "explain": "The sawtooth is the only rhythm with that pattern. Atrial fibrillation is irregularly irregular with no P waves, and three P wave shapes mean wandering atrial pacemaker or multifocal atrial tachycardia."},
  {"q": "A regular, narrow tachycardia at 190 per minute (normal resting 60 to 100) shows an upright P wave before every QRS. What is the rhythm?",
   "choices": ["Sinus tachycardia", "Supraventricular tachycardia", "Atrial flutter", "Junctional tachycardia"], "correct": 0,
   "explain": "Rate is not the rhythm: upright sinus P waves before every QRS make it sinus tachycardia. Supraventricular tachycardia shows no visible P wave, or a retrograde one."},
 ],
 "ventricularblocks": [
  {"q": "A regular, wide-complex tachycardia at 180 per minute (normal 60 to 100) has identical complexes and no visible P waves. What is the rhythm?",
   "choices": ["Torsades de pointes", "Ventricular fibrillation", "Monomorphic ventricular tachycardia", "Idioventricular rhythm"], "correct": 2,
   "explain": "Monomorphic ventricular tachycardia is regular and wide at 100 to 300 with one complex shape. Torsades changes shape and twists; fibrillation has no measurable QRS; idioventricular rhythm is 20 to 40."},
  {"q": "Torsades de pointes is usually a consequence of which finding?",
   "choices": ["A short PR interval", "A prolonged QT interval", "A delta wave", "Complete heart block"], "correct": 1,
   "explain": "Torsades de pointes is polymorphic ventricular tachycardia whose complexes twist around the baseline, and it usually follows a prolonged QT interval."},
  {"q": "The monitor shows an organized sinus rhythm, but the patient has no pulse. What is the diagnosis?",
   "choices": ["Asystole", "Ventricular standstill", "Fine ventricular fibrillation", "Pulseless electrical activity"], "correct": 3,
   "explain": "Pulseless electrical activity is organized electrical activity with no mechanical activity. It can look like any organized rhythm, even normal sinus; the missing pulse makes the diagnosis."},
  {"q": "The PR interval lengthens beat by beat until a P wave is not conducted, then resets. Which block is this?",
   "choices": ["Second-degree type I (Wenckebach)", "Second-degree type II", "First-degree block", "Third-degree block"], "correct": 0,
   "explain": "Type I is a progressive delay in the atrioventricular node until one impulse fails, giving grouped beats. Type II has a constant PR; third-degree has no conducted P waves; first-degree drops nothing."},
  {"q": "Where is the conduction failure in second-degree type II block?",
   "choices": ["Within the atrioventricular node", "In the sinoatrial node", "Below the node, in the His-Purkinje system", "In Bachmann's bundle"], "correct": 2,
   "explain": "Type II block sits below the node (His-Purkinje), is always conduction disease, and is less common and more serious than type I, which is in the node itself."},
 ],
 "axisbbb": [
  {"q": "The QRS is mostly positive in lead I and mostly negative in aVF. What is the axis?",
   "choices": ["Normal axis", "Left axis deviation", "Right axis deviation", "Extreme axis"], "correct": 1,
   "explain": "Lead I up and aVF down is left axis deviation (beyond -30 degrees). Both up is normal, I down with aVF up is right axis deviation, and both down is extreme axis."},
  {"q": "In which group is right axis deviation a normal finding?",
   "choices": ["Children", "Older adults", "Pregnant women", "Trained athletes"], "correct": 0,
   "explain": "Right axis deviation is normal in children. In adults it points to a cause such as chronic obstructive pulmonary disease, pulmonary embolism, dextrocardia or left posterior fascicular block."},
  {"q": "A QRS of 0.14 seconds (normal under 0.12) shows rSR in V1 and slurred S waves in I, aVL, V5 and V6. What is the finding?",
   "choices": ["Left bundle branch block", "Left anterior fascicular block", "Left ventricular hypertrophy", "Right bundle branch block"], "correct": 3,
   "explain": "Right bundle branch block: wide QRS, rSR in V1 (the last deflection positive) and slurred lateral S waves. Left bundle branch block gives rS in V1 with notched lateral complexes."},
  {"q": "Which P wave finding indicates right atrial enlargement?",
   "choices": ["A humped P wave lasting 0.12 seconds or more", "A large negative terminal part in V1", "An upright limb-lead P wave taller than 2.5 millimeters", "A P wave hidden inside the QRS"], "correct": 2,
   "explain": "Right atrial enlargement (P pulmonale) is a tall upright P wave over 2.5 millimeters in the limb leads, with a larger positive first part in V1. The humped P and the negative V1 terminal part are left atrial."},
  {"q": "Which condition is the most common mimic of infarction on a 12-lead?",
   "choices": ["Left ventricular hypertrophy", "Right bundle branch block", "Sinus arrhythmia", "First-degree block"], "correct": 0,
   "explain": "Left ventricular hypertrophy is the most common infarction mimic: concave upward ST elevation in V1 to V3 with lateral T-wave inversion."},
 ],
 "ischemia": [
  {"q": "Which change is often the very first electrocardiographic sign of ischemia?",
   "choices": ["Pathologic Q waves", "ST elevation", "Hyperacute T waves", "T-wave inversion"], "correct": 2,
   "explain": "Broad, tall, symmetrical hyperacute T waves often come first and are easily missed. ST elevation means injury and pathologic Q waves mean infarction."},
  {"q": "ST elevation in II, III and aVF points to which artery in most people?",
   "choices": ["The left anterior descending artery", "The right coronary artery", "The circumflex artery", "The left main artery"], "correct": 1,
   "explain": "II, III and aVF face the inferior wall, which the right coronary artery supplies in most people. The left anterior descending supplies the front and septum; the circumflex the side and back."},
  {"q": "A tracing shows isolated ST depression in V1 to V4 with no ST elevation anywhere. What is the next best step?",
   "choices": ["Obtain V4R", "Repeat the tracing tomorrow", "Treat as pericarditis", "Obtain posterior leads V7 to V9"], "correct": 3,
   "explain": "Isolated ST depression in V1 to V4 is the reciprocal of a posterior infarction until proven otherwise; V4 to V6 move to the back as V7 to V9, and ST elevation there confirms it."},
  {"q": "An inferior infarction comes with hypotension, clear lungs and jugular venous distension. Which lead confirms the suspected complication?",
   "choices": ["V4R", "aVR", "V7", "Lead I"], "correct": 0,
   "explain": "These signs suggest right ventricular involvement. V4R (V4 moved to the right fifth intercostal space, midclavicular line) confirms it when it shows ST elevation."},
  {"q": "What is true of reciprocal changes when ST elevation is present?",
   "choices": ["Their absence rules out infarction", "They confirm ischemia; absence does not exclude it", "They indicate pericarditis instead", "They appear only in aVR"], "correct": 1,
   "explain": "Reciprocal ST depression on the opposite leads confirms ischemia when ST elevation is present, but its absence does not exclude an infarction."},
 ],
 "pericardial": [
  {"q": "Which finding favors acute pericarditis over an infarction?",
   "choices": ["Localized convex ST elevation", "New pathologic Q waves", "PR depression with global concave ST elevation", "ST depression in II, III and aVF"], "correct": 2,
   "explain": "Pericarditis gives PR depression and global concave ST elevation without reciprocal depression (except aVR and V1). Localized convex elevation, reciprocal depression and Q waves point to infarction."},
  {"q": "What is the earliest electrocardiographic sign of hyperkalemia?",
   "choices": ["Peaked, symmetric T waves", "A sine wave pattern", "Prominent U waves", "A short ST segment"], "correct": 0,
   "explain": "Hyperkalemia progresses from peaked symmetric T waves to flat P waves, a wide QRS and finally a sine wave. Prominent U waves belong to hypokalemia; a short ST segment to hypercalcemia."},
  {"q": "Which tracing change is typical of hypocalcemia?",
   "choices": ["Peaked T waves", "A short ST segment", "Prominent U waves", "A long ST segment with a prolonged QTc"], "correct": 3,
   "explain": "Hypocalcemia prolongs phase 2, so the ST segment is long, the T wave normal and the QTc prolonged. Hypercalcemia shortens the ST segment."},
  {"q": "Which triad defines Wolff-Parkinson-White?",
   "choices": ["Long PR, narrow QRS and a U wave", "Short PR, wide QRS and a delta wave", "Sawtooth waves with a narrow QRS", "PR depression and concave ST elevation"], "correct": 1,
   "explain": "An accessory pathway (the bundle of Kent) bypasses the atrioventricular node, so the PR is short, the QRS wide and its upstroke slurred into a delta wave."},
  {"q": "Which finding is the most common electrocardiographic effect of digoxin toxicity?",
   "choices": ["Frequent premature ventricular complexes", "Sinus tachycardia", "Peaked T waves", "A delta wave"], "correct": 0,
   "explain": "Digoxin inhibits the sodium-potassium pump; frequent premature ventricular complexes, often as bigeminy, are the most common finding."},
 ],
}


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


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
    # The deck title gets its own id so the lecture's opening (frame, emphasis box)
    # is its own linkable section for build_guide_links.py; without one, that text
    # is parsed as part of the PREVIOUS lecture's last subsection.
    sid = re.search(r'<section class="deck" id="([^"]+)">', frag).group(1)
    frag = frag.replace('<h2 class="deck-title">', '<h2 class="deck-title" id="%s-top">' % sid, 1)
    key, title = TY_KEYS[n]
    btn = ('  <button type="button" class="test-yourself-btn" style="--acc:#b23a48" '
           "onclick=\"window.openTestYourself('Test yourself &mdash; %s', TEST_YOURSELF.%s)\">"
           "Test yourself! &rarr;</button>\n" % (title, key))
    if '<footer class="guide-foot">' in frag:
        assert n not in FOOTERS, n
        i = frag.rindex('<footer class="guide-foot">')
        frag = frag[:i] + btn.lstrip() + "  " + frag[i:]
    else:
        foot = ('  <footer class="guide-foot">Source: <em>%s</em> (%s). %s</footer>\n'
                % (DECKS[n], LECTURER, FOOTERS[n]))
        frag = frag[:-len("</section>")].rstrip() + "\n\n" + btn + foot + "</section>"
    return frag


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
    head = head.replace("Principles of Diagnostic Medicine I &middot; Exam 2 &mdash; Study Guide",
                        "Principles of Diagnostic Medicine I &middot; Exam 3 &mdash; Study Guide")
    head = re.sub(r'\s*<link rel="alternate"[^>]*>\n', "\n", head)   # build_guide_docx.py adds ours
    head = re.sub(r"<header class=\"top\">.*?</header>", '''<header class="top">
  <h1>Principles of Diagnostic Medicine I &middot; Exam 3 &mdash; Study Guide</h1>
  <p>PAJ 5600 Principles of Diagnostic Medicine I &middot; Class of 2028 &middot; Exam Wednesday 14 October 2026</p>
  <p>Covers Lectures 11&ndash;16, the electrocardiography block (lecture content) &middot; Instructional Objectives (IOs) taken verbatim from the syllabus</p>
</header>''', head, flags=re.S)
    for a, b in ROLE:
        assert a in head, "donor changed, role not found: " + a
        head = head.replace(a, b)
    css = head[:head.index("</head>")]
    # the stale dark-token block is regenerated below; ignore it here
    css_wo_tokens = re.sub(r"<!--DARK-TOKENS:BEGIN.*?DARK-TOKENS:END-->", "", css, flags=re.S).lower()
    left = [h for h in E2_HEXES if h in css_wo_tokens]
    assert not left, "Exam 2 colours left in the head: %r" % left

    toc = ['<nav class="toc">', "  <h2>Contents</h2>"]
    sections = []
    for n in range(11, 17):
        frag = section(n)
        _sid, entries = toc_for(n, frag)
        toc += entries
        sections.append(frag)
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
    for k in TY:
        assert "TEST_YOURSELF.%s)" % k in html, k
    brit = re.findall(r"(?i)\b\w*(?:haem|oedem|tumour|colour|centre|anaem|oesoph|isation|oris[ei]|ognis[ei]|emphasis[ei]|analys[ei]|optimis|visualis|characteris|memoris|summaris)\w*\b", body)
    brit = [w for w in brit if w.lower() not in ("haemophilus", "analysis", "analyses")]
    assert not brit, "British spelling: %r" % sorted(set(brit))
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d figures, %d sections, %d subsections, %d TOC links)" % (
        os.path.relpath(OUT, ROOT), len(html) // 1024, html.count('<figure class="fig">'),
        html.count('<section class="deck"'), html.count('<h3 class="sub"'), len(toc) - 3))


if __name__ == "__main__":
    main()
