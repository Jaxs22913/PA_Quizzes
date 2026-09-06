# -*- coding: utf-8 -*-
"""Neuro-Ophthalmology (Lecture 11) -- Updated ophthalmology masters.

Eight named conditions, but the lecture is really about PATHWAYS: which pupil
finding localises where, and which cranial nerve produces which deviation. The
stems are built so the localisation is derivable rather than recalled.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsophtho_style import Q

D = "11. Neuro-Ophthalmology"
IO = ("a — Neuro-ophthalmological disorders: etiologies, clinical manifestations, differential "
      "diagnosis, diagnostic testing, management, referrals, patient education, prognosis")

QUESTIONS = [

Q("Relative afferent pupillary defect", IO,
  "A 34-year-old woman has reduced vision in the left eye. On the swinging flashlight test, both "
  "pupils constrict when the light is shone in the right eye, but both DILATE when the light is "
  "swung to the left eye. What does this indicate?",
  [["A relative afferent pupillary defect on the left",
    "Correct. The left optic nerve conducts less well, so swinging to it is a net reduction in "
    "light input."],
   ["An efferent defect on the left", "An efferent lesion affects only the pupil on the damaged "
                                      "side; here both pupils behave symmetrically."],
   ["Horner syndrome on the left", "That gives a small pupil with ptosis, and the light reaction is "
                                   "preserved."],
   ["An Adie tonic pupil on the left", "That is a large pupil with a slow, tonic near response."],
   ["Physiological anisocoria", "A benign difference in size with normal reactions."]],
  "diagnosis", D, 25),

Q("Relative afferent pupillary defect", IO,
  "A 41-year-old man is found to have a relative afferent pupillary defect. Which of the following "
  "would explain it?",
  [["Optic neuritis", "Correct — a defect of the afferent pathway, which is the optic nerve."],
   ["A dense cataract", "Media opacity reduces light but does not usually produce a true afferent "
                        "defect."],
   ["Horner syndrome", "A sympathetic efferent problem affecting pupil size, not the light input."],
   ["Third nerve palsy", "An efferent problem; the pupil on that side may be fixed but the "
                         "swinging test is not affected this way."],
   ["Refractive error", "Blurred focus does not alter afferent conduction."]],
  "two-step", D, 26),

Q("Horner syndrome", IO,
  "A 57-year-old smoker has a droopy right upper lid and a small right pupil that reacts to light. "
  "The right side of his face is dry. He has had a cough for three months. What is the most likely "
  "diagnosis, and what must be excluded?",
  [["Horner syndrome, and an apical lung tumour must be excluded",
    "Correct. Ptosis, miosis and anhidrosis; a Pancoast tumour is the concern with this history."],
   ["Third nerve palsy, and an aneurysm must be excluded",
    "That gives a DILATED pupil with the eye down and out, not a small pupil."],
   ["Adie tonic pupil, and syphilis must be excluded",
    "The tonic pupil is large and there is no ptosis."],
   ["Argyll Robertson pupil, and diabetes must be excluded",
    "That is bilateral, small and irregular, with light-near dissociation."],
   ["Myasthenia gravis, and a thymoma must be excluded",
    "Myasthenic ptosis is fatigable and the pupil is spared."]],
  "diagnosis", D, 28),

Q("Horner syndrome", IO,
  "A 44-year-old woman develops sudden ptosis and miosis on the left with neck pain after a "
  "whiplash injury. What must be excluded urgently?",
  [["Carotid artery dissection", "Correct. Painful Horner syndrome of sudden onset is a "
                                 "dissection until proven otherwise."],
   ["Apical lung tumour", "A cause of Horner syndrome, but not the one signalled by acute neck "
                          "pain after trauma."],
   ["Multiple sclerosis", "Causes optic neuritis and internuclear ophthalmoplegia rather than "
                          "Horner syndrome."],
   ["Giant cell arteritis", "Causes ischaemic optic neuropathy in older patients."],
   ["Diabetic third nerve palsy", "Affects the third nerve and spares the pupil."]],
  "two-step", D, 30),

Q("Argyll Robertson pupil", IO,
  "A 52-year-old man has small, irregular pupils bilaterally. They do NOT react to light, but "
  "constrict briskly on near effort. What is the most likely diagnosis?",
  [["Argyll Robertson pupil", "Correct — light-near dissociation with small irregular pupils; "
                              "'accommodates but does not react'."],
   ["Adie tonic pupil", "A LARGE pupil, usually unilateral, with a slow tonic near response."],
   ["Horner syndrome", "A small pupil, but it reacts to light and is accompanied by ptosis."],
   ["Third nerve palsy", "A large fixed pupil with ptosis and an eye that is down and out."],
   ["Physiological anisocoria", "Pupils differ in size but react normally to light."]],
  "diagnosis", D, 31),

Q("Argyll Robertson pupil", IO,
  "Which infection is classically associated with light-near dissociation and small irregular "
  "pupils?",
  [["Syphilis", "Correct — neurosyphilis is the classic association."],
   ["Tuberculosis", "Not the association for this pupil finding."],
   ["Lyme disease", "Causes facial palsy among other neurological features, not this pupil."],
   ["Herpes zoster", "Causes keratitis and post-herpetic neuralgia."],
   ["Toxoplasmosis", "Causes chorioretinitis rather than a pupil abnormality."]],
  "two-step", D, 33),

Q("Adie tonic pupil", IO,
  "A 27-year-old woman has noticed one pupil is larger than the other. The larger pupil reacts "
  "poorly to light but constricts slowly on sustained near effort, then redilates slowly. Deep "
  "tendon reflexes are diminished. What is the most likely diagnosis?",
  [["Adie tonic pupil", "Correct. A large tonic pupil with a slow near response; diminished "
                        "reflexes make it Holmes-Adie syndrome."],
   ["Argyll Robertson pupil", "Small, irregular and bilateral."],
   ["Third nerve palsy", "Would carry ptosis and an eye deviated down and out."],
   ["Horner syndrome", "A small pupil with ptosis and anhidrosis."],
   ["Pharmacological mydriasis", "A fixed dilated pupil with no near response at all."]],
  "diagnosis", D, 34),

Q("Cranial nerve III palsy", IO,
  "A 62-year-old man has sudden ptosis of the right lid. The right eye is deviated DOWN and OUT, "
  "and the right pupil is dilated and unreactive. He has a severe headache. What is the most "
  "appropriate next step?",
  [["Urgent neuroimaging for a posterior communicating artery aneurysm",
    "Correct. A pupil-INVOLVING third nerve palsy with headache is an aneurysm until proven "
    "otherwise."],
   ["Reassure and review in one month", "This is a neurosurgical emergency."],
   ["Prescribe an eye patch and analgesia", "Symptomatic care does not address an aneurysm."],
   ["Check blood glucose and observe", "Pupil-SPARING palsy suggests a microvascular cause; here "
                                       "the pupil is involved."],
   ["Start topical antiglaucoma drops", "The pressure is not the issue."]],
  "treatment", D, 40),

Q("Cranial nerve III palsy", IO,
  "A 66-year-old man with diabetes has ptosis and an eye deviated down and out, but the pupil is "
  "normal in size and reactive. What does the pupil finding suggest about the cause?",
  [["A microvascular ischaemic cause", "Correct. The pupillary fibres run peripherally and are "
                                       "spared by ischaemia but compressed by an aneurysm."],
   ["A compressive aneurysm", "Compression involves the pupil, which is spared here."],
   ["A cavernous sinus lesion", "Would usually involve other nerves as well."],
   ["Myasthenia gravis", "Causes fatigable ptosis with normal pupils but no fixed deviation."],
   ["Thyroid eye disease", "Causes restrictive myopathy and proptosis rather than a third nerve "
                           "pattern."]],
  "two-step", D, 41),

Q("Cranial nerve IV palsy", IO,
  "A 38-year-old man has vertical double vision that is worse when he looks DOWN and tilts his head "
  "to one side to compensate. He fell and struck his head last week. Which nerve is affected?",
  [["The fourth cranial nerve", "Correct. Superior oblique palsy gives vertical diplopia worse on "
                                "downgaze, with a compensatory head tilt."],
   ["The third cranial nerve", "Gives ptosis with the eye down and out."],
   ["The sixth cranial nerve", "Gives horizontal diplopia worse on lateral gaze."],
   ["The second cranial nerve", "Carries vision, not eye movement."],
   ["The seventh cranial nerve", "Supplies facial movement and eyelid closure."]],
  "diagnosis", D, 42),

Q("Cranial nerve VI palsy", IO,
  "A 45-year-old woman has horizontal double vision that is worse when looking to the left, with "
  "the left eye failing to abduct. Which muscle is weak?",
  [["The lateral rectus", "Correct — supplied by the sixth cranial nerve, which abducts the eye."],
   ["The medial rectus", "Adducts the eye and is supplied by the third nerve."],
   ["The superior oblique", "Depresses the adducted eye and is supplied by the fourth nerve."],
   ["The inferior rectus", "Depresses the eye and is supplied by the third nerve."],
   ["The levator palpebrae", "Elevates the lid rather than moving the globe."]],
  "diagnosis", D, 44),

Q("Cranial nerve VI palsy", IO,
  "A 29-year-old woman with headaches and papilledema is found to have a sixth nerve palsy. Why is "
  "this described as a false localising sign?",
  [["Its long intracranial course makes it vulnerable to raised pressure anywhere",
    "Correct — the palsy does not indicate where the lesion is."],
   ["It always indicates a brainstem lesion", "That would make it a true localising sign."],
   ["It only occurs with orbital disease", "The palsy here reflects intracranial pressure."],
   ["It is always bilateral", "It may be unilateral or bilateral."],
   ["It resolves within hours", "Resolution follows treatment of the pressure, not hours."]],
  "two-step", D, 46),

Q("Nystagmus", IO,
  "A 3-week-old infant is noted to have rhythmic to-and-fro eye movements present since birth. "
  "What is the significance of nystagmus at this age?",
  [["It warrants evaluation for a cause of poor vision",
    "Correct. Congenital nystagmus often reflects an underlying visual deficit."],
   ["It is a normal finding in newborns and needs no action",
    "Persistent nystagmus is not a normal finding."],
   ["It always indicates a brain tumour", "A cause to consider, but not the general implication."],
   ["It confirms congenital cataract", "One possible cause among several."],
   ["It resolves without evaluation by six months", "Evaluation is indicated rather than "
                                                    "watchful waiting."]],
  "two-step", D, 4),

Q("Visual fields", IO,
  "A 51-year-old woman has bumped into objects on both sides for months. Formal fields show loss of "
  "BOTH temporal hemifields. Where is the lesion?",
  [["At the optic chiasm", "Correct. Bitemporal (heteronymous) hemianopsia is the chiasmal "
                           "pattern on the visual pathway diagram."],
   ["In one optic nerve", "That produces monocular loss."],
   ["In the optic tract", "That produces a homonymous defect on one side."],
   ["In the occipital cortex", "That produces a homonymous defect, often with macular sparing."],
   ["In the retina of one eye", "That produces a monocular defect."]],
  "diagnosis", D, 25),

Q("Visual fields", IO,
  "A 70-year-old man has a right homonymous hemianopia with macular sparing after a stroke. Where "
  "is the lesion?",
  [["The left occipital cortex", "Correct. Macular sparing is characteristic of an occipital "
                                 "lesion, and the defect is contralateral."],
   ["The right occipital cortex", "That would produce a LEFT-sided field defect."],
   ["The optic chiasm", "That produces a bitemporal rather than homonymous defect."],
   ["The right optic nerve", "That produces monocular loss on the right."],
   ["The left optic nerve", "That produces monocular loss on the left."]],
  "two-step", D, 25),

Q("Visual fields", IO,
  "A field defect is found to be MONOCULAR. Where must the lesion be?",
  [["Anterior to the chiasm", "Correct — a monocular defect localises pre-chiasmal."],
   ["At the chiasm", "A chiasmal lesion affects both eyes."],
   ["Posterior to the chiasm", "Post-chiasmal lesions produce homonymous, binocular defects."],
   ["In the occipital cortex", "That is post-chiasmal and produces a binocular defect."],
   ["In the optic radiation", "Also post-chiasmal and binocular."]],
  "two-step", D, 25),
]
