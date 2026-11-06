# -*- coding: utf-8 -*-
"""Lecture 40 scope -- Obstructive Sleep Apnea and Obesity Hypoventilation Syndrome (Shah), CMS I Exam 7
(Respiratory Block Exam II, Monday 2026-11-16, Lectures 39-45).

Read by cms_e7_partition.py (guards) and imported by every Lecture 40 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Chand Shah, MPAS, PA-C, Assistant Professor -- title slide. calendar-data.js lists "CMS I - LECTURE
#40 - Obstructive Sleep Apnea and Obesity Hypoventilation Syndrome - Professor Shah", Monday 2026-11-02,
11 AM-12 PM (1 hour). No conflict. Deck file "CMS I Obstructive Sleep Apnea & Obesity Hypoventilation Syndrome -
Shah Fallsv.pptx", 38 slides.

PHASE 1 (2026-11-02) was SLIDES ONLY. PHASE 2 (2026-11-06): the recording is folded in below; it sets emphasis, the
minutes weighting and scope only (slides-only grounding: time spoken never adds off-deck content).

RECORDING (2026-11-02): one Notability clip, 57:08, recordings/cms-l40-osa-ohs-shah-2026-11-02.m4a; it opens on the tail
of the title/objectives slide and runs to the exit ticket. Transcript: faster-whisper,
cms-l40-osa-ohs-shah-2026-11-02.transcript.txt -- ONE machine transcription (Notability holds no ASR for this note:
dump_notability_asr.py finds the asset but "no plist"), so there is no second opinion; numbers below were checked
against the slides. Audio only (no screen), so slide positions are inferred from what she reads. Timestamps [m:ss].
DECK VS RECORDING: after slide 3 she taught an interactive case that is NOT in the inbox deck ([2:44]-[17:16]: a
55-year-old man whose wife reports snoring and stopped breathing; the class asks history questions; vitals BMI 36,
BP 167/96; a lettered answer "B" she reads out). Off-deck: never keyed, and its 13.5 minutes of history-taking Q&A are
left out of the minutes (its 1-minute wrap-up of the key findings counts toward risk and presentation). The s36
"Case Studies" were skipped ("I'll post them and you guys can work through them" [55:28]). Every other slide 3-35 was
taught in deck order; s14 (device photographs) was shown [38:00].

WHAT SHE STRESSED:
  OSA diagnosis: "Diagnosis is confirmed in two different ways ... 15 or more ... or if there's five of those ... and
      there's symptoms" [29:13-29:42]; again "I wanna make it as simple as possible, five or more plus a symptom or
      15 or more" [30:32] (s9). "The gold standard is a sleep study" [24:01] (s8). Home kits: "not considered like the
      best, but it is convenient" [27:34]; "it only really checks for obstructive sleep apnea" [28:29]; not for
      cardiopulmonary or neuromuscular patients ("We don't want to use home kits for those patients" [28:17]) (s8);
      and for central apnea "that at home stuff is not effective" [46:35] (s26).
  Patient education: "really patient education is like the most important thing that we can do for this" [43:01];
      CPAP: "people hate it ... a lot of it comes down to patient education" [33:11-33:31]; listen to family members,
      who report the witnessed apneas the patient cannot [22:17] (s7).
  OSA management order: severe OSA -> the oral appliance will not help, "They actually need the full on CPAP"
      [36:04-36:17] (s12); devices are stepwise and patient-specific [36:17, 37:16-37:34]; tracheostomy "is a cure"
      but invasive, never a first step [36:53-37:16] (s13).
  OSA epidemiology: postmenopausal > premenopausal, "that's an important thing because when you look at someone's
      age, especially a female patient, the age will help you a lot" [17:31-17:45] (s5).
  Untreated OSA: she read the s18 multipliers (2.5 x driving accidents; 3 x hypertension; "three to six times
      higher" sudden cardiac death at night) [41:18-42:09]; GERD and immunity improve with CPAP [42:16, 44:08] (s19, s22).
  Central sleep apnea: "i really want everyone to understand these risk factors are very different ... because the
      treatment for central sleep apnea is really taking care of their risk factors" [45:37-46:01] (s24, s26); CPAP
      first, ASV only if CPAP fails, never with poor left ventricular function, "which is why we always start with the
      c-pap first" [47:42-48:57] (s26).
  OHS: "diagnosis of exclusion is kind of the big thing" [49:03, 51:15, 52:06] (s32); "the gender does not matter here"
      [49:47] (s29); first line weight loss + BiPAP or CPAP, "First line, first line, first line" [53:08-53:18] (s33);
      bariatric surgery helps the weight "It will not cure it" [53:36-53:45] (s33); cardiovascular disease is the
      leading cause of death [54:32-54:40] (s35).

WHAT SHE SAID IS NOT THE FOCUS: nothing was said to be off the exam. The s36 case studies are for self-study.

WHERE SHE AND THE SLIDES DIFFER (slides win; none is a correction of a slide):
  Labs: she adds CBC, CMP and liver tests for the OSA workup [23:37-23:45]; s8 lists only TSH. Never keyed.
  s13 "Maxillomandibular advancements" (surgery): she calls it "maximum mandibular advanced devices that the dentist
      will create" [36:47]. Slide keyed (a surgical option); never ask it as a dental device.
  s22 elderly mortality is lower "because the patients will compensate": she says the elderly "not die as fast because
      the CPAP really helps in the compensation" [44:25]. Slide keyed.
  s30 sleep-hypoventilation subgroup has "Less witnessed apneas": she says they "could also have witnessed apneic
      episodes" [50:53]. Slide keyed.
  Home-kit cost ($500-600) and insurance [26:22-27:39], her own sleep study, ring device and AHI of 4 [20:35-22:31,
      26:59-27:35, 29:55-30:30]: personal asides, never keyed.

MINUTES (clip timestamps, by topic; slide positions inferred): OSA management 8.0 (s11-s15 [31:40-39:40]); OSA
diagnosis 7.2 (s8-s10 [23:17-31:40] minus 1.2 of her own sleep-study stories); OSA risk and presentation 5.75 (s5-s7
[17:16-23:17] minus 1.25 of her personal story, plus the 1.0-minute case wrap-up); central sleep apnea 4.1 (s23-s26
[44:32-48:57] minus 0.3); OHS diagnosis 4.0 (s27-s32 [48:57-52:58]); untreated OSA 3.3 (s18-s22 [41:12-44:32]); OHS
management and prognosis 2.5 (s33-s35 [52:58-55:28]); sleep-disordered breathing 2.25 (s2-s3 [0:00-2:44]);
STOP-Bang 1.5 (s16-s17 [39:40-41:12]). Left out: the off-deck case Q&A 13.5, the exit ticket and dog photo 1.7.

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 19, "Obstructive Sleep Apnea and Obesity
Hypoventilation Syndrome"), the leading letters dropped and the sub-list lettering kept (the syllabus prints a
stray empty "a." before the disease list; it is left out). The deck's objectives slide (s2) adds three of its
own ("Explain why obesity hypoventilation syndrome is a diagnosis of exclusion", "Discuss central sleep apnea as
a differential diagnosis for obstructive sleep apnea", "Discuss STOP-Bang questionnaire as a screening tool");
they sit inside the syllabus objectives and the guide answers them there.

THE STOP-BANG PICTURE (s17) is the whole questionnaire as an image: S snore loudly; T tired, fatigued or sleepy
in the daytime; O observed to stop breathing or choking/gasping; P being treated for high blood pressure;
B body mass index more than 35 kg/m2; A age older than 50; N neck size (shirt collar) 16 inches / 40 cm or
larger; G gender male. General population: low risk yes to 0-2, intermediate 3-4, high 5-8; OR yes to 2 or more
of the 4 STOP questions + male gender, + body mass index > 35, or + neck circumference 16 inches / 40 cm.
STOP-Bang totals are keyed from a vignette (Jaxon: the real exam asks "what is the score from the vignette").

SLIDE CONFLICTS (never keyed one way or the other; the guide notes each):
  Neck size: s6 and s7 give the OSA risk-factor neck circumference by sex (>= 17 in men, 16 in women; s7 writes
      ">17in"); the STOP-Bang item (s17) is 16 inches / 40 cm for anyone. A neck-size item says which tool it
      uses; a STOP-Bang item scores the neck at 16 inches regardless of sex.
  Body mass index: STOP-Bang counts > 35 kg/m2 (s17); obesity for obesity hypoventilation syndrome is > 30 (s30,
      s32). Each is keyed only inside its own tool.
  Sex: s6 "Male > women" (OSA); s5 post-menopausal women have more sleep-disordered breathing than premenopausal;
      s29 "Male gender is not a risk factor" (OHS); s30 the sleep-hypoventilation subgroup is "Older females".
  "Gold standard": s8 calls BOTH the split-night and the all-night polysomnogram the gold standard; s32 calls
      polysomnography with continuous nocturnal carbon dioxide monitoring the gold standard for obesity
      hypoventilation syndrome. Never ask split-night versus all-night as "the" gold standard.
  s21 lists both "Increased sympathetic tone" and "Bradycardia" as cardiovascular effects: both are keyable as
      listed; never ask for the heart-rate direction alone.

SPEAKER NOTES ARE NOT SLIDE CONTENT (Jaxon, 2026-10-15): the s9 note (AHI 5 mild / 15 moderate / 30 severe), the
s10 note (central sleep apnea detail), the s12 and s14 notes (CPAP versus BiPAP), the s6 note (micrognathia and
retrognathia definitions) are never used. OSA SEVERITY CATEGORIES BY INDEX ARE NOT ON A SLIDE: never key
mild/moderate/severe from an apnea-hypopnea index number.

EXCLUDED_SLIDES (never cited):
  1, 2            title, objectives
  4, 23, 27       section title slides
  14              three photographs of positive airway pressure devices, no text
  36              "Case Studies" title, no content
  37, 38          resources, questions
"""

