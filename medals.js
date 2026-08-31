/* Personal-best medals on the homepage quiz list.
 *
 * A quiz you have aced gets a small metal disc beside it, so the list doubles as
 * a record of what you have already beaten rather than only a menu of what is
 * left. Hovering gives the exact figure.
 *
 * WHERE "BEST" COMES FROM. Not from the qc: record -- that holds your LATEST
 * completion, so a good score is erased the moment you retake and slip. The best
 * is taken from progressLog, which keeps one entry per completion with its score,
 * and the current qc: value is folded in as well so a run older than the log's
 * 400-entry window is not lost.
 *
 * The discs are decorative, not surface accents, so they sit outside the
 * derived-accent rule in theme.css -- they are metals, and a solved hue would
 * make them look like status colours.
 */
(function () {
  "use strict";

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  function bestByPath() {
    var best = {};
    function put(path, pct) {
      if (!path || !isFinite(pct)) return;
      var k = decodeURIComponent(path).replace(/^\//, "");
      if (!(k in best) || pct > best[k]) best[k] = pct;
    }
    try {
      var log = JSON.parse(localStorage.getItem("progressLog") || "[]");
      log.forEach(function (e) {
        if (e && e.p && e.n > 0) put(e.p, e.s / e.n * 100);
      });
    } catch (e) {}
    for (var i = 0; i < localStorage.length; i++) {
      var key = localStorage.key(i);
      if (!key || key.indexOf("qc:") !== 0) continue;
      try {
        var rec = JSON.parse(localStorage.getItem(key));
        if (rec && rec.total > 0) put(key.slice(3), rec.score / rec.total * 100);
      } catch (e2) {}
    }
    return best;
  }

  function tier(pct) {
    if (pct >= 99.5) return "gold";
    if (pct >= 95) return "silver";
    if (pct >= 90) return "bronze";
    return null;
  }

  function decorate(root, best) {
    var n = 0;
    var links = (root.querySelectorAll ? root.querySelectorAll("a.quiz-link[href]") : []);
    Array.prototype.forEach.call(links, function (a) {
      if (a.querySelector(".medal")) return;
      var href = decodeURIComponent(a.getAttribute("href") || "").replace(/^\//, "");
      var pct = best[href];
      if (pct === undefined) return;
      var t = tier(pct);
      if (!t) return;
      var s = document.createElement("span");
      s.className = "medal medal-" + t;
      s.setAttribute("title", "Personal best " + Math.round(pct) + "%");
      s.setAttribute("aria-label", "personal best " + Math.round(pct) + " percent");
      a.appendChild(s);
      n++;
    });
    return n;
  }

  ready(function () {
    var best = bestByPath();
    if (!Object.keys(best).length) return;
    if (decorate(document, best)) document.documentElement.classList.add("has-medals");

    /* The homepage builds quiz links AFTER this runs -- search results are a
       fresh list, and switching class tabs or opening an exam section can add
       more. Decorating once left every one of those bare. Watch for them
       instead of guessing which events to hook. */
    if (!window.MutationObserver) return;
    var pending = null;
    new MutationObserver(function (muts) {
      var interesting = muts.some(function (m) {
        return Array.prototype.some.call(m.addedNodes, function (nd) {
          return nd.nodeType === 1 &&
            (nd.matches && nd.matches("a.quiz-link") ||
             nd.querySelector && nd.querySelector("a.quiz-link"));
        });
      });
      if (!interesting || pending) return;
      pending = requestAnimationFrame(function () {
        pending = null;
        if (decorate(document, best)) document.documentElement.classList.add("has-medals");
      });
    }).observe(document.body, { childList: true, subtree: true });
  });
})();
