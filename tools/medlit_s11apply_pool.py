# -*- coding: utf-8 -*-
# Interpretation of Medical Literature -- "Reading a Study". An APPLICATION quiz
# for syllabus units 12 (Journal Article Analysis) and 13 (PICO Questions and
# Answers), which have objectives but no decks: Jaxon (2026-10-27) said those
# units are about "understanding how to do those things, not necessarily the
# content of them". So every item gives a short INVENTED study description and
# asks the student to do one thing with it, using a concept taught in sessions
# 1-4 and 7-10 (syllabus units 1-11):
#   design   name the design, or say why one design fits the question
#   bias     spot the bias or threat to validity
#   measure  pick or interpret the measure (numbers supplied for calculations)
#   stats    read a p value or confidence interval, error types, causation criteria
#   pico     name the PICO element, or pick the best-formed question
#   trial    validity, blinding, randomization, efficacy/effectiveness, grades
#   article  the parts of an article, only as far as session 10 slides 38-41 go
#
# GROUNDING. The study scenarios are invented; the CONCEPT applied, and every
# fact an explanation uses, is on a visible slide, and each item cites every
# slide its explanations draw on (several decks are joined with "; "). Speaker
# notes are not used. Slides win on conflict.
#
# HELD (not written) because the slides do not teach them: intention-to-treat
# analysis (only the textbook-derived guide text mentions it); reading a
# confidence interval around a DIFFERENCE (crossing 0) -- the slides show only
# ratio intervals (Statistics slide 15) and the null value 1 (Risk slide 20);
# statistical power (Statistics slide 16 is a title with no content); the number
# needed to treat as a calculation (the slides define it in words only, so NNT
# items here interpret given values); incidence as a calculation (Rates slide 20
# divides by the whole town while slide 28 says the population at risk holds
# only the susceptible, so only prevalence is calculated).
#
# CALCULATIONS (numbers supplied, as the Tests and Risk decks teach them) were
# checked in Python. Numeric options are written in ASCENDING order and are not
# rotated (WRITER.md rule 8): those items carry their own key index `c`, and so
# do the three items with ordered labels (trial phases, USPSTF grades, GRADE
# grades), which carry fixed=True.
#
# RESERVE. Items with reserve=True are written and checked but not shipped;
# they replace a shipped item of the same skill that fails review (swap the flag,
# so the pool order and the partition stay stable).
#
# KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
# Unless an item is numeric or fixed, the correct answer is written FIRST (c=0)
# and the partition script rotates it.
D1 = "1 PAJ5512 Introduction Bias Validity MBF_2026sc.pptx"
D2E = "2 PAJ5512 Evidence MBF_2026sc.pptx"
D2S = "2 PAJ5512 Study Design and Research Methods MBF_2026sc.pptx"
D3 = "3 PAJ5512 Rates and Measurement MBF_2026sc.pptx"
D4 = "4 PAJ5512 Tests MBF 2026sc.pptx"
D7R = "7 PAJ5512 Risk MBF 2026sc.pptx"
D7P = "7 PAJ5512 Prognosis MBF 2026sc.pptx"
D8P = "8 PAJ5512 Prevention MBF_2026sc.pptx"
D8T = "8 PAJ5512 Research and Trials MBF_2026sc.pptx"
D9 = "9 PAJ5512 Statistics Causation MBF_2026sc.pptx"
D10 = "10 PAJ5512 Clinical Questions and Reviews MBF_2026sc.pptx"


def S(deck, *n):
    return "%s, Slide %d" % (deck, n[0]) if len(n) == 1 else \
        "%s, Slides %s" % (deck, ", ".join(str(x) for x in n))


def C(*parts):
    return "; ".join(parts)


# Syllabus objectives (PAJ 5512 Syllabus 2026, units 12 and 13), verbatim.
IO12A = "Identify components of a journal article"
IO12B = "Interpret information presented in journal articles"
IO12C = "Discuss the relevance of journal articles to clinical practice"
IO13A = "Recall components of a PICO question"
IO13B = "Formulate PICO question"
IO13D = "Evaluate information in selected resources"

TOPIC = {"design": "Study design", "bias": "Bias and validity threats", "measure": "Choosing the measure",
         "stats": "P values and intervals", "pico": "Clinical questions", "trial": "Trial design and validity",
         "article": "Reading an article"}

# Shipped questions per skill (60 in all); the rest of each skill is reserve.
TARGET = {"design": 11, "bias": 11, "measure": 12, "stats": 7, "pico": 6, "trial": 9, "article": 4}


def Q(skill, unit, io, q, key, wrong, cite, reserve=False):
    """key = (text, explanation); wrong = [(text, explanation, misconception), x3]. Key authored at 0."""
    assert len(wrong) == 3, q
    return dict(topic=TOPIC[skill], io=io, skill=skill, unit=unit, slot="application", q=q,
                opts=[[key[0], key[1]]] + [[t, e] for t, e, _ in wrong],
                mis={t: m for t, _, m in wrong}, c=0, cite=cite, reserve=reserve)


def N(skill, unit, io, q, opts, c, cite, fixed=False, reserve=False):
    """Options in their FIXED order (ascending values, or an ordered scale); c = key index.
    opts = [(text, explanation, misconception or None for the key), x4]."""
    assert len(opts) == 4 and opts[c][2] is None, q
    d = dict(topic=TOPIC[skill], io=io, skill=skill, unit=unit,
             slot="calculation" if not fixed else "application", q=q,
             opts=[[t, e] for t, e, _ in opts], mis={t: m for t, _, m in opts if m},
             c=c, cite=cite, numeric=not fixed, fixed=fixed, reserve=reserve)
    return d


