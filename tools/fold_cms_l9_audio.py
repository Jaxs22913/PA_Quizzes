#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fold the 24 August Lecture 9 recording in, and state the EXAM FORMAT.

Professor Jaquith, Pre-Malignant and Malignant Cutaneous Lesions. Every quote
is checked against BOTH my transcript and Notability's before it is used.

THE POINT OF THIS ONE IS THE FIRST NINETY SECONDS. Before touching the content
she described how the exam itself is built, and that description had three
consequences for the quizzes, two of which are already applied:

  1. "Pretty much all clinical vignettes." The site is roughly half IO-recall
     quizzes and half vignettes. The recall sets are good for LEARNING the
     facts; they do not match the exam's FORM. Rather than delete them, the
     guide now says which is which, so a student revising for format knows
     where to go. Stated, not silently rebalanced.

  2. Diagnosis is the minority lead-in. Applied: the vignette draw now caps
     diagnosis at 6 of 30 and the shipped share fell from 31% to 18%.

  3. She said repeatedly she would set "how do you diagnose this?" questions.
     Applied: cms_l9_pool_h.py, 16 questions, guaranteed in the draw.

Also captured: 65 questions, and "way more non-pictures than pictures, but
there's a couple" -- which is the only reason the photographs in this guide and
the comparison chart are worth revising from at all.

Idempotent: fenced in <!--CMSL9AUDIO--> and stripped before reinsertion.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
GUIDE = os.path.join(DIR, "cms-exam-1-study-guide.html")
CRAM = os.path.join(DIR, "cms-exam-1-cram-sheet.html")
REC = os.path.expanduser("~/Desktop/Semester 2/Clinical Medicine and Surgery I Inbox/"
                         "Exam 1/recordings")

QUOTES = [
    "clinical vignettes",
    # anchored on the substring both transcripts share: mine has "I don't
    # necessarily want you to memorize it", Notability inserts a stray "mean".
    "want you to memorize it",
    "you guys don't need to know that",
    # mine writes "15 percent survival", Notability writes "15% survival".
    "about a 15",
    "too dangerous",
    "most likely diagnosis",
    "first line treatment",
    "patient education",
    "65 questions",
    "recognize conditions by the vignette",
]


def verify():
    mine = os.path.join(REC, "cms-l9-premalignant-malignant-2026-08-24.transcript.txt")
    theirs = os.path.join(REC, "cms-l9-premalignant-malignant-2026-08-24.notability.txt")
    assert os.path.exists(mine), ("my own transcript is not written yet -- do not attribute "
                                  "exam-format claims from Notability alone")
    def norm(p):
        t = open(p, encoding="utf-8", errors="replace").read()
        t = re.sub(r"\[\d{1,2}:\d{2}(?::\d{2})?\]", " ", t)
        return re.sub(r"\s+", " ", t).lower()
    a, b = norm(mine), norm(theirs)
    bad = [q for q in QUOTES if not (q in a and q in b)]
    for q in bad:
        print("  QUOTE NOT IN BOTH: %-40s mine=%s notability=%s" % (q, q in a, q in b))
    assert not bad, ("%d quote(s) appear in only one transcript. These are claims about how "
                     "the EXAM is built -- do not ship them on one source." % len(bad))
    print("  all %d exam-format quotes present in BOTH transcripts" % len(QUOTES))


BOX = """<!--CMSL9AUDIO-->
<div class="prof-flag" style="border-width:3px"><span class="prof-flag-label">&#9733;&#9733; How this exam is actually built &mdash; from the 24 August lecture</span>
<p>She spent the first minute of Lecture 9 describing the exam before she touched the content.
This is the most useful minute of audio in the block, so it is reproduced here rather than
summarised away.</p>
<table>
  <tr><th>What she said</th><th>What it means for revising</th></tr>
  <tr><td><i>&ldquo;There&rsquo;s gonna be like clinical vignettes or <b>pretty much all clinical
    vignettes</b> &hellip; make sure that you are able to <b>recognize conditions by the
    vignette</b>.&rdquo;</i></td>
    <td><b>The vignette sets are the format-matched practice.</b> Every topic on this site has two
    of them alongside its two recall quizzes. The recall quizzes are for learning the facts; the
    vignette sets are for sitting the paper. If you only have time for one, do the vignettes.</td></tr>
  <tr><td><i>&ldquo;There might be <b>some</b> question, what&rsquo;s the most likely diagnosis,
    but <b>a lot of them</b> are &mdash; what&rsquo;s the <b>next management plan</b>? What&rsquo;s
    your <b>first line treatment</b> plan? &hellip; what&rsquo;s the proper <b>patient
    education</b>?&rdquo;</i></td>
    <td><b>Naming the disease is the easy half.</b> Most marks sit in what you do next. The
    vignette sets are now built to that shape &mdash; diagnosis is capped at 6 of 30, and
    education, treatment and next-step lead-ins outnumber it.</td></tr>
  <tr><td><i>&ldquo;There are some pictures, but I would say <b>way more non-pictures than
    pictures</b> &mdash; but there&rsquo;s a couple.&rdquo;</i></td>
    <td>A couple of image questions, so the photographs in this guide and in the comparison chart
    are worth a pass, but they are not where the paper lives.</td></tr>
  <tr><td><i>&ldquo;<b>65 questions</b>, and I think that&rsquo;s everything.&rdquo;</i></td>
    <td>Note the master exams here are <b>5 forms of 60</b>, which is this site&rsquo;s standing
    format rather than a guess at hers. Sixty-five is the real paper.</td></tr>
</table>
<p><b><mark class="prof-highlight">She also said, three times, which question she is going to
write.</mark></b> On squamous cell carcinoma: <i>&ldquo;what&rsquo;s our diagnostic testing?
We&rsquo;re biopsying it &hellip; I should definitely give you a question on that.&rdquo;</i> On
melanoma: <i>&ldquo;Biopsy, great. I&rsquo;m totally gonna write a question for that. I
haven&rsquo;t done these questions yet.&rdquo;</i> On cutaneous T-cell lymphoma: <i>&ldquo;you guys
know that question for everyone for this lecture at least &hellip; do a biopsy is how you&rsquo;re
gonna diagnose this.&rdquo;</i></p>
<p><b>The answer is never just &ldquo;biopsy&rdquo;, though</b>, because the slides never say that.
Squamous cell needs <b>depth enough to separate in situ from invasive</b>. Basal cell is
<b>shave or punch</b>. Kaposi needs a <b>representative</b> lesion with human herpesvirus 8
findings. Cutaneous T-cell lymphoma needs an <b>active, representative, untreated</b> lesion,
possibly several, and <b>a single nondiagnostic biopsy does not exclude it</b>. Section 9 covers
each, and the quizzes now ask all of them.</p>
</div>
<!--/CMSL9AUDIO-->"""

