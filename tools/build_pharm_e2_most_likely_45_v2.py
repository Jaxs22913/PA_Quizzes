#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build 'Pharmacology I Exam 2: Most Likely 45 (Version 2)' (Jaxon, 2026-10-03: "Create a second most likely 45 Q quiz").

SAME METHOD AS VERSION 1 (tools/build_pharm_e2_most_likely_45.py has the full statement): rank the shipped, vetted
Exam 2 questions by Wood's recorded emphasis, the guide's stars, the killer/contraindication lists, McInnis' weighting
and the course's question shapes, then pick nine per lecture by hand. Version 2 is the NEXT-most-likely set.

NO OVERLAP WITH VERSION 1, by rule (Jaxon's clarification: "Only ask again if he said it will def be on the exam"):
  * no question appears in both versions (checked on pool reference AND on stem text);
  * no FACT is asked again, EXCEPT a fact the lecturer promised outright. 'Definitely' is defined here as a first-person
    statement that this specific fact WILL be on the exam: "I will ask this question", "it'll be somewhere on the test".
    Conditionals do not count ("I might say", "if I asked", "a test question could come from", "I want you to know",
    "definitely" used about a fact rather than about the exam). Read against all 116 entries and a phrase search of the
    four recordings (will ask / will be on the test / definitely be / guarantee / show up on the test), exactly TWO
    entries qualify (DEFINITE below). Both are re-asked in Version 2 from a different angle, as a different question.
  * Version 1's other facts are deliberately avoided (SELECTION_REPORT lists the 45 V1 facts and how V2 steered round
    them; the nearest neighbours are noted).

    python3 tools/build_pharm_e2_most_likely_45_v2.py   # writes tools/pharm_e2_most_likely_45_v2_sets.json,
                                                        # ..._v2_report.json and the combined selection report
    python3 tools/render_pharm_e2_most_likely_45_v2.py
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_pharm_e2_most_likely_45 as V1   # same loader, scorer, position dealer and rules

OUT = os.path.join(HERE, "pharm_e2_most_likely_45_v2_sets.json")
REPORT = os.path.join(HERE, "pharm_e2_most_likely_45_v2_report.json")
COMBINED = os.path.join(HERE, "pharm_e2_most_likely_selection_report.json")
SEED = 20261004

# wood.json entry numbers (0-based) whose quote is a definite promise that the fact will be on the exam
DEFINITE = {
    5: "L4 50:24 'I will tell you, I will ask this question ... rebound hyperemia ... no more than two weeks' (and 'I tell you explicitly')",
    28: "L5 1:21:24 Afrin: 'I'm telling you right now, it'll be somewhere on the test' (rebound congestion, three to five days)",
}
NOT_DEFINITE_NOTE = ("hypothetical or conditional: 'I might give you a vignette' (26), 'if I told you ... nightmares' (84), "
                     "'test question I might ask' (57), 'you can say, the triglyceride is 600' (60), 'if I say a test question' (91), "
                     "'cornucopia of test questions could come from' (96), 'I'll make it pretty clear cut in the question' after "
                     "'I might say' (66), 'I want to be asking questions ... more like' (52); emphasis only: 'really important', "
                     "'know this', 'star it', 'definitely one thing to note' (54)")

