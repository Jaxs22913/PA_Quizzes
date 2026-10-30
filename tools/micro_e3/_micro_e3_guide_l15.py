# -*- coding: utf-8 -*-
"""Section 15 of the Microbiology Exam 3 guide -- Fungi of Medical Importance (Dr. Fair).

Same shape as _micro_e3_guide_l14.py (FIG, DECK, IMAGES, extract(), fig(), TOC, SECTION, TEST):
tools/build_micro_e3_guide.py imports it, calls extract() for the figures and splices TOC, SECTION and TEST.

Attribution: Dr. Fair. The title slide names no lecturer (a cartoon and the title only); the deck file is
"PAJ5200.Fungi of Medical importance.pptx", her PAJ5200.* naming, its file properties name Dianne Fair as author
and last editor, and the calendar row for 30 October 2026 (1-3 pm, Lecture 15) names Dr. Fair. The recording
(Phase 2) confirms or corrects this.

Instructional objectives are VERBATIM from the syllabus (Micro.pdf, page 5): the two numbered objectives under
"Fungi of Medical Importance", which points to Appendix 2's list of seven organisms (page 9: Candida, Aspergillus,
Cryptococcus, Histoplasma, Blastomyces, Coccidioides, Paracoccidioides). The deck's objective slide (slide 3)
matches. Objective 1 is answered topic by topic (15.1-15.21); objective 2 is drawn together in 15.22.

Content is from the VISIBLE slides only, text and pictures; speaker notes do not count (slide 10's WHO link and
slide 18's 18S ribonucleic acid note are notes and are left out). Every picture was viewed at full size,
including the picture-only slides that carry content: 6 (the dimorphism cycle), 9 (Table 22.3), 13/25/29/32/36
(one distribution map, shown once), 17 (the identification flowchart), 18 (stains), 23 (levels of invasion), 28
(the Histoplasma cycle) and 31 (the Coccidioides cycle). Slides 1, 2, 8, 21 and 46 are jokes, a meme, a television
still and a television commercial: no content.

PHASE 1 (30 October 2026): built from the slides while the lecture was being recorded. The MICROL15AUDIO block
is the placeholder the audio pass replaces.
"""
import io, os

FIG = "micro-exam-3-study-guide-images"
DECK = "PAJ5200.Fungi of Medical importance.pptx"
INBOX_DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Microbiology Inbox/Exam 3/" + DECK)

# (slide, picture index on that slide in shape-tree order counting group members and placeholder pictures,
# published file name). Slide 61 holds two pictures: picture 1 is the eye and brain sections, picture 2 a chest
# X-ray. A .jpg name for a PNG blob (or a JPEG over 250 KB or over 900 px wide) means re-encoded as JPEG, quality
# 85, at most 900 px wide.
IMAGES = [
    (6, 1, "l15-s006-thermal-dimorphism.jpg"),
    (9, 1, "l15-s009-opportunists-table.jpg"),
    (13, 1, "l15-s013-true-pathogen-map.jpg"),
    (17, 1, "l15-s017-identifying-isolates.jpg"),
    (18, 1, "l15-s018-fungal-stains.jpg"),
    (23, 1, "l15-s023-levels-of-invasion.jpg"),
    (27, 1, "l15-s027-histoplasma-colonies.jpg"),
    (28, 1, "l15-s028-histoplasma-cycle.jpg"),
    (31, 1, "l15-s031-coccidioides-cycle.jpg"),
    (34, 1, "l15-s034-blastomyces-dimorphism.jpg"),
    (35, 1, "l15-s035-cutaneous-blastomycosis.jpg"),
    (40, 1, "l15-s040-sporothrix.jpg"),
    (41, 1, "l15-s041-lymphocutaneous-sporotrichosis.jpg"),
    (47, 1, "l15-s047-tinea-scalp-body.jpg"),
    (48, 1, "l15-s048-tinea-extremities.jpg"),
    (50, 1, "l15-s050-piedra.jpg"),
    (54, 1, "l15-s054-candidiasis.jpg"),
    (59, 1, "l15-s059-pneumocystis.jpg"),
    (61, 1, "l15-s061-aspergillosis.jpg"),
    (62, 1, "l15-s062-aspergillus.jpg"),
]
MAXW = 900


def _pictures(shapes):
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from _pictures(sh.shapes)
            continue
        try:
            sh.image
        except Exception:
            continue
        yield sh


def extract(imgdir):
    """Write IMAGES into imgdir from the deck (pictures, picture placeholders and grouped pictures)."""
    from pptx import Presentation
    from PIL import Image
    prs = Presentation(INBOX_DECK)
    os.makedirs(imgdir, exist_ok=True)
    for slide, k, name in IMAGES:
        pics = list(_pictures(prs.slides[slide - 1].shapes))
        assert len(pics) >= k, "%s slide %d has %d picture(s)" % (DECK, slide, len(pics))
        img = pics[k - 1].image
        ext = img.ext.replace("jpeg", "jpg")
        out = os.path.join(imgdir, name)
        if name.endswith(".jpg") and (ext != "jpg" or len(img.blob) > 250 * 1024
                                      or Image.open(io.BytesIO(img.blob)).width > MAXW):
            im = Image.open(io.BytesIO(img.blob)).convert("RGB")
            if im.width > MAXW:
                im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
            im.save(out, quality=85)
        else:
            assert name.endswith("." + ext), (name, ext)
            open(out, "wb").write(img.blob)
    return len(IMAGES)


def fig(name, w, h, alt, cap, slide, credit=""):
    note = (credit + " ") if credit else ""
    return ('<figure class="fig"><img width="%d" height="%d" loading="lazy" src="%s/%s" alt="%s">'
            '<figcaption>%s <span class="src">%sSource: %s, Slide %d.</span></figcaption></figure>'
            % (w, h, FIG, name, alt, cap, note, DECK, slide))


MH = "Copyright &copy; The McGraw-Hill Companies."

TOC = """
  <a class="top-link" href="#fungi">15 &middot; Fungi of Medical Importance</a>
  <a class="sub-link" href="#fun-audio">&#9733; What the recording adds</a>
  <a class="sub-link" href="#fun-pathogens">15.1 Objective 1 &mdash; True and opportunistic fungal pathogens</a>
  <a class="sub-link" href="#fun-dimorphism">15.2 Objective 1 &mdash; Thermal dimorphism</a>
  <a class="sub-link" href="#fun-who">15.3 Objective 1 &mdash; The fungal priority pathogens list</a>
  <a class="sub-link" href="#fun-epi">15.4 Objective 1 &mdash; Epidemiology, pathogenesis and host defense</a>
  <a class="sub-link" href="#fun-diagnosis">15.5 Objective 1 &mdash; Diagnosis</a>
  <a class="sub-link" href="#fun-control">15.6 Objective 1 &mdash; Control and amphotericin B</a>
  <a class="sub-link" href="#fun-systemic">15.7 Objective 1 &mdash; Systemic mycoses: the true fungal pathogens</a>
  <a class="sub-link" href="#fun-histo">15.8 Objective 1 &mdash; <em>Histoplasma capsulatum</em></a>
  <a class="sub-link" href="#fun-cocci">15.9 Objective 1 &mdash; <em>Coccidioides immitis</em></a>
  <a class="sub-link" href="#fun-blasto">15.10 Objective 1 &mdash; <em>Blastomyces dermatitidis</em></a>
  <a class="sub-link" href="#fun-paracocci">15.11 Objective 1 &mdash; <em>Paracoccidioides brasiliensis</em></a>
  <a class="sub-link" href="#fun-sporothrix">15.12 Objective 1 &mdash; Subcutaneous mycoses: <em>Sporothrix</em></a>
  <a class="sub-link" href="#fun-dermatophytes">15.13 Objective 1 &mdash; Cutaneous mycoses: the dermatophytes</a>
  <a class="sub-link" href="#fun-superficial">15.14 Objective 1 &mdash; Superficial mycoses</a>
  <a class="sub-link" href="#fun-opportunists">15.15 Objective 1 &mdash; The opportunistic mycoses</a>
  <a class="sub-link" href="#fun-candida">15.16 Objective 1 &mdash; <em>Candida</em> and candidiasis</a>
  <a class="sub-link" href="#fun-crypto">15.17 Objective 1 &mdash; <em>Cryptococcus neoformans</em></a>
  <a class="sub-link" href="#fun-pneumocystis">15.18 Objective 1 &mdash; <em>Pneumocystis jirovecii</em></a>
  <a class="sub-link" href="#fun-aspergillus">15.19 Objective 1 &mdash; <em>Aspergillus</em> and aspergillosis</a>
  <a class="sub-link" href="#fun-mucor">15.20 Objective 1 &mdash; Mucormycosis and other opportunists</a>
  <a class="sub-link" href="#fun-toxins">15.21 Objective 1 &mdash; Fungal allergies and mycotoxins</a>
  <a class="sub-link" href="#fun-transmission">15.22 Objective 2 &mdash; Modes of transmission</a>
  <a class="sub-link" href="#fun-notes">15.23 Where the slides disagree, and where current practice differs</a>
"""

