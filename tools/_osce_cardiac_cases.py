# -*- coding: utf-8 -*-
"""Patient case scripts for the voice-based Cardiac OSCE practice station (2026-10-26).

Each case is the ground truth the simulated patient answers from (door card, persona, opening line, facts),
the facilitator's physical-examination findings (overrides of the maneuver catalog in
tools/_osce_cardiac_catalog.py; every maneuver not overridden returns the catalog's NORMAL finding), and the
grader's answer key.

Grounding: every clinical fact that bears on the diagnosis comes from that condition's row of the Cardiac
OSCE Disease Chart (tools/_cardiac_osce_batch_*.py, merged in tools/_pd2_cardiac_osce_data.py) or the
decks it cites (the `cites` line). Names, jobs, families and speech are invented. Review-of-systems answers
the decks do not cover are realistic negatives consistent with the case (Jaxon, 2026-10-26).

Case list (Jaxon, 2026-10-26): his class already ran stable angina, acute pericarditis, peripheral artery
disease and deep vein thrombosis, so none of those is a case diagnosis (they may appear as differentials).
Chronic heart failure is written as the preserved-ejection-fraction picture the chart row allows
(hypertension, sustained apical impulse, fourth heart sound) so it stays distinct from the dilated
cardiomyopathy case (reduced ejection fraction, displaced impulse, third heart sound, mitral regurgitation).

Schema of each case: see the build brief; the self-check at the bottom enforces it.
"""

