#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Cardiac OSCE "Special Maneuvers" guide: how to remember each maneuver and where its result points.

    python3 tools/build_pd2_cardiac_osce_maneuvers.py

Jaxon, 2026-10-20 (the Cardiac OSCE is Wed 2026-10-21): "make a guide under the cardiac OSCE for how to remember the
special maneuvers I need to know and what their results should lead me to, like the disease/disorder".

Sources, every line tagged on the page:
  * PD2 deck "PD II Advanced Cardiovascular & Peripheral Vascular System - Fall 2026.pptx" (Reynolds), slides 15-114
    (tag "PD2 sN"), and the class maneuvers handout already transcribed on pd2-exam-2-special-maneuvers.html ("Handout").
  * Clinical Medicine and Surgery cardiology decks (tag "CMS Lnn sN"): L20 Hypertension (Jaquith), L21 Hypotension,
    L23 Valvular, L25 Heart Failure, L27 Arterial Occlusive Disease, L28 Cardiomyopathy (Carter), L26 Venous (Shah),
    L31 Pericardial Disease. Slide numbers checked against the decks on 2026-10-20.
  * Slides win on conflict; where the decks disagree (ankle-brachial index cut-offs, the handgrip lists) the page says so.
  * Three things are not on any slide and are labeled: the pulsus paradoxus cut-off (L31 s59's speaker notes) and
    the cuff technique / Quincke's meaning ("Textbook").
The memory system (one tank, two doors) follows memory_aid_systems: one connected picture, labeled, with where it breaks.

Shell: the ENT OSCE study guide's head and tail (petrol OSCE palette, light-only, dark tokens via tools/dark_tokens.py,
where this page is in BESPOKE). Writes "Physical Diagnosis 2 Exam 1/pd2-cardiac-osce-maneuvers.html"; then run
tools/dark_tokens.py and `tools/build_guide_docx.py pd2-cardiac-osce-maneuvers`.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FOLDER = os.path.join(ROOT, "Physical Diagnosis 2 Exam 1")
DONOR = os.path.join(FOLDER, "pd2-ent-osce-study-guide.html")
OUT = os.path.join(FOLDER, "pd2-cardiac-osce-maneuvers.html")
DOCX = "pd2-cardiac-osce-maneuvers.docx"
CHART = "pd2-cardiac-osce-chart.html"


def T(*tags):
    """Slide tags: 'PD2 61' -> PD2 s61, 'L23 48' -> CMS L23 s48, 'Handout', anything else verbatim."""
    out = []
    for t in tags:
        m = re.match(r"^(PD2|L\d\d) (\S+)$", t)
        if m:
            deck, s = m.groups()
            label = ("PD2 s" if deck == "PD2" else "CMS %s s" % deck) + s.replace("-", "&ndash;")
            out.append('<span class="slide-tag">%s</span>' % label)
        elif t in ("Textbook", "Slide notes"):
            out.append('<span class="gl-tag">%s</span>' % t)
        else:
            out.append('<span class="slide-tag">%s</span>' % t)
    return " " + " ".join(out)


def C(slug, label):
    """Link to the condition's row on the Cardiac OSCE Disease Chart."""
    return '<a class="cx" href="%s#c-%s">%s</a>' % (CHART, slug, label)


UP = '<span class="up">&#9650; louder</span>'
DOWN = '<span class="down">&#9660; softer</span>'

HCM = C("hypertrophic-cardiomyopathy", "Hypertrophic cardiomyopathy")
AS = C("aortic-stenosis", "Aortic stenosis")
MR = C("mitral-regurgitation", "Mitral regurgitation")
MVP = C("mitral-valve-prolapse", "Mitral valve prolapse")
HF = C("chronic-heart-failure", "Heart failure")
PERI = C("acute-pericarditis", "Acute pericarditis")
TAMP = C("cardiac-tamponade", "Cardiac tamponade")
DISS = C("aortic-dissection", "Aortic dissection")
HTN = C("primary-hypertension", "Hypertension")
OH = C("orthostatic-hypotension", "Orthostatic hypotension")
VV = C("vasovagal-syncope", "Vasovagal syncope")
PAD = C("peripheral-artery-disease", "Peripheral artery disease")
DVT = C("deep-vein-thrombosis", "Deep vein thrombosis")
CVI = C("chronic-venous-insufficiency-and-varicose-veins", "Chronic venous insufficiency")


def card(cid, title, do, say, results, note=""):
    """One maneuver: what to do, what to say, and a result -> where it points table."""
    h = '<div class="mv" id="%s">\n  <h4 class="mv-h">%s</h4>\n' % (cid, title)
    h += '  <p class="do"><b>Do:</b> %s</p>\n' % do
    if say:
        h += '  <p class="say"><b>Say:</b> &ldquo;%s&rdquo;</p>\n' % say
    h += '  <div class="tw"><table class="res">\n    <tr><th>If you find</th><th>It points to</th></tr>\n'
    for find, to in results:
        h += "    <tr><td>%s</td><td>%s</td></tr>\n" % (find, to)
    h += "  </table></div>\n"
    if note:
        h += '  <p class="mv-note">%s</p>\n' % note
    return h + "</div>\n"


# ------------------------------------------------------------------------------------------------ sections
INTRO = '''<section class="deck" id="start">
  <h2 class="deck-title">How to use this page</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="io-tag">Advanced Cardiac and Peripheral Vascular System Medical History and Examination</p>
    <ol type="a" start="9">
      <li>Demonstrate the proper clinical skills for maneuvers to evaluate murmurs.</li>
      <li>Compare and contrast the physical examination findings related to abnormal peripheral arterial and venous function.</li>
      <li>Define the physical examination findings of peripheral edema.</li>
    </ol>
  </div>
  <p>Every maneuver below is written the same way: <b>what you do</b>, <b>what you say out loud</b>, and a small table of
  <b>what you might find &rarr; the disease or disorder it points to</b>. Disease names in blue open that condition&rsquo;s row on the
  Cardiac OSCE Disease Chart. Learn the memory system first; the rest of the page hangs off it.</p>
  <p>Gray tags like <span class="slide-tag">PD2 s62</span> are the Physical Diagnosis 2 cardiovascular deck and slide;
  <span class="slide-tag">CMS L23 s48</span> is a Clinical Medicine and Surgery lecture and slide; <span class="slide-tag">Handout</span> is the class
  maneuvers handout. Gold tags mark the three things that are not on a slide.</p>
  <div class="related">
    <a href="pd2-cardiac-osce.html">Cardiac OSCE Run-Sheet</a>
    <a class="alt" href="pd2-cardiac-osce-chart.html">Cardiac OSCE Disease Chart</a>
    <a class="alt" href="../Physical%20Diagnosis%202%20Exam%202/pd2-exam-2-special-maneuvers.html">The maneuvers handout</a>
  </div>
  <div class="contents">
    <a class="cont-card" href="#memory"><span class="cc-h">1 &middot; The memory system</span><span class="cc-b">One tank, two doors, a breath and a microphone &mdash; and arteries versus veins for the legs</span></a>
    <a class="cont-card" href="#one-screen"><span class="cc-h">2 &middot; Everything on one screen</span><span class="cc-b">Every maneuver, what it does, what gets louder or softer, and where it points</span></a>
    <a class="cont-card" href="#positions"><span class="cc-h">3&ndash;6 &middot; The heart maneuvers</span><span class="cc-b">Positions, Valsalva / standing / squatting / leg raise, handgrip, breathing</span></a>
    <a class="cont-card" href="#vitals"><span class="cc-h">7 &middot; Vital-sign maneuvers</span><span class="cc-b">Orthostatic vital signs, both arms, radial-femoral delay, pulsus paradoxus, hepatojugular reflux</span></a>
    <a class="cont-card" href="#legs"><span class="cc-h">8 &middot; The legs and hands</span><span class="cc-b">Pulses, capillary refill, pitting edema, elevation and dependency, ankle-brachial index, Allen, Homan</span></a>
    <a class="cont-card" href="#flows"><span class="cc-h">9 &middot; Found something? Do this next</span><span class="cc-b">From the finding in the room to the maneuver that settles it</span></a>
    <a class="cont-card" href="#drill"><span class="cc-h">10 &middot; Quick drill</span><span class="cc-b">Sixteen results; name where each one points, then tap to check</span></a>
  </div>
</section>
'''

