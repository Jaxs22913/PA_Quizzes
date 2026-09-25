#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Find (and with --fix, repair) British spellings in Semester 2+ content.

Jaxon, 2026-09-23: "fix spelling to be US spelling. You have words like
Haemoconcentraion which should be hemoconcentration." He is a US PA student;
his decks and syllabi are American, and the British forms crept in from our
own writing. Semester 1 is FROZEN with its British spellings
([[semester_1_frozen]]), so scope is Semester 2 onward, read from semesters.js.

WHAT IS KEPT AS WRITTEN
  * taxonomic names -- Haemophilus, Enterococcus faecalis, Arcanobacterium
    haemolyticum, Schistosoma haematobium ... (EXCEPT_WORDS)
  * proper nouns -- "Grey Turner" sign
  * URLs, file and image paths, HTML attribute values other than visible text
    (alt/title/aria-label/placeholder/meta content), CSS, JS/Python code,
    identifiers of any kind (a word glued to _ $ or digits, or a hyphen/dot/#
    inside a space-free code string such as "l5-tumour" or ".grey")
  * the guide io-box: the syllabus's Instructional Objectives, verbatim
  * JSON object keys

LAYERS. A fix in the rendered page alone is reverted by the next render, so
the scope covers every layer the pages are generated from: the Semester 2+
class folders (pages, sets/master JSON), the tools that write them (pools,
*_sets.json, lengthfix, guide/cram/Arcade builders and their data modules),
the shared quiz/cram templates, the Semester 2+ decks inside arcade.js, the
Semester 2+ cards in guides.html and the Fall block of index.html.
group-quizzes/ and cram-personal/ are GENERATED -- rebuild them
(build_group_quizzes.py, build_cram_personal.py) rather than editing.

    python3 tools/check_us_spelling.py            # report; exit 1 if any
    python3 tools/check_us_spelling.py --fix      # rewrite in place
    python3 tools/check_us_spelling.py --list     # files in scope
    python3 tools/check_us_spelling.py --words    # per-word counts
    python3 tools/check_us_spelling.py PATH ...   # only these files
