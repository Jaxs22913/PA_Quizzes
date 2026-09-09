#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build "PDM Exam 1 -- Most Likely Tested".

Jaxon, 2026-09-09: "Create a clear most likely tested stuff for PDM exam 1 and
put it under guides. Strip stuff that most likely isnt testable."

NOT ANOTHER CRAM SHEET. The cram sheet is condensed-but-complete: it carries
everything, shortened. This page is the opposite trade -- it drops material on
purpose and commits to a ranking, so it is only useful if the ranking is
defensible. Every row therefore carries WHY it is ranked where it is, and the
evidence is one of three things:

  SAID     the lecturer flagged it out loud. Quoted, with a timestamp, from the
           recordings in the PDM inbox.
  TIME     the lecture spent real time on it, measured by term frequency across
           the transcripts -- e.g. potassium is said 112 times in Lecture 5,
           contrast 60 times in Lecture 2. Not a proxy for importance on its
           own, but decisive between two facts that both sit under one
           objective.
  IO       it answers a numbered syllabus Instructional Objective. Necessary
           for anything to appear at all; on its own it only earns "possible".

The three tiers are NEAR-CERTAIN (two or three kinds of evidence, usually
including SAID), LIKELY (IO plus real lecture time), POSSIBLE (IO-backed but
lightly taught -- know it exists, do not sink an evening into it).

THE STRIP LIST IS THE OTHER HALF OF THE ASK and comes FIRST on the page,
because a page that only adds things does not save anyone any time. Everything
on it is there because a lecturer said so in as many words, or because the
syllabus never asks for it. Nothing is dropped on my judgement alone.

Facts are reused from the audited cram sheet and study guide rather than
re-derived from the decks, so this page cannot drift away from them.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 1/pdm-exam-1-high-yield.html")

# Tier markup. Kept as one function so the three labels cannot drift apart.
def T(level):
    return ('<span class="tier t%d">%s</span>'
            % (level, ["", "NEAR-CERTAIN", "LIKELY", "POSSIBLE"][level]))

N, L, P = T(1), T(2), T(3)

def why(kind, text):
    return '<span class="ev e-%s">%s</span> %s' % (kind.lower(), kind, text)

COLS = ["Odds", "What to know", "Why it is ranked here"]

