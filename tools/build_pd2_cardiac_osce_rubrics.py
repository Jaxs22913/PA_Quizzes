#!/usr/bin/env python3
"""Build the Cardiac OSCE rubric sheet: the five original PD1 lab sheets the Cardiac OSCE draws on,
combined on one page WORD FOR WORD (Jaxon, 2026-10-20: "takes the original rubrics and combines Cardiac,
Respiratory, Peripheral Vascular, Skin, General Survey").

Sources (PAJ 5300 Physical Diagnosis I, Summer 2026; kept out of the repo in
~/Desktop/PA Quizzes/Semester 1/Checksheets/):
  PAJ 5300 General Survey Vitals Pulse Lab Sheet 2026.pdf   -> Introduction, General Survey, Vital Signs
  PAJ_5300_Cardiac & Peripheral_Vascular Lab Sheet 2026.docx -> Cardiovascular, Peripheral Vascular
  PAJ5300 Lungs and Thorax Lab Handout 2026.docx            -> Thorax & Lungs
  PAJ 5300 Skin, Hair, Nails Lab Sheet 2026.pdf              -> Skin, Hair & Nails

Item text, quoted scripts and "Indication" lines are copied exactly, typos included (the run-sheet,
pd2-cardiac-osce.html, is the reworded whole-station version). The only additions are marked as ours:
"also <sheet>" tags where two sheets grade the same step, one source line per section, and the
abbreviation key at the end. Order: the General Survey sheet first (every station opens with it),
then Jaxon's order: Cardiac, Respiratory, Peripheral Vascular, Skin.

Rendering reuses tools/build_pd2_osce.py (the PD1 head-to-toe skeleton: ticks, filters, print, dark mode).
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_pd2_osce as B

# item: (kind, text, script, hint, also)   kind "say" = must be said out loud, "do" = performed
def say(t, script=None, hint=None, also=None): return ("say", t, script, hint, also)
def do(t, script=None, hint=None, also=None):  return ("do", t, script, hint, also)

GS_SRC = "PAJ 5300 Introduction/General Survey/Vital Signs/Peripheral Pulses Lab Sheet (Summer 2026)"
CV_SRC = "PAJ 5300 Cardiovascular Examination Lab Sheet (Summer 2026)"
PV_SRC = "PAJ 5300 Peripheral Vascular Examination Lab Sheet (Summer 2026)"
LU_SRC = "PAJ 5300 Lungs and Thorax Lab Handout (Summer 2026)"
SK_SRC = "PAJ 5300 Skin, Hair, and Nails Lab Sheet (Summer 2026)"

SECTIONS = [
  dict(id="s1", title="Introduction", src="Original: " + GS_SRC + ".", blocks=[
    ("items", [
      say("Introduces self to patient", also="also Cardiac"),
      say("Identifies the patient with two patient identifiers (name and DOB)"),
      say("Explains purpose of examination"),
      say("Student verbalizes they would ensure proper lighting", also="also Cardiac"),
      do("Student verbalizes and/or demonstrates washing of the hands prior to examination", also="also Cardiac"),
      say("Requests patient to disrobe prior to examination"),
      do("Demonstrates professionalism throughout the examination"),
    ])]),
  dict(id="s2", title="General Survey", src="Original: " + GS_SRC + ".", blocks=[
    ("items", [
      do("Inspects for general health status, body habitus, physical deformities"),
      say("Verbalizes “I will evaluate the patient’s orientation and level of consciousness during "
          "interview/conversation” (person/place/time/event, LOC – alert/lethargic/obtunded, stuporous/comatose)"),
      do("Inspects facial expression and observes for signs of distress"),
      do("Inspects if stated age matches apparent age"),
      do("Inspects grooming and hygiene"),
    ])]),
  dict(id="s3", title="Vital Signs &amp; Peripheral Pulses", src="Original: " + GS_SRC + ".", blocks=[
    ("h4", "Height, Weight, BMI"),
    ("items", [say("Student verbalizes they would obtain height, weight, and calculate BMI")]),
    ("h4", "Body Temperature &amp; Pulse Oximetry"),
    ("items", [say("Student verbalizes they would obtain a temperature &amp; pulse ox.")]),
    ("h4", "Heart Rate"),
    ("items", [
      do("Locates the radial artery to check the heart rate (pulse)"),
      do("Assesses pulse with the pads of the index and middle fingers"),
      say("Student verbalizes the calculation they are using to assess the pulse (Must verbalize 30 seconds x2)"),
    ]),
    ("h4", "Respiratory Rate"),
    ("items", [
      do("Ensures adequate exposure of the chest"),
      do("Maintains position as if counting pulse rate"),
      say("Student verbalizes the calculation they are using to assess the respiratory rate"),
    ]),
    ("h4", "Blood Pressure"),
    ("items", [
      do("Positions patient properly – seated with back supported &amp; feet on floor, legs uncrossed"),
      say("Assesses for appropriate cuff size (Must verbalize)"),
      do("Locates the brachial artery"),
      do("Properly positions BP cuff (2.5 cm above antecubital fossa), artery line properly placed"),
      do("Supports the arm with the brachial artery at or slightly above heart level"),
      say("Determines the palpable radial pulse obliteration pressure (aka palpable systolic pressure and "
          "verbalizes reading (inflate cuff while palpating the radial artery until pulse no longer palpable)"),
      do("Deflates cuff completely and waits 15-30 seconds"),
      do("Then re-inflates cuff to 30mm Hg above palpable systolic pressure"),
      do("Assesses for onset of Korotkoff sounds to determine systolic blood pressure"),
      do("Deflates cuff slowly"),
      do("Assesses for cessation of Korotkoff sounds to determine diastolic blood pressure"),
      do("Repeat measurement on opposite arm"),
      say("Student verbalizes if orthostatic measurement was indicated, they would also assess blood pressure "
          "supine and standing after waiting 1-3 minute between positions"),
    ]),
    ("h4", "Peripheral Pulses*"),
    ("ref", "Palpates the following pulses bilaterally noting: rate, rhythm, and quality"),
    ("items", [
      do("Brachial", also="also PV"),
      do("Radial", also="also PV"),
    ]),
    ("ref", "A complete peripheral vascular exam would also include assessment of the carotid, ulnar, femoral, "
            "popliteal, posterior tibialis, and dorsalis pedis pulses.<br><br>* The complete peripheral vascular "
            "exam is covered in detail during the Physical Examination of the Heart and Peripheral Vasculature "
            "lecture and lab. For the purposes of the vital signs, students must be able to locate the radial and "
            "brachial pulses."),
  ]),
  dict(id="s4", title="Cardiovascular", src="Original: " + CV_SRC + ", items 1&ndash;26.", blocks=[
    ("h4", "Preparation"),
    ("items", [
      do("Place the patient in the supine position for the cardiac examination with the head elevated 30 degrees"),
      do("Stand on the right side if right-handed, or left side if left-handed of the patient during the examination."),
      do("Perform hand hygiene and ensure proper lighting.", also="also Intro"),
      say("Introduce yourself. Obtain appropriate history questions and interpret vitals.", also="also Intro"),
      do("Visualize/identify carotid and jugular pulses."),
    ]),
    ("h4", "Inspection"),
    ("ref", "Indication: Inspect the precordium for abnormal wall motion or apical impulse"),
    ("items", [
      do("Inspect the precordium for abnormal wall motion and apical impulse using tangential lighting."),
    ]),
    ("h4", "Carotid Pulse"),
    ("ref", "Indication: to check the carotid pulse including the carotid upstroke, it’s amplitude and contour, "
            "and the presence of thrills."),
    ("items", [
      do("Inspect the carotid pulses in the neck."),
      do("Ask the patient to hold their breath for ten seconds. Auscultating the carotids with the diaphragm and bell."),
      do("With the head of the bed still at 30 degrees, palpate each carotid artery in the lower 1/3 of the neck "
         "using your index and middle finger. Check bilaterally, but only palpate one carotid at a time."),
    ]),
    ("h4", "Palpation of the precordium heaves and lifts using finger pads"),
    ("ref", "Indication: palpate for various indicators such as heaves, palpable S1, S2, S3, or S4, the apical "
            "impulse and PMI."),
    ("items", [
      do("2nd intercostal space, right sternal border - Aortic Area"),
      do("2nd intercostal space, left sternal border - Pulmonic Area"),
      do("3rd intercostal space, left sternal border - Erb’s Point"),
      do("4th intercostal space, left sternal border - Tricuspid Area"),
      do("5th intercostal space, left mid-clavicular line - Mitral Area"),
      do("Note the size and intensity of the apical impulse by palpation. Use palmar surface of several fingers.  "
         "The apical impulse should be described as a light tap."),
      do("Note the location of the point of maximal impulse (PMI)"),
    ]),
    ("h4", "Palpation of the precordium for thrills, using the ball of your hand"),
    ("ref", "Indication: palpate for various indicators such as a thrill, palpable S1, S2, S3, or S4, the apical "
            "impulse and PMI."),
    ("items", [
      do("2nd intercostal space, right sternal border - Aortic Area"),
      do("2nd intercostal space, left sternal border - Pulmonic Area"),
      do("3rd intercostal space, left sternal border - Erb’s Point"),
      do("4th intercostal space, left sternal border - Tricuspid Area"),
      do("5th intercostal space, left mid-clavicular line - Mitral Area"),
    ]),
    ("h4", "Auscultation of the precordium with the Diaphragm and Bell"),
    ("ref", "Indication: rate, rhythm, intensities of S1/S2, systole, diastole, any extra sounds, any murmurs"),
    ("items", [
      do("2nd intercostal space, right sternal border - Aortic Area"),
      do("2nd intercostal space, left sternal border - Pulmonic Area"),
      do("3rd intercostal space, left sternal border - Erb’s Point"),
      do("4th intercostal space, left sternal border - Tricuspid Area"),
      do("5th intercostal space, left mid-clavicular line - Mitral Area"),
    ]),
  ]),
  dict(id="s5", title="Thorax &amp; Lungs (Respiratory)", src="Original: " + LU_SRC + ".", blocks=[
    ("h4", "Inspection"),
    ("items", [
      do("Inspects for the shape and movement of the thorax and any unilateral lag in movement."),
      do("Inspects for rate, rhythm, and effort of respiration."),
      do("Inspects for deformities, asymmetry, abnormal retractions, lesions, and any areas of ecchymosis."),
      do("Inspects for use of accessory muscles."),
      do("Inspects lips for cyanosis."),
      do("Inspects bilateral nail beds for cyanosis and clubbing.", also="also PV &middot; Skin"),
      do("Inspects anterior-posterior (AP) diameter."),
    ]),
    ("h4", "Palpation"),
    ("items", [
      do("Palpates posterior chest wall for tenderness or deformities"),
      do("Palpates lateral chest wall for tenderness or deformities"),
      do("Palpates anterior chest wall for tenderness or deformities"),
      do("Palpates thoracic expansion for symmetry of respiratory effort - POSTERIORLY"),
      do("Palpates tactile fremitus bilaterally – POSTERIORLY, LATERALLY, and ANTERIORLY"),
    ]),
    ("h4", "Percussion"),
    ("items", [
      do("Percusses POSTERIOR chest wall, alternating sides."),
      do("Percusses LATERAL chest wall, alternating sides."),
      do("Percusses upper lobes ANTERIOR chest wall, alternating sides."),
      do("Measures diaphragmatic excursion - in centimeters (4 - 6 cm)",
         hint="Estimates the diaphragmatic excursion by determining the distance between the level of dullness "
              "on full expiration and the level of dullness on full inspiration"),
    ]),
    ("h4", "Auscultation"),
    ("items", [
      say("Asks patient to breathe through mouth during auscultation"),
      say("Asks the patient to cross arms for posterior examination"),
      say("Verbalizes and demonstrates performing one full cycle of inhalation and expiration at each point."),
      do("Auscultates POSTERIOR chest wall, alternating sides bilaterally in a ladder pattern"),
      do("Auscultates LATERAL chest wall, alternating sides bilaterally in a ladder pattern"),
      do("Auscultates upper lobes ANTERIOR chest wall, alternating sides bilaterally in a ladder pattern"),
      say("Verbalizes if breath sounds appropriate for area of auscultation (vesicular, bronchovesicular, "
          "bronchial, tracheal)"),
      say("Verbalizes listening for crackles, rhonchi, wheezes, pleural rubs"),
      say("Verbalizes if adventitious sounds are present, student states, “I will perform one of three tests, "
          "egophony, bronchophony, and /or whispered pectoriloquy.”"),
    ]),
  ]),
  dict(id="s6", title="Peripheral Vascular",
       src=("Original: " + PV_SRC + ". The original numbers it 1&ndash;18 with no items 8 or 13; "
            "nothing is missing."), blocks=[
    ("h4", "Inspection"),
    ("ref", "Indication: Note for size, symmetry, any swelling, venous pattern, color of skin, texture of skin, "
            "temperature of feet and legs, hair growth, ulcerations, and nail beds of the upper and lower extremities."),
    ("items", [
      do("Inspect for size, symmetry, and edema of the extremities."),
      do("Inspect for venous pattern and hair growth."),
      do("Inspect skin color for erythema, cyanosis, and jaundice."),
      do("Inspect for pigmentation changes and ulcerations."),
      do("Inspect the nail beds.", also="also Lungs &middot; Skin"),
    ]),
    ("h4", "Palpation of pulses bilaterally"),
    ("ref", "Indication: Assess the amplitude, rate, rhythm, and quality"),
    ("items", [
      do("Brachial", also="also Vitals"),
      do("Radial", also="also Vitals"),
      do("Femoral"),
      do("Popliteal"),
      do("Posterior tibialis"),
      do("Dorsalis pedis"),
    ]),
    ("h4", "Palpation of lymph nodes bilaterally"),
    ("ref", "Indication: note the presence of nodes, discreteness, note size, consistency, and tenderness"),
    ("items", [
      do("Epitrochlear"),
      do("Vertical inguinal"),
      do("Horizontal inguinal"),
    ]),
    ("h4", "Palpation checking for capillary refill bilaterally"),
    ("ref", "Indication: Note color typically returns within 2-3 seconds."),
    ("items", [
      do("Palpate the nailbeds upper extremities for capillary refill"),
      do("Palpate the nailbeds lower extremities for capillary refill"),
    ]),
  ]),
  dict(id="s7", title="Skin, Hair &amp; Nails", src="Original: " + SK_SRC + ".", blocks=[
    ("ref", "&bull; Skin should be inspected for: Color, uniformity, thickness, symmetry, hygiene, lesions, rashes, "
            "dryness, odors<br>&nbsp;&nbsp;o Inspection of body hair distribution may be performed with skin "
            "inspection<br>&bull; Skin should be palpated for: Moisture, temperature, texture, turgor, mobility<br>"
            "&bull; Nails should be inspected for: Color, condition, cleanliness, length, lesions, redness/swelling "
            "of nail folds, nail base angle<br>&bull; Nails should be palpated for: Texture, firmness, thickness, "
            "uniformity, adherence to nail bed<br>&bull; Hair should be inspected for: Color, distribution, quantity"
            "<br>&bull; Hair Should be palpated for: Texture"),
    ("banner", "<b>SKIN AND NAILS &ndash; Verbalize Procedure While Performing All Techniques</b><br>"
               "Steps 1-11 performed with patient sitting<br>Steps 12-15 performed with patient standing"),
    ("items", [
      do("Inspect and palpate the hair and scalp – must part hair in multiple locations",
         script="“I am inspecting the hair for color, distribution and quantity.  I am inspecting the scalp for "
                "hygiene, lesions, dandruff, nits or lice. I am palpating…”"),
      do("Inspect the head, face, and neck",
         script="“I am inspecting the eyebrows and eyelashes for color, distribution and quantity”<br>"
                "“I am inspecting the skin of the head, face and neck for….”"),
      do("Inspect the upper back", script="“I am inspecting the skin for….”"),
      do("Inspect the shoulders, axillae, and upper extremities"),
      do("Inspect the hands and fingers (all surfaces and between digits)"),
      do("Inspect and palpate fingernails", also="also Lungs &middot; PV",
         script="“I am inspecting the fingernails for…”<br>“I am palpating the fingernails for…”"),
      do("Inspect the chest"),
      do("Inspect the abdomen"),
      do("Inspect the anterior/medial/lateral thighs and lower legs"),
      do("Inspect the feet and toes (all surfaces and between digits)"),
      do("Inspect and palpate toenails"),
      do("Inspect the lower back and posterior legs"),
      say("Verbalize examination of the buttocks, breasts, and genitalia",
          script="“For a full-body examination, the buttocks, breasts, and genitalia would also be assessed”"),
      do("Palpate skin temperature using dorsal surface of hands, bilaterally over upper and lower extremities "
         "(anterior &amp; posterior)",
         script="“I am palpating the skin for temperature and evaluating for symmetry in the extremities”"),
      do("Palpate skin for texture, mobility &amp; turgor, bilaterally over upper and lower extremities "
         "(anterior &amp; posterior)",
         script="“I am palpating the skin to assess texture, mobility and turgor”"),
    ]),
    ("ref", "<b>Abbreviations on the original sheets</b> (key added here, not on the sheets): AP, anterior-posterior; "
            "BMI, body mass index; BP, blood pressure; DOB, date of birth; LOC, level of consciousness; "
            "PMI, point of maximal impulse; S1&ndash;S4, first to fourth heart sounds; PV, peripheral vascular."),
  ]),
]

SPEC = dict(
  slug="pd2-cardiac-osce-rubrics", key="pd2CardiacOsceRubrics",
  h1="Cardiac OSCE &mdash; Original Rubrics, Combined",
  eyebrow="PAJ 5310 &middot; Physical Diagnosis II &middot; Fall 2026",
  date="Wednesday 21 October 2026",
  sub=("The five PD1 lab sheets this station draws on, word for word, on one page: General Survey "
       "(with the introduction and vital signs), Cardiovascular, Thorax &amp; Lungs, Peripheral Vascular, and "
       "Skin, Hair &amp; Nails. Nothing is reworded. A <span class=\"tag dup\">also &hellip;</span> tag marks a step "
       "two sheets both grade: do it once, out loud. For the whole station in order see the "
       "<a href=\"pd2-cardiac-osce.html\">run-sheet</a>; for what each special maneuver finds, the "
       "<a href=\"pd2-cardiac-osce-maneuvers.html\">special maneuvers guide</a>."),
  navlabels=["1 Intro", "2 General Survey", "3 Vitals", "4 Cardiac", "5 Lungs", "6 Peripheral Vascular", "7 Skin"],
  sections=SECTIONS,
)


def render_items(items, counter):
    out = []
    for kind, text, script, hint, also in items:
        counter[0] += 1
        cls = ' class="say"' if kind == "say" else ""
        inner = ('<span class="tag dup">%s</span>' % also if also else "") + text
        if script: inner += '<span class="script">%s</span>' % script
        if hint: inner += '<span class="hint">%s</span>' % hint
        out.append('    <li%s><span class="n">%d</span><input type="checkbox">'
                   '<span class="t">%s</span></li>' % (cls, counter[0], inner))
    return '  <ul class="ck">\n' + "\n".join(out) + '\n  </ul>'


if __name__ == "__main__":
    B.render_items = render_items          # same markup, but our "also" tag instead of the cranial-nerve tag
    path, n, page = B.build(SPEC)
    # The run-sheets carry no links in the intro; give these the page accent so they read in dark mode too.
    css = ("<style>.mast .sub a{color:var(--petrol);text-decoration:underline;text-underline-offset:2px;"
           "text-decoration-thickness:1px}</style>\n")
    assert page.count("</head>") == 1
    page = page.replace("</head>", css + "</head>")
    open(path, "w", encoding="utf-8").write(page)
    # The run-sheets' station banner is right for this page too; its title needs no em dash rewrite.
    says = page.count('<li class="say">')
    assert "pd1HeadToToe" not in page, "save key not swapped"
    assert page.count("</section>") == len(SECTIONS)
    ids = re.findall(r'<section id="(s\d+)"', page)
    assert ids == ["s%d" % (i + 1) for i in range(len(SECTIONS))], ids
    per = {s["id"]: sum(len(b[1]) for b in s["blocks"] if b[0] == "items") for s in SECTIONS}
    print("%s  %d items (%d spoken, %d hands-on)  %d KB  per section %s"
          % (os.path.basename(path), n, says, n - says, len(page) // 1024, per))
