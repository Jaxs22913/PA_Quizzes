#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the teaching figures out of the PD2 Lecture 7 deck (The Advanced Hematological
Physical Examination, Matthew Ward, DMSc, MBA, PA-C) for the Exam 2 guide, and cut the
quiz pictures.

The deck carries 37 pictures across 56 slides. All of them were VIEWED (each slide rendered
through Keynote at 1920 px, and each picture on its own) before any was chosen
([[image_only_slides]]); each is named for what is IN it. Pictures are matched by an MD5
prefix of their bytes, so a re-saved deck that renumbers its media fails loudly.

The crops PowerPoint applies on the slide are applied here too (CROP), so the guide shows
what the slide shows: slide 30's picture hides a typed caption under its visible part,
slide 42's shows only the phalangeal depth panel, slide 20's trims a logo corner.

LEFT OUT, and why:
  1   cartoon stomach on the title slide
  4   a clip-art figure (the three causes of blood loss are icons + words on the slide)
  7, 56  decorative photographs (compass, briefcase of books)
  45  the two stool blood test kit photographs (a product box and a card; the slide's text
      says what matters about the test)
  55  a "Symptoms of anemia" body diagram that is attached to the slide file but NOT on the
      slide (no shape places it; the Keynote render shows text only): not visible, so not used

QUIZ PICTURES (pd2-exam-2-quiz-images/l7-fig-NN.jpg) are numbered in the fixed order of QUIZ
below; a quiz picture's file name never states its answer ([[quiz_image_filenames]]). None of
the chosen pictures carries a printed name of its finding (the slide titles are separate text).

Licensing: [[media_asset_licensing]] clears a course-slide image provided the slide is cited.
Publisher marks baked into the pixels (Mayo Foundation on slide 28, Elsevier on slide 30) stay.

    python3 tools/extract_pd2_e2_l7_figures.py
