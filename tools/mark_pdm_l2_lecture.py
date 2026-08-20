#!/usr/bin/env python3
"""Fold the 2026-08-19 Medical Imaging recording into the PDM I Exam 1 guide and
cram sheet.

The Lecture 2 quizzes, guide and cram were all built BEFORE this audio existed,
and the guide said so explicitly -- "nothing here is weighted by spoken emphasis,
only by what the deck spends slides on". This is the pass that fixes that, and
the footer note is updated to stop claiming otherwise.

CROSS-EXAMINED. Both my own transcription and Notability's were read and diffed.
On the one thing that matters most -- what is NOT on the exam -- they agree
exactly, and there is only ONE such statement in 108 minutes.

Idempotent: fenced in <!--PDML2AUDIO--> and stripped before re-inserting.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1")
GUIDE = os.path.join(DIR, "pdm-exam-1-study-guide.html")
CRAM = os.path.join(DIR, "pdm-exam-1-cram-sheet.html")
OPEN, CLOSE = "<!--PDML2AUDIO-->", "<!--/PDML2AUDIO-->"

BLOCK = '''%s
  <div class="prof-flag"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 19 August 2026</span>
  <p>108 minutes of audio, cross-examined against Notability&rsquo;s own transcript. On the question
  that matters most &mdash; what is <em>not</em> examinable &mdash; the two transcriptions agree
  exactly, and there is only <b>one</b> such statement in the whole lecture.</p>
  <table>
    <tr><th>She said</th><th>What it means for you</th></tr>
    <tr><td><em>&ldquo;The most important thing, and this is totally like a, like don&rsquo;t stress about this. <mark class="prof-highlight">This is not gonna be on the test.</mark> This is just like a life thing&hellip; if you&rsquo;re trying to trend somebody&rsquo;s magnetic resonance images&rdquo;</em> [1:02:11]</td><td><b>The only de-emphasis in the lecture.</b> Keeping a patient on the same scanner so serial studies stay comparable &mdash; her example was repeating scans every six months in multiple sclerosis &mdash; is practice, not exam material.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">You need to know what the view is</mark> when you&rsquo;re looking at it, so that you can kind of decide, like, is this actually cardiomegaly or not?&rdquo;</em> [1:14:06]</td><td>The posterior-anterior versus anterior-posterior distinction is not trivia about beam direction. <b>Read an anterior-posterior film as if it were posterior-anterior and you will call cardiomegaly that is not there.</b> She adds the practical corollary: a sick inpatient who cannot stand gets an anterior-posterior film, so this comes up constantly.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">There&rsquo;s your like buzzword phrase, free air under the diaphragm, perforated bowel.</mark>&rdquo;</em> [1:22:50]</td><td>She called this one a buzzword out loud, which is as close to a flag as this lecture gets. <b>Free air under the diaphragm = perforated bowel</b> &mdash; <em>unless</em> they have had recent laparoscopic surgery with insufflation and have not yet absorbed the gas. With belly pain, fever, nausea and vomiting and no recent surgery, it is perforation. The abdominal film is taken <b>upright</b> precisely so air floats up and fluid settles down.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">You also need to know renal function, but for kind of a different reason.</mark> Gadolinium is not necessarily nephrotoxic. It can be, but the issue is clearance of it&hellip; then it will build up in their tissues and then that is toxic. Magnetic resonance, computed tomography, kidney function, check it.&rdquo;</em> [1:40:24]</td><td><b>This refines the slide.</b> The deck says gadolinium can cause kidney damage but is not as harmful as computed tomography contrast. The mechanism she wants is different: with iodinated contrast the agent is <em>nephrotoxic</em>; with gadolinium the kidney is the <em>route of clearance</em>, and impaired clearance lets it accumulate in tissue where it becomes toxic. Either way, <b>check renal function before either.</b></td></tr>
    <tr><td><em>&ldquo;There should not be cross-reactivity for a shellfish allergy and iodinated radiocontrast. <mark class="prof-highlight">However, if they have an iodine allergy, absolutely you worry about allergy. But when in doubt, you&rsquo;re gonna pretreat.</mark>&rdquo;</em> [1:39:11]</td><td><b>An important refinement on a slide that states the rule bluntly.</b> Shellfish allergy is not iodine allergy &mdash; but a genuine iodine allergy <em>is</em> a concern. Her actual clinic question is: &ldquo;do you have an iodine allergy, yes or no?&rdquo; And when in doubt you pretreat &mdash; diphenhydramine and prednisone at intervals beforehand, plus fluids.</td></tr>
    <tr><td><em>&ldquo;Contrast media&hellip; They are also radiation. The contrast media itself can also increase cancer risk. <mark class="prof-highlight">It&rsquo;s all carcinogenic.</mark>&rdquo;</em> [27:38]</td><td>She stated the deck&rsquo;s carcinogenicity point flatly and then tied it straight back to the diagnostic approach: &ldquo;that&rsquo;s why one of the questions&hellip; is, can we do this without contrast?&rdquo;</td></tr>
    <tr><td><em>&ldquo;Neoplastic agents make more blood vessels grow in that site&hellip; they become more vascularized compared to the surrounding tissues. So you inject intravenous contrast, and <mark class="prof-highlight">that tumor&rsquo;s gonna light up when it&rsquo;s malignant.</mark>&rdquo;</em> [1:27:54]</td><td><b>The mechanism the slide only implies.</b> Contrast delineates a neoplastic from a benign mass because malignancy recruits its own vasculature. The same logic explains why an abscess enhances &mdash; inflammation, oedema and increased blood flow to the area.</td></tr>
    <tr><td><em>&ldquo;In primary care, <mark class="prof-highlight">you should never ever order that</mark>&hellip; you better have sent them to a specialist. Very dangerous.&rdquo;</em> [27:11]</td><td>On injecting contrast into a pregnant uterus. If you have reached the point of needing it, the patient has already been referred.</td></tr>
    <tr><td><em>&ldquo;You&rsquo;re going to choose which side based on <mark class="prof-highlight">which direction you want to view fluid</mark>&hellip; we use decubitus positioning a lot to layer out fluid.&rdquo;</em> [1:17:47]</td><td>Decubitus is not one position but a choice of side, made according to where the fluid should run.</td></tr>
    <tr><td><em>&ldquo;Yes, you can memorize, I do a computed tomography pulmonary embolism protocol for pulmonary embolism&hellip; But if you&rsquo;re like, I don&rsquo;t really know for sure what this patient has, but I think something&rsquo;s wrong with their bones &mdash; <mark class="prof-highlight">you&rsquo;re definitely gonna pick either an x-ray or a computed tomography over an ultrasound.</mark>&rdquo;</em> [1:10:31]</td><td>Her stated method for objective c. Memorised protocols are fine, but the reliable move is to reason from the tissue: <b>bone &rarr; x-ray or computed tomography; soft tissue &rarr; often start with ultrasound.</b> This is also why slide 34&rsquo;s structures table matters less than knowing the principle.</td></tr>
  </table>
  <p class="tag">Quoted from the 19 August 2026 lecture recording, with timestamps. Where the recording
  and the slide disagree on a number, the slide wins &mdash; but where the recording explains a
  mechanism the slide only asserts, the recording is the better teacher.</p>
  </div>
%s''' % (OPEN, CLOSE)

CRAM_ROWS = [
 ("NOT on the exam (her words)", "Keeping a patient on the SAME MRI machine so serial studies stay comparable — e.g. repeating scans every 6 months in multiple sclerosis. “This is not gonna be on the test.” The ONLY de-emphasis in the whole lecture."),
 ("Know the VIEW before you read the film", "“You need to know what the view is… so that you can decide, is this actually cardiomegaly or not?” A sick inpatient who cannot stand gets an AP — so read AP as AP, or you will call cardiomegaly that is not there."),
 ("Her named BUZZWORD", "FREE AIR UNDER THE DIAPHRAGM = PERFORATED BOWEL. Unless recent laparoscopic surgery with insufflation and unabsorbed gas. Belly pain + fever + nausea/vomiting + no recent surgery → perforation. The abdominal film is UPRIGHT so air rises and fluid settles."),
 ("Gadolinium vs iodinated — WHY you check renal function", "IODINATED contrast is NEPHROTOXIC. GADOLINIUM is mostly a CLEARANCE problem — if kidney function is low it BUILDS UP IN TISSUES and that is toxic. Different reason, same action: “MRI, CT, kidney function, check it.”"),
 ("Shellfish vs iodine allergy — the refinement", "NO cross-reactivity between shellfish allergy and iodinated contrast. BUT a genuine IODINE allergy IS a concern. Ask directly: “do you have an iodine allergy, yes or no?” WHEN IN DOUBT, PRETREAT — diphenhydramine and prednisone at intervals beforehand, plus fluids."),
 ("Why contrast shows a malignancy", "Neoplasms GROW THEIR OWN VESSELS and become more vascularized than surrounding tissue, so “that tumor's gonna light up when it's malignant.” Same logic for an abscess: inflammation, oedema and increased blood flow."),
 ("Choosing a modality when you are not sure", "Reason from the TISSUE, not from a memorised protocol. BONE → x-ray or CT. SOFT TISSUE → often start with ultrasound."),
 ("Decubitus is a CHOICE of side", "Pick the side based on WHICH DIRECTION YOU WANT THE FLUID TO RUN. Used a lot to layer out fluid."),
 ("Contrast in pregnancy, primary care", "“You should never ever order that… you better have sent them to a specialist. Very dangerous.”"),
]


def main():
    g = open(GUIDE, encoding="utf-8").read()
    g = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), "", g, flags=re.S)

    # place the block immediately after the Lecture 2 objectives box
    i = g.index('id="medical-imaging"')
    j = g.index("</div>", g.index('<div class="callout">', i)) + len("</div>")
    g = g[:j] + "\n\n  " + BLOCK + g[j:]

    # the footer claimed there was no recording; there is one now
    old = ("There\n  was no lecture recording available for this topic when this section was written, so nothing here\n"
           "  is weighted by spoken emphasis &mdash; only by what the deck spends slides on.")
    new = ("The 19 August 2026 lecture recording has been folded in &mdash; see the emphasis box at the top of\n"
           "  this section &mdash; and was cross-examined against Notability&rsquo;s independent transcript.")
    # Idempotent: a second run finds the replacement already in place.
    if old in g:
        g = g.replace(old, new, 1)
    else:
        assert new in g, "footer is neither the old disclaimer nor the new note"
    assert OPEN in g and "no lecture recording available" not in g
    open(GUIDE, "w", encoding="utf-8").write(g)
    print("guide: emphasis block added, stale 'no recording' footer replaced")

    c = open(CRAM, encoding="utf-8").read()
    if 'id="imaging-lecture"' in c:
        print("cram: lecture rows already present")
        return
    import html as H
    rows = "\n".join('          <tr><td class="h">%s</td><td>%s</td></tr>' % (H.escape(a), H.escape(b))
                     for a, b in CRAM_ROWS)
    sec = ('\n  <section class="topic" id="imaging-lecture" style="--acc:#8a3f4a;--acc-bg:#f3e3e6;'
           '--acc-zebra:#faf1f3;--acc-ink:#6d2f38">\n'
           '    <div class="shead"><span class="dot" style="background:#8a3f4a"></span>'
           '<h2>From the Imaging Lecture Recording</h2></div>\n'
           '    <div class="scroll">\n      <table>\n'
           '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
           '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n' % rows)
    link = ('      <a href="#imaging-lecture" style="color:#6d2f38"><span class="dot" '
            'style="background:#8a3f4a"></span>From the Imaging Lecture</a>\n')
    m = re.search(r'      <a href="#contrast"[^>]*>.*?</a>\n', c, re.S)
    assert m, "contrast jump link not found"
    c = c[:m.end()] + link + c[m.end():]
    foot = "  <footer>"
    assert c.count(foot) == 1
    c = c.replace(foot, sec + "\n" + foot)
    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th"):
        o, cl = len(re.findall(r"<%s[ >]" % tag, c)), c.count("</%s>" % tag)
        assert o == cl, "%s: %d open, %d close" % (tag, o, cl)
    ids = set(re.findall(r'id="([^"]+)"', c))
    assert not [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', c) if a not in ids], "dangling jump link"
    assert "**" not in c
    open(CRAM, "w", encoding="utf-8").write(c)
    print("cram: %d lecture rows added" % len(CRAM_ROWS))


if __name__ == "__main__":
    main()
