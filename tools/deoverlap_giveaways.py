#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Make every vignette giveaway DISCRIMINATE, not merely describe.

A phrase shared by two conditions is not a giveaway. Measured across the first
version of the column, three bold fragments and several key concepts were doing
double duty:

    well-demarcated      Allergic contact dermatitis / plaque psoriasis
    Nikolsky positive    Pemphigus / toxic epidermal necrolysis
    poorly demarcated    Atopic dermatitis / cellulitis
    umbilication         Molluscum / sebaceous hyperplasia
    central clearing     Erythema migrans / tinea corporis
    collarette           Pityriasis rosea / pyogenic granuloma
    pearly               Two basal cell carcinomas / molluscum
    blanches             Five vascular lesions

TWO KINDS OF FIX, and the second is the more useful one:

  1. LEAD WITH WHAT IS UNIQUE. Allergic contact dermatitis now leads on the
     linear vesicles in multiple stages of healing rather than on
     "well-demarcated", which it shares with psoriasis.

  2. WHERE A FEATURE IS GENUINELY SHARED, SAY SO AND NAME WHAT SEPARATES THEM.
     Nikolsky positive really is true of both pemphigus and toxic epidermal
     necrolysis, so the cell now says it does not separate them and gives what
     does. Same for umbilicated papules (molluscum is pearly and in children;
     sebaceous hyperplasia is yellow and in older adults) and for the annular
     lesion with central clearing (tinea has scale on the advancing border;
     erythema migrans does not, and follows a tick).

That second kind is what turns the column from a list of adjectives into
something you can actually discriminate with, which is what a vignette asks for.

Deck language only, as before.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
# ONLY the authoring script. build_cms_derm_chart.py holds SEVERAL dicts keyed
# on the same condition names -- GIVEAWAY and LABS among them -- and a
# name-keyed regex there matched the LABS entry first and overwrote 29 lab
# values with giveaway text. The build still passed: "every cell populated" is
# true of a cell filled with the wrong thing. Edit the source, re-inject, never
# pattern-match a generated file that has more than one dict shaped alike.
TARGETS = [os.path.join(HERE, "add_chart_giveaways.py")]

