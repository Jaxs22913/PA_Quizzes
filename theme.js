/* Anonymous usage counts (metrics.js, added 2026-10-10). Pages and features call
   PAMetrics.add("field") / .mark("name") / .family(name, spec) whenever something happens; until
   metrics.js has loaded, those calls wait in this queue and metrics.js replays them. The note text
   lives here too because the Settings panel (built before metrics.js loads) shows it as well. */
if (!window.PAMetrics) window.PAMetrics = (function () {
  var q = [];
  function later(name) { return function () { q.push([name, [].slice.call(arguments)]); }; }
  return { _q: q, add: later("add"), mark: later("mark"), family: later("family"),
           note: "PA Quizzes counts anonymous totals, like how many questions are answered, how often Pip is used and which pages run into errors, to improve the site and to support a future free version for students everywhere. No names or answers are recorded." };
})();

// Holiday animations (2026-10-25; the choice under Dark mode in Settings, and in the planner's and the relax page's
// settings). Jaxon: "turn off the stuff flying around in the themes", then "make a choose (Turn off Everywhere,
// Everywhere but homepage, or Turn off Just in Quizzes/guides)". localStorage "themeFx" holds the choice:
//   "on" (default) | "study" = off on quiz, guide, cram-sheet and other study pages (the app pages keep them: home,
//   Study Guides list, Arcade, planner, My Progress, group study) | "nothome" = off everywhere but the homepage | "off".
// Off stops everything in a seasonal theme that moves (falling and floating particles, fireworks, flicker, twinkle,
// pulse) and keeps the holiday tint and still decorations. The live state is the class th-fx-off on <html>, set here
// before any theme starts: theme-seasonal.js (kit.reduced()) and theme.css read it, so a change applies at once
// ("themefx" event on this page, the storage event in other tabs). Defined first in this file because the Settings
// panel is built during init(), which runs partway through it; the SEASON GATE further down needs it too.
window.ThemeFx = (function () {
  var root = document.documentElement;
  var CHOICES = [["on", "On everywhere"], ["study", "Off in quizzes and guides"], ["nothome", "Off except the homepage"], ["off", "Off everywhere"]];
  function valid(m) { for (var i = 0; i < CHOICES.length; i++) if (CHOICES[i][0] === m) return true; return false; }
  function mode() { var m = null; try { m = localStorage.getItem("themeFx"); } catch (e) {} return valid(m) ? m : "on"; }
  function isHome() { return (document.body && document.body.classList.contains("homepage")) || /\/(index\.html)?$/.test(location.pathname); }
  function isApp() { return isHome() || /\/(guides|calendar|progress|group-(join|host)|arcade[\w-]*)\.html$/.test(location.pathname); }
  function offHere(m) { return m === "off" || (m === "nothome" && !isHome()) || (m === "study" && !isApp()); }
  function paint() { root.classList.toggle("th-fx-off", offHere(mode())); }
  function fire() { try { window.dispatchEvent(new Event("themefx")); } catch (e) {} }
  paint();
  window.addEventListener("storage", function (e) { if (e.key === "themeFx" || e.key === null) { paint(); fire(); } });
  return {
    CHOICES: CHOICES,
    mode: mode,
    off: function () { return root.classList.contains("th-fx-off"); },
    set: function (m) {
      if (!valid(m)) m = "on";
      try { localStorage.setItem("themeFx", m); } catch (e) {}
      paint(); fire();
    }
  };
})();

/* Error pings (2026-10-19). A script error used to be invisible until a classmate texted Jaxon ("I press
   start the quiz and nothing happens"). Now each distinct error on a page view sends ONE request for
     <site>/_e/v1/<page kind>/<folder~page>/<file-line>/<message>
   -- a path that does not exist (a 404), so nothing is stored by the site: Cloudflare's own request analytics
   count the paths, and tools/error_report.py (daily, .github/workflows/site-errors.yml) reads them back.
   Never sent: names, ids, answers, query strings or page text (URLs and numbers in a message are blanked).
   At most 5 per page view. Same exclusions as metrics.js: usage counts turned off (metrics:off), a developer
   device (metrics:dev), automated browsers, and anywhere but pa-quizzes.com; ?errtest=1 lifts the last two for
   a live self-test. Errors from browser extensions and other sites' scripts (Firebase, analytics) and plain
   network failures are ignored. Quiz pages queue errors from before this file runs in window.__paErrQ
   (template.html <head>), which is drained here. */
