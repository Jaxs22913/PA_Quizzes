/* Pip's window: what opens when a student taps Pip. Loaded by pip/pip.js on the first tap.

   What Pip can do here (no AI model and no API key needed; every answer comes from
   content that is already published and checked):
   - Say what matters on this page: the next exam and how much of it is done, what to
     do after a quiz, where to look in a guide.
   - Answer a typed question by FINDING it in the student's study guides and cram sheets
     and quoting the passage word for word, with a link to it. Pip never writes medical
     content of his own, so he cannot get a fact wrong.
   - Run practice sets and rescue drills from the vetted question bank, right in the
     window, with the same per-option explanations the quizzes show. These answers never
     touch the class stats (Jaxon, 2026-10-08) and live only on this device.
   - Teach Pip: the student adds their own notes (Notes button; PDF, Word, .txt, .md) for
     the exam Pip is on. They stay on this device (pip/pip-notes.js, IndexedDB), and a
     search shows the guide's passages first, then up to two "From your notes" passages.
     Pip never writes quiz questions from notes.

   Rules it keeps:
   - It never helps with a quiz question the student has not answered yet. A pasted
     question is turned away, and no "about this question" help is offered until the
     answer is locked in.
   - Key presses inside the window never reach the quiz underneath. The quiz's keyboard
     shortcuts listen on the whole page, so typing "a" would otherwise answer it.
   - Pip reacts only to what the student does here: opening the window, answering a
     drill question, finishing a set.
   - On a laptop or desktop that can run his brain (pip/pip-brain.js) and has none yet, every
     open of the window starts with the brain card, and typed questions wait for the student's
     pick ("the brain card, first thing on every open", below). */