"""
import ast, io, json, os, re, sys, tokenize
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# ------------------------------------------------------------------ the map

EXCEPT_WORDS = {
    # taxonomic names (genus or species epithet) -- the Latin is the name
    "haemophilus", "haemolyticus", "haemolytica", "haemolyticum", "haematobium",
    "haemonchus", "haemaphysalis", "haemofelis", "haemulonii", "haemoproteus",
    "haemagogus", "haemadipsa", "haemosporida", "faecalis", "faecium", "gonorrhoeae",
    "leuconostoc", "leucovorin", "oesophagostomum", "aegyptius", "caesalpinia",
    # brand / proper names that happen to look British
    "haemoccult",
}

EXPLICIT = {
    "grey": "gray", "greys": "grays", "greyish": "grayish", "greying": "graying",
    "greyscale": "grayscale", "greyed": "grayed",
    "programme": "program", "programmes": "programs",
    "catalogue": "catalog", "catalogues": "catalogs", "catalogued": "cataloged",
    "analogue": "analog", "analogues": "analogs",
    "defence": "defense", "defences": "defenses", "offence": "offense",
    "offences": "offenses", "licence": "license", "licences": "licenses",
    "pretence": "pretense",
    "practise": "practice", "practised": "practiced", "practises": "practices",
    "practising": "practicing",
    "ageing": "aging", "mould": "mold", "moulds": "molds", "mouldy": "moldy",
    "aluminium": "aluminum", "judgement": "judgment", "judgements": "judgments",
    "acknowledgement": "acknowledgment", "artefact": "artifact",
    "artefacts": "artifacts", "artefactual": "artifactual",
    "coeliac": "celiac", "manoeuvre": "maneuver", "manoeuvres": "maneuvers",
    "manoeuvring": "maneuvering",
    "neurone": "neuron", "neurones": "neurons",
    "focussed": "focused", "focussing": "focusing", "focusses": "focuses",
    "benefitted": "benefited", "benefitting": "benefiting",
    "counselling": "counseling", "counselled": "counseled",
    "counsellor": "counselor", "counsellors": "counselors",
    "travelled": "traveled", "travelling": "traveling", "traveller": "traveler",
    "travellers": "travelers", "modelling": "modeling", "modelled": "modeled",
    "labelled": "labeled", "labelling": "labeling", "signalling": "signaling",
    "signalled": "signaled", "cancelled": "canceled", "cancelling": "canceling",
    "fuelled": "fueled", "fuelling": "fueling", "levelled": "leveled",
    "levelling": "leveling", "channelled": "channeled", "tunnelled": "tunneled",
    "tunnelling": "tunneling", "dialled": "dialed", "totalled": "totaled",
    "totalling": "totaling", "equalled": "equaled", "marvellous": "marvelous",
    "jewellery": "jewelry", "woollen": "woolen", "fulfil": "fulfill",
    "fulfils": "fulfills", "fulfilment": "fulfillment", "enrol": "enroll",
    "enrols": "enrolls", "enrolment": "enrollment", "skilful": "skillful",
    "wilful": "willful", "instil": "instill", "instils": "instills",
    "instilment": "instillment", "distil": "distill", "appal": "appall",
    "appalling": "appalling", "tranquilliser": "tranquilizer",
    "tranquillisers": "tranquilizers",
    "leucocyte": "leukocyte", "leucocytes": "leukocytes",
    "leucocytosis": "leukocytosis", "leucopenia": "leukopenia",
    "leucoplakia": "leukoplakia", "leucocyturia": "leukocyturia",
    "leucoderma": "leukoderma", "leucocoria": "leukocoria",
    "leucorrhoea": "leukorrhea",
    "gonadotrophin": "gonadotropin", "gonadotrophins": "gonadotropins",
    "thyrotrophin": "thyrotropin", "corticotrophin": "corticotropin",
    "somatotrophin": "somatotropin", "adrenocorticotrophic": "adrenocorticotropic",
    "corticotrophic": "corticotropic", "gonadotrophic": "gonadotropic",
    "thyrotrophic": "thyrotropic",
    "fibreoptic": "fiberoptic", "fibreglass": "fiberglass",
    "draught": "draft", "cosy": "cozy", "storey": "story", "tyre": "tire",
    "tyres": "tires", "cheque": "check", "sceptical": "skeptical",
    "sceptic": "skeptic", "plough": "plow", "moustache": "mustache",
    "pyjamas": "pajamas", "mediaeval": "medieval",
}

OUR_STEMS = ("tum col behavi hum lab fav od vap rum hon neighb harb rig vig "
             "flav val arm endeav sav clam ferv parl splend cand demean").split()
OUR_RE = re.compile(r"^((?:dis|un|multi|bi|tri|non|mis|pre|off)?(?:%s))our"
                    r"(s|ed|ing|ful|less|ite|ites|able|ably|er|ers|al|ally|ist|ists|"
                    r"ation|ations|ise|ize|ised|ized|igenic|igenesis|ous)?$"
                    % "|".join(OUR_STEMS))

RE_STEMS = "centr fibr litr metr calibr lustr sombr spectr theatr sabr meagr goitr mitr".split()
RE_RE = re.compile(r"^([a-z]*?)(%s)e(s|d)?$" % "|".join(RE_STEMS))

ISE_STEMS = set("""
organ recogn character real util standard priorit summar emphas special general
normal stabil neutral visual local central optim maxim minim categor apolog author
capital critic crystal crystall sensit energ familiar fertil final harmon human ideal
individual industrial initial internal external ion jeopard legal liberal metabol memor
mobil modern monet natural oxid patron penal personal polar popular pressur rational
revolution scrutin sympath synchron synthes system systemat theor traumat vapor vocal
weapon homogen catheter anaesthet anesthet epithelial keratin vascular lateral alkalin
hypnot pasteur carbon magnet vandal marginal hospital immun steril emphas colon agon
antagon opson random custom item stigmat dramat anonym dichotom cauter nebul atom
aerosol solubil digit lyophil heparin exterior interior vital moral legitim politic
romantic public radical medical mineral hybrid global equal material mechan motor
social sanit subsid moistur monopol trivial verbal victim urban national conceptual
contextual operational institutional compartmental symbol styl tender polymer isomer
canal cicatr trypsin edemat commercial civil fossil hypothes quant tranquil tranquill fraternal
""".split())

YSE_RE = re.compile(r"^([a-z]*?(?:analy|paraly|dialy|cataly|electroly|hydroly|haemoly|hemoly|"
                    r"autoly|photoly|plasmoly))s(e|ed|ing|er|ers)$")

# substring rules, applied in order, to words NOT in EXCEPT_WORDS
SUBS = [
    (re.compile(r"haem"), "hem"),
    (re.compile(r"(?<=[a-z])aemi"), "emi"),          # anaemia, ischaemic, hypoxaemia
    (re.compile(r"^aemi"), "emi"),
    (re.compile(r"(an|par|hyper|hypo|dys|syn|kin|hemian)aesth"), r"\1esth"),
    (re.compile(r"^oedem|(?<=[xhl])oedem"), "edem"),   # myxoedema, lymphoedema; NOT angioedema
    (re.compile(r"ooesophag"), "oesophag"),            # gastro-oesophageal run together
    (re.compile(r"^oesophag|(?<=trans)oesophag"), "esophag"),
    (re.compile(r"oestr"), "estr"),
    (re.compile(r"paed"), "ped"),
    (re.compile(r"rrhoe"), "rrhe"),                   # diarrhoea, gonorrhoea, otorrhoea
    (re.compile(r"pnoe"), "pne"),                     # dyspnoea, apnoea, orthopnoea
    (re.compile(r"aetiol"), "etiol"),
    (re.compile(r"^faec"), "fec"),
    (re.compile(r"gynaec"), "gynec"),
    (re.compile(r"^foet"), "fet"),
    (re.compile(r"^caec"), "cec"),
    (re.compile(r"caesar"), "cesar"),
    (re.compile(r"sulph"), "sulf"),
    (re.compile(r"^leuco(?!n|v)"), "leuko"),
]


def us_lower(w):
    """US form of a lowercase word, or None if it is not a British spelling."""
    if w in EXCEPT_WORDS:
        return None
    if w in EXPLICIT:
        return EXPLICIT[w]
    out = w
    for rx, rep in SUBS:
        out = rx.sub(rep, out)
    m = OUR_RE.match(out)
    if m:
        out = m.group(1) + "or" + (m.group(2) or "")
    m = RE_RE.match(out)
    if m and not out.endswith(("acre", "ogre")):
        tail = {"": "er", "s": "ers", "d": "ered"}[m.group(3) or ""]
        # centr+e -> center: the stem minus its trailing 'r', then 'er'
        out = m.group(1) + m.group(2)[:-1] + tail
    m2 = re.match(r"^([a-z]+?)(is)(e|ed|es|ing|ation|ations|er|ers|able)$", out)
    if m2:
        # bare stems first (recognise), then prefixed forms (desensitise,
        # hyperpolarisation, revascularise)
        for pre in ("", "de", "re", "im", "un", "hyper", "hypo", "non", "over", "under",
                    "mis", "pre", "co", "dis", "in", "ir", "sub", "auto", "neo"):
            if m2.group(1).startswith(pre) and m2.group(1)[len(pre):] in ISE_STEMS:
                out = m2.group(1) + "iz" + m2.group(3)
                break
    m = YSE_RE.match(out)
    if m:
        out = m.group(1) + "z" + m.group(2)
    return out if out != w else None


def us_word(word):
    lo = word.lower()
    rep = us_lower(lo)
    if rep is None:
        return None
    if word.isupper() and len(word) > 1:
        return rep.upper()
    if word[0].isupper():
        return rep[0].upper() + rep[1:]
    return rep


# ------------------------------------------------------------------ text engine

TOK = re.compile(r"\\u[0-9a-fA-F]{4}|\\[nrtbf\"'\\/]|[A-Za-z]+|[^A-Za-z\\]+|\\")
PATHY = re.compile(r"://|www\.|\.(?:png|jpe?g|gif|svg|webp|html?|js|json|py|css|m4a|mp3|"
                   r"mp4|pdf|docx?|pptx?|txt|md|aac|wav)\b", re.I)
GLUE = set("0123456789_$")


def fix_text(s, code_string=False, hits=None, where=""):
    """Rewrite British words in a run of visible text.

    code_string: the text is the inside of a JS/Python/JSON string literal that
    may be an identifier or a selector; when it has no whitespace, a word
    touching - . # / : is treated as code and left alone."""
    if not s or not re.search(r"[A-Za-z]", s):
        return s
    if code_string and re.search(r"\(\?[:!=<]|\\[bwdsB]|\[\^", s):
        return s                                  # a regular expression, not prose
    nows = code_string and not re.search(r"\s", s)
    # hyphenated British compounds that close up in US spelling
    def joined(m):
        if hits is not None:
            hits.append((where, m.group(0), m.group(1) + "e" + m.group(2), m.group(0)))
        return m.group(1) + "e" + m.group(2)
    s = re.sub(r"\b([Aa]ngio|[Gg]astro|[Tt]racheo)-oe(dem|sophag)", joined, s)
    toks = [m.group(0) for m in TOK.finditer(s)]
    out = []
    pos = 0
    for i, t in enumerate(toks):
        start = pos
        pos += len(t)
        if not t[0].isalpha():
            out.append(t); continue
        rep = us_word(t)
        if rep is None:
            out.append(t); continue
        prev = s[start - 1] if start else ""
        nxt = s[pos] if pos < len(s) else ""
        if prev in GLUE or nxt in GLUE:
            out.append(t); continue
        if nows and (prev in "-.#/:=" or nxt in "-.#/:=" or prev == "-" or nxt == "-"):
            out.append(t); continue
        # the whitespace-free chunk this word sits in
        a = start
        while a > 0 and not s[a - 1].isspace():
            a -= 1
        b = pos
        while b < len(s) and not s[b].isspace():
            b += 1
        chunk = s[a:b]
        if PATHY.search(chunk) or chunk.startswith(("/", "./", "../", "#")):
            out.append(t); continue
        lo = t.lower()
        if lo.startswith("grey"):
            if re.match(r"[\s\-]*turner", s[pos:pos + 12], re.I):
                out.append(t); continue          # Grey Turner sign (a surname)
            if re.match(r"\s*[;}!]", s[pos:pos + 3]) or re.search(r":\s*$", s[max(0, start - 3):start]):
                out.append(t); continue          # CSS colour value
        out.append(rep)
        if hits is not None:
            hits.append((where, t, rep, s[max(0, start - 40):pos + 40].replace("\n", " ")))
    res = "".join(out)
    # two-word forms
    def pc(m):
        if hits is not None:
            hits.append((where, m.group(0), "percent", m.group(0)))
        return "Percent" if m.group(1)[0] == "P" else ("PERCENT" if m.group(1) == "PER" else "percent")
    res = re.sub(r"\b(per|Per|PER)[  -](?:cent|CENT)\b", pc, res)
    return res