(function () {
  var MAX = 5, n = 0, sent = {};
  var me = document.currentScript, base = me && me.src ? me.src.replace(/theme\.js(\?.*)?$/, "") : "";
  var test = /[?&]errtest=1(&|$)/.test(location.search);
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function off() {
    if (!base || get("metrics:off") === "1" || get("metrics:dev") === "1") return true;
    if (test) return false;
    if (navigator.webdriver || !/^https:$/.test(location.protocol)) return true;
    return !/(^|\.)pa-quizzes\.com$/.test(location.hostname);
  }
  var NOISE = /^(Script error\.?)$|ResizeObserver loop|Failed to fetch|NetworkError|Load failed|network ?error|AbortError|aborted|offline|firebase|firestore|auth\/|Quota|QuotaExceeded/i;
  function clean(s, max, keepDigits) {
    s = String(s || "").replace(/https?:\/\/\S+/g, "url");
    // Quoted text can carry what a student typed (a JSON.parse or selector error): keep a short code name
    // like 'length' or 'startExamModeTour', blank everything else in quotes.
    s = s.replace(/(["'`])([^"'`]*)\1/g, function (m, q, t) { return /^[A-Za-z_$][\w$.]{0,40}$/.test(t) ? m : q + q; });
    if (!keepDigits) s = s.replace(/\d+/g, "N");
    return s.replace(/[^A-Za-z0-9 _.$'()-]+/g, " ").trim().replace(/\s+/g, "-").slice(0, max) || "none";
  }
  function pageSeg() {
    var p = decodeURIComponent(location.pathname).replace(/^\/(PA_Quizzes\/)?/, "").replace(/\.html$/, "");
    var parts = p.split("/"), file = parts.pop() || "index";
    return (parts.length ? clean(parts.join("-"), 45, true).toLowerCase() + "~" : "") + clean(file, 55, true).toLowerCase();
  }
  function kind() {
    var b = document.body;
    if (!b) return "early";
    return b.getAttribute("data-dark-kind") || (b.classList.contains("homepage") ? "home" : document.getElementById("quiz") ? "quiz" : "page");
  }
  function report(msg, file, line) {
    try {
      if (n >= MAX || off() || NOISE.test(msg || "")) return;
      var here = location.origin + location.pathname;
      if (file && file.split(/[?#]/)[0] !== here && file.indexOf(location.origin + "/") !== 0) return;   // extension / another site
      var where = !file || file.split(/[?#]/)[0] === here ? "page" : file.split(/[?#]/)[0].split("/").pop();
      var segs = [kind(), pageSeg(), clean(where, 40, true) + "-" + (line | 0), clean(String(msg).replace(/^Uncaught\s+/, ""), 100)];
      var key = segs.join("|");
      if (sent[key]) return;
      sent[key] = 1; n++;
      new Image().src = base + "_e/v1/" + segs.map(encodeURIComponent).join("/");
    } catch (e) {}
  }
  function onError(e) {
    try {
      if (e && e.target && e.target !== window) return;   // a failed <img>/<script> load, not a script error
      report(e && (e.message || (e.error && e.error.message)), e && e.filename, e && e.lineno);
    } catch (x) {}
  }
  function onReject(e) {
    try {                                                  // a reason can be anything, even an object String() throws on
      var r = e && e.reason;
      report("promise: " + (r && r.message ? r.message : String(r)), r && r.fileName, r && r.lineNumber);
    } catch (x) {}
  }
  try {
    var q = window.__paErrQ;
    if (q && q.length) q.forEach(function (e) { e.type === "unhandledrejection" ? onReject(e) : onError(e); });
    if (q) q.done = true;
  } catch (x) {}
  window.addEventListener("error", onError);
  window.addEventListener("unhandledrejection", onReject);
  /* One ping when this device's storage is full (see STORAGE FULL below): sizes per key family only --
     "guideInk-1800k~qp-60k" -- never a key's text, so it says WHAT fills a student's iPad and nothing else. */
  window.__paStorageFullPing = function () {
    try {
      if (off()) return;
      var fam = {}, total = 0;
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i) || "", v = localStorage.getItem(k) || "";
        // the family is the site's own prefix before the first ":"; a key without one is never sent by name
        var f = k.indexOf(":") > 0 ? k.slice(0, k.indexOf(":")).replace(/[^A-Za-z0-9_]/g, "").slice(0, 20) || "other" : "other";
        fam[f] = (fam[f] || 0) + k.length + v.length; total += k.length + v.length;
      }
      var top = Object.keys(fam).sort(function (a, b) { return fam[b] - fam[a]; }).slice(0, 6)
        .map(function (f) { return f + "-" + Math.round(fam[f] / 1000) + "k"; }).join("~");
      new Image().src = base + "_e/v1/" + ["storagefull", pageSeg(), "total-" + Math.round(total / 1000) + "k", top].map(encodeURIComponent).join("/");
    } catch (e) {}
  };
})();

/* STORAGE FULL (2026-10-20). Safari keeps about 5 MB (2.5 million characters) of localStorage per site. A
   classmate's iPad filled it, and from then on every save threw QuotaExceededError -- including the one
   cloud-sync.js makes when "Start the quiz" clears the old progress, so Start did nothing (it worked in a
   private window, which starts empty). A full device now keeps working: a save that does not fit is skipped,
   the student is told once per page, and one anonymous ping says which kind of data filled it. Installed here,
   before cloud-sync.js loads, so its own patch builds on this one and none of its writes can throw either. */
(function () {
  var S, real;
  try { S = Storage.prototype; real = S.setItem; } catch (e) { return; }
  if (!real || real.__paSafe) return;
  var told = false;
  function isQuota(e) {
    return !!e && (e.name === "QuotaExceededError" || e.name === "NS_ERROR_DOM_QUOTA_REACHED" || e.code === 22 || e.code === 1014);
  }
  function full() {
    if (told) return;
    told = true;
    setTimeout(function () {
      try { if (window.showToast) window.showToast("This device’s storage for PA Quizzes is full, so new progress and notes are not being saved here right now. Everything else still works.", 9000); } catch (e) {}
      try { if (window.__paStorageFullPing) window.__paStorageFullPing(); } catch (e) {}
    }, 0);
  }
  // safeSetItem.failed says whether the LAST call was skipped: cloud-sync.js checks it so a value that never
  // landed is not marked as changed, pushed over the cloud copy, or reloaded for.
  function safeSetItem(key, value) {
    safeSetItem.failed = false;
    try { return real.call(this, key, value); }
    catch (e) { if (!isQuota(e)) throw e; safeSetItem.failed = true; full(); }
  }
  safeSetItem.__paSafe = true;
  S.setItem = safeSetItem;
})();

/* ============================================================
   Site icon set (design review item 14, 2026-09-25). ONE source for UI
   chrome icons, drawn for this site: 24px grid, 2px round-capped stroke,
   currentColor, no fills except tiny dots. Replaces the text glyphs
   (flag, three-line menu, pause bars, stars, arrows) and emoji (controller,
   flame, people, trophy...) that rendered differently on every OS and never
   matched the stroke icons the corner buttons already used.
     window.SiteIcon("flag", 15)  ->  '<svg class="si si-flag" ...>'
   Content emoji (Group Study avatars chosen by students) are not chrome and
   are left alone.
   ============================================================ */
window.SiteIcon = (function () {
  var P = {
    flag: '<path d="M5.5 21V4"/><path d="M5.5 4.6c3.8-2 7.2 2 11 0v8.2c-3.8 2-7.2-2-11 0"/>',
    grid: '<rect x="4" y="4" width="6.5" height="6.5" rx="1.6"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="1.6"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="1.6"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="1.6"/>',
    pause: '<rect x="6.5" y="5" width="3.6" height="14" rx="1.2"/><rect x="13.9" y="5" width="3.6" height="14" rx="1.2"/>',
    arrowLeft: '<path d="M19 12H5"/><path d="M11 18l-6-6 6-6"/>',
    arrowRight: '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>',
    external: '<path d="M14 4h6v6"/><path d="M20 4l-9 9"/><path d="M18 14v4.5a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 4 18.5v-11A1.5 1.5 0 0 1 5.5 6H10"/>',
    list: '<path d="M9 6.5h11M9 12h11M9 17.5h11"/><path d="M4.5 6.5h.01M4.5 12h.01M4.5 17.5h.01" stroke-width="2.6"/>',
    flame: '<path d="M12 3c1 3.2 5 5.4 5 10.2a5 5 0 0 1-10 0c0-2.3 1.1-3.7 2.3-4.9.2 1.7 1 2.8 2.2 3.2-.2-3.1-.1-5.6.5-8.5z"/>',
    users: '<circle cx="9" cy="8.5" r="3.3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><path d="M15.5 5.3a3.3 3.3 0 0 1 0 6.4"/><path d="M17.5 14.4c2 .8 3.5 2.9 3.5 5.6"/>',
    timer: '<circle cx="12" cy="13.5" r="7.5"/><path d="M12 10v3.6l2.4 1.6"/><path d="M9.5 2.8h5"/>',
    cup: '<path d="M4.5 9h12v4.5a5 5 0 0 1-5 5h-2a5 5 0 0 1-5-5z"/><path d="M16.5 10.5h1.2a2.6 2.6 0 0 1 0 5.2h-1.4"/><path d="M8.5 3.5v2.5M12.5 3.5v2.5"/>',
    check: '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    checkCircle: '<circle cx="12" cy="12" r="9"/><path d="M8 12.4l2.8 2.8L16.2 9.6"/>',
    xCircle: '<circle cx="12" cy="12" r="9"/><path d="M9.2 9.2l5.6 5.6M14.8 9.2l-5.6 5.6"/>',
    x: '<path d="M6.5 6.5l11 11M17.5 6.5l-11 11"/>',
    trophy: '<path d="M8 4h8v5.5a4 4 0 0 1-8 0z"/><path d="M8 6H5.5a2.5 2.5 0 0 0 2.6 4M16 6h2.5a2.5 2.5 0 0 1-2.6 4"/><path d="M12 13.5V17M8.5 20.5h7M10 17h4"/>',
    book: '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v14.5H6.5A2.5 2.5 0 0 0 4 20z"/><path d="M4 20a1.5 1.5 0 0 0 1.5 1.5H20V17.5"/>',
    star: '<path d="M12 3.6l2.6 5.2 5.8.9-4.2 4.1 1 5.7L12 16.8l-5.2 2.7 1-5.7-4.2-4.1 5.8-.9z"/>',
    gamepad: '<rect x="2.5" y="7" width="19" height="11" rx="5.5"/><path d="M7.5 10.8v3.4M5.8 12.5h3.4"/><path d="M15.5 11.3h.01M17.8 13.6h.01" stroke-width="2.6"/>',
    medal: '<path d="M8.5 3h7l-2.2 7M8.5 3l2.2 7"/><circle cx="12" cy="15.5" r="5.5"/>',
    calendar: '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
    layers: '<path d="M12 3.5l8.5 4.5-8.5 4.5L3.5 8z"/><path d="M3.5 12.2l8.5 4.5 8.5-4.5"/><path d="M3.5 16.2l8.5 4.5 8.5-4.5"/>',
    play: '<path d="M7 4.8v14.4a.8.8 0 0 0 1.2.7l11.6-7.2a.8.8 0 0 0 0-1.4L8.2 4.1A.8.8 0 0 0 7 4.8z"/>',
    snow: '<path d="M12 3v18M4.2 7.5l15.6 9M19.8 7.5l-15.6 9"/><path d="M9.5 4.5L12 6.5l2.5-2M9.5 19.5L12 17.5l2.5 2"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    sliders: '<path d="M4 7h9M17 7h3M4 17h3M11 17h9"/><circle cx="15" cy="7" r="2.2"/><circle cx="9" cy="17" r="2.2"/>',
    target: '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1" stroke-width="2.6"/>',
    clock: '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
    download: '<path d="M12 4v11"/><path d="M7.5 11l4.5 4.5 4.5-4.5"/><path d="M5 19.5h14"/>',
    chart: '<path d="M4.5 19.5h15"/><path d="M7 19.5v-6M12 19.5V7M17 19.5v-9"/>',
    refresh: '<path d="M19.5 12a7.5 7.5 0 0 1-13 5"/><path d="M4.5 12a7.5 7.5 0 0 1 13-5"/><path d="M17.5 3.5V7H14M6.5 20.5V17H10"/>',
    moon: '<path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/>',
    help: '<circle cx="12" cy="12" r="9"/><path d="M9.6 9.4a2.5 2.5 0 1 1 3.5 2.3c-.7.4-1.1.9-1.1 1.7"/><path d="M12 17h.01" stroke-width="2.6"/>'
  };
  return function (name, size, extraClass) {
    size = size || 16;
    return '<svg class="si si-' + name + (extraClass ? " " + extraClass : "") + '" width="' + size + '" height="' + size +
      '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">' +
      (P[name] || "") + "</svg>";
  };
})();

/* One prompt at a time (design review item 3, 2026-09-25). A first-time
   visitor used to get the sign-in modal AND the install banner together on the
   homepage, and the tour modal AND a controller toast together on their first
   quiz. Two rules now:
     - the two "asks" (install the app, sign in) never share a visit: whichever
       claims the visit first wins, the other waits for a later visit;
     - nothing opens while another prompt is already on screen.
   sessionStorage is the "visit". home.js runs before this file, but only calls
   in from timers that fire after it has loaded, and it guards on the global. */
window.SitePrompts = {
  claim: function (name) {
    var c = null;
    try { c = sessionStorage.getItem("sitePromptThisVisit"); } catch (e) {}
    if (c && c !== name) return false;
    try { sessionStorage.setItem("sitePromptThisVisit", name); } catch (e) {}
    return true;
  },
  anyOpen: function () {
    return !!document.querySelector(".tour-overlay.open, .tour-spotlight, .install-banner.show");
  }
};

(function () {
  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }

  function validate(steps) {
    return steps.filter(function (s) { return !s.selector || document.querySelector(s.selector); });
  }

  // The running spotlight/tooltip does not block clicks to the rest of the
  // page (the "want a tour?" prompt does, until it is answered or tapped
  // away), so two tours can otherwise be
  // triggered back to back (e.g. the page-load quiz tour is still up when
  // Exam Mode's own tour fires moments later) and stack visually on top of
  // each other. One flag, shared across every start()/run() call site,
  // keeps only one tour on screen at a time -- a second call while one is
  // already showing is just a no-op rather than a second overlay.
  var active = false;

  function start(steps, storageKey) {
    if (active || localStorage.getItem(storageKey)) return;
    // Another prompt is already up: leave the tour unseen so it offers itself
    // on the next load instead of stacking on top.
    if (window.SitePrompts.anyOpen()) return;
    var validSteps = validate(steps);
    if (!validSteps.length) return;
    active = true;
    showPrompt(validSteps, storageKey);
  }

  function run(steps, storageKey, onDone) {
    if (active) return;
    var validSteps = validate(steps);
    if (!validSteps.length) return;
    active = true;
    runSteps(validSteps, storageKey, onDone);
  }

  function showPrompt(steps, storageKey) {
    var overlay = el("div", "tour-overlay open");
    var card = el("div", "tour-prompt");
    card.appendChild(el("p", "tour-prompt-title", "Want a quick tour?"));
    card.appendChild(el("p", "tour-prompt-text", "Takes about 30 seconds — shows you where the useful stuff lives."));
    var actions = el("div", "tour-prompt-actions");
    var skipBtn = el("button", "tour-btn", "Skip");
    skipBtn.type = "button";
    var goBtn = el("button", "tour-btn primary", "Take the tour");
    goBtn.type = "button";
    actions.appendChild(skipBtn);
    actions.appendChild(goBtn);
    card.appendChild(actions);
    overlay.appendChild(card);
    document.body.appendChild(overlay);

    // Close first, then remember: a save that fails (a full device) must
    // never leave the prompt covering the page.
    function skip() {
      overlay.remove();
      document.removeEventListener("keydown", onKey);
      active = false;
      try { localStorage.setItem(storageKey, "1"); } catch (e) {}
    }
    function onKey(e) { if (e.key === "Escape") skip(); }
    skipBtn.addEventListener("click", skip);
    // A tap on the dimmed page around the card counts as Skip.
    overlay.addEventListener("click", function (e) { if (e.target === overlay) skip(); });
    document.addEventListener("keydown", onKey);
    goBtn.addEventListener("click", function () {
      overlay.remove();
      document.removeEventListener("keydown", onKey);
      runSteps(steps, storageKey);
    });
  }

  function runSteps(steps, storageKey, onDone) {
    var i = 0;
    var spotlight = el("div", "tour-spotlight");
    var tooltip = el("div", "tour-tooltip");
    document.body.appendChild(spotlight);
    document.body.appendChild(tooltip);

    function finish() {
      spotlight.remove();
      tooltip.remove();
      window.removeEventListener("resize", place);
      active = false;
      try { localStorage.setItem(storageKey, "1"); } catch (e) {}
      if (onDone) { try { onDone(); } catch (e) {} }
    }

    function place() {
      var step = steps[i];
      // A step may switch the page to where its target lives (tabs) before it is measured.
      if (step.before) { try { step.before(); } catch (e) {} }
      var target = step.selector ? document.querySelector(step.selector) : null;
      var r = null;
      if (target) {
        // 'instant' so a page with smooth scrolling is measured after the jump, not mid-scroll.
        try { target.scrollIntoView({ block: "center", behavior: "instant" }); }
        catch (e) { target.scrollIntoView({ block: "center" }); }
        r = target.getBoundingClientRect();
        var pad = 8;
        spotlight.style.display = "block";
        spotlight.style.top = (r.top - pad) + "px";
        spotlight.style.left = (r.left - pad) + "px";
        spotlight.style.width = (r.width + pad * 2) + "px";
        spotlight.style.height = (r.height + pad * 2) + "px";
      } else {
        spotlight.style.display = "none";
      }

      tooltip.innerHTML =
        '<p class="tour-tooltip-step">Step ' + (i + 1) + ' of ' + steps.length + '</p>' +
        '<p class="tour-tooltip-title">' + step.title + '</p>' +
        '<p class="tour-tooltip-text">' + step.text + '</p>' +
        '<div class="tour-tooltip-actions">' +
          '<button type="button" class="tour-btn" id="tour-skip">Skip tour</button>' +
          '<span style="flex:1"></span>' +
          (i > 0 ? '<button type="button" class="tour-btn" id="tour-back">Back</button>' : '') +
          '<button type="button" class="tour-btn primary" id="tour-next">' + (i === steps.length - 1 ? "Done" : "Next") + '</button>' +
        '</div>';

      // Placed after the content exists so the real size is used: beside/below the target
      // when it fits, above it otherwise, and always fully on screen (also centred when
      // the step has no target).
      var tw = tooltip.offsetWidth, th = tooltip.offsetHeight, vw = window.innerWidth, vh = window.innerHeight;
      if (r) {
        var tipTop = r.bottom + 16;
        if (tipTop + th > vh - 12) tipTop = r.top - th - 16;
        if (tipTop < 12) tipTop = vh - th - 12;
        tooltip.style.top = tipTop + "px";
        tooltip.style.left = Math.max(12, Math.min(r.left, vw - tw - 12)) + "px";
      } else {
        tooltip.style.top = Math.max(12, (vh - th) / 2) + "px";
        tooltip.style.left = Math.max(12, (vw - tw) / 2) + "px";
      }

      document.getElementById("tour-skip").addEventListener("click", finish);
      var backBtn = document.getElementById("tour-back");
      if (backBtn) backBtn.addEventListener("click", function () { i--; place(); });
      document.getElementById("tour-next").addEventListener("click", function () {
        if (i === steps.length - 1) { finish(); return; }
        i++; place();
      });
    }

    window.addEventListener("resize", place);
    place();
  }

  window.SiteTour = { start: start, run: run };
})();

(function () {
  var SUN = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>';
  var MOON = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  var REFRESH = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 4 23 10 17 10"/><polyline points="1 20 1 14 7 14"/><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>';
  var PDF_ICON = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>';
  var WORD_ICON = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><path d="M8.5 12.5 10 18l2-4 2 4 1.5-5.5"/></svg>';
  var KEYBOARD = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M6 9h.01M10 9h.01M14 9h.01M18 9h.01M6 13h.01M18 13h.01M8 13h8"/></svg>';
  var GEAR = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>';
  var ARROW_LEFT = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg>';
  var CALC = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="11" x2="8" y2="11.01"/><line x1="12" y1="11" x2="12" y2="11.01"/><line x1="16" y1="11" x2="16" y2="11.01"/><line x1="8" y1="15" x2="8" y2="15.01"/><line x1="12" y1="15" x2="12" y2="15.01"/><line x1="16" y1="15" x2="16" y2="15.01"/><line x1="8" y1="19" x2="8" y2="19.01"/><line x1="12" y1="19" x2="12" y2="19.01"/><line x1="16" y1="19" x2="16" y2="19.01"/></svg>';
  var MORE_ICON = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="5" cy="12" r="1.2"/><circle cx="12" cy="12" r="1.2"/><circle cx="19" cy="12" r="1.2"/></svg>';
  var TIMER = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l3 2"/><path d="M9 2h6"/></svg>';

  function currentTheme() {
    return document.documentElement.getAttribute("data-theme") || "light";
  }
  function paintIcon(btn, theme) {
    btn.innerHTML = theme === "dark" ? SUN : MOON;
  }
  function setTheme(theme, btn) {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("siteTheme", theme);
    if (btn) paintIcon(btn, theme);
  }
  function setTextSize(large) {
    document.documentElement.setAttribute("data-text-size", large ? "large" : "normal");
    localStorage.setItem("textSize", large ? "large" : "normal");
  }
  function setContrast(high) {
    document.documentElement.setAttribute("data-contrast", high ? "high" : "normal");
    localStorage.setItem("contrast", high ? "high" : "normal");
  }
  function initHaptics() {
    if (!("vibrate" in navigator)) return;
    document.addEventListener("click", function (e) {
      if (localStorage.getItem("haptics") !== "1") return;
      var el = e.target.closest && e.target.closest(".opt, .choice");
      if (el) navigator.vibrate(15);
    });
  }

  // Sound effects (added 2026-07-10), same zero-per-quiz-file delegated-click
  // pattern as initHaptics above -- default off, toggled in the settings
  // panel. Synthesized with the Web Audio API (short oscillator tones)
  // rather than shipping audio files, so there's nothing to fetch and it
  // works offline. AudioContext is created lazily on first actual play
  // (always from inside a real click handler) so it starts in a valid,
  // already-user-gestured state instead of "suspended" by autoplay policy.
  //
  // The tone engine itself (getCtx/tone/SOUNDS/playSound) is hoisted to this
  // outer scope and exposed as window.playSiteSound so pages outside the
  // shared quiz engine -- currently group-host.html/group-join.html, which
  // don't have the #shuffle-toggle this file uses to detect "is this a quiz
  // page" and so never call initSoundEffects() below -- can still play the
  // same sounds through the same "soundEffects" localStorage toggle, instead
  // of duplicating this whole engine.
  var audioCtx = null;
  function getCtx() {
    if (!audioCtx) {
      var AC = window.AudioContext || window.webkitAudioContext;
      if (!AC) return null;
      audioCtx = new AC();
    }
    if (audioCtx.state === "suspended") audioCtx.resume();
    return audioCtx;
  }
  function tone(ctx, freq, startTime, duration, type, peakGain) {
    var osc = ctx.createOscillator();
    var gain = ctx.createGain();
    osc.type = type || "sine";
    osc.frequency.value = freq;
    var t0 = ctx.currentTime + startTime;
    gain.gain.setValueAtTime(0, t0);
    gain.gain.linearRampToValueAtTime(peakGain || 0.12, t0 + 0.008);
    gain.gain.exponentialRampToValueAtTime(0.0001, t0 + duration);
    osc.connect(gain).connect(ctx.destination);
    osc.start(t0);
    osc.stop(t0 + duration + 0.02);
  }
  /* Filtered noise burst. Every other sound here is a pure oscillator, which
     can make a chime but not a crack -- a firework is mostly noise, so it
     needs a buffer of random samples pushed through a bandpass. */
  function noise(ctx, startTime, duration, centreHz, peakGain, sweepToHz) {
    var frames = Math.max(1, Math.floor(ctx.sampleRate * duration));
    var buf = ctx.createBuffer(1, frames, ctx.sampleRate);
    var data = buf.getChannelData(0);
    for (var i = 0; i < frames; i++) {
      // taper the tail so the burst decays instead of stopping dead
      data[i] = (Math.random() * 2 - 1) * (1 - i / frames);
    }
    var src = ctx.createBufferSource();
    src.buffer = buf;
    var filter = ctx.createBiquadFilter();
    filter.type = "bandpass";
    filter.Q.value = 0.8;
    var gain = ctx.createGain();
    var t0 = ctx.currentTime + startTime;
    filter.frequency.setValueAtTime(centreHz, t0);
    if (sweepToHz) filter.frequency.exponentialRampToValueAtTime(sweepToHz, t0 + duration);
    gain.gain.setValueAtTime(0, t0);
    gain.gain.linearRampToValueAtTime(peakGain, t0 + 0.01);
    gain.gain.exponentialRampToValueAtTime(0.0001, t0 + duration);
    src.connect(filter).connect(gain).connect(ctx.destination);
    src.start(t0);
    src.stop(t0 + duration + 0.02);
  }

  var SOUNDS = {
    select: function (ctx) { tone(ctx, 700, 0, 0.05, "sine", 0.07); },
    correct: function (ctx) {
      tone(ctx, 880, 0, 0.09, "sine", 0.12);
      tone(ctx, 1318.5, 0.08, 0.14, "sine", 0.12);
    },
    wrong: function (ctx) { tone(ctx, 170, 0, 0.18, "sine", 0.12); },
    complete: function (ctx) {
      [523.25, 659.25, 783.99, 1046.5].forEach(function (freq, i) {
        tone(ctx, freq, i * 0.11, i === 3 ? 0.24 : 0.12, "sine", 0.12);
      });
    },
    join: function (ctx) { tone(ctx, 990, 0, 0.06, "sine", 0.08); },
    tick: function (ctx) { tone(ctx, 520, 0, 0.035, "square", 0.04); },
    reveal: function (ctx) {
      tone(ctx, 440, 0, 0.07, "triangle", 0.09);
      tone(ctx, 660, 0.06, 0.12, "triangle", 0.1);
    },
    podium: function (ctx) {
      [523.25, 659.25, 783.99, 1046.5, 1318.5].forEach(function (freq, i) {
        tone(ctx, freq, i * 0.1, i === 4 ? 0.35 : 0.12, "sine", 0.13);
      });
    },
    /* Firework: a rising whistle, the crack of the shell, then the crackle of
       the sparks trailing off. Three parts because two just sounds like a
       thud -- the tail is what makes it read as fireworks rather than a door
       slamming. Kept quieter than the quiz sounds since several can overlap. */
    firework: function (ctx) {
      var launch = ctx.createOscillator();
      var lg = ctx.createGain();
      var t0 = ctx.currentTime;
      launch.type = "sine";
      launch.frequency.setValueAtTime(420, t0);
      launch.frequency.exponentialRampToValueAtTime(1150, t0 + 0.32);
      lg.gain.setValueAtTime(0.0001, t0);
      lg.gain.exponentialRampToValueAtTime(0.05, t0 + 0.18);
      lg.gain.exponentialRampToValueAtTime(0.0001, t0 + 0.34);
      launch.connect(lg).connect(ctx.destination);
      launch.start(t0);
      launch.stop(t0 + 0.36);

      tone(ctx, 110, 0.34, 0.28, "sine", 0.11);              // the shell going off
      noise(ctx, 0.34, 0.22, 1400, 0.10, 500);               // the crack
      noise(ctx, 0.46, 0.85, 2600, 0.045, 1200);             // sparks trailing
    }
  };
  function playSound(name) {
    if (localStorage.getItem("soundEffects") !== "1") return;
    try {
      var ctx = getCtx();
      if (ctx && SOUNDS[name]) SOUNDS[name](ctx);
    } catch (e) {}
  }
  window.playSiteSound = playSound;

  // Quiz-completion celebration (added 2026-07-17). Confetti piece/keyframe
  // CSS lives in theme.css (ported from arcade.css's existing win-screen
  // confetti, since quiz pages don't load arcade.css). Every quiz template
  // family (see the results-scoring research from this session) renders its
  // percentage as literal "NN%" text somewhere inside #results -- Pattern A's
  // #finalPct, Pattern B's .ring <b>, Pattern C's #pct, Pattern D's .scoresub
  // -- so scraping #results.textContent with a plain regex works across all
  // of them without needing per-template special-casing or touching any of
  // the ~440 individual quiz files.
  /* `spread` is how many seconds the pieces are released over. The default
     0.3 is the original snap-burst, right for a quiz result where the whole
     celebration is over in a moment. Pass something longer for a shower that
     keeps falling -- at 0.3 every piece is in the air at once, which reads as
     one clump dropping rather than confetti.

     Cleanup has to account for it: the fixed 3.2s timeout was fine when
     nothing started later than 0.3s in, but a piece released at 2s would
     otherwise be yanked out of the air mid-fall. */
  function burstConfetti(count, spread) {
    var colors = window.__confettiColors || ["#2563eb", "#16a34a", "#9333ea", "#f59e0b", "#dc2626"];
    var release = typeof spread === "number" ? spread : 0.3;
    var lifetime = (release + 3.2) * 1000;
    for (var i = 0; i < count; i++) {
      (function () {
        var piece = document.createElement("div");
        piece.className = "confetti-piece";
        piece.style.left = Math.random() * 100 + "vw";
        piece.style.background = colors[i % colors.length];
        piece.style.animationDuration = (1.6 + Math.random() * 1.6) + "s";
        piece.style.animationDelay = (Math.random() * release) + "s";
        // a little size variation so a wide spread does not read as rows of
        // identical tickets
        var scale = 0.75 + Math.random() * 0.6;
        piece.style.width = (8 * scale).toFixed(1) + "px";
        piece.style.height = (14 * scale).toFixed(1) + "px";
        document.body.appendChild(piece);
        setTimeout(function () { piece.remove(); }, lifetime);
      })();
    }
  }
  /* Exposed so the homepage's first-day-of-semester celebration can reuse it
     rather than carry a second copy of the same effect. Note the load order:
     home.js is deferred BEFORE theme.js, so anything in home.js must wait for
     DOMContentLoaded before reaching for this. */
  window.burstConfetti = burstConfetti;

  function celebrateScore(results) {
    var match = results.textContent.match(/(\d{1,3})\s*%/);
    var pct = match ? parseInt(match[1], 10) : NaN;
    if (pct === 100) {
      playSound("podium");
      burstConfetti(70);
    } else if (pct >= 75) {
      playSound("complete");
      burstConfetti(30);
    } else {
      playSound("complete");
    }
  }

  function initSoundEffects() {
    document.addEventListener("click", function (e) {
      var opt = e.target.closest && e.target.closest(".opt, .choice");
      if (!opt) return;
      if (opt.classList.contains("correct")) playSound("correct");
      else if (opt.classList.contains("wrong")) playSound("wrong");
      else playSound("select");
    });

    // #results becoming visible is the one truly universal "quiz finished"
    // signal across every family (see feedback_quiz_progress_tracking) --
    // watched generically via MutationObserver instead of a per-file hook,
    // checking computed style so it catches both class-based and inline-
    // style-based hidden/shown toggling.
    var announcedResults = new WeakSet();
    var resultsObserver = new MutationObserver(function () {
      var results = document.getElementById("results");
      if (!results || announcedResults.has(results)) return;
      if (getComputedStyle(results).display !== "none") {
        announcedResults.add(results);
        celebrateScore(results);
        // cloud-sync.js offers sign-in here, on the first finished quiz.
        try { window.dispatchEvent(new CustomEvent("quizResultsShown")); } catch (err) {}
      }
    });
    resultsObserver.observe(document.body, { attributes: true, attributeFilter: ["class", "style"], subtree: true });
  }
  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }
  function makeCornerBtn(id, label) {
    var btn = document.createElement("button");
    btn.type = "button";
    btn.id = id;
    btn.className = "corner-btn";
    btn.setAttribute("aria-label", label);
    btn.title = label;
    return btn;
  }

  var SHORTCUT_ROWS = [
    ["Select an answer", "1", "2", "3", "4"],
    ["Next question", "Enter", "→"],
    ["Previous question", "←"],
    ["Controller: select answer", "A", "B", "X", "Y"],
    ["Controller: next / back", "RB", "LB"],
    ["Show this help", "?"],
    ["Close this help", "Esc"]
  ];

  var QUIZ_TOUR_STEPS = [
    {
      selector: "#shuffle-toggle",
      title: "Shuffle question order",
      text: "Turn this on before you start to answer questions in a random order each attempt — handy once you've mostly memorized the fixed order."
    },
    {
      selector: "#shortcuts-btn",
      title: "Keyboard shortcuts",
      text: "Click here — or press ? anytime — to see the shortcuts for picking, advancing and going back. Once you start, a live timer shows up next to it too, and it pauses automatically whenever you close the page."
    }
  ];

  // Shown once, the first time a quiz page actually enters Exam Mode (not
  // at page load like QUIZ_TOUR_STEPS above -- #flagbtn/#navbtn are hidden
  // until then, and a tour step pointing at a hidden element looks broken).
  // Each quiz's own applyExamModeUI() calls window.startExamModeTour()
  // when examMode is true; this is the one shared place the step content
  // and its own "seen" flag live, instead of duplicating both per file.
  var EXAM_MODE_TOUR_STEPS = [
    {
      selector: "#flagbtn",
      title: "Flag questions",
      text: "Mark any question to come back to later — flagged questions are highlighted in the question grid."
    },
    {
      selector: "#navbtn",
      title: "Jump between questions",
      text: "See every question at a glance, jump to any of them in any order, and submit your exam from here once you're done."
    }
  ];
  window.startExamModeTour = function () {
    if (window.SiteTour) window.SiteTour.start(EXAM_MODE_TOUR_STEPS, "tourSeen:exammode");
  };

  // Guide/study-aid pages call this from a sticky .guide-back-bar link (see
  // theme.css) instead of the generic scroll-gated #corner-actions-left
  // button, since guides specifically need to hop back to guides.html to
  // pick a different guide without the button being hidden until scrolled.
  // Real "previous page" when there is one (matches how someone actually
  // got here, e.g. from guides.html); falls back to a guaranteed link to
  // guides.html when there's no same-origin referrer to go back to (opened
  // directly / no browsing history) so the button is never a dead end.
  window.guideGoBack = function () {
    if (document.referrer && document.referrer.indexOf(location.origin) === 0) {
      history.back();
    } else {
      location.href = "../guides.html";
    }
  };

  function initShortcutsHelp() {
    if (!document.getElementById("timerpill")) return null;

    var overlay = document.createElement("div");
    overlay.className = "shortcuts-overlay";
    overlay.id = "shortcuts-overlay";

    var panel = document.createElement("div");
    panel.className = "shortcuts-panel";

    var closeBtn = document.createElement("button");
    closeBtn.type = "button";
    closeBtn.className = "shortcuts-close";
    closeBtn.setAttribute("aria-label", "Close");
    closeBtn.innerHTML = "&times;";

    var heading = document.createElement("h3");
    heading.textContent = "Keyboard shortcuts";

    panel.appendChild(closeBtn);
    panel.appendChild(heading);

    SHORTCUT_ROWS.forEach(function (row) {
      var rowEl = document.createElement("div");
      rowEl.className = "shortcuts-row";
      var label = document.createElement("span");
      label.textContent = row[0];
      var keys = document.createElement("span");
      keys.className = "shortcuts-keys";
      for (var i = 1; i < row.length; i++) {
        var kbd = document.createElement("kbd");
        kbd.textContent = row[i];
        keys.appendChild(kbd);
      }
      rowEl.appendChild(label);
      rowEl.appendChild(keys);
      panel.appendChild(rowEl);
    });

    var guideLink = document.createElement("button");
    guideLink.type = "button";
    guideLink.className = "shortcuts-guide-link";
    guideLink.textContent = "Need a guide? Take the tour →";
    panel.appendChild(guideLink);

    overlay.appendChild(panel);
    document.body.appendChild(overlay);

    function open() { overlay.classList.add("open"); }
    function close() { overlay.classList.remove("open"); }
    function toggle() {
      if (overlay.classList.contains("open")) close(); else open();
    }

    guideLink.addEventListener("click", function () {
      close();
      if (window.SiteTour && document.getElementById("shuffle-toggle")) {
        window.SiteTour.run(QUIZ_TOUR_STEPS, "tourSeen:quiz");
      }
    });
    closeBtn.addEventListener("click", close);
    overlay.addEventListener("click", function (e) { if (e.target === overlay) close(); });
    document.addEventListener("keydown", function (e) {
      if (e.ctrlKey || e.metaKey || e.altKey) return;
      var tag = (e.target && e.target.tagName) || "";
      if (tag === "INPUT" || tag === "TEXTAREA") return;
      if (e.key === "?") { e.preventDefault(); toggle(); return; }
      if (e.key === "Escape" && overlay.classList.contains("open")) close();
    });

    return { open: open };
  }

  function makeToggleRow(label, checked, onChange) {
    var row = document.createElement("div");
    row.className = "settings-row";

    var span = document.createElement("span");
    span.textContent = label;

    var switchLabel = document.createElement("label");
    switchLabel.className = "settings-switch";
    var input = document.createElement("input");
    input.type = "checkbox";
    input.checked = checked;
    var track = document.createElement("span");
    track.className = "track";
    var thumb = document.createElement("span");
    thumb.className = "thumb";
    switchLabel.appendChild(input);
    switchLabel.appendChild(track);
    switchLabel.appendChild(thumb);

    input.addEventListener("change", function () { onChange(input.checked); });

    row.appendChild(span);
    row.appendChild(switchLabel);
    return { row: row, input: input };
  }

  function makeActionRow(label, onClick) {
    var row = document.createElement("div");
    row.className = "settings-row quick-action";

    var span = document.createElement("span");
    span.textContent = label;

    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "settings-action-btn";
    btn.textContent = "Open";
    btn.addEventListener("click", onClick);

    row.appendChild(span);
    row.appendChild(btn);
    return row;
  }

  function initSettingsPanel() {
    var overlay = document.createElement("div");
    overlay.className = "settings-overlay";
    overlay.id = "settings-overlay";

    var panel = document.createElement("div");
    panel.className = "settings-panel";

    var closeBtn = document.createElement("button");
    closeBtn.type = "button";
    closeBtn.className = "shortcuts-close";
    closeBtn.setAttribute("aria-label", "Close");
    closeBtn.innerHTML = "&times;";

    var heading = document.createElement("h3");
    heading.textContent = "Settings";

    panel.appendChild(closeBtn);
    panel.appendChild(heading);

    // Quick actions: #refresh-btn/#theme-toggle-btn/#calc-btn/#pomo-btn/
    // #account-btn are always hidden now (see theme.css) -- Settings,
    // Search, Your highlights, and Draw are the only tools that stay as
    // standalone corner icons, everything else lives here instead. These
    // rows are wired by literally delegating to the still-fully-functional
    // -but-hidden buttons (except dark mode, which calls setTheme/
    // paintIcon directly since this row is the *only* way to toggle it now,
    // so there's no other place its state could drift out of sync from).
    // Arcade pages (detected by their edge-decor marquee *dots* -- index.html
    // also has its own unrelated, dot-free ".edge-decor" zigzag strips, so
    // matching on ".edge-decor circle" specifically is what tells the two
    // apart) want their Settings panel identical to the homepage's, right
    // down to #refresh-btn staying a visible standalone icon there instead
    // of living in this panel -- see the matching arcade.css override. The
    // one addition is a Sound effects row: Arcade dropped its own corner
    // sound-toggle icon (see arcade.js's initHeader), so this panel is now
    // the only place to flip arcade.js's fc_sound_v1 flag, same as Dark
    // mode is the only place to flip the site's theme.
    var isArcade = !!document.querySelector(".edge-decor circle");

    var darkModeToggle = makeToggleRow(
      "Dark mode",
      currentTheme() === "dark",
      function (checked) {
        setTheme(checked ? "dark" : "light");
        var tBtn = document.getElementById("theme-toggle-btn");
        if (tBtn) paintIcon(tBtn, checked ? "dark" : "light");
      }
    );
    darkModeToggle.row.classList.add("quick-action");
    panel.appendChild(darkModeToggle.row);

    // Holiday animations (2026-10-25, Jaxon: "turn off the stuff flying around in the themes ... put it in all the
    // settings and make it easy to find", then a choice of where): second row, right under Dark mode, on every page
    // and every day, not only while a theme runs (a setting you can reach only during Halloween week is one nobody
    // finds). window.ThemeFx (top of this file) applies it at once on this page and in other open tabs.
    if (window.ThemeFx) {
      var fxRow = document.createElement("div");
      fxRow.className = "settings-row quick-action has-note";
      var fxLabel = document.createElement("label");
      fxLabel.textContent = "Holiday animations";
      fxLabel.htmlFor = "settings-themefx";
      var fxSelect = document.createElement("select");
      fxSelect.id = "settings-themefx";
      fxSelect.className = "settings-select";
      window.ThemeFx.CHOICES.forEach(function (c) {
        var o = document.createElement("option");
        o.value = c[0]; o.textContent = c[1];
        fxSelect.appendChild(o);
      });
      fxSelect.value = window.ThemeFx.mode();
      fxSelect.addEventListener("change", function () { window.ThemeFx.set(fxSelect.value); });
      window.addEventListener("themefx", function () { fxSelect.value = window.ThemeFx.mode(); });
      fxRow.appendChild(fxLabel);
      fxRow.appendChild(fxSelect);
      panel.appendChild(fxRow);
      var fxNote = document.createElement("p");
      fxNote.className = "settings-note";
      fxNote.textContent = "Snow, falling leaves, floating hearts, fireworks, flickering pumpkins and other moving holiday effects. Off keeps the holiday colors.";
      panel.appendChild(fxNote);
    }

    if (isArcade) {
      var soundToggle = makeToggleRow(
        "Sound effects",
        localStorage.getItem("fc_sound_v1") !== "0",
        function (checked) {
          if (window.setFCSoundEnabled) window.setFCSoundEnabled(checked);
        }
      );
      soundToggle.row.classList.add("quick-action");
      panel.appendChild(soundToggle.row);
    }

    // setTimeout(...,0) defers the delegated click until after this click
    // event's own bubble phase finishes -- calc/account both have their own
    // document-level "click outside closes this" listener, and firing the
    // delegated click synchronously means the *original* click event (whose
    // target is this row's button, not something inside the calc/account
    // panel) is still bubbling and reaches that listener right after,
    // reading the panel as freshly-opened-but-clicked-outside and closing
    // it again in the same tick.
    panel.appendChild(makeActionRow("Calculator", function () {
      close();
      setTimeout(function () {
        var b = document.getElementById("calc-btn");
        if (b) b.click();
      }, 0);
    }));
    panel.appendChild(makeActionRow("Study timer", function () {
      close();
      setTimeout(function () {
        var b = document.getElementById("pomo-btn");
        if (b) b.click();
      }, 0);
    }));
    // #refresh-btn stays a visible icon on the homepage, Arcade, and the
    // guides page (see theme.css / arcade.css) -- skip the quick-action row
    // on those so it isn't offered in two places.
    if (!document.body.classList.contains("homepage") && !isArcade &&
        !document.body.classList.contains("guides-page")) {
      panel.appendChild(makeActionRow("Refresh / check for updates", function () {
        var b = document.getElementById("refresh-btn");
        if (b) b.click();
      }));
    }
    panel.appendChild(makeActionRow("Account / sign in", function () {
      close();
      setTimeout(function () {
        var b = document.getElementById("account-btn");
        if (b) b.click();
      }, 0);
    }));

    var textSizeToggle = makeToggleRow(
      "Larger text",
      localStorage.getItem("textSize") === "large",
      function (checked) { setTextSize(checked); }
    );
    panel.appendChild(textSizeToggle.row);

    var contrastToggle = makeToggleRow(
      "High contrast",
      localStorage.getItem("contrast") === "high",
      function (checked) { setContrast(checked); }
    );
    panel.appendChild(contrastToggle.row);

    // Hides what the class picked beside each option, and the "You vs the class"
    // panel on the results screen. UNGATED ON PURPOSE (Jaxon, 2026-09-08: "add
    // the mute class stats to all page settings buttons"). It first shipped
    // gated on #shuffle-toggle so it only appeared where it had something to
    // hide, but that meant the switch could not be found from the homepage or a
    // guide -- and a preference you can only change from inside the thing it
    // affects is a preference people cannot find. It is a stored flag, so
    // flipping it anywhere holds everywhere until it is flipped back.
    var classStatsToggle = makeToggleRow(
      "Hide class statistics",
      localStorage.getItem("hideClassStats") === "1",
      function (checked) {
        if (window.ClassStats && window.ClassStats.setHidden) {
          window.ClassStats.setHidden(checked);
        } else {
          try { localStorage.setItem("hideClassStats", checked ? "1" : "0"); } catch (e) {}
        }
      }
    );
    panel.appendChild(classStatsToggle.row);

    // Anonymous usage counts (metrics.js, 2026-10-10): the permanent home of the one-time note, on every
    // page, with the same switch. Turning it off is a stored flag ("metrics:off") that metrics.js and
    // class-stats.js check before counting anything; it follows the account through cloud sync.
    var usageToggle = makeToggleRow(
      "Count my use in anonymous totals",
      localStorage.getItem("metrics:off") !== "1",
      function (checked) {
        if (window.PAMetrics && window.PAMetrics.setOff) window.PAMetrics.setOff(!checked);
        else { try { localStorage.setItem("metrics:off", checked ? "0" : "1"); } catch (e) {} }
      }
    );
    usageToggle.row.classList.add("has-note");
    panel.appendChild(usageToggle.row);
    var usageNote = document.createElement("p");
    usageNote.className = "settings-note";
    usageNote.textContent = (window.PAMetrics && window.PAMetrics.note) || "";
    if (localStorage.getItem("metrics:dev") === "1") usageNote.textContent += " This is a developer device: nothing here is counted.";
    panel.appendChild(usageNote);

    if (document.getElementById("shuffle-toggle")) {
      var shuffleToggle = makeToggleRow(
        "Shuffle questions by default",
        localStorage.getItem("defaultShuffle") === "1",
        function (checked) { localStorage.setItem("defaultShuffle", checked ? "1" : "0"); }
      );
      panel.appendChild(shuffleToggle.row);

      if ("vibrate" in navigator) {
        var hapticsToggle = makeToggleRow(
          "Haptic feedback",
          localStorage.getItem("haptics") === "1",
          function (checked) { localStorage.setItem("haptics", checked ? "1" : "0"); }
        );
        panel.appendChild(hapticsToggle.row);
      }

      var soundToggle = makeToggleRow(
        "Sound effects",
        localStorage.getItem("soundEffects") === "1",
        function (checked) { localStorage.setItem("soundEffects", checked ? "1" : "0"); }
      );
      panel.appendChild(soundToggle.row);

    }

    // Exam Mode: no per-question feedback until a real submit, free
    // navigation, flagging, a question-jump grid. Opt-in per quiz page via
    // #exam-mode-toggle existing at all (same gating pattern as shuffle).
    if (document.getElementById("exam-mode-toggle")) {
      var examModeToggle = makeToggleRow(
        "Exam Mode by default",
        localStorage.getItem("examModeDefault") === "1",
        function (checked) { localStorage.setItem("examModeDefault", checked ? "1" : "0"); }
      );
      panel.appendChild(examModeToggle.row);

      var hardCutoffToggle = makeToggleRow(
        "Hard time limit by default (1 min/question)",
        localStorage.getItem("hardCutoffDefault") === "1",
        function (checked) { localStorage.setItem("hardCutoffDefault", checked ? "1" : "0"); }
      );
      panel.appendChild(hardCutoffToggle.row);
    }

    // Shared highlights (opt-in, added 2026-07-14) -- OFF by default,
    // unlike "who's studying now" presence, which is automatic for any
    // signed-in user with no toggle at all. Highlighting itself (position +
    // color, never the note text) is materially more personal than an
    // anonymous "someone's here" heartbeat, so this got its own explicit
    // opt-in per product decision -- see feedback_presence memory. Only
    // shown on guide pages at all, matching every other guide-only toggle's
    // gating convention in this panel (shuffle/exam-mode above check for
    // their own quiz-only trigger elements the same way).
    if (document.querySelector(".guide-back-bar")) {
      var shareHlToggle = makeToggleRow(
        "Share my highlights with other students (anonymously)",
        localStorage.getItem("shareHighlights") === "1",
        function (checked) {
          localStorage.setItem("shareHighlights", checked ? "1" : "0");
          window.dispatchEvent(new Event("shareHighlightsChanged"));
        }
      );
      panel.appendChild(shareHlToggle.row);
    }

    overlay.appendChild(panel);
    document.body.appendChild(overlay);

    function open() { overlay.classList.add("open"); }
    function close() { overlay.classList.remove("open"); }

    closeBtn.addEventListener("click", close);
    overlay.addEventListener("click", function (e) { if (e.target === overlay) close(); });

    return { open: open };
  }

  // Basic four-function calculator, available on every page (quiz or
  // practicum, timed or not) since students may want it regardless of
  // whether a given quiz happens to involve calculations. Deliberately a
  // small non-blocking floating panel near the corner button rather than a
  // full-screen overlay like Settings/Shortcuts -- it needs to stay usable
  // side-by-side with the question, not cover it.
  //
  // To extend to a scientific mode later: add entries to CALC_BINARY_OPS
  // (two-argument, applied via chooseOp/equals the same way +/-/x/div
  // already are) or CALC_UNARY_OPS (one-argument, applied immediately to
  // the current display value -- wire a button the same way the digit/op
  // buttons below are wired, calling applyUnary(CALC_UNARY_OPS[key])) and
  // add the corresponding <button> to .calc-grid. No other changes needed.
  function initCalculator() {
    var CALC_BINARY_OPS = {
      "+": function (a, b) { return a + b; },
      "−": function (a, b) { return a - b; },
      "×": function (a, b) { return a * b; },
      "÷": function (a, b) { return b === 0 ? NaN : a / b; }
    };
    var CALC_UNARY_OPS = {
      // Reserved for a future scientific mode, e.g.:
      // "√": function (x) { return Math.sqrt(x); },
    };

    var overlay = el("div", "calc-overlay");
    var panel = el("div", "calc-panel");

    var header = el("div", "calc-header");
    var title = el("span", null, "Calculator");
    var closeBtn = el("button", "calc-close", "&times;");
    closeBtn.type = "button";
    closeBtn.setAttribute("aria-label", "Close calculator");
    header.appendChild(title);
    header.appendChild(closeBtn);

    // Draggable by its header, like a lightweight floating window. Moves the
    // fixed-positioned overlay itself (not the panel inside it) by switching
    // from the default top/right CSS anchor to explicit left/top px once a
    // drag starts; clamped to stay fully on-screen. Position persists across
    // close/reopen for free since overlay is only hidden (display:none via
    // the .open class toggle), never removed/recreated.
    (function makeDraggable() {
      var dragging = false, startX, startY, startLeft, startTop;
      header.addEventListener("pointerdown", function (e) {
        if (e.target.closest(".calc-close")) return;
        dragging = true;
        var r = overlay.getBoundingClientRect();
        startLeft = r.left; startTop = r.top;
        startX = e.clientX; startY = e.clientY;
        overlay.style.left = startLeft + "px";
        overlay.style.top = startTop + "px";
        overlay.style.right = "auto";
        header.setPointerCapture(e.pointerId);
      });
      header.addEventListener("pointermove", function (e) {
        if (!dragging) return;
        var newLeft = startLeft + (e.clientX - startX);
        var newTop = startTop + (e.clientY - startY);
        newLeft = Math.max(4, Math.min(window.innerWidth - overlay.offsetWidth - 4, newLeft));
        newTop = Math.max(4, Math.min(window.innerHeight - overlay.offsetHeight - 4, newTop));
        overlay.style.left = newLeft + "px";
        overlay.style.top = newTop + "px";
      });
      header.addEventListener("pointerup", function () { dragging = false; });
      header.addEventListener("pointercancel", function () { dragging = false; });
    })();

    var display = el("div", "calc-display", "0");
    display.id = "calc-display";

    var grid = el("div", "calc-grid");
    var ROWS = [
      [{ t: "C", action: "clear", cls: "calc-fn" }, { t: "⌫", action: "back", cls: "calc-fn" }, { t: "÷", op: "÷", cls: "calc-op" }, { t: "×", op: "×", cls: "calc-op" }],
      [{ t: "7", d: "7" }, { t: "8", d: "8" }, { t: "9", d: "9" }, { t: "−", op: "−", cls: "calc-op" }],
      [{ t: "4", d: "4" }, { t: "5", d: "5" }, { t: "6", d: "6" }, { t: "+", op: "+", cls: "calc-op" }],
      [{ t: "1", d: "1" }, { t: "2", d: "2" }, { t: "3", d: "3" }, { t: "=", action: "equals", cls: "calc-eq", rowspan: 2 }],
      [{ t: "0", d: "0", cls: "calc-zero", colspan: 2 }, { t: ".", d: "." }]
    ];
    ROWS.forEach(function (row) {
      row.forEach(function (spec) {
        var btn = el("button", "calc-btn" + (spec.cls ? " " + spec.cls : ""), spec.t);
        btn.type = "button";
        if (spec.d != null) btn.dataset.digit = spec.d;
        if (spec.op) btn.dataset.op = spec.op;
        if (spec.action) btn.dataset.action = spec.action;
        if (spec.colspan) btn.style.gridColumn = "span " + spec.colspan;
        if (spec.rowspan) btn.style.gridRow = "span " + spec.rowspan;
        grid.appendChild(btn);
      });
    });

    panel.appendChild(header);
    panel.appendChild(display);
    panel.appendChild(grid);
    overlay.appendChild(panel);
    document.body.appendChild(overlay);

    var current = "0", pending = null, pendingOp = null, justEvaluated = false;

    function render() { display.textContent = current; }

    function formatResult(n) {
      if (!isFinite(n)) return "Error";
      var rounded = Math.round(n * 1e10) / 1e10;
      return String(rounded);
    }
    function inputDigit(d) {
      if (justEvaluated) { current = "0"; justEvaluated = false; }
      if (d === ".") {
        if (current.indexOf(".") !== -1) return;
        current += ".";
      } else if (current === "0") {
        current = d;
      } else {
        current += d;
      }
      render();
    }
    function clearAll() {
      current = "0"; pending = null; pendingOp = null; justEvaluated = false;
      render();
    }
    function backspace() {
      if (justEvaluated) { clearAll(); return; }
      current = current.length > 1 ? current.slice(0, -1) : "0";
      render();
    }
    function chooseOp(op) {
      if (pendingOp != null && !justEvaluated) equals();
      pending = parseFloat(current);
      pendingOp = op;
      justEvaluated = false;
      current = "0";
    }
    function equals() {
      if (pendingOp == null || pending == null) return;
      var result = CALC_BINARY_OPS[pendingOp](pending, parseFloat(current));
      current = formatResult(result);
      pending = null; pendingOp = null; justEvaluated = true;
      render();
    }
    function applyUnary(fn) {
      current = formatResult(fn(parseFloat(current)));
      justEvaluated = true;
      render();
    }

    grid.addEventListener("click", function (e) {
      var btn = e.target.closest(".calc-btn");
      if (!btn) return;
      if (btn.dataset.digit != null) inputDigit(btn.dataset.digit);
      else if (btn.dataset.op) chooseOp(btn.dataset.op);
      else if (btn.dataset.action === "clear") clearAll();
      else if (btn.dataset.action === "back") backspace();
      else if (btn.dataset.action === "equals") equals();
    });

    function isOpen() { return overlay.classList.contains("open"); }
    function toggle() { overlay.classList.toggle("open"); }
    function close() { overlay.classList.remove("open"); }

    closeBtn.addEventListener("click", close);
    document.addEventListener("click", function (e) {
      if (!isOpen()) return;
      if (panel.contains(e.target) || e.target.closest("#calc-btn")) return;
      close();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && isOpen()) close();
    });

    return { toggle: toggle };
  }

  // Study session timer (Pomodoro-style, added 2026-07-14). Same
  // shared-widget pattern as the calculator above -- fully local, zero
  // per-page changes, works on any page (quiz, guide, or homepage). State
  // is keyed by an absolute end-timestamp rather than a plain countdown a
  // setInterval ticks down, so navigating to a different page or a full
  // reload never loses time: remaining time is always `endsAt - Date.now()`,
  // recomputed fresh on every load and every tick, the same trick the
  // quiz-family timers already use for their own pause/resume.
  function initPomodoro() {
    var STATE_KEY = "pomodoroState";
    var DEFAULTS = { phase: "idle", running: false, endsAt: null, remainingMs: null, focusMin: 25, breakMin: 5, completedSessions: 0 };

    function loadState() {
      var s;
      try { s = JSON.parse(localStorage.getItem(STATE_KEY)); } catch (e) { s = null; }
      var out = {};
      for (var k in DEFAULTS) out[k] = (s && s[k] !== undefined) ? s[k] : DEFAULTS[k];
      return out;
    }
    function saveState() { localStorage.setItem(STATE_KEY, JSON.stringify(state)); }

    var state = loadState();

    var overlay = el("div", "pomo-overlay");
    var panel = el("div", "pomo-panel");

    var header = el("div", "pomo-header");
    var title = el("span", null, "Study Timer");
    var closeBtn = el("button", "pomo-close", "&times;");
    closeBtn.type = "button";
    closeBtn.setAttribute("aria-label", "Close study timer");
    header.appendChild(title);
    header.appendChild(closeBtn);

    // Draggable by its header -- identical mechanics to the calculator's own
    // makeDraggable() above (see that comment for why left/top instead of
    // the default top/right anchor, and why clamping is needed).
    (function makeDraggable() {
      var dragging = false, startX, startY, startLeft, startTop;
      header.addEventListener("pointerdown", function (e) {
        if (e.target.closest(".pomo-close")) return;
        dragging = true;
        var r = overlay.getBoundingClientRect();
        startLeft = r.left; startTop = r.top;
        startX = e.clientX; startY = e.clientY;
        overlay.style.left = startLeft + "px";
        overlay.style.top = startTop + "px";
        overlay.style.right = "auto";
        header.setPointerCapture(e.pointerId);
      });
      header.addEventListener("pointermove", function (e) {
        if (!dragging) return;
        var newLeft = startLeft + (e.clientX - startX);
        var newTop = startTop + (e.clientY - startY);
        newLeft = Math.max(4, Math.min(window.innerWidth - overlay.offsetWidth - 4, newLeft));
        newTop = Math.max(4, Math.min(window.innerHeight - overlay.offsetHeight - 4, newTop));
        overlay.style.left = newLeft + "px";
        overlay.style.top = newTop + "px";
      });
      header.addEventListener("pointerup", function () { dragging = false; });
      header.addEventListener("pointercancel", function () { dragging = false; });
    })();

    var phaseLabel = el("div", "pomo-phase");
    var display = el("div", "pomo-display", "25:00");
    display.id = "pomo-display";

    var controlsRow = el("div", "pomo-controls");
    var startBtn = el("button", "pomo-action-btn primary", "Start");
    startBtn.type = "button";
    var pauseBtn = el("button", "pomo-action-btn", "Pause");
    pauseBtn.type = "button";
    var resetBtn = el("button", "pomo-action-btn", "Reset");
    resetBtn.type = "button";
    controlsRow.appendChild(startBtn);
    controlsRow.appendChild(pauseBtn);
    controlsRow.appendChild(resetBtn);

    var settingsRow = el("div", "pomo-settings");
    var focusField = el("label", "pomo-field", "Focus");
    var focusInput = document.createElement("input");
    focusInput.type = "number";
    focusInput.min = "1";
    focusInput.max = "120";
    focusInput.id = "pomo-focus-min";
    focusField.appendChild(focusInput);
    focusField.appendChild(document.createTextNode(" min"));
    var breakField = el("label", "pomo-field", "Break");
    var breakInput = document.createElement("input");
    breakInput.type = "number";
    breakInput.min = "1";
    breakInput.max = "60";
    breakInput.id = "pomo-break-min";
    breakField.appendChild(breakInput);
    breakField.appendChild(document.createTextNode(" min"));
    settingsRow.appendChild(focusField);
    settingsRow.appendChild(breakField);

    var sessionsLabel = el("div", "pomo-sessions");

    panel.appendChild(header);
    panel.appendChild(phaseLabel);
    panel.appendChild(display);
    panel.appendChild(controlsRow);
    panel.appendChild(settingsRow);
    panel.appendChild(sessionsLabel);
    overlay.appendChild(panel);
    document.body.appendChild(overlay);

    focusInput.value = state.focusMin;
    breakInput.value = state.breakMin;
    focusInput.addEventListener("change", function () {
      var v = Math.max(1, Math.min(120, parseInt(focusInput.value, 10) || DEFAULTS.focusMin));
      focusInput.value = v;
      state.focusMin = v;
      saveState();
      render();
    });
    breakInput.addEventListener("change", function () {
      var v = Math.max(1, Math.min(60, parseInt(breakInput.value, 10) || DEFAULTS.breakMin));
      breakInput.value = v;
      state.breakMin = v;
      saveState();
    });

    // Persistent mini-pill -- separate from the panel, visible on EVERY page
    // (not just while the panel happens to be open) whenever a session is
    // actively running, so the countdown is glanceable without reopening the
    // panel each time, the same reason quizzes show #timerpill during an
    // attempt instead of only inside a menu.
    var pill = el("button", "pomo-pill", "");
    pill.type = "button";
    pill.setAttribute("aria-label", "Study timer running — click to open");
    document.body.appendChild(pill);

    function fmt(ms) {
      var totalSec = Math.max(0, Math.ceil(ms / 1000));
      var m = Math.floor(totalSec / 60), s = totalSec % 60;
      return (m < 10 ? "0" : "") + m + ":" + (s < 10 ? "0" : "") + s;
    }
    function phaseTotalMs() { return (state.phase === "break" ? state.breakMin : state.focusMin) * 60000; }
    function remainingMs() {
      if (state.running && state.endsAt) return state.endsAt - Date.now();
      if (state.remainingMs != null) return state.remainingMs;
      return phaseTotalMs();
    }

    function render() {
      var rem = Math.max(0, remainingMs());
      display.textContent = fmt(rem);
      var label = state.phase === "focus" ? "Focus" : state.phase === "break" ? "Break" : "Ready to focus";
      phaseLabel.textContent = label;
      sessionsLabel.textContent = state.completedSessions > 0
        ? state.completedSessions + " focus session" + (state.completedSessions === 1 ? "" : "s") + " completed"
        : "";
      startBtn.textContent = (state.phase !== "idle" && !state.running) ? "Resume" : "Start";
      startBtn.style.display = state.running ? "none" : "";
      pauseBtn.style.display = state.running ? "" : "none";
      resetBtn.style.display = state.phase !== "idle" ? "" : "none";
      focusInput.disabled = state.phase !== "idle";
      breakInput.disabled = state.phase !== "idle";

      if (state.running) {
        pill.classList.add("visible");
        pill.innerHTML = window.SiteIcon(state.phase === "break" ? "cup" : "timer", 14) + " " + fmt(rem);
        pill.classList.toggle("pomo-pill-break", state.phase === "break");
      } else {
        pill.classList.remove("visible");
      }
    }

    var tickTimer = null;
    function startTicking() {
      stopTicking();
      tickTimer = setInterval(function () {
        if (!state.running) { stopTicking(); return; }
        if (remainingMs() <= 0) { advancePhase(); return; }
        render();
      }, 1000);
    }
    function stopTicking() {
      if (tickTimer) { clearInterval(tickTimer); tickTimer = null; }
    }

    // Focus -> break auto-advances (the whole point of the technique is not
    // having to remember to take the break yourself). Break -> idle does
    // NOT auto-restart another focus round -- silently looping forever while
    // someone stepped away would be a worse outcome than just stopping and
    // waiting for an explicit "Start" again.
    function advancePhase() {
      if (state.phase === "focus") {
        state.completedSessions++;
        state.phase = "break";
        state.running = true;
        state.endsAt = Date.now() + state.breakMin * 60000;
        state.remainingMs = null;
        saveState();
        if (window.playSiteSound) window.playSiteSound("complete");
        if (window.showToast) window.showToast("Focus session done — take a " + state.breakMin + "-minute break.", 5000);
        startTicking();
      } else {
        state.phase = "idle";
        state.running = false;
        state.endsAt = null;
        state.remainingMs = null;
        saveState();
        if (window.playSiteSound) window.playSiteSound("reveal");
        if (window.showToast) window.showToast("Break's over — ready for another focus session?", 5000);
        stopTicking();
      }
      render();
    }

    function start() {
      state.endsAt = Date.now() + (state.phase === "idle" ? state.focusMin * 60000 : (state.remainingMs != null ? state.remainingMs : phaseTotalMs()));
      if (state.phase === "idle") state.phase = "focus";
      state.running = true;
      state.remainingMs = null;
      saveState();
      startTicking();
      render();
    }
    function pause() {
      state.remainingMs = Math.max(0, remainingMs());
      state.running = false;
      state.endsAt = null;
      saveState();
      stopTicking();
      render();
    }
    function reset() {
      state.phase = "idle";
      state.running = false;
      state.endsAt = null;
      state.remainingMs = null;
      saveState();
      stopTicking();
      render();
    }

    startBtn.addEventListener("click", start);
    pauseBtn.addEventListener("click", pause);
    resetBtn.addEventListener("click", reset);
    pill.addEventListener("click", open);

    function isOpen() { return overlay.classList.contains("open"); }
    function open() { overlay.classList.add("open"); render(); }
    function toggle() { if (isOpen()) close(); else open(); }
    function close() { overlay.classList.remove("open"); }

    closeBtn.addEventListener("click", close);
    document.addEventListener("click", function (e) {
      if (!isOpen()) return;
      if (panel.contains(e.target) || e.target.closest("#pomo-btn") || e.target === pill) return;
      close();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && isOpen()) close();
    });

    // Catch up on load if a session was left running in a tab/browser that's
    // since been fully closed and reopened (setInterval doesn't survive
    // that) -- a single advancePhase() call, not a fast-forwarding loop
    // through however many phases elapsed during the gap, since exact
    // catch-up accuracy doesn't matter for a casual study timer and a loop
    // here risks looping forever on a very long absence.
    if (state.running && remainingMs() <= 0) {
      advancePhase();
    } else if (state.running) {
      startTicking();
    }
    render();

    return { toggle: toggle };
  }

  function init() {
    document.documentElement.setAttribute("data-text-size", localStorage.getItem("textSize") === "large" ? "large" : "normal");
    document.documentElement.setAttribute("data-contrast", localStorage.getItem("contrast") === "high" ? "high" : "normal");

    var group = document.createElement("div");
    group.id = "corner-actions";

    var refreshBtn = makeCornerBtn("refresh-btn", "Refresh / check for updates");
    refreshBtn.innerHTML = REFRESH;
    refreshBtn.addEventListener("click", function () {
      if ("serviceWorker" in navigator && navigator.serviceWorker.getRegistrations) {
        navigator.serviceWorker.getRegistrations()
          .then(function (regs) { return Promise.all(regs.map(function (r) { return r.update(); })); })
          .catch(function () {})
          .then(function () { location.reload(); });
      } else {
        location.reload();
      }
    });

    var themeBtn = makeCornerBtn("theme-toggle-btn", "Toggle dark mode");
    paintIcon(themeBtn, currentTheme());
    themeBtn.addEventListener("click", function () {
      setTheme(currentTheme() === "dark" ? "light" : "dark", themeBtn);
    });

    var settingsHelp = initSettingsPanel();
    var settingsBtn = makeCornerBtn("settings-btn", "Settings");
    settingsBtn.innerHTML = GEAR;
    settingsBtn.addEventListener("click", settingsHelp.open);
    group.appendChild(settingsBtn);

    var calcHelp = initCalculator();
    var calcBtn = makeCornerBtn("calc-btn", "Calculator");
    calcBtn.innerHTML = CALC;
    calcBtn.addEventListener("click", calcHelp.toggle);
    group.appendChild(calcBtn);

    var pomoHelp = initPomodoro();
    var pomoBtn = makeCornerBtn("pomo-btn", "Study timer");
    pomoBtn.innerHTML = TIMER;
    pomoBtn.addEventListener("click", pomoHelp.toggle);
    group.appendChild(pomoBtn);

    group.appendChild(refreshBtn);
    group.appendChild(themeBtn);

    // Download-as-PDF button -- only on guides & study aids (study guides,
    // cram sheets, reference sheets), gated on .guide-back-bar exactly like
    // the guide's other tools (never on quizzes/homepage). Uses the browser's
    // print-to-PDF; @media print rules (theme.css) strip the page chrome for a
    // clean export, and we force light theme for the print so dark-mode users
    // still get a readable, ink-friendly PDF, then restore their theme after.
    if (document.querySelector(".guide-back-bar")) {
      var pdfBtn = makeCornerBtn("pdf-btn", "Download as PDF");
      pdfBtn.innerHTML = PDF_ICON;

      // LAZY IMAGES DO NOT SURVIVE THE EXPORT. Measured 2026-08-20 on the
      // Anatomy Exam 3 guide, which carries 87 figures: on load only the two
      // in the opening viewport have decoded, and neither window.print() nor
      // switching to print media loads the rest -- the counts stay at 2. A
      // reader who lands on a guide and taps this button without scrolling the
      // whole page gets a 108-page PDF containing two pictures. Flipping every
      // lazy image to eager loads all 87.
      //
      // So the images are warmed BEFORE printing rather than made eager in the
      // markup, because eager markup would pull 9.3 MB on every page view to
      // serve the much rarer export. Warm-up starts on hover or touch, which
      // is usually enough on its own; the click path below covers the case
      // where it is not.
      function warmPrintImages() {
        var imgs = [].slice.call(document.images);
        var pending = imgs.filter(function (i) { return !i.complete || !i.naturalWidth; });
        pending.forEach(function (i) {
          if (i.loading === "lazy") i.loading = "eager";
          if (!i.complete) i.src = i.src;   // nudge one already past the lazy gate
        });
        return pending;
      }
      function printImagesReady() {
        return [].slice.call(document.images).every(function (i) {
          return i.complete && i.naturalWidth > 0;
        });
      }
      ["pointerenter", "touchstart", "focus"].forEach(function (evt) {
        pdfBtn.addEventListener(evt, function () { warmPrintImages(); },
                                { passive: true, once: true });
      });

      pdfBtn.addEventListener("click", function () {
        var root = document.documentElement;

        function doPrint() {
          // Back to the resting look: once the figures are in, every later tap
          // takes the fast path and the button should stop advertising a wait.
          pdfBtn.classList.remove("is-preparing", "is-ready");
          pdfBtn.title = "Download as PDF";
          pdfBtn.setAttribute("aria-label", pdfBtn.title);
          var prev = root.getAttribute("data-theme");
          var done = false;
          function restore() {
            if (done) return;
            done = true;
            if (prev) root.setAttribute("data-theme", prev);
            else root.removeAttribute("data-theme");
            window.removeEventListener("afterprint", restore);
          }
          window.addEventListener("afterprint", restore);
          // CRITICAL: window.print() must run SYNCHRONOUSLY inside the tap
          // gesture -- iOS Safari silently ignores a print() call deferred out
          // of the user-activation context (a setTimeout here broke it on
          // mobile). Set the light theme synchronously first (print() flushes
          // styles, so it's reflected), then print; afterprint restores the
          // theme, with a fallback timeout for browsers that don't fire it.
          root.setAttribute("data-theme", "light");
          window.print();
          setTimeout(restore, 1000);
        }

        if (printImagesReady()) { doPrint(); return; }

        // Images still loading. We cannot await them and then print, because
        // that leaves the gesture and iOS drops the call -- so tell the reader
        // what is happening and arm the next tap, which will be in-gesture and
        // instant. Better one extra tap than a PDF with no pictures in it.
        var pending = warmPrintImages();
        pdfBtn.classList.add("is-preparing");
        pdfBtn.title = "Preparing " + pending.length + " images\u2026";
        pdfBtn.setAttribute("aria-label", pdfBtn.title);
        var left = pending.length, settled = false;
        function ready() {
          if (settled) return;
          settled = true;
          pdfBtn.classList.remove("is-preparing");
          pdfBtn.classList.add("is-ready");
          pdfBtn.title = "Images ready \u2014 tap to download the PDF";
          pdfBtn.setAttribute("aria-label", pdfBtn.title);
          // Desktop keeps working in one tap: doPrint() opens the dialog and
          // resets the button. iOS ignores a print() this far out of the tap
          // gesture, so there the ready cue is what the reader sees and the
          // second tap -- now in-gesture, with every figure decoded -- is the
          // one that exports.
          doPrint();
        }
        pending.forEach(function (i) {
          function tick() { if (--left <= 0) ready(); }
          i.addEventListener("load", tick, { once: true });
          i.addEventListener("error", tick, { once: true });
        });
        setTimeout(ready, 15000);   // never leave the button stuck
      });
      group.appendChild(pdfBtn);

      // Download-as-Word -- an EDITABLE copy, for classmates who want to change
      // things. Gated on the page advertising one:
      //   <link rel="alternate" type="...wordprocessingml.document" href="...">
      // which tools/build_guide_docx.py writes only for Semester 2 and later.
      // Self-gating on purpose: no link, no button, so a guide outside that
      // scope can never show a control that 404s, and there is no second list
      // of filenames to keep in sync.
      var docxLink = document.querySelector(
        'link[rel="alternate"][type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"]');
      if (docxLink && docxLink.getAttribute("href")) {
        var wordBtn = document.createElement("a");
        wordBtn.id = "word-btn";
        wordBtn.className = "corner-btn";
        wordBtn.href = docxLink.getAttribute("href");
        wordBtn.setAttribute("download", "");
        wordBtn.title = "Download as Word (editable)";
        wordBtn.setAttribute("aria-label", wordBtn.title);
        wordBtn.innerHTML = WORD_ICON;
        group.appendChild(wordBtn);
      }
    }

    // ONE TOOLBAR on guides and cram sheets (design review item 8,
    // 2026-09-25). They used to float six 38px circles over the page (half
    // over the hero on desktop, colliding with the logo mark on a phone cram
    // sheet, half of them off-screen on a phone guide). The group now docks
    // as a right-aligned icon row INSIDE the sticky 38px .guide-back-bar.
    // Every script that adds a tool (search, highlights, guide-ink's pen)
    // appends to #corner-actions by id, so they land in the bar too. On
    // phones only Search and Settings stay in the row; the rest open from a
    // "More" menu (the buttons are moved, not rebuilt, so their listeners
    // and ids are untouched).
    var dockBar = document.querySelector(".guide-back-bar");
    if (dockBar) {
      group.classList.add("in-bar");
      var moreBtn = makeCornerBtn("more-btn", "More tools");
      moreBtn.innerHTML = MORE_ICON;
      moreBtn.setAttribute("aria-haspopup", "true");
      moreBtn.setAttribute("aria-expanded", "false");
      var moreMenu = document.createElement("div");
      moreMenu.className = "bar-more-menu";
      moreMenu.setAttribute("role", "menu");
      var ROW_KEEP = { "guide-search-btn": 1, "settings-btn": 1, "more-btn": 1 };
      var SETTINGS_ONLY = { "refresh-btn": 1, "theme-toggle-btn": 1, "calc-btn": 1, "pomo-btn": 1, "account-btn": 1 };
      function closeMore() {
        if (!moreMenu.classList.contains("open")) return;
        [].slice.call(moreMenu.children).forEach(function (b) { group.insertBefore(b, moreBtn); });
        moreMenu.classList.remove("open");
        moreBtn.setAttribute("aria-expanded", "false");
      }
      function openMore() {
        [].slice.call(group.children).forEach(function (b) {
          // tools theme.css folds into the Settings panel stay out of the menu
          if (ROW_KEEP[b.id] || SETTINGS_ONLY[b.id]) return;
          moreMenu.appendChild(b);
        });
        if (!moreMenu.children.length) return;
        moreMenu.classList.add("open");
        moreBtn.setAttribute("aria-expanded", "true");
      }
      moreBtn.addEventListener("click", function (e) {
        e.stopPropagation();
        if (moreMenu.classList.contains("open")) closeMore(); else openMore();
      });
      moreMenu.addEventListener("click", function () { setTimeout(closeMore, 0); });
      document.addEventListener("click", function (e) {
        if (!moreMenu.contains(e.target) && e.target !== moreBtn) closeMore();
      });
      document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeMore(); });
      window.addEventListener("resize", closeMore);
      group.appendChild(moreBtn);
      dockBar.appendChild(group);
      dockBar.appendChild(moreMenu);
      // the pen button is appended later by guide-ink.js; keep More last
      new MutationObserver(function () {
        if (group.lastElementChild !== moreBtn) group.appendChild(moreBtn);
      }).observe(group, { childList: true });
    } else {
      document.body.appendChild(group);
    }

    // "Back to previous page" -- fixed top-left, mirroring #corner-actions'
    // top-right placement. Only on non-homepage pages (index.html has its
    // own top-left #install-app-btn, and doesn't need this anyway), and only
    // when document.referrer shows the visitor actually arrived via an
    // in-site link -- a same-origin check, not just any referrer -- so the
    // button doesn't sit there uselessly for someone who opened this page
    // directly (typed URL, bookmark, new tab) with no real "previous page"
    // on this site to go back to.
    if (!document.body.classList.contains("homepage") &&
        !document.querySelector(".guide-back-bar") &&
        document.referrer && document.referrer.indexOf(location.origin) === 0) {
      var leftGroup = document.createElement("div");
      leftGroup.id = "corner-actions-left";
      var prevBtn = makeCornerBtn("prevpage-btn", "Back to previous page");
      prevBtn.innerHTML = ARROW_LEFT;
      prevBtn.addEventListener("click", function () { history.back(); });
      leftGroup.appendChild(prevBtn);
      document.body.appendChild(leftGroup);

      // Revealed only after a small scroll -- see the CSS comment on
      // #corner-actions-left for why: every page type puts its own title
      // text right at the top-left with no reserved clearance, so showing
      // this unconditionally from page load would sit on top of it.
      var revealAt = 80;
      var setVisible = function () {
        leftGroup.classList.toggle("visible", window.scrollY > revealAt);
      };
      setVisible();
      window.addEventListener("scroll", setVisible, { passive: true });
    }

    var shortcutsHelp = initShortcutsHelp();
    if (shortcutsHelp) {
      var shortcutsBtn = makeCornerBtn("shortcuts-btn", "Keyboard shortcuts");
      shortcutsBtn.innerHTML = KEYBOARD;
      shortcutsBtn.addEventListener("click", shortcutsHelp.open);
      group.insertBefore(shortcutsBtn, refreshBtn);

      // The one-time "controller supported" toast used to fire on every
      // first quiz load, phones included, on top of the tour prompt. It now
      // waits for a controller to actually connect (the gamepadconnected
      // handler further down gives the full mapping the first time).

      initHaptics();
      initSoundEffects();

      var shuffleCb = document.getElementById("shuffle-toggle");
      if (shuffleCb) {
        if (localStorage.getItem("defaultShuffle") === "1") {
          var resumeBanner = document.getElementById("resume-banner");
          var hasProgress = resumeBanner
            ? resumeBanner.style.display === "block"
            : localStorage.getItem("qshuf:" + location.pathname) !== null;
          if (!hasProgress) shuffleCb.checked = true;
        }
        setTimeout(function () {
          // Started within the delay: the tour's targets are gone, so offer it next time.
          var startCard = document.getElementById("start");
          if (startCard && getComputedStyle(startCard).display === "none") return;
          window.SiteTour.start(QUIZ_TOUR_STEPS, "tourSeen:quiz");
        }, 700);
      }

      var examModeCb = document.getElementById("exam-mode-toggle");
      if (examModeCb && localStorage.getItem("examModeDefault") === "1") {
        examModeCb.checked = true;
      }
      var hardCutoffCb = document.getElementById("hard-cutoff-toggle");
      if (hardCutoffCb && localStorage.getItem("hardCutoffDefault") === "1") {
        hardCutoffCb.checked = true;
      }
    }

    if (window.matchMedia) {
      window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function (e) {
        if (!localStorage.getItem("siteTheme")) {
          document.documentElement.setAttribute("data-theme", e.matches ? "dark" : "light");
          paintIcon(themeBtn, currentTheme());
        }
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

// Personal progress log (feeds progress.html's dashboard). When a quiz
// finishes it calls markCompleted() -- the engines' shared finish hook, a
// global on quiz pages -- so wrap that to append a dated completion event to a
// local "progressLog". This adds the time dimension (streaks, recent activity)
// that the per-quiz qc:<path> records lack. Pure localStorage (cloud-sync
// mirrors it across a signed-in user's devices) and independent of Firebase,
// so it keeps working offline. Runs here in theme.js (loads right after the
// page's own inline script) rather than the Firebase chain, so it's in place
// well before any quiz is finished.
(function () {
  if (typeof window.markCompleted !== "function") return;
  var LOG_KEY = "progressLog";
  var orig = window.markCompleted;
  window.markCompleted = function (score, total, timeMs) {
    try {
      var log = [];
      try { log = JSON.parse(localStorage.getItem(LOG_KEY)) || []; } catch (e) {}
      log.push({ t: Date.now(), p: location.pathname, s: score, n: total });
      if (log.length > 400) log = log.slice(log.length - 400);
      localStorage.setItem(LOG_KEY, JSON.stringify(log));
    } catch (e) {}
    return orig.apply(this, arguments);
  };
})();

// Cloud sync bootstrap (added 2026-07-10). Dynamically injects the Firebase
// SDK + firebase-config.js + cloud-sync.js, in that order, on every page --
// same zero-per-page-HTML-edit rollout as the calculator widget, since this
// is the one file every page already loads. All the actual auth/sync logic
// lives in cloud-sync.js, kept out of this already-large file. The relative
// path prefix ("../" on subfolder pages, "" at the repo root) is derived
// from this same script's own <script src> rather than hardcoded, so it
// resolves correctly regardless of page depth or hosting subpath.
(function () {
  var thisScript = document.querySelector('script[src$="theme.js"]');
  var base = thisScript ? thisScript.getAttribute("src").replace(/theme\.js$/, "") : "";
  var FIREBASE_VERSION = "10.14.1";
  var CDN = "https://www.gstatic.com/firebasejs/" + FIREBASE_VERSION + "/";

  function loadScript(src, onload) {
    var s = document.createElement("script");
    s.src = src;
    if (onload) s.onload = onload;
    s.onerror = function () { /* offline / blocked -- site stays fully local-only, no error surfaced */ };
    document.head.appendChild(s);
  }

  function startFirebaseChain() {
    loadScript(CDN + "firebase-app-compat.js", function () {
      // auth-compat and firestore-compat each independently extend the
      // global `firebase` namespace (firebase.auth / firebase.firestore) --
      // both only need firebase-app-compat.js to have loaded first, not
      // each other, so loading them in parallel instead of nested/
      // sequential cuts one full network round-trip out of the chain
      // before anything downstream (config, cloud-sync, presence) can
      // start. Dynamically-created <script> tags execute in whichever
      // order they finish downloading, not insertion order, which is fine
      // here since neither depends on the other's code having already run.
      var remaining = 2;
      function next() {
        remaining--;
        if (remaining > 0) return;
        loadScript(base + "firebase-config.js", function () {
          loadScript(base + "cloud-sync.js", function () {
            // presence.js (added 2026-07-14): "who's studying now" on guide
            // pages. Waits for cloud-sync.js's firebaseReady signal itself
            // (see that file's header comment), so chaining it after
            // cloud-sync.js here is only to keep load order predictable,
            // not a hard dependency -- it no-ops instantly on any page
            // without a .guide-back-bar.
            loadScript(base + "presence.js");
            // class-stats.js (added 2026-07-24): the class-wide cumulative
            // "questions answered" counter. Increments a shared Firestore doc
            // when any quiz finishes and displays it on the homepage. Same
            // firebaseReady-gated, no-op-where-irrelevant pattern as presence.
            loadScript(base + "class-stats.js");
          });
        });
      }
      loadScript(CDN + "firebase-auth-compat.js", next);
      loadScript(CDN + "firebase-firestore-compat.js", next);
    });
  }

  // Cloud sync / presence are background enhancements -- nothing on the
  // page needs them to already be usable/readable. Deferring the whole
  // chain's *start* until the browser reports idle time (falling back to a
  // short timeout on Safari, which doesn't implement requestIdleCallback)
  // keeps six-plus network requests from competing with the page's own
  // critical-path rendering, which matters most on a guide with a lot of
  // embedded content still settling right after load.
  // metrics.js (anonymous usage counts, 2026-10-10) loads straight away rather than with the idle
  // Firebase chain: it only buffers counts on the device, and waits for firebaseReady itself to send them
  loadScript(base + "metrics.js");
  var deferIdle = window.requestIdleCallback || function (fn) { setTimeout(fn, 300); };
  deferIdle(startFirebaseChain, { timeout: 2000 });
})();

// Guide text highlighting (added 2026-07-10). Select text anywhere inside a
// guide's .wrap[data-readable] and a small color-swatch toolbar appears;
// picking a color wraps the selection in <mark class="user-hl-COLOR">,
// clicking an existing highlight removes it. Persisted per-guide to
// localStorage, keyed by a stable index into the same "reading unit"
// elements the read-aloud engine above already walks (a separate constant
// here, not shared, since it lives in a different IIFE/closure -- if a
// future guide's caption/callout markup needs new classes in the read-aloud
// engine's UNIT_SELECTOR, add them here too so highlighting covers the same
// elements). Runs independently of read-aloud/speechSynthesis support (that
// module bails out entirely without it; highlighting shouldn't) -- gated on
// .guide-back-bar (present on every guide, read-aloud or not) rather than
// .wrap[data-readable], since that attribute is opt-in per guide (the
// Hormones reference guide deliberately doesn't have it, being a table
// guide with nothing to narrate) and highlighting has no such prerequisite.
/* ============================================================
   Pip review list (2026-10-11, finished 2026-10-15). A student selects something in a Semester 2
   study guide or cram sheet (or opens a highlight or a note box) and taps "Add to Pip"; it is kept per
   exam under the key "pipReview:<exam slug>" (an ordinary synced key: cloud-sync.js uploads only the
   one key that changed). my-review-guide.html turns the list into a personal guide; Pip's window
   shows a chip with the count. Nothing here writes any text of its own: an item is the guide's own
   words, trimmed (t), plus the student's own note (n) when there is one.
   Item: {id, f (folder), d (page file), a (anchor id), st (section title), k / kt (deck id / title),
   u (position in the page), t, n, at, m (last change), nid (the note box it came from, if any)}.
   A removed item leaves a tombstone {id, x} (see SYNCED LISTS below).
   ============================================================ */
/* ============================================================
   SYNCED LISTS (2026-10-15). "pipReview:<exam>" and "guideNote:<page>" are arrays of records with an
   id, and cloud-sync.js used to upload and download each one whole: two devices used before either
   reloaded lost each other's additions (the last upload won). Now, when cloud-sync.js reads one of
   these keys from the cloud, it calls window.CloudSyncMerge[prefix](local, cloud): the records are
   joined by id, the newer change of each wins (m, else at), and a deletion is kept as a tombstone
   {id, x (ms)} for 30 days, so the other device's copy cannot bring it back. A tombstone has no text
   (t), so every reader that keeps only records with text (PipReview.load, home.js, loadNotes, and
   the copies of this file already on students' devices) skips it.
   No extra Firestore traffic: the merge runs on documents cloud-sync already read, and uploads that
   one key only when the cloud copy lacks something.
   ============================================================ */
window.SyncList = (function () {
  var KEEP_MS = 30 * 86400000;
  function isTomb(x) { return !!x && typeof x === "object" && typeof x.id === "string" && typeof x.x === "number" && !x.t; }
  function isRec(x) { return !!x && typeof x === "object" && typeof x.id === "string" && !isTomb(x); }
  function when(x) { return Math.max(Date.parse(x.m || "") || 0, Date.parse(x.at || "") || 0); }
  // live records + tombstones -> the array to store: one tombstone per id (the newest), none for an id
  // that is live again, none older than 30 days
  function pack(recs, tombs, now) {
    var live = {}, best = {}, out = recs.slice();
    recs.forEach(function (r) { if (r && typeof r.id === "string") live[r.id] = 1; });
    (tombs || []).forEach(function (t) {
      if (!isTomb(t) || live[t.id] || (now || Date.now()) - t.x > KEEP_MS) return;
      if (!best[t.id] || t.x > best[t.id].x) best[t.id] = { id: t.id, x: t.x };
    });
    Object.keys(best).sort().forEach(function (id) { out.push(best[id]); });
    return out;
  }
  function combine(sides, now) {
    var rec = {}, order = [], tomb = {};
    sides.forEach(function (arr) {
      arr.forEach(function (x) {
        if (isTomb(x)) { if (!tomb[x.id] || x.x > tomb[x.id].x) tomb[x.id] = x; return; }
        if (!isRec(x)) return;
        var cur = rec[x.id];
        if (!cur) { rec[x.id] = x; order.push(x.id); return; }
        var a = when(x), b = when(cur);
        // the newer change wins; a tie is broken the same way on every device
        if (a > b || (a === b && JSON.stringify(x) > JSON.stringify(cur))) rec[x.id] = x;
      });
    });
    var recs = [], tombs = [];
    order.forEach(function (id) {
      var r = rec[id], t = tomb[id];
      if (t && t.x >= when(r)) return;            // deleted after its last change
      recs.push(r);
    });
    Object.keys(tomb).forEach(function (id) { tombs.push(tomb[id]); });
    return pack(recs, tombs, now);
  }
  function canon(arr) {
    return JSON.stringify(arr.slice().sort(function (a, b) {
      var ka = (isTomb(a) ? "~" : "") + a.id, kb = (isTomb(b) ? "~" : "") + b.id;
      return ka < kb ? -1 : ka > kb ? 1 : 0;
    }));
  }
  // (local, cloud) JSON strings -> {value, local, cloud}: the merged JSON, and whether it differs (beyond
  // order or expired tombstones) from each side. null = not two arrays: cloud-sync keeps its old rule.
  function merge(localStr, cloudStr) {
    var L, C;
    try { L = JSON.parse(localStr); C = JSON.parse(cloudStr); } catch (e) { return null; }
    if (!Array.isArray(L) || !Array.isArray(C)) return null;
    var now = Date.now(), out = combine([C, L], now), key = canon(out);
    return { value: JSON.stringify(out), local: canon(combine([L], now)) !== key, cloud: canon(combine([C], now)) !== key };
  }
  return { isTomb: isTomb, isRec: isRec, when: when, pack: pack, merge: merge };
})();
window.CloudSyncMerge = window.CloudSyncMerge || {};
window.CloudSyncMerge["pipReview:"] = window.SyncList.merge;
window.CloudSyncMerge["guideNote:"] = window.SyncList.merge;
window.CloudSyncMerge["qa:"] = window.SyncList.merge;   // quiz attempt history (ATTEMPT HISTORY below)

(function () {
  var PFX = "pipReview:", CAP = 600;
  function slugify(s) { return String(s || "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/-+/g, "-").replace(/^-|-$/g, ""); }
  function raw(slug) {
    try { var v = JSON.parse(localStorage.getItem(PFX + slug)); return Array.isArray(v) ? v : []; } catch (e) { return []; }
  }
  // Only well-formed items come back (the key is synced, so it may hold anything): id, t, f and d must be
  // strings; the optional text fields are made strings, so no page reading the list can trip on one.
  function load(slug) {
    var v = raw(slug);
    return v.filter(function (x) {
      return x && typeof x === "object" && typeof x.id === "string" && typeof x.t === "string" && x.t &&
             typeof x.f === "string" && typeof x.d === "string";
    }).map(function (x) {
      ["a", "st", "k", "kt", "n", "at"].forEach(function (f) { if (typeof x[f] !== "string") x[f] = ""; });
      return x;
    });
  }
  // `gone`: ids removed just now, kept as tombstones (with the ones already stored) so a sync cannot bring them back
  function save(slug, list, gone) {
    var now = Date.now(), tombs = raw(slug).filter(window.SyncList.isTomb);
    (gone || []).forEach(function (id) { tombs.push({ id: id, x: now }); });
    try { localStorage.setItem(PFX + slug, JSON.stringify(window.SyncList.pack(list, tombs, now))); return true; } catch (e) { return false; }
  }
  function norm(t) { return String(t || "").replace(/\s+/g, " ").trim(); }
  function idOf(text, file) {
    var s = norm(text).toLowerCase() + "|" + file, h = 5381;
    for (var i = 0; i < s.length; i++) h = ((h << 5) + h + s.charCodeAt(i)) | 0;
    return "r" + (h >>> 0).toString(36);
  }
  function trimText(t) {
    t = norm(t);
    if (t.length <= CAP) return t;
    var c = t.slice(0, CAP), sp = c.lastIndexOf(" ");
    return (sp > CAP * 0.6 ? c.slice(0, sp) : c).replace(/[\s,;:.-]+$/, "") + "…";
  }
  function slugs() {
    var out = [];
    try {
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (k && k.indexOf(PFX) === 0 && load(k.slice(PFX.length)).length) out.push(k.slice(PFX.length));
      }
    } catch (e) {}
    return out;
  }
  window.PipReview = {
    slugify: slugify, load: load, slugs: slugs, trim: trimText,
    count: function (slug) { return load(slug).length; },
    idOf: idOf,
    has: function (slug, id) { return load(slug).some(function (x) { return x.id === id; }); },
    add: function (slug, item) {          // "added", "exists" or "failed"
      var list = load(slug);
      if (list.some(function (x) { return x.id === item.id; })) return "exists";
      item.m = new Date().toISOString();  // newer than any earlier removal of the same id, on any device
      list.push(item);
      return save(slug, list) ? "added" : "failed";
    },
    remove: function (slug, id) {
      var list = load(slug), had = list.some(function (x) { return x.id === id; });
      save(slug, list.filter(function (x) { return x.id !== id; }), had ? [id] : null);
    },
    setNote: function (slug, id, note) {
      var list = load(slug), hit = false, now = new Date().toISOString();
      list.forEach(function (x) { if (x.id === id && (x.n || "") !== note) { x.n = note; x.m = now; hit = true; } });
      if (hit) save(slug, list);
    }
  };
})();

// Study-guide tools live in theme-guide.js (split out 2026-10-19); only guide pages load it. async=false keeps it
// ahead of guide-ink.js (also ordered), so the ink code still runs after the guide tools, as when both were here.
(function () {
  if (!document.querySelector(".guide-back-bar")) return;
  var me = document.querySelector('script[src$="theme.js"]');
  var s = document.createElement("script");
  s.src = (me ? me.getAttribute("src").replace(/theme\.js$/, "") : "") + "theme-guide.js";
  s.onerror = function () {                 // flaky Wi-Fi: one retry, so a dropped request does not lose the feature
    var r = document.createElement("script"); r.src = s.src; r.async = false; document.head.appendChild(r);
  };
  s.async = false;
  document.head.appendChild(s);
})();

// "Test yourself" quiz popup, generic/reusable across any page. Question
// data (title + 5ish {q, choices, correct, explain} objects) is supplied
// by the calling page -- this only owns the modal mechanics: render,
// instant per-question grading, running score, Esc/backdrop-click/X close.
window.openTestYourself = (function () {
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  return function openTestYourself(title, questions) {
    var overlay = el("div", "tq-overlay open");
    var panel = el("div", "tq-panel");

    var closeBtn = el("button", "tq-close", "×");
    closeBtn.type = "button";
    closeBtn.setAttribute("aria-label", "Close");

    var heading = el("p", "tq-title", title);
    var scoreEl = el("p", "tq-score");
    var score = 0;
    function updateScore() { scoreEl.textContent = "Score: " + score + " / " + questions.length; }
    updateScore();

    panel.appendChild(closeBtn);
    panel.appendChild(heading);
    panel.appendChild(scoreEl);

    // Banks were written in two shapes over time: {q, choices, correct, explain|expl}
    // and {q, o, a, why}. Accept both, so no button throws and every explanation shows.
    questions = questions.map(function (q) {
      return {
        q: q.q,
        choices: q.choices || q.o || [],
        correct: (q.correct !== undefined) ? q.correct : q.a,
        explain: q.explain || q.expl || q.why || ""
      };
    });
    questions.forEach(function (q, qi) {
      var qDiv = el("div", "tq-q");
      qDiv.appendChild(el("p", "tq-qtext", (qi + 1) + ". " + q.q));
      var optsWrap = el("div", "tq-opts");
      var explainEl = el("p", "tq-explain hidden", q.explain || "");
      var answered = false;

      q.choices.forEach(function (choice, ci) {
        var btn = el("button", "tq-opt", choice);
        btn.type = "button";
        btn.addEventListener("click", function () {
          if (answered) return;
          answered = true;
          if (ci === q.correct) {
            btn.classList.add("tq-correct");
            score++;
          } else {
            btn.classList.add("tq-wrong");
            optsWrap.children[q.correct].classList.add("tq-correct");
          }
          Array.prototype.forEach.call(optsWrap.children, function (b) { b.disabled = true; });
          explainEl.classList.remove("hidden");
          updateScore();
        });
        optsWrap.appendChild(btn);
      });

      qDiv.appendChild(optsWrap);
      qDiv.appendChild(explainEl);
      panel.appendChild(qDiv);
    });

    overlay.appendChild(panel);
    document.body.appendChild(overlay);

    function close() {
      overlay.remove();
      document.removeEventListener("keydown", onKey);
    }
    function onKey(e) {
      if (e.key === "Escape") close();
    }

    closeBtn.addEventListener("click", close);
    overlay.addEventListener("click", function (e) { if (e.target === overlay) close(); });
    document.addEventListener("keydown", onKey);
  };
})();

// Exam Mode's question-jump grid, shared across every quiz page rather than
// reimplemented per file (see feedback_exam_mode memory) -- a page supplies
// per-question state via getStatus(i) and jump/submit callbacks, this just
// renders the grid and wires clicks. Generic engine, page-specific data,
// same split as openTestYourself/SiteTour above.
window.openQuestionNav = (function () {
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }

  return function openQuestionNav(opts) {
    var overlay = el("div", "qnav-overlay open");
    var panel = el("div", "qnav-panel");

    var closeBtn = el("button", "tq-close", "×");
    closeBtn.type = "button";
    closeBtn.setAttribute("aria-label", "Close");

    var heading = el("p", "tq-title", "Jump to question");
    var summary = el("p", "qnav-summary");

    panel.appendChild(closeBtn);
    panel.appendChild(heading);
    panel.appendChild(summary);

    var legend = el("div", "qnav-legend");
    legend.appendChild(el("span", "qnav-legend-item", "■ Answered"));
    legend.appendChild(el("span", "qnav-legend-item unanswered", "□ Unanswered"));
    legend.appendChild(el("span", "qnav-legend-item flagged", window.SiteIcon("flag", 13) + " Flagged"));
    panel.appendChild(legend);

    var grid = el("div", "qnav-grid");
    var buttons = [];
    for (var i = 0; i < opts.total; i++) {
      var b = el("button", "qnav-item", String(i + 1));
      b.type = "button";
      (function (idx) {
        b.addEventListener("click", function () { close(); opts.onJump(idx); });
      })(i);
      buttons.push(b);
      grid.appendChild(b);
    }
    panel.appendChild(grid);

    function paint() {
      var unanswered = 0, flagged = 0;
      for (var i = 0; i < opts.total; i++) {
        var st = opts.getStatus(i) || {};
        var cls = "qnav-item";
        if (i === opts.current) cls += " current";
        cls += st.answered ? " answered" : " unanswered";
        if (st.flagged) { cls += " flagged"; flagged++; }
        if (!st.answered) unanswered++;
        buttons[i].className = cls;
      }
      summary.textContent = unanswered + " unanswered, " + flagged + " flagged";
    }
    paint();

    var submitBtn = el("button", "btn qnav-submit", "Submit exam →");
    submitBtn.type = "button";
    submitBtn.addEventListener("click", function () { close(); opts.onSubmit(); });
    panel.appendChild(submitBtn);

    overlay.appendChild(panel);
    document.body.appendChild(overlay);

    function close() {
      overlay.remove();
      document.removeEventListener("keydown", onKey);
    }
    function onKey(e) {
      if (e.key === "Escape") close();
    }

    closeBtn.addEventListener("click", close);
    overlay.addEventListener("click", function (e) { if (e.target === overlay) close(); });
    document.addEventListener("keydown", onKey);

    return { close: close };
  };
})();

// Shared toast (added 2026-07-10) -- generalizes the page-local
// showToast() index.html already had (mailto/install-prompt confirmations)
// so any page, quiz or otherwise, can call window.showToast() the same way.
// An optional action (2026-10-15): showToast(message, duration, {label, onClick, focus, returnFocus}) adds
// one real button (Undo, for instance). The toast is a polite live region, so the message is announced
// without moving focus; `focus: true` moves focus to the button (for a keyboard user whose control has
// just gone), and when the toast leaves while its button has focus, returnFocus() (or the element) gets
// it. Hovering or focusing the toast holds it open. Callers with two arguments get exactly what they did.
window.showToast = function (message, duration, action) {
  duration = duration || 3000;
  // The live region must exist (role and aria-live set, in the page) BEFORE its text changes, or some
  // screen readers skip the first message: when it is new here, the text goes in on the next frame.
  var toast = document.getElementById("site-toast"), fresh = false;
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "site-toast";
    toast.setAttribute("role", "status");
    toast.setAttribute("aria-live", "polite");
    toast.setAttribute("aria-atomic", "true");
    document.body.appendChild(toast);
    fresh = true;
  }
  if (!toast._live) {                 // first use here (home.js may have made the element without these)
    toast._live = true;
    if (!toast.hasAttribute("role")) { toast.setAttribute("role", "status"); fresh = true; }
    if (!toast.hasAttribute("aria-live")) { toast.setAttribute("aria-live", "polite"); fresh = true; }
    toast.setAttribute("aria-atomic", "true");
    toast.addEventListener("mouseenter", function () { if (toast._act) clearTimeout(toast._hideTimer); });
    toast.addEventListener("focusin", function () { if (toast._act && !toast._auto) clearTimeout(toast._hideTimer); });
    toast.addEventListener("mouseleave", function () { if (toast._act && !toast.contains(document.activeElement)) toast._arm(2500); });
    toast.addEventListener("focusout", function (e) { if (toast._act && !toast.contains(e.relatedTarget)) toast._arm(2500); });
  }
  clearTimeout(toast._hideTimer);
  clearTimeout(toast._clearTimer);
  var act = action && action.label && typeof action.onClick === "function" ? action : null;
  var old = toast._act;
  toast._act = act;
  function hide() {
    var btn = toast.querySelector(".site-toast-btn"), had = btn && document.activeElement === btn, a = toast._act;
    toast.style.opacity = "0";
    toast._act = null;
    if (had && a) {
      try { if (typeof a.returnFocus === "function") a.returnFocus(); else if (a.returnFocus && a.returnFocus.focus) a.returnFocus.focus({ preventScroll: true }); } catch (e) {}
      if (document.activeElement === btn) btn.blur();
    }
    if (btn) {
      // unreachable at once (not clickable, not in the Tab order); removed when the fade is over
      btn.disabled = true; btn.tabIndex = -1;
      toast.style.pointerEvents = "none";
      toast._clearTimer = setTimeout(function () {
        if (toast._act) return;
        if (btn.parentNode) btn.remove();
        toast.classList.remove("has-action");
        toast.style.pointerEvents = "";
      }, 260);
    }
  }
  toast._arm = function (ms) { clearTimeout(toast._hideTimer); toast._hideTimer = setTimeout(hide, ms); };
  var seq = toast._seq = (toast._seq || 0) + 1;
  function fill() {
    if (!act) {
      // a toast replacing one that had focus on its button: do not leave focus on a vanishing button
      var prev = toast.querySelector(".site-toast-btn");
      if (prev && document.activeElement === prev && old) { try { if (typeof old.returnFocus === "function") old.returnFocus(); else prev.blur(); } catch (e) {} }
      toast.textContent = message;
      toast.classList.remove("has-action");
      toast.style.pointerEvents = "";
    } else {
      toast.textContent = "";
      var msg = document.createElement("span");
      msg.className = "site-toast-msg";
      msg.textContent = message;
      var b = document.createElement("button");
      b.type = "button";
      b.className = "site-toast-btn";
      b.textContent = act.label;
      b.addEventListener("click", function (e) {
        if (toast._act !== act) return;
        hide();
        try { act.onClick(e); } catch (x) {}
      });
      b.addEventListener("keydown", function (e) { if (e.key === "Escape" || e.key === "Esc") { e.stopPropagation(); hide(); } });
      toast.appendChild(msg);
      toast.appendChild(b);
      toast.classList.add("has-action");
      toast.style.pointerEvents = "";
      // moved there by us, not by the student: the toast still leaves on time (their own focus holds it)
      if (act.focus) { toast._auto = true; try { b.focus({ preventScroll: true }); } catch (e) {} toast._auto = false; }
    }
  }
  if (fresh) {
    requestAnimationFrame(function () { if (toast._seq !== seq) return; fill(); toast.style.opacity = "1"; });
  } else {
    fill();
    requestAnimationFrame(function () { toast.style.opacity = "1"; });
  }
  toast._hideTimer = setTimeout(hide, duration);
};

// In-quiz answer-streak feedback (added 2026-07-10). Each MCQ quiz family
// calls window.trackAnswerStreak(correct) as one line inside its own
// choose()-equivalent function, in the normal (non-Exam-Mode) branch only --
// showing "3 in a row!" mid-answer would contradict Exam Mode's whole
// no-feedback-until-submit premise, so callers gate this behind `!examMode`
// themselves rather than this function trying to detect that itself (exam
// mode's own variable name/scope differs slightly family to family).
// Deliberately in-memory only (module-level counter, not localStorage) --
// this is a light in-the-moment nudge for the current sitting, not a stat
// to persist or show elsewhere.
(function () {
  var streak = 0;
  var THRESHOLDS = [3, 5, 10, 15, 20, 25];

  /* ---- Streak flame (2026-10-01) -----------------------------------------------------------------
     After 3 correct answers in a row a small flame sits beside the question number and grows (3 small,
     5 medium, 8 large, 10+ biggest with a spark). A wrong answer snuffs it with a puff of smoke.
     Nothing is stored or sent: the streak is read from the engine's own answer list when it is there
     (so a question answered once counts once, Restart starts from zero, and a resumed quiz shows the
     right number on its next answer), and falls back to a plain in-memory counter otherwise. The
     engine only calls this for first answers in live-feedback mode, never in Exam Mode, which is
     exactly when a flame would leak whether an answer was right. The flame is position:absolute
     inside .topbar (theme.css, "STREAK FLAME"), pointer-events none, so it moves and blocks nothing. */
  var flame = null, smokeT = 0;
  var rmq = window.matchMedia ? matchMedia("(prefers-reduced-motion: reduce)") : { matches: false };
  var gid = 0;
  function flameSvg() {
    var id = "sfg" + (++gid);
    return '<svg class="sf-fl" viewBox="0 0 24 32" aria-hidden="true"><defs><linearGradient id="' + id + '" x1="0" y1="1" x2="0" y2="0">' +
    '<stop offset="0" stop-color="#ea580c"/><stop offset=".6" stop-color="#f97316"/><stop offset="1" stop-color="#fbbf24"/></linearGradient></defs>' +
    '<path fill="url(#' + id + ')" d="M12 1C13 7 20 11 20 20c0 7-3.5 11-8 11s-8-4-8-11c0-5 3-7.500 4.500-10.500C9.500 11.500 10 12.500 11 13 10 8 10.500 4 12 1z"/>' +
    '<path fill="#fde047" d="M12 15c1 3 4 5 4 9 0 3.500-2 5.500-4 5.500s-4-2-4-5.500c0-3 3-5 4-9z"/></svg>';
  }

  function engineStreak() {
    try {
      if (typeof answers === "undefined" || typeof order === "undefined" || typeof QUESTIONS === "undefined") return -1;
      var last = (typeof idx === "number" && answers[idx] !== null && answers[idx] !== undefined) ? idx : -1, i;
      if (last < 0) for (i = 0; i < answers.length; i++) if (answers[i] !== null && answers[i] !== undefined) last = i;
      if (last < 0) return 0;
      var n = 0;                       // the run of correct answers that ENDS at the question just answered
      for (i = last; i >= 0; i--) {
        var q = QUESTIONS[order[i]];
        if (q && answers[i] === q.c) n++; else break;
      }
      return n;
    } catch (e) { return -1; }
  }
  function tierOf(n) { return n >= 10 ? 4 : n >= 8 ? 3 : n >= 5 ? 2 : n >= 3 ? 1 : 0; }
  function topbar() {
    var c = document.getElementById("counter");
    return c && c.parentNode && c.parentNode.classList && c.parentNode.classList.contains("topbar") ? c : null;
  }
  function place(el, c) {
    var bar = c.nextElementSibling, host = c.parentNode, phone = window.innerWidth <= 640;
    el.classList.remove("sf-tight", "sf-over"); host.classList.remove("sf-swap");
    if (!bar) return;
    if (phone) {
      // The phone row is full (question, bar, timer, Pause), so the pill takes the progress bar's own slot
      // while the streak lasts: nothing moves, and the question number still says how far through you are.
      el.classList.add("sf-over");                  // out of the row first, so measuring the bar is not fooled by the flame
      if (bar.offsetWidth < 38) { el.classList.remove("sf-over"); el.classList.add("sf-tight"); return; }
      host.classList.add("sf-swap");
      el.style.left = bar.offsetLeft + "px";
      el.style.top = (bar.offsetTop + bar.offsetHeight / 2 - el.offsetHeight / 2) + "px";
      return;
    }
    el.style.left = el.style.top = "";
    if (bar.offsetWidth < 60) el.classList.add("sf-tight");   // measured with the flame in the row
  }
  function watchCounter(c) {
    if (c._sfWatch || typeof MutationObserver !== "function") return;
    c._sfWatch = true;
    new MutationObserver(function () { if (flame && flame.parentNode) place(flame, c); })
      .observe(c, { childList: true, characterData: true, subtree: true });
  }
  function showFlame(n, fresh) {
    var c = topbar();
    if (!c) return;
    var bar = c.parentNode;
    bar.classList.add("sf-host");
    if (!flame || flame.parentNode !== bar) {
      if (flame && flame.parentNode) flame.parentNode.removeChild(flame);
      flame = document.createElement("span");
      flame.className = "sf"; flame.setAttribute("aria-hidden", "true");
      flame.innerHTML = flameSvg() + '<b class="sf-n"></b><i class="sf-spark"></i><i class="sf-spark b"></i>';
      var sc = document.getElementById("scoretxt");   // a flex item in the row, like the timer and the score
      if (sc && sc.parentNode === bar) bar.insertBefore(flame, sc); else bar.appendChild(flame);
      fresh = true;
    }
    watchCounter(c);
    var t = String(tierOf(n)), grew = flame.getAttribute("data-t") !== t;
    flame.setAttribute("data-t", t);
    flame.querySelector(".sf-n").textContent = n;
    place(flame, c);
    flame.classList.remove("sf-out");
    if (fresh) { flame.classList.remove("sf-grow"); flame.classList.add("sf-ignite"); }
    else if (grew && !rmq.matches) {
      flame.classList.remove("sf-ignite", "sf-grow"); void flame.offsetWidth; flame.classList.add("sf-grow");
    }
  }
  function snuff() {
    if (!flame || !flame.parentNode) return;
    var f = flame, bar = f.parentNode;
    flame = null;
    bar.classList.remove("sf-swap");
    if (!rmq.matches) {
      var sm = document.createElement("span");
      sm.className = "sf-smoke"; sm.setAttribute("aria-hidden", "true");
      sm.innerHTML = "<i></i><i></i><i></i>";
      sm.style.left = (f.offsetLeft + f.offsetWidth / 2) + "px";
      sm.style.top = (f.offsetTop + f.offsetHeight - 6) + "px";
      bar.appendChild(sm);
      setTimeout(function () { if (sm.parentNode) sm.parentNode.removeChild(sm); }, 1000);
    }
    f.classList.remove("sf-ignite", "sf-grow"); f.classList.add("sf-out");
    setTimeout(function () { if (f.parentNode) f.parentNode.removeChild(f); }, rmq.matches ? 0 : 340);
  }

  window.trackAnswerStreak = function (correct) {
    var s = engineStreak();
    if (s < 0) s = correct ? streak + 1 : 0;
    var prev = streak;
    streak = correct ? s : 0;
    if (!correct) { if (prev >= 3 || flame) snuff(); return; }
    if (streak >= 3) showFlame(streak, false);
    else if (flame && flame.parentNode) { flame.parentNode.removeChild(flame); flame = null; }   // e.g. a jump past an unanswered question
    // the flame already says "N in a row", so the older toast only speaks on pages that cannot show one
    if (flame && flame.parentNode) return;
    if (THRESHOLDS.indexOf(streak) !== -1) {
      window.showToast(streak + " in a row!");
    } else if (streak > THRESHOLDS[THRESHOLDS.length - 1] && streak % 10 === 0) {
      window.showToast(streak + " in a row!");
    }
  };
  /* Restart quiz: the engine's own answer list is cleared, but the flame element is still on screen. */
  document.addEventListener("click", function (e) {
    var b = e.target && e.target.closest ? e.target.closest("[onclick*='startExam']") : null;
    if (b && flame) { streak = 0; if (flame.parentNode) flame.parentNode.removeChild(flame); flame = null; }
  });
})();

// Pause/Resume for timed quizzes (added 2026-07-10), same "generic engine,
// page supplies data" split as openQuestionNav/openTestYourself above. This
// only renders the full-screen "Paused" overlay and calls opts.onResume when
// the user clicks Resume -- it deliberately does NOT touch any timer state
// itself, since every quiz family's timerAccumMs/timerStartedAt/
// startTimerInterval/stopTimerInterval/saveProgress are page-local globals
// with no shared engine to hook into (see feedback_exam_mode memory). Each
// quiz's own pauseQuiz() is expected to freeze its timer (mirroring the same
// accumulate-on-pause pattern already used for tab-close/resume) and call
// saveProgress() itself, then call window.openPauseOverlay({onResume:...}),
// with onResume restarting the timer the same way resumeQuiz() already does.
window.openPauseOverlay = function (opts) {
  var overlay = document.createElement("div");
  overlay.className = "pause-overlay open";

  var card = document.createElement("div");
  card.className = "pause-card";
  card.innerHTML =
    '<p class="pause-title">Paused</p>' +
    '<p class="pause-text">Your progress and timer are frozen. Take your time — click Resume when you’re ready to continue.</p>';

  var resumeBtn = document.createElement("button");
  resumeBtn.type = "button";
  resumeBtn.className = "pause-resume-btn";
  resumeBtn.textContent = "Resume →";
  card.appendChild(resumeBtn);

  overlay.appendChild(card);
  document.body.appendChild(overlay);

  resumeBtn.addEventListener("click", function () {
    overlay.remove();
    if (opts && opts.onResume) opts.onResume();
  });
};

// Optional gamepad support (added 2026-07-13) -- lets a connected
// controller answer MCQ questions without ever touching the keyboard.
// Bridges gamepad buttons into synthetic keydown events on the SAME keys
// every quiz-engine family's own keyboard shortcuts already listen for
// (a/b/c/d to pick a choice, ArrowRight/Enter to advance, ArrowLeft to go
// back -- see feedback_new_exam_structure_match: "full keyboard navigation
// on every quiz" has been a standing feature since early in the site).
// That means this needs zero per-quiz changes and works identically across
// every family at once, the same "generic engine, page-specific data"
// split used elsewhere in this file -- except here the "page" is just
// whatever keyboard handler already exists.
(function () {
  if (!("getGamepads" in navigator)) return;

  // Standard gamepad mapping: 0-3 are the four face buttons (A/B/X/Y on
  // Xbox-style pads, Cross/Circle/Square/Triangle on PlayStation) -- mapped
  // left-to-right, top-to-bottom onto the on-screen A/B/C/D choice labels.
  var CHOICE_KEYS = { 0: "a", 1: "b", 2: "c", 3: "d" };
  // Right shoulder/trigger/Start advance; left shoulder/trigger goes back --
  // mirrors how a physical controller's "confirm" side is usually the right
  // hand and "cancel/back" the left.
  var NEXT_BUTTONS = [5, 7, 9];
  var PREV_BUTTONS = [4, 6];

  var prevPressed = {};
  var polling = false;

  function fireKey(key) {
    document.dispatchEvent(new KeyboardEvent("keydown", { key: key, bubbles: true, cancelable: true }));
  }

  function pollGamepads() {
    var pads = navigator.getGamepads();
    var anyConnected = false;
    for (var p = 0; p < pads.length; p++) {
      var gp = pads[p];
      if (!gp) continue;
      anyConnected = true;
      var prev = prevPressed[gp.index] || {};
      var now = {};
      for (var i = 0; i < gp.buttons.length; i++) {
        var pressed = gp.buttons[i].pressed || gp.buttons[i].value > 0.5;
        now[i] = pressed;
        if (pressed && !prev[i]) {
          if (CHOICE_KEYS.hasOwnProperty(i)) fireKey(CHOICE_KEYS[i]);
          else if (NEXT_BUTTONS.indexOf(i) !== -1) fireKey("ArrowRight");
          else if (PREV_BUTTONS.indexOf(i) !== -1) fireKey("ArrowLeft");
        }
      }
      prevPressed[gp.index] = now;
    }
    if (anyConnected) requestAnimationFrame(pollGamepads);
    else polling = false;
  }

  window.addEventListener("gamepadconnected", function (e) {
    prevPressed[e.gamepad.index] = {};
    var firstPad = !localStorage.getItem("gamepadHintShown");
    try { localStorage.setItem("gamepadHintShown", "1"); } catch (err) {}
    if (window.showToast) {
      window.showToast(firstPad
        ? "Controller connected. A/B/X/Y to answer, RB/LB to move on/back. Press ? for full controls."
        : "Controller connected. A/B/X/Y answers, RB/RT next, LB/LT back", firstPad ? 5500 : undefined);
    }
    if (!polling) { polling = true; requestAnimationFrame(pollGamepads); }
  });
  window.addEventListener("gamepaddisconnected", function (e) {
    delete prevPressed[e.gamepad.index];
  });
})();

// focus-timer.js bootstrap (added 2026-09-29) -- a task's focus timer started in the study planner
// follows the student from page to page as a small pill in the top-left corner. The planner keeps
// the running timer in localStorage; this only fetches the pill's code while that key exists, so
// pages with no running timer never request the file. The planner calls window.__loadFocusTimer()
// when it starts or resumes a timer, since the key did not exist yet when its page loaded.
(function () {
  var TKEY = "planner:timer:v1", loaded = false;
  function load() {
    if (loaded || window.FocusTimer) return;
    loaded = true;
    var thisScript = document.querySelector('script[src$="theme.js"]');
    var base = thisScript ? thisScript.getAttribute("src").replace(/theme\.js$/, "") : "";
    var s = document.createElement("script");
    s.src = base + "focus-timer.js";
    document.head.appendChild(s);
  }
  window.__loadFocusTimer = load;
  var has = false;
  try { has = !!localStorage.getItem(TKEY); } catch (e) {}
  if (has) load();
  window.addEventListener("storage", function (e) { if (e.key === TKEY && e.newValue) load(); });   // started in another tab
})();

// guide-ink.js bootstrap (added 2026-07-14) -- freehand stylus/Apple Pencil
// drawing layer for guides. Unlike cloud-sync.js's chain, this has no
// Firebase dependency at all (it just writes to localStorage, which
// cloud-sync.js picks up for free via its own Storage.prototype patch if
// that's already loaded) -- so it's injected directly, no waiting on
// anything. Gated on .guide-back-bar HERE (not just inside guide-ink.js
// itself) so the ~35 quiz pages and the homepage never even issue the
// network request for a file they'd immediately no-op on -- one less
// fetch in the critical path on every page that isn't a guide.
(function () {
  if (!document.querySelector(".guide-back-bar")) return;
  var thisScript = document.querySelector('script[src$="theme.js"]');
  var base = thisScript ? thisScript.getAttribute("src").replace(/theme\.js$/, "") : "";
  var s = document.createElement("script");
  s.src = base + "guide-ink.js";
  s.async = false;                          // after theme-guide.js (see the loader above)
  document.head.appendChild(s);
})();

// Collapsible Contents sidebar (added 2026-07-23) -- every guide's own inline
// CSS lays out nav.toc as a sticky flex sidebar next to <main>; on desktop
// it's always open and eats a fair chunk of width. This adds a shared
// minimize/restore control (state persisted per-device) so it can be tucked
// away and main gets the full width, then brought back via a floating tab.
// Shared here rather than per-guide so all guides get it for free. The
// hide/show CSS lives in theme.css (body.toc-collapsed nav.toc / .toc-fab).
(function () {
  var toc = document.querySelector("nav.toc");
  if (!toc) return;
  var KEY = "tocCollapsed";
  var collapseBtn = document.createElement("button");
  collapseBtn.type = "button";
  collapseBtn.className = "toc-collapse-btn";
  collapseBtn.title = "Minimize contents";
  collapseBtn.setAttribute("aria-label", "Minimize contents");
  collapseBtn.innerHTML = "&laquo;";
  var h2 = toc.querySelector("h2");
  if (h2) h2.appendChild(collapseBtn); else toc.insertBefore(collapseBtn, toc.firstChild);

  var fab = document.createElement("button");
  fab.type = "button";
  fab.className = "toc-fab";
  fab.title = "Show contents";
  fab.setAttribute("aria-label", "Show contents");
  fab.innerHTML = window.SiteIcon("list", 15) + " Contents";
  document.body.appendChild(fab);

  // Collapsing/restoring the sidebar changes <main>'s width, which reflows
  // the text to a new height -- the browser keeps the same scrollY, so the
  // content visibly jumps. Anchor to the first content element still below
  // the sticky top bar, then scroll by however much it moved so that element
  // stays put across the toggle (all synchronous, so it paints once, no jump).
  function anchorEl() {
    var scope = document.querySelector("main") || document.querySelector(".wrap") || document.body;
    // Leaf/text elements only -- never containers like <section>/<div>, whose
    // box can span the whole viewport (top far above, bottom far below) and
    // barely moves on reflow, making it a useless anchor. Pick the first leaf
    // whose top sits just below the sticky top bar: that's what the reader is
    // looking at, and its position tracks the reflow precisely.
    var els = scope.querySelectorAll("h1,h2,h3,h4,h5,p,li,figcaption,td,th,dt,dd,blockquote,pre");
    for (var i = 0; i < els.length; i++) {
      var r = els[i].getBoundingClientRect();
      if (r.height > 0 && r.top >= 50) return els[i];
    }
    return null;
  }
  function setCollapsed(on) {
    var a = anchorEl();
    var before = a ? a.getBoundingClientRect().top : 0;
    document.body.classList.toggle("toc-collapsed", on);
    if (a) {
      var delta = a.getBoundingClientRect().top - before;
      // Must be instant: these guides set scroll-behavior:smooth, so a plain
      // scroll would *animate* the compensation (a visible glide that can be
      // interrupted). Forcing scroll-behavior:auto on the root for the one
      // scrollBy call snaps the anchor back in the same frame the reflow
      // happened, then restores whatever was there.
      if (delta) {
        var root = document.documentElement;
        var prev = root.style.scrollBehavior;
        root.style.scrollBehavior = "auto";
        window.scrollBy(0, delta);
        root.style.scrollBehavior = prev;
      }
    }
    try { localStorage.setItem(KEY, on ? "1" : "0"); } catch (e) {}
  }
  collapseBtn.addEventListener("click", function () { setCollapsed(true); });
  fab.addEventListener("click", function () { setCollapsed(false); });
  try { if (localStorage.getItem(KEY) === "1") setCollapsed(true); } catch (e) {}

  // Keep the whole Contents box inside the visible window at every scroll position
  // (2026-09-30, Jaxon: "the scroll on the contents doesn't let me go to the bottom").
  // Each guide's inline CSS caps nav.toc at 100dvh - 38px and sticks it at top:38px, which is
  // right once the page has scrolled past the banner -- but until then the box starts LOWER
  // (below the header, 170-250px down) and its bottom hangs off the screen. Scrolling inside
  // it cannot help (overscroll-behavior:contain stops the scroll reaching the page), so the
  // last entries were unreachable. The cap is therefore recomputed from where the box
  // actually is: room = visible height - max(its top, 38).
  // Belt and braces (2026-09-30, second report: "still doesn't show it all"): however the browser
  // measures its window (toolbars, zoom, an installed-app frame), the last entries must be able to
  // scroll well clear of the box's bottom edge, so the list ends with ~a hundred pixels of runway
  // and the cap leaves a small margin instead of landing exactly on the window edge.
  toc.style.paddingBottom = "110px";
  var capRaf = 0;
  function capToc() {
    capRaf = 0;
    if (!toc.offsetParent) return;                       // hidden: collapsed, or a narrow screen
    // "Large" text applies CSS zoom to the whole page wrapper (theme.css, data-text-size), and a
    // zoomed element's max-height is in its own, unzoomed pixels: 800px really covers 920 on
    // screen. That is the bug Jaxon kept hitting (1.15 zoom = the box ran ~15% past the window).
    // So measure the zoom (drawn height / layout height) and convert the room back.
    var r = toc.getBoundingClientRect(), zoom = 1;
    if (toc.offsetHeight > 0 && r.height > 0) zoom = r.height / toc.offsetHeight;
    if (Math.abs(zoom - 1) < 0.01 || zoom < 0.5 || zoom > 3) zoom = 1;
    var room = (window.innerHeight - Math.max(r.top, 38) - 12) / zoom;
    toc.style.maxHeight = Math.max(Math.floor(room), 160) + "px";
  }
  function queueCap() { if (!capRaf) capRaf = requestAnimationFrame(capToc); }
  window.addEventListener("scroll", queueCap, { passive: true });
  window.addEventListener("resize", queueCap);
  collapseBtn.addEventListener("click", queueCap);
  fab.addEventListener("click", queueCap);
  queueCap();
})();

/* ============================================================
   SEASON GATE (2026-10-19). Decides which seasonal themes run on this page -- the date windows, the
   precedence rules and the ?theme= / ?<name>=1 previews all live here and nowhere else -- adds each running
   theme's body class straight away (the light-mode tint must not wait for a download), and loads
   theme-seasonal.js (the kit + the themes, window.__themeKit) only when at least one theme is on.
   ============================================================ */
window.__themeSeason = (function () {
  var NAMES = ["snow", "lights", "newyear", "hearts", "clovers", "paweek", "leaves", "halloween", "thanksgiving", "fireworks"];
  var ALIAS = { xmas: "snow", december: "snow", holiday: "lights", ny: "newyear", vday: "hearts", valentines: "hearts",
    stpatricks: "clovers", clover: "clovers", fall: "leaves", autumn: "leaves", july4: "fireworks", fourth: "fireworks" };
  function canon(n) {
    n = String(n || "").toLowerCase();
    return NAMES.indexOf(n) >= 0 ? n : (Object.prototype.hasOwnProperty.call(ALIAS, n) ? ALIAS[n] : null);
  }

  // Thanksgiving week: Monday to Friday around the 4th Thursday of November (Nov 23-27 in 2026).
  function thanksgivingWeek(d) {
    if (d.getMonth() !== 10) return false;
    var firstDow = new Date(d.getFullYear(), 10, 1).getDay();
    var thu = 1 + ((4 - firstDow + 7) % 7) + 21;
    return d.getDate() >= thu - 3 && d.getDate() <= thu + 1;
  }
  var RULES = {                                   // local date, every year unless a year is named
    snow: function (d) { return d.getMonth() === 11; },
    hearts: function (d) { var m = d.getMonth(), x = d.getDate(); return (m === 0 && x === 31) || (m === 1 && x <= 14); },
    clovers: function (d) { var m = d.getMonth(), x = d.getDate(); return m === 2 && x >= 3 && x <= 17; },
    paweek: function (d) { return d.getFullYear() === 2026 && d.getMonth() === 9 && d.getDate() >= 5 && d.getDate() <= 9; },
    leaves: function (d) { return d.getMonth() === 9 && d.getDate() >= 17 && d.getDate() <= 31; },
    halloween: function (d) { return d.getMonth() === 9 && d.getDate() >= 24 && d.getDate() <= 31; },
    lights: function (d) { return d.getMonth() === 11 && d.getDate() <= 25; },
    newyear: function (d) { var m = d.getMonth(), x = d.getDate(); return (m === 11 && x === 31) || (m === 0 && x <= 2); },
    thanksgiving: thanksgivingWeek,
    fireworks: function (d) { return d.getMonth() === 6 && d.getDate() >= 3 && d.getDate() <= 5; }
  };
  var YIELDS = [["halloween", "leaves"], ["newyear", "snow"], ["newyear", "lights"]];         // [winner, loser]: on a date both match, only the winner runs

  var list = [], fresh = [];
  try {
    var stored = sessionStorage.getItem("themePreview");
    if (stored) list = stored.split(",").filter(canon);
    var re = /[?&]([a-z0-9]+)=([^&#]*)/gi, m;
    while ((m = re.exec(location.search))) {
      var key = m[1].toLowerCase(), val = decodeURIComponent(m[2]).toLowerCase();
      if (key === "theme") {
        list = (val === "off" || val === "0" || val === "") ? [] : val.split(",").map(canon).filter(Boolean);
        fresh = list.slice();
      } else if (canon(key) && (val === "1" || val === "0")) {
        var c = canon(key);
        list = list.filter(function (x) { return x !== c; });
        if (val === "1") { list.push(c); fresh.push(c); }
      }
    }
    if (list.length) sessionStorage.setItem("themePreview", list.join(",")); else sessionStorage.removeItem("themePreview");
  } catch (e) {
    var q = /[?&]theme=([a-z,]+)/i.exec(location.search);
    if (q) list = q[1].toLowerCase().split(",").map(canon).filter(Boolean);
    NAMES.forEach(function (n) { if (new RegExp("[?&]" + n + "=1(&|$)").test(location.search)) list.push(n); });
    fresh = list.slice();
  }
  var on = {};
  if (list.length) list.forEach(function (n) { on[n] = true; });
  else {
    var now = new Date();
    NAMES.forEach(function (n) { if (RULES[n](now)) on[n] = true; });
    YIELDS.forEach(function (y) { if (on[y[0]]) delete on[y[1]]; });
  }
  var CLS = { snow: ["xmas-theme"], lights: ["lights-theme", "xmas-theme"], newyear: ["newyear-theme"],
    fireworks: ["fireworks-theme"], hearts: ["vday-theme"], leaves: ["fall-theme"], halloween: ["halloween-theme"],
    thanksgiving: ["thanksgiving-theme"], clovers: ["stpatricks-theme"], paweek: ["paweek-theme"] };
  Object.keys(on).forEach(function (n) { (CLS[n] || []).forEach(function (c) { document.body.classList.add(c); }); });
  return { on: on, fresh: fresh, previewing: list.length > 0 };
})();
(function () {
  if (!Object.keys(window.__themeSeason.on).length) return;
  var me = document.querySelector('script[src$="theme.js"]');
  var s = document.createElement("script");
  s.src = (me ? me.getAttribute("src").replace(/theme\.js$/, "") : "") + "theme-seasonal.js";
  s.onerror = function () {                 // flaky Wi-Fi: one retry, so a dropped request does not lose the feature
    var r = document.createElement("script"); r.src = s.src; r.async = false; document.head.appendChild(r);
  };
  s.async = false;                          // ordered: runs after theme.js, like the code it replaces
  document.head.appendChild(s);
})();


/* ---- Report-a-mistake: in-page form -> Formspree (added 2026-07-22) ---- */
(function () {
  var FORMSPREE = "https://formspree.io/f/xdaqleod";
  function show() {
    var ov = document.getElementById("report-modal-overlay");
    ov.style.display = "flex";
    document.getElementById("report-status").textContent = "";
    var m = document.getElementById("report-msg"); if (m) { m.value = ""; m.focus(); }
    var e = document.getElementById("report-email"); if (e) e.value = "";
  }
  function hide() { var ov = document.getElementById("report-modal-overlay"); if (ov) ov.style.display = "none"; }
  function send() {
    var msg = (document.getElementById("report-msg").value || "").trim();
    var email = (document.getElementById("report-email").value || "").trim();
    var status = document.getElementById("report-status");
    if (!msg) { status.style.color = "#c93a3a"; status.textContent = "Please describe the mistake first."; return; }
    var btn = document.getElementById("report-send"); btn.disabled = true; btn.textContent = "Sending…";
    status.style.color = "#6b7280"; status.textContent = "";
    var data = { message: msg, page: location.href, quiz: document.title, _subject: "PA Quizzes Bug Report: " + document.title };
    // Whatever question is on screen goes with the report. A student who spots
    // a wrong answer should not have to describe which question they mean.
    var ctx = reportContext();
    if (ctx) data.question = ctx;
    if (email) data.email = email;
    fetch(FORMSPREE, { method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" }, body: JSON.stringify(data) })
      .then(function (r) { if (!r.ok) throw new Error("bad"); status.style.color = "#1f8f52"; status.textContent = "Thanks! Your report was sent."; setTimeout(hide, 1500); })
      .catch(function () { status.style.color = "#c93a3a"; status.textContent = "Could not send — please email jaxonluke22913@gmail.com."; })
      .finally(function () { btn.disabled = false; btn.textContent = "Send report"; });
  }
  /* Reads whatever the page is currently showing, so a report carries the
     question with it. Works off the DOM rather than engine variables: the
     quiz engines declare QUESTIONS/current with const, which never become
     window properties, so there is nothing for this to read otherwise. */
  function reportContext() {
    var bits = [];
    function vis(el) { return el && el.offsetParent !== null && el.textContent.trim(); }
    var prog = document.getElementById("progress");
    if (vis(prog)) bits.push(prog.textContent.trim());
    var plate = document.getElementById("source-chip");        // practicum plates
    if (vis(plate)) bits.push("Plate: " + plate.textContent.trim());
    var qt = document.getElementById("qtext");                 // multiple choice
    if (vis(qt)) bits.push("Q: " + qt.textContent.trim().slice(0, 400));
    var topic = document.getElementById("qtopic");
    if (vis(topic)) bits.push("Topic: " + topic.textContent.trim());
    return bits.join(" \u00b7 ");
  }

  window.reportMistake = function () {
    if (document.getElementById("report-modal-overlay")) { show(); return; }
    var ov = document.createElement("div");
    ov.id = "report-modal-overlay";
    ov.style.cssText = "position:fixed;inset:0;background:rgba(0,0,0,.55);display:none;align-items:center;justify-content:center;z-index:6000;padding:16px;";
    ov.innerHTML =
      '<div style="background:#fff;color:#111827;max-width:440px;width:100%;border-radius:14px;padding:22px 22px 18px;box-shadow:0 12px 40px rgba(0,0,0,.35);font-family:system-ui,-apple-system,Segoe UI,sans-serif;">' +
      '<h3 style="margin:0 0 4px;font-size:17px;">Report a mistake</h3>' +
      '<p style="margin:0 0 12px;font-size:13px;color:#6b7280;">Tell us what looks wrong on this page and it will get fixed. Thanks!</p>' +
      '<textarea id="report-msg" rows="4" placeholder="Describe the mistake (which question, what is wrong)…" style="width:100%;box-sizing:border-box;border:1px solid #d1d5db;border-radius:9px;padding:10px;font-size:14px;font-family:inherit;resize:vertical;"></textarea>' +
      '<input id="report-email" type="email" placeholder="Your email (optional, for a reply)" style="width:100%;box-sizing:border-box;border:1px solid #d1d5db;border-radius:9px;padding:9px 10px;font-size:14px;font-family:inherit;margin-top:8px;">' +
      '<div id="report-status" style="font-size:13px;margin-top:8px;min-height:18px;"></div>' +
      '<div style="display:flex;gap:8px;justify-content:flex-end;margin-top:6px;">' +
      '<button id="report-cancel" style="border:none;background:#e5e7eb;color:#111827;border-radius:9px;padding:9px 16px;font-weight:600;font-size:14px;font-family:inherit;cursor:pointer;">Cancel</button>' +
      '<button id="report-send" style="border:none;background:#2563eb;color:#fff;border-radius:9px;padding:9px 18px;font-weight:600;font-size:14px;font-family:inherit;cursor:pointer;">Send report</button>' +
      '</div></div>';
    document.body.appendChild(ov);
    ov.addEventListener("click", function (e) { if (e.target === ov) hide(); });
    document.getElementById("report-cancel").onclick = hide;
    document.getElementById("report-send").onclick = send;
    show();
  };
})();

/* ---- Report a problem with an EXAM question -> Forminit (2026-08-15) ----

   Separate from report-a-mistake above, which is for the site: a broken link,
   a typo, a page that will not load. This one is for the real exam -- a key
   the class thinks is wrong, wording that reads two ways, something asked that
   was never lectured -- so it collects the evidence needed to actually take it
   to a professor.

   Its own Forminit form, so these no longer share an inbox with the site
   issues. That separation was the point of moving.

   PHOTO UPLOAD WORKS on the free plan, confirmed by uploading real images and
   finding them in the dashboard.

   DO NOT TRY TO VERIFY AN UPLOAD FROM THE RESPONSE. Forminit's submit reply
   echoes a `submission.blocks` object listing the text fields it stored, and
   files are never in it -- not when they fail, and not when they succeed. It
   is tempting to read that as "the photo was dropped". This code did exactly
   that for one commit, which would have told every student their screenshot
   had failed while it sat safely in the dashboard, and sent them off to email
   a duplicate. The absence of a file in `blocks` means nothing at all.

   Two other things that look like evidence and are not:
   - The read API answers 403 "File upload not supported on free plan". That
     message is wrong; uploads plainly work. It appears for any key, valid or
     bogus, so it is about the API-read permission, not about files.
   - An upload posted with a malformed image, or from curl, can come back
     stored-but-not-echoed just the same. Only the dashboard tells you the
     truth about whether a file arrived.

   FORMINIT'S WIRE FORMAT is not Formspree's flat keys. Every field must be
   named `fi-{blockType}-{name}` -- `fi-text-problem`, `fi-text-class` -- and
   a body of plain names is rejected outright as EMPTY_SUBMISSION. There is no
   `_subject`; `fi-text-summary` carries the one-line headline instead. */
(function () {
  var ENDPOINT = "https://forminit.com/f/q1jz9v74p78";

  var UPLOADS_SUPPORTED = true;
  function acceptsUploads() { return UPLOADS_SUPPORTED; }

  /* Field name for the photo. Goes up as `fi-file-slideImage`, the same
     `fi-{blockType}-{name}` shape as the text fields. It does NOT come back in
     the response -- see the note above before writing anything that expects
     it to. */
  var FILE_FIELD = "slideImage";
  var ID = "tq-modal-overlay";

  /* Class list comes from the homepage's own tab strip rather than a fourth
     hand-kept copy of the course names (index.html's tabs, calendar.html's
     COURSE_LABEL and semesters.js already each hold one). The student then
     picks from exactly the labels they see on the page. Off the homepage there
     are no tabs, so the field falls back to free text. */
  function classOptions() {
    var out = [];
    document.querySelectorAll(".semester").forEach(function (block) {
      var semLabel = "";
      var reg = window.Semesters;
      var sem = reg && reg.byId ? reg.byId(block.dataset.semester) : null;
      if (sem) semLabel = sem.label;
      block.querySelectorAll(".tab-btn[data-tab]").forEach(function (btn) {
        /* Tab labels carry invisible wrapping hints -- soft hyphens in
           "Micro­biology", a zero-width space in "CAM/​Nutrition". They are
           right in a tab and wrong in an email subject line, so drop both. */
        var name = btn.textContent.replace(/[­​]/g, "").trim();
        if (name) out.push({ group: semLabel, name: name });
      });
    });
    return out;
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function classField() {
    var opts = classOptions();
    if (!opts.length) {
      return '<input id="tq-class" type="text" placeholder="Which class?" ' + INPUT + '>';
    }
    var groups = [], seen = {};
    opts.forEach(function (o) {
      if (!seen[o.group]) { seen[o.group] = []; groups.push(o.group); }
      seen[o.group].push(o.name);
    });
    var html = '<select id="tq-class" ' + INPUT + '><option value="">Which class?</option>';
    groups.forEach(function (g) {
      html += g ? '<optgroup label="' + esc(g) + '">' : "";
      seen[g].forEach(function (n) { html += '<option>' + esc(n) + '</option>'; });
      html += g ? "</optgroup>" : "";
    });
    return html + '<option>Other</option></select>';
  }

  /* 16px on the inputs is not just legibility -- iOS Safari zooms the whole
     page in when a focused field is under 16px, and this form is mostly fields,
     so the old 14px meant the layout lurched on the first tap. */
  var INPUT = 'style="width:100%;box-sizing:border-box;border:1px solid #d1d5db;' +
              'border-radius:10px;padding:11px 12px;font-size:16px;font-family:inherit;background:#fff;color:#111827;"';
  var AREA = 'style="width:100%;box-sizing:border-box;border:1px solid #d1d5db;' +
             'border-radius:10px;padding:12px;font-size:16px;font-family:inherit;line-height:1.5;resize:vertical;' +
             'background:#fff;color:#111827;"';
  var LABEL = 'style="display:block;font-weight:600;font-size:13.5px;font-family:inherit;color:#374151;margin:14px 0 5px;"';

  /* Either a real upload field, or directions to email the photo -- whichever
     the endpoint can actually honour. */
  function evidenceHint() {
    var note = 'style="font-size:13px;line-height:1.5;color:#6b7280;margin-top:5px;"';
    if (acceptsUploads()) {
      return '<input id="tq-file" type="file" accept="image/*" ' +
             'style="margin-top:10px;font-size:14px;font-family:inherit;color:#374151;max-width:100%;">' +
             '<div ' + note + '>A photo of the slide, if you have one — up to about 10 MB. ' +
             'Pasting the text above works too.</div>';
    }
    return '<div ' + note + '>Photos cannot be attached at the moment — paste the wording of ' +
           'the slide above instead, with the lecture and slide number.</div>';
  }

  function hide() { var ov = document.getElementById(ID); if (ov) ov.style.display = "none"; }

  function show() {
    var ov = document.getElementById(ID);
    ov.style.display = "flex";
    document.getElementById("tq-status").textContent = "";
    ["tq-exam", "tq-qnum", "tq-qtext", "tq-problem", "tq-evidence", "tq-file"]
      .forEach(function (id) { var el = document.getElementById(id); if (el) el.value = ""; });
    var c = document.getElementById("tq-class"); if (c) { c.value = ""; c.focus(); }
  }

  function send() {
    var val = function (id) {
      var el = document.getElementById(id);
      return el ? (el.value || "").trim() : "";
    };
    var status = document.getElementById("tq-status");
    var cls = val("tq-class"), problem = val("tq-problem");

    if (!cls) { fail(status, "Please pick which class the exam is from."); return; }
    if (!problem) { fail(status, "Please say what is wrong with the question."); return; }

    var btn = document.getElementById("tq-send");
    btn.disabled = true; btn.textContent = "Sending…";
    status.style.color = "#6b7280"; status.textContent = "";

    var exam = val("tq-exam"), qnum = val("tq-qnum");

    /* Forminit block format: `fi-{blockType}-{name}`. A body of plain field
       names comes back 400 EMPTY_SUBMISSION, so the prefixes are load-bearing,
       not decoration. `summary` stands in for the subject line Formspree had. */
    var fd = new FormData();
    fd.append("fi-text-summary", cls + (exam ? " · " + exam : "") +
                                 (qnum ? " · Q" + qnum : ""));
    fd.append("fi-text-class", cls);
    fd.append("fi-text-problem", problem);
    fd.append("fi-text-page", location.href);
    if (exam) fd.append("fi-text-exam", exam);
    if (qnum) fd.append("fi-text-questionNumber", qnum);
    if (val("tq-qtext")) fd.append("fi-text-questionWording", val("tq-qtext"));
    if (val("tq-evidence")) fd.append("fi-text-evidence", val("tq-evidence"));
    /* No sender block: reports are anonymous by design. Nobody replies to
       these individually, so asking for an address only implied otherwise --
       and a question is either wrong on the evidence or it is not, whoever
       raised it. */

    var fileEl = document.getElementById("tq-file");
    var file = fileEl && fileEl.files && fileEl.files[0];
    if (file) fd.append("fi-file-" + FILE_FIELD, file);

    /* Content-Type is deliberately unset: the browser has to write the
       multipart boundary itself, and setting it by hand yields a body the
       server cannot parse. */
    fetch(ENDPOINT, { method: "POST", body: fd, headers: { Accept: "application/json" } })
      .then(function (r) { if (!r.ok) throw new Error(String(r.status)); })
      .then(function () {
        status.style.color = "#1f8f52";
        status.textContent = "Thanks — sent. I'll look at it and take it up if it holds.";
        setTimeout(hide, 2200);
      })
      .catch(function (err) {
        /* Forminit rate-limits unauthenticated posts to one every 5 seconds, so
           reporting two questions back to back trips it. That is a wait, not a
           failure, and must not read like one -- the report is still sitting in
           the form, and telling someone to email instead would be wrong. */
        if (String(err.message) === "429") {
          fail(status, "One report every few seconds — give it a moment and press send again. Nothing you typed is lost.");
          return;
        }
        /* A photo is much the likeliest reason a send fails -- an oversized
           one especially. Point at the fix that keeps the writing, rather than
           making someone retype a report that was fine. */
        fail(status, file
          ? "Could not send with that photo — it may be too large. Remove it and send the report on its own; the wording is what matters most."
          : "Could not send — check your connection and try again in a moment. Nothing you typed is lost.");
      })
      .finally(function () { btn.disabled = false; btn.textContent = "Send report"; });
  }

  function fail(status, msg) { status.style.color = "#c93a3a"; status.textContent = msg; }

  window.reportTestQuestion = function () {
    if (document.getElementById(ID)) { show(); return; }
    var ov = document.createElement("div");
    ov.id = ID;
    ov.style.cssText = "position:fixed;inset:0;background:rgba(0,0,0,.55);display:none;" +
      "align-items:center;justify-content:center;z-index:6000;padding:16px;";
    ov.innerHTML =
      '<div role="dialog" aria-modal="true" aria-label="Report a problem with an exam question" ' +
      'style="background:#fff;color:#111827;max-width:660px;width:100%;max-height:calc(100dvh - 28px);' +
      'overflow:auto;border-radius:16px;padding:28px 28px 22px;box-shadow:0 12px 40px rgba(0,0,0,.35);' +
      'font-family:system-ui,-apple-system,Segoe UI,sans-serif;">' +
      '<h3 style="margin:0 0 7px;font-size:23px;line-height:1.25;">Issue with a test question</h3>' +
      '<p style="margin:0 0 6px;font-size:15px;line-height:1.55;color:#6b7280;">For a question on a ' +
      '<b>real class exam</b> — a key you think is wrong, wording that reads two ways, or something that was ' +
      'never lectured. The more of this you fill in, the easier it is to take to the professor.</p>' +
      '<p style="margin:0 0 4px;font-size:14px;line-height:1.5;color:#9ca3af;">Not for quizzes on this site — ' +
      'if one of those has a mistake in it, use <b>Report a mistake</b> at the bottom of the quiz instead.</p>' +
      '<label ' + LABEL + '>Class</label>' + classField() +
      '<div style="display:flex;gap:12px;">' +
        '<div style="flex:1;"><label ' + LABEL + '>Exam</label>' +
        '<input id="tq-exam" type="text" placeholder="e.g. Exam 3" ' + INPUT + '></div>' +
        '<div style="flex:1;"><label ' + LABEL + '>Question number</label>' +
        '<input id="tq-qnum" type="text" placeholder="e.g. 14" ' + INPUT + '></div>' +
      '</div>' +
      '<label ' + LABEL + '>The question, as worded</label>' +
      '<textarea id="tq-qtext" rows="4" placeholder="Type the question as it appeared, and the answer choices if you have them…" ' + AREA + '></textarea>' +
      '<label ' + LABEL + '>What is wrong with it</label>' +
      '<textarea id="tq-problem" rows="4" placeholder="What is wrong — which answer was marked correct, and why you think it is not…" ' + AREA + '></textarea>' +
      '<label ' + LABEL + '>Supporting evidence</label>' +
      '<textarea id="tq-evidence" rows="4" placeholder="Paste the slide text, or cite the lecture and slide number…" ' + AREA + '></textarea>' +
      evidenceHint() +
      '<div id="tq-status" style="font-size:14.5px;line-height:1.5;margin-top:14px;min-height:20px;"></div>' +
      '<div style="display:flex;gap:10px;justify-content:flex-end;margin-top:10px;">' +
      '<button id="tq-cancel" style="border:none;background:#e5e7eb;color:#111827;border-radius:10px;padding:12px 20px;font-weight:600;font-size:15.5px;font-family:inherit;cursor:pointer;">Cancel</button>' +
      '<button id="tq-send" style="border:none;background:#2563eb;color:#fff;border-radius:10px;padding:12px 24px;font-weight:600;font-size:15.5px;font-family:inherit;cursor:pointer;">Send report</button>' +
      '</div></div>';
    document.body.appendChild(ov);
    ov.addEventListener("click", function (e) { if (e.target === ov) hide(); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && ov.style.display === "flex") hide();
    });
    document.getElementById("tq-cancel").onclick = hide;
    document.getElementById("tq-send").onclick = send;
    show();
  };

  // Anything can open it by carrying this class, so the pill is not the only
  // possible entry point later.
  document.addEventListener("click", function (e) {
    var t = e.target.closest && e.target.closest(".report-question-btn");
    if (!t) return;
    e.preventDefault();
    window.reportTestQuestion();
  });
})();

/* ============================================================
   Footer mark: reveal only at the end of the page.
   See the "POLISH PASS" note in theme.css -- the mark is fixed at
   bottom-centre on 83 pages and was drawing over table cells, guide
   cards and paragraphs on any page long enough to scroll. Show it
   when the reader reaches the bottom, or immediately if the page
   doesn't scroll at all (where it was always fine).
   ============================================================ */
(function () {
  var mark = document.getElementById("quiz-footer-logo");
  if (!mark) return;
  var SLACK = 48; // px from the bottom that counts as "arrived"
  var ticking = false;

  function apply() {
    ticking = false;
    var doc = document.documentElement;
    var scrollable = doc.scrollHeight - window.innerHeight;
    // A page that barely scrolls never had the collision problem.
    var atBottom = scrollable <= SLACK ||
      (window.scrollY || doc.scrollTop) >= scrollable - SLACK;
    mark.classList.toggle("mark-visible", atBottom);
  }
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(apply);
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });
  // Content can load in late (lazy images, generated question banks),
  // which changes scrollHeight -- re-check when it does.
  if (typeof ResizeObserver === "function") {
    try { new ResizeObserver(onScroll).observe(document.body); } catch (e) {}
  }
  apply();
})();

/* ============================================================
   Quiz banner collapse. Flags <body class="quiz-running"> while a
   question is on screen so theme.css can shrink the title banner --
   see the note there. Purely presentational; the engine is untouched.
   ============================================================ */
(function () {
  var quiz = document.getElementById("quiz");
  if (!quiz) return;
  var results = document.getElementById("results");

  function sync() {
    var answering = quiz.offsetParent !== null &&
                    !(results && results.offsetParent !== null);
    document.body.classList.toggle("quiz-running", answering);
  }
  if (typeof MutationObserver === "function") {
    var mo = new MutationObserver(sync);
    var opts = { attributes: true, attributeFilter: ["style", "class", "hidden"] };
    mo.observe(quiz, opts);
    if (results) mo.observe(results, opts);
  }
  document.addEventListener("click", function () { setTimeout(sync, 60); }, true);
  sync();
})();

/* ============================================================
   Staggered reveal (2026-07-27)
   ------------------------------------------------------------
   Lists that appear as a group -- guide cards on load, quiz links
   when an exam accordion opens, arcade decks -- come in on a short
   stagger instead of all at once. Purely additive: the class only
   drives an animation, so if anything here fails the content is
   already in the DOM and visible.

   Capped at 14 items so a long list never crawls, and skipped
   entirely under prefers-reduced-motion.
   ============================================================ */
(function () {
  if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var MAX = 14;

  function stagger(items) {
    for (var i = 0; i < items.length; i++) {
      if (items[i].classList.contains("stagger-in")) continue;
      items[i].style.setProperty("--i", Math.min(i, MAX));
      items[i].classList.add("stagger-in");
    }
  }

  function onReady() {
    // guides.html card grid
    stagger(document.querySelectorAll(".guide-grid > .guide-card"));
    // arcade deck grid / exam list
    stagger(document.querySelectorAll(".deck-grid > .deck-card"));

    // Quiz links reveal as their exam accordion is opened.
    var sections = document.querySelectorAll("details.exam-section");
    for (var s = 0; s < sections.length; s++) {
      (function (sec) {
        sec.addEventListener("toggle", function () {
          if (!sec.open) return;
          var links = sec.querySelectorAll(".quiz-link");
          for (var i = 0; i < links.length; i++) links[i].classList.remove("stagger-in");
          // next frame, so removing and re-adding actually restarts it
          requestAnimationFrame(function () { stagger(links); });
        });
      })(sections[s]);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", onReady);
  } else {
    onReady();
  }
})();

/* ============================================================
   Content-page motion hooks (2026-07-27)
   ------------------------------------------------------------
   Drives the quiz/guide animations defined in theme.css. Both hooks
   are observers over markup the existing engines already produce, so
   none of the 431 generated quiz pages had to be regenerated.
   ============================================================ */
(function () {
  var reduce = window.matchMedia &&
               window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) return;

  /* --- quiz: replay the entrance whenever the stem changes --------- */
  var qtext = document.getElementById("qtext");
  var quiz = document.getElementById("quiz");
  if (qtext && quiz && typeof MutationObserver === "function") {
    var pending = false;
    new MutationObserver(function () {
      if (pending) return;
      pending = true;
      quiz.classList.remove("q-enter");
      // force a reflow so removing and re-adding actually restarts the run
      void quiz.offsetWidth;
      requestAnimationFrame(function () {
        pending = false;
        quiz.classList.add("q-enter");
      });
    }).observe(qtext, { childList: true, characterData: true, subtree: true });
    quiz.classList.add("q-enter");
  }

  /* --- guides/cram: figures settle in as they're reached -----------
     Scroll-driven rather than IntersectionObserver. IO only fires for
     elements that actually cross the viewport, so jumping via a TOC
     anchor (or Cmd+End, or a restored scroll position) skipped every
     figure in between and left them at opacity 0. A scroll pass reveals
     anything at or above the fold regardless of how you got there. */
  var figs = [].slice.call(document.querySelectorAll("figure.fig"));
  if (figs.length && document.documentElement.scrollHeight > window.innerHeight * 1.6) {
    var pending = [];
    for (var i = 0; i < figs.length; i++) {
      if (figs[i].getBoundingClientRect().top < window.innerHeight) continue; // already visible
      figs[i].classList.add("fig-pending");
      pending.push(figs[i]);
    }

    var ticking = false;
    function reveal() {
      ticking = false;
      for (var j = pending.length - 1; j >= 0; j--) {
        if (pending[j].getBoundingClientRect().top < window.innerHeight * 1.05) {
          pending[j].classList.remove("fig-pending");
          pending[j].classList.add("fig-in");
          pending.splice(j, 1);
        }
      }
      if (!pending.length) window.removeEventListener("scroll", onScroll);
    }
    function onScroll() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(reveal);
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });

    // Absolute backstop: never leave a figure hidden, whatever happens.
    setTimeout(function () {
      document.querySelectorAll("figure.fig.fig-pending").forEach(function (f) {
        f.classList.remove("fig-pending");
      });
      pending.length = 0;
    }, 3000);
  }
})();

/* ============================================================
   Quiz keyboard hint (2026-07-27)
   ------------------------------------------------------------
   The engine already supports A-D / 1-4 to answer, arrows to move,
   Enter to continue, F to flag and ? for the full list -- but nothing
   said so unless you happened to plug in a game controller, which got
   its own toast. One quiet line on the start screen instead.
   ============================================================ */
(function () {
  var start = document.getElementById("start");
  if (!start || document.getElementById("kbd-hint")) return;
  // Prefer the real start button: a page may put other buttons above it (the
  // practicum builder's topic picker does), and the hint belongs beside the
  // control that begins the quiz, not beside whatever button happens to be first.
  var startBtn = document.getElementById("start-btn") || start.querySelector("button");
  if (!startBtn) return;
  // Pointer-only devices get nothing -- the hint would just be noise.
  if (!window.matchMedia || !window.matchMedia("(hover: hover) and (pointer: fine)").matches) return;

  // Practicum pages are type-in identification. Their only key binding is
  // Enter on the answer field, so the multiple-choice hint was advertising four
  // shortcuts that do not exist there. Enter does NOT advance either -- the
  // input is disabled after checking and nothing takes focus -- so the hint
  // claims only what is actually wired up.
  var typeIn = !!document.getElementById("answer-input");

  var p = document.createElement("p");
  p.id = "kbd-hint";
  p.className = "kbd-hint";
  p.innerHTML = typeIn
    ? 'Keyboard: <kbd>Enter</kbd> to check your answer'
    : 'Keyboard: <kbd>A</kbd>&ndash;<kbd>D</kbd> to answer &middot; ' +
      '<kbd>&rarr;</kbd> next &middot; <kbd>F</kbd> flag &middot; ' +
      '<kbd>?</kbd> all shortcuts';
  startBtn.parentNode.insertBefore(p, startBtn.nextSibling);
})();

/* ============================================================
   Connection state (2026-07-27)
   ------------------------------------------------------------
   The site is an installed PWA with a service worker, so a student on
   a train or in a basement lecture hall WILL hit this -- and until now
   nothing said so. Quizzes and guides are cached and keep working;
   sign-in, Group Study and the class counter don't. A quiet bar makes
   the difference legible instead of looking broken.
   ============================================================ */
(function () {
  if (!("onLine" in navigator)) return;
  var bar = null;

  function ensure() {
    if (bar) return bar;
    bar = document.createElement("div");
    bar.id = "net-bar";
    bar.setAttribute("role", "status");
    bar.innerHTML =
      '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" ' +
      'stroke-width="2" stroke-linecap="round"><path d="M1 1l22 22"/>' +
      '<path d="M16.7 13.7a5 5 0 0 0-7.4 0"/><path d="M5 10.5a11 11 0 0 1 3.5-2.3"/>' +
      '<path d="M19 10.5a11 11 0 0 0-4.3-2.6"/><line x1="12" y1="20" x2="12.01" y2="20"/></svg>' +
      "<span>Offline &mdash; your saved quizzes and guides still work</span>";
    document.body.appendChild(bar);
    return bar;
  }

  function sync() {
    if (navigator.onLine) {
      if (bar) bar.classList.remove("show");
    } else {
      ensure().classList.add("show");
    }
  }
  window.addEventListener("online", sync);
  window.addEventListener("offline", sync);
  if (!navigator.onLine) sync();
})();

/* ============================================================
   QUIZ ACCESSIBILITY
   ------------------------------------------------------------
   The generated quiz engine ships with exactly one aria-label and no
   live region, so a screen reader announced nothing when an answer was
   marked right or wrong -- the verdict text just appeared silently.

   Done here rather than in the templates so none of the ~254 generated
   quiz pages need regenerating, same as the motion layer above. Kept in
   its OWN IIFE deliberately: the motion block early-returns under
   prefers-reduced-motion, and a screen-reader user may well have that
   set -- accessibility must not ride along with animation.

   Two engines exist on the site and both are handled: the current
   exam-navigator one (#opts / #expl, 245 files) and an older variant
   (#options / #explain / #qcount, 9 files, all Physiology Exam 3).
   They render identical `button.opt` elements with the same
   correct/wrong/selected-exam state classes, so only the container id
   and the position readout differ.
   ============================================================ */
(function () {
  var quiz = document.getElementById("quiz");
  if (!quiz) return;
  var opts = document.getElementById("opts") || document.getElementById("options");
  if (!opts) return;

  var qtext = document.getElementById("qtext");
  var verdict = document.getElementById("verdict");
  var expl = document.getElementById("expl") || document.getElementById("explain");
  var qcount = document.getElementById("qcount");

  /* The engine already writes "Correct." / "Not quite -- the correct answer
     is B." into #verdict. Making it a live region is all that is needed for
     that to be spoken, with no second copy of the wording to keep in sync. */
  if (verdict) {
    verdict.setAttribute("role", "status");
    verdict.setAttribute("aria-live", "polite");
    verdict.setAttribute("aria-atomic", "true");
  }
  /* Revealed at the same moment as the verdict; announcing it too would talk
     over that, so it is reachable as a landmark but not auto-read. */
  if (expl) {
    expl.setAttribute("role", "region");
    expl.setAttribute("aria-label", "Explanation");
  }

  opts.setAttribute("role", "group");
  opts.setAttribute("aria-label", "Answer choices");

  /* Position readout. The older engine already renders "Question 1 of 50"
     into #qcount, so that element is promoted to the live region rather than
     adding a second one that would say the same thing twice. The current
     engine has no such element, so one is created. */
  var pos = qcount;
  if (!pos) {
    pos = document.createElement("div");
    pos.className = "sr-only";
    quiz.insertBefore(pos, quiz.firstChild);
  }
  pos.setAttribute("role", "status");
  pos.setAttribute("aria-live", "polite");

  function announcePosition() {
    if (qcount) return;            // engine keeps it current itself
    var n, t;
    try { n = (typeof idx === "number" ? idx : -1) + 1; } catch (e) { n = 0; }
    try { t = (typeof QUESTIONS !== "undefined" && QUESTIONS.length) || 0; } catch (e) { t = 0; }
    pos.textContent = (n && t) ? "Question " + n + " of " + t : "";
  }

  /* Re-labels the option buttons after each render. The engine rebuilds the
     options wholesale per question, so this runs on every change -- and it
     reads state off the classes the engine already sets rather than
     duplicating its answer logic. */
  /* Both engines build each option as
        <span class="ltr">B</span><span class="optlabel">text</span>
     plus, while the question is live, a .cross-toggle button whose glyph is
     part of button.textContent. Reading textContent wholesale gave a screen
     reader "BThe myenteric plexus...\u2715" -- so pull the letter and the
     label from their own spans and skip the toggle entirely. */
  function optText(b) {
    var label = b.querySelector(".optlabel");
    var ltr = b.querySelector(".ltr");
    var body = ((label || b).textContent || "").trim();
    var l = ltr ? (ltr.textContent || "").trim() : "";
    return l ? l + ". " + body : body;
  }

  function relabel() {
    var list = opts.querySelectorAll(".opt");
    for (var i = 0; i < list.length; i++) {
      var b = list[i], txt = optText(b);
      b.setAttribute("aria-posinset", i + 1);
      b.setAttribute("aria-setsize", list.length);
      if (b.classList.contains("locked") || b.classList.contains("correct") ||
          b.classList.contains("wrong") || b.classList.contains("dim")) {
        b.setAttribute("aria-disabled", "true");
      } else {
        b.removeAttribute("aria-disabled");
      }
      if (b.classList.contains("correct")) b.setAttribute("aria-label", txt + ", correct answer");
      else if (b.classList.contains("wrong")) b.setAttribute("aria-label", txt + ", your answer, incorrect");
      else if (b.classList.contains("selected-exam")) b.setAttribute("aria-label", txt + ", selected");
      else b.removeAttribute("aria-label");
    }
  }

  if (typeof MutationObserver === "function") {
    if (qtext) {
      new MutationObserver(function () { announcePosition(); relabel(); })
        .observe(qtext, { childList: true, characterData: true, subtree: true });
    }
    /* The options mutate on their own when an answer is revealed (classes
       change on the existing buttons), which a #qtext observer never sees. */
    new MutationObserver(relabel).observe(opts, {
      childList: true, subtree: true, attributes: true, attributeFilter: ["class"]
    });
  }
  announcePosition();
  relabel();
})();

/* ============================================================
   READING-POSITION BAR  (study guides only)
   ------------------------------------------------------------
   Jaxon, 2026-09-02: "The long guides have a table of contents but no sense
   of how far through you are." Some of them run 10,000-27,000px tall.

   APPENDED TO <body>, NOT INTO .wrap. In dark mode theme.css inverts
   `body > .wrap` with a filter, and a filtered ancestor becomes the
   containing block for position:fixed descendants -- the bar would scroll
   away with the page instead of staying pinned, and it would be colour-
   inverted on top of that. Everything fixed on this site is a direct child
   of <body> for exactly that reason.

   Amber because that is the Guides hue in theme.css's hue map, and
   --a-amber already carries its own dark value, which is correct here
   precisely because this element is outside the inverted wrapper.

   Guides are identified by `nav.toc[data-readable]`. Cram sheets have a
   .toc too, but it is a <div> of chips, so they are not matched.
   ============================================================ */
(function () {
  var toc = document.querySelector('nav.toc[data-readable], nav.toc');
  if (!toc || toc.tagName !== 'NAV') return;
  if (!document.body) return;

  var bar = document.createElement('div');
  bar.id = 'read-bar';
  bar.setAttribute('aria-hidden', 'true');
  var fill = document.createElement('span');
  bar.appendChild(fill);
  /* Design review item 17 (2026-09-25): on guides with the sticky back bar
     the progress line runs along that bar's bottom edge, in the guide's own
     --accent, instead of across the very top of the window. The back bar is
     a body child (never inside the inverted .wrap), so the reason above for
     staying out of .wrap still holds; the bar stays 38px because this line is
     absolutely positioned. */
  var backBar = document.querySelector('body > .guide-back-bar');
  if (backBar) { bar.classList.add('in-back-bar'); backBar.appendChild(bar); }
  else document.body.appendChild(bar);

  var ticking = false;

  function paint() {
    ticking = false;
    var doc = document.documentElement;
    /* Scrollable height, not total height: the last viewport of a page is
       reached at 100%, so the bar fills exactly when the end is on screen
       rather than at some unreachable fraction. */
    var max = (doc.scrollHeight || 0) - window.innerHeight;
    if (max < 240) { bar.classList.remove('on'); return; }   // too short to be worth it
    bar.classList.add('on');
    var pct = Math.min(1, Math.max(0, (window.scrollY || doc.scrollTop || 0) / max));
    fill.style.width = (pct * 100).toFixed(2) + '%';
  }

  function onScroll() {
    if (ticking) return;
    ticking = true;
    (window.requestAnimationFrame || setTimeout)(paint, 16);
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  /* Guides load images lazily and open/close accordions, both of which change
     scrollHeight after load; without this the bar drifts out of true. */
  if (window.ResizeObserver) {
    try { new ResizeObserver(onScroll).observe(document.body); } catch (e) {}
  }
  window.addEventListener('load', paint);
  paint();
})();

/* ============================================================
   SWIPE BETWEEN QUESTIONS  (touch devices)
   ------------------------------------------------------------
   Jaxon, 2026-09-02: "The biggest change to how the site feels on a phone,
   which is where you actually use it."

   LIVES HERE, NOT IN tools/quiz-template/template.html, for the same reason
   the missed-question recorder does: the template only applies at render
   time, so putting it there would give the gesture to quizzes built after
   today and to nothing already on the site. theme.js is loaded by every one
   of them, and it no-ops on any page with no #quiz.

   It CLICKS THE ON-SCREEN BUTTONS rather than calling nextQ()/prevQ(), so a
   swipe can never do something the visible controls would not: Back is inert
   on question 1, and Forward stays inert in practice mode until the question
   has been answered -- exactly as the button is.

   The gesture is tracked anywhere on the card, including across the answer
   buttons, because confining it to the padding would make it undiscoverable.
   Browsers still fire a click after a drag that ends on a button, so a
   capture-phase listener swallows that one click: swiping over an option
   cannot answer it, and swiping over a picture cannot open the lightbox.

   Two things keep their own gesture: anything horizontally scrollable (a wide
   table inside an explanation) and Exam Mode's scroll column, which is one
   long page rather than a card at a time. Vertical drags are left alone, so
   the quiz pages' own pull-to-refresh is untouched.
   ============================================================ */
(function () {
  var card = document.getElementById('quiz');
  if (!card) return;
  if (!('ontouchstart' in window) && !navigator.maxTouchPoints) return;

  var THRESH = 58;        // px of travel before it counts as a swipe
  var DECIDE = 10;        // px before the axis is locked in
  var RATIO  = 1.2;       // how much more horizontal than vertical it must be
  var LIMIT  = 800;       // ms; slower than this is a scroll, not a flick

  var x0 = 0, y0 = 0, t0 = 0, dx = 0, axis = '', active = false, swiped = false;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  function scrollableX(el) {
    for (; el && el !== card; el = el.parentElement) {
      if (el.scrollWidth > el.clientWidth + 2) {
        var ov = getComputedStyle(el).overflowX;
        if (ov === 'auto' || ov === 'scroll') return true;
      }
    }
    return false;
  }

  /* The BUTTON decides whether the move is allowed -- Back is disabled on
     question 1, and Forward is display:none in practice mode until the
     question has been answered -- but the move itself is made by calling the
     navigation directly. Dispatching a synthetic click on the button instead
     was the first attempt and it deadlocked: the click-suppressor below
     swallowed the very click this code had just fired. */
  function usable(id) {
    var b = document.getElementById(id);
    if (!b || b.disabled) return false;
    return getComputedStyle(b).display !== 'none';
  }

  card.addEventListener('touchstart', function (e) {
    if (e.touches.length !== 1) return;
    if (document.getElementById('scrollcol')) return;      // Exam Mode scroll view
    if (card.style.display === 'none') return;
    if (scrollableX(e.target)) return;
    var t = e.touches[0];
    x0 = t.clientX; y0 = t.clientY; t0 = Date.now();
    dx = 0; axis = ''; active = true;
    card.classList.remove('swipe-settle');
  }, { passive: true });

  card.addEventListener('touchmove', function (e) {
    if (!active || e.touches.length !== 1) return;
    var t = e.touches[0];
    dx = t.clientX - x0;
    var dy = t.clientY - y0;
    if (!axis) {
      if (Math.abs(dx) < DECIDE && Math.abs(dy) < DECIDE) return;
      axis = Math.abs(dx) > Math.abs(dy) * RATIO ? 'x' : 'y';
    }
    if (axis !== 'x') { active = false; return; }
    if (!reduce) card.style.transform = 'translateX(' + (dx / 3) + 'px)';
  }, { passive: true });

  function release() {
    if (!active) return;
    active = false;
    var moved = dx, quick = Date.now() - t0 < LIMIT;
    card.classList.add('swipe-settle');
    card.style.transform = '';
    if (axis !== 'x' || !quick || Math.abs(moved) < THRESH) return;
    // Left drag = forward, the way a page turns.
    var fwd = moved < 0;
    if (!usable(fwd ? 'nextbtn' : 'prevbtn')) return;
    var go = window[fwd ? 'nextQ' : 'prevQ'];
    if (typeof go !== 'function') return;      // older engine: no paged nav
    // Set before navigating: the browser still delivers a click for the drag
    // that just ended, and it must not land on whatever is now under the
    // finger in the newly rendered question.
    swiped = true;
    setTimeout(function () { swiped = false; }, 400);
    go();
  }

  card.addEventListener('touchend', release, { passive: true });
  card.addEventListener('touchcancel', release, { passive: true });

  // The click the browser fires at the end of a drag, swallowed before it can
  // reach an option button or the picture.
  card.addEventListener('click', function (e) {
    if (!swiped) return;
    swiped = false;
    e.stopPropagation();
    e.preventDefault();
  }, true);
})();

/* ============================================================
   MISSED-QUESTION RECORDER
   ------------------------------------------------------------
   The quiz engine calls clearProgress() the instant results are shown
   (template.html line ~520), which removes the "qp:" entry holding the
   per-question answers. So a COMPLETED quiz kept only {score, total,
   timeMs} -- the record of which questions were actually missed was
   discarded at exactly the moment it became useful, and nothing on the
   site could tell a student what to go back and drill.

   This writes a compact record just before that happens:

     qm:<pathname> = { t, slug, title, total, m: [[questionIndex, chosen], ...] }

   `slug` matches the id used by tools/build_group_quizzes.py, which is a
   slug of "<folder>/<file>" -- every quiz on the site is exactly one
   directory deep (verified: 537 of 537), so the last two path segments
   reproduce it whether the site is served from / or /PA_Quizzes/. That
   is what lets review.html pull the question text from a
   group-quizzes/<slug>.js chunk instead of re-parsing quiz HTML.

   Done from theme.js so none of the ~254 generated quiz pages change.
   ============================================================ */
(function () {
  var results = document.getElementById("results");
  if (!results || typeof MutationObserver !== "function") return;

  function slugFromPath() {
    var parts = decodeURIComponent(location.pathname).split("/").filter(Boolean);
    if (!parts.length) return "";
    var rel = parts.slice(-2).join("/").replace(/\.html$/i, "");
    return rel.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/-+/g, "-").replace(/^-|-$/g, "");
  }

  function globalOf(name) {
    try { return eval("typeof " + name + " !== 'undefined' ? " + name + " : null"); }
    catch (e) { return null; }
  }

  /* Both engines shuffle QUESTION order into an `order` array and keep the
     option order fixed, so a stored choice index is directly comparable to
     the question's own answer index. */
  function collect() {
    var order = globalOf("order");
    if (!order || !order.length) return null;

    // current engine (245 files): QUESTIONS + answers[], parallel to order
    var Q = globalOf("QUESTIONS"), answers = globalOf("answers");
    if (Q && answers && answers.length) {
      var miss = [];
      for (var i = 0; i < answers.length; i++) {
        var qi = order[i];
        if (answers[i] === null || answers[i] === undefined) continue;
        if (Q[qi] && answers[i] !== Q[qi].c) miss.push([qi, answers[i]]);
      }
      return { total: Q.length, m: miss };
    }

    // older engine (9 files, Physiology Exam 3): questions + responses[]
    var q2 = globalOf("questions"), resp = globalOf("responses");
    if (q2 && resp && resp.length) {
      var miss2 = [];
      for (var j = 0; j < resp.length; j++) {
        var r = resp[j];
        if (!r || r.isCorrect) continue;
        var qi2 = order[r.i];               // r.i is a position, not an index
        if (typeof qi2 === "number" && q2[qi2]) miss2.push([qi2, r.choice]);
      }
      return { total: q2.length, m: miss2 };
    }
    return null;
  }

  function record() {
    var data = collect();
    if (!data) return;
    try {
      localStorage.setItem("qm:" + location.pathname, JSON.stringify({
        t: Date.now(),
        slug: slugFromPath(),
        title: (document.title || "").replace(/\s*[-—|]\s*Class of 2028.*$/i, "").trim(),
        total: data.total,
        m: data.m
      }));
    } catch (e) { /* quota or private mode -- reviewing is optional */ }
  }

  /* Trigger on VISIBILITY, not on children being appended. The current engine
     builds #results by writing into an empty container, but the older one
     ships a populated <section id="results" class="hidden"> and simply drops
     the class -- a childList-only observer never fired for those 9 files. */
  function visible() {
    return !!(results.offsetWidth || results.offsetHeight || results.getClientRects().length);
  }
  /* Once per finish. A finished run is told apart by its answers array: startExam()
     makes a new one, so a retake in the same page load records too (a one-shot flag
     used to keep the first run's misses), while #results being hidden and shown again
     (the attempt viewer below does that) records nothing new. */
  var lastRef = null;
  function check() {
    if (!visible()) return;
    var ref = globalOf("answers") || globalOf("responses");
    if (ref && ref === lastRef) return;
    lastRef = ref;
    record();
  }
  new MutationObserver(check).observe(results, {
    childList: true, attributes: true, attributeFilter: ["class", "style", "hidden"]
  });
  check();
})();

/* ============================================================
   ATTEMPT HISTORY (2026-10-23)
   ------------------------------------------------------------
   A classmate asked to keep every finished attempt so they can go back and
   review each one later: the questions they got right as well as the ones they
   missed. Until now a finish kept only the latest score (qc:) and the misses
   (qm:), and the next finish overwrote both.

     qa:<pathname> = [ {id, at, n, s, ms, ex, g, q, a, k}, ... ]   oldest first

   n questions in that attempt, s correct, ms time taken, ex 1 = no-feedback
   (exam) mode, g = hash of the bank's stems; per question IN THE ORDER SEEN:
   q its stable qid (or its bank index on pages without qids), a the choice
   ("0".."9", "-" = skipped), k the key at the time, p a 3-character hash of the
   picked option's text ("---" when skipped). k and p are stored so an attempt is
   never shown against a question whose options have since moved: positions are
   permuted on rebuilds, and the key can stay put while the picked option changes.
   About 0.7 KB for 60 questions; the newest CAP are kept.

   The key syncs like every other key, merged record by record through
   window.SyncList (see SYNCED LISTS), so attempts made on two devices before
   either reloaded are both kept, and a trimmed one leaves a tombstone.

   The viewer is a card inside .wrap (not a fixed overlay), so the dark-mode
   invert, high contrast and large text all apply to it as they do to the quiz.
   Current engine only (QUESTIONS + answers + order: 714 pages). The 9 older
   Physiology Exam 3 pages keep their misses (above) but no history.
   ============================================================ */
(function () {
  var results = document.getElementById("results"), start = document.getElementById("start");
  if (!results || !start || typeof MutationObserver !== "function" || !window.SyncList) return;
  var KEY = "qa:" + location.pathname, CAP = 25, LTR = "ABCDEFGH";

  function globalOf(name) {
    try { return eval("typeof " + name + " !== 'undefined' ? " + name + " : null"); }
    catch (e) { return null; }
  }
  var Q = globalOf("QUESTIONS");
  if (!Array.isArray(Q) || !Q.length || !Array.isArray(globalOf("answers"))) return;

  function sig() {
    var s = Q.map(function (q) { return q && q.q; }).join("\n"), h = 0x811c9dc5;
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 0x01000193); }
    return (h >>> 0).toString(36);
  }
  // qids are used only when every question has one and none repeats
  var byQid = null;
  (function () {
    var m = {};
    for (var i = 0; i < Q.length; i++) {
      var id = Q[i] && Q[i].qid;
      if (typeof id !== "string" || !id || m[id] !== undefined) return;
      m[id] = i;
    }
    byQid = m;
  })();

  function hash3(t) {   // 3 base-36 characters of FNV-1a over the option text
    var h = 0x811c9dc5; t = String(t == null ? "" : t);
    for (var i = 0; i < t.length; i++) { h ^= t.charCodeAt(i); h = Math.imul(h, 0x01000193); }
    return ("00" + ((h >>> 0) % 46656).toString(36)).slice(-3);
  }
  // the key is synced, so it may hold anything: the id goes into an attribute, so it is checked too
  function valid(x) {
    return !!x && typeof x === "object" && typeof x.id === "string" && /^[0-9a-z]{1,32}$/.test(x.id) &&
      !window.SyncList.isTomb(x) && typeof x.n === "number" && x.n > 0 && x.n % 1 === 0 &&
      typeof x.s === "number" && Array.isArray(x.q) && typeof x.a === "string" && typeof x.k === "string" &&
      typeof x.p === "string" && x.q.length === x.n && x.a.length === x.n && x.k.length === x.n && x.p.length === 3 * x.n;
  }
  function when(x) { return Date.parse(x.at || "") || 0; }
  function raw() {
    try { var v = JSON.parse(localStorage.getItem(KEY)); return Array.isArray(v) ? v : []; } catch (e) { return []; }
  }
  function list() { return raw().filter(valid).sort(function (a, b) { return when(a) - when(b); }); }

  function collect() {
    var order = globalOf("order"), answers = globalOf("answers");
    if (!order || !order.length || !answers || answers.length !== order.length) return null;
    var ids = [], a = "", k = "", p = "", s = 0;
    for (var i = 0; i < order.length; i++) {
      var qi = order[i], q = Q[qi];
      if (!q || !Array.isArray(q.opts) || typeof q.c !== "number" || q.c < 0 || q.c > 9) return null;
      var ch = answers[i];
      ids.push(byQid ? q.qid : qi);
      a += (typeof ch === "number" && ch >= 0 && ch <= 9) ? String(ch) : "-";
      k += String(q.c);
      p += a.charAt(i) === "-" || !q.opts[ch] ? "---" : hash3(q.opts[ch][0]);
      if (ch === q.c) s++;
    }
    var ms = 0;
    try { ms = (JSON.parse(localStorage.getItem("qc:" + location.pathname)) || {}).timeMs || 0; } catch (e) {}
    return {
      id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6),
      at: new Date().toISOString(), n: order.length, s: s, ms: typeof ms === "number" ? Math.round(ms) : 0,
      ex: globalOf("deferFeedback") ? 1 : 0, g: sig(), q: ids, a: a, k: k, p: p
    };
  }

  var latestId = null;
  function record() {
    var rec = collect();
    if (!rec) return;
    var all = raw(), recs = all.filter(valid), tombs = all.filter(window.SyncList.isTomb);
    recs.push(rec);
    recs.sort(function (a, b) { return when(a) - when(b); });
    while (recs.length > CAP) {   // never the attempt just made, even if this device's clock runs behind
      var drop = recs[0] === rec ? 1 : 0;
      tombs.push({ id: recs.splice(drop, 1)[0].id, x: Date.now() });
    }
    try {
      localStorage.setItem(KEY, JSON.stringify(window.SyncList.pack(recs, tombs)));
      latestId = rec.id;
    } catch (e) { /* full or private mode: the history is optional */ }
  }

  /* ---------- formatting ---------- */
  function pct(r) { return Math.round(100 * r.s / r.n); }
  function grade(p) { return p >= 80 ? "qa-g" : p >= 60 ? "qa-w" : "qa-b"; }
  function dur(ms) {
    if (!ms || ms < 1000) return "";
    var t = Math.round(ms / 1000), h = Math.floor(t / 3600), m = Math.floor(t % 3600 / 60), sec = t % 60;
    return (h ? h + ":" + (m < 10 ? "0" : "") : "") + m + ":" + (sec < 10 ? "0" : "") + sec;
  }
  function stamp(r) {
    var d = new Date(when(r));
    return d.toLocaleDateString(undefined, { weekday: "short", month: "short", day: "numeric" }) + ", " +
      d.toLocaleTimeString(undefined, { hour: "numeric", minute: "2-digit" });
  }

  /* ---------- the list of attempts (start screen and results) ---------- */
  function listHTML(recs) {
    var best = 0;
    recs.forEach(function (r) { best = Math.max(best, pct(r)); });
    var rows = recs.slice().reverse().map(function (r) {
      var p = pct(r), i = recs.indexOf(r) + 1;
      return '<li><button type="button" class="qa-row" data-qa="' + r.id + '">' +
        '<span class="qa-rn">Attempt ' + i + '</span>' +
        '<span class="qa-rd">' + stamp(r) + (r.ex ? ' &middot; exam mode' : '') + '</span>' +
        '<span class="qa-rs"><b class="' + grade(p) + '">' + p + '%</b> ' + r.s + '/' + r.n +
          (dur(r.ms) ? ' &middot; ' + dur(r.ms) : '') + '</span>' +
        '<span class="qa-go">Review &rarr;</span></button></li>';
    }).join("");
    return '<summary><span class="qa-sum-t">Your past attempts (' + recs.length + ')</span>' +
      '<span class="qa-sum-s">Best ' + best + '% &middot; last ' + pct(recs[recs.length - 1]) + '%</span></summary>' +
      '<ul class="qa-rows">' + rows + '</ul>' +
      '<p class="qa-note">Every question from each attempt, right and wrong. Kept on this device (your last ' + CAP +
      '); signed in, they follow you to your other devices.</p>';
  }
  function placeList(host, before) {
    var old = host.querySelector(":scope > .qa-past");
    var recs = list();
    if (!recs.length) { if (old) old.remove(); return null; }
    var d = old || document.createElement("details");
    var open = old ? old.open : false;
    d.className = "qa-past";
    d.innerHTML = listHTML(recs);
    d.open = open;
    if (!old) { if (before && before.parentNode === host) host.insertBefore(d, before); else host.appendChild(d); }
    return d;
  }

  /* ---------- one attempt, every question ---------- */
  var view = null, from = null, fromY = 0, filter = "all", pushed = false;
  function item(r, i, same) {
    var ref = r.q[i], ch = r.a.charAt(i) === "-" ? null : +r.a.charAt(i), key = +r.k.charAt(i);
    var st = ch === null ? "skip" : ch === key ? "ok" : "bad";
    var qi = typeof ref === "string" ? (byQid && byQid[ref] !== undefined ? byQid[ref] : -1)
           : (same && typeof ref === "number" ? ref : -1);
    var q = qi >= 0 ? Q[qi] : null;
    var tag = st === "ok" ? "&#10003; Correct" : st === "bad" ? "&#10007; Missed" : "&mdash; Skipped";
    var out = '<div class="mitem qa-it qa-' + st + '" data-st="' + st + '">' +
      '<div class="qa-tag">' + tag + '</div>';
    if (!q) return out + '<div class="mq">Q' + (i + 1) + '.</div>' +
      '<p class="qa-gone">This question has been removed from the quiz since this attempt.</p></div>';
    var moved = q.c !== key || (ch !== null && (!q.opts[ch] || hash3(q.opts[ch][0]) !== r.p.substr(3 * i, 3)));
    var fig = globalOf("figHTML");
    out += '<div class="mq">Q' + (i + 1) + '. ' + q.q + '</div>' + (typeof fig === "function" ? fig(q) : "");
    if (moved) out += '<p class="qa-gone">This question was edited after this attempt, so your original pick can&rsquo;t be shown. Here is the current version.</p>';
    out += '<ol class="qa-opts">';
    q.opts.forEach(function (o, j) {
      var isKey = j === q.c, isYou = !moved && j === ch;
      out += '<li class="qa-o' + (isKey ? ' is-key' : '') + (isYou && !isKey ? ' is-you' : '') + '">' +
        '<span class="qa-l">' + LTR.charAt(j) + '</span><span class="qa-ot">' + o[0] + '</span>' +
        (isKey ? '<span class="qa-m">' + (isYou ? 'Your answer &middot; correct' : 'Correct answer') + '</span>'
               : isYou ? '<span class="qa-m">Your answer</span>' : '') + '</li>';
    });
    out += '</ol>';
    out += '<div class="qa-why"><b>Why ' + LTR.charAt(q.c) + ' is right:</b> ' + (q.opts[q.c][1] || '') + '</div>';
    if (!moved && st === "bad" && q.opts[ch][1]) out += '<div class="qa-why qa-why-x"><b>Why ' + LTR.charAt(ch) + ' is wrong:</b> ' + q.opts[ch][1] + '</div>';
    var rest = q.opts.map(function (o, j) { return j; }).filter(function (j) { return j !== q.c && (moved || j !== ch) && q.opts[j][1]; });
    if (rest.length) out += '<details class="qa-more"><summary>Why the other options are wrong</summary>' +
      rest.map(function (j) { return '<p><b>' + LTR.charAt(j) + '.</b> ' + q.opts[j][1] + '</p>'; }).join("") + '</details>';
    if (q.cite) out += '<div class="mc">' + q.cite + '</div>';
    return out + '</div>';
  }
  function applyFilter() {
    if (!view) return;
    var its = view.querySelectorAll(".qa-it"), shownN = 0;
    for (var i = 0; i < its.length; i++) {
      var st = its[i].getAttribute("data-st");
      var on = filter === "all" || (filter === "ok" ? st === "ok" : st !== "ok");
      its[i].hidden = !on;
      if (on) shownN++;
    }
    view.querySelectorAll(".qa-f").forEach(function (b) {
      var on = b.getAttribute("data-f") === filter;
      b.classList.toggle("is-on", on);
      b.setAttribute("aria-pressed", on ? "true" : "false");
    });
    var none = view.querySelector(".qa-none");
    if (none) none.hidden = shownN > 0;
  }
  function render(id) {
    var recs = list(), at = -1;
    for (var i = 0; i < recs.length; i++) if (recs[i].id === id) at = i;
    if (at < 0) return false;
    var r = recs[at], same = r.g === sig(), ok = 0, skip = 0;
    for (var j = 0; j < r.n; j++) { if (r.a.charAt(j) === r.k.charAt(j)) ok++; else if (r.a.charAt(j) === "-") skip++; }
    var lost = !same && r.q.some(function (x) { return typeof x === "number"; });
    var p = pct(r);
    var nav = '<div class="qa-nav">' +
      '<button type="button" class="btn btn-ghost qa-back">&larr; Back</button>' +
      '<span class="qa-step">' +
      (at > 0 ? '<button type="button" class="qa-link" data-qa="' + recs[at - 1].id + '">&lsaquo; Earlier attempt</button>' : '') +
      (at < recs.length - 1 ? '<button type="button" class="qa-link" data-qa="' + recs[at + 1].id + '">Later attempt &rsaquo;</button>' : '') +
      '</span></div>';
    var html = nav +
      '<h2>Attempt ' + (at + 1) + ' of ' + recs.length + '</h2>' +
      '<p class="qa-meta">' + stamp(r) + ' &middot; <b class="' + grade(p) + '">' + p + '%</b> (' + r.s + ' of ' + r.n + ' correct)' +
        (dur(r.ms) ? ' &middot; ' + dur(r.ms) : '') + (r.ex ? ' &middot; exam mode' : '') + '</p>';
    if (lost) {
      html += '<p class="qa-gone">This quiz&rsquo;s questions have changed since this attempt, so they can&rsquo;t be shown again. The score above is kept.</p>';
    } else {
      html += '<div class="qa-filter" role="group" aria-label="Show questions">' +
        '<button type="button" class="qa-f" data-f="all">All ' + r.n + '</button>' +
        '<button type="button" class="qa-f" data-f="ok">Correct ' + ok + '</button>' +
        '<button type="button" class="qa-f" data-f="bad">Missed ' + (r.n - ok) + (skip ? ' (' + skip + ' skipped)' : '') + '</button>' +
        '</div><div class="qa-list">';
      for (var k = 0; k < r.n; k++) html += item(r, k, same);
      html += '<p class="qa-none" hidden>Nothing to show here.</p></div>';
    }
    html += nav.replace('qa-nav"', 'qa-nav qa-nav-end"');
    view.innerHTML = html;
    applyFilter();
    return true;
  }

  function visibleEl(el) { return !!el && el.style.display !== "none" && !!(el.offsetWidth || el.offsetHeight); }
  function openView(id) {
    if (!view) {
      view = document.createElement("div");
      view.id = "qa-view";
      view.className = "card res qa-view";
      view.setAttribute("tabindex", "-1");
      var foot = document.getElementById("resultsfoot") || results;
      foot.parentNode.insertBefore(view, foot.nextSibling);
    }
    var opening = !view.style.display || view.style.display === "none";
    if (opening) {
      from = visibleEl(results) ? "results" : "start";
      fromY = window.scrollY || 0;
    }
    filter = "all";
    if (!render(id)) return;
    // the phone's Back closes the viewer rather than leaving the quiz (as the study-guide panel does)
    if (opening && !pushed) { try { history.pushState({ qaView: 1 }, ""); pushed = true; } catch (e) {} }
    [start, results, document.getElementById("resultsfoot")].forEach(function (el) { if (el) el.style.display = "none"; });
    view.style.display = "block";
    window.scrollTo(0, 0);   // the page header above the card keeps the fixed corner buttons clear of its top row
    try { view.focus({ preventScroll: true }); } catch (e) {}
  }
  function closeView(viaPop) {
    if (!view || view.style.display === "none") return;
    if (pushed) { pushed = false; if (!viaPop) { try { history.back(); } catch (e) {} } }
    view.style.display = "none";
    view.innerHTML = "";
    var show = from === "results" ? [results, document.getElementById("resultsfoot")] : [start];
    show.forEach(function (el) { if (el) el.style.display = el === start ? "" : "block"; });
    if (from === "results") placeList(results, results.querySelector(".resbtns"));
    else placeList(start, null);
    window.scrollTo(0, fromY);
  }

  document.addEventListener("click", function (e) {
    var t = e.target && e.target.closest ? e.target : null;
    if (!t) return;
    var b = t.closest("[data-qa]");
    if (b && (start.contains(b) || results.contains(b) || (view && view.contains(b)))) { e.preventDefault(); openView(b.getAttribute("data-qa")); return; }
    if (view && t.closest(".qa-back") && view.contains(t)) { e.preventDefault(); closeView(); return; }
    var f = t.closest(".qa-f");
    if (f && view && view.contains(f)) { filter = f.getAttribute("data-f"); applyFilter(); }
  });
  /* Escape closes the viewer, but not while something sits on top of it (an enlarged picture, the
     study-guide panel, the shortcuts help, the report form) or the student is typing elsewhere (Pip).
     Captured on window so it runs before those overlays' own handlers close them. */
  function overlayUp() {
    if (document.querySelector(".lb-overlay.open, .shortcuts-overlay.open, .gl-root")) return true;
    var m = document.querySelectorAll("[aria-modal='true']");   // the picture viewer keeps the attribute while hidden
    for (var i = 0; i < m.length; i++) if (m[i].getClientRects().length) return true;
    return false;
  }
  window.addEventListener("keydown", function (e) {
    if (e.key !== "Escape" || !view || view.style.display !== "block" || overlayUp()) return;
    var tg = e.target;
    if (tg && tg.closest && !view.contains(tg) && tg.closest("input, textarea, select, [contenteditable='true']")) return;
    closeView();
  }, true);
  window.addEventListener("popstate", function (e) {
    if (!pushed || (e.state && e.state.qaView)) return;   // landing back on the viewer's own entry keeps it open
    closeView(true);
  });

  /* ---------- wiring ---------- */
  function decorateResults() {
    if (!latestId) return;
    var big = results.querySelector(".big");
    if (big && !results.querySelector(".qa-res")) {
      var row = document.createElement("div");
      row.className = "qa-res";
      var n = 0; list().forEach(function (r) { if (r.id === latestId) n = r.n; });
      if (!n) return;
      row.innerHTML = '<button type="button" class="btn btn-ghost" data-qa="' + latestId + '">Review all ' + n +
        ' questions, right and wrong &rarr;</button>';
      big.parentNode.insertBefore(row, big.nextSibling);
    }
    if (!results.querySelector(".qa-past")) placeList(results, results.querySelector(".resbtns"));
  }
  function shownEl() { return !!(results.offsetWidth || results.offsetHeight || results.getClientRects().length); }
  // once per finish, told apart by the engine's answers array (see the recorder above)
  var lastRef = null;
  function check() {
    if (!shownEl()) return;
    var ref = globalOf("answers");
    if (ref && ref !== lastRef) { lastRef = ref; record(); }
    decorateResults();
  }
  new MutationObserver(check).observe(results, { childList: true, attributes: true, attributeFilter: ["class", "style", "hidden"] });
  check();

  placeList(start, null);
  // quiz.html#attempts (the link on My Progress) opens the list
  function deepLink() {
    var past = start.querySelector(":scope > .qa-past");
    if (!past || location.hash !== "#attempts" || !visibleEl(start)) return;
    past.open = true;
    setTimeout(function () { try { past.scrollIntoView({ block: "start" }); } catch (e) {} }, 60);
  }
  deepLink();
  window.addEventListener("hashchange", deepLink);
  // a signed-in student's attempts from another device arrive after load
  window.addEventListener("storage", function (e) { if (e.key === KEY && visibleEl(start)) placeList(start, null); });
})();

/* ============================================================
   Report entry points, guaranteed (2026-08-02)
   ------------------------------------------------------------
   A student found a wrong answer mid-quiz and had nowhere to report it: the
   quiz pages carried the report link only inside #resultsfoot, which stays
   hidden until you finish. Reporting a bad question should not require
   completing the quiz containing it first.

   Two guarantees, applied here so every page gets them without being touched
   and so anything built later inherits them:

     1. While a quiz is running, a report link sits under the question. It
        carries the question with it (see reportContext).
     2. Any page with no report affordance at all gets one in the footer.

   Both no-op on pages that already show a visible link.
   ============================================================ */
(function () {
  if (!window.reportMistake) return;

  function styleLink(a, extra) {
    a.href = "#";
    a.className = "report-link-auto";
    a.style.cssText = "cursor:pointer;" + (extra || "");
    a.addEventListener("click", function (e) { e.preventDefault(); window.reportMistake(); });
    return a;
  }

  // 1. in-quiz link, so a bad question can be reported while you are looking at it
  var quiz = document.getElementById("quiz");
  if (quiz && !quiz.querySelector(".report-link-auto")) {
    var row = document.createElement("p");
    row.style.cssText = "text-align:center;margin:14px 0 2px;";
    var a = styleLink(document.createElement("a"));
    a.textContent = "Something wrong with this question? Report it";
    row.appendChild(a);
    quiz.appendChild(row);
  }

  // 2. every page gets at least one way in
  function hasVisibleReport() {
    var found = false;
    document.querySelectorAll("a,button").forEach(function (el) {
      if (found || el.classList.contains("report-link-auto")) return;
      var oc = el.getAttribute("onclick") || "";
      if (oc.indexOf("reportMistake") !== -1 && el.offsetParent !== null) found = true;
    });
    return found;
  }

  function ensureFooterLink() {
    if (document.querySelector("footer .report-link-auto")) return;
    if (hasVisibleReport()) return;
    var host = document.querySelector("footer") || document.body;
    var p = document.createElement("p");
    p.className = "report-foot-auto";
    p.style.cssText = "text-align:center;margin:26px 0 18px;";
    var a = styleLink(document.createElement("a"));
    a.textContent = "See a mistake on this page? Report it";
    p.appendChild(a);
    host.appendChild(p);
  }

  // the results footer only becomes visible at the end, so re-check then
  ensureFooterLink();
  var results = document.getElementById("resultsfoot") || document.getElementById("results");
  if (results && window.MutationObserver) {
    new MutationObserver(function () {
      var foot = document.querySelector(".report-foot-auto");
      if (foot && hasVisibleReport()) foot.remove();
    }).observe(results, { attributes: true, attributeFilter: ["style", "class"] });
  }
})();

/* ==========================================================================
   Image lightbox
   --------------------------------------------------------------------------
   Jaxon, 2026-08-27: "add so we can click on the images on this and future
   guide and it blowes it up so we can really see it in good detail and then
   press escape or a X to go back."

   Lives here rather than in any one page so every guide, chart and cram sheet
   that already loads theme.js picks it up with no markup changes, and anything
   built from the templates later gets it for free.

   WHAT IS DELIBERATELY EXCLUDED:
   - .pm-wrap images (practicum study/drill photographs). Their labels are
     percent-positioned SIBLINGS of the <img>, not part of the pixels, so
     enlarging the image on its own would show an unlabelled photo -- strictly
     worse than not zooming. They also already own the click for the drill.
   - images inside a link/button/label, which have their own click meaning.
   - anything marked [data-nozoom] or .nozoom, for future opt-outs.
   - icons and rules under 80px, which have no detail to reveal.
   ========================================================================== */
(function () {
  "use strict";
  if (!document.querySelector || !document.body) return;
  if (!Element.prototype.closest) return;           // ancient browser: skip quietly

  var cands = [];
  var imgs = [];
  var idx = -1;
  var lastFocus = null;
  var overlay, stage, big, cap, count, btnPrev, btnNext, btnZoom;

  function eligible(im) {
    if (im.closest(".pm-wrap")) return false;
    if (im.closest("a, button, label")) return false;
    if (im.hasAttribute("data-nozoom")) return false;
    if ((" " + im.className + " ").indexOf(" nozoom ") > -1) return false;
    return true;
  }

  /* An icon or a hairline rule has no detail to reveal, so it should not get a
     zoom cursor. Size can only be judged once the bitmap is in, and figures far
     down a chart are loading="lazy", so this is re-evaluated rather than fixed
     at startup: naturalWidth when the image has loaded, the laid-out box while
     it has not. */
  function isBig(im) {
    var w = im.naturalWidth || im.offsetWidth || 0;
    var h = im.naturalHeight || im.offsetHeight || 0;
    return w >= 80 && h >= 80;
  }

  /* Rebuilt on every open so the counter and arrow keys only ever walk images
     that actually resolved -- a broken or still-pending figure would otherwise
     leave a dead slot in the sequence. */
  function refresh() {
    imgs = [];
    for (var i = 0; i < cands.length; i++) {
      if (isBig(cands[i])) imgs.push(cands[i]);
    }
  }

  function captionFor(im) {
    var fig = im.closest("figure");
    var fc = fig && fig.querySelector("figcaption");
    var text = fc ? fc.textContent : (im.getAttribute("alt") || "");
    return text.replace(/\s+/g, " ").trim();
  }

  function build() {
    overlay = document.createElement("div");
    overlay.className = "lb-overlay";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-label", "Enlarged image");

    var bar = document.createElement("div");
    bar.className = "lb-bar";

    count = document.createElement("span");
    count.className = "lb-count";

    btnPrev = document.createElement("button");
    btnPrev.type = "button";
    btnPrev.className = "lb-btn";
    btnPrev.innerHTML = "&larr;";
    btnPrev.title = "Previous image (left arrow)";
    btnPrev.setAttribute("aria-label", "Previous image");

    btnNext = document.createElement("button");
    btnNext.type = "button";
    btnNext.className = "lb-btn";
    btnNext.innerHTML = "&rarr;";
    btnNext.title = "Next image (right arrow)";
    btnNext.setAttribute("aria-label", "Next image");

    btnZoom = document.createElement("button");
    btnZoom.type = "button";
    btnZoom.className = "lb-btn";
    btnZoom.textContent = "Zoom in";
    btnZoom.title = "Toggle magnification";

    var spacer = document.createElement("span");
    spacer.className = "lb-spacer";

    var btnX = document.createElement("button");
    btnX.type = "button";
    btnX.className = "lb-btn lb-x";
    btnX.innerHTML = "&#10005;";
    btnX.title = "Close (Esc)";
    btnX.setAttribute("aria-label", "Close");

    bar.appendChild(count);
    bar.appendChild(btnPrev);
    bar.appendChild(btnNext);
    bar.appendChild(btnZoom);
    bar.appendChild(spacer);
    bar.appendChild(btnX);

    stage = document.createElement("div");
    stage.className = "lb-stage";
    big = document.createElement("img");
    big.alt = "";
    stage.appendChild(big);

    cap = document.createElement("div");
    cap.className = "lb-cap";

    overlay.appendChild(bar);
    overlay.appendChild(stage);
    overlay.appendChild(cap);
    document.body.appendChild(overlay);

    btnX.addEventListener("click", close);
    btnPrev.addEventListener("click", function () { step(-1); });
    btnNext.addEventListener("click", function () { step(1); });
    btnZoom.addEventListener("click", function () { toggleZoom(); });
    // backdrop click closes; clicks on the image itself are handled separately
    overlay.addEventListener("click", function (e) {
      if (e.target === overlay || e.target === stage) close();
    });
    big.addEventListener("click", function (e) { toggleZoom(e); });
    wirePan();
  }

  function isZoomed() { return overlay.classList.contains("zoomed"); }

  /* Magnify to twice the size the image is currently displayed at, keeping the
     point that was clicked under the cursor. Natural size is NOT the target --
     several of these figures are downscaled slide captures, so "actual size"
     could be smaller than the fitted view and zooming in would shrink them. */
  function toggleZoom(e) {
    if (isZoomed()) {
      overlay.classList.remove("zoomed");
      big.style.width = "";
      btnZoom.textContent = "Zoom in";
      return;
    }
    var r = big.getBoundingClientRect();
    var target = r.width * 2;
    // relative position of the click within the image, 0..1
    var fx = e && e.clientX != null ? (e.clientX - r.left) / r.width : 0.5;
    var fy = e && e.clientY != null ? (e.clientY - r.top) / r.height : 0.5;
    if (!isFinite(fx)) fx = 0.5;
    if (!isFinite(fy)) fy = 0.5;
    overlay.classList.add("zoomed");
    big.style.width = target + "px";
    btnZoom.textContent = "Zoom out";
    // re-centre after layout settles
    var sr = stage.getBoundingClientRect();
    stage.scrollLeft = fx * big.offsetWidth - sr.width / 2;
    stage.scrollTop = fy * big.offsetHeight - sr.height / 2;
  }

  /* Drag to pan while magnified. */
  function wirePan() {
    var down = false, sx = 0, sy = 0, sl = 0, st = 0;
    big.addEventListener("mousedown", function (e) {
      if (!isZoomed()) return;
      down = true; sx = e.clientX; sy = e.clientY;
      sl = stage.scrollLeft; st = stage.scrollTop;
      big.classList.add("dragging");
      e.preventDefault();
    });
    window.addEventListener("mousemove", function (e) {
      if (!down) return;
      stage.scrollLeft = sl - (e.clientX - sx);
      stage.scrollTop = st - (e.clientY - sy);
    });
    window.addEventListener("mouseup", function (e) {
      if (!down) return;
      down = false;
      big.classList.remove("dragging");
      // a drag should not also count as the click that zooms back out
      if (Math.abs(e.clientX - sx) > 4 || Math.abs(e.clientY - sy) > 4) {
        var swallow = function (ev) { ev.stopPropagation(); };
        big.addEventListener("click", swallow, true);
        setTimeout(function () { big.removeEventListener("click", swallow, true); }, 0);
      }
    });
  }

  function show(i) {
    if (i < 0 || i >= imgs.length) return;
    idx = i;
    var src = imgs[i];
    overlay.classList.remove("zoomed");
    big.style.width = "";
    btnZoom.textContent = "Zoom in";
    big.src = src.currentSrc || src.src;
    big.alt = src.getAttribute("alt") || "";
    cap.textContent = captionFor(src);
    count.textContent = imgs.length > 1 ? (i + 1) + " / " + imgs.length : "";
    btnPrev.disabled = imgs.length < 2;
    btnNext.disabled = imgs.length < 2;
    stage.scrollLeft = 0;
    stage.scrollTop = 0;
  }

  function step(d) {
    if (imgs.length < 2) return;
    show((idx + d + imgs.length) % imgs.length);
  }

  function open(i) {
    lastFocus = document.activeElement;
    overlay.classList.add("open");
    document.documentElement.style.overflow = "hidden";
    show(i);
    setTimeout(function () { overlay.querySelector(".lb-x").focus(); }, 0);
  }

  function close() {
    overlay.classList.remove("open");
    overlay.classList.remove("zoomed");
    big.removeAttribute("src");
    big.style.width = "";
    document.documentElement.style.overflow = "";
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function arm(im) {
    if (im.__lb || !eligible(im)) return;
    im.__lb = 1;
    cands.push(im);
    function mark() {
      if (!isBig(im)) return;
      im.classList.add("lb-able");
      if (!im.getAttribute("title")) im.setAttribute("title", "Click to enlarge");
    }
    mark();
    if (!im.complete) im.addEventListener("load", mark, { once: true });
    im.addEventListener("click", function () {
      if (!isBig(im)) return;
      ensure();
      refresh();
      var n = imgs.indexOf(im);
      if (n > -1) open(n);
    });
  }

  /* Built on first use rather than on every page: most quiz pages carry no
     content images at all and have no business growing a hidden overlay. */
  function ensure() {
    if (overlay) return;
    build();
    document.addEventListener("keydown", function (e) {
      if (!overlay.classList.contains("open")) return;
      if (e.key === "Escape") { e.preventDefault(); close(); }
      else if (e.key === "ArrowRight") { e.preventDefault(); step(1); }
      else if (e.key === "ArrowLeft") { e.preventDefault(); step(-1); }
    });
  }

  function init() {
    var found = document.querySelectorAll("body > .wrap img");
    for (var i = 0; i < found.length; i++) arm(found[i]);
    if (cands.length) ensure();

    /* The Practicum Atlas renders its plates from JS after load, and re-renders
       them on every filter change, so a one-shot scan at DOMContentLoaded would
       arm nothing there. Re-arming is idempotent via the __lb flag. */
    if (window.MutationObserver) {
      new MutationObserver(function (muts) {
        for (var m = 0; m < muts.length; m++) {
          var added = muts[m].addedNodes;
          for (var n = 0; n < added.length; n++) {
            var node = added[n];
            if (node.nodeType !== 1) continue;
            if (node.tagName === "IMG") {
              if (node.closest("body > .wrap")) { arm(node); ensure(); }
            } else if (node.querySelectorAll) {
              var sub = node.querySelectorAll("img");
              for (var k = 0; k < sub.length; k++) {
                if (sub[k].closest("body > .wrap")) { arm(sub[k]); ensure(); }
              }
            }
          }
        }
      }).observe(document.body, { childList: true, subtree: true });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();

// (The guide hero "Details" toggle now lives in theme-guide.js.)


/* ============================================================
   Icon pass over chrome the engine or older markup writes as glyphs
   (design review item 14). Generated quiz pages spell the toolbar with
   text glyphs (flag, three-line menu, pause bars) and the engine rewrites
   the Flag button's innerHTML on every toggle, so this re-applies on
   mutation rather than once. Report links everywhere lose their stars and
   italics and gain the flag icon. Back links' text arrows become the
   arrow icon. No generated file is edited.
   ============================================================ */
(function () {
  var GLYPH = /^\s*[\u2190\u2605\u2691\u2630\u275A\u25A0\u25A1][\s\u2190\u2605\u2691\u2630\u275A\u25A0\u25A1]*/;
  function iconize(el, name, size) {
    // only a control that STARTS with a text glyph; one that already carries
    // an svg (Arcade's and Review's back links) is left alone
    if (!el || el.querySelector("svg")) return;
    var t = el.firstChild;
    if (!t || t.nodeType !== 3 || !GLYPH.test(t.nodeValue)) return;
    t.nodeValue = t.nodeValue.replace(GLYPH, "");
    // the words become their own span so a phone can show the icon alone
    var label = document.createElement("span");
    label.className = "si-label";
    label.textContent = t.nodeValue.replace(/\s+$/, "");
    el.replaceChild(label, t);
    el.insertAdjacentHTML("afterbegin", window.SiteIcon(name, size || 15));
    el.classList.add("has-si");
    // keeps the button named when a phone hides the words
    if (el.tagName === "BUTTON") el.setAttribute("aria-label", el.textContent.replace(/\s+/g, " ").trim());
  }
  function pass(root) {
    root = root || document;
    iconize(document.getElementById("flagbtn"), "flag");
    iconize(document.getElementById("navbtn"), "grid");
    iconize(document.getElementById("pausebtn"), "pause", 13);
    root.querySelectorAll(".sq-flag").forEach(function (b) { iconize(b, "flag", 13); });
    document.querySelectorAll("a.back-link, .guide-back-link, body > .wrap > a[href$='index.html']:first-child, .wrap > a.back").forEach(function (a) {
      iconize(a, "arrowLeft", 15);
    });
    document.querySelectorAll("a.report-link-auto, a[onclick*='reportMistake']").forEach(function (a) {
      if (a.classList.contains("report-link")) return;
      if (a.closest(".question-issue-row, .corner-btn, button")) return;
      // strip the decorative stars around the link, in it and beside it
      a.childNodes.forEach(function (n) { if (n.nodeType === 3) n.nodeValue = n.nodeValue.replace(/\s*★\s*/g, " ").replace(/^\s+|\s+$/g, ""); });
      var p = a.parentElement;
      if (p) {
        p.childNodes.forEach(function (n) { if (n.nodeType === 3 && /★/.test(n.nodeValue)) n.nodeValue = n.nodeValue.replace(/★/g, "").replace(/^\s+$/, ""); });
        if (p.style && p.style.fontStyle === "italic") p.style.fontStyle = "normal";
      }
      a.classList.add("report-link");
      a.style.fontStyle = "normal";
      a.insertAdjacentHTML("afterbegin", window.SiteIcon("flag", 13) + " ");
    });
  }
  function start() {
    pass();
    var quiz = document.getElementById("quiz");
    if (quiz && window.MutationObserver) {
      var pending = false;
      new MutationObserver(function () {
        if (pending) return;
        pending = true;
        requestAnimationFrame(function () { pending = false; pass(quiz); });
      }).observe(quiz, { childList: true, subtree: true });
    }
    // footer links are injected by the report-entry IIFE; catch late ones
    setTimeout(pass, 600);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();


/* ============================================================
   BOLD THE LEAD-IN (design-review leftovers item 3, 2026-09-27).
   Since item 10 the stem is regular weight; the question sentence itself
   ("Which is the most appropriate next step?") is now set bold, so the
   varied lead-ins read at a glance. Done here at display time rather than
   by re-rendering 300 generated quizzes: the engine writes each stem with
   textContent into #qtext (paged view) and .qtext (all-on-a-page view);
   this splits that one text node at the start of the final sentence and
   wraps the tail in <strong class="q-lead">. The text itself (and so
   textContent, the report form's context, copy/paste and answer checking,
   which never reads the stem) is unchanged. Scope: pages tools/dark_tokens.py
   opted in as body[data-dark-kind="quiz"], i.e. Semester 2+ generated
   quizzes only; Semester 1 (frozen) and Group Study never carry it.
   Imperative lead-ins ("Name the condition shown.") count too; a
   one-sentence stem is all lead-in, so it is all bold.
   ============================================================ */
(function () {
  if (typeof MutationObserver !== "function") return;
  // Returns the index where the stem's final sentence (the lead-in) starts.
  // Not a sentence end: a title or Latin abbreviation, or a middle initial
  // after a capitalised name ("Tom G. Prince"); "amphotericin B." still ends one.
  var ABBR = /(?:(?:^|[\s(])(?:Dr|Drs|Mr|Mrs|Ms|St|Sr|Jr|vs|etc|approx|No|Fig|e\.g|i\.e|cf|al|Inc|Prof|U\.S|a\.m|p\.m)|\b[A-Z][a-z]+ [A-Z])\.["”’')\]]*$/;
  function leadStart(t) {
    var re = /[.?!]["”’')\]]*\s+(?=["“‘(]?[A-Z0-9])/g, m, start = 0;
    var end = t.replace(/\s+$/, "").length;
    while ((m = re.exec(t))) {
      var cut = m.index + m[0].length;
      if (cut >= end) break;
      if (ABBR.test(t.slice(0, m.index + 1 + (m[0].match(/^[.?!]["”’')\]]*/)[0].length - 1)))) continue;
      start = cut;
    }
    return start;
  }

  function bolden(el) {
    var n = el.firstChild;
    if (!n || n !== el.lastChild || n.nodeType !== 3) return;   // already split, empty, or not plain text
    var t = n.data;
    if (!t.trim()) return;
    var s = leadStart(t);
    var b = document.createElement("strong");
    b.className = "q-lead";
    var tail = s > 0 ? n.splitText(s) : n;
    el.replaceChild(b, tail);
    b.appendChild(tail);
  }
  function pass(quiz) {
    var list = quiz.querySelectorAll(".qtext");
    for (var i = 0; i < list.length; i++) bolden(list[i]);
  }
  function start() {
    if (!document.body || document.body.getAttribute("data-dark-kind") !== "quiz") return;
    var quiz = document.getElementById("quiz");
    if (!quiz) return;
    pass(quiz);
    new MutationObserver(function () { pass(quiz); })
      .observe(quiz, { childList: true, subtree: true });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();


/* ============================================================
   STUDY-GUIDE PEEK (2026-09-28). Under every explanation, a button opens the
   study-guide passage that teaches the question, in a panel INSIDE the quiz.
   Nothing navigates: the question, the answer, the timer and every saved
   state stay exactly where they were, and closing the panel (x, Esc, tapping
   outside, or the phone's Back button) returns to the same question. That is
   the point of doing it as a panel and not a link.

   Data: <exam folder>/guide-links.json, written by tools/build_guide_links.py
   and keyed by an FNV-1a hash of "<stem>\n<correct option text>", so an edited
   question has no entry and shows no button. No file (or a 404) = the feature
   is simply absent. Scope: body[data-dark-kind="quiz"], i.e. Semester 2+
   generated quizzes; Semester 1 (frozen) and Group Study never carry it.

   The guide is fetched as text and shown in a same-origin srcdoc iframe with
   every <script> removed, so an embedded guide runs none of theme.js: no
   analytics hit, no presence write, no sign-in prompt, no second Firebase.
   All the work (theme, hiding the guide's own chrome, opening any <details>,
   scrolling, highlighting) is done from out here on the iframe's document.

   Where buttons go (all rebuilt by the engine, so a MutationObserver re-adds
   them): #expl after an answer, #sexpl-N in the all-on-a-page view, and every
   .mitem in the results review (matched to its question by stem).
   ============================================================ */
(function () {
  if (typeof MutationObserver !== "function" || !window.fetch) return;
  var links = null, failed = false, requested = false;
  var root = null, lastTrigger = null, pushed = false, scheduled = false;
  var guideCache = {};

  function fnv(s) {
    var h = 0x811c9dc5;
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 0x01000193); }
    return (h >>> 0).toString(36);
  }
  function keyOf(q) { return fnv(q.q + "\n" + q.opts[q.c][0]); }
  function bank() { try { return QUESTIONS; } catch (e) { return null; } }
  function cur() { try { return order; } catch (e) { return null; } }

  function load() {
    if (requested) return;
    requested = true;
    fetch(new URL("guide-links.json", location.href).href)
      .then(function (r) { if (!r.ok) throw 0; return r.json(); })
      .then(function (j) {
        if (!j || j.v !== 1 || !j.l || !j.g) throw 0;
        links = j; schedule();
      })
      .catch(function () { failed = true; });
  }

  function makeBtn(q) {
    var k = keyOf(q), L = links.l[k];
    if (!L) return null;
    var b = document.createElement("button");
    b.type = "button";
    b.className = "gl-btn";
    b.setAttribute("data-gl", k);
    b.innerHTML = window.SiteIcon("book", 17) +
      '<span class="gl-txt"><span class="gl-kicker"></span><span class="gl-title"></span></span>' +
      window.SiteIcon("arrowRight", 15);
    // three honest tiers: the paragraph itself / the section that holds it / the
    // section where that slide's material lives (the guide may not spell it out)
    b.querySelector(".gl-kicker").textContent = L[4] ? "Closest section in the study guide"
      : (L[3] ? "Find it in the study guide" : "Find it in this section of the study guide");
    b.querySelector(".gl-title").textContent = L[2];
    return b;
  }

  // Put (or replace, or remove) the button inside `host` for question `q`.
  function place(host, q) {
    var old = host.querySelector(":scope > .gl-btn");
    var want = q && links.l[keyOf(q)] ? keyOf(q) : null;
    if (old && old.getAttribute("data-gl") === want) return;
    if (old) old.remove();
    if (!want) return;
    host.appendChild(makeBtn(q));
  }

  function pass() {
    scheduled = false;
    var Q = bank();
    if (!Q || !links) return;
    var ord = cur();
    // paged view: the live explanation panel
    var ex = document.getElementById("expl");
    if (ex && ex.classList.contains("show") && ord && typeof idx === "number") {
      var q0 = Q[ord[idx]];
      if (q0) place(ex, q0);
    }
    // all-on-a-page view
    var sx = document.querySelectorAll('[id^="sexpl-"].show');
    for (var i = 0; i < sx.length; i++) {
      var n = parseInt(sx[i].id.slice(6), 10);
      if (ord && !isNaN(n) && Q[ord[n]]) place(sx[i], Q[ord[n]]);
    }
    // results review and the attempt viewer: each item carries "Q7. <stem>"
    var items = document.querySelectorAll("#results .mitem, #qa-view .mitem");
    for (var j = 0; j < items.length; j++) {
      var mq = items[j].querySelector(".mq");
      if (!mq) continue;
      var stem = mq.textContent.replace(/^\s*Q\d+\.\s*/, "").replace(/\s+/g, " ").trim();
      var hit = null;
      for (var m = 0; m < Q.length; m++) {
        if (Q[m].q.replace(/\s+/g, " ").trim() === stem) { hit = Q[m]; break; }
      }
      if (hit) place(items[j], hit);
    }
  }
  function schedule() {
    if (scheduled) return;
    scheduled = true;
    (window.requestAnimationFrame || setTimeout)(pass);
  }

  /* ---------- the panel ---------- */
  var MARK_CSS =
    ".gl-mark{background:#fef3d4!important;color:#3a2c05!important;box-shadow:0 0 0 4px #fef3d4,0 0 0 5px #e8c766;border-radius:4px}" +
    ":root[data-theme='dark'] .gl-mark{background:#4a3a12!important;color:#f7ecc8!important;box-shadow:0 0 0 4px #4a3a12,0 0 0 5px #7a6220}" +
    ".gl-head-mark{scroll-margin-top:10px;border-left:4px solid #e8c766;padding-left:10px!important}" +
    // the sentence Pip quoted (o.quote): the Guides amber, derived from the site tokens, plus an underline
    // so it never rests on color alone; authored light under the older invert-filter dark mode
    ".gl-quote{background:var(--a-amber-soft,#fff2e8)!important;background:color-mix(in oklab,var(--a-amber,#ad631e) 22%,transparent)!important;" +
    "color:inherit!important;border-radius:3px;box-shadow:inset 0 -2px 0 var(--a-amber,#ad631e);padding:1px 0;" +
    "-webkit-box-decoration-break:clone;box-decoration-break:clone}" +
    ":root[data-theme='dark'] body:not([data-dark='tokens']) .gl-quote{background:#eddcce!important;box-shadow:inset 0 -2px 0 #ad631e}" +
    "@media (forced-colors:active){.gl-quote{forced-color-adjust:none;background:Mark!important;color:MarkText!important;box-shadow:none;outline:1px solid CanvasText}}";
  var CHROME_CSS =
    ".guide-back-bar,header.top,nav.toc,#quiz-footer-logo,#pull-refresh,.guide-foot,.word-btn," +
    ".corner-btn,[class*='floating'],.toc-fab{display:none!important}" +
    "html,body{margin:0!important;padding:0!important}" +
    ".layout{display:block!important;max-width:none!important;margin:0!important;padding:10px 16px 60vh!important}" +
    "main{max-width:none!important;margin:0!important;padding:0!important}" +
    MARK_CSS;
  // Expanded ("Full guide"): the whole guide with its contents sidebar; only the bits that
  // need scripts or navigation away from the quiz stay hidden.
  var FULL_CSS =
    ".guide-back-bar,#quiz-footer-logo,#pull-refresh,.word-btn{display:none!important}" + MARK_CSS;

  function textOf(el) { return (el.textContent || "").replace(/\s+/g, ""); }

  function findBlock(doc, target, snippet) {
    var want = snippet.replace(/\s+/g, "");
    if (!want) return null;
    var all = doc.querySelectorAll("li,p,tr,dd,dt,blockquote,figcaption,summary,td");
    var first = null;
    for (var i = 0; i < all.length; i++) {
      var el = all[i];
      if (target && !(target.compareDocumentPosition(el) & 4) && !target.contains(el)) continue;   // at/after the section heading
      if (textOf(el).indexOf(want) !== -1) { first = el; break; }
    }
    if (!first) return null;
    var best = first, bestLen = textOf(first).length;      // the most specific block inside it
    for (var j = 0; j < all.length; j++) {
      var c = all[j];
      if (c !== first && first.contains(c) && textOf(c).indexOf(want) !== -1 && textOf(c).length < bestLen) { best = c; bestLen = textOf(c).length; }
    }
    return best;
  }

  /* The exact sentence Claude cited (o.quote, 2026-10-15): found in the anchored section first, then
     anywhere in the guide, comparing text with whitespace collapsed, curly quotes and dashes made plain
     and case ignored; wrapped in <mark class="gl-quote"> pieces (one per text node, so no element is
     ever split). Returns the marks, or null when the words are not there. */
  var Q_SKIP = "script, style, noscript, template, svg, nav, .guide-back-bar, header.top";   // hidden in the panel or not text
  // one-for-one character folding (so offsets carry over): quotes, dashes, case; whitespace is collapsed separately
  function qFold(s) {
    var l = s.toLowerCase();
    if (l.length !== s.length) l = s;      // a character whose lower case is longer (rare): compare it as written
    return l.replace(/[‘’‚‛′`]/g, "'").replace(/[“”„‟″]/g, '"').replace(/[‐‑‒–—―−]/g, "-").replace(/…/g, ".");
  }
  function qNorm(s) { return qFold(String(s)).replace(/\s+/g, " ").trim(); }
  function sectionEnd(target) {        // a heading's section runs to the next heading of its rank or higher
    var m = /^H([1-6])$/.exec(target.tagName);
    if (!m) return null;
    var all = target.ownerDocument.querySelectorAll("h1,h2,h3,h4,h5,h6"), seen = false;
    for (var i = 0; i < all.length; i++) {
      if (all[i] === target) { seen = true; continue; }
      if (seen && Number(all[i].tagName.slice(1)) <= Number(m[1])) return all[i];
    }
    return null;
  }
  function markQuote(doc, target, quote) {
    var want = qNorm(String(quote || "")), body = doc.body;
    if (want.replace(/[^a-z0-9]/g, "").length < 4 || !body) return null;
    // the guide's text, folded and with whitespace collapsed, built a text node at a time; seg* record where
    // each copied run starts in `text` and which node / offset it came from, so a match maps back exactly
    var text = "", segAt = [], segNode = [], segOff = [], w = doc.createTreeWalker(body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        return n.parentElement && n.parentElement.closest(Q_SKIP) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
      }
    }), n, ws = /\s+/g, m0, last, endsSpace = true;    // (never read text[i] while building: that flattens it every time)
    while ((n = w.nextNode())) {
      var f = qFold(n.data);
      ws.lastIndex = 0; last = 0;
      while (true) {
        m0 = ws.exec(f);
        var stop = m0 ? m0.index : f.length;
        if (stop > last) { segAt.push(text.length); segNode.push(n); segOff.push(last); text += f.slice(last, stop); endsSpace = false; }
        if (!m0) break;
        if (!endsSpace) { segAt.push(text.length); segNode.push(n); segOff.push(m0.index); text += " "; endsSpace = true; }
        last = m0.index + m0[0].length;
      }
    }
    function at(i) {                    // text index -> [node, offset]
      var lo = 0, hi = segAt.length - 1;
      while (lo < hi) { var mid = (lo + hi + 1) >> 1; if (segAt[mid] <= i) lo = mid; else hi = mid - 1; }
      return [segNode[lo], segOff[lo] + (i - segAt[lo])];
    }
    function find(q) {
      var hits = [], k = text.indexOf(q);
      while (k >= 0 && hits.length < 50) { hits.push(k); k = text.indexOf(q, k + 1); }
      return hits;
    }
    var hits = find(want);
    if (!hits.length) {                // the sentence without its outer quotes or closing punctuation
      want = want.replace(/^["'(\[ ]+|["')\]., ;:!?]+$/g, "");
      if (want.replace(/[^a-z0-9]/g, "").length < 4) return null;
      hits = find(want);
    }
    if (!hits.length) return null;
    // in the anchored section (inside it, or under its heading), else the first one after it, else the first
    var pick = -1, after = -1;
    if (target && target !== body) {
      var end = sectionEnd(target), head = /^H[1-6]$/.test(target.tagName);
      for (var h = 0; h < hits.length && pick < 0; h++) {
        var node = at(hits[h])[0], follows = !!(target.compareDocumentPosition(node) & 4);
        if (target.contains(node) || (head && follows && (!end || (end.compareDocumentPosition(node) & 2)))) pick = hits[h];
        else if (follows && after < 0) after = hits[h];
      }
    }
    if (pick < 0) pick = after >= 0 ? after : hits[0];
    var a = at(pick), b = at(pick + want.length - 1), r = doc.createRange();
    r.setStart(a[0], a[1]); r.setEnd(b[0], b[1] + 1);
    var pieces = [], tw = doc.createTreeWalker(r.commonAncestorContainer.nodeType === 3 ? r.commonAncestorContainer.parentNode : r.commonAncestorContainer, NodeFilter.SHOW_TEXT, null), t;
    while ((t = tw.nextNode())) {
      if (!r.intersectsNode(t)) continue;
      var s0 = t === a[0] ? a[1] : 0, e0 = t === b[0] ? b[1] + 1 : t.data.length;
      if (e0 > s0) pieces.push([t, s0, e0]);
    }
    var marks = [];
    pieces.forEach(function (p) {
      var node = p[0], par = node.parentNode, txt = node.data.slice(p[1], p[2]);
      if (!par || (!/\S/.test(txt) && /^(TABLE|THEAD|TBODY|TFOOT|TR|UL|OL|DL|SELECT)$/.test(par.nodeName))) return;
      var mid = p[1] > 0 ? node.splitText(p[1]) : node;
      if (p[2] - p[1] < mid.data.length) mid.splitText(p[2] - p[1]);
      var m = doc.createElement("mark");
      m.className = "gl-quote";
      mid.parentNode.insertBefore(m, mid);
      m.appendChild(mid);
      marks.push(m);
    });
    if (!marks.length) return null;
    marks[0].title = "The sentence Pip quoted";
    return marks;
  }

  function arrive(frame, L, panel) {
    var doc = frame.contentDocument, win = frame.contentWindow;
    if (!doc || !win) return;
    doc.documentElement.setAttribute("data-theme", document.documentElement.getAttribute("data-theme") || "light");
    var st = doc.createElement("style"); st.textContent = CHROME_CSS; doc.head.appendChild(st);
    frame._glStyle = st;
    var target = L[1] ? doc.getElementById(L[1]) : doc.body;
    if (!target) { panel.querySelector(".gl-load").textContent = "That part of the guide moved. Use “Open full guide”."; return; }
    for (var p = target; p; p = p.parentElement) if (p.tagName === "DETAILS") p.open = true;
    var quoted = null;
    if (L[6]) { try { quoted = markQuote(doc, target, L[6]); } catch (e) { quoted = null; } }
    var hit = quoted ? quoted[0] : (L[3] ? findBlock(doc, target, L[3]) : null);
    if (!hit && L[5] && L[3] && L[3].length > 90) hit = findBlock(doc, target, L[3].slice(0, 90));   // Pip's longer passages: match their opening
    if (hit) for (var d = hit; d; d = d.parentElement) if (d.tagName === "DETAILS") d.open = true;
    var mark = hit || target;
    if (quoted) { /* the cited words carry their own mark */ }
    else if (hit) hit.classList.add("gl-mark"); else if (L[1]) target.classList.add("gl-head-mark");
    // Images above the passage load late and push it down, so keep it pinned
    // to the same spot until the student takes over (any scroll gesture / key)
    // or a few seconds pass. Eager loading so the shifts happen now, not as
    // they scroll.
    var pinned = true;
    function align() {
      if (!pinned) return;
      var y = mark.getBoundingClientRect().top + win.pageYOffset - (hit ? Math.max(40, win.innerHeight * 0.28) : 12);
      win.scrollTo(0, Math.max(0, y));
    }
    var imgs = doc.images;
    for (var k = 0; k < imgs.length; k++) imgs[k].loading = "eager";
    frame._glRealign = function () { pinned = true; align(); pinned = false; };
    doc.addEventListener("load", align, true);
    ["wheel", "touchstart", "mousedown", "keydown"].forEach(function (ev) {
      doc.addEventListener(ev, function () { pinned = false; }, { passive: true, capture: true });
    });
    setTimeout(function () { pinned = false; }, 4500);
    align();
    panel.classList.add("is-ready");
  }

  function guideText(url) {
    if (guideCache[url]) return guideCache[url];
    guideCache[url] = fetch(url).then(function (r) { if (!r.ok) throw 0; return r.text(); })
      .then(function (t) {
        t = t.replace(/<script[\s\S]*?<\/script>/gi, "");
        var base = url.split("#")[0];
        return t.replace(/<head([^>]*)>/i, '<head$1><base href="' + base.replace(/"/g, "&quot;") + '">');
      });
    guideCache[url].catch(function () { delete guideCache[url]; });
    return guideCache[url];
  }

  function closePanel(viaPop) {
    if (!root) return;
    root.remove(); root = null;
    document.documentElement.classList.remove("gl-open");
    if (pushed) { pushed = false; if (!viaPop) { try { history.back(); } catch (e) {} } }
    if (lastTrigger && document.contains(lastTrigger)) { try { lastTrigger.focus({ preventScroll: true }); } catch (e) {} }
  }

  function openPanel(key, trigger) {
    var L = links && links.l[key];
    if (!L) return;
    showPanel(L, new URL(links.g[L[0]], location.href).href, trigger, "Back to question", null);
  }
  /* The generic opener (2026-10-11): any page that loads theme.js can open a guide passage in this same
     panel, for Pip's guide links. o = {url (the guide, with or without #anchor), anchor, title, label, passage,
     quote}. quote (2026-10-15, optional): the exact sentence Claude cited; when it is found it is marked
     (gl-quote) and scrolled to instead of the passage's block, and when it is not the panel behaves as
     before. Escape, x, tapping outside or the phone's Back closes it and the page is exactly as it was. */
  window.openGuidePanel = function (o) {
    if (!o || !o.url) return false;
    var u = String(o.url), anchor = o.anchor || "";
    if (!anchor && u.indexOf("#") >= 0) { try { anchor = decodeURIComponent(u.split("#")[1]); } catch (e) { anchor = u.split("#")[1]; } }
    var L = [0, anchor, o.title || "", o.passage || "", 0, 1, typeof o.quote === "string" ? o.quote.slice(0, 1200) : ""];
    showPanel(L, new URL(u, location.href).href.split("#")[0], document.activeElement, "Back to page", o.label || "Study guide");
    return true;
  };
  function showPanel(L, url, trigger, backLabel, kicker) {
    if (root) closePanel(true);
    lastTrigger = trigger;
    root = document.createElement("div");
    root.className = "gl-root";
    root.setAttribute("role", "dialog");
    root.setAttribute("aria-label", "Study guide");
    root.innerHTML =
      '<div class="gl-backdrop"></div>' +
      '<div class="gl-panel">' +
        '<div class="gl-grab" aria-hidden="true"></div>' +
        '<div class="gl-head">' +
          window.SiteIcon("book", 18) +
          '<div class="gl-ht"><div class="gl-hk"></div><div class="gl-hn"></div></div>' +
          '<button type="button" class="gl-full"></button>' +
          '<button type="button" class="gl-x" aria-label="Close study guide"></button>' +
        '</div>' +
        '<div class="gl-body"><div class="gl-load">Loading the guide…</div>' +
          '<iframe class="gl-frame" title="Study guide passage"></iframe></div>' +
      '</div>';
    var panel = root.querySelector(".gl-panel");
    root.querySelector(".gl-hk").textContent = kicker || (L[4] ? "Study guide · closest section"
      : (L[3] ? "Study guide" : "Study guide · this section"));
    root.querySelector(".gl-hn").textContent = L[2];
    // "Full guide" expands THIS panel (no new window, so there is always a way back
    // to the question); the same button then reads "Back to question".
    var full = root.querySelector(".gl-full");
    function setFull(on) {
      panel.classList.toggle("is-full", on);
      full.innerHTML = on ? window.SiteIcon("arrowLeft", 14) + '<span>' + backLabel + '</span>'
                          : '<span>Full guide</span>' + window.SiteIcon("layers", 14);
      var f = root.querySelector(".gl-frame");
      if (f && f._glStyle) { f._glStyle.textContent = on ? FULL_CSS : CHROME_CSS; if (f._glRealign) setTimeout(f._glRealign, 60); }
    }
    full.addEventListener("click", function () { setFull(!panel.classList.contains("is-full")); });
    setFull(false);
    var x = root.querySelector(".gl-x"); x.innerHTML = window.SiteIcon("x", 18);
    x.addEventListener("click", function () { closePanel(false); });
    root.querySelector(".gl-backdrop").addEventListener("click", function () { closePanel(false); });
    document.body.appendChild(root);
    document.documentElement.classList.add("gl-open");
    try { history.pushState({ gl: 1 }, ""); pushed = true; } catch (e) { pushed = false; }
    x.focus({ preventScroll: true });

    var frame = root.querySelector(".gl-frame");
    guideText(url).then(function (t) {
      if (!root || root.querySelector(".gl-frame") !== frame) return;
      frame.addEventListener("load", function () {
        if (!root) return;
        arrive(frame, L, panel);
      }, { once: true });
      frame.srcdoc = t;
    }).catch(function () {
      var ld = root && root.querySelector(".gl-load");
      if (ld) ld.textContent = "The guide could not load here. Use “Full guide” to open it in a new tab.";
    });
  }

  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest(".gl-btn");
    if (b) { e.preventDefault(); openPanel(b.getAttribute("data-gl"), b); }
  });
  document.addEventListener("keydown", function (e) {
    if (root && (e.key === "Escape" || e.key === "Esc")) { e.preventDefault(); closePanel(false); }
  });
  window.addEventListener("popstate", function () { if (root) closePanel(true); });

  function start() {
    if (!document.body || document.body.getAttribute("data-dark-kind") !== "quiz") return;
    if (!document.getElementById("quiz")) return;
    load();
    new MutationObserver(schedule).observe(document.body, { childList: true, subtree: true, attributes: true, attributeFilter: ["class"] });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();


/* ============================================================
   ANSWER FEEDBACK + SCORE RING (2026-09-30)
   ------------------------------------------------------------
   Jaxon: "do 2" from a list of animations to improve. Lives here, not in
   tools/quiz-template/template.html, because the template only applies at
   render time and this must reach all 400+ existing quiz pages.
   - When an option GAINS .correct / .wrong the letter badge gets a check or a cross that
     draws itself (css in theme.css section 7). Options that are rendered with the class
     already set (review lists, exam-mode redraws that remove and re-add it) are left alone,
     which is why this watches class CHANGES rather than looking for the class.
   - When the results ring appears its --p runs from 0 to the score and the number counts up.
   ============================================================ */
(function () {
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  var OK = '<svg class="fx-mark" viewBox="0 0 24 24" aria-hidden="true"><path pathLength="1" d="M6.5 12.8l3.6 3.7 7.4-8.3"/></svg>';
  var BAD = '<svg class="fx-mark" viewBox="0 0 24 24" aria-hidden="true"><path pathLength="1" d="M7.5 7.5l9 9"/><path pathLength="1" d="M16.5 7.5l-9 9"/></svg>';

  function mark(opt, ok) {
    var ltr = opt.querySelector(".ltr");
    if (!ltr) return;
    var old = ltr.querySelector(".fx-mark");
    if (old) old.remove();
    ltr.insertAdjacentHTML("beforeend", ok ? OK : BAD);
    ltr.classList.add("fx-has-mark");
  }
  function unmark(opt) {
    var ltr = opt.querySelector(".ltr");
    if (!ltr || !ltr.classList.contains("fx-has-mark")) return;
    var m = ltr.querySelector(".fx-mark"); if (m) m.remove();
    ltr.classList.remove("fx-has-mark");
  }
  function has(cls, name) { return (" " + cls + " ").indexOf(" " + name + " ") > -1; }

  /* ---- Results reveal (2026-10-01) -------------------------------------------------------------
     The ring fills to the score (as before), the percentage is an ODOMETER whose digits roll into place
     (same technique as the homepage class counter), and the objective rows plus the first few missed
     questions slide in one by one. About 1.5 s in all; ANY click, tap or key skips straight to the end;
     reduced motion shows the final state at once. Nothing here touches scoring: the real "NN%" stays in the
     DOM as visually-hidden text (so scripts that read #results, like the confetti tiers, see the true
     number at every moment) and the rolling digits are CSS-drawn decoration. */
  var ODO_MS = 1000, STAGGER_BASE = 360, STAGGER_STEP = 55, STAGGER_MAX = 10, MISSED_MAX = 4;
  function buildOdometer(b, str) {
    if (!/^\d{1,3}%$/.test(str)) return null;
    var sr = document.createElement("span"); sr.className = "rs-sr"; sr.textContent = str;
    var od = document.createElement("span"); od.className = "rs-od"; od.setAttribute("aria-hidden", "true");
    var cols = [];
    for (var n = 0; n < str.length - 1; n++) {
      var col = document.createElement("span"); col.className = "rs-d";
      var roll = document.createElement("span"); roll.className = "rs-r"; roll.style.setProperty("--d", "0");
      for (var k = 0; k < 10; k++) { var c = document.createElement("span"); c.className = "rs-c"; c.setAttribute("data-d", k); roll.appendChild(c); }
      col.appendChild(roll); od.appendChild(col); cols.push({ el: roll, d: str.charAt(n) });
    }
    var pc = document.createElement("span"); pc.className = "rs-p"; od.appendChild(pc);
    b.textContent = ""; b.appendChild(sr); b.appendChild(od);
    return cols;
  }
  var activeFinish = null;
  function animateRing(ring) {
    if (ring.getAttribute("data-fx") || reduce) return;
    ring.setAttribute("data-fx", "1");
    if (activeFinish) activeFinish();      // a restart that beat the previous show to the end
    var root = document.getElementById("results") || document.body;
    var target = parseFloat(ring.style.getPropertyValue("--p")) || 0;
    var num = ring.querySelector("b"), cols = null, done = false, raf = 0, t0 = null, backstop = 0;

    // stagger: objective rows, then the first few missed questions
    var rows = root.querySelectorAll(".brow"), items = root.querySelectorAll(".missed .mitem"), i, d = 0;
    for (i = 0; i < rows.length && i < STAGGER_MAX; i++, d++) rows[i].style.setProperty("--rs-d", (STAGGER_BASE + d * STAGGER_STEP) + "ms");
    var staged = [].slice.call(rows, 0, STAGGER_MAX);
    for (i = 0; i < items.length && i < MISSED_MAX; i++, d++) {
      items[i].classList.add("rs-it"); items[i].style.setProperty("--rs-d", (STAGGER_BASE + d * STAGGER_STEP) + "ms"); staged.push(items[i]);
    }
    root.classList.add("rs-go");

    if (target > 0) {
      ring.style.setProperty("--p", "0");
      if (num) cols = buildOdometer(num, num.textContent.trim());
      if (cols) {
        void root.offsetWidth;              // flush the 0 digits so the roll is a transition, not a jump
        for (i = 0; i < cols.length; i++) {
          cols[i].el.style.transitionDelay = ((cols.length - 1 - i) * 60) + "ms";   // right-most digit first
          cols[i].el.style.setProperty("--d", cols[i].d);
        }
      }
    }
    function step(ts) {
      if (done) return;
      if (t0 === null) t0 = ts;
      var k = Math.min(1, (ts - t0) / ODO_MS), e = 1 - Math.pow(1 - k, 3);
      ring.style.setProperty("--p", (target * e).toFixed(2));
      if (k < 1) raf = requestAnimationFrame(step);
    }
    if (target > 0) raf = requestAnimationFrame(step);

    function finish() {                      // the end of the show, reached by the clock or by any click
      if (done) return;
      done = true; cancelAnimationFrame(raf); clearTimeout(backstop);
      if (activeFinish === finish) activeFinish = null;
      document.removeEventListener("pointerdown", finish, true);
      document.removeEventListener("keydown", finish, true);
      ring.style.setProperty("--p", String(target));
      if (cols) for (var j = 0; j < cols.length; j++) { cols[j].el.style.transition = "none"; cols[j].el.style.transitionDelay = "0ms"; cols[j].el.style.setProperty("--d", cols[j].d); }
      root.classList.remove("rs-go");
      for (var q = 0; q < staged.length; q++) { staged[q].classList.remove("rs-it"); staged[q].style.removeProperty("--rs-d"); }
    }
    activeFinish = finish;
    document.addEventListener("pointerdown", finish, true);
    document.addEventListener("keydown", finish, true);
    backstop = setTimeout(finish, Math.max(ODO_MS + 200, STAGGER_BASE + staged.length * STAGGER_STEP + 420));
  }

  function start() {
    if (!document.getElementById("opts") && !document.getElementById("results") && !document.querySelector(".opts")) return;
    new MutationObserver(function (list) {
      for (var i = 0; i < list.length; i++) {
        var m = list[i];
        if (m.type === "attributes") {
          var t = m.target;
          if (!t.classList || !t.classList.contains("opt")) continue;
          var was = m.oldValue || "", now = t.className;
          if (has(now, "correct") && !has(was, "correct")) mark(t, true);
          else if (has(now, "wrong") && !has(was, "wrong")) mark(t, false);
          else if (!has(now, "correct") && !has(now, "wrong") && (has(was, "correct") || has(was, "wrong"))) unmark(t);
        } else {
          for (var j = 0; j < m.addedNodes.length; j++) {
            var n = m.addedNodes[j];
            if (n.nodeType !== 1) continue;
            if (n.matches && n.matches(".ring")) animateRing(n);
            else if (n.querySelector) { var r = n.querySelector(".ring"); if (r) animateRing(r); }
          }
        }
      }
    }).observe(document.body, { subtree: true, childList: true, attributes: true, attributeFilter: ["class"], attributeOldValue: true });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();


// (PA Week now lives in theme-seasonal.js.)


/* ============================================================
   GUIDE MOTION (2026-10-01): sections ease in as they are scrolled to, and the Contents list gets a
   sliding marker that follows the section you are reading. Guides, cram sheets and reference pages only
   (body[data-dark-kind] guide / cram / ref).
   ------------------------------------------------------------
   Safety rules, because hiding content is the one thing this must never get wrong:
   - Nothing is hidden unless this script runs to the end: the hidden class is added by script, never
     written in the markup, so JS-off, a script error, the Word export and the "Find it in the study
     guide" panel (which strips scripts) all show everything.
   - Only blocks that start BELOW the first screen are hidden, so nothing visible at load ever flickers.
   - Reaching a block reveals it AND everything before it in the page, so a #hash jump, a Contents click,
     a search hit, Ctrl-F, or a fast scroll can never leave invisible content behind or above you.
   - Print (and beforeprint) reveal everything; reduced motion hides nothing at all.
   - Observed blocks are section-level (callouts, conditions, tables, cards...), not paragraphs, so a long
     guide costs one IntersectionObserver over ~150 elements.
   The marker never reads layout per frame: section positions are cached and refreshed when the page
   changes size, then each scroll frame is a binary search over numbers.
   ============================================================ */
(function () {
  var kind = document.body && document.body.getAttribute("data-dark-kind");
  if (kind !== "guide" && kind !== "cram" && kind !== "ref") return;
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- 1. sections ease in ---------- */
  var UNIT = ".io-box,.callout,.pearl,.cond,.cmp-card,.tbl-wrap,.figgrid,.study,.clip,.scroll,details,h3.sub,.shead";
  var pending = [], ptr = 0, idxOf = typeof WeakMap === "function" ? new WeakMap() : null, io = null;

  function revealUpTo(i, near) {
    for (; ptr <= i && ptr < pending.length; ptr++) {
      var el = pending[ptr];
      if (!near) el.classList.add("rv-now");           // far above or below the screen: no animation to watch
      el.classList.add("rv-in");
      (function (e) { setTimeout(function () { e.classList.remove("rv-p", "rv-in", "rv-now"); }, near ? 520 : 40); })(el);
      if (io) io.unobserve(el);
    }
  }
  function revealAll() { revealUpTo(pending.length - 1, false); }
  function revealThrough(target) {                      // everything before the target, the target's own block, and a little after
    if (!pending.length || !target) return;
    var last = -1;
    for (var i = 0; i < pending.length; i++) {
      var rel = pending[i].compareDocumentPosition(target);
      if (rel & 8 /* contains */ || rel & 4 /* precedes */ || pending[i] === target) last = i;
      else break;
    }
    revealUpTo(Math.min(last + 3, pending.length - 1), false);   // instant: the target must be solid on arrival
  }

  function setupReveal() {
    if (reduce || typeof IntersectionObserver !== "function" || !idxOf) return;
    if (document.documentElement.scrollHeight < window.innerHeight * 1.6) return;
    var H = window.innerHeight, units = [], seen = [];
    var secs = document.querySelectorAll("section");
    for (var s = 0; s < secs.length; s++) {
      var sec = secs[s];
      if (sec.querySelector("section")) continue;
      var kids = [], ch = sec.children;
      for (var c = 0; c < ch.length; c++) if (ch[c].matches(UNIT)) kids.push(ch[c]);
      if (kids.length) for (var k = 0; k < kids.length; k++) units.push(kids[k]);
      else units.push(sec);
    }
    for (var u = 0; u < units.length; u++) {
      var el = units[u];
      if (el.closest("nav,header,.guide-back-bar") || el.matches("figure.fig") || el.querySelector("figure.fig-pending")) continue;
      var r = el.getBoundingClientRect();
      if (r.height < 24 || r.top < H) continue;          // not rendered, tiny, or on / above the first screen: leave alone
      seen.push(el);
    }
    if (!seen.length) return;
    var lastY = window.pageYOffset, jumped = false;
    window.addEventListener("scroll", function () {      // one scroll event that moves most of a screen is a jump, not a scroll
      var y = window.pageYOffset;
      if (Math.abs(y - lastY) > window.innerHeight * 0.9) jumped = true;
      lastY = y;
    }, { passive: true });
    io = new IntersectionObserver(function (list) {
      var hi = -1;
      for (var i = 0; i < list.length; i++) {
        if (!list[i].isIntersecting) continue;
        var n = idxOf.get(list[i].target);
        if (n !== undefined && n > hi) hi = n;
      }
      if (hi >= 0) { revealUpTo(hi, !jumped); jumped = false; }   // reaching one reveals all before it, even ones you jumped over; after a jump (search hit, Ctrl-F, scrollIntoView) no fade, so it lands solid
    });
    for (var p = 0; p < seen.length; p++) {
      idxOf.set(seen[p], p); pending.push(seen[p]);
      seen[p].classList.add("rv-p");
      io.observe(seen[p]);
    }
    window.addEventListener("beforeprint", revealAll);
    window.addEventListener("hashchange", function () {
      try { revealThrough(document.getElementById(decodeURIComponent(location.hash.slice(1)))); } catch (e) {}
    });
    document.addEventListener("click", function (e) {    // a link to a place in this page: open the way before the browser scrolls
      var a = e.target && e.target.closest ? e.target.closest("a[href^='#']") : null;
      if (!a || a.getAttribute("href").length < 2) return;
      try { revealThrough(document.getElementById(decodeURIComponent(a.getAttribute("href").slice(1)))); } catch (x) {}
    }, true);
    if (location.hash.length > 1) { try { revealThrough(document.getElementById(decodeURIComponent(location.hash.slice(1)))); } catch (e) {} }
    // belt and braces: whatever the observer missed, anything on screen after load or resize is shown
    function sweep() {
      var h = window.innerHeight;
      for (var i = ptr; i < pending.length; i++) {
        var rr = pending[i].getBoundingClientRect();
        if (rr.top < h) { revealUpTo(i, true); }
      }
    }
    window.addEventListener("load", function () { setTimeout(sweep, 400); });
    var scT = 0; window.addEventListener("scroll", function () { clearTimeout(scT); scT = setTimeout(function () { jumped = false; sweep(); }, 250); }, { passive: true });   // once the scrolling settles
    var rsT = 0; window.addEventListener("resize", function () { clearTimeout(rsT); rsT = setTimeout(sweep, 300); });
  }

  /* ---------- 2. the Contents marker ---------- */
  function setupMarker() {
    var toc = document.querySelector("nav.toc");
    if (!toc) return;
    var links = toc.querySelectorAll("a[href^='#']"), items = [];
    for (var i = 0; i < links.length; i++) {
      var id = links[i].getAttribute("href").slice(1), t = null;
      try { t = document.getElementById(decodeURIComponent(id)); } catch (e) {}
      if (t) items.push({ a: links[i], t: t, top: 0 });
    }
    if (items.length < 2) return;
    var mark = document.createElement("span");
    mark.className = "toc-mark"; mark.setAttribute("aria-hidden", "true");
    toc.insertBefore(mark, toc.firstChild);
    var LINE = 140, cur = -2, sh = 0, raf = 0, ready = false;

    function measure() {
      var y = window.pageYOffset;
      for (var i = 0; i < items.length; i++) items[i].top = items[i].t.getBoundingClientRect().top + y;
      var sorted = true;                                  // the list should run in page order; if not, fall back to sorting
      for (i = 1; i < items.length; i++) if (items[i].top < items[i - 1].top - 1) { sorted = false; break; }
      if (!sorted) items.sort(function (a, b) { return a.top - b.top; });
      sh = document.documentElement.scrollHeight;
    }
    function show(n) {
      if (!toc.offsetParent) { cur = -2; return; }        // hidden (collapsed or a narrow screen): place it when it comes back
      if (n < 0) { mark.classList.remove("on"); cur = n; return; }
      var a = items[n].a;
      mark.style.height = a.offsetHeight + "px";
      mark.style.transform = "translateY(" + a.offsetTop + "px)";
      if (!ready || reduce) { mark.style.transition = "none"; } else mark.style.transition = "";
      mark.classList.add("on");
      if (!ready) { void mark.offsetWidth; ready = true; if (!reduce) mark.style.transition = ""; }
      var prev = toc.querySelector("a.toc-cur"); if (prev) prev.classList.remove("toc-cur");
      a.classList.add("toc-cur");
      cur = n;
      if (toc.scrollHeight > toc.clientHeight + 4 && !toc.matches(":hover")) {   // keep the entry in sight inside a long list
        var top = a.offsetTop, bot = top + a.offsetHeight;
        if (top < toc.scrollTop + 30 || bot > toc.scrollTop + toc.clientHeight - 30) {
          var want = Math.max(0, top - toc.clientHeight / 3);
          if (reduce || !toc.scrollTo) toc.scrollTop = want; else toc.scrollTo({ top: want, behavior: "smooth" });
        }
      }
    }
    function update() {
      raf = 0;
      if (document.documentElement.scrollHeight !== sh) measure();
      var y = window.pageYOffset + LINE, lo = 0, hi = items.length - 1, n = -1;
      while (lo <= hi) { var mid = (lo + hi) >> 1; if (items[mid].top <= y) { n = mid; lo = mid + 1; } else hi = mid - 1; }
      if (window.pageYOffset + window.innerHeight >= document.documentElement.scrollHeight - 4) n = items.length - 1;
      if (n !== cur) show(n);
    }
    function queue() { if (!raf) raf = requestAnimationFrame(update); }
    measure(); update();
    window.addEventListener("scroll", queue, { passive: true });
    window.addEventListener("resize", function () { measure(); cur = -2; queue(); });
    window.addEventListener("load", function () { measure(); cur = -2; queue(); });
    document.addEventListener("toggle", function () { measure(); queue(); }, true);   // an accordion opening moves everything below it
    new MutationObserver(function () { cur = -2; queue(); }).observe(document.body, { attributes: true, attributeFilter: ["class"] });   // Contents shown or hidden again
  }

  function go() { try { setupReveal(); } catch (e) { revealAll(); } try { setupMarker(); } catch (e) {} }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", go); else go();
})();

/* Pip, the study companion (pip/pip.js). On every page that loads theme.js, Semester 1 pages
   included (Jaxon, 2026-10-11); the few self-contained pages that omit theme.js carry their own
   small copy of this loader. Pip works out for himself what kind of page he is on, and on an older
   quiz page he cannot read he stays paused (pip/pip-window.js). Loaded after the page is up so it
   can never slow first paint.
   Only on pa-quizzes.com (and a local preview): GitHub Pages serves this same theme.js
   but does not get Pip until Jaxon decides otherwise. Same host list as pip-brain.js. */
(function () {
  if (!/^(pa-quizzes\.com|www\.pa-quizzes\.com|localhost|127\.0\.0\.1)$/.test(location.hostname)) return;
  if (window.top !== window) return;                     // never inside a frame
  var thisScript = document.querySelector('script[src$="theme.js"]');
  var base = thisScript ? thisScript.getAttribute("src").replace(/theme\.js$/, "") : "";
  function go() {
    if (!document.body || window.__pip) return;
    var s = document.createElement("script"); s.src = base + "pip/pip.js"; s.async = true;
    document.head.appendChild(s);
  }
  if (document.readyState === "complete") setTimeout(go, 0);
  else window.addEventListener("load", function () { setTimeout(go, 0); });
})();
