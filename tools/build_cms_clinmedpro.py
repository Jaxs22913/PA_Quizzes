#!/usr/bin/env python3
"""Build the CMS I "Clin Med Pro" disease guides, one page per exam.

Shared, data-driven builder. Exams 1-2 and Exams 3-4 were filled by separate
agents on 2026-09-25; this file is render_clinmedpro_e34.py (the Exam 3/4
renderer) promoted into tools/ with three additions that leave plain-text data
rendering exactly as before:
  * INLINE <b>/<i>: after escaping, the literal tags <b> </b> <i> </i> are
    restored (nothing else). Exam 1/2 data uses them for the hallmark word
    and for organism names; the Exam 3/4 data is plain text and unaffected.
  * [[★ phrase]] renders as mark.prof-highlight -- a fact the existing exam
    study guide already marks "★ Professor emphasized" (from the lecture
    recording), carried over onto the same fact here.
  * VALIDATION fails loudly: every condition needs all ten fields and a
    unique id, and an uncovered field must be exactly NC.
Rebuild only the exam(s) you own:  python3 tools/build_cms_clinmedpro.py 1 2

Data:   <repo>/tools/clinmedpro/cms-e<N>.json   (one per exam)
Output: <repo>/Clinical Medicine and Surgery I Exam <N>/cms-exam-<N>-clin-med-pro-guide.html

Page shell (head, pull-refresh, back bar, footer logo, service-worker script)
is sliced from that exam's own study guide so palette + chrome match exactly.

Structure (keep identical if this is merged into tools/build_cms_clinmedpro.py):
  header.top           h1, course line, block line, .hdr-links (Exam 1-4 Clin Med Pro guides + study guide)
  .layout.wrap
    nav.toc            a.top-link per lecture (#lNN), a.sub-link per condition (#<cond id>)
    main
      .callout.cmp-intro      the ten fields, "decks only", uncovered count
      .cmp-tools              input#cmp-filter + count + expand/collapse buttons
      section.deck#lNN        h2.deck-title "Lecture NN · Title", p.lecturer, optional .cmp-note
        details.cmp-card#id   summary(.cmp-name, .cmp-star, .cmp-nc badge)
          dl.cmp-fields       10 x (dt, dd[.nc|.contested] + span.cmp-src)
      footer.guide-foot
Usage: python3 tools/build_cms_clinmedpro.py <exam> [<exam> ...]
"""
import html, json, os, re, sys

REPO = os.path.expanduser("~/Developer/PA_Quizzes")
NC = "Not covered in the lecture"
CONTESTED = "Contested on the slides"
FIELDS = [
    ("name", "Name of Condition"),
    ("definition", "Definition"),
    ("etiology", "Etiology (cause)"),
    ("epidemiology", "Epidemiology (who)"),
    ("risk_factors", "Risk Factors"),
    ("pathology", "Pathology"),
    ("clinical", "Clinical Manifestation"),
    ("diagnosis", "Diagnosis"),
    ("treatment", "Treatment/Therapy"),
    ("mortality", "Mortality &#9733;"),
]
BLOCKS = {1: "Dermatology", 2: "Ophthalmology", 3: "Ear, nose and throat", 4: "Cardiology I"}

e = lambda s: html.escape(s or "", quote=True)

_TAGS = re.compile(r"&lt;(/?)(b|i)&gt;")
_PROF = re.compile(r"\[\[\s*★\s*(.+?)\]\]")


def rich(s):
    """Escape, then restore <b>/<i> and render [[★ phrase]] marks."""
    t = _TAGS.sub(r"<\1\2>", e(s))
    return _PROF.sub(r'<mark class="prof-highlight">&#9733; \1</mark>', t)


def plain(s):
    """Text with markup stripped, for comparisons and counts."""
    return _PROF.sub(r"\1", re.sub(r"</?(?:b|i)>", "", s or "")).strip()