SECTION_HEAD = """
<section class="deck" id="fungi">
  <h2 class="deck-title">15 &middot; Fungi of Medical Importance</h2>
  <p class="lecturer">Dr. Fair &middot; Lecture 15 &middot; 30 October 2026</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases,
      clinical manifestations, methods of treatment, and prevention of fungi of medical importance.</li>
      <li>Describe the modes of transmission by which humans acquire fungi of medical importance.</li>
    </ol>
  </div>

  <div class="callout"><strong>Two questions sort every fungus here.</strong> <em>Can it infect a healthy
  person?</em> If yes it is a <strong>true (primary) pathogen</strong>, and the four true pathogens
  (<em>Histoplasma</em>, <em>Coccidioides</em>, <em>Blastomyces</em>, <em>Paracoccidioides</em>) are
  <strong>thermally dimorphic</strong>: a mold in the soil, a yeast in the body. If no, it is an
  <strong>opportunist</strong> that needs impaired defenses (<em>Candida</em>, <em>Aspergillus</em>,
  <em>Cryptococcus</em>, <em>Pneumocystis</em>, the Zygomycota, <em>Fusarium</em>). <em>How deep does it
  go?</em> Systemic (inhaled spores, lungs first), subcutaneous (a puncture wound: <em>Sporothrix</em>),
  cutaneous (keratin only: the dermatophytes and the tineas) or superficial (the hair or the top of the skin: tinea
  versicolor and the piedras). The syllabus points to its Appendix 2 list of seven organisms for this lecture:
  <em>Candida</em>, <em>Aspergillus</em>, <em>Cryptococcus</em>, <em>Histoplasma</em>, <em>Blastomyces</em>,
  <em>Coccidioides</em> and <em>Paracoccidioides</em>. Objective 1 is answered topic by topic; objective 2 (how
  people acquire each one) is drawn together in 15.22.</div>

<!--MICROL15AUDIO-->
  <div class="prof-flag" id="fun-audio"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 30 October 2026</span>
  <p><b>Not read yet.</b> This lecture was recorded on 30 October and the recording is being transcribed (ours,
  plus Notability&rsquo;s own transcript as a second opinion). Until it has been read, this section is built from
  the slides alone: the quizzes are weighted by slide count, and the only emphasis marked is the slides&rsquo; own
  (&ldquo;Focus on the Latin names for each body part/region&rdquo; on slide 43, 15.13). When the recording has been
  read, this box will carry what Dr. Fair stressed, what she said to skip, and any correction of a slide.</p>
  </div>
<!--/MICROL15AUDIO-->
"""

