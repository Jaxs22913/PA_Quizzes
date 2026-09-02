#!/usr/bin/env python3
"""Transcribe BOTH Ocular Trauma segments, oldest first.

lecture_transcript.py --note takes the newest match, so a two-segment lecture
needs a driver. Segments are ordered by mtime and named -part1/-part2 in that
order; the ordering is then verified against the transcript text rather than
trusted, because Notability often writes several blobs in one batch and their
mtimes land within a second of each other (see [[pdm_exam_spec]]).

Sequential on purpose -- parallel runs just contend for the same cores.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lecture_transcript as LT

DEST = os.path.expanduser(
    "~/Desktop/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 2/recordings")
NEEDLE = "ocular trauma"

recs = [r for r in LT.notability_recordings(LT.DEFAULT_SINCE)
        if NEEDLE in r["title"].lower()]
recs.sort(key=lambda r: r["mtime"])          # oldest first
assert recs, "no Ocular Trauma recording found in Notability"
print("%d segment(s):" % len(recs))
for i, r in enumerate(recs, 1):
    print("  part%d  %.1f MB  mtime %s" % (i, r["size"] / 1048576, r["mtime"]))

for i, r in enumerate(recs, 1):
    name = "cms-l14-ocular-trauma-2026-08-31-part%d" % i
    print("\n=== part %d -> %s ===" % (i, name))
    segs, dur = LT.transcribe(r["path"], "medium.en")
    stem, nflags = LT.write_outputs(DEST, name, segs, dur, r["path"])
    print("wrote %s.transcript.txt  (%s, %d cue(s))" % (stem, dur, nflags))
