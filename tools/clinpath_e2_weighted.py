# -*- coding: utf-8 -*-
"""Shared split-and-guard logic for the Clinical Pathophysiology I Exam 2 lectures that
have a recording to weight by (Lecture 8 Immunity, Lecture 9 Pulmonary).

Same guards as clinpath_vascular_partition.py (the Lecture 7 build this follows), plus
the two things those lectures add:

  MINUTES-WEIGHTED QUOTAS. [[transcript_emphasis_measurement]]: weight by MINUTES spoken,
  never word counts. Each topic is a run of slides; its share of the 60 questions
  (2 x 30, [[clin_path_exam_spec]]) is its share of the minutes the slides were on
  screen / narrated, rounded by largest remainder. Time spoken never adds content:
  a topic needs both minutes AND deck facts, so a topic's quota is capped at the
  questions its slides could support, and the cap's overflow goes to the next
  largest remainder.

  WRITER.md v1 (2026-10-15). Every distractor carries its misconception as a third
  option element from MIS; numeric and other ordered option sets (q["ordered"])
  are authored ascending and keep their positions, and the free questions are
  rotated around them so each set's answer positions stay even.

NO MANAGEMENT, asserted on every option and every explanation: the spec draws this
course's line against Clinical Medicine and Surgery at mechanism against management.
"""
import json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _option_order import option_values, order_options

NOPT, PER_SET, BAR = 4, 30, 0.35
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
CITES = re.compile(r"(?i)\b(lecture|slide|deck|professor|this course|in class|lecturer)\b")
MGMT = re.compile(r"(?i)\b(first-line|first line|drug of choice|treatment of choice|next step|"
                  r"how is it treated|treat with|treated with|managed with|prescrib\w*|"
                  r"epinephrine|antihistamine\w*|give antibiotics|antibiotic therapy|bronchodilat\w*|inhaler\w*|"
                  r"corticosteroid\w*|steroid\w*|oxygen therapy|supplemental oxygen|ventilator settings|"
                  r"intubat\w*|chest tube|thoracentesis|thoracostomy|needle decompression|"
                  r"lobectomy|chemotherapy|radiation therapy|surgical repair|anticoagula\w*|"
                  r"thrombolys\w*|vaccinate the|give the patient)\b")
VIGNETTE = re.compile(r"(?i)^\s*(a|an)\s+\d{1,3}[- ]year[- ]old|^\s*a\s+patient\b|^\s*a\s+\d")
MIS = ("competing diagnosis", "wrong stage or severity", "ruled out by a stated finding",
       "confused mechanism or drug class", "adjacent fact", "reversed direction or value",
       "common lay belief")
ABSOL = re.compile(r"\b(always|never|only|all|none)\b", re.I)


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    r = max(L[:c] + L[c + 1:])
    return L[c] > r and (L[c] - r) >= MARGIN_CHARS and L[c] >= r * (1 + MARGIN_FRAC)


def check(pool, topics):
    seen = set()
    for i, q in enumerate(pool):
        w = "pool[%d] %r" % (i, q["q"][:50])
        assert q["topic"] in topics, "%s: topic %r has no slide range" % (w, q["topic"])
        assert len(q["opts"]) == NOPT, "%s: %d options" % (w, len(q["opts"]))
        assert "?" in q["q"], "%s: stem asks nothing" % w
        assert not CITES.search(q["q"]), "%s: stem cites the course" % w
        assert not VIGNETTE.search(q["q"]), "%s: stem is a vignette" % w
        assert not MGMT.search(q["q"]), "%s: management in the stem" % w
        assert q.get("cite"), "%s: no citation" % w
        if not q.get("ordered"):
            assert q["c"] == 0, "%s: key must be authored first" % w
            assert option_values([o[0] for o in q["opts"]]) is None, \
                "%s: numeric options must be marked ordered and authored ascending" % w
        else:
            vals = option_values([o[0] for o in q["opts"]])
            if vals is not None:
                assert order_options(q)["c"] == q["c"], "%s: numeric options not ascending" % w
        for j, o in enumerate(q["opts"]):
            t, e = o[0], o[1]
            assert not MGMT.search(t), "%s: management in an option: %r" % (w, t)
            assert not MGMT.search(e), "%s: management in an explanation: %r" % (w, e[:70])
            assert not CITES.search(e), "%s: explanation cites the course: %r" % (w, e[:70])
            assert len(e) >= 60, "%s: explanation too thin: %r" % (w, e[:60])
            assert e.lower().startswith("correct") == (j == q["c"]), "%s: option %d Correct-prefix" % (w, j)
            if j != q["c"]:
                assert len(o) == 3 and o[2] in MIS, "%s: distractor %d needs a mis tag" % (w, j)
                if ABSOL.search(t) and not ABSOL.search(q["opts"][q["c"]][0]):
                    print("  note: absolute in a distractor only:", w, repr(t))
            else:
                assert len(o) == 2, "%s: the key carries no mis tag" % w
        assert q["q"] not in seen, "%s: duplicate stem" % w
        seen.add(q["q"])
        assert len({o[0] for o in q["opts"]}) == NOPT, "%s: duplicate option" % w


