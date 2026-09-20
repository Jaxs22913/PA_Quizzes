"""Rewrite a stem so it stops citing the course, keeping its meaning.

Two grammatical cases, and conflating them is what breaks the naive version:

  1. The subject is a wh-NOUN phrase -- "Which symptom does the deck give for
     entropion?" The noun is already fronted, so plain passive works:
     "Which symptom is given for entropion?"

  2. The subject is a bare wh-ADVERB -- "How does the deck treat dacryoadenitis?"
     Here the object sits AFTER the verb and has to be fronted, or you get
     "How is treated dacryoadenitis". Correct: "How is dacryoadenitis treated?"

Number agreement comes from the subject noun phrase: "Which three associations"
takes "are", not "is".

Anything the rules cannot handle confidently is returned UNCHANGED and reported
for hand-rewriting. A stem whose meaning has shifted is worse than one that
still cites the deck, because nothing downstream will catch it.
"""
import re

REF = r"(?:the lecture|the deck|the slides?|the professor|the syllabus|the lecturer)"
PP = {"say":"said","give":"given","list":"listed","name":"named","describe":"described",
      "call":"called","attach":"attached","attribute":"attributed","define":"defined",
      "place":"placed","warn":"warned","order":"ordered","specify":"specified",
      "recommend":"recommended","use":"used","teach":"taught","identify":"identified",
      "state":"stated","pair":"paired","offer":"offered","group":"grouped","divide":"divided",
      "treat":"treated","rank":"ranked","cite":"cited","flag":"flagged","link":"linked",
      "allow":"allowed","expect":"expected","report":"reported","note":"noted",
      "reserve":"reserved","refer":"referred","manage":"managed","admit":"admitted",
      "select":"selected","prefer":"preferred","apply":"applied","avoid":"avoided",
      "measure":"measured","choose":"chosen","set":"set","classify":"classified",
      "advise":"advised","associate":"associated","characterise":"characterised","distinguish":"distinguished",
      "emphasise":"emphasised","require":"required","direct":"directed","mention":"mentioned",
      "contrast":"contrasted","perform":"performed","make":"made","tell":"told","position":"positioned",
      "assign":"assigned","raise":"raised","stress":"stressed","localise":"localised","include":"included",
      "support":"supported","send":"sent","prohibit":"prohibited","start":"started","leave":"left",
      "hospitalise":"hospitalised","instil":"instilled","consider":"considered","mark":"marked",
      "caution":"cautioned","draw":"drawn","qualify":"qualified","estimate":"estimated","locate":"located",
      "explain":"explained","put":"put","point":"pointed","ask":"asked","class":"classed",
      "summarise":"summarised","footnote":"footnoted","categorise":"categorised",
      "instruct":"instructed","conclude":"concluded","add":"added","imply":"implied",
      "counsel":"counselled","suggest":"suggested","exclude":"excluded",
      "favour":"favoured","single":"singled"}
# An adverb may sit between the attribution and the verb ("does the deck
# SPECIFICALLY favour"). It is part of the claim, so it is kept and re-seated
# after the auxiliary, not dropped.
ADV = r"(?:specifically|explicitly|particularly|especially|expressly)"
ADVERBS = ("how", "when", "why", "where", "how long", "how soon", "how often", "how much")

def _head(np):
    """Head noun of a noun phrase: the last word before any preposition.
    First-word fails on an adjective ("which associated findings");
    last-word-overall fails on a postmodifier ("the causes OF anemia")."""
    words = re.split(r"\s+(?:of|with|for|in|on|at|from|to|about)\b", np.strip().lower())[0].split()
    while words and words[-1].strip("?,").endswith("ly"):
        words = words[:-1]
    return words[-1].strip("?,") if words else ""

def _is_plural(head):
    return head.endswith("s") and not head.endswith(("ss", "us", "is", "sis"))

def _plural(subject):
    s = subject.strip().lower()
    if re.match(r"(?:which|what)\s+(?:two|three|four|five|six|several|both)\b", s): return True
    # Head noun = the LAST word before any preposition. First-word fails on an
    # adjective ("which associated findings"); last-word-overall fails on a
    # prepositional phrase ("which patients WITH dacryocystitis").
    m = re.search(r".*\b(?:which|what)\s+(.+)$", s)
    if not m:
        return False
    return _is_plural(_head(m.group(1)))

