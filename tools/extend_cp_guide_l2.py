#!/usr/bin/env python3
"""Add the Dermatology section (Lecture 2) to the Clinical Pathophysiology I guide.

EXTENDS the existing Exam 1 guide rather than creating a second one -- there is
one guide and one cram sheet per exam, and each new lecture adds a section.

Objectives are reproduced verbatim from the SYLLABUS, which differs slightly
from the wording on the lecture's own objectives slide: the syllabus says
"molecular mechanisms of common dermatological conditions" where the slide says
"molecular mechanism of common dermatological skin conditions". The syllabus is
authoritative.

Scope note: this material is also taught in Clinical Medicine and Surgery I this
term. Everything here stays on mechanism -- what is happening in the tissue and
why. Diagnosis and management belong to the other course.
"""
import os, re

G = "/Users/jaxonluke/Developer/PA_Quizzes/Clinical Pathophysiology I Exam 1/cp-exam-1-study-guide.html"
I = "cp-exam-1-study-guide-images"

FIG_SKIN = ('<figure class="fig"><img width="800" height="558" loading="lazy" src="%s/010.jpg" '
 'alt="Labelled three-dimensional block diagram of full-thickness skin showing epidermis, papillary and reticular dermis, '
 'and hypodermis, with hair shaft and follicle, sebaceous gland, eccrine sweat gland, arrector pili muscle, '
 'Meissner\'s and Pacinian corpuscles, free nerve endings, artery and vein.">'
 '<figcaption>The whole of objective (a) in one block. Read it top to bottom: epidermis, then the dermis split into '
 'papillary above and reticular below, then hypodermis. Nearly everything that matters for the rest of this section is '
 'visible here &mdash; the appendages that produce sebum and sweat, the two named mechanoreceptors, and the vessels that '
 'sit in the dermis rather than the epidermis. That last point carries a lot of weight later: the epidermis has no blood '
 'supply of its own, which is why a lesion confined above the dermal-epidermal junction cannot bleed and cannot scar. '
 '<span class="src">&copy; 2004 Pearson Education, Inc., publishing as Benjamin Cummings. Reproduced from the lecture '
 'slides (Slide 5).</span></figcaption></figure>\n  ') % I

FIG_EPI = ('<figure class="fig"><img width="332" height="329" loading="lazy" src="%s/011.png" '
 'alt="Labelled cross-section of the epidermis showing, from deep to superficial, stratum basale, stratum spinosum, '
 'stratum granulosum, stratum lucidum and stratum corneum.">'
 '<figcaption>The five strata in order, and the order is the point: cells are born at the bottom and are dead by the '
 'top. Division happens only in the basale; the spinosum is where desmosomes give the prickle-cell appearance; the '
 'granulosum holds the keratohyalin granules; and the corneum is 20 to 30 layers of dead keratinocytes cemented into '
 'the barrier. Psoriasis is easier to remember against this picture &mdash; it is the loss of the granular layer that '
 'leaves the scale. <span class="src">Reproduced from the lecture slides (Slide 9).</span></figcaption></figure>\n  ') % I

TOC_ADD = '''  <a class="top-link" href="#dermatology">2 &middot; Dermatology</a>
  <a href="#derm-anatomy">2.1 Objective a &mdash; Anatomy of the integument</a>
  <a href="#derm-primary">2.2 Objective b &mdash; Primary skin lesions</a>
  <a href="#derm-secondary">2.3 Objective c &mdash; Secondary skin lesions</a>
  <a href="#derm-healing">2.4 Objective c &mdash; Wound healing &amp; scar</a>
  <a href="#derm-conditions">2.5 Objective d &mdash; Molecular mechanisms</a>
  <a href="#derm-cancers">2.6 Objective d &mdash; Skin cancers</a>
'''

