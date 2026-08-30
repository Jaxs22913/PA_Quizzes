#!/usr/bin/env python3
"""Extract clinical photographs from CMS I Exam 2 Lectures 11 and 12.

Same licensing position as the Lecture 10 extractor: a course PowerPoint image
may be used provided the slide is cited, and baked-in credit marks are left
visible on purpose.

Filenames are prefixed l11-/l12- so they cannot collide with the Lecture 10
images already in this folder. That matters: a silent renumber once put four
WRONG clinical photographs under the right filenames in a derm build, and the
only reason it was caught was a git diff on the image folder.

EVERY IMAGE IS VIEWED BEFORE IT IS PLACED IN THE GUIDE.

Extracting everything put 47 MB of full-size originals in a folder the
chart keeps under 3 MB. After viewing, the twelve that are actually used
were downscaled to 600 px JPEG at quality 80 -- the same treatment the
Lecture 10 images get -- and the rest deleted. Re-running this script
writes the originals again; run tools/prune_cms_e2_l1112_images.sh after.
"""
import os, re, struct, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2",
                   "cms-ophtho-chart-images")
BASE = os.path.expanduser("~/Desktop/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 2/")
DECKS = {"l11": "11. Neuro-Ophthalmology STUDENT VERSION 2026.pptx",
         "l12": "12. Acute Vision Loss current - Jaquith.pptx"}
EMR_STRETCHDIBITS = 81


def emf_dib(data):
    off = 0
    while off + 8 <= len(data):
        itype, nsize = struct.unpack_from("<II", data, off)
        if nsize < 8:
            break
        if itype == EMR_STRETCHDIBITS and off + 64 <= len(data):
            ob, cb, obits, cbits = struct.unpack_from("<IIII", data, off + 48)
            if cb and cbits and off + obits + cbits <= len(data):
                bmi = data[off + ob: off + ob + cb]
                bits = data[off + obits: off + obits + cbits]
                return (b"BM" + struct.pack("<IHHI", 14 + len(bmi) + len(bits),
                                            0, 0, 14 + len(bmi)) + bmi + bits)
        off += nsize
    return None


def main():
    os.makedirs(OUT, exist_ok=True)
    for pref, fname in DECKS.items():
        deck = os.path.join(BASE, fname)
        assert os.path.exists(deck), "deck not found: %s" % deck
        z = zipfile.ZipFile(deck)
        n_img = n_emf = 0
        for i in range(1, 80):
            rel = "ppt/slides/_rels/slide%d.xml.rels" % i
            if rel not in z.namelist():
                continue
            for k, name in enumerate(re.findall(r'Target="\.\./media/([^"]+)"',
                                                z.read(rel).decode("utf8", "replace")), 1):
                member = "ppt/media/" + name
                if member not in z.namelist():
                    continue
                data = z.read(member)
                ext = name.rsplit(".", 1)[-1].lower()
                if ext in ("emf", "wmf"):
                    dib = emf_dib(data)
                    if dib is None:
                        continue
                    data, ext = dib, "bmp"
                    n_emf += 1
                elif ext not in ("png", "jpg", "jpeg"):
                    continue
                if len(data) < 12000:
                    continue
                with open(os.path.join(OUT, "%s-s%03d_%d.%s" % (pref, i, k, ext)), "wb") as fh:
                    fh.write(data)
                n_img += 1
        print("%s: wrote %d images (%d decoded from metafiles)" % (pref, n_img, n_emf))


if __name__ == "__main__":
    main()
