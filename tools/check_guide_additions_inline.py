#!/usr/bin/env python3
"""Prove a run of tools/apply_guide_additions.py only MOVED the added guide lines.

For every study guide that tools/guide_additions/*.json writes into, compare the
working copy with the same file at a git ref (default HEAD) and fail on:

  lost/dup    the multiset of (ga-* id, line text) differs
  edited      the page with every generated line (and old "Also tested" box)
              removed is not byte-identical: something not generated changed
  section     a line is not under its own section_id (nearest id'd h1-h4, what
              build_guide_links/the study-guide panel use), or it moved to a
              different linked section or Pip unit (nearest h2/h3 + any
              <details> it is in) than at the ref. A line the ref had under the
              WRONG section that is now back under its section_id is printed as
              a note, not a failure (the old box skipped nested headings; Pip
              cards in both units then need a re-check before `rehash`)
  context     a generated line sits inside a table, <dl>, heading, <nav>,
              <ol>, another generated line, or an <li> outside a <ul>
  box         an "Also tested" box is still on the page

A positive looks like: "pharm-exam-1-study-guide.html: lost/dup ga-...-012".
Run it after apply_guide_additions.py and before committing; with no
differences from the ref (nothing re-applied) it passes trivially.

Usage: check_guide_additions_inline.py [--ref REF]
"""
import collections, glob, html as H, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import apply_guide_additions as A  # noqa: E402

GA = re.compile(r'<(li|p)\b[^>]*\bid="(ga-[^"]+)"[^>]*>(.*?)</\1>', re.S)
HEAD_ANY = re.compile(r"<(h[1-6])\b([^>]*)>(.*?)</\1>", re.S)


def norm(s):
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def lines(doc):
    return collections.Counter((m.group(2), norm(m.group(3))) for m in GA.finditer(doc))


def where(doc):
    """{ga id: (linked section id, Pip unit heading, details depth)} for every line on the page."""
    heads = [(m.start(), m.group(1), re.search(r'\bid="([^"]+)"', m.group(2)), norm(m.group(3)))
             for m in HEAD_ANY.finditer(doc)]
    out = {}
    for m in GA.finditer(doc):
        pos = m.start()
        sec = next((idm.group(1) for st, tag, idm, _ in reversed(heads)
                    if st < pos and idm and tag in ("h1", "h2", "h3", "h4")), None)
        unit = next((t for st, tag, _, t in reversed(heads) if st < pos and tag in ("h2", "h3")), None)
        det = len(re.findall(r"<details\b", doc[:pos])) - len(re.findall(r"</details>", doc[:pos]))
        out[m.group(2)] = (sec, unit, det)
    return out


def bad_context(doc):
    out = []
    root = A.parse(doc)
    for n in A.walk(root):
        if not (n.attr("id") or "").startswith("ga-"):
            continue
        if n.tag == "li" and n.parent.tag != "ul":
            out.append("%s: <li> inside <%s>" % (n.attr("id"), n.parent.tag))
        x = n.parent
        while x is not None:
            if x.tag in ("table", "dl", "nav", "ol", "p", "li") or re.fullmatch(r"h[1-6]", x.tag) or \
                    (x.attr("id") or "").startswith("ga-"):
                out.append("%s: inside <%s>" % (n.attr("id"), x.tag))
                break
            x = x.parent
    return out


def main():
    ref = sys.argv[sys.argv.index("--ref") + 1] if "--ref" in sys.argv else "HEAD"
    guides = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "tools", "guide_additions", "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        g = os.path.join(d["folder"], d["guide"])
        for it in d["items"]:
            if it.get("html") not in (None, "SKIP"):
                guides.setdefault(g, {})["ga-" + it["id"]] = it["section_id"]
    fails, fixed, moved_total, n_total = [], [], 0, 0
    for g, sids in guides.items():
        name = os.path.basename(g)
        after = open(os.path.join(ROOT, g), encoding="utf-8").read()
        r = subprocess.run(["git", "-C", ROOT, "show", "%s:%s" % (ref, g)], capture_output=True)
        if r.returncode:
            print("%-38s new at %s, nothing to compare" % (name, ref))
            continue
        before = r.stdout.decode("utf-8")
        la, lb = lines(after), lines(before)
        for (i, t), c in (lb - la).items():
            fails.append("%s: lost/dup %s (%r)" % (name, i, t[:60]))
        for (i, t), c in (la - lb).items():
            fails.append("%s: lost/dup %s appeared or changed (%r)" % (name, i, t[:60]))
        if A.strip_generated(after) != A.strip_generated(before):
            a, b = A.strip_generated(after), A.strip_generated(before)
            k = next((j for j in range(min(len(a), len(b))) if a[j] != b[j]), min(len(a), len(b)))
            fails.append("%s: edited: non-generated content differs at offset %d: %r" % (name, k, a[k - 40:k + 40]))
        wa, wb = where(after), where(before)
        for i in wa:
            if i in sids and wa[i][0] != sids[i]:
                fails.append("%s: section %s sits under #%s, its section_id is #%s" % (name, i, wa[i][0], sids[i]))
            elif i in wb and wa[i] != wb[i]:
                if wb[i][0] != sids.get(i):
                    # the ref had it under the wrong section (the old box skipped nested headings)
                    fixed.append("%s: %s back under #%s (was under #%s; Pip unit %r -> %r)"
                                 % (name, i, wa[i][0], wb[i][0], wb[i][1], wa[i][1]))
                else:
                    fails.append("%s: section %s moved from %s to %s" % (name, i, wb[i], wa[i]))
        fails += ["%s: context %s" % (name, x) for x in bad_context(after)]
        if 'class="qa-also"' in after:
            fails.append("%s: box: an Also-tested box is still on the page" % name)
        moved = sum(1 for m in A.GEN_LINE.finditer(after))
        moved_total += moved
        n_total += sum(la.values())
        print("%-38s %4d lines before, %4d after, %4d inline" % (name, sum(lb.values()), sum(la.values()), moved))
    print("TOTAL %d lines, %d written inline; %d problem(s); %d line(s) returned to their own section"
          % (n_total, moved_total, len(fails), len(fixed)))
    for x in fixed:
        print("  note " + x)
    for x in fails[:60]:
        print("  FAIL " + x)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
