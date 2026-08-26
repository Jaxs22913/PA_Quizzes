import re

# -*- coding: utf-8 -*-
"""Prof. Jaquith's three discriminators for every Exam 2 ophthalmology condition.

ONE SOURCE OF TRUTH, imported by BOTH the comparison chart and the cram sheet.
They were written out separately at first and immediately drifted -- the cram's
"painless" list was missing four conditions and its "bilateral" list had one the
chart classified differently. Hand-maintaining the same fact in two places is
how that happens, so the cram now GENERATES its lists from this table.

Her instruction, from the end of the 26 August lecture:

  "My recommendation to you guys for those is again, use your resources, MAKE A
   CHART -- which ones cause PAIN, which ones don't cause pain? Which ones are
   UNILATERAL, which ones are BILATERAL? Which ones will cause which PHYSICAL
   EXAM ABNORMALITIES, like FIXED PUPILS, for example. That's how you're gonna
   differentiate these ... at least two questions minimum."

Values are HTML, because both consumers render them directly.
"""

DIFF = {'Entropion': ('No &mdash; irritation, foreign body sensation', 'Either', 'Lid margin turns <b>IN</b>; lashes on the globe (trichiasis)'), 'Ectropion': ('No &mdash; tearing', 'Either', 'Lid margin turns <b>OUT</b>; inner surface exposed'), 'Dermatochalasis': ('No', 'Bilateral', 'Excess skin folds; <b>visual field deficit</b>'), 'Xanthelasma': ('No &mdash; asymptomatic', 'Usually bilateral', 'Oval <b>yellow plaques</b>, nasal lid'), 'Blepharitis / Meibomitis': ('No &mdash; burning, grittiness', 'Bilateral', '<b>Crusting at the lash bases</b>; toothpaste-like secretion'), 'Chalazion': ('<b>NO &mdash; non-tender</b>', 'Unilateral', 'Nodule that <b>points inside the lid</b>'), 'Hordeolum (stye)': ('<b>YES &mdash; tender</b>', 'Unilateral', 'Tender nodule <b>at the lid margin</b>'), 'Dacryoadenitis': ('<b>YES</b>', 'Unilateral (viral often bilateral)', 'Swelling <b>outer &frac13; of the UPPER lid</b> + preauricular node'), 'Dacryocystitis': ('<b>YES</b>', 'Unilateral', 'Swelling <b>below the medial canthal tendon</b>; pus from the punctum'), 'Pinguecula': ('No &mdash; irritation', 'Either', 'Yellow nodule that <b>stops at the limbus</b>'), 'Pterygium': ('No &mdash; irritation', 'Either', 'Wing of tissue <b>crossing onto the cornea</b>'), 'Subconjunctival haemorrhage': ('<b>NO &mdash; absent</b>', 'Unilateral', 'Blood under the conjunctiva; <b>vision, pupil and cornea all normal</b>'), 'Chemosis': ('Varies with the cause', 'Either', '<b>Swelling of the conjunctiva itself</b>'), 'Allergic conjunctivitis': ('No &mdash; <b>ITCH</b>', '<b>Bilateral</b>', '<b>Papillae</b> (&ldquo;like a strawberry&rdquo;), chemosis, <b>no node</b>'), 'Viral conjunctivitis': ('No &mdash; uncomfortable, tight', '<b>Bilateral</b> (starts in one eye)', '<b>Follicles</b> + <b>TENDER preauricular node</b> + watery discharge'), 'Bacterial conjunctivitis': ('Soreness rather than pain', '<b>Often UNILATERAL</b>', '<b>Papillae</b> + thick yellow discharge, usually <b>no node</b>'), 'Gonococcal conjunctivitis': ('<b>YES &mdash; severe</b>', 'Either; neonate often bilateral', '<b>Severe purulent discharge WITH a palpable preauricular node</b>'), 'Chlamydial conjunctivitis &mdash; adult inclusion': ('No', 'Unilateral, sometimes bilateral', '<b>Follicles</b>, chronic beyond a month, topical treatment failed'), 'Chlamydial conjunctivitis &mdash; neonatal': ('&mdash;', 'Bilateral', 'Neonate; may also have <b>pneumonia</b>'), 'Trachoma': ('Mostly <b>asymptomatic</b>', 'Bilateral', '<b>Upper lid follicles</b>, then scarring, entropion, trichiasis'), 'Autoimmune conjunctivitis': ('<b>Minimal or none</b>, and <b>no discharge</b>', 'Bilateral', 'Recurrent redness with <b>systemic complaints</b>'), 'Episcleritis': ('<b>MILD</b>', 'Unilateral (may recur in either eye)', 'Sectoral redness; vessels <b>MOVE</b>; <b>blanch with phenylephrine</b>'), 'Scleritis': ('<b>SEVERE, boring, WORSE AT NIGHT</b>', 'Unilateral', '<b>Violaceous hue</b>; vessels do <b>NOT</b> move; pain on eye movement'), 'Pre-septal (periorbital) cellulitis': ('<b>YES</b> &mdash; periocular', 'Unilateral', '<b>THE EYE ITSELF IS WHITE</b>; movements full and painless'), 'Post-septal (orbital) cellulitis': ('<b>YES</b>, and <b>pain ON EYE MOVEMENT</b>', 'Unilateral', '<b>PROPTOSIS</b>, restricted painful movement, &plusmn; <b>afferent pupillary defect</b>'), 'Keratitis': ('<b>YES</b>', 'Unilateral', 'Corneal opacification, <b>CILIARY FLUSH</b>, &ldquo;broken up&rdquo; light reflection'), 'Herpes simplex keratitis': ('<b>YES</b>', 'Unilateral', '<b>Dendrite with TERMINAL END BULBS</b> on fluorescein'), 'Herpes zoster keratitis': ('<b>YES</b> &mdash; and skin pain', 'Unilateral, <b>dermatomal V1</b>', '<b>Pseudodendrite</b> (no end bulbs); <b>Hutchinson sign</b>'), 'Corneal ulcer': ('<b>YES</b> &mdash; resists opening the eye', 'Unilateral', '<b>White corneal infiltrate</b> + ciliary flush'), 'Anterior uveitis (iritis, iridocyclitis)': ('<b>YES</b>', 'Unilateral', '<b>CONSENSUAL photophobia</b>, ciliary flush, <b>IRREGULAR pupil</b>, cells in the anterior chamber'), 'Posterior uveitis (choroiditis, retinitis)': ('<b>NO</b> if isolated', 'Either', '<b>Cells in the vitreous</b>, vitreous haze, floaters')}


