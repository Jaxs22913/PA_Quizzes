#!/usr/bin/env python3
"""Remove length bias from the Acute Vision Loss objective pool.

The compare-and-contrast objective produces ENUMERATIVE items -- the keyed
answer is the list the lecture actually gives, so it is naturally the longest
string on the page. Shortening it would delete the content being examined, so
the wrong choices are rewritten to carry comparable weight instead. Every
rewrite stays factually wrong for its own question and keeps its explanation
true.
"""
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))

EDITS = [
 # ---- pool A ----
 ("a", '["Vitreous traction on the retina"', '["Vitreous traction and shrinkage of the retina"'),
 ("a", '["Embolism from the carotid artery"', '["Embolism arising from the carotid artery or heart"'),
 ("a", '["Arteritic and non-arteritic", "Those are the anterior ischemic optic neuropathies."]',
       '["Arteritic and non-arteritic types", "Those are the anterior ischemic optic neuropathies."]'),
 ("a", '["Carotid and cardiac emboli", "Those cause amaurosis fugax and arterial occlusion."]',
       '["Carotid emboli, cardiac emboli and retinal vascular spasm", "Those cause amaurosis fugax and arterial occlusion."]'),
 ("a", '["Vitreous shrinkage and traction"', '["Vitreous shrinkage and traction on the retina"'),
 ("a", '["Sickle cell disease and Raynaud\'s"', '["Sickle cell disease, Raynaud\'s and valve disease"'),
 ("a", '["Myopia and vitreous shrinkage"', '["Myopia, trauma and vitreous shrinkage"'),
 ("a", '["Anterior uveitis and anticholinergics", "Those are angle-closure risks."],\n     ["Myopia and cataract surgery"',
       '["Anterior uveitis and systemic anticholinergic drugs", "Those are angle-closure risks."],\n     ["Myopia and cataract surgery"'),
 ("a", '["Transient, lasting under a minute"', '["Transient, lasting from a few seconds to under a minute"'),
 ("a", '["Coloured halos around lights", "Those belong to angle-closure glaucoma."],\n     ["A curtain across the field"',
       '["Coloured halos seen around bright lights", "Those belong to angle-closure glaucoma."],\n     ["A curtain across the field"'),
 ("a", '["Nausea, vomiting and coloured halos"', '["Severe eye pain, nausea, vomiting and coloured halos"'),
 ("a", '["Gradual and painless over years"', '["Gradual and painless, developing over years"'),
 ("a", '["Cotton wool spots and venous dilation"', '["Cotton wool spots, venous dilation and haemorrhage"'),
 ("a", '["Disc swelling with cotton wool spots"', '["Disc swelling with cotton wool spots and haemorrhage"'),
 ("a", '["Pale retina with a cherry-red spot"', '["Pale retinal swelling with a cherry-red spot at the fovea"'),
 ("a", '["A cherry-red spot at the fovea", "That is arterial occlusion."],\n     ["Optic nerve cupping", "That is chronic glaucoma."],\n     ["An elevated grey retina", "That is detachment."],\n     ["A hazy cornea"',
       '["A cherry-red spot at the fovea with retinal pallor", "That is arterial occlusion."],\n     ["Optic nerve cupping", "That is chronic glaucoma."],\n     ["An elevated grey retina", "That is detachment."],\n     ["A hazy cornea"'),
 # ---- pool B ----
 ("b", '["Carotid Doppler and echocardiogram", "Those look for an embolic source."],\n     ["Lumbar puncture and CT"',
       '["Carotid Doppler and echocardiography of the heart", "Those look for an embolic source."],\n     ["Lumbar puncture and CT"'),
 ("b", '["Tonometry and gonioscopy", "Those assess glaucoma."],\n     ["MRI and lumbar puncture"',
       '["Tonometry and gonioscopy of the anterior drainage angle", "Those assess glaucoma."],\n     ["MRI and lumbar puncture"'),
 ("b", '["It dissolves a retinal embolus"', '["It dissolves an embolus lodged in the retinal artery"'),
 ("b", '["To measure her intraocular pressure"', '["To measure the intraocular pressure in both eyes"'),
 ("b", '["Improvement only after steroids"', '["Improvement only after a long course of steroids"'),
 ("b", '["Risk depends on intraocular pressure"', '["Risk depends only on the intraocular pressure"'),
 ("b", '["Long-term high-dose corticosteroids"', '["A long-term high-dose oral corticosteroid course"'),
 ("b", '["Only glaucoma affects the disc"', '["Only glaucoma affects the appearance of the disc"'),
 ("b", '["The field is never partially affected"', '["The visual field is never partially affected"'),
 ("b", '["Loss of optic nerve axons"', '["Loss of the optic nerve axons"'),
 # ---- the one stem without an age ----
 ("a", 'q="A clinician reviews the profile of arteritic anterior ischemic optic neuropathy. Which age threshold does the lecture give?"',
       'q="A 74-year-old woman is being assessed for arteritic anterior ischemic optic neuropathy. Which age threshold does the lecture give?"'),
]

if __name__ == "__main__":
    paths = {"a": os.path.join(HERE, "cms_e2l3_pool_a.py"),
             "b": os.path.join(HERE, "cms_e2l3_pool_b.py")}
    text = {k: io.open(p, encoding="utf-8").read() for k, p in paths.items()}
    for i, (which, old, new) in enumerate(EDITS):
        n = text[which].count(old)
        if n != 1:
            sys.exit("edit %d matched %d times in pool %s: %.70s" % (i, n, which, old))
        text[which] = text[which].replace(old, new)
    for k, p in paths.items():
        io.open(p, "w", encoding="utf-8").write(text[k])
    print("applied %d edits" % len(EDITS))
