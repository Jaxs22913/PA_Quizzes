#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Jaxon's filled "Pharmacology Drug Study Chart" for Pharmacology I Exam 2 (Lectures 4-8).

Input:   tools/pharm_e2_study_chart.json   (one row per drug class, every cell proved against its slide)
Outputs: Pharmacology I Exam 2/pharm-exam-2-drug-study-chart.html   the chart as a site reference page
         Pharmacology I Exam 2/pharm-exam-2-drug-study-chart.pdf    laid out like his blank form (landscape letter,
                                                                    7 columns, black last column, up to 8 rows a page)

REFUSES TO WRITE unless tools/check_pharm_e2_study_chart.py passes. The page is a reference page (data-dark-kind "ref"),
not a study guide, so the guide-link system is unaffected. The PDF is printed by headless Chrome from a standalone
page (no site scripts, so nothing reaches Firebase); rows are packed onto pages by MEASURED height so that no cell is
clipped.

    python3 tools/build_pharm_e2_study_chart.py            # page + PDF
    python3 tools/build_pharm_e2_study_chart.py --no-pdf   # page only
"""
import html as H, json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import check_pharm_e2_study_chart as CK
import pharm_e2_lib as L
from _pharm_ref_shell import page
import dark_tokens

OUTDIR = os.path.join(ROOT, "Pharmacology I Exam 2")
PAGE = "pharm-exam-2-drug-study-chart.html"
PDF = "pharm-exam-2-drug-study-chart.pdf"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Jaxon's headers, word for word. Page 1 of his form says "Generic Names" and "!! SPECIAL WARNING !!"; pages 2-3 say
# "Generic Names (3+ Drugs)" and "BLACK BOX WARNING / Special Indications or Contraindications".
HEAD_WEB = ["Class of Drugs", "Generic Names (3+ Drugs)", "Mechanism of Action (MOA)", "Indications", "Contraindications",
            "Adverse Effects", "BLACK BOX WARNING / Special Indications or Contraindications"]
HEAD_P1 = ["Class of Drugs", "Generic Names", "Mechanism of Action (MOA)", "Indications", "Contraindications",
           "Adverse Effects", "!! SPECIAL WARNING !!"]
PDF_TITLE = "PHARMACOLOGY DRUG STUDY CHART - Pharmacology I Exam 2"
ROWS_PER_PAGE = 8
E = H.escape


def cites(r):
    """'slides 15-17' style text, plus cross-lecture proofs ('also Lecture 5 slide 15')."""
    s = sorted(r["slides"])
    runs, start, prev = [], s[0], s[0]
    for n in s[1:] + [None]:
        if n is not None and n == prev + 1:
            prev = n; continue
        runs.append(str(start) if start == prev else "%d-%d" % (start, prev))
        if n is not None:
            start = prev = n
    out = ("slide " if len(s) == 1 else "slides ") + ", ".join(runs)
    cross = sorted({(v[3], v[1]) for v in r["verify"] if len(v) == 4})
    if cross:
        out += "; also " + ", ".join("Lecture %d slide %d" % (L.LECTURES[l]["n"], n) for l, n in cross)
    return out


def generics_html(r):
    g = [x.split("|")[0] for x in r["generics"]]
    note = r.get("generics_note") or ("Only %d named in the lecture." % len(g) if len(g) < 3 else "")
    return E(", ".join(g)).replace("carboxymethylcellulose", "carboxymethyl&shy;cellulose"), E(note)


def warn_parts(r):
    k = r["warning_kind"]
    return k, (E(r["warning"]) if k != "none" else "&mdash;")


def lec_title(l):
    return "Lecture %d &mdash; %s" % (L.LECTURES[l]["n"], L.LECTURES[l]["title"])


# --------------------------------------------------------------------------------------------- site page
WEB_CSS = """<style>
  .wrap{max-width:1480px}
  .hero{padding:16px 20px 14px;margin-bottom:14px}
  .hero h1{font-size:27px;margin:4px 0 6px}
  .hero .sub{margin:0 0 6px}
  .hero .legend{margin-top:2px;align-items:center}
  .hero .pdfbtn{display:inline-block;background:var(--indigo-l,var(--indigo));color:#fff;font-weight:800;font-size:13px;text-decoration:none;border-radius:999px;padding:5px 14px;margin-left:8px;vertical-align:1px}
  .chart{background:var(--card);border:1px solid var(--line);border-radius:13px;box-shadow:var(--shadow)}
  .chart table{width:100%;min-width:0;table-layout:fixed;font-size:13.5px;line-height:1.42;border-collapse:separate;border-spacing:0}
  .chart thead th{top:38px;z-index:5;font-size:11.5px;letter-spacing:.03em;text-transform:none;text-align:center;vertical-align:middle;padding:9px 8px;border-left:1px solid rgba(255,255,255,.22)}
  .chart thead th:first-child{border-left:0;border-top-left-radius:12px}
  .chart thead th.warnh,:root[data-theme="dark"] body[data-dark="tokens"] .chart thead th.warnh{background:#000;color:#fff;border-top-right-radius:12px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.28)}
  .chart td{padding:9px 9px;border-top:1px solid var(--line);border-left:1px solid var(--line);vertical-align:top;overflow-wrap:break-word}
  .chart td:first-child{border-left:0}
  .chart col.c1{width:13%}.chart col.c2{width:11%}.chart col.c3{width:15%}.chart col.c4{width:16%}.chart col.c5{width:14.5%}.chart col.c6{width:14%}.chart col.c7{width:16.5%}
  .chart td.dn b{display:block;color:var(--ink);font-size:14px;line-height:1.3}
  .chart td.dn .sl{display:block;margin-top:5px;font-size:11.5px;color:var(--muted);white-space:normal;font-weight:500}
  .chart td.gn{color:var(--ink);font-weight:600}
  .chart td.gn .g{display:block;margin-top:4px;font-weight:500}
  .chart tr.grp td{background:var(--ice);color:var(--navy);font-weight:800;font-size:13px;letter-spacing:.04em;text-transform:uppercase;padding:8px 13px;border-left:0}
  .chart td.wn{font-weight:600}
  .chart td.wn.none{color:var(--muted);font-weight:500;text-align:center}
  .bbwtag{display:inline-block;background:#7a1010;color:#fff;font-size:10.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;border-radius:999px;padding:2px 8px;margin:0 6px 4px 0;vertical-align:1px}
  @media (max-width:980px){
    .chart{background:transparent;border:0;box-shadow:none}
    .chart table,.chart tbody,.chart tr,.chart td{display:block;width:100%}
    .chart thead,.chart colgroup{display:none}
    .chart tr.grp td{border-radius:10px;margin:16px 0 8px;border:1px solid var(--line)}
    .chart tr.row{background:var(--card);border:1px solid var(--line);border-radius:12px;box-shadow:var(--shadow);margin:0 0 12px;overflow:hidden}
    .chart td{border-left:0;padding:9px 13px}
    .chart td[data-label]::before{content:attr(data-label);display:block;font-size:11px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--indigo);margin-bottom:2px}
    .chart td.dn{background:var(--ice);border-top:0}
    .chart td.dn::before{display:none}
    .chart td.dn b{font-size:16px}
    .chart tr.row td.wn{background:#000!important;color:#fff!important}
    .chart td.wn::before{color:#fff}
    .chart td.wn.none{text-align:left}
  }
  @media print{
    @page{size:11in 8.5in;margin:.3in}
    .guide-back-bar,footer,.pdfbtn,#pull-refresh{display:none!important}
    body{background:#fff!important;font-size:8pt}
    .wrap{max-width:none;padding:0}
    .hero{box-shadow:none;border:0;padding:0 0 6px}
    .hero .legend{display:none}
    .chart{border:0;box-shadow:none}
    .chart table{font-size:7pt;line-height:1.25;table-layout:fixed}
    .chart thead{display:table-header-group}
    .chart thead th{position:static;background:#d9d9d9!important;color:#000!important;font-size:7pt;padding:4px}
    .chart thead th.warnh{background:#000!important;color:#fff!important}
    .chart tr{break-inside:avoid}
    .chart td{padding:3px 4px;border:1px solid #000}
    .chart tr.grp td{background:#eee!important;color:#000!important;font-size:7pt;padding:2px 4px}
    .chart td.dn b{font-size:7.5pt}
    .chart td.dn .sl,.chart td.gn .g{font-size:6pt}
    .bbwtag{background:#fff!important;color:#000!important;border:1px solid #000;font-size:6pt}
  }
</style>"""


def build_page(d):
    rows = d["rows"]
    body, last = [], None
    colg = "<colgroup>" + "".join('<col class="c%d">' % i for i in range(1, 8)) + "</colgroup>"
    thead = "<thead><tr>%s</tr></thead>" % "".join(
        '<th%s>%s</th>' % (' class="warnh"' if i == 6 else "", E(h)) for i, h in enumerate(HEAD_WEB))
    for r in rows:
        if r["lecture"] != last:
            body.append('<tr class="grp"><td colspan="7">%s</td></tr>' % lec_title(r["lecture"])); last = r["lecture"]
        g, gnote = generics_html(r)
        k, w = warn_parts(r)
        tag = '<span class="bbwtag">Black box</span>' if k == "bbw" else ""
        body.append(
            '<tr class="row%s">'
            '<td class="dn" data-label="%s"><b>%s</b><span class="sl">%s</span></td>'
            '<td class="gn" data-label="Generic Names">%s%s</td>'
            '<td data-label="Mechanism of Action (MOA)">%s</td>'
            '<td data-label="Indications">%s</td>'
            '<td data-label="Contraindications">%s</td>'
            '<td data-label="Adverse Effects">%s</td>'
            '<td class="wn%s" data-label="Special Warning">%s%s</td></tr>'
            % (" t-bbw" if k == "bbw" else "", E(HEAD_WEB[0]), E(r["class"]), E(cites(r)),
               g, ('<span class="g">%s</span>' % gnote) if gnote else "",
               E(r["moa"]), E(r["indications"]), E(r["contraindications"]), E(r["adverse"]),
               " none" if k == "none" else "", tag, w))
    table = '<div class="chart"><table>%s%s<tbody>%s</tbody></table></div>' % (colg, thead, "".join(body))
    per = {}
    for r in rows:
        per[r["lecture"]] = per.get(r["lecture"], 0) + 1
    sub = ('Your blank Pharmacology Drug Study Chart, filled in for Exam 2 (Lectures 4&ndash;8): one row per drug class, '
           'every cell taken from the slides and checked against them.')
    legend = ('<a class="pdfbtn" href="%s" download style="margin-left:0">Download the PDF</a><span>Shaded rows carry a <b>black box warning</b>; where the slides do not mention it, the cell says so. '
              'No dosages (Dr. Wood does not test them). %d classes.</span>' % (PDF, len(rows)))
    html = page(title="Pharmacology Drug Study Chart - Exam 2", kicker="Pharmacology I &middot; Exam 2 &middot; Class of 2028",
                h1="Pharmacology Drug Study Chart &mdash; Exam 2", sub=sub, legend=legend, notes="", toc="",
                body=WEB_CSS + table, footer_note="")
    html = html.replace("<title>Pharmacology Drug Study Chart - Exam 2</title>", "<title>Pharmacology Drug Study Chart - Exam 2</title>")
    return dark_tokens.apply(html, "ref")


# --------------------------------------------------------------------------------------------- PDF
PDF_CSS = """
@page{size:11in 8.5in;margin:.3in}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff;color:#000;font-family:Arial,Helvetica,sans-serif}
.pg{page-break-after:always;width:10.4in}
.pg:last-child{page-break-after:auto}
h1{font-size:11pt;text-align:center;margin:0 0 5px;height:17px;line-height:17px;letter-spacing:.01em}
table{border-collapse:collapse;width:10.4in;table-layout:fixed;border:1px solid #000}
th{background:#d9d9d9;font-size:7pt;font-weight:700;text-align:center;vertical-align:middle;border:1px solid #000;padding:4px 3px;height:34px;line-height:1.2}
th.w{background:#000;color:#fff}
td{border:1px solid #000;padding:3px 4px;vertical-align:top;font-size:%(fs)spt;line-height:1.22;overflow-wrap:break-word;hyphens:auto;-webkit-hyphens:auto}
td.c b{display:block;font-size:%(fsb)spt;line-height:1.2}
td.c i{display:block;font-style:normal;color:#444;font-size:5.6pt;margin-top:3px;line-height:1.2}
td.g,td.c{hyphens:manual;-webkit-hyphens:manual}
td.g{font-weight:700}
td.g i{display:block;font-style:normal;font-weight:400;color:#444;font-size:5.8pt;margin-top:2px}
td.w.bbw{background:#f3d9d6}
td.w .bb{display:block;font-weight:800;font-size:5.8pt;letter-spacing:.04em;margin-bottom:1px}
td.w.n{text-align:center;color:#555}
col.c1{width:10.5%%}col.c2{width:11%%}col.c3{width:15.5%%}col.c4{width:16.5%%}col.c5{width:15.5%%}col.c6{width:14.5%%}col.c7{width:16.5%%}
"""


def pdf_row(r, minh):
    g, gnote = generics_html(r)
    k, w = warn_parts(r)
    lec = "Lecture %d &middot; %s" % (L.LECTURES[r["lecture"]]["n"], E(cites(r)))
    wc = "w" + (" bbw" if k == "bbw" else "") + (" n" if k == "none" else "")
    return ('<tr style="height:%dpx"><td class="c"><b>%s</b><i>%s</i></td><td class="g">%s%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>'
            '<td class="%s">%s%s</td></tr>'
            % (minh, E(r["class"]), lec, g, ("<i>%s</i>" % gnote) if gnote else "", E(r["moa"]), E(r["indications"]),
               E(r["contraindications"]), E(r["adverse"]), wc, '<span class="bb">BLACK BOX</span>' if k == "bbw" else "", w))


def pdf_table(rows, first, minh):
    head = HEAD_P1 if first else HEAD_WEB
    th = "".join('<th%s>%s</th>' % (' class="w"' if i == 6 else "",
                 E(h).replace(" / ", " /<br>").replace("Special Indications or", "Special Indications or<br>") if i == 6 and not first else E(h))
                 for i, h in enumerate(head))
    cg = "<colgroup>" + "".join('<col class="c%d">' % i for i in range(1, 8)) + "</colgroup>"
    return "<h1>%s</h1><table>%s<thead><tr>%s</tr></thead><tbody>%s</tbody></table>" % (
        E(PDF_TITLE), cg, th, "".join(pdf_row(r, minh) for r in rows))


def doc(body, fs, fsb):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>%s</title><style>%s</style></head><body>%s</body></html>' % (
        E(PDF_TITLE), PDF_CSS % {"fs": fs, "fsb": fsb}, body)


class Chrome:
    """Headless Chrome driven over the DevTools protocol (the CLI --dump-dom / --print-to-pdf flags hang on this
    machine). The pages it opens are standalone files, so nothing site-wide (Firebase, analytics) ever loads."""
    def __init__(self):
        try:
            import websocket
        except ImportError:
            sys.exit("the PDF step needs the websocket-client package (pip install websocket-client); the page alone: --no-pdf")
        import socket, time, urllib.request
        self.websocket, self.urllib = websocket, urllib.request
        s = socket.socket(); s.bind(("127.0.0.1", 0)); self.port = s.getsockname()[1]; s.close()
        self.prof = tempfile.mkdtemp(prefix="pdfchart_")
        self.proc = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--no-first-run", "--remote-allow-origins=*",
                                      "--remote-debugging-port=%d" % self.port, "--user-data-dir=" + self.prof],
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(80):
            try:
                urllib.request.urlopen("http://127.0.0.1:%d/json/version" % self.port, timeout=1).read(); break
            except Exception:
                time.sleep(.25)
        t = json.loads(urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:%d/json/new?about:blank" % self.port, method="PUT")).read())
        self.ws = websocket.create_connection(t["webSocketDebuggerUrl"], timeout=60, suppress_origin=True)
        self.n = 0
        self.call("Page.enable")

    def call(self, method, **params):
        self.n += 1
        self.ws.send(json.dumps({"id": self.n, "method": method, "params": params}))
        while True:
            r = json.loads(self.ws.recv())
            if r.get("id") == self.n:
                return r.get("result", r)

    def load(self, path):
        import time
        self.call("Page.navigate", url="file://" + path)
        for _ in range(100):
            time.sleep(.1)
            if self.call("Runtime.evaluate", expression="document.readyState", returnByValue=True)["result"]["value"] == "complete":
                break
        time.sleep(.3)

    def ev(self, js):
        return self.call("Runtime.evaluate", expression=js, returnByValue=True)["result"].get("value")

    def pdf(self, out):
        import base64
        r = self.call("Page.printToPDF", landscape=True, printBackground=True, preferCSSPageSize=True,
                      displayHeaderFooter=False, marginTop=0, marginBottom=0, marginLeft=0, marginRight=0)
        open(out, "wb").write(base64.b64decode(r["data"]))

    def close(self):
        try:
            self.ws.close()
        finally:
            self.proc.terminate(); shutil.rmtree(self.prof, ignore_errors=True)


def measure(ch, rows, fs, fsb):
    """Natural height (CSS px) of every row at the printed column widths, as Chrome lays them out."""
    probe = ('<div class="pg"><table><colgroup>%s</colgroup><tbody>%s</tbody></table></div>'
             % ("".join('<col class="c%d">' % i for i in range(1, 8)), "".join(pdf_row(r, 0) for r in rows)))
    tmp = tempfile.mkdtemp(prefix="pdfmeasure_")
    p = os.path.join(tmp, "m.html")
    open(p, "w", encoding="utf-8").write(doc(probe, fs, fsb))
    ch.load(p)
    hs = json.loads(ch.ev('JSON.stringify([].slice.call(document.querySelectorAll("tbody tr")).map(function(r){return r.getBoundingClientRect().height}))'))
    shutil.rmtree(tmp, ignore_errors=True)
    return hs


def build_pdf(d, fs="6.5", fsb="7.4"):
    rows = d["rows"]
    # page height 8.5in - .6in margins = 758px; title block 22px, header row 36px (+ border slack)
    avail = 758 - 62
    minh = 72      # rows never print shorter than this, so short rows keep the form's grid look
    ch = None
    for _ in range(4):
        try:
            ch = Chrome(); break
        except Exception:
            pass
    if ch is None:
        sys.exit("could not start headless Chrome")
    try:
        hs = measure(ch, rows, fs, fsb)
        pages, cur, h = [], [], 0
        for r, nat in zip(rows, hs):
            eff = max(nat, minh) + 1
            if cur and (len(cur) >= ROWS_PER_PAGE or h + eff > avail):
                pages.append(cur); cur, h = [], 0
            cur.append(r); h += eff
        pages.append(cur)
        body = "".join('<div class="pg">%s</div>' % pdf_table(pg, i == 0, minh) for i, pg in enumerate(pages))
        tmp = tempfile.mkdtemp(prefix="pdfout_")
        p = os.path.join(tmp, "chart.html")
        open(p, "w", encoding="utf-8").write(doc(body, fs, fsb))
        ch.load(p)
        out = os.path.join(OUTDIR, PDF)
        ch.pdf(out)
        shutil.rmtree(tmp, ignore_errors=True)
    finally:
        ch.close()
    try:
        import pymupdf
        n = len(pymupdf.open(out))
        if n != len(pages):
            sys.exit("PDF has %d pages but %d were laid out: a row overflowed" % (n, len(pages)))
    except ImportError:
        n = len(pages)
    print("wrote %-40s %3d KB  %d pages (%s rows per page)" % (PDF, os.path.getsize(out) // 1024, n, "/".join(str(len(x)) for x in pages)))


def main():
    ok, d = CK.check(verbose=False)
    if not ok:
        CK.check(verbose=True)
        sys.exit("fact-check failed -- refusing to write the chart")
    print("fact-check OK (%d rows)" % len(d["rows"]))
    html = build_page(d)
    open(os.path.join(OUTDIR, PAGE), "w", encoding="utf-8").write(html)
    print("wrote %-40s %3d KB  %d rows" % (PAGE, len(html) // 1024, len(d["rows"])))
    if "--no-pdf" not in sys.argv:
        build_pdf(d)


if __name__ == "__main__":
    main()
