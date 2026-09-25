# -*- coding: utf-8 -*-
"""Section 6 of the Microbiology Exam 1 guide -- The Acquisition of Specific Immunity.

Instructional objectives are VERBATIM from the deck's own objective slide.

DECK-ONLY. Lecture 6 was delivered on 11 September but no recording has
surfaced -- not in the inbox and not in Notability's cache, where Lecture 5's
audio was eventually found. Nothing here depends on audio; the slides are
authoritative anyway, and the guide says where they are thin rather than
filling gaps with invented content.

TWO OBJECTIVES ARE THINLY SERVED BY THE DECK and the guide states so: laboratory
tests in immunology appear only as antibody titres and the BAU unit, and the
classical-against-alternative complement comparison lives in Lecture 5, surviving
here only as complement fixation by antibody.
"""

SECTION = """
<section class="deck" id="specific-immunity">
  <h2 class="deck-title">6 &middot; The Acquisition of Specific Immunity</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Relate innate and specific immunity.</li>
      <li>Review the role of leukocytes in the inflammatory process.</li>
      <li>Describe the interaction between antigens, antibodies, and leukocytes.</li>
      <li>Compare and contrast antibody structure, class, and function in specific immunity.</li>
      <li>Compare and contrast laboratory tests implemented in immunology.</li>
      <li>Compare and contrast genetic basis for specificity, diversity and self/non-self
      discrimination.</li>
      <li>Compare and contrast the mechanisms of humoral and cellular immune responses.</li>
      <li>Compare and contrast classical and alternative complement pathways in specific
      immunity.</li>
    </ol>
  </div>

  <div class="callout">
    <p><strong>This is the second half of a pair.</strong> Lecture 5 covered the two nonspecific
    lines; this one covers the third, and the two are examined together. The hinge between them is
    worth stating: <strong>organisms must hit the barriers in order</strong> &mdash; physical and
    chemical first, then the white cell processes, and only after those can an adaptive response
    begin.</p>
    <p><strong>Where the deck is thin, this guide says so.</strong> Objective 5 (laboratory tests)
    appears only as antibody <strong>titres</strong> and the <strong>BAU</strong> unit. Objective 8
    (classical against alternative complement) was covered in Lecture 5 and survives here only as
    complement fixation by antibody. Nothing has been invented to fill either.</p>
  </div>

  <h3 class="sub" id="si-acquired">6.1 &middot; Objective 1 &mdash; The four kinds of acquired immunity</h3>
  <p><strong>Specific immunity is adaptive</strong> and highly specific, acquired through contact
  with infectious agents &mdash; against <strong>innate</strong> immunity, which we are born with.
  A special type of innate immunity is <strong>species immunity</strong>: illnesses we cannot
  contract <em>because</em> we are human.</p>
  <p>Acquired immunity sorts on two axes at once &mdash; <strong>active or passive</strong>, and
  <strong>natural or artificial</strong>. Four boxes, and the exam will want you to place a
  scenario in one:</p>
  <table class="tbl">
    <tr><th></th><th>NATURAL</th><th>ARTIFICIAL</th></tr>
    <tr><td><strong>ACTIVE</strong><br><span class="muted">you make it</span></td><td>Recovery from infection &mdash; including <strong>subclinical or asymptomatic</strong> infection</td><td><strong>Vaccination.</strong> Degree and duration vary with each disease</td></tr>
    <tr><td><strong>PASSIVE</strong><br><span class="muted">you receive it</span></td><td><strong>Maternal antibody</strong> &mdash; across the placenta, then milk-borne through nursing</td><td><strong>Immunotherapy</strong> &mdash; pooled serum (gamma globulin) or donor antibody. Used for hepatitis A, rabies, tetanus</td></tr>
  </table>
  <p><strong>Two numbers from this section.</strong> Children acquire <strong>99% of natural
  passive immunity in utero</strong> &mdash; nursing adds beneficial microbes and maternal
  antibody the placenta cannot pass, but the bulk arrives before birth. And
  <strong>antibody titres</strong> are what tell you whether a vaccine on your record is still
  measurably effective, or whether a booster is needed before starting a hospital or laboratory
  post.</p>

  <h3 class="sub" id="si-leukocytes">6.2 &middot; Objective 2 &mdash; The leukocytes, in order</h3>
  <p>All five originate in the <strong>bone marrow</strong>, and are counted by manual examination
  of a stained blood smear or by automated hematology.</p>
  <div class="callout">
    <p><strong>&ldquo;Never let monkeys eat bananas&rdquo;</strong> &mdash; highest to lowest
    percentage: <strong>N</strong>eutrophils, <strong>l</strong>ymphocytes,
    <strong>m</strong>onocytes, <strong>e</strong>osinophils, <strong>b</strong>asophils.</p>
    <p>Lecture 5 gives the actual figures, and they are worth carrying together: neutrophils
    55&ndash;90%, lymphocytes 20&ndash;35%, monocytes 3&ndash;7%, eosinophils 1&ndash;3%,
    basophils 0.5%.</p>
  </div>

  <h3 class="sub" id="si-mhc">6.3 &middot; Objectives 3 and 6 &mdash; MHC, and the genetics of self</h3>
  <p>The <strong>Major Histocompatibility Complex</strong> is also called <strong>human leukocyte
  antigen</strong>. Its receptors are on <strong>all cells except red blood cells</strong>, and its
  genes sit on <strong>chromosome 6</strong> in a multi-gene complex of classes I, II and III. It
  does two jobs: <strong>recognition of self</strong>, and <strong>rejection of foreign
  tissue</strong> &mdash; the same system, read two ways.</p>
  <table class="tbl">
    <tr><th>Class I</th><th>Class II</th></tr>
    <tr><td>Displays unique self molecules and regulates immune reactions. Some T cells must engage it before reacting to foreign cells &mdash; the <strong>cytotoxic (Tc)</strong> cells</td><td>The <strong>immune regulatory</strong> receptors. Found on <strong>macrophages, antigen-presenting cells and B lymphocytes</strong>, and REQUIRED for an APC to bring antigen to a <strong>T helper (CD4)</strong> cell</td></tr>
  </table>
  <p>Each person inherits a unique MHC profile, but it can be <strong>close enough</strong> to
  another's to allow transfusion or transplantation &mdash; which is also the requirement for
  marrow donation in 6.9.</p>
  <p><strong>Clonal selection is the genetic answer to objective 6</strong>, and the order of
  events is the part that catches people:</p>
  <ol>
    <li>Lymphocytes use <strong>more than 500 genes</strong> to build their receptors.</li>
    <li>Undifferentiated lymphocytes divide and mutate continuously in the embryo and fetus,
    generating millions to billions of cell types, <strong>each with a unique receptor</strong>.</li>
    <li>Any clone with a specificity for <strong>self is eliminated</strong> before the fetus is
    harmed. A defect here gives an inherited autoimmune disorder such as <strong>severe combined
    immunodeficiency</strong>.</li>
    <li>The surviving naive pool holds <strong>10<sup>14</sup> to 10<sup>18</sup></strong>
    possible variations &mdash; up to a quintillion &mdash; waiting in lymphatic tissue.</li>
  </ol>
  <div class="callout">
    <p><strong>The point to hold: specificity exists BEFORE the antigen does.</strong> It is
    pre-programmed in the genome. Antigen entry does not instruct a lymphocyte what to recognize
    &mdash; it <strong>selects</strong> the clone that already carries the matching receptor. That
    is what &ldquo;clonal selection&rdquo; names, and getting it backwards is the classic error.</p>
  </div>

  <h3 class="sub" id="si-receptors">6.4 &middot; The two receptors</h3>
  <table class="tbl">
    <tr><th></th><th>B-cell receptor (immunoglobulin)</th><th>T-cell receptor</th></tr>
    <tr><td>Structure</td><td><strong>Four</strong> polypeptide chains &mdash; two identical <strong>heavy</strong>, two identical <strong>light</strong>. Y-shaped</td><td><strong>Two</strong> parallel chains. Relatively small &mdash; equivalent to <strong>one fork</strong> of the Y</td></tr>
    <tr><td>Regions</td><td>Variable and constant</td><td>Variable and constant, formed by genetic recombination</td></tr>
    <tr><td>Secreted?</td><td>Yes &mdash; as antibody</td><td><strong>NEVER</strong></td></tr>
    <tr><td>Recognises</td><td>Free antigen</td><td>Antigen <strong>only when presented with MHC</strong></td></tr>
  </table>
  <p>The variable-region genes are <strong>locked in for the life of the cell and its
  progeny</strong>, including its memory cells. The first receptor on a young B cell is a small
  version of <strong>IgM</strong>; mature B cells carry <strong>IgD</strong>.</p>
  <p><strong>Maturation splits by organ.</strong> B cells are directed by <strong>bone marrow
  stromal cells</strong> and migrate to lymph nodes, spleen and gut-associated lymphoid tissue.
  T cells are directed by the <strong>thymus</strong> and its hormones &mdash; which is why the
  thymus unites the immune and endocrine systems. T-cell receptors are the
  <strong>CD</strong> markers (cluster of differentiation): <strong>CD4 on helper cells, CD8 on
  cytotoxic cells</strong>.</p>

  <h3 class="sub" id="si-antigens">6.5 &middot; Antigens and their special categories</h3>
  <p>An <strong>antigen</strong> is anything provoking a response in specific lymphocytes &mdash;
  it must be perceived as foreign <em>and</em> be big enough to attract attention. The
  <strong>antigenic determinant</strong> or <strong>epitope</strong> is the small molecular group
  actually recognized, and one antigen may carry many.</p>
  <p><strong>Size decides antigenicity.</strong> Foreign cells and complex molecules
  <strong>over 100,000 molecular weight</strong> are the most antigenic, and usually large
  proteins. Molecules <strong>under 1,000</strong> &mdash; <strong>haptens</strong> &mdash; are
  generally not antigenic <em>unless attached to a larger carrier</em>. Drugs, metals and
  industrial chemicals behave this way, which is how an occupational allergy to latex or cleaning
  chemicals arises.</p>
  <table class="tbl">
    <tr><th>Category</th><th>What it is</th><th>Consequence</th></tr>
    <tr><td><strong>Autoantigen</strong></td><td>Self tissue for which tolerance is inadequate</td><td>Accounts for some autoimmune disorders</td></tr>
    <tr><td><strong>Alloantigen</strong></td><td>A surface marker of one individual that is antigenic to <strong>another of the same species</strong></td><td>Gives the <strong>blood groups</strong> and the MHC profile; incompatibility causes transfusion reaction or graft-versus-host disease</td></tr>
    <tr><td><strong>Heterophilic</strong></td><td>Molecules from <strong>unrelated species</strong> with similar determinants</td><td>Mammalian heart muscle and group A streptococcal cell wall may cross react</td></tr>
    <tr><td><strong>Superantigen</strong></td><td>A potent T-cell stimulator</td><td><strong>Cytokine storm</strong> &mdash; staphylococcal toxic shock toxin, enterotoxin</td></tr>
    <tr><td><strong>Allergen</strong></td><td>Any antigen provoking allergy &mdash; <strong>Type I hypersensitivity</strong></td><td>Classified by <strong>portal of entry</strong>: inhaled, ingested, injected, contact</td></tr>
  </table>

  <h3 class="sub" id="si-presentation">6.6 &middot; Objective 7 &mdash; Presentation, and the two interleukins</h3>
  <p>T-cell dependent antigens must be processed by an <strong>antigen-presenting cell</strong>,
  which alters the antigen and attaches it to its <strong>class II MHC</strong> receptor.
  Presentation is a three-way collaboration: <strong>APC, T helper cell, and an antigen-specific
  B or T cell</strong>.</p>
  <div class="callout">
    <p><strong>Two interleukins, two sources, two jobs &mdash; and they are easy to swap.</strong></p>
    <ul>
      <li><strong>Interleukin 1</strong> is secreted <strong>by the APC</strong> to activate the T
      helper cell. It is also an <strong>endogenous pyrogen</strong>, stimulating fever and
      inflammation.</li>
      <li><strong>Interleukin 2</strong> is produced <strong>by the activated T helper cell</strong>
      to activate B cells and other T cells, especially enhancing helper function. <strong>Its
      dysregulation</strong> can contribute to lupus and rheumatoid arthritis.</li>
    </ul>
  </div>
  <p>Once B cells process antigen, interact with helper cells and receive growth and
  differentiation factors, they undergo clonal expansion into <strong>plasma cells</strong>, which
  secrete antibody, and <strong>memory cells</strong> &mdash; which <strong>pause partway through
  mitosis</strong>. That pause is why the secondary response is so much faster.</p>
  <p><strong>The naming.</strong> B-cell responses are <strong>antibody-mediated immunity</strong>
  (or humoral-mediated in older texts); T-cell responses are <strong>cell-mediated
  immunity</strong>.</p>

  <h3 class="sub" id="si-antibodies">6.7 &middot; Objective 4 &mdash; The five immunoglobulins</h3>
  <p><strong>Structure first.</strong> A large Y-shaped protein of four chains. The two identical
  <strong>Fab</strong> ends (antigen-binding fragment) bind antigen; the <strong>Fc</strong> end
  (crystallizable fragment) binds cells of the immune system and allows the molecule to
  <strong>swivel</strong>.</p>
  <table class="tbl">
    <tr><th>Class</th><th>Form</th><th>The thing that separates it</th></tr>
    <tr><td><strong>IgG</strong></td><td>Monomer</td><td><strong>MOST prevalent.</strong> The <strong>ONLY</strong> class crossing the placenta. Responsible for <strong>long-term immunity</strong>. Made in the primary response and in very large titre in secondary responses</td></tr>
    <tr><td><strong>IgA</strong></td><td>Monomer <em>or</em> dimer</td><td><strong>SECOND most prevalent.</strong> Lines mucosal epithelium; free or secretory form in <strong>saliva, tears, colostrum and mucus</strong>. Local immunity against enteric, respiratory and genitourinary pathogens</td></tr>
    <tr><td><strong>IgM</strong></td><td><strong>PENTAMER</strong></td><td><strong>By far the LARGEST</strong>, so <strong>too big to cross the placenta</strong>. <strong>First responder</strong> of the primary response. Important <strong>complement fixer</strong>; binds B cells</td></tr>
    <tr><td><strong>IgD</strong></td><td>Monomer</td><td>High titre in <strong>NEWBORNS</strong>, very low in adults and children. Main function is binding B cells, probably triggering activation and regulation</td></tr>
    <tr><td><strong>IgE</strong></td><td>Monomer</td><td><strong>LEAST common</strong> in serum and the <strong>SHORTEST-LIVED</strong>. Against <strong>allergens and parasitic worms</strong>. Binds <strong>mast cells and basophils</strong>; mediates asthma and anaphylaxis through histamine</td></tr>
  </table>
  <p><strong>Four things antibody does once bound</strong> &mdash; and each has a mechanism worth
  separating:</p>
  <table class="tbl">
    <tr><th>Reaction</th><th>How</th></tr>
    <tr><td><strong>Opsonisation</strong></td><td>Coating the organism so phagocytes can engulf it. Matters most for <strong>slippery envelopes, waxy capsules and slime layers</strong>. The word is Greek &mdash; something cooked with food, a condiment or coating</td></tr>
    <tr><td><strong>Neutralisation</strong></td><td>Blocking a virus's <strong>attachment spike proteins</strong> so it cannot enter a host cell &mdash; which also makes it easier to phagocytose</td></tr>
    <tr><td><strong>Agglutination</strong></td><td><strong>Cross-linking</strong> adjacent cells. The <strong>IgM pentamer, with ten binding sites</strong>, is particularly effective</td></tr>
    <tr><td><strong>Complement fixation</strong></td><td>Antibody binds, leaving sites for complement proteins, which use <strong>perforins</strong> to lyse the envelope. This is objective 8's content in this lecture</td></tr>
  </table>

  <h3 class="sub" id="si-response">6.8 &middot; Objective 5 &mdash; Primary against secondary response</h3>
  <table class="tbl">
    <tr><th>PRIMARY</th><th>SECONDARY</th></tr>
    <tr><td>After first exposure. Produces <strong>IgM and IgG</strong>, with a <strong>gradual</strong> rise in titre. B cells make plasma cells for each, plus <strong>memory B cells</strong></td><td>After a second or later contact. <strong>Rapid and stronger</strong>, because of the memory cells. A much higher titre of <strong>IgG</strong>, followed by gradual <strong>IgM</strong></td></tr>
  </table>
  <p>The secondary response is also called the <strong>anamnestic response</strong>. Titre is
  measured in <strong>binding antibody units (BAU)</strong>, and in a healthy person with robust
  responses it <strong>does not fall to zero</strong> between exposures.</p>
  <p><strong>T cells and cell-mediated immunity.</strong> T cells act directly against antigen and
  foreign cells but <strong>require MHC activation</strong>. All of them produce cytokines;
  sensitized T cells become long-lasting <strong>memory T cells</strong>. Four types:</p>
  <table class="tbl">
    <tr><th>Type</th><th>Marker</th><th>Role</th></tr>
    <tr><td><strong>T helper (TH)</strong></td><td>CD4</td><td>Assists other T and B cells &mdash; the <strong>conductor</strong> of the response</td></tr>
    <tr><td><strong>Cytotoxic (TC)</strong></td><td>CD8</td><td>Secretes enzymes that <strong>lyse</strong> cells &mdash; especially virally infected cells, cancer cells, and cells from other humans and animals</td></tr>
    <tr><td><strong>Delayed hypersensitivity (TD)</strong></td><td>&mdash;</td><td>Allergy appearing <strong>hours or days</strong> after contact, or after accumulated contact</td></tr>
    <tr><td><strong>T suppressor (TS)</strong></td><td>&mdash;</td><td><strong>Limits</strong> the actions of other T and B cells</td></tr>
  </table>

  <h3 class="sub" id="si-applications">6.9 &middot; The applications</h3>
  <p><strong>Passive immunization (immunotherapy)</strong> gives short-term protection &mdash; on
  the order of <strong>two to three months</strong>. Early use transfused <strong>horse
  serum</strong> antitoxins for tetanus and diphtheria; horse sera are still sometimes used for
  diphtheria, botulism and spider or snake bites, with <strong>serum sickness or
  anaphylaxis</strong> as the risks. Current <strong>pooled gamma globulin</strong> is used for
  hepatitis A and B, HIV, measles and generally immunodeficient patients.
  <strong>Convalescent plasma</strong> and monoclonal antibodies have a role in viral infection.</p>
  <div class="callout">
    <p><strong>The monoclonal antibody endings are free marks, because the name tells you the
    source.</strong></p>
    <ul>
      <li><strong>-mab</strong> &mdash; monoclonal antibody (a protein)</li>
      <li><strong>-omab</strong> &mdash; <strong>mouse</strong></li>
      <li><strong>-ximab</strong> &mdash; <strong>chimeric</strong></li>
      <li><strong>-zumab</strong> &mdash; <strong>humanised</strong></li>
      <li><strong>-umab</strong> &mdash; entirely <strong>human</strong></li>
    </ul>
    <p>Two examples: <strong>adalimumab</strong> for rheumatoid and psoriatic arthritis, Crohn
    disease and plaque psoriasis; <strong>pembrolizumab</strong> for melanoma and lung cancer.</p>
  </div>
  <p><strong>Vaccination</strong> is deliberate exposure to material that is <strong>antigenic but
  NOT pathogenic</strong>. The practice reached England through <strong>Lady Montagu</strong>; the
  first effective human vaccination was <strong>Jenner's</strong>, using cowpox against smallpox;
  <strong>Pasteur</strong> later developed one against rabies.</p>
  <p><strong>An effective vaccine should</strong> have low toxicity, protect against exposure,
  stimulate <strong>BOTH</strong> antibody-mediated and cell-mediated responses, produce lasting
  <strong>memory B and T cells</strong>, generally not need numerous doses or boosters, and be
  inexpensive, easy to give and long-lived on the shelf. A <strong>sterilizing vaccine</strong>
  &mdash; one leaving the target non-functioning and unable to mutate &mdash; would be best of all.</p>
  <p><strong>Most vaccines contain</strong> killed whole cells or inactivated viruses; live
  attenuated organisms; acellular or subunit antigens; <strong>toxoids</strong> from purified
  antigenic components; or genetically engineered organisms or antigens.</p>
  <p><strong>Marrow and stem cell donation</strong> requires a close <strong>class I MHC
  match</strong> plus further DNA compatibility testing. Marrow is harvested from the
  <strong>sternum, femur or iliac crest</strong>; circulating peripheral stem cells are collected
  by <strong>apheresis</strong> after a mobilizing drug. The recipient receives drug and radiation
  therapy beforehand <strong>to reduce the risk of rejecting the donor cells</strong>.</p>

  <button type="button" class="test-yourself-btn" onclick="window.openTestYourself('Test yourself &mdash; The Acquisition of Specific Immunity', TEST_YOURSELF.specificimmunity)">Test yourself! &rarr;</button>
</section>
"""

