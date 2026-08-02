"""Generate practicum-builder.html — pick your own practicum practice exam.

Reuses a generated master exam as the engine (so the type-in flow, override,
retype-misses, word bank and class counter all come along unchanged) and puts a
picker in front of it instead of a fixed question list.

The picker writes ITEMS at runtime from practicum-bank.js, then starts the same
exam loop. The one behaviour added on top: consecutive structures are pulled
from DIFFERENT plates wherever the selection allows, so it is one structure
then a new picture rather than working through every label on one image.

Usage: python3 tools/build_practicum_builder.py
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "Anatomy Practicum Exam 3", "practicum-exam3-master-exam-form-a.html")
OUT = os.path.join(ROOT, "practicum-builder.html")

PICKER_CSS = """
  /* ---- picker ---- */
  .pick-tabs{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 14px}
  .pick-tab{font:inherit;font-size:13.5px;font-weight:700;cursor:pointer;border:1px solid var(--line,#e5e7ef);
    background:var(--card,#fff);color:var(--muted);border-radius:999px;padding:8px 15px}
  .pick-tab.on{background:var(--accent,#0d7d6c);border-color:var(--accent,#0d7d6c);color:#fff}
  .pick-groups{display:flex;flex-direction:column;gap:8px;margin:0 0 16px}
  .exam-head{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--accent,#0d7d6c);
    font-weight:800;margin:20px 0 4px;padding:0 0 6px;border-bottom:2px solid var(--line,#e5e7ef);
    display:flex;align-items:baseline;gap:10px}
  .exam-head:first-child{margin-top:2px}
  .exam-head .exam-tally{margin-left:auto;font-size:12px;letter-spacing:0;text-transform:none;
    font-weight:600;color:var(--muted)}
  .exam-head .exam-pick{margin-left:0;font-size:11.5px;letter-spacing:0;text-transform:none;
    font-weight:700;color:var(--accent,#0d7d6c);background:none;border:0;cursor:pointer;
    text-decoration:underline;padding:0}
  .pick-group{border:1px solid var(--line,#e5e7ef);border-radius:12px;overflow:hidden;background:var(--card,#fff)}
  .pick-head{display:flex;align-items:center;gap:10px;padding:11px 13px;cursor:pointer}
  .pick-head:hover{background:rgba(127,127,127,.06)}
  .pick-head input{width:17px;height:17px;flex:none;cursor:pointer}
  .pick-name{font-weight:800;font-size:14.5px;flex:1}
  .pick-count{font-size:12.5px;font-weight:700;color:var(--muted)}
  .pick-caret{width:16px;height:16px;color:var(--muted);transition:transform .15s}
  .pick-group.open .pick-caret{transform:rotate(180deg)}
  .pick-plates{display:none;padding:2px 13px 11px 40px;flex-direction:column;gap:5px}
  .pick-group.open .pick-plates{display:flex}
  .pick-plate{display:flex;align-items:center;gap:9px;font-size:13.5px;cursor:pointer;padding:2px 0}
  .pick-plate input{width:15px;height:15px;flex:none;cursor:pointer}
  .pick-plate .t{flex:1}
  .pick-plate .c{font-size:12px;color:var(--muted);font-weight:700}
  .len-row{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:0 0 14px}
  .len-row .lbl{font-size:13.5px;font-weight:800;margin-right:2px}
  .len-btn{font:inherit;font-size:13.5px;font-weight:700;cursor:pointer;border:1px solid var(--line,#e5e7ef);
    background:var(--card,#fff);color:var(--muted);border-radius:9px;padding:7px 13px}
  .len-btn.on{background:var(--accent,#0d7d6c);border-color:var(--accent,#0d7d6c);color:#fff}
  .pick-summary{font-size:13.5px;font-weight:700;margin:0 0 12px;color:var(--muted)}
  .pick-summary b{color:var(--ink)}
  .pick-actions{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
  .mini-btn{font:inherit;font-size:12.5px;font-weight:700;cursor:pointer;border:0;background:transparent;
    color:var(--accent,#0d7d6c);text-decoration:underline;padding:2px 0}
"""

PICKER_HTML = """
    <div class="pick-tabs" id="pick-tabs"></div>
    <div class="pick-actions" style="margin:0 0 12px">
      <button type="button" class="mini-btn" onclick="pickAll(true)">Select everything shown</button>
      <button type="button" class="mini-btn" onclick="pickAll(false)">Clear selection</button>
    </div>
    <div class="pick-groups" id="pick-groups"></div>
    <div class="len-row" id="len-row">
      <span class="lbl">How many structures?</span>
      <button type="button" class="len-btn" data-len="10">10</button>
      <button type="button" class="len-btn on" data-len="20">20</button>
      <button type="button" class="len-btn" data-len="30">30</button>
      <button type="button" class="len-btn" data-len="60">60</button>
      <button type="button" class="len-btn" data-len="0">All selected</button>
    </div>
    <p class="pick-summary" id="pick-summary">Nothing selected yet.</p>
"""

PICKER_JS = r"""
/* ---------------- picker ----------------
   Builds ITEMS at run time from practicum-bank.js. Plate geometry (viewBox,
   arrow scale, reveal placement) travels with every structure, because a
   custom exam mixes plates whose sizes differ by more than 30x. */
const BANK = window.PRACTICUM_BANK || [];
let examFilter = "all";
let wantLen = 20;
const chosen = new Set();

/* Exam 2 and Exam 3 are kept apart: each gets its own heading with its own
   select-all, and section names sit underneath rather than being prefixed with
   the exam. Mixing them in one flat list made it easy to pick Exam 2 content by
   accident when revising for Exam 3. */
function bankByExam(){
  const out = new Map();
  BANK.forEach(p => {
    if (examFilter !== "all" && p.exam !== examFilter) return;
    if (!out.has(p.exam)) out.set(p.exam, new Map());
    const secs = out.get(p.exam);
    if (!secs.has(p.sec)) secs.set(p.sec, []);
    secs.get(p.sec).push(p);
  });
  return out;
}

function bankGroups(){
  const flat = new Map();
  bankByExam().forEach((secs, exam) => secs.forEach((plates, sec) => flat.set(exam + " · " + sec, plates)));
  return flat;
}

function renderTabs(){
  const exams = [...new Set(BANK.map(p => p.exam))].sort();
  const el = document.getElementById("pick-tabs");
  el.innerHTML = ['<button type="button" class="pick-tab' + (examFilter === "all" ? " on" : "") +
                  '" data-exam="all">Both exams</button>']
    .concat(exams.map(e => '<button type="button" class="pick-tab' + (examFilter === e ? " on" : "") +
                           '" data-exam="' + e + '">' + e + "</button>")).join("");
  el.querySelectorAll(".pick-tab").forEach(b => b.addEventListener("click", () => {
    examFilter = b.dataset.exam; renderTabs(); renderGroups(); updateSummary();
  }));
}

const CARET = '<svg class="pick-caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>';

function renderGroups(){
  const host = document.getElementById("pick-groups");
  host.innerHTML = "";
  bankByExam().forEach((secs, exam) => {
    let examPlates = 0, examItems = 0;
    secs.forEach(plates => {
      examPlates += plates.length;
      examItems += plates.reduce((s, p) => s + p.items.length, 0);
    });
    const hd = document.createElement("h2");
    hd.className = "exam-head";
    hd.innerHTML = '<span>' + exam + '</span>' +
      '<button type="button" class="exam-pick">select all</button>' +
      '<span class="exam-tally">' + examPlates + ' plates · ' + examItems + ' structures</span>';
    hd.querySelector(".exam-pick").addEventListener("click", () => {
      let all = true;
      secs.forEach(plates => plates.forEach(p => { if (!chosen.has(p.slug)) all = false; }));
      secs.forEach(plates => plates.forEach(p => all ? chosen.delete(p.slug) : chosen.add(p.slug)));
      renderGroups(); updateSummary();
    });
    host.appendChild(hd);
    renderSections(host, secs);
  });
}

function renderSections(host, secs){
  secs.forEach((plates, key) => {
    const n = plates.reduce((s, p) => s + p.items.length, 0);
    const wrap = document.createElement("div");
    wrap.className = "pick-group";
    const allOn = plates.every(p => chosen.has(p.slug));
    const someOn = !allOn && plates.some(p => chosen.has(p.slug));
    wrap.innerHTML =
      '<div class="pick-head"><input type="checkbox"' + (allOn ? " checked" : "") + '>' +
      '<span class="pick-name">' + key + '</span>' +
      '<span class="pick-count">' + plates.length + ' plates · ' + n + ' structures</span>' +
      CARET + '</div><div class="pick-plates"></div>';
    const box = wrap.querySelector(".pick-head input");
    box.indeterminate = someOn;
    box.addEventListener("click", e => {
      e.stopPropagation();
      plates.forEach(p => box.checked ? chosen.add(p.slug) : chosen.delete(p.slug));
      renderGroups(); updateSummary();
    });
    wrap.querySelector(".pick-head").addEventListener("click", () => wrap.classList.toggle("open"));

    const list = wrap.querySelector(".pick-plates");
    plates.forEach(p => {
      const row = document.createElement("label");
      row.className = "pick-plate";
      row.innerHTML = '<input type="checkbox"' + (chosen.has(p.slug) ? " checked" : "") + '>' +
                      '<span class="t">' + p.title + '</span><span class="c">' + p.items.length + '</span>';
      row.querySelector("input").addEventListener("change", ev => {
        ev.target.checked ? chosen.add(p.slug) : chosen.delete(p.slug);
        renderGroups(); updateSummary();
      });
      list.appendChild(row);
    });
    host.appendChild(wrap);
  });
}

function pickAll(on){
  bankGroups().forEach(plates => plates.forEach(p => on ? chosen.add(p.slug) : chosen.delete(p.slug)));
  renderGroups(); updateSummary();
}

function selectedPlates(){ return BANK.filter(p => chosen.has(p.slug)); }

function updateSummary(){
  const plates = selectedPlates();
  const n = plates.reduce((s, p) => s + p.items.length, 0);
  const take = wantLen === 0 ? n : Math.min(wantLen, n);
  const el = document.getElementById("pick-summary");
  el.innerHTML = n === 0
    ? "Nothing selected yet."
    : "<b>" + take + "</b> structure" + (take === 1 ? "" : "s") + " from <b>" + plates.length +
      "</b> plate" + (plates.length === 1 ? "" : "s") +
      (wantLen !== 0 && n > wantLen ? " (drawn at random from " + n + ")" : "");
  const btn = document.getElementById("start-btn");
  btn.disabled = n === 0;
  btn.textContent = n === 0 ? "Pick something to start" : "Start practicum →";
}

/* Reorder so consecutive structures come from different plates where the
   selection allows it -- the whole point is one structure then a new picture,
   not every label on one image in a row. */
function spreadByPlate(list){
  const byPlate = new Map();
  list.forEach(it => {
    if (!byPlate.has(it.slug)) byPlate.set(it.slug, []);
    byPlate.get(it.slug).push(it);
  });
  const out = [];
  let last = null;
  while (out.length < list.length){
    // take from the plate with most remaining that isn't the one just used
    let best = null;
    byPlate.forEach((arr, slug) => {
      if (!arr.length || slug === last) return;
      if (!best || arr.length > byPlate.get(best).length) best = slug;
    });
    if (best === null){                      // only the just-used plate is left
      byPlate.forEach((arr, slug) => { if (arr.length && best === null) best = slug; });
    }
    out.push(byPlate.get(best).pop());
    last = best;
  }
  return out;
}

function buildAndStart(){
  const plates = selectedPlates();
  let pool = [];
  plates.forEach(p => p.items.forEach(it => pool.push({
    answer: it.a, cx: it.x, cy: it.y, side: it.s,
    rx: it.rx, ry: it.ry, ra: it.ra,
    img: p.img, w: p.w, h: p.h, ak: p.ak, fs: p.fs,
    source: p.title, slug: p.slug
  })));
  if (!pool.length) return;
  pool = shuffle(pool);
  if (wantLen > 0) pool = pool.slice(0, wantLen);
  ITEMS = spreadByPlate(pool);
  buildWordBank();
  document.getElementById("picker-body").classList.add("hidden");
  startQuiz();
}

document.getElementById("len-row").addEventListener("click", e => {
  const b = e.target.closest(".len-btn");
  if (!b) return;
  wantLen = parseInt(b.dataset.len, 10);
  document.querySelectorAll(".len-btn").forEach(x => x.classList.toggle("on", x === b));
  updateSummary();
});

renderTabs(); renderGroups(); updateSummary();
"""


def main():
    s = open(TEMPLATE, encoding="utf-8").read()

    s = re.sub(r"<title>.*?</title>",
               "<title>Build Your Own Practicum — Anatomy Practicum</title>", s, count=1, flags=re.S)
    s = re.sub(r'<div class="eyebrow">.*?</div>',
               '<div class="eyebrow">Anatomy Practicum &middot; Build your own</div>', s, count=1, flags=re.S)
    s = re.sub(r"<h1>.*?</h1>", "<h1>Build Your Own Practicum</h1>", s, count=1, flags=re.S)
    s = re.sub(r'<p class="sub">.*?</p>',
               '<p class="sub">Choose the topics you want, pick a length, and get a randomized '
               'structure-identification exam &mdash; one structure per image, then a new image.</p>',
               s, count=1, flags=re.S)

    # back link points at the site root from here, not the parent folder
    s = s.replace('href="../index.html"', 'href="index.html"')
    s = s.replace('href="../', 'href="')
    s = s.replace('src="../', 'src="')

    # the bank supplies every structure
    s = s.replace("</head>", '<script src="practicum-bank.js"></script>\n</head>', 1)

    s = s.replace("</style>", PICKER_CSS + "</style>", 1)

    # the "how it works" list and count chip describe a fixed exam; replace the
    # whole block between the sub line and the start toggles with the picker
    start_i = s.index('<div class="obj">')
    end_i = s.index('<div class="wordbank-row start-toggles">')
    s = s[:start_i] + '<div id="picker-body">' + PICKER_HTML + "</div>\n    " + s[end_i:]

    # ITEMS is now built at run time
    s = re.sub(r"const ITEMS = \[.*?\];", "let ITEMS = [];", s, count=1, flags=re.S)

    # the start button builds the exam instead of starting a fixed one
    s = re.sub(r'(<button[^>]*id="start-btn"[^>]*onclick=")[^"]*(")', r"\1buildAndStart()\2", s, count=1)

    # a stale saved attempt can't be resumed into a freshly built exam
    s = s.replace("</body>", "<script>\n" + PICKER_JS + "\n</script>\n</body>", 1)
    s = s.replace('$("resume-banner").classList.add("hidden");',
                  '$("resume-banner").classList.add("hidden");', 1)

    open(OUT, "w", encoding="utf-8").write(s)
    print(f"wrote {os.path.relpath(OUT, ROOT)} ({os.path.getsize(OUT)/1024:.0f} KB)")


if __name__ == "__main__":
    main()
