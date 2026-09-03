#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Put a FIRST-LINE treatment table into every section of the CMS I Exam 2
(ophthalmology) study guide.

Jaxon, 2026-09-03: "For the CMS guides do the First line part of the guides
like you did for the derm guide." The dermatology guide got one on 2026-08-27
(add_guide_derm_treatment.py); the ophthalmology guide had no treatment summary
at all -- "First line" appeared in it zero times.

Same source discipline as the derm version: this reads the generated comparison
chart and reuses its treatment column, so the guide cannot drift from the chart
and one correction fixes both.

BUT THE CUT IS NOT THE SAME, because the two charts are not written the same
way. Derm's column is literally "First line -> second line treatment", a ladder
in every one of its 146 rows. This one is "Treatment & how fast", a complete
short plan, and ONLY 10 OF 81 ROWS ESCALATE AT ALL.

That matters because the obvious rule -- cut at the first arrow -- is wrong
here. In this chart an arrow almost always means "in this case, do this":

    Immunocompetent adult &rarr; topical broad-spectrum antibiotic
    Mild &rarr; outpatient oral antibiotics
    Inflammatory &rarr; corticosteroids. Viral &rarr; cool compresses.

Cutting those at the arrow would leave "Immunocompetent adult". So escalation is
recognised by an explicit FAILURE or PERSISTENCE trigger, or by a trailing
definitive-surgery clause, and the cut is taken at the EARLIEST such marker --
not the last, which left the laser step sitting in the glaucoma row.

A THIRD COLUMN THE DERM TABLE DOES NOT HAVE. This chart's column is "Treatment
& HOW FAST", and in ophthalmology the urgency is the examinable half -- emergent
versus routine changes the answer more often than the drug does. It is carried
across as its own column rather than dropped.

RUN ORDER. After build_cms_ophtho_chart.py and fix_ophtho_urgency_class.py.
Idempotent -- each block is fenced in <!--OPHTX--> markers and stripped before
re-inserting.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2")
GUIDE = os.path.join(DIR, "cms-exam-2-study-guide.html")
CHART = os.path.join(DIR, "cms-ophtho-comparison-chart.html")

FENCE_OPEN, FENCE_CLOSE = "<!--OPHTX-->", "<!--/OPHTX-->"

# the chart's lecture badge -> the guide section it belongs to
SECTION_FOR_LECTURE = {
    "L10": "ophthalmology-i", "L11": "neuro-ophthalmology",
    "L12": "acute-vision-loss", "L13": "chronic-vision-loss",
    "L14": "ocular-trauma",
}

# A sentence is beyond first line if its PLAIN TEXT starts with one of these.
# Tested on the tag-stripped sentence, not the raw HTML: the chart writes
# "<b>Laser trabeculoplasty</b> if refractory", so a raw-string match for
# "Laser trabeculoplasty if refractory" never fires.
ESCALATION = re.compile(
    r'^(?:no better after'
    r'|persistent\b(?=.*&rarr;|.*\u2192)'
    r'|no spontaneous resolution'
    r'|surgery is definitive'
    r'|surgery if '
    r'|laser trabeculoplasty if refractory'
    r')', re.I)


def _sentences(html_):
    """Split on sentence ends that are OUTSIDE a tag, so every piece keeps its
    own balanced markup."""
    parts, depth, start = [], 0, 0
    for i, ch in enumerate(html_):
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth = max(0, depth - 1)
        elif ch == "." and depth == 0:
            j = i + 1
            while j < len(html_) and html_[j] in "<>/bi ":       # step over "</b> "
                if html_[j] == " ":
                    parts.append(html_[start:j]); start = j + 1
                    break
                j += 1
            else:
                if j >= len(html_):
                    parts.append(html_[start:]); start = len(html_)
    if start < len(html_):
        parts.append(html_[start:])
    return [p for p in (x.strip() for x in parts) if p]


def first_line(cell):
    """The treatment cell with the urgency badge and any escalation removed."""
    m = re.search(r'<span class="u [a-z]+">(.*?)</span>', cell, re.S)
    urgency = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""
    tx = re.sub(r'<span class="u [a-z]+">.*?</span>', "", cell, flags=re.S).strip()

    kept = []
    for seg in _sentences(tx):
        plain = re.sub(r"<[^>]+>", "", seg).strip()
        if ESCALATION.search(plain):
            break
        kept.append(seg)
    tx = " ".join(kept).strip() if kept else tx

    # "First-line latanoprost..." is redundant under a heading that says First line.
    tx = re.sub(r"^\s*First[- ]line\s+", "", tx, flags=re.I)
    tx = re.sub(r"^\s*<b>\s*</b>\s*", "", tx)
    tx = re.sub(r"\s+", " ", tx).strip().rstrip(";,").strip()
    # Stripping a label can leave the sentence starting lower case.
    mm = re.match(r"((?:<[^>]+>|\s)*)([a-z])", tx)
    if mm:
        tx = tx[:mm.start(2)] + mm.group(2).upper() + tx[mm.end(2):]
    if tx and not tx.endswith((".", "!", "?", ">")):
        tx += "."
    return tx, urgency


