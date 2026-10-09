#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write the PDM I Exam 3 guide FRAGMENTS for Lecture 11 and Lecture 12.

    tools/pdm_e3/l11_guide.html   section 11, Rhythm Analysis and Sinus Rhythms
    tools/pdm_e3/l12_guide.html   section 12, Ectopy, Escape Rhythms and Supraventricular Dysrhythmias

The Exam 3 guide page itself is built by the assembler; these are drop-in <section class="deck">
blocks in the Exam 2 guide's markup (io-box, prof-flag, h3.sub, figure.fig, callout, pearl,
mark.prof-highlight); the assembler builds the TOC from the h3.sub ids.

Rules carried in:
  * Instructional Objectives are VERBATIM from the syllabus (PDM.pdf, Topic Outline 11 and 12),
    lettered a-i and a-h, and each is answered in order (guide_verbatim_io_rule).
  * Lecturer: Scott Mathis, EMS educator, First Response Training Group, from both decks' title
    slides; the recording's speaker calls Professor Elwaya "your professor", so the guest is the
    speaker. The calendar's "Professor Elwaya" is the scheduled name only.
  * Emphasis quotes are from the 5 October recording and appear in BOTH transcripts (the local
    faster-whisper run and Notability's own); times are clip and minute.
  * Every fact is from the deck; where the deck and the truth disagree the truth is taught and the
    slide's wording is noted (truth_wins_on_conflict).
  * Rhythm strips: the guide NAMES the rhythm in the caption and points at the defining features,
    using the labeled versions of the strips (extract_pdm_l11_figures.py / _l12_).
"""
import os, re
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DIR = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 3")
IMG = "pdm-exam-3-study-guide-images"
OUT = os.path.join(HERE, "pdm_e3")
D11 = "11. Rhythm Analysis and Sinus Rhythm.pptx"
D12 = "12. Ectopy, Escape Rhythms and Supraventricular Dysrhythmias.pptx"


def fig(name, alt, cap, deck, slide):
    for p in (alt, cap):
        assert "  " not in p, p[:40]
    path = os.path.join(DIR, IMG, name)
    assert os.path.exists(path), name
    w, h = Image.open(path).size
    return ('<figure class="fig"><img width="%d" height="%d" loading="lazy" src="%s/%s" alt="%s">'
            '<figcaption>%s <span class="tag">Source: %s, Slide %s.</span></figcaption></figure>'
            % (w, h, IMG, name, alt, cap, deck, slide))


def f11(name, alt, cap, slide): return fig(name, alt, cap, D11, slide)
def f12(name, alt, cap, slide): return fig(name, alt, cap, D12, slide)


STAR = '<mark class="prof-highlight">&#9733; '

# =====================================================================================  LECTURE 11
L11 = f'''<section class="deck" id="rhythm-analysis">
  <h2 class="deck-title">11 &middot; Rhythm Analysis &amp; Sinus Rhythms</h2>
  <p class="lecturer">Scott Mathis, EMS (emergency medical services) educator, First Response Training Group &middot; 5 October 2026</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Topic Outline 11: Rhythm Analysis and Sinus Rhythms</p>
    <ol type="a">
      <li>Review cardiac conduction system anatomy and physiology.</li>
      <li>Review ECG lead placement.</li>
      <li>Review determination of: i. Heart rate &middot; ii. Rhythm &middot; iii. PR interval &middot; iv. QRS duration &middot; v. QT interval &middot; vi. QTc interval</li>
      <li>Apply a systematic approach to ECG interpretation.</li>
      <li>Recognize normal sinus rhythm.</li>
      <li>Recognize sinus rhythms: i. Sinus bradycardia &middot; ii. Sinus tachycardia &middot; iii. Sinus arrhythmia</li>
      <li>Interpret electrocardiographic findings for sinus rhythms: i. Sinus arrhythmia &middot; ii. Sinus block &middot; iii. Sick sinus syndrome</li>
      <li>Compare and contrast sinus rhythms: i. Sinus bradycardia &middot; ii. Sinus tachycardia &middot; iii. Sinus arrhythmia &middot; iv. Sinus block &middot; v. Sick sinus syndrome</li>
      <li>Discuss the related anatomy and physiology of sinus node dysfunction.</li>
    </ol>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Lecturer emphasized &mdash; 5 October recording</span>
  <table>
    <tr><th>He said</th><th>So</th></tr>
    <tr><td><em>&ldquo;If there is P waves, the rhythm is atrial. Remember that, that&rsquo;s very important.&rdquo;</em> (part 2, 0:00)</td><td>A P wave before every QRS means the impulse starts above the ventricles, whatever the QRS looks like. Uniform upright P waves mean the sinus node. See 11.4.</td></tr>
    <tr><td><em>&ldquo;Very important for you to remember, duration of the PR interval should be between 0.12 and 0.2 seconds.&rdquo;</em> (part 2, 2:00) The QRS <em>&ldquo;must be&rdquo;</em> under 0.12 seconds.</td><td>Three to five small boxes for the PR; under three small boxes for the QRS. These two numbers decide most of the rhythms that follow.</td></tr>
    <tr><td>The five steps: <em>&ldquo;you need to do every single time you&rsquo;re interpreting a rhythm.&rdquo;</em> (part 2, 17:00) <em>&ldquo;If you follow that systematic approach, 99% of the time you are going to be correct.&rdquo;</em> (part 1, 2:00)</td><td>Rate, regularity, P waves, PR interval, QRS, in that order, on every strip (11.4).</td></tr>
    <tr><td>The six-second method is <em>&ldquo;probably the most commonly used method you are going to use&rdquo;</em> (part 2, 23:00). The 1500 method: <em>&ldquo;ain&rsquo;t nobody got time for that.&rdquo;</em></td><td>Know the six-second and count-down methods cold; know that the 1500 method is the most accurate (11.3).</td></tr>
    <tr><td>The absolute and relative refractory periods: <em>&ldquo;very, very important that you understand that.&rdquo;</em> (part 2, 13:00)</td><td>The peak of the T wave divides them (11.1); it is the basis of R on T in Lecture 12.</td></tr>
    <tr><td>Sinus arrhythmia: <em>&ldquo;the only difference between sinus arrhythmia and sinus rhythm essentially is the irregularity.&rdquo;</em> (part 3, 2:00)</td><td>And bradycardia and tachycardia differ from normal sinus rhythm only in rate (11.8).</td></tr>
    <tr><td><strong>Not examined now, said out loud:</strong> the U wave (<em>&ldquo;Don&rsquo;t focus on that right now&rdquo;</em>, part 2, 15:00), the word hexaxial (<em>&ldquo;Don&rsquo;t get too into the weeds of that terminology&rdquo;</em>, part 2, 42:00), and all treatment (<em>&ldquo;That&rsquo;ll be next week&rdquo;</em>, part 1, 0:00).</td><td>Recognize and interpret; do not learn management from this lecture.</td></tr>
  </table></div>

  <div class="callout"><p><strong>The one-line frame for the whole lecture.</strong> <em>Every rhythm is read the same five ways, and every sinus rhythm has the same P waves.</em> Normal sinus rhythm, sinus bradycardia and sinus tachycardia differ only in rate; sinus arrhythmia only in regularity; sinus exit block, sinus pause and sinus arrest by what happens to the missing beats.</p></div>

  <h3 class="sub" id="ra-conduction">11.1 &middot; Objective a &mdash; The conduction system and the cardiac cell</h3>
  <p>The heart has four chambers. The right atrium receives deoxygenated blood from the two venae cavae, the right ventricle pumps it to the lungs, the left atrium receives oxygenated blood from the lungs and the left ventricle pumps it into the aorta. <strong>Seventy to 80 percent of ventricular filling is passive</strong>, needing no atrial contraction, which becomes important when the atria stop contracting (atrial fibrillation, Lecture 12).</p>
  <table>
    <tr><th>Structure</th><th>Where and what</th><th>Intrinsic rate</th></tr>
    <tr><td><strong>Sinoatrial node</strong></td><td>The main pacemaker. Upper wall of the right atrium, just below the opening of the superior vena cava.</td><td><strong>60&ndash;100 per minute</strong></td></tr>
    <tr><td>Bachmann&rsquo;s bundle</td><td>Extends from the right to the left atrium; the main route of interatrial conduction.</td><td>&mdash;</td></tr>
    <tr><td>Three internodal tracts</td><td>Superior anterior (the <strong>fast</strong> tract), middle, and inferior posterior (the <strong>slow</strong> tract), from the sinoatrial node toward the atrioventricular node. In most people <strong>only the fast tract truly attaches to the atrioventricular node</strong>; the other two end within the right atrium (this matters for reentry, Lecture 12).</td><td>&mdash;</td></tr>
    <tr><td><strong>Atrioventricular node</strong></td><td>At the junction of the atria and ventricles, near the coronary sinus. The <strong>backup pacemaker</strong> if the sinoatrial node fails. Three zones: transition, compact and trigger.</td><td><strong>40&ndash;60 per minute</strong></td></tr>
    <tr><td><strong>Bundle of His</strong></td><td>Connects the atrioventricular node to the bundle branches. A nonconductive atrioventricular septum separates atria from ventricles, so <strong>in a normal heart the bundle of His is the only path from atria to ventricles</strong>.</td><td>&mdash;</td></tr>
    <tr><td>Left bundle branch</td><td>A small piece of tissue that splits into <strong>three fascicles</strong>: the left posterior (finger-like projections across the posterior left ventricle), the interventricular septal (depolarizes the septum, the Q wave) and the left anterior (ends in the Purkinje network).</td><td>&mdash;</td></tr>
    <tr><td>Right bundle branch</td><td>A <strong>much longer</strong> piece of tissue than the left bundle; enters the right ventricle and ends in the Purkinje network.</td><td>&mdash;</td></tr>
    <tr><td><strong>Purkinje network</strong></td><td>The heart&rsquo;s third pacemaker, used when both nodes fail. Conducts action potentials more quickly and efficiently than any other cell in the conduction system; essential for synchronized rhythm.</td><td><strong>20&ndash;40 per minute</strong></td></tr>
  </table>
  {f11("l11-s008-atrial-conduction-system.png", "Diagram of the atria showing the sinoatrial node, Bachmann's bundle to the left atrium, the anterior, middle and posterior internodal tracts, the atrioventricular node and the coronary sinus.", "<b>The atrial conduction system.</b> From the sinoatrial node, Bachmann&rsquo;s bundle carries the impulse to the left atrium, and three internodal tracts (anterior, middle, posterior) run toward the atrioventricular node near the coronary sinus. In most people only the anterior (fast) tract truly reaches the node.", 8)}
  {f11("l11-s012-left-bundle-fascicles.png", "Diagram of the atrioventricular node, bundle of His, right bundle branch and the left bundle branch dividing into septal, left posterior and left anterior fascicles.", "<b>The bundle branches.</b> The bundle of His divides into the right bundle branch and the left bundle branch, and the left divides again into three fascicles: septal, left posterior and left anterior.", 12)}
  <p><strong>Four cardiac cell properties.</strong> <strong>Automaticity</strong>: producing its own impulse. <strong>Excitability</strong>: responding to an impulse or stimulus. <strong>Contractility</strong>: contracting. <strong>Conductivity</strong>: conducting the impulse from myocyte to myocyte. Spontaneous firing of the lower cells is prevented by the <strong>natural hierarchy of pacemaker function</strong>, so the fastest pacemaker, the sinoatrial node, normally sets the rate.</p>
  <table>
    <tr><th>Action potential phase</th><th>What happens</th></tr>
    <tr><td><strong>4</strong> &mdash; rest (diastole)</td><td>More potassium inside, sodium and calcium outside; the inside sits at <strong>&minus;90 millivolts</strong> and the cell is ready to respond.</td></tr>
    <tr><td><strong>0</strong> &mdash; upstroke (depolarization)</td><td>Fast sodium channels open and <strong>sodium rushes in</strong>, making the inside positive.</td></tr>
    <tr><td><strong>1</strong> &mdash; early repolarization, &ldquo;the notch&rdquo;</td><td>Sodium channels close and potassium channels reopen; a slight negative shift.</td></tr>
    <tr><td><strong>2</strong> &mdash; plateau</td><td><strong>Calcium enters the cell and causes contraction</strong>; the voltage holds level while potassium moves the other way.</td></tr>
    <tr><td><strong>3</strong> &mdash; rapid repolarization</td><td>Calcium channels close, potassium channels stay open and <strong>potassium flows out of the cell</strong>, and the inside returns to &minus;90 millivolts.</td></tr>
  </table>
  {f11("l11-s017-action-potential-phases.png", "Graph of membrane potential against time for a ventricular action potential, phases 4, 0, 1, 2, 3 labeled, with the ion channels for each phase shown above.", "<b>The cardiac action potential.</b> The phases run 4, 0, 1, 2, 3: rest at &minus;90 millivolts, the sodium upstroke, the notch, the calcium plateau and repolarization. The figure&rsquo;s own labels show potassium <em>leaving</em> the cell (efflux) during repolarization.", 17)}
  <p>{STAR}<strong>Absolute refractory period</strong>: a short time after an action potential (typically about 180 milliseconds) when the cell <strong>will not respond</strong> to another stimulus. <strong>Relative refractory period</strong>: during repolarization, when the cell <strong>will respond</strong> to a second stimulus but is <strong>very fragile</strong>. The <strong>peak of the T wave</strong> divides the two.</mark></p>
  {f11("l11-s037-refractory-periods.png", "Two copies of one PQRST complex: on the left, shading from the start of the QRS to the T wave peak, labeled absolute refractory period; on the right, shading over the downslope of the T wave, labeled relative refractory period.", "<b>The two refractory periods on the tracing.</b> Absolute from the start of the QRS to the peak of the T wave; relative over the T wave&rsquo;s downslope. A stimulus in the relative period can trigger an arrhythmia.", 37)}
  <p><strong>The heart&rsquo;s vector.</strong> The heart sits in the mediastinum; the true pathway of conduction runs <strong>left and down, toward the front of the body</strong>, and any variation is abnormal. <strong>Lead II has a perfect view of that vector</strong>, which is why it is the lead used for rhythm interpretation.</p>
  <div class="callout warn"><p><strong>Where the slide text and the truth differ.</strong> Slides 20&ndash;22 say potassium moves <em>into</em> the cell in phases 1, 2 and 3. Repolarization is potassium <strong>leaving</strong> the cell (an outward positive current makes the inside negative again), and the deck&rsquo;s own figure on slide 17 shows exactly that efflux. The quizzes key the efflux.</p></div>

  <h3 class="sub" id="ra-leads">11.2 &middot; Objective b &mdash; Lead placement</h3>
  <table>
    <tr><th>Leads</th><th>How they are made</th></tr>
    <tr><td><strong>I, II, III</strong> &mdash; limb, <strong>bipolar</strong></td><td>Einthoven&rsquo;s triangle across both shoulders and the left leg; each needs a physical positive and negative pole. <strong>Lead I</strong>: positive left shoulder, negative right shoulder. <strong>Lead II</strong>: positive <strong>left foot</strong>, negative <strong>right shoulder</strong>. <strong>Lead III</strong>: positive left foot, negative left shoulder. Each positive lead is a camera.</td></tr>
    <tr><td><strong>aVR, aVL, aVF</strong> (augmented vector right, left, foot) &mdash; <strong>unipolar</strong></td><td>Amplified and created by the machine from one physical lead and a theoretical negative pole in the center of the heart, the central terminal. (Slide 64 calls it Wilson&rsquo;s terminal; strictly, Wilson&rsquo;s central terminal is the chest leads&rsquo; reference, and the augmented leads use the average of the other two limb electrodes.)</td></tr>
    <tr><td>The six limb leads together</td><td>I, II, III and the augmented leads form the first six leads of the 12-lead tracing and are used to determine the axis.</td></tr>
    <tr><td><strong>V1&ndash;V6</strong> &mdash; precordial (chest), <strong>unipolar</strong></td><td>Use the central terminal as the negative pole; very specific placement; give a <strong>horizontal</strong> view of the heart.</td></tr>
  </table>
  {f11("l11-s062-einthoven-triangle.png", "Figure of a person with arms outstretched and electrodes on the right arm, left arm and left leg, the triangle between them shaded and labeled Einthoven's triangle, with leads I, II and III along its sides.", "<b>Einthoven&rsquo;s triangle.</b> The three bipolar limb leads join the right arm, left arm and left leg: lead I across the shoulders, lead II from the right arm to the left leg, lead III from the left arm to the left leg.", 62)}
  <table>
    <tr><th>Chest lead</th><th>Placement</th></tr>
    <tr><td>V1</td><td>Fourth intercostal space, just <strong>right</strong> of the sternum</td></tr>
    <tr><td>V2</td><td>Fourth intercostal space, just <strong>left</strong> of the sternum</td></tr>
    <tr><td>V3</td><td>Directly between V2 and V4</td></tr>
    <tr><td>V4</td><td>Fifth intercostal space at the midclavicular line</td></tr>
    <tr><td>V5</td><td>Level with V4 at the left anterior axillary line</td></tr>
    <tr><td>V6</td><td>Level with V5 at the midaxillary line</td></tr>
  </table>
  {f11("l11-s068-precordial-lead-placement.jpg", "Chest figure with six colored electrode positions, beside a key listing V1 to V6 with their intercostal spaces and lines.", "<b>Precordial lead placement.</b> V1 and V2 in the fourth space either side of the sternum, V4 in the fifth space at the midclavicular line, V3 between them, V5 and V6 level with V4 at the anterior and mid axillary lines.", 68)}
  <table>
    <tr><th>Leads (contiguous groups)</th><th>Look at</th></tr>
    <tr><td>V1, V2</td><td>Septal wall</td></tr>
    <tr><td>V3, V4</td><td>Anterior wall of the left ventricle</td></tr>
    <tr><td>I, aVL (augmented vector left), V5, V6</td><td>Lateral wall of the left ventricle</td></tr>
    <tr><td>II, III, aVF (augmented vector foot)</td><td>Inferior wall</td></tr>
  </table>
  <p><strong>Contiguous leads</strong> are two or more leads that look at the same area of the heart: V1&ndash;V4; II, III and aVF; I, aVL, V5 and V6. aVR (augmented vector right) has clinical significance but is not usually used in basic 12-lead interpretation.</p>
  {f11("l11-s070-contiguous-leads.jpg", "A 12-lead tracing laid out in its grid with the lead boxes shaded and labeled lateral, inferior and anterior or septal, and a legend naming the leads in each group.", "<b>Contiguous lead groups on a 12-lead tracing.</b> Lateral (I, aVL, V5, V6), inferior (II, III, aVF) and anterior or septal (V1 to V4).", 70)}

  <h3 class="sub" id="ra-determine">11.3 &middot; Objective c &mdash; Determining rate, rhythm, PR, QRS, QT and QTc</h3>
  <p><strong>The paper.</strong> Printed at 25 millimeters per second. Each <strong>small box</strong> is 1 millimeter tall and <strong>0.04 seconds</strong> wide; each <strong>large box</strong> is five small boxes, 5 millimeters tall and <strong>0.2 seconds</strong> wide. Left to right is <strong>time</strong>; up and down is <strong>voltage</strong>. Standard calibration is one large box (0.2 seconds) wide and two large boxes (10 millimeters) tall.</p>
  <table>
    <tr><th>Component</th><th>Represents</th><th>Normal</th></tr>
    <tr><td>Baseline (isoelectric line)</td><td>No electrical activity; all measurements start here</td><td>&mdash;</td></tr>
    <tr><td><strong>P wave</strong></td><td>Atrial depolarization, whatever its morphology</td><td>Round and upright in lead II, 2.5 millimeters or less tall, under 0.12 seconds</td></tr>
    <tr><td><strong>PR interval</strong></td><td>Onset of P to start of QRS: the impulse reaching the atrioventricular node, the His bundle, the bundle branches and the Purkinje network (&ldquo;the busiest time in the cardiac cycle&rdquo;)</td><td>{STAR}<strong>0.12&ndash;0.20 seconds (3&ndash;5 small boxes)</strong></mark>, constant across the strip</td></tr>
    <tr><td><strong>QRS complex</strong></td><td>Ventricular depolarization; called a complex because it combines the Q, R and S waves (not every rhythm has all three)</td><td>{STAR}<strong>Under 0.12 seconds</strong>, narrow with sharp points</mark>; 0.12 seconds or more means abnormal conduction through the ventricles</td></tr>
    <tr><td>Q wave</td><td>First negative deflection after the PR: septal depolarization, away from lead II</td><td>Under 0.04 seconds, low amplitude, not always visible</td></tr>
    <tr><td>R wave</td><td>First positive deflection: ventricular depolarization moving toward lead II (the deck: the anterior left ventricle; see the note below)</td><td>&mdash;</td></tr>
    <tr><td>S wave</td><td>First negative deflection after the R, moving away from lead II (the deck: the lateral left ventricle)</td><td>Must go below baseline to be a true S wave; otherwise an S wave pattern</td></tr>
    <tr><td><strong>J point</strong></td><td>Where the QRS ends and the ST segment begins</td><td>At baseline, 1 millimeter variance allowed</td></tr>
    <tr><td>ST segment</td><td>Between ventricular depolarization and repolarization; the ventricles hold their contraction to empty</td><td>At baseline</td></tr>
    <tr><td>T wave</td><td>Ventricular repolarization</td><td>Asymmetric: slow upstroke, sharp downstroke; its peak divides the refractory periods</td></tr>
    <tr><td><strong>QT interval</strong></td><td>All ventricular activity in one cycle: start of QRS to end of T</td><td>350&ndash;450 milliseconds in males, 360&ndash;460 in females</td></tr>
    <tr><td><strong>TP segment</strong></td><td>The resting state: end of T to the next P</td><td><strong>The best place to judge the isoelectric line</strong> (the PR segment is not, because the impulse is still crossing the node)</td></tr>
    <tr><td>R to R and P to P intervals</td><td>Distance between consecutive R waves, and consecutive P waves</td><td>Used for rate, regularity and heart blocks</td></tr>
  </table>
  {f11("l11-s027-waves-segments-intervals.png", "Labeled diagram of one cardiac cycle: P wave, PR segment, PR interval, Q, R and S waves, QRS complex, ST segment, T wave, QT interval and the baseline.", "<b>The waves, segments and intervals.</b> An interval contains at least one wave; a segment is the flat line between waves. Lead II is the standard view.", 27)}
  {f11("l11-s030-pr-interval-conduction.png", "Conduction system diagram above a PR interval, color-coded: sinoatrial node, atria, atrioventricular node, His bundle, bundle branches and Purkinje fibers each mapped to their share of the PR interval.", "<b>What the PR interval contains.</b> Atrial depolarization (the P wave), then the hold in the atrioventricular node, then the His bundle, bundle branches and Purkinje fibers, all before the QRS begins.", 30)}
  {f11("l11-s040-tp-segment.jpg", "Close-up tracing with the PR segment, ST segment and TP segment each bracketed and labeled.", "<b>The TP segment is the true baseline.</b> Judge the isoelectric line between the end of the T wave and the next P wave, not in the PR segment.", 40)}
  <table>
    <tr><th>Rate method</th><th>How</th><th>When</th></tr>
    <tr><td>{STAR}<strong>Six-second method</strong></mark></td><td>On a six-second strip (two three-second markers, or 30 large boxes), count QRS complexes &times; 10 for the <strong>ventricular</strong> rate; count P waves &times; 10 for the <strong>atrial</strong> rate.</td><td>The most commonly used; works on irregular rhythms because it counts every beat.</td></tr>
    <tr><td><strong>Count-down method</strong></td><td>From an R wave on a heavy line, count the following heavy lines: 300, 150, 100, 75, 60, 50.</td><td><strong>Unreliable below 50</strong> (and on irregular rhythms).</td></tr>
    <tr><td><strong>300 method</strong></td><td>300 &divide; large boxes between consecutive R waves.</td><td>Regular rhythms.</td></tr>
    <tr><td><strong>1500 method</strong></td><td>1500 &divide; small boxes between consecutive R waves.</td><td><strong>The most accurate.</strong></td></tr>
  </table>
  {f11("l11-s045-six-second-strip.jpg", "Six-second rhythm strip with three-second tick marks and nine regularly spaced narrow complexes.", "<b>The six-second method.</b> Nine QRS complexes between the markers, times ten, is a ventricular rate of 90 per minute.", 45)}
  {f11("l11-s048-count-down-method.png", "Strip with arrows over the heavy grid lines after an R wave, labeled start here, 300, 150, 100, 75, 60 and 50.", "<b>The count-down method.</b> Start at an R wave on a heavy line and count down the following heavy lines; where the next R wave lands is the rate.", 48)}
  <p><strong>Rhythm (regularity).</strong> Compare consecutive R to R intervals. Most irregular rhythms are obvious at a glance; if unsure, use <strong>calipers</strong> (or a marked sheet of paper).</p>
  <p><strong>QTc.</strong> This deck has no slide on the QTc interval. It is the QT corrected for heart rate, covered in Lecture 7 (Exam 2 guide, section 7.7): the same normal values as the QT, borderline above 450 (460 in women) to 500 milliseconds, and high-risk above 500 milliseconds.</p>
  <div class="callout warn"><p><strong>Slide 26 says a small box is &ldquo;0.04ms&rdquo; in duration.</strong> It is 0.04 <strong>seconds</strong> (40 milliseconds); five of them make the 0.2-second large box on the same slide.</p></div>
  <div class="callout warn"><p><strong>Slides 33 and 34 tie the R wave to the anterior left ventricle and the S wave to its lateral wall.</strong> Standard teaching describes the R wave as depolarization of the main mass of the ventricles and the S wave as the last, basal parts to depolarize, not as single walls. Both agree on the direction (toward lead II draws an upright wave, away from it a negative one), and that is all the quizzes ask.</p></div>

  <h3 class="sub" id="ra-system">11.4 &middot; Objective d &mdash; The systematic approach</h3>
  <div class="pearl"><strong>Five steps, every strip, in order.</strong> 1 <strong>Rate</strong> (under 60, 60&ndash;100, over 100) &rarr; 2 <strong>Regularity</strong> (consecutive R to R intervals) &rarr; 3 <strong>P waves</strong> &rarr; 4 <strong>PR interval</strong> (0.12&ndash;0.20 seconds, constant?) &rarr; 5 <strong>QRS</strong> (narrow under 0.12 seconds, or wide).</div>
  <p>The P wave questions: Are they all the same morphology? Is there one before each QRS? Are they <strong>married</strong> to the QRS complexes (is each P wave causing its QRS)? Are they normal (round, upright in lead II, 2.5 millimeters or less, under 0.12 seconds)? Is the PR interval constant across the strip? Atrioventricular nodal blocks, accessory pathways and alternate pacemaker sites can put the PR outside its normal range.</p>
  <p>{STAR}<strong>A P wave before every QRS means the rhythm is atrial in origin</strong>, whatever the QRS looks like; uniform upright P waves point to the sinoatrial node.</mark> No P waves with a QRS means the impulse began below the atria.</p>
  {f11("l11-s058-normal-sinus-rhythm.jpg", "Rhythm strip of evenly spaced narrow complexes, each preceded by a small upright P wave.", "<b>P waves married to every QRS.</b> One uniform upright P wave before each narrow QRS at a constant PR: the impulse is coming from the sinoatrial node.", 58)}

  <h3 class="sub" id="ra-nsr">11.5 &middot; Objective e &mdash; Normal sinus rhythm</h3>
  <table>
    <tr><th>Normal sinus rhythm</th><th></th></tr>
    <tr><td>Rate</td><td>60&ndash;100 per minute</td></tr>
    <tr><td>Regularity</td><td>Regular</td></tr>
    <tr><td>P waves</td><td>Normal, present, married to the QRS complexes</td></tr>
    <tr><td>PR interval</td><td>Normal, 0.12&ndash;0.20 seconds, constant</td></tr>
    <tr><td>QRS</td><td>Narrow</td></tr>
  </table>
  <p>The worked strip on slides 73&ndash;74 runs at 75&ndash;80 per minute: regular, P waves present and married, normal PR, narrow QRS.</p>

  <h3 class="sub" id="ra-brady-tachy">11.6 &middot; Objective f &mdash; Sinus bradycardia, sinus tachycardia and sinus arrhythmia</h3>
  <table>
    <tr><th></th><th>Sinus bradycardia</th><th>Sinus tachycardia</th><th>Sinus arrhythmia</th></tr>
    <tr><td>Rate</td><td><strong>Under 60</strong></td><td><strong>Over 100</strong></td><td>60&ndash;100</td></tr>
    <tr><td>Regularity</td><td>Regular</td><td>Regular</td><td><strong>Irregular</strong></td></tr>
    <tr><td>P waves</td><td colspan="3">Normal, present, married to the QRS complexes</td></tr>
    <tr><td>PR interval</td><td colspan="3">Normal, 0.12&ndash;0.20 seconds</td></tr>
    <tr><td>QRS</td><td>Narrow or wide</td><td>Narrow or wide</td><td>Narrow or wide (most often narrow)</td></tr>
  </table>
  <p>What makes each of these <em>sinus</em> is the P waves: present, normal and married to the QRS. The QRS can be wide if ventricular conduction is abnormal without changing the name.</p>
  {f11("l11-s076-sinus-bradycardia.png", "Rhythm strip with three widely spaced narrow complexes, each preceded by a small upright P wave.", "<b>Sinus bradycardia, about 51 per minute.</b> Regular, normal P waves married to narrow QRS complexes, normal PR; only the rate (R waves about six large boxes apart) is below 60.", 76)}
  {f11("l11-s079-sinus-tachycardia.jpg", "Rhythm strip of closely and evenly spaced narrow complexes, each with a small P wave before it.", "<b>Sinus tachycardia, 150 per minute.</b> R waves two large boxes apart; regular, with a normal P wave married to each narrow QRS.", 79)}
  {f11("l11-s083-sinus-arrhythmia.png", "Rhythm strip with three-second marks and narrow complexes, each with an upright P wave, at varying spacing.", "<b>Sinus arrhythmia, 60&ndash;70 per minute.</b> Every beat is a normal sinus beat (P wave, normal PR, narrow QRS), but the R to R intervals lengthen and shorten.", 83)}

  <h3 class="sub" id="ra-interpret">11.7 &middot; Objective g &mdash; Interpreting sinus arrhythmia, sinus block and sick sinus syndrome</h3>
  <p><strong>Sinus arrhythmia</strong> (respiratory sinus arrhythmia) is a <strong>benign</strong> variation in the intervals between heartbeats, <strong>most commonly seen in children</strong>. The rate rises on inspiration and falls on exhalation; you can watch it follow the patient&rsquo;s breathing.</p>
  {f11("l11-s081-sinus-arrhythmia-respiration.png", "Diagram linking the medulla, vagus nerve and lungs to the sinoatrial node, with strips showing the rate changing between expiration, inspiration and expiration.", "<b>Sinus arrhythmia follows breathing.</b> All complexes are normal and the rhythm is irregular; the figure&rsquo;s criterion is that the longest R to R interval exceeds the shortest by more than 0.16 seconds.", 81)}
  <p><strong>Sinus exit block</strong> (sinus block): the sinus node fires as normal, but its impulses are <strong>blocked</strong>, so one or more whole cardiac cycles are absent (no P wave, no QRS, no T wave). Because the node never stopped, <strong>the P to P intervals still march out</strong> once activity resumes: the gap is an exact multiple of the normal cycle.</p>
  {f11("l11-s085-sinus-exit-block-diagram.jpg", "Diagram of a regular rhythm with one missing complex drawn in as a ghost, the gap marked as a multiple of the P to P interval.", "<b>Sinus exit block.</b> The missing beat would have landed exactly on schedule, so the gap is a multiple of the P to P interval.", 85)}
  {f11("l11-s089-sinus-exit-block.jpg", "Monitor strip titled SA exit block with the intervals labeled 1.1, 1.0, 2.2 and 1.0 seconds.", "<b>Sinus exit block on a monitor strip.</b> The 2.2-second gap is two 1.1-second cycles: the beats march out.", 89)}
  <p>{STAR}<strong>Sick sinus syndrome</strong>: sinus exit block, sinus pause and sinus arrest occurring in the same patient, even on the same strip.</mark> The deck calls it rare.</p>

  <h3 class="sub" id="ra-compare">11.8 &middot; Objective h &mdash; The sinus rhythms compared</h3>
  <table>
    <tr><th>Rhythm</th><th>Rate</th><th>Regular?</th><th>The deciding feature</th></tr>
    <tr><td>Normal sinus rhythm</td><td>60&ndash;100</td><td>Yes</td><td>All criteria normal</td></tr>
    <tr><td>Sinus bradycardia</td><td>Under 60</td><td>Yes</td><td>Rate only</td></tr>
    <tr><td>Sinus tachycardia</td><td>Over 100</td><td>Yes</td><td>Rate only</td></tr>
    <tr><td>Sinus arrhythmia</td><td>60&ndash;100</td><td>No</td><td>R to R varies with breathing; no beats missing</td></tr>
    <tr><td>Sinus exit block</td><td>Variable (typically under 150)</td><td>No</td><td>Whole cycles missing; <strong>P to P marches out</strong></td></tr>
    <tr><td>Sinus pause</td><td>Variable</td><td>No</td><td>Node stops and restarts; <strong>resets</strong>, P to P does not march out</td></tr>
    <tr><td>Sinus arrest</td><td>Variable</td><td>No</td><td>Like a pause, but <strong>at least three cycles missed</strong></td></tr>
    <tr><td>Sick sinus syndrome</td><td>Variable</td><td>No</td><td>Exit block, pause and arrest together in one patient</td></tr>
  </table>
  <p>In exit block, pause and arrest the P waves, when present, are normal and married to the QRS, and the PR is normal; the deck&rsquo;s criteria table for all three is the same (slides 86, 92 and 96).</p>
  {f11("l11-s091-sinus-pause-diagram.jpg", "Diagram of a regular rhythm with one long gap, a star marking where the node stopped, the gap labeled as not a multiple of the P to P interval.", "<b>Sinus pause.</b> The node stops and starts again, so the next beat does not land on the old schedule: not a multiple of the P to P interval.", 91)}
  {f11("l11-s093-sinus-pause.jpg", "Rhythm strip with four sinus beats, a long flat stretch, then two more beats.", "<b>Sinus pause on a strip.</b> After the flat gap the rhythm resumes on a new timing.", 93)}
  {f11("l11-s095-sinus-arrest-diagram.jpg", "Diagram of a regular rhythm with a very long gap, labeled as longer than a sinus pause and not a multiple of the P to P interval.", "<b>Sinus arrest.</b> Longer than a pause (at least three cycles missed) and, like a pause, not a multiple of the P to P interval.", 95)}
  {f11("l11-s099-sinus-arrest.jpg", "Rhythm strip with four narrow complexes, a long flat baseline several cycles wide, then four more complexes.", "<b>Sinus arrest on a strip.</b> Well over three cycles are missing before the sinus beats return.", 99)}
  <div class="callout warn"><p><strong>Two recording slips, keyed to the deck.</strong> In passing the lecturer said sinus arrest <em>&ldquo;picks back up at the same rate that it started at&rdquo;</em>; the deck (slide 95) and his own answer to a student at the end of the clip say the node <strong>resets</strong>, so the beats after an arrest do not march out. He also said sinus arrhythmia is seen in kids <em>&ldquo;and elderly&rdquo;</em>; the deck says most commonly in children, which is what the quizzes key. The deck&rsquo;s line of three missed cycles for sinus arrest is this course&rsquo;s dividing line; other references draw it by the length of the pause instead.</p></div>

  <h3 class="sub" id="ra-dysfunction">11.9 &middot; Objective i &mdash; Anatomy and physiology of sinus node dysfunction</h3>
  <ul>
    <li><strong>The node.</strong> The sinoatrial node, in the upper right atrial wall below the superior vena cava, fires at 60&ndash;100 per minute and keeps the lower pacemakers quiet through the pacemaker hierarchy; when it fails, the atrioventricular node (40&ndash;60) and then the Purkinje network (20&ndash;40) take over.</li>
    <li><strong>Exit block</strong> is a conduction problem: the node fires on time but the impulse is blocked from leaving it, so the timing is preserved and the beats march out.</li>
    <li><strong>Pause and arrest</strong> are firing problems: the node stops and starts again, the cycle resets, and the beats do not march out; at least three missed cycles is arrest.</li>
    <li><strong>Sick sinus syndrome</strong> is the combination of all three in one patient.</li>
    <li><strong>Sinus arrhythmia</strong> is physiology, not dysfunction: on inspiration intrathoracic pressure falls, arterial pressure falls, the baroreceptors respond, <strong>vagal tone is suppressed</strong> and the heart rate rises; on exhalation the opposite happens.</li>
  </ul>
</section>
'''

# =====================================================================================  LECTURE 12
L12 = f'''<section class="deck" id="ectopy-supraventricular">
  <h2 class="deck-title">12 &middot; Ectopy, Escape Rhythms &amp; Supraventricular Dysrhythmias</h2>
  <p class="lecturer">Scott Mathis, EMS (emergency medical services) educator, First Response Training Group &middot; 5 October 2026</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Topic Outline 12: Ectopy, Escape Rhythms, and Supraventricular Dysrhythmias</p>
    <ol type="a">
      <li>Recognize atrial, junctional, and ventricular premature beats.</li>
      <li>Compare and contrast ECG findings associated with atrial, junctional, and ventricular premature beats: i. Atrial premature beats &middot; ii. Junctional premature beats &middot; iii. Ventricular premature beats</li>
      <li>Recognize atrial, junctional, and ventricular escape rhythms.</li>
      <li>Recognize ECG findings associated with dysrhythmias: i. Junctional rhythm &middot; ii. Accelerated junctional rhythm &middot; iii. Idioventricular rhythm</li>
      <li>Compare and contrast junctional and idioventricular rhythms.</li>
      <li>Recognize common supraventricular dysrhythmias: i. Atrial tachycardia &middot; ii. Supraventricular tachycardia (SVT) &middot; iii. Atrial flutter &middot; iv. Atrial fibrillation</li>
      <li>Compare and contrast ECG findings associated with supraventricular dysrhythmias: i. Atrial flutter &middot; ii. Atrial fibrillation &middot; iii. SVT &middot; iv. Atrial tachycardia</li>
      <li>Discuss the related anatomy and physiology of supraventricular arrhythmias.</li>
    </ol>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Lecturer emphasized &mdash; 5 October recording</span>
  <table>
    <tr><th>He said</th><th>So</th></tr>
    <tr><td>Atrial flutter&rsquo;s sawtooth: <em>&ldquo;This is the only rhythm that will have this pattern. If you see this on a test &hellip; it&rsquo;s a flutter.&rdquo;</em> (part 2, 15:00)</td><td>The sawtooth is pathognomonic. Then document the ratio (12.6).</td></tr>
    <tr><td><em>&ldquo;If you ever hear the phrase irregularly irregular, they&rsquo;re talking about atrial fibrillation.&rdquo;</em> (part 2, 26:00)</td><td>No P waves, fibrillatory waves, irregularly irregular.</td></tr>
    <tr><td><em>&ldquo;No P wave, narrow QRS, regular R-R interval, and a rate above 150 is AVNRT (atrioventricular nodal reentrant tachycardia), or SVT (supraventricular tachycardia).&rdquo;</em> (part 2, 40:00) And: <em>&ldquo;the rate does not determine the rhythm.&rdquo;</em> (part 2, 13:00)</td><td>A sinus P wave before every QRS is sinus tachycardia even at 200; the reentry tachycardia has no visible P waves (12.7).</td></tr>
    <tr><td><em>&ldquo;A junctional rhythm by definition must be regular. So if it is irregular, find where it is irregular &hellip; that&rsquo;s where your PJC (premature junctional complex) is going to be.&rdquo;</em> (part 3, 15:00)</td><td>Junctional rhythms are regular; an early beat interrupting one is a premature junctional complex (12.4).</td></tr>
    <tr><td><em>&ldquo;Anytime you see a wide QRS with a contralateral T wave, think ventricular.&rdquo;</em> (part 3, 27:00)</td><td>Wide plus opposite-direction T wave means a ventricular origin (12.2).</td></tr>
    <tr><td><em>&ldquo;If it&rsquo;s one or the other, always go with the T wave.&rdquo;</em> (part 3, 1:00)</td><td>When a single wave between rapid QRS complexes could be a P or a T, call it a T wave and say no P waves are visible.</td></tr>
    <tr><td><strong>Not this week, said out loud:</strong> <em>&ldquo;we&rsquo;re not gonna get into treatment here. This is just solely about rhythm interpretation and diagnosis&rdquo;</em> (part 1, 0:00); the three types of atrial fibrillation: <em>&ldquo;You don&rsquo;t have to get too much into the weeds of this right now&rdquo;</em> (part 2, 25:00).</td><td>Recognize and compare; management comes later.</td></tr>
  </table></div>

  <div class="callout"><p><strong>The one-line frame for the whole lecture.</strong> <em>Early or late, narrow or wide, and what the P wave looks like.</em> A premature beat comes early; an escape beat comes late after a pause. A narrow QRS means the impulse used the normal pathway from above the ventricles; a wide QRS with an opposite T wave means it started in the ventricles. The P wave says where above the ventricles: a new-shaped upright P is atrial, an inverted, hidden or trailing P is junctional, a sawtooth is flutter, chaos is fibrillation.</p></div>

  <h3 class="sub" id="es-premature">12.1 &middot; Objective a &mdash; Recognizing premature beats</h3>
  <p><strong>Premature atrial complex.</strong> An early ectopic impulse from outside the sinoatrial node, within the atria, from one or several sites, usually from <strong>increased automaticity</strong>. It arrives <strong>early</strong> with a <strong>P wave of different morphology</strong> and (usually) a narrow QRS; the rest of the rhythm is normal.</p>
  {f12("l12-s006-premature-atrial-complex-diagram.jpg", "Two heart diagrams, one with normal conduction from the sinoatrial node and one with an ectopic atrial focus, above a strip in which the fourth beat is labeled PAC.", "<b>A premature atrial complex.</b> An ectopic atrial focus fires before the sinus node is due; the early beat has its own P wave.", 6)}
  {f12("l12-s007-premature-atrial-complexes-labeled.jpg", "Strip with two early beats labeled PAC and their P waves circled.", "<b>Premature atrial complexes on a strip.</b> The circled P waves come early and look different from the sinus P waves; the QRS that follows is narrow.", 7)}
  <p><strong>Premature junctional complex.</strong> Comes early, before the next expected R wave, from increased automaticity of the atrioventricular junction. Its P wave is that of any junctional beat: <strong>none, inverted, or after the QRS</strong>. <strong>Isolated premature junctional complexes have no clinical significance.</strong></p>
  {f12("l12-s050-premature-junctional-complexes.jpg", "Lead II rhythm strip with two arrows over early narrow beats that have no P wave in front of them.", "<b>Premature junctional complexes with no P waves.</b> The arrowed beats are early and narrow, with no P wave before them.", 50)}
  <p><strong>Premature ventricular complex.</strong> Comes early, before the next expected R wave. Ventricular beats are <strong>wide and abnormal-looking</strong> (QRS typically over 0.12 seconds), with <strong>no P wave</strong> and a T wave that goes the <strong>opposite</strong> direction (&ldquo;contralateral&rdquo;). Two in a row is a <strong>couplet</strong>, three a <strong>triplet</strong>; the same shape means one focus (<strong>unifocal</strong>), different shapes mean several foci (<strong>multifocal</strong>). Frequent, especially grouped, premature ventricular complexes can reduce cardiac output.</p>
  {f12("l12-s070-premature-ventricular-complex.png", "Strip of narrow beats in which one early beat is broad and deep with an upright wave after it.", "<b>A premature ventricular complex.</b> Early, wide, no P wave, and the T wave goes opposite to the QRS.", 70)}
  {f12("l12-s071-multifocal-pvc-couplet.jpg", "Two-lead strip with a circle around two consecutive broad beats of different shapes.", "<b>A multifocal couplet.</b> Two premature ventricular complexes in a row, of different shapes: two foci.", 71)}
  {f12("l12-s071-run-of-ventricular-tachycardia.jpg", "Strip with one broad beat then a run of six broad complexes between narrow beats.", "<b>A run of ventricular tachycardia.</b> After a single premature ventricular complex, six come in a row.", 71)}
  <p>{STAR}<strong>R on T.</strong> If the R wave of a premature ventricular complex lands on the T wave of the beat before it, in the relative refractory period, it can set off ventricular tachycardia or ventricular fibrillation.</mark></p>
  {f12("l12-s072-r-on-t.png", "Strip with labels for a premature beat landing on the T wave of the preceding beat, followed by rapid irregular polymorphic waves.", "<b>R on T.</b> A premature ventricular complex lands on the preceding T wave and a polymorphic ventricular tachycardia follows.", 72)}
  <p><strong>Patterns.</strong> Premature atrial, junctional and ventricular complexes can all recur in a pattern: every other beat is <strong>bigeminy</strong>, every third beat <strong>trigeminy</strong>, every fourth beat <strong>quadrigeminy</strong>.</p>
  {f12("l12-s008-atrial-bigeminy.jpg", "Two green grid strips with narrow beats arriving in close pairs.", "<b>Bigeminy.</b> Every other beat is premature (here premature atrial complexes).", 8)}
  {f12("l12-s009-atrial-trigeminy.jpg", "Lead II strip titled atrial trigeminy with every third beat early.", "<b>Trigeminy.</b> Two normal beats, then a premature one.", 9)}
  {f12("l12-s010-ventricular-quadrigeminy.jpg", "Lead II strip with a broad deep beat after every three narrow beats.", "<b>Quadrigeminy.</b> Every fourth beat is premature; here they are premature ventricular complexes, the deck&rsquo;s example on both slide 10 and slide 73.", 10)}
  {f12("l12-s073-trigeminal-pvcs.jpg", "Strip with two narrow beats then one broad beat, repeating.", "<b>Trigeminal premature ventricular complexes.</b> Every third beat is wide and early.", 73)}

  <h3 class="sub" id="es-premature-compare">12.2 &middot; Objective b &mdash; The three premature beats compared</h3>
  <table>
    <tr><th></th><th>Premature atrial</th><th>Premature junctional</th><th>Premature ventricular</th></tr>
    <tr><td>Origin</td><td>Atria, outside the sinoatrial node</td><td>Atrioventricular junction (most from the transition zone)</td><td>Ventricles</td></tr>
    <tr><td>Timing</td><td colspan="3">Early, before the next expected R wave</td></tr>
    <tr><td>P wave</td><td><strong>Present, different shape</strong></td><td><strong>None, inverted, or after the QRS</strong></td><td><strong>None</strong></td></tr>
    <tr><td>QRS</td><td>Usually narrow</td><td>Usually narrow</td><td><strong>Wide</strong>, abnormal, typically over 0.12 seconds</td></tr>
    <tr><td>T wave</td><td>Normal</td><td>Normal</td><td><strong>Opposite</strong> the QRS</td></tr>
    <tr><td>Patterns</td><td colspan="3">Bigeminy, trigeminy, quadrigeminy for all three</td></tr>
  </table>
  <div class="pearl"><strong>Narrow or wide first.</strong> A narrow early beat came from above the ventricles: look at its P wave to choose atrial (new upright P) or junctional (no P, inverted P, P after). A wide early beat with an opposite T wave and no P wave is ventricular.</div>

  <h3 class="sub" id="es-escape">12.3 &middot; Objective c &mdash; Escape beats and escape rhythms</h3>
  <p>An escape beat comes <strong>late</strong>, past the point where the next R wave was expected, because the pacemaker above it has failed or slowed.</p>
  <table>
    <tr><th>Escape</th><th>When</th><th>Looks like</th></tr>
    <tr><td><strong>Junctional escape beat</strong></td><td>The sinoatrial node fails to fire or fires too slowly</td><td>A late narrow beat after a pause, with junctional P wave findings; the sinus node then resets</td></tr>
    <tr><td><strong>Junctional escape rhythm</strong></td><td>Escape beats become the rhythm: the atrioventricular node takes over as the main pacemaker and suppresses the sinoatrial node</td><td>40&ndash;60 per minute, regular, junctional P waves (12.4)</td></tr>
    <tr><td><strong>Ventricular escape complex</strong></td><td>Both the sinoatrial and atrioventricular nodes fail to act as the pacemaker</td><td>A late wide beat past the expected R wave</td></tr>
    <tr><td><strong>Idioventricular rhythm</strong></td><td>The Purkinje network takes over as the primary pacemaker</td><td>20&ndash;40 per minute, regular, wide, no P waves (12.4)</td></tr>
  </table>
  {f12("l12-s052-junctional-escape-beat.jpg", "Strip titled junctional escape beat with a red arrow under a late narrow beat after a long gap.", "<b>A junctional escape beat.</b> After a pause past the expected R wave, a late narrow junctional beat arrives.", 52)}
  {f12("l12-s053-junctional-escape-rhythm-onset.jpg", "Strip labeled sinus beat failed to materialize, then a run labeled junctional escape.", "<b>A junctional escape rhythm begins.</b> The sinus beat fails to appear and the junction takes over.", 53)}
  {f12("l12-s074-ventricular-escape-complex.jpg", "Strip of narrow beats with one longer gap ended by a single broad beat.", "<b>A ventricular escape complex.</b> Late and wide: neither node supplied the beat.", 74)}
  <p><strong>Atrial escape rhythms</strong> are named in the objective, but the deck has no slide on them: its atrial rhythms are all premature, tachycardic or fibrillating ones.</p>

  <h3 class="sub" id="es-junctional">12.4 &middot; Objective d &mdash; Junctional, accelerated junctional and idioventricular rhythms</h3>
  <p><strong>Where the junctional P wave goes.</strong> A junctional impulse can travel up into the atria and down the His bundle at once, and its P wave depends on which arrives first:</p>
  <ul>
    <li><strong>Atria first</strong> &rarr; an <strong>inverted P wave</strong> just before the QRS (the atria depolarize from the bottom up, away from positive lead II), with a short PR.</li>
    <li><strong>At the same time</strong>, or the atria are never depolarized &rarr; <strong>no visible P wave</strong> (the QRS hides it).</li>
    <li><strong>Ventricles first</strong> (an impulse from the trigger zone reaches the His bundle first, then climbs the slow compact zone) &rarr; the <strong>P wave after the QRS</strong>.</li>
  </ul>
  {f12("l12-s047-junctional-inverted-p-wave.jpg", "Strip of narrow beats with the inverted P wave before one QRS drawn in red and labeled inverted P wave.", "<b>Inverted P waves of a junctional rhythm.</b> The atria are activated from below, so the P wave points down in lead II, close before the QRS.", 47)}
  <table>
    <tr><th></th><th>Junctional escape rhythm</th><th>Accelerated junctional rhythm</th><th>Junctional tachycardia</th></tr>
    <tr><td>Rate</td><td><strong>40&ndash;60</strong></td><td><strong>60&ndash;100</strong></td><td><strong>Over 100</strong></td></tr>
    <tr><td>Regularity</td><td colspan="3">Regular</td></tr>
    <tr><td>P waves</td><td colspan="3">Absent, or inverted, either just before the QRS or after it</td></tr>
    <tr><td>PR interval</td><td colspan="3">If present, under 0.12 seconds</td></tr>
    <tr><td>QRS</td><td colspan="3">Narrow or wide (most commonly narrow)</td></tr>
  </table>
  {f12("l12-s055-junctional-escape-rhythm.jpg", "Strip of regular narrow beats, each with a small inverted P wave just before it.", "<b>Junctional escape rhythm, 50 per minute.</b> Regular, inverted P waves married to narrow QRS complexes, short PR.", 55)}
  {f12("l12-s057-junctional-escape-rhythm-no-p.jpg", "Dark grid strip of regular narrow beats with no P waves.", "<b>Junctional escape rhythm, 50 per minute, no P waves.</b> The P waves are hidden in or absent from the QRS.", 57)}
  {f12("l12-s060-accelerated-junctional-rhythm.jpg", "Pink grid strip of regular narrow beats with small inverted deflections before them.", "<b>Accelerated junctional rhythm, 80 per minute.</b> The same junctional picture at 60&ndash;100.", 60)}
  {f12("l12-s067-junctional-tachycardia.jpg", "Lead II strip of rapid regular narrow beats with small inverted P waves before them.", "<b>Junctional tachycardia, 120 per minute.</b> The same picture over 100.", 67)}
  <table>
    <tr><th></th><th>Idioventricular rhythm</th><th>Accelerated idioventricular rhythm</th></tr>
    <tr><td>Rate</td><td><strong>20&ndash;40</strong></td><td><strong>40&ndash;100</strong></td></tr>
    <tr><td>Regularity</td><td colspan="2">Regular</td></tr>
    <tr><td>P waves / PR</td><td colspan="2">None</td></tr>
    <tr><td>QRS</td><td colspan="2"><strong>Wide</strong>, longer than 0.12 seconds</td></tr>
  </table>
  {f12("l12-s077-idioventricular-rhythm.jpg", "Pink grid strip with four widely spaced broad complexes and no P waves.", "<b>Idioventricular rhythm, 40 per minute.</b> Regular, wide, no P waves: the Purkinje network is pacing.", 77)}
  {f12("l12-s082-accelerated-idioventricular-rhythm.png", "Gray grid strip of regular broad complexes with no P waves at a faster rate.", "<b>Accelerated idioventricular rhythm, 90 per minute.</b> The same wide rhythm at 40&ndash;100.", 82)}
  <div class="callout warn"><p><strong>Slide 75 calls idioventricular rhythm &ldquo;also known as agonal rhythm.&rdquo;</strong> Agonal rhythm is the dying, very slow end of it (the lecturer: <em>&ldquo;especially if you&rsquo;re below 20 or so&rdquo;</em>), and he treats it as a sign of imminent arrest; idioventricular rhythm at 20&ndash;40 is not automatically agonal. No question keys the two as synonyms.</p></div>

  <h3 class="sub" id="es-junc-vs-ivr">12.5 &middot; Objective e &mdash; Junctional versus idioventricular rhythms</h3>
  <table>
    <tr><th></th><th>Junctional</th><th>Idioventricular</th></tr>
    <tr><td>Pacemaker</td><td>Atrioventricular node (compact zone)</td><td>Purkinje network</td></tr>
    <tr><td>Intrinsic rate</td><td>40&ndash;60 (accelerated 60&ndash;100, tachycardia over 100)</td><td>20&ndash;40 (accelerated 40&ndash;100)</td></tr>
    <tr><td>P waves</td><td>Absent, or inverted before or after the QRS</td><td>None</td></tr>
    <tr><td>QRS</td><td>Most commonly <strong>narrow</strong> (it still travels the normal pathway)</td><td><strong>Wide</strong>, over 0.12 seconds</td></tr>
    <tr><td>Regularity</td><td colspan="2">Both regular</td></tr>
  </table>

  <h3 class="sub" id="es-svt">12.6 &middot; Objective f &mdash; Recognizing the supraventricular dysrhythmias</h3>
  <p><strong>Atrial tachycardia in this deck is multifocal atrial tachycardia</strong>, presented with its slower twin, the wandering atrial pacemaker:</p>
  <table>
    <tr><th></th><th>Wandering atrial pacemaker</th><th>Multifocal atrial tachycardia</th></tr>
    <tr><td>Rate</td><td><strong>Under 100</strong></td><td><strong>Over 100</strong></td></tr>
    <tr><td>Regularity</td><td colspan="2">Irregular</td></tr>
    <tr><td>P waves</td><td colspan="2"><strong>At least three different morphologies</strong>, still married to the QRS</td></tr>
    <tr><td>PR interval</td><td colspan="2">Variable</td></tr>
    <tr><td>QRS</td><td colspan="2">Narrow or wide</td></tr>
  </table>
  {f12("l12-s011-wandering-atrial-pacemaker-diagram.png", "Four heart diagrams with the pacemaker at different atrial sites above a strip whose P waves vary.", "<b>Wandering atrial pacemaker.</b> At least three atrial sites compete; the P wave shape, PR and P to P intervals vary, and so do the R to R intervals.", 11)}
  {f12("l12-s013-wandering-atrial-pacemaker.jpg", "Pink grid strip of narrow complexes with P waves of varying shape at slightly uneven spacing.", "<b>Wandering atrial pacemaker, 60 per minute.</b> Three P wave shapes, irregular, under 100.", 13)}
  {f12("l12-s017-multifocal-atrial-tachycardia.jpg", "Strip titled multifocal atrial tachycardia with red arrows over P waves and the criteria printed beneath.", "<b>Multifocal atrial tachycardia.</b> At least three P wave shapes and an irregular rhythm over 100 per minute.", 17)}
  <p><strong>Atrial flutter.</strong> A rapid atrial rate from a <strong>reentry circuit</strong>, most often in the <strong>right atrium</strong>, set up by chamber enlargement or scarred or ischemic tissue. On paper it makes a {STAR}<strong>sawtooth pattern that is pathognomonic</strong></mark>. Flutter waves (F waves) replace P waves; there is no PR interval; the QRS is narrow or wide. The atrial rate is about 300 (the deck&rsquo;s range is 200&ndash;350); the ventricular rate depends on how many flutter waves pass for each QRS. <strong>Document the ratio</strong>: two flutter waves per QRS is atrial flutter with 2:1 ratio, three is 3:1. If the ratio changes, the rhythm is irregular and is documented as <strong>atrial flutter with variable conduction</strong>. To count, draw a line through the flutter-wave peaks and count the troughs to the next QRS; a notch at the end of the QRS counts as a flutter wave too.</p>
  {f12("l12-s023-atrial-flutter-circuit.png", "Heart cross-section with a looping arrow circulating in the right atrium, labeled signal circulating in atria.", "<b>The flutter circuit.</b> A reentry loop circulating in the right atrium.", 23)}
  {f12("l12-s024-atrial-flutter-sawtooth.jpg", "Strip with narrow complexes separated by a continuous pointed zigzag baseline.", "<b>Atrial flutter, 5:1.</b> The sawtooth baseline is pathognomonic; counting troughs (including the notch at the end of each QRS) gives five flutter waves per QRS.", 24)}
  {f12("l12-s030-atrial-flutter-variable-conduction.jpg", "Strip of four narrow complexes at unequal spacing over a rounded zigzag baseline.", "<b>Atrial flutter with variable conduction.</b> The flutter waves stay constant (atrial rate about 300) while the R to R intervals change.", 30)}
  <p><strong>Atrial fibrillation.</strong> The most treated cardiac arrhythmia: irregular electrical activity of <strong>multiple atrial sites</strong> that <strong>suppresses the sinoatrial node</strong>. The atria quiver instead of contracting, so the <strong>atrial kick is lost</strong>. No P waves, only <strong>fibrillatory (f) waves</strong>; the atrial rate is indeterminate and the ventricular rate variable; {STAR}<strong>irregularly irregular</strong></mark>; no PR interval; QRS narrow or wide. Three types: paroxysmal (converts without intervention), persistent (responds to drug or electrical cardioversion), permanent (chronic, does not respond).</p>
  {f12("l12-s032-atrial-fibrillation-diagram.jpg", "Two heart diagrams, typical rhythm with a single sinus impulse and atrial fibrillation with many irregular impulses, above matching strips.", "<b>Normal rhythm versus atrial fibrillation.</b> One organized sinus impulse against many chaotic atrial impulses; on the strip the P waves vanish and the rhythm becomes irregular.", 32)}
  {f12("l12-s034-atrial-fibrillation.jpg", "Strip of narrow complexes at unpredictable spacing over a wavy baseline with no distinct P waves.", "<b>Atrial fibrillation, ventricular rate 80&ndash;150.</b> No P waves, fibrillatory baseline, irregularly irregular.", 34)}
  <p><strong>Atrioventricular nodal reentrant tachycardia</strong>, commonly called <strong>supraventricular tachycardia</strong>: a regular, narrow-complex tachycardia from a <strong>reentry circuit</strong> over the slow and fast pathways, usually set off by an ectopic beat, typically a <strong>premature atrial complex</strong> near the fast (superior anterior) or slow (inferior posterior) tract. {STAR}<strong>Rate 150&ndash;300, regular, P waves not visible (or retrograde), no PR (or an RP interval), narrow QRS.</strong></mark></p>
  <ul>
    <li><strong>Typical</strong> (most common): the circuit runs counterclockwise <strong>down the slow tract and up the fast tract</strong>; no P waves, or retrograde P waves buried at the end of the QRS (<strong>pseudo S waves</strong>).</li>
    <li><strong>Atypical</strong> (rare): <strong>down the fast tract and up the slow</strong>; retrograde P waves are clearly visible, with an RP interval rather than a PR.</li>
  </ul>
  {f12("l12-s038-avnrt-circuit.png", "Diagram of the atrioventricular node region with a slow pathway and a fast pathway joined in a loop above the bundle of His.", "<b>The reentry circuit.</b> An impulse goes down one pathway and returns up the other, circling over and over.", 38)}
  {f12("l12-s039-pseudo-s-waves.png", "Strip of tall evenly spaced narrow complexes with a yellow highlight on the small notch ending each one.", "<b>Pseudo S waves.</b> In the typical form, retrograde P waves are buried at the end of the QRS.", 39)}
  {f12("l12-s041-avnrt.jpg", "Strip of very rapid evenly spaced narrow complexes with no visible P waves.", "<b>Atrioventricular nodal reentrant tachycardia, 200 per minute.</b> Regular, narrow, no visible P waves.", 41)}

  <h3 class="sub" id="es-svt-compare">12.7 &middot; Objective g &mdash; The supraventricular dysrhythmias compared</h3>
  <table>
    <tr><th></th><th>Atrial flutter</th><th>Atrial fibrillation</th><th>Supraventricular tachycardia (atrioventricular nodal reentry)</th><th>Atrial tachycardia (multifocal)</th></tr>
    <tr><td>Atrial activity</td><td><strong>Sawtooth flutter waves</strong>, about 300</td><td><strong>Fibrillatory waves</strong>, rate indeterminate</td><td><strong>Not visible</strong>, or retrograde</td><td><strong>P waves of three or more shapes</strong></td></tr>
    <tr><td>Ventricular rate</td><td>Set by the ratio</td><td>Variable</td><td>150&ndash;300</td><td>Over 100</td></tr>
    <tr><td>Regularity</td><td>Regular, or irregular with variable conduction</td><td><strong>Irregularly irregular</strong></td><td><strong>Regular</strong></td><td>Irregular</td></tr>
    <tr><td>PR</td><td>None</td><td>None</td><td>None (or RP)</td><td>Variable</td></tr>
    <tr><td>QRS</td><td>Narrow or wide</td><td>Narrow or wide</td><td>Narrow</td><td>Narrow or wide</td></tr>
  </table>
  <div class="pearl"><strong>The rate does not name the rhythm.</strong> A sinus P wave before every QRS at 190 is sinus tachycardia, not supraventricular tachycardia. The reentry tachycardia is the regular narrow one with <em>no visible</em> P waves, and if a single wave between rapid complexes could be a P or a T, call it a T.</div>

  <h3 class="sub" id="es-svt-physiology">12.8 &middot; Objective h &mdash; Anatomy and physiology of the supraventricular arrhythmias</h3>
  <ul>
    <li><strong>Premature atrial complexes</strong>: increased automaticity of an ectopic atrial site.</li>
    <li><strong>Wandering pacemaker and multifocal atrial tachycardia</strong>: at least three atrial sites competing to be the pacemaker, so the P wave shape keeps changing.</li>
    <li><strong>Atrial flutter</strong>: one reentry circuit, most often in the right atrium, in enlarged, scarred or ischemic tissue; the atrioventricular node lets only some flutter waves through, giving the ratio.</li>
    <li><strong>Atrial fibrillation</strong>: many atrial sites firing chaotically, suppressing the sinus node; loss of the atrial kick (the 20&ndash;30 percent of ventricular filling that is not passive, Lecture 11).</li>
    <li><strong>Atrioventricular nodal reentrant tachycardia</strong>: a reentry loop over a slow and a fast tract, started by a premature atrial complex; in the typical form down the slow tract and up the fast.</li>
    <li><strong>The atrioventricular node&rsquo;s three zones</strong>: the <strong>transition zone</strong> receives the sinus impulse and is very arrhythmogenic (most premature junctional complexes); the <strong>compact zone</strong> is the core that slows conduction to allow atrial contraction and ventricular filling, resembles the sinus node and can be the backup pacemaker; the <strong>trigger zone</strong> sends the signal down the His bundle.</li>
  </ul>
  <div class="callout warn"><p><strong>Where the deck&rsquo;s wording is loose.</strong> (1) Slide 5 lists &ldquo;Multifocal atrial pacemaker (MAT)&rdquo;; the rhythm is multifocal atrial <em>tachycardia</em> (slide 17 has it right). (2) Slide 5 also files atrioventricular nodal reentrant tachycardia under &ldquo;atrial rhythms&rdquo;; its circuit is nodal. (3) Slide 38 places the circuit &ldquo;in between the internodal pathways of the sinus node and the AV (atrioventricular) node&rdquo;; current teaching puts its slow and fast pathways in and around the atrioventricular node itself. The quizzes key only what both say: a reentry circuit over a slow and a fast pathway, started by an ectopic beat. (4) &ldquo;Supraventricular&rdquo; strictly means any rhythm from above the ventricles; the deck and the lecturer use <em>supraventricular tachycardia</em> for this one reentry rhythm, and so do the quizzes. (5) Slide 70 calls six premature ventricular complexes in a row &ldquo;a run of V-tach&rdquo; that requires intervention; the usual definition of ventricular tachycardia is three or more consecutive ventricular beats, so no question asks the number, and a brief (nonsustained) run calls for evaluation rather than automatic treatment. (6) Slide 27&rsquo;s flutter atrial rate of 200&ndash;350 is wider than the classic 250&ndash;350; both worked strips sit at about 300. (7) Slide 38 says <em>all</em> cases of atrioventricular nodal reentrant tachycardia are triggered by an ectopic focus such as a premature atrial complex; a premature atrial complex is the usual trigger, but not the only one, so the quizzes say &ldquo;usually&rdquo;.</p></div>
</section>
'''


def main():
    os.makedirs(OUT, exist_ok=True)
    for name, html in (("l11_guide.html", L11), ("l12_guide.html", L12)):
        assert html.count("<section") == 1 and html.count("</section>") == 1
        assert not re.search(r"\b(colour|tumour|oedema|haem|anaem|centre|behaviour|recognise|organise)", html), name
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
        print("wrote tools/pdm_e3/%s  %d subsections, %d figures, %d starred" % (
            name, html.count('<h3 class="sub"'), html.count('<figure class="fig">'), html.count("prof-highlight")))


if __name__ == "__main__":
    main()
