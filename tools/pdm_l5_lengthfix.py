# -*- coding: utf-8 -*-
"""Length-bias fixes for the PDM I Lecture 5 pool.

A question is gameable when the correct option is the uniquely longest AND is
at least 8 characters and 18 per cent longer than the runner-up -- a student
can score above chance without reading the medicine. See
[[distractor_style_matching]].

THE RULE IS PAD, NEVER TRIM. Most of these correct answers are enumerations
("all six liver tests", "all four findings") or a technique plus its caveat.
Shortening them would delete real content from the answer a student is meant to
learn. So the runner-up distractor is lengthened instead, keeping it plausible
and unambiguously wrong.

KEYS ARE (question index, option index) INTO THE CONCATENATED POOL, never the
option string. Option strings recur across questions -- a string replace once
hit a distractor in one question and the CORRECT answer in another. The
partition script asserts that no fix targets a correct option.
"""
FIXES = {
 (0, 2):  "Clotting factor activity together with the time taken for a clot to form in the sample",
 (8, 1):  "A basic metabolic panel, which is the same panel run without its liver additions",
 (13, 1): "Any newly started prescription medication, whatever its route or class",
 (20, 1): "The labels are added later by the laboratory when the values are entered",
 (24, 1): "Using a repeat potassium to confirm that a raised potassium is not simply haemolysed",
 (25, 1): "The patient's own previous result from the same laboratory, and nothing else besides",
 (36, 1): "Small changes reliably indicate that the sample was taken or handled incorrectly",
 (37, 3): "Hepatic encephalopathy with confusion",
 (39, 1): "It accumulates steadily over time and must then be actively removed from the body",
 (40, 1): "Antidiuretic hormone, acting at the collecting duct",
 (41, 1): "Storage in, and release from, the glycogen held in skeletal muscle",
 (42, 1): "Both raise the measured potassium by causing haemolysis of the sample",
 (46, 3): "It binds to haemoglobin and is carried to the lungs for excretion",
 (54, 2): "Maintaining the resting membrane potential across the cell",
 (55, 2): "Cortisol lowers it; insulin and adrenaline together raise it",
 (65, 1): "It is produced at a rate that never varies between people, whatever their build or age",
 (69, 3): "It is released into the blood only when the bile ducts have become obstructed",
 (76, 3): "These tests are unreliable in any patient who also has significant kidney disease",
 (79, 1): "Albumin, which can fall within twenty-four hours of a severe hepatic injury",
 (84, 1): "Viral hepatitis, alcohol, ischaemia, and drug injury",
 (90, 1): "Raised transaminases with a low albumin, a prolonged prothrombin time and jaundice",
 (101, 2): "They are both reported on the comprehensive panel and on no other panel",
 (109, 2): "Diarrhoea, renal tubular acidosis, saline infusion, and acetazolamide",
 (113, 1): "Prerenal failure from intrinsic renal failure",
 (115, 3): "Hepatorenal syndrome in advanced liver disease",
 (116, 1): "Serum sodium, serum potassium, serum calcium, serum magnesium, and serum phosphate",
 (117, 1): "Ignore the sodium value entirely until the glucose has been brought back to normal",
 (121, 1): "The number alone is diagnostic whenever it falls outside the printed reference range",
 (125, 1): "Liver ultrasound, cystatin C, a urine protein, and a repeat panel in three months",
 (128, 1): "A lab value is diagnostic on its own once it falls outside the reference range",
 (129, 1): "Low sodium, raised potassium, raised chloride, and a low bicarbonate with acidaemia",
 (130, 2): "The liver stops clearing bicarbonate from the blood as the alkalosis develops",
 (131, 1): "Giving intravenous bicarbonate promptly",
}
