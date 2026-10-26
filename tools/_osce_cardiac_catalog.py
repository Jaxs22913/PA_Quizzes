# -*- coding: utf-8 -*-
"""The cardiac OSCE practice station's maneuver catalog (2026-10-26).

Every maneuver the Cardiac OSCE run-sheet (tools/build_pd2_osce.py, CARDIAC_EXAM) asks for, plus the special
positions and maneuvers the cardiac chart's "exam" column uses, each with the finding the facilitator gives
when the patient is NORMAL there. A case (tools/_osce_cardiac_cases.py) overrides only what is abnormal for
its condition. Maneuvers on other systems (abdomen, neurologic, ...) are not listed: the patient model
answers those as normal, in keeping with the case (Jaxon, 2026-10-26: the slides will not cover other
systems' findings or review-of-systems answers).

Each entry: id -> (name the facilitator and the grader see, what the student would say to do it, normal finding).
"""

CATALOG = {
    "position": ("Positions the patient",
                 "lie back, head of the bed at 30 degrees",
                 "The patient is lying back with the head of the bed at 30 degrees."),
    "general-survey": ("General survey",
                       "looks at the patient: distress, color, work of breathing, sweating",
                       "Alert and oriented, comfortable at rest, in no acute distress. Normal color, no sweating, "
                       "breathing is unlabored."),
    "hands-nails": ("Hands and nail beds",
                    "inspects the hands and nails for cyanosis and clubbing",
                    "Hands are warm. Nail beds are pink, with no cyanosis and no clubbing."),
    "jvp": ("Jugular veins",
            "inspects the neck for jugular vein distention",
            "No jugular vein distention at 30 degrees."),
    "carotid-inspect": ("Carotid inspection",
                        "inspects the carotid pulses",
                        "Carotid pulsations are visible, normal and symmetric."),
    "carotid-ausc": ("Carotid auscultation",
                     "holds breath, listens over each carotid with diaphragm and bell",
                     "No bruit over either carotid."),
    "carotid-palp": ("Carotid palpation",
                     "palpates each carotid, one side at a time",
                     "Carotid pulses are 2+ and symmetric, with a brisk upstroke and no thrill."),
    "precordium-inspect": ("Precordium inspection",
                           "inspects the chest wall with tangential light",
                           "No visible heaves, lifts or abnormal pulsations on the chest wall."),
    "precordium-palp": ("Precordium palpation for heaves and lifts",
                        "finger pads over the aortic, pulmonic, Erb's point, tricuspid and mitral areas",
                        "No heaves or lifts over the aortic, pulmonic, Erb's point, tricuspid or mitral areas."),
    "pmi": ("Point of maximal impulse",
            "finds the apical impulse: location, size, intensity",
            "The point of maximal impulse is a light tap about 2 centimeters across, at the fifth intercostal "
            "space in the left midclavicular line. It is not displaced."),
    "thrills": ("Palpation for thrills",
                "ball of the hand over all five areas",
                "No thrills over any of the five areas."),
    "ausc-aortic": ("Auscultation, aortic area",
                    "second intercostal space, right sternal border, diaphragm and bell",
                    "Aortic area: regular rate and rhythm, normal first and second heart sounds, no murmur."),
    "ausc-pulmonic": ("Auscultation, pulmonic area",
                      "second intercostal space, left sternal border, diaphragm and bell",
                      "Pulmonic area: normal first and second heart sounds, no murmur."),
    "ausc-erb": ("Auscultation, Erb's point",
                 "third intercostal space, left sternal border, diaphragm and bell",
                 "Erb's point: normal heart sounds, no murmur."),
    "ausc-tricuspid": ("Auscultation, tricuspid area",
                       "fourth intercostal space, left sternal border, diaphragm and bell",
                       "Tricuspid area: normal first and second heart sounds, no murmur."),
    "ausc-mitral": ("Auscultation, mitral area",
                    "fifth intercostal space, left midclavicular line, diaphragm and bell",
                    "Mitral area: normal first and second heart sounds. No murmur, no third or fourth heart sound."),
    "left-lateral": ("Left lateral decubitus, bell at the apex",
                     "rolls the patient onto the left side, listens at the apex with the bell",
                     "Left lateral decubitus, bell at the apex: no extra heart sounds and no murmur."),
    "lean-forward": ("Sitting up and leaning forward",
                     "sits the patient up, leaning forward, breath out, diaphragm along the left sternal border",
                     "Leaning forward at end-expiration: no murmur and no rub along the left sternal border."),
    "dynamic": ("Dynamic maneuvers (Valsalva, squat to stand, handgrip)",
                "asks the patient to bear down, squat and stand, or squeeze a fist while listening",
                "No murmur appears or changes with the maneuver."),
    "lung-bases": ("Lung bases",
                   "listens to the posterior lung bases on both sides",
                   "Lungs are clear at both bases. No crackles."),
    "ext-inspect": ("Extremity inspection",
                    "inspects the legs and arms: size, symmetry, color, veins, hair, ulcers",
                    "Arms and legs are symmetric with no swelling. Normal color and hair growth, no varicose veins, "
                    "no ulcers."),
    "pulses": ("Peripheral pulses",
               "brachial, radial, femoral, popliteal, posterior tibial and dorsalis pedis, both sides",
               "Brachial, radial, femoral, popliteal, posterior tibial and dorsalis pedis pulses are 2+ and "
               "symmetric on both sides."),
    "cap-refill": ("Capillary refill",
                   "presses a nail bed on a hand and a foot",
                   "Capillary refill is under 2 seconds in the fingers and toes."),
    "edema": ("Pitting edema",
              "presses over the tibia and ankles",
              "No pitting edema over the shins or ankles."),
    "bp-both-arms": ("Blood pressure in both arms",
                     "rechecks the blood pressure in both arms",
                     "Blood pressure is within 10 mmHg between the two arms."),
    "orthostatic": ("Orthostatic vital signs",
                    "blood pressure and heart rate lying, then standing",
                    "No significant drop in blood pressure and no large rise in heart rate on standing."),
}
