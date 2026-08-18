#!/usr/bin/env python3
"""Build the three Physical Diagnosis 2 OSCE run-sheets: ENT, Cardiac, Pulmonary.

Format is the WHOLE OSCE RUN, not just the maneuvers, because that is what the
station is graded on. The syllabus lecture lists the components in order --
focused history of present illness, focused review of systems, focused past
medical history, focused social history, family history with medications and
allergies, physical examination, differentials, labs and studies, diagnosis,
treatment plan including patient education, and a one-minute case presentation
-- and each page walks that sequence end to end. The system-specific
examination sits inside it as one part rather than being the whole page.

Skeleton is lifted from the PD1 combined head-to-toe checksheet: its CSS, dark
mode, print rules, tick persistence, spoken/hands-on filters and settings menu
all come across unchanged, so these read as the same instrument. Like that page
and relax.html, it deliberately does NOT load theme.js/theme.css, so
window.reportMistake is provided locally and the theme is read from the shared
siteTheme key.

Examination items are drawn from the PD1 lab checksheets already merged into
that page -- the maneuvers for ears, nose, mouth, neck, nodes, lungs, cardiac
and peripheral vascular do not change between courses. What changes is that
these are FOCUSED encounters, so each page carries the subset a station on that
system would actually grade, in the order you would perform it, plus the
history and reasoning steps PD1 never asked for. PD2's own lectures land on
9/3 (ENT), 9/17 (Cardiac) and 10/22 (Thorax); anything those add gets layered
in then.

Each page stores its ticks under its own key so the three do not overwrite
each other.
"""
import os, re, html

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
DONOR = os.path.join(ROOT, "Physical Diagnosis 1 Exam 3/pd1-head-to-toe-checksheet.html")
OUTDIR = os.path.join(ROOT, "Physical Diagnosis 2 Exam 1")

# ---------------------------------------------------------------- content DSL
# item: ("say"|"do", text, script=None, hint=None, tag=None)
def say(t, script=None, hint=None, tag=None): return ("say", t, script, hint, tag)
def do(t, script=None, hint=None, tag=None):  return ("do", t, script, hint, tag)


# ------------------------------------------------------------- shared spine
def opening(system):
    return dict(id="s1", title="Opening &amp; Preparation", src=(
        "Every station opens the same way. The chief complaint and vital signs are "
        "given to you on a separate form &mdash; read them before you enter."),
      blocks=[("items", [
        do("Reviews the chief complaint and vital signs on the form before entering the room"),
        say("Knocks, enters, and introduces self by name and role",
            script='"Hello, I am [name], a physician assistant student. I will be taking care of you today."'),
        say("Confirms the patient's identity",
            hint="Patient identifying data is the one thing the &ldquo;patient&rdquo; will answer directly. Everything else comes from the facilitator."),
        do("Performs hand hygiene"),
        say("States the purpose of the visit and obtains permission to proceed",
            script='"I am going to ask you some questions about what brought you in, and then examine you. Is that all right?"'),
        do("Ensures patient comfort and privacy before beginning"),
        say("Interprets the vital signs out loud",
            hint="Do not just read them back. Say whether each is normal and what an abnormal one would mean for %s." % system),
      ])])


def hpi(system, lead, items):
    return dict(id="s2", title="Focused History of Present Illness", src=lead,
      blocks=[
        ("ref", "OLD CHARTS &mdash; Onset &middot; Location &middot; Duration &middot; Character &middot; "
                "Alleviating and aggravating factors &middot; Radiation &middot; Temporal pattern &middot; "
                "Symptoms associated. Any of the four pain mnemonics is acceptable; use one and use it completely."),
        ("h4", "The seven attributes, applied to the chief complaint"),
        ("items", [
          say("Onset &mdash; when it began, and what the patient was doing"),
          say("Location &mdash; where it is, and whether the patient can point to it"),
          say("Duration &mdash; constant or intermittent, and how long each episode lasts"),
          say("Character &mdash; what it feels like, in the patient's own words"),
          say("Alleviating and aggravating factors &mdash; what makes it better, what makes it worse"),
          say("Radiation &mdash; whether it moves anywhere"),
          say("Severity &mdash; on a scale of one to ten",
              hint="Anchor the scale. The number is meaningless until you ask what a ten is for this patient."),
          say("Temporal pattern &mdash; better or worse at any time of day, or with any activity"),
        ]),
        ("h4", "Associated symptoms &mdash; %s" % system),
        ("items", items),
      ])


