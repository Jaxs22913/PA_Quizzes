# -*- coding: utf-8 -*-
"""Figure machinery shared by the Lecture 18 guide (_micro_e3_guide_l18.py and its fragment
_micro_e3_guide_l18_viruses.py), kept apart so the fragment can be imported alone. A copy of
_micro_e3_guide_l17_figs.py with the Lecture 18 deck and names.

PROTECTED figures: the Microbiology Exam 3 Webster review page (tools/build_micro_e3_webster_review.py) shows 15 of
this guide's Lecture 18 figures by file name. This guide uses all 15 with exactly the (slide, picture number, name,
crop=None) below, and extract() never removes them.
"""
import io, os, glob

FIG = "micro-exam-3-study-guide-images"
DECK = "Lecture 18  Dr. Webster -  DNA viruses of medical importance.pptx"
# The deck name as printed in the page: the assembler writes out bare "DNA" in prose, which must not rewrite a file
# name, so the D is an entity (renders "DNA").
DECK_HTML = DECK.replace("DNA", "&#68;NA")
INBOX_DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Microbiology Inbox/Exam 3/" + DECK)
MAXW = 900
MH = "Copyright &copy; The McGraw-Hill Companies."

PROTECTED = [
    (10, 1, "l18-s010-naked-and-enveloped.jpg"),
    (17, 1, "l18-s017-phage-cycles.jpg"),
    (22, 1, "l18-s022-animal-virus-entry.jpg"),
    (23, 1, "l18-s023-dna-virus-replication.jpg"),
    (27, 1, "l18-s027-effects-on-host-cells.jpg"),
    (30, 1, "l18-s030-dna-virus-groups.jpg"),
    (33, 1, "l18-s033-poxvirus.jpg"),
    (45, 1, "l18-s045-smallpox.jpg"),
    (56, 1, "l18-s056-herpesvirus.jpg"),
    (61, 1, "l18-s061-herpetic-whitlow.jpg"),
    (70, 1, "l18-s070-varicella-zoster.jpg"),
    (76, 2, "l18-s076-burkitt-lymphoma.jpg"),
    (82, 1, "l18-s082-roseola.jpg"),
    (84, 1, "l18-s084-kaposi-sarcoma.jpg"),
    (105, 1, "l18-s105-fifth-disease.jpg"),
]
_PROTECTED_NAMES = set(n for _, _, n in PROTECTED)

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
    (group members and picture placeholders count); name = l18-sNNN-what-it-shows.jpg (always .jpg);
    crop = (left, top, right, bottom) on the ORIGINAL picture's pixels, or None."""
    assert name.startswith("l18-s%03d-" % slide) and name.endswith(".jpg"), name
    assert name not in [n for _, _, n, _ in IMAGES], "figure used twice: " + name
    if name in _PROTECTED_NAMES:
        assert (slide, k, name) in PROTECTED and crop is None, "protected figure changed: " + name
    IMAGES.append((slide, k, name, crop))
    w, h = _image(slide, k, crop).size
    note = (credit + " ") if credit else ""
    return ('<figure class="fig"><img width="%d" height="%d" loading="lazy" src="%s/%s" alt="%s">'
            '<figcaption>%s <span class="src">%sSource: %s, Slide %d.</span></figcaption></figure>'
            % (w, h, FIG, name, alt, cap, note, DECK_HTML, slide))


def extract(imgdir):
    """Write every figure fig() recorded into imgdir, and remove Lecture 18 figures no longer used (never a
    protected one: the Webster review page shows those)."""
    used = set(n for _, _, n, _ in IMAGES)
    missing = _PROTECTED_NAMES - used
    assert not missing, "the guide must use every protected Lecture 18 figure: %s" % sorted(missing)
    os.makedirs(imgdir, exist_ok=True)
    keep = used | _PROTECTED_NAMES
    for old in glob.glob(os.path.join(imgdir, "l18-s*.jpg")):
        if os.path.basename(old) not in keep:
            os.remove(old)
    for slide, k, name, crop in IMAGES:
        _image(slide, k, crop).save(os.path.join(imgdir, name), quality=85)
    return len(IMAGES)
