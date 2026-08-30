"""Regenerate the Group Study question bank from EVERY quiz
on the site, so Group Study always mirrors the full quiz catalog with no manual
porting.

Run from the repo root after adding/changing any quiz:

    python3 tools/build_group_quizzes.py

It scans every quiz HTML file, extracts its `const QUESTIONS = [...]` array
(handling all of the site's quiz-engine schemas), converts each question to the
Group Study shape { q, choices[4], answer, exp }, and writes:

    group-quizzes/index.js  -> window.GROUP_INDEX  = { "<id>": {title, category, n} }
    group-quizzes/<id>.js   -> window.GROUP_QUIZZES["<id>"] = { title, category, questions:[...] }

Quizzes are keyed by a stable slug of their file path; `category` is the class
(the folder with any "Exam N" stripped) and drives the host picker's grouping.
Image-dependent quizzes are skipped (Group Study is text-only). This file is
the single source of truth -- do not hand-edit anything in group-quizzes/.
"""
import re, os, glob, json, sys, html
try:
    import json5  # tolerant parser: handles JS-object literals (unquoted keys, trailing commas)
    _loads = json5.loads
except ImportError:
    # Do NOT fall back to strict json.loads. On 2026-08-19 a run without json5
    # parsed only the quizzes whose banks are strict JSON and silently dropped
    # five older JS-literal ones (Physiology Exam 3 gi/hemostasis/immunology/
    # metabolism/pulmonary) out of Group Study. The run looked successful --
    # "skipped: 0" -- because those files never reached the skip counters.
    # A missing parser must stop the build, not quietly shrink the bank.
    sys.exit("build_group_quizzes needs json5 (pip install json5). Refusing to run "
             "without it: strict JSON silently drops every JS-object-literal quiz.")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SKIP_BASENAMES = {"index.html", "guides.html", "group-host.html", "group-join.html", "arcade.html"}
SKIP_SUBSTR = ["study-guide", "cram-sheet", "-blood-flow", "-flows", "-hormones", "-peritoneum"]


# The site's quiz engines store the question bank under different variable
# names (QUESTIONS, questions, Q, DECK...) and in either strict JSON or JS
# object-literal form. Try each candidate name, parse tolerantly, and accept
# the first array whose objects actually look like questions.
QVARS = ["QUESTIONS", "questions", "Q", "DECK", "ITEMS", "BANK", "quizData"]


def _looks_like_questions(arr):
    return isinstance(arr, list) and arr and isinstance(arr[0], dict) and \
        any(k in arr[0] for k in ("q", "question", "stem"))


def extract_questions(src):
    for var in QVARS:
        for decl in (r'\bconst ' + var + r'\s*=\s*', r'\b(?:let|var) ' + var + r'\s*=\s*'):
            m = re.search(decl + r'(\[.*?\]);', src, re.DOTALL)  # non-greedy first
            if not m:
                continue
            for text in (m.group(1),):
                try:
                    arr = _loads(text)
                    if _looks_like_questions(arr):
                        return arr
                except Exception:
                    pass
            # non-greedy can truncate on a stray "];" inside a string; retry greedy
            mg = re.search(decl + r'(\[.*\]);', src, re.DOTALL)
            if mg:
                try:
                    arr = _loads(mg.group(1))
                    if _looks_like_questions(arr):
                        return arr
                except Exception:
                    pass
    return None


def clean_title(src, fallback):
    m = re.search(r'<title>(.*?)</title>', src, re.DOTALL | re.IGNORECASE)
    t = html.unescape(re.sub(r'\s+', ' ', m.group(1)).strip()) if m else fallback
    # strip trailing " — <Class Exam N>" / " | site" boilerplate
    t = re.split(r'\s+[|]\s+', t)[0]
    return t or fallback


def exam_from_path(path):
    """The exam a quiz belongs to, taken from its folder rather than guessed
    from the slug. review.html groups by it so a student can drill just the
    exam they are sitting, and the folder is the only place that is authoritative
    -- "Anatomy Practicum Exam 3" and "Physical Diagnosis 1 Exam 2" do not share
    a slug shape."""
    folder = path.split(os.sep)[0]
    m = re.search(r'\bExam\s*(\d+)\s*$', folder)
    return ("Exam " + m.group(1)) if m else "General"


def category_from_path(path):
    folder = path.split(os.sep)[0]
    cat = re.sub(r'\s*Exam\s*\d+\s*$', '', folder).strip()
    cat = re.sub(r'\s*\d+\s*$', '', cat).strip() if re.search(r'\bDiagnosis\b', cat) else cat
    fixups = {
        "CAM Nutrition": "CAM / Nutrition", "Nutrition Class": "Nutrition",
        "Anatomy Practicum": "Anatomy Practicum", "Intro to PA Profession": "Intro to PA",
    }
    return fixups.get(cat, cat) or "Other"