MEMORY = '''<section class="deck" id="memory">
  <h2 class="deck-title">1 &middot; The memory system</h2>
  <div class="memo">
    <p class="memo-label">Memory aid &mdash; one picture for every heart maneuver</p>
    <p><b>The left ventricle is a water tank.</b> Blood comes in through the <b>back door</b> (the mitral valve) and leaves through the
    <b>front door</b> (the aortic valve) to the body. Every heart maneuver does one of four things to that tank.</p>
    <ol class="rules">
      <li><b>Fill it or drain it.</b> Squatting and raising the legs push the blood stored in the legs back to the heart &mdash; the tank
      <b>fills</b>.''' + T("PD2 62") + ''' Valsalva and standing up quickly leave blood in the legs and chest &mdash; the tank
      <b>drains</b>.''' + T("PD2 61", "PD2 62") + '''</li>
      <li><b>More water, more noise.</b> Almost every murmur gets <b>louder on a full tank and softer on an empty one</b>: aortic stenosis
      (more blood rushing past the narrow front door''' + T("PD2 62") + '''), mitral and aortic regurgitation''' + T("L23 48", "L23 28") + ''', and the
      innocent flow murmur, which fades when the patient stands, sits up or bears down.''' + T("PD2 66") + '''</li>
      <li><b>Two rebels get worse on an EMPTY tank.</b> <i>Hypertrophic cardiomyopathy</i> is a bulging wall (the thick septum) beside the
      front door: a full tank holds the walls apart, the outflow obstruction lessens and the murmur softens''' + T("PD2 62") + '''; drain the tank
      and the bulge closes in on the door &mdash; louder.''' + T("PD2 61") + ''' <i>Mitral valve prolapse</i> is a floppy back-door flap: on a
      draining tank its murmur increases''' + T("Handout") + '''; fill the tank and the click moves later in systole.''' + T("PD2 62") + '''
      <br><b>So: a murmur that gets LOUDER with Valsalva or standing is one of the two rebels &mdash; and a click means prolapse.</b></li>
      <li><b>Lean on the front door.</b> A sustained handgrip raises the pressure the heart pumps against (afterload).''' + T("Handout") + '''
      Blood that can go backward does: mitral regurgitation, aortic regurgitation and a ventricular septal defect get
      <b>louder</b>.''' + T("PD2 63") + ''' The murmurs of blood leaving through the front door &mdash; aortic stenosis and hypertrophic
      cardiomyopathy &mdash; get <b>softer</b>.''' + T("L23 17", "Handout") + '''</li>
      <li><b>A breath feeds the right side.</b> Breathing in pulls more blood into the right heart, so right-sided sounds get louder on
      inspiration: <b>RILE &mdash; Right Inspiration, Left Expiration</b>.''' + T("L23 10") + ''' A holosystolic murmur that grows on
      inspiration is tricuspid, not mitral (the Carvallo sign).''' + T("L23 71") + '''</li>
      <li><b>Bring the tank to the microphone.</b> <i>Left side down</i> rolls the apex against the chest wall &mdash; for the
      <b>low</b> sounds at the apex, with the bell: S3, S4, mitral stenosis.''' + T("PD2 40", "PD2 42", "PD2 79") + ''' <i>Sit up, lean forward,
      breathe out and hold</i> &mdash; for the <b>high</b> sounds along the left sternal border: aortic regurgitation and the pericardial
      rub.''' + T("PD2 77", "PD2 81") + '''</li>
    </ol>
    <p class="memo-label" style="margin-top:14px">And for the legs &mdash; arteries hate elevation, veins hate hanging</p>
    <p>Arteries push blood <b>down</b> to the foot; veins carry it back <b>up</b>. Raise a leg with sick arteries and the blood cannot
    climb: the foot goes <b>pale</b>; let it hang and it flushes <b>deep red</b> (dependent rubor) &mdash; peripheral artery
    disease.''' + T("L27 30", "PD2 91") + ''' Let a leg with sick veins hang and blood pools: <b>dusky, swollen, varicose</b>''' + T("PD2 93", "L26 40") + '''
    &mdash; and raising it brings relief.''' + T("L26 6") + '''</p>
  </div>
  <p class="breaks"><b>Where the picture breaks.</b> It is a way to hold the <i>direction</i> of each change, not the physiology. The slides
  give results, not a flap-and-strings mechanism for prolapse. Mitral stenosis and pulmonic stenosis also sit on the deck&rsquo;s handgrip
  list''' + T("PD2 63") + ''' though neither is a backward leak &mdash; learn those two as list facts. And one exception to rule 5: the pulmonic
  ejection sound gets <i>softer</i> on inspiration.''' + T("PD2 38") + '''</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Marked in the lecture</span>
    <p>The deck puts this in capitals on the hypertrophic cardiomyopathy maneuvers slide: <em>&ldquo;IMPORTANT TO LEARN THIS MURMUR SO YOU DON&rsquo;T
    SIGN OFF INCORRECTLY ON A SPORTS PHYSICAL.&rdquo;</em>''' + T("PD2 60") + ''' Rules 2 and 3 are how you catch it: an innocent murmur
    softens when the athlete stands or bears down; hypertrophic cardiomyopathy gets louder.</p>
  </div>
</section>
'''