VISIBLE_ATTRS = ("alt", "title", "aria-label", "placeholder", "content", "data-tip",
                 "data-hint", "data-desc", "data-title", "data-label")
ATTR = re.compile(r'(\s)([A-Za-z_:][-A-Za-z0-9_:.]*)(\s*=\s*)("([^"]*)"|\'([^\']*)\')')


def fix_tag(tag, hits, where):
    def one(m):
        name = m.group(2).lower()
        val = m.group(5) if m.group(5) is not None else m.group(6)
        if name not in VISIBLE_ATTRS and not (name.startswith("data-") and re.search(r"\s", val)):
            return m.group(0)
        if name == "content" and not re.search(r"\s", val):
            return m.group(0)
        q = m.group(4)[0]
        return m.group(1) + m.group(2) + m.group(3) + q + fix_text(val, hits=hits, where=where) + q
    return ATTR.sub(one, tag)


MARKUP = re.compile(r"<!--.*?-->|<(script|style)\b[^>]*>.*?</\1\s*>|<[^<>]+>|[^<]+|<", re.S | re.I)


def fix_markup(s, hits, where, code_string=False, js_scripts=True):
    """Text that may contain HTML: rewrite text nodes and visible attributes,
    leave tags, CSS and comments alone, and keep the io-box verbatim."""
    if "<" not in s:
        return fix_text(s, code_string=code_string, hits=hits, where=where)
    out = []
    io_depth = 0
    for m in MARKUP.finditer(s):
        t = m.group(0)
        if t.startswith("<!--"):
            out.append(t); continue
        if m.group(1):
            if m.group(1).lower() == "script" and js_scripts:
                open_end = t.index(">") + 1
                close_start = t.lower().rindex("</script")
                body = t[open_end:close_start]
                typ = re.search(r'type\s*=\s*["\']([^"\']+)', t[:open_end])
                if typ and "json" not in typ.group(1) and "javascript" not in typ.group(1) \
                        and "module" not in typ.group(1):
                    out.append(t); continue
                out.append(t[:open_end] + fix_js(body, hits, where) + t[close_start:])
            else:
                out.append(t)
            continue
        if t.startswith("<") and len(t) > 1:
            if io_depth:
                if re.match(r"<div\b", t, re.I):
                    io_depth += 1
                elif re.match(r"</div\s*>", t, re.I):
                    io_depth -= 1
                out.append(t); continue
            if re.match(r'<div\b[^>]*class="[^"]*\bio-box\b', t, re.I):
                io_depth = 1
                out.append(t); continue
            out.append(fix_tag(t, hits, where)); continue
        if io_depth:
            out.append(t); continue
        out.append(fix_text(t, code_string=code_string and not re.search(r"\s", t),
                            hits=hits, where=where))
    return "".join(out)


