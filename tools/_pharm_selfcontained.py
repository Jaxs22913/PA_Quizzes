# -*- coding: utf-8 -*-
"""Make the Pharmacology I explanations self-contained.

Requirement, 2026-08-30: a question must not depend on having been in the room.
"According to the lecture", "the deck says", "Dr. Wood said" all fail that --
a classmate revising from the site has no lecture to consult.

Stems and options were cleared by the stem rewrites. This handles the
EXPLANATIONS, which carried 610 references. Rules are deletions and simple
substitutions that leave grammatical prose; anything a rule cannot clean is
reported for a hand fix rather than mangled.
"""
import re

# Eight explanations the rules cannot clean without mangling the sentence --
# deleting the attribution strands the verb ("Not what states"). Hand-written.
OVERRIDES = {
 "Bleaching rather than staining is what the lecture describes.":
   "Bleaching rather than staining is the effect.",
 "Correct \u2014 another prodrug in a lecture full of them, alongside valacyclovir, famciclovir and valganciclovir.":
   "Correct \u2014 one of several prodrugs, alongside valacyclovir, famciclovir and valganciclovir.",
 "Enzymatic inactivation is what the lecture specifies.":
   "Enzymatic inactivation is the mechanism.",
 "It is the exception among ganglionic agents in the lecture.":
   "It is the exception among the ganglionic agents.",
 "It targets both A and B, and the lecture gives a defined season.":
   "It targets both A and B, and there is a defined season.",
 "Not what the lecture states.": "That is not the case.",
 "The lecture credits them with an improvement.": "They are credited with an improvement.",
 "The lecture lists it among the significant interactions.":
   "It is among the significant interactions.",
}


RULES = [
 # Attributions are DELETED, not relabelled. Renaming "the lecture" to "the
 # material" would leave the same dependency on an outside source; the fix is
 # for the explanation to assert the fact on its own.
 (r",?\s+(?:in|per|from|according to)\s+(?:this|the)\s+lectures?\b", ""),
 (r"^(?:In|Per|According to)\s+(?:this|the)\s+lectures?,\s*", ""),
 (r"\s*\((?:in|per|from)\s+(?:this|the)\s+lectures?\)", ""),
 # trailing relative clauses: "the reason the lecture gives" -> "the reason"
 (r"\s+(?:that\s+)?the lectures?\s+(?:gives|lists|names|describes|specifies|"
  r"identifies|uses|makes|provides|attributes|reserves|warns|places|covers)\b", ""),
 # fixed idioms that need a real rewrite rather than a deletion
 (r"^The lectures?\s+(?:states|says|notes)\s+the opposite\.?$", "The opposite is true."),
 (r"^The lectures?\s+(?:is|was)\s+explicit\b", "This is explicit"),
 # leading "The lecture VERBs X" -> "X"
 (r"^The lectures?\s+(?:gives|lists|names|specifies|identifies|provides|describes|"
  r"calls|defines|covers|places|reserves|attributes|links|pairs|assigns|adds|"
  r"states|says|notes|mentions|warns|puts|includes)\s+", ""),
 # possessives
 (r"\bthe lecture's own\b", "the"),
 (r"\bthe lecture's account\b", "the material"),
 (r"\bthe lecture's\b", "the"),
 # last resort
 (r"^The lectures?\s+", ""),
 (r"\s+the lectures?\b", ""),
 (r"\bthis lectures?\b", "this"),
 (r"\bthe lectures?\b", ""),
]
TIDY = [
 (r"\s{2,}", " "),
 (r"\s+([.,;:])", r"\1"),
 (r"\.\.+", "."),
 (r"^\s*,\s*", ""),
 (r"\bthe material the material\b", "the material"),
 (r"\bin the material given\b", "given"),
]


def clean(text):
    if text in OVERRIDES:
        return OVERRIDES[text]
    out = text
    for pat, rep in RULES:
        out = re.sub(pat, rep, out, flags=re.I)
    for pat, rep in TIDY:
        out = re.sub(pat, rep, out)
    out = out.strip()
    if out and out[0].islower():
        out = out[0].upper() + out[1:]
    return out
