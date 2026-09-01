#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add PDM I section 6 (Urinalysis) to the Exam 1 study guide.

Instructional Objectives are quoted VERBATIM from the PAJ 5600 syllabus,
including its a-c lettering and roman sub-items, per [[guide_verbatim_io_rule]].

FOLDS IN THE 1 SEPTEMBER RECORDING (Prof. Gopal, 49:43). It matters more here
than in any earlier PDM lecture, because THIS DECK HAS NO SPEAKER NOTES -- all
35 notes slides are empty placeholders, where Lectures 1-5 carried substantial
notes. Three things exist only in the audio:

  1. Her testing rule, at 15:08. Know which pads read NEGATIVE; ranges are
     supplied rather than memorised.
  2. Bence Jones proteins are found with urine protein ELECTROPHORESIS, not a
     dipstick, at 40:09.
  3. The worked case, at 48:38. Slide 36 is an unfinished answer slide -- a
     dipstick chart with three unlabelled "x" shapes. Which analytes they mark
     was resolved from their coordinates against the picture's own extent, and
     agrees with what she read out.

The recording stops mid-sentence at 49:41, part-way through her explanation of
the case. Nothing here depends on what came after the cut, and the guide says
so rather than papering over it.

Idempotent: fenced in <!--PDML6--> and stripped before reinsert.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1")
GUIDE = os.path.join(DIR, "pdm-exam-1-study-guide.html")
IMGDIR = os.path.join(DIR, "pdm-exam-1-l6-images")
ACC6 = "#2f5d50"


def fig(slug, ext, caption, slide):
    path = os.path.join(IMGDIR, slug + ext)
    assert os.path.exists(path), "missing figure %s -- run extract_pdm_l6_figures.py" % slug
    return ('<figure class="fig"><img src="pdm-exam-1-l6-images/%s%s" decoding="async" '
            'alt="Lecture 6 slide %d figure."><figcaption>%s '
            '<span class="cite">Lecture 6 &middot; Slide %d</span></figcaption></figure>'
            % (slug, ext, slide, caption, slide))


FIGS = {
 "@@COLOUR@@": [("urine-colour", ".jpeg",
   "Urine colour against what it suggests. Note the food causes of red urine &mdash; "
   "<b>beets</b>, blueberries and rhubarb &mdash; and that fizzing points to protein.", 7)],
 "@@STRIP@@": [("reagent-strip-chart", ".png",
   "The reagent strip chart. The <b>reading time differs by analyte</b> &mdash; thirty seconds "
   "for glucose, two minutes for leukocytes &mdash; which is why the timing has to be watched.", 12)],
 "@@NEPHRON@@": [("nephron", ".jpg",
   "The nephron. The glomerulus filters; the tubules reabsorb. Almost every abnormal "
   "urinalysis parameter is a failure of one or the other.", 15)],
}

