#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the teaching figures out of the Clin Path I Lecture 5 (ENT) deck.

The deck holds 97 pictures, most of them template chrome a few hundred bytes
wide. These eleven were each VIEWED at full size before being chosen, per
[[image_only_slides]], and the .rels order is arbitrary per
[[lettered_slide_images]] -- so every file here is named for what is IN it, not
for its position in the relationship list.

  ear-anatomy       slide 4  -- four panels: whole ear, membranous labyrinth with
                    the crista/cupula inset, the cochlear duct with the organ of
                    Corti, and a hair cell wired to a spiral ganglion neuron.
                    One figure that answers objectives 1 and 3 together.
  cochlear-section  slide 5  -- labelled cochlear cross-section. This is the only
                    figure that shows the STRIA VASCULARIS, which is where both
                    cisplatin and furosemide do their damage.
  otosclerosis      slide 10 -- ossicular chain with the fixation point marked at
                    the stapes footplate.
  otitis-externa    slide 13 -- the clinical photograph he narrated at [24:13].
  meniere           slide 16 -- normal labyrinth beside a hydropic one, so the
                    ballooning of the scala media is visible rather than asserted.
  labyrinthitis     slide 17 -- inflammation drawn across canals AND cochlea, which
                    is the whole reason balance and hearing fail together.
  bppv              slide 18 -- otoconia shown both in the utricle and displaced
                    into the canals.
  deviated-septum   slide 22 -- normal against deviated, with the CONTRALATERAL
                    turbinate hypertrophy labelled. The compensation is the part
                    students miss, and this figure shows it directly.
  nasal-polyp       slide 21 -- endoscopic view of a polyp.
  vocal-cords       slide 25 -- bilateral nodules beside a unilateral polyp. The
                    slide's own picture settles the laterality, which matters
                    because he misspoke on it aloud and corrected himself.
  tonsillitis       slide 26 -- healthy, bacterial and viral tonsils. The white
                    patches against plain red swelling live ONLY in this picture;
                    the slide text does not carry them.

Licensing: [[media_asset_licensing]] clears a course-slide image provided the
slide is cited, and says not to crop vendor marks out. The cochlear section
carries an Encyclopaedia Britannica notice and it stays visible.
"""
import os, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 1",
                   "cp-exam-1-l5-images")
DECK = os.path.expanduser(
    "~/Desktop/Semester 2/Clinical Pathophysiology I Inbox/Exam 1/"
    "5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx")

WANTED = [("ppt/media/image18.jpg", "ear-anatomy",      "jpg",  4),
          ("ppt/media/image10.png", "cochlear-section", "png",  5),
          ("ppt/media/image40.png", "otosclerosis",     "png", 10),
          ("ppt/media/image59.png", "otitis-externa",   "png", 13),
          ("ppt/media/image67.png", "meniere",          "png", 16),
          ("ppt/media/image63.png", "labyrinthitis",    "png", 17),
          ("ppt/media/image64.png", "bppv",             "png", 18),
          ("ppt/media/image89.png", "nasal-polyp",      "png", 21),
          ("ppt/media/image79.png", "deviated-septum",  "png", 22),
          ("ppt/media/image86.png", "vocal-cords",      "png", 25),
          ("ppt/media/image93.png", "tonsillitis",      "png", 26)]

# Sizes recorded at the time each file was viewed. If the deck is re-saved and
# the numbering shifts, image7.png is not going to be 223 KB -- the assertion
# catches the swap instead of silently writing the wrong picture under the right
# name, which is the failure [[image_only_slides]] warns about.
SIZES = {"ear-anatomy": 223038, "cochlear-section": 740306, "otosclerosis": 294292,
         "otitis-externa": 530257, "meniere": 349566, "labyrinthitis": 138120,
         "bppv": 165455, "nasal-polyp": 696638, "deviated-septum": 115716,
         "vocal-cords": 82873, "tonsillitis": 236610}


def main():
    assert os.path.exists(DECK), "deck not found: %s" % DECK
    os.makedirs(OUT, exist_ok=True)
    z = zipfile.ZipFile(DECK)
    names = set(z.namelist())
    for member, slug, ext, slide in WANTED:
        assert member in names, ("%s is not in the deck -- media numbering has changed, "
                                 "re-view every figure before trusting this list" % member)
        data = z.read(member)
        assert len(data) == SIZES[slug], (
            "%s is %d bytes but %r was %d when it was viewed -- the deck's media "
            "numbering has shifted. View the pictures again before rebuilding."
            % (member, len(data), slug, SIZES[slug]))
        open(os.path.join(OUT, "%s.%s" % (slug, ext)), "wb").write(data)
        print("  slide %2d  %-17s %7d bytes" % (slide, slug, len(data)))
    print("wrote %d figures to %s" % (len(WANTED), os.path.basename(OUT)))


if __name__ == "__main__":
    main()
