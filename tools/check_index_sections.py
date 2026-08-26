"""Verify every quiz on index.html is listed under the right section divider.

Background: on 2026-08-25 Jaxon noticed three Pigmented Skin Lesions quizzes
(Quiz 2, Vignettes 1, Vignettes 2) sitting under CMS I Exam 1's "Master
Exams" divider instead of "Individual Topic Exam". A master exam is a
cumulative 60-question form drawn across the whole block; a topic quiz is
30 questions on one lecture. Filing one under the other misrepresents what
a student is about to sit down and take.

Nothing caught it because index.html is hand-edited: a new quiz gets its
<li> appended, and if the cursor is past the closing </ul> of the topic
list it lands in the master list instead. Both render identically -- a
bulleted link -- so it is invisible unless you read the divider above it.

The rule this enforces is the one the site already follows everywhere else:
a link under a "Master Exams" divider must be a master exam, and a link
under an "Individual Topic Exam" divider must not be. Classification is by
BOTH the visible label and the href, and the two must agree; a page whose
filename says master-exam but whose label doesn't (or vice versa) is
reported rather than quietly resolved, because that mismatch is itself a
mistake worth a human look.

Also checks, since it has the list parsed anyway:
  - every quiz-link target actually exists on disk
  - no quiz is linked twice from the same page

Run:
    python3 tools/check_index_sections.py           # checks index.html
    python3 tools/check_index_sections.py foo.html  # or specific pages

Exit status is 1 if anything is wrong, so it can gate a build.
"""
import os
import re
import sys
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DIVIDER = re.compile(r'<div class="divider"><span>(.*?)</span></div>', re.S)
LINK = re.compile(r'<a class="quiz-link" href="([^"]+)"[^>]*>(.*?)</a>', re.S)

# A divider whose text contains one of these introduces master exams.
MASTER_DIVIDER = ("master exam",)
# ...and one of these introduces per-lecture topic quizzes.
TOPIC_DIVIDER = ("individual topic exam", "topic exam", "individual topic")


def _scope_end(src, start, hard_stop):
    """Where a divider's list ends.

    A divider owns everything up to the next divider -- but no further than
    the container it lives in. The practicum pages nest <details> groups and
    put a divider inside one of them, so a flat scan to the next divider
    runs straight through the closing tag and swallows the sibling groups'
    links. Track <details> depth and stop as soon as we close out past the
    level the divider sits at.
    """
    depth = 0
    for m in re.finditer(r"<details\b|</details>", src[start:hard_stop]):
        if m.group(0) == "</details>":
            if depth == 0:
                return start + m.start()
            depth -= 1
        else:
            depth += 1
    return hard_stop


def _text(html):
    """Visible text of a fragment: strip tags, decode the few entities used."""
    t = re.sub(r"<[^>]+>", "", html)
    for ent, ch in (("&mdash;", "-"), ("&ndash;", "-"), ("&amp;", "&"),
                    ("&shy;", ""), ("&nbsp;", " ")):
        t = t.replace(ent, ch)
    return " ".join(t.split())


def _is_master(label, href):
    """Classify a link, or return None if the label and href disagree."""
    by_label = ("master exam" in label.lower()
                or "comprehensive" in label.lower())
    by_href = "master-exam" in unquote(href).lower()
    if by_label != by_href:
        return None
    return by_label


def check(path):
    rel = os.path.relpath(path, ROOT)
    src = open(path, encoding="utf-8").read()
    problems = []

    # Walk dividers in document order; each one owns the markup up to the
    # next divider, which is where its links live.
    marks = [(m.start(), m.end(), _text(m.group(1))) for m in DIVIDER.finditer(src)]
    # Every quiz link on the page, divider or not, gets the cheap checks.
    seen = {}
    for m in LINK.finditer(src):
        href = m.group(1)
        line = src.count("\n", 0, m.start()) + 1
        seen.setdefault(href, []).append(line)
        if not os.path.exists(os.path.join(os.path.dirname(path), unquote(href))):
            problems.append("%s:%d  link target does not exist: %s"
                            % (rel, line, unquote(href)))

    scoped = 0
    for i, (start, end, title) in enumerate(marks):
        stop = _scope_end(src, end, marks[i + 1][0] if i + 1 < len(marks) else len(src))
        low = title.lower()
        wants_master = any(k in low for k in MASTER_DIVIDER)
        wants_topic = any(k in low for k in TOPIC_DIVIDER)
        for m in LINK.finditer(src[end:stop]):
            href, label = m.group(1), _text(m.group(2))
            line = src.count("\n", 0, end + m.start()) + 1
            scoped += 1
            is_master = _is_master(label, href)
            if is_master is None:
                problems.append(
                    "%s:%d  label and filename disagree about whether this is a "
                    "master exam: %r -> %s" % (rel, line, label, unquote(href)))
            elif wants_master and not is_master:
                problems.append(
                    "%s:%d  %r is under the %r divider but is a per-topic quiz, "
                    "not a master exam -- move it up into the topic list"
                    % (rel, line, label, title))
            elif wants_topic and is_master:
                problems.append(
                    "%s:%d  %r is under the %r divider but is a master exam -- "
                    "move it down into the master list" % (rel, line, label, title))

    for href, lines in sorted(seen.items()):
        if len(lines) > 1:
            problems.append("%s  linked %d times (lines %s): %s"
                            % (rel, len(lines), ", ".join(map(str, lines)),
                               unquote(href)))

    return problems, len(seen), scoped, len(marks)


def main(argv):
    paths = argv[1:] or [os.path.join(ROOT, "index.html")]
    bad = 0
    for p in paths:
        p = os.path.abspath(p)
        problems, nlinks, scoped, ndiv = check(p)
        label = os.path.relpath(p, ROOT)
        if problems:
            bad += len(problems)
            for line in problems:
                print(line)
        print("%-14s %4d quiz links (%d under one of %d section dividers) -- %s"
              % (label, nlinks, scoped, ndiv,
                 "%d PROBLEM(S)" % len(problems) if problems else "ok"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
