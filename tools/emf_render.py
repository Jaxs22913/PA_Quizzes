#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Draw a vector EMF (enhanced metafile) as a picture, with no LibreOffice, Inkscape or ImageMagick.

WHY. A slide that renders BLANK (or with a few stray arrows) is often an embedded Word or Excel object whose only
picture is a vector .emf. The deck renders used for this site drop those pictures, Pillow and macOS Vision cannot
open EMF, and tools/emf_text.py recovers only the words. Found 2026-11-05 on Pharmacology I Exam 3: the heart
failure cascade (Lecture 9, slide 49), the digitalis mechanism (Lecture 9, slide 62), the mast cell mediators
(Lecture 11, slide 59) and the leukotriene pathway (Lecture 11, slides 61 and 76) are all Word drawings stored as EMF.

HOW. An EMF is a list of GDI drawing records. This reads the plain-GDI half of a "dual" EMF+/EMF file (Office writes
both; the EMF+ comments are skipped) and writes an SVG: paths (move, line, bezier, polygon, polypolygon), fills and
strokes with the selected pen and brush, the world transform stack (SAVEDC / RESTOREDC / MODIFYWORLDTRANSFORM),
PATCOPY rectangle fills, and text placed character by character from the record's own advance widths, so the
words land where Word put them whatever font is substituted. Clipping, hatches, bitmaps and the EMF+ records are
NOT drawn (none of the four pictures above needs them). PyMuPDF then rasterizes the SVG.

    python3 tools/emf_render.py picture.emf out.png [width]

