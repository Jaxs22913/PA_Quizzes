#!/usr/bin/env python3
"""Pull the teaching figures from the PDM Lecture 2 (Medical Imaging) deck.

Nine, out of 56. This deck is far more visual than Lecture 1's, and unlike that
one most of its images are the teaching -- a labelled radiograph does the work
three paragraphs cannot. What is left out is section-divider art, stock photos
of scanners, and the clinical images that duplicate a figure already chosen.

TWO OF THESE ARE THE ONLY SOURCE FOR THEIR CONTENT. Slide 13's Hounsfield table
and slide 21's organ-dose table exist ONLY as pictures; the deck's extracted
text has neither, and slide 21 extracts as completely empty. They drove a whole
extra pool of quiz questions once they were seen -- see pdm_l2_pool_d.py.

Slide images are cleared for use provided the slide is cited, so each carries
its deck and slide number. Every one was viewed at full size before captioning.

NOT loading="lazy" here, unlike the Lecture 1 figures: a lazy figure is absent
from the guide's own Download-as-PDF unless the reader happened to scroll past
it. theme.js now warms lazy images before printing, so the old ones are covered
too, but new figures do not need the crutch.
"""
import os, shutil
from PIL import Image

SRC = "/private/tmp/claude-501/-Users-jaxonluke/8623a091-045a-42b8-8052-ca7d2eb04188/scratchpad/pdm_l2_imgs"
OUT = ("/Users/jaxonluke/Developer/PA_Quizzes/Principles of Diagnostic Medicine I Exam 1/"
       "pdm-exam-1-l2-images")
MAXW = 900
DECK = "2. svPrinciples of Medical Imaging.pptx"

