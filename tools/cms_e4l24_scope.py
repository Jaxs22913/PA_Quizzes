# -*- coding: utf-8 -*-
"""Lecture 24 Coronary Artery Disease (Carter) -- scope for the guarded CMS Exam 4 partition.

The deck, the verbatim syllabus objectives, and everything the partition must
refuse for this lecture. Taught Fri 2026-09-25 (two recordings). The content
map is work/cms-carter/l23-coronary-artery-disease-map.md -- labeled "l23" but
this is Lecture 24. Errata and emphasis: work/audio-carter/l24-errata.md and
l24-cad-emphasis.md.

NO SLIDE ERRATUM this lecture (errata section A): his one "that's wrong"
retracts his own spoken claim that V4 is lateral, so slide 61 stands (V3-V4
anterior). The rule is therefore plain: THE SLIDE WINS, and his spoken slips
are never keyed.

SLIDE 72a (SUPPLEMENT). The troponin slide he projected between posted slides
71 and 72 is not in the posted deck; Jaxon photographed it. It is treated as
deck content and cited as SUPP below. He said its numbers are "the numbers that
you need to know for testing".

DEFAULTS DECIDED FOR THIS BUILD (Jaxon may overturn any of them -- each is a
line below):
  D1  troponin: KEY standard troponin I above 0.04 ng/mL = abnormal;
      high-sensitivity troponin I 99th percentile 12 ng/L women, 20 ng/L men;
      troponin as a RULE-OUT tool; the serial draw ("when you get one, you have
      to get two"); troponin I is heart-specific. NEVER a stem value at a
      cut-off (STEM_BANNED), never a bare "troponin" with a number (LINTS).
      NOT keyed: the 1-hour / 3-hour deltas and "as early as 90 min" (never
      spoken), the LOQ / highest reportable rows, the 40 ng/L row.
  D2  risk scores: key ONLY "TIMI 3 or higher -> early invasive approach"
      (intensive care or emergent revascularization, slide 72). No other score
      cut-off or percentage -- HEART bands and MACE percentages included; the
      HEART components themselves may be asked.
  D3  "must markers be present for STEMI" (slide 65 vs the audio) -- unasked.
  D4  vasospastic electrocardiogram: slide 90 -- transient ST changes, ST
      elevation during an episode, that resolve. Slide 91's "T-wave inversion;
      maybe ST depression" is unkeyed AND never used as a marked-wrong
      distractor (TOPIC_BANNED).
  D5  NSTEMI electrocardiogram: slide 47's wording (ST depression >1 mm and/or
      T-wave inversion in two or more consecutive leads). Never slide 86's
      "ST inversion".
  D6  nitroglycerin in right ventricular infarct: AVOID (slide 63; spoken three
      times). Every stem that withholds it names the right ventricular
      involvement -- never an inferior infarct alone (LINTS). Slide 73's
      "caution" is never keyed against "do not give".
  D7  no electrocardiogram pictures. Posterior infarct = ST depression V1-V3,
      confirmed with posterior leads V7-V9 (slide 62's row, per the audio).
  D8  drug classes may be named ("P2Y12 receptor antagonist"); no how-does-it-
      work stems, no dosing, generic names only, no bare acronyms.
  D9  microvascular angina / MINOCA: the deck's definitions stay (guide caveat);
      no question asks students to tell them apart -- "MINOCA" and
      "non-obstructive" are banned from questions outright.
  D10 coronary dominance: the number is avoided (67% banned; slide 62's
      70-85% banned).
  D11 his spoken slips are never keyed -- every errata "unkeyed" item is one
      SCOPE_BANNED line below.
  D12 dual antiplatelet durations (slide 52 vs 83 differ): unkeyed.
  D13 deck typos (Forsinopril, Antistreplase, "Drug Eluding", "suppled",
      "PCTA"): correct spellings in content; the typos are banned.

EXCLUDED SLIDES: 54 (Braunwald table, brushed past, mis-cited "APACHE II") and
56-60 (unannotated electrocardiogram pictures -- no picture questions; the
posterior-infarct teaching is cited to slide 62's row).
"""

DECK = "Coronary Artery Disease Carter 2026.pptx"
SUPP = "Coronary Artery Disease Carter 2026 - SUPPLEMENT slide 72a"
EXTRA_CITES = (SUPP,)


def C(*n):
    return "%s, Slide%s %s" % (DECK, "s" if len(n) > 1 else "", ", ".join(str(x) for x in n))


