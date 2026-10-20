/* theme-seasonal.js -- the seasonal themes (snow, lights, New Year, Valentine, St. Patrick, PA Week, autumn
   leaves, Halloween, Thanksgiving, July 4th) and the kit they share. Split out of theme.js 2026-10-19 so pages
   do not download and parse ~70 KB that runs only inside a holiday window: theme.js decides which themes are on
   (window.__themeSeason, which also adds each running theme's body class at once so the tint never arrives
   late) and loads this file only when at least one is. Moved verbatim apart from the kit's date logic. */

/* ============================================================
   THEME KIT (2026-10-01) -- the one place the seasonal themes share their plumbing, so a new theme is
   a small config instead of a copy of the last one. window.__themeKit gives every theme:
   - WHEN: kit.on("snow") answers "is this theme running on this page?". All date windows and the
     precedence rules live in RULES / YIELDS below, nowhere else.
   - PREVIEW: ?theme=<name>[,<name>] shows just those themes on any date (sticks for the rest of the
     browser tab via sessionStorage; ?theme=off clears it). Each theme also answers to its own
     ?<name>=1 / ?<name>=0 (?halloween=1, ?paweek=1, ?lights=1 ...). kit.fresh(name) is true only
     when the flag is in THIS url, so one-shot things (welcome cards) replay on a preview click but
     not on every page of a sticky preview.
   - kit.field: a canvas of drifting particles behind the UI (repel from the cursor or a finger,
     optional spin kick, respawn, wrap, paused when the tab is hidden, reduced-motion mode).
   - kit.canvas / kit.loop / kit.pointer / kit.repel / kit.trail / kit.card / kit.shapes / kit.colors:
     the pieces kit.field and the bespoke themes are built from.
   Rules every theme keeps: behind the content or pointer-events none, no layout shift, nothing runs in
   a hidden tab, reduced motion respected, fine-pointer-only cursor effects.
   ============================================================ */