ONE_SCREEN_ROWS = [
    ("Left side down (left lateral decubitus), bell at the apex", "Brings the apex to the chest wall",
     "S3, S4, the mitral stenosis rumble, mitral regurgitation", "&mdash;",
     "S3 &rarr; " + HF + "; S4 &rarr; " + HTN.replace(">Hypertension<", ">hypertension<") + ", aortic stenosis, hypertrophic cardiomyopathy; rumble &rarr; mitral stenosis"),
    ("Sit up, lean forward, breathe out and hold", "Brings the base forward",
     "Aortic regurgitation, pericardial rub, aortic stenosis", "&mdash;",
     "Blowing diastolic murmur &rarr; aortic regurgitation (with tearing pain: " + DISS.replace(">Aortic dissection<", ">dissection<") + "); scratchy rub &rarr; " + PERI.replace(">Acute pericarditis<", ">pericarditis<")),
    ("Valsalva, or standing up quickly from a squat", "Drains the tank (less preload)",
     "Hypertrophic cardiomyopathy, mitral valve prolapse", "Aortic stenosis, mitral and aortic regurgitation, innocent murmur",
     "Louder &rarr; " + HCM.replace(">Hypertrophic", ">hypertrophic") + " (or prolapse if there is a click); softer &rarr; aortic stenosis or an innocent murmur"),
    ("Squatting from standing, or raising the legs", "Fills the tank (more preload)",
     "Aortic stenosis, mitral and aortic regurgitation", "Hypertrophic cardiomyopathy, mitral valve prolapse (click later)",
     "Louder &rarr; " + AS.replace(">Aortic", ">aortic") + "; softer &rarr; hypertrophic cardiomyopathy"),
    ("Sustained handgrip", "Leans on the front door (more afterload)",
     "Mitral regurgitation, aortic regurgitation, ventricular septal defect, mitral stenosis (and, on the slide, pulmonic stenosis)",
     "Aortic stenosis, hypertrophic cardiomyopathy, mitral valve prolapse",
     "Louder at the apex &rarr; " + MR.replace(">Mitral", ">mitral")),
    ("Breathe in", "Feeds the right heart", "Right-sided murmurs: tricuspid and pulmonic regurgitation", "Pulmonic ejection sound",
     "Holosystolic murmur louder on inspiration &rarr; tricuspid regurgitation (Carvallo sign)"),
]


def one_screen():
    h = '''<section class="deck" id="one-screen">
  <h2 class="deck-title">2 &middot; Everything on one screen</h2>
  <p>The heart maneuvers side by side. Sources and detail are in sections 3&ndash;6.</p>
  <div class="tw"><table class="glance">
    <tr><th>Maneuver</th><th>What it does</th><th>Louder</th><th>Softer</th><th>Where the result points</th></tr>
'''
    for row in ONE_SCREEN_ROWS:
        h += "    <tr>" + "".join("<td>%s</td>" % c for c in row) + "</tr>\n"
    h += '''  </table></div>
  <div class="tw"><table class="glance">
    <tr><th>Leg or vital-sign maneuver</th><th>Positive result</th><th>Where it points</th></tr>
    <tr><td>Orthostatic vital signs</td><td>Systolic falls more than 20 or diastolic more than 10 within 3 minutes of standing</td><td>''' + OH + '''</td></tr>
    <tr><td>Pressure in both arms</td><td>Arms differ by more than 10&ndash;15 mmHg</td><td>Subclavian stenosis; with tearing pain, ''' + DISS.replace(">Aortic", ">aortic") + '''</td></tr>
    <tr><td>Radial and femoral pulses together</td><td>The femoral pulse lags</td><td>Coarctation of the aorta</td></tr>
    <tr><td>Pulsus paradoxus</td><td>Systolic pressure falls on inspiration</td><td>''' + TAMP + '''</td></tr>
    <tr><td>Hepatojugular reflux</td><td>Neck veins distend with firm pressure over the liver</td><td>Congestion: ''' + HF.replace(">Heart", ">heart") + ''', cardiomyopathy</td></tr>
    <tr><td>Raise the leg, then let it hang</td><td>Pale when raised, deep red when hanging</td><td>''' + PAD + '''</td></tr>
    <tr><td>Ankle-brachial index</td><td>Below 0.90 (below 0.50 severe); above 1.40 calcified</td><td>''' + PAD + '''</td></tr>
    <tr><td>Allen test</td><td>The hand stays white after you release one artery</td><td>That artery is not patent</td></tr>
    <tr><td>Homan sign</td><td>Pain behind the knee on quick dorsiflexion</td><td>''' + DVT + ''' (neither sensitive nor specific)</td></tr>
    <tr><td>Pitting edema</td><td>Both legs, with raised neck veins / one leg / brown staining</td><td>''' + HF + ''' / ''' + DVT.replace(">Deep", ">deep") + ''' / ''' + CVI.replace(">Chronic", ">chronic") + '''</td></tr>
  </table></div>
</section>
'''
    return h


def positions():
    h = '<section class="deck" id="positions">\n  <h2 class="deck-title">3 &middot; Positions: bring the sound to the stethoscope</h2>\n'
    h += '  <p>Do these after the routine five areas. The deck lists two special positions.' + T("PD2 59") + '</p>\n'
    h += card("pos-left", "Left lateral decubitus &mdash; left side down, bell at the apex",
              "Roll the patient onto the left side. Find the apical impulse and listen there with the <b>bell</b>, held lightly."
              + T("PD2 59", "PD2 79"),
              "I&rsquo;m going to have you roll onto your left side so I can listen at the apex with the bell for low-pitched sounds.",
              [("A low sound just <b>after S2</b>, with the bell &mdash; Ken-TUC-ky" + T("PD2 40"),
                "<b>S3.</b> Over age 40: " + HF + " or volume overload from aortic or mitral regurgitation. Normal in children, young adults up to 35&ndash;40 and late pregnancy." + T("PD2 40")),
               ("A dull, low sound just <b>before S1</b> &mdash; TEN-nes-see" + T("PD2 42"),
                "<b>S4</b>, a stiff ventricle: " + HTN.replace(">Hypertension<", ">hypertensive heart disease<") + ", " + AS.replace(">Aortic", ">aortic")
                + ", ischemic and " + HCM.replace(">Hypertrophic", ">hypertrophic") + ". Normal in trained athletes and older adults." + T("PD2 42")),
               ("A low-pitched <b>rumble</b> in mid to late diastole at the apex, after an opening snap" + T("PD2 79", "L23 38"),
                "<b>Mitral stenosis.</b>"),
               ("A <b>holosystolic</b>, blowing murmur at the apex" + T("L23 48"),
                MR + " &mdash; then follow it into the left axilla." + T("PD2 74"))])
    h += card("pos-forward", "Sitting up, leaning forward, breath out and held",
              "Sit the patient up, leaning forward; ask them to breathe all the way out and hold it. Listen along the left sternal border with the diaphragm."
              + T("PD2 59", "L31 17"),
              "Please sit up and lean forward, breathe all the way out, and hold your breath for a few seconds while I listen.",
              [("A high-pitched, <b>blowing, decrescendo</b> murmur right after S2" + T("PD2 77"),
                "<b>Aortic regurgitation.</b> New, with tearing chest or back pain and unequal arm pressures: " + DISS + "." + T("L20 29")),
               ("A <b>scratchy, scraping</b> sound through systole and diastole, loudest at Erb&rsquo;s point" + T("PD2 81"),
                "<b>Pericardial friction rub</b> &rarr; " + PERI + ". It stays with the breath held; a pleural rub is heard only during inspiration." + T("L31 17")),
               ("A harsh midsystolic crescendo-decrescendo murmur at the right second intercostal space",
                AS + " &mdash; heard better sitting and leaning forward." + T("PD2 67", "L23 17"))])
    h += "</section>\n"
    return h


