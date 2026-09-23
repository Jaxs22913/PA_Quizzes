#!/usr/bin/env python3
"""Find answer keys that were cut short -- in pools, sets, and shipped masters.

The defect: a key that is a genuine enumeration, or a sentence whose second half
is the actual answer, gets cut down (usually by a length-bias trim) and the rest
is dropped or pushed into the explanation. The content survives somewhere; the
ANSWER does not, and the student is marked right for half of it.

Three independent checks, because each layer can carry the damage on its own:

1  POOL SIGNATURES -- every pool and vignette bank read on its own terms:
     A  number word, fewer items   "Three: the left posterior, the septal"
     B  stem asks a list, key names one thing
     C  orphan tail -- the STEM asks for a list, the key names ONE thing, and
        the explanation's last sentence is a short comma-list of more things of
        the same kind. (A first attempt that tested only "tail has no finite
        verb" flagged 246 good explanations; requiring the list-asking stem AND
        a one-item key cut that to 5, all real.)
     D  key ends mid-list, on a comma or a trailing lower-case conjunction
   These are heuristics. Each flag that was read and judged sound is listed in
   REVIEWED with the reason, and is reported as excluded, never silently.

1b MASTER SIGNATURES -- the pool signatures of (1), run on every master
   question as well; REVIEWED_MASTERS holds the ones judged sound.

2  MASTER vs TWIN -- every master form (page, and the master-exams*.json it is
   rendered from). The twin is a topic PAGE in the same folder (by stem, else by
   the set of wrong options), and failing that a POOL or sets.json question (by
   stem, else wrong options). A master key that is a strict PREFIX of the twin's
   key, or (stem twins only) names fewer items of a list the twin enumerates, is
   a truncation. Written after six Physical Diagnosis 2 Exam 1 master keys
   shipped truncated (form-a #46, b #16, d #8, d #29, e #0, e #59) while
   check_answer_key_consistency passed: `c` pointed at the right, shortened,
   option. A page twin is flagged on any truncation. A source twin is flagged
   only when the stem asks for several things, and a list-collapse only when
   items were dropped rather than reworded -- a pool key predates the length
   pass, whose rule is to SHORTEN THE KEY, so most shorter master keys are that
   rule working (the reasoning and the measurement are in masters()).
   Until 2026-09-22 this looked at page twins only: 2,633 of 6,300 master
   questions had no page twin and were never compared, and PD2 Exam 1 form-b
   #40 (stage I pressure ulcer: key "Changes in temperature", pool key
   "Temperature, consistency, sensation and colour") went unseen.

3  SOURCE vs SHIPPED PAGE -- every pool and sets.json question against the
   shipped topic page with the same stem and at least two of the same wrong
   options (the same question, not a namesake in another class). A source
   key that is a truncation of the page's key means the page is currently better than its source, and the
   next render will cut it: tools/pd2_l1_pool_a.py and pd2_l1_sets.json hold
   five truncated Lecture 1 keys (the audit of 2026-09-22 found three; this
   check found two more) that only clinical-reasoning-documentation-quiz.html
   still has in full. (The other direction -- page shorter than
   source -- is how a deliberate "shorten the key" edit looks, and is not
   flagged.)

    python3 tools/check_truncated_keys.py            # Semester 2 and later
    python3 tools/check_truncated_keys.py --json out.json

Paths resolve from the repo root, whatever the cwd. Exit 1 on any flag and on
any module that fails to import -- a bank that cannot be read was not checked.
"""
import glob, importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from check_exam_standard import is_frozen
from check_pool_cites import SKIP as TOOLING           # same glob skip rule as the citation check
from check_self_contained import page_banks

NUM = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8}
LIST_Q = re.compile(r"\bwhich (are|factors|injuries|causes|types|kinds|categories|forms|"
                    r"things|features|findings|structures|modalities|changes|indications|"
                    r"agents|drugs|signs|symptoms|steps|three|four|five)\b|"
                    r"\bwhat are the\b|\bin what order\b|\blist the\b|\bname the\b", re.I)

