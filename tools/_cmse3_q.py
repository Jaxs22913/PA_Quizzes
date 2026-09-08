# -*- coding: utf-8 -*-
"""Question helper for the Lecture 18 and 19 topic quizzes.

Four options (Jaxon, 2026-09-08: "topic quizzes just 4 as well"), and the same
explanation contract the master exams use -- a reason on every option rather
than a dismissal. Thinner than _cmsent_style.Q because the topic-quiz
partitioner supplies its own rotation and expects the key at index 0.
"""
import re

MIN_EXPL = 80
MIN_KEY = 110
BANNED = re.compile(r"(?i)\b(not correct|is incorrect|does not apply|not the answer|"
                    r"wrong answer|not right|obviously|nope)\b")


def Q(topic, io, q, opts, cite):
    assert len(opts) == 4, "four options: %s" % q[:60]
    assert len({o[0].strip().lower() for o in opts}) == 4, "duplicate option: %s" % q[:60]
    assert len({o[1].strip() for o in opts}) == 4, "shared explanation: %s" % q[:60]
    assert re.match(r"correct\b", opts[0][1], re.I), \
        "the key is authored FIRST and its explanation opens 'Correct': %s" % q[:60]
    assert len(opts[0][1]) >= MIN_KEY, \
        "key explanation %d chars, needs %d: %s" % (len(opts[0][1]), MIN_KEY, q[:60])
    for o in opts[1:]:
        assert not re.match(r"correct\b", o[1], re.I), "distractor opens 'Correct': %s" % o[0]
        assert len(o[1]) >= MIN_EXPL, \
            "explanation for %r is %d chars, needs %d" % (o[0][:40], len(o[1]), MIN_EXPL)
        assert not BANNED.search(o[1]), "vacuous phrasing for %r" % o[0][:40]
    return {"topic": topic, "io": io, "q": q, "opts": opts, "c": 0, "cite": cite}
