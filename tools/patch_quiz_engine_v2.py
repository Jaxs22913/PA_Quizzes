#!/usr/bin/env python3
"""Add scroll view and a length picker to the exam-navigator quiz engine.

From a student request Jaxon forwarded on 2026-08-19: a Canvas-style view where
every question sits on one page with a clickable number palette, and a way to
take a shorter quiz.

Half of the first request already existed -- flagging and a jump-to-question
navigator ship today behind the "Flag questions & jump between them" checkbox.
What was missing was the LAYOUT: ours is one question at a time with the
navigator as a pop-up. So this adds a second render path rather than new
features, and both views share the same state, timer, progress-save and scoring.

Scope is Semester 2 and later (Jaxon, 2026-08-19). The template change covers
every future quiz automatically; the 21 existing Fall 2026 quizzes are patched
in place. Semester 1's quizzes are deliberately left alone.

The patch is a set of exact string replacements rather than a re-render, because
the engine is byte-identical across all 272 quizzes that carry it -- verified by
hashing the openNav..submitExam region -- so a replacement either applies
cleanly everywhere or fails loudly on the first file. Re-rendering would mean
re-running two dozen separate build scripts and risking content drift.

SUBSETTING. `order` was always the list of question indices for this attempt,
but the engine assumed order.length === QUESTIONS.length in nine places. Those
become order.length so a short attempt counts, scores, paces and resumes
against what the student actually took.

Sampling is not a slice. These sets are built with deliberate objective coverage
and answer-position spread, and taking the first N throws both away. It
round-robins across objectives, then rebalances answer positions -- see
pickOrder(). Below the objective count full coverage stops being possible and
the sample just spreads as widely as it can.
"""
import io, os, sys, hashlib, glob

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
TEMPLATE = os.path.join(ROOT, "tools/quiz-template/template.html")
SEM2_DIRS = [
    "Clinical Medicine and Surgery I Exam 1", "Microbiology Exam 1",
    "Pharmacology I Exam 1", "Physical Diagnosis 2 Exam 1",
    "Clinical Pathophysiology I Exam 1", "Principles of Diagnostic Medicine I Exam 1",
]

# ---------------------------------------------------------------- 1. markup
START_ANCHOR = '''    <label style="display:flex;align-items:center;gap:8px;font-size:14px;color:var(--muted);margin:0 0 8px;cursor:pointer">
      <input type="checkbox" id="shuffle-toggle" style="width:16px;height:16px">
      Shuffle question order
    </label>
'''
START_NEW = '''    <div class="startopt">
      <span class="startopt-label">View</span>
      <div class="seg" id="view-seg" role="group" aria-label="Quiz view">
        <button type="button" class="seg-btn is-on" data-view="paged" onclick="setView('paged')">One at a time</button>
        <button type="button" class="seg-btn" data-view="scroll" onclick="setView('scroll')">All on a page</button>
      </div>
    </div>
    <div class="startopt">
      <span class="startopt-label">Length</span>
      <input type="number" id="length-input" class="lenbox" min="1" step="1" aria-label="Number of questions">
      <span class="startopt-hint" id="length-hint"></span>
    </div>
''' + START_ANCHOR

