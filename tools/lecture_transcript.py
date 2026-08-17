#!/usr/bin/env python3
"""Pull a lecture recording out of Notability and transcribe it.

Notability keeps every attachment as a content-addressed blob with a hex name
and NO extension, under

  ~/Library/Containers/com.gingerlabs.Notability/Data/Library/
      Application Support/local-persistence-collab-production/assets/

so searching for "*.m4a" finds nothing. Audio is identified here by magic
bytes, and the blob is mapped back to its note title (and folder) through the
app's own SQLite index in the same directory.

The index is COPIED to a temp dir before being read. Notability is usually
running and holds a write-ahead log; opening the live file read-only is asking
for trouble, and this tool has no business writing to it.

Usage
  # what have I recorded this semester?
  python3 tools/lecture_transcript.py --list

  # transcribe the newest recording into the class inbox
  python3 tools/lecture_transcript.py --latest \
      --class "Microbiology" --exam 1 --name "lecture-3-bacterial-genetics"

  # or pick one by note title (substring, case-insensitive)
  python3 tools/lecture_transcript.py --note "Micro L3" --class "Microbiology" --exam 1

  # or transcribe any audio file, skipping Notability entirely
  python3 tools/lecture_transcript.py --file ~/Desktop/rec.m4a --class "Microbiology" --exam 1

Writes three files into <Class> Inbox/Exam <N>/recordings/:
  <name>.m4a               the audio, copied out of Notability
  <name>.transcript.txt    timestamped, one line per segment
  <name>.flags.md          every emphasis / de-emphasis cue, with timestamps

NOTHING here goes into the PA_Quizzes repo. It is a public site -- a lecture
recording or its transcript is the professor's content and must not be
republished. The tool refuses to write inside the repo.
"""
import argparse, os, re, shutil, sqlite3, sys, tempfile, time
from datetime import datetime, date

NOTABILITY = os.path.expanduser(
    "~/Library/Containers/com.gingerlabs.Notability/Data/Library/"
    "Application Support/local-persistence-collab-production")
ASSETS = os.path.join(NOTABILITY, "assets")
INDEX = os.path.join(NOTABILITY, "local_persistence")

INBOX_ROOT = os.path.expanduser("~/Desktop/Semester 2")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Fall 2026 starts here; older recordings are last semester's and are noise.
# Matches semesters.js's fall-2026 start date.
DEFAULT_SINCE = "2026-08-17"

# ---------------------------------------------------------------- emphasis ---
# Tuned from how lecturers actually flag material out loud. These are the
# highest-signal cues in a transcript because they survive it perfectly -- a
# professor SAYING "this is on the exam" beats any amount of vocal stress.
# Extend as you learn each professor's phrasing; that is the point of keeping
# it a plain list.
EMPHASIS = [
    r"on the (exam|test)", r"will be tested", r"(exam|test) question",
    r"i(?:'ll| will) ask", r"you(?:'ll| will) see this",
    r"know this", r"you need to know", r"make sure you (know|understand)",
    r"remember (this|that)", r"if you remember one thing",
    r"high[- ]yield", r"cannot stress", r"can(?:'t| not) stress",
    r"pay attention", r"write (this|that) down", r"listen up", r"now listen",
    r"this is (key|important|critical)", r"the key (thing|point)",
    r"take[- ]home", r"bottom line", r"most common", r"classic(?:ally)?",
    r"hallmark", r"buzzword", r"pathognomonic", r"board(?:s)? (question|favorite)",
]
DEEMPHASIS = [
    r"won(?:'t| not) (be )?test", r"will not be tested", r"not testable",
    r"do(?:n't| not) worry about", r"you do(?:n't| not) need to know",
    r"not going to ask", r"for your information", r"just background",
    r"beyond the scope",
]
EMPH_RE = re.compile("|".join(EMPHASIS), re.I)
DEEMPH_RE = re.compile("|".join(DEEMPHASIS), re.I)


