# -*- coding: utf-8 -*-
# Microbiology Exam 2 — "Webster Review" forms A and B, Lecture 12 (Epidemiology).
# One question per review item (3.1-3.10) in each form, plus four extras on the Know-cold items she
# gave her strongest instructions on, two in form A and two in form B:
#   A: 3.8 (a scenario judged association versus causation), 3.9 (reading a mixed epidemic curve);
#   B: 3.7 (prevalence worked from numbers, using the incidence/prevalence numerators), 3.3 (genomic
#      epidemiology as the outbreak-investigation tool).
# Light touch gets nothing: the slide 13 graph, the slide 23 notifiable-disease list, the slide 25
# uses-of-surveillance list.
#
# Grounding: visible slide text and pictures only (no speaker notes, no spoken asides). The review page
# lists no point where her words and the Lecture 12 slides differ, so nothing here needed a slide-over-
# words call. Pictures viewed at full size: slide 24 (CDC weekly tables), 45, 49, 56-58 (epidemic
# curves; slide 56 left = Point, right = Continuous; slide 57 left = Propagated, right = Mixed). The
# curve items are NEW scenarios written in words, never the slides' own outbreaks.
# Stems avoid the existing topic-quiz stems in micro_l12_pool.py (107 items) and the guide's self-test.
# KEYS ARE WRITTEN SHORT ON PURPOSE — detail lives in the explanation. Key position is rebalanced later;
# "c" is simply the key's index here. Numeric sets are ascending with the key where its value falls.

SRC = "Lecture 12 Dr. Webster - Epidemiology.pptx"
def cs(n): return f"{SRC}, Slide {n}"
def cr(a, b): return f"{SRC}, Slides {a}-{b}"
def cl(*n): return f"{SRC}, Slides " + ", ".join(map(str, n))

IO = {
    1: "1 — Distinguish between descriptive and analytic epidemiology.",
    2: "2 — Describe the specific uses for epidemiology training.",
    3: "3 — Describe key events in the history and development of epidemiology, including genomic epidemiology",
    4: "4 — Identify common sources of epidemiologic data.",
    5: "5 — Define the primary components of public health surveillance.",
    6: "6 — Define reportable disease",
    7: "7 — Describe selected measures of morbidity and mortality.",
    8: "8 — Distinguish between the terms association and causation.",
    9: "9 — Define the terms endemic, epidemic, pandemic, sporadic, and herd immunity.",
    10: ("10 — Compare and contrast applications of epidemiology, including policy development, outbreak "
         "investigation, social and behavioral issues, the environment and occupational health"),
}

