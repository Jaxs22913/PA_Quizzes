#!/usr/bin/env python3
"""Daily check: for every lecture on the calendar today, did its deck and its
recording actually arrive?

Jaxon asked for this on 2026-08-18: on any day with lectures, tell him by 7pm
which ones are missing slides or audio, so the gap gets caught while it is still
recoverable rather than a week before the exam.

MATCHING IS PER-LECTURE, not per-class. A day with two lectures in one class
(which happens often — PD2 ran Intro at 1pm and Dermatology at 3pm on the day
this was written) has to be able to say WHICH one is missing. Two independent
signals are used and the stronger one wins:

  TITLE OVERLAP - distinctive words shared between the calendar title and the
      filename or Notability note title. "PDM I - Lecture #1 - Principles of
      Laboratory Medicine" against "1. Principles of Laboratory Diagnostics
      sv.pptx" shares {principles, laboratory}. Boilerplate is stripped first,
      because "lecture", "student", "2026" and the class's own abbreviation
      appear in nearly every title and would match everything to everything.

  TIME WINDOW - the calendar gives each lecture a start and end; a recording's
      window is derived from its file mtime minus its duration. This is the
      WEAKER signal and is treated as such: Notability writes segments in
      batches, so several blobs can share an mtime to the second and their
      derived start times are then fiction. It is used only to break ties
      between title candidates, never on its own.

Anything that matches nothing is reported as unmatched rather than being
silently attached to the nearest lecture — a wrong attribution is worse than an
admitted gap, because it reports a lecture as covered when it is not.

NO-RECORD EXCEPTIONS never count as missing audio, and their recordings are not
reported on at all.

Exit code 0 always; this is a report, not a gate.
"""
import os, re, json, sys, datetime, sqlite3, shutil, tempfile

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
CAL = os.path.join(ROOT, "calendar-data.js")
INBOX_ROOT = os.path.expanduser("~/Desktop/Semester 2")
NOTA = os.path.expanduser(
    "~/Library/Containers/com.gingerlabs.Notability/Data/Library/"
    "Application Support/local-persistence-collab-production")

CLASS_INBOX = {
    "cms-1": "Clinical Medicine and Surgery I Inbox",
    "pdm-1": "Principles of Diagnostic Medicine I Inbox",
    "microbiology": "Microbiology Inbox",
    "pharm-1": "Pharmacology I Inbox",
    "physical-diagnosis-2": "Physical Diagnosis 2 Inbox",
    "clin-path-1": "Clinical Pathophysiology I Inbox",
    "med-lit": "Interpretation of Medical Literature Inbox",
}
CLASS_LABEL = {
    "cms-1": "Clinical Medicine and Surgery I", "pdm-1": "PDM I",
    "microbiology": "Microbiology", "pharm-1": "Pharmacology I",
    "physical-diagnosis-2": "Physical Diagnosis 2",
    "clin-path-1": "Clin Path I", "med-lit": "Med Lit",
}
NO_RECORD = {("physical-diagnosis-2", 1): "class was told not to record this one"}

# A Notability note title belongs to exactly one class. This has to be decided
# BEFORE per-lecture matching: on 2026-08-18 both Clin Path and PD2 ran a
# lecture called Dermatology, and matching on the topic word alone handed Clin
# Path's recording to PD2 -- reporting a lecture as covered that had not been
# recorded at all. Topic words are never sufficient; the note has to name its
# course. Ordered, first hit wins.
NOTE_CLASS = [
    ("clin-path-1", ["pathophys", "clin path", "clinpath"]),
    ("pdm-1", ["principles of laboratory", "diagnostic medicine", "pdm",
               "electrocardiog", " ekg", "urinalysis", "coagulation"]),
    ("physical-diagnosis-2", ["pd ii", "pdii", "physical diagnosis ii",
                              "pd 2", "physical diagnosis 2"]),
    ("cms-1", ["cms", "clinical medicine"]),
    ("pharm-1", ["pharm"]),
    # TOPIC words are not COURSE names. "bacteri", "virus", "fungi" and
    # "parasite" all describe things CMS teaches too, and "bacteri" routed CMS's
    # "4. Cutaneous Bacterial Infections" recording to Microbiology, where no
    # lecture claimed it -- so CMS Lecture 4 reported no audio while the file sat
    # on disk. Hints must identify the COURSE; anything unlabelled now competes
    # across every class on title overlap anyway, so a narrow hint costs nothing.
    ("microbiology", ["micro", "microbiology"]),
    ("med-lit", ["literature", "med lit", "evidence"]),
]