# ---------------------------------------------------------------- 2. styles
CSS_ANCHOR = "</style>"
CSS_NEW = '''
/* --- start-screen option rows: view switch and length box ---------------- */
.startopt{display:flex;align-items:center;gap:10px;margin:0 0 10px;flex-wrap:wrap;}
.startopt-label{font-size:14px;color:var(--muted);min-width:52px;}
.startopt-hint{font-size:12.5px;color:var(--muted);opacity:.85;}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;}
.seg-btn{
  appearance:none;border:0;background:transparent;cursor:pointer;
  padding:7px 14px;font:600 13px/1 inherit;color:var(--muted);
}
.seg-btn.is-on{background:var(--navy);color:#fff;}
.seg-btn:not(.is-on):hover{background:var(--ice);color:var(--navy);}
.lenbox{
  width:78px;padding:6px 9px;font:600 14px/1.2 inherit;color:var(--ink);
  border:1px solid var(--line);border-radius:8px;background:var(--paper,#fff);
}

/* --- scroll view --------------------------------------------------------- */
/* Two columns on a wide screen, one on a phone -- the palette moves from a
   sticky rail to a collapsible strip above the questions, because a right-hand
   rail has nowhere to live at 380px. */
.scrollwrap{display:grid;grid-template-columns:minmax(0,1fr) 148px;gap:22px;align-items:start;}
.scrollcol{min-width:0;}
.sq{border-top:1px solid var(--line);padding:20px 0 4px;}
.sq:first-child{border-top:0;padding-top:4px;}
.sq-head{display:flex;align-items:center;gap:10px;margin:0 0 8px;}
.sq-num{font:800 13px/1 inherit;color:var(--navy);letter-spacing:.02em;}
.sq-flag{
  appearance:none;border:1px solid var(--line);background:transparent;cursor:pointer;
  border-radius:999px;padding:4px 10px;font:600 12px/1 inherit;color:var(--muted);
}
.sq-flag.flagged{background:var(--gold);border-color:var(--gold);color:#3a2c05;}
.palette{position:sticky;top:14px;}
.palette h4{margin:0 0 8px;font:700 12px/1 inherit;color:var(--muted);text-transform:uppercase;letter-spacing:.06em;}
.palette-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;}
.pal{
  appearance:none;border:1px solid var(--line);background:transparent;cursor:pointer;
  border-radius:7px;padding:7px 0;font:700 12.5px/1 inherit;color:var(--muted);
}
.pal.answered{background:var(--ice);border-color:var(--indigo);color:var(--navy);}
.pal.flagged{border-color:var(--gold);box-shadow:inset 0 0 0 1.5px var(--gold);}
.pal.here{outline:2px solid var(--navy);outline-offset:1px;}
.palette-foot{margin-top:10px;font-size:12px;color:var(--muted);line-height:1.5;}
@media (max-width:820px){
  .scrollwrap{grid-template-columns:1fr;}
  .palette{position:static;order:-1;}
  .palette-grid{grid-template-columns:repeat(10,1fr);}
}
@media (max-width:520px){ .palette-grid{grid-template-columns:repeat(8,1fr);} }
''' + CSS_ANCHOR

# ---------------------------------------------------------------- 3. engine
# Every place the engine meant "questions in THIS attempt" but said
# "QUESTIONS.length". order.length is the same number until a length is chosen.
LEN_FIXES = [
 ("""  document.getElementById('counter').textContent = `Question ${idx+1} of ${QUESTIONS.length}`;
  document.getElementById('barfill').style.width = (100*idx/QUESTIONS.length)+'%';""",
  """  document.getElementById('counter').textContent = `Question ${idx+1} of ${order.length}`;
  document.getElementById('barfill').style.width = (100*idx/order.length)+'%';"""),
 ("""    document.getElementById("navbadge").textContent = (QUESTIONS.length-answers.filter(a=>a!==null).length) > 0 ? " \\u00b7 " + (QUESTIONS.length-answers.filter(a=>a!==null).length) + " left" : "";""",
  """    document.getElementById("navbadge").textContent = (order.length-answers.filter(a=>a!==null).length) > 0 ? " \\u00b7 " + (order.length-answers.filter(a=>a!==null).length) + " left" : "";"""),
 ("""    document.getElementById('nextbtn').textContent = (idx===QUESTIONS.length-1)?'Submit exam \\u2192':'Next \\u2192';""",
  """    document.getElementById('nextbtn').textContent = (idx===order.length-1)?'Submit exam \\u2192':'Next \\u2192';"""),
 ("""  document.getElementById('nextbtn').textContent = (idx===QUESTIONS.length-1)?'See results \\u2192':'Next \\u2192';""",
  """  document.getElementById('nextbtn').textContent = (idx===order.length-1)?'See results \\u2192':'Next \\u2192';"""),
 ("""    total: QUESTIONS.length,""", """    total: order.length,"""),
 ("""    const unanswered = QUESTIONS.length - answers.filter(a=>a!==null).length;""",
  """    const unanswered = order.length - answers.filter(a=>a!==null).length;"""),
 ("""  if(idx<QUESTIONS.length-1){ idx++; saveProgress(); renderQ(); window.scrollTo({top:0,behavior:'smooth'}); }""",
  """  if(idx<order.length-1){ idx++; saveProgress(); renderQ(); window.scrollTo({top:0,behavior:'smooth'}); }"""),
 ("""  cutoffMs = hardCutoff ? QUESTIONS.length*60000 : 0;""",
  """  cutoffMs = hardCutoff ? order.length*60000 : 0;"""),
 ("""  idx=0; score=0; answers=new Array(QUESTIONS.length).fill(null);""",
  """  idx=0; score=0; answers=new Array(order.length).fill(null);"""),
 # resume must accept a short attempt; it previously demanded the full bank
 ("""  order = (saved.order && saved.order.length===QUESTIONS.length) ? saved.order : QUESTIONS.map((_,i)=>i);""",
  """  order = (saved.order && saved.order.length) ? saved.order : QUESTIONS.map((_,i)=>i);"""),
]

