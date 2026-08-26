"""Recover slide content that lives inside pictures, using macOS Vision OCR.

WHY THIS EXISTS
A .pptx stores editable text as <a:t> runs, and every extractor on this site
reads those. But a slide that is a SCREENSHOT of a table, or a textbook plate
pasted in as a picture, has no <a:t> at all -- it extracts as an empty slide
and silently disappears from every downstream build.

Two decks caught in one morning (2026-08-26):
  - PDM Lecture 5 slide 4 is a hand-drawn "Lab Values" fishbone carrying the
    ENTIRE reference-range set. Extracted text: nothing.
  - PD2 Ocular slide 48 is the Bates red-eye differential table -- five
    conditions crossed against seven exam findings, the single highest-yield
    slide in a 125-slide deck. Extracted text: nothing. Slide 110 holds the
    whole hypertensive-retinopathy objective (copper wire, silver wire, A-V
    nicking) the same way.

So: OCR every embedded picture, and report which slides gain text that plain
extraction never saw. See the "image-only-slides" memory.

WHAT IT DOES NOT DO
This reads the pictures EMBEDDED in the deck, not rendered slides. Text typed
into PowerPoint shapes is already in <a:t> and is not OCR'd again. Rendering
whole slides would need LibreOffice, which is not installed here.

OCR IS EVIDENCE, NOT TRUTH. Vision misreads small type, subscripts and
handwriting -- it read "HCO3" off a handwritten fishbone but mangled the
range. Treat output as "go look at this slide", exactly like
check_ppt_grounding.py. Never paste OCR text straight into a quiz.

USAGE
    python3 tools/ocr_deck_images.py <deck.pptx> [-o report.txt]
    python3 tools/ocr_deck_images.py <deck.pptx> --slides 48,110
    python3 tools/ocr_deck_images.py --image path/to/one.png

Needs pyobjc-framework-Vision + pyobjc-framework-Quartz:
    python3 -m pip install pyobjc-framework-Vision pyobjc-framework-Quartz
It FAILS LOUDLY if they are missing rather than degrading to a no-op scan --
per the build-tool-dependency-guards memory, a silent skip reports success
over nothing.
"""
import argparse
import os
import re
import sys
import tempfile
import zipfile

try:
    import Quartz
    import Vision
    from Foundation import NSURL
except ImportError as e:                       # loud, not silent
    sys.exit("FATAL: %s\nInstall with:\n"
             "  python3 -m pip install pyobjc-framework-Vision "
             "pyobjc-framework-Quartz\n"
             "Refusing to run a scan that would find nothing and call it clean."
             % e)

# A true icon floor. It was 120px and that was WRONG -- it silently skipped the
# 280x112 visual-field figures on PD2 slides 60-62. They turned out to hold no
# text, but the tool had no way to know that and neither did I. Attempt OCR on
# almost everything; skips are now listed BY NAME, never just counted.
MIN_PX = 48

# Media that is not a still image at all. Reported separately and loudly --
# an embedded video is lecture content that no text extractor has ever seen.
NON_IMAGE = (".mp4", ".mov", ".m4a", ".mp3", ".wav", ".avi", ".wmv", ".emf", ".wmf")
# A slide whose real <a:t> text is shorter than this is "effectively empty".
THIN_TEXT = 40

# Figure captions that are not teaching content. A slide carrying only these
# is just as empty as one carrying nothing -- PD2 has ~14 Bates plates whose
# only text is a download date and a copyright line.
BOILERPLATE = re.compile(
    r'^(date of download|copyright|from:|legend:|bates|http|source:|'
    r'reproduced|adapted from)', re.I)
# ...and OCR must find at least this much to call it a real recovery.
MIN_RECOVERED = 25


def ocr_image(path):
    """OCR one picture.

    Returns (status, text, width, height) where status is one of:
      "ok"    -- Vision ran; text may still be "" if the picture has no words
      "small" -- below the icon floor, deliberately not attempted
      "fail"  -- Vision could not decode the file at all
    These are three different things and the caller must not conflate them.
    An earlier version returned "" for both "too small" and "no words found",
    which made the report claim a 2048px plate had been skipped as an icon.
    """
    src = Quartz.CGImageSourceCreateWithURL(
        NSURL.fileURLWithPath_(path), None)
    if src is None:
        return "fail", "", 0, 0
    img = Quartz.CGImageSourceCreateImageAtIndex(src, 0, None)
    if img is None:
        return "fail", "", 0, 0
    w, h = Quartz.CGImageGetWidth(img), Quartz.CGImageGetHeight(img)
    if w < MIN_PX or h < MIN_PX:
        return "small", "", w, h
    req = Vision.VNRecognizeTextRequest.alloc().init()
    req.setRecognitionLevel_(0)                # 0 = accurate (1 = fast)
    req.setUsesLanguageCorrection_(True)
    handler = Vision.VNImageRequestHandler.alloc().initWithCGImage_options_(
        img, None)
    ok, _err = handler.performRequests_error_([req], None)
    if not ok:
        return "fail", "", w, h
    lines = []
    for obs in (req.results() or []):
        cands = obs.topCandidates_(1)
        if cands:
            lines.append(cands[0].string())
    return "ok", "\n".join(lines), w, h


def real_text(lines):
    """Native lines minus figure-caption boilerplate."""
    return [l for l in lines if not BOILERPLATE.match(l.strip())]


