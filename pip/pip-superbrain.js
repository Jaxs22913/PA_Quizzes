/* Superbrain: Pip asking Claude, through our own small server (superbrain/, a Cloudflare
   Worker). Loaded by pip/pip-window.js the first time a student asks for it.

   - Only signed-in students (the site's existing Google sign-in). The server checks the
     sign-in token itself and keeps a dollar ledger with daily and monthly caps.
   - Only with the student's OK, asked once: the question and the passages Pip found (in the
     guide, or at most two short ones from the student's own notes) are sent to Claude;
     nothing else about the student is. An ask with note passages is marked private, so the
     server never puts it in the answer cache it shares with the class.
   - The key never reaches the browser; the server holds it.
   - It works on phones too, because the thinking happens on the server. */
(function () {
  "use strict";
  if (window.PipSuperbrain) return;
  var K_OK = "local:pip:claude:ok";

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

  function call(path, body) {
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
      return r.json().catch(function () { return {}; }).then(function (j) {
        if (!r.ok || !j || typeof j.ok !== "boolean") return { ok: false, code: (j && j.code) || "http_" + r.status, remainingToday: j && j.remainingToday };
        return j;
      });
    }).catch(function () { clearTimeout(timer); return { ok: false, code: timedOut ? "timeout" : "network" }; });
  }
  function clip(s, n) {
    s = String(s == null ? "" : s);
    if (s.length > n) { s = s.slice(0, n); var c = s.charCodeAt(n - 1); if (c >= 0xD800 && c <= 0xDBFF) s = s.slice(0, n - 1); }   // no half emoji at the cut
    return s.replace(/[\uD800-\uDBFF](?![\uDC00-\uDFFF])|(^|[^\uD800-\uDBFF])[\uDC00-\uDFFF]/g, function (m, pre) { return (pre || "") + "\uFFFD"; });
  }
  function ask(q) {
    // the server enforces the same limits; trimming here keeps a long passage from failing the request
    var ps = (q.passages || []).slice(0, 4);
    var body = {
      question: clip(q.question, 500),
      exam: { title: clip(q.exam && q.exam.title, 120), folder: clip(q.exam && q.exam.folder, 120) },
      passages: ps.map(function (p) { return { title: clip(p.title, 200), text: clip(p.text, 1200) }; }),
      mode: q.mode
    };
    // Teach Pip: when any passage comes from the student's own notes the ask is private, and
    // the server keeps it out of the answer cache it shares with the class
    if (q.private === true || ps.some(function (p) { return p && p.note; })) body.private = true;
    return call("/v1/ask", body);
  }
  function signIn() { return window.cloudSignIn ? Promise.resolve(window.cloudSignIn()) : Promise.resolve(); }

  var statusP = null;                                  // one status check per page (owner flag, remaining today)
  function status() { if (!statusP) statusP = call("/v1/status").then(function (r) { if (!r || r.ok === false && r.code === "network") statusP = null; return r; }); return statusP; }
  // invite-only: a classmate enters the class code once and the server adds their account
  function join(code) { return call("/v1/join", { code: clip(String(code || "").trim(), 64) }).then(function (r) { statusP = null; return r; }); }
  window.PipSuperbrain = { state: state, consented: consented, setConsent: setConsent, ask: ask, signIn: signIn,
                           status: status, join: join, endpoint: endpoint };
})();
