# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 -- Pulmonary Infections, Asthma and COPD/COLD (Lecture 11), topic: chronic obstructive pulmonary
disease, its drug therapy by group, smoking cessation and immunizations.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. The key is authored FIRST (c == 0);
pharm_e3_partition.py rotates it (numeric option sets are sorted ascending instead, WRITER.md rule 8).

SOURCE. Pulmonology-2.pptx slides 100-108: the definition (101, with the lung-function figure, its text read by eye into
tools/pharm_e3/ocr.json under "L11": symptoms develop only after a significant decline in forced expiratory volume in
1 second), the drug therapy table by group A to D and the measures for all groups (102), smoking and its cessation
(103), the six cessation agents (104), bupropion (105), nicotine replacement (106), varenicline (107) and immunizations
(108). Distractor explanations also use neighbouring slides where they supply the replacing fact (57 asthma, 62 viral
triggers, 70 long-acting beta-2 agonists not alone in asthma, 73 inhaled corticosteroid thrush and growth, 42 rifampin's
orange secretions, 39 and 45 tuberculosis-drug hepatitis, 86 anticholinergics).

The treatment-group stems describe symptoms in the table's own words (breathless with strenuous exercise; has to stop
to catch breath on level ground) rather than by the symptom-test score, so no abbreviation is needed.

WRITER.md v1 (2026-10-15): every distractor carries its misconception as a third element (mis); slides only (this deck
has no speaker notes); slides win on conflict. Keyed as the slide gives it, with a "current guidelines differ" note in
the guide: the ABCD groups (102; GOLD 2023 merged C and D into E) and varenicline's black box warning (107; the FDA
removed it in 2016).

LEFT OUT ON PURPOSE:
  * every dose: the bupropion schedule (105) and any nicotine strength;
  * the percentages "15-20% of smokers" and ">85% of cases" (103) as keys;
  * the symptom-test score cut-offs (102) as keys;
  * the pneumococcal vaccine brand (108) as the only acceptable product (the item asks for the vaccine, not the brand);
  * tiotropium "COPD only" (86): never keyed.
