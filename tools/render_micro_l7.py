#!/usr/bin/env python3
"""Render Microbiology Exam 2, Lecture 7 — Disorders in Immunity.

Palette and header shape inherited from Exam 1 so the class reads as one.
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 2")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["Immunopathologies", "The four types", "Allergy management",
         "Transfusion reactions", "Transplantation", "Autoimmunity",
         "Immunodeficiency", "Carcinogenesis", "Immunotherapy"]
INTRO = ("Lecture 7 of Microbiology &mdash; Disorders in Immunity. Thirty questions, every one "
         "cited to the slide it came from. "
         "<b>One table organizes most of this lecture.</b> The four hypersensitivities differ by "
         "effector mechanism, and everything else follows from it: I is IgE on mast cells and is "
         "<i>immediate</i>; II is IgG or IgM against <i>cell surface</i> antigen with complement "
         "lysis; III is IgG or IgM against <i>soluble</i> antigen forming complexes that lodge in "
         "basement membranes; IV is <i>T cell</i> mediated and therefore <i>delayed</i>. Learn the "
         "mechanism and the examples place themselves. "
         "<b>Watch for the diseases that cross types.</b> Asthma begins as type I in the acute "
         "response and becomes type IV when chronic. Autoimmunity involves every type except I. "
         "Transplant rejection uses three different types depending on how fast it happens. "
         "<b>The hygiene hypothesis is the one piece of reasoning worth following in full</b> "
         "&mdash; helminth infection produces exactly the allergic profile (TH2, high IgE, "
         "eosinophils, mast cells) and yet no allergic disease, because nonspecific IgE crowds "
         "the Fc receptors and regulatory T cells suppress the response. "
         "Covers the four immunopathologies; the cells shared by defense and allergy; the four "
         "hypersensitivity types with their examples; allergens and portals of entry; "
         "sensitizing and provocative doses; the skin, nasal, gut and airway manifestations; "
         "anaphylaxis and how epinephrine reverses it; the late phase reaction; allergy "
         "diagnosis and the three management strategies including desensitization; and "
         "transfusion reactions through ABO, cross-matching, Rh factor and Rhogam; "
         "graft types and the rejection timeline (hyperacute type II, acute type IV, chronic type III, "
         "graft versus host type IV) with the tissues that tolerate mismatch; the origins of "
         "autoimmunity and its type II, III and IV diseases; primary against secondary "
         "immunodeficiency; carcinogenesis, oncogenic viruses and tumor evasion; and the "
         "immunotherapies from checkpoint inhibitors to cancer vaccines.")

sets = json.load(io.open(os.path.join(HERE, "micro_l7_sets.json"), encoding="utf-8"))
for n, key, fname in ((1, "set1", "disorders-in-immunity-quiz.html"),
                      (2, "set2", "disorders-in-immunity-quiz-version-2.html")):
    html = render(
        title="Disorders in Immunity &mdash; Quiz %d" % n,
        h1="Disorders in Immunity",
        sub="Microbiology &middot; Exam 2 &middot; Lecture 7 &middot; Set %d" % n,
        pill="30 questions",
        chips=CHIPS,
        intro=INTRO,
        questions=sets[key],
        already_converted=True,
        **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, fname)
    io.open(p, "w", encoding="utf-8").write(html)
    print("wrote %s  (%d KB)" % (fname, len(html) // 1024))
