#!/usr/bin/env python3
"""The one detector for a question that names the person who taught it.

_selfcontain_rx.RX catches "Professor Jaquith" and "the lecture", but a bare
surname slips straight past it: "Why did Beck ask the class to know the
referral list?" and "Webster tied presbyopia to a letter in an examination
mnemonic." both shipped on pages the site checker reported clean (audit of
2026-09-22). This module is the surname half of the self-contained rule, and
check_self_contained.py and check_pool_cites.py both import it, so the page
check and the pre-render pool check cannot disagree about what a lecturer
citation is.

    from _lecturers import lecturer_hits
    lecturer_hits("Why did Beck ask the class ...")  ->  [("surname", "Beck")]

WHERE THE NAMES COME FROM, measured 2026-09-22:

  calendar-data.js  every lecture row ends in the lecturer: Dr. Fair, Dr. Rappa,
                    Dr. Webster, Dr. Wood, Dr. Jaquith, Professor Reynolds,
                    Professor Shah, Prof. Finck, Professor Griffenkranz,
                    Professor Elwaya.  Read LIVE at import, so a new lecturer
                    added to the calendar is detected without editing this file
                    (and is reported by unclassified_calendar_names()).
  deck title slides lecturers the calendar never names: Valerie Beck (PD2 derm
                    and ocular; CMS chronic vision loss), Stacie Gopal (Clin
                    Path dermatology and vascular; PDM urinalysis), Matthew Ward
                    (Clin Path cardiac), Rob Gray (PD2 ENT presenter; "adopted
                    from Robert Gray" on the CMS ophthalmology deck), Katelyn
                    Kelley ("adopted from" on the CMS fungal/viral deck), and
                    Bill Webster (the Clin Path guest -- a different person from
                    the Microbiology Dr. Webster, same surname, same detector).
  lecturer_profiles / pharmacology_exam_spec   Dr. McInnis (Pharmacology).

THREE STRENGTHS OF MATCH, because some of these surnames are ordinary words:

  title      Dr./Doctor/Prof./Professor/Mr./Ms./Mrs. + (first name) + surname.
             Always a hit, for every lecturer.
  fullname   first name + surname ("Adam Wood", "Hugh G. Rappa").  Always a hit.
  surname    the bare capitalised surname.  Only for DISTINCTIVE names -- nobody
             writes "Jaquith" or "Rappa" about anything else.
  context    an ORDINARY-WORD surname (Fair, Wood, Ward, Gray) counts only when
             a teaching verb or a lecture noun follows it: "Wood says", "Fair's
             slides".  Bare, they are clinical words here: 248 "Wood's lamp" /
             "Wood lamp", 8 "Fair-skinned", 13 "Gray" (the grey-top blood tube)
             and 17 "Grey baby syndrome / grey discolouration" in the Semester 2
             question banks -- every one of them clinical, none a citation.

CLINICAL EPONYMS ARE EXEMPT, NARROWLY -- only the named sign, scale or book,
never the bare surname (the list, with where each was found, is at EPONYMS):
Reynolds' pentad / number / Risk Score, Beck's triad and the Beck inventories,
Kelley's Textbook, Webster's Dictionary, and any hyphenated compound
(Shah-Waardenburg, Merriam-Webster).  Wood's lamp needs no exemption because
Wood is an ordinary-word surname and "lamp" is not a teaching word.

A TITLE ALWAYS COUNTS, Mr./Ms./Mrs. included. "Mrs. Shah" or "Mr. Ward" as a
vignette patient is flagged on purpose: a student who sat the course reads it
as the lecturer, so rename the patient (0 such patients in the banks,
2026-09-22).
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# surname -> (first names, ordinary English word?, where it was verified)
LECTURERS = {
    "Reynolds":     (("Lauren",),          False, "calendar; CMS/PDM/Clin Path/PD2 decks"),
    "Jaquith":      (("Monique",),         False, "calendar; CMS decks"),
    "Shah":         (("Chand",),           False, "calendar; CMS/PDM decks"),
    "Griffenkranz": (("Hugh",),            False, "calendar; CMS decks"),
    "Rappa":        (("Hugh",),            False, "calendar; Clin Path L3 deck"),
    "Webster":      (("Bill",),            False, "calendar (Micro); Clin Path L4/L5 decks (guest)"),
    "Finck":        (("Megan",),           False, "calendar; Med Lit decks; PD2 ENT deck author"),
    "Elwaya":       (("Ayelet",),          False, "calendar; PD2 L1 and PDM L7/L8 decks"),
    "Beck":         (("Valerie",),         False, "PD2 derm/ocular decks; CMS chronic vision loss deck"),
    "Gopal":        (("Stacie",),          False, "Clin Path L2/vascular and PDM L6 decks"),
    "McInnis":      ((),                   False, "pharmacology_exam_spec memory"),
    "Kelley":       (("Katelyn",),         False, "CMS fungal/viral deck ('adopted from')"),
    "Fair":         ((),                   True,  "calendar (Micro)"),
    "Wood":         (("Adam",),            True,  "calendar; Pharmacology decks"),
    "Ward":         (("Matthew",),         True,  "Clin Path L6 cardiac deck"),
    "Gray":         (("Rob", "Robert"),    True,  "PD2 ENT deck presenter; CMS ophtho deck"),
}

# Named clinical signs, scales and books that carry a lecturer's surname.
# Negative lookaheads, applied right after the surname -- they exempt the named
# thing, never the bare name. Each was found in a deck or probed, 2026-09-22:
#   Reynolds  pentad (cholangitis), number (flow), Risk Score -- "Reynolds Risk
#             Score for CVD" is on slide 21 of the PDM Exam 2 deck svCardiac
#             Biomarkers and Lipids.pptx, the one false positive among all 58
#             Semester 2 decks, and flagging it would push a builder to reword
#             the deck's own term.
#   Beck      triad (tamponade); the Beck Depression / Anxiety / Hopelessness /
#             Suicide Ideation / Youth inventories and scales.
#   Kelley    Kelley's Textbook of Rheumatology; "Kelley and Firestein".
#   Webster   Webster's Dictionary / Webster's Third.
# Hyphenated compounds need no entry: "Shah-Waardenburg syndrome" and
# "Merriam-Webster" are exempted for every surname by _COMPOUND below.
EPONYMS = {
    "Reynolds": r"(?!(?i:['’]?s?\s+(?:pentad|number|risk\s+score)\b))",
    "Beck":     r"(?!(?i:['’]?s?\s+triad\b"
                r"|['’]?s?\s+(?:Depression|Anxiety|Hopelessness|Suicid\w*|Youth)\b))",
    "Kelley":   r"(?!(?i:['’]s\s+Textbook\b|\s+and\s+Firestein\b))",
    "Webster":  r"(?!(?i:['’]s\s+(?:New\s+)?(?:Dictionary|Third)\b))",
}

# A surname fused to another capitalised name by a hyphen is an eponym, not a
# person: Shah-Waardenburg, Merriam-Webster. ("Wood-type lesion" is lower-case
# after the hyphen and is not exempted by this.)
_COMPOUND_BEFORE = r"(?<![A-Za-z][\-‐‑])"
_COMPOUND_AFTER = r"(?![\-‐‑][A-Z])"

TITLE = r"(?i:\b(?:Dr|Doctor|Prof|Professor|Mr|Ms|Mrs)\b\.?)"
FIRST = r"(?:[A-Z][a-z]+\s+)?(?:[A-Z]\.\s*)?"           # "Hugh G. " / "Adam "

# Teaching verbs (the same list the site detector uses) and lecture nouns, for
# the ordinary-word surnames that need context to count.
from _selfcontain_rx import SAY  # noqa: E402

LECTURE_NOUN = r"(?:lecture|lectures|deck|decks|slide|slides|notes|class|talk|review|handout)"


def calendar_surnames(path=None):
    """Surnames the academic calendar attaches to a title, e.g. 'Dr. Fair'."""
    path = path or os.path.join(ROOT, "calendar-data.js")
    try:
        text = open(path, encoding="utf-8").read()
    except OSError:
        return set()
    names = set()
    for title in re.findall(r't:"([^"]*)"', text):
        for m in re.finditer(r"\b(?:Dr\.?|Professor|Prof\.)\s+([A-Z][A-Za-z'\-]+)", title):
            names.add(m.group(1))
    return names


def unclassified_calendar_names():
    """Calendar lecturers missing from LECTURERS. They are still detected (as
    title-or-context only, the safe default), but someone should classify them
    here -- print this list rather than let it go stale silently."""
    return sorted(calendar_surnames() - set(LECTURERS))


def _build():
    table = dict(LECTURERS)
    for extra in unclassified_calendar_names():
        table[extra] = ((), True, "calendar-data.js (unclassified)")
    pats = []
    for sur, (firsts, ordinary, _src) in sorted(table.items()):
        s = "%s(?P<s>%s)" % (_COMPOUND_BEFORE, re.escape(sur))
        tail = _COMPOUND_AFTER + EPONYMS.get(sur, "")
        pats.append(("title", sur, r"%s\s+%s%s\b%s" % (TITLE, FIRST, s, tail)))
        if firsts:
            fn = "|".join(map(re.escape, firsts))
            pats.append(("fullname", sur, r"\b(?:%s)\s+(?:[A-Z]\.\s*)?%s\b%s" % (fn, s, tail)))
        if ordinary:
            pats.append(("context", sur,
                         r"\b%s(?:\s+(?:%s)\b|['’]s\s+(?:own\s+)?%s\b)" % (s, SAY, LECTURE_NOUN)))
        else:
            pats.append(("surname", sur, r"\b%s\b%s" % (s, tail)))
    return [(kind, sur, re.compile(p)) for kind, sur, p in pats]


PATTERNS = _build()
KINDS = ("title", "fullname", "surname", "context")


def lecturer_spans(text):
    """-> [(kind, matched text, start, end)], one per surname occurrence, the
    strongest kind winning when several patterns see the same surname."""
    text = text or ""
    spans = {}
    for kind, _sur, rx in PATTERNS:
        for m in rx.finditer(text):
            key = m.start("s")                  # the surname itself: dedupe kinds
            if key not in spans or KINDS.index(kind) < KINDS.index(spans[key][0]):
                spans[key] = (kind, m.group(0), m.start(), m.end())
    return [spans[k] for k in sorted(spans)]


def lecturer_hits(text):
    """-> [(kind, matched text)]."""
    return [(k, f) for k, f, _s, _e in lecturer_spans(text)]


def flagged(text):
    return bool(lecturer_spans(text))


def citation_hits(text):
    """Everything the self-contained rule looks for in one string, as
    [(severity, detector, fragment)] -- the single definition that
    check_self_contained.py and check_pool_cites.py both use.

      hard    "rx"                 _selfcontain_rx.RX
      hard    "lecturer:<kind>"    a lecturer named here, unless RX already
                                   covers that text ("Professor Rappa" is one
                                   citation, not two)
      review  "review"             REVIEW_RX, pronoun + teaching verb
    """
    from _selfcontain_rx import RX, REVIEW_RX
    text = text or ""
    out, taken = [], []
    for m in RX.finditer(text):
        out.append(("hard", "rx", m.group(0)))
        taken.append((m.start(), m.end()))
    for kind, frag, s, e in lecturer_spans(text):
        if not any(s < te and ts < e for ts, te in taken):
            out.append(("hard", "lecturer:" + kind, frag))
    out += [("review", "review", m.group(0)) for m in REVIEW_RX.finditer(text)]
    return out


if __name__ == "__main__":
    import sys
    print("lecturers:", ", ".join(sorted(LECTURERS)))
    print("calendar surnames:", ", ".join(sorted(calendar_surnames())) or "NONE -- calendar-data.js unreadable")
    missing = unclassified_calendar_names()
    if missing:
        print("UNCLASSIFIED calendar lecturers (detected as title/context only):", ", ".join(missing))
    for arg in sys.argv[1:]:
        print(repr(arg), "->", lecturer_hits(arg))
