# -*- coding: utf-8 -*-
"""Lecture 30 scope -- Arrhythmias II: Blocks and Ventriculars (Elwaya), CMS I Exam 5.

Read by cms_e5_partition.py (guards) and imported by every Lecture 30 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Ayelet Elwaya, MSHS, PA-C, CAQ-EM -- the deck's title slide, and the
2026-10-12 afternoon recording (two Notability clips, 46.0 + 50.7 min) is her
voice continuing the morning's Arrhythmias I. calendar-data.js also names
Professor Elwaya: no conflict.

Built from the SLIDES (every picture viewed 2026-10-15), with the audio used only
for emphasis and scope (Notability's transcript; our own Whisper pass was still
running). The audio never adds content the deck lacks.

WHAT SHE SAID ABOUT THE EXAM (both lectures, L29 opening):
  "you see this EKG, what would you do? or what is a risk factor for this EKG?"
      -- not "what is this EKG"; the CMS goal is who gets it, why, what to do.
  Medications ARE tested ("first line, second line ... you do need to know
      them"); doses are NOT ("you're not responsible for the dose"). The doses
      left on s44 (picture) and s50 are reference only.
  Risk factors: "I will not sit here and read to you the risk factors ... I do
      expect you to know some ... especially when I have like most common."
  Mobitz II / complete block: "I'm not going to ask you about those two meds"
      (atropine, epinephrine -- the guideline is changing) "But you do need to
      know that emergently ... pace them and take them to a permanent pacer."
  PVCs: "if there is anything that you want to highlight today, is that the main
      reason people have PVCs is hypoxia and hypoxemia or some sort of
      electrolyte imbalance."
  Polymorphic ventricular tachycardia: "the point that I've been beating to
      death ... there is no such thing as stable [polymorphic] VTAC" ->
      defibrillate even with a pulse.
  Torsades: "Mag, mag and more mag" (the slide says the same).
  QT drug list (s42): "I will not ask you which [drug] ... because of this.
      That's cheating" -- no question keys a drug from that list.
  The septal-infarction-in-bundle-branch-block aside: "You will not be
      responsible for this." The arrest algorithm (s51): "I'm not going to make
      you memorize it."
  REQUIRED below puts one of each of the first four in every form.

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 16,
"Arrhythmias 2: Ventricular Dysrhythmias", read with PyMuPDF 2026-10-15), the
syllabus's lettering kept inline and only the leading "1." / "2." dropped.
  IO_A   the nine dysrhythmias. Sudden cardiac death, the implantable
         defibrillator, asystole and pulseless electrical activity sit under
         ventricular tachycardia / fibrillation management and carry IO_A.
  IO_POP adult, elderly: questions test what the deck says about age
         (degenerative conduction disease of old age) and patient groups
         (high- vs low-risk PVC patients, coronary disease and sudden death).
  GAPS: "g. Idioventricular rhythm" is on NO slide of this deck (text or
         picture) -- no questions; the guide records the gap. "h. Junctional
         rhythm" is taught on the Arrhythmias I deck (slides 59-64), so the
         Lecture 29 pools carry it under this objective.

EXCLUDED_SLIDES (never cited):
  1, 3      title cartoon and section cartoon
  19        "Heart Block Poem" picture (a mnemonic; keyed facts come from s4-s18)
  34        four unlabeled ectopic-beat strips
  51        2020 adult cardiac arrest algorithm picture -- "not going to make you
            memorize it"; its facts are keyed only where s50/s55 say them in text
  54        four unlabeled "Rhythm 1-4" practice strips

PICTURE-ONLY CONTENT (cited by slide number):
  s22  conduction system: SA node, AV node, His bundle, left bundle with anterior
       and posterior fascicles, right bundle, Purkinje fibers.
  s38  the implantable defibrillator's parts (pulse generator, right
       ventricular coil, sensing/pacing electrodes).
  s44  "Antiarrhythmic infusions for stable wide-QRS tachycardia": doses (out),
       and "procainamide ... Avoid if prolonged QT or CHF" (keyed, no dose).
  s49  coarse and fine ventricular fibrillation strips.

CONTESTED on the slides, or wrong, so handled as noted (truth wins):
  QRS width in bundle branch block: s21's table says "Wide (> 0.20)"; s24 and
      s29 say > 0.12. Truth: complete bundle branch block is a QRS of 0.12 s
      (120 ms) or more. Keyed as 0.12; never 0.20; stems use 0.16 s.
  Left bundle branch block leads: s23 says the vector is "seen best in I, II, V5
      and V6". Lead II is an inferior lead; the lateral leads are I, aVL, V5,
      V6 (s24's own "absent Q waves in I, V5, V6"). Lead II is never keyed.
  New left bundle branch block: s27 "should always be considered a sign of
      pathology (STEMI equivalent)". The audio says the guideline changed about
      six weeks before the lecture: a new left bundle branch block is now worked
      up as unstable angina (troponins), and the catheterization team is called
      only if the troponins rise. Current guidance agrees that a new left bundle
      branch block alone is no longer a ST-elevation equivalent. Keyed only as
      "a sign of pathology that needs a workup"; "equivalent" is banned.
  Atropine and epinephrine for Mobitz II and complete block (s14, s18): "no
      longer contraindicated but highly controversial". She will not test
      them. Never keyed either way; transcutaneous
      pacing (emergent) and a permanent pacemaker (definitive) are keyed.
  First-degree block pacing (s6): "Consider permanent pacemaker for symptomatic
      patients or patients with PR interval greater than 0.3 sec". Truth: pacing
      is for symptoms attributable to marked PR prolongation, not a long PR
      alone. Keyed only for the symptomatic patient. Hypokalemia as a cause of
      first-degree block (s6) is not keyed.
  Non-sustained ventricular tachycardia after a failed beta blocker (s43):
      catheter ablation "a primary alternative" to antiarrhythmics, the audio
      went straight to amiodarone. Ablation and an antiarrhythmic are never
      set against each other as key and distractor.
  Torsades and beta blockers (s47): avoided in torsades because bradycardia
      lengthens the QT. True for acquired, pause-dependent torsades; congenital
      long QT syndrome is a different story the deck does not tell. Keyed only
      for the acquired, drug-induced case.
  Calcium gluconate and sodium bicarbonate in arrest (s50, "consider"): not
      routine in current resuscitation guidance; never keyed.
  The order of epinephrine and amiodarone against the shock count differs
      between s50's text and the s51 picture; no question keys a shock count.
  "Aka automated ICD (AICD)" (s38): not keyed.
  Mobitz type I and exertion (s9): "Symptoms usually appear in individual with
      exertion inducing heart block". Truth: exertion speeds atrioventricular
      nodal conduction, so typical Mobitz type I improves with exercise; a block
      that appears with exertion suggests disease below the node. Exertion is
      not keyed as the trigger (2026-10-15 fact-check): the two items now key
      "usually asymptomatic" (pool A) and "symptoms make her a pacemaker
      candidate" (vignettes A).
  P waves in ventricular tachycardia (s39 table "None"): P waves are often
      present but dissociated from the QRS and hard to see. No key turns on it;
      explanations say P waves are "not tied to the QRS".
"""

