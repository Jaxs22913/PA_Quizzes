#!/usr/bin/env python3
"""Transcribe today's lecture recordings, segment by segment, sequentially.

Three PDM segments and the Dermatology second half. Run SEQUENTIALLY rather than
in parallel: faster-whisper is CPU-bound and int8-quantised, so two runs on the
same machine do not go twice as fast, they contend and both slow down. This also
keeps the machine usable.

Segments are transcribed separately and stitched afterwards rather than
concatenated first, because a concatenated file would give one continuous
timeline that hides where the breaks fell -- and the breaks are exactly where
"we're about halfway through" style landmarks live.

Notability saved several of these in one batch, so their file mtimes are all
within a second of each other and the derived start times are unreliable. Order
here is by duration and content, verified from the transcripts afterwards, not
from mtime.
"""
import os, subprocess, sys, time

TOOL = "/Users/jaxonluke/Developer/PA_Quizzes/tools/lecture_transcript.py"
ASSETS = os.path.expanduser(
    "~/Library/Containers/com.gingerlabs.Notability/Data/Library/"
    "Application Support/local-persistence-collab-production/assets")

def blob(prefix):
    hits = [f for f in os.listdir(ASSETS) if f.startswith(prefix)]
    assert len(hits) == 1, "prefix %r matched %d blobs" % (prefix, len(hits))
    return os.path.join(ASSETS, hits[0])

JOBS = [
 # (blob prefix, class, exam, output name)
 ("488406ca4828e4", "Principles of Diagnostic Medicine I", 1, "lecture-1-lab-diagnostics-part1"),
 ("a5e187ada3bfb5", "Principles of Diagnostic Medicine I", 1, "lecture-1-lab-diagnostics-part2"),
 ("2bbd109bddbbdf", "Principles of Diagnostic Medicine I", 1, "lecture-1-lab-diagnostics-part3"),
 ("5e685380e0d1f2", "Clinical Pathophysiology I", 1, "lecture-2-dermatology-part2"),
]

if __name__ == "__main__":
    t0 = time.time()
    for i, (pref, klass, exam, name) in enumerate(JOBS, 1):
        src = blob(pref)
        mb = os.path.getsize(src) / 1e6
        print("\n=== [%d/%d] %s  (%.1f MB) ===" % (i, len(JOBS), name, mb), flush=True)
        r = subprocess.run([sys.executable, TOOL, "--file", src,
                            "--class", klass, "--exam", str(exam), "--name", name])
        if r.returncode != 0:
            print("!! %s FAILED (exit %d) -- continuing with the rest" % (name, r.returncode),
                  flush=True)
    print("\nall done in %.1f min" % ((time.time() - t0) / 60), flush=True)
