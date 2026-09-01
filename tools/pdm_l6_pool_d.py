# -*- coding: utf-8 -*-
# PDM I Lecture 6 (Urinalysis, Prof. Stacie Gopal) -- pool D.
# The blood pad, and objective b: telling hematuria, hemoglobinuria and
# myoglobinuria apart.
#
# The whole objective turns on one fact: the pad detects HEME, which sits in
# red cells, in free hemoglobin and in myoglobin alike, so a positive result
# does not say which. What separates them is what else is true --
#   hematuria      intact red cells seen on microscopy
#   hemoglobinuria no intact cells; raised serum UNCONJUGATED bilirubin
#   myoglobinuria   no intact cells; raised serum creatine phosphokinase
#
# The "3 RBCs" threshold for microscopic hematuria is ONLY in the slide 23
# picture; the shape text on that slide breaks off at "microscopic hematuria"
# and loses it. View the image, do not trust the extraction.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "6. Urinalysis Diagnostics SV Gopal Fall 2026.pptx"
def c(n):  return f"{SRC}, Slide {n}"
def ci(n): return f"{SRC}, Slide {n} (image)"
def au(t): return f"Lecture recording, 1 September 2026, {t}"

IOB = "b — Differentiate between hematuria, hemoglobinuria, and myoglobinuria"