def _string_body(body, hits, where):
    # a string holding markup is markup; otherwise it is plain text / maybe code
    if re.search(r"<[A-Za-z/!]", body):
        return fix_markup(body, hits, where, code_string=True)
    return fix_text(body, code_string=True, hits=hits, where=where)


def fix_js(src, hits, where, json_mode=False):
    """Rewrite words inside string literals only (JS or JSON)."""
    out = []
    i, n = 0, len(src)
    last_sig = ""
    while i < n:
        c = src[i]
        if c in "\"'`":
            j = i + 1
            while j < n and src[j] != c:
                if src[j] == "\\":
                    j += 1
                elif c == "`" and src[j] == "$" and j + 1 < n and src[j + 1] == "{":
                    depth = 0
                    while j < n:
                        if src[j] == "{": depth += 1
                        elif src[j] == "}":
                            depth -= 1
                            if depth == 0: break
                        j += 1
                j += 1
            body = src[i + 1:j]
            k = j + 1
            while k < n and src[k] in " \t\r\n":
                k += 1
            is_key = (k < n and src[k] == ":" and (json_mode or last_sig in "{,"))
            if is_key or (c == "`" and "${" in body):
                if c == "`" and "${" in body and not is_key:
                    # rewrite only the literal parts between ${...}
                    parts = re.split(r"(\$\{[^}]*\})", body)
                    body = "".join(p if p.startswith("${") else _string_body(p, hits, where) for p in parts)
                out.append(c + body + c)
            else:
                out.append(c + _string_body(body, hits, where) + c)
            i = j + 1
            last_sig = c
            continue
        if not json_mode and c == "/" and i + 1 < n and src[i + 1] == "/":
            j = src.find("\n", i)
            j = n if j < 0 else j
            out.append(src[i:j]); i = j; continue
        if not json_mode and c == "/" and i + 1 < n and src[i + 1] == "*":
            j = src.find("*/", i + 2)
            j = n if j < 0 else j + 2
            out.append(src[i:j]); i = j; continue
        if not json_mode and c == "/" and (last_sig == "" or last_sig in "(,=:[!&|?{};+-*%<>~^"):
            j = i + 1
            in_cls = False
            while j < n and src[j] != "\n":
                if src[j] == "\\": j += 2; continue
                if src[j] == "[": in_cls = True
                elif src[j] == "]": in_cls = False
                elif src[j] == "/" and not in_cls: break
                j += 1
            if j < n and src[j] == "/":
                j += 1
                while j < n and src[j].isalpha(): j += 1
                out.append(src[i:j]); i = j; last_sig = ")"; continue
        out.append(c)
        if not c.isspace():
            last_sig = c
        i += 1
    return "".join(out)


