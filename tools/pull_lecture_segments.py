#!/usr/bin/env python3
"""Pull ALL segments of one lecture out of Notability, in the right order.

lecture_transcript.py handles a single recording. Real lectures are not single
recordings -- a two-hour class stops for a break, or the app is paused, and
Notability writes each stretch as its own content-addressed blob. CMS Lecture 2
came out as four. Transcribing only the newest one silently loses most of the
lecture, and that is the failure this tool exists to prevent.

ORDERING IS THE WHOLE PROBLEM. Blob filenames are hashes and file mtimes are
when the blob was last touched, not when the audio was recorded -- they do not
reliably sort. `asr_job_metadata.creationTime` is epoch milliseconds at
recording START and does sort. Segments without a creationTime are reported
rather than guessed at.

Writes into "<Class> Inbox/Exam <N>/recordings/":
  <name>-seg<i>.m4a              each segment, in recording order
  <name>.notability.txt          Notability's OWN transcript, per segment
  <name>.transcript.txt          our transcription, segments concatenated
  <name>.flags.md                emphasis / de-emphasis cues with timestamps

Both transcripts on purpose: they disagree, and the disagreements are where the
interesting content is. See the standing rule about cross-examining them.

  python3 tools/pull_lecture_segments.py --list-notes
  python3 tools/pull_lecture_segments.py --note "Cutaneous Bacterial" \
      --class "Clinical Medicine and Surgery I" --exam 1 --name cms-l4-2026-08-19
  # inspect the segment list without transcribing (fast):
  python3 tools/pull_lecture_segments.py --note "..." --dry-run

NOTHING here goes into the PA_Quizzes repo. It is a public site; a lecture
recording and its transcript are the professor's content.
"""
import argparse, json, os, plistlib, shutil, sqlite3, sys, tempfile
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

NOTABILITY = os.path.expanduser(
    "~/Library/Containers/com.gingerlabs.Notability/Data/Library/"
    "Application Support/local-persistence-collab-production")
ASSETS = os.path.join(NOTABILITY, "assets")
ASR = os.path.join(NOTABILITY, "asr")
INDEX = os.path.join(NOTABILITY, "local_persistence")
INBOX_ROOT = os.path.expanduser("~/Desktop/Semester 2")


def open_index():
    """Copy the live index before reading it -- Notability holds a write-ahead
    log and this tool has no business touching the original."""
    tmp = tempfile.mkdtemp(prefix="nota-idx-")
    for suffix in ("", "-wal", "-shm"):
        src = INDEX + suffix
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(tmp, "idx" + suffix))
    return sqlite3.connect(os.path.join(tmp, "idx")), tmp


def segments(note_query, since_day=None):
    db, tmp = open_index()
    try:
        rows = db.execute("""
            SELECT j.hash, n.title, j.creationTime, j.duration, j.stage, j.fileSize
            FROM asr_job_metadata j
            JOIN asset_note_associations a ON a.assetHash = j.hash
            JOIN note_metadata n ON n.id = a.noteId
        """).fetchall()
    finally:
        db.close()
        shutil.rmtree(tmp, ignore_errors=True)

    out, undated = [], []
    for h, title, ctime, dur, stage, size in rows:
        if note_query and note_query.lower() not in (title or "").lower():
            continue
        path = os.path.join(ASSETS, h)
        if not os.path.exists(path):
            continue
        if ctime is None:
            undated.append((title, h[:8]))
            continue
        start = datetime.fromtimestamp(ctime / 1000)
        if since_day and start.strftime("%Y-%m-%d") < since_day:
            continue
        out.append(dict(hash=h, title=title, start=start,
                        mins=(dur or 0) / 60000.0, stage=stage,
                        size=size or os.path.getsize(path), path=path))
    out.sort(key=lambda r: r["start"])
    return out, undated


