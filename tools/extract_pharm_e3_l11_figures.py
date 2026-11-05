#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 11 (Drugs for Pulmonary Infections, Asthma and COPD) figures for the Pharmacology I Exam 3 guide.

Deck: "Pulmonology-2.pptx" (109 slides; Adam Wood, Pharm.D., DABAT). Every slide was rendered at 1920 px and viewed,
and every picture in the deck was looked at full size. Slide images are cleared for use provided the slide is cited.
Slides 33, 69 and 90 were already in the guide (l11-slide-33/69/90.jpg, not rebuilt here).

TAKEN (file in "Pharmacology I Exam 3/pharm-e3-images/", slide, why):
  l11-slide-05-bronchitis.jpg            5   a normal bronchial tube beside an inflamed one with thick mucus.
  l11-slide-21-hap-algorithm.jpg         21  the nosocomial pneumonia algorithm. The guide already holds it as a
                                             table; the picture is the slide's own flowchart.
  l11-slide-58-asthma-inflammation.jpg   58  inflammation driving hyperresponsiveness, obstruction and symptoms.
  l11-slide-59-mast-cell-mediators.jpg   59  the mast cell's three mediator timescales. An embedded Word drawing whose
                                             only picture is a vector EMF (the deck render leaves the slide blank);
                                             drawn with tools/emf_render.py, words checked against tools/emf_text.py.
  l11-slide-60-early-late-reaction.jpg   60  the early and late asthmatic reaction (FEV1 against time, and the cells).
  l11-slide-65-asthma-severity.jpg       65  the severity classification table. It is a picture on the slide; the
                                             guide already holds it as a table; shown so students see the original.
  l11-slide-76-leukotriene-pathway.jpg   76  the leukotriene pathway (slide 61 is the same EMF drawing; shown once,
                                             beside montelukast).
  l11-slide-91-nebulizer.jpg             91  the labeled nebulizer diagram only (the slide's other picture is a stock
                                             photograph of a child using a nebulizer: left out).
  l11-slide-93-dry-powder-inhalers.jpg   93  three dry powder inhalers, cropped exactly as the slide crops the photo.
  l11-slide-94-mdi-parts.jpg             94  the metered dose inhaler parts and the spacer diagram (two pictures on
                                             the slide, joined side by side; the wikiHow mark stays).
  l11-slide-96-inhaler-technique.jpg     96  the three ways to hold the inhaler (three drawings, joined in a row).
  l11-slide-101-copd-fev1-decline.jpg    101 lung function against symptoms in chronic obstructive pulmonary disease,
                                             cropped exactly as the slide crops the screenshot it comes from (the
                                             journal caption under the chart is not on the slide and is not shown).

LEFT OUT: slide 32 (a vintage tuberculosis poster: decoration); slides 37, 40 and 43 (chemical structures);
slide 49 (an allergy clip-art poster; its trigger list is already written into the guide); slide 52 (epinephrine
auto-injector packaging, and its label prints a dose); slide 91's photograph (stock); slide 61 (duplicate of 76).
Slide 102 (the chronic obstructive pulmonary disease groups) is a real PowerPoint table, not a picture, and is
already a table in the guide. NO DOSES: none of the pictures taken shows a dose (the canister and actuator labels on
slide 94 are illegible at the deck's resolution; slide 99's albuterol rate is slide text, left out of the guide).

    python3 tools/extract_pharm_e3_l11_figures.py
"""
import os, sys
from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from extract_pharm_e3_l9_figures import INBOX, slide_blobs, slide_ole_emf, picture, side_by_side, save  # noqa: E402

DECK = os.path.join(INBOX, "Pulmonology-2.pptx")


def main():
    from emf_render import emf_to_image
    assert os.path.exists(DECK), "deck not found: %s" % DECK
    prs = Presentation(DECK)

    def pics(n, count):
        p = slide_blobs(prs, n)
        assert len(p) == count, "slide %d: expected %d pictures, found %d" % (n, count, len(p))
        return [picture(b, s) for b, _, s in p]

    def by_size(n, count, size):
        """The one picture on slide n whose original pixel size is `size` (slides with a photo beside a diagram)."""
        p = [picture(b, s) for b, _, s in slide_blobs(prs, n) if s.image.size == size]
        assert len(p) == 1 and len(slide_blobs(prs, n)) == count, "slide %d: picture %r not found" % (n, size)
        return p[0]

    save(pics(5, 1)[0], "l11-slide-05-bronchitis.jpg")
    save(pics(21, 1)[0], "l11-slide-21-hap-algorithm.jpg", 92)
    save(pics(58, 1)[0], "l11-slide-58-asthma-inflammation.jpg")
    save(emf_to_image(slide_ole_emf(DECK, 59), 1400), "l11-slide-59-mast-cell-mediators.jpg", 90)
    save(pics(60, 1)[0].resize((1200, round(1948 * 1200 / 2071))), "l11-slide-60-early-late-reaction.jpg", 82)
    save(pics(65, 1)[0], "l11-slide-65-asthma-severity.jpg", 92)
    save(emf_to_image(slide_ole_emf(DECK, 76), 1400), "l11-slide-76-leukotriene-pathway.jpg", 90)
    save(by_size(91, 2, (245, 198)), "l11-slide-91-nebulizer.jpg", 92)
    save(pics(93, 1)[0], "l11-slide-93-dry-powder-inhalers.jpg", 82)
    save(side_by_side(pics(94, 2)), "l11-slide-94-mdi-parts.jpg", 84)
    save(side_by_side(pics(96, 3), gap=20), "l11-slide-96-inhaler-technique.jpg")
    save(pics(101, 1)[0], "l11-slide-101-copd-fev1-decline.jpg")


if __name__ == "__main__":
    main()