TOC = """  <a class="top-link" href="#specific-immunity">6 &middot; The Acquisition of Specific Immunity</a>
  <a class="sub-link" href="#si-acquired">6.1 The four kinds of acquired immunity</a>
  <a class="sub-link" href="#si-leukocytes">6.2 The leukocytes, in order</a>
  <a class="sub-link" href="#si-mhc">6.3 MHC &amp; the genetics of self</a>
  <a class="sub-link" href="#si-receptors">6.4 The two receptors</a>
  <a class="sub-link" href="#si-antigens">6.5 Antigens &amp; their categories</a>
  <a class="sub-link" href="#si-presentation">6.6 Presentation &amp; the interleukins</a>
  <a class="sub-link" href="#si-antibodies">6.7 The five immunoglobulins</a>
  <a class="sub-link" href="#si-response">6.8 Primary vs secondary response</a>
  <a class="sub-link" href="#si-applications">6.9 The applications</a>
"""

TEST = """    specificimmunity: [
      {q:"A patient recovers from an asymptomatic infection and is resistant to it. Which immunity?",
       o:["Natural active","Natural passive","Artificial active","Artificial passive"],a:0,
       why:"Active means they made it themselves; natural means it came from infection rather than a needle."},
      {q:"What proportion of natural passive immunity is acquired IN UTERO?",
       o:["About 99 percent","About half","About 10 percent","None — it all comes from milk"],a:0,
       why:"Nursing adds beneficial microbes and antibody the placenta cannot pass, but the bulk arrives before birth."},
      {q:"Which cells lack MHC receptors?",
       o:["Red blood cells","Macrophages","B lymphocytes","Neutrophils"],a:0,
       why:"MHC is on all cells EXCEPT erythrocytes, and its genes sit on chromosome 6."},
      {q:"Which MHC class must an antigen-presenting cell use to activate a T helper cell?",
       o:["Class II","Class I","Class III","Either class works"],a:0,
       why:"Class I is what cytotoxic T cells read. Class II is the immune regulatory receptor, on macrophages, APCs and B cells."},
      {q:"When is lymphocyte specificity determined?",
       o:["BEFORE any antigen arrives — it is pre-programmed genetically",
          "When the antigen instructs the cell","At puberty","On the second exposure"],a:0,
       why:"Antigen SELECTS a clone that already exists. Getting this backwards is the classic error about clonal selection."},
      {q:"What happens to lymphocyte clones specific for SELF?",
       o:["They are eliminated before the fetus is harmed","They become memory cells",
          "They migrate to the thymus","They become plasma cells"],a:0,
       why:"A defect here gives an inherited autoimmune disorder such as severe combined immunodeficiency."},
      {q:"How does the T-cell receptor differ from the B-cell receptor?",
       o:["Two chains, small, and NEVER secreted","Four chains, and secreted as antibody",
          "Identical to it","One chain, and secreted"],a:0,
       why:"It is equivalent to one fork of the Y, and it needs MHC presentation where the B-cell receptor binds free antigen."},
      {q:"What is a HAPTEN?",
       o:["A molecule under 1,000 molecular weight, antigenic only on a carrier",
          "A molecule over 100,000 molecular weight","A fragment of antibody","A self molecule escaping tolerance"],a:0,
       why:"Drugs, metals and industrial chemicals behave this way — which is how occupational latex allergy arises."},
      {q:"Which antigen category causes a CYTOKINE STORM?",
       o:["Superantigen","Autoantigen","Alloantigen","Heterophilic antigen"],a:0,
       why:"Staphylococcal toxins such as toxic shock syndrome toxin and enterotoxin."},
      {q:"Which interleukin does the APC secrete, and what else does it do?",
       o:["Interleukin 1 — an endogenous pyrogen causing fever","Interleukin 2 — a pyrogen",
          "Interferon gamma","Interleukin 6"],a:0,
       why:"Interleukin 2 comes from the ACTIVATED helper cell. Swapping these two is the easy mistake here."},
      {q:"Which immunoglobulin is most prevalent AND the only one crossing the placenta?",
       o:["IgG","IgA","IgM","IgE"],a:0,
       why:"IgM is too big to cross — it is a pentamer. IgA is second most prevalent but secretory."},
      {q:"Which immunoglobulin is a pentamer, and what follows from it?",
       o:["IgM — largest, too big for the placenta, ten binding sites","IgG — largest","IgA — largest","IgE — largest"],a:0,
       why:"Those ten binding sites are why it is the best agglutinator, and it is the first responder of the primary response."},
      {q:"Which immunoglobulin is LEAST common in serum and shortest-lived?",
       o:["IgE","IgD","IgM","IgA"],a:0,
       why:"It binds mast cells and basophils, mediating asthma and anaphylaxis through histamine."},
      {q:"What makes the SECONDARY response faster and stronger?",
       o:["Memory cells, which paused partway through mitosis","A larger antigen dose",
          "Innate immunity taking over","Earlier complement activation"],a:0,
       why:"It produces a much higher titre of IgG followed by gradual IgM, and is also called the anamnestic response."},
      {q:"Which T cell limits the actions of other T and B cells?",
       o:["The T suppressor cell","The cytotoxic T cell","The T helper cell","The delayed hypersensitivity cell"],a:0,
       why:"Four types: helper (CD4) conducts, cytotoxic (CD8) lyses, delayed hypersensitivity causes late allergy, suppressor limits."},
      {q:"What does the ending -zumab signify?",
       o:["Humanized protein","Mouse protein","Chimeric protein","Entirely human protein"],a:0,
       why:"-omab is mouse, -ximab chimeric, -zumab humanized, -umab entirely human."},
      {q:"What match is required for marrow donation?",
       o:["A close class I MHC match, plus DNA compatibility testing","A class II MHC match only",
          "ABO compatibility alone","No match is needed"],a:0,
       why:"Marrow comes from the sternum, femur or iliac crest; peripheral stem cells by apheresis after a mobilizing drug."},
      {q:"Which responses should an effective vaccine stimulate?",
       o:["BOTH antibody-mediated and cell-mediated","Antibody-mediated only",
          "Cell-mediated only","Innate only"],a:0,
       why:"And it should produce memory B and T cells, with few doses, low toxicity and a long shelf-life."}
    ],
"""
