#!/usr/bin/env python3
"""Transcribe a long lecture in chunks, writing results to disk as they finish.

lecture_transcript.py treats a recording as one atomic operation: it consumes
the whole faster-whisper generator, then writes. That is fine for 40 minutes and
wrong for 145. A run on a two-and-a-half-hour lecture reached minute 27 and then
the machine went to sleep; ten hours later it had produced nothing on disk,
because nothing is written until the generator finishes. The sleep was the
interruption, but the atomicity is what turned a pause into a total loss -- any
interruption at all would have done the same.

So: split the audio, transcribe each piece independently, and append each
piece's segments to disk the moment it lands.

  - Progress is durable. An interruption costs one chunk, not the whole run.
  - Re-running RESUMES: finished chunks are read back and skipped, which is
    what makes an overnight job on a laptop that sleeps actually viable.
  - A genuinely stuck chunk is bounded and visible rather than silent.

Chunk boundaries are placed at the QUIETEST point within a window either side of
each target, so a cut lands in a pause rather than mid-word. Boundaries are
still the weak spot of any chunked transcription, and putting them in silence is
what keeps a split sentence from becoming a garbled one.

Usage:
  python3 tools/transcribe_long.py <audio> --out <dir> --name <stem>
                                   [--model medium.en] [--chunk-min 10]
"""
import argparse, json, os, sys, time
import numpy as np

SR = 16000


def hhmmss(sec):
    m, s = divmod(int(sec), 60)
    h, m = divmod(m, 60)
    return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:d}:{s:02d}"


def decode(path):
    """Whole file as mono float32 at 16 kHz, via PyAV (no system ffmpeg needed)."""
    import av
    container = av.open(path)
    stream = container.streams.audio[0]
    rs = av.audio.resampler.AudioResampler(format="fltp", layout="mono", rate=SR)
    out = []
    for frame in container.decode(stream):
        for f in rs.resample(frame):
            out.append(f.to_ndarray().reshape(-1))
    return np.concatenate(out) if out else np.zeros(0, dtype=np.float32)


def quiet_split(x, target, window=20.0):
    """Sample index near `target` seconds sitting at the quietest point.

    Scans 20 ms frames within +-window and picks the lowest-energy one, so the
    cut lands in a pause. Falls back to the exact target if the window runs off
    either end of the audio.
    """
    lo = max(0, int((target - window) * SR))
    hi = min(len(x), int((target + window) * SR))
    if hi - lo < SR:
        return min(int(target * SR), len(x))
    step = int(0.02 * SR)
    seg = x[lo:hi]
    n = (len(seg) // step) * step
    frames = seg[:n].reshape(-1, step)
    energy = (frames.astype(np.float32) ** 2).mean(axis=1)
    return lo + int(np.argmin(energy)) * step


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("--out", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--model", default="medium.en")
    ap.add_argument("--chunk-min", type=float, default=10.0)
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    stem = os.path.join(a.out, a.name)
    partial = stem + ".chunks.jsonl"        # durable, one JSON line per chunk

    print("decoding audio…", flush=True)
    x = decode(a.audio)
    total = len(x) / SR
    print(f"  {hhmmss(total)} at {SR} Hz", flush=True)

    # chunk boundaries, each nudged into a nearby silence
    step = a.chunk_min * 60
    targets = [i * step for i in range(1, int(np.ceil(total / step)))]
    bounds = [0] + [quiet_split(x, t) for t in targets] + [len(x)]
    chunks = [(bounds[i], bounds[i + 1]) for i in range(len(bounds) - 1)]
    print(f"  {len(chunks)} chunks of about {a.chunk_min:g} minutes", flush=True)

    done = {}
    if os.path.exists(partial):
        for line in open(partial, encoding="utf-8"):
            try:
                rec = json.loads(line)
                done[rec["chunk"]] = rec["segments"]
            except Exception:
                pass                      # a torn final line is expected after a kill
        if done:
            print(f"  resuming: {len(done)} of {len(chunks)} chunks already done", flush=True)

    from faster_whisper import WhisperModel
    print(f"loading {a.model}…", flush=True)
    model = WhisperModel(a.model, device="cpu", compute_type="int8")

    t0 = time.time()
    fh = open(partial, "a", encoding="utf-8")
    for i, (s0, s1) in enumerate(chunks):
        if i in done:
            continue
        audio = x[s0:s1].astype(np.float32)
        offset = s0 / SR
        c0 = time.time()
        segments, _ = model.transcribe(audio, beam_size=5, language="en",
                                       vad_filter=True,
                                       vad_parameters=dict(min_silence_duration_ms=700))
        segs = [{"start": sg.start + offset, "end": sg.end + offset,
                 "text": sg.text.strip()} for sg in segments]
        # write BEFORE moving on -- this is the whole point of chunking
        fh.write(json.dumps({"chunk": i, "segments": segs}, ensure_ascii=False) + "\n")
        fh.flush()
        os.fsync(fh.fileno())
        done[i] = segs
        el = time.time() - c0
        span = (s1 - s0) / SR
        remaining = sum((b - aa) / SR for j, (aa, b) in enumerate(chunks) if j not in done)
        pace = span / el if el else 0
        print(f"  chunk {i+1}/{len(chunks)}  {hhmmss(offset)}-{hhmmss(s1/SR)}  "
              f"{len(segs):>3} segs  {pace:.1f}x  ~{hhmmss(remaining / max(pace, .01))} left",
              flush=True)
    fh.close()

    allsegs = [s for i in sorted(done) for s in done[i]]
    with open(stem + ".transcript.txt", "w", encoding="utf-8") as f:
        f.write(f"# {a.name}\n# {hhmmss(total)} · {len(allsegs)} segments\n\n")
        for s in allsegs:
            f.write(f"[{hhmmss(s['start'])}] {s['text']}\n")
    print(f"\nwrote {stem}.transcript.txt  ({len(allsegs)} segments, "
          f"{sum(len(s['text'].split()) for s in allsegs):,} words)")
    print(f"total {hhmmss(time.time() - t0)} for {hhmmss(total)} of audio")


if __name__ == "__main__":
    main()
