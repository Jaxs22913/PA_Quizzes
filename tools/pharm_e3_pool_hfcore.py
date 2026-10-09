# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Diuretics and Heart Failure Drugs (Lecture 9), topic 4: heart failure -- causes, types,
decompensation, non-drug therapy, diuretics, angiotensin-converting enzyme inhibitors and beta blockers.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

SOURCE. Diuretics and Heart Failure Drugs.pptx slides 44-60 (picture-only slide 49, the heart failure cascade, was read
by eye into tools/pharm_e3/ocr.json).

WEIGHTING (Dr. McInnis): indications, patient education, adverse effects, contraindications, drug choice, interactions and
monitoring outnumber mechanism plus physiology. The standing Dr. Wood rule is carried by the diuretic items: a drug that is
good for mortality is mandatory, a drug that only relieves symptoms is not.

LEFT OUT ON PURPOSE (no key built on them):
  * the ischemic heart disease share of cases (50-60 percent), the ejection fraction cut-off (slide 46 says under 45
    percent; the current threshold is 40 percent or less, so only "reduced" and "preserved" are keyed: brief decision 9);
  * the sodium (1-3 grams per day) and fluid (under 2 liters per day) limits and the weight gain figure (over 1 pound per
    day over several days): keyed as restriction and daily weights, never as numbers (brief decision 10);
  * "in hospital preferred" and "6-8 weeks" for beta blocker titration (brief decision 10): keyed as stable, very low
    dose, slow titration;
  * switching to an angiotensin receptor blocker for cough or angioedema (said aloud, not on a slide);
  * the left ventricular hypertrophy line of the compensatory response beyond recognition, and the list of
    cardiomyopathy types (alcoholic, viral, hypertrophic) beyond one item.
