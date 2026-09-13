#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Ocular Drug Reference for Pharmacology I Exam 2.

ONE PAGE RATHER THAN THREE. Exam 1 has separate Indications, Side Effects and
Contraindications charts. Exam 2 is a single 79-slide lecture, so splitting it
three ways would give three thin pages; the six-point frame from
[[pharmacology_exam_spec]] is carried per row instead.

WHAT DR. McINNIS SAID STUDENTS UNDER-STUDY drives the column order: indications,
patient education, side effects and contraindications come before mechanism,
because mechanism is the part that is already over-weighted.

THE TOP SECTION IS WHAT HE SAID HE WOULD ASK. The recording contains one
explicit promise -- rebound hyperaemia from topical vasoconstrictors -- and
several explicit de-scopings. Both are more useful the night before than any
individual row.

Uses _pharm_ref_shell.page() so it shares a stylesheet with the Exam 1
references and cannot drift from them.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _pharm_ref_shell import page

OUTDIR = os.path.join(ROOT, "Pharmacology I Exam 2")
DECK = "Ophthalmology-2.pptx"

# (group, agents, indication, education, side effects, contraindications/cautions, mechanism, slide)
ROWS = [
 ("Antibacterial", "Erythromycin (ointment)",
  "Superficial conjunctival or corneal infection; prophylaxis of ophthalmia neonatorum",
  "Soothing on an inflamed eye, so it may be used even when bacterial infection is not confirmed. Dirt cheap.",
  "Ocular irritation, hypersensitivity &mdash; shared by essentially every ophthalmic antibiotic",
  "None specific", "Blocks transpeptidation at the 50S ribosome", 15),
 ("Antibacterial", "Azithromycin (AzaSite)",
  "Bacterial conjunctivitis",
  "Given twice daily rather than four or more times &mdash; but considerably more expensive, so not used as often clinically.",
  "Ocular irritation, hypersensitivity",
  "Cost is the practical barrier", "Blocks transpeptidation at the 50S ribosome", 17),
 ("Antibacterial", "Ciprofloxacin (Ciloxan)",
  "Conjunctivitis, keratitis, corneal ulcers, blepharitis, dacryocystitis",
  "A WHITE PRECIPITATE appears in about 17% &mdash; specific to this agent, and worth warning about so it is not mistaken for worsening.",
  "Ocular irritation, white precipitate, unpleasant taste after instillation",
  "Emerging resistance; expensive", "Inhibits DNA gyrase and topoisomerase IV", 21),
 ("Antibacterial", "Moxifloxacin (Vigamox), ofloxacin, levofloxacin, gatifloxacin",
  "Conjunctivitis; corneal ulcers",
  "PREFERRED for corneal ulcers or suspected Pseudomonas, and for conjunctivitis in CONTACT LENS WEARERS once keratitis is excluded.",
  "Ocular irritation, unpleasant taste after instillation",
  "Expensive; emerging resistance", "Inhibits DNA gyrase and topoisomerase IV", 22),
 ("Antibacterial", "Gentamicin, tobramycin (Tobrex)",
  "Conjunctivitis and external infections of the eye and adnexa",
  "Watch for CORNEAL ULCERATION and reactive keratoconjunctivitis after several days of use &mdash; the one adverse effect specific enough to attach to a class.",
  "Ocular irritation, CORNEAL ULCERATION, reactive keratoconjunctivitis",
  "Prolonged use", "Binds the 30S ribosomal subunit", 23),
 ("Antibacterial", "Sulfacetamide sodium",
  "Bacterial conjunctivitis and other superficial ocular infection",
  "Ask about sulfa allergy before prescribing.",
  "Ocular irritation, allergic reactions",
  "AVOID in sulfonamide allergy", "Antagonises PABA to block folic acid synthesis", 19),
 ("Antibacterial", "Bacitracin (ointment)",
  "Bacterial conjunctivitis, blepharitis, keratitis, corneal ulcers, meibomianitis",
  "Inexpensive ointment for lid and surface disease.",
  "Ocular irritation", "None specific",
  "Blocks cell wall synthesis by preventing mucopeptide transfer", 20),
 ("Antibacterial", "Trimethoprim / polymyxin B (Polytrim)",
  "Bacterial conjunctivitis",
  "A combination of two different mechanisms in one drop.",
  "Ocular irritation", "None clinically",
  "Trimethoprim blocks reduction of folic acid to tetrahydrofolate; polymyxin B binds membrane phospholipids and lets contents leak", 18),
 ("Antiviral", "Trifluridine (Viroptic)",
  "Herpes simplex keratitis and keratoconjunctivitis",
  "The topical antiviral. Adenoviral conjunctivitis has NO antiviral &mdash; it is self-limited and treated symptomatically.",
  "Ocular irritation, PUNCTATE KERATOPATHY, hypersensitivity",
  "None specific",
  "Inhibits thymidylate synthetase and substitutes for thymidine in viral DNA", 27),
 ("Antiviral", "Ganciclovir (Zirgan)",
  "Herpetic keratitis; cytomegalovirus retinitis by intravitreal injection",
  "The other ophthalmic preparation alongside trifluridine.",
  "Ocular irritation, punctate keratitis", "None specific",
  "Competitively inhibits deoxyguanosine triphosphate binding to DNA polymerase", 28),
 ("Antiviral", "Acyclovir, valacyclovir, famciclovir",
  "Herpes zoster ophthalmicus; herpes simplex keratitis and iridocyclitis",
  "Oral or intravenous rather than topical.",
  "Systemic", "Renal dosing considerations", "Nucleoside analogues", 26),
 ("Antiviral", "Foscarnet, ganciclovir, valganciclovir, cidofovir",
  "Cytomegalovirus retinitis",
  "Intravenous, oral or intravitreal &mdash; specialty use cases.",
  "Systemic toxicity", "Specialty use", "Various antiviral mechanisms", 26),
 ("Antifungal", "Natamycin (Natacyn)",
  "Conjunctivitis and keratitis from Aspergillus, Candida, Cephalosporium, Fusarium, Penicillium",
  "THE ONLY commercially available ophthalmic antifungal. Everything else is compounded or systemic. Risk factors for ocular fungal infection: trauma, chronic ocular surface disease, contact lens wear, immunosuppression INCLUDING topical steroid use.",
  "Ocular irritation", "None specific",
  "Binds sterol, increasing fungal cell membrane permeability", 32),
 ("Allergy", "Ketotifen (Zaditor, OTC), olopatadine, azelastine, alcaftadine, bepotastine, emedastine, epinastine",
  "Ocular allergy",
  "Onset within MINUTES; allow two weeks to judge full efficacy. Typically PREFERRED over mast cell stabilisers.",
  "Ocular irritation, headache, INCREASED ocular dryness",
  "No significant interactions",
  "H1 INVERSE AGONISTS &mdash; they inactivate the receptor rather than simply blocking it, and remain competitive with histamine", 42),
 ("Allergy", "Cromolyn (Opticrom), lodoxamide (Alomide), nedocromil (Alocril)",
  "Predictable seasonal allergy in patients who cannot tolerate other therapy",
  "5 to 14 days for full efficacy and NOT useful for acute symptoms. Often four times daily, which is not ideal.",
  "Ocular irritation, unpleasant taste, headache", "None specific",
  "Inhibit mast cell degranulation, limiting histamine, tryptase and prostaglandin D2", 45),
 ("Allergy", "Tetrahydrozoline (Opti-Clear), naphazoline (VasoClear), naphazoline with pheniramine (Visine-A)",
  "Short-term relief of conjunctival redness and oedema",
  "&#9733; NO MORE THAN TWO WEEKS &mdash; prolonged use causes REBOUND HYPERAEMIA on stopping. If no improvement within 72 HOURS, stop and see a provider. The same trap appears with nasal sprays.",
  "REBOUND HYPERAEMIA after discontinuation",
  "Prolonged use; accidental ingestion in children",
  "Alpha-1 agonist LOCALLY; these imidazolines target alpha-2 SYSTEMICALLY, which is what makes an ingestion dangerous", 48),
 ("Inflammation", "Bromfenac, diclofenac, flurbiprofen, ketorolac, nepafenac",
  "Postoperative inflammation and pain; allergic conjunctivitis",
  "NOT routinely recommended for conjunctivitis.",
  "Lacrimation, keratitis, RAISED intraocular pressure, ocular irritation",
  "Caution where pressure matters",
  "Block cyclooxygenase, stopping conversion of arachidonic acid to prostaglandins and thromboxanes", 51),
 ("Inflammation", "Dexamethasone, prednisolone (Pred Forte), difluprednate",
  "Severe ocular allergy, anterior uveitis, external eye inflammatory disease, inflammation after ocular surgery",
  "Limited to a pulse of LESS THAN TWO WEEKS. Generally reserved for refractory symptoms.",
  "CATARACT formation, raised pressure and glaucoma, infection from reduced immune function, delayed wound healing, corneal ulcers",
  "Raised pressure is MORE LIKELY WITH A FAMILY HISTORY",
  "Inhibit phospholipase A2, cutting off arachidonic acid derived mediators; also inhibit fibrin and collagen deposition, reducing scarring", 52),
 ("Inflammation", "Fluorometholone (FML), loteprednol (Alrex), rimexolone (Vexol)",
  "As for the other ocular steroids",
  "The SOFT STEROIDS &mdash; lower risk of raising intraocular pressure.",
  "Same class risks, but less pressure elevation",
  "Same cautions, reduced", "As for the glucocorticoids", 55),
 ("Dry eye", "Cyclosporine (Restasis)",
  "Chronic dry eye with inflammation &mdash; keratoconjunctivitis sicca",
  "Treat the underlying disease first. Systemic causes: Sjogren syndrome, rheumatoid arthritis, vitamin A deficiency, Stevens-Johnson syndrome.",
  "OCULAR BURNING (17%), foreign body sensation, blurred vision",
  "None specific",
  "Inhibits production and release of interleukin 2, reducing T cell activation; raises tear production", 58),
 ("Glaucoma", "Latanoprost (Xalatan), travoprost, bimatoprost (Lumigan), tafluprost",
  "Open-angle glaucoma &mdash; FIRST LINE and the most commonly used",
  "ONCE DAILY and do not exceed it &mdash; more frequent dosing INHIBITS the pressure-lowering effect. Warn about lash and iris changes.",
  "Conjunctival hyperaemia, ocular irritation, CHANGES IN EYELASH LENGTH AND IRIS COLOUR",
  "Limited systemic side effects",
  "Prostaglandin F2 alpha analogues; increase aqueous OUTFLOW", 65),
 ("Glaucoma", "Timolol (Timoptic), carteolol, levobunolol &mdash; nonselective",
  "Open-angle glaucoma &mdash; second line",
  "Nonselective is MORE efficacious in the eye because beta-2 receptors predominate there &mdash; but that is also why it is worse tolerated.",
  "Worsening heart failure, BRADYCARDIA, heart block, INCREASED AIRWAY RESISTANCE",
  "Asthma, heart failure, bradyarrhythmia",
  "Block beta receptors in ciliary body epithelium; less cyclic AMP, less aqueous PRODUCTION", 67),
 ("Glaucoma", "Betaxolol (Betoptic-S) &mdash; beta-1 selective",
  "Open-angle glaucoma",
  "The selective option, so LESS risk of bronchoconstriction in a patient with asthma.",
  "As for the class, reduced respiratory risk",
  "Still cardiac caution",
  "Selective beta-1 blockade; reduces aqueous production", 68),
 ("Glaucoma", "Brimonidine (Alphagan P), apraclonidine (Iopidine)",
  "Open-angle glaucoma &mdash; the only class doing BOTH jobs",
  "Brimonidine is more lipophilic; apraclonidine is highly ionised at physiological pH. Allergic conjunctivitis is LESS common with brimonidine.",
  "Ocular irritation, hyperaemia (rebound effect), pruritus, allergic conjunctivitis",
  "CONTRAINDICATED IN CHILDREN UNDER TWO &mdash; central nervous system depression and apnoea",
  "Alpha-2 agonists; decrease production AND increase outflow", 69),
 ("Glaucoma", "Dorzolamide (Trusopt), brinzolamide (Azopt)",
  "Open-angle glaucoma",
  "Warn about the taste and the sting &mdash; both are common enough to cause people to stop.",
  "BITTER TASTE (25%), burning or stinging (33%), allergic conjunctivitis",
  "Sulfonamide-derived",
  "Inhibit carbonic anhydrase in ciliary body epithelium; less bicarbonate, less fluid transport", 70),
 ("Glaucoma", "Pilocarpine (Pilopine HS), carbachol (Miostat), acetylcholine (Miochol-E)",
  "Open-angle glaucoma; acetylcholine in surgical settings",
  "Poor compliance from side effects and frequent dosing. YOUNGER patients are usually intolerant because of the visual blurring.",
  "FIXED SMALL PUPILS, myopia, visual disturbance, headache",
  "Younger patients tolerate miotics poorly",
  "Activate muscarinic receptors; ciliary muscle contraction facilitates OUTFLOW", 72),
 ("Diagnostic", "Proparacaine (Alcaine), tetracaine (Altacaine)",
  "Tonometry, foreign body removal, superficial corneal surgery",
  "&#9733; DO NOT WRITE PRESCRIPTIONS FOR THESE. The eye stays numb 10 to 20 minutes with NO BLINK REFLEX.",
  "Hypersensitivity, burning sensation",
  "Never dispensed for home use",
  "Inhibit sodium influx into the neuron, preventing signal propagation", 75),
 ("Diagnostic", "Tropicamide (Mydriacyl), cyclopentolate (Cyclogyl), atropine",
  "Fundoscopic examination; uveitis, to prevent synechiae and relieve ciliary spasm",
  "Mydriasis. The pupil is LESS reactive to light than with a sympathomimetic.",
  "Photosensitivity, blurred vision",
  "Caution where dilation is unsafe",
  "Antimuscarinics &mdash; competitively block muscarinic acetylcholine receptors", 76),
 ("Diagnostic", "Phenylephrine (Neo-Synephrine)",
  "Mydriasis for examination",
  "The dilated pupil stays MORE REACTIVE TO LIGHT than with an antimuscarinic.",
  "Photosensitivity, conjunctival hyperaemia",
  "Caution in cardiovascular disease",
  "Adrenergic receptor agonist", 77),
 ("Diagnostic", "Fluorescein",
  "Anterior segment staining; disclosing corneal injury",
  "Reveals epithelial defects of the cornea and conjunctiva.",
  "Hypersensitivity, burning sensation", "None specific",
  "Stains epithelial defects", 78),
]

