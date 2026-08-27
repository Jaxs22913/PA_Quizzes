# Principles of Diagnostic Medicine I, Lecture 1 — pool A
# Role of laboratory testing, patient counseling, and the three phases.
# Syllabus objectives a, b, c, d.
#
# PROFESSOR REYNOLDS' RULES, from the 2026-08-18 recording, enforced throughout:
#   - Reference ranges are ALWAYS supplied on her exams, so no question here may
#     require a memorised normal value. If a number appears, its range appears.
#   - Scope leans to the TESTS rather than the diagnoses: "more related to the
#     tests themselves rather than maybe the specific diagnosis".
#   - Vignette / next-best-test phrasing where it is natural, which is the shape
#     she described.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "1. Principles of Laboratory Diagnostics sv.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "a — Importance and role of laboratory testing in evaluating a patient"
IOB = "b — Patient counseling for diagnostic testing to reduce medical errors"
IOC = "c — Phases of the diagnostic testing process"
IOD = "d — Components of the pretest, intratest and posttest phases"

POOL_A = [
 dict(topic="Role of testing", io=IOA,
   q="A patient asks why you are ordering a laboratory test when you already suspect the diagnosis. Which statement best describes the role of laboratory testing?",
   opts=[
     ["It is a tool used alongside a thorough history and physical examination to add information",
      "Correct. Diagnostics supplement the history and examination rather than replacing them."],
     ["It replaces the history and physical examination once results are available",
      "Testing is used in conjunction with the history and examination, never instead of them."],
     ["It is primarily therapeutic rather than diagnostic",
      "Testing is not necessarily therapeutic, though a blood culture that guides antibiotic choice can be."],
     ["It is ordered chiefly to satisfy documentation requirements",
      "Documentation matters, but it is not why a test is ordered."]],
   c=0, cite=c(6)),

 dict(topic="Role of testing", io=IOA,
   q="Which of the following is a stated use of diagnostic testing?",
   opts=[
     ["Monitoring a patient's response to therapy",
      "Correct. The others are confirming a diagnosis, informing health status, evaluating severity, directing treatment, and guiding ongoing care through screening."],
     ["Establishing the patient's insurance eligibility",
      "Cost and reimbursement are considered in the pretest phase, but this is not a use of the test result."],
     ["Replacing the need for follow-up visits",
      "Results frequently generate follow-up rather than removing it."],
     ["Providing a definitive answer in every clinical situation",
      "No test is claimed to be definitive in every situation."]],
   c=0, cite=c(6)),

 dict(topic="Role of testing", io=IOA,
   q="Before ordering a test, which two questions should be asked about it?",
   opts=[
     ["Will it support or guide management, and is it cost effective?",
      "Correct — appropriateness for this patient is the first consideration, not availability."],
     ["Is it available in-house, and how quickly does it result?",
      "Turnaround matters operationally but is not the appropriateness question."],
     ["Has the patient had it before, and did they tolerate it?",
      "Prior testing is part of the history rather than the test-selection question."],
     ["Is it the newest available assay, and is it automated?",
      "Neither novelty nor automation determines whether a test is appropriate."]],
   c=0, cite=c(14)),

 dict(topic="Patient counseling", io=IOB,
   q="What is the stated relationship between patient education and compliance with a diagnostic plan?",
   opts=[
     ["Patients are more likely to be compliant when they are informed and understand the advised plan",
      "Correct, and this is why counseling is framed as a means of reducing medical errors."],
     ["Compliance depends chiefly on the cost of the test to the patient",
      "Cost is a consideration but is not what the counseling objective addresses."],
     ["Compliance is determined mainly by how quickly results return",
      "Turnaround time is not the stated driver."],
     ["Education has little effect once the order has been placed",
      "The opposite is stated."]],
   c=0, cite=c(14)),

 dict(topic="Patient counseling", io=IOB,
   q="Which elements should patient education about a diagnostic test include?",
   opts=[
     ["The testing process, answers to their questions, and the anticipated timeline for results",
      "Correct — all three are named as part of pretest patient and family education."],
     ["Only the preparation instructions, since the rest follows after results",
      "The timeline and the opportunity to ask questions are also included."],
     ["Only the cost, since that is what most affects the decision",
      "Cost is considered by the clinician, but education is broader."],
     ["Only the risks, since consent is the legal requirement",
      "Consent is one element among several."]],
   c=0, cite=c(8)),

 dict(topic="Patient counseling", io=IOB,
   q="Why does understanding a patient's perceptions and anxieties about testing matter?",
   opts=[
     ["It allows communication on a deeper level so that a therapeutic relationship can develop",
      "Correct. Empathy is expected throughout all phases of testing."],
     ["It allows the clinician to decide whether to disclose the result",
      "Results are communicated clearly and sensitively, not withheld on this basis."],
     ["It determines whether consent is legally required",
      "Consent requirements do not depend on the patient's anxiety level."],
     ["It identifies patients who should be referred before any testing",
      "This is not the stated purpose."]],
   c=0, cite=c(14)),

 dict(topic="Patient counseling", io=IOB,
   q="Which factors should be considered when communicating about diagnostic testing?",
   opts=[
     ["Ethnicity, culture, gender and age",
      "Correct — these are named alongside preparing the patient properly and following standards."],
     ["Only the patient's stated educational level",
      "The list is broader than education alone."],
     ["Only whether an interpreter is required",
      "Language access matters but is not the full list."],
     ["Only the urgency of the clinical situation",
      "Urgency does not replace individualised communication."]],
   c=0, cite=c(15)),

 dict(topic="Phases", io=IOC,
   q="What are the three phases of the diagnostic testing process, in order?",
   opts=[
     ["Pretest, intratest, posttest",
      "Correct — also called the preanalytical, analytical and postanalytical phases."],
     ["Preanalytical, postanalytical, analytical",
      "The analytical phase is the middle one, not the last."],
     ["Screening, diagnostic, confirmatory",
      "These describe test purposes rather than the phases of the process."],
     ["Collection, transport, interpretation",
      "These are steps within phases rather than the phases themselves."]],
   c=0, cite=c(7)),

 dict(topic="Phases", io=IOC,
   q="Which term corresponds to the intratest phase?",
   opts=[
     ["The analytical phase",
      "Correct. Pretest is preanalytical and posttest is postanalytical."],
     ["The preanalytical phase",
      "That is the pretest phase."],
     ["The postanalytical phase",
      "That is the posttest phase."],
     ["The interpretive phase",
      "No such phase is named."]],
   c=0, cite=c(10)),

 dict(topic="Phases", io=IOC,
   q="When does the pretest phase begin and end?",
   opts=[
     ["It begins with patient preparation and extends until the diagnostic test begins",
      "Correct — preparation through to the moment the test starts."],
     ["It begins when the order is placed and ends when the specimen reaches the laboratory",
      "The phase ends when the test itself begins, not at laboratory receipt."],
     ["It begins at the patient's arrival and ends when consent is signed",
      "Consent is one component within the phase rather than its endpoint."],
     ["It begins when the specimen is collected and ends when it is analysed",
      "That describes the intratest phase."]],
   c=0, cite=c(8)),

 dict(topic="Phases", io=IOC,
   q="When does the posttest phase begin?",
   opts=[
     ["Once the test is complete, focusing on patient aftercare",
      "Correct — aftercare, interpretation, communication and follow-up."],
     ["Once the result has been communicated to the patient",
      "Communication happens within the phase rather than starting it."],
     ["Once the specimen has been transported to the laboratory",
      "That falls within the intratest phase."],
     ["Once follow-up testing has been ordered",
      "Ordering follow-up is a component of the phase, not its start."]],
   c=0, cite=c(11)),

 dict(topic="Phases", io=IOD,
   q="During which phase of testing do most errors occur?",
   opts=[
     ["The pretest phase",
      "Correct, and this is why preparation, labeling and communication receive so much attention."],
     ["The intratest phase",
      "Errors occur here but this is not where most occur."],
     ["The posttest phase",
      "Communication errors occur here, but the pretest phase carries the most."],
     ["Errors are distributed evenly across the three phases",
      "They are not; the pretest phase predominates."]],
   c=0, cite=c(9)),

 dict(topic="Phases", io=IOD,
   q="Which of the following is a technical error of the pretest phase?",
   opts=[
     ["Inadequate blood in the vacuum tube",
      "Correct. Delay in transport and inappropriate storage are the other technical errors listed."],
     ["Failure to identify a critical value",
      "That belongs to the posttest phase."],
     ["Failure to monitor vital signs during the procedure",
      "That belongs to the intratest phase."],
     ["Failure to schedule appropriate follow-up",
      "That belongs to the posttest phase."]],
   c=0, cite=c(9)),

 dict(topic="Phases", io=IOD,
   q="A patient arrives for a test that required fasting but has eaten breakfast. Which category of pretest error is this?",
   opts=[
     ["Inappropriate patient preparation",
      "Correct — fasting is the example given for this error category."],
     ["A technical error",
      "Technical errors are things like inadequate tube fill and transport delay."],
     ["A communication error",
      "Communication failure may be the cause, but the error category named for fasting is patient preparation."],
     ["A postanalytical error",
      "The error has occurred before the test begins."]],
   c=0, cite=c(9)),

 dict(topic="Phases", io=IOD,
   q="Which of the following is listed as a variable that can affect laboratory results?",
   opts=[
     ["Time of specimen collection",
      "Correct. The list also includes patient preparation, current drug therapy, physical activity, hydration, age, sex and body mass index."],
     ["The patient's insurance carrier",
      "Reimbursement is a pretest consideration but does not alter results."],
     ["The ordering clinician's specialty",
      "This is not among the variables listed."],
     ["Whether the test was ordered electronically",
      "The ordering method is not a listed variable."]],
   c=0, cite=c(9)),

 dict(topic="Phases", io=IOD,
   q="Which activity belongs to the intratest phase?",
   opts=[
     ["Monitoring vital signs and administering analgesics or sedatives during the procedure",
      "Correct — the intratest phase covers performing the test and everything it encompasses."],
     ["Identifying contraindications to the test",
      "That is a pretest consideration."],
     ["Ordering appropriate follow-up laboratory studies",
      "That belongs to the posttest phase."],
     ["Assessing the patient's coping styles, fears and phobias",
      "That is a pretest consideration."]],
   c=0, cite=c(10)),

 dict(topic="Phases", io=IOD,
   q="Which activities are named for the intratest phase alongside performing the procedure?",
   opts=[
     ["Providing emotional and physical comfort, observing universal precautions, and minimizing delays",
      "Correct, along with monitoring the testing environment and watching for complications."],
     ["Obtaining consent and reviewing contraindications",
      "Both belong to the pretest phase."],
     ["Interpreting results and identifying critical values",
      "Both belong to the posttest phase."],
     ["Arranging referrals and considering emotional well-being",
      "Both belong to posttest integration and follow-up."]],
   c=0, cite=c(10)),

 dict(topic="Phases", io=IOD,
   q="Which complications should be monitored for during the posttest phase?",
   opts=[
     ["Bleeding, infection, respiratory difficulties, perforation, and adverse effects of sedation or anesthesia",
      "Correct — these five are the named posttest complications."],
     ["Only bleeding at the puncture site",
      "The list is considerably broader."],
     ["Only adverse effects of sedation",
      "Sedation effects are one item among five."],
     ["Only laboratory errors in the reported value",
      "Result errors matter but are not the complications named."]],
   c=0, cite=c(11)),

 dict(topic="Phases", io=IOD,
   q="A significant abnormal result returns. Which posttest responsibility does this trigger?",
   opts=[
     ["Identify and treat critical values, and communicate results clearly and sensitively",
      "Correct. Behavioural responses to a significant diagnosis may last several weeks or longer."],
     ["Repeat the test before informing the patient of anything",
      "Repeating is not the stated posttest responsibility."],
     ["Defer communication until the follow-up appointment",
      "Results are communicated clearly and sensitively rather than deferred by default."],
     ["Refer immediately without interpreting the result",
      "Interpretation of the result and the patient's response is a posttest responsibility."]],
   c=0, cite=c(11)),

 dict(topic="Phases", io=IOD,
   q="What does the integration component of the posttest phase refer to?",
   opts=[
     ["Diagnosis, subsequent acceptance, healing, and health-promoting behavior",
      "Correct — it includes patient education for the diagnosis and treatment plan."],
     ["Combining results from several laboratories into one record",
      "Integration here refers to the patient's process, not to data merging."],
     ["Entering results into the electronic health record",
      "That is documentation rather than integration."],
     ["Reconciling the result against the pretest probability",
      "That is a separate concept from the integration phase."]],
   c=0, cite=c(12)),

 dict(topic="Phases", io=IOD,
   q="Which principle is stated about documentation in the posttest phase?",
   opts=[
     ["“If it wasn't documented, it wasn't done”",
      "Correct — detailed documentation is described as essential to accurate record keeping and reporting."],
     ["Documentation may be deferred until results are final",
      "Detailed documentation is expected rather than deferred."],
     ["Only abnormal results require documentation",
      "Accurate record keeping applies regardless of the result."],
     ["Verbal handoff is sufficient when the result is communicated directly",
      "Detailed documentation is described as essential."]],
   c=0, cite=c(12)),

 dict(topic="Phases", io=IOD,
   q="Which posttest activities are grouped under integration and follow-up?",
   opts=[
     ["Ordering appropriate follow-up laboratory studies, scheduling follow-up, and making appropriate referrals",
      "Correct, alongside patient education and consideration of emotional well-being."],
     ["Monitoring vital signs and administering sedation",
      "Both belong to the intratest phase."],
     ["Reviewing history and identifying contraindications",
      "Both belong to the pretest phase."],
     ["Selecting the collection tube and the order of draw",
      "That is a specimen-collection matter within the intratest phase."]],
   c=0, cite=c(12)),

 dict(topic="Phases", io=IOD,
   q="Which of the following is a pretest consideration?",
   opts=[
     ["Ethical and legal considerations, including consent",
      "Correct — listed alongside history review, contraindications, coping styles, universal precautions, documentation and cost."],
     ["Monitoring for perforation after the procedure",
      "That is a posttest complication."],
     ["Interpreting the test result and the patient's response",
      "That belongs to the posttest phase."],
     ["Minimizing delays in specimen handling during collection",
      "That belongs to the intratest phase."]],
   c=0, cite=c(8)),

 dict(topic="Effective testing", io=IOB,
   q="Which practice is named as part of delivering effective diagnostic testing services?",
   opts=[
     ["Managing diagnostic services using a team approach",
      "Correct, alongside communicating clearly, preparing the patient, following standards, measuring outcomes and maintaining records."],
     ["Restricting result interpretation to the ordering clinician alone",
      "A team approach is what is described."],
     ["Ordering the broadest available panel to avoid missing anything",
      "Appropriateness and cost effectiveness are the stated considerations."],
     ["Standardising communication so that every patient receives the same script",
      "Communication is adapted to ethnicity, culture, gender and age."]],
   c=0, cite=c(15)),
]
