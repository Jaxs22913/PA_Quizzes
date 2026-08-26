#!/usr/bin/env python3
"""Pull the two teachable figures out of the PDM I Lecture 5 deck.

Only two of the deck's ten pictures carry content. The rest are a periodic
table, three chemistry-cat memes, a glucose molecule, an "element of surprise"
joke and a stock photo of the case patient -- all decorative, and none of them
belongs in a study guide. See [[image_only_slides]]: the check has to happen by
LOOKING, and it did.

  fishbone.png  slide 4 (also slide 6)  -- the hand-drawn reference-range sheet.
                Slide 4 extracts as COMPLETELY EMPTY text. This picture is the
                only copy of the reference set anywhere in the file, which is
                exactly the failure mode tools/ocr_deck_images.py was written
                for. Reynolds narrates it in the lecture and points out it
                carries ranges but no units.
  co2-buffer.png slide 12 -- the carbon dioxide and bicarbonate buffer system,
                lungs against kidney with the pH scale. Prose cannot carry this.
"""
import os, re, zipfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE),
                   "Principles of Diagnostic Medicine I Exam 1", "pdm-exam-1-l5-images")
DECK = os.path.expanduser(
    "~/Desktop/Semester 2/Principles of Diagnostic Medicine I Inbox/Exam 1/"
    "5. Chemistry Panels, Renal Fxn, Elytes.pptx")

# (member in the pptx, output slug, the slide it teaches)
WANTED = [("ppt/media/image3.png", "fishbone", 4),
          ("ppt/media/image7.png", "co2-buffer", 12)]


def main():
    assert os.path.exists(DECK), "deck not found: %s" % DECK
    os.makedirs(OUT, exist_ok=True)
    z = zipfile.ZipFile(DECK)
    names = set(z.namelist())
    for member, slug, slide in WANTED:
        assert member in names, ("%s is not in the deck -- the media numbering has "
                                 "changed, re-check before trusting this list" % member)
        data = z.read(member)
        assert len(data) > 20000, ("%s is only %d bytes, too small to be the figure "
                                   "expected on slide %d" % (member, len(data), slide))
        with open(os.path.join(OUT, slug + ".png"), "wb") as fh:
            fh.write(data)
        print("wrote %-12s %7d bytes  (slide %d)" % (slug + ".png", len(data), slide))


if __name__ == "__main__":
    main()