PICKS = [
    # ---- Lecture 4 ----
    dict(ref="e2:set1:3", lec="L4", shape="recognise the effect (definite-promise fact, new angle)", wood=[5], redo_v1=True,
         why="Rebound hyperemia, asked as 'what has happened' after a month of daily redness-relief drops. Version 1 asks the "
             "two-week limit; he promised this fact outright, so Version 2 asks it from the other side."),
    dict(ref="e2:set2:6", lec="L4", shape="patient education", wood=[10],
         why="Prostaglandin analogs: longer lashes and iris color change (ladder body: no more than once daily, cosmetic changes)."),
    dict(ref="e2:set2:10", lec="L4", shape="contraindication", wood=[10],
         why="Alpha-2 agonists are contraindicated under two years (apnea): the one age-based class ban in the glaucoma ladder."),
    dict(ref="e2:set2:14", lec="L4", shape="patient education", wood=[13],
         why="Carbonic anhydrase inhibitors: bitter taste and stinging are the adherence problem and the reason they are add-ons."),
    dict(ref="op:inflam2:5", lec="L4", shape="patient education", wood=[70],
         why="'First step, most important step: wash your hands.'"),
    dict(ref="e2:set1:14", lec="L4", shape="drug choice", wood=[4],
         why="Natamycin is the only commercially available ophthalmic antifungal (he said not to memorize the organisms; the drug is the point)."),
    dict(ref="e2:set1:6", lec="L4", shape="adverse effect", wood=[1],
         why="Aminoglycoside drops (tobramycin, gentamicin) are one of the two antibiotic exceptions he named: corneal ulceration."),
    dict(ref="e2:set1:1", lec="L4", shape="drug choice", wood=[0],
         why="Erythromycin ointment: 'the most common ophthalmic antibiotic, dirt cheap'; newborn prophylaxis is its named use."),
    dict(ref="op:glauc2:8", lec="L4", shape="side effect", wood=[10],
         why="Cholinergic agonists are the last-line class; young patients cannot tolerate the blurring (ladder, last rung)."),
    # ---- Lecture 5 ----
    dict(ref="en:cough1:11", lec="L5", shape="patient education (definite-promise fact, new angle)", wood=[28], redo_v1=True,
         why="Topical nasal decongestant: do not use beyond a few days. Version 1 asks 'what has happened' after three weeks; "
             "he promised this fact outright, so Version 2 asks the instruction itself."),
    dict(ref="en:hist1:15", lec="L5", shape="interaction / anticipate", wood=[27],
         why="Systemic steroids raise blood sugar and blunt antidiabetic drugs (side-effect list he walked through)."),
    dict(ref="en:cough1:16", lec="L5", shape="patient education", wood=[71],
         why="Benzonatate: swallow whole, the do-not-chew-or-crush list."),
    dict(ref="en:anti2:16", lec="L5", shape="allergy backup", wood=[15],
         why="'First line's not good because the patient has an allergy, what do you use as a backup?' Ear infection with penicillin allergy."),
    dict(ref="en:hist1:5", lec="L5", shape="monitoring / interaction", wood=[31],
         why="Diuretic plus dexamethasone: potassium ('anything that affects your potassium ... a very easy test question')."),
    dict(ref="en:hist1:17", lec="L5", shape="patient education", wood=[27],
         why="Systemic steroids: 'no cold turkey, have them slowly taper off' after about a week."),
    dict(ref="en:cough1:13", lec="L5", shape="contraindication", wood=[19],
         why="Dextromethorphan with a monoamine oxidase inhibitor: interaction rule ('easy to ask ... significant drug interactions')."),
    dict(ref="en:anti2:12", lec="L5", shape="first-line drug choice", wood=[15],
         why="Bacterial sinusitis standard of care (amoxicillin-clavulanate), the 'first line' stem for the third infection."),
    dict(ref="en:inflam1:8", lec="L5", shape="contraindication", wood=[24],
         why="Who should avoid ibuprofen (asthma, prior ulcer, renal impairment): the nonsteroidal anti-inflammatory risk list."),
    # ---- Lecture 6 ----
    dict(ref="ht:beta1:7", lec="L6", shape="drug choice", wood=[46],
         why="'Just know these three': carvedilol, metoprolol succinate, bisoprolol for heart failure."),
    dict(ref="ht:raas1:9", lec="L6", shape="adverse effect", wood=[32],
         why="ACE inhibitors can drop kidney function acutely when flow depends on angiotensin II (and protect long term)."),
    dict(ref="ht:raas2:5", lec="L6", shape="contraindication", wood=[33, 55],
         why="ACE inhibitors and receptor blockers in pregnancy (fetal toxicity); not a substitute for each other."),
    dict(ref="ht:other2:12", lec="L6", shape="adverse effect / antidote", wood=[75],
         why="Nitroprusside is given with sodium thiosulfate to limit cyanide toxicity."),
    dict(ref="ht:other2:7", lec="L6", shape="adverse effect", wood=[49],
         why="Alpha-1 blockers (the -zosins): orthostatic hypotension."),
    dict(ref="ht:ccb2:15", lec="L6", shape="contraindication", wood=[38, 39],
         why="Non-dihydropyridines (diltiazem, verapamil) act on the heart, so advanced heart block is a contraindication."),
    dict(ref="ht:beta2:7", lec="L6", shape="class discrimination", wood=[44, 80],
         why="'If it starts with an N through Z it's likely non-selective; A through M cardioselective': nadolol is non-selective."),
    dict(ref="ht:beta1:12", lec="L6", shape="patient education", wood=[43, 47],
         why="Beta blockers in diabetes: they prolong hypoglycemia and mask its warning signs (the beta blocker adverse-effect list)."),
    dict(ref="ht:other1:14", lec="L6", shape="drug choice", wood=[49],
         why="Terazosin and doxazosin treat hypertension and benign prostatic hyperplasia."),
    # ---- Lecture 7 ----
    dict(ref="li:tg2:13", lec="L7", shape="class discrimination", wood=[61],
         why="'If you ever see niacinamide, that's not the same thing': nicotinic acid is the antilipemic."),
    dict(ref="li:statin1:4", lec="L7", shape="indication / guideline", wood=[56],
         why="No LDL target: 'it's not really the number that matters', the risk group and statin intensity do."),
    dict(ref="li:statin2:0", lec="L7", shape="class discrimination", wood=[65],
         why="'Can you identify what falls into the category of high': atorvastatin and rosuvastatin only."),
    dict(ref="li:ldl2:13", lec="L7", shape="class discrimination", wood=[67],
         why="When a statin is not the answer: the PCSK9 inhibitors are injected monoclonal antibodies."),
    dict(ref="li:statin2:1", lec="L7", shape="adverse effect / management", wood=[54],
         why="Statin muscle toxicity: myalgia, creatine kinase, stop the statin ('definitely one thing to note')."),
    dict(ref="li:tg2:5", lec="L7", shape="interaction", wood=[58],
         why="Fibrates increase the effect of warfarin (watch for bruising and bleeding)."),
    dict(ref="li:tg1:9", lec="L7", shape="contraindication", wood=[63],
         why="Niacin: chronic liver disease is the absolute contraindication (gout, diabetes, ulcer relative)."),
    dict(ref="li:ldl1:12", lec="L7", shape="indication", wood=[59],
         why="Bile acid resins are not absorbed, so they are the safest class and approved in children and pregnancy."),
    dict(ref="li:tg1:0", lec="L7", shape="contraindication", wood=[62, 64],
         why="Fibrates: existing gallbladder disease contraindicates them (cholelithiasis is also their adverse effect)."),
    # ---- Lecture 8 ----
    dict(ref="mv:set1:23", lec="L8", shape="allergy backup", wood=[103],
         why="Aspirin first in acute coronary syndrome; clopidogrel if the patient is allergic."),
    dict(ref="mv:set1:7", lec="L8", shape="class discrimination", wood=[104],
         why="'Nitrates only help with symptom relief ... they don't do anything for outcomes.'"),
    dict(ref="mv:set1:15", lec="L8", shape="drug choice", wood=[106],
         why="Morphine for pain unresponsive to nitrates: pain only, no outcome benefit."),
    dict(ref="mv:set1:3", lec="L8", shape="drug choice", wood=[98],
         why="ACE inhibitors do not treat angina; they slow progression (post-infarction, ventricular dysfunction, diabetes)."),
    dict(ref="mv:set2:13", lec="L8", shape="contraindication", wood=[115],
         why="Non-ST-elevation: 'same drugs, fewer fibrinolytics'."),
    dict(ref="mv:set2:2", lec="L8", shape="contraindication", wood=[87],
         why="'Typically we avoid short-acting agents like nifedipine': prefer long-acting amlodipine."),
    dict(ref="mv:set1:8", lec="L8", shape="patient education", wood=[93],
         why="Nitroglycerin tablets: original container, replace every three to six months (course rule; explanation notes current labeling)."),
    dict(ref="mv:set2:16", lec="L8", shape="patient education", wood=[92],
         why="'After five minutes if you don't get the relief, call 911': the action is the testable point."),
    dict(ref="ms:anginal2:25", lec="L8", shape="drug choice", wood=[86],
         why="Left ventricular dysfunction: dihydropyridine only (amlodipine)."),
]

