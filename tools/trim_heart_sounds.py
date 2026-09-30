#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cut the University of Michigan Heart Sound & Murmur Library recordings to 20-second excerpts.

The library (Judge and Mangrulkar, University of Michigan; CC BY-SA 3.0) ships each recording as a
one-minute mp3. The Physical Diagnosis 2 listening pages need about twenty seconds -- enough beats
to hear the pattern, a quarter of the download. Excerpting is an adaptation under the licence, so
the pages credit the excerpts as such and keep the CC BY-SA 3.0 notice.

    python3 tools/trim_heart_sounds.py SOURCE_DIR

SOURCE_DIR holds the library's 23 mp3s under their original names (01_apex_normal_s1_s2_supine_bell.mp3 ...).
Needs ffmpeg on PATH or the imageio-ffmpeg package; it stops rather than ship untrimmed files.
"""
import glob, os, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "Physical Diagnosis 2 Exam 2", "heart-sounds")
START, LENGTH = 1.0, 20.0


def ffmpeg():
    p = shutil.which("ffmpeg")
    if p:
        return p
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("no ffmpeg: install it or `pip install imageio-ffmpeg` -- refusing to continue")


def main(src):
    ff = ffmpeg()
    files = sorted(glob.glob(os.path.join(src, "[0-9][0-9]_*.mp3")))
    if len(files) != 23:
        sys.exit("expected the library's 23 recordings in %s, found %d" % (src, len(files)))
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for f in files:
        out = os.path.join(OUT, os.path.basename(f).replace("__", "_").replace("spilt", "split"))
        subprocess.run([ff, "-v", "error", "-y", "-ss", str(START), "-t", str(LENGTH), "-i", f, "-ac", "1",
                        "-c:a", "libmp3lame", "-b:a", "96k", "-map_metadata", "-1", out], check=True)
        total += os.path.getsize(out)
        print("%-58s %4d KB" % (os.path.basename(out), os.path.getsize(out) // 1024))
    print("%d files, %.1f MB" % (len(files), total / 1e6))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
