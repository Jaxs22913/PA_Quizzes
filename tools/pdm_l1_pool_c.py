# Principles of Diagnostic Medicine I, Lecture 1 — pool C
# Qualitative vs quantitative, point-of-care logistics and regulation, and the
# statistics: sensitivity, specificity, predictive values, screening vs
# diagnostic, and pre/post-test probability.
# Syllabus objectives i, j, k, l, m, n, o.
#
# NO ARITHMETIC. Professor Reynolds, 2026-08-18: "we don't, we're not gonna do
# math, I'm not gonna make you do math" -- said while walking the shark-bite
# example, immediately before asking which SCENARIO has the higher positive
# predictive value. So predictive value is tested as REASONING (which direction
# does prevalence push it, and why) and never as a calculation. The frostbite
# and shark-bite worked examples appear here as reasoning prompts, with any
# numbers supplied in the stem rather than demanded from the student.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "1. Principles of Laboratory Diagnostics sv.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOI = "Objective i — Qualitative versus quantitative diagnostic tests"
IOJ = "Objective j — Availability, advantages and limitations of point-of-care testing"
IOK = "Objective k — Quality assurance measures for point-of-care testing"
IOL = "Objective l — Accreditation and regulatory considerations"
IOM = "Objective m — Sensitivity, specificity, positive and negative predictive value"
ION = "Objective n — Screening versus diagnostic tests"
IOO = "Objective o — Pretest and posttest probability"

