#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Make every vignette stem stand on its own.

REPORTED BY A STUDENT, 25 August 2026, through the report-a-mistake form:
"Multiple questions not giving the diagnosis to answer", on Benign Skin Lesions
Vignettes 2, citing:

    "The same patient is not bothered by her lesion but wants to know her
     options. Which is the most appropriate answer?"

They are right, and it is my doing. These stems were written as CHAINS -- one
vignette sets the scene, the next two say "the same patient". That never worked,
because the partitioner SHUFFLES: the questions land in different sets, in a
different order, sometimes in different quizzes entirely. Nothing guaranteed the
setup question was anywhere nearby, or present at all.

It only became visible when I hid the topic tag, because until then the tag said
"Dermatofibroma" above the stem and quietly supplied the missing lesion. One bug
was masking the other. Fixing the giveaway exposed the dependency, and the
student hit it the same day.

THE GUARD THAT SHOULD HAVE CAUGHT THIS DID NOT. Every vignette partition carries

    _DEP = re.compile(r"previous question|question above|as in the last|earlier question")

which is the phrasing I IMAGINED a dependent stem would use, not the phrasing I
actually wrote, which is "The same patient". A guard tested only against the
cases you thought of is a guard that passes.

Each stem below now carries its own clinical detail, taken from the setup
question it used to lean on, so it can be read cold in any order.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

REWRITE = {
 "tools/cms_l7_vig_a.py": [
  ("The same patient asks what will happen to his scar over the next year. Which is the most appropriate answer?",
   "A 30-year-old man had an appendicectomy five weeks ago. The scar is raised, firm and red but stops exactly at the edges of the original incision. He asks what will happen to it over the next year. Which is the most appropriate answer?"),
  ("The same patient wants the lesions removed for cosmetic reasons. Which is the most appropriate approach?",
   "A 58-year-old woman with obesity has several soft, skin-coloured, pedunculated papules on a thin stalk in both axillae and on her neck. She wants them removed for cosmetic reasons. Which is the most appropriate approach?"),
 ],
 "tools/cms_l7_vig_b.py": [
  ("The same patient's abscess is tense and fluctuant. Which is the most appropriate immediate management?",
   "A 22-year-old lorry driver has sudden pain and swelling over his sacrum. There is a warm, tender, erythematous swelling that is now tense and fluctuant. Which is the most appropriate immediate management?"),
  ("Dermoscopy is performed on that patient's leg lesion. Which finding would support the diagnosis?",
   "A 34-year-old woman has a firm brown nodule on her lower leg that appeared after an insect bite. Dermoscopy is performed. Which finding would support a diagnosis of dermatofibroma?"),
  ("The same patient is not bothered by her lesion but wants to know her options. Which is the most appropriate answer?",
   "A 34-year-old woman has a firm 8 mm brown nodule on her lower leg that retracts beneath the skin when compressed from the sides. She is not bothered by it but wants to know her options. Which is the most appropriate answer?"),
  ("The patient asks whether his lesion is a sebaceous cyst full of oil. Which is the most appropriate response?",
   "A 45-year-old man has a firm, movable, round nodule on his upper back with a small central pore that expresses cream-coloured pasty material. He asks whether it is a sebaceous cyst full of oil. Which is the most appropriate response?"),
  ("The same patient asks about having them removed. Which is the most appropriate counselling point?",
   "A 17-year-old girl has multiple 1 to 2 mm skin-coloured papules symmetrically distributed on both lower eyelids and upper cheeks. She asks about having them removed. Which is the most appropriate counselling point?"),
 ],
 "tools/cms_l7_vig_c.py": [
  ("The same mother asks whether the lesion will need surgery. Which is the most appropriate answer?",
   "A 6-week-old former preterm girl has a bright red raised plaque on her scalp. Her mother says the area first looked pale, then developed fine red lines, and now asks whether it will need surgery. Which is the most appropriate answer?"),
  ("The same patient asks whether removing them will stop new ones appearing. Which is the most appropriate response?",
   "A 61-year-old man has several smooth, firm, deep red papules under 5 mm on his trunk that blanch with pressure and have accumulated over recent years. He asks whether removing them will stop new ones appearing. Which is the most appropriate response?"),
  ("The same patient is not troubled by the lesion. Which is the most appropriate management?",
   "A 48-year-old man has a soft, painless, rubbery subcutaneous nodule about 4 cm across on his back. It is mobile with no overlying pore, and he is not troubled by it. Which is the most appropriate management?"),
 ],
 "tools/cms_l9_vig_c.py": [
  ("That same patient is not yet on antiretroviral therapy. Which is the first priority in his Kaposi sarcoma management?",
   "A 34-year-old man newly diagnosed with human immunodeficiency virus has several red-purple plaques on his legs and is not yet on antiretroviral therapy. Which is the first priority in his Kaposi sarcoma management?"),
 ],
}

# Every vignette partition gets a guard that matches what people actually write.
OLD_DEP = r'_DEP = re.compile(r"previous question|question above|as in the last|earlier question", re.I)'
NEW_DEP = '''# A stem must stand alone: the partitioner shuffles, so there is no "previous
# question". The original version of this pattern listed only the phrasings I
# imagined -- "previous question", "question above" -- and missed the one I had
# actually written thirteen times, "The same patient". A student found it before
# the guard did. It now matches back-references anywhere in the stem, not just
# the explicit ones.
_DEP = re.compile(r"previous question|question above|as in the last|earlier question"
                  r"|\\b(?:that|the same|this same) (?:patient|man|woman|girl|boy|mother|"
                  r"father|child|infant|lesion|nodule|plaque|rash|scar)\\b"
                  r"|\\bthe patient (?:above|described above)\\b", re.I)'''


def main():
    root = os.path.dirname(HERE)
    total = 0
    for rel, pairs in REWRITE.items():
        p = os.path.join(root, rel)
        s = open(p, encoding="utf-8").read()
        for old, new in pairs:
            if new in s:
                continue
            assert s.count(old) == 1, "stem not found exactly once in %s: %r" % (rel, old[:60])
            s = s.replace(old, new)
            total += 1
        open(p, "w", encoding="utf-8").write(s)
    print("rewrote %d dependent stem(s) to stand alone" % total)

    import glob
    n = 0
    for f in sorted(glob.glob(os.path.join(HERE, "cms_l*_vig_partition.py"))):
        s = open(f, encoding="utf-8").read()
        if "that|the same|this same" in s:
            continue
        assert s.count(OLD_DEP) == 1, "dep guard not found once in %s" % os.path.basename(f)
        open(f, "w", encoding="utf-8").write(s.replace(OLD_DEP, NEW_DEP))
        n += 1
    print("widened the dependency guard in %d partition(s)" % n)


if __name__ == "__main__":
    main()
