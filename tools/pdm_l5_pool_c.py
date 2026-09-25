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
      "Correct — insulin lowers glucose, glucagon and the counter-regulatory hormones raise it, and the kidney also contributes through gluconeogenesis."],
     ["Glucagon lowers it; insulin and cortisol raise it",
      "This reverses the roles of insulin and glucagon."],
     ["Cortisol lowers it; insulin and adrenaline raise it",
      "Cortisol is one of the counter-regulatory hormones that raise glucose."],
     ["Insulin lowers it; antidiuretic hormone raises it",
      "That hormone governs water handling, not glucose."]],
   c=0, cite=c(13)),

 dict(topic="Glucose", io=IOB5, slot="etiology",
   q="Besides the pancreatic hormones, which organ contributes to glucose regulation, and how?",
   opts=[
     ["The kidney, through gluconeogenesis",
      "Correct — glucose is balanced by insulin and by glucagon and the counter-regulatory hormones, and the kidney also contributes through gluconeogenesis."],
     ["The spleen, through glucose storage",
      "The spleen has no stated role in glucose regulation; the kidney contributes through gluconeogenesis, alongside insulin and glucagon."],
     ["The thyroid, through its effect on metabolic rate",
      "The thyroid is not the organ given; besides insulin and glucagon, the kidney contributes to glucose regulation through gluconeogenesis."],
     ["The adrenal medulla, through glycogen storage",
      "The adrenal medulla is not the organ given; the kidney contributes to glucose regulation through gluconeogenesis, alongside insulin and glucagon."]],
   c=0, cite=c(13)),

 dict(topic="Glucose", io=IOB5, slot="test finding",
   q="Which piece of context must a glucose value always be interpreted against?",
   opts=[
     ["Whether the patient was fasting or not",
      "Correct — the diagnostic thresholds for diabetes differ entirely between the fasting and the random state, so the same number means different things depending on when the patient last ate."],
     ["Whether the sample was taken from an artery or a vein",
      "Arterial and venous glucose differ only slightly; what changes the interpretation completely is whether the patient was fasting."],
     ["The time elapsed since the last insulin dose",
      "Insulin timing matters when adjusting a regimen, but the fasting state is what determines which diagnostic threshold applies."],
     ["The patient's body mass index",
      "Body mass index bears on diabetes risk rather than on how a given glucose value is read; the fasting state does that."]],
   c=0, cite=c(13)),

 dict(topic="Glucose", io=IOB5, slot="test finding",
   q="What effect does marked hyperglycaemia have on the measured sodium?",
   opts=[
     ["It lowers it, by dilution",
      "Correct — marked hyperglycemia lowers the measured sodium by dilution, by about 1.6 to 2 milliequivalents per liter for each 100 milligrams per deciliter of glucose above normal."],
     ["It raises it, by drawing water into the cells",
      "The water shift is out of the cells, which dilutes the sodium."],
     ["It leaves it unchanged but raises the potassium",
      "The effect is on sodium: marked hyperglycemia lowers the measured sodium by dilution, which is why a corrected sodium is used."],
     ["It makes the sodium unmeasurable until the glucose is corrected",
      "The sodium is measurable; it simply reads low."]],
   c=0, cite=cn(13)),

 # ---- blood urea nitrogen ----
 dict(topic="Blood urea nitrogen", io=IOB6, slot="etiology",
   q="What is blood urea nitrogen, and where is it produced and cleared?",
   opts=[
     ["A nitrogenous waste product of protein metabolism, produced by the liver and cleared by the kidneys",
      "Correct — urea nitrogen is a nitrogenous waste of protein metabolism, produced by the liver and cleared by the kidneys, so it rises with reduced renal clearance."],
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
      "Correct — urea nitrogen is non-specific: besides reduced renal clearance, dehydration, gastrointestinal bleeding, high protein intake and catabolic states raise it."],
     ["Low dietary protein intake",
      "A high protein intake raises it; a low intake would not."],
     ["Overhydration",
      "Dehydration raises it; the opposite state does not."],
     ["Reduced muscle mass",
      "Muscle mass influences creatinine rather than urea nitrogen."]],
   c=0, cite=c(14)),

 dict(topic="Blood urea nitrogen", io=IOB6, slot="differential",
   q="Which four non-renal factors raise blood urea nitrogen?",
   opts=[
     ["Dehydration, gastrointestinal bleeding, high protein intake, and catabolic states",
      "Correct — dehydration, gastrointestinal bleeding, high protein intake and catabolic states raise urea nitrogen, so it is non-specific and read with creatinine."],
     ["Dehydration, haemolysis, low protein intake, and pregnancy",
      "Hemolysis, low protein intake and pregnancy are not among them; the non-renal causes are dehydration, gastrointestinal bleeding, high protein intake and catabolic states."],
     ["Liver failure, malnutrition, overhydration, and immobility",
      "These would tend to lower rather than raise it."],
     ["Muscle injury, strenuous exercise, high creatine intake, and male sex",
      "Those influence creatinine, not urea nitrogen."]],
   c=0, cite=c(14)),

 dict(topic="Blood urea nitrogen", io=IOB6, slot="test finding",
   q="A ratio of blood urea nitrogen to creatinine above twenty to one suggests which kind of cause?",
   opts=[
     ["A prerenal cause", "Correct — a ratio above 20 to 1 points to a prerenal cause such as hypovolemia, distinguishing it from an intrinsic renal cause."],
     ["An intrinsic renal cause", "Intrinsic causes sit below that ratio."],
     ["A postrenal obstructive cause", "A postrenal cause is not what the ratio flags; a urea nitrogen to creatinine ratio above 20 to 1 separates prerenal from intrinsic renal causes."],
     ["A hepatic cause", "The ratio addresses kidney rather than liver disease."]],
   c=0, cite=c(14)),

 dict(topic="Blood urea nitrogen", io=IOB6, slot="education",
   q="How should blood urea nitrogen be read?",
   opts=[
     ["Interpret it alongside creatinine, not alone",
      "Correct — urea nitrogen alone cannot distinguish dehydration or a protein load from kidney failure; the ratio to creatinine is what separates them."],
     ["Interpret it alone, since creatinine is less specific",
      "Creatinine is the more specific of the two for kidney function, which is precisely why urea nitrogen is read against it rather than alone."],
     ["Interpret it only when the patient is fasting",
      "Fasting is a glucose consideration."],
     ["Interpret it only if the estimated filtration rate is normal",
      "Urea nitrogen is read against creatinine whatever the filtration rate; the ratio itself is what carries the information."]],
   c=0, cite=cn(14)),

 # ---- creatinine ----
 dict(topic="Creatinine", io=IOB7, slot="etiology",
   q="Where does creatinine come from?",
   opts=[
     ["It is a waste product of muscle creatine metabolism",
      "Correct — creatinine is a waste product of muscle creatine metabolism, filtered by the kidneys, and a more specific renal marker than urea nitrogen."],
     ["It is a waste product of protein metabolism produced by the liver",
      "That describes blood urea nitrogen."],
     ["It is filtered from dietary creatine without being metabolised",
      "Creatinine is not filtered dietary creatine; it is a waste product of muscle creatine metabolism that the kidneys then filter."],
     ["It is produced by the kidney tubules during filtration",
      "The kidney filters it rather than producing it."]],
   c=0, cite=c(14)),

 dict(topic="Creatinine", io=IOB7, slot="test finding",
   q="Why is creatinine a more specific marker of kidney function than blood urea nitrogen?",
   opts=[
     ["It is filtered by the kidneys and rises as the filtration rate falls, without the many non-renal influences on urea nitrogen",
      "Correct — creatinine is filtered by the kidneys and rises as filtration falls, while urea nitrogen is also raised by dehydration, bleeding, protein intake and catabolic states."],
     ["It is produced at a rate that never varies between people",
      "Production does vary, with muscle mass, age and sex, so creatinine may underestimate kidney dysfunction in patients with low muscle mass."],
     ["It is measured by a more accurate laboratory method",
      "Laboratory method is not the reason; urea nitrogen is non-specific, raised by dehydration, bleeding, protein intake and catabolism, while creatinine is not."],
     ["It rises earlier in kidney injury than any other marker",
      "Earliness is not the point; creatinine rises as the filtration rate falls and is a more specific marker of kidney function than urea nitrogen."]],
   c=0, cite=c(14)),

 dict(topic="Creatinine", io=IOB7, slot="test finding",
   q="Which three factors influence creatinine and can make it misleading?",
   opts=[
     ["Muscle mass, age, and sex",
      "Correct — creatinine is influenced by muscle mass, age and sex, so it may underestimate kidney dysfunction in patients with low muscle mass."],
     ["Protein intake, hydration, and recent bleeding",
      "Those influence blood urea nitrogen instead."],
     ["Liver function, bilirubin, and albumin",
      "None of these is given as a creatinine influence."],
     ["Time of day, posture, and fasting state",
      "Time of day, posture and fasting state are not the factors given; creatinine is influenced by muscle mass, age and sex."]],
   c=0, cite=c(14)),

 dict(topic="Creatinine", io=IOB7, slot="test finding",
   q="In which patients can a normal creatinine hide a reduced filtration rate?",
   opts=[
     ["Elderly or cachectic patients",
      "Correct — with little muscle to generate creatinine, production is low, so the serum level stays within range even after substantial filtration has been lost."],
     ["Young athletes with high muscle mass",
      "High muscle mass tends to raise creatinine rather than mask a fall in filtration."],
     ["Patients with liver disease",
      "Liver disease can lower urea nitrogen, but the trap for creatinine is low muscle mass, as in the elderly or cachectic."],
     ["Patients who have recently eaten a high protein meal",
      "That affects urea nitrogen."]],
   c=0, cite=cn(14)),

 dict(topic="Creatinine", io=IOB7, slot="initial test",
   q="The estimated glomerular filtration rate is derived from which measurement?",
   opts=[
     ["Serum creatinine", "Correct — the estimating equations take serum creatinine and adjust it for age and sex, which stand in for the muscle mass that determines production."],
     ["Serum blood urea nitrogen alone", "Urea nitrogen is too non-specific to estimate the rate on its own."],
     ["Serum albumin", "Albumin is a liver synthetic marker."],
     ["Urine output over twenty-four hours", "That is a different measure of kidney function."]],
   c=0, cite=c(14)),

 # ---- liver studies ----
 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Why is alanine transaminase more specific for liver injury than aspartate aminotransferase?",
   opts=[
     ["It is found primarily in the liver, whereas the other is also in cardiac and skeletal muscle, kidney, and brain",
      "Correct — alanine transaminase is concentrated in hepatocytes, so a rise points to the liver, whereas aspartate aminotransferase can equally reflect damaged heart, skeletal muscle, kidney or brain."],
     ["It rises earlier after hepatocyte injury",
      "Timing is not the distinction; specificity comes from alanine transaminase being largely confined to the liver."],
     ["It is measured by a more reliable assay",
      "Both are measured reliably; the difference is where each enzyme is found in the body."],
     ["It is released only when the bile ducts are obstructed",
      "Biliary obstruction raises alkaline phosphatase; the transaminases are released from damaged hepatocytes whatever the cause."]],
   c=0, cite=c(15)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Besides the liver, in which four tissues is aspartate aminotransferase found?",
   opts=[
     ["Cardiac muscle, skeletal muscle, kidney, and brain",
      "Correct — aspartate aminotransferase is also found in cardiac and skeletal muscle, kidney and brain, so it is less liver-specific than alanine transaminase."],
     ["Bone, placenta, intestine, and kidney",
      "Those are the extrahepatic sources of alkaline phosphatase."],
     ["Spleen, pancreas, lung, and thyroid",
      "Spleen, pancreas, lung and thyroid are not significant sources; the extrahepatic ones are cardiac and skeletal muscle, kidney and brain."],
     ["Red blood cells, platelets, bone marrow, and lymph nodes",
      "Those are not the tissues; besides the liver, aspartate aminotransferase is found in cardiac and skeletal muscle, kidney and brain."]],
   c=0, cite=c(15)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="A raised alkaline phosphatase points to which process?",
   opts=[
     ["Cholestasis or bile duct obstruction",
      "Correct — the enzyme sits on the canalicular membrane of the biliary epithelium, and obstructed bile flow induces its production and releases it into the blood."],
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
      "Correct — bone turnover, pregnancy and intestinal activity all raise it, so a raised value does not by itself mean liver disease."],
     ["Cardiac muscle, skeletal muscle, and brain",
      "Those are extrahepatic sources of aspartate aminotransferase."],
     ["Kidney, spleen, and pancreas",
      "Kidney, spleen and pancreas are not significant sources; bone, placenta and intestine are the ones that confound a raised value."],
     ["Red blood cells, platelets, and marrow",
      "Blood cells are not a source of alkaline phosphatase; bone, placenta and intestine are the extrahepatic origins."]],
   c=0, cite=c(15)),

 dict(topic="Liver studies", io=IOC, slot="initial test",
   q="Which test confirms that a raised alkaline phosphatase is of hepatic origin?",
   opts=[
     ["Gamma-glutamyl transferase",
      "Correct — alkaline phosphatase is also found in bone, placenta and intestine, so gamma-glutamyl transferase is used to confirm a hepatic origin."],
     ["Lactate dehydrogenase",
      "Lactate dehydrogenase is not the confirmatory test; gamma-glutamyl transferase confirms that a raised alkaline phosphatase is hepatic."],
     ["A bone-specific isoenzyme assay",
      "An isoenzyme assay is not the route; alkaline phosphatase is also present in bone, placenta and intestine, and gamma-glutamyl transferase confirms hepatic origin."],
     ["A repeat alkaline phosphatase in one month",
      "Repeating does not distinguish the tissue of origin."]],
   c=0, cite=c(15)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Which is a synthetic product of the liver, and therefore a measure of what the liver is making?",
   opts=[
     ["Albumin", "Correct — albumin is synthesized only by the liver, and with a half-life of about three weeks a low value marks chronic liver disease."],
     ["Alkaline phosphatase", "That is an enzyme marking cholestasis."],
     ["Total bilirubin", "That is a breakdown product of red blood cells."],
     ["Aspartate aminotransferase", "That is an enzyme released on injury."]],
   c=0, cite=c(15)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Total bilirubin is a breakdown product of what?",
   opts=[
     ["Red blood cells", "Correct — haem from senescent red cells is broken down to unconjugated bilirubin, which the liver conjugates and excretes into bile."],
     ["Skeletal muscle protein", "That yields creatinine and urea nitrogen."],
     ["Dietary protein in the gut", "Dietary protein yields urea rather than bilirubin; bilirubin comes from the haem of broken-down red cells."],
     ["Hepatocyte membranes during injury", "Injury releases enzymes rather than generating bilirubin."]],
   c=0, cite=c(15)),

 dict(topic="Liver studies", io=IOC, slot="education",
   q="The label 'liver function tests' is a misnomer for most of the panel. Why?",
   opts=[
     ["The transaminases, alkaline phosphatase, and bilirubin mark liver INJURY rather than liver function",
      "Correct — the transaminases, alkaline phosphatase and bilirubin rise when hepatocytes are damaged, so they report injury rather than synthetic function; albumin and the prothrombin time are the tests that actually measure what the liver is making."],
     ["These tests are only valid when the patient is fasting",
      "Fasting is not the caveat; these tests are interpreted without regard to the last meal, unlike glucose or a lipid panel."],
     ["These tests are not on the comprehensive metabolic panel",
      "They are precisely what the comprehensive metabolic panel adds over the basic panel, so they are on it."],
     ["These tests are unreliable in patients with kidney disease",
      "Kidney disease does not invalidate them; urea nitrogen and creatinine are the panel components that track renal function."]],
   c=0, cite=cn(15)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Which three tests are measures of synthetic and excretory function?",
   opts=[
     ["Albumin, prothrombin time, and bilirubin",
      "Correct — albumin and the clotting factors behind the prothrombin time are made by the liver, and bilirubin is cleared by it, so all three report on what the liver can still do."],
     ["Aspartate aminotransferase, alanine transaminase, and alkaline phosphatase",
      "Those three are released from damaged cells and so measure injury; function is measured by albumin, the prothrombin time and bilirubin."],
     ["Albumin, total protein, and alkaline phosphatase",
      "Alkaline phosphatase belongs to the injury group."],
     ["Bilirubin, gamma-glutamyl transferase, and alanine transaminase",
      "Only bilirubin belongs to the function group."]],
   c=0, cite=cn(16)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Why does a low albumin indicate CHRONIC rather than acute liver disease?",
   opts=[
     ["Its half-life is about three weeks, so the level takes that long to fall",
      "Correct — with a half-life of around three weeks, existing albumin persists long after synthesis stops, so the level cannot fall quickly enough to reflect acute injury."],
     ["It is only produced when the liver is inflamed",
      "Albumin is produced continuously by the healthy liver."],
     ["It is consumed rapidly during acute illness and replaced within days",
      "Albumin can fall in severe acute illness through capillary leak, but the reason a low level implies chronicity is its long half-life."],
     ["It is measured only on repeat panels",
      "Measurement frequency is not the reason."]],
   c=0, cite=c(16)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="Which liver test is called the most sensitive marker of function, and how fast can it move?",
   opts=[
     ["The prothrombin time with its ratio, which can prolong within twenty-four hours of severe injury",
      "Correct — the clotting factors have half-lives measured in hours, so synthetic failure shows in the prothrombin time within a day, long before albumin moves."],
     ["Albumin, which can fall within twenty-four hours of severe injury",
      "Albumin's three-week half-life makes it slow, not fast."],
     ["Alanine transaminase, which rises within hours of injury",
      "That is a marker of injury rather than of function."],
     ["Bilirubin, which rises within twenty-four hours of severe injury",
      "Bilirubin reflects conjugation and excretion but is not called the most sensitive."]],
   c=0, cite=c(16)),

 dict(topic="Liver studies", io=IOC, slot="etiology",
   q="Which clotting factors are linked to the prothrombin time as a measure of liver function?",
   opts=[
     ["Factors two, seven, nine, and ten",
      "Correct — factors two, seven, nine and ten are the vitamin K dependent factors made by the liver, and factor seven has the shortest half-life, which is what makes the test move so fast."],
     ["Factors one, five, eight, and thirteen",
      "Factors one, five, eight and thirteen are not the vitamin K dependent group; factor eight is made outside the liver and stays normal in liver failure."],
     ["Factors eight, nine, eleven, and twelve",
      "Those are intrinsic pathway factors reflected in the activated partial thromboplastin time; the prothrombin time tracks factors two, seven, nine and ten."],
     ["Factors five, seven, ten, and thirteen",
      "Factors five and thirteen are not vitamin K dependent; the group is two, seven, nine and ten."]],
   c=0, cite=c(16)),

 dict(topic="Liver studies", io=IOC, slot="test finding",
   q="What does bilirubin reflect about liver function?",
   opts=[
     ["Conjugation and excretion capacity",
      "Correct — the liver must conjugate bilirubin to make it water-soluble and then excrete it into bile, so a raised level indicates failure of one or other step."],
     ["Protein synthetic capacity",
      "Albumin carries that signal."],
     ["The degree of hepatocyte necrosis",
      "The transaminases reflect injury."],
     ["The patency of the portal vein",
      "Portal vein patency is assessed by imaging; bilirubin reports the liver's ability to conjugate and excrete."]],
   c=0, cite=c(16)),
]
