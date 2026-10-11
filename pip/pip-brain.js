/* Pip's brain on this laptop. Loaded by pip/pip-window.js only when it is needed.

   What it is: a small open model (Qwen3, Apache-2.0) that runs inside the browser on the
   laptop's own graphics chip through WebLLM (Apache-2.0). It downloads once (about 2.3 GB),
   then works offline. Nothing the student types leaves the computer.

   What it may do: put the study-guide passages Pip already found into a few plain
   sentences. Nothing else. It never sees the answer key and never writes questions.

   The guard (stage-2 content rule): an answer is shown only if every word of five or more
   letters and every number in it also appears in the passages or the student's question
   (apart from a short list of everyday words). Anything else, or a model that says the
   passages don't answer it, falls back to the passages themselves, which are always shown.

   Where it may run: laptops and desktops with WebGPU (and 16-bit shader support), on
   pa-quizzes.com or a local preview. Phones and tablets get the no-model Pip. */
(function () {
  "use strict";
  if (window.PipBrain) return;

  // web-llm's own one-file ES build (no imports of its own), fetched with its hash checked and run from
  // this page's origin, the same way Teach Pip loads pdf.js; the worker loads it the same way
  var LIB = "https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm@0.2.85/lib/index.js";
  var LIB_SRI = "sha384-rfElDdXnNkSgbLTTGiKHTrsetCVAYzzLZBD96/rZdD9XYvryEyShqz3ph8j+x7HH";
  var LIBS = "https://raw.githubusercontent.com/mlc-ai/binary-mlc-llm-libs/025bcaf3780fa8254f5e5efd3bfea0a5397248f4/web-llm-models/v0_2_84/base/";
  // pinned to exact commits, so what a student downloads never changes under them
  var TIERS = {
    lite: { name: "Lite", gb: 1.0, id: "Qwen3-1.7B-q4f16_1-MLC",
            model: "https://huggingface.co/mlc-ai/Qwen3-1.7B-q4f16_1-MLC/resolve/80b3abcec6c3b3f5355dc0cc99cc4fb578f192bc/",
            lib: LIBS + "Qwen3-1.7B-q4f16_1_cs1k-webgpu.wasm", vram: 2037 },
    standard: { name: "Standard", gb: 2.3, id: "Qwen3-4B-q4f16_1-MLC",
                model: "https://huggingface.co/mlc-ai/Qwen3-4B-q4f16_1-MLC/resolve/a5c9fab855e3ccbdfed2e7e69683d75f30332161/",
                lib: LIBS + "Qwen3-4B-q4f16_1_cs1k-webgpu.wasm", vram: 3432 }
  };
  // K_NO was the 14-day "Not now" of the old after-a-question offer. Since 2026-10-10 Pip asks at the
  // start of every open instead and "Not now" lasts for that open only (pip/pip-window.js), so nothing
  // reads it any more; a download that works still clears an old one.
  var K_TIER = "local:pip:brain", K_NO = "local:pip:brain:no";
  // WebLLM 0.2.83-0.2.85 can fail with "Object has already been disposed" and leave the graphics device
  // hung (mlc-ai/web-llm, fix merged upstream 2026-10-02, not yet released). A failed or stalled model
  // (a download, a first load or a summary) marks this computer's brain as broken for three days, so
  // Pip does not retry it on every question and does not ask to download it again; after that the
  // download card comes back, and a download that works clears the mark.
  var K_BROKE = "local:pip:brain:broke";
  var HOSTS = /^(pa-quizzes\.com|www\.pa-quizzes\.com|localhost|127\.0\.0\.1)$/;
  var me = document.currentScript;
  var HERE = new URL(".", me ? me.src : location.href).href;

  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { if (v == null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) {} }
  // anonymous usage counts (metrics.js): whether the model loaded on this laptop, nothing else
  function count(field) { try { if (window.PAMetrics) window.PAMetrics.add(field); } catch (e) {} }
  function config(t) {
    return { model_list: [{ model: t.model, model_id: t.id, model_lib: t.lib, vram_required_MB: t.vram,
                            low_resource_required: true, overrides: { context_window_size: 4096 } }] };
  }

  var lib = null;
  function webllm() {
    if (!lib) lib = fetch(LIB, { integrity: LIB_SRI, credentials: "omit", referrerPolicy: "no-referrer" })
      .then(function (r) { if (!r.ok) throw new Error("http " + r.status); return r.blob(); })
      .then(function (bl) { return import(URL.createObjectURL(new Blob([bl], { type: "text/javascript" }))); });
    lib.catch(function () { lib = null; });
    return lib;
  }

  // ------------------------------------------------------------------ can this device run it?
  var capCache = null;
  function capable() {
    if (capCache) return capCache;
    capCache = (async function () {
      if (!HOSTS.test(location.hostname)) return { ok: false, why: "host" };
      var touch = (navigator.maxTouchPoints || 0) > 1 || (window.matchMedia && window.matchMedia("(pointer: coarse)").matches);
      if (touch || /Android|iPhone|iPad|Mobile/i.test(navigator.userAgent)) return { ok: false, why: "phone" };
      if (!navigator.gpu) return { ok: false, why: "webgpu" };
      var a = null;
      try { a = await navigator.gpu.requestAdapter(); } catch (e) {}
      if (!a) return { ok: false, why: "webgpu" };
      if (!a.features.has("shader-f16")) return { ok: false, why: "f16" };
      var free = Infinity;
      try { var est = await navigator.storage.estimate(); free = (est.quota || 0) - (est.usage || 0); } catch (e) {}
      // Only Standard is offered: measured 2026-10-08 on 12 guide questions, Lite (Qwen3-1.7B)
      // got almost nothing past the guard and invented facts (statins "work on CYP3A4"), while
      // Standard (Qwen3-4B) passed about half, every one of them correct.
      var mem = navigator.deviceMemory;                  // Chrome reports at most 8; Safari reports nothing
      if (mem && mem < 8) return { ok: false, why: "memory" };
      if (free < 3e9) return { ok: false, why: "space" };
      return { ok: true, tiers: ["standard"] };
    })();
    return capCache;
  }
  function tier() { var t = get(K_TIER); return TIERS[t] ? t : null; }
  // kept only so a window script cached before 2026-10-10 still works (see K_NO above)
  function declinedRecently() { var t = +get(K_NO) || 0; return Date.now() - t < 14 * 864e5; }
  function broken() { var t = +get(K_BROKE) || 0; return Date.now() - t < 3 * 864e5; }
  function markBroken() { set(K_BROKE, String(Date.now())); }
  function decline() { set(K_NO, String(Date.now())); }

  // ------------------------------------------------------------------ loading
  var engine = null, loading = null, loadedTier = null;
  function load(t, onProgress) {
    if (engine && loadedTier === t) return Promise.resolve(engine);
    if (loading) return loading;
    if (engine && loadedTier !== t) { var old = engine; engine = null; loadedTier = null; old.unload().catch(function () {}); }
    var T = TIERS[t];
    loading = webllm().then(function (w) {
      var worker = new Worker(HERE + "pip-brain-worker.js", { type: "module" });
      return w.CreateWebWorkerMLCEngine(worker, T.id, {
        appConfig: config(T),
        initProgressCallback: function (r) { if (onProgress) onProgress(r.progress || 0, r.text || ""); }
      });
    }).then(function (e) { engine = e; loadedTier = t; loading = null; count("brain_ok"); return e; },
            function (err) { loading = null; count("brain_fail"); throw err; });
    return loading;
  }
  function install(t, onProgress) {
    return load(t, onProgress).then(function () {
      set(K_TIER, t); set(K_NO, null); set(K_BROKE, null);
      try { if (navigator.storage && navigator.storage.persist) navigator.storage.persist(); } catch (e) {}
      return true;
    });
  }
  function remove() {
    var t = tier(); set(K_TIER, null);
    var drop = engine ? engine.unload().catch(function () {}) : Promise.resolve();
    engine = null; loadedTier = null;
    if (!t) return drop;
    return drop.then(webllm).then(function (w) { return w.deleteModelAllInfoInCache(TIERS[t].id, config(TIERS[t])); }).catch(function () {});
  }

  // ------------------------------------------------------------------ the guard
  var COMMON = {};
  ("about above after again against along among another around because before being below between cannot could does doing " +
   "during each either enough every first found given helps however include includes including instead itself known later " +
   "least makes means might mostly mainly often other others otherwise rather really second should simply since small still " +
   "their there these thing things those though three through together under until usually using which while whose within " +
   "would yourself guide guides study simple simpler words answer question called common commonly generally especially " +
   "example likely related based different overall therefore plain short basically essentially refers describe described " +
   "explains remember focus check passage passages section sections important where whether typically specific " +
   "something someone anything right wrong point points part parts happen happens whole kind kinds " +
   // structure and units only: words that say what something IS made of or measured in, never
   // what it causes, means or treats (those must come from the passages)
   "consist consists consisting contain contains containing called named known seconds minutes hours weeks months years " +
   "measure measured value values number numbers list listed below above first second third").split(" ")
    .forEach(function (w) { COMMON[w] = 1; });
  function norm(s) { return String(s || "").toLowerCase().normalize("NFKD").replace(/[̀-ͯ]/g, ""); }
  function base(w) { return w.replace(/(ies)$/, "y").replace(/(ing|ed|es|s|ly)$/, ""); }
  // words that turn two facts into a cause and an effect: the answer may use them only where the
  // passages do (measured 2026-10-08: "PCR is useful for Mycobacterium BECAUSE a thermal cycler..."
  // passed the word check while joining two unrelated facts)
  var LINKS = ["because", "since", "therefore", "thus", "hence", "so that", "due to", "leads to", "lead to", "results in",
               "result in", "causes", "caused by", "which means", "means that", "as a result", "in order to", "responsible for"];
  function check(answer, sources) {
    var bag = {}, bases = {}, nums = {};
    norm(sources).split(/[^a-z0-9]+/).forEach(function (w) { if (!w) return; bag[w] = 1; bases[base(w)] = 1; if (/^\d/.test(w)) nums[w] = 1; });
    var bad = [];
    norm(answer).split(/[^a-z0-9]+/).forEach(function (w) {
      if (!w) return;
      if (/\d/.test(w)) { if (!nums[w] && !bag[w]) bad.push(w); return; }
      if (w.length < 5 || COMMON[w] || bag[w] || bases[base(w)]) return;
      bad.push(w);
    });
    var na = " " + norm(answer).replace(/[^a-z0-9]+/g, " ") + " ", ns = " " + norm(sources).replace(/[^a-z0-9]+/g, " ") + " ";
    LINKS.forEach(function (l) { if (na.indexOf(" " + l + " ") >= 0 && ns.indexOf(" " + l + " ") < 0) bad.push("[" + l + "]"); });
    return bad;
  }

  // ------------------------------------------------------------------ answering
  // Two ways of asking, measured 2026-10-08: the first rephrases with the passages' own
  // phrases; if the guard rejects that, the second picks the passages' own sentences.
  var SYSTEM = "You are Pip, a study buddy for physician assistant students. Answer the question in one or two sentences " +
    "built from the passages' exact phrases. Copy the key phrases word for word; you may add only small linking words such as " +
    "and, or, which, this, also. Never say one thing causes or explains another unless the passages say so. Never add a fact, number, drug, test or condition that is not in the passages. Never mention " +
    "lectures, professors, slides or section numbers. If the " +
    "passages do not answer the question, reply exactly: NOT_IN_GUIDE\n\nExample.\nPassages:\n[1] Loop diuretics block the " +
    "Na-K-2Cl cotransporter in the thick ascending limb; hypokalemia is the classic adverse effect.\nQuestion: what is the main " +
    "side effect of loop diuretics\nAnswer: The classic adverse effect of loop diuretics is hypokalemia; they block the " +
    "Na-K-2Cl cotransporter in the thick ascending limb.";
  var PICK = "Find the sentence in the passages that best answers the question. Reply with that sentence copied exactly, word " +
    "for word, and nothing else. You may add one more sentence from the passages if it is needed. If no sentence answers it, " +
    "reply exactly: NOT_IN_GUIDE";
  var queue = Promise.resolve();
  function summarize(question, passages, onProgress) {
    var t = tier();
    if (!t) return Promise.resolve({ ok: false, why: "not-installed" });
    var job = queue.then(function () { return load(t, onProgress); }).then(function (e) {
      var ctx = passages.map(function (p, i) { return "[" + (i + 1) + "] " + (p.title ? p.title + ": " : "") + String(p.text).slice(0, 900); }).join("\n\n");
      var src = passages.map(function (p) { return (p.title || "") + " " + p.text; }).join(" ") + " " + question;
      function ask(sys, temp, picking) {
        return e.chat.completions.create({
          messages: [{ role: "system", content: sys }, { role: "user", content: "Passages:\n" + ctx + "\n\nQuestion: " + question }],
          temperature: temp, top_p: 0.9, max_tokens: 200, extra_body: { enable_thinking: false }
        }).then(function (r) {
          var text = ((r.choices && r.choices[0] && r.choices[0].message && r.choices[0].message.content) || "")
            .replace(/<think>[\s\S]*?<\/think>/g, "").trim();
          if (!text || /NOT_IN_GUIDE/.test(text) || /passages? (do|does) not|not (mention|provide|contain|say)/i.test(text)) return { ok: false, why: "not-in-guide" };
          if (text.length > 700) return { ok: false, why: "too-long", text: text };
          // answers must stand on their own: no pointers back to lectures, slides or guide sections
          if (/\b(professor|lecturer|lecture|slide|section)s?\b|\bsee \d|\(\s*\d+\.\d+\s*\)|[“”"]/i.test(text)) return { ok: false, why: "points-elsewhere", text: text };
          if (picking && text.split(/\s+/).length < 8) return { ok: false, why: "fragment", text: text };
          var bad = check(text, src);
          return bad.length ? { ok: false, why: "unsupported", words: bad, text: text } : { ok: true, text: text };
        });
      }
      return ask(SYSTEM, 0.2).then(function (r) {
        // the model saying the passages don't answer it is trusted; only a guard failure gets a second try
        return r.ok || r.why === "not-in-guide" ? r : ask(PICK, 0.1, true).then(function (r2) { return r2.ok ? r2 : r; });
      });
    });
    queue = job.catch(function () {});
    return job;
  }

  window.PipBrain = { tiers: TIERS, capable: capable, tier: tier, install: install, remove: remove,
                      summarize: summarize, declinedRecently: declinedRecently, decline: decline,
                      broken: broken, markBroken: markBroken,
                      loaded: function () { return !!engine; }, _check: check,
                      // for measuring prompts on this machine only; runs on the local model, nothing leaves it
                      _raw: function (messages, opts, t) {
                        return load(t || tier()).then(function (e) {
                          return e.chat.completions.create(Object.assign({ messages: messages, temperature: 0.2, max_tokens: 220, extra_body: { enable_thinking: false } }, opts || {}));
                        }).then(function (r) { return (r.choices[0].message.content || "").replace(/<think>[\s\S]*?<\/think>/g, "").trim(); });
                      } };
})();