def _split_lead(subj):
    """Split a vignette sentence off the front of the question clause.

    Every test below inspects the START of the subject -- _plural matches
    "which|what" there, and the adverb branch matches "how|when|why|where".
    A vignette stem ("A 46-year-old man has X. Which causes ...") puts the
    vignette in the way of both, so they silently fall through to the wrong
    branch: "Which causes IS named", "How is characterised its cause".
    """
    m = re.match(r"^(.*[.!?])\s+(.*)$", subj, re.S)
    if m:
        return m.group(1) + " ", m.group(2)
    m = re.match(r"^(.*,\s+(?:and|or)\s+)((?:how|when|why|where|which|what)\b.*)$",
                 subj, re.I | re.S)
    return (m.group(1), m.group(2)) if m else ("", subj)

# Stems whose auto-rewrite I read and rejected. The rule produces grammatical
# output; it is the ATTACHMENT that is wrong ("the decision left ON steroid
# drops" -- the phrase belongs to "decision", not to "left"), which no
# surface rule can detect. Hand-written in the HAND pass instead.
REJECT = {
    "Why does the deck leave the decision on steroid drops for a corneal ulcer to ophthalmology?",
}

# Rewrites I wrote and verified by hand, where the general rule produces
# grammatical nonsense ("What is told patients to do"). Tried a rule for these
# (front the object after a bare wh-word); it fixed two stems and broke
# fifteen, because after a bare "what" the next phrase is usually a
# PREPOSITIONAL one -- "what is noted ABOUT x" -- not an object.
FORCE = {
 "A 78-year-old woman presents to a primary care clinic with sudden vision loss in one eye. What does the lecture direct the clinician to do?":
   "A 78-year-old woman presents to a primary care clinic with sudden vision loss in one eye. What is the clinician directed to do?",
 "What does the lecture tell patients to do after handling a scopolamine patch?":
   "What are patients told to do after handling a scopolamine patch?",
 "What does the lecture warn happens if oxymetazoline is used beyond three days?":
   "What happens if oxymetazoline is used beyond three days?",
 "What does the lecture advise patients about washing in acne?":
   "What are patients advised about washing in acne?",
}