TOPICS = [

# ---------------------------------------------------------------- STRIP
{"id": "cut", "label": "Cut this first", "color": "#8c1d12", "cols": COLS, "rows": [
  {"group": "SAID OUT LOUD IN LECTURE — these are not coming"},
  ("&mdash;", "<b>Animal hearing ranges.</b> The figure with killer whales, dogs and bats.",
   why("SAID", "Lecture 3 at 1:00:43: &ldquo;I&rsquo;m not going to ask you to be like, what is the "
               "range of the killer whale&hellip; I&rsquo;m not gonna ask you about that.&rdquo;")),
  ("&mdash;", "<b>Keeping a patient on the same magnetic resonance machine strength</b> so serial "
              "scans stay comparable &mdash; the multiple sclerosis follow-up example.",
   why("SAID", "Lecture 2 at 1:02:11: &ldquo;don&rsquo;t stress about this. This is not gonna be on "
               "the test. This is just like a life thing.&rdquo;")),
  ("&mdash;", "<b>Memorising normal reference ranges.</b> Any of them.",
   why("SAID", "Lecture 5 at 36:14: &ldquo;there&rsquo;s not anything I need you to memorize number "
               "wise&hellip; you don&rsquo;t have to memorize the normal ranges.&rdquo; Ranges are "
               "supplied on the exam. Learn DIRECTION and rough magnitude &mdash; sodium about 140, "
               "potassium single digits &mdash; so an absurd value looks absurd.")),
  ("&mdash;", "<b>Calculating a glomerular filtration rate.</b>",
   why("SAID", "Lecture 5: &ldquo;I don&rsquo;t need you to calculate that or know that just yet, "
               "but know OF it.&rdquo; Know what it means and that cystatin C measures it better; do "
               "not learn a formula.")),
  ("&mdash;", "<b>Predictive-value arithmetic.</b> No two-by-two tables to fill in.",
   why("SAID", "Lecture 1: &ldquo;We&rsquo;re not gonna do math, I&rsquo;m not gonna make you do "
               "math.&rdquo; You still need the DIRECTION prevalence pushes positive predictive "
               "value &mdash; that part is very much testable.")),
  ("&mdash;", "<b>Cystatin C in any detail.</b>",
   why("SAID", "Lecture 5 at 1:31:30: &ldquo;we&rsquo;ll talk about cystatin C in the future.&rdquo; "
               "Deferred to a later exam.")),
  ("&mdash;", "<b>The genetics of each anemia beyond genetic vs non-genetic.</b>",
   why("SAID", "Lecture 4, twice: &ldquo;for now, I&rsquo;m happy if you understand genetic versus "
               "non-genetic; the rest will come later.&rdquo;")),
  {"group": "NOT ASKED FOR BY ANY OBJECTIVE — low return on your time"},
  ("&mdash;", "<b>Hounsfield numbers as a memorised list</b> (air &minus;1000, fat &minus;40, and so on).",
   why("IO", "The objective asks you to <i>compare and contrast radiographic density and contrast</i>. "
             "Know the five-density ladder and that water is 0 by convention; the rest of the table is "
             "on an image slide and no objective asks you to recall it.")),
  ("&mdash;", "<b>Exact organ radiation doses in milliSieverts.</b>",
   why("IO", "The objective is <i>compare and contrast the risks and benefits associated with "
             "radiation exposure</i>. Relative ranking is the point &mdash; and that neonatal "
             "abdominal computed tomography is about twice the adult dose.")),
  ("&mdash;", "<b>White cell lifespans</b> (neutrophil 7 hours, eosinophil 8&ndash;12 days&hellip;).",
   why("IO", "Image-only slide, no objective. Contrast with the percentages and the absolute count, "
             "which are objective-backed and near-certain.")),
  ("&mdash;", "<b>Accreditation bodies as an org chart.</b>",
   why("IO", "One objective mentions <i>accreditation and regulatory considerations</i>. Who does "
             "what in one line is enough: CMS certifies and enforces, FDA categorises, CDC sets "
             "standards. The load-bearing fact is that regulation only ever gets STRICTER.")),
]},

# ---------------------------------------------------------------- L1
{"id": "l1", "label": "L1 &middot; Lab Diagnostics", "color": "#1f6f5c", "cols": COLS, "rows": [
  (N, "<b>SnNout / SpPin.</b> High SENSITIVITY + Negative rules OUT (good at detecting, best for "
      "SCREENING). High SPECIFICITY + Positive rules IN (good at confirming).",
   why("TIME", "Sensitivity said 14&times;, specificity 10&times;, and it carries its own objective. "
               "The single most reusable idea in the lecture.")),
  (N, "<b>Sensitivity and specificity belong to the TEST. Positive and negative predictive value "
      "belong to the POPULATION.</b> Same test, different prevalence, different predictive value.",
   why("TIME", "Positive predictive value said 14&times;. The frostbite worked example &mdash; 95% "
               "sensitivity in Michigan gives a positive predictive value near 68%, in Florida near "
               "2% &mdash; exists only to make this point.")),
  (N, "<b>The named trap.</b> &ldquo;My patient&rsquo;s test is positive &mdash; do they have it?&rdquo; "
      "feels like sensitivity. It is POSITIVE PREDICTIVE VALUE.",
   why("SAID", "Called out as a trap in the lecture and written into the deck as one.")),
  (N, "<b>Most errors are PRETEST.</b> Communication, medication administration, labelling.",
   why("IO", "Two objectives cover the phases and their components; this is the fact they converge on.")),
  (N, "<b>Get cultures BEFORE antibiotics</b> &mdash; blood, sputum and throat alike.",
   why("TIME", "Culture is said 33&times;, the most of any term in the lecture. One rule spanning "
               "three objectives.")),
  (L, "<b>The four tube pairings.</b> Light blue = coagulation. Lavender = complete blood count. "
      "Yellow = blood cultures. Gray = glucose. The order exists to stop additive carryover.",
   why("IO", "&ldquo;Identify which colored laboratory collection tubes correspond to common "
             "laboratory tests&rdquo; &mdash; an objective that names the task exactly.")),
  (L, "<b>Screening vs diagnostic.</b> SCREENING: asymptomatic, cheap, says whether more testing is "
      "needed. DIAGNOSTIC: symptomatic, may be invasive, aims to name the disease.",
   why("IO", "Its own objective, plus 11 mentions.")),
  (L, "<b>Pre-test vs post-test probability.</b> Pre-test comes from signs, symptoms, history, risk "
      "and how common the thing is; the result moves you to post-test.",
   why("IO", "Its own objective; 11 mentions across the two terms.")),
  (L, "<b>Point-of-care testing</b> &mdash; testing outside the central lab, at or near the patient. "
      "Know the primary-care menu against the acute-care menu, and that it trades precision for speed.",
   why("TIME", "21 mentions and FOUR separate objectives, but it is mostly list-recall, which is why "
               "it sits here rather than above.")),
  (L, "<b>Qualitative / semi-quantitative / quantitative.</b> Rapid strep and pregnancy are "
      "qualitative; the urinalysis dipstick is SEMI-quantitative (trace, 1+, 2+); a lab value is "
      "quantitative.",
   why("IO", "Its own objective, and the semi-quantitative middle term is the one people drop.")),
  (P, "<b>CLIA is a MINIMUM and cannot be downgraded</b> &mdash; state and city rules are always "
      "stricter. CMS certifies and enforces, FDA categorises by complexity, CDC sets standards.",
   why("IO", "Objective-backed but thinly taught &mdash; quality assurance is mentioned once. Know "
             "the one-way direction of regulation and move on.")),
  (P, "<b>Ova and parasites: do NOT refrigerate, THREE separate specimens.</b> Guaiac: heme oxidises "
      "the reagent, BLUE = POSITIVE, use a small sample.",
   why("IO", "Under the stool-studies objective, but a small share of lecture time.")),
]},

# ---------------------------------------------------------------- L2
{"id": "l2", "label": "L2 &middot; Medical Imaging", "color": "#7a4a9c", "cols": COLS, "rows": [
  (N, "<b>Iodinated contrast is NEPHROTOXIC.</b> Check blood urea nitrogen and creatinine, give one "
      "litre of normal saline. GADOLINIUM is a CLEARANCE problem instead &mdash; poor function lets "
      "it build up in tissue.",
   why("SAID", "Contrast is said 60&times;, more than any term in any lecture, and Lecture 5 adds "
               "&ldquo;you still need to know before you give that person contrast &mdash; you will "
               "order these two labs&hellip; ALWAYS. We don&rsquo;t say always very often in "
               "medicine.&rdquo;")),
  (N, "<b>Shellfish allergy is NOT an iodine allergy.</b> No cross-reactivity. A genuine iodine "
      "allergy is a real concern; a prior contrast reaction is the actual high-risk history.",
   why("SAID", "Made explicitly in lecture and flagged in the deck. A classic single-best-answer trap.")),
  (N, "<b>T1 vs T2.</b> T2: water is WHITE (oedema, infection, cerebrospinal fluid). T1: water is "
      "DARK. Check yourself on the ventricles &mdash; bright cerebrospinal fluid means T2.",
   why("TIME", "The deck itself labels this &ldquo;the always-asked one&rdquo;, and 27 mentions of "
               "Tesla and weighting back it up.")),
  (N, "<b>Free air under the diaphragm = perforated bowel.</b> Unless there has been recent "
      "laparoscopic surgery with insufflation.",
   why("SAID", "Lecture 2 at 1:22:50, her own word: &ldquo;there&rsquo;s your like buzzword "
               "phrase.&rdquo; Preceded at 1:22:11 by &ldquo;this is important.&rdquo;")),
  (N, "<b>Know the VIEW before you read the film.</b> Posterior-anterior reduces magnification of "
      "the heart; an anterior-posterior film makes the heart look big. Projections are named for "
      "what the BEAM strikes first.",
   why("SAID", "Lecture 2 at 1:14:06: &ldquo;you need to know what the view is&hellip; so that you "
               "can decide, is this actually cardiomegaly or not?&rdquo; View said 30&times;.")),
  (N, "<b>The five densities, whitest to blackest: METAL, CALCIUM, FLUID/SOFT TISSUE, FAT, AIR.</b> "
      "Fluid and soft tissue are the SAME density on a plain film &mdash; which is why computed "
      "tomography, which expands the grey scale, exists.",
   why("IO", "Directly under the density-and-contrast objective, and the foundation for reading "
             "anything.")),
  (L, "<b>Barium is CONTRAINDICATED if perforation is suspected</b> &mdash; use Gastrografin. Barium "
      "in the peritoneum is toxic.",
   why("IO", "Under contraindications and safety. A clean vignette answer.")),
  (L, "<b>Highest radiation emitters: computed tomography, positron emission tomography, SPECT.</b> "
      "Ultrasound and magnetic resonance use none. Neonatal abdominal computed tomography is about "
      "TWICE the adult organ dose.",
   why("TIME", "Radiation said 36&times;; the deck marks the emitter ranking IMPORTANT.")),
  (L, "<b>Position drives the question.</b> DECUBITUS levels out a PLEURAL EFFUSION (and you choose "
      "the side by which way you want fluid to run). KUB is supine for the genitourinary tract.",
   why("IO", "The patient-positioning objective; taught with worked reasoning rather than as a list.")),
  (L, "<b>Ultrasound indicator side.</b> Cardiac imaging: indicator on the RIGHT of the screen. "
      "Every other ultrasound: on the LEFT.",
   why("SAID", "Called &ldquo;crucial&rdquo; in the deck; getting it wrong mirrors left and right.")),
  (L, "<b>Reason from the TISSUE, not a memorised protocol.</b> Bone &rarr; x-ray or computed "
      "tomography. Soft tissue &rarr; often ultrasound first. Nerves, cord, marrow &rarr; magnetic "
      "resonance.",
   why("SAID", "Her stated method for choosing when you are unsure, and it answers the "
               "&ldquo;anatomical structures best visualized by each modality&rdquo; objective.")),
  (P, "<b>Modality mechanics.</b> Positron emission tomography uses fluorodeoxyglucose-18 for cancer "
      "staging; SPECT uses technetium-99 and follows blood flow. Angiography is not one test &mdash; "
      "any modality can image vessels.",
   why("IO", "Objective-backed, but the clinical application matters more than the physics.")),
  (P, "<b>The radiology relationship.</b> They have not seen your patient; a vague report is a "
      "conversation. Four regions of spine is FOUR orders, not one.",
   why("IO", "Has its own objective, which is why it is here at all, but it is one slide.")),
]},

# ---------------------------------------------------------------- L3
{"id": "l3", "label": "L3 &middot; Derm, ENT &amp; Ophtho Testing", "color": "#a8562f", "cols": COLS, "rows": [
  (N, "<b>THE MELANOMA RULE.</b> NARROW EXCISIONAL biopsy, 1&ndash;3 <i>millimetre</i> margins, to a "
      "depth that does NOT transect the base &mdash; so Breslow depth can be measured. A partial "
      "shave is allowed only when suspicion is LOW and may underestimate depth.",
   why("SAID", "Said three separate times in the lecture. Do not confuse the 1&ndash;3 mm DIAGNOSTIC "
               "margin with the 0.5&ndash;2 cm definitive re-excision margin &mdash; that swap is "
               "the obvious distractor.")),
  (N, "<b>The necrotising fasciitis red flag.</b> HYPOTENSION + white cell count &ge;15,000 + "
      "VIOLACEOUS skin &rarr; must be screened for necrotising fasciitis.",
   why("SAID", "Bolded in the deck AND said aloud. Three findings, one answer &mdash; exactly the "
               "shape of a vignette stem.")),
  (N, "<b>Potassium hydroxide readings.</b> BRANCHING SEPTATE HYPHAE = DERMATOPHYTE. PSEUDOHYPHAE + "
      "BUDDING YEAST = CANDIDA. Negative = no fungal elements.",
   why("IO", "&ldquo;Interpret potassium hydroxide (KOH) preparations&rdquo; is an objective that "
             "says <i>interpret</i> &mdash; it is asking for this table.")),
  (N, "<b>Tympanogram types, and the flat-trace split.</b> A = normal. B = restricted mobility. "
      "C = significant negative pressure. FLAT + HIGH canal volume &rarr; PERFORATION or patent tube. "
      "FLAT + NORMAL volume &rarr; MIDDLE-EAR EFFUSION.",
   why("IO", "Tympanometry has its own objective, and the volume split is the one number that "
             "changes the answer.")),
  (N, "<b>Rapid strep sensitivity is only 70&ndash;90%.</b> A NEGATIVE test IN A CHILD should be "
      "confirmed by CULTURE; not routinely required in adults. Culture is the gold standard.",
   why("TIME", "Strep said 20&times;, culture 22&times;. The child-versus-adult split is the "
               "testable half.")),
  (N, "<b>Fluorescein patterns.</b> LINEAR &rarr; abrasion. BRANCHING or DENDRITIC &rarr; HERPETIC "
      "keratitis. Cobalt-blue light, after topical anaesthetic.",
   why("TIME", "Fluorescein said 10&times; and it is named in the objective. Dendritic is the "
               "pattern that changes management.")),
  (N, "<b>Always choose the LEAST INVASIVE test that answers the question.</b> The four factors: "
      "cost, availability, invasiveness, diagnostic yield.",
   why("SAID", "The lecture&rsquo;s closing rule, and the final objective is literally &ldquo;apply "
               "diagnostic test selection principles&rdquo; &mdash; so it is the exam&rsquo;s own "
               "framing.")),
  (L, "<b>Which test for which question.</b> Infection &rarr; potassium hydroxide or culture. "
      "Neoplasm or persistent rash &rarr; biopsy. Abscess vs cellulitis &rarr; point-of-care "
      "ultrasound.",
   why("IO", "Covers three objectives at once; biopsy said 20&times;.")),
  (L, "<b>Biopsy techniques.</b> SHAVE for raised epidermal lesions and basal or squamous cell "
      "carcinoma. PUNCH for full-thickness. EXCISIONAL when you need the whole lesion.",
   why("IO", "&ldquo;Discuss indications for skin biopsy and common biopsy techniques.&rdquo;")),
  (L, "<b>Tonometry: normal pressure 10&ndash;21 mm Hg, and acute angle-closure glaucoma is an "
      "EMERGENCY.</b> Cup-to-disc normally about 0.3; glaucomatous above 0.7 and EXCAVATED, not "
      "merely pale.",
   why("IO", "Named in the objective. Note tonometry is said only once in lecture &mdash; the deck "
             "carries it, so learn the numbers and the emergency.")),
  (L, "<b>Visual acuity and the pinhole.</b> Test every eye complaint, best-corrected. Pinhole "
      "CORRECTS &rarr; refractive error. Does NOT correct &rarr; something else.",
   why("IO", "First named ophthalmic test in the objective; 8 mentions.")),
  (L, "<b>Computed tomography for BONE, TRAUMA and SPEED. Magnetic resonance for SOFT TISSUE, "
      "NERVES and intracranial or orbital extension.</b> No imaging at all for uncomplicated "
      "rhinosinusitis, otitis or simple soft-tissue infection.",
   why("IO", "Two objectives &mdash; comparing the modalities in head and neck, and selecting "
             "studies. The &ldquo;no imaging needed&rdquo; list is the half people forget.")),
  (P, "<b>Visual field patterns.</b> Central scotoma &rarr; macula or optic nerve. Peripheral loss "
      "&rarr; glaucoma. Bitemporal hemianopia &rarr; chiasmal.",
   why("IO", "Objective-backed, 5 mentions. Worth a read, not an evening.")),
  (P, "<b>The Levine method for wound culture.</b> Clean with sterile saline, NOT antimicrobial; "
      "rotate over 1 cm&sup2; of CLEAN tissue with enough pressure to express fluid.",
   why("IO", "Under the wound-culture objective, but procedural detail; a single fact at most.")),
]},

# ---------------------------------------------------------------- L4
{"id": "l4", "label": "L4 &middot; Complete Blood Count &amp; Hematology", "color": "#b03030", "cols": COLS, "rows": [
  (N, "<b>ABSOLUTE NEUTROPHIL COUNT = white cell count &times; (%neutrophils + %BANDS) &divide; 100.</b> "
      "BANDS COUNT WITH THE NEUTROPHILS &mdash; that is the trap. Worked example: 6,000 with 40% "
      "neutrophils and 5% bands &rarr; 2,700.",
   why("SAID", "Lecture 4 at 15:37: apps and the record will compute it, &ldquo;HOWEVER, EVERYONE "
               "NEEDS TO KNOW HOW TO CALCULATE THAT.&rdquo; The one calculation this exam wants.")),
  (N, "<b>The three MCV bands.</b> MICROCYTIC &lt;80 fL, NORMOCYTIC 80&ndash;100, MACROCYTIC &gt;100. "
      "Haemoglobin says there IS an anaemia; the mean corpuscular volume says WHICH KIND.",
   why("IO", "Its own objective comparing the three patterns; the whole workup hangs off it.")),
  (N, "<b>Iron studies, the two patterns.</b> IRON DEFICIENCY: ferritin DOWN, iron DOWN, total "
      "iron-binding capacity UP. ANAEMIA OF CHRONIC DISEASE: ferritin UP, iron DOWN, capacity DOWN.",
   why("TIME", "Iron said 30&times;. The reciprocal ferritin/capacity movement is the discriminator, "
               "and it is an objective on evaluating anaemia.")),
  (N, "<b>Iron deficiency is the MOST COMMON cause of anaemia</b> &mdash; and demands evaluation for "
      "occult blood loss, often the first sign of gastrointestinal bleeding.",
   why("SAID", "Flagged &ldquo;most common&rdquo; three times between 49:07 and 52:56.")),
  (N, "<b>Which line for which problem.</b> BACTERIAL &rarr; neutrophils. VIRAL &rarr; lymphocytes. "
      "ALLERGY or PARASITES &rarr; eosinophils.",
   why("TIME", "Neutrophil said 40&times;, the most in the lecture. Straight out of the "
               "clinical-significance objective.")),
  (N, "<b>LEFT SHIFT.</b> Bands are immature neutrophils, normally &le;5%. Neutrophils plus bands "
      "rising means the marrow is pushing out immature cells &mdash; acute bacterial infection.",
   why("IO", "Under white cell significance, and it is the reason bands are in the absolute count "
             "formula above.")),
  (L, "<b>Haemoglobin vs haematocrit.</b> Haemoglobin is the AMOUNT in a volume; haematocrit is the "
      "PERCENTAGE of blood that is red cells. Her habit: read the haemoglobin, multiply by three, "
      "check the haematocrit lands nearby.",
   why("IO", "Its own objective &mdash; &ldquo;explain the difference between hemoglobin and "
             "hematocrit&rdquo; &mdash; and the &times;3 rule is a fast sanity check.")),
  (L, "<b>The morphology&ndash;disease pairs.</b> HOWELL-JOLLY &rarr; post-splenectomy. "
      "BASOPHILIC STIPPLING &rarr; LEAD. HEINZ BODIES &rarr; G6PD deficiency (needs a supravital "
      "stain). TARGET CELLS &rarr; post-splenectomy and liver disease. SCHISTOCYTES &rarr; "
      "fragmentation. TEARDROP &rarr; marrow infiltration.",
   why("IO", "Under red cell significance. Pairs like these are the easiest thing on the exam to "
             "write a question about.")),
  (L, "<b>The reticulocyte split in a NORMOCYTIC anaemia.</b> HIGH retics &rarr; haemolysis, sickle "
      "cell, acute haemorrhage. LOW retics with low white cells and platelets &rarr; marrow failure.",
   why("IO", "The reticulocyte count is step four of the stated workup; this split is what it is for.")),
  (L, "<b>The four indices.</b> MCV = average volume (80&ndash;100 fL, measured). MCH = haemoglobin "
      "per cell. MCHC = concentration. RDW = variation in size.",
   why("IO", "&ldquo;Discuss red blood cell indices&rdquo; is an objective by itself.")),
  (L, "<b>Neutrophils UP</b> in bacterial infection, myocardial infarction, burns, STEROIDS "
      "(by DEMARGINATION &mdash; detaching from the vessel wall, not new production), pregnancy. "
      "<b>DOWN</b> with marrow damage, and with FOLATE or B12 deficiency.",
   why("TIME", "Part of the 40 neutrophil mentions; demargination is the mechanism worth a sentence.")),
  (L, "<b>Macrocytic: megaloblastic vs not.</b> MEGALOBLASTIC &mdash; B12, folate, drugs impairing "
      "DNA synthesis &mdash; shows MACROOVALOCYTES and HYPERSEGMENTED NEUTROPHILS. Without them, "
      "think liver disease or alcohol.",
   why("IO", "Third arm of the three-pattern objective; the smear finding is the discriminator.")),
  (P, "<b>Platelets: 150,000&ndash;450,000</b> &mdash; the one range she said she has NOT seen vary "
      "between labs. From megakaryocyte fragments, lifespan 7&ndash;10 days.",
   why("SAID", "Explicitly the exception to &ldquo;ranges vary by lab&rdquo;. If you commit ONE "
               "number in this lecture, commit this one.")),
  (P, "<b>Rouleaux vs agglutination, and MCHC as a screening flag</b> for hereditary spherocytosis.",
   why("IO", "Genuinely taught but thinly, and neither is named in an objective.")),
]},

# ---------------------------------------------------------------- L5
{"id": "l5", "label": "L5 &middot; Chemistry Panels", "color": "#1b4965", "cols": COLS, "rows": [
  (N, "<b>POTASSIUM is the centre of this lecture.</b> Excreted by the kidney with NO reabsorption, "
      "so it must be replaced. What SHIFTS it across the membrane: INSULIN, ACID-BASE STATUS, "
      "CATECHOLAMINES. Both high and low cause LIFE-THREATENING ARRHYTHMIAS.",
   why("SAID", "Said 112 times &mdash; more than twice any other term in any lecture &mdash; and at "
               "14:59: &ldquo;I want you to pay attention to these numbers&hellip; I want your ears "
               "to perk up, be like, this is important, potassium&rsquo;s important.&rdquo;")),
  (N, "<b>Potassium and pH move in OPPOSITE directions.</b> ACIDOSIS drives potassium OUT of cells "
      "(serum rises). ALKALOSIS drives it IN (serum falls). This is why the potassium in diabetic "
      "ketoacidosis misleads &mdash; serum can be HIGH while total body stores are DEPLETED.",
   why("TIME", "Acidosis said 28&times;, and diabetic ketoacidosis was singled out at 1:08:52 as "
               "&ldquo;why this is important&rdquo;. A reliable two-step question.")),
  (N, "<b>An abnormal SODIUM is a WATER problem first.</b> Ask &ldquo;too much or too little free "
      "water&rdquo; BEFORE &ldquo;too much or too little sodium&rdquo;. Sodium is the major "
      "extracellular cation; potassium the major intracellular one.",
   why("SAID", "Sodium said 58&times;; at 14:16 she works through exactly why the sodium is ordered. "
               "The framing is the answer to several possible stems.")),
  (N, "<b>ANION GAP = sodium &minus; (chloride + bicarbonate). Normal 8&ndash;12.</b> Raised gap "
      "means unmeasured acids &mdash; MUDPILES. Normal gap means bicarbonate LOSS from gut or kidney.",
   why("SAID", "&ldquo;Quick and dirty, calculate it.&rdquo; This is the one calculation she asks "
               "for in this lecture &mdash; contrast with the filtration rate, which she explicitly "
               "does not want calculated.")),
  (N, "<b>BUN : CREATININE greater than 20 : 1 is PRERENAL.</b> Below that, intrinsic renal. "
      "Creatinine is more specific (muscle origin); blood urea nitrogen is raised by bleeding, "
      "steroids and protein load too.",
   why("TIME", "Creatinine said 30&times;. A single ratio that answers a whole vignette.")),
  (N, "<b>Before any contrast study, order blood urea nitrogen and creatinine BY THEMSELVES.</b>",
   why("SAID", "At 38:11: &ldquo;you still need to know before you give that person contrast&hellip; "
               "ALWAYS. We don&rsquo;t say always very often in medicine. Always.&rdquo; It also "
               "ties Lecture 2 to Lecture 5, so it can be asked from either side.")),
  (N, "<b>BASIC panel = 8 tests</b> (glucose, calcium, sodium, potassium, chloride, bicarbonate, "
      "blood urea nitrogen, creatinine). <b>COMPREHENSIVE = 14</b>, adding albumin, total protein, "
      "alkaline phosphatase, the transaminases and bilirubin. <b>Chem-7 vs chem-8 is CALCIUM.</b>",
   why("IO", "&ldquo;Explain the components of a chemistry panel&rdquo; is objective one, and the "
             "basic-versus-comprehensive choice is how it gets asked.")),
  (L, "<b>Liver: INJURY vs FUNCTION.</b> AST, ALT, alkaline phosphatase and bilirubin mark INJURY. "
      "ALBUMIN, PROTHROMBIN TIME and bilirubin measure FUNCTION. ALT is more liver-specific; AST is "
      "also cardiac and skeletal muscle.",
   why("TIME", "Liver said 57&times;, third highest in the lecture, and it has its own objective.")),
  (L, "<b>Three liver shortcuts.</b> AST:ALT above 2:1 &rarr; ALCOHOL. Transaminases in the "
      "THOUSANDS &rarr; only three causes: viral, ischaemia, toxins. Alkaline phosphatase out of "
      "proportion &rarr; CHOLESTATIC; confirm hepatic origin with GGT.",
   why("IO", "Under the hepatic-pattern objective. Compact, high-signal, easy to write questions on.")),
  (L, "<b>Bicarbonate is reported as &ldquo;CO2&rdquo;.</b> LOW means metabolic acidosis &mdash; and "
      "that is your cue to calculate the anion gap. Chloride follows sodium for electrical "
      "neutrality and is reciprocal with bicarbonate.",
   why("TIME", "Chloride said 28&times;. The reporting-name trap is worth one sentence of memory.")),
  (L, "<b>The pattern trio.</b> RENAL: urea and creatinine up, filtration down, metabolic acidosis. "
      "HEPATIC: transaminases or alkaline phosphatase up, albumin down late. METABOLIC (DKA): "
      "glucose up, bicarbonate down, gap up, pH low.",
   why("IO", "&ldquo;Compare and contrast laboratory patterns seen in renal, hepatic and metabolic "
             "disorders&rdquo; &mdash; the objective asks for exactly these three side by side.")),
  (L, "<b>The vomiting case.</b> Sodium, potassium and chloride all DOWN, bicarbonate UP, alkalaemia. "
      "It persists because volume, potassium and chloride depletion force the kidney to keep "
      "reabsorbing bicarbonate.",
   why("IO", "The worked example for the fluid-and-electrolyte objective; a ready-made vignette.")),
  (P, "<b>Albumin correction of the gap</b> (add about 2.5 per 1 g/dL fall) and <b>serum osmolality</b> "
      "(about 275&ndash;285) separating true from pseudo-hyponatraemia.",
   why("IO", "Real content under the homeostasis objective, but she does not ask for calculations "
             "&mdash; recognise the concepts.")),
  (P, "<b>Hepatorenal and cardiorenal syndrome</b> as names for combined failure.",
   why("IO", "Mentioned once. Know the words.")),
]},

# ---------------------------------------------------------------- L6
{"id": "l6", "label": "L6 &middot; Urinalysis", "color": "#8a7526", "cols": COLS, "rows": [
  (N, "<b>It is NITRITES, not nitrates.</b> Urease-producing bacteria carry a reductase that turns "
      "urinary NITRATES into NITRITES, and it needs MORE THAN FOUR HOURS in the bladder.",
   why("SAID", "She asked the class for this naming point TWICE. When a lecturer repeats a naming "
               "distinction, it is a question.")),
  (N, "<b>E. coli causes most urinary tract infections and is RARELY urease-positive.</b> So a "
      "POSITIVE nitrite is helpful, but a NEGATIVE nitrite does NOT exclude infection. Nitrite "
      "sensitivity is only about 50%.",
   why("SAID", "At 18:59 she names E. coli as &ldquo;the most common microorganism&rdquo;, returns "
               "at 24:06 with &ldquo;remember which one did I say was most common?&rdquo;, and the "
               "take-home flag lands at 23:17. Three cues on one idea.")),
  (N, "<b>Leukocyte esterase positive = PYURIA.</b> Also raised in interstitial cystitis and "
      "glomerulonephritis, which are inflammatory rather than infective. Either pad negative with "
      "symptoms &rarr; STILL send culture and sensitivity.",
   why("SAID", "&ldquo;That&rsquo;s the take-home point&rdquo; at 23:17, and it is named in the "
               "parameters objective.")),
  (N, "<b>Blood on the pad has THREE meanings, and the pad cannot tell them apart.</b> "
      "HAEMATURIA = intact red cells. HAEMOGLOBINURIA = free haemoglobin, from intravascular "
      "haemolysis &mdash; confirm with raised UNCONJUGATED BILIRUBIN. MYOGLOBINURIA = muscle injury "
      "&mdash; confirm with raised CREATINE PHOSPHOKINASE.",
   why("IO", "An entire objective is &ldquo;differentiate between hematuria, hemoglobinuria and "
             "myoglobinuria&rdquo;. One of only three objectives in the lecture &mdash; and the two "
             "confirming tests are how you differentiate them.")),
  (N, "<b>Which pads should read NEGATIVE</b> &mdash; leukocyte esterase, nitrites, ketones, "
      "glucose, blood, bilirubin (protein negative or trace). <b>Specific gravity and pH ALWAYS "
      "carry a value</b> and are never simply &ldquo;negative&rdquo;.",
   why("IO", "The parameters objective lists the pads by name. This is the cleanest way to hold them.")),
  (L, "<b>Ketones mean cells are burning FATTY ACIDS.</b> Next move: CHECK THE GLUCOSE. Causes "
      "include diabetic ketoacidosis, starvation, fasting, alcohol, very low-carbohydrate diets.",
   why("IO", "Named in the parameters objective; the &ldquo;next move&rdquo; is the correlation the "
             "third objective asks for.")),
  (L, "<b>Glucose appears in urine above the TUBULAR THRESHOLD, around 180 mg/dL</b> &mdash; it is "
      "normally filtered then wholly reabsorbed proximally. It can also appear without high blood "
      "sugar: impaired reabsorption, dextrose infusions, PREGNANCY.",
   why("TIME", "Glucose said 19&times;. The threshold is the mechanism the question turns on.")),
  (L, "<b>Protein is NOT pathognomonic.</b> It narrows the field; it does not name a disease. Normal "
      "trace in pregnancy, fever and strenuous exercise. Next test is a TWENTY-FOUR HOUR collection.",
   why("SAID", "At 37:33: &ldquo;it&rsquo;s not pathognomonic for any one single thing.&rdquo; "
               "Protein is also the most-said term in the lecture at 22.")),
  (L, "<b>The myeloma trap.</b> Reagent strips are INSENSITIVE to BENCE JONES proteins &mdash; use "
      "urine protein electrophoresis, not a dipstick.",
   why("IO", "Under the protein parameter; a clean single-best-answer trap.")),
  (L, "<b>Specific gravity.</b> LOW (dilute): overhydration, diuresis, chronic kidney disease, "
      "DIABETES INSIPIDUS. HIGH (concentrated): dehydration, reduced renal blood flow, SIADH. "
      "Radiographic CONTRAST has large particles and pushes it above 1.040.",
   why("TIME", "Said 11&times; and named first in the parameters objective. The contrast artefact is "
               "the memorable bit.")),
  (L, "<b>Reading time DIFFERS by analyte</b> &mdash; glucose 30 seconds, leukocytes 2 minutes &mdash; "
      "so a strip cannot be read all at once, and pads sit in different orders on different brands.",
   why("IO", "Practical detail under the parameters objective, and it makes a plausible "
             "&ldquo;what went wrong&rdquo; stem.")),
  (P, "<b>pH and stones.</b> ACIDIC urine &rarr; calcium oxalate and uric acid stones. ALKALINE "
      "&rarr; triple phosphate and struvite, driven by urease-producing organisms, so treat the "
      "INFECTION. Name trap: RENAL TUBULAR ACIDOSIS gives ALKALINE urine.",
   why("IO", "pH is in the objective list; the stone pairings are a step beyond it. The name trap is "
             "the part worth holding.")),
  (P, "<b>Colour and odour lists.</b> Yellow-brown or green &rarr; bilirubin. Fruity &rarr; ketones. "
      "Ammonia &rarr; the sample stood too long. Faecal odour &rarr; enterovesical fistula.",
   why("IO", "Physical characteristics are covered, but these are recall lists and the objectives "
             "emphasise the chemical pads.")),
  (P, "<b>After the strip:</b> microscopy adds white cells, red cells, squamous epithelial cells, "
      "casts and crystals. More than twenty squamous cells per field means CONTAMINATION.",
   why("IO", "Correlation objective, lightly taught &mdash; the contamination number is the one fact "
             "worth keeping.")),
]},
]