def classify(pain, side):
    """Bucket one condition for the chart's filters and the cram's lists.

    The first version keyed on exact strings and mis-bucketed two rows:
    "Usually bilateral" fell through to 'either', and "Mostly asymptomatic"
    fell through to 'var' instead of painless. Both are handled here.
    """
    p = re.sub(r"<[^>]+>", "", pain).strip().upper()
    if p.startswith("&MDASH;") or p in ("", "—"):
        painful = "na"
    elif "ASYMPTOMATIC" in p or p.startswith("NO"):
        painful = "no"
    elif "VARIES" in p or "SORENESS" in p:
        painful = "var"
    elif p.startswith(("YES", "SEVERE", "MILD", "MINIMAL")):
        painful = "no" if p.startswith("MINIMAL") else "yes"
    else:
        painful = "var"

    s = re.sub(r"<[^>]+>", "", side).strip().lower()
    # Order matters. "Either; neonate often bilateral" contains "bilateral" and
    # was being bucketed as bilateral -- so an explicit "either" wins first.
    if s.startswith("either"):
        lat = "either"
    elif s.startswith("unilateral"):
        lat = "uni"
    elif "bilateral" in s and "unilateral" not in s:
        lat = "bi"
    else:
        lat = "either"
    return painful, lat


def bucket(key):
    """All condition names in one bucket, in the chart's own row order."""
    out = []
    for name, (pain, side, _sign) in DIFF.items():
        p, l = classify(pain, side)
        if key in (p, "lat_" + l):
            out.append(name)
    return out
