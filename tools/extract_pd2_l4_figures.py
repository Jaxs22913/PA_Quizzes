#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the teaching figures out of the PD2 Lecture 4 (ENT) deck.

The deck holds 105 pictures across 95 slides, most of them template chrome.
These eight were each VIEWED at full size before being chosen, per
[[image_only_slides]], and named for what is IN them rather than for their
position in the relationship list, per [[lettered_slide_images]].

  conduction      slide 5  -- a tuning fork wired into a cut-away ear, with the
                  air conduction and bone conduction routes drawn as separate
                  arrows converging on the cochlea. This is the figure for the
                  block the class was told is worth three points.
  normal-drum     slide 27 -- a normal tympanic membrane. "Know what normal
                  looks like" was said repeatedly; this is the reference.
  bulging-series  slide 32 -- FOUR panels, lettered A to D: normal, mild,
                  moderate and severe bulging from middle ear effusion. The
                  lettering and caption are baked into the picture.
  centor          slide 65 -- THE MODIFIED CENTOR ALGORITHM. This is the reason
                  the figure set exists: slide 65's text is one line, and the
                  entire scoring scheme -- the four criteria at one point each,
                  the AGE adjustment, and the score bands -- lives only inside
                  this image. A text-only reading of the deck loses it.
  septum          slide 56 -- basal view of a caudal septal deviation.
  polyp           slide 59 -- endoscopic view labelled P for polyp, S for
                  septum, T for an allergic-looking inferior turbinate. Shows
                  the polyp AGAINST the turbinate, which is the usual confusion.
  strep           slide 72 -- erythematous tonsils in group A streptococcal
                  pharyngitis.
  nodes           slide 79 -- the neck node chains labelled, with external and
                  internal drainage arrows. Supports the practical, where the
                  chain has to be NAMED while it is being palpated.
  ludwig          slide 83 -- anterior neck oedema and early cellulitis in
                  Ludwig's angina.

Licensing: [[media_asset_licensing]] clears a course-slide image provided the
slide is cited, and says not to crop vendor marks out. Several of these carry
publisher attribution baked in and it stays visible.
"""
import os, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "Physical Diagnosis 2 Exam 1",
                   "pd2-exam-1-l4-images")
DECK = os.path.expanduser(
    "~/Desktop/Semester 2/Physical Diagnosis 2 Inbox/Exam 1/PD II ENT 2026.pptx")

WANTED = [("ppt/media/image5.png",   "conduction",     "png",  5),
          ("ppt/media/image31.png",  "normal-drum",    "png", 27),
          ("ppt/media/image40.png",  "bulging-series", "png", 32),
          ("ppt/media/image56.png",  "septum",         "png", 56),
          ("ppt/media/image60.png",  "polyp",          "png", 59),
          ("ppt/media/image69.png",  "centor",         "png", 65),
          ("ppt/media/image80.png",  "strep",          "png", 72),
          ("ppt/media/image97.png",  "nodes",          "png", 79),
          ("ppt/media/image99.png",  "ludwig",         "png", 83)]

# Sizes recorded when each file was viewed. If the deck is re-saved and the
# media numbering shifts, these stop matching -- which beats silently writing
# the wrong picture under the right name.
SIZES = {"conduction": 332585,
         "normal-drum": 198042,
         "bulging-series": 269553,
         "septum": 232845,
         "polyp": 292099,
         "centor": 45296,
         "strep": 120197,
         "nodes": 416656,
         "ludwig": 226439}


def main():
    assert os.path.exists(DECK), "deck not found: %s" % DECK
    os.makedirs(OUT, exist_ok=True)
    z = zipfile.ZipFile(DECK)
    names = set(z.namelist())
    mismatched = []
    for member, slug, ext, slide in WANTED:
        assert member in names, ("%s is not in the deck -- media numbering has changed, "
                                 "re-view every figure before trusting this list" % member)
        data = z.read(member)
        if len(data) != SIZES[slug]:
            mismatched.append((slug, member, len(data), SIZES[slug]))
            continue
        open(os.path.join(OUT, "%s.%s" % (slug, ext)), "wb").write(data)
        print("  slide %2d  %-15s %7d bytes" % (slide, slug, len(data)))
    assert not mismatched, (
        "media numbering has shifted -- view the pictures again before rebuilding: %r"
        % mismatched)
    print("wrote %d figures to %s" % (len(WANTED), os.path.basename(OUT)))


if __name__ == "__main__":
    main()