SEC6 = """
<section class="deck" id="urinalysis">
  <h2 class="deck-title">6 &middot; Urinalysis</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Topic Outline 6: Urinalysis</p>
    <ol type="a">
      <li>Describe the following urinalysis parameters: i. Specific gravity &middot; ii. pH &middot; iii. Protein &middot; iv. Glucose &middot; v. Ketones &middot; vi. Leukocyte esterase &middot; vii. Nitrites &middot; viii. Blood &middot; ix. Bilirubin</li>
      <li>Differentiate between: i. Hematuria &middot; ii. Hemoglobinuria &middot; iii. Myoglobinuria</li>
      <li>Correlate urinalysis findings with common clinical presentations.</li>
    </ol>
  </div>

  <div class="callout prof">
    <p><strong>What she said about numbers, on 1 September.</strong>
    <em>&ldquo;For testing purposes, I would like you to know what a normal urinalysis involves
    &hellip; It&rsquo;s important to know that we should not find nitrites. We should not find
    ketones. We should not find glucose. So I do want you to know that.
    <strong>I&rsquo;m not asking that you memorize ranges</strong>, okay? But I do want you to know
    if there should just be none present at all. But for testing purposes, if there&rsquo;s a range
    involved, <strong>it&rsquo;ll be provided for you</strong>.&rdquo;</em></p>
    <p>So the split is clean. <strong>Which pads read negative in a healthy person is fair to know
    cold.</strong> A reference range is not &mdash; it will be given to you. Learn the direction of
    abnormality and what it means.</p>
    <p><strong>One naming point she asked for twice:</strong> <em>&ldquo;Please make sure you call
    it <strong>nitrites</strong> and not nitrates. It&rsquo;s like a pet peeve of mine.&rdquo;</em>
    Nitr<b>a</b>tes are what is in the urine to begin with; bacteria reduce them to
    nitr<b>i</b>tes, and the nitrite is what the pad reports.</p>
  </div>

  <h3 class="sub" id="l6-what">6.1 &middot; What the test is, and when to order it</h3>
  <p>Urinalysis examines the <strong>physical, chemical and microscopic</strong> contents of urine.
  It is inexpensive, non-invasive and fast, which is why it is done routinely on admission and in
  primary care, obstetrics and paediatrics alike. In a renal evaluation it <strong>complements the
  serum creatinine and blood urea nitrogen</strong> rather than replacing them.</p>
  <p>It reaches well beyond the urinary tract: it speaks to hepatic and biliary disease, hydration
  status and infection. <strong>Any patient with abdominal, pelvic or back pain needs one.</strong></p>

  @@NEPHRON@@

  <h3 class="sub" id="l6-inspection">6.2 &middot; Inspection &mdash; colour, transparency, odour</h3>
  <p>The examination starts the way a physical examination does, by looking.</p>
  <table class="tbl">
    <tr><th>Colour</th><th>Suggests</th></tr>
    <tr><td>Pale yellow to colourless</td><td>Dilute urine &mdash; possibly overhydrated</td></tr>
    <tr><td>Dark yellow or amber</td><td>Concentrated urine &mdash; possibly dehydrated</td></tr>
    <tr><td>Yellow-brown or green</td><td><b>Bilirubin</b> &mdash; hepatitis, cirrhosis, biliary obstruction</td></tr>
    <tr><td>Bright or dark red</td><td><b>Blood</b> &mdash; infection, stone, tumour, or menstrual contamination</td></tr>
    <tr><td>Blue, orange or green</td><td><b>Medications</b> &mdash; phenazopyridine, rifampicin, urinary anaesthetics</td></tr>
  </table>
  <p>The medication colours are a <strong>patient education point</strong>: tell the patient before
  they start, so a startling colour does not alarm them.</p>

  @@COLOUR@@

  <p><strong>Transparency</strong> runs clear &rarr; hazy &rarr; cloudy &rarr; turbid. Cloudiness
  comes from red cells, white cells, epithelial cells, bacteria, yeast, crystals, mucus, contrast
  media or fat. <strong>Foam is the one to notice separately &mdash; it points to protein.</strong></p>
  <p><strong>Odour.</strong> Normal is called <em>aromatic</em>. An <b>ammonia</b> smell means the
  sample has stood long enough for bacteria to decompose its urea &mdash; refrigerate a specimen
  that will not be read within one to two hours, and <strong>add no preservative</strong>. A
  <b>foul</b> odour suggests bacterial infection; a <b>faecal</b> odour suggests an enterovesical
  fistula; a <b>fruity or sweet</b> odour means ketones, and sends you to the blood sugar.</p>

  <h3 class="sub" id="l6-strip">6.3 &middot; The reagent strip</h3>
  <p>A fresh specimen in a sterile container. Strips are kept desiccated. Results come in two
  shapes: <strong>qualitative</strong> (positive or negative) and <strong>semi-quantitative</strong>
  (trace, 1+, 2+, 3+ &mdash; a graded estimate, not a measurement).</p>
  <p>Two practical traps. <strong>Reading time differs by analyte</strong>, so the strip cannot be
  read all at once. And <strong>manufacturers order the pads differently</strong>, so a strip must
  be read against its own chart &mdash; reading a pad against the wrong row is how the result goes
  wrong. An automated reader improves accuracy where one is available.</p>

  @@STRIP@@

  <div class="callout">
    <p><strong>The six that should read negative.</strong> Leukocyte esterase, nitrites, ketones,
    glucose, blood and bilirubin. Protein is negative or trace. <strong>Specific gravity and pH are
    the two that always carry a value</strong> &mdash; neither is ever simply &ldquo;negative&rdquo;.
    That distinction is worth holding, because it is exactly what she said to know cold.</p>
  </div>

  <h3 class="sub" id="l6-ph">6.4 &middot; pH, and what it does for stones</h3>
  <p>Urine pH reports the <strong>renal tubules' ability to hold the hydrogen ion concentration
  steady</strong>. The kidneys do that by excreting hydrogen ions as ammonium and by reabsorbing and
  producing bicarbonate. Four things move it: <strong>diet, medications, systemic acid-base
  disorders and tubular function</strong>.</p>
  <table class="tbl">
    <tr><th></th><th>Acidic urine</th><th>Alkaline urine</th></tr>
    <tr><td><b>Causes</b></td>
        <td>Ketoacidosis, <i>Escherichia coli</i> infection, metabolic and respiratory acidosis, a diet high in meat or cranberries</td>
        <td>Urea-splitting organisms (<i>Proteus</i>, <i>Staphylococcus</i>, <i>Klebsiella</i>, <i>Pseudomonas</i>), bacterial contamination, acute and chronic renal failure, renal tubular acidosis, metabolic and respiratory alkalosis, a diet high in fruit and vegetables</td></tr>
    <tr><td><b>Stones</b></td>
        <td>Calcium oxalate and uric acid</td>
        <td>Triple phosphate and struvite</td></tr>
    <tr><td><b>Treatment aim</b></td>
        <td>Alkalinise the urine &mdash; chiefly for uric acid stones</td>
        <td>Treat the infection, since urease-producing bacteria are driving them</td></tr>
  </table>
  <p class="muted">Note the trap in the left column: <b>renal tubular acidosis produces ALKALINE
  urine</b> despite its name, because the defect is a failure to excrete acid.</p>

  <h3 class="sub" id="l6-infection">6.5 &middot; The two infection pads</h3>
  <p><strong>Leukocyte esterase</strong> detects the esterase that white cells release.
  <em>&ldquo;Leukocyte esterase indicates pyuria. That&rsquo;s the take-home point.&rdquo;</em>
  It rises with urinary tract infection, and also with interstitial cystitis and
  glomerulonephritis, both inflammatory rather than infective.</p>
  <p><strong>Nitrites.</strong> Urease-producing bacteria carry a reductase that turns urinary
  nitrates into nitrites. Two conditions have to be met for the pad to work: a urease-producing
  organism, and <strong>more than four hours of urine sitting in the bladder</strong> for the
  conversion. Sensitivity is about 50%, lower than leukocyte esterase.</p>
  <div class="callout prof">
    <p><strong>The single most emphasised idea in the lecture.</strong>
    <em>&ldquo;Remember which one did I say was most common? <strong>E. coli. E. coli is not
    urease-positive.</strong> If nitrites is positive, it&rsquo;s very helpful &hellip; but if
    nitrites is negative, it does not rule out a urinary tract infection, because the majority of
    simple urinary tract infections are caused by E. coli, which will not cause this to turn
    positive.&rdquo;</em></p>
    <p>So: <strong>a positive nitrite is useful; a negative one is not.</strong> Either way, if the
    patient is symptomatic, <strong>send a culture and sensitivity</strong>. The same holds for a
    negative leukocyte esterase. In young children the pad is less reliable still, because they void
    too often for the conversion to happen.</p>
  </div>

  <h3 class="sub" id="l6-ketones">6.6 &middot; Ketones and glucose</h3>
  <p><strong>Ketones</strong> are made in the liver from fatty acids and normally metabolised
  completely, so almost none reaches the urine. Ketonuria means <strong>cells are burning fatty
  acids rather than glucose</strong> &mdash; uncontrolled diabetes and ketoacidosis, starvation,
  fasting, alcoholic ketoacidosis, a high-fat low-carbohydrate diet, liver disease, and febrile
  illness in infants and children. <strong>Ketones on a strip should send you to the glucose.</strong></p>
  <p><strong>Glucose</strong> is filtered freely and then wholly reabsorbed in the proximal tubules,
  so none should appear. It spills once the blood level exceeds the <strong>tubular threshold</strong>
  &mdash; around 180 milligrams per decilitre. Glucosuria is <em>not</em> diagnostic, because the
  threshold differs between people, but it always means further workup.</p>
  <p>Three ways glucose appears without uncontrolled diabetes: <strong>impaired tubular
  reabsorption</strong>, so it spills at a normal blood level; <strong>dextrose-containing
  intravenous fluids</strong>; and <strong>pregnancy</strong>, where a trace is normal because the
  threshold falls.</p>

  <h3 class="sub" id="l6-blood">6.7 &middot; Objective b &mdash; blood, and the three things it can mean</h3>
  <p>This is the objective that carries its own bullet in the syllabus, and it turns on one fact:
  <strong>the pad detects heme, and heme sits in red cells, in free hemoglobin and in myoglobin
  alike.</strong> A positive result does not say which. What separates them is what else is true.</p>
  <table class="tbl">
    <tr><th></th><th>Hematuria</th><th>Hemoglobinuria</th><th>Myoglobinuria</th></tr>
    <tr><td><b>What is in the urine</b></td><td>Intact red cells</td><td>Free hemoglobin, no intact cells</td><td>Myoglobin, no intact cells</td></tr>
    <tr><td><b>Where it comes from</b></td><td>Bleeding anywhere along the urinary tract</td><td>Intravascular destruction of red cells</td><td>Skeletal muscle injury</td></tr>
    <tr><td><b>Causes</b></td><td>Infection, inflammation, trauma, tumour, calculus, over-aggressive anticoagulation</td><td>Hemolysis, hemolytic anemia (sickle cell), transfusion reaction, severe burns</td><td>Trauma, electric shock, rhabdomyolysis from compression injury, hyperthermia or statins</td></tr>
    <tr><td><b>The confirming serum test</b></td><td>&mdash; (red cells seen on microscopy)</td><td><b>Raised unconjugated bilirubin</b></td><td><b>Raised creatine phosphokinase</b></td></tr>
  </table>
  <p><strong>Gross</strong> hematuria is visible to the naked eye; <strong>microscopic</strong>
  hematuria needs analysis to find, and is defined as <strong>three or more red cells</strong>. A
  trace of blood can follow strenuous exercise in an otherwise well patient.</p>

  <h3 class="sub" id="l6-bilirubin">6.8 &middot; Bilirubin and protein</h3>
  <p><strong>Bilirubin.</strong> Only the <strong>conjugated</strong> form appears, because only it
  is water soluble. So bilirubinuria points to disease <em>after</em> conjugation &mdash; hepatic
  disease, or biliary obstruction such as a gallstone. Its screening value is timing: it can appear
  <strong>days before the patient looks jaundiced</strong>.</p>
  <p><strong>Protein</strong> &mdash; albumin, mostly &mdash; reports on glomerular and tubular
  function, and is reported semi-quantitatively. A trace can be normal in
  <strong>pregnancy, fever and strenuous exercise</strong>. Contamination with prostatic or vaginal
  secretions gives a false positive. Persistent proteinuria is a significant sign of renal disease,
  and a positive strip is followed by a <strong>twenty-four hour collection</strong>, which measures
  it properly rather than estimating.</p>
  <table class="tbl">
    <tr><th>Mechanism</th><th>Causes</th></tr>
    <tr><td><b>Diminished tubular reabsorption</b></td><td>Renal tubular disease, pyelonephritis, interstitial nephritis</td></tr>
    <tr><td><b>Transient, mild</b></td><td>After exercise, acute illness, bleeding or infection in the urinary tract</td></tr>
    <tr><td><b>Glomerular damage</b></td><td>Nephrotic syndrome (massive proteinuria), glomerulonephritis, diabetes mellitus, polycystic kidney disease, systemic lupus erythematosus, preeclampsia</td></tr>
    <tr><td><b>Increased serum protein</b></td><td>Multiple myeloma &mdash; overflow of Bence Jones proteins</td></tr>
  </table>
  <div class="callout">
    <p><strong>The dipstick cannot find myeloma.</strong>
    <em>&ldquo;[Reagent strips] do not react to the Bence Jones proteins that are associated with
    multiple myeloma &hellip; <strong>we actually use urine protein electrophoresis to diagnose it,
    not a dipstick</strong>.&rdquo;</em> A negative protein pad does not exclude light chains. This
    one is on the slide as a footnote and stated plainly in the recording.</p>
  </div>
  <p class="muted">Protein in the urine is <b>not pathognomonic for anything</b> &mdash; her words.
  It narrows the field; it does not name the disease.</p>

  <h3 class="sub" id="l6-sg">6.9 &middot; Specific gravity</h3>
  <p>The <strong>weight of the solutes in urine against an equal volume of water</strong>, which
  estimates the kidneys' concentrating and excretory ability. Water is 1.000, and urine can never
  quite reach it, because there is always some solute &mdash; hence a floor around 1.002.</p>
  <p>It is affected by <strong>particle size</strong>, not just particle number. Her image: marbles
  dropped into a beaker weigh far more than the same volume of glitter. That is why
  <strong>radiographic contrast, whose particles are large, drives it above 1.040</strong>.</p>
  <table class="tbl">
    <tr><th>Low &mdash; dilute urine</th><th>High &mdash; concentrated urine</th></tr>
    <tr><td>Overhydration; diuresis; chronic kidney disease with lost concentrating ability;
        <b>diabetes insipidus</b> (less antidiuretic hormone, more water out)</td>
        <td>Dehydration; reduced renal blood flow (heart failure, hypotension, renal artery
        stenosis); <b>syndrome of inappropriate antidiuretic hormone</b> (more hormone, less water out);
        contrast above 1.040</td></tr>
  </table>
  <p class="muted"><i>Insipidus</i> means tasteless &mdash; the historical way of separating the two
  diabetes was to taste the urine. Sweet was mellitus; tasteless, and dilute, was insipidus.</p>

  <h3 class="sub" id="l6-micro">6.10 &middot; What comes after the strip</h3>
  <p>A <strong>microscopic urinalysis</strong> adds white cells, red cells, squamous epithelial
  cells, casts and crystals, and the specimen can go on for <strong>culture and sensitivity</strong>
  to name the organism and the agent that will treat it.</p>
  <p><strong>Bacteria are significant</strong> when the specimen came by straight catheterisation,
  or when they sit alongside raised white cells and a positive leukocyte esterase. They are
  <strong>probably not significant</strong> when there are more than twenty squamous epithelial
  cells per high power field (contamination), or when they come from a longstanding indwelling
  catheter, which is colonised rather than acutely infected. Gram stain and culture are what make
  the diagnosis definitive.</p>

  <h3 class="sub" id="l6-case">6.11 &middot; The worked case</h3>
  <p>A 28-year-old woman, two days of dysuria, frequency and urgency, mild suprapubic discomfort.
  No fever, no flank pain, no vaginal discharge. Temperature 37.0&deg;C, blood pressure 112/68,
  heart rate 88, respiratory rate 16, oxygen saturation 99% on room air. Mild suprapubic tenderness,
  no costovertebral angle tenderness.</p>
  <p><strong>Next step: urinalysis.</strong> The dipstick came back positive for
  <strong>leukocyte esterase, nitrites and blood</strong>, and negative for glucose, bilirubin,
  ketones and protein.</p>
  <p>Read it in two halves. The <strong>positives</strong> give pyuria, urease-producing bacteria
  and blood &mdash; the picture of a urinary tract infection. The <strong>negatives</strong> matter
  just as much: no glucose or ketones argues against a metabolic cause, no bilirubin against a
  hepatic one, and no protein against glomerular disease. Then send the
  <strong>culture and sensitivity</strong>.</p>
  <p class="muted">Slide 36 is an unfinished answer slide &mdash; a dipstick chart carrying three
  unlabelled marks. Which analytes they sit against was resolved from their position on the chart,
  and matches what she read out. The recording stops mid-sentence at 49:41, part-way through her
  explanation, so the last few seconds of the class are not on tape.</p>
</section>
"""

