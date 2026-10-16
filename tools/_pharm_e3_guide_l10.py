# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 study guide -- section 2, Lecture 10 (Antiarrhythmic Drugs).

Imported by build_pharm_e3_guide.py.

SOURCES
  Facts   "Antiarrhythmics.pptx" (46 slides; Adam Wood, Pharm.D., DABAT). `python3 tools/pharm_e3_lib.py dump L10`
          prints the slide text. The deck has NO speaker notes. Its pictures are chemical structures (slides 9, 12,
          14, 17, 21, 24, 26, 29, 31, 35, 38, 42: not used) plus six content pictures read by eye into
          tools/pharm_e3/ocr.json under "L10": the sodium channel states (slide 7) and the action potential
          tracings (slides 8, 16, 20, 25, 30; slide 37 repeats slide 25). Those six are shown as figures, each
          cited (slide images are cleared for use when cited).
  Weight  Dr. Wood's live stream of 2026-10-12 (0:00 = start of the stream; the lecture runs to about 52:40, then a
          worked patient case, which is not used). Star boxes quote it with timestamps; a star sets weight and adds
          no fact. Where a star box repeats something he said that is NOT on a slide, it says so.

SLIDES WIN (standing rule, 2026-10-15). The slides are keyed. Where a slide differs from current guidelines, one
short "Current guidelines differ" sentence follows (lidocaine and adenosine for Wolff-Parkinson-White, amiodarone
replacing lidocaine, digoxin with beta blockers or calcium channel blockers). Where the recording and a slide
disagree without an explicit correction (propranolol and glucose; "only lidocaine causes seizures"; "beta blockers do
nothing for ventricular arrhythmias"), the guide prints both and no question turns on the point.

NO DOSES. The magnesium sulfate amount on slide 45 is left out. Half-lives and durations stay (absorption and
elimination, objective 4), as recognition facts.

DESCOPED BY THE LECTURER: channel affinity (open versus inactivated) and dissociation rate (slides 5, 8, 16, 20).
"I don't care about that so much... but you do need to be able to recognize which drugs fit into each of those
three categories" (5:07). Printed for completeness, never asked.

SLIDES NOT COVERED: 1 (title), 2 (the deck's own objectives; the syllabus wording is used), 40 (section list),
46 ("Questions?"). Every other slide is represented.
"""

TOC = '''  <a class="top-link" href="#antiarrhythmics">2 &middot; Antiarrhythmic Drugs</a>
  <a href="#aa-frame">2.1 Objectives 1&ndash;3 &mdash; Principles, the four classes and the indication trend (with a memory aid)</a>
  <a href="#aa-channel">2.2 Objective 2 &mdash; The sodium channel and the action potential</a>
  <a href="#aa-1a">2.3 Objectives 1&ndash;8 &mdash; Class IA: quinidine, procainamide, disopyramide</a>
  <a href="#aa-1b">2.4 Objectives 1&ndash;7 &mdash; Class IB: lidocaine</a>
  <a href="#aa-1c">2.5 Objectives 1&ndash;7 &mdash; Class IC: flecainide, propafenone</a>
  <a href="#aa-2">2.6 Objectives 1&ndash;8 &mdash; Class II: beta blockers</a>
  <a href="#aa-3">2.7 Objectives 1&ndash;8 &mdash; Class III: amiodarone, dofetilide, sotalol</a>
  <a href="#aa-4">2.8 Objectives 1&ndash;7 &mdash; Class IV: verapamil, diltiazem</a>
  <a href="#aa-misc">2.9 Objectives 1&ndash;8 &mdash; Miscellaneous agents: adenosine, digoxin, magnesium sulfate</a>
  <a href="#aa-summary">2.10 Objectives 4 and 8&ndash;10 &mdash; Absorption and elimination, interactions, monitoring and patient education</a>'''


def star(at, quote, takeaway):
    return ('''
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At %s of the recording: <em>&ldquo;%s&rdquo;</em></p>
    <p>%s</p>
  </div>
''' % (at, quote, takeaway))


def fig(src, alt, cap, slide):
    return ('''
  <figure class="fig l10fig"><img src="pharm-e3-images/%s" loading="lazy" alt="%s"><figcaption>%s <span class="cite">Antiarrhythmics.pptx, slide %d</span></figcaption></figure>
''' % (src, alt, cap, slide))


BODY = '''
<style>
  figure.l10fig{margin:14px 0 16px;max-width:600px}
  figure.l10fig img{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:8px;background:#fff}
  figure.l10fig figcaption{font-size:.86rem;line-height:1.45;color:var(--soft);margin-top:6px}
  figure.l10fig .cite{display:block;font-size:.78rem;opacity:.85;margin-top:2px}
</style>
<section class="deck" id="antiarrhythmics">
  <h2 class="deck-title">2 &middot; Antiarrhythmic Drugs</h2>
  <p class="lecturer">Adam Wood, Pharm.D., DABAT</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Identify antiarrhythmic drug classes and commonly prescribed antiarrhythmic drugs.</li>
      <li>Describe the molecular mechanism of action of antiarrhythmic drugs.</li>
      <li>Identify indications for commonly used antiarrhythmic drugs.</li>
      <li>Describe absorption, distribution, metabolism, and excretion of antiarrhythmic drugs.</li>
      <li>Summarize side effects and toxic manifestations of antiarrhythmic drugs.</li>
      <li>Describe adverse effects of antiarrhythmic drugs.</li>
      <li>Identify contraindications for antiarrhythmic drugs.</li>
      <li>Discuss potential drug-drug, drug-food, and drug-herb interactions with antiarrhythmic drugs.</li>
      <li>List commonly used protocols and patient monitoring for antiarrhythmic drugs.</li>
      <li>Outline appropriate patient education for antiarrhythmic drugs.</li>
    </ol>
  </div>

  <div class="callout"><strong>The second of five lectures in Exam 3.</strong> Dr. Wood delivered Lecture 10 live on
  October 12, 2026 and covered the whole deck (46 slides) in about 52 minutes, then walked through a patient case from his
  own practice (not used here: a lecture's worked example is not exam material). Twelve of the deck&rsquo;s pictures are
  chemical structures; the six that carry content (the sodium channel and the action potential tracings) are shown below.</div>

  <div class="callout"><strong>What he stresses, and what he said he will not test.</strong>
  <ul>
    <li><strong>Know which drugs sit in which class.</strong> &ldquo;You do need to be able to recognize which drugs fit into each of those three categories&rdquo; (1A, 1B, 1C; at 5:07). His mnemonic for class IA is <strong>PDQ</strong>: procainamide, disopyramide, quinidine (at 11:08).</li>
    <li><strong>Not the channel affinity.</strong> &ldquo;I&rsquo;m not really going to harp so much on whether it binds to the open over the inactivated. I don&rsquo;t care about that so much&rdquo; (at 5:07), and again for dissociation (at 10:53). Those slide lines are printed below for completeness and are not asked.</li>
    <li><strong>The indication table is for the trend, not for memorizing.</strong> Class II and class IV are for arrhythmias above the ventricles; class I and class III can treat both atrial and ventricular arrhythmias (at 5:55; see 2.1).</li>
    <li><strong>Rate control against rhythm control.</strong> &ldquo;Kind of the difference between which drugs are going to be more of a rate control versus rhythm control&rdquo; (at 30:08). The slides do not use those two words; 2.1 shows where the slides say the same thing in their own words.</li>
    <li><strong>Doses.</strong> Not tested in this course and left out here (the deck gives one, for magnesium sulfate).</li>
    <li><strong>Where a slide differs from current guidelines,</strong> the slide is what you are tested on and a one-line note says how practice differs.</li>
  </ul></div>

  <h3 class="sub" id="aa-frame">2.1 &middot; Objectives 1&ndash;3 &mdash; Principles, the four classes and the indication trend</h3>

  <p><strong>Principles of therapy [slide 3].</strong></p>
  <ul>
    <li><strong>Identify and remove precipitating factors first</strong>: hypoxia, ischemia, electrolytes.</li>
    <li><strong>Establish the goal</strong>: <strong>termination</strong> of an ongoing arrhythmia, or <strong>prevention</strong> of arrhythmia (judged by symptoms, frequency and reproducibility, and structural damage).</li>
    <li><strong>Minimize risk: all antiarrhythmics may induce arrhythmias</strong>, so understand the mechanism.</li>
    <li>The heart&rsquo;s electrophysiology is a <strong>&ldquo;moving target&rdquo;</strong>: ischemia may alter the resting membrane potential, conduction velocity, intracellular calcium and the rate of repolarization.</li>
  </ul>
''' + star("2:01", "Any antiarrhythmic drug may itself induce arrhythmias&hellip; antiarrhythmics themselves, depending on which ones we&rsquo;re using, can be potentially quite dangerous if you don&rsquo;t know what you&rsquo;re doing with them.",
           "<mark class=\"prof-highlight\">Every antiarrhythmic can cause an arrhythmia</mark> [slide 3]; it is the reason class I drugs fell out of favor (2.3 to 2.5).") + '''
  <p><strong>The four ways to classify them [slide 4].</strong></p>
  <table>
    <tr><th>Mechanism</th><th>What it does [slide 4]</th></tr>
    <tr><td><strong>Sodium channel blockers</strong></td><td>Decrease excitability</td></tr>
    <tr><td><strong>Action potential prolongation</strong></td><td>By blocking potassium channels</td></tr>
    <tr><td><strong>Beta receptor blockade</strong></td><td>Prolong atrioventricular refractoriness, prolong conduction, increase the energy required for fibrillation</td></tr>
    <tr><td><strong>Calcium channel blockers</strong></td><td>Decrease the excitability of slow-response cells</td></tr>
  </table>

  <p><strong>The classification (Objective 1) [slide 5].</strong></p>
  <table>
    <tr><th>Class</th><th>What it is [slide 5]</th><th>Drugs in this deck</th></tr>
    <tr><td><strong>Class 1</strong></td><td><strong>Sodium channel blockers</strong>: 1A (open &gt; inactivated), 1B (inactivated &gt; open), 1C (open &gt; inactivated)</td><td><strong>1A:</strong> quinidine, procainamide, disopyramide [slides 9 to 15]<br><strong>1B:</strong> lidocaine [slides 17 to 19]<br><strong>1C:</strong> flecainide, propafenone [slides 21 to 24]</td></tr>
    <tr><td><strong>Class 2</strong></td><td><strong>Beta receptor antagonists</strong></td><td>Propranolol; metoprolol, acebutolol; esmolol [slides 26 to 29]</td></tr>
    <tr><td><strong>Class 3</strong></td><td><strong>Prolong repolarization</strong> (potassium)</td><td>Amiodarone, dofetilide, sotalol [slides 31 to 36]</td></tr>
    <tr><td><strong>Class 4</strong></td><td><strong>Calcium channel blockers</strong></td><td>Verapamil, diltiazem [slides 38 and 39]</td></tr>
    <tr><td><strong>Others</strong></td><td>Adenosine, digitalis</td><td>Adenosine, digoxin, magnesium sulfate [slides 40 to 45]</td></tr>
  </table>
''' + star("5:07", "I&rsquo;m not really going to harp so much on whether it binds to the open over the inactivated. I don&rsquo;t care about that so much. But you do need to be able to recognize which drugs fit into each of those three categories.",
           "Learn <mark class=\"prof-highlight\">which drug is 1A, which is 1B and which is 1C</mark> [slide 5]; the open-or-inactivated preference in brackets is not tested.") + '''
  <p><strong>Indications by class (Objective 3) [slide 6].</strong></p>
  <table>
    <tr><th>Class</th><th>Indications [slide 6]</th></tr>
    <tr><td><strong>1A</strong></td><td>Supraventricular tachycardia, ventricular tachycardia, ventricular fibrillation prevention, and prevention of premature ventricular contractions</td></tr>
    <tr><td><strong>1B</strong></td><td>Ventricular tachycardia, ventricular fibrillation prevention, symptomatic ventricular beats</td></tr>
    <tr><td><strong>1C</strong></td><td><strong>Life-threatening</strong> ventricular tachycardia or fibrillation, <strong>refractory</strong> supraventricular tachycardia</td></tr>
    <tr><td><strong>II</strong></td><td>Supraventricular tachycardia, fibrillation</td></tr>
    <tr><td><strong>III</strong></td><td><strong>Refractory</strong> ventricular tachycardia, atrial fibrillation, flutter, supraventricular tachycardia</td></tr>
    <tr><td><strong>IV</strong></td><td>Supraventricular tachycardia</td></tr>
    <tr><td><strong>Miscellaneous</strong></td><td>Supraventricular tachycardia</td></tr>
  </table>
''' + star("5:55", "This list is not meant to fully memorize&hellip; what I want you to take are sort of the trends. If you look at class two and class four, notice here these are good for treating supraventricular arrhythmias, or things that originate above the ventricles&hellip; They don&rsquo;t really do anything for ventricular arrhythmias&hellip; Class one as a whole and class three, based off how they work, they can treat both atrial arrhythmias and ventricular arrhythmias.",
           "Read slide 6 as a pattern: <mark class=\"prof-highlight\">classes I and III treat both supraventricular and ventricular arrhythmias; classes II and IV (and the miscellaneous agents) are listed for supraventricular ones</mark>. Two slide details sit beside the trend: propranolol&rsquo;s own slide also lists ventricular ectopic beats (he called that use &ldquo;out in the weeds&rdquo;, at 30:54), and verapamil and diltiazem are to be avoided in ventricular arrhythmias [slides 27 and 39].") + '''
  <p><strong>Rate control and rhythm control.</strong> Dr. Wood sorts the drugs by goal: a <strong>rhythm control</strong> drug puts the patient back in, and keeps them in, normal sinus rhythm; a <strong>rate control</strong> drug leaves the atria in their arrhythmia and limits how many beats reach the ventricles. The slides say the same thing in their own words:</p>
  <ul>
    <li><strong>Rhythm:</strong> quinidine &ldquo;maintain rhythm with atrial flutter or fibrillation&rdquo; [slide 10]; dofetilide &ldquo;normal rhythm in atrial fibrillation&rdquo; [slide 34].</li>
    <li><strong>Rate:</strong> beta blockers prolong atrioventricular conduction [slide 25]; verapamil and diltiazem decrease atrioventricular conduction [slide 38]; digoxin &ldquo;slow ventricular rate&rdquo; [slide 44].</li>
    <li>Amiodarone&rsquo;s slide says &ldquo;maintain normal rate in atrial fibrillation&rdquo; [slide 31], although he called amiodarone the rhythm control drug you will see most often (at 36:09). No question here turns on that wording.</li>
  </ul>
''' + star("12:28", "The class ones that we&rsquo;re looking at so far are going to be what we consider rhythm control. That means that they will maintain normal sinus rhythm in a patient as opposed to just preventing the symptoms.",
           "Class I = <mark class=\"prof-highlight\">rhythm control</mark>; the class II beta blockers are his example of <mark class=\"prof-highlight\">rate control</mark> (at 28:36). The words are his, not the slides&rsquo;.") + '''
  <div class="callout"><strong>Memory aid &mdash; the heart as a nightclub.</strong>
  <em>A story to hang the slide facts on. When a question asks for a fact, answer from the facts in this section, not from the story.</em>
  <ul>
    <li><strong>The rooms.</strong> The sinoatrial node is the DJ who sets the beat. The atria are the front room, the
    atrioventricular node is the door to the main room, and the ventricles are the main room, where the real work (pumping) is done.</li>
    <li><strong>Rate control works the door.</strong> <strong>Class II beta blockers are the bouncer</strong> (Dr. Wood&rsquo;s own image, at 29:19):
    he ignores the adrenaline passes (beta receptors), so the pacemaker cells take longer to reach threshold (a flatter phase 4) and fewer
    beats get through to the main room [slides 25 and 26]. <strong>Class IV verapamil and diltiazem are a second bouncer at the same door</strong>,
    working through calcium instead (L-type calcium channels; slower atrioventricular node conduction) [slides 37 and 38].
    <strong>Digoxin turns up the calming music</strong> at the door: more parasympathetic tone, slower atrioventricular conduction, a slower ventricular rate [slides 43 and 44].</li>
    <li><strong>Door staff cannot stop a fight that starts inside the main room.</strong> That is the slide 6 trend: classes II and IV are listed for
    supraventricular arrhythmias, and verapamil and diltiazem are to be avoided in ventricular arrhythmias [slides 6 and 39].</li>
    <li><strong>Rhythm control works on the dancers themselves</strong>, in both rooms. <strong>Class I slows every dancer&rsquo;s first step</strong> (phase 0, the sodium upstroke):
    <strong>IA (&ldquo;PDQ&rdquo;)</strong> slows the first step and makes the whole song longer [slide 8]; <strong>IC</strong> slows the first step the most and works
    on healthy dancers too (&ldquo;affect normal heart&rdquo;) [slide 20]; <strong>IB lidocaine</strong> only goes after dancers in the damaged (ischemic) corner, and makes
    their songs shorter [slides 16 and 18]. <strong>Class III makes every dancer rest longer before the next song</strong> (prolonged repolarization and refractory period) [slide 30].</li>
    <li><strong>Rest too long and the dance floor twists</strong>: torsades de pointes, from class IA, dofetilide and sotalol [slides 11, 13, 15, 34 and 36].
    <strong>Magnesium sulfate</strong> is the one move that untwists it [slide 45].</li>
    <li><strong>Adenosine flips the club&rsquo;s power off for 2 to 3 seconds</strong> and back on (Dr. Wood&rsquo;s &ldquo;turn it off and turn it back on&rdquo;, at 46:41), which can reset a runaway beat from above the ventricles [slides 41 and 42].</li>
  </ul>
  <strong>Where it breaks:</strong> propranolol&rsquo;s slide also lists ventricular ectopic beats (it is &ldquo;membrane stabilizing&rdquo;) [slides 26 and 27];
  amiodarone blocks almost everything (potassium, sodium and calcium channels, alpha and beta receptors) [slide 32]; sotalol and propafenone each straddle two classes [slides 24 and 35];
  and the story says nothing about the toxicities outside the heart (lungs, thyroid, skin and eyes with amiodarone, lupus with procainamide, cinchonism with quinidine).
  For those, use the facts below.</div>
'''

BODY += '''
  <h3 class="sub" id="aa-channel">2.2 &middot; Objective 2 &mdash; The sodium channel and the action potential</h3>

  <p>Slide 7 shows the three states of the cardiac sodium channel. At <strong>rest</strong> the channel is closed and sodium
  cannot enter. When an action potential arrives the channel is <strong>activated</strong>: it opens, sodium rushes in and the
  membrane potential shoots up (phase 0). It then becomes <strong>inactivated</strong>: a gate plugs the inner mouth of the channel
  and no sodium enters while the cell repolarizes, until the channel <strong>recovers</strong> to the resting state [slide 7].
  The time the channels spend inactivated is the refractory period, when another beat cannot start.</p>
''' + fig("l10-slide-07.jpg", "Three panels of a sodium channel in a cell membrane. Resting: the channel is closed and sodium bounces off. Activated: the channel is open and sodium flows in while the membrane potential trace shoots up. Inactivated: a gate plugs the inner mouth of the channel. An arrow labeled Recovery runs from inactivated back to resting.",
          "The sodium channel cycles from <strong>resting</strong> to <strong>activated</strong> (sodium flows in, phase 0) to <strong>inactivated</strong> (plugged while the cell repolarizes) and recovers to resting. Class I drugs act on this channel.", 7) + '''
  <p>The action potential pictures in this deck all follow one convention: the <strong>solid line is the normal action potential</strong>
  and the <strong>dashed line is the action potential with the drug</strong>. Each class changes a different part of the curve; the table
  is the summary, and each class section below shows its own picture.</p>
  <table>
    <tr><th>Class</th><th>Cells it acts on</th><th>What the dashed line shows</th></tr>
    <tr><td><strong>IA</strong> [slide 8]</td><td>Fast-response (working) cells</td><td>Slower, lower phase 0 upstroke; the action potential lasts longer</td></tr>
    <tr><td><strong>IB</strong> [slide 16]</td><td>Fast-response cells, ischemic tissue most</td><td>Same upstroke; repolarization (phase 3) ends sooner, so the action potential is shorter</td></tr>
    <tr><td><strong>IC</strong> [slide 20]</td><td>Fast-response cells, including normal tissue</td><td>Markedly slower phase 0 upstroke</td></tr>
    <tr><td><strong>II</strong> [slide 25]</td><td>Slow-response (pacemaker) cells</td><td>Flatter phase 4, so threshold is reached later and the next beat is delayed</td></tr>
    <tr><td><strong>III</strong> [slide 30]</td><td>Fast-response cells</td><td>Same upstroke; phase 3 repolarization is delayed, so the action potential is longer</td></tr>
    <tr><td><strong>IV</strong> [slide 37]</td><td>Slow-response (pacemaker) cells</td><td>The same picture as class II: a flatter phase 4</td></tr>
  </table>
  <p>Calcium channel blockers &ldquo;decrease slow-response cells excitability&rdquo; [slide 4]; the slow-response cells are the pacemaker
  cells of the sinoatrial and atrioventricular nodes (the recording, at 7:22), which is why classes II and IV act on the nodes.</p>
'''

BODY += '''
  <h3 class="sub" id="aa-1a">2.3 &middot; Objectives 1&ndash;8 &mdash; Class IA: quinidine, procainamide, disopyramide</h3>

  <p><strong>Class IA actions (Objective 2) [slide 8].</strong> <strong>Slow phase 0</strong>, <strong>slow conduction</strong> and
  <strong>prolong the action potential</strong>. (Channel affinity: open &gt; inactivated; dissociation: slow. Not tested.)</p>
''' + fig("l10-slide-08.jpg", "Two overlaid action potentials from -90 millivolts. The dashed one rises more slowly and less high, has a lower plateau, and repolarizes later than the solid one.",
          "<strong>Class IA:</strong> the dashed (drug) line rises more slowly and less high in phase 0 and ends later, so the action potential is <strong>longer</strong>.", 8) + star("11:08", "I like to use the acronym PDQ for my class 1A antiarrhythmics&hellip; those are going to be the three drugs that fit into this category here.",
           "<mark class=\"prof-highlight\">PDQ = procainamide, disopyramide, quinidine</mark>, the three class IA drugs [slides 9 to 15].") + '''
  <h4 class="subsub">Quinidine [slides 9 to 11]</h4>
  <p>Quinidine is the <strong>D-isomer of quinine</strong> (brand names Quinalan, Cardioquin, Quinidex) [slide 9].</p>
  <table>
    <tr><th>Topic</th><th>What the slides give for quinidine</th></tr>
    <tr><td><strong>2 &middot; Direct actions</strong> [slide 9]</td><td>Slows conduction; <strong>prolongs the refractory period</strong>; slows the rate of rise of phase 0; increases the threshold for excitability; decreases automaticity</td></tr>
    <tr><td><strong>2 &middot; Indirect actions</strong> [slide 9]</td><td><strong>Anticholinergic</strong>; <strong>alpha blocker at higher doses</strong></td></tr>
    <tr><td><strong>3 &middot; Indications</strong> [slide 10]</td><td><strong>Maintain rhythm with atrial flutter or fibrillation</strong>; control ventricular tachycardia; conversion of atrial flutter and fibrillation (<strong>very limited use</strong>), with anticoagulants and digitalis listed under it</td></tr>
    <tr><td><strong>8 &middot; Interactions</strong> [slide 10]</td><td><strong>Cytochrome P450 2D6 (CYP2D6) inhibitor</strong> (codeine, morphine)</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Toxicity</strong> [slide 11]</td><td><strong>Nausea, vomiting, diarrhea (30 to 50 percent)</strong>; arrhythmias (ventricular and atrial); hypotension; <strong>thrombocytopenia (may be fatal)</strong>; <strong>cinchonism: tinnitus, dizziness, blurred vision</strong>; <strong>quinidine sudden death</strong>; <strong>torsades de pointes (2 to 8 percent)</strong>; immunological reactions</td></tr>
  </table>
''' + star("14:49", "Quinidine and quinine actually come from the cinchona tree. And so there&rsquo;s this triad of symptoms that you get that is linked to substances that come from the cinchona tree. And so it&rsquo;s called cinchonism, and that includes tinnitus, dizziness, and blurred vision.",
           "<mark class=\"prof-highlight\">Cinchonism (tinnitus, dizziness, blurred vision) points to quinidine</mark> [slide 11].") + star("15:31", "Because we are prolonging the whole action potential, everything from the QRS and the QTc are going to be prolonged. Is that QT prolongation what we care about? Because that can put the patient at risk for torsades, or that twisting of the points.",
           "Class IA <mark class=\"prof-highlight\">prolongs the action potential, and torsades de pointes is the danger</mark> (quinidine 2 to 8 percent) [slides 8 and 11]. The QRS and QT wording is his; the slides show the longer action potential. He added that a second QT-prolonging drug (his example: a macrolide antibiotic) raises the risk further, and that the electrocardiogram is checked against a baseline (at 16:01; not on the slides).") + '''
  <p>The <strong>hypotension</strong> follows from the alpha blockade at higher doses [slides 9 and 11]. Dr. Wood also said the class I
  drugs have <strong>fallen out of favor</strong> because of this toxicity, and that a beta blocker is much &ldquo;cleaner&rdquo; (at 14:05 and 16:34).</p>

  <h4 class="subsub">Procainamide [slides 12 and 13]</h4>
  <p>Procainamide is an <strong>amide derivative of procaine</strong> (brand names Procan, Pronestyl) [slide 12].</p>
  <table>
    <tr><th>Topic</th><th>What the slides give for procainamide</th></tr>
    <tr><td><strong>4 &middot; Duration</strong> [slide 12]</td><td><strong>Short duration of action (3 to 4 hours)</strong>, so there is a <strong>slow-release preparation</strong></td></tr>
    <tr><td><strong>2 &middot; Compared with quinidine</strong> [slide 12]</td><td><strong>Less anticholinergic activity; no alpha-blocking activity</strong></td></tr>
    <tr><td><strong>4 &middot; Metabolism</strong> [slide 12]</td><td><strong>Active acetylated metabolite (N-acetylprocainamide, NAPA)</strong>, which has <strong>class III activity</strong>; <strong>fast acetylators may increase the active metabolite</strong></td></tr>
    <tr><td><strong>5&ndash;6 &middot; Adverse effects</strong> [slide 13]</td><td>Hypotension; slowing of conduction; nausea; <strong>lupus-like syndrome (25 to 50 percent, more often in slow acetylators)</strong>; <strong>torsades de pointes</strong>; <strong>bone marrow suppression (0.2 percent)</strong></td></tr>
    <tr><td><strong>Route</strong> [slide 13]</td><td><strong>Intravenous: better tolerated than quinidine. Oral: poorly tolerated long term</strong></td></tr>
  </table>
''' + star("18:53", "Anytime you see acetylation&hellip; it&rsquo;s probably going to be linked back to this lupus-like syndrome. That&rsquo;s kind of a very notable sort of side effect associated with that.",
           "Acetylation means <mark class=\"prof-highlight\">lupus-like syndrome, more often in slow acetylators</mark> [slide 13]. He linked it to hydralazine from the antihypertensive lecture, which is metabolized the same way (at 18:23).") + '''
  <h4 class="subsub">Disopyramide [slides 14 and 15]</h4>
  <table>
    <tr><th>Topic</th><th>What the slides give for disopyramide (Norpace)</th></tr>
    <tr><td><strong>2 &middot; Actions</strong> [slide 14]</td><td>Effects similar to quinidine; <strong>more anticholinergic actions</strong>; <strong>negative inotropic effects</strong></td></tr>
    <tr><td><strong>3 &middot; Indications</strong> [slide 14]</td><td>Ventricular tachycardia; supraventricular arrhythmias (flutter, fibrillation)</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Toxicity</strong> [slide 15]</td><td>Hypotension; <strong>antimuscarinic effects</strong>; conduction disturbances; <strong>congestive heart failure (decreased contractility)</strong>; torsades de pointes</td></tr>
    <tr><td><strong>7 &middot; Contraindicated</strong> [slide 15]</td><td><strong>Heart block, hypersensitivity, glaucoma</strong></td></tr>
  </table>
  <p>The two contraindications that are not allergy follow from its actions: <strong>glaucoma</strong> from the strong anticholinergic effect, and
  <strong>heart block</strong> from a drug that already causes conduction disturbances [slides 14 and 15]. The negative inotropy is why it can
  bring on <strong>heart failure</strong> [slide 15].</p>

  <div class="pearl"><strong>Telling the three class IA drugs apart.</strong>
  <table>
    <tr><th>Clue in the stem</th><th>Drug</th></tr>
    <tr><td>Tinnitus, dizziness and blurred vision (cinchonism); diarrhea in a third to a half; fatal thrombocytopenia; sudden death; a CYP2D6 inhibitor</td><td><strong>Quinidine</strong> [slides 10 and 11]</td></tr>
    <tr><td>Lupus-like syndrome in a slow acetylator; an active metabolite with class III activity; a 3 to 4 hour duration; least anticholinergic, no alpha block</td><td><strong>Procainamide</strong> [slides 12 and 13]</td></tr>
    <tr><td>The most anticholinergic; contraindicated in glaucoma and heart block; negative inotropy and heart failure</td><td><strong>Disopyramide</strong> [slides 14 and 15]</td></tr>
  </table></div>
'''

BODY += '''
  <h3 class="sub" id="aa-1b">2.4 &middot; Objectives 1&ndash;7 &mdash; Class IB: lidocaine</h3>

  <p><strong>Class IB actions (Objective 2) [slide 16].</strong> <strong>Shorten phase 3</strong> (a shorter action potential) and
  <strong>decrease ectopic foci automaticity</strong>. The channel preference is inactivated &gt; open, with a
  <strong>higher affinity in ischemic tissue and little effect in normal tissue</strong>; dissociation is rapid (under 1 second).
  The ischemic-tissue point is the one to keep; the affinity and dissociation wording is not tested.</p>
''' + fig("l10-slide-16.jpg", "Two overlaid action potentials from -90 millivolts with the same upstroke; the dashed one repolarizes slightly earlier than the solid one.",
          "<strong>Class IB:</strong> the upstroke is unchanged; the dashed (drug) line repolarizes sooner, so the action potential is <strong>shorter</strong>.", 16) + '''
  <table>
    <tr><th>Topic</th><th>What the slides give for lidocaine (Xylocaine)</th></tr>
    <tr><td><strong>3 &middot; Indications</strong> [slide 17]</td><td>Ventricular tachycardia and premature beats; ventricular fibrillation; <strong>acute myocardial infarction</strong>; Wolff-Parkinson-White is also listed</td></tr>
    <tr><td><strong>4 &middot; Route</strong> [slide 18]</td><td><strong>Given intravenously (extensive first-pass metabolism)</strong></td></tr>
    <tr><td><strong>2 &middot; Actions</strong> [slide 18]</td><td>Binds the open or inactivated channel, recovery very rapid; <strong>most effective on sodium channels in ischemic tissue</strong>; less effect on normal tissue; <strong>not effective against atrial arrhythmias</strong></td></tr>
    <tr><td><strong>5&ndash;6 &middot; Toxicity</strong> [slide 19]</td><td><strong>Central nervous system toxicity: drowsiness, confusion, restlessness, muscle twitches, seizures; nystagmus is an early sign of toxicity</strong>; hypersensitivity; increases atrioventricular conduction</td></tr>
    <tr><td><strong>7 &middot; Contraindications</strong> [slide 19]</td><td><strong>Seizures, age</strong></td></tr>
  </table>
  <div class="callout"><strong>Current guidelines differ:</strong> lidocaine is not a recommended treatment for Wolff-Parkinson-White syndrome. The slide lists it, so know that it is on the slide; no question here turns on it.</div>
''' + star("21:16", "Because it has higher affinity in ischemic tissue&hellip; When would I see myocardial ischemic tissue? Probably during a heart attack&hellip; the action potentials in that ischemic tissue, they get longer on their own. So if we could use something like lidocaine to shorten that up, it would help to restore more normal-ish sort of function there.",
           "Lidocaine <mark class=\"prof-highlight\">works where the tissue is ischemic (acute myocardial infarction) and shortens the action potential</mark> [slides 16 to 18].") + star("23:02", "This one has to be given IV because it has really extensive first pass&hellip; also not effective for atrial arrhythmias. This would be relegated to specifically ventricular arrhythmias.",
           "<mark class=\"prof-highlight\">Intravenous only; ventricular arrhythmias only</mark> [slide 18].") + star("23:37", "If we&rsquo;re having too much lidocaine on board it can cause things like drowsiness&hellip; confusion, restlessness, and that can then eventually lead into seizures.",
           "Too much lidocaine shows in the <mark class=\"prof-highlight\">brain first: drowsiness and confusion, then seizures; nystagmus is the early sign</mark> [slide 19]. He also said lidocaine use in cardiac arrest has largely been replaced by a class III drug (amiodarone; at 22:42), and that heart failure or liver disease slows its clearance (at 24:12; not on the slides).") + '''
  <div class="callout"><strong>The recording and the slides on seizures.</strong> At 24:04 Dr. Wood said seizures are a feature of lidocaine that you
  &ldquo;don&rsquo;t really see&rdquo; with the other class I drugs; the flecainide slide also lists seizures [slide 23], and he read that line
  out at 27:05. Both are on slides, so no question here treats seizures as unique to one drug. Nystagmus as the early sign of toxicity is lidocaine&rsquo;s alone [slide 19].</div>
'''

BODY += '''
  <h3 class="sub" id="aa-1c">2.5 &middot; Objectives 1&ndash;7 &mdash; Class IC: flecainide, propafenone</h3>

  <p><strong>Class IC actions (Objective 2) [slide 20].</strong> <strong>Slow phase 0</strong>, <strong>slow conduction</strong>,
  <strong>prolong the refractory period</strong>, and <strong>affect the normal heart</strong> (the opposite of class IB). Channel affinity:
  open &gt; inactivated; dissociation: very slow (not tested).</p>
''' + fig("l10-slide-20.jpg", "Two overlaid action potentials on a scale from -90 to +30 millivolts. The dashed one has a much slower, sloped upstroke and a lower peak, and ends slightly later than the solid one.",
          "<strong>Class IC:</strong> the dashed (drug) line has a <strong>markedly slower phase 0</strong>, the strongest sodium channel effect of the three class I groups.", 20) + '''
  <h4 class="subsub">Flecainide [slides 21 to 23]</h4>
  <table>
    <tr><th>Topic</th><th>What the slides give for flecainide (Tambocor)</th></tr>
    <tr><td><strong>2 &middot; Actions</strong> [slide 21]</td><td><strong>Blocks sodium channels and potassium channels in the ventricles</strong>, slows recovery of the sodium channel; <strong>prolongs the PR, QRS and QT intervals</strong>; prevents premature ventricular contractions</td></tr>
    <tr><td><strong>4 &middot; Kinetics</strong> [slide 21]</td><td><strong>Long half-life (14 hours)</strong>; oral or intravenous</td></tr>
    <tr><td><strong>3 &middot; Indications</strong> [slide 22]</td><td><strong>Life-threatening sustained ventricular arrhythmias</strong>; supraventricular arrhythmias</td></tr>
    <tr><td><strong>7 &middot; Restriction</strong> [slide 22]</td><td><strong>Use only in patients without significant structural damage to the heart</strong></td></tr>
    <tr><td><strong>5&ndash;6 &middot; Toxicity</strong> [slide 23]</td><td>Blurred vision, tremor; <strong>ventricular tachycardia resistant to treatment</strong>; bronchospasm; seizures; thrombocytopenia; <strong>increased mortality in myocardial infarction</strong></td></tr>
  </table>
  <p>The restriction and the mortality line belong together: a drug that <strong>raises mortality after a myocardial infarction</strong> is kept
  for hearts <strong>without significant structural damage</strong> [slides 22 and 23]. <em>Added background (not on the slides): this is
  flecainide&rsquo;s Food and Drug Administration (FDA) boxed warning, from the Cardiac Arrhythmia Suppression Trial.</em></p>

  <h4 class="subsub">Propafenone [slide 24]</h4>
  <p>Propafenone has the <strong>same mechanism as flecainide plus beta-blocking activity</strong> [slide 24]. Its toxicity:
  <strong>proarrhythmic</strong>; dizziness, blurred vision, <strong>bradycardia</strong>; <strong>bronchospasm</strong> and beta-adrenergic blockade;
  <strong>agranulocytosis, anemia, thrombocytopenia</strong>; it can <strong>worsen heart failure</strong> [slide 24]. The bradycardia,
  bronchospasm and worse heart failure are the beta-blocker part.</p>
''' + star("26:38", "The downside to doing that was we actually found we end up causing a bunch of arrhythmias to occur, and that has led to patients dying basically, and so that&rsquo;s why we&rsquo;ve kind of moved over to the relatively safer form of rate control.",
           "Class IC <mark class=\"prof-highlight\">can cause the very arrhythmias it treats, and raises mortality after a myocardial infarction</mark> [slides 23 and 24]. He also said both drugs are older and now used mainly in specialty cases (at 24:49).") + '''
  <div class="pearl"><strong>Class I side by side.</strong>
  <table>
    <tr><th></th><th>IA</th><th>IB</th><th>IC</th></tr>
    <tr><td><strong>Phase 0</strong></td><td>Slowed [slide 8]</td><td>Unchanged; phase 3 shortened [slide 16]</td><td>Slowed the most [slides 20 and the picture]</td></tr>
    <tr><td><strong>Action potential</strong></td><td>Prolonged [slide 8]</td><td>Shortened [slide 16]</td><td>Refractory period prolonged [slide 20]</td></tr>
    <tr><td><strong>Where it works</strong></td><td>Both supraventricular and ventricular [slide 6]</td><td>Ischemic tissue; ventricular only [slides 16 and 18]</td><td>Normal heart too; life-threatening or refractory cases [slides 6 and 20]</td></tr>
    <tr><td><strong>Drugs</strong></td><td>Quinidine, procainamide, disopyramide</td><td>Lidocaine</td><td>Flecainide, propafenone</td></tr>
  </table></div>
'''

BODY += '''
  <h3 class="sub" id="aa-2">2.6 &middot; Objectives 1&ndash;8 &mdash; Class II: beta blockers</h3>

  <p><strong>Class II actions (Objective 2) [slide 25].</strong> <strong>Slow conduction</strong>, <strong>decrease automaticity</strong>,
  <strong>prolong atrioventricular conduction</strong>, <strong>decrease phase 4 depolarization</strong>.</p>
''' + fig("l10-slide-25.jpg", "Pacemaker cell action potentials from about -70 to +10 millivolts. The solid line rises through phase 4 to fire a second beat; the dashed line's phase 4 slope is flatter, so its second beat comes much later.",
          "<strong>Class II</strong> (and class IV, slide 37 repeats this picture): in a pacemaker cell the dashed (drug) line has a <strong>flatter phase 4</strong>, so threshold is reached later and the next beat is delayed.", 25) + star("29:19", "The beta blocker serving as sort of like a bouncer, right? So they only want to let so many people into the club at a steady rate, and this prevents any of the other riff-raff from getting in.",
           "Beta blockers are <mark class=\"prof-highlight\">rate control at the atrioventricular node</mark>: in atrial fibrillation they limit how many beats reach the ventricles [slides 25 and 26]. He said the class IV calcium channel blockers do &ldquo;almost identically the same thing&rdquo; through calcium (at 29:34).") + '''
  <h4 class="subsub">Propranolol [slides 26 to 28]</h4>
  <table>
    <tr><th>Topic</th><th>What the slides give for propranolol (Inderal, Betachron)</th></tr>
    <tr><td><strong>1&ndash;2 &middot; Class and actions</strong> [slide 26]</td><td><strong>Nonselective beta blocker</strong>; reduces phase 4 activation; <strong>slows atrioventricular conduction</strong>; <strong>negative inotropic and chronotropic effects</strong>; suppresses premature ventricular beats; membrane stabilizing</td></tr>
    <tr><td><strong>3 &middot; Indications</strong> [slide 27]</td><td><strong>Supraventricular arrhythmias</strong>; ventricular ectopic beats; <strong>myocardial infarction</strong></td></tr>
    <tr><td><strong>5&ndash;6 &middot; Toxicity</strong> [slide 28]</td><td><strong>Heart failure</strong>; <strong>heart block</strong>; hypotension; hyperglycemia (see the box below); <strong>bronchospasm</strong>; digitalis toxicity</td></tr>
  </table>
''' + star("31:28", "Remember, propranolol is a nonselective beta blocker. It&rsquo;ll affect both beta 1 and beta 2 equally. So if you have someone with asthma, they may have those beta 2 receptors blocked up and they may cause bronchospasm.",
           "<mark class=\"prof-highlight\">Nonselective, so bronchospasm in asthma</mark> [slides 26 and 28]; choose a beta-1 selective agent instead [slide 29].") + '''
  <div class="callout"><strong>The recording and the slide on blood sugar.</strong> Slide 28 lists <strong>hyperglycemia</strong> for propranolol.
  In the recording (at 31:41) Dr. Wood read it as a blood sugar effect and added that beta blockers can <strong>mask the warning signs of
  hypoglycemia</strong> (low blood sugar); he did not say the slide was wrong. Our two transcripts disagree on whether he said hyperglycemia or
  hypoglycemia, and beta blockers can push glucose either way, so no question here turns on the direction.</div>

  <h4 class="subsub">Metoprolol, acebutolol and esmolol [slide 29]</h4>
  <p>Metoprolol and acebutolol (Lopressor, Sectral) are <strong>beta-1 selective</strong> blockers, <strong>similar to propranolol</strong> but with
  <strong>less bronchospasm</strong>. They can still cause <strong>congestive heart failure</strong> and <strong>central nervous system sedation and
  fatigue</strong>. <strong>Esmolol is the intravenous, short-acting</strong> beta blocker [slide 29].</p>
''' + star("32:26", "Metoprolol and acebutolol, examples of beta 1 selective beta blockers, definitely better for patients who have like reactive airway disease or asthma. I would certainly recommend something like this over propranolol if that&rsquo;s the case.",
           "<mark class=\"prof-highlight\">Asthma: a beta-1 selective agent over propranolol</mark> [slide 29]. He added that esmolol is easy to titrate up or down in the emergency room or intensive care unit because it is so short-acting (at 32:51), and that any beta blocker from earlier lectures is fair game (at 32:04).") + '''
  <p><strong>Interactions (Objective 8).</strong> Propranolol&rsquo;s toxicity list includes <strong>digitalis toxicity</strong> [slide 28], and
  the digoxin slide says to avoid beta blockers with it [slide 44].</p>
'''

BODY += '''
  <h3 class="sub" id="aa-3">2.7 &middot; Objectives 1&ndash;8 &mdash; Class III: amiodarone, dofetilide, sotalol</h3>

  <p><strong>Class III actions (Objective 2) [slide 30].</strong> Potassium channel blockers that <strong>prolong repolarization</strong>:
  they <strong>reduce potassium efflux</strong>, <strong>prolong phase 3 repolarization</strong>, <strong>prolong the refractory period</strong>
  and <strong>prolong the duration of the action potential</strong>.</p>
''' + fig("l10-slide-30.jpg", "Two overlaid action potentials from -90 millivolts with the same upstroke and plateau; the dashed one repolarizes much later.",
          "<strong>Class III:</strong> the upstroke is unchanged; the dashed (drug) line repolarizes much later (<strong>prolonged phase 3</strong>), so the action potential and refractory period are longer.", 30) + star("33:41", "If we block that potassium efflux, it&rsquo;s going to be prolonging the repolarization. The refractory period does get longer.",
           "Class III = <mark class=\"prof-highlight\">block potassium efflux, prolong repolarization and the refractory period</mark> [slide 30]. He added that on the electrocardiogram the QT interval is the one most affected (at 33:51; not on the slides).") + '''
  <h4 class="subsub">Amiodarone [slides 31 to 33]</h4>
  <table>
    <tr><th>Topic</th><th>What the slides give for amiodarone (Cordarone, Pacerone)</th></tr>
    <tr><td><strong>1 &middot; What it is</strong> [slide 31]</td><td>Oral and intravenous; <strong>an analog of thyroid hormone</strong></td></tr>
    <tr><td><strong>4 &middot; Kinetics</strong> [slide 31]</td><td><strong>Half-life 40 days (26 to 107)</strong>: slow onset, slow elimination; <strong>may require loading doses</strong></td></tr>
    <tr><td><strong>3 &middot; Indications</strong> [slide 31]</td><td><strong>Recurrent ventricular tachycardia or fibrillation resistant to other drugs</strong>; maintain normal rate in atrial fibrillation; <strong>intravenous: terminates acute ventricular tachycardia or fibrillation, replacing lidocaine in myocardial infarction</strong></td></tr>
    <tr><td><strong>2 &middot; Actions</strong> [slide 32]</td><td><strong>Blocks potassium channels, inactivated sodium channels, calcium channels, and alpha and beta receptors</strong>; decreases automaticity; decreases conduction; prolongs refractory periods</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Toxicity</strong> [slide 33]</td><td>Hypotension; <strong>pneumonitis, pulmonary fibrosis (potentially fatal)</strong>; neurotoxicity, neuropathy, muscle weakness, ataxia; <strong>blue-gray skin color, photosensitivity</strong>; <strong>corneal deposits</strong>; <strong>thyroid abnormalities (hyper or hypo)</strong>; <strong>hepatic dysfunction</strong></td></tr>
    <tr><td><strong>8 &middot; Interactions</strong> [slide 33]</td><td><strong>Increases digoxin, warfarin, flecainide, phenytoin and procainamide</strong></td></tr>
  </table>
  <div class="callout"><strong>Current guidelines differ:</strong> resuscitation guidance lists amiodarone or lidocaine as options for shock-refractory ventricular fibrillation or pulseless ventricular tachycardia; the slide says amiodarone has replaced lidocaine [slide 31].</div>
''' + star("36:09", "Amio is probably the one you&rsquo;re going to see most frequently, especially in the hospital&hellip; And interestingly, it&rsquo;s an analog of thyroid hormone. That&rsquo;ll come in up later when we get into some side effects here.",
           "Amiodarone is <mark class=\"prof-highlight\">the analog of thyroid hormone, so thyroid abnormalities (hyper or hypo)</mark> [slides 31 and 33].") + star("36:42", "The drug is notable because it has a really, really long half-life, like on average about 40 days&hellip; very slow elimination&hellip; That&rsquo;s why we use loading doses.",
           "<mark class=\"prof-highlight\">A half-life of about 40 days is why amiodarone needs loading doses</mark> [slide 31]. In answer to a question he added that stopping it brings no withdrawal: the level simply trails off over weeks (at 40:30).") + star("39:05", "If patients are on this chronically, this is where some of the stuff more pops up. So things like pulmonary fibrosis or pneumonitis over time, neurotoxicity, you can see this kind of blue-gray skin discoloration&hellip; corneal issues, thyroid problems, both hyper or hypo&hellip; hepatic issues, and then just a ton of drug interactions.",
           "Amiodarone&rsquo;s <mark class=\"prof-highlight\">lungs, skin, eyes, thyroid and liver</mark>, plus its interactions [slide 33]. He mentioned checking vision and lung function over time on long-term therapy (at 39:52; not on the slides). <em>Added background (not on the slides): the pulmonary and hepatic toxicity are part of amiodarone&rsquo;s FDA boxed warning.</em>") + '''
  <h4 class="subsub">Dofetilide [slide 34]</h4>
  <p>Dofetilide (Tikosyn) is a <strong>potent pure potassium channel blocker</strong>. Indication: <strong>normal rhythm in atrial fibrillation</strong>.
  <strong>Limited availability to those with special training.</strong> Adverse effects: <strong>torsades de pointes (1 to 3 percent)</strong> and
  <strong>marked QT prolongation</strong>. It is <strong>mainly eliminated unchanged by the kidneys</strong> [slide 34].</p>
''' + star("42:53", "Torsades is really the biggest risk here because this can purely just be blocking the potassium to prolong the QT. And so this is actually so potentially dangerous, you have to start this, like, in the hospital.",
           "Dofetilide&rsquo;s danger is <mark class=\"prof-highlight\">torsades de pointes from pure potassium block and marked QT prolongation</mark> [slide 34]. Starting it in hospital with electrocardiograms, electrolytes and kidney function checked is from the recording (at 43:08), not the slide; the slide says prescribing is limited to those with special training. <em>Added background (not on the slides): that in-hospital start is dofetilide&rsquo;s FDA boxed warning.</em>") + '''
  <h4 class="subsub">Sotalol [slides 35 and 36]</h4>
  <p>Sotalol (Betapace) has <strong>beta-blocking activity</strong>, <strong>inhibits potassium channels</strong> and decreases phase 4
  depolarization [slide 35]; it increases action potential duration and decreases atrioventricular node conduction [slide 36].
  Indications: <strong>atrial flutter and fibrillation, ventricular tachyarrhythmia</strong> [slide 35]. Toxicity: <strong>torsades de pointes</strong>,
  <strong>bronchospasm</strong>, beta-blocking effects [slide 36].</p>
''' + star("44:09", "If you see sotalol, you&rsquo;re like, wait a second, that ends &lsquo;-lol&rsquo;. That should be a beta blocker&hellip; Well, it actually turns out sotalol is kind of a unique beta blocker because it&rsquo;s a nonselective beta blocker, but it also can block some potassium channel efflux. So you get both a class 2 and a class 3 effect here.",
           "<mark class=\"prof-highlight\">Sotalol = class II plus class III</mark>: a beta blocker that also blocks potassium channels, so it brings both torsades and bronchospasm [slides 35 and 36].") + '''
  <div class="pearl"><strong>Telling the three class III drugs apart.</strong>
  <table>
    <tr><th>Clue in the stem</th><th>Drug</th></tr>
    <tr><td>Blocks almost everything; thyroid hormone analog; 40-day half-life and loading doses; lungs, thyroid, blue-gray skin, corneal deposits, liver; raises digoxin and warfarin</td><td><strong>Amiodarone</strong> [slides 31 to 33]</td></tr>
    <tr><td>Pure potassium channel blocker; atrial fibrillation only; special training to prescribe; eliminated unchanged by the kidneys; torsades and marked QT prolongation</td><td><strong>Dofetilide</strong> [slide 34]</td></tr>
    <tr><td>A beta blocker that also blocks potassium channels; torsades plus bronchospasm</td><td><strong>Sotalol</strong> [slides 35 and 36]</td></tr>
  </table></div>
'''

BODY += '''
  <h3 class="sub" id="aa-4">2.8 &middot; Objectives 1&ndash;7 &mdash; Class IV: verapamil, diltiazem</h3>

  <p><strong>Class IV actions (Objective 2) [slide 37].</strong> <strong>Decrease automaticity</strong>, <strong>block the L-type calcium channel</strong>,
  <strong>slow atrioventricular node conduction</strong>, <strong>negative inotropic</strong>. Slide 37 repeats the class II picture: a flatter
  phase 4 in pacemaker cells.</p>
  <table>
    <tr><th>Topic</th><th>What the slides give for verapamil and diltiazem (Calan, Cardizem)</th></tr>
    <tr><td><strong>2 &middot; Actions</strong> [slide 38]</td><td>Block both activated and inactivated channels; <strong>most effective in the most active tissue</strong>; <strong>decrease atrioventricular conduction</strong>; <strong>suppress the sinoatrial node</strong></td></tr>
    <tr><td><strong>3 &middot; Indications</strong> [slide 39]</td><td><strong>Paroxysmal supraventricular tachycardia</strong>; atrial fibrillation</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Toxicity</strong> [slide 39]</td><td><strong>Hypotension, edema</strong></td></tr>
    <tr><td><strong>4 &middot; Metabolism</strong> [slide 39]</td><td><strong>Hepatic metabolism: caution in liver damage</strong></td></tr>
    <tr><td><strong>7 &middot; Avoid</strong> [slide 39]</td><td><strong>Ventricular arrhythmias, sick sinus syndrome, depressed cardiac function</strong></td></tr>
  </table>
  <p>Each &ldquo;avoid&rdquo; follows from the actions: a drug that acts at the nodes does nothing for an arrhythmia that starts in the
  ventricles; one that suppresses the sinoatrial node is dangerous when that node is already sick; and a negative inotrope can push a weak
  heart into failure [slides 37 to 39].</p>
''' + star("45:15", "You&rsquo;re going to see class 4 and class 2, they look really, really similar in terms of their overall actions and how they work on supraventricular arrhythmias. They don&rsquo;t work on ventricular arrhythmias, as it turns out.",
           "Class IV works like class II: <mark class=\"prof-highlight\">supraventricular arrhythmias only; avoid in ventricular arrhythmias</mark> [slides 37 to 39]. He added that these are the nondihydropyridine calcium channel blockers and that they inhibit cytochrome P450 3A4, which brings drug interactions (at 4:33 and 45:53 and 45:54; not on these slides).") + '''

  <h3 class="sub" id="aa-misc">2.9 &middot; Objectives 1&ndash;8 &mdash; Miscellaneous agents: adenosine, digoxin, magnesium sulfate</h3>

  <h4 class="subsub">Adenosine [slides 41 and 42]</h4>
  <table>
    <tr><th>Topic</th><th>What the slides give for adenosine</th></tr>
    <tr><td><strong>2 &middot; Actions</strong> [slide 41]</td><td><strong>Activates potassium channels in the atria and blocks calcium channels</strong>; <strong>hyperpolarizes cells</strong>; decreases conduction velocity and <strong>may stop the heart for 2 to 3 seconds</strong>; decreases automaticity; prolongs the refractory period</td></tr>
    <tr><td><strong>4 &middot; Half-life</strong> [slide 41]</td><td><strong>About 10 seconds</strong></td></tr>
    <tr><td><strong>3 &middot; Indications</strong> [slide 42]</td><td><strong>Paroxysmal supraventricular tachycardia</strong>; Wolff-Parkinson-White is also listed</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Toxicity</strong> [slide 42]</td><td><strong>Flushing (20 percent)</strong>; shortness of breath; burning in the chest</td></tr>
  </table>
  <div class="callout"><strong>Current guidelines differ:</strong> adenosine can end the reentrant tachycardia of Wolff-Parkinson-White, but it is avoided when the syndrome presents as pre-excited atrial fibrillation.</div>
''' + star("46:40", "Imagine if your computer starts going on the fritz. What do you do? You turn it off and you turn it back on again&hellip; This is what adenosine does, but for the heart. It causes a rapid hyperpolarization of the cells. And if you&rsquo;re checking a continuous EKG, you will actually see your patient flatline for just a couple seconds.",
           "<mark class=\"prof-highlight\">Adenosine hyperpolarizes the cells and may stop the heart for 2 to 3 seconds, then the heart restarts, often in normal sinus rhythm</mark> [slide 41]; its use is paroxysmal supraventricular tachycardia [slide 42]. Because the half-life is so short, he described giving it as a rapid push followed at once by a saline flush (at 48:52; not on the slides).") + '''
  <h4 class="subsub">Digoxin (digitalis) [slides 43 and 44]</h4>
  <table>
    <tr><th>Topic</th><th>What the slides give for digoxin as an antiarrhythmic</th></tr>
    <tr><td><strong>2 &middot; Actions</strong> [slide 43]</td><td><strong>Sodium-potassium ATPase inhibition</strong>; <strong>slows atrioventricular conduction</strong>; inhibits calcium channels in the atrioventricular node; <strong>indirectly increases parasympathetic tone and decreases sympathetic tone</strong>; <strong>can induce heart block</strong></td></tr>
    <tr><td><strong>3 &middot; Indications</strong> [slide 44]</td><td><strong>Slow the ventricular rate</strong>; induce heart block (atrial flutter, fibrillation)</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Toxicity</strong> [slide 44]</td><td>Nausea, vomiting, diarrhea, anorexia; central nervous system: confusion, delirium, headache, seizures, visual disturbances</td></tr>
    <tr><td><strong>8 &middot; Avoid</strong> [slide 44]</td><td><strong>Calcium channel blockers and beta blockers</strong></td></tr>
  </table>
  <div class="callout"><strong>Current guidelines differ:</strong> digoxin is often combined with a beta blocker or a nondihydropyridine calcium channel blocker for rate control in atrial fibrillation, with the heart rate watched for excessive slowing.</div>
''' + star("51:30", "Then of course we avoid calcium channel blockers and beta blockers at the same time, just because they would both synergize in terms of decreasing heart rate, which may be causing greater degrees of heart block. Not recommended.",
           "<mark class=\"prof-highlight\">Digoxin plus a beta blocker or calcium channel blocker: additive slowing and heart block</mark> [slides 43 and 44]. He reminded the class that digoxin needs drug level monitoring and that its visual clue is yellow-green halos (at 51:15; both from Lecture 9, see section 1).") + '''
  <h4 class="subsub">Magnesium sulfate [slide 45]</h4>
  <p>Indication: <strong>torsades de pointes</strong>, given <strong>intravenously</strong>. Toxicity: <strong>bradycardia, flushing, headache,
  respiratory paralysis</strong> [slide 45]. (The dose on the slide is not tested.)</p>
''' + star("52:00", "This is a great pimping question from preceptors: what&rsquo;s a treatment of choice for torsades? It&rsquo;s always magnesium sulfate.",
           "<mark class=\"prof-highlight\">Torsades de pointes &rarr; intravenous magnesium sulfate</mark> [slide 45]. Torsades is the danger of the drugs that lengthen repolarization: quinidine, procainamide, disopyramide, dofetilide and sotalol [slides 11, 13, 15, 34 and 36].") + '''
'''

BODY += '''
  <h3 class="sub" id="aa-summary">2.10 &middot; Objectives 4 and 8&ndash;10 &mdash; Absorption and elimination, interactions, monitoring and patient education</h3>

  <h4 class="subsub">Absorption, distribution, metabolism and excretion (Objective 4)</h4>
  <table>
    <tr><th>Drug</th><th>What the slides give</th></tr>
    <tr><td><strong>Procainamide</strong></td><td>Short duration (3 to 4 hours), slow-release preparation; acetylated to an active metabolite (N-acetylprocainamide) with class III activity; fast acetylators make more of it; slow acetylators get the lupus-like syndrome more often [slides 12 and 13]</td></tr>
    <tr><td><strong>Lidocaine</strong></td><td>Intravenous, because of extensive first-pass metabolism [slide 18]</td></tr>
    <tr><td><strong>Flecainide</strong></td><td>Long half-life (14 hours); oral or intravenous [slide 21]</td></tr>
    <tr><td><strong>Esmolol</strong></td><td>Intravenous, short-acting [slide 29]</td></tr>
    <tr><td><strong>Amiodarone</strong></td><td>Oral and intravenous; half-life 40 days (26 to 107); slow onset and slow elimination; may need loading doses [slide 31]</td></tr>
    <tr><td><strong>Dofetilide</strong></td><td>Mainly eliminated unchanged by the kidneys [slide 34]</td></tr>
    <tr><td><strong>Verapamil, diltiazem</strong></td><td>Hepatic metabolism, caution in liver damage [slide 39]</td></tr>
    <tr><td><strong>Adenosine</strong></td><td>Half-life about 10 seconds [slide 41]</td></tr>
  </table>

  <h4 class="subsub">Interactions (Objective 8)</h4>
  <table>
    <tr><th>Combination</th><th>What happens</th></tr>
    <tr><td><strong>Quinidine with codeine or morphine</strong></td><td>Quinidine is a cytochrome P450 2D6 (CYP2D6) inhibitor [slide 10]</td></tr>
    <tr><td><strong>Amiodarone with digoxin, warfarin, flecainide, phenytoin or procainamide</strong></td><td>Amiodarone increases each of them [slide 33]</td></tr>
    <tr><td><strong>Propranolol with digoxin</strong></td><td>Digitalis toxicity is on propranolol&rsquo;s list [slide 28]</td></tr>
    <tr><td><strong>Digoxin with a beta blocker or calcium channel blocker</strong></td><td>Avoid: added slowing of atrioventricular conduction and heart block [slides 43 and 44]</td></tr>
  </table>
  <p>The slides name <strong>no drug-food or drug-herb interactions</strong> for these drugs.</p>

  <h4 class="subsub">Protocols and monitoring (Objective 9)</h4>
  <ul>
    <li><strong>Before any antiarrhythmic:</strong> identify and remove precipitating factors (hypoxia, ischemia, electrolytes) and set the goal (terminate or prevent) [slide 3].</li>
    <li><strong>Torsades de pointes</strong> is the thing to watch for with class IA, dofetilide and sotalol; magnesium sulfate treats it [slides 11, 13, 15, 34, 36 and 45].</li>
    <li><strong>Lidocaine:</strong> watch for nystagmus, the early sign of toxicity [slide 19].</li>
    <li><strong>Amiodarone:</strong> loading doses because of the 40-day half-life [slide 31]; watch the lungs, thyroid, liver, skin and eyes [slide 33].</li>
    <li><strong>Dofetilide:</strong> limited to prescribers with special training; marked QT prolongation; renal elimination [slide 34].</li>
    <li><strong>Procainamide:</strong> blood counts (bone marrow suppression) and the lupus-like syndrome [slide 13].</li>
    <li><strong>Adenosine:</strong> the heart may pause for 2 to 3 seconds [slide 41].</li>
  </ul>

  <h4 class="subsub">Patient education (Objective 10)</h4>
  <ul>
    <li><strong>Quinidine:</strong> diarrhea and nausea are common; report ringing in the ears, dizziness or blurred vision [slide 11].</li>
    <li><strong>Procainamide:</strong> a lupus-like syndrome is common, more so in slow acetylators [slide 13].</li>
    <li><strong>Disopyramide:</strong> anticholinergic (antimuscarinic) effects; not for people with glaucoma [slide 15].</li>
    <li><strong>Propranolol and sotalol:</strong> report wheezing or breathlessness (bronchospasm) [slides 28 and 36]; metoprolol and acebutolol cause less bronchospasm but can cause tiredness and sedation [slide 29].</li>
    <li><strong>Amiodarone:</strong> sun sensitivity and a blue-gray skin color, eye deposits, thyroid changes, and cough or breathlessness (pneumonitis) [slide 33].</li>
    <li><strong>Verapamil and diltiazem:</strong> ankle swelling (edema) and low blood pressure [slide 39].</li>
    <li><strong>Adenosine:</strong> brief flushing, shortness of breath and chest burning; the heart may pause for 2 to 3 seconds [slides 41 and 42].</li>
    <li><strong>Digoxin:</strong> report nausea, loss of appetite, confusion or visual disturbances [slide 44].</li>
  </ul>

  <div class="callout"><strong>What is left out of this section, and why.</strong>
  <ul>
    <li><strong>Doses.</strong> Not tested in this course; the magnesium sulfate amount on slide 45 is omitted.</li>
    <li><strong>Channel affinity and dissociation</strong> (slides 5, 8, 16, 20): printed for completeness; Dr. Wood said he will not test them.</li>
    <li><strong>Where a slide differs from current guidelines,</strong> a one-line note says so: lidocaine and adenosine for Wolff-Parkinson-White (slides 17 and 42), amiodarone replacing lidocaine (slide 31), and digoxin with beta blockers or calcium channel blockers (slide 44).</li>
    <li><strong>Where the recording and a slide disagree</strong> without an explicit correction (propranolol and blood sugar, slide 28; seizures as a lidocaine-only effect, slides 19 and 23; beta blockers and ventricular beats, slides 6 and 27), both are printed and no question turns on the point.</li>
    <li><strong>Boxed warnings.</strong> The slides never use the words; the guide flags in italics where a slide fact is also a Food and Drug Administration boxed warning (flecainide, amiodarone, dofetilide). The side-effects page shades every such row.</li>
    <li><strong>Slides not represented:</strong> 1 (title), 2 (the deck&rsquo;s own objectives), 40 (the list of miscellaneous agents) and 46 (&ldquo;Questions?&rdquo;); the twelve chemical-structure pictures.</li>
  </ul></div>

</section>
'''
