#!/usr/bin/env python3
"""Star what Professor Beck emphasised in PD2 Lecture 2 (Dermatology).

Source: the 2026-08-18 recording, 91 minutes across two segments. Ordering was
confirmed from content, not file times -- part 1 ends inside primary morphology
and part 2 opens on secondary morphology.

The find worth the whole exercise is a pair of statements about lesion SIZES.
Beck teaches one centimetre as the macule/patch boundary; Professor Gopal teaches
five millimetres for the same lesions in Clinical Pathophysiology, three hours
earlier on the same day. Both then, independently, told their class not to worry
about borderline cases. Two courses, two conventions, and a student who met both
in one day would reasonably assume one of them was wrong. The guide now says so
outright rather than leaving it to be discovered mid-exam.

Also carries a DE-emphasis, which is worth as much as a star: the shingles-on-the-
nose-tip pearl is explicitly not examinable here, and she said so while telling
the class what is.

The PD1 donor guide predates the professor-emphasis convention, so its CSS has to
come across too -- lifted from build_pharm_guide.py so the convention stays
identical site-wide.

Idempotent.
"""
import io, os, sys

G = "/Users/jaxonluke/Developer/PA_Quizzes/Physical Diagnosis 2 Exam 1/pd2-exam-1-study-guide.html"
PHARM = "/Users/jaxonluke/Developer/PA_Quizzes/tools/build_pharm_guide.py"


def flag(label, body):
    return ('<div class="prof-flag"><span class="prof-flag-label">&#9733; %s</span>\n  %s</div>\n  '
            % (label, body))


MARKS = [
 # (anchor already in the guide, block inserted AFTER it)
 ('<h3 class="sub" id="derm-vocabulary">',
  flag("Professor emphasized",
   '<p><strong>This vocabulary is the backbone, not a glossary to skim.</strong> '
   '<em>&ldquo;This is what&rsquo;s very important &hellip; this is going to be really important for '
   '<u>every system</u> that you learn within physical exam lab and physical exam lectures. These are '
   'going to be the backbone of how you write your notes and how you communicate to other '
   'providers.&rdquo;</em></p>'
   '<p>She is saying this section outlives dermatology &mdash; it is how you will describe findings in '
   'every organ system for the rest of the course.</p>')),

 ('<h3 class="sub" id="derm-primary">',
  flag("Professor emphasized &mdash; and a cross-course warning",
   '<p><strong>Beck uses ONE CENTIMETRE as the macule/patch boundary.</strong> <em>&ldquo;A macule is '
   'less than one centimeter, it is a flat discoloration &mdash; that&rsquo;s important. A patch is '
   'going to be a flat discoloration that&rsquo;s more than one centimeter. Okay? That&rsquo;s '
   'important.&rdquo;</em></p>'
   '<p><strong>Clinical Pathophysiology teaches five millimetres for the same lesions</strong>, and '
   'Professor Gopal said her numbers are the ones her exam uses. Both lectures ran on 2026-08-18, three '
   'hours apart. <u>Neither is wrong &mdash; they are different conventions, and each course examines '
   'its own.</u> Use one centimetre here and five millimetres there.</p>'
   '<p><strong>Neither of them will ask a borderline case.</strong> Beck: <em>&ldquo;My exam question '
   'is not going to involve this &hellip; I&rsquo;m not going to ask you &lsquo;it&rsquo;s point seven '
   'five centimetres&rsquo; &hellip; so it&rsquo;s going to be very clear.&rdquo;</em> Gopal, the same '
   'day: <em>&ldquo;it&rsquo;s not gonna be a gotcha thing on the exam.&rdquo;</em> Learn the ordering '
   'cold; do not lose sleep over the millimetre.</p>')),

 ('<h3 class="sub" id="derm-abnormal">',
  flag("Professor emphasized",
   '<p><strong>The pressure ulcer stages.</strong> <em>&ldquo;These are very important. You&rsquo;re '
   'gonna come across it.&rdquo;</em> She then walked stage one in full &mdash; intact skin, erythema '
   'that fails to blanch, and the four changes: temperature (warmth or coolness), consistency (firm or '
   'boggy), sensation (pain or itching), and colour.</p>'
   '<p><strong>The melanoma letters.</strong> <em>&ldquo;Things to look out for and to remember &hellip; '
   'you wanna remember the A, B, C, Ds &hellip; that&rsquo;s really important.&rdquo;</em> She stopped '
   'and taught them from scratch when the class had not met them before.</p>')),

 ('<h3 class="sub" id="derm-hairnails">',
  flag("Professor emphasized",
   '<p><strong>Exclamation point hairs in alopecia areata.</strong> <em>&ldquo;Hair loss in multiple '
   'round patchy areas, and this is important &mdash; you&rsquo;ll see exclamation point hairs. Those '
   'are like a few follicles that are still trying &hellip; that should trigger in your mind, oh okay, '
   'alopecia areata, we gotta jump on this.&rdquo;</em></p>')),

 ('<h3 class="sub" id="derm-technique">',
  flag("Professor said you do NOT need this",
   '<p><strong>Clinical pearls are context, not exam material.</strong> After explaining that shingles '
   'on the tip of the nose is a medical emergency because that dermatome carries the optic nerve, she '
   'drew the line explicitly: <em>&ldquo;I&rsquo;m not going to test you on that &mdash; the testing is '
   'on <u>this kind of stuff</u> &mdash; but I&rsquo;m just trying to give you the clinical '
   'level.&rdquo;</em></p>'
   '<p>&ldquo;This kind of stuff&rdquo; is the descriptive terminology and the examination itself. She '
   'added the pearl is worth knowing anyway because she believes it recurs on board exams &mdash; so '
   'learn it for practice, not for this exam.</p>')),
]


def main():
    s = io.open(G, encoding="utf-8").read()
    if "prof-flag-label" in s:
        print("marks already present — nothing to do")
        return 0

    # bring the emphasis CSS across from the pharm builder
    src = io.open(PHARM, encoding="utf-8").read()
    i = src.index("PROF_CSS = '''"); j = src.index("'''", i + 14)
    css = src[i + 14:j]
    # PROF_CSS was written to CLOSE a style block, so it ends with its own
    # </style>. Inserting it before an existing one produced a duplicate
    # closing tag and an unbalanced document.
    css = css.replace("</style>", "")
    assert "</style>" in s
    k = s.rfind("</style>")
    s = s[:k] + css + s[k:]

    added = 0
    for anchor, block in MARKS:
        assert s.count(anchor) == 1, "anchor %r appears %d times" % (anchor, s.count(anchor))
        # land the block AFTER the whole heading line, not before it
        h = s.index(anchor)
        h = s.index("</h3>", h) + len("</h3>")
        s = s[:h] + "\n  " + block + s[h:]
        added += 1

    io.open(G, "w", encoding="utf-8").write(s)
    print("applied %d marks; guide now has %d boxed blocks" % (added, s.count('class="prof-flag"')))
    return 0


if __name__ == "__main__":
    sys.exit(main())