def rewrite(stem):
    if stem in FORCE:
        return FORCE[stem], None
    if stem in REJECT:
        return stem, "reviewed and rejected -- hand rewrite"
    """Return (new_stem, note); note is None when the rewrite is confident."""
    m = re.search(r"^(.*?)\s+does\s+%s\s+(?:(%s)\s+)?(\w+)\b(.*)$" % (REF, ADV),
                  stem, re.I | re.S)
    if m:
        lead, subj = _split_lead(m.group(1).strip())
        adv = (m.group(2) + " ") if m.group(2) else ""
        verb, rest = m.group(3).lower(), m.group(4)
        if verb not in PP:
            return stem, "unmapped verb: %s" % verb
        pp = PP[verb]
        low = subj.lower()
        # "say" as a reporting verb ("what does the deck say IS most common")
        # cannot be passivised without nonsense -- drop the attribution instead.
        if verb == "say":
            r = rest.strip()
            if r.startswith("about "):
                return lead + f"{subj} is true of {r[6:]}", None
            if re.match(r"(is|are|was|were)\b", r):
                return lead + f"{subj} {r}", None
            if r.startswith("to "):
                return stem, "reporting 'say to ...' needs a hand rewrite"
            return stem, "reporting 'say' needs a hand rewrite"
        has_obj = bool(rest.strip().strip("?").strip())
        fronted_pp = (re.match(r"(?:for|in|among|on|at|with|under|within|above|below|beyond|after|before)\s+(?:which|what)\b",
                              low) and has_obj)
        if low in ADVERBS or low.startswith(("how ", "when ", "why ", "where ")) or fronted_pp:
            # The object sits after the verb and must be fronted, but a trailing
            # prepositional phrase must NOT come with it -- "refer a hordeolum to
            # ophthalmology" fronts "a hordeolum" and leaves "to ophthalmology"
            # after the participle, or you get "is a hordeolum to ophthalmology
            # referred". Cut the object at the first preposition.
            r = rest.strip()
            if r.startswith(","):
                return stem, "object starts at a comma"
            m2 = re.match(r"(.+?)(\s+(?:to|for|in|with|at|on|from|before|after|during|"
                          r"unless|until|once|when|if|by|against|relative)\b.*|\s*[,?].*)?$", r, re.S)
            if not m2:
                return stem, "could not split the object"
            obj, tail = m2.group(1).strip(), (m2.group(2) or "")
            # A comma after the object is fine when it introduces a SEPARATE
            # clause ("..., and how fast should it respond?") and fatal when it
            # is joining more adjectives to the same noun ("an afebrile,
            # systemically well, reliable patient").
            t = tail.lstrip()
            if re.match(r",\s*(?:and|or)\s+\w+\s*,", t):
                return stem, "appositive inside the object"
            if "," in obj or (t.startswith(",") and not re.match(
                    r",\s*(and|or|but|which|what|how|why|when|where)\b", t, re.I)):
                return stem, "comma splits the object -- needs a hand rewrite"
            if not obj or len(obj.split()) > 6:
                return stem, "object too long to front safely"
            # A fronted object that begins, ends, or is hinged on a preposition
            # means the split fell inside a prepositional phrase, and fronting
            # it strands the preposition: "Why is ABOUT THIS DESCRIPTION warned",
            # "Where are alpha-one AS placed against alpha-two receptors".
            STRAND = ("to","about","as","of","than","with","for","in","on","at",
                      "by","against","from","into","over","under")
            ow = obj.rstrip("?,").lower().split()
            if not ow:
                return stem, "empty object after the split"
            if verb == "call":
                return stem, "complex-transitive 'call' needs a hand rewrite"
            if ow[0] == "that":
                return stem, "that-clause complement, not an object"
            if ow[0] in STRAND or ow[-1] in STRAND or "as" in ow[1:-1]:
                return stem, "fronting would strand a preposition"
            head = _head(obj)
            if not head:
                return stem, "empty object after the split"
            be = "are" if _is_plural(head) else "is"
            return lead + f"{subj} {be} {obj} {adv}{pp}{tail}", None
        be = "are" if _plural(subj) else "is"
        out = lead + f"{subj} {be} {adv}{pp}{rest}"
        # self-check: a participle stranded far from its auxiliary, or a number
        # mismatch, means the split went wrong. Report rather than ship it.
        if re.search(r"\b(is|are)\s+\w+(\s+\w+){4,}\s+%s\b" % pp, out):
            return stem, "participle stranded -- hand rewrite"
        if re.search(r"\b(?:to|for|with|about|as|from|by|of|into|onto|upon|between|through|under|over|within|against|among)\s*\??\s*$", out, re.I):
            return stem, "passive strands a trailing preposition"
        SAFE = (r"to|about|that|against|for|regarding|of|on|in|at|with|by|as|"
                r"when|before|after|while|only|not|strongly|explicitly|specifically|"
                r"between|relating|during|through|without|under|over")
        if re.search(r"\b(?:is|are)\s+(?:told|asked|advised|instructed|directed|given)\s+"
                     r"(?!(?:%s)\b)\w" % SAFE, out[len(lead):], re.I):
            return stem, "passive strands an indirect object"
        if re.search(r"\b(?:is|are)\s+\w+ed\s+(?!regarding|concerning|including|following|relating|depending|involving|during)\w+ing\b", out[len(lead):], re.I):
            return stem, "gerund complement, not a passive"
        return out, None

    for pat, rep in (
        (r",?\s*(?:as|per)\s+%s\s+(?:lists?|gives?|has|states?)\s+(?:them|it)\b" % REF, ""),
        (r"\s*\(per %s\)" % REF, ""),
        (r"^according to %s,\s*" % REF, ""),
        (r",?\s*according to %s\b(?!'s)" % REF, ""),
        (r"^per %s,\s*" % REF, ""),
    ):
        new = re.sub(pat, rep, stem, flags=re.I)
        if new != stem:
            return new[0].upper() + new[1:] if new else new, None
    return stem, "no rule matched"