def fix_py(src, hits, where):
    """Rewrite words inside Python string literals (incl. f-string text)."""
    toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    lines = src.splitlines(keepends=True)
    offs = [0]
    for ln in lines:
        offs.append(offs[-1] + len(ln))
    edits = []
    FSM = getattr(tokenize, "FSTRING_MIDDLE", None)
    TSM = getattr(tokenize, "TSTRING_MIDDLE", None)
    for t in toks:
        if t.type == tokenize.STRING:
            a = offs[t.start[0] - 1] + t.start[1]
            b = offs[t.end[0] - 1] + t.end[1]
            lit = src[a:b]
            m = re.match(r"^([A-Za-z]*)('''|\"\"\"|'|\")", lit, re.S)
            pre, q = m.group(1), m.group(2)
            if "b" in pre.lower():
                continue
            body = lit[len(pre) + len(q):len(lit) - len(q)]
            new = _string_body(body, hits, where)
            if new != body:
                edits.append((a, b, pre + q + new + q))
        elif t.type in (FSM, TSM) and t.type is not None:
            a = offs[t.start[0] - 1] + t.start[1]
            b = offs[t.end[0] - 1] + t.end[1]
            body = src[a:b]
            new = _string_body(body, hits, where)
            if new != body:
                edits.append((a, b, new))
    for a, b, new in sorted(edits, reverse=True):
        src = src[:a] + new + src[b:]
    return src


