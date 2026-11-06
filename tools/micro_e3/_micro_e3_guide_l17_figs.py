# -*- coding: utf-8 -*-
"""Figure machinery shared by the Lecture 17 guide fragments (_micro_e3_guide_l17_protozoa.py,
_micro_e3_guide_l17_helminths.py) and _micro_e3_guide_l17.py, kept apart so a fragment can be imported alone.
"""
import io, os, glob

FIG = "micro-exam-3-study-guide-images"
DECK = "Lecture 16 Dr. Webster Parasites of Medical Importance.pptx"
INBOX_DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Microbiology Inbox/Exam 3/" + DECK)
MAXW = 900
MH = "Copyright &copy; The McGraw-Hill Companies."
CDC = "Image: Centers for Disease Control and Prevention, DPDx."

IMAGES = []          # (slide, picture number, published name, crop box or None), filled by fig()
_PRS = None


def _pictures(shapes):
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from _pictures(sh.shapes)
            continue
        try:
            sh.image
        except Exception:
            continue
        yield sh


def _image(slide, k, crop):
    """The picture as a PIL image after crop and the 900-pixel cap (what extract() writes)."""
    global _PRS
    from PIL import Image
    if _PRS is None:
        from pptx import Presentation
        _PRS = Presentation(INBOX_DECK)
    pics = list(_pictures(_PRS.slides[slide - 1].shapes))
    assert len(pics) >= k, "%s slide %d has %d picture(s)" % (DECK, slide, len(pics))
    im = Image.open(io.BytesIO(pics[k - 1].image.blob)).convert("RGB")
    if crop:
        im = im.crop(crop)
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    return im


def fig(slide, k, name, alt, cap, credit="", crop=None):
    """A captioned slide picture. slide = slide number; k = picture number on that slide in shape-tree order
    (group members and picture placeholders count); name = l17-sNNN-what-it-shows.jpg (always .jpg);
    crop = (left, top, right, bottom) on the ORIGINAL picture's pixels, or None."""
    assert name.startswith("l17-s%03d-" % slide) and name.endswith(".jpg"), name
    assert name not in [n for _, _, n, _ in IMAGES], "figure used twice: " + name
    IMAGES.append((slide, k, name, crop))
    w, h = _image(slide, k, crop).size
    note = (credit + " ") if credit else ""
    return ('<figure class="fig"><img width="%d" height="%d" loading="lazy" src="%s/%s" alt="%s">'
            '<figcaption>%s <span class="src">%sSource: %s, Slide %d.</span></figcaption></figure>'
            % (w, h, FIG, name, alt, cap, note, DECK, slide))


def extract(imgdir):
    """Write every figure fig() recorded into imgdir, and remove Lecture 17 figures no longer used."""
    os.makedirs(imgdir, exist_ok=True)
    keep = set(n for _, _, n, _ in IMAGES)
    for old in glob.glob(os.path.join(imgdir, "l17-s*.jpg")):
        if os.path.basename(old) not in keep:
            os.remove(old)
    for slide, k, name, crop in IMAGES:
        _image(slide, k, crop).save(os.path.join(imgdir, name), quality=85)
    return len(IMAGES)
