#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the CMS I Exam 2 Lecture 14 (Ocular Trauma) Arcade decks.

Two decks, split by how the material is actually revised: the eye itself, and
the bones around it. One deck per topic per the arcade content policy, and
every card is a SINGLE ATOMIC FACT -- Match and Sprint are unplayable when the
answer is a paragraph.

arcade.js keeps decks in a flat list AND in a separate class/exam grouping. A
deck in one but not the other is invisible in the app, so this asserts both.
Idempotent.
"""
import io, os

ARCADE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "arcade.js")
SHIELD = ('<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/>'
          '<path d="M9 12l2 2 4-4"/>')
BONE = ('<path d="M4 12h16"/><circle cx="6" cy="9" r="2.2"/><circle cx="6" cy="15" r="2.2"/>'
        '<circle cx="18" cy="9" r="2.2"/><circle cx="18" cy="15" r="2.2"/>')

DECKS = [
 dict(id="cms-ocular-trauma", name="Ocular Trauma", color="accent3", icon=SHIELD, cards=[
  ["What comes first in any trauma?", "Airway, breathing, circulation."],
  ["Leading cause of monocular blindness in young adult men in the US?", "Ocular trauma."],
  ["Which imaging for a suspected metallic intraocular foreign body?", "CT orbit. Never MRI."],
  ["Why never MRI with a metallic fragment?", "The magnetic field moves it through the eye."],
  ["What is done with a penetrating object in the eye?", "Leave it in place."],
  ["Why leave a penetrating object in place?", "It may be tamponading the wound; removal can extrude contents."],
  ["Which action is never taken when ocular trauma is suspected?", "Dilating the eye."],
  ["What must be confirmed after penetration with metal or organic material?", "Tetanus is up to date."],
  ["Which findings make CT without contrast automatic?", "Loss of consciousness, alcohol, confusion, tachypnoea, apnoea, anticoagulants, eye penetration."],
  ["Define open globe injury.", "A full-thickness defect in cornea and/or sclera."],
  ["Which way is the pupil distorted in an open globe?", "Toward the wound."],
  ["Name the signs of an open globe.", "Distorted pupil, flat chamber, uveal protrusion, chemosis, soft eye, deep lid laceration, intraocular blood."],
  ["Two forms of open globe injury?", "Full-thickness eye wall laceration, and globe rupture."],
  ["Which mechanism causes a full-thickness eye wall laceration?", "A sharp object or high-velocity projectile."],
  ["Which mechanism causes a globe rupture?", "Severe blunt force."],
  ["Where does the globe rupture?", "At weak points: behind the muscle insertions, old surgical incisions, the lamina cribrosa."],
  ["What is placed over a suspected open globe?", "A rigid protective shield."],
  ["Why give antiemetics in a suspected open globe?", "Vomiting raises intraocular pressure and can extrude contents."],
  ["What happens to a lens whose capsule is cut?", "It becomes hydrated, oedematous and opaque."],
  ["Is lensectomy done at the time of globe repair?", "Often deferred, to let hyphema and inflammation settle."],
  ["What is done with a posterior segment foreign body initially?", "Leave it alone."],
  ["What is a corneal abrasion?", "Scraped-away corneal epithelium."],
  ["Typical history for a corneal abrasion?", "A fingernail, or handling a contact lens."],
  ["How is a corneal abrasion diagnosed?", "Slit lamp with fluorescein."],
  ["What does fluorescein stain in an abrasion?", "The exposed basement membrane."],
  ["Treatment for a corneal abrasion?", "Topical broad-spectrum antibacterial; patching may ease pain."],
  ["Which drops are NEVER sent home?", "Topical anaesthetics."],
  ["Why are take-home anaesthetic drops forbidden?", "They delay healing, mask worsening symptoms and can cause a corneal ulcer."],
  ["Typical history for a corneal foreign body?", "Grinding or striking metal."],
  ["What do vertical linear corneal defects indicate?", "A foreign body under the upper lid."],
  ["How is a corneal foreign body removed?", "Sterile 27-gauge needle after topical anaesthetic."],
  ["How is a rust ring removed?", "A battery-operated drill with a burr tip."],
  ["What forms a rust ring?", "Iron or copper."],
  ["What is a hyphema?", "Blood in the anterior chamber."],
  ["What else can a hyphema indicate?", "An open globe."],
  ["Goal of hyphema management?", "Preventing a rebleed."],
  ["Name the elements of hyphema management.", "Bed rest head-up, antiemetics, ocular hypotensives, corticosteroids, cycloplegics, aminocaproic acid."],
  ["What does aminocaproic acid do?", "Slows clot breakdown, reducing rebleeding."],
  ["When does most rebleeding after hyphema occur?", "In the first 72 hours."],
  ["Which drugs are avoided in hyphema?", "Aspirin and antiplatelets."],
  ["Which disease raises the risk of hyphema complications?", "Sickle cell disease."],
  ["When is intraocular pressure NOT measured?", "When a penetrating globe injury is suspected."],
  ["Which lid lacerations need ophthalmology?", "Margin, within 6-8 mm of the medial canthus, lacrimal duct or sac, inner surface, ptosis, tarsal plate or levator."],
  ["What share of full-thickness lid lacerations have a globe injury?", "About two thirds."],
  ["What follows an unrepaired canalicular injury?", "Chronic tearing."],
  ["Why may a facial laceration be left open 24 hours?", "The face is highly vascular."],
  ["What is an orbital contusion?", "Soft tissue swelling within the orbit without haemorrhage."],
  ["What keeps contusion blood in front of the eye?", "The tarsal plate and septal margin."],
  ["What is a periorbital haematoma?", "Bleeding within the bony orbit."],
  ["How is a periorbital haematoma treated?", "Canthotomy with cantholysis."],
  ["Name non-traumatic causes of periorbital haematoma.", "Eye surgery, peribulbar injections, orbital varices, malformations, anticoagulants, sickle cell, pseudotumour."],
  ["Three types of retinal detachment?", "Rhegmatogenous, traction, exudative."],
  ["Which retinal detachment is most common?", "Rhegmatogenous."],
  ["What precedes a rhegmatogenous detachment?", "Posterior vitreous detachment."],
  ["What causes a traction retinal detachment?", "Proliferative diabetic retinopathy."],
  ["What shape is a traction detachment?", "Localised and concave."],
  ["Which detachment has no break and no traction?", "Exudative."],
  ["How is an exudative detachment managed?", "Treat the underlying condition."],
  ["Symptoms of retinal detachment?", "Curtain or shadow, cloudy or smoky vision, floaters, flashes, monocular field defect."],
  ["How soon must a retinal detachment be seen?", "Within 24 hours."],
  ["Position for a patient awaiting detachment repair?", "Head of bed at 30 to 40 degrees."],
 ]),
 dict(id="cms-orbital-fractures", name="Orbital &amp; Skull Fractures", color="accent2", icon=BONE, cards=[
  ["Two mechanisms of an orbital floor fracture?", "True blowout from raised orbital pressure, or buckling from force on the infraorbital rim."],
  ["Which orbital wall blows out most often?", "The floor."],
  ["Which other wall commonly blows out?", "The medial wall."],
  ["Diplopia on UPWARD gaze means what?", "Inferior rectus entrapment."],
  ["Diplopia on LATERAL gaze means what?", "Medial rectus entrapment."],
  ["Which nerve injury causes cheek numbness after orbital fracture?", "The infraorbital nerve."],
  ["What is a white-eyed blowout?", "Entrapment in a child with no orbital soft tissue signs."],
  ["Which autonomic signs accompany entrapment?", "Bradycardia and vomiting on attempted eye movement."],
  ["Imaging for a suspected orbital fracture?", "CT of the orbits and midface."],
  ["Management with no injury or entrapment?", "Ice and analgesia, review in 2 to 3 days."],
  ["What does blood in the maxillary sinus add?", "Antibiotics."],
  ["Why consult ophthalmology for a true blowout?", "About 30% have a significant globe injury."],
  ["Who is called for muscle entrapment, and why?", "A facial trauma surgeon urgently, because the muscle can necrose."],
  ["Why delay orbital fracture surgery 1 to 2 weeks?", "To let swelling settle, lowering intraorbital pressure during surgery."],
  ["What is expected if the optic nerve was damaged at injury?", "It is unlikely to improve, and surgery may worsen it."],
  ["What is a basilar skull fracture?", "A linear fracture of the skull base."],
  ["Which bones make up the skull base here?", "Ethmoid cribriform plate, frontal orbital plate, temporal, sphenoid, occipital."],
  ["Why is a basilar skull fracture often silent?", "Trauma there frequently produces no symptoms of its own."],
  ["Name the indirect signs of a basilar skull fracture.", "Raccoon eyes, Battle sign, haemotympanum, CSF leak, bleeding into the middle ear or sphenoid sinus."],
  ["What is Battle sign?", "Retroauricular ecchymosis over the mastoid."],
  ["What are raccoon eyes?", "Periorbital ecchymosis without direct orbital trauma."],
  ["What is haemotympanum?", "Blood behind the tympanic membrane."],
  ["Which bedside test may be positive with CSF?", "A dextrose stick."],
  ["What is the halo or double ring sign?", "Inner ring of blood, outer ring of cerebrospinal fluid, on filter paper or a bedsheet."],
  ["Imaging for a basilar skull fracture?", "CT orbits, though the fracture is not always evident."],
  ["What does a CSF leak require?", "Neurosurgery consult and admission."],
  ["Why are antibiotics for a CSF leak controversial?", "They risk selecting resistant organisms."],
 ]),
]


def card_js(c):
    q, a = (x.replace("\\", "\\\\").replace('"', '\\"') for x in c)
    return '      ["%s", "%s"],' % (q, a)


def deck_js(d):
    return ('  { id: "%s", name: "%s", color: "%s",\n'
            "    icon: '%s',\n"
            "    cards: [\n%s\n    ]},\n\n") % (
        d["id"], d["name"], d["color"], d["icon"],
        "\n".join(card_js(c) for c in d["cards"]))


def main():
    t = io.open(ARCADE, encoding="utf-8").read()
    before = len(t)

    anchor = '  { id: "cms-ophthalmology-1",'
    assert t.count(anchor) == 1
    for d in DECKS:
        if '{ id: "%s",' % d["id"] in t:
            continue
        t = t.replace(anchor, deck_js(d) + anchor)

    old_group = ('    { id: "exam2", name: "Exam 2", deckIds: [\n'
                 '      "cms-ophthalmology-1", "cms-neuro-ophthalmology", "cms-acute-vision-loss",\n'
                 '      "cms-chronic-vision-loss", "cms-cataract", "cms-ocular-tumors"\n'
                 '    ] }')
    new_group = ('    { id: "exam2", name: "Exam 2", deckIds: [\n'
                 '      "cms-ophthalmology-1", "cms-neuro-ophthalmology", "cms-acute-vision-loss",\n'
                 '      "cms-chronic-vision-loss", "cms-cataract", "cms-ocular-tumors",\n'
                 '      "cms-ocular-trauma", "cms-orbital-fractures"\n'
                 '    ] }')
    if new_group not in t:
        assert t.count(old_group) == 1, "CMS Exam 2 grouping not found as expected"
        t = t.replace(old_group, new_group, 1)

    io.open(ARCADE, "w", encoding="utf-8").write(t)
    print("arcade.js %d -> %d bytes (+%d)" % (before, len(t), len(t) - before))

    cms = t[t.index('id: "cms-1"'):] if 'id: "cms-1"' in t else t
    for d in DECKS:
        assert '{ id: "%s",' % d["id"] in t, "%s missing from the flat deck list" % d["id"]
        assert '"%s"' % d["id"] in t, "%s missing from the CMS exam grouping" % d["id"]
        print("  %-24s %3d cards, in both the list and the grouping" % (d["id"], len(d["cards"])))


if __name__ == "__main__":
    main()