def chart_rows():
    src = open(CHART, encoding="utf-8").read()
    body = src[src.find("<tbody>"):]
    out = []
    for r in re.findall(r'<tr data-g="[^"]*"[^>]*>(.*?)</tr>', body, re.S):
        tds = re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)
        if len(tds) < 8:
            continue
        nm = re.search(r"<b>(.*?)</b>", tds[1])
        name = re.sub(r"<[^>]+>", "", nm.group(1)).strip() if nm else ""
        lec = re.search(r'<b class="lect">([^<]*)</b>', tds[1])
        lec = lec.group(1).strip() if lec else ""
        tx, urg = first_line(tds[7])
        assert name, "row with no condition name"
        assert re.sub(r"<[^>]+>", "", tx).strip(), "no first line left for %r" % name
        out.append((lec, name, tx, urg))
    assert len(out) >= 78, "only parsed %d chart rows -- markup changed?" % len(out)
    return out


def block(rows):
    trs = "".join(
        '<tr><td class="txc">%s</td><td>%s</td><td class="txu">%s</td></tr>' % (n, tx, u)
        for _l, n, tx, u in rows)
    return ('%s\n  <p class="figgrid-h">First-line treatment</p>\n'
            '  <p class="txnote">Every condition in this lecture, with <b>what you reach for '
            'first</b> and <b>how fast</b> &mdash; which in ophthalmology is half the answer. '
            'Where the deck escalates after a failed trial, only the first step is here; the '
            'full ladder and the reasoning are in the '
            '<a href="cms-ophtho-comparison-chart.html">comparison chart</a>.</p>\n'
            '  <table class="txtab"><tr><th>Condition</th><th>First line</th>'
            '<th class="txu">How fast</th></tr>%s</table>\n  %s'
            % (FENCE_OPEN, trs, FENCE_CLOSE))


CSS = """
  /* First-line treatment tables (add_guide_ophtho_treatment.py). The condition
     column is held narrow so the treatment text gets the width; the urgency
     column is narrower still and never wraps mid-word. */
  .txnote{font-size:13px;line-height:1.5;color:var(--soft);margin:0 0 10px}
  table.txtab td.txc{width:200px;font-weight:700;vertical-align:top}
  table.txtab td{vertical-align:top;font-size:14px;line-height:1.5}
  table.txtab .txu{width:120px;font-size:12.5px;line-height:1.4}
  table.txtab td.txu{font-weight:700}
  @media(max-width:700px){
    table.txtab td.txc{width:auto;display:block;border-bottom:none;padding-bottom:0}
    table.txtab td:not(.txc){display:block;border-top:none;padding-top:3px}
    table.txtab .txu{width:auto}
  }
"""


def main():
    src = open(GUIDE, encoding="utf-8").read()
    src = re.sub(re.escape(FENCE_OPEN) + r".*?" + re.escape(FENCE_CLOSE) + r"\s*",
                 "", src, flags=re.S)

    by_section = {}
    for lec, name, tx, urg in chart_rows():
        sid = SECTION_FOR_LECTURE.get(lec)
        assert sid, "lecture %r has no guide section" % lec
        by_section.setdefault(sid, []).append((lec, name, tx, urg))

    n_tables = n_rows = 0
    for sid, items in by_section.items():
        i = src.find('<section class="deck" id="%s"' % sid)
        assert i > -1, "guide has no section %r" % sid
        end = src.find("</section>", i)
        assert end > -1
        btn = src.rfind('<button type="button" class="test-yourself-btn"', i, end)
        at = btn if btn > -1 else end
        src = src[:at] + block(items) + "\n  " + src[at:]
        n_tables += 1
        n_rows += len(items)

    if ".txnote{" not in src:
        src = src.replace("</style>", CSS + "</style>", 1)

    open(GUIDE, "w", encoding="utf-8").write(src)
    print("wrote %d first-line tables, %d conditions, into %s"
          % (n_tables, n_rows, os.path.basename(GUIDE)))
    for sid, items in by_section.items():
        print("   %-22s %d" % (sid, len(items)))


if __name__ == "__main__":
    main()
