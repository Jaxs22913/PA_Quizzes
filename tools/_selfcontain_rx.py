#!/usr/bin/env python3
"""The one detector for source attribution in question text.

A question must stand on its own: no reference to the lecture, the deck, the
slides, the syllabus, or the person who taught it.  Imported by the sweep and
by check_self_contained.py so both agree on what counts as a violation.

Its companion is _lecturers.py, which catches a lecturer named by surname alone
("Why did Beck ask...") -- a shape no phrase pattern here can see.
check_self_contained.py and check_pool_cites.py run BOTH as hard failures.

CHANGING A PATTERN. Every consumer runs this: apply_selfcontain.py,
propagate_selfcontain.py, build_propagate_map.py, dump_*.py, and
pdm_l6_partition.py, which ASSERTS its pool has no RX hit -- so a widening can
stop that partition from running. Measure every change over the whole corpus
(live pages, pools, *_sets.json, master-exams*.json, and the frozen Semester 1
pages as a false-positive probe), and re-run pdm_l6_partition.py in a scratch
copy to confirm it still reproduces tools/pdm_l6_sets.json byte for byte.

HISTORY, 2026-09-22 (both directions, measured):
  narrowed   "see/face/watch the speaker" (lip-reading advice) and "the slide
             is/are left" (Gram-stain timing) no longer match. The title
             pattern needs a case-sensitive capitalised name and stops at ONE
             name, so "a professor for clarification" and "Dr. Eugene Stead"
             (PA history) are not citations. That title pattern also WIDENED
             slightly: its name class [A-Z][A-Za-z'-]+ matches "Dr. O'Brien",
             which [A-Z][a-z]+ did not (0 strings affected in the corpus).
  widened    the shapes the old private regex in check_pool_cites.py caught
             and this file did not -- "this slide", "in this course", "the
             material notes/states/asks..." (the relabelling Jaxon rejected),
             "(lecture|deck|material) notes", "course material", "the notes
             start" -- plus the cross-references a student cannot use without
             the course: bare "lecture(s)"/"lecturer(s)" ("from Lecture 2", "in
             the previous lecture"), bare "deck(s)", "syllabus", slides named by
             number, position or title ("slide 17", "the same slide", "the
             review slide lists", "on the risk factor slide"), "examinable
             content/part", "exam material" and "from the recording". Every string they newly flag in Semester 2
             was read and judged a citation; over the frozen Semester 1 pages
             the only non-citation was the option "Lecture-based" (a teaching
             format, in frozen PA-profession content).
"""
import re

SAY = (r"say|says|said|state|states|stated|call|calls|called|name|names|named"
       r"|describe|describes|described|list|lists|listed|give|gives|gave"
       r"|flag|flags|flagged|stress|stresses|stressed|note|notes|noted"
       r"|emphasise|emphasises|emphasised|emphasize|emphasizes|emphasized"
       r"|mark|marks|marked|point|points|pointed|warn|warns|warned"
       r"|specify|specifies|specified|recommend|recommends|recommended"
       r"|prefer|prefers|preferred|teach|teaches|taught|single|singles|singled"
       r"|want|wants|wanted|ask|asks|asked|make|makes|made|treat|treats|treated"
       r"|show|shows|showed|use|uses|used|add|adds|added|put|puts|contrast"
       r"|contrasts|contrasted|define|defines|defined|rank|ranks|ranked"
       r"|cover|covers|covered|include|includes|included|offer|offers|offered"
       r"|argue|argues|argued|indicate|indicates|indicated|raise|raises|raised"
       r"|tie|ties|tied|separate|separates|separated|set|sets|pair|pairs|paired"
       r"|assign|assigns|assigned|draw|draws|drew|link|links|linked"
       r"|place|places|placed|attach|attaches|attached|frame|frames|framed"
       r"|reserve|reserves|reserved|prescribe|prescribes|prescribed")

# Third-person present forms of SAY, for "the material notes / states / asks".
_SAYS = "|".join(w for w in SAY.split("|") if w.endswith("s") and w != "stress")

# "the slide" is also the glass one under a microscope ("flooding the slide with
# crystal violet"), so the lab verbs that precede it are excluded.
_LAB = (r"(?<!flood )(?<!flooding )(?<!warm )(?<!warming )(?<!stain )(?<!staining )"
        r"(?<!heat )(?<!heating )(?<!fix )(?<!fixing )(?<!dry )(?<!drying )"
        r"(?<!mount )(?<!mounting )(?<!prepare )(?<!preparing )(?<!cover )")

# One word of a slide TITLE ("the hepatitis B slide", "the risk factor slide"):
# never an article or preposition, so "from the patient onto a slide" cannot
# pass for a title.
_TITLEWORD = (r"(?!(?:a|an|the|this|that|onto|on|to|into|with|of|in|and|or|is|are|was|were)\b)"
              r"[\w\-]+")
# Lab equipment anywhere in the would-be title: "the Gram-stained slide shows",
# "on the glass slide", "the potassium hydroxide slide".
_LABWORD = (r"(?:[\w\-]+ ){0,2}?(?:glass|microscope|microscopic|potassium|hydroxide|KOH|stained"
            r"|Gram|smear|mount|wet|blood|Tzanck|prepared|specimen|sample|frosted|clean|dry"
            r"|fixed|heat|cover)\b")

