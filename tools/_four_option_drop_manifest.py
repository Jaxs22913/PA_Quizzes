#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Record which option index was removed from each converted question.

The length-bias shortfix tables (cmsderm_shortfix.py, cmsophtho_shortfix.py)
address options BY INDEX into the original five, so after the conversion to four
they address the wrong option -- or run off the end. Rebuilding them needs to
know which index went.

The choice is deterministic, so it is recomputed from the pre-conversion files
in git rather than being remembered: read the original blob, run the same
chooser, write the answer out. That also means this can be regenerated at any
point instead of being a one-off artefact nobody can reproduce.
"""
import ast, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import importlib.util
_spec = importlib.util.spec_from_file_location(
    "cv4", os.path.join(HERE, "convert_cms_to_four_options.py"))
cv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cv)

OUT = os.path.join(HERE, "cms_four_option_drops.json")


def original(relpath, rev):
    return subprocess.check_output(["git", "show", "%s:%s" % (rev, relpath)],
                                   cwd=os.path.dirname(HERE)).decode("utf-8")


def main():
    rev = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    names = sorted(n for n in os.listdir(HERE)
                   if n.endswith(".py") and n.startswith(cv.SCOPE_PREFIXES))
    drops = {}
    for name in names:
        rel = "tools/" + name
        try:
            src = original(rel, rev)
        except subprocess.CalledProcessError:
            continue                      # not tracked at that revision
        try:
            spans = cv.option_spans(src.encode("utf-8"), ast.parse(src))
        except SyntaxError:
            continue
        five = [spans[o] for o in sorted(spans) if len(spans[o]["spans"]) >= 5]
        if not five:
            continue
        per = []
        for rec in five:
            per.append(cv.choose_drop({"opts": rec["opts"], "c": 0, "q": ""}))
        drops[name] = per
    json.dump(drops, open(OUT, "w", encoding="utf-8"), indent=1, sort_keys=True)
    print("wrote %s: %d file(s), %d question(s)"
          % (os.path.basename(OUT), len(drops), sum(len(v) for v in drops.values())))


if __name__ == "__main__":
    main()