mis = misconception tag on every distractor (WRITER.md rule 5)
"""

D = "Pulmonology-2.pptx"
IO_CLASS = "Identify respiratory drug classes and commonly prescribed drugs for pulmonary infections, asthma, and COPD/COLD"
IO_MOA = "Describe the molecular mechanism of action of drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_IND = "Identify indications for drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_ADME = "Describe absorption, distribution, metabolism, and excretion of drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_TOX = "Summarize side effects and toxic manifestations of respiratory drugs"
IO_AE = "Describe adverse effects of drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_CONTRA = "Identify contraindications for drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_INTER = "Discuss potential drug-drug, drug-food, and drug-herb interactions with drugs used for pulmonary infections, asthma, and COPD/COLD"
IO_PROT = "List commonly used protocols and patient monitoring for pulmonary infections, asthma, and COPD/COLD"
IO_EDU = "Outline appropriate patient education for drugs used for pulmonary infections, asthma, and COPD/COLD"

MECH, ADJ, REV, LAY, STAGE, RULED, COMP = ("confused mechanism or drug class", "adjacent fact", "reversed direction or value",
                                           "common lay belief", "wrong stage or severity", "ruled out by a stated finding",
                                           "competing diagnosis")


def Q(topic, io, slot, q, opts, slide):
    return {"topic": topic, "io": io, "slot": slot, "q": q, "opts": opts, "c": 0, "cite": "%s, Slide %d" % (D, slide)}


QUESTIONS = [

# ---- the disease (slide 101) -----------------------------------------------------------------------
Q("Chronic obstructive pulmonary disease", IO_IND, "physiology",
  "Which feature of the inflammation in chronic obstructive pulmonary disease distinguishes it from asthma?",
  [["It is generally not fully reversible", "Correct. Chronic obstructive pulmonary disease is chronic inflammation of the airways and lung parenchyma that is generally not fully reversible, with an accelerated decline in lung function."],
   ["It causes widespread reversible narrowing", "Widespread reversible narrowing of the bronchial airways characterizes asthma; the inflammation of chronic obstructive pulmonary disease is generally not fully reversible.", COMP],
   ["It is eosinophilic in the bronchial mucosa", "Eosinophilic inflammation of the bronchial mucosa is how asthma is characterized; chronic obstructive pulmonary disease is inflammation that is generally not fully reversible.", COMP],
   ["It spares the lung parenchyma", "The inflammation involves the airways and the lung parenchyma; what sets chronic obstructive pulmonary disease apart is that it is generally not fully reversible.", REV]], 101),

Q("Chronic obstructive pulmonary disease", IO_IND, "physiology",
  "In chronic obstructive pulmonary disease, when do symptoms generally develop?",
  [["After a significant decline in lung function", "Correct. Symptoms generally develop only after a significant decline in forced expiratory volume in 1 second (FEV1) has occurred, and they progress as lung function deteriorates further."],
   ["Before lung function begins to decline", "Lung function falls first; patients stay asymptomatic while it is normal and early in its decline, and symptoms appear after a significant fall in forced expiratory volume in 1 second (FEV1).", REV],
   ["As soon as lung function first falls", "Patients remain asymptomatic in the first stretch of reduced lung function; symptoms develop only after a significant decline in forced expiratory volume in 1 second (FEV1).", STAGE],
   ["When lung function returns to normal", "Chronic obstructive pulmonary disease is generally not fully reversible, and symptoms rise as forced expiratory volume in 1 second (FEV1) keeps falling after a significant decline.", REV]], 101),

# ---- drug therapy by group (slide 102) -------------------------------------------------------------
Q("Treatment groups", IO_PROT, "protocol",
  "Which measure is recommended for every patient with chronic obstructive pulmonary disease, whatever the treatment group?",
  [["Pneumococcal vaccination", "Correct. Measures for all groups are avoiding risk factors such as smoking, annual influenza and pneumococcal vaccination, regular physical activity, inhaler technique review, long-term oxygen if chronically hypoxemic and pulmonary rehabilitation."],
   ["A regular long-acting bronchodilator", "A regular long-acting bronchodilator is the treatment for group B (and the long-acting muscarinic antagonist for groups C and D), not a measure for every patient; pneumococcal vaccination is.", STAGE],
   ["An inhaled glucocorticoid", "A combination glucocorticoid-long-acting beta-2 agonist inhaler is considered in group D when asthma features overlap; pneumococcal vaccination applies to every group.", STAGE],
   ["A long-acting muscarinic antagonist", "A regular long-acting muscarinic antagonist is the treatment for groups C and D; the measure for every group is pneumococcal vaccination, with annual influenza vaccination.", STAGE]], 102),

Q("Treatment groups", IO_IND, "indication",
  "For which patients with chronic obstructive pulmonary disease is long-term oxygen therapy listed?",
  [["Those with persistent hypoxemia", "Correct. Long-term oxygen therapy is listed, for patients in any group, if there is chronic (persistent) hypoxemia."],
   ["Those in the high-risk groups", "High risk (two or more exacerbations a year) moves a patient to group C or D and decides the inhaler, not oxygen; oxygen is listed for chronic hypoxemia.", ADJ],
   ["Those with asthma overlap", "Features of asthma overlap make a combination glucocorticoid-long-acting beta-2 agonist inhaler preferred in group D; long-term oxygen is for chronic hypoxemia.", ADJ],
   ["Those who still smoke", "Smokers are told to avoid the risk factor and are offered cessation; long-term oxygen therapy is listed for chronic hypoxemia.", LAY]], 102),

Q("Treatment groups", IO_PROT, "drug choice",
  "A patient with chronic obstructive pulmonary disease is breathless only with strenuous exercise and had no exacerbations last year. What is the suggested treatment?",
  [["A short-acting bronchodilator as needed", "Correct. Group A (mild or infrequent symptoms, 0 or 1 exacerbation without hospitalization) is treated with a short-acting bronchodilator, beta-2 agonist, antimuscarinic or both, as needed."],
   ["A regular long-acting bronchodilator", "A regular long-acting bronchodilator is for group B, the more symptomatic low-risk patient; mild symptoms with no exacerbations is group A, a short-acting bronchodilator as needed.", STAGE],
   ["A regular long-acting muscarinic antagonist", "A regular long-acting muscarinic antagonist is an option for groups B, C and D; this low-risk, mildly symptomatic patient is group A, which needs only a short-acting bronchodilator as needed.", STAGE],
   ["A long-acting beta-2 agonist plus muscarinic antagonist", "The long-acting combination is reserved for group D with severe breathlessness; this patient is group A and needs only a short-acting bronchodilator as needed.", STAGE]], 102),

Q("Treatment groups", IO_PROT, "drug choice",
  "A patient with chronic obstructive pulmonary disease must stop to catch breath when walking on level ground and had one exacerbation last year without hospitalization. What is the suggested regular treatment?",
  [["A long-acting muscarinic antagonist or beta-2 agonist", "Correct. Group B (more symptomatic, low risk) gets regular treatment with one long-acting bronchodilator, either a muscarinic antagonist or a beta-2 agonist by patient preference, plus a short-acting bronchodilator as needed."],
   ["A short-acting bronchodilator as needed alone", "As-needed short-acting bronchodilator alone is group A, the less symptomatic patient; stopping to catch breath on level ground makes this group B, which needs a regular long-acting bronchodilator.", STAGE],
   ["An inhaled glucocorticoid with a long-acting beta-2 agonist", "A glucocorticoid-long-acting beta-2 agonist inhaler is considered in group D when asthma features overlap; this low-risk patient is group B.", STAGE],
   ["A long-acting beta-2 agonist plus muscarinic antagonist", "The two long-acting bronchodilators together are for group D with severe breathlessness; with only one exacerbation and no hospitalization this patient is group B.", RULED]], 102),

Q("Treatment groups", IO_PROT, "drug choice",
  "A patient with chronic obstructive pulmonary disease has mild symptoms but had two exacerbations last year, one needing hospitalization. What is the suggested regular treatment?",
  [["A regular long-acting muscarinic antagonist", "Correct. Group C (less symptomatic, high risk: two or more exacerbations a year with one or more hospitalized) gets regular treatment with a long-acting muscarinic antagonist, with a short-acting beta-2 agonist for relief."],
   ["A regular long-acting beta-2 agonist", "A long-acting beta-2 agonist is one of the two group B choices; group C, the high-risk patient with mild symptoms, gets a long-acting muscarinic antagonist.", MECH],
   ["A short-acting bronchodilator as needed", "As-needed short-acting bronchodilator alone is for group A, the low-risk patient; two exacerbations with a hospitalization make this patient high risk, group C.", RULED],
   ["An inhaled glucocorticoid with a long-acting beta-2 agonist", "A glucocorticoid-long-acting beta-2 agonist inhaler is considered in group D when asthma features overlap; group C gets a long-acting muscarinic antagonist.", STAGE]], 102),

# Recording pass: Dr. Wood, 1:39:46-1:42:21, "compare and contrast that to the asthma management": in chronic
# obstructive pulmonary disease a long-acting bronchodilator alone is fine ("asthma can't do a SABA or a LABA by itself.
# Here you can"), the anti-inflammatories sit at the bottom of the list, and no biologics are used (slides 70 and 102).
Q("Treatment groups", IO_PROT, "drug choice",
  "Which regular therapy is acceptable on its own in chronic obstructive pulmonary disease but never on its own in asthma?",
  [["A long-acting beta-2 agonist", "Correct. In chronic obstructive pulmonary disease a long-acting muscarinic antagonist or a long-acting beta-2 agonist alone is regular treatment; in asthma a long-acting beta-2 agonist is never used alone."],
   ["An inhaled corticosteroid", "In asthma the inhaled corticosteroid is the mainstay controller; in chronic obstructive pulmonary disease a steroid is added only at the top group, combined, when asthma features overlap.", REV],
   ["A leukotriene receptor antagonist", "A leukotriene receptor antagonist is an other controller option in asthma and is not on the chronic obstructive pulmonary disease table; long-acting bronchodilators are.", ADJ],
   ["An anti-immunoglobulin E antibody", "Omalizumab is an asthma add-on for the top step; the chronic obstructive pulmonary disease groups list bronchodilators and no biologics.", ADJ]], 102),

Q("Treatment groups", IO_PROT, "drug choice",
  "A high-risk patient with chronic obstructive pulmonary disease has severe breathlessness and no features of asthma. What is the suggested regular treatment?",
  [["A long-acting beta-2 agonist plus muscarinic antagonist", "Correct. Group D (more symptomatic, high risk) gets a long-acting muscarinic antagonist or, if breathlessness is severe, the combination of a long-acting beta-2 agonist and a long-acting muscarinic antagonist."],
   ["A long-acting muscarinic antagonist alone", "A long-acting muscarinic antagonist alone is the group D start when breathlessness is not severe, and the group C treatment; severe breathlessness calls for the combination.", STAGE],
   ["A short-acting bronchodilator as needed", "As-needed short-acting bronchodilator alone is the group A treatment; a high-risk, severely breathless patient is group D.", STAGE],
   ["An inhaled glucocorticoid with a long-acting beta-2 agonist", "The glucocorticoid-long-acting beta-2 agonist inhaler may be preferred only when features of asthma overlap, which this patient does not have.", RULED]], 102),

Q("Treatment groups", IO_PROT, "drug choice",
  "A patient with chronic obstructive pulmonary disease has frequent hospitalized exacerbations, marked breathlessness and features that overlap with asthma. Which inhaler may be preferred?",
  [["A glucocorticoid plus long-acting beta-2 agonist", "Correct. In group D a combination glucocorticoid-long-acting beta-2 agonist inhaler may be preferred if features of asthma and chronic obstructive pulmonary disease overlap."],
   ["A long-acting beta-2 agonist on its own", "A long-acting beta-2 agonist is not used alone in asthma, and asthma overlap is the reason a glucocorticoid-long-acting beta-2 agonist combination may be preferred.", RULED],
   ["A long-acting muscarinic antagonist on its own", "A long-acting muscarinic antagonist alone is the group C and milder group D treatment; asthma overlap makes the glucocorticoid-long-acting beta-2 agonist inhaler preferable.", STAGE],
   ["A short-acting beta-2 agonist plus antimuscarinic", "The short-acting beta-2 agonist and antimuscarinic combination is an as-needed group A choice; overlap with asthma in group D favors the glucocorticoid-long-acting beta-2 agonist inhaler.", STAGE]], 102),

Q("Treatment groups", IO_PROT, "protocol",
  "Which finding places a patient with chronic obstructive pulmonary disease in a high-risk treatment group?",
  [["Two exacerbations a year, one hospitalized", "Correct. High risk (groups C and D) is two or more exacerbations per year with one or more leading to hospitalization; 0 or 1 exacerbation without hospitalization is low risk."],
   ["Breathlessness walking on level ground", "Breathlessness on level ground is the symptom axis, which separates more symptomatic (B, D) from less symptomatic (A, C) patients; risk is set by exacerbations.", COMP],
   ["Chronic hypoxemia needing oxygen", "Chronic hypoxemia calls for long-term oxygen therapy in any group; the high-risk groups are defined by two or more exacerbations a year with a hospitalization.", ADJ],
   ["One exacerbation without hospitalization", "Zero or one exacerbation in the past year without hospitalization is the low-risk definition (groups A and B); high risk needs two or more with a hospitalization.", STAGE]], 102),

# ---- smoking and its cessation (slide 103) ---------------------------------------------------------
Q("Smoking cessation", IO_EDU, "education",
  "In a patient with chronic obstructive pulmonary disease, what can stopping smoking do to the decline in ventilatory function?",
  [["Return it to the normal age-related rate", "Correct. Smoking cessation can return the decline in ventilatory function to the normal age-related rate and reduce the risk of lung cancer."],
   ["Reverse the existing obstruction fully", "Chronic obstructive pulmonary disease is generally not fully reversible; stopping smoking returns the rate of decline to the normal age-related rate.", LAY],
   ["Stop age-related decline entirely", "Age-related decline continues after quitting; what cessation can do is return the decline to the normal age-related rate.", REV],
   ["Speed it up for the first year", "Quitting does not accelerate the decline; it can return the decline in ventilatory function to the normal age-related rate and reduce lung cancer risk.", REV]], 103),

Q("Smoking cessation", IO_EDU, "education",
  "Which factor directly correlates with a patient's success in quitting smoking?",
  [["Intensity and frequency of counseling", "Correct. Effective programs combine pharmacologic intervention with counseling, and the intensity and frequency of counseling directly correlate with the success of quitting."],
   ["Using medication without counseling", "Effective programs combine drug therapy with counseling rather than replacing it; the intensity and frequency of counseling correlate with success.", REV],
   ["Daily cigarette count at the start", "The level of dependence guides the dose and duration of nicotine replacement, but the factor tied directly to quitting success is the intensity and frequency of counseling.", ADJ],
   ["Length of the smoking history", "Quitting is a complex physical, psychological and social issue; the factor that directly correlates with success is the intensity and frequency of counseling.", LAY]], 103),

# ---- the agents (slides 104-107) -------------------------------------------------------------------
Q("Smoking cessation agents", IO_CLASS, "class",
  "Which smoking cessation agent is marketed as Zyban?",
  [["Bupropion", "Correct. Bupropion sustained release (Zyban) is one of the six listed smoking cessation agents, with the nicotine patch, gum, spray and inhaler, and varenicline (Chantix)."],
   ["Varenicline", "Varenicline is marketed as Chantix, a partial nicotine receptor agonist; Zyban is bupropion sustained release.", ADJ],
   ["Nicotine polacrilex", "Nicotine polacrilex is the nicotine gum, available over the counter; Zyban is bupropion sustained release.", ADJ],
   ["Nicotine transdermal system", "The nicotine transdermal system is the patch, available over the counter; Zyban is bupropion sustained release.", ADJ]], 104),

Q("Smoking cessation agents", IO_EDU, "education",
  "In which form is nicotine polacrilex given?",
  [["Gum", "Correct. Nicotine polacrilex is the nicotine gum; with the patches, the gum is available over the counter."],
   ["Patch", "The patch is the nicotine transdermal system; nicotine polacrilex is the gum.", ADJ],
   ["Spray", "The nicotine spray is a separate listed form; nicotine polacrilex is the gum.", ADJ],
   ["Inhaler", "The nicotine inhaler is a separate listed form; nicotine polacrilex is the gum.", ADJ]], 104),

Q("Bupropion", IO_MOA, "mechanism",
  "How is bupropion thought to help a smoker quit?",
  [["It inhibits norepinephrine and dopamine uptake", "Correct. Nicotine indirectly activates epinephrine and dopamine in the central nervous system, and bupropion is postulated to mimic these effects because it inhibits the uptake of norepinephrine and dopamine."],
   ["It partially stimulates nicotine receptors", "Partial nicotine receptor agonism, to a lesser degree than nicotine, is varenicline's mechanism; bupropion inhibits norepinephrine and dopamine uptake.", MECH],
   ["It replaces nicotine to ease withdrawal", "Replacing nicotine to reduce craving and withdrawal is what the patch, gum, spray and inhaler do; bupropion inhibits norepinephrine and dopamine uptake.", MECH],
   ["It blocks muscarinic acetylcholine receptors", "Blocking acetylcholine at muscarinic receptors is the anticholinergic bronchodilator mechanism; bupropion inhibits norepinephrine and dopamine uptake.", MECH]], 105),

Q("Bupropion", IO_CONTRA, "contraindication",
  "A patient with a seizure disorder asks for help to stop smoking. Which agent should be avoided?",
  [["Bupropion", "Correct. Bupropion sustained release is to be avoided in patients with seizure disorders and in patients taking monoamine oxidase inhibitors."],
   ["Varenicline", "Varenicline's listed side effects are nausea, sleep disturbance and headache, with a black box warning for neuropsychiatric events; the agent to avoid in a seizure disorder is bupropion.", ADJ],
   ["Nicotine gum", "Nicotine replacement calls for caution in cardiovascular problems (tachyarrhythmias, hypertension); the agent to avoid in a seizure disorder is bupropion.", ADJ],
   ["Nicotine patch", "The patch reduces craving and withdrawal and needs caution in cardiovascular problems; bupropion is the agent avoided in seizure disorders.", ADJ]], 105),

Q("Bupropion", IO_INTER, "interaction",
  "In which patient should bupropion be avoided rather than used with caution?",
  [["One taking a monoamine oxidase inhibitor", "Correct. Bupropion is avoided in patients taking monoamine oxidase inhibitors and in seizure disorders; noradrenergic antidepressants (tricyclics and venlafaxine) call only for caution."],
   ["One taking a tricyclic antidepressant", "Tricyclic antidepressants, like venlafaxine, are noradrenergic antidepressants that call for caution with bupropion; avoidance is for monoamine oxidase inhibitors.", STAGE],
   ["One with cardiovascular disease", "Cardiovascular problems are the caution for nicotine replacement (tachyarrhythmias, hypertension); bupropion is avoided with monoamine oxidase inhibitors and seizure disorders.", ADJ],
   ["One with a history of depression", "Depression and suicidal ideation are the neuropsychiatric events in varenicline's black box warning; bupropion is avoided with monoamine oxidase inhibitors and seizure disorders.", ADJ]], 105),

Q("Nicotine replacement", IO_IND, "indication",
  "What is the purpose of the nicotine replacement agents?",
  [["To reduce craving and physical withdrawal", "Correct. Nicotine replacement reduces the craving to smoke and minimizes physical withdrawal (anxiety, irritability, restlessness, insomnia, headache, depression and nausea)."],
   ["To inhibit norepinephrine and dopamine uptake", "Inhibiting norepinephrine and dopamine uptake is bupropion's postulated mechanism; nicotine replacement reduces craving and physical withdrawal.", MECH],
   ["To partly block the nicotine receptor", "Varenicline is the partial nicotine receptor agonist; nicotine replacement supplies nicotine to reduce craving and physical withdrawal.", MECH],
   ["To make cigarettes taste unpleasant", "Nicotine replacement does not work by aversion; it reduces the craving to smoke and minimizes physical withdrawal symptoms.", LAY]], 106),

Q("Nicotine replacement", IO_PROT, "protocol",
  "What determines the dose and duration of nicotine replacement therapy?",
  [["Dependence level and stage of treatment", "Correct. The dose and duration of nicotine replacement depend on the patient's level of dependence and point in therapy; the duration is between 6 and 12 weeks."],
   ["Body weight and kidney function", "Renal function guides many drug adjustments, but nicotine replacement is set by the patient's level of dependence and point in therapy.", ADJ],
   ["The age at which smoking began", "The age smoking began is not what sets therapy; nicotine replacement depends on the level of dependence and the point in therapy.", LAY],
   ["The number of past quit attempts", "Past quit attempts are not the stated basis; the dose and duration depend on the level of dependence and the point in therapy.", LAY]], 106),

Q("Nicotine replacement", IO_PROT, "protocol",
  "What is the usual duration of nicotine replacement therapy?",
  [["6 to 12 weeks", "Correct. The duration of nicotine replacement therapy is between 6 and 12 weeks, set by the level of dependence and point in therapy."],
   ["2 to 4 weeks", "Two to four weeks is shorter than the stated course; nicotine replacement runs between 6 and 12 weeks.", REV],
   ["16 to 20 weeks", "Sixteen to twenty weeks is longer than the stated course; nicotine replacement runs between 6 and 12 weeks.", REV],
   ["24 to 52 weeks", "Six months to a year is far longer than the stated course; nicotine replacement runs between 6 and 12 weeks.", REV]], 106),

Q("Nicotine replacement", IO_EDU, "education",
  "Which nicotine replacement forms are available over the counter?",
  [["Patches and gum", "Correct. Nicotine patches and gum are available over the counter; the spray and the inhaler are the other listed nicotine forms."],
   ["Spray and inhaler", "The nicotine spray and inhaler are listed forms, but the ones named as over the counter are the patches and gum.", REV],
   ["Gum and spray", "The gum is over the counter, but the spray is not among the forms named as over the counter; those are the patches and gum.", ADJ],
   ["Patches and inhaler", "The patches are over the counter, but the inhaler is not among the forms named as over the counter; those are the patches and gum.", ADJ]], 106),

Q("Nicotine replacement", IO_CONTRA, "contraindication",
  "Nicotine replacement calls for caution in which patients?",
  [["Those with cardiovascular problems", "Correct. Nicotine replacement calls for caution in patients with cardiovascular problems because of the chance of tachyarrhythmias and hypertension."],
   ["Those with a seizure disorder", "A seizure disorder is the reason to avoid bupropion; nicotine replacement calls for caution in cardiovascular problems.", ADJ],
   ["Those taking a monoamine oxidase inhibitor", "Monoamine oxidase inhibitors are a reason to avoid bupropion; nicotine replacement calls for caution in cardiovascular problems.", ADJ],
   ["Those with a history of depression", "Depression and suicidal ideation are varenicline's boxed neuropsychiatric warning; nicotine replacement calls for caution in cardiovascular problems.", ADJ]], 106),

Q("Varenicline", IO_MOA, "mechanism",
  "Which smoking cessation agent is a partial nicotine receptor agonist?",
  [["Varenicline", "Correct. Varenicline (Chantix) is a partial nicotine receptor agonist, acting to a lesser degree than nicotine."],
   ["Bupropion", "Bupropion is postulated to work by inhibiting norepinephrine and dopamine uptake; the partial nicotine receptor agonist is varenicline.", MECH],
   ["Nicotine polacrilex", "Nicotine polacrilex (gum) supplies nicotine itself to reduce craving and withdrawal; the partial agonist, acting to a lesser degree than nicotine, is varenicline.", MECH],
   ["Nicotine transdermal system", "The nicotine patch supplies nicotine itself to reduce craving and withdrawal; the partial nicotine receptor agonist is varenicline.", MECH]], 107),

Q("Varenicline", IO_EDU, "protocol",
  "When should varenicline be started relative to the quit date?",
  [["One week before the quit date", "Correct. Varenicline is started one week before the quit date and continued for 12 weeks."],
   ["On the quit date itself", "Varenicline is not started on the quit date; it begins one week before it and continues for 12 weeks.", STAGE],
   ["One week after the quit date", "Starting after quitting reverses the timing; varenicline begins one week before the quit date and continues for 12 weeks.", REV],
   ["Once withdrawal symptoms begin", "Varenicline is not started in response to withdrawal; it begins one week before the quit date and continues for 12 weeks.", STAGE]], 107),

Q("Varenicline", IO_AE, "adverse effect",
  "Which side effects are listed for varenicline?",
  [["Nausea, sleep disturbance and headache", "Correct. Varenicline's listed side effects are nausea, sleep disturbance and headache, and it carries a black box warning for neuropsychiatric events."],
   ["Tachyarrhythmias and hypertension", "Tachyarrhythmias and hypertension are the reason for caution with nicotine replacement in cardiovascular problems; varenicline causes nausea, sleep disturbance and headache.", ADJ],
   ["Orange tears, sweat and urine", "Orange-colored secretions are a rifampin effect; varenicline's listed side effects are nausea, sleep disturbance and headache.", ADJ],
   ["Oral thrush and growth delay", "Oral candidiasis and growth suppression in children belong to inhaled corticosteroids; varenicline causes nausea, sleep disturbance and headache.", ADJ]], 107),

Q("Varenicline", IO_TOX, "adverse effect",
  "Which black box warning is listed for varenicline?",
  [["Neuropsychiatric events", "Correct. Varenicline's black box warning is for neuropsychiatric events such as depression and suicidal ideation."],
   ["Lowered seizure threshold", "A seizure disorder is the reason bupropion is avoided; varenicline's black box warning is for neuropsychiatric events.", ADJ],
   ["Cardiac tachyarrhythmias", "Tachyarrhythmias are the cardiovascular caution for nicotine replacement; varenicline's black box warning is for neuropsychiatric events.", ADJ],
   ["Severe liver toxicity", "Hepatitis is a concern with isoniazid and pyrazinamide; varenicline's black box warning is for neuropsychiatric events such as depression and suicidal ideation.", ADJ]], 107),

# ---- immunizations (slide 108) ---------------------------------------------------------------------
Q("Immunizations", IO_IND, "indication",
  "Why is annual influenza vaccination highly recommended for patients with chronic obstructive pulmonary disease?",
  [["They risk serious pneumonia from influenza", "Correct. Patients with chronic obstructive pulmonary disease are at risk for significant morbidity and mortality from pneumonia caused by influenza, so annual vaccination is highly recommended."],
   ["Influenza triggers most asthma attacks", "Viral respiratory infection triggers most asthma attacks, but the reason for the vaccine in chronic obstructive pulmonary disease is the risk of serious influenza pneumonia.", ADJ],
   ["The vaccine slows the fall in lung function", "Smoking cessation is what can return the decline in lung function to the normal rate; the vaccine guards against serious influenza pneumonia.", ADJ],
   ["It replaces the pneumococcal vaccine", "Patients should also receive the pneumococcal vaccine; annual influenza vaccination is given because influenza pneumonia carries significant morbidity and mortality.", REV]], 108),
]