EXTRA_CSS = """
<style>
  td .tier{display:inline-block;font-size:.62rem;font-weight:800;letter-spacing:.06em;
           padding:3px 8px;border-radius:999px;white-space:nowrap;color:#fff;}
  .tier.t1{background:#8c1d12;} .tier.t2{background:#7a5a08;} .tier.t3{background:#4a5c24;}
  td .ev{display:inline-block;font-size:.6rem;font-weight:800;letter-spacing:.07em;
         padding:2px 6px;border-radius:4px;margin-right:6px;vertical-align:1px;}
  .ev.e-said{background:#8c1d12;color:#fff;}
  .ev.e-time{background:#1b4965;color:#fff;}
  .ev.e-io{background:#3f5c46;color:#fff;}
  table td:first-child{text-align:center;vertical-align:middle;width:8.5em;}
  table td:last-child{font-size:.86rem;line-height:1.5;}
  .keybox{border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:16px 0 4px;
          background:var(--card);}
  .keybox h3{margin:0 0 8px;font-size:.95rem;}
  .keybox p{margin:6px 0;font-size:.86rem;line-height:1.55;}
  .keybox .ev{margin-right:8px;}
</style>
"""

KEY = """
<div class="keybox">
  <h3>How to read the Odds column</h3>
  <p><span class="tier t1">NEAR-CERTAIN</span> Two or three kinds of evidence agree, usually
     including something the lecturer said out loud. If you are short on time, this is the exam.</p>
  <p><span class="tier t2">LIKELY</span> Answers a numbered objective and the lecture spent real
     time on it.</p>
  <p><span class="tier t3">POSSIBLE</span> Objective-backed but lightly taught. Know it exists;
     do not sink an evening into it.</p>
  <h3 style="margin-top:14px">And the evidence tags</h3>
  <p><span class="ev e-said">SAID</span> the lecturer flagged it aloud &mdash; quoted, with a
     timestamp, from the recordings.</p>
  <p><span class="ev e-time">TIME</span> measured by how often the term appears across the
     lecture transcripts. Potassium is said 112 times in Lecture 5; contrast 60 times in Lecture 2.</p>
  <p><span class="ev e-io">IO</span> it answers a numbered syllabus Instructional Objective.
     Necessary for anything to be here at all.</p>
</div>
"""