def validate(n, data):
    seen, bad = set(), []
    for L in data["lectures"]:
        for c in L["conditions"]:
            if c["id"] in seen:
                bad.append("duplicate id %s" % c["id"])
            seen.add(c["id"])
            for k, _ in FIELDS:
                v = c["fields"].get(k)
                if not isinstance(v, str) or not v.strip():
                    bad.append("%s: field %s missing/empty" % (c["id"], k))
                elif NC in v and v.strip() != NC:
                    bad.append("%s: field %s mixes NC with text" % (c["id"], k))
    if bad:
        sys.exit(("FATAL cms-e%d.json:\n  " % n) + "\n  ".join(bad[:40]))


def slide_label(s):
    s = (s or "").strip()
    if not s:
        return ""
    s = s.replace("-", "–")
    multi = bool(re.search(r"[,– ]", s))
    return ("Slides " if multi else "Slide ") + s


def shell(n):
    folder = "Clinical Medicine and Surgery I Exam %d" % n
    src = open(os.path.join(REPO, folder, "cms-exam-%d-study-guide.html" % n), encoding="utf8").read()
    head = src[:src.index('<header class="top">')]
    head = re.sub(r'\s*<link rel="alternate"[^>]*\.docx"[^>]*>\n?', "\n", head)
    # The study guide's Word link points at the study guide's .docx. This page
    # gets its OWN link, and only once tools/build_guide_docx.py has written
    # that file -- theme.js turns the link into a Word button, and a button to
    # a .docx that does not exist is a 404.
    docx = "cms-exam-%d-clin-med-pro-guide.docx" % n
    if os.path.exists(os.path.join(REPO, folder, docx)):
        head = head.replace(
            "</head>",
            '  <link rel="alternate" type="application/vnd.openxmlformats-officedocument.'
            'wordprocessingml.document" href="%s" title="Editable Word copy">\n</head>' % docx, 1)
    head = re.sub(r"<title>.*?</title>",
                  "<title>Clinical Medicine and Surgery I &middot; Exam %d &mdash; Clin Med Pro Guide</title>" % n,
                  head, count=1, flags=re.S)
    i = src.index("<script>\n(function () {\n  const indicator")
    j = src.find("\n<style>\n  .cond", i)
    if j < 0:
        j = src.index("</body>", i)
    tail = src[i:j]
    return folder, head, tail