GROUPS = ["Antibacterial", "Antiviral", "Antifungal", "Allergy", "Inflammation",
          "Dry eye", "Glaucoma", "Diagnostic"]
COLOUR = {"Antibacterial": "#9c5230", "Antiviral": "#7a4a86", "Antifungal": "#2f6b5a",
          "Allergy": "#b8860b", "Inflammation": "#a8452f", "Dry eye": "#2f6f8a",
          "Glaucoma": "#3f6b2f", "Diagnostic": "#6b5a35"}


def esc(s):
    return s


def main():
    notes = (
        '<div class="note"><h3>&#9733; The one he said he would ask</h3>'
        '<p>In the recording, on the topical vasoconstrictors: <em>&ldquo;Most of you will '
        'probably forget this and we&rsquo;ll get it wrong on the test. But I will tell you, '
        '<strong>I will ask this question</strong> &hellip; there&rsquo;s <strong>rebound '
        'hyperemia</strong> &hellip; <strong>star that, underline it, highlight it</strong>. A lot '
        'of people still get it wrong every test. I don&rsquo;t know why because I tell you '
        'explicitly, that&rsquo;s what I&rsquo;m going to be asking about.&rdquo;</em></p>'
        '<p>So: <strong>no more than two weeks</strong>, because prolonged use causes rebound '
        'hyperaemia on stopping; and <strong>if no improvement in 72 hours</strong>, stop and see '
        'a provider. He noted the same trap returns with nasal sprays in ENT.</p></div>'
        '<div class="note"><h3>What he took OFF the table</h3><ul>'
        '<li><strong>Indications for the individual antibiotics</strong> &mdash; <em>&ldquo;don&rsquo;t '
        'worry so much about indications for use &hellip; a lot of them have a lot of '
        'crossover.&rdquo;</em> They are listed below for reference, not for memorising.</li>'
        '<li><strong>Formulations</strong> &mdash; <em>&ldquo;I don&rsquo;t care that you memorize '
        'that necessarily, with some exceptions.&rdquo;</em></li>'
        '<li><strong>Which agent causes irritation or hypersensitivity</strong> &mdash; '
        '<em>&ldquo;don&rsquo;t memorize which ones cause eye irritation or hypersensitivity. '
        'ANY of these can do that.&rdquo;</em> The effects worth attaching to one class are the '
        'aminoglycoside corneal ulceration, the ciprofloxacin white precipitate, and the '
        'fluoroquinolone taste.</li>'
        '<li><strong>The specific combination products</strong> &mdash; <em>&ldquo;I don&rsquo;t '
        'care that you memorize, but just know if I was to say, hey, patient&rsquo;s on this drug '
        'right now, what would be a helpful second line agent to add on?&rdquo;</em> So learn the '
        'principle: add a <strong>different mechanism</strong>, for synergy and fewer drops.</li>'
        '</ul></div>')

    body = []
    toc = []
    for g in GROUPS:
        rows = [r for r in ROWS if r[0] == g]
        if not rows:
            continue
        gid = "g-" + re.sub(r"[^a-z]+", "-", g.lower()).strip("-")
        toc.append('<a href="#%s" style="color:%s"><span class="dot" style="background:%s"></span>%s</a>'
                   % (gid, COLOUR[g], COLOUR[g], g))
        out = ['<section id="%s" style="--acc:%s"><div class="shead">'
               '<span class="dot" style="background:%s"></span><h2>%s</h2></div>'
               '<div class="scroll"><table><thead><tr>'
               '<th class="dn">Agent</th><th>Indication</th><th>Patient education</th>'
               '<th>Side effects</th><th>Contraindications &amp; cautions</th>'
               '<th>Mechanism</th><th class="sl">Slide</th></tr></thead><tbody>'
               % (gid, COLOUR[g], COLOUR[g], g)]
        for _g, agent, ind, edu, se, ci, mech, slide in rows:
            out.append('<tr><td class="dn">%s</td><td>%s</td><td>%s</td><td>%s</td>'
                       '<td>%s</td><td>%s</td><td class="sl">slide %d</td></tr>'
                       % (agent, ind, edu, se, ci, mech, slide))
        out.append("</tbody></table></div></section>")
        body.append("".join(out))

    html = page(
        title="Ocular Drug Reference &mdash; Pharmacology I Exam 2 (Class of 2028)",
        kicker="Pharmacology I &middot; Exam 2 &middot; Class of 2028",
        h1="Ocular Drug Reference",
        sub="Every agent in the ophthalmology lecture, with indication, patient education, side "
            "effects, contraindications and mechanism. %d entries, each citing its slide. "
            "Indication, education, side effects and contraindications come FIRST, because "
            "mechanism is the part already over-weighted." % len(ROWS),
        legend="", notes=notes, toc="".join(toc), body="".join(body),
        footer_note="Source: <em>%s</em> (Adam Wood, PharmD, DABAT), and the lecture recording "
                    "of 3 September 2026. No doses are given &mdash; Dr. Wood does not ask for "
                    "them." % DECK)
    p = os.path.join(OUTDIR, "pharm-exam-2-ocular-reference.html")
    open(p, "w", encoding="utf-8").write(html)

    # Guards: the promised item and every de-scoping must survive into the page.
    for needle, what in (("I will ask this question", "the explicit exam promise"),
                         ("rebound hyperaemia", "the rebound hyperaemia rule"),
                         ("72 hours", "the 72-hour review point"),
                         ("ANY of these can do that", "the adverse-effect de-scoping")):
        assert needle.lower() in html.lower(), "%s was dropped" % what
    assert not re.search(r"\b\d+\s*(?:mg|mcg|g)\b", " ".join(r[2] + r[3] for r in ROWS)), \
        "a dose reached the page, and Dr. Wood does not ask for doses"
    print("wrote %s (%d KB, %d agents across %d groups)"
          % (os.path.basename(p), len(html) // 1024, len(ROWS), len(GROUPS)))


if __name__ == "__main__":
    main()