def background(items):
    return dict(id="s3", title="Focused Review of Systems, Past Medical, Social &amp; Family History", src=(
        "All of these are FOCUSED, not comprehensive. Ask what bears on this complaint and "
        "on your differential &mdash; that selection is itself part of what is being graded."),
      blocks=[
        ("h4", "Focused review of systems"),
        ("items", items),
        ("h4", "Focused past medical history"),
        ("items", [
          say("Prior episodes of the same problem, and what was done about them"),
          say("Chronic medical conditions"),
          say("Previous surgeries or procedures"),
          say("Hospitalisations"),
        ]),
        ("h4", "Medications and allergies"),
        ("items", [
          say("Prescription medications, with dose and how long they have been taken"),
          say("Over-the-counter medications, supplements and herbal products",
              hint="Easy to skip and easy to lose a point on. Ask it explicitly."),
          say("Allergies, and the reaction to each",
              hint="&ldquo;No known drug allergies&rdquo; is an answer; &ldquo;allergies?&rdquo; with no follow-up is not."),
        ]),
        ("h4", "Focused social history"),
        ("items", [
          say("Tobacco use &mdash; current or past, and how much"),
          say("Alcohol and recreational drug use"),
          say("Occupation and relevant exposures"),
          say("Living situation and who is at home"),
        ]),
        ("h4", "Focused family history"),
        ("items", [
          say("Conditions in first-degree relatives that bear on this complaint"),
        ]),
        ("h4", "Close the history"),
        ("items", [
          say("Summarises the history back to the patient and asks whether anything was missed",
              script='"Let me make sure I have this right &mdash; [summary]. Is there anything else I should know?"'),
          say("Signals the transition to the examination and obtains permission",
              script='"I would like to examine you now. Is that all right?"'),
        ]),
      ])


def reasoning(ddx_hint):
    return dict(id="s6", title="Differentials, Studies &amp; Diagnosis", src=(
        "Spoken, not performed. This is the part that separates a strong station from a "
        "complete one, and it is where the small groups have been training you: every "
        "request needs a reason attached."),
      blocks=[
        ("h4", "Differential diagnosis"),
        ("items", [
          say("States a differential diagnosis out loud", hint=ddx_hint),
          say("Includes the worst-case diagnosis that must be excluded, even if it is unlikely",
              hint="&ldquo;What must be examined to rule out the worst-case scenario?&rdquo; is one of the two questions that decide the scope of a focused encounter."),
          say("Justifies each differential against a specific finding from the history or examination",
              script='"[Diagnosis] is on my differential because of [finding], and against it is [finding]."'),
        ]),
        ("h4", "Laboratory and imaging studies"),
        ("items", [
          say("States which studies would be ordered"),
          say("Justifies each one &mdash; why it is needed and what it would tell you about the patient",
              hint="This is the exact standard the small groups apply: a facilitator will not release information until the justification is given."),
          say("States which differential each study would rule in or rule out"),
        ]),
        ("h4", "Diagnosis"),
        ("items", [
          say("States the working diagnosis"),
          say("States the evidence from this encounter that supports it"),
        ]),
      ])


def plan(items):
    return dict(id="s7", title="Treatment Plan &amp; Patient Education", src=(
        "The plan is a graded component in its own right, and patient education is named "
        "explicitly in the station's component list &mdash; it is not optional garnish."),
      blocks=[
        ("h4", "Treatment plan"),
        ("items", items),
        ("h4", "Patient education"),
        ("items", [
          say("Explains the diagnosis in plain language, without medical jargon",
              hint="Adapting style and content to the patient is a graded professional behaviour."),
          say("Explains what the treatment is and why it is being recommended"),
          say("States return precautions &mdash; what would bring the patient back sooner"),
          say("Confirms understanding and invites questions",
              script='"What questions do you have for me?"'),
        ]),
        ("h4", "Closure"),
        ("items", [
          say("States the follow-up interval"),
          say("Thanks the patient and closes the encounter"),
          do("Performs hand hygiene on the way out"),
        ]),
      ])


def presentation(system):
    return dict(id="s8", title="One-Minute Case Presentation", src=(
        "Delivered at the end of the station. A well-organised vignette that describes the "
        "patient and the clinical problem &mdash; not the note read aloud."),
      blocks=[
        ("banner", "<b>The test of a good presentation &mdash;</b> it leads your facilitator to the "
                   "<b>same differential you formulated</b>. If they reach a different one, the "
                   "presentation failed even if every fact in it was true."),
        ("items", [
          say("Opens with the past medical history and the chief complaint",
              script='"This is a [age]-year-old [patient] with a history of [past medical history] presenting with [chief complaint]."'),
          say("Gives the pertinent positives from the history"),
          say("Gives the pertinent negatives from the history",
              hint="Negatives carry as much weight as positives. They are how the listener sees what you ruled out."),
          say("Gives the pertinent positives and negatives from the %s examination" % system),
          say("Presents mostly in the order the history was obtained and the examination performed"),
          say("States the differential"),
          say("States the studies and the diagnosis"),
          say("States the plan"),
          do("Delivers it without reading from notes",
             hint="Reading works directly against helping the listener visualise the patient."),
          do("Keeps it to about one minute"),
        ]),
      ])


