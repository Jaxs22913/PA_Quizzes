#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Physical Diagnosis 2, Exam 2 heart-sound listening guide and quiz.

    python3 tools/build_pd2_heart_sounds.py

Writes into "Physical Diagnosis 2 Exam 2/":
  pd2-exam-2-heart-sound-guide.html   -- every recording with what to listen for (deck facts only)
  heart-sound-quiz.html               -- 18 questions; each is a recording, four choices
  heart-sounds/*.mp3                  -- the excerpts (tools/trim_heart_sounds.py makes them)

Recordings: University of Michigan Heart Sound & Murmur Library (Judge and Mangrulkar, CC BY-SA 3.0).
The guide's skeleton is the Exam 2 study guide's head and tail, so it carries the same design system,
back bar and footer links.
"""
import glob, html as H, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import pd2_heart_sound_pool as P
from render import render

FOLDER = os.path.join(ROOT, "Physical Diagnosis 2 Exam 2")
DONOR = os.path.join(FOLDER, "pd2-exam-2-study-guide.html")
GUIDE = os.path.join(FOLDER, "pd2-exam-2-heart-sound-guide.html")
QUIZ = os.path.join(FOLDER, "heart-sound-quiz.html")
AUDIO = "heart-sounds/"


def slide(*ns):
    return "Slide%s %s" % ("s" if len(ns) > 1 else "", ", ".join(str(n) for n in ns))


# ------------------------------------------------------------------ quiz
def quiz_questions():
    """18 questions, correct answers spread over A-D with no run of three the same."""
    rnd = random.Random(20260929)
    for _ in range(2000):
        pos = [i % 4 for i in range(len(P.POOL))]
        rnd.shuffle(pos)
        if all(not (pos[i] == pos[i + 1] == pos[i + 2]) for i in range(len(pos) - 2)):
            break
    else:
        raise SystemExit("could not spread answer positions")
    out = []
    for (clip, stem, topic, io, sl, ok, ok_x, bad), c in zip(P.POOL, pos):
        opts = [[t, x] for t, x in bad]
        opts.insert(c, [ok, ok_x])
        assert len(opts) == 4
        out.append({"topic": topic, "io": io, "q": stem, "opts": opts, "c": c,
                    "cite": P.slide(sl), "audio": AUDIO + P.CLIPS[clip][0], "alt": P.ALT, "credit": P.CREDIT})
    return out


def build_quiz():
    qs = quiz_questions()
    intro = ("Eighteen recordings from the University of Michigan Heart Sound and Murmur Library, one per question. "
             "<b>Press play, listen through a few beats, then choose.</b> Work in this order, the way the lecture does: "
             "is it in <b>systole</b> (between S1 and S2) or <b>diastole</b> (between S2 and S1)? How long does it last? "
             "Is there an extra sound, and where does it fall? "
             "<b>Low-pitched sounds</b> (S3, S4, the mitral stenosis rumble) belong to the bell; "
             "<b>high-pitched ones</b> (clicks, ejection sounds, opening snaps, regurgitant murmurs) to the diaphragm. "
             "Every choice is explained after you answer, and each question links to the listening guide passage that "
             "teaches it. The recordings are shortened to twenty seconds and credited on each question.")
    html = render(title="Heart Sound and Murmur Listening Quiz &mdash; PD2 Exam 2",
                  h1="Heart Sound and Murmur Listening Quiz",
                  sub="Physical Diagnosis 2 &middot; Exam 2 &middot; Lecture 5",
                  pill="%d questions" % len(qs),
                  chips=["Listening", "Heart sounds", "Murmurs", "Audio"], intro=intro,
                  questions=qs, already_converted=True,
                  navy="#3a5a40", indigo="#5f8a68", gold="#c08a2e", ice="#eef4ef")
    open(QUIZ, "w", encoding="utf-8").write(html)
    print("wrote %s: %d questions, correct positions %s" % (os.path.basename(QUIZ), len(qs),
          "".join("ABCD"[q["c"]] for q in qs)))


# ------------------------------------------------------------------ guide
def player(clip, label=None):
    fn, title, where = P.CLIPS[clip]
    assert os.path.exists(os.path.join(FOLDER, AUDIO + fn)), "missing audio " + fn
    return ('<div class="clip"><p class="clip-title"><b>%s</b> <span class="clip-where">&middot; %s</span></p>'
            '<audio controls preload="none" src="%s%s" aria-label="%s"></audio></div>'
            % (H.escape(label or title), H.escape(where), AUDIO, fn, H.escape(title)))


CSS = """  .clip{margin:10px 0 6px;padding:10px 14px 12px;border:1px solid var(--line);border-left:4px solid var(--accent2);
    border-radius:10px;background:transparent;}
  .clip-title{margin:0 0 6px;font-size:.95rem;}
  .clip-where{color:var(--soft);font-weight:400;font-size:.84rem;}
  .clip audio{width:100%;max-width:480px;height:44px;display:block;}
  header.top h1::before{content:"";display:inline-block;width:.85em;height:.85em;margin-right:.35em;vertical-align:-.05em;
    background:currentColor;-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 18v-6a9 9 0 0 1 18 0v6'/%3E%3Cpath d='M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z'/%3E%3C/svg%3E") center / contain no-repeat;mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M3 18v-6a9 9 0 0 1 18 0v6'/%3E%3Cpath d='M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z'/%3E%3C/svg%3E") center / contain no-repeat;}
  .lib-note{font-size:.84rem;color:var(--soft);margin:2px 0 14px;}
  @media(max-width:700px){main table{display:block;max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;}}
"""

TOC = '''<nav class="toc">
  <h2>Contents</h2>
  <a class="top-link" href="#heartsounds">Heart sound and murmur listening guide</a>
  <a href="#hs-method">1 &middot; How to listen</a>
  <a href="#hs-normal">2 &middot; Normal sounds and splitting of S2</a>
  <a href="#hs-extra">3 &middot; Extra heart sounds</a>
  <a href="#hs-murmurs">4 &middot; Murmurs by timing</a>
  <a href="#hs-combos">5 &middot; Sounds and murmurs together</a>
  <a href="#hs-table">6 &middot; Every recording at a glance</a>
  <a href="#hs-credit">Recordings and licence</a>
</nav>'''

BODY = '''<main>

<section class="deck" id="heartsounds">
  <h2 class="deck-title">Heart Sound and Murmur Listening Guide</h2>
  <p class="lecturer">Lecture 5 &middot; Advanced Cardiovascular &amp; Peripheral Vascular Examination &middot; 22 recordings</p>
  <div class="callout"><p><b>Press play on each recording, and listen for a few beats before reading what follows it.</b>
  Every recording is a twenty-second excerpt from the University of Michigan Heart Sound and Murmur Library, the same
  library whose first recording the lecture plays on slide 36. What each sound <em>is</em> comes from the lecture slides, cited
  to the slide; a few recordings show findings the deck does not teach, and they are marked. The
  <a href="heart-sound-quiz.html">listening quiz</a> asks the recordings the deck does teach, and each question links back here.</p></div>

  <h3 class="sub" id="hs-method">1 &middot; How to listen</h3>
  <p><b>Ask the same questions every time</b> (slide 49): is the murmur during diastole or systole? How long is it? Where is it
  loudest, and does it radiate? Is it crescendo or decrescendo? Are there any extra heart sounds present?</p>
  <p><b>Timing comes first.</b> A systolic murmur falls between S1 and S2 and a diastolic murmur falls between S2 and S1; palpating the
  carotid artery while you listen helps, because systolic sounds coincide with the carotid upstroke (slide 50). Systolic murmurs are
  named by where they sit in systole: midsystolic, pansystolic (holosystolic) or late systolic (slide 51). Diastolic murmurs are early,
  mid or late (slide 52), and they are less common and more difficult to hear than systolic murmurs (slide 76).</p>
  <p><b>Choose the chest piece by pitch</b> (slides 26 and 30). The bell picks up low-pitched sounds and is applied lightly; the diaphragm
  picks up high-pitched sounds (S1, S2, rubs, and the aortic and mitral regurgitation murmurs) and is pressed firmly. Listen in a quiet
  setting, isolate each sound in turn, and close your eyes to focus on it.</p>

  <h3 class="sub" id="hs-normal">2 &middot; Normal sounds and splitting of S2</h3>
  <p><b>S1 and S2</b> (slides 13, 14 and 34). S1, &ldquo;lub&rdquo;, is closure of the mitral and tricuspid valves; it is best heard with the diaphragm
  at the apex, and it precedes the carotid pulse. S2, &ldquo;dub&rdquo;, is closure of the aortic and pulmonic valves; it is best heard with the diaphragm
  at the base, and it follows the carotid pulse. S2 has two components: aortic (A2), usually louder, and pulmonic (P2).</p>
  ''' + player("01") + '''
  <p class="lib-note">This is the recording the lecture itself plays on slide 36. In a normal heart nothing extra sounds in systole or diastole:
  only S1 and S2, repeating.</p>

  <p><b>Physiologic splitting of S2</b> (slides 15 and 35). The two components of S2 are normally fused as one sound during expiration and audibly
  separated during inspiration. When both are heard during inspiration it is normal, and it is called physiologic splitting of S2. A single S2
  is the fused sound of expiration.</p>
  ''' + player("20") + '''
  <p class="lib-note">The split comes and goes with the breathing cycle: separate on inspiration, single on expiration.</p>
  ''' + player("18") + '''
  <p class="lib-note">A single, unsplit S2, as heard when the two components are fused.</p>

  <p><b>Pathologic splitting of S2</b> (slide 35). Splitting that is audible during expiration is pathologic and suggests heart disease.</p>
  ''' + player("19") + '''
  <p class="lib-note">The two components stay separate through the whole breathing cycle instead of fusing on expiration.</p>
  ''' + player("02", "Split S1 (not taught in the deck)") + '''
  <p class="lib-note">Included from the library for completeness. The deck says only that splitting of S1 is usually not present (slide 34), so it is not asked in the quiz.</p>

  <h3 class="sub" id="hs-extra">3 &middot; Extra heart sounds</h3>
  <p><b>Early ejection sounds</b> (slide 38). An early systolic ejection sound occurs shortly after S1, is high in pitch with a sharp clicking quality, and is best heard
  with the diaphragm. It coincides with the sudden pathologic halting of the aortic or pulmonic valve as it opens in early systole, and it indicates
  cardiovascular disease. A pulmonic ejection sound is best heard in the second and third intercostal spaces and decreases with inspiration; its causes include
  dilatation of the pulmonary artery, pulmonary hypertension and pulmonic stenosis. You will hear one with the pulmonic murmur in section 5.</p>

  <p><b>The systolic click</b> (slide 39). A click is usually caused by mitral valve prolapse. It falls in mid to late systole, is usually single but may be more than one,
  is high pitched and is best heard with the diaphragm. It is followed by a late systolic murmur from mitral regurgitation that crescendos up to S2.</p>
  ''' + player("04") + '''

  <p><b>S3, the ventricular gallop</b> (slide 40). S3 is heard after S2, early in diastole, with the cadence Ken-TUC-ky (lub-dub-dee). It is low pitched and best heard with the
  bell at the apex with the patient in the left lateral decubitus position. It is physiologic in children, young adults and the last trimester of pregnancy, and
  pathologic in adults over 40, where it comes from high left ventricular filling pressures; causes include decreased myocardial contractility, heart failure,
  ventricular volume overload from aortic or mitral regurgitation, and left-to-right shunts.</p>
  ''' + player("05") + '''

  <p><b>S4, the atrial gallop</b> (slide 42). S4 is heard just before S1, with the cadence Ten-nes-SEE (dee-lub-dub). It is dull, low pitched and best heard with the bell at the apex
  in the left lateral decubitus position. It is normal in trained athletes and older people; it is more often due to ventricular hypertrophy or fibrosis that makes the
  ventricle stiff, and causes include hypertensive heart disease, aortic stenosis, and ischemic and hypertrophic cardiomyopathy.</p>
  ''' + player("03") + '''

  <p><b>The opening snap</b> (slide 44). An opening snap is a very early diastolic sound caused by abrupt deceleration as a stenotic mitral valve opens. It is high pitched with an obvious snap,
  heard best with the diaphragm just medial to the apex and along the lower left sternal border, and it can be mistaken for the pulmonic component of S2. You will hear
  it with its murmur in section 5.</p>

  <h3 class="sub" id="hs-murmurs">4 &middot; Murmurs by timing</h3>
  <p><b>A murmur</b> is a sound made by turbulent blood flow over a heart valve, and it sounds like a swoosh (slide 46).</p>
  <p><b>Midsystolic murmur</b> (slides 51 and 66&ndash;68). It sits in the middle of systole, between S1 and S2, with a gap on either side; its shape is crescendo-decrescendo, like a diamond.
  Innocent murmurs are midsystolic; the pathologic ones include aortic stenosis, pulmonic stenosis and hypertrophic cardiomyopathy.</p>
  ''' + player("07") + '''
  <p><b>Late systolic murmur</b> (slides 39 and 51). It starts late in systole and builds up to S2; in mitral valve prolapse it follows a mid to late systolic click.</p>
  ''' + player("08") + '''
  <p><b>Holosystolic (pansystolic) murmur</b> (slides 72&ndash;74). It begins immediately with S1 and continues to S2. It is pathologic: blood flows from a chamber of high pressure to one of lower pressure through
  a valve or structure that should be closed. Mitral regurgitation is loudest at the apex and radiates to the left axilla; tricuspid regurgitation is loudest at the lower left sternal border and does not
  reach the axilla.</p>
  ''' + player("09") + '''
  <p class="lib-note">Also in the library: an early systolic murmur, which the deck does not teach and the quiz does not ask.</p>
  ''' + player("06", "Early systolic murmur (not taught in the deck)") + '''

  <p><b>Early diastolic murmur: aortic regurgitation</b> (slides 52 and 77). It is a high-pitched, blowing decrescendo murmur at the aortic area, and it may be mistaken for breath sounds. It is heard best
  with the patient sitting and leaning forward, holding the breath after exhaling. Pulmonic regurgitation is also an early diastolic, high-pitched decrescendo murmur, but it sits at the pulmonic area (slide 78).</p>
  ''' + player("16") + '''
  <p><b>Mid to late diastolic murmur: mitral stenosis</b> (slide 79). It is a low-pitched, decrescendo rumble at the apex, heard with the bell with the patient in the left lateral decubitus position.
  You will hear it after the opening snap in section 5.</p>

  <h3 class="sub" id="hs-combos">5 &middot; Sounds and murmurs together</h3>
  <p><b>Aortic stenosis</b> (slide 67). A harsh midsystolic crescendo-decrescendo murmur at the aortic area that often radiates to the carotids, down the left sternal border and even to the apex.</p>
  ''' + player("15") + '''
  <p class="lib-note">The library labels this recording a systolic murmur with an absent S2; the deck does not mention an absent S2, so the description above is the deck&rsquo;s.</p>
  ''' + player("17", "Systolic and diastolic murmurs (not taught in the deck)") + '''
  <p class="lib-note">A murmur in both phases at the aortic area. The deck teaches the systolic murmur of aortic stenosis and the diastolic murmur of aortic regurgitation separately, so this recording is not asked in the quiz.</p>

  <p><b>Mitral valve prolapse: click, then a late systolic murmur</b> (slide 39). A mid to late systolic click followed by a late systolic murmur from mitral regurgitation that crescendos up to S2.</p>
  ''' + player("10") + '''
  <p><b>S3 with a holosystolic murmur</b> (slides 40 and 74). Ventricular volume overload from mitral regurgitation is one cause of an S3, and mitral regurgitation is a holosystolic murmur, so the two are heard together.</p>
  ''' + player("12") + '''
  <p><b>S4 with a mid-systolic murmur</b> (slides 42 and 67&ndash;70). The dull S4 just before S1 is followed by a murmur in the middle of systole; aortic stenosis and hypertrophic cardiomyopathy are causes of an S4 and are midsystolic murmurs.</p>
  ''' + player("11") + '''
  <p><b>Opening snap with a diastolic murmur: mitral stenosis</b> (slides 44 and 79). The snap of a stenotic mitral valve opening is followed by the low-pitched mid to late diastolic murmur of mitral stenosis, heard with the bell at the apex.</p>
  ''' + player("13") + '''
  <p><b>Ejection sound with a mid-systolic murmur: pulmonic stenosis</b> (slides 38 and 68). A pulmonic ejection sound comes right after S1 and is high pitched; pulmonic stenosis is a midsystolic
  crescendo-decrescendo murmur at the pulmonic area, and it is one cause of the ejection sound.</p>
  ''' + player("23") + '''
  <p><b>Midsystolic murmur with physiologic or pathologic splitting of S2</b> (slides 35 and 66&ndash;68). Listen for two things separately: the murmur sits in the middle of systole, and the split of S2 either
  comes and goes with breathing (physiologic) or stays audible during expiration (pathologic, suggesting heart disease).</p>
  ''' + player("21") + player("22") + '''

  <h3 class="sub" id="hs-table">6 &middot; Every recording at a glance</h3>
  <table>
    <tr><th>Recording</th><th>Where it was recorded</th><th>What to hear</th><th>Slides</th></tr>
    <tr><td>Normal S1 and S2</td><td>Apex, supine</td><td>Two sounds repeating, nothing extra</td><td>13, 14, 34</td></tr>
    <tr><td>Transient split S2</td><td>Pulmonic area</td><td>S2 splits on inspiration and fuses on expiration (physiologic)</td><td>15, 35</td></tr>
    <tr><td>Persistent split S2</td><td>Pulmonic area</td><td>S2 stays split on expiration (pathologic)</td><td>35</td></tr>
    <tr><td>Mid-systolic click</td><td>Apex, supine</td><td>Sharp, high-pitched sound in mid to late systole (mitral valve prolapse)</td><td>39</td></tr>
    <tr><td>S3 gallop</td><td>Apex, left lateral decubitus</td><td>Low-pitched sound after S2 (Ken-TUC-ky)</td><td>40</td></tr>
    <tr><td>S4 gallop</td><td>Apex, left lateral decubitus</td><td>Dull sound just before S1 (Ten-nes-SEE)</td><td>42</td></tr>
    <tr><td>Mid-systolic murmur</td><td>Apex, supine</td><td>Murmur in the middle of systole, gaps at both ends</td><td>51, 66&ndash;68</td></tr>
    <tr><td>Late systolic murmur</td><td>Apex, supine</td><td>Murmur that starts late and builds up to S2</td><td>39, 51</td></tr>
    <tr><td>Holosystolic murmur</td><td>Apex, supine</td><td>Murmur from S1 all the way to S2</td><td>72&ndash;74</td></tr>
    <tr><td>Click, then late systolic murmur</td><td>Apex, left lateral decubitus</td><td>Mitral valve prolapse</td><td>39</td></tr>
    <tr><td>S3 with holosystolic murmur</td><td>Apex, left lateral decubitus</td><td>Volume overload from mitral regurgitation</td><td>40, 74</td></tr>
    <tr><td>S4 with mid-systolic murmur</td><td>Apex, left lateral decubitus</td><td>Dull sound before S1, then a midsystolic murmur</td><td>42, 67&ndash;70</td></tr>
    <tr><td>Opening snap with diastolic murmur</td><td>Apex, left lateral decubitus</td><td>Mitral stenosis</td><td>44, 79</td></tr>
    <tr><td>Systolic murmur, aortic area</td><td>Aortic area, sitting</td><td>Aortic stenosis: harsh, midsystolic, radiates to the carotids</td><td>67</td></tr>
    <tr><td>Early diastolic murmur</td><td>Aortic area, sitting</td><td>Aortic regurgitation: high-pitched, blowing, decrescendo</td><td>77</td></tr>
    <tr><td>Ejection sound with mid-systolic murmur</td><td>Pulmonic area</td><td>Pulmonic stenosis</td><td>38, 68</td></tr>
  </table>

  <h3 class="sub" id="hs-credit">Recordings and licence</h3>
  <p>All recordings are from the <a href="''' + P.LIB_URL + '''" target="_blank" rel="noopener">Heart Sound &amp; Murmur Library</a>, produced by the Learning Resource Center,
  Office of Medical Education, University of Michigan, by <b>Richard D. Judge</b> and <b>Rajesh Mangrulkar</b>, and licensed under
  <a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank" rel="noopener">Creative Commons Attribution-ShareAlike 3.0</a>. Copyright The Regents of the University of Michigan.
  Each recording here is shortened to a twenty-second excerpt (an adaptation), converted to a smaller mp3 and shared under the same licence. The lecture deck embeds the library&rsquo;s first recording on slide 36.</p>

  <footer class="guide-foot">Source: <em>''' + P.DECK + '''</em> (Lauren Reynolds, MSPA, PA-C), Slides 13&ndash;15, 26, 30, 34&ndash;44, 46, 49&ndash;52, 66&ndash;80 and the
  University of Michigan Heart Sound &amp; Murmur Library recordings.</footer>
</section>

<footer class="guide-foot">
  <p style="text-align:center;margin:0 0 10px;"><a href="../index.html" style="color:inherit;font-weight:700;text-decoration:none;">&larr; Back to Homepage</a></p>
  <p style="text-align:center;">Built from your PAJ 5310 lecture decks for personal study &middot; Class of 2028.</p>
  <p style="text-align:center;font-style:italic;">&#9733; <a href="#" style="color:inherit;text-decoration:underline;cursor:pointer" onclick="event.preventDefault(); window.reportMistake()">If you see any mistakes, click here to report it</a> &#9733;</p>
</footer>
'''


def build_guide():
    donor = open(DONOR, encoding="utf-8").read()
    head = donor[:donor.index('<div class="layout wrap"')]
    tail = donor[donor.index("</main>") + len("</main>"):]
    ty0 = tail.index("var TEST_YOURSELF = {")
    ty1 = tail.index("\n  };", ty0) + len("\n  };")
    tail = tail[:ty0] + "var TEST_YOURSELF = {};" + tail[ty1:]
    head = re.sub(r'\s*<link rel="alternate" type="application/vnd\.openxmlformats[^>]*>', "", head)
    head = re.sub(r"<title>.*?</title>", "<title>Physical Diagnosis 2 &middot; Exam 2 &mdash; Heart Sound Listening Guide</title>",
                  head, count=1, flags=re.S)
    head = re.sub(r'<header class="top">.*?</header>',
        '<header class="top">\n'
        '  <h1>Heart Sound &amp; Murmur Listening Guide</h1>\n'
        '  <p>PAJ 5310 Physical Diagnosis II &middot; Class of 2028 &middot; Exam 2 is Friday 20 November</p>\n'
        '  <p>Lecture 5 &middot; 22 recordings from the University of Michigan library, each tied to the lecture slide that teaches it</p>\n'
        '</header>', head, count=1, flags=re.S)
    head = head.replace("</style>", CSS + "</style>", 1)
    html = head + '<div class="layout wrap" data-readable>\n' + TOC + "\n\n" + BODY + tail
    for need in ('class="guide-back-bar"', "window.reportMistake()", "../theme.js", 'data-dark-kind="guide"'):
        assert need in html, "missing chrome: %r" % need
    for bad in ("Exam 2 &mdash; Study Guide</h1>", "TEST_YOURSELF.cardiovascular", "pd2-exam-2-study-guide.docx"):
        assert bad not in html, "donor residue: %r" % bad
    # every recording placed exactly once, every file present
    used = re.findall(r'src="heart-sounds/([^"]+)"', html)
    assert len(used) == len(set(used)) == 22, (len(used), len(set(used)))
    assert set(used) == set(os.path.basename(f) for f in glob.glob(os.path.join(FOLDER, "heart-sounds", "*.mp3")))
    open(GUIDE, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB), %d recordings" % (os.path.basename(GUIDE), len(html) // 1024, len(used)))


if __name__ == "__main__":
    build_guide()
    build_quiz()