def filling():
    h = '<section class="deck" id="filling">\n  <h2 class="deck-title">4 &middot; Fill or drain the tank: Valsalva, standing, squatting, leg raise</h2>\n'
    h += ('  <p>These are the maneuvers that <b>separate the systolic murmurs</b> &mdash; above all, hypertrophic cardiomyopathy and mitral valve prolapse '
          'from aortic stenosis.' + T("PD2 60") + '</p>\n')
    h += card("valsalva", "Valsalva &mdash; drains the tank",
              "Patient supine. Ask them to bear down, like straining for a bowel movement, or to push against your hand on the mid-abdomen. Forceful expiration against a closed airway raises the pressure in the chest and <b>decreases left ventricular filling</b> (preload)." + T("PD2 61"),
              "I&rsquo;d like you to bear down as if you&rsquo;re straining, and keep holding while I listen.",
              [("The murmur gets <b>LOUDER</b>", HCM + "." + T("PD2 61") + " With a mid-systolic click instead: " + MVP + " (its murmur increases)." + T("Handout")),
               ("The murmur gets <b>softer or does not change</b>", AS + "." + T("PD2 61") + " A grade 1&ndash;3 murmur in a young person that softens: an innocent flow murmur." + T("PD2 66")),
               ("A holosystolic murmur at the apex gets softer", MR + "." + T("L23 48"))],
              "The deck adds that Valsalva can also identify heart failure and pulmonary hypertension." + T("PD2 61"))
    h += card("stand", "Standing up quickly from a squat &mdash; drains the tank",
              "Patient squats; listen; then the patient stands up quickly while you listen. Blood moves to the legs, less returns to the heart, and <b>left ventricular preload falls</b>." + T("PD2 62"),
              "I&rsquo;m going to have you squat down, then stand up quickly with me while I keep listening.",
              [("The murmur gets <b>LOUDER</b>", HCM + "." + T("PD2 62", "PD2 70") + " Mitral valve prolapse also increases." + T("Handout")),
               ("The murmur gets <b>softer</b>", AS + "." + T("PD2 62") + " An innocent murmur also softens on standing." + T("PD2 66"))])
    h += card("squat", "Squatting from standing, or raising the legs &mdash; fills the tank",
              "From standing, have the patient squat while you listen; or, if they cannot squat, raise their legs while they lie supine. Blood stored in the legs returns to the heart and <b>preload rises</b>." + T("PD2 62"),
              "Now I&rsquo;m going to raise your legs for a moment while I listen.",
              [("The murmur gets <b>LOUDER</b>", AS + " &mdash; more blood rushing past the narrow valve." + T("PD2 62") + " Mitral regurgitation and aortic regurgitation also increase." + T("L23 48", "L23 28")),
               ("The murmur gets <b>softer</b>", HCM + " &mdash; the outflow obstruction lessens." + T("PD2 62")),
               ("The click moves <b>later</b> in systole", MVP + "." + T("PD2 62"))])
    h += '''  <h3 class="sub" id="filling-table">The systolic murmurs through the filling maneuvers</h3>
  <div class="tw"><table class="glance">
    <tr><th>Murmur</th><th>Drain the tank<br>Valsalva &middot; standing</th><th>Fill the tank<br>squatting &middot; leg raise</th><th>Where it is</th></tr>
    <tr><td>''' + AS + '''</td><td>''' + DOWN + ''' or no change''' + T("PD2 61", "PD2 62") + '''</td><td>''' + UP + T("PD2 62") + '''</td><td>Right second intercostal space &rarr; carotids''' + T("L23 17", "PD2 67") + '''</td></tr>
    <tr><td>''' + HCM + '''</td><td>''' + UP + T("PD2 61", "PD2 62") + '''</td><td>''' + DOWN + T("PD2 62") + '''</td><td>Erb&rsquo;s point, tricuspid area; never to the neck''' + T("PD2 70") + '''</td></tr>
    <tr><td>''' + MVP + '''</td><td>''' + UP + T("Handout") + '''</td><td>''' + DOWN + ''', click later''' + T("Handout", "PD2 62") + '''</td><td>Click at or medial to the apex''' + T("PD2 39") + '''</td></tr>
    <tr><td>''' + MR + '''</td><td>''' + DOWN + T("L23 48") + '''</td><td>''' + UP + T("L23 48", "PD2 74") + '''</td><td>Apex &rarr; left axilla''' + T("PD2 74") + '''</td></tr>
    <tr><td>Innocent flow murmur</td><td>''' + DOWN + T("PD2 66") + '''</td><td>&mdash;</td><td>Grade 1&ndash;3 of 6''' + T("PD2 66") + '''</td></tr>
  </table></div>
  <p><b>Read across:</b> with every fill-or-drain maneuver, aortic stenosis and hypertrophic cardiomyopathy move in <i>opposite</i> directions, and prolapse moves with
  hypertrophic cardiomyopathy (handgrip is the exception: it softens both). The click is what separates prolapse from hypertrophic cardiomyopathy.</p>
</section>
'''
    return h


def handgrip():
    h = '<section class="deck" id="handgrip">\n  <h2 class="deck-title">5 &middot; Handgrip: lean on the front door</h2>\n'
    h += card("grip", "Sustained isometric handgrip",
              "Have the patient squeeze both hands as hard as they can and hold while you listen. It raises systemic arterial pressure (afterload)." + T("PD2 63", "Handout"),
              "Squeeze my hands as hard as you can and keep squeezing while I listen.",
              [("A holosystolic murmur at the apex gets <b>LOUDER</b>", MR + "." + T("PD2 63", "L23 48")),
               ("A blowing early diastolic murmur gets <b>LOUDER</b>", "Aortic regurgitation." + T("PD2 63", "L23 28")),
               ("A diastolic rumble at the apex gets <b>LOUDER</b>", "Mitral stenosis." + T("PD2 63", "L23 38")),
               ("A systolic murmur gets <b>LOUDER</b>", "Ventricular septal defect (or, by the slide, pulmonic stenosis)." + T("PD2 63")),
               ("A midsystolic ejection murmur gets <b>softer</b>", AS + T("L23 17", "Handout") + " or " + HCM.replace(">Hypertrophic", ">hypertrophic") + "." + T("Handout"))],
              "The slide&rsquo;s handgrip list and the handout disagree about the mitral valve: the slide has mitral regurgitation louder, the handout has mitral valve prolapse softer. Learn each as its source gives it.")
    h += "</section>\n"
    return h


