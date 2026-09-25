# -*- coding: utf-8 -*-
"""Section 7 of the Microbiology Exam 2 guide -- Disorders in Immunity (Dr. Webster).

Instructional objectives are VERBATIM from the syllabus (Micro.pdf, pages 3-4),
including its wording "Describe etiology autoimmune conditions." Content is
from the deck; the recording supplies emphasis only (the slide wins).

AUDIO: both halves of the 18 September recording were read from Notability's
own transcript (46 + 51 minutes). The local faster-whisper transcription was
still running when this was written, so the two-transcript cross-examination
is PENDING for this lecture; the quotes below are single-source and are marked
that way on the page.
"""

FIG = "micro-exam-2-study-guide-images"
DECK = "Lecture 7 &nbsp;Dr. Webster &nbsp;Disorders in Immunity.pptx"


def fig(name, w, h, alt, cap, slide):
    return ('<figure class="fig"><img width="%d" height="%d" loading="lazy" src="%s/%s" alt="%s">'
            '<figcaption>%s <span class="src">Source: %s, Slide %d.</span></figcaption></figure>'
            % (w, h, FIG, name, alt, cap, DECK, slide))


TOC = """
  <a class="top-link" href="#disorders-immunity">7 &middot; Disorders in Immunity</a>
  <a class="sub-link" href="#di-audio">&#9733; What the recording adds</a>
  <a class="sub-link" href="#di-immunopathologies">7.1 Objective 1 &mdash; The four immunopathologies</a>
  <a class="sub-link" href="#di-hypersensitivities">7.2 Objective 2 &mdash; The four hypersensitivities</a>
  <a class="sub-link" href="#di-allergy">7.3 Objective 3 &mdash; Diagnosing, treating &amp; preventing allergy</a>
  <a class="sub-link" href="#di-transfusion">7.4 Objective 4 &mdash; Transfusion reactions</a>
  <a class="sub-link" href="#di-transplant">7.5 Objective 5 &mdash; Transplantation &amp; histocompatibility</a>
  <a class="sub-link" href="#di-autoimmunity">7.6 Objective 6 &mdash; Autoimmunity</a>
  <a class="sub-link" href="#di-immunodeficiency">7.7 Objective 7 &mdash; Primary vs secondary immunodeficiency</a>
  <a class="sub-link" href="#di-cancer">7.8 Objective 8 &mdash; Carcinogenesis</a>
  <a class="sub-link" href="#di-immunotherapy">7.9 Objective 9 &mdash; Immunotherapy strategies</a>
"""

