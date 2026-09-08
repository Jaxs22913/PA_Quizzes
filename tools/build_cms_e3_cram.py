#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Clinical Medicine and Surgery I, Exam 3 cram sheet (ENT block).

The guide carries the reasoning; this carries only what has to come back cold.

THE FIRST TWO SECTIONS ARE THE TESTS AND THE DURATIONS, not a condition list.
Weber and Rinne is a syllabus objective in its own right AND the question
Jaquith said outright is on the paper; the vertigo durations are the fastest
sort in the block. Everything after them is disease detail.

THE LISTS ARE GENERATED FROM THE CHART DATA. Which conditions are conductive,
which are sensorineural, which are emergent -- all read off the same rows the
chart and guide use. Hand-writing those lists is exactly how the Exam 2 sheet
drifted from its chart within the hour.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
sys.path.insert(0, HERE)
from render import render
from _cms_e3_chart_l15 import ROWS_L15, DIFF_L15
from _cms_e3_chart_l16 import ROWS_L16, DIFF_L16
from _cms_e3_chart_l17 import ROWS_L17, DIFF_L17
from _cms_e3_chart_l18 import ROWS_L18, DIFF_L18
from _cms_e3_chart_l19 import ROWS_L19, DIFF_L19

OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 3", "cms-exam-3-cram-sheet.html")
ROWS = ROWS_L15 + ROWS_L16 + ROWS_L17 + ROWS_L18 + ROWS_L19
DIFF = dict(DIFF_L15, **DIFF_L16, **DIFF_L17, **DIFF_L18, **DIFF_L19)


