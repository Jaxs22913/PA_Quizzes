#!/usr/bin/env python3
"""Designed dark mode for quiz, guide and cram pages (design review item 7).

Until 2026-09-25 these pages were dark-moded by `filter: invert(1)
hue-rotate(180deg)` on body > .wrap: navy banners came out pastel lavender,
cards pure black, the warm guide paper a maroon brown. This tool gives a page a
real dark palette instead, DERIVED from that page's own light palette, so every
exam keeps its identity (navy stays navy) and no colour is invented.

For each opted-in page it

  1. adds data-dark="tokens" to <body>  (theme.css then drops the invert
     filter and the image counter-invert for that page, together), and
  2. writes a fenced <style id="dark-tokens"> block into <head> that, under
     :root[data-theme="dark"], re-points the page's own palette variables.

THE RECIPE is the site's one accent recipe (site_design_tokens memory): the
lightness that lands the hue on 4.60:1 against its background, at 90% of the
maximum chroma sRGB can hold at that lightness. A text-role accent is solved
against the darkest TINTED surface it can sit on (the page's dark "soft"),
so it clears 4.60:1 there and more on the plain card. Fill roles (banners,
filled buttons, table headers carrying white text) keep the LIGHT value,
exposed as --<name>-l, because white text needs the darker fill.

Neutrals are the site's existing dark tokens (home.css / theme.css): page
#0f1115, card #191c22, line #2a2e37, ink #e5e7eb, muted #9aa1ac, and
Progress/Review's dark green/crimson for right/wrong.

Scope: Semester 2+ only. Semester 1 is frozen and stays on the filter.
Idempotent; re-run after any quiz render, guide build or cram build:

    python3 tools/dark_tokens.py            # apply to every eligible page
    python3 tools/dark_tokens.py --check    # report pages missing/stale, exit 1
    python3 tools/dark_tokens.py --selftest # reproduce the shipped accents
"""
import math, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Semester 1 folders (same tuple as check_exam_standard.py's FROZEN).
FROZEN = ("Anatomy Exam", "Anatomy Practicum Exam", "CAM Nutrition Exam",
          "Intro to PA Profession", "Nutrition Class", "Pharmacodynamics Exam",
          "Physical Diagnosis 1 Exam", "Physiology Exam")
# Page kinds rolled out so far. Each kind needs its component rules in
# theme.css ("DESIGNED DARK MODE" block) before it is switched on here.
KINDS = ("quiz", "guide")
# Pages that ship their own bespoke component set the theme.css block does not
# cover; they keep the invert filter until someone maps their components.
EXCLUDE = {"Physical Diagnosis 2 Exam 1/pd2-ent-osce-study-guide.html"}
SKIP_DIRS = {".git", "tools", "group-quizzes", "cram-personal", "icons", "audio",
             "class-traps", "Remediation"}

PAGE, CARD, LINE, INK, MUTED = "#0f1115", "#191c22", "#2a2e37", "#e5e7eb", "#9aa1ac"
OK, OK_BG, BAD, BAD_BG = "#31974d", "#0c2a13", "#f53c52", "#3c1718"
TARGET = 4.60
SOFT_L, SOFT_C = 0.255, 0.045   # dark tinted surface: same L band as the site's -soft darks

# ---------------------------------------------------------------- colour math
def hex_rgb(h):
    h = h.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))

def rgb_hex(rgb):
    return "#" + "".join("%02x" % max(0, min(255, round(c * 255))) for c in rgb)

