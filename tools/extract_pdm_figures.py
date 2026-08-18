#!/usr/bin/env python3
"""Pull the four teaching figures from the PDM Lecture 1 deck.

Four, not twenty-eight. Most of this deck's images are decorative stock photos —
a bowl of collection tubes on a gradient background, a blurry snapshot of a
Hemoccult developer bottle on someone's kitchen table. Shipping those would pad
the guide without teaching anything. What survives earns its place:

  - the order-of-draw memory jogger, which is precisely the thing Professor
    Reynolds said she wants known ("the order and sort of the broad category")
  - the matched sensitivity/specificity threshold pair, which is the only place
    the false-positive and false-negative trade-off is drawn rather than stated
  - a urinalysis dipstick being read against its chart, as the concrete example
    of a semi-quantitative point-of-care result

Slide images are cleared for use provided the slide is cited, so each carries
its deck and slide number. Every one was viewed before being captioned.
"""
import os, shutil
from PIL import Image

SRC = "/private/tmp/claude-501/-Users-jaxonluke/8623a091-045a-42b8-8052-ca7d2eb04188/scratchpad/pdm_imgs"
OUT = "/Users/jaxonluke/Developer/PA_Quizzes/Principles of Diagnostic Medicine I Exam 1/pdm-exam-1-study-guide-images"
MAXW = 900

FIGURES = [
 ("s17_1.jpg", "order-of-draw", 17,
  "Chart titled Memory Jogger for the order of draw, showing eight coloured tube stoppers left to right, each captioned with a word forming the phrase Stop Light Red Stay Put Green Light Go, and labelled beneath as sterile, light blue, red, serum separator tube, plasma separator tube, green, lavender and gray.",
  "<b>Stop &middot; Light &middot; Red &middot; Stay &middot; Put &middot; Green &middot; Light &middot; Go.</b> This is the figure to learn from this lecture. Professor Reynolds narrowed the tube objective to exactly this: <em>&ldquo;the thing I want you to know better is kind of the order and sort of the broad category.&rdquo;</em> Sterile (blood culture) first, coagulation second, non-additive next, then the additive tubes. The reason the sequence exists is to stop additive from one tube carrying into the next and corrupting the result."),

 ("s43_1.png", "threshold-sensitivity", 43,
  "Scatter plot with test results on the vertical axis and two groups on the horizontal axis, no disease and disease. A dashed horizontal threshold line is drawn low; a circled cluster of no-disease points sitting above it is labelled false-positives. Annotation states the line is drawn to maximize sensitivity, identifying all those with disease correctly.",
  "<b>A threshold drawn to maximize sensitivity.</b> Push the line down until every diseased patient falls above it and you catch them all &mdash; at the cost of sweeping in the healthy people circled here as <b>false positives</b>. This is SnNout made visual: a negative result now genuinely rules out."),

 ("s43_2.png", "threshold-specificity", 43,
  "The same scatter plot of test results for no disease and disease groups, with the dashed threshold line drawn higher. A circled cluster of disease points sitting below the line is labelled false-negatives. Annotation states the line is drawn to maximize specificity, identifying all those without disease correctly.",
  "<b>The same data, the threshold moved up.</b> Now no healthy patient is above the line, so a positive genuinely rules in &mdash; SpPin &mdash; but the circled diseased patients below it are missed as <b>false negatives</b>. Read this against the figure above: it is one dataset and one dial. You cannot maximize both, which is why a sensitive test screens and a specific test confirms."),

 ("s30_1.png", "urinalysis-dipstick", 30,
  "Gloved hands holding a urinalysis reagent strip beside a specimen cup of urine, comparing the strip's coloured pads against the printed colour chart on the reagent bottle.",
  "A <b>semi-quantitative</b> point-of-care result. The pads are matched against the chart on the bottle rather than read by a machine, which puts urinalysis between the purely qualitative tests (rapid strep, pregnancy &mdash; positive or negative) and the quantitative ones that need a reader (glucose, cardiac markers)."),
]


def main():
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    before = after = 0
    for i, (src, stem, slide, alt, cap) in enumerate(FIGURES, 1):
        sp = os.path.join(SRC, src); before += os.path.getsize(sp)
        im = Image.open(sp)
        if im.mode in ("RGBA","P","LA"):
            bg = Image.new("RGB", im.size, (255,255,255)); im = im.convert("RGBA")
            bg.paste(im, mask=im.split()[-1]); im = bg
        else:
            im = im.convert("RGB")
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height*MAXW/im.width)), Image.LANCZOS)
        im.save(os.path.join(OUT, "%d-%s.jpg" % (i, stem)), "JPEG", quality=88, optimize=True, progressive=True)
        after += os.path.getsize(os.path.join(OUT, "%d-%s.jpg" % (i, stem)))
    print("figures: %d   %.2f MB -> %.2f MB" % (len(FIGURES), before/1e6, after/1e6))


def figure_html(dirname):
    out = {}
    for i, (src, stem, slide, alt, cap) in enumerate(FIGURES, 1):
        fn = "%d-%s.jpg" % (i, stem)
        path = os.path.join(OUT, fn); dims = ""
        if os.path.exists(path):
            with Image.open(path) as im: dims = ' width="%d" height="%d"' % im.size
        out[stem] = ('<figure class="fig"><img%s loading="lazy" src="%s/%s" alt="%s">'
                     '<figcaption>%s <span class="tag">Source: 1. Principles of Laboratory '
                     'Diagnostics sv.pptx, Slide %d.</span></figcaption></figure>'
                     % (dims, dirname, fn, alt, cap, slide))
    return out


if __name__ == "__main__":
    main()