def strip(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()


EAR_ONLY = {r[0] for r in ROWS_L15 + ROWS_L16}


def by_hearing(kind):
    """Every EAR condition whose hearing-loss cell names this type.

    Scoped to Lectures 15 and 16 on purpose: the Lecture 17 rows use that same
    middle column for the DISCHARGE, so sweeping them in would file allergic
    rhinitis under "hearing not affected" -- true, and completely useless.
    """
    out = []
    for n, *_ in ROWS:
        if n not in EAR_ONLY:
            continue
        h = strip(DIFF[n][1]).lower()
        if kind == "cond" and "conductive" in h and "sensorineural" not in h:
            out.append(n)
        elif kind == "snhl" and "sensorineural" in h and "conductive" not in h:
            out.append(n)
        elif kind == "none" and h.startswith(("none", "not affected")):
            out.append(n)
    return out


def by_urgency(level):
    return [r[0] for r in ROWS if level in r[6].upper()]


def lst(names):
    return " &middot; ".join(strip(n).upper() for n in names)


topics = [
 dict(id="tests", label="The tests", color="#6a4fa3", tag="objectives b to f", rows=[
  ["WEBER", "Tuning fork on the MIDLINE. Compares BONE conduction between the two ears. Asks WHICH SIDE IS LOUDER."],
  ["RINNE", "Tuning fork at the EAR then the MASTOID. Compares AIR against BONE in ONE ear."],
  ["CONDUCTIVE", "Weber lateralises <b>TO the BAD ear</b>. Rinne: <b>BC &ge; AC</b>. Voice stays SOFT. Hearing BETTER in noise."],
  ["SENSORINEURAL", "Weber lateralises <b>AWAY, to the GOOD ear</b>. Rinne: <b>AC &gt; BC &mdash; SAME AS NORMAL</b>. Voice LOUD. Hearing WORSE in noise."],
  ["WHY WEBER DECIDES", "A sensorineural Rinne looks exactly like a normal ear. Only WEBER separates them."],
  ["THE QUESTION SHE PROMISED", "Fullness + reduced hearing AFTER A COLD, AMBER effusion behind an INTACT drum with REDUCED MOBILITY &rarr; conductive &rarr; <b>Weber TO that ear, BC &ge; AC</b>. She also asks it BACKWARDS: given the fork findings, name the diagnosis &mdash; the distractors die on LOSS TYPE."],
  ["AUDIOMETRY &mdash; ALL BY 20s", "Normal 0&ndash;20 &middot; MILD 20&ndash;40 &middot; MODERATE 40&ndash;60 &middot; SEVERE 60&ndash;80 &middot; <b>PROFOUND &gt;80 dB</b>. The prevalence percentages are explicitly NOT to be memorised."],
  ["TYMPANOGRAM", "<b>A</b> normal &middot; <b>B</b> FLAT = fluid or perforation &middot; <b>C</b> peak NEGATIVE = eustachian tube dysfunction &middot; <b>As</b> SHALLOW/stiff = ossicular FIXATION, tympanosclerosis &middot; <b>Ad</b> DEEP = ossicular DISCONTINUITY, monomeric drum."],
  ["VESTIBULAR", "<b>ELECTRONYSTAGMOGRAPHY</b> = gold standard, one ear at a time. <b>MRI WITH GADOLINIUM</b> = gold standard for RETROCOCHLEAR. <b>DIX-HALLPIKE</b> diagnoses positional vertigo; <b>EPLEY</b> treats it."],
 ]),
 dict(id="vertigo", label="Vertigo, by how long it lasts", color="#15707f",
      tag="she said definitely know this", rows=[
  ["SECONDS (10&ndash;60)", "<b>BENIGN PAROXYSMAL POSITIONAL VERTIGO.</b> On rolling over. Hearing NOT affected, NO tinnitus. Beyond a MINUTE &rarr; think again. Dix-Hallpike diagnoses, EPLEY treats."],
  ["MINUTES TO HOURS", "<b>M&Eacute;NI&Egrave;RE&rsquo;S.</b> Tetrad: vertigo + FLUCTUATING LOW-FREQUENCY sensorineural loss + LOW-TONE tinnitus + FULLNESS. Hearing IS affected. RULE OUT SYPHILIS &mdash; indistinguishable."],
  ["DAYS TO WEEKS, hearing AFFECTED", "<b>LABYRINTHITIS.</b> Inflammation of the membranous labyrinth. Viral. Meclizine or diazepam, steroids, antibiotics ONLY if bacterial features."],
  ["DAYS TO WEEKS, hearing NORMAL", "<b>VESTIBULAR NEURONITIS.</b> Inflammation of the VESTIBULAR portion of CN VIII. BENIGN and SELF-LIMITING. No hearing change, NO focal neurology."],
  ["THE ONE WORD", "Labyrinthitis vs vestibular neuronitis = <b>does it affect HEARING</b>. That is the whole difference."],
  ["CENTRAL &mdash; STOP", "Vertigo + FACIAL PARALYSIS, CROSSED sensory loss, GAZE palsy or HORNER = <b>VERTEBROBASILAR</b>. Vertigo + ATAXIA, HEADACHE or facial numbness = <b>CEREBELLAR INFARCT</b>. Both EMERGENT."],
 ]),
 dict(id="sort", label="Sort the whole block", color="#3a3a6b", tag="generated from the chart",
      rows=[
  ["CONDUCTIVE", lst(by_hearing("cond"))],
  ["SENSORINEURAL", lst(by_hearing("snhl"))],
  ["HEARING NOT AFFECTED", lst(by_hearing("none"))],
  ["EMERGENT", lst(by_urgency("EMERGENT"))],
 ]),
 dict(id="om", label="The otitis media family", color="#8f5aa8", rows=[
  ["ACUTE OTITIS MEDIA", "BULGING ERYTHEMATOUS drum, reduced mobility. Otalgia + FEVER + hearing loss. Peak age ~<b>2 YEARS</b>; adults only 3&ndash;15%."],
  ["ITS CAUSE &mdash; the slide is incomplete", "<b>FAR AND AWAY MOST ARE VIRAL.</b> Bacterial three: <b>S. PNEUMONIAE, H. INFLUENZAE, M. CATARRHALIS</b>. M. catarrhalis has OVERTAKEN H. influenzae because of VACCINATION &mdash; ask IMMUNISATION STATUS."],
  ["ITS TREATMENT", "MOST RESOLVE SPONTANEOUSLY. Bacterial &rarr; <b>AMOXICILLIN</b>. RECURRENT = 3 in 6 months or &gt;4 in 12 &rarr; TYMPANOSTOMY TUBES."],
  ["OTITIS MEDIA WITH EFFUSION", "DULL drum, AIR&ndash;FLUID LEVEL, reduced mobility. OFTEN ASYMPTOMATIC, found incidentally. Treat on <b>DURATION + degree of hearing loss + effect on SPEECH AND LANGUAGE</b>."],
  ["CHRONIC OTITIS MEDIA", "<b>NON-HEALING PERFORATION.</b> Benign = dry. With effusion = serous drainage. SUPPURATIVE = pus. Refer to ENT."],
  ["MASTOIDITIS", "Spread into the MASTOID AIR CELLS. Complication of acute otitis media &mdash; alongside PERFORATION, LABYRINTHITIS, rarely MENINGITIS."],
 ]),
 dict(id="canal", label="The canal", color="#a4502a", rows=[
  ["OTITIS EXTERNA", "<b>PAIN ON MOVING THE TRAGUS.</b> Swimmer. <b>P. AERUGINOSA 38%</b>. Remove debris FIRST, then drops &plusmn; steroid. WICK if the canal is closed."],
  ["MALIGNANT (NECROTIZING)", "<b>ELDERLY DIABETIC</b> + <b>PAIN OUT OF PROPORTION</b> + <b>FACIAL NERVE WEAKNESS</b>. &gt;95% P. aeruginosa. IMAGING shows BONY involvement. <b>ANTIPSEUDOMONAL</b> &mdash; ciprofloxacin. EMERGENT."],
  ["OTOMYCOSIS", "ITCH &gt; pain. <b>ASPERGILLUS = &ldquo;WET NEWSPAPER&rdquo;</b>. <b>CANDIDA = WHITE CURD</b>. Debris removal + topical antifungal."],
  ["CERUMEN IMPACTION", "MOST OFTEN <b>SELF-INDUCED BY CLEANING</b>. Irrigate ONLY if the drum is INTACT, body-temperature water. TUBES or PERFORATION &rarr; ENT."],
  ["FOREIGN BODY", "DO NOT PUSH DEEPER. Firm &rarr; loop/hook. Soft &rarr; alligator forceps. <b>ORGANIC SWELLS WHEN WET</b> &mdash; no irrigation. INSECT &rarr; LIDOCAINE first."],
  ["CARCINOMA OF THE CANAL", "<b>OTITIS EXTERNA THAT WILL NOT RESPOND</b> + BLOODY otorrhoea + FRIABLE canal. Often MISDIAGNOSED. <b>BIOPSY.</b> EMERGENT."],
 ]),
 dict(id="drum", label="The drum, pressure and fixation", color="#7a5a2e", rows=[
  ["EUSTACHIAN TUBE DYSFUNCTION", "<b>RETRACTED</b> drum, reduced mobility. Fullness + CRACKLING/POPPING after a cold. Decongestant + intranasal steroid. <b>NO FLYING until it resolves.</b>"],
  ["BAROTRAUMA", "Flying or DIVING. <b>HAEMOTYMPANUM.</b> Window rupture adds VERTIGO + TINNITUS + SENSORINEURAL loss. MYRINGOTOMY gives instant relief."],
  ["TM PERFORATION", "<b>THE PAIN STOPS</b> when it ruptures. CENTRAL vs MARGINAL. Most heal; after acute otitis media as fast as <b>48&ndash;72 HOURS</b>."],
  ["CHOLESTEATOMA", "<b>KERATIN in a RETRACTION POCKET</b> + <b>RECURRENT OTORRHOEA WITH NO OTITIS EXTERNA</b>. Not a neoplasm, no cholesterol. CT for extent. <b>SURGERY</b> &mdash; it erodes bone."],
  ["OTOSCLEROSIS", "<b>STAPES fixation.</b> Gradual CONDUCTIVE loss with a <b>NORMAL DRUM</b>. <b>HEARS BETTER IN NOISE.</b> Weber TO the affected ear. CT first-line imaging. Stapes prosthesis."],
  ["AURICULAR HAEMATOMA", "Sub-perichondrial. Landmarks LOST. <b>DRAIN WITHIN 7 DAYS</b> &mdash; then splint. Re-check at 12&ndash;24h because it can appear LATE. Otherwise CAULIFLOWER EAR."],
 ]),
 dict(id="snhl", label="Sensorineural causes worth knowing cold", color="#2a5f8f", rows=[
  ["PRESBYCUSIS", "Commonest sensorineural loss. BILATERAL, SYMMETRICAL, GRADUAL, <b>HIGH FREQUENCY FIRST</b>. &ldquo;Hears but cannot make out words.&rdquo; Screen from <b>65</b>."],
  ["OTOTOXICITY", "<b>AMINOGLYCOSIDES</b> most ototoxic and most common &mdash; monitor peaks. Also FUROSEMIDE, ASPIRIN, PLATINUM. <b>Ototoxic drugs are frequently NEPHROTOXIC too.</b>"],
  ["NOISE-INDUCED", "TEMPORARY threshold shift recovers in <b>24&ndash;48h</b>; repeated exposure makes it PERMANENT. Damage from ~80 dB; PAIN at 120."],
  ["SUDDEN SNHL", "<b>UNILATERAL. A SYNDROME, NOT A DISEASE.</b> Viral or vascular. <b>SAME-DAY ENT REFERRAL</b> &mdash; steroids work only in the first weeks."],
  ["ACOUSTIC NEUROMA", "UNILATERAL loss with <b>SPEECH DISCRIMINATION WORSE THAN THE TONES PREDICT</b>. May involve CN V and VII. <b>MRI WITH GADOLINIUM.</b>"],
  ["PERILYMPHATIC FISTULA", "<b>AUDIBLE POP</b> then sudden loss + vertigo after STRAINING, DIVING or a BLOW. Round or oval window."],
  ["SYPHILIS", "<b>INDISTINGUISHABLE FROM M&Eacute;NI&Egrave;RE&rsquo;S</b> and TREATABLE. Order <b>FTA-ABS and MHA-TP</b>; <b>VDRL IS NOT HELPFUL</b>. Antibiotic + systemic steroid."],
  ["GLOMUS TUMOUR", "<b>PULSATILE TINNITUS</b> + vascular middle ear mass. Can paralyse CN IX, X, XI."],
  ["TINNITUS RED FLAG", "<b>UNILATERAL or PULSATILE</b> is investigated. No drug beats placebo; masking and biofeedback may help."],
 ]),
 dict(id="nose", label="Nose and sinuses", color="#9c5230", tag="Lecture 17", rows=[
  ["ACUTE SINUSITIS", "<b>UNDER 4 WEEKS.</b> <b>90&ndash;98% VIRAL</b>; only 0.5&ndash;2% superinfect. Pain <b>WORSE BENDING FORWARD</b>, localises to the sinus. 1 in 8 adults; <b>5th leading reason antibiotics are prescribed</b>."],
  ["BACTERIAL &mdash; the 5 features", "<b>DOUBLE WORSENING</b> after 5&ndash;6 days &middot; <b>&ge;10 DAYS</b> persistent &middot; persistent PURULENT discharge &middot; <b>UNILATERAL</b> tooth/facial pain or maxillary tenderness &middot; FEVER."],
  ["PAIN IS THE DISCRIMINATOR", "Pain occurs <b>ONLY in bacterial and fungal</b> sinusitis and is <b>REPRODUCIBLE ON PALPATION</b>. A common cold is not."],
  ["DISCHARGE COLOUR", "<b>Yellow/green = LEAST helpful.</b> Clear = viral or allergic. Yellow AND putrid = bacterial. <b>BLACK = FUNGUS.</b> Rust = possible S. pneumoniae."],
  ["SINUSITIS DIAGNOSTICS", "<b>NO test separates viral from bacterial.</b> Routine radiography DISCOURAGED &mdash; 3+ clinical findings match imaging accuracy. <b>CT</b> for recurrence, treatment failure, or suspected EXTRASINUS involvement."],
  ["SINUSITIS TREATMENT", "Most improve WITHOUT antibiotics. Symptomatic: decongestants, NSAIDs, lavage, intranasal steroids. <b>Bacterial &rarr; AMOXICILLIN/CLAVULANATE.</b> Penicillin allergy &rarr; <b>DOXYCYCLINE</b> or moxifloxacin. Influenza &rarr; oseltamivir 5 days if &gt;13."],
  ["URGENT IN SINUSITIS", "<b>DIPLOPIA</b> or visual disturbance &middot; <b>PERIORBITAL swelling/erythema</b> &middot; <b>ALTERED MENTAL STATUS</b>. Get the CT."],
  ["CHRONIC SINUSITIS", "<b>OVER 12 WEEKS.</b> Impaired MUCOCILIARY CLEARANCE &rarr; REPEATED infections, not one persistent one. Oral steroids + <b>2 weeks amoxicillin/clavulanate</b>; courses often 3&ndash;4 weeks. ENT for surgery, allergy for skin testing."],
  ["CHRONIC FUNGAL", "<b>ASPERGILLUS</b>, noninvasive, immunocompetent. Mild disease cured by <b>ENDOSCOPIC SURGERY WITHOUT ANTIFUNGALS</b>. Fungus ball &rarr; surgery, antifungals ONLY if bony erosion. Allergic form: polyps + asthma + <b>PEANUT-BUTTER mucus</b>."],
  ["DEVIATED SEPTUM", "One passage smaller. Congestion &rarr; ANOSMIA; severe = <b>OSA, snoring, facial pain, RECURRENT NOSEBLEEDS</b>. Treatment SEPTOPLASTY."],
  ["PERFORATED SEPTUM", "<b>INTRANASAL STEROIDS or COCAINE</b> &mdash; chronic ischaemia. Rarely GRANULOMATOSIS WITH POLYANGIITIS or secondary SYPHILIS. Treat the cause; else septoplasty."],
  ["SEPTAL HAEMATOMA", "Between septum and PERICHONDRIUM. Usually TRAUMA; associated with nasal fracture. <b>DRAIN via intranasal incision under general anaesthesia.</b>"],
  ["EPISTAXIS &mdash; ANTERIOR", "<b>90%</b>, from <b>KIESSELBACH&rsquo;S PLEXUS</b>. Commonest cause = <b>the patient&rsquo;s finger</b>. Peaks &lt;10 and 45&ndash;65; WINTER."],
  ["EPISTAXIS &mdash; POSTERIOR", "<b>SPHENOPALATINE ARTERY.</b> Significant haemorrhage. <b>HIGHER RISK because of ASPIRATION</b> and subsequent infection."],
  ["STOPPING THE BLEED", "Blow out clots &rarr; spray <b>OXYMETAZOLINE</b> &rarr; <b>PINCH THE ALAE 10 MINUTES CONTINUOUSLY</b>. Sit up, lean FORWARD. Cold compress. Then tampons, packing, balloon catheters, thrombogenic foams. <b>DO NOT BLOW THE NOSE.</b>"],
  ["EPISTAXIS WORKUP", "<b>PT/INR is NOT routine</b> &mdash; only if anticoagulated. Haematocrit + type and crossmatch if massive, with <b>2 large-bore IV lines</b>."],
  ["NASAL FOREIGN BODY", "<b>UNILATERAL PURULENT FOUL-SMELLING discharge in a young child.</b> Floor of the passage under the INFERIOR turbinate, or in front of the MIDDLE turbinate. Visualisation is the diagnosis."],
  ["NASAL FRACTURE &mdash; no x-ray if", "<b>ALL FOUR:</b> tenderness/swelling ISOLATED to the bony bridge &middot; breathes through EACH naris &middot; nose STRAIGHT, no septal deviation &middot; <b>NO SEPTAL HAEMATOMA</b>. Otherwise film it. Initial care: ICE + head of bed up."],
  ["NASAL POLYPS", "<b>GREY, GLISTENING</b> masses &rarr; congestion, thick discharge, <b>ANOSMIA</b>. Asthma 20&ndash;50%, <b>allergic fungal sinusitis 85%</b>, aspirin intolerance 8&ndash;20%, alcohol intolerance 50%, Churg-Strauss 50%, <b>CF 5&ndash;44%</b>. <b>EVALUATE EVERY CHILD WITH MULTIPLE POLYPS FOR CF AND ASTHMA</b> &mdash; chloride sweat test. Surgery gives only TEMPORARY relief."],
  ["ALLERGIC RHINITIS", "<b>CLEAR discharge from BOTH nostrils</b>, <b>BLUISH hue</b>, oedematous mucosa, &plusmn; polyps. <b>80% end up on 2+ medicines.</b> Antihistamine + leukotriene inhibitor at night + intranasal steroid; ipratropium; immunotherapy. <b>Allergy creates the environment for infection but is not itself an -itis.</b>"],
  ["NASOPHARYNGEAL CARCINOMA", "<b>NECK MASS + DIPLOPIA + facial numbness + headache.</b> <b>EBV</b>, HPV, smoking; endemic SOUTHERN CHINA; <b>2&ndash;3&times; more in males</b>. ENT + endoscopic guided biopsy."],
 ]),
 dict(id="neck", label="Neck masses", color="#2f6b6f", tag="Lecture 18", rows=[
  ["THINK MALIGNANCY WHEN", "No infectious origin &middot; <b>&gt;2 WEEKS</b> &middot; <b>&gt;1.5 CM</b> &middot; FIRM, non-cystic, NON-TENDER, immobile &middot; <b>AGE &gt;40</b> &middot; tobacco + alcohol &middot; ULCERATION. Under 40 most are inflammatory &mdash; <b>except HODGKIN LYMPHOMA</b>."],
  ["FOUR RULES OF THUMB", "Present for YEARS = benign (lipoma, cyst) &middot; RAPIDLY growing = infectious if other symptoms, <b>LYMPHOMA if not</b> &middot; FLUCTUANT = cystic &middot; <b>PULSATILE or BRUIT = VASCULAR</b>."],
  ["MIDLINE vs LATERAL", "<b>MIDLINE</b> &rarr; THYROGLOSSAL DUCT CYST (moves with tongue protrusion), DERMOID CYST, THYROID. <b>LATERAL</b> &rarr; BRANCHIAL CLEFT CYST (anterior border of SCM), lymphadenopathy, cystic hygroma."],
  ["THE TWO CONGENITAL SIGNS", "<b>THYROGLOSSAL DUCT CYST moves VERTICALLY with SWALLOWING or TONGUE PROTRUSION</b> &mdash; pathognomonic, and why the SISTRUNK operation takes the CENTRE OF THE HYOID. <b>LYMPHANGIOMA TRANSILLUMINATES.</b>"],
  ["BRANCHIAL CLEFT CYST", "Infected after a URI. <b>AVOID I&amp;D</b> &mdash; it makes definitive excision harder; needle aspiration if you must. <b>Rule out HPV-associated SCC in an adult</b> &mdash; it can present as a cystic neck mass."],
  ["HAEMANGIOMA", "Grows through year 1, <b>involutes at 18&ndash;24 months</b>, <b>90% self-resolve</b>. Enlarges with CRYING. First line if you must treat: <b>PROPRANOLOL</b>."],
  ["THE EXPOSURE HISTORIES", "<b>CATS scratch</b> &rarr; <i>Bartonella henselae</i> &middot; <b>CAT FAECES / undercooked meat</b> &rarr; toxoplasmosis &middot; <b>RABBITS, TICKS</b> &rarr; tularemia (STREPTOMYCIN) &middot; <b>UNPASTEURISED MILK</b> &rarr; brucellosis (total-body nodes)."],
  ["MYCOBACTERIA, THE TWO", "<b>ATYPICAL</b>: children, <b>UNILATERAL</b>, <b>BRAWNY reddish-brown skin</b>, surgical excision. <b>TB (SCROFULA)</b>: adults &gt; children, <b>DIFFUSE and BILATERAL</b>, <b>RIPE</b>."],
  ["THE WORKUP", "<b>FNA BIOPSY = STANDARD OF CARE</b>, minimum <b>4 PASSES</b>; separates neoplasm from inflammation and carcinoma from lymphoma. <b>FNA not EXCISIONAL</b> &mdash; excision spills tumour. <b>AVOID IODINE CONTRAST if thyroid cancer is suspected.</b>"],
  ["THYROID MASS", "<b>Immobile MIDLINE mass that ELEVATES WITH SWALLOWING.</b> Low TSH + nodule &rarr; <b>RADIONUCLIDE SCAN FIRST</b>: <b>HOT = no biopsy</b> (low malignant risk); <b>COLD or WARM = FNA</b>."],
  ["THYROID CANCER, THE FOUR", "<b>PAPILLARY 75%</b>, best prognosis, young women &middot; <b>FOLLICULAR 16%</b>, spreads by <b>BLOOD to BONE and LUNG</b>, H&uuml;rthle variant worse &middot; <b>MEDULLARY 5%</b>, <b>C cells, CALCITONIN</b>, screen family for <b>MEN</b> &middot; <b>ANAPLASTIC 1%</b>, elderly, <b>death 6&ndash;36 months</b>, resistant to everything."],
  ["THYROID LYMPHOMA", "Non-Hodgkin B cell, on a background of <b>HASHIMOTO</b>. <b>FNA alone cannot separate it from Hashimoto</b> &mdash; needs biopsy. <b>Chemo + radiation, NOT surgery.</b>"],
 ]),
 dict(id="oral", label="Mouth, throat and jaw", color="#8c4a5f", tag="Lecture 19", rows=[
  ["THE SCRAPE TEST", "<b>WIPES OFF &rarr; CANDIDIASIS.</b> <b>Will NOT scrape off + WHITE &rarr; LEUKOPLAKIA</b> (premalignant, <b>5&ndash;20% &rarr; SCC</b>). <b>Lacy white lines &rarr; LICHEN PLANUS</b> (Wickham striae, 1&ndash;4% &rarr; SCC). <b>Disappears on STRETCHING &rarr; LEUKOEDEMA</b>, a normal variant."],
  ["ERYTHROPLAKIA", "Like leukoplakia but <b>RED</b>. <b>90% are already dysplastic or carcinoma.</b> Red beats white for danger, every time."],
  ["HAIRY LEUKOPLAKIA", "<b>LATERAL TONGUE</b>, painless, waxes and wanes. <b>EBV</b>. <b>Strongly associated with HIV &mdash; a common EARLY finding.</b>"],
  ["APHTHOUS vs HERPES", "<b>APHTHOUS &rarr; NON-KERATINISED, freely moving mucosa</b> (buccal, labial, non-attached gingiva); yellow-grey centre, RED HALO. <b>HERPES &rarr; keratinised surfaces</b>, with a <b>24-hour BURNING PRODROME</b>. Recurrent aphthous = <b>SUTTON DISEASE</b>."],
  ["SIALOLITHIASIS", "<b>Pain and swelling WITH EATING</b> (salivary colic). <b>80&ndash;90% SUBMANDIBULAR</b> &mdash; longer duct, alkaline mucin-rich saliva. <b>RADIOPAQUE.</b> CT most sensitive; digital subtraction sialography most accurate."],
  ["SUPPURATIVE SIALADENITIS", "<b>PAROTID</b>, dehydrated post-op or elderly patient. <b><i>S. aureus</i></b>. <b>PUS FROM THE DUCT.</b> Rehydrate + antistaphylococcal antibiotics. <b>No improvement in 48 h = presume ABSCESS.</b>"],
  ["VOCAL CORDS", "<b>NODULES: BILATERAL, symmetric</b>, junction of anterior 1/3 and posterior 2/3, vocal abuse, <b>SPEECH THERAPY first line</b>. <b>POLYPS: UNILATERAL</b>, smokers, <b>excise &mdash; may hide an occult SCC</b>. <b>PAPILLOMATOSIS: HPV 6 and 11</b>, warty, <b>AVOID TRACHEOSTOMY</b>."],
  ["HOARSENESS CLOCK", "<b>ACUTE LARYNGITIS</b> = commonest cause, persists ~1 week after the cold clears, <b>NO antibiotics</b>. <b>&gt;2 WEEKS = CHRONIC = not a diagnosis &rarr; SCOPE IT</b> for cancer and polyps."],
  ["EPIGLOTTITIS", "<b>ENT EMERGENCY.</b> Children <b>4 Ds: DROOLING, DYSPHAGIA, DYSPHONIA, DISTRESS</b> + <b>TRIPOD</b> position. <b>HIB</b>. <b>DO NOT examine the mouth or draw blood</b> &mdash; it can complete the obstruction. <b>THUMBPRINT SIGN not needed</b>; <b>laryngoscopy is the gold standard</b>. <b>STRIDOR IS LATE.</b>"],
  ["CENTOR", "+1 each: <b>NO COUGH</b>, tonsillar EXUDATE, FEVER, tender anterior cervical NODES. Age <b>3&ndash;14 +1</b>, 15&ndash;44 <b>0</b>, <b>&ge;45 &minus;1</b>. <b>Negative rapid test &rarr; ALWAYS culture.</b> Definitive = <b>ASO</b>. Treat: <b>PENICILLIN VK 10 DAYS</b>."],
  ["MONONUCLEOSIS", "<b>Fever + tonsillar pharyngitis + cervical adenopathy</b>, ages 15&ndash;24, <b>EBV 90%</b>. <b>MONOSPOT falsely negative in WEEK 1.</b> <b>NO CONTACT SPORTS ~1 MONTH</b> &mdash; splenic rupture. <b>GIVING PENICILLIN CAUSES A RASH</b> &mdash; that rash is often how the diagnosis gets made."],
  ["RHEUMATIC FEVER", "<b>2&ndash;3 WEEKS</b> after untreated GABHS, peak ages <b>5&ndash;15</b>. Cross-reactive antibodies attack heart muscle. <b>This is why a sore throat gets an antibiotic at all.</b>"],
  ["PERITONSILLAR ABSCESS", "<b>TRIAD: TRISMUS (most reliable) + UVULAR DEVIATION + DYSPHONIA.</b> <b>&ldquo;HOT POTATO&rdquo; voice.</b> Commonest deep head and neck infection. Airway first, then <b>needle aspiration / I&amp;D</b> + amoxicillin-clavulanate or clindamycin."],
  ["RETROPHARYNGEAL ABSCESS", "<b>SURGICAL EMERGENCY.</b> Child <b>&lt;5</b>. <b>WIDENED RETROPHARYNGEAL SPACE</b> on lateral neck XR; <b>CT is gold standard</b>. <b>MEDIASTINITIS carries 50% MORTALITY.</b>"],
  ["LUDWIG ANGINA", "<b>EMERGENCY.</b> Floor of mouth + submental + sublingual + submandibular. <b>TONGUE PUSHED UP AND BACK.</b> Usually ODONTOGENIC &mdash; <b>dental consult is part of the treatment</b>. PCN + metronidazole; bilateral submental drainage if the airway is threatened."],
  ["DIPHTHERIA", "<b>TENACIOUS GREY MEMBRANE</b> over tonsils and pharynx, unimmunised child. <b>ANTITOXIN from the CDC</b> + PCN or erythromycin <b>14 days</b>. <b>MYOCARDITIS</b> and <b>cranial neuropathy</b> are the killers."],
  ["TMJ DISORDERS", "<b>SECOND commonest musculoskeletal cause of pain and disability.</b> Women of childbearing age. Three categories: <b>MYOFASCIAL PAIN, INTERNAL DERANGEMENT, ARTHRITIS</b>. <b>The ear symptoms are the trap</b> &mdash; tinnitus, fullness, dizziness with a normal ear exam."],
  ["ORAL CANCER", "<b>NON-HEALING ULCER.</b> Tobacco + alcohol; <b>60&ndash;80% of OROPHARYNGEAL is HPV</b>. <b>SCC commonest.</b> <b>REFERRED OTALGIA</b> and ill-fitting dentures in advanced disease. Oral cavity &rarr; <b>SURGERY ALONE</b>; oropharynx &rarr; <b>SURGERY + RADIOTHERAPY</b>."],
  ["SALIVARY NEOPLASM", "<b>The SMALLER the gland, the likelier MALIGNANT.</b> Parotid <b>75&ndash;80% benign</b>; minor glands only <b>35% benign</b>. Commonest benign = <b>PLEOMORPHIC ADENOMA</b>; commonest malignant = <b>MUCOEPIDERMOID CARCINOMA</b>. <b>PAIN or FACIAL NERVE involvement = bad prognosis.</b>"],
 ]),
]

html = render(
    title="Clinical Medicine and Surgery I &middot; Exam 3 &mdash; Cram Sheet",
    kicker="PAJ 5500 &middot; Class of 2028",
    h1="Clinical Medicine and Surgery I &middot; Exam 3",
    sub="Ear, nose and throat block &mdash; Lectures 15 to 17, everything that has to be "
        "recallable cold",
    topics=topics,
    guide_href="cms-exam-3-study-guide.html",
    footer_note=("The study guide carries the reasoning; this is the night-before sheet. "
                 "Lectures 18 and 19 are added as they are delivered. Where a slide is incomplete "
                 "and the lecturer corrected it out loud, the correction is what is written."),
    primary="#6a4fa3")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB, %d sections, %d rows)"
      % (os.path.basename(OUT), len(html) // 1024, len(topics),
         sum(len(t["rows"]) for t in topics)))
