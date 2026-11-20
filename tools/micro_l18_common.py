# -*- coding: utf-8 -*-
"""Shared helpers for the Microbiology Lecture 18 pools (DNA Viruses of Medical Importance, Dr. Webster,
13 November 2026): tools/micro_l18_pool_a.py ... pool_e.py. Same item shape as the Lecture 17 pools
(tools/micro_l17_pool_c.py): key authored at index 0 with the only "Correct." opener; `mis` per distractor;
QO for ascending numeric options (never rotated)."""
SRC = "Lecture 18  Dr. Webster -  DNA viruses of medical importance.pptx"
IMG = "micro-exam-3-quiz-images"

IO1 = "1 — Recall the steps of DNA virus replication."
IO2 = ("2 — Compare and contrast the characteristics of a lytic viral infection versus a persistent chronic or "
       "persistent latent infection.")
IO3 = "3 — Differentiate between oncogenic and teratogenic viruses."
IO4 = ("4 — Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases, clinical "
       "manifestations, methods of treatment, and prevention of DNA viruses of medical importance.")
IO5 = ("5 — Compare and contrast the mode of transmission, clinical manifestations, and availability of a vaccine for "
       "DNA viruses of medical importance.")


def c(*n):
    return f"{SRC}, Slide " + (str(n[0]) if len(n) == 1 else ", ".join(map(str, n[:-1])) + " and " + str(n[-1]))


def ci(img, *n):
    """cite with a picture slide: c(n...) + ' and image on Slide img'"""
    return (c(*n) + f" and image on Slide {img}") if n else c(img)


def Q(topic, io, q, key, wrong, cite, **kw):
    """key = (text, explanation); wrong = [(text, explanation, misconception), x3]. Key authored at 0."""
    assert len(wrong) == 3, q
    d = dict(topic=topic, io=io, q=q,
             opts=[[key[0], key[1]]] + [[t, e] for t, e, _ in wrong],
             mis={t: m for t, _, m in wrong}, c=0, cite=cite)
    d.update(kw)
    return d


def QO(topic, io, q, options, key_index, cite, **kw):
    """ORDERED (numeric) options, listed ASCENDING: options = [(text, explanation, misconception or None) x4];
    the key's misconception is None. Never rotated by the partition."""
    assert len(options) == 4 and options[key_index][2] is None, q
    d = dict(topic=topic, io=io, q=q, opts=[[t, e] for t, e, _ in options],
             mis={t: m for i, (t, _, m) in enumerate(options) if i != key_index}, c=key_index, cite=cite,
             ordered=True)
    d.update(kw)
    return d
