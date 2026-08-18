#!/usr/bin/env python3
"""Star what Professor Gopal emphasised in the Dermatology lecture (Clin Path I, Lecture 2).

Source: the 2026-08-18 recording, 8:14–8:50 local. That is the PRE-BREAK portion
only — the recording ends on "Take a 10 minute break", and at 34:42 she says
"we're about halfway through". So these marks cover roughly the first half of the
lecture: anatomy, primary lesions, secondary lesions, and wound healing. Skin
conditions and skin cancers (§2.5, §2.6) are UNMARKED because there is no audio
for them, not because she skipped over them. That distinction is stated on the
page so the absence of a star is never read as "not emphasised".

Method. Two instruments, and they disagreed in a way worth recording:

  - VERBAL cues carried nearly everything. She flags emphasis explicitly and
    repeatedly — "it's important for you to remember", "do keep that in mind",
    "please note", "make note of that too", "that's important to notice", and
    once, decisively, "for our sake of this lecture and testing".
  - PROSODY was close to useless here. Its top hits were slide transitions
    ("Okay, into the dermis", "First we're gonna go through all the primary
    lesions") — she pauses when advancing a slide, which the detector cannot
    tell from emphasis. Exactly one prosody hit overlapped a real verbal cue:
    the keratinocyte 90% line at 2:20. Same conclusion as Dr. Wood's lecture:
    prosody is a weak second instrument, not a primary one.

Idempotent: re-running is a no-op. Run it AFTER extend_cp_guide_l2.py, which
regenerates the section and would otherwise drop the marks.
"""
import io, sys, os

G = "/Users/jaxonluke/Developer/PA_Quizzes/Clinical Pathophysiology I Exam 1/cp-exam-1-study-guide.html"

def flag(label, body):
    return ('<div class="prof-flag"><span class="prof-flag-label">&#9733; %s</span>\n  %s</div>'
            % (label, body))

# ---- boxed emphasis blocks -------------------------------------------------
# (anchor already in the guide, block to insert AFTER it)
BLOCKS = [
 # §2.1 — the framing principle she opened the lecture with and returned to
 ('<p>Three layers: <strong>epidermis</strong>, <strong>dermis</strong> and\n'
  '  <strong>subcutaneous (hypodermis)</strong>. The dermis is where the nerves and vasculature sit.</p>',
  flag("Professor emphasized",
   '<p><strong>There is no vasculature in the epidermis.</strong> She said this in the first '
   'thirty seconds and told the class to carry it through the whole lecture: <em>&ldquo;do keep '
   'that in mind &hellip; it&rsquo;s important for you to remember &hellip; that will help you '
   'differentiate things as we go.&rdquo;</em> It is the reason an erosion cannot bleed and cannot '
   'scar while an ulcer can, and the reason the dermal-epidermal junction is the boundary that '
   'matters in half the definitions below.</p>')),

 # §2.1 — keratin, the only item both instruments flagged
 ('<strong>keratinocytes (about 90%)</strong>, melanocytes, Merkel cells and Langerhans cells.\n'
  '  Turnover is every 30 to 60 days and is more rapid in younger patients.</p>',
  flag("Professor emphasized",
   '<p><strong>Keratinocytes are about 90% of the epidermis, and keratin is the recurring theme.</strong> '
   '<em>&ldquo;That&rsquo;s important to remember, because they produce keratin, and as we walk through '
   'the pathophysiology of the skin today you&rsquo;re going to hear keratin over and over and over '
   'again.&rdquo;</em> It duly reappears below in hyperkeratosis, the epidermal inclusion cyst, the '
   'fissure and lichenification. This was also the one point the prosody analysis independently '
   'flagged.</p>')),

 # §2.1 — mast cells, flagged twice
 ('adipocytes and\n'
  '  <strong>mast cells</strong>, which mediate immunoglobulin E-driven inflammation.</p>',
  flag("Professor emphasized",
   '<p><strong>Where the mast cells live.</strong> Flagged twice &mdash; <em>&ldquo;it&rsquo;s important '
   'to remember that this is where our mast cells are located, because we&rsquo;ll be talking about mast '
   'cells a lot later in the pathophysiology&rdquo;</em>, then again on the next slide, <em>&ldquo;make '
   'note of that too&rdquo;</em>. They sit in the <strong>dermis</strong>, and they are the mechanism '
   'behind the wheal.</p>')),

 # §2.2 — the single most useful thing in the recording
 ('<div class="pearl"><strong>One discriminator does most of the work:</strong> macules and patches\n'
  '  are <em>not</em> palpable; papules, nodules and plaques are. Everything else follows from depth\n'
  '  and content.</div>',
  flag("Professor emphasized &mdash; exam scope",
   '<p><strong>She addressed the size cut-offs directly, and told the class how they will be '
   'tested.</strong> Sources disagree &mdash; many define a macule as up to <em>one centimetre</em> '
   'rather than five millimetres, and the Physical Diagnosis II deck does exactly that.</p>'
   '<p><em>&ldquo;For our sake of this lecture and testing, I&rsquo;m going to define it up to five '
   'millimetres &hellip; if you&rsquo;re reading it in other sources and it goes up to one centimetre, '
   'don&rsquo;t be alarmed.&rdquo;</em> And twice: <em>&ldquo;it&rsquo;s not gonna be a gotcha thing on '
   'the exam, I promise you &hellip; do know the general range. The macules are smaller, the patches '
   'are bigger.&rdquo;</em></p>'
   '<p>So the table above uses <strong>her</strong> numbers, which are the ones this exam will use. '
   'Know the ordering cold; do not lose sleep over the exact millimetre.</p>')),

 # §2.4 — she called this out, then a student question made it the payoff
 ('<h3 class="sub" id="derm-healing">',
  None),  # handled separately below, needs to land INSIDE the subsection
]