def fix_file(path, hits):
    rel = os.path.relpath(path, ROOT)
    src = open(path, encoding="utf-8").read()
    if path.endswith(".py"):
        new = fix_py(src, hits, rel)
    elif path.endswith(".json"):
        new = fix_js(src, hits, rel, json_mode=True)
    elif path.endswith(".js"):
        if os.path.basename(path) == "arcade.js":
            new = fix_arcade(src, hits, rel)
        else:
            new = fix_js(src, hits, rel)
    elif path.endswith((".html", ".htm")):
        if rel == "index.html":
            new = fix_index(src, hits, rel)
        elif rel == "guides.html":
            new = fix_guides(src, hits, rel)
        else:
            new = fix_markup(src, hits, rel)
    else:
        return src, src
    return src, new


# ------------------------------------------------------------------ scope

def semesters():
    s = open(os.path.join(ROOT, "semesters.js"), encoding="utf-8").read()
    sems = []
    for m in re.finditer(r'id:\s*"([^"]+)"(.*?)classes:\s*\[(.*?)\]', s, re.S):
        sems.append((m.group(1), re.findall(r'"([^"]+)"', m.group(3))))
    rules = [(re.compile(p.replace("\\/", "/"), re.I if f else 0), c)
             for p, f, c in re.findall(r'\[/(.+?)/(i?),\s*"([^"]+)"\]', s)]
    return sems, rules


def in_scope_classes():
    sems, _ = semesters()
    ids = [sid for sid, _ in sems]
    cut = ids.index("fall-2026")
    return {c for sid, cls in sems[cut:] for c in cls}


def class_of_folder(folder):
    _, rules = semesters()
    for rx, c in rules:
        if rx.search(folder):
            return c
    return None


def scope_folders():
    live = in_scope_classes()
    out = []
    for d in sorted(os.listdir(ROOT)):
        if os.path.isdir(os.path.join(ROOT, d)) and class_of_folder(d) in live:
            out.append(d)
    return out


def frozen_folders():
    live = in_scope_classes()
    return [d for d in sorted(os.listdir(ROOT))
            if os.path.isdir(os.path.join(ROOT, d)) and class_of_folder(d)
            and class_of_folder(d) not in live]


