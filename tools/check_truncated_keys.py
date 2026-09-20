"""Find keys damaged by an over-aggressive length-bias trim.

The defect: a key that is a genuine enumeration gets cut to its first item and
the remainder is appended to its explanation as a dangling noun phrase. The
content survives; the ANSWER does not. Four independent signatures, because no
single one catches them all:

  A  number word, fewer items   "Three: the left posterior, the septal"
  B  stem asks a list, key names one thing
  C  orphan tail -- the STEM asks for a list, the key names ONE thing, and the
     explanation's last sentence is a short comma-list of more things of the
     same kind. That conjunction is what makes it precise. A first attempt
     tested only "tail has no finite verb" and flagged 246 perfectly good
     explanations, because the verb list can never be complete ("opposes",
     "antagonises" were both missing). Requiring the stem to ask for a list AND
     the key to be a single item cut that to 5, all of them real.
  D  key ends mid-list, on a comma or a trailing conjunction
"""
import glob, importlib.util, re, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

NUM = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8}
LIST_Q = re.compile(r"\bwhich (are|factors|injuries|causes|types|kinds|categories|forms|"
                    r"things|features|findings|three|four|five)\b|"
                    r"\bwhat are the\b|\bin what order\b|\blist the\b|\bname the\b", re.I)
def items(s):
    body = re.sub(r'^\s*\w+[:,]\s*', '', s)
    return len([p for p in re.split(r',| and ', body) if p.strip()])

def sweep():
    out = []
    for f in sorted(glob.glob('tools/*pool*.py')):
        mod = os.path.basename(f)[:-3]
        try:
            spec = importlib.util.spec_from_file_location(mod, f)
            m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        except Exception:
            continue
        for attr in dir(m):
            P = getattr(m, attr)
            if not (isinstance(P, list) and P and isinstance(P[0], dict) and 'opts' in P[0]):
                continue
            for q in P:
                key, expl = q['opts'][0][0], q['opts'][0][1]
                sig = []
                n = re.match(r'^(two|three|four|five|six|seven|eight)\b[:,]', key, re.I)
                if n and items(key) < NUM[n.group(1).lower()]:
                    sig.append('A')
                if LIST_Q.search(q['q']) and not re.search(r',| and | or ', key, re.I) and len(key) < 40:
                    sig.append('B')
                sents = [x.strip() for x in re.split(r'(?<=[.!?])\s+', expl.strip()) if x.strip()]
                if LIST_Q.search(q['q']) and not re.search(r',| and | or ', key, re.I) \
                   and len(sents) > 1:
                    tail = sents[-1].rstrip('.')
                    if (',' in tail or ' and ' in tail.lower()) and len(tail.split()) <= 11 \
                       and not re.match(r'^(it|they|this|that|these|those)\b', tail, re.I):
                        sig.append('C')
                if re.search(r'[,;]\s*$|\b(and|or|with|plus)\s*$', key, re.I):
                    sig.append('D')
                if sig:
                    out.append((mod, ''.join(sig), q['q'], key, sents[-1] if sents else ''))
    return out

if __name__ == '__main__':
    rows = sweep()
    for mod, sig, stem, key, tail in rows:
        print(f"[{sig:<4}] {mod}")
        print(f"        Q {stem[:92]}")
        print(f"        A {key[:92]}")
        if 'C' in sig: print(f"        tail: {tail[:88]}")
    print(f"\n{len(rows)} flagged")
