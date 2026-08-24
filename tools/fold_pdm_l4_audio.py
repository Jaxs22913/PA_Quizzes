#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fold the 24 August Lecture 4 recording into the PDM I guide, cram and quizzes.

Professor Shah, 63 minutes, two segments. Cross-examined against Notability's
independent transcript before anything here was written -- neither transcript
can be keyword-searched reliably for medical vocabulary, so both get read.

WHAT THE RECORDING CHANGED, and it is more than usual:

1. THE THREE "CONTRADICTORY" REFERENCE RANGES ARE NOT AN ERROR IN THE DECK.
   She teaches ranges as approximate and lab-dependent, repeatedly and by
   design: "54 to 62 PLUS OR MINUS A FEW, depending on what lab you're in ...
   it doesn't matter what the range is, it just matters what the range is for
   where you're working." That reframes the whole warning box, which had
   presented the disagreement as something to be careful of rather than as her
   actual position.

2. SHE USED 150,000-450,000 FOR PLATELETS -- the teaching-slide figure, not the
   reference table's 400,000 -- and singled it out as the one that does NOT vary:
   "this one I have not seen be very different from lab to lab."

3. THE NEUTROPENIA TABLE ONLY APPLIES BELOW 1,500. Asked directly about the
   worked example, she answered that the chart "is only for those individuals
   who have an ANC of less than 1500 ... we know that the 2700 is more than
   1500, we know that the patient is not neutropenic." Nothing on the slide
   says this, and without it a student may try to grade a normal count.

4. THE CALCULATION IS EXPLICITLY REQUIRED: apps and the electronic record will
   compute it, "however, EVERYONE NEEDS TO KNOW HOW TO CALCULATE THAT." That
   confirms the inverse guard in pdm_l4_partition.py was right to demand the
   worked examples exist.

5. SHE DE-EMPHASISED THE DEEP BRANCHES OF THE ANEMIA ALGORITHM, twice. On the
   microcytic arm: "for now, I'm happy if you understand genetic versus
   non-genetic; the rest of the stuff will come later." On the normocytic arm:
   "all of this will come [with heme] -- if you can just focus on this first
   part here, that will be beneficial for you." The content stays in the guide
   because it is on the slides, but the emphasis box now says where she put the
   line.

Idempotent: the blocks it writes are fenced, and re-running replaces them.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1")
GUIDE = os.path.join(DIR, "pdm-exam-1-study-guide.html")
CRAM = os.path.join(DIR, "pdm-exam-1-cram-sheet.html")
REC = os.path.expanduser("~/Desktop/Semester 2/Principles of Diagnostic Medicine I Inbox/"
                         "Exam 1/recordings")

# Every quote below is checked against BOTH transcripts before it is written.
# Notability garbles medical vocabulary and faster-whisper garbles different
# words, so a quote surviving in both is a quote that was actually said.
QUOTES = [
    "everyone needs to know how to calculate",
    "it doesn't matter what the range is",
    "plus or minus a few",
    "focus on this first part",
    "happy if you understand",
    "chart is only for those individuals",
    "not seen be very different from lab to lab",
]


def verify_quotes():
    mine = os.path.join(REC, "pdm-l4-cbc-hematology-2026-08-24.transcript.txt")
    theirs = os.path.join(REC, "pdm-l4-cbc-hematology-2026-08-24.notability.txt")
    assert os.path.exists(mine), ("my own transcript is not written yet -- do not fold in "
                                  "quotes from Notability alone")
    def norm(p):
        t = open(p, encoding="utf-8", errors="replace").read()
        # STRIP THE TIMESTAMP MARKERS FIRST. My transcripts interleave [MM:SS]
        # every couple of seconds and Notability's do not, so a quote spanning
        # one -- "not seen be very different [26:19] from lab to lab" -- failed
        # to match even though both transcripts plainly contain it. That is a
        # defect in the comparison, not evidence the quote was not said, and
        # loosening the guard instead of fixing the normaliser would have been
        # the wrong repair.
        t = re.sub(r"\[\d{1,2}:\d{2}(?::\d{2})?\]", " ", t)
        return re.sub(r"\s+", " ", t).lower()
    a, b = norm(mine), norm(theirs)
    both, only = [], []
    for q in QUOTES:
        ql = q.lower()
        inA, inB = ql in a, ql in b
        (both if (inA and inB) else only).append((q, inA, inB))
    for q, inA, inB in only:
        print("  QUOTE NOT IN BOTH: %-46s mine=%s notability=%s" % (q[:46], inA, inB))
    assert not only, ("%d quote(s) appear in only one transcript -- verify by ear before "
                      "attributing them" % len(only))
    print("  all %d quotes present in BOTH transcripts" % len(both))