def CS(*n):
    """Cite the troponin supplement (72a), optionally after deck slides."""
    return (C(*n) + "; " + SUPP) if n else SUPP


# Syllabus page 14 of 26, verbatim (checked with pypdf 2026-09-25), including the
# syllabus's own broken lettering (a lone "b." before the angina sub-list) and
# its typo "infraction". Objective d names populations the deck narrows to
# "adult and elderly" (deck slide 2).
IO_A = ("Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing (including ordering and interpretation), management "
        "(acute and chronic, including applicable rehabilitative and palliative care), appropriate "
        "referrals, patient education, and prognosis of the following coronary artery disease:")
IO_ANG = "Angina pectoris"
IO_STABLE = "Stable"
IO_UNSTABLE = "Unstable"
IO_VSA = "Vasospastic (Prinzmetal variant)"
IO_ACS = "Acute coronary syndrome"
IO_AMI = "Acute myocardial infraction"
IO_NSTE = "Non-ST segment elevation"
IO_STE = "ST segment elevation"
IO_D = ("Identify medical care strategies for coronary artery disease in the lecture topic list for the "
        "following populations.")
IOS = [IO_A, IO_ANG, IO_STABLE, IO_UNSTABLE, IO_VSA, IO_ACS, IO_AMI, IO_NSTE, IO_STE, IO_D]

# Topics (shared by every pool so the partition's topic terms line up).
T_ANAT = "Ischemia and coronary anatomy"
T_RISK = "Atherosclerosis and risk factors"
T_PRES = "Angina presentation"
T_WORK = "Chest pain workup and risk scores"
T_TROP = "Troponin"
T_SA = "Stable angina"
T_UA = "Unstable angina and non-ST-elevation infarction"
T_ECG = "Electrocardiogram localization"
T_STEMI = "ST-elevation infarction and right ventricular infarct"
T_REV = "Catheterization and revascularization"
T_POST = "Post-infarction care and sudden cardiac death"
T_VSA = "Vasospastic angina"
T_MVA = "Microvascular angina"

EXCLUDED_SLIDES = {54, 56, 57, 58, 59, 60}

SCOPE_BANNED = [
    # ---- errata section C/E: his spoken slips and unkeyed items, one line each
    r"women (over|older than|above|>) ?45",                                  # C10 "women over 45" (slide 23: <45)
    r"(under|younger than|below|<) ?15\b",                                   # C11 "under 15" (slide 88: <50)
    r"90th percentile|99 ?% of (people|patients)",                           # C12 + the 40-row misreading
    r"(nitroglycerin|nitrates?)[^.?;]{0,40}\b(is|are|acts? as) an? phosphodiesterase",  # C16 NTG "PDE inhibitor"
    r"miss(es|ed)? 2[23]|sensitivity (of )?90|specificity (of )?77|\b77 ?%",  # C9 stress-test numbers / his arithmetic
    r"cardiac enzyme|troponin is an enzyme",                                 # C20 "enzyme"
    r"orders? of magnitude|limit of quantitation|\bLOQ\b|highest reportable|25,?000",  # 72a LOQ / range rows
    r"\bdelta\b|at (1|one|3|three) hours? from baseline|as early as",       # D1 deltas + "90 min" (never spoken)
    r"\b40 ng/L|hs-Tn 40|traditional",                                       # 72a 40 row (misread in class)
    r"improved specificity|specificity to rule",                             # C26 slide wording
    r"dead tissue",                                                          # C8 "elevation = dead tissue"
    r"usually (a |the )?vein\b|vein[^.?;]{0,30}first choice",               # C7 CABG "usually a vein"
    r"avoid(ing|ed)? (all |the |any )?beta[- ]blockers",                     # C14 quantifier dropped (slide: nonselective)
    r"morphine[^.?;]{0,60}(shown|mortality|survival|benefit|helps?\b|gone away)",  # C17 morphine remarks cancel
    r"caution[^.?;]{0,60}(inferior|right[- ]sided)",                         # B3 slide 73 "caution" never keyed
    r"\bevery inferior|\ball inferior",                                          # B3 overgeneralization
    r"\bST[- ](segment )?inversion",                                         # B1 slide 86 wording
    r"(markers?|troponin)[^.?;]{0,40}must be present|must be present[^.?;]{0,40}(marker|troponin)",  # C2 / D3
    r"MINOCA|non-?obstructive",                                              # C15 / D9 no MINOCA item
    r"hypothyroid|hypothermia",                                              # C13 ASR-ambiguous (slide: hyper-, hyper-)
    r"inferolateral|high[- ]lateral",                                        # C21/C22 picture reads; slide 62 self-study rows
    r"\b67\b|15 ?[-–] ?33|70 ?[-–] ?85|8 ?[-–] ?12 ?%|co-?dominan",          # C1 / D10 dominance numbers
    r"2\.5 ?mm|1\.5 ?mm|men (under|younger than|<) ?40|men (≥|over|aged) ?40",  # C3 slide 62 V2-V3 cut-offs
    r"Braunwald|APACHE",                                                     # C5 / C23 slide 54 excluded
    r"\b0\.2 ?mg",                                                           # C5 unrecoverable spoken dose
    # ---- D2 risk scores: only "TIMI 3 or higher"
    r"MACE|major adverse cardiac|risk of death",                             # HEART / TIMI outcome percentages
    r"\b0 ?[-–] ?3\b|\b4 ?[-–] ?6\b|(score|scores) of (7|seven)|≥ ?7|0\.9|1\.7 ?%|16\.6|50 ?[-–] ?65",  # HEART bands
    r"45 ?[-–] ?64|\+ ?[12]\b|two points|one point each",                    # HEART age bands / point split (C18)
    r"\b(5|8|13|20|26|41) ?%[^.?;]{0,40}(TIMI|score)|day 14",               # TIMI percentage table
    r"0\.5 ?mm|past (7|seven) days|(2|two) or more episodes",               # TIMI criteria cut-offs
    # ---- D12 dual antiplatelet durations
    r"\b(6|six|12|twelve) months?\b|\b(a|one|full) year\b",
    # ---- D13 deck typos
    r"Forsinopril|Antistreplase|Eluding|suppled|PCTA",
    # ---- brand names on this deck the partition's generic list lacks
    r"Plavix|Brilinta|Effient|Cardizem|Isopt|Coumadin|Capoten|Monopril|Accupril|Lipitor|Crestor",
]

