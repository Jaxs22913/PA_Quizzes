# -*- coding: utf-8 -*-
"""Clinical Reasoning and Problem Solving (Reynolds) -- pool for the Updated CMS derm master exams.

No arithmetic: per [[lecturer_profiles]] Reynolds does not examine calculation, so these test the
concepts (what sensitivity means, when to use which approach) rather than computing values.
"""
DECK = "1. svClinical Reasoning and Problem Solving.pptx"

def Q(topic, io, q, opts, c, slide):
    return {"topic": topic, "io": io, "q": q, "opts": opts, "c": c, "cite": f"{DECK}, Slide {slide}"}

QUESTIONS = [

Q("Sensitivity and specificity", "1 — Compare and contrast sensitivity and specificity",
  "A clinician wants a test that will correctly identify patients who do have a condition, minimising the number of "
  "affected patients missed. What property is she describing?",
  [["Sensitivity, the probability that the test is positive when the person does have the condition",
    "Correct. Sensitivity is the probability that the test shows a person has the condition when they do have it — "
    "how well a test detects a condition. Sensitivity is related to fewer false negatives."],
   ["Specificity, the probability that the test is negative when the person does not have the condition",
    "Specificity is the ability of a test to correctly identify patients who do not have the disease. It governs "
    "false positives rather than missed cases, which is the concern described here."],
   ["Pretest probability, the likelihood of disease before the result is known",
    "Pretest probability is the likelihood of the condition before the test result is known, derived from signs and "
    "symptoms, history and risk factors, and how common the condition is in the population."],
   ["Posttest probability, the likelihood of disease after the result is known",
    "Posttest probability is the likelihood of the condition after the test result is known. It is an output of "
    "testing rather than a property of the test."],
   ["Positive predictive value, the proportion of positive results that are true",
    "Predictive values depend on disease prevalence in the population tested, whereas the property being described "
    "here is intrinsic to the test's ability to detect disease."]],
  0, 6),

Q("Sensitivity and specificity", "1 — Compare and contrast sensitivity and specificity",
  "Which statement correctly pairs each test property with the error it reduces?",
  [["Sensitivity is related to fewer false negatives, and specificity to fewer false positives",
    "Correct. Sensitivity describes how well a test detects a condition and is related to fewer false negatives. "
    "Specificity is the ability to correctly identify patients who do not have the disease and is related to fewer "
    "false positives."],
   ["Sensitivity is related to fewer false positives, and specificity to fewer false negatives",
    "The two are reversed, and this is the single most common confusion in the topic. A clinician applying it would "
    "choose a specific test when trying not to miss disease."],
   ["Both properties reduce false negatives equally",
    "They address opposite errors, which is why the choice between them depends on whether missing disease or "
    "over-diagnosing it is the greater harm."],
   ["Neither property relates to false results, only to disease prevalence",
    "Prevalence governs pretest probability and predictive values. Sensitivity and specificity are properties of the "
    "test itself."],
   ["Sensitivity applies to screening only and specificity to diagnosis only",
    "Screening identifies the likelihood of occult disease and diagnostic testing complements history and "
    "examination, but both properties are relevant to both purposes."]],
  0, 8),

Q("Posttest probability", "3 — Define posttest probability",
  "How do pretest and posttest probability differ?",
  [["Pretest probability is the likelihood of the condition before the result is known and posttest probability the "
    "likelihood after",
    "Correct. Pretest probability is the likelihood of a condition before the test result is known, informed by signs "
    "and symptoms, history and risk factors, and how common the condition is in the population. Posttest probability "
    "is the likelihood after the result is known."],
   ["Pretest probability is the likelihood after the result is known and posttest probability before",
    "The two are reversed, which would invert the entire logic of how testing updates a clinical impression."],
   ["Both refer to the same quantity measured by different methods",
    "They are distinct quantities, and the difference between them is precisely what a test contributes."],
   ["Pretest probability applies only to screening tests",
    "Pretest probability applies to any clinical question, including diagnostic testing that complements history and "
    "physical examination."],
   ["Posttest probability is fixed by the test and does not depend on the clinical picture",
    "Posttest probability depends on where the patient started, which is why pretest probability from history, risk "
    "factors, and prevalence matters."]],
  0, 9),

Q("Diagnostic tools", "4 — Discuss clinical principles and decision-making",
  "How does screening testing differ in purpose from diagnostic testing?",
  [["Screening identifies the likelihood of occult disease, whereas diagnostic testing complements history and "
    "examination to reduce uncertainty and guide management",
    "Correct. Screening testing identifies the likelihood of occult disease. Diagnostic testing complements the "
    "history and physical examination, reduces uncertainty about diagnosis or prognosis, and helps decide "
    "management."],
   ["Screening confirms a diagnosis, whereas diagnostic testing looks for occult disease",
    "The purposes are reversed. Screening looks for disease not yet apparent; diagnostic testing addresses a question "
    "the clinical encounter has already raised."],
   ["Both have identical purposes and are interchangeable",
    "They answer different questions, and applying a screening test to a symptomatic patient or a diagnostic test to "
    "an asymptomatic population misuses both."],
   ["Screening is used only in emergency medicine",
    "Emergency medicine is the setting most associated with the naturalistic, event-driven approach rather than with "
    "screening."],
   ["Diagnostic testing replaces the history and physical examination",
    "Diagnostic testing complements the history and physical examination rather than replacing them."]],
  0, 10),

Q("Clinical approach", "4 — Discuss clinical principles and decision-making",
  "What are the first three steps of the clinical reasoning process?",
  [["Gather initial patient information, organise and interpret clinical information, then synthesise it into a "
    "problem representation",
    "Correct. The process begins with gathering initial patient information, then organising and interpreting it, "
    "then synthesising the information into a problem representation, before hypotheses are generated and tested."],
   ["Generate hypotheses, gather information, then test the hypotheses",
    "Generating hypotheses before gathering and organising information inverts the sequence and invites premature "
    "anchoring on a diagnosis."],
   ["Order diagnostic tests, interpret them, then take a history",
    "Diagnostic testing complements the history and physical examination rather than preceding them."],
   ["Treat the presenting symptoms, observe the response, then diagnose",
    "Treating signs and symptoms before a definitive diagnosis describes the naturalistic or event-driven approach, "
    "used mostly in emergency medicine for unstable patients and atypical presentations."],
   ["Apply a clinical guideline, then confirm it fits the patient",
    "Guidelines are common practice and often follow an if-then rule, but they should be applied appropriately to the "
    "individual rather than substituted for the reasoning process."]],
  0, 11),

Q("Differential diagnosis", "4 — Discuss clinical principles and decision-making",
  "A student uses the VINDICATE mnemonic to build a differential for confusion. What do the letters stand for?",
  [["Vascular, infectious, neoplastic, degenerative, iatrogenic, congenital, autoimmune, trauma, and endocrine or "
    "metabolic",
    "Correct. VINDICATE is a category-based framework: vascular, infectious, neoplastic, degenerative, iatrogenic, "
    "congenital, autoimmune, trauma, and endocrine or metabolic. Applied to confusion it yields stroke, meningitis, "
    "brain tumour, Alzheimer disease, and so on."],
   ["Vascular, inflammatory, neurological, drug-related, idiopathic, cardiac, allergic, toxic, and environmental",
    "Several of these categories are plausible in isolation but they are not the letters of this mnemonic, and a "
    "misremembered framework produces a differential with systematic gaps."],
   ["A sequence of steps for physical examination",
    "VINDICATE is a differential diagnosis framework organised by disease category rather than an examination "
    "sequence."],
   ["A checklist for evaluating the quality of published evidence",
    "Evaluating the quality and validity of evidence is a step in evidence-based practice, separate from this "
    "mnemonic."],
   ["A scoring system for estimating pretest probability",
    "The mnemonic generates categories to consider rather than producing a numerical probability."]],
  0, 16),

Q("Hypothetico-deductive method", "4 — Discuss clinical principles and decision-making",
  "What does the hypothetico-deductive method involve?",
  [["Proposing hypotheses and testing whether they are acceptable by deciding if the data are consistent with them",
    "Correct. The hypothetico-deductive method proposes hypotheses and tests whether they are acceptable or not by "
    "deciding whether the data are consistent with what has been observed. It runs from initial history, examination, "
    "and screening cues through hypothesis generation to hypothesis evaluation."],
   ["Treating signs and symptoms before a definitive diagnosis is reached",
    "Treating before a definitive diagnosis describes the naturalistic or event-driven approach, used mostly in "
    "emergency medicine."],
   ["Recognising disease patterns automatically without deliberate analysis",
    "Fast, automatic pattern recognition is the intuitive system used in straightforward or common situations, "
    "contrasted with the more deliberate, controlled process."],
   ["Applying an if-then rule from a published guideline",
    "If-then rules from guidelines are a distinct approach — straightforward and easy to use but requiring "
    "appropriate application."],
   ["Ranking diagnoses purely by how common they are in the population",
    "Base rates matter and common things occur commonly, but the method is defined by generating and testing "
    "hypotheses against the data."]],
  0, 19),

Q("Naturalistic approach", "5 — Discuss the naturalistic approach",
  "In which situation is the naturalistic, event-driven approach most appropriate?",
  [["An unstable patient with an atypical presentation in whom the worst-case scenario must be excluded",
    "Correct. The naturalistic or event-driven approach treats signs and symptoms before a definitive diagnosis. It "
    "is used mostly in emergency medicine, for unstable patients and atypical presentations, to rule out the "
    "worst-case scenario, following responses to interventions."],
   ["A stable outpatient with a classic presentation of a common condition",
    "Straightforward or common situations are where pattern recognition and the intuitive system work well, and where "
    "there is time for a deliberate diagnostic process before treatment."],
   ["A research setting where evidence quality is being appraised",
    "Appraising evidence quality and validity belongs to evidence-based practice rather than to bedside management of "
    "an unstable patient."],
   ["A screening programme in an asymptomatic population",
    "Screening identifies the likelihood of occult disease in people without symptoms, which is the opposite of an "
    "event-driven response to an acute presentation."],
   ["Any situation, since treating before diagnosis is always preferable",
    "Treating before diagnosis is a deliberate trade-off appropriate to instability and diagnostic uncertainty, not a "
    "universal default."]],
  0, 24),

Q("Clinical principles", "4 — Discuss clinical principles and decision-making",
  "What does the principle 'place your bets on uncommon manifestations of common conditions rather than common "
  "manifestations of uncommon conditions' mean in practice?",
  [["An atypical presentation of a frequent disease is more likely than a typical presentation of a rare one",
    "Correct. Common things occur commonly — when you hear hoof beats think of horses, not zebras. An unusual "
    "presentation of a common condition is more probable than a textbook presentation of something rare."],
   ["A typical presentation of a rare disease should be favoured over an atypical presentation of a common one",
    "This inverts the principle and is precisely the reasoning error it exists to prevent."],
   ["Rare diagnoses should never be considered",
    "The principle orders probabilities rather than forbidding rare diagnoses, and clinicians are also advised to "
    "actively seek alternative diagnoses."],
   ["All diagnoses on a differential are equally likely until tested",
    "Being aware of the base rate of disease for diagnoses on the differential is explicitly recommended, so they are "
    "not treated as equally likely."],
   ["The most serious diagnosis should always be assumed first",
    "Ruling out the worst-case scenario belongs to the naturalistic approach in unstable patients rather than being "
    "the general principle of probability."]],
  0, 25),

Q("Clinical decision making", "4 — Discuss clinical principles and decision-making",
  "Which suggestion for good decision-making addresses confirmation bias most directly?",
  [["Ask questions to disprove, rather than confirm, your working diagnosis",
    "Correct. Among the suggestions for good decision-making is to ask questions to disprove rather than confirm, "
    "alongside slowing down, being aware of base rates, considering what data is truly relevant, and actively seeking "
    "alternative diagnoses."],
   ["Apply an if-then guideline rule as early as possible",
    "Guidelines are usually straightforward and easy to use but should be applied appropriately, and reaching for one "
    "early does not counteract a bias toward one's initial impression."],
   ["Gather as much data as possible regardless of relevance",
    "The advice is to consider what data is truly relevant. Indiscriminate data gathering produces incidental "
    "findings without improving reasoning."],
   ["Rely on intuitive pattern recognition to reach a conclusion quickly",
    "The intuitive system works in straightforward or common situations but is the mode in which confirmation bias "
    "operates most freely, which is why slowing down is advised."],
   ["Defer all decisions until every test result has returned",
    "Deferring indefinitely is not among the suggestions and can be harmful in an unstable patient."]],
  0, 26),

Q("Implications for treatment", "6 — Discuss the implications for treatment",
  "What factors govern the decision to treat when the diagnosis carries some uncertainty?",
  [["The probability of disease, the likelihood of treatment success, the patient's ability to tolerate treatment, "
    "and the balance of risk against benefit",
    "Correct. The value of treatment versus no treatment is a linear function of the probability of disease, together "
    "with the likelihood of success and the ability to tolerate treatment, weighed as risk against benefit."],
   ["Only the probability of disease, independent of the treatment's risks",
    "Probability is one input, but the likelihood of success, tolerability, and the risk-benefit balance all bear on "
    "whether treating is worthwhile."],
   ["Only the cost of the treatment",
    "Cost and affordability are recognised barriers to adherence rather than the framework for deciding whether "
    "treatment is indicated."],
   ["Treatment should always be withheld until the diagnosis is certain",
    "Certainty is often unattainable, and the naturalistic approach treats before a definitive diagnosis in unstable "
    "patients specifically because waiting can be harmful."],
   ["Treatment should always be given when any possibility of disease exists",
    "That discards the risk-benefit weighing entirely and would expose patients to treatments they do not need."]],
  0, 27),

Q("Counselling and adherence", "7 — Recall counseling strategies to help patients adhere to treatment plans",
  "Why must clinicians be able to communicate evidence on prognosis, treatment, testing, and prevention effectively?",
  [["To help patients understand their risks and options",
    "Correct. Healthcare providers must be able to effectively communicate evidence on prognosis, treatments, "
    "diagnostic testing, and prevention to help patients understand their risks and options."],
   ["To ensure patients accept whatever plan the clinician has chosen",
    "The purpose is to enable understanding of risks and options rather than to secure compliance with a "
    "predetermined decision."],
   ["To satisfy documentation requirements",
    "Documentation is a separate concern; the stated purpose of communication here is patient understanding."],
   ["To reduce the time spent in consultation",
    "Effective communication of evidence generally takes time, and time is listed among the limitations of "
    "evidence-based practice rather than a benefit."],
   ["To transfer responsibility for the decision entirely to the patient",
    "Helping patients understand risks and options supports shared decision-making rather than abdicating clinical "
    "responsibility."]],
  0, 28),

Q("Counselling and adherence", "7 — Recall counseling strategies to help patients adhere to treatment plans",
  "Which barriers to treatment and medication adherence should be considered?",
  [["Cost and affordability, low health literacy or lack of understanding, and cultural or religious factors",
    "Correct. Barriers to treatment and medication adherence include the cost and affordability of medications or "
    "services, low health literacy or lack of understanding, and cultural or religious considerations."],
   ["Only the cost of medications",
    "Cost is one barrier among several, and addressing it alone leaves understanding and cultural factors "
    "unaddressed."],
   ["Only the patient's motivation",
    "Framing non-adherence as a motivational failing overlooks the structural and educational barriers explicitly "
    "listed."],
   ["Only the complexity of the dosing regimen",
    "Regimen complexity is a real-world issue but is not among the barriers named here."],
   ["Barriers are unpredictable and cannot be anticipated",
    "The named barriers are precisely those a clinician can anticipate and address during counselling."]],
  0, 29),

Q("Clinical decision making", "4 — Discuss clinical principles and decision-making",
  "What are the limitations of applying evidence-based medicine at the bedside?",
  [["It is time consuming and many clinical questions do not have relevant evidence available",
    "Correct. The limitations given are that the process is time consuming and that many clinical questions do not "
    "have relevant evidence to answer them."],
   ["It always produces a definitive answer but is expensive",
    "The difficulty is that many questions lack relevant evidence, so a definitive answer is often exactly what is "
    "not available."],
   ["It cannot be combined with clinical guidelines",
    "Clinical guidelines are common practice and sit alongside evidence appraisal rather than being incompatible "
    "with it."],
   ["It applies only to surgical decisions",
    "The framework applies across clinical questions, with the worked example being whether a chest radiograph or "
    "computed tomography better evaluates a smoker with chest pain and haemoptysis."],
   ["It removes the need for clinical judgement",
    "Deciding how to use evidence to care for a particular patient is itself a step requiring judgement."]],
  0, 22),

Q("Clinical decision making", "4 — Discuss clinical principles and decision-making",
  "What three questions must clinicians answer in clinical decision making?",
  [["What disease does the patient have, should testing be done, and should this patient be treated",
    "Correct. Clinical decision making requires answering what disease the patient has, whether testing should be "
    "done, and whether this patient should be treated — alongside deciding what information to gather and how to "
    "integrate it."],
   ["What disease does the patient have, what is the prognosis, and what is the cost",
    "Prognosis and cost are relevant to counselling and adherence, but the three decision questions concern "
    "diagnosis, testing, and treatment."],
   ["Which guideline applies, which specialist to consult, and when to follow up",
    "Guidelines and referral are tools within decision-making rather than the framing questions."],
   ["Is the patient stable, is the diagnosis certain, and is the family informed",
    "Stability drives the naturalistic approach in emergency settings but is not one of the three stated questions."],
   ["What is the pretest probability, the posttest probability, and the likelihood ratio",
    "These quantitative concepts inform decisions but are not themselves the three clinical questions."]],
  0, 13),
]