DECK = "CMS I Obstructive Sleep Apnea & Obesity Hypoventilation Syndrome - Shah Fallsv.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
CS = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential "
        "diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, "
        "including applicable rehabilitative and palliative care), appropriate referrals, patient education, and "
        "prognosis for obstructive sleep apnea and obesity hypoventilation syndrome: a. Obstructive sleep apnea "
        "b. Central sleep apnea c. Obesity hypoventilation syndrome (also known as Pickwickian Syndrome)")
IO_SCREEN = "Discuss screening tools for obstructive sleep apnea"
IO_COMP = ("Discuss the following complications of untreated obstructive sleep apnea and comorbidities of "
           "obstructive sleep apnea, including: a. Atrial fibrillation and cardiac arrythmias b. Pulmonary "
           "hypertension and right heart failure c. Heart failure d. Systemic hypertension e. Coronary artery "
           "disease f. Type 2 diabetes mellitus and metabolic syndrome g. Nonalcoholic fatty liver disease")
IO_POP = ("Identify medical care strategies for obstructive sleep apnea and obesity hypoventilation syndrome for "
          "the following populations. 1. adult 2. elderly")
IOS = [IO_A, IO_SCREEN, IO_COMP, IO_POP]

EXCLUDED_SLIDES = {1, 2, 4, 14, 23, 27, 36, 37, 38}