GUIDE_BOX = """<!--PDML4AUDIO-->
  <div class="prof-flag"><span class="prof-flag-label">&#9733; From the 24 August lecture</span>
  <p><b><mark class="prof-highlight">The reference ranges are meant to be approximate.</mark></b>
  This is the thing the recording changes most. The three ranges that differ between the deck's
  reference table and its teaching slides are not a mistake to be resolved &mdash; she teaches them
  as lab-dependent on purpose. On neutrophils: <i>&ldquo;54 to 62 <b>plus or minus a few</b>,
  depending on what lab you're in &hellip; I've probably seen so many different ranges throughout,
  and <b>it doesn&rsquo;t matter what the range is, it just matters what the range is for where
  you&rsquo;re working.</b>&rdquo;</i> Learn the approximate figure and the direction of
  abnormality, not the decimal.</p>
  <p><b>The one range she says does NOT vary is the platelet count.</b> She used
  <b>150,000&ndash;450,000</b> &mdash; the teaching-slide figure &mdash; and added
  <i>&ldquo;this one I have <b>not seen be very different from lab to lab</b>. This one&rsquo;s
  been pretty consistently the same.&rdquo;</i></p>
  <p><b>The absolute neutrophil count calculation is explicitly required.</b> Apps and the
  electronic record will do it for you, <i>&ldquo;however, <b>everyone needs to know how to
  calculate that</b>.&rdquo;</i> There are two formulas, and which you use depends only on whether
  the white cell count is written in whole numbers or in thousands.</p>
  <p><b><mark class="prof-highlight">The neutropenia table only applies below 1,500.</mark></b>
  Asked directly whether the worked example's answer of 2,700 could be graded on it, she said the
  <i>&ldquo;<b>chart is only for those individuals</b> who have an [absolute neutrophil count] of
  less than 1500. Because we know that the 2700 is more than 1500, we know that the patient is not
  neutropenic.&rdquo;</i> Nothing on the slide says that. Calculate first, then decide whether the
  table applies at all.</p>
  <p><b>She drew a line around the anemia algorithm &mdash; twice.</b> On the microcytic arm:
  <i>&ldquo;for now, I&rsquo;m <b>happy if you understand</b> genetic versus non-genetic; the rest
  of the stuff will come later.&rdquo;</i> On the normocytic arm: <i>&ldquo;all of this will come
  [with heme] &mdash; if you can just <b>focus on this first part</b> here, that will be beneficial
  for you.&rdquo;</i> The full algorithm stays below because it is on the slides, but that is where
  she put the emphasis.</p>
  <p><b>Two practical habits she offered.</b> Read hemoglobin, multiply by three, and check the
  hematocrit lands in the same vicinity. And on ordering: the <b>first</b> time you meet a patient
  and work them up, order <b>with</b> differential; afterwards, for monitoring a known problem,
  <b>without</b> is enough. Her one-liner on the panel itself: <i>&ldquo;if we don&rsquo;t know what
  to order, start with a CBC.&rdquo;</i></p>
  </div>
<!--/PDML4AUDIO-->"""

CRAM_ROWS = [
 ("★ The ranges are MEANT to be approximate",
  "She teaches them as LAB-DEPENDENT BY DESIGN: “54 to 62 PLUS OR MINUS A FEW, depending on what lab you're in… IT DOESN'T MATTER WHAT THE RANGE IS, IT JUST MATTERS WHAT THE RANGE IS FOR WHERE YOU'RE WORKING.” So the deck's three “contradictions” are not errors. Learn the approximate figure and the DIRECTION of abnormality."),
 ("★ The exception — PLATELETS",
  "She used 150,000–450,000 and said this is the ONE she has NOT seen vary from lab to lab. If you must commit one platelet range, commit that."),
 ("★ ANC — you must be able to calculate it",
  "Apps and the EMR will compute it, “HOWEVER, EVERYONE NEEDS TO KNOW HOW TO CALCULATE THAT.” Two formulas; which one depends ONLY on whether the white count is in whole numbers or thousands."),
 ("★ The neutropenia table only applies BELOW 1,500",
  "Asked directly: the “CHART IS ONLY FOR THOSE INDIVIDUALS who have an ANC of LESS THAN 1500. Because we know that the 2700 is more than 1500, we know that the patient is not neutropenic.” NOT ON THE SLIDE. Calculate FIRST, then decide whether the table applies at all."),
 ("Where she put the line on the anemia algorithm",
  "TWICE. Microcytic: “for now, I'm HAPPY IF YOU UNDERSTAND GENETIC VERSUS NON-GENETIC; the rest will come later.” Normocytic: “all of this will come [with heme] — if you can just FOCUS ON THIS FIRST PART here.” The full algorithm is still on the slides; that is just where the emphasis is."),
 ("With vs without differential — her rule",
  "FIRST time you meet a patient and work them up → WITH differential. AFTERWARDS, monitoring a known problem → WITHOUT is enough. And: “IF WE DON'T KNOW WHAT TO ORDER, START WITH A CBC.”"),
 ("Her hemoglobin/hematocrit habit",
  "Read the HEMOGLOBIN, MULTIPLY BY THREE, and check the HEMATOCRIT lands in the same vicinity."),
]


