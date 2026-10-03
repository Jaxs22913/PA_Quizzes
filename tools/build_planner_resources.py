#!/usr/bin/env python3
"""Writes planner-resources.json: for each Semester 2 exam folder, the pages a study
task should link to (study guide, cram sheet, OSCE/reference pages, quizzes).
The planner keys it by "<class id>|<exam number>"; practical exams (OSCE) key by
"<class id>|osce". Nothing here is hand-edited -- rerun after adding a folder."""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_guide_links as BG      # load_questions: how many questions a page holds
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER_CLASS = [
    (r"^Physical Diagnosis 2", "physical-diagnosis-2"), (r"^Pharmacology", "pharm-1"),
    (r"^Clinical Medicine", "cms-1"), (r"^Clinical Path", "clin-path-1"),
    (r"^Principles of Diagnostic Medicine", "pdm-1"), (r"^Microbiology", "microbiology"),
    (r"^Interpretation of Medical Literature", "med-lit"),
]
def cls(folder):
    for pat, c in FOLDER_CLASS:
        if re.match(pat, folder, re.I):
            return c
def title(fn):
    t = re.sub(r"\.html$", "", fn)
    t = re.sub(r"[-_]+", " ", t)
    return t.strip().capitalize()
def head_title(path):
    try:
        s = open(path, encoding="utf-8", errors="ignore").read(6000)
        m = re.search(r"<title>(.*?)</title>", s, re.S | re.I)
        if not m:
            return None
        t = html.unescape(re.sub(r"\s+", " ", m.group(1))).strip()
        return re.split(r"\s+[\u2014\u2013|:]\s+|\s+-\s+", t)[0].strip() or t
    except OSError:
        return None
def raw_title(path):
    try:
        m = re.search(r"<title>(.*?)</title>", open(path, encoding="utf-8", errors="ignore").read(6000), re.S | re.I)
        return html.unescape(re.sub(r"\s+", " ", m.group(1))).strip() if m else None
    except OSError:
        return None
def page_name(path, fn):
    """Short, human name for one quiz/reference page ("Adrenergic Drugs Quiz 1")."""
    m = re.search(r"master-exam(-updated)?-form-([a-z])", fn)
    if m:
        return ("Updated master exam" if m.group(1) else "Master exam") + ", form " + m.group(2).upper()
    t = raw_title(path) or title(fn)
    parts = re.split(r"\s+[\u2014\u2013|]\s+", t)
    t = (parts[-1] if len(parts) > 1 and re.search(r"Exam \d+$", parts[0]) else parts[0]).strip()
    t = re.sub(r"\s*\(Class of \d+\)\s*$", "", t)
    return t
def qcount(path):
    try:
        return len(BG.load_questions(path) or [])
    except Exception:
        return 0
out = {}
for folder in sorted(os.listdir(ROOT)):
    m = re.search(r"Exam (\d+)$", folder)
    c = cls(folder)
    if not (m and c and os.path.isdir(os.path.join(ROOT, folder))):
        continue
    d = os.path.join(ROOT, folder)
    files = sorted(f for f in os.listdir(d) if f.endswith(".html"))
    rec = {"folder": folder, "guide": None, "cram": None, "refs": [], "quizzes": 0, "master": None, "items": []}
    for f in files:
        rel = folder + "/" + f
        low = f.lower()
        if low.endswith("study-guide.html") and "osce" not in low:
            rec["guide"] = rec["guide"] or rel
        elif "cram-sheet" in low:
            rec["cram"] = rec["cram"] or rel
        elif "osce" in low or "reference" in low or "chart" in low:
            rec["refs"].append({"href": rel, "t": head_title(os.path.join(d, f)) or title(f)})
        elif "master-exam" in low and not rec["master"]:
            rec["master"] = rel
        elif "quiz" in low or "drill" in low or "vignette" in low or "master" in low or "most-likely" in low:
            rec["quizzes"] += 1
    for f in files:
        low = f.lower()
        rel = folder + "/" + f
        path = os.path.join(d, f)
        if re.search(r"-v1\.html$", low) or low.startswith("guide-links"):
            continue                                  # superseded copies of the same master
        if low.endswith("study-guide.html") and "osce" not in low:
            rec["items"].append({"k": "guide", "t": "Study guide", "href": rel})
        elif "cram-sheet" in low:
            rec["items"].append({"k": "cram", "t": "Cram sheet", "href": rel})
        elif "master-exam" in low:
            rec["items"].append({"k": "master", "t": page_name(path, f), "href": rel, "n": qcount(path)})
        elif re.search(r"quiz|drill|vignette|most-likely", low):
            k = "drill" if "drill" in low else "quiz"
            rec["items"].append({"k": k, "t": page_name(path, f), "href": rel, "n": qcount(path)})
        elif re.search(r"osce|reference|chart|indications|side-effects|receptor|what-to-star|killers|gram-coverage|review-session|referral|guide", low):
            rec["items"].append({"k": "ref", "t": page_name(path, f), "href": rel})
    # a topic can have several sets whose page titles read alike ("Ophthalmic Drugs"): tell them apart
    seen = {}
    for i in rec["items"]:
        seen.setdefault(i["t"], []).append(i)
    for t_, group in seen.items():
        if len(group) > 1 and group[0]["k"] in ("quiz", "drill"):
            for i in group:
                i["t"] += " (set 2)" if "version-2" in i["href"] else " (set 1)"
    rank = {"guide": 0, "cram": 1, "ref": 2, "quiz": 3, "drill": 4, "master": 5}
    rec["items"].sort(key=lambda i: (rank[i["k"]], i["t"] if i["k"] in ("quiz", "drill", "ref") else i["href"]))
    out[c + "|" + m.group(1)] = rec
    osce = [r for r in rec["refs"] if "osce" in r["href"].lower()]
    if osce:
        o = out.setdefault(c + "|osce", {"folder": folder, "guide": None, "cram": None, "refs": [], "quizzes": 0, "master": None, "items": []})
        o["refs"] += [r for r in osce if r not in o["refs"]]
        o["items"] += [{"k": "ref", "t": r["t"], "href": r["href"]} for r in osce if not any(i["href"] == r["href"] for i in o["items"])]
json.dump(out, open(os.path.join(ROOT, "planner-resources.json"), "w"), indent=1, sort_keys=True)
print(len(out), "entries ->", "planner-resources.json")
for k, v in sorted(out.items()):
    print(" ", k, "guide" if v["guide"] else "-", "cram" if v["cram"] else "-", len(v["refs"]), "refs", v["quizzes"], "quizzes", "master" if v["master"] else "")