def hhmmss(sec):
    m, s = divmod(int(sec), 60)
    h, m = divmod(m, 60)
    return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:d}:{s:02d}"


# ---------------------------------------------------------------- discovery --
def is_audio(path):
    try:
        with open(path, "rb") as f:
            h = f.read(12)
    except OSError:
        return False
    return h[4:8] == b"ftyp" or h[:4] in (b"caff", b"RIFF", b"OggS") or h[:3] == b"ID3"


def notability_recordings(since=None):
    """Every audio blob, newest first, joined to its note title and folder."""
    if not os.path.isfile(INDEX):
        sys.exit("Notability index not found. Is Notability installed and synced?")
    tmp = tempfile.mkdtemp(prefix="notability-idx-")
    # the -wal carries recent writes; without it the copy reads as stale
    for suffix in ("", "-wal", "-shm"):
        src = INDEX + suffix
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(tmp, "idx" + suffix))
    db = sqlite3.connect(os.path.join(tmp, "idx"))
    db.row_factory = sqlite3.Row

    org = {r["id"]: (r["title"], r["parentId"])
           for r in db.execute("select id, title, parentId from organizers")}

    def folder_path(oid):
        parts, seen = [], set()
        while oid in org and oid not in seen:
            seen.add(oid)
            title, parent = org[oid]
            parts.append(title)
            oid = parent
        return " / ".join(reversed(parts)) or "—"

    member = {r["noteId"]: r["organizerId"]
              for r in db.execute("select noteId, organizerId from organizer_note_membership")}

    cutoff = None
    if since:
        cutoff = datetime.strptime(since, "%Y-%m-%d").timestamp()

    out = []
    for r in db.execute("""select a.assetHash h, n.title t, n.id nid
                           from asset_note_associations a
                           join note_metadata n on n.id = a.noteId"""):
        blob = os.path.join(ASSETS, r["h"])
        if not is_audio(blob):
            continue
        st = os.stat(blob)
        if cutoff and st.st_mtime < cutoff:
            continue
        out.append({"hash": r["h"], "path": blob, "title": r["t"] or "Untitled",
                    "folder": folder_path(member.get(r["nid"])),
                    "mtime": st.st_mtime, "size": st.st_size})
    db.close()
    shutil.rmtree(tmp, ignore_errors=True)
    out.sort(key=lambda r: -r["mtime"])
    return out


# -------------------------------------------------------------- transcribe ---
def transcribe(audio, model_name, language="en"):
    from faster_whisper import WhisperModel
    print(f"loading {model_name} (first run downloads the model)…", flush=True)
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    print("transcribing…", flush=True)
    t0 = time.time()
    segments, info = model.transcribe(audio, beam_size=5, language=language,
                                      vad_filter=True,
                                      vad_parameters=dict(min_silence_duration_ms=700))
    segs = [{"start": s.start, "end": s.end, "text": s.text.strip()} for s in segments]
    took = time.time() - t0
    dur = info.duration
    print(f"done: {hhmmss(dur)} of audio in {hhmmss(took)} "
          f"({dur / took:.1f}x realtime)", flush=True)
    return segs, dur


def find_flags(segs):
    hits = []
    for s in segs:
        for label, rx in (("EMPHASIS", EMPH_RE), ("skip", DEEMPH_RE)):
            m = rx.search(s["text"])
            if m:
                hits.append((s["start"], label, m.group(0), s["text"]))
    return hits


