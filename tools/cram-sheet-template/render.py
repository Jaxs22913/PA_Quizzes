import colorsys, os, re, sys

_HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = open(os.path.join(_HERE, "template.html"), encoding="utf-8").read()

def hex_to_rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c*2 for c in h)
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#" + "".join(f"{max(0,min(255,int(round(c)))):02x}" for c in rgb)

def mix(hexcolor, target, frac):
    r, g, b = hex_to_rgb(hexcolor)
    tr, tg, tb = target
    return rgb_to_hex((r + (tr-r)*frac, g + (tg-g)*frac, b + (tb-b)*frac))

def tint(hexcolor, frac):
    """Blend toward white by `frac` (0-1) -- consistent pastel regardless of the source hue's own lightness."""
    return mix(hexcolor, (255, 255, 255), frac)

def shade(hexcolor, frac):
    """Blend toward black by `frac` (0-1) -- for a readable dark ink version of an accent color."""
    return mix(hexcolor, (0, 0, 0), frac)

def mnemonic_html(m):
    """Optional "Memory aid" box under a topic's table (criteria tables, see
    README). `m` is raw HTML, or a dict: hook (the one-line hook), key (a list
    of [token, meaning] pairs, or HTML), breaks (optional: where the aid stops
    matching the slide), label (optional, default "Memory aid")."""
    if isinstance(m, str):
        body = f"<p>{m}</p>"
        label = "Memory aid"
    else:
        label = m.get("label", "Memory aid")
        parts = [f'<p class="mnem-hook">{m["hook"]}</p>']
        key = m.get("key")
        if key:
            if isinstance(key, str):
                parts.append(f'<p class="mnem-key">{key}</p>')
            else:
                spans = "".join(f"<span><b>{tok}</b> {meaning}</span>" for tok, meaning in key)
                parts.append(f'<p class="mnem-key">{spans}</p>')
        if m.get("breaks"):
            parts.append(f'<p class="mnem-brk"><b>Where it breaks:</b> {m["breaks"]}</p>')
        body = "".join(parts)
    return (f'\n    <div class="mnem"><div class="mnem-k">{label}</div>'
            f'{body}</div>')

def topic_html(topic):
    acc = topic["color"]
    acc_bg = tint(acc, 0.86)
    acc_zebra = tint(acc, 0.93)
    acc_ink = shade(acc, 0.22)
    tid = topic["id"]
    label = topic["label"]
    tag = topic.get("tag", "")
    tag_html = f'<span class="tag">{tag}</span>' if tag else ""
    cols = topic.get("cols")
    if cols:
        # multi-column mode: rows are tuples matching len(cols), or a dict
        # {"group": "..."} for a full-width group-header row (matches the
        # site's existing multi-column reference-table style, e.g. the
        # Anatomy Exam 3 Hormones page).
        ncols = len(cols)
        widths = topic.get("widths")   # optional per-column CSS widths
        wattr = (lambda i: f' style="width:{widths[i]}"') if widths else (lambda i: "")
        head_cells = "".join(
            f'<th class="term"{wattr(i)}>{c}</th>' if i == 0 else f'<th{wattr(i)}>{c}</th>'
            for i, c in enumerate(cols)
        )
        row_parts = []
        for r in topic["rows"]:
            if isinstance(r, dict) and "group" in r:
                row_parts.append(f'          <tr><td class="grp" colspan="{ncols}">{r["group"]}</td></tr>')
            elif isinstance(r, dict) and "note" in r:
                # one-line footnote row, e.g. where two slides disagree
                row_parts.append(f'          <tr><td class="rnote" colspan="{ncols}">{r["note"]}</td></tr>')
            else:
                cells = "".join(
                    f'<td class="h">{v}</td>' if i == 0 else f'<td>{v}</td>'
                    for i, v in enumerate(r)
                )
                row_parts.append(f'          <tr>{cells}</tr>')
        rows_html = "\n".join(row_parts)
        head_html = f'<thead><tr>{head_cells}</tr></thead>'
    else:
        rows_html = "\n".join(
            f'          <tr><td class="h">{term}</td><td>{fact}</td></tr>'
            for term, fact in topic["rows"]
        )
        head_html = f"<thead><tr><th class=\"term\">{topic.get('col1', 'Term')}</th><th>{topic.get('col2', 'What you need to know')}</th></tr></thead>"
    mnem = mnemonic_html(topic["mnemonic"]) if topic.get("mnemonic") else ""
    # optional: override the table's 560px min-width (e.g. "0" lets a narrow
    # criteria table fit a phone instead of scrolling sideways)
    mw = topic.get("min_width")
    table_open = f'<table style="min-width:{mw}">' if mw is not None else "<table>"
    return f"""  <section class="topic" id="{tid}" style="--acc:{acc};--acc-bg:{acc_bg};--acc-zebra:{acc_zebra};--acc-ink:{acc_ink}">
    <div class="shead"><span class="dot" style="background:{acc}"></span><h2>{label}{tag_html}</h2></div>
    <div class="scroll">
      {table_open}
        {head_html}
        <tbody>
{rows_html}
        </tbody>
      </table>
    </div>{mnem}
  </section>"""

def toc_chip(topic):
    acc_ink = shade(topic["color"], 0.22)
    return f'      <a href="#{topic["id"]}" style="color:{acc_ink}"><span class="dot" style="background:{topic["color"]}"></span>{topic.get("toc_label", topic["label"])}</a>'

# CSS for the optional features (mnemonic box, note rows) lives in template.html
# between these markers; it is emitted only when a page uses one of them, so
# every sheet that does not renders byte-identically to before.
_OPT_CSS = re.compile(r"/\*CRAM-OPTIONAL-CSS:BEGIN\*/\n(.*?)/\*CRAM-OPTIONAL-CSS:END\*/\n", re.S)

def _uses_optional(topics):
    for t in topics:
        if t.get("mnemonic"):
            return True
        if t.get("cols") and any(isinstance(r, dict) and "note" in r for r in t["rows"]):
            return True
    return False

def render(*, title, kicker, h1, sub, topics, guide_href, footer_note, primary=None):
    if primary is None:
        primary = topics[0]["color"]
    # a topic with "toc": False gets no chip (e.g. a run of criteria tables that
    # share one chip on the first, whose "toc_label" names the whole run)
    toc_html = "\n".join(toc_chip(t) for t in topics if t.get("toc", True))
    topics_html = "\n\n".join(topic_html(t) for t in topics)
    src = TEMPLATE
    src = _OPT_CSS.sub(lambda m: m.group(1) if _uses_optional(topics) else "", src)
    src = src.replace("__TITLE__", title)
    src = src.replace("__KICKER__", kicker)
    src = src.replace("__H1__", h1)
    src = src.replace("__SUB__", sub)
    src = src.replace("__TOC_CHIPS__", toc_html)
    src = src.replace("__GUIDE_HREF__", guide_href)
    src = src.replace("__TOPICS_HTML__", topics_html)
    src = src.replace("__FOOTER_NOTE__", footer_note)
    src = src.replace("__PRIMARY__", primary)
    # Designed dark mode (tools/dark_tokens.py): opt in and derive the page's
    # dark palette, per-topic colours included.
    sys.path.insert(0, os.path.dirname(_HERE))
    import dark_tokens
    return dark_tokens.apply(src, "cram")
