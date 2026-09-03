#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tie every quiz question on the site to the Cram Sheet row that covers it.

Jaxon, 2026-09-02: "A personalised cram sheet ... generating one from your
misses — the rows you actually keep failing — is a different product from the
same template."

my-cram-sheet.html needs to turn a list of MISSED QUESTIONS into a list of
CRAM ROWS. The obvious join -- a question's `topic` against a row's term --
was measured first and is not good enough: it lands 79% on CMS Exam 1 but 7%
on Physiology Exam 2, because those quizzes put an instructional objective in
`topic` rather than a condition name. Site-wide it was 39%.

So the join is on CONTENT, not labels. Each row is a document (its term
weighted x3, plus its detail cell); each question is a query (topic, objective,
stem, the correct choice and its explanation); the match is TF-IDF cosine
within that exam's own rows. Measured over all 16,977 questions: 95% match at
0.16, 68% at 0.30, median 0.37. Spot-checking the 0.16-0.22 band showed real
misfires ("Brachial Plexus" landing on "Spinal cord blood supply"), so the
shipped cutoff is 0.28 -- a personalised sheet that quietly includes the wrong
rows is worse than one that includes fewer.

All of this happens HERE, at build time, because the runtime page then needs
nothing but localStorage and one small file per exam. Output:

  cram-personal/index.js      exam metadata + quiz-slug -> exam key
  cram-personal/<key>.js      that exam's rows, its section styling, and
                              map[quizslug] = [rowIndex per question, -1 if none]