# ------------------------------------------------------------------- ENT OSCE
ENT_EXAM = dict(id="s5", title="Focused Physical Examination &mdash; Ear, Nose &amp; Throat", src=(
    "Maneuvers from the PD1 Head, Ears, Nose and Throat lab checksheet, reduced to what a "
    "focused ENT station grades and ordered as you would perform it. Narrate as you go."),
  blocks=[
    ("h4", "General"),
    ("items", [
      do("Performs hand hygiene before touching the patient"),
      say("Performs a general survey &mdash; distress, voice quality, audible stridor or mouth breathing",
          hint="Hoarseness or a muffled &ldquo;hot potato&rdquo; voice is a finding you get for free before you touch anything."),
      do("Gathers equipment &mdash; otoscope with speculum, penlight, tongue depressor, gloves"),
    ]),
    ("h4", "Ears"),
    ("items", [
      say("Inspects the auricle for deformities, discharge and lesions",
          script='"I am inspecting the auricle for deformities, discharge, or lesions."'),
      say("Palpates the auricle, tragus and mastoid for tenderness",
          script='"I am palpating the auricle, tragus, and mastoid for tenderness."',
          hint="Tragal tenderness points outward to the canal; mastoid tenderness points inward and is the worrying one."),
      do("Chooses an appropriately sized speculum"),
      do("Pulls the auricle upward, outward and back to straighten the canal"),
      say("Verbalizes the structures assessed in the ear canal",
          script='"I am noting the condition of the external canal, the amount of cerumen, and the presence of any inflammation, edema, or foreign bodies."'),
      say("Notes the colour and contour of the tympanic membrane",
          script='"I am noting the color and contour of the tympanic membrane as pearly gray."'),
      say("Identifies the landmarks and the light reflex",
          script='"I am visualizing the malleus, umbo, pars tensa, pars flaccida, and the cone of light."'),
      do("Examines both ears &mdash; the unaffected side first"),
    ]),
    ("h4", "Hearing &mdash; cranial nerve VIII", ),
    ("items", [
      say("States the cranial nerve number and name &mdash; <b>VIII, Vestibulocochlear</b>", tag="CN VIII"),
      say("Verbalizes that the canals were confirmed patent first, with the otoscope"),
      do("Performs the whispered hearing test bilaterally, standing two feet away"),
      say("Verbalizes the follow-up if gross hearing is abnormal",
          script='"If this test was abnormal, I would perform a Rinne and Weber test for bone versus air conduction."'),
    ]),
    ("h4", "Nose &amp; sinuses"),
    ("items", [
      say("Inspects the external nose for deformities",
          script='"I am inspecting the nose for deformities."'),
      do("Evaluates nasal patency bilaterally &mdash; occludes one nostril and has the patient sniff"),
      do("Palpates the nose for tenderness"),
      say("Uses the otoscope with an appropriate speculum to inspect the nares",
          script='"I am inspecting the condition of the nasal mucosa, the turbinates for polyps, and the nasal septum for septal deviation or perforations."'),
      do("Palpates the frontal and maxillary sinuses for tenderness"),
      say("Verbalizes transillumination of the sinuses if sinusitis is suspected"),
      say("States the cranial nerve number and name &mdash; <b>I, Olfactory</b>", tag="CN I",
          hint="Test it here if the complaint involves smell; otherwise verbalize that you would."),
    ]),
    ("h4", "Oral cavity &amp; pharynx"),
    ("items", [
      do("Uses a penlight and tongue depressor, and gloves to palpate"),
      say("Inspects the lips, buccal mucosa, gingiva, floor of mouth and teeth",
          script='"I am inspecting the nasolabial fold, lips, buccal mucosa, gingiva, floor of mouth, and teeth."'),
      say("Notes inflammation, lesions and the condition of the dentition",
          script='"I am noting any inflammation or lesions and condition of dentition."'),
      say("Inspects the palate and oropharynx for inflammation and lesions",
          script='"I am inspecting the palate and oropharynx for inflammation or lesions."'),
      say("Inspects the posterior pharynx, noting the condition of the tonsils",
          script='"I am inspecting the posterior pharynx noting the condition of the tonsils."',
          hint="Note tonsillar size, exudate, and whether the uvula is midline &mdash; deviation is the finding that changes the plan."),
      say("States the cranial nerve numbers and names &mdash; <b>IX Glossopharyngeal, X Vagus</b>", tag="CN IX &middot; X"),
      say("Asks the patient to say &ldquo;AHH&rdquo; while observing and listening",
          script='"I am noting the phonation and symmetrical rise and fall of the soft palate and uvula."'),
      say("Verbalizes performance of the gag reflex"),
      say("States the cranial nerve number and name &mdash; <b>XII, Hypoglossal</b>", tag="CN XII"),
      say("Asks the patient to protrude the tongue and notes colour, texture and whether it is midline",
          script='"I am noting the color and texture of the tongue and assessing if it is midline."'),
    ]),
    ("h4", "Neck &amp; lymph nodes"),
    ("items", [
      say("Inspects the anterior neck for masses, asymmetry and thyromegaly",
          script='"I am inspecting the anterior neck for masses, asymmetry, or thyromegaly."'),
      say("Inspects and palpates the position of the trachea",
          script='"I am inspecting and palpating the position of the trachea."'),
      do("Palpates the thyroid isthmus and each lobe"),
      say("Verbalizes the names of the lymph nodes as they are palpated"),
      do("Palpates using the pads of the fingers in a circular motion"),
      do("Preauricular &middot; posterior auricular &middot; occipital"),
      do("Tonsillar &middot; submandibular &middot; submental"),
      do("Superficial cervical &middot; posterior cervical &middot; deep cervical chains"),
      do("Supraclavicular &mdash; asks the patient to take a deep breath during palpation"),
      say("Describes any node found &mdash; size, consistency, mobility, tenderness",
          hint="A tender, mobile, soft node reads infectious; a hard, fixed, non-tender one does not."),
    ]),
  ])