def _lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def _gam(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055

def rgb_oklch(rgb):
    r, g, b = (_lin(c) for c in rgb)
    l = (0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b) ** (1 / 3)
    m = (0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b) ** (1 / 3)
    s = (0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b) ** (1 / 3)
    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    A = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    B = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    return L, math.hypot(A, B), math.degrees(math.atan2(B, A)) % 360

def oklch_rgb(L, C, H, clip=False):
    A, B = C * math.cos(math.radians(H)), C * math.sin(math.radians(H))
    l = (L + 0.3963377774 * A + 0.2158037573 * B) ** 3
    m = (L - 0.1055613458 * A - 0.0638541728 * B) ** 3
    s = (L - 0.0894841775 * A - 1.2914855480 * B) ** 3
    r = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    b = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    if not clip and (min(r, g, b) < -1e-4 or max(r, g, b) > 1 + 1e-4):
        return None
    return tuple(_gam(min(1, max(0, c))) for c in (r, g, b))

def lum(rgb):
    r, g, b = (_lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)

def max_chroma(L, H):
    lo, hi = 0.0, 0.4
    for _ in range(40):
        mid = (lo + hi) / 2
        if oklch_rgb(L, mid, H) is None:
            hi = mid
        else:
            lo = mid
    return lo

def solve(hue, bg_hex, target=TARGET, frac=0.9, cmax=None):
    """Lightness landing `hue` on `target` contrast against bg, at frac*max chroma.
    On a dark ground contrast RISES with lightness (the binary search flips).
    cmax caps the chroma at the source colour's own: the site accents are
    saturated so the cap never binds for them, but a muted exam palette
    (PDM's plum, CMS's teal) must stay muted in dark, not turn neon."""
    bg = hex_rgb(bg_hex)
    dark_bg = lum(bg) < 0.18
    chroma = lambda L: min(max_chroma(L, hue) * frac, cmax if cmax is not None else 9)
    lo, hi = 0.0, 1.0
    for _ in range(50):
        L = (lo + hi) / 2
        c = contrast(oklch_rgb(L, chroma(L), hue, clip=True), bg)
        if (c < target) == dark_bg:
            lo = L
        else:
            hi = L
    L = hi if dark_bg else lo
    return rgb_hex(oklch_rgb(L, chroma(L), hue, clip=True))

def lift(hexcolor, bg_hex, target=TARGET):
    """Dark-mode text value of a light palette colour: same hue, its own chroma
    at most, solved to `target` against bg."""
    L, C, H = rgb_oklch(hex_rgb(hexcolor))
    return solve(H, bg_hex, target, cmax=C)

def fill(light, darker):
    """Filled surface carrying white text: the light value if white clears 4.5:1
    on it, else the palette's darker partner (both are the page's own colours)."""
    return light if contrast(hex_rgb("#ffffff"), hex_rgb(light)) >= 4.5 else darker

def soft(hue):
    return rgb_hex(oklch_rgb(SOFT_L, min(SOFT_C, max_chroma(SOFT_L, hue) * 0.9), hue, clip=True))

def hue_of(h):
    return rgb_oklch(hex_rgb(h))[2]

# ------------------------------------------------------------------ palettes
def quiz_tokens(v):
    """v: dict of the page's light --navy/--indigo/--gold/--ice."""
    ice = soft(hue_of(v["indigo"]))
    indigo_d = lift(v["indigo"], ice)
    return {
        "navy-l": v["navy"], "gold-l": v["gold"],
        "indigo-l": fill(v["indigo"], v["navy"]),
        "navy": lift(v["navy"], ice, 7.0),     # heading/emphasis text
        "indigo": indigo_d,                    # accent text + borders
        "gold": v["gold"],                     # mid-light already; fills only
        "ice": ice,
        "ink": INK, "muted": MUTED, "line": LINE, "card": CARD, "page": PAGE,
        "paper": CARD,
        "ok": OK, "ok-bg": OK_BG, "bad": BAD, "bad-bg": BAD_BG,
        # the template's own light right/wrong, kept for filled badges with white text
        "ok-l": "#1f8f52", "bad-l": "#c93a3a",
        "exam-toolbar-accent": indigo_d,
    }

def guide_tokens(v):
    a1 = soft(hue_of(v["accent"]))
    t = {"ink": INK, "paper": PAGE, "line": LINE, "soft": MUTED, "muted": MUTED,
         "card": CARD, "soft-bg": a1}
    for k in ("accent", "accent2", "accent3"):
        if k in v:
            t[k + "-l"] = v[k]
            t[k] = lift(v[k], soft(hue_of(v[k])))
            t[k + "-soft"] = soft(hue_of(v[k]))
    return t

def cram_tokens(v):
    return {"ink": INK, "body": INK, "muted": MUTED, "line": LINE,
            "paper": PAGE, "card": CARD,
            "primary-l": v["primary"],
            "primary": lift(v["primary"], soft(hue_of(v["primary"])))}

# ---------------------------------------------------------------- page scan
VAR = lambda name: re.compile(r"--%s\s*:\s*(#[0-9a-fA-F]{3,6})\b" % re.escape(name))

def first_root_block(s):
    m = re.search(r":root\s*\{([^}]*)\}", s)
    return m.group(1) if m else ""

def classify(s):
    if 'id="examtoolbar"' in s and "--navy" in s:
        return "quiz"
    if '<header class="top"' in s and 'class="layout' in s and "--accent" in s:
        return "guide"
    if "--primary" in s and 'class="topic' in s:
        return "cram"
    return None

def tokens_for(kind, s):
    root = first_root_block(s)
    get = lambda n: (VAR(n).search(root) or [None, None])[1]
    if kind == "quiz":
        v = {n: get(n) for n in ("navy", "indigo", "gold", "ice")}
        return quiz_tokens(v) if all(v.values()) else None
    if kind == "guide":
        v = {n: get(n) for n in ("accent", "accent2", "accent3") if get(n)}
        return guide_tokens(v) if "accent" in v else None
    if kind == "cram":
        p = get("primary")
        return cram_tokens({"primary": p}) if p else None

BEGIN, END = "<!--DARK-TOKENS:BEGIN (tools/dark_tokens.py)-->", "<!--DARK-TOKENS:END-->"

def block(tok):
    body = "".join("--%s:%s;" % kv for kv in tok.items())
    return ('%s<style id="dark-tokens">:root[data-theme="dark"] body[data-dark="tokens"]{%s}</style>%s'
            % (BEGIN, body, END))

def apply(s, kind=None):
    """Return the page with the opt-in attribute and a fresh token block."""
    kind = kind or classify(s)
    if not kind:
        return s
    tok = tokens_for(kind, s)
    if not tok:
        return s
    s = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?", "", s, flags=re.S)
    s = s.replace("</head>", block(tok) + "\n</head>", 1)
    if not re.search(r"<body[^>]*\bdata-dark=", s):
        s = re.sub(r"<body\b", '<body data-dark="tokens" data-dark-kind="%s"' % kind, s, count=1)
    return s

def eligible():
    for d in sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, d)
        if not os.path.isdir(p) or d in SKIP_DIRS or d.startswith(".") or d.startswith(FROZEN):
            continue
        for f in sorted(os.listdir(p)):
            if f.endswith(".html") and d + "/" + f not in EXCLUDE:
                yield os.path.join(p, f)

