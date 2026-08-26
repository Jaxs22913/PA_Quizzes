#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Lecture 3 (Advanced Ocular Examination) topics to the PD2 cram sheet.

The FIRST section is what she took OUT of scope, because on a cram sheet
knowing what you do not have to learn is worth as much as any fact -- and
Prof. Beck's skip instructions are binding.

Appended after the Lecture 2 sections. Idempotent.
"""
import os, re, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Physical Diagnosis 2 Exam 1",
                    "pd2-exam-1-cram-sheet.html")

TOPICS = [
 ("l3-scope", "★ WHAT SHE TOOK OUT OF SCOPE", "#b8860b", "#f7efd9", "#fbf7ec", "#7a5a08", [
   ("The named virus in viral conjunctivitis", "“I'm not going to test you on it, but adenovirus…” — she uses it for the great-mimicker story. NOTE: CMS I Exam 2 DOES test adenovirus. Different course."),
   ("The exophthalmometer", "“I am not going to test you on the minutia of how to do that test… it was 20 to 22 millimetres… DON'T WORRY ABOUT IT.” BUT RECOGNISING EXOPHTHALMOS IS IN — “about exophthalmos and how to recognise it.”"),
   ("The strabismus diagram", "“This is just a visual… that you don't have to memorize.” ESO-, EXO- and HYPERTROPIA as concepts stay in."),
   ("The corneal reflection test", "“We've already done this, so I'm not gonna test you on it… we already did that in PD1.”"),
   ("The Adie's pupil look-alikes", "Dysautonomia/POTS, Shy-Drager, diabetes, amyloidosis — “it's not on my test this time.” BUT ADIE'S PUPIL ITSELF IS IN: “you should know Adie's pupil, that could be on my test.”"),
   ("The Latin behind OD/OS/OU", "“I don't care if you remember Oculus Sinister or Dexter.” BUT THE ABBREVIATIONS ARE IN — “those are terms that you must remember.” OD RIGHT · OS LEFT · OU BOTH."),
 ]),
 ("l3-memory", "★ “VERY IMPORTANT TO COMMIT TO MEMORY”", "#8c1d12", "#f7e3e0", "#fbf1f0", "#6b1610", [
   ("DIPLOPIA and the cranial nerves", "HORIZONTAL (images SIDE BY SIDE) = palsy of CN III or VI. VERTICAL (images ON TOP of each other) = palsy of CN III or IV. Her shortcut: “THREE FOR BOTH OF THOSE” — CN III is in both patterns; side-by-side is where CN VI joins in."),
   ("The RED-EYE CHART — “be very familiar with that chart”", "It is a PICTURE on the slide, so it is in no text copy of the deck. Written out in full in the study guide. Scan it by COLUMN: pattern of redness, pain, vision, discharge, pupil, cornea, significance."),
   ("RED TEXT ON A SLIDE", "“See how this is in red — red's important too.” Said of: an ACUTE, SIGNIFICANTLY DILATED PUPIL IS A MEDICAL EMERGENCY, particularly with headache or neurologic signs — UNCAL HERNIATION or POSTERIOR COMMUNICATING ARTERY ANEURYSM."),
   ("THE REFERRAL LIST — “please know this list”", "Her reason: “because you're going to be making those dispos.” EMERGENT (ophtho/ER IMMEDIATELY): SUDDEN VISION LOSS · RETINAL ARTERY OCCLUSION · CHEMICAL BURNS · RUPTURE · ACUTE ANGLE-CLOSURE GLAUCOMA · VITREOUS HAEMORRHAGE. URGENT (ophtho in A DAY OR LESS): ACUTE GLAUCOMA · ORBITAL CELLULITIS · CORNEAL ULCER OR ABRASION · RETINAL DETACHMENT · MACULAR OEDEMA OR HAEMORRHAGE · HYPHAEMA."),
 ]),
 ("l3-history", "History & Symptom Patterns", "#4a5c24", "#e8ecdd", "#f4f6ee", "#3a4a1c", [
   ("The four axes", "TIME COURSE · PRECIPITATING FACTORS · PALLIATIVE/EXACERBATING VARIABLES · VISION LOSS."),
   ("Laterality and floaters", "BILATERAL visual loss → NEUROLOGIC, not ophthalmologic. MULTIPLE NEW flashes/floaters → RETINAL TEAR or VITREOUS HAEMORRHAGE. A SINGLE floater → probably benign."),
   ("Tempo", "RAPID deterioration → VASCULAR. GRADUAL → CATARACT and the like."),
   ("The anaesthetic test", "Pain RELIEVED by topical anaesthetic → a SURFACE problem (corneal injury). NOT relieved → a DEEPER source."),
   ("Four symptom patterns", "ACUTE/UNILATERAL/PAINLESS → retinal vascular occlusion, detachment, vitreous haemorrhage, macular degeneration. ACUTE/UNILATERAL/PAINFUL → cornea + anterior chamber: abrasion/ulcer, uveitis, traumatic hyphaema, acute narrow angle glaucoma. ACUTE/BILATERAL/PAINFUL → THERMAL, RADIATION or CHEMICAL. GRADUAL/PAINLESS → simple glaucoma or cataract."),
   ("Eye pain, qualified", "With BLINKING → abrasion or foreign body. GRITTY → conjunctivitis. + PHOTOPHOBIA → iris inflammation. + HEADACHE → acute narrow angle glaucoma. On EYE MOTION → optic neuritis. + TEMPORAL pain → temporal arteritis."),
   ("Discharge", "WATERY or MUCOID → allergic or viral. PURULENT → bacterial."),
   ("Don't forget to ask", "TETANUS STATUS in eye trauma. ACID OR ALKALI after a chemical splash. Systemic: DIABETES, HYPERTENSION and HIV — “HIV is going to affect basically any type of aetiology.”"),
 ]),
 ("l3-inspect", "Inspection", "#6b7f35", "#eaeee0", "#f5f7f0", "#54642a", [
   ("Order of the exam", "INSPECTION → external → cornea/lens/pupils → VISUAL ACUITY (“the vital sign of the eye”) → VISUAL FIELDS → OCULAR MOTILITY → PUPILLARY REACTIONS (CHECK BEFORE DILATING) → corneal reflection → special tests → slit lamp → pressure → ophthalmoscopy."),
   ("In trauma", "DO NOT PALPATE THE GLOBE."),
   ("Lid and brow signs", "SCALY brows → seborrhoeic dermatitis. LATERAL SPARSENESS → HYPOTHYROIDISM. PTOSIS → myasthenia gravis, CN III damage, or sympathetic damage (HORNER); senile = weak muscle + relaxed tissue + herniated fat weight. XANTHELASMA on the NASAL lid → lipid disorders."),
   ("HORDEOLUM vs CHALAZION on inspection", "HORDEOLUM: PAINFUL, AT THE LID'S EDGE. CHALAZION: chronic, NON-painful, meibomian, generally NOT at the margin — POINTS INSIDE THE LID."),
   ("Sclera colour", "YELLOW → LIVER DISEASE. BLUE → OSTEOGENESIS IMPERFECTA."),
   ("Proptosis technique", "STAND BEHIND THE SEATED PATIENT AND LOOK DOWN FROM ABOVE, drawing the lid slightly up. Causes: retrobulbar haemorrhage, orbital cellulitis, orbital tumour, GRAVES."),
   ("Nasolacrimal duct test", "Look UP; press the lower lid near the MEDIAL CANTHUS just inside the bony rim; watch for regurgitation from the puncta. MUCOPURULENT FLUID = OBSTRUCTION. AVOID if significantly inflamed or tender."),
   ("Everting the upper lid", "Look DOWN and relax → raise the lid so lashes protrude → grasp and pull DOWN AND FORWARD → stick AT LEAST 1 cm ABOVE THE MARGIN at the upper tarsal border → push down as you raise the edge. DO NOT PRESS ON THE EYEBALL. NEVER EVERT IF GLOBE RUPTURE IS SUSPECTED."),
   ("Subconjunctival haemorrhage on exam", "PAIN ABSENT · VISION AND PUPIL UNAFFECTED · NO DISCHARGE · CORNEA CLEAR. GLOBE RUPTURE MORE LIKELY in trauma and when the haemorrhage ENCIRCLES THE ENTIRE CORNEA."),
   ("Injection pattern", "DIFFUSE, MAXIMAL PERIPHERALLY → conjunctivitis. JUST AROUND THE CORNEA → KERATITIS, IRITIS or ACUTE GLAUCOMA."),
 ]),
 ("l3-acuity", "Acuity, Fields & Motility", "#3a5a40", "#e3ece5", "#f1f5f2", "#2c452f", [
   ("OD / OS / OU", "OD = RIGHT eye. OS = LEFT eye. OU = BOTH. “Terms that you must remember.”"),
   ("20/200", "At 20 FEET the patient reads print a NORMAL eye reads at 200 FEET. THE LARGER THE SECOND NUMBER, THE WORSE THE VISION. Cannot read the chart → document COUNTING FINGERS, HAND MOTION, or LIGHT PERCEPTION."),
   ("PINHOLE TEST", "Admits only light PERPENDICULAR to the lens, so it need not be bent → CORRECTS ANY REFRACTIVE ERROR. NOT corrected → consider CATARACT, OPTIC NERVE DISEASE or RETINAL DISEASE."),
   ("Confrontation fields", "STATIC FINGER WIGGLE (arm's length, hands 2 ft apart lateral to the ears, into centre of view, each quadrant) PLUS KINETIC RED TARGET (5 mm red-topped pin inward from beyond each quadrant — ask when it FIRST APPEARS RED)."),
   ("Blind spot", "15 DEGREES TEMPORAL to the line of gaze. ENLARGED in GLAUCOMA, OPTIC NEURITIS and PAPILLOEDEMA. A temporal defect in one eye → TEST FOR A NASAL DEFECT IN THE OTHER."),
   ("Nystagmus", "A FEW BEATS ON LATERAL GAZE IS NORMAL. Bring the finger back into BINOCULAR vision — if it persists there, consider NEUROLOGIC disease."),
   ("Lid lag", "Rim of SCLERA VISIBLE ABOVE THE IRIS on DOWNWARD gaze. Most often HYPERTHYROIDISM."),
 ]),
 ("l3-pupils", "The Pupils", "#5f4a7d", "#e9e4f0", "#f4f1f8", "#493a60", [
   ("Anisocoria", "½ to 1 mm difference is COMMON and BENIGN IF THE REACTIONS ARE NORMAL. ABNORMAL: difference > 1 mm, or a POORLY REACTIVE pupil."),
   ("SWINGING LIGHT TEST", "Indication: ANISOCORIA. ABNORMAL = PARADOXICAL DILATION OF BOTH PUPILS when the light swings to the affected eye, WITH AN INTACT CONSENSUAL REFLEX = RELATIVE AFFERENT PUPILLARY DEFECT = MARCUS GUNN PUPIL = THE LESION IS THE OPTIC NERVE. Mechanism: reduced afferent input → reduced efferent output to BOTH pupils → net dilation."),
   ("ADIE'S TONIC", "LARGE, regular, usually UNILATERAL. Light reaction SEVERELY REDUCED/ABSENT. NEAR REACTION PRESENT BUT VERY SLOW. Degeneration of the CILIARY GANGLIA and POSTGANGLIONIC PARASYMPATHETIC fibres."),
   ("ARGYLL ROBERTSON", "SMALL, UNEQUAL, IRREGULAR. “ACCOMMODATES BUT DOESN'T REACT.” Classically TERTIARY SYPHILIS, today more often DIABETES; also LYME. Mydriatics dilate it only INCOMPLETELY."),
   ("HORNER SYNDROME", "PTOSIS · MIOSIS · ANHIDROSIS of the ipsilateral face. THE SMALL PUPIL STILL REACTS BRISKLY to light and near — that is what separates it. Sympathetic supply to pupil AND levator interrupted. CONGENITAL: involved iris is LIGHTER (heterochromia)."),
   ("CN III PALSY", "DILATED pupil FIXED to BOTH light and near, with PTOSIS and LATERAL DEVIATION almost always present."),
   ("Three causes of a dilated pupil", "Once local eye disease is excluded: (1) COMPRESSION/LESION OF CN III · (2) PARASYMPATHETIC DENERVATION from a ciliary ganglion lesion = ADIE'S · (3) PHARMACOLOGIC BLOCK of the sphincter."),
   ("Oblique lighting — crescent shadow", "Light from the TEMPORAL side. NO SHADOW = normal, flat iris, OPEN angle. A SHADOW on the MEDIAL side = iris BOWED FORWARD = NARROW ANGLE = raised risk of NARROW-ANGLE GLAUCOMA."),
   ("Corneal scar vs cataract", "SCAR: SUPERFICIAL greyish-white corneal opacity. CATARACT: DEEPER, visible ONLY THROUGH THE PUPIL."),
 ]),
 ("l3-fundus", "Fundoscopy & Trauma", "#7a4a2e", "#f0e7e1", "#f8f3f0", "#5f3922", [
   ("DO NOT DILATE if…", "SERIAL NEUROLOGIC EXAMS are required · ELDERLY PATIENTS WHO HAVE HAD CATARACT SURGERY · SUSPECTED ACUTE ANGLE-CLOSURE GLAUCOMA. If you dilate: DOCUMENT THE TIME AND THE AGENTS."),
   ("NORMAL fundus", "YELLOWISH-ORANGE TO CREAM · small disc vessels · SHARP disc margin · cup CENTRAL or slightly TEMPORAL, diameter LESS THAN HALF the disc."),
   ("PAPILLOEDEMA", "RAISED INTRACRANIAL PRESSURE. PINK, disc SWOLLEN with BLURRED MARGINS, CUP NOT VISIBLE, LOSS OF VESSEL PULSATIONS."),
   ("GLAUCOMATOUS CUPPING", "Cup ENLARGED, MORE THAN HALF the disc diameter; retinal vessels SINK IN AND AROUND the disc."),
   ("OPTIC ATROPHY", "WHITE disc, TINY DISC VESSELS ABSENT — death of optic nerve fibres. Seen in OPTIC NEURITIS, MULTIPLE SCLEROSIS, TEMPORAL ARTERITIS."),
   ("Trauma mechanics", "LARGER objects transfer most energy to the ORBITAL RIM; SMALLER objects may strike the GLOBE directly."),
   ("ORBITAL (BLOW-OUT) FRACTURE", "SUNKEN EYE · INFRAORBITAL HYPOAESTHESIA (infraorbital nerve) · DIPLOPIA PARTICULARLY ON UPWARD GAZE · decreased motility · sometimes IPSILATERAL NOSEBLEED. Look for ECCHYMOSIS, POINT TENDERNESS, PALPABLE STEP-OFF."),
   ("ZYGOMATIC FRACTURE", "FLATTENING OF THE MALAR EMINENCE, best seen from BEHIND the seated patient looking down. PAIN ON OPENING THE MOUTH because TEMPORALIS passes MEDIAL to the arch and inserts on the MANDIBLE."),
   ("HYPHAEMA", "Blood in the ANTERIOR CHAMBER from blunt trauma. Check ACUITY · PUPILS (crescent-like iris defect if torn) · RED REFLEX · INTRAOCULAR PRESSURE · SLIT LAMP."),
   ("CORNEAL ABRASION", "EVERT THE UPPER LID — a foreign body in the upper tarsal conjunctiva scratches with every blink. A HAZY CORNEA SUGGESTS BACTERIAL INFECTION. TOPICAL ANAESTHETIC IS FOR DIAGNOSIS, NOT TREATMENT."),
   ("CORNEAL ULCER", "HERPES SIMPLEX ULCERS ARE NOT VERY PAINFUL. Ophthalmoscope at +40 DIOPTRES may reveal it, but FLUORESCEIN IS MORE SENSITIVE for early ulcers. Fluorescein is taken up by cornea DEVOID OF EPITHELIUM."),
 ]),
]


def section(t):
    tid, title, acc, bg, zeb, ink, rows = t
    body = "\n".join(
        '          <tr><td class="h">%s</td><td>%s</td></tr>' % (H.escape(a), H.escape(b))
        for a, b in rows)
    return ('\n  <section class="topic" id="%s" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">\n'
            '    <div class="shead"><span class="dot" style="background:%s"></span><h2>%s</h2></div>\n'
            '    <div class="scroll">\n      <table>\n'
            '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
            '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n'
            % (tid, acc, bg, zeb, ink, acc, H.escape(title), body))


def main():
    s = open(CRAM, encoding="utf-8").read()
    for tid in [t[0] for t in TOPICS]:
        s = re.sub(r'\n  <section class="topic" id="%s".*?\n  </section>\n' % re.escape(tid),
                   "", s, flags=re.S)
        s = re.sub(r'      <a href="#%s"[^\n]*\n' % re.escape(tid), "", s)

    last = s.rindex('<section class="topic"')
    end = s.index("\n  </section>", last) + len("\n  </section>\n")
    links_anchor = s.rindex("</a>\n", 0, s.index("</nav>") if "</nav>" in s else len(s)) + len("</a>\n")
    links = "".join(
        '      <a href="#%s" style="color:%s"><span class="dot" style="background:%s"></span>%s</a>\n'
        % (t[0], t[5], t[2], t[1]) for t in TOPICS)
    s = s[:end] + "".join(section(t) for t in TOPICS) + s[end:]
    s = s[:links_anchor] + links + s[links_anchor:]

    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th", "div"):
        o, c = len(re.findall(r"<%s[ >]" % tag, s)), s.count("</%s>" % tag)
        assert o == c, "%s: %d open, %d close" % (tag, o, c)
    ids = set(re.findall(r'id="([^"]+)"', s))
    dangling = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a and a not in ids]
    assert not dangling, "dangling jump links: %r" % dangling
    assert "**" not in s, "markdown emphasis left in a cram row"

    open(CRAM, "w", encoding="utf-8").write(s)
    print("Lecture 3 cram topics added: %d sections, %d rows"
          % (len(TOPICS), sum(len(t[6]) for t in TOPICS)))


if __name__ == "__main__":
    main()