ENT = dict(
  slug="pd2-ent-osce", key="pd2EntOsce",
  h1="ENT OSCE &mdash; Focused Encounter Run-Sheet",
  eyebrow="PAJ 5310 &middot; Physical Diagnosis II &middot; Fall 2026",
  date="Tuesday 16 September 2026",
  sub=("The whole station in order, from the introduction through the one-minute case "
       "presentation. Examination maneuvers come from the PD1 Head, Ears, Nose and Throat "
       "lab checksheet, reduced to what a focused ENT encounter grades."),
  navlabels=["1 Open", "2 HPI", "3 History", "4 Vitals", "5 ENT Exam", "6 Reasoning", "7 Plan", "8 Present"],
  sections=[
    opening("an ear, nose and throat complaint"),
    hpi("Ear, nose and throat",
        "Take it focused. The chief complaint is on the form; this is where you build the story around it.",
        [
          say("Ear pain &mdash; one side or both, and whether anything makes it worse"),
          say("Ear discharge &mdash; and its character"),
          say("Hearing change, and whether it came on suddenly or gradually"),
          say("Tinnitus"),
          say("Vertigo or dizziness",
              hint="Make the patient describe it rather than accepting the word &ldquo;dizzy&rdquo;."),
          say("Nasal congestion or obstruction"),
          say("Rhinorrhea &mdash; and its character"),
          say("Epistaxis"),
          say("Facial pain or pressure, and whether it worsens on bending forward"),
          say("Sore throat, and whether swallowing makes it worse"),
          say("Dysphagia or odynophagia"),
          say("Hoarseness or voice change"),
          say("Fever"),
          say("Recent upper respiratory infection, or sick contacts",
              hint="Bugs, drugs, contact applies here as much as in dermatology."),
        ]),
    background([
      say("Constitutional &mdash; fever, chills, fatigue, weight loss"),
      say("Head and neck &mdash; headache, neck stiffness, neck swelling"),
      say("Respiratory &mdash; cough, shortness of breath"),
      say("Gastrointestinal &mdash; nausea, vomiting, reflux",
          hint="Reflux is a genuine cause of hoarseness and chronic sore throat."),
      say("Denies symptoms outside the focused set, and says so out loud"),
    ]),
    dict(id="s4", title="Vital Signs &amp; General Survey", src=(
        "Vitals are handed to you on the form. Interpreting them out loud is the graded part."),
      blocks=[("items", [
        say("Restates the vital signs and interprets each one"),
        say("Comments on any fever and what it adds to the differential"),
        say("Performs a general survey &mdash; level of distress, hydration, voice, work of breathing"),
      ])]),
    ENT_EXAM,
    reasoning("Three is a reasonable floor for an ENT station. Say them; do not leave them implied."),
    plan([
      say("States whether the condition is managed symptomatically or requires directed treatment"),
      say("Addresses pain control"),
      say("States whether an antimicrobial is indicated, and why or why not",
          hint="Being able to justify NOT prescribing is as gradeable as prescribing."),
      say("States any red flags that would change the plan or prompt referral"),
      say("States what would prompt referral to ear, nose and throat surgery"),
    ]),
    presentation("ear, nose and throat"),
  ])


