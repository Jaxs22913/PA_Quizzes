#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Interpretation of Medical Literature Arcade decks.

Six decks, one per quiz topic, so Arcade and the quizzes divide the course the
same way.

ATOMIC FACTS ONLY, per [[arcade_content_policy]] -- one question, one short
answer, no vignettes, nothing that needs a picture. The worked examples (the
HUGIT 2x2, the Centor case, the prevalence/predictive-value table) stay in the
guide, because a card cannot carry a table.

This course has no group in arcade.js yet, so the script creates one. It goes
after Clinical Pathophysiology I, keeping the Fall classes adjacent.

Idempotent: fenced between markers, re-runnable.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCADE = os.path.join(ROOT, "arcade.js")
OPEN, CLOSE = "  // <!--MEDLIT-DECKS-->", "  // <!--/MEDLIT-DECKS-->"

SCALE_ICON = ('<path d="M12 3v18"/><path d="M5 7h14"/><path d="M5 7l-2 6a3 3 0 0 0 6 0z"/>'
              '<path d="M19 7l2 6a3 3 0 0 1-6 0z"/><path d="M8 21h8"/>')
BOOK_ICON = ('<path d="M4 5a2 2 0 0 1 2-2h12v16H6a2 2 0 0 0-2 2z"/><path d="M8 7h7"/><path d="M8 11h7"/>')
FLASK_ICON = ('<path d="M10 3v6L4 19a2 2 0 0 0 2 3h12a2 2 0 0 0 2-3l-6-10V3"/>'
              '<path d="M9 3h6"/><path d="M7.5 14h9"/>')
CHART_ICON = ('<path d="M4 20V10"/><path d="M10 20V4"/><path d="M16 20v-7"/><path d="M3 20h18"/>')
RULER_ICON = ('<path d="M3 15l12-12 6 6-12 12z"/><path d="M7 11l2 2"/><path d="M10 8l2 2"/>'
              '<path d="M13 5l2 2"/>')
GRID_ICON = ('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 12h18"/><path d="M12 3v18"/>')