"""

D = "Diuretics and Heart Failure Drugs.pptx"
IO_CLASS = "Identify diuretics and heart failure drug classes and commonly prescribed diuretics and heart failure drugs"
IO_MOA = "Describe the molecular mechanism of action of diuretics and heart failure drugs"
IO_IND = "Identify indications for commonly used diuretics and heart failure drugs"
IO_TOX = "Summarize side effects and toxic manifestations of diuretics and heart failure drugs"
IO_AE = "Describe adverse effects of diuretics and heart failure drugs"
IO_CONTRA = "Identify contraindications for diuretics and heart failure drugs"
IO_INTER = "Discuss potential drug-drug, drug-food, and drug-herb interactions with diuretics and heart failure drugs"
IO_PROT = "List commonly used protocols and patient monitoring for diuretics and heart failure drugs"
IO_EDU = "Outline appropriate patient education for diuretics and heart failure drugs"

TY = "Types and causes of heart failure"
DE = "Decompensation and non-drug therapy"
DI = "Diuretics in heart failure"
AC = "Angiotensin-converting enzyme inhibitors"
BB = "Beta blockers in heart failure"

QUESTIONS = [

# ---- types and causes (slides 45-49) ------------------------------------------------
{"topic": TY, "io": IO_CLASS, "slot": "physiology",
 "q": "What is the most common cause of heart failure?",
 "opts": [
  ["Ischemic heart disease", "Correct. Ischemic heart disease, including myocardial infarction, accounts for the largest share of heart failure cases."],
  ["Uncontrolled hypertension", "Hypertension is an important cause but accounts for fewer cases than ischemic heart disease."],
  ["Idiopathic dilated cardiomyopathy", "Idiopathic dilated cardiomyopathy is a recognized cause but a less common one than ischemic heart disease."],
  ["Alcoholic cardiomyopathy", "Alcohol, viral illness and drugs can damage the heart, but they cause fewer cases than ischemic heart disease."]],
 "c": 0, "cite": D + ", Slide 45"},

{"topic": TY, "io": IO_CLASS, "slot": "class",
 "q": "Which defect characterizes systolic dysfunction?",
 "opts": [
  ["Decreased contractility", "Correct. Systolic dysfunction is a failure of contraction, assessed as a reduced ejection fraction."],
  ["Impaired relaxation", "Impaired relaxation is the defect of diastolic dysfunction, where ejection fraction is preserved."],
  ["Excess blood leaving the ventricle", "In systolic dysfunction the ventricle ejects too little blood, not too much."],
  ["A failure of the valves to open", "Systolic dysfunction is a muscle problem of weak contraction, not a valve opening problem."]],
 "c": 0, "cite": D + ", Slide 46"},

{"topic": TY, "io": IO_CLASS, "slot": "class",
 "q": "A patient has symptoms of heart failure with a preserved ejection fraction. Which type is this?",
 "opts": [
  ["Diastolic dysfunction", "Correct. Heart failure symptoms with preserved ejection fraction reflect impaired relaxation and filling, or diastolic dysfunction."],
  ["Systolic dysfunction", "Systolic dysfunction shows a reduced ejection fraction, so a preserved fraction points away from it."],
  ["Right-sided valve disease", "Valve disease is not the described type; preserved ejection fraction with symptoms is diastolic dysfunction."],
  ["Dilated cardiomyopathy", "Dilated cardiomyopathy causes systolic dysfunction with a reduced ejection fraction, not a preserved one."]],
 "c": 0, "cite": D + ", Slide 47"},

{"topic": TY, "io": IO_MOA, "slot": "physiology",
 "q": "Which change leads to systolic dysfunction?",
 "opts": [
  ["Loss of myocardial muscle mass", "Correct. Loss of muscle mass, as after an infarction, and dilated cardiomyopathies lower contractility."],
  ["Impaired relaxation from trapped calcium", "Poor relaxation with preserved contraction is the mechanism of diastolic dysfunction, not systolic dysfunction."],
  ["Faster removal of calcium from the cytosol", "Impaired, not faster, calcium removal is what stiffens the ventricle in diastolic dysfunction."],
  ["Longer time for ventricular filling", "Longer filling time does not weaken contraction and would help cardiac output."]],
 "c": 0, "cite": D + ", Slide 46"},

{"topic": TY, "io": IO_MOA, "slot": "physiology",
 "q": "Why do thicker, stiffer ventricles lower cardiac output?",
 "opts": [
  ["They relax poorly, so filling falls", "Correct. Stiff ventricles relax less efficiently, so ventricular filling and cardiac output decrease."],
  ["They contract with too much force", "Contraction is not too forceful; the problem is relaxation and filling."],
  ["They empty the blood too quickly", "The problem is poor filling because the stiff ventricle cannot relax, not overly rapid emptying."],
  ["They lose their ability to hold blood", "The issue is stiffness that limits filling, not loss of volume capacity."]],
 "c": 0, "cite": D + ", Slide 47"},

{"topic": TY, "io": IO_MOA, "slot": "physiology",
 "q": "How does ischemia contribute to diastolic dysfunction?",
 "opts": [
  ["Calcium removal from the cytosol is impaired", "Correct. Ischemia impairs return of calcium from the cytosol to the sarcoplasmic reticulum, so the muscle relaxes poorly."],
  ["Calcium entry into the cell is blocked", "Blocked entry would weaken contraction; the diastolic problem is impaired calcium removal."],
  ["Sodium is retained by the kidney", "Sodium retention raises preload as a compensatory response but is not the diastolic defect of ischemia."],
  ["Contraction becomes too forceful", "Ischemia does not strengthen contraction; it impairs relaxation by trapping calcium."]],
 "c": 0, "cite": D + ", Slide 47"},

{"topic": TY, "io": IO_MOA, "slot": "physiology",
 "q": "Which compensatory response in heart failure increases preload?",
 "opts": [
  ["Sodium and water retention", "Correct. Retaining sodium and water expands blood volume and raises preload."],
  ["Vasoconstriction", "Vasoconstriction raises afterload, the resistance pumped against; preload rises with sodium and water retention."],
  ["Left ventricular hypertrophy", "Hypertrophy is a structural response of the ventricle, not a change in preload."],
  ["Bradycardia", "The compensatory response is tachycardia, driven by sympathetic activation."]],
 "c": 0, "cite": D + ", Slide 48"},

{"topic": TY, "io": IO_MOA, "slot": "physiology",
 "q": "Which compensatory response in heart failure increases afterload?",
 "opts": [
  ["Vasoconstriction", "Correct. Vasoconstriction raises the resistance the ventricle pumps against, or afterload."],
  ["Sodium and water retention", "Retention increases preload, the filling volume, not afterload."],
  ["Increased contractility", "Greater contractility is a sympathetic response that raises output, not the resistance."],
  ["Tachycardia", "Tachycardia raises heart rate, not the resistance the ventricle pumps against."]],
 "c": 0, "cite": D + ", Slide 48"},

{"topic": TY, "io": IO_MOA, "slot": "physiology",
 "q": "Which two neurohormonal systems are activated as cardiac output falls in heart failure?",
 "opts": [
  ["Sympathetic and renin-angiotensin-aldosterone systems", "Correct. Falling cardiac output activates both systems, causing vasoconstriction, faster heart rate and sodium and water retention."],
  ["Parasympathetic and thyroid systems", "Parasympathetic tone falls rather than rises in failure, and the thyroid axis is not what drives the compensatory response."],
  ["Insulin and glucagon", "These regulate glucose and are not the neuroendocrine systems activated by low output."],
  ["Thyroid and growth hormone axes", "These are not the neurohormonal systems driving the compensatory response."]],
 "c": 0, "cite": D + ", Slide 49"},

# ---- decompensation and non-drug therapy (slides 50-52) -----------------------------
{"topic": DE, "io": IO_EDU, "slot": "education",
 "q": "A man with heart failure ran out of his medications two weeks ago and now has marked breathlessness and swelling. Which precipitant of decompensation fits best?",
 "opts": [
  ["Lack of compliance", "Correct. Not taking prescribed therapy is a common precipitant of decompensation."],
  ["Cardiac arrhythmia", "An arrhythmia would need a new irregular or very fast rhythm in the history."],
  ["Pulmonary infection", "An infection would need fever or cough in the history, which this patient does not have."],
  ["Acute anginal chest pain", "Anginal chest pain would need a history of chest pain, which this patient does not describe."]],
 "c": 0, "cite": D + ", Slide 50"},

{"topic": DE, "io": IO_EDU, "slot": "education",
 "q": "A patient with stable heart failure develops a new rapid, irregular pulse and worsening breathlessness. Which precipitant fits best?",
 "opts": [
  ["Cardiac arrhythmia", "Correct. An arrhythmia, such as a new rapid rhythm, is a recognized precipitant of decompensation."],
  ["Lack of compliance", "Nothing in the history points to missed doses; the new rapid, irregular pulse points to a rhythm problem."],
  ["Uncontrolled hypertension", "Hypertension would need a markedly high blood pressure in the history, not an irregular pulse."],
  ["Emotional stress", "Stress can precipitate decompensation but would not explain a new irregular pulse."]],
 "c": 0, "cite": D + ", Slide 50"},

{"topic": DE, "io": IO_EDU, "slot": "education",
 "q": "A patient with heart failure measures a blood pressure of 210 over 120 and is breathless. Which precipitant fits best?",
 "opts": [
  ["Uncontrolled hypertension", "Correct. Uncontrolled hypertension raises afterload and is a recognized precipitant of decompensation."],
  ["Cardiac arrhythmia", "An arrhythmia would need a new irregular or very fast pulse in the history, which is not described."],
  ["Pulmonary infection", "An infection would need fever or productive cough, which are not described."],
  ["Lack of compliance", "Nothing in the history points to missed doses; the blood pressure reading points to uncontrolled hypertension."]],
 "c": 0, "cite": D + ", Slide 50"},

{"topic": DE, "io": IO_EDU, "slot": "education",
 "q": "Which non-cardiac illness can precipitate decompensation in heart failure?",
 "opts": [
  ["Pulmonary infection", "Correct. Pulmonary infection, emotional stress and acute anginal chest pain are listed precipitants."],
  ["Weight loss", "Weight loss is not a listed precipitant; inappropriate medications or fluid overload are."],
  ["Regular exercise", "Physical activity may improve functional status rather than precipitate decompensation."],
  ["A low-sodium diet", "Sodium restriction is part of therapy; excess sodium and fluid can precipitate decompensation."]],
 "c": 0, "cite": D + ", Slide 50"},

{"topic": DE, "io": IO_EDU, "slot": "education",
 "q": "Which dietary advice is part of non-drug therapy for heart failure?",
 "opts": [
  ["Restrict sodium and fluid", "Correct. Limiting dietary sodium and fluid reduces edema and helps functional status."],
  ["Increase sodium to maintain volume", "Extra sodium causes fluid retention and can precipitate decompensation."],
  ["Drink extra water to flush the kidneys", "Extra fluid worsens congestion, so fluid is limited, not increased."],
  ["Eat no protein", "Protein restriction is not part of heart failure therapy; sodium and fluid are restricted."]],
 "c": 0, "cite": D + ", Slide 51"},

{"topic": DE, "io": IO_EDU, "slot": "education",
 "q": "Which lifestyle measure may improve functional status in heart failure?",
 "opts": [
  ["Physical activity", "Correct. Physical activity may improve functional status in patients with heart failure."],
  ["Strict bed rest", "Prolonged rest is not recommended; activity may improve functional status."],
  ["Avoiding all exertion", "Avoiding all exertion is not advised; activity may improve functional status."],
  ["Fluid loading", "Fluid loading worsens congestion; the advice is to limit fluid."]],
 "c": 0, "cite": D + ", Slide 51"},

{"topic": DE, "io": IO_PROT, "slot": "monitoring",
 "q": "Which home measurement best detects worsening fluid overload in heart failure?",
 "opts": [
  ["Daily body weight", "Correct. A rising weight over several days reflects fluid accumulation, so daily weights detect worsening overload."],
  ["Daily oral temperature", "Temperature detects fever, not fluid overload; body weight tracks retained fluid."],
  ["Morning blood glucose", "Glucose monitoring does not reflect fluid status; body weight tracks retained fluid."],
  ["Urine color", "Urine color is not a reliable guide to fluid status; body weight is."]],
 "c": 0, "cite": D + ", Slide 52"},

# ---- diuretics (slides 52-53) -------------------------------------------------------
{"topic": DI, "io": IO_IND, "slot": "drug choice",
 "q": "Which diuretic class is the mainstay of heart failure therapy?",
 "opts": [
  ["Loop diuretics", "Correct. Loop diuretics are the mainstay for relieving congestion in heart failure."],
  ["Thiazide diuretics", "Thiazides are not potent enough for most heart failure patients."],
  ["Potassium-sparing diuretics", "These are weak diuretics, used mainly in combination, and are not the mainstay."],
  ["Carbonic anhydrase inhibitors", "These are weak diuretics whose effect wanes; they are not the mainstay."]],
 "c": 0, "cite": D + ", Slide 52"},

{"topic": DI, "io": IO_IND, "slot": "drug choice",
 "q": "Why are thiazide diuretics unsuitable for most patients with heart failure?",
 "opts": [
  ["They are not potent enough", "Correct. Thiazides are not potent enough to clear the fluid of most heart failure patients."],
  ["They raise potassium dangerously", "Thiazides waste potassium rather than raising it; their limit in heart failure is modest potency."],
  ["They increase preload", "Thiazides promote sodium and water loss, so they do not raise preload; their limit is modest potency."],
  ["They worsen contractility", "Thiazides do not weaken contraction; the limit is their modest potency."]],
 "c": 0, "cite": D + ", Slide 52"},

{"topic": DI, "io": IO_IND, "slot": "indication",
 "q": "How do loop diuretics benefit patients with heart failure?",
 "opts": [
  ["They relieve symptoms by lowering preload", "Correct. Less sodium and water retention lowers preload and gives symptomatic benefit."],
  ["They slow disease progression", "There is no evidence that diuretics slow progression; they give symptomatic relief only."],
  ["They prolong survival", "There is no evidence that diuretics decrease mortality; they give symptomatic relief only."],
  ["They reverse ventricular remodeling", "Reversal of remodeling is an effect of angiotensin-converting enzyme inhibitors, not diuretics."]],
 "c": 0, "cite": D + ", Slide 52"},

{"topic": DI, "io": IO_EDU, "slot": "education",
 "q": "A patient asks whether his loop diuretic will help him live longer. What is the best answer?",
 "opts": [
  ["It eases symptoms but not survival", "Correct. Diuretics give symptomatic relief only, with no evidence of reduced progression or mortality."],
  ["It slows heart failure progression", "There is no evidence that diuretics slow progression; they give symptomatic relief only."],
  ["It must be taken daily to prevent death", "Diuretics do not reduce mortality, so they are not taken for that purpose."],
  ["It reverses the ventricular damage", "Diuretics do not reverse ventricular damage or remodeling; they only relieve congestion."]],
 "c": 0, "cite": D + ", Slide 53"},

# ---- angiotensin-converting enzyme inhibitors (slides 54-56) ------------------------
{"topic": AC, "io": IO_MOA, "slot": "mechanism",
 "q": "Which hemodynamic effect do angiotensin-converting enzyme inhibitors have in heart failure?",
 "opts": [
  ["Lower both preload and afterload", "Correct. These drugs decrease preload and afterload and also lower sympathetic activation."],
  ["Raise preload and lower afterload", "They lower preload as well as afterload; raising preload would worsen congestion."],
  ["Lower preload and raise afterload", "They lower afterload too; raising it would increase the load on the failing ventricle."],
  ["Raise both preload and afterload", "They lower both loads; raising both would worsen failure and is the opposite of their action."]],
 "c": 0, "cite": D + ", Slide 54"},

{"topic": AC, "io": IO_IND, "slot": "drug choice",
 "q": "Which drug class both slows heart failure progression and decreases mortality?",
 "opts": [
  ["Angiotensin-converting enzyme inhibitors", "Correct. In heart failure with reduced ejection fraction these drugs slow progression and decrease mortality, which is why they are mandatory there."],
  ["Loop diuretics", "Loops relieve symptoms but have no evidence of slowing progression or lowering mortality."],
  ["Thiazide diuretics", "Thiazides are not potent enough for most patients and do not lower mortality."],
  ["Cardiac glycosides such as digoxin", "Digoxin improves symptoms but has no survival benefit, unlike the classes that prolong survival."]],
 "c": 0, "cite": D + ", Slide 54"},

{"topic": AC, "io": IO_MOA, "slot": "mechanism",
 "q": "Which effect on the ventricle do angiotensin-converting enzyme inhibitors have in heart failure?",
 "opts": [
  ["Less hypertrophy and remodeling", "Correct. They decrease left ventricular hypertrophy, dilation and remodeling, which slows progression."],
  ["More remodeling and dilation", "They reduce remodeling and dilation; increasing them would worsen failure."],
  ["More sympathetic activation", "They decrease sympathetic activation, which is part of their benefit in heart failure."],
  ["Thicker ventricular walls", "They decrease hypertrophy, or wall thickening, rather than increasing it."]],
 "c": 0, "cite": D + ", Slide 54"},

{"topic": AC, "io": IO_IND, "slot": "indication",
 "q": "Which benefit is expected from an angiotensin-converting enzyme inhibitor in heart failure?",
 "opts": [
  ["Better exercise tolerance", "Correct. These drugs improve exercise tolerance, and in heart failure with reduced ejection fraction they also bring fewer admissions and longer survival."],
  ["Greater force of contraction", "A direct increase in contractile force is the action of inotropes such as digoxin, not of these drugs."],
  ["A faster heart rate", "They do not speed the heart; they lower sympathetic activation."],
  ["Higher sympathetic tone", "They lower sympathetic activation, which is part of their benefit."]],
 "c": 0, "cite": D + ", Slide 55"},

{"topic": AC, "io": IO_AE, "slot": "adverse effect",
 "q": "Which effect on the kidney can angiotensin-converting enzyme inhibitors cause in heart failure?",
 "opts": [
  ["Impaired renal function", "Correct. Impairment of renal function is a recognized problem with these drugs."],
  ["Kidney stones", "Stones are not a listed problem; the listed kidney problem is impaired renal function."],
  ["Excessive urine volume", "They do not cause a large increase in urine volume; they can reduce renal function."],
  ["Improved filtration in every patient", "These drugs can impair renal function rather than improve it."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": AC, "io": IO_AE, "slot": "adverse effect",
 "q": "Which electrolyte change can angiotensin-converting enzyme inhibitors cause?",
 "opts": [
  ["Elevated serum potassium", "Correct. These drugs raise serum potassium, so levels are watched, especially with other potassium-raising drugs."],
  ["Low serum potassium", "Low potassium is the usual result of loops and thiazides; these drugs raise it."],
  ["Low serum calcium", "Calcium is not the electrolyte named for these drugs; serum potassium is the one that rises."],
  ["High serum chloride", "Chloride is not the electrolyte named for these drugs; serum potassium is the one that rises."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": AC, "io": IO_AE, "slot": "adverse effect",
 "q": "Which respiratory adverse effect is associated with angiotensin-converting enzyme inhibitors?",
 "opts": [
  ["Cough", "Correct. Cough is a recognized adverse effect of these drugs."],
  ["Bronchospasm", "Bronchospasm is not the listed respiratory problem; cough is."],
  ["Hemoptysis", "Hemoptysis is not a listed effect of these drugs; the respiratory effect listed is cough."],
  ["Pleural effusion", "Pleural effusion is not a listed effect of these drugs; cough is."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": AC, "io": IO_AE, "slot": "adverse effect",
 "q": "Which life-threatening reaction involves swelling of the lips, tongue and throat during angiotensin-converting enzyme inhibitor therapy?",
 "opts": [
  ["Angioedema", "Correct. Angioedema is a recognized and potentially dangerous adverse reaction to these drugs."],
  ["Peripheral edema", "Peripheral edema is swelling of the legs, not of the lips, tongue and throat."],
  ["Pulmonary edema", "Pulmonary edema is fluid in the lungs, not swelling of the lips, tongue and throat."],
  ["Ascites", "Ascites is fluid in the abdomen, not swelling of the lips, tongue and throat."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": AC, "io": IO_PROT, "slot": "monitoring",
 "q": "A patient on a loop diuretic is started on an angiotensin-converting enzyme inhibitor. What should be monitored?",
 "opts": [
  ["Serum potassium and renal function", "Correct. The inhibitor can raise potassium and impair renal function, and the loop pushes potassium the other way."],
  ["Serum calcium and phosphate", "These are not the values most affected by the combination; potassium and renal function are."],
  ["Blood glucose and ketones", "These are not the values most affected by the combination; potassium and renal function are."],
  ["White blood cell count", "This is not a problem listed for the combination; potassium and renal function are."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": AC, "io": IO_INTER, "slot": "interaction",
 "q": "How do loop diuretics and angiotensin-converting enzyme inhibitors differ in their effect on serum potassium?",
 "opts": [
  ["Loops lower it and the inhibitors raise it", "Correct. Loops increase potassium excretion, while angiotensin-converting enzyme inhibitors elevate serum potassium."],
  ["Both lower it", "The inhibitors raise potassium, so only the loop lowers it by increasing excretion."],
  ["Both raise it", "Loops lower potassium by increasing its excretion, so only the inhibitor raises it."],
  ["Loops raise it and the inhibitors lower it", "This is reversed; loops lower potassium and the inhibitors raise it."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": AC, "io": IO_IND, "slot": "drug choice",
 "q": "Which two drug classes should a patient with heart failure and a reduced ejection fraction be on irrespective of symptoms?",
 "opts": [
  ["Angiotensin-converting enzyme inhibitor and beta blocker", "Correct. Patients should be on both classes irrespective of symptoms, since both lower mortality."],
  ["Loop diuretic and cardiac glycoside", "A loop diuretic and digoxin relieve symptoms but do not lower mortality, so they are not required for every patient."],
  ["Thiazide diuretic and dihydropyridine calcium channel blocker", "Neither is required for every patient with heart failure; the required pair lowers mortality."],
  ["Loop diuretic and thiazide diuretic", "Diuretics relieve symptoms but do not lower mortality, so neither is required for every patient."]],
 "c": 0, "cite": D + ", Slide 60"},

# ---- beta blockers (slides 57-60) ---------------------------------------------------
{"topic": BB, "io": IO_CONTRA, "slot": "contraindication",
 "q": "Why were beta blockers classically considered contraindicated in heart failure?",
 "opts": [
  ["They can worsen heart failure", "Correct. Lowering heart rate and contractility can decompensate a failing heart, so they were once avoided."],
  ["They raise serum potassium", "Raising potassium is not the reason; the concern was weakening of the failing heart."],
  ["They cause fluid loss", "Fluid loss is a diuretic effect and not the concern with beta blockers."],
  ["They block the renin system", "Blocking the renin system would benefit heart failure and is not the reason."]],
 "c": 0, "cite": D + ", Slide 57"},

{"topic": BB, "io": IO_CLASS, "slot": "class",
 "q": "Which three beta blockers reduce mortality in heart failure?",
 "opts": [
  ["Carvedilol, metoprolol succinate, bisoprolol", "Correct. These three have been shown to lower mortality in heart failure."],
  ["Metoprolol tartrate, atenolol, nadolol", "Only the extended-release succinate form of metoprolol is named, and atenolol and nadolol show no mortality benefit in heart failure."],
  ["Propranolol, labetalol, acebutolol", "None of these three is among the agents with a proven mortality benefit in heart failure."],
  ["Esmolol, timolol, labetalol", "None of these three is among the agents with a proven mortality benefit in heart failure."]],
 "c": 0, "cite": D + ", Slide 57"},

{"topic": BB, "io": IO_IND, "slot": "drug choice",
 "q": "A patient with class III heart failure takes a loop diuretic and an angiotensin-converting enzyme inhibitor. Which drug should be added to lower mortality?",
 "opts": [
  ["Carvedilol", "Correct. Carvedilol is one of the three beta blockers with a mortality benefit and is first-line therapy."],
  ["Digoxin", "Digoxin improves symptoms but has no survival benefit, unlike the classes that prolong survival."],
  ["Hydrochlorothiazide", "A thiazide is not potent enough for most patients and does not lower mortality."],
  ["Atenolol", "Atenolol is not one of the beta blockers with a proven mortality benefit in heart failure."]],
 "c": 0, "cite": D + ", Slide 60"},

{"topic": BB, "io": IO_PROT, "slot": "protocol",
 "q": "How should a beta blocker be started in a patient with heart failure?",
 "opts": [
  ["At a very low dose, then raised slowly", "Correct. Beta blockers are started at very low doses and titrated up slowly while watching for worsening failure."],
  ["At the full target dose", "A full dose can decompensate a failing heart, so the start is very low."],
  ["At a low dose, stopped once symptoms ease", "The goal is long-term therapy with slow titration, not stopping when symptoms ease."],
  ["At a full dose after a loading period", "There is no loading period; the start is very low with slow titration."]],
 "c": 0, "cite": D + ", Slide 58"},

{"topic": BB, "io": IO_PROT, "slot": "protocol",
 "q": "In which state should a heart failure patient be before a beta blocker is started?",
 "opts": [
  ["Clinically stable", "Correct. The patient should be stable before a beta blocker is initiated."],
  ["Acutely decompensated", "Starting a beta blocker in an acutely decompensated patient can worsen failure."],
  ["Hypotensive and congested", "Hypotension with congestion is an unstable state in which a beta blocker should not be started."],
  ["Receiving intravenous inotropes", "Dependence on intravenous inotropes is an unstable state, not the stable state required."]],
 "c": 0, "cite": D + ", Slide 58"},

{"topic": BB, "io": IO_PROT, "slot": "monitoring",
 "q": "What should be monitored after a beta blocker is started in heart failure?",
 "opts": [
  ["Signs and symptoms of worsening failure", "Correct. Worsening heart failure is the main risk after starting, so signs and symptoms are monitored."],
  ["A serum digoxin level", "A digoxin level is monitored for digoxin, not for a beta blocker."],
  ["The international normalized ratio", "This is a warfarin test and is not the monitoring step for a beta blocker."],
  ["Serum uric acid", "Uric acid is followed with loop and thiazide diuretics, not with beta blockers."]],
 "c": 0, "cite": D + ", Slide 58"},

{"topic": BB, "io": IO_IND, "slot": "indication",
 "q": "Which benefit do beta blockers provide in heart failure?",
 "opts": [
  ["Fewer hospitalizations", "Correct. Beta blockers decrease hospitalizations and the need for transplant, and lower mortality."],
  ["Immediate relief of congestion", "Beta blockers do not relieve congestion quickly; diuretics do."],
  ["An immediate rise in contractility", "They lower heart rate and contractility; benefit comes with slow titration."],
  ["Prevention of sodium retention", "Preventing sodium retention is not their action; diuretics reduce retention."]],
 "c": 0, "cite": D + ", Slide 59"},

{"topic": BB, "io": IO_IND, "slot": "drug choice",
 "q": "Which drug class is first-line therapy for heart failure of functional class II to IV, alongside angiotensin-converting enzyme inhibitors?",
 "opts": [
  ["Beta blockers", "Correct. Beta blockers are first-line therapy for heart failure of functional class II to IV."],
  ["Digoxin", "Digoxin is an add-on for symptoms in patients on optimal therapy, not first-line therapy."],
  ["Thiazide diuretics", "Thiazides are not potent enough for most patients and are not first-line therapy."],
  ["Calcium channel blockers", "Calcium channel blockers are not first-line therapy for heart failure."]],
 "c": 0, "cite": D + ", Slide 60"},

{"topic": TY, "io": IO_CLASS, "slot": "physiology",
 "q": "Which exposure is a recognized cause of cardiomyopathy leading to heart failure?",
 "opts": [
  ["Alcohol", "Correct. Alcoholic, viral and hypertrophic cardiomyopathies, and drug-induced damage, are recognized causes of heart failure."],
  ["Moderate exercise", "Exercise does not damage the heart muscle; physical activity may improve functional status."],
  ["Low sodium intake", "Low sodium intake is part of therapy and does not cause cardiomyopathy."],
  ["Vitamin C intake", "Vitamin C is not a recognized cause of cardiomyopathy; alcohol is."]],
 "c": 0, "cite": D + ", Slide 45"},

{"topic": AC, "io": IO_AE, "slot": "adverse effect",
 "q": "Which blood pressure problem can angiotensin-converting enzyme inhibitors cause in heart failure?",
 "opts": [
  ["Hypotension", "Correct. Hypotension is a recognized problem, particularly with other blood pressure-lowering drugs."],
  ["Hypertensive crisis", "These drugs lower blood pressure; they do not cause a hypertensive crisis."],
  ["Orthostatic hypertension", "These drugs lower, not raise, blood pressure, so the problem is hypotension."],
  ["Pulmonary hypertension", "Pulmonary hypertension is not a listed problem; hypotension is."]],
 "c": 0, "cite": D + ", Slide 56"},

{"topic": BB, "io": IO_IND, "slot": "indication",
 "q": "Which hemodynamic improvement do beta blockers eventually produce in heart failure?",
 "opts": [
  ["A rise in ejection fraction", "Correct. With long-term therapy beta blockers improve hemodynamics, including an increase in ejection fraction."],
  ["A fall in ejection fraction", "Ejection fraction rises with long-term beta blocker therapy rather than falling."],
  ["A rise in resting heart rate", "Beta blockers lower heart rate and do not raise it; ejection fraction is what improves."],
  ["A rise in cardiac preload", "Beta blockers do not raise preload; sodium and water retention does."]],
 "c": 0, "cite": D + ", Slide 59"},

{"topic": BB, "io": IO_IND, "slot": "indication",
 "q": "Beta blockers decrease the need for which procedure in heart failure?",
 "opts": [
  ["Heart transplant", "Correct. Beta blockers decrease the need for transplant, along with hospitalizations and mortality."],
  ["Coronary stenting", "Stenting is not a listed benefit; the decreased need is for transplant."],
  ["Valve replacement", "Valve replacement is not a listed benefit; the decreased need is for transplant."],
  ["Pacemaker placement", "Pacemaker placement is not a listed benefit; the decreased need is for transplant."]],
 "c": 0, "cite": D + ", Slide 59"},

]