def breathing():
    h = '<section class="deck" id="breathing">\n  <h2 class="deck-title">6 &middot; Breathing: RILE</h2>\n'
    h += ('  <p><b>Right-sided sounds get louder on Inspiration, Left-sided on Expiration.</b>' + T("L23 10") +
          ' Ask the patient to take a slow deep breath in and out while you stay on the spot.</p>\n')
    h += card("breath", "Deep breath in, then out",
              "Listen through a slow, deep breath at the lower left sternal border and the pulmonic area; for neck veins, watch them through the breath.",
              "Take a slow, deep breath in for me&hellip; and all the way out.",
              [("A holosystolic murmur at the lower left sternal border gets <b>louder on inspiration</b>",
                "<b>Tricuspid regurgitation</b> &mdash; the Carvallo sign, which distinguishes it from mitral regurgitation." + T("L23 71", "PD2 73")),
               ("A holosystolic murmur at the apex, radiating to the axilla, without that inspiratory increase", MR + " &mdash; the Carvallo sign is what separates the two." + T("L23 71", "PD2 74")),
               ("An early diastolic murmur in the pulmonic area that grows on inspiration", "Pulmonic regurgitation." + T("PD2 78", "L23 63")),
               ("S2 splits into two sounds on inspiration and fuses on expiration", "<b>Normal</b> &mdash; physiologic splitting of S2." + T("PD2 15")),
               ("The scratchy sound <b>stops</b> when the breath is held", "A pleural rub, not a pericardial one (a pleural rub is heard only during inspiration)." + T("L31 17")),
               ("The neck veins <b>rise</b> on inspiration instead of falling", "<b>Kussmaul sign</b>: constrictive pericarditis or restrictive cardiomyopathy." + T("L31 39", "L28 92"))],
              "Two inspiration exceptions: the pulmonic ejection sound gets softer on inspiration, and the aortic ejection sound does not vary." + T("PD2 38"))
    h += "</section>\n"
    return h


def vitals():
    h = '<section class="deck" id="vitals">\n  <h2 class="deck-title">7 &middot; Vital-sign maneuvers</h2>\n'
    h += '  <p>Say these out loud even when the vitals form already has the numbers: they are how you rule a diagnosis in or out.</p>\n'
    h += card("ortho", "Orthostatic vital signs",
              "Blood pressure and heart rate supine, then standing; read within 3 minutes." + T("L21 13", "L20 39"),
              "I&rsquo;d like to check your blood pressure lying down and again after you stand.",
              [("Systolic falls <b>more than 20</b> or diastolic <b>more than 10</b> within 3 minutes (or systolic more than 30 with a high baseline or supine hypertension)",
                OH + "." + T("L21 13")),
               ("&hellip; and the heart rate rises a lot (68 &rarr; 92)", "Non-neurogenic: volume loss or medicines &mdash; diarrhea, hemorrhage, diuretics." + T("L21 34-36")),
               ("&hellip; and the heart rate barely rises (72 &rarr; 76)", "Neurogenic: autonomic failure &mdash; diabetes, Parkinson disease." + T("L21 30", "L21 36")),
               ("Heart rate rises more than 30 (or above 120) within 10 minutes of standing", "Postural orthostatic tachycardia syndrome." + T("L21 18")),
               ("Normal orthostatic readings, with a trigger such as fear, pain, heat or long standing", VV + "." + T("L21 14"))])
    h += card("arms", "Blood pressure in both arms, and radial with femoral pulses",
              "Measure the pressure in both arms (at the first visit" + T("L20 39") + "; with tearing pain, to look for a difference" + T("L20 29") + "). Then feel the radial and femoral pulses at the same time." + T("PD2 102"),
              "I&rsquo;m going to check the pressure in both arms and feel the pulses at your wrist and groin together.",
              [("Arms differ by more than 10&ndash;15 mmHg", "Subclavian stenosis or other vascular disease." + T("L20 39")),
               ("Unequal arm pressures or a pulse deficit, with tearing pain maximal at onset", DISS + " &mdash; and normal pulses do not exclude it." + T("L20 29")),
               ("The femoral pulse <b>lags</b> behind the radial", "<b>Coarctation of the aorta</b>; measure the leg pressure." + T("PD2 102", "L20 39", "L20 40"))])
    h += card("pulsus", "Pulsus paradoxus",
              "With a manual cuff, deflate slowly: note the pressure where sounds appear only on expiration, then where they are heard throughout the breath." + T("Textbook"),
              "I&rsquo;m going to watch how your blood pressure changes as you breathe.",
              [("Systolic pressure <b>falls with inspiration</b> &mdash; by more than 10 mmHg" + T("L31 59", "Slide notes"),
                TAMP + ", with Beck triad: low pressure, distended neck veins, muffled heart sounds." + T("L31 54", "L31 59") + " Also seen in constrictive pericarditis." + T("L31 44"))])
    h += card("hjr", "Hepatojugular reflux",
              "Press firmly over the liver and watch the neck veins." + T("L28 33"),
              "I&rsquo;m going to press on your belly for a few seconds while I watch your neck.",
              [("The neck veins <b>distend</b> with pressure over the liver",
                "Venous congestion: " + HF + " (right-sided failure backs up into the neck veins" + T("L25 10") + "), dilated or restrictive cardiomyopathy." + T("L28 33", "L28 93"))])
    h += "</section>\n"
    return h


