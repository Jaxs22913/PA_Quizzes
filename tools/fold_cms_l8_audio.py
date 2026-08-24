#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fold the 24 August CMS Lecture 8 recording into the guide and cram sheet.

Professor Shah, Pigmented Skin Lesions. Cross-examined against Notability's
independent transcript; every quote below appears in BOTH.

THE RECORDING IS INCOMPLETE AT BOTH ENDS and the guide says so. It opens
mid-sentence, already discussing ephelides and the MCR1 gene, so the start of
the lecture is missing; and it stops mid-case at the end -- "here's a picture
... I'm gonna ask you for a question, right? So based". 33.6 minutes across two
segments with a forty-minute gap between them, and Notability holds no part 1.
Absence of emphasis on a topic here is therefore NOT evidence she passed over
it.

NOTHING WAS MISSING FROM THE BUILT CONTENT. Blue naevus, Reed, Spitz, the
neurocutaneous melanosis magnetic resonance indication -- all already in the
pools, guide, cram and chart. What the audio adds is a TEACHING STRUCTURE that
appears nowhere on the slides, which is the whole reason to listen.

THE NAMES ARE BADLY TRANSCRIBED, in both. "Ephelides" came out as "apelities",
"Reed nevus" as "read nevi" in both, and "SPITZ" APPEARS IN NEITHER TRANSCRIPT
IN ANY FORM. So the identification of the second exception as Spitz is made from
the DECK -- segment 2 opens on a dome-shaped lesion that resembles melanoma and
is managed by wide excision, which is slide 42 word for word -- and the guide
says that is where it comes from rather than implying she named it.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
GUIDE = os.path.join(DIR, "cms-exam-1-study-guide.html")
CRAM = os.path.join(DIR, "cms-exam-1-cram-sheet.html")
REC = os.path.expanduser("~/Desktop/Semester 2/Clinical Medicine and Surgery I Inbox/"
                         "Exam 1/recordings")

QUOTES = ["remembering the pattern", "two things that it's not like that for",
          "these do not go away", "pretty upset at you", "dome shape",
          "resemble melanoma", "remove all the margins", "wide excision"]


def verify():
    mine = os.path.join(REC, "cms-l8-pigmented-lesions-2026-08-24.transcript.txt")
    theirs = os.path.join(REC, "cms-l8-pigmented-lesions-2026-08-24.notability.txt")
    assert os.path.exists(mine), "my own transcript is not written yet"
    def norm(p):
        t = open(p, encoding="utf-8", errors="replace").read()
        t = re.sub(r"\[\d{1,2}:\d{2}(?::\d{2})?\]", " ", t)
        return re.sub(r"\s+", " ", t).lower()
    a, b = norm(mine), norm(theirs)
    bad = [q for q in QUOTES if not (q in a and q in b)]
    for q in bad:
        print("  QUOTE NOT IN BOTH: %r" % q)
    assert not bad, "%d quote(s) in only one transcript" % len(bad)
    # and the claim the guide makes about Spitz being unsaid must hold
    assert "spitz" not in a and "spitz" not in b, \
        "'Spitz' now appears in a transcript -- update the wording that says it does not"
    print("  all %d quotes in BOTH transcripts; 'Spitz' confirmed absent from both" % len(QUOTES))


BOX = """<!--CMSL8AUDIO-->
  <div class="prof-flag"><span class="prof-flag-label">&#9733; From the 24 August lecture</span>
  <p><b><mark class="prof-highlight">She teaches this whole topic to one repeating pattern.</mark></b>
  For lesion after lesion the management is the same three steps &mdash; <b>diagnose clinically,
  observe, and biopsy if it changes in size, colour or shape</b>. Partway through she says it out
  loud: <i>&ldquo;I hope everyone&rsquo;s still <b>remembering the pattern</b> here &hellip; it&rsquo;s
  very similar, very much the same. There&rsquo;s like <b>two things that it&rsquo;s not like that
  for</b>.&rdquo;</i></p>
  <p><b>The two exceptions are the two that imitate melanoma, and both need tissue out with
  margins.</b> <b>Reed naevus</b> (pigmented spindle cell) &mdash; confirm by biopsy, then
  <i>&ldquo;<b>remove all the margins</b> because of the risk of it turning&rdquo;</i> malignant;
  the deck says excision with negative margins. And the one she reaches immediately after, a
  <i>&ldquo;<b>dome shape</b> &hellip; sometimes it can <b>resemble melanoma</b>&rdquo;</i> managed
  by <i>&ldquo;<b>wide excision</b>, so not just removing part of the lesion &hellip; but the entire
  area surrounding it too&rdquo;</i>. <b>Neither transcript contains the word Spitz in any form</b>,
  so that identification comes from the deck &mdash; slide 42 describes exactly this lesion, dome
  shaped, resembling melanoma, diagnosed by biopsy versus wide excision. If you remember one frame
  for this lecture, make it <b>&ldquo;watch them all, cut out the two that look like melanoma&rdquo;</b>.</p>
  <p><b>The ephelides-versus-lentigines discriminator, in her words.</b> On lentigines:
  <i>&ldquo;<b>these do not go away</b> as sun exposure gets less and less&rdquo;</i> &mdash;
  <i>&ldquo;that will be one way that you will be able to differentiate lentigines, sunspots, from
  ephelides, freckles.&rdquo;</i> Same fact as the cram sheet, but it is the one she chose to spell
  out.</p>
  <p><b>A counselling point she framed as self-protection.</b> On cryotherapy for a seborrhoeic
  keratosis: it can come back, so tell them beforehand &mdash; <i>&ldquo;otherwise they&rsquo;ll be
  <b>pretty upset at you</b>&rdquo;</i>.</p>
  <p><b><mark class="prof-highlight">This recording is incomplete at both ends.</mark></b> It begins
  mid-sentence, already in the middle of ephelides and the MCR1 gene, and it stops mid-case during
  the practice questions at the end &mdash; 33.6 minutes across two segments with a forty-minute gap,
  and no part one exists. <b>If a topic below carries no emphasis note, that is not evidence she
  passed over it.</b> Everything on the slides is covered in the sections that follow regardless.</p>
  </div>
<!--/CMSL8AUDIO-->"""