# Tools that generate Semester 2+ content. Chosen by what they reference: a
# tool is in scope when it names a Semester 2+ class folder or output (or is a
# JSON data file with a Semester 2+ prefix) and names no Semester 1 folder.
S2_PREFIX = re.compile(r"^(cms|cmse\d|cmsderm|cmsent|cmsophtho|cp|clinpath|pd2|pdm|micro|mb|medlit|"
                       r"pharm(?!aco?dyn)|clinmedpro)[_-]", re.I)
TOOL_SKIP = re.compile(r"^(check_|audit_|measure_|console_|transcribe_|pull_|ocr_|"
                       r"parse_|dump_|gen_calendar|daily_|lecture_|verify_)")


# shared infrastructure that names Semester 2 folders but writes no content of
# its own (and _lecturers.py, whose strings are match patterns)
TOOL_EXCLUDE = {"check_us_spelling.py", "_lecturers.py", "build_guide_docx.py",
                "build_master_exams.py", "patch_quiz_engine_v2.py", "patch_quiz_engine_v2b.py",
                "fix_guide_footers.py", "add_guide_report_footer.py",
                "patch_guide_top_and_save.py", "_arcade_add.py", "_pharm_render_guard.py"}


# content tools whose names do not say which class they serve
TOOL_INCLUDE = {"add_chart_giveaways.py", "deoverlap_giveaways.py", "fix_dependent_stems.py",
                "_cmse3_leadin_fp.py", "_cmse3_leadins.py"}


def scope_tools():
    live_f = scope_folders()
    frozen_f = frozen_folders()
    # Semester 1 is recognised by its FOLDER names, never by bare words --
    # "anatomy" or "physiology" turn up in Semester 2 question text all the time
    s1_words = sorted(set(frozen_f)) + ["Pharmacodynamics", "CAM Nutrition", "Intro to PA",
                                        "Physical Diagnosis 1", "Nutrition Class"]
    s2_words = sorted({f.split(" Exam")[0] for f in live_f})
    out = []
    tdir = os.path.join(ROOT, "tools")
    for dp, dn, fn in os.walk(tdir):
        dn[:] = [d for d in dn if d != "__pycache__"]
        for f in fn:
            if not f.endswith((".py", ".json", ".js", ".html")):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, tdir)
            base = os.path.basename(f)
            if base in TOOL_EXCLUDE or TOOL_SKIP.match(base):
                continue
            if rel.startswith(("quiz-template", "cram-sheet-template", "clinmedpro")):
                out.append(p); continue
            txt = open(p, encoding="utf-8", errors="replace").read()
            s1_name = re.match(r"_?(physio|anatomy|pd1|pharmacodynamics|pharmacod|cam|intro)[_-]", base, re.I)
            s1 = s1_name or any(w in txt for w in s1_words)
            core = re.sub(r"^(build|add|render|extract|mark|fold|fix|apply|swap|patch|tighten|"
                          r"prune|trim|deoverlap)_", "", base.lstrip("_"))
            if base in TOOL_INCLUDE or base.startswith("_osce_batch_") or \
                    ((S2_PREFIX.match(base.lstrip("_")) or S2_PREFIX.match(core)) and not s1_name):
                out.append(p); continue              # named for a Semester 2 class
            s2 = any(w in txt for w in s2_words)
            if s2 and not s1:
                out.append(p)
    return sorted(out)


def scope_files():
    files = []
    for d in scope_folders():
        for dp, dn, fn in os.walk(os.path.join(ROOT, d)):
            for f in fn:
                if f.endswith((".html", ".json", ".js")) and not f.endswith(".min.js"):
                    files.append(os.path.join(dp, f))
    files += scope_tools()
    files += [os.path.join(ROOT, x) for x in ("arcade.js", "index.html", "guides.html")]
    return sorted(set(files))


# ------------------------------------------------------------------ shared pages