def write_outputs(dest, name, segs, dur, audio_src):
    os.makedirs(dest, exist_ok=True)
    stem = os.path.join(dest, name)

    ext = os.path.splitext(audio_src)[1] or ".m4a"
    shutil.copy2(audio_src, stem + ext)

    with open(stem + ".transcript.txt", "w", encoding="utf-8") as f:
        f.write(f"# {name}\n# {hhmmss(dur)} · transcribed {date.today()}\n\n")
        for s in segs:
            f.write(f"[{hhmmss(s['start'])}] {s['text']}\n")

    flags = find_flags(segs)
    words = sum(len(s["text"].split()) for s in segs)
    with open(stem + ".flags.md", "w", encoding="utf-8") as f:
        f.write(f"# Emphasis cues — {name}\n\n")
        f.write(f"- Length: {hhmmss(dur)}\n- Words: {words:,} "
                f"({words / (dur / 60):.0f} per minute)\n"
                f"- Cues found: {len(flags)}\n\n")
        if not flags:
            f.write("_No explicit cues matched. Either the lecturer does not flag "
                    "material out loud, or the pattern list needs their phrasing "
                    "added (see EMPHASIS in tools/lecture_transcript.py)._\n")
        for start, label, cue, text in flags:
            mark = "**EXAM**" if label == "EMPHASIS" else "_skip_"
            f.write(f"### [{hhmmss(start)}] {mark} — “{cue}”\n{text}\n\n")
    return stem, len(flags)


# -------------------------------------------------------------------- main ---
def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--list", action="store_true", help="list recordings and exit")
    src.add_argument("--latest", action="store_true", help="use the newest recording")
    src.add_argument("--note", help="pick by note title (substring, case-insensitive)")
    src.add_argument("--file", help="transcribe this audio file, ignore Notability")
    ap.add_argument("--class", dest="klass", help='e.g. "Microbiology"')
    ap.add_argument("--exam", type=int, help="exam block number")
    ap.add_argument("--name", help="output basename (default: derived from the note title)")
    ap.add_argument("--model", default="medium.en",
                    help="faster-whisper model (default medium.en; small.en is ~3x faster)")
    ap.add_argument("--since", default=DEFAULT_SINCE,
                    help=f"ignore recordings older than this (default {DEFAULT_SINCE}, "
                         "the start of Fall 2026)")
    ap.add_argument("--all", action="store_true", help="no date cutoff")
    a = ap.parse_args()

    if a.file:
        audio, title = os.path.expanduser(a.file), os.path.basename(a.file)
    else:
        recs = notability_recordings(None if a.all else a.since)
        if a.list or not (a.latest or a.note):
            if not recs:
                print(f"No recordings since {a.since}. "
                      f"Record one in Notability, or pass --all to see older ones.")
                return
            print(f"{len(recs)} recording(s) since {a.since}:\n")
            for r in recs:
                print(f"  {datetime.fromtimestamp(r['mtime']):%Y-%m-%d %H:%M}  "
                      f"{r['size'] / 1048576:7.1f} MB  {r['title'][:46]:<46} [{r['folder'][:30]}]")
            return
        if a.note:
            match = [r for r in recs if a.note.lower() in r["title"].lower()]
            if not match:
                sys.exit(f'No recording since {a.since} with a title matching "{a.note}".')
            rec = match[0]
        else:
            if not recs:
                sys.exit(f"No recordings since {a.since}.")
            rec = recs[0]
        audio, title = rec["path"], rec["title"]
        print(f"Using: {title}  ({rec['size'] / 1048576:.1f} MB, "
              f"{datetime.fromtimestamp(rec['mtime']):%Y-%m-%d %H:%M})")

    name = a.name or re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-") or "lecture"

    if a.klass and a.exam:
        dest = os.path.join(INBOX_ROOT, f"{a.klass} Inbox", f"Exam {a.exam}", "recordings")
    else:
        dest = os.path.join(os.path.expanduser("~/Desktop"), "Lecture Recordings")
        print(f"No --class/--exam given; writing to {dest}")

    # the site is public -- a recording must never land in the repo
    if os.path.abspath(dest).startswith(REPO + os.sep):
        sys.exit("Refusing to write inside the PA_Quizzes repo: it is a public site.")

    segs, dur = transcribe(audio, a.model)
    stem, nflags = write_outputs(dest, name, segs, dur, audio)
    print(f"\nwrote {stem}.transcript.txt")
    print(f"wrote {stem}.flags.md  ({nflags} cue(s))")


if __name__ == "__main__":
    main()