PATTERNS = [
    _LAB + r"\bthe (professor|instructor)\b",
    # "Lecture" has no clinical sense in this material: every Semester 2
    # occurrence is the course ("from Lecture 2", "in the previous lecture",
    # "the ear lectures", "per lecture"). The same holds for deck and syllabus.
    r"\blectures?\b",
    r"\blecturers?\b",
    r"\bdecks?\b",
    r"\bsyllab(?:us|i)\b",
    # A microscope slide again, AFTER the noun this time: "How long the slide
    # is left before reading" is Gram-stain / KOH timing (pdm_l3_pool_a), not a
    # citation. Audited false positive, 2026-09-22.
    _LAB + r"\bthe slides?\b(?!\s+(?:is|are)\s+left\b)",
    _LAB + r"\bthis slides?\b",
    # Slides by number, position or title. A bare "slide" is also the glass one
    # ("pressed with a glass slide", "scrape onto a slide", "the potassium
    # hydroxide slide"), so each of these needs a number, a position word, or a
    # slide TITLE that is not lab equipment, followed by a teaching verb or
    # preceded by on/from/in.
    r"\bslides? \d",
    r"\b(?:same|later|earlier|next|previous|preceding|following|final|opening|title|separate"
    r"|summary|review|teaching|highest-yield) slides?\b",
    r"\b(?:that|no|own) slides?\b|\bpair of slides\b|\b(?:is|are|appears?) on a slide\b",
    r"\bthe (?!%s)(?:%s ){1,3}slides?\s+(?:%s)\b" % (_LABWORD, _TITLEWORD, SAY),
    r"\b(?:on|from|in) the (?!%s)(?:%s ){1,3}slides?\b" % (_LABWORD, _TITLEWORD),
    # "Being able to SEE the speaker matters." is hearing-loss advice about
    # lip-reading (inner-ear vignettes, cms_e3l16_vig_a), not a citation.
    # Audited false positive, 2026-09-22. "the speaker notes" still counts.
    _LAB + r"(?<!see )(?<!seeing )(?<!face )(?<!facing )(?<!watch )(?<!watching )"
    r"\bthe speaker\b",
    r"\b(?:speaker|material|lecture|deck|course|class|slide) notes?\b",
    # "the notes" only where it means lecture notes -- a teaching verb, a
    # possessive, or a preposition in front of it.  Bare "the notes" also
    # means the clinical record ("hand the notes to the listener").
    r"\bthe notes['\u2019]",
    r"\bthe notes\s+(?:%s|start|starts|begin|begins)\b" % SAY,
    r"\b(?:in|per|on|from|than|that|what) the notes\b",
    # "The material" alone is clinical ("the material cultured at incision and
    # drainage", "The material described is wax"), so it counts only as the
    # SUBJECT of a present-tense teaching verb: "the material notes / asks".
    r"\bthe (?:course )?material\s+(?:%s)\b" % _SAYS,
    r"\bcourse materials?\b",
    # "this course" only as the course: "the opposite of this course" in a
    # keloid explanation is the disease course, as is "this course of therapy".
    r"\bin this course\b(?!\s+of\b)",
    r"\bthis course\s+(?:%s)\b" % SAY,
    # A title and ONE capitalised name: "Professor Jaquith", "Dr. Rappa's".
    # The name is matched case-SENSITIVELY -- under re.I, "[A-Z][a-z]+" matched
    # any word, so "Asking a professor for clarification" was a hit. And a
    # title followed by a first AND last name is a person being described, not
    # a lecturer being cited: "Dr. Eugene Stead founded the first PA program".
    # Lecturers named in full ("Professor Hugh Rappa") are still caught, by
    # _lecturers.py, which check_self_contained and check_pool_cites also run.
    # Both audited false positives, 2026-09-22.
    r"\b(professor|prof\.?|dr\.?)\s+(?-i:[A-Z][A-Za-z'\u2019\-]+)"
    r"(?![A-Za-z])(?!\s+(?-i:[A-Z][a-z]))",
    r"\bin class\b(?![ -]?\d)",   # not "in class 5" -- steroid potency
    r"\bon the slide\b",
    r"\b(according to|per) the (lecture|deck|slides?|syllabus|professor|notes)\b",
    r"\bcovered in (a |the )?(later|earlier|another) (course|lecture)\b",
    r"\bwas (taught|presented|shown)\b",
    # Exam meta-commentary ("not the examinable part", "examinable content",
    # "rather than exam material") -- but not "the bladder is examinable", which
    # is clinical (frozen PD1 abdominal exam), so a content noun must follow.
    r"\bexaminable (?:content|material|part|point|fact|detail|topic|item)s?\b",
    r"\bexam material\b",
    r"\b(?:from|in|on|per) the recording\b",
]

RX = re.compile("|".join("(?:%s)" % p for p in PATTERNS), re.I)

# Pronoun + teaching verb catches "she flagged", "he said" — but also fires on
# patients ("he covers either eye", "she prefers"), so it feeds a review list
# for a human to judge rather than the pass/fail check.
REVIEW_RX = re.compile(r"\b(she|he|they)\s+(%s)\b" % SAY, re.I)


def review_hits(text):
    return [m.group(0) for m in REVIEW_RX.finditer(text or "")]


def hits(text):
    return [m.group(0) for m in RX.finditer(text or "")]


def flagged(text):
    return bool(RX.search(text or ""))