# Signature flags read by a person and judged to be complete answers. Keyed by
# (module, key text). Keep the reason: an exclusion nobody can audit is a hole.
REVIEWED = {
    ("clinpath_ent_pool", "The otolith organs"):
        "B: 'structures' is answered by a plural noun; nothing is missing",
    ("cmsderm_l2_pool", "Wickham striae"):
        "B: the stem's list is the vignette's findings; the key is the one named sign asked for",
    ("cmsophtho_l10d_pool", "The choroid and/or the retina"):
        "B: both structures are in the key ('and/or' defeats the list test)",
    ("medlit_s2evid_pool", "Findings may be presented in language clinicians struggle with"):
        "D: a complete sentence that ends on a preposition, not a cut list",
    ("micro_l3_pool_a", "Our own immune responses"):
        "B: the host response IS the factor asked for; explanation has no dangling tail",
    ("pd2_l3_pool_c", "An enlarged cup with vessels sinking in"):
        "B: a complete description of the finding",
    ("pharm_l2_derm_pool_b", "Topical corticosteroids"):
        "B: a drug class, plural; the complete answer",
    ("cms_e3l15_vig_a", "The mastoid air cells"):
        "B: 'which structures' answered by one plural structure (mastoiditis)",
}


# The same, for master questions (signatures and source-twin truncations),
# keyed by (folder, key text) so one entry covers a form page and the
# master-exams.json it is rendered from.
REVIEWED_MASTERS = {
    # signature B on the same keys already judged in the pools (REVIEWED above)
    ("Clinical Medicine and Surgery I Exam 1", "Wickham striae"):
        "B: the stem's list is the vignette's findings; the key is the one named sign asked for",
    ("Clinical Medicine and Surgery I Exam 2", "The choroid and/or the retina"):
        "B: both structures are in the key ('and/or' defeats the list test)",
    ("Clinical Pathophysiology I Exam 1", "The otolith organs"):
        "B: 'structures' is answered by a plural noun; nothing is missing",
    ("Pharmacology I Exam 1", "Topical corticosteroids"):
        "B: a drug class, plural; the complete answer",
    # NOT the shipped key: PD2 Exam 1 form-c #46 ships "The physiologic cup is
    # enlarged" and is FLAGGED (the vessels went into the explanation). This is
    # the pool's complete key, judged sound there, so restoring it passes.
    ("Physical Diagnosis 2 Exam 1", "An enlarged cup with vessels sinking in"):
        "B: a complete description of the finding",
    # source-twin truncations read and judged complete
    ("Clinical Medicine and Surgery I Exam 1", "Pre-eruptive, acute eruptive, postherpetic neuralgia"):
        "list-collapse artefact: all three phases are named; the pool's 'dysesthesia or pain' "
        "describes a phase, it is not a fourth item",
    ("Clinical Medicine and Surgery I Exam 2", "A sharp object or high-velocity projectile"):
        "prefix: the dropped tail is examples ('such as a fishing hook or knife'), not a mechanism",
}


def items(s):
    body = re.sub(r'^\s*\w+[:,]\s*', '', s)
    return len([p for p in re.split(r',| and ', body) if p.strip()])


