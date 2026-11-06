# -*- coding: utf-8 -*-
"""Lecture 44 vignette pool B -- spontaneous pneumothorax treatment and education (s51-60), traumatic and tension
pneumothorax (s61-68), hemothorax (s69-74) and pneumomediastinum (s75-79).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md. Stability items show each American College of
Chest Physicians criterion against the stem's vital signs (s51: respiratory rate under 24, heart rate over 60 and
under 120, normal blood pressure, room-air saturation over 90%, whole sentences); no vital sign sits on a cutoff.

Held for the scope (cms_e7l44_scope.py):
  size     every stem gives an apex-to-cupola distance well clear of 3 cm (2 cm or 4-5 cm), never 3 cm.
  large    the large symptomatic first primary pneumothorax item keys chest tube (s55) and offers NO catheter or
           needle aspiration, small-bore catheter or Heimlich valve option (s58 conflict).
  tension  next-step stems say whether a chest tube kit is at hand (s66 vs s58): no kit -> needle decompression;
           after the needle -> chest tube; kit at bedside -> the item asks what to AVOID (the X-ray). The needle
           site item uses a patient of average build and never offers the 4th/5th intercostal space.
  timing   no observation or air-leak timing is keyed (s53 vs s58, s58 vs s60); air travel is keyed as "delay
           and confirm with a film", with the 7-14 days only in the explanation (s60, no conflict).
  recurrence  "approaches 50% within three years" (s59) is keyed with its own window only.
  hemothorax  the hematocrit rule is read off the s74 picture (pleural over 50% of blood = hemothorax); the
           straight line with no meniscus (s71) is never keyed for hemothorax; tube sizes never appear.
  pneumomediastinum  Hamman crunch carries its s77 description (synchronous with the heartbeat) in the stem.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e7l44_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


def ORD(d, asc):
    d["ordered"] = True; d["asc"] = asc; return d


STB = "Stable"
U_RR = "Unstable: respiratory rate"
U_HR = "Unstable: heart rate"
U_SAT = "Unstable: oxygen saturation"

QUESTIONS = [

# ---------------------------------------------------------------- stability (American College of Chest Physicians)
V(T_SPTX, IO_A,
  "A 24-year-old man has a primary spontaneous pneumothorax. His respiratory rate is 28 breaths per minute, heart rate 104 beats per minute, blood pressure 124/78 mm Hg and oxygen saturation 95% on room air, and he speaks in whole sentences. How is he classified by the American College of Chest Physicians stability definition?",
  [[U_RR,
    "Correct. Stability requires all of: respiratory rate under 24 breaths per minute, heart rate over 60 and under 120, normal blood pressure, room-air saturation over 90% and whole sentences. His heart rate of 104, normal pressure, saturation of 95% and full sentences pass, but a rate of 28 fails, and every other patient is unstable."],
   [STB,
    "Stability needs every criterion met, and one failure makes the patient unstable. Tell: his respiratory rate of 28 breaths per minute is above the cutoff of under 24, so he cannot be called stable despite his other normal values.", "wrong stage or severity"],
   [U_HR,
    "The heart-rate criterion is over 60 and under 120 beats per minute. Tell: his heart rate of 104 sits inside that range; the failed criterion is his respiratory rate of 28.", "ruled out by a stated finding"],
   [U_SAT,
    "The saturation criterion is a room-air oxygen saturation over 90%. Tell: his 95% on room air passes; it is his respiratory rate of 28, against a cutoff of under 24, that makes him unstable.", "ruled out by a stated finding"]],
  C(51), "manifestation", "classify"),

V(T_SPTX, IO_A,
  "A 26-year-old woman has a small primary spontaneous pneumothorax. Her respiratory rate is 20 breaths per minute, heart rate 96 beats per minute, blood pressure 118/74 mm Hg and oxygen saturation 96% on room air, and she speaks in whole sentences. How is she classified by the American College of Chest Physicians stability definition?",
  [[STB,
    "Correct. Every criterion is met: respiratory rate 20, under 24; heart rate 96, between 60 and 120; normal blood pressure; room-air saturation 96%, over 90%; and whole sentences. Stability requires all of these, and she has all of them."],
   [U_RR,
    "The respiratory-rate criterion is under 24 breaths per minute. Tell: her rate of 20 meets it, and her heart rate, pressure, saturation and speech pass too, so nothing makes her unstable.", "ruled out by a stated finding"],
   [U_HR,
    "The heart-rate criterion is over 60 and under 120 beats per minute. Tell: her heart rate of 96 sits inside that range, so tachycardia has not crossed the cutoff of 120, and her other values pass as well.", "ruled out by a stated finding"],
   [U_SAT,
    "The saturation criterion is a room-air oxygen saturation over 90%. Tell: her 96% on room air clears it, and her respiratory rate, heart rate, pressure and whole sentences meet the other criteria.", "ruled out by a stated finding"]],
  C(51), "test finding", "classify"),

V(T_SPTX, IO_A,
  "A 30-year-old man has a primary spontaneous pneumothorax. His respiratory rate is 18 breaths per minute, heart rate 54 beats per minute, blood pressure 116/72 mm Hg and oxygen saturation 97% on room air, and he speaks in whole sentences. How is he classified by the American College of Chest Physicians stability definition?",
  [[U_HR,
    "Correct. The heart-rate criterion has two bounds: over 60 and under 120 beats per minute. His rate of 54 is below 60, so he fails it even though his respiratory rate of 18, normal pressure, saturation of 97% and full sentences pass; anyone who misses a criterion is unstable."],
   [STB,
    "Stability needs every criterion, including a heart rate over 60. Tell: his rate of 54 falls below that lower bound, so he cannot be classed as stable despite his other values.", "wrong stage or severity"],
   [U_RR,
    "The respiratory-rate criterion is under 24 breaths per minute. Tell: his rate of 18 meets it easily; his failed criterion is the heart rate of 54, under the lower bound of 60 beats per minute.", "ruled out by a stated finding"],
   [U_SAT,
    "The saturation criterion is a room-air oxygen saturation over 90%. Tell: his 97% on room air passes; the slow heart rate of 54 is what fails the definition.", "ruled out by a stated finding"]],
  C(51), "differential", "classify"),

# ---------------------------------------------------------------- primary spontaneous pneumothorax treatment
V(T_SPTX, IO_A,
  "A 23-year-old man has a first primary spontaneous pneumothorax with an apex-to-cupola distance of 2 cm on his upright chest radiograph. He has mild pleuritic pain, no significant dyspnea and stable vital signs. Which is the most appropriate management?",
  [["Observation with 100% oxygen",
    "Correct. A small primary spontaneous pneumothorax, under 3 cm at the apex, with minimal symptoms is observed with adequate analgesia and oxygen at 100% by non-rebreather mask, which accelerates resorption of air. A repeat film confirms it has not expanded, and he is discharged if it is stable and he is asymptomatic."],
   ["Chest tube insertion",
    "A chest tube treats a moderate or large primary pneumothorax, over 3 cm at the apex, with moderate or severe symptoms, or a failed observation or aspiration. Tell: his is 2 cm with mild pain and no failed treatment.", "wrong stage or severity"],
   ["Catheter aspiration",
    "Catheter aspiration treats a small primary pneumothorax when significant dyspnea persists after analgesia. Tell: he has mild pain without significant dyspnea, so observation fits first.", "wrong stage or severity"],
   ["Thoracoscopic pleurodesis",
    "Video-assisted thoracoscopic surgery with pleurodesis is the treatment for a recurrent primary pneumothorax and the best preventive procedure. Tell: this is his first episode, small and minimally symptomatic.", "wrong stage or severity"]],
  CS(53, 54, 55), "first-line", "next step"),

V(T_SPTX, IO_A,
  "A 28-year-old man has a first primary spontaneous pneumothorax with an apex-to-cupola distance of 5 cm on his upright chest radiograph. He has significant chest pain and dyspnea. Which is the most appropriate treatment?",
  [["Chest tube insertion",
    "Correct. A moderate or large primary spontaneous pneumothorax, more than 3 cm at the apex, with moderate or severe symptoms such as significant chest pain and dyspnea is treated with chest tube insertion. His 5 cm apex-to-cupola distance is large by the 3 cm rule, and his symptoms are significant."],
   ["Observation with 100% oxygen",
    "Observation with analgesia and 100% oxygen is for a small primary pneumothorax, under 3 cm, with minimal symptoms. Tell: his is 5 cm with significant pain and dyspnea.", "wrong stage or severity"],
   ["Thoracoscopic pleurodesis",
    "Video-assisted thoracoscopic surgery with pleurodesis is for a recurrent primary pneumothorax. Tell: this is his first episode, and a large symptomatic first episode is drained with a chest tube.", "wrong stage or severity"],
   ["Discharge, repeat film",
    "Discharge with a follow-up film comes after a small pneumothorax has been observed and stayed stable in an asymptomatic patient. Tell: he is large and symptomatic, so he needs evacuation of the space now.", "wrong stage or severity"]],
  CS(28, 53, 55), "first-line", "treatment"),

V(T_SPTX, IO_A,
  "A 25-year-old man presents with his second primary spontaneous pneumothorax on the right; the first was treated 18 months ago. He is stable. Which management best prevents further recurrence?",
  [["Thoracoscopic surgery with pleurodesis",
    "Correct. A recurrent primary spontaneous pneumothorax calls for surgical therapy, video-assisted thoracoscopic surgery with pleurodesis, which is the best preventive procedure. Recurrence is common, approaching 50% within three years after a first episode, and his second episode proves the risk."],
   ["Catheter aspiration, then discharge",
    "Recurrent pneumothorax is on the list of contraindications to catheter aspiration. Tell: his is a second episode, and aspiration does nothing to prevent a third.", "ruled out by a stated finding"],
   ["Observation with 100% oxygen",
    "Observation with oxygen fits a small first primary pneumothorax with minimal symptoms. Tell: a recurrence calls for definitive prevention, which observation does not provide.", "wrong stage or severity"],
   ["Chest tube, then discharge",
    "A chest tube evacuates the space in a large symptomatic episode but leaves the pleural space open to recur. Tell: for a recurrent primary pneumothorax the plan is surgery with pleurodesis.", "wrong stage or severity"]],
  CS(39, 53, 55, 59), "escalation", "treatment"),

V(T_SPTX, IO_A,
  "A 22-year-old man with a first primary spontaneous pneumothorax and an apex-to-cupola distance of 2 cm is being observed with oxygen and analgesia. His repeat chest radiograph shows that the pneumothorax has enlarged, his respiratory rate is 32 breaths per minute and his oxygen saturation is 88% on room air. Which is the most appropriate next step?",
  [["Chest tube insertion",
    "Correct. A chest tube is indicated for failure of observation: an enlarging pneumothorax, persistent tachypnea over 30 breaths per minute, or saturation under 90% on room air. He has all three, so observation has failed."],
   ["Continue observation",
    "Observation suits a small pneumothorax that stays the same on repeat film in a patient with minimal symptoms. Tell: his has enlarged, with a rate over 30 and saturation under 90%, the definition of failed observation.", "wrong stage or severity"],
   ["Discharge, repeat film",
    "Discharge requires a stable pneumothorax on the repeat film and an asymptomatic patient. Tell: his repeat film shows enlargement and he is tachypneic and hypoxemic.", "ruled out by a stated finding"],
   ["Thoracoscopic pleurodesis",
    "Thoracoscopic surgery with pleurodesis is for a recurrent primary pneumothorax or a failed chest tube. Tell: this is his first episode and no tube has been tried; failed observation calls for the tube first.", "wrong stage or severity"]],
  CS(49, 53, 54, 55), "escalation", "next step"),

# ---------------------------------------------------------------- secondary spontaneous pneumothorax
V(T_SPTX, IO_POP,
  "A 69-year-old woman with chronic obstructive pulmonary disease has a small left pneumothorax found on a chest radiograph, with an apex-to-cupola distance of 2 cm. She has no new symptoms and her vital signs are stable. Which is the most appropriate next step?",
  [["Admit for observation",
    "Correct. Her chronic obstructive pulmonary disease makes this a secondary spontaneous pneumothorax. A small, asymptomatic one is observed, with hospitalization for monitoring and supportive care, because secondary pneumothorax is more life-threatening from lack of pulmonary reserve."],
   ["Discharge after a stable film",
    "Discharge after a stable repeat film belongs to a small primary pneumothorax in an asymptomatic patient. Tell: hers is secondary, and a small secondary pneumothorax is managed with hospitalization.", "competing diagnosis"],
   ["Catheter aspiration",
    "Underlying pulmonary disease is a contraindication to catheter aspiration. Tell: her chronic obstructive pulmonary disease rules it out, and she has no symptoms that need evacuation yet.", "ruled out by a stated finding"],
   ["Chest tube insertion",
    "In a small secondary pneumothorax, a chest tube is inserted for symptoms or a persistent air leak. Tell: she has no new symptoms, so observation in the hospital comes first.", "wrong stage or severity"]],
  CS(39, 53, 56, 57), "first-line", "next step"),

V(T_SPTX, IO_POP,
  "A 71-year-old man with severe chronic obstructive pulmonary disease uses noninvasive positive-pressure ventilation at home every night. He is admitted with a secondary spontaneous pneumothorax, and air is still bubbling through his chest tube, showing an active air leak. Which of his therapies should be held for now?",
  [["Noninvasive ventilation",
    "Correct. Positive-pressure therapies are held during an active air leak. His nightly noninvasive ventilation is positive pressure, and air still bubbling through his tube shows the leak is active, so it is paused until the leak has closed."],
   ["Supplemental oxygen",
    "Oxygen accelerates resorption of pleural air and is part of observing a small pneumothorax. Tell: oxygen is not a positive-pressure therapy; the device to hold is the one that pushes air under pressure.", "adjacent fact"],
   ["Analgesic medication",
    "Adequate analgesia is part of pneumothorax care. Tell: pain control does nothing to an air leak; the therapy to hold during an active leak is positive pressure.", "adjacent fact"],
   ["Chest tube drainage",
    "Most secondary spontaneous pneumothoraces are treated with chest tube insertion. Tell: the tube is draining his leak and stays; the positive pressure from his home ventilator is what pauses.", "reversed direction or value"]],
  CS(53, 57, 60), "avoid", "avoid"),

# ---------------------------------------------------------------- education and referral
V(T_SPTX, IO_A,
  "A 20-year-old man is being discharged after his first spontaneous pneumothorax. He asks how likely it is to happen again, and the clinician counsels him about the risk over the next three years. Which recurrence estimate is accurate?",
  [["About 50%",
    "Correct. Recurrence approaches 50% within three years after an initial spontaneous pneumothorax. That is why education explains the condition, names video-assisted thoracoscopic surgery with pleurodesis as the best preventive procedure, and discusses smoking cessation."],
   ["About 5%",
    "A 5% figure treats recurrence as rare, which would make prevention hardly worth discussing. Tell: recurrence is common after a first spontaneous pneumothorax, approaching 50% within three years.", "reversed direction or value"],
   ["About 15%",
    "A figure near 15% understates the risk by a wide margin and would undercut the case for prevention. Tell: within three years of a first spontaneous pneumothorax, recurrence approaches half of patients.", "reversed direction or value"],
   ["About 90%",
    "Recurrence is common but not near-certain after a first episode. Tell: the risk approaches 50% within three years; figures above 60% describe the risk after a second episode.", "reversed direction or value"]],
  CS(59, 60), "prognosis", "education"),

V(T_SPTX, IO_A,
  "A 27-year-old woman is being discharged after her primary spontaneous pneumothorax has resolved. She has a flight booked for a conference and asks for advice about air travel. Which advice is accurate?",
  [["Delay flying; confirm with a film",
    "Correct. Air travel is delayed for 7-14 days after resolution, and resolution is confirmed with a chest X-ray before she flies. Follow-up films verify complete lung re-expansion, and she is also counseled on recurrence and, if she smokes, on stopping."],
   ["Fly once the chest pain is gone",
    "Pain relief does not show that the lung has fully re-expanded. Tell: the advice is a delay after resolution, with resolution confirmed on a chest X-ray, not judged by symptoms.", "common lay belief"],
   ["Fly if her oxygen level is normal",
    "A normal oxygen saturation does not confirm that the pneumothorax has resolved. Tell: the check before flying is a chest X-ray showing re-expansion, after a waiting period.", "common lay belief"],
   ["Avoid air travel permanently",
    "Air travel is delayed, not forbidden for life. Tell: the guide is to wait after resolution and confirm it with a film; avoiding scuba diving is the lasting restriction.", "adjacent fact"]],
  CS(59, 60), "education", "education"),

V(T_SPTX, IO_A,
  "A 29-year-old commercial airline pilot has recovered from his first primary spontaneous pneumothorax, and a follow-up film confirms that the lung has re-expanded. He does not smoke and has no family history of pneumothorax. Which referral is recommended?",
  [["Early surgical evaluation",
    "Correct. Pilots and divers need early surgical options for safety, and video-assisted thoracoscopic surgery closes leaks to prevent future collapses. Recurrence approaches 50% within three years, a risk his occupation cannot carry."],
   ["Genetics referral",
    "Genetics referral is recommended when the family history reveals spontaneous pneumothorax. Tell: he has no such family history; his occupation is what drives the referral.", "ruled out by a stated finding"],
   ["Smoking cessation program",
    "Smoking cessation is part of education after a spontaneous pneumothorax, because smoking raises recurrence risk. Tell: he does not smoke, so the program would not address his risk.", "ruled out by a stated finding"],
   ["No referral; resume flying",
    "Returning to the cockpit without a plan ignores a recurrence risk that approaches 50% within three years. Tell: pilots and divers are singled out for early surgical evaluation.", "common lay belief"]],
  CS(59, 60), "referral", "referral"),

# ---------------------------------------------------------------- traumatic and tension pneumothorax
V(T_TENSION, IO_A,
  "A 34-year-old man is brought in after a high-speed motor vehicle crash. He is in severe respiratory distress, with blood pressure 78/50 mm Hg and heart rate 136 beats per minute. His trachea is deviated to the left, his neck veins are distended, his right chest is hyperresonant and breath sounds are absent on the right. What is the most likely diagnosis?",
  [["Tension pneumothorax",
    "Correct. Air enters the pleural space but cannot escape, a one-way valve, causing severe ventilatory compromise and a mediastinal shift to the contralateral side. Decreased venous return and cardiac output follow, with hypotension, tracheal deviation, neck vein distention and absent breath sounds, his exact picture."],
   ["Hemothorax",
    "Hemothorax is blood in the pleural space, most often from trauma, and fluid is dull to percussion. Tell: his right chest is hyperresonant, the note of air, and his trachea is pushed away from it under pressure.", "ruled out by a stated finding"],
   ["Pneumomediastinum",
    "Pneumomediastinum is air in the mediastinal tissues, found as subcutaneous emphysema in the neck and a crunch with each heartbeat. Tell: his findings are a hyperresonant, silent hemithorax with shock and tracheal shift.", "competing diagnosis"],
   ["Open pneumothorax",
    "An open pneumothorax needs a direct wound in the chest wall that lets air in during inhalation. Tell: he has blunt trauma with no chest wall wound, and his shock with tracheal shift marks trapped air under tension.", "ruled out by a stated finding"]],
  CS(62, 63, 64, 66, 77, 88), "manifestation", "diagnosis"),

V(T_TENSION, IO_A,
  "A 41-year-old woman on a ventilator after a fall suddenly becomes hypotensive at 74/46 mm Hg. Her trachea has shifted to the right, her neck veins are distended and breath sounds are absent on the left. No chest tube kit is readily available on the unit. Which is the most appropriate next step?",
  [["Needle decompression",
    "Correct. Tension pneumothorax is a clinical diagnosis, and time is critical. Immediate chest tube placement is ideal, but when a chest tube is not readily available, immediate needle decompression is performed, followed by a moderate or large chest tube and admission."],
   ["Chest radiograph first",
    "Tension pneumothorax is a medical emergency diagnosed clinically: there is no time for the X-ray. Tell: hypotension, tracheal shift, distended neck veins and absent breath sounds are enough to act on.", "wrong stage or severity"],
   ["Catheter aspiration",
    "Tension pneumothorax and hemodynamic instability are both contraindications to catheter aspiration. Tell: she has both; the emergency tool without a chest tube is needle decompression.", "ruled out by a stated finding"],
   ["Chest computed tomography",
    "Computed tomography is the best test for the presence, size and location of a pneumothorax, but it is impractical in a time-critical situation. Tell: she is hypotensive with tension signs, and every minute counts.", "wrong stage or severity"]],
  CS(33, 39, 64, 66), "first-line", "next step"),

V(T_TENSION, IO_A,
  "A 29-year-old man with a stab wound to the left chest develops hypotension, tracheal deviation to the right, distended neck veins and absent left breath sounds. With no chest tube kit at hand, needle decompression is performed, and his blood pressure improves. Which step should follow?",
  [["Chest tube insertion",
    "Correct. Needle decompression of a tension pneumothorax is followed by moderate or large-size chest tube insertion, then admission. The needle relieves the pressure for now, but the goals of therapy, evacuating the space and closing the leak, need the tube."],
   ["Observe after the needle",
    "Needle decompression relieves the tension but is not where care ends. Tell: it is followed by a moderate or large chest tube, because the space still has to be evacuated and the leak closed.", "wrong stage or severity"],
   ["Catheter aspiration",
    "Traumatic and tension pneumothorax are both contraindications to catheter aspiration. Tell: his stab wound and tension physiology rule it out; the chest tube follows the needle.", "ruled out by a stated finding"],
   ["Thoracoscopic surgery",
    "Thoracoscopic surgery is indicated for recurrence, bilateral pneumothorax, failure of a chest tube or secondary pneumothorax. Tell: none applies yet; after the needle, the next step is a chest tube.", "wrong stage or severity"]],
  CS(36, 39, 49, 66), "escalation", "next step"),

V(T_TENSION, IO_A,
  "A 38-year-old man of average build has hypotension, tracheal deviation to the left, distended neck veins and absent breath sounds on the right after blunt chest trauma. No chest tube kit is readily available, so needle decompression is planned. Where is the needle typically inserted?",
  [["Right 2nd intercostal space, midclavicular",
    "Correct. Needle decompression, also called needle thoracostomy, typically goes in on the thoracic side of the pneumothorax, in the 2nd intercostal space, over the 3rd rib, at the midclavicular line. His silent right chest with the trachea pushed left puts the pneumothorax on the right."],
   ["Left 2nd intercostal space, midclavicular",
    "The trachea deviates away from a tension pneumothorax, toward the contralateral side. Tell: his trachea points left because the trapped air is on the right, where breath sounds are absent; the needle goes on the side of the pneumothorax.", "reversed direction or value"],
   ["Right 2nd intercostal space, midaxillary",
    "The midaxillary line is the typical chest tube line, used at the 4th or 5th intercostal space. Tell: the needle decompression site pairs the 2nd intercostal space with the midclavicular line.", "adjacent fact"],
   ["Right 3rd intercostal space, midclavicular",
    "The needle passes over the 3rd rib, which places it in the 2nd intercostal space, not below that rib. Tell: the typical site is the 2nd intercostal space at the midclavicular line on the affected side.", "reversed direction or value"]],
  CS(64, 66, 67, 68), "agent/regimen", "treatment"),

V(T_TENSION, IO_A,
  "A 52-year-old woman with a rib fracture from a fall becomes acutely hypotensive, with tracheal deviation to the right, distended neck veins and absent breath sounds on the left. A chest tube kit is at the bedside. Which action should be avoided?",
  [["Waiting for a chest radiograph",
    "Correct. Tension pneumothorax is a medical emergency and a clinical diagnosis: time is critical, and there is no time for the X-ray. With a chest tube readily available, immediate chest tube placement is ideal, so waiting for imaging only wastes the time she does not have."],
   ["Immediate chest tube placement",
    "Immediate chest tube placement is the ideal treatment for tension pneumothorax when a tube is readily available. Tell: her kit is at the bedside, so placing it now is the right move, not one to avoid.", "reversed direction or value"],
   ["Hospital admission",
    "Admission follows decompression and chest tube insertion for tension pneumothorax. Tell: it is part of her care, while delaying treatment for a film is the error.", "reversed direction or value"],
   ["Chest tube at the midaxillary line",
    "The typical chest tube site is the 4th or 5th intercostal space at the midaxillary line. Tell: placing her tube there is standard practice, not something to avoid.", "reversed direction or value"]],
  CS(41, 65, 66, 68), "avoid", "avoid"),

V(T_TENSION, IO_A,
  "A 25-year-old man has a stab wound to the right chest wall. Air can be heard moving through the wound, which draws air into the pleural space with each inhalation, and breath sounds are diminished on the right. How is his pneumothorax classified?",
  [["Open pneumothorax",
    "Correct. An open pneumothorax has a direct wound in the chest wall that allows air to enter the pleural space during inhalation, and it can lead to a sucking chest wound. A penetrating stab wound is a traumatic cause."],
   ["Closed pneumothorax",
    "A closed pneumothorax has no external wound; air enters the pleural space from the lung because of broken ribs or internal injuries. Tell: his chest wall is open, and air enters through the wound itself.", "ruled out by a stated finding"],
   ["Primary spontaneous",
    "Spontaneous pneumothorax means no thoracic trauma; primary adds no underlying lung abnormality. Tell: he has a penetrating stab wound, which makes his pneumothorax traumatic.", "ruled out by a stated finding"],
   ["Iatrogenic",
    "Iatrogenic pneumothorax is pleural injury from a medical intervention, such as thoracentesis or a subclavian vein catheter. Tell: his wound came from a stabbing, not a procedure.", "ruled out by a stated finding"]],
  CS(17, 61, 62), "etiology", "classify"),

V(T_TENSION, IO_A,
  "A 46-year-old woman falls from a ladder and fractures several left ribs. The skin over her chest is intact, and a chest radiograph shows a visceral pleural line on the left. How is her pneumothorax classified?",
  [["Closed traumatic",
    "Correct. Blunt chest trauma in which a rib fracture tears the lung is a traumatic pneumothorax. With no external wound, air enters the pleural space from the lung because of the broken ribs, which makes it closed."],
   ["Open traumatic",
    "An open traumatic pneumothorax has a direct chest wall wound that lets air in during inhalation. Tell: her skin is intact, so the air came from the torn lung, not through the chest wall.", "ruled out by a stated finding"],
   ["Iatrogenic",
    "Iatrogenic pneumothorax follows a medical intervention such as bronchoscopy or mechanical ventilation. Tell: her pneumothorax followed a fall with rib fractures, which is thoracic trauma, not a procedure.", "ruled out by a stated finding"],
   ["Primary spontaneous",
    "Spontaneous pneumothorax means no thoracic trauma, and primary means no underlying lung abnormality. Tell: she fell and broke ribs, which is thoracic trauma.", "ruled out by a stated finding"]],
  CS(17, 61, 62), "etiology", "classify"),

V(T_TENSION, IO_A,
  "A 33-year-old man with a tension pneumothorax after a gunshot wound has hypotension, tracheal deviation to the right, distended neck veins and absent left breath sounds. His family asks why his blood pressure has fallen. Which mechanism explains his hypotension?",
  [["Less venous return to the heart",
    "Correct. In tension pneumothorax, air trapped by a one-way valve shifts the mediastinum to the contralateral side. Venous return to the heart decreases, cardiac output falls, and hypotension follows, along with tracheal deviation and neck vein distention."],
   ["Blood loss into the chest",
    "Bleeding into the pleural space is hemothorax, and trauma is its most common cause. Tell: his distended neck veins and tracheal shift fit trapped air impeding venous return, the tension mechanism.", "competing diagnosis"],
   ["Increased cardiac output",
    "Tension pneumothorax lowers cardiac output, it does not raise it. Tell: the mediastinal shift decreases venous return to the heart, so output and blood pressure both fall.", "reversed direction or value"],
   ["Slowed heart rate",
    "The listed consequences of tension pneumothorax are decreased venous return and cardiac output, with hypotension, tracheal deviation and neck vein distention. Tell: his pressure falls because filling falls, not because the heart slows.", "confused mechanism or drug class"]],
  CS(63, 64, 69), "complication", "complication"),

# ---------------------------------------------------------------- hemothorax
V(T_HEMO, IO_A,
  "A 40-year-old man has blunt chest trauma from a motor vehicle crash. He has dullness to percussion and diminished breath sounds at the right base, and an upright chest radiograph shows a large right pleural fluid collection consistent with a hemothorax. Which is the most appropriate initial treatment?",
  [["Chest tube to drain and quantify",
    "Correct. Trauma is the most common cause of hemothorax, and treatment begins with a chest tube to evacuate and quantify the bleeding; tube thoracostomy is the essential first step for drainage. The measured output then decides whether a thoracotomy is needed."],
   ["Catheter aspiration",
    "Traumatic pneumothorax is a contraindication to catheter aspiration, a technique for removing air in selected spontaneous cases. Tell: his chest holds blood after trauma, which needs a chest tube that both drains and measures it.", "ruled out by a stated finding"],
   ["Immediate thoracotomy",
    "Thoracotomy is the step when blood loss through the chest tube exceeds 200 mL per hour. Tell: no tube is in yet and no output has been measured, so the tube comes first.", "wrong stage or severity"],
   ["Observation and repeat film",
    "Leaving the blood in place risks retained hemothorax, which leads to empyema, fibrothorax and trapped lung. Tell: a large traumatic hemothorax is drained with a chest tube from the start.", "wrong stage or severity"]],
  CS(39, 69, 74), "first-line", "treatment"),

V(T_HEMO, IO_A,
  "A 36-year-old woman with a hemothorax after a stab wound has a chest tube placed. Over the next 2 hours it drains blood at about 300 mL per hour, and her blood pressure is falling. Which is the most appropriate next step?",
  [["Thoracotomy",
    "Correct. The chest tube evacuates and quantifies the bleeding, and blood loss over 200 mL per hour calls for thoracotomy, an open approach to the intrathoracic space. Persistent hemorrhage or shock is the indication for surgery, and she has both."],
   ["Continued tube drainage",
    "Continued drainage alone fits bleeding that slows below the surgical threshold. Tell: her output of about 300 mL per hour exceeds 200 mL per hour and her pressure is falling, so the tube has done its job of measuring and surgery follows.", "wrong stage or severity"],
   ["Chemical pleurodesis",
    "Chemical pleurodesis makes the pleural layers adhere to prevent recurrent pneumothorax or a recurring effusion. Tell: it does nothing to stop active bleeding into the chest.", "adjacent fact"],
   ["Needle decompression",
    "Needle decompression relieves a tension pneumothorax when no chest tube is at hand. Tell: she already has a chest tube, and her problem is blood loss, not trapped air.", "competing diagnosis"]],
  CS(45, 66, 69, 74), "referral", "referral"),

V(T_HEMO, IO_A,
  "A 58-year-old man has a bloody-appearing pleural effusion after a fall. The pleural fluid hematocrit is 30%, and his blood hematocrit is 40% (normal 41-53%). How is the effusion classified?",
  [["Hemothorax",
    "Correct. A pleural fluid hematocrit over 50% of the peripheral blood hematocrit defines a hemothorax, while under 50% marks a hemorrhagic effusion. His fluid hematocrit of 30% is 75% of his blood value of 40%, well over half, and trauma causes most hemothoraces."],
   ["Hemorrhagic effusion",
    "A hemorrhagic effusion is bloody fluid whose hematocrit is under 50% of the blood hematocrit. Tell: 30 divided by 40 is 75%, above the 50% cutoff, so this is a hemothorax.", "reversed direction or value"],
   ["Chylothorax",
    "Chylothorax is lipid from chyle in the pleural space, with milky fluid and elevated triglycerides. Tell: his fluid is bloody, and its hematocrit is the deciding measurement.", "competing diagnosis"],
   ["Empyema",
    "Empyema is purulent fluid in the pleural space, usually after bacterial pneumonia with a parapneumonic effusion. Tell: his fluid is bloody after a fall, not purulent after an infection.", "competing diagnosis"]],
  CS(74, 98, 105, 108), "test finding", "classify"),

V(T_HEMO, IO_A,
  "A 47-year-old man had a traumatic hemothorax that was only partly drained, and a collection of blood remains in his pleural space weeks later. Which complication does this retained blood most directly risk?",
  [["Empyema",
    "Correct. Undrained blood collections serve as a primary nidus for infection, and a retained hemothorax leads directly to empyema, as well as fibrothorax and trapped lung. That is why tube thoracostomy, the essential first step, aims to evacuate the blood."],
   ["Tension pneumothorax",
    "Tension pneumothorax is trapped air under a one-way valve with hypotension and tracheal deviation. Tell: retained blood is fluid, and its risk is infection of that fluid.", "competing diagnosis"],
   ["Chylothorax",
    "Chylothorax follows thoracic duct disruption, most often from trauma such as thoracic surgery, and fills the space with chyle. Tell: retained blood does not become chyle; it becomes a nidus for infection.", "competing diagnosis"],
   ["Pneumomediastinum",
    "Pneumomediastinum is air in the mediastinal tissues after alveolar rupture or esophageal perforation. Tell: blood left in the pleural space risks infection, not mediastinal air.", "competing diagnosis"]],
  CS(63, 74, 75, 104), "complication", "complication"),

# ---------------------------------------------------------------- pneumomediastinum
V(T_PMED, IO_A,
  "A 19-year-old man has several hours of pleuritic chest and neck pain, sore throat and mild dyspnea after a bout of violent vomiting. On examination there is palpable subcutaneous emphysema (crackling under the skin) in his neck and a Hamman crunch (substernal crackling heard with each heartbeat). His breath sounds are equal, and his chest is not hyperresonant. What is the most likely diagnosis?",
  [["Pneumomediastinum",
    "Correct. Air collects in the mediastinal tissues, often after a sudden rise in intrathoracic pressure such as violent coughing, vomiting or inhalation drug use. Nonspecific chest or neck pain, sore throat, dyspnea, subcutaneous emphysema in the neck and a crunch synchronous with the heartbeat fit."],
   ["Spontaneous pneumothorax",
    "A spontaneous pneumothorax brings hyperresonance and diminished breath sounds on the affected side. Tell: his breath sounds are equal and his chest is not hyperresonant; the air is in his neck and mediastinum.", "ruled out by a stated finding"],
   ["Pericarditis",
    "Pericarditis is among the dangerous causes of pleuritic-type chest pain. Tell: his crunch comes from the heart beating against air-filled tissue, and the palpable air in his neck places that air in the mediastinum.", "competing diagnosis"],
   ["Pleurisy",
    "Pleurisy produces a pleural friction rub that disappears when the patient holds his breath. Tell: his sound keeps time with the heartbeat, and the crackling air under his neck skin is not a pleural finding.", "competing diagnosis"]],
  CS(12, 13, 23, 75, 76, 77), "manifestation", "diagnosis"),

V(T_PMED, IO_A,
  "A 22-year-old woman has spontaneous pneumomediastinum after a severe coughing fit. She is speaking comfortably, her airway is patent and her vital signs are stable, and no underlying cause such as esophageal perforation is found. Which management is most appropriate?",
  [["Oxygen, rest and analgesics",
    "Correct. Once the airway is assessed and maintained, and with no cause to treat, pneumomediastinum is managed conservatively: the air is often gradually absorbed, oxygen may increase air absorption, physical activity is avoided and analgesics are given."],
   ["Chest tube insertion",
    "A chest tube drains air or fluid from the pleural space in pneumothorax or effusion. Tell: her air sits in the mediastinal tissues, not the pleural space, and it usually absorbs on its own.", "competing diagnosis"],
   ["Needle decompression",
    "Needle decompression relieves a tension pneumothorax with hypotension and tracheal deviation. Tell: she is stable with normal vital signs, and air in the mediastinum is not trapped pleural air under tension.", "competing diagnosis"],
   ["Emergent cardiothoracic surgery",
    "An emergent cardiothoracic surgery consult is reserved for severe pneumomediastinum. Tell: she is stable with a patent airway, so conservative care fits.", "wrong stage or severity"]],
  CS(41, 66, 75, 79), "first-line", "treatment"),

V(T_PMED, IO_A,
  "A 27-year-old man with pneumomediastinum after forceful breath-holding while inhaling an illicit drug develops worsening dyspnea, subcutaneous emphysema spreading up his neck and a falling oxygen saturation despite oxygen. His airway is being supported. Which referral is most appropriate?",
  [["Cardiothoracic surgery",
    "Correct. Pneumomediastinum is usually managed conservatively, but if it is severe, cardiothoracic surgery is consulted emergently, after the airway is assessed and maintained. His worsening dyspnea, spreading emphysema and falling saturation despite oxygen mark severe disease."],
   ["Outpatient pulmonology",
    "An outpatient visit fits a stable patient whose air is expected to absorb with conservative care. Tell: his disease is worsening despite oxygen, which calls for an emergent consult.", "wrong stage or severity"],
   ["Genetics referral",
    "Genetics referral is recommended after spontaneous pneumothorax when the family history shows the same condition. Tell: his problem is severe mediastinal air after drug inhalation, which needs surgery now.", "adjacent fact"],
   ["Gastroenterology clinic",
    "Esophageal perforation is one cause of pneumomediastinum, and an identified cause is treated. Tell: his history points to a pressure rise from breath-holding, and his worsening state needs an emergent surgical consult, not a clinic visit.", "wrong stage or severity"]],
  CS(60, 75, 76, 79), "referral", "referral"),

V(T_PMED, IO_A,
  "An 18-year-old woman with spontaneous pneumomediastinum after an episode of violent coughing asks how coughing could put air in her chest. Which explanation is accurate?",
  [["Alveoli ruptured under pressure",
    "Correct. Violent coughing is a sudden increase in intrathoracic pressure. Excessive intra-alveolar pressure leads to rupture of alveoli bordering the mediastinum, and the escaping air collects in the mediastinal tissues."],
   ["A chest wall wound let air in",
    "A direct chest wall wound that lets air in during inhalation is an open pneumothorax. Tell: she has no wound; her air came from inside the lung after a pressure rise.", "competing diagnosis"],
   ["An apical bleb burst",
    "Rupture of an apical bleb, a small air space within the visceral pleura, causes spontaneous pneumothorax, with air in the pleural space. Tell: her air is in the mediastinum, from alveoli that border it.", "competing diagnosis"],
   ["Infection produced the gas",
    "The listed causes of pneumomediastinum are alveolar rupture from high pressure, esophageal perforation, and esophageal or bowel rupture with air dissecting into the mediastinum. Tell: coughing raised the pressure that ruptured alveoli; no infection made gas.", "common lay belief"]],
  CS(18, 62, 75, 76), "etiology", "education"),

]
