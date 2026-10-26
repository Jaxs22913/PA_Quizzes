/* Superbrain: Pip asking Claude, through our own small server (superbrain/, a Cloudflare
   Worker). Loaded by pip/pip-window.js the first time a student asks for it.

   - Only signed-in students (the site's existing Google sign-in). The server checks the
     sign-in token itself and keeps a dollar ledger with daily and monthly caps.
   - Only with the student's OK, asked once: the question and the passages Pip found (in the
     guide, or at most two short ones from the student's own notes) are sent to Claude;
     nothing else about the student is. An ask with note passages is marked private, so the
     server never puts it in the answer cache it shares with the class.
   - The key never reaches the browser; the server holds it.
   - It works on phones too, because the thinking happens on the server.
   - Follow-ups (2026-10-15): a question that refers back ("what about treatment?") also sends the last two
     exchanges of this chat window (prior), which Pip keeps in memory only; they are never stored.
   - Streaming (2026-10-15): mode "guide" asks for the answer as Claude writes it (text/event-stream); anything the
     server says before Claude starts (limits, a cached answer, a bad request) is plain JSON, and both are read.
   - OSCE practice (2026-10-26): osce("status" | "start" | "turn" | "grade", body, onEvent) for the practice station
     page, and speech(body) for Google's natural voice (an audio Blob). A refusal carries the server's own message. */