def _n(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s.rstrip(" .;:,")


def _items(s):
    return len([p for p in re.split(r",|;| and | or ", _n(s)) if p.strip()])


def truncation(short, full, by_stem=True):
    """How `short` is a cut-down `full`, or None.

    prefix         `full` starts with `short` and continues past a separator
    list-collapse  `full` enumerates (2+ items) and `short` names fewer, and is
                   shorter -- only for twins matched by STEM, since two different
                   questions can share a set of wrong options."""
    a, b = _n(short), _n(full)
    if not a or a == b or len(a) >= len(b):
        return None
    if b.startswith(a) and b[len(a)] in ",;:( -\u2014":
        return "prefix"
    if by_stem and _items(full) >= 2 and _items(short) < _items(full):
        return "list-collapse"
    return None


# "Asks for several": LIST_Q, or a plural head noun right after "which" (an
# explicit list -- a regex for "any plural" matched verbs like "does" and
# "produces"). Used only to decide which SOURCE-twin truncations are defects:
# see masters().
SEVERAL = re.compile(
    r"\bwhich (?:[a-z\-]+ )?(?:patients|bones|options|conditions|findings|organisms|infections"
    r"|muscles|nerves|tests|drugs|agents|causes|signs|symptoms|features|structures|treatments"
    r"|groups|populations|sites|regions|components|elements|criteria|complications|presentations"
    r"|mechanisms|studies|investigations|measures|steps|questions|layers|types|classes|diseases"
    r"|disorders|lesions|medications|pathogens|bacteria|viruses|species|vessels|glands|cells"
    r"|tissues|organs|changes|factors|injuries|modalities|indications|phases|stages)\b", re.I)
LIMITER = re.compile(r"\b(?:alone|only|just)\b", re.I)


def _toks(s):
    return {w[:5] for w in re.findall(r"[a-z0-9]+", _n(s)) if len(w) >= 4}


def _item_list(s):
    return [p.strip() for p in re.split(r",|;| and | or |\u2014| - ", _n(s)) if p.strip()]


def items_dropped(short, full):
    """For a list-collapse: True when every item of `short` matches an item of
    `full` (shared content word) -- items were DROPPED, not reworded."""
    fi = _item_list(full)
    return all(any(_toks(a) & _toks(b) for b in fi) for a in _item_list(short))


def key_of(q):
    c = q.get("c", 0)
    try:
        return q["opts"][c][0]
    except (IndexError, KeyError, TypeError):
        return None


# ---------------------------------------------------------------- 1  pools
def load_pools():
    """-> (banks, failures, n_candidates, n_tooling). banks: [(module, file, [q...])]"""
    cands = sorted(set(glob.glob(os.path.join(HERE, "*pool*.py")))
                   | set(glob.glob(os.path.join(HERE, "*_vig*.py"))))
    banks, failures, tooling = [], [], 0
    for f in cands:
        if TOOLING.search(os.path.basename(f)):
            tooling += 1
            continue
        mod = os.path.basename(f)[:-3]
        try:
            spec = importlib.util.spec_from_file_location(mod, f)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
        except BaseException as e:
            failures.append({"module": mod, "error": "%s: %s" % (type(e).__name__, str(e)[:120])})
            continue
        qs, seen = [], set()
        for attr in sorted(dir(m)):
            P = getattr(m, attr)
            if not (isinstance(P, list) and P and isinstance(P[0], dict) and 'opts' in P[0]):
                continue
            for i, q in enumerate(P):
                if id(q) not in seen and isinstance(q, dict) and 'opts' in q:
                    seen.add(id(q))
                    qs.append(("%s[%d]" % (attr, i), q))
        if qs:
            banks.append((mod, os.path.relpath(f, ROOT), qs))
    return banks, failures, len(cands), tooling


def signatures(banks, reviewed=None):
    """Signature flags for [(name, file, [(loc, q)])]. `reviewed` maps
    (name, key text) -> reason; a pool's name is its module, a master's is its
    folder (so one entry covers the page and the master-exams.json it renders)."""
    reviewed = REVIEWED if reviewed is None else reviewed
    flags, excluded, n = [], [], 0
    for mod, rel, qs in banks:
        for loc, q in qs:
            key = key_of(q)
            if key is None:
                continue
            n += 1
            c = q.get("c", 0)
            expl = q['opts'][c][1] if len(q['opts'][c]) > 1 else ""
            sig = []
            m = re.match(r'^(two|three|four|five|six|seven|eight)\b[:,]', key, re.I)
            if m and items(key) < NUM[m.group(1).lower()]:
                sig.append('A')
            if LIST_Q.search(q['q']) and not re.search(r',| and | or ', key, re.I) and len(key) < 40:
                sig.append('B')
            sents = [x.strip() for x in re.split(r'(?<=[.!?])\s+', expl.strip()) if x.strip()]
            if LIST_Q.search(q['q']) and not re.search(r',| and | or ', key, re.I) and len(sents) > 1:
                tail = sents[-1].rstrip('.')
                if (',' in tail or ' and ' in tail.lower()) and len(tail.split()) <= 11 \
                   and not re.match(r'^(it|they|this|that|these|those)\b', tail, re.I):
                    sig.append('C')
            # lower-case only: "Essential Evidence Plus" is a product name
            if re.search(r'[,;]\s*$|\b(and|or|with|plus)\s*$', key):
                sig.append('D')
            if sig:
                rec = {"check": "signature", "file": rel, "index": loc, "signature": "".join(sig),
                       "stem": q['q'], "key": key, "tail": sents[-1] if sents else ""}
                reason = reviewed.get((mod, key))
                if reason:
                    rec["reviewed"] = reason
                    excluded.append(rec)
                else:
                    flags.append(rec)
    return flags, excluded, n


# ---------------------------------------------------------------- pages
def live_folders():
    out = []
    for d in sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, d)
        if os.path.isdir(p) and not d.startswith(".") and not is_frozen(d) and \
           d not in ("tools", "group-quizzes", "icons", "audio", "rpg", "node_modules"):
            out.append(d)
    return out