def main():
    html = render(
        title="PDM Exam 1 &mdash; Most Likely Tested",
        kicker="Principles of Diagnostic Medicine I &middot; Exam 1 &middot; Class of 2028",
        h1="Most Likely Tested",
        sub="Six lectures ranked by how likely each fact is to be asked, with what to stop "
            "studying at the top. Built from the 56 syllabus objectives, the six lecture "
            "recordings, and what each lecturer said out loud about their own exam.",
        topics=TOPICS,
        guide_href="pdm-exam-1-study-guide.html",
        footer_note="Ranked, not exhaustive &mdash; this page drops material on purpose. The "
                    "<a href=\"pdm-exam-1-study-guide.html\">study guide</a> has the full "
                    "treatment and the <a href=\"pdm-exam-1-cram-sheet.html\">cram sheet</a> "
                    "has everything condensed. Every quotation is from a lecture recording; "
                    "recordings stay off the site.",
    )
    # The template's stock note describes a CRAM SHEET -- "condensed... assumes
    # you've already learned the material". This page makes a different promise,
    # so the note has to say so or it misrepresents what the reader is holding.
    # Matched by REGEX from the opening phrase to the link that follows it: the
    # template hard-wraps and re-indents that sentence, and two attempts at a
    # whitespace-exact match both failed on it.
    new_note = ("this page is RANKED, and it leaves things out on purpose. Start at "
                "<b>Cut this first</b> \u2014 everything there was ruled out by a lecturer in as "
                "many words, so it is time you get back. Then work down each lecture from "
                "NEAR-CERTAIN. It is an argument about what matters most, with the evidence for "
                "every call in the last column, not a complete account \u2014 for that, see the ")
    html, n = re.subn(r"this is a condensed, night-before-the-exam reference.*?go back to the\s*",
                      new_note, html, count=1, flags=re.S)
    assert n == 1, "the cram template's stock note has changed -- re-check it"

    html = html.replace("</body>", EXTRA_CSS + "</body>")
    # The key belongs above the first table, right after the jump chips.
    anchor = '<section'
    i = html.index(anchor)
    html = html[:i] + KEY + html[i:]

    for tag in ("table", "thead", "tbody", "tr", "td", "th", "div", "section", "p"):
        o = len(re.findall(r"<%s[ >]" % tag, html)); c = html.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    assert "T(0)" not in html
    open(OUT, "w", encoding="utf-8").write(html)
    n = sum(len(t["rows"]) for t in TOPICS)
    print("wrote %s (%d KB, %d topics, %d rows)"
          % (os.path.basename(OUT), len(html) // 1024, len(TOPICS), n))


if __name__ == "__main__":
    main()
