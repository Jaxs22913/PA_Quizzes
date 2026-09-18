# -*- coding: utf-8 -*-
# Interpretation of Medical Literature, Session 1 (Introduction, Bias and
# Validity, Megan B. Finck) -- pool A: epidemiology and its data sources,
# evidence-based medicine, and the anatomy of a research study. Pool B carries
# the bias taxonomy, chance and validity.
#
# COURSE MECHANICS ARE NOT CONTENT. Slides 2-8 set out the grading weights, the
# required text and the assignment structure. The computerised exam covers the
# assigned readings and the lecture material, so none of that is examinable and
# none of it is here.
#
# The session was not recorded, so every question comes off the slides and
# cites the slide it came from.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "1 PAJ5512 Introduction Bias Validity MBF_2026sc.pptx"
def c(n):  return f"{SRC}, Slide {n}"

IOA = "Identify epidemiologic data sources"
IOB = "Discuss the purposes of research"
IOC = "Discuss internal and external validity"
IOD = "Describe chance and how it affects medical research"
IOE = ("Discuss the various types of bias in medical research including: "
       "selection/sampling bias, measurement bias, confounding, procedural bias, "
       "attrition effect, non-response bias, reporting bias, publication bias")

POOL_A = [

{"topic": "Epidemiology", "io": IOA, "slot": "definition",
 "q": "How is epidemiology defined?",
 "opts": [
  ["The distribution and determinants of health-related states in populations",
   "Correct, and the definition does not stop at studying: it extends to applying that study to the control of health problems, which is what makes it a practical discipline rather than a descriptive one."],
  ["The study of disease mechanisms at the cellular and molecular level",
   "That describes pathophysiology. Epidemiology works at the level of populations rather than mechanisms within an individual."],
  ["The study of how drugs are absorbed, distributed and eliminated",
   "That describes pharmacokinetics. Epidemiology concerns the distribution and determinants of health states across populations."],
  ["The statistical analysis of data collected during a single clinical trial",
   "Statistical analysis is a tool epidemiology uses, not its definition, and epidemiology extends far beyond any one trial."]],
 "c": 0, "cite": c(10)},

{"topic": "Epidemiology", "io": IOA, "slot": "purpose",
 "q": "Which purposes does epidemiology serve in public health practice?",
 "opts": [
  ["Discovering agent, host and environmental factors that affect health",
   "Correct, and two more complete the set: identifying the population segments at greatest risk, and evaluating whether health programmes and services actually improve population health. Ranking the relative importance of causes of illness, disability and death belongs to it too."],
  ["Establishing the diagnosis in an individual patient presenting to clinic",
   "Individual diagnosis is clinical work. Epidemiology addresses populations, and informs individual care only indirectly through what it learns about groups."],
  ["Determining the appropriate dose of a medication for a given patient",
   "Dosing is a pharmacological question. The purposes named for epidemiology concern causes, risk segments and programme evaluation across populations."],
  ["Setting the reimbursement rates paid to hospitals and clinics",
   "Payment policy is not among the named purposes, which centre on identifying causes, risks and the effectiveness of health programmes."]],
 "c": 0, "cite": c(11)},

{"topic": "Epidemiology", "io": IOA, "slot": "contribution",
 "q": "Which of these is named as a contribution of epidemiology to medicine?",
 "opts": [
  ["Determining the natural history of disease",
   "Correct. The list also includes investigating new disease transmission, finding preventable causes, studying the biological spectrum of disease, evaluating community interventions, setting control priorities and providing expert testimony."],
  ["Synthesising new pharmaceutical compounds",
   "Drug synthesis is a laboratory science. Epidemiology contributes by describing disease in populations and evaluating what changes it."],
  ["Performing surgical procedures more safely",
   "Operative technique is not among the named contributions, which concern transmission, causation, natural history and the evaluation of interventions."],
  ["Writing the medical record for an individual encounter",
   "Documentation is a clinical task. The contributions named are population-level: transmission, preventable causes, natural history and programme evaluation."]],
 "c": 0, "cite": c(12)},

{"topic": "Data sources", "io": IOA, "slot": "data source",
 "q": "Which international body publishes the Demographic Yearbook?",
 "opts": [
  ["The United Nations",
   "Correct, and it carries demographic and social statistics. The World Health Organization publishes the separate World Health Statistics Manual, covering health statistics for its member states."],
  ["The World Health Organization",
   "That body publishes the World Health Statistics Manual, which carries health statistics for World Health Organization member states rather than demographic and social statistics."],
  ["The Centers for Disease Control and Prevention",
   "That is a United States agency rather than an international body, and it operates the national disease reporting system."],
  ["The National Center for Health Statistics",
   "That is a United States agency, and it conducts periodic surveys of disease and disability rather than publishing an international yearbook."]],
 "c": 0, "cite": c(13)},

{"topic": "Data sources", "io": IOA, "slot": "data source",
 "q": "What does the United States Vital Statistics System collect?",
 "opts": [
  ["Births, deaths, causes of death, marriages and divorces",
   "Correct. It is the registration system for life events, which is distinct from the population census and from the periodic health surveys run by the National Center for Health Statistics."],
  ["Reportable communicable diseases only",
   "Reportable diseases run through the disease reporting system operated by health departments, not through vital statistics registration of life events."],
  ["Hospital emergency department and discharge data",
   "Hospital data is listed separately among other sources. Vital statistics covers registered life events such as births, deaths, marriages and divorces."],
  ["Self-reported health behaviours gathered by telephone",
   "That describes the Behavioral Risk Factor Surveillance Survey, which is a telephone survey rather than a registration system."]],
 "c": 0, "cite": c(13)},

{"topic": "Data sources", "io": IOA, "slot": "data source",
 "q": "What kind of data does the National Center for Health Statistics gather?",
 "opts": [
  ["Periodic surveys of disease and disability",
   "Correct. Its examples include the National Health Interview Survey and the National Health and Nutrition Examination Survey, both periodic rather than continuous registrations."],
  ["Continuous registration of every birth and death",
   "Birth and death registration belongs to the Vital Statistics System. This agency conducts periodic surveys instead."],
  ["Disease-specific data collected by state governments",
   "Disease-specific collection by state government describes a disease registry, such as a state cancer data system."],
  ["Financial data on health care spending by household",
   "The surveys named concern disease and disability rather than household expenditure."]],
 "c": 0, "cite": c(14)},

{"topic": "Data sources", "io": IOA, "slot": "data source",
 "q": "What is the Behavioral Risk Factor Surveillance Survey?",
 "opts": [
  ["A telephone survey of health-related risk behaviours",
   "Correct, and it also captures chronic health conditions among United States residents, which makes it a behavioural and chronic-disease instrument rather than a registration system. It covers preventive service use as well."],
  ["A registry of cancer cases maintained by state government",
   "That describes a disease registry such as the Connecticut tumour registry or the Florida Cancer Data System."],
  ["A mandatory report filed by clinicians for notifiable diseases",
   "Notifiable disease reporting runs through the disease reporting system rather than through a voluntary telephone survey."],
  ["A physical examination survey conducted in mobile clinics",
   "Physical examination data is collected by the National Health and Nutrition Examination Survey rather than by this telephone instrument."]],
 "c": 0, "cite": c(16)},

{"topic": "Data sources", "io": IOA, "slot": "data source",
 "q": "What is the particular value of a disease registry?",
 "opts": [
  ["It provides information about trends over time",
   "Correct. Registries are usually established by state government to collect disease-specific data, and because collection continues, they show how a disease behaves across years rather than at one moment."],
  ["It measures self-reported behaviour in a representative sample",
   "Self-reported behaviour in a sample describes a survey instrument such as the Behavioral Risk Factor Surveillance Survey."],
  ["It registers every birth and death in the jurisdiction",
   "Life-event registration is the role of the Vital Statistics System rather than of a disease-specific registry."],
  ["It establishes the cause of a disease directly",
   "A registry records cases; establishing causation requires study designs built for the question rather than the registry alone."]],
 "c": 0, "cite": c(16)},

{"topic": "Data sources", "io": IOA, "slot": "data source",
 "q": "Which agency, together with state and county health departments, operates the United States disease reporting system?",
 "opts": [
  ["The Centers for Disease Control and Prevention",
   "Correct. Reportable diseases flow from clinicians through state and county health departments to that agency, which is what makes notifiable-disease lists a usable national data source."],
  ["The United Nations",
   "That is an international body publishing demographic and social statistics rather than operating a United States reporting system."],
  ["The National Center for Health Statistics",
   "That agency conducts periodic surveys of disease and disability rather than operating the notifiable-disease reporting system."],
  ["The World Health Organization",
   "That body compiles health statistics for its member states rather than running the United States disease reporting system."]],
 "c": 0, "cite": c(14)},

{"topic": "Clinical epidemiology", "io": IOA, "slot": "definition",
 "q": "What does clinical epidemiology do?",
 "opts": [
  ["Makes predictions about individual patients from events in groups of similar patients",
   "Correct, and the qualifier matters: strong scientific methods are what make those predictions accurate, so the method by which the group was studied determines how much the prediction is worth."],
  ["Describes disease frequency in a population without reference to individuals",
   "Pure description of populations is general epidemiology. The clinical branch turns group data into predictions about the individual in front of you."],
  ["Replaces the history and physical examination with statistical reasoning",
   "It informs clinical judgement rather than replacing examination, and good decisions still rest on history, examination and provider knowledge."],
  ["Studies disease mechanisms in laboratory animal models",
   "Animal models are basic science. Clinical epidemiology works from events observed in groups of patients."]],
 "c": 0, "cite": c(17)},

{"topic": "Medical decisions", "io": IOB, "slot": "principle",
 "q": "On what does good medical decision making depend?",
 "opts": [
  ["Good information, from history, examination and knowledge",
   "Correct, and it also relies on patient goals and values, provider beliefs, and the risks, benefits, effectiveness, adverse reactions and cost of any intervention."],
  ["The provider's clinical experience alone",
   "Experience matters, but treating it as sufficient is exactly the eminence-based reasoning that evidence-based practice was formulated against."],
  ["Published evidence alone, independent of the patient",
   "Patient values and preferences are one of the three inputs to good clinical decision making, alongside clinical expertise and external evidence."],
  ["The cost of the intervention above all other factors",
   "Cost is one consideration among many, listed alongside risks, benefits, effectiveness and adverse reactions."]],
 "c": 0, "cite": c(18)},

{"topic": "Evidence-based medicine", "io": IOB, "slot": "definition",
 "q": "What is evidence-based medicine?",
 "opts": [
  ["Applying clinical epidemiology to patient care",
   "Correct, and it has three moves: using clinical judgement to assess available research for validity and applicability, then applying that evidence to decisions about care."],
  ["Following national guidelines without individual judgement",
   "Clinical judgement is built into the definition: the research must be assessed for validity and applicability before it is applied."],
  ["Basing decisions on the recommendation of a senior colleague",
   "Deferring to seniority because experience is held to trump evidence is eminence-based medicine, which is named as an alternative influence rather than as evidence-based practice."],
  ["Collecting original data on every patient before treating them",
   "It concerns appraising and applying existing research rather than generating new data for each encounter."]],
 "c": 0, "cite": c(25)},

{"topic": "Evidence-based medicine", "io": IOB, "slot": "principle",
 "q": "Which three inputs combine to produce good clinical decision making?",
 "opts": [
  ["Clinical expertise, external evidence, and patient values",
   "Correct, and the output named is not merely a decision but improved patient care, which is the point of combining all three rather than relying on any one."],
  ["Clinical expertise, institutional policy and cost containment",
   "Policy and cost are practical constraints rather than the three named inputs, which are expertise, external evidence and the patient's own values."],
  ["External evidence, statistical significance and journal reputation",
   "Significance and reputation are features of evidence rather than separate inputs, and this omits both clinical expertise and the patient."],
  ["Patient values, provider confidence and peer consensus",
   "Confidence and consensus are among the alternative influences named, not the inputs to evidence-based decision making."]],
 "c": 0, "cite": c(26)},

{"topic": "Other influences", "io": IOB, "slot": "definition",
 "q": "What is described as eminence-based medicine?",
 "opts": [
  ["Senior colleagues holding experience to trump evidence",
   "Correct, and it heads a list of alternatives to evidence that each substitute something else for appraisal: volume, eloquence, timidity, fear of litigation or bravado."],
  ["Substituting volume and stridency for evidence",
   "That is vehemence-based medicine, where the force of assertion rather than seniority does the work."],
  ["Sartorial elegance and verbal eloquence",
   "That is eloquence-based or elegance-based medicine, where presentation substitutes for evidence."],
  ["Fear of litigation driving over-investigation",
   "That is nervousness-based medicine, where legal anxiety rather than seniority drives the decision."]],
 "c": 0, "cite": c(27)},

{"topic": "Other influences", "io": IOB, "slot": "definition",
 "q": "What characterises nervousness-based medicine?",
 "opts": [
  ["Fear of litigation driving over-investigation",
   "Correct, and it is distinct from diffidence-based medicine, where the practitioner is too timid to make any decision at all rather than moved to do too much. Overtreatment follows from the same fear."],
  ["Being too timid to make any medical decision",
   "That is diffidence-based medicine. Nervousness-based medicine produces action rather than paralysis, in the form of over-investigation."],
  ["Bravado standing in for evidence",
   "That is confidence-based medicine, which overestimates rather than fears."],
  ["Leaving the decision in the hands of the Almighty",
   "That is providence-based medicine, which defers the decision rather than overreacting to legal risk."]],
 "c": 0, "cite": c(28)},

{"topic": "Finding evidence", "io": IOA, "slot": "resource",
 "q": "Which database is named as the source for literature reviews?",
 "opts": [
  ["The Cochrane Database of Systematic Reviews",
   "Correct. Original articles are found instead through MEDLINE and PubMed, so the choice of database follows from whether you want a synthesis or the primary studies."],
  ["MEDLINE",
   "MEDLINE is named as a source of original articles rather than of systematic reviews."],
  ["PubMed",
   "PubMed is named alongside MEDLINE as a source of original articles rather than of literature reviews."],
  ["The National Health Interview Survey",
   "That is a periodic population survey producing data, not a database of published literature."]],
 "c": 0, "cite": c(31)},

{"topic": "Finding evidence", "io": IOA, "slot": "resource",
 "q": "At which levels are practice guidelines produced?",
 "opts": [
  ["Hospital or clinic, national, and professional bodies",
   "Correct, with the Centers for Disease Control and Prevention among the national sources and bodies such as the American Academy of Pediatrics among the professional organisations."],
  ["Only by national government agencies",
   "Guidelines also exist at hospital or clinic level and are issued by professional organisations."],
  ["Only by the individual treating clinician",
   "Guidelines are produced by institutions, national bodies and professional organisations rather than by individual practitioners."],
  ["Only by the journals that publish original research",
   "Journals publish research and reviews; guidelines come from clinical institutions, national agencies and professional organisations."]],
 "c": 0, "cite": c(30)},

{"topic": "The five As", "io": IOB, "slot": "framework",
 "q": "In the five As framework, what does Ask mean?",
 "opts": [
  ["Define the clinical question",
   "Correct, and the example given is whether one treatment is better than another. Everything after it depends on the question being defined first."],
  ["Systematically retrieve the available literature",
   "That is Acquire, the second step, which can only be done once the question has been defined."],
  ["Assess validity and applicability",
   "That is Appraise, the third step, where clinical judgement is brought to bear on what was retrieved."],
  ["Evaluate outcomes on patient care",
   "That is Assess, the final step, which measures what happened after the change was made."]],
 "c": 0, "cite": c(32)},

{"topic": "The five As", "io": IOB, "slot": "framework",
 "q": "What are the final two steps of the five As?",
 "opts": [
  ["Apply, then Assess",
   "Correct: changes are made to practice, and then outcomes on patient care are evaluated. Skipping the last step leaves you without evidence that the change helped."],
  ["Assess, then Apply",
   "The order runs the other way. Practice is changed first, and the effect of that change is evaluated afterwards."],
  ["Appraise, then Acquire",
   "Those are the third and second steps respectively, and in the reverse order: literature is retrieved before it is appraised."],
  ["Ask, then Acquire",
   "Those are the first two steps rather than the last two: the question is defined, then the literature is retrieved."]],
 "c": 0, "cite": c(32)},

{"topic": "Purposes of research", "io": IOB, "slot": "purpose",
 "q": "What is the purpose of exploratory research?",
 "opts": [
  ["To address a new or understudied topic and satisfy curiosity",
   "Correct, and it has two further purposes that are practical rather than intellectual: testing the feasibility of a more careful study and developing the methods that study would use."],
  ["To observe carefully and describe what is found",
   "That is descriptive research, which reports disease rates and the demographic characteristics of those affected."],
  ["To attempt to explain why something occurs",
   "That is explanatory research, which goes beyond describing what is happening to account for it."],
  ["To analyse data that another researcher has already collected",
   "That describes secondary research, a distinction about the source of the data rather than the purpose of the study."]],
 "c": 0, "cite": c(33)},

{"topic": "Purposes of research", "io": IOB, "slot": "purpose",
 "q": "What does descriptive research produce?",
 "opts": [
  ["Careful observation and a description of what is found",
   "Correct, and the examples given are concrete: disease rates for a given population, and the demographic characteristics of those who have the disease."],
  ["An account of why a relationship exists",
   "Explaining why is the purpose of explanatory research. Description reports what is observed without attempting the account."],
  ["A test of whether a larger study would be feasible",
   "Feasibility testing is one purpose of exploratory research rather than of description."],
  ["A pooled estimate drawn from several published studies",
   "Pooling published studies describes a meta-analysis, which is a form of secondary research."]],
 "c": 0, "cite": c(34)},

{"topic": "Primary and secondary research", "io": IOB, "slot": "definition",
 "q": "What distinguishes primary from secondary research?",
 "opts": [
  ["Primary research uses data the researcher collects personally",
   "Correct, and secondary research analyses data that already exists. Original research articles are the example of the first; meta-analyses and systematic reviews of the second."],
  ["Primary research is published first, secondary research later",
   "The distinction is about who collected the data rather than the order of publication."],
  ["Primary research is always a randomised trial",
   "Primary research is defined by collecting the data personally, whatever the design, and the instruments listed include questionnaires and clinical measurements."],
  ["Secondary research involves a second group of participants",
   "Secondary research recruits no participants at all; it analyses data that has already been collected."]],
 "c": 0, "cite": c(35)},

{"topic": "Primary and secondary research", "io": IOB, "slot": "definition",
 "q": "Which are given as examples of secondary research?",
 "opts": [
  ["Meta-analyses and systematic review articles",
   "Correct, because both analyse data that already exists rather than collecting new data. Original research articles are the example of primary research."],
  ["Original research articles",
   "Original research articles are the named example of primary research, where the investigators collected the data themselves."],
  ["Questionnaires and surveys",
   "Those are data collection instruments used in primary research rather than examples of secondary research."],
  ["Laboratory test results and vital signs",
   "Those are clinical measurements listed among the primary research instruments."]],
 "c": 0, "cite": c(36)},

{"topic": "Variables", "io": IOB, "slot": "definition",
 "q": "What is the independent variable in a study?",
 "opts": [
  ["The possible cause",
   "Correct, and the dependent variable is the possible effect. Naming which is which is the first step in reading what a study actually claims."],
  ["The possible effect",
   "That is the dependent variable. The independent variable is the one proposed as the cause."],
  ["A variable that may distort the relationship between the other two",
   "That describes an extraneous variable, also called a covariate."],
  ["The subset of people actually studied",
   "That is the sample, drawn from the population, rather than a variable."]],
 "c": 0, "cite": c(37)},

{"topic": "Variables", "io": IOB, "slot": "definition",
 "q": "What is another name for an extraneous variable?",
 "opts": [
  ["A covariate",
   "Correct, and the definition is functional: it is a variable that may affect the relationship between the independent and dependent variables, which is what makes it worth identifying."],
  ["A dependent variable",
   "The dependent variable is the possible effect under study rather than an outside influence on the relationship."],
  ["An independent variable",
   "The independent variable is the possible cause under study rather than an additional variable acting on the relationship."],
  ["A sample",
   "A sample is a subset of a population, not a variable of any kind."]],
 "c": 0, "cite": c(37)},

{"topic": "Variables", "io": IOB, "slot": "definition",
 "q": "How do a population and a sample differ?",
 "opts": [
  ["A population is everyone in a defined setting; a sample is a subset of it",
   "Correct, and the definition of a population turns on the defining characteristic or setting, which is what determines whether a given sample represents it."],
  ["A population is the people studied; a sample is everyone else",
   "The relationship runs the other way: the sample is the subset actually studied, drawn from the larger population."],
  ["A population is always larger than one million people",
   "No size threshold defines a population; it is everyone in a defined setting or with defined characteristics."],
  ["A sample is chosen only when the population cannot be identified",
   "Sampling is a normal feature of research design rather than a fallback for an unidentifiable population."]],
 "c": 0, "cite": c(37)},

{"topic": "Questions before answers", "io": IOB, "slot": "framework",
 "q": "Which clinical question does the term Abnormality address?",
 "opts": [
  ["Is the patient sick or well?",
   "Correct, and it sits alongside Frequency, which asks how often a disease occurs, as one of the questions that has to be settled before any answer about this patient is possible."],
  ["How often does the disease occur?",
   "That is Frequency, which concerns the rate of a disease in a population rather than the state of the individual in front of you."],
  ["What factors are associated with increased risk?",
   "That is Risk, which identifies what makes disease more likely rather than whether it is present now."],
  ["What are the consequences of having the disease?",
   "That is Prognosis, which looks forward from an established diagnosis rather than establishing whether the patient is unwell."]],
 "c": 0, "cite": c(22)},

{"topic": "Questions before answers", "io": IOB, "slot": "framework",
 "q": "Which clinical question does the term Diagnosis address?",
 "opts": [
  ["How accurate are the tests used to identify the disease?",
   "Correct. The question is about the performance of the tests themselves, which is why test properties are studied as a topic in their own right rather than assumed."],
  ["What conditions lead to the disease?",
   "That is Cause, which concerns the origins of the disease rather than the accuracy of the tests used to detect it."],
  ["How does treatment change the course of the disease?",
   "That is Treatment, which asks what an intervention does once disease is established."],
  ["Does early detection improve the course of the disease?",
   "That belongs to Prevention, which covers both keeping disease from arising and detecting it early."]],
 "c": 0, "cite": c(22)},

{"topic": "Questions before answers", "io": IOB, "slot": "framework",
 "q": "Which two questions fall under Prevention?",
 "opts": [
  ["Does prevention stop disease arising, and does early detection help?",
   "Correct, and the pairing matters because the two are different claims: stopping disease from arising is not the same as finding it sooner once it has."],
  ["What conditions lead to the disease, and what are its origins?",
   "Both of those belong to Cause, which asks what conditions lead to disease."],
  ["How often does the disease occur, and who is most at risk?",
   "Those are Frequency and Risk respectively, which describe the distribution of disease rather than efforts to avert it."],
  ["Is the patient sick or well, and what happens to them next?",
   "Those are Abnormality and Prognosis, concerning the individual's current state and future rather than prevention."]],
 "c": 0, "cite": c(23)},

{"topic": "Finding answers", "io": IOB, "slot": "framework",
 "q": "From what three sources are answers to clinical questions drawn?",
 "opts": [
  ["Experience, knowledge and clinical research",
   "Correct, and the three are complementary: leaning on experience alone is the eminence-based reasoning that evidence-based practice was formulated against."],
  ["Experience, intuition and consensus",
   "Intuition and consensus are not among the three named sources, which are experience, knowledge and clinical research."],
  ["Guidelines, textbooks and colleagues",
   "Those are vehicles through which knowledge and research travel rather than the three sources named."],
  ["Knowledge, cost and patient preference",
   "Cost and patient preference bear on the decision made, but the sources of answers are experience, knowledge and clinical research."]],
 "c": 0, "cite": c(24)},

{"topic": "Data sources", "io": IOA, "slot": "data source",
 "q": "Besides registries and surveys, which other data sources are named?",
 "opts": [
  ["Hospital data such as admissions and discharges, and clinic data",
   "Correct, and their value is that they already exist as a by-product of care, though they describe only the people who sought that care. Emergency department records belong to the same category."],
  ["Peer-reviewed journal articles",
   "Published articles report findings drawn from data; the category here is the underlying data sources themselves."],
  ["Practice guidelines issued by professional organisations",
   "Guidelines synthesise evidence into recommendations rather than serving as a source of epidemiologic data."],
  ["Textbooks of clinical epidemiology",
   "A textbook is a teaching resource rather than a source of epidemiologic data."]],
 "c": 0, "cite": c(16)},

{"topic": "Data sources", "io": IOA, "slot": "data source",
 "q": "What characterises a state list of reportable diseases?",
 "opts": [
  ["It is long and varied, spanning infections, poisonings and cancers",
   "Correct. A single state list runs from acquired immunodeficiency syndrome and anthrax through arsenic and carbon monoxide poisoning to cancer and congenital anomalies."],
  ["It is limited to sexually transmitted infections",
   "Chancroid and chlamydia appear on such lists, but so do poisonings, congenital anomalies and cancers."],
  ["It is limited to diseases that can be prevented by vaccination",
   "Vaccine-preventable diseases such as diphtheria appear, but the lists extend well beyond them."],
  ["It is identical in every state",
   "Reportable disease lists are set by individual states, which is why they are described state by state."]],
 "c": 0, "cite": c(15)},

{"topic": "Making decisions", "io": IOB, "slot": "principle",
 "q": "How should a clinician judge whether they have good information?",
 "opts": [
  ["By critically analysing it and distinguishing strong from weak",
   "Correct, and two other things bear on it: a trusting patient-provider relationship, and the quality of the source material behind the provider's own knowledge."],
  ["By checking whether it agrees with what they already believe",
   "Agreement with prior belief is not a test of quality, and provider beliefs are listed among the influences on a decision rather than a standard for judging evidence."],
  ["By counting how many colleagues share the same view",
   "Peer agreement can reflect shared assumptions rather than evidence, and critical analysis is what is called for."],
  ["By accepting anything published in a medical journal",
   "Distinguishing reliable from unreliable sources is precisely the task, which publication alone does not settle."]],
 "c": 0, "cite": c(19)},

{"topic": "Study quality", "io": IOB, "slot": "principle",
 "q": "What is the difficulty with applying statistical analysis to data from poorly designed research?",
 "opts": [
  ["It may give a false sense of respectability to the research",
   "Correct, and the reason it is a trap is that no analysis can correct for unknown biases, so the statistics look rigorous while resting on data that is not."],
  ["Statistical analysis cannot be performed on such data at all",
   "It can be performed; the problem is what the output implies rather than whether it can be produced."],
  ["It removes the effect of bias from the results",
   "Analysis can estimate the effect of chance, but no analysis can correct for unknown biases."],
  ["It converts a descriptive study into an explanatory one",
   "The purpose of a study is set by its design and question rather than changed by the analysis applied afterwards."]],
 "c": 0, "cite": c(49)},
]