SECTION = """
<section class="deck" id="disorders-immunity">
  <h2 class="deck-title">7 &middot; Disorders in Immunity</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Describe the types of immunopathologies.</li>
      <li>Compare and contrast the types of hypersensitivities and diseases caused by hypersensitivity
      conditions.</li>
      <li>Describe the primary methods of diagnosing, treating, and preventing allergies.</li>
      <li>Describe the mechanism of transfusion reactions.</li>
      <li>Explain the immunology of transplantations and tissue histocompatibility.</li>
      <li>Describe etiology autoimmune conditions.</li>
      <li>Differentiate between primary and secondary immunodeficiency conditions.</li>
      <li>Explain the mechanisms of carcinogenesis.</li>
      <li>Compare and contrast immunotherapy strategies.</li>
    </ol>
  </div>

  <div class="callout"><strong>One table organizes most of this lecture.</strong> The four
  hypersensitivities differ by <em>effector mechanism</em>, and nearly everything later in the deck
  is one of them applied somewhere new: transfusion reactions are type II, the three speeds of
  transplant rejection are types II, IV and III, and autoimmunity uses every type <em>except</em> I.
  Learn the table in 7.2 first and the rest of the lecture places itself.</div>

<!--MICROL7AUDIO-->
  <div class="prof-flag" id="di-audio"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 18 September 2026</span>
  <p>About 97 minutes with Dr. Webster, in two parts. <b>Read from one transcript so far</b>
  (Notability&rsquo;s own); the second, independent transcription was still running when this guide
  was built, so the quotes below have not yet been cross-checked against it. Every factual claim was
  checked against the deck, and where the two differ the slide is what this guide teaches.</p>
  <p><b>Unlike Lecture 1, this lecture signposts.</b> It names one chart to learn, one mechanism
  that matters most, and <b>five slides not to memorize</b>.</p>
  <table>
    <tr><th>What was said</th><th>What it means for you</th></tr>
    <tr><td><em>&ldquo;This is actually a chart you <mark class="prof-highlight">should pay attention
    to</mark> because it is a very good summary chart of the four different types of
    hypersensitivities.&rdquo;</em> [part 1, about minute 10]</td>
    <td>Slide 9, the four-types table. It is reproduced in 7.2 and is the spine of the lecture.</td></tr>
    <tr><td><em>&ldquo;The most important thing I want [you] to remember about this is <mark
    class="prof-highlight">making the IgG antibodies, which can block the reaction</mark>.&rdquo;</em>
    [part 1, about minute 34]</td>
    <td>Desensitization (slides 29&ndash;30). The regulatory T cell effects are real, but the
    blocking immunoglobulin G is the headline.</td></tr>
    <tr><td><em>&ldquo;Please note <mark class="prof-highlight">there&rsquo;s no type 1 at
    all</mark>.&rdquo;</em> [part 2, about minute 13] &mdash; and of autoimmunity, <em>&ldquo;type 1 is not
    involved in either of these.&rdquo;</em> [part 2, about minute 21]</td>
    <td>Type I plays no part in graft rejection or in autoimmunity. Both lists run II, III and IV.</td></tr>
    <tr><td><em>&ldquo;B cell defect is agammaglobulinemia&hellip; we associate [it] with more bacterial
    infections. And <mark class="prof-highlight">yes, you need to know that. That&rsquo;s why it is
    bold and italicized</mark>.&rdquo;</em> [part 2, about minute 32]</td>
    <td>B cell deficiency &rarr; recurrent <b>bacterial</b> infections; T cell deficiency &rarr;
    fungal, viral and protozoan (slide 63&ndash;64).</td></tr>
    <tr><td><em>&ldquo;This is not a chart you need to memorize.&rdquo;</em> [part 1, about minute 4]</td>
    <td>Slide 6, the helminth antigen &harr; allergen pairings. Know the principle (allergens resemble
    parasite antigens), not the pairs.</td></tr>
    <tr><td><em>&ldquo;You don&rsquo;t need to memorize this chart.&rdquo;</em> [part 2, about minute 19]</td>
    <td>Slide 50, the four grades of graft versus host disease. Know what the disease is and that it
    affects about 30% of marrow recipients.</td></tr>
    <tr><td><em>&ldquo;Charts I do not want you to memorize&hellip; no, you do not need to memorize
    those charts.&rdquo;</em> [part 2, about minutes 29&ndash;30]</td>
    <td>Slides 58&ndash;60, the type II, III and IV autoimmune disease tables. The diseases you are
    expected to know are the ones slide 61 writes out: Graves&rsquo;, Hashimoto&rsquo;s, type 1
    diabetes, myasthenia gravis, multiple sclerosis.</td></tr>
    <tr><td><em>&ldquo;The process of transformation&hellip; I&rsquo;m not going to ask you to memorize
    the sequence.&rdquo;</em> [part 2, about minute 37]</td>
    <td>Slide 67&rsquo;s stepwise colon-cancer figure. Know that a cancer is one cell with
    <em>accumulated</em> mutations, not the order of the genes lost.</td></tr>
    <tr><td>Oncogenic viruses: <em>&ldquo;we will talk about the papilloma virus&hellip; hepatitis B and
    Epstein-Barr when you have my lecture on DNA [deoxyribonucleic acid] viruses. Dr. Fair will talk about&hellip; the human T
    cell leukemia virus as well as HIV and some herpes viruses.&rdquo;</em> [part 2, about minutes 38&ndash;39]</td>
    <td>Slide 68 is deferred to the virus lectures. Here, know that viruses are one route to oncogene
    activation, and the two that slide 81 names for prevention.</td></tr>
  </table>
  <p><b>Things said that are not on a slide</b> &mdash; consistent with the deck, useful as hooks:</p>
  <ul>
    <li><b>Immunoglobulin G is the only antibody that crosses the placenta</b>, which is why a
    sensitized Rh-negative mother&rsquo;s <em>next</em> Rh-positive baby is the one at risk.</li>
    <li>The tuberculin skin test is read at <b>48 to 72 hours</b>, and once positive it stays positive
    because of memory cells.</li>
    <li>Poison ivy oil binds the skin within about <b>15 minutes</b> (wash it off before then), and the
    first exposure takes <b>7 to 10 days</b> to make effector T cells &mdash; by which time the
    exposed skin has shed, so the first contact produces no rash.</li>
    <li>Blood type <b>O</b> is the universal donor (no A or B antigen on the cell); <b>AB</b> is the
    universal recipient (no anti-A or anti-B antibody in the serum).</li>
    <li>Bone marrow donors are matched on <b>at least 10</b> human leukocyte antigen markers, and even
    that is not always enough to prevent graft versus host disease.</li>
    <li>&ldquo;Nobody actually dies of HIV. They die of the things you catch because of the suppressed
    immune system.&rdquo;</li>
  </ul>
  <p class="muted"><b>Two things to distrust in the transcript:</b> it has the lecturer describe immune
  complexes as &ldquo;a type 2 reaction&rdquo; at the start of part 2 (slide 38 says type III, and it
  is type III) and allergy as &ldquo;IgA mediated&rdquo; (slide 23 says immunoglobulin E). Both may be
  transcription errors; the second transcription will settle it. Go by the slides.</p>
  </div>
<!--/MICROL7AUDIO-->

  <h3 class="sub" id="di-immunopathologies">7.1 &middot; Objective 1 &mdash; The four immunopathologies</h3>
  <table>
    <tr><th>Immunopathology</th><th>What it is</th><th>Direction</th></tr>
    <tr><td><strong>Allergy / hypersensitivity</strong></td><td>An exaggerated, misdirected expression of
    immune responses to an allergen (antigen). Uses the <em>same mechanisms</em> as protective
    immunity. Four types: I, II, III are <strong>B cell mediated</strong>; IV is <strong>T cell
    mediated</strong></td><td>Overreaction</td></tr>
    <tr><td><strong>Autoimmunity</strong></td><td>Abnormal responses to self antigens</td><td>Typically
    overreaction</td></tr>
    <tr><td><strong>Immunodeficiency</strong></td><td>Deficiency or loss of immunity</td><td>Underreaction</td></tr>
    <tr><td><strong>Cancer</strong></td><td>Both a <em>cause</em> and an <em>effect</em> of immune
    dysfunction</td><td>Underreaction</td></tr>
  </table>
  """ + fig("l7-s04-immunopathology-overview.png", 522, 346,
      "Overview diagram of immunopathologies: allergenic stimulation branches into overreaction (hypersensitivities types I to IV with examples) and underreaction (immunodeficiency and cancer).",
      "The whole lecture on one page. Read it as a fork at the top: <b>overreaction</b> on the right "
      "splits into the four hypersensitivities by the cell that drives them (B cell arrows to types I, II "
      "and III; the T cell arrow to type IV), while <b>underreaction</b> on the left leads to "
      "immunodeficiency and, through lack of surveillance, to cancer. Type II&rsquo;s example is a "
      "mother and fetus because Rh incompatibility is a type II reaction.", 4) + """

  <h3 class="sub" id="di-hypersensitivities">7.2 &middot; Objective 2 &mdash; The four hypersensitivities and their diseases</h3>
  <h4 class="subsub">The cells shared by defense and allergy</h4>
  <table>
    <tr><th>Cell</th><th>Where / what</th><th>Defensive role</th></tr>
    <tr><td>Mast cells</td><td>On epithelial surfaces; immunoglobulin E on the surface; filled with cytokine granules</td><td>&mdash;</td></tr>
    <tr><td>Eosinophils</td><td>Granulocytes that release toxic mediators in an immunoglobulin E response</td><td>Eukaryotic parasites</td></tr>
    <tr><td>Basophils</td><td>Rare granulocytes that initiate a type 2 helper T cell response and production of immunoglobulin E</td><td>Helminths</td></tr>
  </table>
  <div class="pearl"><strong>The hygiene hypothesis.</strong> Many allergens resemble parasitic antigens,
  and helminth infection (about 1 billion people heavily and persistently infected) produces exactly the
  allergic profile &mdash; CD4 type 2 helper T responses, high immunoglobulin E, more eosinophils and
  mast cells &mdash; yet no allergic disease. Why: <strong>nonspecific immunoglobulin E competes</strong>
  for the Fc receptors on mast cells, basophils and activated eosinophils, and <strong>regulatory T
  cells suppress</strong> T cell responses in chronic parasitic infection. Where helminths were eradicated
  (Western Europe, North America) by better hygiene, vaccination and antibiotics, the immune system is
  underused and less successfully regulated.</div>
  <p><strong>Predisposition.</strong> A generalized predisposition to allergy is familial &mdash; not a
  predisposition to a specific allergy. Allergy is affected by age, infection and geographic area; atopic
  allergies may be lifelong, outgrown, or develop later in life. The four groups are defined by the
  <strong>effector mechanism</strong>, and the reaction can differ with the mechanism of exposure.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; &ldquo;a chart you should pay attention to&rdquo;</span>
  <table>
    <tr><th>Type</th><th>Mechanism</th><th>Examples</th></tr>
    <tr><td><strong>I</strong><br>Immediate</td><td><strong>Immunoglobulin E mediated.</strong> Cell-bound antibody
    is crosslinked and releases inflammatory mediators; mast cells, basophils and eosinophils involved</td>
    <td>Hay fever, hives, anaphylactic shock</td></tr>
    <tr><td><strong>II</strong></td><td>Initiated by <strong>immunoglobulin G and M</strong>. Free antibody binds
    <strong>cell surface</strong> antigens; complement activated; cell lysis by the membrane attack complex
    and phagocytosis</td><td>Transfusion reactions</td></tr>
    <tr><td><strong>III</strong></td><td>Initiated by immunoglobulin G and M. Free antibody binds
    <strong>soluble</strong> antigens forming <strong>immune complexes</strong>, which embed in basement
    membranes and start inflammation (phagocytosis and complement)</td><td>Serum sickness; autoimmune
    conditions such as lupus</td></tr>
    <tr><td><strong>IV</strong><br>Delayed</td><td><strong>T cell mediated.</strong> Cytotoxic cells destroy tissue</td>
    <td>Contact dermatitis</td></tr>
  </table></div>

  <h4 class="subsub">Allergens and the type I mechanism</h4>
  <p>Allergens are immunogenic: <strong>proteins</strong>, or lower molecular weight
  <strong>haptens</strong>. They typically enter through epithelial portals &mdash; respiratory,
  gastrointestinal, skin &mdash; and the organ where the allergy shows may or may not be the portal of
  entry.</p>
  <table>
    <tr><th>Dose</th><th>What happens</th></tr>
    <tr><td><strong>Sensitizing dose</strong> (first contact)</td><td>Specific B cells form immunoglobulin E, which
    attaches to mast cells and basophils. <strong>Generally no signs or symptoms.</strong></td></tr>
    <tr><td><strong>Provocative dose</strong> (later contact)</td><td>The same allergen binds the immunoglobulin E on
    the mast cell (each cell binds 10,000&ndash;40,000 immunoglobulin E); mast cells
    <strong>degranulate</strong>, releasing inflammatory cytokines.</td></tr>
  </table>
  """ + fig("l7-s13-type-i-sensitization.png", 692, 510,
      "Two-panel diagram: sensitization with B cell recognition, plasma cells making immunoglobulin E that binds mast cells; then subsequent exposure where allergen crosslinks the bound antibody and the mast cell degranulates, causing red itchy eyes, hives and runny nose.",
      "Two exposures, two panels. On the left nothing visible happens: the allergen is carried to a "
      "lymph node, plasma cells make immunoglobulin E, and it parks on mast cells (step 6) &mdash; which is "
      "why the sensitizing dose produces no symptoms. On the right the <em>same</em> allergen bridges the "
      "bound antibody (step 8) and the mast cell empties its granules into the blood, so the symptoms "
      "appear in organs far from where the allergen entered.", 13) + """
  <p>General targets are the skin, upper respiratory tract, gastrointestinal tract and conjunctiva
  (rashes, itching, redness, rhinitis, sneezing, diarrhea, tears); systemic targets are smooth muscle,
  mucous glands and nervous tissue (vascular dilation and constriction changing blood pressure and
  respiration).</p>
  <table>
    <tr><th>Manifestation</th><th>Mechanism</th></tr>
    <tr><td>Urticaria (hives)</td><td>Mast cells in the skin release histamine &rarr; raised, itchy swelling</td></tr>
    <tr><td>Angioedema</td><td>Activation of mast cells <em>deeper</em> in the skin</td></tr>
    <tr><td>Atopic dermatitis (eczema)</td><td>A more <em>prolonged</em> allergic response in the skin</td></tr>
    <tr><td>Allergic rhinitis (hay fever)</td><td>Inhaled allergen; histamine raises capillary permeability and nasal mucus; eosinophils are attracted from blood, release mediators and are shed into the nasal passage</td></tr>
    <tr><td>Food allergy</td><td>Vomiting, diarrhea and urticaria. Local histamine acts on intestinal epithelium, vessels and smooth muscle; <strong>urticaria appears because antigen enters blood vessels and is carried to the skin</strong></td></tr>
    <tr><td>Allergic asthma</td><td><strong>Acute:</strong> bronchial smooth muscle contraction, more mucus, airway obstruction. Leads to <strong>chronic asthma, which is type IV</strong>, mediated by cytokines and eosinophil granules</td></tr>
  </table>
  <h4 class="subsub">Anaphylaxis</h4>
  <p><strong>Cutaneous anaphylaxis</strong> is the wheal and flare skin reaction &mdash; the one used in
  allergy diagnosis. <strong>Systemic anaphylaxis</strong> is sudden respiratory and circulatory
  disruption that can be fatal in minutes. Allergen and route vary: bee stings, antibiotics and serum by
  injection; foods such as peanuts by mouth. The allergen reaches the bloodstream and activates
  connective tissue mast cells around blood vessels throughout the body. Fluid leaves the blood &rarr;
  drastic fall in blood pressure &rarr; tissue swelling &rarr; organ damage &rarr; death by asphyxiation
  from constricted airways; <strong>500&ndash;1000 deaths a year</strong> in the United States.</p>
  """ + fig("l7-s22-anaphylaxis-epinephrine.jpg", 935, 813,
      "Graph of mean arterial pressure and epinephrine concentration against time during systemic anaphylaxis: pressure collapses at time zero and recovers as an epinephrine spike is given.",
      "Read the two lines against each other. The red mean arterial pressure line falls off a cliff at "
      "time zero &mdash; fluid leaving the vessels &mdash; and the yellow arrows mark the epinephrine doses. "
      "Pressure climbs back only as the blue epinephrine line spikes, which is the curve&rsquo;s whole point: "
      "epinephrine is what reverses the collapse, by resealing endothelial tight junctions and "
      "stimulating the heart.", 22) + """
  <div class="pearl"><strong>What epinephrine does in anaphylaxis</strong> (five actions): stimulates
  reformation of endothelial <strong>tight junctions</strong>; relaxes bronchial smooth muscle; prevents or
  decreases upper airway mucosal edema; stimulates the heart; binds receptors on immune cells to suppress
  histamine release.</div>
  <p><strong>Late phase reaction.</strong> Immunoglobulin E reactions have an immediate response
  (the wheal and flare, from mast cell degranulation) followed <strong>about 6 hours</strong> later by a
  late phase reaction mediated by <em>synthesized</em> products such as leukotrienes. It attracts more
  cells, including eosinophils, whose cytokines enhance inflammation and make the tissue more sensitive
  next time. In asthma, measured as forced expiratory volume in 1 second, the immediate response is
  under 1 hour and the late phase response over 6 hours.</p>

  <h4 class="subsub">Types II, III and IV and their diseases</h4>
  <table>
    <tr><th>Type</th><th>Key features</th><th>Diseases</th></tr>
    <tr><td><strong>II</strong></td><td>Lyses foreign cells; immunoglobulin G or M; stimulates complement</td>
    <td>Transfusion reactions (ABO); Rh factor &mdash; hemolytic disease of the newborn; some autoimmune:
    autoimmune hemolytic anemia, myasthenia gravis (acetylcholine receptors)</td></tr>
    <tr><td><strong>III</strong></td><td>Immunoglobulin G and M (sometimes A) with complement; complexes deposit in
    basement membranes of epithelial tissues; <strong>needs a large amount of antigen</strong>;
    symptoms <strong>delayed hours to days</strong>; joints, skin and kidney typical</td>
    <td><strong>Serum sickness</strong> (foreign animal proteins &mdash; horse serum for tetanus, animal
    hormones or drugs; complexes in heart, kidneys, skin, joints). <strong>Arthus reaction</strong>
    (localized dermal vasculitis after a second vaccine injection at one site; self-limiting).
    Autoimmune: post-streptococcal glomerulonephritis, systemic lupus erythematosus, rheumatoid arthritis</td></tr>
    <tr><td><strong>IV</strong></td><td>Delayed; T cell mediated; activation of and damage by T cells</td>
    <td>Infectious allergy (tuberculosis, leprosy, syphilis, histoplasmosis, toxoplasmosis,
    candidiasis); tuberculin skin test; contact dermatitis from plants, metals, cosmetics; graft
    rejection</td></tr>
  </table>
  <p><strong>Contact dermatitis</strong> follows the same two-dose logic as type I, but with T cells:
  first contact is the sensitizing dose; later contact is the reactive dose, with tissue damage from
  macrophage cytokines and cytotoxic T cells.</p>

  <h3 class="sub" id="di-allergy">7.3 &middot; Objective 3 &mdash; Diagnosing, treating and preventing allergies</h3>
  <p>First decide whether the patient has <strong>allergy or infection</strong>. Then:</p>
  <table>
    <tr><th>Test</th><th>Use</th></tr>
    <tr><td>Skin testing &mdash; skin prick, intradermal</td><td>Reads wheal and flare reactions</td></tr>
    <tr><td>Blood tests</td><td>Specific immunoglobulin E; increased basophils</td></tr>
    <tr><td>Physician-supervised challenge</td><td>Food allergy when other tests are inconclusive</td></tr>
    <tr><td>Patch test</td><td>Contact dermatitis (type IV)</td></tr>
  </table>
  <p>Management of type I hypersensitivity has three general methods: <strong>prevention,
  pharmacological control and desensitization</strong>. Prevention means modifying the environment and
  behaviors to avoid the allergen.</p>
  <table>
    <tr><th>Drug</th><th>Action</th></tr>
    <tr><td>Corticosteroids</td><td>Inhibit lymphocytes to reduce immunoglobulin E</td></tr>
    <tr><td>Cromolyn sodium</td><td>Blocks mast cell degranulation</td></tr>
    <tr><td>Montelukast sodium</td><td>Blocks leukotriene synthesis</td></tr>
    <tr><td>Omalizumab</td><td>Monoclonal antibody against immunoglobulin E</td></tr>
    <tr><td>Antihistamines</td><td>Bind histamine receptors on target organs</td></tr>
    <tr><td>Epinephrine</td><td>Reverses airway constriction; re-establishes endothelial tight junctions</td></tr>
  </table>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; &ldquo;the most important thing&rdquo;</span>
  <p><strong>Desensitization</strong> (allergen-specific immunotherapy). The most common form is
  <strong>subcutaneous immunotherapy</strong>: small amounts of allergen by injection. The injected
  allergen stimulates high levels of <mark class="prof-highlight">allergen-specific immunoglobulin G that
  blocks the allergen from reaching the immunoglobulin E</mark>, so mast cells do not degranulate. It
  improves reactions in about <strong>80%</strong> of those who complete it.</p></div>
  <p>&ldquo;Of course it&rsquo;s not that simple&rdquo;: desensitization also activates <strong>regulatory T
  cells</strong>, which inhibit T cell activation of B cells and release anti-inflammatory cytokines, and
  induces mediators that damp T cell proliferation and mast cell and eosinophil activity.
  <strong>Sublingual immunotherapy</strong> places allergen under the tongue as a tablet or liquid; it is
  used more elsewhere than in the United States (which has tablets for pollen and dust mite). A 4-year
  trial of a peanut dose equal to 1/75 of a kernel was effective and safe, protecting against accidental
  exposure; it has also worked for kiwi, hazelnut, milk and peach.</p>

  <h3 class="sub" id="di-transfusion">7.4 &middot; Objective 4 &mdash; The mechanism of transfusion reactions</h3>
  <p>A transfusion reaction is <strong>type II</strong>. Donor and recipient are matched for the ABO
  blood group antigens because <strong>red blood cells carry no major histocompatibility complex
  molecules</strong> &mdash; ABO is what the immune system sees. You carry antibodies in your serum
  against the ABO antigens you <em>lack</em>. Transfusions are temporary, and an ABO incompatibility can be
  fatal through complement activation and cell lysis.</p>
  <table>
    <tr><th>Step</th><th>Detail</th></tr>
    <tr><td>Cross-match</td><td><strong>Recipient&rsquo;s serum against donor&rsquo;s red cells.</strong> Not the
    reverse: even whole blood carries too little donor antibody to coat the recipient&rsquo;s cells densely
    enough to react</td></tr>
    <tr><td>Consequences</td><td>Red cell destruction &rarr; blocked glomeruli, fever, jaundice. Even incomplete
    complement activation leaves antibody-coated cells for natural killer cells and macrophages</td></tr>
  </table>
  <div class="callout"><strong>Rh factor and hemolytic disease of the newborn (erythroblastosis fetalis).</strong>
  Rh antigen is on Rh-positive cells only. An Rh-negative person makes no anti-Rh antibody
  <em>unless sensitized</em> &mdash; by a bad transfusion or an incompatible pregnancy (Rh-negative mother,
  Rh-positive fetus). The <strong>first pregnancy is normally fine</strong>; it sensitizes. Later
  pregnancies may be hemolytic. Prevention is <strong>passive immunization with antibody against the Rh
  antigen (Rhogam)</strong>, which prevents sensitization of the mother. Give it at <strong>26&ndash;28
  weeks</strong>, <strong>within 72 hours after birth</strong>, and after prenatal invasive tests, abdominal
  injury or accidental exposure.</div>

  <h3 class="sub" id="di-transplant">7.5 &middot; Objective 5 &mdash; The immunology of transplantation and tissue histocompatibility</h3>
  <p>Rejection runs both ways &mdash; the host may reject the graft, and the graft may reject the host
  &mdash; and it is governed by the <strong>major histocompatibility complex</strong>: different grafts
  succeed to different degrees because of its compatibility.</p>
  <table>
    <tr><th>Graft</th><th>Source</th></tr>
    <tr><td>Autograft</td><td>Self (skin, gum or vein graft)</td></tr>
    <tr><td>Isograft</td><td>Genetically identical twin</td></tr>
    <tr><td>Allograft</td><td>Another member of the same species</td></tr>
    <tr><td>Xenograft</td><td>Another species</td></tr>
  </table>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; &ldquo;there&rsquo;s no type 1 at all&rdquo;</span>
  <table>
    <tr><th>Solid organ problem</th><th>Type</th><th>Mechanism</th></tr>
    <tr><td>Hyperacute rejection</td><td><strong>II</strong></td><td>Preexisting antibody against graft antigens; the
    graft becomes engorged and purple from hemorrhage and fails</td></tr>
    <tr><td>Acute rejection</td><td><strong>IV</strong></td><td>Effector T cells respond to human leukocyte antigen
    differences between donor and recipient</td></tr>
    <tr><td>Chronic rejection</td><td><strong>III</strong></td><td>Months or years later; immune complexes in the
    graft&rsquo;s vessel walls thicken them until blood supply fails. Causes failure of <strong>more than half of
    kidney and heart transplants after 10 years</strong> or more</td></tr>
    <tr><td>Graft versus host disease</td><td><strong>IV</strong></td><td>Donor cells attack host tissue</td></tr>
  </table></div>
  """ + fig("l7-s46-acute-rejection.png", 743, 218,
      "Four-panel strip showing acute kidney rejection: donor dendritic cells in the graft migrate to the spleen, activate effector T cells, which travel back through the blood and destroy the graft.",
      "Acute rejection as a round trip. The graft brings its own dendritic cells; they leave for the "
      "<b>spleen</b>, activate the recipient&rsquo;s effector T cells there, and those T cells come back "
      "through the blood to destroy the kidney. No antibody appears anywhere in the strip, which is what "
      "makes this type IV rather than the antibody-driven hyperacute type II.", 46) + """
  <table>
    <tr><th>Tissue</th><th>Matching requirement</th><th>Why</th></tr>
    <tr><td><strong>Cornea</strong> (first organ successfully transplanted)</td><td>Succeeds even without a human
    leukocyte antigen match</td><td>The eye downregulates T cells, macrophages, neutrophils and complement so
    inflammation cannot impair vision</td></tr>
    <tr><td><strong>Liver</strong></td><td>Human leukocyte antigens <em>not</em> assessed; <strong>ABO blood group
    is</strong></td><td>Architecture and vascularization; hepatocytes carry very little class I and no class II;
    constant exposure to digestive proteins makes it tolerant</td></tr>
    <tr><td><strong>Bone marrow</strong></td><td><strong>Most sensitive</strong> to human leukocyte antigen
    discrepancies</td><td>Used for genetic disorders and cancers. Sensitivity can cause <strong>graft versus host
    disease</strong>: systemic, with skin rash, muscle, liver and gastrointestinal involvement, in about
    <strong>30%</strong> of marrow recipients</td></tr>
  </table>
  <p><strong>Dealing with graft issues:</strong> minimize rejection by tissue matching human leukocyte
  antigens (mixed lymphocyte reaction, tissue typing), and with immunosuppressive drugs &mdash; purine
  analogs, corticosteroids, tacrolimus and cyclosporine, rapamycin (sirolimus).</p>

  <h3 class="sub" id="di-autoimmunity">7.6 &middot; Objective 6 &mdash; The etiology of autoimmune conditions</h3>
  <p>In autoimmunity the immune system has <strong>lost tolerance</strong> to autoantigens and forms
  autoantibodies and sensitized T cells against them, destroying self tissue. It involves <strong>all
  hypersensitivity types except type I</strong>. There are genetic and gender predispositions:
  autoimmunities run in families, and <strong>women are more likely than men</strong> to have them.
  Disruption can be systemic or organ specific.</p>
  <table>
    <tr><th>Origin</th><th>Mechanism</th><th>Examples</th></tr>
    <tr><td><strong>Sequestered antigen theory</strong></td><td>Some tissues are immunologically privileged during
    embryonic growth; damaged later, they release antigens that are attacked</td><td>Central nervous system, lens of the
    eye, thyroid, testes. Trauma to one eye releases intraocular antigens that activate T cells, which attack
    <em>both</em> eyes (slide 55)</td></tr>
    <tr><td><strong>Molecular mimicry</strong> (a normal immune response)</td><td>Foreign and self antigens are
    similar, so the response cross-reacts</td><td>Rheumatic fever (cross-reactive strep antigen; antibodies react
    with heart tissue); Lyme disease arthritis (<em>Borrelia burgdorferi</em>); reactive arthritis
    (<em>Shigella</em>, <em>Salmonella</em>, <em>Campylobacter</em>); type 1 diabetes (coxsackie virus A and B,
    echovirus, rubella)</td></tr>
    <tr><td>Noninfectious response</td><td>Tissue damage without infection</td><td>The eye trauma example above</td></tr>
    <tr><td><strong>Thymic senescence</strong></td><td>The thymus is most active in fetal and early neonatal life, then
    involutes (replaced by fat). Premature thymic aging is characteristic of young people with autoimmune
    disorders; decreased output may mean less efficient T cell development and more opportunistic
    infection, cancer and autoimmunity</td><td>The mechanism is unclear</td></tr>
  </table>
  <table>
    <tr><th>Disease</th><th>Target</th><th>Result</th></tr>
    <tr><td>Graves&rsquo; disease</td><td>Autoantibodies attach to receptors on thyroxine-secreting follicle cells</td><td>More thyroxine &mdash; hyperthyroidism</td></tr>
    <tr><td>Hashimoto&rsquo;s thyroiditis</td><td>Autoantibodies and T cells destroy follicle cells</td><td>Less thyroxine &mdash; hypothyroidism</td></tr>
    <tr><td>Diabetes mellitus (type 1)</td><td>Insulin-producing cells of the pancreas</td><td>Reduced insulin</td></tr>
    <tr><td>Myasthenia gravis</td><td>Autoantibodies bind acetylcholine receptors</td><td>Pronounced muscle weakness</td></tr>
    <tr><td>Multiple sclerosis</td><td>Myelin sheath damaged by T cells <em>and</em> autoantibodies; may follow Epstein-Barr or a retrovirus</td><td>Paralyzing neuromuscular disease</td></tr>
  </table>
  <p class="muted">Slides 58&ndash;60 tabulate further type II, III and IV autoimmune diseases with their
  autoantigens. They were named in the lecture as charts not to memorize.</p>

  <h3 class="sub" id="di-immunodeficiency">7.7 &middot; Objective 7 &mdash; Primary versus secondary immunodeficiency</h3>
  <p>Components of the immune response are absent; deficiencies can involve B cells, T cells,
  phagocytes and complement.</p>
  <table>
    <tr><th></th><th>Primary</th><th>Secondary</th></tr>
    <tr><td>When</td><td><strong>Congenital</strong> &mdash; usually genetic errors</td><td><strong>Acquired after birth</strong>, from natural or artificial agents</td></tr>
    <tr><td>Examples</td><td><strong>Agammaglobulinemia</strong> (B cell defect, no antibodies &rarr; more
    <mark class="prof-highlight">bacterial</mark> infections). <strong>DiGeorge syndrome</strong> (T cell
    defect; thymus missing or abnormal &rarr; fungal, protozoan, helminth, viral infections).
    <strong>Severe combined immunodeficiency</strong> (both lymphocyte limbs missing or defective; no
    adaptive response). Complement and phagocyte deficiencies</td>
    <td>Infection and organic disease &mdash; the <strong>human immunodeficiency virus targets T helper
    cells</strong>, suppressing immunity overall; chemotherapy or radiation; blood cell cancers</td></tr>
  </table>
  """ + fig("l7-s64-primary-immunodeficiency.png", 777, 387,
      "Diagram of lymphocyte development from lymphoid stem cell into T cells via the thymus and B cells via bone marrow, with X marks at the defects: severe combined immunodeficiency, DiGeorge syndrome, adenosine deaminase deficiency, congenital agammaglobulinemia and hypogammaglobulinemia, and the infections each causes.",
      "Every primary immunodeficiency is an X on this developmental map, and <b>where</b> the X falls "
      "predicts the infections. Block at the stem cell and both limbs fail (severe combined "
      "immunodeficiency). Block on the upper T cell limb &mdash; no thymus in DiGeorge &mdash; and the "
      "panel on the right shows fungal, protozoan and viral infections. Block on the lower B cell limb "
      "and the result is recurrent <b>bacterial</b> infection.", 64) + """

  <h3 class="sub" id="di-cancer">7.8 &middot; Objective 8 &mdash; The mechanisms of carcinogenesis</h3>
  <p>Cancer cells carry genetic alterations that disrupt the normal cell division cycle. Possible causes:
  errors in mitosis, genetic damage, <strong>activation of oncogenes</strong>, or retroviruses. Tumors may be
  <strong>benign</strong> (nonspreading, self-contained) or <strong>malignant</strong> (spreading from the
  tissue of origin to other sites). <strong>Immune surveillance</strong> keeps cancer &ldquo;in check.&rdquo;</p>
  <p><strong>Transformation:</strong> a cancer arises from a <strong>single cell</strong> that has
  accumulated <strong>multiple mutations</strong>; oncogenes are activated by radiation, chemicals or
  oncogenic viruses (papillomavirus and cervical carcinoma, hepatitis B virus and liver cancer, among
  others).</p>
  <table>
    <tr><th>Necessary characteristics of cancer cells</th></tr>
    <tr><td>They stimulate their own growth &middot; ignore growth-inhibiting signals &middot; avoid death by
    apoptosis &middot; develop a blood supply (angiogenesis) &middot; leave their site of origin to invade other
    tissues (metastasis) &middot; replicate constantly &middot; evade and outrun the immune response</td></tr>
  </table>
  <table>
    <tr><th>Tumor antigens (more than 1000 identified)</th><th>Where found</th></tr>
    <tr><td><strong>Tumor specific</strong></td><td>On tumor cells, <strong>not</strong> on normal cells. Derived from
    viral proteins, mutated cellular proteins or amino acid recombinations</td></tr>
    <tr><td><strong>Tumor associated</strong></td><td>On tumor cells <strong>and</strong> on normal cells in smaller
    amounts</td></tr>
  </table>
  <div class="pearl"><strong>How successful tumors evade immunity.</strong> A variant tumor cell can cleave
  the stress molecule that natural killer and gamma-delta T cells recognize from its surface; the soluble
  molecule then binds the lymphocytes&rsquo; receptor, and the tumor cell escapes killing. Tumors also
  secrete <strong>transforming growth factor beta</strong>, suppressing immunity and recruiting
  <strong>regulatory T cells</strong>, which make more of it plus interleukin 10 and suppress the CD8 and CD4
  type 1 helper cells specific for tumor antigens. <strong>The more regulatory T cells in a tumor, the
  worse the prognosis.</strong></div>

  <h3 class="sub" id="di-immunotherapy">7.9 &middot; Objective 9 &mdash; Comparing immunotherapy strategies</h3>
  <table>
    <tr><th>Strategy</th><th>How it works</th><th>Status / use</th></tr>
    <tr><td><strong>Immune checkpoint inhibitors</strong></td><td>Block checkpoint proteins binding their partner,
    preventing the &ldquo;off&rdquo; signal so T cells keep killing. Do <em>not</em> kill cancer cells directly</td>
    <td>Melanoma, some lung cancers</td></tr>
    <tr><td><strong>Adoptive cell therapy</strong></td><td>Patient&rsquo;s own cells engineered outside the body and
    returned</td><td>Tumor infiltrating lymphocytes: in development, not approved. CAR-T (chimeric antigen
    receptor T cells): <strong>approved for blood cancers</strong>. Chimeric antigen receptor natural killer cells: mostly in
    trials, including solid tumors</td></tr>
    <tr><td><strong>Monoclonal antibodies</strong></td><td>Diagnosis <em>and</em> elimination of cancer cells;
    can carry a chemotherapy drug or radionuclide (anti-CD20 plus radionuclide irradiates malignant B cells;
    anti-CD30 plus auristatin stops lymphoma cells forming a mitotic spindle)</td><td>More than 100 approved
    by the Food and Drug Administration</td></tr>
    <tr><td><strong>Cytokines</strong></td><td>Interleukin 2 (aldesleukin): more cytotoxic T and natural killer cells;
    interferon alpha: activates natural killer and dendritic cells; growth factors: erythropoietin (red cells),
    interleukin 11 (platelets)</td><td>Interleukin 2: metastatic kidney cancer, melanoma. Interferon alpha:
    melanoma, Kaposi&rsquo;s sarcoma, several blood cancers</td></tr>
    <tr><td><strong>Coley&rsquo;s toxins</strong></td><td>1890s: bone sarcomas regressed with streptococcal skin
    infection; mix of killed streptococci and <em>Serratia marcescens</em></td><td>Fell from favor with radiation
    and chemotherapy</td></tr>
    <tr><td><strong>Oncolytic viruses</strong></td><td>Infect normal and cancer cells but replicate in and lyse
    only tumor cells; some natural (mumps), others engineered. Challenge: the immune system may clear them
    first</td><td>A few approved; one in the United States, for melanoma</td></tr>
    <tr><td><strong>Cancer vaccines</strong></td><td><strong>Prophylactic</strong> &mdash; prevent the infection
    (hepatitis B &rarr; hepatocarcinoma; papillomavirus &rarr; reproductive cancers). <strong>Therapeutic</strong>
    &mdash; activate immunity against tumor antigens</td><td>Bacillus Calmette-Gu&eacute;rin (weakened
    tuberculosis organism): bladder cancer. Sipuleucel-T: metastatic, castration-resistant prostate
    cancer</td></tr>
  </table>
  <p class="muted">Slide 78 also says granulocyte and granulocyte-macrophage colony-stimulating factors
  &ldquo;stimulate growth of T cells.&rdquo; That is the slide&rsquo;s wording; no quiz question turns on it.</p>

  <button type="button" class="test-yourself-btn" onclick="window.openTestYourself('Test yourself &mdash; Disorders in Immunity', TEST_YOURSELF.disordersImmunity)">Test yourself! &rarr;</button>
  <p class="src">Source: <em>Lecture 7 &mdash; Disorders in Immunity</em> (Dr. Webster), Slides 1&ndash;81,
  and the PAJ 5200 syllabus instructional objectives.</p>
</section>
"""

