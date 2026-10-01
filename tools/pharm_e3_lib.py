# -*- coding: utf-8 -*-
"""Shared pieces for the Pharmacology I Exam 3 reference charts.

Data lives in tools/pharm_e3/<L9|L10|...>.json, one file per lecture, so a new lecture is one new
file (Lectures 10-13 arrive later). Every row carries the slide it came from and `verify`
substrings that must appear on that slide, exactly as the Exam 1 charts do.

    python3 tools/pharm_e3_lib.py dump L9 [slide ...]   # print a deck's slide text (with slide numbers)
"""
import html as H, json, os, re, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(HERE, "pharm_e3")
BASE = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Pharmacology I Inbox/Exam 3/")

LECTURES = {
    "L9": {"n": 9, "title": "Diuretics and Heart Failure Drugs", "deck": "Diuretics and Heart Failure Drugs.pptx"},
}
KINDS = ("indications", "sideeffects", "contra")
_cache = {}
OCR = json.load(open(os.path.join(DATA, "ocr.json"), encoding="utf-8")) if os.path.exists(os.path.join(DATA, "ocr.json")) else {}


def norm(s):
    s = H.unescape(s)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("–", "-"), ("—", "-"),
                 ("−", "-"), ("\xa0", " "), ("…", "..."), ("​", ""), ("→", "->")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


def deck_path(lec):
    d = LECTURES[lec]["deck"]
    return BASE + d if d else None


def slide_count(lec):
    z = zipfile.ZipFile(deck_path(lec))
    return len([n for n in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)])


def slide_raw(lec, n):
    """Slide text (runs joined by spaces) plus the speaker notes."""
    z = zipfile.ZipFile(deck_path(lec))
    out = []
    for member in ("ppt/slides/slide%d.xml" % n, "ppt/notesSlides/notesSlide%d.xml" % n):
        if member in z.namelist():
            x = z.read(member).decode("utf-8", "ignore")
            paras = re.findall(r"<a:p>(.*?)</a:p>", x, re.S)
            for p in paras:
                t = "".join(re.findall(r"<a:t>(.*?)</a:t>", p, re.S))
                if t.strip():
                    out.append(H.unescape(t))
    return out


def slide_text(lec, n):
    key = (lec, n)
    if key not in _cache:
        z = zipfile.ZipFile(deck_path(lec))
        parts = []
        for member in ("ppt/slides/slide%d.xml" % n, "ppt/notesSlides/notesSlide%d.xml" % n):
            if member in z.namelist():
                x = z.read(member).decode("utf-8", "ignore")
                runs = re.findall(r"<a:t>(.*?)</a:t>", x, re.S)
                parts.append(" ".join(runs))      # runs separated
                parts.append("".join(runs))       # runs joined -- PowerPoint splits words mid-word
        extra = OCR.get(lec, {}).get(str(n))          # text read off a picture-only slide (see pharm_e3/ocr.json)
        if extra:
            parts.append(extra); parts.append(re.sub(r"\s+", "", extra))
        _cache[key] = norm(" ".join(parts))
    return _cache[key]


def load(lec):
    p = os.path.join(DATA, lec + ".json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None


def lectures_present():
    return [l for l in LECTURES if load(l) is not None]


def charts_of(d):
    """The lecture's comparison charts: the single "chart" plus any in "charts"."""
    return ([d["chart"]] if d.get("chart") else []) + list(d.get("charts") or [])


def iter_rows(d):
    """(kind, row) for every row that carries slide+verify."""
    for k in KINDS:
        for r in d.get(k, []):
            yield k, r
    for grp in ("killers", "commons", "zebras"):
        for r in (d.get("kcz") or {}).get(grp, []):
            yield "kcz-" + grp, r
    for ch in charts_of(d):
        for r in ch.get("rows", []):
            yield "chart", r


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "dump":
        lec = sys.argv[2]
        want = [int(x) for x in sys.argv[3:]] or range(1, slide_count(lec) + 1)
        for n in want:
            t = slide_raw(lec, n)
            print("=== SLIDE %d ===" % n)
            print("\n".join(t))
