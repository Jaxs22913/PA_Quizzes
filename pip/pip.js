/* Pip, the study companion. Loaded by theme.js on Semester 2+ study pages (their <body>
   carries data-dark-kind) and the homepage. Never on frozen Semester 1 pages.

   The rule (Jaxon, 2026-10-08): Pip reacts to things that actually happened (an answer
   submitted, a guide opened, a pack finished). It never animates for decoration, never
   distracts during a question, and always has an easy hide control.

   So:
   - Between events Pip idles (breathing, blinks, an occasional look-around). Jaxon asked
     for the idle animations later the same day; see the idle section below for the limits.
   - On a quiz page Pip watches only what the page has ALREADY revealed: the #verdict
     line, which the quiz writes after an answer is locked in, and the results screen.
     It never reads the answer key, so it cannot hint at a correct answer early.
   - A hide button sits on Pip at all times; hidden, a small tab brings it back. The
     choice, and the "still faces only" setting, are per device ("local:" keys, which
     cloud-sync never uploads).
   - prefers-reduced-motion (or the setting): a still face for the moment, no motion.
   - Pip never takes clicks: only its two buttons do, and it slides out of the way of
     answer choices and other controls it would cover. */
(function () {
  "use strict";
  if (window.__pip) return;
  var me = document.currentScript;
  var ROOT = new URL("../", me ? me.src : location.href).href;        // site root (pip/ is one folder down)
  var ASSETS = ROOT + "immutable/pip/v1/";
  var K_HIDDEN = "local:pip:hidden", K_HIDE_QUIZ = "local:pip:hidden:quiz", K_STILL = "local:pip:still";
  var kind = (document.body && document.body.getAttribute("data-dark-kind")) || (isHome() ? "home" : null);
  if (!kind) return;

  function isHome() {
    var p = location.pathname.replace(/\/index\.html$/, "/");
    return new URL(".", ROOT).pathname === p;
  }
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) {} }
  var reducedQ = window.matchMedia ? window.matchMedia("(prefers-reduced-motion: reduce)") : null;
  function still() { return get(K_STILL) === "1" || (reducedQ && reducedQ.matches); }
  function dark() { return document.documentElement.getAttribute("data-theme") === "dark"; }

  // ------------------------------------------------------------------ dock
  var css = document.createElement("style");
  css.textContent = [
    "#pip-dock{position:fixed;right:max(4px,env(safe-area-inset-right));bottom:max(2px,env(safe-area-inset-bottom));z-index:900;",
    " pointer-events:none;transition:bottom .3s cubic-bezier(.3,1.35,.6,1),right .3s cubic-bezier(.3,1.35,.6,1)}",
    "#pip-dock.open{z-index:1901}",
    "#pip-dock.open .pip-hide{display:none}",     // the window's own "Hide Pip" button takes over while it is open
    "@media (prefers-reduced-motion:reduce){#pip-dock,#pip-dock .pip-in,#pip-dock.away .pip-in,#pip-tab,#pip-tab.away{transition:none}}",
    // the dock never moves (its box is where Pip lives); only the inner layer slides out
    "#pip-dock .pip-in{position:relative;transition:transform .35s cubic-bezier(.3,1.3,.6,1),opacity .25s,visibility 0s}",
    "#pip-dock.away .pip-in{transform:translateX(70%);opacity:0;visibility:hidden;",
    " transition:transform .35s cubic-bezier(.3,1.3,.6,1),opacity .25s,visibility 0s .35s}",
    "#pip-dock canvas{display:block;image-rendering:pixelated;image-rendering:crisp-edges}",
    "#pip-dock .pip-clawd{position:absolute;top:0;z-index:1;pointer-events:none}",   // Clawd stands to Pip's right, drawn above him
    "html[data-theme=dark] #pip-dock canvas{filter:drop-shadow(0 0 6px rgba(110,150,230,.45))}",
    "#pip-dock .pip-hide,#pip-tab{pointer-events:auto;position:absolute;border:1px solid #7d89ab;",
    " background:#fff;color:#1E3974;font:600 12px/1 system-ui,sans-serif;border-radius:999px;cursor:pointer}",
    // tapping Pip opens his window; the tap area covers his body, the × sits above it
    "#pip-dock .pip-open{pointer-events:auto;position:absolute;left:18%;top:24%;width:64%;height:72%;border:0;padding:0;background:transparent;cursor:pointer;border-radius:40%}",
    "#pip-dock .pip-open:focus-visible{outline:2px solid #6E96E6;outline-offset:2px}",
    "#pip-dock .pip-hide{z-index:2;width:22px;height:22px;padding:0;top:18%;right:10%;opacity:.85}",
    // a 44 px tap target round the small visible button
    "#pip-dock .pip-hide::after{content:'';position:absolute;inset:-11px;border-radius:50%}",
    "#pip-dock .pip-hide:hover,#pip-dock .pip-hide:focus-visible{opacity:1}",
    "#pip-tab{position:fixed;right:0;bottom:12px;z-index:900;padding:6px 8px 6px 10px;border-radius:999px 0 0 999px;",
    " border-right:0;display:flex;align-items:center;gap:6px;transition:transform .3s,opacity .2s}",
    "#pip-tab.away{transform:translateX(100%);opacity:0;visibility:hidden;transition:transform .3s,opacity .2s,visibility 0s .3s}",
    "#pip-tab img{width:16px;height:16px;image-rendering:pixelated}",
    // Jaxon 2026-10-09: "He should be easy to find but never block." When Pip tucks away from text, a slim
    // handle stays at the screen edge (inside the page gutter): one tap or Enter opens his window.
    "#pip-peek{position:fixed;right:0;bottom:84px;z-index:900;width:14px;height:58px;padding:0;border:0;border-radius:10px 0 0 10px;",
    " background:#3d63c4;cursor:pointer;box-shadow:-1px 1px 4px rgba(20,30,70,.25);display:none}",
    "#pip-peek::before{content:'';position:absolute;left:4px;top:9px;width:6px;height:6px;border-radius:50%;background:#fff;box-shadow:0 9px 0 -1px rgba(255,255,255,.75),0 17px 0 -2px rgba(255,255,255,.5)}",
    "#pip-peek::after{content:'';position:absolute;inset:-4px 0 -4px -10px}",       // a 24-px-wide tap area, still in the gutter
    "#pip-peek:focus-visible{outline:2px solid #1E3974;outline-offset:2px}",
    "html[data-theme=dark] #pip-peek{background:#6E96E6}html[data-theme=dark] #pip-peek::before{background:#0d1530;box-shadow:0 9px 0 -1px rgba(13,21,48,.75),0 17px 0 -2px rgba(13,21,48,.5)}",
    "html[data-theme=dark] #pip-dock .pip-hide,html[data-theme=dark] #pip-tab{background:#17264f;color:#E6EDFB;border-color:#6a7fb8}",
    "@media print{#pip-dock,#pip-tab,#pip-peek{display:none}}"
  ].join("\n");
  document.head.appendChild(css);

  var dock = document.createElement("div"); dock.id = "pip-dock"; dock.setAttribute("aria-hidden", "false");
  var cv = document.createElement("canvas"); cv.setAttribute("aria-hidden", "true");
  var hideBtn = document.createElement("button"); hideBtn.type = "button"; hideBtn.className = "pip-hide";
  hideBtn.setAttribute("aria-label", "Hide Pip"); hideBtn.title = "Hide Pip"; hideBtn.textContent = "×";
  var openBtn = document.createElement("button"); openBtn.type = "button"; openBtn.className = "pip-open";
  openBtn.setAttribute("aria-label", "Open Pip"); openBtn.setAttribute("aria-expanded", "false"); openBtn.title = "Talk to Pip";
  var inner = document.createElement("div"); inner.className = "pip-in";
  var cv2 = document.createElement("canvas"); cv2.className = "pip-clawd"; cv2.setAttribute("aria-hidden", "true"); cv2.style.display = "none";
  inner.appendChild(cv); inner.appendChild(cv2); inner.appendChild(openBtn); inner.appendChild(hideBtn); dock.appendChild(inner);
  var peek = document.createElement("button"); peek.type = "button"; peek.id = "pip-peek";
  peek.setAttribute("aria-label", "Open Pip"); peek.title = "Pip";
  peek.addEventListener("click", function () { if (man) withWindow(function (w) { w.open(); }); });
  var tab = document.createElement("button"); tab.type = "button"; tab.id = "pip-tab";
  tab.setAttribute("aria-label", "Show Pip"); tab.title = "Show Pip"; tab.textContent = "Pip";

  // Hiding is one tap, on every page, at any moment Pip is on screen. The × hides Pip
  // everywhere; the settings panel can also hide him on quiz pages only.
  hideBtn.addEventListener("click", function () {
    if (window.PipWindow) window.PipWindow.close(); set(K_HIDDEN, "1"); applyHidden();
    setTimeout(function () { if (!tab.classList.contains("away")) tab.focus({ preventScroll: true }); }, 0);   // keyboard users land on the way back
  });
  openBtn.addEventListener("click", function () { if (man) withWindow(function (w) { w.toggle(); }); });
  tab.addEventListener("click", function () {
    set(K_HIDDEN, null); if (kind === "quiz") set(K_HIDE_QUIZ, null); applyHidden();
    setTimeout(function () { if (!dock.classList.contains("away")) openBtn.focus({ preventScroll: true }); }, 0);
  });
  function isHidden() { return get(K_HIDDEN) === "1" || (kind === "quiz" && get(K_HIDE_QUIZ) === "1"); }
  function applyHidden() {
    var h = isHidden();
    if (h) { activeId = 0; current = null; clearTimeout(faceTimer); duetCancel(); }    // stop any animation mid-way
    dock.style.display = h ? "none" : "";
    tab.style.display = h ? "" : "none";
    if (!h) { if (man) { activeId = 0; rest(); } else draw(); }
    syncSettings(); schedule();
  }

  // ------------------------------------------------------------------ sprites
  var man = null, strips = {}, W = 112, H = 112, scale = 1, kpx = 1, cssK = 1;   // kpx: device pixels per art pixel
  function loadStrip(name) {
    if (strips[name]) return strips[name];
    var a = man && man.anims[name];
    if (!a) return Promise.resolve(null);
    strips[name] = new Promise(function (res) {
      var img = new Image(); img.decoding = "async";
      img.onload = function () { res(img); }; img.onerror = function () { res(null); };
      img.src = ASSETS + a.file;
    });
    return strips[name];
  }
  function frames(a) {                 // expanded per-tick unique-frame index list
    if (!a._f) { a._f = []; a.seq.forEach(function (s) { var n = Math.max(1, Math.round(s[1] * a.fps / 1000)); for (var i = 0; i < n; i++) a._f.push(s[0]); }); }
    return a._f;
  }
  function resize() {
    scale = window.innerWidth >= 1180 ? 2 : 1;
    // every art pixel is a whole number of DEVICE pixels, so the art stays crisp at 1.25x or 1.5x too
    var raw = window.devicePixelRatio || 1;
    kpx = Math.max(1, Math.round(scale * raw)); cssK = kpx / raw;
    [cv, cv2].forEach(function (c) {
      c.width = W * kpx; c.height = H * kpx;
      c.style.width = (W * cssK) + "px"; c.style.height = (H * cssK) + "px";
    });
    cv2.style.left = (CLAWD_DX * cssK) + "px";
    if (dock.classList.contains("duet")) dock.style.marginRight = (CLAWD_DX * cssK) + "px";
    draw(); paint(CL);
  }
  var shown = { img: null, u: 0 };               // what is on the canvas now
  var rimCache = new WeakMap();
  function rim(img) {                            // dark mode: a 1-px blue rim from the opaque pixels only
    if (rimCache.has(img)) return rimCache.get(img);
    var c = document.createElement("canvas"); c.width = img.width; c.height = img.height;
    var x = c.getContext("2d"); x.drawImage(img, 0, 0);
    var d = x.getImageData(0, 0, c.width, c.height), p = d.data;
    for (var i = 3; i < p.length; i += 4) p[i] = p[i] === 255 ? 255 : 0;
    x.putImageData(d, 0, 0); x.globalCompositeOperation = "source-in"; x.fillStyle = "#6E96E6"; x.fillRect(0, 0, c.width, c.height);
    rimCache.set(img, c); return c;
  }
  var PIP = { cv: cv, shown: shown }, CL = { cv: cv2, shown: { img: null, u: 0 } };
  function paint(t) {
    var c = t.cv, sh = t.shown, ctx = c.getContext("2d"), k = kpx;
    ctx.imageSmoothingEnabled = false; ctx.clearRect(0, 0, c.width, c.height);
    if (!sh.img) return;
    if (dark()) { var r = rim(sh.img); [[1, 0], [-1, 0], [0, 1], [0, -1]].forEach(function (o) { ctx.drawImage(r, sh.u * W, 0, W, H, o[0] * k, o[1] * k, W * k, H * k); }); }
    ctx.drawImage(sh.img, sh.u * W, 0, W, H, 0, 0, W * k, H * k);
  }
  function draw() { paint(PIP); }
  function showFrame(img, u) { shown.img = img; shown.u = u; draw(); }

  var REST = "idle", CLAWD_DX = 77;              // Clawd's frame sits 77 art px right of Pip's (ASSET_CONTRACT)
  function restFrame() {
    current = null;
    return loadStrip(REST).then(function (img) { if (img) showFrame(img, frames(man.anims[REST])[0]); });
  }

  // ------------------------------------------------------------------ idle
  // Jaxon, 2026-10-08: "I want PIP to have the idle animations." Between reactions Pip
  // breathes, blinks and now and then looks around, the way the approved motion test
  // directs him, only calmer. While a quiz question is waiting for an answer he only
  // breathes and blinks (no look-arounds to pull the eye), and after four minutes
  // without input on a non-quiz page he dozes off until the student does something.
  // He is frozen whenever he is hidden, tucked away, in a background tab, or motion is off.
  var IDLES = { idle: 1, idle_blink: 1, idle_look: 1, idle_curious: 1, sleepy: 1 };
  var current = null, lastInput = Date.now(), SLEEP_MS = 240000;
  function canIdle() {
    return !!man && !isHidden() && !still() && !document.hidden && !dock.classList.contains("away") && dock.isConnected;
  }
  function questionWaiting() {
    if (kind !== "quiz") return false;
    try {
      var st = document.getElementById("start"), res = document.getElementById("results");
      if ((st && st.style.display !== "none") || (res && res.style.display === "block")) return false;
      if (typeof answers === "undefined" || typeof idx === "undefined") return false;
      if (typeof holdFeedback === "function" && holdFeedback()) return true;
      return answers[idx] === null;
    } catch (e) { return false; }
  }
  function pickIdle() {
    var r = Math.random();
    if (questionWaiting()) return r < 0.3 ? "idle_blink" : "idle";
    if (kind !== "quiz" && Date.now() - lastInput > SLEEP_MS && man.anims.sleepy) return "sleepy";
    return r < 0.32 ? "idle_blink" : r < 0.42 ? "idle_look" : (r < 0.5 && man.anims.idle_curious) ? "idle_curious" : "idle";
  }
  function rest() {                                  // after any animation: the next idle, or the still pose
    if (canIdle()) { play(pickIdle(), 1); return Promise.resolve(); }
    return restFrame();
  }
  function idleCheck() {                             // conditions changed: start or stop the idle
    if (!man) return;
    if (canIdle()) { if (!activeId) rest(); }
    else if (!current || IDLES[current]) { activeId = 0; restFrame(); }
  }
  ["pointerdown", "keydown", "wheel", "touchstart", "scroll"].forEach(function (t) {
    window.addEventListener(t, function () {
      lastInput = Date.now();
      if (current === "sleepy") play("blink", 1);    // wakes up the moment the student is back
    }, { passive: true, capture: true });
  });
  document.addEventListener("visibilitychange", idleCheck);
  if (reducedQ && reducedQ.addEventListener) reducedQ.addEventListener("change", idleCheck);

  // ------------------------------------------------------------------ playing an animation
  var seqId = 0, activeId = 0;                       // a newer animation cancels an older one
  function play(name, loops) {
    var a = man && man.anims[name];
    if (!a) return Promise.resolve();
    var token = ++seqId; activeId = token; current = name;
    return loadStrip(name).then(function (img) {
      if (!img || token !== activeId) return;
      var f = frames(a), seq = [];
      var g = a.segments || {};
      if (g.loop) {
        var i;
        if (g["in"]) for (i = g["in"][0]; i < g["in"][1]; i++) seq.push(f[i]);
        for (var l = 0; l < (loops || 1); l++) for (i = g.loop[0]; i < g.loop[1]; i++) seq.push(f[i]);
        if (g.out) for (i = g.out[0]; i < g.out[1]; i++) seq.push(f[i]);
      } else seq = f.slice();
      return new Promise(function (done) {
        var t0 = performance.now(), ms = 1000 / a.fps, last = -1;
        function tick(now) {
          if (token !== activeId) return done();
          var i = Math.floor((now - t0) / ms);
          if (i >= seq.length) { activeId = 0; current = null; rest().then(done); return; }
          if (i !== last) { last = i; showFrame(img, seq[i]); }
          requestAnimationFrame(tick);
        }
        requestAnimationFrame(tick);
      });
    });
  }
  // ------------------------------------------------------------------ Clawd and the Superbrain duet
  // Clawd is our own pixel drawing (never copied, and never a hint that Anthropic sponsors the
  // site). He appears only while Pip is asking Claude something the student asked for:
  // Pip calls him, he inspects the passages while the answer comes, hands it back (the two
  // contact frames land on the same tick), they bump fists, he leaves and Pip waves.
  var cman = null, cstrips = {}, cTok = 0, duet = null;
  function clawdMan() {
    if (!cman) cman = fetch(ASSETS + "clawd/manifest.json").then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; });
    return cman;
  }
  function cAnim(name) {
    return clawdMan().then(function (m) {
      var a = m && m.anims[name]; if (!a) return null;
      if (!cstrips[name]) cstrips[name] = new Promise(function (res) {
        var img = new Image(); img.decoding = "async"; img.onload = function () { res(img); }; img.onerror = function () { res(null); };
        img.src = ASSETS + "clawd/" + a.file;
      });
      return cstrips[name].then(function (img) { return img ? { a: a, img: img, f: frames(a) } : null; });
    });
  }
  function runSeq(t, img, seq, fps, live) {       // play frames on a canvas; false if cut short
    return new Promise(function (done) {
      if (!seq.length) return done(true);
      var t0 = performance.now(), ms = 1000 / fps, last = -1;
      function tick(now) {
        if (!live()) return done(false);
        var i = Math.floor((now - t0) / ms);
        if (i >= seq.length) return done(true);
        if (i !== last) { last = i; t.shown.img = img; t.shown.u = seq[i]; paint(t); }
        requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    });
  }
  function cOnce(name, tok) {
    return cAnim(name).then(function (x) { return x ? runSeq(CL, x.img, x.f, x.a.fps, function () { return tok === cTok; }) : false; });
  }
  function cState(name, tok, hold) {                // in, then loop for as long as hold() says, then out
    return cAnim(name).then(function (x) {
      if (!x) return false;
      var g = x.a.segments || {}, f = x.f, live = function () { return tok === cTok; };
      function part(r) { return r ? f.slice(r[0], r[1]) : []; }
      return runSeq(CL, x.img, part(g["in"]), x.a.fps, live).then(function loop(ok) {
        if (!ok) return false;
        if (hold()) return runSeq(CL, x.img, part(g.loop), x.a.fps, live).then(loop);
        return runSeq(CL, x.img, part(g.out), x.a.fps, live);
      });
    });
  }
  function clawdOn(on) {
    cv2.style.display = on ? "" : "none";
    dock.classList.toggle("duet", on);
    dock.style.marginRight = on ? (CLAWD_DX * cssK) + "px" : "";
    if (!on) { CL.shown.img = null; paint(CL); }
  }
  function wait(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }
  function duetStart() {
    if (!man || still() || isHidden()) return false;
    var tok = ++cTok, d = { tok: tok, waiting: true };
    clawdOn(true);
    play("call_claude", 1);
    d.flow = wait(900).then(function () { return tok === cTok && cOnce("enter", tok); })
      .then(function (ok) { return ok && busy(tok, d); });
    duet = d;
    return true;
  }
  // Jaxon 2026-10-08: "Claw'd should stay until it actually has the info to give pip back."
  // While the answer is on its way Clawd keeps working: two passes over the passages, a
  // think, and again, for as long as it takes. He hands back only once the answer is in.
  function busy(tok, d) {
    function step() {
      if (tok !== cTok || !d.waiting) return Promise.resolve(true);
      var loops = 0;
      return cState("inspect_source", tok, function () { return d.waiting && ++loops <= 2; })
        .then(function (ok) { return ok && d.waiting ? cOnce("reason", tok) : ok; })
        .then(function (ok) { return ok === false ? false : step(); });
    }
    return step();
  }
  function duetFinish(ok, onHandoff) {             // onHandoff runs when the card changes hands
    var d = duet; duet = null;
    var handed = false;
    function hand() { if (!handed) { handed = true; if (onHandoff) onHandoff(); } }
    if (!d || d.tok !== cTok) { hand(); return Promise.resolve(); }
    d.waiting = false;
    return d.flow.then(function () {
      if (d.tok !== cTok) return hand();
      if (!ok) return cOnce("exit", d.tok).then(function () { if (d.tok === cTok) clawdOn(false); react("concerned", 1); hand(); });
      return Promise.all([clawdMan(), cAnim("hand_back_result")]).then(function (r) {
        var cc = (r[1] && r[1].a.events && r[1].a.events.contact) || 14;
        var pc = (man.anims.receive_claude_help && man.anims.receive_claude_help.events && man.anims.receive_claude_help.events.contact) || 12;
        var tick = 1000 / 24, gap = Math.max(0, cc - pc) * tick, pipDone;
        var clawdDone = cOnce("hand_back_result", d.tok);
        setTimeout(hand, cc * tick);
        pipDone = wait(gap).then(function () { return d.tok === cTok && play("receive_claude_help"); });
        return Promise.all([clawdDone, pipDone]);
      }).then(function () {
        if (d.tok !== cTok) return;
        play("clawd_bump");                        // both contact on tick 10: start together
        return cOnce("clawd_bump", d.tok);
      }).then(function () {
        if (d.tok !== cTok) return;
        play("wave", 1);
        return cOnce("exit", d.tok);
      }).then(function () { if (d.tok === cTok) clawdOn(false); hand(); });
    });
  }
  function duetCancel() { if (duet || dock.classList.contains("duet")) { cTok++; duet = null; clawdOn(false); } }

  // still mode: a face that says the same thing, held for a moment, then the rest pose
  var FACE = { celebrate_small: "happy", celebrate_big: "happy", proud: "proud", concerned: "concerned",
               error_recover: "effort", reviewing: "focused", wave: "happy" };
  var faceTimer = 0;
  function face(name) {
    var ex = man && man.expressions; if (!ex) return;
    var i = ex.names.indexOf(FACE[name] || "neutral"); if (i < 0) return;
    if (!strips.__ex) strips.__ex = new Promise(function (res) { var img = new Image(); img.onload = function () { res(img); }; img.onerror = function () { res(null); }; img.src = ASSETS + ex.file; });
    strips.__ex.then(function (img) {
      if (!img) return;
      activeId = 0; current = "face"; showFrame(img, i);
      clearTimeout(faceTimer); faceTimer = setTimeout(rest, 2200);
    });
  }
  function react(name, loops) {
    if (!man || isHidden()) return;
    if (dock.classList.contains("away") && !dock.classList.contains("open")) return;   // tucked away: nobody would see it
    if (still()) face(name); else play(name, loops);
  }
  // the window (pip/pip-window.js) loads on the first tap and drives Pip through this
  var winLoading = null;
  function withWindow(cb) {
    if (window.PipWindow) return cb(window.PipWindow);
    if (!winLoading) winLoading = new Promise(function (res) {
      var s = document.createElement("script"); s.src = ROOT + "pip/pip-window.js";
      s.onload = function () { res(window.PipWindow); }; s.onerror = function () { s.remove(); res(null); };
      document.head.appendChild(s);
    });
    winLoading.then(function (w) { if (w) cb(w); else winLoading = null; });   // null: the next tap tries again
  }
  function setOpen(o) {
    dock.classList.toggle("open", o); openBtn.setAttribute("aria-expanded", o ? "true" : "false");
    openBtn.setAttribute("aria-label", o ? "Close Pip's window" : "Open Pip");
    if (!o) {
      schedule();
      var a = document.activeElement;
      if (!a || a === document.body || !a.isConnected) setTimeout(function () { if (!dock.classList.contains("away")) openBtn.focus({ preventScroll: true }); }, 0);
    }
  }
  // Anonymous usage counts (metrics.js): Pip's own day documents, metrics_pip/{YYYY-MM-DD}. Counts only, never
  // what anyone typed or what Pip answered; each field's most-per-write matches firestore.rules (metrics_pip).
  if (window.PAMetrics) window.PAMetrics.family("pip", {
    coll: "metrics_pip",
    fields: { pip_open: 50, pip_ask: 200, explain_card: 200, explain_tap: 100, followup: 50, claude_ask: 50,
              practice: 50, rescue: 50, brain_yes: 10, brain_no: 10, brain_ok: 20, brain_fail: 20,
              thumb_up: 100, thumb_down: 100, fallback: 100, error: 100, pip_users_d: 1, pip_users_w: 1, pip_users_m: 1 },
    marks: { pip_users: { d: "pip_users_d", w: "pip_users_w", m: "pip_users_m" } }
  });
  window.__pip = { react: react, ROOT: ROOT, kind: kind, dock: dock, setOpen: setOpen, now: function () { return current; },
                   duet: { start: duetStart, finish: duetFinish, cancel: duetCancel, active: function () { return dock.classList.contains("duet"); } },
                   hide: function () { set(K_HIDDEN, "1"); applyHidden(); },
                   scale: function () { return cssK; }, get frameH() { return H; }, get frameW() { return W; }, clawdDX: CLAWD_DX,
                   get ground() { return (man && man.ground) || 104; } };

  // ------------------------------------------------------------------ events that actually happened
  function watchQuiz() {
    // React only when the quiz's own choose() locks in a NEW answer. The verdict line is
    // rewritten when an answered question is revisited and never cleared between questions,
    // so it alone cannot tell a new submission from a re-display.
    var v = document.getElementById("verdict");
    var orig = window.choose;
    if (v && typeof orig === "function" && !orig.__pip) {
      var writes = 0;
      if (window.MutationObserver) new MutationObserver(function () { writes++; })
        .observe(v, { attributes: true, attributeFilter: ["class"], childList: true, characterData: true, subtree: true });
      var wrapped = function () {
        var before = writes;
        var r = orig.apply(this, arguments);
        // MutationObserver callbacks run as a microtask: look once they have landed
        Promise.resolve().then(function () {
          if (writes === before) return;            // nothing revealed (exam mode defers feedback)
          if (/\bok\b/.test(v.className)) react("celebrate_small");
          else if (/\bbad\b/.test(v.className)) react("concerned", 1);
        });
        return r;
      };
      wrapped.__pip = true;
      window.choose = wrapped;
    }
    window.addEventListener("quizResultsShown", function () {
      var pct = null;
      try {
        var t = (document.getElementById("results") || {}).textContent || "";
        var m = t.match(/(\d{1,3})\s*%/); if (m) pct = +m[1];
      } catch (e) {}
      if (!isHidden()) withWindow(function (w) { w.offerRescue(); });
      setTimeout(function () {
        if (pct === null || pct >= 90) react("celebrate_big");
        else if (pct >= 70) react("proud");
        else react("error_recover");      // a "shake it off, go again" beat, never a sad one
      }, 900);
    });
  }

  // ------------------------------------------------------------------ staying out of the way
  // Anything a student reads or taps: Pip never sits on top of it (phones and narrow
  // windows, where the page runs under the corner). Checked by hit-testing a few points
  // inside Pip's body rather than measuring every element, so long guides stay cheap.
  var AVOID = "a, button, input, textarea, select, label, summary, .opt, .verdict, .settings-panel, nav.toc, " +
              "p, li, dt, dd, h1, h2, h3, h4, h5, h6, td, th, caption, img, svg, figure, pre, blockquote";
  var awayTimer = 0;
  // Text blocks count only where their LINES are (a short centred line in a full-width
  // paragraph leaves the corner free); controls and pictures count by their whole box.
  var TEXTY = /^(P|LI|DT|DD|H[1-6]|TD|TH|CAPTION|PRE|BLOCKQUOTE|LABEL|SUMMARY)$/;
  function linesHit(elm, box) {
    var rg = document.createRange(); rg.selectNodeContents(elm);
    var rs = rg.getClientRects();
    for (var i = 0; i < rs.length; i++) {
      var q = rs[i];
      if (q.width && q.left < box.r && q.right > box.l && q.top < box.b && q.bottom > box.t) return true;
    }
    return false;
  }
  function covers(r, fx, fw, fy, fh, n) {          // does anything a student reads or taps sit under this box?
    var box = { l: r.left + r.width * fx, r: r.left + r.width * (fx + fw), t: r.top + r.height * fy, b: r.top + r.height * (fy + fh) };
    var seen = [];
    for (var yi = 0; yi < n; yi++) for (var xi = 0; xi < n; xi++) {
      var all = document.elementsFromPoint(box.l + (box.r - box.l) * xi / (n - 1), box.t + (box.b - box.t) * yi / (n - 1));
      for (var j = 0; j < all.length; j++) {          // look past Pip's own buttons AND decorative overlays
        if (all[j].closest("#pip-dock, #pip-tab, #pip-win, #pip-peek")) continue;   // (a table's edge fade sits on its text)
        var m = all[j].closest(AVOID);
        if (m && seen.indexOf(m) < 0) {
          seen.push(m);
          if (!TEXTY.test(m.tagName) && !m.classList.contains("verdict")) return true;
          if (linesHit(m, box)) return true;
        }
      }
    }
    return false;
  }
  function checkOverlap() {
    if (dock.style.display === "none") {          // hidden: the small "Pip" tab gets the same courtesy
      peek.style.display = "none";
      if (tab.style.display !== "none") tab.classList.toggle("away", covers(tab.getBoundingClientRect(), 0, 1, 0, 1, 3));
      return;
    }
    if (dock.classList.contains("open")) { dock.classList.remove("away"); peek.style.display = "none"; return; }   // standing on his window
    var r = dock.getBoundingClientRect();          // the dock's own box never slides, so this does not flip-flop
    // only Pip's body matters (the frame has empty margins): its lower-middle area
    var was = dock.classList.contains("away"), now = covers(r, 0.2, 0.65, 0.3, 0.66, 6);
    dock.classList.toggle("away", now);
    if (was !== now) idleCheck();
    if (now && man) {
      peek.style.display = "block";                 // the stylesheet hides it by default
      if (covers(peek.getBoundingClientRect(), 0, 1, 0, 1, 3)) peek.style.display = "none";   // never block, even with the handle
    } else peek.style.display = "none";
  }
  function schedule() { cancelAnimationFrame(awayTimer); awayTimer = requestAnimationFrame(checkOverlap); }

  // ------------------------------------------------------------------ settings rows
  function syncSettings() {
    var a = document.getElementById("pip-set-show"), q = document.getElementById("pip-set-quiz"), b = document.getElementById("pip-set-still");
    if (a) a.checked = get(K_HIDDEN) !== "1";
    if (q) { q.checked = get(K_HIDE_QUIZ) !== "1"; q.disabled = get(K_HIDDEN) === "1"; }
    if (b) b.checked = !still();
  }
  function addSettings() {
    var panel = document.querySelector("#settings-overlay .settings-panel");
    if (!panel || document.getElementById("pip-set-show")) return;
    function row(id, label, checked, on) {
      var r = document.createElement("div"); r.className = "settings-row";
      var s = document.createElement("span"); s.textContent = label;
      var l = document.createElement("label"); l.className = "settings-switch";
      var i = document.createElement("input"); i.type = "checkbox"; i.id = id; i.checked = checked;
      var tr = document.createElement("span"); tr.className = "track"; var th = document.createElement("span"); th.className = "thumb";
      l.appendChild(i); l.appendChild(tr); l.appendChild(th);
      i.addEventListener("change", function () { on(i.checked); });
      r.appendChild(s); r.appendChild(l); panel.appendChild(r);
    }
    row("pip-set-show", "Show Pip", get(K_HIDDEN) !== "1", function (on) { set(K_HIDDEN, on ? null : "1"); applyHidden(); });
    row("pip-set-quiz", "Show Pip on quiz pages", get(K_HIDE_QUIZ) !== "1", function (on) { set(K_HIDE_QUIZ, on ? null : "1"); applyHidden(); });
    row("pip-set-still", "Pip animations", !still(), function (on) { set(K_STILL, on ? null : "1"); idleCheck(); });
    // Claude help: Pip asks for the OK the first time he wants to check with Claude; this is the off switch
    row("pip-set-claude", "Let Pip check with Claude", get("local:pip:claude:ok") === "1", function (on) {
      set("local:pip:claude:ok", on ? "1" : null); set("local:pip:claude:no", on ? null : String(Date.now()));
    });
    // Teach Pip: the student's own notes (IndexedDB on this device; pip/pip-notes.js loads
    // only when Settings is opened, and only looks: it never creates an empty database)
    var nr = document.createElement("div"); nr.className = "settings-row"; nr.id = "pip-set-notes";
    var ns = document.createElement("span"); ns.textContent = "Pip's notes";
    var nc = document.createElement("span"); nc.className = "pip-set-count"; nc.style.cssText = "opacity:.7;margin-left:6px;font-size:.92em";
    ns.appendChild(nc);
    var nd = document.createElement("button"); nd.type = "button"; nd.className = "settings-action-btn"; nd.textContent = "Delete all";
    nd.disabled = true;
    nr.appendChild(ns); nr.appendChild(nd); panel.appendChild(nr);
    var nCount = 0;
    var notesLoading = null;
    function notesMod(cb) {
      if (window.PipNotes) return cb(window.PipNotes);
      if (!notesLoading) notesLoading = new Promise(function (res) {
        var s3 = document.createElement("script"); s3.src = ROOT + "pip/pip-notes.js";
        s3.onload = function () { res(window.PipNotes || null); };
        s3.onerror = function () { notesLoading = null; res(null); };
        document.head.appendChild(s3);
      });
      notesLoading.then(function (N) { if (N) cb(N); });
    }
    function notesRow() {
      notesMod(function (N) {
        N.count().then(function (n) {
          nCount = n; nc.textContent = n ? "· " + n + (n === 1 ? " file" : " files") : "· none";
          nd.disabled = !n; nd.setAttribute("aria-label", n ? "Delete all " + n + " of Pip's notes" : "No notes to delete");
        });
      });
    }
    nd.addEventListener("click", function () {
      if (!nCount) return;
      if (!window.confirm("Delete all " + nCount + " of your notes from Pip on this device? This can't be undone.")) return;
      nd.disabled = true; nd.textContent = "Deleting…";
      notesMod(function (N) { N.removeAll().then(function () { nd.textContent = "Delete all"; notesRow(); }); });
    });
    var ov = document.getElementById("settings-overlay");
    if (ov && window.MutationObserver) new MutationObserver(function () { if (ov.classList.contains("open")) notesRow(); })
      .observe(ov, { attributes: true, attributeFilter: ["class"] });
    if (ov && ov.classList.contains("open")) notesRow();
    window.addEventListener("pip:notes", function () { if (window.PipNotes) notesRow(); });
    var bt = get("local:pip:brain");
    if (bt) {                                          // Pip's on-laptop brain: say it is there, offer to remove it
      var r = document.createElement("div"); r.className = "settings-row"; r.id = "pip-set-brain";
      var sp = document.createElement("span"); sp.textContent = "Pip's brain (on this laptop)";
      var rm = document.createElement("button"); rm.type = "button"; rm.className = "settings-btn"; rm.textContent = "Remove";
      rm.style.cssText = "border:1px solid currentColor;background:transparent;border-radius:999px;padding:4px 12px;cursor:pointer;font:inherit;color:inherit";
      rm.addEventListener("click", function () {
        rm.disabled = true; rm.textContent = "Removing…";
        var go = function () { window.PipBrain.remove().then(function () { r.remove(); }); };
        if (window.PipBrain) go(); else { var s2 = document.createElement("script"); s2.src = ROOT + "pip/pip-brain.js"; s2.onload = go; document.head.appendChild(s2); }
      });
      r.appendChild(sp); r.appendChild(rm); panel.appendChild(r);
    }
  }

  // ------------------------------------------------------------------ start
  function start() {
    document.body.appendChild(dock); document.body.appendChild(tab); document.body.appendChild(peek);
    var hidden = isHidden();
    dock.style.display = hidden ? "none" : ""; tab.style.display = hidden ? "" : "none";
    resize();
    fetch(ASSETS + "manifest.json").then(function (r) { return r.ok ? r.json() : null; }, function () { return null; }).then(function (m) {
      if (!m) { dock.remove(); tab.remove(); peek.remove(); return; }
      man = m; W = m.frame[0]; H = m.frame[1]; resize();
      return rest();
    }).then(function () {
      if (!man) return;
      if (kind === "quiz") { watchQuiz(); ["celebrate_small", "concerned"].forEach(loadStrip); }
      if (kind === "guide" || kind === "cram") setTimeout(function () { react("reviewing", 1); }, 600);   // a guide was opened
      schedule();
    }).catch(function () {});
    window.addEventListener("resize", function () { resize(); schedule(); });
    window.addEventListener("scroll", schedule, { passive: true });
    // headings and cards that slide in as you scroll land after the scroll check: look again
    document.addEventListener("transitionend", function (e) { if (!dock.contains(e.target)) schedule(); }, true);
    document.addEventListener("animationend", function (e) { if (!dock.contains(e.target)) schedule(); }, true);
    if (window.MutationObserver) {
      new MutationObserver(function () { draw(); paint(CL); }).observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
      // pages animate their own decorations many times a second: look again at most every 250 ms
      var mt = 0;
      new MutationObserver(function () { if (!mt) mt = setTimeout(function () { mt = 0; schedule(); }, 250); })
        .observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ["class", "style"] });
    }
    addSettings();
    var so = document.getElementById("settings-overlay");
    if (!so && window.MutationObserver) {
      var mo = new MutationObserver(function () { if (document.getElementById("settings-overlay")) { mo.disconnect(); addSettings(); } });
      mo.observe(document.body, { childList: true });
    }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
})();
