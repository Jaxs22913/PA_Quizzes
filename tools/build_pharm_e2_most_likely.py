#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build 'Pharmacology I Exam 2: Most Likely 40' (Jaxon, 2026-10-03, two days before the exam).

THE REQUEST. "Make a 40 questions quiz with the most likely questions he would ask [Dr. Wood] with about equal
weighting on the lectures." Forty questions, EIGHT PER LECTURE (Lectures 4 to 8: ophthalmic, ear/nose/throat,
antihypertensives, lipids, myocardial ischemia), chosen as the questions he is most likely to ask. Nobody can know
what will be asked; this is an evidence-ranked bet, and the quiz says so.

THE EVIDENCE (five signals, all read from files in this repo, none invented):

  1. WOOD  tools/pharm_e2/wood.json: 116 timestamped entries from his own recordings (kinds: emphasis, scope,
           rule, shape, marker). He says what he WILL test ("I will ask this question", "it'll be somewhere on the
           test", "a cornucopia of test questions"), HOW he writes stems ("delineate between these products",
           "patient is on this, what do you add next", "a patient who drives for a living"), and what he will NOT
           test (the antibiotic indication table, shared side effects, the natamycin organisms, statin intensity
           by patient, the ACE inhibitor versus receptor blocker elimination route, cell lines, dosages).
  2. GUIDE the Exam 2 study guide already stars what he stressed ('Professor emphasized'); a question whose linked
           guide passage carries the star gets a point.
  3. KCZ   tools/pharm_e2/L4..L8.json 'killers' (the adverse effects and traps that hurt a patient or are the classic
           miss) and the absolute-contraindication tier of 'contra'.
  4. MCINNIS the course director's correction (pharmacology_exam_spec): indications, patient education, side
           effects and contraindications are examined MORE than mechanism, so those question kinds score up and
           mechanism scores down.
  5. SHAPE the Exam 1 / Exam 2 question shapes the course actually uses and Wood described: class before agent,
           first-line / add-on / switch, which-is-contraindicated, counseling, one class-discrimination item.

HOW THE PICKS WERE MADE. `score()` below ranks every shipped, vetted Exam 2 question (676, from the same sets files
the topic quizzes and masters are rendered from) by the five signals; the ranked list per lecture is written to
tools/pharm_e2_most_likely_report.json. The final eight per lecture are then chosen BY HAND from the top of that
ranking against the entry-by-entry map in PICKS (each pick names the Wood entry numbers that drove it), because
the score cannot see two things a person must: (a) the spread of shapes inside a lecture and (b) near-duplicates.
Equal weighting is kept at 8/8/8/8/8 even where one lecture's eighth pick is weaker than another's ninth.

HARD EXCLUSIONS (they stay in the topic quizzes):
  * dosages, doses, regimens, frequencies (Dr. Wood: no dosages): same DOSE_KEY rule as the master exams. The ONE
    number he told the class to memorize, the acetaminophen daily limit, is therefore NOT asked: Jaxon's
    instruction (no dosages) wins and the report flags it.
  * Exam 3 content, course mechanics, anything he said is not tested.
  * a fact he said aloud that the slides do not carry (sinus rinses: distilled water) stays out: slides-only
    grounding, and the guide has no passage that states it.

SOURCING. 39 of the 40 come from the shipped pools; 33 are reused VERBATIM (their option explanations, citations and
audited guide links come with them: a link is keyed to the stem plus the correct option text, so the same question
keeps the same link), 5 had a stacked or underspecified stem rewritten after the independent review (REPLACE;
each re-audited by a separate judge), and ten distractor explanations on five Lecture 4 vignettes were lengthened to
meet the 60-character rule (EXPL_OVERRIDE). One question is NEW (NEW_QUESTIONS below), written to the full standard
for Wood's own worked example of a stem ("a truck driver, which antihistamine"), because the pools had no question
for it. Reviewer swaps after the first draft: ht:raas2:6 (add-next shape), li:statin1:9 (statin pregnancy) and
mv:set1:22 (add-on) replaced a pregnancy yes/no, a muscle-toxicity item and the five-minute nitroglycerin item.

POSITIONS. Answer letters are re-dealt so the quiz holds exactly ten of each letter, two of each inside every
lecture, with no run longer than two; the key moves with its explanation.

    python3 tools/build_pharm_e2_most_likely.py   # writes tools/pharm_e2_most_likely_sets.json + ..._report.json
    python3 tools/render_pharm_e2_most_likely.py  # writes Pharmacology I Exam 2/pharm-e2-most-likely-40.html
