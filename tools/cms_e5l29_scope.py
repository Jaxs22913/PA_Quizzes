# -*- coding: utf-8 -*-
"""Lecture 29 scope -- Arrhythmias I: Supraventricular (Elwaya), CMS I Exam 5.

Read by cms_e5_partition.py (guards) and imported by every Lecture 29 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Ayelet Elwaya, MSHS, PA-C, CAQ-EM -- the deck's title slide; the 2026-10-12 recording
(Notability, two segments, 45.6 + 57.9 min) is an emergency-medicine PA speaking ("I'll see you in
the ER", the class's EKG course taught by Mr. Mathis that week). Matches calendar-data.js.

Built from the deck (2026-10-15). The recording sets EMPHASIS and SCOPE only, never content
(slides-only grounding). Notability's text only so far; our own Whisper transcript is pending, and
anything garbled is marked RECHECK below and never keyed.

WHAT SHE SAID THE EXAM IS (segment 1, opening):
  "I don't think I had that many 'what is this EKG' questions last year ... It was more like you
  see this EKG, what would you do? Or what is a risk factor for this EKG?" -- so the vignette sets
  lead with management and risk factors, and the rhythm itself is a minority lead-in.
  "You are responsible for medications ... first line, second line ... you're not responsible for
  the dose" -- drugs keyed by name, never a dose (the partition's dosing guard already holds).

WHAT SHE EMPHASIZED (REQUIRED below puts each in every form):
  Wolff-Parkinson-White: "a very important point", "this was a high miss last year on an exam",
      "the history here is really important". Adenosine slowing a tachycardia that then shows a
      delta wave / pre-excited atrial fibrillation -> procainamide, never adenosine; definitive
      treatment is ablation of the accessory pathway; the classic first presentation is a young
      person collapsing during sport. The delta wave shows only in sinus rhythm (pre-excitation),
      not during the tachycardia.
  Stable supraventricular tachycardia: "listen, open your ears, vagal maneuver" first, then
      adenosine (may be repeated once); unstable -> synchronized cardioversion.
  Tachy-brady syndrome: "by far the most common" form of sick sinus syndrome, and the tachycardia
      is "usually atrial fibrillation" (said about six times; "in a tachy-brady syndrome, what is
      the most likely tachycardic rhythm? You will see").
  Symptomatic, unstable bradycardia: "you do need to know that atropine is the first one", then a
      temporary pacemaker, then a permanent pacemaker.
  Atrial fibrillation and flutter: "goal number one ... is always, always, always, always rate
      control"; anticoagulation is step two; cardioversion only after 21 days of anticoagulation.
  Atrial fibrillation with Wolff-Parkinson-White: "if it ever comes up, what is the worst
      combination?"

WHAT SHE CAPPED (never keyed):
  The anticoagulation score TABLES (slide 51): "I'm not going to make you memorize this. Please
      don't memorize this." She wants what each score means (stroke risk vs bleeding risk) and the
      low-risk line (0 for men, 1 for women). Slide 51 is excluded; no component points are keyed.
  Premature junctional contractions: "I will not hold you accountable of where in the AV node will
      give you what morphology. I just want you to know it can come from three different locations
      top, middle, bottom" -- the location -> P-wave-position mapping (s59/s62) is never keyed.
  The narrow-complex algorithm (s27): "There is a whole algorithm ... I did not need you to
      memorize it." Excluded.
  Triggers of reentry (accessory pathway physiology): "I'm not gonna bother you with the triggers."

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 16, "Arrhythmias 1: Atrial or
Supraventricular Dysrhythmias", read with PyMuPDF on 2026-10-15), the syllabus's own lettering kept
and only the leading "1." dropped, as in the Lecture 26-28 scopes.
  IO_A    the nine supraventricular rhythms.
  IO_POP  adult and elderly (the deck's age content: sinus bradycardia in adults over 65 s13,
          symptoms worse in the elderly s25, "elderly" among atrial fibrillation risks s48).
  IO_L30  JUNCTIONAL RHYTHM is taught on THIS deck (s59-64, premature junctional contractions and
          junctional rhythm) but the syllabus files "h. Junctional rhythm" under the Lecture 30
          objective (Arrhythmias 2: Ventricular Dysrhythmias). Those questions carry that Lecture 30
          objective, verbatim, and cite this deck.

EXCLUDED_SLIDES (never cited):
  1, 2     title (cartoon) and the objectives slide
  27       the UpToDate narrow-complex algorithm she said not to memorize (it names "SANRT", which no
           other slide teaches)
  51       the CHA2DS2-VASc and HAS-BLED component tables (see the cap above)
  55       four unlabeled premature-beat strips with no text

IMAGE-ONLY content (in no text form; keyed only where it repeats or completes a text slide):
  s4  paper speed and box values (small box 0.04 s, large box 0.20 s) and the 300-150-100-75-60-50
      count-off; s10 sinus arrhythmia strip labeled faster with "breathe in"; s34 pre-excitation vs
      orthodromic (antegrade through the atrioventricular node, normal QRS, no delta wave,
      retrograde P after the QRS) vs antidromic (retrograde through the node, wide QRS with delta
      wave); s43 flutter waves with 2:1, 3:1 and 4:1 block; s53 ventricular tachycardia (regular,
      150-200) vs atrial fibrillation with Wolff-Parkinson-White (irregular, rates approach 300).

CONTESTED or WRONG on the slides, so NEVER KEYED (truth noted; the guide carries the discrepancy):
  s50 "HAS-BLED score 3 and up, no AC" (and the audio: "greater than three, I'm not going to
      anticoagulate"). NOT TRUE: a HAS-BLED (bleeding risk) score of 3 or more marks high bleeding
      risk -- correct the modifiable risks and follow closely -- and is not by itself a reason to
      withhold anticoagulation (ACC/AHA/ACCP/HRS 2023; ESC 2020/2024). Only "the score estimates
      bleeding risk" is keyed.
  s49 "Anticoagulation for all" vs s50 "0 for men or 1 for women = low risk. May not require AC".
      Truth is s50: anticoagulation follows the stroke-risk score. "For all" is never keyed.
  s24 "All are also REGULAR tachycardias, except for atrial fibrillation, and variable conduction
      subtype of atrial flutter" -- but s28 (and truth) make multifocal atrial tachycardia
      IRREGULAR. Multifocal is keyed irregular; the s24 sentence is never keyed.
  s28 table gives multifocal atrial tachycardia a "constant" PR interval; truth: the PR varies with
      the changing P waves. Never keyed.
  s33 calls atrioventricular reentrant tachycardia "a reentry circuit within the AV node through an
      accessory pathway". Truth (and s34, s38): the reentrant loop uses the atrioventricular node
      AND the accessory pathway; a circuit WITHIN the node is nodal reentry (s38). Keyed that way.
  s33 table "QRS narrow, < 0.12 +/- delta wave" vs s35 "Wide QRS > 0.1 sec": the orthodromic
      tachycardia is narrow, the resting pre-excited beat is widened by the delta wave. The s35
      "0.1 sec" figure is loose (the usual criterion is about 0.11-0.12 s) and no QRS number is
      keyed for Wolff-Parkinson-White.
  s37 "If WPW is known ... IV procainamide should be used - NEVER adenosine" (and the audio). The
      guideline position (ACC/AHA/HRS 2015 supraventricular tachycardia) is narrower: vagal
      maneuvers and adenosine remain acceptable for ORTHODROMIC reentry (with a defibrillator at
      hand), while ALL atrioventricular nodal blockers -- adenosine, beta blockers, calcium channel
      blockers, digoxin -- are contraindicated in PRE-EXCITED ATRIAL FIBRILLATION, which gets
      procainamide (or cardioversion). Stems therefore key procainamide only where both agree:
      pre-excited atrial fibrillation, or adenosine slowing a tachycardia to reveal it (the s37
      wording). A known-Wolff-Parkinson-White patient with a REGULAR narrow tachycardia is never
      used as a "never adenosine" stem.
  Rates across slides do not agree: supraventricular tachycardia ">160" (s23) vs nodal reentry
      "usually 140 to 180" (s38) vs reentrant tachycardia "usually 200-300" (s33) vs focal/
      multifocal "usually 150-250" (s28). No stem sits near a boundary and no reentry rate band is
      keyed; sinus tachycardia's ceiling of 160 (s14, and the audio) is keyed.
  s5 normal QRS "Duration: 0.12s OR 3 small boxes" vs s7 "Narrow, < 0.12": keyed as < 0.12 s only.
  s42 atrial flutter table "PR interval 0.12-0.20, constant": there is no true PR interval in
      flutter (flutter waves replace P waves). Never keyed.
  s32 multifocal: "BB or non-DHP CCB (not suitable for long term, increases mortality in heart
      failure patients)" -- ambiguous (beta blockers LOWER mortality in heart failure with reduced
      ejection fraction; nondihydropyridine calcium channel blockers are the class to avoid there).
      Only "treat the underlying condition" and "inpatient, short-term rate control" are keyed.
  Audio, s9 mechanism: she explains sinus arrhythmia as a conduction "lag" from intrathoracic
      pressure; the slide (and truth) is rate change with breathing -- faster on inspiration,
      slower on expiration. The slide is keyed; the audio's mechanism is not.
  Audio, s54 ratios: she describes bigeminy/trigeminy with muddled ratios; the slide's "every other
      beat = bigeminy, every third beat = trigeminy" is keyed.

RECHECK against our own transcript when it lands (Notability text garbled, nothing keyed on it):
  segment 2 end, junctional rhythm from digoxin toxicity: "I'm gonna hold you accountable for some
      immune sound. Because I don't even remember that by heart" -- whether she does or does NOT
      hold the class to digoxin immune Fab. Until rechecked, digoxin immune Fab appears only in
      explanations, never as a key.
  segment 1, the asymptomatic-bradycardia "under 30 beats per minute" figure ("don't hold me to that
      number") -- never keyed.
"""

