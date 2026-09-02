#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Lecture 14 (Ocular Trauma) to the CMS I Exam 2 cram sheet.

Additive, fenced and idempotent, like the Lecture 11/12 and 13 adders. The cram
sheet is the night-before sheet: reasoning stays in the guide, this carries only
what has to come back cold. Capitals mark the discriminator, matching house
style.

The first section is the four DO-NOT rules, because in trauma the thing that
changes the outcome is usually what you refrain from doing -- not dilating, not
removing the object, not ordering an MRI, not sending anaesthetic drops home.
"""
import io, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2",
                    "cms-exam-2-cram-sheet.html")
OPEN, CLOSE = "<!--CMSE2L14-CRAM-->", "<!--/CMSE2L14-CRAM-->"


def sec(sid, title, acc, bg, zebra, ink, rows, star=False):
    body = "\n".join(
        '          <tr><td class="h">%s</td><td>%s</td></tr>' % (a, b) for a, b in rows)
    return """
  <section class="topic" id="%s" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">
    <div class="shead"><span class="dot" style="background:%s"></span><h2>%s%s</h2></div>
    <div class="scroll">
      <table>
        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>
        <tbody>
%s
        </tbody>
      </table>
    </div>
  </section>
""" % (sid, acc, bg, zebra, ink, acc, "&#9733; " if star else "", title, body)


TRA, TRABG, TRAZ, TRAINK = "#94371f", "#f7ece8", "#fcf5f2", "#742a17"
FX,  FXBG,  FXZ,  FXINK  = "#7a5a2e", "#f4eee4", "#faf7f1", "#5f4522"

SECTIONS = "".join([

 sec("tra-rules", "THE FOUR DO-NOTs &mdash; BREAK ONE AND YOU MAKE IT WORSE", TRA, TRABG, TRAZ, TRAINK, [
  ("DO NOT remove a penetrating object", "It may be TAMPONADING the wound. Removal can extrude intraocular contents."),
  ("DO NOT order MRI", "CT ORBIT. A magnet moves a METALLIC fragment through the eye."),
  ("DO NOT dilate the eye", "NEVER, when ocular trauma is suspected. It costs you the pupil exam."),
  ("DO NOT send home topical anaesthetic", "Delays healing, MASKS worsening symptoms, can cause a CORNEAL ULCER."),
  ("ALWAYS", "ABCs FIRST. Then tetanus status for any metal or organic penetration."),
  ("Automatic CT without contrast", "Loss of consciousness, alcohol, confusion, TACHYPNOEA, apnoeic breathing, ANTICOAGULANTS, or eye penetration."),
  ("Epidemiology", "Leading cause of MONOCULAR BLINDNESS in YOUNG ADULT MEN in the US. Usually arrives with MAJOR BRAIN TRAUMA."),
 ], star=True),

 sec("tra-globe", "OPEN GLOBE", TRA, TRABG, TRAZ, TRAINK, [
  ("Definition", "FULL-THICKNESS defect in cornea and/or sclera. Compartments open to the outside."),
  ("THE SIGNS", "PUPIL DISTORTED TOWARD THE WOUND &middot; FLAT anterior chamber &middot; uveal tissue protruding &middot; massive haemorrhagic CHEMOSIS &middot; SOFT EYE &middot; deep lid laceration &middot; hyphema or vitreous haemorrhage."),
  ("Two forms", "FULL-THICKNESS EYE WALL LACERATION (sharp / high velocity) vs GLOBE RUPTURE (blunt)."),
  ("Globe rupture &mdash; where", "At a WEAK POINT: posterior to the EOM insertions (esp SUPERONASAL), OLD SURGICAL INCISIONS, LAMINA CRIBROSA."),
  ("Globe rupture &mdash; suspect when", "Blunt trauma + MASSIVE HAEMORRHAGIC CHEMOSIS or a SOFT EYE."),
  ("THE MOMENT you suspect it", "RIGID SHIELD taped over the eye + OPHTHO IMMEDIATELY + ANTIEMETIC + analgesia + tetanus. Then SURGICAL REPAIR."),
  ("Cut lens capsule", "Lens becomes HYDRATED, OEDEMATOUS, OPAQUE. LENSECTOMY required but often DEFERRED."),
  ("Posterior segment foreign body", "LEAVE IT ALONE at initial evaluation &mdash; going after it does more damage."),
 ], star=True),

 sec("tra-surface", "CORNEAL ABRASION &amp; FOREIGN BODY", TRA, TRABG, TRAZ, TRAINK, [
  ("Corneal abrasion &mdash; history", "FINGERNAIL or CONTACT LENS handling. One of the COMMONEST ocular injuries."),
  ("Corneal abrasion &mdash; symptoms", "SEVERE foreign body sensation, tearing, photophobia, blurred vision."),
  ("Corneal abrasion &mdash; diagnosis", "SLIT LAMP with FLUORESCEIN &mdash; stains the exposed BASEMENT MEMBRANE."),
  ("Corneal abrasion &mdash; treatment", "TOPICAL BROAD-SPECTRUM ANTIBACTERIAL. Patching may ease pain. Re-examine."),
  ("Foreign body &mdash; history", "GRINDING or STRIKING METAL."),
  ("THE LOCALISING SIGN", "LINEAR VERTICAL corneal defects = object in the TARSAL CONJUNCTIVA of the UPPER LID. EVERT THE LID."),
  ("Foreign body &mdash; removal", "Topical anaesthetic &rarr; slit lamp &rarr; STERILE 27-GAUGE NEEDLE. RUST RING (iron/copper) &rarr; battery BURR."),
  ("When to refer", "Any concern the object passed THROUGH the cornea &mdash; that is an OPEN GLOBE."),
 ]),

 sec("tra-hyphema", "HYPHEMA", TRA, TRABG, TRAZ, TRAINK, [
  ("What", "Blood in the ANTERIOR CHAMBER from injured vessels. Blunt or penetrating. CAN BE A SIGN OF OPEN GLOBE."),
  ("Symptoms", "Blurred vision, eye pain, photophobia."),
  ("Measure the pressure", "YES &mdash; UNLESS penetrating globe injury is suspected."),
  ("Whole goal of management", "PREVENT A REBLEED."),
  ("Management", "BED REST head elevated &middot; ANTIEMETICS &middot; ocular hypotensives &middot; topical or oral CORTICOSTEROIDS &middot; CYCLOPLEGIC drops (atropine, homatropine, scopolamine) &middot; ORAL AMINOCAPROIC ACID (antifibrinolytic, slows clot breakdown)."),
  ("THE TIMING FACT", "MOST REBLEEDING IS IN THE FIRST 72 HOURS. Secondary haemorrhage is what causes PERMANENT visual loss."),
  ("Avoid", "ASPIRIN and ANTIPLATELETS. Increased risk in SICKLE CELL DISEASE."),
  ("Raised pressure treated with", "Beta blockers, PILOCARPINE, ACETAZOLAMIDE, osmotic agents if needed."),
 ], star=True),

 sec("tra-lids", "LIDS, CONTUSION &amp; PERIORBITAL HAEMATOMA", TRA, TRABG, TRAZ, TRAINK, [
  ("Lid laceration &mdash; CONSULT OPHTHO IF", "LID MARGIN &middot; within 6&ndash;8 mm of the MEDIAL CANTHUS &middot; LACRIMAL duct or sac &middot; INNER lid surface &middot; associated PTOSIS &middot; TARSAL PLATE or LEVATOR."),
  ("Full-thickness lid laceration", "Comes with a corneal laceration or GLOBE RUPTURE in about TWO THIRDS of cases."),
  ("Partial-thickness", "Repair in the ED, ophtho follow-up in 2&ndash;3 days."),
  ("Medial third laceration", "May transect the CANALICULAR system &rarr; CHRONIC TEARING FOR LIFE if not repaired properly."),
  ("Facial lacerations", "May be left OPEN 24 HOURS before closure &mdash; the face is highly vascular."),
  ("ORBITAL CONTUSION", "Swelling WITHOUT haemorrhage. Held IN FRONT of the septum by the tarsal plate and septal margin &rarr; PRESEPTAL ecchymosis. Supportive to surgery. RULE OUT BRAIN TRAUMA."),
  ("PERIORBITAL HAEMATOMA", "Bleeding WITHIN the orbit. NOT ALWAYS TRAUMATIC &mdash; eye surgery, peribulbar injections, orbital VARICES, lymphangiomas/AVM, ANTICOAGULANTS, SICKLE CELL, orbital pseudotumour, idiopathic."),
  ("Periorbital haematoma &mdash; treatment", "CANTHOTOMY with CANTHOLYSIS &mdash; expose the lateral canthal tendon, cut its INFERIOR branch, let the blood out."),
 ]),

 sec("tra-detach", "RETINAL &amp; VITREOUS DETACHMENT &mdash; THE THREE TYPES", FX, FXBG, FXZ, FXINK, [
  ("Presentation (all)", "CURTAIN or shadow descending &middot; cloudy/smoky vision &middot; FLOATERS &middot; momentary FLASHES &middot; monocular field defect &middot; acuity drops when the MACULA goes."),
  ("Diagnosis &amp; timing", "History + DILATED EYE EXAM. Must be seen by ophtho WITHIN 24 HOURS."),
  ("RHEGMATOGENOUS", "MOST COMMON. FULL-THICKNESS BREAKS + vitreous traction + liquefied vitreous into the subretinal space. Preceded by POSTERIOR VITREOUS DETACHMENT. &rarr; SURGICAL."),
  ("Rhegmatogenous &mdash; brought forward by", "MYOPIA, CATARACT SURGERY, OCULAR TRAUMA."),
  ("TRACTION", "Most commonly PROLIFERATIVE DIABETIC RETINOPATHY. More LOCALISED and CONCAVE. &rarr; SURGICAL."),
  ("EXUDATIVE (serous)", "NO break, NO traction. Systemic vascular/inflammatory disease or INTRAOCULAR TUMOUR. &rarr; TREAT THE UNDERLYING CONDITION."),
  ("Acute management", "Ophtho STAT, pain control, antiemetics, HEAD OF BED 30&ndash;40 DEGREES."),
 ]),

 sec("tra-fracture", "ORBITAL FLOOR (BLOWOUT) FRACTURE", FX, FXBG, FXZ, FXINK, [
  ("Mechanism 1 &mdash; true blowout", "Blunt object raises ORBITAL PRESSURE, blowing out the FLOOR (most often) or MEDIAL WALL. Fist or ball."),
  ("Mechanism 2", "Force to the INFRAORBITAL RIM buckles the floor."),
  ("THE GAZE RULE", "DIPLOPIA ON UPWARD GAZE = INFERIOR RECTUS entrapment. DIPLOPIA ON LATERAL GAZE = MEDIAL RECTUS."),
  ("Other findings", "Periorbital ecchymosis, lid oedema, chemosis, subconjunctival haemorrhage, INFRAORBITAL NUMBNESS (infraorbital nerve), subcutaneous EMPHYSEMA, enophthalmos, proptosis."),
  ("Entrapment also gives", "SEVERE PAIN + AUTONOMIC disturbance: BRADYCARDIA and VOMITING on attempted eye movement."),
  ("THE PAEDIATRIC TRAP", "&ldquo;WHITE-EYED BLOWOUT&rdquo; &mdash; entrapment with NO orbital soft tissue signs at all. A quiet-looking eye does not exclude it."),
  ("Diagnosis", "CT of ORBITS and MIDFACE."),
  ("Management ladder", "No injury/entrapment &rarr; ICE + analgesia, review 2&ndash;3 days. Blood in MAXILLARY SINUS &rarr; ANTIBIOTICS. True blowout &rarr; OPHTHO (30% have a significant globe injury). ENTRAPMENT &rarr; FACIAL TRAUMA SURGEON STAT (muscle NECROSIS)."),
  ("WHY antibiotics for blood in the sinus", "PROPHYLACTIC, not treatment. The eye is STERILE; blood in the sinus means the sinus is DISRUPTED and now has a PORTAL OF ENTRY."),
  ("WHY the CT includes the MIDFACE", "To catch ADDITIONAL FRACTURES. Finding the orbital floor is not the same as excluding everything else."),
  ("Surgical timing", "Often DELAYED 1&ndash;2 WEEKS to let swelling settle. Already-damaged optic nerve is unlikely to improve and surgery may worsen it."),
 ], star=True),

 sec("tra-basilar", "BASILAR SKULL FRACTURE", FX, FXBG, FXZ, FXINK, [
  ("What", "LINEAR fracture of the skull base: CRIBRIFORM PLATE of ethmoid, orbital plate of FRONTAL, PETROUS/SQUAMOUS TEMPORAL, SPHENOID, OCCIPITAL."),
  ("The catch", "Trauma there often has NO SYMPTOMS of its own &mdash; you find it on INDIRECT SIGNS."),
  ("INDIRECT SIGNS", "RACCOON EYES &middot; BATTLE SIGN &middot; HAEMOTYMPANUM &middot; bleeding into middle ear or sphenoid sinus &middot; CSF LEAK with CLEAR or PINK RHINORRHOEA."),
  ("TWO BEDSIDE TESTS FOR CSF", "DEXTROSE STICK may be positive. Fluid on FILTER PAPER or the BEDSHEET shows a HALO / DOUBLE RING SIGN &mdash; INNER ring of BLOOD, OUTER ring of CSF."),
  ("HOW to do the halo test", "Hold a BEDSHEET, paper or tissue under the nostril, let the drip fall, and watch it DRY. Two rings appear. She called this &ldquo;very classic&rdquo; and a sign NOT TO MISS."),
  ("Diagnosis", "CT ORBITS &mdash; but the fracture is NOT ALWAYS EVIDENT."),
  ("Management", "CSF present &rarr; NEUROSURGERY CONSULT and ADMISSION. Otherwise admission depends on clinical condition, associated injuries, brain injury on CT."),
  ("Antibiotics for a CSF leak", "CONTROVERSIAL &mdash; risk of selecting RESISTANT organisms."),
 ], star=True),
])


def main():
    t = io.open(CRAM, encoding="utf-8").read()
    before = len(t)
    anchor = "\n  <footer>"
    fenced = OPEN + SECTIONS + CLOSE
    pat = re.compile(re.escape(OPEN) + ".*?" + re.escape(CLOSE), re.S)
    if pat.search(t):
        t = pat.sub(lambda _: fenced, t, count=1)
    else:
        assert t.count(anchor) == 1, "footer anchor not unique"
        t = t.replace(anchor, fenced + anchor)
    io.open(CRAM, "w", encoding="utf-8").write(t)
    print("cram %d -> %d bytes (+%d)" % (before, len(t), len(t) - before))

    blk = t[t.index(OPEN):t.index(CLOSE)]
    assert blk.count("<section") == blk.count("</section>") == 8, blk.count("<section")
    assert blk.count("<table>") == blk.count("</table>") == 8
    assert blk.count("<tr>") == blk.count("</tr>")
    assert t.index(CLOSE) < t.index("<footer>"), "block must sit above the footer"
    # the Lecture 13 block must still be there
    assert "<!--CMSE2L13-CRAM-->" in t, "Lecture 13 cram block lost"
    print("verified: 8 sections, %d rows, all above the footer, Lecture 13 intact"
          % blk.count('<td class="h">'))


if __name__ == "__main__":
    main()
