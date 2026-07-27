// Class-wide cumulative "questions answered" counter. A single shared Firestore
// doc -- stats/global.questionsCompleted -- is incremented whenever anyone
// finishes a quiz, and the homepage subscribes to it live with an animated
// count-up. Built on the same Firebase project as cloud-sync.js / presence.js,
// and loaded by theme.js's Firebase bootstrap chain on every page. It only does
// work where relevant: it increments on a quiz page (by hooking the engines'
// shared markCompleted() finish signal) and displays on any page that has a
// #class-counter-value element (the homepage).
//
// Scoring here is client-trusted. The published rule on this doc is fully
// open -- verified 2026-07-27 by a successful UNAUTHENTICATED write, so it is
// `allow read, write: if true`, not the auth-gated form an earlier version of
// this comment claimed. That is deliberate: most quiz-page visitors are not
// signed in (Google sign-in is optional), so an auth gate would drop the
// majority of real increments. The tradeoff is that anyone can write any
// value with no credentials, which is acceptable for a casual engagement
// metric and would not be for anything load-bearing.
//   match /stats/global {
//     allow read: if true;
//     allow write: if request.resource.data.questionsCompleted is number;
//     allow delete: if false;
//   }
// It is shape-guarded rather than wide open: unauthenticated writes ARE
// allowed, but only ones that set questionsCompleted to a number, so the doc
// cannot be used as arbitrary storage. Anyone can still set the counter to any
// value without signing in.
// Until such a rule is published, writes/reads fail silently (counter stays 0).
//
// EVENT LOG (added 2026-07-27). The running total is a single integer with no
// history, so when it jumped ~18k in a day there was no way to attribute the
// delta after the fact -- only to confirm the increment path was sound. Every
// increment now also appends one immutable row to stats_events, which makes a
// future jump traceable to when it happened, which quiz produced it, and
// whether it came from one browser session or many. Needs its own rule, and
// it must be append-only -- a log anything can rewrite is not evidence.
// `create: if true` deliberately matches the counter's own open rule: gating
// the log on auth while the total stays open would log only the signed-in
// minority, so the log and the total would disagree by design and the
// reconciliation check below would be worthless. The bounds on `n` stop the
// log being poisoned with absurd values even though it is open:
// The rule lives in firestore.rules in this repo (match /stats_events), which
// is the source of truth -- but that file is NOT auto-deployed; it has to be
// published in the Firebase console or via the Firebase CLI before the log
// records anything.
// The session id is a random per-tab value; it is NOT tied to any account and
// identifies nobody. Its only job is to show that N completions shared one
// origin, which is exactly the shape automated or inflated traffic has.
(function () {
  "use strict";

  var db = null;
  var ready = false;
  var pending = 0; // increments queued before Firebase is ready

  function statRef() { return db.collection("stats").doc("global"); }

  // Random per-tab id so a burst of completions from a single session is
  // visible as such in the log. Regenerated every tab; not linked to any user.
  var sessionId = (function () {
    try {
      var k = "__statsSession";
      var v = sessionStorage.getItem(k);
      if (!v) {
        v = Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4);
        sessionStorage.setItem(k, v);
      }
      return v;
    } catch (e) {
      return "nostore";
    }
  })();

  // One immutable row per increment. Written alongside the running total, not
  // derived from it, so the two can be reconciled: summing the log's n values
  // from a known baseline should reproduce questionsCompleted. A divergence is
  // itself the signal that something wrote the total directly.
  function logEvent(n, kind) {
    if (!db) return;
    try {
      db.collection("stats_events").add({
        n: n,
        kind: kind || "quiz-complete",
        // pathname only -- which quiz, never anything about who.
        path: (location.pathname || "").slice(-120),
        session: sessionId,
        at: firebase.firestore.FieldValue.serverTimestamp()
      }).catch(function () { /* rule not published yet -- total still works */ });
    } catch (e) { /* never let logging break the counter */ }
  }

  function flush() {
    if (!ready || pending <= 0) return;
    var n = pending;
    pending = 0;
    statRef().set({
      questionsCompleted: firebase.firestore.FieldValue.increment(n),
      updatedAt: firebase.firestore.FieldValue.serverTimestamp()
    }, { merge: true }).then(function () {
      logEvent(n);
    }).catch(function () { /* permission-denied / offline -- drop silently */ });
  }

  window.ClassStats = {
    // Record n newly-completed questions toward the class total.
    record: function (n) {
      n = Math.max(0, Math.floor(+n || 0));
      if (!n) return;
      pending += n;
      flush();
    }
  };

  // Hook the quiz engines: markCompleted(score, total, timeMs) is their shared
  // finish signal (a top-level function, so it's on window). Wrapping it here --
  // this file loads after the quiz page's own inline script has defined it --
  // means finishing a quiz adds its question count to the class total, with no
  // per-quiz edits. A quiz completed in the ~2s before this file loads is the
  // only miss, which is negligible since a quiz takes far longer than that.
  if (typeof window.markCompleted === "function") {
    var orig = window.markCompleted;
    window.markCompleted = function (score, total, timeMs) {
      try { window.ClassStats.record(total); } catch (e) {}
      return orig.apply(this, arguments);
    };
  }

  function animateTo(el, target) {
    var start = parseInt(el.getAttribute("data-val") || "0", 10) || 0;
    if (target === start) { el.textContent = target.toLocaleString(); el.setAttribute("data-val", target); return; }
    var t0 = performance.now(), dur = 900;
    (function step(now) {
      var p = Math.min(1, (now - t0) / dur);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(start + (target - start) * eased).toLocaleString();
      if (p < 1) requestAnimationFrame(step);
      else { el.textContent = target.toLocaleString(); el.setAttribute("data-val", target); }
    })(t0);
  }

  function boot() {
    db = firebase.firestore();
    ready = true;
    flush();

    var el = document.getElementById("class-counter-value");
    if (!el) return; // this page doesn't display the counter
    statRef().onSnapshot(function (snap) {
      var v = (snap.exists && snap.data() && snap.data().questionsCompleted) || 0;
      var wrap = document.getElementById("class-counter");
      if (wrap) wrap.classList.add("ready");
      animateTo(el, v);
    }, function () { /* offline / permission-denied -- leave the placeholder */ });
  }

  if (window.__firebaseReady) boot();
  else window.addEventListener("firebaseReady", boot, { once: true });
})();