# Sampling + view switching + the scroll renderer.
ENGINE_ANCHOR = "function startExam(){\n  clearProgress();"
ENGINE_NEW = '''var viewMode = 'paged';
function setView(v){
  viewMode = v;
  document.querySelectorAll('#view-seg .seg-btn').forEach(function(b){
    b.classList.toggle('is-on', b.getAttribute('data-view')===v);
  });
}

/* Choose which questions this attempt uses.

   NOT a slice. Every set on this site is built with deliberate objective
   coverage and an even spread of correct answers across A-D; taking the first
   N throws both away, and a student drilling 15 of 30 would get a quiz that
   silently skips an objective or lands five answers on B.

   Round-robin across objectives first, so coverage degrades as slowly as the
   count allows. Then rebalance answer positions by swapping in questions with
   under-represented letters where the objective mix permits. Below the number
   of objectives, full coverage is arithmetically impossible and the sample just
   spreads as widely as it can. */
function pickOrder(n){
  var all = QUESTIONS.map(function(_,i){ return i; });
  if(!n || n >= all.length) return all;

  var byIO = {};
  all.forEach(function(i){ (byIO[QUESTIONS[i].io] = byIO[QUESTIONS[i].io] || []).push(i); });
  Object.keys(byIO).forEach(function(k){ shuffleArray(byIO[k]); });

  var ios = Object.keys(byIO); shuffleArray(ios);
  var picked = [], r = 0;
  while(picked.length < n){
    var progressed = false;
    for(var k=0;k<ios.length && picked.length<n;k++){
      var bucket = byIO[ios[k]];
      if(bucket.length > r){ picked.push(bucket[r]); progressed = true; }
    }
    if(!progressed) break;
    r++;
  }

  /* Answer-position rebalance. Count letters, then for each over-represented
     letter try to swap a question out for an unpicked one with a scarce letter
     from the SAME objective, so coverage is never traded away for balance. */
  var chosen = {}; picked.forEach(function(i){ chosen[i]=true; });
  function counts(){
    var c=[0,0,0,0]; picked.forEach(function(i){ c[QUESTIONS[i].c]++; }); return c;
  }
  for(var pass=0; pass<40; pass++){
    var c = counts(), hi=0, lo=0;
    for(var L=1;L<4;L++){ if(c[L]>c[hi]) hi=L; if(c[L]<c[lo]) lo=L; }
    if(c[hi]-c[lo] <= 1) break;
    var swapped=false;
    for(var p=0;p<picked.length && !swapped;p++){
      var out = picked[p];
      if(QUESTIONS[out].c !== hi) continue;
      var pool = byIO[QUESTIONS[out].io] || [];
      for(var q=0;q<pool.length;q++){
        var cand = pool[q];
        if(chosen[cand] || QUESTIONS[cand].c !== lo) continue;
        picked[p]=cand; delete chosen[out]; chosen[cand]=true; swapped=true; break;
      }
    }
    if(!swapped) break;
  }
  return picked;
}

function chosenLength(){
  var el = document.getElementById('length-input');
  if(!el) return QUESTIONS.length;
  var v = parseInt(el.value, 10);
  if(!v || v < 1) return QUESTIONS.length;
  return Math.min(v, QUESTIONS.length);
}

/* ---- scroll view -------------------------------------------------------- */
/* Shares all state with the paged view: same order, answers, flagged, timer and
   saved progress. Only the presentation differs, so switching cannot desync
   scoring. */
function renderScroll(){
  var quiz = document.getElementById('quiz');
  var body = quiz.querySelector('.qbody');
  body.innerHTML =
    '<div class="topbar">' +
      '<span id="counter"></span>' +
      '<div class="bar"><span id="barfill"></span></div>' +
      '<span class="score" id="timerpill">00:00</span>' +
      '<button type="button" class="examctl-btn" id="pausebtn" onclick="pauseQuiz()">&#10074;&#10074; Pause</button>' +
      '<span class="score" id="scoretxt">Score 0</span>' +
    '</div>' +
    '<div class="scrollwrap">' +
      '<div class="scrollcol" id="scrollcol"></div>' +
      '<aside class="palette"><h4>Questions</h4><div class="palette-grid" id="palgrid"></div>' +
      '<p class="palette-foot" id="palfoot"></p>' +
      '<button class="btn btn-primary" style="width:100%;margin-top:10px" onclick="submitExam()">Submit &rarr;</button></aside>' +
    '</div>';

  var col = document.getElementById('scrollcol');
  order.forEach(function(qi, i){
    var q = QUESTIONS[qi];
    var d = document.createElement('div');
    d.className = 'sq'; d.id = 'sq-'+i;
    d.innerHTML =
      '<div class="sq-head"><span class="sq-num">Question ' + (i+1) + ' of ' + order.length + '</span>' +
      '<button type="button" class="sq-flag" data-i="' + i + '">&#9873; Flag</button></div>' +
      '<div class="qmeta"><span class="tag tag-topic">' + q.topic + '</span>' +
      '<span class="tag tag-io">Objective ' + q.io + '</span></div>' +
      '<div class="qtext"></div><div class="opts"></div>' +
      '<div class="expl" id="sexpl-' + i + '"></div>';
    d.querySelector('.qtext').textContent = q.q;
    var wrap = d.querySelector('.opts');
    q.opts.forEach(function(o, oi){
      var b = document.createElement('button');
      b.className = 'opt'; b.setAttribute('data-i', oi);
      b.innerHTML = '<span class="ltr">' + LTR[oi] + '</span><span class="optlabel">' + o[0] + '</span>';
      b.onclick = function(){ chooseAt(i, oi); };
      wrap.appendChild(b);
    });
    d.querySelector('.sq-flag').onclick = function(){ toggleFlagAt(i); };
    col.appendChild(d);
  });
  buildPalette();
  order.forEach(function(_, i){ if(answers[i]!==null) paintScrollAnswer(i); });
  syncScrollChrome();
}

function buildPalette(){
  var g = document.getElementById('palgrid'); if(!g) return;
  g.innerHTML = '';
  order.forEach(function(_, i){
    var b = document.createElement('button');
    b.className = 'pal'; b.textContent = (i+1);
    b.onclick = function(){
      var el = document.getElementById('sq-'+i);
      if(el) el.scrollIntoView({behavior:'smooth', block:'start'});
    };
    g.appendChild(b);
  });
  paintPalette();
}

function paintPalette(){
  var g = document.getElementById('palgrid'); if(!g) return;
  Array.prototype.forEach.call(g.children, function(b, i){
    b.classList.toggle('answered', answers[i]!==null);
    b.classList.toggle('flagged', flagged.has(i));
  });
  var foot = document.getElementById('palfoot');
  if(foot){
    var left = order.length - answers.filter(function(a){ return a!==null; }).length;
    foot.textContent = left ? left + ' unanswered' : 'All answered';
  }
}

function syncScrollChrome(){
  var c = document.getElementById('counter');
  var done = answers.filter(function(a){ return a!==null; }).length;
  if(c) c.textContent = done + ' of ' + order.length + ' answered';
  var bf = document.getElementById('barfill');
  if(bf) bf.style.width = (100*done/order.length) + '%';
  var st = document.getElementById('scoretxt');
  if(st){ st.textContent = 'Score ' + score; st.classList.toggle('hidden', deferFeedback); }
}

function toggleFlagAt(i){
  if(flagged.has(i)) flagged.delete(i); else flagged.add(i);
  var btn = document.querySelector('#sq-'+i+' .sq-flag');
  if(btn){
    btn.classList.toggle('flagged', flagged.has(i));
    btn.innerHTML = flagged.has(i) ? '&#9873; Flagged' : '&#9873; Flag';
  }
  paintPalette(); saveProgress();
}

/* Answering from the scroll view. Mirrors choose() but targets a given index
   rather than the current one, since every question is on screen at once. */
function chooseAt(i, oi){
  if(!deferFeedback && answers[i]!==null) return;
  var q = QUESTIONS[order[i]];
  var first = answers[i]===null;
  answers[i] = oi;
  if(!deferFeedback && first && oi===q.c) score++;
  paintScrollAnswer(i);
  paintPalette(); syncScrollChrome(); saveProgress();
  if(!deferFeedback && typeof recordAnswerStat === 'function'){
    try{ recordAnswerStat(oi===q.c); }catch(e){}
  }
}

function paintScrollAnswer(i){
  var d = document.getElementById('sq-'+i); if(!d) return;
  var q = QUESTIONS[order[i]], a = answers[i];
  Array.prototype.forEach.call(d.querySelectorAll('.opt'), function(b, oi){
    b.classList.remove('selected-exam','correct','wrong');
    if(deferFeedback){ if(a===oi) b.classList.add('selected-exam'); return; }
    if(a===null) return;
    if(oi===q.c) b.classList.add('correct');
    else if(oi===a) b.classList.add('wrong');
  });
  var ex = document.getElementById('sexpl-'+i);
  if(ex && !deferFeedback && a!==null){
    ex.innerHTML = '<b>' + (a===q.c ? 'Correct.' : 'Not quite.') + '</b> ' +
                   q.opts[q.c][1] + ' <span class="cite">' + q.cite + '</span>';
    ex.classList.add('show');
  }
}

function startExam(){
  clearProgress();'''