BODY = """
  <h3 class="sub" id="fun-pathogens">15.1 &middot; Objective 1 &mdash; True and opportunistic fungal pathogens</h3>
  <p><strong>Molds and yeasts are widely distributed</strong> in air, dust, fomites and the normal flora of humans,
  plants and animals. <strong>Humans are relatively resistant to fungal infections as long as the immune system is
  competent</strong>; immunocompromised status is the serious consideration throughout this lecture. Fungi are
  <strong>relatively nonpathogenic</strong>: of about 100,000 fungal species only about 300 (0.3%) have been linked
  to disease in humans and animals. But fungi are the <strong>most common plant pathogens</strong> (potato blights,
  infected grape crops and fruit trees), which can cause huge socio-economic losses such as the potato famines in
  Ireland and Eastern Europe. <strong>Human mycoses</strong> (&ldquo;myco&rdquo; = fungi) are caused by true fungal
  pathogens and by opportunistic pathogens.</p>
  <table>
    <tr><th>Kind of pathogen</th><th>Definition</th><th>Key adaptation</th><th>Levels of disease</th><th>Immunity afterwards</th></tr>
    <tr><td><strong>True (primary) fungal pathogen</strong></td><td>Can <strong>invade and grow in a healthy host</strong></td><td><strong>Switching from hyphal cells to yeast cells</strong> (multicellular to unicellular) with temperature: <strong>thermal dimorphism</strong> (15.2)</td><td>May cause <strong>systemic, subcutaneous, cutaneous and superficial</strong> mycoses</td><td>Long-term immunity can develop against a few true fungal pathogens</td></tr>
    <tr><td><strong>Opportunistic fungal pathogen</strong></td><td>Has <strong>little or no virulence of its own</strong>; the host defenses must be impaired (human immunodeficiency virus infection, cancer, diabetes, chronic obstructive pulmonary disease, autoimmune disorder, nosocomial infection)</td><td>Few, if any, virulence factors; infection usually starts in an immunocompromised host. Consider predisposing factors: primary illness, corticosteroids, diabetes, cancer</td><td>From superficial colonization of external tissues to potentially fatal systemic disease of one or more organ systems</td><td><strong>Reinfection is highly likely</strong> (think of recurring vaginal yeast infection or foot fungus)</td></tr>
  </table>
  <p><strong>An emerging medical concern.</strong> Mycoses account for about 10% of all nosocomial infections, and
  the proportion is rising. <strong>Dermatophytes</strong> (residents of human and animal skin) may be undergoing a
  gradual transformation to become true pathogens.</p>

  <h3 class="sub" id="fun-dimorphism">15.2 &middot; Objective 1 &mdash; Thermal dimorphism</h3>
  <p>The most striking adaptation of a true pathogen to survival and growth in the human host is the ability to
  switch from hyphal cells to yeast cells, from multicellular to unicellular forms, with the corresponding change in
  temperature. <strong>Thermal dimorphism: the fungus grows as a mold (multicellular) at 30&nbsp;&deg;C and as a
  yeast (unicellular) at 37&nbsp;&deg;C, which is human body temperature.</strong></p>
  """ + fig("l15-s006-thermal-dimorphism.jpg", 800, 523,
      "A cycle diagram: on the left, the natural habitat with hyphae and spores and a photograph of fuzzy hyphal colonies; on the right, the animal habitat with spores budding into yeast cells and a photograph of smooth yeast colonies; arrows marked with temperature, oxygen and nutrient changes link the two halves.",
      "<b>Two habitats, two forms.</b> Natural habitat: <b>saprobic (free-living), mycelial phase, below "
      "30&nbsp;&deg;C, reproduces by sporulation</b>. Animal habitat: <b>parasitic, yeast phase, "
      "35&ndash;40&nbsp;&deg;C, reproduces by budding or endospores</b>. (1) Spores that enter a warm-blooded animal "
      "(increased temperature, reduced oxygen, suboptimal nutrients) germinate into yeasts and stay yeasts in the "
      "host. (2) Yeast cells that leave the host (decreased temperature, optimal oxygen, improved nutrients) revert "
      "to the sporulating hyphal state; these conversions can be shown on artificial media in the laboratory.",
      6, MH) + """
  """ + fig("l15-s027-histoplasma-colonies.jpg", 900, 362,
      "Two colonies side by side: on the left a fuzzy, tan, spreading colony; on the right a smooth, wrinkled, cream colony.",
      "<b>The same fungus at two temperatures.</b> <em>Histoplasma capsulatum</em> grown below 35&nbsp;&deg;C "
      "(left, the mold) and at 37&nbsp;&deg;C (right, the yeast).", 27,
      "&copy; Elmer W. Koneman/Visuals Unlimited. " + MH) + """

  <h3 class="sub" id="fun-who">15.3 &middot; Objective 1 &mdash; The fungal priority pathogens list</h3>
  <p>The World Health Organization announced its first-ever <strong>fungal priority pathogens list</strong> in
  October 2022, to complement its bacterial priority pathogens list of 2017. Worldwide, drug-resistant bacteria
  directly cause over 1 million deaths a year and contribute to another 5 million; <strong>drug-resistant fungi are
  rapidly becoming a concern</strong>. With closer attention to nosocomial and secondary infections,
  <strong>invasive fungal diseases have been found to be increasing, especially among immunocompromised
  populations</strong>. The catch: fungal infections get <strong>little attention compared with bacterial or viral
  infections</strong>, and so less money for research and development (detection, diagnosis, treatment, new
  drugs).</p>
  <table>
    <tr><th>Priority</th><th>Fungi on the list</th></tr>
    <tr><td><strong>Critical</strong></td><td><em>Cryptococcus neoformans</em> (&ldquo;the number one critical fungal pathogen&rdquo;, slide 56), <em>Aspergillus fumigatus</em> (number three, slide 60), <em>Candida albicans</em>, <em>Candida auris</em></td></tr>
    <tr><td><strong>High</strong></td><td>Other <em>Candida</em> species, eumycetoma causative agents, <em>Fusarium</em> species, <em>Histoplasma</em> species, Mucorales (mucormycosis opportunists)</td></tr>
    <tr><td><strong>Medium</strong></td><td><em>Coccidioides</em>, <em>Cryptococcus gattii</em>, <em>Pneumocystis jirovecii</em>, <em>Paracoccidioides</em> species</td></tr>
  </table>

  <h3 class="sub" id="fun-epi">15.4 &middot; Objective 1 &mdash; Epidemiology, pathogenesis and host defense</h3>
  <ul>
    <li><strong>Most fungal pathogens do not require a host</strong> to complete their life cycles, and these
    infections are <strong>generally not communicable</strong> to other persons.</li>
    <li>The exceptions: <strong>dermatophytes</strong> (literally &ldquo;skin plants&rdquo;) and <strong><em>Candida</em>
    species</strong> naturally inhabit the human body and <strong>are transmissible from person to person</strong>,
    or by fomites such as shared exercise equipment.</li>
    <li><strong>True fungal pathogens are distributed in predictable geographical patterns</strong>, coinciding with
    climate and soil requirements (the map in 15.7).</li>
    <li><strong>Dermatophytoses are the most prevalent fungal diseases</strong>, and many cases go undiagnosed or are
    misdiagnosed (for example as skin-related allergies or autoimmune disorders).</li>
  </ul>
  <table>
    <tr><th>Type of mycosis</th><th>Portal of entry (slide 14)</th></tr>
    <tr><td>Primary (systemic) mycoses</td><td><strong>Respiratory</strong>: spores inhaled from the air</td></tr>
    <tr><td>Subcutaneous</td><td><strong>Inoculated</strong> into skin or nails: <strong>trauma</strong></td></tr>
    <tr><td>Cutaneous and superficial</td><td><strong>Contamination</strong> of the skin or hair surface</td></tr>
  </table>
  <p><strong>Virulence factors</strong>: thermal dimorphism, toxin-like substances, capsules and adhesion factors,
  hydrolytic enzymes, inflammatory stimulants.</p>
  """ + fig("l15-s023-levels-of-invasion.jpg", 900, 652,
      "Left, a human figure with lungs, kidneys, bladder and brain and arrows spreading from the lungs; right, a block of skin labeled epidermis, stratum corneum, dermis and subcutaneous tissue, with a depth bar colored green for superficial, pink for cutaneous and blue for subcutaneous.",
      "<b>Levels of invasion.</b> (a) In <b>systemic (deep) mycoses</b> the fungus disseminates from the lungs or "
      "other sites into the circulation; fungemia leads to infection of the brain, kidneys and other organs. (b) "
      "<b>Superficial</b>: extremely shallow epidermal colonization. <b>Cutaneous</b>: the stratum corneum and "
      "occasionally the upper dermis. <b>Subcutaneous</b>: after a puncture wound has introduced the fungus deeper, "
      "into the subcutaneous tissues.", 23, MH) + """
  <h4 class="subsub">Host defense</h4>
  <p>The main antifungal defenses are the <strong>integrity of the skin, mucous membranes and intact respiratory
  cilia</strong>. The <strong>most important defenses are cell-mediated immunity</strong> (T cells and their
  cytokines), <strong>phagocytosis and inflammation</strong>. <strong>Long-term immunity can develop against only a
  few true fungal pathogens, not the opportunists: reinfection is highly likely with opportunistic
  fungi</strong> (the repeated &ldquo;episodes&rdquo; of vaginal yeast infection or foot fungus).</p>

  <h3 class="sub" id="fun-diagnosis">15.5 &middot; Objective 1 &mdash; Diagnosis</h3>
  <p>Diagnosis and identification need <strong>microscopic examination of stained specimens, culture on selective
  and enriched media, and specific biochemical or serological tests</strong>. <strong>Sabouraud dextrose agar</strong>
  is commonly used, with chemicals added to inhibit bacterial growth; its <strong>fairly low pH inhibits most
  bacteria, but not fungi</strong>.</p>
  """ + fig("l15-s017-identifying-isolates.jpg", 900, 864,
      "A four-column flowchart of specimen processing for fungi: sputum; blood, cerebrospinal fluid, pus and vaginal secretions; hair, skin and nails; tissue biopsies and punches, each branching through stains, mounts, culture temperatures and tests.",
      "<b>Identifying fungal isolates (the flowchart).</b> <b>Sputum</b>: digested to remove debris; negative stain "
      "for a capsule, potassium hydroxide wet mount, special stains and brighteners; culture for up to 8 weeks on "
      "selective agar at room temperature (25 or 30&nbsp;&deg;C) and blood agar at 37&nbsp;&deg;C to "
      "<b>demonstrate dimorphism</b>; then differential media, biochemical and antigen tests or animal inoculation. "
      "<b>Blood, cerebrospinal fluid, pus, vaginal secretions</b>: potassium hydroxide mount, negative stain for a "
      "capsule, direct stains; culture at 25 or 30&nbsp;&deg;C on selective media and 37&nbsp;&deg;C on brain heart "
      "infusion or blood agar; then differential media, biochemical and antigen tests, the <b>germ tube test</b>, "
      "genetic probes, serological tests. <b>Hair, skin, nails</b>: <b>Wood&rsquo;s light on hairs</b>, hot "
      "potassium hydroxide wet mount, brighteners, periodic acid-Schiff stain; implant on selective media and "
      "incubate for 4 weeks; hair infection test with sterile hair. <b>Tissue biopsies</b>: histological stains; "
      "culture at 25&ndash;37&nbsp;&deg;C and at 37&nbsp;&deg;C to test for dimorphism; specific nucleic acid "
      "probe. Footnotes: animal inoculation is done only to help diagnose systemic mycoses when other methods are "
      "unavailable or indeterminate; some yeasts, incubated in serum for 2&ndash;4 hours, sprout tiny hyphal tubes "
      "called <b>germ tubes</b>.", 17, MH) + """
  """ + fig("l15-s018-fungal-stains.jpg", 470, 900,
      "Two fluorescence micrographs: above, a bright blue-green tangle of branched filaments; below, a green yeast cell sprouting a long, thin tube.",
      "<b>Dyes amplify fungal elements.</b> Above, <em>Aspergillus</em> from a sputum specimen: <b>branched septate "
      "hyphae</b>. Below, <b>germinating <em>Candida albicans</em></b>: a young hypha growing from a germinating "
      "yeast (an oral or vaginal swab could give this). Treating such a slide with dilute <b>potassium hydroxide "
      "lyses the human epithelial cells</b> and leaves the fungal cells intact, because <b>fungi have a thicker cell "
      "wall</b> that human cells lack.", 18, MH) + """

  <h3 class="sub" id="fun-control">15.6 &middot; Objective 1 &mdash; Control and amphotericin B</h3>
  <ul>
    <li><strong>Immunization is typically ineffective</strong> for preventing fungal infections, <strong>because
    reinfection is exceedingly common</strong>.</li>
    <li><strong>Antifungal drugs</strong>: amphotericin B, flucytosine, azoles and nystatin.</li>
    <li>In some cases <strong>surgical removal of damaged tissue</strong> is necessary.</li>
    <li><strong>Prevention</strong> is essentially limited to <strong>high-quality respirator masks and protective
    clothing and hygiene</strong>, to reduce contact with fungal spores.</li>
  </ul>
  <table>
    <tr><th>Amphotericin B</th><th>Slide 20</th></tr>
    <tr><td>Standing</td><td>The <strong>drug of choice for many fungal infections</strong>: highly toxic and often expensive</td></tr>
    <tr><td>Source</td><td>Produced by a <strong>soil bacterium of the genus <em>Streptomyces</em></strong>; it attacks fungal cells, which are eukaryotic</td></tr>
    <tr><td>Mechanism</td><td><strong>Forms complexes with fungal cell membrane lipids</strong>, causing openings and seepage of cytoplasmic ions</td></tr>
    <tr><td>Why it is toxic</td><td>Not selective enough to attack only fungi: <strong>fungi and humans are both eukaryotes</strong></td></tr>
    <tr><td>Side effects</td><td><strong>Fatigue, weakness, fever and arrhythmia</strong>; sometimes known as <strong>&ldquo;ampho-terrible&rdquo;</strong></td></tr>
    <tr><td>Routes</td><td>Called versatile on the slide (topical, oral, intramuscular or intravenous; see 15.23)</td></tr>
  </table>

  <h3 class="sub" id="fun-systemic">15.7 &middot; Objective 1 &mdash; Systemic mycoses: the true fungal pathogens</h3>
  <p>Mycoses are organized by <strong>type, level of infection and degree of pathogenicity</strong> (15.1). The
  systemic infections of the true pathogens share a pattern (slide 24):</p>
  <ul>
    <li>Each true fungal pathogen is <strong>restricted to certain endemic regions</strong> of the world.</li>
    <li>Infection occurs when <strong>soil or other matter (such as animal waste) containing the conidia is
    disturbed</strong>.</li>
    <li>The <strong>spores germinate in the lungs, producing yeast or yeast-like cells</strong>: thermal dimorphism
    at work.</li>
    <li>Infection can become <strong>systemic</strong> in some hosts; spores may also be <strong>inoculated into broken
    skin</strong>.</li>
    <li>The diseases of the true fungal pathogens <strong>can result in immunity in a competent host</strong>.</li>
  </ul>
  """ + fig("l15-s013-true-pathogen-map.jpg", 785, 600,
      "Map of the Americas and Africa with four colored zones: blue dots for Histoplasma across the eastern and central United States, parts of Central and South America and a wide band of central Africa; yellow for Blastomyces over the midwestern and southeastern United States into Canada; green for Coccidioides in the southwestern United States and Mexico with a few South American spots; pink for Paracoccidioides across Central and South America.",
      "<b>Where the four true fungal pathogens live</b> (shown on slides 13, 25, 29, 32 and 36). Blue,"
      " <em>Histoplasma</em>: eastern and central United States, Latin America and Africa. Yellow, "
      "<em>Blastomyces</em>: midwestern and southeastern United States and southern Canada. Green, "
      "<em>Coccidioides</em>: the southwestern United States and Mexico. Pink, <em>Paracoccidioides</em>: Central "
      "and South America.", 13, MH) + """
  <table>
    <tr><th>Pathogen</th><th>Disease (nickname)</th><th>Where</th><th>Soil</th><th>Signature</th><th>Treatment on the slide</th></tr>
    <tr><td><strong><em>Histoplasma capsulatum</em></strong></td><td>Histoplasmosis, &ldquo;Ohio Valley fever&rdquo;</td><td>Eastern and central United States; worldwide; Latin America, Africa</td><td>Moist, high-nitrogen soil, <strong>bird and bat guano</strong></td><td>The <strong>most common</strong> true fungal pathogen; <strong>not</strong> person to person</td><td>Amphotericin B and azoles</td></tr>
    <tr><td><strong><em>Coccidioides immitis</em></strong></td><td>Coccidioidomycosis, &ldquo;Valley fever&rdquo;</td><td>Southwestern United States, Mexico, Central and South America</td><td><strong>Alkaline, salty</strong> soils of semiarid, hot climates</td><td>Block-like <strong>arthroconidia</strong>; <strong>spherules with endospores</strong> in the lungs</td><td>Amphotericin B; <strong>most cases need no treatment</strong></td></tr>
    <tr><td><strong><em>Blastomyces dermatitidis</em></strong></td><td>North American blastomycosis</td><td>Midwestern and southeastern United States, southern Canada</td><td>Rich organic matter: forest soil, decaying wood, animal manure</td><td>May be <strong>mistaken for lung cancer</strong> on chest X-ray</td><td>Amphotericin B</td></tr>
    <tr><td><strong><em>Paracoccidioides brasiliensis</em></strong></td><td>Paracoccidioidomycosis</td><td>Central and South America (Brazil, Colombia, Venezuela, Argentina, Paraguay)</td><td>Cool, humid soils</td><td>The <strong>rarest</strong> primary mycosis</td><td>Ketoconazole, amphotericin B, sulfa drugs</td></tr>
  </table>

  <h3 class="sub" id="fun-histo">15.8 &middot; Objective 1 &mdash; <em>Histoplasma capsulatum</em>: histoplasmosis, &ldquo;Ohio Valley fever&rdquo;</h3>
  <ul>
    <li><strong>The most common true fungal pathogen</strong>; causes histoplasmosis. <strong>Thermally
    dimorphic</strong> (the two colonies in 15.2).</li>
    <li>Distributed worldwide; known in the <strong>eastern and central regions of the United States</strong>, and now
    recognized as endemic in parts of Latin America and Africa.</li>
    <li>Grows in <strong>moist soil with high nitrogen content, especially soil containing bird and bat
    guano</strong>.</li>
    <li><strong>Inhaled conidia</strong> produce a <strong>primary pulmonary infection</strong> that may progress to
    systemic involvement of a variety of organs, the central nervous system, and chronic lung disease.
    <strong>It is NOT transmitted person to person.</strong></li>
    <li><strong>Treatment</strong>: amphotericin B and azoles are common options.</li>
  </ul>
  """ + fig("l15-s028-histoplasma-cycle.jpg", 795, 900,
      "Illustrated cycle: birds on soil, spores blown toward a jogger, a micrograph of spiky spores, the patient in bed, an inset of a phagocyte containing yeasts, and organs (brain, heart, liver, bone, intestine, kidney).",
      "<b>Events in histoplasmosis.</b> (1) Soil containing bird droppings is whipped up by the wind. (2) "
      "<b>Microconidia are inhaled.</b> (3) The patient develops a <b>mild pneumonitis, which might recur</b>. (4) In "
      "the tissue phase the <b>yeast phase develops, is phagocytosed and multiplies by budding "
      "intracellularly</b>; <b>most patients recover without complications</b>. (5) In some cases phagocytes enter "
      "the blood and cause <b>disseminated disease</b> in a number of organs.", 28,
      "&copy; A.M. Siegelman/Visuals Unlimited. " + MH) + """

  <h3 class="sub" id="fun-cocci">15.9 &middot; Objective 1 &mdash; <em>Coccidioides immitis</em>: coccidioidomycosis, &ldquo;Valley fever&rdquo;</h3>
  <ul>
    <li>Mainly in the <strong>southwestern United States</strong>, extending to Mexico and Central and South
    America. Exposure comes with <strong>farming, road construction and repair, archaeological digs, landslides and
    dust storms</strong>. It <strong>remains dormant in winter and spring</strong>.</li>
    <li><strong>Significant risk factors</strong>: people of African or African-American descent, increasing age
    (over 40&ndash;60 years), and environmental or occupational exposure to dust and soil.</li>
    <li><strong>Distinctive morphology</strong>: <strong>block-like arthroconidia</strong> in the free-living stage, and
    <strong>spherules containing endospores</strong> in the lungs.</li>
    <li>Lives in <strong>alkaline, salty soils in semiarid, hot climates</strong>; its spread is greatly enhanced by
    <strong>cycles of drought and heavy rain, followed by windstorms</strong>.</li>
    <li><strong>Arthrospores inhaled from dust</strong> create spherules and can form <strong>nodules in the
    lungs</strong>.</li>
    <li><strong>Prevention</strong>: oiling roads, planting to minimize erosion, and dust masks to reduce inhalation of
    spores.</li>
    <li><strong>Treatment</strong>: amphotericin B is the most common option, but <strong>most cases do not require any
    treatment at all</strong>.</li>
  </ul>
  """ + fig("l15-s031-coccidioides-cycle.jpg", 900, 822,
      "Illustrated cycle: a boy digging soil, an inset of chained barrel-shaped arthrospores, the boy inhaling, a circle showing an arthrospore enlarging into a spherule full of endospores, and a second boy with skin and bone lesions.",
      "<b>Events in coccidioidomycosis.</b> (1) <b>Digging in soil produces an aerosol of arthrospores.</b> (2) "
      "<b>Inhaled arthrospores establish a lung infection.</b> (3) An arthrospore develops into a <b>spherule "
      "(giant sporangium)</b> that produces endospores, released in the lungs. (4) <b>Immunocompetent persons fight "
      "the infection and return to health.</b> (5) <b>Compromised people can develop meningitis, osteomyelitis and "
      "skin granulomas.</b>", 31, "&copy; Science VU-Charles Sutton/Visuals Unlimited. " + MH) + """

  <h3 class="sub" id="fun-blasto">15.10 &middot; Objective 1 &mdash; <em>Blastomyces dermatitidis</em>: North American blastomycosis</h3>
  <ul>
    <li>A <strong>dimorphic</strong> fungus that inhabits <strong>rich organic matter: forest soil, decaying wood,
    animal manure</strong>.</li>
    <li>Free-living, mainly in the soil of a large section of the <strong>midwestern and southeastern United
    States</strong>, and in <strong>southern Canada</strong>; <strong>dormant in warm, dry weather, then sporulates in
    colder, wetter weather</strong>. Also reported in South and Central America, Africa and the Middle East.</li>
    <li><strong>Inhaled conidia</strong> (10&ndash;100) <strong>convert to yeasts and multiply in the lungs</strong>; the
    infection <strong>may be mistaken for lung cancer on a chest X-ray</strong>.</li>
    <li>Symptoms: <strong>cough, chest pain and fever</strong>, in humans, <strong>dogs, cats and horses</strong>.</li>
    <li><strong>Chronic cutaneous nodules</strong>, with later <strong>bone and nervous system</strong>
    complications.</li>
    <li><strong>Treatment</strong>: amphotericin B is the most common option.</li>
  </ul>
  """ + fig("l15-s034-blastomyces-dimorphism.jpg", 800, 316,
      "Two micrographs: on the left, thin branching filaments bearing small round cells; on the right, a dense field of round, thick-walled, red-stained cells, one marked with an arrow.",
      "<b>The dimorphic nature of <em>Blastomyces dermatitidis</em></b>: (a) the mold form, hyphae with conidia; "
      "(b) the yeast form in tissue.", 34, MH) + """
  """ + fig("l15-s035-cutaneous-blastomycosis.jpg", 800, 573,
      "Photograph of a swollen, red hand and wrist with dark crusted ulcers.",
      "<b>Cutaneous blastomycosis</b> of the hand and wrist.", 35, MH) + """

  <h3 class="sub" id="fun-paracocci">15.11 &middot; Objective 1 &mdash; <em>Paracoccidioides brasiliensis</em>: paracoccidioidomycosis</h3>
  <ul>
    <li>Endemic in <strong>Central and South America</strong>, mainly the cool, humid soils of Brazil, Colombia,
    Venezuela, Argentina and Paraguay; <strong>the rarest of the primary mycoses</strong>. Most studies in the
    World Health Organization report were among human immunodeficiency virus-positive patients in Brazil.</li>
    <li><strong>Lung or skin infection occurs through inhalation or inoculation of spores, respectively.</strong></li>
    <li><strong>Most at risk</strong>: rural farm workers and harvesters, where <strong>poor nutrition</strong> is a
    predisposing factor; male, over 40 years old.</li>
    <li><strong>Systemic disease is not common</strong>; these are usually <strong>mild, self-limiting</strong>
    infections.</li>
    <li><strong>Treatment</strong>: ketoconazole, amphotericin B and sulfa drugs are commonly used.</li>
  </ul>

  <h3 class="sub" id="fun-sporothrix">15.12 &middot; Objective 1 &mdash; Subcutaneous mycoses: <em>Sporothrix schenckii</em></h3>
  <p><strong>Subcutaneous mycoses</strong> occur when fungi are <strong>transferred directly into traumatized
  skin</strong> and invade the damaged site. Most species in this group are <strong>greatly inhibited by the higher
  temperatures of the blood and viscera, so they rarely disseminate</strong> through the body. These diseases are
  <strong>progressive</strong> and may destroy skin and underlying tissue.</p>
  <ul>
    <li><strong>Sporotrichosis, &ldquo;rose-gardener&rsquo;s disease&rdquo;</strong>, usually comes from a
    <strong>puncture wound</strong>: a thorn, wood, bare roots.</li>
    <li>A very common <strong>saprobic</strong> fungus (one that derives its nutrition from dead or decaying matter)
    that decomposes plant matter in soil. <strong>Garden center workers, plant nurseries and people who handle pine
    straw or hay bales</strong> may be at risk.</li>
    <li>Infects <strong>appendages and lungs</strong> (humans, horses, dogs, cats and mules; in animals it is often
    seen in the feet, claws or hooves).</li>
    <li><strong>Treatment</strong>: heat packs and/or <strong>super-saturated potassium iodide</strong>; systemic
    infections with amphotericin B and/or itraconazole.</li>
    <li>The <strong>lymphocutaneous</strong> variety: contaminated plant material penetrates the skin, the pathogen
    forms a <strong>nodule, then spreads to nearby lymph nodes</strong>.</li>
  </ul>
  """ + fig("l15-s040-sporothrix.jpg", 800, 413,
      "Two micrographs: on the left, thin hyphae with rosette-like clusters of small oval conidia at their tips; on the right, scattered oval and budding yeast cells.",
      "<b>The microscopic morphology of <em>Sporothrix schenckii</em></b>: (a) hyphae with clusters of conidia; (b) "
      "yeast cells.", 40, "&copy; CDC/Dr. Libero Ajello, CDC/Dr. Lucille K. Georg. " + MH) + """
  """ + fig("l15-s041-lymphocutaneous-sporotrichosis.jpg", 800, 567,
      "Photograph of a forearm with a row of red, crusted nodules running along it.",
      "<b>Lymphocutaneous sporotrichosis</b>: nodules along the arm.", 41,
      "&copy; Everett S. Beneke/Visuals Unlimited. " + MH) + """

  <h3 class="sub" id="fun-dermatophytes">15.13 &middot; Objective 1 &mdash; Cutaneous mycoses: the dermatophytes</h3>
  <ul>
    <li>Infections <strong>strictly confined to keratinized epidermis (skin, hair, scalp, nails)</strong> are called
    <strong>dermatophytoses</strong>: &ldquo;<strong>ringworm</strong>&rdquo; and &ldquo;<strong>tinea</strong>&rdquo;.</li>
    <li>They involve <strong>39 species in three genera: <em>Trichophyton</em>, <em>Microsporum</em> and
    <em>Epidermophyton</em></strong>, all closely related and morphologically similar.
    <strong>The actual causative agent of &ldquo;ringworm&rdquo; varies case to case.</strong></li>
    <li><strong>Natural reservoirs</strong>: humans, animals and soil.</li>
    <li><strong>What promotes infection</strong>: the <strong>hardiness of the spores</strong>, the presence of
    <strong>abraded skin</strong>, and <strong>close person-to-person or person-to-fomite contact</strong>.</li>
    <li>A <strong>long infection period</strong> followed by <strong>localized inflammation and allergic reactions to
    fungal proteins</strong>.</li>
  </ul>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Flagged on the slide</span>
  <p><mark class="prof-highlight">&ldquo;Focus on the Latin names for each body part/region&rdquo;</mark> (slide 43).</p>
  <table>
    <tr><th>Name</th><th>Body site</th><th>What the slides say</th></tr>
    <tr><td><strong>Tinea capitis</strong></td><td>Scalp</td><td>Scalp and hair-bearing regions of the head; <strong>hair may be lost</strong>; <strong>common in children</strong></td></tr>
    <tr><td><strong>Tinea barbae</strong></td><td>Beard</td><td>Chin and beard of <strong>adult males</strong>; contracted mainly <strong>from animals</strong></td></tr>
    <tr><td><strong>Tinea corporis</strong></td><td>Body</td><td><strong>Inflamed, red ring lesions</strong> anywhere on <strong>smooth skin</strong>; contact, clothing, bedding</td></tr>
    <tr><td><strong>Tinea cruris</strong></td><td>Groin</td><td>&ldquo;<strong>Jock itch</strong>&rdquo;: groin and scrotal regions; pervasive among <strong>athletes and crowded living conditions</strong></td></tr>
    <tr><td><strong>Tinea pedis</strong></td><td>Foot</td><td>Spread by exposure to <strong>public surfaces</strong>; between the digits and on the soles; <strong>rare where people usually go barefoot</strong></td></tr>
    <tr><td><strong>Tinea manuum</strong></td><td>Hand</td><td>Paired with tinea pedis on the slide: public surfaces; between the digits</td></tr>
    <tr><td><strong>Tinea unguium</strong></td><td>Nails</td><td>A <strong>persistent colonization of the nails</strong> of the hands and feet that <strong>distorts the nail bed</strong>; <strong>nail extensions</strong> may provide a portal of entry</td></tr>
  </table>
  </div>
  <p><strong>Treatment of dermatophytoses</strong> most often uses <strong>topical antifungal agents: azoles applied
  for several weeks</strong>, which may be partnered with oral antifungal drugs if needed. <strong>Debridement of the
  skin and ultraviolet light treatments</strong> have also been successful.</p>
  """ + fig("l15-s047-tinea-scalp-body.jpg", 525, 900,
      "Two photographs: above, the back of a boy's head with a scaly, crusted patch and thinned hair; below, red, scaly patches with raised edges on the skin of a shoulder and armpit.",
      "<b>Ringworm of the scalp and body</b>: (a) tinea capitis, a scaly patch with hair loss; (b) tinea corporis, "
      "red lesions with raised edges.", 47, "&copy; Everett S. Beneke/Visuals Unlimited, Kenneth E. Greer/Visuals Unlimited. " + MH) + """
  """ + fig("l15-s048-tinea-extremities.jpg", 473, 900,
      "Two photographs: above, a foot with red, scaling skin across the top and between the toes; below, fingers with thickened, white, crumbling nails.",
      "<b>Ringworm of the extremities</b>: (a) tinea pedis; (b) tinea unguium, distorted nails.", 48, MH) + """

  <h3 class="sub" id="fun-superficial">15.14 &middot; Objective 1 &mdash; Superficial mycoses</h3>
  <table>
    <tr><th>Mycosis</th><th>Cause</th><th>What it does</th></tr>
    <tr><td><strong>Tinea versicolor</strong></td><td>A <strong>yeast, <em>Malassezia furfur</em></strong></td><td>Mild, chronic <strong>scaling and mottling</strong> of the skin; also implicated in folliculitis, psoriasis and seborrheic dermatitis</td></tr>
    <tr><td><strong>White piedra</strong> (piedra = stone)</td><td><em>Trichosporon</em> species</td><td><strong>Whitish or colored masses on pubic or axillary hair</strong> (also body, beard, mustache, eyebrows)</td></tr>
    <tr><td><strong>Black piedra</strong></td><td><em>Piedraia</em> species</td><td><strong>Dark-brown to black, gritty nodules, mainly on scalp hairs</strong></td></tr>
  </table>
  <p>Both piedras are considered <strong>non-contagious</strong> and may result from <strong>poor personal hygiene</strong>
  (oily hair products, tight hats or veils). <strong>Neither piedra is common in the United States.</strong></p>
  """ + fig("l15-s050-piedra.jpg", 588, 900,
      "Two micrographs of hair shafts: above, a hair shaft sheathed in a pale granular mass; below, a hair shaft with a dark brown nodule wrapped around it.",
      "<b>The two piedras on a hair shaft</b>: (a) white piedra; (b) black piedra.", 50,
      "&copy; Everett S. Beneke/Visuals Unlimited. " + MH) + """

  <h3 class="sub" id="fun-opportunists">15.15 &middot; Objective 1 &mdash; The opportunistic mycoses</h3>
  <p>These fungi were once considered <strong>&ldquo;harmless&rdquo; skin or air contaminants</strong>. All have
  predisposing factors, and the host&rsquo;s defenses are compromised: <strong><em>Candida</em> species, the dominant
  opportunistic pathogen</strong>; <strong><em>Aspergillus fumigatus</em>, which accounts for most lung
  infections</strong> (the slide&rsquo;s words; read it as most of the <em>Aspergillus</em> lung infections); <em>Cryptococcus neoformans</em>; <em>Fusarium</em> species; and <em>Rhizopus</em> species.</p>
  """ + fig("l15-s009-opportunists-table.jpg", 747, 600,
      "Table 22.3, Common Opportunistic Fungi and Conditions That Predispose Patients to Them, with four rows: Candida, Aspergillus, Cryptococcus and Zygomycota species.",
      "<b>Table 22.3, the predisposing conditions.</b> <em>Candida</em>: antibiotic therapy, catheters, diabetes, "
      "corticosteroids, immunosuppression. <em>Aspergillus</em>: leukemia, corticosteroids, tuberculosis, "
      "immunosuppression, intravenous drug abuse. <em>Cryptococcus</em>: diabetes, tuberculosis, cancer, "
      "corticosteroids, immunosuppression. Zygomycota species: diabetes, cancer, corticosteroids, intravenous "
      "therapy, third-degree burns. (Footnotes: anti-inflammatory drugs are often given for chronic lung diseases "
      "and to transplant patients to prevent rejection; immunosuppression includes acquired immunodeficiency "
      "syndrome and genetic conditions that compromise host defenses.)", 9, MH) + """

  <h3 class="sub" id="fun-candida">15.16 &middot; Objective 1 &mdash; <em>Candida</em> and candidiasis</h3>
  <ul>
    <li><strong><em>Candida albicans</em></strong> is the familiar one, but <strong><em>Candida auris</em> is emerging as a
    serious cause of invasive candidiasis</strong>, producing <strong>hospital outbreaks that are difficult to
    eradicate</strong>: antifungal drug resistance, <strong>thermoresistant</strong>, and partially resistant to common
    disinfectants. <em>C. auris</em> was first identified in <strong>Japan in 2009, as the cause of an ear
    infection, hence the name</strong>; cases have increased in recent years.</li>
    <li><em>C. albicans</em> is a widespread yeast, <strong>usually endogenous</strong> and not always considered
    contagious; it <strong>can be spread through surgery, childbirth, breast-feeding and sexual contact</strong>.</li>
    <li>Infections range from <strong>short-lived, superficial skin irritations to overwhelming, fatal systemic
    disease</strong> in seriously compromised hosts.</li>
    <li>Colony: <strong>off-white, pasty, with a yeasty (&ldquo;baking bread&rdquo;) odor</strong>.</li>
    <li><strong>Normal flora</strong> of the oral cavity, genitalia, large intestine or skin of 20% of humans;
    accounts for <strong>70% of nosocomial fungal infections</strong>.</li>
  </ul>
  <table>
    <tr><th>Form</th><th>What the slides say</th></tr>
    <tr><td><strong>Thrush</strong></td><td>A <strong>thick, white, adherent growth</strong> on the mucous membranes of the mouth and throat (chronic thrush in an adult man with diabetes, slide 54)</td></tr>
    <tr><td><strong>Vulvovaginal yeast infection</strong></td><td>A painful inflammatory condition of the female genital region with ulceration and discharge; <strong>may be transmitted to unprotected sexual partners, especially uncircumcised males</strong></td></tr>
    <tr><td><strong>Cutaneous candidiasis</strong></td><td>In <strong>chronically moist areas of skin</strong> and in <strong>burn patients</strong>; <strong>intertriginous lesions</strong> (armpits, groin, under the breasts) are common in obese patients</td></tr>
  </table>
  """ + fig("l15-s054-candidiasis.jpg", 554, 900,
      "Two photographs: above, a tongue covered with thick, white, curd-like plaques; below, a red, glazed rash in a groin fold.",
      "<b>Infections by <em>Candida albicans</em></b>: (a) chronic thrush in an adult male with diabetes; (b) "
      "intertriginous lesions.", 54, "&copy; Everett S. Beneke/Visuals Unlimited. " + MH) + """
  <p><strong>Diagnosis and treatment.</strong> A <strong>presumptive diagnosis is made if budding yeast cells and
  pseudohyphae are found</strong>; growth on <strong>selective, differential media differentiates the <em>Candida</em>
  species</strong>; the germ tube test is on the identification flowchart (15.5). <strong>Topical antifungals</strong>
  are used for superficial infections; <strong>amphotericin B and azoles</strong> for systemic infections.</p>

  <h3 class="sub" id="fun-crypto">15.17 &middot; Objective 1 &mdash; <em>Cryptococcus neoformans</em> and cryptococcosis</h3>
  <ul>
    <li><strong>The number one critical fungal pathogen</strong> on the World Health Organization&rsquo;s list.</li>
    <li>A widespread <strong>encapsulated yeast</strong> that inhabits <strong>soil around pigeon roosts in urban
    areas</strong>, and soil containing decaying wood.</li>
    <li><strong>Healthy humans are strongly resistant</strong>; frank infection occurs in immunocompromised patients
    (human immunodeficiency virus infection and acquired immunodeficiency syndrome, cancer, immunosuppression,
    autoimmune disease, diabetes, cirrhosis). Treatment protocols are well established for patients with human
    immunodeficiency virus infection, though the drugs may be unavailable in many countries.</li>
    <li><strong>Lungs</strong>: cough, fever and lung nodules. <strong>Dissemination to the meninges and the
    brain</strong> can cause severe neurological disturbance and death.</li>
    <li><strong>Diagnosis</strong>: a <strong>negative stain shows the encapsulated budding yeast</strong>;
    <strong>biochemical and serological testing are the best diagnostic tools</strong>.</li>
    <li><strong>Treatment</strong>: systemic infection generally requires <strong>amphotericin B and fluconazole or
    another azole-class drug</strong>.</li>
  </ul>

  <h3 class="sub" id="fun-pneumocystis">15.18 &middot; Objective 1 &mdash; <em>Pneumocystis jirovecii</em> and <em>Pneumocystis</em> pneumonia</h3>
  <ul>
    <li>Formerly <em>Pneumocystis carinii</em>. A <strong>small, unicellular fungus that causes pneumonia</strong>;
    <strong>the most prominent opportunistic infection in patients with human immunodeficiency virus infection and
    acquired immunodeficiency syndrome</strong>.</li>
    <li>Immunological evidence such as <strong>antibody titer</strong> suggests that <strong>contact with it is very
    widespread and most of us remain asymptomatic</strong>.</li>
    <li>The pneumonia forms <strong>secretions in the lungs that block breathing</strong> and can be <strong>rapidly
    fatal</strong> if not controlled (cough, fever, shallow respiration and cyanosis). <strong>Kidney transplant
    patients</strong> are also at high risk.</li>
    <li><strong>Treatment</strong>: <strong>pentamidine (an anti-protozoan) and the antibacterial co-trimoxazole
    (trimethoprim-sulfamethoxazole)</strong>; <strong>these are NOT the traditional antifungal drugs</strong>.</li>
    <li>Its taxonomy is still debated, fungus or protozoan; most scientists lean toward <strong>a fungal
    classification because of genetic analysis</strong>.</li>
  </ul>
  """ + fig("l15-s059-pneumocystis.jpg", 747, 600,
      "Micrograph of tissue crowded with round, dark-speckled structures, one bracketed by a label.",
      "<b><em>Pneumocystis jirovecii</em></b> in tissue: a cyst containing several bodies.", 59,
      "&copy; A.M. Siegelman/Visuals Unlimited. " + MH) + """

  <h3 class="sub" id="fun-aspergillus">15.19 &middot; Objective 1 &mdash; <em>Aspergillus</em> and aspergillosis</h3>
  <ul>
    <li>A <strong>very common airborne soil fungus</strong>; its <strong>resistance to azole fungicides can be
    attributed to agricultural practices</strong> (crop spraying to prevent loss to fungi).</li>
    <li>About 600 species, 8 involved in human disease; <strong><em>A. fumigatus</em> is the most common</strong> and is
    <strong>number three on the World Health Organization&rsquo;s critical list</strong>.</li>
    <li>A <strong>serious opportunistic threat in human immunodeficiency virus infection and acquired immunodeficiency
    syndrome, leukemia, and transplant patients</strong>.</li>
    <li>Infection usually occurs in the <strong>lungs: spores germinate and form fungal balls</strong>; it can also
    colonize the <strong>sinuses, ear canals, eyelids and conjunctiva</strong>.</li>
    <li><strong>Invasive aspergillosis</strong> can produce <strong>necrotic pneumonia</strong> and infection of the
    brain, heart and other organs; <strong>transplant recipients (organ and bone marrow) and cystic fibrosis
    patients</strong> are at increased risk.</li>
    <li>Treatment on the slide: amphotericin B and nystatin (see 15.23).</li>
    <li>In a sputum specimen it shows <strong>branched septate hyphae</strong> (15.5).</li>
  </ul>
  """ + fig("l15-s061-aspergillosis.jpg", 900, 638,
      "Two pictures: on the left, a young man's face with a swollen, red upper eyelid; on the right, slices of brain with dark, hemorrhagic lesions.",
      "<b>Clinical aspects of aspergillosis</b>: (a) infection around the eye; (b) brain sections with lesions of "
      "invasive disease. (Slide 61 also shows a chest X-ray.)", 61,
      "&copy; Everett S. Beneke/Visuals Unlimited, Science VU-AFIP/Visuals Unlimited. " + MH) + """
  """ + fig("l15-s062-aspergillus.jpg", 650, 600,
      "Micrograph of brown, branching filaments in pink tissue, with a round head bearing a fringe of spore-producing cells.",
      "<b><em>Aspergillus</em></b> in tissue: a <b>conidial head</b> on <b>hyphae</b>.", 62,
      "&copy; Image courtesy David Ellis, Adelaide Women's and Children's Hospital. " + MH) + """

  <h3 class="sub" id="fun-mucor">15.20 &middot; Objective 1 &mdash; Mucormycosis and other opportunists</h3>
  <h4 class="subsub">Zygomycosis (mucormycosis)</h4>
  <ul>
    <li>Members of the <strong>Division Zygomycota</strong> are extremely abundant <strong>saprobic</strong> fungi found
    in <strong>soil, water, organic debris and spoiled food</strong>.</li>
    <li>Mucormycosis is called <strong>&ldquo;black mold&rdquo;</strong> (the slide spells it mould) and has arisen as a big concern in
    <strong>India</strong> over the last few years; <strong>injudicious use of respiratory steroids and uncontrolled
    diabetes</strong> may have contributed. Rhino-orbital-oral-cerebral symptoms have been documented.</li>
    <li>The fungi most often involved are <strong><em>Rhizopus</em> and <em>Mucor</em></strong> species.</li>
    <li>Usually <strong>harmless air contaminants</strong> that may invade the membranes of the <strong>nose, eyes,
    heart and brain</strong> of people with <strong>diabetes, leukemia or malnutrition</strong>, with severe
    consequences. There is also a <strong>pediatric gastrointestinal complication in children who lack sufficient
    protein (kwashiorkor)</strong>.</li>
    <li><strong>Treatment</strong>: <strong>removal of affected tissue and amphotericin B</strong>.</li>
  </ul>
  <h4 class="subsub">Miscellaneous fungal opportunists</h4>
  <ul>
    <li><strong>Any fungus</strong> can be implicated when the host&rsquo;s immune defenses are severely compromised.</li>
    <li><strong><em>Fusarium</em></strong>: another mainly tropical soil mold; occasionally infects the <strong>eyes (for
    example from contaminated contact lenses)</strong>, toenails, feet and burned skin, and can result in severe
    disability and death.</li>
    <li><strong>Eumycetomas</strong>, deep tissue infections, are especially prevalent in poor countries; risk factors:
    <strong>male, 11&ndash;30 years old, farmer, not wearing shoes</strong>. <strong>Long-term antifungal drug therapy
    and amputation</strong> may be required for full resolution.</li>
  </ul>

  <h3 class="sub" id="fun-toxins">15.21 &middot; Objective 1 &mdash; Fungal allergies and mycotoxins</h3>
  <ul>
    <li><strong>Fungal spores are common sources of atopic allergies or hypersensitivities</strong>: seasonal
    allergies and asthma; <strong>farmer&rsquo;s lung, teapicker&rsquo;s lung, bark stripper&rsquo;s
    disease</strong>.</li>
    <li><strong>Fungal toxins cause mycotoxicoses</strong>, usually by <strong>ingesting or inhaling</strong> fungal
    toxins.</li>
  </ul>
  <table>
    <tr><th>Toxin or mold</th><th>What the slide says</th></tr>
    <tr><td><strong>Aflatoxin</strong></td><td><strong>Hepatotoxic and carcinogenic</strong>; grains, corn, peanuts; lethal to poultry and livestock (especially turkeys, ducklings, pigs and calves); in humans it may be a <strong>co-factor in liver cancer</strong></td></tr>
    <tr><td><strong>Ergot</strong></td><td>On <strong>rye or other grains contaminated by <em>Claviceps</em></strong> fungi; mind-altering lysergic acid (the slide writes LSD; lysergic acid diethylamide is a semi-synthetic derivative of it); cross-reference Salem, Massachusetts</td></tr>
    <tr><td><strong><em>Stachybotrys chartarum</em></strong></td><td><strong>Sick building syndrome</strong> (damp building related illness, the &ldquo;black mold&rdquo;; <strong>very different from mucormycosis</strong>); can cause severe hematologic and neurological damage. <strong>Not all molds in buildings are toxic, and not all illnesses in buildings are due to fungi</strong>; fear of mold has spawned a whole industry of environmental mold control</td></tr>
  </table>

  <h3 class="sub" id="fun-transmission">15.22 &middot; Objective 2 &mdash; Modes of transmission</h3>
  <table>
    <tr><th>How people acquire it</th><th>Fungi</th></tr>
    <tr><td><strong>Inhaling spores</strong> from disturbed soil or animal waste</td><td>The true pathogens: <em>Histoplasma</em> (soil with bird and bat guano, conidia whipped up by wind), <em>Coccidioides</em> (arthrospores in dust from digging, construction, dust storms), <em>Blastomyces</em> (conidia from forest soil, decaying wood, manure), <em>Paracoccidioides</em> (lung infection by inhalation)</td></tr>
    <tr><td><strong>Inhaling spores or yeasts</strong> of opportunists</td><td><em>Cryptococcus</em> (soil around urban pigeon roosts), <em>Aspergillus</em> (airborne soil fungus; spores germinate in the lungs), the Zygomycota (air contaminants)</td></tr>
    <tr><td><strong>Inoculation</strong> through broken or punctured skin</td><td><em>Sporothrix</em> (thorn, wood, bare roots); <em>Paracoccidioides</em> (skin infection by inoculation); true-pathogen spores into broken skin; nail extensions as a portal for tinea unguium</td></tr>
    <tr><td><strong>Person to person or by fomites</strong></td><td>The <strong>dermatophytes</strong> (close contact, shared equipment, clothing, bedding, public surfaces; tinea barbae mainly from animals) and <strong><em>Candida</em></strong> (surgery, childbirth, breast-feeding, sexual contact)</td></tr>
    <tr><td><strong>Endogenous</strong> (already on the body)</td><td><em>Candida albicans</em>, usually endogenous normal flora</td></tr>
    <tr><td><strong>Not communicable</strong></td><td>Most fungal pathogens; <em>Histoplasma</em> is explicitly <strong>not transmitted person to person</strong>; the piedras are non-contagious</td></tr>
    <tr><td><strong>Ingesting or inhaling toxins</strong></td><td>Mycotoxicoses: aflatoxin (grains, corn, peanuts), ergot (rye)</td></tr>
  </table>

  <h3 class="sub" id="fun-notes">15.23 Where the slides disagree, and where current practice differs</h3>
  <ul>
    <li><strong>Immunity after a true fungal pathogen.</strong> Slide 15 says long-term immunity &ldquo;can only
    develop against a few true fungal pathogens&rdquo;; slide 24 says &ldquo;all of the diseases caused by the true
    fungal pathogens can result in immunity in a competent host&rdquo;. No question asks which, or how many; the
    contrast with the opportunists (reinfection highly likely) is the same on both slides.</li>
    <li><strong>Amphotericin B routes (slide 20).</strong> The slide calls it versatile, given topically, orally, by
    intramuscular injection or intravenously. In current practice it is given intravenously for systemic infection;
    it is not given by intramuscular injection and is poorly absorbed by mouth. Not asked.</li>
    <li><strong>Why amphotericin B is toxic (slide 20).</strong> The slide gives the reason as fungi and humans both
    being eukaryotes, so the drug is not selective enough. Pharmacology references add the mechanism: it binds
    ergosterol in fungal membranes but also binds some cholesterol in human membranes. One quiz question asks this,
    keyed as the slide says.</li>
    <li><strong>Aspergillosis treatment (slide 60).</strong> The slide lists amphotericin B and nystatin. Nystatin is
    a topical and oral (non-absorbed) agent and current practice does not use it for invasive aspergillosis (azoles
    such as voriconazole are used). Not asked.</li>
    <li><strong>Temperatures.</strong> Slide 5 gives mold at 30&nbsp;&deg;C and yeast at 37&nbsp;&deg;C; the slide 6
    figure gives the ranges below 30&nbsp;&deg;C and 35&ndash;40&nbsp;&deg;C, and slide 27 grows the mold below
    35&nbsp;&deg;C. They agree on direction; the quizzes use slide 5&rsquo;s two numbers.</li>
    <li><strong>&ldquo;Black mold.&rdquo;</strong> Slide 63 calls mucormycosis &ldquo;black mould&rdquo;; slide 65 calls
    <em>Stachybotrys</em> the &ldquo;black mold&rdquo; and says the two are very different. Know them apart by what
    they do: mucormycosis invades tissue (nose, eyes, brain) in diabetes and leukemia; <em>Stachybotrys</em> is the
    sick building mold.</li>
    <li><strong>Spellings.</strong> The deck&rsquo;s &ldquo;Blastomyces dermatiditis&rdquo; (slide 34) is <em>Blastomyces
    dermatitidis</em>, as slide 33 spells it; &ldquo;mould&rdquo; is written mold here.</li>
  </ul>

  <button type="button" class="test-yourself-btn" onclick="window.openTestYourself('Test yourself &mdash; Fungi of Medical Importance', TEST_YOURSELF.fungi)">Test yourself! &rarr;</button>
  <p class="src">Source: <em>Fungi of Medical Importance</em> (PAJ5200.Fungi of Medical importance.pptx), Slides
  1&ndash;65, and the PAJ 5200 syllabus instructional objectives.</p>
</section>
"""