TOC = """  <a class="top-link" href="#urinalysis">6 &middot; Urinalysis</a>
  <a class="sub-link" href="#l6-what">6.1 What the test is</a>
  <a class="sub-link" href="#l6-inspection">6.2 Colour, transparency, odour</a>
  <a class="sub-link" href="#l6-strip">6.3 The reagent strip</a>
  <a class="sub-link" href="#l6-ph">6.4 pH &amp; stones</a>
  <a class="sub-link" href="#l6-infection">6.5 The two infection pads</a>
  <a class="sub-link" href="#l6-ketones">6.6 Ketones &amp; glucose</a>
  <a class="sub-link" href="#l6-blood">6.7 Blood &mdash; the three meanings</a>
  <a class="sub-link" href="#l6-bilirubin">6.8 Bilirubin &amp; protein</a>
  <a class="sub-link" href="#l6-sg">6.9 Specific gravity</a>
  <a class="sub-link" href="#l6-micro">6.10 After the strip</a>
  <a class="sub-link" href="#l6-case">6.11 The worked case</a>
"""

TY = """    "urinalysis": [
      {q:"Which analytes should read NEGATIVE on a healthy urinalysis?",
       o:["Leukocyte esterase, nitrites, ketones, glucose, blood, bilirubin",
          "Leukocyte esterase, nitrites, and specific gravity",
          "Ketones, glucose, and pH","Blood, bilirubin, and specific gravity"],a:0,
       why:"Specific gravity and pH always carry a value, so neither is ever simply negative."},
      {q:"A symptomatic patient has a NEGATIVE nitrite. What does that tell you?",
       o:["Very little &mdash; E. coli causes most infections and is rarely urease-positive",
          "Infection is excluded","The organism is fungal","The specimen was contaminated"],a:0,
       why:"A positive nitrite is helpful; a negative one does not rule infection out. Culture either way."},
      {q:"The blood pad is positive, no red cells are seen, and the creatine phosphokinase is raised. Which is it?",
       o:["Myoglobinuria","Hemoglobinuria","Hematuria","Specimen contamination"],a:0,
       why:"Creatine phosphokinase points to muscle. A raised unconjugated bilirubin would point to hemolysis instead."},
      {q:"Which mechanism links multiple myeloma to protein in the urine?",
       o:["Overflow from raised plasma protein","Glomerular damage","Diminished tubular reabsorption","Transient loss after exercise"],a:0,
       why:"And the dipstick misses it &mdash; Bence Jones proteins need urine protein electrophoresis."},
      {q:"Which produces a LOW specific gravity?",
       o:["Diabetes insipidus","Dehydration","Syndrome of inappropriate antidiuretic hormone","Radiographic contrast"],a:0,
       why:"Less antidiuretic hormone leaves more water in the urine. The other three concentrate it."},
      {q:"Urine is alkaline and the patient has recurrent stones and infections. Which stone type?",
       o:["Struvite","Uric acid","Calcium oxalate","Cystine"],a:0,
       why:"Urease-producing organisms alkalinise the urine, and treatment targets the infection."},
      {q:"Bilirubin appears in the urine. Which form, and what does it mean?",
       o:["Conjugated &mdash; disease after conjugation, or biliary obstruction",
          "Unconjugated &mdash; hemolysis","Either form &mdash; any liver disease",
          "Conjugated &mdash; renal tubular damage"],a:0,
       why:"Only the conjugated form is water soluble, so only it reaches the urine."},
      {q:"How long must urine sit in the bladder for nitrites to be detectable?",
       o:["More than four hours","About thirty minutes","About one hour","A full day"],a:0,
       why:"The conversion needs time, which is why the pad is less reliable in young children."}
    ],
"""


