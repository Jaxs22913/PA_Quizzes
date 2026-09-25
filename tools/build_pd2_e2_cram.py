#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Physical Diagnosis 2, Exam 2 cram sheet.

Condensed from the Exam 2 study guide (tools/build_pd2_e2_guide.py) and nothing
else -- no row here says anything the guide does not ([[cram_sheets_feature]]).
Numbers are kept exactly as the slides give them: 0.90-1.40, 2-3 seconds,
10% of body weight, the 2/4/6/8 mm pitting depths, grade 4 = first thrill.

Lecture 5 only so far; Pulmonary (6) and Hematology (7) topics get appended
when those decks land.

The first topic carries the lecturer's emphasis (the rows marked with a star),
the same convention the Exam 1 sheet uses for its Lecture 3 and 4 marks. The
recording named NOTHING as on or off the exam, so the stars mark repetition,
not a promise.

NO MARKDOWN IN ROWS: render() HTML-escapes them, so asterisks would ship
literally. Asserted below.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

OUT = os.path.join(ROOT, "Physical Diagnosis 2 Exam 2", "pd2-exam-2-cram-sheet.html")

topics = [
 {"id": "l5-emphasis", "label": "★ What the lecture kept coming back to", "color": "#b8860b",
  "rows": [
    ["★ The sound is not the diagnosis",
     "Document what you hear, when and where: 'grade 4/6 systolic ejection murmur, crescendo-decrescendo, loudest at the right 2nd intercostal space, radiating to the carotids, with a thrill.' The disease name (aortic stenosis) goes in the differential, not the physical examination."],
    ["★ Try before you buy",
     "Tricuspid is the FIRST valve blood crosses on its way back to the heart (tricuspid before bicuspid/mitral). Said twice: 'That is important, that is important.'"],
    ["★ Hypertrophic obstructive cardiomyopathy",
     "Learn this murmur so you do not sign off a sports physical wrongly. Aortic and pulmonic stenosis worry you at a point; this one worries you, period. Murmur LOUDER with Valsalva or standing = echocardiogram, no activity until done."],
    ["★ Mitral vs tricuspid regurgitation",
     "Both pansystolic. Mitral (apex) radiates to the LEFT AXILLA; tricuspid (lower left sternal border) does NOT. Loudest spot plus the axilla decides it."],
    ["★ The thrill is the jump",
     "Loudness raises the grade, but a palpable thrill makes it at least grade 4/6. An arteriovenous fistula is what a thrill feels like."],
    ["★ Weight before swelling",
     "Up to 10% of body weight can accumulate before pitting shows. Two pounds overnight is water. Daily morning weight; know a dialysis or heart failure patient's dry weight."],
    ["★ Syncope: before and after",
     "Prodrome (lightheaded, pale, clammy) = vasovagal. On standing = orthostatic. Sudden, no warning = arrhythmia. Confused afterward = postictal, think seizure. Feel faint? Sit down."],
    ["★ Negative Homans does not reassure",
     "Do it when you already suspect deep vein thrombosis, on the worrying leg. Positive confirms suspicion; negative in a high-risk story, still worried."],
    ["Time on topic",
     "No exam-scope statements in 138 minutes. Cardiac content took about 110 minutes; peripheral vascular about 25 ('almost entirely review... the cardiac stuff is a lot of new')."],
  ]},

 {"id": "l5-history", "label": "The Cardiac History", "color": "#3a5a40",
  "rows": [
    ["Symptoms to ask", "Chest pain, palpitations, dyspnea, orthopnea, paroxysmal nocturnal dyspnea, edema, syncope. Quantify the baseline level of activity."],
    ["Chest pain", "Most common symptom of coronary artery disease. Always consider angina, myocardial infarction, dissecting aortic aneurysm, pulmonary embolism. Open-ended first, then details; ask the patient to point."],
    ["Atypical presentation", "Women over 65: upper back, neck or jaw pain, shortness of breath, paroxysmal nocturnal dyspnea, nausea, vomiting, fatigue."],
    ["Palpitations", "Unpleasant awareness of the heartbeat (skipping, racing, fluttering, pounding). Anxiety and hyperthyroidism cause them; not necessarily heart disease. Get an electrocardiogram."],
    ["Dyspnea", "Uncomfortable awareness of breathing inappropriate to the level of exertion. Cardiac or pulmonary."],
    ["Orthopnea", "Dyspnea supine, better sitting up. Count the pillows, and ask what they are for."],
    ["Paroxysmal nocturnal dyspnea", "Sudden dyspnea waking the patient, usually 1-2 hours after going to bed; sits up or goes to the window. May wheeze and cough."],
    ["Syncope", "Transient loss of consciousness with recovery. Most common: neurocardiogenic (vasovagal). Arrhythmia in about 20%."],
  ]},

 {"id": "l5-cycle", "label": "Cardiac Cycle & Heart Sounds", "color": "#46704f",
  "rows": [
    ["Systole vs diastole", "Named for the VENTRICLES. Systole: contraction, S1 to S2. Diastole: relaxation and filling, S2 to S1."],
    ["S1 (lub)", "Mitral + tricuspid closure. Diaphragm, apex. Usually not split. Precedes the carotid pulse."],
    ["S2 (dub)", "Aortic (A2, usually louder) + pulmonic (P2) closure. Diaphragm, base. Follows the carotid pulse."],
    ["Physiologic splitting", "S2 split on INSPIRATION, fused on expiration. Normal. Best at the pulmonic area."],
    ["Pathologic splitting", "Audible split on EXPIRATION: suggests heart disease. Tends to be fixed."],
    ["Early ejection sound", "Just after S1; high, clicking; diaphragm. Aortic: base and apex, no change with inspiration. Pulmonic: 2nd-3rd intercostal spaces, decreases with inspiration."],
    ["Click", "Mid to late systolic, at or medial to the apex; high, diaphragm. Mitral valve prolapse; followed by a late systolic murmur crescendoing to S2."],
    ["S3 ventricular gallop", "After S2: Ken-TUC-ky. Bell, apex, left lateral decubitus. Normal to about 35-40 and in late pregnancy; over 40 = heart failure, volume overload."],
    ["S4 atrial gallop", "Before S1: Ten-nes-SEE. Dull, low; bell, apex, left lateral decubitus. Stiff ventricle: hypertension, aortic stenosis. Normal in athletes and older adults. Right-sided S4 at lower left sternal border, louder with inspiration."],
    ["Opening snap", "Very early diastole, stenotic MITRAL valve. HIGH pitch, diaphragm. Can be mistaken for P2. Fades as the leaflets calcify."],
  ]},

 {"id": "l5-impulse", "label": "Apical Impulse & Point of Maximal Impulse", "color": "#5f8a68",
  "rows": [
    ["Normal", "5th intercostal space at or just medial to the left midclavicular line. Marks the LEFT border of the heart. About 2.5 cm (a quarter), brisk and tapping."],
    ["Displaced", "Enlarged heart: lateral and possibly inferior (for example 6th space, anterior axillary line). Document where you find it."],
    ["Can't find it", "Left lateral decubitus; then exhale fully and hold."],
    ["Hyperkinetic", "Increased stroke volume; not necessarily disease. Anxiety, hyperthyroidism, severe anemia. Normal location, under 2/3 of systole."],
    ["Sustained (pressure load)", "Hypertrophy, increased afterload. Left: aortic stenosis, hypertension. Right: pulmonic stenosis, pulmonary hypertension."],
    ["Diffuse (volume load)", "Dilation, increased preload. Left: displaced left and down; aortic or mitral regurgitation, cardiomyopathy. Right: atrial septal defect."],
  ]},

 {"id": "l5-auscultation", "label": "Auscultation — Areas, Diaphragm & Bell", "color": "#2f6b5e",
  "rows": [
    ["Why the areas are where they are", "Not over the valves: the next place DOWNSTREAM along the blood flow with no bone in the way. Aortic stenosis can radiate to both carotids."],
    ["The five areas", "Aortic (right 2nd space), pulmonic (left 2nd), Erb's point (between pulmonic and mitral), tricuspid (lower left sternal border), mitral (apex)."],
    ["Bell", "Low pitch. Light pressure, no gaps. Apex, then medially along the lower sternal border. S3, S4, mitral stenosis."],
    ["Diaphragm", "High pitch. Press firmly, whole precordium. S1, S2, clicks, opening snap, aortic and mitral regurgitation, friction rubs."],
    ["Technique", "Quiet room, skin contact always (never over clothing), isolate each sound, close your eyes. Unsure if systolic? Palpate the carotid while listening."],
  ]},

 {"id": "l5-murmur-describe", "label": "Describing & Grading Murmurs", "color": "#c08a2e",
  "rows": [
    ["Murmur / thrill / bruit", "Murmur: turbulent flow over a valve, heard. Thrill: its vibration, felt with the balls of the hand held still. Bruit: turbulent flow in a vessel."],
    ["Causes of a murmur", "Partially obstructed valve; increased flow through a normal valve (child); ejection into a dilated chamber; regurgitation; shunting to a lower pressure chamber."],
    ["Seven characteristics", "Timing, shape, location, radiation, intensity, pitch, quality."],
    ["Shapes", "Crescendo-decrescendo (diamond); decrescendo (starts maximal, fades); plateau (unchanging); crescendo (grows)."],
    ["Levine grades", "1 heard only after tuning in. 2 heard immediately. 3 moderately loud. 4 loud WITH THRILL. 5 thrill, heard with stethoscope partly off. 6 thrill, heard entirely off."],
    ["Pitch and quality", "High, medium, low. Blowing, harsh, rumbling, musical."],
    ["Innocent", "No structural abnormality; grade 1-3; softer on standing, sitting up or Valsalva; childhood. Defined by no symptoms or structural disease, not by grade. A thrill = not innocent."],
    ["Physiologic vs pathologic", "Physiologic: anemia, pregnancy, fever, hyperthyroidism. Pathologic: structural (aortic or pulmonic stenosis, hypertrophic cardiomyopathy, atrial septal defect)."],
  ]},

 {"id": "l5-murmurs", "label": "The Murmurs One by One", "color": "#7a3b3b",
  "cols": ["Lesion", "Timing & shape", "Pitch", "Loudest", "Radiation", "Maneuvers"],
  "rows": [
    {"group": "SYSTOLIC"},
    ("Aortic stenosis", "Midsystolic, crescendo-decrescendo", "Medium, harsh", "Aortic area", "Carotids, down left sternal border, even apex", "Sitting forward; louder with squatting and leg raise"),
    ("Pulmonic stenosis", "Midsystolic, crescendo-decrescendo", "Medium, harsh", "Pulmonic area", "Left shoulder and neck if loud", "None"),
    ("Hypertrophic cardiomyopathy", "Midsystolic, crescendo-decrescendo", "Medium, harsh", "Erb's point, tricuspid area", "Down left sternal border to apex; NEVER the neck", "Softer with squatting; LOUDER with Valsalva and standing"),
    ("Tricuspid regurgitation", "Pansystolic, plateau", "Medium, blowing", "Lower left sternal border", "Right sternum, xiphoid; NOT the axilla", "May increase slightly with inspiration"),
    ("Mitral regurgitation", "Pansystolic, holosystolic", "Medium-high, harsh", "Apex", "LEFT AXILLA", "Louder with handgrip or squatting; apical thrill if loud"),
    {"group": "DIASTOLIC"},
    ("Aortic regurgitation", "Early diastolic, decrescendo; grade 1-3", "High, blowing (like breath sounds)", "Aortic area, down left spaces", "Apex if loud", "Sit forward, exhale, hold"),
    ("Pulmonic regurgitation", "Early diastolic, decrescendo; grade 1-3", "High", "Pulmonic area", "None", "None; may increase with inspiration"),
    ("Mitral stenosis", "Mid to late diastolic, decrescendo; grade 1-4", "Low rumble: BELL", "Apex", "Little or none", "Bell at the apical impulse, left lateral decubitus"),
    ("Tricuspid stenosis", "Mid to late diastolic, decrescendo; grade 1-4", "Low rumble after an opening snap: bell", "Lower left sternal border near xiphoid", "Little or none", "Bell"),
    {"group": "OTHER"},
    ("Pericardial friction rub", "Scratchy, both systole and diastole; plateau", "High: diaphragm", "Erb's point", "Little", "Louder leaning forward, exhaled, breath held"),
  ]},

 {"id": "l5-maneuvers", "label": "Maneuvers", "color": "#5b4a8a",
  "rows": [
    ["Valsalva (strain)", "Forceful expiration against a closed airway: bear down, or push against your hand on the mid-abdomen. Less preload. Hypertrophic cardiomyopathy LOUDER; aortic stenosis softer or unchanged."],
    ["Standing from squatting", "Less venous return, less preload. Hypertrophic cardiomyopathy LOUDER; aortic stenosis SOFTER; mitral prolapse click earlier, murmur longer."],
    ["Squatting from standing or leg raise", "More venous return, more preload. Hypertrophic cardiomyopathy SOFTER; aortic stenosis LOUDER; mitral prolapse click later, murmur shorter."],
    ["Isometric handgrip", "Raises resistance. Increases mitral regurgitation, pulmonic stenosis, ventricular septal defect, aortic regurgitation, mitral stenosis."],
    ["The one rule", "Smaller left ventricle = more outflow obstruction in hypertrophic cardiomyopathy. More blood through a fixed narrow valve = louder aortic stenosis."],
    ["Positions", "Left lateral decubitus: apex (S3, S4, mitral stenosis). Seated, leaning forward, exhaled: aortic regurgitation, friction rub."],
  ]},

 {"id": "l5-peripheral", "label": "Peripheral Vascular Examination", "color": "#8a5a2b",
  "rows": [
    ["Inspection", "Size, symmetry, venous pattern, hair growth, edema, skin color, ulcers. Always compare sides."],
    ["Capillary refill", "2-3 seconds. Quincke's sign: nail bed flashes red to pale with each beat."],
    ["Pulse grades", "4+ bounding, 3+ increased, 2+ brisk normal, 1+ faint, 0 absent. ALWAYS compare both sides."],
    ["Arterial insufficiency", "Claudication to rest pain; pale or dusky red; cool; NO edema; thin shiny hairless skin; painful toe ulcer; gangrene; decreased pulses; pallor on elevation, dependent rubor."],
    ["Venous insufficiency", "No pain; brown hemosiderin staining; normal temperature; pitting edema; thickened skin; ulcer at the medial and lateral malleolus; gangrene rare; NORMAL pulses."],
    ["Pulse landmarks", "Brachial: medial to biceps tendon. Radial: lateral wrist. Ulnar: medial wrist, may be impalpable. Femoral: below inguinal ligament, midway anterior superior iliac spine to pubic symphysis. Dorsalis pedis: lateral to great toe extensor tendon. Posterior tibial: behind medial malleolus."],
    ["Carotid", "Hold breath, auscultate BEFORE palpating, one side at a time."],
    ["Pulse lag", "Radial and femoral together; femoral lag = coarctation of the aorta."],
    ["Bruit sites", "Aorta (upper midline); renal 3-4 cm lateral to aorta; iliac 3-4 cm lateral to umbilicus, about 2 cm below; femoral."],
    ["Allen test", "Compress radial and ulnar, clench 30 s, open; release ULNAR and watch the hand pink up; repeat for radial. Persistent pallor = occlusion. Done before an arterial blood gas."],
    ["Ankle brachial index", "Higher ankle pressure (dorsalis pedis or posterior tibial) over brachial systolic, each leg, 2 decimals. Supine 10 min; inflate 20 mm Hg above last pulse; deflate 1 mm Hg per second."],
    ["Index values", "Over 1.40 noncompressible calcified vessel. 0.90-1.40 normal. Under 0.90 peripheral arterial disease. Under 0.50 severe."],
    ["Homans sign", "Knee bent, dorsiflex the foot quickly and forcefully; pain BEHIND THE KNEE = positive. Deep vein thrombosis."],
  ]},

 {"id": "l5-edema", "label": "Peripheral Edema", "color": "#3f5b6b",
  "rows": [
    ["Definition", "Excess fluid in the extravascular interstitial space. Up to 10% of body weight before pitting. Obscures veins, tendons, bony prominences."],
    ["Technique", "Thumb pressed firmly at least 2 seconds over the dorsum of the foot, behind the medial malleolus, or the shins. Describe depth AND extent. Unilateral or bilateral?"],
    ["1+", "2 mm, disappears rapidly."],
    ["2+", "4 mm, gone in 10-15 seconds."],
    ["3+", "6 mm, may last more than 1 minute."],
    ["4+", "8 mm, can last more than 2 minutes."],
  ]},

 {"id": "l5-exam", "label": "Running the Examination", "color": "#4a4a4a",
  "rows": [
    ["Order", "Inspection (including jugular venous pressure), palpation, auscultation, special techniques."],
    ["Equipment and room", "Stethoscope, ruler, penlight, tongue depressor. Tangential light, quiet room, warm hands, short nails."],
    ["The patient", "In a gown; never examine over clothing. Positioning: 30-45 degrees, left lateral decubitus, seated leaning forward."],
    ["Cardiac OSCE (objective structured clinical examination)", "21 October. The whole station is on the Cardiac OSCE run-sheet."],
  ]},
]