def page_questions(path):
    banks, problems = page_banks(path)
    for name, entries in banks:
        if name == "QUESTIONS":
            return [q for _loc, q in entries if isinstance(q, dict) and "opts" in q and "q" in q], problems
    return None, problems


def wrong_set(q):
    c = q.get("c", 0)
    return frozenset(_n(o[0]) for j, o in enumerate(q["opts"]) if j != c)


# ---------------------------------------------------------------- sources
def load_sets():
    """-> (records [(file, loc, q)], n_files, unreadable). The derived
    tools/*_sets.json and cms_l*_set*.json that topic pages render from."""
    sets = sorted(set(glob.glob(os.path.join(HERE, "*_sets.json")))
                  | set(glob.glob(os.path.join(HERE, "cms_l*_set*.json"))))
    recs, unreadable, nfiles = [], [], 0
    for f in sets:
        rel = os.path.relpath(f, ROOT)
        try:
            data = json.load(open(f, encoding="utf-8"))
        except ValueError as e:
            unreadable.append({"file": rel, "problem": str(e)[:80]})
            continue
        nfiles += 1
        for key, qs in (data.items() if isinstance(data, dict) else []):
            if not isinstance(qs, list):
                continue
            for i, q in enumerate(qs):
                if isinstance(q, dict) and "opts" in q and "q" in q:
                    recs.append((rel, "%s[%d]" % (key, i), q))
    return recs, nfiles, unreadable


def source_index(banks, set_recs):
    """Every pool and sets.json question, by normalised stem and by wrong-option set."""
    by_stem, by_opts = {}, {}
    recs = [(rel, loc, q) for _m, rel, qs in banks for loc, q in qs] + list(set_recs)
    for rel, loc, q in recs:
        if key_of(q) is None:
            continue
        by_stem.setdefault(_n(q["q"]), []).append((rel, loc, q))
        by_opts.setdefault(wrong_set(q), []).append((rel, loc, q))
    return by_stem, by_opts


