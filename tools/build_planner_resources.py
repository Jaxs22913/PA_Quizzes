#!/usr/bin/env python3
"""Writes planner-resources.json: for each Semester 2 exam folder, the pages a study
task should link to (study guide, cram sheet, OSCE/reference pages, quizzes).
The planner keys it by "<class id>|<exam number>"; practical exams (OSCE) key by
"<class id>|osce". Nothing here is hand-edited -- rerun after adding a folder."""
import html, json, os, re, sys
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
out = {}
for folder in sorted(os.listdir(ROOT)):
    m = re.search(r"Exam (\d+)$", folder)
    c = cls(folder)
    if not (m and c and os.path.isdir(os.path.join(ROOT, folder))):
        continue
    d = os.path.join(ROOT, folder)
    files = sorted(f for f in os.listdir(d) if f.endswith(".html"))
    rec = {"folder": folder, "guide": None, "cram": None, "refs": [], "quizzes": 0, "master": None}
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
        elif "quiz" in low or "drill" in low or "vignette" in low or "master" in low:
            rec["quizzes"] += 1
    out[c + "|" + m.group(1)] = rec
    osce = [r for r in rec["refs"] if "osce" in r["href"].lower()]
    if osce:
        o = out.setdefault(c + "|osce", {"folder": folder, "guide": None, "cram": None, "refs": [], "quizzes": 0, "master": None})
        o["refs"] += [r for r in osce if r not in o["refs"]]
json.dump(out, open(os.path.join(ROOT, "planner-resources.json"), "w"), indent=1, sort_keys=True)
print(len(out), "entries ->", "planner-resources.json")
for k, v in sorted(out.items()):
    print(" ", k, "guide" if v["guide"] else "-", "cram" if v["cram"] else "-", len(v["refs"]), "refs", v["quizzes"], "quizzes", "master" if v["master"] else "")