def legs():
    h = '<section class="deck" id="legs">\n  <h2 class="deck-title">8 &middot; The legs and hands: arteries hate elevation, veins hate hanging</h2>\n'
    h += '  <p><b>Always compare both sides.</b>' + T("PD2 86") + '</p>\n'
    h += card("pulses", "Pulses &mdash; grade every one, 0 to 4+",
              "Radial, brachial, femoral, popliteal, posterior tibial and dorsalis pedis, both sides." + T("PD2 98-104") + " 4+ bounding, 3+ increased, 2+ brisk (normal), 1+ diminished, 0 absent." + T("PD2 86"),
              "Pulses are 2+ and symmetric in the upper and lower extremities.",
              [("Absent or diminished distal pulses", PAD + " (atherosclerosis), a systemic embolism, or small-vessel disease such as diabetes." + T("PD2 96", "L20 40")),
               ("Bounding pulses with a wide pulse pressure", "Aortic regurgitation." + T("L23 28")),
               ("A double systolic peak (pulsus bisferiens)", HCM + "." + T("L28 67")),
               ("A weak, delayed carotid with a forceful apex, felt together", AS + ", severe." + T("L23 17"))])
    h += card("caprefill", "Capillary refill",
              "Press on a fingernail, release, and time how long the nail bed takes to turn pink." + T("PD2 85"),
              "Capillary refill is two to three seconds.",
              [("Pink within <b>2&ndash;3 seconds</b>", "Normal." + T("PD2 85")),
               ("The nail bed flashes red to pale with each heartbeat (Quincke pulse)" + T("PD2 85"),
                "Classically aortic regurgitation." + T("Textbook"))])
    h += card("edema", "Pitting edema &mdash; press, then grade",
              "Press firmly with the thumb for at least 2 seconds over the dorsum of the foot, behind the medial malleolus and over the shin. Grade it and say how high it goes."
              + T("PD2 88") + "<br><span class=\"grades\">1+ 2 mm, gone quickly &middot; 2+ 4 mm, gone in 10&ndash;15 s &middot; 3+ 6 mm, lasts over 1 min &middot; 4+ 8 mm, lasts over 2 min</span>" + T("PD2 89"),
              "There is 2+ pitting edema of both lower legs to the mid-shin.",
              [("<b>Both</b> legs, with raised neck veins", HF + " (right-sided)." + T("L25 10")),
               ("<b>One</b> leg, swollen, warm and tender", DVT + " &mdash; swelling is 97% sensitive." + T("L26 51")),
               ("Edema with brown (hemosiderin) staining, ulcers over the malleoli, normal pulses", CVI + "." + T("PD2 93")),
               ("<b>No</b> edema, with cool, shiny, hairless skin and weak pulses", PAD + "." + T("PD2 91"))])
    h += card("buerger", "Raise the leg, then let it hang (Buerger test)",
              "Supine: raise one leg to 45 degrees for 1 minute and look at the foot. Then sit the patient up with the legs hanging over the side of the bed." + T("L27 30")
              + " For veins, look at the legs with the patient <b>standing</b>." + T("L26 40"),
              "I&rsquo;m going to raise your leg for a minute, then have you sit with your legs hanging over the side.",
              [("<b>Pale</b> when raised, then <b>deep red</b> when hanging (dependent rubor)", PAD + " &mdash; the arteries cannot push blood uphill." + T("L27 30", "PD2 91")),
               ("Dusky, bluish foot when hanging, brown pigmentation, normal pulses", CVI + "." + T("PD2 93")),
               ("Dilated, tortuous veins seen and felt when the patient stands", "Varicose veins &mdash; long-standing ones progress to chronic venous insufficiency." + T("L26 40"))])
    h += card("abi", "Ankle-brachial index",
              "Supine for 10 minutes. Doppler and cuff: brachial pressure (two readings averaged in each arm; use the higher arm), then dorsalis pedis and posterior tibial at the ankle, cuff just above the malleoli. Take the <b>higher ankle pressure &divide; the brachial systolic pressure</b>, for each leg, to 2 decimal places." + T("PD2 110-112", "L27 27"),
              "I would order an ankle-brachial index to look for arterial disease in the legs.",
              [("<b>0.90&ndash;1.40</b>", "Normal." + T("PD2 110")),
               ("<b>Below 0.90</b>", PAD + "." + T("PD2 113")),
               ("<b>Below 0.50</b>", "Severe peripheral artery disease." + T("PD2 113")),
               ("<b>Above 1.40</b>", "A noncompressible, calcified vessel (diabetes, for example) &mdash; the number is not reliable." + T("PD2 113", "L27 42"))],
              "The Clinical Medicine deck uses slightly different cut-offs (normal above 0.9 to 1.3; claudication 0.4&ndash;0.9; rest pain or tissue loss 0&ndash;0.4)." + T("L27 42") + " For this station, use the Physical Diagnosis numbers above.")
    h += card("allen", "Allen test",
              "The patient clenches a fist for 30 seconds; press on both the radial and ulnar arteries; the patient opens the hand (it is white); release the <b>ulnar</b> artery and watch the hand. Repeat, releasing the radial." + T("PD2 108"),
              "I&rsquo;m checking that both arteries supply the hand.",
              [("The hand <b>pinks up</b> when you release the artery", "That artery is patent &mdash; normal." + T("PD2 108")),
               ("The hand <b>stays white</b>", "That artery is not patent: poor arterial supply to the hand from it." + T("PD2 108"))])
    h += card("homan", "Homan sign",
              "Keep the knee bent and quickly, forcefully dorsiflex the foot at the ankle. Do it on the leg you are worried about." + T("PD2 114"),
              "I&rsquo;m going to bend your foot up quickly; tell me if that hurts.",
              [("<b>Pain behind the knee</b>", DVT + "." + T("PD2 114")),
               ("A negative result", "Does not rule it out: the sign is neither sensitive nor specific." + T("L26 51") + " Score the Wells criteria and get a venous duplex ultrasound." + T("L26 54", "L26 57"))])
    h += "</section>\n"
    return h


FLOWS = [
    ("A harsh <b>midsystolic</b> murmur", "Valsalva, or squat &rarr; stand",
     "Louder &rarr; " + HCM + " (a click &rarr; " + MVP.replace(">Mitral", ">mitral") + "). Softer &rarr; " + AS.replace(">Aortic", ">aortic") + " if it goes to the carotids in an older patient; an innocent murmur if grade 1&ndash;3 in a young one. Confirm with squatting or a leg raise: the opposite change."),
    ("A <b>holosystolic</b> murmur", "Breathe in; then handgrip",
     "Louder on inspiration &rarr; tricuspid regurgitation. No change, at the apex into the axilla, louder with handgrip &rarr; " + MR.replace(">Mitral", ">mitral") + "."),
    ("A <b>click</b> in mid-systole", "Stand up quickly, then squat",
     "Murmur increases on standing; the click moves later on squatting &rarr; " + MVP.replace(">Mitral", ">mitral") + "."),
    ("A soft <b>diastolic</b> murmur, or you are not sure", "Sit up, lean forward, out and hold; then left side down with the bell",
     "Blowing, after S2, along the left sternal border &rarr; aortic regurgitation (tearing pain &rarr; " + DISS.replace(">Aortic", ">aortic") + "). Low rumble at the apex &rarr; mitral stenosis."),
    ("An <b>extra sound</b> at the apex", "Left side down, bell",
     "After S2 &rarr; S3 (over 40: " + HF.replace(">Heart", ">heart") + "). Before S1 &rarr; S4 (hypertension, aortic stenosis, hypertrophic cardiomyopathy)."),
    ("A <b>scratchy</b> sound", "Sit up, lean forward, out and hold",
     "Persists with the breath held &rarr; pericardial rub, " + PERI.replace(">Acute", ">acute") + ". Stops &rarr; pleural rub. Hypotension and distended neck veins too &rarr; check pulsus paradoxus for " + TAMP.replace(">Cardiac", ">cardiac") + "."),
    ("Fainting or dizziness on standing", "Orthostatic vital signs; then listen with Valsalva",
     "Pressure falls &rarr; " + OH.replace(">Orthostatic", ">orthostatic") + " (heart rate up = volume or medicines; flat = neurogenic). Normal with a trigger &rarr; " + VV.replace(">Vasovagal", ">vasovagal") + ". A murmur that grows with Valsalva in a young patient &rarr; hypertrophic cardiomyopathy."),
    ("Tearing chest or back pain", "Pressure in both arms; radial with femoral pulses; lean forward for a diastolic murmur",
     "Unequal pressures, a pulse deficit or a new aortic regurgitation murmur &rarr; " + DISS.replace(">Aortic", ">aortic") + "."),
    ("Calf pain or a swollen leg", "Compare both legs, pitting, Homan; then pulses and elevation",
     "One leg, warm, swollen &rarr; " + DVT.replace(">Deep", ">deep") + ". Both legs, brown staining, normal pulses &rarr; " + CVI.replace(">Chronic", ">chronic") + ". Pale raised, red hanging, weak pulses, no edema &rarr; " + PAD.replace(">Peripheral", ">peripheral") + " (order the ankle-brachial index)."),
]