(function () {
  "use strict";
  if (window.PipWindow) return;
  var P = window.__pip;
  if (!P) return;
  var ROOT = P.ROOT, DATA = ROOT + "pip/data/";
  var K_HIST = "local:pip:hist";

  // ------------------------------------------------------------------ small helpers
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    return e;
  }
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  // anonymous usage counts (metrics.js; Pip's family is registered in pip.js): a +1 and nothing else
  function count(field) { try { if (window.PAMetrics) window.PAMetrics.add(field); } catch (e) {} }
  function jget(k, d) { try { var v = JSON.parse(get(k)); return v == null ? d : v; } catch (e) { return d; } }
  var cache = {};
  function getJSON(path) {
    // the small index is always re-checked; the big files are fetched under the index's build
    // stamp, so a rebuild of pip/data reaches students instead of sitting behind a stale cache
    var url = path === "index.json" ? DATA + path : DATA + path + "?v=" + encodeURIComponent((IX && IX.built) || "");
    if (!cache[path]) cache[path] = fetch(url, path === "index.json" ? { cache: "no-cache" } : undefined)
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); });
    return cache[path];
  }
  function loadScript(src) {
    return new Promise(function (res) {
      var s = document.createElement("script"); s.src = src; s.onload = res; s.onerror = res;
      document.head.appendChild(s);
    });
  }
  function shuffle(a) { for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function ymd(d) { return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
  function daysUntil(s) {
    var p = s.split("-"), then = new Date(+p[0], +p[1] - 1, +p[2]), now = new Date();
    now = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    return Math.round((then - now) / 86400000);
  }
  function niceDate(s) {
    var p = s.split("-");
    return new Date(+p[0], +p[1] - 1, +p[2]).toLocaleDateString(undefined, { weekday: "short", month: "short", day: "numeric" });
  }
  function pageURL(folder, file, hash) {     // file may climb out of the folder ("../Other Exam/guide.html")
    var base = ROOT + folder.split("/").map(encodeURIComponent).join("/") + "/";
    var rel = String(file).split("/").map(function (s) { return s === ".." || s === "." ? s : encodeURIComponent(s); }).join("/");
    return new URL(rel + (hash ? "#" + encodeURIComponent(hash) : ""), base).href;
  }
  function decodedPath(p) { try { return decodeURIComponent(p); } catch (e) { return p; } }
  var LTR = "ABCDEFG";

  // ------------------------------------------------------------------ words (search + guard)
  var STOP = {};
  ("a an the and or of to in on for with by at from is are was were be been being as that this these those it its into " +
   "than then which who whom whose what when where why how not no do does did can could should would may might will shall " +
   "about over under after before between during per via vs i me my you your we our tell show explain mean means meaning " +
   "find look up guide difference differences different compare comparison contrast versus explain describe define " +
   "definition useful purpose role important " +
   // chat filler a student types around the actual topic ("whats", "explain it simply", "how does X work")
   "whats hows whys wheres whos thats im dont cant please pls plz just really actually basically simply simple quick " +
   "quickly again like kind thing things stuff concept idea topic understand know learn study help give talk overview " +
   "summary summarize work works working happen happens eli5 confused lost tho though u ur ya yeah ok okay so fast pros cons get gets got getting go goes going many much " +
   // how a long question is wrapped ("ok so in lecture she said ... and i keep mixing it up, can u walk me thru")
   "lecture lectures lecturer said says saying told prof profs professor teacher slide slides recording today yesterday " +
   "gotta wanna gonna kinda sorta idk lol hmm um uh guess think thought feel sure bit little question questions asking ask " +
   "answer matter whole lot lots way ways something anything everything someone somebody keep keeps kept mixing mix mixed " +
   "remember forget real deal thru through dr she he they them their his her we our us made make makes making " +
   "but totally literally seriously honestly super pretty even still ever anyway also too very").split(" ").forEach(function (w) { STOP[w] = 1; });
  function norm(s) { return String(s || "").toLowerCase().normalize("NFKD").replace(/[̀-ͯ]/g, ""); }
  function stem(w) {
    if (w.length > 4 && /ies$/.test(w)) return w.slice(0, -3) + "y";
    // "masses" -> "mass", "branches" -> "branch", but "causes" -> "cause", "diseases" -> "disease", "headaches" -> "headache"
    if (w.length > 4 && /ses$/.test(w)) return /sses$|uses$/.test(w) ? w.slice(0, -2) : w.slice(0, -1);
    if (w.length > 4 && /(xes|ches|shes)$/.test(w) && !/aches$/.test(w)) return w.slice(0, -2);
    if (w.length > 4 && /(zes|aches)$/.test(w)) return w.slice(0, -1);
    if (w.length > 3 && /s$/.test(w) && !/(ss|us|is)$/.test(w)) w = w.slice(0, -1);
    // Latin plurals: "streptococci" and "streptococcus", "thrombi" and "thrombus" are one word
    if (/(cocc|bacill|fung|thromb|embol|bronch|alveol|nucle)i$/.test(w)) return w.slice(0, -1) + "us";
    // one form for a word and its -ion / -ed / -ing forms: "rejected" and "rejection" -> "reject",
    // "elevated" and "elevation" -> "elevat", "caused" and "causing" -> "cause"
    if (w.length > 6 && /ion$/.test(w)) return w.slice(0, -3);
    if (w.length > 5 && /ated$/.test(w)) return w.slice(0, -2);
    if (w.length > 5 && /[svzcgu]ed$/.test(w) && !/ssed$/.test(w)) return w.slice(0, -1);
    if (w.length > 5 && /ed$/.test(w) && !/eed$/.test(w)) return w.slice(0, -2);
    if (w.length > 6 && /ating$/.test(w)) return w.slice(0, -3);
    if (w.length > 6 && /[svzcgu]ing$/.test(w) && !/ssing$/.test(w)) return w.slice(0, -3) + "e";
    if (w.length > 6 && /ing$/.test(w)) return w.slice(0, -3);
    return w;
  }
  // "P wave", "T-waves", "J point": one word each ("pwave"), plus the plain word, so a question about the P wave is not
  // about every wave (Jaxon, 2026-10-15: "What's the difference between a T and P wave?" got an infarct card).
  // tools/build_pip_data.py makes the same words for pip/data/words.json
  function letterTerms(n) { return n.replace(/\b([pqrstuj])[\s-]+(waves?|points?)\b/g, "$1$2 $2"); }
  function toks(s) {
    var out = [];
    letterTerms(norm(s)).split(/[^a-z0-9]+/).forEach(function (w) { if (w.length >= 2 && !STOP[w]) { var t = stem(w); if (!STOP[t]) out.push(t); } });
    return out;
  }
  // the shorthand students type that the guides never use (real abbreviations such as NNT or PVC are
  // expanded from the guides' own "(ABBR)" list in expandFor)
  var CASUAL = [[/\bc\.? ?diff\b/g, "clostridioides difficile"], [/\bstaph\b/g, "staph staphylococcus"], [/\bstrep\b/g, "strep streptococcus"],
    [/\bsens\b/g, "sensitivity"], [/\bspec\b/g, "specificity"], [/\bcalc\b/g, "calculate"], [/\babx\b/g, "antibiotics"],
    [/\btx\b/g, "treatment"], [/\bddx\b/g, "differential diagnosis"], [/\bdx\b/g, "diagnosis"], [/\bsx\b/g, "symptoms"],
    [/\bhx\b/g, "history"], [/\ba ?fib\b/g, "atrial fibrillation"], [/\ba ?flutter\b/g, "atrial flutter"],
    [/\bv ?fib\b/g, "ventricular fibrillation"], [/\bv ?tach\b/g, "ventricular tachycardia"], [/\bekg\b/g, "electrocardiogram"],
    [/\bbrady\b/g, "bradycardia"], [/\btachy?\b/g, "tachycardia"], [/\bdiff\b/g, "difference"], [/\bpvcs?\b/g, "premature ventricular complex"],
    [/\bpacs?\b/g, "premature atrial complex"], [/\bpjcs?\b/g, "premature junctional complex"], [/\blafb\b/g, "left anterior fascicular block"],
    [/\blpfb\b/g, "left posterior fascicular block"], [/\bavnrt\b/g, "atrioventricular nodal reentrant tachycardia"],
    [/\b1st\b/g, "first"], [/\b2nd\b/g, "second"], [/\b3rd\b/g, "third"], [/\b4th\b/g, "fourth"]];
  var SYN = { strep: "streptococcus", staph: "staphylococcus" };
  // abbreviations that are also everyday words count only when typed in capitals ("why does AS cause angina")
  var CAPS = { AS: "aortic stenosis", AR: "aortic regurgitation", MS: "mitral stenosis", MR: "mitral regurgitation", US: "ultrasound", ID: "infectious disease" };
  function casual(q) {
    var caps = []; String(q).replace(/\b(AS|AR|MS|MR|US|ID)\b/g, function (m) { caps.push(CAPS[m]); return m; });
    var s = norm(q); CASUAL.forEach(function (r) { s = s.replace(r[0], r[1]); });
    return caps.length ? s + " " + caps.join(" ") : s;
  }
  function uniq(a) { var s = {}, o = []; a.forEach(function (x) { if (!s[x]) { s[x] = 1; o.push(x); } }); return o; }
  function escRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }

  // BM25 over a list of texts; built once per data file and kept on it
  function makeIndex(texts, extras) {
    var N = texts.length, df = Object.create(null), docs = new Array(N), total = 0;
    for (var i = 0; i < N; i++) {
      var t = toks(texts[i]), tf = Object.create(null);
      t.forEach(function (w) { tf[w] = (tf[w] || 0) + 1; });
      if (extras) toks(extras[i]).forEach(function (w) { tf[w] = (tf[w] || 0) + 0.6; });
      docs[i] = { tf: tf, len: t.length || 1 };
      total += t.length;
      for (var w in tf) df[w] = (df[w] || 0) + 1;
    }
    return { N: N, df: df, docs: docs, avg: total / (N || 1) };
  }
  // "PCR" -> "polymerase chain reaction" when this text never uses the abbreviation itself
  // (the guides spell abbreviations out); the site-wide list comes from tools/build_pip_data.py
  function expandFor(query, ix) {
    var ab = abFor(ix);
    return String(query).replace(/\b[A-Za-z][A-Za-z0-9]{1,7}\b/g, function (w) {     // whole words only ("ics" inside "antibiotics" is not intercostal space)
      var k = w.toLowerCase(), exp = ab[k];
      return exp && !ix.df[stem(k)] ? exp : w;
    });
  }
  // a word the index has never seen becomes the closest one it knows: a cut-off word ("contraindic")
  // its commonest completion; a misspelling ("wenkebach", "psuedoaneurysm", "valsava") the closest word
  // with the same first letter, at most one edit away (two for words of 9+ letters; a swap of
  // neighbours counts as one). Words under 6 letters are left alone, so ordinary words are not "fixed".
  function near(a, b, max) {
    if (Math.abs(a.length - b.length) > max) return false;
    var prev2 = null, prev = [], cur, i, j;
    for (j = 0; j <= b.length; j++) prev[j] = j;
    for (i = 1; i <= a.length; i++) {
      cur = [i]; var low = i;
      for (j = 1; j <= b.length; j++) {
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
        if (prev2 && i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) cur[j] = Math.min(cur[j], prev2[j - 2] + 1);
        if (cur[j] < low) low = cur[j];
      }
      if (low > max) return false;
      prev2 = prev; prev = cur;
    }
    return prev[b.length] <= max;
  }
  function spell(q, ix) {
    if (!ix._vocab) ix._vocab = Object.keys(ix.df);
    // a word the guide already knows goes back AS TYPED, not as its stem: callers tokenize the
    // result again, and stemming a stem twice broke words such as "hypertension" (hypertens ->
    // hyperten, which no passage holds), so Pip said they were not in the guide
    var words = [];
    letterTerms(norm(q)).split(/[^a-z0-9]+/).forEach(function (raw) { if (raw.length >= 2 && !STOP[raw]) { var t = stem(raw); if (!STOP[t]) words.push([raw, t]); } });
    return words.map(function (p) {
      var w = p[1];
      if (w.length < 5 || ix.df[w] || /\d/.test(w) || /^[pqrstuj](?:wave|point)$/.test(w)) return p[0];
      var best = null, max = w.length >= 9 ? 2 : 1;
      ix._vocab.forEach(function (v) { if (v.length > w.length && v.indexOf(w) === 0 && (!best || ix.df[v] > ix.df[best])) best = v; });
      if (best || w.length < 6) return best || w;
      ix._vocab.forEach(function (v) { if (v.length >= 5 && w.length - v.length <= 3 && w.indexOf(v) === 0 && (!best || v.length > best.length)) best = v; });
      if (best) return best;
      ix._vocab.forEach(function (v) { if (v[0] === w[0] && (!best || ix.df[v] > ix.df[best]) && near(w, v, max)) best = v; });
      return best || w;
    }).join(" ");
  }
  // when half or more of a question's specific words never appear in this exam's guide ("what is
  // wenckebach on an ekg" asked of a vascular exam), it is about something else: say so rather than
  // show passages that share only its common words
  function offGuide(q, gix) {
    // only short questions (a long one carries words of its own); "typeii" is a card-search word only
    var core = uniq(toks(q)).filter(function (w) { return !GENERIC[w] && w.length >= 4 && !/^(type|class|grade|stage|phase|degree|group|schedule|mobitz)(i{1,3}|iv|v)$/.test(w); });
    if (!core.length || core.length > 4 || !gix) return false;
    return core.filter(function (w) { return !gix.df[w]; }).length * 2 >= core.length;
  }
  // this exam's own abbreviations first (PTA is peritonsillar abscess in the ear-nose-throat guide but
  // percutaneous transluminal angioplasty in the vascular one), then the site-wide list
  function abFor(ix) {
    var site = (IX && IX.ab) || {}, own = ix && ix.ab2;
    if (!own) return site;
    if (!ix._ab) { ix._ab = Object.create(null); for (var k in site) ix._ab[k] = site[k]; for (var j in own) ix._ab[j] = own[j]; }
    return ix._ab;
  }
  function rank(ix, texts, query, k, share) {
    var qt = uniq(toks(query)), nq = norm(query).trim(), out = [];
    if (!qt.length) return out;
    // a short form and its long form ("strep streptococcus", from casual()) count as one word
    var pairs = [];
    for (var a in SYN) if (qt.indexOf(a) >= 0 && qt.indexOf(SYN[a]) >= 0) pairs.push([a, SYN[a]]);
    var nw = qt.length - pairs.length;
    // a long question names its topic among many other words: it needs fewer of them to match
    var need = nw <= 2 ? nw : Math.ceil(nw * (share || (nw >= 7 ? 0.4 : 0.6)));
    for (var i = 0; i < ix.N; i++) {
      var d = ix.docs[i], s = 0, hit = 0;
      for (var j = 0; j < qt.length; j++) {
        var tf = d.tf[qt[j]]; if (!tf) continue;
        var df = ix.df[qt[j]], idf = Math.log(1 + (ix.N - df + 0.5) / (df + 0.5));
        s += idf * (tf * 2.2) / (tf + 1.2 * (0.25 + 0.75 * d.len / ix.avg)); hit++;
      }
      pairs.forEach(function (p) { if (d.tf[p[0]] && d.tf[p[1]]) hit--; });
      if (hit < need) continue;
      if (nq.length > 5 && norm(texts[i]).indexOf(nq) >= 0) s += 4;
      out.push([s * (0.6 + 0.4 * hit / qt.length), i]);
    }
    out.sort(function (a, b) { return b[0] - a[0]; });
    return out.slice(0, k || 5);
  }

  // ------------------------------------------------------------------ where are we, what is next
  var where = { folder: null, file: decodedPath(location.pathname).split("/").pop() };
  function index() { return getJSON("index.json").then(function (ix) { IX = ix; return ix; }); }
  function folderOf(ix) {
    var parts = decodedPath(location.pathname).split("/");
    var name = parts.length > 1 ? parts[parts.length - 2] : "";
    for (var i = 0; i < ix.folders.length; i++) if (ix.folders[i].f === name) return ix.folders[i];
    return null;
  }
  function calendar() {
    if (window.CalendarData) return Promise.resolve(window.CalendarData);
    return loadScript(ROOT + "calendar-data.js").then(function () { return window.CalendarData || null; });
  }
  // Jaxon 2026-10-09: "Only forward moving content like for upcoming exams. No need for PIP to drill
  // old passed exams unless asked." An exam is PAST once its exam day is behind us. On a past exam's
  // pages Pip points ahead to the next exam and offers no practice, rescue or Claude of his own;
  // a typed "quiz me" there, or picking a past exam in Switch exam, is the student asking, and works.
  function examDate(f) {                          // that folder's exam day, from the calendar (null if none)
    return calendar().then(function (cal) {
      if (!cal || !cal.graded || !f) return null;
      var best = null;
      cal.graded().forEach(function (ev) {
        if (ev.k !== "exam" || ev.c !== f.c) return;
        var m = String(ev.t).match(/EXAM\s*#?\s*(\d+)/i), want = m ? +m[1] : null;
        if (want !== null && f.x !== null && f.x !== want) return;
        if (!best || ev.d > best) best = ev.d;
      });
      return best;
    });
  }
  var herePast = false;
  var PAST = {};                                  // exam slug -> its exam day is behind us (filled when Pip looks across exams)
  function nextExam(ix) {
    return calendar().then(function (cal) {
      if (!cal || !cal.graded) return null;
      var soon = cal.graded().filter(function (e) { return e.k === "exam" && daysUntil(e.d) >= 0; })
        .sort(function (a, b) { return a.d < b.d ? -1 : a.d > b.d ? 1 : 0; });
      for (var i = 0; i < soon.length; i++) {
        var ev = soon[i], m = String(ev.t).match(/EXAM\s*#?\s*(\d+)/i), want = m ? +m[1] : null, best = null;
        ix.folders.forEach(function (f) {
          if (f.c !== ev.c || (want !== null && f.x !== null && f.x !== want)) return;
          if (!best || f.quizzes.length > best.quizzes.length) best = f;
        });
        if (best) return { ev: ev, folder: best, days: daysUntil(ev.d) };
      }
      return soon.length ? { ev: soon[0], folder: null, days: daysUntil(soon[0].d) } : null;
    });
  }
  function doneQuizzes() {                     // decoded paths of every finished quiz on this device
    var s = {};
    try {
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (k && k.indexOf("qc:") === 0) { var v = jget(k, null); if (v && v.total > 0) s[decodedPath(k.slice(3))] = 1; }
      }
    } catch (e) {}
    return s;
  }
  function progressFor(folder) {
    var done = doneQuizzes(), n = 0;
    folder.quizzes.forEach(function (q) { if (done[decodedPath(new URL(pageURL(folder.f, q.file)).pathname)]) n++; });
    return { done: n, total: folder.quizzes.length };
  }
  function missedIds(folder, bank) {          // question ids this device last got wrong in this folder's quizzes
    var bySlug = {}, out = [];
    folder.quizzes.forEach(function (q) { bySlug[q.id] = q.file; });
    try {
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (!k || k.indexOf("qm:") !== 0) continue;
        var r = jget(k, null), file = r && bySlug[r.slug], ids = file && bank.pages[file];
        if (!ids || !r.m) continue;
        r.m.forEach(function (pair) { var id = ids[pair[0]]; if (id) out.push(id); });
      }
    } catch (e) {}
    return uniq(out);
  }
  function missCount() {
    var n = 0;
    try {
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (k && k.indexOf("qm:") === 0) { var r = jget(k, null); if (r && r.m) n += r.m.length; }
      }
    } catch (e) {}
    return n;
  }

  // ------------------------------------------------------------------ the quiz underneath
  function quizState() {
    // What the page has revealed so far. Never reads which answer is correct.
    var st = { onQuiz: P.kind === "quiz", unrevealed: [], current: null, answered: false, results: false };
    if (!st.onQuiz) return st;
    try {
      var res = document.getElementById("results");
      st.results = !!(res && res.style.display === "block");
      if (st.results || typeof QUESTIONS === "undefined" || typeof order === "undefined" || typeof answers === "undefined") return st;
      var hold = typeof holdFeedback === "function" ? holdFeedback() : false;
      order.forEach(function (qi, i) { if (hold || answers[i] === null) st.unrevealed.push(QUESTIONS[qi]); });
      var quiz = document.getElementById("quiz");
      if (quiz && quiz.style.display !== "none" && typeof idx === "number" && order[idx] != null) {
        st.current = QUESTIONS[order[idx]];
        st.answered = !hold && answers[idx] !== null;
      }
    } catch (e) {}
    return st;
  }
  // Pip is PAUSED (quizInProgress() is true) while a quiz question is still open. Jaxon, 2026-10-11:
  // once the CURRENT question is answered and its feedback is on screen, the student may ask Pip anything
  // until they move to the next question. So Pip stays paused: from Start until the current question is
  // answered; for the whole quiz when feedback waits until Submit ("No feedback until you submit");
  // and on a page whose quiz he cannot read (an older page): from Start until the results screen.
  // In the "All on a page" view he is not paused, but refuses anything that matches a question still
  // open (looksLikeOpenQuestion, and every pool he draws from leaves out the open questions: openSet()).
  // Stage-5 found the window could serve, and reveal the key of, questions still open on the page:
  // "quiz me on <two words of a stem>" drew that very question from the bank (the bank is made of the
  // same questions), which is why every pool leaves the open questions out.
  var pauseWhy = "open";
  function quizInProgress() {
    pauseWhy = "open";
    if (P.gated) { pauseWhy = "group"; return true; }                // a live group game: paused the whole time
    if (P.kind !== "quiz") return false;
    try {
      var st = document.getElementById("start"), res = document.getElementById("results"), qz = document.getElementById("quiz");
      if (res && res.style.display === "block") return false;
      if (st && st.style.display !== "none") return false;
      if (typeof order === "undefined" || typeof answers === "undefined" || typeof QUESTIONS === "undefined" || typeof idx === "undefined") {
        // cannot tell which question is open (an older page): paused while the quiz is showing
        pauseWhy = "unknown";
        return !qz || getComputedStyle(qz).display !== "none";
      }
      if (!order.length) return false;
      var defer = typeof deferFeedback !== "undefined" && deferFeedback;
      if (defer) { pauseWhy = "submit"; return true; }
      if (typeof viewMode !== "undefined" && viewMode === "scroll") return false;     // refused per question instead
      var q = quizState();
      return !(q.current && q.answered);
    } catch (e) { pauseWhy = "unknown"; return true; }
  }
  function openSet() {
    var ids = {}, stems = {};
    quizState().unrevealed.forEach(function (q) { if (q.qid) ids[q.qid] = 1; stems[norm(q.q).replace(/\s+/g, " ").trim()] = 1; });
    return { ids: ids, stems: stems };
  }
  function notOpen(list) {
    var o = openSet();
    return list.filter(function (q) { return !o.ids[q.id] && !o.ids[String(q.id).replace(/~\d+$/, "")] && !o.stems[norm(q.q).replace(/\s+/g, " ").trim()]; });
  }
  function pausedText() {
    quizInProgress();
    if (pauseWhy === "group") return "I stay quiet during a live group quiz so it stays fair. Ask me anything on a study page.";
    if (pauseWhy === "submit") return "You chose no feedback until you submit, so I'm on pause until you submit. After that, ask me anything.";
    if (pauseWhy === "unknown") return "I'm on pause while this quiz is open, so I can't give anything away. When you finish, ask me anything.";
    return "I'm on pause until you answer this question, so I can't give anything away. Once you've answered it and seen the feedback, ask me anything until you move on to the next question.";
  }
  function looksLikeOpenQuestion(text) {
    var qt = uniq(toks(text));
    var st = quizState(), nt = norm(text);
    for (var i = 0; i < st.unrevealed.length; i++) {
      var q = st.unrevealed[i], bag = {};
      toks(q.q + " " + q.opts.map(function (o) { return o[0]; }).join(" ")).forEach(function (w) { bag[w] = 1; });
      var hit = qt.filter(function (w) { return bag[w]; }).length;
      if (qt.length >= 4 && hit / qt.length >= 0.75) return true;
      if (norm(q.q).length > 24 && nt.indexOf(norm(q.q).slice(0, 40)) >= 0) return true;
    }
    return false;
  }

  // ------------------------------------------------------------------ the window
  var css = el("style");
  css.textContent = [
    "#pip-win{position:fixed;right:16px;bottom:16px;width:384px;max-width:calc(100vw - 32px);z-index:1900;display:flex;flex-direction:column;",
    " height:min(580px,calc(100vh - var(--pip-h,112px) - 36px));height:min(580px,calc(100dvh - var(--pip-h,112px) - 36px));",
    " background:#fff;color:#1b2440;border:1px solid rgba(30,57,116,.16);border-radius:18px;box-shadow:0 18px 50px rgba(20,30,70,.24);",
    " overflow:hidden;font:15px/1.45 system-ui,-apple-system,'Segoe UI',sans-serif;transform-origin:85% 100%;animation:pipwin-in .2s ease-out}",
    "@keyframes pipwin-in{from{opacity:0;transform:translateY(10px) scale(.97)}to{opacity:1;transform:none}}",
    "@media (prefers-reduced-motion:reduce){#pip-win{animation:none}}",
    "@media (max-width:600px){#pip-win{left:0;right:0;bottom:0;width:auto;max-width:none;border-radius:18px 18px 0 0;border-bottom:0;",
    " height:min(78vh,calc(100vh - var(--pip-h,112px) - 14px));height:min(78dvh,calc(100dvh - var(--pip-h,112px) - 14px));padding-bottom:env(safe-area-inset-bottom)}}",
    "#pip-win.pw-short{top:4px;bottom:4px!important;height:auto!important;max-height:none}",
    "#pip-win.pw-short .pw-head{padding-right:12px!important}",
    "#pip-win .pw-head{display:flex;align-items:center;gap:10px;padding:12px 12px 10px 16px;border-bottom:1px solid rgba(30,57,116,.1)}",
    "#pip-win .pw-ttl{flex:1;min-width:0}#pip-win .pw-ttl b{display:block;font-size:16px;color:#1E3974}",
    "#pip-win .pw-ttl span{display:block;font-size:12.5px;color:#5b6687;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}",
    "#pip-win .pw-x{flex:0 0 auto;width:34px;height:34px;border-radius:50%;border:0;background:transparent;color:#1E3974;font-size:22px;line-height:1;cursor:pointer}",
    "#pip-win .pw-x:hover,#pip-win .pw-x:focus-visible{background:#EEF2FA}",
    "#pip-win .pw-hide,#pip-win .pw-hbtn{flex:0 0 auto;border:1px solid rgba(30,57,116,.22);background:transparent;color:#1E3974;border-radius:999px;padding:5px 10px;font:600 12.5px/1 inherit;cursor:pointer;min-height:30px}",
    "#pip-win .pw-hide:hover,#pip-win .pw-hide:focus-visible,#pip-win .pw-hbtn:hover,#pip-win .pw-hbtn:focus-visible,#pip-win .pw-hbtn[aria-expanded=true]{background:#EEF2FA}",
    "@media (max-width:600px){#pip-win .pw-head{padding-right:max(12px,30%);gap:6px}#pip-win .pw-hide,#pip-win .pw-hbtn{padding:5px 8px}}",
    "html[data-theme=dark] #pip-win .pw-hide,html[data-theme=dark] #pip-win .pw-hbtn{color:#C9D8FA;border-color:#2b3f78}",
    "html[data-theme=dark] #pip-win .pw-hbtn:hover,html[data-theme=dark] #pip-win .pw-hbtn[aria-expanded=true],html[data-theme=dark] #pip-win .pw-hide:hover{background:#1c2a52}",
    // Teach Pip: the notes card and the "From your notes" results
    "#pip-win .pw-nrow{display:flex;align-items:center;gap:10px;padding:8px 0;border-top:1px solid rgba(30,57,116,.1)}",
    "#pip-win .pw-nlist .pw-nrow:first-child{border-top:0}",
    "#pip-win .pw-nname{flex:1;min-width:0}#pip-win .pw-nname b{display:block;font-size:13.5px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}",
    "#pip-win .pw-nname span{display:block;font-size:12px;color:#5b6687}",
    "#pip-win .pw-ndel{flex:0 0 auto;border:1px solid rgba(176,50,36,.35);background:transparent;color:#b03224;border-radius:999px;padding:5px 11px;font:600 12.5px/1 inherit;cursor:pointer;min-height:32px}",
    "#pip-win .pw-ndel:hover,#pip-win .pw-ndel:focus-visible{background:#fcefed}#pip-win .pw-ndel:disabled{opacity:.5;cursor:default}",
    "#pip-win .pw-nempty{font-size:13.5px;color:#5b6687;margin:4px 0 2px}",
    "#pip-win .pw-nfile{position:absolute;width:1px;height:1px;opacity:0;overflow:hidden;clip-path:inset(50%);pointer-events:none}",
    "#pip-win .pw-nstat{font-size:13px;margin-top:8px;white-space:pre-line;overflow-wrap:anywhere}#pip-win .pw-nstat:empty{display:none}",
    "#pip-win .pw-nstat.bad{color:#b03224}",
    "#pip-win .pw-npriv{font-size:12.5px;color:#3d4a6b;background:#F4F7FD;border-radius:10px;padding:8px 10px;margin-top:10px}",
    "#pip-win .pw-card.pw-note{border-left:3px solid #D9A441}",
    "html[data-theme=dark] #pip-win .pw-nname span,html[data-theme=dark] #pip-win .pw-nempty{color:#9fb0d6}",
    "html[data-theme=dark] #pip-win .pw-nrow{border-color:#22335f}html[data-theme=dark] #pip-win .pw-npriv{background:#16213f;color:#C9D8FA}",
    "html[data-theme=dark] #pip-win .pw-ndel{color:#f08a7e;border-color:#7a3a33}html[data-theme=dark] #pip-win .pw-ndel:hover{background:#3a1714}",
    "html[data-theme=dark] #pip-win .pw-nstat.bad{color:#f08a7e}html[data-theme=dark] #pip-win .pw-card.pw-note{border-left-color:#C8953A}",
    "#pip-win .pw-log{flex:1;overflow-y:auto;padding:14px 14px 6px;display:flex;flex-direction:column;gap:9px;overscroll-behavior:contain}",
    "#pip-win .pw-msg{max-width:88%;padding:9px 12px;border-radius:14px;white-space:pre-line;overflow-wrap:anywhere}",
    "#pip-win .pw-pip{align-self:flex-start;background:#F1F4FB;border-bottom-left-radius:4px}",
    "#pip-win .pw-me{align-self:flex-end;background:#1E3974;color:#fff;border-bottom-right-radius:4px}",
    "#pip-win .pw-card{align-self:stretch;border:1px solid rgba(30,57,116,.14);border-radius:12px;padding:10px 12px;background:#fff}",
    "#pip-win .pw-card h4{margin:0 0 2px;font-size:13px;color:#1E3974}",
    "#pip-win .pw-card .pw-src{font-size:12px;color:#5b6687;margin-bottom:4px}",
    "#pip-win .pw-card p{margin:0;font-size:14px}",
    "#pip-win .pw-card a{color:#1E3974;font-weight:600;font-size:13px;text-decoration:none;display:inline-block;margin-top:6px}",
    "#pip-win .pw-card a:hover{text-decoration:underline}",
    "#pip-win mark{background:#FFE7A0;color:inherit;border-radius:3px;padding:0 1px}",
    "#pip-win .pw-chips{display:flex;gap:6px;overflow-x:auto;padding:8px 12px 2px;scrollbar-width:none;flex:0 0 auto}",
    "#pip-win .pw-chips::-webkit-scrollbar{display:none}",
    "#pip-win .pw-chip{flex:0 0 auto;border:1px solid #7d89ab;background:#fff;color:#1E3974;border-radius:999px;padding:7px 12px;",
    " font:600 13px/1.2 inherit;cursor:pointer;white-space:nowrap}",
    "#pip-win .pw-chip:hover,#pip-win .pw-chip:focus-visible{background:#EEF2FA}",
    "#pip-win form{display:flex;gap:8px;padding:8px 12px 12px;flex:0 0 auto}",
    "#pip-win .pw-in{flex:1;min-width:0;border:1px solid #7d89ab;border-radius:12px;padding:9px 12px;font:16px/1.3 inherit;color:inherit;background:#fff}",
    "#pip-win .pw-in:focus{outline:2px solid #3d63c4;outline-offset:0}",   // the border stays; the focus ring is 5:1 on white
    "#pip-win .pw-send{flex:0 0 auto;border:0;border-radius:12px;padding:0 14px;background:#1E3974;color:#fff;font:600 14px inherit;cursor:pointer}",
    "#pip-win .pw-meta{display:flex;justify-content:space-between;gap:8px;font-size:12px;color:#5b6687;margin-bottom:6px}",
    "#pip-win .pw-io{font-size:12px;color:#1E3974;background:#EEF2FA;border-radius:999px;padding:3px 9px;display:inline-block;margin-bottom:6px;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}",
    "#pip-win .pw-q{font-weight:600;margin:0 0 6px}",
    "#pip-win .pw-opt{display:flex;gap:9px;align-items:flex-start;width:100%;text-align:left;border:1px solid #7d89ab;border-radius:10px;",
    " padding:8px 10px;margin-top:6px;background:#fff;color:inherit;cursor:pointer;font:14px/1.4 inherit}",
    "#pip-win .pw-opt:hover:not(:disabled){border-color:#6E96E6}",
    "#pip-win .pw-opt:disabled{cursor:default}",
    "#pip-win .pw-opt .l{flex:0 0 22px;height:22px;border-radius:50%;display:grid;place-items:center;background:#EEF2FA;font-weight:700;font-size:12px;margin-top:-1px}",
    "#pip-win .pw-opt.ok{border-color:#2e8b57;background:#eaf7ef}#pip-win .pw-opt.ok .l{background:#23794a;color:#fff}",
    "#pip-win .pw-opt.bad{border-color:#c0392b;background:#fcefed}#pip-win .pw-opt.bad .l{background:#c0392b;color:#fff}",
    "#pip-win .pw-verdict{font-weight:700;margin-top:10px}#pip-win .pw-verdict.ok{color:#23794a}#pip-win .pw-verdict.bad{color:#b03224}",
    "#pip-win .pw-ex{font-size:13.5px;margin-top:4px}#pip-win .pw-ex div{margin-top:5px;padding-left:18px;text-indent:-18px}",
    "#pip-win .pw-cite{font-size:12px;color:#5b6687;font-style:italic;margin-top:6px}",
    "#pip-win .pw-next{margin-top:10px;border:0;border-radius:10px;padding:8px 14px;background:#1E3974;color:#fff;font:600 14px inherit;cursor:pointer}",
    "#pip-win .pw-brain .pw-lbl{display:block;margin-top:6px;font-size:11.5px;color:#5b6687}",
    "#pip-win .pw-row{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:8px}#pip-win .pw-row .pw-next{margin-top:0}",
    "#pip-win .pw-prog{height:6px;border-radius:3px;background:#EEF2FA;overflow:hidden;margin-top:10px}",
    "#pip-win .pw-prog i{display:block;height:100%;width:0;background:#6E96E6;transition:width .3s}",
    "html[data-theme=dark] #pip-win .pw-brain .pw-lbl{color:#9fb0d6}html[data-theme=dark] #pip-win .pw-prog{background:#1c2a52}",
    // the brain card that opens the window on a computer that can run his brain and has none yet
    "#pip-win .pw-card.pw-brainask{border:1.5px solid #6E96E6;padding:14px 14px 12px}",
    "#pip-win .pw-brainask h4{font-size:15px;margin-bottom:6px}#pip-win .pw-brainask p+p{margin-top:6px}",
    "#pip-win .pw-big{display:block;width:100%;margin-top:12px;padding:12px 16px;border:0;border-radius:12px;background:#1E3974;color:#fff;",
    " font-family:inherit;font-size:16px;font-weight:700;cursor:pointer}",
    "#pip-win .pw-big:hover,#pip-win .pw-big:focus-visible{background:#2a4d96}",
    "#pip-win .pw-later{display:block;margin:6px auto 0;min-height:32px;padding:6px 12px;border:0;background:transparent;color:#3d4a6b;",
    " font-family:inherit;font-size:13px;font-weight:600;text-decoration:underline;cursor:pointer}",
    "#pip-win .pw-brainask .pw-src{margin:8px 0 0;text-align:center}#pip-win .pw-brainask .pw-prog+.pw-src{text-align:left}",
    "html[data-theme=dark] #pip-win .pw-card.pw-brainask{border-color:#6E96E6}html[data-theme=dark] #pip-win .pw-big{background:#3d63c4}",
    "html[data-theme=dark] #pip-win .pw-big:hover{background:#4d73d4}html[data-theme=dark] #pip-win .pw-later{color:#C9D8FA}",
    "#pip-win .pw-claude{border-color:rgba(217,119,87,.45);background:#FFF8F4}",
    "#pip-win .pw-chead{display:flex;align-items:center;gap:8px;margin-bottom:4px}#pip-win .pw-chead b{color:#B4532F;font-size:13px}",
    "#pip-win .pw-badge{font-size:11.5px;font-weight:600;color:#7a4a12;background:#FDEBC8;border-radius:999px;padding:2px 8px}",
    "#pip-win .pw-claude p{margin:4px 0 0}#pip-win .pw-claude ul{margin:4px 0 0;padding-left:20px}#pip-win .pw-claude li{margin-top:2px}",
    "#pip-win .pw-claude .pw-src{margin-top:8px}#pip-win .pw-claude .pw-src a{margin:0;font-size:12px}",
    "html[data-theme=dark] #pip-win .pw-claude{background:#2a1c18;border-color:#7a4632}html[data-theme=dark] #pip-win .pw-chead b{color:#F0A987}",
    "html[data-theme=dark] #pip-win .pw-badge{background:#4a3410;color:#F5D58E}",
    "#pip-win .pw-bar{display:flex;align-items:center;gap:8px;font-size:13px;margin-top:5px}",
    "#pip-win .pw-bar span:first-child{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}",
    ".pip-flash{outline:3px solid #6E96E6;outline-offset:3px;border-radius:6px;transition:outline-color 1.6s ease .9s}",
    ".pip-flash.pip-flash-off{outline-color:transparent}",
    ".pip-rescue{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;margin:14px 0;padding:12px 14px;border-radius:12px;",
    " border:1px solid rgba(30,57,116,.18);background:#F4F7FD;color:#1b2440;font-size:14px}",
    ".pip-rescue b{color:#1E3974}.pip-rescue span{flex:1 1 220px}",
    ".pip-rescue button{border:0;border-radius:10px;padding:8px 12px;background:#1E3974;color:#fff;font:600 13.5px system-ui,sans-serif;cursor:pointer}",
    "html[data-theme=dark] #pip-win{background:#121a33;color:#E6EDFB;border-color:#2b3f78;box-shadow:0 18px 50px rgba(0,0,0,.5)}",
    "html[data-theme=dark] #pip-win .pw-head{border-color:#22335f}html[data-theme=dark] #pip-win .pw-ttl b{color:#C9D8FA}",
    "html[data-theme=dark] #pip-win .pw-ttl span,html[data-theme=dark] #pip-win .pw-src,html[data-theme=dark] #pip-win .pw-meta,html[data-theme=dark] #pip-win .pw-cite{color:#9fb0d6}",
    "html[data-theme=dark] #pip-win .pw-x{color:#C9D8FA}html[data-theme=dark] #pip-win .pw-x:hover{background:#1c2a52}",
    "html[data-theme=dark] #pip-win .pw-pip{background:#1c2a52}html[data-theme=dark] #pip-win .pw-me{background:#3d63c4}",
    // dark outlines at >= 3:1 against the window (they are what marks a chip or an option as a button)
    "html[data-theme=dark] #pip-win .pw-card,html[data-theme=dark] #pip-win .pw-opt,html[data-theme=dark] #pip-win .pw-in,html[data-theme=dark] #pip-win .pw-chip{background:#121a33;border-color:#5b6fa8;color:#E6EDFB}",
    "html[data-theme=dark] #pip-win .pw-card h4,html[data-theme=dark] #pip-win .pw-card a,html[data-theme=dark] #pip-win .pw-chip,html[data-theme=dark] #pip-win .pw-io{color:#C9D8FA}",
    "html[data-theme=dark] #pip-win .pw-io,html[data-theme=dark] #pip-win .pw-opt .l{background:#1c2a52}",
    "html[data-theme=dark] #pip-win .pw-opt.ok{background:#12301f;border-color:#3fae6e}html[data-theme=dark] #pip-win .pw-opt.bad{background:#3a1714;border-color:#d0574a}",
    "html[data-theme=dark] #pip-win .pw-verdict.ok{color:#6fd39a}html[data-theme=dark] #pip-win .pw-verdict.bad{color:#f08a7e}",
    "html[data-theme=dark] #pip-win mark{background:#6b5a1f;color:#fff}",
    "html[data-theme=dark] #pip-win .pw-in{border-color:#6a7fb8}html[data-theme=dark] #pip-win .pw-in::placeholder{color:#9fb0d6}",
    "html[data-theme=dark] #pip-win .pw-send,html[data-theme=dark] #pip-win .pw-next,html[data-theme=dark] .pip-rescue button{background:#3d63c4}",
    "html[data-theme=dark] .pip-rescue{background:#16213f;border-color:#2b3f78;color:#E6EDFB}html[data-theme=dark] .pip-rescue b{color:#C9D8FA}",
    // Pip explains: his plain-language explanation leads an answer; the guide's own words follow it
    "#pip-win .pw-explain{max-width:94%;white-space:normal}",
    "#pip-win .pw-explain .pw-xh{display:block;font-size:12.5px;font-weight:700;color:#2f55b8;margin-bottom:4px}",
    "#pip-win .pw-explain .pw-xl{display:block;font-size:12px;color:#5b6687;margin:-2px 0 6px}html[data-theme=dark] #pip-win .pw-explain .pw-xl{color:#9fb0d6}",
    "#pip-win .pw-explain p{margin:0}#pip-win .pw-explain p+p{margin-top:8px}",
    "#pip-win .pw-explain ul{margin:6px 0 0;padding-left:20px}#pip-win .pw-explain li{margin-top:3px}",
    "#pip-win .pw-explain a{display:inline-block;margin-top:8px;color:#1E3974;font-weight:600;font-size:13px;text-decoration:none}",
    "#pip-win .pw-explain a:hover{text-decoration:underline}",
    "#pip-win .pw-glink a,#pip-win .pw-brain a{display:inline-block;margin-top:8px;color:#1E3974;font-weight:600;font-size:13px;text-decoration:none}",
    "#pip-win .pw-glink a:hover,#pip-win .pw-brain a:hover{text-decoration:underline}",
    "html[data-theme=dark] #pip-win .pw-glink a,html[data-theme=dark] #pip-win .pw-brain a{color:#C9D8FA}",
    "#pip-win .pw-help{display:flex;align-items:center;gap:6px;margin-top:8px;font-size:12.5px;color:#5b6687}",
    "#pip-win .pw-help.pw-thanked{display:block}",
    "#pip-win .pw-fb{margin-top:8px;font-size:13px}#pip-win .pw-fb p{margin:0 0 6px}#pip-win .pw-fb .pw-row{margin-top:6px}",
    "#pip-win .pw-fbc{width:100%;box-sizing:border-box;font:inherit;font-size:16px;padding:8px 10px;border-radius:10px;border:1px solid rgba(30,57,116,.25);background:#fff;color:#1d2433;resize:vertical}",
    "html[data-theme=dark] #pip-win .pw-fbc{background:#16213f;color:#e6ecfa;border-color:rgba(201,216,250,.3)}",
    "#pip-win .pw-thumb{display:inline-flex;align-items:center;justify-content:center;width:40px;height:34px;padding:0;border:1px solid #c9d1e6;border-radius:999px;background:#fff;color:#1E3974;cursor:pointer}",
    "#pip-win .pw-thumb:hover,#pip-win .pw-thumb:focus-visible{background:#EEF2FA}",
    "#pip-win .pw-down svg{transform:rotate(180deg)}",
    "html[data-theme=dark] #pip-win .pw-help{color:#9fb0d6}html[data-theme=dark] #pip-win .pw-thumb{background:#121a33;border-color:#5b6fa8;color:#C9D8FA}",
    "#pip-win .pw-card .pw-explain{max-width:none;margin-top:10px;padding:10px 12px;border-radius:12px;background:#F1F4FB}",
    "#pip-win .pw-guidehd{font-size:12px;color:#5b6687;margin:2px 2px -4px}#pip-win .pw-slot{display:contents}",
    // the two labelled parts of an answer (2026-10-15): "From your class" and "From general knowledge"
    "#pip-win .pw-part{font-size:11.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#5b6687;margin:12px 2px -2px}",
    "#pip-win .pw-fixed{display:block;font-weight:400;letter-spacing:0;text-transform:none;font-size:12px;margin-top:2px}",
    "#pip-win .pw-deflead{font-weight:700}#pip-win .pw-explain li a{display:inline;margin-top:0;font-weight:500}",
    "#pip-win .pw-alinks{margin-top:4px}#pip-win .pw-alinks a,#pip-win .pw-alinks span{display:block;margin-top:6px}#pip-win .pw-left{margin:2px 4px 0;text-align:right}",
    "#pip-win .pw-explain .pw-lbl{display:block;margin-top:6px;font-size:11.5px;color:#5b6687}html[data-theme=dark] #pip-win .pw-explain .pw-lbl{color:#9fb0d6}",
    "#pip-win .pw-explain .pw-quote{border-left:3px solid rgba(30,57,116,.25);padding-left:9px;margin-top:6px;color:#33405f}",
    "html[data-theme=dark] #pip-win .pw-part{color:#9fb0d6}html[data-theme=dark] #pip-win .pw-explain .pw-quote{color:#d3ddf5;border-left-color:rgba(201,216,250,.35)}",
    // comparisons: the side-by-side dissection, the guide links under it, the folded full cards
    "#pip-win .pw-cmp{align-self:stretch;max-width:none;white-space:normal}",
    "#pip-win .pw-cmp p{margin:0}#pip-win .pw-cmp p+p{margin-top:8px}",
    "#pip-win .pw-cmpgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:4px 8px;margin-top:8px}",
    "#pip-win .pw-cmpgrid.pw-cmp1{grid-template-columns:minmax(0,1fr)}",
    "#pip-win .pw-cmphd{font-size:13px;color:#1E3974;padding:0 2px}",
    "#pip-win .pw-cmprow{grid-column:1/-1;margin-top:6px;font-size:11.5px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:#5b6687}",
    "#pip-win .pw-cmpcell{background:#fff;border:1px solid rgba(30,57,116,.14);border-radius:10px;padding:7px 9px;font-size:13.5px;line-height:1.4;overflow-wrap:anywhere}",
    "#pip-win .pw-cmpnone{color:#5b6687;font-style:italic;background:transparent;border-style:dashed}",
    "#pip-win .pw-cmpbottom{margin-top:10px!important;padding-top:8px;border-top:1px solid rgba(30,57,116,.14)}",
    "#pip-win .pw-cmplinks{display:flex;flex-direction:column;gap:2px;max-width:none}",
    "#pip-win .pw-cmplinks a{color:#1E3974;font-weight:600;font-size:13px;text-decoration:none;padding:4px 0}#pip-win .pw-cmplinks a:hover{text-decoration:underline}",
    "#pip-win .pw-more{align-self:stretch;font-size:13px}#pip-win .pw-more>summary{cursor:pointer;color:#1E3974;font-weight:600;padding:4px 2px}",
    "#pip-win .pw-more>.pw-msg{margin-top:8px}",
    "html[data-theme=dark] #pip-win .pw-cmpcell{background:#121a33;border-color:#2b3f78}html[data-theme=dark] #pip-win .pw-cmpnone{background:transparent}",
    "html[data-theme=dark] #pip-win .pw-cmphd,html[data-theme=dark] #pip-win .pw-cmplinks a,html[data-theme=dark] #pip-win .pw-more>summary{color:#C9D8FA}",
    "html[data-theme=dark] #pip-win .pw-cmprow,html[data-theme=dark] #pip-win .pw-cmpnone{color:#9fb0d6}html[data-theme=dark] #pip-win .pw-cmpbottom{border-color:#2b3f78}",
    "#pip-win .pw-xbtn{margin-top:10px;margin-left:8px}",
    "html[data-theme=dark] #pip-win .pw-explain .pw-xh{color:#9fb8f5}html[data-theme=dark] #pip-win .pw-explain a{color:#C9D8FA}",
    "html[data-theme=dark] #pip-win .pw-guidehd{color:#9fb0d6}html[data-theme=dark] #pip-win .pw-card .pw-explain{background:#1c2a52}",
    // full screen: the window fills the screen with the conversation in a readable column; minimize puts it back
    "#pip-win .pw-fs{flex:0 0 auto;width:34px;height:34px;border-radius:50%;border:0;padding:0;background:transparent;color:#1E3974;cursor:pointer;display:grid;place-items:center}",
    "#pip-win .pw-fs:hover,#pip-win .pw-fs:focus-visible{background:#EEF2FA}#pip-win .pw-fs svg{width:18px;height:18px;display:block}",
    "html[data-theme=dark] #pip-win .pw-fs{color:#C9D8FA}html[data-theme=dark] #pip-win .pw-fs:hover,html[data-theme=dark] #pip-win .pw-fs:focus-visible{background:#1c2a52}",
    "#pip-win.pw-full{top:0;left:0;right:0;bottom:0;width:auto;max-width:none;height:auto!important;max-height:none;border:0;border-radius:0;box-shadow:none;",
    " padding:env(safe-area-inset-top) env(safe-area-inset-right) 0 env(safe-area-inset-left);animation:pipwin-full .18s ease-out}",
    "@keyframes pipwin-full{from{opacity:.5;transform:scale(.985)}to{opacity:1;transform:none}}",
    "#pip-win.pw-full .pw-head{padding:14px max(16px,calc((100% - 780px)/2)) 12px}#pip-win.pw-full .pw-ttl b{font-size:18px}",
    "#pip-win.pw-full .pw-log{padding:20px max(16px,calc((100% - 780px)/2)) 8px;gap:11px}",
    "#pip-win.pw-full .pw-chips{padding:8px max(12px,calc((100% - 780px)/2)) 2px}",
    "#pip-win.pw-full form{padding:8px max(12px,calc((100% - 780px)/2)) max(16px,env(safe-area-inset-bottom))}",
    "#pip-win.pw-full .pw-msg{max-width:82%}#pip-win.pw-full .pw-explain{max-width:100%;font-size:16px;line-height:1.55}",
    "@media (prefers-reduced-motion:reduce){#pip-win.pw-full{animation:none}}",
    "@media print{#pip-win,.pip-rescue{display:none}}"
  ].join("\n");
  document.head.appendChild(css);

  var win = null, log, chipsBox, input, sub, notesBtn, fsBtn, isOpen = false, drillActive = null, full = false;
  var ASK_HINT = "Ask me to explain anything";

  function build() {
    win = el("section"); win.id = "pip-win";
    win.setAttribute("role", "dialog"); win.setAttribute("aria-label", "Pip, your study buddy");
    var head = el("div", "pw-head"), ttl = el("div", "pw-ttl");
    ttl.appendChild(el("b", null, "Pip")); sub = el("span", null, "Your study buddy"); ttl.appendChild(sub);
    // Teach Pip: the student's own notes for this exam, kept on this device
    notesBtn = el("button", "pw-hbtn", "Notes"); notesBtn.type = "button";
    notesBtn.title = "Your own notes for this exam (they stay on this device)";
    notesBtn.setAttribute("aria-expanded", "false");
    notesBtn.addEventListener("click", function () { toggleNotes(); });
    var hide = el("button", "pw-hide", "Hide Pip"); hide.type = "button";
    hide.title = "Hide Pip on every page (bring him back from the Pip tab or Settings)";
    hide.addEventListener("click", function () { close(); P.hide(); });
    // Jaxon, 2026-10-09: "Make it so people can make PIP full screen as well and then can minimize him
    // back to the page they were on". The page underneath never moves, so minimizing lands right back on it.
    fsBtn = el("button", "pw-fs"); fsBtn.type = "button";
    fsBtn.addEventListener("click", function () { setFull(!full); });
    fsIcon();
    var x = el("button", "pw-x", "×"); x.type = "button"; x.setAttribute("aria-label", "Close Pip's window"); x.title = "Close";
    x.addEventListener("click", function () { close(); });
    head.appendChild(ttl); head.appendChild(notesBtn); head.appendChild(hide); head.appendChild(fsBtn); head.appendChild(x);
    log = el("div", "pw-log"); log.setAttribute("aria-live", "polite");
    chipsBox = el("div", "pw-chips");
    var form = el("form");
    input = el("input", "pw-in"); input.type = "text"; input.placeholder = ASK_HINT;
    input.setAttribute("aria-label", "Ask Pip"); input.autocomplete = "off"; input.setAttribute("enterkeyhint", "send");
    var send = el("button", "pw-send", "Ask"); send.type = "submit";
    form.appendChild(input); form.appendChild(send);
    form.addEventListener("submit", function (e) { e.preventDefault(); var t = input.value.trim(); if (!t || held(t)) return; input.value = ""; ask(t); });
    win.appendChild(head); win.appendChild(log); win.appendChild(chipsBox); win.appendChild(form);
    // nothing typed or pressed in here reaches the quiz's page-wide keyboard shortcuts
    win.addEventListener("keydown", function (e) {
      e.stopPropagation();
      if (e.key === "Escape") { e.preventDefault(); if (full) { setFull(false); fsBtn.focus(); } else close(); return; }
      if (full && e.key === "Tab") { trapTab(e); return; }       // full screen covers the page: keep focus inside
      if (e.target === input || e.ctrlKey || e.metaKey || e.altKey) return;
      // keys on the window's other controls (Notes, its file picker and buttons, Hide, close) belong to
      // those controls; only keys pressed in the drill card itself, or on nothing in particular, run the drill
      var t = e.target;
      if (t && t.closest && t !== win && !t.closest(".pw-drill") && t.matches("button, a, input, select, textarea, label, summary")) return;
      if (drillActive && drillActive.key(e)) e.preventDefault();
    });
    ["keyup", "keypress"].forEach(function (t) { win.addEventListener(t, function (e) { e.stopPropagation(); }); });
    document.body.appendChild(win);
    document.addEventListener("keydown", function (e) {
      if (isOpen && e.key === "Escape" && !e.defaultPrevented && !document.querySelector(".settings-overlay.open, .tour-overlay.open")) { if (full) setFull(false); else close(); }
    });
    window.addEventListener("resize", place);
    if (window.visualViewport) window.visualViewport.addEventListener("resize", place);
  }

  // Pip stands on top of his window while it is open
  function place() {
    if (!isOpen || !win) return;
    var k = P.scale(), vv = window.visualViewport;
    var kb = vv ? Math.max(0, window.innerHeight - vv.height - vv.offsetTop) : 0;   // on-screen keyboard
    if (full) {
      // full screen: Pip stands in his usual corner, in the margin beside the conversation, when that
      // margin fits him and Clawd (who joins him there to fetch answers); on narrower screens he waits
      win.classList.remove("pw-short");
      win.style.bottom = kb + "px";
      var margin = (window.innerWidth - 780) / 2;
      P.dock.style.bottom = ""; P.dock.style.right = "";
      P.dock.style.visibility = kb || margin < (P.frameW + P.clawdDX) * k * 0.8 ? "hidden" : "";
      return;
    }
    win.style.bottom = (window.innerWidth <= 600 ? kb : 16 + kb) + "px";
    var short = window.innerHeight - kb < 520;
    win.classList.toggle("pw-short", short);
    P.dock.style.visibility = short ? "hidden" : "";
    if (short) return;
    // layout box, not getBoundingClientRect: the opening animation scales the window for a moment
    var top = win.offsetTop, right = win.offsetLeft + win.offsetWidth;
    P.dock.style.bottom = Math.round(window.innerHeight - top - (P.frameH - P.ground) * k - 1) + "px";
    P.dock.style.right = Math.round(window.innerWidth - right + (window.innerWidth <= 600 ? 4 : 8)) + "px";
  }

  function open(intent) {
    if (!win) build();
    var first = !isOpen;
    win.style.display = "";
    win.style.setProperty("--pip-h", (P.frameH * P.scale()) + "px");
    isOpen = true; P.setOpen(true);
    place();
    if (first) {
      count("pip_open");
      try { if (window.PAMetrics) window.PAMetrics.mark("pip_users"); } catch (e) {}
      P.react("wave", 1);                       // the student tapped him: say hi
      log.textContent = ""; chips([]);
      notesCard = null; notesBtn.setAttribute("aria-expanded", "false");
      openGate(intent);                           // the brain card first, when this computer should get one
    } else if (intent) { if (gate.state === "off") greet(intent); else gate.intent = intent; }
    if (window.matchMedia && window.matchMedia("(pointer:fine)").matches && !(intent && intent.drill)) setTimeout(function () { input.focus(); }, 60);
  }
  // full screen on or off; the page underneath is never touched, only its scrolling is paused
  var EXPAND = "M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5", SHRINK = "M9 4v5H4M15 4v5h5M9 20v-5H4M15 20v-5h5", pageOverflow = null;
  function fsIcon() {
    fsBtn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="' + (full ? SHRINK : EXPAND) + '"/></svg>';
    fsBtn.setAttribute("aria-label", full ? "Minimize Pip back to the page" : "Make Pip full screen");
    fsBtn.title = full ? "Minimize (back to the page)" : "Full screen";
  }
  function setFull(on) {
    if (!win || full === !!on) return;
    full = !!on;
    win.classList.toggle("pw-full", full);
    win.setAttribute("aria-modal", full ? "true" : "false");
    var de = document.documentElement;
    if (full) { pageOverflow = de.style.overflow; de.style.overflow = "hidden"; }
    else if (pageOverflow !== null) { de.style.overflow = pageOverflow; pageOverflow = null; }
    fsIcon(); place();
    scrollDown();
  }
  function trapTab(e) {
    var f = Array.prototype.filter.call(win.querySelectorAll("button, a[href], input, select, textarea, [tabindex]:not([tabindex='-1'])"),
      function (n) { return !n.disabled && n.offsetParent !== null && !n.classList.contains("pw-nfile"); });
    if (!f.length) return;
    var i = f.indexOf(document.activeElement);
    if (e.shiftKey && i <= 0) { e.preventDefault(); f[f.length - 1].focus(); }
    else if (!e.shiftKey && (i === -1 || i === f.length - 1)) { e.preventDefault(); f[0].focus(); }
  }
  function close() {
    if (!win || !isOpen) return;
    setFull(false);                             // closing always lands back on the page as it was
    isOpen = false; drillActive = null;
    gate = { state: "off", closed: true };      // the next open asks again; questions waiting on a download are dropped
    if (P.duet && P.duet.active()) P.duet.cancel();   // the answer still lands in the window for next time
    win.style.display = "none";
    P.dock.style.bottom = ""; P.dock.style.right = ""; P.dock.style.visibility = "";
    P.setOpen(false);
  }

  // ------------------------------------------------------------------ messages
  function scrollDown() { log.scrollTop = log.scrollHeight; }
  function say(text) { var m = el("div", "pw-msg pw-pip", text); log.appendChild(m); scrollDown(); return m; }
  function me(text) { var m = el("div", "pw-msg pw-me", text); log.appendChild(m); scrollDown(); return m; }
  function card() { var c = el("div", "pw-card"); log.appendChild(c); scrollDown(); return c; }
  function chips(list) {
    chipsBox.textContent = "";
    list.forEach(function (c) {
      var b = el("button", "pw-chip", c[0]); b.type = "button";
      b.addEventListener("click", function () { if (c[2] !== false) me(c[0]); c[1](); });
      chipsBox.appendChild(b);
    });
    chipsBox.style.display = list.length ? "" : "none";
  }
  // Jaxon, 2026-10-11: a guide link opens the guide in the site's own study-guide panel (theme.js
  // window.openGuidePanel, the same one a quiz's "Find it in the study guide" uses), scrolled to the passage and
  // highlighted, so the student never loses the page they are on. On the guide itself it just scrolls there;
  // a page without theme.js (no panel) opens the guide in a new tab.
  function linkTo(folder, file, anchor, label, passage) {
    var a = el("a", null, label || "Open in the guide →");
    a.href = pageURL(folder, file, anchor);
    var here = decodedPath(new URL(a.href).pathname) === decodedPath(location.pathname);
    if (here) a.addEventListener("click", function (e) { e.preventDefault(); reveal(anchor); if (window.innerWidth <= 600) close(); });
    else if (!window.openGuidePanel) { a.target = "_blank"; a.rel = "noopener"; }
    else a.addEventListener("click", function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.button) return;     // a new-tab click still opens a tab
      var fo = IX && IX.folders.filter(function (x) { return x.f === folder; })[0];
      if (window.openGuidePanel({ url: a.href, anchor: anchor, title: fo ? fo.t : "", label: "Study guide", passage: passage || "" })) e.preventDefault();
    });
    return a;
  }
  function reveal(id) {
    var t = document.getElementById(id); if (!t) return;
    for (var n = t; n; n = n.parentElement) if (n.tagName === "DETAILS") n.open = true;
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    t.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "center" });
    t.classList.remove("pip-flash", "pip-flash-off"); void t.offsetWidth; t.classList.add("pip-flash");
    setTimeout(function () { t.classList.add("pip-flash-off"); }, 50);
    setTimeout(function () { t.classList.remove("pip-flash", "pip-flash-off"); }, 2800);
  }
  function snippet(text, query) {
    var qt = uniq(toks(query)).filter(function (w) { return w.length >= 2; });
    var re = qt.length ? new RegExp("\\b(" + qt.map(escRe).join("|") + ")[a-z0-9]*", "gi") : null;
    var start = 0, m = re && re.exec(text);
    if (m && m.index > 90) { start = text.lastIndexOf(" ", m.index - 70); if (start < 0) start = 0; }
    var s = text.slice(start, start + 280), end = start + 280 < text.length;
    if (end) s = s.slice(0, s.lastIndexOf(" ") > 200 ? s.lastIndexOf(" ") : s.length);
    var p = el("p");
    if (start > 0) p.appendChild(document.createTextNode("… "));
    if (re) {
      re.lastIndex = 0; var last = 0, mm;
      while ((mm = re.exec(s))) {
        p.appendChild(document.createTextNode(s.slice(last, mm.index)));
        p.appendChild(el("mark", null, mm[0])); last = mm.index + mm[0].length;
      }
      p.appendChild(document.createTextNode(s.slice(last)));
    } else p.appendChild(document.createTextNode(s));
    if (end) p.appendChild(document.createTextNode(" …"));
    return p;
  }

  // ------------------------------------------------------------------ Teach Pip: the student's own notes
  // Notes stay on this device (IndexedDB, in pip/pip-notes.js, loaded only when needed) and
  // belong to ONE exam: the one Pip is working on. Search uses only that exam's notes.
  // Note text is only ever put on the page as text (el / textContent), never as HTML.
  var notesP = null, notesCard = null, notesList = null, notesStat = null, notesFor = null;
  var NOTES_PRIVACY = "Your notes stay on this device. Pip never uploads them; when Pip checks with Claude he sends only the few lines that match your question.";
  var NOTES_ACCEPT = ".pdf,.docx,.txt,.md,application/pdf,text/plain,text/markdown,application/vnd.openxmlformats-officedocument.wordprocessingml.document";
  function notes() {
    if (!notesP) notesP = window.PipNotes ? Promise.resolve(window.PipNotes)
      : loadScript(ROOT + "pip/pip-notes.js").then(function () { return window.PipNotes || null; });
    notesP.then(function (N) { if (!N) notesP = null; });
    return notesP;
  }
  function toggleNotes() {
    if (notesCard && notesCard.isConnected) { notesCard.remove(); notesCard = null; notesBtn.setAttribute("aria-expanded", "false"); return; }
    notesCard = card(); notesCard.classList.add("pw-notes");
    notesBtn.setAttribute("aria-expanded", "true");
    renderNotes();
  }
  function renderNotes() {
    var cd = notesCard;
    if (!cd) return;
    context().then(function (c) {
      if (cd !== notesCard) return;
      var f = c.active;
      notesFor = f; cd.textContent = "";
      cd.appendChild(el("h4", null, f ? "Your notes for " + f.t : "Your notes"));
      if (!f) {
        cd.appendChild(el("p", "pw-nempty", "Pick an exam first, then you can add your notes for it."));
        chips([["Switch exam", function () { switchExam(); }]]);
        return scrollTo(cd);
      }
      notesList = el("div", "pw-nlist"); cd.appendChild(notesList);
      notesStat = el("div", "pw-nstat"); notesStat.setAttribute("role", "status"); cd.appendChild(notesStat);
      var row = el("div", "pw-row"), add = el("button", "pw-next", "Add notes"), inp = el("input", "pw-nfile");
      add.type = "button";
      inp.type = "file"; inp.multiple = true; inp.accept = NOTES_ACCEPT; inp.tabIndex = -1;
      inp.setAttribute("aria-hidden", "true");
      add.addEventListener("click", function () { inp.click(); });
      inp.addEventListener("change", function () {
        var files = Array.prototype.slice.call(inp.files || []); inp.value = "";
        addNotes(f, files);
      });
      row.appendChild(add); row.appendChild(inp); cd.appendChild(row);
      cd.appendChild(el("div", "pw-src", "PDF, Word (.docx), .txt or .md · up to 30 files, 15 MB each"));
      cd.appendChild(el("div", "pw-npriv", NOTES_PRIVACY));
      fillNotes(f);
      scrollTo(cd);
    });
  }
  function noteMeta(r) {
    var kb = r.bytes / 1024, size = kb < 1000 ? Math.max(1, Math.round(kb)) + " KB" : (kb / 1024).toFixed(1) + " MB";
    var what = r.pages ? r.pages + (r.pages === 1 ? " page" : " pages") : r.kind === "docx" ? "Word" : r.kind === "md" ? "Markdown" : "Text";
    return what + " · " + size + " · " + new Date(r.added).toLocaleDateString(undefined, { month: "short", day: "numeric" });
  }
  function fillNotes(f) {
    var box = notesList;
    if (!box) return;
    notes().then(function (N) {
      if (!N) throw new Error("no module");
      return N.list(f.s).then(function (rows) {
        if (box !== notesList) return;
        box.textContent = "";
        if (!rows.length) {
          box.appendChild(el("p", "pw-nempty", "No notes yet. Add your own notes and I'll look in them, along with your guides, when you ask me about " + f.t + "."));
          return;
        }
        rows.forEach(function (r) {
          var row = el("div", "pw-nrow"), nm = el("div", "pw-nname");
          nm.appendChild(el("b", null, r.name)); nm.title = r.name;
          nm.appendChild(el("span", null, noteMeta(r)));
          var del = el("button", "pw-ndel", "Delete"); del.type = "button";
          del.setAttribute("aria-label", "Delete " + r.name);
          del.addEventListener("click", function () {
            del.disabled = true;
            N.remove(r.id).then(function () { noteStatus("Deleted “" + r.name + "”."); },
                                function () { del.disabled = false; noteStatus("I couldn't delete that one. Try again.", true); });
          });
          row.appendChild(nm); row.appendChild(del); box.appendChild(row);
        });
      });
    }).catch(function () {
      if (box !== notesList) return;
      box.textContent = "";
      box.appendChild(el("p", "pw-nempty", "This browser won't let me keep notes (a private window can do that)."));
    });
  }
  function noteStatus(text, bad) {
    if (!notesStat) return;
    notesStat.textContent = text; notesStat.classList.toggle("bad", !!bad);
  }
  function noteError(e, f) {
    var n = "“" + ((e && e.file) || "That file") + "”";
    switch (e && e.code) {
      case "too_big": return n + " is over 15 MB, more than I can hold. Try splitting it into smaller files.";
      case "too_many": return "You've added 30 files for " + f.t + ", which is my limit. Delete one to make room for " + n + ".";
      case "total_full": return "I'm out of room for notes on this device (40 MB of text). Delete some to make room for " + n + ".";
      case "picture": return n + " looks like pictures of text. I can't read pictures of text yet; a PDF or Word file with real text works.";
      case "no_text": return "I couldn't find any text in " + n + ".";
      case "unsupported": return "I can read PDF, Word (.docx), .txt and .md files. Save " + n + " as one of those and try again.";
      case "duplicate": return "You've already added " + n + ".";
      case "password": return n + " is password-protected. Save a copy without the password and try again.";
      case "reader_unavailable": return "I couldn't load my reader for " + n + ". Check your connection and try again.";
      case "quota": return "Your browser is out of space for notes. Delete some notes, or free up space on this device, and try again.";
      case "no_storage": return "This browser won't let me keep notes (a private window can do that).";
      case "busy": return "Close Pip in your other tabs, then try again.";
      case "write_failed": return "I couldn't save " + n + ". Try again.";
      default: return "I couldn't read " + n + ". It may be damaged.";
    }
  }
  function addNotes(f, files) {
    if (!files.length) return;
    var added = [], errs = [];
    notes().then(function (N) {
      if (!N) { noteStatus("I couldn't load my note reader. Check your connection and try again.", true); return; }
      var chain = Promise.resolve();
      files.forEach(function (file) {
        chain = chain.then(function () {
          noteStatus("Reading “" + file.name + "”…");
          return N.add(f.s, file, function (phase, i, n) {
            if (phase === "page") noteStatus("Reading “" + file.name + "”: page " + i + " of " + n + "…");
          }).then(function (meta) { added.push(meta); }, function (e) { errs.push(noteError(e, f)); });
        });
      });
      return chain.then(function () {
        var lines = [];
        if (added.length === 1) lines.push("Added “" + added[0].name + "”. I'll look in it when you ask me about " + f.t + ".");
        else if (added.length) lines.push("Added " + added.length + " files. I'll look in them when you ask me about " + f.t + ".");
        noteStatus(lines.concat(errs).join("\n"), !!errs.length);
        if (added.length) P.react("reviewing", 1);           // a real event: the student just taught Pip something
        scrollDown();
      });
    });
  }
  window.addEventListener("pip:notes", function () {            // added, deleted, or "Delete all" in Settings
    if (notesCard && notesCard.isConnected && notesFor) fillNotes(notesFor);
  });
  // up to k passages from the active exam's notes, ranked with the guide search's own code
  function noteHits(f, text, k) {
    if (!f) return Promise.resolve([]);
    if (P.kind === "quiz" && looksLikeOpenQuestion(text)) return Promise.resolve([]);   // never search for an unanswered question
    return notes().then(function (N) {
      if (!N) return [];
      return N.blocks(f.s).then(function (nb) {
        if (!nb.items.length) return [];
        if (!nb._ix) { nb._texts = nb.items.map(function (x) { return x.text; }); nb._ix = makeIndex(nb._texts); }
        var q2 = expandFor(text, nb._ix);
        return rank(nb._ix, nb._texts, q2, k).map(function (r) { return { s: r[0], it: nb.items[r[1]], q2: q2 }; });
      });
    }).catch(function () { return []; });
  }
  function noteCard(r) {
    var c2 = card(); c2.classList.add("pw-note");
    c2.appendChild(el("h4", null, "From your notes"));
    c2.appendChild(el("div", "pw-src", r.it.name + (r.it.page ? " · p. " + r.it.page : "")));
    c2.appendChild(snippet(r.it.text, r.q2));
    scrollDown();                                  // the note cards come last: show the whole card
  }
  function notePassage(r) {                       // what Claude may see: the lines, never the file name
    return { title: "Student's own notes" + (r.it.page ? ", page " + r.it.page : ""), text: r.it.text, note: true };
  }
  function isPrivate(passages) { return (passages || []).some(function (p) { return p && p.note; }); }

  // ------------------------------------------------------------------ greeting per page
  // Pip works on ONE exam at a time and never pulls questions or passages from another
  // (Jaxon, 2026-10-08): the page's own exam, or on the homepage the next exam unless the
  // student switched to a different one.
  var IX = null, folderOfPage = null, NEXT = null, K_EXAM = "pip:exam";
  function chosen(ix) {
    var s = null; try { s = sessionStorage.getItem(K_EXAM); } catch (e) {}
    for (var i = 0; s && i < ix.folders.length; i++) if (ix.folders[i].s === s) return ix.folders[i];
    return null;
  }
  function context() {
    return index().then(function (ix) {
      IX = ix;
      var f = folderOf(ix); folderOfPage = f ? f.f : null; where.folder = f;
      return Promise.all([nextExam(ix), f ? examDate(f) : null]).then(function (r) {
        var n = r[0]; NEXT = n;
        herePast = !!(r[1] && daysUntil(r[1]) < 0);
        return { ix: ix, here: f, next: n, herePast: herePast, active: f || chosen(ix) || (n && n.folder) || null };
      });
    }).catch(function () { return { ix: null, here: null, next: null, active: null }; });
  }
  function switchExam() {
    context().then(function (c) {
      if (!c.ix) return;
      var upcoming = [], seen = {};
      calendar().then(function (cal) {
        (cal && cal.graded ? cal.graded() : []).filter(function (e) { return e.k === "exam" && daysUntil(e.d) >= 0; })
          .sort(function (a, b) { return a.d < b.d ? -1 : 1; }).forEach(function (ev) {
            var m = String(ev.t).match(/EXAM\s*#?\s*(\d+)/i), want = m ? +m[1] : null;
            c.ix.folders.forEach(function (f) {
              if (!seen[f.s] && f.c === ev.c && (want === null || f.x === null || f.x === want) && f.quizzes.length) { seen[f.s] = 1; upcoming.push([f, ev.d]); }
            });
          });
        var cd = card();
        cd.appendChild(el("h4", null, "Which exam should I focus on?"));
        function row(f, d) {
          var b = el("button", "pw-opt"); b.type = "button";
          b.appendChild(el("span", null, f.t + (d ? " · " + niceDate(d) : "")));
          if (c.active === f) b.classList.add("ok");
          b.addEventListener("click", function () {
            try { sessionStorage.setItem(K_EXAM, f.s); } catch (e) {}
            sub.textContent = f.t; me(f.t); say("Okay, I'll stick to " + f.t + ".");
            chips(examChips(f, false));
            if (notesCard && notesCard.isConnected) renderNotes();     // the notes card follows the exam
          });
          cd.appendChild(b);
        }
        upcoming.forEach(function (u) { row(u[0], u[1]); });
        var rest = c.ix.folders.filter(function (f) { return !seen[f.s] && f.quizzes.length; });
        if (rest.length) cd.appendChild(el("div", "pw-src", "Past exams (only if you want to review):"));
        rest.forEach(function (f) { row(f, null); });
        scrollTo(cd);
      });
    });
  }
  // The student's own saved bits (select text in a study guide, "Add to Pip notes"): kept in this browser and
  // synced like the highlights, under "pipReview:<exam slug>" (theme.js, window.PipReview).
  function reviewCount(f) {
    if (!f) return 0;
    try { return window.PipReview ? window.PipReview.count(f.s) : (jget("pipReview:" + f.s, []) || []).length; } catch (e) { return 0; }
  }
  function reviewChip(f) {
    var n = reviewCount(f);
    return n ? ["Your review guide (" + n + ")", function () { location.href = ROOT + "my-review-guide.html?exam=" + encodeURIComponent(f.s); }] : null;
  }
  function addReviewChip(list, f) {
    var rc = reviewChip(f);
    if (rc && !list.some(function (c) { return c[0].indexOf("Your review guide") === 0; })) list.push(rc);
    return list;
  }
  function openReviewGuide() {
    context().then(function (c) {
      var f = c.active, slugs = [];
      try { slugs = window.PipReview ? window.PipReview.slugs() : []; } catch (e) {}
      if (!reviewCount(f) && slugs.length && c.ix) {              // nothing saved for this exam: open the one that has something
        c.ix.folders.forEach(function (x) { if (!reviewCount(f) && slugs.indexOf(x.s) >= 0) f = x; });
      }
      if (!f) { say("Which exam? Pick one and ask me again."); chips([["Switch exam", function () { switchExam(); }]]); return; }
      var n = reviewCount(f);
      if (!n) {
        say("You haven't added anything for " + f.t + " yet. In a study guide or cram sheet, select a sentence and tap \"Add to Pip\". I'll gather what you save into your own review guide.");
        return;
      }
      say("Opening your review guide for " + f.t + " (" + n + " saved).");
      setTimeout(function () { location.href = ROOT + "my-review-guide.html?exam=" + encodeURIComponent(f.s); }, 450);
    });
  }
  // "Quiz me on these" from the review guide page: the exam's questions whose guide link lands in one of the
  // sections the student saved from. No model writes anything; it is the same drill as every other set.
  function startReviewPractice(spec) {
    context().then(function (c) {
      var f = c.ix && c.ix.folders.filter(function (x) { return x.s === spec.s; })[0];
      if (!f) return say("I couldn't find that exam.");
      Promise.all([bankOf(f), explainOf(f)]).then(function (r) {
        var b = r[0], m = (r[1] && r[1].m) || {};
        function unitOf(d, a) { return m[d + "#" + a] || (d + "#" + a); }
        var want = {};
        (spec.sections || []).forEach(function (x) { if (x.a) want[unitOf(x.d, x.a)] = 1; });
        var pool = notOpen(b.q.filter(function (q) { return q.g && want[unitOf(q.g[0], q.g[1])]; }));
        if (!pool.length) return say("I don't have practice questions linked to those parts of the guide yet. Your saved passages are still the best review.");
        var set = pickFresh(pool, 10);
        say("Here " + (set.length === 1 ? "is 1 question" : "are " + set.length + " questions") + " from the parts of the guide you saved. It's just for you: it doesn't count toward the class stats.");
        count("practice");
        drill("Your review guide", shuffle(set), f);
      }).catch(function () { say("I couldn't load the questions for " + f.t + "."); });
    });
  }
  function examChips(f, onHome) {
    var list = [];
    if (!f) return list;
    list.push(["Practice 10 for " + f.t, function () { startPractice(f, 10); }]);
    if (f.guides && f.guides.length) list.push(["Open the study guide", function () { location.href = pageURL(f.f, f.guides[0]); }]);
    addReviewChip(list, f);
    if (onHome !== false || !where.folder) list.push(["Switch exam", function () { switchExam(); }]);
    return list;
  }
  function examLine(n) {
    if (!n) return "";
    var name = n.folder ? n.folder.t : String(n.ev.t).replace(/\s*\(.*\)\s*$/, "");
    var when = n.days === 0 ? "today" : n.days === 1 ? "tomorrow" : "in " + n.days + " days";
    var s = name + " is " + when + " (" + niceDate(n.ev.d) + ").";
    if (n.folder) { var p = progressFor(n.folder); s += " You've finished " + p.done + " of its " + p.total + " quizzes."; }
    return s;
  }
  function greet(intent) {
    context().then(function (c) {
      if (!c.ix) { say("Hi! My search index for this site isn't built yet, so I can't search or quiz you here."); return; }
      if (intent && intent.rescue) { startRescue(intent.rescue); return; }
      if (intent && intent.review) { startReviewPractice(intent.review); return; }
      var st = quizState(), here = c.here, n = c.next, list = [];
      sub.textContent = here ? here.t : "Your study buddy";
      var ahead = n && n.folder && n.folder !== here ? n.folder : null;
      if (here && c.herePast && !(st.onQuiz && st.current)) {
        say(here.t + " is behind you." + (n ? " " + examLine(n) : "") + (P.kind === "guide" || P.kind === "cram" ? " I can still find things in this guide if you ask." : ""));
        if (ahead) {
          list.push(["Get ahead on " + ahead.t, function () { startPractice(ahead, 10); }]);
          if (ahead.guides && ahead.guides.length) list.push(["Open its study guide", function () { location.href = pageURL(ahead.f, ahead.guides[0]); }]);
        }
        chips(list);
        return;
      }
      if (st.onQuiz && st.results) {
        say("Nice work finishing that! Want to go after what tripped you up?");
        rescueTargets().slice(0, 2).forEach(function (r) {
          list.push(["Rescue: " + shortIO(r.io), function () { startRescue(r); }]);
        });
        if (here) list.push(["Practice 10 from " + here.t, function () { startPractice(here, 10); }]);
        if (missCount()) list.push(["Review all my misses", function () { location.href = ROOT + "review.html"; }]);
      } else if (st.onQuiz && st.current && !st.answered) {
        say("I'll stay out of the way while you answer. Once you lock in an answer and see the feedback, ask me anything until you move on to the next question.");
        // nothing that searches while the quiz is open (it could surface an open question's answer)
      } else if (st.onQuiz && st.current && st.answered) {
        say("Want more on this one?");
        list.push(["Where's this in my guide?", function () { guideForCurrent(); }]);
        list.push(["5 more like this", function () { moreLikeCurrent(); }]);
      } else if (P.kind === "guide" || P.kind === "cram") {
        say("Ask me about anything in this " + (P.kind === "cram" ? "cram sheet" : "guide") + ". I'll explain it in plain words and take you to it.");
        if (here) list.push(["Quiz me on this exam (10)", function () { startPractice(here, 10); }]);
      } else {
        var line = examLine(n);
        say(line ? "Hi! " + line : "Hi! Ask me anything in your study guides, or let me quiz you.");
        if (c.active && (!n || c.active !== n.folder)) say("I'm focused on " + c.active.t + " right now.");
        if (c.active) sub.textContent = c.active.t;
        list = list.concat(examChips(c.active, true));
        var mc = missCount();
        if (mc) list.push(["Review my misses (" + mc + ")", function () { location.href = ROOT + "review.html"; }]);
        var plan = jget("planner:home:v1", null);
        if (plan && plan.day === ymd(new Date()) && plan.planned) list.push(["Today's plan", function () { location.href = ROOT + "calendar.html"; }]);
      }
      if (here && !list.length && !c.herePast) list.push(["Practice 10 from " + here.t, function () { startPractice(here, 10); }]);
      if (!(st.onQuiz && st.current && !st.answered)) addReviewChip(list, here || c.active);
      chips(list);
    });
  }

  // ------------------------------------------------------------------ asking
  function ask(text, quiet) {                    // quiet: the question is already on screen (it waited for the brain)
    if (!quiet) me(text);
    count("pip_ask");
    var t = norm(text).trim();
    if (quizInProgress()) {                       // small talk is fine; anything that searches or quizzes waits
      if (/^(hi|hey|hello|yo|sup|hiya)\b/.test(t)) { say("Hey! I'm here when you finish."); return; }
      if (/^(thanks|thank you|thx|ty)\b/.test(t)) { say("Anytime!"); return; }
      if (/\b(next exam|when is|when's|how long until)\b/.test(t)) {
        context().then(function (c) { say(c.next ? examLine(c.next) : "I don't see an exam coming up on the calendar."); });
        return;
      }
      say(pausedText()); return;
    }
    if (P.kind === "quiz" && looksLikeOpenQuestion(text)) {
      say("That looks like a question you haven't answered yet. Give it your best shot first, then I'll show you where your guide covers it.");
      return;
    }
    if (/^(hi|hey|hello|yo|sup|hiya)\b/.test(t)) { say("Hey! Ask me to explain anything for your exam, or say \"quiz me\"."); return; }
    if (/^(thanks|thank you|thx|ty)\b/.test(t)) { say("Anytime!"); return; }
    // only a bare "help" asks how Pip works; "help me understand X" is a question about X
    if (/^(what can you do|help me|how do you work|help|what do you do)[\s.!?]*$/.test(t)) {
      say("Ask me about anything for your exam and I'll explain it in plain words, then show you where it is in your study guide. I can look in your own notes too (tap Notes to add them), quiz you on an exam (\"quiz me\") or a topic (\"quiz me on beta blockers\"), and tell you when your next exam is. If something still doesn't click, just say so.");
      return;
    }
    if (/\b(next exam|when is|when's|how long until)\b/.test(t)) {
      context().then(function (c) { say(c.next ? examLine(c.next) : "I don't see an exam coming up on the calendar."); });
      return;
    }
    if (/\b(my review guide|review guide|my pip notes|my notes for this exam|my saved (notes|bits|passages)|what (have )?i (saved|added))\b/.test(t)) { openReviewGuide(); return; }
    if (/\b(missed|mistakes|my misses)\b/.test(t)) {
      var n = missCount();
      say(n ? "You have " + n + " missed questions saved from your quizzes." : "No missed questions saved on this device yet.");
      if (n) chips([["Review my misses", function () { location.href = ROOT + "review.html"; }]]);
      return;
    }
    var t2 = t.replace(/[’']/g, "'");
    if (lastAsk && Date.now() - lastAsk.t < 10 * 60000 && (SIMPLER.test(t2) || DEEPER.test(t2))) {
      var la = lastAsk, simp = SIMPLER.test(t2); lastAsk = null; followFrom = la;
      count("followup");
      // "I still don't get it" wants the same idea more simply; "why?" / "tell me more" wants a level deeper
      // After one of Pip's own cards the follow-up is the same request for every student (the card's
      // concept, more simply / one level deeper), so the class-wide answer cache answers it once per card
      // and everyone after that gets it free; a free-form question keeps the student's own words.
      var fq = la.expl ? (simp ? "I still don't get this. Explain it again, more simply: " : "Go one level deeper on this: why and how does it work? ") + la.expl.t
        : la.q + "\nFollow-up from the student: " + text;
      var fp = la.expl ? [{ title: "Pip's plain-language explanation of " + la.expl.t, text: la.expl.x }] : la.passages;
      if (la.expl) fp.link = { folder: la.f.f, file: la.expl.doc, a: la.expl.a };
      maybeClaude(fq, simp ? "simpler" : "deeper", fp, la.f,
                  simp ? "You said it wasn't clicking yet, so I asked Claude to put it more simply." : "You wanted more on that, so I asked Claude to go a level deeper.", true);
      return;
    }
    var m = t.match(/^(?:can you |please )?(?:quiz|test|drill|practice)(?: me)?(?: on| about)?\s*(.*)$/);
    if (m) {
      context().then(function (c) {
        var f = c.active, topic = m[1].trim();
        if (!f) { say("Which exam? Pick one and ask me again."); chips([["Switch exam", function () { switchExam(); }]]); return; }
        if (topic) topicPractice(f, topic); else startPractice(f, 10);
      });
      return;
    }
    searchGuides(text);
  }

  function guideIndex(folder) { return index().then(function () { return getJSON("guide/" + folder.s + ".json"); }); }
  function bankOf(folder) { return index().then(function () { return getJSON("bank/" + folder.s + ".json"); }); }

  function hasGuides(f) { return f.guides.length || f.cram.length; }
  function guideHits(scope, text, here, limit) {      // ranked passages across folders; this page's exam and doc rank a little higher
    var curFile = decodedPath(location.pathname).split("/").pop();
    return Promise.all(scope.map(function (f) {
      return guideIndex(f).then(function (g) {
        prepGuide(g);
        g._ix.ab2 = g.ab;
        var q2 = spell(expandFor(text, g._ix), g._ix);
        if (offGuide(q2, g._ix)) return [];
        // a passage must hold at least one of the question's specific words: "thrush risk factors"
        // must not surface a hearing-loss line just because it says "risk factors"
        var core = uniq(toks(q2)).filter(function (w) { return !GENERIC[w] && g._ix.df[w]; });
        var holds = function (r) { return !core.length || core.some(function (w) { return g._ix.docs[r[1]].tf[w]; }); };
        var found = rank(g._ix, g._texts, q2, 8).filter(holds);
        // a short question may leave a generic word out ("thrush risk factors": the thrush lines)
        if (!found.length && core.length && core.length < uniq(toks(q2)).length) found = rank(g._ix, g._texts, core.join(" "), 8).filter(holds);
        return found.slice(0, 4).map(function (r) {
          var b = g.b[r[1]], boost = (here && f === here ? 1.25 : 1) * (here && f === here && g.docs[b[0]].file === curFile ? 1.5 : 1);
          return { s: r[0] * boost, f: f, g: g, b: b, q2: q2 };
        });
      }).catch(function () { return []; });
    })).then(function (lists) {
      var all = [].concat.apply([], lists).sort(function (a, b) { return b.s - a.s; }), seen = {}, out = [];
      all.forEach(function (r) { var key = r.f.s + "|" + r.b[0] + "|" + r.b[1]; if (!seen[key] && out.length < (limit || 3)) { seen[key] = 1; out.push(r); } });
      return out;
    });
  }
  function searchGuides(text) {
    context().then(function (c) {
      if (!c.ix) return say("My search index for this site isn't built yet.");
      var f = c.active;
      if (!f) {
        say("Which exam should I look in?");
        if (!c.here) chips([["Switch exam", function () { switchExam(); }]]);
        return;
      }
      // Jaxon, 2026-10-15: every question gets an answer in two labelled parts. "From your class": Pip's cards
      // and the guides' passages, from whichever exams of the semester hold the question's words (the active
      // exam leads on a tie), misspellings fixed first. "From general knowledge": Claude, clearly labelled,
      // only when the class materials fall short (they never define the word, or cover only part of the
      // question). Never "not in your guide" as the whole answer.
      var FX = null, D = null, L = null, SCOPE = null, here = c.here || f, text0 = text;
      fixSpelling(text0).then(function (fx) {
        FX = fx; text = fx.text;
        var qx = casual(text);
        D = defineTerm(text); L = listAsk(text);
        examsFor(qx, f).then(function (scope) {
          if (scope.indexOf(f) < 0 && hasGuides(f)) scope = scope.slice(0, 3).concat([f]);   // the active exam is always searched
          SCOPE = scope;
          (L ? gatherList(L, scope, here) : Promise.resolve(null)).then(function (lst) {
            if (lst) return showList(lst);
            // the guides of those exams AND the student's own notes for the active exam (never another exam's),
            // Pip's own plain-language explanation of the concept when he has one, and for "what does X mean"
            // the sentence that defines X
            Promise.all([wideHits(f, scope, qx, c.here, text), noteHits(f, text, 2), explainWide(f, qx, text),
                         D ? findDefinition(D.t, scope.filter(hasGuides), here) : null])
              .then(function (r) { show(r[0], r[1], r[2], r[3]); });
          });
        });
      });
      function show(out, mine, ex, dd) {
        input.placeholder = ASK_HINT;
        // "what does X mean": a card leads only when its title names X; a bare word ("iatrogenic") keeps
        // the usual answer when no guide defines it
        if (D && ex.length && !titleNames(ex[0], D.t) && (!D.bare || (dd && dd.def))) ex = [];
        // a term a guide TEACHES (a heading is about it) gets the usual explanation from its passages; the defining
        // sentence is for words the guides only use ("iatrogenic")
        var defn = D && !ex.length && dd && ((dd.def && dd.def.strong) || (!dd.taught && (dd.def || !D.bare)));
        // a card that holds under half of the question's naming words doesn't answer it
        if (!defn && ex.length && !ex.cmp && fullCover(ex, text, true) < 0.5) ex = [];
        if (!defn && ex.cross) {                        // another exam's answer: only that exam's passages, no notes
          var xf = ex.map(function (x) { return x._f; });
          out = out.filter(function (r) { return xf.indexOf(r.f) >= 0; }); mine = [];
        }
        // Pip's own short answer to THIS question, written with Claude from the candidates the search found (Jaxon,
        // 2026-10-15: "reword and give a short run down to answer the students question"). The usual answer is the
        // fallback (no Claude for this student, out of asks, the helper down). A comparison with a card for each side
        // keeps its side-by-side dissection (Claude writes that one too); a comparison with one card or none gets the
        // short answer (Jaxon, 2026-10-15: "difference between a T and P wave" got one infarct card and no Claude)
        var dissect = !ex.cmp && (ex.length >= 2 || (ex.length && !ex.cross && STAND.test(norm(text))));
        // the usual answer; tried: Claude already had this question with the whole guide, so no second ask
        var classic = function (tried) {
          if (defn) return showDefinition(dd, mine);
          if (!tried && !dissect && (ex.length || out.length || mine.length) && (wantsExplanation(text) || D))
            return askAnswer(text, candidates(out, mine, ex), rest);
          rest();
        };
        // Jaxon, 2026-10-15 ("do whatever to actually make pip useful"): every real question goes to Claude WITH THE
        // WHOLE STUDY GUIDE of the exam it is about, so a wrong pick by the word search can't sink the answer (his
        // "difference between a T and P wave" got an infarct card). Pip's picks go along as candidates and hints.
        if (wantsExplanation(text) || D) return askGuide(text, out, mine, ex, dd, defn, classic);
        classic(false);
        function rest() {
          if (ex.length) return explained(out, mine, ex);
          if (!out.length && !mine.length) {
            count("fallback");
            classHead();
            if (!hasGuides(f) && !out.length) say(f.t + " doesn't have a study guide yet, and I didn't find this in your other guides.");
            else say("I didn't find this in your guides. If I missed it, try other words, like the name of the condition, drug or test.");
            var none = c.here ? [] : [["Switch exam", function () { switchExam(); }]];
            chips(none);
            ownerChips(none, [["Ask Claude (beyond your guide)", function () { askClaude(text, "beyond", [], f, "You asked me to check with Claude."); }]]);
            // a real question only: a lookup ("where is ...", "find ...") wants a place, never Claude
            if (wantsExplanation(text) || D) general(text, [], f, "Your class materials don't cover this, so I asked Claude.");
            return;
          }
          var lead = null;
          if (out.length) {
            classHead();
            whereLine(uniq(out.map(function (r) { return r.f; })));
            lead = say("Your guide's exact words:");
            out.forEach(function (r) {
              var doc = r.g.docs[r.b[0]], c2 = card();
              c2.appendChild(el("h4", null, r.b[2] || doc.title));
              c2.appendChild(el("div", "pw-src", r.f.t + " · " + (doc.kind === "cram" ? "Cram sheet" : "Study guide")));
              c2.appendChild(snippet(r.b[3], r.q2 || text));
              c2.appendChild(linkTo(r.f.f, doc.file, r.b[1], null, r.b[3]));
            });
          }
          if (mine.length) {
            if (!out.length) classHead();
            var nl = out.length ? null : say("I didn't find that in your guides, but your notes mention it:");
            if (!lead) lead = nl;
            mine.forEach(noteCard);
          }
          var guideP = out.map(function (r) { return { title: r.b[2] || "", text: r.b[3] }; });
          var noteP = mine.map(notePassage);
          // what may go to Claude: the guide's passages first, then at most two note passages,
          // within the server's limit of four (a private ask the server never shares)
          var passages = guideP.slice(0, 3).concat(noteP.slice(0, Math.min(2, 4 - Math.min(3, guideP.length))));
          var from = !noteP.length ? "Your guide's passages don't" : !guideP.length ? "Your notes don't" : "Your guide and notes don't";
          var base = [["Quiz me on this", function () { topicPractice(f, text); }]];
          chips(base);
          ownerChips(base, [["Ask Claude to explain", function () { askClaude(text, "explain", passages, f, "You asked me to check with Claude."); }],
                            ["Go deeper with Claude", function () { askClaude(text, "deeper", passages, f, "You asked Claude to go deeper."); }]]);
          // Own words first (Jaxon, 2026-10-11): Pip's summary or Claude's answer goes ABOVE the guide's exact
          // words, with a "Read it in your guide" link under it to the top passage it was built from
          var topLink = out.length ? { folder: out[0].f.f, file: out[0].g.docs[out[0].b[0]].file, a: out[0].b[1] } : null;
          var place = { before: lead, note: null };
          passages.link = topLink; passages.place = place;
          lastAsk = { q: text, passages: passages, f: f, t: Date.now() };
          brainAfter(text, guideP.concat(noteP), lead, !noteP.length ? "your guide" : !guideP.length ? "your notes" : "your guide and notes", topLink).then(function (got) {
            // Pip decides: his own checked summary is enough; otherwise a real question (not a lookup)
            // goes to Claude for a plain-language explanation
            if (got === "summary" || !wantsExplanation(text)) return;
            // no own words yet: say so, and the note goes when Claude's answer lands above the guide's words
            // the passages cover only part of the question: general knowledge fills the gap (one Claude ask, not two)
            if (passCover(out, text) < SHORT_OF) { general(text, passages, f, "Your guide covers only part of this, so I asked Claude."); return; }
            if (lead && lead.parentNode === log) { place.note = el("div", "pw-msg pw-pip", "I can't put this in my own words right now, so here is the exact wording from your guide."); log.insertBefore(place.note, lead); }
            maybeClaude(text, "explain", passages, f, "I asked Claude to explain this in plain words.");
          });
        }
      }
      // Pip has his own checked explanation: it leads, then the single best line from the guide (its
      // exact words), then notes. Claude is not called; "I still don't get it" or "why?" can call him.
      // A question that asks how things differ, compares them or what makes one stand out gets a dissection
      // first (Jaxon, 2026-10-11): see explainedCompare
      function explained(out, mine, ex) {
        if (ex.cmp) return explainedOne(out, mine, ex);
        if (ex.length >= 2) return explainedCompare(out, mine, ex, false);
        if (!STAND.test(norm(text)) || ex.cross) return explainedOne(out, mine, ex);
        // "what makes X stand out": X against the other cards of its own section
        explainOf(f).then(function (e) {
          // look-alikes: other cards of its section whose titles share a specific word with it ("type II" / "type III" / "type IV")
          var mine0 = toks(numbered(ex[0].t)).filter(function (w) { return !GENERIC[w]; });
          var share = function (c) { return toks(numbered(c.t)).filter(function (w) { return mine0.indexOf(w) >= 0; }).length; };
          var sib = e ? e.cards.filter(function (c) { return c.u === ex[0].u && c.id !== ex[0].id && share(c); })
            .sort(function (a, b) { return share(b) - share(a); }).slice(0, 2) : [];
          if (!sib.length) return explainedOne(out, mine, ex);
          var ex2 = [ex[0]].concat(sib); ex2.m = ex.m;
          explainedCompare(out, mine, ex2, true);
        });
      }
      function explainedOne(out, mine, ex) {
        count("explain_card");
        var cf = ex[0]._f || f;                       // the exam this card comes from
        classHead();
        whereLine([cf]);
        var lead = explainBubble(ex[0], f);
        helpful(lead);
        if (ex[1]) explainBubble(ex[1], f);
        // the guide's own line for it, from the section the explanation covers (a top hit elsewhere,
        // such as the objectives list, would only repeat the question back); found once the guide loads
        var slot = el("div", "pw-slot"); log.appendChild(slot);
        guideLine(f, ex[0], ex.m, text).then(function (r) {
          if (!r) { slot.remove(); return; }
          slot.appendChild(el("div", "pw-guidehd", "Your guide's exact words:"));
          var c2 = el("div", "pw-card"); slot.appendChild(c2);
          c2.appendChild(el("h4", null, r.b[2] || r.doc.title));
          c2.appendChild(el("div", "pw-src", cf.t + " · Study guide"));
          c2.appendChild(snippet(r.b[3], ex[0].t + " " + text));
          c2.appendChild(linkTo(cf.f, r.doc.file, r.b[1], null, r.b[3]));
        });
        mine.forEach(noteCard);
        var guideP = out.map(function (r) { return { title: r.b[2] || "", text: r.b[3] }; }), noteP = mine.map(notePassage);
        var passages = guideP.slice(0, 2).concat(noteP.slice(0, 1));
        passages.link = { folder: cf.f, file: ex[0].doc, a: ex[0].a };
        var base = PAST[cf.s] && cf !== f ? [] : [["Quiz me on this", function () { topicPractice(cf, text); }]];
        chips(base);
        ownerChips(base, [["Ask Claude to explain", function () { askClaude(text, "explain", passages, cf, "You asked me to check with Claude."); }],
                          ["Go deeper with Claude", function () { askClaude(text, "deeper", passages, cf, "You asked Claude to go deeper."); }]]);
        lastAsk = { q: text, passages: passages, f: cf, t: Date.now(), expl: ex[0] };
        input.placeholder = "Still fuzzy? Say which part, or ask \u201cwhy?\u201d";
        scrollTo(lead);
        if (fullCover(ex, text) < SHORT_OF && wantsExplanation(text))
          general(text, [{ title: ex[0].t, text: ex[0].x }], cf, "Pip's explanation covers only part of this, so I asked Claude.");
      }
      // the exam whose guide Claude reads: the one whose guides say the most about the question's naming words (Jaxon
      // 2026-10-15: "What is a pulmonary embolism?" read the electrocardiography exam's guide because its best card
      // was "Pulmonary embolism on the ECG"; the Exam 5 guide teaches it). The page's exam keeps it when it says at
      // least 60% as much; a strong defining sentence keeps its own exam; else the best card's, passage's, page's.
      function guideExam(out, ex, dd, defn) {
        if (defn && dd.def && dd.def.strong && hasGuides(dd.def.src.f)) return Promise.resolve(dd.def.src.f);
        var pick = defn && dd.def ? dd.def.src.f : ex.length ? (ex[0]._f || f) : out.length ? out[0].f : (SCOPE || []).filter(hasGuides)[0];
        return examByWords(casual(text), f).then(function (w) {
          if (w && hasGuides(f) && w.f !== f) {
            var fi = IX.folders.indexOf(f);
            return words().then(function (W) {
              var own = Math.min.apply(null, specific(casual(text)).map(function (x) { var i = wordAt(W, x); return i < 0 ? 0 : wordCount(W, i, fi); }));
              return own >= 0.6 * w.n ? f : w.f;
            });
          }
          if (w) return w.f;
          return pick && hasGuides(pick) ? pick : hasGuides(f) ? f : null;
        });
      }
      // Pip's best guide lines in that exam (their numbers in its guide data): a card's section, then the passages found
      function hintsFor(g, gf, out, ex) {
        var hs = [];
        ex.forEach(function (c) {
          if ((c._f || f) !== gf || !c.a) return;
          for (var i = 0; i < g.b.length; i++) if (g.b[i][1] === c.a && g.docs[g.b[i][0]].file === c.doc) { hs.push(i); break; }
        });
        out.forEach(function (r) { if (r.f === gf) { var i = r.g.b.indexOf(r.b); if (i >= 0) hs.push(i); } });
        // then that guide's own best lines for the question: Claude reads a guide Pip's answer may not have come from, and
        // without pointers it missed the Exam 5 lines on pulmonary embolism (inside deep vein thrombosis), 2026-10-15
        prepGuide(g);
        if (g.ab && !g._ix.ab2) g._ix.ab2 = g.ab;
        rank(g._ix, g._texts, expandFor(casual(text), g._ix), 12).forEach(function (r) {
          if (g.docs[g.b[r[1]][0]].kind !== "cram") hs.push(r[1]);
        });
        return uniq(hs).slice(0, 12);
      }
      function askGuide(q, out, mine, ex, dd, defn, fallback) {
        Promise.all([guideExam(out, ex, dd, defn), claudeUsable(q, f)]).then(function (r1) {
          var gf = r1[0], ok = r1[1];
          if (!gf) return fallback(false);
          if (!ok || !claudeRoom("answer")) return fallback(false);
          Promise.all([superbrain(), guideIndex(gf).catch(function () { return null; })]).then(function (r0) {
            var S = r0[0], g = r0[1];
            if (!S) return fallback(false);
            var cands = candidates(out, mine, ex);
            if (defn && dd.def && cands.length < 6) cands.push({ title: dd.def.src.head, text: dd.def.s, f: dd.def.src.f, short: dd.def.src.head,
              link: function () { return linkTo(dd.def.src.f.f, dd.def.src.file, dd.def.src.a, "Read it in your guide: " + dd.def.src.head + " \u2192", dd.def.src.text || ""); },
              full: function (into) { var c2 = el("div", "pw-card"); c2.appendChild(el("h4", null, dd.def.src.head)); c2.appendChild(el("p", "pw-quote", dd.def.s)); into.appendChild(c2); } });
            var ps = cands.map(function (c) { return { title: c.title, text: c.text, note: !!c.note }; });
            var priv = isPrivate(ps), k = cacheKey("guide", q + "|" + cands.map(function (c) { return c.title; }).join("|"), gf, priv), hit = cached(k, priv);
            if (hit) return renderGuide(hit, cands, gf, null, fallback);
            var wait = el("div", "pw-msg pw-pip pw-brain", "Let me read your guide\u2026"); log.appendChild(wait); scrollDown();
            var db = deviceBudget(); db.n++; set(K_CDAY, JSON.stringify(db)); lastClaudeAt = Date.now();
            count("claude_ask");
            var duet = P.duet && P.duet.start();
            S.ask({ question: q, mode: "guide", passages: ps, exam: { title: gf.t, folder: gf.f, slug: gf.s }, hints: g ? hintsFor(g, gf, out, ex) : [], private: priv }).then(function (r) {
              var go = function () {
                wait.remove();
                if (!r.ok) {
                  count(/^(user_|day_|month_)/.test(r.code || "") ? "fallback" : "error");
                  // a helper without guide mode yet, or an exam it has no guide for: the usual answer may still ask Claude
                  return fallback(!/^(bad_mode|bad_exam|bad_hints|unknown_field|no_guide)$/.test(r.code || ""));
                }
                remember(k, r, priv);
                renderGuide(r, cands, gf, r, fallback);
              };
              if (duet) P.duet.finish(!!r.ok, go); else go();
            });
          });
        });
      }
      // Claude's answer in mode "guide": "Used:" names guide lines ([n], sent back by the helper as cites: doc, anchor,
      // heading, text) and Pip's candidates (plain numbers), in its order; lines of one section share one link
      function renderGuide(r, cands, gf, rr, fallback) {
        var a = parseAnswer(r.answer, cands.length), byN = {}, all = [], seen = {};
        (r.cites || []).forEach(function (c) { byN[c.n] = c; });
        (a.refs || []).forEach(function (t) {
          if (t.cand) { var c0 = cands[t.cand - 1]; if (c0 && all.indexOf(c0) < 0) all.push(c0); return; }
          var c = byN[t.line]; if (!c) return;
          var key = c.doc + "#" + c.a;
          if (seen[key]) { seen[key].text += " \u2026 " + c.t; return; }
          all.push(seen[key] = citeCand(c, gf));
        });
        if (a.used === null && !all.length) all = cands.slice(0, 1);
        if (!all.length && !a.general) return fallback(true);
        renderAnswer({ used: all.map(function (x, i) { return i + 1; }), body: a.body, general: a.general }, all, rr, function () { fallback(true); });
      }
      function citeCand(c, gf) {
        var head = c.i || String(c.h || "").split(" \u203a ").pop().split("\u2605")[0].replace(/^[\d.]+\s*\u00b7\s*/, "").replace(/^objectives?\s+[a-z\d&,\s\u2013-]+\s*\u2014\s*/i, "").trim() || gf.t;
        if (head.length > 80) head = head.slice(0, head.lastIndexOf(" ", 77)) + "\u2026";
        var o = { title: c.h, text: c.t, f: gf, short: head };
        o.link = function (long) { return linkTo(gf.f, c.doc, c.a, "Read it in your guide: " + (long ? c.h : head) + " \u2192", c.t); };
        o.full = function (into) {
          var c2 = el("div", "pw-card"); c2.appendChild(el("h4", null, c.h));
          c2.appendChild(el("div", "pw-src", gf.t + " \u00b7 Study guide"));
          c2.appendChild(snippet(o.text, text)); c2.appendChild(linkTo(gf.f, c.doc, c.a, null, c.t)); into.appendChild(c2);
        };
        return o;
      }
      // the search's candidates for Claude to choose from: Pip's cards (the match and the next best), then guide
      // lines, then at most one of the student's own note passages (private: never cached for the class); six at most
      function candidates(out, mine, ex) {
        var cs = [], seen = {};
        ex.concat(ex.alt || []).forEach(function (c) {
          var cf = c._f || f, k = cf.s + "|" + c.id;
          if (seen[k] || cs.length >= 3) return; seen[k] = 1;
          cs.push({ title: c.t, text: c.x, f: cf,
            link: function (long) { return linkTo(cf.f, c.doc, c.a, "Read " + (long ? c.t : shortT(c)) + " in your guide \u2192"); }, short: shortT(c),
            full: function (into) { explainBubble(c, f, into); } });
        });
        out.forEach(function (r) {
          if (cs.length >= 5) return;
          var doc = r.g.docs[r.b[0]], head = (r.b[2] || doc.title) + (r.b[5] ? " \u203a " + r.b[5] : "");
          cs.push({ title: head, text: r.b[3], f: r.f,
            link: function () { return linkTo(r.f.f, doc.file, r.b[1], "Read it in your guide: " + headOf(r.b, r.g) + " \u2192", r.b[3]); },
            full: function (into) {
              var c2 = el("div", "pw-card"); c2.appendChild(el("h4", null, r.b[2] || doc.title));
              c2.appendChild(el("div", "pw-src", r.f.t + " \u00b7 " + (doc.kind === "cram" ? "Cram sheet" : "Study guide")));
              c2.appendChild(snippet(r.b[3], r.q2 || text)); c2.appendChild(linkTo(r.f.f, doc.file, r.b[1], null, r.b[3])); into.appendChild(c2);
            } });
        });
        mine.slice(0, 1).forEach(function (r) {
          var np = notePassage(r);
          cs.push({ title: np.title, text: np.text, note: true, f: f,
            link: function () { return el("span", "pw-src", "From your notes: " + r.it.name); },
            full: function (into) { var c2 = el("div", "pw-card pw-note"); c2.appendChild(el("h4", null, "From your notes"));
                                    c2.appendChild(snippet(r.it.text, r.q2)); into.appendChild(c2); } });
        });
        return cs.slice(0, 6);
      }
      // ask Claude (mode "answer") once the student can use him and has asks left; else the usual answer (fallback)
      function askAnswer(q, cands, fallback) {
        if (!cands.length) return fallback();
        claudeUsable(q, f).then(function (ok) {
          if (!ok || !claudeRoom("answer")) return fallback();
          var ps = cands.map(function (c) { return { title: c.title, text: c.text, note: !!c.note }; });
          var priv = isPrivate(ps), k = cacheKey("answer", q + "|" + cands.map(function (c) { return c.title; }).join("|"), f, priv), hit = cached(k, priv);
          if (hit) return renderAnswer(parseAnswer(hit.answer, cands.length), cands, null, fallback);
          superbrain().then(function (S) {
            if (!S) return fallback();
            var wait = el("div", "pw-msg pw-pip pw-brain", "Let me think about that\u2026"); log.appendChild(wait); scrollDown();
            var db = deviceBudget(); db.n++; set(K_CDAY, JSON.stringify(db)); lastClaudeAt = Date.now();
            count("claude_ask");
            var duet = P.duet && P.duet.start();
            S.ask({ question: q, mode: "answer", passages: ps.map(function (p) { return { title: p.title, text: p.text, note: p.note || undefined }; }),
                    exam: { title: f.t, folder: f.f }, private: priv }).then(function (r) {
              var go = function () {
                wait.remove();
                var a = r.ok ? parseAnswer(r.answer, cands.length) : null;
                if (!a || (!a.body && !a.general)) {
                  if (!r.ok) count(/^(user_|day_|month_)/.test(r.code || "") ? "fallback" : "error");
                  return fallback();
                }
                remember(k, r, priv);
                renderAnswer(a, cands, r, fallback);
              };
              if (duet) P.duet.finish(!!r.ok, go); else go();
            });
          });
        });
      }
      function renderAnswer(a, cands, r, fallback) {
        // "Used: none" with nothing general to say is no answer: the usual one instead
        var used = a.used === null ? [cands[0]] : a.used.map(function (i) { return cands[i - 1]; }).filter(Boolean);
        if (!used.length && !a.general) return fallback();
        count("explain_card");
        var top = classHead(), lead = null;
        if (used.length && a.body) {
          whereLine(uniq(used.map(function (c) { return c.f; })));
          lead = el("div", "pw-msg pw-pip pw-explain pw-answer");
          if (used.some(function (c) { return c.note; })) lead.classList.add("pw-private");
          paras(lead, a.body);
          lead.appendChild(el("span", "pw-lbl", "Pip's answer from your class materials, put into words with Claude. The guide is the source."));
          var links = el("div", "pw-alinks");
          used.forEach(function (c) {                  // two cards with one short name ("Aortic stenosis") get their full titles
            links.appendChild(c.link(c.short && used.filter(function (o) { return o.short === c.short; }).length > 1));
          });
          lead.appendChild(links);
          log.appendChild(lead); helpful(lead);
          var more = el("details", "pw-more");
          more.appendChild(el("summary", null, "Full explanation and your guide's exact words"));
          used.forEach(function (c) { c.full(more); });
          log.appendChild(more);
        } else say("Your guides don't answer this directly.");
        if (a.general) {
          log.appendChild(el("div", "pw-part", "From general knowledge"));
          var g = card(); g.classList.add("pw-claude", "pw-general");
          var head = el("div", "pw-chead"); head.appendChild(el("b", null, "Claude")); head.appendChild(el("span", "pw-badge", "Not from your class materials"));
          g.appendChild(head); paras(g, a.general);
          g.appendChild(el("div", "pw-src", "Claude can make mistakes. For your exam, your guide is the source."));
          if (!lead) helpful(g);
        }
        if (r && typeof r.remainingToday === "number") log.appendChild(el("div", "pw-src pw-left", r.remainingToday + " Claude question" + (r.remainingToday === 1 ? "" : "s") + " left today."));
        var c0 = used.filter(function (c) { return !c.note; })[0];
        lastAsk = { q: text, passages: used.map(function (c) { return { title: c.title, text: c.text, note: c.note }; }), f: c0 ? c0.f : f, t: Date.now() };
        var base = c0 && !(PAST[c0.f.s] && c0.f !== f) ? [["Quiz me on this", function () { topicPractice(c0.f, text); }]] : [];
        chips(base);
        var ps0 = lastAsk.passages.slice(0, 4);
        ownerChips(base, [["Ask Claude to explain", function () { askClaude(text, "explain", ps0, lastAsk.f, "You asked me to check with Claude."); }],
                          ["Go deeper with Claude", function () { askClaude(text, "deeper", ps0, lastAsk.f, "You asked Claude to go deeper."); }]]);
        input.placeholder = "Still fuzzy? Say which part, or ask \u201cwhy?\u201d";
        scrollLead(top);
      }
      // "From your class", with "I read X as Y" when a misspelling was fixed
      function classHead() {
        var h = el("div", "pw-part", "From your class");
        if (FX && FX.fixed.length) h.appendChild(el("span", "pw-fixed", "I read " + FX.fixed.map(function (p) { return "\u201c" + p[0] + "\u201d as \u201c" + p[1] + "\u201d"; }).join(", ")));
        log.appendChild(h); scrollDown();
        return h;
      }
      // "what does X mean": the defining sentence (with its meaning up front when it is a "X (meaning)" gloss),
      // then where else it comes up; general knowledge only when no class sentence really defines it
      function showDefinition(dd, mine) {
        count("explain_card");
        var d = dd.def, term = D.t, top = classHead();
        if (d) {
          whereLine([d.src.f]);
          var m = el("div", "pw-msg pw-pip pw-explain");
          if (d.gloss) m.appendChild(el("p", "pw-deflead", term.charAt(0).toUpperCase() + term.slice(1) + ": " + d.gloss.replace(/[.]$/, "") + "."));
          m.appendChild(el("p", "pw-quote", d.s));
          m.appendChild(el("span", "pw-lbl", (d.src.card ? "Pip's explanation: " : "Your guide: ") + d.src.head));
          m.appendChild(linkTo(d.src.f.f, d.src.file, d.src.a, "Read it in your guide \u2192", d.src.text || ""));
          log.appendChild(m); helpful(m);
        } else say(dd.total ? "I didn't find a line in your guides that says what \u201c" + term + "\u201d means." : "I didn't find \u201c" + term + "\u201d in your guides.");
        if (dd.mentions.length) {
          var box = el("div", "pw-msg pw-pip pw-explain"), ul = el("ul");
          box.appendChild(el("p", null, d ? "It also comes up in:" : "It comes up in:"));
          dd.mentions.forEach(function (x) {
            var li = el("li"); li.appendChild(linkTo(x.f.f, x.file, x.a, x.head + (x.f !== f ? " (" + x.f.t + ")" : ""), x.text)); ul.appendChild(li);
          });
          box.appendChild(ul); log.appendChild(box);
        }
        mine.forEach(noteCard);
        var passages = d ? [{ title: d.src.head, text: d.s }] : dd.mentions.map(function (x) { return { title: x.head, text: x.text }; });
        lastAsk = { q: text, passages: passages, f: f, t: Date.now() };
        chips([]);
        scrollLead(top);
        if (!d || !d.strong) general(D.bare ? "What does \u201c" + term + "\u201d mean?" : text, passages, f,
                                     d ? "Your class materials only hint at what it means, so I asked Claude."
                                       : dd.total ? "Your class materials don't define it, so I asked Claude." : "Your class materials don't mention it, so I asked Claude.");
      }
      // "the X of each Y": one line per item of the section the group names
      function showList(lst) {
        count("explain_card");
        var top = classHead();
        whereLine([lst.f]);
        var m = el("div", "pw-msg pw-pip pw-explain"), ul = el("ul"), N = 15;
        m.appendChild(el("p", null, (L.attr ? "The " + L.attr + " of each, from " : "Each one, from ") + (lst.part ? "\u201c" + lst.part + "\u201d" : "your guide") + ":"));
        lst.items.slice(0, N).forEach(function (it) {
          var li = el("li"); li.appendChild(el("b", null, it.name)); if (it.text) li.appendChild(document.createTextNode(": " + it.text)); ul.appendChild(li);
        });
        m.appendChild(ul);
        if (lst.items.length > N) m.appendChild(el("span", "pw-lbl", "And " + (lst.items.length - N) + " more in your guide."));
        m.appendChild(linkTo(lst.f.f, lst.items[0].file, lst.items[0].a, "Read them in your guide \u2192"));
        log.appendChild(m); helpful(m);
        var passages = [{ title: lst.part || L.group, text: lst.items.slice(0, 12).map(function (it) { return it.name + (it.text ? ": " + it.text : ""); }).join("\n").slice(0, 1200) }];
        lastAsk = { q: text, passages: passages, f: lst.f, t: Date.now() };
        chips(PAST[lst.f.s] && lst.f !== f ? [] : [["Quiz me on this", function () { topicPractice(lst.f, L.group); }]]);
        scrollLead(top);
      }
      // The comparison: the dissection comes FIRST (Claude, else the laptop brain, else the cards' own sentences),
      // then a guide link for each side, then the full cards folded away, then the guide's exact words.
      function explainedCompare(out, mine, ex0, look) {
        count("explain_card");
        var sides = (look ? ex0 : orderSides(ex0, text)).slice(0, 3); sides.m = ex0.m;
        var names = sides.map(shortT);
        classHead();
        whereLine(sides.map(function (c) { return c._f || f; }));
        var links = el("div", "pw-msg pw-pip pw-cmplinks");
        // a side from another exam names that exam, and its link goes to THAT exam's guide
        sides.forEach(function (c) {
          var cf = c._f || f;
          links.appendChild(linkTo(cf.f, c.doc, c.a, "Read " + names[sides.indexOf(c)] + " in your guide →"));
        });
        log.appendChild(links);
        var more = el("details", "pw-more");
        more.appendChild(el("summary", null, "Full explanations: " + names.join(" and ")));
        sides.forEach(function (c) { explainBubble(c, f, more); });
        log.appendChild(more);
        var slot = el("div", "pw-slot"); log.appendChild(slot);
        mine.forEach(noteCard);
        scrollTo(links);
        input.placeholder = "Still fuzzy? Say which part, or ask “why?”";
        Promise.all(sides.map(function (c) { return guideLine(f, c, ex0.m, text); })).then(function (lines) {
          var seen = {}, passages = sides.map(function (c) { return { title: c.t, text: c.x }; });
          lines.forEach(function (r, i) {
            if (!r || seen[r.b[1] + r.b[3]]) return;
            seen[r.b[1] + r.b[3]] = 1;
            if (!slot.firstChild) slot.appendChild(el("div", "pw-guidehd", "Your guide's exact words:"));
            var c2 = el("div", "pw-card"); slot.appendChild(c2);
            c2.appendChild(el("h4", null, r.b[2] || r.doc.title));
            var sf = sides[i]._f || f;
            c2.appendChild(el("div", "pw-src", sf.t + " · Study guide"));
            c2.appendChild(snippet(r.b[3], sides[i].t + " " + text));
            c2.appendChild(linkTo(sf.f, r.doc.file, r.b[1], null, r.b[3]));
            if (passages.length < 4) passages.push({ title: r.b[2] || r.doc.title, text: r.b[3] });
          });
          var f0 = sides[0]._f || f, anyPast = sides.some(function (c) { return PAST[(c._f || f).s]; });
          var base = anyPast ? [] : [["Quiz me on this", function () { topicPractice(f0, text); }]];
          chips(base);
          lastAsk = { q: text, passages: passages, f: f0, t: Date.now(), expl: sides[0] };
          var noModel = function () { var t = cmpTable(sides, look); log.insertBefore(t, links); helpful(t); scrollTo(t); };
          var viaBrain = function () {
            var qb = text.slice(0, 300) + (look ? " Say what sets the first one apart from the others, in a few short sentences." : " Say how they differ, in a few short sentences.");
            brainAfter(qb, passages, links, "your guide", null).then(function (got) { if (got !== "summary") noModel(); });
          };
          // Claude only for a student who can already use him, inside the usual limits; anything else falls through
          var qc = text.slice(0, 270) + CMP_ASK;
          claudeUsable(qc, f0).then(function (ok) {
            if (!ok) return viaBrain();
            var priv = false, k = cacheKey("explain", qc, f0, priv), hit = cached(k, priv);
            passages.place = { before: links, note: null }; passages.onFail = viaBrain;
            if (hit) { claudeCard({ answer: hit.answer }, hit.mode, passages, "I asked Claude to compare them. (I'd asked before.)"); return; }
            if (!claudeRoom()) return viaBrain();
            askClaude(qc, "explain", passages, f0, "I asked Claude to compare them side by side.", k);
          });
        });
      }
    });
  }

  // ------------------------------------------------------------------ comparisons: a dissection, not a stack of cards
  // Jaxon, 2026-10-11: "Can we have PIP give a nuanced dissection when asked how things differ, or compare,
  // or what makes something stand out". For "primary vs secondary hypertension" Pip used to stack his two
  // cards. Now the dissection leads: a short lead line, a side-by-side of only the rows the sources say
  // something about, and one "Quick way to tell them apart" line, then a guide link for each side, then
  // the full cards (folded away) and the guide's exact words. Source, in order: Claude (invited students,
  // the usual limits and answer cache), Pip's laptop brain (the usual word guard), else NO model: the
  // cards' own sentences, sorted into rows by cue words, never a fact that is not in a card.
  var STAND = /\b(stand(s)? out|unique|special|sets? (it|them|this|that) apart|what makes .{1,60}\bdifferent)\b/;
  var CMP_ASK = "\nCompare them side by side in short plain lines, one per row (what it is, cause, how common, who gets it, clues, tests, treatment; " +
    "only rows the passages cover), then a last line starting \"Quick way to tell them apart:\". No tables.";
  var CMP_ROWS = [
    ["What it is", null, 1],
    ["Cause or mechanism", /\b(causes?|caused|due to|mechanisms?|driven|susceptibility|arises?|results? from|comes? from)\b/, 1],
    ["How common", /\d\s*%|\bpercent\b|\b(prevalence|makes? up|most common|uncommon|rare)\b/, 1],
    ["Who gets it", /\b(risk factors?|family history|older adults|advancing age|inherit\w*)\b/, 1],
    ["Telling clues", /\b(go looking|look for|clues?|suspect\w*|signs?|symptoms?|features?|onset|resistant|unexplained)\b/, 2],
    ["Workup", /\b(tests?|testing|imaging|screen\w*|work-?up|diagnos\w*|biops\w*|labs?)\b/, 1],
    ["Treatment", /\b(treat\w*|therapy|drugs?|medications?|surgery|surgical|first-line|manag\w*)\b/, 1],
    ["How it stands apart", /\b(unlike|whereas|while|in contrast|rather than|versus|vs|instead|but)\b/, 1]];
  function shortT(c) { return String(c.t).split(":")[0].trim(); }
  function cmpSentences(x) {                       // one card's text as sentences (bullets and blank lines dropped)
    var out = [];
    String(x).split(/\n+/).forEach(function (line) {
      line = line.replace(/^[-•]\s+/, "").trim();
      if (line) line.replace(/([.!?])\s+(?=[A-Z0-9(])/g, "$1\u0001").split("\u0001").forEach(function (t) { if (t.trim()) out.push(t.trim()); });
    });
    return out;
  }
  // the question's order decides the sides' order ("primary vs secondary" puts primary first)
  function orderSides(ex, text) {
    var n = " " + norm(text).replace(/[^a-z0-9]+/g, " ") + " ";
    var words = ex.map(function (c) { return norm(c.t).split(/[^a-z0-9]+/).filter(function (w) { return w.length >= 4; }); });
    var pos = ex.map(function (c, i) {
      var best = 1e9;
      words[i].forEach(function (w) {
        var elsewhere = words.some(function (o, j) { return j !== i && o.indexOf(w) >= 0; });
        var at = elsewhere ? -1 : n.indexOf(" " + w.slice(0, 5));
        if (at >= 0 && at < best) best = at;
      });
      return best;
    });
    var idx = ex.map(function (c, i) { return i; }).sort(function (a, b) { return pos[a] - pos[b] || a - b; });
    var out = idx.map(function (i) { return ex[i]; }); out.m = ex.m;
    return out;
  }
  // Rows from the cards' own sentences, with no model. Each sentence is used once, in the first row whose cue it
  // holds; the "quick way to tell" block of a card is the bottom line. Returns {rows: [[label, [cell...]]], bottom}.
  function cmpFromCards(sides) {
    var bottom = "", rowsBy = {};
    var per = sides.map(function (c) {
      var ss = cmpSentences(c.x), qi = -1;
      ss.forEach(function (t, i) { if (qi < 0 && /quick way to (tell|tell them|distinguish)/i.test(t)) qi = i; });
      if (qi >= 0 && !bottom) {
        bottom = ss.slice(qi).join(" ").replace(/^[^:]*quick way to[^:]*:\s*/i, "");
        bottom = bottom.charAt(0).toUpperCase() + bottom.slice(1);
      }
      return qi >= 0 ? ss.slice(0, qi) : ss;
    });
    per.forEach(function (ss, si) {
      ss.forEach(function (t, i) {
        var ri = i === 0 ? 0 : -1;
        for (var r = 1; ri < 0 && r < CMP_ROWS.length; r++) if (CMP_ROWS[r][1].test(t)) ri = r;
        if (ri < 0) return;
        var cell = rowsBy[ri] = rowsBy[ri] || [];
        var mine = cell[si] = cell[si] || [];
        if (mine.length < CMP_ROWS[ri][2]) mine.push(t);
      });
    });
    var rows = [];
    CMP_ROWS.forEach(function (r, ri) {
      var cell = rowsBy[ri];
      if (!cell) return;
      rows.push([r[0], sides.map(function (c, si) { return cell[si] ? cell[si].join(" ") : ""; })]);
    });
    return { rows: rows, bottom: bottom };
  }
  // Jaxon, 2026-10-11: "At the top just say this was discussed in this guide." EVERY answer from a guide starts with
  // this one plain line (a comparison whose sides come from two exams names both)
  function whereLine(exams) {
    var seen = {}, t = [];
    exams.forEach(function (x) { if (x && !seen[x.s]) { seen[x.s] = 1; t.push(x.t); } });
    if (!t.length) return null;
    var names = t.length > 2 ? t.slice(0, -1).join(", ") + " and " + t[t.length - 1] : t.join(" and ");
    return say("This was discussed in your " + names + (t.length > 1 ? " guides." : " guide."));
  }
  function cmpTable(sides, look) {
    var d = cmpFromCards(sides), n = sides.length, box = el("div", "pw-msg pw-pip pw-cmp");
    var names = sides.map(shortT);
    box.appendChild(el("p", "pw-cmplead", look
      ? "Here is what sets " + names[0] + " apart from the other topics in its section, using only what your guide says about each:"
      : "Here is how " + names.slice(0, -1).join(", ") + " and " + names[n - 1] + " differ, using only what your guide says about each:"));
    if (!d.rows.length) {                          // cards with nothing to line up: say so rather than guess
      box.appendChild(el("p", null, "Your guide's cards below say more about each one."));
      return box;
    }
    var grid = el("div", "pw-cmpgrid" + (n > 2 ? " pw-cmp1" : ""));
    if (n === 2) names.forEach(function (nm) { grid.appendChild(el("b", "pw-cmphd", nm)); });
    d.rows.forEach(function (r) {
      grid.appendChild(el("div", "pw-cmprow", r[0]));
      r[1].forEach(function (t, i) {
        var cell = el("div", "pw-cmpcell" + (t ? "" : " pw-cmpnone"));
        if (n > 2) cell.appendChild(el("b", null, names[i] + ": "));
        cell.appendChild(document.createTextNode(t || "Not covered here"));
        grid.appendChild(cell);
      });
    });
    box.appendChild(grid);
    if (d.bottom) {
      var q = el("p", "pw-cmpbottom"); q.appendChild(el("b", null, "Quick way to tell them apart: ")); q.appendChild(document.createTextNode(d.bottom));
      box.appendChild(q);
    }
    return box;
  }

  // ------------------------------------------------------------------ Pip explains: his own checked explanations
  // Jaxon, 2026-10-09: "I want him to not just give the guides when someone asks for help I want him to
  // explain the concept questioned in easier to understand language. There doesnt need to be a word
  // limit but dont make it a whole page for each explanation." Each upcoming exam has cards written
  // from its own study guide and independently fact-checked (pip/explain/, tools/pip_explain.py): one
  // concept each, in plain words, linked to its section. Free, instant, and the same on every device.
  var ROMAN = { "1": "i", "2": "ii", "3": "iii", "4": "iv", "5": "v" };
  function numbered(s) {          // "type 3" and "type III" both become the one word "typeiii" (digits alone don't index)
    return String(s).replace(/\b(type|class|grade|stage|phase|degree|group|schedule|mobitz)\s+(iv|v|i{1,3}|[1-5])\b/gi, function (m, w, n) {
      return m + " " + w.toLowerCase() + (ROMAN[n] || n.toLowerCase());
    });
  }
  function explainOf(f) {
    if (!f || !f.ex) return Promise.resolve(null);
    return getJSON("explain/" + f.s + ".json").then(function (e) {
      e.cards.forEach(function (c) { c._f = f; c._m = e.m; });         // each card knows its own exam and anchor map
      if (!e._ix) {
        e._texts = e.cards.map(function (c) { return numbered([c.t, c.t, c.k.join(" ; "), c.q.join(" ; ")].join(" ; ")); });
        e._ix = makeIndex(e._texts, e.cards.map(function (c) { return numbered(c.x); }));
        e._names = e.cards.map(function (c) { var o = {}; toks(numbered(c.t + " " + c.k.join(" "))).forEach(function (w) { o[w] = 1; }); return o; });
        e._title = e.cards.map(function (c) { var o = {}; toks(numbered(c.t)).forEach(function (w) { o[w] = 1; }); return o; });
        e._kind = e.cards.map(function (c) { return kinds(c.t); });
      }
      e.cards.forEach(function (c) { c._ix = e._ix; });                // and its exam's card index (fullCover)
      return e;
    }).catch(function () { return null; });
  }
  var GENERIC = {};
  toks("risk risks factor factors cause causes sign signs symptom symptoms treatment treat treating treated management manage managing " +
       "diagnosis diagnose diagnosing diagnosed test tests " +
       "type types feature features common normal side effect effects finding findings exam examination patient patients when " +
       "first best most use used uses change changes").forEach(function (w) { GENERIC[w] = 1; });
  // what KIND of answer a question wants, and what kind each card is (read from its title): among cards
  // about the same thing, "first line med for HCM" wants the drugs card, "what does takotsubo mean" the
  // what-it-is card, "PAC vs PVC" the side-by-side card, "how do i remember weber" the memory-aid card
  var WANTS = [["compare", /\b(vs|versus|difference|differences|differ|compare|compared|distinguish|tell apart|tell\b.{1,60}\bfrom|apart)\b/],
    ["remember", /\b(remember|memori[sz]e|mnemonic|trick|keep mixing|mixing (it|them) up|mix (it|them) up)\b/],
    ["treat", /\b(treat|treats|treated|treating|treatment|first[- ]line|drugs?|meds?|medications?|manage|management|therapy|antibiotics?|prescribe)\b/],
    ["diagnose", /\b(diagnos\w*|tests?|testing|work ?up|labs?|imaging|criteria|cutoffs?|cut off|score)\b/],
    ["why", /\b(why|how come|how does|how do(es)? \w+ (work|cause|happen|lead)|mechanism|pathophysiology)\b/],
    ["define", /^(what(s|'s| is| are| does| do)|define|definition|meaning of)\b|\bwhat does .* mean\b|\bmean(s)?\b/]];
  var KIND = { compare: /\b(vs|versus|compared|comparing|apart|differences?|telling)\b/, remember: /\b(remember|remembering|memory|mnemonic|trick)\b/,
    treat: /\b(treat\w*|management|managing|drugs?|therapy|medications?|antibiotics?|reversal)\b/,
    diagnose: /\b(diagnos\w*|tests?|testing|work-?up|imaging|criteria|score|reading|laboratory)\b/,
    why: /\b(why|how|mechanism|works|happens|develops)\b/, define: /\b(what it is|what they are|definition|defined)\b/ };
  function wants(text) { var n = norm(text).replace(/[’']/g, "'"), o = {}; WANTS.forEach(function (w) { if (w[1].test(n)) o[w[0]] = 1; }); return o; }
  function kinds(title) { var n = norm(title), o = {}; for (var k in KIND) if (KIND[k].test(n)) o[k] = 1; return o; }
  var COMPARE = /\b(difference|differences|different|differ|differs|distinguish|versus|vs|compare|compared|comparing|comparison|contrast|contrasts|contrasting|tell apart|tell the difference|similar|similarities|similarity|alike)\b|\btell\b.{1,60}\bfrom\b/;
  // the card that answers this question: it must match most of the question's words (rank() asks for
  // 60%) AND be about something the question names (a word of its title or other names), so a passing
  // mention in some other card's text never answers for it. A comparison may bring a second card.
  // lite: another exam's cards, searched with ITS OWN abbreviations (pip/data/ab.json) and without loading its guide
  function explainHits(f, text, lite) {
    return Promise.all([explainOf(f), lite ? null : guideIndex(f).catch(function () { return null; }), lite ? abAll() : null]).then(function (r0) {
      var e = r0[0], g = r0[1];
      if (!e || !e.cards.length) return [];
      if (g && g.ab) e._ix.ab2 = g.ab; else if (r0[2] && r0[2][f.s]) e._ix.ab2 = r0[2][f.s];
      if (g) prepGuide(g);
      var ab = abFor(e._ix);
      var expandAb = function (s) { return numbered(String(s).replace(/\b[A-Za-z][A-Za-z0-9]{1,7}\b/g, function (w) { var x = ab[w.toLowerCase()]; return !x ? w : e._ix.df[stem(w.toLowerCase())] ? w + " " + x : x; })); };
      var q = spell(expandAb(text), e._ix);
      // a comparison's sides ("PVC vs SVT"): a side-by-side card earns its bonus only when it names every side
      // (Jaxon's PVC vs SVT on the electrocardiography exam led with "Sinus tachycardia versus supraventricular tachycardia")
      var sd = COMPARE.test(norm(text)) ? sidesOf(text) : null;
      var sideT = sd && sd.map(function (x) { return uniq(toks(spell(expandAb(casual(x)), e._ix))).filter(function (w) { return !GENERIC[w]; }); });
      // a word every side holds ("wave" in "T wave vs P wave") tells neither side apart
      if (sideT) { var shared = sideT[0].filter(function (w) { return sideT.every(function (st) { return st.indexOf(w) >= 0; }); });
        if (shared.length && sideT.every(function (st) { return st.length > shared.length; })) sideT = sideT.map(function (st) { return st.filter(function (w) { return shared.indexOf(w) < 0; }); }); }
      if (g && g._ix && offGuide(spell(q, g._ix), g._ix)) return [];
      var qt = uniq(toks(q));
      // generic words ("risk factors", "signs", "treatment") never name a concept on their own: "thrush risk
      // factors" must not pull in a hearing-loss card whose other names say "risk factors"
      var named = function (i) { return qt.some(function (w) { return e._names[i][w] && !GENERIC[w]; }); };
      // a card whose TITLE holds the question's words is about that thing; one that only mentions them is not
      var idf = function (w) { var df = e._ix.df[w] || 0; return Math.log(1 + (e._ix.N - df + 0.5) / (df + 0.5)); };
      var cands = rank(e._ix, e._texts, q, 14).filter(function (r) { return named(r[1]); });
      // a card about one side holds only that side's words, so a two-sided question never ranks it: each side is
      // searched on its own too ("PVC vs SVT" found no premature ventricular complex card)
      if (sideT) sideT.forEach(function (st) {
        if (st.length) rank(e._ix, e._texts, st.join(" "), 6).forEach(function (r) {
          if (named(r[1]) && !cands.some(function (c) { return c[1] === r[1]; })) cands.push(r);
        });
      });
      // "mastoiditis signs": every word is needed for a short question, but a generic one may be left out
      if (!cands.length) { var core = qt.filter(function (w) { return !GENERIC[w]; }); if (core.length && core.length < qt.length) cands = rank(e._ix, e._texts, core.join(" "), 14).filter(function (r) { return named(r[1]); }); }
      var want = wants(text), asks = Object.keys(want).length, bare = !asks && qt.length <= 3;
      var exact = norm(text).replace(/[’]/g, "'").replace(/[?!.\s]+$/, "")          // "what is a P wave" -> "p wave"
        .replace(/^(?:what(?:'s|s| is| are| does| do)|define|explain|describe|tell me about)\s+(?:an? |the )?/, "").replace(/\s+(?:mean|means)$/, "").trim();
      var hits = cands.map(function (r) {
        var tt = e._title[r[1]], bonus = 0, kd = e._kind[r[1]], cd = e.cards[r[1]];
        // the question IS one of the card's names ("t wave" is the J point, ST segment and T wave card's other name)
        if (norm(cd.t) === exact || cd.k.some(function (k) { return norm(k) === exact; })) bonus += 3;
        qt.forEach(function (w) { if (tt[w]) bonus += idf(w) * 1.3; else if (e._names[r[1]][w]) bonus += idf(w) * 0.3; });
        for (var k in want) if (kd[k]) {
          if (k === "compare" && sideT && !sideT.every(function (st) {       // half or more of each side's words
            return st.filter(function (w) { return e._names[r[1]][w]; }).length * 2 >= st.length && st.length; })) continue;
          bonus += k === "compare" ? 4 : 2.5;
        }
        // a bare topic ("varicose veins") or "what is X" wants the card that says what it is, not its
        // treatment, tests or comparison with something else
        if ((bare || (want.define && asks === 1)) && (kd.treat || kd.diagnose || kd.compare)) bonus -= 2;
        return [r[0] + bonus, r[1]];
      }).sort(function (a, b) { return b[0] - a[0]; });
      // "PAC vs PVC": a side-by-side card that names two of the question's terms answers it better than
      // the card for either side alone
      if (want.compare) {
        for (var ci = 0; ci < hits.length; ci++) {
          var i2 = hits[ci][1], tf2 = e._ix.docs[i2].tf, core2 = qt.filter(function (w) { return !GENERIC[w] && e._ix.df[w]; });
          var both = core2.filter(function (w) { return e._names[i2][w]; }).length;
          // it must hold EVERY specific word of the question ("primary vs secondary prevention" is not the
          // primary-versus-secondary-research card), and name at least two of them
          var miss = core2.filter(function (w) { return !tf2[w]; }).length;
          if (e._kind[i2].compare && both >= 2 && miss <= (sideT && core2.length >= 4 ? 1 : 0) &&
              (!sideT || sideT.every(function (st) { return st.some(function (w) { return e._names[i2][w]; }); }))) { if (ci) hits.unshift(hits.splice(ci, 1)[0]); hits.cmp = 1; break; }
        }
      }
      // no single card compares them: each side's best card leads, in the question's order
      if (sideT && !hits.cmp && hits.length > 1) {
        var isSide = function (c, si) { var x = norm(sd[si]); return norm(c.t) === x || c.k.some(function (k) { return norm(k) === x; }); };
        var sideOf = function (st, si) {
          var i;
          for (i = 0; i < hits.length; i++) if (isSide(e.cards[hits[i][1]], si)) return hits[i];        // the side is one of its names
          for (i = 0; i < hits.length; i++) if (titleNames(e.cards[hits[i][1]], sd[si])) return hits[i];   // then a card ABOUT that side
          for (i = 0; i < hits.length; i++) if (st.length && st.filter(function (w) { return e._names[hits[i][1]][w]; }).length * 2 >= st.length) return hits[i];
          return null;
        };
        // one of the best cards has every side in its title ("Weber and Rinne patterns"): it leads alone
        var half = function (h, st) { return st.length && st.filter(function (w) { return e._title[h[1]][w]; }).length * 2 >= st.length; };
        var whole = hits.slice(0, 3).filter(function (h) { return sideT.every(function (st) { return half(h, st); }); })[0];
        var picks = whole ? [] : sideT.map(sideOf);
        if (whole) hits = [whole].concat(hits.filter(function (h) { return h !== whole; }));
        else if (picks.length >= 2 && picks.every(Boolean) && picks[0][1] !== picks[1][1]) hits = picks.slice(0, 2).concat(hits.filter(function (h) { return picks.indexOf(h) < 0; }));
      }
      if (!hits.length) {
        // no card names it, but one holds every word of a two-or-more-word question ("gonorrhoeae vs meningitidis")
        var all = rank(e._ix, e._texts, q, 1).filter(function (r) { return qt.length >= 2 && qt.every(function (w) { return e._ix.docs[r[1]].tf[w]; }); });
        if (all.length) hits = all;
      }
      if (!hits.length) return [];
      var out = [e.cards[hits[0][1]]];
      out.m = e.m;                                // anchor -> section, to pick the guide line from the same section
      out.cmp = hits.cmp ? 1 : 0;                  // a side-by-side card already answers it
      out.sc = hits[0][0];
      if ((COMPARE.test(norm(text)) || /\b[a-z]{3,} or [a-z]{3,}\b/.test(norm(text))) && !hits.cmp) {
        var first = e._names[hits[0][1]];
        for (var i = 1; i < hits.length; i++) {
          // a different concept, named by a question word the first card's names don't have
          var own = qt.filter(function (w) { return e._names[hits[i][1]][w] && !first[w]; });
          if (own.length && hits[i][0] >= hits[0][0] * 0.4) { out.push(e.cards[hits[i][1]]); break; }
        }
      }
      out.cov = coverOf(e, out, text, ab);
      // the next best cards about something the question names: candidates for Claude's short answer to choose from
      out.alt = hits.slice(1, 5).map(function (h) { return e.cards[h[1]]; }).filter(function (c) { return out.indexOf(c) < 0; }).slice(0, 2);
      return out;
    }).catch(function () { return []; });
  }
  // ------------------------------------------------------------------ one question, every exam of the semester
  // Jaxon, 2026-10-11: "PVC vs SVT" on the Clinical Medicine and Surgery I Exam 4 guide got one card that only
  // lists them, because Pip searched only that exam; the real cards are in Principles of Diagnostic Medicine I
  // Exam 3. The page's own exam (or the active one) still wins when its best card really covers the question
  // (the question's specific words are in the card's title, other names or lead); otherwise a clearly stronger
  // card from another exam of the semester wins, a current or upcoming exam before a past one. Each exam is
  // searched with its own abbreviations; another exam's guide loads only for the answer that comes from it.
  var COVER = 0.75, abP = null;
  function abAll() {                              // slug -> that exam's own abbreviations (small; loaded on first need)
    if (!abP) abP = index().then(function () { return getJSON("ab.json"); }).catch(function () { return {}; });
    return abP;
  }
  var CMPW = {};
  ("vs versus difference differences differ differs different differently compare compared comparing comparison contrast " +
   "distinguish apart similar similarity similarities alike between tell").split(" ").forEach(function (w) { CMPW[w] = 1; });
  // the share of the question's specific words (an abbreviation counts through its long form) that the best
  // cards' title, other names or first sentence hold
  function coverOf(e, cards, text, ab) {
    var have = {};
    cards.slice(0, 2).forEach(function (c) {
      var lead = String(c.x).split(/\n/)[0].split(/[.!?]\s/)[0];
      toks(numbered(c.t + " " + c.k.join(" ") + " " + lead)).forEach(function (w) { have[w] = 1; });
    });
    var n = 0, ok = 0, seen = {};
    letterTerms(norm(numbered(String(text)))).replace(/[A-Za-z][A-Za-z0-9]*/g, function (w) {
      var lw = w.toLowerCase(), t = toks(lw)[0];
      if (!t || CMPW[lw] || GENERIC[t] || seen[t]) return w;
      seen[t] = 1; n++;
      var long = ab[lw], sp = toks(spell(lw, e._ix));
      if (have[t] || sp.some(function (x) { return have[x]; }) || (long && toks(long).length && toks(long).every(function (x) { return have[x]; }))) ok++;
      return w;
    });
    return n ? ok / n : 0;
  }
  // "PVC vs SVT", "difference between X and Y", "how do X and Y differ" -> ["pvc", "svt"]; null if it has no clear sides
  function sidesOf(text) {
    var n = norm(text).replace(/[’]/g, "'").replace(/[?!.]+\s*$/, "").trim();
    n = n.replace(/\b(differ|differs|different|differently|compare|compared|alike|similar|apart)\b.*$/, "")
      .replace(/^(?:(?:what(?:'s|s| is| are)?|how (?:do|does|can|is|are)|can you|please|tell me|i|you|we)\s+)*(?:the )?(?:difference|differences|diff|similarit(?:y|ies)|comparison)\s+(?:between|of|in)\s+/, "")
      .replace(/^(?:(?:how (?:do|can) (?:i|you|we) )?tell|compare|contrast|distinguish|differentiate)\s+/, "")
      .replace(/^(?:how (?:do|does|are|is)\s+)/, "").trim();
    var parts = n.split(/\b(?:vs|versus)\b/.test(n) ? /\s+(?:vs\.?|versus)\s+/ : /\s+(?:vs\.?|versus|and|or|from|with|against)\s+/).map(function (x) { return x.replace(/^(?:a|an|the|between)\s+/, "").trim(); }).filter(Boolean);
    if (parts.length < 2 || parts.length > 3) return null;
    // one noun shared by every side: "T and P wave" is the T wave and the P wave, "aortic and mitral stenosis" is
    // aortic stenosis and mitral stenosis (a lone side that only modifies: a letter, -ic/-al/-ar/-ous/-ive, left/right ...)
    var MOD = /^(?:[a-z]|[a-z]+(?:ic|al|ar|ary|ous|ive|ile)|primary|secondary|tertiary|first|second|third|left|right|upper|lower|acute|chronic|early|late)$/;
    var last = parts[parts.length - 1].split(/\s+/);
    if (last.length >= 2 && MOD.test(last[0]) && parts.slice(0, -1).every(function (x) { return MOD.test(x); }))
      parts = parts.slice(0, -1).map(function (x) { return x + " " + last.slice(1).join(" "); }).concat([parts[parts.length - 1]]);
    for (var i = 0; i < parts.length; i++) if (parts[i].length > 60 || !toks(parts[i]).length) return null;
    return parts;
  }
  // the best exam for this wording: home if it really covers, else a clearly stronger exam (past or upcoming alike)
  // about: one side of a comparison ("t wave"): a card whose title or other name IS that side wins over a card that only
  // mentions it (the infarction exam's ST-elevation card lists "hyperacute T waves"), the page's exam first
  function pickBest(f, text, others, about) {
    return Promise.all([f].concat(others).map(function (x) {
      return Promise.all([explainHits(x, text, x !== f), examDate(x)]).then(function (r) {
        PAST[x.s] = !!(r[1] && daysUntil(r[1]) < 0);
        return { f: x, h: r[0], cov: r[0].length ? (r[0].cov || 0) : 0, past: PAST[x.s] };
      });
    })).then(function (rs) {
      var home = rs[0];
      if (about) {
        var named = rs.filter(function (r) { return r.h.length && titleNames(r.h[0], about); });
        if (named.length) return named.indexOf(home) >= 0 ? home : named.sort(function (a, b) { return b.cov - a.cov || (b.h.sc || 0) - (a.h.sc || 0); })[0];
      }
      if (home.cov >= COVER) return home;
      var ok = rs.slice(1).filter(function (r) { return r.cov >= COVER && r.cov >= home.cov + 0.2; });
      ok.sort(function (a, b) { return b.cov - a.cov || (b.h.sc || 0) - (a.h.sc || 0); });   // any exam, past or upcoming: best match
      return ok[0] || null;
    });
  }
  function explainWide(f, qx, text) {
    return explainHits(f, qx).then(function (home) {
      if (!IX || (home.length && home.cov >= COVER)) return home;
      var others = IX.folders.filter(function (x) { return x !== f && x.ex && x.sem === f.sem; });
      if (!others.length) return home;
      var sides = COMPARE.test(norm(text)) ? sidesOf(text) : null;
      return Promise.all([pickBest(f, qx, others),
        sides ? Promise.all(sides.map(function (sd) { return pickBest(f, casual(sd), others, sd); })) : null]).then(function (r) {
        var rs = r[1];
        // each side found on its own (maybe in different exams): one card per side, at least one from another exam
        if (rs && rs.every(function (x) { return x && x.h.length; })) {
          var cards = [], seen = {};
          rs.forEach(function (x) { var c = x.h[0], k = c._f.s + "|" + c.id; if (!seen[k]) { seen[k] = 1; cards.push(c); } });
          if (cards.length >= 2 && cards.some(function (c) { return c._f !== f; })) {
            cards.m = cards[0]._m; cards.cmp = 0; cards.cross = 1; cards.cov = 1;
            return cards;
          }
        }
        var w = r[0];
        if (w && w.f !== f && w.h.length) { var o = w.h.slice(); o.m = w.h.m; o.cmp = w.h.cmp; o.cross = 1; o.cov = w.cov; o.alt = w.h.alt; return o; }
        return home;
      });
    }).catch(function () { return []; });
  }
  // ------------------------------------------------------------------ every word of every exam (pip/data/words.json)
  // Jaxon, 2026-10-15: "junctional rythm?" found nothing, because a misspelled word under 6 letters was never
  // corrected. words.json lists every word the guides and cards use, commonest first, with a bit per exam
  // (index.json folder order). A word some guide uses is never "corrected" (so no exam's word is turned into
  // another's); an unknown word becomes the commonest completion of a cut-off word, else the commonest known
  // word one edit away (two for 9+ letters) with the same first letter. The bits send a question to the
  // exams that hold its words.
  var wordsP = null;
  function words() {
    if (!wordsP) wordsP = index().then(function () { return getJSON("words.json"); }).then(function (d) {
      var w = d.w.split(" "), at = Object.create(null);
      for (var i = 0; i < w.length; i++) at[w[i]] = i;
      return { w: w, m: d.m.split(" ").map(function (x) { return parseInt(x, 16); }), at: at, c: d.c ? d.c.split(" ") : null };
    }).catch(function () { wordsP = null; return null; });
    return wordsP;
  }
  // how often exam number fi (index.json order) uses word i: from words.json "c" (its exams in bit order), 1 for a
  // word only one exam uses, 0 when the exam never does
  function wordCount(W, i, fi) {
    var m = W.m[i];
    if (!(m & (1 << fi))) return 0;
    if (!W.c || !W.c[i]) return 1;
    var k = 0; for (var b = 0; b < fi; b++) if (m & (1 << b)) k++;
    return +(W.c[i].split(".")[k] || 1);
  }
  // the exam of this semester whose guides say the most about the question: its LEAST used naming word counts (an
  // exam that never says "embolism" knows nothing about "pulmonary embolism"); null when no exam holds them all
  function examByWords(text, f) {
    return words().then(function (W) {
      if (!W || !IX) return null;
      var ix = specific(text).map(function (w) { return wordAt(W, w); });
      if (!ix.length || ix.some(function (i) { return i < 0; })) ix = ix.filter(function (i) { return i >= 0; });
      if (!ix.length) return null;
      var best = null, bs = 0;
      IX.folders.forEach(function (x, fi) {
        if (x.sem !== f.sem || !hasGuides(x)) return;
        var s = Math.min.apply(null, ix.map(function (i) { return wordCount(W, i, fi); }));
        if (s > bs || (s === bs && s > 0 && x === f)) { bs = s; best = x; }
      });
      return best ? { f: best, n: bs } : null;
    });
  }
  function wordAt(W, w) {                         // a word (or its singular / plural) in some guide: its index, else -1
    var c = [w, w + "s", w + "es", w.replace(/ies$/, "y"), w.replace(/es$/, ""), w.replace(/s$/, "")];
    for (var i = 0; i < c.length; i++) if (c[i].length >= 3 && W.at[c[i]] !== undefined) return W.at[c[i]];
    return -1;
  }
  // the student's words, misspellings fixed (case and punctuation kept); fx.fixed lists [typed, read as]
  function fixSpelling(text) {
    return words().then(function (W) {
      var fixed = [];
      if (!W) return { text: text, fixed: fixed };
      var ab = (IX && IX.ab) || {};
      var out = String(text).replace(/[A-Za-z]{4,}/g, function (raw) {
        var w = raw.toLowerCase();
        if (STOP[w] || ab[w] || wordAt(W, w) >= 0) return raw;
        var best = null, i, v, max = w.length >= 9 ? 2 : 1;
        if (w.length >= 5) for (i = 0; i < W.w.length && !best; i++) { v = W.w[i]; if (v.length > w.length && v.indexOf(w) === 0) best = v; }
        for (var d = 1; d <= max && !best; d++)
          for (i = 0; i < W.w.length; i++) {
            v = W.w[i];
            if (v[0] === w[0] && Math.abs(v.length - w.length) <= d && v.length >= 3 && near(w, v, d)) { best = v; break; }
          }
        if (!best) return raw;
        fixed.push([raw, best]);
        return raw[0] === raw[0].toUpperCase() ? best[0].toUpperCase() + best.slice(1) : best;
      });
      return { text: out, fixed: fixed };
    });
  }
  // words that ask rather than name ("can you give me the one ... of each"): never a topic
  var FILL = {};
  ("give tell show list name explain describe define definition meaning mean means each every all one single main key " +
   "can could would you please need want get just again different kind kinds sort sorts " +
   // words that frame a question ("where are they found", "what does X stand for", "how big", "how long", "how does it work")
   "found stand stands fail fails big bigger small smaller feel feels look looks looking work works working place places " +
   "cutoff cutoffs much many long often usually happen happens mechanism mechanisms calculate calculating calculation " +
   "step steps formation classification classify").split(" ").forEach(function (w) { FILL[w] = 1; });
  function specific(text) {                       // the question's naming words, raw (as words.json holds them)
    return uniq(letterTerms(norm(text)).split(/[^a-z0-9]+/).filter(function (w) {
      return w.length >= 3 && !STOP[w] && !FILL[w] && !GENERIC[stem(w)] && !CMPW[w] && !/^\d+$/.test(w);
    }));
  }
  // the semester's exams whose guides or cards hold the question's words, best first (a word few exams use
  // counts more); the active exam leads on a tie. At most four.
  function examsFor(text, f) {
    return words().then(function (W) {
      if (!W || !IX) return [f];
      var ws = specific(text).map(function (w) { var i = wordAt(W, w); return i < 0 ? 0 : W.m[i]; }).filter(Boolean);
      if (!ws.length) return [f];
      var pop = function (m) { var n = 0; while (m) { n += m & 1; m >>>= 1; } return n; };
      var rs = IX.folders.map(function (x, i) {
        if (x.sem !== f.sem || !hasGuides(x)) return null;
        var sc = 0; ws.forEach(function (m) { if (m & (1 << i)) sc += 1 / pop(m); });
        return sc ? { f: x, sc: sc * (x === f ? 1.1 : 1) } : null;
      }).filter(Boolean).sort(function (a, b) { return b.sc - a.sc; });
      if (!rs.length) return [f];
      return rs.filter(function (r) { return r.sc >= rs[0].sc * 0.5; }).slice(0, 4).map(function (r) { return r.f; });
    });
  }
  function prepGuide(g) {
    if (!g._ix) {
      g._texts = g.b.map(function (b) { return b[3]; });
      // a line's own heading and its item heading ("Aortic stenosis", for "Defining feature: ...") count as weaker
      // words of it (its lecture would not: every line of a lecture would then hold its title's words)
      g._ix = makeIndex(g._texts, g.b.map(function (b) { return (b[2] || "") + (b[5] ? " " + b[5] : ""); }));
    }
    return g;
  }

  // ------------------------------------------------------------------ "what does X mean": the defining sentence
  // Jaxon, 2026-10-15: "What does iatrogenic mean" got a long pulmonic regurgitation card (the word is in its
  // other names). A short "what is X" / "what does X mean" / bare "X" is answered with the sentence of the
  // guides or cards that DEFINES X; a card leads only when its title names X. When the class materials only
  // use the word, Pip shows where it comes up and general knowledge (Claude, labelled) gives the meaning.
  var DEFQ = /^(?:so |ok |okay |and )?(?:what(?:'s| is| are| was| were)|whats|what does|what do|define|definition of|meaning of|what(?:'s| is) the (?:meaning|definition) of|what is meant by|what does the (?:word|term))\s+(?:the (?:word|term) )?(?:an? |the )?(.+?)(?:\s+(?:mean|means|stand for|stands for|refer to|refers to))?(?:\s+again)?$/;
  function defineTerm(text) {
    var n = norm(text).replace(/[’]/g, "'").replace(/[?!.\s]+$/, "").trim(), m = n.match(DEFQ), t = m ? m[1] : null;
    if (!t) { m = n.match(/^(.+?)\s+(?:meaning|definition|defined|means)$/); t = m ? m[1] : null; }
    var bare = !t;
    if (bare) {                                   // a bare term ("iatrogenic", "junctional rythm?"): up to three naming words
      if (Object.keys(wants(text)).length || COMPARE.test(n) || n.split(/\s+/).length > 3) return null;
      t = n;
    }
    t = t.replace(/^["“'‘]+|["”'’]+$/g, "").trim();
    if (!t || t.split(/\s+/).length > 4) return null;
    if (/\b(for|of|in|with|between|to|vs|versus|and|or|from|on|when|how|why|that|which|most|best|first|cause|causes|treat|treatment|happen|happens|do|does|is|are|you|i|me|my)\b/.test(t)) return null;
    var tt = toks(t);
    if (!tt.length || tt.some(function (x) { return GENERIC[x]; })) return null;
    return { t: t, bare: bare };
  }
  function ciRe(s) {                              // a term as a case-blind pattern, so the rest of a pattern can care about case
    return escRe(s).replace(/[a-z]/gi, function (c) { return "[" + c.toLowerCase() + c.toUpperCase() + "]"; }).replace(/\s+/g, "[\\s-]+");
  }
  function defPatterns(term) {
    var t = ciRe(term) + "(?:e?s)?";                // "Bacteriostatic drugs. They inhibit growth ..."
    return [
      // "Tachyphylaxis is the loss of effect ...", "Pulmonic regurgitation is incomplete closing of ...": not "X is the
      // whole problem", "X is the most common cause", "X is handled by ..." (a verb ending in -ed, unless "defined as")
      [3, new RegExp("(?:^|[.;!?]\\s+|^[-\u2022]\\s*)(?:[Aa]n? |[Tt]he )?(" + t + ")\\s+(?:is|are|means|refers to|describes|denotes)\\s+" +
        "(?!(?:the |a |an )?(?:whole|main|key|first|best|most|same|only|big|biggest|real|problem|answer|reason|issue|point|more|less|least|" +
        "usually|often|common|commonest|rare|rarely|always|never|not|also|second|third|important|present|absent|typically|classically|called|" +
        "increased|decreased|elevated|low|high|higher|lower)\\b)(?!(?!(?:defined|known|termed|characterized|marked)\\b)[a-z]+ed\\b)")],
      [3, new RegExp("\\b(" + t + ")\\s*\\(([a-z][^()]{5,120})\\)")],           // "Iatrogenic (caused by treatment)"
      // "Opsonization — Coating the organism so ...": strong at a line's start with one dash (not a table row)
      [2, new RegExp("\\b(" + t + ")(?:\\s*\\([^()]{1,20}\\))?\\s*(?:=|\u2014|:)\\s*(?:a |an |the )?([A-Za-z][^.;()]{8,140})")],   // "Half-life (t\u00bd) \u2014 the time ..."
      [2, new RegExp("([^.;:()]{8,140})\\((" + t + ")\\)")],                       // "from a medical procedure (iatrogenic)"
      [2, new RegExp("^(" + t + ")\\.\\s+((?:It|They|This|These|A|An|The)\\s[^.]{10,200})")]   // "Opsonization. It coats ..."
    ];
  }
  function sentencesOf(x) {
    return String(x).split(/\n+/).map(function (l) { return l.replace(/^[-•]\s+/, "").trim(); }).filter(Boolean)
      .reduce(function (a, l) { return a.concat(l.replace(/([.!?])\s+(?=[A-Z★])/g, "$1\u0001").split("\u0001")); }, []);
  }
  function headOf(b, g) {                          // a block's place, short: its item heading, else its section without badges
    var h = b[5] || String(b[2] || "").split(" \u203a ").pop() || g.docs[b[0]].title;
    h = h.split("\u2605")[0].replace(/\s+(Routine|Urgent|Emergent|Emergency|Slides? [\d,–-]+)$/i, "").trim() || h;
    return h.length > 80 ? h.slice(0, h.lastIndexOf(" ", 77)) + "\u2026" : h;
  }
  // a heading ABOUT the term ("2.1 · Selective toxicity"), not one that names it among others ("acquired (traumatic or iatrogenic)")
  function aboutTerm(head, tt) {
    var ht = toks(String(head).replace(/^[\d.\s·]+|objectives?\s+[\d&,\s–-]+\s*—/gi, "")).filter(function (w) { return !GENERIC[w]; });
    var n = tt.filter(function (w) { return ht.indexOf(w) >= 0; }).length;
    return n === tt.length && n * 2 >= ht.length;
  }
  function findDefinition(term, scope, here) {
    var bare = term.replace(/\s+(drugs?|agents?|medications?|therapy|tests?|signs?)$/i, "");
    var pats = defPatterns(term).concat(bare !== term ? defPatterns(bare).map(function (p) { return [p[0] - 0.2, p[1]]; }) : []);
    var tt = uniq(toks(bare));
    var best = null, mentions = [], taught = false;   // taught: a heading of some guide is about the term
    function consider(s, sc, src) {
      if (s.length > 320) return;
      for (var i = 0; i < pats.length; i++) {
        var m = s.match(pats[i][1]);
        if (!m) continue;
        var k = i % 5, off = i >= 5 ? 0.2 : 0, pw = pats[i][0];   // i >= 5: the term without "drug", "test" ...
        // "X (gloss)" and "X: gloss" define X only when nothing modifies it: "epidermal hyperplasia (active T cells
        // drive ...)" says what drives the epidermal kind, not what hyperplasia is
        if ((k === 1 || k === 2) && m.index > 0 && !/(?:[,;:(\u2014\u2013-]\s*|\b(?:a|an|the|of|or|and|called|termed|as)\s+)$/i.test(s.slice(0, m.index))) continue;
        if (k === 2) pw = (m.index === 0 && s.split(" \u2014 ").length === 2 ? 3 : /^[a-z]/.test(m[2]) ? 2 : 1.5) - off;
        if (k === 4) pw = 3 - off;
        var score = pw * (src.f === here ? 1.2 : 1) * (src.card ? 1.1 : 1) - s.length / 400;
        // [3] "X (gloss)" and [2] "X = gloss" give the meaning in their own words: "Iatrogenic: caused by treatment."
        var gloss = k === 1 || k === 2 ? m[2].trim().replace(/[\s,:;—-]+$/, "") : null;
        if (gloss && /^[A-Z][a-z]/.test(gloss)) gloss = gloss.charAt(0).toLowerCase() + gloss.slice(1);
        if (!best || score > best.sc) best = { sc: score, strong: pw >= 2.8, s: s, gloss: gloss, src: src };
        return;
      }
    }
    return Promise.all(scope.map(function (f) {
      return Promise.all([f.ex ? explainOf(f) : null, guideIndex(f).then(prepGuide).catch(function () { return null; })]).then(function (r) {
        var e = r[0], g = r[1];
        if (e) e.cards.forEach(function (c) {
          if (!tt.every(function (w) { return toks(c.x).indexOf(w) >= 0; })) return;
          sentencesOf(c.x).forEach(function (s) { consider(s, 0, { f: f, card: c, file: c.doc, a: c.a, head: c.t }); });
        });
        if (!g) return;
        g.b.forEach(function (b, i) {
          var tf = g._ix.docs[i].tf;
          if (!tt.every(function (w) { return tf[w]; }) || g.docs[b[0]].kind === "cram") return;
          if (!taught && aboutTerm(b[5] || String(b[2] || "").split(" \u203a ").pop(), tt)) taught = true;
          var src = { f: f, file: g.docs[b[0]].file, a: b[1], head: headOf(b, g), text: b[3] };
          sentencesOf(b[3]).forEach(function (s) { consider(s, 0, src); });
          mentions.push(src);
        });
      });
    })).then(function () {
      // where the word comes up: one line per section, this exam first, short lines first
      var seen = {}, ms = mentions.sort(function (a, b) { return (b.f === here) - (a.f === here) || a.text.length - b.text.length; })
        .filter(function (m) { var k = m.f.s + "|" + m.head; if (seen[k] || (best && best.src.head === m.head)) return false; seen[k] = 1; return true; });
      return { def: best, mentions: ms.slice(0, 3), total: mentions.length, taught: taught };
    });
  }
  // the card whose TITLE is about the term (not one that lists it among others: "The optic disc: normal,
  // papilledema, cupping and atrophy" does not answer "what is atrophy"), or whose other name IS the term
  function titleNames(c, term) {
    var tt = toks(numbered(term));
    if (!tt.length) return false;
    if (c.k.some(function (k) { return norm(k) === norm(term); })) return true;
    var share = function (s) { var t = uniq(toks(numbered(s))).filter(function (w) { return !GENERIC[w]; }); return tt.every(function (w) { return t.indexOf(w) >= 0; }) ? tt.length / t.length : 0; };
    return share(String(c.t).split(":")[0]) >= 0.4 || share(c.t) >= 0.5;
  }

  // ------------------------------------------------------------------ "the X of each Y": one line per item
  // Jaxon, 2026-10-15: "Can you give me the one defining feature of each valvular disease" got one card about
  // something else. The guide has the answer as one "Defining feature:" line per condition (section 4.13, one
  // h4 per condition), so Pip gathers it: the lecture or section the group names, then from each item in it
  // the line that carries the asked-for label.
  function listAsk(text) {
    var n = norm(text).replace(/[’]/g, "'").replace(/[?!.\s]+$/, "").trim(), m, attr = "", group = "";
    if ((m = n.match(/^(.*?)\b(?:of|for|in|on|from|about)\s+(?:each|every|all)(?:\s+of)?(?:\s+the)?\s+(.+)$/))) { attr = m[1]; group = m[2]; }
    else if ((m = n.match(/\b(?:each|every)\s+(.+?)'s?\s+(.+)$/))) { group = m[1]; attr = m[2]; }
    else if ((m = n.match(/^(?:(?:can|could|would) you |please )*(?:list|name)\s+(?:all\s+)?(?:of\s+)?(?:the\s+)?(.+)$/))) group = m[1];
    else if ((m = n.match(/^what are all(?: of)?(?: the)? (.+)$/))) group = m[1];
    else return null;
    var strip = function (s) { var w = s.split(/\s+/); while (w.length && (FILL[w[0]] || STOP[w[0]] || /^(what'?s?|whats|is|are)$/.test(w[0]))) w.shift(); return w.join(" "); };
    attr = strip(attr); group = strip(group.replace(/\s+(please|again)$/, ""));
    var gt = toks(group).filter(function (w) { return !GENERIC[w] && !FILL[w]; });
    if (!gt.length) return null;
    return { attr: attr, at: uniq(toks(attr)).filter(function (w) { return !FILL[w]; }), group: group, gt: uniq(gt) };
  }
  function gatherList(L, scope, here) {
    return Promise.all(scope.map(function (f) {
      return guideIndex(f).then(prepGuide).then(function (g) {
        var hasAll = function (s) { var t = toks(s); return L.gt.every(function (w) { return t.indexOf(w) >= 0; }); };
        var parts = (g.p || []).map(hasAll), heads = {};
        var inScope = function (b) { return (b[4] >= 0 && parts[b[4]]) || (heads[b[2]] !== undefined ? heads[b[2]] : (heads[b[2]] = hasAll(b[2] || ""))); };
        var items = [], by = {}, label = new RegExp("^([^:—]{2,40})[:—]");
        g.b.forEach(function (b, i) {
          if (g.docs[b[0]].kind === "cram" || !inScope(b)) return;
          var name = b[5] || "", text = b[3], tf = g._ix.docs[i].tf;
          if (L.at.length) {
            // the asked-for label at the start of the line ("Defining feature: ...") or, failing that, all its words in it
            var lm = text.match(label), lab = lm ? toks(lm[1]) : [];
            var atStart = L.at.every(function (w) { return lab.indexOf(w) >= 0; });
            if (!atStart && !L.at.every(function (w) { return tf[w]; })) return;
            if (!name) { var row = text.split(" — "); if (row.length > 1 && row[0].length <= 50 && !atStart) name = row[0]; }
            if (!name) return;
            var k = norm(name);
            if (by[k] && (by[k].atStart || !atStart)) return;
            var it = { name: name, text: atStart ? text.slice(lm[0].length).trim() : text, atStart: atStart, f: f, file: g.docs[b[0]].file, a: b[1] };
            if (by[k]) items[items.indexOf(by[k])] = it; else items.push(it);
            by[k] = it;
          } else if (name && !by[norm(name)]) {   // "list all the X": the item headings themselves
            by[norm(name)] = 1; items.push({ name: name, text: "", f: f, file: g.docs[b[0]].file, a: b[1] });
          }
        });
        return { f: f, items: items, part: (g.p || []).filter(function (p, i) { return parts[i]; })[0] || "" };
      }).catch(function () { return { f: f, items: [] }; });
    })).then(function (rs) {
      rs = rs.filter(function (r) { return r.items.length >= 2; })
        .sort(function (a, b) { return (b.items.length + (b.f === here ? 1 : 0)) - (a.items.length + (a.f === here ? 1 : 0)); });
      return rs[0] || null;
    });
  }

  // the share of the question's naming words that Pip's cards (title, other names, whole text) or the shown
  // passages hold: under COVER, the class materials answer only part of it
  // How much of the question the shown cards or passages hold: its naming words (shorthand and abbreviations
  // expanded), each weighted by how rare it is in that exam's own cards or guide, so a missing everyday word
  // ("looks", "rate") barely counts and a missing word they never use ("why does aortic stenosis cause syncope
  // during pregnancy") counts a lot. Under SHORT_OF the class materials answer only part of it.
  var SHORT_OF = 0.8;
  function shareIn(text, have, ix) {
    var ab = (IX && IX.ab) || {}, tot = 0, got = 0;
    specific(casual(text)).forEach(function (w) {
      var t = toks(numbered(w))[0]; if (!t) return;
      var df = (ix && ix.df[t]) || 0, wt = ix ? Math.log(1 + (ix.N - df + 0.5) / (df + 0.5)) : 1;
      var long = ab[w] ? toks(ab[w]) : null;
      tot += wt;
      if (have[t] || (long && long.length && long.every(function (x) { return have[x]; }))) got += wt;
    });
    return tot ? got / tot : 1;
  }
  function fullCover(cards, text, plain) {       // plain: every word counts the same (is the card about this at all?)
    var have = {};
    cards.slice(0, 2).forEach(function (c) { toks(numbered(c.t + " " + c.k.join(" ") + " " + c.x)).forEach(function (w) { have[w] = 1; }); });
    return shareIn(text, have, plain ? null : cards[0] && cards[0]._ix);
  }
  function passCover(out, text) {
    var have = {};
    out.forEach(function (r) { toks(numbered((r.b[2] || "") + " " + (r.b[5] || "") + " " + r.b[3])).forEach(function (w) { have[w] = 1; }); });
    return shareIn(text, have, out[0] && out[0].g._ix);
  }
  // guide passages: the active exam's when they cover the question, else the best of the exams that hold its words
  // (a common word such as "pathogen" must not bring another class's table row ahead of this exam's own lines)
  function wideHits(f, scope, qx, here, text) {
    var others = scope.filter(function (x) { return x !== f && hasGuides(x); });
    return (hasGuides(f) ? guideHits([f], qx, here) : Promise.resolve([])).then(function (own) {
      if ((own.length && passCover(own, text) >= SHORT_OF) || !others.length) return own;
      return guideHits(others, qx, here).then(function (ot) {
        if (!own.length) return ot;
        return ot.length && passCover(ot, text) > passCover(own, text) ? ot : own;
      });
    });
  }
  // Claude's "answer" reply: "Used: 2, 1" (the candidates it answered from; null when the line is missing), the answer,
  // and an optional "General:" paragraph for what the candidates don't cover
  function parseAnswer(raw, n) {
    var lines = String(raw || "").replace(/\r/g, "").split("\n"), used = null;
    while (lines.length && !lines[0].trim()) lines.shift();
    var m = lines.length && lines[0].match(/^\s*\**used\**:\s*(.*)$/i);
    var refs = [];
    if (m) {
      lines.shift();
      // mode "guide": "[123]" is a line of the study guide, a plain number one of Pip's candidates (in the order written)
      m[1].replace(/\[\s*(\d+)\s*\]|(\d+)/g, function (all, ln, cn) {
        if (ln) refs.push({ line: +ln }); else if (+cn >= 1 && +cn <= n) refs.push({ cand: +cn });
        return all;
      });
      used = /none/i.test(m[1]) ? [] : uniq(refs.filter(function (t) { return t.cand; }).map(function (t) { return t.cand; }));
      if (/none/i.test(m[1])) refs = [];
    }
    var body = lines.join("\n").trim(), gen = "", gi = body.search(/(^|\n)\s*\**general\**:/i);
    if (gi >= 0) { gen = body.slice(gi).replace(/^\s*\**general\**:\s*/i, "").trim(); body = body.slice(0, gi).trim(); }
    return { used: used, body: body, general: gen, refs: refs };
  }
  function paras(into, text) {                     // plain lines as paragraphs, "- " lines as a list (text only, never HTML)
    var list = null;
    String(text || "").split(/\n+/).forEach(function (line) {
      line = line.trim(); if (!line) return;
      var m = line.match(/^(?:[-\u2022*]|\d+[.)])\s+(.*)$/);
      if (m) { if (!list) { list = el("ul"); into.appendChild(list); } list.appendChild(el("li", null, m[1])); }
      else { list = null; into.appendChild(el("p", null, line)); }
    });
  }
  // "From general knowledge" (Jaxon, 2026-10-15): Claude, labelled "not from your class materials", only when the
  // class materials fall short; the passages Pip did find go along so Claude fills the gap instead of repeating
  // them. Lookups never; every usual limit applies (maybeClaude).
  function general(question, passages, f, why) {
    if (LOOKUP.test(norm(question).trim())) return;
    var ps = (passages || []).slice(0, 3);
    maybeClaude(question, "general", ps, f, why);
  }

  // the line of the explained section that is most about this concept: the card's own names and the
  // question's words, weighted by how rare they are in the guide
  function guideLine(f, c, amap, question) {
    f = c._f || f; amap = c._m || amap;           // a card from another exam reads THAT exam's guide
    if (!amap) return Promise.resolve(null);
    return guideIndex(f).then(function (g) {
      prepGuide(g);
      // the question's own words decide (weight 1); the card's names only break ties (weight 0.35)
      var qw = uniq(toks(spell(numbered(casual(question)), g._ix))), cw = uniq(toks(numbered(c.t + " " + c.k.join(" ")))).filter(function (w) { return qw.indexOf(w) < 0; });
      var key = qw.filter(function (w) { return !GENERIC[w] && g._ix.df[w]; });
      var idf = function (w) { return Math.log(1 + (g._ix.N - g._ix.df[w] + 0.5) / (g._ix.df[w] + 0.5)); };
      var best = null, top = 0;
      g.b.forEach(function (b, i) {
        var doc = g.docs[b[0]];
        if (doc.kind === "cram" || doc.file !== c.doc) return;
        var tf = g._ix.docs[i].tf, sc = 0, text = b[3], head = norm(text).slice(0, 40);
        qw.forEach(function (w) { if (tf[w]) sc += idf(w); });
        cw.forEach(function (w) { if (tf[w]) sc += idf(w) * 0.35; });
        if (!sc) return;
        if ((text.match(/ · /g) || []).length >= 3) return;                // a navigation strip, not a sentence
        if (amap[doc.file + "#" + b[1]] !== c.u) sc *= 0.55;             // another section of the same page: only if clearly better
        // a bare heading or name ("Pericardial friction rub") says nothing; a line that STARTS with the
        // asked-about term ("Furuncle — ...") is about it, one that only lists it in passing is not
        if (text.length < 50 || (text.length < 70 && !/[.—:;]/.test(text))) sc *= 0.45;
        if (key.some(function (w) { return toks(head).indexOf(w) >= 0; })) sc *= 1.3;
        if (sc > top) { top = sc; best = { b: b, doc: doc }; }
      });
      return best;
    }).catch(function () { return null; });
  }
  // the explanation as Pip's own message (or, inside a drill card, a panel under the answer)
  // "Helpful?" under an explanation (one of Pip's cards or a Claude assist): one tap adds 1 to an anonymous
  // count and that is all; nothing records which explanation it was or who tapped
  var THUMB = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" ' +
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 11v9H4v-9z"/>' +
    '<path d="M7 11l4-7c1.3 0 2.2 1 2 2.3L12.5 10H18a2 2 0 0 1 2 2.3l-1.2 6A2 2 0 0 1 16.8 20H7"/></svg>';
  function helpful(into) {
    if (!into || into.querySelector(".pw-help")) return;
    var row = el("div", "pw-help");
    row.appendChild(el("span", null, "Helpful?"));
    [["thumb_up", "Yes, that helped", ""], ["thumb_down", "No, that didn't help", " pw-down"]].forEach(function (t) {
      var b = el("button", "pw-thumb" + t[2]); b.type = "button";
      b.setAttribute("aria-label", t[1]); b.title = t[1]; b.innerHTML = THUMB;
      b.addEventListener("click", function () {
        count(t[0]);
        row.textContent = t[0] === "thumb_up" ? "Glad it helped." : "Thanks for telling me. Say which part is fuzzy, or ask \u201cwhy?\u201d, and I'll try again.";
        row.classList.add("pw-thanked");
        if (t[0] === "thumb_down" && !offerSend(into, row)) input.focus();
      });
      row.appendChild(b);
    });
    into.appendChild(row);
  }
  // Jaxon, 2026-10-15: "Helpful?" should tell him how to improve Pip's answers. After a thumbs-down the student
  // may CHOOSE to send the question and Pip's answer, with an optional comment. Only that, the exam, the kind of
  // answer and the day go: no name, email or account id. Never an answer that used the student's own notes
  // (note cards, or a summary or Claude answer built from them): those are not offered at all. At most 5 a day
  // on a device. Create-only Firestore collection pip_feedback (firestore.rules); nobody can read it from the
  // site; Jaxon reads it with tools/pip_feedback_report.py.
  var K_FB = "local:pip:fb:day";
  function exchangeOf(into) {
    var top = into; while (top && top.parentNode !== log) top = top.parentNode;
    var me = top; while (me && !me.classList.contains("pw-me")) me = me.previousElementSibling;
    if (!me) return null;
    var parts = [], kind = "pip";
    for (var n = me.nextElementSibling; n; n = n.nextElementSibling) {
      if (n.classList.contains("pw-me")) break;
      if (n.classList.contains("pw-note") || n.classList.contains("pw-private") || n.querySelector(".pw-note, .pw-private")) return null;
      if (n.classList.contains("pw-general")) kind = "general";
      else if ((n.classList.contains("pw-claude") || n.classList.contains("pw-answer")) && kind === "pip") kind = "claude";
      var c = n.cloneNode(true);
      Array.prototype.forEach.call(c.querySelectorAll(".pw-help, .pw-fb, button, form, textarea"), function (x) { x.remove(); });
      Array.prototype.forEach.call(c.querySelectorAll("h4, p, div, li, dt, dd, summary, tr, span.pw-lbl"), function (x) { x.appendChild(document.createTextNode(" ")); });
      var t = c.textContent.replace(/\s+/g, " ").trim(); if (t) parts.push(t);
    }
    return { q: me.textContent.trim(), a: parts.join("\n"), kind: kind };
  }
  function offerSend(into, row) {
    var fb = null; try { fb = window.firebase && firebase.firestore && firebase.auth ? firebase : null; } catch (e) {}
    var ex = fb && exchangeOf(into), today = ymd(new Date()), d = jget(K_FB, null);
    if (!ex || (d && d.d === today && d.n >= 5)) return false;
    var box = el("div", "pw-fb");
    box.appendChild(el("p", null, "Want to send this question and my answer so I can get better? Only the question, my answer, the exam and today's date are sent. No name or account."));
    var ta = el("textarea", "pw-fbc"); ta.rows = 2; ta.maxLength = 500;
    ta.placeholder = "What was wrong or missing? (optional)"; ta.setAttribute("aria-label", "What was wrong or missing? (optional)");
    var r = el("div", "pw-row"), go = el("button", "pw-next", "Send"), no = el("button", "pw-chip", "No thanks");
    go.type = no.type = "button";
    r.appendChild(go); r.appendChild(no); box.appendChild(ta); box.appendChild(r);
    row.parentNode.insertBefore(box, row.nextSibling);
    no.addEventListener("click", function () { box.remove(); input.focus(); });
    go.addEventListener("click", function () {
      go.disabled = no.disabled = true; go.textContent = "Sending\u2026";
      var doc = { v: 1, day: today, exam: (lastAsk && lastAsk.f && lastAsk.f.s) || "", kind: ex.kind, q: ex.q.slice(0, 500), a: ex.a.slice(0, 3000) };
      if (ta.value.trim()) doc.c = ta.value.trim().slice(0, 500);
      var auth = fb.auth();
      new Promise(function (res) { var off = auth.onAuthStateChanged(function (u) { off(); res(u); }); })
        // never signed in: a silent anonymous session (as Group Study and the usage counts do), so the rule can ask for one
        .then(function (u) { return u || auth.signInAnonymously(); })
        .then(function () { return fb.firestore().collection("pip_feedback").add(doc); })
        .then(function () {
          var dd = jget(K_FB, null); dd = dd && dd.d === today ? dd : { d: today, n: 0 }; dd.n++; set(K_FB, JSON.stringify(dd));
          box.textContent = "Sent. Thank you, this helps me get better.";
        }, function () { box.textContent = "I couldn't send it just now. \u201cReport a mistake\u201d on the page works too."; });
    });
    setTimeout(function () { ta.focus(); }, 30);
    scrollDown();
    return true;
  }
  function explainBubble(c, f, into, before) {
    var m = el("div", "pw-msg pw-pip pw-explain");
    m.appendChild(el("span", "pw-xh", c.t));
    var cf = c._f || f;
    var list = null;
    String(c.x).split(/\n+/).forEach(function (line) {
      line = line.trim(); if (!line) return;
      var b = line.match(/^[-•]\s+(.*)$/);
      if (b) { if (!list) { list = el("ul"); m.appendChild(list); } list.appendChild(el("li", null, b[1])); }
      else { list = null; m.appendChild(el("p", null, line)); }
    });
    m.appendChild(linkTo(cf.f, c.doc, c.a, "Read it in your guide →"));
    if (into) into.insertBefore(m, before || null); else { log.appendChild(m); scrollDown(); }
    return m;
  }
  // after a drill question: the card for the guide section that question links to, picked by the
  // question and its answer; if that section has none, the best card for the words
  function explainQuestion(q, f, into, before) {
    return explainOf(f).then(function (e) {
      if (!e) return null;
      var words = q.q + " " + q.o[q.c][0], pick = null;
      var u = q.g && e.m[q.g[0] + "#" + q.g[1]];
      if (u) {
        var idx = [];
        e.cards.forEach(function (c, i) { if (c.u === u) idx.push(i); });
        var sub = makeIndex(idx.map(function (i) { return e._texts[i]; }), idx.map(function (i) { return numbered(e.cards[i].x); }));
        var r = rank(sub, idx.map(function (i) { return e._texts[i]; }), numbered(words), 1);
        pick = idx.length ? e.cards[idx[r.length ? r[0][1] : 0]] : null;
        if (!r.length && idx.length > 1) {          // nothing clearly closest: the card whose names the question uses most
          var best = -1;
          idx.forEach(function (i) { var n = toks(numbered(words)).filter(function (w) { return e._names[i][w]; }).length; if (n > best) { best = n; pick = e.cards[i]; } });
        }
      }
      if (!pick) return explainHits(f, words).then(function (h) { return h[0] || null; });
      return pick;
    }).then(function (c) { return c ? explainBubble(c, f, into, before) : null; });
  }

  // ------------------------------------------------------------------ Pip's brain (on this laptop)
  var brainP = null, brokeSaid = false;
  // a model that stops answering (no progress and no reply for this long) counts as failed
  var BRAIN_STALL_MS = window.__PIP_BRAIN_STALL_MS || 45000;
  function brain() {
    if (!brainP) brainP = window.PipBrain ? Promise.resolve(window.PipBrain)
      : loadScript(ROOT + "pip/pip-brain.js").then(function () { return window.PipBrain || null; });
    return brainP;
  }
  function sayBroke() {                           // said once per page, however the brain failed
    if (brokeSaid) return;
    brokeSaid = true;
    say("My laptop brain had trouble on this computer, so I'll stick to your guide's own words for now.");
  }
  function brainAfter(question, passages, lead, of, link) {   // resolves "summary" when a checked summary was shown
    return brain().then(function (B) {
      if (!B) return "none";
      if (B.tier() && !(B.broken && B.broken())) {
        var b = el("div", "pw-msg pw-pip pw-brain", "Let me put that simply…");
        log.insertBefore(b, lead); scrollDown();
        // a hung model (the WebLLM disposed-object bug can leave the graphics device stuck) must never
        // leave this bubble spinning or hold back the guide's passages and Claude: no progress and no
        // reply for BRAIN_STALL_MS counts as a failure
        var last = Date.now(), settled = false;
        var stall = new Promise(function (res, rej) {
          var iv = setInterval(function () {
            if (settled) return clearInterval(iv);
            if (Date.now() - last > BRAIN_STALL_MS) { clearInterval(iv); rej(new Error("stalled")); }
          }, 1000);
        });
        // the guard checks every word against exactly these passages (guide and notes alike)
        return Promise.race([B.summarize(question, passages, function (p) {
          last = Date.now();
          b.textContent = "Waking up my brain… " + Math.round(p * 100) + "%";
        }), stall]).then(function (r) {
          settled = true;
          if (!r.ok) { count("fallback"); b.remove(); return "failed"; }
          b.textContent = r.text;
          if (/notes/.test(of || "")) b.classList.add("pw-private");
          b.appendChild(el("span", "pw-lbl", "Pip's summary of " + (of || "your guide") + " · checked against the passages below"));
          if (link) b.appendChild(linkTo(link.folder, link.file, link.a, "Read it in your guide →"));
          scrollDown();
          return "summary";
        }).catch(function () {
          settled = true; count("error"); b.remove();
          if (B.markBroken) B.markBroken();
          sayBroke();
          return "failed";
        });
      }
      return "none";
    }).catch(function () { return "none"; });
  }

  // ------------------------------------------------------------------ the brain card, first thing on every open
  // Jaxon, 2026-10-10: "Pip should prompt people when they open the chat to download his brain before
  // he will answer questions". On a laptop or desktop that can run his brain (PipBrain.capable()) and
  // has none yet, EVERY open of the window starts with one card asking to download it, and typed
  // questions wait until the student picks (Pip says so once). "Not now" is for this open only: the
  // next open asks again (this replaced the after-a-question offer and its 14-day "no").
  // Going full screen and back is not a new open. During the download and first load questions wait
  // and are answered once it is ready; a failed or stalled download marks the brain broken for three
  // days (pip-brain.js) and Pip answers without it, with no card while it is broken. Phones,
  // tablets, computers that can't run it and computers that already have it never see the card.
  // gate.state: "checking" (asking the computer), "ask" (card up), "loading" (downloading), "off"
  var gate = { state: "off" }, installing = null, brainNews = null;
  function openGate(intent) {
    var g = gate = { state: "checking", intent: intent, told: false, queue: [], card: null };
    // a check that hangs (a graphics adapter that never answers) must never keep Pip silent: after
    // four seconds this open goes ahead without the card
    var slow = new Promise(function (res) { setTimeout(function () { res("off"); }, 4000); });
    g.ready = Promise.race([brainGate(), slow]).then(function (how) {
      if (g !== gate) return;                     // the window was closed (and maybe opened again) meanwhile
      if (how === "loading" && installing) { g.state = "loading"; progressCard(g); }
      else if (how && how.ask) brainCard(g, how.ask);
      else ungate(g);
    });
  }
  function brainGate() {                          // {ask: PipBrain}, "loading" or "off"
    if (installing) return Promise.resolve("loading");
    return brain().then(function (B) {
      if (!B || B.tier() || (B.broken && B.broken())) return "off";
      return B.capable().then(function (c) { return c && c.ok ? { ask: B } : "off"; });
    }).catch(function () { return "off"; });
  }
  function ungate(g) {                            // the student picked (or no card was needed): Pip is himself
    g.state = "off";
    if (brainNews === "broken") sayBroke();
    else if (brainNews === "ready") say("My brain finished downloading while you were away. It's ready.");
    brainNews = null;
    greet(g.intent);
    var q = g.queue; g.queue = [];
    if (!q.length) return;
    say("Now your question: “" + q[0] + "”");
    ask(q[0], true);
    if (q.length > 1) say("You asked me " + (q.length - 1) + " more " + (q.length === 2 ? "thing" : "things") +
      " while I was downloading. Ask me again and I'll answer " + (q.length === 2 ? "it" : "them") + " too.");
  }
  // a question typed while the card is up or the brain is downloading: true when it is held here
  function held(text) {
    var g = gate;
    if (g.state === "off") return false;
    if (g.state === "checking") {                 // a moment's wait while Pip asks the computer
      input.value = "";
      g.ready.then(function () { if (g === gate && isOpen && !held(text)) ask(text); });
      return true;
    }
    if (g.state === "ask") {
      if (g.told) { flash(g.card); return true; }  // said once already: the question stays in the box for later
      g.told = true; input.value = "";
      me(text);
      say("I'd love to help with that! First I need your answer to the card above: tap “Download my brain” or “Not now”, then ask me again.");
      return true;
    }
    input.value = "";                             // "loading"
    me(text);
    say("I'm still downloading my brain, nearly there. I'll answer that as soon as it's ready.");
    g.queue.push(text);
    return true;
  }
  function flash(node) {
    if (!node || !node.isConnected) return;
    scrollTo(node);
    node.classList.remove("pip-flash", "pip-flash-off"); void node.offsetWidth; node.classList.add("pip-flash");
    setTimeout(function () { node.classList.add("pip-flash-off"); }, 50);
    setTimeout(function () { node.classList.remove("pip-flash", "pip-flash-off"); }, 2800);
  }
  function brainCard(g, B) {
    g.state = "ask";
    var T = (B.tiers && (B.tiers.standard || B.tiers[Object.keys(B.tiers)[0]])) || { gb: 2.3 };
    var cd = card(); cd.classList.add("pw-brainask"); g.card = cd;
    cd.appendChild(el("h4", null, "First, can I download my brain?"));
    cd.appendChild(el("p", null, "My brain lets me put your study guide into a few plain sentences of my own, and I check every word against your guide."));
    cd.appendChild(el("p", null, "It's a one-time download of " + (+T.gb).toFixed(1) + " gigabytes. It stays on this computer and works offline after that, and nothing you ask it leaves this computer."));
    var go = el("button", "pw-big", "Download my brain"); go.type = "button";
    var no = el("button", "pw-later", "Not now"); no.type = "button";
    cd.appendChild(go); cd.appendChild(no);
    cd.appendChild(el("p", "pw-src", "Not now: I'll use your guide's own words this time and ask again the next time you open me."));
    go.addEventListener("click", function () {
      if (g !== gate || g.state !== "ask") return;
      count("brain_yes");
      startInstall(B, g);
    });
    no.addEventListener("click", function () {
      if (g !== gate || g.state !== "ask") return;
      count("brain_no");
      cd.remove(); g.card = null;
      say("No problem. This time I'll use your guide's own words. I'll ask again the next time you open me.");
      ungate(g);
    });
    scrollDown();
  }
  function startInstall(B, g) {
    g.state = "loading";
    var job = installing = { pct: 0, txt: "", view: null };
    var last = Date.now(), settled = false;
    // the same watchdog as a summary: no progress for BRAIN_STALL_MS is a failure, never a spinner forever
    var stall = new Promise(function (res, rej) {
      var iv = setInterval(function () {
        if (settled) return clearInterval(iv);
        if (Date.now() - last > BRAIN_STALL_MS) { clearInterval(iv); rej(new Error("stalled")); }
      }, 1000);
    });
    progressCard(g);
    P.react("think", 1);
    Promise.race([B.install("standard", function (p, txt) { last = Date.now(); job.pct = p || 0; job.txt = txt || ""; paint(job); }), stall])
      .then(function () {
        settled = true; installing = null;
        var g2 = gate;
        if (g2.state !== "loading") { brainNews = "ready"; return; }   // the window was closed meanwhile
        if (g2.card) g2.card.remove(); g2.card = null;
        P.react("celebrate_small", 1);
        say("All set! My brain is ready, and it stays on this computer.");
        ungate(g2);
      }, function () {
        settled = true; installing = null;
        count("error");
        if (B.markBroken) B.markBroken();
        var g2 = gate;
        if (g2.state !== "loading") { brainNews = "broken"; return; }
        if (g2.card) g2.card.remove(); g2.card = null;
        sayBroke();
        ungate(g2);
      });
  }
  function progressCard(g) {                      // the card while the brain downloads (on reopening, a new one)
    var cd = g.card && g.card.isConnected ? g.card : card();
    g.card = cd; cd.textContent = ""; cd.classList.add("pw-brainask");
    cd.appendChild(el("h4", null, "Downloading my brain…"));
    var bar = el("div", "pw-prog"), fill = el("i"); bar.appendChild(fill);
    bar.setAttribute("role", "progressbar"); bar.setAttribute("aria-label", "Downloading Pip's brain");
    bar.setAttribute("aria-valuemin", "0"); bar.setAttribute("aria-valuemax", "100");
    var note = el("p", "pw-src");
    cd.appendChild(bar); cd.appendChild(note);
    cd.appendChild(el("p", "pw-src", "I'll answer your questions as soon as it's ready. Keep this tab open; if you leave, it picks up where it left off."));
    if (installing) { installing.view = { bar: bar, fill: fill, note: note }; paint(installing); }
    scrollDown();
  }
  function paint(job) {
    var v = job.view;
    if (!v || !v.fill.isConnected) return;
    var pc = Math.max(0, Math.min(100, Math.round(job.pct * 100)));
    v.fill.style.width = pc + "%"; v.bar.setAttribute("aria-valuenow", String(pc));
    v.note.textContent = (!job.txt || /fetch|download|loading model from cache/i.test(job.txt) ? "Downloading… " : "Getting ready… ") + pc + "%";
  }

  // ------------------------------------------------------------------ Superbrain: asking Claude (opt-in, signed in)
  var sbP = null;
  function superbrain() {
    if (!sbP) sbP = window.PipSuperbrain ? Promise.resolve(window.PipSuperbrain)
      : loadScript(ROOT + "pip/pip-superbrain.js").then(function () { return window.PipSuperbrain || null; });
    return sbP;
  }
  var CLAUDE_SAYS = {
    user_day: "You've used today's Claude questions. They reset at midnight.",
    user_month: "You've used this month's Claude questions.",
    user_gap: "One second, then try again.",
    day_budget: "Claude's taking a break for the class today. Try again tomorrow.",
    month_budget: "Claude's out of study budget for this month.",
    refused: "Claude couldn't help with that one.",
    network: "I couldn't reach Claude. Check your connection and try again.",
    signed_out: "Sign in first, then ask again.",
    timeout: "Claude took too long to answer. Try again in a moment.",
    bad_text: "Some odd characters in that passage stopped Claude from reading it. Your guide's passages are above."
  };
  // ------------------------------------------------------------------ Pip decides when to ask Claude
  // Jaxon, 2026-10-08: "PIP should decide when to ask claude otherwise students may just use
  // all the claude API tokens". There is no Ask-Claude button. Pip calls Claude only when:
  //   - he has no checked explanation of his own for the question (no "Pip explains" card matched and,
  //     on a laptop with his brain, no checked summary), so the student would otherwise get only the
  //     guide's words (Jaxon, 2026-10-09: explain the concept, don't just give the guide);
  //   - the student says they still don't get it ("simpler") or asks why / for more ("deeper"),
  //     right after an answer;
  //   - the guide has nothing, but the question uses this exam's own words ("beyond").
  // Never for lookups, chit-chat, repeats (answers are remembered), or other classes; at most
  // 40 a day on this device (the helper allows 40 per student since 2026-10-15, when every question got a short answer
  // written with Claude) and one every 3 seconds (20 for the costlier "deeper" and "beyond"), on top of the server's caps.
  var followFrom = null;                         // the answer a follow-up is about (kept for a retry after the cooldown)
  var lastAsk = null, K_CDAY = "local:pip:claude:day", K_CCACHE = "local:pip:claude:cache", K_CNO = "local:pip:claude:no";
  // a follow-up is a short reply to the last answer ("why?", "I still don't get it"), never a new
  // question that happens to start with "why" (caught in testing: that sent a fresh question to
  // the costlier model as "go deeper" on the previous one)
  var SIMPLER = /^(huh|what|wait what|i (still )?(don'?t|do not) (get|understand)( it| that| this)?|still (confused|lost|don'?t get it)|what does that mean|i'?m (still )?(confused|lost)|(say|explain|put) (it|that|this) (simpler|more simply|in simpler (words|terms)|another way|differently|again)|(simpler|more simply)( please)?|in simpler (words|terms)|eli5|dumb it down|explain (again|it again|that again))[\s.!?]*$/;
  var DEEPER = /^(why|why is that|why does that happen|how come|how so|explain more|more detail|more details|go deeper|deeper|tell me more)[\s.!?]*$/;
  var EXPLAIN = /\b(why|how|explain|mechanism|causes?|caused|happens?|difference|differ|compare|versus|vs|relationship|leads? to|results? in|works?|role of|purpose of)\b/;
  function needsExplaining(q) { return EXPLAIN.test(norm(q)) && norm(q).split(/\s+/).length >= 4; }
  // a lookup ("where is ...", "open the cram sheet") wants a place, not an explanation
  var LOOKUP = /^(where|find|open|show me|take me|go to|link|page)\b/;
  function wantsExplanation(q) { var n = norm(q).trim(); return !LOOKUP.test(n) && toks(q).length >= 1 && (n.split(/\s+/).length >= 2 || needsExplaining(q)); }
  function relatedToExam(q, f) {                 // does the question use this exam's own vocabulary?
    return guideIndex(f).then(function (g) {
      prepGuide(g);
      var hits = toks(expandFor(q, g._ix)).filter(function (w) { return w.length >= 4 && g._ix.df[w]; });
      return hits.length >= 1 && norm(q).split(/\s+/).length >= 3;
    }).catch(function () { return false; });
  }
  function cacheKey(mode, q, f, priv) { return (priv ? "notes|" : "") + mode + "|" + (f ? f.s : "") + "|" + norm(q).replace(/[^a-z0-9]+/g, " ").trim(); }
  // An answer built from the student's own notes is never written to localStorage (cloud-sync
  // copies every key there, and "local:" keys would still hold note-derived text): it is kept
  // in memory for this page only.
  var privCache = {};
  function cached(k, priv) {
    var e = priv ? privCache[k] : jget(K_CCACHE, {})[k];
    return e && Date.now() - e.t < 14 * 864e5 ? e : null;
  }
  function remember(k, r, priv) {
    var e = { t: Date.now(), answer: r.answer, mode: r.mode };
    if (r.cites && r.cites.length) e.cites = r.cites;   // mode "guide": where the lines it used are
    if (priv) { privCache[k] = e; return; }
    var c = jget(K_CCACHE, {}); c[k] = e;
    var ks = Object.keys(c).sort(function (a, b) { return c[b].t - c[a].t; }); ks.slice(40).forEach(function (x) { delete c[x]; });
    set(K_CCACHE, JSON.stringify(c));
  }
  var lastClaudeAt = 0, signInNudged = false, ownerP = null;
  // Jaxon 2026-10-08: on his own account the manual Ask-Claude buttons stay. Who the owner is
  // lives only on the server (ADMIN_EMAILS / ADMIN_UIDS); /v1/status says owner:true after it
  // checks the sign-in, so no email or id is ever in the site's public code.
  function isOwner() {
    if (!ownerP) ownerP = superbrain().then(function (S) {
      if (!S || S.state() !== "ready") { ownerP = null; return false; }
      return S.status().then(function (st) { ownerKnown = !!(st && st.owner); return ownerKnown; });
    }).catch(function () { ownerP = null; return false; });
    return ownerP;
  }
  function ownerChips(list, extra) {             // add the owner's manual buttons to a chip row
    isOwner().then(function (o) { if (o) chips(list.concat(extra)); });
  }
  function deviceBudget() {
    var d = jget(K_CDAY, null), today = ymd(new Date());
    return d && d.d === today ? d : { d: today, n: 0 };
  }
  var ownerKnown = false, invitedOk = false, joinAsked = false;
  function joinCard(S, then) {
    var cd = card();
    cd.appendChild(el("h4", null, "Got your class code?"));
    cd.appendChild(el("p", null, "Your class has a code for Claude help. Enter it once and I can check the tricky ones with Claude."));
    var form = el("form", "pw-row"), inp = el("input", "pw-in"), go = el("button", "pw-next", "Join"), no = el("button", "pw-chip", "Not now");
    inp.type = "text"; inp.autocomplete = "off"; inp.setAttribute("aria-label", "Class code"); inp.placeholder = "Class code"; inp.maxLength = 64;
    inp.setAttribute("autocapitalize", "characters"); inp.setAttribute("autocorrect", "off"); inp.spellcheck = false;   // case doesn't matter to the helper
    go.type = "submit"; no.type = "button";
    form.appendChild(inp); form.appendChild(go); form.appendChild(no); cd.appendChild(form);
    var note = el("div", "pw-src"); cd.appendChild(note);
    no.addEventListener("click", function () { cd.remove(); });
    form.addEventListener("submit", function (e) {
      e.preventDefault(); if (!inp.value.trim()) return;
      go.disabled = true; note.textContent = "Checking…";
      S.join(inp.value).then(function (r) {
        go.disabled = false;
        if (r && r.ok) { cd.remove(); invitedOk = true; ownerP = null; say("You're in!"); if (then) then(); return; }
        note.textContent = r && r.code === "join_limit" ? "Too many tries today. Try again tomorrow."
          : r && r.code === "banned" ? "This account can't use Claude help." : "That code didn't work. Check it with your class.";
      });
    });
    setTimeout(function () { inp.focus(); }, 30);
  }
  var CANT_CLAUDE = "I can't check with Claude right now. Tell me which part is fuzzy, a word or a step, and I'll explain that piece.";
  function cantClaude() { count("fallback"); say(CANT_CLAUDE); }
  // A comparison may ask Claude unprompted only for a student who can already use him (signed in, invited,
  // consented), outside a quiz in progress (a past exam is fair game since 2026-10-11), inside the usual limits. Anything else is "no".
  var DEVICE_DAY = 40;
  function gapFor(mode) { return mode === "deeper" || mode === "beyond" ? 20000 : 3000; }
  function claudeRoom(mode) {
    if (!ownerKnown) {
      if (deviceBudget().n >= DEVICE_DAY) return false;
      if (Date.now() - lastClaudeAt < gapFor(mode)) return false;
    }
    return !(+get(K_CNO) && Date.now() - +get(K_CNO) < 14 * 864e5);
  }
  function claudeUsable(question, f) {
    if (quizInProgress() || (P.kind === "quiz" && looksLikeOpenQuestion(question))) return Promise.resolve(false);
    return isOwner().then(function () {
      return superbrain().then(function (S) {
        if (!S || S.state() !== "ready" || !S.consented()) return false;
        if (invitedOk) return true;
        return S.status().then(function (st) { if (st && st.ok !== false && st.invited) { invitedOk = true; return true; } return false; });
      });
    }).catch(function () { return false; });
  }
  function maybeClaude(question, mode, passages, f, why, fromFollowUp) {
    if (quizInProgress() || (P.kind === "quiz" && looksLikeOpenQuestion(question))) return;
    var priv = isPrivate(passages), k = cacheKey(mode, question, f, priv), hit = cached(k, priv);
    if (hit) { claudeCard({ answer: hit.answer }, hit.mode, passages, why + " (I'd asked before.)"); return; }
    var db = deviceBudget();
    if (db.n >= DEVICE_DAY && !ownerKnown) { if (fromFollowUp) say("I've checked with Claude a lot today, so let's stick with your guide until tomorrow."); return; }
    if (Date.now() - lastClaudeAt < gapFor(mode) && !ownerKnown) {
      // a follow-up is the student asking for help, so say why nothing happened (and keep it for a retry)
      if (fromFollowUp) { lastAsk = followFrom ? { q: followFrom.q, passages: followFrom.passages, f: f, t: Date.now(), expl: followFrom.expl }
                                       : { q: question.split("\nFollow-up")[0], passages: passages, f: f, t: Date.now() };
                          say("Give me a few seconds to catch my breath, then ask me again."); }
      return;
    }
    if (+get(K_CNO) && Date.now() - +get(K_CNO) < 14 * 864e5) { if (fromFollowUp) say("You asked me not to check with Claude, so let's look at your guide's passages again. You can turn Claude help back on in Settings."); return; }
    askClaude(question, mode, passages, f, why, k, fromFollowUp);
  }

  function askClaude(question, mode, passages, f, why, cacheK, fu) {
    if (quizInProgress()) { say(pausedText()); return; }
    if (P.kind === "quiz" && looksLikeOpenQuestion(question)) {
      say("That looks like a question you haven't answered yet. Give it your best shot first, then Claude and I can help.");
      return;
    }
    superbrain().then(function (S) {
      if (!S) { count("error"); return say("I can't reach Claude from here."); }
      var st = S.state();
      if (st === "off" || st === "no-sync") { if (fu) cantClaude(); return; }   // Pip can't reach Claude here: the passages stand
      if (st === "signed-out") {
        if (signInNudged) { if (fu) say(CLAUDE_SAYS.signed_out); return; }
        signInNudged = true;
        var cd = card();
        cd.appendChild(el("h4", null, "I could check this one with Claude"));
        cd.appendChild(el("p", null, "Sign in and I'll ask Claude when your guide isn't enough. Everyone in the class gets a fair share each day."));
        var row = el("div", "pw-row"), go = el("button", "pw-next", "Sign in with Google"); go.type = "button";
        go.addEventListener("click", function () {
          S.signIn().then(function () { setTimeout(function () { cd.remove(); if (S.state() === "ready") askClaude(question, mode, passages, f); }, 400); });
        });
        row.appendChild(go); cd.appendChild(row);
        return;
      }
      if (!invitedOk) {
        return S.status().then(function (st) {
          if (st && st.ok !== false && st.invited) { invitedOk = true; return askClaude(question, mode, passages, f, why, cacheK, fu); }
          if (!st || !st.canJoin || joinAsked) { if (fu) cantClaude(); return; }   // not invited and no way in: the passages stand
          joinAsked = true; joinCard(S, function () { askClaude(question, mode, passages, f, why, cacheK, fu); });
        });
      }
      if (!S.consented()) {
        var cc = card();
        cc.appendChild(el("h4", null, "Can I check with Claude when your guide isn't enough?"));
        cc.appendChild(el("p", null, "When I do, I send your question and the passages I found in your guide or notes " +
          "to Claude, an AI made by Anthropic. Nothing else about you is sent, and it's never used to grade you. You can turn this off in Settings."));
        var r2 = el("div", "pw-row"), yes = el("button", "pw-next", "Yes, check with Claude"), no = el("button", "pw-chip", "Not now");
        yes.type = no.type = "button";
        yes.addEventListener("click", function () { S.setConsent(true); cc.remove(); askClaude(question, mode, passages, f, why, cacheK, fu); });
        no.addEventListener("click", function () { set(K_CNO, String(Date.now())); cc.remove(); say("Okay. I'll stick to your guide."); });
        r2.appendChild(yes); r2.appendChild(no); cc.appendChild(r2);
        return;
      }
      var wait = say(mode === "beyond" ? "Your guide doesn't cover that. Let me check with Claude…" : mode === "general" ? "Let me check general knowledge with Claude…"
                     : mode === "simpler" ? "Let me ask Claude to put it another way…" : "Let me check with Claude…");
      var db = deviceBudget(); db.n++; set(K_CDAY, JSON.stringify(db)); lastClaudeAt = Date.now();
      count("claude_ask");
      var duet = P.duet && P.duet.start();
      var priv = isPrivate(passages);
      // private: the server must never put an answer built from the student's notes in its shared cache
      S.ask({ question: question, mode: mode, passages: passages, exam: { title: f ? f.t : "", folder: f ? f.f : "" }, private: priv }).then(function (r) {
        var show = function () {
          wait.remove();
          // a daily or monthly cap is Pip falling back to the guide; anything else is an error
          // a helper deployed before the "general" mode existed answers it as "beyond" (one retry)
          if (!r.ok && r.code === "bad_mode" && mode === "general") { wait.remove(); lastClaudeAt = 0; return askClaude(question, "beyond", passages, f, why, cacheK, fu); }
          if (!r.ok) { count(/^(user_|day_|month_)/.test(r.code || "") ? "fallback" : "error");
                       if (passages && passages.onFail) { passages.onFail(); return; }     // a comparison: the brain or the cards take over
                       say(CLAUDE_SAYS[r.code] || "Claude couldn't answer just now. Your guide's passages are above."); return; }
          if (cacheK) remember(cacheK, r, priv);
          claudeCard(r, mode, passages, why);
        };
        if (duet) P.duet.finish(!!r.ok, show); else show();
      });
    });
  }
  function claudeCard(r, mode, passages, why) {
    // Claude's answer is Pip's "own words" for a guide question: it goes above the guide's exact words
    // (once), with a "Read it in your guide" link under it
    var pl = passages && passages.place; if (pl) delete passages.place;
    var cd = card(); cd.classList.add("pw-claude");
    if (isPrivate(passages)) cd.classList.add("pw-private");        // built from the student's notes: never sent anywhere
    if (pl) {
      if (pl.note) pl.note.remove();
      if (pl.before && pl.before.parentNode === log) log.insertBefore(cd, pl.before);
    }
    var head = el("div", "pw-chead");
    if (mode === "general") {
      cd.classList.add("pw-general");
      var gh = el("div", "pw-part", "From general knowledge"); log.insertBefore(gh, cd);
      head.appendChild(el("b", null, "Claude"));
      head.appendChild(el("span", "pw-badge", "Not from your class materials"));
    } else head.appendChild(el("b", null, "Claude assist"));
    if (mode === "beyond") head.appendChild(el("span", "pw-badge", "Beyond your guide"));
    else if (mode === "deeper") head.appendChild(el("span", "pw-badge", "Deeper than your guide"));
    cd.appendChild(head);
    var list = null;
    String(r.answer || "").split(/\n+/).forEach(function (line) {
      line = line.trim(); if (!line) return;
      var m = line.match(/^(?:[-•*]|\d+[.)])\s+(.*)$/);
      if (m) { if (!list) { list = el("ul"); cd.appendChild(list); } list.appendChild(el("li", null, m[1])); }
      else { list = null; cd.appendChild(el("p", null, line)); }
    });
    var gl = mode !== "general" && passages && passages.link;
    if (gl) { var gw = el("div", "pw-glink"); gw.appendChild(linkTo(gl.folder, gl.file, gl.a, "Read it in your guide →")); cd.appendChild(gw); }
    if (why) cd.insertBefore(el("div", "pw-src", why + (r.cached ? " (Claude answered this one before.)" : "")), cd.children[1] || null);
    var foot = el("div", "pw-src");
    foot.appendChild(document.createTextNode("Claude can make mistakes. For your exam, your guide is the source." +
      (typeof r.remainingToday === "number" ? " " + r.remainingToday + " Claude question" + (r.remainingToday === 1 ? "" : "s") + " left today." : "")));
    if (window.reportMistake) {
      var rep = el("a", null, " Something off? Report it"); rep.href = "#";
      rep.addEventListener("click", function (e) { e.preventDefault(); window.reportMistake(); });
      foot.appendChild(rep);
    }
    cd.appendChild(foot);
    helpful(cd);
    if (pl) scrollTo(cd); else scrollDown();
  }

  // ------------------------------------------------------------------ "about this question" (only once it is answered)
  function currentAnswered() { var st = quizState(); return st.current && st.answered ? st.current : null; }
  function guideForCurrent() {
    var q = currentAnswered();
    if (!q) return say("Answer it first, then I'll show you.");
    context().then(function (c) {
      if (!c.here) return say("I don't have notes for this exam yet.");
      bankOf(c.here).then(function (b) {
        var hit = b.q.filter(function (x) { return x.id === q.qid; })[0];
        if (!hit || !hit.g) {
          if (quizInProgress()) return say("This one doesn't have a matching passage in your guide. Ask me again once you've answered the question.");
          say("This one doesn't have a matching passage. Here's what I found by searching instead:"); return searchGuides(q.q + " " + q.opts[q.c][0]);
        }
        var cd = card();
        cd.appendChild(el("h4", null, hit.g[2]));
        cd.appendChild(el("div", "pw-src", c.here.t + " · Study guide"));
        if (hit.g[3]) cd.appendChild(el("p", null, hit.g[3]));
        cd.appendChild(linkTo(c.here.f, hit.g[0], hit.g[1], null, hit.g[3]));
      });
    });
  }
  function moreLikeCurrent() {
    var q = currentAnswered();
    if (!q) return say("Answer it first, then I'll find more like it.");
    context().then(function (c) {
      if (!c.here) return say("I don't have questions for this exam yet.");
      bankOf(c.here).then(function (b) {
        var pool = notOpen(b.q.filter(function (x) { return x.io === q.io && x.id !== q.qid; }));
        if (!pool.length) return say("That was the only question on this objective.");
        count("practice");
        drill("More on " + shortIO(q.io), pickFresh(pool, 5), c.here);
      });
    });
  }

  // ------------------------------------------------------------------ choosing questions
  function hist() { return jget(K_HIST, {}); }
  function record(id, ok) {
    var h = hist(), r = h[id] || [0, 0, 0];
    h[id] = [r[0] + 1, r[1] + (ok ? 1 : 0), Math.round(Date.now() / 1000)];
    var ids = Object.keys(h);
    if (ids.length > 4000) ids.sort(function (a, b) { return h[a][2] - h[b][2]; }).slice(0, ids.length - 4000).forEach(function (k) { delete h[k]; });
    set(K_HIST, JSON.stringify(h));
  }
  function pickFresh(pool, n) {        // never-seen first, then the ones Pip has seen least lately
    var h = hist();
    return shuffle(pool.slice()).sort(function (a, b) {
      var x = h[a.id], y = h[b.id];
      return (x ? 1 : 0) - (y ? 1 : 0) || (x ? x[2] : 0) - (y ? y[2] : 0);
    }).slice(0, n);
  }
  function startPractice(folder, n) {
    if (quizInProgress()) return say(pausedText());
    bankOf(folder).then(function (b) {
      b = { q: notOpen(b.q), pages: b.pages };
      var h = hist(), missed = missedIds(folder, b), byId = {};
      b.q.forEach(function (q) { byId[q.id] = q; });
      // still-missed: wrong in a quiz and not answered right in Pip since
      var still = missed.filter(function (id) { return byId[id] && !(h[id] && h[id][1] > 0); }).map(function (id) { return byId[id]; });
      var weak = {};
      still.forEach(function (q) { weak[q.io] = (weak[q.io] || 0) + 1; });
      Object.keys(h).forEach(function (id) { var r = h[id]; if (byId[id] && r[0] > r[1]) weak[byId[id].io] = (weak[byId[id].io] || 0) + 1; });
      var done = doneQuizzes(), unseenPages = {};
      folder.quizzes.forEach(function (qz) { if (!done[decodedPath(new URL(pageURL(folder.f, qz.file)).pathname)]) unseenPages[qz.file] = 1; });
      var picked = [], used = {};
      function take(list, k) { list.forEach(function (q) { if (picked.length < n && k > 0 && !used[q.id]) { used[q.id] = 1; picked.push(q); k--; } }); }
      take(pickFresh(still, n), Math.round(n * 0.4));
      var weakIOs = Object.keys(weak).sort(function (a, z) { return weak[z] - weak[a]; }).slice(0, 3);
      take(pickFresh(b.q.filter(function (q) { return weakIOs.indexOf(q.io) >= 0; }), n), Math.round(n * 0.3));
      take(pickFresh(b.q.filter(function (q) { return q.p.some(function (f) { return unseenPages[f]; }); }), n), n);
      take(pickFresh(b.q, n), n);
      var why = still.length ? "mostly from what you've missed, plus a few you haven't seen" : "a mix across the whole exam";
      say("Here's a " + picked.length + "-question set for " + folder.t + ", " + why + ". It's just for you: it doesn't count toward the class stats.");
      count("practice");
      drill(folder.t + " practice", shuffle(picked), folder);
    }).catch(function () { say("I couldn't load the questions for " + folder.t + "."); });
  }
  function topicHits(b, text) {
    if (!b._ix) {
      b._texts = b.q.map(function (q) { return q.q + " " + q.o[q.c][0] + " " + q.o[q.c][1]; });
      b._ix = makeIndex(b._texts, b.q.map(function (q) { return (q.t || "") + " " + (q.io || ""); }));
    }
    return rank(b._ix, b._texts, expandFor(text, b._ix), 10).map(function (r) { return b.q[r[1]]; });
  }
  function topicPractice(folder, text) {
    if (quizInProgress()) return say(pausedText());
    bankOf(folder).then(function (b) {
      var hits = notOpen(topicHits(b, text));
      if (!hits.length) return say("I couldn't find questions about that in " + folder.t + ". Try the name of a condition, drug or test.");
      say((hits.length === 1 ? "Here's 1 question" : "Here are " + hits.length + " questions") + " about \"" + text + "\" from " + folder.t + ".");
      count("practice");
      drill("Practice: " + text, shuffle(hits), folder);
    });
  }
  function shortIO(io) {
    var s = String(io || "").replace(/^\s*(\d+)\s*[—-]\s*/, "Objective $1: ");
    return s.length > 46 ? s.slice(0, 44).replace(/\s+\S*$/, "") + "…" : s;
  }

  // ------------------------------------------------------------------ rescue (offered on the results screen)
  function rescueTargets() {
    var out = [];
    try {
      if (typeof QUESTIONS === "undefined" || typeof order === "undefined" || typeof answers === "undefined") return out;
      var miss = {}, ids = {};
      order.forEach(function (qi, i) {
        var q = QUESTIONS[qi]; ids[q.qid] = 1;
        if (answers[i] !== q.c) miss[q.io] = (miss[q.io] || 0) + 1;
      });
      Object.keys(miss).forEach(function (io) { if (miss[io] >= 3) out.push({ io: io, miss: miss[io], seen: ids }); });
      out.sort(function (a, b) { return b.miss - a.miss; });
    } catch (e) {}
    return out;
  }
  function startRescue(r) {
    context().then(function (c) {
      if (!c.here) return say("I don't have questions for this exam yet.");
      bankOf(c.here).then(function (b) {
        var pool = notOpen(b.q.filter(function (q) { return q.io === r.io; }));
        var fresh = pool.filter(function (q) { return !(r.seen && r.seen[q.id]); });
        var set5 = pickFresh(fresh, 5);
        if (set5.length < 5) set5 = set5.concat(pickFresh(pool.filter(function (q) { return set5.indexOf(q) < 0; }), 5 - set5.length));
        if (!set5.length) return say("I don't have more questions on that objective yet.");
        say("Rescue time: " + set5.length + " questions on " + shortIO(r.io) + ". Read each explanation, even when you get it right.");
        count("rescue");
        drill("Rescue: " + shortIO(r.io), set5, c.here);
      });
    });
  }
  function offerRescue() {
    context().then(function (c) { if (!c.herePast) offerRescueNow(); });
  }
  function offerRescueNow() {
    var res = document.getElementById("results"), list = rescueTargets();
    if (!res || !list.length || res.querySelector(".pip-rescue")) return;
    var box = el("div", "pip-rescue"), top = list[0];
    var t = el("span"); t.appendChild(el("b", null, "Pip: "));
    t.appendChild(document.createTextNode(shortIO(top.io) + " tripped you up " + top.miss + " times. Want a quick rescue?"));
    var b = el("button", null, "Rescue it: 5 questions"); b.type = "button";
    b.addEventListener("click", function () { open({ rescue: top }); });
    box.appendChild(t); box.appendChild(b);
    var anchor = res.querySelector(".breakdown");
    if (anchor) res.insertBefore(box, anchor); else res.appendChild(box);
  }

  // ------------------------------------------------------------------ the drill runner
  function drill(title, qs, folder) {
    var c = card(), i = 0, right = 0, misses = {}, answered = false, opts = [];
    c.classList.add("pw-drill");
    function show() {
      answered = false; c.textContent = "";
      var q = qs[i], meta = el("div", "pw-meta");
      meta.appendChild(el("span", null, title)); meta.appendChild(el("span", null, (i + 1) + " of " + qs.length));
      c.appendChild(meta);
      if (q.io) c.appendChild(el("div", "pw-io", shortIO(q.io)));
      c.appendChild(el("p", "pw-q", q.q));
      opts = q.o.map(function (o, k) {
        var b = el("button", "pw-opt"); b.type = "button";
        b.appendChild(el("span", "l", LTR[k])); b.appendChild(el("span", null, o[0]));
        b.addEventListener("click", function () { choose(k); });
        c.appendChild(b); return b;
      });
      drillActive = api; scrollTo(c);
    }
    function choose(k) {
      if (answered) return;
      answered = true;
      var q = qs[i], ok = k === q.c;
      if (ok) right++; else misses[q.io] = (misses[q.io] || 0) + 1;
      record(q.id, ok);
      opts.forEach(function (b, j) { b.disabled = true; if (j === q.c) b.classList.add("ok"); else if (j === k) b.classList.add("bad"); });
      P.react(ok ? "celebrate_small" : "concerned", 1);
      var v = el("div", "pw-verdict " + (ok ? "ok" : "bad"), ok ? "Correct." : "Not quite. The answer is " + LTR[q.c] + ".");
      c.appendChild(v);
      var ex = el("div", "pw-ex");
      q.o.forEach(function (o, j) { ex.appendChild(el("div", null, (j === q.c ? "✓ " : "✗ ") + LTR[j] + ". " + o[1])); });
      c.appendChild(ex);
      if (q.cite) c.appendChild(el("div", "pw-cite", q.cite));
      if (q.g) c.appendChild(linkTo(folder.f, q.g[0], q.g[1], "Find it in the study guide →"));
      var nx = el("button", "pw-next", i + 1 < qs.length ? "Next →" : "See how I did"); nx.type = "button";
      nx.addEventListener("click", next); c.appendChild(nx);
      if (folder.ex) {                         // Pip's plain-language explanation of the idea behind it
        var xb = el("button", "pw-chip pw-xbtn", "Explain the idea"); xb.type = "button";
        var at = i;
        xb.addEventListener("click", function () {
          xb.disabled = true;
          count("explain_tap");
          explainQuestion(q, folder, c, nx).then(function (m) {
            if (at !== i) return;
            xb.remove();
            if (m) helpful(m);
            if (m) scrollTo(m);
            else c.insertBefore(el("p", "pw-src", "I don't have my own explanation of this one yet. The explanations above and the guide link are the best place to start."), nx);
          });
        });
        c.appendChild(xb);
      }
      scrollTo(v); nx.focus({ preventScroll: true });
    }
    function next() { if (!answered) return; i++; if (i < qs.length) show(); else finish(); }
    function finish() {
      drillActive = null; c.textContent = "";
      c.appendChild(el("div", "pw-meta", title));
      c.appendChild(el("p", "pw-q", "You got " + right + " of " + qs.length + "."));
      var weakest = Object.keys(misses).sort(function (a, b) { return misses[b] - misses[a]; });
      weakest.slice(0, 3).forEach(function (io) {
        var row = el("div", "pw-bar"); row.appendChild(el("span", null, shortIO(io))); row.appendChild(el("span", null, misses[io] + " missed"));
        c.appendChild(row);
      });
      var pct = right / qs.length;
      P.react(pct >= 0.9 ? "celebrate_big" : pct >= 0.7 ? "proud" : "error_recover", 1);
      say(pct >= 0.9 ? "Excellent! That one's locked in." : pct >= 0.7 ? "Solid. A couple to tidy up." : "Good effort. Those explanations are where the points are.");
      var list = [["Another set", function () { startPractice(folder, Math.max(5, qs.length)); }]];
      if (weakest.length) list.push(["Rescue: " + shortIO(weakest[0]), function () { startRescue({ io: weakest[0] }); }]);
      list.push(["Done", function () { close(); }, false]);
      chips(list);
      scrollTo(c);
    }
    function key(e) {
      var k = e.key.toLowerCase(), map = { "1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, a: 0, b: 1, c: 2, d: 3, e: 4, f: 5 };
      if (!answered && map[k] !== undefined && map[k] < qs[i].o.length) { choose(map[k]); return true; }
      if (answered && (k === "enter" || k === "arrowright")) { next(); return true; }
      return false;
    }
    var api = { key: key };
    chips([]);
    show();
  }
  function scrollLead(node) {                     // an answer's first line at the top of the conversation
    log.scrollTop = node.getBoundingClientRect().top - log.getBoundingClientRect().top + log.scrollTop - 8;
  }
  function scrollTo(node) {
    // measured against the conversation itself (offsetTop counts from the window, header included)
    var top = node.getBoundingClientRect().top - log.getBoundingClientRect().top + log.scrollTop - 8;
    if (top < log.scrollTop || top + node.offsetHeight > log.scrollTop + log.clientHeight) log.scrollTop = top;
  }

  window.PipWindow = { open: open, close: close, toggle: function () { if (isOpen) close(); else open(); }, isOpen: function () { return isOpen; }, offerRescue: offerRescue };
})();