def s2_deck_ids(src):
    live = in_scope_classes()
    ids = set()
    m = re.search(r"var DEMO_CLASSES = \[(.*?)\n\];", src, re.S)
    for cm in re.finditer(r'\{ id: "([^"]+)", name: "[^"]*", exams: \[(.*?)\]\},?\s*(?=\{ id:|$)',
                          m.group(1) + "\n", re.S):
        cid = cm.group(1)
        cid = {"physiology": "physio"}.get(cid, cid)
        if cid in live:
            ids.update(re.findall(r'"([a-z0-9-]+)"', cm.group(2)))
    return ids


def fix_arcade(src, hits, where):
    """Only the Semester 2+ decks of DEMO_DECKS; the engine and Semester 1
    decks are left as they are."""
    keep = s2_deck_ids(src)
    starts = [(m.start(), m.group(1)) for m in
              re.finditer(r'^  \{ id: "([^"]+)",', src, re.M)]
    end_decks = src.index("\n];", src.index("var DEMO_DECKS = ["))
    out, last = [], 0
    for k, (a, did) in enumerate(starts):
        if a > end_decks:
            break
        b = starts[k + 1][0] if k + 1 < len(starts) and starts[k + 1][0] < end_decks else end_decks
        if did in keep:
            out.append(src[last:a])
            out.append(fix_js(src[a:b], hits, where + ":" + did))
            last = b
    out.append(src[last:])
    return "".join(out)


def fix_index(src, hits, where):
    """The Fall-and-later semester blocks of index.html only."""
    live = [sid for sid, _ in semesters()[0]][[sid for sid, _ in semesters()[0]].index("fall-2026"):]
    out, last = [], 0
    for m in re.finditer(r'<div class="semester"[^>]*data-semester="([^"]+)"', src):
        if m.group(1) not in live:
            continue
        # the block runs to the next semester block (or the end of the card)
        nxt = re.compile(r'<div class="semester"[^>]*data-semester=').search(src, m.end())
        b = nxt.start() if nxt else src.index("</main>") if "</main>" in src else len(src)
        out.append(src[last:m.start()])
        out.append(fix_markup(src[m.start():b], hits, where, js_scripts=False))
        last = b
    out.append(src[last:])
    return "".join(out)


def fix_guides(src, hits, where):
    """Only the guides.html cards that point into a Semester 2+ folder."""
    live = [f.replace(" ", "%20") for f in scope_folders()]
    def card(m):
        href = re.search(r'href="([^"/]+)/', m.group(0))
        if href and href.group(1) in live:
            return fix_markup(m.group(0), hits, where)
        return m.group(0)
    return re.sub(r'<a class="guide-card[^"]*"[^>]*>.*?</a>', card, src, flags=re.S)


# ------------------------------------------------------------------ main

def main(argv):
    fix = "--fix" in argv
    paths = [a for a in argv if not a.startswith("--")]
    files = [os.path.abspath(p) for p in paths] if paths else scope_files()
    if "--list" in argv:
        for f in files:
            print(os.path.relpath(f, ROOT))
        print("%d file(s) in scope" % len(files))
        return 0
    hits = []
    changed = []
    for f in files:
        h = []
        try:
            old, new = fix_file(f, h)
        except Exception as e:                  # never silently skip a file
            print("ERROR %s: %s" % (os.path.relpath(f, ROOT), e))
            return 2
        hits += h
        if new != old:
            changed.append(f)
            if fix:
                if f.endswith(".py"):
                    ast.parse(new)
                elif f.endswith(".json"):
                    json.loads(new)
                open(f, "w", encoding="utf-8").write(new)
    per_file = Counter(h[0].split(":")[0] for h in hits)
    words = Counter((h[1].lower(), h[2].lower()) for h in hits)
    if "--words" in argv:
        for (a, b), n in words.most_common():
            print("%6d  %s -> %s" % (n, a, b))
    if "--context" in argv:
        for h in hits:
            print("%s | %s -> %s | %s" % h)
    print("%s %d British spelling(s) in %d of %d file(s) in scope"
          % ("fixed" if fix else "found", len(hits), len(changed), len(files)))
    if not fix:
        for f, n in per_file.most_common(15):
            print("   %5d  %s" % (n, f))
    return 0 if (fix or not hits) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