# ---------------------------------------------------------------- 2  masters
def masters(folders, src_by_stem, src_by_opts):
    """Every master form against its twin. Returns (flags, by_design, stats,
    topic_index, master_banks); master_banks feed the signature pass.

    Twin order: a topic PAGE in the same folder by stem, then by wrong options;
    failing both, a POOL or sets.json question by stem, then by wrong options.
    The two kinds are judged differently, measured 2026-09-22:
      page twin    the page and the master are both shipped, so any truncation
                   is flagged (it caught the six PD2 Exam 1 keys and nothing else).
      source twin  a pool key is written BEFORE the length-bias pass, whose
                   standing rule is "shorten the key, never pad the distractors"
                   (Jaxon, 2026-08-30) -- so a master key shorter than its pool
                   key is usually that rule working. Of 96 raw source-twin
                   truncations, 88 dropped rationale from a one-answer stem
                   ("It is a life-threatening malignancy[, not only a threat to
                   sight]"). A source-twin truncation is flagged only when the
                   stem asks for SEVERAL things (LIST_Q or SEVERAL) or a
                   distractor is the key plus "alone/only"; and a list-collapse
                   only when the items were dropped rather than reworded. The
                   rest are counted, and written to --json as by_design, never
                   silently passed."""
    flags, by_design = [], []
    stats = {"forms": 0, "questions": 0, "by_stem": 0, "by_options": 0, "src_by_stem": 0,
             "src_by_options": 0, "unpaired": 0, "unreadable": []}
    topic_index, master_banks = {}, []
    for d in folders:
        pages = sorted(glob.glob(os.path.join(ROOT, d, "*.html")))
        by_stem, by_opts = {}, {}
        forms = []
        for p in pages:
            rel = os.path.relpath(p, ROOT)
            qs, problems = page_questions(p)
            for pr in problems:
                stats["unreadable"].append({"file": rel, "problem": pr})
            if not qs:
                continue
            if "master-exam" in os.path.basename(p):
                forms.append((rel, "#%d", qs))
                continue
            for i, q in enumerate(qs):
                by_stem.setdefault(_n(q["q"]), []).append((rel, "#%d" % i, q))
                by_opts.setdefault(wrong_set(q), []).append((rel, "#%d" % i, q))
        topic_index[d] = by_stem
        for jf in sorted(glob.glob(os.path.join(ROOT, d, "master-exams*.json"))):
            rel = os.path.relpath(jf, ROOT)
            try:
                data = json.load(open(jf, encoding="utf-8"))
            except ValueError as e:
                stats["unreadable"].append({"file": rel, "problem": str(e)[:80]})
                continue
            for form, qs in sorted(data.items()):
                if isinstance(qs, list):
                    forms.append((rel, form + "[%d]", [q for q in qs if isinstance(q, dict) and "opts" in q]))
        for rel, locfmt, qs in forms:
            stats["forms"] += 1
            master_banks.append((d, rel, [(locfmt % i, q) for i, q in enumerate(qs)]))
            for i, q in enumerate(qs):
                stats["questions"] += 1
                mk = key_of(q)
                stem = _n(q["q"])
                kind, twins, stem_pair = "page", by_stem.get(stem), True
                if twins:
                    stats["by_stem"] += 1
                elif by_opts.get(wrong_set(q)):
                    twins, stem_pair = by_opts[wrong_set(q)], False
                    stats["by_options"] += 1
                elif src_by_stem.get(stem):
                    kind, twins = "source", src_by_stem[stem]
                    stats["src_by_stem"] += 1
                elif src_by_opts.get(wrong_set(q)):
                    kind, twins, stem_pair = "source", src_by_opts[wrong_set(q)], False
                    stats["src_by_options"] += 1
                else:
                    stats["unpaired"] += 1
                    continue
                for trel, tloc, tq in twins:
                    tk = key_of(tq)
                    how = truncation(mk, tk, by_stem=stem_pair)
                    if not how:
                        continue
                    rec = {"check": "master-vs-twin", "file": rel, "index": locfmt % i, "how": how,
                           "stem": q["q"], "key": mk, "twin": "%s %s" % (trel, tloc), "twin_key": tk,
                           "twin_kind": kind, "paired_by": "stem" if stem_pair else "wrong options"}
                    if kind == "source":
                        c = q.get("c", 0)
                        limiter = any(LIMITER.search(o[0]) and _toks(mk) <= _toks(o[0])
                                      for j, o in enumerate(q["opts"]) if j != c)
                        several = bool(LIST_Q.search(q["q"]) or SEVERAL.search(q["q"]))
                        why = None
                        if how == "list-collapse" and not items_dropped(mk, tk):
                            why = "list reworded, no item dropped"
                        elif not (several or limiter):
                            why = "one-answer stem: key shortened by design"
                        else:
                            reason = REVIEWED_MASTERS.get((d, mk))
                            if reason:
                                why = "REVIEWED: " + reason
                        if why:
                            rec["not_flagged_because"] = why
                            by_design.append(rec)
                            break
                        rec["asks_several"], rec["limiter_distractor"] = several, limiter
                    flags.append(rec)
                    break
    return flags, by_design, stats, topic_index, master_banks


# ---------------------------------------------------------------- 3  sources
def sources_vs_pages(banks, set_recs, topic_index):
    pages = {}
    for d, idx in topic_index.items():
        for stem, lst in idx.items():
            pages.setdefault(stem, []).extend(lst)
    flags = []
    stats = {"pool_questions": 0, "pool_paired": 0, "sets_questions": 0, "sets_paired": 0}

    def compare(kind, rel, loc, q):
        # Same stem is not enough across the whole site: "What is pre-test
        # probability?" is asked by Med Lit and PDM with different options. A
        # twin must also share at least two wrong options -- the same question.
        # (Measured 2026-09-22: every real pair shared 2-3, every stray 0.)
        ws = wrong_set(q)
        twins = [t for t in pages.get(_n(q["q"]), []) if len(ws & wrong_set(t[2])) >= 2]
        if not twins:
            return False
        for trel, tloc, tq in twins:
            how = truncation(key_of(q), key_of(tq), by_stem=True)
            if how:
                flags.append({"check": "source-vs-page", "file": rel, "index": loc, "how": how,
                              "source_kind": kind, "stem": q["q"], "key": key_of(q),
                              "page": "%s %s" % (trel, tloc), "page_key": key_of(tq)})
                break
        return True

    for mod, rel, qs in banks:
        for loc, q in qs:
            if key_of(q) is None:
                continue
            stats["pool_questions"] += 1
            stats["pool_paired"] += compare("pool", rel, loc, q)
    for rel, loc, q in set_recs:
        stats["sets_questions"] += 1
        stats["sets_paired"] += compare("sets", rel, loc, q)
    return flags, stats