(function () {
  "use strict";
  if (window.PipSuperbrain) return;
  var K_OK = "local:pip:claude:ok";
  var ME = (document.currentScript && document.currentScript.src) || "";
  var ROOT = ME.replace(/pip\/pip-superbrain\.js(\?.*)?$/, "");

  function endpoint() {
    if (window.PIP_SUPERBRAIN_URL) return window.PIP_SUPERBRAIN_URL;
    var h = location.hostname;
    if (h === "127.0.0.1" || h === "localhost") return "http://127.0.0.1:8787";      // wrangler dev
    // production: the Worker "pa-quizzes-helper" (superbrain/wrangler.jsonc, env.production)
    if (/(^|\.)pa-quizzes\.com$/.test(h)) return "https://helper.pa-quizzes.com";
    return null;
  }
  function user() {
    // local preview only: the preview server signs the owner in with a test key (never on a real host)
    if (window.__PIP_DEMO_USER && /^(127\.0\.0\.1|localhost)$/.test(location.hostname)) return window.__PIP_DEMO_USER;
    try {
      var u = window.firebase && firebase.auth && firebase.auth().currentUser;
      return u && !u.isAnonymous ? u : null;
    } catch (e) { return null; }
  }
  function state() {
    if (!endpoint()) return "off";
    if (!(window.firebase && firebase.auth) && !user()) return "no-sync";
    return user() ? "ready" : "signed-out";
  }
  function consented() { try { return localStorage.getItem(K_OK) === "1"; } catch (e) { return false; } }
  function setConsent(on) { try { if (on) localStorage.setItem(K_OK, "1"); else localStorage.removeItem(K_OK); } catch (e) {} }

  // can this browser read a reply as it arrives? (old ones get the whole answer at once, as before)
  function canStream() { return !!(window.ReadableStream && window.TextDecoder && window.Response && "body" in Response.prototype); }
  function call(path, body, onDelta, onEvent) {
    var u = user();
    if (!u) return Promise.resolve({ ok: false, code: "signed_out" });
    // give up after 30 s: Clawd waits for the answer, but not for one that is never coming
    var ctl = window.AbortController ? new AbortController() : null, timer = 0, timedOut = false;
    return u.getIdToken().then(function (tok) {
      if (ctl) timer = setTimeout(function () { timedOut = true; ctl.abort(); }, 30000);
      return fetch(endpoint() + path, {
        method: body ? "POST" : "GET",
        headers: { authorization: "Bearer " + tok, "content-type": "application/json" },
        body: body ? JSON.stringify(body) : undefined,
        signal: ctl ? ctl.signal : undefined
      });
    }).then(function (r) {
      clearTimeout(timer);
      if ((onDelta || onEvent) && r.ok && /^text\/event-stream/i.test(r.headers.get("content-type") || "") && r.body && r.body.getReader) return events(r, onDelta, ctl, onEvent);
      return r.json().catch(function () { return {}; }).then(function (j) {
        if (!r.ok || !j || typeof j.ok !== "boolean") {
          return { ok: false, code: (j && j.code) || "http_" + r.status, remainingToday: j && j.remainingToday,
                   message: j && typeof j.message === "string" ? j.message : undefined };
        }
        return j;
      });
    }).catch(function () { clearTimeout(timer); return { ok: false, code: timedOut ? "timeout" : "network" }; });
  }
  // a streamed answer: "delta" {text} pieces go to onDelta as they come, then "done" is the same reply as a plain
  // answer, or "error" {code}. Any other named event goes to onEvent (the OSCE grading's "progress"). Given up when
  // nothing arrives for 30 s.
  function events(r, onDelta, ctl, onEvent) {
    var reader = r.body.getReader(), dec = new TextDecoder(), buf = "", idle = 0, timedOut = false;
    function wait() { clearTimeout(idle); if (ctl) idle = setTimeout(function () { timedOut = true; ctl.abort(); }, 30000); }
    return new Promise(function (resolve) {
      var end = function (x) { clearTimeout(idle); try { reader.cancel(); } catch (e) {} resolve(x); };
      function one(chunk) {
        var ev = /^event: ?(.*)$/m.exec(chunk), data = /^data: ?(.*)$/m.exec(chunk), d = null;
        try { d = data ? JSON.parse(data[1]) : null; } catch (e) { return false; }
        if (!ev || !d) return false;
        if (ev[1] === "delta") { if (onDelta && typeof d.text === "string") try { onDelta(d.text); } catch (e) {} return false; }
        if (ev[1] === "done") { end(typeof d.ok === "boolean" ? d : { ok: false, code: "bad_reply" }); return true; }
        if (ev[1] === "error") { end({ ok: false, code: String(d.code || "stream_error"), remainingToday: d.remainingToday, message: typeof d.message === "string" ? d.message : undefined }); return true; }
        if (onEvent) try { onEvent(ev[1], d); } catch (e) {}
        return false;
      }
      function pump() {
        wait();
        reader.read().then(function (x) {
          if (x.done) return end({ ok: false, code: "network" });      // the stream ended without an answer
          buf += dec.decode(x.value, { stream: true }).replace(/\r\n?/g, "\n");
          for (var i = buf.indexOf("\n\n"); i >= 0; i = buf.indexOf("\n\n")) {
            var chunk = buf.slice(0, i); buf = buf.slice(i + 2);
            if (one(chunk)) return;
          }
          pump();
        }).catch(function () { end({ ok: false, code: timedOut ? "timeout" : "network" }); });
      }
      pump();
    });
  }
  function clip(s, n) {
    s = String(s == null ? "" : s);
    if (s.length > n) { s = s.slice(0, n); var c = s.charCodeAt(n - 1); if (c >= 0xD800 && c <= 0xDBFF) s = s.slice(0, n - 1); }   // no half emoji at the cut
    return s.replace(/[\uD800-\uDBFF](?![\uDC00-\uDFFF])|(^|[^\uD800-\uDBFF])[\uDC00-\uDFFF]/g, function (m, pre) { return (pre || "") + "\uFFFD"; });
  }
  function ask(q) {
    // the server enforces the same limits; trimming here keeps a long passage from failing the request
    var many = q.mode === "answer" || q.mode === "guide";
    var ps = (q.passages || []).slice(0, many ? 6 : 4);   // "answer"/"guide": the search's candidates, for Claude to choose from
    var body = {
      question: clip(q.question, 500),
      exam: { title: clip(q.exam && q.exam.title, 120), folder: clip(q.exam && q.exam.folder, 120) },
      passages: ps.map(function (p) { return { title: clip(p.title, 200), text: clip(p.text, 1200) }; }),
      mode: q.mode
    };
    // "guide": the helper reads that exam's whole study guide (public, from this site); hints are the guide lines
    // Pip's search ranked highest (they pick the volume of a big guide)
    if (q.mode === "guide") {
      body.exam.slug = String(q.exam && q.exam.slug || "").slice(0, 100);
      var hs = (q.hints || []).filter(function (n) { return n === (n | 0) && n >= 0 && n < 100000; }).slice(0, 12);
      if (hs.length) body.hints = hs;
    }
    // a follow-up: the last two exchanges of this chat (the server takes at most 2, 500 + 1,200 characters each)
    var pr = (q.prior || []).filter(function (t) { return t && String(t.q || "").trim() && String(t.a || "").trim(); }).slice(-2);
    if (pr.length) body.prior = pr.map(function (t) { return { q: clip(String(t.q).trim(), 500), a: clip(String(t.a).trim(), 1200) }; });
    // Teach Pip: when any passage comes from the student's own notes the ask is private, and
    // the server keeps it out of the answer cache it shares with the class
    if (q.private === true || ps.some(function (p) { return p && p.note; })) body.private = true;
    var onDelta = typeof q.onDelta === "function" && canStream() ? q.onDelta : null;
    if (onDelta) body.stream = true;
    return call("/v1/ask", body, onDelta);
  }
  function signIn() {
    if (window.cloudSignIn) return Promise.resolve(window.cloudSignIn());
    // a page without theme.js has no cloud-sync.js: the same Google popup, through the auth ready() brought in
    try { return firebase.auth().signInWithPopup(new firebase.auth.GoogleAuthProvider()).catch(function () {}); }
    catch (e) { return Promise.resolve(); }
  }

  /* Pages that skip theme.js (the OSCE run-sheets, relax.html, the Pharmacology game plan ...) never load
     Firebase, so Pip saw "no-sync" there and quietly kept Claude out (Jaxon, 2026-10-20: "its just not
     letting me ask claude stuff"). There, ready() brings in ONLY the sign-in part: Firebase keeps the
     session in this browser, so a student signed in anywhere on the site is signed in here too. No
     Firestore, no cloud sync. Pages with theme.js are left to their own chain (cloud-sync.js initialises
     the app, and a second initializeApp would break it). Resolves once the first auth answer is in; never
     rejects (offline or blocked: state() stays "no-sync", as before). */
  var FB = "https://www.gstatic.com/firebasejs/10.14.1/";   // the version theme.js loads
  var readyP = null;
  function addScript(src) {
    return new Promise(function (res, rej) {
      var s = document.createElement("script"); s.src = src; s.onload = res; s.onerror = rej; document.head.appendChild(s);
    });
  }
  function firstAuth() {                                // the stored session restored, or nobody
    return new Promise(function (res) {
      var done = false, off = null, t = setTimeout(fin, 5000);
      function fin() { if (done) return; done = true; clearTimeout(t); try { if (off) off(); } catch (e) {} res(); }
      try { off = firebase.auth().onAuthStateChanged(fin); } catch (e) { fin(); }
    });
  }
  function ready() {
    if (readyP) return readyP;
    if (!endpoint() || window.__PIP_DEMO_USER || document.querySelector('script[src$="theme.js"]')) return (readyP = Promise.resolve());
    readyP = (window.firebase && firebase.auth && firebase.apps && firebase.apps.length ? Promise.resolve()
      : addScript(FB + "firebase-app-compat.js").then(function () {
          return Promise.all([addScript(FB + "firebase-auth-compat.js"), window.FIREBASE_CONFIG ? null : addScript(ROOT + "firebase-config.js")]);
        }).then(function () {
          if (!firebase.apps.length) firebase.initializeApp(window.FIREBASE_CONFIG);
          try { firebase.auth().setPersistence(firebase.auth.Auth.Persistence.LOCAL).catch(function () {}); } catch (e) {}
        })
    ).then(firstAuth).catch(function () {});
    return readyP;
  }

  var statusP = null;                                  // one status check per page (owner flag, remaining today)
  function status() { if (!statusP) statusP = call("/v1/status").then(function (r) { if (!r || r.ok === false && r.code === "network") statusP = null; return r; }); return statusP; }
  // invite-only: a classmate enters the class code once and the server adds their account
  function join(code) { return call("/v1/join", { code: clip(String(code || "").trim(), 64) }).then(function (r) { statusP = null; return r; }); }
  // OSCE practice: the station routes only. The grading is always a stream (progress events, then done or error).
  function osce(what, body, onEvent) {
    if (!/^(status|start|turn|grade)$/.test(what)) return Promise.resolve({ ok: false, code: "bad_route" });
    if (what === "grade" && !canStream()) return Promise.resolve({ ok: false, code: "old_browser", message: "This browser can't receive the grading. Try an up-to-date Chrome, Edge or Safari." });
    return call("/v1/osce/" + what, what === "status" ? undefined : body, null, what === "grade" ? (onEvent || function () {}) : null);
  }
  // Google's natural voice for one line: {ok: true, blob} or {ok: false, code} (the page falls back to the free voices)
  function speech(body) {
    var u = user();
    if (!u || !endpoint()) return Promise.resolve({ ok: false, code: "signed_out" });
    var ctl = window.AbortController ? new AbortController() : null, timer = 0;
    return u.getIdToken().then(function (tok) {
      if (ctl) timer = setTimeout(function () { ctl.abort(); }, 15000);
      return fetch(endpoint() + "/v1/osce/tts", {
        method: "POST",
        headers: { authorization: "Bearer " + tok, "content-type": "application/json" },
        body: JSON.stringify(body),
        signal: ctl ? ctl.signal : undefined
      });
    }).then(function (r) {
      if (r.ok && /^audio\//i.test(r.headers.get("content-type") || "")) return r.blob().then(function (b) { clearTimeout(timer); return { ok: true, blob: b }; });
      clearTimeout(timer);
      return r.json().catch(function () { return {}; }).then(function (j) { return { ok: false, code: (j && j.code) || "http_" + r.status }; });
    }).catch(function () { clearTimeout(timer); return { ok: false, code: "network" }; });
  }
  window.PipSuperbrain = { state: state, consented: consented, setConsent: setConsent, ask: ask, signIn: signIn,
                           status: status, join: join, endpoint: endpoint, ready: ready, osce: osce, speech: speech };
})();
