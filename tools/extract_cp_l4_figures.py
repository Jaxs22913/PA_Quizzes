#!/usr/bin/env python3
"""Pull the teaching figures out of the Clin Path I Lecture 4 deck.

The deck holds 136 pictures. Most are clinical photographs of one condition
each; these four are the ones prose cannot replace, and each was VIEWED at full
size before being chosen, per [[image_only_slides]].

  visual-fields   slide 34 -- lesion sites A to E against the resulting monocular
                  fields. This is the figure Webster scoped in the lecture:
                  know A, B and C; D and E go to neurology.
  detachment      slide 35 -- labelled cross-section showing fluid passing through
                  a retinal tear and peeling the retina off.
  normal-fundus   slide 29 -- a normal fundus for comparison.
  oct             slide 30 -- optical coherence tomography showing the retinal
                  layers in section.

DELIBERATELY NOT INCLUDED: the deck's labelled eye-anatomy diagram on slide 5.
It carries a third-party vendor watermark across the bottom, and this repository
is public, so committing it would republish someone's marked asset. The anatomy
it teaches is carried in prose and in the tunics table instead.
See [[media_asset_licensing]].
"""
import os, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 1",
                   "cp-exam-1-l4-images")
DECK = os.path.expanduser(
    "~/Desktop/Semester 2/Clinical Pathophysiology I Inbox/Exam 1/"
    "4. Ophthalmic Pathophysiology_STUDENT VERSION_v2.pptx")

WANTED = [("ppt/media/image105.png", "visual-fields", "png", 34),
          ("ppt/media/image114.png", "detachment",    "png", 35),
          ("ppt/media/image93.jpg",  "normal-fundus", "jpg", 29),
          ("ppt/media/image92.jpg",  "oct",           "jpg", 30)]


def main():
    assert os.path.exists(DECK), "deck not found: %s" % DECK
    os.makedirs(OUT, exist_ok=True)
    z = zipfile.ZipFile(DECK)
    names = set(z.namelist())
    for member, slug, ext, slide in WANTED:
        assert member in names, ("%s is not in the deck -- media numbering has changed, "
                                 "re-view before trusting this list" % member)
        data = z.read(member)
        assert len(data) > 15000, ("%s is only %d bytes, too small to be the figure "
                                   "expected on slide %d" % (member, len(data), slide))
        with open(os.path.join(OUT, "%s.%s" % (slug, ext)), "wb") as fh:
            fh.write(data)
        print("wrote %-16s %7d bytes  (slide %d)" % (slug + "." + ext, len(data), slide))


if __name__ == "__main__":
    main()
