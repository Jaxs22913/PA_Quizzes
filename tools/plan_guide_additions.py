#!/usr/bin/env python3
"""Plan which quiz facts each class's STUDY GUIDE does not teach, and where each
belongs. Output (stdout JSON path given by --out) feeds the authoring step; the
committed data is tools/guide_additions/<folder-slug>.json (see
apply_guide_additions.py).

A fact is a gap when, after the normal matching (build_guide_links.py) against
the exam's study guide ALONE, the section it lands in holds < 60% of the correct
option's terms. Its target is the section the slide's neighbors define (the same
placement the 'closest section' tier uses). Questions whose facts are near
duplicates in the same section are grouped so the guide gets one line, not five.
"""
import glob, json, os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_guide_links as B

ROOT = B._REPO
GAP_MAX = 0.60


def study_guide(folder):
    c = [g for g in glob.glob(os.path.join(folder, "*study-guide.html"))
         if 'data-dark-kind="guide"' in open(g, encoding="utf-8").read() and "osce" not in g]
    return c[0] if len(c) == 1 else None


def explanation(q):
    e = q["opts"][q["c"]][1].strip()
    return re.sub(r"^Correct[.,:]\s*", "", e)


def plan_folder(folder, only_keys=None, id_tag=""):
    g = study_guide(folder)
    if not g:
        return []
    B.ensure_heading_ids(g)
    idx = B.Index([g])
    if not idx.secs:
        return []
    pos = {(sc["guide"], sc["id"]): i for i, sc in enumerate(idx.secs)}
    items, seen = [], set()
    for f in sorted(glob.glob(os.path.join(folder, "*.html"))):
        Q = B.load_questions(f)
        for q in Q or []:
            k = B.qkey(q)
            if k in seen:
                continue
            seen.add(k)
            items.append(dict(q=q, k=k, deck=B.deck_of(q["cite"]), slide=B.slide_of(q["cite"]), link=None))
    for it in items:                                   # direct matches -> anchors
        if only_keys is not None and it["k"] in only_keys:
            continue                                   # the builder already decided: not explained
        sc, exact = B.match(idx, it["q"])
        if sc is None:
            continue
        blk = B.best_block(idx, it["q"], sc)
        b = idx.cov(it["q"], set(B.toks(blk or "")))
        if exact or (b is not None and b >= B.PASSAGE_MIN):
            it["link"] = ("passage", pos[(sc["guide"], sc["id"])])
    anchors = [(i_["deck"], i_["slide"], i_["link"][1]) for i_ in items if i_["link"] and i_["slide"] is not None]
    gaps = []
    for it in items:
        if it["link"]:
            continue
        q = it["q"]
        win = B.near_window(idx, anchors, it["deck"], it["slide"])
        p = B.near_section(idx, anchors, q, it["deck"], it["slide"])
        if p is None:
            sc, _ = B.match(idx, q)
            p = pos[(sc["guide"], sc["id"])] if sc else None
        if p is None:
            continue
        sc = idx.secs[p]
        cov = idx.cov(q, sc["tok"])
        # is the fact anywhere in a window section?
        best = max([idx.cov(q, idx.secs[i]["tok"]) or 0 for i in range((win[0] if win else p), (win[1] if win else p) + 1)] or [0])
        if only_keys is None:
            if cov is not None and best >= B.SECTION_MIN:
                continue                               # a window section already teaches it
            if best >= GAP_MAX and cov is not None and cov >= GAP_MAX:
                continue
        elif it["k"] not in only_keys:
            continue
        gaps.append(dict(k=it["k"], q=q["q"], key=q["opts"][q["c"]][0], expl=explanation(q), cite=q["cite"],
                         deck=it["deck"], slide=it["slide"], guide=os.path.basename(g),
                         section_id=sc["id"], section=sc["title"]))
    # group near-duplicate facts landing in the same section
    groups = []
    for gp in gaps:
        t = set(B.toks(gp["key"] + " " + gp["expl"]))
        for grp in groups:
            if grp["section_id"] == gp["section_id"]:
                u = grp["_t"]
                if len(t & u) / max(1, len(t | u)) >= 0.5:
                    grp["members"].append(gp); grp["_t"] = u | t
                    break
        else:
            groups.append(dict(section_id=gp["section_id"], section=gp["section"], guide=gp["guide"], _t=t, members=[gp]))
    out = []
    for n, grp in enumerate(groups):
        m = grp["members"][0]
        out.append(dict(id="%s-%s%03d" % (re.sub(r"[^a-z0-9]+", "-", os.path.basename(folder).lower()).strip("-"), id_tag, n),
                        section_id=grp["section_id"], section=grp["section"], guide=grp["guide"],
                        keys=[x["k"] for x in grp["members"]],
                        question=m["q"], key=m["key"], explanation=m["expl"],
                        cites=sorted({x["cite"] for x in grp["members"]}),
                        extra=[dict(key=x["key"], explanation=x["expl"]) for x in grp["members"][1:]]))
    return out


def main():
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
    allp = {}
    for d in sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, d)
        if not os.path.isdir(p) or not d.startswith(("Clinical", "Microbiology", "Pharmacology I", "Physical Diagnosis 2", "Principles", "Interpretation")):
            continue
        if "--round2" in sys.argv:
            res = B.build_folder(p, dry=True)
            keys = {B.qkey(q) for q, _ in (res[2] if res else [])}
            r = plan_folder(p, only_keys=keys, id_tag=(sys.argv[sys.argv.index("--tag") + 1] if "--tag" in sys.argv else "b")) if keys else []
        else:
            r = plan_folder(p)
        allp[d] = r
        print("%-48s %4d facts to add (%d questions)" % (d, len(r), sum(len(x["keys"]) for x in r)))
    print("TOTAL %d facts, %d questions" % (sum(len(v) for v in allp.values()), sum(len(x["keys"]) for v in allp.values() for x in v)))
    if out:
        json.dump(allp, open(out, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