ALWAYS LOOK at the result next to the slide text before using it: this is a partial GDI, and a picture that leans
on an unsupported record (a bitmap, a clip region) will come out incomplete. tools/emf_text.py lists the words the
picture must contain.
"""
import math, struct, sys
from xml.sax.saxutils import escape

# Symbol-font private-use characters Office writes for arrows and a few signs.
SYMBOL = {0xF0AD: "↑", 0xF0AF: "↓", 0xF0AE: "→", 0xF0AC: "←", 0xF0AB: "↔",
          0xF0B4: "×", 0xF0B1: "±", 0xF0A3: "≤", 0xF0B3: "≥", 0xF0B7: "•",
          0xF061: "α", 0xF062: "β", 0xF067: "γ", 0xF064: "δ", 0xF0B0: "°"}
STOCK = {0x80000000: ("brush", (255, 255, 255)), 0x80000001: ("brush", (192, 192, 192)),
         0x80000002: ("brush", (128, 128, 128)), 0x80000003: ("brush", (64, 64, 64)),
         0x80000004: ("brush", (0, 0, 0)), 0x80000005: ("brush", None),
         0x80000006: ("pen", ((255, 255, 255), 0)), 0x80000007: ("pen", ((0, 0, 0), 0)),
         0x80000008: ("pen", None)}


def _mul(a, b):
    """Compose two GDI XFORMs (a then b): (m11, m12, m21, m22, dx, dy)."""
    return (a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3],
            a[4] * b[0] + a[5] * b[2] + b[4], a[4] * b[1] + a[5] * b[3] + b[5])


def _rgb(c):
    return (c & 0xFF, (c >> 8) & 0xFF, (c >> 16) & 0xFF)


def _hex(rgb):
    return "#%02x%02x%02x" % rgb


def emf_to_svg(data, min_stroke_px=1.1, out_width=1400):
    t, sz = struct.unpack_from("<II", data, 0)
    assert t == 1, "not an EMF"
    bl, bt, br, bb = struct.unpack_from("<4i", data, 8)
    st = {"xf": (1, 0, 0, 1, 0, 0), "pen": ((0, 0, 0), 0), "brush": (255, 255, 255), "font": None,
          "tcolor": (0, 0, 0), "talign": 0, "fill": "evenodd", "worg": (0, 0)}
    stack, objs, out = [], {}, []
    path, inpath, cur = [], False, (0, 0)
    unit = (br - bl) / float(out_width)            # device units per output pixel
    o = 0

    def xf_attr():
        m = st["xf"]
        wx, wy = st["worg"]
        return 'transform="matrix(%.6g %.6g %.6g %.6g %.6g %.6g)"' % (m[0], m[1], m[2], m[3], m[4] - wx, m[5] - wy)

    def scale():
        m = st["xf"]
        return math.sqrt(abs(m[0] * m[3] - m[1] * m[2])) or 1.0

    def paint(d, do_fill, do_stroke):
        if not d:
            return
        fill = _hex(st["brush"]) if (do_fill and st["brush"] is not None) else "none"
        if do_stroke and st["pen"] is not None:
            col, w = st["pen"]
            w = max(w, min_stroke_px * unit / scale())
            stroke = 'stroke="%s" stroke-width="%.4g" stroke-linejoin="round"' % (_hex(col), w)
        else:
            stroke = 'stroke="none"'
        if fill == "none" and stroke == 'stroke="none"':
            return
        out.append('<path %s d="%s" fill="%s" fill-rule="%s" %s/>' % (xf_attr(), d, fill, st["fill"], stroke))

    def pts16(off, n):
        return [struct.unpack_from("<hh", data, off + 4 * i) for i in range(n)]

    while o + 8 <= len(data):
        t, sz = struct.unpack_from("<II", data, o)
        if sz < 8:
            break
        if t == 14:                                       # EOF
            break
        elif t == 10:                                     # SETWINDOWORGEX
            st["worg"] = struct.unpack_from("<2i", data, o + 8)
        elif t == 19:                                     # SETPOLYFILLMODE
            st["fill"] = "evenodd" if struct.unpack_from("<I", data, o + 8)[0] == 1 else "nonzero"
        elif t == 22:                                     # SETTEXTALIGN
            st["talign"] = struct.unpack_from("<I", data, o + 8)[0]
        elif t == 24:                                     # SETTEXTCOLOR
            st["tcolor"] = _rgb(struct.unpack_from("<I", data, o + 8)[0])
        elif t == 33:                                     # SAVEDC
            stack.append(dict(st))
        elif t == 34:                                     # RESTOREDC (relative)
            n = struct.unpack_from("<i", data, o + 8)[0]
            for _ in range(-n if n < 0 else 1):
                if stack:
                    st = stack.pop()
        elif t == 35:                                     # SETWORLDTRANSFORM
            st["xf"] = struct.unpack_from("<6f", data, o + 8)
        elif t == 36:                                     # MODIFYWORLDTRANSFORM
            x = struct.unpack_from("<6f", data, o + 8)
            mode = struct.unpack_from("<I", data, o + 32)[0]
            if mode == 1:
                st["xf"] = (1, 0, 0, 1, 0, 0)
            elif mode == 2:
                st["xf"] = _mul(x, st["xf"])
            elif mode == 3:
                st["xf"] = _mul(st["xf"], x)
            elif mode == 4:
                st["xf"] = x
        elif t == 37:                                     # SELECTOBJECT
            ih = struct.unpack_from("<I", data, o + 8)[0]
            kind, val = STOCK.get(ih) or objs.get(ih, (None, None))
            if kind in ("pen", "brush"):
                st[kind] = val
            elif kind == "font":
                st["font"] = val
        elif t == 38:                                     # CREATEPEN
            ih, style, wx, wy, col = struct.unpack_from("<IIiiI", data, o + 8)
            objs[ih] = ("pen", None if (style & 0xF) == 5 else (_rgb(col), wx))
        elif t == 39:                                     # CREATEBRUSHINDIRECT
            ih, style, col, hatch = struct.unpack_from("<IIII", data, o + 8)
            objs[ih] = ("brush", None if style == 1 else _rgb(col))
        elif t == 95:                                     # EXTCREATEPEN
            ih, ob, cb, obits, cbits, style, w, bstyle, col = struct.unpack_from("<9I", data, o + 8)
            objs[ih] = ("pen", None if ((style & 0xF) == 5 or bstyle == 1) else (_rgb(col), w))
        elif t == 82:                                     # EXTCREATEFONTINDIRECTW
            ih = struct.unpack_from("<I", data, o + 8)[0]
            h, w, esc, ori, weight = struct.unpack_from("<5i", data, o + 12)
            italic = data[o + 32]
            face = data[o + 40:o + 104].decode("utf-16le", "ignore").split("\x00")[0]
            objs[ih] = ("font", {"h": h, "esc": esc, "bold": weight >= 600, "italic": bool(italic), "face": face})
        elif t == 40:                                     # DELETEOBJECT
            objs.pop(struct.unpack_from("<I", data, o + 8)[0], None)
        elif t == 59:                                     # BEGINPATH
            path, inpath = [], True
        elif t == 60:                                     # ENDPATH
            inpath = False
        elif t == 61:                                     # CLOSEFIGURE
            path.append("Z")
        elif t == 27:                                     # MOVETOEX
            cur = struct.unpack_from("<2i", data, o + 8)
            if inpath:
                path.append("M%d %d" % cur)
        elif t == 54:                                     # LINETO
            nxt = struct.unpack_from("<2i", data, o + 8)
            if inpath:
                path.append("L%d %d" % nxt)
            else:
                paint("M%d %d L%d %d" % (cur[0], cur[1], nxt[0], nxt[1]), False, True)
            cur = nxt
        elif t in (62, 63, 64):                           # FILLPATH, STROKEANDFILLPATH, STROKEPATH
            paint(" ".join(path), t in (62, 63), t in (63, 64))
            path = []
        elif t in (85, 86, 87, 88, 89):                   # POLY*16
            n = struct.unpack_from("<I", data, o + 24)[0]
            p = pts16(o + 28, n)
            if not p:
                pass
            elif t in (88, 89):                           # ...TO: continue from the current point
                if t == 89:
                    seg = " ".join("L%d %d" % q for q in p)
                else:
                    seg = " ".join("C%d %d %d %d %d %d" % (p[i][0], p[i][1], p[i + 1][0], p[i + 1][1], p[i + 2][0], p[i + 2][1])
                                   for i in range(0, n - 2, 3))
                if inpath:
                    path.append(seg)
                else:
                    paint("M%d %d %s" % (cur[0], cur[1], seg), False, True)
                cur = p[-1]
            else:
                if t == 85:
                    seg = "M%d %d " % p[0] + " ".join("C%d %d %d %d %d %d" % (p[i][0], p[i][1], p[i + 1][0], p[i + 1][1], p[i + 2][0], p[i + 2][1])
                                                     for i in range(1, n - 2, 3))
                else:
                    seg = "M%d %d " % p[0] + " ".join("L%d %d" % q for q in p[1:]) + (" Z" if t == 86 else "")
                if inpath:
                    path.append(seg)
                else:
                    paint(seg, t == 86, True)
        elif t == 91:                                     # POLYPOLYGON16
            npoly, cpts = struct.unpack_from("<II", data, o + 24)
            counts = struct.unpack_from("<%dI" % npoly, data, o + 32)
            p = pts16(o + 32 + 4 * npoly, cpts)
            segs, k = [], 0
            for c in counts:
                q = p[k:k + c]; k += c
                segs.append("M%d %d " % q[0] + " ".join("L%d %d" % r for r in q[1:]) + " Z")
            if inpath:
                path.extend(segs)
            else:
                paint(" ".join(segs), True, True)
        elif t == 76:                                     # BITBLT: only the PATCOPY rectangle fill is drawn
            xd, yd, cx, cy, rop = struct.unpack_from("<iiiiI", data, o + 24)
            cb = struct.unpack_from("<I", data, o + 88)[0]
            if rop == 0x00F00021 and cb == 0 and st["brush"] is not None:
                out.append('<rect %s x="%d" y="%d" width="%d" height="%d" fill="%s"/>' % (xf_attr(), xd, yd, cx, cy, _hex(st["brush"])))
        elif t == 84:                                     # EXTTEXTOUTW
            x, y, n, offs, opts = struct.unpack_from("<iiIII", data, o + 36)
            offdx = struct.unpack_from("<I", data, o + 72)[0]
            raw = data[o + offs:o + offs + 2 * n].decode("utf-16le", "ignore")
            dx = list(struct.unpack_from("<%di" % n, data, o + offdx)) if (offdx and n) else [0] * n
            if opts & 0x2000:                             # ETO_PDY: pairs of (dx, dy)
                dx = dx[0::2]
            f = st["font"] or {"h": -12, "esc": 0, "bold": False, "italic": False, "face": "Arial"}
            size = abs(f["h"]) if f["h"] < 0 else f["h"] * 0.86
            chars = [SYMBOL.get(ord(c), c) for c in raw]
            if not "".join(chars).strip():
                o += sz; continue
            total = sum(dx[:len(chars)])
            ta = st["talign"]
            if ta & 6 == 6:          # TA_CENTER
                x0 = x - total / 2.0
            elif ta & 6 == 2:        # TA_RIGHT
                x0 = x - total
            else:
                x0 = x
            if ta & 24 == 24:        # TA_BASELINE
                yb = y
            elif ta & 24 == 8:       # TA_BOTTOM
                yb = y - 0.21 * size
            else:                    # TA_TOP
                yb = y + 0.905 * size
            xs, acc = [], x0
            for i, c in enumerate(chars):
                xs.append(acc); acc += dx[i] if i < len(dx) else size * 0.5
            keep = [(xx, c) for xx, c in zip(xs, chars)]
            rot = ' rotate(%.4g %.4g %.4g)' % (-f["esc"] / 10.0, x, y) if f["esc"] else ""
            m = st["xf"]; wx, wy = st["worg"]
            tr = 'transform="matrix(%.6g %.6g %.6g %.6g %.6g %.6g)%s"' % (m[0], m[1], m[2], m[3], m[4] - wx, m[5] - wy, rot)
            face = (f["face"] or "").lower()             # MuPDF knows the base-14 names only
            fam = "Times" if "times" in face else "Helvetica"
            if "black" in face:
                f = dict(f, bold=True)
            # One <text> per character: MuPDF's SVG reader ignores an x list, and the record's own advance
            # widths are what put each glyph where Word drew it. MuPDF does not inherit font attributes from a
            # <g>, so each <text> carries its own.
            fa = 'font-family="%s" font-size="%.4g"%s%s' % (
                fam, size, ' font-weight="bold"' if f["bold"] else "", ' font-style="italic"' if f["italic"] else "")
            out.append('<g %s fill="%s">%s</g>' % (
                tr, _hex(st["tcolor"]), "".join('<text x="%.4g" y="%.4g" %s>%s</text>' % (xx, yb, fa, escape(c))
                                                for xx, c in keep if c.strip())))
        o += sz
    w, h = br - bl, bb - bt
    pad = 0.01 * w
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%.6g %.6g %.6g %.6g" width="%d" height="%d">'
            '<rect x="%.6g" y="%.6g" width="%.6g" height="%.6g" fill="#ffffff"/>%s</svg>' % (
                bl - pad, bt - pad, w + 2 * pad, h + 2 * pad, out_width, round(out_width * (h + 2 * pad) / (w + 2 * pad)),
                bl - pad, bt - pad, w + 2 * pad, h + 2 * pad, "\n".join(out)))


def emf_to_image(data, out_width=1400):
    """Return a PIL RGB image of the EMF at out_width pixels wide."""
    import io
    import pymupdf
    from PIL import Image
    svg = emf_to_svg(data, out_width=out_width).encode("utf-8")
    doc = pymupdf.open(stream=svg, filetype="svg")
    page = doc[0]
    zoom = out_width / page.rect.width
    pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), alpha=False)
    return Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")


if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    width = int(sys.argv[3]) if len(sys.argv) > 3 else 1400
    emf_to_image(open(src, "rb").read(), width).save(dst)
    print("wrote", dst)