def selftest():
    # the light recipe must reproduce the shipped accents exactly
    ref = {262: "#2a6df2", 302: "#9c46f3", 58: "#ad631e", 196: "#228283", 149: "#218640"}
    ok = True
    for hue, want in ref.items():
        got = solve(hue_of(want), "#ffffff")
        c = contrast(hex_rgb(got), hex_rgb("#ffffff"))
        print("light hue %.1f want %s got %s (%.2f:1)" % (hue_of(want), want, got, c))
        ok &= abs(c - 4.60) < 0.03
    for want in ("#4981ee", "#a465ee", "#c0722d", "#329293", "#31974d"):
        got = solve(hue_of(want), CARD)
        print("dark  want %s (%.2f:1) got %s (%.2f:1)" % (want, contrast(hex_rgb(want), hex_rgb(CARD)),
              got, contrast(hex_rgb(got), hex_rgb(CARD))))
    return ok

def main():
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    check = "--check" in sys.argv
    kinds_on = set(KINDS)
    changed = missing = n = 0
    kinds = {}
    for path in eligible():
        s = open(path, encoding="utf-8").read()
        kind = classify(s)
        if not kind or kind not in kinds_on:
            continue
        new = apply(s, kind)
        if new == s and "data-dark=" not in s:
            continue   # palette not found: stays on the filter
        n += 1
        kinds[kind] = kinds.get(kind, 0) + 1
        if new != s:
            if check:
                missing += 1
                print("stale or missing:", os.path.relpath(path, ROOT))
            else:
                open(path, "w", encoding="utf-8").write(new)
                changed += 1
    print("%d eligible page(s) %s; %s" % (n, kinds, ("%d need a re-run" % missing) if check else ("%d written" % changed)))
    if check and missing:
        sys.exit(1)

if __name__ == "__main__":
    main()
