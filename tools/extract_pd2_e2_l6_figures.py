#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the teaching figures out of the PD2 Lecture 6 deck (Advanced Thorax and Lung
Physical Examination, Crowe) for the Exam 2 guide, and cut the quiz pictures.

The deck carries 24 pictures across 65 slides. All of them were VIEWED before any was
chosen ([[image_only_slides]]); each is named for what is IN it. Pictures are matched by
an MD5 prefix of their bytes, so a re-saved deck that renumbers its media fails loudly
instead of writing the wrong picture under the right name (the Lecture 5 extractor's rule).

SLIDES WHOSE CONTENT LIVES IN THE PICTURE (read by eye):
  6   the vertical reference lines (midsternal, midclavicular, the three axillary lines,
      scapular and vertebral) are named only in the photographs
  32  the eight breathing patterns, each with its tracing and definition -- and its own
      printed "Source discrepancy" line (12-18 against about 14-20 per minute)
  36-38 the chest wall deformities: each drawing carries its definition as a caption
  45  the four normal breath sounds: duration, intensity, pitch and where heard
  56  normal against consolidated lung: breath sounds, transmitted voice sounds, fremitus,
      and the two notes on the hyperinflated lung and on pleural effusion

LEFT OUT, and why:
  9   "The anatomy of the bronchial tree", a social-media infographic credited to an
      individual account; every fact on it is in the slide's own text
  45  (second picture) a small labeled waveform key that repeats the table beside it

QUIZ PICTURES (pd2-exam-2-quiz-images/l6-fig-NN.jpg, numbered in the fixed order of QUIZ
below; a quiz picture's file name never states its answer) are cropped so the printed name and
caption do not answer the question: the "Normal"/"Clubbed" titles (slide 26), the panel
title and definition (slide 32), the deformity names and definitions (slides 36-38). They
are enlarged 2x because the deck's copies are small.

Licensing: [[media_asset_licensing]] clears a course-slide image provided the slide is
cited. Publisher marks baked into the pixels (Healthwise on slide 10) stay visible.

    python3 tools/extract_pd2_e2_l6_figures.py
"""
import hashlib, io, os
from pptx import Presentation
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EXAM = os.path.join(ROOT, "Physical Diagnosis 2 Exam 2")
OUT = os.path.join(EXAM, "pd2-exam-2-study-guide-images")
QOUT = os.path.join(EXAM, "pd2-exam-2-quiz-images")
DECK_NAME = "6. Thorax - Dr. Crowe.pptx"
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Physical Diagnosis 2 Inbox/Exam 2/" + DECK_NAME)

# (slide, md5 prefix, stem, alt text, caption)
FIGURES = [
 (3, "b8ade0", "anterior-landmarks",
  "Front view of a torso with the rib cage drawn in, labeled suprasternal notch, manubrium, sternal angle, body of sternum, xiphoid process, 2nd rib, 2nd rib interspace, 2nd costal cartilage, costochondral junctions and costal angle.",
  "The anterior landmarks. The <b>sternal angle</b> sits beside the <b>2nd rib</b>, so the space just below it is the 2nd intercostal space; count down from there. Each intercostal space takes the number of the rib above it."),
 (4, "25a9bf", "anterior-ribs",
  "Front view of the chest with the ribs numbered 1 to 10 and the intercostal spaces numbered between them, the sternal angle (angle of Louis) labeled, and T4 marked on the sternum.",
  "Ribs and spaces numbered from the front. The <b>sternal angle (angle of Louis)</b> marks the 2nd rib and lines up with <b>T4</b>, the lower margin for an endotracheal tube on a chest x-ray."),
 (5, "a3ae1e", "posterior-ribs",
  "Back view of the chest with the ribs and intercostal spaces numbered down to 12, the spinous processes of C7 and T1 labeled, and the 7th rib at the inferior angle of the scapula.",
  "The posterior count. The <b>inferior angle of the scapula</b> lies at about the <b>7th rib</b>; the thoracentesis needle goes into the 7th intercostal space, immediately above the 8th rib."),
 (6, "a14784", "lines-anterior",
  "A man's chest with three vertical lines drawn on it, labeled midsternal line, midclavicular line and anterior axillary line.",
  "Anterior lines: <b>midsternal</b>, <b>midclavicular</b>, <b>anterior axillary</b>."),
 (6, "2e739a", "lines-lateral",
  "A man's side with his arm raised and three vertical lines labeled anterior axillary, midaxillary and posterior axillary line.",
  "Lateral lines: <b>anterior axillary</b>, <b>midaxillary</b>, <b>posterior axillary</b>."),
 (6, "b5e76f", "lines-posterior",
  "A man's back with two vertical lines labeled scapular line and vertebral line.",
  "Posterior lines: <b>scapular</b> and <b>vertebral</b>."),
 (7, "b48fb8", "triangle-of-safety",
  "A patient lying with the arm raised; shaded areas mark the pectoralis major in front and the latissimus dorsi behind, with the triangle of safety between them above the numbered 4th to 7th ribs.",
  "The <b>triangle of safety</b> in the midaxillary line: the lateral border of the <b>pectoralis major</b> in front, the lateral border of the <b>latissimus dorsi</b> behind, and the nipple line (4th or 5th intercostal space) below. The safe position for a chest tube."),
 (8, "8d7c6e", "lobes-anterior",
  "Front view of a man's chest with the lungs drawn on it: right upper, middle and lower lobes and left upper and lower lobes, the apex of the lung, the horizontal fissure and the oblique fissure labeled.",
  "From the front: the right lung shows three lobes, the left two. The <b>apex</b> rises above the clavicle, and the <b>horizontal fissure</b> sets off the right middle lobe."),
 (8, "10a497", "lobes-right-lateral",
  "Right side view of a man's chest with the right upper, middle and lower lobes drawn in.",
  "The right side: the middle lobe sits in front, below the horizontal fissure."),
 (8, "927c1c", "lobes-left-lateral",
  "Left side view of a man's chest with the left upper and lower lobes and the left oblique fissure labeled.",
  "The left side: two lobes and the <b>left oblique fissure</b>. There is no left middle lobe."),
 (8, "78c406", "lobes-posterior",
  "Back view of a man's chest with the lungs drawn in, labeled left and right upper and lower lobes, the spinous process of T3, and dashed outlines of the inspiratory descent below each base.",
  "From behind, almost all lower lobe. The oblique fissures start near <b>T3</b>; the dashed lines show how far the bases descend on inspiration."),
 (10, "f85815", "pleurae",
  "Drawing of the lungs in a torso with a magnified circle showing the lung surface, the visceral pleura on it, the pleural space, and the parietal pleura outside it.",
  "The two pleural layers. The <b>visceral pleura</b> on the lung lacks sensory nerves; the <b>parietal pleura</b> lining the chest wall and diaphragm is highly innervated, so irritating it causes pleuritic pain."),
 (26, "b71115", "clubbing",
  "Two fingertips in profile, labeled normal and clubbed, each crossed by two measurement lines; the clubbed one has a bulbous, swollen nail base.",
  "<b>Clubbing</b> (right) beside a normal finger (left): the soft tissue at the nail base swells and the normal angle between the nail and the proximal nail fold is lost."),
 (32, "5637f3", "breathing-patterns",
  "Chart of eight breathing tracings with definitions: normal, bradypnea, tachypnea, rapid deep breathing, Cheyne-Stokes breathing, ataxic (Biot) breathing, sighing respiration and obstructive breathing.",
  "The eight breathing patterns. Note the slide's own line at the bottom: the text gives 12&ndash;18 breaths per minute as normal, the table about 14&ndash;20."),
 (36, "c8d062", "chest-normal",
  "Outline of a normal chest cross-section, wider than it is deep, beside a man's chest in side view, with a caption on the normal adult ratio.",
  "The <b>normal adult</b> chest is wider than it is deep: the anteroposterior to lateral ratio is about 0.7 up to 0.9, and it rises with age."),
 (36, "2ad61a", "chest-barrel",
  "Almost round chest cross-section beside a deep-chested man in side view, captioned barrel chest.",
  "<b>Barrel chest</b>: increased anteroposterior diameter. Normal in infancy; often accompanies aging and chronic obstructive pulmonary disease."),
 (37, "0b6a0f", "chest-pigeon",
  "Chest cross-section pointed at the front, with the anteriorly displaced sternum and depressed costal cartilages labeled, beside a boy's chest, captioned pigeon chest.",
  "<b>Pigeon chest (pectus carinatum)</b>: the sternum is displaced forward and the costal cartilages beside it are depressed."),
 (37, "d9e80c", "chest-funnel",
  "Chest cross-section dipped in at the front, beside a young man's chest with a hollow over the lower sternum, captioned funnel chest.",
  "<b>Funnel chest (pectus excavatum)</b>: a depression in the lower sternum. Compression of the heart and great vessels may cause murmurs."),
 (38, "b01ff7", "chest-flail-kyphoscoliosis",
  "Two drawings: a chest cross-section whose dashed inspiratory outline caves inward on one side, captioned traumatic flail chest, and a bent-forward back with a curved spine, captioned thoracic kyphoscoliosis.",
  "<b>Traumatic flail chest</b> (left): the fractured segment caves in on inspiration and moves out on expiration. <b>Thoracic kyphoscoliosis</b> (right): the deformed chest distorts the lungs and makes findings hard to interpret."),
 (43, "b86d8d", "diaphragmatic-excursion",
  "A man's bare back with two percussed levels of dullness marked, a shaded band with arrows on one side and a single line on the other, both labeled dull.",
  "<b>Diaphragmatic excursion</b>: percuss down to dullness at full expiration and at full inspiration, mark each, and measure between them."),
 (45, "d4b714", "breath-sounds",
  "Table of the four breath sounds, vesicular, bronchovesicular, bronchial and tracheal, each with a waveform and its duration, intensity, pitch and where it is heard normally.",
  "The four normal breath sounds. Read the waveforms as inspiration up, expiration down: <b>vesicular</b> has the long inspiration, <b>bronchial</b> the long expiration, and the other two are about equal."),
 (56, "96a909", "consolidation-table",
  "Two-column table comparing a normal air-filled lung with a consolidated airless lung in lobar pneumonia, each with a drawing and an x-ray, and rows for breath sounds, transmitted voice sounds and tactile fremitus, with notes on obstructive lung disease and pleural effusion.",
  "Normal against consolidated lung, side by side. Consolidation turns every transmitted finding UP: bronchial sounds, &ldquo;ee&rdquo; heard as &ldquo;ay&rdquo;, louder spoken and whispered words, increased fremitus. The notes under it turn them DOWN for the hyperinflated lung and for an effusion."),
]

# (slide, md5 prefix, quiz file, crop box in source pixels)
QUIZ = [
 (26, "b71115", "l6-fig-01.jpg", (0, 22, 354, 218)),
 (32, "5637f3", "l6-fig-02.jpg", (20, 590, 412, 760)),
 (36, "2ad61a", "l6-fig-03.jpg", (0, 0, 282, 185)),
 (37, "d9e80c", "l6-fig-04.jpg", (0, 0, 244, 128)),
 (37, "0b6a0f", "l6-fig-05.jpg", (0, 0, 245, 156)),
 (38, "b01ff7", "l6-fig-06.jpg", (0, 0, 282, 122)),
 (43, "b86d8d", "l6-fig-07.jpg", None),
]

MAX_W = 760


def _load():
    assert os.path.exists(DECK), "deck not found: %s" % DECK
    p = Presentation(DECK)
    blobs = {}
    for i, sl in enumerate(p.slides, 1):
        for rel in sl.part.rels.values():
            if "image" in rel.reltype and not rel.is_external:
                b = rel.target_part.blob
                blobs[(i, hashlib.md5(b).hexdigest()[:6])] = b
    return blobs


def _flat(b):
    im = Image.open(io.BytesIO(b))
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, "white")
        bg.paste(im, mask=im.split()[-1])
        return bg
    return im.convert("RGB")


def _name(n, stem):
    return "l6-%02d-%s.jpg" % (n, stem)


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(QOUT, exist_ok=True)
    blobs = _load()
    want = [(s, h) for s, h, *_ in FIGURES] + [(s, h) for s, h, *_ in QUIZ]
    missing = [k for k in want if k not in blobs]
    assert not missing, ("pictures not found by content hash -- the deck changed; view every "
                         "figure again before trusting this list: %r" % missing)
    stems = [st for _s, _h, st, _a, _c in FIGURES]
    assert len(stems) == len(set(stems)), "duplicate stem"
    total = 0
    for n, (s, h, stem, _a, _c) in enumerate(FIGURES, 1):
        im = _flat(blobs[(s, h)])
        if im.width > MAX_W:
            im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
        path = os.path.join(OUT, _name(n, stem))
        im.save(path, "JPEG", quality=86, optimize=True, progressive=True)
        total += os.path.getsize(path)
        print("  slide %3d  %-30s %4dx%-4d %6d bytes" % (s, stem, im.width, im.height, os.path.getsize(path)))
    print("wrote %d guide figures, %d KB, to %s" % (len(FIGURES), total // 1024, OUT))
    for s, h, fn, box in QUIZ:
        im = _flat(blobs[(s, h)])
        if box:
            im = im.crop(box)
        if im.width < 400:
            im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
        path = os.path.join(QOUT, fn)
        im.save(path, "JPEG", quality=86, optimize=True, progressive=True)
        print("  quiz  slide %3d  %-26s %4dx%-4d" % (s, fn, im.width, im.height))


def figure_html(dirname):
    """The <figure> blocks, keyed by stem, for the guide add script."""
    out = {}
    for n, (slide, _h, stem, alt, cap) in enumerate(FIGURES, 1):
        fn = _name(n, stem)
        path = os.path.join(OUT, fn)
        dims = ""
        if os.path.exists(path):
            with Image.open(path) as im:
                dims = ' width="%d" height="%d"' % im.size
        out[stem] = ('<figure class="fig"><img%s loading="lazy" src="%s/%s" alt="%s">'
                     '<figcaption>%s <span class="tag">Source: %s, Slide %d.</span>'
                     '</figcaption></figure>' % (dims, dirname, fn, alt, cap, DECK_NAME, slide))
    return out


if __name__ == "__main__":
    main()
