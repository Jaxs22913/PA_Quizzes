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
# 2026-09-22: three more were course mechanics (facilitator feedback, the
# grading rubric, reusing your own work for academic credit). Jaxon: remove
# only, not replace -- the pool is now fifteen and the shipped quiz twelve.
# pd2_l1_partition.py asserts none of the three can come back.
# Every explanation refutes or confirms AND states the replacing fact from the
# deck, at least 60 characters (site rule, decided 2026-09-22).
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
      "Correct — a good oral case presentation leads the listener to the same differential the presenter formulated."],
     ["It lasts less than two minutes from start to finish",
      "Length is not the measure of whether a presentation succeeded."],
     ["It includes every element contained in the written note",
      "A presentation is a well-organized vignette of the patient and the clinical problem, not the written note read aloud."],
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
      "Alphabetical grouping is not used; a presentation mostly follows the order in which the history was obtained and the examination performed."],
     ["Physical examination findings first, then the history that prompted them",
      "Leading with the examination reverses the encounter; the history comes first because a presentation follows the order the encounter ran."]],
   c=0, cite=c(9)),

 dict(topic="Oral presentation", io=IOC,
   q="How should notes be used while presenting a case?",
   opts=[
     ["Try not to read from them",
      "Correct — reading works directly against helping the listener visualise the patient."],
     ["Read from them verbatim so that no detail is omitted",
      "Verbatim reading is exactly what to avoid; the presenter should try not to read from notes while presenting."],
     ["Notes are not permitted during a case presentation at all",
      "Notes are not banned outright; the point is to try not to read from them while presenting the case."],
     ["Hand the notes to the listener rather than presenting aloud",
      "The presenter delivers the case aloud to the listener; notes stay with the presenter, who tries not to read from them."]],
   c=0, cite=c(9)),

 dict(topic="Focused encounter", io=IOE,
   q="Which components of the history are taken in focused rather than comprehensive form during a focused encounter?",
   opts=[
     ["History of present illness, review of systems, past medical history and social history",
      "Correct — in a focused encounter the history of present illness, review of systems, past medical history and social history are all taken in focused form."],
     ["Only the history of present illness, with everything else taken in full",
      "The history of present illness is only one focused element; the review of systems, past medical history and social history are focused too."],
     ["Only the review of systems and the family history",
      "The review of systems is one focused element, but so are the history of present illness, the past medical history and the social history."],
     ["None — a focused encounter narrows the examination but never the history",
      "A focused encounter narrows the history too: the history of present illness, review of systems, past medical history and social history are all focused."]],
   c=0, cite=c(7)),

 dict(topic="Focused encounter", io=IOE,
   q="Beyond taking a history and examining the patient, what else must be produced in a focused clinical encounter?",
   opts=[
     ["Differentials, laboratory and imaging studies, a diagnosis, and a treatment plan including patient education",
      "Correct. The encounter tests the whole reasoning chain, from differentials and studies to a diagnosis and a treatment plan with patient education."],
     ["A diagnosis and a prescription, with the reasoning left implicit",
      "The required output is considerably broader than a diagnosis and a prescription."],
     ["A written history and physical document completed afterwards",
      "The written note is a separate piece of work from the encounter itself."],
     ["A referral letter to the appropriate specialist",
      "A referral letter is not required; the encounter instead calls for differentials, laboratory and imaging studies, a diagnosis and a treatment plan."]],
   c=0, cite=c(7)),

 dict(topic="Communication", io=IOH,
   q="When a third party supplies the patient's responses during an assessed encounter, where should your attention stay?",
   opts=[
     ["On the patient, interacting with the patient rather than the person supplying the answers",
      "Correct — you should always be looking at and interacting with the patient, even when the responses are supplied by someone else."],
     ["On whoever is supplying the answers, since that is the source of information",
      "The person supplying the answers is not the patient; you should always be looking at and interacting with the patient instead."],
     ["On the documentation form, so that responses are recorded accurately",
      "The documentation form is not the focus; you should always be looking at and interacting with the patient throughout the encounter."],
     ["Divided evenly between the patient and the person answering",
      "Attention is not split between them; you should always be looking at and interacting with the patient, not the person answering."]],
   c=0, cite=c(8)),

 dict(topic="Documentation", io=IOG,
   q="How should physical examination findings be recorded in a written clinical note?",
   opts=[
     ["Describe what was found, rather than writing normal, abnormal or unremarkable",
      "Correct — a description communicates what was actually observed, where a label does not."],
     ["Use unremarkable wherever nothing is wrong, to keep the note concise",
      "Unremarkable is one of the labels to avoid; findings are described in words instead of being written as normal, abnormal or unremarkable."],
     ["Record only the abnormal findings and omit the normal ones entirely",
      "Normal findings are still recorded; every finding is described in words rather than being labeled normal, abnormal or unremarkable."],
     ["Assign each system a numeric score on a standard scale",
      "Numeric scores are not used; findings are described in words instead of being labeled normal, abnormal or unremarkable."]],
   c=0, cite=c(20)),

 dict(topic="Documentation", io=IOG,
   q="What is the rule on abbreviations in written clinical assignments?",
   opts=[
     ["No abbreviations",
      "Correct — written clinical assignments use no abbreviations at all, with no exception for defined or widely known terms."],
     ["Abbreviations are acceptable once defined on first use",
      "Defining an abbreviation first does not make it acceptable; written clinical assignments allow no abbreviations at all."],
     ["Only widely recognised medical abbreviations may be used",
      "Common medical abbreviations are not exempt; written clinical assignments allow no abbreviations of any kind."],
     ["Abbreviations are encouraged wherever they shorten the note",
      "Abbreviations are not encouraged; written clinical assignments allow none, so every term is written out in full."]],
   c=0, cite=c(20)),

 dict(topic="Documentation", io=IOG,
   q="What must be done if part of the examination was not performed?",
   opts=[
     ["Document why it was not done — findings may never be invented",
      "Correct — history and examination findings may never be made up; if something was not done, the note documents why."],
     ["Record the finding that would be expected if it were normal",
      "Recording an expected finding for an untested part is making up a finding; the note must document why it was not done."],
     ["Leave the section blank without further comment",
      "A blank section leaves the omission unexplained; if part of the examination was not done, the note must document why."],
     ["Obtain the finding from a classmate who examined the same patient",
      "A note may not be written with another student, and the finding would still not be yours."]],
   c=0, cite=c(20)),

 dict(topic="Documentation", io=IOG,
   q="How should subjective and objective information be arranged in a note?",
   opts=[
     ["Each kept in its own appropriate section, not mixed together",
      "Correct — subjective and objective information are each kept in their appropriate sections of the note rather than blended."],
     ["Combined into a single narrative so the encounter reads chronologically",
      "A single chronological narrative mixes the two; subjective and objective information each belong in their own appropriate section."],
     ["Subjective information may be omitted when the examination is complete",
      "Both are required regardless of how complete the examination was."],
     ["Objective findings recorded within the assessment section",
      "Objective findings do not belong in the assessment; they are kept in the objective section, separate from subjective information."]],
   c=0, cite=c(20)),

 # REMOVED 2026-09-22 (Jaxon: remove only, not replace): course-mechanics question
 # "Why can reusing your own earlier written work create an academic integrity problem?"
 dict(topic="Communication", io=IOH,
   q="How should communication style be handled across different patients?",
   opts=[
     ["Adapt the style and content of communication appropriately for each patient",
      "Correct — communication is expected to change to suit the patient rather than following one fixed script."],
     ["Use consistent phrasing with every patient so nothing is missed",
      "Uniform phrasing is not the standard; a professional adapts the style and content of communication appropriately for each patient."],
     ["Match the register of whoever referred the patient",
      "The referrer's register is irrelevant; communication style and content are adapted appropriately for each patient being seen."],
     ["Keep communication strictly to the presenting clinical question",
      "Communication is not restricted to one question; its style and content are adapted appropriately to each individual patient."]],
   c=0, cite=c(23)),

 # REMOVED 2026-09-22 (Jaxon: remove only, not replace): course-mechanics question
 # "How should a student handle feedback that differs between facilitators?"
 # REMOVED 2026-09-22 (Jaxon: remove only, not replace): course-mechanics question
 # "What should be reviewed before submitting a written clinical assignment?"
 dict(topic="Focused encounter", io=IOE,
   q="What distinguishes a focused encounter from a comprehensive one?",
   opts=[
     ["The history and examination are both narrowed to what the presenting problem requires",
      "Correct — a focused encounter is not a shorter version of everything, it is a targeted selection."],
     ["The examination is narrowed but the history remains complete",
      "The history is not kept complete; in a focused encounter both the history and the physical examination are narrowed to the problem."],
     ["The history is narrowed but every system is still examined",
      "Every system is not examined; in a focused encounter the physical examination is narrowed as well as the history."],
     ["The encounter is identical but documented more briefly",
      "The difference is in what is gathered, not only in how it is written up."]],
   c=0, cite=c(7)),
]