SECTION = SECTION_HEAD + BODY

TEST = """
    fungi: [
      {q:"What is thermal dimorphism?",
       choices:["Growing only at body temperature","A mold at 30 C and a yeast at 37 C","A yeast in soil and a mold in the body","Surviving freezing and boiling"],correct:1,
       explain:"True fungal pathogens grow as multicellular molds at 30 C and switch to unicellular yeasts at 37 C, human body temperature."},
      {q:"Which fungal pathogen is linked to soil with bird and bat guano and is NOT spread person to person?",
       choices:["Coccidioides immitis","Candida albicans","Histoplasma capsulatum","Sporothrix schenckii"],correct:2,
       explain:"Histoplasma capsulatum, Ohio Valley fever: inhaled conidia from nitrogen-rich soil with guano. Coccidioides lives in alkaline desert soil; Sporothrix enters through a puncture wound."},
      {q:"What forms in the lungs in coccidioidomycosis?",
       choices:["Fungal balls","Spherules containing endospores","Germ tubes","Encapsulated budding yeasts"],correct:1,
       explain:"Inhaled arthrospores become spherules full of endospores. Fungal balls are aspergillosis; an encapsulated budding yeast is Cryptococcus."},
      {q:"Which tinea is 'jock itch'?",
       choices:["Tinea cruris","Tinea corporis","Tinea capitis","Tinea barbae"],correct:0,
       explain:"Tinea cruris affects the groin and scrotal regions. Corporis = smooth skin of the body; capitis = scalp; barbae = beard."},
      {q:"Why is Pneumocystis pneumonia unusual among fungal infections in its treatment?",
       choices:["It needs no treatment","It is treated with pentamidine and co-trimoxazole, not traditional antifungals","Only surgery works","It is treated with nystatin alone"],correct:1,
       explain:"Pentamidine (an anti-protozoan) and co-trimoxazole (an antibacterial) are used; these are not the traditional antifungal drugs."}
    ],
"""
