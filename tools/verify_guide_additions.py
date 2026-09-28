#!/usr/bin/env python3
"""Every line written into a guide must trace to its source question.

For each item in tools/guide_additions/*.json: the line may contain only <b>/<i>
markup; every numeral in it must appear in the source (question, key,
explanation, merged extras, or the section title); and every content word
(5+ letters, after the site's stemming) must appear in the source or be a
prefix-stem of a source word. Anything else is a word the author added ->
listed for a human to read; exit 1 if any remain.
"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_guide_links as B

DATA = os.path.join(B._REPO, "tools", "guide_additions")
# words that carry no clinical claim and may be added when joining a fact into a sentence
GLUE = set("""usually often typically generally always never because therefore however whereas instead rather
about both either neither every another several including without within among across toward since until while during
which where whose their there these those would could should might versus depends depend course example meaning
start choose despite following causing needed hence thus also""".split())


NUMS = {"twenty": "20", "thirty": "30", "forty": "40", "fifty": "50", "sixty": "60", "seventy": "70",
        "eighty": "80", "ninety": "90", "hundred": "100", "thirteen": "13", "fourteen": "14", "fifteen": "15",
        "sixteen": "16", "eighteen": "18", "half": "0.5"}
NUMRE = re.compile(r"\b(" + "|".join(NUMS) + r")\b", re.I)


def norm(t):
    """Spelled-out numbers -> digits, '%' -> percent, so '50%' and 'fifty percent' agree."""
    t = t.replace("%", " percent ")
    return NUMRE.sub(lambda m: NUMS[m.group(1).lower()], t)


def source_tokens(it):
    s = it["src"]
    txt = " ".join([s["question"], s["key"], s["explanation"], it.get("section_title", "")] +
                   [e["key"] + " " + e["explanation"] for e in s.get("also", [])])
    return set(B.toks(norm(txt))), norm(txt).lower()


def main():
    bad, n = [], 0
    for f in sorted(glob.glob(os.path.join(DATA, "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for it in d["items"]:
            h = it.get("html")
            if not h or h == "SKIP":
                continue
            n += 1
            if re.search(r"<(?!/?(?:b|i)>)[a-zA-Z/]", h):
                bad.append((d["folder"], it["id"], "markup other than <b>/<i>", h)); continue
            plain = re.sub(r"<[^>]+>", "", h)
            body = re.sub(r"<[^>]+>", "", re.sub(r"^\s*<b>.*?</b>", "", h, count=1, flags=re.S))   # the bold label is a title, not a claim
            if re.search(r"\b(this patient|the question|the answer|the deck|the slide|correct answer)\b", plain, re.I):
                bad.append((d["folder"], it["id"], "leaks question framing", h)); continue
            st, raw = source_tokens(it)
            novel = []
            for t in B.toks(norm(body)):
                if t in st or t in GLUE:
                    continue
                if t.isdigit() or re.fullmatch(r"\d+(\.\d+)?", t):
                    novel.append(t); continue
                if len(t) < 5:
                    continue
                if any(s[:4] == t[:4] for s in st if len(s) >= 4):
                    continue
                novel.append(t)
            if novel:
                bad.append((d["folder"], it["id"], "not in source: " + ", ".join(sorted(set(novel))), h))
    print("checked %d lines; %d need a human look" % (n, len(bad)))
    for folder, i, why, h in bad[:60]:
        print("  %-16s %-8s %s\n      %s" % (folder[:16], i, why, re.sub(r"<[^>]+>", "", h)[:160]))
    if bad:
        sys.exit(1)


if __name__ == "__main__":
    main()