def flows():
    h = '''<section class="deck" id="flows">
  <h2 class="deck-title">9 &middot; Found something? Do this next</h2>
  <p>From what you notice in the room, to the maneuver that settles it. Every arrow is sourced in sections 3&ndash;8.</p>
  <div class="tw"><table class="glance flow">
    <tr><th>You notice</th><th>Do</th><th>Then</th></tr>
'''
    for a, b, c in FLOWS:
        h += "    <tr><td>%s</td><td>%s</td><td>%s</td></tr>\n" % (a, b, c)
    return h + "  </table></div>\n</section>\n"


DRILL = [
    ("A systolic murmur gets louder when the patient bears down.", "Hypertrophic cardiomyopathy (or mitral valve prolapse, if there is a click)."),
    ("A systolic murmur gets louder when the patient squats and softer when they stand.", "Aortic stenosis."),
    ("A holosystolic murmur at the lower left sternal border grows on inspiration.", "Tricuspid regurgitation &mdash; the Carvallo sign."),
    ("A holosystolic apical murmur gets louder with handgrip.", "Mitral regurgitation."),
    ("A mid-systolic click moves later when the patient squats.", "Mitral valve prolapse."),
    ("A low rumble at the apex, heard with the patient on the left side and the bell.", "Mitral stenosis."),
    ("A low sound just after S2 at the apex in a 65-year-old.", "S3 &rarr; heart failure."),
    ("A scratchy sound that persists with the breath held while leaning forward.", "Pericardial rub &rarr; acute pericarditis."),
    ("Supine 142/82, heart rate 72; standing at 3 minutes 108/66, heart rate 76.", "Orthostatic hypotension, neurogenic (the heart rate barely rose)."),
    ("Arm pressures 30 mmHg apart in a patient with tearing back pain.", "Aortic dissection."),
    ("The femoral pulse lags behind the radial.", "Coarctation of the aorta."),
    ("Systolic pressure falls with inspiration in a hypotensive patient with distended neck veins.", "Pulsus paradoxus &rarr; cardiac tamponade."),
    ("The foot goes pale when raised and deep red when hanging.", "Peripheral artery disease."),
    ("Ankle-brachial index 0.45. And 1.60?", "Severe peripheral artery disease. Above 1.40: a noncompressible, calcified vessel."),
    ("The hand stays white after you release the ulnar artery.", "The ulnar artery is not patent."),
    ("Pain behind the knee on quick dorsiflexion of the foot.", "A positive Homan sign &rarr; suspect deep vein thrombosis (but a negative does not rule it out)."),
]


def drill():
    h = '''<section class="deck" id="drill">
  <h2 class="deck-title">10 &middot; Quick drill</h2>
  <p>Say where each result points, then tap to check.</p>
'''
    for i, (q, a) in enumerate(DRILL, 1):
        h += '  <details class="drill"><summary><span class="dn">%d</span> %s</summary><p>%s</p></details>\n' % (i, q, a)
    return h + "</section>\n"


SOURCES = '''<section class="deck" id="sources">
  <h2 class="deck-title">Sources, and where they disagree</h2>
  <ul>
    <li><b>Physical Diagnosis 2:</b> <em>PD II Advanced Cardiovascular &amp; Peripheral Vascular System - Fall 2026.pptx</em> (Lauren Reynolds, MSPA, PA-C), slides 15&ndash;114, and the class handout on special maneuvers.</li>
    <li><b>Clinical Medicine and Surgery:</b> Lecture 20 Hypertension (Jaquith); Lecture 21 Hypotension, 23 Valvular Heart Disease, 25 Heart Failure, 27 Arterial Occlusive Disease and Aneurysms, 28 Cardiomyopathy (Carter); Lecture 26 Venous Disorders (Shah); Lecture 31 Pericardial Disease.</li>
    <li><b>Ankle-brachial index:</b> the Physical Diagnosis deck gives normal 0.90&ndash;1.40, below 0.90 disease, below 0.50 severe, above 1.40 calcified; the Clinical Medicine deck gives normal above 0.9 to 1.3, above 1.3 calcified, and 0.4 as the rest-pain line. Use the Physical Diagnosis numbers at this station.</li>
    <li><b>Handgrip:</b> the Physical Diagnosis slide lists mitral regurgitation, pulmonic stenosis, ventricular septal defect, aortic regurgitation and mitral stenosis as louder; the handout lists aortic stenosis, mitral valve prolapse and hypertrophic cardiomyopathy as softer. Both are given as their sources say.</li>
    <li><b>Mitral stenosis and Valsalva:</b> the Clinical Medicine valvular slide also lists mitral stenosis as louder with Valsalva and exertion (&ldquo;increasing blood into the left atrium&rdquo;).''' + T("L23 38") + ''' It is left out of the filling table above, which follows the Physical Diagnosis deck.</li>
    <li><b>Venous ulcer site:</b> the Physical Diagnosis deck puts it over the medial and lateral malleolus''' + T("PD2 93") + '''; the Venous Disorders deck puts it above the ankle, on the medial or anterior side.''' + T("L26 15") + '''</li>
    <li><b>Not on a slide:</b> the pulsus paradoxus cut-off of more than 10 mmHg is in the speaker notes of Pericardial Disease slide 59 (the slide itself shows the inspiratory fall); the cuff technique for pulsus paradoxus and the meaning of a Quincke pulse are textbook.</li>
  </ul>
</section>
'''

TOC = '''<nav class="toc">
  <h2>Contents</h2>
  <a class="top-link" href="#start">How to use this page</a>
  <a class="top-link" href="#memory">1 &middot; The memory system</a>
  <a class="top-link" href="#one-screen">2 &middot; Everything on one screen</a>
  <a class="top-link" href="#positions">3 &middot; Positions</a>
  <a class="sub-link" href="#pos-left">Left side down</a>
  <a class="sub-link" href="#pos-forward">Sit up, lean forward</a>
  <a class="top-link" href="#filling">4 &middot; Fill or drain the tank</a>
  <a class="sub-link" href="#valsalva">Valsalva</a>
  <a class="sub-link" href="#stand">Standing from a squat</a>
  <a class="sub-link" href="#squat">Squatting, leg raise</a>
  <a class="sub-link" href="#filling-table">The systolic murmurs</a>
  <a class="top-link" href="#handgrip">5 &middot; Handgrip</a>
  <a class="top-link" href="#breathing">6 &middot; Breathing: RILE</a>
  <a class="top-link" href="#vitals">7 &middot; Vital-sign maneuvers</a>
  <a class="sub-link" href="#ortho">Orthostatic vital signs</a>
  <a class="sub-link" href="#arms">Both arms, radial-femoral</a>
  <a class="sub-link" href="#pulsus">Pulsus paradoxus</a>
  <a class="sub-link" href="#hjr">Hepatojugular reflux</a>
  <a class="top-link" href="#legs">8 &middot; The legs and hands</a>
  <a class="sub-link" href="#pulses">Pulses</a>
  <a class="sub-link" href="#caprefill">Capillary refill</a>
  <a class="sub-link" href="#edema">Pitting edema</a>
  <a class="sub-link" href="#buerger">Raise, then hang</a>
  <a class="sub-link" href="#abi">Ankle-brachial index</a>
  <a class="sub-link" href="#allen">Allen test</a>
  <a class="sub-link" href="#homan">Homan sign</a>
  <a class="top-link" href="#flows">9 &middot; Found something? Do this next</a>
  <a class="top-link" href="#drill">10 &middot; Quick drill</a>
  <a class="top-link" href="#sources">Sources</a>
</nav>'''