CSS = r"""
<style>
  /* Clin Med Pro cards (tools/build_cms_clinmedpro.py) */
  .cmp-intro ol{columns:2;column-gap:28px;margin:6px 0 4px;padding-left:22px;font-size:.9rem}
  .cmp-tools{position:sticky;top:38px;z-index:5;background:var(--paper);padding:10px 0 8px;
    display:flex;flex-wrap:wrap;gap:8px;align-items:center;border-bottom:1px solid var(--line);margin-bottom:10px}
  .cmp-tools input{flex:1 1 220px;min-width:0;font:inherit;font-size:16px;padding:8px 12px;
    border:1.5px solid var(--line);border-radius:999px;background:#fff;color:var(--ink)}
  .cmp-tools input:focus{outline:none;border-color:var(--accent)}
  .cmp-tools button{font:inherit;font-size:.8rem;font-weight:700;padding:7px 12px;border-radius:999px;
    border:1.5px solid var(--accent);background:transparent;color:var(--accent);cursor:pointer}
  .cmp-tools .cmp-count{font-size:.8rem;color:var(--soft);min-width:6em}
  .cmp-note{border-left:4px solid #b4541a;background:#fbeee4;padding:10px 16px;margin:12px 0 16px;
    border-radius:0 8px 8px 0;font-size:.92rem}
  .cmp-note b{color:#8a3a0c}
  details.cmp-card{border:1px solid var(--line);border-radius:10px;margin:10px 0;background:#fff;
    scroll-margin-top:100px}
  details.cmp-card>summary{cursor:pointer;list-style:none;padding:11px 14px;display:flex;
    align-items:center;gap:8px;flex-wrap:wrap;font-weight:700;color:var(--ink)}
  details.cmp-card>summary::-webkit-details-marker{display:none}
  details.cmp-card>summary::before{content:"\25B8";color:var(--accent);transition:transform .15s;
    display:inline-block;width:1em}
  details.cmp-card[open]>summary::before{transform:rotate(90deg)}
  details.cmp-card[open]>summary{border-bottom:1px solid var(--line)}
  .cmp-name{flex:1 1 auto;min-width:0}
  .cmp-star{font-size:.7rem;font-weight:700;background:#fef3d4;color:#8a6205;border:1px solid #d4a017;
    border-radius:8px;padding:1px 8px}
  .cmp-nc{font-size:.68rem;font-weight:700;color:var(--soft);border:1px solid var(--line);
    border-radius:999px;padding:1px 8px;white-space:nowrap}
  dl.cmp-fields{display:grid;grid-template-columns:190px 1fr;gap:0;margin:0}
  dl.cmp-fields dt,dl.cmp-fields dd{padding:8px 14px;border-top:1px solid var(--line);margin:0}
  dl.cmp-fields dt:first-of-type,dl.cmp-fields dd:first-of-type{border-top:none}
  dl.cmp-fields dt{font-size:.72rem;font-weight:800;letter-spacing:.04em;text-transform:uppercase;
    color:var(--accent);background:#f7f1f3}
  dl.cmp-fields dd{font-size:.92rem;line-height:1.55;overflow-wrap:anywhere}
  dl.cmp-fields dd.nc{color:var(--soft);font-style:italic}
  dl.cmp-fields dd.contested{background:#fbeee4}
  .cmp-src{display:inline-block;margin-left:6px;font-size:.7rem;color:var(--soft);white-space:nowrap}
  .cmp-prof{margin:0;padding:8px 14px;font-size:.84rem;background:#fffdf5;border-bottom:1px solid var(--line)}
  .cmp-hidden{display:none !important}
  dl.cmp-fields mark.prof-highlight{background:#fef3d4;color:#3a2c05;padding:0 3px;border-radius:3px;
    box-shadow:inset 0 0 0 1px #e8c766}
  @media(max-width:820px){.cmp-tools{position:static}}
  @media(max-width:640px){
    .cmp-intro ol{columns:1}
    dl.cmp-fields{grid-template-columns:1fr}
    dl.cmp-fields dt{border-top:1px solid var(--line);padding:6px 12px 2px;background:transparent}
    dl.cmp-fields dd{border-top:none;padding:0 12px 9px}
    details.cmp-card>summary{padding:10px 12px}
  }
  @media print{.cmp-tools{display:none}}
</style>
"""

JS = r"""
<script>
(function(){
  var input=document.getElementById('cmp-filter'), count=document.getElementById('cmp-count');
  var cards=[].slice.call(document.querySelectorAll('details.cmp-card'));
  var decks=[].slice.call(document.querySelectorAll('section.deck'));
  function apply(){
    var q=(input.value||'').trim().toLowerCase();
    if(q.length<2){
      cards.forEach(function(c){c.classList.remove('cmp-hidden');c.open=false;});
      decks.forEach(function(d){d.classList.remove('cmp-hidden');});
      count.textContent='';return;
    }
    var n=0;
    cards.forEach(function(c){var hit=c.textContent.toLowerCase().indexOf(q)!==-1;
      c.classList.toggle('cmp-hidden',!hit);c.open=hit;if(hit)n++;});
    decks.forEach(function(d){d.classList.toggle('cmp-hidden',!d.querySelector('details.cmp-card:not(.cmp-hidden)'));});
    count.textContent=n+(n===1?' match':' matches');
  }
  input.addEventListener('input',apply);
  input.addEventListener('keydown',function(ev){if(ev.key==='Escape'){input.value='';apply();}});
  document.getElementById('cmp-expand').addEventListener('click',function(){
    cards.forEach(function(c){if(!c.classList.contains('cmp-hidden'))c.open=true;});});
  document.getElementById('cmp-collapse').addEventListener('click',function(){
    cards.forEach(function(c){c.open=false;});});
  // theme.js "Search this guide" marks the current hit with .search-hit-current
  // but cannot see inside a closed <details>; open that card (a user action).
  new MutationObserver(function(ms){ms.forEach(function(m){var el=m.target;
    if(el.classList&&el.classList.contains('search-hit-current')){var d=el.closest('details.cmp-card');
      if(d&&!d.open){d.classList.remove('cmp-hidden');d.open=true;el.scrollIntoView({block:'center'});}}});})
    .observe(document.querySelector('main')||document.body,{subtree:true,attributes:true,attributeFilter:['class']});
  // Following a table-of-contents link opens that card (a user action, not load state).
  document.addEventListener('click',function(ev){
    var a=ev.target.closest&&ev.target.closest('a[href^="#"]');if(!a)return;
    var t=document.getElementById(a.getAttribute('href').slice(1));
    if(t&&t.tagName==='DETAILS'){t.classList.remove('cmp-hidden');t.open=true;}
  });
})();
</script>
"""


