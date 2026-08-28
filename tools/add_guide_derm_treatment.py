#!/usr/bin/env python3
"""Put a FIRST-LINE treatment table into every dermatology section of the CMS I
Exam 1 study guide.

Jaxon, 2026-08-27: "For the derm guide I dont see treatments on there can you
add them. First line only." He was right -- the guide taught recognition,
pathophysiology and testing, and then stopped. Second line is deliberately not
here; he asked for first line only, and the comparison chart already carries the
full ladder for anyone who wants it.

WHERE THE TREATMENTS COME FROM. Not re-derived from the decks: this reads the
generated comparison chart and reuses its treatment column, the same way
add_guide_derm_images.py reuses its image mapping. That column has already been
checked against the PowerPoints, so the guide cannot drift away from the chart,
and a correction to one is a correction to both.

HOW "FIRST LINE" IS DECIDED. Not by looking for a "1st:" label -- only 31 of the
146 rows carry a bare one. The rest say "1st (mild):", "1st (limited):", "Urgent
treatment needed. 1st:", "Male-pattern: ...", "Supportive.", or "No treatment
needed". So the rule is positional instead: first line is everything in the cell
BEFORE the "2nd" marker, which holds for all 146 rows including the ones that
never mention a first line explicitly.

RUN ORDER. After build_cms_derm_chart.py. Idempotent -- each block is fenced in
<!--DERMTX--> markers and stripped before re-inserting.
"""
import os, re, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
GUIDE = os.path.join(DIR, "cms-exam-1-study-guide.html")
CHART = os.path.join(DIR, "cms-derm-comparison-chart.html")

FENCE_OPEN, FENCE_CLOSE = "<!--DERMTX-->", "<!--/DERMTX-->"

# lecture number in the chart's section label -> the guide section it belongs to
SECTION_FOR_LECTURE = {
    2: "general-derm-1", 3: "general-derm-2", 4: "cutaneous-bacterial",
    5: "derm-infestations", 6: "viral-fungal", 7: "benign-skin-lesions",
    8: "pigmented-lesions", 9: "malignant-lesions",
}

SECOND_LINE = re.compile(r"<br>\s*<b>2nd\b.*$", re.S)


def chart_treatments():
    """[(lecture number, condition, first-line html)] in chart order."""
    src = open(CHART, encoding="utf-8").read()
    body = src[src.find("<tbody>"):]
    out, lecture = [], None
    for r in re.findall(r"<tr(?: class=\"sec\")?[^>]*>(.*?)</tr>", body, re.S):
        if "colspan" in r:
            label = " ".join(re.sub("<[^>]+>", "", r).split())
            m = re.match(r"Lecture (\d+)", label)
            lecture = int(m.group(1)) if m else None
            continue
        tds = re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)
        if len(tds) < 6 or lecture is None:
            continue
        name = " ".join(re.sub("<[^>]+>", " ", tds[1]).split())
        first = SECOND_LINE.sub("", tds[5]).strip()
        # STRIPPING THE "1st" LABEL IS FIDDLIER THAN IT LOOKS. The chart writes it
        # 27 different ways: sometimes the bold span holds only the label
        # (<b>1st:</b>), sometimes the label AND the sentence (<b>1st: penicillin
        # V.</b>), sometimes a band (<b>1st (mild):</b>), sometimes a qualifier
        # (<b>1st oral:</b>, <b>1st and most important:</b>). Matching only the
        # first form left a literal "1st:" sitting in 14 rows of a table already
        # headed "First-line treatment".
        #
        # Bands and qualifiers are KEPT and promoted, because they are the choice
        # being tested; only the redundant "1st" is dropped.
        first = re.sub(r"<b>1st \(([^)]+)\):",
                       lambda m: "<b>%s:" % (m.group(1)[0].upper() + m.group(1)[1:]), first)
        first = re.sub(r"<b>1st and most important:\s*", "<b>Most important: ", first)
        first = re.sub(r"<b>1st (oral|systemic|drug):\s*",
                       lambda m: "<b>%s: " % m.group(1).capitalize(), first)
        first = re.sub(r"<b>1st:\s*</b>\s*", "", first)   # span holding only the label
        first = re.sub(r"<b>1st:\s*", "<b>", first)        # label sharing a span with its text
        first = re.sub(r"<b>\s*</b>", "", first)           # tidy an emptied span
        # NOT lstrip("&mdash;") -- that strips CHARACTERS in that set, so it ate the
        # leading letter of anything starting with a/d/h/m/s: "site-appropriate"
        # became "ite-appropriate", "medium" became "edium", "dapsone" became
        # "psone". Remove a leading dash as a whole token instead.
        first = re.sub(r"^(?:&mdash;|&ndash;|\u2014|\u2013|-)\s*", "", first.strip()).strip()

        # Removing the label can leave a segment starting mid-sentence in lower
        # case -- erysipelas read "...can be rapid. penicillin V." Each cell is a
        # <br>-separated list, so capitalise the first letter of the cell and of
        # every segment after a <br>, stepping over any opening tags first.
        def _cap_segment(seg):
            m = re.match(r"((?:<[^>]+>|\s)*)([a-z])", seg)
            return seg if not m else seg[:m.start(2)] + m.group(2).upper() + seg[m.end(2):]
        first = "<br>".join(_cap_segment(part) for part in first.split("<br>"))
        assert re.sub("<[^>]+>", "", first).strip(), "no first line for %r" % name
        out.append((lecture, name, first))
    assert len(out) >= 140, "only parsed %d chart rows -- markup changed?" % len(out)
    return out