def quotas(pool, topics, minutes, total):
    """topics: {name: [slides]}; minutes: {slide: min}. -> {topic: n}, summing to total."""
    have = {t: sum(1 for q in pool if q["topic"] == t) for t in topics}
    mins = {t: sum(minutes.get(s, 0.0) for s in sl) for t, sl in topics.items()}
    tot = sum(mins.values())
    exact = {t: total * m / tot for t, m in mins.items()}
    q = {t: min(int(exact[t]), have[t]) for t in topics}
    while sum(q.values()) < total:
        open_ = [t for t in topics if q[t] < have[t]]
        assert open_, "pool too small for %d questions" % total
        t = max(open_, key=lambda t: (exact[t] - q[t], mins[t]))
        q[t] += 1
    return q, mins, exact


def split(pool, topics, minutes, seed, out_name, label):
    check(pool, topics)
    rng = random.Random(seed)
    q_n, mins, exact = quotas(pool, topics, minutes, 2 * PER_SET)
    print("%s: %d in pool, %.1f minutes across %d topics" % (label, len(pool), sum(mins.values()), len(topics)))
    print("  %-40s %6s %6s %5s %5s" % ("topic", "min", "exact", "quota", "pool"))
    chosen = []
    for t in topics:
        items = [q for q in pool if q["topic"] == t]
        core = [q for q in items if q.get("core")]
        rest = [q for q in items if not q.get("core")]
        rng.shuffle(core); rng.shuffle(rest)
        take = (core + rest)[:q_n[t]]
        chosen.append((t, take))
        print("  %-40s %6.1f %6.2f %5d %5d" % (t, mins[t], exact[t], q_n[t], len(items)))
    picked = {q["io"] for _, take in chosen for q in take}
    missing = sorted({q["io"] for q in pool} - picked)
    assert not missing, "objective(s) with no question in either set (mark one core): %r" % missing
    # Deal each topic across the two sets, the larger topics first, always to the
    # emptier set, so both sets cover every topic at its weight.
    sets = [[], []]
    flip = 0
    for t, take in sorted(chosen, key=lambda x: -len(x[1])):
        for q in take:
            k = 0 if len(sets[0]) < len(sets[1]) else 1 if len(sets[1]) < len(sets[0]) else flip
            flip ^= 1
            sets[k].append(q)
    out = {}
    for n, qs in enumerate(sets, 1):
        assert len(qs) == PER_SET, "set%d has %d" % (n, len(qs))
        rng.shuffle(qs)
        fixed = {i: q["c"] for i, q in enumerate(qs) if q.get("ordered")}
        want = [PER_SET // NOPT + (1 if k < PER_SET % NOPT else 0) for k in range(NOPT)]
        rng.shuffle(want)                     # which positions get the odd extra two
        for v in fixed.values():
            want[v] -= 1
        free = []
        for k in range(NOPT):
            free += [k] * max(0, want[k])
        need = len(qs) - len(fixed)
        while len(free) < need:               # fixed keys overfilled a position
            cnt = [free.count(k) + list(fixed.values()).count(k) for k in range(NOPT)]
            free.append(cnt.index(min(cnt)))
        free = free[:need]
        rng.shuffle(free)
        it = iter(free)
        rot = []
        for i, q in enumerate(qs):
            r = json.loads(json.dumps(q))
            if i in fixed:
                rot.append(r)
                continue
            t = next(it)
            o = r["opts"]; key = o.pop(0); o.insert(t, key)
            r["c"] = t
            rot.append(r)
        for i, r in enumerate(rot):
            assert r["opts"][r["c"]][1].lower().startswith("correct"), "set%d q%d: key moved" % (n, i)
            r.pop("core", None)
        pos = [sum(1 for r in rot if r["c"] == k) for k in range(NOPT)]
        assert max(pos) - min(pos) <= 1, "set%d uneven: %r" % (n, pos)
        frac = sum(gameable(r["opts"], r["c"]) for r in rot) / len(rot)
        assert frac <= BAR, "set%d: key longest in %.0f%%" % (n, frac * 100)
        tops = {}
        for r in rot:
            tops[r["topic"]] = tops.get(r["topic"], 0) + 1
        out["set%d" % n] = rot
        print("set%d  %d questions  positions=%s  key-is-longest=%.0f%%  ordered=%d"
              % (n, len(rot), dict(zip("ABCD", pos)), frac * 100, len(fixed)))
    path = os.path.join(HERE, out_name)
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", out_name)
    return out
