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

Kinds: quiz, guide, cram, chart (the --c-* comparison charts) and ref (the
older Pharmacology I reference sheets: --ink/--body/--paper/--navy/--indigo/
--ice, .hero, .toc, .scroll tables; added 2026-09-28, which also repairs their
light-mode contrast and the gram-coverage page's undefined filter variables).

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
KINDS = ("quiz", "guide", "cram", "chart", "ref")
# Pages that ship their own bespoke component set the theme.css block does not
# cover; they keep the invert filter until someone maps their components.
EXCLUDE = set()
# Pages on the shared template's palette that also carry their OWN hard-coded
# light components (cards, tables, chips set in the page CSS). They get the
# generic light-surface pass in light_surface_rules() on top of their kind.
BESPOKE = {"Physical Diagnosis 2 Exam 1/pd2-ent-osce-study-guide.html"}
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

ZEBRA = "#21242a"   # card + 3.5% white, the zebra row every kind uses

def chart_tokens(v):
    """Comparison charts (the --c-* palette: CMS derm/ophtho/ENT, derm staging,
    PD2 ENT OSCE chart). Text roles lifted against the lightest dark ground a
    cell can have (a zebra row or the panel tint); the giveaway column gets
    its own gold tint. Fills that carry white text (--acc in the header row,
    --acc2 section rows, --c-gv-h) keep their light values."""
    panel = soft(hue_of(v["acc"]))
    grounds = (CARD, ZEBRA, panel)
    worst = max(grounds, key=lambda c: lum(hex_rgb(c)))
    t = {"page": PAGE, "ink": INK, "muted": MUTED, "line": LINE, "card": CARD,
         "acc-l": v["acc"], "acc": lift(v["acc"], worst),
         "c-line": LINE, "c-tbl": CARD, "c-zebra": ZEBRA, "c-fg": INK,
         "c-panel": panel, "c-panel-fg": INK, "c-btn-bg": CARD,
         "c-mute": MUTED, "c-mute2": MUTED, "c-pt": MUTED}
    for k, target in (("c-name", TARGET), ("c-b", 7.0), ("c-warn", TARGET),
                      ("c-labs-h", TARGET), ("c-dup", TARGET)):
        if k in v:
            t[k] = lift(v[k], worst, target)
    if "c-gv-bg" in v:
        gv = soft(hue_of(v["c-gv-bg"]))
        t["c-gv-bg"] = gv
        if "c-gv-b" in v:
            t["c-gv-b"] = lift(v["c-gv-b"], gv)
    return t

_RULE = re.compile(r"([^{}]+)\{([^{}]*)\}")

# selectors the shared theme.css already themes; a bespoke pass must not fight it
_SHARED_CHROME = re.compile(r"^(?:header\.top|nav\.toc|body|html)\b")

def light_surface_rules(s, tok=None):
    """Dark equivalents for the hard-coded LIGHT surfaces a bespoke page sets in
    its own CSS (white cards and tables, pale tinted callouts and chips): a
    near-white surface becomes the card, a tint becomes the dark tint of its own
    hue, and a text colour set in the same rule is lifted with the site recipe
    against the new ground. Gradients, fills that carry white text and the
    shared chrome are left alone."""
    pre = ':root[data-theme="dark"] body[data-dark="tokens"] '
    css = re.sub(r"/\*.*?\*/", "", "".join(re.findall(r"<style[^>]*>(.*?)</style>", s, re.S)), flags=re.S)
    out = []
    for sel, body in _RULE.findall(css):
        sel = sel.strip()
        if (not sel or sel.startswith("@") or "data-theme" in sel or ":root" in sel or "{" in sel
                or "gradient" in body or _SHARED_CHROME.match(sel)):
            continue
        # a fill drawn from a palette variable under white text keeps its LIGHT
        # partner (the lifted value is a text colour: white on it is ~3.4:1)
        bv = re.search(r"(?<![-\w])background(?:-color)?\s*:\s*var\(--([\w-]+)\)", body)
        if (bv and tok and (bv.group(1) + "-l") in tok
                and re.search(r"(?<![-\w])color\s*:\s*#fff(?:fff)?\b", body)):
            out.append(",".join(pre + x.strip() for x in sel.split(",")) + "{background:var(--%s-l)}" % bv.group(1))
            continue
        bg = re.search(r"(?<![-\w])background(?:-color)?\s*:\s*(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})\b", body)
        if not bg or lum(hex_rgb(bg.group(1))) <= 0.55:
            continue
        h = bg.group(1)
        dark = CARD if contrast(hex_rgb(h), hex_rgb("#ffffff")) < 1.12 else soft(hue_of(h))
        decl = "background:%s" % dark
        cm = re.search(r"(?<![-\w])color\s*:\s*(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})\b", body)
        if cm and contrast(hex_rgb(cm.group(1)), hex_rgb(dark)) < 4.5:
            decl += ";color:%s" % lift(cm.group(1), dark)
        # text set from a palette variable: shared theme.css re-points every guide
        # <th> at the LIGHT palette (so header cells keep their fill), which would
        # leave a row-header cell dark-on-dark; use the page's lifted value literally
        vm = re.search(r"(?<![-\w])color\s*:\s*var\(--([\w-]+)\)", body)
        if vm and tok and vm.group(1) in tok:
            decl += ";color:%s" % tok[vm.group(1)]
        out.append(",".join(pre + x.strip() for x in sel.split(",")) + "{" + decl + "}")
    return "".join(out)

def ref_tokens(v):
    """Pharmacology I reference sheets (the older hand-built template: --ink
    --body --muted --line --paper --card --navy --indigo --gold --ice, .hero,
    .toc, .scroll tables). Same recipe as the quiz kind, on the same variable
    names, so the page's own CSS goes dark by itself once the variables move.
    --navy and --indigo become TEXT/accent values; anything that uses them as a
    FILL under white text (the table header) is re-pointed at the -l partner
    in ref_rules()."""
    ice = soft(hue_of(v["indigo"]))
    return {
        "navy-l": v["navy"], "indigo-l": fill(v["indigo"], v["navy"]),
        "navy": lift(v["navy"], ice, 7.0), "indigo": lift(v["indigo"], ice),
        "gold": v["gold"], "ice": ice,
        "ink": INK, "body": INK, "muted": MUTED, "line": LINE, "paper": PAGE, "card": CARD,
        "shadow": "0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.35)",
    }

INLINE_FG = re.compile(r'style="[^"]*?(?<![-\w])color:\s*(#[0-9a-fA-F]{6})')

def ref_rules(s):
    """Rules a reference sheet needs beyond its variables.

    Both themes: the gram-coverage sheet's filter buttons read --acc, --c-line,
    --c-btn-bg, --c-fg and --c-mute, which that page never defines (the active
    button was white text on nothing); define them from the page's own palette.
    thead th.dn / th.sl (header cells that also carry the body-cell classes) were ink / grey on navy, 1.79:1; header text is always white.
    Dark only: the table header keeps its LIGHT navy fill, zebra rows and the
    contraindication tints (hard-coded light in the page CSS) go dark, and any
    dark-on-white text colour set inline is lifted with the site recipe."""
    both = ('body[data-dark="tokens"]{--acc:var(--indigo);--c-line:var(--line);--c-btn-bg:var(--card);'
            '--c-fg:var(--ink);--c-mute:var(--muted)}'
            'body[data-dark="tokens"] thead th{color:#fff}')
    # a fill under white text (the gram key's olive "moderate" cell was 4.46:1):
    # white-on-fill must clear 4.5:1 in BOTH themes, so solve it once for both
    css = re.sub(r"/\*.*?\*/", "", "".join(re.findall(r"<style[^>]*>(.*?)</style>", s, re.S)), flags=re.S)
    for sel, decl in _RULE.findall(css):
        sel = sel.strip()
        bg = _BG.search(decl)
        if (bg and re.search(r"(?<![-\w])color\s*:\s*#fff(?:fff)?\b", decl)
                and "data-theme" not in sel and not sel.startswith("@") and "{" not in sel):
            f = darken_to(bg.group(1), "#ffffff")
            if f != bg.group(1):
                both += "".join('body[data-dark="tokens"] %s{background:%s}' % (one.strip(), f) for one in sel.split(","))
    pre = ':root[data-theme="dark"] body[data-dark="tokens"] '
    red = soft(hue_of("#b3261e"))
    rules = [
        "thead th{background:var(--navy-l)}",
        "tbody tr:nth-child(even){background:%s}" % ZEBRA,
        "tr.t-abs td,tr.t-bbw td,tr.t-abs:nth-child(even) td,tr.t-bbw:nth-child(even) td{background:%s}" % red,
        ".note{border-color:%s}" % LINE,
        ".note.warn{background:%s;border-color:#5a2a2c}" % red,
        ".gf.on{background:var(--indigo-l);border-color:var(--indigo-l)}",
    ]
    for h in sorted(set(INLINE_FG.findall(s))):
        if contrast(hex_rgb(h), hex_rgb(ZEBRA)) < 4.5:
            rules.append('[style*="color:%s"]{color:%s!important}' % (h, lift(h, ZEBRA)))
    # per-card colour set as an inline custom property (--cc, --rc: the group
    # cards' heading text and left border). Lifted only when the stylesheet
    # uses it as text/border and never as a fill, so no white-on-fill pair breaks.
    css = re.sub(r"/\*.*?\*/", "", "".join(re.findall(r"<style[^>]*>(.*?)</style>", s, re.S)), flags=re.S)
    for name, h in sorted(set(re.findall(r'style="[^"]*?--([\w-]+):\s*(#[0-9a-fA-F]{6})', s))):
        uses = [(prop, val) for _sel, body in _RULE.findall(css) for prop, val in re.findall(r"([\w-]+)\s*:\s*([^;]*)", body)
                if "var(--%s)" % name in val]
        if uses and all(prop == "color" or prop.startswith("border") for prop, _ in uses) \
                and contrast(hex_rgb(h), hex_rgb(CARD)) < 4.5:
            rules.append('[style*="--%s:%s"]{--%s:%s!important}' % (name, h, name, lift(h, CARD)))
    def scoped(rule):
        # every selector of a comma list needs the dark prefix, not just the first
        sel, _, decl = rule.partition("{")
        return ",".join(pre + x.strip() for x in sel.split(",")) + "{" + decl
    return both + "".join(scoped(r) for r in rules)

_COLOR = re.compile(r"(?<![-\w])color\s*:\s*(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})\b")

def fixed_text_rules(s):
    """Dark rules for text colours a chart hard-codes in its own CSS (urgency
    labels, coverage keys): each dark-on-white hex is lifted with the recipe
    against the zebra row, keeping its hue. Rules with a background of their
    own (a filled chip) are left alone."""
    out = []
    for block in re.findall(r"<style[^>]*>(.*?)</style>", s, re.S):
        css = re.sub(r"/\*.*?\*/", "", block, flags=re.S)
        css = re.sub(r"@media print\s*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}", "", css)
        for sel, body in _RULE.findall(css):
            sel = sel.strip()
            if sel.startswith((":root", "@")) or "data-theme" in sel:
                continue
            pre = lambda: ",".join(':root[data-theme="dark"] body[data-dark="tokens"] ' + x.strip()
                                   for x in sel.split(","))
            # a hard-coded white surface (TOC pills, figure frames) -> the card;
            # image backgrounds stay white for transparent slide captures
            if re.search(r"background(?:-color)?\s*:\s*#fff(?:fff)?\b", body) and "img" not in sel:
                out.append(pre() + "{background:%s}" % CARD)
            if "background" in body:
                continue
            for h in _COLOR.findall(body):
                if contrast(hex_rgb(h), hex_rgb(CARD)) < 4.5:
                    out.append(pre() + "{color:%s}" % lift(h, ZEBRA))
    # group chips carry an inline fill under white text
    for g in sorted(set(re.findall(r'class="grp" style="background:(#[0-9a-fA-F]{6})"', s))):
        f = darken_to(g, "#ffffff")
        if f != g:
            # white text on the chip must clear 4.5:1 in BOTH themes (the light
            # value of the ophtho gold was 3.25:1, the ENT olive 4.46:1)
            out.append('body[data-dark="tokens"] .grp[style*="background:%s"]{background:%s!important}' % (g, f))
    return "".join(out)

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
    if "--c-panel" in s and "--acc:" in first_root_block(s):
        return "chart"
    root = first_root_block(s)
    if 'class="hero"' in s and all(("--%s:" % n) in root for n in ("body", "paper", "navy", "indigo", "ice")):
        return "ref"
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
    if kind == "chart":
        v = {m.group(1): m.group(2) for m in re.finditer(r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})\b", root)}
        return chart_tokens(v) if "acc" in v else None
    if kind == "ref":
        v = {n: get(n) for n in ("navy", "indigo", "gold", "ice")}
        return ref_tokens(v) if all(v.values()) else None

BOOT = ("<script>document.documentElement.setAttribute('data-theme', localStorage.getItem('siteTheme')"
        " || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));</script>")

BEGIN, END = "<!--DARK-TOKENS:BEGIN (tools/dark_tokens.py)-->", "<!--DARK-TOKENS:END-->"

TOPIC = re.compile(r'<section class="topic" id="([^"]+)" style="--acc:(#[0-9a-fA-F]{3,6})')

def cram_topic_rules(s):
    """Cram sheets colour each topic inline (--acc/--acc-bg/--acc-zebra/--acc-ink
    on the <section>, a dark ink on its TOC chip). Inline custom properties only
    lose to an !important stylesheet declaration, hence the !important here."""
    out = []
    for tid, acc in TOPIC.findall(s):
        H = hue_of(acc)
        bg = soft(H)
        # the term cell sits on the tint, the card, or a zebra row (card + 3.5%
        # white = #21242a); solve against whichever is lightest
        worst = max((bg, CARD, "#21242a"), key=lambda c: lum(hex_rgb(c)))
        ink = lift(acc, worst)
        out.append('#%s{--acc-bg:%s!important;--acc-zebra:rgba(255,255,255,.035)!important;--acc-ink:%s!important}'
                   % (tid, bg, ink))
        out.append('.toc a[href="#%s"]{color:%s!important}' % (tid, lift(acc, CARD)))
    pre = ':root[data-theme="dark"] body[data-dark="tokens"] '
    return "".join(pre + r for r in out)


# ------------------------------------------------ light-mode contrast repairs
# (2026-09-27, design-review leftovers item 1). Several templates set a mid-
# light palette colour as TEXT or as a FILL under white text, 2.0-4.46:1 in
# LIGHT mode. Each such colour gets a light "-t" partner: itself when it already clears 4.5:1, else
# the same hue re-solved with the site recipe to 4.60:1 against the darkest
# light surface it sits on, chroma capped at its own (gold stays gold, just
# deeper). White text on a -t fill then also clears 4.60:1. theme.css
# re-points the page variables at these only under data-theme="light", so
# dark mode is untouched.
LIGHT_TARGET = 4.60

def darken_to(hexc, bg, target=LIGHT_TARGET):
    if contrast(hex_rgb(hexc), hex_rgb(bg)) >= 4.5:
        return hexc
    L, C, H = rgb_oklch(hex_rgb(hexc))
    return solve(H, bg, target, cmax=C)

_BG = re.compile(r"background(?:-color)?\s*:\s*(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})\b")

def light_surfaces(s):
    """Solid light backgrounds the page's own first <style> paints text on
    (paper, TOC, IO box, callouts, zebra rows, figures). Code chips, images,
    marks, table headers and dark-mode rules are not text grounds for accents."""
    m = re.search(r"<style[^>]*>(.*?)</style>", s, re.S)
    css = re.sub(r"/\*.*?\*/", "", m.group(1), flags=re.S) if m else ""
    out = []
    for sel, body in _RULE.findall(css):
        if re.search(r"code|img|mark|prof|\bth\b|data-theme|kbd|@media|header", sel):
            continue
        for h in _BG.findall(body):
            if lum(hex_rgb(h)) > 0.55:
                out.append(h)
    root = first_root_block(s)
    for n in ("paper", "page", "card", "ice"):
        h = (VAR(n).search(root) or [None, None])[1]
        if h:
            out.append(h)
    return out or ["#ffffff"]

def darkest(cols):
    return min(cols, key=lambda c: lum(hex_rgb(c)))

INLINE_ACC = re.compile(r'class="test-yourself-btn"[^>]*style="--acc:(#[0-9a-fA-F]{3,6})')
INLINE_TOPLINK = re.compile(r'class="top-link"[^>]*style="color:\s*(#[0-9a-fA-F]{3,6})')

def light_tokens(kind, s):
    """The LIGHT-mode block: -t tokens on body, plus rules for colours a page
    sets inline (a stylesheet only beats an inline custom property with
    !important), all under data-theme="light"."""
    root = first_root_block(s)
    get = lambda n: (VAR(n).search(root) or [None, None])[1]
    worst = darkest(light_surfaces(s))
    tok, rules = {}, []
    pre = ':root[data-theme="light"] body[data-dark="tokens"] '
    if kind == "guide":
        for k in ("accent", "accent2", "accent3"):
            if get(k):
                tok[k + "-t"] = darken_to(get(k), worst)
        for acc in sorted(set(INLINE_ACC.findall(s))):
            f = darken_to(acc, "#ffffff")
            if f != acc:
                rules.append('.test-yourself-btn[style*="--acc:%s"]{--acc:%s!important}' % (acc, f))
        for col in sorted(set(INLINE_TOPLINK.findall(s))):
            t = darken_to(col, worst)
            if t != col:
                rules.append('nav.toc a.top-link[style*="%s"]{color:%s!important}' % (col, t))
    elif kind == "quiz":
        # the failing pairs are all on the white card: white text on the
        # filled buttons, and Back / Flag / "N left" text on the card
        ground = get("card") or "#ffffff"
        for k in ("navy", "indigo"):
            if get(k):
                tok[k + "-t"] = darken_to(get(k), ground)
    elif kind == "cram":
        if get("primary"):
            tok["primary-t"] = darken_to(get("primary"), worst)
        # topic term cells take an inline --acc-ink; on the topic's zebra row
        # a few measured 4.40-4.50:1
        for tid, style in re.findall(r'<section class="topic" id="([^"]+)" style="([^"]*)"', s):
            v = dict(re.findall(r"--([\w-]+):(#[0-9a-fA-F]{3,6})", style))
            if "acc-ink" not in v:
                continue
            ground = darkest([v[k] for k in ("acc-bg", "acc-zebra") if k in v] + ["#ffffff"])
            ink = darken_to(v["acc-ink"], ground)
            if ink != v["acc-ink"]:
                rules.append('#%s{--acc-ink:%s!important}' % (tid, ink))
    elif kind == "chart":
        # a palette colour used as TEXT on the white/zebra ground (the derm
        # staging chart's gold source line was 3.04:1): solve it in light only
        root_vars = dict(re.findall(r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{6})\b", root))
        css = re.sub(r"/\*.*?\*/", "", "".join(re.findall(r"<style[^>]*>(.*?)</style>", s, re.S)), flags=re.S)
        for sel, decl in _RULE.findall(css):
            sel = sel.strip()
            m = re.search(r"(?<![-\w])color\s*:\s*var\(--([\w-]+)\)", decl)
            if (m and m.group(1) in root_vars and "background" not in decl
                    and "data-theme" not in sel and not sel.startswith("@") and "{" not in sel):
                t = darken_to(root_vars[m.group(1)], worst)
                if t != root_vars[m.group(1)]:
                    for one in sel.split(","):
                        rules.append("%s{color:%s}" % (one.strip(), t))
        # the giveaway header cell: pale text on the gold fill was 3.99:1
        if "th.gv-h" in s:
            rules.append("th.gv-h,th.gv-h span{color:#fff!important}")   # the span carries an inline pale colour
    elif kind == "ref":
        # muted grey text sat at 4.33-4.46:1 on the zebra row and the tints
        if get("muted"):
            tok["muted"] = darken_to(get("muted"), worst)
        # dark-on-light text colours set inline (a gold TOC chip was 3.25:1)
        for h in sorted(set(INLINE_FG.findall(s))):
            t = darken_to(h, worst)
            if t != h:
                rules.append('[style*="color:%s"]{color:%s!important}' % (h, t))
    body = "".join("--%s:%s;" % kv for kv in tok.items())
    head = (':root[data-theme="light"] body[data-dark="tokens"]{%s}' % body) if body else ""
    return head + "".join(pre + r for r in rules)

def block(tok, extra=""):
    body = "".join("--%s:%s;" % kv for kv in tok.items())
    return ('%s<style id="dark-tokens">:root[data-theme="dark"] body[data-dark="tokens"]{%s}%s</style>%s'
            % (BEGIN, body, extra, END))

def apply(s, kind=None, bespoke=False):
    """Return the page with the opt-in attribute and a fresh token block."""
    kind = kind or classify(s)
    if not kind:
        return s
    tok = tokens_for(kind, s)
    if not tok:
        return s
    s = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?", "", s, flags=re.S)
    if bespoke:
        # palette variables the kind does not know (a page's own --warn rust,
        # used as heading text) still need lifting for the dark ground
        css_all = "".join(re.findall(r"<style[^>]*>(.*?)</style>", s, re.S))
        for name, h in re.findall(r"--([\w-]+)\s*:\s*(#[0-9a-fA-F]{6})\b", first_root_block(s)):
            if (name not in tok and not name.endswith(("-l", "-t"))
                    and re.search(r"(?<![-\w])color\s*:\s*var\(--%s\)" % re.escape(name), css_all)
                    and contrast(hex_rgb(h), hex_rgb(ZEBRA)) < 4.5):
                tok[name] = lift(h, ZEBRA)
    extra = ((cram_topic_rules(s) if kind == "cram" else "")
             + (fixed_text_rules(s) if kind in ("chart", "ref") else "")
             + (ref_rules(s) if kind == "ref" else "")
             + (light_surface_rules(s, tok) if bespoke else "")
             + light_tokens(kind, s))
    s = s.replace("</head>", block(tok, extra) + "\n</head>", 1)
    # Every page needs the one-line theme bootstrap before first paint;
    # theme.js only toggles data-theme, it never sets it on load. The five
    # comparison charts shipped without it, so they never went dark at all.
    if "setAttribute('data-theme'" not in s:
        s = re.sub(r"(<meta charset=[^>]*>)", r"\1\n" + BOOT.replace("\\", "\\\\"), s, count=1)
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
        new = apply(s, kind, os.path.relpath(path, ROOT) in BESPOKE)
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
