# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 study guide -- section 3, Lecture 11 (Drugs for Pulmonary Infections, Asthma and COPD).

Imported by build_pharm_e3_guide.py.

SOURCES
  Facts   "Pulmonology-2.pptx" (109 slides; Adam Wood, Pharm.D., DABAT). `python3 tools/pharm_e3_lib.py dump L11`
          prints the slide text. The deck has NO speaker notes. Every picture was viewed: the content pictures were
          read by eye into tools/pharm_e3/ocr.json under "L11" (slide 21 the nosocomial pneumonia algorithm, 33 the
          tuberculosis drug targets, 58-61 and 76 the asthma inflammation figures and the leukotriene pathway, which
          are embedded Word objects on 59, 61 and 76, 65 the severity table, 69 beta-2 signaling, 90 the stepwise
          asthma chart, 94 the inhaler parts, 101 the lung-function decline in COPD). Slides 33, 69 and 90 are shown
          as cited figures; the slide 21 algorithm and the slide 65 table are reproduced as text. Decorative or
          non-content pictures (5, 32, 37, 40 and 43 structures, 49, 52, 91, 93, 96) are described, not shown.
  Weight  Dr. Wood's live stream of 2026-10-26 (1:53:07; Whisper transcript only, no caption track exists). Star
          boxes quote it with timestamps; a star sets weight and adds no fact.

SLIDES WIN (standing rule, 2026-10-15). Where a slide differs from current guidelines, one short "Current guidelines
differ" note follows the slide fact. Where the slides contradict themselves or a slide is factually wrong, the guide
prints the slide, says so in one line, and no question turns on the point (see tools/pharm_e3 keying list in the
pool docstrings).