Re-run after adding or changing any quiz or cram sheet.
"""
import glob, html, json, math, os, re, sys, unicodedata
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Folder -> semester comes from build_group_quizzes, which parses semesters.js.
# Imported rather than restated: that registry is the one source of truth for
# class-to-term, and a second copy here is exactly how the two drift apart.
from build_group_quizzes import semester_from_path

OUT = os.path.join(ROOT, "cram-personal")

CUTOFF = 0.28

# Jaxon, 2026-09-02: "You only have to do Semester 2 content and forward from
# here on out." A DENYLIST of the one finished term, not an allowlist of the
# live ones -- Spring 2027 and everything after should be picked up without
# anyone remembering to come back and add them here. See [[semester_1_frozen]].
FROZEN_SEMESTERS = {"summer-1-2026"}

# Deliberately short. These are the words a medical question stem is made of,
# so leaving them in makes every question look like every row.
STOP = set("""the a an of and in for to with vs versus is are be by on at or as from that this
it its not no than then when which what who whom how why all any both each more most other some
such only own same so too very can will just should now patient following best next likely
year old man woman presents presenting history exam finding findings would does did has have""".split())

SECTION = re.compile(
    r'<section class="topic" id="([^"]+)"[^>]*style="([^"]*)"[^>]*>(.*?)</section>', re.S)
SHEAD = re.compile(r'<h2>(.*?)</h2>', re.S)
ROW = re.compile(r'<tr>\s*<td class="(?:h|term)">(.*?)</td>\s*<td[^>]*>(.*?)</td>\s*</tr>', re.S)
BANK = re.compile(r'const (?:QUESTIONS|questions) = (\[.*?\]);', re.S)

SKIP_IN_NAME = ("cram-sheet", "study-guide", "chart", "guess-that-disease")


def slug(s):
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s.lower())).strip('-')


def words(s):
    s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
    s = unicodedata.normalize('NFKD', s).lower()
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    return [w for w in s.split() if len(w) > 2 and w not in STOP]


def question_text(q):
    """Both engines' schemas: native {q,opts,c} and the nine legacy
    {q,choices,answer,correct,why} files. Taking the CORRECT option and its
    explanation matters more than the stem -- that is where the fact lives."""
    parts = [q.get("topic", ""), q.get("io", ""), q.get("q", "")]
    opts, c = q.get("opts"), q.get("c")
    if isinstance(opts, list) and isinstance(c, int) and 0 <= c < len(opts):
        parts += [opts[c][0], opts[c][1] if len(opts[c]) > 1 else ""]
    elif isinstance(q.get("choices"), list):
        a = q.get("answer")
        if isinstance(a, int) and 0 <= a < len(q["choices"]):
            parts.append(q["choices"][a])
        parts += [q.get("correct", ""), q.get("why", "")]
    return " ".join(str(p) for p in parts)


def parse_cram(path):
    """Sections, their accent styling, and their rows -- in document order."""
    src = open(path, encoding="utf-8").read()
    sections, rows = [], []
    for m in SECTION.finditer(src):
        sid, style, body = m.group(1), m.group(2), m.group(3)
        h2 = SHEAD.search(body)
        # Entities decoded here, NOT left encoded: my-cram-sheet.html escapes the
        # title before inserting it, so a stored "&amp;" came out on screen as
        # literal "&amp;". Store plain text and let the page do the escaping.
        title = html.unescape(re.sub(r'<[^>]+>', '', h2.group(1))).strip() if h2 else sid
        first = len(rows)
        for r in ROW.finditer(body):
            rows.append({"t": r.group(1).strip(), "d": r.group(2).strip(), "s": len(sections)})
        if len(rows) == first:
            continue                      # a section with no term rows adds nothing
        sections.append({"id": sid, "title": title, "style": style})
    return sections, rows


def vectorise(rows):
    docs = [words(r["t"]) * 3 + words(r["d"]) for r in rows]
    df = Counter()
    for d in docs:
        df.update(set(d))
    n = len(docs)
    idf = {w: math.log(1 + n / (1 + df[w])) for w in df}
    vecs = []
    for d in docs:
        c = Counter(d)
        norm = math.sqrt(sum((v * idf.get(w, 0)) ** 2 for w, v in c.items())) or 1.0
        vecs.append({w: v * idf.get(w, 0) / norm for w, v in c.items()})
    return idf, vecs


def best_row(text, idf, vecs):
    c = Counter(words(text))
    norm = math.sqrt(sum((v * idf.get(w, 0)) ** 2 for w, v in c.items())) or 1.0
    q = {w: v * idf.get(w, 0) / norm for w, v in c.items() if w in idf}
    if not q:
        return -1, 0.0
    bi, bs = -1, 0.0
    for i, v in enumerate(vecs):
        s = 0.0
        for w, qv in q.items():
            rv = v.get(w)
            if rv:
                s += qv * rv
        if s > bs:
            bi, bs = i, s
    return bi, bs


def main():
    os.makedirs(OUT, exist_ok=True)
    sheets = sorted(glob.glob("*/*cram-sheet.html"))
    assert sheets, "no cram sheets found -- run from the repo root"
    index, quiz_map = {}, {}
    total_q = total_hit = 0

    skipped = []
    for sheet in sheets:
        folder = sheet.split("/")[0]
        sem = semester_from_path(sheet)
        if sem in FROZEN_SEMESTERS:
            skipped.append(folder)
            continue
        key = slug(folder)
        sections, rows = parse_cram(sheet)
        if not rows:
            print("  %-44s no parseable rows, skipped" % folder[:44])
            continue
        idf, vecs = vectorise(rows)

        mapping, nq, nhit = {}, 0, 0
        for qf in sorted(glob.glob(folder + "/*.html")):
            base = os.path.basename(qf).lower()
            if any(x in base for x in SKIP_IN_NAME):
                continue
            src = open(qf, encoding="utf-8").read()
            m = BANK.search(src)
            if not m:
                continue
            try:
                qs = json.loads(m.group(1))
            except Exception:
                continue
            qslug = slug(folder + "/" + os.path.basename(qf)[:-5])
            hits = []
            for q in qs:
                i, s = best_row(question_text(q), idf, vecs)
                hits.append(i if s >= CUTOFF else -1)
            if not any(h >= 0 for h in hits):
                continue
            mapping[qslug] = hits
            quiz_map[qslug] = key
            nq += len(hits)
            nhit += sum(1 for h in hits if h >= 0)

        payload = {"title": folder, "sections": sections, "rows": rows, "map": mapping}
        body = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
        with open(os.path.join(OUT, key + ".js"), "w", encoding="utf-8") as fh:
            fh.write("// AUTO-GENERATED by tools/build_cram_personal.py -- DO NOT EDIT BY HAND.\n")
            fh.write("(window.CRAM_PERSONAL=window.CRAM_PERSONAL||{})[%s]=%s;\n"
                     % (json.dumps(key), body))
        index[key] = {"title": folder, "rows": len(rows), "quizzes": len(mapping)}
        total_q += nq
        total_hit += nhit
        print("  %-44s %4d rows  %3d quizzes  %5d/%-5d questions tied (%.0f%%)"
              % (folder[:44], len(rows), len(mapping), nhit, nq,
                 100 * nhit / nq if nq else 0))

    with open(os.path.join(OUT, "index.js"), "w", encoding="utf-8") as fh:
        fh.write("// AUTO-GENERATED by tools/build_cram_personal.py -- DO NOT EDIT BY HAND.\n")
        fh.write("window.CRAM_PERSONAL_INDEX=%s;\n"
                 % json.dumps(index, ensure_ascii=False, separators=(",", ":")))
        fh.write("window.CRAM_PERSONAL_QUIZ=%s;\n"
                 % json.dumps(quiz_map, ensure_ascii=False, separators=(",", ":")))

    if skipped:
        print("\nskipped %d frozen-semester exam(s): %s"
              % (len(skipped), ", ".join(sorted(skipped))))
    # A rerun after the denylist changed must not leave last run's files behind.
    stale = [f for f in os.listdir(OUT)
             if f.endswith(".js") and f != "index.js" and f[:-3] not in index]
    for f in stale:
        os.remove(os.path.join(OUT, f))
    if stale:
        print("removed %d stale file(s): %s" % (len(stale), ", ".join(sorted(stale))))

    size = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT))
    print("\n%d exams, %d quizzes mapped, %d/%d questions tied (%.0f%%), %.0f KB total"
          % (len(index), len(quiz_map), total_hit, total_q,
             100 * total_hit / total_q if total_q else 0, size / 1024))
    print("index.js is %.0f KB" % (os.path.getsize(os.path.join(OUT, "index.js")) / 1024))


if __name__ == "__main__":
    main()
