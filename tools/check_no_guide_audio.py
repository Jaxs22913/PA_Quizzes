#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""No page may ship pre-rendered read-aloud audio.

Jaxon, 13 September 2026: "Remove all audio stuff from the entire site and stop
creating that. We can save space there."

395 MB of pre-rendered guide narration was deleted that day -- 7,196 MP3s across
twelve Semester 1 guides, two neural voices each. The published site was about
900 MB against GitHub Pages' 1 GB limit, and generating the same for the nine
Semester 2 guides would have added roughly another 870 MB.

THE READ-ALOUD FEATURE ITSELF STILL WORKS. theme.js only uses pre-rendered files
when a guide carries data-audio-dir; with the attribute gone it falls through to
speakLive() and the browser's own speech synthesis, which costs no bytes. So
this gate removes the STORAGE, not the feature.

What it refuses:
  * any data-audio-dir attribute on any page
  * any directory named *-study-guide-audio
  * any stray .mp3 outside audio/, which holds the relax page's soundscape

tools/generate_guide_audio.py was deleted alongside this. If pre-rendered audio
is ever wanted again it is recoverable from git history -- but it should not
come back without a decision about where it is hosted, because the site does not
have room for it.
"""
import os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ALLOWED_AUDIO = {"audio/rain-on-window.mp3"}   # the relax page's soundscape


def main():
    bad = []

    for f in sorted(glob.glob(os.path.join(ROOT, "*", "*.html"))) + \
             sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        src = open(f, encoding="utf-8", errors="replace").read()
        if "data-audio-dir" in src:
            bad.append(("data-audio-dir attribute", os.path.relpath(f, ROOT)))

    for d in sorted(glob.glob(os.path.join(ROOT, "*", "*-study-guide-audio"))):
        bad.append(("pre-rendered audio directory", os.path.relpath(d, ROOT)))

    for ext in ("mp3", "wav", "ogg", "opus", "m4a", "aac"):
        for f in sorted(glob.glob(os.path.join(ROOT, "**", "*." + ext), recursive=True)):
            rel = os.path.relpath(f, ROOT).replace(os.sep, "/")
            if rel.startswith(".git/") or rel in ALLOWED_AUDIO:
                continue
            bad.append(("audio file", rel))

    for kind, where in bad:
        print("  %-28s %s" % (kind, where))
    print("\n%d violation(s); the site ships no pre-rendered read-aloud audio"
          % len(bad) if bad else
          "clean: the site ships no pre-rendered read-aloud audio")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