"""
import html as H
import json
import os
import random
import re
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import build_guide_links as B  # noqa: E402  (same key function the guide-link builder uses)

OUT = os.path.join(HERE, "pharm_e2_most_likely_sets.json")
REPORT = os.path.join(HERE, "pharm_e2_most_likely_report.json")
FOLDER = os.path.join(ROOT, "Pharmacology I Exam 2")
SEED = 20261003

FILES = {"op": "pharm_oph_sets.json", "e2": "pharm_e2_vignette_sets.json", "en": "pharm_ent_sets.json",
         "ht": "pharm_htn_sets.json", "li": "pharm_lipid_sets.json", "ms": "pharm_mi_sets.json",
         "mv": "pharm_mi_vignette_sets.json"}
LEC_OF = {"op": "L4", "e2": "L4", "en": "L5", "ht": "L6", "li": "L7", "ms": "L8", "mv": "L8"}
LEC_NAME = {"L4": "Lecture 4: Ophthalmic Drugs", "L5": "Lecture 5: Ear, Nose and Throat Drugs",
            "L6": "Lecture 6: Antihypertensive Drugs", "L7": "Lecture 7: Lipid-Lowering Drugs",
            "L8": "Lecture 8: Myocardial Ischemia Drugs"}
DOSE_KEY = re.compile(r"(?i)\bdos(e|es|ing|age)\b|\bonce daily\b|\btwice\b|\b\d+(\.\d+)?\s*(mg|mcg|microgram|units?)\b|\bregimen")

# --------------------------------------------------------------------------------------------------------------
# The Wood entries behind each pick are numbered as in tools/pharm_e2/wood.json (0-based position in 'entries').
# shape = the question shape the pick fills in its lecture.
# --------------------------------------------------------------------------------------------------------------
PICKS = [
    # ---- Lecture 4: ophthalmic -------------------------------------------------------------------------------
    dict(ref="e2:set2:1", lec="L4", shape="patient education", wood=[5],
         why="Rebound hyperemia and the two-week limit: he said 'I will ask this question ... star that, underline "
             "it, highlight it' and that people still miss it every test."),
    dict(ref="e2:set2:12", lec="L4", shape="side effect / safety", wood=[6],
         why="Vasoconstrictor drops swallowed by a toddler (alpha-1 locally, alpha-2 systemically): he spent a "
             "minute on 'OTC does not mean safe' and the counseling point."),
    dict(ref="op:inflam1:7", lec="L4", shape="class discrimination", wood=[8],
         why="'Three which are going to be starred': the soft steroids (fluorometholone, loteprednol, rimexolone) "
             "against the hard-hitting dexamethasone."),
    dict(ref="e2:set1:17", lec="L4", shape="first-line drug choice", wood=[10],
         why="Glaucoma ladder: prostaglandin analogs first line. He gave the order and a stem shape for it."),
    dict(ref="e2:set2:16", lec="L4", shape="contraindication", wood=[11, 12],
         why="Asthma history: choose the beta-1 selective drop (betaxolol). 'Just ones you kind of have to know.'"),
    dict(ref="e2:set1:7", lec="L4", shape="add-on / escalation", wood=[14],
         why="His own stem: 'patient is on this drug, what would you add?' and the right answer is a different "
             "mechanism, never a second drug of the same class."),
    dict(ref="op:anti1:12", lec="L4", shape="contraindication", wood=[2],
         why="Sulfacetamide and a sulfonamide allergy: 'one thing you might want to be worried about ... notable'; "
             "the only antibiotic restriction he singled out."),
    dict(ref="op:anti2:16", lec="L4", shape="indication / class before agent", wood=[3],
         why="Corneal ulcer or contact lens wearer means Pseudomonas, and the fluoroquinolone is the class."),
    # ---- Lecture 5: ear, nose and throat -----------------------------------------------------------------------
    dict(ref="en:cough1:14", lec="L5", shape="side effect / patient education", wood=[28],
         why="Oxymetazoline rebound congestion: 'I highlight this every year ... it'll be somewhere on the test, "
             "and a significant number of people still miss it.'"),
    dict(ref="en:anti2:14", lec="L5", shape="contraindication", wood=[18],
         why="Polymyxin B with a ruptured eardrum or tubes: 'really important ... an absolute contraindication'; he "
             "asked it two ways (which is contraindicated, which is preferred)."),
    dict(ref="NEW:truck", lec="L5", shape="drug choice vignette", wood=[26],
         why="His worked example of a vignette: a patient who drives a truck for a living, which antihistamine. "
             "Second-generation agents barely sedate; first-generation ones are the ones to avoid."),
    dict(ref="en:anti1:7", lec="L5", shape="side effect / interaction", wood=[19],
         why="'Anytime you see QT prolongation or CYP3A4, make a note ... why do I make so many test questions "
             "about that?' Ketoconazole is that lecture's example."),
    dict(ref="en:inflam1:4", lec="L5", shape="contraindication", wood=[23],
         why="Reye syndrome: no aspirin for a child with a viral illness ('a really notable one ... potentially fatal')."),
    dict(ref="en:anti1:17", lec="L5", shape="failed first-line, next step", wood=[15],
         why="'First line, the backup if allergic, what if first line failed': the failure step for ear infection "
             "(no better at three days, step up to amoxicillin-clavulanate). The first-line item itself is not "
             "used because its key is 'high-dose amoxicillin' and he does not test doses."),
    dict(ref="en:inflam2:2", lec="L5", shape="class discrimination", wood=[21],
         why="Aspirin is an irreversible platelet inhibitor and ibuprofen is not: 'the key difference'."),
    dict(ref="en:inflam2:10", lec="L5", shape="interaction / monitoring", wood=[24, 34, 30],
         why="NSAID with a diuretic and an ACE inhibitor: the stomach and the kidney are the two big concerns, and "
             "he said to highlight anything kidney-toxic."),
    # ---- Lecture 6: antihypertensives ---------------------------------------------------------------------------
    dict(ref="ht:raas1:3", lec="L6", shape="first-line drug choice", wood=[52, 30],
         why="His own stem: 'based off this comorbidity, what do you start with', and his example is type 2 "
             "diabetes, so an ACE inhibitor or receptor blocker for the kidney protection."),
    dict(ref="ht:raas1:17", lec="L6", shape="class discrimination", wood=[36],
         why="ACE inhibitor versus receptor blocker: cough and angioedema ('great for test questions')."),
    dict(ref="ht:raas2:6", lec="L6", shape="add-on / next step", wood=[52],
         why="His own stem again: 'the patient's on this, what do you want to go to next?' After an ACE inhibitor plus "
             "a dihydropyridine, the diuretic is the third drug (the order he walked through)."),
    dict(ref="ht:raas1:11", lec="L6", shape="side effect / laboratory", wood=[31],
         why="'Anytime a medication affects your potassium ... a very easy test question to ask.'"),
    dict(ref="ht:ccb2:6", lec="L6", shape="drug choice", wood=[38, 39],
         why="'Which one would you use to reduce heart rate? It's diltiazem or verapamil'; he repeated it for "
             "emphasis and called it very easy to ask."),
    dict(ref="ht:beta1:5", lec="L6", shape="patient education", wood=[47],
         why="Never stop a beta blocker abruptly (rebound, receptor up-regulation); he repeated it in Lecture 8."),
    dict(ref="ht:ccb2:8", lec="L6", shape="patient education", wood=[40, 89],
         why="Constipation with the calcium channel blockers: 'very, very, very common ... ask about bowel habits'; "
             "stressed again in Lecture 8."),
    dict(ref="ht:beta1:10", lec="L6", shape="class discrimination", wood=[44, 45],
         why="Carvedilol and labetalol break the letter rule and add alpha-1 blockade: 'you just have to know these'."),
    # ---- Lecture 7: lipids ---------------------------------------------------------------------------------------
    dict(ref="li:ldl2:5", lec="L7", shape="contraindication", wood=[60],
         why="His own question: a triglyceride of 600, which class is contraindicated (the bile acid resin)."),
    dict(ref="li:tg1:2", lec="L7", shape="drug choice", wood=[57],
         why="His own question: the patient's only problem is very high triglycerides, which class is best (fibrate)."),
    dict(ref="li:statin2:6", lec="L7", shape="interaction", wood=[53],
         why="Statins cleared by CYP3A4 and the way around it when the patient must be on verapamil or diltiazem "
             "(rosuvastatin): 'definitely know these'."),
    dict(ref="li:tg2:11", lec="L7", shape="patient education", wood=[63],
         why="Niacin flushing: aspirin pretreatment and extended release, with the prostaglandin reason."),
    dict(ref="li:tg2:7", lec="L7", shape="interaction", wood=[58],
         why="Statin plus fibrate: 'really careful ... myopathy risk goes up'; he said it under both drug classes."),
    dict(ref="li:ldl2:4", lec="L7", shape="patient education", wood=[59],
         why="Bile acid resins bind other medicines: 'really critical ... separate from other meds'."),
    dict(ref="li:statin2:5", lec="L7", shape="indication", wood=[66],
         why="The four statin benefit groups: 'I'd want you to be able to identify those four risk categories'."),
    dict(ref="li:statin1:9", lec="L7", shape="contraindication", wood=[55],
         why="'ACEs, ARBs and now the statins are going to be mega no-no-go for pregnancy.'"),
    # ---- Lecture 8: myocardial ischemia --------------------------------------------------------------------------
    dict(ref="mv:set1:24", lec="L8", shape="switch vignette", wood=[84, 82],
         why="'He wrote this question out loud': a beta blocker not tolerated because of nightmares, what to "
             "switch to (a non-dihydropyridine calcium channel blocker)."),
    dict(ref="mv:set1:16", lec="L8", shape="interaction / safety", wood=[90],
         why="Nitrate with a phosphodiesterase-5 inhibitor: 'profound hypotension ... they could die'."),
    dict(ref="ms:anginal2:12", lec="L8", shape="quick relief versus prevention", wood=[77, 91],
         why="'Which is best for quick relief': sublingual nitroglycerin. He said he will keep repeating the "
             "prophylaxis-versus-acute distinction."),
    dict(ref="mv:set1:22", lec="L8", shape="add-on", wood=[78, 83],
         why="'Patient's already on this and not at goal, what do you want to do next?': a dihydropyridine is added "
             "to a beta blocker (a non-dihydropyridine is not)."),
    dict(ref="ms:anginal1:20", lec="L8", shape="contraindication", wood=[85, 101],
         why="Variant (Prinzmetal) angina: calcium channel blocker, and avoid the beta blocker."),
    dict(ref="ms:anginal1:27", lec="L8", shape="interaction", wood=[83, 99, 48],
         why="Beta blocker with verapamil or diltiazem is 'begging for trouble' (bradycardia, heart block); a "
             "dihydropyridine is the partner. Stressed in Lectures 6 and 8."),
    dict(ref="mv:set1:1", lec="L8", shape="comorbidity table", wood=[96, 97],
         why="The comorbidity table was 'a cornucopia of test questions'; prior myocardial infarction means prefer a "
             "beta blocker and avoid calcium channel blockers (keyed as the course taught it; the explanation says "
             "what current practice allows)."),
    dict(ref="mv:set1:14", lec="L8", shape="contraindication vignette", wood=[110],
         why="Fibrinolytic contraindications: 'go through this checklist ... once it's given you can't take it away'."),
]

# --------------------------------------------------------------------------------------------------------------
# NEW question (Wood's own worked example). Every option is explained (refutes AND supplies the replacing fact).
# The guide already states both facts (s195 second-generation agents largely stay out of the central nervous
# system; s196 fexofenadine and loratadine are rated very low for sedation, cetirizine low; the table rates
# diphenhydramine, hydroxyzine and promethazine high).
# --------------------------------------------------------------------------------------------------------------
NEW_QUESTIONS = {
    "NEW:truck": {
        "topic": "Antihistamines and sedation",
        "io": "Compare the first- and second-generation histamine-1 (H1) antagonists",
        "slot": "drug choice",
        "q": "A 45-year-old long-haul truck driver has seasonal allergic rhinitis and drives 12 hours a day. Which "
             "antihistamine is the most appropriate choice for him?",
        "opts": [
            ["Fexofenadine",
             "Correct. A second-generation histamine-1 (H1) blocker largely stays out of the central nervous system "
             "and is rated very low for sedation, so it treats the allergy without making a driver drowsy."],
            ["Diphenhydramine",
             "A first-generation agent rated high for sedation and for antimuscarinic effects; drowsiness is the "
             "wrong trade for a driver, and a second-generation agent such as fexofenadine avoids it."],
            ["Hydroxyzine",
             "A first-generation agent rated high for sedation. It crosses into the brain, and the sedation adds up "
             "with alcohol and other depressants, so a driver should be given a second-generation drug instead."],
            ["Promethazine",
             "One of four first-generation agents rated high for sedation, and it is also high for antiemetic and "
             "antimuscarinic effects; that is a poor fit for a driver, whereas fexofenadine is rated very low for sedation."],
        ],
        "c": 0,
        "cite": "ENT Jax Pharmacology.pptx, Slides 32 and 37",
    },
}


# --------------------------------------------------------------------------------------------------------------
# Five Lecture 4 vignettes (pharm_e2_vignette_sets.json) predate the 60-character explanation rule: ten of their
# distractor explanations are 18 to 54 characters and only say "no". In THIS quiz each is rewritten to refute AND
# supply the replacing fact (checked against the guide). The source sets are left alone (their pages are shipped);
# the rewrite is keyed by (pick, option text) so it cannot attach to the wrong option after positions are dealt.
# --------------------------------------------------------------------------------------------------------------
EXPL_OVERRIDE = {
    ("e2:set2:1", "As long as her eyes stay red"):
        "Using the drops for as long as the eyes stay red is exactly what produces rebound hyperemia; the limit is no more than two weeks.",
    ("e2:set2:1", "No more than six weeks"):
        "Six weeks is far beyond the stated limit. The receptors down-regulate with longer use, so the cap is no more than two weeks.",
    ("e2:set2:12", "They inhibit carbonic anhydrase systemically"):
        "Carbonic anhydrase inhibition is how dorzolamide and brinzolamide work, a different glaucoma class; swallowed redness-relief drops act on alpha-2 receptors.",
    ("e2:set1:17", "A carbonic anhydrase inhibitor"):
        "Effective, but carbonic anhydrase inhibitors are third or fourth line because of burning, stinging and a bitter taste; the first-line class is the prostaglandin analogs.",
    ("e2:set1:17", "A topical glucocorticoid"):
        "A topical glucocorticoid raises intraocular pressure and can cause glaucoma, so it works against the goal; the first-line class is the prostaglandin analogs.",
    ("e2:set1:17", "A cholinergic agonist"):
        "Cholinergic agonists such as pilocarpine are the last-line class because side effects and frequent dosing hurt compliance; the first-line class is the prostaglandin analogs.",
    ("e2:set1:7", "Add a second prostaglandin analog"):
        "A second drug of the same class works by the same mechanism, so it adds side effects without extra pressure lowering; add an agent with a different mechanism.",
    ("e2:set1:7", "Increase the prostaglandin to twice daily"):
        "Going beyond once daily actually inhibits a prostaglandin analog's pressure-lowering effect, so it backfires; the principle is to add a different mechanism.",
    ("e2:set1:7", "Add a topical steroid"):
        "A topical steroid raises intraocular pressure and can cause glaucoma, so it works against the goal; add an agent with a different mechanism instead.",
}


# --------------------------------------------------------------------------------------------------------------
# Rewrites made after the independent review (2026-10-03). A stacked stem ("which agent, and why?") asks two
# things, which the site forbids; one stem left the first drug unnamed; one distractor was defensible under current
# practice. Each replaces the shipped question's text IN THIS QUIZ ONLY (the topic quizzes keep theirs), so each
# gets its own guide-link audit. Every option still refutes AND supplies the replacing fact.
# --------------------------------------------------------------------------------------------------------------
REPLACE = {
    "op:inflam1:7": dict(
        q="Which ocular glucocorticoids are called soft steroids because they carry a lower risk of raising intraocular pressure?",
        opts=[["Fluorometholone, loteprednol and rimexolone",
               "Correct. These three are marked as the soft steroids because they carry a lower risk of raising eye pressure, which matters most in a patient who has glaucoma or is at risk of it."],
              ["Dexamethasone, prednisolone and difluprednate",
               "These are the harder-hitting steroids and raise eye pressure more readily; the soft steroids are fluorometholone, loteprednol and rimexolone."],
              ["Triamcinolone, dexamethasone and prednisolone",
               "Triamcinolone is the intravitreal agent and the other two are conventional, harder-hitting steroids; none is a soft steroid. The soft ones are fluorometholone, loteprednol and rimexolone."],
              ["Prednisolone, loteprednol and difluprednate",
               "Only loteprednol is a soft steroid; prednisolone and difluprednate are harder-hitting, so the group fails. The soft three are fluorometholone, loteprednol and rimexolone."]],
        c=0),
    "e2:set2:16": dict(
        q="A 58-year-old with asthma needs a beta blocker eye drop for glaucoma. Which agent is the best choice?",
        opts=[["Betaxolol",
               "Correct. Betaxolol is the beta-1 selective eye drop, so it carries the least risk of airway narrowing; the nonselective agents work better in the eye but add airway resistance."],
              ["Carteolol",
               "Carteolol is nonselective, so it carries the airway risk that asthma makes dangerous; the beta-1 selective drop, betaxolol, is the one to choose."],
              ["Levobunolol",
               "Levobunolol is also nonselective, so it carries the same airway risk; in asthma the beta-1 selective drop, betaxolol, is the one to choose."],
              ["Timolol",
               "Timolol is nonselective and more efficacious, but its added airway resistance is exactly the problem in asthma; betaxolol, the beta-1 selective drop, is the choice."]],
        c=0),
    "op:anti2:16": dict(
        q="A contact lens wearer has bacterial conjunctivitis and keratitis has been ruled out. Which class is preferred?",
        opts=[["A fluoroquinolone",
               "Correct. Contact lens use raises the risk of Pseudomonas aeruginosa, a gram-negative rod, and the fluoroquinolones are the class that covers it; they are also preferred for corneal ulcers for the same reason."],
              ["A macrolide",
               "Erythromycin is soothing and the commonest ophthalmic antibiotic, but macrolides do not address Pseudomonas, the organism lens wearers are at risk from; a fluoroquinolone is the class."],
              ["An aminoglycoside",
               "Aminoglycosides have gram-negative activity, but they carry a risk of corneal ulceration, and the class named for Pseudomonas and corneal ulcers is the fluoroquinolones."],
              ["A sulfonamide",
               "Sulfacetamide is cheap but does not answer the Pseudomonas risk, and it must be avoided altogether in sulfonamide allergy; a fluoroquinolone is the class."]],
        c=0),
    "en:anti1:17": dict(
        q="A child with acute otitis media was started on amoxicillin and has not improved after three days. What is the next step?",
        opts=[["Amoxicillin-clavulanate",
               "Correct. Failure of first-line amoxicillin at three days is the trigger to step up, and amoxicillin-clavulanate is that step; a third-generation cephalosporin is the other step-up option listed."],
              ["Continue the same agent for a further three days",
               "Three days without improvement is the stated point at which therapy is considered to have failed, so continuing the same drug is not the response; the step up is amoxicillin-clavulanate."],
              ["Move straight to injected ceftriaxone",
               "Injected ceftriaxone is kept for further failure or for a child who cannot take oral medication; the first step up from failed amoxicillin is amoxicillin-clavulanate."],
              ["Stop antibiotics and observe",
               "Observation is not the response to a treatment failure; failure at three days is the point at which therapy is stepped up to amoxicillin-clavulanate rather than withdrawn."]],
        c=0),
    "en:inflam2:2": dict(
        q="Which statement describes how aspirin inhibits cyclooxygenase in platelets?",
        opts=[["Irreversibly, so the platelet never recovers",
               "Correct. A platelet has no nucleus and cannot make fresh enzyme, so one exposure disables it for its lifetime; ibuprofen binds reversibly, which is why its effect fades within about a day."],
              ["Reversibly, so the effect ends as the drug is cleared",
               "That describes ibuprofen. Aspirin binds irreversibly, so a platelet exposed to it never recovers the enzyme and the effect lasts until new platelets are made."],
              ["Selectively at cyclooxygenase-2 only",
               "Aspirin is non-selective between the two isoforms, and hitting cyclooxygenase-1 as well is where its gastric and bleeding effects come from."],
              ["Indirectly, by reducing prostaglandin release from storage",
               "Prostaglandins are made on demand rather than stored, and aspirin acts on the enzyme itself, irreversibly in platelets, rather than on any store."]],
        c=0),
    "li:statin2:5": dict(
        q="Which patient falls into one of the four major statin benefit groups?",
        opts=[["A 55-year-old after a myocardial infarction",
               "Correct. Clinical atherosclerotic cardiovascular disease is the first benefit group; the others are LDL (low-density lipoprotein) above 190 mg/dL, diabetes at 40 to 75 with LDL 70 to 189, and high estimated risk."],
              ["A 35-year-old with diabetes and LDL of 120",
               "The diabetes group covers ages 40 to 75 with LDL (low-density lipoprotein) 70 to 189 mg/dL; at 35 this patient falls outside it."],
              ["A 50-year-old with LDL of 150 and 3% risk",
               "Without disease, diabetes or LDL above 190 mg/dL, a statin group needs a high estimated 10-year risk; 3% is low."],
              ["A 30-year-old with LDL of 160 and no other findings",
               "Under 40, with no disease, no diabetes and LDL below 190 mg/dL, this patient fits none of the four benefit groups; the groups are disease, LDL above 190, diabetes at 40 to 75, and high estimated risk."]],
        c=0, keep_same_stem=True),
}
TOPIC_OVERRIDE = {"mv:set1:1": "Antianginals after a myocardial infarction", "en:inflam2:2": "Aspirin and cyclooxygenase",
                  "en:inflam1:4": "Salicylates and Reye syndrome"}
# explanation-only edits for keys (do not change the question's identity or guide link)
EXPL_OVERRIDE.update({
    ("en:inflam2:10", "Renal function"):
        "Correct. Two interactions at once: ibuprofen with a diuretic puts the kidney at risk, and ibuprofen blunts the ACE inhibitor, so the blood pressure response also needs watching.",
    ("en:inflam2:10", "Serum potassium only"):
        "Potassium can rise with this pair, but watching it alone misses the kidney risk and the blunted blood pressure response; renal function is what needs watching.",
    ("en:inflam1:4", "It causes irreversible hearing loss in children"):
        "Salicylate ear effects such as tinnitus are exposure-related and not the basis of this restriction; the restriction exists because aspirin in a child with a viral illness risks Reye syndrome.",
    ("mv:set1:14", "A beta blocker"):
        "It lowers heart rate and oxygen demand and does not affect bleeding risk; the class to avoid with an active bleed is the fibrinolytic.",
    ("mv:set1:14", "A nitrate"):
        "It dilates vessels and does not impair hemostasis, so bleeding does not forbid it; the class to avoid with an active bleed is the fibrinolytic.",
    ("mv:set1:14", "An opioid analgesic"):
        "It does not interfere with clotting, and bleeding is not a contraindication to it; the class to avoid with an active bleed is the fibrinolytic.",
    ("e2:set2:12", "Systemically they act on alpha-2"):
        "Correct. Local alpha-1 against systemic alpha-2 is why an ingestion behaves differently from an instillation: a small child can develop a slow heart rate, low blood pressure and central nervous system depression.",
    ("li:statin1:9", "A patient who is pregnant"):
        "Correct. Hepatic disease and pregnancy are the statin contraindications. The course teaches avoiding statins in pregnancy; the US Food and Drug Administration relaxed the formal contraindication in 2021, but statins are still stopped in most pregnancies.",
})

def load_pool():
    pool = {}
    for key, f in FILES.items():
        d = json.load(open(os.path.join(HERE, f), encoding="utf-8"))
        for s in sorted(d):
            for i, q in enumerate(d[s]):
                pool["%s:%s:%d" % (key, s, i)] = dict(q, lec=LEC_OF[key], ref="%s:%s:%d" % (key, s, i))
    return pool


# ----- scoring (screening aid; see the module docstring) ------------------------------------------------------
KIND_W = {"emphasis": 1.0, "marker": 1.4, "shape": 1.3, "rule": 1.1, "scope": -1.0}
STRONG = re.compile(r"(?i)will ask|test question|on the test|star|highlight|underline|know (this|that|it)|"
                    r"important|critical|really|big thing|cornucopia|exceptions|delineate")
SLOT_W = {"education": 1.0, "contraindication": 1.0, "adverse effect": 0.9, "interaction": 0.9, "indication": 0.9,
          "drug choice": 0.9, "first-line": 1.0, "agent/regimen": 0.9, "avoid": 1.0, "complication": 0.9,
          "class": 0.7, "next step": 0.8, "protocol": 0.6, "monitoring": 0.6, "diagnosis": 0.4, "mechanism": 0.2,
          "physiology": 0.1, "escalation": 0.9, "referral": 0.8, "initial test": 0.6, "test finding": 0.4,
          "risk factor": 0.5, "risk factors": 0.5}


def plain(s):
    return H.unescape(re.sub(r"<[^>]+>", " ", s))


def wood_entries():
    return json.load(open(os.path.join(HERE, "pharm_e2", "wood.json"), encoding="utf-8"))["entries"]


def kcz_text():
    out = []
    for lec in ("L4", "L5", "L6", "L7", "L8"):
        d = json.load(open(os.path.join(HERE, "pharm_e2", lec + ".json"), encoding="utf-8"))
        for k in d.get("kcz", {}).get("killers", []):
            out.append((lec, set(B.toks(plain(k.get("effect", "") + " " + k.get("what", ""))))))
        for c in d.get("contra", []):
            if c.get("tier") == "ABS":
                out.append((lec, set(B.toks(plain(c.get("text", ""))))))
    return out


def score_all(pool):
    wood = wood_entries()
    wsets = []
    for n, e in enumerate(wood):
        t = set(B.toks(plain(e["topic"] + " " + e["quote"] + " " + e["body"])))
        k = KIND_W.get(e["kind"], 1.0) * (1.25 if STRONG.search(plain(e["quote"])) else 1.0)
        wsets.append((n, e["lec"], t, k))
    kcz = kcz_text()
    GL = json.load(open(os.path.join(FOLDER, "guide-links.json"), encoding="utf-8"))["l"]
    scored = []
    for ref, q in pool.items():
        stem = set(B.toks(plain(q["q"] + " " + q["opts"][q["c"]][0])))
        key = set(B.toks(plain(q["opts"][q["c"]][0] + " " + q["opts"][q["c"]][1])))
        core = stem | key
        if not core:
            continue
        best = []
        for n, wl, t, k in wsets:
            ov = len(core & t) / max(8, min(len(core), 14))
            best.append((ov * k, n))
        best.sort(reverse=True)
        w1 = best[0][0]
        killer = max((len(core & t) / max(6, min(len(core), 12)) for lec, t in kcz if lec == q["lec"]), default=0)
        link = GL.get(B.qkey(q))
        star = 1.0 if link and "★" in link[3] else 0.0
        s = (3.0 * w1 + 1.0 * killer + 0.8 * star) * (0.5 + SLOT_W.get(q["slot"], 0.6))
        dose = bool(DOSE_KEY.search(plain(q["opts"][q["c"]][0])))
        scored.append(dict(ref=ref, lec=q["lec"], score=round(s, 3), wood=best[0][1], wood_overlap=round(w1, 3),
                           killer=round(killer, 3), star=star, slot=q["slot"], dose=dose, q=plain(q["q"])[:110]))
    return scored


def deal_positions(qs, rng):
    """Exactly ten of each letter, two per letter inside each block of eight, no run longer than two."""
    for _ in range(20000):
        pos = []
        for _blk in range(len(qs) // 8):
            blk = [0, 0, 1, 1, 2, 2, 3, 3]
            rng.shuffle(blk)
            pos += blk
        run = 1
        ok = True
        for a, b in zip(pos, pos[1:]):
            run = run + 1 if a == b else 1
            if run > 2:
                ok = False
                break
        if ok and all(c == len(pos) // 4 for c in Counter(pos).values()):
            return pos
    raise SystemExit("could not deal positions")


def main():
    pool = load_pool()
    pool.update({k: dict(v, lec="L5", ref=k) for k, v in NEW_QUESTIONS.items()})
    scored = score_all({k: v for k, v in pool.items() if not k.startswith("NEW:")})
    rank = {}
    for lec in sorted(LEC_NAME):
        rows = sorted((r for r in scored if r["lec"] == lec and not r["dose"]), key=lambda r: -r["score"])
        for i, r in enumerate(rows, 1):
            rank[r["ref"]] = (i, len(rows))
    # ----- validate the picks -----
    refs = [p["ref"] for p in PICKS]
    assert len(refs) == len(set(refs)) == 40, "need 40 distinct picks, got %d" % len(refs)
    per = Counter(p["lec"] for p in PICKS)
    assert dict(per) == {l: 8 for l in LEC_NAME}, per
    stems = set()
    for p in PICKS:
        q = pool[p["ref"]]
        assert q["lec"] == p["lec"] or p["ref"].startswith("NEW:"), p["ref"]
        assert len(q["opts"]) == 4 and q["opts"][q["c"]][1].startswith("Correct"), p["ref"]
        # laboratory values (600 mg/dL) are not doses
        lab = lambda t: re.sub(r"mg/(dL|g)", "", plain(t))
        assert not DOSE_KEY.search(lab(q["opts"][q["c"]][0])), "dosage in the key of %s" % p["ref"]
        if DOSE_KEY.search(lab(q["q"])):      # the word 'dose' in a stem that asks what to DO, not how much
            print("  note: stem mentions a dose word, key does not (read it): %s | %s" % (p["ref"], plain(q["q"])[:90]))
        assert q["q"] not in stems
        stems.add(q["q"])
    # ----- deal positions, keep lecture order (L4..L8), then write -----
    rng = random.Random(SEED)
    ordered = []
    for p in PICKS:
        q = dict(pool[p["ref"]])
        if p["ref"] in REPLACE:
            r = REPLACE[p["ref"]]
            q["q"], q["opts"], q["c"] = r["q"], r["opts"], r["c"]
        if p["ref"] in TOPIC_OVERRIDE:
            q["topic"] = TOPIC_OVERRIDE[p["ref"]]
        q["opts"] = [[t, EXPL_OVERRIDE.get((p["ref"], t), e)] for t, e in q["opts"]]
        ordered.append(q)
    for p, q in zip(PICKS, ordered):
        for o in q["opts"]:
            assert len(o[1]) >= 60, (p["ref"], o[1])
        used = {t for t, _e in q["opts"]}
        assert all(k[1] in used for k in EXPL_OVERRIDE if k[0] == p["ref"]), p["ref"]
    pos = deal_positions(ordered, rng)
    out = []
    for p, q, want in zip(PICKS, ordered, pos):
        o = list(q["opts"])
        key = o.pop(q["c"])
        o.insert(want, key)
        r = {k: q[k] for k in ("topic", "q", "cite")}
        r["io"] = "Topic — " + LEC_NAME[p["lec"]]
        r["opts"] = o
        r["c"] = want
        out.append(r)
    rep = {
        "counts_per_lecture": dict(per),
        "reused": sum(1 for p in PICKS if not p["ref"].startswith("NEW:")),
        "new": sum(1 for p in PICKS if p["ref"].startswith("NEW:")),
        "positions": {chr(65 + k): v for k, v in sorted(Counter(pos).items())},
        "shapes": dict(Counter(p["shape"].split(" / ")[0].split(" vignette")[0] for p in PICKS)),
        "picks": [dict(p, rank_in_lecture=rank.get(p["ref"]), question=plain(pool[p["ref"]]["q"])) for p in PICKS],
        "top_unpicked": {},
        "score_note": "score = (3 x Wood-entry overlap + killer/absolute-contraindication overlap + guide star) x "
                      "(0.5 + McInnis slot weight); a screening aid, final picks are by hand (module docstring)",
    }
    for lec in sorted(LEC_NAME):
        rows = sorted((r for r in scored if r["lec"] == lec and not r["dose"]), key=lambda r: -r["score"])
        rep["top_unpicked"][lec] = [dict(ref=r["ref"], score=r["score"], q=r["q"]) for r in rows[:25]
                                    if r["ref"] not in refs][:12]
    json.dump({"set1": out}, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(rep, open(REPORT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote %s (%d questions) and %s" % (os.path.basename(OUT), len(out), os.path.basename(REPORT)))
    print("per lecture %s  reused %d  new %d  positions %s" % (rep["counts_per_lecture"], rep["reused"], rep["new"],
                                                              rep["positions"]))
    for p in PICKS:
        r = rank.get(p["ref"])
        print("  %-14s %s rank %s  %s" % (p["ref"], p["lec"], "%d/%d" % r if r else "new", p["shape"]))


if __name__ == "__main__":
    main()
