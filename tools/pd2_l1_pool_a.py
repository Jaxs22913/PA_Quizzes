# Physical Diagnosis 2, Lecture 1 (Introduction to Physical Diagnosis II) — pool
#
# ONE 15-question quiz, not the house 2x30 (Jaxon, 2026-08-18). The deck is
# largely course orientation -- OSCE logistics, grade weightings, small-group
# timings, file naming, professionalism -- and he ruled that out: "If its stuff
# about how the course works you dont have to include that." What survives is
# genuinely clinical: the oral case presentation, focused versus comprehensive
# history, and the documentation principles. That is about twenty questions
# written, fifteen selected. Padding it would mean exactly the deck-dependent
# trivia he also ruled out.
#
# STANDING RULE: no question may depend on having the deck open. Read it cold --
# if someone who knows the material can answer it with no slides, it is fair.
SRC = "Intro to PD II - Elwaya .pdf"
def c(n): return f"{SRC}, Page {n}"

IOC = "c — Clinical reasoning in oral presentations"
IOE = "e — Comprehensive versus focused history and examination"
IOG = "g — Documentation of a complete history and physical examination"
IOH = "h — Involving the patient in healthcare communication"

POOL_A = [
 dict(topic="Oral presentation", io=IOC,
   q="What should the opening statement of an oral case presentation include?",
   opts=[
     ["The past medical history and the chief complaint",
      "Correct — those two orient the listener before any detail follows."],
     ["The diagnosis and the proposed treatment plan",
      "Those belong at the end; opening with them removes the reasoning the listener is meant to follow."],
     ["The complete review of systems, system by system",
      "A presentation carries pertinent positives and negatives, not the entire review."],
     ["The laboratory and imaging results obtained so far",
      "Results come later in the presentation, not in the opening statement."]],
   c=0, cite=c(9)),

 dict(topic="Oral presentation", io=IOC,
   q="Which findings belong in an oral case presentation?",
   opts=[
     ["Pertinent positives and negatives from both the history and the physical examination",
      "Correct. Choosing what counts as pertinent is the clinical reasoning being assessed."],
     ["Every finding obtained, whether positive or negative",
      "A presentation is a selected vignette rather than a complete transcript of the encounter."],
     ["Only the abnormal findings, since normal findings add nothing",
      "Pertinent negatives carry as much weight as positives in narrowing a differential."],
     ["Only the physical examination findings, since the history is documented separately",
      "Both the history and the examination contribute to the presentation."]],
   c=0, cite=c(9)),

 dict(topic="Oral presentation", io=IOC,
   q="What is the test of whether an oral case presentation was a good one?",
   opts=[
     ["It leads the listener to the same differential the presenter formulated",
      "Correct — a functional test rather than a stylistic one, and the sharpest single criterion given."],
     ["It lasts less than two minutes from start to finish",
      "Length is not the measure of whether a presentation succeeded."],
     ["It includes every element contained in the written note",
      "A presentation is a vignette, not the note read aloud."],
     ["It avoids all medical terminology in favour of plain language",
      "Plain language matters with patients, not in a case presentation to a colleague."]],
   c=0, cite=c(9)),

 dict(topic="Oral presentation", io=IOC,
   q="What is the provider's goal when delivering an oral case presentation?",
   opts=[
     ["To help the listeners visualise the patient and understand the problem",
      "Correct, which is why it should be a well-organised vignette describing the patient and the clinical problem."],
     ["To demonstrate the thoroughness of the history that was obtained",
      "Completeness is not the aim of a presentation; comprehension by the listener is."],
     ["To justify each diagnostic test that was ordered for the patient",
      "Justifying information requests is a separate skill from presenting the case."],
     ["To create a permanent record of the encounter for the chart",
      "That is the job of the written note rather than the spoken presentation."]],
   c=0, cite=c(9)),

 dict(topic="Oral presentation", io=IOC,
   q="In what order should an oral case presentation generally proceed?",
   opts=[
     ["Mostly the order in which the history was obtained and the examination performed",
      "Correct. Following the encounter's own sequence is what makes it easy to follow."],
     ["In reverse, opening with the diagnosis and working back to the evidence",
      "The presentation builds toward the assessment rather than announcing it first."],
     ["Grouped by body system in alphabetical order",
      "No such convention applies to case presentations."],
     ["Physical examination findings first, then the history that prompted them",
      "The order should track how the encounter actually ran."]],
   c=0, cite=c(9)),

 dict(topic="Oral presentation", io=IOC,
   q="What advice is given about using notes while presenting a case?",
   opts=[
     ["Try not to read from them",
      "Correct — reading works directly against helping the listener visualise the patient."],
     ["Read from them verbatim so that no detail is omitted",
      "The advice is the opposite; verbatim reading defeats the purpose."],
     ["Notes are not permitted during a case presentation at all",
      "The guidance is to avoid reading from them, not that they are banned outright."],
     ["Hand the notes to the listener rather than presenting aloud",
      "The presentation is delivered verbally."]],
   c=0, cite=c(9)),

 dict(topic="Focused encounter", io=IOE,
   q="Which components of the history are taken in focused rather than comprehensive form during a focused encounter?",
   opts=[
     ["History of present illness, review of systems, past medical history and social history",
      "Correct — all four are narrowed, alongside family history, medications and allergies."],
     ["Only the history of present illness, with everything else taken in full",
      "Several components are narrowed, not just one."],
     ["Only the review of systems and the family history",
      "The focused approach applies more broadly than those two."],
     ["None — a focused encounter narrows the examination but never the history",
      "The history is focused as well as the examination."]],
   c=0, cite=c(7)),

 dict(topic="Focused encounter", io=IOE,
   q="Beyond taking a history and examining the patient, what else must be produced in a focused clinical encounter?",
   opts=[
     ["Differentials, laboratory and imaging studies, a diagnosis, and a treatment plan including patient education",
      "Correct. The encounter tests the whole reasoning chain rather than data gathering alone."],
     ["A diagnosis and a prescription, with the reasoning left implicit",
      "The required output is considerably broader than a diagnosis and a prescription."],
     ["A written history and physical document completed afterwards",
      "The written note is a separate piece of work from the encounter itself."],
     ["A referral letter to the appropriate specialist",
      "Referral is not among the required components."]],
   c=0, cite=c(7)),

 dict(topic="Communication", io=IOH,
   q="When a third party supplies the patient's responses during an assessed encounter, where should your attention stay?",
   opts=[
     ["On the patient, interacting with the patient rather than the person supplying the answers",
      "Correct, and it is stated emphatically. The encounter is with the patient even when the words come from elsewhere."],
     ["On whoever is supplying the answers, since that is the source of information",
      "The instruction is the opposite: always look at and interact with the patient."],
     ["On the documentation form, so that responses are recorded accurately",
      "Attention is meant to stay with the patient throughout."],
     ["Divided evenly between the patient and the person answering",
      "The instruction is unambiguous about interacting with the patient."]],
   c=0, cite=c(8)),

 dict(topic="Documentation", io=IOG,
   q="How should physical examination findings be recorded in a written clinical note?",
   opts=[
     ["Describe what was found, rather than writing normal, abnormal or unremarkable",
      "Correct — a description communicates what was actually observed, where a label does not."],
     ["Use unremarkable wherever nothing is wrong, to keep the note concise",
      "That is precisely the shortcut the guidance warns against."],
     ["Record only the abnormal findings and omit the normal ones entirely",
      "Description is expected rather than omission."],
     ["Assign each system a numeric score on a standard scale",
      "No scoring system of that kind is used."]],
   c=0, cite=c(20)),

 dict(topic="Documentation", io=IOG,
   q="What is the rule on abbreviations in written clinical assignments?",
   opts=[
     ["No abbreviations",
      "Correct, and it is stated without qualification."],
     ["Abbreviations are acceptable once defined on first use",
      "No such allowance is made."],
     ["Only widely recognised medical abbreviations may be used",
      "The instruction admits no exceptions."],
     ["Abbreviations are encouraged wherever they shorten the note",
      "The opposite is instructed."]],
   c=0, cite=c(20)),

 dict(topic="Documentation", io=IOG,
   q="What must be done if part of the examination was not performed?",
   opts=[
     ["Document why it was not done — findings may never be invented",
      "Correct. Recording something you did not do is the one error the guidance treats as absolute."],
     ["Record the finding that would be expected if it were normal",
      "That is fabricating a finding, which is expressly prohibited."],
     ["Leave the section blank without further comment",
      "The reason for the omission has to be documented."],
     ["Obtain the finding from a classmate who examined the same patient",
      "A note may not be written with another student, and the finding would still not be yours."]],
   c=0, cite=c(20)),

 dict(topic="Documentation", io=IOG,
   q="How should subjective and objective information be arranged in a note?",
   opts=[
     ["Each kept in its own appropriate section, not mixed together",
      "Correct — blending them is one of the commonest documentation errors."],
     ["Combined into a single narrative so the encounter reads chronologically",
      "They belong in their own sections."],
     ["Subjective information may be omitted when the examination is complete",
      "Both are required regardless of how complete the examination was."],
     ["Objective findings recorded within the assessment section",
      "Objective findings belong in the objective section."]],
   c=0, cite=c(20)),

 dict(topic="Documentation", io=IOG,
   q="Why can reusing your own earlier written work create an academic integrity problem?",
   opts=[
     ["Work is not original when it has already been submitted for academic credit, whether by you or anyone else",
      "Correct — which is why reusing a template from a previous assignment carries a warning."],
     ["Earlier work may contain clinical guidance that has since changed",
      "The concern is originality rather than currency of the content."],
     ["Reused documents often carry formatting errors",
      "The caution is about academic integrity, not formatting."],
     ["Faculty cannot grade the same document twice",
      "The issue is the originality standard, not grading logistics."]],
   c=0, cite=c(22)),

 dict(topic="Communication", io=IOH,
   q="How should communication style be handled across different patients?",
   opts=[
     ["Adapt the style and content of communication appropriately for each patient",
      "Correct — communication is expected to change to suit the patient rather than following one fixed script."],
     ["Use consistent phrasing with every patient so nothing is missed",
      "Adaptation, not uniformity, is the stated expectation."],
     ["Match the register of whoever referred the patient",
      "The expectation concerns the patient in front of you."],
     ["Keep communication strictly to the presenting clinical question",
      "No such restriction is described."]],
   c=0, cite=c(23)),

 dict(topic="Communication", io=IOH,
   q="How should a student handle feedback that differs between facilitators?",
   opts=[
     ["Accept the constructive feedback and modify behaviour, recognising that different facilitators give different feedback",
      "Correct — the variation is anticipated rather than treated as a contradiction to be resolved."],
     ["Follow only the most senior facilitator's feedback",
      "All constructive feedback is to be accepted and acted on."],
     ["Ask for a single standardised rubric to settle any disagreement",
      "Adaptation is expected rather than standardisation."],
     ["Disregard feedback that conflicts with earlier guidance",
      "Feedback is to be accepted and acted upon."]],
   c=0, cite=c(23)),

 dict(topic="Documentation", io=IOG,
   q="What should be reviewed before submitting a written clinical assignment?",
   opts=[
     ["The grading rubric, and the comments left on previous assignments",
      "Correct — prior feedback is the most direct guide to what still needs improving."],
     ["A classmate's completed version of the same assignment",
      "Notes may not be shared or written together."],
     ["The academic calendar and the course schedule",
      "Neither bears on the quality of the note."],
     ["Only the textbook chapter on documentation",
      "The rubric and prior feedback are what is specified."]],
   c=0, cite=c(20)),

 dict(topic="Focused encounter", io=IOE,
   q="What distinguishes a focused encounter from a comprehensive one?",
   opts=[
     ["The history and examination are both narrowed to what the presenting problem requires",
      "Correct — a focused encounter is not a shorter version of everything, it is a targeted selection."],
     ["The examination is narrowed but the history remains complete",
      "Both are narrowed in a focused encounter."],
     ["The history is narrowed but every system is still examined",
      "The examination is focused as well."],
     ["The encounter is identical but documented more briefly",
      "The difference is in what is gathered, not only in how it is written up."]],
   c=0, cite=c(7)),
]
