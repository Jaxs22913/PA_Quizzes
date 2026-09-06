# -*- coding: utf-8 -*-
"""Acute Vision Loss (Lecture 12) -- second pool.

Second angles on the vascular occlusions and the glaucomas, plus the systemic
workups each one triggers. Several stems here are deliberately SHORT, because
three of the six exemplars are and a bank of uniformly long stems reads wrong.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmsophtho_style import Q

D = "12. Acute Vision Loss"
IO = ("a — Acute vision loss: etiologies, epidemiology, risk factors, clinical manifestations, "
      "differential diagnosis, diagnostic testing, management, referrals, patient education, "
      "prognosis")

QUESTIONS = [

Q("Central retinal artery occlusion", IO,
  "A 70-year-old man has sudden painless monocular vision loss. Which systemic workup does the "
  "diagnosis trigger?",
  [["A stroke workup, including carotid imaging and cardiac assessment",
    "Correct — it is a stroke of the eye and carries the same embolic sources."],
   ["Allergy testing", "No allergic mechanism is involved."],
   ["Thyroid function testing alone", "Not the workup this diagnosis triggers."],
   ["A dermatological review", "Unrelated to retinal arterial occlusion."],
   ["Pulmonary function testing", "Not indicated by this presentation."]],
  "two-step", D, 40),

Q("Central retinal artery occlusion", IO,
  "A 76-year-old woman has a central retinal artery occlusion. Which additional feature would make "
  "you suspect giant cell arteritis as the cause?",
  [["Jaw claudication and scalp tenderness",
    "Correct — the arteritic cause changes management to immediate high-dose steroids."],
   ["A history of migraine", "Not a feature pointing to arteritis."],
   ["Recent contact lens use", "Relevant to corneal ulcer, not arterial occlusion."],
   ["Bilateral itching", "An allergic symptom."],
   ["Photophobia alone", "Non-specific and not the arteritic signal."]],
  "two-step", D, 49),

Q("Branch retinal artery occlusion", IO,
  "A 66-year-old man has sudden painless loss of the lower half of his visual field in one eye. "
  "Fundoscopy shows a wedge of pale retina above the macula. What is the most likely diagnosis?",
  [["Branch retinal artery occlusion", "Correct. A pale wedge in one artery's territory, producing "
                                       "loss of the opposite field."],
   ["Central retinal artery occlusion", "Would affect the whole retina with a cherry-red spot."],
   ["Branch retinal vein occlusion", "Produces haemorrhage in the territory rather than pallor."],
   ["Retinal detachment", "Elevated retina preceded by flashes and floaters."],
   ["Non-arteritic ischaemic optic neuropathy", "Causes altitudinal loss with disc swelling rather "
                                                "than a retinal wedge."]],
  "diagnosis", D, 41),

Q("Central retinal vein occlusion", IO,
  "A 69-year-old man with a central retinal vein occlusion is being counselled. Which complication "
  "is he monitored for?",
  [["Neovascular glaucoma", "Correct — ischaemia drives new vessel growth at the iris and angle."],
   ["Cataract within weeks", "Not the complication that drives monitoring."],
   ["Corneal ulceration", "Unrelated to venous occlusion."],
   ["Optic neuritis", "An inflammatory demyelinating condition."],
   ["Retinal detachment from a break", "Not the mechanism following venous occlusion."]],
  "two-step", D, 33),

Q("Central retinal vein occlusion", IO,
  "A 62-year-old woman has a central retinal vein occlusion. Which systemic conditions should be "
  "sought?",
  [["Hypertension, diabetes and hyperviscosity states",
    "Correct — the venous side reflects systemic vascular and rheological disease."],
   ["Asthma and eczema", "Atopic conditions, unrelated to venous occlusion."],
   ["Inflammatory bowel disease alone", "Associated with uveitis rather than venous occlusion."],
   ["Osteoarthritis", "Not a vascular risk factor."],
   ["Migraine alone", "Not the systemic profile sought here."]],
  "two-step", D, 34),

Q("Acute angle-closure glaucoma", IO,
  "A 61-year-old woman has confirmed acute angle-closure glaucoma with an intraocular pressure of "
  "58 mm Hg. What is the definitive treatment once the pressure is controlled?",
  [["Laser peripheral iridotomy", "Correct — it creates an alternative route for aqueous and "
                                  "prevents recurrence."],
   ["Long-term topical beta blocker alone", "Controls pressure without addressing the blocked "
                                            "angle."],
   ["Cataract extraction as first line", "Lens extraction can help, but the named definitive step "
                                         "is iridotomy."],
   ["Topical pilocarpine indefinitely", "A temporising agent, not the definitive treatment."],
   ["Observation once the pressure falls", "Without iridotomy the attack recurs."]],
  "treatment", D, 17),

Q("Acute angle-closure glaucoma", IO,
  "A 63-year-old man is treated for acute angle-closure in one eye. What is done about the other "
  "eye?",
  [["Prophylactic iridotomy, as it is anatomically at risk",
    "Correct — the fellow eye shares the crowded anatomy."],
   ["Nothing, unless it becomes symptomatic", "Waiting for the second attack is avoidable."],
   ["Long-term topical steroids", "Steroids can raise pressure and do not open an angle."],
   ["Immediate cataract surgery", "Not the standard prophylactic step."],
   ["Patching for a week", "Has no effect on the angle."]],
  "two-step", D, 20),

Q("Chronic open-angle glaucoma", IO,
  "A 65-year-old woman is diagnosed with open-angle glaucoma. Why is she unlikely to have noticed "
  "anything?",
  [["Peripheral field loss is gradual and the other eye compensates",
    "Correct — which is why it is found on screening rather than by symptoms."],
   ["The disease causes no field loss at all", "It does; the loss is simply unnoticed."],
   ["Central vision fails first and she has adapted",
    "Central acuity is preserved until late."],
   ["It only affects colour vision early", "Colour is not the early casualty."],
   ["The pressure is normal in all cases", "Pressure is typically raised, though normal-tension "
                                           "disease exists."]],
  "two-step", D, 15),

Q("Chronic open-angle glaucoma", IO,
  "A 59-year-old man with open-angle glaucoma is not controlled on maximal topical therapy. What is "
  "the next step?",
  [["Laser trabeculoplasty", "Correct — the named escalation when medical therapy is refractory."],
   ["Increase the same drops to eight times daily", "Beyond maximal therapy by definition."],
   ["Switch to a topical steroid", "Steroids can raise pressure further."],
   ["Observation with annual review", "Uncontrolled pressure needs active escalation."],
   ["Immediate enucleation", "Grossly disproportionate."]],
  "treatment", D, 21),

Q("Optic neuritis", IO,
  "A 32-year-old woman with optic neuritis asks about her vision. What is the expected course?",
  [["Vision usually recovers substantially over weeks",
    "Correct, though colour desaturation may persist."],
   ["Vision is permanently lost in most patients", "Most recover substantially."],
   ["Vision recovers fully within 24 hours", "Recovery takes weeks."],
   ["The other eye always becomes involved within a month",
    "Fellow eye involvement is not inevitable."],
   ["The condition never recurs", "Recurrence is possible, particularly with demyelinating "
                                  "disease."]],
  "two-step", D, 24),

Q("Retinal detachment", IO,
  "A 55-year-old man reports flashes and floaters but no field loss. Examination shows a posterior "
  "vitreous detachment with no retinal break. What is the appropriate advice?",
  [["Return immediately if a curtain or shadow appears",
    "Correct — the warning is what converts this from observation to emergency."],
   ["No follow-up is needed", "A break can develop, and the warning symptoms matter."],
   ["Bed rest for two weeks", "Not the management."],
   ["Start topical steroids", "There is no inflammation."],
   ["Patch the eye", "Does not affect the vitreous or retina."]],
  "two-step", D, 27),

Q("Amaurosis fugax", IO,
  "A 72-year-old woman describes transient monocular vision loss lasting minutes. What is the "
  "underlying mechanism?",
  [["Transient retinal ischaemia, usually embolic",
    "Correct — most often from carotid atheroma."],
   ["Acute rise in intraocular pressure", "That is angle closure, which is painful and does not "
                                          "resolve spontaneously."],
   ["Optic nerve demyelination", "That produces sustained loss with pain on movement."],
   ["Retinal break with subretinal fluid", "That produces a progressive curtain, not a transient "
                                           "episode."],
   ["Vitreous haemorrhage", "Produces floaters and persistent blur rather than complete transient "
                            "loss."]],
  "two-step", D, 5),

Q("Papilledema", IO,
  "A 29-year-old woman with papilledema has a lumbar puncture. What finding is expected?",
  [["A raised opening pressure with normal constituents",
    "Correct — that is the pattern in idiopathic intracranial hypertension."],
   ["A raised white cell count", "That would indicate infection or inflammation."],
   ["A low opening pressure", "The pressure is raised, which is the point."],
   ["Xanthochromia", "That suggests subarachnoid haemorrhage."],
   ["A markedly raised protein with normal pressure",
    "Not the expected pattern here."]],
  "two-step", D, 46),

Q("Acute vision loss approach", IO,
  "A 54-year-old man has sudden vision loss that is PAINFUL. Which two diagnoses in this block "
  "should come to mind first?",
  [["Acute angle-closure glaucoma and optic neuritis",
    "Correct — those are the two painful causes; the rest are painless."],
   ["Central retinal artery occlusion and retinal detachment",
    "Both are painless; the artery occlusion is instant and the detachment is preceded by "
    "flashes."],
   ["Central and branch retinal vein occlusion",
    "Painless, and their hallmark is haemorrhage rather than pain."],
   ["Amaurosis fugax and papilledema",
    "Amaurosis is transient and painless; papilledema causes headache rather than eye pain."],
   ["Non-arteritic ischaemic optic neuropathy and branch artery occlusion",
    "Both painless, and both produce a field defect rather than pain."]],
  "two-step", D, 4),

Q("Arteritic AION", IO,
  "A 79-year-old woman with suspected giant cell arteritis has vision loss in one eye. What "
  "investigation confirms the diagnosis?",
  [["Temporal artery biopsy", "Correct — but treatment starts before the result."],
   ["Carotid Doppler", "That is the amaurosis fugax pathway."],
   ["Fluorescein angiography alone", "Characterises retinal perfusion but does not confirm "
                                     "arteritis."],
   ["Visual field testing", "Documents the deficit rather than the cause."],
   ["Optical coherence tomography", "Images the retina, not the artery wall."]],
  "two-step", D, 51),
]
