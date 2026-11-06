#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Pulmonary OSCE chart's test pictures out of the course decks (and
the one Wikimedia Commons file) into the clean folder outside the repo.

Every picture is taken from the slide that LABELS it as its finding (the slide
title or the picture's own label); _pd2_pulm_osce_images.py holds the citation,
caption and yellow-box coordinates for each. The clean copies are never boxed:
tools/box_pd2_pulm_osce_images.py draws the boxes from them into the site
folder, so a re-run never boxes a picture twice.

A slide's pictures are picked by their pixel size, not by relationship id
(a deck's .rels order is not the reading order). Tiny pictures are enlarged so
the boxes and the finding stay readable; that is said in the credit line.

    python3 tools/extract_pd2_pulm_osce_images.py [--out DIR]
"""
import argparse, io, os, urllib.request
from pptx import Presentation
from PIL import Image

INBOX = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2")
CMS6 = INBOX + "/Clinical Medicine and Surgery I Inbox/Exam 6/"
CMS7 = INBOX + "/Clinical Medicine and Surgery I Inbox/Exam 7/"
PDM3 = INBOX + "/Principles of Diagnostic Medicine I Inbox/Exam 3/"
PDM4 = INBOX + "/Principles of Diagnostic Medicine I Inbox/Exam 4/"
CLEAN = INBOX + "/Physical Diagnosis 2 Inbox/Pulm OSCE images (clean)"

DECKS = {
    "L35": CMS6 + "PAJ5500 CMSI Asthma MBF 2026sc.pptx",
    "L36": CMS6 + "37. svCOPD 2026.pptx",
    "L37": CMS6 + "37. Respiratory Infections - Bobilin - 10-29-2026 SV.pptx",
    "L38": CMS6 + "38. Mycobacterial Infections including Tuberculosis - Bobilin - 10-29-2025 SV.pptx",
    "L40": CMS7 + "CMS I Obstructive Sleep Apnea & Obesity Hypoventilation Syndrome - Shah Fallsv.pptx",
    "L41": CMS7 + "Inflammatory Lung Disease 2026.pptx",
    "L43": CMS7 + "Pulmonary Nodules and Neoplasms 2026.pptx",
    "L44": CMS7 + "Pleural Disorders 2026.pptx",
    "PDM14": PDM3 + "14. EKG Axis, BBB.pptx",
    "PDM16": PDM3 + "16. EKG Pericarditis Electrolytes and Other Abnormalities.pptx",
    "PDM17": PDM4 + "17. Pulmonary Imaging - Prof. Fowler (GUEST).pptx",
}
COMMONS = {
    "cxr-ards.jpg":
        "https://upload.wikimedia.org/wikipedia/commons/b/bb/AARDS_X-ray_cropped.jpg",
}

# out file -> (deck, slide, [(w, h) of each picture used], options)
#   crop:  (x0, y0, x1, y1) on the picture before scaling
#   scale: enlarge small pictures (Lanczos)
#   join:  several pictures side by side, top-aligned on white
SPECS = {
    "spirometry-normal-vs-asthma.png":     ("L35", 56, [(1521, 1030)], {}),
    "peak-flow-meter-and-normal-values.png": ("L35", 61, [(771, 390)], {"scale": 1.5}),
    "spirometry-obstructive-copd.png":     ("L36", 28, [(650, 377)], {"scale": 1.6}),
    "cxr-copd-hyperinflation.jpg":         ("L36", 31, [(520, 605)], {"scale": 1.5}),
    "stop-bang-questionnaire.png":         ("L40", 17, [(594, 570)], {"scale": 1.4}),
    "cxr-influenza-pneumonia.jpg":         ("L37", 106, [(241, 209)], {"scale": 2.5}),
    "cxr-normal.jpg":                      ("PDM17", 80, [(640, 480)], {"crop": (50, 128, 302, 402), "scale": 2.2}),
    "cxr-right-upper-lobe-consolidation.jpg": ("L37", 35, [(960, 720)], {}),
    "ct-consolidation.jpg":                ("PDM17", 79, [(823, 692)], {}),
    "tuberculin-skin-test-reading.jpg":    ("L38", 20, [(252, 350)], {"scale": 2}),
    "cxr-tuberculosis-bilateral.jpg":      ("L38", 31, [(1032, 1006)], {}),
    "hrct-honeycombing.jpg":               ("L41", 36, [(425, 436)], {"scale": 2}),
    "pft-restrictive-pattern.png":         ("L41", 29, [(678, 593), (662, 529)], {"join": True}),
    "cxr-hilar-adenopathy.jpg":            ("L41", 28, [(1012, 863)], {}),
    "ct-hypersensitivity-pneumonitis.jpg": ("L41", 70, [(1000, 780)], {}),
    "histology-granulomas.jpg":            ("L41", 70, [(795, 1106)], {}),
    "ct-lung-tumor.jpg":                   ("L43", 34, [(400, 329)], {"scale": 2}),
    "pet-ct-nodule.jpg":                   ("L43", 17, [(702, 507)], {"scale": 1.4}),
    "ecg-right-ventricular-hypertrophy.jpg": ("PDM14", 34, [(1200, 557)], {}),
    "cxr-pulmonary-edema.jpg":             ("PDM17", 82, [(553, 553)], {"scale": 1.6}),
    "ecg-pulmonary-embolism.jpg":          ("PDM16", 50, [(797, 442)], {"scale": 1.6}),
    "vq-scan-and-ct-angiogram.jpg":        ("PDM17", 61, [(492, 1090)], {}),
    "cxr-pleural-effusion.jpg":            ("L44", 90, [(600, 564)], {"scale": 1.5}),
    "cxr-pneumothorax.jpg":                ("L44", 27, [(1004, 940)], {}),
    "ct-pneumothorax.jpg":                 ("L44", 33, [(1800, 1800)], {"scale": 0.5}),
    "cxr-hemopneumothorax.jpg":            ("L44", 72, [(1219, 1195)], {}),
}


def slide_pictures(prs, n):
    """Every picture a slide references (picture shapes and picture fills), by pixel size."""
    s = prs.slides[n - 1]
    out = {}
    for b in s._element.xpath('.//a:blip'):
        rid = b.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
        if not rid:
            continue
        try:
            im = Image.open(io.BytesIO(s.part.related_part(rid).blob))
            im.load()
        except Exception:
            continue
        out.setdefault(im.size, im)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=CLEAN)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    cache = {}
    for fn, (deck, slide, sizes, opt) in SPECS.items():
        prs = cache.get(deck) or cache.setdefault(deck, Presentation(DECKS[deck]))
        pics = slide_pictures(prs, slide)
        missing = [z for z in sizes if z not in pics]
        assert not missing, "%s: %s slide %d has no picture of size %r (has %r)" % (fn, deck, slide, missing, list(pics))
        ims = [pics[z].convert("RGB") for z in sizes]
        if opt.get("join"):
            gap = 24
            h = max(i.height for i in ims)
            im = Image.new("RGB", (sum(i.width for i in ims) + gap * (len(ims) - 1), h), "white")
            x = 0
            for i in ims:
                im.paste(i, (x, 0)); x += i.width + gap
        else:
            im = ims[0]
        if opt.get("crop"):
            im = im.crop(opt["crop"])
        if opt.get("scale"):
            f = opt["scale"]
            im = im.resize((round(im.width * f), round(im.height * f)), Image.LANCZOS)
        dst = os.path.join(a.out, fn)
        im.save(dst, "PNG" if fn.endswith(".png") else "JPEG", quality=92)
        print("%-42s %s slide %-3d %dx%d" % (fn, deck, slide, im.width, im.height))
    for fn, url in COMMONS.items():
        dst = os.path.join(a.out, fn)
        if not os.path.exists(dst):
            req = urllib.request.Request(url, headers={"User-Agent": "PAQuizzesBuild/1.0 (study site)"})
            open(dst, "wb").write(urllib.request.urlopen(req, timeout=60).read())
        im = Image.open(dst)
        print("%-42s Wikimedia Commons %dx%d" % (fn, im.width, im.height))


if __name__ == "__main__":
    main()