SECTION = '''
<section class="deck" id="dermatology">
  <h2 class="deck-title">2 &middot; Dermatology: Pathophysiology of the Skin</h2>
  <p class="lecturer">Stacie Gopal, DMS, PA-C</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol type="a">
      <li>Review the anatomy of the integumentary system, including the different strata of the integument</li>
      <li>Compare and contrast pathophysiology of common primary skin lesions</li>
      <li>Compare and contrast pathophysiology of common secondary skin lesions</li>
      <li>Describe the molecular mechanisms of common dermatological conditions</li>
    </ol>
  </div>

  <div class="callout"><strong>The line between this course and Clinical Medicine and Surgery I.</strong>
  Dermatology is taught in both this term, and the same diseases appear in each. The split is
  that this course asks <em>what is happening in the tissue and why</em> &mdash; which cell, which
  pathway, which layer &mdash; while Clinical Medicine and Surgery I asks how you recognise it and
  what you do about it. If a fact would sit equally well in both, it is probably pitched for the
  other one.</div>

  <h3 class="sub" id="derm-anatomy">2.1 &middot; Objective a &mdash; Anatomy of the integumentary system</h3>
  <p>Skin is the largest organ in the body, with hair, nails and glands as accessory structures.
  Its functions are a physical barrier against pathogens, ultraviolet light, fluid loss and trauma;
  thermoregulation; sensation; and an endocrine role.</p>
  <div class="pearl"><strong>The vitamin D chain crosses three organs.</strong> Cholecalciferol
  (vitamin D3) is produced <em>in the skin</em> under ultraviolet B light, then hydroxylated first
  <em>in the liver</em> and then <em>in the kidneys</em> to the active form calcitriol. The skin
  only starts the process.</div>
  ''' + FIG_SKIN + '''
  <p>Three layers: <strong>epidermis</strong>, <strong>dermis</strong> and
  <strong>subcutaneous (hypodermis)</strong>. The dermis is where the nerves and vasculature sit.</p>
  <h4 class="subsub">The epidermis</h4>
  <p>Stratified squamous epithelium, 0.05 to 1.5 mm, with four cell types &mdash;
  <strong>keratinocytes (about 90%)</strong>, melanocytes, Merkel cells and Langerhans cells.
  Turnover is every 30 to 60 days and is more rapid in younger patients.</p>
  ''' + FIG_EPI + '''
  <table>
    <tr><th>Stratum</th><th>What defines it</th></tr>
    <tr><td>Basale (deepest)</td><td>Single layer of rapidly dividing columnar keratinocytes &mdash; <strong>the site of cell division</strong>. Contains melanocytes and Merkel cells (light touch)</td></tr>
    <tr><td>Spinosum</td><td>8&ndash;10 layers joined by <strong>desmosomes</strong>, giving the prickle-cell appearance. Contains dendritic and Langerhans cells, the immune sentinels</td></tr>
    <tr><td>Granulosum</td><td>3&ndash;5 layers of diamond-shaped cells containing keratohyalin granules</td></tr>
    <tr><td>Lucidum</td><td>2&ndash;3 layers of flattened dead keratinocytes with clear protein and lipids</td></tr>
    <tr><td>Corneum (outermost)</td><td>20&ndash;30 layers of keratin and dead keratinocytes, packed and cemented into a <strong>semi-impermeable barrier</strong></td></tr>
  </table>
  <h4 class="subsub">The dermis and the appendages</h4>
  <p>Two connective tissue layers: <strong>papillary</strong> (thin, superficial) and
  <strong>reticular</strong> (dense, deeper). <strong>Collagen</strong> is the primary component,
  produced by fibroblasts, giving tensile strength; <strong>elastic fibres</strong> of elastin and
  fibrillin give recoil. Cells include fibroblasts, macrophages, histiocytes, adipocytes and
  <strong>mast cells</strong>, which mediate immunoglobulin E-driven inflammation.</p>
  <table>
    <tr><th>Appendage</th><th>Secretion and function</th></tr>
    <tr><td>Eccrine sweat glands</td><td>Open onto the skin surface; water and electrolytes (sodium, chloride); cooling by evaporation</td></tr>
    <tr><td>Apocrine sweat glands</td><td>Axilla and anogenital areas; protein and fatty lipids; scent glands. <strong>Apocrine sweat + bacterial degradation = body odour</strong></td></tr>
    <tr><td>Sebaceous glands</td><td>Sebum &mdash; triglycerides, wax esters, squalene &mdash; lubricating skin and hair</td></tr>
  </table>
  <p>Hair comes in three types: <strong>terminal</strong> (thick, androgen-regulated),
  <strong>lanugo</strong> (fine, newborn) and <strong>vellus</strong> (fine, short, growth
  independent of androgens).</p>
  <button class="test-yourself-btn" style="--acc:#6a4fa3" onclick="window.openTestYourself('Test yourself &mdash; Integumentary anatomy', TEST_YOURSELF.dermAnatomy)">Test yourself! &rarr;</button>

  <h3 class="sub" id="derm-primary">2.2 &middot; Objective b &mdash; Primary skin lesions</h3>
  <p>A <strong>primary</strong> lesion is the direct result of the underlying disease and retains
  its original, unmodified appearance. Read the table by mechanism rather than by name &mdash; the
  size cut-offs are arbitrary, but what is happening in the tissue is not.</p>
  <table>
    <tr><th>Lesion</th><th>Size</th><th>What is happening in the tissue</th></tr>
    <tr><td>Macule</td><td>&le; 5 mm</td><td rowspan="2">Flat, circumscribed discoloration, <strong>NOT palpable</strong>. Hyperpigmented from increased melanin in the basal layer; hypopigmented from <em>loss of melanocytes</em> (vitiligo)</td></tr>
    <tr><td>Patch</td><td>&gt; 5 mm</td></tr>
    <tr><td>Papule</td><td>&lt; 5 mm</td><td>Epidermal hyperplasia with hyperkeratosis, plus inflammation and dense collagen in the dermis</td></tr>
    <tr><td>Nodule</td><td>&gt; 5 mm</td><td>Dermal-based, dense collagen bundles, extending into subcutaneous tissue</td></tr>
    <tr><td>Plaque</td><td>&gt; 1 cm</td><td>Confluence of papules, with marked epidermal thickening and dilated dermal vessels</td></tr>
    <tr><td>Vesicle</td><td>&le; 5 mm</td><td>Fluid with inflammatory cells collecting <em>within or directly beneath</em> the epidermis</td></tr>
    <tr><td>Bulla</td><td>&gt; 5 mm</td><td><strong>Separation of epidermis from dermis</strong> with fluid accumulation &mdash; a deeper plane of cleavage, not just a bigger vesicle</td></tr>
    <tr><td>Wheal</td><td>transient</td><td>Mast cells release histamine &rarr; vasodilation and vascular permeability &rarr; plasma leaks into dermis; histamine also acts on cutaneous nerve endings to cause pruritus</td></tr>
    <tr><td>Pustule</td><td>&le; 1 cm</td><td>Purulent material &mdash; leukocytes, debris, serous fluid, possibly organisms. Usually Gram-positive (<em>Staphylococcus aureus</em>, <em>Streptococcus pyogenes</em>); <strong>may be sterile</strong>, as in rosacea</td></tr>
    <tr><td>Cyst</td><td>&mdash;</td><td>Encapsulated, in dermis or subcutis. Epidermal inclusion cyst arises from a hair follicle and contains keratin</td></tr>
    <tr><td>Tumor</td><td>&gt; 2 cm</td><td>General term for rapid cellular growth, benign or malignant. Dermatofibroma is benign fibrous overgrowth; lipoma is an enclosed capsule of adipocytes</td></tr>
  </table>
  <div class="pearl"><strong>One discriminator does most of the work:</strong> macules and patches
  are <em>not</em> palpable; papules, nodules and plaques are. Everything else follows from depth
  and content.</div>

  <h3 class="sub" id="derm-secondary">2.3 &middot; Objective c &mdash; Secondary skin lesions</h3>
  <p>A <strong>secondary</strong> lesion is a primary lesion modified over time by infection,
  trauma or other factors, and it may or may not still resemble what it came from.</p>
  <table>
    <tr><th>Lesion</th><th>What is happening in the tissue</th></tr>
    <tr><td>Scale</td><td>Compact portion of desquamating stratum corneum (psoriasis)</td></tr>
    <tr><td>Crust</td><td>Dried sebum, cellular debris, blood or necrotic skin (impetigo)</td></tr>
    <tr><td>Lichenification</td><td>Thickened epidermis from long-term scratching &mdash; the <strong>itch-scratch cycle</strong>. Hyperplasia and hyperkeratosis; thick plaques <em>without</em> scaling (lichen simplex chronicus)</td></tr>
    <tr><td>Erosion</td><td>Focal loss of epidermis that <strong>does not penetrate below the dermal-epidermal junction</strong></td></tr>
    <tr><td>Ulcer</td><td>Focal loss of epidermis <strong>and dermis</strong>, with destruction of collagen and infiltration of inflammatory cells</td></tr>
    <tr><td>Fissure</td><td>Linear ulcer forming a crack, from loss of elasticity, severe dryness and mechanical tension, with hyperkeratosis</td></tr>
    <tr><td>Atrophy</td><td>Thinning: keratinocyte division slows, collagen synthesis slows, elastin degrades</td></tr>
  </table>
  <div class="callout"><strong>Why an ulcer scars and an erosion does not.</strong> The dermal-epidermal
  junction is the boundary. An erosion stays above it, so the dermis and its collagen are untouched
  and there is nothing to repair with scar. An ulcer crosses it and destroys collagen, so healing
  has to lay down new collagen &mdash; and that is what a scar is.</div>

  <h3 class="sub" id="derm-healing">2.4 &middot; Objective c &mdash; Wound healing and scar</h3>
  <table>
    <tr><th>Phase</th><th>Days</th><th>What happens</th></tr>
    <tr><td>Inflammatory</td><td>1&ndash;3</td><td>Fibrin haemostatic plug; neutrophils and macrophages remove dead tissue; growth factors and cytokines signal the next phase to begin</td></tr>
    <tr><td>Proliferative</td><td>4&ndash;21</td><td><strong>Granulation tissue</strong> forms &mdash; macrophages, fibroblasts and endothelial cells</td></tr>
    <tr><td>Remodelling</td><td>21 &ndash; 1 year</td><td>Granulation tissue formation ceases. <strong>Type III collagen is replaced with stronger type I</strong>, oriented in small parallel bundles &mdash; where normal dermis has a basket-weave orientation</td></tr>
  </table>
  <p>The lecture marks remodelling as the important phase, and the collagen swap is why: the scar
  ends up strong but architecturally different from the skin around it, which is why it never quite
  matches.</p>
  <div class="pearl"><strong>Hypertrophic scars and keloids are two failures, not one.</strong>
  Fibroblast dysregulation <em>prolongs the proliferative phase</em>, and deposition and degradation
  become imbalanced <em>during remodelling</em>. Collagen bundles then develop haphazardly and
  <strong>exceed the boundaries of the initial wound</strong> &mdash; which is the defining
  feature.</div>

  <h3 class="sub" id="derm-conditions">2.5 &middot; Objective d &mdash; Molecular mechanisms of common conditions</h3>
  <table>
    <tr><th>Condition</th><th>Mechanism</th></tr>
    <tr><td>Petechiae / purpura / ecchymoses</td><td>Bleeding into the dermis from capillary rupture, infection, thrombocytopenia or vasculitis. Same pathology at three sizes: &le;1&ndash;2 mm, 3&ndash;10 mm, &gt;10 mm. Non-blanchable. Henoch-Schonlein purpura is an immunoglobulin A vasculitis of skin, joints, kidneys and intestines, commonly aged 3&ndash;10</td></tr>
    <tr><td>Telangiectasia</td><td>Permanent dilatation and thinning of endothelium of superficial dermal vessels, <strong>with no inflammatory cell infiltration</strong></td></tr>
    <tr><td>Urticaria</td><td>Mast cell degranulation releasing histamine, forming wheals</td></tr>
    <tr><td>Allergic contact dermatitis</td><td><strong>Delayed hypersensitivity, 48&ndash;72 hours.</strong> <em>Sensitization</em>: Langerhans cells present haptens to T cells, creating memory. <em>Elicitation</em>: re-exposure promotes T cell migration and cutaneous inflammation (nickel, poison ivy)</td></tr>
    <tr><td>Irritant contact dermatitis</td><td>Direct cutaneous interaction with a chemical, biologic or physical agent &mdash; <strong>does not require prior exposure</strong></td></tr>
    <tr><td>Eczema (atopic dermatitis)</td><td>T cell-mediated. Overactive immune system plus <strong>insufficient filaggrin</strong> from a compromised epidermal barrier, with genetic, environmental and psychogenic factors. &ldquo;The itch that rashes&rdquo;</td></tr>
    <tr><td>Neurodermatitis</td><td>Cause unknown; nerve hypersensitivity suspected. Itch-scratch cycle producing thick, leathery, scaly plaques</td></tr>
    <tr><td>Seborrhoeic dermatitis</td><td>Cause incompletely understood. Microbiome dysbiosis, altered immune response and barrier dysfunction, in sebaceous-rich regions. Dandruff is the non-inflammatory form</td></tr>
    <tr><td>Seborrhoeic keratosis</td><td><strong>Benign</strong> proliferation of immature keratinocytes; possibly activating mutations in <strong>fibroblast growth factor receptor-3</strong></td></tr>
    <tr><td>Actinic keratosis</td><td>Cumulative ultraviolet damage &rarr; intraepidermal proliferation of <strong>dysplastic</strong> keratinocytes. The most common precancer; higher risk for squamous cell carcinoma</td></tr>
    <tr><td>Psoriasis</td><td>Chronic autoimmune inflammatory dermatosis; cells multiply up to <strong>10&times;</strong> faster. Active T cells infiltrate the epidermis and stimulate keratinocyte proliferation with <strong>tumour necrosis factor alpha, interferon gamma and interleukin-12</strong>. Epidermal hyperplasia, <strong>loss of the stratum granulosum</strong>, and failure to secrete lipids (xeroderma)</td></tr>
    <tr><td>Verrucae vulgaris</td><td>Human papillomavirus invades epidermal <strong>basal</strong> cells through microabrasions, driving epidermal proliferation</td></tr>
    <tr><td>Dermatophyte infection</td><td><em>Trichophyton</em>, <em>Microsporum</em>, <em>Epidermophyton</em>. Spores secrete <strong>keratinases and proteases</strong> to digest keratin, typically in the <strong>stratum corneum</strong> &mdash; hence the annular patch with central clearing</td></tr>
  </table>
  <h4 class="subsub">Nails</h4>
  <table>
    <tr><th>Finding</th><th>Mechanism</th></tr>
    <tr><td>Leukonychia (Mee&rsquo;s lines)</td><td>Temporary incomplete keratinization at the nail bed; usually harmless, but also heavy metal poisoning</td></tr>
    <tr><td>Koilonychia</td><td>Impaired keratin synthesis, associated with deficiency anaemia; thin, concave, ridged</td></tr>
    <tr><td>Beau&rsquo;s lines</td><td><strong>Halt of keratin production</strong> &mdash; transverse grooves. Illness, stress, injury, malnourishment</td></tr>
    <tr><td>Terry&rsquo;s nails</td><td>Overgrowth of connective tissue in the nail bed. Aging, liver disease, congestive heart failure, diabetes</td></tr>
    <tr><td>Clubbing</td><td><strong>Increased capillary density</strong> with increased release of vascular endothelial growth factor. Lung, inflammatory bowel, cardiovascular and liver disease</td></tr>
  </table>
  <button class="test-yourself-btn" style="--acc:#3b2a5e" onclick="window.openTestYourself('Test yourself &mdash; Dermatological mechanisms', TEST_YOURSELF.dermMechanisms)">Test yourself! &rarr;</button>

  <h3 class="sub" id="derm-cancers">2.6 &middot; Objective d &mdash; Skin cancers</h3>
  <table>
    <tr><th>Cancer</th><th>Mechanism and behaviour</th></tr>
    <tr><td><strong>Basal cell carcinoma</strong></td><td>Most common skin cancer and <strong>most common malignancy in humans</strong>. Ultraviolet-induced mutation of basal keratinocytes overactivating the <strong>Hedgehog signalling pathway</strong>. Head and neck; slow growing, rarely metastasises. Pearly papules with telangiectasias</td></tr>
    <tr><td><strong>Squamous cell carcinoma</strong></td><td>Second most common. Ultraviolet DNA damage and mutation in the <strong>tp53</strong> tumour suppressor gene; derived from keratinocytes. <strong>Keratin pearls and epithelial pearls are pathognomonic.</strong> Immunosuppression is a notable risk factor</td></tr>
    <tr><td><strong>Melanoma</strong></td><td>Arises from melanocytes at the <strong>dermal-epidermal junction</strong>. Ultraviolet light and oxidative stress damage melanocyte DNA. Risk inherited as an <strong>autosomal dominant trait with variable penetrance</strong></td></tr>
  </table>
  <div class="pearl"><strong>Melanoma progresses in a fixed order:</strong> radial growth within the
  epidermis &rarr; vertical growth penetrating the dermis &rarr; increasing tumour thickness &rarr;
  metastatic invasion of lymphatics and blood vessels. The radial-to-vertical shift is the moment
  depth starts to matter.</div>
  <p class="src">Lecture references include Fitzpatrick&rsquo;s Color Atlas and Synopsis of Clinical
  Dermatology (9th edition) and several StatPearls chapters; the course text is Banasik,
  <em>Pathophysiology</em>.</p>
</section>
'''