for t in topics:
    for r in t["rows"]:
        cells = list(r.values()) if isinstance(r, dict) else list(r)
        for c in cells:
            assert "**" not in c and "__" not in c, "markdown in a row: %r" % c

html = render(
    title="Cram Sheet — Physical Diagnosis 2 Exam 2",
    kicker="Physical Diagnosis 2 Exam 2 · Class of 2028",
    h1="Physical Diagnosis 2 Exam 2 Cram Sheet",
    sub="Lecture 5, the advanced cardiovascular and peripheral vascular examination: the history, the cardiac cycle and every extra sound, the apical impulse, the listening areas and which end of the stethoscope, how to describe and grade a murmur, all eleven lesions side by side, the maneuvers, and the peripheral vascular examination with edema, the Allen test, the ankle brachial index and Homans sign. Pulmonary and hematology are added when those lectures are posted.",
    topics=topics,
    guide_href="pd2-exam-2-study-guide.html",
    footer_note="Condensed from the Physical Diagnosis 2 Exam 2 Study Guide (Class of 2028). Covers Lecture 5 so far; Exam 2 (Friday 20 November) covers Lectures 5 to 7. Rows marked with a star are what the lecturer repeated, not a statement of what is on the exam. For the full explanation and the figures behind any row, see the full guide.",
)
open(OUT, "w", encoding="utf-8").write(html)
rows = sum(len([r for r in t["rows"] if not isinstance(r, dict)]) for t in topics)
print("wrote %s (%d KB, %d topics, %d rows)"
      % (os.path.relpath(OUT, ROOT), len(html) // 1024, len(topics), rows))