SCOPE_BANNED = [
    r"\b30 (?:or more )?(?:events|per hour)|severe (?:obstructive sleep apnea|OSA) (?:is|=|means) ",
    r"Lecturio|UpToDate|Pasha|Guyton",
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "facial plethora": "swelling",        # s31: facial plethora (facial swelling, puffiness)
    "cheyne-stokes": "alternating",       # s24: hyperventilation alternating with apnea
}

# Every form carries at least one STOP-Bang total worked from the stem (s17).
REQUIRED = [
    ("STOP-Bang total", r"STOP-Bang", r".", 1),
]
# The objective set has 9 STOP-Bang items; spread them (a first partition put 1 in Set 1 and 6 in Set 2).
REQUIRED_IO = [
    ("STOP-Bang item", r"STOP-Bang", r".", 3),
    # Recording [29:13-30:41]: the two diagnostic routes, said twice ("as simple as possible").
    ("OSA diagnostic criteria", r"events per hour", r".", 1),
    # Recording [45:37-46:01]: "i really want everyone to understand these risk factors".
    ("CSA risk factor", r"risk factor for central sleep apnea", r".", 1),
]
REQUIRED_VIG = REQUIRED + [
    ("OSA diagnostic criteria", r"events per hour", r".", 1),
]

# Minutes spoken per pool topic (recording 2026-11-02; see MINUTES above). Each form aims for this share of 30.
TOPIC_MINUTES = {
    "Sleep-disordered breathing": 2.25,
    "Obstructive sleep apnea: risk and presentation": 5.75,
    "Obstructive sleep apnea: diagnosis": 7.2,
    "Obstructive sleep apnea: management": 8.0,
    "STOP-Bang screening": 1.5,
    "Untreated obstructive sleep apnea": 3.3,
    "Central sleep apnea": 4.1,
    "Obesity hypoventilation syndrome: diagnosis": 4.0,
    "Obesity hypoventilation syndrome: management and prognosis": 2.5,
}