CASES = [

# =====================================================================================================
# 1. CHRONIC HEART FAILURE (preserved ejection fraction, hypertensive)
# =====================================================================================================
dict(
  id="cardiac-chronic-heart-failure",
  condition="Chronic heart failure",
  cites=("CMS L25 Heart Failure, slides 5-10, 16, 18, 23-24, 26, 30, 32, 38-40, 56; CMS L26 Venous Disorders "
         "slide 27; PD2 Cardiovascular slides 7, 8, 20, 22-23, 42, 88-89"),
  door=dict(
    name="Lorraine Whitcomb", sex="female", age=74, dob="July 9, 1952",
    setting="Outpatient primary care clinic",
    cc="\"I get short of breath when I walk.\"",
    vitals=[("Blood pressure", "162/88 mmHg"),
            ("Heart rate", "88 beats per minute, regular"),
            ("Respiratory rate", "20 breaths per minute"),
            ("Temperature", "98.1 °F (36.7 °C)"),
            ("Oxygen saturation", "95% on room air"),
            ("Height and weight", "5 feet 4 inches, 188 pounds (body mass index 32.3)")],
  ),
  persona=("A 74-year-old retired school librarian, warm and chatty, who apologizes for 'making a fuss' and "
           "blames her age and her weight. She pauses to catch her breath in long answers and sits upright on "
           "the edge of the chair. She knows her pills well but admits she forgets them, and she is more "
           "worried than she lets on."),
  opening="I just can't walk like I used to without getting winded. It's been creeping up on me for months.",
  facts=[
    ("Full name", "Lorraine Whitcomb."),
    ("Date of birth", "July 9, 1952."),
    ("Onset", "It's crept up over about four months. I first noticed it carrying the laundry basket up the "
              "stairs. Now I get winded just walking to the mailbox."),
    ("Location", "It's not a pain, dear, it's my breathing. There's nothing to point to."),
    ("Duration", "It comes on whenever I walk any distance and settles after a few minutes sitting down. I'm "
                 "tired most of the time now, too."),
    ("Character", "Like I can't get a full breath. Like I've been running when I've only walked to the end of "
                  "the driveway."),
    ("Alleviating factors", "Sitting down and resting. At night, propping myself up on more pillows."),
    ("Aggravating factors", "Walking, the stairs, carrying anything, and lying flat."),
    ("Radiation", "No, there's no pain going anywhere."),
    ("Severity", "I'd say a six out of ten. A ten was my gallbladder attack back in 1998."),
    ("Temporal pattern", "Worse in the evening and at night when I lie down. A little worse each month than "
                         "the month before."),
    ("How far she can walk", "To the mailbox, maybe fifty yards, then I have to stop. A year ago I walked the "
                             "whole neighborhood with my friend every morning."),
    ("Prior episodes", "Nothing like this before."),
    ("Shortness of breath", "Only when I move around. Sitting here quietly I'm all right."),
    ("Orthopnea", "I'm up to three pillows now. I used to sleep on one. Some nights I end up in the recliner, "
                  "because lying flat makes me feel like I'm drowning."),
    ("Waking at night short of breath", "Yes, once or twice a week. An hour or two after I fall asleep I wake "
                                        "up gasping and have to sit on the edge of the bed, sometimes open the "
                                        "window, before it settles."),
    ("Palpitations", "No, my heart feels steady. No racing or skipping."),
    ("Fainting or near-fainting", "No, I haven't fainted or come close."),
    ("Leg swelling", "Yes, both ankles. My shoes are tight by evening and my socks leave deep marks. It's "
                     "better in the morning."),
    ("Rings and other swelling", "Now that you mention it, my rings are tight. My face isn't puffy."),
    ("Weight change", "I've put on about eight pounds in the last two months, and I'm eating less, so it "
                      "doesn't make sense to me."),
    ("Leg pain with walking", "No, my legs don't hurt when I walk. It's the breathing that stops me."),
    ("Cough", "A little dry tickle of a cough at night when I lie down. Nothing comes up."),
    ("Chest pain", "No, no chest pain at all."),
    ("Nausea, vomiting or sweating", "No vomiting and no sweats. My appetite is down a bit, and I feel full "
                                     "quickly."),
    ("Fever", "No fevers."),
    ("Constitutional", "No fevers or chills. I'm tired all the time now. And the weight gain, like I said."),
    ("Coughing up blood or wheezing", "No blood. No wheezing that I can hear."),
    ("Heartburn or belly pain", "No heartburn. No real belly pain, just that full feeling."),
    ("Neurologic", "No weakness on one side, no trouble speaking, no vision changes. My mind's still sharp."),
    ("Urination", "Normal amounts. Nothing unusual there."),
    ("Anything else", "No, I think that's everything. It's mostly the breathing and the swelling."),
    ("Chronic conditions", "High blood pressure for about twenty-five years, type 2 diabetes for about ten, "
                           "and arthritis in my knees."),
    ("Prior heart problems or stents", "No heart attacks, no stents. I had a stress test three years ago and "
                                       "they told me there were no blockages."),
    ("Surgeries and procedures", "My gallbladder out in 1998, and both cataracts done a few years ago."),
    ("Hospitalizations", "Only for the gallbladder, and having my two children."),
    ("Prescription medications", "Amlodipine 10 milligrams every morning for my blood pressure, for about "
                                 "three years. Metformin 1,000 milligrams twice a day for about ten years. "
                                 "Atorvastatin 20 milligrams at night for about five."),
    ("Taking them as prescribed", "Honestly, I forget the blood pressure pill maybe twice a week."),
    ("Over-the-counter medicines and supplements", "Naproxen, the Aleve, two tablets most days for my knees, "
                                                   "for about six months now. And a multivitamin."),
    ("Allergies", "Penicillin. I got hives as a child."),
    ("Tobacco", "I smoked a pack a day from about twenty-three until I quit at sixty-three. So forty years. "
                "I haven't touched one since."),
    ("Alcohol", "A glass of wine at Thanksgiving and Christmas. That's all."),
    ("Recreational drugs", "Goodness, no."),
    ("Salt and diet", "I don't cook much since my husband passed. A lot of canned soup, frozen dinners and "
                      "deli turkey. I do like my salt."),
    ("Exercise and activity", "I used to walk the neighborhood every morning. I've had to stop."),
    ("Occupation and exposures", "Retired school librarian. No dust or chemical exposures."),
    ("Living situation", "I live alone in a two-story house since my husband died three years ago. My "
                         "daughter lives ten minutes away and checks on me."),
    ("High blood pressure", "Yes. My home cuff usually reads in the 160s on top, more when I forget the pill."),
    ("High cholesterol", "Yes, that's why I take the atorvastatin."),
    ("Diabetes", "Type 2, for about ten years. The doctor says my sugars are 'okay, not great.'"),
    ("Family history, mother", "My mother had a weak heart. Her legs swelled up terribly at the end, and she "
                               "died at 80."),
    ("Family history, father", "My father had a stroke at 76."),
    ("Family history, siblings", "My sister is 71 and has diabetes. My brother is healthy, as far as I know."),
    ("What she thinks it is", "I figured it's my age and these extra pounds."),
    ("Concerns", "My daughter is worried my heart is giving out like my mother's did. I'm scared she might "
                 "be right."),
  ],
  questions=["Is my heart failing?",
             "Do I have to go into the hospital?",
             "Can I keep taking my Aleve for my knees?"],
  exam={
    "position": "She lies back with the head of the bed at 30 degrees and says she could not lie any flatter.",
    "general-survey": ("Alert and oriented, sitting upright, mildly short of breath after walking into the room "
                       "but speaking in full sentences. Normal color, no sweating, no distress at rest."),
    "jvp": ("Jugular venous distention at 30 degrees, with the pulsation visible about 5 centimeters above the "
            "sternal angle."),
    "precordium-palp": "A sustained lift at the apex (mitral area). No heaves or lifts over the other areas.",
    "pmi": ("The point of maximal impulse is forceful and sustained, about 3 centimeters across, at the fifth "
            "intercostal space in the left midclavicular line. It is not displaced."),
    "ausc-mitral": ("Mitral area: regular rhythm, normal first and second heart sounds, with a soft, dull extra "
                    "sound just before the first heart sound (a fourth heart sound). No murmur."),
    "left-lateral": ("Left lateral decubitus, bell at the apex: a dull, low-pitched fourth heart sound just "
                     "before the first heart sound, the 'Ten-nes-SEE' cadence. No third heart sound, no murmur."),
    "ext-inspect": ("Both lower legs are symmetrically swollen from the feet to mid-shin, with deep sock-line "
                    "marks. No brown staining, no varicose veins, no ulcers; normal hair growth."),
    "edema": ("2+ pitting edema, symmetric, over the dorsum of both feet, behind the medial malleoli and up the "
              "shins to mid-shin."),
    "bp-both-arms": "Right arm 162/88 mmHg, left arm 158/86 mmHg: within 10 mmHg between the arms, high on both.",
  },
  special=[
    ("hepatojugular-reflux", "Hepatojugular reflux",
     "presses firmly over the right upper abdomen for about 10 seconds while watching the neck veins",
     "Positive: the jugular venous pulsation rises and stays up for as long as the pressure is held."),
    ("liver-edge", "Liver edge palpation",
     "palpates upward from the right lower abdomen for the liver edge below the right costal margin",
     "The liver edge is smooth and slightly tender, palpable about 2 centimeters below the right costal "
     "margin."),
  ],
  key=dict(
    diagnosis=("Chronic heart failure, most likely with preserved ejection fraction from long-standing "
               "hypertension (New York Heart Association class III, with fluid overload but stable for outpatient "
               "care)"),
    must_not_miss=["Acute decompensated heart failure: breathlessness at rest, chest pain or fainting means "
                   "the emergency department now",
                   "Acute coronary syndrome as a hidden trigger: a troponin if there is any concern for a heart "
                   "attack"],
    ddx=[
      dict(name="Chronic heart failure (most likely preserved ejection fraction)",
           support=("Exertional breathlessness now at 50 yards, three-pillow orthopnea, waking up gasping, "
                    "bilateral pitting edema, rings tight, 8-pound weight gain, early fullness, raised neck "
                    "veins, a positive hepatojugular reflux and an enlarged liver. High blood pressure with a "
                    "sustained, nondisplaced apical impulse and a fourth heart sound points to a stiff, "
                    "hypertrophied ventricle with a preserved ejection fraction."),
           against=("Clear lungs; crackles are often absent in chronic failure even with fluid overload, and "
                    "the echocardiogram still has to set the ejection fraction group.")),
      dict(name="Chronic obstructive pulmonary disease",
           support="Forty pack-years of smoking, exertional breathlessness and a night-time cough.",
           against=("No wheeze and nothing coughed up; orthopnea, waking up gasping, raised neck veins and a "
                    "fourth heart sound point to the heart, and a high natriuretic peptide points away.")),
      dict(name="Chronic venous insufficiency",
           support="Ankle swelling that is worse by evening and better in the morning.",
           against=("Both legs equally, with breathlessness and raised neck veins; no brown staining, varicose "
                    "veins or ulcers.")),
      dict(name="Dihydropyridine calcium channel blocker edema",
           support="She takes amlodipine, which causes dependent ankle swelling.",
           against=("Amlodipine started three years before the swelling; raised neck veins, orthopnea and "
                    "breathlessness are not drug edema.")),
    ],
    studies=[
      dict(test="B-type natriuretic peptide",
           why=("Confirms heart failure as the cause of the breathlessness: above 400 makes it likely, below "
                "100 rules out acute failure."),
           expect="Elevated, about 640."),
      dict(test="Echocardiogram",
           why=("Measures the ejection fraction, which sets the treatment group: 40% or less reduced, 41 to 49% "
                "mildly reduced, 50% or more preserved."),
           expect=("Thick left ventricular walls (hypertrophy), normal chamber size, ejection fraction about "
                   "60%: preserved.")),
      dict(test="Chest X-ray",
           why="Looks for congestion (cephalization, Kerley B lines, effusion) and heart size.",
           expect="Cephalization of the upper lung vessels; no infiltrate."),
      dict(test="Electrocardiogram",
           why="Looks for ischemic changes or left ventricular hypertrophy.",
           expect=("Sinus rhythm at 88 with left ventricular hypertrophy (tall R waves in V5 and V6, deep S "
                   "waves in V1 and V2); no ischemic changes.")),
      dict(test="Metabolic panel and complete blood count",
           why=("Potassium and kidney function before and during treatment; anemia as a high-output cause of "
                "failure."),
           expect="Potassium and kidney function normal; no anemia."),
    ],
    plan=[
      ("Preserved ejection fraction: a loop diuretic (furosemide) as needed for the fluid, and a sodium-glucose "
       "cotransporter 2 inhibitor (dapagliflozin) first."),
      ("Stop amlodipine (calcium channel blockers are avoided in heart failure) and control her blood pressure "
       "with medicines that suit her other conditions: a renin-angiotensin system blocker (lisinopril or "
       "losartan), a beta blocker or spironolactone."),
      "Stop naproxen: anti-inflammatory painkillers hold salt and water.",
      ("Follow potassium and kidney function, co-manage with cardiology, and refer to cardiac "
       "rehabilitation."),
      ("Same-day review if her weight or breathlessness climbs; emergency department for breathlessness at "
       "rest, chest pain or fainting."),
    ],
    education=[
      ("Your heart muscle has grown thick and stiff from years of high blood pressure, so it cannot fill "
       "well, and fluid backs up into your lungs and legs. That is why lying flat makes you breathless and "
       "your ankles swell."),
      ("Weigh yourself every morning. Call for a gain of more than 2 to 3 pounds in a day or 5 in a week: an "
       "overnight gain is fluid, not fat."),
      ("Take every medicine every day, even when you feel well; the goals are a longer life and slower "
       "progression, not just comfort."),
      "Limit salt, stop the naproxen and other anti-inflammatory painkillers, stay off cigarettes, keep alcohol low.",
      ("Call the same day for more pillows, waking up gasping, swelling climbing your legs, less urine or new "
       "confusion; call 911 for breathlessness at rest, chest pain or fainting."),
    ],
    red_flags=["Breathlessness at rest", "Chest pain", "Fainting"],
    follow_up=("Routine: clinic follow-up with cardiology co-management to start and adjust therapy and to "
               "recheck potassium and kidney function; same-day review if her weight or breathlessness climbs."),
    presentation=(
      "Mrs. Whitcomb is a 74-year-old woman with long-standing hypertension, type 2 diabetes and a 40 "
      "pack-year former smoking history, presenting with four months of worsening exertional "
      "breathlessness, now after 50 yards. She sleeps on three pillows, up from one, wakes gasping once or "
      "twice a week, and has evening ankle swelling with an eight-pound weight gain. She takes amlodipine "
      "and daily naproxen. She denies chest pain, palpitations, fainting, wheeze and productive cough. Blood "
      "pressure is 162/88, heart rate 88, saturation 95%. Examination shows jugular venous distention, a "
      "positive hepatojugular reflux, an enlarged liver, a sustained, nondisplaced apical impulse, a fourth "
      "heart sound, clear lungs and 2+ pitting edema to mid-shin. My differential is chronic heart failure, "
      "chronic obstructive pulmonary disease, venous insufficiency and amlodipine edema. I would order a "
      "natriuretic peptide, echocardiogram, chest X-ray, electrocardiogram and metabolic panel. My working "
      "diagnosis is chronic heart failure, likely preserved ejection fraction. Plan: a diuretic and a "
      "sodium-glucose cotransporter 2 inhibitor, stop amlodipine and naproxen, daily weights, cardiology."),
    high_yield=[
      dict(item="Ask how many pillows she sleeps on, and why",
           why="Quantifies orthopnea: one pillow a year ago, three now, sometimes the recliner."),
      dict(item="Ask whether she wakes up at night gasping",
           why="Paroxysmal nocturnal dyspnea, an hour or two after lying down, is a heart failure symptom; chronic obstructive pulmonary disease does not give it."),
      dict(item="Measure the jugular venous pressure at 30 to 45 degrees, then do the hepatojugular reflux",
           why="Raised neck veins separate heart failure from venous insufficiency and drug edema."),
      dict(item="Locate and size the apical impulse; listen with the bell at the apex in left lateral decubitus",
           why="A sustained, nondisplaced impulse with a fourth heart sound means a stiff, hypertrophied ventricle (preserved ejection fraction); a displaced, diffuse one with a third heart sound means a dilated ventricle."),
      dict(item="Grade the pitting edema and say how high it climbs",
           why="Thumb for 2 seconds over the foot, behind the medial malleolus and on the shin; symmetric 2+ to mid-shin."),
      dict(item="Ask about over-the-counter medicines",
           why="Daily naproxen holds salt and water; amlodipine is also a cause of ankle swelling and is avoided in heart failure."),
      dict(item="Listen to the lung bases and say what clear lungs mean",
           why=("Clear lungs do not exclude heart failure: crackles are often absent in chronic failure even "
                "with fluid overload, and finding them would point to decompensation.")),
      dict(item="Teach daily weights with numbers",
           why="More than 2 to 3 pounds in a day or 5 in a week is fluid and needs a call."),
    ],
  ),
),

# =====================================================================================================
# 2. ATRIAL FIBRILLATION
# =====================================================================================================
dict(
  id="cardiac-atrial-fibrillation",
  condition="Atrial fibrillation",
  cites=("CMS L29 Arrhythmias I: Supraventricular, slides 24, 28, 32, 42, 46, 48-50, 56, 58; PD2 "
         "Cardiovascular slides 6, 30, 99"),
  door=dict(
    name="Marjorie Pell", sex="female", age=76, dob="January 22, 1950",
    setting="Outpatient primary care clinic, same-day visit",
    cc="\"My heart has been acting funny since last night.\"",
    vitals=[("Blood pressure", "138/86 mmHg"),
            ("Heart rate", "124 beats per minute, irregular"),
            ("Respiratory rate", "18 breaths per minute"),
            ("Temperature", "98.4 °F (36.9 °C)"),
            ("Oxygen saturation", "97% on room air"),
            ("Height and weight", "5 feet 4 inches, 182 pounds (body mass index 31.2)")],
  ),
  persona=("A 76-year-old retired bank teller, brisk and talkative, a little rattled, who keeps pressing her "
           "palm to her chest while she talks. She is precise about dates and times and jumps to the worst "
           "case because of what happened to her mother. She settles down when things are explained plainly."),
  opening="Since last night my heart's been doing something strange, and it hasn't stopped. It has me rattled.",
  facts=[
    ("Full name", "Marjorie Pell."),
    ("Date of birth", "January 22, 1950."),
    ("Onset", "Last night around nine. We'd just come home from my granddaughter's engagement dinner and I was "
              "sitting on the couch when it started, all of a sudden."),
    ("Location", "(Presses her palm flat over the left side of her chest.) In here. It's not a pain, it's the "
                 "beating."),
    ("Duration", "It hasn't stopped once since last night. So about fifteen hours now."),
    ("Character", "Racing and fluttering, all over the place. There's no steady beat to it, like a drummer "
                  "who can't keep time."),
    ("Regular or irregular", "Irregular. Completely irregular, not just fast."),
    ("Alleviating factors", "Nothing has helped. I tried lying down, deep breaths, a glass of cold water."),
    ("Aggravating factors", "Walking around makes me more winded. The stairs this morning were hard."),
    ("Radiation", "It doesn't go anywhere. There's no pain to go anywhere."),
    ("Severity", "Maybe a four out of ten. It's more frightening than painful. A ten was giving birth to my "
                 "son."),
    ("Temporal pattern", "Constant since it started. It's the same now as it was at midnight."),
    ("Prior episodes", "Once, maybe six months ago, I had a few minutes of fluttering after my morning coffee, "
                       "and it stopped by itself. I didn't tell anyone."),
    ("Chest pain", "No chest pain. Just the fluttering."),
    ("Shortness of breath", "I got winded walking up the stairs this morning, which isn't like me. Sitting "
                            "still I'm all right."),
    ("Orthopnea", "One pillow, as always. I lay flat last night trying to sleep and my breathing was fine."),
    ("Waking at night short of breath", "No. I hardly slept because of the fluttering, but not because of my "
                                        "breathing."),
    ("Palpitations", "Yes, that's the whole problem, and it's irregular."),
    ("Fainting or near-fainting", "I haven't fainted. I got a little dizzy, lightheaded, when I stood up "
                                  "quickly this morning. It passed in a few seconds."),
    ("Leg swelling", "No, my ankles look normal."),
    ("Leg pain with walking", "No."),
    ("Cough", "No cough."),
    ("Nausea, vomiting or sweating", "No."),
    ("Fever", "No fever."),
    ("Constitutional", "No fevers or chills. I'm tired today because I hardly slept. My weight's been steady."),
    ("Heat intolerance, tremor or weight loss", "No. I'm not hot all the time, no shakes, and I haven't lost "
                                                "any weight."),
    ("Coughing up blood or wheezing", "No."),
    ("Heartburn or belly pain", "No."),
    ("Neurologic", "No weakness on either side, my face feels normal, I can talk fine, no vision trouble. I "
                   "checked myself in the mirror because of my mother."),
    ("Bleeding history", "No bleeding problems, no ulcers, no blood in my stool. And I've never had a fall."),
    ("Prior stroke or mini-stroke", "No, never. Only my mother."),
    ("Recent illness, surgery or new medicines", "None. No cold medicines, no decongestants, no energy "
                                                 "drinks. I've been eating and drinking normally."),
    ("Anything else", "My husband says I snore something awful. Otherwise, no."),
    ("Chronic conditions", "High blood pressure for about twelve years. And I'm heavier than I'd like."),
    ("Surgeries and procedures", "A hysterectomy in 1992 and a right knee replacement in 2018."),
    ("Hospitalizations", "Just for those two operations."),
    ("Prior heart problems", "No heart attacks, no stents, no heart failure. No one has ever said I had a "
                             "rhythm problem."),
    ("Kidney or liver problems", "No, my kidneys and liver have always been fine on my blood work."),
    ("Prescription medications", "Losartan 50 milligrams every morning, for about eight years. That's my "
                                 "only prescription."),
    ("Over-the-counter medicines and supplements", "Calcium with vitamin D every day, and Tylenol now and then "
                                                   "for my knee. No aspirin, no blood thinners."),
    ("Allergies", "Codeine makes me throw up."),
    ("Tobacco", "Never smoked."),
    ("Alcohol", "A glass or two of wine most evenings. Last night at the engagement dinner I had three, maybe "
                "four. More than usual."),
    ("Recreational drugs", "No."),
    ("Caffeine", "Two cups of coffee in the morning."),
    ("Occupation and exposures", "Retired bank teller. I volunteer at the library two mornings a week."),
    ("Exercise and activity", "I walk with a friend twice a week, about twenty minutes."),
    ("Diet", "I cook at home most nights, but I like my salt and my desserts."),
    ("Living situation", "I live with my husband, Frank. He's 78. We have a two-story house."),
    ("Sleep and snoring", "Frank says I snore loudly and sometimes seem to stop breathing for a bit. I often "
                          "wake up tired."),
    ("High blood pressure", "Yes, on the losartan. At home it usually runs in the 130s on top."),
    ("High cholesterol", "My doctor says it's borderline. I'm not on anything for it."),
    ("Diabetes", "No, my sugar has always been normal."),
    ("Family history, mother", "My mother had an irregular heartbeat in her seventies, and she had a stroke at "
                               "82. She never walked again."),
    ("Family history, father", "My father had a heart attack at 74."),
    ("Family history, siblings", "My younger sister has high blood pressure."),
    ("What she thinks it is", "Maybe too much wine and excitement last night. But I'm afraid it's my heart."),
    ("Concerns", "I'm afraid of a stroke, after what happened to my mother. And I'm afraid it's a heart "
                 "attack."),
  ],
  questions=["Am I going to have a stroke like my mother?",
             "Do I have to go to the hospital?",
             "Will I be on a blood thinner forever?"],
  exam={
    "general-survey": ("Alert and oriented, a little anxious, comfortable at rest and speaking in full "
                       "sentences. Normal color, no sweating, breathing unlabored."),
    "carotid-palp": ("Carotid pulses are 2+ and symmetric but irregularly irregular, with the strength varying "
                     "from beat to beat. No thrill."),
    "pmi": ("The point of maximal impulse is a light tap about 2 centimeters across at the fifth intercostal "
            "space in the left midclavicular line, not displaced, and irregular."),
    "ausc-aortic": ("Aortic area: irregularly irregular rhythm at about 124 beats per minute. The first heart "
                    "sound varies in loudness from beat to beat. No murmur."),
    "ausc-pulmonic": "Pulmonic area: irregularly irregular rhythm; no murmur.",
    "ausc-erb": "Erb's point: irregularly irregular rhythm; no murmur.",
    "ausc-tricuspid": "Tricuspid area: irregularly irregular rhythm; no murmur.",
    "ausc-mitral": ("Mitral area: irregularly irregular rhythm; the first heart sound varies in loudness. No "
                    "murmur, no third or fourth heart sound."),
    "pulses": ("Peripheral pulses are present and symmetric on both sides but irregularly irregular, with the "
               "strength varying from beat to beat."),
    "bp-both-arms": "Right arm 138/86 mmHg, left arm 136/84 mmHg: within 10 mmHg between the arms.",
  },
  special=[
    ("apical-radial", "Apical and radial rates counted together",
     "counts the apical rate with the stethoscope and the radial pulse at the same time for a full 60 seconds",
     "Apical rate 124, radial rate 108 over a full minute. The rhythm has no pattern at all."),
    ("thyroid-palp", "Thyroid palpation", "palpates the thyroid from behind while the patient swallows",
     "The thyroid is not enlarged, smooth and nontender, with no nodules."),
    ("stroke-screen", "Stroke screen (face, arm drift, speech)",
     "asks the patient to smile, hold both arms out with the eyes closed, and repeat a sentence",
     "Symmetric smile, no arm drift, clear and fluent speech."),
  ],
  key=dict(
    diagnosis=("Atrial fibrillation with a rapid ventricular response, hemodynamically stable, first "
               "documented episode about 15 hours ago (one brief self-limited episode six months ago)"),
    must_not_miss=["Stroke from atrial clot: screen face, arm and speech now, and decide on anticoagulation today",
                   "Unstable atrial fibrillation (hypotension, pulmonary edema or an acute myocardial "
                   "infarction), which needs synchronized cardioversion"],
    ddx=[
      dict(name="Atrial fibrillation",
           support=("Sudden racing, fluttering heartbeat with no steady beat; an irregularly irregular pulse at "
                    "124 with a pulse deficit and a first heart sound that varies; age 76, high blood pressure, "
                    "obesity, nightly wine plus a heavy night, loud snoring with pauses, and a mother with an "
                    "irregular heartbeat."),
           against="Nothing in the history or examination; the electrocardiogram confirms it."),
      dict(name="Atrial flutter",
           support="Rapid palpitations with dizziness and breathlessness.",
           against=("Flutter with the usual 2:1 block is regular; hers is irregularly irregular with no "
                    "pattern, and the electrocardiogram would show sawtooth flutter waves.")),
      dict(name="Multifocal atrial tachycardia",
           support="Also an irregular rhythm.",
           against=("Seen in acutely ill lung or heart failure patients; she has neither, and the "
                    "electrocardiogram would show a P wave of at least three shapes before every beat.")),
      dict(name="Frequent premature atrial contractions",
           support="Her brief fluttering six months ago after coffee.",
           against=("Premature atrial contractions break a regular rhythm with early beats; her pulse has had no "
                    "steady rhythm at all for 15 hours.")),
    ],
    studies=[
      dict(test="12-lead electrocardiogram",
           why=("Confirms the rhythm and separates it from flutter, multifocal atrial tachycardia and premature "
                "atrial contractions."),
           expect="Irregularly irregular narrow-complex rhythm at about 124, no P waves and no PR interval."),
      dict(test="CHA2DS2-VASc score",
           why="Stroke risk, which decides anticoagulation; 0 in a man or 1 in a woman is low risk.",
           expect="4 (female, age 75 or older, high blood pressure): high risk, so she needs anticoagulation."),
      dict(test="HAS-BLED score",
           why="Bleeding risk on anticoagulation.",
           expect=("2 (age over 65 and her regular alcohol use): under 3, so anticoagulation goes ahead, and "
                   "cutting alcohol lowers the risk.")),
      dict(test="Thyroid-stimulating hormone and electrolytes",
           why="Looks for a driver to treat: a low thyroid-stimulating hormone means hyperthyroidism.",
           expect="Normal."),
      dict(test="Echocardiogram",
           why=("Looks for the cause, and for valve disease, which decides whether a direct oral anticoagulant "
                "(for nonvalvular atrial fibrillation) is the choice."),
           expect="Normal valves and normal pumping function: nonvalvular atrial fibrillation."),
    ],
    plan=[
      ("She is stable (normal blood pressure, no pulmonary edema, no chest pain) but has a rapid ventricular "
       "response: intravenous rate control (diltiazem or metoprolol) in the emergency department today."),
      ("Then oral rate control, a beta blocker (metoprolol) or a nondihydropyridine calcium channel blocker "
       "(diltiazem or verapamil); rate, not rhythm, is goal one."),
      ("Anticoagulate for a CHA2DS2-VASc of 4: a direct oral anticoagulant (apixaban, rivaroxaban, edoxaban or "
       "dabigatran) for nonvalvular atrial fibrillation, or warfarin to an international normalized ratio of "
       "2 to 3."),
      ("Cardiology referral; outpatient cardioversion only after 21 days of anticoagulation, and ablation is an "
       "option. Synchronized cardioversion at once if she becomes unstable."),
      "Risk factors: cut alcohol, lose weight, test for and treat sleep apnea, keep blood pressure controlled.",
    ],
    education=[
      ("Your heart has slipped into an irregular, fast rhythm called atrial fibrillation. It is not a heart "
       "attack, but it can let a clot form in the heart that causes a stroke, which is why the blood thinner "
       "matters."),
      ("Take the blood thinner every day without gaps; it is what prevents the stroke. Report black stools, "
       "blood in the urine or easy bruising."),
      "Call 911 for face drooping, arm weakness or slurred speech, chest pain, fainting or severe breathlessness.",
      "Cut back on alcohol, lose weight, get checked for sleep apnea, and keep your blood pressure controlled.",
    ],
    red_flags=["Face drooping, arm weakness or slurred speech",
               "Chest pain or fainting",
               "Severe breathlessness"],
    follow_up=("Same day: the emergency department today for intravenous rate control and the anticoagulation "
               "decision, then cardiology follow-up, with outpatient cardioversion only after 21 days of "
               "anticoagulation."),
    presentation=(
      "Mrs. Pell is a 76-year-old woman with hypertension presenting with about 15 hours of a racing, "
      "fluttering, irregular heartbeat that began suddenly last night after more wine than usual. She has "
      "breathlessness on stairs and lightheadedness on standing, and denies chest pain, fainting, "
      "orthopnea, leg swelling, thyroid symptoms and stroke symptoms. She drinks wine nightly, snores with "
      "pauses, and her mother had an irregular heartbeat and a stroke. Heart rate is 124 and irregular, "
      "blood pressure 138/86, saturation 97%. Examination shows an irregularly irregular rhythm "
      "with a varying first heart sound, a pulse deficit of 16, no murmur, normal neck veins, clear lungs, no "
      "edema, a normal thyroid and a normal stroke screen. My differential is atrial fibrillation, atrial "
      "flutter, multifocal atrial tachycardia and premature atrial contractions. I would order an "
      "electrocardiogram, thyroid-stimulating hormone, electrolytes and an echocardiogram; CHA2DS2-VASc is 4. "
      "My working diagnosis is stable atrial fibrillation with a rapid ventricular response. Plan: "
      "intravenous rate control in the emergency department, a direct oral anticoagulant, and cardiology."),
    high_yield=[
      dict(item="Count the apical and radial rates together for a full 60 seconds",
           why="A short count misleads in an irregular rhythm; the apical rate exceeds the radial (pulse deficit)."),
      dict(item="Ask whether the palpitations are regular or irregular, and exactly when they started",
           why="Irregularly irregular separates fibrillation from flutter and early beats; the onset frames the cardioversion decision."),
      dict(item="Ask about stroke symptoms and do a stroke screen",
           why="Stroke from atrial clot is the danger; face, arm drift and speech take seconds."),
      dict(item="Look for instability: blood pressure, jugular veins, lung bases, ankles, chest pain",
           why="Hypotension, pulmonary edema or an infarction means synchronized cardioversion, not rate control."),
      dict(item="Ask the risk factors on the list",
           why="Alcohol, snoring with pauses (sleep apnea), high blood pressure, obesity, diabetes and a family history of atrial fibrillation."),
      dict(item="Palpate the thyroid and ask about heat intolerance and weight loss",
           why="Hyperthyroidism is a driver to treat; the thyroid-stimulating hormone confirms it."),
      dict(item="Say the CHA2DS2-VASc and HAS-BLED scores out loud",
           why="Stroke risk decides anticoagulation; bleeding risk is weighed against it."),
      dict(item="Name the management branch",
           why="Stable with a rapid ventricular response means intravenous rate control in the emergency department."),
    ],
  ),
),

# =====================================================================================================
# 3. AORTIC STENOSIS
# =====================================================================================================
dict(
  id="cardiac-aortic-stenosis",
  condition="Aortic stenosis",
  cites=("CMS L23 Valvular Heart Disease, slides 11-13, 16-22, 48; CMS L28 Cardiomyopathy slides 68-72; PD2 "
         "Cardiovascular slides 23, 42, 50, 59-62, 67, 70"),
  door=dict(
    name="Walter Ostrowski", sex="male", age=79, dob="May 30, 1947",
    setting="Outpatient primary care clinic",
    cc="\"I almost passed out on the stairs last week.\"",
    vitals=[("Blood pressure", "126/84 mmHg"),
            ("Heart rate", "72 beats per minute, regular"),
            ("Respiratory rate", "16 breaths per minute"),
            ("Temperature", "97.9 °F (36.6 °C)"),
            ("Oxygen saturation", "97% on room air"),
            ("Height and weight", "5 feet 9 inches, 176 pounds (body mass index 26.0)")],
  ),
  persona=("A 79-year-old retired machinist, polite, slow-spoken and stoic, who hates a fuss. He answers only "
           "what he is asked and needs a direct question before he admits the chest tightness he has been "
           "ignoring. His wife made the appointment and he keeps saying it was probably nothing."),
  opening="Last week I was climbing the stairs at my daughter's and everything went gray. I had to sit down.",
  facts=[
    ("Full name", "Walter Ostrowski."),
    ("Date of birth", "May 30, 1947."),
    ("Onset of the near-fainting", "A week ago Sunday, climbing the stairs at my daughter's house with a bag "
                                   "of groceries. About two-thirds of the way up, everything went gray and my "
                                   "legs went weak."),
    ("What happened during the episode", "I grabbed the rail and sat down on the step. I didn't black out "
                                         "completely. In about a minute it cleared, and I was myself again, "
                                         "no confusion."),
    ("Warning before it", "No racing heart, no flutter, no warning like that. I was just working hard on the "
                          "stairs."),
    ("Has it happened before", "Not the graying out. That was the first time."),
    ("Chest tightness", "Since you ask, yes. For about two months I get a tightness in my chest when I walk "
                        "more than a block or two, or do stairs."),
    ("Location", "(Rubs the middle of his chest with an open hand.) Across the middle here."),
    ("Duration", "A few minutes. It goes once I stop and rest."),
    ("Character", "Tight, like a band across my chest. Not sharp."),
    ("Alleviating factors", "Stopping to rest. Sitting down."),
    ("Aggravating factors", "Walking any distance, stairs, carrying things, working in the garden."),
    ("Position and breathing", "No, lying down or taking a deep breath doesn't change it."),
    ("Radiation", "It stays in the chest."),
    ("Severity", "A four out of ten, maybe. A ten was crushing my thumb in a lathe back in 1982."),
    ("Temporal pattern", "Only when I exert myself. Never sitting still, never at night. About the same over "
                         "these two months."),
    ("Shortness of breath", "Yes, I get out of breath walking any distance now, along with the tightness. "
                            "Sitting here I'm fine."),
    ("Orthopnea", "One pillow. I can lie flat fine."),
    ("Waking at night short of breath", "No."),
    ("Palpitations", "No, my heart doesn't race or skip."),
    ("Leg swelling", "No."),
    ("Leg pain with walking", "No, my legs are fine. It's the chest and the wind that stop me."),
    ("Cough", "No."),
    ("Nausea, vomiting or sweating", "No."),
    ("Fever", "No."),
    ("Constitutional", "No fevers. I tire out more than I used to. My weight's steady."),
    ("Coughing up blood or wheezing", "No."),
    ("Heartburn or belly pain", "No heartburn. My stomach's fine."),
    ("Neurologic", "No weakness on one side, no trouble talking, no vision changes. When I grayed out it was "
                   "everything at once, not one side."),
    ("Anything else", "No, that's about it."),
    ("Heart murmur", "Now that you mention it, a doctor told me about five years ago that I had a murmur. He "
                     "said to keep an eye on it. Nobody ever did anything about it."),
    ("Chronic conditions", "High blood pressure and high cholesterol, both for about fifteen years. A bit of "
                           "arthritis in my hands."),
    ("Surgeries and procedures", "A hernia repair in 1995 and a prostate procedure in 2016. Never had a heart "
                                 "test that I know of, other than the heart tracing at physicals."),
    ("Hospitalizations", "One night after the prostate procedure. That's all."),
    ("Prior heart problems or stents", "No heart attacks, no stents."),
    ("Rheumatic fever, childhood heart problem or kidney disease", "No, none that I know of."),
    ("Prescription medications", "Lisinopril 20 milligrams in the morning and atorvastatin 40 milligrams at "
                                 "night. Both for years."),
    ("Over-the-counter medicines and supplements", "A baby aspirin some days, fish oil, and Tylenol for my "
                                                   "hands."),
    ("Allergies", "None that I know of."),
    ("Tobacco", "About a pack a day from eighteen until I was fifty, so about thirty years. I quit in 1997."),
    ("Alcohol", "A beer or two on bowling night."),
    ("Recreational drugs", "No."),
    ("Fluids", "I don't drink much water. Coffee in the morning, and the beer on bowling night."),
    ("Occupation and exposures", "Retired machinist. Forty years in a machine shop, around cutting oils and "
                                 "metal dust, but my lungs have always been fine."),
    ("Exercise and activity", "Gardening, and bowling on Thursdays. I've sat out bowling the last month "
                              "because I get winded carrying the ball bag."),
    ("Diet", "My wife cooks. Meat and potatoes, mostly."),
    ("Living situation", "I live with my wife, Irene, in a one-story house. Our daughter lives across town; "
                         "that's the house with the stairs."),
    ("High blood pressure", "Yes, on the lisinopril. They say it's under control."),
    ("High cholesterol", "Yes, on the atorvastatin."),
    ("Diabetes", "No."),
    ("Family history, father", "My father died of a stroke at 77."),
    ("Family history, mother", "My mother lived to 90. She had arthritis."),
    ("Family history, siblings", "My brother had bypass surgery at 72. My sister is fine."),
    ("Family history, sudden death", "Nobody in the family died suddenly young. No one with a heart muscle "
                                     "problem that I know of."),
    ("What he thinks it is", "I figured I went up the stairs too fast. Old age."),
    ("Concerns", "Irene's worried it'll happen when I'm driving. I suppose I'd like to know what's going on."),
  ],
  questions=["Is it my heart?",
             "Is there a pill for this, or do I need an operation?",
             "Can I keep bowling and working in the garden?"],
  exam={
    "carotid-inspect": "Carotid pulsations are small and slow to rise on both sides.",
    "carotid-ausc": ("A harsh systolic sound over both carotids, loudest low in the neck, that can be followed "
                     "continuously down to the right second intercostal space."),
    "carotid-palp": "Carotid upstrokes are weak and delayed on both sides: slow to rise and low in volume. No thrill.",
    "precordium-palp": "A forceful, sustained lift at the apex (mitral area). No heaves or lifts over the other areas.",
    "pmi": ("The point of maximal impulse is forceful and sustained, a little over 2 centimeters across, at the "
            "fifth intercostal space in the left midclavicular line. It is not displaced."),
    "thrills": ("A thrill is felt with the ball of the hand over the aortic area, second intercostal space at "
                "the right sternal border. No thrills elsewhere."),
    "ausc-aortic": ("Aortic area: a harsh, medium-pitched, midsystolic crescendo-decrescendo murmur, grade 4 out "
                    "of 6, loudest here and radiating to both carotids. Regular rhythm at about 72. No diastolic "
                    "murmur."),
    "ausc-pulmonic": "Pulmonic area: the same systolic murmur, softer, carried over from the aortic area.",
    "ausc-erb": "Erb's point: the systolic murmur is heard more softly down the left sternal border.",
    "ausc-tricuspid": "Tricuspid area: the systolic murmur is faint here.",
    "ausc-mitral": ("Mitral area: the systolic murmur is faint at the apex. A soft fourth heart sound just "
                    "before the first heart sound."),
    "left-lateral": ("Left lateral decubitus, bell at the apex: a dull, low-pitched fourth heart sound just "
                     "before the first heart sound. No third heart sound; the systolic murmur is faint here."),
    "lean-forward": ("Sitting up and leaning forward at end-expiration: the harsh systolic murmur is louder at "
                     "the right upper sternal border. No diastolic murmur and no rub."),
    "dynamic": ("Squatting from standing, or a passive leg raise: the murmur gets louder. Valsalva or standing "
                "quickly: it gets softer. Isometric handgrip: softer."),
    "bp-both-arms": "Right arm 126/84 mmHg, left arm 124/84 mmHg: within 10 mmHg between the arms.",
  },
  special=[
    ("apex-carotid", "Apex and carotid palpated together",
     "places one hand on the apical impulse and the other on the right carotid at the same time",
     "A forceful, sustained apical impulse, while the carotid upstroke under the other hand is weak and arrives "
     "late."),
    ("murmur-timing", "Carotid palpation while listening (timing)",
     "keeps a finger on the carotid while listening at the aortic area",
     "The murmur coincides with the carotid upstroke: it is systolic."),
  ],
  key=dict(
    diagnosis="Symptomatic aortic stenosis, likely severe and degenerative (calcific) in a man over 70",
    must_not_miss=["Coronary artery disease causing the exertional chest tightness: the two often coexist, so "
                   "the murmur does not end the angina workup",
                   "Hypertrophic obstructive cardiomyopathy: exertional near-fainting with a systolic murmur"],
    ddx=[
      dict(name="Aortic stenosis",
           support=("Exertional chest tightness, breathlessness and near-fainting on the stairs in a 79-year-old "
                    "man with a murmur known for five years; a harsh grade 4 out of 6 midsystolic "
                    "crescendo-decrescendo murmur at the right second intercostal space with a thrill, radiating "
                    "to both carotids, louder with squatting and leaning forward, softer with Valsalva and "
                    "handgrip; a forceful, sustained apex with a weak, delayed carotid; a fourth heart sound."),
           against="Nothing; the echocardiogram grades the severity."),
      dict(name="Hypertrophic obstructive cardiomyopathy",
           support="Exertional near-fainting with a systolic murmur.",
           against=("Age 79 with no family history of sudden death; the murmur is loudest at the right second "
                    "intercostal space and carries into the carotids, not at Erb's point; it gets softer, not "
                    "louder, with Valsalva and standing.")),
      dict(name="Mitral regurgitation",
           support="A systolic murmur with exertional breathlessness.",
           against=("Midsystolic and loudest at the base, carrying into the neck, not holosystolic at the apex "
                    "into the axilla; softer, not louder, with handgrip.")),
      dict(name="Stable angina from coronary artery disease",
           support=("Exertional chest tightness relieved by rest in an older former smoker with high blood "
                    "pressure and high cholesterol."),
           against=("The ejection murmur, the carotid findings and the near-fainting point to the valve, but the "
                    "two often coexist.")),
    ],
    studies=[
      dict(test="Transthoracic echocardiogram",
           why=("Confirms and grades the stenosis, and excludes hypertrophic cardiomyopathy and mitral "
                "regurgitation; anyone with symptoms suggestive of aortic stenosis gets one."),
           expect=("Thickened, calcified aortic leaflets with reduced systolic opening and left ventricular "
                   "hypertrophy; valve area 0.8 square centimeters, mean gradient 48 mmHg, jet velocity 4.3 "
                   "meters per second: severe (the '4, 40 and 1' rule). Normal septum, no regurgitant mitral "
                   "jet.")),
      dict(test="Electrocardiogram",
           why="Left ventricular hypertrophy in severe disease (low sensitivity).",
           expect="Sinus rhythm at 72 with left ventricular hypertrophy."),
      dict(test="Left heart catheterization",
           why="The definitive finding.",
           expect="Confirms a severe gradient across the aortic valve."),
    ],
    plan=[
      "Urgent cardiology valve referral: every patient with aortic stenosis on echocardiogram goes to cardiology.",
      ("Severe and symptomatic: aortic valve replacement, by transcatheter aortic valve replacement or with a "
       "mechanical valve (lifelong anticoagulation) or a biological valve."),
      ("No medicine fixes the valve, and he is preload dependent: avoid dehydration, strenuous activity and "
       "competitive sports."),
      ("Avoid nitrates for the chest tightness, and keep beta blockers and calcium channel blockers out of his "
       "blood pressure regimen."),
    ],
    education=[
      ("The valve out of your heart has narrowed, so your heart has to work harder to push blood through it. "
       "When it cannot keep up during effort, you get the chest tightness, the breathlessness and the graying "
       "out."),
      ("Now that it causes symptoms, the plan is to replace the valve, so the heart specialist needs to see you "
       "soon."),
      ("Drink enough fluids, avoid heavy exertion, and do not take nitroglycerin unless the heart specialist "
       "prescribes it."),
      "Report chest pain, fainting or breathlessness on exertion right away; they change the plan.",
      "Keep the echocardiogram and the cardiology appointments.",
    ],
    red_flags=["Fainting, or graying out again",
               "Chest pain that does not settle with rest",
               "Breathlessness at rest or lying flat, or waking up gasping"],
    follow_up="Urgent: echocardiogram and cardiology valve referral within days, because he has symptoms.",
    presentation=(
      "Mr. Ostrowski is a 79-year-old man with hypertension, high cholesterol, former smoking and a murmur "
      "noted five years ago, presenting after nearly fainting on the stairs last week. He "
      "also has two months of exertional chest tightness and breathlessness after a block or two, relieved by "
      "rest. He denies palpitations, rest pain, orthopnea, leg swelling and family sudden death. Vital signs "
      "are normal. He has a harsh grade 4 out of 6 midsystolic crescendo-decrescendo murmur at the right "
      "second intercostal space with a thrill, radiating to both carotids, louder with squatting and leaning "
      "forward, softer with Valsalva and handgrip; a forceful, sustained apical impulse with weak, delayed "
      "carotid upstrokes; a fourth heart sound; and clear lungs. My differential is aortic stenosis, "
      "hypertrophic obstructive cardiomyopathy, mitral regurgitation and coronary artery disease. I would "
      "order an echocardiogram and electrocardiogram, then left heart catheterization. My working diagnosis "
      "is symptomatic, likely severe aortic stenosis. Plan: urgent cardiology for valve replacement, no "
      "nitrates, and no dehydration or strenuous exertion."),
    high_yield=[
      dict(item="Ask directly about exertional chest pain, near-fainting and breathlessness",
           why="The three cardinal symptoms; once any appears, 3-year mortality is 75% without valve replacement."),
      dict(item="Describe the murmur completely: timing, location, radiation, grade, quality",
           why="Timing first (palpate the carotid while listening); harsh, midsystolic, right second intercostal space, into both carotids."),
      dict(item="Feel for a thrill over the aortic area",
           why="A thrill means grade 4 out of 6 or more."),
      dict(item="Trace the sound from the aortic area into both carotids before calling it a bruit",
           why="The aortic stenosis murmur radiates to the carotids."),
      dict(item="Palpate the apex and the carotid together",
           why="A forceful, sustained apex with a weak, delayed carotid upstroke signals severe stenosis."),
      dict(item="Do the dynamic maneuvers and say what they mean",
           why="Squatting or a leg raise makes it louder, Valsalva or standing softer: the opposite of hypertrophic cardiomyopathy."),
      dict(item="Ask about a murmur found in the past",
           why="A known murmur that was never worked up is the history clue here."),
      dict(item="State the plan cautions",
           why="No nitrates, avoid dehydration and strenuous exertion, urgent echocardiogram and cardiology."),
    ],
  ),
),

# =====================================================================================================
# 4. CHRONIC VENOUS INSUFFICIENCY AND VARICOSE VEINS
# =====================================================================================================
dict(
  id="cardiac-chronic-venous-insufficiency-and-varicose-veins",
  condition="Chronic venous insufficiency and varicose veins",
  cites=("CMS L26 Venous Disorders, slides 5-15, 27-44 (deep vein thrombosis slides 46-72); CMS L27 Arterial "
         "Occlusive Disease slides 15, 19; PD2 Cardiovascular slides 85-95"),
  door=dict(
    name="Teresa Vandermolen", sex="female", age=61, dob="August 17, 1965",
    setting="Outpatient primary care clinic",
    cc="\"My legs ache by the end of the day.\"",
    vitals=[("Blood pressure", "128/78 mmHg"),
            ("Heart rate", "74 beats per minute, regular"),
            ("Respiratory rate", "14 breaths per minute"),
            ("Temperature", "98.2 °F (36.8 °C)"),
            ("Oxygen saturation", "98% on room air"),
            ("Height and weight", "5 feet 5 inches, 182 pounds (body mass index 30.3)")],
  ),
  persona=("A 61-year-old hairstylist who still works full days on her feet, upbeat, practical and a bit "
           "embarrassed about how her legs look. She talks with her hands and jokes about 'my mother's legs.' "
           "She has put off coming in for years and is here mostly because of the sore that will not heal."),
  opening="My legs get heavy and achy by evening, and my ankles puff up. It's been years, but it's worse now.",
  facts=[
    ("Full name", "Teresa Vandermolen."),
    ("Date of birth", "August 17, 1965."),
    ("Onset", "The aching has been going on for years, at least ten. The last year or so it's gotten worse, "
              "and the left one has started to change color."),
    ("Location", "(Runs her hands down both lower legs.) Both calves and ankles, the left worse than the "
                 "right."),
    ("Duration", "Every workday. It builds through the day and it's at its worst by evening."),
    ("Character", "Heavy and achy, like my legs are full of sand. Sometimes a throbbing."),
    ("Alleviating factors", "Putting my feet up on the couch at night helps a lot, and so does walking around. "
                            "By morning they feel better."),
    ("Aggravating factors", "Standing at the chair all day, and sitting a long time with my feet down, like "
                            "on a long drive."),
    ("Radiation", "No, it stays in the lower legs."),
    ("Severity", "Maybe a five out of ten by the end of the day. A ten was the blood clot in my leg years ago."),
    ("Temporal pattern", "Worse as the day goes on and in hot weather; better in the morning."),
    ("Ankle swelling", "Yes, both ankles swell by evening, the left more. It's mostly down by morning."),
    ("Skin changes and itching", "The skin around my left inner ankle has gone brown over the last year, and "
                                 "it itches like crazy. I try not to scratch."),
    ("The sore", "About five weeks ago a sore opened up just above my left inner ankle. It's a little sore, "
                 "it stings when my sock rubs, and it weeps a bit of clear fluid. It isn't getting better."),
    ("Visible veins", "I've had bulging, ropey veins on both legs since my last pregnancy. My mother had the "
                      "same."),
    ("Prior episodes", "Not the sore. That's new."),
    ("Sudden swelling of one leg", "No. Nothing sudden. It's been the same slow pattern for years."),
    ("Calf pain, redness or warmth", "No new calf pain, and the leg isn't hot or red."),
    ("Leg pain with walking", "No, walking actually makes my legs feel better."),
    ("Shortness of breath", "No, my breathing is fine."),
    ("Orthopnea", "One pillow. I lie flat fine."),
    ("Waking at night short of breath", "No."),
    ("Palpitations", "No."),
    ("Fainting or near-fainting", "No."),
    ("Cough", "No."),
    ("Chest pain", "No."),
    ("Nausea, vomiting or sweating", "No."),
    ("Fever", "No fevers or chills."),
    ("Constitutional", "No fevers, no weight change. Tired at the end of a long day, like anyone."),
    ("Coughing up blood or wheezing", "No."),
    ("Heartburn or belly pain", "No."),
    ("Urine and kidneys", "Nothing unusual with my urine. No one has ever said I have a kidney or liver "
                          "problem."),
    ("Neurologic", "No numbness or weakness. My feet feel normal."),
    ("Anything else", "No, it's just the legs. And the sore."),
    ("Chronic conditions", "High blood pressure for about six years, and I'm heavier than I'd like."),
    ("Prior blood clot", "Yes, a blood clot in my left leg when I was 48, after my hysterectomy. I was on a "
                         "blood thinner for three months."),
    ("Clot risk", "No cancer, no long trips or time off my feet lately, and no clotting problems in the "
                  "family."),
    ("Past treatment", "I've never worn compression stockings. No leg ulcers or skin infections before "
                       "this."),
    ("Surgeries and procedures", "The hysterectomy in 2013 for fibroids. No vein procedures."),
    ("Hospitalizations", "The hysterectomy, and the blood clot afterward. And three deliveries."),
    ("Pregnancies", "Three children, all normal deliveries."),
    ("Prior heart problems", "No heart problems at all."),
    ("Prescription medications", "Lisinopril 10 milligrams in the morning for about six years. No blood "
                                 "thinners now."),
    ("Hormones", "No hormone pills or creams."),
    ("Over-the-counter medicines and supplements", "Tylenol now and then for my back, and a multivitamin."),
    ("Allergies", "Penicillin gives me hives."),
    ("Tobacco", "I smoked in my twenties, maybe half a pack a day, and quit at thirty."),
    ("Alcohol", "A glass of wine on the weekend."),
    ("Recreational drugs", "No."),
    ("Occupation and exposures", "I've been a hairstylist for thirty-five years. On my feet at the chair all "
                                 "day, nine or ten hours."),
    ("Exercise and activity", "Not much besides work. I'm too tired after."),
    ("Diet", "Pretty normal. Too much takeout."),
    ("Living situation", "I live with my husband, Ray. Our kids are grown."),
    ("High blood pressure", "Yes, on the lisinopril. It runs fine."),
    ("High cholesterol", "No, it's been normal."),
    ("Diabetes", "No."),
    ("Family history, mother", "My mother had terrible varicose veins and sores on her legs that took forever "
                               "to heal. She lived to 84."),
    ("Family history, father", "My father had high blood pressure and died of a heart attack at 79."),
    ("Family history, siblings", "My sister has varicose veins too."),
    ("What she thinks it is", "My mother's legs. I always knew they'd catch up with me."),
    ("Concerns", "I'm worried the sore won't heal, and that it's another blood clot."),
  ],
  questions=["Is this another blood clot?",
             "Will the sore ever heal?",
             "Do I really have to wear those tight stockings every day?"],
  exam={
    "ext-inspect": ("Brown discoloration around both ankles, worse on the left, starting at the inner ankle "
                    "bone, with dry, scaly, red skin and shiny, taut skin. A shallow 2-centimeter ulcer just "
                    "above the left inner ankle bone with irregular borders, a clean yellowish base and a "
                    "little clear drainage; no surrounding redness. Normal hair growth."),
    "edema": ("2+ pitting edema over the left ankle and lower shin, 1+ over the right ankle, stopping well "
              "below the knees."),
    "bp-both-arms": "Right arm 128/78 mmHg, left arm 126/78 mmHg: within 10 mmHg between the arms.",
  },
  special=[
    ("standing-inspection", "Inspection of both legs standing",
     "has the patient stand and inspects both legs from the groin to the feet, front and back",
     "Standing: dilated, tortuous superficial veins along the inner thigh and calf of both legs, more on the left, "
     "visible and palpable and mildly tender. The swelling and the color change look more obvious."),
    ("leg-temperature-calves", "Skin temperature and deep-vein palpation",
     "feels both legs with the back of the hand, then palpates along the deep veins of each calf",
     "Both legs are the same normal temperature, with no heat. No tenderness along the deep veins; the calves "
     "are soft."),
    ("calf-circumference", "Calf circumference",
     "measures both calves 10 centimeters below the tibial tuberosity",
     "Left 39 centimeters, right 38 centimeters."),
  ],
  key=dict(
    diagnosis=("Chronic venous insufficiency (secondary, after her left leg deep vein thrombosis) with varicose "
               "veins, stasis dermatitis and a venous ulcer above the left medial malleolus"),
    must_not_miss=["Deep vein thrombosis: new one-sided swelling with calf pain and warmth; the venous duplex "
                   "ultrasound settles it",
                   "Peripheral artery disease: an arterial ulcer, weak pulses or a low ankle-brachial index means "
                   "no compression"],
    ddx=[
      dict(name="Chronic venous insufficiency and varicose veins",
           support=("Years of heavy, aching legs worse with standing and better with elevation and walking; "
                    "evening ankle swelling; itching and brown staining starting at the left medial malleolus; "
                    "a weeping ulcer above it; varicose veins on standing. Risk factors: prior left leg clot, "
                    "female, age, three pregnancies, obesity, decades of standing at work, and a mother and "
                    "sister with varicose veins."),
           against="Nothing; the duplex scan confirms reflux and excludes a clot."),
      dict(name="Peripheral artery disease",
           support="A leg ulcer in a woman over 60 with high blood pressure and a smoking history.",
           against=("No pain with walking (walking helps); warm legs with normal hair, normal pulses and "
                    "capillary refill; the ulcer sits above the medial malleolus with a clean base, not on the "
                    "toes or lateral ankle; edema is present.")),
      dict(name="Deep vein thrombosis",
           support="A prior left leg clot, and the left leg is more swollen.",
           against=("Years of slow symptoms rather than acute swelling over days; no new calf pain, heat or "
                    "deep-vein tenderness; calves differ by only 1 centimeter.")),
      dict(name="Heart failure, kidney or liver disease",
           support="Swelling in both ankles.",
           against=("Asymmetric, with varicose veins, staining and an ulcer; normal neck veins, clear lungs, no "
                    "breathlessness or orthopnea, and no kidney or liver history; she takes no calcium channel "
                    "blocker or anti-inflammatory painkiller.")),
    ],
    studies=[
      dict(test="Venous duplex ultrasound",
           why=("The first test: confirms the diagnosis, checks patency (is there a clot?) and valve competence "
                "(is there reflux?), and maps the reflux."),
           expect=("Valvular reflux in the great saphenous vein on both sides and scarred, incompetent deep "
                   "valves in the left leg from the old clot; the deep veins are patent and compressible, with "
                   "no thrombus.")),
      dict(test="Ankle-brachial index",
           why="Rules out arterial disease before compression, and is done for any lower leg wound.",
           expect="1.05 on both sides: normal, so compression is safe."),
      dict(test="Catheter venography",
           why="The gold standard, but kept for planning an intervention.",
           expect="Not needed now."),
    ],
    plan=[
      ("Nonoperative first: elevate the legs above heart level, daily walking and ankle flexion, avoid long "
       "spells of sitting or standing, gentle cleansing and emollients."),
      ("Graduated compression stockings now that arterial disease is excluded; the ulcer needs compression plus "
       "a wound-care referral (healing can take 4 to 6 months)."),
      ("Stasis dermatitis: barrier cream, then a mid-potency topical corticosteroid (triamcinolone) for the "
       "itch and inflammation; an antibiotic for cellulitis only if it develops: clindamycin (the "
       "course material also lists cephalexin, used with caution given her penicillin hives)."),
      ("Varicose veins: weeks to months of stockings first, then sclerotherapy, laser or radiofrequency ablation, "
       "or stripping."),
      ("Vascular referral for a nonhealing or recurrent ulcer, persistent dermatitis or significant saphenous "
       "reflux."),
    ],
    education=[
      ("The valves in your leg veins leak, partly from the old clot, so blood pools in your lower legs. That "
       "pressure causes the swelling, the brown staining, the itch and the sore."),
      "Wear the stockings every day; the swelling and the sores come back when they are not worn.",
      ("Put your feet up above the level of your heart, walk every day, avoid long spells of sitting or "
       "standing, moisturize, and do not scratch."),
      "Come back for a new sore, a hot, red, painful leg, or sudden swelling of one calf.",
    ],
    red_flags=["Sudden swelling of one calf, with pain or warmth",
               "A hot, red, painful leg or a fever",
               "Sudden breathlessness or chest pain"],
    follow_up=("Routine: primary care follow-up to check the ulcer and stocking use, with wound care, and "
               "vascular referral if the ulcer does not heal or recurs; sudden one-sided swelling is a deep vein "
               "thrombosis until proven otherwise."),
    presentation=(
      "Mrs. Vandermolen is a 61-year-old hairstylist with a left leg deep vein thrombosis at 48, three "
      "pregnancies and obesity, presenting with years of heavy, aching legs by evening, worse standing, "
      "better with elevation and walking. Her left inner ankle has itched and browned over a year, with a "
      "sore above it unhealed for five weeks. Her mother had varicose veins. She denies sudden one-sided "
      "swelling, calf pain, warmth, fever, claudication and breathlessness. Vital signs are normal. She has "
      "varicose veins on standing, worse on the left, hemosiderin staining, stasis dermatitis, a shallow "
      "fibrinous ulcer above the left medial malleolus and pitting edema, 2+ left, 1+ right. Temperature, "
      "pulses and neck veins are normal; calves differ by 1 centimeter. "
      "My differential is chronic venous insufficiency, deep vein thrombosis, peripheral artery disease and "
      "heart, kidney or liver edema. I would order a venous duplex ultrasound and an ankle-brachial index. My "
      "working diagnosis is chronic venous insufficiency with a venous ulcer. Plan: elevation, walking, skin "
      "care, compression, wound care."),
    high_yield=[
      dict(item="Inspect both legs with the patient standing",
           why="Varicose veins are seen and felt in the dependent position; compare the two sides."),
      dict(item="Ask what makes the aching better and worse",
           why="Worse standing, better with elevation and walking is venous; pain with walking that rest relieves would be arterial."),
      dict(item="Ask about a prior blood clot, pregnancies, family history and work on her feet",
           why="Prior deep vein thrombosis is a leading cause; family history is the most common predisposing factor for varicose veins."),
      dict(item="Separate a new clot from the chronic picture",
           why="Ask about sudden one-sided swelling, calf pain and warmth; feel the temperature, palpate the deep veins, measure both calves."),
      dict(item="Palpate the pulses and check capillary refill, and say why",
           why="Arterial disease must be excluded before compression; an ankle-brachial index is done for any leg wound."),
      dict(item="Grade the pitting edema and describe the ulcer",
           why="Location above the medial malleolus with a clean fibrinous base is venous; toes or the lateral ankle with weak pulses is arterial."),
      dict(item="Look for a heart cause of the edema",
           why="Normal neck veins and clear lungs argue against heart failure as the cause."),
      dict(item="Teach daily stockings and elevation above heart level",
           why="The swelling and ulcers come back when the stockings are not worn."),
    ],
  ),
),

# =====================================================================================================
# 5. VASOVAGAL SYNCOPE
# =====================================================================================================
dict(
  id="cardiac-vasovagal-syncope",
  condition="Vasovagal syncope",
  cites=("CMS L21 Hypotension, slides 8-9, 13-17, 23, 27; CMS L23 Valvular Heart Disease slides 16-17; PD2 "
         "Cardiovascular slides 9, 60-62, 70"),
  door=dict(
    name="Madison Hartwell", sex="female", age=22, dob="April 2, 2004",
    setting="Outpatient primary care clinic",
    cc="\"I fainted over the weekend.\"",
    vitals=[("Blood pressure", "108/68 mmHg"),
            ("Heart rate", "66 beats per minute, regular"),
            ("Respiratory rate", "14 breaths per minute"),
            ("Temperature", "98.4 °F (36.9 °C)"),
            ("Oxygen saturation", "99% on room air"),
            ("Height and weight", "5 feet 6 inches, 128 pounds (body mass index 20.7)")],
  ),
  persona=("A 22-year-old college senior studying elementary education, friendly, a little embarrassed and "
           "slightly anxious, who talks quickly and laughs at herself. She feels completely fine now and is "
           "only here because her mother insisted. She is in another wedding next month and wants to know "
           "how to keep it from happening again."),
  opening="I passed out at my cousin's wedding on Saturday. I feel totally fine now, but my mom made me come in.",
  facts=[
    ("Full name", "Madison Hartwell."),
    ("Date of birth", "April 2, 2004."),
    ("Onset", "Saturday afternoon, at my cousin's outdoor wedding. I was a bridesmaid, standing up front for "
              "the whole ceremony, about forty minutes, in the sun. It was really hot."),
    ("What she felt first", "I got really hot all of a sudden, then sick to my stomach and sweaty, and my "
                            "vision went gray around the edges, like a tunnel."),
    ("What happened next", "The next thing I knew I was on the grass with people around me. My sister said I "
                           "was out for a few seconds."),
    ("Recovery", "I felt fine within a minute or two. A little tired and embarrassed, but I knew where I was "
                 "and remembered everything right away."),
    ("What a witness saw", "My sister says I just went limp and slid down. She caught my arm. No shaking or "
                           "jerking, and I didn't wet myself."),
    ("Tongue biting or injury", "No, I didn't bite my tongue. I scraped my elbow a little. I didn't hit my "
                                "head."),
    ("Location", "There wasn't any pain. It was more a whole-body feeling, hot and woozy."),
    ("Duration", "The warning feeling was maybe half a minute, then I was out for a few seconds."),
    ("Character", "Hot, queasy, clammy, like I was going to throw up, and then everything faded out."),
    ("Alleviating factors", "Lying on the grass. Once I was down, it passed fast. They gave me water and I "
                            "sat in the shade."),
    ("Aggravating factors", "Standing still for so long in the heat. I'd been on my feet all morning getting "
                            "ready, too."),
    ("Radiation", "No pain anywhere."),
    ("Severity", "Not painful at all. The worst part was the embarrassment. If you mean the woozy feeling, "
                 "maybe an eight right before I went down. A ten would be my appendix when I was fifteen."),
    ("Temporal pattern", "Just that once. I've felt completely normal since."),
    ("Prior episodes", "I've never fully passed out before. But I get woozy when I have blood drawn. Twice I "
                       "had to lie down so I wouldn't faint."),
    ("Exertion", "No, I wasn't doing anything. I was just standing there. I run three times a week and I've "
                 "never felt faint doing that."),
    ("Standing up quickly", "It didn't happen when I stood up. I'd been standing for a long time."),
    ("Shortness of breath", "No."),
    ("Orthopnea", "No, I sleep on one pillow."),
    ("Waking at night short of breath", "No."),
    ("Palpitations", "No racing or pounding before it, and none since."),
    ("Chest pain", "No."),
    ("Leg swelling", "No."),
    ("Leg pain with walking", "No."),
    ("Cough", "No."),
    ("Nausea, vomiting or sweating", "Yes, right before I fainted I felt sick to my stomach and sweaty, like "
                                     "I said. I didn't throw up."),
    ("Fever", "No."),
    ("Eating and drinking that day", "I had a granola bar and some coffee in the morning and not much water. "
                                     "There wasn't time for lunch."),
    ("Constitutional", "No fevers, no weight change. I feel normal."),
    ("Coughing up blood or wheezing", "No."),
    ("Heartburn or belly pain", "No."),
    ("Neurologic", "No weakness on one side, no trouble talking, no headache, no vision problems now. No "
                   "confusion afterward."),
    ("Last menstrual period", "Two weeks ago, normal. I have the birth control implant in my arm."),
    ("Diarrhea, vomiting or bleeding", "No diarrhea, no vomiting, no heavy bleeding, and my period was "
                                       "normal. No blood pressure pills or water pills."),
    ("Could you be pregnant", "No, I have the implant."),
    ("Anything else", "No, I really feel fine."),
    ("Chronic conditions", "None. I'm healthy."),
    ("Surgeries and procedures", "My appendix out when I was fifteen."),
    ("Hospitalizations", "Just one night for the appendix."),
    ("Prior heart problems", "No. No one has ever told me I have a murmur or a heart problem. My sports "
                             "physicals in high school were normal."),
    ("Prescription medications", "None, other than the birth control implant, for about two years."),
    ("Over-the-counter medicines and supplements", "Ibuprofen for cramps sometimes. No supplements, no diet "
                                                   "pills or energy drinks."),
    ("Allergies", "None that I know of."),
    ("Tobacco", "No, never. I don't vape either."),
    ("Alcohol", "A couple of drinks at parties, maybe twice a month. Nothing before the ceremony."),
    ("Recreational drugs", "No."),
    ("Caffeine", "One iced coffee most mornings."),
    ("Occupation and exposures", "I'm a senior in college, studying elementary education. I work weekends at a "
                                 "coffee shop."),
    ("Exercise and activity", "I run about three miles, three times a week. No problems with it."),
    ("Diet", "Pretty healthy, but I skip meals when I'm busy."),
    ("Living situation", "I share an apartment near campus with two roommates."),
    ("High blood pressure", "No. If anything it's on the low side."),
    ("High cholesterol", "No."),
    ("Diabetes", "No."),
    ("Family history, parents", "My mom has an underactive thyroid. My dad is healthy."),
    ("Family history, heart disease or sudden death", "No one in my family died suddenly or young, and no one "
                                                      "has a heart muscle problem that I know of."),
    ("Family history, seizures", "No one has seizures."),
    ("What she thinks it is", "I think I just got overheated and didn't eat enough."),
    ("Concerns", "I'm in another wedding next month. I don't want to pass out in front of everyone again. And "
                 "my mom's worried it's my heart."),
  ],
  questions=["Is something wrong with my heart?",
             "Am I going to faint again?",
             "I'm in another wedding next month. What can I do so this doesn't happen?"],
  exam={
    "orthostatic": ("Supine 108/68 mmHg, heart rate 64. Standing at 1 minute 104/70, heart rate 74; at 3 "
                    "minutes 106/70, heart rate 76. No fall of more than 20 systolic or 10 diastolic: negative."),
    "bp-both-arms": "Right arm 108/68 mmHg, left arm 106/68 mmHg: within 10 mmHg between the arms.",
    "dynamic": ("No murmur at rest, and none appears or changes with Valsalva or with standing quickly from a "
                "squat."),
  },
  special=[
    ("tongue-inspect", "Tongue and mouth inspection",
     "looks at the tongue and the inside of the cheeks for a bite",
     "No tongue or cheek bite."),
    ("neuro-focused", "Focused neurologic examination",
     "checks orientation, speech, cranial nerves, strength, sensation, coordination and gait",
     "Alert and oriented with fluent speech; cranial nerves intact; strength and sensation normal and "
     "symmetric; finger-to-nose and gait normal. No focal deficit."),
  ],
  key=dict(
    diagnosis="Vasovagal (reflex) syncope triggered by prolonged standing in the heat",
    must_not_miss=["Cardiogenic syncope: an arrhythmia, or an outflow obstruction such as hypertrophic "
                   "cardiomyopathy (the murmur that gets louder with Valsalva or standing) or aortic stenosis"],
    ddx=[
      dict(name="Vasovagal syncope",
           support=("A classic trigger (standing still about 40 minutes in the heat), a warm, nauseated, sweaty "
                    "prodrome with graying vision, a few seconds out and rapid full recovery; near-faints at "
                    "blood draws before; a young woman; normal vital signs, orthostatic vital signs and "
                    "examination."),
           against="Nothing; the history is classic."),
      dict(name="Orthostatic hypotension",
           support="She was upright when it happened, after little food and water.",
           against=("It came after standing still a long time, not on standing up; orthostatic vital signs are "
                    "negative; no medicines, diarrhea or bleeding.")),
      dict(name="Cardiogenic syncope (arrhythmia, or outflow obstruction from aortic stenosis or hypertrophic "
                "cardiomyopathy)",
           support="Any faint has to have the heart excluded, above all the outflow murmur in a young patient.",
           against=("Arrhythmia: a warning prodrome, no palpitations before it, a regular pulse and a normal "
                    "electrocardiogram. Outflow obstruction: not during exertion (she runs without symptoms), no "
                    "chest pain, no murmur at rest or with Valsalva and squat-to-stand, and no family history "
                    "of sudden death.")),
      dict(name="Seizure",
           support="A sudden loss of consciousness.",
           against=("No shaking or jerking, no tongue bite, no incontinence, no postictal confusion; she was "
                    "fully herself within a minute or two; normal neurologic examination.")),
    ],
    studies=[
      dict(test="Electrocardiogram",
           why="Looks for an arrhythmia or a conduction problem behind the faint.",
           expect="Normal sinus rhythm at 66 with normal intervals: lowers suspicion of an arrhythmia."),
      dict(test="Fingerstick glucose",
           why="Excludes hypoglycemia, especially after a skipped lunch.",
           expect="Normal, about 92."),
      dict(test="Urine pregnancy test",
           why="Excludes pregnancy as a contributor to the faint",
           expect="Negative"),
      dict(test="Orthostatic vital signs",
           why="Excludes orthostatic hypotension: a systolic fall of more than 20 or diastolic of more than 10 "
               "within 3 minutes of standing.",
           expect="Negative."),
      dict(test="Tilt-table test",
           why="Only if episodes recur and the cause is unclear.",
           expect="Not needed now; if done, it would reproduce the prodrome with a fall in pressure and heart rate."),
    ],
    plan=[
      "Reassure and educate: education is the treatment, because understanding is the key to compliance.",
      ("Trigger avoidance (standing still for long periods, heat), with safety precautions when a trigger "
       "cannot be avoided, such as lying down for blood draws and injections."),
      ("At the first warmth or nausea, sit or lie down at once; fluids and physical counter-pressure "
       "maneuvers (crossing the legs, tensing the arms)."),
      "Keep a log of each episode (setting, trigger, warning) to show the pattern.",
      ("No emergency workup with a classic history and a normal electrocardiogram; cardiology referral only if "
       "the source becomes unclear."),
    ],
    education=[
      ("This was a common faint, a reflex: standing still in the heat made your nervous system slow your heart "
       "and relax your blood vessels for a moment, your blood pressure dipped, and your brain got a little "
       "less blood for a few seconds."),
      "If you feel faint, sit or lie down wherever you are, at the first warmth or nausea.",
      ("At the wedding, drink plenty of fluids, and at the first warning cross your legs or tense your arms, "
       "then sit or lie down."),
      "Tell staff before blood draws so you can lie down, and keep a log of any episode to bring back.",
      ("Come back at once for a faint with no warning, during exercise, with chest pain or a racing heart, or "
       "with an injury."),
    ],
    red_flags=["A faint with no warning, or during exercise",
               "Fainting with chest pain or a racing heart",
               "A faint that causes an injury"],
    follow_up=("Routine: clinic follow-up with her episode log; cardiology referral only if the history becomes "
               "unclear; return at once for any red flag."),
    presentation=(
      "Ms. Hartwell is a healthy 22-year-old woman presenting after a single faint on Saturday. She had "
      "stood still about 40 minutes as a bridesmaid at an outdoor wedding in the heat when she felt hot, "
      "nauseated and sweaty and her vision grayed; her sister says she was out a few seconds without shaking, "
      "and she recovered fully within minutes. She has felt faint at blood draws before. She denies "
      "palpitations, chest pain, exertional symptoms, tongue biting, incontinence, confusion afterward and "
      "family sudden death. Vital signs are normal and orthostatic vital signs are negative. The cardiac "
      "examination is normal, with no murmur at rest or with Valsalva and squat-to-stand; there is no tongue "
      "bite and the neurologic examination is normal. My differential is vasovagal syncope, orthostatic "
      "hypotension, cardiogenic syncope and seizure. I would order an electrocardiogram and a fingerstick "
      "glucose. My working diagnosis is vasovagal syncope. Plan: education, trigger avoidance, lying down at "
      "the first warning, fluids, counter-pressure maneuvers and an episode log."),
    high_yield=[
      dict(item="Ask exactly what she was doing right before",
           why="A trigger (standing a long time, heat, fear, pain) is the tell-tale of a vasovagal faint."),
      dict(item="Ask what she felt before she went down",
           why="A warm, nauseated, sweaty prodrome points to a reflex faint; collapse with no warning points to the heart."),
      dict(item="Ask the witness about shaking, tongue biting, incontinence and how fast she recovered",
           why="Separates seizure from syncope: rapid full recovery versus prolonged postictal confusion."),
      dict(item="Ask about palpitations, chest pain, fainting with exercise and family sudden death",
           why="The questions that screen for cardiogenic syncope."),
      dict(item="Take orthostatic vital signs, supine then standing within 3 minutes",
           why="Excludes orthostatic hypotension (systolic fall over 20 or diastolic over 10)."),
      dict(item="Auscultate for an outflow murmur, then repeat with Valsalva and squat-to-stand",
           why="A hypertrophic cardiomyopathy murmur gets louder: the cardiogenic faint not to miss in a young patient."),
      dict(item="Inspect the tongue and do a focused neurologic examination",
           why="No tongue bite and no focal deficit argue against seizure and stroke."),
      dict(item="Make education the treatment",
           why="Sit or lie down at the first warning, avoid triggers, fluids, counter-pressure maneuvers, an episode log."),
    ],
  ),
),

# =====================================================================================================
# 6. DILATED CARDIOMYOPATHY
# =====================================================================================================
dict(
  id="cardiac-dilated-cardiomyopathy",
  condition="Dilated cardiomyopathy",
  cites=("CMS L28 Cardiomyopathy, slides 15, 17-45; CMS L25 Heart Failure slides 7, 38; PD2 Cardiovascular "
         "slides 20, 23, 40, 59"),
  door=dict(
    name="Travis Kettleman", sex="male", age=46, dob="February 11, 1980",
    setting="Outpatient primary care clinic",
    cc="\"I've been really tired lately.\"",
    vitals=[("Blood pressure", "104/86 mmHg"),
            ("Heart rate", "108 beats per minute, with occasional skipped beats"),
            ("Respiratory rate", "20 breaths per minute"),
            ("Temperature", "98.0 °F (36.7 °C)"),
            ("Oxygen saturation", "95% on room air"),
            ("Height and weight", "5 feet 11 inches, 172 pounds (body mass index 24.0)")],
  ),
  persona=("A 46-year-old roofing contractor, gruff, proud and a little defensive, especially about his "
           "drinking, which he plays down until he is asked plainly how much. He is used to being the strong "
           "one and is frustrated and scared that he cannot keep up at work. He speaks in short sentences and "
           "gets short of breath in longer ones."),
  opening="I'm wiped out all the time. The last couple of months I can't climb a ladder without stopping.",
  facts=[
    ("Full name", "Travis Kettleman."),
    ("Date of birth", "February 11, 1980."),
    ("Onset", "About three months ago. It started with getting worn out on jobs and it's been getting worse "
              "every few weeks."),
    ("Location", "It's not a pain. It's my whole body tired, and my breathing."),
    ("Duration", "I'm tired all day, every day now. The breathing comes on whenever I work or climb, and "
                 "settles after I sit for a few minutes."),
    ("Character", "Wiped out, like I've got no gas in the tank. And winded, like I can't get enough air."),
    ("How far he can go", "Three months ago I could carry bundles of shingles up a ladder all day. Six weeks "
                          "ago I was stopping halfway. Now one flight of stairs and I have to stop."),
    ("Alleviating factors", "Sitting down. Sleeping propped up."),
    ("Aggravating factors", "Ladders, stairs, carrying anything, lying flat."),
    ("Radiation", "No pain going anywhere."),
    ("Severity", "The breathing is a seven out of ten on a ladder. A ten was when I fell off a roof in 2009 "
                 "and broke my ribs."),
    ("Temporal pattern", "Worse at night lying down, and worse every few weeks than before."),
    ("Prior episodes", "Never had anything like this. I've always been the guy who outworks everybody."),
    ("Shortness of breath", "Yes, with any work or the stairs. Sitting still I'm mostly okay."),
    ("Orthopnea", "I sleep on three pillows now, or in the recliner. Flat, I feel like I'm suffocating."),
    ("Waking at night short of breath", "Yes, a few times a week I wake up gasping and have to sit up on the "
                                        "edge of the bed."),
    ("Palpitations", "Sometimes my heart skips and then flip-flops. It doesn't race for long, just skips."),
    ("Fainting or near-fainting", "No, I haven't passed out."),
    ("Leg swelling", "Yes, my ankles are swollen most evenings, both of them."),
    ("Belly swelling and weight", "My belly's bigger and my work pants are tight. I've put on about ten pounds "
                                  "in two months, and I'm barely eating."),
    ("Leg pain with walking", "No, my legs don't hurt. It's the wind."),
    ("Cough", "A dry cough at night when I lie down. Nothing comes up."),
    ("Chest pain", "No chest pain. Just the breathing."),
    ("Nausea, vomiting or sweating", "No vomiting, no sweats. No appetite, and I feel full fast."),
    ("Fever", "No."),
    ("Recent illness", "No colds or flu that I remember in the last year."),
    ("Constitutional", "No fevers. Exhausted all the time. Weight up even though I'm eating less."),
    ("Coughing up blood or wheezing", "No."),
    ("Heartburn or belly pain", "No heartburn. My belly feels full and tight, not painful."),
    ("Neurologic", "No weakness on one side, no trouble talking, no vision change."),
    ("Anything else", "No. That's plenty."),
    ("Chronic conditions", "None that I know of. I don't really go to doctors."),
    ("Last checkup", "A physical for a work insurance thing about three years ago. They said everything was "
                     "normal, blood pressure fine, no murmur."),
    ("Surgeries and procedures", "None. Just the broken ribs that healed on their own."),
    ("Hospitalizations", "Two nights after the fall in 2009."),
    ("Prior heart problems", "No heart attacks, no heart problems that anyone ever told me."),
    ("Cancer or chemotherapy", "No, never had cancer or any chemotherapy."),
    ("Prescription medications", "None."),
    ("Over-the-counter medicines and supplements", "Ibuprofen sometimes for my back. No supplements."),
    ("Allergies", "None that I know of."),
    ("Tobacco", "Half a pack a day since I was about twenty."),
    ("Alcohol", "(Hesitates.) More than I should. A twelve-pack most days after work, more on the weekend. "
                "For fifteen years, maybe longer."),
    ("Recreational drugs", "No. No cocaine, no meth, nothing like that."),
    ("Heat intolerance, tremor or weight loss", "No. I'm not hot, no shakes. The weight I've gained is "
                                                "fluid, I think."),
    ("Diet", "I skip meals a lot. Mostly one meal a day, whatever's quick."),
    ("Occupation and exposures", "I run a small roofing crew. Up and down ladders all day in the heat."),
    ("Exercise and activity", "Work is my exercise. I can't keep up with my crew now."),
    ("Living situation", "I live with my girlfriend, Dana. No kids."),
    ("High blood pressure", "No, it was always normal when they checked."),
    ("High cholesterol", "Not that I know of."),
    ("Diabetes", "No."),
    ("Family history, parents", "My dad has high blood pressure, he's 70. My mom is healthy."),
    ("Family history, siblings", "One sister, healthy."),
    ("Family history, heart muscle disease or sudden death", "No one with a weak or enlarged heart, and no one "
                                                             "who died suddenly or young."),
    ("What he thinks it is", "I figured I'm just run down. Getting older. Too much work."),
    ("Concerns", "Dana says I look gray. I'm scared I can't work, and that something's really wrong with my "
                 "heart."),
  ],
  questions=["Is my heart going to get better?",
             "Do I really have to stop drinking completely?",
             "Am I going to need a heart transplant?"],
  exam={
    "general-survey": ("Lean man sitting upright, mildly short of breath after walking into the room but "
                       "speaking in full sentences; slightly pale, no sweating, no distress at rest."),
    "carotid-palp": "Carotid pulses are small and weak, 1+ and symmetric. No thrill.",
    "hands-nails": "Hands are cool. Nail beds are pink, with no cyanosis and no clubbing.",
    "jvp": ("Jugular venous distention at 30 degrees, with the pulsation visible about 6 centimeters above the "
            "sternal angle."),
    "precordium-inspect": "The apical impulse is visible lateral to the midclavicular line, low on the chest wall.",
    "pmi": ("The point of maximal impulse is diffuse, about 4 centimeters across, and displaced laterally and "
            "down to the sixth intercostal space at the anterior axillary line."),
    "ausc-aortic": ("Aortic area: fast, regular rhythm at about 108 with occasional early beats followed by a "
                    "pause; normal first and second heart sounds; no murmur at the base."),
    "ausc-tricuspid": ("Tricuspid area: a soft, blowing holosystolic murmur at the lower left sternal border "
                       "that gets slightly louder on inspiration."),
    "ausc-mitral": ("Mitral area: a harsh, medium-to-high-pitched holosystolic murmur, grade 3 out of 6, at the "
                    "apex radiating to the left axilla, with a third heart sound right after the second."),
    "left-lateral": ("Left lateral decubitus, bell at the apex: a loud third heart sound right after the second "
                     "heart sound, the 'Ken-TUC-ky' cadence; the holosystolic murmur is heard here too."),
    "dynamic": "Isometric handgrip and squatting: the apical holosystolic murmur gets louder.",
    "lung-bases": "Fine crackles at both posterior lung bases.",
    "ext-inspect": ("Both lower legs are symmetrically swollen; the skin is cool. No brown staining, no "
                    "varicose veins, no ulcers."),
    "pulses": ("Pulses are present and symmetric on both sides; the radial pulse is fast and regular with "
               "occasional early, weak beats."),
    "cap-refill": "Capillary refill is about 3 seconds, and the fingers and toes are cool.",
    "edema": "2+ pitting edema over both feet, ankles and shins, symmetric, to mid-shin.",
    "bp-both-arms": ("Right arm 104/86 mmHg, left arm 102/84 mmHg: within 10 mmHg between the arms, with a "
                     "narrow pulse pressure of about 18."),
  },
  special=[
    ("hepatojugular-reflux", "Hepatojugular reflux",
     "presses firmly over the right upper abdomen for about 10 seconds while watching the neck veins",
     "Positive: the neck veins distend further and stay up for as long as the pressure is held."),
    ("liver-edge", "Liver edge palpation",
     "palpates upward from the right lower abdomen for the liver edge below the right costal margin",
     "The liver edge is smooth and tender, palpable about 4 centimeters below the right costal margin."),
    ("pulsus-paradoxus", "Pulsus paradoxus measurement",
     "with a manual cuff, deflates slowly and notes where the sounds appear only in expiration, then where "
     "they are heard throughout breathing",
     "The gap is 4 mmHg."),
    ("abdomen-fluid", "Abdominal inspection and percussion", "inspects the abdomen and percusses for fluid",
     "The abdomen is distended and full, with a fluid wave and shifting dullness; the flanks bulge."),
  ],
  key=dict(
    diagnosis=("Dilated cardiomyopathy, most likely from long-term heavy alcohol use, presenting as heart "
               "failure with reduced ejection fraction and secondary mitral regurgitation"),
    must_not_miss=["Acute coronary syndrome or coronary disease as the cause: dilated cardiomyopathy is "
                   "dysfunction without severe occlusive coronary disease, so check the electrocardiogram and "
                   "troponin",
                   "A sudden arrhythmia: fainting or a sustained racing heartbeat means the emergency department"],
    ddx=[
      dict(name="Dilated cardiomyopathy",
           support=("A 46-year-old man with about fifteen years of heavy drinking and poor eating, three months "
                    "of fatigue and progressive exertional breathlessness, three-pillow orthopnea, waking up "
                    "gasping, ankle and belly swelling with a 10-pound gain, and skipped beats. A laterally "
                    "displaced, diffuse point of maximal impulse, a third heart sound, apical mitral and "
                    "tricuspid regurgitation murmurs, raised neck veins, a positive hepatojugular reflux, an "
                    "enlarged liver, basal crackles, cool extremities, edema and a narrow pulse pressure."),
           against=("Nothing in the history; the echocardiogram must show dilated, thin-walled chambers with a "
                    "low ejection fraction and no primary valve lesion.")),
      dict(name="Acute coronary syndrome (or ischemic heart disease as the cause of the failure)",
           support="Heart failure in a man in his 40s who smokes.",
           against=("No chest pain or exertional pressure; no ST changes and a normal troponin. Dilated "
                    "cardiomyopathy is defined by failure without severe occlusive coronary disease, which "
                    "cardiology confirms.")),
      dict(name="Valvular heart disease (mitral regurgitation or aortic stenosis)",
           support="A holosystolic apical murmur radiating to the axilla, louder with handgrip.",
           against=("No murmur three years ago; no aortic stenosis murmur at the base; the ventricle is dilated "
                    "with globally weak squeeze, so the regurgitation followed the stretched ventricle rather "
                    "than causing it.")),
      dict(name="Cardiac tamponade",
           support="Raised neck veins, breathlessness, a fast heart rate and a narrow pulse pressure.",
           against=("No hypotension, heart sounds are not muffled (a third heart sound and murmurs are heard), "
                    "no pulsus paradoxus, crackles rather than clear lungs, and no effusion on the "
                    "echocardiogram.")),
    ],
    studies=[
      dict(test="Echocardiogram",
           why="Confirms the diagnosis and separates it from valve disease and tamponade.",
           expect=("Dilated, thin-walled chambers (the prominent feature), globally hypokinetic, ejection "
                   "fraction about 25%, with mitral and tricuspid regurgitation; no pericardial effusion and no "
                   "primary valve lesion.")),
      dict(test="Electrocardiogram",
           why="Usually abnormal in dilated cardiomyopathy; a normal tracing almost rules it out.",
           expect=("Sinus tachycardia at 108 with frequent premature ventricular contractions and left "
                   "ventricular hypertrophy; no ST elevation or depression.")),
      dict(test="Chest X-ray",
           why="Looks for cardiomegaly and congestion.",
           expect="Cardiomegaly, small pleural effusions and Kerley B lines (pulmonary edema)."),
      dict(test="B-type natriuretic peptide and troponin",
           why=("An elevated natriuretic peptide means raised filling pressure (below 100 excludes heart "
                "failure); a rising troponin with ST changes would point to acute coronary syndrome."),
           expect="Natriuretic peptide elevated, about 820; troponin normal."),
      dict(test="Labs for a cause: complete blood count, metabolic panel, liver tests, thyroid function",
           why="Anemia, electrolytes and kidney function, liver changes from alcohol, thyroid disease.",
           expect="No anemia; potassium and kidney function normal; liver tests mildly raised; thyroid normal."),
    ],
    plan=[
      ("Remove the cause: stop alcohol completely (heart function can recover when drinking stops), correct "
       "nutritional deficiency such as thiamine, and quit smoking."),
      ("Heart failure medicines: an angiotensin-converting enzyme inhibitor (lisinopril), angiotensin receptor "
       "blocker (losartan) or sacubitril-valsartan; a beta blocker (carvedilol, metoprolol succinate or "
       "bisoprolol); spironolactone; a diuretic (furosemide) for the fluid."),
      "Sodium under 2 grams a day; follow potassium and kidney function.",
      ("Urgent cardiology referral, with an echocardiogram within days, to establish care, consider genetic "
       "testing and plan devices."),
      ("Implantable cardioverter-defibrillator if the ejection fraction stays under 35% on maximum medical "
       "therapy; a biventricular pacemaker, ventricular assist device or transplantation in advanced disease."),
      ("Emergency department now for breathlessness at rest, chest pain, fainting or a sustained racing "
       "heartbeat."),
    ],
    education=[
      ("Your heart muscle has stretched and weakened, most likely from years of heavy drinking, so it pumps "
       "poorly and fluid backs up into your lungs, belly and legs."),
      ("Stopping alcohol completely is the most important thing you can do: the heart can recover when the "
       "drinking stops."),
      ("Take every medicine and keep every follow-up; how well you do depends on how well the treatment works, "
       "and about half of people with this die within 5 years if it progresses."),
      "Keep salt under 2 grams a day, and stop smoking.",
      "Call 911 for fainting, chest pain, breathlessness at rest or a racing heartbeat that does not stop.",
    ],
    red_flags=["Fainting", "Chest pain", "Breathlessness at rest",
               "A racing heartbeat that does not stop"],
    follow_up=("Urgent: cardiology and an echocardiogram within days; emergency department now for "
               "breathlessness at rest, chest pain, fainting or a sustained racing heartbeat."),
    presentation=(
      "Mr. Kettleman is a 46-year-old roofer, a smoker who drinks a twelve-pack a day, with no known heart "
      "disease or hypertension, presenting with three months of fatigue and breathlessness, now after one "
      "flight of stairs. He sleeps on three pillows, wakes gasping, has ankle and "
      "belly swelling with a 10-pound gain, and feels skipped beats. He denies chest pain, fainting and "
      "family cardiomyopathy or sudden death. Heart rate is 108 with early beats; blood pressure 104/86, a "
      "narrow pulse pressure. He has jugular venous distention, a positive "
      "hepatojugular reflux, an enlarged liver, a diffuse apical impulse displaced to the sixth intercostal "
      "space at the anterior axillary line, a third heart sound, an apical holosystolic murmur to the axilla, "
      "basal crackles, cool extremities and 2+ edema, without pulsus paradoxus. My differential is dilated "
      "cardiomyopathy, acute coronary syndrome, valvular disease and tamponade. I would order an "
      "echocardiogram, electrocardiogram, chest X-ray, natriuretic peptide, troponin and labs. My "
      "working diagnosis is alcohol-related dilated cardiomyopathy. Plan: stop alcohol, heart failure "
      "medicines, salt restriction, urgent cardiology."),
    high_yield=[
      dict(item="Ask how far he could walk or climb three months ago, six weeks ago, and now",
           why="Quantifies the progressive exertional breathlessness that dilated cardiomyopathy presents with."),
      dict(item="Ask plainly how much alcohol, and about chemotherapy, recent viral illness and family history",
           why="Search for the cause: alcohol, chemotherapy, myocarditis, or a relative with cardiomyopathy or sudden death."),
      dict(item="Palpate and document the point of maximal impulse",
           why="Laterally displaced to the sixth intercostal space at the anterior axillary line means a dilated heart."),
      dict(item="Listen with the bell at the apex in left lateral decubitus",
           why="The third heart sound of a volume-overloaded, dilated ventricle."),
      dict(item="Describe the apical murmur and do handgrip or squatting",
           why="Holosystolic to the axilla and louder with handgrip is mitral regurgitation, here from the stretched ventricle."),
      dict(item="Measure pulsus paradoxus and note the pulse pressure",
           why="No pulsus paradoxus argues against tamponade; a narrow pulse pressure reflects low stroke volume."),
      dict(item="Do the hepatojugular reflux and listen at the lung bases",
           why="Right-sided congestion and crackles grade how decompensated he is."),
      dict(item="Tell him alcohol cessation can let the heart recover",
           why="Removing the cause is the first line of the plan."),
    ],
  ),
),

]