def main(argv):
    json_out = argv[argv.index("--json") + 1] if "--json" in argv else None
    banks, failures, ncand, ntool = load_pools()
    set_recs, nsets, sets_unreadable = load_sets()
    sig, excluded, nsig = signatures(banks)
    folders = live_folders()
    src_by_stem, src_by_opts = source_index(banks, set_recs)
    mflags, by_design, mstats, topic_index, master_banks = masters(folders, src_by_stem, src_by_opts)
    msig, mexcluded, nmsig = signatures(master_banks, REVIEWED_MASTERS)
    sflags, sstats = sources_vs_pages(banks, set_recs, topic_index)

    def show_sig(title, recs):
        if recs:
            print(title)
        for r in recs:
            print(f"[{r['signature']:<4}] {r['file']}  {r['index']}")
            print(f"        Q {r['stem'][:92]}")
            print(f"        A {r['key'][:92]}")
            if 'C' in r['signature']:
                print(f"        tail: {r['tail'][:88]}")

    show_sig("\n1  POOL SIGNATURES", sig)
    show_sig("\n1b MASTER-FORM SIGNATURES (the same heuristics, on every master question)", msig)
    if mflags:
        print("\n2  MASTER KEY IS A CUT-DOWN TWIN KEY")
    for r in mflags:
        print(f"[{r['how']}] {r['file']} {r['index']}   ({r['twin_kind']} twin by {r['paired_by']}: {r['twin']})")
        print(f"        Q {r['stem'][:92]}")
        print(f"        master {r['key'][:88]}")
        print(f"        twin   {r['twin_key'][:88]}")
    if sflags:
        print("\n3  SOURCE KEY IS A CUT-DOWN SHIPPED KEY (a re-render would cut the page)")
    for r in sflags:
        print(f"[{r['how']}] {r['file']} {r['index']}   (page: {r['page']})")
        print(f"        Q {r['stem'][:92]}")
        print(f"        source {r['key'][:88]}")
        print(f"        page   {r['page_key'][:88]}")
    for fl in failures:
        print("IMPORT FAILED -- NOT CHECKED: %s  %s" % (fl["module"], fl["error"]))
    unreadable = mstats["unreadable"] + sets_unreadable
    for u in unreadable:
        print("UNREADABLE -- NOT CHECKED: %s  %s" % (u["file"], u["problem"]))

    print("\npools: %d candidate module(s), %d skipped as tooling, %d with questions, %d import failure(s); "
          "sets: %d file(s), %d question(s)"
          % (ncand, ntool, len(banks), len(failures), nsets, len(set_recs)))
    print("1  signatures: %d pool key(s) screened; %d flagged; %d reviewed and excluded (REVIEWED)"
          % (nsig, len(sig), len(excluded)))
    print("1b signatures: %d master key(s) screened; %d flagged; %d reviewed and excluded (REVIEWED_MASTERS)"
          % (nmsig, len(msig), len(mexcluded)))
    print("2  masters: %d form(s) in %d live folder(s) (pages and master-exams*.json), %d question(s); "
          "page twin by stem %d, by wrong options %d; pool/sets twin by stem %d, by wrong options %d; "
          "no twin %d; %d flagged, %d source-twin truncation(s) not flagged (see by_design in --json)"
          % (mstats["forms"], len(folders), mstats["questions"], mstats["by_stem"], mstats["by_options"],
             mstats["src_by_stem"], mstats["src_by_options"], mstats["unpaired"], len(mflags), len(by_design)))
    print("3  sources: %d pool question(s) (%d with a shipped twin), %d sets question(s) "
          "(%d with a shipped twin); %d flagged"
          % (sstats["pool_questions"], sstats["pool_paired"], sstats["sets_questions"],
             sstats["sets_paired"], len(sflags)))
    total = len(sig) + len(msig) + len(mflags) + len(sflags)
    print("%d flagged in total" % total)
    if json_out:
        with open(json_out, "w", encoding="utf-8") as fh:
            json.dump({"signatures": sig, "reviewed_excluded": excluded,
                       "master_signatures": msig, "master_reviewed_excluded": mexcluded,
                       "masters": mflags, "by_design": by_design,
                       "sources": sflags, "import_failures": failures, "unreadable": unreadable,
                       "stats": {"masters": mstats, "sources": sstats}}, fh, ensure_ascii=False, indent=1)
        print("wrote %s" % json_out)
    bad = total or failures or unreadable
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