def clip_class(note):
    t = (note or "").lower().replace("+", " ")
    for cid, hints in NOTE_CLASS:
        if any(h in t for h in hints):
            return cid
    return None

DECK_EXT = (".pptx", ".ppt", ".pdf", ".docx", ".doc", ".key")

# Words that appear in nearly every title and so discriminate nothing.
STOP = set("""lecture lec class session student sv copy final draft updated new
the a an and or of for to in on with de la 2024 2025 2026 2027 fall spring summer
i ii iii iv v vi vii viii ix x tbd part pt professor prof dr am pm
note notes jan feb mar apr may jun jul aug sep sept oct nov dec
january february march april june july august september october november
december""".split())
CLASS_TOKENS = set("""pdm pd cms micro microbiology pharm pharmacology path
pathophysiology pathophys clin clinical diagnosis diagnostic medicine surgery
literature""".split())


def toks(s):
    s = (s or "").lower().replace("+", " ")
    s = re.sub(r"\.(pptx?|pdf|docx?|key|m4a|txt|md)\b", " ", s)   # extensions are not content
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return {w for w in s.split() if len(w) > 2 and w not in STOP}


def _same(x, y):
    """Tokens match exactly, or one is a prefix of the other with >=4 shared
    characters. Decks abbreviate where calendars do not -- "PD II Derm - Beck"
    against "LECTURE #2 - Dermatology" shares no exact word, and treating those
    as unrelated reported a deck that was sitting right there as missing."""
    if x == y:
        return True
    a, b = (x, y) if len(x) <= len(y) else (y, x)
    return len(a) >= 4 and b.startswith(a)


def overlap(a, b):
    """Distinctive-word overlap, ignoring words that name the class itself."""
    ta, tb = toks(a) - CLASS_TOKENS, toks(b) - CLASS_TOKENS
    if not ta or not tb:
        return 0.0
    hits = sum(1 for x in ta if any(_same(x, y) for y in tb))
    return hits / min(len(ta), len(tb))


# THE LECTURE NUMBER IS THE DISCRIMINATOR, and toks() throws it away: digits and
# roman numerals are shorter than the 3-character floor or sit in STOP. So
# "2. General Dermatology I" and "3. Dermatology II" both reduce to
# {general, dermatology} / {dermatology}, tie against both lectures, and one
# lecture ends up with two decks while the next reports none -- which is what
# 2026-08-19 did, flagging a deck and two recordings that were all on disk.
_ROMAN = {"i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5, "vi": 6, "vii": 7,
          "viii": 8, "ix": 9, "x": 10, "xi": 11, "xii": 12}


def lecture_no(text):
    """The lecture number a title claims, or None."""
    t = (text or "").lower()
    m = re.search(r"lecture\s*#?\s*(\d{1,2})", t)
    if m:
        return int(m.group(1))
    m = re.match(r"\s*(\d{1,2})\s*[.)-]", t)          # "6. Fungal and Viral..."
    if m:
        return int(m.group(1))
    return None


def number_agreement(a, b):
    """+1 when both name the same lecture, -1 when they disagree, 0 if unknown."""
    na, nb = lecture_no(a), lecture_no(b)
    if na is None or nb is None:
        return 0
    return 1 if na == nb else -1



def parse_hhmm(s, day):
    m = re.match(r"(\d{1,2}):(\d{2})(AM|PM)", (s or "").strip(), re.I)
    if not m:
        return None
    h, mi, ap = int(m.group(1)), int(m.group(2)), m.group(3).upper()
    if ap == "PM" and h != 12: h += 12
    if ap == "AM" and h == 12: h = 0
    return datetime.datetime.combine(day, datetime.time(h, mi))


def todays_lectures(today):
    src = open(CAL, encoding="utf-8").read()
    day = datetime.date.fromisoformat(today)
    out = []
    pat = (r'\{\s*d:"(\d{4}-\d{2}-\d{2})",\s*t:"(.*?)",\s*c:"([a-z0-9-]+)",\s*'
           r'k:"([a-z]+)"[^}]*?(?:h:"([^"]*)")?[^}]*?(?:e:"([^"]*)")?[^}]*\}')
    for m in re.finditer(pat, src):
        d, title, cid, kind, h, e = m.groups()
        if d != today or kind != "lecture":
            continue
        nm = re.search(r"(?:lecture|l)\s*#?\s*(\d+)", title, re.I)
        out.append({"title": title, "class": cid,
                    "num": int(nm.group(1)) if nm else None,
                    "start": parse_hhmm(h, day), "end": parse_hhmm(e, day)})
    return out


