#!/usr/bin/env python3
"""Every accordion on the site opens closed.

A page that loads with sections already unfolded buries the thing you came
for. Two ways that used to happen, both fixed and both guarded here:

  1. an `open` attribute written into the markup or emitted by a generator
  2. script that reopens a section from a remembered localStorage value

Opening a section in response to something the user just did -- typing in a
search box, following a link -- is fine and is not flagged; only page-load
state is.

  python3 tools/check_accordions_closed.py
"""
import glob, os, re, sys

# `<details ... open>` anywhere it can reach the page, markup or generated.
OPEN_TAG = re.compile(r"<details\b[^>]*\bopen\b", re.I)

# Script that reopens a section from stored state on load. The giveaway is a
# localStorage read feeding a `.open =`, so look for a remembered-open key.
REMEMBERED = re.compile(
    r"localStorage\.getItem\(\s*[\"'][^\"']*[Oo]pen[^\"']*[\"']", re.I)

SKIP_DIRS = {".git", "node_modules", "group-quizzes"}


def files():
    for pat in ("*.html", "*.js", "tools/*.py"):
        for f in glob.glob(pat):
            yield f
    for f in glob.glob("*/*.html"):
        if f.split(os.sep)[0] not in SKIP_DIRS:
            yield f


def main():
    bad = 0
    me = os.path.basename(__file__)
    for f in sorted(set(files())):
        if os.path.basename(f) == me:      # this file quotes the patterns
            continue
        try:
            text = open(f, encoding="utf8").read()
        except Exception:
            continue
        for rx, why in ((OPEN_TAG, "accordion defaults to open"),
                        (REMEMBERED, "reopens from remembered state on load")):
            for m in rx.finditer(text):
                line = text.count("\n", 0, m.start()) + 1
                bad += 1
                print("%s:%d  %s\n    %s" % (f, line, why, m.group(0)[:90]))
    print("\n%s" % ("all accordions start closed" if not bad
                    else "%d accordion(s) open by default" % bad))
    return bad


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