def render(n):
    data = json.load(open(os.path.join(REPO, "tools/clinmedpro/cms-e%d.json" % n), encoding="utf8"))
    validate(n, data)
    folder, head, tail = shell(n)
    lectures = data["lectures"]
    ncond = sum(len(L["conditions"]) for L in lectures)
    nc_total = sum(1 for L in lectures for c in L["conditions"] for k, _ in FIELDS
                   if c["fields"][k].strip() == NC)
    nc_mort = sum(1 for L in lectures for c in L["conditions"] if c["fields"]["mortality"].strip() == NC)

    links = []
    for k in (1, 2, 3, 4):
        label = "Exam %d &middot; %s" % (k, BLOCKS[k])
        href = "../Clinical Medicine and Surgery I Exam %d/cms-exam-%d-clin-med-pro-guide.html" % (k, k)
        if k == n:
            links.append('<a href="#top" aria-current="page" style="background:rgba(255,255,255,.22)">%s</a>' % label)
        else:
            links.append('<a href="%s">%s</a>' % (e(href), label))
    links.append('<a href="cms-exam-%d-study-guide.html">Exam %d study guide</a>' % (n, n))

    out = [head]
    out.append('<header class="top" id="top">\n'
               '  <h1>Clinical Medicine and Surgery I &middot; Exam %d &mdash; Clin Med Pro Guide</h1>\n'
               '  <p>PAJ 5500 Clinical Medicine and Surgery I &middot; Class of 2028</p>\n'
               '  <p>%s block &middot; <b>%d conditions</b> across %d lectures &middot; Dr. Carter&rsquo;s Clin Med Pro Study Tip, ten fields per condition</p>\n'
               '  <div class="hdr-links">%s</div>\n</header>\n' % (n, BLOCKS[n], ncond, len(lectures), "".join(links)))
    out.append(CSS)
    out.append('<div class="layout wrap" data-readable>\n<nav class="toc">\n')
    out.append('  <a class="top-link" href="#how">How to use this guide</a>\n')
    for L in lectures:
        out.append('  <a class="top-link" href="#l%d">Lecture %d &middot; %s</a>\n' % (L["lecture"], L["lecture"], e(L["title"])))
        for c in L["conditions"]:
            out.append('  <a class="sub-link" href="#%s">%s</a>\n' % (e(c["id"]), e(c["name"])))
    out.append('</nav>\n\n<main>\n')
    out.append('<section class="deck" id="how">\n<h2 class="deck-title">How to use this guide</h2>\n'
               '<div class="callout cmp-intro"><p>Dr. Carter&rsquo;s <b>Clin Med Pro Study Tip</b> (Hypotension deck, slide 7) '
               'lists what to learn for every condition. Each card below answers those ten fields:</p><ol>%s</ol>'
               '<p>Every field comes from the lecture slides only. Where a deck is silent the card says '
               '<i>%s</i> rather than filling the gap from elsewhere (%d of %d fields in this exam; Mortality alone: %d of %d). '
               'Slide numbers follow each field. Cards open closed; tap one to read it.</p></div>\n</section>\n'
               % ("".join("<li>%s</li>" % lbl for _, lbl in FIELDS), NC, nc_total, ncond * 10, nc_mort, ncond))
    if any("[[" in v for L in lectures for c in L["conditions"] for v in c["fields"].values()):
        out[-1] = out[-1].replace('</div>\n</section>\n',
            '<p>The &#9733; on <b>Mortality</b> is on the original study-tip slide: fill it when a figure exists. '
            'A <mark class="prof-highlight" style="background:#fef3d4;padding:0 3px;border-radius:3px">&#9733; highlighted phrase</mark> '
            'inside a field is a fact the professor emphasized in the lecture recording, carried over from this exam&rsquo;s study guide.</p>'
            '</div>\n</section>\n')
    out.append('<div class="cmp-tools"><input type="search" id="cmp-filter" placeholder="Filter conditions (e.g. vertigo, murmur, statin)" '
               'aria-label="Filter conditions" autocomplete="off"><span class="cmp-count" id="cmp-count" aria-live="polite"></span>'
               '<button type="button" id="cmp-expand">Expand all</button><button type="button" id="cmp-collapse">Collapse all</button></div>\n')

    for L in lectures:
        out.append('<section class="deck" id="l%d">\n<h2 class="deck-title">Lecture %d &middot; %s</h2>\n'
                   '<p class="lecturer">%s &middot; %d conditions &middot; source: %s</p>\n'
                   % (L["lecture"], L["lecture"], e(L["title"]), e(L["lecturer"]), len(L["conditions"]), e(L["deck"])))
        if L.get("note"):
            out.append('<div class="cmp-note"><b>Note:</b> %s</div>\n' % e(L["note"]))
        for c in L["conditions"]:
            f, s = c["fields"], c.get("slides", {})
            nnc = sum(1 for k, _ in FIELDS if f[k].strip() == NC)
            badge = '<span class="cmp-nc">%d not covered</span>' % nnc if nnc else ""
            star = '<span class="cmp-star">&#9733; Professor emphasized</span>' if c.get("prof") else ""
            out.append('<details class="cmp-card" id="%s"><summary><span class="cmp-name">%s</span>%s%s</summary>\n'
                       % (e(c["id"]), e(c["name"]), star, badge))
            if c.get("prof") and c.get("prof_note"):
                out.append('<p class="cmp-prof">&#9733; %s</p>\n' % e(c["prof_note"]))
            out.append('<dl class="cmp-fields">\n')
            for k, lbl in FIELDS:
                v = f[k].strip()
                cls = ' class="nc"' if v == NC else (' class="contested"' if v.startswith(CONTESTED) or CONTESTED.lower() in v.lower() else "")
                src = slide_label(s.get(k, "")) if v != NC else ""
                out.append('<dt>%s</dt><dd%s>%s%s</dd>\n' % (lbl, cls, rich(v),
                           ' <span class="cmp-src">%s</span>' % e(src) if src else ""))
            out.append('</dl>\n</details>\n')
        out.append('</section>\n')

    out.append('<footer class="guide-foot">\n'
               '  <p style="text-align:center;margin:0 0 10px;"><a href="../index.html" style="color:inherit;font-weight:700;text-decoration:none;">&larr; Back to Homepage</a></p>\n'
               '  <p style="text-align:center;">Built from your PAJ 5500 lecture decks for personal study &middot; Class of 2028.</p>\n'
               '  <p style="text-align:center;font-style:italic;">&#9733; <a href="#" style="color:inherit;text-decoration:underline;cursor:pointer" onclick="event.preventDefault(); window.reportMistake()">If you see any mistakes, click here to report it</a> &#9733;</p>\n'
               '</footer>\n</main>\n</div>\n\n')
    out.append(tail)
    out.append(JS)
    out.append("</body>\n</html>\n")
    path = os.path.join(REPO, folder, "cms-exam-%d-clin-med-pro-guide.html" % n)
    open(path, "w", encoding="utf8").write("".join(out))
    print("wrote %s: %d conditions, %d/%d fields not covered (mortality %d)" % (path, ncond, nc_total, ncond * 10, nc_mort))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: build_cms_clinmedpro.py <exam> [<exam> ...]  (rebuild only the exams you own)")
    for a in sys.argv[1:]:
        render(int(a))