def _semester_map():
    """Folder -> semester id, read out of semesters.js.

    The mapping is duplicated nowhere: this parses the same registry the pages
    use, so adding a class to a semester in one place updates the group manifest
    too. If the file ever moves or its shape changes, every quiz simply comes
    back with no semester and the picker shows them all -- the failure mode is
    "unfiltered", not "wrong semester".
    """
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "semesters.js")
    try:
        js = open(path, encoding="utf-8").read()
    except OSError:
        return [], {}
    folder_class = re.findall(r'\[/\^([^/]+)/i,\s*"([^"]+)"\]', js)
    class_sem = {}
    for block in re.finditer(r'id:\s*"([^"]+)".*?classes:\s*\[(.*?)\]', js, re.S):
        sid, classes = block.group(1), re.findall(r'"([^"]+)"', block.group(2))
        for c in classes:
            class_sem.setdefault(c, sid)
    return folder_class, class_sem


_FOLDER_CLASS, _CLASS_SEM = _semester_map()


def semester_from_path(path):
    folder = path.split(os.sep)[0]
    for pattern, class_id in _FOLDER_CLASS:
        if re.match(pattern, folder, re.I):
            return _CLASS_SEM.get(class_id)
    return None


def slug(s):
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s.lower())).strip('-')


def has_image(q):
    blob = json.dumps(q, ensure_ascii=False).lower()
    return any(k in blob for k in ('"img"', 'imgsrc', 'imgcaption', 'data-img', '.png', '.jpg', '.jpeg', '.webp'))


def _first(q, keys):
    for k in keys:
        if k in q and q[k] is not None:
            return q[k]
    return None


def convert(q):
    """Field-inferring conversion that works across every quiz-engine schema on
    the site (and, being inference-based, future ones too). Returns
    (qtext, choices, answer_index, exp) or None."""
    qtext = _first(q, ["q", "question", "stem", "prompt"])
    opts = _first(q, ["opts", "o", "options", "choices", "answers"])
    if qtext is None or opts is None:
        return None

    choices, embedded_ans = [], None
    letter_keys = None
    if isinstance(opts, dict):                       # {A:..,B:..}
        letter_keys = sorted(opts.keys())
        choices = [str(opts[k]) for k in letter_keys]
    elif isinstance(opts, list):
        for i, o in enumerate(opts):
            if isinstance(o, (list, tuple)):         # [text, explanation]
                choices.append(str(o[0]))
            elif isinstance(o, dict):                # {t/text, c/correct}
                choices.append(str(_first(o, ["t", "text", "label", "opt"]) or ""))
                if o.get("c") or o.get("correct") or o.get("isCorrect"):
                    embedded_ans = i
            else:
                choices.append(str(o))
    else:
        return None

    # answer index
    ans = embedded_ans
    if ans is None:
        raw = _first(q, ["c", "a", "answer", "correct", "correctIndex", "ans"])
        if isinstance(raw, bool):
            return None
        elif isinstance(raw, int):
            ans = raw
        elif isinstance(raw, str):
            r = raw.strip()
            if letter_keys and r in letter_keys:
                ans = letter_keys.index(r)
            elif len(r) == 1 and r.upper() in "ABCDEFGH":
                ans = ord(r.upper()) - 65
            elif r.isdigit():
                ans = int(r)
            elif r in choices:
                ans = choices.index(r)
    if not isinstance(ans, int) or not (0 <= ans < len(choices)):
        return None

    # explanation
    exp = ""
    e = _first(q, ["exp", "e", "r", "rationale", "explain", "explanation", "why"])
    if isinstance(e, dict):
        exp = str(e.get(str(ans), e.get(ans, "")) or "")
    elif isinstance(e, list):
        exp = str(e[ans]) if 0 <= ans < len(e) and e[ans] else ""
    elif e:
        exp = str(e)
    if not exp and isinstance(opts, list) and 0 <= ans < len(opts) \
            and isinstance(opts[ans], (list, tuple)) and len(opts[ans]) > 1:
        exp = str(opts[ans][1])
    cite = _first(q, ["cite", "src", "source"])
    if cite:
        exp = (exp + " — " + str(cite)).strip(" —")

    return qtext, choices, ans, exp