"""
import hashlib, io, os
from pptx import Presentation
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EXAM = os.path.join(ROOT, "Physical Diagnosis 2 Exam 2")
OUT = os.path.join(EXAM, "pd2-exam-2-study-guide-images")
QOUT = os.path.join(EXAM, "pd2-exam-2-quiz-images")
DECK_NAME = "Anemia-PDII-Ward-STUDENT-COPY-Updated.pptx"
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Physical Diagnosis 2 Inbox/Exam 2/" + DECK_NAME)

# md5 prefix -> (left, top, right, bottom) fractions cut off, as on the slide
CROP = {
    "9f91be": (0.094, 0.0, 0.0, 0.09),
    "8bcd15": (0.059, 0.007, 0.034, 0.258),
    "389648": (0.0, 0.485, 0.0, 0.0),
    "2ab4ef": (0.0, 0.0, 0.0, 0.16),     # the face photo's own "Jaundice" tag along its lower edge
}

# (slide, md5 prefix, stem, alt text, caption)
FIGURES = [
 (17, "de79de", "palmar-pallor",
  "Two open palms side by side; the hand on the left is much paler than the pink hand on the right.",
  "<b>Palmar pallor</b> (left) beside a normal palm. Pallor is looked for in the conjunctivae, oral mucosa, "
  "palms and nail beds; it suggests anemia but is an <b>unreliable estimate of the hemoglobin</b>."),
 (18, "2ab4ef", "jaundice-face",
  "Close view of an older man's face; the skin is distinctly yellow.",
  "<b>Jaundice</b> of the skin of the face."),
 (18, "e7b943", "jaundice-hands",
  "Two hands, one resting on the other's forearm; the skin of the forearm is yellow.",
  "Yellow skin of the forearm and hands in <b>jaundice</b>."),
 (18, "bd47be", "jaundice-legs",
  "A patient's lower legs and feet on a bed sheet; the skin is yellow.",
  "<b>Jaundice</b> is easy to see against white bed linen."),
 (19, "9ea110", "scleral-icterus",
  "Close view of a woman's eyes; the whites of the eyes are yellow.",
  "<b>Scleral icterus</b>: yellow sclerae. With jaundice it points to <b>hemolytic anemia, including sickle "
  "cell disease</b>, though disorders of bilirubin metabolism also cause it."),
 (20, "9f91be", "hair-shedding",
  "The top of a woman's head with visibly thinned hair along the part.",
  "<b>Hair shedding</b>: a possible sign of iron deficiency, but it has multiple other causes."),
 (22, "1aae2b", "nail-ridging",
  "Three fingertips with pale, flattened nails crossed by fine lengthwise ridges.",
  "Flattened nails with <b>longitudinal ridging</b>: nonspecific."),
 (23, "919cf6", "nail-ridging-close",
  "A thumbnail close up, covered with fine lengthwise ridges.",
  "<b>Longitudinal ridging</b> close up. Brittle nails, flattening and ridging are <b>nonspecific</b>."),
 (24, "b09201", "koilonychia",
  "A thumb seen from the side; the nail is thin and dished upward like a spoon.",
  "<b>Koilonychia</b>: thin, concave, spoon-shaped nails, associated with <b>iron deficiency</b>. Nail findings "
  "are supporting clues; they cannot tell you the cause or the severity."),
 (26, "26e670", "petechiae-purpura",
  "Lower legs covered with small red spots; one tiny pinpoint spot is circled and labeled petechiae, and a larger spot is circled and labeled purpura.",
  "<b>Petechiae</b> are pinpoint, nonblanching skin hemorrhages; <b>purpura</b> are larger nonblanching lesions."),
 (27, "6977c4", "petechiae-leg",
  "The side of a lower leg scattered with many small red pinpoint spots.",
  "<b>Petechiae</b> on the leg (the slide notes this patient had regional enteritis, Crohn&rsquo;s disease)."),
 (28, "251ba5", "purpura-legs",
  "Both lower legs and feet covered with large, merging dark red patches.",
  "Extensive <b>purpura</b> of both legs."),
 (30, "8bcd15", "conjunctival-pallor",
  "A lower eyelid pulled down to show a pale, almost white inner lining.",
  "<b>Pallor of the palpebral conjunctiva</b>: pull the lower lid down and look at its lining."),
 (31, "809d91", "pale-gums",
  "Front view of teeth and gums; the gums are very pale.",
  "<b>Pale gums</b> (oral mucosal pallor)."),
 (31, "ac5cd8", "normal-gingiva",
  "Front view of teeth and gums; the gums are a healthy pink-red.",
  "<b>Normal gingiva</b> for comparison."),
 (32, "d4a59d", "palatal-petechiae",
  "An open mouth showing the roof of the mouth, with a cluster of small red dots on the soft palate.",
  "<b>Palatal petechiae</b>: mucosal bleeding is looked for in the mouth along with pallor."),
 (34, "bc80ba", "glossitis",
  "A protruded tongue that is smooth, glossy and beefy red.",
  "<b>Glossitis</b>: a smooth, sore, beefy-red tongue. Possible iron, B12 or folate deficiency; "
  "<b>nonspecific</b> for any one of them."),
 (35, "361b78", "angular-cheilitis",
  "Close view of a woman's closed lips with pale, cracked fissures at both corners of the mouth.",
  "<b>Angular cheilitis</b>: inflammation and fissures at the corners of the mouth."),
 (35, "06c482", "cheilitis-close",
  "Close view of the corner of a mouth, red and crusted with flaking skin.",
  "<b>Cheilosis / cheilitis</b> close up. Causes include nutritional deficiency, <i>Candida</i>, bacteria and local irritation."),
 (39, "5fa067", "clubbing-hands",
  "The backs of two hands; every fingertip is broad and bulbous with curved nails.",
  "<b>Digital clubbing</b>. It is <b>atypical for uncomplicated anemia</b>: look for an underlying cardiopulmonary, "
  "gastrointestinal or other systemic disorder."),
 (40, "d951f0", "nail-fold-angle",
  "A finger seen from the side with two colored lines drawn along the nail and the skin of the nail fold, meeting at an angle.",
  "<b>Nail-fold profile angle</b>: normal under 180&deg;, clubbing over 180&deg;."),
 (41, "8b268c", "schamroth",
  "Two pairs of fingers held back to back, labeled normal and clubbed; the normal pair leaves a small diamond-shaped gap between the nails, the clubbed pair does not.",
  "<b>Schamroth&rsquo;s window</b>: hold the backs of matching fingers together. A normal pair leaves a small "
  "diamond-shaped window; in clubbing it is gone."),
 (42, "389648", "phalangeal-depth",
  "Two fingers in profile, labeled normal and clubbed, each marked DPD at the nail base and IPD at the end joint.",
  "<b>Phalangeal depth ratio</b>: the distal phalangeal depth (DPD) against the interphalangeal depth (IPD). "
  "In the clubbed finger the nail-base depth is the greater."),
 (48, "b1b434", "cullen",
  "A patient's lower abdomen with a dark purple bruise around the navel.",
  "<b>Cullen sign</b>: periumbilical ecchymosis, from internal bleeding."),
 (49, "3387ab", "grey-turner",
  "A patient lying on one side with several purple bruises across the flank.",
  "<b>Grey Turner sign</b>: flank ecchymosis, from retroperitoneal or intra-abdominal bleeding."),
 (51, "71fe38", "spinal-cord-b12",
  "Stained cross-section of the spinal cord with pale areas in the posterior and lateral white matter.",
  "Spinal cord in <b>B12 deficiency</b>: the posterior columns (vibration and position sense) and the lateral "
  "corticospinal tracts (spasticity, hyperreflexia) are affected."),
 (53, "4a08f2", "romberg",
  "A man standing upright with his feet together and his eyes closed while a clinician stands beside him with her arms ready to catch him.",
  "<b>Romberg testing</b>, with the examiner guarding against a fall. Greater instability with the eyes closed "
  "suggests impaired proprioception."),
]

# (slide, md5 prefix, quiz file, crop box in source pixels after CROP)
QUIZ = [
 (24, "b09201", "l7-fig-01.jpg", None),
 (32, "d4a59d", "l7-fig-02.jpg", None),
 (34, "bc80ba", "l7-fig-03.jpg", None),
 (35, "361b78", "l7-fig-04.jpg", None),
 (48, "b1b434", "l7-fig-05.jpg", None),
 (49, "3387ab", "l7-fig-06.jpg", None),
 (19, "9ea110", "l7-fig-07.jpg", None),
 (30, "8bcd15", "l7-fig-08.jpg", None),
 (27, "6977c4", "l7-fig-09.jpg", None),
 (53, "4a08f2", "l7-fig-10.jpg", None),
 (17, "de79de", "l7-fig-11.jpg", None),
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


def _flat(b, h):
    im = Image.open(io.BytesIO(b))
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, "white")
        bg.paste(im, mask=im.split()[-1])
        im = bg
    else:
        im = im.convert("RGB")
    if h in CROP:
        l, t, r, btm = CROP[h]
        W, H = im.size
        im = im.crop((round(W * l), round(H * t), round(W * (1 - r)), round(H * (1 - btm))))
    return im


def _name(n, stem):
    return "l7-%02d-%s.jpg" % (n, stem)


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
        im = _flat(blobs[(s, h)], h)
        if im.width > MAX_W:
            im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
        path = os.path.join(OUT, _name(n, stem))
        im.save(path, "JPEG", quality=86, optimize=True, progressive=True)
        total += os.path.getsize(path)
        print("  slide %3d  %-22s %4dx%-4d %6d bytes" % (s, stem, im.width, im.height, os.path.getsize(path)))
    print("wrote %d guide figures, %d KB, to %s" % (len(FIGURES), total // 1024, OUT))
    for s, h, fn, box in QUIZ:
        im = _flat(blobs[(s, h)], h)
        if box:
            im = im.crop(box)
        if im.width > MAX_W:
            im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
        if im.width < 400:
            im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
        path = os.path.join(QOUT, fn)
        im.save(path, "JPEG", quality=86, optimize=True, progressive=True)
        print("  quiz  slide %3d  %-14s %4dx%-4d" % (s, fn, im.width, im.height))


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