def decks_today(cid, today):
    folder = CLASS_INBOX.get(cid)
    if not folder:
        return []
    base = os.path.join(INBOX_ROOT, folder)
    if not os.path.isdir(base):
        return []
    hits = []
    for dirpath, _d, files in os.walk(base):
        low = os.path.basename(dirpath).lower()
        # recordings/ is where THIS tool's own output lands; counting it would
        # make the audit congratulate itself for files it created.
        if low.startswith("syllabus") or low == "recordings":
            continue
        for f in files:
            if f.startswith(".") or not f.lower().endswith(DECK_EXT):
                continue
            p = os.path.join(dirpath, f)
            try:
                # ON OR BEFORE the lecture day, not ON it. Professors post slides
                # in advance -- that is the normal case, not an anomaly. Requiring
                # mtime == today reported three decks as missing on 2026-08-20
                # that had been sitting in the inbox since the 19th, which is most
                # of what this check is supposed to reassure you about.
                if datetime.date.fromtimestamp(os.path.getmtime(p)).isoformat() <= today:
                    hits.append(f)
            except OSError:
                pass
    return hits


class AudioUnavailable(Exception):
    """Notability's container could not be read.

    macOS TCC guards ~/Library/Containers. A terminal usually holds Full Disk
    Access so this works by hand, but a LaunchAgent does not inherit it and gets
    EPERM. That must NOT look like "no recording was made" -- reporting a
    missing recording when the truth is a missing permission is the worst
    failure this tool could have, because it sends Jaxon hunting for audio that
    is sitting right there.
    """


def audio_today(today):
    """Audio blobs modified today: [{note, minutes, start, end}].

    Raises AudioUnavailable if the container cannot be read."""
    tmp = tempfile.mkdtemp()
    for a, b in (("local_persistence", "idx"), ("local_persistence-wal", "idx-wal"),
                 ("local_persistence-shm", "idx-shm")):
        p = os.path.join(NOTA, a)
        if os.path.exists(p):
            try:
                shutil.copy2(p, os.path.join(tmp, b))
            except PermissionError:
                shutil.rmtree(tmp, ignore_errors=True)
                raise AudioUnavailable(
                    "cannot read Notability's container -- grant Full Disk Access")
    idx = os.path.join(tmp, "idx")
    if not os.path.exists(idx):
        return []
    db = sqlite3.connect(idx); db.row_factory = sqlite3.Row
    assets = os.path.join(NOTA, "assets")
    out = []
    try:
        rows = db.execute("select a.assetHash h, n.title t from asset_note_associations a "
                          "join note_metadata n on n.id = a.noteId").fetchall()
    except sqlite3.Error:
        shutil.rmtree(tmp, ignore_errors=True); return []
    for r in rows:
        p = os.path.join(assets, r["h"])
        if not os.path.exists(p):
            continue
        try:
            mtime = os.path.getmtime(p)
            if datetime.date.fromtimestamp(mtime).isoformat() != today:
                continue
            with open(p, "rb") as fh:
                if b"ftyp" not in fh.read(12):
                    continue
        except OSError:
            continue
        mins = None
        try:
            import av
            c = av.open(p); mins = round(c.duration / av.time_base / 60, 1); c.close()
        except Exception:
            pass
        end = datetime.datetime.fromtimestamp(mtime)
        out.append({"note": r["t"] or "", "minutes": mins,
                    "start": end - datetime.timedelta(minutes=mins or 0), "end": end})
    shutil.rmtree(tmp, ignore_errors=True)
    return out


def window_overlaps(lec, clip):
    """Weak signal: does the clip's derived window sit inside the lecture slot?
    Generous by two hours each way, because batch-saved mtimes shift it."""
    if not lec["start"] or not lec["end"] or not clip["start"]:
        return False
    pad = datetime.timedelta(hours=2)
    return clip["start"] < lec["end"] + pad and clip["end"] > lec["start"] - pad