TEST = """    disordersImmunity: [
      {q:"A kidney graft placed into a patient who already carries antibody against its antigens swells, turns purple and fails. Which hypersensitivity type is this?",
       choices:["Type II","Type I","Type III","Type IV"],correct:0,
       explain:"Hyperacute rejection is type II: preexisting antibody binds the graft's cells and triggers complement. Acute rejection is type IV and chronic rejection is type III; type I plays no part in rejection."},
      {q:"How does subcutaneous desensitization prevent mast cell degranulation?",
       choices:["It removes immunoglobulin E from mast cells","It destroys the mast cells","It blocks histamine receptors","It raises allergen-specific immunoglobulin G that blocks the allergen"],correct:3,
       explain:"The injected allergen raises blocking immunoglobulin G, so the allergen never reaches the immunoglobulin E on the mast cell. Blocking histamine receptors is what antihistamines do."},
      {q:"A child has recurrent bacterial infections and no detectable antibody. Which defect fits?",
       choices:["DiGeorge syndrome","Human immunodeficiency virus infection","A B cell defect (agammaglobulinemia)","A complement deficiency"],correct:2,
       explain:"B cell deficiency brings recurrent bacterial infections. T cell deficiency, such as DiGeorge syndrome, brings fungal, protozoan and viral infections."},
      {q:"In a cross-match, what is tested against what?",
       choices:["Donor serum against recipient red cells","Recipient serum against donor red cells","Recipient red cells against donor red cells","Donor serum against recipient serum"],correct:1,
       explain:"Recipient serum is tested against donor red cells. The reverse is not done because even whole blood carries too little donor antibody to cause a reaction."},
      {q:"Which transplant is most sensitive to human leukocyte antigen mismatch?",
       choices:["Cornea","Liver","Bone marrow","Skin autograft"],correct:2,
       explain:"Bone marrow is the most sensitive and can cause graft versus host disease in about 30% of recipients. The cornea and liver both succeed across human leukocyte antigen differences."}
    ],
"""
