#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Say where the "Clark level" name came from, because the deck never uses it.

THE PROBLEM. Slide 50 of the CMS Lecture 9 deck has NO TEXT AT ALL -- it is
purely a figure showing five blocks of skin labelled "Level I" to "Level V"
against Epidermis / Papillary dermis / Reticular dermis / Subcutaneous tissue.
The word "Clark" appears NOWHERE in the deck: not on that slide, not in the
figure itself, not anywhere in the other 100 slides.

I supplied the name from outside the deck. The content is correct -- that IS the
Clark level system -- but two things follow that matter for a student:

  1. Anyone searching their slides for "Clark" finds nothing, and reasonably
     concludes they have lost a slide.
  2. If the exam is written from the deck, the question will say "Level IV",
     not "Clark level IV".

So the name stays, because it is the right name and they will meet it
everywhere else, but it is now introduced AS an outside name rather than
presented as the deck's own wording.

This is the third thing this build turned up about slide 50 and its neighbours:
they carry content that exists only as pictures, they extract as blank, and now,
that even the vocabulary is not in the file.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CMS = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 1")

EDITS = [
 # ---- study guide -------------------------------------------------------
 (os.path.join(CMS, "cms-exam-1-study-guide.html"),
  '<tr><th>Clark level (slide 50)</th><th>What it means</th></tr>',
  '<tr><th>Level of invasion (slide 50)</th><th>What it means</th></tr>'),

 (os.path.join(CMS, "cms-exam-1-study-guide.html"),
  '<p class="prof-lead"><mark class="prof-highlight">The next three items exist only as pictures in the\n  deck.</mark></p>',
  '<p class="prof-lead"><mark class="prof-highlight">The next three items exist only as pictures in the\n  deck.</mark> A note on naming: <b>slide 50 labels these simply &ldquo;Level I&rdquo; to\n  &ldquo;Level V&rdquo;.</b> The word <b>Clark</b> does not appear anywhere in this deck &mdash; it\n  is the conventional name for this system and you will meet it everywhere else, so it is used\n  below, but do not go hunting your slides for it.</p>'),

 (os.path.join(CMS, "cms-exam-1-study-guide.html"),
  '<p><strong>Clark level is an anatomic layer; Breslow thickness is a measurement &mdash; and Breslow\n  is the dominant prognostic variable</strong>',
  '<p><strong>The level of invasion (Clark) is an anatomic LAYER; Breslow thickness is a\n  MEASUREMENT &mdash; and Breslow is the dominant prognostic variable</strong>'),

 # ---- cram sheet --------------------------------------------------------
 (os.path.join(CMS, "cms-exam-1-cram-sheet.html"),
  'CLARK LEVELS (slide 50 is an IMAGE)',
  'LEVEL OF INVASION, i.e. CLARK (slide 50 is an IMAGE, and the deck never says &quot;Clark&quot;)'),
]


def main():
    changed = 0
    for path, old, new in EDITS:
        s = open(path, encoding="utf-8").read()
        if new in s and old not in s:
            print("  already applied: %s" % os.path.basename(path))
            continue
        assert s.count(old) == 1, ("expected exactly one %r in %s, found %d"
                                   % (old[:50], os.path.basename(path), s.count(old)))
        open(path, "w", encoding="utf-8").write(s.replace(old, new))
        changed += 1
        print("  updated: %s" % os.path.basename(path))

    # The guide must now state, in plain words, that the deck does not use the name.
    g = open(os.path.join(CMS, "cms-exam-1-study-guide.html"), encoding="utf-8").read()
    assert "does not appear anywhere in this deck" in g, \
        "the naming caveat did not land in the guide"
    print("\n%d file(s) updated; guide carries the naming caveat" % changed)


if __name__ == "__main__":
    main()