# --------------------------------------------------------------- CARDIAC OSCE
CARDIAC_EXAM = dict(id="s5", title="Focused Physical Examination &mdash; Cardiovascular", src=(
    "Maneuvers from the PD1 Cardiovascular and Peripheral Vascular lab checksheets, reduced "
    "to what a focused cardiac station grades. The position change matters &mdash; do it early "
    "and say why."),
  blocks=[
    ("banner", "<b>Position &mdash;</b> patient <b>supine with the head of the bed elevated 30&deg;</b>. "
               "Stand on the patient's right if you are right-handed, left if left-handed. "
               "Say the position out loud; it is a graded item, and the jugular venous "
               "assessment is meaningless without it."),
    ("h4", "General"),
    ("items", [
      do("Performs hand hygiene before touching the patient"),
      do("Places the patient supine with the head elevated thirty degrees"),
      do("Stands on the correct side of the patient for handedness"),
      say("Performs a general survey &mdash; distress, colour, work of breathing, diaphoresis"),
      say("Inspects the hands and nail beds for cyanosis and clubbing"),
    ]),
    ("h4", "Neck &mdash; jugular and carotid"),
    ("items", [
      say("Inspects the anterior neck for jugular vein distention",
          script='"I am inspecting the anterior neck for jugular vein distention."'),
      say("Inspects the carotid pulses",
          hint="Looking for the upstroke, its amplitude and contour, and any visible thrill."),
      do("Asks the patient to hold their breath for ten seconds and auscultates each carotid with the diaphragm <em>and</em> the bell"),
      do("Palpates each carotid in the lower third of the neck, <b>one side at a time</b>",
         hint="One at a time, always. Bilateral simultaneous carotid pressure is the error being watched for."),
    ]),
    ("h4", "Inspection of the precordium"),
    ("items", [
      say("Inspects the precordium for abnormal wall motion and the apical impulse, using tangential lighting"),
    ]),
    ("h4", "Palpation of the precordium &mdash; finger pads, for heaves and lifts"),
    ("items", [
      do("Second intercostal space, right sternal border &mdash; <b>Aortic</b>"),
      do("Second intercostal space, left sternal border &mdash; <b>Pulmonic</b>"),
      do("Third intercostal space, left sternal border &mdash; <b>Erb's point</b>"),
      do("Fourth intercostal space, left sternal border &mdash; <b>Tricuspid</b>"),
      do("Fifth intercostal space, left midclavicular line &mdash; <b>Mitral</b>"),
      say("Notes the size and intensity of the apical impulse &mdash; should be a light tap"),
      say("Notes the location of the point of maximal impulse",
          hint="Displaced laterally is the finding that matters."),
    ]),
    ("h4", "Palpation of the precordium &mdash; ball of the hand, for thrills"),
    ("items", [
      do("All five areas &mdash; aortic, pulmonic, Erb's point, tricuspid, mitral"),
    ]),
    ("h4", "Auscultation of the precordium &mdash; diaphragm and bell at each area"),
    ("items", [
      do("Second intercostal space, right sternal border &mdash; <b>Aortic</b>"),
      do("Second intercostal space, left sternal border &mdash; <b>Pulmonic</b>"),
      do("Third intercostal space, left sternal border &mdash; <b>Erb's point</b>"),
      do("Fourth intercostal space, left sternal border &mdash; <b>Tricuspid</b>"),
      do("Fifth intercostal space, left midclavicular line &mdash; <b>Mitral</b>"),
      say("Verbalizes what is being listened for &mdash; rate, rhythm, intensity of the first and second heart sounds, systole, diastole, extra sounds, murmurs"),
      say("Describes any murmur found &mdash; timing, location, radiation, intensity, quality",
          hint="Timing first. Systolic versus diastolic is the branch point of the whole differential."),
    ]),
    ("h4", "Lung bases"),
    ("items", [
      do("Auscultates the posterior lung bases bilaterally"),
      say("Verbalizes listening for crackles",
          hint="A cardiac station that never listens to the lungs has skipped the finding that separates compensated from decompensated."),
    ]),
    ("h4", "Peripheral vascular"),
    ("items", [
      say("Inspects the extremities for size, symmetry and edema"),
      say("Inspects skin colour, venous pattern, hair growth and any ulceration"),
      do("Palpates peripheral pulses bilaterally &mdash; brachial, radial, femoral, popliteal, posterior tibialis, dorsalis pedis"),
      say("Grades each pulse and comments on symmetry"),
      do("Assesses capillary refill in the upper and lower extremities"),
      say("Notes that colour typically returns within two to three seconds"),
      do("Palpates for pitting edema over the tibia and ankles"),
      say("Grades any edema found and states how far up it extends"),
    ]),
  ])