DECKS = [
 ("medlit-bias", "Bias &amp; Validity", "accent1", SCALE_ICON, [
  ("Define bias.", "Systematic error producing conclusions that differ from the true results."),
  ("Define chance.", "Random variation producing conclusions that differ from the true results."),
  ("What separates bias from chance?", "Bias is systematic and one-directional; chance is random and equally likely either way."),
  ("At which stages can bias occur?", "Conception and design, data collection, data analysis, data interpretation."),
  ("Selection (sampling) bias is about what?", "Compared groups differing in more ways affecting the outcome than the study&rsquo;s focus."),
  ("At which stage is selection bias considered?", "Study design."),
  ("At which stage is confounding considered?", "Data analysis."),
  ("Define measurement bias.", "The method of measurement leads to incorrect results."),
  ("Classic measurement bias example?", "Blood pressure taken without a standardised procedure every time."),
  ("Define confounding.", "The covariate&rsquo;s effect cannot be separated from the variable being studied."),
  ("Must a confounder cause the disease?", "No &mdash; it need only be associated with both the exposure and the outcome."),
  ("What can give rise to confounding?", "Selection bias or chance."),
  ("Define procedural bias.", "Interview or questionnaire results affected by the method of delivery."),
  ("Procedural bias example?", "A post-operative questionnaire given while anaesthesia is still wearing off."),
  ("Define the attrition effect.", "Participants drop out, reducing the sample size."),
  ("Define non-response bias.", "Responders differ from non-responders, so the sample may not reflect the population."),
  ("Define performance bias.", "Care differs between groups in ways other than the topic of interest."),
  ("What protects against performance bias?", "Blinding of study participants."),
  ("Define reporting bias.", "Only a subset of all relevant data is made available."),
  ("Define publication bias.", "Research without statistically significant results is less likely to be published."),
  ("Two forces driving publication bias?", "Journal editor preference, and sponsors unwilling to support unfavourable research."),
  ("Define conflict of interest.", "Financial or personal considerations affecting objectivity; should be disclosed."),
  ("Can a conflict of interest act unconsciously?", "Yes &mdash; the impact may be conscious or unconscious."),
  ("Can statistics correct for bias?", "No. Analysis estimates chance; no analysis corrects for unknown biases."),
  ("Can chance be eliminated?", "No &mdash; reduced by good design, estimated statistically, never eliminated."),
  ("All blood pressures fall above the true value. Bias or chance?", "Bias &mdash; random variation would scatter both ways."),
  ("Define internal validity.", "The degree results are correct for the sample of patients studied."),
  ("Define external validity.", "The degree results are also true in other clinical settings."),
  ("What else is external validity called?", "Generalisability."),
  ("Is external validity settled by one study?", "No &mdash; rarely determined from a single study."),
  ("Independent variable is?", "The possible cause."),
  ("Dependent variable is?", "The possible effect."),
  ("What is a covariate?", "An extraneous variable that may impact the relationship between the other two."),
  ("Population versus sample?", "Population is everyone in a defined setting; a sample is a subset of it."),
  ("Primary versus secondary research?", "Primary collects its own data; secondary analyses data that already exists."),
  ("Three purposes of research?", "Exploration, description, explanation."),
  ("Define epidemiology.", "The study of the distribution and determinants of health-related states among specified populations."),
  ("Which body publishes the Demographic Yearbook?", "The United Nations."),
  ("What does the Vital Statistics System collect?", "Births, deaths, causes of death, marriages and divorces."),
  ("What is the Behavioral Risk Factor Surveillance Survey?", "A telephone survey of risk behaviours, chronic conditions and preventive service use."),
  ("What is the particular value of a disease registry?", "It shows trends over time."),
  ("Eminence-based medicine is?", "Senior colleagues who hold experience to trump evidence."),
  ("Nervousness-based medicine is?", "Fear of litigation driving over-investigation and overtreatment."),
  ("Diffidence-based medicine is?", "Being too timid to make any decision."),
  ("The five As, in order?", "Ask, Acquire, Appraise, Apply, Assess."),
 ]),

 ("medlit-evidence", "Evidence", "accent2", BOOK_ICON, [
  ("Where did evidence-based medicine originate?", "McMaster University, in the 1970s."),
  ("Who provided the core concepts and definition?", "Dr David Sackett."),
  ("What did Dr Archie Cochrane advocate?", "Randomised controlled trials and systematic reviews to verify treatment effectiveness."),
  ("Define evidence-based medicine.", "The conscientious, explicit and judicious use of current best evidence in decisions about individual patients."),
  ("What does its practice integrate?", "Individual clinical expertise with the best available external clinical evidence."),
  ("Three inputs to good clinical decision making?", "Clinical expertise, external clinical evidence, patient values and preferences."),
  ("Five challenges of implementing it?", "Time to search, evidence unavailable, conflicting, outdated, and written in difficult language."),
  ("Descriptive evidence answers what?", "What are the characteristics of patients with a specific diagnosis."),
  ("Assessment evidence answers what?", "Which tests are most effective at identifying or predicting a diagnosis."),
  ("Treatment evidence answers what?", "Which treatments are most effective for a diagnosis in a population."),
  ("Three properties of higher-level evidence?", "Least vulnerable to bias, more generalisable, outcomes attributable to the construct studied."),
  ("What sits at the base of the pyramid?", "Background information and expert opinion."),
  ("What sits at the apex?", "Systematic reviews."),
  ("What sits immediately below randomised trials?", "Cohort studies."),
  ("Which levels count as filtered information?", "Systematic reviews, critically appraised topics, critically appraised individual articles."),
  ("What does filtered mean?", "Someone has already appraised the primary studies for you."),
  ("Define a systematic review.", "Systematically identifying and evaluating multiple studies to answer one specific, focused question."),
  ("Define a meta-analysis.", "Pooling data from multiple studies to produce a single large study."),
  ("Why pool data?", "A greater number of participants usually means greater power."),
  ("How does USPSTF define certainty?", "The likelihood that its assessment of net benefit is correct."),
  ("Define net benefit.", "Benefit minus harm of the service in a general primary care population."),
  ("High certainty means?", "Consistent results from well-designed studies in representative populations; future studies unlikely to change it."),
  ("Low certainty means?", "Evidence insufficient to assess effects on health outcomes."),
  ("Grade A?", "High certainty of substantial net benefit &mdash; offer or provide."),
  ("Grade B?", "High certainty of moderate benefit, or moderate certainty of moderate to substantial &mdash; offer or provide."),
  ("Grade C?", "At least moderate certainty of small net benefit &mdash; offer selectively."),
  ("Grade D?", "Moderate or high certainty of no net benefit, or harms outweigh benefits &mdash; discourage."),
  ("Grade I?", "Evidence insufficient; the balance cannot be determined."),
  ("Which two grades share the same instruction?", "A and B &mdash; offer or provide the service."),
  ("D versus I?", "D is a finding against the service; I is the absence of a finding either way."),
  ("Markers of a quality source?", "Peer-reviewed and government databases; be cautious of websites."),
  ("The ABCD method stands for?", "Author, Bias, Content, Date."),
  ("What does the C ask about?", "Level of detail."),
  ("What does the D ask about?", "Whether the material is still current."),
  ("Which library test appraises websites?", "The CRAAP test."),
  ("Which database holds original articles?", "Medline and PubMed, from the National Library of Medicine."),
  ("Which library holds systematic reviews?", "The Cochrane Library."),
  ("Which agency links to the USPSTF?", "The Agency for Healthcare Research and Quality."),
  ("What does the MMWR carry?", "Public health policies for prevention and treatment."),
  ("Three elements of joint clinical decision making?", "Disclosure of risks and benefits, exploration of patient values, the actual decision."),
  ("First step of evidence-based practice?", "Creating a focused clinical question."),
  ("Accepted substitute for a systematic review?", "An evidence-based synopsis from a credible resource."),
  ("Last step of evidence-based practice?", "Evaluating performance or outcome."),
  ("What does the retracted vaccine and autism study teach?", "Publication in a respected journal does not guarantee integrity."),
 ]),

 ("medlit-design", "Study Design", "accent3", FLASK_ICON, [
  ("Qualitative research is?", "Naturalistic and inductive, developing descriptions."),
  ("Quantitative research is?", "Positivistic and deductive, developing predictions."),
  ("Qualitative data are?", "Observation, field notes, audio recordings."),
  ("Quantitative data are?", "Numerical, objective, measurable."),
  ("Four qualitative examples?", "Case study, biography, ethnography, phenomenology."),
  ("Define study design.", "The organisation and plan for data collection and analysis."),
  ("The design chain?", "Strong design gives strong data, which gives valid, reliable results and conclusions."),
  ("Descriptive design does what?", "Describes characteristics of a group of people."),
  ("Two descriptive examples?", "Case report and case series."),
  ("Analytic design does what?", "Compares two or more groups to draw inference for a population."),
  ("Three analytic examples?", "Randomised controlled trials, cohort, case control."),
  ("Experimental design means?", "The investigator assigns and manipulates the intervention."),
  ("Observational design means?", "The exposure is observed rather than assigned."),
  ("Where does cross-sectional sit?", "Under both descriptive and analytic; always observational."),
  ("Longitudinal research measures?", "Changes over time."),
  ("Policy research determines?", "Whether a programme works or a policy is helpful."),
  ("Quasi-experimental means?", "The researcher controls treatment but not assignment to groups."),
  ("Where is field research used?", "In epidemiology during investigations &mdash; new screening tests, vaccine trials."),
  ("Goal of epidemiologic research design?", "An unbiased comparison between a group with the factor and one without."),
  ("Four things a good design allows?", "Group comparison, quantifying risk difference, determining temporal sequence, minimising bias."),
  ("Typical study sequence?", "Clinical observations, available data, case-control, cohort, randomised trials."),
  ("Cross-sectional design is for?", "Generating hypotheses."),
  ("When is cross-sectional data obtained?", "At a single point in time &mdash; risk factor and disease measured together."),
  ("Why can cross-sectional not show sequence?", "Risk factor and disease are measured at the same time."),
  ("Ecologic studies use what data?", "Population level rather than individual level."),
  ("Define the ecologic fallacy.", "Applying aggregate data to an individual."),
  ("The 1996 Atlanta Olympics asthma finding is what design?", "A cross-sectional ecologic study."),
  ("Case-control groups are defined by?", "Outcome &mdash; disease or no disease."),
  ("Which direction does case-control look?", "Backward, from outcome to exposure."),
  ("Case-control can do what with hypotheses?", "Generate or test them."),
  ("Define a cohort.", "A group with a common characteristic assembled at a similar point and followed over time."),
  ("Cohort groups are defined by?", "Exposure rather than outcome."),
  ("How should the cohort comparison group be chosen?", "As similar as possible except for the exposure."),
  ("Why must cohort follow-up be complete?", "So attrition does not falsely skew the outcome data."),
  ("Prospective (concurrent) cohort?", "Assemble groups now by exposure, collect baseline data, follow forward."),
  ("Retrospective (historical) cohort?", "Go back in history to define a risk group and follow it to the present."),
  ("Cohort studies are for?", "Testing hypotheses."),
  ("A randomised controlled trial is what kind of design?", "Experimental, for testing hypotheses."),
  ("What blinding is possible in a trial?", "Single or double."),
  ("What must a trial account for?", "Withdrawals and drop-outs."),
  ("What do stronger designs prove?", "Cause and effect; weaker ones prove relationships or predictability."),
  ("Do weaker designs have a use?", "Yes &mdash; all studies serve a purpose and can guide practice."),
 ]),

 ("medlit-rates", "Rates &amp; Measurement", "accent4", CHART_ICON, [
  ("Define a rate.", "The number of times an event occurs during a fixed time period."),
  ("Why use rates rather than counts?", "Rates allow comparisons."),
  ("Crude mortality rate measures?", "Deaths from all causes in a population."),
  ("Denominator of the crude death rate?", "The mid-interval population."),
  ("Cause-specific death rate?", "Deaths from a specified cause over the mid-interval population."),
  ("Age-specific mortality rate?", "Mortality limited to a particular age group."),
  ("Why is proportionate mortality not a rate?", "Its denominator is deaths rather than population."),
  ("What must proportionate mortality sum to?", "One hundred per cent."),
  ("Which measure compares health between nations?", "The infant mortality rate."),
  ("Infant mortality rate?", "Deaths under one year over live births, times 1,000."),
  ("Neonatal mortality rate covers which ages?", "Under 28 days."),
  ("Postneonatal mortality rate covers which ages?", "28 to 364 days."),
  ("Denominator of the maternal mortality rate?", "Live births, times 100,000."),
  ("Death-to-case ratio compares?", "Deaths from a cause against new cases of it."),
  ("Case fatality measures?", "Disease severity &mdash; the proportion diagnosed who die from it."),
  ("Years of potential life lost weights what?", "Age at death &mdash; dying young loses more productive years."),
  ("Why does an age-adjusted rate differ from a crude one?", "It removes the effect of the population&rsquo;s age structure."),
  ("Define prevalence.", "The portion of a group with a condition at a point in time."),
  ("Define incidence.", "The portion who develop a condition over a period &mdash; new cases in previously healthy people."),
  ("Point versus period prevalence?", "Point is a single moment per person; period counts cases present during a time span."),
  ("Cumulative incidence?", "New cases over time in a group of fixed size."),
  ("Incidence density?", "New cases over time in a changing population."),
  ("Denominator of incidence density?", "Person-time."),
  ("One person followed 10 years contributes?", "Ten person-years."),
  ("Where does incidence density error arise?", "Variation in duration of follow-up."),
  ("Chronic disease: which is larger?", "Prevalence &mdash; incidence is usually lower."),
  ("Acute illness: which is larger?", "Incidence &mdash; prevalence may be lower because people recover."),
  ("Prevalence study is also called?", "A cross-sectional study."),
  ("Incidence study is also called?", "A cohort study."),
  ("The Framingham Heart Study is which design?", "An incidence, or cohort, study."),
  ("The SchoolNuts study is which design?", "A prevalence, or cross-sectional, study."),
  ("Two clinical uses of prevalence?", "Prioritising the differential, and setting the pretest probability."),
  ("Why does case definition matter?", "Most clinical information is on a continuum, so where the line falls changes measured frequency."),
  ("Who belongs in the population at risk?", "Only those susceptible to the disease or outcome."),
  ("Random sample?", "Each individual has an equal chance of selection."),
  ("Probability sample?", "Each has a known probability, which may or may not be equal."),
  ("Convenience sample?", "Non-random, convenient to obtain."),
  ("Grab sample?", "Researchers take whoever they can find."),
  ("Three levels of disease distribution?", "Person, place, time."),
  ("Endemic means?", "Disease limited by geographic location."),
  ("Epidemic means?", "A concentration of new cases in a given time."),
  ("Pandemic means?", "Widespread cases; may develop rapidly or slowly."),
  ("Surveillance may be?", "Active or passive."),
  ("Why does surveillance need a baseline?", "Without it, a rise in cases cannot be recognised as a rise."),
  ("Which designs let surveillance test aetiology?", "Case-control or cohort studies."),
  ("Why is mortality a surveillance strategy?", "Some cases are detected only at death."),
  ("What is an epi curve?", "The number of cases plotted against time."),
  ("Last step of an outbreak investigation?", "Deciding the outbreak is over."),
  ("The 1976 Philadelphia Legionnaires&rsquo; outbreak illustrates?", "The classic epi curve, following an American Legion convention."),
 ]),

 ("medlit-data", "Data &amp; Variation", "accent5", RULER_ICON, [
  ("Three types of data?", "Nominal, ordinal, interval."),
  ("Nominal data?", "Categories without any specified order."),
  ("Nominal examples?", "Blood group, eye colour."),
  ("Dichotomous data?", "Nominal data divided into two categories &mdash; yes/no, present/absent."),
  ("Ordinal data?", "Some order to the categories, but no defined intervals between them."),
  ("Ordinal examples?", "Cancer staging I&ndash;IV, pitting oedema 1+ to 4+."),
  ("What can you say about two ordinal values?", "Whether one is more, less or equally desirable &mdash; not by how much."),
  ("Interval data?", "Order with defined, equal intervals."),
  ("Continuous data?", "Can take any value in a continuum, limited by the precision of measurement."),
  ("Discrete data?", "Takes only specific values &mdash; number of children, number of heart attacks."),
  ("Define validity in measurement.", "The degree to which data measure what they are supposed to measure; accuracy."),
  ("Define reliability.", "Consistency &mdash; repeated attempts produce similar results."),
  ("Other names for reliability?", "Reproducibility, repeatability, precision."),
  ("How is validity ensured?", "Calibrating devices and comparing results against known values."),
  ("How is validity approached for subjective measures?", "Structured questions &mdash; CAGE questionnaires, pain scales."),
  ("Content validity?", "Includes all relevant dimensions while excluding irrelevant information."),
  ("Criterion validity?", "The measurement predicts or is associated with an observable response or event."),
  ("Construct validity?", "The measurement relates to others believed part of the same phenomenon."),
  ("Low validity with high reliability looks like?", "A tight cluster of results, all away from the true value."),
  ("Intrasubject variation?", "Variation within one person &mdash; biological, time of day, position, stress."),
  ("Intraobserver variation?", "One observer interpreting the same thing differently on two occasions."),
  ("Interobserver variation?", "Two observers reading the same finding differently."),
  ("True biologic variation is due to?", "Many unknown factors each contributing a small random effect."),
  ("Systematic variation is?", "Variation when the conditions of measurement are known to affect the values."),
  ("Systematic variation examples?", "Time of day, after a cigarette, patient position, white coat phenomenon."),
  ("Random measurement error causes?", "A lack of reliability."),
  ("Systematic measurement error causes?", "A lack of validity."),
  ("Three sources of intra-patient variation?", "True biologic variation, measurement error, biologic change representing disease."),
  ("When should intervention be considered?", "Only when there is a true pathological change."),
  ("What does random variation do across many measurements?", "Balances out &mdash; no net misrepresentation of the true state."),
  ("How is random variation reduced?", "By taking an average."),
  ("What does systematic variation do?", "Biases the results."),
  ("Frequency distributions portray?", "The quantity of each category, class or interval."),
  ("Two ways to describe a distribution?", "Central tendency and dispersion."),
  ("Define the mean.", "Sum of all values divided by the number of observations."),
  ("Weakness of the mean?", "It can be affected by extreme outliers."),
  ("Define the median.", "The middle score, half above and half below."),
  ("Define the mode.", "The most frequently occurring value."),
  ("Define the range.", "All values from the lowest to the highest."),
  ("Define the interquartile range.", "A limited range index &mdash; for example the 25th to 75th percentiles."),
  ("Define the standard deviation.", "The variability of the scores about the mean."),
  ("What falls within 1 standard deviation?", "About two thirds of the values."),
  ("What falls within 2 standard deviations?", "About 95 per cent of the values."),
  ("The normal distribution is based on?", "Mathematical theory, not actual measurement."),
  ("Other names for the normal distribution?", "Gaussian, or the bell curve."),
  ("Why is there no clear point where disease begins?", "Disease is often acquired by degrees."),
  ("The progression to death runs?", "Susceptibility, pre-symptomatic, clinical disease, dysfunction, death."),
  ("Does statistical abnormality mean clinical abnormality?", "No &mdash; a cholesterol of 201 is above desired but not in itself significant."),
  ("Abnormal finding without being sick &mdash; example?", "A sickle cell trait carrier."),
  ("Which value extremes are desirable?", "The lower end of systolic pressure; the higher end of high-density lipoprotein."),
  ("Does a normal test rule out disease?", "No."),
  ("Why repeat an abnormal test?", "Regression to the mean."),
  ("What is said of normal/abnormal cutoffs?", "They are often arbitrary &mdash; be careful of labelling."),
 ]),

 ("medlit-tests", "Diagnostic Tests", "accent1", GRID_ICON, [
  ("Diagnostic tests are for whom?", "Symptomatic individuals."),
  ("Screening tests are for whom?", "Asymptomatic individuals."),
  ("Which is more frequent?", "Uncommon presentations of common disease, over common presentations of uncommon disease."),
  ("Five considerations before ordering a test?", "Avoid indiscriminate ordering, risk to benefit, know the limits, avoid repeating without indication, consider cost."),
  ("Define a gold standard test.", "A diagnostic procedure believed to identify the disease with certainty."),
  ("Four gold standard examples?", "Culture for strep throat, biopsy for cancer, catheterisation for coronary disease, endoscopy for peptic ulcer."),
  ("Four gold standard limitations?", "Often expensive, invasive or risky, not acceptable to patients, not easily completed."),
  ("Define sensitivity.", "The probability a person with disease has a positive test result."),
  ("Define specificity.", "The probability a person without disease has a negative test result."),
  ("Sensitivity formula?", "TP / (TP + FN), or a / (a + c)."),
  ("Specificity formula?", "TN / (TN + FP), or d / (b + d)."),
  ("Define positive predictive value.", "The probability a person with a positive result has the disease."),
  ("Define negative predictive value.", "The probability a person with a negative result is disease free."),
  ("PPV formula?", "TP / (TP + FP), or a / (a + b)."),
  ("NPV formula?", "TN / (TN + FN), or d / (c + d)."),
  ("Prevalence in the lettered cells?", "(a + c) / (a + b + c + d)."),
  ("Which cell is a?", "True positives."),
  ("Which cell is b?", "False positives."),
  ("Which cell is c?", "False negatives."),
  ("Which cell is d?", "True negatives."),
  ("What does SnOUT mean?", "A negative result on a highly sensitive test rules disease out."),
  ("What does SpIN mean?", "A positive result on a highly specific test rules disease in."),
  ("When does high sensitivity matter most?", "When missing the disease would have serious consequences."),
  ("When does high specificity matter most?", "When false positives would lead to risky or expensive work-ups."),
  ("How are sensitivity and specificity related?", "Inversely."),
  ("What does an ROC curve plot?", "True positive rate against false positive rate."),
  ("Which ROC curve marks the better test?", "The one closest to the upper left, with the greatest area beneath it."),
  ("What else does an ROC curve help set?", "The cutoff point."),
  ("Are sensitivity and specificity affected by prevalence?", "No &mdash; they are fairly fixed characteristics of the test."),
  ("Are predictive values affected by prevalence?", "Yes &mdash; their calculations include both diseased and healthy people."),
  ("Screening campaign strategy?", "Screen with a highly sensitive test and confirm with a highly specific one."),
  ("As prevalence falls, PPV does what?", "Falls &mdash; and NPV rises."),
  ("As prevalence rises, PPV does what?", "Rises &mdash; and NPV falls."),
  ("Low prevalence produces more of what?", "False positives."),
  ("Define pretest probability.", "The chance the patient has the disease based on what is known before the test."),
  ("Define posttest probability.", "The chance the patient has the disease after the test; it informs treatment decisions."),
  ("What does a likelihood ratio describe?", "How much a test result changes the probability the patient has the condition."),
  ("Is a likelihood ratio affected by prevalence?", "No."),
  ("LR+ formula?", "Sensitivity / (1 &minus; specificity)."),
  ("LR&minus; formula?", "(1 &minus; sensitivity) / specificity."),
  ("An LR+ of 4 means?", "A positive result makes the condition four times more likely than the pretest probability."),
  ("An LR&minus; of 0.5 means?", "A negative result makes the condition half as likely."),
  ("LR above 10 means?", "Strong evidence to rule the disease in."),
  ("LR of 5 to 10 means?", "Moderate evidence to rule in."),
  ("LR of 0.5 to 2 means?", "Indeterminate."),
  ("LR of 0.2 to 0.5 means?", "Weak evidence to rule out."),
  ("LR of 0.1 to 0.2 means?", "Moderate evidence to rule out."),
  ("LR below 0.1 means?", "Strong evidence to rule the disease out."),
  ("Rule of thumb for an LR of 10?", "Posttest probability increases about 45 percentage points."),
  ("Rule of thumb for an LR of 0.1?", "Posttest probability decreases about 45 percentage points."),
  ("How is the rule-of-thumb shift applied?", "It is added to the pretest probability."),
  ("Mathematical route to posttest probability?", "Convert pretest probability to odds, multiply by the LR, convert back."),
  ("How is the nomogram read?", "Draw a straight line from pretest probability through the LR to the right-hand column."),
  ("When does a very high LR rule disease in?", "When the pretest probability lies between 30 and 70 per cent."),
  ("Caution with likelihood ratios?", "Even a high LR test can mislead when the disease has a low prevalence."),
  ("Which tool gives pretest probability for strep throat?", "The modified Centor score."),
  ("Which Centor criterion can score minus one?", "Age over 45."),
  ("Parallel testing means?", "All tests conducted at once, when rapid diagnosis is preferred."),
  ("Parallel testing increases?", "Sensitivity and negative predictive value."),
  ("What determines the sensitivity gain in parallel testing?", "How well each test detects cases the other misses."),
  ("Serial testing means?", "Tests one after another, when speed matters less or tests are risky or costly."),
  ("Serial testing increases?", "Specificity and positive predictive value &mdash; and lowers sensitivity and NPV."),
  ("Which test goes first in serial testing?", "The one with the highest specificity, unless another is cheaper or less risky."),
  ("Serial testing example?", "Exercise tolerance test, then cardiac catheterisation if positive."),
  ("Trade-off of serial over parallel?", "Fewer tests used, but more time taken."),
 ]),
]


