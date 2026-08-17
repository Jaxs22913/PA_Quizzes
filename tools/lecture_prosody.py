#!/usr/bin/env python3
"""Recover the emphasis channel a transcript throws away.

Reading a transcript tells you WHAT was said, never HOW. A sentence delivered
loudly, slowly, and bracketed by silence reads identically to every other
sentence. That channel is physically measurable, though, so this script measures
it and writes the numbers next to the words.

Four features per transcript segment, each scored against the speaker's OWN
rolling baseline rather than a global one -- a lecturer walks around, and mic
distance drifts over 50 minutes:

  pause_before  silence immediately before the segment. The single most reliable
                marker: deliberately leaving a gap is hard to do by accident.
  rate          words per second of VOICED time. Slowing down is deliberate.
  loudness      mean frame energy in dB. Real but the least trustworthy here,
                because distance from the mic moves it as much as intent does.
  pitch         median fundamental frequency, in semitones off baseline.

Pauses are measured from the AUDIO, not from segment boundaries. Whisper breaks
segments on punctuation and a 30-second window, which are model artifacts; a
real pause is a real silence.

Usage
  python3 tools/lecture_prosody.py <audio> <transcript.txt> [--top 25] [-o out.md]

The transcript must be the "[M:SS] text" format tools/lecture_transcript.py
writes. Output is a markdown file ranked by composite emphasis score.
"""
import argparse, os, re, sys
import numpy as np

SR = 16000          # whisper's rate; plenty for speech prosody
FRAME = 400         # 25 ms
HOP = 160           # 10 ms
F0_MIN, F0_MAX = 70, 300        # human speech fundamental
PAUSE_MIN = 0.30    # shorter than this is just articulation, not a pause
BASELINE_WIN = 90.0 # seconds each side for the rolling baseline


def hhmmss(sec):
    m, s = divmod(int(sec), 60)
    h, m = divmod(m, 60)
    return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:d}:{s:02d}"


def decode(path):
    """Mono float32 at SR, via PyAV so no system ffmpeg is needed."""
    import av
    container = av.open(path)
    stream = container.streams.audio[0]
    resampler = av.audio.resampler.AudioResampler(format="fltp", layout="mono", rate=SR)
    chunks = []
    for frame in container.decode(stream):
        for out in resampler.resample(frame):
            chunks.append(out.to_ndarray().reshape(-1))
    return np.concatenate(chunks) if chunks else np.zeros(0, dtype=np.float32)


def frames_of(x):
    """Overlapping frames as a view -- no copy, so 50 minutes stays cheap."""
    n = 1 + (len(x) - FRAME) // HOP
    return np.lib.stride_tricks.as_strided(
        x, shape=(n, FRAME), strides=(x.strides[0] * HOP, x.strides[0]))


def frame_energy_db(fr):
    rms = np.sqrt((fr.astype(np.float64) ** 2).mean(axis=1) + 1e-12)
    return 20.0 * np.log10(rms + 1e-12)


def voiced_mask(db):
    """Adaptive gate: noise floor from a low percentile, plus a margin.

    A fixed dB threshold fails the moment the recording level changes; taking
    the floor from the recording itself survives that.
    """
    floor = np.percentile(db, 10)
    speech = np.percentile(db, 85)
    thresh = floor + 0.35 * (speech - floor)
    return db > thresh, thresh


def pitch_track(x, fr, mask):
    """Median F0 per frame by autocorrelation, voiced frames only.

    Chunked because a 50-minute lecture is ~290k frames and doing the whole
    correlation at once would need gigabytes.
    """
    lag_lo, lag_hi = int(SR / F0_MAX), int(SR / F0_MIN)
    idx = np.flatnonzero(mask)
    f0 = np.full(len(fr), np.nan)
    CH = 4000
    for s in range(0, len(idx), CH):
        sel = idx[s:s + CH]
        block = fr[sel].astype(np.float64)
        block = block - block.mean(axis=1, keepdims=True)
        win = block * np.hanning(FRAME)
        n = 1 << (2 * FRAME - 1).bit_length()
        spec = np.fft.rfft(win, n=n)
        ac = np.fft.irfft(spec * np.conj(spec), n=n)[:, :lag_hi + 1]
        zero = ac[:, :1].copy()
        zero[zero == 0] = 1e-12
        ac = ac / zero
        seg = ac[:, lag_lo:lag_hi + 1]
        best = seg.argmax(axis=1) + lag_lo
        peak = seg.max(axis=1)
        good = peak > 0.30          # weak periodicity == unvoiced/noise
        f0[sel[good]] = SR / best[good]
    return f0