FIGURES = [
 ("s008_1.png", "five-densities", 8,
  "Table of the five basic radiographic densities with a grey-scale bar beside it, listing air, fat, fluid or soft tissue, calcium and metal, each with a description of how much x-ray it absorbs and how it appears.",
  "<b>The five basic densities, and the grey-scale bar that orders them.</b> Read the bar, not the list: air absorbs least and prints blackest, metal absorbs most and prints whitest, and everything else falls between. The row that matters for exam questions is the third &mdash; <b>fluid and soft tissue have the same density</b>, so a plain film cannot separate blood from muscle."),

 ("s013_1.png", "hounsfield-numbers", 13,
  "Table headed Tissue and Hounsfield numbers, with a grey-scale bar alongside. Air is minus 1000, fat is approximately minus 40 to minus 120, water is 0, soft tissue is approximately plus 20 to plus 100, bone is approximately plus 400 to plus 600, and metal is approximately plus 1000 or higher.",
  "<b>This table is only on the slide as a picture &mdash; there is no text version of it in the deck.</b> It is the same ordering as the five densities above, given numbers. <b>Water is zero by definition</b> and everything is placed relative to it: negative absorbs less than water and prints darker, positive absorbs more and prints brighter. Note what computed tomography buys you over a plain film &mdash; it pulls <b>water apart from soft tissue</b>, which is the asterisk on this lecture's &ldquo;Five*&rdquo;."),

 ("s010_1.png", "radiodensity-labelled", 10,
  "Pelvic radiograph with a metal hip prosthesis, annotated with three yellow labels: bone equals radiopaque, gas equals radiolucent, and metal equals very opaque.",
  "<b>Three of the five densities in one film.</b> The prosthesis is the brightest thing on the image because metal absorbs essentially the whole beam; bowel gas is the darkest because it absorbs almost none. Learn the vocabulary off this picture: <b>radiopaque</b> and <b>hyperdense</b> mean white because less of the beam got through, <b>radiolucent</b> and <b>hypodense</b> mean black because more did."),

 ("s021_1.png", "organ-doses", 21,
  "Table titled Typical Organ Radiation Doses from Various Radiologic Studies, listing study type, relevant organ and dose in milligrays or millisieverts: dental radiography brain 0.005, posterior-anterior chest radiography lung 0.01, lateral chest radiography lung 0.15, screening mammography breast 3, adult abdominal computed tomography stomach 10, barium enema colon 15, and neonatal abdominal computed tomography stomach 20.",
  "<b>The deck's extraction reports this slide as empty. It is this entire table</b>, and it is the only quantitative treatment of objective f in the lecture. Two things to take from it rather than memorising the column. First, the <b>span is four orders of magnitude</b> &mdash; a dental film and a neonatal abdominal scan are not the same conversation. Second, <b>the neonatal scan doses twice the adult one</b>: the smaller the patient, the larger the organ dose for the same study, which is the whole reason the diagnostic approach asks whether something with less radiation would do."),

 ("s039_1.png", "pa-vs-ap", 39,
  "Two chest radiographs side by side, labelled PA CHEST and AP CHEST. The heart on the AP film is visibly larger relative to the thorax than on the PA film.",
  "<b>Why the projection is named in the exam question.</b> The heart sits anteriorly, so on the posterior-anterior film it is close to the detector and its shadow is close to life size; on the anterior-posterior film it is far from the detector and is <b>magnified</b>. Read an anterior-posterior film as if it were posterior-anterior and you will call cardiomegaly that is not there. The other reasons posterior-anterior is preferred: less dose to radiation-sensitive organs, better lung fields and apices, and well-seen posterior ribs."),

 ("s029_1.png", "t1-t2-tesla", 29,
  "Nine brain magnetic resonance images in a three by three grid. Rows are 1.5 Tesla, 3 Tesla and 7 Tesla from top to bottom. The left column is T2-weighted and the middle column is T1-weighted; cerebrospinal fluid in the ventricles is bright in the left column and dark in the middle column.",
  "<b>Read this grid down the columns for weighting and across the rows for field strength.</b> The left column is T2 and the middle is T1, and the ventricles tell you which is which without reading the label: <b>on T2 water is bright, on T1 water is dark.</b> Fat, oedema, infection, blood and cerebrospinal fluid all follow water. Down the rows is 1.5 to 3 to 7 Tesla &mdash; same physics, more signal, finer detail."),

 ("s041_1.png", "decubitus-effusion", 41,
  "Two chest radiographs of the same patient. On the upright film, arrows point to blunting at the costophrenic angle; on the lateral decubitus film, arrows point to fluid that has layered out along the dependent chest wall.",
  "<b>What the decubitus view is for.</b> Lay the patient on their side and gravity moves free pleural fluid into a layer along the dependent wall, where it can be seen and measured. This is the position question with an actual answer attached: <b>decubitus equals pleural effusion</b>, as upright equals free air and air-fluid levels."),

 ("s045_1.png", "imaging-planes", 45,
  "Diagram of a standing figure with three translucent planes drawn through it, labelled coronal plane dividing front from back, sagittal plane dividing left from right, and axial or transverse plane dividing upper from lower.",
  "<b>The three planes of cross-sectional imaging.</b> Axial (transverse) divides upper from lower and is much the commonest; coronal divides anterior from posterior; sagittal divides right from left. A sagittal plane in the midline is <b>midsagittal</b> (median), and one off to either side is <b>parasagittal</b>. Pair this with the viewing convention: on a traditional axial slice you are looking at the patient's feet, so <b>their left is on your right</b>."),

 ("s048_1.png", "ultrasound-indicator", 48,
  "Two ultrasound images side by side. The left is a four-chamber cardiac view with the orientation indicator marker at the top right of the screen; the right is an abdominal view with the indicator marker at the top left.",
  "<b>The indicator is the one thing the deck calls crucial about ultrasound.</b> In cardiac imaging it belongs on the <b>right</b> of the screen; for every other ultrasound it belongs on the <b>left</b>. Get it wrong and the image is mirrored, which means left and right are swapped on a study you may be using to decide which side to drain."),
]


def main():
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    before = after = 0
    for i, (src, stem, slide, alt, cap) in enumerate(FIGURES, 1):
        sp = os.path.join(SRC, src)
        assert os.path.exists(sp), "missing extracted image %s -- re-run the pptx dump" % src
        before += os.path.getsize(sp)
        im = Image.open(sp)
        if im.mode in ("RGBA", "P", "LA"):
            bg = Image.new("RGB", im.size, (255, 255, 255)); im = im.convert("RGBA")
            bg.paste(im, mask=im.split()[-1]); im = bg
        else:
            im = im.convert("RGB")
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        fn = "%d-%s.jpg" % (i, stem)
        im.save(os.path.join(OUT, fn), "JPEG", quality=88, optimize=True, progressive=True)
        after += os.path.getsize(os.path.join(OUT, fn))
    print("figures: %d   %.2f MB -> %.2f MB" % (len(FIGURES), before / 1e6, after / 1e6))


def figure_html(dirname):
    out = {}
    for i, (src, stem, slide, alt, cap) in enumerate(FIGURES, 1):
        fn = "%d-%s.jpg" % (i, stem)
        path = os.path.join(OUT, fn); dims = ""
        if os.path.exists(path):
            with Image.open(path) as im: dims = ' width="%d" height="%d"' % im.size
        out[stem] = ('<figure class="fig"><img%s decoding="async" src="%s/%s" alt="%s">'
                     '<figcaption>%s <span class="tag">Source: %s, Slide %d.</span></figcaption></figure>'
                     % (dims, dirname, fn, alt, cap, DECK, slide))
    return out


if __name__ == "__main__":
    main()
