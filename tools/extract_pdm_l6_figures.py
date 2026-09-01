#!/usr/bin/env python3
"""Pull the Lecture 6 (Urinalysis) figures worth carrying into the guide.

Three earn their place. The colour wheel and the reagent strip chart are the
lecture's two reference images -- the strip chart in particular carries the
per-analyte READING TIMES, which appear nowhere in the slide text and are the
whole reason slide 11 says the timing "differs among analytes". The nephron
supports the anatomy review.

The colour figure also settles a transcription artifact: the recording renders
the red-urine food as "beans"; the figure says BEETS, along with blueberries
and rhubarb. The picture wins.
"""
import os, re, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1")
OUT = os.path.join(DIR, "pdm-exam-1-l6-images")
DECK = os.path.expanduser(
    "~/Desktop/Semester 2/Principles of Diagnostic Medicine I Inbox/Exam 1/"
    "6. Urinalysis Diagnostics SV Gopal Fall 2026.pptx")

WANT = {"image3.jpeg": "urine-colour", "image6.png": "reagent-strip-chart",
        "image8.jpg": "nephron"}

os.makedirs(OUT, exist_ok=True)
z = zipfile.ZipFile(DECK)
for src, slug in WANT.items():
    path = "ppt/media/" + src
    assert path in z.namelist(), "deck is missing %s" % src
    ext = os.path.splitext(src)[1]
    dest = os.path.join(OUT, slug + ext)
    open(dest, "wb").write(z.read(path))
    print("wrote %s (%d KB)" % (os.path.basename(dest), os.path.getsize(dest) // 1024))