CARDIAC = dict(
  slug="pd2-cardiac-osce", key="pd2CardiacOsce",
  h1="Cardiac OSCE &mdash; Focused Encounter Run-Sheet",
  eyebrow="PAJ 5310 &middot; Physical Diagnosis II &middot; Fall 2026",
  date="Wednesday 21 October 2026",
  sub=("The whole station in order, from the introduction through the one-minute case "
       "presentation. Examination maneuvers come from the PD1 Cardiovascular and Peripheral "
       "Vascular lab checksheets, reduced to what a focused cardiac encounter grades."),
  navlabels=["1 Open", "2 HPI", "3 History", "4 Vitals", "5 Cardiac Exam", "6 Reasoning", "7 Plan", "8 Present"],
  sections=[
    opening("a cardiac complaint"),
    hpi("Cardiovascular",
        "Chest pain is the commonest stem, but the same structure works for palpitations, syncope or dyspnea.",
        [
          say("Dyspnea &mdash; at rest or on exertion, and how much exertion it takes"),
          say("Orthopnea &mdash; how many pillows the patient sleeps on"),
          say("Paroxysmal nocturnal dyspnea &mdash; waking at night short of breath"),
          say("Palpitations &mdash; and whether they are regular or irregular"),
          say("Syncope or presyncope"),
          say("Lower extremity edema"),
          say("Claudication &mdash; leg pain with walking that resolves with rest"),
          say("Cough, and whether anything is produced"),
          say("Nausea, vomiting or diaphoresis with the pain",
              hint="These are the associated symptoms that raise the concern rather than lower it."),
          say("Fever"),
        ]),
    background([
      say("Constitutional &mdash; fever, fatigue, weight change"),
      say("Respiratory &mdash; cough, hemoptysis, wheeze"),
      say("Gastrointestinal &mdash; reflux, epigastric pain",
          hint="Worth asking explicitly, because it belongs on the chest-pain differential."),
      say("Neurologic &mdash; focal weakness, visual change"),
      say("Denies symptoms outside the focused set, and says so out loud"),
    ]),
    dict(id="s4", title="Vital Signs, Risk Factors &amp; General Survey", src=(
        "The cardiac risk factors are a graded part of the history, not an afterthought. "
        "Ask them as a set so none is dropped."),
      blocks=[
        ("h4", "Vital signs"),
        ("items", [
          say("Restates the vital signs and interprets each one"),
          say("Comments on blood pressure, heart rate and oxygen saturation specifically"),
          say("States that blood pressure would be checked in both arms if indicated"),
        ]),
        ("h4", "Cardiac risk factors"),
        ("items", [
          say("Hypertension"),
          say("Hyperlipidemia"),
          say("Diabetes mellitus"),
          say("Tobacco use &mdash; current or past, and how much"),
          say("Family history of premature coronary artery disease"),
          say("Obesity and level of physical activity"),
          say("Prior cardiac events, procedures or stents"),
        ]),
        ("h4", "General survey"),
        ("items", [
          say("Comments on distress, colour, diaphoresis and work of breathing"),
        ]),
      ]),
    CARDIAC_EXAM,
    reasoning("For chest pain the differential must reach beyond the heart &mdash; pulmonary, "
              "gastrointestinal and musculoskeletal causes all belong on it."),
    plan([
      say("States immediate management if the presentation is acute"),
      say("States which medications would be started or adjusted"),
      say("Addresses risk factor modification &mdash; tobacco, diet, exercise, lipid and blood pressure control"),
      say("States what would prompt cardiology referral"),
      say("States red flags that would send the patient to the emergency department"),
    ]),
    presentation("cardiovascular"),
  ])


# -------------------------------------------------------------- PULMONARY OSCE
PULM_EXAM = dict(id="s5", title="Focused Physical Examination &mdash; Thorax &amp; Lungs", src=(
    "Maneuvers from the PD1 Lungs and Thorax lab checksheet. Performed with the patient "
    "seated. Work through inspection, palpation, percussion and auscultation in that order "
    "and do not let the sequence break."),
  blocks=[
    ("banner", "<b>Order &mdash;</b> inspection, palpation, percussion, auscultation. The lungs are "
               "one of the systems that uses all four, and the order is graded. Compare "
               "<b>side to side</b> at every level rather than working down one lung and then the other."),
    ("h4", "General"),
    ("items", [
      do("Performs hand hygiene before touching the patient"),
      do("Positions the patient seated, with the back exposed"),
      say("Performs a general survey &mdash; distress, ability to speak in full sentences, audible wheeze"),
    ]),
    ("h4", "Inspection"),
    ("items", [
      say("Inspects the shape and movement of the thorax, and any unilateral lag"),
      say("Inspects the rate, rhythm and effort of respiration"),
      say("Inspects for deformities, asymmetry, retractions, lesions and ecchymosis"),
      say("Inspects for use of accessory muscles"),
      say("Inspects the lips for cyanosis"),
      say("Inspects the nail beds for cyanosis and clubbing"),
      say("Inspects the anterior-posterior diameter",
          hint="An increased anterior-posterior diameter is the barrel chest &mdash; say what it suggests."),
    ]),
    ("h4", "Palpation"),
    ("items", [
      do("Palpates the posterior chest wall for tenderness or deformity"),
      do("Palpates the lateral chest wall for tenderness or deformity"),
      do("Palpates the anterior chest wall for tenderness or deformity"),
      do("Palpates thoracic expansion for symmetry of respiratory effort &mdash; <b>posteriorly</b>"),
      do("Palpates tactile fremitus bilaterally &mdash; <b>posteriorly, laterally and anteriorly</b>"),
      say("States what increased and decreased fremitus would each suggest",
          hint="Consolidation increases it; effusion and pneumothorax decrease it. Fremitus and percussion should agree &mdash; when they do, that is your answer."),
    ]),
    ("h4", "Percussion"),
    ("items", [
      do("Percusses the <b>posterior</b> chest wall, alternating sides"),
      do("Percusses the <b>lateral</b> chest wall, alternating sides"),
      do("Percusses the upper lobes, <b>anterior</b> chest wall, alternating sides"),
      do("Measures diaphragmatic excursion in centimetres",
         hint="Four to six centimetres is normal &mdash; the distance between the level of dullness on full expiration and on full inspiration."),
      say("States what dullness and hyperresonance would each suggest"),
    ]),
    ("h4", "Auscultation"),
    ("items", [
      do("Asks the patient to breathe through the mouth"),
      do("Asks the patient to cross their arms for the posterior examination"),
      say("Verbalizes <em>and</em> demonstrates one full cycle of inhalation and expiration at each point"),
      do("Auscultates the <b>posterior</b> chest wall bilaterally in a ladder pattern"),
      do("Auscultates the <b>lateral</b> chest wall bilaterally in a ladder pattern"),
      do("Auscultates the upper lobes, <b>anterior</b> chest wall, bilaterally in a ladder pattern"),
      say("Verbalizes whether breath sounds are appropriate for the area &mdash; vesicular, bronchovesicular, bronchial, tracheal"),
      say("Verbalizes listening for crackles, rhonchi, wheezes and pleural rubs"),
      say("Verbalizes the follow-up if adventitious sounds are present",
          script='"I will perform one of three tests: egophony, bronchophony, and/or whispered pectoriloquy."'),
      say("States which of those three would be performed and what a positive result would mean"),
    ]),
    ("h4", "Related"),
    ("items", [
      say("Inspects the anterior neck and palpates tracheal position",
          hint="Tracheal deviation is the finding that turns a pulmonary station into an emergency."),
      do("Palpates for cervical and supraclavicular lymphadenopathy"),
      do("Assesses the lower extremities for edema"),
    ]),
  ])