def assign(lectures, items, key):
    """Attach each item to its best-matching lecture. Title overlap decides;
    the time window only breaks ties. Unmatched items are returned, not forced."""
    out = {id(l): [] for l in lectures}
    unmatched = []
    for it in items:
        text = it if isinstance(it, str) else it["note"]
        scored = []
        for l in lectures:
            s = overlap(text, l["title"])
            if not isinstance(it, str) and window_overlaps(l, it):
                s += 0.15
            # A stated lecture number outranks fuzzy word overlap: agreeing is
            # near-proof, disagreeing is near-disproof.
            s += 0.60 * number_agreement(text, l["title"])
            scored.append((s, l))
        scored.sort(key=lambda x: -x[0])
        best, lec = scored[0]

        # AN UNTITLED RECORDING STILL HAPPENED. Notability's default name is
        # "Note Aug 17, 2026", which carries no content words at all -- title
        # overlap is 0 for every lecture, so it matched nothing and three
        # lectures reported no audio while their recordings sat on disk. When
        # there is no title to go on, the time window is the only signal, and it
        # is a good one: fall back to it rather than discarding the clip.
        if not isinstance(it, str) and not (toks(text) - CLASS_TOKENS):
            inwin = [l for l in lectures if window_overlaps(l, it)]
            if len(inwin) == 1:
                out[id(inwin[0])].append(it)
            else:
                unmatched.append("%s (%s min)" % (it["note"], it["minutes"]))
            continue

        if best >= 0.30:
            out[id(lec)].append(it)
        elif len(lectures) == 1 and best > 0:
            out[id(lectures[0])].append(it)
        else:
            unmatched.append(text if isinstance(it, str) else
                             "%s (%s min)" % (it["note"], it["minutes"]))
    return out, unmatched


def arrived_today(cid, today):
    """Decks whose mtime is the lecture day itself."""
    folder = CLASS_INBOX.get(cid)
    if not folder:
        return set()
    base = os.path.join(INBOX_ROOT, folder)
    out = set()
    for dirpath, _d, files in os.walk(base):
        low = os.path.basename(dirpath).lower()
        if low.startswith("syllabus") or low == "recordings":
            continue
        for f in files:
            if f.startswith(".") or not f.lower().endswith(DECK_EXT):
                continue
            try:
                if datetime.date.fromtimestamp(
                        os.path.getmtime(os.path.join(dirpath, f))).isoformat() == today:
                    out.add(f)
            except OSError:
                pass
    return out



def main():
    today = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    lectures = todays_lectures(today)
    rep = {"date": today, "lectures": len(lectures),
           "missing_deck": [], "missing_audio": [], "ok": [], "exempt": [],
           "unmatched_files": [], "unmatched_audio": []}
    if not lectures:
        print(json.dumps(rep)); return 0

    try:
        clips = audio_today(today)
    except AudioUnavailable as e:
        rep["audio_check_blocked"] = str(e)
        clips = []
    for c in clips:
        c["cid"] = clip_class(c["note"])
    by_class = {}
    for l in lectures:
        by_class.setdefault(l["class"], []).append(l)

    claimed = set()
    for cid, lecs in by_class.items():
        deck_map, deck_left = assign(lecs, decks_today(cid, today), "deck")
        # A recording whose title names no course still competes here on title
        # overlap. Notability names a note after the deck imported into it, so
        # "6. Fungal and Viral Skin Infections - Jaquith" carries no course word
        # at all -- and dropping those made every lecture on 2026-08-20 report
        # "no audio" while the recordings sat on disk. Course hints now narrow
        # the field when present and are simply absent when they are not.
        mine = [c for c in clips if c.get("cid") in (cid, None)]
        clip_map, clip_left = assign(lecs, mine, "audio")
        for l in lecs:
            for c in clip_map[id(l)]:
                claimed.add(id(c))
        # Only flag a deck that ARRIVED TODAY and matched nothing. Now that the
        # pool is every deck in the inbox rather than only today's, the folder
        # legitimately holds slides for other lectures, and listing those every
        # evening is precisely the always-fires ping this tool exists to avoid.
        rep["unmatched_files"] += ["%s: %s" % (CLASS_LABEL.get(cid, cid), x)
                                   for x in deck_left if x in arrived_today(cid, today)]

        for l in lecs:
            label = "%s — %s" % (CLASS_LABEL.get(cid, cid), l["title"][:72])
            got_deck = deck_map[id(l)]
            got_clips = clip_map[id(l)]
            exempt = NO_RECORD.get((cid, l["num"]))
            if not got_deck:
                rep["missing_deck"].append(label)
            if exempt:
                rep["exempt"].append("%s (%s)" % (label, exempt))
            elif not got_clips and not rep.get("audio_check_blocked"):
                rep["missing_audio"].append(label)
            if got_deck and (got_clips or exempt):
                mins = sum(c["minutes"] or 0 for c in got_clips)
                rep["ok"].append("%s%s" % (label,
                    "" if exempt else "  [%d segment(s), %.0f min]" % (len(got_clips), mins)))
    # Report a recording as unmatched only after EVERY class has had a chance at
    # it -- reporting per class listed the same clip once per course.
    rep["unmatched_audio"] += ["%s (%s min)" % (c["note"], c["minutes"])
                               for c in clips if id(c) not in claimed]
    print(json.dumps(rep, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