DECK = "arrhythmias I - Elwaya-2.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)

IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing (including ordering and interpretation), management "
        "(acute and chronic, including applicable rehabilitative and palliative care), appropriate "
        "referrals, patient education, and prognosis of the following atrial and supraventricular "
        "dysrhythmias: a. Sinus arrhythmia b. Sinus bradycardia c. Sinus tachycardia d. Sick sinus "
        "syndrome e. Atrial premature beats f. Atrial flutter g. Atrial fibrillation h. Atrial "
        "tachycardia i. Paroxysmal supraventricular tachycardia")
IO_POP = ("Identify medical care strategies for atrial and supraventricular dysrhythmias for the "
          "following populations. 3. adult 4. elderly")
# Lecture 30's objective, verbatim: junctional rhythm is taught on this deck (s59-64).
IO_L30 = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
          "differential diagnosis, diagnostic testing (including ordering and interpretation), management "
          "(acute and chronic, including applicable rehabilitative and palliative care), appropriate "
          "referrals, patient education, and prognosis of the following ventricular dysrhythmias: "
          "a. Atrioventricular block b. Bundle branch blocks c. Ventricular premature beats "
          "d. Ventricular tachycardia e. Ventricular fibrillation f. Torsades de Pointes "
          "g. Idioventricular rhythm h. Junctional rhythm i. QT prolongation")