def block(rows):
    trs = "".join(
        '<tr><td class="txc">%s</td><td>%s</td></tr>' % (name, first)
        for _lec, name, first in rows)
    return ('%s\n  <p class="figgrid-h">First-line treatment</p>\n'
            '  <p class="txnote">Every condition in this lecture, with <b>what you reach for '
            'first</b> and nothing else. Where the deck bands treatment by severity or site, '
            'those bands are kept, because that is the choice being tested. Second line, and '
            'the reasoning behind each, are in the '
            '<a href="cms-derm-comparison-chart.html">comparison chart</a>.</p>\n'
            '  <table class="txtab"><tr><th>Condition</th><th>First line</th></tr>%s</table>\n  %s'
            % (FENCE_OPEN, trs, FENCE_CLOSE))


CSS = """
  /* First-line treatment tables (add_guide_derm_treatment.py). The condition
     column is held narrow so the treatment text -- which is the part being
     read -- gets the width. */
  .txnote{font-size:13px;line-height:1.5;color:var(--soft);margin:0 0 10px}
  table.txtab td.txc{width:210px;font-weight:700;vertical-align:top}
  table.txtab td{vertical-align:top;font-size:14px;line-height:1.5}
  @media(max-width:700px){
    table.txtab td.txc{width:auto;display:block;border-bottom:none;padding-bottom:0}
    table.txtab td:last-child{display:block;border-top:none;padding-top:3px}
  }
"""


def main():
    src = open(GUIDE, encoding="utf-8").read()
    # the trailing \s* matters: the insert below adds "\n  " after the fence, and
    # without consuming it here every re-run left another one behind and the file
    # grew 24 bytes a time -- idempotent in content but not on disk
    src = re.sub(re.escape(FENCE_OPEN) + r".*?" + re.escape(FENCE_CLOSE) + r"\s*",
                 "", src, flags=re.S)

    rows = chart_treatments()
    by_section = {}
    for lec, name, first in rows:
        sid = SECTION_FOR_LECTURE.get(lec)
        assert sid, "lecture %d has no guide section" % lec
        by_section.setdefault(sid, []).append((lec, name, first))

    n_tables = n_rows = 0
    for sid, items in by_section.items():
        i = src.find('<section class="deck" id="%s"' % sid)
        assert i > -1, "guide has no section %r" % sid
        end = src.find("</section>", i)
        assert end > -1
        # sit before the Test-yourself button so it stays the last thing in the section
        btn = src.rfind('<button type="button" class="test-yourself-btn"', i, end)
        at = btn if btn > -1 else end
        src = src[:at] + block(items) + "\n  " + src[at:]
        n_tables += 1
        n_rows += len(items)

    if ".txnote{" not in src:
        src = src.replace("</style>", CSS + "</style>", 1)

    open(GUIDE, "w", encoding="utf-8").write(src)
    print("wrote %d first-line treatment tables, %d conditions, into %s"
          % (n_tables, n_rows, os.path.basename(GUIDE)))
    for sid, items in by_section.items():
        print("   %-22s %d" % (sid, len(items)))


if __name__ == "__main__":
    main()