def slide_text(xml):
    """The <a:t> text a normal extractor would see, paragraph by paragraph."""
    out = []
    for para in re.findall(r'<a:p\b.*?</a:p>|<a:p/>', xml, re.S):
        line = "".join(re.findall(r'<a:t>(.*?)</a:t>', para, re.S))
        for a, b in (('&amp;', '&'), ('&lt;', '<'), ('&gt;', '>'),
                     ('&quot;', '"'), ('&#8217;', "'"), ('&apos;', "'")):
            line = line.replace(a, b)
        line = " ".join(line.split())
        if line:
            out.append(line)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("deck", nargs="?", help="path to a .pptx")
    ap.add_argument("--image", help="OCR a single image file and print it")
    ap.add_argument("--slides", help="only these slide numbers, e.g. 48,110")
    ap.add_argument("-o", "--out", help="write the full report here")
    a = ap.parse_args(argv)

    if a.image:
        status, text, w, h = ocr_image(a.image)
        if status == "fail":
            sys.exit("could not read %s" % a.image)
        print("# %s  (%dx%d) [%s]\n%s" % (a.image, w, h, status, text))
        return 0
    if not a.deck:
        ap.error("give a .pptx, or --image")

    want = None
    if a.slides:
        want = {int(x) for x in re.findall(r'\d+', a.slides)}

    z = zipfile.ZipFile(a.deck)
    nslides = len([n for n in z.namelist()
                   if re.match(r'ppt/slides/slide\d+\.xml$', n)])
    tmp = tempfile.mkdtemp(prefix="deckocr-")
    cache, report = {}, []
    n_img = n_ocr = 0
    skipped, notext, failed, nonimage = [], [], [], []
    recovered, thin_no_gain = [], []

    for i in range(1, nslides + 1):
        if want and i not in want:
            continue
        xml = z.read('ppt/slides/slide%d.xml' % i).decode('utf8', 'replace')
        native = slide_text(xml)
        native_len = sum(len(x) for x in real_text(native))

        rel = 'ppt/slides/_rels/slide%d.xml.rels' % i
        imgs = []
        if rel in z.namelist():
            imgs = re.findall(r'Target="\.\./media/([^"]+)"',
                              z.read(rel).decode('utf8', 'replace'))

        found = []
        for name in imgs:
            n_img += 1
            if name not in cache:
                member = 'ppt/media/' + name
                if member not in z.namelist():
                    cache[name] = ("fail", "", 0, 0)
                else:
                    p = os.path.join(tmp, name)
                    with open(p, 'wb') as fh:
                        fh.write(z.read(member))
                    cache[name] = ocr_image(p)
            status, text, w, h = cache[name]
            if name.lower().endswith(NON_IMAGE):
                if name not in [x for x, _ in nonimage]:
                    nonimage.append((name, i))
            elif status == "fail":
                if name not in failed:
                    failed.append(name)
            elif status == "small":
                if name not in [x for x, _, _ in skipped]:
                    skipped.append((name, w, h))
            elif text.strip():
                n_ocr += 1
                found.append((name, w, h, text))
            elif name not in [x for x, _, _ in notext]:
                notext.append((name, w, h))

        gained = sum(len(t) for _, _, _, t in found)
        if native_len < THIN_TEXT:
            if gained >= MIN_RECOVERED:
                recovered.append((i, native_len, gained))
            else:
                thin_no_gain.append(i)

        if found:
            report.append("=" * 68)
            report.append("SLIDE %d   (native text: %d chars%s)"
                          % (i, native_len,
                             "  <-- EFFECTIVELY EMPTY" if native_len < THIN_TEXT else ""))
            for line in native:
                report.append("    native: %s" % line)
            for name, w, h, text in found:
                report.append("    --- OCR %s (%dx%d) ---" % (name, w, h))
                for line in text.split("\n"):
                    report.append("      %s" % line)

    body = "\n".join(report)
    if a.out:
        open(a.out, "w").write(body + "\n")
    else:
        print(body)

    # The denominator matters more than the flag count. Print all of it.
    print("\n" + "=" * 68)
    print("deck            : %s" % os.path.basename(a.deck))
    print("slides scanned  : %d of %d" % (len(want) if want else nslides, nslides))
    print("picture refs    : %d  (%d distinct)" % (n_img, len(cache)))
    print("  yielded text  : %d refs" % n_ocr)
    print("  wordless pics : %d distinct  (looked at, genuinely no text -- a"
          " diagram can still be content)" % len(notext))
    if skipped:
        print("  under %dpx     : %d distinct  %s" % (MIN_PX, len(skipped),
              ", ".join("%s(%dx%d)" % (n, w, h) for n, w, h in skipped)))
    if failed:
        print("  UNREADABLE    : %d  %s   <-- go look at these"
              % (len(failed), ", ".join(failed)))
    if nonimage:
        print("  EMBEDDED VIDEO/AUDIO: %d  <-- lecture content no extractor sees"
              % len(nonimage))
        for n, sl in nonimage:
            print("      %s on slide %d" % (n, sl))
    print("slides where OCR RECOVERED text that extraction missed: %d"
          % len(recovered))
    for i, nl, g in recovered:
        print("    slide %-4d native %3d chars -> OCR found %d" % (i, nl, g))
    if thin_no_gain:
        print("thin slides with nothing recoverable (spoken-only or decorative): %s"
              % ", ".join(map(str, thin_no_gain)))
    if a.out:
        print("full text -> %s" % a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