window.__themeKit = (function () {
  var kit = {}, body = document.body;
  // Which themes run, and the preview flags, are decided by window.__themeSeason in theme.js, so that
  // theme.js can skip loading this file on the ~300 days a year no theme is running.
  var S = window.__themeSeason || { on: {}, fresh: [], previewing: false };
  var on = S.on, fresh = S.fresh;
  kit.previewing = S.previewing;
  kit.on = function (n) { return !!on[n]; };
  kit.fresh = function (n) { return fresh.indexOf(n) >= 0; };
  kit.colors = function (arr) { window.__confettiColors = arr; };

  /* ----- motion preference, pointer type, tab visibility ----- */
  var rmq = window.matchMedia ? matchMedia("(prefers-reduced-motion: reduce)") : { matches: false };
  var fmq = window.matchMedia ? matchMedia("(hover: hover) and (pointer: fine)") : { matches: false };
  kit.reduced = function () { return rmq.matches; };
  kit.fine = function () { return fmq.matches; };
  var motionSubs = [], visSubs = [];
  kit.onMotion = function (fn) { motionSubs.push(fn); };
  kit.onVisible = function (fn) { visSubs.push(fn); };
  function motionChanged() { motionSubs.forEach(function (f) { f(rmq.matches); }); }
  if (rmq.addEventListener) rmq.addEventListener("change", motionChanged); else if (rmq.addListener) rmq.addListener(motionChanged);
  function visChanged() {
    body.classList.toggle("th-paused", document.hidden);            // CSS animations pause with it
    visSubs.forEach(function (f) { f(!document.hidden); });
  }
  document.addEventListener("visibilitychange", visChanged);
  window.addEventListener("pageshow", function (e) { if (e.persisted) visChanged(); });   // back/forward cache restore

  /* ----- cursor / finger position (null when it is off the window) and the standing scatter ----- */
  var ptr = { x: null, y: null }, ptrOn = false;
  kit.pointer = function () {
    if (!ptrOn) {
      ptrOn = true;
      window.addEventListener("mousemove", function (e) { ptr.x = e.clientX; ptr.y = e.clientY; });
      document.documentElement.addEventListener("mouseleave", function () { ptr.x = ptr.y = null; });     // window never gets mouseleave
      window.addEventListener("mouseout", function (e) { if (!e.relatedTarget) ptr.x = ptr.y = null; });
      window.addEventListener("touchmove", function (e) { if (e.touches.length) { ptr.x = e.touches[0].clientX; ptr.y = e.touches[0].clientY; } }, { passive: true });
      window.addEventListener("touchend", function () { ptr.x = ptr.y = null; });
    }
    return ptr;
  };
  // Pushes particle p (drawn at x,y; carries vx/vy) away from the pointer inside radius R. kick: also
  // spin it (needs p.spinSpeed). The caller decays vx/vy each frame, so p settles back by itself.
  kit.repel = function (p, x, y, R, k, kick) {
    if (ptr.x === null) return;
    var dx = x - ptr.x, dy = y - ptr.y, dist = Math.sqrt(dx * dx + dy * dy);
    if (dist < R && dist > 0.01) {
      var force = (1 - dist / R) * k;
      p.vx += (dx / dist) * force; p.vy += (dy / dist) * force;
      if (kick) {
        p.spinSpeed += (dx > 0 ? 1 : -1) * force * 0.01;
        if (p.spinSpeed > 0.12) p.spinSpeed = 0.12;
        if (p.spinSpeed < -0.12) p.spinSpeed = -0.12;
      }
    }
  };

  /* ----- a fixed canvas behind the UI, sized to the viewport ----- */
  kit.canvas = function (cls, dprCap) {
    var el = document.createElement("canvas");
    el.className = "th-cv " + cls; el.setAttribute("aria-hidden", "true");
    el.style.cssText = "position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:-1;";
    body.insertBefore(el, body.firstChild);
    var o = { el: el, ctx: el.getContext("2d"), W: 0, H: 0, onSize: null, gone: false };
    function size() {
      var dpr = Math.min(window.devicePixelRatio || 1, dprCap || 2);
      o.W = window.innerWidth; o.H = window.innerHeight;
      el.width = Math.round(o.W * dpr); el.height = Math.round(o.H * dpr);
      o.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      if (o.onSize) o.onSize();
    }
    var t = 0;
    function onResize() { clearTimeout(t); t = setTimeout(function () { if (!o.gone) size(); }, 100); }
    window.addEventListener("resize", onResize);
    o.remove = function () { o.gone = true; window.removeEventListener("resize", onResize); if (el.parentNode) el.parentNode.removeChild(el); };
    size();
    return o;
  };

  /* ----- a requestAnimationFrame loop that stops in a hidden tab (fps: optional cap) ----- */
  kit.loop = function (fn, fps) {
    var raf = 0, last = 0, want = false, gap = fps ? 1000 / fps - 2 : 0;
    function frame(now) {
      raf = requestAnimationFrame(frame);
      if (gap && now - last < gap) return;
      var dt = Math.min(0.05, (now - last) / 1000); last = now;
      fn(now, dt);
    }
    function go() { if (!raf && want && !document.hidden) { last = performance.now(); raf = requestAnimationFrame(frame); } }
    function halt() { cancelAnimationFrame(raf); raf = 0; }
    kit.onVisible(function (vis) { if (vis) go(); else halt(); });
    return { start: function () { want = true; go(); }, stop: function () { want = false; halt(); } };
  };

  /* ----- particles drifting behind the UI -----
     cfg: cls, count (number or function), make(randomY), move(p), gone(p), wrap (px margin), draw(ctx, p),
     begin(ctx) once per frame, after(ctx, still, k) once per frame after the particles, kick (spin from the cursor),
     repelR/repelK, dprCap, fps (cap), onSize(particles, W, H), rad(p) (bounding radius: redraw only the dirty rectangles) + strip() ->
     [y, height] of a band to clear as well + dirty() -> [[x, y, w, h], ...] more rectangles to clear,
     reduced: "run" (ignore the preference), "still" (one frozen frame), "off" (no canvas), first (draw a frame at once). */
  kit.field = function (cfg) {
    var cv = null, ps = [], mode = cfg.reduced || "off", R = cfg.repelR || 110, K = cfg.repelK || 1.8;
    kit.pointer();
    function frame(still, dt) {
      var ctx = cv.ctx, W = window.innerWidth, H = window.innerHeight, i, p, r;
      var k = cfg.fps && dt ? Math.max(0.5, Math.min(3, dt * 60)) : 1;      // frame-rate scale (1 at 60 fps)
      if (cfg.rad && !still) {                                   // erase only where each particle was (plus the strip, if any)
        for (i = 0; i < ps.length; i++) { p = ps[i]; if (p.bb) ctx.clearRect(p.bb[0], p.bb[1], p.bb[2], p.bb[3]); }
        if (cfg.strip) { r = cfg.strip(); ctx.clearRect(0, r[0], W, r[1]); }
        if (cfg.dirty) { r = cfg.dirty(); for (i = 0; i < r.length; i++) ctx.clearRect(r[i][0], r[i][1], r[i][2], r[i][3]); }
      } else ctx.clearRect(0, 0, W, H);
      if (cfg.begin) cfg.begin(ctx);
      for (i = 0; i < ps.length; i++) {
        p = ps[i];
        if (!still) {
          kit.repel(p, p.x, p.y, R, K * k, cfg.kick);
          var dec = k === 1 ? 0.9 : Math.pow(0.9, k);
          p.vx *= dec; p.vy *= dec;
          cfg.move(p, k);
          if (cfg.gone(p)) { ps[i] = cfg.make(false); continue; }
          if (cfg.wrap) {
            if (p.x < -cfg.wrap) p.x = window.innerWidth + cfg.wrap;
            if (p.x > window.innerWidth + cfg.wrap) p.x = -cfg.wrap;
          }
        }
        cfg.draw(ctx, p);
        if (cfg.rad) { r = cfg.rad(p) + 2; p.bb = [Math.floor(p.x - r), Math.floor(p.y - r), Math.ceil(2 * r) + 1, Math.ceil(2 * r) + 1]; }
      }
      if (cfg.after) cfg.after(ctx, still, k);
      ctx.globalAlpha = 1;
    }
    var loop = kit.loop(function (now, dt) { frame(false, dt); }, cfg.fps);
    function apply() {
      if (kit.reduced() && mode !== "run") {
        loop.stop();
        if (mode === "off") { if (cv) { cv.remove(); cv = null; } ps = []; }
        else { if (!cv) build(); frame(true); }
      } else { var fresh = !cv; if (fresh) build(); loop.start(); if (fresh && cfg.first) frame(false); }
    }
    function build() {
      cv = kit.canvas(cfg.cls, cfg.dprCap);
      cv.onSize = function () {                                                          // resizing clears a canvas: repaint the frozen frame
        if (cfg.onSize) cfg.onSize(ps, cv.W, cv.H);
        if (kit.reduced() && mode === "still") frame(true);
      };
      var n = typeof cfg.count === "function" ? cfg.count() : cfg.count;
      ps = []; for (var i = 0; i < n; i++) ps.push(cfg.make(true));
    }
    kit.onMotion(apply);
    if (window.MutationObserver) new MutationObserver(function () {                      // the site light/dark switch repaints a frozen frame
      if (cv && kit.reduced() && mode === "still") frame(true);
    }).observe(document.documentElement, { attributes: true, attributeFilter: ["data-theme"] });
    apply();
    return { particles: function () { return ps; }, canvas: function () { return cv; } };
  };

  /* ----- a pooled cursor trail (fine pointers only, never on touch, throttled) -----
     o: cls, pool, gap (ms), min (px between drops), dx/dy (offset from the pointer), ms, ease,
     frames(x, y) -> Web Animations keyframes */
  kit.trail = function (o) {
    var pool = [], idx = 0, lastX = -999, lastY = -999, lastT = 0, N = o.pool || 16;
    function el(i) {
      if (pool[i]) return pool[i];
      var d = document.createElement("div");
      d.className = o.cls; d.setAttribute("aria-hidden", "true");
      body.appendChild(d); pool[i] = d; return d;
    }
    window.addEventListener("mousemove", function (e) {
      if (kit.reduced() || !kit.fine() || document.hidden || e.buttons) return;
      var now = e.timeStamp || Date.now();
      if (now - lastT < (o.gap || 55)) return;
      var dx = e.clientX - lastX, dy = e.clientY - lastY, min = o.min || 26;
      if (dx * dx + dy * dy < min * min) return;
      lastT = now; lastX = e.clientX; lastY = e.clientY;
      var d = el(idx); idx = (idx + 1) % N;
      if (d._a) d._a.cancel();
      d._a = d.animate(o.frames(Math.round(e.clientX) + (o.dx || 0), Math.round(e.clientY) + (o.dy || 0)),
        { duration: o.ms || 950, easing: o.ease || "ease-out", fill: "backwards" });
    });
  };

  /* ----- a welcome card, once a day per device on the app-shell pages (preview: every time) -----
     o: key (localStorage), fresh (replay), cls, html, ms, burst [count, spread]. Returns the card or null. */
  kit.isShell = function () {
    var path = location.pathname.replace(/^.*\//, "");
    return body.classList.contains("homepage") || /^(|index\.html|guides\.html|calendar\.html|arcade[\w-]*\.html|group-(join|host)\.html)$/.test(path);
  };
  kit.card = function (o) {
    var seen = false;
    try { seen = !o.fresh && localStorage.getItem(o.key) === "1"; } catch (e) {}
    if (seen) return null;
    try { localStorage.setItem(o.key, "1"); } catch (e) {}
    var card = document.createElement("div");
    card.className = "pa-toast" + (o.cls ? " " + o.cls : ""); card.setAttribute("role", "status");
    card.innerHTML = o.html + '<button type="button" class="pa-toast-x" aria-label="Close">&times;</button>';
    body.appendChild(card);
    function close() { card.classList.add("out"); setTimeout(function () { card.remove(); }, 450); }
    card.querySelector(".pa-toast-x").addEventListener("click", close);
    document.addEventListener("keydown", function esc(e) { if (e.key === "Escape") { document.removeEventListener("keydown", esc); close(); } });
    setTimeout(close, o.ms || 9000);
    if (o.burst && !kit.reduced() && window.burstConfetti) setTimeout(function () { window.burstConfetti(o.burst[0], o.burst[1]); }, 350);
    return card;
  };

  /* ----- a decoration beside/behind the homepage logo (homepage only) -----
     The homepage has two logos: the big one (.brand-mark, desktop) and the small one in the h1 (phones);
     whichever is showing gets the visible copy. Returns the two spans (or null off the homepage). */
  kit.logoMark = function (cls, behind) {
    if (!body.classList.contains("homepage")) return null;
    var bigHost = document.querySelector(".brand-mark"), smallHost = document.querySelector(".page > header h1");
    function mk(host, c) {
      if (!host) return null;
      var el = document.createElement("span");
      el.className = cls + " " + cls + "-" + c; el.setAttribute("aria-hidden", "true");
      host.style.position = "relative"; if (behind) host.style.isolation = "isolate";
      host.insertBefore(el, host.firstChild); return el;
    }
    var big = mk(bigHost, "big"), small = mk(smallHost, "small");
    function which() {
      var desktop = !!(bigHost && bigHost.offsetParent !== null && bigHost.getBoundingClientRect().height > 0);
      if (big) big.classList.toggle("on", desktop); if (small) small.classList.toggle("on", !desktop);
    }
    which(); window.addEventListener("resize", which);
    return [big, small];
  };

  /* ----- outlines the themes share (path only: the caller fills or strokes) ----- */
  kit.shapes = {
    heart: function (ctx, s) {                    // classic two-lobe heart, notch on top, tip at (0, h)
      var w = s * 1.8, h = s * 1.7, top = h * 0.28, mid = (h + top) / 2;
      ctx.beginPath(); ctx.moveTo(0, top);
      ctx.bezierCurveTo(0, 0, -w / 2, 0, -w / 2, top); ctx.bezierCurveTo(-w / 2, mid, 0, mid, 0, h);
      ctx.bezierCurveTo(0, mid, w / 2, mid, w / 2, top); ctx.bezierCurveTo(w / 2, 0, 0, 0, 0, top); ctx.closePath();
    },
    leaf: function (ctx, s) {                     // pointed leaf, tip to tip along y
      ctx.beginPath(); ctx.moveTo(0, -s);
      ctx.quadraticCurveTo(s * 0.9, -s * 0.3, 0, s); ctx.quadraticCurveTo(-s * 0.9, -s * 0.3, 0, -s); ctx.closePath();
    },
    leaflet: function (ctx, s) {                  // one heart-shaped clover leaflet, tip at the origin (no beginPath)
      var w = s * 1.45, h = s * 1.1, top = h * 0.22, mid = (h + top) / 2;
      ctx.moveTo(0, top - h);
      ctx.bezierCurveTo(0, -h, -w / 2, -h, -w / 2, top - h); ctx.bezierCurveTo(-w / 2, mid - h, 0, mid - h, 0, 0);
      ctx.bezierCurveTo(0, mid - h, w / 2, mid - h, w / 2, top - h); ctx.bezierCurveTo(w / 2, -h, 0, -h, 0, top - h);
    },
    clover: function (ctx, s) {                   // four leaflets meeting at the origin
      ctx.beginPath();
      for (var i = 0; i < 4; i++) { ctx.save(); ctx.rotate(i * Math.PI / 2); kit.shapes.leaflet(ctx, s); ctx.restore(); }
      ctx.closePath();
    }
  };
  return kit;
})();

// Seasonal snowfall (added 2026-07-16, brought up to the Halloween standard 2026-10-01) -- December (Dec 1-30;
// Dec 31 is New Year's). Lives here rather than in any one page's HTML so every current page picks it up for free and
// every future page does too, as long as it includes theme.js. A canvas fixed to the viewport and pushed behind all real
// content with z-index:-1 (the same technique index.html's own .edge-decor strips use), built on __themeKit.field.
//   - The bigger flakes are six-armed crystals that spin slowly and spin away from the cursor or a finger.
//   - Flakes that reach the bottom edge settle into a thin drift (a few pixels at most) that gently melts away.
//   - Light mode draws the flakes with a faint cool outline (white on cream was nearly invisible).
//   - Quiz-completion confetti is icy blue and silver unless the holiday lights set their own. 30 fps, dirty-rect
//     redraw, canvas capped at 2x pixel density, reduced motion: one frozen frame.
(function () {
  var kit = window.__themeKit;
  if (!kit.on("snow")) return;
  document.body.classList.add("xmas-theme");
  if (!kit.on("lights")) kit.colors(["#93c5fd", "#60a5fa", "#bfdbfe", "#a5b4fc", "#cbd5e1"]);
  var windStrength = 0.35, COL = 6, MAXH = 5, heights = [], dark = false, gain = window.innerWidth < 700 ? 0.4 : 0.73;   // the drift: one height per 6px column, in px

  function landed(x) {                                            // a flake settles: bump the columns around it
    var c = Math.floor(x / COL), i, d;
    for (d = -3; d <= 3; d++) {
      i = c + d;
      if (i >= 0 && i < heights.length) heights[i] = Math.min(MAXH, heights[i] + gain * (1 - Math.abs(d) / 4));
    }
  }
  // One draw call per opacity band instead of one per flake: flakes are queued by draw() and flushed in after().
  var dots = [[], [], []], arms = [[], [], []], ALPHA = [0.65, 0.82, 0.97];
  function flush(ctx) {
    var b, i, f, a, dx, dy, r;
    for (b = 0; b < 3; b++) {
      ctx.globalAlpha = ALPHA[b];
      if (dots[b].length) {
        ctx.beginPath();
        for (i = 0; i < dots[b].length; i++) { f = dots[b][i]; ctx.moveTo(f.x + f.r, f.y); ctx.arc(f.x, f.y, f.r, 0, Math.PI * 2); }
        ctx.fill(); if (!dark) ctx.stroke();
      }
      if (arms[b].length) {                                        // six arms = three lines through the center
        ctx.beginPath();
        for (i = 0; i < arms[b].length; i++) {
          f = arms[b][i]; r = f.r * 0.9 * 1.7;
          for (a = 0; a < 3; a++) {
            dx = Math.cos(f.spin + a * Math.PI / 3) * r; dy = Math.sin(f.spin + a * Math.PI / 3) * r;
            ctx.moveTo(f.x - dx, f.y - dy); ctx.lineTo(f.x + dx, f.y + dy);
          }
        }
        ctx.stroke();
      }
      dots[b].length = 0; arms[b].length = 0;
    }
  }
  kit.field({
    cls: "th-snow", dprCap: 1.5, reduced: "still", wrap: 10, kick: true, fps: 30,
    count: window.innerWidth < 700 ? 45 : 90,                      // lighter on narrow/mobile viewports
    rad: function (f) { return f.r * 1.9 + 2; },
    strip: function () { return [window.innerHeight - MAXH - 4, MAXH + 5]; },
    make: function (randomY) {
      var r = 1.7 + Math.random() * 3.4;
      return {
        x: Math.random() * window.innerWidth,
        y: randomY ? Math.random() * window.innerHeight : -10 - Math.random() * 40,
        r: r, speed: 0.5 + r * 0.45 + Math.random() * 0.4,
        drift: Math.random() * Math.PI * 2, driftSpeed: 0.005 + Math.random() * 0.01,
        spin: Math.random() * Math.PI, spinSpeed: (Math.random() - 0.5) * 0.03,
        opacity: 0.6 + Math.random() * 0.4, vx: 0, vy: 0
      };
    },
    move: function (f, k) {
      f.y += (f.speed + f.vy) * k; f.drift += f.driftSpeed * k; f.x += (Math.sin(f.drift) * (windStrength * 1.6) + f.vx) * k;
      f.spin += f.spinSpeed * k;
    },
    gone: function (f) {
      var H = window.innerHeight;
      if (f.y > H + 10) return true;
      var h = heights[Math.floor(f.x / COL)] || 0;
      if (f.r > 2.2 && f.y > H - h - f.r - 3 && Math.random() < 0.6) { landed(f.x); return true; }   // lands on the drift
      return false;
    },
    begin: function (ctx) {
      var n = Math.ceil(window.innerWidth / COL) + 2;
      if (heights.length !== n) { heights.length = 0; for (var i = 0; i < n; i++) heights.push(0); }
      dark = document.documentElement.getAttribute("data-theme") === "dark";
      ctx.fillStyle = dark ? "#ffffff" : "#f4f8fd";
      ctx.strokeStyle = dark ? "#ffffff" : "rgba(110, 140, 185, .75)"; ctx.lineWidth = dark ? 1 : 0.9; ctx.lineCap = "round";
    },
    draw: function (ctx, f) { (f.r > 3.4 ? arms : dots)[f.opacity < 0.75 ? 0 : (f.opacity < 0.9 ? 1 : 2)].push(f); },
    after: function (ctx, still, k) {
      flush(ctx);
      var H = window.innerHeight, W = window.innerWidth, i, any = false;
      for (i = 0; i < heights.length; i++) {
        if (!still) heights[i] = Math.max(0, heights[i] - (0.0008 * heights[i] + 0.0004) * (k || 1));   // melts: proportional + a little constant
        if (heights[i] > 0.15) any = true;
      }
      if (!any) return;
      ctx.beginPath(); ctx.moveTo(0, H);
      for (i = 0; i < heights.length; i++) ctx.lineTo(i * COL + COL / 2, H - heights[i]);
      ctx.lineTo(W, H); ctx.closePath();
      ctx.globalAlpha = 0.92; ctx.fillStyle = dark ? "#ffffff" : "#f4f8fd"; ctx.fill();
      ctx.globalAlpha = 1; ctx.strokeStyle = dark ? "rgba(255,255,255,0)" : "rgba(110, 140, 185, .6)"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(0, H - heights[0]);
      for (i = 1; i < heights.length; i++) ctx.lineTo(i * COL + COL / 2, H - heights[i]);
      ctx.stroke();
    }
  });
})();

/* ============================================================
   HOLIDAY LIGHTS (2026-10-01) -- Dec 1-25 (local date, every year), or ?theme=lights to preview.
   A string of bulbs hanging along the top of the page, blinking in a slow wave that travels along it and
   swaying a little. It runs alongside the December snow (which keeps going to Dec 30).
   - Pure CSS animation, no canvas, no JS loop. Bulbs are dealt into 10 wrappers (bulb 1, 11, 21 ... share
     one), each wrapper twinkles (opacity) and sways (a few px sideways) on its own phase, so consecutive
     bulbs are out of step and the blink travels along the string. Ten animations instead of eighty is what
     keeps the main-thread cost (measured) inside the Halloween budget.
   - It hangs from the TOP OF THE DOCUMENT (position:absolute), not the viewport, so it scrolls away with
     the page and never sits over text you are reading. z-index 1: every positioned bar, button, tab strip,
     toast and dialog (z-index 2 and up) paints over it, and it is pointer-events:none, so nothing it
     overlaps can be blocked or hidden. On the guides and reference pages, where the sticky back bar is the first thing
     on the page, it hangs from the bottom edge of that bar instead of behind it.
   - Rebuilt (debounced) on resize; hidden while printing; reduced motion: the bulbs stay lit and still.
   The December cream tint comes from body.xmas-theme, which this also sets.
   ============================================================ */
(function () {
  var kit = window.__themeKit;
  if (!kit.on("lights")) return;
  var body = document.body;
  body.classList.add("lights-theme", "xmas-theme");
  kit.colors(["#dc2626", "#16a34a", "#f59e0b", "#2563eb", "#ec4899"]);

  var COLORS = ["#ef4444", "#f59e0b", "#22c55e", "#3b82f6", "#ec4899"];
  var host = document.createElement("div");
  host.className = "th-lights"; host.setAttribute("aria-hidden", "true");
  body.appendChild(host);
  function firstInFlow(el) {                                  // nothing visible comes before it in the page flow
    for (var e = el; e && e !== body; e = e.parentElement) {
      for (var p = e.previousElementSibling; p; p = p.previousElementSibling) {
        var pos = getComputedStyle(p).position;
        if (p.offsetHeight > 0 && pos !== "fixed" && pos !== "absolute") return false;
      }
    }
    return true;
  }
  function place() {                                          // below the sticky back bar where a page has one
    var bar = document.querySelector(".guide-back-bar");        // (its offsetTop is its stuck position once scrolled, so ask about the flow instead)
    host.style.top = (bar && firstInFlow(bar) ? bar.offsetHeight : 0) + "px";
  }

  function build() {
    var W = window.innerWidth, narrow = W < 700;
    var swags = Math.max(2, Math.round(W / (narrow ? 130 : 200))), sw = W / swags, sag = narrow ? 7 : 10;
    var gap = narrow ? 30 : 36, n = Math.max(6, Math.floor(W / gap)), step = W / n;
    var d = "M0 2", i, html = "";
    for (i = 0; i < swags; i++) d += " Q" + ((i + 0.5) * sw).toFixed(1) + " " + (2 + 2 * sag) + " " + ((i + 1) * sw).toFixed(1) + " 2";
    html = '<svg class="th-wire" width="' + W + '" height="' + (sag + 6) + '" viewBox="0 0 ' + W + " " + (sag + 6) + '"><path d="' + d + '"/></svg>';
    var G = 10, groups = [];                                    // bulbs i, i+G, i+2G ... share one wrapper (and one animation)
    for (i = 0; i < G; i++) groups.push("");
    for (i = 0; i < n; i++) {
      var x = (i + 0.5) * step, k = Math.min(swags - 1, Math.floor(x / sw)), t = (x - k * sw) / sw;
      var y = 2 + 4 * sag * t * (1 - t);
      groups[i % G] += '<i class="th-bulb" style="left:' + x.toFixed(1) + "px;top:" + y.toFixed(1) + "px;--c:" + COLORS[i % COLORS.length] + '"></i>';
    }
    for (i = 0; i < G; i++) html += '<div class="th-grp" style="--d:' + (-(i * 0.34)).toFixed(2) + 's">' + groups[i] + "</div>";
    host.innerHTML = html;
    place();
  }
  build();
  var t = 0, lastW = window.innerWidth;
  window.addEventListener("resize", function () {                // height-only changes (a phone's URL bar) rebuild nothing
    clearTimeout(t);
    t = setTimeout(function () { if (window.innerWidth !== lastW) { lastW = window.innerWidth; build(); } else place(); }, 150);
  });
})();


/* ============================================================
   FIREWORKS ENGINE (2026-10-01) -- shared by the New Year's and July 4 themes: quiet bursts in the
   corners and along the edges, behind the UI. A rocket rises from the bottom edge, bursts into a ring
   of sparks that drift down and fade. At most 2-3 bursts at once, 30 frames a second, one canvas behind
   the UI, redrawn only where something moved, stopped in a hidden tab, none under reduced motion.
   kit.fireworks({ cls, palettes: function (dark) -> [[color, ...], ...], white: "colors that need an
   outline on a light page" }). A palette is one burst's colors.
   ============================================================ */
window.__themeKit.fireworks = function (cfg) {
  var kit = window.__themeKit, cv = null, ctx = null, shows = [], dirty = [], next = 0, clock = 0;
  var loop = kit.loop(function (now, dt) {
    var W = cv.W, H = cv.H, dark = document.documentElement.getAttribute("data-theme") === "dark", i, j;
    for (i = 0; i < dirty.length; i++) ctx.clearRect(dirty[i][0], dirty[i][1], dirty[i][2], dirty[i][3]);
    dirty.length = 0;
    clock += dt;
    var narrow = W < 700;
    if (clock >= next && shows.length < (narrow ? 2 : 3)) {
      var band = narrow ? 0.5 : 0.26, left = Math.random() < 0.5;       // wide screens: the outer quarters only
      var x = narrow ? W * (0.1 + Math.random() * 0.8) : (left ? W * (0.03 + Math.random() * band * 0.85) : W * (1 - 0.03 - Math.random() * band * 0.85));
      var pals = cfg.palettes(dark);
      shows.push({ x: x, by: H * (0.1 + Math.random() * 0.4), y: H + 8, rise: 0, pal: pals[(Math.random() * pals.length) | 0],
        parts: null, age: 0, scale: narrow ? 0.7 : 1 });
      next = clock + 1.1 + Math.random() * 1.8;
    }
    for (i = shows.length - 1; i >= 0; i--) {
      var s = shows[i], x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
      if (!s.parts) {                                                    // rocket on its way up
        s.rise += dt / 0.6; var e = 1 - Math.pow(1 - Math.min(1, s.rise), 2), ny = H + 8 + (s.by - H - 8) * e;
        var rc = s.pal[0]; if (cfg.white && cfg.white.indexOf(rc) >= 0 && !dark) rc = s.pal[1] || rc;      // a white rocket would vanish on a light page
        ctx.globalAlpha = 0.85; ctx.strokeStyle = rc; ctx.lineWidth = 1.8; ctx.lineCap = "round";
        ctx.beginPath(); ctx.moveTo(s.x, ny + 22); ctx.lineTo(s.x, ny); ctx.stroke();
        dirty.push([Math.floor(s.x - 4), Math.floor(ny - 4), 9, 30]);
        if (s.rise >= 1) {                                               // burst
          var n = 36 + ((Math.random() * 18) | 0), sp0 = (190 + Math.random() * 110) * s.scale;
          s.parts = [];
          for (j = 0; j < n; j++) {
            var a = (j / n) * Math.PI * 2 + Math.random() * 0.2, v = sp0 * (0.55 + Math.random() * 0.45);
            s.parts.push({ x: s.x, y: s.by, vx: Math.cos(a) * v, vy: Math.sin(a) * v, c: s.pal[j % s.pal.length], k: (Math.random() * 9) | 0 });
          }
          s.life = 1.7 + Math.random() * 0.6;
        }
        continue;
      }
      s.age += dt;
      if (s.age >= s.life) { shows.splice(i, 1); continue; }
      var f = s.age / s.life, alpha = (f < 0.12 ? f / 0.12 : 1 - (f - 0.12) / 0.88) * (dark ? 0.95 : 0.85);
      var drag = Math.pow(0.968, dt * 60), fall = 28 * dt, byColor = {}, p, key;
      for (j = 0; j < s.parts.length; j++) {
        p = s.parts[j];
        p.vx *= drag; p.vy = p.vy * drag + fall; p.x += p.vx * dt; p.y += p.vy * dt;
        if (f > 0.5 && ((j + (s.age * 9 | 0) * 3 + p.k) % 5) === 0) continue;       // late sparks twinkle out
        (byColor[p.c] || (byColor[p.c] = [])).push(p);
        if (p.x < x0) x0 = p.x; if (p.x > x1) x1 = p.x; if (p.y < y0) y0 = p.y; if (p.y > y1) y1 = p.y;
      }
      ctx.lineCap = "round";
      for (key in byColor) {
        var arr = byColor[key], white = cfg.white && cfg.white.indexOf(key) >= 0 && !dark;
        if (white) {                                                       // white spark on a light page: a blue halo first
          ctx.globalAlpha = alpha * 0.5; ctx.strokeStyle = "#1e40af"; ctx.lineWidth = 3.6; ctx.beginPath();
          for (j = 0; j < arr.length; j++) { ctx.moveTo(arr[j].x - arr[j].vx * 0.045, arr[j].y - arr[j].vy * 0.045); ctx.lineTo(arr[j].x, arr[j].y); }
          ctx.stroke();
        }
        ctx.globalAlpha = alpha; ctx.strokeStyle = key; ctx.lineWidth = white ? 2 : 2.4; ctx.beginPath();
        for (j = 0; j < arr.length; j++) { ctx.moveTo(arr[j].x - arr[j].vx * 0.045, arr[j].y - arr[j].vy * 0.045); ctx.lineTo(arr[j].x, arr[j].y); }
        ctx.stroke();
      }
      if (x1 > x0) dirty.push([Math.floor(x0 - 18), Math.floor(y0 - 18), Math.ceil(x1 - x0 + 36), Math.ceil(y1 - y0 + 36)]);
    }
    ctx.globalAlpha = 1;
  }, 30);
  function apply() {
    if (kit.reduced()) { loop.stop(); if (cv) { cv.remove(); cv = ctx = null; } shows = []; dirty = []; return; }
    if (!cv) { cv = kit.canvas(cfg.cls, 2); ctx = cv.ctx; cv.onSize = function () { dirty = [[0, 0, cv.W, cv.H]]; }; next = 0.5; clock = 0; }
    loop.start();
  }
  kit.onMotion(apply);
  apply();
};

/* ============================================================
   NEW YEAR'S (2026-10-01) -- Dec 31, Jan 1 and Jan 2 (local date, every year), or ?theme=newyear.
   Takes precedence over the December snow and lights on Dec 31. Quiet gold and silver fireworks in the
   corners and edges behind the UI (kit.fireworks), a champagne light-mode tint (body.newyear-theme),
   gold and silver quiz confetti, and a one-time-per-day splash card with the year that is about to
   begin (Dec 31 shows next year's number; Jan 1-2 the current one) on the app-shell pages.
   ============================================================ */
(function () {
  var kit = window.__themeKit;
  if (!kit.on("newyear")) return;
  document.body.classList.add("newyear-theme");
  kit.colors(["#d4a017", "#f0c040", "#b8c0cc", "#94a3b8", "#e5b73b"]);
  kit.fireworks({
    cls: "th-newyear",
    palettes: function (dark) {
      return dark ? [["#fbbf24", "#fde68a"], ["#e2e8f0", "#cbd5e1"], ["#fcd34d", "#e2e8f0"]]
                  : [["#b8860b", "#d4a017"], ["#64748b", "#94a3b8"], ["#c28a00", "#64748b"]];
    }
  });
  if (!kit.isShell()) return;
  var now = new Date(), year = now.getMonth() >= 6 ? now.getFullYear() + 1 : now.getFullYear();
  var card = kit.card({
    key: "themeCard:newyear:" + now.getFullYear() + "-" + (now.getMonth() + 1) + "-" + now.getDate(), fresh: kit.fresh("newyear"),
    cls: "th-card-ny", burst: [70, 1.2],
    html: '<div class="th-ny-year"></div><div class="pa-toast-txt"><b>Happy New Year!</b><span>Class of 2028: another year closer.</span></div>'
  });
  if (card) card.querySelector(".th-ny-year").textContent = String(year);
})();

/* ============================================================
   FIREWORKS / JULY 4 (2026-10-01) -- Jul 3, 4 and 5 (local date, every year), or ?theme=fireworks.
   The same quiet fireworks as New Year's (kit.fireworks) in red, white and blue behind the UI, a pale
   blue light-mode tint (body.fireworks-theme), patriotic quiz confetti, and a small "Happy 4th" card
   once a day on the app-shell pages.
   ============================================================ */
(function () {
  var kit = window.__themeKit;
  if (!kit.on("fireworks")) return;
  document.body.classList.add("fireworks-theme");
  kit.colors(["#dc2626", "#2563eb", "#1e40af", "#ef4444", "#3b82f6"]);
  kit.fireworks({
    cls: "th-fireworks", white: ["#ffffff"],
    palettes: function (dark) {
      return dark ? [["#f87171", "#ef4444"], ["#60a5fa", "#3b82f6"], ["#ffffff", "#e2e8f0"], ["#f87171", "#ffffff", "#60a5fa"]]
                  : [["#dc2626", "#ef4444"], ["#2563eb", "#3b82f6"], ["#dc2626", "#ffffff", "#2563eb"], ["#ffffff", "#2563eb"]];
    }
  });
  if (!kit.isShell()) return;
  var now = new Date();
  kit.card({
    key: "themeCard:fireworks:" + now.getFullYear() + "-" + (now.getMonth() + 1) + "-" + now.getDate(), fresh: kit.fresh("fireworks"),
    cls: "th-card-4th", burst: [60, 1.2],
    html: '<div class="pa-toast-txt"><b>Happy 4th of July!</b><span>Enjoy the fireworks, then back to the books.</span></div>'
  });
})();

// Seasonal Valentine's theme (added 2026-07-17, brought up to the Halloween standard 2026-10-01) -- Jan 31 - Feb 14.
// Floating hearts behind all UI, plus the light-mode pink tint on the app-shell pages (body.vday-theme).
//   - A heart pops in a tiny sparkle when the cursor lands right on it or it is clicked/tapped (another floats up
//     from the bottom to replace it); the standing scatter-from-the-cursor still applies around it.
//   - On the homepage the logo gets a soft heartbeat glow behind it (CSS only, lub-dub then a rest).
//   - Pink quiz-completion confetti. 30 fps, dirty-rect redraw, canvas capped at 2x, reduced motion: one still frame.
(function () {
  var kit = window.__themeKit;
  if (!kit.on("hearts")) return;
  document.body.classList.add("vday-theme");
  var COLORS = ["#ec4899", "#f472b6", "#f43f5e", "#fb7185", "#e11d48"], speedMul = 0.35;
  kit.colors(["#ec4899", "#f472b6", "#f43f5e", "#fb7185", "#e11d48"]);
  var ptr = kit.pointer(), sparks = [], rects = [], F = null;
  function pop(h) {                                              // a heart bursts into a few sparks
    h.dead = true;
    for (var i = 0; i < 9; i++) {
      var a = (i / 9) * Math.PI * 2 + Math.random() * 0.5, v = 1.1 + Math.random() * 1.5;
      sparks.push({ x: h.x, y: h.y + h.s * 0.7, vx: Math.cos(a) * v, vy: Math.sin(a) * v - 0.3, life: 0, max: 0.55 + Math.random() * 0.3,
        r: 1.2 + Math.random() * 1.5, c: i % 3 === 0 ? "#fde68a" : (i % 3 === 1 ? "#ffffff" : h.color) });
    }
  }
  window.addEventListener("click", function (e) {                // a click or tap on a heart pops it (the click still goes to the page)
    if (!F || kit.reduced()) return;
    var ps = F.particles(), best = null, bd = 1e9;
    for (var i = 0; i < ps.length; i++) {
      var h = ps[i], dx = e.clientX - h.x, dy = e.clientY - (h.y + h.s * 0.7), d = dx * dx + dy * dy, R = h.s * 1.3 + 10;
      if (d < R * R && d < bd && !h.dead) { best = h; bd = d; }
    }
    if (best) pop(best);
  });
  F = kit.field({
    cls: "th-hearts", dprCap: 1.5, reduced: "still", wrap: 20, fps: 30,
    count: window.innerWidth < 700 ? 18 : 34,
    rad: function (h) { return h.s * 1.9 + 3; },
    dirty: function () { return rects; },
    make: function (randomY) {
      var s = 6 + Math.random() * 9;
      return {
        x: Math.random() * window.innerWidth,
        y: randomY ? Math.random() * window.innerHeight : window.innerHeight + 10 + Math.random() * 40,
        s: s, speed: (0.35 + s * 0.045) * speedMul,
        drift: Math.random() * Math.PI * 2, driftSpeed: 0.006 + Math.random() * 0.012,
        opacity: 0.35 + Math.random() * 0.4, color: COLORS[(Math.random() * COLORS.length) | 0], vx: 0, vy: 0, dead: false
      };
    },
    move: function (h, k) {
      h.y -= h.speed * k; h.y += h.vy * k; h.drift += h.driftSpeed * k; h.x += (Math.sin(h.drift) * 0.6 + h.vx) * k;
      if (ptr.x !== null && kit.fine()) {                          // the cursor lands right on it
        var dx = ptr.x - h.x, dy = ptr.y - (h.y + h.s * 0.7), R = h.s * 0.9 + 5;
        if (dx * dx + dy * dy < R * R) pop(h);
      }
    },
    gone: function (h) { return h.dead || h.y < -20; },
    draw: function (ctx, h) {
      ctx.save(); ctx.translate(h.x, h.y); ctx.rotate(Math.sin(h.drift) * 0.25);
      ctx.globalAlpha = h.opacity; ctx.fillStyle = h.color;
      kit.shapes.heart(ctx, h.s); ctx.fill(); ctx.restore();
    },
    after: function (ctx, still, k) {
      rects = [];
      if (still) { sparks.length = 0; return; }                    // reduced motion switched on mid-pop: no frozen sparks
      if (!sparks.length) return;
      var dt = (k || 1) / 60;
      for (var i = sparks.length - 1; i >= 0; i--) {
        var p = sparks[i]; p.life += dt;
        if (p.life >= p.max) { sparks.splice(i, 1); continue; }
        p.x += p.vx * (k || 1); p.y += p.vy * (k || 1); p.vy += 0.03 * (k || 1);
        ctx.globalAlpha = 1 - p.life / p.max; ctx.fillStyle = p.c;
        ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fill();
        rects.push([Math.floor(p.x - p.r - 2), Math.floor(p.y - p.r - 2), Math.ceil(p.r * 2 + 5), Math.ceil(p.r * 2 + 5)]);
      }
      ctx.globalAlpha = 1;
    }
  });
  kit.logoMark("vd-beat", true);
})();

// Seasonal Fall theme (added 2026-07-17, brought up to the Halloween standard 2026-10-01) -- Oct 17-23
// (Oct 24-31 is Halloween, which takes over; see __themeKit YIELDS). Autumn leaves behind all UI, plus the
// warm light-mode tint (body.fall-theme).
//   - Leaves rock side to side like a pendulum as they fall and flip over (a squashed width), instead of
//     spinning flat; the cursor or a finger still scatters and spins them.
//   - Leaves that reach the bottom edge can land and lie there (a loose litter along the edge, never more than
//     half of them), fade out after 20-30 seconds, and fly up again if the cursor sweeps through.
//   - Quiz-completion confetti in autumn colors. 30 fps, dirty-rect redraw, reduced motion: one still frame.
(function () {
  var kit = window.__themeKit;
  if (!kit.on("leaves")) return;
  document.body.classList.add("fall-theme");
  kit.colors(["#ea580c", "#c2410c", "#ca8a04", "#991b1b", "#b45309"]);
  var COLORS = ["#ea580c", "#c2410c", "#ca8a04", "#a16207", "#991b1b", "#b45309"], speedMul = 0.35;
  var N = window.innerWidth < 700 ? 18 : 34, MAXPILE = Math.round(N * 0.5), resting = 0, F = null;
  F = kit.field({
    cls: "th-leaves", dprCap: 1.5, reduced: "still", wrap: 20, kick: true, fps: 30, count: N,
    rad: function (l) { return l.s * 2.2; },
    onSize: function (ps, W, H) {                                  // the window grew or shrank: lying leaves go back on the new bottom edge
      for (var i = 0; i < ps.length; i++) if (ps[i].rest) ps[i].y = H - ps[i].s * 0.45 - Math.random() * 3;
    },
    make: function (randomY) {
      var s = 5 + Math.random() * 7;
      return {
        x: Math.random() * window.innerWidth,
        y: randomY ? Math.random() * window.innerHeight : -10 - Math.random() * 40,
        s: s, speed: (0.3 + s * 0.05) * speedMul,
        drift: Math.random() * Math.PI * 2, driftSpeed: 0.008 + Math.random() * 0.014,
        spin: Math.random() * Math.PI * 2, spinSpeed: (Math.random() - 0.5) * 0.016,
        flip: Math.random() * Math.PI * 2, flipSpeed: 0.03 + Math.random() * 0.05,
        rest: false, restT: 0, restMax: 20 + Math.random() * 10,
        opacity: 0.5 + Math.random() * 0.4, color: COLORS[(Math.random() * COLORS.length) | 0], vx: 0, vy: 0
      };
    },
    move: function (l, k) {
      if (l.rest) {
        if (Math.abs(l.vx) + Math.abs(l.vy) > 0.9) { l.rest = false; l.vy = -(1.6 + Math.random() * 1.6); l.restT = 0; }   // the cursor swept it up
        else { l.restT += k / 60; l.vx = l.vy = 0; return; }
      }
      l.y += (l.speed + l.vy) * k; l.drift += l.driftSpeed * k; l.spin += l.spinSpeed * k; l.flip += l.flipSpeed * k;
      l.x += (Math.sin(l.drift) * 1.1 + l.vx) * k;
    },
    gone: function (l) {
      var H = window.innerHeight;
      if (l.rest) return l.restT > l.restMax;
      if (l.y > H - l.s * 0.5 && resting < MAXPILE && Math.random() < 0.8) {     // lands on the edge
        l.rest = true; l.restT = 0; l.vx = l.vy = 0; l.y = H - l.s * 0.45 - Math.random() * 3; return false;
      }
      return l.y > H + 20;
    },
    begin: function () { if (!F) return; resting = 0; var ps = F.particles(); for (var i = 0; i < ps.length; i++) if (ps[i].rest) resting++; },
    draw: function (ctx, l) {
      ctx.save(); ctx.translate(l.x, l.y);
      var a = l.opacity;
      if (l.rest) {
        ctx.rotate(l.spin); ctx.scale(1, 0.42);                                  // lying flat
        a = Math.min(l.opacity + 0.1, 0.85) * Math.min(1, (l.restMax - l.restT) / 3);
      } else {
        ctx.rotate(Math.cos(l.drift) * 0.7 + l.spin * 0.35);                     // rocks into each swing
        ctx.scale(Math.max(0.18, Math.abs(Math.cos(l.flip))), 1);              // tumbles over
      }
      ctx.globalAlpha = a; ctx.fillStyle = l.color;
      kit.shapes.leaf(ctx, l.s); ctx.fill(); ctx.restore();
    }
  });
})();

/* ============================================================
   HALLOWEEN (2026-10-01) -- Oct 24-31 inclusive (local date), or ?theme=halloween / ?halloween=1 to
   preview (__themeKit; the autumn leaves yield to it).
   Three things, each cheap and each behind the content, none touching layout:
   1. A few bats flapping across the sky (one canvas behind the UI, dirty-rect redraw, cursor/finger
      scatters them like the other particle themes, stops when the tab is hidden).
   2. Two candle glows in opposite corners that flicker (CSS opacity/transform only).
   3. A pumpkin trail behind a mouse pointer (fine-pointer devices only, 16 pooled elements, Web
      Animations, throttled; never on touch).
   body.halloween-theme tints the app-shell pages in light mode (theme.css, arcade.css, guides.html,
   group-join.html, group-host.html). prefers-reduced-motion: no bats, no trail, glows hold still.
   ============================================================ */
(function () {
  var kit = window.__themeKit;
  if (!kit.on("halloween")) return;
  var body = document.body;
  body.classList.add("halloween-theme");
  kit.colors(["#f97316", "#7c3aed", "#22c55e", "#facc15", "#ea580c"]);

  /* ---------- 2. candle glows (CSS does the flicker) ---------- */
  ["a", "b"].forEach(function (k) {
    var g = document.createElement("div");
    g.className = "hw-glow hw-glow-" + k; g.setAttribute("aria-hidden", "true");
    body.insertBefore(g, body.firstChild);
  });

  /* ---------- 1. bats ---------- */
  var cv = null, ctx = null, W = 0, H = 0, bats = [];
  var ptr = kit.pointer(), REPEL = 120;
  var nBats = window.innerWidth < 700 ? 4 : 7;

  function makeBat(first) {
    var s = 11 + Math.random() * 11;                       // half wingspan in px
    var dir = Math.random() < 0.5 ? 1 : -1;
    return {
      s: s, dir: dir, speed: 38 + Math.random() * 46,
      x: first ? Math.random() * W : (dir > 0 ? -40 - s * 2 : W + 40 + s * 2),
      baseY: H * (0.06 + Math.random() * 0.7), bobA: 10 + Math.random() * 26, bobF: 0.5 + Math.random() * 0.8,
      t: Math.random() * 20, flap: Math.random() * 6, flapF: 5.5 + Math.random() * 3,
      wait: first ? 0 : 1 + Math.random() * 6, a: 0.55 + Math.random() * 0.25,
      ox: 0, oy: 0, vx: 0, vy: 0, bb: null, y: 0
    };
  }
  function onSize() { W = cv.W; H = cv.H; for (var i = 0; i < bats.length; i++) bats[i].bb = null; }

  // front-facing bat silhouette: body, head with ears, two scalloped wings (flap = -1..1 lifts the tips)
  function drawBat(b, color) {
    var s = b.s, f = Math.sin(b.flap), tip = -f * s * 0.75;
    ctx.save();
    ctx.translate(b.x + b.ox, b.y + b.oy);
    ctx.rotate(Math.max(-0.35, Math.min(0.35, (b.vyDraw || 0) * 0.004)));
    ctx.globalAlpha = b.a; ctx.fillStyle = color;
    for (var side = -1; side <= 1; side += 2) {
      ctx.save(); ctx.scale(side, 1);
      ctx.beginPath();
      ctx.moveTo(s * 0.1, -s * 0.12);
      ctx.quadraticCurveTo(s * 0.5, -s * 0.45 + tip * 0.45, s, tip);                     // leading edge to the tip
      ctx.quadraticCurveTo(s * 0.86, tip * 0.7 + s * 0.2, s * 0.68, tip * 0.5 + s * 0.3);  // scallops back
      ctx.quadraticCurveTo(s * 0.58, tip * 0.4 + s * 0.12, s * 0.45, tip * 0.3 + s * 0.36);
      ctx.quadraticCurveTo(s * 0.3, tip * 0.15 + s * 0.16, s * 0.12, s * 0.3);
      ctx.closePath(); ctx.fill();
      ctx.restore();
    }
    ctx.beginPath(); ctx.ellipse(0, s * 0.02, s * 0.17, s * 0.3, 0, 0, Math.PI * 2); ctx.fill();   // body
    ctx.beginPath(); ctx.arc(0, -s * 0.3, s * 0.15, 0, Math.PI * 2); ctx.fill();                  // head
    ctx.beginPath();                                                                               // ears
    ctx.moveTo(-s * 0.14, -s * 0.36); ctx.lineTo(-s * 0.12, -s * 0.62); ctx.lineTo(-s * 0.02, -s * 0.42);
    ctx.moveTo(s * 0.14, -s * 0.36); ctx.lineTo(s * 0.12, -s * 0.62); ctx.lineTo(s * 0.02, -s * 0.42);
    ctx.fill();
    ctx.restore();
  }

  var loop = kit.loop(function (now, dt) {
    var dark = document.documentElement.getAttribute("data-theme") === "dark";
    var color = dark ? "#9d86c4" : "#2b1b3d";
    var i, b;
    for (i = 0; i < bats.length; i++) {                // erase where each bat was
      b = bats[i];
      if (b.bb) ctx.clearRect(b.bb[0], b.bb[1], b.bb[2], b.bb[3]);
      b.bb = null;
    }
    var decay = Math.pow(0.9, dt * 60);
    for (i = 0; i < bats.length; i++) {
      b = bats[i];
      if (b.wait > 0) { b.wait -= dt; continue; }
      b.t += dt; b.flap += dt * b.flapF * Math.PI * 2;
      b.x += b.dir * b.speed * dt;
      b.y = b.baseY + Math.sin(b.t * b.bobF * Math.PI * 2) * b.bobA;
      kit.repel(b, b.x + b.ox, b.y + b.oy, REPEL, 2.2);   // scatter from the cursor like the other themes
      b.vx *= decay; b.vy *= decay; b.ox += b.vx; b.oy += b.vy;
      b.ox *= Math.pow(0.985, dt * 60); b.oy *= Math.pow(0.985, dt * 60);   // drift back to the flight line
      b.vyDraw = Math.cos(b.t * b.bobF * Math.PI * 2) * b.bobA * b.bobF;
      if ((b.dir > 0 && b.x > W + 50) || (b.dir < 0 && b.x < -50)) { bats[i] = makeBat(false); continue; }
      drawBat(b, color);
      var r = b.s * 1.4 + 4, cx = b.x + b.ox, cy = b.y + b.oy;
      b.bb = [Math.floor(cx - r), Math.floor(cy - r), Math.ceil(r * 2), Math.ceil(r * 2)];
    }
    ctx.globalAlpha = 1;
  });
  function startBats() {
    if (cv || kit.reduced()) return;
    cv = kit.canvas("th-bats hw-bats", 2); ctx = cv.ctx; cv.onSize = onSize; onSize();
    bats = []; for (var i = 0; i < nBats; i++) bats.push(makeBat(true));
    // the first-frame bats are spread across the sky already, but leave a few outside so it opens calm
    for (i = 0; i < bats.length; i += 2) { bats[i].wait = 0.5 + Math.random() * 4; bats[i].x = bats[i].dir > 0 ? -40 : W + 40; }
    loop.start();
  }
  function stopBats() { loop.stop(); if (cv) cv.remove(); cv = ctx = null; bats = []; }
  kit.onMotion(function (reduced) { if (reduced) stopBats(); else startBats(); });
  startBats();

  /* ---------- 3. pumpkin trail ---------- */
  kit.trail({
    cls: "hw-pumpkin", pool: 16, gap: 55, min: 26, dx: -14, dy: 12, ms: 950,   // offset so the pointer never sits on one
    frames: function (x, y) {
      var r = Math.round((Math.random() - 0.5) * 50), sz = 0.8 + Math.random() * 0.45;
      return [
        { opacity: 0, transform: "translate(" + x + "px," + y + "px) rotate(" + r + "deg) scale(" + (sz * 0.4) + ")" },
        { opacity: 0.8, offset: 0.16, transform: "translate(" + x + "px," + y + "px) rotate(" + r + "deg) scale(" + sz + ")" },
        { opacity: 0, transform: "translate(" + x + "px," + (y + 16) + "px) rotate(" + (r + 35) + "deg) scale(" + (sz * 0.55) + ")" }
      ];
    }
  });
})();

/* ============================================================
   THANKSGIVING (2026-10-01) -- Monday to Friday of Thanksgiving week (the 4th Thursday of November;
   Nov 23-27 in 2026, computed every year by __themeKit), or ?theme=thanksgiving to preview.
   1. Autumn leaves, acorns and wheat drifting down behind the UI (kit.field; the leaf outline is the
      same kit.shapes.leaf the October leaves use, they spin away from the cursor or a finger).
   2. A little acorn-spark trail behind a mouse pointer (kit.trail: fine pointers only, 14 pooled
      elements, never on touch).
   3. Harvest confetti on quiz completion (window.__confettiColors) and the warm light-mode tint on the
      app-shell pages (body.thanksgiving-theme in theme.css, arcade.css, guides.html, group-join.html,
      group-host.html).
   prefers-reduced-motion: one still frame of the drift, no trail.
   ============================================================ */
(function () {
  var kit = window.__themeKit;
  if (!kit.on("thanksgiving")) return;
  document.body.classList.add("thanksgiving-theme");
  kit.colors(["#c2410c", "#d97706", "#ca8a04", "#92400e", "#b45309", "#65a30d"]);

  var LEAF = ["#ea580c", "#c2410c", "#ca8a04", "#a16207", "#991b1b", "#b45309"];
  var NUT = ["#a16207", "#92400e", "#b45309"];
  var GRAIN = ["#ca8a04", "#d4a017", "#b8860b"];
  var KINDS = ["leaf", "leaf", "leaf", "acorn", "acorn", "wheat"], speedMul = 0.35;

  function acorn(ctx, s, color) {                   // nut with a dark cap and a short stem, centered on the origin
    ctx.fillStyle = color; ctx.beginPath(); ctx.ellipse(0, s * 0.3, s * 0.55, s * 0.85, 0, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = "#5b3410"; ctx.beginPath(); ctx.ellipse(0, -s * 0.28, s * 0.68, s * 0.46, 0, Math.PI, 0); ctx.closePath(); ctx.fill();
    ctx.lineWidth = Math.max(1, s * 0.16); ctx.strokeStyle = "#5b3410"; ctx.lineCap = "round";
    ctx.beginPath(); ctx.moveTo(0, -s * 0.7); ctx.lineTo(s * 0.12, -s * 1.05); ctx.stroke();
  }
  function wheat(ctx, s, color) {                   // a stalk with pairs of grains up the top
    ctx.strokeStyle = color; ctx.fillStyle = color; ctx.lineWidth = Math.max(1, s * 0.13); ctx.lineCap = "round";
    ctx.beginPath(); ctx.moveTo(0, s * 1.5); ctx.lineTo(0, -s * 0.8); ctx.stroke();
    for (var k = 0; k < 4; k++) {
      var y = -s * 0.7 + k * s * 0.4;
      ctx.beginPath(); ctx.ellipse(-s * 0.2, y, s * 0.11, s * 0.3, -0.55, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.ellipse(s * 0.2, y, s * 0.11, s * 0.3, 0.55, 0, Math.PI * 2); ctx.fill();
    }
    ctx.beginPath(); ctx.ellipse(0, -s * 1.15, s * 0.11, s * 0.32, 0, 0, Math.PI * 2); ctx.fill();
  }

  kit.field({
    cls: "th-thanks", dprCap: 1.5, reduced: "still", wrap: 20, kick: true, fps: 30, rad: function (p) { return p.s * 2.4; },
    count: window.innerWidth < 700 ? 16 : 30,
    make: function (randomY) {
      var kind = KINDS[(Math.random() * KINDS.length) | 0], s = 6 + Math.random() * 6;
      var pal = kind === "leaf" ? LEAF : (kind === "acorn" ? NUT : GRAIN);
      return {
        kind: kind, x: Math.random() * window.innerWidth,
        y: randomY ? Math.random() * window.innerHeight : -10 - Math.random() * 40,
        s: s, speed: (0.3 + s * 0.05) * speedMul,
        drift: Math.random() * Math.PI * 2, driftSpeed: 0.008 + Math.random() * 0.014,
        spin: kind === "wheat" ? (Math.random() - 0.5) * 0.5 : Math.random() * Math.PI * 2,
        spinSpeed: kind === "wheat" ? 0 : (Math.random() - 0.5) * 0.04,
        opacity: 0.5 + Math.random() * 0.4, color: pal[(Math.random() * pal.length) | 0], vx: 0, vy: 0
      };
    },
    move: function (p, k) {
      p.y += (p.speed + p.vy) * k; p.drift += p.driftSpeed * k; p.x += (Math.sin(p.drift) * 1.1 + p.vx) * k;
      if (p.kind === "wheat") p.spinSpeed = 0; else p.spin += p.spinSpeed * k;      // wheat sways instead of tumbling
    },
    gone: function (p) { return p.y > window.innerHeight + 24; },
    draw: function (ctx, p) {
      ctx.save(); ctx.translate(p.x, p.y);
      ctx.rotate(p.kind === "wheat" ? p.spin + Math.sin(p.drift) * 0.35 : p.spin);
      ctx.globalAlpha = p.opacity;
      if (p.kind === "leaf") { ctx.fillStyle = p.color; kit.shapes.leaf(ctx, p.s); ctx.fill(); }
      else if (p.kind === "acorn") acorn(ctx, p.s, p.color);
      else wheat(ctx, p.s * 0.95, p.color);
      ctx.restore();
    }
  });

  kit.trail({
    cls: "th-acorn", pool: 14, gap: 60, min: 30, dx: -8, dy: 12, ms: 900,
    frames: function (x, y) {
      var r = Math.round((Math.random() - 0.5) * 60), sz = 0.8 + Math.random() * 0.4, j = Math.round((Math.random() - 0.5) * 12);
      return [
        { opacity: 0, transform: "translate(" + x + "px," + y + "px) rotate(" + r + "deg) scale(" + (sz * 0.4) + ")" },
        { opacity: 0.9, offset: 0.16, transform: "translate(" + x + "px," + y + "px) rotate(" + r + "deg) scale(" + sz + ")" },
        { opacity: 0, transform: "translate(" + (x + j) + "px," + (y + 18) + "px) rotate(" + (r + 40) + "deg) scale(" + (sz * 0.5) + ")" }
      ];
    }
  });
})();

// Seasonal St. Patrick's theme (added 2026-07-17, brought up to the Halloween standard 2026-10-01) -- Mar 3-17.
// Falling four-leaf clovers behind all UI, plus the green light-mode tint (body.stpatricks-theme).
//   - Clovers spin faster and tumble over as they fall (the width squashes and flips), and every second or so one
//     catches the light with a little golden glint.
//   - A lucky-sparkle trail follows a mouse pointer (kit.trail: fine pointers only, 14 pooled elements).
//   - Green and gold quiz-completion confetti. 30 fps, dirty-rect redraw, canvas capped at 2x, reduced motion:
//     one still frame and no trail.
(function () {
  var kit = window.__themeKit;
  if (!kit.on("clovers")) return;
  document.body.classList.add("stpatricks-theme");
  kit.colors(["#16a34a", "#22c55e", "#4ade80", "#fbbf24", "#15803d"]);
  var COLORS = ["#16a34a", "#22c55e", "#15803d", "#4ade80", "#166534"], speedMul = 0.35, F = null;
  F = kit.field({
    cls: "th-clovers", dprCap: 1.5, reduced: "still", wrap: 20, kick: true, fps: 30,
    count: window.innerWidth < 700 ? 16 : 30,
    rad: function (c) { return c.s * 2.6; },
    make: function (randomY) {
      var s = 5 + Math.random() * 7;
      return {
        x: Math.random() * window.innerWidth,
        y: randomY ? Math.random() * window.innerHeight : -10 - Math.random() * 40,
        s: s, speed: (0.3 + s * 0.05) * speedMul,
        drift: Math.random() * Math.PI * 2, driftSpeed: 0.008 + Math.random() * 0.014,
        spin: Math.random() * Math.PI * 2, spinSpeed: (Math.random() - 0.5) * 0.06,
        flip: Math.random() * Math.PI * 2, flipSpeed: 0.025 + Math.random() * 0.04, glint: 0,
        opacity: 0.4 + Math.random() * 0.4, color: COLORS[(Math.random() * COLORS.length) | 0], vx: 0, vy: 0
      };
    },
    move: function (c, k) {
      c.y += (c.speed + c.vy) * k; c.drift += c.driftSpeed * k; c.spin += c.spinSpeed * k; c.flip += c.flipSpeed * k;
      c.x += (Math.sin(c.drift) * 1.1 + c.vx) * k;
      if (c.glint > 0) c.glint -= k / 60;
    },
    gone: function (c) { return c.y > window.innerHeight + 24; },
    begin: function () {                                              // now and then one clover catches the light
      if (!F || Math.random() > 0.03) return;
      var ps = F.particles(), c = ps[(Math.random() * ps.length) | 0];
      if (c && c.glint <= 0 && c.y > 0 && c.y < window.innerHeight) c.glint = 0.55;
    },
    draw: function (ctx, c) {
      ctx.save(); ctx.translate(c.x, c.y); ctx.rotate(c.spin);
      ctx.save(); ctx.scale(Math.max(0.3, Math.abs(Math.cos(c.flip))), 1);          // tumbles over
      ctx.globalAlpha = c.opacity; ctx.fillStyle = c.color;
      kit.shapes.clover(ctx, c.s); ctx.fill();
      ctx.beginPath(); ctx.moveTo(0, c.s * 0.1); ctx.lineTo(0, c.s * 1.15);          // the stem
      ctx.lineWidth = Math.max(1, c.s * 0.16); ctx.strokeStyle = "#14532d"; ctx.stroke();
      ctx.restore();
      if (c.glint > 0 && !kit.reduced()) {                                           // a four-point golden glint
        var t = Math.sin(Math.PI * (1 - c.glint / 0.55)), r = c.s * (0.5 + 1.1 * t);
        ctx.rotate(-c.spin); ctx.globalAlpha = 0.9 * t; ctx.fillStyle = "#fde047";
        ctx.beginPath(); ctx.moveTo(0, -r); ctx.quadraticCurveTo(r * 0.12, -r * 0.12, r, 0); ctx.quadraticCurveTo(r * 0.12, r * 0.12, 0, r);
        ctx.quadraticCurveTo(-r * 0.12, r * 0.12, -r, 0); ctx.quadraticCurveTo(-r * 0.12, -r * 0.12, 0, -r); ctx.fill();
      }
      ctx.restore();
    }
  });
  kit.trail({
    cls: "cl-spark", pool: 14, gap: 55, min: 26, dx: -9, dy: 8, ms: 850,
    frames: function (x, y) {
      var r = Math.round((Math.random() - 0.5) * 80), sz = 0.7 + Math.random() * 0.6, j = Math.round((Math.random() - 0.5) * 14);
      return [
        { opacity: 0, transform: "translate(" + x + "px," + y + "px) rotate(" + r + "deg) scale(" + (sz * 0.3) + ")" },
        { opacity: 0.95, offset: 0.2, transform: "translate(" + x + "px," + y + "px) rotate(" + (r + 20) + "deg) scale(" + sz + ")" },
        { opacity: 0, transform: "translate(" + (x + j) + "px," + (y - 14) + "px) rotate(" + (r + 90) + "deg) scale(" + (sz * 0.4) + ")" }
      ];
    }
  });
})();

/* ============================================================
   PA WEEK (2026-09-30, Jaxon: "a theme for PA week ... Monday through Friday
   next week", "fun animations")
   ------------------------------------------------------------
   Active Mon 5 - Fri 9 October 2026 only (year-specific on purpose: move the dates each
   year), or on any page loaded with ?paweek=1 so it can be previewed outside the window.
   Same architecture as the other seasonal themes: lives here so every page gets it.
   1. A canvas of PA-themed things drifting UP like balloons behind the UI (hearts,
      stethoscopes, medical crosses, pills, little "PA" badges) that scatter from the
      cursor or a finger (the standing repel default for particle themes).
   2. body.paweek-theme, which the app-shell pages tint and drift (theme.css, arcade.css,
      guides.html, group-join.html, group-host.html).
   3. A welcome card on the app-shell pages, once a day per device: a heartbeat line that
      keeps drawing, a line for the day of the week, and a burst of PA-coloured confetti.
   4. Quiz-completion confetti in the same colours all week.
   ============================================================ */
(function () {
  var kit = window.__themeKit;
  if (!kit.on("paweek")) return;
  var now = new Date();
  var preview = kit.fresh("paweek");

  document.body.classList.add("paweek-theme");
  var PALETTE = ["#2563eb", "#14b8a6", "#f43f5e", "#f59e0b", "#8b5cf6"];
  kit.colors(PALETTE);

  /* ---------- 1. the drifting shapes (kit.field: one canvas behind the UI, repel, hidden-tab pause) ---------- */
  // heart (the same two-lobe bezier the Valentine's theme uses), stethoscope, cross, pill, PA badge
  var KINDS = ["heart", "heart", "steth", "steth", "cross", "cross", "pill", "badge"];
  function drawShape(ctx, p) {
    var s = p.s, c = p.color;
    ctx.fillStyle = c; ctx.strokeStyle = c;
    if (p.kind === "heart") { ctx.translate(0, -s * 1.7 * 0.5); kit.shapes.heart(ctx, s); ctx.fill(); }
    else if (p.kind === "cross") {
      var a = s * 0.42; ctx.beginPath(); ctx.rect(-a, -s, 2 * a, 2 * s); ctx.rect(-s, -a, 2 * s, 2 * a); ctx.fill();
    } else if (p.kind === "pill") {
      var r = s * 0.72, h = s * 1.05;
      ctx.beginPath(); ctx.moveTo(-h, -r); ctx.lineTo(h, -r); ctx.arc(h, 0, r, -Math.PI / 2, Math.PI / 2); ctx.lineTo(-h, r); ctx.arc(-h, 0, r, Math.PI / 2, Math.PI * 1.5); ctx.closePath();
      ctx.fill();
      ctx.save(); ctx.clip(); ctx.fillStyle = "rgba(255,255,255,.88)"; ctx.fillRect(-h * 2, -r, h * 2, 2 * r); ctx.restore();
      ctx.lineWidth = 1.4; ctx.stroke();
    } else if (p.kind === "steth") {
      ctx.lineWidth = Math.max(1.6, s * 0.2); ctx.lineCap = "round"; ctx.lineJoin = "round";
      ctx.beginPath(); ctx.moveTo(-s * 0.75, -s * 1.05); ctx.quadraticCurveTo(-s * 0.75, s * 0.35, 0, s * 0.35); ctx.quadraticCurveTo(s * 0.75, s * 0.35, s * 0.75, -s * 1.05); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(0, s * 0.35); ctx.bezierCurveTo(0, s * 1.0, s * 0.95, s * 0.6, s * 0.95, s * 1.0); ctx.stroke();
      ctx.beginPath(); ctx.arc(s * 0.95, s * 1.25, s * 0.28, 0, Math.PI * 2); ctx.fill();
      ctx.beginPath(); ctx.arc(-s * 0.75, -s * 1.05, s * 0.14, 0, Math.PI * 2); ctx.arc(s * 0.75, -s * 1.05, s * 0.14, 0, Math.PI * 2); ctx.fill();
    } else {
      ctx.beginPath(); ctx.arc(0, 0, s * 1.15, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = "#fff"; ctx.font = "800 " + Math.round(s * 1.05) + "px -apple-system, system-ui, sans-serif";
      ctx.textAlign = "center"; ctx.textBaseline = "middle"; ctx.fillText("PA", 0, s * 0.06);
    }
  }
  function make(randomY) {
    return {
      kind: KINDS[(Math.random() * KINDS.length) | 0], color: PALETTE[(Math.random() * PALETTE.length) | 0],
      s: 8 + Math.random() * 7, x: Math.random() * window.innerWidth,
      y: randomY ? Math.random() * window.innerHeight : window.innerHeight + 30 + Math.random() * 60,
      speed: 0.28 + Math.random() * 0.4, drift: Math.random() * Math.PI * 2, driftSpeed: 0.006 + Math.random() * 0.012,
      tilt: Math.random() * 6, opacity: 0.5 + Math.random() * 0.35, vx: 0, vy: 0
    };
  }
  kit.field({
    cls: "th-paweek", dprCap: 1.5, reduced: "still", wrap: 40, first: true, fps: 30,
    count: window.innerWidth < 700 ? 14 : 28,
    rad: function (p) { return p.s * 2.6; },
    make: make,
    move: function (p, k) { p.y -= p.speed * k; p.y += p.vy * k; p.drift += p.driftSpeed * k; p.x += (Math.sin(p.drift) * 0.9 + p.vx) * k; p.tilt += 0.012 * k; },
    gone: function (p) { return p.y < -60; },
    draw: function (ctx, p) {
      ctx.save(); ctx.translate(p.x, p.y); ctx.rotate(Math.sin(p.tilt) * 0.4);
      ctx.globalAlpha = p.opacity * (0.85 + 0.15 * Math.sin(p.drift * 2));
      drawShape(ctx, p); ctx.restore();
    }
  });

  /* ---------- 2b. the splash text on the logo (homepage only) ----------
     Jaxon: "add the #s that are for PA week on the side like how minecraft has the pulsing in the
     corner". A yellow tilted hashtag that pulses beside the logo and changes every few seconds,
     like the splash text on Minecraft's title screen. Two copies (the big desktop logo and the
     small phone logo); whichever logo is showing gets the visible one. */
  var marks = kit.logoMark("pa-splash");
  if (marks) {
    var TAGS = ["#PAWeek", "#NationalPAWeek", "#PAWeek2026", "#ClassOf2028"], ti = 0, timer = 0;
    marks.forEach(function (el) { if (el) el.textContent = TAGS[0]; });
    var cycle = function () {
      ti = (ti + 1) % TAGS.length;
      marks.forEach(function (el) { if (el) { el.textContent = TAGS[ti]; el.classList.remove("swap"); void el.offsetWidth; el.classList.add("swap"); } });
    };
    var run = function (on) { clearInterval(timer); timer = on ? setInterval(cycle, 3800) : 0; };
    run(!document.hidden); kit.onVisible(run);                      // nothing cycles in a hidden tab
  }

  /* ---------- 2c. a tiny medical-cross trail behind a mouse pointer (kit.trail: fine pointers only) ---------- */
  kit.trail({
    cls: "pa-trail", pool: 14, gap: 60, min: 30, dx: -8, dy: 10, ms: 900,
    frames: function (x, y) {
      var r = Math.round((Math.random() - 0.5) * 50), sz = 0.8 + Math.random() * 0.45;
      return [
        { opacity: 0, transform: "translate(" + x + "px," + y + "px) rotate(" + r + "deg) scale(" + (sz * 0.4) + ")" },
        { opacity: 0.85, offset: 0.16, transform: "translate(" + x + "px," + y + "px) rotate(" + r + "deg) scale(" + sz + ")" },
        { opacity: 0, transform: "translate(" + x + "px," + (y + 16) + "px) rotate(" + (r + 30) + "deg) scale(" + (sz * 0.5) + ")" }
      ];
    }
  });

  /* ---------- 3. the welcome card (app-shell pages only, once a day) ---------- */
  if (!kit.isShell()) return;
  var DAYS = {
    1: "Kickoff! This week belongs to physician assistants, and to the one you are becoming.",
    2: "Every heartbeat you learn is a patient you will help someday.",
    3: "Halfway there. Teamwork is at the heart of the PA profession.",
    4: "Fun fact: PAs practice medicine in every specialty.",
    5: "Last day of PA Week. You have earned a little celebration."
  };
  var dow = now.getDay(); if (dow < 1 || dow > 5) dow = 1;
  var card = kit.card({
    key: "paWeekSeen:" + now.getFullYear() + "-" + (now.getMonth() + 1) + "-" + now.getDate(), fresh: preview, burst: [90, 1.4],
    html: '<svg class="pa-ecg" viewBox="0 0 120 32" aria-hidden="true"><path pathLength="1" d="M0 17H22L27 17 31 5 37 28 42 12 46 17H70L75 17 79 7 85 26 89 17H120"/></svg>' +
      '<div class="pa-toast-txt"><b>Happy PA Week, Class of 2028!</b><span></span></div>'
  });
  if (card) card.querySelector("span").textContent = DAYS[dow];
})();