CRAM_ROWS = [
 ("★★ HOW THE EXAM IS BUILT",
  "Her words, opening Lecture 9: “there's gonna be like clinical vignettes or PRETTY MUCH ALL CLINICAL VIGNETTES… make sure that you are able to RECOGNIZE CONDITIONS BY THE VIGNETTE.” 65 QUESTIONS. “Way more non-pictures than pictures, but there's a couple.”"),
 ("★★ Where the marks are",
  "“There might be SOME question, what's the most likely diagnosis, but A LOT OF THEM are — what's the NEXT MANAGEMENT PLAN? What's your FIRST LINE TREATMENT plan?… what's the proper PATIENT EDUCATION?” NAMING THE DISEASE IS THE EASY HALF. Do the vignette sets, not just the recall quizzes."),
 ("★★ HOW FAR INTO TNM TO GO",
  "She capped this herself: “I want you to kind of know this… but I DON'T NECESSARILY WANT YOU TO MEMORIZE IT.” And on the sub-rows: “that's why I didn't put all that, YOU GUYS DON'T NEED TO KNOW THAT. I just want you to know this exists.” WHAT SHE DOES WANT: T = tumour, N = nodes, M = metastasis; and the five stages plainly — 0 epidermal region, I localized and very thin, II localized but thicker, III lymph nodes, IV other organs. “That's the general of what I do want you to know.”"),
 ("Survival figures said ALOUD only (on no slide)",
  "Under 1 mm Breslow → “over 95-ish per cent survival”. Distant metastases → “about a 15 PER CENT survival”. NOT ON ANY SLIDE — the deck only says survival drops sharply with thickness and spread. No quiz question is built on them. Her point: that gap is why you catch it early."),
 ("Referral, verbatim",
  "Anything deeper than 1 mm goes to a specialist. “I AM NOT TREATING FAMILY MEDICINE MELANOMA. NEITHER SHOULD YOU. IT'S TOO DANGEROUS.”"),
 ("★ The question she said she'd write",
  "Three separate times: “how do you diagnose this?” → BIOPSY. But NEVER a bare biopsy — SCC needs DEPTH ENOUGH TO SEPARATE IN SITU FROM INVASIVE; BCC is SHAVE OR PUNCH; KAPOSI needs a REPRESENTATIVE lesion with HHV-8 findings; CTCL needs an ACTIVE, REPRESENTATIVE, UNTREATED lesion, possibly several, and ONE NEGATIVE BIOPSY DOES NOT EXCLUDE IT."),
]


