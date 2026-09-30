# -*- coding: utf-8 -*-
"""Physical Diagnosis 2, Exam 2 -- the heart-sound listening quiz (18 questions) and its clips.

Every recording is from the University of Michigan Heart Sound & Murmur Library (Richard D. Judge and
Rajesh Mangrulkar, CC BY-SA 3.0). The lecture deck embeds the library's first recording byte for byte
(slide 36), which is how the provenance of the set was confirmed.

Questions use only what the lecture deck teaches (slides-only grounding). Library clips the deck does not
teach (an early systolic murmur, a split first heart sound, a combined systolic and diastolic aortic
murmur) are on the listening guide but are not asked. Clips 14 and 18 are the same recording under two
labels, so only 18 is shipped.
"""

DECK = "PD II Advanced Cardiovascular & Peripheral Vascular System - Fall 2026.pptx"
LIB_URL = "https://open.umich.edu/find/open-educational-resources/medical/heart-sound-murmur-library"
CREDIT = ('Recording: <a href="%s" target="_blank" rel="noopener">Heart Sound &amp; Murmur Library</a>, Richard D. Judge and '
          'Rajesh Mangrulkar, University of Michigan, <a href="https://creativecommons.org/licenses/by-sa/3.0/" '
          'target="_blank" rel="noopener">CC BY-SA 3.0</a>. Shortened to a 20-second excerpt.' % LIB_URL)
ALT = "A recording made through a stethoscope. Press play to listen."

SOUNDS_IO = "Compare and contrast the cardiac cycle with reference to timing of heart sounds and gallops"
MURMUR_IO = "Identify the physical characteristics of cardiac thrills and murmurs"

# ---- clip metadata: file (as trimmed), library title, recording position, deck slides that teach it ----
# `where` is the library's own description: area, patient position, chest piece.
CLIPS = {
    "01": ("01_apex_normal_s1_s2_supine_bell.mp3", "Normal S1 and S2", "Apex, supine, bell"),
    "02": ("02_apex_split_s1_supine_bell.mp3", "Split S1", "Apex, supine, bell"),
    "03": ("03_apex_s4_lld_bell.mp3", "S4 gallop", "Apex, left lateral decubitus, bell"),
    "04": ("04_apex_mid_sys_click_supine_bell.mp3", "Mid-systolic click", "Apex, supine, bell"),
    "05": ("05_apex_s3_lld_bell.mp3", "S3 gallop", "Apex, left lateral decubitus, bell"),
    "06": ("06_apex_early_sys_mur_supine_bell.mp3", "Early systolic murmur", "Apex, supine, bell"),
    "07": ("07_apex_mid_sys_mur_supine_bell.mp3", "Mid-systolic murmur", "Apex, supine, bell"),
    "08": ("08_apex_late_sys_mur_supine_bell.mp3", "Late systolic murmur", "Apex, supine, bell"),
    "09": ("09_apex_holo_sys_mur_supine_bell.mp3", "Holosystolic murmur", "Apex, supine, bell"),
    "10": ("10_apex_sys_click_late_sys_mur_lld_bell.mp3", "Systolic click with a late systolic murmur", "Apex, left lateral decubitus, bell"),
    "11": ("11_apex_s4_mid_sys_mur_lld_bell.mp3", "S4 with a mid-systolic murmur", "Apex, left lateral decubitus, bell"),
    "12": ("12_apex_s3_holo_sys_mur_lld_bell.mp3", "S3 with a holosystolic murmur", "Apex, left lateral decubitus, bell"),
    "13": ("13_apex_os_dias_mur_lld_bell.mp3", "Mitral opening snap with a diastolic murmur", "Apex, left lateral decubitus, bell"),
    "15": ("15_aortic_sys_mur_absent_s2_sitting_bell.mp3", "Systolic murmur with an absent S2", "Aortic area, sitting, bell"),
    "16": ("16_aortic_early_dias_mur_sitting_bell.mp3", "Early diastolic murmur", "Aortic area, sitting, bell"),
    "17": ("17_aortic_sys_dias_mur_sitting_bell.mp3", "Systolic and diastolic murmurs", "Aortic area, sitting, bell"),
    "18": ("18_pulm_single_s2_supine_diaph.mp3", "Single S2", "Pulmonic area, supine, diaphragm"),
    "19": ("19_pulm_split_s2_persistent_supine_diaph.mp3", "Persistent split S2", "Pulmonic area, supine, diaphragm"),
    "20": ("20_pulm_split_s2_transient_supine_diaph.mp3", "Transient split S2", "Pulmonic area, supine, diaphragm"),
    "21": ("21_pulm_eject_sys_mur_trans_split_s2_supine_diaph.mp3", "Ejection systolic murmur with a transient split S2", "Pulmonic area, supine, diaphragm"),
    "22": ("22_pulm_split_s2_eject_sys_mur_supine_diaph.mp3", "Ejection systolic murmur with a persistent split S2", "Pulmonic area, supine, diaphragm"),
    "23": ("23_pulm_eject_sys_mur_single_s2_eject_click_supine_diaph.mp3", "Ejection systolic murmur with a single S2 and an ejection click", "Pulmonic area, supine, diaphragm"),
}