DECK = "Arrhythmias II - Elwaya  (1).pptx"     # two spaces, as the filename has
C = lambda n: "%s, Slide %d" % (DECK, n)

IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing (including ordering and interpretation), management "
        "(acute and chronic, including applicable rehabilitative and palliative care), appropriate "
        "referrals, patient education, and prognosis of the following ventricular dysrhythmias: "
        "a. Atrioventricular block b. Bundle branch blocks c. Ventricular premature beats d. Ventricular "
        "tachycardia e. Ventricular fibrillation f. Torsades de Pointes g. Idioventricular rhythm "
        "h. Junctional rhythm i. QT prolongation")
IO_POP = ("Identify medical care strategies for ventricular dysrhythmias for the following populations. "
          "3. adult 4. elderly")
IOS = [IO_A, IO_POP]

EXCLUDED_SLIDES = {1, 3, 19, 34, 51, 54}

SCOPE_BANNED = [
    r"\batropine\b",
    r"equivalent",
    r"QRS (?:duration |width )?(?:of |is |over |above |greater than |more than |> ?)0\.2\d?\b",  # s21 "> 0.20"
    r"calcium gluconate|bicarbonate",
    r"\bseptal (?:myocardial )?infarction",      # the not-responsible aside
    r"citalopram|escitalopram|haloperidol|droperidol|chlorpromazine|ziprasidone|olanzapine|"
    r"risperidone|clozapine|quetiapine|clarithromycin|erythromycin|fluoroquinolone|fluconazole|"
    r"methadone|ondansetron|propofol|kinase inhibitor|tricyclic",
]

# Named findings in vignette stems carry their description in parentheses.
NAMED = {
    "wenckebach": "longer",                 # s7: PR progressively longer, then a dropped beat
    "stokes": "faint",                      # s13: sudden fainting spell or seizure
    "bunny ears": "second upward",          # s28: rsR' pattern
    "rsr'": "second upward",
    "torsades": "twist",                    # s40: QRS complexes appear to twist around the baseline
    "bigeminy": "every other beat",         # s33
    "trigeminy": "every third beat",        # s33
    "delta wave": "slurred",
    "lyme carditis": "tick",
    "lenègre": "fibro",
}

# Content she said WILL be tested, as (label, stem regex, key regex, minimum per form).
REQUIRED = [
    ("Pacing for Mobitz II and complete block", r"mobitz type ii|complete (?:heart |atrioventricular )?block|third-degree"
     r"|no qrs|not followed by a qrs|no relationship|dissociat|unrelated", r"pac(?:ing|emaker)", 1),
    ("PVCs: hypoxemia and electrolytes", r"premature ventricular|wide,? early|early,? wide|extra beat|skipped",
     r"hypox|electrolyte|potassium|magnesium", 1),
    ("Polymorphic ventricular tachycardia: defibrillate", r"polymorphic|vary in shape|varying shape|changing shape"
     r"|differ(?:s|ing)? in shape|shapes? (?:vary|varies|change)", r"defibrillat", 1),
    ("Torsades: magnesium", r"torsades|twist", r"magnesium", 1),
]
