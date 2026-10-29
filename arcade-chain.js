/* Acid-Base Case Chains (arcade-chain.html?set=<id>[&case=<caseId>][&from=home]).
   Each case is one patient worked through a chain of steps. A wrong pick offers "Try again" or "Walk me
   through this step" (the reasoning with the case's own numbers, then the answer). A step scores only when
   it is right on the first try. Case data: arcade-chain/<set>.json, written by tools/build_acid_base_chain.py
   and checked by tools/check_acid_base_cases.py; never hand-edit it.
   Progress: localStorage abchain_v1 through arcade.js (loadChainStore/saveChainStore), never the quiz
   qc:/qa:/qm: records, so nothing here feeds medals, the exam countdown or Pip. */
(function () {
  "use strict";

  var params = new URLSearchParams(location.search);
  var META = findChainSet(params.get("set"));
  var FROM_HOME = params.get("from") === "home";
  var app = document.getElementById("chain-app");
  var live = document.getElementById("chain-live");
  var DATA = null;          // the set's JSON
  var view = "home";        // "home" | "case"
  var C = null;             // current case object
  var cur = null;           // { idx: active step index, phase: "ask" | "wrong" | "resolved" }

  var REDUCED = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  function esc(t) {
    return String(t == null ? "" : t).replace(/[&<>"']/g, function (ch) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch];
    });
  }
  function say(msg) { if (live) { live.textContent = ""; setTimeout(function () { live.textContent = msg; }, 30); } }
  function stripCorrect(t) { return String(t).replace(/^Correct\.\s*/, ""); }
  function reportLine() {
    return '<p class="chain-report-line"><a href="#" onclick="event.preventDefault(); window.reportMistake()">' +
           'If you see any mistakes, click here to report it</a></p>';
  }

  // ---- back link ----
  (function () {
    var a = document.getElementById("chain-back"), t = document.getElementById("chain-back-text");
    if (FROM_HOME) { a.href = "index.html"; t.textContent = "Back to home"; }
  })();

  // ---- progress store ----
  function setRec() {
    var s = loadChainStore();
    if (!s.sets[META.id]) s.sets[META.id] = { cases: {} };
    return s;
  }
  function caseRec(id) {
    var s = loadChainStore();
    return ((s.sets[META.id] || {}).cases || {})[id] || null;
  }
  function writeCase(id, rec) {
    var s = setRec();
    s.sets[META.id].cases[id] = rec;
    s.sets[META.id].last = id;
    saveChainStore(s);
  }
  function clearSet() {
    var s = loadChainStore();
    delete s.sets[META.id];
    saveChainStore(s);
  }

  function setURL(caseId) {
    var p = new URLSearchParams();
    p.set("set", META.id);
    if (caseId) p.set("case", caseId);
    if (FROM_HOME) p.set("from", "home");
    try { history.replaceState(null, "", location.pathname + "?" + p.toString()); } catch (e) {}
  }

  function scrollToEl(el, focusEl) {
    if (!el) return;
    try { el.scrollIntoView({ behavior: REDUCED ? "auto" : "smooth", block: "start" }); } catch (e) { el.scrollIntoView(); }
    if (focusEl) { try { focusEl.focus({ preventScroll: true }); } catch (e) { focusEl.focus(); } }
  }

  // ================= home (the set's case list) =================
  function nextCaseId() {
    for (var i = 0; i < DATA.cases.length; i++) {
      var r = caseRec(DATA.cases[i].id);
      if (!r || !r.done) return DATA.cases[i].id;
    }
    return null;
  }

  function renderHome() {
    view = "home";
    C = null; cur = null;
    setURL(null);
    document.title = DATA.name + " (" + DATA.exam + ") — Arcade";
    var prog = chainProgress(META.id);
    var nxt = nextCaseId();
    var started = null;
    DATA.cases.some(function (c) { var r = caseRec(c.id); if (r && !r.done && r.steps && Object.keys(r.steps).length) { started = c; return true; } return false; });
    var target = started ? started.id : nxt;
    var tcase = DATA.cases.filter(function (c) { return c.id === target; })[0];
    var mainLabel = !prog.done && !started ? "Start with case 1"
      : target ? (started ? "Continue case " + tcase.n : "Next: case " + tcase.n) : "All done: replay case 1";
    var pct = prog.steps ? Math.round(prog.first / prog.steps * 100) : null;

    var rows = DATA.cases.map(function (c) {
      var r = caseRec(c.id);
      var st, cls;
      if (r && r.done) {
        var f = 0, n = 0;
        Object.keys(r.steps || {}).forEach(function (k) { n++; if (r.steps[k].first) f++; });
        st = f + " of " + n + " first try"; cls = f === n ? "is-perfect" : "is-done";
      } else if (r && r.steps && Object.keys(r.steps).length) {
        st = "In progress"; cls = "is-started";
      } else { st = c.steps.length + " steps"; cls = ""; }
      return '<li><button type="button" class="chain-case-row ' + cls + '" data-case="' + esc(c.id) + '">' +
             '<span class="ccr-n">' + c.n + '</span>' +
             '<span class="ccr-who">' + esc(c.who) + '</span>' +
             '<span class="ccr-st">' + esc(st) + '</span></button></li>';
    }).join("");

    app.innerHTML =
      '<section class="chain-hero" aria-labelledby="chain-set-title">' +
        '<p class="chain-eyebrow">' + esc(DATA.course) + ' &middot; ' + esc(DATA.exam) + '</p>' +
        '<h2 id="chain-set-title">' + esc(DATA.name) + '</h2>' +
        '<p class="chain-scope">' + esc(DATA.scope) + ' &middot; ' + DATA.cases.length + ' cases</p>' +
        '<p class="chain-intro">' + esc(DATA.intro) + '</p>' +
        '<div class="chain-stats">' +
          '<div><b>' + prog.done + '</b><span>of ' + DATA.cases.length + ' cases done</span></div>' +
          '<div><b>' + (pct == null ? "&ndash;" : pct + "%") + '</b><span>steps right on the first try</span></div>' +
        '</div>' +
        '<div class="deck-actions">' +
          '<button type="button" class="btn sprint" data-act="open" data-case="' + esc(target || DATA.cases[0].id) + '">' + esc(mainLabel) + '</button>' +
          '<button type="button" class="btn ghost" data-act="random">Random case</button>' +
        '</div>' +
        '<p class="chain-how">A wrong pick lets you try again or walk through the step with this patient\'s numbers. ' +
        'A step counts only when it is right on the first try.<span class="chain-keys"> Keys: 1 to 4 pick, T try again, ' +
        'W walk me through, Enter next.</span></p>' +
      '</section>' +
      '<h3 class="chain-h3">All cases</h3>' +
      '<ol class="chain-case-list">' + rows + '</ol>' +
      runSummaryHTML() +
      (prog.done || started ? '<p class="chain-reset"><button type="button" class="chain-linkbtn" data-act="reset">Clear my progress for this set</button></p>' : "") +
      reportLine();
  }

  // per step type, right first try / tried, across finished cases
  function runSummaryHTML() {
    var agg = {}, order = [];
    DATA.cases.forEach(function (c) {
      var r = caseRec(c.id);
      if (!r || !r.done) return;
      c.steps.forEach(function (s) {
        var rs = (r.steps || {})[s.id];
        if (!rs) return;
        if (!agg[s.label]) { agg[s.label] = { f: 0, n: 0, h: 0 }; order.push(s.label); }
        agg[s.label].n++;
        if (rs.first) agg[s.label].f++;
        if (rs.helped) agg[s.label].h++;
      });
    });
    if (!order.length) return "";
    var rows = order.map(function (k) {
      var a = agg[k], p = Math.round(a.f / a.n * 100);
      return '<tr><th scope="row">' + esc(k) + '</th><td>' + a.f + ' of ' + a.n + '</td>' +
             '<td><span class="chain-meter" aria-hidden="true"><i style="width:' + p + '%"></i></span>' + p + '%</td>' +
             '<td>' + (a.h ? a.h + (a.h === 1 ? " walk-through" : " walk-throughs") : "&ndash;") + '</td></tr>';
    }).join("");
    return '<section class="chain-run" aria-labelledby="chain-run-h"><h3 class="chain-h3" id="chain-run-h">Your steps so far</h3>' +
           '<div class="chain-table-wrap"><table class="chain-run-table"><thead><tr><th scope="col">Step</th>' +
           '<th scope="col">First try</th><th scope="col">Rate</th><th scope="col">Help</th></tr></thead><tbody>' + rows +
           '</tbody></table></div></section>';
  }

  // ================= case view =================
  function labTable(c) {
    var rows = c.labs.map(function (r) {
      return '<tr><th scope="row">' + esc(r.label) + '</th><td><b>' + esc(r.v) + '</b>' +
             (r.unit ? ' <span class="u">' + esc(r.unit) + '</span>' : "") + '</td><td>' + esc(r.range) + '</td></tr>';
    }).join("");
    return '<table class="chain-labs"><caption class="sr-only">Results with normal ranges</caption>' +
           '<thead><tr><th scope="col">Test</th><th scope="col">Result</th><th scope="col">Normal</th></tr></thead>' +
           '<tbody>' + rows + '</tbody></table>';
  }
  function labStrip(c) {
    return '<div class="chain-strip" aria-hidden="true">' + c.labs.map(function (r) {
      return '<span><i>' + esc(r.short || r.label) + '</i> <b>' + esc(r.v) + '</b></span>';
    }).join("") + '</div>';
  }

  function openCase(id, fresh) {
    var c = DATA.cases.filter(function (x) { return x.id === id; })[0];
    if (!c) { renderHome(); return; }
    C = c; view = "case";
    var rec = caseRec(c.id);
    if (fresh || !rec || rec.done) rec = { done: false, steps: {} };
    writeCase(c.id, rec);
    setURL(c.id);
    document.title = c.title + " — " + DATA.name + " — Arcade";
    // first step not yet finished
    var idx = 0;
    while (idx < c.steps.length && rec.steps[c.steps[idx].id] && rec.steps[c.steps[idx].id].done) idx++;
    cur = { idx: idx, phase: "ask", tried: [] };
    var active = rec.steps[(c.steps[idx] || {}).id];
    if (active && active.tries) cur.tried = active.tries.slice();

    app.innerHTML =
      '<div class="chain-case">' +
        '<div class="chain-bar">' +
          '<button type="button" class="chain-linkbtn" data-act="home">All cases</button>' +
          '<span id="progress" class="chain-progress"></span>' +
        '</div>' +
        labStrip(c) +
        '<div class="chain-grid">' +
          '<aside class="chain-patient" aria-labelledby="chain-case-title">' +
            '<h2 id="chain-case-title">' + esc(c.title) + ' <span>' + esc(c.who) + '</span></h2>' +
            '<p class="chain-vignette">' + esc(c.vignette) + '</p>' +
            labTable(c) +
          '</aside>' +
          '<section class="chain-steps" aria-label="Steps">' +
            '<p id="qtopic" class="chain-topic"></p>' +
            '<div id="chain-step-list"></div>' +
            '<div id="chain-summary-slot"></div>' +
            reportLine() +
          '</section>' +
        '</div>' +
      '</div>';
    var list = document.getElementById("chain-step-list");
    for (var i = 0; i < idx; i++) list.appendChild(doneCard(i, rec.steps[c.steps[i].id]));
    if (idx < c.steps.length) {
      list.appendChild(activeCard(idx));
      updateBar();
      if (!fresh && idx > 0) scrollToEl(document.getElementById("step-" + c.steps[idx].id));
      else window.scrollTo(0, 0);
    } else {
      finishCase(true);
    }
  }

  function updateBar() {
    var p = document.getElementById("progress"), t = document.getElementById("qtopic");
    var s = C.steps[cur.idx];
    if (p) p.textContent = C.title + " of " + DATA.cases.length + (s ? " · Step " + (cur.idx + 1) + " of " + C.steps.length : " · Done");
    if (t) t.textContent = DATA.name + " · " + C.who + (s ? " · " + s.label : "");
  }

  function optionsHTML(s, tried) {
    return s.options.map(function (o, i) {
      var wrong = tried.indexOf(i) !== -1;
      return '<button type="button" class="learn-choice chain-opt' + (wrong ? " wrong" : "") + '" data-opt="' + i + '"' +
             (wrong ? ' disabled aria-disabled="true"' : "") + '>' +
             '<span class="letter">' + LETTERS[i] + '</span><span class="opt-t">' + esc(o.t) + '</span></button>';
    }).join("");
  }

  function activeCard(i) {
    var s = C.steps[i];
    var el = document.createElement("article");
    el.className = "chain-step is-active";
    el.id = "step-" + s.id;
    el.innerHTML =
      '<header class="cs-head"><span class="cs-num">Step ' + (i + 1) + ' of ' + C.steps.length + '</span>' +
      '<span class="cs-label">' + esc(s.label) + '</span></header>' +
      '<p class="cs-prompt" id="qtext" tabindex="-1">' + esc(s.prompt) + '</p>' +
      '<div class="cs-opts" role="group" aria-label="Choices for step ' + (i + 1) + '">' + optionsHTML(s, cur.tried) + '</div>' +
      '<div class="cs-fb"></div>';
    if (cur.tried.length) {
      cur.phase = "wrong";
      el.querySelector(".cs-fb").innerHTML = wrongHTML(s, cur.tried[cur.tried.length - 1]);
    }
    return el;
  }

  function othersHTML(s) {
    var items = s.options.map(function (o, i) {
      if (i === s.key) return "";
      return '<li><b>' + LETTERS[i] + '. ' + esc(o.t) + '</b> ' + esc(o.e) + '</li>';
    }).join("");
    return '<details class="cs-others"><summary>Why the other choices are wrong</summary><ul>' + items + '</ul></details>';
  }

  function wrongHTML(s, pick) {
    return '<div class="fb fb-wrong">' +
             '<p class="fb-verdict"><b>Not quite.</b> ' + esc(s.options[pick].t) + ' is not the answer for this step.</p>' +
             '<div class="fb-actions">' +
               '<button type="button" class="btn ghost" data-act="retry">Try again <kbd>T</kbd></button>' +
               '<button type="button" class="btn primary" data-act="walk">Walk me through this step <kbd>W</kbd></button>' +
             '</div>' +
           '</div>';
  }

  function resolvedHTML(s, mode, last) {
    var key = s.options[s.key];
    var head = mode === "walk"
      ? '<p class="fb-verdict"><b>Here is this step, worked through.</b></p><ol class="fb-walk">' +
          s.walk.map(function (w) { return "<li>" + esc(w) + "</li>"; }).join("") + '</ol>' +
          '<p class="fb-answer">Answer: <b>' + LETTERS[s.key] + '. ' + esc(key.t) + '</b></p>'
      : '<p class="fb-verdict"><b>' + (mode === "first" ? "Correct on the first try." : "Correct.") + '</b></p>';
    return '<div class="fb ' + (mode === "walk" ? "fb-walkthrough" : "fb-right") + '">' + head +
             '<p class="fb-expl">' + esc(stripCorrect(key.e)) + '</p>' +
             othersHTML(s) +
             '<p class="cs-cite">Source: ' + esc(s.cite) + '</p>' +
             '<div class="fb-actions"><button type="button" class="btn sprint" data-act="next">' +
               (last ? "See how this case went" : "Next step") + ' <kbd>Enter</kbd></button></div>' +
           '</div>';
  }

  function doneCard(i, rs) {
    var s = C.steps[i];
    var el = document.createElement("article");
    el.className = "chain-step is-done";
    el.id = "step-" + s.id;
    var badge = rs.helped ? '<span class="cs-badge is-help">Walked through</span>'
      : rs.first ? '<span class="cs-badge is-first">First try</span>'
      : '<span class="cs-badge is-later">Got it on a retry</span>';
    el.innerHTML =
      '<header class="cs-head"><span class="cs-num">Step ' + (i + 1) + '</span><span class="cs-label">' + esc(s.label) + '</span>' + badge + '</header>' +
      '<p class="cs-prompt-done">' + esc(s.prompt) + '</p>' +
      '<p class="cs-answer">' + esc(s.options[s.key].t) + '</p>' +
      '<details class="cs-more"><summary>Explanation</summary>' +
        (rs.helped ? '<ol class="fb-walk">' + s.walk.map(function (w) { return "<li>" + esc(w) + "</li>"; }).join("") + '</ol>' : "") +
        '<p class="fb-expl">' + esc(stripCorrect(s.options[s.key].e)) + '</p>' + othersHTML(s) +
        '<p class="cs-cite">Source: ' + esc(s.cite) + '</p></details>';
    return el;
  }

  function activeEl() { return document.getElementById("step-" + C.steps[cur.idx].id); }

  function saveStep(patch) {
    var rec = caseRec(C.id) || { done: false, steps: {} };
    var sid = C.steps[cur.idx].id;
    var rs = rec.steps[sid] || { tries: [] };
    for (var k in patch) rs[k] = patch[k];
    rec.steps[sid] = rs;
    writeCase(C.id, rec);
    return rs;
  }

  function pick(i) {
    if (view !== "case" || !cur || cur.phase === "resolved") return;
    var s = C.steps[cur.idx];
    if (!s || i < 0 || i > 3 || cur.tried.indexOf(i) !== -1) return;
    var el = activeEl();
    var btn = el.querySelector('[data-opt="' + i + '"]');
    bumpStreak();
    if (i === s.key) {
      var first = cur.tried.length === 0;
      btn.classList.add("correct");
      el.querySelectorAll(".chain-opt").forEach(function (b) { b.disabled = true; });
      SOUNDS.correct();
      cur.phase = "resolved";
      saveStep({ tries: cur.tried.concat([i]), first: first, helped: false, done: true });
      showResolved(first ? "first" : "retry");
      say(first ? "Correct on the first try." : "Correct.");
    } else {
      cur.tried.push(i);
      btn.classList.add("wrong");
      btn.disabled = true;
      btn.setAttribute("aria-disabled", "true");
      SOUNDS.wrong();
      cur.phase = "wrong";
      saveStep({ tries: cur.tried.slice(), first: false, helped: false, done: false });
      el.querySelector(".cs-fb").innerHTML = wrongHTML(s, i);
      say("Not quite. Try again, or ask to be walked through this step.");
      var retry = el.querySelector('[data-act="retry"]');
      if (retry) { try { retry.focus({ preventScroll: true }); } catch (e) { retry.focus(); } }
    }
  }

  function showResolved(mode) {
    var el = activeEl(), s = C.steps[cur.idx];
    var last = cur.idx === C.steps.length - 1;
    el.querySelector(".cs-fb").innerHTML = resolvedHTML(s, mode, last);
    el.classList.add(mode === "walk" ? "was-walked" : "was-right");
    var nb = el.querySelector('[data-act="next"]');
    var fb = el.querySelector(".fb");
    if (fb && fb.getBoundingClientRect().bottom > window.innerHeight) scrollToEl(fb, nb);
    else if (nb) { try { nb.focus({ preventScroll: true }); } catch (e) { nb.focus(); } }
  }

  function retry() {
    if (cur.phase !== "wrong") return;
    var el = activeEl();
    cur.phase = "ask";
    el.querySelector(".cs-fb").innerHTML = "";
    var first = el.querySelector(".chain-opt:not([disabled])");
    if (first) { try { first.focus({ preventScroll: true }); } catch (e) { first.focus(); } }
    say("Pick another answer.");
  }

  function walk() {
    if (cur.phase !== "wrong") return;
    var el = activeEl(), s = C.steps[cur.idx];
    el.querySelectorAll(".chain-opt").forEach(function (b) { b.disabled = true; });
    var kb = el.querySelector('[data-opt="' + s.key + '"]');
    if (kb) kb.classList.add("correct", "revealed");
    cur.phase = "resolved";
    saveStep({ tries: cur.tried.slice(), first: false, helped: true, done: true });
    showResolved("walk");
    say("Walk-through shown. The answer is " + s.options[s.key].t + ".");
  }

  function next() {
    if (cur.phase !== "resolved") return;
    var list = document.getElementById("chain-step-list");
    var rec = caseRec(C.id);
    var old = activeEl();
    list.replaceChild(doneCard(cur.idx, rec.steps[C.steps[cur.idx].id]), old);
    cur.idx++;
    cur.tried = [];
    cur.phase = "ask";
    if (cur.idx >= C.steps.length) { finishCase(false); return; }
    var card = activeCard(cur.idx);
    list.appendChild(card);
    updateBar();
    scrollToEl(card, card.querySelector("#qtext"));
  }

  function finishCase(silent) {
    var rec = caseRec(C.id) || { steps: {} };
    rec.done = true;
    rec.at = new Date().toISOString().slice(0, 10);
    writeCase(C.id, rec);
    cur = { idx: C.steps.length, phase: "done", tried: [] };
    updateBar();
    var f = 0, help = [], retried = [];
    C.steps.forEach(function (s) {
      var rs = rec.steps[s.id] || {};
      if (rs.first) f++;
      else if (rs.helped) help.push(s.label);
      else retried.push(s.label);
    });
    var n = C.steps.length;
    var idx = DATA.cases.indexOf(C);
    var nextC = DATA.cases[idx + 1] || null;
    var slot = document.getElementById("chain-summary-slot");
    slot.innerHTML =
      '<section class="chain-summary" id="chain-summary" tabindex="-1" aria-labelledby="chain-sum-h">' +
        '<h3 id="chain-sum-h">' + esc(C.title) + ' complete</h3>' +
        '<p class="cs-score"><b>' + f + '</b> of ' + n + ' steps right on the first try</p>' +
        '<p class="cs-sumline">' + esc(C.summary) + '</p>' +
        (help.length ? '<p class="cs-help"><b>Walked through:</b> ' + esc(help.join(", ")) + '</p>' : "") +
        (retried.length ? '<p class="cs-help"><b>Right on a retry:</b> ' + esc(retried.join(", ")) + '</p>' : "") +
        (!help.length && !retried.length ? '<p class="cs-help">No help needed on any step.</p>' : "") +
        '<div class="deck-actions">' +
          (nextC ? '<button type="button" class="btn sprint" data-act="open" data-case="' + esc(nextC.id) + '">Next case: ' + esc(nextC.title) + ' <kbd>Enter</kbd></button>'
                 : '<button type="button" class="btn sprint" data-act="home">See all cases <kbd>Enter</kbd></button>') +
          '<button type="button" class="btn ghost" data-act="replay">Replay this case</button>' +
        '</div>' +
      '</section>';
    var sum = document.getElementById("chain-summary");
    if (!silent) {
      if (f === n) { SOUNDS.win(); if (!REDUCED) burstConfetti(); }
      say(C.title + " complete: " + f + " of " + n + " steps right on the first try.");
    }
    scrollToEl(sum, sum.querySelector(".btn.sprint") || sum);
  }

  function randomCase() {
    var pool = DATA.cases.filter(function (c) { var r = caseRec(c.id); return !r || !r.done; });
    if (!pool.length) pool = DATA.cases;
    var c = pool[Math.floor(Math.random() * pool.length)];
    openCase(c.id, false);
  }

  // ================= events =================
  document.addEventListener("click", function (e) {
    var o = e.target.closest(".chain-opt");
    if (o && !o.disabled) { pick(parseInt(o.getAttribute("data-opt"), 10)); return; }
    var row = e.target.closest(".chain-case-row");
    if (row) { openCase(row.getAttribute("data-case"), false); return; }
    var b = e.target.closest("[data-act]");
    if (!b) return;
    var act = b.getAttribute("data-act");
    if (act === "retry") retry();
    else if (act === "walk") walk();
    else if (act === "next") next();
    else if (act === "home") { renderHome(); window.scrollTo(0, 0); }
    else if (act === "open") openCase(b.getAttribute("data-case"), false);
    else if (act === "replay") openCase(C.id, true);
    else if (act === "random") randomCase();
    else if (act === "reset") {
      if (window.confirm("Clear your progress for these " + DATA.cases.length + " cases?")) { clearSet(); renderHome(); }
    }
  });

  function typing(t) {
    if (!t) return false;
    var tag = (t.tagName || "").toLowerCase();
    return tag === "input" || tag === "textarea" || tag === "select" || t.isContentEditable;
  }
  function modalOpen() {
    var ov = document.getElementById("report-modal-overlay");
    return ov && ov.style.display !== "none" && ov.offsetParent !== null;
  }

  document.addEventListener("keydown", function (e) {
    if (e.ctrlKey || e.metaKey || e.altKey || typing(e.target) || modalOpen() || !DATA) return;
    var k = e.key;
    if (view !== "case" || !cur) return;
    if (cur.phase === "ask" || cur.phase === "wrong") {
      var n = "1234".indexOf(k);
      if (n === -1 && k.length === 1) n = "abcd".indexOf(k.toLowerCase());
      if (n !== -1) { e.preventDefault(); pick(n); return; }
    }
    if (cur.phase === "wrong") {
      if (k === "t" || k === "T") { e.preventDefault(); retry(); return; }
      if (k === "w" || k === "W") { e.preventDefault(); walk(); return; }
    }
    var onButton = e.target && e.target.closest && e.target.closest("button, a, summary");
    if ((k === "Enter" && !onButton) || k === "n" || k === "N") {
      if (cur.phase === "resolved") { e.preventDefault(); next(); }
      else if (cur.phase === "done") {
        var nb = document.querySelector("#chain-summary .btn.sprint");
        if (nb) { e.preventDefault(); nb.click(); }
      }
    }
  });

  window.onFCGamepadButton = function (bi) {
    if (view !== "case" || !cur) return;
    if (cur.phase === "ask" || cur.phase === "wrong") { if (bi >= 0 && bi <= 3) pick(bi); return; }
    if (cur.phase === "resolved" && (bi === 0 || bi === 9)) next();
    else if (cur.phase === "done" && (bi === 0 || bi === 9)) {
      var nb = document.querySelector("#chain-summary .btn.sprint");
      if (nb) nb.click();
    }
  };

  // ================= boot =================
  initHeader();
  if (!META) {
    app.innerHTML = '<div class="empty-state"><p>That case set was not found.</p>' +
                    '<p><a class="btn ghost" href="arcade.html">Back to the Arcade</a></p></div>';
    return;
  }
  fetch("arcade-chain/" + encodeURIComponent(META.id) + ".json?v=" + encodeURIComponent(META.ver || "1"))
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (d) {
      DATA = d;
      var want = params.get("case");
      if (want && DATA.cases.some(function (c) { return c.id === want; })) openCase(want, false);
      else renderHome();
    })
    .catch(function () {
      app.innerHTML = '<div class="empty-state"><p>The cases could not load. Check your connection and refresh.</p></div>';
    });
})();