POOL = [

# ---------------------------------------------------------------- 3.1 (Know cold) descriptive vs analytic
dict(lecture=12, item="3.1", tier="cold", form="A", topic="Descriptive versus analytic: what each yields", io=IO[1],
  q=("A community health survey records the age, neighborhood and month of onset of each resident's rash "
     "illness, to see how the illness is distributed by person, place and time. What can a study of this "
     "kind yield?"),
  opts=[["Hypotheses and associations",
         "Correct: a community health survey is descriptive epidemiology, which examines distribution by person, place and time and formulates hypotheses and examines associations."],
        ["A cause-effect relationship",
         "A cause-effect relationship comes from analytic epidemiology, which tests a specific hypothesis with cohort, case-control or experimental designs; a descriptive survey yields hypotheses and associations."],
        ["The cause in each person",
         "Epidemiology does not determine the cause of a disease in a given individual; it relates exposures to disease frequency in populations, and a descriptive survey yields hypotheses and associations."],
        ["A tested specific hypothesis",
         "Testing a specific hypothesis about a disease and a specific cause is analytic epidemiology; a descriptive survey comes first and formulates the hypotheses that analytic studies later test."]],
  mis={"A cause-effect relationship": "confuses the output of descriptive epidemiology with that of analytic epidemiology",
       "The cause in each person": "thinks epidemiology determines the cause of disease in an individual",
       "A tested specific hypothesis": "confuses formulating a hypothesis with testing one"},
  c=0, cite=cl(32, 43),
  guide_quote="Formulates hypotheses and examines associations"),

dict(lecture=12, item="3.1", tier="cold", form="B", topic="Analytic triad: environment", io=IO[1],
  q=("Investigators studying a respiratory infection record household crowding, housing quality and sewage "
     "disposal in each home. In the triad that analytic epidemiology assesses, where do these factors belong?"),
  opts=[["Environment",
         "Correct: the analytic triad is host, agent and environment, and living conditions such as housing, crowding, water supply, refuse and sewage are environmental factors."],
        ["Host",
         "Host factors are genetic endowment, immunologic status, personal characteristics and personal behavior; housing, crowding and sewage are living conditions, which belong to the environment."],
        ["Agent",
         "Agents are biological, physical, chemical, environmental or psychological causes such as microorganisms or tobacco; housing, crowding and sewage are living conditions, part of the environment."],
        ["Place",
         "Place belongs to the descriptive triad of person, place and time; the analytic triad is host, agent and environment, and living conditions such as crowding and sewage fall under environment."]],
  mis={"Host": "files the household's living conditions under the person's own characteristics",
       "Agent": "confuses the conditions around the disease with its cause",
       "Place": "mixes the descriptive triad (person, place, time) into the analytic one"},
  c=0, cite=cr(37, 40),
  guide_quote="Living conditions (housing, crowding, water supply, refuse, sewage); atmosphere and climate"),

# ---------------------------------------------------------------- 3.2 (Know it) uses of epidemiology training
dict(lecture=12, item="3.2", tier="it", form="A", topic="Uses of training: surveillance", io=IO[2],
  q=("An epidemiologist helps a state health department set up, manage and evaluate a system that routinely "
     "collects, analyzes and interprets data on a disease. Which use of epidemiological training is this?"),
  opts=[["Public health surveillance",
         "Correct: setting up, managing and evaluating public health surveillance systems, which collect, analyze and interpret disease data, is one of the uses of epidemiological training."],
        ["Outbreak response",
         "Outbreak response means identifying, reporting and investigating outbreaks in a timely manner; building and running an ongoing data system is public health surveillance."],
        ["Public health communication",
         "Public health communication is developing and delivering public health communications; setting up, managing and evaluating a data system is public health surveillance."],
        ["Experimental epidemiology",
         "Experimental epidemiology develops a hypothesis for a health concern and designs an experimental model to test it; running a routine data system is public health surveillance."]],
  mis={"Outbreak response": "confuses the ongoing data system with responding to one outbreak",
       "Public health communication": "confuses collecting and analyzing data with delivering messages",
       "Experimental epidemiology": "confuses routine data analysis with designing a model to test a hypothesis"},
  c=0, cite=cl(7, 8, 14),
  guide_quote="Public health surveillance: setting up, managing and evaluating surveillance systems."),

dict(lecture=12, item="3.2", tier="it", form="B", topic="Uses of training: outbreak response", io=IO[2],
  q=("Days after a cluster of severe pneumonia cases appears in one town, an epidemiologist identifies it, "
     "reports it to the health department and investigates it. Which use of epidemiological training is this?"),
  opts=[["Outbreak response",
         "Correct: outbreak response means identifying outbreaks, reporting them and investigating them in a timely manner, as done here within days."],
        ["Public health communication",
         "Public health communication is developing and delivering public health communications; identifying, reporting and promptly investigating a cluster is outbreak response."],
        ["Disease prioritization",
         "Disease prioritization evaluates and ranks diseases of concern by who gets them, who dies and the outcome; identifying, reporting and investigating a cluster is outbreak response."],
        ["Program evaluation and management",
         "Program evaluation and management evaluates prevention and intervention programs, such as vaccine and clinical trials, and their staff; investigating a cluster is outbreak response."]],
  mis={"Public health communication": "takes reporting the cluster for delivering public messages",
       "Disease prioritization": "confuses investigating one cluster with ranking diseases of concern",
       "Program evaluation and management": "confuses outbreak work with evaluating intervention programs"},
  c=0, cite=cr(7, 8),
  guide_quote="Outbreak response: identifying, reporting and investigating outbreaks in a timely manner."),

# ---------------------------------------------------------------- 3.3 (Know cold) history, genomic epidemiology
dict(lecture=12, item="3.3", tier="cold", form="A", topic="Genomic epidemiology: what made it possible", io=IO[3],
  q="Genomic epidemiology monitors the genetic makeup of the pathogens that cause disease. What made it possible?",
  opts=[["Advances in sequencing",
         "Correct: genomic epidemiology, the monitoring of the genetic makeup of disease-causing pathogens, was made possible by advances in sequencing techniques."],
        ["Spot maps of cases",
         "Spot maps, marking where cases lived and worked, belong to John Snow's field epidemiology of the 1800s; genomic epidemiology was made possible by advances in sequencing."],
        ["Life-table approaches",
         "Life-table approaches to the force and burden of mortality were William Farr's work in the 1800s; genomic epidemiology was made possible by advances in sequencing techniques."],
        ["Koch's postulates",
         "Koch's postulates, published in 1884, established cause and effect between microbes and disease; genomic epidemiology was made possible by advances in sequencing techniques."]],
  mis={"Spot maps of cases": "takes an older field method for the advance behind genomic work",
       "Life-table approaches": "confuses genomic epidemiology with the history of vital statistics",
       "Koch's postulates": "confuses proving microbial causation with sequencing pathogens"},
  c=0, cite=cl(10, 12, 41, 42, 69),
  guide_quote=("Genomic epidemiology, one of the most important developments in the field, is the process of "
               "monitoring the genetic makeup of the pathogens that cause disease, made possible by advances in "
               "sequencing.")),

dict(lecture=12, item="3.3", tier="cold", form="B", topic="History: the Framingham study", io=IO[3],
  q="The multigenerational study that began in Framingham in 1948 set out to identify what?",
  opts=[["Common factors in cardiovascular disease",
         "Correct: the Framingham Heart Study, begun in 1948, is a multigenerational study to identify common factors contributing to cardiovascular disease."],
        ["The link between smoking and lung cancer",
         "Smoking and lung cancer was the 1950 work of Doll and Hill; the Framingham study set out to identify common factors contributing to cardiovascular disease."],
        ["The water source of cholera outbreaks",
         "Tracing cholera to water was John Snow's work in the mid-1800s; the Framingham study set out to identify common factors contributing to cardiovascular disease."],
        ["Mortality gaps between town and country",
         "Urban and rural differences in mortality were noted by John Graunt in the 17th century; the Framingham study set out to identify factors contributing to cardiovascular disease."]],
  mis={"The link between smoking and lung cancer": "confuses Framingham with Doll and Hill (1950)",
       "The water source of cholera outbreaks": "confuses Framingham with John Snow",
       "Mortality gaps between town and country": "confuses Framingham with John Graunt's tabulations"},
  c=0, cite=cr(10, 11),
  guide_quote="A multigenerational study to identify common factors contributing to cardiovascular disease"),

dict(lecture=12, item="3.3", tier="cold", form="B", topic="Genomic epidemiology: where it is used", io=IO[3],
  q="Genomic epidemiology is called one of the most reliable tools in which application of epidemiology?",
  opts=[["Outbreak investigation",
         "Correct: genomic epidemiology is one of the most reliable tools in outbreak investigation, identifying sources of exposure and transmission links and linking cases found in different places."],
        ["Policy development",
         "Policy development rests on values, ideology, politics and evidence, evidence being the main contribution of epidemiology; genomic epidemiology is a key tool in outbreak investigation."],
        ["Occupational health",
         "Occupational health studies how workplace conditions and hazardous substances affect workers' health; genomic epidemiology is one of the most reliable tools in outbreak investigation."],
        ["Environmental issues",
         "Environmental epidemiology studies how air and water pollution or hazardous waste sites affect human health; genomic epidemiology is one of the most reliable tools in outbreak investigation."]],
  mis={"Policy development": "takes epidemiology's evidence-for-policy role for the genomic tool's use",
       "Occupational health": "picks an adjacent application of epidemiology",
       "Environmental issues": "picks an adjacent application of epidemiology"},
  c=0, cite=cl(12, 61, 69, 72, 76),
  guide_quote="It is one of the most reliable tools in outbreak investigation"),

# ---------------------------------------------------------------- 3.4 (Know it) sources of data
dict(lecture=12, item="3.4", tier="it", form="A", topic="Data sources: individual persons", io=IO[4],
  q=("Investigators want epidemiologic data gathered directly from individual persons. Which collection method "
     "fits that source?"),
  opts=[["Questionnaires and surveys",
         "Correct: data from individual persons are collected by questionnaire or survey, as in a foodborne illness outbreak or a national health and nutrition survey."],
        ["River water and soil samples",
         "Samples of river water or soil, and sensors for environmental change, collect data from the environment; individual persons are reached by questionnaire or survey."],
        ["Notifications of observed cases",
         "Notifications to the health department when certain diseases are observed come from health care providers; individual persons are reached by questionnaire or survey."],
        ["Sales and court records",
         "Sales and court records are nonhealth-related financial and legal sources, such as cigarette sales; individual persons are reached by questionnaire or survey."]],
  mis={"River water and soil samples": "takes the environmental source's method",
       "Notifications of observed cases": "takes the health care provider source's method",
       "Sales and court records": "takes the nonhealth-related (financial, legal) source's method"},
  c=0, cite=cs(18),
  guide_quote=None),

dict(lecture=12, item="3.4", tier="it", form="B", topic="Data sources: social media", io=IO[4],
  q="Social media can be a valuable source of data for monitoring what?",
  opts=[["Disease outbreaks and mental health",
         "Correct: social media can be a valuable source of data for monitoring disease outbreaks and mental health issues."],
        ["Air and water pollutant levels",
         "Pollutants are measured from the environment, with samples of river water or soil and sensors; social media helps monitor disease outbreaks and mental health issues."],
        ["Cancer cases for state registries",
         "Cancer is its own group of reportable disease, reported to state cancer registries; social media helps monitor disease outbreaks and mental health issues."],
        ["Cigarette sales across a region",
         "Cigarette sales come from sales records, a nonhealth-related source; social media can be a valuable source for monitoring disease outbreaks and mental health issues."]],
  mis={"Air and water pollutant levels": "assigns the environmental source's data to social media",
       "Cancer cases for state registries": "assigns a reportable-disease registry to social media",
       "Cigarette sales across a region": "assigns a nonhealth-related sales source to social media"},
  c=0, cite=cl(18, 20, 22),
  guide_quote="Can be valuable for monitoring disease outbreaks and mental health issues"),

# ---------------------------------------------------------------- 3.5 (Know it) public health surveillance
dict(lecture=12, item="3.5", tier="it", form="A", topic="Surveillance types: passive", io=IO[5],
  q=("A country's routine health information system relies on the reports that health care facilities and "
     "providers submit. Which type of surveillance is this?"),
  opts=[["Passive surveillance",
         "Correct: passive surveillance relies on reports submitted by health care facilities and providers, and it includes routine health information systems."],
        ["Active surveillance",
         "Active surveillance uses staff members to contact health care providers regularly for data; relying on the reports that facilities submit is passive surveillance."],
        ["Sentinel surveillance",
         "Sentinel surveillance uses a prearranged group of reporting sources that agree to report all cases of specific conditions; a routine system of submitted reports is passive."],
        ["Syndromic surveillance",
         "Syndromic surveillance is defined by case definitions based entirely on clinical features, such as diarrhea instead of cholera; routine submitted reports are passive surveillance."]],
  mis={"Active surveillance": "reverses who starts the contact (staff reaching out versus reports coming in)",
       "Sentinel surveillance": "takes any provider reporting for a prearranged reporting group",
       "Syndromic surveillance": "confuses the reporting route with the kind of case definition"},
  c=0, cite=cr(19, 20),
  guide_quote="Relies on reports submitted by health care facilities and providers (includes routine health information systems)"),

dict(lecture=12, item="3.5", tier="it", form="B", topic="Surveillance characteristics: specificity", io=IO[5],
  q=("A surveillance team tightens its case definition so that persons who do not have the disease are no "
     "longer counted as cases. Which critical characteristic of surveillance does this improve?"),
  opts=[["Specificity",
         "Correct: specificity is the critical characteristic of surveillance that excludes persons not having the disease from the count."],
        ["Sensitivity",
         "Sensitivity allows individual persons with the disease to be identified for treatment, quarantine or other control; excluding persons without the disease is specificity."],
        ["Representation",
         "Representation gives an accurate picture of the temporal trend of the disease; excluding persons who do not have the disease from the count is specificity."],
        ["Timeliness",
         "Timeliness lets effective control measures be implemented in time; excluding persons who do not have the disease from the count is specificity."]],
  mis={"Sensitivity": "swaps sensitivity (finding the ill) with specificity (excluding the well)",
       "Representation": "thinks an accurate trend is the same as excluding non-cases",
       "Timeliness": "confuses speed of data with accuracy of the case count"},
  c=0, cite=cs(15),
  guide_quote="To exclude persons not having the disease"),

# ---------------------------------------------------------------- 3.6 (Know it) reportable disease
dict(lecture=12, item="3.6", tier="it", form="A", topic="Reportable disease groups: written report", io=IO[6],
  q="Which reportable disease belongs to the group that requires a mandatory written report?",
  opts=[["Gonorrhea",
         "Correct: gonorrhea and salmonellosis are the examples of reportable diseases in the group that requires a mandatory written report."],
        ["Pertussis",
         "Pertussis, with rubeola, is in the group that requires a mandatory report by telephone; gonorrhea and salmonellosis require a mandatory written report."],
        ["Chickenpox",
         "Chickenpox, with influenza, is reported as a total number of cases rather than case by case; gonorrhea and salmonellosis require a mandatory written report."],
        ["Cancer",
         "Cancer forms its own group, reported to state cancer registries; gonorrhea and salmonellosis are the examples that require a mandatory written report."]],
  mis={"Pertussis": "takes the telephone-report group for the written-report group",
       "Chickenpox": "takes the total-number-of-cases group for the written-report group",
       "Cancer": "takes the cancer-registry group for the written-report group"},
  c=0, cite=cs(22),
  guide_quote=None),

dict(lecture=12, item="3.6", tier="it", form="B", topic="Reportable disease: the annual list", io=IO[6],
  q="How many times a year is the list of notifiable diseases produced?",
  opts=[["1",
         "Correct: a list of notifiable diseases is produced every year, naming the diseases required by law to be reported to government authorities."],
        ["4",
         "Four would mean a new list every quarter; the list of notifiable diseases is produced once every year."],
        ["12",
         "Twelve would mean a new list every month; the list of notifiable diseases is produced once every year."],
        ["52",
         "Fifty-two matches the weekly tables of notifiable disease cases from the CDC (Centers for Disease Control and Prevention); the list of diseases itself is produced once a year."]],
  mis={"4": "guesses a quarterly cycle",
       "12": "guesses a monthly cycle",
       "52": "confuses the weekly tables of case counts with the yearly list"},
  c=0, cite=cl(21, 22, 24),
  guide_quote=("In the United States, collection is done through the CDC’s National Notifiable Diseases "
               "Surveillance System, and a list of notifiable diseases is produced every year.")),

# ---------------------------------------------------------------- 3.7 (Know cold) morbidity and mortality
dict(lecture=12, item="3.7", tier="cold", form="A", topic="Incidence versus prevalence: low prevalence", io=IO[7],
  q=("A respiratory infection arises at the same rate in two cities. In City B it causes no deaths, yet its "
     "prevalence there is far lower. Which explanation fits?"),
  opts=[["Patients in City B recover sooner",
         "Correct: prevalence depends on incidence and duration of illness; with equal incidence and no deaths, the lower prevalence in City B points to rapid recovery."],
        ["Patients in City B live longer uncured",
         "Prolonged survival without cure lengthens the duration of illness and raises prevalence; lower prevalence with equal incidence and no deaths points to rapid recovery."],
        ["Patients in City B die sooner",
         "A rapidly fatal process can lower prevalence, but the infection causes no deaths in City B; with equal incidence, its lower prevalence points to rapid recovery."],
        ["More new cases arise in City B",
         "The infection arises at the same rate in both cities, and more new cases would raise prevalence, not lower it; the lower prevalence points to rapid recovery."]],
  mis={"Patients in City B live longer uncured": "reverses the effect of duration on prevalence",
       "Patients in City B die sooner": "ruled out by a stated finding (no deaths)",
       "More new cases arise in City B": "ignores the equal incidence and reverses its effect"},
  c=0, cite=cs(27),
  guide_quote=("High prevalence may reflect high incidence, prolonged survival without cure, or both; low "
               "prevalence may mean low incidence, a rapidly fatal process, or rapid recovery.")),

dict(lecture=12, item="3.7", tier="cold", form="B", topic="Mortality rates: crude", io=IO[7],
  q=("A health department counts every death from any cause in its whole population during one year. Which "
     "rate does this give?"),
  opts=[["Crude mortality rate",
         "Correct: the crude mortality rate counts deaths from all causes in a population in a given time period."],
        ["Cause-specific mortality rate",
         "A cause-specific mortality rate counts deaths from one specific cause in a population; counting deaths from all causes in a period gives the crude mortality rate."],
        ["Age-specific mortality rate",
         "An age-specific mortality rate counts deaths in one specific age group; counting deaths from all causes across the whole population gives the crude mortality rate."],
        ["Case fatality rate",
         "The case fatality rate is deaths divided by total cases of one disease; counting every death from all causes in a population gives the crude mortality rate."]],
  mis={"Cause-specific mortality rate": "confuses all causes with one cause",
       "Age-specific mortality rate": "confuses the whole population with one age group",
       "Case fatality rate": "confuses a population death rate with deaths among cases of one disease"},
  c=0, cite=cl(29, 59),
  guide_quote="Deaths from all causes in a population in a given time period"),

dict(lecture=12, item="3.7", tier="cold", form="B", topic="Prevalence from numbers", io=IO[7],
  q=("A town has 5,000 residents. On 1 January, 300 of them are living with a chronic disease; during the "
     "year, 100 more are newly diagnosed, and no one with the disease dies, recovers or moves away. What is "
     "the prevalence of the disease in the town during that year?"),
  opts=[["2%",
         "2% counts only the 100 new cases over the 5,000 residents, which is the incidence; prevalence during the year counts all 400 cases present, giving 8%."],
        ["6%",
         "6% counts only the 300 cases present on 1 January; prevalence during the year counts all cases present during the period, 300 plus 100, so 400 of 5,000 is 8%."],
        ["8%",
         "Correct: the numerator of prevalence is all cases present during the period, 300 existing plus 100 new, so 400 of the 5,000 residents is 8%."],
        ["33%",
         "33% divides the 100 new cases by the 300 existing ones, not by the population; prevalence is all 400 cases present over the 5,000 residents, which is 8%."]],
  mis={"2%": "uses the incidence numerator (new cases only) for prevalence",
       "6%": "counts only the cases present at the start of the period",
       "33%": "divides by existing cases instead of the population"},
  c=2, cite=cr(27, 28),
  guide_quote="Incidence counts new cases during a period; prevalence counts all cases present."),

# ---------------------------------------------------------------- 3.8 (Know cold) association versus causation
dict(lecture=12, item="3.8", tier="cold", form="A", topic="Hill's criteria: temporal sequence and latency", io=IO[8],
  q=("A study links an exposure to a cancer that has a latent period of about 15 years, but in most cases the "
     "exposure began only 2 years before diagnosis. Which of Hill's criteria does this timing fail to meet?"),
  opts=[["Temporal sequence",
         "Correct: temporal sequence requires exposure to precede disease and, in diseases with latency periods, to precede the latent period; exposure 2 years before diagnosis falls inside a 15-year latency."],
        ["Biological gradient",
         "Biological gradient is a dose-response relationship, a trend in relative risk with changing exposure; the timing problem here fails temporal sequence, since exposure must precede the latent period."],
        ["Strength of association",
         "Strength of association concerns a relative risk that is very high or very low; exposure that starts after the latent period has begun fails temporal sequence, not strength."],
        ["Consistency of findings",
         "Consistency asks whether the finding is repeated across studies, populations, circumstances and designs; exposure that begins inside the latent period fails temporal sequence."]],
  mis={"Biological gradient": "confuses the amount of exposure with its timing",
       "Strength of association": "confuses the size of the relative risk with timing",
       "Consistency of findings": "confuses replication across studies with timing"},
  c=0, cite=cl(46, 50),
  guide_quote="in diseases with latency periods, it must precede the latent period"),

dict(lecture=12, item="3.8", tier="cold", form="B", topic="Hill's criteria: the most reliable indicator", io=IO[8],
  q=("Investigators weigh several lines of evidence that an exposure causes a disease. Which one is regarded as "
     "one of the most reliable indicators of causality?"),
  opts=[["Risk that rises with dose",
         "Correct: a biological gradient, in which changes in exposure are related to a trend in relative risk, is one of the most reliable indicators of causality."],
        ["A single characteristic effect",
         "Specificity makes causation easier to support, but many exposures cause multiple diseases; the biological gradient, risk rising with dose, is one of the most reliable indicators."],
        ["A plausible mechanism",
         "Plausibility matters, but the relationship may be indirect and data may not yet support a mechanism; a dose-response gradient is one of the most reliable indicators of causality."],
        ["An association in one study",
         "Finding an association does not make it causal, and one study is not consistency across studies; a dose-response biological gradient is one of the most reliable indicators."]],
  mis={"A single characteristic effect": "overrates specificity, which many exposures lack",
       "A plausible mechanism": "overrates plausibility, which may rest on indirect or missing data",
       "An association in one study": "takes an association for causation"},
  c=0, cite=cl(43, 47, 49, 51, 52),
  guide_quote="Changes in exposure are related to a trend in relative risk; one of the most reliable indicators of causality"),

dict(lecture=12, item="3.8", tier="cold", form="A", topic="Association or causation: a scenario", io=IO[8],
  q=("A large study finds that a lung disease is twice as common among people living beside busy highways. No "
     "study has yet shown that the exposure came before the disease, or that risk rises with traffic exposure. "
     "What does this evidence establish so far?"),
  opts=[["An association",
         "Correct: an identifiable relationship between an exposure and a disease is an association; without temporal sequence or a dose-response gradient, causation cannot yet be inferred."],
        ["A causal relationship",
         "Finding an association does not make it causal; causation is inferred when criteria such as temporal sequence and a biological gradient are met, and neither has been shown here."],
        ["Each patient's own cause",
         "Epidemiology does not determine the cause of disease in a given individual; it relates an exposure to the frequency of disease in populations, and this finding is an association."],
        ["A chance finding",
         "Nothing shown here marks the result as chance, which is only one possible explanation of an association; a doubled risk is an identifiable relationship, an association."]],
  mis={"A causal relationship": "takes an association for causation",
       "Each patient's own cause": "thinks a population study determines individual causes",
       "A chance finding": "dismisses an identifiable relationship without evidence of chance"},
  c=0, cite=cl(43, 44, 46, 49, 50),
  guide_quote=("A relationship between an exposure and a disease is an association; causation is inferred from "
               "association plus Hill’s criteria")),

# ---------------------------------------------------------------- 3.9 (Know cold) terms and epidemic curves
dict(lecture=12, item="3.9", tier="cold", form="A", topic="Terms: epidemic versus pandemic", io=IO[9],
  q=("A new respiratory infection spreads uncontrolled through one city's neighborhoods but has not appeared in "
     "any other country. Which term fits?"),
  opts=[["Epidemic",
         "Correct: an epidemic is a disease occurring in excess of what might be expected, or as an uncontrolled spread in a community; it need not be worldwide."],
        ["Pandemic",
         "A pandemic is a worldwide epidemic; an infection spreading uncontrolled within one city that has reached no other country is an epidemic."],
        ["Endemic",
         "Endemic describes a disease found at chronically low levels in a population; an uncontrolled spread through a community is an epidemic."],
        ["Sporadic",
         "Sporadic describes disease occurring at irregular intervals or as isolated incidents; an uncontrolled spread through a community is an epidemic."]],
  mis={"Pandemic": "thinks any uncontrolled spread is a pandemic, whatever its reach",
       "Endemic": "confuses a steady low level with uncontrolled spread",
       "Sporadic": "confuses isolated cases with spread through a community"},
  c=0, cite=cs(54),
  guide_quote=("Diseases occurring in excess of what might be expected in a population, or as an uncontrolled "
               "spread in a community")),

dict(lecture=12, item="3.9", tier="cold", form="B", topic="Epidemic curves: continuous common source", io=IO[9],
  q=("Cases of an intestinal illness among workers at one factory, plotted by date of onset, appear on most days "
     "for six weeks with no single sharp peak and no successive waves, and stop soon after the factory's "
     "contaminated drinking-water tank is replaced. Which type of epidemic does this curve show?"),
  opts=[["Continuous common source",
         "Correct: a group exposed to the same source over a longer time gives a continuous common-source curve, with cases spread over weeks until the source is removed."],
        ["Point common source",
         "A point source exposes the group for a short time, within one incubation period, giving one sharp rise and fall; six weeks of cases from one tank is continuous exposure."],
        ["Propagated",
         "A propagated epidemic spreads person to person, giving successive waves of cases; cases spread over weeks from one water tank, with no waves, are a continuous common source."],
        ["Mixed",
         "A mixed epidemic starts as a common source and is then propagated person to person; one water tank feeding cases for weeks, without waves, is a continuous common source."]],
  mis={"Point common source": "ignores how long the exposure lasted",
       "Propagated": "ignores the single shared source and the absence of waves",
       "Mixed": "reads the long run of cases as person-to-person spread"},
  c=0, cite=cr(55, 56),
  guide_quote="Continuous: exposure over a longer time."),

dict(lecture=12, item="3.9", tier="cold", form="A", topic="Epidemic curves: mixed", io=IO[9],
  q=("An epidemic curve of an intestinal infection shows a sharp peak among guests who drank from one punch bowl "
     "at a party, followed over the next six weeks by successive waves of cases among people who never attended "
     "but had contact with ill guests. Which type of epidemic does this curve show?"),
  opts=[["Mixed",
         "Correct: a mixed epidemic may start as a common source, here the punch bowl, and then be propagated person to person, as the later waves among contacts show."],
        ["Point common source",
         "A point source alone gives one sharp rise and fall from a short exposure; the later waves among people who never attended show person-to-person spread after it, a mixed epidemic."],
        ["Propagated",
         "A propagated epidemic spreads person to person from the start; this one began with a common source, the punch bowl, before spreading person to person, which makes it mixed."],
        ["Continuous common source",
         "A continuous common source keeps exposing a group over a longer time; here a single exposure at the party was followed by person-to-person waves, which makes the epidemic mixed."]],
  mis={"Point common source": "reads only the first peak",
       "Propagated": "reads only the later waves",
       "Continuous common source": "reads the long tail as ongoing exposure to the source"},
  c=0, cite=cr(55, 57),
  guide_quote="Mixed: may start as a common source and then be propagated."),

# ---------------------------------------------------------------- 3.10 (Know it) applications of epidemiology
dict(lecture=12, item="3.10", tier="it", form="A", topic="Policy cycle: implementation", io=IO[10],
  q=("Having chosen a policy, a state health department sets target goals and allocates the money and staff the "
     "policy needs. Which step of the policy cycle is this?"),
  opts=[["Policy implementation",
         "Correct: policy implementation is the step of the policy cycle at which target goals are set and the necessary resources are allocated."],
        ["Policy choices",
         "Policy choices come before, when an option is chosen with tools such as computer modeling and delivered for a consensus decision; setting goals and resources is implementation."],
        ["Policy evaluation",
         "Policy evaluation comes last, collecting data on the results of the intervention and planning future modeling; setting goals and allocating resources is implementation."],
        ["Assessment of interventions",
         "Assessment of potential interventions identifies interventions and provides evidence of their efficacy; setting target goals and allocating resources is policy implementation."]],
  mis={"Policy choices": "confuses choosing a policy with putting it into effect",
       "Policy evaluation": "confuses the last step with the one before it",
       "Assessment of interventions": "confuses an early evidence step with implementation"},
  c=0, cite=cs(73),
  guide_quote="Policy implementation: set target goals and allocate the resources."),

dict(lecture=12, item="3.10", tier="it", form="B", topic="Outbreak investigation: where descriptive epidemiology fits", io=IO[10],
  q=("In a communicable disease outbreak investigation, at which point is descriptive epidemiology used to "
     "describe and orient the data?"),
  opts=[["After cases are defined and identified",
         "Correct: once cases are defined and identified, descriptive epidemiology is used to describe and orient the data, and a focused hypothesis is developed next."],
        ["Before the outbreak is established",
         "The first step is establishing the existence of an outbreak, then preparing for field work and verifying the diagnosis; descriptive epidemiology follows the defining of cases."],
        ["After the hypothesis is refined",
         "Refining the hypothesis comes after it has been developed and evaluated, which depends on data already oriented by descriptive epidemiology once cases were defined and identified."],
        ["After control methods are implemented",
         "Control and prevention methods come near the end, after the hypothesis is refined; descriptive epidemiology is used much earlier, right after cases are defined and identified."]],
  mis={"Before the outbreak is established": "puts a middle step ahead of the first step",
       "After the hypothesis is refined": "confuses describing the data with the later hypothesis steps",
       "After control methods are implemented": "puts describing the data after the response"},
  c=0, cite=cs(62),
  guide_quote="Use descriptive epidemiology to describe and orient the data."),

]