POOL_C = [
 dict(topic="Qualitative vs quantitative", io=IOI,
   q="Which question does a qualitative test answer?",
   opts=[
     ["A “why” question, producing observation and description",
      "Correct — qualitative data is observed and interpreted, and analysed by grouping common data."],
     ["A “how much” question, producing a numerical result",
      "That describes a quantitative test."],
     ["A “how often” question, producing an incidence rate",
      "Neither category is defined this way."],
     ["A “when” question, producing a timeline",
      "Neither category is defined this way."]],
   c=0, cite=c(41)),

 dict(topic="Qualitative vs quantitative", io=IOI,
   q="Which characteristic belongs to quantitative testing?",
   opts=[
     ["Data are numbers or statistical results, analysed statistically",
      "Correct — quantitative testing measures and tests, answering how many or how much."],
     ["Data are descriptions requiring non-statistical grouping",
      "That describes qualitative testing."],
     ["Results are always reported as positive or negative",
      "That is closer to a qualitative cartridge result."],
     ["Results require no instrumentation to interpret",
      "That describes non-instrumental point-of-care testing."]],
   c=0, cite=c(41)),

 dict(topic="Qualitative vs quantitative", io=IOI,
   q="A urine pregnancy test returns simply positive or negative. How is this analyser type classified?",
   opts=[
     ["Qualitative",
      "Correct — rapid strep and influenza tests are likewise qualitative; a urinalysis dipstick is semi-quantitative."],
     ["Quantitative",
      "A quantitative result would be a number, such as a glucose value."],
     ["Semi-quantitative",
      "The urinalysis dipstick is the semi-quantitative example."],
     ["Multiple-use benchtop",
      "That describes a device category rather than the result type."]],
   c=0, cite=c(32)),

 dict(topic="Qualitative vs quantitative", io=IOI,
   q="Which is described as the highest-volume point-of-care test using a single-use quantitative cartridge or strip with a reader?",
   opts=[
     ["Glucose",
      "Correct — listed alongside blood chemistries, coagulation studies, cardiac markers and hemoglobin A1c."],
     ["Rapid strep",
      "That is a qualitative cartridge test."],
     ["Urinalysis dipstick",
      "That is semi-quantitative."],
     ["Urine pregnancy testing",
      "That is qualitative and non-instrumental."]],
   c=0, cite=c(32)),

 dict(topic="POCT devices", io=IOJ,
   q="What defines non-instrumental point-of-care testing?",
   opts=[
     ["It does not rely on instrumentation to interpret results",
      "Correct — urine pregnancy testing, coronavirus tests and fecal occult blood are the examples."],
     ["It requires no reagents or consumables",
      "Handheld equipment usually requires reagents; that is not what non-instrumental means."],
     ["It may only be performed by licensed personnel",
      "Some non-instrumental tests are performed at home."],
     ["It produces a numerical result without a reader",
      "Non-instrumental tests are typically read visually as positive or negative."]],
   c=0, cite=c(33)),

 dict(topic="POCT devices", io=IOJ,
   q="How does handheld point-of-care equipment differ from a benchtop device?",
   opts=[
     ["Handheld equipment is easy to carry, involves one to two steps, and usually gives one or few data points; benchtop devices are stationary, multi-step, and give multiple data points",
      "Correct — portability, complexity and data yield all differ."],
     ["Handheld equipment requires no reagents while benchtop devices do",
      "Both usually require reagents and consumables."],
     ["Handheld equipment is quantitative while benchtop devices are qualitative",
      "Both categories span result types."],
     ["Handheld equipment requires a laboratory certificate while benchtop devices do not",
      "All testing sites require certification regardless of device."]],
   c=0, cite=c(33)),

 dict(topic="POCT logistics", io=IOJ,
   q="Which is listed as an advantage of point-of-care testing?",
   opts=[
     ["Better care where resources are limited, such as rural settings or disaster zones",
      "Correct, alongside convenience, speed, less manpower, fewer visits and fingerstick rather than needle stick."],
     ["Greater precision than central laboratory methods",
      "Results may be less precise, which is listed as a limitation."],
     ["Lower cost than central laboratory testing",
      "Expense is listed among the limitations."],
     ["Standardised vocabulary across manufacturers",
      "Vocabulary is described as not always standardised, which is a limitation."]],
   c=0, cite=c(35)),

 dict(topic="POCT logistics", io=IOJ,
   q="Which is listed as a limitation of point-of-care testing?",
   opts=[
     ["Operator and manufacturer variability",
      "Correct, alongside expense, difficulty controlling quality assurance, non-standardised vocabulary, imprecision and supply needs."],
     ["Longer turnaround than central laboratory testing",
      "Speed is an advantage of point-of-care testing."],
     ["The need for venipuncture rather than fingerstick",
      "Fingerstick rather than needle stick is listed as an advantage."],
     ["Requirement for a hospital setting",
      "Point-of-care testing is specifically used away from the central laboratory."]],
   c=0, cite=c(35)),

 dict(topic="POCT quality", io=IOK,
   q="Which quality measure addresses post-testing errors in point-of-care testing?",
   opts=[
     ["Connecting devices to electronic information systems",
      "Correct — communication breakdown is the named risk, and connectivity is the stated mitigation."],
     ["Requiring two operators to witness each result",
      "This is not among the quality measures listed."],
     ["Repeating every abnormal result in the central laboratory",
      "Confirmatory testing may occur clinically but is not the listed quality measure."],
     ["Restricting testing to daylight hours",
      "This is not a quality measure."]],
   c=0, cite=c(34)),

 dict(topic="POCT quality", io=IOK,
   q="Which of the following is a named quality assurance measure for point-of-care testing?",
   opts=[
     ["Active enrollment and participation in an External Quality Assurance program",
      "Correct, alongside trained and competent operators, correct specimen collection, accurate patient identification and quality control."],
     ["Annual replacement of all devices regardless of performance",
      "This is not among the measures."],
     ["Testing only specimens collected by laboratory staff",
      "Point-of-care testing is performed by a range of practitioners."],
     ["Reporting results verbally rather than electronically",
      "Electronic connection is what is recommended."]],
   c=0, cite=c(34)),

 dict(topic="Regulation", io=IOL,
   q="What does the Clinical Laboratory Improvement Amendments program establish?",
   opts=[
     ["Federal guidelines for minimum quality standards when testing human samples at all types of sites",
      "Correct — it sets the floor, and it arose from problems in cytology laboratories reading Papanicolaou smears."],
     ["Voluntary best-practice recommendations for hospital laboratories only",
      "The standards are federal requirements, not voluntary, and they apply to all site types."],
     ["Maximum permissible turnaround times for laboratory results",
      "The amendments address quality standards rather than turnaround."],
     ["Reimbursement rates for laboratory testing",
      "User fees are collected but rate-setting is not what the program establishes."]],
   c=0, cite=c(36)),

 dict(topic="Regulation", io=IOL,
   q="A state enacts laboratory regulation that differs from the federal Clinical Laboratory Improvement Amendments. What is the relationship?",
   opts=[
     ["State and city regulation will always be stricter, because the federal standard is the minimum and cannot be downgraded",
      "Correct — states may add requirements but may never relax them."],
     ["State regulation supersedes the federal standard in either direction",
      "States cannot downgrade the federal minimum."],
     ["Federal regulation applies only where no state rule exists",
      "The federal standard applies as the minimum everywhere."],
     ["State regulation applies only to hospital laboratories",
      "The federal minimum applies to all testing sites."]],
   c=0, cite=c(38)),

 dict(topic="Regulation", io=IOL,
   q="Which testing complexity category accounts for roughly 75% of the twelve thousand available laboratory tests?",
   opts=[
     ["Moderately complex testing",
      "Correct — usually automated, and the majority of tests in use."],
     ["Waived testing",
      "Waived testing carries little chance of a negative outcome from a false result."],
     ["Highly complex testing",
      "Highly complex testing requires operator skill and decision making, such as cross match testing."],
     ["Provider-performed microscopy",
      "That is slide examination of a freshly collected specimen by a provider."]],
   c=0, cite=c(37)),

 dict(topic="Regulation", io=IOL,
   q="How does the Joint Commission classify testing performed outside a traditional laboratory?",
   opts=[
     ["As waived testing, which includes point-of-care testing",
      "Correct — that classification is what brings point-of-care testing under the waived category."],
     ["As moderately complex testing",
      "That category covers the majority of laboratory tests, not point-of-care testing by definition."],
     ["As highly complex testing",
      "Highly complex testing requires operator decision making and complex instrumentation."],
     ["As provider-performed microscopy",
      "That is a distinct category for slide examination."]],
   c=0, cite=c(37)),

 dict(topic="Regulation", io=IOL,
   q="Which category describes slide examination of a freshly collected specimen by a provider, such as a Gram stain or manual cell count?",
   opts=[
     ["Provider-performed microscopy",
      "Correct — a distinct complexity category."],
     ["Waived testing",
      "Waived testing is defined by low risk from an incorrect result."],
     ["Moderately complex testing",
      "That category is usually automated."],
     ["Highly complex testing",
      "That category involves complex instrumentation such as cross match testing."]],
   c=0, cite=c(37)),

 dict(topic="Regulation", io=IOL,
   q="Which agency categorizes tests based on complexity under the Clinical Laboratory Improvement Amendments?",
   opts=[
     ["The Food and Drug Administration",
      "Correct — it also reviews waiver applications and develops categorization guidance."],
     ["The Centers for Medicare and Medicaid Services",
      "That agency issues certificates, collects fees, inspects and enforces."],
     ["The Centers for Disease Control and Prevention",
      "That agency provides analysis, research, technical standards and quality improvement studies."],
     ["The Joint Commission",
      "It classifies testing outside a traditional laboratory as waived, but does not perform federal complexity categorization."]],
   c=0, cite=c(39)),

 dict(topic="Regulation", io=IOL,
   q="Which agency issues laboratory certificates and conducts inspections?",
   opts=[
     ["The Centers for Medicare and Medicaid Services",
      "Correct — it also collects user fees, approves accreditation organizations and publishes the rules."],
     ["The Food and Drug Administration",
      "That agency categorizes tests by complexity."],
     ["The Centers for Disease Control and Prevention",
      "That agency develops technical standards and conducts quality improvement studies."],
     ["The National Institutes of Health",
      "This agency has no role in the program."]],
   c=0, cite=c(39)),

 dict(topic="Regulation", io=IOL,
   q="How often must a testing site reapply for its certificate?",
   opts=[
     ["Every two years",
      "Correct, and the certificate must match the level of testing complexity performed."],
     ["Every year",
      "The stated interval is two years."],
     ["Every five years",
      "The stated interval is two years."],
     ["Only when the scope of testing changes",
      "Reapplication is on a fixed cycle."]],
   c=0, cite=c(38)),

 dict(topic="Screening vs diagnostic", io=ION,
   q="What distinguishes a screening test from a diagnostic test?",
   opts=[
     ["Screening looks for evidence of disease in an asymptomatic person; a diagnostic test looks for the reason for symptoms",
      "Correct — the presence or absence of symptoms is the discriminator."],
     ["Screening is always more invasive than diagnostic testing",
      "Diagnostic tests may be more invasive and carry more risk of complications."],
     ["Screening provides the definitive diagnosis",
      "A screening test does not necessarily provide a diagnosis and may require confirmation."],
     ["Screening is performed only after an abnormal diagnostic result",
      "The sequence runs the other way."]],
   c=0, cite=c(40)),

 dict(topic="Screening vs diagnostic", io=ION,
   q="Which characteristics describe a screening test?",
   opts=[
     ["Typically inexpensive and easy to perform, indicating whether further testing is needed",
      "Correct — screening should be performed before more expensive or time-consuming tests."],
     ["Typically invasive with a meaningful risk of complications",
      "That describes a diagnostic test."],
     ["Typically performed to confirm a condition already suspected",
      "Confirmation is the role of a diagnostic test."],
     ["Typically reserved for symptomatic patients",
      "Screening targets asymptomatic people."]],
   c=0, cite=c(40)),

 dict(topic="Screening vs diagnostic", io=ION,
   q="A colonoscopy performed for routine screening reveals a lesion, which is then biopsied. What does this illustrate?",
   opts=[
     ["A screening test may become diagnostic if an abnormality is found during testing",
      "Correct — colonoscopy is the example given for exactly this."],
     ["A diagnostic test may be downgraded to screening once normal",
      "The transition described runs in the other direction."],
     ["Screening tests must always be followed by a separate diagnostic procedure",
      "The point is that the same procedure can serve both roles."],
     ["Screening and diagnostic testing are interchangeable terms",
      "They are distinguished by purpose and by whether symptoms are present."]],
   c=0, cite=c(40)),

 dict(topic="Sensitivity and specificity", io=IOM,
   q="What does sensitivity measure?",
   opts=[
     ["The probability that the test is positive when the person does have the condition",
      "Correct — it reflects how well a test detects a condition, and relates to fewer false negatives."],
     ["The probability that the test is negative when the person does not have the condition",
      "That is specificity."],
     ["The probability that a person with a positive test has the disease",
      "That is positive predictive value."],
     ["The probability that a person with a negative test lacks the disease",
      "That is negative predictive value."]],
   c=0, cite=c(42)),

 dict(topic="Sensitivity and specificity", io=IOM,
   q="What does the memory aid “SnNout” mean?",
   opts=[
     ["A test with high Sensitivity and a Negative result helps rule out disease",
      "Correct — with sensitivity, a negative is a negative."],
     ["A test with high Sensitivity and a Positive result helps rule in disease",
      "That inverts it; the positive-rules-in aid is SpPin, for specificity."],
     ["A test with high Specificity and a Negative result helps rule out disease",
      "That mixes the two aids."],
     ["A test with high Specificity and a Positive result helps rule in disease",
      "That is SpPin."]],
   c=0, cite=c(42)),

 dict(topic="Sensitivity and specificity", io=IOM,
   q="Specificity relates to fewer of which kind of error?",
   opts=[
     ["False positives",
      "Correct, and specificity does not address false negatives."],
     ["False negatives",
      "Sensitivity relates to fewer false negatives."],
     ["Both false positives and false negatives equally",
      "Each measure addresses one and not the other."],
     ["Neither; specificity addresses precision rather than error type",
      "Specificity is explicitly tied to false positives."]],
   c=0, cite=c(42)),

 dict(topic="Sensitivity and specificity", io=IOM,
   q="Which test characteristic is best suited to screening, and which to confirming a diagnosis?",
   opts=[
     ["A highly sensitive test is best for screening; a highly specific test is best for confirming",
      "Correct — screening should not miss disease, and confirmation should not falsely label it."],
     ["A highly specific test is best for screening; a highly sensitive test is best for confirming",
      "That reverses the application."],
     ["Sensitivity is preferred for both roles",
      "Each characteristic suits a different role."],
     ["Neither characteristic bears on the choice",
      "The application follows directly from them."]],
   c=0, cite=c(44)),

 dict(topic="Sensitivity and specificity", io=IOM,
   q="Screening for human immunodeficiency virus uses a highly sensitive test first. Why is this the right order?",
   opts=[
     ["It is better to have a few false positives, later corrected by a confirmatory test, than to miss infected individuals who might unknowingly infect others",
      "Correct — the confirmatory supplemental test is highly specific and minimises false-positive diagnoses."],
     ["A highly sensitive test is cheaper than a highly specific one in every case",
      "Cost is not the stated reason for the sequence."],
     ["A highly sensitive test provides a definitive diagnosis on its own",
      "Confirmatory testing follows precisely because it does not."],
     ["Confirmatory testing is unnecessary once a sensitive screen is negative",
      "The reasoning given concerns positives and the risk of missed infection."]],
   c=0, cite=c(44)),

 dict(topic="Predictive values", io=IOM,
   q="What does positive predictive value indicate?",
   opts=[
     ["The likelihood that a positive test result identifies someone with the disease",
      "Correct — and negative predictive value is the likelihood that a negative result identifies someone without it."],
     ["The likelihood that the test will be positive when disease is present",
      "That is sensitivity."],
     ["The proportion of the population that has the disease",
      "That is prevalence."],
     ["The likelihood that the test will be negative when disease is absent",
      "That is specificity."]],
   c=0, cite=c(46)),

 dict(topic="Predictive values", io=IOM,
   q="Which pair are test-centered probabilities, and which are patient-centered?",
   opts=[
     ["Sensitivity and specificity are test-centered; predictive values are patient-centered",
      "Correct — the reversal of conditioning between them is the foundation of Bayes' theorem."],
     ["Sensitivity and specificity are patient-centered; predictive values are test-centered",
      "That reverses the distinction."],
     ["All four are test-centered",
      "Predictive values depend on the population being tested."],
     ["All four are patient-centered",
      "Sensitivity and specificity belong to the test itself."]],
   c=0, cite=c(47)),

 dict(topic="Predictive values", io=IOM,
   q="A clinician asks: “My patient's test is positive — what is the probability they actually have the disease?” Which measure answers this?",
   opts=[
     ["Positive predictive value",
      "Correct. It is tempting to reach for sensitivity here, but sensitivity answers the reverse question."],
     ["Sensitivity",
      "Sensitivity is the probability the test is positive given disease is present — the reverse conditioning."],
     ["Specificity",
      "Specificity concerns those without the disease."],
     ["Prevalence",
      "Prevalence describes the population rather than this patient's result."]],
   c=0, cite=c(47)),

 dict(topic="Predictive values", io=IOM,
   q="A test with 95% sensitivity and 95% specificity is used in a high-prevalence population and then in a low-prevalence one. What happens to positive predictive value?",
   opts=[
     ["It is higher in the high-prevalence population and lower in the low-prevalence one",
      "Correct — the frostbite example gives 68% in the high-prevalence setting against about 2% in the low-prevalence one, with the same test."],
     ["It stays the same, because the test characteristics are unchanged",
      "Predictive value belongs to the population, not the test."],
     ["It is lower where prevalence is high, because more true cases dilute the result",
      "The relationship runs the other way."],
     ["It cannot be compared without recalculating sensitivity",
      "Sensitivity is unchanged; prevalence is what differs."]],
   c=0, cite=c(50)),

 dict(topic="Predictive values", io=IOM,
   q="In the shark-bite example, an identical detector is used in Florida and in Michigan. Where will most positive results be false positives, and why?",
   opts=[
     ["Michigan, because shark bites are extraordinarily rare there, so the pre-test probability is very low",
      "Correct — the tests are identical; only the pre-test probability differs."],
     ["Florida, because the higher number of true cases produces more errors overall",
      "Higher prevalence raises the proportion of positives that are true."],
     ["Both equally, because the test has the same sensitivity and specificity in each",
      "Equal test characteristics do not produce equal predictive value."],
     ["Neither, because a detector with 95% specificity rarely produces false positives",
      "Even a good test yields mostly false positives when the condition is rare."]],
   c=0, cite=c(51)),

 dict(topic="Pre and post-test probability", io=IOO,
   q="What is pre-test probability?",
   opts=[
     ["The likelihood of the condition before the test result is known, based on signs, symptoms, history, risk factors and how common it is in the population",
      "Correct — post-test probability is the likelihood after the result, and depends on sensitivity and specificity."],
     ["The likelihood that the test will be performed correctly",
      "That concerns quality assurance rather than probability."],
     ["The proportion of positive results a laboratory reports",
      "That is not what pre-test probability describes."],
     ["The likelihood of the condition after the result is known",
      "That is post-test probability."]],
   c=0, cite=c(45)),

 dict(topic="Pre and post-test probability", io=IOO,
   q="What is the difference between prevalence and incidence?",
   opts=[
     ["Prevalence reflects how commonly something occurs in a population; incidence is how often it happens",
      "Correct — prevalence is the existing case burden, usually expressed as a percentage."],
     ["Prevalence is how often something happens; incidence is how common it is",
      "That reverses the two."],
     ["They are interchangeable terms for disease frequency",
      "They are distinguished explicitly."],
     ["Prevalence applies to tests and incidence applies to populations",
      "Both are population measures."]],
   c=0, cite=c(47)),

 dict(topic="Pre and post-test probability", io=IOO,
   q="Which statement best summarises the relationship between a test and the population it is used in?",
   opts=[
     ["Sensitivity and specificity belong to the test; predictive value belongs to the population being tested",
      "Correct — the test stays the same, and prevalence changes the meaning of the result."],
     ["Both the test characteristics and the predictive values belong to the test",
      "Predictive value shifts with the population."],
     ["Both belong to the population and vary from place to place",
      "Sensitivity and specificity are properties of the test itself."],
     ["Neither is affected by where the test is performed",
      "Predictive value very much is."]],
   c=0, cite=c(52)),

 dict(topic="Pre and post-test probability", io=IOO,
   q="Why does knowing the pre-test probability help before a test is ordered?",
   opts=[
     ["It indicates the chance the condition is present beforehand, which helps decide whether the test is worth ordering at all",
      "Correct — that judgement comes from the patient's presentation and risk factors."],
     ["It allows the sensitivity of the test to be adjusted for that patient",
      "Sensitivity is a fixed property of the test."],
     ["It determines which collection tube should be used",
      "Tube selection depends on the assay, not on probability."],
     ["It establishes whether the test requires a laboratory certificate",
      "Certification depends on test complexity."]],
   c=0, cite=c(45)),

 dict(topic="Bayes", io=IOM,
   q="What does incorporating prevalence into sensitivity produce?",
   opts=[
     ["The clinically useful positive predictive value, by way of Bayes' theorem",
      "Correct — moving from a test-centered probability to a patient-centered one."],
     ["The specificity of the test in that population",
      "Specificity is a property of the test and does not derive from prevalence."],
     ["The incidence of the condition",
      "Incidence is how often something happens, and is not derived this way."],
     ["The pre-test probability of the next patient tested",
      "Pre-test probability is an input rather than the output."]],
   c=0, cite=c(47)),
]