NO DOSES. Milligram amounts (tuberculosis regimen, bupropion, continuous albuterol), fluid volumes (slide 50) and
epinephrine concentrations (slide 52) are left out. Durations, routes and timings stay.
"""

TOC = '''  <a class="top-link" href="#pulmonary">3 &middot; Drugs for Pulmonary Infections, Asthma and Chronic Obstructive Pulmonary Disease</a>
  <a href="#pu-bronchitis">3.1 Objectives 1&ndash;3 &mdash; Acute bronchitis</a>
  <a href="#pu-cap">3.2 Objectives 1&ndash;3 and 9 &mdash; Community-acquired pneumonia</a>
  <a href="#pu-hap">3.3 Objectives 3 and 9 &mdash; Nosocomial pneumonia: who gets it, what causes it, how wide to cover</a>
  <a href="#pu-hapdrugs">3.4 Objectives 1&ndash;9 &mdash; The hospital pneumonia antibiotics</a>
  <a href="#pu-tb">3.5 Objectives 1, 3 and 9 &mdash; Tuberculosis: the organism and combination therapy</a>
  <a href="#pu-tbdrugs">3.6 Objectives 1&ndash;10 &mdash; Isoniazid, rifampin, ethambutol, pyrazinamide</a>
  <a href="#pu-anaphylaxis">3.7 Objectives 1&ndash;6 &mdash; Anaphylaxis treatment</a>
  <a href="#pu-asthma">3.8 Objectives 1&ndash;3 &mdash; Asthma: the disease and the three ways to treat it (with a memory aid)</a>
  <a href="#pu-bronchodilators">3.9 Objectives 1&ndash;9 &mdash; Bronchodilators: beta-2 agonists, theophylline, anticholinergics</a>
  <a href="#pu-controllers">3.10 Objectives 1&ndash;10 &mdash; Controllers: corticosteroids, montelukast, mast cell stabilizers, biologics</a>
  <a href="#pu-inhalers">3.11 Objectives 9&ndash;10 &mdash; Stepwise therapy, inhaler devices, technique and status asthmaticus</a>
  <a href="#pu-copd">3.12 Objectives 1&ndash;10 &mdash; Chronic obstructive pulmonary disease, smoking cessation and immunizations</a>
  <a href="#pu-summary">3.13 Objectives 4 and 8&ndash;10 &mdash; Absorption and elimination, interactions, monitoring and patient education</a>'''


def star(at, quote, takeaway):
    return ('''
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At %s of the recording: <em>&ldquo;%s&rdquo;</em></p>
    <p>%s</p>
  </div>
''' % (at, quote, takeaway))


def fig(src, alt, cap, slide):
    return ('''
  <figure class="fig l11fig"><img src="pharm-e3-images/%s" loading="lazy" alt="%s"><figcaption>%s <span class="cite">Pulmonology-2.pptx, slide %d</span></figcaption></figure>
''' % (src, alt, cap, slide))


BODY = '''
<style>
  figure.l11fig{margin:14px 0 16px;max-width:640px}
  figure.l11fig img{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:8px;background:#fff}
  figure.l11fig figcaption{font-size:.86rem;line-height:1.45;color:var(--soft);margin-top:6px}
  figure.l11fig .cite{display:block;font-size:.78rem;opacity:.85;margin-top:2px}
</style>
<section class="deck" id="pulmonary">
  <h2 class="deck-title">3 &middot; Drugs for Pulmonary Infections, Asthma and Chronic Obstructive Pulmonary Disease</h2>
  <p class="lecturer">Adam Wood, Pharm.D., DABAT</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Identify respiratory drug classes and commonly prescribed drugs for pulmonary infections, asthma, and COPD/COLD.</li>
      <li>Describe the molecular mechanism of action of drugs used for pulmonary infections, asthma, and COPD/COLD.</li>
      <li>Identify indications for drugs used for pulmonary infections, asthma, and COPD/COLD.</li>
      <li>Describe absorption, distribution, metabolism, and excretion of drugs used for pulmonary infections, asthma, and COPD/COLD.</li>
      <li>Summarize side effects and toxic manifestations of respiratory drugs.</li>
      <li>Describe adverse effects of drugs used for pulmonary infections, asthma, and COPD/COLD.</li>
      <li>Identify contraindications for drugs used for pulmonary infections, asthma, and COPD/COLD.</li>
      <li>Discuss potential drug-drug, drug-food, and drug-herb interactions with drugs used for pulmonary infections, asthma, and COPD/COLD.</li>
      <li>List commonly used protocols and patient monitoring for pulmonary infections, asthma, and COPD/COLD.</li>
      <li>Outline appropriate patient education for drugs used for pulmonary infections, asthma, and COPD/COLD.</li>
    </ol>
  </div>
  <p>COPD/COLD in the objectives = chronic obstructive pulmonary disease / chronic obstructive lung disease. The rest of
  this section spells it out.</p>

  <div class="callout"><strong>The third of five lectures in Exam 3, and the longest.</strong> Dr. Wood delivered Lecture 11 live on
  October 26, 2026 (109 slides; the stream runs 1 hour 53 minutes). It has two halves: <strong>pulmonary infections</strong>
  (acute bronchitis, community-acquired and nosocomial pneumonia and their antibiotics, tuberculosis) and the
  <strong>airway drugs</strong> (anaphylaxis, asthma, the inhaler devices, chronic obstructive pulmonary disease and smoking cessation).
  He covered every slide in order, then took two questions. <strong>The recording has one transcript only</strong>: a machine
  transcription, with no captions to check it against, so each garbled drug name was read from its slide and nothing below rests on
  a garbled stretch of audio alone.</div>

  <div class="callout"><strong>What he stresses, and what he said he will not test.</strong> (From the recording; the transcript is a machine transcription only, so every point below is tied to a slide.)
  <ul>
    <li><strong>The broad nosocomial regimen.</strong> &ldquo;There will be a question like this on the test&rdquo; (22:56; also 18:41): a list of drug names; name each drug&rsquo;s class and decide whether the regimen is valid. One antipseudomonal beta-lactam + one antipseudomonal fluoroquinolone or aminoglycoside + vancomycin or linezolid (3.3).</li>
    <li><strong>Quick relief or controller</strong>, for every asthma drug: &ldquo;those are easy test questions I can ask&rdquo; (54:21; again at 1:36:06).</li>
    <li><strong>Stepwise asthma therapy as a ladder</strong>: what to start, and what to move up to next (1:27:49); no doses (3.11).</li>
    <li><strong>Never a long-acting beta-2 agonist alone in asthma</strong> (1:04:05); <strong>rifampin is an inducer</strong>, &ldquo;really, really important&rdquo; (42:16); <strong>renal adjustment for every hospital pneumonia antibiotic except linezolid</strong> (25:25).</li>
    <li><strong>Compare chronic obstructive pulmonary disease with asthma</strong> (1:39:46): in chronic obstructive pulmonary disease a long-acting bronchodilator alone is fine, the steroid comes last and there are no biologics (3.12).</li>
    <li><strong>Not tested, in his words:</strong> the pathogen lists by setting (8:41, learn the trend); the second-line tuberculosis list (45:56, &ldquo;I would not memorize this list&rdquo;); the vancomycin trough number (29:58); classifying a patient&rsquo;s asthma severity (58:44); which interleukin each biologic targets (1:14:19); doses (1:29:03).</li>
    <li><strong>Slide points he affirmed aloud</strong> where current guidelines differ, so each is asked once as the slide says: ceftazidime not recommended (24:33) and the 5-day steroid taper rule (1:22:13). He also repeated montelukast&rsquo;s &ldquo;minimal side effects&rdquo; (1:09:59) and theophylline&rsquo;s renal elimination (1:17:44); those two stay unasked (3.9, 3.10).</li>
  </ul></div>
'''

# ------------------------------------------------------------------------------------------------- 3.1 bronchitis
BODY += '''
  <h3 class="sub" id="pu-bronchitis">3.1 &middot; Objectives 1&ndash;3 &mdash; Acute bronchitis</h3>

  <p><strong>What it is [slide 5].</strong> Bronchitis is <strong>inflammation of one or more bronchi</strong>, generally
  secondary to infection. It <strong>does not involve the bronchioles and alveoli</strong> (that is what separates it from
  pneumonia). <strong>Acute</strong> bronchitis affects all ages; <strong>chronic</strong> bronchitis primarily affects patients
  with chronic obstructive pulmonary disease. The slide picture shows a normal bronchial tube beside an inflamed one with
  thick mucus.</p>

  <p><strong>Causes [slide 6].</strong></p>
  <ul>
    <li><strong>Common causes: viruses</strong> &mdash; rhinovirus, coronavirus, influenza, adenovirus.</li>
    <li><strong>Occasionally bacterial</strong> &mdash; <em>Mycoplasma pneumoniae</em>, <em>Chlamydia pneumoniae</em>, <em>Bordetella pertussis</em>;
    <em>Streptococcus</em>, <em>Staphylococcus</em> and <em>Haemophilus</em> species, which may occur secondary to a viral illness.</li>
  </ul>

  <p><strong>Treatment (Objective 3) [slides 7 and 8].</strong></p>
  <ul>
    <li><strong>Generally self-limited: symptomatic and supportive care only</strong> &mdash; analgesics, antipyretics, antitussives, fluids [slide 7].</li>
    <li><strong>Possibly avoid antihistamines and sympathomimetics:</strong> they <strong>dehydrate bronchial secretions</strong> and may prolong symptoms [slide 7].</li>
    <li><strong>Routine antibiotics are not recommended</strong>; acute bronchitis is a common cause of unnecessary antibiotic prescription [slide 8].</li>
    <li><strong>Symptoms persisting more than 5 days:</strong> consider bacterial involvement [slide 8]. Then:
      <ul>
        <li><strong>Doxycycline</strong> is <strong>preferred if <em>Mycoplasma</em> is documented</strong>, because of macrolide resistance.</li>
        <li><strong>Macrolides</strong>: azithromycin, erythromycin, clarithromycin.</li>
        <li><strong>A respiratory fluoroquinolone is avoided unless there was recent antibiotic exposure</strong>, which raises the risk of resistant <em>Streptococcus pneumoniae</em>.</li>
      </ul></li>
  </ul>
'''

# ------------------------------------------------------------------------------------------------- 3.2 CAP
BODY += '''
  <h3 class="sub" id="pu-cap">3.2 &middot; Objectives 1&ndash;3 and 9 &mdash; Community-acquired pneumonia</h3>

  <p><strong>How microbes reach the lung [slide 10].</strong></p>
  <ul>
    <li><strong>Aspiration from the oropharynx</strong> &mdash; common in the elderly.</li>
    <li><strong>Inhalation of infectious aerosols.</strong></li>
    <li><strong>Hematogenous dissemination.</strong></li>
    <li><strong>Direct inoculation and contiguous spread</strong>, for example trauma.</li>
  </ul>

  <p><strong>Diagnosis (Objective 9) [slide 11].</strong></p>
  <ul>
    <li><strong>Outpatients do well with empiric antibiotics</strong>; diagnostic tests are not routinely performed.</li>
    <li><strong>Hospitalized patients: blood and sputum cultures, drawn before antibiotics are given.</strong></li>
    <li><strong>Sputum Gram stain and culture are controversial</strong>: expectorated sputum is frequently contaminated, and the responsible pathogen is not always identified.</li>
  </ul>
''' + star("6:30", "If they&rsquo;re sick enough, though, to become hospitalized, then we definitely want to get blood and sputum cultures&hellip; And this needs to be done prior to antibiotics. This is really, really important because if you get the order confused and give the antibiotics first, there&rsquo;s a possibility you wipe out those bacteria and then nothing grows on the culture.",
           "<mark class=\"prof-highlight\">Hospitalized: blood and sputum cultures BEFORE the first antibiotic</mark> [slide 11]. Outpatients are treated empirically.") + '''

  <p><strong>Likely pathogens by setting [slide 12].</strong></p>
  <table>
    <tr><th>Setting</th><th>Pathogens [slide 12]</th></tr>
    <tr><td><strong>Outpatient</strong></td><td><em>Streptococcus pneumoniae</em>, <em>Mycoplasma pneumoniae</em>, <em>Haemophilus influenzae</em>, <em>Moraxella catarrhalis</em>, respiratory viruses</td></tr>
    <tr><td><strong>Inpatient, not in the intensive care unit</strong></td><td><em>S. pneumoniae</em>, <em>M. pneumoniae</em>, <em>Chlamydia pneumoniae</em>, <em>H. influenzae</em>, <em>Legionella</em> species, aspiration, respiratory viruses</td></tr>
    <tr><td><strong>Inpatient, intensive care unit</strong></td><td><em>S. pneumoniae</em>, <strong><em>Staphylococcus aureus</em></strong>, <em>Legionella</em> species, <strong>gram-negative bacilli</strong>, <em>H. influenzae</em></td></tr>
  </table>
''' + star("8:41", "I&rsquo;m not having you to memorize this exact list, right, but it&rsquo;s how we kind of link back to why do we use the drugs that we do, right? Why is it that a patient who&rsquo;s going to the ICU gets a bigger caliber of drug compared to those who are outpatient?",
           "Learn the trend, not the lists: <mark class=\"prof-highlight\">the sicker the setting, the tougher the organisms; the intensive care unit list adds <em>Staphylococcus aureus</em> and gram-negative bacilli</mark> [slide 12], which is why the intensive care unit regimen adds methicillin-resistant <em>S. aureus</em> coverage [slide 15].") + '''

  <p><strong>Risk factors for penicillin-resistant <em>Streptococcus pneumoniae</em> [slide 13].</strong> They decide the outpatient regimen.</p>
  <ul>
    <li><strong>Age over 65 years</strong></li>
    <li><strong>A beta-lactam within the past 3 months</strong></li>
    <li><strong>Alcoholism</strong></li>
    <li><strong>Immunosuppression</strong></li>
    <li><strong>Medical comorbidities</strong> &mdash; diabetes, renal insufficiency, congestive heart failure, coronary artery disease, malignancy and so on</li>
    <li><strong>Exposure to a child in a day care center</strong></li>
  </ul>
''' + star("9:12", "One in particular is if we have a risk for penicillin-resistant strep pneumo, that&rsquo;s going to be a big decision point of whether we need to upgrade kind of the spectrum of drugs that we&rsquo;re using here.",
           "<mark class=\"prof-highlight\">Any one risk factor moves the outpatient from a macrolide alone to a beta-lactam plus a macrolide, or a respiratory fluoroquinolone</mark> [slides 13 and 14].") + '''

  <p><strong>Empiric treatment (Objective 3) [slides 14 and 15].</strong></p>
  <table>
    <tr><th>Setting</th><th>Regimen</th></tr>
    <tr><td><strong>Outpatient, no risk of resistant <em>S. pneumoniae</em></strong> [slide 14]</td><td><strong>First line: a macrolide</strong> &mdash; azithromycin, clarithromycin.<br><strong>Second line:</strong> doxycycline, minocycline.</td></tr>
    <tr><td><strong>Outpatient, risk factors for resistant <em>S. pneumoniae</em></strong> [slide 14]</td><td><strong>A beta-lactam plus a macrolide</strong> &mdash; the beta-lactam is amoxicillin with or without clavulanic acid, or cefuroxime or cefpodoxime (second- or third-generation cephalosporins);<br><strong>or a respiratory fluoroquinolone</strong> (levofloxacin, moxifloxacin), <strong>good for patients with a beta-lactam allergy</strong>.</td></tr>
    <tr><td><strong>Inpatient, not in the intensive care unit</strong> [slide 15]</td><td><strong>An intravenous beta-lactam</strong> (cefotaxime, ceftriaxone, high-dose ampicillin) <strong>plus</strong> an intravenous or oral <strong>macrolide</strong>, <strong>or</strong> plus doxycycline; <strong>or a respiratory fluoroquinolone</strong> (beta-lactam allergy).</td></tr>
    <tr><td><strong>Intensive care unit</strong> [slide 15]</td><td><strong>The same, but every drug intravenous from the start</strong>; consider <strong>methicillin-resistant <em>Staphylococcus aureus</em> (MRSA) coverage</strong> if warranted.</td></tr>
  </table>
  <div class="callout"><strong>Current guidelines differ:</strong> the 2019 community-acquired pneumonia guideline prefers amoxicillin or
  doxycycline for a healthy outpatient and keeps a macrolide alone for areas where pneumococcal macrolide resistance is low.
  The slide (macrolide first line) is what is tested.</div>
'''

# ------------------------------------------------------------------------------------------------- 3.3 nosocomial
BODY += '''
  <h3 class="sub" id="pu-hap">3.3 &middot; Objectives 3 and 9 &mdash; Nosocomial pneumonia: who gets it, what causes it, how wide to cover</h3>

  <p><strong>Definition [slide 16].</strong> Nosocomial pneumonia is an <strong>infection of the lung not present at the time of
  admission</strong>, occurring <strong>more than 48 hours after hospital admission</strong>. It includes hospital-acquired,
  ventilator-associated and health-care associated pneumonia. It is the <strong>second most common infection in hospitalized
  patients, after urinary tract infection</strong>, with a higher incidence in the elderly and in mechanically ventilated patients
  and higher mortality and hospital costs.</p>

  <p><strong>Health-care associated pneumonia: the criteria [slide 17].</strong> Pneumonia in a patient who meets any of these:</p>
  <ul>
    <li>Hospitalized in an acute care facility for <strong>more than 2 days in the past 90 days</strong></li>
    <li>Lives in a <strong>nursing home or long-term care facility</strong></li>
    <li><strong>Recent intravenous antibiotics</strong></li>
    <li><strong>Chemotherapy</strong></li>
    <li><strong>Wound care in the previous 30 days</strong></li>
    <li><strong>A hemodialysis patient</strong></li>
  </ul>
  <div class="callout"><strong>Current guidelines differ:</strong> the 2016 hospital-acquired and ventilator-associated pneumonia
  guideline dropped health-care associated pneumonia as a separate category. The slide&rsquo;s criteria are what is tested.</div>

  <p><strong>Risk factors [slide 18].</strong></p>
  <table>
    <tr><th>Unmodifiable</th><th>Modifiable</th></tr>
    <tr><td>Age over 70 years; chronic lung disease; depressed consciousness; large-volume aspiration; hospitalized during the winter months</td>
        <td><strong>Mechanical ventilation</strong>; nasogastric tube; intracranial pressure monitor; <strong>histamine H2 blocker or antacid therapy</strong>; previous antibiotic exposure; reintubation</td></tr>
  </table>

  <p><strong>What causes it [slide 19].</strong></p>
  <ul>
    <li><strong>Gram-negative bacilli:</strong> <strong><em>Pseudomonas aeruginosa</em> (the most common)</strong>, <em>Escherichia coli</em>, <em>Klebsiella pneumoniae</em>, <em>Acinetobacter</em>, <em>Enterobacter</em> and <em>Serratia</em> species.</li>
    <li><strong>Gram-positive cocci:</strong> <strong>methicillin-resistant <em>Staphylococcus aureus</em> (the most common)</strong>, <em>Streptococcus pneumoniae</em>.</li>
    <li><strong>Fungi:</strong> <em>Candida</em> species, <em>Aspergillus fumigatus</em>.</li>
  </ul>

  <p><strong>Treatment principles (Objective 9) [slide 20].</strong></p>
  <ul>
    <li><strong>Start therapy as soon as possible; do not wait for a definitive culture.</strong></li>
    <li><strong>Start broad-spectrum antibiotics</strong>, considering multidrug-resistant pathogens: the regimen <strong>must cover methicillin-resistant <em>S. aureus</em> and <em>Pseudomonas</em></strong>.</li>
    <li><strong>Streamline therapy once cultures and sensitivities are available.</strong></li>
  </ul>
  <p>The &ldquo;must cover&rdquo; line applies when multidrug-resistant pathogens are a concern: the next slides give a <strong>limited-spectrum</strong>
  regimen, not built to cover either organism, for patients without those risk factors [slides 21 and 22].</p>

  <p><strong>Limited or broad? The algorithm [slide 21].</strong></p>
  <table>
    <tr><th>Hospital-acquired, ventilator-associated or health-care associated pneumonia suspected. Late onset (5 days or more) or risk factors for multidrug-resistant pathogens (prior antibiotics, colonization, hospitalization or chronic care, immunosuppressive disease or therapy)?</th><th>Start</th></tr>
    <tr><td><strong>No</strong></td><td><strong>Limited-spectrum</strong> initial antibiotic therapy [slide 22]</td></tr>
    <tr><td><strong>Yes</strong></td><td><strong>Broad-spectrum</strong> initial antibiotic therapy for multidrug-resistant pathogens [slide 23]</td></tr>
  </table>

  <table>
    <tr><th>Limited-spectrum empiric coverage: no multidrug-resistance risk factors [slide 22]</th><th>Broad-spectrum empiric coverage: multidrug-resistance risk factors present [slide 23]</th></tr>
    <tr><td><strong>One</strong> of:
      <ul>
        <li><strong>Ceftriaxone</strong> (third-generation cephalosporin)</li>
        <li><strong>Levofloxacin or moxifloxacin</strong> &mdash; <strong>choose this group if worried about atypical pathogens</strong></li>
        <li><strong>Ampicillin/sulbactam</strong></li>
        <li><strong>Ertapenem</strong> (narrow-spectrum carbapenem)</li>
      </ul></td>
      <td><strong>Gram-negative combination therapy:</strong> an antipseudomonal cephalosporin, <strong>or</strong> antipseudomonal carbapenem,
      <strong>or</strong> antipseudomonal penicillin/beta-lactamase inhibitor, <strong>plus</strong> an antipseudomonal fluoroquinolone
      (levofloxacin, ciprofloxacin) <strong>or</strong> an aminoglycoside;
      <br><strong>plus gram-positive coverage: vancomycin or linezolid.</strong></td></tr>
  </table>
''' + star("22:56", "If I put an answer choice and I say, hey, you&rsquo;re suspecting a patient has ventilator associated pneumonia, which of these regimens is going to be sufficient for empiric treatment?&hellip; There will be a question like this on the test and you&rsquo;re going to get a bunch of drug names and your job is to be able to identify what classes they come from and then is that an appropriate regimen?",
           "He said it twice (also at 18:41) and called it &ldquo;at least one question&rdquo; (24:24). <mark class=\"prof-highlight\">A broad regimen is three drugs: ONE antipseudomonal beta-lactam, plus ONE antipseudomonal fluoroquinolone or aminoglycoside, plus vancomycin or linezolid</mark> [slide 23]. His own examples of what fails: two beta-lactams together (&ldquo;They do the same thing. We are shooting for synergy, so we want different mechanisms,&rdquo; 22:45), and two drugs for methicillin-resistant <em>S. aureus</em> with only one gram-negative drug (23:59).") + '''
  <div class="callout"><strong>Checking a broad regimen in four steps [slides 23 to 30].</strong>
  <ol>
    <li><strong>Name each drug&rsquo;s class.</strong></li>
    <li><strong>Exactly one antipseudomonal beta-lactam:</strong> an antipseudomonal cephalosporin (<strong>cefepime</strong>, ceftazidime), an antipseudomonal carbapenem (<strong>imipenem/cilastatin, meropenem</strong>; <em>not</em> ertapenem, which has limited <em>Pseudomonas</em> activity), or an antipseudomonal penicillin (<strong>piperacillin/tazobactam</strong>).</li>
    <li><strong>Plus exactly one second gram-negative drug of another class:</strong> an antipseudomonal fluoroquinolone (<strong>levofloxacin, ciprofloxacin</strong>) or an aminoglycoside (<strong>gentamicin, tobramycin, amikacin</strong>).</li>
    <li><strong>Plus exactly one gram-positive drug:</strong> <strong>vancomycin or linezolid</strong>.</li>
  </ol>
  Two beta-lactams, two gram-positive drugs, a missing gram-negative partner, or a limited-spectrum drug (ceftriaxone, moxifloxacin, ampicillin/sulbactam, ertapenem) in the beta-lactam slot all make the regimen inappropriate.</div>

  <p><strong>After the first days (Objective 9) [slide 31].</strong></p>
  <ul>
    <li><strong>Scale back antibiotic coverage as cultures become available.</strong></li>
    <li><strong>Switch to oral therapy when possible</strong> (cheaper).</li>
    <li><strong>Failure of therapy</strong> has three explanations:
      <strong>wrong therapy</strong> (resistant pathogens, inadequate antimicrobial therapy),
      <strong>wrong diagnosis</strong> (pulmonary embolus, neoplasm and so on), or
      <strong>complications</strong> (<em>Clostridioides difficile</em> colitis, empyema or lung abscess).</li>
    <li><strong>Duration:</strong> 7 to 8 days (10 to 14 for <em>P. aeruginosa</em>, <em>Acinetobacter baumannii</em>, <em>Burkholderia cepacia</em> or <em>Stenotrophomonas maltophilia</em>).</li>
  </ul>
  <div class="callout"><strong>Current guidelines differ:</strong> the 2016 guideline recommends about 7 days for most hospital-acquired
  and ventilator-associated pneumonia, including <em>Pseudomonas</em>; no question here turns on the longer duration.</div>
'''

# ------------------------------------------------------------------------------------------------- 3.4 hospital antibiotics
BODY += '''
  <h3 class="sub" id="pu-hapdrugs">3.4 &middot; Objectives 1&ndash;9 &mdash; The hospital pneumonia antibiotics</h3>

  <p>Every antipseudomonal agent on these slides, the aminoglycosides and vancomycin <strong>require renal adjustment</strong>;
  <strong>linezolid does not</strong> [slides 24 to 30].</p>
  <table>
    <tr><th>Drug (brand)</th><th>What the slides say</th></tr>
    <tr><td><strong>Ceftazidime</strong> (Fortaz) &mdash; antipseudomonal cephalosporin</td><td>Not recommended because of rapid development of resistance; rarely used. <strong>Requires renal adjustment</strong> [slide 24]</td></tr>
    <tr><td><strong>Cefepime</strong> (Maxipime) &mdash; antipseudomonal cephalosporin</td><td><strong>Fourth-generation cephalosporin. Requires renal adjustment</strong> [slide 24]</td></tr>
    <tr><td><strong>Imipenem/cilastatin</strong> (Primaxin) &mdash; antipseudomonal carbapenem</td><td><strong>Use with caution in patients with a seizure history.</strong> Renal adjustment [slide 25]</td></tr>
    <tr><td><strong>Meropenem</strong> (Merrem) &mdash; antipseudomonal carbapenem</td><td><strong>Less risk for seizures.</strong> Renal adjustment [slide 25]</td></tr>
    <tr><td><strong>Ertapenem</strong></td><td><strong>Limited activity against <em>P. aeruginosa</em></strong> [slide 25]; it is the narrow-spectrum carbapenem of the limited-spectrum list [slide 22]</td></tr>
    <tr><td><strong>Piperacillin/tazobactam</strong> (Zosyn) &mdash; antipseudomonal penicillin</td><td>Requires renal adjustment [slide 26]</td></tr>
    <tr><td><strong>Ticarcillin/clavulanate</strong> (Timentin) &mdash; antipseudomonal penicillin</td><td>Not used very often: increased gram-negative resistance. Renal adjustment [slide 26]</td></tr>
    <tr><td><strong>Ciprofloxacin</strong> (Cipro), <strong>levofloxacin</strong> (Levaquin) &mdash; antipseudomonal fluoroquinolones</td><td><strong>Good activity against atypicals</strong> (<em>Mycoplasma</em>, <em>Chlamydia</em>, <em>Legionella</em>); <strong>good lung tissue penetration</strong>; increasing use is producing gram-negative resistance, so <strong>use judiciously</strong>. Renal adjustment [slide 27]. <em>Fluoroquinolones also carry a Food and Drug Administration boxed warning (tendon rupture, peripheral neuropathy, central nervous system effects); the slide does not list it.</em></td></tr>
    <tr><td><strong>Gentamicin, tobramycin, amikacin</strong> &mdash; aminoglycosides</td><td><strong>Extended-interval dosing</strong> (once daily or longer), because of <strong>poor lung penetration: bigger doses give higher concentrations</strong>. Adjust dose and frequency <strong>based on levels</strong>; <strong>highly dependent on renal function</strong>; <strong>ototoxicity and nephrotoxicity</strong> [slide 28]. <em>The nephrotoxicity and ototoxicity are also a boxed warning.</em></td></tr>
    <tr><td><strong>Vancomycin</strong></td><td><strong>Primarily used for empiric methicillin-resistant <em>S. aureus</em> coverage.</strong> A goal trough is drawn <strong>before the third or fourth dose (steady state)</strong>. Requires renal adjustment; <strong>ototoxicity</strong>; <strong>nephrotoxic, with other nephrotoxins</strong> [slide 29]</td></tr>
    <tr><td><strong>Linezolid</strong> (Zyvox)</td><td><strong>Great methicillin-resistant <em>S. aureus</em> coverage</strong>; <strong>intravenous and oral forms</strong>; <strong>good lung penetration</strong>; expensive; <strong>no dose adjustment for renal function</strong> [slide 30]</td></tr>
  </table>
''' + star("24:33", "Antipseudomonal cephalosporins, [ceftazidime&rsquo;s] not a really good player here because of resistance issues. We&rsquo;re going to stick with cefepime. Maxipime&rsquo;s going to be our fourth generation of choice here to cover for pseudomonas.",
           "<mark class=\"prof-highlight\">Cefepime is the antipseudomonal cephalosporin of choice; ceftazidime is set aside for rapid resistance</mark> [slide 24]. (The transcript renders the drug name as &ldquo;tetazodine&rsquo;s&rdquo;; slide 24 names it.)") + star("25:25", "Note the exceptions when I go through and say, hey, this one doesn&rsquo;t require renal dose adjustment. That&rsquo;s a good thing to know. Otherwise, most of these do require adjustments&hellip; [of linezolid, at 31:20] Finally, the one thing that doesn&rsquo;t require renal dose adjustment.",
           "<mark class=\"prof-highlight\">Renal adjustment for all of them except linezolid</mark> [slides 24 to 30].") + star("28:06", "These, you definitely have to adjust for renal function, but these are going to be looking at with therapeutic drug monitoring&hellip; If those levels start to climb up, they&rsquo;re going to be at risk for that ototoxicity and the nephrotoxicity, right?&hellip; So certainly really important to watch like a hawk.",
           "<mark class=\"prof-highlight\">Aminoglycosides: dose and frequency follow levels; ototoxicity and nephrotoxicity</mark> [slide 28]. Vancomycin shares both toxicities [slide 29].") + star("29:58", "You don&rsquo;t have to memorize the specific goal trough level.",
           "The vancomycin trough is drawn <strong>before the third or fourth dose (steady state)</strong> [slide 29]; the number itself is not tested. (The transcript reads &ldquo;gold trough&rdquo;: goal trough.)") + '''
  <div class="callout"><strong>Current guidelines differ:</strong> ceftazidime is still listed as an antipseudomonal option for
  hospital-acquired pneumonia; the slide&rsquo;s &ldquo;not recommended&rdquo;, which Dr. Wood affirmed aloud (24:33), is what is tested, and one question
  asks why it is rarely used. Vancomycin is now usually dosed to an area-under-the-curve target rather than the trough value on the
  slide (the trough number is not asked). Ticarcillin/clavulanate is no longer marketed in the United States (&ldquo;I&rsquo;ve never actually
  seen that out in the wild,&rdquo; 26:32); no question is built on choosing it.</div>
'''

# ------------------------------------------------------------------------------------------------- 3.5 tuberculosis
BODY += '''
  <h3 class="sub" id="pu-tb">3.5 &middot; Objectives 1, 3 and 9 &mdash; Tuberculosis: the organism and combination therapy</h3>

  <p><strong>The organism [slide 34].</strong> Mycobacteria are <strong>acid-fast bacilli</strong> with a distinct phosphoglycolipid layer
  (<strong>mycolic acid</strong>) that forms a <strong>waxy cell coat</strong>. <em>Mycobacterium tuberculosis</em> is <strong>very slow growing</strong>
  and can exist in <strong>dormant states</strong> for long periods, so <strong>antimicrobials that affect cell division do not work as well</strong>.</p>
''' + fig("l11-slide-33.jpg", "A tuberculosis bacillus with three magnified insets. Isoniazid and ethambutol point at the layers of the cell wall, rifampin at RNA polymerase, and pyrazinamide, with question marks, at the plasma membrane and at adenosine triphosphate (ATP) synthesis.",
          "Where the four first-line drugs act: <strong>isoniazid</strong> and <strong>ethambutol</strong> inhibit cell wall synthesis (the mycolic acid and arabinogalactan layers), <strong>rifampin</strong> inhibits RNA synthesis at RNA polymerase, and <strong>pyrazinamide</strong>&rsquo;s exact target is unclear (it disrupts the plasma membrane and energy metabolism).", 33) + '''
  <p><strong>Combination therapy (Objective 9) [slide 35].</strong> The milligram amounts on the slide are not tested.</p>
  <table>
    <tr><th>Phase</th><th>Drugs</th></tr>
    <tr><td><strong>First 2 months</strong></td><td><strong>Isoniazid, rifampin, ethambutol, pyrazinamide</strong> (four drugs)</td></tr>
    <tr><td><strong>Then 4 months</strong></td><td><strong>Isoniazid and rifampin</strong></td></tr>
  </table>
''' + star("35:42", "We start off with four drugs in the beginning, a useful acronym, a student just reminded me of is RIPE. So rifampin, isoniazid, pyrazinamide, ethambutol&hellip; And so we&rsquo;re gonna do that for two months.",
           "<mark class=\"prof-highlight\">RIPE (rifampin, isoniazid, pyrazinamide, ethambutol) for 2 months, then rifampin and isoniazid for 4</mark> [slide 35]; six months is the minimum [slide 36].") + '''

  <p><strong>How long [slide 36].</strong></p>
  <ul>
    <li><strong>Pulmonary tuberculosis:</strong> 6 to 9 months.</li>
    <li><strong>Patients with HIV (human immunodeficiency virus) and tuberculosis:</strong> 9 to 12 months.</li>
    <li><strong>Complicated (other body parts):</strong> 18 to 24 months.</li>
    <li><strong>Never use single agents in active disease</strong>: combination therapy prevents the development of resistance.</li>
  </ul>
  <div class="callout"><strong>Current guidelines differ:</strong> most patients with HIV now receive the standard 6-month regimen, most
  tuberculosis outside the lungs is treated for 6 to 12 months, and newer regimens for drug-resistant disease can be much shorter than the
  18 to 24 months on the slides. The slides&rsquo; durations are printed; no question here keys the longer durations.</div>

  <p><strong>Resistance and the second-line agents [slide 46].</strong> With <strong>isoniazid or rifampin resistance, treat 18 to 24 months</strong>.
  Other agents are used for resistance or drug intolerance. <strong>Not tested:</strong> no question, drill or card here asks about them.</p>
''' + star("45:56", "Here&rsquo;s a list of other agents you may see occasionally. I would not memorize this list&hellip; I&rsquo;m not going to quiz you on them so specifically. I&rsquo;d rather you know those big four more clearly there.",
           "Know the <mark class=\"prof-highlight\">big four</mark> (3.6); the list below is for reference only.") + '''
  <table>
    <tr><th>Agent</th><th>For reference only [slide 46]</th></tr>
    <tr><td><strong>Streptomycin</strong></td><td>Auditory and vestibular toxicity</td></tr>
    <tr><td><strong>Aminosalicylic acid</strong></td><td>Gastrointestinal problems</td></tr>
    <tr><td><strong>Cycloserine</strong></td><td>Central nervous system: psychosis, seizures</td></tr>
    <tr><td><strong>Rifabutin, macrolides, quinolones</strong></td><td>Alternatives</td></tr>
    <tr><td><strong>Clofazimine</strong></td><td>A leprosy drug</td></tr>
    <tr><td><strong>Linezolid</strong></td><td>Also listed</td></tr>
  </table>
'''

# ------------------------------------------------------------------------------------------------- 3.6 TB drugs
BODY += '''
  <h3 class="sub" id="pu-tbdrugs">3.6 &middot; Objectives 1&ndash;10 &mdash; Isoniazid, rifampin, ethambutol, pyrazinamide</h3>

  <h4 class="subsub">Isoniazid [slides 37 to 39]</h4>
  <table>
    <tr><th>Topic</th><th>What the slides give</th></tr>
    <tr><td><strong>2 &middot; Mechanism</strong></td><td><strong>Inhibits mycolic acid production</strong>, so it inhibits the waxy cell coat [slide 37]. It is a prodrug: <strong>metabolically activated by the bacterial catalase-peroxidase</strong>; <strong>resistance</strong> comes from a <strong>mutation in the DNA coding for that activating enzyme</strong> [slide 38]</td></tr>
    <tr><td><strong>Killing</strong></td><td><strong>Bacteriostatic for latent bacteria, bactericidal for dividing bacteria</strong> [slide 37]</td></tr>
    <tr><td><strong>4 &middot; Absorption and elimination</strong></td><td><strong>Well absorbed, enters the central nervous system</strong> [slide 38]. 75 to 95 percent is excreted as an <strong>acetylated</strong> metabolite; <strong>fast and slow acetylators</strong> differ (half-life about 70 minutes against 2.5 hours) [slide 37]</td></tr>
    <tr><td><strong>3 &middot; Uses</strong></td><td><strong>Prophylaxis: used alone. Active disease: combination therapy</strong> [slide 39]</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Adverse effects</strong> [slide 39]</td><td>
      <strong>Allergic reactions: a lupus-like syndrome.</strong><br>
      <strong>Hepatitis</strong>, more common <strong>in alcoholics</strong> and <strong>with increasing age</strong>. <em>Hepatitis is also the drug&rsquo;s Food and Drug Administration boxed warning.</em><br>
      <strong>Peripheral neuritis</strong>, from <strong>pyridoxine deficiency</strong>: <strong>give pyridoxine (vitamin B6)</strong>.<br>
      <strong>Central nervous system:</strong> seizures, euphoria, psychosis, memory impairment.</td></tr>
  </table>
''' + star("39:30", "Anytime you hear that acetylation, you should think about that lupus-like effects&hellip; Isoniazid is really rough on the liver, so especially patients with alcoholism, elderly patients or just anyone with previous, pre-existing hepatic disease, you&rsquo;ve got to watch your LFTs very closely&hellip; make sure you&rsquo;re supplementing your B6.",
           "Isoniazid&rsquo;s four: <mark class=\"prof-highlight\">lupus-like syndrome (acetylation), hepatitis (alcohol, age), peripheral neuritis (give pyridoxine), central nervous system effects</mark> [slides 38 and 39]. LFTs = liver function tests.") + '''

  <h4 class="subsub">Rifampin [slides 40 to 42]</h4>
  <table>
    <tr><th>Topic</th><th>What the slides give</th></tr>
    <tr><td><strong>Origin and spectrum</strong></td><td>A semisynthetic form of rifamycin B from <em>Streptomyces mediterranei</em>; <strong>broad spectrum</strong> [slide 40]</td></tr>
    <tr><td><strong>2 &middot; Mechanism</strong></td><td><strong>Inhibits DNA-dependent RNA polymerase</strong>, forming a complex with the enzyme; <strong>no effect on the human enzyme</strong> [slide 41]</td></tr>
    <tr><td><strong>3 &middot; Uses</strong></td><td><strong>Rarely used alone because of rapid tolerance.</strong> Primary use: <strong>tuberculosis</strong>; also <strong>meningococcal disease prophylaxis</strong> and <strong>endocarditis</strong> [slide 41]. (Current latent tuberculosis guidance does include a rifampin-alone regimen; no question here keys &ldquo;never alone&rdquo; for rifampin.)</td></tr>
    <tr><td><strong>8 &middot; Interactions</strong></td><td><strong>Induces cytochrome P450 enzymes</strong> (CYP1A2, CYP2C9, CYP3A4), lowering <strong>anticoagulants, contraceptives</strong>, chloramphenicol, digoxin, ketoconazole and theophylline [slide 42]</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Adverse effects</strong> [slide 42]</td><td><strong>Jaundice and hepatitis</strong> (chronic liver disease); <strong>orange-colored secretions (tears, sweat, urine)</strong>; hypersensitivity: a <strong>flu-like syndrome</strong> in 20 percent of patients; gastrointestinal disturbances</td></tr>
  </table>
''' + star("42:16", "This is going to be a CYP3A4 inducer in particular&hellip; make note of it, because it&rsquo;s really, really important, but this is not an inhibitor, this is an inducer, so it&rsquo;s gonna cause levels of other drugs like certain anticoagulants or contraceptives or things like digoxin, it&rsquo;s gonna drop their levels and make those drugs less effective&hellip; the biggest thing is the drug interactions, liver injury, and again, the kind of color change.",
           "<mark class=\"prof-highlight\">Rifampin INDUCES cytochrome P450 (CYP3A4): anticoagulants, contraceptives and digoxin fall</mark> [slide 42]; warn a patient on an oral contraceptive (45:12). Then liver injury and orange secretions.") + '''
  <div class="callout"><strong>The slides disagree with microbiology:</strong> slide 40 lists <em>Neisseria</em> and <em>Legionella</em> among rifampin&rsquo;s
  gram-positive organisms, but both are gram-negative. No question here asks rifampin&rsquo;s spectrum lists.</div>

  <h4 class="subsub">Ethambutol [slides 43 and 44]</h4>
  <table>
    <tr><th>Topic</th><th>What the slides give</th></tr>
    <tr><td><strong>Killing and mechanism</strong></td><td><strong>Bacteriostatic.</strong> Mechanism unknown: it <strong>inhibits mycolic acid incorporation into membranes</strong>; no effect on other bacteria. The <strong>weakened cell wall lets the other agents in</strong> [slide 43]. (The slide 33 picture places it at the arabinogalactan layer of the cell wall, which is its target in current references.)</td></tr>
    <tr><td><strong>4 &middot; Elimination</strong></td><td><strong>75 percent excreted unchanged: adjust the dose in renal disease</strong> [slide 44]</td></tr>
    <tr><td><strong>Resistance</strong></td><td><strong>Develops quickly if used alone</strong> [slide 44]</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Adverse effects</strong> [slide 44]</td><td><strong>Visual disturbances: decreased red-green discrimination, decreased visual acuity</strong> (the slide notes &ldquo;limited in children&rdquo;); <strong>increased uric acid levels</strong></td></tr>
  </table>
''' + star("44:01", "The one unique kind of side effect you&rsquo;ll see with ethambutol is this sort of visual disturbances, where basically the patients have this decreased sort of like red-green color discrimination&hellip; So visual changes are going to be notable for this one.",
           "<mark class=\"prof-highlight\">Ethambutol = the eyes: decreased red-green discrimination and visual acuity</mark> [slide 44].") + '''

  <h4 class="subsub">Pyrazinamide [slide 45]</h4>
  <table>
    <tr><th>Topic</th><th>What the slide gives</th></tr>
    <tr><td><strong>2 &middot; Mechanism</strong></td><td><strong>Converted to pyrazinoic acid, which lowers the pH so the bacteria cannot grow</strong>; it <strong>enters macrophages</strong></td></tr>
    <tr><td><strong>Why it is in the regimen</strong></td><td><strong>Decreases the duration of combined therapy</strong></td></tr>
    <tr><td><strong>9 &middot; Protocol</strong></td><td><strong>Given the first two months only, to avoid liver toxicity</strong></td></tr>
    <tr><td><strong>5&ndash;7 &middot; Adverse effects and contraindication</strong></td><td><strong>Hepatitis</strong> (15 percent): <strong>monitor liver enzymes</strong>. <strong>Inhibits uric acid excretion: all patients become hyperuricemic.</strong> <strong>Avoid in pregnancy.</strong></td></tr>
  </table>
  <div class="callout"><strong>Current guidelines differ:</strong> the World Health Organization recommends pyrazinamide in pregnancy, while United States
  guidance has historically left it out for lack of data. The slide&rsquo;s &ldquo;avoid in pregnancy&rdquo; is what is tested.</div>
''' + star("44:42", "This one, again, because of liver injury, can only give it the first two months only&hellip; this one, really rough on the liver, so that&rsquo;s three drugs now. You&rsquo;re seeing this pretty rough on the liver. You&rsquo;ve got to be monitoring for those very closely there. This one also causes hyperuricemia, similar to ethambutol, and this one is going to be avoided in pregnancy.",
           "<mark class=\"prof-highlight\">Three of the four hurt the liver (isoniazid, rifampin, pyrazinamide); ethambutol does not</mark>; pyrazinamide stops after 2 months to spare the liver and is avoided in pregnancy [slides 39, 42 and 45]. He gave teratogenicity as the pregnancy reason (45:02).") + '''

  <p><strong>The four side by side.</strong> Two raise uric acid (<strong>ethambutol and pyrazinamide</strong>) [slides 44 and 45]; three hit the liver
  (<strong>isoniazid, rifampin, pyrazinamide</strong>) [slides 39, 42 and 45]; one turns secretions orange (<strong>rifampin</strong>) [slide 42];
  one needs pyridoxine (<strong>isoniazid</strong>) [slide 39]; one is checked with the eyes (<strong>ethambutol</strong>) [slide 44].</p>
'''

# ------------------------------------------------------------------------------------------------- 3.7 anaphylaxis
BODY += '''
  <h3 class="sub" id="pu-anaphylaxis">3.7 &middot; Objectives 1&ndash;6 &mdash; Anaphylaxis treatment</h3>

  <p><strong>What it is [slide 48].</strong> Anaphylaxis is a <strong>severe, systemic allergic reaction</strong> with multisystem involvement
  (skin, airway, vascular system and gastrointestinal tract). <strong>Severe cases may end in complete airway obstruction, cardiovascular
  collapse and death.</strong> The slide 49 picture sorts the triggers by route: skin contact (poison plants, animal scratches, pollen, latex),
  injection (bee sting), ingestion (medication, nuts and shellfish) and inhalation (pollen, dust, mold and mildew, animal dander).</p>

  <table>
    <tr><th>Treatment</th><th>What it does, and what to know</th></tr>
    <tr><td><strong>Volume expansion</strong> [slide 50]</td><td><strong>Intravenous crystalloids (0.9 percent sodium chloride)</strong> for <strong>profound vasodilation and hypotension</strong>; they increase intravascular volume. Severe cases need much more volume. (The volumes on the slide are not tested.)</td></tr>
    <tr><td><strong>Epinephrine</strong> [slides 51 and 52]</td><td>An <strong>endogenous catecholamine (adrenaline)</strong> acting on <strong>alpha and beta receptors</strong>.
      <strong>Alpha effects: vasoconstriction and decreased vascular permeability.</strong> <strong>Beta effects: bronchial smooth muscle relaxation.</strong>
      It also <strong>alleviates pruritus, urticaria and angioedema</strong> [slide 51].<br>
      <strong>Route:</strong> intramuscular or subcutaneous, or intravenous; <strong>intramuscular is generally preferred unless the patient is coding</strong>.
      It comes in two concentrations that differ tenfold (the amounts are not tested); the picture is an epinephrine auto-injector [slide 52].<br>
      <strong>Adverse effects:</strong> anxiety, hypertension, tachycardia, nausea and vomiting, diaphoresis. <strong>Overdose</strong> can cause cerebrovascular hemorrhage, myocardial infarction and pulmonary edema [slide 52].</td></tr>
    <tr><td><strong>Histamine blockers</strong> [slide 53]</td><td>Massive amounts of histamine are released in an acute anaphylactic reaction.
      <strong>Histamine H1 blockers</strong> (diphenhydramine, hydroxyzine) <strong>relieve the rash, pruritus and hives</strong> (the cutaneous effects).
      The <strong>histamine H2 blocker famotidine</strong> blocks the <strong>systemic (vasodilation) and gastrointestinal effects</strong> (increased gastric acid secretion).</td></tr>
    <tr><td><strong>Bronchodilator: albuterol</strong> [slide 54]</td><td>A <strong>beta-2 agonist</strong> that <strong>relaxes bronchial smooth muscle</strong>. Adverse effects: anxiousness, tremor, tachycardia.</td></tr>
    <tr><td><strong>Corticosteroids</strong> [slide 55]</td><td><strong>Block the production of inflammatory mediators at the cellular level</strong> and work on all aspects of anaphylaxis, but <strong>take several hours to work</strong>. Agents: <strong>methylprednisolone</strong> (intramuscular, intravenous), <strong>prednisone</strong>.</td></tr>
  </table>
''' + star("48:41", "Epinephrine works for everything. Not every allergic reaction requires epinephrine though. But if we have suspicion, they could be developing anaphylaxis, any kind of cardiovascular compromise, any sort of airway compromise, absolutely use the epinephrine right away.",
           "<mark class=\"prof-highlight\">Airway or cardiovascular compromise: epinephrine right away</mark>, usually intramuscular or subcutaneous (intravenous if the patient is coding) [slides 51 and 52]. A milder reaction (itching, rash, no airway or circulation problem) may need only a histamine H1 blocker and a corticosteroid (52:33).") + star("53:10", "Epi is going to work super fast. As soon as you give it, it&rsquo;s going to be kicking in. Things like corticosteroids, they take some time to work. They take hours because they work at the site of the nucleus to change things like gene transcription and protein production.",
           "<mark class=\"prof-highlight\">Epinephrine acts at once; corticosteroids take several hours</mark> [slide 55]. He called the histamine H2 blocker &ldquo;kind of an optional thing&rdquo; (51:17).")

# ------------------------------------------------------------------------------------------------- 3.8 asthma
BODY += '''
  <h3 class="sub" id="pu-asthma">3.8 &middot; Objectives 1&ndash;3 &mdash; Asthma: the disease and the three ways to treat it</h3>

  <p><strong>What it is [slide 57].</strong> Asthma is <strong>widespread, reversible narrowing of the bronchial airways</strong> with
  <strong>eosinophilic inflammation of the bronchial mucosa</strong>, a <strong>marked increase in bronchial responsiveness</strong> and
  <strong>thickening of the bronchial mucosa</strong>. Symptoms: shortness of breath, chest tightness, wheezing and coughing. Genetic factors play an
  important role in most cases (60 to 80 percent). The slide 58 figure puts <strong>inflammation</strong> at the top: it drives both
  <strong>airway hyperresponsiveness</strong> and <strong>airway obstruction</strong>, and those two produce the clinical symptoms.</p>

  <p><strong>The mast cell and its mediators [slides 59 and 60].</strong> Allergen binds immunoglobulin E (IgE) on the mast cell, which releases
  mediators on three timescales:</p>
  <table>
    <tr><th>Release</th><th>Mediators [slide 59]</th></tr>
    <tr><td><strong>Granule contents, immediate</strong></td><td>Histamine, proteases, heparin, tumor necrosis factor</td></tr>
    <tr><td><strong>Membrane-derived lipid mediators, over minutes</strong></td><td>Prostaglandins, <strong>leukotrienes</strong>, platelet-activating factor</td></tr>
    <tr><td><strong>Cytokine production, over hours</strong></td><td>Interleukins 2, 3, 4, 5, 6 and 8; tumor necrosis factor</td></tr>
  </table>
  <p>Slide 60 shows the result as two dips in forced expiratory volume in 1 second (FEV1): an <strong>early reaction</strong> within the first hour
  (histamine, tryptase, leukotriene C4 and the other mast cell mediators on airway smooth muscle) and a <strong>late reaction</strong> hours later,
  when eosinophils, neutrophils and T lymphocytes infiltrate the airway wall. The <strong>leukotriene pathway</strong> [slides 61 and 76] runs from
  arachidonic acid through <strong>5-lipoxygenase</strong> to leukotriene A4, then leukotriene B4 and the cysteinyl leukotrienes C4, D4 and E4
  (the cyclooxygenase branch makes the prostaglandins and thromboxane).</p>

  <p><strong>Other causes of attacks [slides 62 and 63].</strong></p>
  <ul>
    <li><strong>Most asthma attacks are not triggered by allergens; most are triggered by a viral respiratory infection</strong> [slide 62].</li>
    <li>Bronchospasm can be provoked by <strong>distilled water, exercise, cold air and rapid respiratory maneuvers</strong> (nonspecific bronchial hyperreactivity) [slide 62].</li>
    <li><strong>Bronchial reactivity is measured as the fall in forced expiratory volume in 1 second (FEV1) after inhaling increasing concentrations of methacholine</strong> [slide 62].</li>
    <li>Bronchoconstriction comes not only from the mediators directly but also through neural and humoral pathways: they <strong>stimulate afferent vagal receptors</strong> to start reflex bronchoconstriction, and release <strong>tachykinins (for example, substance P)</strong> that contract smooth muscle directly. <strong>So asthma can be treated with drugs of differing mechanisms</strong> [slide 63].</li>
  </ul>

  <p><strong>The three therapeutic approaches (Objective 1) [slide 64].</strong></p>
  <table>
    <tr><th>Approach</th><th>Drugs [slide 64]</th></tr>
    <tr><td><strong>1. Reverse bronchospasm</strong></td><td>Beta-2 agonists, ipratropium, theophylline</td></tr>
    <tr><td><strong>2. Remove the trigger or antigen</strong></td><td>Cromolyn, nedocromil</td></tr>
    <tr><td><strong>3. Control inflammation</strong></td><td>Steroids, lipoxygenase inhibitors</td></tr>
  </table>

  <p><strong>Classifying severity (youths 12 and older and adults) [slide 65].</strong></p>
  <table>
    <tr><th>Component</th><th>Intermittent</th><th>Mild persistent</th><th>Moderate persistent</th><th>Severe persistent</th></tr>
    <tr><td><strong>Symptoms</strong></td><td>2 days a week or fewer</td><td>More than 2 days a week, not daily</td><td>Daily</td><td>Throughout the day</td></tr>
    <tr><td><strong>Nighttime awakenings</strong></td><td>2 a month or fewer</td><td>3 to 4 a month</td><td>More than once a week, not nightly</td><td>Often 7 a week</td></tr>
    <tr><td><strong>Short-acting beta-2 agonist use</strong></td><td>2 days a week or fewer</td><td>More than 2 days a week, not more than once a day</td><td>Daily</td><td>Several times a day</td></tr>
    <tr><td><strong>Interference with normal activity</strong></td><td>None</td><td>Minor limitation</td><td>Some limitation</td><td>Extremely limited</td></tr>
    <tr><td><strong>Lung function</strong> (FEV1 = forced expiratory volume in 1 second; FVC = forced vital capacity)</td><td>Normal FEV1 between exacerbations; FEV1 over 80 percent predicted; FEV1/FVC normal</td><td>FEV1 80 percent predicted or more; FEV1/FVC normal</td><td>FEV1 over 60 but under 80 percent predicted; FEV1/FVC reduced 5 percent</td><td>FEV1 under 60 percent predicted; FEV1/FVC reduced more than 5 percent</td></tr>
    <tr><td><strong>Exacerbations needing oral systemic corticosteroids</strong></td><td>0 to 1 a year</td><td colspan="3">2 or more a year</td></tr>
  </table>
''' + star("58:44", "I&rsquo;m not going to have you, you know, diagnose the specific type of asthma someone has on a test question from me at least. But keep in mind that a lot of times we will distinguish the severity and type of asthma a patient has based off of their symptomatology.",
           "The table is for reference: no question here asks you to classify a patient&rsquo;s severity.") + '''

  <p><strong>Goals of treatment [slide 66].</strong></p>
  <ul>
    <li><strong>Reduce bronchial responsiveness long term.</strong> Responsiveness is related to airway inflammation and is reduced with <strong>anti-inflammatory agents, for example inhaled corticosteroids</strong>.</li>
    <li><strong>Prevent or reverse acute bronchospasm:</strong> avoid allergens and asthma triggers, and treat with <strong>short-acting beta-2 agonists</strong>.</li>
  </ul>

  <p><strong>Quick relief or long-term control (Objectives 1 and 3) [slide 67].</strong></p>
  <table>
    <tr><th>Quick-relief medications</th><th>Long-term controller medications</th></tr>
    <tr><td>Short-acting beta-2 agonists<br>Anticholinergics<br>Systemic corticosteroids</td>
        <td>Long-acting beta-2 agonists<br>Inhaled corticosteroids<br>Leukotriene modifiers<br>Mast cell stabilizers<br>Anti-immunoglobulin E antibody<br>Methylxanthines (theophylline)</td></tr>
  </table>
''' + star("54:21", "When I delineate the different medications, I want you to make clear the difference between drugs that are used for quick relief of symptoms and those which are used for control of symptoms or prevention of symptoms because they&rsquo;re not necessarily used interchangeably&hellip; Because those are easy test questions I can ask. I say which one of these is good for quick relief? Which one of these is good as a controller med?",
           "<mark class=\"prof-highlight\">For every asthma drug, know whether it is quick relief or a long-term controller</mark> [slide 67].") + star("1:00:10", "A sign of a poorly controlled asthmatic patient [with] persistent asthma is they will be burning through their rescue inhaler very quickly and they will not be using their controller medication because some of our controller meds they don&rsquo;t work immediately they take time like weeks sometimes to kick in.",
           "<mark class=\"prof-highlight\">Frequent rescue-inhaler refills mean poor control</mark>: ask about the controller, which takes weeks to work (inhaled corticosteroids up to 8 weeks [slide 73], mast cell stabilizers up to 4 weeks [slide 78]).") + '''

  <div class="callout"><strong>Memory aid &mdash; the airway as a house on fire.</strong>
  <em>A story to hang the slide facts on. When a question asks for a fact, answer from the facts in this section, not from the story.</em>
  <ul>
    <li><strong>The fire is inflammation; the smoke is bronchospasm.</strong> Inflammation drives both the hyperresponsiveness and the obstruction [slide 58].
    The matches are <strong>immunoglobulin E on the mast cells</strong>; the allergen strikes them, and the mast cell flashes histamine at once, then leukotrienes over minutes,
    then cytokines that keep the embers smoldering for hours (the late reaction) [slides 59 and 60]. Most fires, though, are started by a virus, not an allergen [slide 62].</li>
    <li><strong>Clearing the smoke = reversing bronchospasm</strong> [slide 64]. <strong>Beta-2 agonists are the fans</strong>: they raise cyclic adenosine monophosphate and relax the smooth muscle;
    the short-acting fan (albuterol) starts at once and runs 4 to 6 hours, the long-acting fan (salmeterol, formoterol) 12 hours or more [slides 68 and 70].
    <strong>Ipratropium cuts the alarm wire</strong>: it blocks the acetylcholine of the vagal reflex at muscarinic receptors [slides 63 and 86].
    <strong>Theophylline is the old fan with a frayed cord</strong>: less effective, less well tolerated, a narrow therapeutic index, seizures and arrhythmias when it runs too hot [slides 82 and 84].</li>
    <li><strong>Fireproofing = removing the trigger.</strong> <strong>Cromolyn and nedocromil</strong> work only if they are on <strong>before</strong> the spark (&ldquo;must be taken before antigen insult&rdquo;) and need weeks of regular use [slides 77 and 78].</li>
    <li><strong>Putting the fire out = controlling inflammation.</strong> <strong>Inhaled corticosteroids are the sprinkler system</strong>: they inhibit the whole inflammatory cascade but take up to 8 weeks for full effect,
    and the water that drips in the mouth is <strong>thrush</strong> [slide 73]. <strong>Montelukast closes one fuel line</strong>, the leukotriene D4 receptor [slide 75].
    <strong>Omalizumab takes away the matches</strong>: it binds circulating immunoglobulin E so the mast cells cannot degranulate [slide 79]; the anti-interleukin-5 drugs starve the eosinophils that feed an eosinophilic fire [slide 81].
    <strong>Systemic corticosteroids are the fire department</strong>: the most potent, kept for exacerbations because of the water damage (their side effects) [slides 88 and 89].</li>
    <li><strong>A fan without a sprinkler is dangerous</strong>: a long-acting beta-2 agonist is never used alone in asthma [slide 70]. <strong>Opening the windows every hour means the fire is not out</strong>:
    albuterol overuse signals poor control and the need to adjust the long-term therapy [slide 98].</li>
    <li><strong>Chronic obstructive pulmonary disease is a house with smoke damage that never fully clears</strong> (not fully reversible) [slide 101], and the arsonist is cigarette smoke: stopping smoking is what slows the damage [slide 103].</li>
  </ul>
  <strong>Where it breaks:</strong> the story has nothing to say about the infections half of the lecture, about anaphylaxis (where epinephrine is the drug, through alpha and beta receptors at once) or about the devices.
  For those, use the facts in 3.1 to 3.7 and 3.11.</div>
'''

# ------------------------------------------------------------------------------------------------- 3.9 bronchodilators
BODY += '''
  <h3 class="sub" id="pu-bronchodilators">3.9 &middot; Objectives 1&ndash;9 &mdash; Bronchodilators: beta-2 agonists, theophylline, anticholinergics</h3>

  <h4 class="subsub">Beta-2 agonists [slides 68 to 71]</h4>
  <p><strong>Mechanism [slide 68].</strong> They <strong>increase cyclic adenosine monophosphate (cAMP)</strong> and <strong>relax airway smooth muscle</strong>.
  The slide 69 picture shows how: the beta-2 receptor activates the stimulatory G protein, which makes cyclic adenosine monophosphate from adenosine triphosphate, and that <strong>inhibits myosin light chain kinase</strong>,
  the enzyme that calcium and calmodulin switch on to contract the muscle.</p>
''' + fig("l11-slide-69.jpg", "A smooth muscle cell. Calcium enters through an L-type channel and leaves the sarcoplasmic reticulum, binds calmodulin and activates myosin light chain kinase. A beta-2 receptor with its stimulatory G protein makes cyclic adenosine monophosphate from adenosine triphosphate, which inhibits myosin light chain kinase.",
          "Beta-2 agonists: the <strong>beta-2 receptor &rarr; stimulatory G protein &rarr; cyclic adenosine monophosphate (cAMP)</strong>, which <strong>inhibits myosin light chain kinase</strong>, so the airway smooth muscle relaxes.", 69) + '''
  <table>
    <tr><th></th><th>Short-acting [slides 68 and 70]</th><th>Long-acting [slides 68 and 70]</th></tr>
    <tr><td><strong>Onset and duration</strong></td><td><strong>Work rapidly; last 4 to 6 hours</strong></td><td><strong>Last 12 or more hours</strong></td></tr>
    <tr><td><strong>Drugs (brands)</strong></td><td><strong>Albuterol</strong> (ProAir, Ventolin); <strong>levalbuterol</strong> (Xopenex)</td><td><strong>Formoterol</strong> (Foradil); <strong>salmeterol</strong> (Serevent)</td></tr>
    <tr><td><strong>Role</strong></td><td>Quick relief [slide 67]</td><td>Long-term controller [slide 67]; <strong>do NOT use alone for asthma</strong> [slide 70]</td></tr>
  </table>
''' + star("1:04:05", "One really critical point here is that for control of asthma long-term control you never ever ever ever ever ever use a long acting beta agonist by itself they&rsquo;ve actually found the studies that that increased risk for death&hellip; the long actings have to be paired with a it&rsquo;ll be a steroid&hellip; that&rsquo;ll be different we get into COPD.",
           "<mark class=\"prof-highlight\">Asthma: a long-acting beta-2 agonist is never used alone; it is paired with an inhaled corticosteroid</mark> [slides 70 and 74]. Chronic obstructive pulmonary disease is different (3.12).") + '''
  <p><strong>Adverse effects [slides 68 and 71].</strong> Increased heart rate and tremor [slide 68]; the full list: <strong>tachycardia, hypotension, headache,
  dizziness, insomnia, tremors, hyperglycemia</strong> [slide 71].</p>

  <h4 class="subsub">Methylxanthines: theophylline [slides 82 to 85]</h4>
  <table>
    <tr><th>Topic</th><th>What the slides give</th></tr>
    <tr><td><strong>2 &middot; Mechanism</strong></td><td>A <strong>nonspecific phosphodiesterase inhibitor</strong> [slide 82]: it <strong>inhibits phosphodiesterase 4 and 5</strong>, raising cyclic adenosine monophosphate (cAMP) and cyclic guanosine monophosphate (cGMP); it is an <strong>adenosine receptor (A2B) antagonist</strong>; and it has <strong>anti-inflammatory actions</strong>, inhibiting inflammatory mediators in the late response [slide 83]</td></tr>
    <tr><td><strong>Place in therapy</strong></td><td>Compared with the long-acting bronchodilators it is <strong>less effective and less well tolerated</strong>, with a <strong>narrow therapeutic index</strong> [slide 82]. <strong>Limited use</strong>, only generic; <strong>used in chronic obstructive pulmonary disease</strong> [slide 83]. The intravenous form is <strong>aminophylline</strong> [slide 82]</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Adverse effects</strong></td><td>Arrhythmias, convulsions, headaches, nausea, insomnia, heartburn [slide 82]. It <strong>stimulates gastric acid</strong>, has <strong>diuretic effects</strong>, relaxes smooth muscle, and at high levels is a <strong>central nervous system stimulant (convulsions)</strong> and a <strong>cardiac stimulant (arrhythmias)</strong> [slide 84]</td></tr>
    <tr><td><strong>9 &middot; Monitoring</strong></td><td><strong>Monitor theophylline plasma levels</strong>: nausea, vomiting and cardiac effects appear at the top of the therapeutic range; seizures and arrhythmias are the toxic effects at higher levels [slide 85]</td></tr>
  </table>
  <div class="callout"><strong>The slides disagree with each other and with pharmacology:</strong> slide 85 says theophylline is &ldquo;renally eliminated&rdquo;,
  but it is mainly metabolized by the liver, which is why rifampin&rsquo;s enzyme induction lowers its level [slide 42]; and slide 84 writes the
  level in mcg/ml where slide 85 writes mg/ml. No question here asks how theophylline is eliminated or asks a level as a number.
  Dr. Wood repeated the slide aloud (an older patient with poor kidney function accumulates it, 1:17:44) and framed the drug as
  &ldquo;historical perspective, I hope you never run into these&rdquo; (1:16:14): know its class, its narrow therapeutic index and its
  toxicity (seizures, arrhythmias).</div>

  <h4 class="subsub">Anticholinergics [slides 86 and 87]</h4>
  <p><strong>Mechanism [slide 86].</strong> They <strong>block acetylcholine&rsquo;s effect on muscarinic receptors</strong>, which produces bronchodilation.</p>
  <table>
    <tr><th></th><th>Short-acting</th><th>Long-acting</th></tr>
    <tr><td><strong>Drug (brand)</strong></td><td><strong>Ipratropium</strong> (Atrovent)</td><td><strong>Tiotropium</strong> (Spiriva)</td></tr>
    <tr><td><strong>Duration</strong></td><td>Up to 8 hours</td><td>24 hours or more</td></tr>
    <tr><td><strong>Note</strong></td><td>A quick-relief medication [slide 67]; one of the drugs that reverse bronchospasm [slide 64]</td><td>The slide says &ldquo;COPD (chronic obstructive pulmonary disease) only&rdquo; [slide 86], yet the stepwise asthma chart lists add-on tiotropium at steps 4 and 5 [slide 90]. No question here turns on &ldquo;COPD (chronic obstructive pulmonary disease) only&rdquo;.</td></tr>
  </table>
  <p><strong>Anticholinergic side effects, the mnemonic [slide 87].</strong></p>
  <table>
    <tr><th>Saying</th><th>Effect [slide 87]</th></tr>
    <tr><td>Blind as a bat</td><td>Blurry vision, mydriasis</td></tr>
    <tr><td>Mad as a hatter</td><td>Hallucinations, delirium, memory loss, psychosis</td></tr>
    <tr><td>Red as a beet</td><td>Flushing</td></tr>
    <tr><td>Hot as Hades</td><td>Fever, hyperthermia</td></tr>
    <tr><td>Dry as a bone</td><td>Dry mouth, dry eyes</td></tr>
    <tr><td>The bowel and bladder lose their tone</td><td>Constipation, urinary retention (the slide words it &ldquo;increase their tone&rdquo;)</td></tr>
    <tr><td>And the heart runs alone</td><td>Tachycardia, hypertension</td></tr>
  </table>
''' + star("1:19:01", "There they may actually get a combination of both albuterol plus something like ipratropium. Patients usually are not home on ipratropium&hellip; by using both an anti-muscarinic and a beta 2 agonist, you&rsquo;re kind of working on two different mechanisms there to get more bronchodilation&hellip; Long acting tiotropium, mostly for COPD only, occasionally for more difficult to control asthma patients.",
           "In an emergency department visit for asthma, <mark class=\"prof-highlight\">ipratropium is added to albuterol: two mechanisms, more bronchodilation</mark>. Tiotropium is mostly a chronic obstructive pulmonary disease drug, occasionally add-on for hard-to-control asthma (steps 4 and 5, slide 90). (Whisper writes the drugs as &ldquo;ipitropium&rdquo; and &ldquo;teatroprime&rdquo;.)") + '''
'''

# ------------------------------------------------------------------------------------------------- 3.10 controllers
BODY += '''
  <h3 class="sub" id="pu-controllers">3.10 &middot; Objectives 1&ndash;10 &mdash; Controllers: corticosteroids, montelukast, mast cell stabilizers, biologics</h3>

  <h4 class="subsub">Inhaled corticosteroids [slides 72 and 73]</h4>
  <table>
    <tr><th>Drug</th><th>Brand [slide 72]</th></tr>
    <tr><td>Beclomethasone</td><td>QVAR</td></tr>
    <tr><td>Budesonide</td><td>Pulmicort</td></tr>
    <tr><td>Flunisolide</td><td>Aerobid</td></tr>
    <tr><td>Fluticasone</td><td>Flovent</td></tr>
    <tr><td>Mometasone</td><td>Asmanex</td></tr>
    <tr><td>Triamcinolone</td><td>Azmacort</td></tr>
  </table>
  <ul>
    <li><strong>Mechanism:</strong> they <strong>inhibit the inflammatory cascade</strong> [slide 73].</li>
    <li><strong>Onset:</strong> <strong>up to 8 weeks for maximal effect</strong> [slide 73] &mdash; tell the patient it is a daily controller, not a rescue inhaler.</li>
    <li><strong>Adverse effects:</strong> <strong>oral candidiasis (thrush)</strong>; <strong>growth suppression in children (high dose)</strong>; <strong>immune suppression (systemic action)</strong> [slide 73].</li>
  </ul>
''' + star("1:05:40", "This is going to be kind of the mainstay the gold standard for prevention of asthma symptoms are going to be the inhaled corticosteroids&hellip; they do take some time to kick in so up to eight weeks for maximal effects&hellip; so it&rsquo;s important to educate&hellip; consistency is key.",
           "<mark class=\"prof-highlight\">Inhaled corticosteroids are the mainstay controller; up to 8 weeks for maximal effect, so tell the patient to keep taking them</mark> [slides 72 and 73].") + star("1:07:12", "Adverse effects wise one thing you can see is oral candidiasis or thrush that happens because when you breathe in the medication some amount of it is going to hit the back of the throat&hellip; normally what we&rsquo;ll tell patients to do is make sure they rinse their mouth out after using their inhaled corticosteroids.",
           "<mark class=\"prof-highlight\">Thrush: rinse the mouth after each use</mark> [slide 73]; he suggested linking it to brushing the teeth (1:07:54).") + '''

  <p><strong>Combination inhalers: an inhaled corticosteroid plus a long-acting beta-2 agonist [slide 74].</strong></p>
  <table>
    <tr><th>Combination</th><th>Brand [slide 74]</th></tr>
    <tr><td>Formoterol / budesonide</td><td>Symbicort</td></tr>
    <tr><td>Formoterol / mometasone</td><td>Dulera</td></tr>
    <tr><td>Salmeterol / fluticasone</td><td>Advair</td></tr>
  </table>

  <h4 class="subsub">Leukotriene modifiers: montelukast [slide 75]</h4>
  <ul>
    <li><strong>Montelukast</strong> (Singulair) is an <strong>oral leukotriene antagonist</strong>: a <strong>leukotriene D4 antagonist at the cysteinyl leukotriene 1 (cysLT1) receptor</strong>.</li>
    <li>That receptor mediates <strong>inflammation, bronchial constriction and mucus secretion</strong>.</li>
    <li><strong>Effective in aspirin-induced asthma.</strong></li>
    <li>The slide calls its side effects minimal and well tolerated.</li>
  </ul>
  <div class="callout"><strong>Current labeling differs:</strong> since 2020 montelukast carries a Food and Drug Administration boxed warning for
  serious neuropsychiatric events (mood and behavior changes, suicidal thinking). Dr. Wood repeated the slide (&ldquo;pretty well tolerated,
  it&rsquo;s pretty minimal side effects,&rdquo; 1:09:59) and added that it is &ldquo;not probably going to be the most effective controller med.&rdquo;
  No question here asks montelukast&rsquo;s side-effect profile.</div>

  <h4 class="subsub">Mast cell stabilizers: cromolyn and nedocromil [slides 77 and 78]</h4>
  <ul>
    <li>They <strong>remove the trigger or antigen</strong> by <strong>stabilizing mast cells</strong>; <strong>limited use</strong> [slide 77].</li>
    <li><strong>Cromolyn sodium</strong> (the slide gives the brand Nasalcrom, which is the nasal spray) and <strong>nedocromil</strong> (Tilade), both <strong>inhaled</strong> [slides 77 and 78].</li>
    <li><strong>Must be taken before the antigen insult</strong> [slide 77].</li>
    <li><strong>May take up to 4 weeks to work; must be taken regularly</strong> [slide 78].</li>
    <li>Mechanism unknown (may interfere with calcium) [slide 77].</li>
  </ul>
''' + star("1:11:25", "To be honest, these are not that great in terms of efficacy compared to like your steroids. So these are not really all that well used, but they still pop up occasionally. So just list it here for completeness sake.",
           "Mast cell stabilizers: <mark class=\"prof-highlight\">taken before the trigger, regularly, up to 4 weeks to work; weaker than steroids</mark> [slides 77 and 78].") + '''

  <h4 class="subsub">Omalizumab, the anti-immunoglobulin E antibody [slides 79 and 80]</h4>
  <ul>
    <li><strong>Omalizumab</strong> (Xolair), given <strong>subcutaneously every 2 to 4 weeks</strong> [slide 79].</li>
    <li>A <strong>recombinant DNA-derived humanized monoclonal antibody against immunoglobulin E</strong> [slide 79].</li>
    <li><strong>Mechanism:</strong> it <strong>binds circulating immunoglobulin E</strong>, which decreases the high-affinity receptors on mast cells and <strong>prevents degranulation</strong> [slide 79].</li>
    <li><strong>Adverse effects:</strong> gastrointestinal disturbances, <strong>anaphylaxis</strong>, neutralizing antibodies, secondary malignancies [slide 79];
    urticaria (0.1 percent), anaphylaxis (0.1 percent), <strong>injection site pain, bruising</strong> [slide 80]. <em>Anaphylaxis is also omalizumab&rsquo;s Food and Drug Administration boxed warning.</em></li>
  </ul>

  <h4 class="subsub">Other biologics for asthma [slide 81]</h4>
  <p>Used for the <strong>eosinophilic phenotype</strong> (peripheral blood eosinophils above 150 per microliter), with <strong>a side-effect profile similar to omalizumab&rsquo;s</strong>.</p>
  <table>
    <tr><th>Group</th><th>Drugs (brands) [slide 81]</th></tr>
    <tr><td><strong>Anti-interleukin-5</strong></td><td>Mepolizumab (Nucala); benralizumab (Fasenra); <strong>reslizumab (Cinqair), given intravenously</strong></td></tr>
    <tr><td><strong>Anti-interleukin-4</strong></td><td><strong>Dupilumab</strong> (Dupixent)</td></tr>
  </table>
''' + star("1:14:19", "So you can either target IL-5 or IL-4. I&rsquo;m not going to really care if you know the difference between the two, I would just recognize that these are affecting interleukin. So instead of targeting IgE, they&rsquo;re going to be targeting these interleukins here.",
           "<mark class=\"prof-highlight\">Omalizumab targets immunoglobulin E (IgE); the eosinophilic-phenotype biologics target interleukins</mark> [slides 79 and 81]. Which interleukin each one targets is not tested. All are injected proteins: hypersensitivity and anaphylaxis, neutralizing antibodies, injection site reactions (1:13:16).") + '''
  <p>(Strictly, benralizumab binds the interleukin-5 receptor rather than interleukin-5 itself, and dupilumab the interleukin-4 receptor; the slide groups them by the interleukin.)</p>

  <h4 class="subsub">Oral systemic corticosteroids [slides 88 and 89]</h4>
  <ul>
    <li>They <strong>suppress, control and reverse airway inflammation</strong> and <strong>inhibit the production of inflammatory cytokines</strong> [slide 88].</li>
    <li><strong>The most potent, but of limited use because of their side effects: used in asthma exacerbations</strong> [slide 88].</li>
  </ul>
  <table>
    <tr><th>Drug (brand)</th><th>Form [slide 88]</th></tr>
    <tr><td>Prednisone (Deltasone)</td><td>Oral tablet</td></tr>
    <tr><td>Prednisolone (Ora-Pred)</td><td>Oral liquid</td></tr>
    <tr><td>Methylprednisolone (Solu-Medrol)</td><td>Oral or parenteral</td></tr>
    <tr><td>Dexamethasone (Decadron)</td><td>Oral or parenteral</td></tr>
  </table>
  <p><strong>Systemic corticosteroid side effects [slide 89].</strong> <strong>Adrenal suppression</strong> (the slide&rsquo;s general rule: taper if the course lasts more than 5 days);
  <strong>growth suppression</strong>; <strong>dermal thinning</strong>; <strong>hypertension</strong>; <strong>hyperglycemia</strong>; altered mood or mental status;
  <strong>muscle weakness (steroid myopathy)</strong>; <strong>immunosuppression</strong>.</p>
''' + star("1:22:13", "Remember, if they&rsquo;re on it for more than five days, you have to taper. So if the patient got admitted and they&rsquo;re on it for a week or more, then you&rsquo;d have to taper down the dose. If it&rsquo;s just a five-day course, no problem.",
           "<mark class=\"prof-highlight\">More than 5 days of a systemic corticosteroid: taper; a 5-day burst can simply stop</mark> [slide 89]. He gives a short oral course (about 5 days) after an emergency visit, intravenous methylprednisolone if admitted (1:21:13).") + '''
  <div class="callout"><strong>Current guidelines differ:</strong> short bursts of oral corticosteroid for an asthma exacerbation are usually stopped without a taper;
  tapering is reserved for longer courses. The slide&rsquo;s five-day rule, which Dr. Wood affirmed aloud, is what is tested (one question asks it).</div>
'''

# ------------------------------------------------------------------------------------------------- 3.11 steps, devices, status
BODY += '''
  <h3 class="sub" id="pu-inhalers">3.11 &middot; Objectives 9&ndash;10 &mdash; Stepwise therapy, inhaler devices, technique and status asthmaticus</h3>

  <p><strong>Stepwise asthma therapy [slide 90].</strong> Management is a cycle (assess, adjust, review the response), and treatment is
  <strong>adjusted up and down</strong> for the individual patient.</p>
''' + fig("l11-slide-90.jpg", "A management cycle (assess, adjust, review response) above five steps of asthma medication. Each step lists a preferred controller, other controller options, and the relievers.",
          "Stepwise asthma therapy: the <strong>preferred controller</strong> rises from as-needed low-dose inhaled corticosteroid-formoterol (step 1) to high-dose inhaled corticosteroid plus long-acting beta-2 agonist with phenotype referral (step 5); the <strong>preferred reliever</strong> is as-needed low-dose inhaled corticosteroid-formoterol, and as-needed short-acting beta-2 agonist is the other reliever option.", 90) + '''
  <table>
    <tr><th>Step</th><th>Preferred controller [slide 90]</th><th>Other controller options [slide 90]</th></tr>
    <tr><td><strong>1</strong></td><td>As-needed low-dose inhaled corticosteroid-formoterol</td><td>Low-dose inhaled corticosteroid taken whenever the short-acting beta-2 agonist is taken</td></tr>
    <tr><td><strong>2</strong></td><td>Daily low-dose inhaled corticosteroid, or as-needed low-dose inhaled corticosteroid-formoterol</td><td>Low-dose inhaled corticosteroid whenever the short-acting beta-2 agonist is taken, or a leukotriene receptor antagonist</td></tr>
    <tr><td><strong>3</strong></td><td>Low-dose inhaled corticosteroid plus long-acting beta-2 agonist</td><td>Medium-dose inhaled corticosteroid, or low-dose inhaled corticosteroid plus a leukotriene receptor antagonist</td></tr>
    <tr><td><strong>4</strong></td><td>Medium-dose inhaled corticosteroid plus long-acting beta-2 agonist</td><td>High-dose inhaled corticosteroid, add-on tiotropium, or add-on leukotriene receptor antagonist</td></tr>
    <tr><td><strong>5</strong></td><td>High-dose inhaled corticosteroid plus long-acting beta-2 agonist; <strong>refer for phenotypic assessment</strong>, with or without add-on therapy (tiotropium, anti-immunoglobulin E, anti-interleukin-5 or its receptor, anti-interleukin-4 receptor)</td><td>Add low-dose oral corticosteroid, but consider the side effects</td></tr>
  </table>
  <p><strong>Relievers [slide 90]:</strong> the <strong>preferred reliever is as-needed low-dose inhaled corticosteroid-formoterol</strong>; the <strong>other reliever option is an as-needed short-acting beta-2 agonist</strong>.</p>
''' + star("1:27:49", "I could either ask you, hey, what would be the first line agent you&rsquo;d prefer for a patient for control of asthmatic symptoms&hellip; but I can also ask questions further up the line and say, hey, they&rsquo;re on this already, what would you want to move up to next?&hellip; So I will not make you memorize the doses&hellip; Remember to KISS, keep it simple student.",
           "Read the chart as a ladder. <mark class=\"prof-highlight\">First controller: a daily low-dose inhaled corticosteroid. Then add a long-acting beta-2 agonist (low dose), then medium dose, then high dose with referral for phenotypic assessment and a biologic</mark> [slide 90]. His wrong answers for a new patient: albuterol (a reliever), theophylline (&ldquo;I don&rsquo;t really do that anymore&rdquo;) and omalizumab (last line). For quick relief, <strong>either</strong> as-needed inhaled corticosteroid-formoterol or a short-acting beta-2 agonist &ldquo;would be a perfectly fine answer&rdquo; (1:25:14).") + '''

  <p><strong>The devices (Objective 10) [slides 91 to 95].</strong></p>
  <table>
    <tr><th>Device</th><th>How it works</th><th>Who it suits, and the catch</th></tr>
    <tr><td><strong>Nebulizer</strong> [slide 92]</td><td>A <strong>compressor forces liquid medication into a fine mist</strong> (slide 91 shows the cup, mouthpiece, tubing and compressor)</td><td><strong>Passive inhalation: good for children and the elderly who cannot use a metered dose inhaler.</strong> A <strong>bigger dose is given overall</strong>, which may lead to more side effects. <strong>Must be cleaned regularly to prevent microbial growth.</strong></td></tr>
    <tr><td><strong>Dry powder inhaler</strong> [slide 93]</td><td>Medication in <strong>powder</strong> form; the <strong>patient provides the inspiratory force</strong> to draw it out of the device</td><td><strong>Not good for patients with poor inspiratory capacity.</strong> Clean regularly.</td></tr>
    <tr><td><strong>Metered dose inhaler</strong> [slide 94]</td><td>Medication in <strong>liquid</strong> form; a <strong>propellant</strong> in the canister forces it out as a fine mist (parts: drug canister, plastic actuator, cap)</td><td><strong>Requires the most coordination.</strong> <strong>Spacers</strong> hold the medication for patients with poor coordination. Clean regularly.</td></tr>
    <tr><td><strong>Spacer</strong> [slide 95]</td><td>The generic term for an <strong>open tube that extends the inhaler away from the mouth</strong></td><td rowspan="2">Both <strong>retain the large particles</strong> from the inhaler, leaving a <strong>higher proportion of smaller, respirable particles</strong>.</td></tr>
    <tr><td><strong>Valve holding chamber</strong> [slide 95]</td><td>Has <strong>one-way valves</strong> that do not let the patient <strong>exhale into the device</strong></td></tr>
  </table>

  <p><strong>Metered dose inhaler technique (Objective 10) [slides 96 and 97].</strong></p>
  <ol>
    <li><strong>Take off the cap and shake the inhaler</strong> (it may need to be primed).</li>
    <li><strong>Breathe out all the way.</strong></li>
    <li><strong>Hold the inhaler</strong> one of three ways: a short distance in front of the open mouth, through a spacer, or between the closed lips (the slide 96 drawings).</li>
    <li><strong>Start breathing in slowly as you press down on the inhaler.</strong> <strong>With a holding chamber, press down first, then begin breathing within 5 seconds.</strong></li>
    <li><strong>Breathe in slowly and deeply.</strong></li>
    <li><strong>Hold your breath for 10 seconds</strong>, or as long as comfortable.</li>
    <li>For inhaled quick-relief medicines (beta-2 agonists), <strong>wait 15 to 30 seconds between puffs</strong>.</li>
  </ol>
''' + star("1:34:17", "I use this analogy of the movie Finding Nemo&hellip; the sea turtles&hellip; They don&rsquo;t expend any energy get in places because they&rsquo;re just flowing along the current&hellip; after they breathe out had them start to breathe in&hellip; then you depress the canister that allows the medication to hop a ride down into the lungs.",
           "<mark class=\"prof-highlight\">Start the breath, then press: the medicine rides the current</mark> [slide 97]. He waits 15 to 30 seconds between puffs because the first loosens the airway and the second goes deeper (1:35:27), and checks technique by teach-back (1:35:58).") + '''
  <div class="callout"><strong>Current guidelines differ:</strong> many inhaler instructions advise waiting about a minute between puffs; the slide&rsquo;s 15 to 30 seconds is what is tested.</div>

  <p><strong>The summary slide (Objective 10) [slide 98].</strong></p>
  <ul>
    <li><strong>Asthma is a chronic disease.</strong></li>
    <li><strong>Long-term controller medications need to be used daily</strong> if indicated.</li>
    <li><strong>Albuterol only provides short-term relief and should be used sparingly.</strong> <strong>Excessive use indicates poor control and the need to adjust the long-term therapy.</strong></li>
    <li><strong>Avoid the triggers</strong> that worsen asthma or induce attacks.</li>
  </ul>

  <p><strong>Status asthmaticus (Objective 9) [slide 99].</strong> A <strong>medical emergency</strong>: an acute exacerbation that <strong>remains
  unresponsive to initial bronchodilator treatment</strong>. The algorithm (doses not tested):</p>
  <ol>
    <li><strong>Continuous nebulized albuterol.</strong></li>
    <li><strong>Steroids</strong> (intravenous preferred).</li>
    <li><strong>Magnesium</strong> (a bolus followed by a continuous infusion).</li>
    <li><strong>Ketamine, if intubated</strong>: an <strong>NMDA (N-methyl-D-aspartate) receptor antagonist</strong> (dissociative anesthetic) that <strong>increases catecholamine release, producing bronchodilation</strong>. Adverse reactions: <strong>emergence phenomenon</strong>, hypertension, tachycardia, vomiting.</li>
    <li>Aminophylline, with a question mark on the slide.</li>
  </ol>
  <div class="callout"><strong>Current guidelines differ:</strong> oral corticosteroids work as well as intravenous ones in an exacerbation when the patient can swallow; the slide&rsquo;s &ldquo;intravenous preferred&rdquo; is what is tested.</div>
''' + star("1:36:32", "We have just an asthma exacerbation that just is not improving. It&rsquo;s called status asthmaticus. And so this is a medical emergency&hellip; big whopping doses of albuterol&hellip; We&rsquo;ll start with IV steroids&hellip; You can actually utilize magnesium sulfate&hellip; a preferred agent is actually a drug called ketamine.",
           "<mark class=\"prof-highlight\">Status asthmaticus: continuous albuterol, intravenous steroids, magnesium, and ketamine if intubated</mark> [slide 99]. Ketamine is the preferred sedative here because its catecholamine release bronchodilates; expect tachycardia, hypertension, vomiting and an emergence reaction. Aminophylline is a last-ditch option he has &ldquo;only ever seen once&rdquo; (1:38:50).") + '''
'''

# ------------------------------------------------------------------------------------------------- 3.12 COPD
BODY += '''
  <h3 class="sub" id="pu-copd">3.12 &middot; Objectives 1&ndash;10 &mdash; Chronic obstructive pulmonary disease, smoking cessation and immunizations</h3>

  <p><strong>What it is [slide 101].</strong> Chronic obstructive pulmonary disease is <strong>chronic inflammation of the airways and lung
  parenchyma that is generally not fully reversible</strong> (asthma, by contrast, is reversible [slide 57]), with an <strong>accelerated decline
  in forced expiratory volume in 1 second (FEV1)</strong>. The slide&rsquo;s figure shows that <strong>symptoms generally appear only after a significant decline in forced expiratory volume in 1 second</strong> has
  already happened, and then worsen as lung function falls.</p>

  <p><strong>Drug therapy by group [slide 102].</strong> <strong>Every group</strong>: avoid the risk factors, such as smoking; <strong>annual influenza
  vaccination</strong>; <strong>pneumococcal vaccination</strong>; regular physical activity; <strong>regular review and correction of inhaler technique</strong>;
  long-term oxygen if there is chronic hypoxemia; pulmonary rehabilitation.</p>
  <table>
    <tr><th>Group</th><th>Symptoms</th><th>Exacerbation risk</th><th>Suggested treatment [slide 102]</th></tr>
    <tr><td><strong>A</strong></td><td>Less symptomatic (COPD (chronic obstructive pulmonary disease) Assessment Test score under 10)</td><td>Low: 0 or 1 exacerbation in the past year, no hospitalization</td><td><strong>A short-acting bronchodilator as needed</strong> (short-acting beta-2 agonist, short-acting muscarinic antagonist, or both)</td></tr>
    <tr><td><strong>B</strong></td><td>More symptomatic (score 10 or more)</td><td>Low</td><td><strong>Regular long-acting bronchodilator: a long-acting muscarinic antagonist or a long-acting beta-2 agonist</strong>, by patient preference; short-acting bronchodilator for relief</td></tr>
    <tr><td><strong>C</strong></td><td>Less symptomatic</td><td>High: 2 or more a year, one or more leading to hospitalization</td><td><strong>Regular long-acting muscarinic antagonist</strong>; short-acting beta-2 agonist for relief</td></tr>
    <tr><td><strong>D</strong></td><td>More symptomatic</td><td>High</td><td><strong>Long-acting muscarinic antagonist</strong>, or with severe breathlessness (score over 20) <strong>a long-acting beta-2 agonist plus long-acting muscarinic antagonist</strong>; an <strong>inhaled corticosteroid plus long-acting beta-2 agonist</strong> may be preferred if asthma and chronic obstructive pulmonary disease overlap; short-acting beta-2 agonist for relief</td></tr>
  </table>
  <p>Tiotropium (Spiriva) is the long-acting anticholinergic (muscarinic antagonist) of the lecture [slide 86], and theophylline is &ldquo;used in COPD&rdquo; (chronic obstructive pulmonary disease) [slide 83].</p>
  <div class="callout"><strong>Current guidelines differ:</strong> since 2023 the international chronic obstructive pulmonary disease report merges groups C and D into a single
  group E (for which a long-acting beta-2 agonist plus long-acting muscarinic antagonist is preferred). The slide&rsquo;s A to D groups are what is tested.</div>
''' + star("1:39:46", "I want you to compare and contrast that to the asthma management. Because this is a less of an inflammatory condition, we&rsquo;re gonna see that our anti-inflammatories actually fit all the way down at the bottom of the list&hellip; So for them, they could be on a long-acting beta agonist, that&rsquo;s fine. That&rsquo;s different from asthma, asthma can&rsquo;t do a SABA or a LABA by itself. Here you can.",
           "<mark class=\"prof-highlight\">Chronic obstructive pulmonary disease climbs a bronchodilator ladder; asthma climbs a steroid ladder</mark>. As needed: a short-acting beta-2 agonist, ipratropium, or both (group A) &rarr; one long-acting bronchodilator alone, muscarinic antagonist or beta-2 agonist (B, C) &rarr; the two together (D) &rarr; a glucocorticoid only for the most symptomatic high-risk patient, with asthma features [slide 102]. No biologics: &ldquo;there&rsquo;s nothing really to target&rdquo; (1:42:11).") + '''

  <p><strong>Smoking and chronic obstructive pulmonary disease [slide 103].</strong></p>
  <ul>
    <li><strong>Smoking is a major contributor to chronic obstructive pulmonary disease</strong>: 15 to 20 percent of smokers develop it, and cigarette smoke is responsible for more than 85 percent of cases.</li>
    <li><strong>Stopping smoking can return the decline in ventilatory function to the normal age-related rate</strong> and reduces the risk of lung cancer.</li>
    <li>It is a complex, multiple-component issue: physical, psychological and social.</li>
    <li><strong>Effective programs combine pharmacologic intervention with counseling</strong>; <strong>the intensity and frequency of counseling correlate directly with success</strong>.</li>
  </ul>

  <p><strong>The smoking cessation agents [slides 104 to 107].</strong> Bupropion SR (sustained release; Zyban), the nicotine transdermal system (patches),
  nicotine polacrilex (gum), nicotine spray, nicotine inhaler and varenicline (Chantix) [slide 104].</p>
  <table>
    <tr><th>Agent</th><th>Mechanism</th><th>What to know</th></tr>
    <tr><td><strong>Bupropion SR</strong> (Zyban) [slide 105]</td><td>Nicotine indirectly activates epinephrine and dopamine in the brain; bupropion is thought to <strong>mimic this because it inhibits the uptake of norepinephrine and dopamine</strong></td><td><strong>Avoid in patients with seizure disorders</strong> and in <strong>patients taking monoamine oxidase inhibitors</strong>; <strong>use caution with noradrenergic antidepressants</strong> (tricyclic antidepressants, venlafaxine). (The dosing schedule is not tested.)</td></tr>
    <tr><td><strong>Nicotine replacement</strong> [slide 106]</td><td>Replaces the nicotine: <strong>reduces the craving to smoke and minimizes physical withdrawal</strong> (anxiety, irritability, restlessness, insomnia, headache, depression, nausea)</td><td>Dose and duration depend on the level of dependence; <strong>therapy lasts 6 to 12 weeks</strong>. <strong>Patches and gum are available over the counter.</strong> <strong>Caution in cardiovascular disease</strong>: tachyarrhythmias and hypertension.</td></tr>
    <tr><td><strong>Varenicline</strong> (Chantix) [slide 107]</td><td>A <strong>partial nicotine receptor agonist</strong> (a lesser degree than nicotine)</td><td><strong>Start one week before the quit date and continue for 12 weeks.</strong> Side effects: <strong>nausea, sleep disturbance, headache</strong>. <strong>Black box warning: neuropsychiatric events</strong> (depression, suicidal ideation).</td></tr>
  </table>
''' + star("1:45:34", "Now people to avoid this in, if they have a seizure disorder, this can lower that seizure threshold so avoid it there. And then it&rsquo;d be very cautious in patients on medications that can also boost up norepinephrine levels.",
           "<mark class=\"prof-highlight\">Bupropion: avoid with a seizure disorder; avoid with a monoamine oxidase inhibitor, caution with tricyclics and venlafaxine</mark> [slide 105]. (Aloud he grouped the monoamine oxidase inhibitors with the cautions; the slide says avoid, and the slide is what is tested.)") + star("1:47:24", "The big thing here you want to warn patients of is you don&rsquo;t want them to fall off the wagon, so to speak, relapse, and then continue their nicotine of choice plus the nicotine replacement. That&rsquo;s a no-go because now they&rsquo;re even at higher nicotine levels.",
           "His counseling point (not on the slides, so not asked): a patient who goes back to smoking stops the nicotine replacement. The slide&rsquo;s point is the caution in cardiovascular disease, for tachyarrhythmias and hypertension [slide 106]. With varenicline, a partial agonist, smoking adds little (1:48:16), and he would be &ldquo;very, very cautious&rdquo; with it after depression or suicidal thinking (1:49:00), its slide&rsquo;s boxed warning [slide 107].") + '''
  <div class="callout"><strong>Current labeling differs:</strong> the Food and Drug Administration removed the boxed warning for neuropsychiatric events from varenicline (and from bupropion for smoking cessation) in 2016; the slide&rsquo;s black box warning is what is tested. Current bupropion labeling also lists eating disorders and abrupt alcohol or sedative withdrawal as contraindications, and varenicline&rsquo;s label warns about seizures; the slides do not, and neither is asked.</div>

  <p><strong>Immunizations (Objective 9) [slide 108].</strong> Patients with chronic obstructive pulmonary disease are at risk of significant morbidity and mortality from pneumonia
  caused by influenza, so <strong>annual influenza vaccination is highly recommended</strong>; they should <strong>also receive the pneumococcal vaccine</strong> (Pneumovax).</p>
  <div class="callout"><strong>Current guidelines differ:</strong> adult schedules now usually start with a pneumococcal conjugate vaccine rather than the polysaccharide vaccine (Pneumovax) alone.</div>
'''

# ------------------------------------------------------------------------------------------------- 3.13 summary
BODY += '''
  <h3 class="sub" id="pu-summary">3.13 &middot; Objectives 4 and 8&ndash;10 &mdash; Absorption and elimination, interactions, monitoring and patient education</h3>

  <h4 class="subsub">Absorption, distribution, metabolism and excretion (Objective 4)</h4>
  <table>
    <tr><th>Drug or group</th><th>What the slides give</th></tr>
    <tr><td><strong>Antipseudomonal cephalosporins, carbapenems, penicillins and fluoroquinolones; aminoglycosides; vancomycin</strong></td><td><strong>Require renal adjustment</strong> [slides 24 to 29]</td></tr>
    <tr><td><strong>Linezolid</strong></td><td>Intravenous and oral; good lung penetration; <strong>no renal dose adjustment</strong> [slide 30]</td></tr>
    <tr><td><strong>Aminoglycosides</strong></td><td><strong>Poor lung penetration</strong>, hence extended-interval dosing; highly dependent on renal function [slide 28]</td></tr>
    <tr><td><strong>Fluoroquinolones</strong></td><td><strong>Good lung tissue penetration</strong> [slide 27]</td></tr>
    <tr><td><strong>Isoniazid</strong></td><td>Well absorbed; enters the central nervous system; excreted mostly as an acetylated metabolite (fast and slow acetylators) [slides 37 and 38]</td></tr>
    <tr><td><strong>Ethambutol</strong></td><td>75 percent excreted unchanged: adjust in renal disease [slide 44]</td></tr>
    <tr><td><strong>Pyrazinamide</strong></td><td>Converted to pyrazinoic acid; enters macrophages [slide 45]</td></tr>
    <tr><td><strong>Epinephrine</strong></td><td>Intramuscular (preferred), subcutaneous or intravenous [slide 52]</td></tr>
    <tr><td><strong>Beta-2 agonists</strong></td><td>Short-acting: rapid, 4 to 6 hours; long-acting: 12 hours or more [slide 68]</td></tr>
    <tr><td><strong>Anticholinergics</strong></td><td>Ipratropium up to 8 hours; tiotropium 24 hours or more [slide 86]</td></tr>
    <tr><td><strong>Inhaled corticosteroids; mast cell stabilizers</strong></td><td>Up to 8 weeks for maximal effect [slide 73]; up to 4 weeks to work [slide 78]</td></tr>
    <tr><td><strong>Systemic corticosteroids in anaphylaxis</strong></td><td>Take several hours to work [slide 55]</td></tr>
    <tr><td><strong>Montelukast; omalizumab; reslizumab</strong></td><td>Oral [slide 75]; subcutaneous every 2 to 4 weeks [slide 79]; intravenous [slide 81]</td></tr>
    <tr><td><strong>Theophylline</strong></td><td>Narrow therapeutic index; the slide says renally eliminated (see the note in 3.9) [slides 82 and 85]</td></tr>
  </table>

  <h4 class="subsub">Interactions (Objective 8)</h4>
  <table>
    <tr><th>Combination</th><th>What happens</th></tr>
    <tr><td><strong>Rifampin with anticoagulants, contraceptives, chloramphenicol, digoxin, ketoconazole or theophylline</strong></td><td>Rifampin <strong>induces cytochrome P450 enzymes</strong> (CYP1A2, CYP2C9, CYP3A4) and lowers them [slide 42]</td></tr>
    <tr><td><strong>Vancomycin with other nephrotoxins</strong></td><td>Nephrotoxicity [slide 29]</td></tr>
    <tr><td><strong>Bupropion with a monoamine oxidase inhibitor</strong></td><td>Avoid [slide 105]</td></tr>
    <tr><td><strong>Bupropion with a tricyclic antidepressant or venlafaxine</strong></td><td>Use caution (noradrenergic antidepressants) [slide 105]</td></tr>
    <tr><td><strong>Histamine H2 blocker or antacid therapy</strong></td><td>A modifiable risk factor for nosocomial pneumonia [slide 18]</td></tr>
  </table>
  <p>The slides name <strong>no drug-food or drug-herb interactions</strong> for these drugs.</p>

  <h4 class="subsub">Protocols and monitoring (Objective 9)</h4>
  <ul>
    <li><strong>Community-acquired pneumonia:</strong> outpatients are treated empirically without routine tests; hospitalized patients get blood and sputum cultures <strong>before antibiotics</strong> [slide 11].</li>
    <li><strong>Nosocomial pneumonia:</strong> start at once, broad if there are multidrug-resistance risk factors, then streamline to the cultures and switch to oral when possible [slides 20 to 23 and 31].</li>
    <li><strong>Aminoglycosides:</strong> adjust dose and frequency to drug levels and renal function [slide 28]. <strong>Vancomycin:</strong> trough before the third or fourth dose (steady state) [slide 29].</li>
    <li><strong>Tuberculosis:</strong> never a single agent in active disease; four drugs for 2 months, then isoniazid and rifampin for 4 [slides 35 and 36]. <strong>Pyrazinamide:</strong> first two months only; monitor liver enzymes [slide 45]. <strong>Isoniazid:</strong> pyridoxine against neuritis [slide 39]. <strong>Ethambutol:</strong> watch vision [slide 44].</li>
    <li><strong>Theophylline:</strong> monitor plasma levels [slide 85].</li>
    <li><strong>Asthma:</strong> severity by symptoms, night awakenings, short-acting beta-2 agonist use, activity, lung function and exacerbations [slide 65]; adjust the steps up and down [slide 90]; albuterol overuse = poor control [slide 98]; status asthmaticus escalation [slide 99].</li>
    <li><strong>Chronic obstructive pulmonary disease:</strong> review inhaler technique regularly; annual influenza and pneumococcal vaccination [slides 102 and 108].</li>
  </ul>

  <h4 class="subsub">Patient education (Objective 10)</h4>
  <ul>
    <li><strong>Acute bronchitis:</strong> usually viral and self-limited; antibiotics are not routinely needed [slides 6 to 8].</li>
    <li><strong>Rifampin:</strong> tears, sweat and urine turn orange [slide 42]; contraceptives and anticoagulants may not work as well (enzyme induction) [slide 42].</li>
    <li><strong>Isoniazid:</strong> take the pyridoxine; avoid alcohol, which raises the hepatitis risk [slide 39].</li>
    <li><strong>Ethambutol:</strong> report changes in vision or color vision [slide 44].</li>
    <li><strong>Epinephrine:</strong> intramuscular is the route unless the patient is coding; expect anxiety, a racing heart and sweating [slide 52].</li>
    <li><strong>Inhaled corticosteroids:</strong> a daily controller that takes up to 8 weeks for full effect; watch for thrush [slide 73].</li>
    <li><strong>Long-acting beta-2 agonists:</strong> never alone for asthma [slide 70]. <strong>Albuterol:</strong> use sparingly; needing it often means the asthma is poorly controlled [slide 98].</li>
    <li><strong>Cromolyn and nedocromil:</strong> take regularly and before exposure; up to 4 weeks to work [slides 77 and 78].</li>
    <li><strong>Devices:</strong> clean every device regularly; a spacer for poor coordination; a dry powder inhaler needs a strong breath; the metered dose inhaler technique steps [slides 92 to 97].</li>
    <li><strong>Smoking cessation:</strong> combine medication with counseling [slide 103]; nicotine patches and gum are over the counter [slide 106]; start varenicline one week before the quit date [slide 107].</li>
  </ul>

  <div class="callout"><strong>What is left out of this section, and why.</strong>
  <ul>
    <li><strong>Doses</strong>: the tuberculosis milligram amounts (slide 35), fluid volumes (slide 50), epinephrine concentrations (slide 52), the bupropion schedule (slide 105) and the albuterol rate (slide 99). Not tested in this course.</li>
    <li><strong>Drug levels as numbers</strong>: the vancomycin trough (slide 29) and the theophylline ranges (slides 84 and 85) are not asked as numbers.</li>
    <li><strong>Points the slides get wrong or contradict</strong>, printed with a note and never asked: rifampin&rsquo;s gram-positive list (slide 40), theophylline &ldquo;renally eliminated&rdquo; (slide 85), tiotropium for chronic obstructive pulmonary disease only (slides 86 and 90), montelukast&rsquo;s &ldquo;minimal&rdquo; side effects (slide 75).</li>
    <li><strong>Where a slide differs from current guidelines,</strong> a one-line note says so: the outpatient macrolide (slide 14), health-care associated pneumonia (slide 17), ceftazidime and the vancomycin trough (slides 24 and 29), treatment duration (slide 31), the tuberculosis durations (slides 36 and 46), pyrazinamide in pregnancy (slide 45), the steroid taper (slide 89), intravenous steroids in status asthmaticus (slide 99), the chronic obstructive pulmonary disease groups (slide 102), the varenicline boxed warning (slide 107) and the pneumococcal vaccine (slide 108).</li>
    <li><strong>Boxed warnings the slides do not name</strong> are flagged in italics (fluoroquinolones, aminoglycosides, isoniazid hepatitis, omalizumab anaphylaxis); the only boxed warning the deck itself states is varenicline&rsquo;s.</li>
    <li><strong>Slides not represented:</strong> 1 (title), 2 (the deck&rsquo;s own objectives), the section title slides (3, 4, 9, 47, 56, 100), 109 (&ldquo;Questions?&rdquo;), and the chemical structures (slides 37, 40 and 43) and decorative pictures (slides 32 and 49 are described).</li>
  </ul></div>

</section>
'''

BODY = BODY.replace("@@STRESS@@", "")
