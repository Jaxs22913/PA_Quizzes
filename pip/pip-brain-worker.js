// Pip's brain runs here, off the page's main thread, so the page never stutters while
// the model thinks. Started by pip/pip-brain.js as a module worker.
// web-llm's one-file ES build is fetched with its hash checked (same pin as pip-brain.js) and run
// from a blob URL; messages that arrive before it is ready wait in a queue.
const LIB = "https://cdn.jsdelivr.net/npm/@mlc-ai/web-llm@0.2.85/lib/index.js";
const LIB_SRI = "sha384-rfElDdXnNkSgbLTTGiKHTrsetCVAYzzLZBD96/rZdD9XYvryEyShqz3ph8j+x7HH";
let handler = null;
const waiting = [];
self.onmessage = (msg) => { if (handler) handler.onmessage(msg); else waiting.push(msg); };
(async () => {
  const r = await fetch(LIB, { integrity: LIB_SRI, credentials: "omit", referrerPolicy: "no-referrer" });
  if (!r.ok) throw new Error("web-llm http " + r.status);
  const url = URL.createObjectURL(new Blob([await r.blob()], { type: "text/javascript" }));
  const { WebWorkerMLCEngineHandler } = await import(url);
  handler = new WebWorkerMLCEngineHandler();
  waiting.splice(0).forEach((m) => handler.onmessage(m));
})();