PULMONARY = dict(
  slug="pd2-pulmonary-osce", key="pd2PulmOsce",
  h1="Pulmonary OSCE &mdash; Focused Encounter Run-Sheet",
  eyebrow="PAJ 5310 &middot; Physical Diagnosis II &middot; Fall 2026",
  date="Tuesday 10 November 2026",
  sub=("The whole station in order, from the introduction through the one-minute case "
       "presentation. Examination maneuvers come from the PD1 Lungs and Thorax lab "
       "checksheet, reduced to what a focused respiratory encounter grades."),
  navlabels=["1 Open", "2 HPI", "3 History", "4 Vitals", "5 Lung Exam", "6 Reasoning", "7 Plan", "8 Present"],
  sections=[
    opening("a respiratory complaint"),
    hpi("Respiratory",
        "Shortness of breath and cough are the commonest stems. Pin down the timeline before anything else.",
        [
          say("Cough &mdash; dry or productive, and how long it has been present"),
          say("Sputum &mdash; colour, amount, and any change"),
          say("Hemoptysis"),
          say("Dyspnea &mdash; at rest or on exertion, and how much exertion it takes"),
          say("Wheeze"),
          say("Chest pain, and whether it is worse on inspiration",
              hint="Pleuritic versus not is the branch point."),
          say("Fever, chills or night sweats"),
          say("Weight loss"),
          say("Orthopnea and paroxysmal nocturnal dyspnea",
              hint="Asking these is how you keep heart failure on a respiratory differential."),
          say("Leg swelling or calf pain",
              hint="This is the pulmonary embolism question. Ask it explicitly."),
          say("Recent travel, immobility or surgery"),
          say("Sick contacts and known exposures"),
        ]),
    background([
      say("Constitutional &mdash; fever, night sweats, weight loss, fatigue"),
      say("Cardiovascular &mdash; chest pain, palpitations, edema"),
      say("Ear, nose and throat &mdash; congestion, sore throat, post-nasal drip"),
      say("Gastrointestinal &mdash; reflux",
          hint="Reflux, post-nasal drip and asthma are the three commonest causes of a chronic cough."),
      say("Denies symptoms outside the focused set, and says so out loud"),
    ]),
    dict(id="s4", title="Vital Signs, Exposures &amp; General Survey", src=(
        "Oxygen saturation and respiratory rate are the two that change the plan. Interpret "
        "them out loud rather than reading them back."),
      blocks=[
        ("h4", "Vital signs"),
        ("items", [
          say("Restates the vital signs and interprets each one"),
          say("Comments specifically on respiratory rate and oxygen saturation"),
          say("Comments on fever if present, and what it adds to the differential"),
        ]),
        ("h4", "Exposures and risk"),
        ("items", [
          say("Tobacco use &mdash; current or past, and pack-years"),
          say("Occupational and environmental exposures"),
          say("Known asthma, chronic obstructive pulmonary disease or other lung disease"),
          say("Immunisation status"),
          say("Prior tuberculosis exposure or testing"),
        ]),
        ("h4", "General survey"),
        ("items", [
          say("Comments on distress, ability to speak in full sentences, positioning and colour"),
        ]),
      ]),
    PULM_EXAM,
    reasoning("Keep cardiac and pulmonary embolism causes on the differential rather than "
              "confining it to the lungs."),
    plan([
      say("States immediate management if the patient is hypoxic or in distress"),
      say("States whether oxygen, bronchodilators or antimicrobials are indicated, and why"),
      say("Addresses smoking cessation where relevant"),
      say("States what would prompt admission rather than discharge"),
      say("States red flags that would bring the patient back or send them to the emergency department"),
    ]),
    presentation("respiratory"),
  ])