POOL = [

# =================================================================== DESIGN
Q("design", 3, IO12B,
  "A county health department mailed one questionnaire to 2,400 randomly chosen adults during a single "
  "month. It asked whether each person currently smoked and whether each currently had a chronic cough, and "
  "both answers came from the same reply. No one was contacted again. Which study design is this?",
  ("Cross-sectional study",
   "Correct, because the data were obtained at a single point in time, with the risk factor (smoking) and the "
   "condition (cough) measured at the same time in each person."),
  [("Prospective cohort study",
    "A prospective cohort assembles groups on the basis of exposure, collects baseline data and follows them "
    "over time, but no one here was followed after the single questionnaire.", "follow-up over time"),
   ("Case-control study",
    "A case-control study first defines groups by outcome (disease or no disease) and then assesses exposure, "
    "but these adults were sampled without regard to whether they had a cough.", "groups defined by outcome"),
   ("Randomized controlled trial",
    "In a randomized controlled trial the investigator randomly assigns subjects to treatment and control "
    "groups, but nothing was assigned here and smoking was only observed.", "experimental design")],
  C(S(D2S, 9, 17, 22, 27, 30))),

Q("design", 3, IO12B,
  "A hospital team identified 120 adults admitted with a first hip fracture and 240 adults of similar age "
  "admitted for planned surgery who had no fracture. Interviewers then asked everyone in both groups about "
  "long-term use of a sleeping medication during the previous five years. Which study design did the team use?",
  ("Case-control study",
   "Correct, because the groups were defined by the outcome (fracture or no fracture) and then assessed for a "
   "difference in past exposure, with the controls drawn from the hospital."),
  [("Retrospective cohort study",
    "A retrospective cohort is defined by exposure from past records and followed forward to the present for "
    "the outcome, whereas these groups were chosen by outcome first.", "looking back means retrospective cohort"),
   ("Prospective cohort study",
    "A prospective cohort is assembled in the present on the basis of exposure and followed forward, whereas "
    "this study started from people who already had the outcome.", "groups defined by exposure"),
   ("Cross-sectional study",
    "A cross-sectional study measures exposure and outcome at the same time in one population, whereas here "
    "fracture cases and controls were selected separately before exposure was asked about.",
    "single point in time")],
  C(S(D2S, 17, 22, 27, 28), S(D7R, 30))),

Q("design", 3, IO12B,
  "In 2015, researchers enrolled 5,000 nurses who did not have diabetes, recorded how many night shifts each "
  "usually worked, and contacted every nurse every two years. In 2025 they compared the number of new diabetes "
  "cases among nurses who regularly worked night shifts with the number among those who did not. Which study "
  "design is this?",
  ("Prospective cohort study",
   "Correct, because the groups were assembled in the present on the basis of exposure (night shifts), baseline "
   "data were collected, and the nurses were followed forward to see who developed diabetes."),
  [("Retrospective cohort study",
    "A retrospective cohort is identified by going back into history and following members to the present, "
    "whereas these nurses were enrolled first and then followed into the future.", "cohort direction reversed"),
   ("Case-control study",
    "A case-control study starts from people who already have the disease and people who do not, whereas no "
    "nurse had diabetes at enrollment and the groups were defined by exposure.", "groups defined by outcome"),
   ("Randomized controlled trial",
    "In a randomized controlled trial the investigator assigns the intervention, whereas the nurses' shift "
    "patterns were observed rather than assigned.", "experimental design")],
  C(S(D2S, 9, 22, 26, 27, 28)), reserve=True),

Q("design", 3, IO12B,
  "Using factory employment records from 1990, investigators identified 800 workers who had handled an "
  "industrial solvent and 800 who had not. They then searched medical records from 1990 up to the present for "
  "new cases of kidney disease in each group. Which study design is this?",
  ("Retrospective cohort study",
   "Correct, because the investigators went back in history to define the groups by exposure and followed the "
   "members forward to the present to find the outcome."),
  [("Prospective cohort study",
    "A prospective cohort is assembled in the present and followed into the future, whereas these workers' "
    "exposures and outcomes had already occurred and were found in records.", "cohort direction reversed"),
   ("Case-control study",
    "A case-control study selects people by outcome (kidney disease or not) and then looks at exposure, whereas "
    "these groups were chosen by solvent exposure.", "past records mean case-control"),
   ("Cross-sectional study",
    "A cross-sectional study measures exposure and outcome at a single point in time, whereas this study "
    "followed each group through more than 30 years of records.", "single point in time")],
  C(S(D2S, 17, 22, 27, 28), S(D7R, 12))),

Q("design", 3, IO12B,
  "Researchers compared each country's yearly sales of sugar-sweetened drinks per person with its rate of "
  "type 2 diabetes across 40 countries, using only national totals. No data on any individual person were "
  "collected. Countries with higher sales had higher diabetes rates. Which study design is this?",
  ("Ecologic study",
   "Correct, because a cross-sectional ecologic study relates the frequency of a characteristic to an outcome "
   "using population-level data, so applying its result to one person risks the ecologic fallacy."),
  [("Meta-analysis",
    "A meta-analysis pools data from multiple studies to produce a single large study, whereas here national "
    "totals were compared rather than the results of separate studies.", "combining many sources means pooling"),
   ("Case-control study",
    "A case-control study compares individuals with and without a disease for exposure, but this study used no "
    "data on any individual person.", "comparing high and low groups"),
   ("Cohort study",
    "A cohort study follows a group of people over time on the basis of exposure, whereas here whole countries "
    "were compared using population totals.", "comparing exposed and unexposed")],
  C(S(D2S, 18, 19, 22, 25, 32))),

Q("design", 3, IO12B,
  "Four hundred adults with knee osteoarthritis were placed by a computer-generated random sequence either in "
  "a supervised exercise program or in usual care. Pain scores were measured in both groups after 12 weeks. What "
  "feature makes this study experimental rather than observational?",
  ("The investigators assigned the intervention",
   "Correct, because in an experimental design the intervention (independent variable) is assigned and "
   "manipulated by the investigator, whereas in an observational design it is only observed."),
  [("The groups were followed forward in time",
    "A cohort is also a group followed over time, and a cohort is observational, so following groups forward "
    "cannot be what makes this study experimental.", "follow-up means experiment"),
   ("Two groups were compared on an outcome",
    "Comparing two or more groups makes a design analytic, and cohort and case-control studies do this too "
    "while remaining observational.", "comparison means experiment"),
   ("Pain was recorded as a numerical score",
    "Numerical, measurable data mark quantitative research, which also includes cohort and case-control "
    "studies, so a score does not make a study experimental.", "numbers mean experiment")],
  C(S(D2S, 6, 8, 9, 25))),

Q("design", 6, IO12B,
  "A team wants to learn whether a medication taken during pregnancy raises the risk of a rare childhood "
  "cancer, diagnosed in about 1 in 50,000 children. Its budget covers a study of a few hundred children, and "
  "an answer is needed within about a year. Which study design best fits these limits?",
  ("Case-control study",
   "Correct, because it starts from children who already have the cancer, so it needs smaller samples and no "
   "waiting for the condition to develop."),
  [("Prospective cohort study",
    "A cohort must enroll a large group, is expensive, and gives results only after many years, and because so "
    "many more subjects are needed than develop the disease, it is poorly suited to rare diseases.",
    "cohort is always stronger"),
   ("Randomized controlled trial",
    "Experimental studies of risk in humans are limited by ethical constraints, so pregnant women cannot be "
    "assigned to a possibly harmful medication.", "trial is always best"),
   ("Cross-sectional study",
    "A cross-sectional study measures exposure and disease at one time and is poor for determining cause and "
    "effect, so it suits developing hypotheses rather than testing this one.", "cheap and quick suits any aim")],
  C(S(D7R, 8, 15, 16, 29), S(D3, 23))),

Q("design", 6, IO12B,
  "A research group wants to measure how often stroke, dementia and hip fracture newly develop in older adults "
  "who do and do not use a common sleep medication. Funding allows the group to follow participants for 15 "
  "years. Which study design fits this aim?",
  ("Prospective cohort study",
   "Correct, because a cohort establishes incidence directly and can assess the relationship between one "
   "exposure and a number of outcomes."),
  [("Case-control study",
    "A case-control study starts from people with one condition and controls without it, and its measure is the "
    "odds ratio, so it does not establish incidence directly.", "case-control measures incidence"),
   ("Cross-sectional study",
    "A cross-sectional study is a snapshot of who has a condition at one point in time, which gives prevalence "
    "rather than how often new cases arise.", "snapshot gives new cases"),
   ("Case series",
    "A case series is descriptive, describing the characteristics of one group of people, so it offers no "
    "comparison of users with nonusers.", "description is enough")],
  C(S(D7R, 14, 16, 30, 35), S(D3, 15, 22), S(D2S, 8))),

Q("design", 11, IO12B,
  "An experienced cardiologist writes an overview of heart failure care, covering diagnosis, drugs, devices and "
  "end-of-life planning. She cites the trials she considers most useful, and the article describes no search "
  "method or rules for choosing studies. Which kind of article is this?",
  ("Narrative review",
   "Correct, because it is an expert summary of evidence covering a broad topic and a range of issues, and its "
   "unstructured choice of cited articles is a recognized disadvantage."),
  [("Systematic review",
    "A systematic review answers a specific, predetermined question with explicit criteria for selecting "
    "studies, and this broad overview has neither.", "any review of trials is systematic"),
   ("Meta-analysis",
    "A meta-analysis combines the numerical results of similar studies into a weighted estimate of effect, and "
    "this overview pools nothing.", "summarizing trials means pooling"),
   ("Cohort study",
    "A cohort study is primary research that follows a group of people over time, whereas this article "
    "summarizes trials that others carried out.", "primary research")],
  C(S(D10, 4, 5, 6, 22), S(D2S, 3, 25))),

Q("design", 11, IO12B,
  "Reviewers searched three databases for randomized trials of a smoking-cessation drug, applied set inclusion "
  "criteria, and kept nine trials. They then combined the trials' results, weighting each trial by its size, "
  "into a single estimate of effect. Which step made this review a meta-analysis?",
  ("Pooling the results",
   "Correct, because a meta-analysis combines the results of similar studies, weighted in proportion to study "
   "size, to give a more precise estimate of effect."),
  [("Searching several databases",
    "Finding all relevant studies is part of selecting studies for any systematic review, and it does not by "
    "itself produce a pooled estimate.", "searching widely is the defining step"),
   ("Applying inclusion criteria",
    "Explicit selection criteria are a step of every systematic review, while pooling is the later step a "
    "meta-analysis adds when it is justified.", "selection rules define meta-analysis"),
   ("Limiting the review to trials",
    "Restricting the design of included studies is part of defining what is selected, and a review limited to "
    "trials need not pool their results.", "trials only means meta-analysis")],
  C(S(D10, 21, 22)), reserve=True),

Q("design", 2, IO13D,
  "A clinician looking into a treatment finds three sources: a case series of 12 patients, a cohort study of "
  "5,000 patients, and a systematic review of eight randomized controlled trials. Which source sits highest in "
  "the hierarchy of evidence?",
  ("The systematic review",
   "Correct, because systematic reviews sit at the top of the clinical studies pyramid, and studies at higher "
   "levels are least vulnerable to bias and more generalizable."),
  [("The cohort study",
    "Cohort studies sit below randomized controlled trials on the pyramid, so 5,000 patients do not lift a "
    "cohort above a review of trials.", "largest sample ranks highest"),
   ("The case series",
    "Case series sit below cohort and case-control studies on the pyramid, so a detailed account of 12 patients "
    "ranks lowest of the three.", "most detail ranks highest"),
   ("They rank equally",
    "All studies serve a purpose and can guide practice, but some designs are stronger than others, which is "
    "why evidence is ranked as a hierarchy.", "every design is equal")],
  C(S(D2E, 8), S(D2S, 33, 34, 35))),

Q("design", 4, IO12B,
  "A survey of 3,000 adults asked, in one interview, about current depression and about exercise in the past "
  "week. Adults with depression reported less exercise. The authors conclude that inactivity causes "
  "depression. What is the main weakness of that conclusion?",
  ("It cannot show which came first in time",
   "Correct, because a cross-sectional study measures the risk factor and the condition at the same time, "
   "while causality requires that the cause precede the effect."),
  [("It cannot measure how common depression is",
    "Measuring the portion of a group with a condition at one point in time is exactly what a cross-sectional, "
    "or prevalence, study does well.", "cross-sectional cannot give prevalence"),
   ("It cannot include adults without depression",
    "Prevalence is measured by counting the number with and without the condition in the population, so adults "
    "without depression are counted too.", "only cases are studied"),
   ("It cannot use questionnaires to collect data",
    "Surveys and questionnaires are useful for collecting prevalence information, as in cross-sectional studies "
    "of food allergy.", "surveys are not valid data")],
  C(S(D2S, 17), S(D3, 15, 22, 23), S(D9, 30))),

Q("design", 8, IO12B,
  "To study asthma control, researchers numbered the 60 asthma support groups in a region, randomly chose 12 "
  "of them, and enrolled every member of each chosen group. Which sampling method did they use?",
  ("Cluster sampling",
   "Correct, because participants were selected on the basis of their membership in a group, with whole groups "
   "chosen and every member enrolled."),
  [("Stratified sampling",
    "Stratified sampling creates subgroups, such as by age or education level, to represent how those groups "
    "exist in the population.", "groups mean strata"),
   ("Convenience sampling",
    "A convenience sample is non-random and simply easy to obtain, whereas these groups were chosen at random "
    "from a numbered list.", "existing groups are convenient"),
   ("Random sampling of individuals",
    "Random sampling gives every member of the population the same chance of selection one by one, whereas here "
    "whole groups were chosen and individuals came in as members.", "any random step is simple random")],
  C(S(D8T, 16, 18, 20), S(D3, 29)), reserve=True),

Q("design", 9, IO12B,
  "A randomized trial tests whether a supervised exercise and education program, started after a first heart "
  "attack, reduces later complications such as heart failure. Which level of prevention does the trial study?",
  ("Tertiary prevention",
   "Correct, because tertiary prevention is clinical intervention to reduce complications following a "
   "diagnosis, and its treatments are usually studied with randomized trials."),
  [("Secondary prevention",
    "Secondary prevention detects disease while it is still asymptomatic, as screening does, whereas these "
    "patients have already had a heart attack.", "any prevention after risk is secondary"),
   ("Primary prevention",
    "Primary prevention removes underlying causes or risk factors to prevent a disease from occurring, but this "
    "disease has already occurred.", "lifestyle change is always primary"),
   ("Chemoprevention",
    "Chemoprevention is one of the types of preventive care, listed with immunization, screening and counseling, "
    "not one of the three levels of prevention.", "type confused with level")],
  C(S(D8P, 4, 5, 12))),

# =================================================================== BIAS
Q("bias", 1, IO12B,
  "A study of a home exercise program for heart failure enrolled volunteers who answered an advertisement "
  "placed in fitness centers. The comparison group was taken from a list of patients recently discharged from "
  "the hospital. The exercise group had fewer readmissions over a year. Which threat to validity is most likely?",
  ("Selection bias",
   "Correct, because the groups differ in more ways that affect the outcome than only the program, so few "
   "conclusions can be drawn about the program itself."),
  [("Measurement bias",
    "Measurement bias comes from a method of measurement that gives incorrect results, while the problem here "
    "lies in how the two groups were chosen.", "flaw in measurement"),
   ("Attrition effect",
    "The attrition effect arises when participants drop out of a study, and nothing here says anyone left "
    "either group.", "dropouts"),
   ("Performance bias",
    "Performance bias is a difference in the care given to the two groups other than the topic of interest, "
    "while these groups differed before the program began.", "care differs between groups")],
  C(S(D1, 40, 41, 44, 45))),

Q("bias", 1, IO12B,
  "In a 6-month weight-loss trial, the intervention group was weighed on a calibrated clinic scale at every "
  "visit. The control group reported weights from their own home scales, which were never checked. The trial "
  "reported more weight loss in the intervention group. Which threat to validity does this raise?",
  ("Measurement bias",
   "Correct, because the method of measurement differed between the groups and may lead to incorrect results, "
   "and calibrating measuring devices is how the validity of a measurement is ensured."),
  [("Selection bias",
    "Selection bias arises when the groups are assembled so that they differ in more than the focus of the "
    "study, whereas the flaw here is in how weight was measured.", "group composition"),
   ("Non-response bias",
    "Non-response bias arises when those who answer a survey differ from those who do not, and every "
    "participant here supplied a weight.", "self-report means non-response"),
   ("Reporting bias",
    "Reporting bias means only a subset of the relevant data is made available, whereas here the data are "
    "complete but were measured differently.", "self-reported weights mean reporting bias")],
  C(S(D1, 40, 41, 44, 45), S(D3, 52))),

Q("bias", 1, IO12B,
  "A cohort study found that adults with gray hair had twice the rate of heart attack of adults without it. "
  "Gray hair was far more common in the older participants, and older age also raises the risk of heart "
  "attack. Which term best describes age in this study?",
  ("A confounding variable",
   "Correct, because age is associated with both the exposure (gray hair) and the outcome (heart attack), so "
   "its effect cannot be separated from the effect of gray hair."),
  [("An effect modifier",
    "An effect modifier is a variable whose presence or absence changes the effect of an exposure and is not a "
    "bias, whereas age here creates the apparent link itself.", "confounding confused with effect modification"),
   ("The dependent variable",
    "The dependent variable is the possible effect, which in this study is heart attack rather than age.",
    "variable roles confused"),
   ("The independent variable",
    "The independent variable is the possible cause under study, which in this study is gray hair rather than "
    "age.", "variable roles confused")],
  C(S(D1, 37, 42), S(D7R, 26, 28))),

Q("bias", 1, IO12B,
  "A 12-month trial of a weight-loss drug enrolled 300 adults. By month 12, 40 percent of the drug group and "
  "10 percent of the placebo group had stopped attending visits, many after reporting nausea. Only those who "
  "completed the trial were analyzed. Which threat to validity is most prominent?",
  ("Attrition effect",
   "Correct, because participants dropping out reduces the sample size, and a trial must account for "
   "withdrawals and dropouts so that attrition does not falsely skew the outcome data."),
  [("Non-response bias",
    "Non-response bias arises when people who answer a survey differ from those who do not, whereas these "
    "participants enrolled and then left a trial partway through.", "leaving confused with not answering"),
   ("Procedural bias",
    "Procedural bias arises when the method of delivering an interview or questionnaire affects the results, "
    "which is not what happened here.", "trial procedures"),
   ("Publication bias",
    "Publication bias concerns which studies reach print, with research lacking significant results less "
    "likely to be published, not who stays in a trial.", "bias in what is reported")],
  C(S(D1, 44, 46), S(D2S, 27, 30))),

Q("bias", 1, IO12B,
  "A health department mailed a survey about exercise habits to 5,000 randomly chosen residents. Only 900 "
  "returned it, and most of those who replied were retired adults with more free time. The department reported "
  "that residents exercised far more than expected. Which threat to validity is most likely?",
  ("Non-response bias",
   "Correct, because the people who responded differ from those who did not, so the results may not reflect "
   "the whole population."),
  [("Attrition effect",
    "The attrition effect is participants dropping out of a study after entering it, whereas most residents "
    "here never took part at all.", "not answering confused with dropping out"),
   ("Measurement bias",
    "Measurement bias is a method of measurement that leads to incorrect results, whereas the problem here is "
    "who replied, not how exercise was measured.", "survey answers are measurement"),
   ("Confounding",
    "Confounding needs a covariate associated with both an exposure and an outcome, whereas this survey describes "
    "one group's habits without testing an exposure.", "any third factor is confounding")],
  C(S(D1, 41, 42, 44))),

Q("bias", 1, IO12B,
  "A hospital studied patient satisfaction with meals. Patients on the same ward were split at random into two "
  "groups: one answered the questions aloud to the nurse who had served their meals, and the other filled in the "
  "same questions on an anonymous mailed form. The group questioned in person rated satisfaction much higher. "
  "Which bias does this show?",
  ("Procedural bias",
   "Correct, because interview or questionnaire results can be affected by the method of delivery, and here "
   "only the method of asking differed between the groups."),
  [("Selection bias",
    "Selection bias arises when compared groups differ in more than the focus of the study, but these groups "
    "were split at random and asked the same questions.", "two groups means selection bias"),
   ("Reporting bias",
    "Reporting bias means only a subset of the relevant data is made available, whereas both groups' answers "
    "were reported.", "answers distorted when reported"),
   ("Attrition effect",
    "The attrition effect is participants dropping out and reducing the sample size, which nothing here "
    "describes.", "mailed forms are lost")],
  C(S(D1, 40, 44, 45)), reserve=True),

Q("bias", 1, IO12B,
  "In an unblinded trial of a new sleep medication against placebo, participants knew which pill they were "
  "taking. Many in the placebo group began using over-the-counter sleep aids during the study, and the drug "
  "showed little advantage. Which bias does this describe?",
  ("Performance bias",
   "Correct, because care other than the topic of interest differed between the groups, and blinding study "
   "participants is what protects against it."),
  [("Selection bias",
    "Selection bias arises from how the groups were formed, so that they differ at the start, whereas these "
    "groups diverged in the care they received after assignment.", "groups differ, so selection"),
   ("Non-response bias",
    "Non-response bias arises when survey responders differ from non-respondents, whereas this describes extra "
    "treatment taken during a trial.", "participant behavior means non-response"),
   ("Reporting bias",
    "Reporting bias means only a subset of the data is made available, whereas the problem here arose before "
    "any results were reported.", "outcome reports distorted")],
  C(S(D1, 40, 44, 45))),

Q("bias", 1, IO12B,
  "A company sponsored five trials of its new pain drug. The two trials that found a statistically significant "
  "benefit were published, while the three that found no significant difference were never submitted to a "
  "journal. A later review of the published trials concluded that the drug works. Which bias most affected "
  "that review?",
  ("Publication bias",
   "Correct, because research without statistically significant results is less likely to be published, and a "
   "sponsor is less likely to support research that is unfavorable to its product."),
  [("Selection bias",
    "Selection bias arises when a study's comparison groups differ in more than the factor studied, whereas the "
    "distortion here lies in which whole trials reached print.", "the review selected studies"),
   ("Non-response bias",
    "Non-response bias arises when people who answer a survey differ from those who do not, a problem inside "
    "one study rather than across the literature.", "missing trials as non-responders"),
   ("Confounding",
    "Confounding is a covariate associated with both exposure and outcome within a study, and it cannot explain "
    "why the trials without significant results went unpublished.", "any distortion is confounding")],
  C(S(D1, 40, 42, 44, 46))),

Q("bias", 1, IO12B,
  "A published trial of a new arthritis drug listed six outcomes in its plan, including pain, function and "
  "stomach bleeding. The journal article reported only the two outcomes that favored the drug, and the other "
  "four were never made available. Which bias does this describe?",
  ("Reporting bias",
   "Correct, because only a subset of all the relevant data was made available, even though the trial itself "
   "was published."),
  [("Publication bias",
    "Publication bias concerns research that never gets published, often because it lacks statistically "
    "significant results, whereas this trial did reach print.", "any missing results are publication bias"),
   ("Measurement bias",
    "Measurement bias arises when the method of measurement leads to incorrect results, whereas the problem here "
    "is which results were shown.", "outcomes measured wrongly"),
   ("Attrition effect",
    "The attrition effect is participants dropping out and reducing the sample size, which nothing here "
    "describes.", "lost outcomes as lost participants")],
  C(S(D1, 41, 44, 45, 46))),

Q("bias", 6, IO12B,
  "In a case-control study of a birth defect, mothers of affected infants and mothers of healthy infants were "
  "interviewed a year after delivery about the medicines they had taken during pregnancy. No pharmacy or medical "
  "records were checked. Which bias most threatens the exposure data?",
  ("Recall bias",
   "Correct, because the exposure was asked about rather than measured, so it depends on how well each mother "
   "remembers, and remembering is difficult."),
  [("Selection bias",
    "Selection bias concerns how people get into a study, whereas the weak point named here is how exposure was "
    "learned once they were in it.", "case-control groups are always selection"),
   ("Confounding",
    "Confounding is a third factor that distorts the relationship between exposure and outcome, whereas the "
    "problem here is the accuracy of the exposure information itself.", "any distortion is confounding"),
   ("Random error",
    "Random error occurs by chance and is accounted for through the p values used in a study, whereas relying "
    "on memory for exposure is a named bias.", "memory lapses are chance")],
  C(S(D7R, 33), S(D9, 34))),

Q("bias", 9, IO12B,
  "An observational study reports that patients whose colon cancer was found by screening lived a median of 7 "
  "years after diagnosis, compared with 4 years for patients diagnosed after symptoms appeared. The tumors in "
  "both groups had similar growth rates, and patients in both groups died at about the same age. Which bias "
  "best explains the longer survival after diagnosis?",
  ("Lead-time bias",
   "Correct, because screening moved the diagnosis earlier without moving the death, so the apparent gain is "
   "increased time knowing the diagnosis rather than improved survival."),
  [("Length-time bias",
    "Length-time bias arises when screening detects more slow-developing conditions with better prognoses, but "
    "the tumors here grew at similar rates.", "any screening gain is length-time"),
   ("Compliance bias",
    "Compliance bias arises when screened people do better because they are more invested in their health, yet "
    "death came at about the same age in both groups.", "screened people are healthier"),
   ("Overdiagnosis",
    "Overdiagnosis is finding a disease whose detection does not help the patient, an extreme example of "
    "length-time bias, which the similar growth rates rule out here.", "finding more cancers")],
  C(S(D8P, 17, 18, 19, 21, 23))),

Q("bias", 7, IO12B,
  "A survival study compared two treatments for a lymphoma. Patients given treatment A were mostly enrolled at "
  "diagnosis, while patients given treatment B were mostly enrolled after earlier therapy had failed. Treatment "
  "A showed far better survival. Which bias could falsely create this difference?",
  ("Susceptibility bias",
   "Correct, because the groups assembled for the study differ in their point in the disease course and in "
   "prior treatment, which alone can change survival."),
  [("Migration bias",
    "Migration bias arises when patients drop out of a study or change groups during it, whereas these groups "
    "differed when they entered.", "differences arising during follow-up"),
   ("Measurement bias",
    "Measurement bias means one group's outcome is more likely to be detected than the other's, whereas the "
    "problem here is who was enrolled in each group.", "outcome detection"),
   ("Publication bias",
    "Publication bias concerns whether studies without statistically significant results get published, not "
    "differences between the patients within one study.", "bias in what is published")],
  C(S(D7P, 22, 23, 24), S(D1, 46))),

Q("bias", 8, IO12B,
  "Researchers studying hand hygiene told the staff on one hospital ward that observers would record every hand "
  "washing for four weeks. Hand-washing rates rose sharply during those weeks and fell back after the observers "
  "left. Which effect best explains the rise?",
  ("Hawthorne effect",
   "Correct, because participants tend to change their behavior when they are given special interest or "
   "attention during a study."),
  [("Placebo effect",
    "The placebo effect is a change in condition in people given a placebo because they expect a change, and no "
    "placebo was given here.", "expectation effect"),
   ("Attrition effect",
    "The attrition effect is participants dropping out and reducing the sample size, which would not raise "
    "hand-washing rates.", "effect named for loss"),
   ("Recall bias",
    "Recall bias arises when an exposure is asked about rather than measured, whereas this behavior was "
    "observed directly.", "self-report bias")],
  C(S(D8T, 21), S(D1, 44), S(D7R, 33)), reserve=True),

Q("bias", 4, IO12B,
  "In a study of a skin-cancer screening program, two dermatologists independently rated photographs of the same "
  "200 moles as benign or suspicious. They disagreed on 46 of the photographs. Which type of variation does this "
  "disagreement show?",
  ("Interobserver variation",
   "Correct, because two different observers reached different readings of the same thing, which reduces the "
   "reliability of the measurement."),
  [("Intraobserver variation",
    "Intraobserver variation is one observer reading the same thing differently on two occasions, whereas two "
    "separate dermatologists disagreed here.", "within versus between confused"),
   ("Intrasubject variation",
    "Intrasubject variation is change within the person measured, such as blood pressure varying with time of "
    "day, whereas the photographs did not change.", "the subject varied"),
   ("True biologic variation",
    "True biologic variation is the small random variation within a patient from many unknown factors, which "
    "cannot arise between two readings of one photograph.", "biology explains disagreement")],
  C(S(D3, 58, 60, 63)), reserve=True),

# =================================================================== MEASURE
N("measure", 4, IO12B,
  "On January 1, a survey of a retirement community of 2,000 residents found 160 with diabetes. Over the "
  "following year, 40 residents who had not had diabetes developed it. What was the prevalence of diabetes on "
  "January 1?",
  [("2 percent",
    "That uses the 40 new cases arising during the year, which describe incidence (new cases in previously "
    "healthy people), not who had the condition on January 1.", "incidence confused with prevalence"),
   ("8 percent",
    "Correct, because prevalence is the portion of a group with a condition at a specific point in time: 160 of "
    "2,000 residents is 8 percent.", None),
   ("10 percent",
    "That counts the 160 existing cases plus the 40 new ones, which gives the prevalence at the end of the year "
    "rather than on January 1.", "wrong point in time"),
   ("20 percent",
    "That divides the 40 new cases by the 200 total cases, while prevalence divides the existing cases by the "
    "whole community of 2,000.", "wrong denominator")],
  1, C(S(D3, 15, 17, 20))),

Q("measure", 4, IO12B,
  "A county health department wants to know how many previously healthy residents develop Lyme disease each "
  "summer, so it can judge whether a new tick-control program is working. Which measure should it track?",
  ("Incidence",
   "Correct, because incidence is the portion of a group who develop a condition during a specified time "
   "period, describing new cases in previously healthy people."),
  [("Point prevalence",
    "Point prevalence counts everyone with the condition at a single point in time, old cases and new, so it "
    "cannot isolate the new infections.", "prevalence counts new cases"),
   ("Period prevalence",
    "Period prevalence counts all cases present during a time period, including those that began earlier, so it "
    "does not isolate new cases.", "a time period means incidence"),
   ("Case fatality",
    "Case fatality is the proportion of people diagnosed with a disease who die from it, a measure of severity "
    "rather than of new cases.", "outcome rate confused with occurrence")],
  C(S(D3, 14, 15, 17)), reserve=True),

Q("measure", 4, IO12B,
  "A study tested a new automatic blood pressure cuff against an intra-arterial line, which shows the true "
  "pressure. Repeated cuff readings on the same patient agreed within 1 point of each other, but every reading "
  "was about 15 points higher than the true pressure. How should the cuff be described?",
  ("Reliable but not valid",
   "Correct, because repeated readings were consistent (reliability, or precision) but did not measure the true "
   "value (validity, or accuracy)."),
  [("Valid but not reliable",
    "Validity means measuring what is supposed to be measured, and these readings were consistently 15 points "
    "off, while their close agreement shows reliability.", "the two properties reversed"),
   ("Both valid and reliable",
    "Close agreement between repeated readings shows reliability, but a consistent 15-point error means the cuff "
    "does not measure what it is supposed to.", "consistency implies accuracy"),
   ("Neither valid nor reliable",
    "Repeated readings that agree closely are the definition of reliability, so the cuff cannot be called "
    "unreliable.", "any error means unreliable")],
  C(S(D3, 52, 58, 59))),

Q("measure", 4, IO12B,
  "A trial of a new eczema cream recorded each patient's result at 8 weeks as worse, unchanged, improved or "
  "cleared. At which level of measurement are these outcome data?",
  ("Ordinal",
   "Correct, because the categories have an order but no defined intervals between them, like cancer staging or "
   "grades of pitting edema."),
  [("Nominal",
    "Nominal data are categories without a specified order, such as blood type, whereas these four results run "
    "from worse to cleared.", "any category is nominal"),
   ("Dichotomous",
    "Dichotomous data are nominal data divided into two categories, such as yes or no, and this outcome has "
    "four.", "improved or not"),
   ("Continuous",
    "Continuous data have equal, defined intervals and can take any value on a continuum, like weight, which "
    "these four categories cannot.", "order implies interval")],
  C(S(D3, 49, 50, 51)), reserve=True),

N("measure", 6, IO12B,
  "A cohort study followed 400 adults who worked night shifts and 400 who worked only day shifts for five "
  "years. A peptic ulcer developed in 24 of the night-shift workers and 8 of the day-shift workers. What is the "
  "relative risk of ulcer for night-shift work?",
  [("0.04",
    "That is the attributable risk, the incidence in exposed persons (0.06) minus the incidence in non-exposed "
    "persons (0.02), not their ratio.", "attributable risk confused with relative risk"),
   ("0.33",
    "That divides the day-shift incidence by the night-shift incidence, which inverts the ratio, since relative "
    "risk puts the exposed group's incidence on top.", "ratio inverted"),
   ("3",
    "Correct, because relative risk is the incidence in exposed persons divided by the incidence in non-exposed "
    "persons: 24/400 = 0.06 and 8/400 = 0.02, and 0.06/0.02 = 3.", None),
   ("6",
    "That is the incidence among night-shift workers expressed as a percentage (24 of 400 is 6 percent), not a "
    "comparison with the day-shift workers.", "incidence confused with relative risk")],
  2, C(S(D7R, 17, 18, 19, 24))),

N("measure", 6, IO12B,
  "A case-control study enrolled 80 patients with liver cancer and 160 controls without it. Forty of the cases "
  "and 20 of the controls had a history of a particular viral infection. What is the odds ratio for the "
  "infection?",
  [("0.14",
    "That is the odds of infection among the controls, 20 infected to 140 uninfected, which is only the "
    "denominator of the odds ratio.", "one group's odds"),
   ("1",
    "That is the odds of infection among the cases alone, 40 infected to 40 uninfected, before it is compared "
    "with the controls' odds.", "one group's odds"),
   ("4",
    "That divides the proportion of cases infected (40 of 80) by the proportion of controls infected (20 of "
    "160), a ratio of proportions rather than of odds.", "relative risk method used on case-control data"),
   ("7",
    "Correct, because the odds of exposure are 40/40 = 1 in cases and 20/140 in controls, and their ratio, ad/bc "
    "= (40 x 140)/(20 x 40), is 7.", None)],
  3, C(S(D7R, 35, 36, 37, 38))),

Q("measure", 6, IO12B,
  "Investigators followed 3,000 adults for ten years, comparing those who took a daily aspirin with those who "
  "did not, and counted the new cases of colon cancer in each group. Which measure of association should they "
  "report?",
  ("Relative risk",
   "Correct, because a cohort study can directly calculate the incidence of disease in the exposed and the "
   "non-exposed, so relative risk is used rather than the odds ratio."),
  [("Odds ratio",
    "The odds ratio is the measure of association for case-control studies, which start from cases and controls "
    "rather than following a group forward.", "odds ratio fits every design"),
   ("Likelihood ratio",
    "A likelihood ratio describes how much a test result changes the probability that a patient has a "
    "condition, so it belongs to studies of tests.", "any ratio compares groups"),
   ("Case-fatality ratio",
    "The case-fatality ratio is the number of people who die of a disease divided by the number who have it, "
    "which does not compare exposed and unexposed groups.", "any ratio compares groups")],
  C(S(D7R, 35, 40), S(D4, 30), S(D7P, 16))),

N("measure", 5, IO12B,
  "A rapid urine test for bladder infection was compared with urine culture, the gold standard, in 400 "
  "patients. Culture was positive in 100 of them. The rapid test was positive in 90 of those 100 and in 15 of "
  "the 300 patients with a negative culture. What is the sensitivity of the rapid test?",
  [("86 percent",
    "That is the positive predictive value, 90 true positives out of the 105 positive tests, which starts from a "
    "positive result rather than from infection.", "predictive value confused with sensitivity"),
   ("90 percent",
    "Correct, because sensitivity is true positives divided by true positives plus false negatives: 90/(90 + 10) "
    "= 90 percent.", None),
   ("95 percent",
    "That is the specificity, 285 true negatives out of the 300 patients without infection.",
    "specificity confused with sensitivity"),
   ("97 percent",
    "That is the negative predictive value, 285 true negatives out of the 295 negative tests.",
    "predictive value confused with sensitivity")],
  1, C(S(D4, 16, 19, 24))),

N("measure", 5, IO12B,
  "A blood test for a liver disease was given to 1,000 adults, and a biopsy, the gold standard, showed that 50 "
  "of them had the disease. The test was positive in 40 of the 50 with the disease and in 95 of the 950 without "
  "it. An adult in this study tests positive. What is the probability that this adult has the disease?",
  [("30 percent",
    "Correct, because this is the positive predictive value, true positives divided by all positives: 40/(40 + "
    "95) = 30 percent.", None),
   ("80 percent",
    "That is the sensitivity, 40 of the 50 diseased adults testing positive, which starts from disease rather "
    "than from a positive result.", "sensitivity confused with predictive value"),
   ("90 percent",
    "That is the specificity, 855 of the 950 adults without the disease testing negative.",
    "specificity confused with predictive value"),
   ("99 percent",
    "That is the negative predictive value, 855 true negatives out of 865 negative tests, which applies to a "
    "negative result.", "negative predictive value used for a positive result")],
  0, C(S(D4, 16, 19, 24, 25))),

Q("measure", 5, IO12B,
  "A study of two blood tests for appendicitis reports that test A has a sensitivity of 98 percent and a "
  "specificity of 70 percent, while test B has a sensitivity of 75 percent and a specificity of 97 percent. A "
  "clinician wants a negative result to rule appendicitis out. Which choice is best?",
  ("Test A, as high sensitivity leaves few false negatives",
   "Correct, because a negative result on a highly sensitive test rules disease out: when sensitivity is high, "
   "there are very few false negatives."),
  [("Test B, as high specificity leaves few false negatives",
    "High specificity means very few false positives, not false negatives, so test B's lower sensitivity makes "
    "its negative result the less reassuring one.", "specificity confused with sensitivity"),
   ("Test B, as a positive result on it rules disease in",
    "A positive result on a highly specific test does rule disease in, but the clinician here wants a negative "
    "result that rules it out.", "rule-in used for rule-out"),
   ("Test A, as high sensitivity leaves few false positives",
    "High sensitivity means very few false negatives, while it is high specificity that means few false "
    "positives, so this reason is reversed.", "false positives and negatives reversed")],
  C(S(D4, 20))),

N("measure", 5, IO12B,
  "A study of a knee examination maneuver for a torn ligament reports a sensitivity of 80 percent and a "
  "specificity of 90 percent. What is the positive likelihood ratio of the maneuver?",
  [("0.22",
    "That is the negative likelihood ratio, (1 - sensitivity)/specificity = 0.2/0.9, which applies to a negative "
    "result.", "negative likelihood ratio"),
   ("0.89",
    "That divides sensitivity by specificity, 0.8/0.9, but the denominator of the positive likelihood ratio is "
    "1 - specificity.", "wrong denominator"),
   ("4.5",
    "That divides specificity by 1 - sensitivity, 0.9/0.2, which puts the wrong property in both the numerator "
    "and the denominator.", "formula reversed"),
   ("8",
    "Correct, because the positive likelihood ratio is sensitivity/(1 - specificity) = 0.8/0.1 = 8, moderate "
    "evidence to rule the tear in.", None)],
  3, C(S(D4, 30, 31, 44))),

Q("measure", 5, IO12B,
  "A clinic checks patients for a hormone-secreting tumor with an inexpensive urine test and orders a costly, "
  "risky scan only for those whose urine test is positive. Which description fits this testing strategy?",
  ("Serial testing, raising specificity",
   "Correct, because tests done one after another, with the costly or risky test used after the simpler one, "
   "make up serial testing, which maximizes specificity and positive predictive value."),
  [("Serial testing, raising sensitivity",
    "This is serial testing, but serial testing lowers sensitivity and negative predictive value while it "
    "maximizes specificity.", "serial testing effect reversed"),
   ("Parallel testing, raising sensitivity",
    "Parallel tests are all conducted at once, which is not what happens when the scan waits for a positive urine "
    "result.", "two tests means parallel"),
   ("Parallel testing, raising specificity",
    "Parallel tests are conducted at once and generally increase sensitivity, not specificity, and these tests "
    "were done in sequence.", "parallel testing effect reversed")],
  C(S(D4, 46, 47, 48, 49)), reserve=True),

Q("measure", 9, IO12B,
  "Two drugs were tested for stroke prevention over five years. For drug A, the number needed to treat to "
  "prevent one stroke was 40, and the number needed to harm (major bleeding) was 25. For drug B, the number "
  "needed to treat was 120, and the number needed to harm was 400. Which statement best describes the two drugs?",
  ("A prevents more strokes but harms more often",
   "Correct, because a smaller number needed to treat means a more effective intervention, while a smaller "
   "number needed to harm means harm occurs after fewer patients are treated."),
  [("B prevents more strokes and harms less often",
    "B does harm less often, with its larger number needed to harm, but its larger number needed to treat means "
    "it is the less effective drug.", "larger number needed to treat read as better"),
   ("A prevents more strokes and harms less often",
    "A does prevent more strokes, but its number needed to harm of 25 is far smaller than B's 400, so harm comes "
    "after fewer patients are treated.", "smaller number needed to harm read as safer"),
   ("B prevents more strokes but harms more often",
    "B's number needed to treat of 120 is larger than A's 40, so B is less effective, and its larger number needed "
    "to harm means it harms less.", "both numbers read backward")],
  C(S(D8P, 13, 14))),

Q("measure", 7, IO12B,
  "A survival study of patients after a heart attack used Cox proportional hazards regression, adjusted for age "
  "and sex. Patients with a ventricular arrhythmia had a hazard ratio for death of 3.0 compared with patients "
  "without one. How should this hazard ratio be read?",
  ("Three times the risk of dying",
   "Correct, because a hazard ratio can be interpreted as a relative risk, so a value of 3 means the group with "
   "the factor has three times the risk of the outcome."),
  [("One third the risk of dying",
    "A hazard ratio below 1 is considered protective, but a hazard ratio of 3.0 is above 1, so the risk is "
    "higher, not lower.", "ratio direction reversed"),
   ("A 3 percent risk of dying",
    "A hazard ratio compares the risk of the outcome in two groups and is not itself a percentage of patients "
    "who die.", "ratio read as absolute risk"),
   ("Survival three years shorter",
    "A hazard ratio is interpreted as a relative risk of the outcome, not as a difference in survival time "
    "measured in years.", "ratio read as time")],
  C(S(D7P, 19))),

N("measure", 7, IO12B,
  "During an outbreak, 200 people in a city of 100,000 were diagnosed with a new respiratory illness, and 10 of "
  "those 200 died of it. What is the case-fatality ratio?",
  [("0.01 percent",
    "That divides the 10 deaths by the whole city of 100,000, a death rate for the population rather than the "
    "proportion of diagnosed people who died.", "population denominator"),
   ("0.2 percent",
    "That is the share of the city diagnosed with the illness, 200 of 100,000, which describes how many were "
    "affected rather than how many of them died.", "cases confused with deaths"),
   ("5 percent",
    "Correct, because the case-fatality ratio is the number of people who die divided by the number of people "
    "who have the disease: 10/200 = 5 percent.", None),
   ("95 percent",
    "That is the proportion of diagnosed people who survived, whereas the case-fatality ratio counts those who "
    "die, and framing by deaths or by survivors needs care.", "survivors counted instead of deaths")],
  2, C(S(D7P, 16), S(D3, 14))),

Q("measure", 10, IO12B,
  "A trial compares the mean systolic blood pressure after 12 weeks between 150 patients on a new drug and 150 "
  "patients on placebo. Which statistical test fits this comparison?",
  ("Student t test",
   "Correct, because the Student t test is used to test the statistical significance of a difference between "
   "two means."),
  [("Chi square test",
    "Chi square tests a difference between two or more proportions when there are a large number of "
    "observations, not a difference between means.", "large sample means chi square"),
   ("Fisher exact test",
    "The Fisher exact test compares two proportions when there are a small number of observations, so it does "
    "not fit two means.", "two groups means Fisher exact"),
   ("Mann-Whitney U test",
    "The Mann-Whitney U test compares two medians rather than two means.", "medians confused with means")],
  C(S(D9, 13)), reserve=True),

# =================================================================== STATS
Q("stats", 10, IO12B,
  "A randomized trial of a migraine drug reports 1.5 fewer migraine days per month than placebo, with a p value "
  "of 0.08. How should this result be described?",
  ("Not statistically significant",
   "Correct, because p values less than 0.05 are generally accepted as statistically significant, and 0.08 is "
   "above that cutoff."),
  [("Significant at the 0.05 level",
    "A result is generally accepted as significant when p is less than 0.05, and 0.08 is above that value.",
    "cutoff misread"),
   ("Highly significant",
    "Highly significant is generally used for a p value of 0.01, a 1 in 100 probability of chance, which is far "
    "below 0.08.", "any reported p value is significant"),
   ("Proof that the drug has no effect",
    "A result that is not significant can be a type II error, a false negative that study limitations can cause, "
    "so it does not prove there is no effect.", "absence of significance proves no effect")],
  C(S(D9, 7, 11))),

Q("stats", 10, IO12B,
  "A trial of 30,000 adults found that a new blood pressure drug lowered systolic pressure by 1 millimeter of "
  "mercury more than the standard drug, with a p value below 0.001. Which conclusion is best supported?",
  ("Significant, but perhaps not clinically important",
   "Correct, because statistical significance does not imply clinical significance, and a difference can have a "
   "very small p value yet no relevance to clinical practice."),
  [("Clinically important, because p is so small",
    "A very small p value shows the difference is unlikely to be due to chance, but statistical significance "
    "does not imply clinical significance.", "small p value means important"),
   ("Not significant, because the difference is small",
    "Small differences can still be statistically significant, and a p value of 0.001 is generally accepted as "
    "very highly significant.", "small difference means not significant"),
   ("Probably due to chance, given the small difference",
    "A p value of 0.001 means the probability of chance is 1 in 1,000, so chance is an unlikely explanation.",
    "small difference means chance")],
  C(S(D9, 7, 22))),

Q("stats", 10, IO12B,
  "A trial of an inhaled drug for chronic lung disease reports relative risks, drug versus placebo, with 95 "
  "percent confidence intervals: hospital admission 0.70 (0.55 to 0.90), death 0.85 (0.60 to 1.20), pneumonia "
  "1.40 (0.90 to 2.20), and oral thrush 2.10 (1.40 to 3.10). Which outcome shows a statistically significant "
  "increase with the drug?",
  ("Oral thrush",
   "Correct, because its whole interval lies above 1, the null value at which risk is equal in the two groups, "
   "so a true relative risk of 1 is not within the interval."),
  [("Pneumonia",
    "Its point estimate of 1.40 suggests more pneumonia, but the interval of 0.90 to 2.20 includes 1, the value "
    "of no association.", "point estimate read alone"),
   ("Death",
    "Its interval of 0.60 to 1.20 includes 1, the value of no association, so a true difference in deaths is not "
    "shown either way.", "estimate below 1 read as change"),
   ("Hospital admission",
    "Its interval lies wholly below 1, which shows a significant decrease in admissions with the drug, not an "
    "increase.", "direction reversed")],
  C(S(D9, 14, 15), S(D7R, 20))),

Q("stats", 10, IO12B,
  "A meta-analysis of a lifestyle program reports a relative risk of 0.80 (95 percent confidence interval 0.70 "
  "to 0.92) for developing type 2 diabetes and 0.95 (0.80 to 1.12) for heart attack. Which statement is correct?",
  ("Only the diabetes result is significant",
   "Correct, because the diabetes interval lies entirely below 1, while the heart attack interval runs from 0.80 "
   "to 1.12 and so includes 1, the value of no association."),
  [("Only the heart attack result is significant",
    "The heart attack interval includes 1, the null value at which risk is equal in both groups, so that result "
    "is not statistically significant.", "interval including 1 read as significant"),
   ("Both results are statistically significant",
    "Both point estimates are below 1, but the heart attack interval of 0.80 to 1.12 still includes 1, so only "
    "one result is significant.", "point estimates read alone"),
   ("Neither result is statistically significant",
    "The diabetes interval of 0.70 to 0.92 stays below 1, so the true value is not likely to be 1 and that "
    "result is statistically significant.", "every interval read as including 1")],
  C(S(D9, 14, 15), S(D7R, 20))),

Q("stats", 10, IO12B,
  "A trial of 40 patients followed for three months found no statistically significant difference in relapse "
  "between a new drug and placebo. A later trial of 2,000 patients followed for two years found a clear benefit "
  "of the same drug. What error did the first trial most likely make?",
  ("A type II error",
   "Correct, because concluding that no relationship exists when one does is a type II error, a false negative "
   "that can result from study limitations such as the length of follow-up."),
  [("A type I error",
    "A type I error is a false positive, concluding that a relationship exists when it does not, which is the "
    "opposite of the first trial's finding.", "error types reversed"),
   ("Recall bias",
    "Recall bias comes from participants' difficulty remembering, whereas relapse in a trial is an outcome the "
    "researchers observe.", "any error is a bias"),
   ("Confounding",
    "Confounding is a third factor that distorts an exposure-outcome relationship, not the name for a study "
    "failing to detect a difference that exists.", "any error is confounding")],
  C(S(D9, 9, 10, 11, 34))),

Q("stats", 10, IO12B,
  "A trial tests whether a new antibiotic cures more ear infections than amoxicillin. Before the analysis, the "
  "statistician states the null hypothesis. Which statement is the null hypothesis?",
  ("The two drugs cure the same share",
   "Correct, because the null hypothesis is the hypothesis that there is no difference, usually the opposite of "
   "what the researchers are interested in finding."),
  [("The new drug cures more infections",
    "That is what the researchers hope to show, whereas the null hypothesis is usually the opposite, that there "
    "is no difference.", "research hypothesis confused with null"),
   ("Amoxicillin cures more infections",
    "That states a difference in the other direction, whereas the null hypothesis is that there is no "
    "difference between the drugs.", "null means the opposite direction"),
   ("Neither drug cures any infection",
    "The null hypothesis is that the drugs do not differ, not that both fail, since equal cure rates can be "
    "high or low.", "null means zero effect")],
  C(S(D9, 8)), reserve=True),

Q("stats", 10, IO12B,
  "A trial compared a dietary supplement with placebo on 25 different outcomes. Only one, hair thickness, "
  "reached a p value of 0.04. The published article was built around that finding and did not say how many "
  "outcomes had been examined or which had been primary. What is the main problem with its conclusion?",
  ("Multiple comparisons",
   "Correct, because selecting the more interesting comparisons after the analysis, without saying how many "
   "questions were examined or which was primary, can distort the data."),
  [("A type II error",
    "A type II error is a false negative, concluding that no relationship exists when one does, whereas this "
    "article claims a positive finding.", "error types reversed"),
   ("Recall bias",
    "Recall bias arises from participants' difficulty remembering, whereas this trial measured its outcomes "
    "directly.", "any distortion is recall"),
   ("Confounding",
    "Confounding is a third factor that distorts a relationship, whereas the problem here is how the one "
    "significant result was chosen.", "any distortion is confounding")],
  C(S(D9, 11, 17, 18, 34))),

Q("stats", 10, IO12B,
  "A cohort study of 20,000 adults found that bladder cancer rates rose step by step with the number of "
  "cigarettes smoked per day, from light to moderate to heavy smokers. Which criterion for causality does this "
  "finding support?",
  ("Dose-response",
   "Correct, because a larger exposure leading to a higher rate of disease is the dose-response criterion for "
   "causality."),
  [("Temporality",
    "Temporality means the cause precedes the effect, whereas this finding concerns how the rate changes with "
    "the amount smoked.", "any cohort finding is temporality"),
   ("Reversibility",
    "Reversibility means decreased exposure leads to less disease, which would need people who cut down or "
    "quit, not a comparison of amounts smoked.", "less exposure, less disease"),
   ("Consistency",
    "Consistency means findings are replicable in other studies, whereas this is a single study.",
    "large study means consistent")],
  C(S(D9, 30))),

# =================================================================== PICO
Q("pico", 11, IO13A,
  "A clinician asks: \"In adults over 65 with type 2 diabetes, does adding a daily walking program, compared "
  "with diet advice alone, lower average blood glucose after six months?\" In this clinical question, which part "
  "is the comparison?",
  ("Diet advice alone",
   "Correct, because the comparison is the main alternative to compare with the intervention, here diet advice "
   "given without the walking program."),
  [("A daily walking program",
    "The walking program is the intervention, the main option being considered, while the comparison is what it "
    "is weighed against.", "intervention confused with comparison"),
   ("Adults over 65 with type 2 diabetes",
    "Adults over 65 with type 2 diabetes are the patients or population, the group similar to the clinician's "
    "own patients.", "population confused with comparison"),
   ("Lower average blood glucose",
    "Lower average blood glucose is the outcome, what the clinician hopes to accomplish, measure, improve or "
    "affect.", "outcome confused with comparison")],
  C(S(D10, 8, 9, 10))),

Q("pico", 11, IO13A,
  "A pediatrician asks: \"In children with an ear infection, does a delayed antibiotic prescription, compared "
  "with an immediate antibiotic, relieve ear pain as well within three days?\" Which part of the question is the "
  "outcome?",
  ("Relief of ear pain within three days",
   "Correct, because the outcome is what the clinician hopes to accomplish, measure, improve or affect, here "
   "relief of ear pain within three days."),
  [("Children with an ear infection",
    "Children with an ear infection are the patients or population, the group of patients the question "
    "describes.", "population confused with outcome"),
   ("A delayed antibiotic prescription",
    "The delayed prescription is the intervention, the main option being considered.",
    "intervention confused with outcome"),
   ("An immediate antibiotic",
    "The immediate antibiotic is the comparison, the main alternative weighed against the intervention.",
    "comparison confused with outcome")],
  C(S(D10, 8, 9))),

Q("pico", 11, IO13A,
  "A student drafts this question for a literature search: \"In adult smokers, does a nicotine patch help "
  "people stay smoke-free for one year?\" Which element of a PICO (Patients, Intervention, Comparison, "
  "Outcomes) question is missing?",
  ("Comparison",
   "Correct, because nothing in the question states the main alternative to compare with the nicotine patch, "
   "such as no patch."),
  [("Patients",
    "Adult smokers are named as the patients, the group of people the question is about.",
    "population thought missing"),
   ("Intervention",
    "The nicotine patch is named as the intervention, the main option being considered.",
    "intervention thought missing"),
   ("Outcomes",
    "Staying smoke-free for one year is named as the outcome, the result the student hopes to measure.",
    "outcome thought missing")],
  C(S(D10, 8, 9, 16))),

Q("pico", 11, IO13B,
  "A clinician wonders whether vitamin D helps older people avoid falls. Which question is best formed for "
  "searching the literature?",
  ("In adults over 70, does vitamin D, compared with placebo, reduce falls?",
   "Correct, because it names all four parts: the patients (adults over 70), the intervention (vitamin D), the "
   "comparison (placebo) and the outcome (falls)."),
  [("In adults over 70, does daily vitamin D taken every winter reduce falls?",
    "It names the patients, the intervention and the outcome, but no comparison, the main alternative to weigh "
    "against vitamin D.", "detail substitutes for a comparison"),
   ("Does daily vitamin D, compared with a placebo tablet, reduce falls?",
    "It names the intervention, the comparison and the outcome, but no patients, so it does not describe a group "
    "similar to the clinician's.", "population can be left implicit"),
   ("In adults over 70, is daily vitamin D better than a placebo tablet?",
    "It names the patients, the intervention and the comparison, but \"better\" names no outcome to measure.",
    "outcome can be left implicit")],
  C(S(D10, 8, 9, 10))),

Q("pico", 11, IO13A,
  "A researcher asks: \"In working women, is regular night-shift work, compared with day work only, associated "
  "with a higher risk of breast cancer?\" Which element is regular night-shift work?",
  ("Intervention, as an exposure",
   "Correct, because the intervention element can be an intervention, a prognostic factor or an exposure, and "
   "night-shift work is the exposure being considered."),
  [("Patients, as the population",
    "The patients or population here are working women, the group the question describes.",
    "population confused with exposure"),
   ("Comparison, as the alternative",
    "The comparison is day work only, the main alternative weighed against night-shift work.",
    "comparison confused with exposure"),
   ("Outcome, as the result measured",
    "The outcome is the risk of breast cancer, what the researcher hopes to measure.",
    "outcome confused with exposure")],
  C(S(D10, 9))),

Q("pico", 11, IO13A,
  "A clinician asks: \"In adults with suspected kidney stones, does ultrasound detect stones as accurately as "
  "computed tomography?\" Which element of the question is ultrasound?",
  ("The intervention",
   "Correct, because ultrasound is the main option being considered, while computed tomography is the "
   "alternative it is compared against."),
  [("The comparison",
    "The comparison is computed tomography, the main alternative against which ultrasound is judged.",
    "intervention confused with comparison"),
   ("The outcome",
    "The outcome is how accurately stones are detected, the result the clinician hopes to measure.",
    "test confused with outcome"),
   ("The population",
    "The population is adults with suspected kidney stones, the group the question is about.",
    "population confused with intervention")],
  C(S(D10, 9, 14)), reserve=True),

Q("pico", 11, IO13A,
  "An abstract reads: \"We randomly assigned 600 adults with acute low back pain seen in primary care to "
  "naproxen or acetaminophen and measured disability scores at four weeks.\" Which detail is the outcome element "
  "of a matching clinical question?",
  ("Disability at four weeks",
   "Correct, because the outcome is what the clinician hopes to measure, improve or affect, here disability "
   "scores at four weeks."),
  [("Adults with acute low back pain",
    "Adults with acute low back pain in primary care are the patients, the group whose care the question "
    "concerns.", "population confused with outcome"),
   ("Naproxen",
    "Naproxen is one of the two treatments being compared, the intervention or its comparison, not the result "
    "that was measured.", "treatment confused with outcome"),
   ("Acetaminophen",
    "Acetaminophen is the other treatment in the comparison, not the result that was measured.",
    "treatment confused with outcome")],
  C(S(D10, 8, 9))),

# =================================================================== TRIAL
Q("trial", 1, IO12C,
  "A randomized trial of a heart failure drug enrolled only men aged 40 to 60 with normal kidney function, at "
  "three academic medical centers, and found a clear benefit. A clinician in a community practice wants to give "
  "the drug to an 82-year-old woman with kidney disease. Which property of the trial is most in question for her?",
  ("Its external validity",
   "Correct, because external validity is the degree to which results are also true in other clinical settings, "
   "and this sample may not represent her."),
  [("Its internal validity",
    "Internal validity is the degree to which the results are correct for the sample of patients studied, and "
    "nothing here suggests they were wrong for those men.", "the two validities confused"),
   ("Its statistical significance",
    "Statistical significance concerns how likely a result is to have happened by chance, not whether it applies "
    "to a patient unlike those studied.", "significance means applicability"),
   ("Its reliability",
    "Reliability is consistency of measurement on repeated attempts, which does not address whether the trial's "
    "patients resemble hers.", "reliability means applicability")],
  C(S(D1, 50, 51), S(D9, 6), S(D3, 58))),

Q("trial", 8, IO12B,
  "A trial of a new inhaler was run in ordinary primary care clinics, with patients managing their own doses, "
  "usual reminders and no extra monitoring, to learn how well it works in everyday practice. What does this "
  "trial mainly measure?",
  ("Effectiveness",
   "Correct, because effectiveness represents real, ordinary circumstances and takes into account compliance, "
   "practicality and cost."),
  [("Efficacy",
    "Efficacy represents ideal trial circumstances, such as close monitoring, which this trial deliberately "
    "avoided.", "efficacy and effectiveness confused"),
   ("Non-inferiority",
    "A non-inferiority trial asks whether a new treatment is unlikely to be less effective than an established "
    "one, which is not the aim stated here.", "comparison with standard treatment"),
   ("Allocation concealment",
    "Allocation concealment means the researchers assigning patients to treatment groups are blinded, a "
    "safeguard rather than something a trial measures.", "trial safeguard confused with aim")],
  C(S(D8T, 23, 27, 28, 29))),

Q("trial", 8, IO12B,
  "In a trial of a new antidepressant, a pharmacist prepared identical-looking capsules of drug and placebo. "
  "Neither the participants nor the researchers who assessed them knew who received which. Which term describes "
  "this trial?",
  ("Double-blind",
   "Correct, because in a double-blind trial the researchers and the subjects are both unaware of which "
   "treatment is being received."),
  [("Single-blind",
    "In a single-blind trial the subjects are unaware but the researchers are aware, whereas here the researchers "
    "were unaware as well.", "who is blinded confused"),
   ("Open label",
    "Open label means no blinding is done, whereas identical capsules kept everyone here unaware.",
    "placebo use confused with blinding"),
   ("Non-inferiority",
    "A non-inferiority trial is defined by its aim, showing a new treatment is unlikely to be less effective, not "
    "by who is unaware of the treatment.", "trial aim confused with blinding")],
  C(S(D8T, 21, 23, 29))),

Q("trial", 8, IO12B,
  "In a randomized trial of surgery versus medication, the coordinator enrolling patients could see the next "
  "assignment on an open list. Several frail patients were held back until a medication slot came up. Which "
  "safeguard was missing?",
  ("Allocation concealment",
   "Correct, because allocation concealment means the researchers assigning patients to treatment groups are "
   "blinded, so the coordinator could not have known the next assignment."),
  [("A placebo control",
    "A placebo is indistinguishable from the treatment and helps blinding of participants, but it would not hide "
    "the list from the coordinator.", "placebo prevents all bias"),
   ("Stratified sampling",
    "Stratified sampling creates subgroups to represent how groups exist in the population, which does not hide "
    "upcoming assignments.", "sampling confused with assignment"),
   ("Exclusion criteria",
    "Exclusion criteria are factors that prevent inclusion in a study, and holding frail patients back for one "
    "arm is not a stated criterion.", "eligibility confused with assignment")],
  C(S(D8T, 15, 18, 21, 23))),

Q("trial", 7, IO12B,
  "Investigators planning a study of a dietary supplement debate how to control confounding. One suggests "
  "matching participants on age and sex, and another suggests random assignment to supplement or placebo. Which "
  "advantage does random assignment offer over matching?",
  ("It balances factors no one chose to measure",
   "Correct, because randomization is the only method of dealing with differences between groups whose benefits "
   "are not limited to the factors selected for consideration."),
  [("It makes the results generalizable",
    "Generalizability is often limited because study patients may not represent other populations, and "
    "randomization does not change who is enrolled.", "randomization ensures generalizability"),
   ("It can be applied after data are collected",
    "Randomization assigns participants before outcomes occur, so it cannot be applied after the data are "
    "collected.", "design and analysis methods confused"),
   ("It removes the need to blind anyone",
    "Randomization decides who receives which treatment, while blinding keeps participants and researchers "
    "unaware of it, so one does not replace the other.", "randomization replaces blinding")],
  C(S(D7P, 25, 26), S(D7R, 27), S(D8T, 23))),

Q("trial", 1, IO12C,
  "A trial at one referral hospital randomized patients, blinded the outcome assessors, kept the groups similar "
  "at baseline and followed every patient to the end. All participants were referred by specialists and had "
  "severe disease. Which description best fits the trial?",
  ("High internal, uncertain external validity",
   "Correct, because its methods protect the correctness of the results for the patients studied, but referred "
   "patients with severe disease may not represent those in other clinical settings."),
  [("Low internal, high external validity",
    "Randomization, blinding and complete follow-up protect internal validity, and a referred, severe sample "
    "makes generalizability uncertain rather than high.", "both validities reversed"),
   ("Low internal, uncertain external validity",
    "The trial's methods protect the correctness of results for the sample studied, so its internal validity is "
    "high rather than low.", "a single center means low internal validity"),
   ("High internal and high external validity",
    "Generalizability is rarely determined from a single study, and patients referred to one center may not "
    "represent other settings.", "internal validity implies external validity")],
  C(S(D1, 51), S(D7P, 8, 26, 30))),

Q("trial", 8, IO12B,
  "A new oral antibiotic costs less and causes fewer side effects than an established injected antibiotic. A "
  "trial is designed to show only that the new drug is unlikely to be less effective than the established one. "
  "Which type of trial is this?",
  ("Non-inferiority trial",
   "Correct, because a non-inferiority trial determines whether a new treatment, which may be cheaper, safer or "
   "easier, is unlikely to be less effective than an established one."),
  [("Superiority trial",
    "A superiority trial determines whether one treatment is better than another, a stronger claim than this "
    "trial sets out to make.", "any comparison trial is superiority"),
   ("Phase I trial",
    "A phase I trial uses a small number of participants, with no control group, to identify a safe or tolerated "
    "dose.", "new drug means phase I"),
   ("Trial of N = 1",
    "A trial of N = 1 gives one patient one treatment at a time, with patient and provider blinded, rather than "
    "comparing two groups.", "single drug means single subject")],
  C(S(D8T, 29, 32, 33))),

N("trial", 8, IO12B,
  "A company gives a new drug at gradually rising doses to 20 volunteers, with no control group, to find the "
  "highest dose people can tolerate safely. Which phase of clinical trial is this?",
  [("Phase I",
    "Correct, because phase I trials use a small number of participants, with no control group, to identify a "
    "safe or tolerated dose.", None),
   ("Phase II",
    "Phase II also uses a small number of participants, but it identifies a preliminary effect and any "
    "relationship to dose.", "dose finding in phase II"),
   ("Phase III",
    "Phase III uses more participants than phases I and II, is randomized, and seeks definitive evidence of "
    "effect.", "phases confused"),
   ("Postmarketing surveillance",
    "Postmarketing surveillance follows large numbers of patients after a drug is released, to find more "
    "uncommon side effects.", "safety means postmarketing")],
  0, C(S(D8T, 33, 34)), fixed=True, reserve=True),

N("trial", 2, IO13D,
  "A national task force reviews a screening test for adults over 85 and concludes, with moderate certainty, "
  "that the service has no net benefit. Which grade of recommendation does this conclusion match?",
  [("Grade B",
    "Grade B recommends the service, with high certainty of moderate net benefit or moderate certainty of "
    "moderate to substantial net benefit.", "moderate certainty means grade B"),
   ("Grade C",
    "Grade C means offering the service selectively, with at least moderate certainty that the net benefit is "
    "small rather than absent.", "small benefit confused with none"),
   ("Grade D",
    "Correct, because grade D recommends against a service when there is moderate or high certainty that it has "
    "no net benefit or that the harms outweigh the benefits.", None),
   ("Grade I",
    "Grade I means the evidence is insufficient to assess the balance of benefits and harms, whereas this "
    "conclusion was reached with moderate certainty.", "no benefit confused with insufficient evidence")],
  2, C(S(D2E, 12, 13)), fixed=True),

N("trial", 11, IO13D,
  "A guideline panel finds that the benefits of a treatment clearly outweigh its risks, based on consistent "
  "evidence from well-performed randomized controlled trials, and judges that further research is unlikely to "
  "change its confidence. Which grade fits this recommendation?",
  [("1A",
    "Correct, because a strong recommendation with high-quality evidence rests on consistent evidence from "
    "well-performed randomized controlled trials, with benefits clearly outweighing risks.", None),
   ("1C",
    "Grade 1C is a strong recommendation on low-quality evidence, from observational studies or trials with "
    "serious flaws, where any estimate of effect is uncertain.", "evidence quality misread"),
   ("2A",
    "Grade 2A has high-quality evidence but is a weak recommendation, because benefits are closely balanced with "
    "risks and burdens.", "strength of recommendation misread"),
   ("2C",
    "Grade 2C is a weak recommendation on low-quality evidence, with uncertainty in the estimates of benefits, "
    "risks and burdens.", "both scales misread")],
  0, C(S(D10, 30, 31)), fixed=True, reserve=True),

Q("trial", 2, IO13D,
  "A health website about a joint supplement is written by a board-certified physician, gives detailed "
  "information on dosing and side effects, and was updated last month. The site is owned by the company that "
  "sells the supplement. Which element of the ABCD (Author, Bias, Content, Date) method raises the main concern?",
  ("Bias",
   "Correct, because a site owned by the seller of the product it describes raises the question of bias, which "
   "the author's credentials, the detail and the recent date do not answer."),
  [("Author",
    "The author element asks about credentials, qualifications and expertise in the field, and a board-certified "
    "physician meets it.", "commercial site means unqualified author"),
   ("Content",
    "The content element concerns the level of detail, and this site gives detailed dosing and side-effect "
    "information.", "content element covers motive"),
   ("Date",
    "The date element asks whether the source is still current, and an update last month meets it.",
    "date element covers motive")],
  C(S(D2E, 17, 18))),

# =================================================================== ARTICLE
Q("article", 11, IO12A,
  "A clinician scanning a list of new articles finds one whose title matches her question. She wants to learn "
  "quickly what the study was about and what it concluded. Which part of the article should she read first?",
  ("The abstract",
   "Correct, because a quick reading starts with the abstract, which shows what the study is about and what was "
   "concluded."),
  [("The methods",
    "The methods show how strong the research was, an in-depth question that comes after the abstract has shown "
    "the article is relevant.", "in-depth step first"),
   ("The discussion",
    "The discussion gives context and belongs to the in-depth review, after the abstract has shown the article "
    "is worth reading.", "in-depth step first"),
   ("The figures and tables",
    "The figures and tables show how big the effect was, an in-depth question that comes after the abstract.",
    "in-depth step first")],
  C(S(D10, 38, 39, 40, 41))),

Q("article", 11, IO12A,
  "After reading an abstract, a reader wants to check how participants were assigned to groups and whether the "
  "outcome assessors were blinded. Which part of the article answers these questions?",
  ("The methods",
   "Correct, because how strong the methods were is answered in the methods section during an in-depth review."),
  [("The introduction",
    "The introduction shows the importance of the research question, not how the study was carried out.",
    "introduction describes the study"),
   ("The discussion",
    "The discussion places the study in context rather than describing how participants were assigned and "
    "assessed.", "discussion describes the study"),
   ("The figures and tables",
    "The figures and tables show how big the effect was, not how the study was designed.",
    "results describe the design")],
  C(S(D10, 39, 41))),

Q("article", 11, IO12A,
  "A reader has decided an article is relevant and now wants to see the actual size of the difference in "
  "outcomes between the groups, with the numbers for each group. Where should the reader look?",
  ("The figures and tables",
   "Correct, because the question of how big the effect was is answered by the figures and tables during an "
   "in-depth review."),
  [("The introduction",
    "The introduction shows how important the research question is, not how large the effect was.",
    "introduction gives results"),
   ("The methods",
    "The methods show how strong the study's methods were, not the size of the effect it found.",
    "methods give results"),
   ("The title",
    "The title tells what the study is about, the first step of a cursory review, and gives no numbers.",
    "title gives results")],
  C(S(D10, 39, 41))),

Q("article", 11, IO12A,
  "A rural clinician reading an abstract wants to know whether the study's participants and setting resemble her "
  "own patients before reading further. Which question of a cursory review is she asking?",
  ("To whom does it apply?",
   "Correct, because asking to whom the study applies directs the reader to the patients and setting, one step "
   "of a cursory review."),
  [("Is it likely to be true?",
    "Asking whether a study is likely to be true directs the reader to its design, not to its patients and "
    "setting.", "truth confused with applicability"),
   ("What was concluded?",
    "Asking what was concluded directs the reader to the conclusions rather than to who was studied.",
    "conclusion confused with applicability"),
   ("How big was the effect?",
    "Asking how big the effect was belongs to the in-depth review and is answered by the figures and tables.",
    "effect size confused with applicability")],
  C(S(D10, 38, 41))),

Q("article", 11, IO12A,
  "A reader finds an article whose title fits her topic. On reading the abstract, she finds the aims unclear, no "
  "well-defined research hypothesis, and conclusions that do not fit what she is looking for. What should she do "
  "next?",
  ("Skip it for the next article",
   "Correct, because when the abstract is not useful or relevant to what the reader is looking for, the reader "
   "skips the article and goes to the next."),
  [("Read the entire article",
    "The entire article is read only when the abstract is useful or relevant to the reader's question, which this "
    "one is not.", "always read the whole article"),
   ("Read only the discussion",
    "The discussion belongs to an in-depth review, which is reached only after the abstract has shown the article "
    "is relevant.", "discussion rescues an article"),
   ("Read only the figures and tables",
    "The figures and tables are part of an in-depth review, which this reader has no reason to begin.",
    "results rescue an article")],
  C(S(D10, 40, 41)), reserve=True),
]
