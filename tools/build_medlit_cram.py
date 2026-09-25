#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Interpretation of Medical Literature cram sheet.

Condensed from the study guide, per the template README: compress what the
guide already says, do not add anything new, and keep numbers and names
verbatim. Six topics, matching the guide's six deck sections.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

topics = [
{"id": "bias", "label": "Bias, Chance & Validity", "color": "#7a2d47", "rows": [
 ["Bias", "<b>Systematic</b> error producing conclusions that differ from the truth. Can enter at conception/design, data collection, analysis or interpretation. Potential for bias does not mean bias is present &mdash; but it is often detectable when reading the article."],
 ["Chance", "<b>Random</b> variation. Equally likely above or below the truth. Reduced by good design, estimated statistically, <b>never eliminated</b>. May coexist with bias."],
 ["Telling them apart", "Readings that all fall on <i>one</i> side of the true value = bias. Random variation would scatter both ways."],
 ["Selection (sampling) bias", "Compared groups differ in more ways affecting the outcome than the study's focus. Consider at <b>study design</b>. Example: surgical arm healthy enough to tolerate surgery, medical arm sicker."],
 ["Measurement bias", "The method of measurement gives incorrect results &mdash; blood pressure taken without a standardized procedure every time."],
 ["Confounding", "The covariate's effect cannot be separated from the variable studied. Associated with <b>both</b> exposure and outcome; <b>need not cause</b> the disease. Consider at <b>data analysis</b>. May result from selection bias or chance."],
 ["Procedural bias", "Interview/questionnaire results affected by method of delivery &mdash; a post-op questionnaire while anesthesia is wearing off."],
 ["Attrition effect", "Participants drop out; reduces sample size."],
 ["Non-response bias", "Responders differ from non-responders; may not reflect the population."],
 ["Performance bias", "Care differs between groups other than the topic of interest &mdash; controls seeking other treatment. <b>Blinding participants protects against it.</b>"],
 ["Reporting vs publication bias", "<b>Reporting</b> = only a subset of the data is made available (the study appears, not all its findings). <b>Publication</b> = non-significant research is less likely to be published, via editor preference and sponsors avoiding unfavorable results."],
 ["Conflict of interest", "Financial or personal considerations affecting objectivity; impact may be conscious <b>or unconscious</b>; should be disclosed by authors."],
 ["The statistics limit", "Analysis estimates the effect of <b>chance</b>. <b>No analysis corrects for unknown bias.</b> Statistics on a poor design give a false sense of respectability."],
 ["Internal validity", "Degree results are correct <b>for the sample studied</b>. &ldquo;Are the conclusions valid for these people?&rdquo;"],
 ["External validity", "Degree results are true <b>in other settings</b> &mdash; <b>generalisability</b>. &ldquo;Does the sample represent my patients?&rdquo; Rarely determined from a single study."],
 ["Variables", "Independent = possible <b>cause</b>. Dependent = possible <b>effect</b>. Extraneous (covariate) = may impact the relationship."],
 ["Primary vs secondary research", "Primary collects its own data (questionnaires, surveys, measurements, labs) &rarr; original articles. Secondary analyses existing data &rarr; meta-analyses, systematic reviews."],
]},

{"id": "evidence", "label": "Evidence & the Hierarchy", "color": "#8a5a2b", "rows": [
 ["Origins", "<b>McMaster University, 1970s.</b> <b>Sackett</b> gave the core concepts and definition; <b>Cochrane</b> advocated randomized trials and systematic reviews to verify treatment effectiveness."],
 ["Definition", "The conscientious, explicit and judicious use of current best evidence in decisions about individual patients &mdash; integrating <b>clinical expertise</b> with <b>external evidence</b>, and considering the <b>patient's situation and preferences</b>."],
 ["Five challenges", "Searching takes time &middot; evidence unavailable &middot; conflicting &middot; outdated &middot; written in language clinicians struggle with."],
 ["Three types of evidence", "<b>Descriptive</b> (characteristics of patients with a diagnosis) &middot; <b>Assessment</b> (which tests identify/predict it) &middot; <b>Treatment</b> (what works, in whom)."],
 ["Higher levels are&hellip;", "Least vulnerable to bias &middot; more generalizable &middot; outcomes more likely attributable to the construct studied."],
 ["Pyramid, base to apex", "Expert opinion/background &rarr; case-control, case series/reports &rarr; cohort &rarr; randomized controlled trials &rarr; <span style='white-space:nowrap'>critically-appraised articles</span> &rarr; critically-appraised topics &rarr; <b>systematic reviews</b>. (The laboratory version adds in vitro and animal research below case reports.)"],
 ["Filtered vs unfiltered", "<b>Filtered</b> = already appraised for you (systematic reviews, critically-appraised topics and articles). <b>Unfiltered</b> = primary studies you appraise yourself (randomized trials, cohort, case-control)."],
 ["Systematic review vs meta-analysis", "<b>Review</b> identifies and evaluates multiple studies for one specific, focused question. <b>Meta-analysis</b> pools their data into a single large study &mdash; greater <i>n</i> usually means greater power."],
 ["USPSTF certainty", "= the likelihood the <b>net benefit</b> assessment is correct. Net benefit = benefit minus harm in a general primary care population. <b>High</b> = consistent results, representative populations, future studies unlikely to change it. <b>Moderate</b> = sufficient but constrained (number/size/quality, inconsistency, generalisability, coherence). <b>Low</b> = insufficient to assess effects."],
 ["USPSTF grades", "<b>A</b> high certainty, substantial benefit &rarr; offer. <b>B</b> high certainty moderate, or moderate certainty moderate-to-substantial &rarr; offer. <b>C</b> at least moderate certainty of <i>small</i> benefit &rarr; offer <i>selectively</i>. <b>D</b> moderate/high certainty of no net benefit or net harm &rarr; <i>discourage</i>. <b>I</b> insufficient evidence &rarr; balance cannot be determined."],
 ["D vs I", "<b>D</b> is a finding <i>against</i> the service. <b>I</b> is the <i>absence</i> of a finding either way."],
 ["Judging sources", "Peer-reviewed and government databases; <b>be cautious of websites</b>. <b>ABCD:</b> Author (credentials) &middot; Bias &middot; Content (level of detail) &middot; Date (still current?). The library's <b>CRAAP test</b> does the same job."],
 ["Databases", "<b>Medline/PubMed</b> (National Library of Medicine, original articles) &middot; <b>Cochrane Library</b> (systematic reviews) &middot; Evidence Based Medicine Reviews &middot; Up-To-Date, TripPro, Clinical Key, Essential Evidence Plus &middot; ACP Journal Club. <b>Guidelines:</b> AHRQ (links to USPSTF), MMWR, Task Force on Community Preventive Services."],
 ["Steps to EBP", "Focused clinical question &rarr; systematic review <i>or an evidence-based synopsis from a credible resource</i> &rarr; evaluate validity &rarr; apply to the patient &rarr; evaluate outcome."],
 ["Joint decision making", "Disclosure of risks and benefits &rarr; exploration of patient values &rarr; the actual decision."],
]},

{"id": "design", "label": "Study Design", "color": "#2f5d6b", "rows": [
 ["Qualitative vs quantitative", "<b>Qualitative</b>: naturalistic, inductive, develops <i>descriptions</i>; data are observation, field notes, recordings; case study, biography, ethnography, phenomenology. <b>Quantitative</b>: positivistic, deductive, develops <i>predictions</i>; numerical, objective, measurable; trials, cohort, case-control."],
 ["Study design", "The organization and plan for data collection and analysis. <b>Strong design &rarr; strong data &rarr; valid, reliable results.</b>"],
 ["Descriptive vs analytic", "<b>Descriptive</b> describes one group (case report, case series). <b>Analytic</b> compares two or more groups to draw inference for a population (randomized trials, cohort, case-control)."],
 ["Experimental vs observational", "<b>Experimental</b>: the investigator <i>assigns and manipulates</i> the intervention (randomized trial). <b>Observational</b>: the exposure is <i>observed</i> (cohort, case-control). Cross-sectional is observational and appears under both descriptive and analytic."],
 ["Other methods", "<b>Longitudinal</b> (changes over time) &middot; <b>survey</b> &middot; <b>policy research/evaluation</b> &mdash; all observational. <b>Quasi-experimental</b>: controls treatment but <i>not</i> assignment. <b>Field research</b> (epidemiologic investigations, new screening tests, vaccine trials): either."],
 ["Design goal", "An <b>unbiased comparison</b> between a group with the factor and one without. Good design permits group comparison, quantification of risk difference, <b>determination of temporal sequence</b>, and minimized bias."],
 ["Cross-sectional", "Observational, <b>generates</b> hypotheses. Single point in time; risk factor and disease measured <i>together</i>, so temporal sequence cannot be established. <b>Ecologic</b> versions use population-level data &mdash; beware the <b>ecologic fallacy</b> (applying aggregate data to an individual)."],
 ["Case-control", "Observational; generates <i>or</i> tests hypotheses. Groups defined by <b>outcome</b>, then assessed for a difference in exposure. Looks <b>backward</b>."],
 ["Cohort", "Observational; <b>tests</b> hypotheses. Groups defined by <b>exposure</b>, followed forward. Comparison group as similar as possible <i>except for the exposure</i>. Follow long enough for the outcome and <b>completely</b>, so attrition does not skew it. <b>Prospective (concurrent)</b> assembles now; <b>retrospective (historical)</b> defines a past risk group and follows it to the present."],
 ["Randomized controlled trial", "Experimental; tests hypotheses. Clear hypothesis, protocol, results applicable to a larger population, <b>random assignment</b>, single or double blinding, adequate sample size, accounts for withdrawals and drop-outs."],
 ["Design hierarchy", "Some designs are stronger: they prove <b>cause and effect</b>; weaker ones prove <b>relationships or predictability</b>. All studies serve a purpose and can guide practice."],
 ["Typical sequence", "Clinical observations &rarr; available data &rarr; case-control &rarr; cohort &rarr; randomized trials."],
]},

{"id": "rates", "label": "Rates, Incidence & Prevalence", "color": "#1f5c3a", "rows": [
 ["Rate", "The number of times an event occurs during a fixed time period. <b>Rates allow comparisons</b> &mdash; that is why they exist rather than raw counts."],
 ["Crude death rate", "All deaths &divide; <b>mid-interval population</b> &times;1,000 or 100,000. <b>Age-adjusted</b> removes the effect of age structure (US 2009: crude ~794, adjusted 741 per 100,000)."],
 ["Cause- and age-specific", "<b>Cause-specific</b>: deaths from one cause &divide; mid-interval population &times;100,000. <b>Age-specific</b>: limited to one age group."],
 ["Proportionate mortality", "Deaths from a cause &divide; <b>total deaths</b> &times;100. <b>NOT a rate</b> &mdash; the denominator is deaths, not population. All causes must sum to <b>100%</b>. (CVD ~24.5% of US deaths.)"],
 ["Death-to-case ratio", "Deaths from a cause &divide; <b>new cases</b> of the same disease &times;100."],
 ["Maternal & child rates", "All take <b>live births</b> as the denominator. <b>Neonatal</b> &lt;28 days &middot; <b>postneonatal</b> 28&ndash;364 days &middot; <b>infant</b> &lt;1 year (&times;1,000) &middot; <b>maternal</b> pregnancy-related deaths (&times;100,000). Infant mortality is the usual international comparison."],
 ["Case fatality / YPLL", "<b>Case fatality</b> = disease <i>severity</i>: proportion diagnosed who die from it. <b>Years of potential life lost</b> = dying young loses more productive years; used to target interventions."],
 ["Prevalence", "Portion of a group <i>with</i> a condition at a point in time &mdash; a snapshot. <b>Point</b> (single moment per person, not necessarily the same date) vs <b>period</b> (cases present during a span). Surveys collect it. Prevalence study = <b>cross-sectional</b> (SchoolNuts)."],
 ["Incidence", "Portion who <i>develop</i> a condition over a period &mdash; <b>new cases in previously healthy people</b>. <b>Cumulative incidence</b> = fixed-size group. <b>Incidence density</b> = changing population, denominator in <b>person-time</b> (1 person &times; 10 years = 10 person-years); error arises from varying follow-up duration. Incidence study = <b>cohort</b> (Framingham, 1948&ndash;)."],
 ["Which is bigger?", "<b>Chronic disease</b>: incidence LOWER than prevalence (cases accumulate). <b>Acute illness</b>: prevalence may be LOWER than incidence (people recover &mdash; the common cold)."],
 ["Prevalence clinically", "Prioritizes the differential (<i>horses, not zebras</i>) and sets the <b>pretest probability</b>."],
 ["What distorts measurement", "<b>Case definition</b> &mdash; most clinical information is on a continuum, so where the line falls changes frequency. <b>Population at risk</b> &mdash; only the susceptible (no men in an ovarian cancer denominator); narrowing it may curtail generalisability."],
 ["Sampling", "<b>Random</b> = equal chance. <b>Probability</b> = known chance, not necessarily equal (useful for subgroups). <b>Convenience</b> = non-random, easy to obtain. <b>Grab</b> = whoever researchers can find."],
 ["Distribution: person, place, time", "<b>Person</b> = profile of those affected, demographics <i>and</i> behavior. <b>Place</b> = <b>endemic</b>, limited by geography. <b>Time</b> = <b>epidemic</b> (new cases concentrated in time) and <b>pandemic</b> (widespread; rapid like 1900s influenza or slow like HIV/AIDS)."],
 ["Surveillance", "Active or passive; national, state, county. Establishes a <b>baseline</b>. Functions: magnitude &middot; natural history &middot; detect outbreaks &middot; document geographic spread &middot; test etiology (via case-control or cohort) &middot; evaluate control &middot; monitor agent change. Strategies: screen high-risk groups &middot; symptoms/syndrome &middot; <b>mortality</b> (some cases detected only at death) &middot; provider reporting &middot; laboratory reporting."],
 ["Outbreak investigation", "Epidemic vs endemic &rarr; attack rate &rarr; establish diagnosis &rarr; <b>case definition</b> &rarr; confirm an epidemic truly exists &rarr; characterize by time, place, person &rarr; <b>epi curve</b> (cases vs time) &rarr; hypotheses about source/type/route &rarr; test &rarr; control measures &rarr; solve source &rarr; <b>decide it is over</b>. (Philadelphia Legionnaires', 1976.)"],
]},

{"id": "data", "label": "Data, Validity & Variation", "color": "#4a3a7a", "rows": [
 ["Three types of data", "<b>Nominal</b> &mdash; categories, no order (blood group, eye color); <b>dichotomous</b> is nominal split in two. <b>Ordinal</b> &mdash; order, <i>no defined intervals</i> (cancer stage I&ndash;IV, edema 1+&ndash;4+); you can say more/less, not by how much. <b>Interval</b> &mdash; order <i>with</i> equal defined intervals; <b>continuous</b> (blood pressure, weight, limited by measurement precision) or <b>discrete</b> (number of children)."],
 ["Validity vs reliability", "<b>Validity</b> (accuracy) = measures what it is supposed to; ensured by calibration against known values, or by structured questions for subjective measures (CAGE, pain scales). <b>Reliability</b> (reproducibility, repeatability, precision) = repeated attempts give similar results. <b>A measure can be reliably wrong.</b>"],
 ["Three validities", "<b>Content</b> &mdash; includes all relevant dimensions, <i>excludes irrelevant</i> ones. <b>Criterion</b> &mdash; predicts/associates with an observable event. <b>Construct</b> &mdash; relates to other measures of the same phenomenon."],
 ["Types of variation", "<b>Intrasubject</b> (within one person) &middot; <b>intraobserver</b> (one reader, two occasions) &middot; <b>interobserver</b> (two readers &mdash; murmur graded 3 vs 4)."],
 ["Biologic vs systematic", "<b>True biologic variation</b> = many <i>unknown</i> factors each with a small <i>random</i> effect. <b>Systematic variation</b> = <i>known</i> conditions affecting the value (time of day, after a cigarette, position, white coat)."],
 ["Measurement error", "<b>Random</b> (chance; equally above or below) &rarr; lack of <b>reliability</b>. <b>Systematic</b> (a flaw in the process) &rarr; lack of <b>validity</b>; determines a range for the true score."],
 ["Intra-patient variation", "May be biologic variation, measurement error, <i>or</i> biologic change representing disease. <b>Intervene only for a true pathological change.</b>"],
 ["Effects of variation", "<b>Random</b> balances out &mdash; reduce by <b>averaging</b>, estimate statistically; individual measurements can still mislead. <b>Systematic will bias results</b>, and averaging does not help."],
 ["Central tendency", "<b>Mean</b> = sum &divide; n; best estimate, but <i>affected by outliers</i>. <b>Median</b> = middle score. <b>Mode</b> = most frequent value."],
 ["Dispersion", "<b>Range</b> = lowest to highest. <b>Interquartile range</b> = limited index, e.g. 25th&ndash;75th percentile. <b>Standard deviation</b> = variability about the mean."],
 ["Normal distribution", "Gaussian / bell curve. <b>~2/3 within 1 SD</b>, <b>95% within 2 SD</b>. <b>Based on mathematical theory, not actual measurement.</b>"],
 ["Normal vs abnormal", "No clear-cut point: <b>susceptibility &rarr; pre-symptomatic &rarr; clinical disease &rarr; dysfunction &rarr; death</b>. Statistical abnormality &ne; clinical abnormality (cholesterol 201). You can be abnormal and well (sickle cell trait). Extremes may be <i>desirable</i> (low systolic, high HDL). <b>A normal test does not rule out disease.</b>"],
 ["Defining abnormality", "Use values associated with <b>disease, disability or death</b>; a clinically recognizable difference from healthy. <b>Repeat abnormal tests</b> &mdash; regression to the mean. Cutoffs are <b>often arbitrary</b>. <b>Be careful of labeling.</b>"],
]},

{"id": "tests", "label": "Diagnostic Tests", "color": "#a3341f", "rows": [
 ["Before ordering", "Horses, not zebras. <b>Uncommon presentations of common disease beat common presentations of rare disease.</b> No disease is rare to the patient who has it. Avoid indiscriminate ordering &middot; risk:benefit &middot; know the limits &middot; do not repeat without indication &middot; consider cost."],
 ["Diagnostic vs screening", "<b>Diagnostic</b> = symptomatic individuals. <b>Screening</b> = asymptomatic individuals."],
 ["Gold standard", "A procedure believed to identify the disease <b>with certainty</b> &mdash; culture for strep, biopsy for cancer, catheterization for coronary disease, endoscopy for peptic ulcer. Often expensive, invasive/risky, unacceptable, or not easily completed, so alternatives are usually the initial choice."],
 ["The 2&times;2, lettered", "<b>a</b> = true positives &middot; <b>b</b> = false positives &middot; <b>c</b> = false negatives &middot; <b>d</b> = true negatives."],
 ["Sensitivity", "Probability a person <i>with</i> disease tests <i>positive</i>. <b>TP/(TP+FN) = a/(a+c)</b>. Read <b>down the disease column</b> &rarr; fixed property of the test."],
 ["Specificity", "Probability a person <i>without</i> disease tests <i>negative</i>. <b>TN/(TN+FP) = d/(b+d)</b>. Read down the no-disease column &rarr; fixed property of the test."],
 ["Predictive values", "<b>PPV</b> = probability a positive result means disease = <b>TP/(TP+FP) = a/(a+b)</b>. <b>NPV</b> = probability a negative result means no disease = <b>TN/(TN+FN) = d/(c+d)</b>. Read <b>across the test rows</b> &rarr; <b>depend on prevalence</b>. Prevalence = (a+c)/(a+b+c+d)."],
 ["SnOUT / SpIN", "<b>Sn-OUT</b>: a <i>negative</i> on a highly <b>sensitive</b> test rules <b>OUT</b> (few false negatives) &mdash; matters when missing disease is dangerous. <b>Sp-IN</b>: a <i>positive</i> on a highly <b>specific</b> test rules <b>IN</b> (few false positives) &mdash; matters when false positives trigger risky or costly work-ups."],
 ["Sensitivity vs specificity", "<b>Inversely related.</b> The <b>ROC curve</b> plots true positive rate against false positive rate (1&minus;specificity); the better test's curve is <b>closest to the upper left</b> with the <b>greatest area beneath</b>, and it also sets the <b>cutoff point</b>. Screening strategy: screen <i>sensitive</i>, confirm <i>specific</i>."],
 ["Prevalence effect", "Same test, sensitivity 99% / specificity 95%: at <b>1%</b> prevalence PPV = <b>17%</b>, NPV 99.9%; at <b>5%</b> prevalence PPV = <b>51%</b>, NPV 97%. As prevalence <i>falls</i>, PPV falls and NPV rises (more false positives). <b>Spectrum bias.</b>"],
 ["Pre- and post-test probability", "<b>Pretest</b> = chance of disease before the test, often the prevalence. <b>Posttest</b> = chance after it; informs treatment."],
 ["Likelihood ratios", "How much a result changes the probability. <b>Not affected by prevalence.</b> <b>LR+ = Sn/(1&minus;Sp)</b> &middot; <b>LR&minus; = (1&minus;Sn)/Sp</b>. LR+ of 4 &rarr; 4&times; more likely; LR&minus; of 0.5 &rarr; half as likely."],
 ["LR bands", "<b>&gt;10</b> strong rule-in (<b>+45%</b>) &middot; <b>5&ndash;10</b> moderate rule-in (+30%) &middot; <b>0.5&ndash;2</b> indeterminate (&plusmn;15%) &middot; <b>0.2&ndash;0.5</b> weak rule-out (&minus;15%) &middot; <b>0.1&ndash;0.2</b> moderate rule-out (&minus;30%) &middot; <b>&lt;0.1</b> strong rule-out (&minus;45%). The shift is <b>added to the pretest probability</b>. A very high LR rules in when pretest probability is <b>30&ndash;70%</b>. <b>Even a high LR misleads at low prevalence.</b>"],
 ["Getting to posttest", "Convert pretest probability &rarr; <b>odds</b>, multiply by the LR &rarr; posttest odds, convert back. Or the <b>nomogram</b>: line from pretest probability through the LR to the right-hand column."],
 ["Worked example", "Rapid strep antigen, Sn 65% / Sp 96%. <b>LR+ = 0.65/0.04 = 16.25</b>; <b>LR&minus; = 0.35/0.96 = 0.36</b>. Pretest from the <b>modified Centor score</b> (fever &gt;38&deg;C, absent cough, tender anterior nodes, tonsillar swelling/exudate = 1 each; age 3&ndash;14 = +1, 15&ndash;44 = 0, &gt;45 = <b>&minus;1</b>). Posttest ~<b>93%</b> positive, ~<b>22%</b> negative."],
 ["Parallel vs serial", "<b>Parallel</b> = all at once, when speed matters; <b>&uarr;sensitivity and NPV</b>; gain depends on how well the tests complement each other. <b>Serial</b> = one after another, when speed matters less or tests are risky/costly; <b>&uarr;specificity and PPV</b>, &darr;sensitivity and NPV; fewer tests, more time. <b>Do the most specific first</b> unless another is cheaper or safer (exercise tolerance test &rarr; catheterization)."],
 ["Appraising a new test", "Disease of interest? Spectrum of patients? What is the test? Did <b>every subject undergo both</b> it and the gold standard? Were the testers <b>blinded</b> to the other result? Benefits and risks reasonable? Sn, Sp, PPV, NPV? <b>Similar prevalence in your population?</b>"],
]},
]

html = render(
    title="Cram Sheet — Interpretation of Medical Literature",
    kicker="Interpretation of Medical Literature · Class of 2028",
    h1="Medical Literature Cram Sheet",
    sub="Sessions 1–4 condensed: the bias taxonomy, the evidence hierarchy and USPSTF grades, "
        "every study design, rates with incidence against prevalence, data and variation, and "
        "the whole of diagnostic test interpretation.",
    topics=topics,
    guide_href="medical-literature-study-guide.html",
    footer_note="Condensed from the Medical Literature Study Guide (Class of 2028). "
                "For the full explanation and the worked examples behind any of these, see the full guide.",
)
out = os.path.join(ROOT, "Interpretation of Medical Literature Exam 1",
                   "medical-literature-cram-sheet.html")
open(out, "w", encoding="utf-8").write(html)
print("wrote", os.path.basename(out), len(html), "bytes,",
      sum(len(t["rows"]) for t in topics), "rows across", len(topics), "topics")