EXPL_OVERRIDE = {
    ("e2:set2:6", "Drooping of the eyelid"):
        "Eyelid drooping is not among the effects listed for the prostaglandin analogs; the effects to warn about are longer lashes, iris color change and conjunctival hyperemia.",
    ("e2:set2:10", "Carbonic anhydrase inhibitors"):
        "Carbonic anhydrase inhibitors cause bitter taste and stinging rather than apnea and have no stated age ban; the class contraindicated under two years is the alpha-2 agonists.",
    ("e2:set2:10", "Cholinergic agonists"):
        "Cholinergic agonists cause miosis and blurred vision rather than apnea and have no stated age ban; the class contraindicated under two years is the alpha-2 agonists.",
    ("e2:set2:14", "This means the drop is contaminated"):
        "A bitter taste and stinging are known, expected effects of dorzolamide rather than signs of contamination; warning patients in advance improves adherence.",
    ("e2:set2:14", "This indicates systemic absorption and cardiac risk"):
        "Cardiac risk belongs to the beta blocker drops; taste and stinging are the expected local effects of a carbonic anhydrase inhibitor and do not signal cardiac harm.",
    ("e2:set1:14", "Trifluridine"):
        "Trifluridine is an antiviral for herpes simplex keratitis and has no antifungal action; natamycin is the commercially available ophthalmic antifungal.",
    ("e2:set1:6", "Rebound hyperemia"):
        "Rebound hyperemia follows stopping an alpha-agonist redness-relief drop; an antibiotic that leaves a corneal defect points to corneal ulceration from an aminoglycoside.",
    ("en:cough1:16", "It releases local anesthetic into the mouth"):
        "Correct. Benzonatate is a local anesthetic, so chewing the capsule releases it in the mouth and throat, numbing the airway a patient needs to protect, and the drug then does not treat the cough.",
    ("en:cough1:13", "One taking a monoamine oxidase inhibitor"):
        "Correct. The restriction runs for two weeks after stopping a monoamine oxidase inhibitor, which is the part most easily missed because the patient has already stopped the drug.",
    ("en:inflam1:8", "Those with asthma it may worsen"):
        "Correct. Asthma is the one most easily forgotten because it is not an obvious consequence of blocking prostaglandin synthesis; previous ulcer or perforation and renal impairment are the other contraindications.",
    ("en:hist1:17", "Stopping suddenly produces rebound symptoms"):
        "Correct. After more than about a week of use, stopping suddenly produces rebound symptoms, so the drug is tapered instead; a short course and a long course are stopped differently.",
    ("e2:set1:1", "Azithromycin solution"):
        "Azithromycin solution is used for conjunctivitis and is considerably more expensive; the inexpensive named agent for newborn prophylaxis is erythromycin ointment.",
    ("e2:set1:1", "Moxifloxacin solution"):
        "Moxifloxacin is a fluoroquinolone kept for conjunctivitis and corneal ulcers, not newborn prophylaxis; erythromycin ointment is the named agent.",
    ("e2:set1:1", "Natamycin suspension"):
        "Natamycin is an antifungal and has no role in preventing neonatal bacterial conjunctivitis; erythromycin ointment is the named agent.",
}
TOPIC_OVERRIDE = {"mv:set1:23": "Aspirin allergy and antiplatelet therapy", "mv:set1:3": "ACE inhibitors in coronary disease"}
V1_FACTS_AVOIDED_NEIGHBOURS = {
    "L4": "V1 has betaxolol for asthma, soft steroids, prostaglandin first line, add a second agent, sulfacetamide, contact-lens fluoroquinolone, anesthetic drops, toddler ingestion, rebound limit. V2 skips the beta blocker drop's systemic effects (the reason behind V1's betaxolol item), the steroid raised-pressure concern and the steroid-course-length item (a duration key and a uveitis case where practice differs).",
    "L5": "V1 has Afrin rebound, polymyxin B, truck driver, ketoconazole QT, Reye, ear infection failure step, aspirin irreversible, NSAID kidney, acetaminophen with alcohol. V2 skips aspirin plus anticoagulant (same platelet fact as V1), first-generation sedation with alcohol (same teaching as V1's truck driver) and the ear infection first-line item (its key is a dose).",
    "L6": "V1 has T2DM start, cough to receptor blocker, add a thiazide, potassium with ACE inhibitors, AF rate control, beta blocker withdrawal, constipation, carvedilol, hydralazine acetylators. V2 skips angioedema (same bradykinin teaching as V1's cough), clonidine rebound (V1's withdrawal theme), propranolol nightmares and lipid solubility (Wood ties them to V1's nightmares switch), tacrolimus with diltiazem (same CYP3A4 teaching as V1's verapamil and statin), NSAIDs blunting ACE inhibitors (V1 L5) and the start-two-drugs item.",
    "L7": "V1 has triglyceride 600, triglycerides over 1000, verapamil and statins, niacin flush, statin plus fibrate, resin timing, benefit groups, statin pregnancy, niacin and fibrate versus resins. V2 skips grapefruit and simvastatin (V1's CYP3A4 point), the statins-lower-LDL-most comparison and resin warfarin.",
    "L8": "V1 has nightmares switch, tadalafil, quick relief, add felodipine, variant angina, beta blocker plus verapamil, prior infarction, fibrinolytic bleeding contraindication, nitrate-free interval. V2 skips asthma to diltiazem (same switch logic as V1), verapamil and simvastatin, fibrinolytic intracranial hemorrhage (same bleeding teaching as V1's contraindication) and aspirin first chewed (kept to the clopidogrel allergy item). The five-minute call is in V2 only.",
}


