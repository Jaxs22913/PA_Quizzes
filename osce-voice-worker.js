/* The free on-device voice (Kokoro, open source) for osce-practice.html, run in the background.

   On the page itself this work froze everything: about half a second to build the voice, then 4 to 7 seconds for
   each line it spoke (the station clock, the microphone and scrolling all stopped; measured 2026-10-26). Here the
   same work runs off the page's main thread, one line at a time.

   Two ways to run it (measured on a 10-core Mac, 2026-10-26; every clip below transcribed back word for word):
     fast  the graphics chip (WebGPU), full precision: about 330 MB once; a short line in about half a second
     slow  the processor (WebAssembly), 8-bit: about 90 MB once; about 1.5 s of work per second of speech
   The smaller graphics-chip versions (fp16, q4f16) are NOT used: their speech came out garbled ("I get scared of
   blood" for "I get short of breath when I walk up the stairs ...").

   In:  {type: "load", gpu}                     build the voice; gpu false = the slow way only (under 4 GB of
                                                memory, or a device whose tab died building the fast one)
        {type: "say", id, text, voice, epoch, low}   make one line's audio; low = only when nothing else waits (the
                                                page makes the patient's common short replies ahead this way)
        {type: "cancel", epoch}                 drop every queued line from an earlier epoch (the station ended)
   Out: {type: "progress", file, loaded, total} · {type: "building"} (fast way: downloaded, now building)
        {type: "ready", fast} · {type: "failed"}
        {type: "audio", id, wav}                a WAV file as an ArrayBuffer (transferred, not copied): 16-bit, with
                                                the model's silence cut (it pads every clip with about 0.4 s before
                                                and 0.5 s after the speech, measured 2026-10-26: dead air before
                                                the patient's first word and after every line)
        {type: "audio", id, error: true} · {type: "audio", id, skipped: true} */
import { KokoroTTS } from "https://cdn.jsdelivr.net/npm/kokoro-js@1.2.1/dist/kokoro.web.js";

var MODEL = "onnx-community/Kokoro-82M-v1.0-ONNX";
var loading = null, fast = false;
var high = [], low = [], working = false;   // one line at a time: every asked-for line before any made-ahead one
var epoch = 0;

function build(device, dtype) {
  return KokoroTTS.from_pretrained(MODEL, {
    dtype: dtype, device: device,
    progress_callback: function (p) {
      if (p && p.status === "progress" && p.total) self.postMessage({ type: "progress", file: p.file, loaded: p.loaded, total: p.total });
      // the model is in hand; building it on the graphics chip is the step that can exhaust a tablet tab's memory
      if (p && p.status === "done" && device === "webgpu" && /\.onnx$/.test(p.file || "")) self.postMessage({ type: "building" });
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

// the clip without the model's padding: from 40 ms before the first sound to 120 ms after the last
function trimmed(x, sr) {
  var win = Math.round(sr * 0.01), thr = 0.008, n = x.length, a, b;
  function loud(i) { for (var j = i, e = Math.min(n, i + win); j < e; j++) if (x[j] > thr || x[j] < -thr) return true; return false; }
  for (a = 0; a < n && !loud(a); a += win);
  if (a >= n) return x;
  for (b = n - win; b > a && !loud(b); b -= win);
  return x.subarray(Math.max(0, a - Math.round(sr * 0.04)), Math.min(n, b + win + Math.round(sr * 0.12)));
}
function wav16(x, sr) {
  var buf = new ArrayBuffer(44 + x.length * 2), v = new DataView(buf);
  function str(o, t) { for (var i = 0; i < t.length; i++) v.setUint8(o + i, t.charCodeAt(i)); }
  str(0, "RIFF"); v.setUint32(4, 36 + x.length * 2, true); str(8, "WAVE"); str(12, "fmt ");
  v.setUint32(16, 16, true); v.setUint16(20, 1, true); v.setUint16(22, 1, true); v.setUint32(24, sr, true);
  v.setUint32(28, sr * 2, true); v.setUint16(32, 2, true); v.setUint16(34, 16, true); str(36, "data"); v.setUint32(40, x.length * 2, true);
  for (var i = 0, o = 44; i < x.length; i++, o += 2) { var s = Math.max(-1, Math.min(1, x[i])); v.setInt16(o, s < 0 ? s * 0x8000 : s * 0x7fff, true); }
  return buf;
}
function pump() {
  if (working) return;
  var m = high.shift() || low.shift();
  if (!m) return;
  working = true;
  function next() { working = false; pump(); }
  if ((m.epoch || 0) < epoch) { self.postMessage({ type: "audio", id: m.id, skipped: true }); return next(); }
  load(false).then(function (tts) { return tts.generate(String(m.text || ""), { voice: m.voice }); }).then(function (a) {
    var wav = wav16(trimmed(a.audio, a.sampling_rate), a.sampling_rate);
    self.postMessage({ type: "audio", id: m.id, wav: wav }, [wav]);
  }).catch(function () { self.postMessage({ type: "audio", id: m.id, error: true }); }).then(next);
}

self.onmessage = function (e) {
  var m = e.data || {};
  if (m.type === "load") {
    load(!!m.gpu).then(function () { self.postMessage({ type: "ready", fast: fast }); }, function () { self.postMessage({ type: "failed" }); });
  } else if (m.type === "cancel") {
    epoch = Math.max(epoch, m.epoch || 0);
  } else if (m.type === "say") {
    (m.low ? low : high).push(m);
    pump();
  }
};