IOS = [IO_A, IO_POP, IO_L30]

EXCLUDED_SLIDES = {1, 2, 27, 51, 55}

SCOPE_BANNED = [
    r"HAS-BLED[^?]{0,80}\b(?:3|three)\b",          # s50's withholding threshold -- not true
    r"anticoagulat\w* (?:for all|every patient|all patients)",
    r"regular tachycardias,? except",               # s24's blanket rule (multifocal is irregular)
    r"\bSANRT\b|sinoatrial nodal reentr",           # only on the excluded algorithm
    r"0\.1 sec|>\s?0\.10?\s?s",                     # s35's loose QRS figure
    r"increases? mortality",                        # s32's ambiguous parenthesis
    r"(?:top|middle|bottom) of the atrioventricular node",   # PJC location mapping: capped
    r"bundle of kent[^?]{0,60}trigger|trigger[^?]{0,60}bundle of kent",
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "delta wave": "slurred",                 # s35: slurred upstroke of the QRS complex
    "flutter waves": "sawtooth",             # s42: sawtooth (flutter) waves
    "frog sign": "neck",                     # s40: "neck pulsations"
    "bigeminy": "every other beat",          # s54
    "trigeminy": "every third beat",         # s54
    "pre-excitation": "short pr",            # s33: short PR interval and delta wave
    "tachy-brady": "alternat",               # s18: tachyarrhythmia alternates with bradycardia
    "retrograde p": "inverted",              # s59/s62: inverted in II, III, aVF
}

# Content she said WILL be tested, as (label, stem regex, key regex, minimum per form).
REQUIRED = [
    ("Wolff-Parkinson-White -> procainamide", r"wolff|delta wave|pre-excit|accessory pathway",
     r"procainamide", 1),
    ("stable supraventricular tachycardia -> vagal maneuver first", r"supraventricular|narrow",
     r"vagal", 1),
    ("tachy-brady -> atrial fibrillation", r"tachy-brady|alternat", r"atrial fibrillation", 1),
    ("symptomatic bradycardia -> atropine", r"bradycardi|slow", r"atropine", 1),
    ("atrial fibrillation/flutter -> rate control first", r"atrial fibrillation|flutter",
     r"rate control|beta blocker|calcium channel blocker|diltiazem|metoprolol|verapamil", 1),
]