# =========================================================================================== self-check
if __name__ == "__main__":
    import datetime
    import re
    from _osce_cardiac_catalog import CATALOG
    from _pd2_cardiac_osce_data import ROWS

    ORDER = ["Chronic heart failure", "Atrial fibrillation", "Aortic stenosis",
             "Chronic venous insufficiency and varicose veins", "Vasovagal syncope", "Dilated cardiomyopathy"]
    BARRED = {"Stable angina", "Acute pericarditis", "Peripheral artery disease", "Deep vein thrombosis"}
    TODAY = datetime.date(2026, 10, 26)
    # Typical ages, from tools/_pd2_cardiac_osce_ages.py, as inclusive (low, high).
    AGE_RANGE = {"Chronic heart failure": (65, 100), "Atrial fibrillation": (55, 100),
                 "Aortic stenosis": (66, 100), "Chronic venous insufficiency and varicose veins": (40, 100),
                 "Vasovagal syncope": (15, 39), "Dilated cardiomyopathy": (20, 60)}
    VITALS = ["Blood pressure", "Heart rate", "Respiratory rate", "Temperature", "Oxygen saturation",
              "Height and weight"]
    ABBREV = re.compile(r"\b(JVD|JVP|PMI|ECG|EKG|BNP|NT-proBNP|CRP|ESR|NSAIDs?|TAVR|DOACs?|RUSB|LUSB|LLSB|LSB|"
                        r"ICS|SOB|DOE|PND|MI|CAD|CHF|HFrEF|HFpEF|COPD|GERD|LVH|RVR|ED|ER|PPI|NTG|ASA|ABI|"
                        r"DVT|PAD|CVI|HCM|HOCM|DCM|MR|AS|TR|BP|HR|RR|ICD|ARNI|ACE|ARB|MRA|SGLT2|TSH|CBC|"
                        r"CMP|LFTs?|CT|MRI|IV|IUD|TV|A1C|BMI|EF|NYHA|LV|RV|CXR)\b")

    def strings(obj, skip=("cites",)):
        if isinstance(obj, str):
            yield obj
        elif isinstance(obj, dict):
            for k, v in obj.items():
                if k not in skip:
                    yield from strings(v, skip)
        elif isinstance(obj, (list, tuple)):
            for v in obj:
                yield from strings(v, skip)

    def slug(s):
        return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

    assert len(CASES) == 6, len(CASES)
    assert [c["condition"] for c in CASES] == ORDER, [c["condition"] for c in CASES]
    ids = [c["id"] for c in CASES]
    assert len(set(ids)) == len(ids), "duplicate ids"
    sexes = [c["door"]["sex"] for c in CASES]
    assert sexes.count("female") >= 2 and sexes.count("male") >= 2, sexes
    for c in CASES:
        cond, d, k = c["condition"], c["door"], c["key"]
        where = c["id"]
        assert cond in ROWS, (where, "not a chart row")
        assert cond not in BARRED, (where, "barred case")
        assert c["id"] == "cardiac-" + slug(cond), where
        assert d["sex"] in ("male", "female"), where
        assert isinstance(d["age"], int), where
        lo, hi = AGE_RANGE[cond]
        assert lo <= d["age"] <= hi, (where, d["age"])
        born = datetime.datetime.strptime(d["dob"], "%B %d, %Y").date()
        age = TODAY.year - born.year - ((TODAY.month, TODAY.day) < (born.month, born.day))
        assert age == d["age"], (where, "dob gives", age)
        assert d["cc"].startswith('"') and d["cc"].endswith('"') and len(d["cc"]) < 90, (where, d["cc"])
        assert [v[0] for v in d["vitals"]] == VITALS, where
        assert len(c["opening"]) < 160, (where, len(c["opening"]))
        assert 45 <= len(c["facts"]) <= 80, (where, len(c["facts"]))
        topics = [f[0] for f in c["facts"]]
        assert len(set(topics)) == len(topics), (where, "duplicate fact topic")
        assert topics[:2] == ["Full name", "Date of birth"], where
        assert all(len(f) == 2 and all(isinstance(x, str) and x for x in f) for f in c["facts"]), where
        assert 2 <= len(c["questions"]) <= 3, where
        for mid in c["exam"]:
            assert mid in CATALOG, (where, "unknown maneuver", mid)
        for sp in c["special"]:
            assert len(sp) == 4 and sp[0] not in CATALOG, (where, sp[0])
        assert len(c["special"]) <= 4, where
        assert "bp-both-arms" in c["exam"], where
        bp = d["vitals"][0][1].split()[0]
        assert bp in c["exam"]["bp-both-arms"], (where, "door blood pressure not in bp-both-arms")
        assert 1 <= len(k["must_not_miss"]) <= 2, where
        assert len(k["ddx"]) == 4, where
        assert cond.lower() in k["ddx"][0]["name"].lower(), (where, "own condition not first")
        chart_ddx = [n for n, _ in ROWS[cond]["ddx"]]
        for mine, chart in zip(k["ddx"][1:], chart_ddx):
            assert mine["name"].startswith(chart), (where, mine["name"], chart)
        assert all(set(x) == {"name", "support", "against"} for x in k["ddx"]), where
        assert 3 <= len(k["studies"]) <= 5, where
        assert all(set(x) == {"test", "why", "expect"} for x in k["studies"]), where
        assert 3 <= len(k["plan"]) <= 6, where
        assert 3 <= len(k["education"]) <= 5, where
        assert 2 <= len(k["red_flags"]) <= 4, where
        assert 5 <= len(k["high_yield"]) <= 8, where
        assert all(set(x) == {"item", "why"} for x in k["high_yield"]), where
        assert isinstance(k["follow_up"], str) and k["follow_up"], where
        words = len(k["presentation"].split())
        assert 120 <= words <= 170, (where, "presentation words", words)
        for s in strings(c):
            low = s.lower()
            for bad in ("slide", "lecture", "professor"):
                assert bad not in low, (where, bad, s[:80])
            m = ABBREV.search(s)
            assert not m, (where, "abbreviation", m.group(0) if m else "", s[:80])
        print("%-58s %-6s %3d  facts %2d  exam %2d  special %d  presentation %3d words  cc %s"
              % (c["id"], d["sex"], d["age"], len(c["facts"]), len(c["exam"]), len(c["special"]), words, d["cc"]))
    print("OK: %d cases" % len(CASES))