TY = '''    dermAnatomy: [
      {q:"Which epidermal layer is the site of cellular division?",
       choices:["Stratum corneum","Stratum granulosum","Stratum basale","Stratum lucidum"],correct:2,
       explain:"The basale is a single layer of rapidly dividing columnar keratinocytes at the bottom. Everything above it is a cell on its way to becoming dead barrier."},
      {q:"Vitamin D activation begins in the skin. Where do the two hydroxylation steps occur?",
       choices:["Liver, then kidneys","Kidneys, then liver","Both in the liver","Both in the skin"],correct:0,
       explain:"The skin makes cholecalciferol under ultraviolet B light; it is inactive until hydroxylated in the liver and then the kidneys to calcitriol."},
      {q:"What gives the stratum spinosum its prickle-cell appearance?",
       choices:["Keratohyalin granules","Desmosomes joining keratinocytes","Melanin transfer","Dead flattened keratinocytes"],correct:1,
       explain:"Desmosomes are the intercellular connections that produce the spiny look. This layer also holds the Langerhans cells."},
      {q:"Which cell mediates immunoglobulin E-driven inflammation in the dermis?",
       choices:["Fibroblast","Keratinocyte","Melanocyte","Mast cell"],correct:3,
       explain:"Mast cell degranulation is the mechanism behind both the wheal and urticaria."},
      {q:"Apocrine sweat itself is odourless. What produces body odour?",
       choices:["Bacterial degradation of apocrine sweat","Evaporation of eccrine sweat","Oxidation of sebum","Keratin breakdown in the corneum"],correct:0,
       explain:"Apocrine glands secrete protein and fatty lipids; the smell comes from bacteria acting on them."}
    ],
    dermMechanisms: [
      {q:"Why does an ulcer scar when an erosion generally does not?",
       choices:["An ulcer is infected","An ulcer destroys dermal collagen; an erosion spares the dermal-epidermal junction","An ulcer is larger","An ulcer loses melanocytes"],correct:1,
       explain:"Scarring is a dermal repair process. A lesion confined above the junction has no collagen loss to repair."},
      {q:"Allergic contact dermatitis appears 48 to 72 hours after exposure. Why the delay?",
       choices:["Histamine takes days to accumulate","It is a delayed hypersensitivity requiring T cell migration","The allergen must be absorbed slowly","Mast cells degranulate gradually"],correct:1,
       explain:"Langerhans cells present haptens to T cells during sensitization; re-exposure then requires T cells to migrate, which takes days rather than minutes."},
      {q:"Which structural change in psoriasis leaves the characteristic scale?",
       choices:["Loss of the stratum granulosum","Thickening of the stratum lucidum","Loss of melanocytes","Separation of epidermis from dermis"],correct:0,
       explain:"Epidermal hyperplasia with loss of the granular layer, plus failure to secrete lipids, produces the dry silvery scale."},
      {q:"Which pathway does basal cell carcinoma overactivate?",
       choices:["tp53 tumour suppressor","Fibroblast growth factor receptor-3","Hedgehog signalling","Vascular endothelial growth factor"],correct:2,
       explain:"Ultraviolet-induced mutation of basal keratinocytes overactivates Hedgehog signalling. tp53 belongs to squamous cell carcinoma."},
      {q:"How do keloids differ from normal scar remodelling?",
       choices:["Collagen bundles develop haphazardly and exceed the original wound boundaries","Type I collagen is replaced by type III","Granulation tissue never forms","Melanocytes proliferate at the wound edge"],correct:0,
       explain:"Fibroblast dysregulation prolongs the proliferative phase and unbalances deposition against degradation, so the scar overruns the wound it came from."}
    ],
'''

t = open(G, encoding="utf-8").read()

assert "dermatology" not in t.lower().split("<main>")[0].lower() or 'id="dermatology"' not in t, "already extended"
t = t.replace('  <a href="#inf-mediators">1.7 Objective f &mdash; Mediators &amp; opsonins</a>\n',
              '  <a href="#inf-mediators">1.7 Objective f &mdash; Mediators &amp; opsonins</a>\n' + TOC_ADD, 1)
t = t.replace("\n</main>", SECTION + "\n</main>", 1)
t = t.replace("  var TEST_YOURSELF = {\n", "  var TEST_YOURSELF = {\n" + TY, 1)

open(G, "w", encoding="utf-8").write(t)
print("sections:", re.findall(r'<section class="deck" id="([^"]+)"', t))
print("TEST_YOURSELF keys:", re.findall(r'^\s{4}(\w+): \[', t, re.M))
print("figures:", t.count('class="fig"'), "| buttons:", t.count("test-yourself-btn"))
d = 0
for l in t.split("\n"):
    d += len(re.findall(r'<div\b', l)) - len(re.findall(r'</div>', l))
print("div balance (0 = ok):", d)