CSS = '''
  /* Cardiac OSCE maneuvers guide (tools/build_pd2_cardiac_osce_maneuvers.py) */
  .io-tag{margin:0 0 4px;font-weight:700;color:var(--accent3);}
  .memo{border:2px dashed var(--accent2);background:#fdf8ee;border-radius:12px;padding:14px 18px 8px;margin:16px 0;}
  .memo-label{font-size:.74rem;text-transform:uppercase;letter-spacing:1px;font-weight:800;color:#8c631b;margin:0 0 6px;}
  ol.rules{padding-left:22px;}
  ol.rules li{margin-bottom:9px;}
  .breaks{font-size:.92rem;color:var(--soft);}
  .mv{background:#ffffff;border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:10px;padding:12px 16px 6px;margin:16px 0;scroll-margin-top:18px;}
  h4.mv-h{margin:0 0 6px;color:var(--accent3);font-size:1.06rem;font-weight:800;}
  .mv p.do{margin:4px 0;}
  .mv p.say{margin:4px 0 8px;color:var(--soft);font-style:italic;}
  .mv p.say b{font-style:normal;color:var(--accent);}
  .mv-note{font-size:.88rem;color:var(--soft);}
  table.res td:first-child{width:46%;}
  table.glance td,table.res td{font-size:.9rem;}
  a.cx{color:var(--accent);font-weight:700;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:2px;}
  .up{color:#1f6b3a;font-weight:800;white-space:nowrap;}
  .down{color:#8c3b12;font-weight:800;white-space:nowrap;}
  .grades{display:inline-block;margin-top:4px;font-size:.86rem;color:var(--soft);}
  details.drill{background:#ffffff;border:1px solid var(--line);border-radius:10px;padding:9px 14px;margin:8px 0;}
  details.drill summary{cursor:pointer;font-weight:600;}
  details.drill p{margin:8px 0 2px;color:var(--accent3);font-weight:700;}
  .dn{display:inline-block;min-width:1.6em;color:var(--accent2);font-weight:800;}
  .prof-flag{border:2px solid var(--accent2);background:#fdf8ee;border-radius:10px;padding:10px 16px;margin:16px 0;}
  .prof-flag-label{font-size:.74rem;text-transform:uppercase;letter-spacing:1px;font-weight:800;color:#8c631b;}
  :root[data-theme="dark"] .up{color:#6cc98a;}
  :root[data-theme="dark"] .down{color:#e39470;}
  :root[data-theme="dark"] .memo-label,:root[data-theme="dark"] .prof-flag-label{color:#d6a650;}
'''


def build_body():
    return ("<main>\n\n" + INTRO + MEMORY + one_screen() + positions() + filling() + handgrip() + breathing()
            + vitals() + legs() + flows() + drill() + SOURCES)


def main():
    donor = open(DONOR, encoding="utf-8").read()
    head = donor[:donor.index('<div class="layout wrap"')]
    tail = donor[donor.index('<footer class="guide-foot">\n  <p style="text-align:center;margin:0 0 10px;">'):]
    head = re.sub(r'\s*<link rel="alternate" type="application/vnd\.openxmlformats[^>]*>', "", head)
    head = re.sub(r"<!--DARK-TOKENS:BEGIN.*?<!--DARK-TOKENS:END-->", "", head, flags=re.S)
    head = re.sub(r"<title>.*?</title>", "<title>Cardiac OSCE Special Maneuvers &mdash; Physical Diagnosis 2</title>", head, count=1, flags=re.S)
    head = re.sub(r'<header class="top">.*?</header>',
        '<header class="top">\n'
        '  <h1>Cardiac OSCE &middot; Special Maneuvers</h1>\n'
        '  <p>PAJ 5310 Physical Diagnosis II &middot; Class of 2028 &middot; Cardiac OSCE Wednesday 21 October</p>\n'
        '  <p>How to remember each maneuver, what to say while you do it, and which disease or disorder each result points to &middot; Companion to the run-sheet and disease chart</p>\n'
        '</header>', head, count=1, flags=re.S)
    head = head.replace("</style>", CSS + "</style>", 1)
    tail = tail.replace("lecture decks for personal study", "lecture decks and the Clinical Medicine and Surgery cardiology decks for personal study", 1)
    html = head + '<div class="layout wrap" data-readable>\n' + TOC + "\n\n" + build_body() + "\n" + tail
    for need in ('class="guide-back-bar"', "window.reportMistake()", "../theme.js", 'data-dark-kind="guide"', "</main>"):
        assert need in html, "missing chrome: %r" % need
    for bad in ("ENT OSCE Study Guide</h1>", "Cerumen", "pd2-ent-osce-study-guide.docx"):
        assert bad not in html, "donor residue: %r" % bad
    main_text = re.sub(r"<[^>]+>", " ", html.split("<main>")[1].split("</main>")[0])
    for ab in ("HOCM", "HCM", "MVP", "JVP", "JVD", "ABI", "DVT", "PAD", "CVI", "LLD", "RUSB", "LLSB", "VSD", "SBP", "DBP", "POTS", "HF "):
        assert not re.search(r"\b%s\b" % ab.strip(), main_text), "abbreviation left: %s" % ab
    assert "RILE" in main_text
    for slug in re.findall(r'href="%s#c-([a-z0-9-]+)"' % re.escape(CHART), html):
        chart = open(os.path.join(FOLDER, CHART), encoding="utf-8").read()
        assert 'id="c-%s"' % slug in chart, "no chart row for %s" % slug
    ids = re.findall(r'\sid="([^"]+)"', html)
    assert len(ids) == len(set(ids)), "duplicate ids: %s" % sorted({i for i in ids if ids.count(i) > 1})
    for href in re.findall(r'<nav class="toc">(.*?)</nav>', html, re.S)[0].split('href="#')[1:]:
        assert href.split('"')[0] in ids, "toc target missing: " + href.split('"')[0]
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d maneuver cards, %d drill items)" % (os.path.basename(OUT), len(html) // 1024, html.count('class="mv"'), len(DRILL)))


if __name__ == "__main__":
    main()