def main():
    files = []
    for f in glob.glob("**/*.html", recursive=True):
        base = os.path.basename(f)
        if base in SKIP_BASENAMES or any(x in base for x in SKIP_SUBSTR):
            continue
        if f.startswith("tools" + os.sep) or f.startswith("group-quizzes" + os.sep):
            continue
        src = open(f, encoding="utf-8", errors="ignore").read()
        qs = extract_questions(src)
        if qs is None:
            continue
        files.append((f, src, qs))

    bank = {}
    ids_used = {}
    stats = {"quizzes": 0, "questions": 0, "skipped_img": 0, "skipped_bad": 0, "skipped_files": 0}
    for f, src, qs in sorted(files):
        rel = f.replace(os.sep, "/")
        qid = slug(rel[:-5] if rel.endswith(".html") else rel)
        # guarantee uniqueness
        if qid in ids_used:
            ids_used[qid] += 1
            qid = f"{qid}-{ids_used[qid]}"
        else:
            ids_used[qid] = 1
        out_qs = []
        bad = False
        for q in qs:
            if has_image(q):
                stats["skipped_img"] += 1
                bad = True
                break
            conv = convert(q)
            if not conv:
                stats["skipped_bad"] += 1
                continue
            qtext, choices, ans, exp = conv
            # 4 or 5 choices: the CMS derm Updated masters are five-option A-E, and both
            # Group Study clients render choices generically with forEach.
            if not qtext or not isinstance(choices, list) or len(choices) not in (4, 5):
                stats["skipped_bad"] += 1
                continue
            if not isinstance(ans, int) or not (0 <= ans < len(choices)):
                stats["skipped_bad"] += 1
                continue
            out_qs.append({"q": str(qtext), "choices": [str(c) for c in choices], "answer": ans, "exp": str(exp)})
        if bad or not out_qs:
            stats["skipped_files"] += 1
            continue
        bank[qid] = {
            "title": clean_title(src, os.path.basename(f)[:-5]),
            "category": category_from_path(f),
            "exam": exam_from_path(f),
            "sem": semester_from_path(f),
            "questions": out_qs,
        }
        stats["quizzes"] += 1
        stats["questions"] += len(out_qs)

    # ---- write the split bank -------------------------------------------
    # One chunk per quiz plus a question-free manifest, replacing the old
    # single 5.8 MB group-questions.js. The host picker only ever needs
    # title/category/count for every quiz; the question text of ONE quiz is
    # needed once a room is created or joined. Shipping all of it upfront
    # meant a 5.8 MB download before anyone could start a study session,
    # which on cellular is the difference between "we're studying" and
    # "hang on, it's loading".
    outdir = "group-quizzes"
    os.makedirs(outdir, exist_ok=True)
    for stale in glob.glob(os.path.join(outdir, "*.js")):
        os.remove(stale)

    chunk_header = ("// AUTO-GENERATED by tools/build_group_quizzes.py -- DO NOT EDIT BY HAND.\n"
                    "// One quiz's questions, loaded on demand by group-quizzes/loader.js.\n")
    total_bytes = 0
    for k, v in sorted(bank.items()):
        payload = ("(window.GROUP_QUIZZES=window.GROUP_QUIZZES||{})["
                   + json.dumps(k, ensure_ascii=False) + "]="
                   + json.dumps(v, ensure_ascii=False, separators=(",", ":")) + ";\n")
        blob = chunk_header + payload
        total_bytes += len(blob.encode("utf-8"))
        open(os.path.join(outdir, k + ".js"), "w", encoding="utf-8").write(blob)

    index = {k: {"title": v["title"], "category": v["category"],
                 "exam": v["exam"], "sem": v["sem"], "n": len(v["questions"])}
             for k, v in sorted(bank.items())}
    index_body = ",\n".join(
        json.dumps(k, ensure_ascii=False) + ":" + json.dumps(v, ensure_ascii=False, separators=(",", ":"))
        for k, v in index.items())
    out = ("// AUTO-GENERATED by tools/build_group_quizzes.py -- DO NOT EDIT BY HAND.\n"
           "// Manifest for the Group Study bank: every quiz's title, class and\n"
           "// question COUNT, with no question text. This is what the host picker\n"
           "// renders from; the questions live in group-quizzes/<id>.js and are\n"
           "// fetched one quiz at a time by loader.js.\n"
           "window.GROUP_INDEX = {\n" + index_body + "\n};\n")
    open(os.path.join(outdir, "index.js"), "w", encoding="utf-8").write(out)

    size_mb = total_bytes / 1e6
    index_kb = len(out.encode("utf-8")) / 1024
    cats = {}
    for v in bank.values():
        cats[v["category"]] = cats.get(v["category"], 0) + 1
    print(f"group-quizzes/ written: {stats['quizzes']} chunks, {stats['questions']} questions, {size_mb:.1f} MB total")
    print(f"group-quizzes/index.js (manifest, no question text): {index_kb:.0f} KB")
    print(f"skipped -> image quizzes: {stats['skipped_img']} q, unconvertible: {stats['skipped_bad']} q, empty files: {stats['skipped_files']}")
    print("categories:", dict(sorted(cats.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    main()
