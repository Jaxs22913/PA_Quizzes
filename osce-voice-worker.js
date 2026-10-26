/* The free on-device voice (Kokoro, open source) for osce-practice.html, run in the background.

   On the page itself this work froze everything: about half a second to build the voice, then 4 to 7 seconds for
   each line it spoke (the station clock, the microphone and scrolling all stopped; measured 2026-10-26). Here the
   same work runs off the page's main thread, one line at a time.

   Two ways to run it (measured on a 10-core Mac, 2026-10-26; every clip below transcribed back word for word):
     fast  the graphics chip (WebGPU), full precision: about 330 MB once; a short line in about half a second
     slow  the processor (WebAssembly), 8-bit: about 90 MB once; about 1.5 s of work per second of speech
   The smaller graphics-chip versions (fp16, q4f16) are NOT used: their speech came out garbled ("I get scared of
   blood" for "I get short of breath when I walk up the stairs ...").

   In:  {type: "load", gpu}                     build the voice; gpu false = the slow way only (phones, tablets)
        {type: "say", id, text, voice, epoch}   make one line's audio
        {type: "cancel", epoch}                 drop every queued line from an earlier epoch (the station ended)
   Out: {type: "progress", file, loaded, total} · {type: "ready", fast} · {type: "failed"}
        {type: "audio", id, wav}                a WAV file as an ArrayBuffer (transferred, not copied)
        {type: "audio", id, error: true} · {type: "audio", id, skipped: true} */
import { KokoroTTS } from "https://cdn.jsdelivr.net/npm/kokoro-js@1.2.1/dist/kokoro.web.js";

var MODEL = "onnx-community/Kokoro-82M-v1.0-ONNX";
var loading = null, fast = false;
var queue = Promise.resolve();   // the voice makes one line at a time, in the order they were asked for
var epoch = 0;

function build(device, dtype) {
  return KokoroTTS.from_pretrained(MODEL, {
    dtype: dtype, device: device,
    progress_callback: function (p) {
      if (p && p.status === "progress" && p.total) self.postMessage({ type: "progress", file: p.file, loaded: p.loaded, total: p.total });
    }
  });
}
function hasGpu() {
  if (!self.navigator || !navigator.gpu) return Promise.resolve(false);
  return navigator.gpu.requestAdapter().then(function (a) { return !!a; }, function () { return false; });
}
function load(gpu) {
  if (!loading) {
    loading = (gpu ? hasGpu() : Promise.resolve(false)).then(function (ok) {
      if (!ok) return build("wasm", "q8");
      // the first line on the graphics chip compiles its programs (1 to 2.5 s): do that now, not on the patient's first line
      return build("webgpu", "fp32").then(function (tts) {
        return tts.generate("Hello.", { voice: "af_heart" }).then(function () { fast = true; return tts; });
      }).catch(function () { fast = false; return build("wasm", "q8"); });
    });
    loading.catch(function () { loading = null; });
  }
  return loading;
}

self.onmessage = function (e) {
  var m = e.data || {};
  if (m.type === "load") {
    load(!!m.gpu).then(function () { self.postMessage({ type: "ready", fast: fast }); }, function () { self.postMessage({ type: "failed" }); });
  } else if (m.type === "cancel") {
    epoch = Math.max(epoch, m.epoch || 0);
  } else if (m.type === "say") {
    queue = queue.then(function () {
      if ((m.epoch || 0) < epoch) { self.postMessage({ type: "audio", id: m.id, skipped: true }); return; }
      return load(false).then(function (tts) { return tts.generate(String(m.text || ""), { voice: m.voice }); }).then(function (a) {
        var wav = a.toWav();
        self.postMessage({ type: "audio", id: m.id, wav: wav }, [wav]);
      });
    }).catch(function () { self.postMessage({ type: "audio", id: m.id, error: true }); });
  }
};
