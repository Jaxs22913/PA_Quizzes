# -*- coding: utf-8 -*-
# PDM I Lecture 5 -- pool C. Glucose, blood urea nitrogen and creatinine
# (objective b, parts v-vii), and the liver studies on a chemistry panel
# (objective c).
#
# THE GLOMERULAR FILTRATION RATE IS NOT CALCULATED HERE. Reynolds, 26 August:
# "I don't need you to calculate that or know that just yet, but know OF it."
# Questions ask what the rate means and what it is derived from, never for the
# arithmetic. pdm_l5_partition.py asserts this.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "5. Chemistry Panels, Renal Fxn, Elytes.pptx"
def c(n): return f"{SRC}, Slide {n}"
def cn(n): return f"{SRC}, Slide {n} (speaker notes)"

IOB5 = "b(v) — Discuss the physiological role of glucose"
IOB6 = "b(vi) — Discuss the physiological role of blood urea nitrogen"
IOB7 = "b(vii) — Discuss the physiological role of creatinine"
IOC = "c — Discuss basic liver function studies included in chemistry testing"

POOL_C = [
 # ---- glucose ----
 dict(topic="Glucose", io=IOB5, slot="etiology",
   q="Which hormone lowers blood glucose, and which raise it?",
   opts=[
     ["Insulin lowers it; glucagon and the counter-regulatory hormones raise it",
      "Correct — the deck's pairing for glucose regulation."],
     ["Glucagon lowers it; insulin and cortisol raise it",
      "This reverses the roles of insulin and glucagon."],
     ["Cortisol lowers it; insulin and adrenaline raise it",
      "Cortisol is one of the counter-regulatory hormones that raise glucose."],
     ["Insulin lowers it; antidiuretic hormone raises it",
      "That hormone governs water handling, not glucose."]],
   c=0, cite=c(13)),

 dict(topic="Glucose", io=IOB5, slot="etiology",
   q="Besides the pancreatic hormones, which organ does the deck say contributes to glucose regulation, and how?",
   opts=[
     ["The kidney, through gluconeogenesis",
      "Correct — the deck credits the kidney with a gluconeogenic contribution."],
     ["The spleen, through glucose storage",
      "The spleen has no such role in the deck."],
     ["The thyroid, through its effect on metabolic rate",
      "Metabolic rate is not the mechanism the deck names here."],
     ["The adrenal medulla, through glycogen storage",
      "Glycogen is stored in liver and muscle, and the deck names gluconeogenesis."]],
   c=0, cite=c(13)),

 dict(topic="Glucose", io=IOB5, slot="test finding",
   q="Which piece of context does the deck say a glucose value must always be interpreted against?",
   opts=[
     ["Whether the patient was fasting or not",
      "Correct — the deck ties interpretation to the fasting state."],
     ["Whether the sample was taken from an artery or a vein",
      "The deck does not raise sampling site for glucose."],
     ["The time elapsed since the last insulin dose",
      "Relevant clinically, but not the context the deck specifies."],
     ["The patient's body mass index",
      "Not the interpretive context the deck gives."]],
   c=0, cite=c(13)),

 dict(topic="Glucose", io=IOB5, slot="test finding",
   q="What effect do the speaker notes say marked hyperglycaemia has on the measured sodium?",
   opts=[
     ["It lowers it, by dilution",
      "Correct — the notes describe a dilutional fall in measured sodium."],
     ["It raises it, by drawing water into the cells",
      "The water shift is out of the cells, which dilutes the sodium."],
     ["It leaves it unchanged but raises the potassium",
      "The notes describe an effect on sodium."],
     ["It makes the sodium unmeasurable until the glucose is corrected",
      "The sodium is measurable; it simply reads low."]],
   c=0, cite=cn(13)),

 # ---- blood urea nitrogen ----
 dict(topic="Blood urea nitrogen", io=IOB6, slot="etiology",
   q="What is blood urea nitrogen, and where is it produced and cleared?",
   opts=[
     ["A nitrogenous waste product of protein metabolism, produced by the liver and cleared by the kidneys",
      "Correct — the deck's full description of its origin and clearance."],
     ["A nitrogenous waste product of muscle metabolism, produced and cleared by the kidneys",
      "That description belongs to creatinine, and the kidney does not produce it."],
     ["A breakdown product of red blood cells, conjugated by the liver",
      "That is bilirubin."],
     ["An enzyme released from injured hepatocytes into the blood",
      "That describes the transaminases."]],
   c=0, cite=c(14)),

 dict(topic="Blood urea nitrogen", io=IOB6, slot="differential",
   q="Besides reduced kidney clearance, which of these raises blood urea nitrogen?",
   opts=[
     ["Gastrointestinal bleeding",
      "Correct — one of the non-renal causes the deck lists."],
     ["Low dietary protein intake",
      "A high protein intake raises it; a low intake would not."],
     ["Overhydration",
      "Dehydration raises it; the opposite state does not."],
     ["Reduced muscle mass",
      "Muscle mass influences creatinine rather than urea nitrogen."]],
   c=0, cite=c(14)),

 dict(topic="Blood urea nitrogen", io=IOB6, slot="differential",
   q="Which four non-renal factors does the deck list as raising blood urea nitrogen?",
   opts=[
     ["Dehydration, gastrointestinal bleeding, high protein intake, and catabolic states",
      "Correct — the four the deck names when calling the value non-specific."],
     ["Dehydration, haemolysis, low protein intake, and pregnancy",
      "Haemolysis, low protein intake, and pregnancy are not on the deck's list."],
     ["Liver failure, malnutrition, overhydration, and immobility",
      "These would tend to lower rather than raise it."],
     ["Muscle injury, strenuous exercise, high creatine intake, and male sex",
      "Those influence creatinine, not urea nitrogen."]],
   c=0, cite=c(14)),

 dict(topic="Blood urea nitrogen", io=IOB6, slot="test finding",
   q="A ratio of blood urea nitrogen to creatinine above twenty to one suggests which kind of cause?",
   opts=[
     ["A prerenal cause", "Correct — the deck uses this ratio to separate prerenal from intrinsic renal causes."],
     ["An intrinsic renal cause", "Intrinsic causes sit below that ratio."],
     ["A postrenal obstructive cause", "The deck's contrast is prerenal against intrinsic."],
     ["A hepatic cause", "The ratio addresses kidney rather than liver disease."]],
   c=0, cite=c(14)),

 dict(topic="Blood urea nitrogen", io=IOB6, slot="education",
   q="What do the speaker notes say about reading blood urea nitrogen?",
   opts=[
     ["Interpret it alongside creatinine, not alone",
      "Correct — the notes' instruction for this value."],
     ["Interpret it alone, since creatinine is less specific",
      "Creatinine is the more specific of the two, and the notes pair them."],
     ["Interpret it only when the patient is fasting",
      "Fasting is a glucose consideration."],
     ["Interpret it only if the estimated filtration rate is normal",
      "The notes set no such condition."]],
   c=0, cite=cn(14)),

 # ---- creatinine ----
 dict(topic="Creatinine", io=IOB7, slot="etiology",
   q="Where does creatinine come from?",
   opts=[
     ["It is a waste product of muscle creatine metabolism",
      "Correct — the deck's description of its origin."],
     ["It is a waste product of protein metabolism produced by the liver",
      "That describes blood urea nitrogen."],
     ["It is filtered from dietary creatine without being metabolised",
      "The deck describes it as a metabolic product of muscle creatine."],
     ["It is produced by the kidney tubules during filtration",
      "The kidney filters it rather than producing it."]],
   c=0, cite=c(14)),

 dict(topic="Creatinine", io=IOB7, slot="test finding",
   q="Why does the deck call creatinine a more specific marker of kidney function than blood urea nitrogen?",
   opts=[
     ["It is filtered by the kidneys and rises as the filtration rate falls, without the many non-renal influences on urea nitrogen",
      "Correct — specificity is the contrast the deck draws between the two."],
     ["It is produced at a rate that never varies between people",
      "Muscle mass, age, and sex all influence it, as the deck says."],
     ["It is measured by a more accurate laboratory method",
      "The deck's argument is physiological rather than analytic."],
     ["It rises earlier in kidney injury than any other marker",
      "The deck's point is specificity, not earliness."]],
   c=0, cite=c(14)),

 dict(topic="Creatinine", io=IOB7, slot="test finding",
   q="Which three factors does the deck say influence creatinine and can make it misleading?",
   opts=[
     ["Muscle mass, age, and sex",
      "Correct — the three the deck names."],
     ["Protein intake, hydration, and recent bleeding",
      "Those influence blood urea nitrogen instead."],
     ["Liver function, bilirubin, and albumin",
      "None of these is given as a creatinine influence."],
     ["Time of day, posture, and fasting state",
      "The deck does not list these."]],
   c=0, cite=c(14)),

 dict(topic="Creatinine", io=IOB7, slot="test finding",
   q="In which patients do the speaker notes warn that a normal creatinine can hide a reduced filtration rate?",
   opts=[
     ["Elderly or cachectic patients",
      "Correct — low muscle mass is the trap the notes name."],
     ["Young athletes with high muscle mass",
      "High muscle mass tends to raise creatinine rather than mask a fall in filtration."],
     ["Patients with liver disease",
      "The notes name low muscle mass rather than hepatic disease."],
     ["Patients who have recently eaten a high protein meal",
      "That affects urea nitrogen."]],
   c=0, cite=cn(14)),

 dict(topic="Creatinine", io=IOB7, slot="initial test",
   q="The estimated glomerular filtration rate is derived from which measurement?",
   opts=[
     ["Serum creatinine", "Correct — the rate is estimated from creatinine, as the deck and the lecture both state."],
     ["Serum blood urea nitrogen alone", "Urea nitrogen is too non-specific to estimate the rate on its own."],
     ["Serum albumin", "Albumin is a liver synthetic marker."],
     ["Urine output over twenty-four hours", "That is a different measure of kidney function."]],
   c=0, cite=c(14)),

 # ---- liver studies ----
 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Why is alanine transaminase more specific for liver injury than aspartate aminotransferase?",
   opts=[
     ["It is found primarily in the liver, whereas the other is also in cardiac and skeletal muscle, kidney, and brain",
      "Correct — the tissue distribution the deck gives for each."],
     ["It rises earlier after hepatocyte injury",
      "The deck's argument is about where each enzyme is found."],
     ["It is measured by a more reliable assay",
      "The difference the deck describes is biological."],
     ["It is released only when the bile ducts are obstructed",
      "That pattern belongs to alkaline phosphatase."]],
   c=0, cite=c(15)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Which four tissues besides the liver does the deck say aspartate aminotransferase is found in?",
   opts=[
     ["Cardiac muscle, skeletal muscle, kidney, and brain",
      "Correct — the four the deck lists."],
     ["Bone, placenta, intestine, and kidney",
      "Those are the extrahepatic sources of alkaline phosphatase."],
     ["Spleen, pancreas, lung, and thyroid",
      "The deck names none of these."],
     ["Red blood cells, platelets, bone marrow, and lymph nodes",
      "Not tissues the deck associates with this enzyme."]],
   c=0, cite=c(15)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="A raised alkaline phosphatase points to which process?",
   opts=[
     ["Cholestasis or bile duct obstruction",
      "Correct — the deck's assignment for this enzyme."],
     ["Hepatocellular injury",
      "That is signalled by the transaminases."],
     ["Impaired hepatic synthetic function",
      "Albumin and the prothrombin time carry that signal."],
     ["Increased red blood cell breakdown",
      "That raises bilirubin."]],
   c=0, cite=c(15)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Which three non-hepatic tissues also contain alkaline phosphatase?",
   opts=[
     ["Bone, placenta, and intestine",
      "Correct — the three the deck names, and the reason a raised value needs confirming."],
     ["Cardiac muscle, skeletal muscle, and brain",
      "Those are extrahepatic sources of aspartate aminotransferase."],
     ["Kidney, spleen, and pancreas",
      "The deck does not list these for this enzyme."],
     ["Red blood cells, platelets, and marrow",
      "Not sources the deck gives."]],
   c=0, cite=c(15)),

 dict(topic="Liver studies", io=IOC, slot="initial test",
   q="Which test confirms that a raised alkaline phosphatase is of hepatic origin?",
   opts=[
     ["Gamma-glutamyl transferase",
      "Correct — the deck names this as the confirmatory step."],
     ["Lactate dehydrogenase",
      "Not the confirmatory test the deck gives."],
     ["A bone-specific isoenzyme assay",
      "The deck's stated route is the transferase."],
     ["A repeat alkaline phosphatase in one month",
      "Repeating does not distinguish the tissue of origin."]],
   c=0, cite=c(15)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Which is a synthetic product of the liver, and therefore a measure of what the liver is making?",
   opts=[
     ["Albumin", "Correct — the deck lists albumin as a synthetic product of the liver."],
     ["Alkaline phosphatase", "That is an enzyme marking cholestasis."],
     ["Total bilirubin", "That is a breakdown product of red blood cells."],
     ["Aspartate aminotransferase", "That is an enzyme released on injury."]],
   c=0, cite=c(15)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Total bilirubin is a breakdown product of what?",
   opts=[
     ["Red blood cells", "Correct — the deck's description of where bilirubin comes from."],
     ["Skeletal muscle protein", "That yields creatinine and urea nitrogen."],
     ["Dietary protein in the gut", "The deck attributes bilirubin to red cell breakdown."],
     ["Hepatocyte membranes during injury", "Injury releases enzymes rather than generating bilirubin."]],
   c=0, cite=c(15)),

 dict(topic="Liver studies", io=IOC, slot="education",
   q="The slide is titled 'Liver Function Tests' with an asterisk. What do the speaker notes say the asterisk is there for?",
   opts=[
     ["The transaminases, alkaline phosphatase, and bilirubin mark liver INJURY rather than liver function",
      "Correct — the notes correct the slide's own title on exactly this point."],
     ["These tests are only valid when the patient is fasting",
      "Fasting is not the caveat the notes raise."],
     ["These tests are not on the comprehensive metabolic panel",
      "They are precisely what the comprehensive panel adds."],
     ["These tests are unreliable in patients with kidney disease",
      "The notes make no such claim."]],
   c=0, cite=cn(15)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Which three tests do the speaker notes group as measures of synthetic and excretory function?",
   opts=[
     ["Albumin, prothrombin time, and bilirubin",
      "Correct — the notes' grouping for function as opposed to injury."],
     ["Aspartate aminotransferase, alanine transaminase, and alkaline phosphatase",
      "The notes group those three as markers of injury."],
     ["Albumin, total protein, and alkaline phosphatase",
      "Alkaline phosphatase belongs to the injury group."],
     ["Bilirubin, gamma-glutamyl transferase, and alanine transaminase",
      "Only bilirubin belongs to the function group."]],
   c=0, cite=cn(16)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Why does a low albumin indicate CHRONIC rather than acute liver disease?",
   opts=[
     ["Its half-life is about three weeks, so the level takes that long to fall",
      "Correct — the deck ties chronicity to the half-life."],
     ["It is only produced when the liver is inflamed",
      "Albumin is produced continuously by the healthy liver."],
     ["It is consumed rapidly during acute illness and replaced within days",
      "The deck notes it may drop in severe illness, but the chronicity argument is the half-life."],
     ["It is measured only on repeat panels",
      "Measurement frequency is not the reason."]],
   c=0, cite=c(16)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Which liver test does the deck call the most sensitive marker of function, and how fast can it move?",
   opts=[
     ["The prothrombin time with its ratio, which can prolong within twenty-four hours of severe injury",
      "Correct — the deck's most sensitive functional marker and its speed."],
     ["Albumin, which can fall within twenty-four hours of severe injury",
      "Albumin's three-week half-life makes it slow, not fast."],
     ["Alanine transaminase, which rises within hours of injury",
      "That is a marker of injury rather than of function."],
     ["Bilirubin, which rises within twenty-four hours of severe injury",
      "Bilirubin reflects conjugation and excretion but is not called the most sensitive."]],
   c=0, cite=c(16)),

 dict(topic="Liver studies", io=IOC, slot="etiology",
   q="Which clotting factors does the deck link to the prothrombin time as a measure of liver function?",
   opts=[
     ["Factors two, seven, nine, and ten",
      "Correct — the four the deck lists."],
     ["Factors one, five, eight, and thirteen",
      "Not the group the deck names."],
     ["Factors eight, nine, eleven, and twelve",
      "Those belong to the intrinsic pathway and are not the deck's list."],
     ["Factors five, seven, ten, and thirteen",
      "Only two of these appear on the deck's list."]],
   c=0, cite=c(16)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="What does bilirubin reflect about liver function?",
   opts=[
     ["Conjugation and excretion capacity",
      "Correct — the deck's phrasing for what bilirubin measures."],
     ["Protein synthetic capacity",
      "Albumin carries that signal."],
     ["The degree of hepatocyte necrosis",
      "The transaminases reflect injury."],
     ["The patency of the portal vein",
      "The deck makes no such link."]],
   c=0, cite=c(16)),
]