# ------------------------------------------------------------------- renderer
def render_items(items, counter):
    out = []
    for kind, text, script, hint, tag in items:
        counter[0] += 1
        cls = ' class="say"' if kind == "say" else ""
        inner = ""
        if tag:
            inner += '<span class="tag cn">%s</span>' % tag
        inner += text
        if script:
            inner += '<span class="script">%s</span>' % script
        if hint:
            inner += '<span class="hint">%s</span>' % hint
        out.append('    <li%s><span class="n">%d</span><input type="checkbox">'
                   '<span class="t">%s</span></li>' % (cls, counter[0], inner))
    return '  <ul class="ck">\n' + "\n".join(out) + '\n  </ul>'


def render_section(sec, n, counter):
    parts = ['<section id="%s">' % sec["id"],
             '  <h3><span class="num">%02d</span> %s</h3>' % (n, sec["title"])]
    if sec.get("src"):
        parts.append('  <p class="src">%s</p>' % sec["src"])
    for block in sec["blocks"]:
        kind = block[0]
        if kind == "h4":
            parts.append('  <h4>%s</h4>' % block[1])
        elif kind == "ref":
            parts.append('  <div class="ref">%s</div>' % block[1])
        elif kind == "banner":
            parts.append('  <div class="banner">%s</div>' % block[1])
        elif kind == "items":
            parts.append(render_items(block[1], counter))
    parts.append('</section>')
    return "\n".join(parts)


donor = open(DONOR, encoding="utf-8").read()
HEAD = donor[:donor.index("<body>")]
CHROME = donor[donor.index("<body>"):donor.index('<p class="sitebar">')]
TAIL = donor[donor.index('<div id="quiz-footer-logo"'):]
assert donor.count('<div id="quiz-footer-logo"') == 1
assert 'pd1HeadToToe:ticks' in TAIL


def build(spec):
    counter = [0]
    body_sections = "\n\n".join(
        render_section(s, i + 1, counter) for i, s in enumerate(spec["sections"]))

    head = re.sub(r"<title>.*?</title>",
                  "<title>%s</title>" % re.sub(r"&mdash;", "—", spec["h1"]),
                  HEAD, count=1, flags=re.S)

    nav = "\n".join('    <li><a href="#s%d">%s</a></li>' % (i + 1, lbl)
                    for i, lbl in enumerate(spec["navlabels"]))

    page = head + CHROME + '''<p class="sitebar"><a href="../index.html">&larr; Back to Homepage</a></p>

<header class="mast">
  <p class="eyebrow">%(eyebrow)s</p>
  <h1>%(h1)s</h1>
  <p class="sub">%(sub)s</p>
</header>

<div class="legend">
  <span class="key"><span class="sw grey"></span> Must be said out loud</span>
  <span class="key"><span class="sw white"></span> Performed &mdash; inspect / palpate / percuss / auscultate</span>
  <span class="spacer"></span>
  <button id="fSay" aria-pressed="false">Spoken only</button>
  <button id="fDo" aria-pressed="false">Hands-on only</button>
  <button id="reset">Clear ticks</button>
  <button onclick="window.print()">Print</button>
</div>

<div class="banner"><b>Station &mdash;</b> %(date)s, 20&ndash;25 minutes. The chief complaint and
vital signs are given on a separate form. You may bring <b>diagnostic equipment and a pen</b>,
nothing else. The &ldquo;patient&rdquo; gives no verbal responses except identifying data &mdash;
the facilitator answers for them, and you should <b>always be looking at and interacting with the
patient, not the facilitator</b>. Faculty do not answer questions about the exam or technique once
testing has started.</div>

<nav>
  <ol>
%(nav)s
    <li id="progress">0 / 0</li>
  </ol>
</nav>

%(sections)s

</div>

''' % dict(eyebrow=spec["eyebrow"], h1=spec["h1"], sub=spec["sub"],
           date=spec["date"], nav=nav, sections=body_sections)

    tail = TAIL.replace("pd1HeadToToe:ticks", "%s:ticks" % spec["key"])
    page += tail

    path = os.path.join(OUTDIR, spec["slug"] + ".html")
    open(path, "w", encoding="utf-8").write(page)
    return path, counter[0], page


if __name__ == "__main__":
    for spec in (ENT, CARDIAC, PULMONARY):
        path, n, page = build(spec)
        says = page.count('<li class="say">')
        print("%-26s %3d items (%d spoken, %d hands-on)  %d KB"
              % (os.path.basename(path), n, says, n - says, len(page) // 1024))
        assert "pd1HeadToToe" not in page, "save key not swapped in %s" % spec["slug"]
        assert page.count("</section>") == len(spec["sections"])