# Stems only: never set a value AT a troponin cut-off (or in the 0.03-0.05 band
# the Principles of Diagnostic Medicine course reads differently).
STEM_BANNED = [
    r"\b0\.0[345]\b",
    r"\b(12|20) ng/L",
]

# Vasospastic angina: slide 91's "T-wave inversion; maybe ST depression" is not
# keyed and not used as a marked-wrong distractor either (D4).
TOPIC_BANNED = {
    T_VSA: [r"T[- ]wave inversion|inverted T", r"ST[- ](segment )?depression"],
}

# (label, trigger regex, required regex, where): "each" = every stem, option and
# explanation that matches the trigger must also match the requirement; "stem" =
# the stem.
LINTS = [
    ("a troponin value names troponin I", r"ng/m?L", r"troponin I\b", "each"),
    ("withholding nitroglycerin in an inferior infarct names the right ventricle",
     r"inferior[^?]{0,240}(nitroglycerin|nitrate)|(nitroglycerin|nitrate)[^?]{0,240}inferior",
     r"right ventric|V4R", "stem"),
]

# Waveform and lead names, like QRS: the ST segment and the augmented limb leads
# are names, not abbreviations. HEART and TIMI are score names (emphasis report
# section 3); they are still written out on first use.
ACRO_OK = r"(?:[Nn]on-)?ST(?:-[a-z]+)*|aVF|aVL|aVR|HEART|TIMI"

# Named findings in vignette stems carry their description in parentheses.
NAMED = {
    "levine": "fist",
    "dressler": "pericarditis",
}

# Content he said WILL be tested, in every form of both sets (stem regex, key
# regex on the keyed option, minimum per form).
REQUIRED = [
    ("troponin (slide 72a)", r"troponin", r".", 1),
    ("right ventricular infarct -> no nitroglycerin", r"right ventric", r"nitroglycerin|nitrate|preload", 1),
]

# Every syllabus disease gets questions in every form; no one topic crowds the
# others. Scored (x60) and asserted per form.
TOPIC_BAND = {
    T_ANAT: (2, 4), T_RISK: (1, 3), T_PRES: (2, 4), T_WORK: (1, 3), T_TROP: (2, 4),
    T_SA: (2, 4), T_UA: (2, 4), T_ECG: (2, 4), T_STEMI: (2, 4), T_REV: (2, 4),
    T_POST: (1, 3), T_VSA: (2, 4), T_MVA: (1, 2),
}
