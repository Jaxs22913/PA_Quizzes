#!/usr/bin/env python3
"""Write the facts a class study guide was missing INTO its sections.

Source of truth: tools/guide_additions/<folder-slug>.json, one file per exam
folder: {"folder", "guide", "items": [{"id", "section_id", "html", "keys",
"src": {question, key, explanation, also}}]}. `html` is one guide line (bold
topic phrase + the fact), composed from the quiz question's own vetted,
slide-cited explanation -- nothing beyond it (tools/verify_guide_additions.py
checks that). `keys` are the quiz questions the line answers.

This tool inserts each line at the END of its section, inside a block

    <div class="qa-also" data-gen="1"><p class="qa-also-label">Also tested</p>
    <ul><li id="ga-<id>">...</li></ul></div>

at the same nesting depth as the section's heading (so wrappers/cards are never
split). Idempotent: an existing generated block is removed first, so re-running
after a guide REBUILD (which drops the lines, because the guides are generated)
restores them. Order after any guide or quiz rebuild:

    python3 tools/apply_guide_additions.py
    python3 tools/build_guide_links.py
    python3 tools/check_guide_links.py
    python3 tools/build_guide_docx.py        # the Word copies

Usage: apply_guide_additions.py [--check]   (--check: report guides whose lines are missing/stale)
"""
import glob, html as H, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "tools", "guide_additions")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
TAG = re.compile(r"<!--.*?-->|<(script|style)\b.*?</\1>|<(/?)([a-zA-Z][a-zA-Z0-9]*)([^>]*?)(/?)>", re.S)
GEN = re.compile(r'<div class="qa-also" data-gen="1">.*?</div>\n?', re.S)


def insertion_point(doc, section_id):
    """Index at which to insert a block at the end of the section headed by id=section_id."""
    m = re.search(r"<(h[1-6])\b[^>]*\bid=\"%s\"[^>]*>.*?</\1>" % re.escape(section_id), doc, re.S)
    if not m:
        return None
    stack = []
    for t in TAG.finditer(doc, 0, m.start()):
        if t.group(1) or t.group(0).startswith("<!--"):
            continue
        close, name, selfc = t.group(2), t.group(3).lower(), t.group(5)
        if name in VOID or selfc:
            continue
        if close:
            while stack and stack.pop() != name:
                pass
        else:
            stack.append(name)
    depth = len(stack)
    for t in TAG.finditer(doc, m.end()):
        if t.group(1) or t.group(0).startswith("<!--"):
            continue
        close, name, selfc = t.group(2), t.group(3).lower(), t.group(5)
        if name in VOID or selfc:
            continue
        if not close and re.fullmatch(r"h[1-4]", name) and len(stack) == depth:
            return t.start()
        if close:
            while stack and stack.pop() != name:
                pass
            if len(stack) < depth:
                return t.start()
        else:
            stack.append(name)
    return len(doc)


def render_block(items):
    lis = "".join('<li id="ga-%s">%s</li>' % (it["id"], it["html"]) for it in items)
    return '<div class="qa-also" data-gen="1"><p class="qa-also-label">Also tested</p><ul>%s</ul></div>\n' % lis


def apply_guide(gpath, datas, check=False):
    """Write every additions file that targets this guide in ONE pass (a second pass would
    strip the first file's generated blocks: GEN removes them all before re-inserting)."""
    doc = open(gpath, encoding="utf-8").read()
    base = GEN.sub("", doc)
    by = {}
    for path, data in datas:
        for it in data["items"]:
            if it.get("html") and it["html"] != "SKIP":
                by.setdefault(it["section_id"], []).append(it)
    # insert from the bottom of the document up so earlier offsets stay valid
    spots = []
    for sid, its in by.items():
        p = insertion_point(base, sid)
        if p is None:
            raise SystemExit("%s: section id %s not found in %s" % ([d[0] for d in datas], sid, gpath))
        spots.append((p, sid, its))
    new = base
    for p, sid, its in sorted(spots, key=lambda x: -x[0]):
        new = new[:p] + render_block(its) + new[p:]
    if new != doc and not check:
        open(gpath, "w", encoding="utf-8").write(new)
    return new != doc


def main():
    check = "--check" in sys.argv
    stale = 0
    files = {}
    for f in sorted(glob.glob(os.path.join(DATA, "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        files.setdefault(os.path.join(ROOT, d["folder"], d["guide"]), []).append((f, d))
    for gpath, datas in files.items():
        changed = apply_guide(gpath, datas, check)
        for f, d in datas:
            n = len([1 for it in d["items"] if it.get("html") not in (None, "SKIP")])
            print("%-46s %4d lines  %s" % (os.path.basename(f)[:-5][:46], n, ("STALE/missing" if check else "written") if changed else "up to date"))
        stale += changed
    if check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
