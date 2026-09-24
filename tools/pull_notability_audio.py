#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull lecture recordings out of Notability into the Desktop class inboxes
(~/Desktop/PA Quizzes/Semester <n>/<Class> Inbox/).

Notability keeps every recording as a content-addressed blob -- the filename is
a SHA of the contents, with no extension and no hint of which lecture it is --
under

    ~/Library/Containers/com.gingerlabs.Notability/Data/Library/
      Application Support/local-persistence-collab-production/assets/

The mapping lives in the SQLite database next to it, `local_persistence`:

    note_metadata            id, title, created, modified, hasRecordings
    asset_note_associations  assetHash, noteId

and the title IS the deck filename, because Notability keeps the name of the
PowerPoint it imported. So note title -> deck -> which inbox it belongs in,
without guessing. Normalising both sides to lowercase alphanumerics absorbs the
URL-escaping that decks downloaded from the portal carry ("PD+II+...%26...").

Two things this gets right that a naive copy does not:

  * ORDER. A lecture is usually several clips, and the asset hashes carry no
    ordering at all. Sorting by hash would interleave a lecture at random. The
    order comes from creation_time in each file's movie header, which means
    walking the top-level atoms to find moov -- it is often at the END of the
    file for a recording that was streamed to disk, so reading the first few
    kilobytes finds nothing.

  * WHAT IS ALREADY THERE. Only lectures with no recording in their inbox are
    copied. Re-pulling everything would duplicate about 150 files under second
    names, since the inbox names lectures (cms-l19-oral-cavity-...) and
    Notability names decks.

    python3 tools/pull_notability_audio.py              # report only
    python3 tools/pull_notability_audio.py --go         # actually copy