def json_str(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def js(decks):
    out = []
    for did, name, colour, icon, cards in decks:
        rows = "\n".join('      [%s, %s],' % (json_str(q), json_str(a)) for q, a in cards)
        out.append('  { id: "%s", name: "%s", color: "%s",\n'
                   "    icon: '%s',\n"
                   "    cards: [\n%s\n    ]},\n" % (did, name, colour, icon, rows))
    return "\n".join(out)


def main():
    src = open(ARCADE, encoding="utf-8").read()
    block = OPEN + "\n" + js(DECKS) + CLOSE

    if OPEN in src:
        src = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), lambda _m: block, src, flags=re.S)
    else:
        # Inside DEMO_DECKS, anchored to its own closing bracket -- a deck placed
        # after the array closes is still valid JavaScript, so nothing complains,
        # but findDeck() never sees it. See the note in add_cms_e3_arcade.py.
        decl = src.index("var DEMO_DECKS = [")
        end = src.index("\n];", decl)
        src = src[:end] + "\n\n" + block + src[end:]

    # Register the group. This course has no group yet, so create one, placed
    # after Clinical Pathophysiology I to keep the Fall classes adjacent.
    deck_ids = ", ".join('"%s"' % d[0] for d in DECKS)
    group = ('  { id: "med-lit", name: "Interpretation of Medical Literature", exams: [\n'
             '    { id: "exam1", name: "Exam", deckIds: [%s] }\n'
             '  ]},\n' % deck_ids)
    if 'id: "med-lit"' in src:
        src = re.sub(r'  \{ id: "med-lit", name: "Interpretation of Medical Literature", exams: \[.*?\n  \]\},\n',
                     lambda _m: group, src, flags=re.S)
    else:
        anchor = '\n  { id: "cms-1", name: "Clinical Medicine and Surgery I", exams: ['
        assert src.count(anchor) == 1, "could not place the group uniquely"
        src = src.replace(anchor, "\n" + group + anchor)

    # Every deck must sit INSIDE DEMO_DECKS, and the group must sit outside it.
    d0 = src.index("var DEMO_DECKS = [")
    d1 = src.index("\n];", d0)
    for did, *_ in DECKS:
        at = src.index('id: "%s"' % did)
        assert d0 < at < d1, "%s was placed OUTSIDE the DEMO_DECKS array" % did
    assert src.index('id: "med-lit"') > d1, "the group was placed INSIDE DEMO_DECKS"

    open(ARCADE, "w", encoding="utf-8").write(src)
    n = sum(len(d[4]) for d in DECKS)
    print("wrote %d decks, %d cards into arcade.js" % (len(DECKS), n))
    for did, name, _c, _i, cards in DECKS:
        print("   %-18s %-28s %d cards" % (did, re.sub("&[a-z]+;", "&", name), len(cards)))


if __name__ == "__main__":
    main()