# ---- inline highlights -----------------------------------------------------
HIGHLIGHTS = [
 ("Meissner's and Pacinian corpuscles", None),  # in figure alt text - skip
]

INLINE = [
 # (exact text in the guide, replacement wrapping it in a highlight)
 ("Open onto the skin surface; water and electrolytes (sodium, chloride); cooling by evaporation",
  'Open onto the skin surface; <mark class="prof-highlight">water and electrolytes (sodium, chloride)</mark>; cooling by evaporation'),
 ("General term for rapid cellular growth, benign or malignant.",
  'General term for rapid cellular growth, <mark class="prof-highlight">benign or malignant &mdash; &ldquo;tumor by itself doesn&rsquo;t mean malignant&rdquo;</mark>.'),
]


def main():
    s = io.open(G, encoding="utf-8").read()
    if "Professor emphasized &mdash; exam scope" in s:
        print("marks already present — nothing to do")
        return 0
    added = 0

    for anchor, block in BLOCKS:
        if block is None:
            continue
        assert s.count(anchor) == 1, "anchor not unique (%d): %r" % (s.count(anchor), anchor[:60])
        s = s.replace(anchor, anchor + "\n  " + block, 1)
        added += 1

    # §2.4 wound healing — insert after the phase table's intro paragraph
    heal_anchor = '<h3 class="sub" id="derm-healing">'
    i = s.index(heal_anchor)
    j = s.index("</p>", i) + len("</p>")
    s = s[:j] + "\n  " + flag("Professor emphasized",
       '<p><strong>Granulation tissue must stop forming after the proliferative phase.</strong> '
       '<em>&ldquo;The formation of granulation tissue should cease at this stage, so that&rsquo;s '
       'important to notice. We should not be producing granulation tissue outside of the '
       'proliferative phase.&rdquo;</em></p>'
       '<p>A student then asked what happens when it does not cease, and Professor Gopal called it '
       '<em>&ldquo;a great question &hellip; this is exactly where we&rsquo;re at&rdquo;</em>: '
       'fibroblast dysregulation prolongs the proliferative phase, collagen is laid down abundantly '
       'and haphazardly, and it exceeds the boundaries of the original wound &mdash; giving '
       '<strong>hypertrophic scars and keloids</strong>. She added that keloids are especially common '
       'in <strong>darker skin tones</strong>, and that trauma as minor as an ear piercing can '
       'produce one.</p>') + s[j:]
    added += 1

    for old, new in INLINE:
        assert s.count(old) == 1, "inline target not unique (%d): %r" % (s.count(old), old[:50])
        s = s.replace(old, new, 1)
        added += 1

    # coverage note, so an unmarked subsection is never misread
    cov_anchor = '<h3 class="sub" id="derm-conditions">'
    assert s.count(cov_anchor) == 1
    note = ('<div class="callout"><strong>No recording past this point.</strong> The stars above come '
            'from the 2026-08-18 lecture recording, which covers only up to the mid-lecture break '
            '&mdash; at 34:42 she said &ldquo;we&rsquo;re about halfway through&rdquo;. Sections 2.5 '
            'and 2.6 are unmarked because there is no audio for them, <em>not</em> because she passed '
            'over them quickly. Treat the absence of a star here as missing data.</div>\n  ')
    k = s.index(cov_anchor)
    k = s.index("</h3>", k) + len("</h3>")
    s = s[:k] + "\n  " + note + s[k:]
    added += 1

    io.open(G, "w", encoding="utf-8").write(s)
    print("applied %d marks" % added)
    print("  boxed blocks : %d" % s.count('class="prof-flag"'))
    print("  highlights   : %d" % s.count('class="prof-highlight"'))
    return 0


if __name__ == "__main__":
    sys.exit(main())
