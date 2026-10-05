#!/usr/bin/env python3
"""One runner for the standing Semester 2 checks on an exam folder.

    python3 tools/check_all.py "Pharmacology I Exam 3"          # everything
    python3 tools/check_all.py "Pharmacology I Exam 3" --fast   # skip the slow guide-link pair

Runs, in order: answer-key consistency, exam standard (--new), self-contained,
lead-in present, length bias (fast, node), pool cites, US spelling, spelling vs
the inbox (advisory, only if the inbox folder exists), accordions closed, then
build_guide_links + check_guide_links --strict LAST (rewrites guide-links.json;
skipped by --fast).

DELIBERATELY EXCLUDED: check_console_errors.py, check_answer_distribution.py and
check_dark_contrast.py. They hit live Firebase and answering a quiz writes real
class data. Never add them here.

Prints one summary table (check, status, one-line reason). Exit 1 on any FAIL;
WARN (advisory) never fails. Per-check output is trimmed to its last line; rerun
the single checker for detail.
"""
import os, re, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PY = sys.executable


def run(args, timeout=900):
    t = time.time()
    try:
        p = subprocess.run([PY] + args, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
        out = (p.stdout + "\n" + p.stderr).strip()
        rc = p.returncode
    except subprocess.TimeoutExpired:
        out, rc = "timed out after %ds" % timeout, 124
    lines = [l.strip() for l in out.splitlines() if l.strip()]
    # prefer a summary-looking line; otherwise the last line
    pick = ""
    if rc != 0:  # on failure prefer the line that names the failure
        for l in lines:
            if re.search(r"HARD references:|FAIL|MISMATCH|ERROR|UNREADABLE|over \d+%", l):
                pick = l
                break
    for l in ([] if pick else reversed(lines)):
        if re.search(r"\b(pass|fail|ok|clean|flag|found|checked|scanned|gameable|hit|error|mismatch|verified|\d+)\b", l, re.I):
            pick = l
            break
    return rc, (pick or (lines[-1] if lines else "(no output)"))[:110], round(time.time() - t, 1)


def main(argv):
    fast = "--fast" in argv
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1:
        print(__doc__)
        return 2
    folder = args[0].rstrip("/")
    if not os.path.isdir(os.path.join(ROOT, folder)):
        print("no such folder in repo: %r" % folder)
        return 2
    m = re.match(r"(.+) (Exam \d+)$", folder)
    inbox = None
    if m:
        cand = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/%s Inbox/%s" % (m.group(1), m.group(2)))
        inbox = cand if os.path.isdir(cand) else None

    checks = [  # (name, args, advisory)
        ("answer keys", ["tools/check_answer_key_consistency.py", folder], False),
        ("exam standard (--new)", ["tools/check_exam_standard.py", "--new"], False),
        ("self-contained", ["tools/check_self_contained.py", folder], False),
        ("lead-in present", ["tools/check_leadin_present.py", folder], False),
        ("length bias (fast)", ["tools/check_length_bias_fast.py", folder], False),
        ("pool cites", ["tools/check_pool_cites.py"], False),
        ("US spelling", ["tools/check_us_spelling.py"] + sorted(
            os.path.join(folder, f) for f in os.listdir(os.path.join(ROOT, folder))
            if f.endswith((".html", ".json"))), False),
    ]
    if inbox:
        checks.append(("spelling vs inbox", ["tools/check_spelling.py", folder, inbox], True))
    checks.append(("accordions closed", ["tools/check_accordions_closed.py"], False))
    if not fast:
        checks.append(("build_guide_links", ["tools/build_guide_links.py", folder], False))
        checks.append(("guide links --strict", ["tools/check_guide_links.py", "--strict"], False))

    rows, hard = [], 0
    for name, a, adv in checks:
        rc, why, secs = run(a)
        status = "PASS" if rc == 0 else ("WARN" if adv else "FAIL")
        if status == "FAIL":
            hard += 1
        rows.append((name, status, why, secs))
        print("  %-22s %-4s %5.1fs" % (name, status, secs), flush=True)
    print("\n%s%s" % (folder, "  [--fast: guide links skipped]" if fast else ""))
    print("%-22s %-5s %s" % ("check", "state", "reason (last relevant line)"))
    print("-" * 100)
    for name, status, why, _ in rows:
        print("%-22s %-5s %s" % (name, status, why))
    if not inbox:
        print("(spelling vs inbox skipped: no inbox folder for this exam)")
    print("-" * 100)
    print("%d hard failure(s)" % hard)
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