def main():
    print("verifying quotes against BOTH transcripts...")
    verify_quotes()

    # ---- guide: insert the emphasis box, and correct the "no recording" footer
    g = open(GUIDE, encoding="utf-8").read()
    g = re.sub(r"<!--PDML4AUDIO-->.*?<!--/PDML4AUDIO-->", "", g, flags=re.S)
    anchor = '  <h3 class="sub" id="l4-components">'
    assert g.count(anchor) == 1, "section 4.1 anchor not found once"
    g = g.replace(anchor, GUIDE_BOX + "\n\n" + anchor, 1)

    # Matched as a WHITESPACE-TOLERANT pattern, not an exact string: the source
    # wraps this sentence across lines and the break falls inside "No lecture
    # recording", so an exact match failed on a sentence that was plainly there.
    OLDFOOT_RX = re.compile(
        r"<b>No\s+lecture\s+recording exists for this topic yet</b>\s*&mdash;\s*everything here is\s+"
        r"from the slides, and where the\s+deck states a value two different ways both are\s+"
        r"shown rather than one being chosen silently\.")
    NEWFOOT = ("The 24 August 2026 lecture recording (Professor Chand Shah, 63 minutes) has been "
               "folded in &mdash; see the emphasis box at the top of this section &mdash; and was "
               "cross-examined against Notability&rsquo;s independent transcript. Where the deck "
               "states a value two different ways both are shown, because the recording confirms "
               "that is deliberate.")
    # Idempotent: the emphasis box is fenced and stripped on re-run, but this
    # footer edit is one-way, so a second run must recognise its own output
    # rather than assert. (It did assert, after a later step in the same run
    # failed and left the guide edited but the cram sheet not.)
    if NEWFOOT not in g:
        assert OLDFOOT_RX.search(g), "the 'no recording' footer sentence was not found to replace"
        g = OLDFOOT_RX.sub(lambda _m: NEWFOOT, g, count=1)
    assert "No lecture recording exists" not in g, "stale 'no recording' claim survived"

    for tag in ("section", "table", "tr", "td", "th", "div", "p"):
        o = len(re.findall(r"<%s[ >]" % tag, g)); c = g.count("</%s>" % tag)
        assert o == c, "%s unbalanced after edit: %d/%d" % (tag, o, c)
    open(GUIDE, "w", encoding="utf-8").write(g)

    # ---- cram: a lecture-emphasis section, same convention as the other classes
    import html as H
    c = open(CRAM, encoding="utf-8").read()
    c = re.sub(r'\n  <section class="topic" id="l4-lecture".*?</section>\n', "", c, flags=re.S)
    c = re.sub(r'      <a href="#l4-lecture".*?</a>\n', "", c)
    # THE LECTURE-EMPHASIS SECTIONS SHARE ONE ACCENT ON PURPOSE. Every
    # "From Prof. X's Lecture" block across the cram sheets uses #8a3f4a --
    # derm2-lecture, bacterial-lecture, infest-lecture and imaging-lecture all
    # do. So this must NOT assert accent uniqueness the way a new topic section
    # does; it must assert the opposite, that it matches the house colour for
    # this kind of section.
    acc, bg, zeb, ink = "#8a3f4a", "#f4e3e6", "#faf1f3", "#6b2f38"
    siblings = re.findall(r'<section class="topic" id="[a-z0-9-]*lecture"[^>]*--acc:(#[0-9a-f]{6})', c)
    assert not siblings or all(x == acc for x in siblings), (
        "lecture-emphasis sections already use %r, not %s -- follow the house "
        "convention rather than introducing a second colour" % (sorted(set(siblings)), acc))
    rows = "\n".join('          <tr><td class="h">%s</td><td>%s</td></tr>'
                     % (H.escape(a), H.escape(b)) for a, b in CRAM_ROWS)
    sec = ('\n  <section class="topic" id="l4-lecture" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">\n'
           '    <div class="shead"><span class="dot" style="background:%s"></span><h2>&#9733; From Prof. Shah&rsquo;s Lecture</h2></div>\n'
           '    <div class="scroll">\n      <table>\n'
           '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
           '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n'
           % (acc, bg, zeb, ink, acc, rows))
    last = c.rindex('<section class="topic"')
    end = c.index("\n  </section>", last) + len("\n  </section>\n")
    link = ('      <a href="#l4-lecture" style="color:%s"><span class="dot" style="background:%s">'
            '</span>&#9733; From Prof. Shah&rsquo;s Lecture</a>\n' % (ink, acc))
    c = c[:end] + sec + c[end:]
    # The cram sheets have no </nav>; the jump rail is a bare run of <a> tags.
    # Anchoring on it unconditionally raised ValueError on a file that was
    # otherwise fine, so fall back to the last link on the page.
    _stop = c.index("</nav>") if "</nav>" in c else len(c)
    la = c.rindex("</a>\n", 0, _stop) + len("</a>\n")
    c = c[:la] + link + c[la:]
    ids = set(re.findall(r'id="([^"]+)"', c))
    dang = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', c) if a and a not in ids]
    assert not dang, "dangling jump links: %r" % dang
    open(CRAM, "w", encoding="utf-8").write(c)

    print("guide: emphasis box added, 'no recording' footer corrected")
    print("cram: lecture section added (%d rows)" % len(CRAM_ROWS))


if __name__ == "__main__":
    main()