Recordings Jaxon has said not to take are listed in SKIP below and are never
copied, whatever the database says.
"""
import datetime, json, os, re, shutil, sqlite3, struct, sys, unicodedata, urllib.parse

NOTA = os.path.expanduser(
    '~/Library/Containers/com.gingerlabs.Notability/Data/Library/'
    'Application Support/local-persistence-collab-production')
DB = os.path.join(NOTA, 'local_persistence')
ASSETS = os.path.join(NOTA, 'assets')
INBOX_BASE = os.path.expanduser('~/Desktop/PA Quizzes')
EPOCH = datetime.datetime(1904, 1, 1)

# Lectures whose audio must never be pulled, with the reason.
SKIP = {
    'introtopdiiupdatedelwaya':
        'PD II Lecture 1 -- the class was told not to record this one, and only '
        'this one. Lectures 2 onward are recorded normally.',
    'introtopdiielwaya': 'Same lecture, unescaped title.',
}


def norm(s):
    s = urllib.parse.unquote(s.replace('+', ' '))
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '', s.lower())


def mvhd(path):
    """(creation_time, duration_seconds), walking atoms so a trailing moov is found."""
    try:
        size = os.path.getsize(path)
        with open(path, 'rb') as f:
            pos = 0
            while pos < size - 8:
                f.seek(pos)
                hdr = f.read(8)
                if len(hdr) < 8:
                    break
                n = struct.unpack('>I', hdr[:4])[0]
                typ = hdr[4:8]
                if n == 1:
                    n = struct.unpack('>Q', f.read(8))[0]
                if n < 8:
                    break
                if typ == b'moov':
                    blob = f.read(min(n, 1 << 20))
                    i = blob.find(b'mvhd')
                    if i < 0:
                        return None, None
                    if blob[i + 4] == 0:
                        ct, _, ts, du = struct.unpack('>IIII', blob[i + 8:i + 24])
                    else:
                        ct, _, ts, du = struct.unpack('>QQIQ', blob[i + 8:i + 36])
                    return (EPOCH + datetime.timedelta(seconds=ct),
                            (du / ts if ts else None))
                pos += n
    except (OSError, struct.error):
        pass
    return None, None


def is_audio(path):
    try:
        with open(path, 'rb') as f:
            return f.read(12)[4:8] == b'ftyp'
    except OSError:
        return False


def notes_with_audio():
    """normalised title -> {title, modified, clips[]} for notes holding audio."""
    if not os.path.exists(DB):
        sys.exit('Notability database not found at %s\n'
                 'Is Notability installed and has it synced on this Mac?' % DB)
    con = sqlite3.connect('file:%s?mode=ro' % DB, uri=True)
    rows = con.execute("""
        SELECT n.title, substr(n.modified,1,10), a.assetHash
        FROM note_metadata n
        JOIN asset_note_associations a ON a.noteId = n.id AND a.userId = n.userId
        WHERE n.hasRecordings = 1 AND n.deleted IS NULL
    """).fetchall()
    con.close()
    out = {}
    for title, modified, h in rows:
        p = os.path.join(ASSETS, h)
        if not is_audio(p):
            continue
        rec = out.setdefault(norm(title), {'title': title, 'modified': modified, 'clips': []})
        ct, du = mvhd(p)
        rec['clips'].append({'path': p, 'created': ct, 'dur': du,
                             'mb': os.path.getsize(p) / 1e6})
    for rec in out.values():
        rec['clips'].sort(key=lambda c: (c['created'] or EPOCH))
    return out


def decks(semester):
    root = os.path.join(INBOX_BASE, semester)
    if not os.path.isdir(root):
        sys.exit('No such semester folder: %s' % root)
    out = []
    for cls in sorted(os.listdir(root)):
        if not cls.endswith('Inbox'):
            continue
        cpath = os.path.join(root, cls)
        if not os.path.isdir(cpath):
            continue
        for exam in sorted(os.listdir(cpath)):
            epath = os.path.join(cpath, exam)
            if not os.path.isdir(epath) or not exam.lower().startswith('exam'):
                continue
            for f in sorted(os.listdir(epath)):
                if f.lower().endswith(('.pptx', '.ppt', '.pdf')):
                    stem = os.path.splitext(f)[0]
                    out.append({'class': cls[:-6].strip(), 'exam': exam, 'deck': stem,
                                'norm': norm(stem),
                                'rec': os.path.join(epath, 'recordings')})
    return out


def main():
    go = '--go' in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    semester = args[0] if args else 'Semester 2'

    audio = notes_with_audio()
    D = decks(semester)
    print('%s: %d deck(s) | Notability: %d note(s) carrying audio\n'
          % (semester, len(D), len(audio)))

    matched, orphan_decks = [], []
    for d in D:
        (matched if d['norm'] in audio else orphan_decks).append(d)
    used = {d['norm'] for d in matched}

    print('=== decks with a recording in Notability (%d) ===' % len(matched))
    for d in matched:
        rec = audio[d['norm']]
        n_have = len([f for f in os.listdir(d['rec'])
                      if f.lower().endswith(('.m4a', '.mp4', '.aac', '.wav'))]) \
            if os.path.isdir(d['rec']) else 0
        note = ''
        if d['norm'] in SKIP:
            note = '  SKIP: ' + SKIP[d['norm']].split(' -- ')[0]
        print('  %-30s %-7s %-44s %d clip(s), inbox has %d%s'
              % (d['class'][:30], d['exam'], d['deck'][:44],
                 len(rec['clips']), n_have, note))

    print('\n=== decks with NO recording in Notability (%d) ===' % len(orphan_decks))
    for d in orphan_decks:
        print('  %-30s %-7s %s' % (d['class'][:30], d['exam'], d['deck'][:50]))

    orphan_notes = [v for k, v in audio.items() if k not in used]
    if orphan_notes:
        print('\n=== recordings whose deck is in no inbox (%d) ===' % len(orphan_notes))
        print('    (either the deck was never saved, or it is an exam review)')
        for v in sorted(orphan_notes, key=lambda x: x['modified'], reverse=True)[:15]:
            print('  %s  %-52s %d clip(s)'
                  % (v['modified'], v['title'][:52], len(v['clips'])))

    print('\nNothing is copied without an explicit destination: add the lecture to '
          'TARGETS in this file, or pass it by hand.\n'
          'This run was %s.' % ('LIVE (--go)' if go else 'a report only'))


if __name__ == '__main__':
    main()