def main():
    src = open(GUIDE, encoding="utf-8").read()
    src = re.sub(r"<!--PDML6-->.*?<!--/PDML6-->\s*", "", src, flags=re.S)
    src = re.sub(r"<!--PDMTOC6-->.*?<!--/PDMTOC6-->\s*", "", src, flags=re.S)
    src = re.sub(r"<!--PDMTY6-->.*?<!--/PDMTY6-->\s*", "", src, flags=re.S)

    body = SEC6
    for token, items in FIGS.items():
        assert token in body, "figure token %s unused" % token
        body = body.replace(token, "\n".join(fig(s, e, cap, sl) for s, e, cap, sl in items))
    assert "@@" not in body, "unfilled figure token"

    end = src.index("</main>")
    src = src[:end] + "<!--PDML6-->" + body + "<!--/PDML6-->\n\n" + src[end:]

    navend = src.rindex("</nav>")
    src = src[:navend] + "<!--PDMTOC6-->\n" + TOC + "<!--/PDMTOC6-->\n" + src[navend:]

    tyanchor = "  var TEST_YOURSELF = {\n"
    assert src.count(tyanchor) == 1, "TEST_YOURSELF object not found once"
    src = src.replace(tyanchor, tyanchor + "<!--PDMTY6-->\n" + TY + "<!--/PDMTY6-->\n", 1)

    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li",
                "figure", "figcaption"):
        o = len(re.findall(r"<%s[ >]" % tag, src)); c = src.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added section 6: %d subsections, %d figures, %d test-yourself questions"
          % (len(re.findall(r'<h3 class="sub" id="l6-', src)),
             len(re.findall(r'src="pdm-exam-1-l6-images/', src)),
             TY.count("{q:")))


if __name__ == "__main__":
    main()
