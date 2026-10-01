#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Pharmacology I Exam 3 reference pages from tools/pharm_e3/*.json.

Pages (each lecture present in tools/pharm_e3 contributes a section, so Lecture 8 is one new JSON file
and a rebuild):
    pharm-exam-3-indications.html        Indications & Patient Education
    pharm-exam-3-side-effects.html       Side Effects & Monitoring (black box warnings flagged)
    pharm-exam-3-contraindications.html  Contraindications & Cautions
    pharm-exam-3-killers-commons-zebras.html
    pharm-exam-3-<slug>.html             one comparison chart per lecture that defines a "chart"
    pharm-exam-3-what-to-star.html       what the lecturers said to star, from the recordings

REFUSES TO WRITE unless check_pharm_e3.py (slides) and check_pharm_e3_wood.py (recordings) pass.
Shares _pharm_ref_shell.page() with the Exam 1 references so the stylesheet cannot drift.

    python3 tools/build_pharm_e3_charts.py
"""
import os, re, subprocess, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _pharm_ref_shell import page
import pharm_e3_lib as L

OUTDIR = os.path.join(ROOT, "Pharmacology I Exam 3")
KICK = "Pharmacology I &middot; Exam 3 &middot; Class of 2028"
COLORS = {"L9": "#3a6ea5", "L10": "#2f7d6d", "L11": "#9c5230", "L12": "#7a4b9a", "L13": "#a04060"}
IND_TIER = {
    "DOC": ("Drug of choice", "#1f5d3a", "The slide says <b>&ldquo;drug of choice&rdquo;</b> (or first-line / preferred) for that indication."),
    "IND": ("Indication", "#5b6472", "A stated indication or use."),
    "EDU": ("Education-heavy", "#9c5230", "The row where the <b>counseling point</b> matters more than the indication."),
    "MON": ("Monitoring", "#7c1d6f", "A target level or laboratory goal."),
}
CON_TIER = {
    "ABS": ("Contraindicated", "#b3261e", "The slide literally says <b>contraindicated</b>."),
    "BBW": ("Black box", "#7a1010", "The slide says <b>black box warning</b>."),
    "AVOID": ("Avoid", "#a24d0d", "The slide says avoid, do not use or cannot use."),
    "NAMED": ("Named reaction", "#7c1d6f", "A named reaction or syndrome."),
    "CAUT": ("Caution", "#5b6472", "A caution the slide states that is not worded as a contraindication."),
}
EXTRA_CSS = """<style>
  tr.grp td{background:var(--ice);color:var(--navy);font-weight:800;font-size:13px;letter-spacing:.04em;text-transform:uppercase;padding:8px 13px}
  .bbwtag{display:inline-block;background:#7a1010;color:#fff;font-size:10.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;border-radius:999px;padding:2px 8px;margin-left:6px;vertical-align:1px}
  .wq{margin:12px 0 10px;padding:13px 16px;border-left:4px solid var(--gold);background:var(--ice);border-radius:0 11px 11px 0}
  .wq p{margin:0;font-size:15.5px;line-height:1.5;font-style:italic}
  .wq footer{margin:8px 0 0;font-size:12.5px;color:var(--muted);font-style:normal;font-weight:600;text-align:left}
  .wq .ts{font-variant-numeric:tabular-nums}
  .rule{background:var(--card);border:1px solid var(--line);border-radius:13px;padding:16px 18px;margin:0 0 14px;box-shadow:var(--shadow)}
  .rule h3{margin:0 0 4px;font-size:17px;color:var(--ink);letter-spacing:-.01em}
  .rule > p{margin:6px 0 0;font-size:14.5px}
  .said{font-size:12px;font-weight:600;color:var(--muted);letter-spacing:.02em;margin-left:6px}
  .kbucket{margin:0 0 22px}
</style>"""


def plain(s):
    return re.sub(r"<[^>]+>", "", s)


def gate():
    for script in ("check_pharm_e3.py", "check_pharm_e3_wood.py"):
        r = subprocess.run([sys.executable, os.path.join(HERE, script)], capture_output=True, text=True)
        print(r.stdout.strip())
        if r.returncode != 0:
            sys.exit("fact-check failed (%s) -- refusing to write the pages" % script)


def lecs():
    return [l for l in L.LECTURES if L.load(l) is not None]


def src(lec, slide):
    return '<td class="sl">%s<br><span class="g">slide %d</span></td>' % (lec, slide)


def table(headers, rows_html):
    th = "".join('<th%s>%s</th>' % (a, h) for h, a in headers)
    return '<div class="scroll"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, "".join(rows_html))


def section(sid, title, tag, inner, note=""):
    return ('<section id="%s"><div class="shead"><span class="dot" style="background:%s"></span><h2>%s <span class="tag">%s</span></h2></div>%s%s</section>'
            % (sid, COLORS.get(sid.upper(), "#9c5230"), title, tag, note, inner))


def grouped(rows, ncols, cellfn, extra_cls=None):
    out, last = [], None
    for r in rows:
        g = r.get("group")
        if g and g != last:
            out.append('<tr class="grp"><td colspan="%d">%s</td></tr>' % (ncols, g)); last = g
        out.append(cellfn(r))
    return out


def lec_label(l):
    return "Lecture %d &mdash; %s" % (L.LECTURES[l]["n"], L.LECTURES[l]["title"])


def write(name, html, rows):
    p = os.path.join(OUTDIR, name)
    open(p, "w", encoding="utf-8").write(html)
    print("wrote %-42s %4d KB  %d rows" % (name, len(html) // 1024, rows))


def with_css(body):
    return EXTRA_CSS + body


def toc_of(ls):
    return "".join('<a href="#%s">L%d %s</a>' % (l.lower(), L.LECTURES[l]["n"], L.LECTURES[l]["title"]) for l in ls)


def build_indications():
    secs, n, ls = [], 0, []
    for l in lecs():
        rows = (L.load(l).get("indications") or [])
        if not rows:
            continue
        ls.append(l); n += len(rows)
        hdr = [("Drug or class", ' class="dn-h"'), ("Tier", ' class="p-h"'), ("Indications", ""), ("Patient education &amp; practical notes", ""), ("Source", ' class="sl-h"')]
        def cell(r, l=l):
            lab, col, _ = IND_TIER[r["tier"]]
            return ('<tr><td class="dn">%s</td><td><span class="pill" style="background:%s">%s</span></td><td class="ct">%s</td><td class="ct">%s</td>%s</tr>'
                    % (r["drug"], col, lab, r["text"], r["edu"], src(l, r["slide"])))
        secs.append(section(l.lower(), lec_label(l), "%d entries" % len(rows), table(hdr, grouped(rows, 5, cell))))
    ndoc = sum(1 for l in ls for r in L.load(l)["indications"] if r["tier"] == "DOC")
    legend = "".join('<span><span class="dot" style="background:%s"></span><b>%s</b> &mdash; %s</span>' % (c, lab, d) for lab, c, d in IND_TIER.values())
    notes = ('<div class="note"><b>Read the green rows first.</b> The slides say <b>&ldquo;drug of choice&rdquo;</b> or first-line for %d indications here, '
             'and a stem that describes a patient is usually asking which drug the slide named for them.</div>'
             '<div class="note warn"><b>No dosages.</b> Dr. Wood said drug dosages are not tested, so routes, timings and durations appear here but milligram doses do not.</div>' % ndoc)
    write("pharm-exam-3-indications.html", page(
        title="Indications &amp; Patient Education &mdash; Pharmacology I Exam 3 (Class of 2028)", kicker=KICK,
        h1="Indications &amp; Patient Education",
        sub="What each drug is FOR, and what you tell the patient. %d entries across the Exam 3 lectures, each citing its slide. Indications and patient education are the two things students under-study most." % n,
        legend=legend, notes=notes, toc=toc_of(ls), body=with_css("\n".join(secs)),
        footer_note="Every row is checked against the slide it cites by <code>tools/check_pharm_e3.py</code> before this page is written."), n)


def build_sideeffects():
    secs, n, ls, nb = [], 0, [], 0
    systems = Counter()
    for l in lecs():
        rows = (L.load(l).get("sideeffects") or [])
        if not rows:
            continue
        ls.append(l); n += len(rows)
        hdr = [("Drug or class", ' class="dn-h"'), ("Side effects", ""), ("Monitoring &amp; what to watch", ""), ("System", ' class="p-h"'), ("Source", ' class="sl-h"')]
        def cell(r, l=l):
            for s in r["system"].split(" / "):
                systems[s.strip()] += 1
            bb = r.get("bbw")
            tag = '<span class="bbwtag">Black box</span>' if bb else ""
            return ('<tr%s><td class="dn">%s%s</td><td class="ct">%s</td><td class="ct">%s</td><td class="ct">%s</td>%s</tr>'
                    % (' class="t-bbw"' if bb else "", r["drug"], tag, r["text"], r["monitor"], r["system"], src(l, r["slide"])))
        nb += sum(1 for r in rows if r.get("bbw"))
        secs.append(section(l.lower(), lec_label(l), "%d entries" % len(rows), table(hdr, grouped(rows, 5, cell))))
    top = ", ".join("<b>%s</b> (%d)" % (k, v) for k, v in systems.most_common(6))
    notes = ('<div class="note"><b>Black box warnings come first.</b> The course director ranks them above ordinary adverse effects; %d rows here carry one and are shaded. '
             'Most common systems: %s.</div>' % (nb, top))
    write("pharm-exam-3-side-effects.html", page(
        title="Side Effects &mdash; Pharmacology I Exam 3 (Class of 2028)", kicker=KICK, h1="Side Effects &amp; Monitoring",
        sub="%d entries across the Exam 3 lectures, each citing its slide, with black box warnings shaded. Companion to the contraindications and indications charts." % n,
        legend='<span>Grouped by class within each lecture; the <b>System</b> column is how a stem gives it to you &mdash; &ldquo;a patient on this drug develops a dry cough&rdquo; is a respiratory question, not a drug-name question.</span>',
        notes=notes, toc=toc_of(ls), body=with_css("\n".join(secs)),
        footer_note="Every row is checked against the slide it cites by <code>tools/check_pharm_e3.py</code> before this page is written."), n)


def build_contra():
    secs, n, ls = [], 0, []
    for l in lecs():
        rows = (L.load(l).get("contra") or [])
        if not rows:
            continue
        ls.append(l); n += len(rows)
        hdr = [("Drug or class", ' class="dn-h"'), ("Tier", ' class="p-h"'), ("Do not use / caution", ""), ("Source", ' class="sl-h"')]
        def cell(r, l=l):
            lab, col, _ = CON_TIER[r["tier"]]
            return ('<tr class="t-%s"><td class="dn">%s</td><td><span class="pill" style="background:%s">%s</span></td><td class="ct">%s</td>%s</tr>'
                    % (r["tier"].lower(), r["drug"], col, lab, r["text"], src(l, r["slide"])))
        secs.append(section(l.lower(), lec_label(l), "%d entries" % len(rows), table(hdr, grouped(rows, 4, cell))))
    legend = "".join('<span><span class="dot" style="background:%s"></span><b>%s</b> &mdash; %s</span>' % (c, lab, d) for lab, c, d in CON_TIER.values())
    notes = '<div class="note"><b>The tier is what the slide actually says.</b> Nothing is promoted above its wording: a caution stays a caution.</div>'
    write("pharm-exam-3-contraindications.html", page(
        title="Contraindications &mdash; Pharmacology I Exam 3 (Class of 2028)", kicker=KICK, h1="Contraindications &amp; Cautions",
        sub="When NOT to give each drug. %d entries across the Exam 3 lectures, each citing its slide and tiered by the strength of the slide&rsquo;s own wording." % n,
        legend=legend, notes=notes, toc=toc_of(ls), body=with_css("\n".join(secs)),
        footer_note="Every row is checked against the slide it cites by <code>tools/check_pharm_e3.py</code> before this page is written."), n)


KCZ_BUCKETS = [
    ("killers", "Killers", "#8c2f22", "Dangerous. <b>Immediate discontinuation and evaluation.</b> Not necessarily common: these are the ones you warn the patient about <i>in advance</i>."),
    ("commons", "Commons", "#6b5312", "What actually happens, often. <b>These belong to the class, not the drug</b>, so they are listed by class."),
    ("zebras", "Zebras", "#5f3a8a", "Uncommon, but <b>unique to one drug</b>. Each is worth about one question, and with the killers they are where to look."),
]


def build_kcz():
    secs, n, ls = [], 0, []
    for l in lecs():
        k = L.load(l).get("kcz") or {}
        if not any(k.get(b[0]) for b in KCZ_BUCKETS):
            continue
        ls.append(l)
        inner = ""
        for key, label, col, blurb in KCZ_BUCKETS:
            rows = k.get(key) or []
            if not rows:
                continue
            n += len(rows)
            hdr = [("Effect", ' class="dn-h"'), ("Drug or class", ' class="p-h"'), ("What it means / what to do", ""), ("Source", ' class="sl-h"')]
            trs = ['<tr><td class="dn">%s</td><td class="ct"><b>%s</b></td><td class="ct">%s</td>%s</tr>' % (r["effect"], r["drugs"], r["what"], src(l, r["slide"])) for r in rows]
            inner += ('<div class="kbucket"><div class="shead"><span class="dot" style="background:%s"></span><h2 style="font-size:17px">%s <span class="tag">%d</span></h2></div>'
                      '<p class="sub" style="margin:0 0 8px">%s</p>%s</div>' % (col, label, len(rows), blurb, table(hdr, trs)))
        secs.append(section(l.lower(), lec_label(l), "", inner))
    notes = ('<div class="note"><b>Dr. Wood&rsquo;s three buckets.</b> He sorts adverse effects into <b>killers</b>, <b>commons</b> and <b>zebras</b>, and said that any time you see a killer or a zebra, '
             'those are the things to look at. The sorting below applies his framework to the slides; each entry cites its slide.</div>')
    write("pharm-exam-3-killers-commons-zebras.html", page(
        title="Killers, Commons and Zebras &mdash; Pharmacology I Exam 3 (Class of 2028)", kicker=KICK, h1="Killers, Commons &amp; Zebras",
        sub="The adverse effects of the Exam 3 lectures sorted the way Dr. Wood sorts them. %d entries." % n,
        legend="", notes=notes, toc=toc_of(ls), body=with_css("\n".join(secs)),
        footer_note="Every entry is checked against the slide it cites by <code>tools/check_pharm_e3.py</code> before this page is written."), n)


def build_charts():
    for l, ch in [(l, c) for l in lecs() for c in L.charts_of(L.load(l))]:
        hdr = [(h, "") for h in ch["headers"]]
        trs = []
        for r in ch["rows"]:
            assert len(r["cells"]) == len(ch["headers"]), (l, r["cells"][0])
            tds = "".join('<td class="%s">%s</td>' % ("dn" if i == 0 else "ct", c) for i, c in enumerate(r["cells"]))
            extra = "".join("<br>slide %d" % a["slide"] for a in r.get("also", []))
            trs.append("<tr>%s%s</tr>" % (tds, src(l, r["slide"]).replace("</span></td>", extra + "</span></td>")))
        hdr.append(("Source", ' class="sl-h"'))
        body = section(l.lower(), lec_label(l), "%d rows" % len(trs), table(hdr, trs), ch.get("notes") and '<div class="note">%s</div>' % ch["notes"] or "")
        write("pharm-exam-3-%s.html" % ch["slug"], page(
            title="%s &mdash; Pharmacology I Exam 3 (Class of 2028)" % ch["title"], kicker=KICK, h1=ch["title"], sub=ch["sub"],
            legend="", notes="", toc="", body=with_css(body),
            footer_note="Every row is checked against the slide it cites by <code>tools/check_pharm_e3.py</code> before this page is written."), len(trs))


WOOD_KINDS = [("marker", "How the lecturer signals emphasis", "#c9a227"), ("rule", "Standing rules: star these wherever they appear", "#b3261e"),
              ("shape", "Test-question shapes said out loud", "#1f5d3a"), ("emphasis", "Specific facts flagged as testable", "#9c5230"),
              ("scope", "Said NOT to be tested or beyond this course", "#5b6472")]


def build_wood():
    import json
    p = os.path.join(L.DATA, "wood.json")
    if not os.path.exists(p):
        return
    d = json.load(open(p, encoding="utf-8"))["entries"]
    order = {l: i for i, l in enumerate(L.LECTURES)}
    secs, toc = [], []
    for kind, title, col in WOOD_KINDS:
        es = sorted([e for e in d if e["kind"] == kind], key=lambda e: (order[e["lec"]], e["at"].zfill(8)))
        if not es:
            continue
        blocks = []
        for e in es:
            blocks.append('<div class="rule"><h3>%s <span class="said">Lecture %d</span></h3>'
                          '<blockquote class="wq"><p>&ldquo;%s&rdquo;</p><footer>%s &middot; <span class="ts">%s</span></footer></blockquote><p>%s</p></div>'
                          % (e["topic"], L.LECTURES[e["lec"]]["n"], e["quote"], lec_label(e["lec"]), e["at"], e["body"]))
        secs.append('<section id="%s"><div class="shead"><span class="dot" style="background:%s"></span><h2>%s <span class="tag">%d</span></h2></div>%s</section>'
                    % (kind, col, title, len(es), "".join(blocks)))
        toc.append('<a href="#%s">%s</a>' % (kind, title))
    notes = ('<div class="note"><b>Why this page is separate.</b> The other Exam 3 charts come from the PowerPoints, which say nothing about what the lecturers weight. This one comes from the <b>recordings</b>, '
             'and every entry is a direct quote with its lecture and timestamp so you can go back and hear it.</div>'
             '<div class="note warn"><b>On the quotes.</b> They are lightly cleaned for reading, because the automatic transcript garbles drug names. Every quote is checked against the raw transcript by '
             '<code>tools/check_pharm_e3_wood.py</code> before this page is written.</div>')
    write("pharm-exam-3-what-to-star.html", page(
        title="What the Lecturers Told You to Star &mdash; Pharmacology I Exam 3 (Class of 2028)", kicker=KICK, h1="What They Told You to Star",
        sub="%d moments from the Exam 3 lecture recordings where the lecturer said what would be tested, gave a test question, or drew a scope line." % len(d),
        legend="", notes=notes, toc="".join(toc), body=with_css("".join(secs)),
        footer_note="Every quote is checked against the recording transcript by <code>tools/check_pharm_e3_wood.py</code>."), len(d))


if __name__ == "__main__":
    gate()
    build_indications(); build_sideeffects(); build_contra(); build_kcz(); build_charts(); build_wood()