def main():
    pool = V1.load_pool()
    v1refs = {p["ref"] for p in V1.PICKS}
    refs = [p["ref"] for p in PICKS]
    assert len(refs) == len(set(refs)) == 45
    assert not (set(refs) & v1refs), set(refs) & v1refs
    assert dict(Counter(p["lec"] for p in PICKS)) == {l: 9 for l in V1.LEC_NAME}
    v1stems = {V1.plain(pool[r]["q"]) for r in v1refs if r in pool} | {V1.plain(v["q"]) for v in V1.REPLACE.values()} \
        | {V1.plain(v["q"]) for v in V1.NEW_QUESTIONS.values()}
    ordered, seen = [], set()
    for p in PICKS:
        q = dict(pool[p["ref"]])
        assert q["lec"] == p["lec"], p["ref"]
        stem = V1.plain(q["q"])
        assert stem not in v1stems and stem not in seen, "stem repeated: " + stem
        seen.add(stem)
        q["opts"] = [[t, EXPL_OVERRIDE.get((p["ref"], t), e)] for t, e in q["opts"]]
        if p["ref"] in TOPIC_OVERRIDE:
            q["topic"] = TOPIC_OVERRIDE[p["ref"]]
        used = {t for t, _ in q["opts"]}
        assert all(k[1] in used for k in EXPL_OVERRIDE if k[0] == p["ref"]), p["ref"]
        key = q["opts"][q["c"]]
        assert len(q["opts"]) == 4 and key[1].startswith("Correct"), p["ref"]
        assert not V1.DOSE_KEY.search(re.sub(r"mg/(dL|g)", "", V1.plain(key[0]))), "dose in key " + p["ref"]
        for o in q["opts"]:
            assert len(o[1]) >= 60, (p["ref"], o[1])
        ordered.append(q)
    pos = V1.deal_positions(ordered, random.Random(SEED))
    out = []
    for p, q, want in zip(PICKS, ordered, pos):
        o = list(q["opts"]); k = o.pop(q["c"]); o.insert(want, k)
        r = {x: q[x] for x in ("topic", "q", "cite")}
        r["io"] = "Topic — " + V1.LEC_NAME[p["lec"]]
        r["opts"] = o; r["c"] = want
        out.append(r)
    scored = V1.score_all({k: v for k, v in pool.items()})
    rank = {}
    for lec in V1.LEC_NAME:
        rows = sorted((r for r in scored if r["lec"] == lec and not r["dose"]), key=lambda r: -r["score"])
        for i, r in enumerate(rows, 1):
            rank[r["ref"]] = i
    v1rep = json.load(open(os.path.join(HERE, "pharm_e2_most_likely_45_report.json"), encoding="utf-8"))
    v2 = {
        "counts_per_lecture": {l: 9 for l in V1.LEC_NAME},
        "reused": 45, "new": 0,
        "positions": {chr(65 + k): v for k, v in sorted(Counter(pos).items())},
        "picks": [dict(p, rank_in_lecture=rank.get(p["ref"]), question=V1.plain(pool[p["ref"]]["q"])) for p in PICKS],
    }
    combined = {
        "definite_promise_definition": "a first-person statement that this specific fact WILL be on the exam ('I will ask this question', "
                                       "'it'll be somewhere on the test'); conditionals and emphasis-only phrases do not count",
        "definite_promise_entries": DEFINITE,
        "reasked_in_v2": [p["ref"] for p in PICKS if p.get("redo_v1")],
        "not_definite_examples": NOT_DEFINITE_NOTE,
        "v1_facts_avoided_neighbours": V1_FACTS_AVOIDED_NEIGHBOURS,
        "overlap_questions_v1_v2": sorted(set(refs) & v1refs),
        "v1": v1rep, "v2": v2,
    }
    json.dump({"set1": out}, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(v2, open(REPORT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(combined, open(COMBINED, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", os.path.basename(OUT), len(out), "questions; positions", v2["positions"])
    for p in PICKS:
        print("  %-14s %s rank %s %s" % (p["ref"], p["lec"], rank.get(p["ref"]), p["shape"]))


if __name__ == "__main__":
    main()
