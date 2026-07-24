// Class-wide cumulative "questions answered" counter. A single shared Firestore
// doc -- stats/global.questionsCompleted -- is incremented whenever anyone
// finishes a quiz, and the homepage subscribes to it live with an animated
// count-up. Built on the same Firebase project as cloud-sync.js / presence.js,
// and loaded by theme.js's Firebase bootstrap chain on every page. It only does
// work where relevant: it increments on a quiz page (by hooking the engines'
// shared markCompleted() finish signal) and displays on any page that has a
// #class-counter-value element (the homepage).
//
// Like presence.js, scoring here is client-trusted -- a determined student
// could inflate the count, which is fine for a casual class engagement metric,
// not a leaderboard. Needs a Firestore rule allowing this doc to be read and
// incremented (see the group_study/presence rules pattern):
//   match /stats/global { allow read: if true; allow write: if request.auth != null; }
// Until such a rule is published, writes/reads fail silently (counter stays 0).
(function () {
  "use strict";

  var db = null;
  var ready = false;
  var pending = 0; // increments queued before Firebase is ready

  function statRef() { return db.collection("stats").doc("global"); }

  function flush() {
    if (!ready || pending <= 0) return;
    var n = pending;
    pending = 0;
    statRef().set({
      questionsCompleted: firebase.firestore.FieldValue.increment(n),
      updatedAt: firebase.firestore.FieldValue.serverTimestamp()
    }, { merge: true }).catch(function () { /* permission-denied / offline -- drop silently */ });
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