CRAM_ROWS = [
 ("★ THE PATTERN — and its two exceptions",
  "She teaches nearly every pigmented lesion the same way: DIAGNOSE CLINICALLY → OBSERVE → BIOPSY IF IT CHANGES in size, colour or shape. Verbatim: “I hope everyone's still REMEMBERING THE PATTERN here… there's like TWO THINGS THAT IT'S NOT LIKE THAT FOR.” The two are the ones that IMITATE MELANOMA and need tissue out WITH MARGINS: REED NAEVUS (excision with negative margins) and SPITZ (biopsy vs WIDE EXCISION — “not just removing part of the lesion but the ENTIRE AREA SURROUNDING it”). One frame for the whole lecture: WATCH THEM ALL, CUT OUT THE TWO THAT LOOK LIKE MELANOMA."),
 ("Ephelides vs lentigines, her wording",
  "On lentigines: “THESE DO NOT GO AWAY as sun exposure gets less and less” — “that will be one way that you will be able to DIFFERENTIATE LENTIGINES, SUNSPOTS, FROM EPHELIDES, FRECKLES.”"),
 ("Counselling — cryotherapy recurrence",
  "Warn BEFORE you freeze a seborrhoeic keratosis that it can come back, “OTHERWISE THEY'LL BE PRETTY UPSET AT YOU.”"),
 ("⚠ The recording is PARTIAL",
  "Starts MID-SENTENCE inside ephelides/MCR1 and stops MID-CASE at the end; 33.6 min, no part one exists. NO emphasis note on a topic does NOT mean she skipped it. Deck content is covered in full regardless."),
]


def main():
    print("verifying quotes against BOTH transcripts...")
    verify()

    g = open(GUIDE, encoding="utf-8").read()
    g = re.sub(r"<!--CMSL8AUDIO-->.*?<!--/CMSL8AUDIO-->", "", g, flags=re.S)
    anchor = '  <h3 class="sub" id="pig-ephelides"'
    if g.count(anchor) != 1:
        # fall back to the first subsection inside the pigmented section
        i = g.index('id="pigmented-lesions"')
        m = re.search(r'  <h3 class="sub" id="[^"]+"', g[i:])
        assert m, "no subsection found inside the pigmented section"
        anchor = g[i + m.start(): i + m.end()]
        assert g.count(anchor) == 1, "fallback anchor is not unique"
    g = g.replace(anchor, BOX + "\n\n" + anchor, 1)
    for tag in ("section", "table", "tr", "td", "th", "div", "p"):
        o = len(re.findall(r"<%s[ >]" % tag, g)); c = g.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d/%d" % (tag, o, c)
    open(GUIDE, "w", encoding="utf-8").write(g)

    import html as H
    c = open(CRAM, encoding="utf-8").read()
    c = re.sub(r'\n  <section class="topic" id="l8-lecture".*?</section>\n', "", c, flags=re.S)
    c = re.sub(r'      <a href="#l8-lecture".*?</a>\n', "", c)
    acc, bg, zeb, ink = "#8a3f4a", "#f4e3e6", "#faf1f3", "#6b2f38"
    sibs = re.findall(r'<section class="topic" id="[a-z0-9-]*lecture"[^>]*--acc:(#[0-9a-f]{6})', c)
    assert not sibs or all(x == acc for x in sibs), \
        "lecture sections use %r, not %s" % (sorted(set(sibs)), acc)
    rows = "\n".join('          <tr><td class="h">%s</td><td>%s</td></tr>'
                     % (H.escape(a), H.escape(b)) for a, b in CRAM_ROWS)
    sec = ('\n  <section class="topic" id="l8-lecture" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">\n'
           '    <div class="shead"><span class="dot" style="background:%s"></span><h2>&#9733; From Prof. Shah&rsquo;s Pigmented Lesions Lecture</h2></div>\n'
           '    <div class="scroll">\n      <table>\n'
           '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
           '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n'
           % (acc, bg, zeb, ink, acc, rows))
    j = c.index('<section class="topic" id="pigmented')
    j = c.index("\n  </section>", j) + len("\n  </section>\n")
    c = c[:j] + sec + c[j:]
    link = ('      <a href="#l8-lecture" style="color:%s"><span class="dot" style="background:%s">'
            '</span>&#9733; From Prof. Shah&rsquo;s Pigmented Lesions Lecture</a>\n' % (ink, acc))
    pig = re.search(r'      <a href="#pigmented"[^>]*>.*?</a>\n', c, re.S)
    assert pig, "pigmented jump link not found"
    c = c[:pig.end()] + link + c[pig.end():]
    ids = set(re.findall(r'id="([^"]+)"', c))
    dang = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', c) if a and a not in ids]
    assert not dang, "dangling jump links: %r" % dang
    open(CRAM, "w", encoding="utf-8").write(c)

    print("guide: emphasis box added inside the pigmented section")
    print("cram: lecture section added (%d rows)" % len(CRAM_ROWS))


if __name__ == "__main__":
    main()
