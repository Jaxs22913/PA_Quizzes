#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Splice Lecture 14 (Ocular Trauma) into the CMS I Exam 2 study guide.

Additive and fenced, like the Lecture 11/12 and 13 adders, and for the same
reason: a guide rebuild once destroyed hand-written content that had to be
recovered from git. Separate toc/body fences, because a single shared pair made
the second splice find and overwrite the first.

FIGURES REUSE THE CHART'S OWN AUDITED IMAGES in place, per the standing rule
that a visual subject gets photographs in the guide.

EVERY PICTURE HERE COMES FROM A SLIDE WHOSE NOTES LABEL IT BY POSITION, and the
notes in this deck do not map to slides by index. Four assignments were checked
by eye against the notes' own labels before any caption was written:
  slide 45 pos1 haemotympanum, pos3 Battle sign, pos6 Battle sign
  slide 42 pos2 inferior rectus entrapment limiting upward gaze
All four matched, which is what licenses trusting the rest of the reading-order
mapping. Slide 45's notes say "Top right: battle sign" twice; both right-hand
pictures really are a Battle sign, so the second means bottom right.
"""
import io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _cms_e2_guide_l14 import SECTION as S14, TOC as T14, TEST as Q14

GUIDE = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2",
                     "cms-exam-2-study-guide.html")
IMGDIR = os.path.join(os.path.dirname(GUIDE), "cms-ophtho-chart-images")
FENCES = {"toc":  ("<!--CMSE2L14-TOC-->",  "<!--/CMSE2L14-TOC-->"),
          "body": ("<!--CMSE2L14-BODY-->", "<!--/CMSE2L14-BODY-->")}

# token -> [(file, name, caption, slide)]
FIGS = {
 "@@GLOBE@@": [
   ("l14-s015_pos1.jpg", "Full-thickness eye wall laceration",
    "Cut clean through by a sharp object or high-velocity projectile", 15),
   ("l14-s017_pos1.jpg", "Globe rupture",
    "Blunt force splitting the eye at a weak point", 17)],
 "@@SURFACE@@": [
   ("l14-s018_pos1.jpg", "Corneal abrasion",
    "Fluorescein staining the exposed basement membrane", 18),
   ("l14-s021_pos1.jpg", "Corneal foreign body",
    "Lodged after grinding or striking metal", 21)],
 "@@HYPHEMA@@": [
   ("l14-s024_pos1.jpg", "Hyphema",
    "Blood layered in the anterior chamber, with a visible fluid level", 24)],
 "@@LIDS@@": [
   ("l14-s027_pos1.jpg", "Lid laceration",
    "Look underneath &mdash; two thirds of full-thickness cuts have a globe injury with them", 27),
   ("l14-s032_pos1.jpg", "Orbital contusion",
    "Swelling held in front of the septum, without haemorrhage", 32),
   ("l14-s034_pos2.jpg", "Periorbital haematoma",
    "Bleeding behind the septum, within the bony orbit", 34)],
 "@@DETACH@@": [
   ("l14-s037_pos2.jpg", "Posterior vitreous detachment",
    "The event that usually precedes a rhegmatogenous detachment", 37),
   ("l14-s038_pos1.jpg", "Retinal detachment on ultrasound",
    "The detached retina as a bright membrane tethered in the vitreous cavity", 38)],
 "@@FRACTURE@@": [
   ("l14-s042_pos1.jpg", "Orbital floor fracture",
    "Periorbital ecchymosis and lid oedema after blunt force", 42),
   ("l14-s042_pos2.jpg", "Inferior rectus entrapment",
    "The right eye fails to elevate on upward gaze &mdash; diplopia looking up", 42),
   ("l14-s042_pos4.jpg", "Medial wall fracture",
    "Periorbital ecchymosis and swelling", 42)],
 "@@BASILAR@@": [
   ("l14-s045_pos1.jpg", "Haemotympanum",
    "Blood behind the tympanic membrane", 45),
   ("l14-s045_pos2.jpg", "Raccoon eyes",
    "Periorbital ecchymosis, without direct orbital trauma", 45),
   ("l14-s045_pos3.jpg", "Battle sign",
    "Retroauricular ecchymosis over the mastoid", 45),
   ("l14-s046_pos1.jpg", "Halo (double ring) sign",
    "Otorrhoea on a bedsheet: inner ring of blood, outer ring of cerebrospinal fluid", 46)],
}


def figure(fn, name, cap, slide):
    return ('<figure><img src="cms-ophtho-chart-images/%s" loading="lazy" decoding="async" '
            'alt="%s &mdash; %s"><figcaption><span class="fg-name">%s</span>%s'
            '<span class="fg-cite">Slide %d</span></figcaption></figure>'
            % (fn, name, cap, name, cap, slide))


def splice(text, key, block, before):
    op, cl = FENCES[key]
    fenced = op + block + cl
    pat = re.compile(re.escape(op) + ".*?" + re.escape(cl), re.S)
    if pat.search(text):
        return pat.sub(lambda _: fenced, text, count=1)
    assert text.count(before) == 1, "anchor %r is not unique" % before
    return text.replace(before, fenced + before)


def main():
    body = S14
    for token, items in FIGS.items():
        assert token in body, "figure token %s unused" % token
        for fn, _n, _c, _s in items:
            assert os.path.exists(os.path.join(IMGDIR, fn)), \
                "missing %s -- run extract_cms_e2_l14_images.py" % fn
        body = body.replace(token, '<div class="figgrid">'
                            + "".join(figure(*i) for i in items) + "</div>")
    assert "@@" not in body, "unfilled figure token"

    t = io.open(GUIDE, encoding="utf-8").read()
    before = len(t)

    t = splice(t, "toc", "\n" + T14, "</nav>")
    t = splice(t, "body", "\n" + body + "\n", "</main>")

    anchor = "  var TEST_YOURSELF = {\n"
    assert t.count(anchor) == 1
    if "    trauma: [" not in t:
        t = t.replace(anchor, anchor + Q14)

    io.open(GUIDE, "w", encoding="utf-8").write(t)
    print("guide %d -> %d bytes (+%d)" % (before, len(t), len(t) - before))

    folder = os.path.dirname(GUIDE)
    missing = [s for s in re.findall(r'src="(cms-ophtho-chart-images/[^"]+)"', t)
               if not os.path.exists(os.path.join(folder, s))]
    assert not missing, "missing images: %s" % missing

    # every earlier section and its table of contents must survive
    for need in ('id="ocular-trauma"', "    trauma: [", 'id="chronic-vision-loss"',
                 'id="neuro-ophthalmology"', 'id="acute-vision-loss"',
                 'href="#e2l1-approach"', 'href="#e2l4-melanoma"', "    cvl: ["):
        assert need in t, "missing after splice: %s" % need

    nav_a, nav_b = t.index('<nav class="toc">'), t.index("</nav>")
    main_a, main_b = t.index("<main"), t.index("</main>")
    sec = t.index('id="ocular-trauma"')
    assert main_a < sec < main_b, "section landed outside <main>"
    link = t.index('href="#e2l5-rules"')
    assert nav_a < link < nav_b, "table of contents link landed outside <nav>"

    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li",
                "figure", "figcaption"):
        o = len(re.findall(r"<%s[ >]" % tag, t)); c = t.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    print("verified: section inside <main>, links inside <nav>, earlier sections intact, "
          "%d figures" % len(re.findall(r'src="cms-ophtho-chart-images/l14-', t)))


if __name__ == "__main__":
    main()