def rolling_baseline(times, values, win=BASELINE_WIN):
    """Median of the same feature within +-win seconds, excluding this point."""
    out = np.full(len(values), np.nan)
    for i, t in enumerate(times):
        lo, hi = np.searchsorted(times, [t - win, t + win])
        near = np.concatenate([values[lo:i], values[i + 1:hi]])
        near = near[~np.isnan(near)]
        if len(near) >= 5:
            out[i] = np.median(near)
    return out


def parse_transcript(path):
    segs = []
    for line in open(path, encoding="utf-8"):
        m = re.match(r"\[(?:(\d+):)?(\d+):(\d+)\]\s*(.*)", line.strip())
        if not m:
            continue
        h, mm, ss, text = m.groups()
        t = int(h or 0) * 3600 + int(mm) * 60 + int(ss)
        if text.strip():
            segs.append({"start": float(t), "text": text.strip()})
    for i, s in enumerate(segs):
        s["end"] = segs[i + 1]["start"] if i + 1 < len(segs) else s["start"] + 6.0
    return segs


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("audio")
    ap.add_argument("transcript")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("-o", "--out")
    a = ap.parse_args()

    segs = parse_transcript(a.transcript)
    if not segs:
        sys.exit("No '[M:SS] text' lines found in the transcript.")
    print(f"segments: {len(segs)}")

    print("decoding audio…", flush=True)
    x = decode(a.audio)
    print(f"  {len(x)/SR/60:.1f} minutes at {SR} Hz", flush=True)
    fr = frames_of(x)
    ftimes = np.arange(len(fr)) * HOP / SR
    print("measuring energy…", flush=True)
    db = frame_energy_db(fr)
    mask, thresh = voiced_mask(db)
    print(f"  voiced {100*mask.mean():.0f}% of frames (gate {thresh:.1f} dB)", flush=True)
    print("tracking pitch…", flush=True)
    f0 = pitch_track(x, fr, mask)
    print(f"  pitch found on {100*np.mean(~np.isnan(f0)):.0f}% of frames", flush=True)

    # silence runs -> pause lookup
    unvoiced = ~mask
    edges = np.diff(unvoiced.astype(np.int8))
    starts = np.flatnonzero(edges == 1) + 1
    ends = np.flatnonzero(edges == -1) + 1
    if unvoiced[0]:
        starts = np.r_[0, starts]
    if unvoiced[-1]:
        ends = np.r_[ends, len(unvoiced)]
    n = min(len(starts), len(ends))
    pauses = [(ftimes[s], ftimes[e - 1]) for s, e in zip(starts[:n], ends[:n])
              if ftimes[e - 1] - ftimes[s] >= PAUSE_MIN]
    print(f"  {len(pauses)} pauses >= {PAUSE_MIN}s", flush=True)
    pstart = np.array([p[0] for p in pauses]) if pauses else np.zeros(0)
    pend = np.array([p[1] for p in pauses]) if pauses else np.zeros(0)

    # per-segment features
    for s in segs:
        i0, i1 = np.searchsorted(ftimes, [s["start"], s["end"]])
        i1 = max(i1, i0 + 1)
        m = mask[i0:i1]
        voiced_s = m.sum() * HOP / SR
        s["voiced"] = voiced_s
        s["loud"] = float(np.mean(db[i0:i1][m])) if m.any() else np.nan
        seg_f0 = f0[i0:i1][~np.isnan(f0[i0:i1])]
        s["f0"] = float(np.median(seg_f0)) if len(seg_f0) >= 5 else np.nan
        s["rate"] = len(s["text"].split()) / voiced_s if voiced_s > 0.4 else np.nan
        # pause ending within 250 ms of this segment's start
        if len(pend):
            j = np.argmin(np.abs(pend - s["start"]))
            s["pause"] = (pend[j] - pstart[j]) if abs(pend[j] - s["start"]) < 0.25 else 0.0
        else:
            s["pause"] = 0.0

    t = np.array([s["start"] for s in segs])
    def z(key, invert=False):
        v = np.array([s[key] for s in segs], dtype=float)
        base = rolling_baseline(t, v)
        d = v - base
        sd = np.nanstd(d)
        zz = d / sd if sd > 0 else np.zeros_like(d)
        return -zz if invert else zz

    z_loud = z("loud")
    z_rate = z("rate", invert=True)      # SLOWER than baseline == emphasis
    zf = np.array([s["f0"] for s in segs], dtype=float)
    semis = 12 * np.log2(zf / rolling_baseline(t, zf))
    sd = np.nanstd(semis)
    z_pitch = semis / sd if sd > 0 else np.zeros_like(semis)
    pause = np.array([s["pause"] for s in segs])
    z_pause = pause / (np.std(pause) or 1.0)

    # weights follow how much each feature can be trusted on room audio
    W = {"pause": 1.0, "rate": 0.8, "loud": 0.6, "pitch": 0.4}
    score = (W["pause"] * np.nan_to_num(z_pause) + W["rate"] * np.nan_to_num(z_rate)
             + W["loud"] * np.nan_to_num(z_loud) + W["pitch"] * np.nan_to_num(z_pitch))
    for i, s in enumerate(segs):
        s.update(score=score[i], zl=z_loud[i], zr=z_rate[i], zp=z_pitch[i], zpa=z_pause[i])

    out = a.out or os.path.splitext(a.transcript)[0].replace(".transcript", "") + ".prosody.md"
    ranked = sorted(segs, key=lambda s: -s["score"])[:a.top]
    ranked.sort(key=lambda s: s["start"])
    with open(out, "w", encoding="utf-8") as f:
        f.write("# Prosodic emphasis\n\n")
        f.write(f"Measured from the audio: {len(segs)} segments, {len(pauses)} pauses "
                f"of {PAUSE_MIN}s or longer.\n\n")
        f.write("Each number is standard deviations from **this speaker's own** rolling "
                "baseline (±90 s), so mic drift does not masquerade as emphasis. "
                "`pause` is the silence immediately before the line, in seconds.\n\n")
        f.write("This is a *proxy*. It detects getting louder, slowing down and leaving "
                "a gap — which correlate with emphasis but are not the same thing. "
                "Weighted pause > rate > loudness > pitch, in that order of trust.\n\n")
        f.write("**A high score means the line was delivered with weight; a low score does "
                "NOT mean the content is unimportant.** Validated against the first real "
                "lecture: the bottom of the ranking holds genuine asides (\"I left space for "
                "notes\") but also real content rattled off fast. The clearest pattern is "
                "that a principle gets introduced slowly and its examples are then listed "
                "quickly — \"standard of care\" scored +6.1 being introduced and −5.4 thirty "
                "seconds later listing cases of it. Read this as where the speaker leaned "
                "in, not as a syllabus.\n\n")
        f.write("| time | score | pause | slower | louder | pitch | line |\n")
        f.write("|---|---|---|---|---|---|---|\n")
        for s in ranked:
            txt = s["text"].replace("|", "\\|")[:150]
            f.write(f"| {hhmmss(s['start'])} | {s['score']:.1f} | {s['pause']:.1f}s | "
                    f"{s['zr']:+.1f} | {s['zl']:+.1f} | {s['zp']:+.1f} | {txt} |\n")
    print(f"\nwrote {out}")
    for s in ranked[:8]:
        print(f"  [{hhmmss(s['start'])}] score {s['score']:.1f}  {s['text'][:88]}")


if __name__ == "__main__":
    main()