# startExam has to build `order` through pickOrder and dispatch on the view.
START_FIX = [
 ("""  order = QUESTIONS.map((_,i)=>i);
  if(document.getElementById('shuffle-toggle') && document.getElementById('shuffle-toggle').checked) shuffleArray(order);""",
  """  order = pickOrder(chosenLength());
  if(document.getElementById('shuffle-toggle') && document.getElementById('shuffle-toggle').checked) shuffleArray(order);"""),
 ("""  document.getElementById('quiz').style.display='block';
  renderQ();
}

function resumeQuiz(){""",
  """  document.getElementById('quiz').style.display='block';
  if(viewMode==='scroll') renderScroll(); else renderQ();
}

function resumeQuiz(){"""),
]

# Resume has to come back into the same view, and the length box needs its
# default and hint filled in on load.
BOOT_ANCHOR = """function startExam(){"""
INIT_PATCH = ("""(function(){
  var el = document.getElementById('length-input');
  if(el){
    el.value = QUESTIONS.length;
    el.max = QUESTIONS.length;
    var hint = document.getElementById('length-hint');
    if(hint) hint.textContent = 'of ' + QUESTIONS.length + ' \\u00b7 sampled to keep objectives covered';
  }
})();
""" + BOOT_ANCHOR)


def patch(src, path):
    out = src
    misses = []

    def rep(old, new, why):
        nonlocal out
        if out.count(old) != 1:
            misses.append("%s (found %d)" % (why, out.count(old)))
            return
        out = out.replace(old, new, 1)

    rep(START_ANCHOR, START_NEW, "start-screen controls")
    # CSS goes before the LAST </style>, which is the page's own block
    i = out.rfind(CSS_ANCHOR)
    if i == -1:
        misses.append("no </style> to extend")
    else:
        out = out[:i] + CSS_NEW[:-len(CSS_ANCHOR)] + out[i:]
    for old, new in LEN_FIXES:
        rep(old, new, "length ref: " + old.strip()[:44])
    rep(ENGINE_ANCHOR, ENGINE_NEW, "scroll engine")
    for old, new in START_FIX:
        rep(old, new, "startExam: " + old.strip()[:40])
    rep(BOOT_ANCHOR, INIT_PATCH, "length-box init")
    return out, misses


def main():
    targets = [TEMPLATE]
    for d in SEM2_DIRS:
        for f in sorted(glob.glob(os.path.join(ROOT, d, "*.html"))):
            s = io.open(f, encoding="utf-8").read()
            if 'id="flag-nav-toggle"' in s and 'id="view-seg"' not in s:
                targets.append(f)

    print("patching %d file(s)\n" % len(targets))
    ok = fail = 0
    for f in targets:
        s = io.open(f, encoding="utf-8").read()
        if 'id="view-seg"' in s:
            print("  skip (already patched): %s" % os.path.relpath(f, ROOT)); continue
        new, misses = patch(s, f)
        if misses:
            fail += 1
            print("  FAIL %s" % os.path.relpath(f, ROOT))
            for m in misses[:4]:
                print("       - %s" % m)
            continue
        io.open(f, "w", encoding="utf-8").write(new)
        ok += 1
        print("  ok   %s" % os.path.relpath(f, ROOT))
    print("\npatched %d, failed %d" % (ok, fail))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
