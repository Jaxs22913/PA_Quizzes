#!/usr/bin/env python3
"""check_length_bias.py without the browser: same numbers, seconds not an hour.

check_length_bias.py navigates headless Chrome to every quiz page and reads the
question array in page scope. Correct, but it loads every image and service
worker too -- about 4 seconds a file, over an hour for the site -- and it died
on a websocket error mid-sweep (2026-09-20).

The array is a plain JavaScript literal in a <script> tag, so it can be cut out
of the HTML by bracket-matching and evaluated on its own by node. The constants,
the option-shape normalisation and the probe order are the Chrome tool's, so the
numbers are the same numbers:

  longest%   the correct answer is the UNIQUELY longest choice (~25% is chance)
  gameable%  ...longest by at least MARGIN_CHARS characters AND at least
             MARGIN_FRAC longer than the runner-up. The number that matters.

    python3 tools/check_length_bias_fast.py                    # whole site
    python3 tools/check_length_bias_fast.py "Anatomy Exam 4"   # folder(s) or file(s)
    python3 tools/check_length_bias_fast.py --json out.json

Exit 1 if any file is over THRESHOLD gameable, or if a page that carries a
question bank in its source could not be read -- that page was not checked.

VALIDATION. The prototype (a scratch script, 2026-09-20) matched the Chrome
tool exactly on two folders: 37 files / 1,670 questions and 43 files / 2,730
questions, including the option-level {"t":..,"c":true} shape. Re-validated when
this was checked in (2026-09-22) against check_length_bias.py on "Clinical
Pathophysiology I Exam 1" + "Interpretation of Medical Literature Exam 1": 27
files, 960 questions, 465 longest, 87 gameable from both, identical file by
file. Requires node on PATH; without it this fails loudly rather than reporting
an empty, clean-looking sweep.
"""
import argparse, json, os, re, shutil, subprocess, sys, tempfile

MARGIN_CHARS = 8      # absolute characters longer than the runner-up
MARGIN_FRAC = 0.18    # ...and at least this much longer, proportionally
THRESHOLD = 0.35      # flag a file above this gameable rate
# check_length_bias.py probes these identifiers in this order and takes the
# first that holds a non-empty array; so does this.
PROBES = ["QUESTIONS", "questions", "Q", "DECK", "BANK", "ITEMS"]
SKIP_DIRS = ("rpg", "tools", ".git", "node_modules")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cut_literal(text, start):
    """Bracket-match a JS array literal at `start`, respecting strings and comments."""
    depth, i, n = 0, start, len(text)
    while i < n:
        ch = text[i]
        if ch in "\"'`":
            quote = ch
            i += 1
            while i < n:
                if text[i] == "\\":
                    i += 2
                    continue
                if text[i] == quote:
                    break
                i += 1
        elif ch == "/" and i + 1 < n and text[i + 1] == "/":
            while i < n and text[i] != "\n":
                i += 1
        elif ch == "/" and i + 1 < n and text[i + 1] == "*":
            i += 2
            while i + 1 < n and not (text[i] == "*" and text[i + 1] == "/"):
                i += 1
            i += 1
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
            if depth == 0:
                return text[start:i + 1]
        i += 1
    return None


# The same normalisation as check_length_bias.EXTRACT, run over each literal.
NODE = r"""
const fs = require('fs');
const payload = JSON.parse(fs.readFileSync(process.env.PAYLOAD, 'utf8'));
const out = {};
for (const [file, lits] of Object.entries(payload)) {
  let arr = null;
  for (const src of lits) {
    try { const v = (0, eval)('(' + src + ')'); if (v && v.length) { arr = v; break; } } catch (e) {}
  }
  if (!arr) { out[file] = null; continue; }
  const res = [];
  for (const q of arr) {
    if (!q || typeof q !== 'object') continue;
    const opts = q.opts || q.choices || q.options || q.o;
    let c = (q.c !== undefined) ? q.c : (q.answer !== undefined ? q.answer : q.a);
    if (!opts) continue;
    if (c === undefined && Array.isArray(opts)) {
      for (let f = 0; f < opts.length; f++) {
        const of_ = opts[f];
        if (of_ && typeof of_ === 'object' && (of_.c === true || of_.correct === true)) { c = f; break; }
      }
    }
    const texts = [];
    if (Array.isArray(opts)) {
      for (const o of opts) texts.push(typeof o === 'string' ? o : (o && (o[0] || o.t || o.text)) || '');
    } else {
      const keys = Object.keys(opts).sort();
      for (const k of keys) texts.push(String(opts[k]));
      if (typeof c === 'string') c = keys.indexOf(c.toUpperCase());
    }
    if (typeof c === 'string') c = c.charCodeAt(0) - 65;
    if (typeof c !== 'number' || c < 0 || c >= texts.length) continue;
    res.push({ c: c, lens: texts.map(t => String(t).trim().length) });
  }
  out[file] = res;
}
process.stdout.write(JSON.stringify(out));
"""


