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
   - kit.field: a canvas of drifting particles behind the UI (respawn, wrap, paused when the tab is
     hidden, reduced-motion mode).
   - kit.canvas / kit.loop / kit.card / kit.shapes / kit.colors: the pieces kit.field and the bespoke
     themes are built from.
   Rules every theme keeps: behind the content or pointer-events none, no layout shift, nothing runs in
   a hidden tab, reduced motion and the Holiday animations switch respected, calm enough to study beside.
   NO MOUSE OR TOUCH EFFECTS (Jaxon, 2026-10-25: "remove the mouse effects I dont want them on any theme"):
   the cursor scatter and the cursor trails were taken out of every theme; do not add them back.
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

  /* ----- motion preference (the system setting OR the site's Holiday animations switch), tab visibility -----
     kit.reduced(): hold still. kit.calm(): the switch is off, so nothing moving is shown at all (a field that
     would freeze one still frame under reduced motion is removed instead). */
  var rmq = window.matchMedia ? matchMedia("(prefers-reduced-motion: reduce)") : { matches: false };
  kit.calm = function () { return document.documentElement.classList.contains("th-fx-off"); };
  kit.reduced = function () { return rmq.matches || kit.calm(); };
  var motionSubs = [], visSubs = [];
  kit.onMotion = function (fn) { motionSubs.push(fn); };
  kit.onVisible = function (fn) { visSubs.push(fn); };
  function motionChanged() { var r = kit.reduced(); motionSubs.forEach(function (f) { f(r); }); }
  if (rmq.addEventListener) rmq.addEventListener("change", motionChanged); else if (rmq.addListener) rmq.addListener(motionChanged);
  window.addEventListener("themefx", motionChanged);                 // theme.js window.ThemeFx: the switch flipped
  function visChanged() {
    body.classList.toggle("th-paused", document.hidden);            // CSS animations pause with it
    visSubs.forEach(function (f) { f(!document.hidden); });
  }
  document.addEventListener("visibilitychange", visChanged);
  window.addEventListener("pageshow", function (e) { if (e.persisted) visChanged(); });   // back/forward cache restore

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
     begin(ctx) once per frame, after(ctx, still, k) once per frame after the particles, dprCap, fps (cap), onSize(particles, W, H), rad(p) (bounding radius: redraw only the dirty rectangles) + strip() ->
     [y, height] of a band to clear as well + dirty() -> [[x, y, w, h], ...] more rectangles to clear,
     reduced: "run" (ignore the preference), "still" (one frozen frame), "off" (no canvas), first (draw a frame at once).
     The Holiday animations switch (kit.calm()) always means no canvas. */
  kit.field = function (cfg) {
    var cv = null, ps = [], mode = cfg.reduced || "off";
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
      if (kit.calm() || (kit.reduced() && mode !== "run")) {
        loop.stop();
        if (mode === "off" || kit.calm()) { if (cv) { cv.remove(); cv = null; } ps = []; }
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
//   - The bigger flakes are six-armed crystals that spin slowly. Calmed 2026-10-25 (fewer, slower flakes).
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
    cls: "th-snow", dprCap: 1.5, reduced: "still", wrap: 10, fps: 30,
    count: window.innerWidth < 700 ? 28 : 55,                      // lighter on narrow/mobile viewports
    rad: function (f) { return f.r * 1.9 + 2; },
    strip: function () { return [window.innerHeight - MAXH - 4, MAXH + 5]; },
    make: function (randomY) {
      var r = 1.7 + Math.random() * 3.4;
      return {
        x: Math.random() * window.innerWidth,
        y: randomY ? Math.random() * window.innerHeight : -10 - Math.random() * 40,
        r: r, speed: (0.5 + r * 0.45 + Math.random() * 0.4) * 0.5,      // 40-95 px a second (was 75-190)
        drift: Math.random() * Math.PI * 2, driftSpeed: 0.004 + Math.random() * 0.008,
        spin: Math.random() * Math.PI, spinSpeed: (Math.random() - 0.5) * 0.02,
        opacity: 0.6 + Math.random() * 0.4
      };
    },
    move: function (f, k) {
      f.y += f.speed * k; f.drift += f.driftSpeed * k; f.x += Math.sin(f.drift) * (windStrength * 1.6) * k;
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
   of sparks that drift down and fade. At most 1-2 bursts at once, one every 3-6 seconds (calmed
   2026-10-25; it was 2-3 at once every 1-3 seconds), 30 frames a second, one canvas behind
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
    if (clock >= next && shows.length < (narrow ? 1 : 2)) {
      var band = narrow ? 0.5 : 0.26, left = Math.random() < 0.5;       // wide screens: the outer quarters only
      var x = narrow ? W * (0.1 + Math.random() * 0.8) : (left ? W * (0.03 + Math.random() * band * 0.85) : W * (1 - 0.03 - Math.random() * band * 0.85));
      var pals = cfg.palettes(dark);
      shows.push({ x: x, by: H * (0.1 + Math.random() * 0.4), y: H + 8, rise: 0, pal: pals[(Math.random() * pals.length) | 0],
        parts: null, age: 0, scale: narrow ? 0.7 : 1 });
      next = clock + 3 + Math.random() * 3;
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
//   - 2026-10-25: the cursor/tap pop and its sparkle were removed (no mouse effects on any theme) and there are fewer hearts.
//   - On the homepage the logo gets a soft heartbeat glow behind it (CSS only, lub-dub then a rest).
//   - Pink quiz-completion confetti. 30 fps, dirty-rect redraw, canvas capped at 2x, reduced motion: one still frame.
(function () {
  var kit = window.__themeKit;
  if (!kit.on("hearts")) return;
  document.body.classList.add("vday-theme");
  var COLORS = ["#ec4899", "#f472b6", "#f43f5e", "#fb7185", "#e11d48"], speedMul = 0.35;
  kit.colors(["#ec4899", "#f472b6", "#f43f5e", "#fb7185", "#e11d48"]);
  kit.field({
    cls: "th-hearts", dprCap: 1.5, reduced: "still", wrap: 20, fps: 30,
    count: window.innerWidth < 700 ? 9 : 18,
    rad: function (h) { return h.s * 1.9 + 3; },
    make: function (randomY) {
      var s = 6 + Math.random() * 9;
      return {
        x: Math.random() * window.innerWidth,
        y: randomY ? Math.random() * window.innerHeight : window.innerHeight + 10 + Math.random() * 40,
        s: s, speed: (0.35 + s * 0.045) * speedMul,
        drift: Math.random() * Math.PI * 2, driftSpeed: 0.006 + Math.random() * 0.012,
        opacity: 0.3 + Math.random() * 0.35, color: COLORS[(Math.random() * COLORS.length) | 0]
      };
    },
    move: function (h, k) { h.y -= h.speed * k; h.drift += h.driftSpeed * k; h.x += Math.sin(h.drift) * 0.6 * k; },
    gone: function (h) { return h.y < -20; },
    draw: function (ctx, h) {
      ctx.save(); ctx.translate(h.x, h.y); ctx.rotate(Math.sin(h.drift) * 0.25);
      ctx.globalAlpha = h.opacity; ctx.fillStyle = h.color;
      kit.shapes.heart(ctx, h.s); ctx.fill(); ctx.restore();
    }
  });
  kit.logoMark("vd-beat", true);
})();

// Seasonal Fall theme (added 2026-07-17, brought up to the Halloween standard 2026-10-01) -- Oct 17-23
// (Oct 24-31 is Halloween, which takes over; see __themeKit YIELDS). Autumn leaves behind all UI, plus the
// warm light-mode tint (body.fall-theme).
//   - Leaves rock side to side like a pendulum as they fall and flip over (a squashed width), instead of
//     spinning flat. 2026-10-25: no cursor scatter (no mouse effects on any theme) and fewer leaves.
//   - Leaves that reach the bottom edge can land and lie there (a loose litter along the edge, never more than
//     half of them) and fade out after 20-30 seconds.
//   - Quiz-completion confetti in autumn colors. 30 fps, dirty-rect redraw, reduced motion: one still frame.
(function () {
  var kit = window.__themeKit;
  if (!kit.on("leaves")) return;
  document.body.classList.add("fall-theme");
  kit.colors(["#ea580c", "#c2410c", "#ca8a04", "#991b1b", "#b45309"]);
  var COLORS = ["#ea580c", "#c2410c", "#ca8a04", "#a16207", "#991b1b", "#b45309"], speedMul = 0.35;
  var N = window.innerWidth < 700 ? 12 : 24, MAXPILE = Math.round(N * 0.5), resting = 0, F = null;
  F = kit.field({
    cls: "th-leaves", dprCap: 1.5, reduced: "still", wrap: 20, fps: 30, count: N,
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
        flip: Math.random() * Math.PI * 2, flipSpeed: 0.015 + Math.random() * 0.025,     // a slow tumble (halved 2026-10-25)
        rest: false, restT: 0, restMax: 20 + Math.random() * 10,
        opacity: 0.5 + Math.random() * 0.4, color: COLORS[(Math.random() * COLORS.length) | 0]
      };
    },
    move: function (l, k) {
      if (l.rest) { l.restT += k / 60; return; }
      l.y += l.speed * k; l.drift += l.driftSpeed * k; l.spin += l.spinSpeed * k; l.flip += l.flipSpeed * k;
      l.x += Math.sin(l.drift) * 1.1 * k;
    },
    gone: function (l) {
      var H = window.innerHeight;
      if (l.rest) return l.restT > l.restMax;
      if (l.y > H - l.s * 0.5 && resting < MAXPILE && Math.random() < 0.8) {     // lands on the edge
        l.rest = true; l.restT = 0; l.y = H - l.s * 0.45 - Math.random() * 3; return false;
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
        ctx.rotate(Math.cos(l.drift) * 0.5 + l.spin * 0.35);                     // rocks into each swing
        ctx.scale(Math.max(0.18, Math.abs(Math.cos(l.flip))), 1);              // tumbles over
      }
      ctx.globalAlpha = a; ctx.fillStyle = l.color;
      kit.shapes.leaf(ctx, l.s); ctx.fill(); ctx.restore();
    }
  });
})();

/* ============================================================
   HALLOWEEN (2026-10-01; rebuilt 2026-10-25) -- Oct 24-31 inclusive (local date), or ?theme=halloween /
   ?halloween=1 to preview (__themeKit; the autumn leaves yield to it).
   Jaxon, 2026-10-25: the bats were "too distracting", no mouse effects on any theme, "just put some high quality
   cartoon pumpkins that flicker/glow in the bottom left sitting", then "those pumpkins look too good and plastic
   what if the bottom of the screen was like a thin layer of fall leaves piled up also" and "I want something on
   the homepage". So:
   1. A thin pile of fallen leaves along the bottom edge of the window on every page: one canvas behind the content,
      drawn once from a fixed seed (every page shows the same pile), redrawn only when the width changes. Still.
   2. Three carved jack-o'-lanterns, matte (grained skin, no gloss), faces lit from inside with a gentle candle
      flicker. On the homepage they sit beside the big logo (or the small phone logo); elsewhere in the bottom-left
      corner of the window on the leaves, sized to the empty corner and left out where the content fills the width.
   Layers (SVGs with one viewBox, stacked): glow, pumpkins with unlit carved hollows, one lit face each. Only
   whole-layer opacity animates (theme.css), so the flicker runs on the compositor. The gradients, filters and
   clip paths live once in a 0 x 0 SVG so every copy can share them. Reduced motion or the Holiday animations
   setting: lit and still. body.halloween-theme tints the app-shell pages in light mode (theme.css, arcade.css,
   guides.html, group-join.html, group-host.html).
   ============================================================ */
(function () {
  var kit = window.__themeKit;
  if (!kit.on("halloween")) return;
  var body = document.body, home = body.classList.contains("homepage");
  body.classList.add("halloween-theme");
  kit.colors(["#f97316", "#7c3aed", "#22c55e", "#facc15", "#ea580c"]);

  /* ---------- the pumpkins (each drawn in a 120 x 100 box, base at y = 100, placed with [x, y, scale]) ---------- */
  var PUMPKINS = [
    { at: [8, 26, 1], face: "classic" },
    { at: [146, 55, 0.72], face: "happy" },
    { at: [104, 80, 0.46], face: "cute" }
  ];
  var FACES = {
    classic: "M33 55 L50 55 L44 40 Z M70 55 L87 55 L76 40 Z M55 64 L65 64 L60 57 Z" +
      "M28 67 Q60 100 92 67 L83 71 L80 77 L74 72 L66 74 L63 80 L57 80 L54 74 L46 72 L40 77 L37 71 Z",
    happy: "M32 54 Q41 35 50 54 Q41 49 32 54 Z M70 54 Q79 35 88 54 Q79 49 70 54 Z" +
      "M32 64 Q60 96 88 64 Q81 69 74 69 L71 75 L66 70 L54 70 L49 75 L46 69 Q39 69 32 64 Z",
    cute: "M37 54 L49 54 L43 43 Z M71 54 L83 54 L77 43 Z M56 62 L64 62 L60 56 Z M45 69 Q60 84 75 69 Q60 75 45 69 Z"
  };
  var RIBS = [[30, 61, 28, 36, "o"], [90, 61, 28, 36, "o"], [44, 59, 26, 40, "m"], [76, 59, 26, 40, "m"], [60, 58, 19, 41, "c"]];   // outer ribs first
  function place(p) { return '<g transform="translate(' + p.at[0] + " " + p.at[1] + ") scale(" + p.at[2] + ')">'; }
  function ribs(attrs) {
    return RIBS.map(function (r) { return '<ellipse cx="' + r[0] + '" cy="' + r[1] + '" rx="' + r[2] + '" ry="' + r[3] + '"' + attrs(r) + "/>"; }).join("");
  }
  function pumpkin(p) {
    var o = place(p) + '<ellipse cx="60" cy="99" rx="54" ry="6" fill="url(#hwpk-shadow)"/>';
    o += '<g filter="url(#hwpk-grain)">' + ribs(function (r) { return ' fill="url(#hwpk-' + r[4] + ')" stroke="#7a3412" stroke-width="1.7"'; }) + "</g>";
    o += '<ellipse cx="44" cy="40" rx="34" ry="24" fill="url(#hwpk-light)"/>' +                                    // soft light, no gloss
      '<path d="M2 62 Q3 98 32 98 L88 98 Q117 98 118 62 Q112 93 60 100 Q8 93 2 62 Z" fill="#5c240a" opacity=".22"/>' +  // shade underneath
      '<g class="hw-night" fill="#140600">' + ribs(function () { return ""; }) + "</g>";                              // dimmer at night
    o += '<path d="M66 21 C71 15 79 15 82 20 C85 25 79 29 76 25 C74 22 77 20 79 22" fill="none" stroke="#6b5a2a" stroke-width="1.6" stroke-linecap="round"/>' +
      '<path d="M53 23 C52 16 54 9 58 4 L66 2 C67 9 64 15 66 23 Z" fill="url(#hwpk-stem)" stroke="#3d2c12" stroke-width="1.6" stroke-linejoin="round"/>' +
      '<path d="M57 21 C56 15 57 10 60 5 M62 21 C61 15 62 9 64 4" fill="none" stroke="#3d2c12" stroke-width=".9" opacity=".55"/>' +
      '<ellipse cx="62" cy="3" rx="4.3" ry="1.6" fill="#a89060" stroke="#3d2c12" stroke-width="1"/>';                 // woody stem, cut top
    o += '<path d="' + FACES[p.face] + '" fill="#2e0f04" stroke="#5a2408" stroke-width="1.5" stroke-linejoin="round"/>';   // the hollow, unlit
    return o + "</g>";
  }
  function litFace(p, i) {                                    // candlelight, the cut wall inside each hole, a little light on the skin
    var d = FACES[p.face];
    return place(p) + '<path d="' + d + '" fill="#ffb84a" stroke="#ffa63a" stroke-width="5" stroke-linejoin="round" filter="url(#hwpk-blur)" opacity=".7"/>' +
      '<path d="' + d + '" fill="url(#hwpk-flame)"/>' +
      '<path d="' + d + '" fill="none" stroke="#e8923a" stroke-width="4.5" stroke-linejoin="round" clip-path="url(#hwpk-cut' + i + ')" opacity=".85"/>' +
      '<path d="' + d + '" fill="none" stroke="#5a2408" stroke-width="1.3" stroke-linejoin="round"/>' +
      '<ellipse cx="60" cy="64" rx="46" ry="30" fill="url(#hwpk-bleed)"/></g>';
  }
  function frontLeaves() {                                    // a few leaves lying in front of the pumpkins' feet
    var L = [[22, 126, 7, -23, "#a8431c"], [50, 129, 6, 52, "#c8962e"], [92, 127, 6.5, -69, "#8f2f1f"], [128, 128, 5.5, 17, "#b8642a"],
      [160, 129, 6, -46, "#7d4a22"], [196, 127, 6.5, 63, "#c9612a"], [226, 129, 5, -11, "#a8762e"]];
    return L.map(function (l) {
      return '<g transform="translate(' + l[0] + " " + l[1] + ") scale(1 .55) rotate(" + l[3] + ')"><path d="M0 ' + (-l[2]) + " Q" + (l[2] * 0.75) + " 0 0 " + l[2] +
        " Q" + (-l[2] * 0.75) + " 0 0 " + (-l[2]) + 'Z" fill="' + l[4] + '"/><path d="M0 ' + (-l[2] * 0.8) + " L0 " + (l[2] * 0.85) + '" stroke="#4a2410" stroke-width=".9" opacity=".5"/></g>';
    }).join("");
  }
  var VB = 'viewBox="0 0 240 130" xmlns="http://www.w3.org/2000/svg" focusable="false"';
  var defs = '<svg class="hw-pk-defs" width="0" height="0" aria-hidden="true" focusable="false"><defs>' +
    '<linearGradient id="hwpk-o" x1="0" x2="1"><stop offset="0" stop-color="#8f3a14"/><stop offset=".55" stop-color="#c4602a"/><stop offset="1" stop-color="#93401a"/></linearGradient>' +
    '<linearGradient id="hwpk-m" x1="0" x2="1"><stop offset="0" stop-color="#a84a1c"/><stop offset=".5" stop-color="#d9772f"/><stop offset="1" stop-color="#ad4f1f"/></linearGradient>' +
    '<linearGradient id="hwpk-c" x1="0" x2="1"><stop offset="0" stop-color="#b9581f"/><stop offset=".5" stop-color="#e58a3a"/><stop offset="1" stop-color="#bd5c22"/></linearGradient>' +
    '<radialGradient id="hwpk-light"><stop offset="0" stop-color="#ffd8a6" stop-opacity=".22"/><stop offset="1" stop-color="#ffd8a6" stop-opacity="0"/></radialGradient>' +
    '<linearGradient id="hwpk-stem" x1="0" x2="1"><stop offset="0" stop-color="#7c6a34"/><stop offset=".5" stop-color="#5e5024"/><stop offset="1" stop-color="#43381a"/></linearGradient>' +
    '<radialGradient id="hwpk-flame" cx=".5" cy=".55" r=".6"><stop offset="0" stop-color="#fff6d6"/><stop offset=".4" stop-color="#ffe08a"/><stop offset=".8" stop-color="#ffc04a"/><stop offset="1" stop-color="#f59e2a"/></radialGradient>' +
    '<radialGradient id="hwpk-bleed"><stop offset="0" stop-color="#ffd27a" stop-opacity=".14"/><stop offset="1" stop-color="#ffd27a" stop-opacity="0"/></radialGradient>' +
    '<radialGradient id="hwpk-halo"><stop offset="0" stop-color="#fdba74" stop-opacity=".45"/><stop offset=".55" stop-color="#fb923c" stop-opacity=".14"/><stop offset="1" stop-color="#fb923c" stop-opacity="0"/></radialGradient>' +
    '<radialGradient id="hwpk-shadow"><stop offset="0" stop-color="#1c0a02" stop-opacity=".32"/><stop offset="1" stop-color="#1c0a02" stop-opacity="0"/></radialGradient>' +
    '<filter id="hwpk-blur" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="3"/></filter>' +
    '<filter id="hwpk-grain" x="-6%" y="-6%" width="112%" height="112%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="7" result="n"/>' +
    '<feColorMatrix in="n" type="matrix" values="0 0 0 0 .32  0 0 0 0 .14  0 0 0 0 .03  0 0 0 .7 -.2" result="s"/>' +
    '<feComposite in="s" in2="SourceGraphic" operator="in" result="g"/><feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="g"/></feMerge></filter>' +
    PUMPKINS.map(function (p, i) { return '<clipPath id="hwpk-cut' + i + '">' + place(p) + '<path d="' + FACES[p.face] + '"/></g></clipPath>'; }).join("") +
    "</defs></svg>";
  var layers = '<svg class="hw-pk-glow" ' + VB + '><ellipse cx="68" cy="90" rx="78" ry="50" fill="url(#hwpk-halo)"/><ellipse cx="189" cy="100" rx="58" ry="38" fill="url(#hwpk-halo)"/></svg>' +
    '<svg class="hw-pk-base" ' + VB + ">" + PUMPKINS.map(pumpkin).join("") + frontLeaves() + "</svg>" +
    PUMPKINS.map(function (p, i) { return '<svg class="hw-pk-lit hw-pk-lit-' + (i + 1) + '" ' + VB + ">" + litFace(p, i) + "</svg>"; }).join("");
  function patch(cls) {
    var d = document.createElement("div");
    d.className = "hw-pk " + cls; d.setAttribute("aria-hidden", "true"); d.innerHTML = layers;
    return d;
  }

  /* ---------- 1. the leaf bed ---------- */
  var bed = document.createElement("canvas");
  bed.className = "hw-leafbed"; bed.setAttribute("aria-hidden", "true");
  var BED_H = 30, bedW = 0;
  function drawBed() {
    var W = window.innerWidth;
    if (W === bedW) return;
    bedW = W;
    var dpr = Math.min(window.devicePixelRatio || 1, 2), ctx = bed.getContext("2d"), H = BED_H;
    bed.width = Math.round(W * dpr); bed.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, H);
    var seed = 20261031;                                     // mulberry32: the same pile on every page and every visit
    function rnd() { seed = seed + 0x6D2B79F5 | 0; var t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }
    var PAL = ["#a8431c", "#c9612a", "#c8962e", "#7d4a22", "#8f2f1f", "#d9a441", "#7a6a2a", "#b08a5a", "#b8642a", "#9c5a26"];
    var g = ctx.createLinearGradient(0, H, 0, H - 22);       // the ground under the pile
    g.addColorStop(0, "rgba(92, 46, 16, .16)"); g.addColorStop(1, "rgba(92, 46, 16, 0)");
    ctx.fillStyle = g; ctx.fillRect(0, H - 22, W, 22);
    var MAPLE = [[0, -1], [0.28, -0.42], [0.9, -0.55], [0.5, 0.05], [0.72, 0.62], [0.12, 0.38], [0, 0.95], [-0.12, 0.38], [-0.72, 0.62], [-0.5, 0.05], [-0.9, -0.55], [-0.28, -0.42]];
    function leaf(x, y, sz, a, col, kind, shade) {
      ctx.save(); ctx.translate(x, y); ctx.scale(1, 0.5); ctx.rotate(a);          // lying flat, seen from a low angle
      ctx.beginPath();
      if (kind === 0) { ctx.moveTo(0, -sz); ctx.quadraticCurveTo(sz * 0.8, -sz * 0.2, 0, sz); ctx.quadraticCurveTo(-sz * 0.8, -sz * 0.2, 0, -sz); }
      else if (kind === 1) ctx.arc(0, 0, sz * 0.72, 0, Math.PI * 2);
      else { ctx.moveTo(MAPLE[0][0] * sz, MAPLE[0][1] * sz); for (var k = 1; k < MAPLE.length; k++) ctx.lineTo(MAPLE[k][0] * sz, MAPLE[k][1] * sz); }
      ctx.closePath(); ctx.fillStyle = col; ctx.fill();
      if (shade) { ctx.fillStyle = "rgba(40, 18, 6, " + shade + ")"; ctx.fill(); }
      ctx.strokeStyle = "rgba(60, 28, 10, .4)"; ctx.lineWidth = 0.9;
      ctx.beginPath(); ctx.moveTo(0, -sz * 0.85); ctx.lineTo(0, sz * 0.9); ctx.stroke();
      ctx.restore();
    }
    var LAYERS = [[1.1, 0.3], [0.9, 0.15], [0.7, 0]], i, j, n, x;    // back to front: [leaves per 10 px, shade]
    for (i = 0; i < LAYERS.length; i++) {
      n = Math.round(W / 10 * LAYERS[i][0]);
      for (j = 0; j < n; j++) {
        x = (j + rnd()) * (W + 20) / n - 10;                 // spread evenly, so the pile has no bare gaps
        var depth = Math.pow(rnd(), 0.8) * (x < 300 && !home ? 14 + 6 * (1 - x / 300) : 14);   // a little mound under the corner pumpkins
        leaf(x, H - depth + 1, 6 + rnd() * 6, rnd() * Math.PI * 2, PAL[(rnd() * PAL.length) | 0], rnd() < 0.5 ? 0 : (rnd() < 0.7 ? 2 : 1), LAYERS[i][1]);
      }
    }
  }
  body.insertBefore(bed, body.firstChild);
  drawBed();
  var dt = 0;
  window.addEventListener("resize", function () { clearTimeout(dt); dt = setTimeout(drawBed, 150); });

  var defsEl = document.createElement("div");
  defsEl.innerHTML = defs;
  body.insertBefore(defsEl.firstChild, body.firstChild);

  /* ---------- 2a. the homepage: beside the logo that is showing (the big one on wide screens, the h1 one on phones) ---------- */
  if (home) {
    var hero = patch("hw-pk-hero");
    body.appendChild(hero);
    var placeHero = function () {
      var big = document.querySelector(".brand-mark"), small = document.querySelector(".page > header h1 svg, .page > header h1 img");
      var r, left, bottom, w;
      if (big && big.getBoundingClientRect().height > 0) {
        r = big.getBoundingClientRect();                     // the mark sits in the middle of a wider box: 37% from its left, the caption ends at 82%
        left = r.left + r.width * 0.37; bottom = r.top + r.height * 0.82; w = 210;
      } else if (small && small.getBoundingClientRect().height > 0) {
        r = small.getBoundingClientRect();
        left = r.left + r.width / 2 - Math.min(r.width, r.height * 1.4) / 2; bottom = r.bottom; w = 104;
      } else { hero.style.display = "none"; return; }
      var gap = w > 150 ? 26 : 12, x = left - gap - w;
      if (x < 6) { w = left - gap - 6; x = 6; }
      if (w < 70) { hero.style.display = "none"; return; }
      hero.style.display = "";
      hero.style.width = Math.round(w) + "px";
      hero.style.left = Math.round(x + window.scrollX) + "px";
      hero.style.top = Math.round(bottom + window.scrollY - w * 130 / 240) + "px";
    };
    placeHero();
    window.addEventListener("load", placeHero);
    var ht = 0;
    window.addEventListener("resize", function () { clearTimeout(ht); ht = setTimeout(placeHero, 150); });
    return;
  }

  /* ---------- 2b. other pages: the bottom-left corner of the window, on the leaves ----------
     Sized to how wide that corner is before the first box that paints (a background, border, shadow, picture or
     control; fixed chrome and pointer-events:none decoration do not count), and left out below MIN: a pumpkin
     half-hidden behind a card looks broken. */
  var corner = patch("hw-pumpkins"), MIN = 96;
  body.insertBefore(corner, bed.nextSibling);
  function paints(els) {
    for (var i = 0; i < els.length; i++) {
      var e = els[i];
      if (e === body || e === document.documentElement) return false;
      if (/^(img|svg|canvas|video|input|button|select|textarea|iframe)$/i.test(e.tagName)) return true;
      var cs = getComputedStyle(e);
      if (cs.position === "fixed") continue;
      if (cs.backgroundImage !== "none" || !/^(transparent|rgba\(0, 0, 0, 0\))$/.test(cs.backgroundColor) ||
          parseFloat(cs.borderLeftWidth) > 0 || parseFloat(cs.borderTopWidth) > 0 || cs.boxShadow !== "none") return true;
    }
    return false;
  }
  function fit() {
    if (!document.elementsFromPoint) return;
    var H = window.innerHeight, free = window.innerWidth < 700 ? 150 : 230, ys = [H - 8, H - 40, H - 75, H - 110], i, x;
    for (i = 0; i < ys.length; i++) {
      for (x = 4; x < free + 12; x += 8) if (paints(document.elementsFromPoint(x, ys[i]))) { free = x - 12; break; }
    }
    corner.style.width = Math.max(0, free) + "px";
    corner.style.display = free < MIN ? "none" : "";
  }
  fit();
  window.addEventListener("load", fit);
  var ft = 0;
  window.addEventListener("resize", function () { clearTimeout(ft); ft = setTimeout(fit, 200); });
})();

/* ============================================================
   THANKSGIVING (2026-10-01) -- Monday to Friday of Thanksgiving week (the 4th Thursday of November;
   Nov 23-27 in 2026, computed every year by __themeKit), or ?theme=thanksgiving to preview.
   1. Autumn leaves, acorns and wheat drifting down behind the UI (kit.field; the leaf outline is the
      same kit.shapes.leaf the October leaves use). 2026-10-25: fewer of them, and the cursor scatter and
      the acorn cursor trail were removed (no mouse effects on any theme).
   2. Harvest confetti on quiz completion (window.__confettiColors) and the warm light-mode tint on the
      app-shell pages (body.thanksgiving-theme in theme.css, arcade.css, guides.html, group-join.html,
      group-host.html).
   prefers-reduced-motion: one still frame of the drift.
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
    cls: "th-thanks", dprCap: 1.5, reduced: "still", wrap: 20, fps: 30, rad: function (p) { return p.s * 2.4; },
    count: window.innerWidth < 700 ? 11 : 22,
    make: function (randomY) {
      var kind = KINDS[(Math.random() * KINDS.length) | 0], s = 6 + Math.random() * 6;
      var pal = kind === "leaf" ? LEAF : (kind === "acorn" ? NUT : GRAIN);
      return {
        kind: kind, x: Math.random() * window.innerWidth,
        y: randomY ? Math.random() * window.innerHeight : -10 - Math.random() * 40,
        s: s, speed: (0.3 + s * 0.05) * speedMul,
        drift: Math.random() * Math.PI * 2, driftSpeed: 0.008 + Math.random() * 0.014,
        spin: kind === "wheat" ? (Math.random() - 0.5) * 0.5 : Math.random() * Math.PI * 2,
        spinSpeed: kind === "wheat" ? 0 : (Math.random() - 0.5) * 0.03,
        opacity: 0.5 + Math.random() * 0.4, color: pal[(Math.random() * pal.length) | 0]
      };
    },
    move: function (p, k) {
      p.y += p.speed * k; p.drift += p.driftSpeed * k; p.x += Math.sin(p.drift) * 1.1 * k;
      if (p.kind !== "wheat") p.spin += p.spinSpeed * k;                            // wheat sways instead of tumbling
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
})();

// Seasonal St. Patrick's theme (added 2026-07-17, brought up to the Halloween standard 2026-10-01) -- Mar 3-17.
// Falling four-leaf clovers behind all UI, plus the green light-mode tint (body.stpatricks-theme).
//   - Clovers spin and tumble over as they fall (the width squashes and flips), and now and then one catches the
//     light with a little golden glint. 2026-10-25: fewer and slower-spinning, and the lucky-sparkle cursor trail
//     was removed (no mouse effects on any theme).
//   - Green and gold quiz-completion confetti. 30 fps, dirty-rect redraw, canvas capped at 2x, reduced motion:
//     one still frame.
(function () {
  var kit = window.__themeKit;
  if (!kit.on("clovers")) return;
  document.body.classList.add("stpatricks-theme");
  kit.colors(["#16a34a", "#22c55e", "#4ade80", "#fbbf24", "#15803d"]);
  var COLORS = ["#16a34a", "#22c55e", "#15803d", "#4ade80", "#166534"], speedMul = 0.35, F = null;
  F = kit.field({
    cls: "th-clovers", dprCap: 1.5, reduced: "still", wrap: 20, fps: 30,
    count: window.innerWidth < 700 ? 9 : 18,
    rad: function (c) { return c.s * 2.6; },
    make: function (randomY) {
      var s = 5 + Math.random() * 7;
      return {
        x: Math.random() * window.innerWidth,
        y: randomY ? Math.random() * window.innerHeight : -10 - Math.random() * 40,
        s: s, speed: (0.3 + s * 0.05) * speedMul,
        drift: Math.random() * Math.PI * 2, driftSpeed: 0.008 + Math.random() * 0.014,
        spin: Math.random() * Math.PI * 2, spinSpeed: (Math.random() - 0.5) * 0.03,
        flip: Math.random() * Math.PI * 2, flipSpeed: 0.015 + Math.random() * 0.02, glint: 0,
        opacity: 0.4 + Math.random() * 0.4, color: COLORS[(Math.random() * COLORS.length) | 0]
      };
    },
    move: function (c, k) {
      c.y += c.speed * k; c.drift += c.driftSpeed * k; c.spin += c.spinSpeed * k; c.flip += c.flipSpeed * k;
      c.x += Math.sin(c.drift) * 1.1 * k;
      if (c.glint > 0) c.glint -= k / 60;
    },
    gone: function (c) { return c.y > window.innerHeight + 24; },
    begin: function () {                                              // now and then one clover catches the light
      if (!F || Math.random() > 0.012) return;
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
})();

/* ============================================================
   PA WEEK (2026-09-30, Jaxon: "a theme for PA week ... Monday through Friday
   next week", "fun animations")
   ------------------------------------------------------------
   Active Mon 5 - Fri 9 October 2026 only (year-specific on purpose: move the dates each
   year), or on any page loaded with ?paweek=1 so it can be previewed outside the window.
   Same architecture as the other seasonal themes: lives here so every page gets it.
   1. A canvas of PA-themed things drifting UP like balloons behind the UI (hearts,
      stethoscopes, medical crosses, pills, little "PA" badges). 2026-10-25: fewer, and the
      cursor scatter and the medical-cross cursor trail were removed (no mouse effects).
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

  /* ---------- 1. the drifting shapes (kit.field: one canvas behind the UI, hidden-tab pause) ---------- */
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
      tilt: Math.random() * 6, opacity: 0.5 + Math.random() * 0.35
    };
  }
  kit.field({
    cls: "th-paweek", dprCap: 1.5, reduced: "still", wrap: 40, first: true, fps: 30,
    count: window.innerWidth < 700 ? 8 : 14,
    rad: function (p) { return p.s * 2.6; },
    make: make,
    move: function (p, k) { p.y -= p.speed * k; p.drift += p.driftSpeed * k; p.x += Math.sin(p.drift) * 0.9 * k; p.tilt += 0.012 * k; },
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