def notability_asr(h):
    """Notability's own transcript for a blob, if it has finished one. Stored
    as a plist under asr/ keyed by the same content hash."""
    for name in (h, h + ".plist"):
        p = os.path.join(ASR, name)
        if os.path.exists(p):
            try:
                with open(p, "rb") as f:
                    d = plistlib.load(f)
            except Exception:
                return None
            for key in ("transcript", "text", "fullText"):
                if isinstance(d, dict) and isinstance(d.get(key), str):
                    return d[key]
            if isinstance(d, dict):
                segs = d.get("segments") or d.get("results")
                if isinstance(segs, list):
                    parts = [s.get("text", "") for s in segs if isinstance(s, dict)]
                    if any(parts):
                        return " ".join(parts)
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list-notes", action="store_true",
                    help="list every note that has recordings, newest first")
    ap.add_argument("--note", help="note title substring, case-insensitive")
    ap.add_argument("--day", help="only segments recorded on this YYYY-MM-DD")
    ap.add_argument("--since", help="ignore segments recorded before this YYYY-MM-DD")
    ap.add_argument("--class", dest="klass")
    ap.add_argument("--exam", type=int)
    ap.add_argument("--name", help="output basename")
    ap.add_argument("--model", default="medium.en")
    ap.add_argument("--dry-run", action="store_true",
                    help="show the segment list and stop before transcribing")
    a = ap.parse_args()

    if a.list_notes:
        segs, undated = segments(None, a.since)
        by_note = {}
        for s in segs:
            by_note.setdefault(s["title"], []).append(s)
        for title, ss in sorted(by_note.items(), key=lambda kv: -kv[1][-1]["start"].timestamp()):
            total = sum(s["mins"] for s in ss)
            print("  %-46s %d seg  %6.1f min  %s -> %s"
                  % (title[:46], len(ss), total,
                     ss[0]["start"].strftime("%Y-%m-%d %H:%M"),
                     ss[-1]["start"].strftime("%H:%M")))
        if undated:
            print("\n  %d blob(s) with NO creationTime, not orderable: %s"
                  % (len(undated), ", ".join("%s/%s" % u for u in undated[:6])))
        return

    if not a.note:
        sys.exit("--note is required (or --list-notes)")
    segs, undated = segments(a.note, a.since)
    if a.day:
        segs = [s for s in segs if s["start"].strftime("%Y-%m-%d") == a.day]
    if not segs:
        sys.exit('No segments match "%s".' % a.note)

    print('"%s" -- %d segment(s), %.1f min total:'
          % (segs[0]["title"], len(segs), sum(s["mins"] for s in segs)))
    for i, s in enumerate(segs, 1):
        print("  seg%d  %s  %6.1f min  %5.1f MB  %s  %s"
              % (i, s["start"].strftime("%Y-%m-%d %H:%M:%S"), s["mins"],
                 s["size"] / 1048576, s["stage"], s["hash"][:8]))
    incomplete = [s for s in segs if s["stage"] != "completed"]
    if incomplete:
        print("  NOTE: %d segment(s) not marked completed -- Notability may still "
              "be processing them." % len(incomplete))
    if undated:
        print("  WARNING: %d blob(s) on this note have NO creationTime and were "
              "left out, because they cannot be placed in order." % len(undated))
    if a.dry_run:
        return

    if not (a.klass and a.exam and a.name):
        sys.exit("--class, --exam and --name are required to write output")
    dest = os.path.join(INBOX_ROOT, "%s Inbox" % a.klass, "Exam %d" % a.exam, "recordings")
    if os.path.abspath(dest).startswith(REPO + os.sep):
        sys.exit("Refusing to write inside the PA_Quizzes repo: it is a public site.")
    os.makedirs(dest, exist_ok=True)

    copied = []
    for i, s in enumerate(segs, 1):
        out = os.path.join(dest, "%s-seg%d.m4a" % (a.name, i))
        shutil.copy2(s["path"], out)
        copied.append(out)
    print("copied %d segment(s) into %s" % (len(copied), dest))

    # Notability's own transcript, kept for cross-examination
    nota = []
    for i, s in enumerate(segs, 1):
        t = notability_asr(s["hash"])
        nota.append("=== SEGMENT %d  (%s, %.1f min) ===\n%s"
                    % (i, s["start"].strftime("%Y-%m-%d %H:%M:%S"), s["mins"],
                       t or "(Notability has no transcript for this segment)"))
    open(os.path.join(dest, a.name + ".notability.txt"), "w", encoding="utf-8"
         ).write("\n\n".join(nota))
    got = sum(1 for n in nota if "has no transcript" not in n)
    print("wrote %s.notability.txt (%d of %d segments had one)" % (a.name, got, len(segs)))

    from lecture_transcript import transcribe, write_outputs, EMPHASIS, DEEMPHASIS  # noqa
    all_segs, offset, total = [], 0.0, 0.0
    for i, path in enumerate(copied, 1):
        print("\n--- transcribing segment %d of %d ---" % (i, len(copied)))
        s2, dur = transcribe(path, a.model)
        for seg in s2:
            seg = dict(seg) if isinstance(seg, dict) else seg
            all_segs.append(_shift(seg, offset))
        offset += dur
        total += dur
    stem, nflags = write_outputs(dest, a.name, all_segs, total, copied[0])
    print("\nwrote %s.transcript.txt (%.1f min across %d segments)" % (stem, total / 60, len(copied)))
    print("wrote %s.flags.md  (%d cue(s))" % (stem, nflags))
    print("\nNow read BOTH transcripts and diff them before trusting either.")


def _shift(seg, offset):
    """Segment timestamps restart at zero in every file; push each one past the
    segments before it so the combined transcript reads as one continuous
    lecture and a flag's timestamp means something."""
    if offset == 0:
        return seg
    if isinstance(seg, dict):
        s = dict(seg)
        for k in ("start", "end"):
            if k in s and s[k] is not None:
                s[k] = s[k] + offset
        return s
    start, end, text = seg
    return (start + offset, end + offset, text)


if __name__ == "__main__":
    main()
