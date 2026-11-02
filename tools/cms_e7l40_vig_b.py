# -*- coding: utf-8 -*-
"""Lecture 40 vignette pool B -- obstructive sleep apnea diagnosis (home kit versus polysomnogram for the
comorbid patient, split-night, all-night and titration studies, the apnea-hypopnea and respiratory disturbance
indices worked from counts, the diagnostic criteria) and management (s8, s9, s11-s13, s15).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md: the key names the decisive clue and the fact; each
wrong choice says why it fails for THIS patient, the replacing fact, and a "Tell:". Score items show the
arithmetic letter by letter; every wrong total names the item it missed or wrongly counted.

STOP-Bang rules are the questionnaire picture's own (s17): body mass index MORE than 35, age OLDER than 50, neck
16 inches / 40 cm or larger for anyone, gender male; low 0-2, intermediate 3-4, high 5-8, or yes to 2 or more
of the 4 STOP questions + male gender, + body mass index > 35, or + neck 16 inches / 40 cm = high risk.
The sex-specific risk-factor neck sizes (s6, s7) are never used here (scope SLIDE CONFLICTS).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e7l40_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


def ORD(d, asc):
    d["ordered"] = True; d["asc"] = asc; return d


SDB = "Sleep-disordered breathing"
RISK = "Obstructive sleep apnea: risk and presentation"
DX = "Obstructive sleep apnea: diagnosis"
SB = "STOP-Bang screening"
MGT = "Obstructive sleep apnea: management"
UNT = "Untreated obstructive sleep apnea"
CSA = "Central sleep apnea"
OHSD = "Obesity hypoventilation syndrome: diagnosis"
OHSM = "Obesity hypoventilation syndrome: management and prognosis"

SBX = "STOP-Bang (snoring, tiredness, observed apnea, pressure, body mass index, age, neck, gender)"

QUESTIONS = [

# ---------------------------------------------------------------- which sleep study (home kit versus polysomnogram)
V(DX, IO_A,
  "A 66-year-old man with heart failure and chronic obstructive pulmonary disease has loud snoring, witnessed apneas and daytime sleepiness. His insurer suggests a home sleep apnea kit. Which test should be used instead?",
  [["In-laboratory polysomnogram",
    "Correct. At-home kits suit uncomplicated suspected obstructive sleep apnea, but in significant cardiopulmonary disease a polysomnogram is used, not an at-home kit. His heart failure and chronic lung disease are that comorbidity, and heart failure is also a risk factor for central apnea, which a home kit cannot assess."],
   ["Home sleep apnea kit at a later date",
    "Delaying the same study does not remove the problem: at-home kits are set aside in significant cardiopulmonary disease. Tell: his heart failure and lung disease, not the timing, decide that he needs a polysomnogram.", "ruled out by a stated finding"],
   ["Positive airway pressure titration",
    "A positive airway pressure titration study is used when the diagnosis of sleep-disordered breathing is already known, to set the pressure. Tell: he has no diagnosis yet, so the first study has to establish one.", "wrong stage or severity"],
   ["Thyroid-stimulating hormone level",
    "A thyroid-stimulating hormone level is added when hypothyroidism is suspected, and it does not diagnose a sleep disorder. Tell: nothing here suggests thyroid disease; the question is which sleep study his heart and lung disease allow.", "adjacent fact"]],
  CS(8, 24), "initial test", "test"),

V(DX, IO_A,
  "A 54-year-old woman who has taken opioid medications for chronic back pain for years has snoring, frequent awakenings and daytime sleepiness. Which sleep study fits her?",
  [["Polysomnogram in a sleep laboratory",
    "Correct. Long-term opioid use is one of the settings where a polysomnogram, not an at-home kit, is used. Opioid medications are also a risk factor for central sleep apnea, which home kits cannot assess, since they assess obstructive sleep apnea and not other sleep disorders."],
   ["Home sleep apnea kit",
    "Home kits assess obstructive sleep apnea and not other sleep disorders. Tell: her years of opioid use raise the possibility of central apnea and place her on the list of patients who need a polysomnogram instead.", "ruled out by a stated finding"],
   ["Questionnaire score before any study",
    "A questionnaire places a patient in a risk group and cannot diagnose; screening tools have value in symptomatic patients in high-risk settings such as preoperative evaluation. Tell: she already has symptoms, and opioid use decides which study she needs.", "adjacent fact"],
   ["Positive airway pressure titration",
    "A titration study sets the device pressure once the diagnosis is known. Tell: she has no diagnosis yet, and her long-term opioid use points to a diagnostic polysomnogram first.", "wrong stage or severity"]],
  CS(8, 16, 24, 26), "initial test", "test"),

V(DX, IO_A,
  "A 71-year-old man had a stroke last year. His wife reports loud snoring and pauses in his breathing during sleep, and a home sleep apnea kit has been ordered. What is the best next step?",
  [["Change the order to a polysomnogram",
    "Correct. Stroke is one of the conditions in which a polysomnogram is used instead of an at-home kit. Stroke is also a risk factor for central sleep apnea, and at-home testing assesses obstructive sleep apnea and is not sufficient for central apnea, so the order should change."],
   ["Proceed with the home kit as ordered",
    "A home kit can serve uncomplicated suspected obstructive sleep apnea, but stroke is listed among the conditions that call for a polysomnogram. Tell: his stroke, not his snoring, decides the type of study.", "ruled out by a stated finding"],
   ["Start positive airway pressure now",
    "Continuous positive airway pressure is the most effective treatment once obstructive sleep apnea is diagnosed. Tell: he has no diagnosis yet, and his stroke also raises the question of central apnea, so a polysomnogram comes first.", "wrong stage or severity"],
   ["Prescribe modafinil for sleepiness",
    "Stimulants such as modafinil treat sleepiness and need caution in cardiovascular conditions. Tell: no diagnosis has been made, and the decision in front of you is which sleep study to order after a stroke.", "wrong stage or severity"]],
  CS(8, 11, 12, 24, 26), "initial test", "next step"),

V(DX, IO_A,
  "A 59-year-old woman with a neuromuscular disease causing generalized weakness has snoring and morning headaches. Her awake room-air oxygen saturation is 92% (normal 95-100%). Which study should evaluate her for sleep-disordered breathing?",
  [["Attended polysomnogram",
    "Correct. Neuromuscular weakness and awake hypoventilation or hypoxemia are both conditions in which a polysomnogram is used instead of an at-home kit. Her room-air saturation of 92% is below normal, and a polysomnogram can also find sleep disorders other than obstructive sleep apnea."],
   ["Home sleep apnea kit",
    "At-home kits are set aside in neuromuscular weakness and in awake hypoventilation or hypoxemia. Tell: she has both, so a home kit is the wrong study even though her snoring and headaches suggest obstructive sleep apnea.", "ruled out by a stated finding"],
   ["Repeat saturation in a month",
    "Waiting leaves her symptoms and low awake saturation unexplained, while the diagnosis of sleep-disordered breathing rests on a sleep study. Tell: her weakness and hypoxemia call for a polysomnogram now.", "wrong stage or severity"],
   ["Pressure titration study",
    "A positive airway pressure titration is used when the diagnosis is already known, to set the device pressure. Tell: she has no diagnosis yet; her first study must be a diagnostic polysomnogram.", "wrong stage or severity"]],
  CS(8, 31), "initial test", "test"),

V(DX, IO_A,
  "A 43-year-old woman with habitual snoring and daytime sleepiness has a home sleep apnea test that does not show obstructive sleep apnea. Her symptoms persist. What is the best next step?",
  [["Polysomnogram",
    "Correct. At-home kits will not always diagnose mild obstructive sleep apnea; they are most helpful in moderate to severe disease. A negative home study in a woman with ongoing snoring and sleepiness therefore needs a polysomnogram, which can also find other sleep disorders a home kit cannot assess."],
   ["Reassurance",
    "A negative home study does not exclude mild disease, since home kits will not always diagnose it. Tell: her symptoms persist, so the question stays open until a polysomnogram answers it.", "common lay belief"],
   ["Repeat home test",
    "Repeating the same kind of study repeats its limits: home kits assess obstructive sleep apnea alone and can miss mild disease. Tell: the polysomnogram is the study that measures severity across sleep stages and positions.", "adjacent fact"],
   ["Modafinil",
    "Stimulants such as modafinil treat sleepiness but carry headaches, anxiety and many drug interactions. Tell: she has no diagnosis yet, and treating the symptom would skip the study that could find mild disease.", "wrong stage or severity"]],
  CS(8, 11), "initial test", "next step"),

# ---------------------------------------------------------------- split-night, all-night and titration studies
V(DX, IO_A,
  "A 55-year-old man is having a split-night polysomnogram. The first 2 hours of sleep show significant obstructive sleep apnea. What happens during the rest of the night?",
  [["Continuous positive airway pressure titration",
    "Correct. In a split-night polysomnogram the first 2 hours of sleep are recorded to determine severity, and if obstructive sleep apnea is significant, the rest of the night is a continuous positive airway pressure titration that finds the exact pressure needed to keep the airway open."],
   ["Bilevel positive airway pressure titration",
    "Bilevel positive airway pressure is the choice for obesity hypoventilation syndrome with sleep-related hypoventilation. Tell: the split-night protocol titrates continuous positive airway pressure once significant obstructive apnea is seen.", "confused mechanism or drug class"],
   ["Adaptive servo-ventilation titration",
    "Adaptive servo-ventilation is considered for central sleep apnea when continuous positive airway pressure fails. Tell: his first 2 hours show obstructive apnea and nothing has failed yet; the second half titrates continuous pressure.", "adjacent fact"],
   ["Untreated recording until morning",
    "Recording the whole night untreated is the all-night polysomnogram, performed when baseline sleep-disordered breathing is mild to moderate. Tell: his first 2 hours already show significant disease, which switches the night to titration.", "adjacent fact"]],
  CS(8, 26, 33), "initial test", "next step"),

V(DX, IO_A,
  "A 50-year-old woman's baseline sleep recording shows mild to moderate sleep-disordered breathing. Her clinician wants to know how severe it is in different stages of sleep and in different sleep positions. Which study fits?",
  [["All-night polysomnogram",
    "Correct. The all-night polysomnogram is performed when sleep-disordered breathing is mild to moderate during the baseline, and it helps determine severity in different stages of sleep and in different sleep positions, the exact question her clinician is asking."],
   ["Split-night polysomnogram",
    "A split-night study records the first 2 hours to set severity, then switches to continuous positive airway pressure titration when obstructive sleep apnea is significant. Tell: her baseline disease is mild to moderate, which calls for the whole night of recording.", "wrong stage or severity"],
   ["Home sleep apnea kit",
    "At-home kits will not always diagnose mild obstructive sleep apnea and assess no other sleep disorder. Tell: her disease is mild to moderate and the question is severity by stage and position, which a polysomnogram answers.", "ruled out by a stated finding"],
   ["Pressure titration study",
    "A positive airway pressure titration sets the device pressure when the diagnosis is already known. Tell: her clinician wants severity across stages and positions, a diagnostic question for the all-night recording.", "adjacent fact"]],
  C(8), "initial test", "test"),

V(DX, IO_A,
  "A 61-year-old man was diagnosed with obstructive sleep apnea on a sleep study at another center and now needs the pressure on his new device set. Which study is used?",
  [["Pressure titration study",
    "Correct. A positive airway pressure titration is used when the diagnosis of sleep-disordered breathing is already known; it finds the exact air pressure needed to keep his airway open. His diagnosis is established, so a diagnostic study is not repeated first."],
   ["Split-night polysomnogram",
    "A split-night study first records 2 hours of sleep to determine severity, for a patient still being diagnosed. Tell: his diagnosis is already known, so the study he needs is the titration by itself.", "wrong stage or severity"],
   ["Overnight diagnostic polysomnogram",
    "A diagnostic polysomnogram, such as the all-night study used when baseline disease is mild to moderate, measures severity across stages and positions. Tell: he already has a diagnosis; what is missing is the pressure setting.", "wrong stage or severity"],
   ["Home sleep apnea kit",
    "A home kit tests for obstructive sleep apnea and does not set device pressure. Tell: with the diagnosis known, the open task is titrating the pressure, which is the job of a titration study.", "adjacent fact"]],
  C(8), "initial test", "next step"),

# ---------------------------------------------------------------- indices and diagnostic criteria worked from the numbers
V(DX, IO_A,
  "A 46-year-old man has habitual snoring and daytime sleepiness. During 6 hours of sleep his polysomnogram records 48 apneas, 42 hypopneas and 36 respiratory effort-related arousals, predominantly obstructive. What is his apnea-hypopnea index?",
  [["15 events per hour",
    "Correct. The apnea-hypopnea index is (apneas + hypopneas) divided by total sleep time in hours: (48 + 42) / 6 = 90 / 6 = 15 events per hour. Respiratory effort-related arousals belong to the respiratory disturbance index, not to this one. At 15 or more predominantly obstructive events, the diagnosis is confirmed."],
   ["7 events per hour",
    "7 is the hypopneas alone, 42 / 6, leaving out his 48 apneas. Tell: the index adds apneas and hypopneas before dividing by the hours of sleep, so (48 + 42) / 6 = 15 events per hour.", "adjacent fact"],
   ["8 events per hour",
    "8 is the apneas alone, 48 / 6, leaving out his 42 hypopneas. Tell: both event types are counted in the numerator, (48 + 42) / 6 = 15, and only the arousals stay out.", "adjacent fact"],
   ["21 events per hour",
    "21 adds the 36 respiratory effort-related arousals: (48 + 42 + 36) / 6 = 21, which is his respiratory disturbance index. Tell: the apnea-hypopnea index leaves the arousals out and comes to 15.", "confused mechanism or drug class"]],
  C(9), "test finding", "classify"),

V(DX, IO_A,
  "A 52-year-old woman with loud snoring and fatigue has an 8-hour polysomnogram that records 40 apneas, 32 hypopneas and 40 respiratory effort-related arousals. What is her respiratory disturbance index?",
  [["14 events per hour",
    "Correct. The respiratory disturbance index is (apneas + hypopneas + respiratory effort-related arousals) divided by total sleep time in hours: (40 + 32 + 40) / 8 = 112 / 8 = 14 events per hour. The arousals are obstructive airflow reductions that are neither apneas nor hypopneas."],
   ["4 events per hour",
    "4 is the hypopneas alone, 32 / 8. Tell: the respiratory disturbance index counts apneas, hypopneas and respiratory effort-related arousals together, which gives 112 / 8 = 14.", "adjacent fact"],
   ["5 events per hour",
    "5 is a single event type over the night, 40 / 8, either the apneas or the arousals. Tell: this index sums all three event types before dividing by the 8 hours of sleep, giving 14.", "adjacent fact"],
   ["9 events per hour",
    "9 is the apnea-hypopnea index, (40 + 32) / 8, which leaves out the arousals. Tell: the respiratory disturbance index adds the 40 respiratory effort-related arousals, (40 + 32 + 40) / 8 = 14.", "confused mechanism or drug class"]],
  C(9), "test finding", "test"),

V(DX, IO_A,
  "A 41-year-old woman has daytime sleepiness, and her partner reports habitual snoring and pauses in her breathing. Her polysomnogram shows 8 predominantly obstructive respiratory events per hour, and her symptoms are not explained by another condition, a medication or a substance. How should this result be interpreted?",
  [["Diagnostic of obstructive sleep apnea",
    "Correct. The diagnosis is confirmed with 5 or more predominantly obstructive events per hour plus a symptom such as sleepiness, or habitual snoring and breathing interruptions noted by a bed partner, when no other condition, medication or substance explains them. She has 8 events and those symptoms."],
   ["Not diagnostic until 15 events per hour",
    "15 or more predominantly obstructive events per hour confirm the diagnosis without any symptom. Tell: she has symptoms, so the lower threshold of 5 events per hour applies, and her 8 events meet it.", "wrong stage or severity"],
   ["Diagnostic of central sleep apnea",
    "Central sleep apnea shows repetitive apneas in the absence of thoracic-abdominal excursion, airflow stopping because effort stops. Tell: her events are predominantly obstructive, the defining feature of obstructive sleep apnea.", "competing diagnosis"],
   ["Indeterminate until a home kit is done",
    "A home kit will not always diagnose mild disease and adds nothing after a polysomnogram has answered the question. Tell: her result already meets the criterion of 5 or more events per hour with symptoms.", "adjacent fact"]],
  CS(9, 8, 26), "test finding", "classify"),

V(DX, IO_A,
  "A 50-year-old man has a polysomnogram as part of a research study. He has no sleepiness, fatigue or insomnia, and no one has noted snoring or pauses in his breathing. The study shows 7 predominantly obstructive events per hour. How should this result be interpreted?",
  [["Criteria for diagnosis are not met",
    "Correct. Without symptoms, the diagnosis needs 15 or more predominantly obstructive events per hour; 5 or more counts only with a symptom such as sleepiness, fatigue, insomnia, choking or snoring noted by an observer. He has 7 events and no symptoms, so neither criterion is met."],
   ["Diagnostic of obstructive sleep apnea",
    "7 events per hour would confirm obstructive sleep apnea only alongside a qualifying symptom. Tell: he has no sleepiness, fatigue, insomnia or observer-noted snoring, so the symptom-free threshold of 15 events per hour applies.", "wrong stage or severity"],
   ["Diagnostic of central sleep apnea",
    "Central apnea shows repetitive apneas in the absence of thoracic-abdominal excursion. Tell: his events are predominantly obstructive, and they fall below the diagnostic threshold for a symptom-free patient anyway.", "competing diagnosis"],
   ["Needs positive airway pressure therapy",
    "Continuous positive airway pressure is the most effective treatment once obstructive sleep apnea is diagnosed. Tell: his result meets neither diagnostic criterion, so there is no diagnosis to treat.", "wrong stage or severity"]],
  CS(9, 12, 26), "test finding", "classify"),
# ---------------------------------------------------------------- management: devices, drugs, surgery, referral
V(MGT, IO_A,
  "A 47-year-old man has obstructive sleep apnea newly confirmed on polysomnogram, with daytime sleepiness and hypertension. Which treatment is the most effective option for him?",
  [["Continuous positive airway pressure",
    "Correct. Continuous positive airway pressure is the most effective non-pharmacologic treatment for obstructive sleep apnea. It also improves consequences of untreated disease, such as reflux, raised proinflammatory cytokines and, in the elderly, drowsiness and nocturia."],
   ["Nasal expiratory resistance device",
    "A nasal expiratory resistance device uses the patient's own breathing to produce expiratory positive airway pressure, an alternative device. Tell: the option named most effective is continuous positive airway pressure.", "adjacent fact"],
   ["Modafinil for daytime sleepiness",
    "Stimulants such as modafinil target sleepiness, carry headaches, anxiety and many drug interactions, and need caution in cardiovascular conditions. Tell: a stimulant treats a symptom, while continuous positive airway pressure treats the obstruction and is the most effective option.", "confused mechanism or drug class"],
   ["Oral appliance worn during sleep",
    "An oral appliance is one of the non-pharmacologic options, but it is not effective in severe obstructive sleep apnea or in patients without teeth. Tell: the treatment named most effective is continuous positive airway pressure.", "adjacent fact"]],
  CS(12, 11, 8, 19, 22), "first-line", "treatment"),

V(MGT, IO_A,
  "A 63-year-old woman with newly diagnosed obstructive sleep apnea also has heart failure and chronic obstructive pulmonary disease. She asks for the adjustable device a friend uses. Which device should she not be given?",
  [["Autotitrating positive airway pressure",
    "Correct. Autotitrating (adjustable) positive airway pressure is used in patients without significant comorbid conditions. Her heart failure and chronic obstructive pulmonary disease are significant comorbidities, so she should get continuous positive airway pressure, the most effective option, instead."],
   ["Continuous positive airway pressure",
    "Continuous positive airway pressure is the most effective treatment, and no comorbidity limit is attached to it. Tell: it is the device she should receive; the comorbidity limit belongs to the autotitrating device.", "reversed direction or value"],
   ["Nasal expiratory resistance device",
    "A nasal expiratory resistance device uses the patient's own breathing to produce expiratory positive airway pressure, and no comorbidity limit is attached to it. Tell: the device kept for patients without significant comorbidities is the autotitrating one.", "adjacent fact"],
   ["Oral appliance worn during sleep",
    "An oral appliance is not effective in severe obstructive sleep apnea or in patients with no teeth; nothing in her history states either limit, and no comorbidity limit is attached to it. Tell: her heart failure and lung disease restrict the autotitrating device, not the appliance.", "adjacent fact"]],
  C(12), "avoid", "avoid"),

V(MGT, IO_POP,
  "A 76-year-old man with moderate obstructive sleep apnea has no teeth and wears full dentures. He cannot tolerate his continuous positive airway pressure mask and asks about a mouthpiece instead. Which option should be avoided?",
  [["Oral appliance",
    "Correct. An oral appliance is not effective in patients who have no teeth (or in severe obstructive sleep apnea). He is edentulous, so the mouthpiece he asks about is the option to avoid, even though he cannot tolerate his mask."],
   ["Radiofrequency ablation",
    "Radiofrequency ablation is used in mild to moderate obstructive sleep apnea when continuous positive airway pressure cannot be tolerated, which describes him. Tell: his lack of teeth limits the oral appliance, not this procedure.", "adjacent fact"],
   ["Nasal expiratory resistance device",
    "A nasal expiratory resistance device uses his own breathing to produce expiratory positive airway pressure and does not depend on teeth. Tell: the option tied to having teeth is the oral appliance.", "adjacent fact"],
   ["Positional therapy",
    "Positional therapy with a sleep belt or sleep shirt keeps the patient on his side and fits events that occur when supine. Tell: missing teeth do not limit it; the oral appliance is the option that needs them.", "adjacent fact"]],
  CS(12, 13), "avoid", "avoid"),

V(MGT, IO_A,
  "A 52-year-old woman has severe obstructive sleep apnea on polysomnogram. She finds her mask uncomfortable and asks whether an oral appliance would work as well. What should she be told?",
  [["It is not effective in severe disease",
    "Correct. An oral appliance is not effective in severe obstructive sleep apnea or in patients without teeth. Her disease is severe, so the appliance is not a substitute; continuous positive airway pressure remains the most effective treatment for her."],
   ["It is the most effective option",
    "Continuous positive airway pressure is the option named most effective, not the oral appliance. Tell: for her severe disease the appliance is not effective at all, so it cannot match the mask.", "reversed direction or value"],
   ["It works if she sleeps on her back",
    "Sleeping supine is the position positional therapy avoids, keeping the patient on her side when events occur supine. Tell: no sleeping position makes an appliance effective in severe disease.", "reversed direction or value"],
   ["It equals the mask if worn nightly",
    "Nightly use does not change the limit: the appliance is not effective in severe obstructive sleep apnea. Tell: her severity, not how often she would wear it, rules the appliance out.", "common lay belief"]],
  C(12), "education", "education"),

V(MGT, IO_A,
  "A 44-year-old man with obstructive sleep apnea has respiratory events on polysomnogram that occur when he sleeps on his back and not when he lies on his side. He wants a measure to add to his care. Which therapy targets this pattern?",
  [["Positional therapy",
    "Correct. Positional therapy fits when events occur in the supine position: a sleep belt or sleep shirt keeps him lying on his side. His events are confined to back-sleeping, the exact pattern it addresses."],
   ["Nasal steroid spray",
    "Nasal steroids treat nasal congestion and inflammation from allergic rhinitis in patients with obstructive sleep apnea. Tell: he has no nasal symptoms; his events depend on his body position.", "adjacent fact"],
   ["Palatal implants",
    "Palatal implants are for mild obstructive sleep apnea when continuous positive airway pressure cannot be tolerated. Tell: nothing says he cannot tolerate pressure therapy, and his events are tied to position.", "wrong stage or severity"],
   ["Tracheostomy",
    "Tracheostomy is a cure because it bypasses the site of upper airway obstruction, but it is a surgical airway. Tell: his events depend on body position, which a sleep belt or shirt addresses without surgery.", "wrong stage or severity"]],
  CS(12, 13), "agent/regimen", "treatment"),

V(MGT, IO_A,
  "A 34-year-old woman with obstructive sleep apnea has seasonal allergic rhinitis, and the nasal congestion makes her positive airway pressure mask hard to use. Which treatment addresses her congestion?",
  [["A nasal steroid spray",
    "Correct. Nasal steroids are used in patients with obstructive sleep apnea for nasal congestion and inflammation from allergic rhinitis. Treating her congestion targets the problem that is getting in the way of her positive airway pressure therapy."],
   ["Modafinil each morning",
    "Modafinil is a stimulant for sleepiness, with headaches, nervousness, dizziness, nausea and many drug interactions. Tell: her problem is congestion from allergic rhinitis, which is what nasal steroids are used for.", "confused mechanism or drug class"],
   ["A sedative at bedtime",
    "Sedatives are a risk factor for obstructive sleep apnea, and the advice is to avoid them. Tell: a sedative would work against her sleep apnea and leave the congestion untreated.", "reversed direction or value"],
   ["Positional sleep shirt",
    "Positional therapy keeps the patient on her side when events occur while supine. Tell: her complaint is nasal congestion from allergic rhinitis, which positioning does not address; a nasal steroid does.", "adjacent fact"]],
  CS(11, 12, 6, 15), "agent/regimen", "treatment"),

V(MGT, IO_A,
  "A 62-year-old man with obstructive sleep apnea uses continuous positive airway pressure nightly but still has daytime sleepiness. He also has coronary artery disease, cirrhosis and generalized anxiety disorder. Which treatment calls for caution because of his other conditions?",
  [["Modafinil",
    "Correct. Stimulants such as modafinil or armodafinil are used with caution in patients with cardiovascular, hepatic or psychiatric conditions, and he has all three: coronary artery disease, cirrhosis and an anxiety disorder. Nervousness and anxiety are also listed side effects."],
   ["A nasal steroid spray",
    "Nasal steroids are used for nasal congestion and inflammation from allergic rhinitis, with no caution tied to heart, liver or psychiatric disease. Tell: the caution for those conditions is attached to the stimulants.", "adjacent fact"],
   ["Positional therapy",
    "Positional therapy with a sleep belt or shirt has no comorbidity caution attached and fits events that occur when supine. Tell: his heart, liver and psychiatric conditions are named cautions for the stimulants, not for positioning.", "adjacent fact"],
   ["Diet and exercise for weight loss",
    "Diet and exercise for weight loss is a risk modification for obstructive sleep apnea with no listed caution. Tell: his comorbidities raise concern for a stimulant drug, not for a lifestyle change.", "adjacent fact"]],
  CS(11, 12, 15), "avoid", "avoid"),

V(MGT, IO_POP,
  "A 78-year-old woman with obstructive sleep apnea has residual daytime sleepiness despite continuous positive airway pressure, and armodafinil is being considered. She has no heart, liver or psychiatric disease. Which approach to its dose fits her?",
  [["A lower dose than in younger adults",
    "Correct. Stimulants such as modafinil and armodafinil are given at lower doses in the elderly population. At 78, with no cardiovascular, hepatic or psychiatric condition to add caution, she can be considered for the drug at a reduced dose."],
   ["A higher dose than in younger adults",
    "Age moves the dose down, not up: lower doses are used in the elderly. Tell: a higher dose would add to listed side effects such as headache, nervousness, dizziness and nausea.", "reversed direction or value"],
   ["The same dose as in younger adults",
    "The elderly are singled out for lower doses, so the standard adult dose is not the plan for a 78-year-old. Tell: her age alone is enough to lower the stimulant dose.", "adjacent fact"],
   ["Avoiding the drug because of age",
    "Older age calls for a lower dose, not for avoiding the drug. Tell: the conditions that call for caution are cardiovascular, hepatic and psychiatric disease, and she has none of them.", "wrong stage or severity"]],
  C(11), "agent/regimen", "treatment"),

V(MGT, IO_A,
  "A 50-year-old man started modafinil for residual daytime sleepiness from obstructive sleep apnea. Two weeks later he develops a widespread rash and feels unwell. Which adverse effect of the drug best fits?",
  [["Drug hypersensitivity reaction",
    "Correct. Listed side effects of modafinil and armodafinil include headaches, nervousness or anxiety, dizziness, nausea, and dermatologic and systemic hypersensitivities. A widespread rash with feeling unwell after starting the drug fits a dermatologic and systemic hypersensitivity reaction."],
   ["Stimulant nervousness and anxiety",
    "Nervousness and anxiety are listed side effects, but they are feelings, not a skin eruption. Tell: a widespread rash with systemic illness matches the dermatologic and systemic hypersensitivities listed for the stimulants.", "adjacent fact"],
   ["Worsening of his sleep apnea",
    "Worsening sleep apnea would bring more sleepiness, snoring or witnessed apneas, the features of the disease. Tell: a new rash after a new drug points to the drug's listed dermatologic and systemic hypersensitivities.", "competing diagnosis"],
   ["Stimulant-induced headache",
    "Headache is a listed side effect of modafinil, but it does not produce a rash. Tell: skin involvement with feeling unwell is the hypersensitivity pattern, a separate listed side effect.", "adjacent fact"]],
  C(11), "complication", "complication"),

V(MGT, IO_A,
  "A 46-year-old man with moderate obstructive sleep apnea cannot tolerate continuous positive airway pressure despite several mask changes. Which option is described for his severity and his intolerance of the device?",
  [["Radiofrequency ablation",
    "Correct. Radiofrequency ablation is used in patients with mild to moderate obstructive sleep apnea who cannot tolerate continuous positive airway pressure. His disease is moderate and he cannot tolerate the device, which matches both conditions."],
   ["Palatal implants",
    "Palatal implants are used in mild obstructive sleep apnea when continuous positive airway pressure cannot be tolerated. Tell: his disease is moderate, beyond the mild range the implants cover; radiofrequency ablation reaches mild to moderate.", "wrong stage or severity"],
   ["Adaptive servo-ventilation",
    "Adaptive servo-ventilation is considered for central sleep apnea after continuous positive airway pressure fails, and it is itself a positive airway pressure therapy. Tell: his disease is obstructive, and his problem is tolerating pressure therapy.", "competing diagnosis"],
   ["Modafinil",
    "Modafinil is a stimulant for sleepiness, with headaches, anxiety and many drug interactions. Tell: no severity or device-intolerance indication is attached to it; radiofrequency ablation carries exactly his two.", "confused mechanism or drug class"]],
  CS(11, 13, 26), "escalation", "treatment"),

V(MGT, IO_A,
  "A 58-year-old man with obstructive sleep apnea has not been helped by continuous positive airway pressure or an oral appliance. He asks which operation would be a cure. Which procedure is described as a cure for obstructive sleep apnea?",
  [["Tracheostomy",
    "Correct. Tracheostomy is a cure for obstructive sleep apnea because the site of upper airway obstruction is bypassed. Breathing no longer depends on the narrowed upper airway that collapses during sleep."],
   ["Bariatric surgery",
    "Bariatric surgery for weight loss may be helpful in obstructive sleep apnea, a weaker claim than a cure. Tell: the procedure called a cure is the one that bypasses the site of obstruction, tracheostomy.", "adjacent fact"],
   ["Palatal implants",
    "Palatal implants are an option in mild obstructive sleep apnea for patients who cannot tolerate continuous positive airway pressure. Tell: they treat mild disease; the cure comes from bypassing the upper airway obstruction.", "wrong stage or severity"],
   ["Radiofrequency ablation",
    "Radiofrequency ablation is used in mild to moderate disease when continuous positive airway pressure cannot be tolerated. Tell: it is a treatment option; tracheostomy, which bypasses the obstruction, is the one called a cure.", "adjacent fact"]],
  C(13), "escalation", "treatment"),

V(MGT, IO_A,
  "A 53-year-old man has loud snoring, witnessed apneas and daytime sleepiness, and his primary care clinician suspects obstructive sleep apnea. Which referral is part of his care?",
  [["Sleep physician",
    "Correct. Patient education for obstructive sleep apnea includes referral to a sleep physician, together with proper counseling. His snoring, witnessed apneas and sleepiness make the diagnosis likely, and confirming it takes a sleep study."],
   ["Bariatric surgeon",
    "Bariatric surgery for weight loss may be helpful, but it is a surgical option rather than the referral named for a suspected diagnosis. Tell: the named referral is to a sleep physician, with proper counseling.", "wrong stage or severity"],
   ["Maxillofacial surgeon",
    "Maxillomandibular advancement is one of many surgical options for established disease. Tell: he has no diagnosis yet, and the referral named in patient education is to a sleep physician.", "wrong stage or severity"],
   ["Cardiologist",
    "Untreated obstructive sleep apnea raises cardiovascular risks such as hypertension, arrhythmias and sudden cardiac death at night, but the referral named for the sleep disorder is a sleep physician. Tell: he is being evaluated for the apnea itself.", "adjacent fact"]],
  CS(15, 13, 18), "referral", "referral"),

]