def classify(c, lens):
    """-> (is_longest, is_gameable), exactly check_length_bias.classify."""
    correct = lens[c]
    others = [l for i, l in enumerate(lens) if i != c]
    if not others:
        return False, False
    runner = max(others)
    is_longest = correct > runner
    gameable = is_longest and (correct - runner) >= MARGIN_CHARS and \
        runner > 0 and (correct - runner) / runner >= MARGIN_FRAC
    return is_longest, gameable


def collect(targets):
    files = []
    for t in targets:
        p = t if os.path.exists(t) else os.path.join(ROOT, t)
        if not os.path.exists(p):
            sys.exit("no such folder or file: %s" % t)
        if os.path.isfile(p):
            files.append(os.path.relpath(os.path.abspath(p), ROOT))
            continue
        for dirpath, dirnames, filenames in os.walk(p):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in filenames:
                if fn.endswith(".html"):
                    files.append(os.path.relpath(os.path.abspath(os.path.join(dirpath, fn)), ROOT))
    return sorted(set(files))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", default=[])
    ap.add_argument("--json", dest="json_out")
    ap.add_argument("--threshold", type=float, default=THRESHOLD)
    args = ap.parse_args()

    node = shutil.which("node")
    if not node:
        sys.exit("node is not on PATH -- install it, or run check_length_bias.py (Chrome). "
                 "Refusing to report a sweep that read nothing.")
    files = collect(args.paths or [ROOT])

    payload, has_bank = {}, set()
    for f in files:
        text = open(os.path.join(ROOT, f), encoding="utf-8", errors="ignore").read()
        if re.search(r"(?:var|const|let)?\s*QUESTIONS\s*=\s*\[", text):
            has_bank.add(f)
        lits = []
        for name in PROBES:
            for m in re.finditer(r"(?:const|let|var)\s+%s\s*=\s*(?=\[)" % name, text):
                lit = cut_literal(text, m.end())
                if lit:
                    lits.append(lit)
        if lits:
            payload[f] = lits

    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as fh:
        json.dump(payload, fh)
        tmp = fh.name
    try:
        res = subprocess.run([node, "-e", NODE], capture_output=True, text=True,
                             env=dict(os.environ, PAYLOAD=tmp))
    finally:
        os.unlink(tmp)
    if res.returncode != 0:
        sys.exit("node failed: " + res.stderr[:400])
    data = json.loads(res.stdout)

    results = []
    tot_q = tot_long = tot_game = 0
    for f in files:
        qs = data.get(f)
        if not qs:
            continue
        nl = ng = 0
        for q in qs:
            L, G = classify(q["c"], q["lens"])
            nl += L
            ng += G
        results.append({"file": f, "n": len(qs), "longest": nl, "gameable": ng,
                        "longest_pct": nl / len(qs), "gameable_pct": ng / len(qs)})
        tot_q += len(qs)
        tot_long += nl
        tot_game += ng
    read = {r["file"] for r in results}
    unread = sorted(f for f in has_bank if f not in read)

    flagged = sorted((r for r in results if r["gameable_pct"] > args.threshold),
                     key=lambda r: -r["gameable_pct"])
    if unread:
        print("HAS A QUESTION BANK IN ITS SOURCE BUT COULD NOT BE READ -- NOT CHECKED:")
        for f in unread:
            print("   %s" % f)
        print()
    print(f"html files walked          : {len(files)}")
    print(f"files with a question bank : {len(results)}")
    print(f"questions                  : {tot_q}")
    if tot_q:
        print(f"correct answer is longest  : {tot_long} ({tot_long/tot_q*100:.1f}%)   [~25% = chance]")
        print(f"  ...by a gameable margin  : {tot_game} ({tot_game/tot_q*100:.1f}%)"
              f"   [>={MARGIN_CHARS} chars and >={MARGIN_FRAC:.0%} longer]")
    print(f"files over {args.threshold:.0%} gameable      : {len(flagged)}")
    for r in flagged[:25]:
        print(f"   {r['gameable_pct']*100:5.1f}%  {r['gameable']:3d}/{r['n']:3d}  {r['file']}")
    if args.json_out:
        with open(args.json_out, "w") as fh:
            json.dump({"totals": {"questions": tot_q, "longest": tot_long, "gameable": tot_game},
                       "files": results, "unread": unread}, fh, indent=1)
        print(f"\nwrote {args.json_out}")
    sys.exit(1 if (flagged or unread) else 0)


if __name__ == "__main__":
    main()