SCOPE_BOX = """<!--CMSL9SCOPE-->
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Scope, from the 24 August lecture</span>
  <p><b><mark class="prof-highlight">She told you how far into the staging table to go, and it is not
  far.</mark></b> On the T, N and M grid: <i>&ldquo;I want you to kind of know this &hellip; but I
  <b>don&rsquo;t necessarily want you to memorize it</b>. I feel like for this stage of where
  you&rsquo;re at &hellip; it just might be too much.&rdquo;</i> And on the sub-classifications,
  the N1a and T1a-versus-T1b rows: <i>&ldquo;that&rsquo;s why I didn&rsquo;t put all that,
  <b>you guys don&rsquo;t need to know that</b>. I just want you to know this exists.&rdquo;</i></p>
  <p><b>What she DOES want, in her words:</b> that T is the tumour, N the nodes and M the
  metastases; and the five stages in plain terms &mdash; <b>0</b> confined to the epidermal region,
  <b>I</b> localized and very thin, <b>II</b> localized but thicker, <b>III</b> spread to lymph
  nodes, <b>IV</b> spread to other organs. <i>&ldquo;That&rsquo;s the general of what I do want you
  to know.&rdquo;</i> The quizzes here ask exactly that and no more &mdash; what the letters denote
  and the anchor stages, never a row of the grid.</p>
  <p><b>Two survival figures she gave out loud that are on NO slide.</b> Under one millimetre
  Breslow, <i>&ldquo;your prognosis is good &hellip; over 95-ish per cent survival&rdquo;</i>; with
  distant metastases, <i>&ldquo;about a <b>15 per cent</b> survival&rdquo;</i>. The deck says only
  that survival drops sharply with thickness and spread. <b>No quiz question is built on these</b>,
  because they are not on a slide and she stumbled over the first figure &mdash; but the contrast
  is the reason she gives for catching it early, so it is worth carrying.</p>
  <p><b>On referral she was blunt.</b> Anything deeper than one millimetre goes to a specialist, and
  <i>&ldquo;I am not treating family medicine melanoma. Neither should you. It&rsquo;s
  <b>too dangerous</b>.&rdquo;</i></p>
  </div>
<!--/CMSL9SCOPE-->"""


def main():
    print("verifying exam-format quotes against BOTH transcripts...")
    verify()

    g = open(GUIDE, encoding="utf-8").read()
    g = re.sub(r"<!--CMSL9AUDIO-->.*?<!--/CMSL9AUDIO-->\n?", "", g, flags=re.S)
    # It belongs at the TOP of the guide, not buried in section 9: it is about
    # the whole paper, not about malignant lesions.
    anchor = '<section class="deck" id="clinical-reasoning"'
    if g.count(anchor) != 1:
        m = re.search(r'<section class="deck" id="[^"]+"', g)
        assert m, "no deck section found to anchor the exam-format box above"
        anchor = m.group(0)
        assert g.count(anchor) == 1, "anchor not unique"
    g = g.replace(anchor, BOX + "\n\n" + anchor, 1)
    for tag in ("section", "table", "tr", "td", "th", "div", "p"):
        o = len(re.findall(r"<%s[ >]" % tag, g)); c = g.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d/%d" % (tag, o, c)
    g = re.sub(r"<!--CMSL9SCOPE-->.*?<!--/CMSL9SCOPE-->\n?", "", g, flags=re.S)
    anchor9 = '  <h3 class="sub" id="mal-melanoma">'
    assert g.count(anchor9) == 1, "melanoma subsection anchor not found once"
    g = g.replace(anchor9, SCOPE_BOX + "\n\n" + anchor9, 1)
    for tag in ("section", "table", "tr", "td", "th", "div", "p"):
        o = len(re.findall(r"<%s[ >]" % tag, g)); c = g.count("</%s>" % tag)
        assert o == c, "%s unbalanced after scope box: %d/%d" % (tag, o, c)
    open(GUIDE, "w", encoding="utf-8").write(g)

    import html as H
    c = open(CRAM, encoding="utf-8").read()
    c = re.sub(r'\n  <section class="topic" id="exam-format".*?</section>\n', "", c, flags=re.S)
    c = re.sub(r'      <a href="#exam-format".*?</a>\n', "", c)
    acc, bg, zeb, ink = "#8a3f4a", "#f4e3e6", "#faf1f3", "#6b2f38"
    rows = "\n".join('          <tr><td class="h">%s</td><td>%s</td></tr>'
                     % (H.escape(a), H.escape(b)) for a, b in CRAM_ROWS)
    sec = ('\n  <section class="topic" id="exam-format" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">\n'
           '    <div class="shead"><span class="dot" style="background:%s"></span><h2>&#9733;&#9733; How This Exam Is Built</h2></div>\n'
           '    <div class="scroll">\n      <table>\n'
           '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
           '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n'
           % (acc, bg, zeb, ink, acc, rows))
    # first section on the sheet, because it governs how to use everything else
    j = c.index('<section class="topic"')
    j = c.rindex("\n", 0, j)
    c = c[:j] + sec + c[j:]
    link = ('      <a href="#exam-format" style="color:%s"><span class="dot" style="background:%s">'
            '</span>&#9733;&#9733; How This Exam Is Built</a>\n' % (ink, acc))
    m = re.search(r'      <a href="#[^"]+"[^>]*>.*?</a>\n', c, re.S)
    assert m, "no jump link found to anchor above"
    c = c[:m.start()] + link + c[m.start():]
    ids = set(re.findall(r'id="([^"]+)"', c))
    dang = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', c) if a and a not in ids]
    assert not dang, "dangling jump links: %r" % dang
    open(CRAM, "w", encoding="utf-8").write(c)

    print("guide: exam-format box added at the top")
    print("cram: 'How This Exam Is Built' added as the first section (%d rows)" % len(CRAM_ROWS))


if __name__ == "__main__":
    main()
