# Principles of Diagnostic Medicine I, Lecture 1 — pool B
# Collection tubes, stool/blood/sputum/throat studies, and point-of-care testing.
# Syllabus objectives e, f, g, h.
#
# TUBE SCOPE, narrowed by Professor Reynolds herself: "the thing I want you to
# know better, have a better handle on, is kind of the ORDER and sort of the
# BROAD CATEGORY -- so light blue, think coags; lavender, we're gonna be using
# this for like our CBC." The deck carries a full additive-by-stopper-colour
# table running to two dozen rows; she does not want it memorised. Questions
# here therefore test order of draw and the common colour-to-test pairings, not
# the exhaustive additive table.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "1. Principles of Laboratory Diagnostics sv.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOE = "Objective e — Colored laboratory collection tubes and their corresponding tests"
IOF = "Objective f — Purpose and appropriate use of stool, throat, sputum and blood studies"
IOG = "Objective g — Definition of point-of-care testing"
IOH = "Objective h — Common point-of-care tests in primary care and acute care"

POOL_B = [
 dict(topic="Collection tubes", io=IOE,
   q="Why does the order of draw matter when collecting multiple specimens?",
   opts=[
     ["To avoid cross-contamination of additives between tubes and ensure accuracy",
      "Correct — that is the stated reason the sequence exists."],
     ["To reduce the total volume of blood drawn from the patient",
      "The order does not change the volume required."],
     ["To shorten the time the tourniquet remains in place",
      "Tourniquet time matters clinically but is not why the order is specified."],
     ["To allow the tubes to be labeled in a consistent sequence",
      "Labeling is a separate step from the draw order."]],
   c=0, cite=c(17)),

 dict(topic="Collection tubes", io=IOE,
   q="Which tube is drawn first when multiple specimens are collected?",
   opts=[
     ["Yellow, for blood cultures",
      "Correct — blood cultures come first, then light blue coagulation tubes, then non-additive, then additive tubes."],
     ["Light blue, for coagulation studies",
      "Light blue follows the blood culture tube."],
     ["Lavender, for the complete blood count",
      "Additive tubes such as lavender come last."],
     ["Red, the non-additive tube",
      "Non-additive tubes follow the coagulation tube."]],
   c=0, cite=c(17)),

 dict(topic="Collection tubes", io=IOE,
   q="You are ordering coagulation studies. Which tube should the specimen arrive in?",
   opts=[
     ["Light blue",
      "Correct — light blue contains sodium citrate and is the coagulation tube."],
     ["Lavender",
      "Lavender contains ethylenediaminetetraacetic acid and is used for the complete blood count."],
     ["Gray",
      "Gray contains a glycolytic inhibitor."],
     ["Green",
      "Green is a heparin tube."]],
   c=0, cite=c(16)),

 dict(topic="Collection tubes", io=IOE,
   q="A complete blood count is ordered. Which tube colour corresponds to it?",
   opts=[
     ["Lavender",
      "Correct. Lavender tubes contain ethylenediaminetetraacetic acid."],
     ["Light blue",
      "Light blue is the sodium citrate coagulation tube."],
     ["Yellow",
      "Yellow contains sterile media for blood culture."],
     ["Gray",
      "Gray contains a glycolytic inhibitor."]],
   c=0, cite=c(16)),

 dict(topic="Collection tubes", io=IOE,
   q="Which additive does the light blue tube contain?",
   opts=[
     ["Sodium citrate",
      "Correct, and it requires three to four inversions."],
     ["Ethylenediaminetetraacetic acid",
      "That is in the lavender tube."],
     ["Sodium heparin",
      "That is in tan and royal blue tubes."],
     ["A glycolytic inhibitor",
      "That is in the gray tube."]],
   c=0, cite=c(16)),

 dict(topic="Collection tubes", io=IOE,
   q="What is the purpose of the clear tube in the order of draw?",
   opts=[
     ["It is a discard tube used to fill collection set spaces before the coagulation tube",
      "Correct — it is nonadditive and is used when no royal blue tube is collected."],
     ["It is the tube used for trace metal studies",
      "Trace metal studies use the royal blue tube."],
     ["It is the tube used for blood cultures",
      "Blood cultures use the yellow tube with sterile media."],
     ["It is the serum separator tube",
      "That is gold or red."]],
   c=0, cite=c(16)),

 dict(topic="Stool studies", io=IOF,
   q="A patient is to collect a stool specimen for ova and parasites at home. What instruction must you give about storage?",
   opts=[
     ["Do not refrigerate it — warm stool is best for detecting ova and parasites",
      "Correct, and it is worth saying explicitly, because patients refrigerate it by instinct."],
     ["Refrigerate it immediately to preserve the organisms",
      "Refrigeration is exactly what must be avoided for this study."],
     ["Freeze it if transport will be delayed more than an hour",
      "Freezing is not advised; the specimen should stay at room temperature or warm."],
     ["Store it in preservative solution and refrigerate",
      "The instruction is not to refrigerate."]],
   c=0, cite=c(21)),

 dict(topic="Stool studies", io=IOF,
   q="Why are three separate random stool specimens recommended for ova and parasite testing?",
   opts=[
     ["Because of the life cycle of parasites, which increases the likelihood of detection",
      "Correct — organisms are shed intermittently, so a single specimen can miss them."],
     ["Because each specimen tests for a different class of organism",
      "All three are the same test; the repetition addresses intermittent shedding."],
     ["Because the first specimen is always discarded as contaminated",
      "No specimen is routinely discarded."],
     ["Because laboratories require a minimum volume across three containers",
      "Volume is not the reason for three specimens."]],
   c=0, cite=c(21)),

 dict(topic="Stool studies", io=IOF,
   q="What must a stool specimen be free of?",
   opts=[
     ["Urine or other bodily secretions such as menstrual blood",
      "Correct, and it must be collected into a dry, clean container."],
     ["Any trace of normal gut flora",
      "Normal flora is expected; overgrowth of it is one of the things sought."],
     ["Dietary fibre residue",
      "No dietary restriction of this kind is specified for collection."],
     ["Water from the toilet bowl only",
      "Urine and other secretions are named specifically, not only water."]],
   c=0, cite=c(20)),

 dict(topic="Stool studies", io=IOF,
   q="Which finding indicates a positive guaiac test?",
   opts=[
     ["The sample turns blue",
      "Correct — heme causes rapid oxidation of hydrogen peroxide in the guaiac, turning it blue."],
     ["The sample turns red",
      "Blue, not red, indicates a positive result."],
     ["The sample turns yellow",
      "That is not the guaiac endpoint."],
     ["No colour change occurs",
      "Absence of colour change is a negative result."]],
   c=0, cite=c(21)),

 dict(topic="Stool studies", io=IOF,
   q="How large a stool sample should be applied to a guaiac card?",
   opts=[
     ["A small sample — a large one obscures the result",
      "Correct. More is not better here."],
     ["A large sample, to maximise sensitivity",
      "A large sample obscures results."],
     ["Enough to fill the window completely",
      "Filling the window obscures the colour change."],
     ["The sample size does not affect interpretation",
      "It does; the guidance is explicit."]],
   c=0, cite=c(21)),

 dict(topic="Stool studies", io=IOF,
   q="Which of the following is an indication for stool studies?",
   opts=[
     ["Recent travel, consumption of well water, or prolonged antibiotic use",
      "Correct, alongside diarrhea, excessive flatus, abdominal discomfort and change in stool color."],
     ["Unexplained weight gain",
      "This is not among the indications listed."],
     ["Chronic cough with sputum production",
      "That points to a sputum culture."],
     ["Fever with suspected bloodstream infection",
      "That points to blood cultures."]],
   c=0, cite=c(20)),

 dict(topic="Blood cultures", io=IOF,
   q="A patient presents with an acute febrile illness and suspected septicemia. How should blood cultures be collected?",
   opts=[
     ["Two separate samples from opposite arms, ideally before starting antibiotic therapy",
      "Correct, and the aerobic sample is drawn first."],
     ["A single large-volume sample from either arm before antibiotics",
      "Two separate samples from opposite arms are required."],
     ["Two samples from the same arm, thirty minutes apart",
      "They should come from opposite arms."],
     ["A single sample drawn after the first antibiotic dose",
      "Cultures should be obtained before antibiotics wherever possible."]],
   c=0, cite=c(23)),

 dict(topic="Blood cultures", io=IOF,
   q="Why are blood cultures described as both diagnostic and therapeutic?",
   opts=[
     ["They identify the pathogen and provide sensitivities that direct antibiotic selection",
      "Correct — the sensitivities are what make the result therapeutically useful."],
     ["They remove circulating organisms during the draw",
      "Drawing blood does not clear an infection."],
     ["They allow antibiotics to be infused through the same line",
      "That is unrelated to why the culture is described this way."],
     ["They confirm the diagnosis without further testing in every case",
      "The therapeutic value comes from the sensitivities, not from finality."]],
   c=0, cite=c(23)),

 dict(topic="Blood cultures", io=IOF,
   q="After the puncture site has been disinfected for a blood culture, what must be avoided?",
   opts=[
     ["Palpating the site, unless sterile gloves are worn",
      "Correct — palpating after disinfection recontaminates the site."],
     ["Allowing the antiseptic to dry before puncture",
      "The antiseptic should be allowed to dry."],
     ["Drawing the aerobic bottle first",
      "The aerobic sample is drawn first."],
     ["Using the opposite arm for the second sample",
      "Opposite arms are exactly what is required."]],
   c=0, cite=c(23)),

 dict(topic="Sputum culture", io=IOF,
   q="What are the two steps of a sputum culture?",
   opts=[
     ["A Gram stain to establish Gram-positive versus Gram-negative, then culture for identification and sensitivities",
      "Correct — the stain gives early information while the culture grows."],
     ["Culture first, then a Gram stain on the isolated colonies",
      "The Gram stain is performed first."],
     ["An acid-fast stain followed by antigen testing",
      "Acid-fast bacilli testing can also be performed but is not the two-step sequence described."],
     ["Direct antigen testing followed by polymerase chain reaction",
      "Neither is the described sequence."]],
   c=0, cite=c(25)),

 dict(topic="Sputum culture", io=IOF,
   q="How should a patient be prepared to produce a sputum specimen?",
   opts=[
     ["Sit upright, rinse the mouth with water, then take three deep breaths and produce a deep cough",
      "Correct — rinsing reduces contamination by mouth flora."],
     ["Lie flat and cough gently into the container",
      "The patient should sit upright."],
     ["Rinse with antiseptic mouthwash before expectorating",
      "Water is specified; antiseptic would affect the culture."],
     ["Collect the first saliva produced on waking",
      "Saliva is not sputum; the specimen must come from deep in the airways."]],
   c=0, cite=c(25)),

 dict(topic="Sputum culture", io=IOF,
   q="What may be used to help a patient who cannot produce a sputum specimen?",
   opts=[
     ["Aerosols such as sterile water, saline or albuterol",
      "Correct — these help loosen and induce secretions."],
     ["Chest percussion alone, without any aerosol",
      "Aerosols are the named aid."],
     ["A prolonged breath hold before coughing",
      "This is not the described technique."],
     ["Delaying collection until the following morning",
      "Delay is not the recommended solution."]],
   c=0, cite=c(25)),

 dict(topic="Throat culture", io=IOF,
   q="Which organism is a throat culture most often obtained to identify?",
   opts=[
     ["Streptococci, because of the risk of beta-hemolytic streptococcal pharyngitis",
      "Correct — most commonly affecting children aged three to fifteen years."],
     ["Staphylococcus aureus, because of the risk of toxin production",
      "Streptococci are the named target."],
     ["Haemophilus influenzae, because of the risk of epiglottitis",
      "This organism is not the stated focus of the throat culture."],
     ["Candida albicans, because of the risk of thrush",
      "This is not the stated focus."]],
   c=0, cite=c(26)),

 dict(topic="Throat culture", io=IOF,
   q="How should the swab be applied when obtaining a throat culture?",
   opts=[
     ["Rotate it firmly and gently over the posterior throat, both tonsils, and any areas of inflammation, exudation or ulceration",
      "Correct, and the tongue and lips must not be touched."],
     ["Swab the anterior tongue and the inner cheeks",
      "Touching the tongue is specifically to be avoided."],
     ["Swab a single tonsil to minimise the gag reflex",
      "Both tonsils and the posterior throat are sampled."],
     ["Swab the soft palate only, avoiding the tonsils",
      "The tonsils are part of what is sampled."]],
   c=0, cite=c(26)),

 dict(topic="Throat culture", io=IOF,
   q="Why is a tongue blade used during a throat culture?",
   opts=[
     ["To increase visualization of the pharynx, relax the throat muscles and decrease the gag reflex",
      "Correct — all three purposes are named."],
     ["To collect the specimen directly from the tongue surface",
      "The specimen comes from the pharynx and tonsils."],
     ["To keep the patient from swallowing during collection",
      "This is not the stated purpose."],
     ["To protect the clinician from exposure",
      "Personal protective equipment serves that purpose."]],
   c=0, cite=c(26)),

 dict(topic="Cultures — general", io=IOF,
   q="Which principle applies to throat, sputum and blood cultures alike?",
   opts=[
     ["Obtain the specimen before initiating antibiotics whenever possible",
      "Correct — stated for all three, since antibiotics reduce the yield."],
     ["Refrigerate the specimen immediately after collection",
      "Refrigeration is discussed for stool ova and parasites, where it is prohibited."],
     ["Collect three separate specimens on consecutive days",
      "Three specimens are recommended for stool ova and parasites, not for these cultures."],
     ["Send the specimen only after the patient becomes febrile",
      "Fever is an indication for blood cultures but not a universal rule."]],
   c=0, cite=c(25)),

 dict(topic="Point-of-care testing", io=IOG,
   q="How is point-of-care testing defined?",
   opts=[
     ["Medical testing completed outside the centralized laboratory, at or close to the site of patient care",
      "Correct — also called near-patient, remote, satellite laboratory testing or rapid diagnostics."],
     ["Any laboratory test with a turnaround time under one hour",
      "The definition is about location, not speed alone."],
     ["Testing performed by a licensed clinician rather than a technologist",
      "Operator identity does not define it; many practitioners can perform it."],
     ["Testing that does not require a laboratory certificate",
      "All testing sites must be certified regardless of complexity."]],
   c=0, cite=c(27)),

 dict(topic="Point-of-care testing", io=IOG,
   q="Which feature of point-of-care testing is described as universal and inherent?",
   opts=[
     ["Results should align with established laboratory methods",
      "Correct, alongside simplicity of use, durable reagents, and safety during testing."],
     ["Results should be more precise than central laboratory methods",
      "Precision is listed among the limitations, not the strengths."],
     ["It should be performed only by licensed laboratory personnel",
      "It can be performed by a wide range of practitioners, and some tests by non-medical individuals."],
     ["It should replace central laboratory testing wherever available",
      "It complements rather than replaces central testing."]],
   c=0, cite=c(28)),

 dict(topic="Point-of-care testing", io=IOH,
   q="Which test is listed among common point-of-care tests in the acute care setting?",
   opts=[
     ["Troponin",
      "Correct, alongside venous blood gas, point-of-care glucose, brain natriuretic peptide and D-dimer."],
     ["Hemoglobin A1c",
      "That is listed under primary care."],
     ["Fecal occult blood",
      "That is listed under primary care."],
     ["Cholesterol",
      "That is listed under primary care."]],
   c=0, cite=c(29)),

 dict(topic="Point-of-care testing", io=IOH,
   q="Which test is listed among common point-of-care tests in primary care?",
   opts=[
     ["Hemoglobin A1c",
      "Correct, alongside blood glucose, urinalysis, rapid influenza, rapid strep, fecal occult blood, pregnancy testing, cholesterol, prothrombin time with international normalized ratio, and drug screening."],
     ["D-dimer",
      "That is listed under acute care."],
     ["Venous blood gas",
      "That is listed under acute care."],
     ["Brain natriuretic peptide",
      "That is listed under acute care."]],
   c=0, cite=c(30)),

 dict(topic="Point-of-care testing", io=IOH,
   q="Which portable machines are named as point-of-care devices?",
   opts=[
     ["Portable x-ray, electrocardiography, pulse oximetry and ultrasound",
      "Correct — point-of-care extends beyond laboratory assays to imaging and monitoring."],
     ["Portable magnetic resonance imaging and computed tomography",
      "Neither is named as a point-of-care machine."],
     ["Bench top chemistry analysers only",
      "Bench top devices are one category, but the portable machines named are broader."],
     ["Automated blood culture incubators",
      "These are central laboratory equipment."]],
   c=0, cite=c(29)),

 dict(topic="Point-of-care testing", io=IOH,
   q="Which two areas of point-of-care testing are noted as rapidly increasing?",
   opts=[
     ["Fentanyl testing and human immunodeficiency virus testing",
      "Correct — both are flagged as growing rapidly."],
     ["Cholesterol and hemoglobin A1c testing",
      "Both are common but are not the ones flagged as rapidly increasing."],
     ["Pregnancy and ovulation testing",
      "Neither is flagged in this way."],
     ["Rapid strep and rapid influenza testing",
      "Both are common but are not the flagged growth areas."]],
   c=0, cite=c(30)),
]