REWRITE = {
 "Atopic dermatitis": "<b>FLEXURES in children and adults; cheeks and extensors in INFANTS</b> &middot; lichenification from chronic scratching &middot; poorly demarcated &middot; personal or family atopy",
 "Nummular eczema": "<b>COIN-SHAPED discrete plaques</b> &mdash; the shape IS the diagnosis &middot; extremities",
 "Allergic contact dermatitis": "<b>LINEAR vesicles in MULTIPLE STAGES OF HEALING</b> (urushiol / poison ivy) &middot; well-demarcated <b>at the contact site</b> &middot; needs prior sensitisation",
 "Irritant contact dermatitis": "<b>Well demarcated and &ldquo;GLAZED APPEARING&rdquo;</b> &middot; <b>shaped like the exposure</b> &middot; hands and forearms &middot; frequent handwashing, gloves &middot; no sensitisation needed",
 "Bullous pemphigoid": "<b>TENSE bullae that do NOT rupture easily</b> &middot; <b>Nikolsky NEGATIVE &mdash; the one of the three that is</b> &middot; elderly &middot; mucosa uncommon",
 "Pemphigus (vulgaris)": "<b>FLACCID bullae that rupture, leaving erosions</b> &middot; <b>MUCOSA often the FIRST site</b> &middot; middle-aged &middot; Nikolsky positive &mdash; <b>so is toxic epidermal necrolysis, so it does not separate them</b>",
 "Toxic epidermal necrolysis": "<b>&gt;30% body surface DETACHMENT</b> &middot; <b>&ldquo;wet parchment&rdquo;</b> &middot; drug and prodrome 1&ndash;3 days before &middot; Nikolsky positive &mdash; <b>shared with pemphigus; the body-surface figure is what separates them</b>",
 "Psoriasis &mdash; plaque": "<b>Thick SILVERY scale</b> &middot; <b>Auspitz sign</b> when the scale is lifted &middot; EXTENSOR surfaces, scalp, nails &middot; psoriatic arthritis goes with it",
 "Pityriasis rosea": "<b>HERALD PATCH alone for a week or two BEFORE the rest</b> &middot; <b>Christmas-tree</b> pattern along skin lines &middot; collarette of SCALE",
 "Pyogenic granuloma": "<b>Moist bright red papule that BLEEDS readily, with an EPITHELIAL COLLARETTE at its BASE</b> &middot; pregnancy, fingers &middot; misnamed &mdash; neither infectious nor granulomatous",
 "Cellulitis": "<b>Poorly demarcated and FLAT</b> &mdash; <b>erysipelas is sharply demarcated and RAISED</b> &middot; deeper dermis and subcutis &middot; lower leg",
 "Erysipelas": "<b>Sharply demarcated, RAISED border</b> &mdash; <b>cellulitis is flat and poorly demarcated</b> &middot; sudden high fever within 48 hours &middot; UPPER dermis",
 "Molluscum contagiosum": "<b>Umbilicated PEARLY FLESH-COLOURED dome</b>, 3&ndash;5&nbsp;mm &middot; poxvirus, children &middot; <b>vs sebaceous hyperplasia, which is YELLOW and in older adults</b>",
 "Sebaceous hyperplasia": "<b>YELLOW umbilicated papule in an OLDER ADULT</b> &middot; face &middot; <b>vs molluscum, which is pearly flesh-coloured and in children</b> &middot; no malignant potential",
 "Tinea corporis (body) &mdash; &ldquo;ringworm&rdquo;": "<b>Annular, with SCALE ON THE ADVANCING BORDER</b> and progressive central clearing &middot; <b>the scale is what separates it from granuloma annulare AND from erythema migrans</b>",
 "Lyme disease": "<b>&gt;5&nbsp;cm ring EXPANDING over days after a tick</b>, central clearing, darker punctate centre &middot; <b>NO scale on the border &mdash; unlike tinea</b>",
 "Granuloma annulare": "<b>Annular ring of papules with NO SCALE ANYWHERE</b> &mdash; that absence separates it from tinea &middot; dorsal hands and feet &middot; flesh-coloured",
 "Cherry angioma": "<b>Deep red dome that INCREASES IN NUMBER WITH AGE</b> &middot; trunk &middot; &lt;5&nbsp;mm &middot; new ones keep appearing and cannot be prevented",
 "Telangiectasia": "<b>A permanently dilated capillary UNDER 1&nbsp;mm</b>, sometimes with a central punctum &middot; associated with numerous diseases &mdash; work up the cause",
 "Nevus araneus (spider angioma)": "<b>ESTROGEN EXCESS</b> &mdash; pregnancy or the pill (both resolve after), <b>CIRRHOSIS and liver failure</b> &middot; dilation of existing vessels, no proliferation",
 "Infantile hemangioma": "<b>INVOLUTES &mdash; 50% by 5, 70% by 7, 90% by 9</b> &middot; preterm, female 3:1 &middot; earliest sign is BLANCHING, then fine telangiectasias, then bright red",
 "Nevus flammeus (port-wine stain)": "<b>NEVER involutes</b> &mdash; dilation with NO endothelial proliferation, which is why &middot; present at birth, <b>DARKENS and THICKENS</b> &middot; sharp midline cutoff",
 "Seborrheic keratosis": "<b>&ldquo;STUCK ON&rdquo; or pasted-on</b>, velvety or warty, beige to black &middot; <b>dermatosis papulosa nigrans is the SAME lesion, small, on the FACE of darker skin</b>",
 "Dermatosis papulosa nigrans": "<b>Multiple small dark papules on the FACE and NECK of darker skin</b> &middot; <b>histologically identical to seborrheic keratosis &mdash; the site and the skin tone are the clue</b>",
 "Basal cell carcinoma &mdash; nodular": "<b>PEARLY translucent papule whose telangiectasias STRETCHING THE SKIN accentuates</b> &middot; central erosion &middot; slow growth over years &middot; INTERMITTENT intense sun",
 "Basal cell carcinoma &mdash; superficial": "<b>Reddish shiny scaly THIN plaque on the BACK or CHEST</b> &middot; thready pearly border with spotty edge pigment",
 "Pressure injury (pressure ulcer)": "<b>NON-BLANCHABLE erythema over a BONY PROMINENCE</b> = stage 1 &middot; obscured by slough or eschar = unstageable &middot; the non-blanching is the whole point",
 "Diaper dermatitis": "<b>CONVEX surfaces of the napkin area, sparing the folds</b> &middot; <b>once the FOLDS are involved with satellite lesions, it is candidal</b>",
 "Cutaneous candidiasis and intertrigo": "<b>SATELLITE lesions beyond the main patch</b>, in body folds &middot; friction, moisture and heat &middot; <i>Candida albicans</i>",
}


def main():
    n_files = 0
    for path in TARGETS:
        s = open(path, encoding="utf-8").read()
        before = s
        for name, new in REWRITE.items():
            # the dict is stored repr'd in the chart builder and literal in the
            # authoring script, so match the key in either quoting style
            for k in ('"%s"' % name, "'%s'" % name):
                pat = re.compile(re.escape(k) + r"\s*:\s*(?P<q>['\"])(?P<val>.*?)(?<!\\)(?P=q)", re.S)
                m = pat.search(s)
                if not m:
                    continue
                q = m.group("q")
                repl = k + ": " + q + new.replace(q, "\\" + q) + q
                s = s[:m.start()] + repl + s[m.end():]
                break
            else:
                sys.exit("key not found in %s: %r" % (os.path.basename(path), name))
        if s != before:
            open(path, "w", encoding="utf-8").write(s)
            n_files += 1
    print("rewrote %d giveaway(s) across %d file(s)" % (len(REWRITE), n_files))


if __name__ == "__main__":
    main()