POOL_D = [
 dict(topic="The blood pad", io=IOB, slot="mechanism",
   q="What does the blood pad on a reagent strip actually detect?",
   opts=[
     ["Heme",
      "Correct — and heme is present in all three of the possible sources."],
     ["Intact red cells only",
      "Intact cells are one source, but the pad detects the molecule."],
     ["Free hemoglobin only",
      "Free hemoglobin is one source among three."],
     ["Iron released from ferritin stores",
      "Storage iron is not what the pad reacts to."]],
   c=0, cite=c(23)),

 dict(topic="The blood pad", io=IOB, slot="limitation",
   q="The blood pad is positive. What can it NOT tell you?",
   opts=[
     ["Which of red cells, hemoglobin, or myoglobin is responsible",
      "Correct — the pad does not differentiate between them."],
     ["Whether heme is present at all",
      "That is precisely what it does establish."],
     ["Whether the specimen was fresh",
      "Freshness is a matter of collection rather than of this pad."],
     ["Whether protein is also present",
      "Protein has its own pad."]],
   c=0, cite=c(23)),

 dict(topic="Hematuria", io=IOB, slot="interpretation",
   q="What does hematuria refer to?",
   opts=[
     ["Intact red cells in the urine",
      "Correct — the cells themselves are present."],
     ["Free hemoglobin with no intact cells",
      "That is hemoglobinuria."],
     ["Myoglobin released from injured muscle",
      "That is myoglobinuria."],
     ["Heme detected on a pad with no source identified",
      "That describes a positive pad rather than hematuria specifically."]],
   c=0, cite=c(24)),

 dict(topic="Hematuria", io=IOB, slot="interpretation",
   q="How is gross hematuria distinguished from microscopic hematuria?",
   opts=[
     ["Gross is visible to the naked eye; microscopic needs analysis to detect",
      "Correct — visibility is the distinction."],
     ["Gross comes from the kidney; microscopic comes from the bladder",
      "Either can arise anywhere along the tract."],
     ["Gross is painless; microscopic is painful",
      "Pain does not separate the two."],
     ["Gross means more than three red cells; microscopic means fewer",
      "The threshold defines microscopic hematuria rather than separating the two this way."]],
   c=0, cite=c(24)),

 dict(topic="Hematuria", io=IOB, slot="interpretation",
   q="How many red cells define microscopic hematuria?",
   opts=[
     ["Three or more",
      "Correct — that is the threshold."],
     ["One or more",
      "A single cell is below the threshold."],
     ["Ten or more",
      "Higher than the threshold used."],
     ["Twenty or more",
      "Far above the threshold used."]],
   c=0, cite=ci(23)),

 dict(topic="Hematuria", io=IOB, slot="interpretation",
   q="Which of these causes bleeding into the urinary tract?",
   opts=[
     ["Infection, inflammation, trauma, tumour, or a stone",
      "Correct — any of these can produce hematuria."],
     ["Intravascular destruction of red cells",
      "That gives hemoglobinuria, with no intact cells."],
     ["Crush injury to skeletal muscle",
      "That gives myoglobinuria."],
     ["Biliary obstruction by a gallstone",
      "That produces bilirubin in the urine, not blood."]],
   c=0, cite=c(24)),

 dict(topic="Hematuria", io=IOB, slot="interpretation",
   q="A patient on anticoagulation reports blood in the urine. What should that raise?",
   opts=[
     ["The possibility that the anticoagulation is over-aggressive",
      "Correct — excessive anticoagulation is a recognised cause."],
     ["The possibility of rhabdomyolysis",
      "Muscle injury gives myoglobinuria rather than frank blood."],
     ["The possibility of intravascular hemolysis",
      "That would give hemoglobinuria with no intact cells."],
     ["The possibility of a reduced tubular threshold",
      "That concerns glucose rather than blood."]],
   c=0, cite=c(24)),

 dict(topic="Hemoglobinuria", io=IOB, slot="mechanism",
   q="How does free hemoglobin reach the urine?",
   opts=[
     ["Through intravascular destruction of red cells",
      "Correct — hemolysis inside the vessels releases it."],
     ["Through bleeding anywhere along the urinary tract",
      "That gives intact cells, which is hematuria."],
     ["Through release from injured skeletal muscle",
      "Muscle releases myoglobin instead."],
     ["Through failure of tubular reabsorption of protein",
      "That gives proteinuria."]],
   c=0, cite=c(25)),

 dict(topic="Hemoglobinuria", io=IOB, slot="interpretation",
   q="Which serum finding accompanies hemoglobinuria?",
   opts=[
     ["A raised unconjugated bilirubin",
      "Correct — it is a direct product of hemoglobin metabolism."],
     ["A raised conjugated bilirubin",
      "The conjugated form rises with hepatic and biliary disease."],
     ["A raised creatine phosphokinase",
      "That accompanies myoglobinuria."],
     ["A raised serum albumin",
      "Albumin does not rise here."]],
   c=0, cite=c(25)),

 dict(topic="Hemoglobinuria", io=IOB, slot="interpretation",
   q="Which of these produces hemoglobinuria?",
   opts=[
     ["A hemolytic transfusion reaction",
      "Correct — rapid intravascular destruction of red cells."],
     ["A crush injury to the thigh",
      "That releases myoglobin."],
     ["A bladder tumour",
      "That bleeds, giving intact red cells."],
     ["A ureteric stone",
      "That also bleeds, giving intact cells."]],
   c=0, cite=c(25)),

 dict(topic="Hemoglobinuria", io=IOB, slot="interpretation",
   q="Which of these is a recognised cause of hemoglobinuria?",
   opts=[
     ["Severe burns",
      "Correct — extensive burns destroy red cells intravascularly."],
     ["Statin therapy",
      "Statins are associated with rhabdomyolysis and myoglobinuria."],
     ["Over-aggressive anticoagulation",
      "That produces bleeding and intact red cells."],
     ["Electric shock",
      "That damages muscle, giving myoglobinuria."]],
   c=0, cite=c(25)),

 dict(topic="Myoglobinuria", io=IOB, slot="mechanism",
   q="Where does the myoglobin in myoglobinuria come from?",
   opts=[
     ["Damaged skeletal muscle",
      "Correct — muscle injury releases it."],
     ["Destroyed circulating red cells",
      "Those release hemoglobin."],
     ["Bleeding from the bladder wall",
      "That gives intact red cells."],
     ["The liver, after conjugation",
      "The liver conjugates bilirubin, not myoglobin."]],
   c=0, cite=c(26)),

 dict(topic="Myoglobinuria", io=IOB, slot="interpretation",
   q="Which serum finding supports myoglobinuria?",
   opts=[
     ["A raised creatine phosphokinase",
      "Correct — it is released alongside myoglobin from damaged muscle."],
     ["A raised unconjugated bilirubin",
      "That accompanies hemoglobinuria."],
     ["A raised conjugated bilirubin",
      "That points to hepatic or biliary disease."],
     ["A raised serum glucose",
      "Glucose is unrelated to muscle breakdown here."]],
   c=0, cite=c(26)),

 dict(topic="Myoglobinuria", io=IOB, slot="interpretation",
   q="Which of these causes rhabdomyolysis?",
   opts=[
     ["A compression injury, hyperthermia, or a statin",
      "Correct — all three are recognised causes."],
     ["A hemolytic transfusion reaction",
      "That destroys red cells rather than muscle."],
     ["Sickle cell disease",
      "That produces intravascular hemolysis."],
     ["A urinary tract infection",
      "Infection does not cause rhabdomyolysis."]],
   c=0, cite=c(26)),

 dict(topic="Differentiating the three", io=IOB, slot="interpretation",
   q="The blood pad is positive but microscopy shows no intact red cells. Which two possibilities remain?",
   opts=[
     ["Hemoglobinuria and myoglobinuria",
      "Correct — both give heme without intact cells."],
     ["Hematuria and hemoglobinuria",
      "Hematuria would show intact cells."],
     ["Hematuria and myoglobinuria",
      "Hematuria would show intact cells."],
     ["Proteinuria and hemoglobinuria",
      "Protein registers on a different pad."]],
   c=0, cite=c(26)),

 dict(topic="Differentiating the three", io=IOB, slot="next step",
   q="The blood pad is positive, microscopy shows no red cells, and the serum creatine phosphokinase is raised. Which is it?",
   opts=[
     ["Myoglobinuria",
      "Correct — a raised creatine phosphokinase points to muscle."],
     ["Hemoglobinuria",
      "That would raise the unconjugated bilirubin instead."],
     ["Hematuria",
      "Intact cells would be visible."],
     ["Contamination of the specimen",
      "Contamination does not raise the creatine phosphokinase."]],
   c=0, cite=au("34:47")),

 dict(topic="Differentiating the three", io=IOB, slot="next step",
   q="The blood pad is positive, no intact red cells are seen, and the serum unconjugated bilirubin is raised. Which is it?",
   opts=[
     ["Hemoglobinuria",
      "Correct — the unconjugated bilirubin comes from hemoglobin breakdown."],
     ["Myoglobinuria",
      "That would raise the creatine phosphokinase."],
     ["Hematuria",
      "Intact cells would be visible."],
     ["Bilirubinuria from biliary obstruction",
      "That raises the conjugated form and shows on the bilirubin pad."]],
   c=0, cite=c(25)),

 dict(topic="Blood pad", io=IOB, slot="interpretation",
   q="A healthy patient has a trace of blood on the dipstick after a hard run. How is that read?",
   opts=[
     ["A trace can follow strenuous exercise",
      "Correct — exercise can produce a small amount."],
     ["It always indicates a stone",
      "A stone is one cause among several, not the only reading."],
     ["It confirms intravascular hemolysis",
      "Hemolysis would not be assumed from a trace after exercise."],
     ["It indicates the specimen was contaminated",
      "Exercise is the simpler explanation."]],
   c=0, cite=au("29:48")),
]
