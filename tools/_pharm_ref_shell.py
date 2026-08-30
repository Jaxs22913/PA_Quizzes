# -*- coding: utf-8 -*-
"""Shared page shell for the three Pharmacology I Exam 1 reference charts.

Contraindications, Indications & Patient Education, and Side Effects all use
this so the CSS cannot drift between them. Extracted from the contraindications
builder; that page rebuilds byte-identical against its committed version, which
is asserted by tools/check_pharm_shell_parity.py.

Palette is inherited from the Pharmacology I quizzes and guide.
"""
NAVY, INDIGO, GOLD, ICE = "#6b3524", "#9c5230", "#c9a227", "#fbf1e6"

CSS = r"""<style>
  :root{
    --ink:#161a24;--body:#2b3140;--muted:#6b7280;--line:#e4e7ef;--paper:#f6f7fb;--card:#fff;
    --navy:__NAVY__;--indigo:__INDIGO__;--gold:__GOLD__;--ice:__ICE__;
    --shadow:0 1px 2px rgba(20,22,40,.05),0 10px 30px rgba(20,22,40,.05);
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--paper);color:var(--body);
    font:400 15.5px/1.55 ui-sans-serif,"Segoe UI",system-ui,-apple-system,Roboto,Arial,sans-serif;
    -webkit-font-smoothing:antialiased}
  .wrap{max-width:1180px;margin:0 auto;padding:26px 20px 70px}
  .hero{background:var(--card);border:1px solid var(--line);border-radius:16px;
    padding:22px 22px 18px;box-shadow:var(--shadow);margin-bottom:18px}
  .kicker{font-size:12.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--indigo);font-weight:800}
  h1{margin:6px 0 8px;font-size:31px;line-height:1.15;color:var(--ink);letter-spacing:-.015em}
  .sub{margin:0 0 14px;color:var(--muted);font-size:15px}
  .legend{display:flex;flex-wrap:wrap;gap:10px 22px;font-size:13.5px;margin-top:6px}
  .legend .dot{width:9px;height:9px;border-radius:50%;display:inline-block;margin-right:6px;vertical-align:middle}
  .note{margin-top:14px;background:var(--ice);border:1px solid rgba(107,53,36,.18);
    border-radius:11px;padding:13px 15px;font-size:14.5px}
  .note.warn{background:#fff6f5;border-color:rgba(179,38,30,.22)}
  .toc{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px}
  .toc a{font-size:13px;font-weight:700;text-decoration:none;color:var(--navy);
    background:var(--card);border:1px solid var(--line);border-radius:999px;padding:6px 13px}
  .toc a:hover{background:var(--ice)}
  section{margin:0 0 26px}
  .shead{display:flex;align-items:center;gap:9px;margin:0 0 9px}
  .shead .dot{width:11px;height:11px;border-radius:50%;background:var(--indigo)}
  h2{margin:0;font-size:19.5px;color:var(--ink);letter-spacing:-.01em}
  .tag{font-size:12px;font-weight:600;color:var(--muted);background:var(--card);
    border:1px solid var(--line);border-radius:999px;padding:2px 9px;margin-left:6px;vertical-align:2px}
  .scroll{overflow-x:auto;background:var(--card);border:1px solid var(--line);
    border-radius:13px;box-shadow:var(--shadow)}
  table{border-collapse:collapse;width:100%;min-width:760px;font-size:14.5px}
  thead th{position:sticky;top:0;background:var(--navy);color:#fff;text-align:left;
    padding:10px 13px;font-size:12.5px;letter-spacing:.05em;text-transform:uppercase;font-weight:800}
  td{padding:11px 13px;border-top:1px solid var(--line);vertical-align:top}
  tbody tr:nth-child(even){background:#fbfbfd}
  .dn-h{width:20%}.p-h{width:12%}.sl-h{width:9%}
  .dn{font-weight:800;color:var(--ink)}
  .ct u{text-underline-offset:3px;text-decoration-thickness:2px}
  .sl{font-size:12.5px;color:var(--muted);white-space:nowrap}
  .g{color:var(--muted);font-weight:500;font-size:12.5px}
  .pill{display:inline-block;color:#fff;font-size:11px;font-weight:800;letter-spacing:.04em;
    text-transform:uppercase;border-radius:999px;padding:3px 9px;white-space:nowrap}
  tr.t-abs td,tr.t-bbw td{background:#fff6f5}
  tr.t-abs:nth-child(even) td,tr.t-bbw:nth-child(even) td{background:#fff1ef}
  footer{margin-top:34px;color:var(--muted);font-size:13.5px;text-align:center}
  /* NO dark palette here on purpose. theme.css does dark mode by inverting
     body > .wrap (filter: invert(1) hue-rotate(180deg)), so a page authors in
     LIGHT colours and the filter flips them. These charts used to declare a
     dark palette too, so in dark mode the filter turned those dark cards back
     into LIGHT ones -- readable, but a white card on a black page. Measured
     against guides.html, which keeps its cards dark because it does not
     double up. Checked by tools/check_dark_contrast.py. */
  @media(max-width:640px){h1{font-size:25px}.wrap{padding:18px 13px 60px}}
</style>"""


def page(title, kicker, h1, sub, legend, notes, toc, body, footer_note):
    """Assemble one reference page. `notes` and `body` are pre-rendered HTML."""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<script>document.documentElement.setAttribute('data-theme', localStorage.getItem('siteTheme') || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));</script>
<link rel="stylesheet" href="../theme.css">
<script src="../theme.js" defer></script>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-2K06TXC2KK"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-2K06TXC2KK');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__TITLE__</title>
__CSSBLOCK__
</head>
<body>
<div id="pull-refresh">
  <svg viewBox="0 0 300 60" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M0,30 L120,30 L135,8 L150,52 L165,30 L300,30" vector-effect="non-scaling-stroke" />
  </svg>
</div>
<div class="guide-back-bar">
  <a href="#" class="guide-back-link" onclick="event.preventDefault(); window.guideGoBack();">&larr; Back</a>
</div>
<div class="wrap">

  <header class="hero">
    <div class="kicker">__KICKER__</div>
    <h1>__H1__</h1>
    <p class="sub">__SUB__</p>
    <div class="legend">__LEGEND__</div>
__NOTES__
  </header>

  <div class="toc">__TOC__</div>

__BODY__

  <footer>
    __FOOTNOTE__
    <p style="text-align:center;margin-top:26px;"><a href="../index.html" style="color:inherit;font-weight:700;text-decoration:none;">&larr; Back to Homepage</a></p>
    <p style="text-align:center;font-size:13px;font-style:italic;">&#9733; <a href="#" style="color:inherit;text-decoration:underline;cursor:pointer" onclick="event.preventDefault(); window.reportMistake()">If you see any mistakes, click here to report it</a> &#9733;</p>
  </footer>
</div>
</body>
</html>
"""
    css = CSS.replace("__NAVY__", NAVY).replace("__INDIGO__", INDIGO)
    css = css.replace("__GOLD__", GOLD).replace("__ICE__", ICE)
    for k, v in (("__TITLE__", title), ("__CSSBLOCK__", css), ("__KICKER__", kicker),
                 ("__H1__", h1), ("__SUB__", sub), ("__LEGEND__", legend),
                 ("__NOTES__", notes), ("__TOC__", toc), ("__BODY__", body),
                 ("__FOOTNOTE__", footer_note)):
        html = html.replace(k, v)
    return html