AT_APEX = "Heard at the apex with the patient supine. "
AT_APEX_LLD = "Heard at the apex with the patient in the left lateral decubitus position. "
AT_AORTIC = "Heard at the aortic area with the patient sitting. "
AT_PULM = "Heard at the pulmonic area with the patient supine, over several breaths. "

# The five sound-plus-murmur patterns that recur as options. Each is right for exactly one clip.
P_CLICK = "Mid-systolic click, then a late systolic murmur"
P_SNAP = "Opening snap, then a diastolic murmur"
P_S3 = "S3 gallop with a holosystolic murmur"
P_S4 = "S4 gallop with a mid-systolic murmur"
P_EJ = "Ejection sound with a mid-systolic murmur"

# The four timing-by-splitting combinations for the pulmonic-area ejection murmurs.
C_MP = "Mid-systolic murmur with physiologic splitting of S2"
C_MX = "Mid-systolic murmur with pathologic splitting of S2"
C_HP = "Holosystolic murmur with physiologic splitting of S2"
C_HX = "Holosystolic murmur with pathologic splitting of S2"


def slide(n):
    return "%s, Slide %d" % (DECK, n)


# (clip, stem, topic, io, slide, correct_text, correct_expl, [(distractor, expl) x3])
POOL = [
    ("01", AT_APEX + "Which heart sounds are these?", "Normal S1 and S2", SOUNDS_IO, 34,
     "Normal S1 and S2 only",
     "Correct. S1 is closure of the mitral and tricuspid valves and S2 is closure of the aortic and pulmonic valves, with nothing extra in systole or diastole.",
     [("S1 and S2 followed by an S3 gallop", "An S3 would follow S2 early in diastole with the cadence Ken-TUC-ky; here the pair of sounds repeats with nothing after S2."),
      ("An S4 gallop before S1 and S2", "An S4 sits just before S1 with the cadence Ten-nes-SEE; here nothing comes before S1."),
      ("S1, a mid-systolic click, then S2", "A click is a high-pitched extra sound in mid to late systole, between S1 and S2; the gap between S1 and S2 here is silent.")]),

    ("03", AT_APEX_LLD + "What extra heart sound is this?", "S4 gallop", SOUNDS_IO, 42,
     "S4, the atrial gallop",
     "Correct. S4 falls just before S1 with the cadence Ten-nes-SEE; it is dull and low pitched and is best heard with the bell at the apex.",
     [("S3, the ventricular gallop", "S3 comes after S2, early in diastole, with the cadence Ken-TUC-ky; the sound here comes just before S1, which is S4."),
      ("Mitral opening snap", "An opening snap is a sharp, high-pitched, very early diastolic sound from a stenotic mitral valve, not a dull low-pitched one."),
      ("Mid-systolic click", "A click is high pitched and falls in mid to late systole, between S1 and S2, not just before S1.")]),

    ("05", AT_APEX_LLD + "What extra heart sound is this?", "S3 gallop", SOUNDS_IO, 40,
     "S3, the ventricular gallop",
     "Correct. S3 comes after S2, early in diastole, with the cadence Ken-TUC-ky, and is best heard with the bell at the apex in left lateral decubitus.",
     [("S4, the atrial gallop", "S4 comes just before S1 with the cadence Ten-nes-SEE; the extra sound here follows S2 instead."),
      ("Early systolic ejection sound", "An ejection sound comes right after S1, is sharp and high pitched and is heard with the diaphragm; S3 is a low-pitched diastolic sound."),
      ("Mid-systolic click", "A click falls in mid to late systole, between S1 and S2, and is high pitched; S3 falls in diastole, after S2.")]),

    ("04", AT_APEX + "What extra heart sound is this?", "Mid-systolic click", SOUNDS_IO, 39,
     "Mid-systolic click",
     "Correct. A click is a high-pitched extra sound in mid to late systole, usually from mitral valve prolapse, and is heard with the diaphragm.",
     [("S3 gallop", "S3 is a low-pitched diastolic sound after S2 with the cadence Ken-TUC-ky, not a sharp sound in the middle of systole."),
      ("Mitral opening snap", "An opening snap is diastolic, very soon after S2, and comes from a stenotic mitral valve; a click falls in systole."),
      ("S4 gallop", "S4 is a dull, low-pitched sound just before S1 with the cadence Ten-nes-SEE, not a sharp high-pitched click.")]),

    ("20", AT_PULM + "What does the second heart sound show?", "Physiologic splitting of S2", SOUNDS_IO, 35,
     "Physiologic splitting of S2",
     "Correct. A2 and P2 separate on inspiration and fuse on expiration, so the split comes and goes with breathing and is normal.",
     [("Pathologic splitting of S2", "Pathologic splitting stays audible during expiration and suggests heart disease; this split comes and goes with breathing."),
      ("An unsplit S2", "An unsplit S2 is a single sound, but here the aortic and pulmonic components are audibly separate on inspiration."),
      ("An S3 gallop", "S3 is a separate low-pitched sound after S2 with the cadence Ken-TUC-ky; both parts here are the closing sounds of S2.")]),

    ("19", AT_PULM + "What does the second heart sound show?", "Pathologic splitting of S2", SOUNDS_IO, 35,
     "Pathologic splitting of S2",
     "Correct. Splitting that stays audible during expiration is pathologic and suggests heart disease; physiologic splitting fuses on expiration.",
     [("Physiologic splitting of S2", "Physiologic splitting appears on inspiration and fuses on expiration; this split persists through both phases of breathing."),
      ("An unsplit S2", "An unsplit S2 is a single sound, but here the aortic and pulmonic components stay audibly separate."),
      ("An S4 gallop", "S4 sits just before S1 with the cadence Ten-nes-SEE; the two-part sound here is S2 itself.")]),

    ("07", AT_APEX + "What is this murmur?", "Mid-systolic murmur", MURMUR_IO, 51,
     "Mid-systolic murmur",
     "Correct. It sits in the middle of systole, between S1 and S2, with a gap on either side; aortic stenosis, pulmonic stenosis and hypertrophic cardiomyopathy are pathologic causes.",
     [("Holosystolic murmur", "A holosystolic (pansystolic) murmur begins immediately with S1 and continues through to S2, leaving no gap."),
      ("Late systolic murmur", "A late systolic murmur starts only near the end of systole, as after the click of mitral valve prolapse."),
      ("Early diastolic murmur", "Diastolic murmurs fall between S2 and S1; this murmur sits between S1 and S2, so it is systolic.")]),

    ("08", AT_APEX + "What is this murmur?", "Late systolic murmur", MURMUR_IO, 39,
     "Late systolic murmur",
     "Correct. It starts late in systole and builds up to S2; in mitral valve prolapse it follows a mid to late systolic click and crescendos up to S2.",
     [("Mid-systolic murmur", "A midsystolic murmur is centered in systole and fades before S2 (crescendo-decrescendo); this one builds toward S2."),
      ("Holosystolic murmur", "A holosystolic murmur begins immediately with S1; this murmur leaves a silent gap after S1."),
      ("Mid-diastolic murmur", "A mid-diastolic murmur falls between S2 and S1 and is a low-pitched rumble; this one falls in systole.")]),

    ("09", AT_APEX + "What is this murmur?", "Holosystolic murmur", MURMUR_IO, 72,
     "Holosystolic murmur",
     "Correct. It begins immediately with S1 and continues to S2, as in mitral regurgitation at the apex and tricuspid regurgitation at the lower left sternal border.",
     [("Mid-systolic murmur", "A midsystolic murmur rises and falls with a gap after S1 and before S2, whereas this murmur fills all of systole."),
      ("Late systolic murmur", "A late systolic murmur leaves early systole silent and starts only near the end; this murmur begins right at S1."),
      ("Early diastolic murmur", "An early diastolic murmur begins right after S2 and is a high-pitched blowing sound; this one fills systole.")]),

    ("10", AT_APEX_LLD + "What is this murmur?", "Mitral valve prolapse", MURMUR_IO, 39,
     P_CLICK,
     "Correct. Mitral valve prolapse gives a mid to late systolic click followed by a late systolic murmur of mitral regurgitation that crescendos up to S2.",
     [(P_SNAP, "That is the mitral stenosis pattern, an opening snap and then a low-pitched diastolic rumble; here both sounds fall in systole."),
      (P_S3, "That pattern has the S3 after S2 in diastole (Ken-TUC-ky); here the extra sound is a sharp click in systole."),
      (P_EJ, "An ejection sound comes right after S1 and goes with stenosis of the aortic or pulmonic valve; a prolapse click comes later, in mid to late systole.")]),

    ("11", AT_APEX_LLD + "What is this murmur?", "S4 with a mid-systolic murmur", MURMUR_IO, 42,
     P_S4,
     "Correct. The dull S4 just before S1 (Ten-nes-SEE) is followed by a murmur in the middle of systole; aortic stenosis and hypertrophic cardiomyopathy are causes of both.",
     [(P_S3, "The S3 follows S2 in diastole (Ken-TUC-ky); here the extra sound comes just before S1, and the murmur is midsystolic rather than holosystolic."),
      (P_CLICK, "A prolapse click is a sharp, high-pitched sound in mid to late systole; the extra sound here is a dull, low-pitched one just before S1."),
      (P_SNAP, "An opening snap is a sharp, very early diastolic sound of mitral stenosis; here the extra sound comes before S1 and the murmur is systolic.")]),

    ("12", AT_APEX_LLD + "What is this murmur?", "S3 with a holosystolic murmur", MURMUR_IO, 40,
     P_S3,
     "Correct. An S3 after S2 (Ken-TUC-ky) with a murmur that fills systole fits volume overload from mitral regurgitation, which causes both.",
     [(P_S4, "S4 comes just before S1 (Ten-nes-SEE), and a midsystolic murmur leaves gaps at both ends; here the murmur runs from S1 to S2."),
      (P_CLICK, "A prolapse click is a sharp, high-pitched sound in mid to late systole; the extra sound here is a low-pitched one in diastole."),
      (P_EJ, "An ejection sound is a sharp systolic sound right after S1 with a midsystolic murmur; here the extra sound is a low-pitched one after S2.")]),

    ("13", AT_APEX_LLD + "What is this murmur?", "Mitral stenosis", MURMUR_IO, 44,
     P_SNAP,
     "Correct. The snap of a stenotic mitral valve opening is followed by the low-pitched mid to late diastolic murmur of mitral stenosis, heard with the bell at the apex.",
     [(P_S3, "That pattern of volume overload has a low-pitched S3 and a murmur filling systole; the sharp sound here comes very early in diastole and the murmur is diastolic."),
      (P_CLICK, "A prolapse click and its murmur both fall in systole; here the sharp sound and the murmur come after S2, in diastole."),
      (P_S4, "S4 comes just before S1 and is followed by a systolic murmur; here the sharp sound follows S2 and the murmur is diastolic.")]),

    ("23", AT_PULM + "What is this murmur?", "Pulmonic stenosis", MURMUR_IO, 38,
     P_EJ,
     "Correct. An ejection sound comes right after S1 and is high pitched; with a midsystolic murmur at the pulmonic area it fits pulmonic stenosis, which causes both.",
     [(P_S3, "The S3 is a low-pitched sound after S2 and goes with a murmur filling systole; the sharp sound here comes right after S1."),
      (P_CLICK, "A prolapse click comes in mid to late systole, and its murmur builds up to S2; an ejection sound comes right after S1."),
      (P_SNAP, "An opening snap falls in diastole with a diastolic murmur; here the sharp sound and the murmur are both systolic.")]),

    ("15", AT_AORTIC + "What is this murmur?", "Aortic stenosis", MURMUR_IO, 67,
     "Aortic stenosis",
     "Correct. Aortic stenosis is a harsh midsystolic crescendo-decrescendo murmur at the aortic area that often radiates to the carotids.",
     [("Aortic regurgitation", "Aortic regurgitation is an early diastolic, high-pitched blowing decrescendo murmur; the murmur here is systolic."),
      ("Mitral regurgitation", "Mitral regurgitation is pansystolic and loudest at the apex, radiating to the left axilla; this murmur is centered in systole at the aortic area."),
      ("Pulmonic regurgitation", "Pulmonic regurgitation is an early diastolic murmur loudest at the pulmonic area; this murmur is systolic, at the aortic area.")]),

    ("16", AT_AORTIC + "What is this murmur?", "Aortic regurgitation", MURMUR_IO, 77,
     "Aortic regurgitation",
     "Correct. It is an early diastolic, high-pitched blowing decrescendo murmur at the aortic area, best heard with the patient sitting forward after exhaling.",
     [("Aortic stenosis", "Aortic stenosis is a harsh midsystolic crescendo-decrescendo murmur; this murmur falls after S2, in diastole."),
      ("Mitral stenosis", "Mitral stenosis is a low-pitched mid to late diastolic rumble at the apex heard with the bell; this murmur is high pitched and starts right after S2."),
      ("Tricuspid regurgitation", "Tricuspid regurgitation is pansystolic and loudest at the lower left sternal border; this murmur falls in diastole.")]),

    ("21", AT_PULM + "What is this murmur?", "Ejection murmur, physiologic split", MURMUR_IO, 35,
     C_MP,
     "Correct. The murmur sits in the middle of systole and the split of S2 comes and goes with breathing, which is physiologic.",
     [(C_MX, "The murmur is right, but pathologic splitting stays audible during expiration; here the split fuses on expiration."),
      (C_HP, "The splitting is right, but a holosystolic murmur begins immediately with S1 and continues to S2, leaving no gap."),
      (C_HX, "Both parts are wrong: a holosystolic murmur leaves no gap between S1 and S2, and a pathologic split stays audible on expiration.")]),

    ("22", AT_PULM + "What is this murmur?", "Ejection murmur, pathologic split", MURMUR_IO, 35,
     C_MX,
     "Correct. The murmur sits in the middle of systole and the split of S2 stays audible during expiration, which is pathologic and suggests heart disease.",
     [(C_MP, "The murmur is right, but physiologic splitting fuses on expiration; here the split persists through breathing."),
      (C_HX, "The splitting is right, but a holosystolic murmur begins immediately with S1 and continues to S2, leaving no gap."),
      (C_HP, "Both parts are wrong: a holosystolic murmur leaves no gap between S1 and S2, and a physiologic split fuses on expiration.")]),
]

assert len(POOL) == 18
