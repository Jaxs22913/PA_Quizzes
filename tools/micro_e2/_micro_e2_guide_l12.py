# -*- coding: utf-8 -*-
"""Section 12 of the Microbiology Exam 2 guide -- Epidemiology (Dr. Webster).

Same shape as _micro_e2_guide_l11.py (FIG, DECK, fig(), TOC, SECTION, TEST, IMAGES, extract()):
build_micro_e2_guide.py imports it, calls extract() for the figures and splices TOC, SECTION and TEST.

Attribution: Dr. Webster, from the deck file name ("Lecture 12 Dr. Webster - Epidemiology.pptx") and the
calendar row for 16 October 2026; the title slide names no lecturer.

Instructional objectives are VERBATIM from the syllabus (Micro.pdf, pages 3-4): the ten numbered
objectives under "Epidemiology", answered in order (12.1 objective 1 ... 12.10 objective 10). The deck
teaches them in a different order (definition and uses first, descriptive and analytic studies in the
middle); the guide follows the objectives. The deck's own objective slides (2-3) match the syllabus.

Content is from the VISIBLE slides only (text and pictures; the deck's one speaker note, "Use this slide",
adds nothing). Pictures read at full size: slide 25 (the uses-of-surveillance-data table), slide 42 (Snow's
two tables), slide 44 (the pyramid: its labels sit bottom to top Chance, Spurious/artifact, Confounded,
Non-causal, Causal), slide 49 (the dose-response table), slides 56-58 (the epidemic curves; on slide 56 the
LEFT picture, hepatitis A, is labeled Point and the RIGHT, diarrheal illness, Continuous; on slide 57 the
LEFT, measles, is Propagated and the RIGHT, Shigella at a festival, Mixed; slide 58's two are Other), slide
71 (the public health approach).

AUDIO: parts 1-3 of the 16 October 2026 recording (34 + 10 + 29 minutes) are the lecture; part 4 (21 minutes)
is her review for Exam 2 (Lectures 7 and 10, then this lecture's objectives from 19:38). All four read in
BOTH transcripts (Notability's own and the local faster-whisper medium.en run) and compared 2026-10-16. Every
quote in the box and the stars appears in both; timestamps are the local transcript's. The recording supplies
emphasis only (the slide wins).
"""
import os

FIG = "micro-exam-2-study-guide-images"
DECK = "Lecture 12 Dr. Webster - Epidemiology.pptx"
INBOX_DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Microbiology Inbox/Exam 2/Lecture 12 Dr. Webster - Epidemiology.pptx")

# (slide, picture index on that slide in shape-tree order counting group members and placeholder
# pictures, published file name). Indexes were resolved against each picture's position on the slide.
IMAGES = [
    (41, 1, "l12-s041-snow-spot-map.png"),
    (45, 2, "l12-s045-web-of-causation.png"),
    (56, 1, "l12-s056-point-source-curve.png"),
    (56, 2, "l12-s056-continuous-source-curve.png"),
    (57, 2, "l12-s057-propagated-curve.png"),
    (57, 1, "l12-s057-mixed-curve.png"),
    (58, 1, "l12-s058-lyme-by-year.png"),
    (71, 1, "l12-s071-public-health-approach.png"),
]


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
    prs = Presentation(INBOX_DECK)
    os.makedirs(imgdir, exist_ok=True)
    for slide, k, name in IMAGES:
        pics = list(_pictures(prs.slides[slide - 1].shapes))
        assert len(pics) >= k, "%s slide %d has %d picture(s)" % (DECK, slide, len(pics))
        img = pics[k - 1].image
        assert name.endswith("." + img.ext.replace("jpeg", "jpg")), (name, img.ext)
        open(os.path.join(imgdir, name), "wb").write(img.blob)
    return len(IMAGES)


def fig(name, w, h, alt, cap, slide):
    return ('<figure class="fig"><img width="%d" height="%d" loading="lazy" src="%s/%s" alt="%s">'
            '<figcaption>%s <span class="src">Source: %s, Slide %d.</span></figcaption></figure>'
            % (w, h, FIG, name, alt, cap, DECK, slide))


TOC = """
  <a class="top-link" href="#epidemiology">12 &middot; Epidemiology</a>
  <a class="sub-link" href="#epi-audio">&#9733; What the recording adds</a>
  <a class="sub-link" href="#epi-descriptive">12.1 Objective 1 &mdash; Descriptive and analytic epidemiology</a>
  <a class="sub-link" href="#epi-uses">12.2 Objective 2 &mdash; What epidemiology is, and the uses of epidemiologic training</a>
  <a class="sub-link" href="#epi-history">12.3 Objective 3 &mdash; Key events in its history, including genomic epidemiology</a>
  <a class="sub-link" href="#epi-data">12.4 Objective 4 &mdash; Common sources of epidemiologic data</a>
  <a class="sub-link" href="#epi-surveillance">12.5 Objective 5 &mdash; Public health surveillance</a>
  <a class="sub-link" href="#epi-reportable">12.6 Objective 6 &mdash; Reportable (notifiable) diseases</a>
  <a class="sub-link" href="#epi-measures">12.7 Objective 7 &mdash; Measures of morbidity and mortality</a>
  <a class="sub-link" href="#epi-causation">12.8 Objective 8 &mdash; Association and causation</a>
  <a class="sub-link" href="#epi-terms">12.9 Objective 9 &mdash; Endemic, epidemic, pandemic, sporadic, herd immunity</a>
  <a class="sub-link" href="#epi-applications">12.10 Objective 10 &mdash; Applications of epidemiology</a>
  <a class="sub-link" href="#epi-notes">12.11 Where the slides need a second look</a>
"""

SECTION_HEAD = """
<section class="deck" id="epidemiology">
  <h2 class="deck-title">12 &middot; Epidemiology</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Distinguish between descriptive and analytic epidemiology.</li>
      <li>Describe the specific uses for epidemiology training.</li>
      <li>Describe key events in the history and development of epidemiology, including genomic
      epidemiology</li>
      <li>Identify common sources of epidemiologic data.</li>
      <li>Define the primary components of public health surveillance.</li>
      <li>Define reportable disease</li>
      <li>Describe selected measures of morbidity and mortality.</li>
      <li>Distinguish between the terms association and causation.</li>
      <li>Define the terms endemic, epidemic, pandemic, sporadic, and herd immunity.</li>
      <li>Compare and contrast applications of epidemiology, including policy development, outbreak
      investigation, social and behavioral issues, the environment and occupational health</li>
    </ol>
  </div>

  <div class="callout"><strong>The lecture in one sentence:</strong> epidemiology is the study of the
  occurrence and distribution of health-related diseases or events in specified populations, including the
  determinants that influence them, and the <em>application</em> of that knowledge to control the health
  problem. Everything else hangs off that definition: <strong>descriptive</strong> studies say who, where and
  when (person, place, time); <strong>analytic</strong> studies test why (host, agent, environment);
  <strong>surveillance</strong> and <strong>reportable diseases</strong> supply the data; <strong>incidence,
  prevalence and mortality rates</strong> measure the burden; <strong>Hill&rsquo;s criteria</strong> decide
  whether an association is causal; and the applications (outbreaks, policy, social and behavioral factors,
  the environment, the workplace) are where it is used. Ten objectives, answered in order below.</div>

<!--MICROL12AUDIO-->
  <div class="prof-flag" id="epi-audio"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 16 October 2026</span>
  <p>About 74 minutes of lecture with Dr. Webster, in three parts (the recording starts a few slides in, at
  the uses of epidemiology), then a fourth part that is her <b>review for Exam 2</b>: Lectures 7 and 10, and
  at the end this lecture&rsquo;s objectives [part 4, 19:38]. <b>Both transcripts read and compared</b>
  (Notability&rsquo;s own and an independent local transcription); <b>every quote below appears in both</b>.
  Every factual claim was checked against the deck, and where the two differ the slide is what this guide
  teaches.</p>
  <p><b>Like Lecture 7, this lecture signposts</b>, in her soft wording (&ldquo;you should know&rdquo;,
  &ldquo;you need to know&rdquo;, &ldquo;you should be able to&rdquo;), and it ends with her own list of
  what to study.</p>
  <table>
    <tr><th>What was said</th><th>What it means for you</th></tr>
    <tr><td><em>&ldquo;You need to know the basic components of descriptive epidemiology versus analytic
    epidemiology.&rdquo;</em> [part 2, 6:51]</td>
    <td>12.1: descriptive = <b>person, place, time</b>; analytic = <b>host, agent, environment</b>, and what
    sits under each.</td></tr>
    <tr><td><em>&ldquo;Go back and look at the history and <mark class="prof-highlight">the people who are
    important in history</mark>.&rdquo;</em> [part 4, 19:44]</td>
    <td>12.3: Hippocrates, John Graunt, William Farr (father of modern vital statistics), John Snow (father of
    field epidemiology), and what each did.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">You need to know genomic epidemiology.</mark>&rdquo;</em>
    [part 3, 24:46]</td>
    <td>12.3 and 12.10: sequencing pathogens to link cases to one outbreak, find transmission links and
    sources, and map spread.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">You should know the difference between incidence and
    prevalence.</mark>&rdquo;</em> [part 1, 30:33]</td>
    <td>12.7: incidence counts <b>new</b> cases in a period (the speedometer); prevalence counts <b>all</b>
    cases present (the odometer), and depends on incidence and how long the disease lasts.</td></tr>
    <tr><td><em>&ldquo;If I were to&hellip; give you a scenario that gave you some information, <mark
    class="prof-highlight">you should be able to tell me whether something is going to be more of an
    association or a causation</mark>.&rdquo;</em> [part 3, 11:10]</td>
    <td>12.8: be ready to class a described study. A relationship alone is an association; causation is
    inferred when Hill&rsquo;s criteria are met.</td></tr>
    <tr><td><em>&ldquo;These different kinds of epidemics can be graphed and show different patterns,
    <mark class="prof-highlight">which you should be able to identify</mark>.&rdquo;</em> [part 3, 13:47]</td>
    <td>12.9: read an epidemic curve as point, continuous, propagated, mixed or other (the five curves are
    reproduced there).</td></tr>
    <tr><td>Her closing list: <em>&ldquo;public health surveillance, the different kinds of surveillances&hellip;
    the different measures of morbidity and mortality, association and causation, the Hill&rsquo;s criteria,
    and then know that endemic, epidemic, pandemic, sporadic, herd immunity, and then the fact that
    epidemiology gives us the evidence for policy development.&rdquo;</em> [part 4, 19:52]</td>
    <td>Seven of the ten objectives are on it by name (not the uses of training, data sources or reportable
    diseases); epidemiology&rsquo;s
    main contribution to policy is <b>evidence</b> (12.10).</td></tr>
    <tr><td><em>&ldquo;This particular graph, which I&rsquo;m not asking you to memorize&rdquo;</em> [part 1,
    11:25]</td>
    <td>Slide 13&rsquo;s life-course picture of factors behind long-term health. Not asked.</td></tr>
    <tr><td><em>&ldquo;Here&rsquo;s a list I&rsquo;m absolutely not requiring you to pay attention
    to&rdquo;</em> [part 1, 27:48]</td>
    <td>Slide 23, the full list of notifiable diseases. Know what makes a disease reportable and how the
    groups are reported (slides 21&ndash;22), not the list.</td></tr>
    <tr><td><em>&ldquo;I don&rsquo;t want you to memorize this list.&rdquo;</em> [part 1, 29:10]</td>
    <td>Slide 25, the uses of surveillance data. Know that surveillance data are used; the list itself is
    not asked.</td></tr>
  </table>
  <p><b>Things said that are not on a slide</b> &mdash; consistent with the deck, useful as hooks, and each
  present in both transcripts:</p>
  <ul>
    <li>Passive versus sentinel: in passive surveillance anyone may send reports, with no instruction on
    how to collect or submit them; sentinel providers are chosen to represent the population and told
    exactly how to collect and send the data, so the data are more accurate. [part 1, 24:07&ndash;24:58]</li>
    <li>Syndromic surveillance (counting diarrhea rather than confirmed cholera) is &ldquo;maybe the best
    that they can do&rdquo; in developing countries; a cluster of a syndrome then prompts targeted testing to
    find the actual agent. [part 1, 21:35&ndash;23:41]</li>
    <li>Herd immunity protects people who cannot be vaccinated (a young child, an older person, someone with
    an immune disorder); her current example is measles, as vaccination falls. [part 3, 18:04&ndash;18:47]</li>
    <li>Legionnaires&rsquo; disease: the organism was traced to the hotel&rsquo;s air-conditioning system, so
    walking through the lobby meant breathing it in; the attendees, mostly older smokers, were especially
    susceptible. [part 3, 23:13&ndash;23:37] (Slide 68&rsquo;s faucet and air-conditioner picture is
    otherwise unexplained in the deck.)</li>
  </ul>
  </div>
<!--/MICROL12AUDIO-->
"""

BODY = """
  <h3 class="sub" id="epi-descriptive">12.1 &middot; Objective 1 &mdash; Descriptive and analytic epidemiology</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; &ldquo;you need to know the basic components of descriptive epidemiology versus analytic epidemiology&rdquo;</span>
  <p>The two triads and what sits under each: person, place and time for descriptive; host, agent and environment for analytic.</p></div>
  <table>
    <tr><th></th><th>Descriptive epidemiology</th><th>Analytic epidemiology</th></tr>
    <tr><td>What it does</td><td>Examines the <strong>distribution</strong> of a disease in a population and
    observes the basic features of that distribution in terms of <strong>time, place and person</strong></td>
    <td><strong>Tests a specific hypothesis</strong> about the relationship of a disease to a specific cause,
    by relating the <strong>exposure</strong> of interest to the <strong>outcome</strong> of interest</td></tr>
    <tr><td>What it yields</td><td><strong>Formulates hypotheses</strong> and examines associations</td>
    <td>A <strong>cause-effect relationship</strong></td></tr>
    <tr><td>Typical designs</td><td>The <strong>community health survey</strong> (also called a
    <strong>cross-sectional</strong> or descriptive study)</td><td><strong>Cohort</strong>,
    <strong>case-control</strong> and <strong>experimental</strong> designs</td></tr>
    <tr><td>Its triad</td><td><strong>Person, place, time</strong></td><td><strong>Host, agent,
    environment</strong></td></tr>
  </table>
  <p><strong>Descriptive comes first.</strong> Before you undertake any analytic study you have to
  understand the descriptive components. The <strong>basic triad of descriptive epidemiology</strong> is
  person, place and time:</p>
  <ul>
    <li><strong>Person:</strong> age, gender, socio-economic status (education, occupation, income), marital
    status, ethnicity/race/genetic profile, behavior and habits.</li>
    <li><strong>Place:</strong> geographically restricted or widespread (outbreak, epidemic, pandemic)?
    off-shore (a tsunami)? climate effects (temperature, humidity); urban, suburban-squatter or rural;
    relation to environmental exposure (water, food supply); multiple clusters or one?</li>
    <li><strong>Time:</strong> changing or stable? <strong>clustered (epidemic) or evenly distributed
    (endemic)</strong>? Time trends: <strong>point source</strong> (localized and stationary),
    <strong>propagated</strong> (reflects a spreading infection; may be extended), <strong>seasonal</strong>,
    and <strong>secular</strong> (occurrence over a prolonged period, usually years).</li>
  </ul>
  <p>The <strong>basic triad of analytic epidemiology</strong> is the three phenomena it assesses:
  <strong>host, environment and agent</strong>.</p>
  <table>
    <tr><th>Agents</th><th>Host factors</th><th>Environment</th></tr>
    <tr><td><strong>Biological</strong> (microorganisms); <strong>physical</strong> (temperature, radiation,
    trauma); <strong>chemical</strong> (acids, alkalis, poisons, tobacco); <strong>environmental</strong>
    (nutrients in the diet, allergens); <strong>psychological</strong> experiences</td>
    <td>Genetic endowment; immunologic status; personal characteristics; personal behavior;
    <strong>definitive versus intermediate</strong> host (in vector-borne diseases)</td>
    <td>Living conditions (housing, crowding, water supply, refuse, sewage); atmosphere and climate;
    <strong>modes of communication</strong>, the phenomena that bring host and agent together, such as a
    <strong>vector, vehicle or reservoir</strong></td></tr>
  </table>
  <p><strong>John Snow&rsquo;s cholera investigations show both kinds.</strong></p>
  <ul>
    <li><strong>Descriptive</strong> (the outbreak in the Golden Square area of London): he marked where people
    with cholera lived and worked on a map, <strong>now called a spot map</strong>, and marked the water
    pumps. More cases were found near <strong>Pump A</strong> than near B or C; residents said they preferred
    Pump A; few cases occurred two blocks to the east, where a <strong>brewery with its own deep well</strong>
    let employees take their water (and a daily allotment of malt liquor). Households with cholera all drew
    from Pump A, the common factor. Officials were notified, the <strong>pump was closed and the outbreak
    ended</strong>.</li>
    <li><strong>Analytic</strong> (re-examining data from different outbreaks): the districts with the highest
    death rates were served by two water companies, Lambeth and Southwark and Vauxhall, both drawing from the
    Thames downstream from London. Lambeth then <strong>moved its intake upstream</strong>. Snow developed the
    hypothesis that water from below London was the source, and tested it by identifying the <strong>water
    source for every house with a cholera death</strong>. Houses supplied by Southwark and Vauxhall alone had
    a cholera death rate of 4.2 per 1,000 people; houses supplied by Lambeth alone, 0.5 per 1,000 (Table 1.2,
    slide 42).</li>
    <li>The point: <strong>without any knowledge of microbes</strong>, he established that water could
    transmit cholera and that epidemiological information can direct prompt public health action. Koch&rsquo;s
    postulates, which established cause and effect between microbes and disease, were published later
    (1884).</li>
  </ul>
  """ + fig("l12-s041-snow-spot-map.png", 382, 352,
      "A street map of part of London with many small dots marking cholera cases, clustered around a pump marked with an X labeled Pump A on Broad Street; other pumps marked B, C and two more lie farther away.",
      "<b>The spot map.</b> Each dot is a cholera case; the X&rsquo;s are pumps. The cases crowd around "
      "<b>Pump A</b> on Broad Street, which is what pointed Snow to the water.", 41) + """
  <p><strong>Noncommunicable disease</strong> uses the same descriptive groundwork (slide 70): define the
  population of interest; conceptualize and create measures of exposures and health indicators; take a
  sample of the population; estimate measures of association between exposures and health indicators;
  rigorously evaluate whether the association suggests a causal one; assess the evidence for causes working
  together; and assess whether the result is externally valid for other populations.</p>

  <h3 class="sub" id="epi-uses">12.2 &middot; Objective 2 &mdash; What epidemiology is, and the uses of epidemiologic training</h3>
  <p><strong>The word:</strong> <em>epi</em> = upon, <em>demos</em> = people, <em>ology</em> = science:
  &ldquo;the science which deals with what falls upon people.&rdquo; It is a <strong>bridge between the
  biomedical, social and behavioral sciences</strong>.</p>
  <p><strong>The 5 W&rsquo;s of epidemiology</strong>, a mnemonic for the fundamental questions of any
  epidemiological study:</p>
  <table>
    <tr><th>W</th><th>Asks about</th></tr>
    <tr><td>What</td><td>The health event or diagnosis</td></tr>
    <tr><td>Who</td><td>The person or population involved</td></tr>
    <tr><td>Where</td><td>The location of the event</td></tr>
    <tr><td>When</td><td>The time period of the event</td></tr>
    <tr><td>Why</td><td>The causes, risk factors and modes of transmission</td></tr>
  </table>
  <p><strong>Where epidemiology has impact</strong> (slide 6), each for its own reason: <strong>public
  health</strong> (the emphasis on disease prevention); <strong>clinical medicine</strong> (disease
  classification and diagnosis); <strong>pathophysiology</strong> (understanding basic biological
  mechanisms in disease); <strong>biostatistics</strong> (quantifying disease frequency and its relationships
  to antecedents); <strong>social sciences</strong> (the social context in which disease occurs and
  presents).</p>
  <p><strong>Uses of epidemiological training</strong> (slides 7&ndash;8):</p>
  <ul>
    <li><strong>Outbreak response</strong>: identifying, reporting and investigating outbreaks in a timely
    manner.</li>
    <li><strong>Public health surveillance</strong>: setting up, managing and evaluating surveillance
    systems.</li>
    <li><strong>Public health communication</strong>: developing and delivering it.</li>
    <li><strong>Disease prioritization</strong>: evaluating and prioritizing diseases of concern, including
    describing the clinical picture: who gets the disease, who dies from it, and what its outcome is.</li>
    <li><strong>Training and mentoring</strong> health professionals.</li>
    <li><strong>Experimental epidemiology</strong>: developing a hypothesis for a health concern and designing
    an experimental model to test it.</li>
    <li><strong>Program evaluation and management</strong>: evaluating prevention and intervention programs
    (for example vaccine and clinical trials) and managing their staff and resources.</li>
  </ul>

  <h3 class="sub" id="epi-history">12.3 &middot; Objective 3 &mdash; Key events in its history, including genomic epidemiology</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; &ldquo;you need to know genomic epidemiology&rdquo;</span>
  <p>Also on her closing list: &ldquo;the people who are important in history&rdquo; &mdash; know who did what.</p></div>
  <p>Epidemiology is <strong>relatively new as a formal scientific discipline</strong>, but
  &ldquo;counting&rdquo; health and disease goes back centuries; many of today&rsquo;s design and analytic
  techniques arose in response to health concerns of the 19th and 20th centuries.</p>
  <table>
    <tr><th>Who or when</th><th>What they contributed</th></tr>
    <tr><td><strong>Hippocrates</strong> (about 400 BC)</td><td>Explained disease from a <strong>rational
    rather than spiritual</strong> standpoint: environmental and host factors</td></tr>
    <tr><td><strong>John Graunt</strong> (17th century)</td><td>Pioneered <strong>tabulating population
    health and mortality</strong> in rates, ratios and proportions; noted differences between males and
    females, high infant mortality, urban/rural differences and seasonal variation</td></tr>
    <tr><td><strong>William Farr</strong> (1800s)</td><td>Systematically collected and analyzed Britain&rsquo;s
    mortality statistics: the <strong>father of modern vital statistics</strong>. Developed life-table
    approaches, and <strong>reported</strong> his statistics to the authorities and the public</td></tr>
    <tr><td><strong>John Snow</strong> (mid 1800s)</td><td>An anesthesiologist who used epidemiologic
    approaches on the London cholera epidemic: the <strong>father of field epidemiology</strong>. Developed
    and applied basic measures of disease frequency; his studies combine descriptive and analytic
    epidemiology (12.1)</td></tr>
    <tr><td>Mid to late 1800s</td><td>Focus on <strong>acute infectious diseases</strong></td></tr>
    <tr><td>1930s and 1940s</td><td>Methods extended to <strong>noninfectious</strong> diseases; after World
    War II, more development of research methods and theory; then health outcomes tied to behaviors and
    attitudes</td></tr>
    <tr><td><strong>Doll and Hill</strong> (1950)</td><td><strong>Smoking and lung cancer</strong></td></tr>
    <tr><td><strong>Framingham Heart Study</strong> (began 1948)</td><td>A <strong>multigenerational</strong>
    study to identify common factors contributing to <strong>cardiovascular disease</strong></td></tr>
    <tr><td>1960s and 1970s</td><td>Epidemiological methods applied to <strong>eradicate smallpox</strong>
    worldwide</td></tr>
    <tr><td>1980s</td><td>Extended to studies of <strong>injuries and violence</strong></td></tr>
    <tr><td>1990s, accelerating after 2001</td><td>The deliberate spread of disease: <strong>biologic warfare
    and bioterrorism</strong></td></tr>
    <tr><td>Continuing</td><td><strong>New</strong> infectious agents (Ebola virus, human immunodeficiency
    virus, severe acute respiratory syndrome, COVID) and <strong>changed</strong> ones (drug-resistant
    organisms such as tuberculosis, and variations of influenza)</td></tr>
  </table>
  <p><strong>Genomic epidemiology</strong>, one of the most important developments in the field, is the
  process of <strong>monitoring the genetic makeup of the pathogens</strong> that cause disease, made
  possible by advances in sequencing. It is one of the most reliable tools in outbreak investigation:</p>
  <ul>
    <li><strong>early outbreak detection</strong>: if the pathogens from different cases are closely related,
    the cases may be part of the same outbreak;</li>
    <li>identifying <strong>transmission links</strong> (a common pathway of spread);</li>
    <li>identifying or confirming <strong>sources of exposure</strong>;</li>
    <li>understanding disease location and <strong>spatial distribution</strong>, to link cases or outbreaks in
    different locations and confirm more definitively that they are part of the same outbreak.</li>
  </ul>

  <h3 class="sub" id="epi-data">12.4 &middot; Objective 4 &mdash; Common sources of epidemiologic data</h3>
  <table>
    <tr><th>Source</th><th>Method</th><th>Example</th></tr>
    <tr><td><strong>Individual persons</strong></td><td>Questionnaire; survey</td><td>A foodborne illness
    outbreak; the National Health and Nutrition Examination Survey of the CDC (Centers for Disease Control
    and Prevention): health data on United States residents</td></tr>
    <tr><td><strong>Environment</strong></td><td>Samples from the environment (river water, soil); sensors
    for environmental changes</td><td>Water collected from area streams and checked for chemical pollutants;
    air-quality ratings</td></tr>
    <tr><td><strong>Health care providers</strong></td><td>Notifications to the health department when cases
    of certain diseases are observed</td><td>Reporting cases of <strong>meningitis</strong> to the health
    department</td></tr>
    <tr><td><strong>Nonhealth-related sources</strong> (financial, legal)</td><td>Sales records; court
    records</td><td><strong>Cigarette sales</strong>; <strong>intoxicated-driver arrests</strong></td></tr>
  </table>

  <h3 class="sub" id="epi-surveillance">12.5 &middot; Objective 5 &mdash; Public health surveillance</h3>
  <p class="muted">Recording: the uses-of-surveillance-data table (slide 25) is not to be memorized (&ldquo;I
  don&rsquo;t want you to memorize this list&rdquo;); her closing list asks for &ldquo;the different kinds of
  surveillances&rdquo; &mdash; passive, active, sentinel and syndromic.</p>
  <p><strong>Public health surveillance</strong> is a tool that <strong>systematically collects, analyzes and
  interprets data</strong> to facilitate the prevention and control of disease. It measures what is going on
  in the population, the need for interventions and the effects of interventions; it informs decision
  making; and how it is done may differ between developed and developing nations. It must have a
  <strong>clear objective</strong> that includes how the data will be collected, consolidated and
  analyzed.</p>
  <table>
    <tr><th>Critical characteristic</th><th>Why it matters</th></tr>
    <tr><td><strong>Timeliness</strong></td><td>To implement effective control measures</td></tr>
    <tr><td><strong>Representation</strong></td><td>To give an accurate picture of the <strong>temporal
    trend</strong> of the disease</td></tr>
    <tr><td><strong>Sensitivity</strong></td><td>To <strong>identify individual persons with the
    disease</strong>, so they can be treated, quarantined or otherwise controlled</td></tr>
    <tr><td><strong>Specificity</strong></td><td>To <strong>exclude persons not having the disease</strong></td></tr>
  </table>
  <p><strong>Considerations when planning surveillance</strong> (slides 16&ndash;17): the health-related event
  and its <strong>case definition</strong>; the purpose and objectives; the planned uses of the data; the
  <strong>legal authority</strong> for collecting it; which organization conducts it and with which other
  health information systems; the data sources and collection method; the frequency (continuous or
  intermittent); the population under surveillance; how data are processed and managed; how
  <strong>confidentiality</strong> is maintained; how and by whom the data are analyzed; and how the
  information is disseminated, to everyone who needs it including the medical and public health communities
  and policymakers.</p>
  <p><strong>The vocabulary</strong> (slides 19&ndash;20):</p>
  <ul>
    <li><strong>Indicator</strong>: a measurable factor used to estimate the size of a health problem and to
    measure the effects of interventions.</li>
    <li><strong>Case surveillance</strong> is foundational to public health practice. It begins with
    <strong>local and state</strong> health departments collecting data about a case or person with a disease
    or condition that poses a serious health threat (infectious diseases, foodborne outbreaks, and
    noninfectious conditions such as lead poisoning); <strong>if the condition is notifiable, it is then
    reported to the CDC</strong> (Centers for Disease Control and Prevention).</li>
  </ul>
  <table>
    <tr><th>Type</th><th>How it works</th><th>Strengths and weaknesses</th></tr>
    <tr><td><strong>Active</strong></td><td><strong>Staff regularly contact</strong> health care providers for
    data</td><td><strong>Most accurate, but most expensive</strong>; often used for specific purposes, such as
    during outbreaks or seasonal events</td></tr>
    <tr><td><strong>Passive</strong></td><td>Relies on <strong>reports submitted</strong> by health care
    facilities and providers (includes routine health information systems)</td><td><strong>Most
    common</strong>, but less comprehensive; data quality is hard to control and it may lead to
    <strong>under-reporting</strong></td></tr>
    <tr><td><strong>Sentinel</strong></td><td>A <strong>prearranged group</strong> of reporting sources,
    normally health care providers, agrees to report all cases of specific conditions</td><td>A smaller
    representative group tracking on behalf of a much larger population; tries to get ahead of an
    outbreak</td></tr>
    <tr><td><strong>Syndromic</strong></td><td>Active or passive; case definitions based <strong>entirely on
    clinical features</strong> (diarrhea instead of cholera, for example)</td><td>The <strong>most frequently
    found system in developing countries</strong></td></tr>
    <tr><td><strong>Social media</strong></td><td>A source of data</td><td>Can be valuable for monitoring
    disease outbreaks and mental health issues</td></tr>
  </table>
  <p><strong>Uses of surveillance data</strong> (slide 25), by how quickly they are used:</p>
  <table>
    <tr><th>Immediate detection of</th><th>Periodic dissemination for</th><th>Stored information for</th></tr>
    <tr><td>Epidemics; newly emerging health problems; changes in health practices; changes in antibiotic
    resistance; changes in the distribution of the population at risk</td>
    <td>Estimating the magnitude of a health problem, including its cost; assessing control activities;
    setting research priorities; determining risk factors; facilitating planning; monitoring risk factors and
    changes in health practices; documenting the distribution and spread of disease and injury</td>
    <td>Describing the <strong>natural history of diseases</strong>; facilitating epidemiologic and laboratory
    research; validating the use of preliminary data; setting research priorities; documenting the
    distribution and spread of disease and injury</td></tr>
  </table>

  <h3 class="sub" id="epi-reportable">12.6 &middot; Objective 6 &mdash; Reportable (notifiable) diseases</h3>
  <p class="muted">Recording: the full notifiable-disease list (slide 23) is &ldquo;a list I&rsquo;m absolutely not
  requiring you to pay attention to.&rdquo; The definition and the reporting groups below are what count.</p>
  <p>A <strong>reportable (notifiable) disease</strong> is any disease that is <strong>required by law to be
  reported to government authorities</strong>. Diseases are made reportable because they are of public
  interest by reason of their <strong>contagiousness, severity or frequency</strong>. They include
  <strong>infectious</strong> diseases, <strong>bioterrorism agents</strong>, <strong>sexually
  transmitted</strong> infections and <strong>noninfectious</strong> conditions. Collecting the data lets
  authorities monitor the disease and gives <strong>early warning of potential outbreaks</strong>. In the
  United States, collection is done through the CDC&rsquo;s <strong>National Notifiable Diseases Surveillance
  System</strong>, and a list of notifiable diseases is <strong>produced every year</strong>.</p>
  <table>
    <tr><th>Group of reportable disease</th><th>Examples</th></tr>
    <tr><td>Mandatory <strong>written</strong> report</td><td>Gonorrhea, salmonellosis</td></tr>
    <tr><td>Mandatory report <strong>by telephone</strong></td><td>Rubeola (measles), pertussis</td></tr>
    <tr><td>Report of the <strong>total number of cases</strong></td><td>Chickenpox, influenza</td></tr>
    <tr><td><strong>Cancer</strong></td><td>Reported to <strong>state cancer registries</strong></td></tr>
  </table>
  <p>The national list (slide 23) runs from anthrax to Zika virus and shows how wide &ldquo;notifiable&rdquo;
  is: infections (botulism, cholera, Lyme disease, measles, syphilis, tuberculosis), resistant organisms
  (carbapenemase-producing carbapenem-resistant Enterobacteriaceae; vancomycin-intermediate and
  vancomycin-resistant <em>Staphylococcus aureus</em>), outbreaks as such (foodborne and waterborne disease
  outbreaks), and <strong>noninfectious conditions</strong> such as <strong>elevated blood lead levels, carbon
  monoxide poisoning, acute pesticide-related illness and silicosis</strong>. The CDC publishes weekly tables
  of notifiable disease cases by reporting area (slide 24).</p>

  <h3 class="sub" id="epi-measures">12.7 &middot; Objective 7 &mdash; Measures of morbidity and mortality</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; &ldquo;you should know the difference between incidence and prevalence&rdquo;</span>
  <p>Incidence counts new cases during a period; prevalence counts all cases present. Prevalence rises with incidence and with how long the disease lasts.</p></div>
  <p>Both are <strong>measures of the disease burden</strong> in a population.
  <strong>Morbidity</strong> is having a disease or a symptom of disease: the level of disease in a
  population, sometimes used to determine the risk of a disease. It is measured by
  <strong>incidence</strong> and <strong>prevalence</strong>. <strong>Mortality</strong> is the death rate,
  the number of deaths in a group of people at a particular time; it may be given by age, sex or cause.</p>
  <table>
    <tr><th></th><th>Incidence</th><th>Prevalence</th></tr>
    <tr><td>Definition</td><td>The proportion or rate of persons who <strong>develop</strong> a condition
    during a particular time period</td><td>The proportion of persons who <strong>have</strong> a condition at
    or during a particular time period</td></tr>
    <tr><td>Image</td><td>The <strong>speedometer</strong> (how fast new cases arrive)</td><td>The
    <strong>odometer</strong> (how many have accumulated)</td></tr>
    <tr><td>Numerator</td><td><strong>New cases</strong> that occurred during the time period</td><td><strong>All
    cases present</strong> during the time period</td></tr>
  </table>
  <ul>
    <li><strong>Prevalence depends on both incidence and the duration of illness.</strong> High prevalence
    may reflect high incidence, prolonged survival without cure, or both; low prevalence may mean low
    incidence, a <strong>rapidly fatal</strong> process, or <strong>rapid recovery</strong>.</li>
    <li><strong>Prevalence rather than incidence is often measured for chronic diseases</strong> such as
    diabetes or osteoarthritis, which last a long time and whose onset is hard to date.</li>
    <li><strong>Telling them apart in a formula</strong> (slide 28): the number of women in a town
    <em>reported with</em> heart disease in a health survey, over the number of women residents, is a
    <strong>prevalence</strong>; the number <em>newly diagnosed</em> in one year, over the women residents at
    mid-year, is an <strong>incidence</strong>.</li>
  </ul>
  <table>
    <tr><th>Mortality rate</th><th>Counts</th></tr>
    <tr><td><strong>Crude</strong></td><td>Deaths from <strong>all causes</strong> in a population in a given
    time period</td></tr>
    <tr><td><strong>Cause-specific</strong></td><td>Deaths from a <strong>specific cause</strong></td></tr>
    <tr><td><strong>Age-specific</strong></td><td>Deaths in a <strong>specific age group</strong></td></tr>
    <tr><td><strong>Infant</strong></td><td>Infant deaths; <strong>used to compare health status between
    countries</strong>. A concerning statistic for the United States, which ranks well below most other
    developed nations, with considerable disparities by race and socioeconomic status</td></tr>
    <tr><td><strong>Maternal</strong></td><td>Mortality associated with <strong>pregnancy</strong>; slide 30
    charts it by race and Hispanic origin for 2022 and 2023, highest for non-Hispanic Black women</td></tr>
  </table>
  <p><strong>Case fatality rate</strong> (slide 59) = <strong>deaths / total cases</strong>. Early in an
  outbreak it may be <strong>over-estimated</strong>, because the sickest cases are the ones hospitalized
  and counted; later it may be <strong>under-estimated</strong> as testing finds more mild cases, and a long
  time to resolution can make it look better than it is.</p>

  <h3 class="sub" id="epi-causation">12.8 &middot; Objective 8 &mdash; Association and causation</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; &ldquo;you should be able to tell me whether something is going to be more of an association or a causation&rdquo;</span>
  <p>Expect a described study to classify. A relationship between an exposure and a disease is an association; causation is inferred from association plus Hill&rsquo;s criteria (also on her closing list).</p></div>
  <ul>
    <li>Epidemiology <strong>does not determine the cause of a disease in a given individual</strong>. It
    determines the relationship, or <strong>association</strong>, between an exposure and the frequency of
    disease in <strong>populations</strong>. We <strong>infer</strong> causation from association and other
    factors.</li>
    <li><strong>Association</strong>: an identifiable relationship between an exposure and a disease. It
    implies that the exposure <em>might</em> cause the disease. Exposures associated with a difference in
    disease risk are often called <strong>risk factors</strong>. Most often, in public health, interventions
    are designed on the basis of associations.</li>
    <li><strong>Causation</strong>: implies a <strong>true mechanism</strong> leading from exposure to disease.
    <strong>Finding an association does not make it causal.</strong></li>
  </ul>
  <p><strong>The pyramid of associations</strong> (slide 44), from its broad base to its narrow top:
  <strong>chance</strong>, <strong>spurious/artifact</strong>, <strong>confounded</strong>,
  <strong>non-causal</strong>, and at the apex <strong>causal</strong>.</p>
  <p><strong>Models of causation</strong> (slide 45): a <strong>cause</strong> is an event or condition that
  plays a role in producing an occurrence of a disease. It is <strong>not generally a single factor</strong>:
  most diseases come from an interplay of factors, from exposure plus additional factors to a whole web.</p>
  """ + fig("l12-s045-web-of-causation.png", 424, 381,
      "A spider web with the word Disease at its center and strands labeled phenotype, social organization, behavior, microbes, environment, genes, workplace and unknown factors.",
      "<b>The web of causation.</b> Genes, phenotype, microbes, behavior, social organization, environment, the "
      "workplace and unknown factors all feed one disease: causes are rarely single.", 45) + """
  <p><strong>Hill&rsquo;s criteria for causal inference</strong> (slides 46&ndash;52):</p>
  <table>
    <tr><th>Criterion</th><th>What it asks</th></tr>
    <tr><td><strong>Consistency of findings</strong></td><td>Shown in <strong>multiple studies</strong>, across
    different populations, in differing circumstances, with different study designs</td></tr>
    <tr><td><strong>Strength of association</strong></td><td>A strong association is <strong>less likely to be
    caused by chance or bias</strong>; it is one in which the <strong>relative risk is either very high or
    very low</strong></td></tr>
    <tr><td><strong>Biological gradient</strong> (dose-response)</td><td>Changes in exposure are related to a
    <strong>trend in relative risk</strong>; <strong>one of the most reliable indicators of
    causality</strong></td></tr>
    <tr><td><strong>Temporal sequence</strong></td><td>The <strong>exposure must precede the disease</strong>;
    in diseases with latency periods, it must precede the latent period; chronic diseases often need
    long-term exposure</td></tr>
    <tr><td><strong>Biological plausibility</strong> and <strong>coherence</strong></td><td>The proposed
    mechanism should be biologically plausible and must not contradict what is known about the natural
    history and biology of the disease; but the relationship may be indirect, data may not yet support the
    mechanism directly, and existing understanding may need reinterpreting in the face of new findings</td></tr>
    <tr><td><strong>Specificity of association</strong></td><td>An exposure leads to a single or
    characteristic effect, or affects people with a specific susceptibility; easier to support causation when
    associations are specific, but <strong>many exposures cause multiple diseases</strong></td></tr>
  </table>
  <p><strong>A dose-response example</strong> (slide 49): standardized mortality ratios for lung cancer rise
  with cigarettes smoked per day in each of three studies.</p>
  <table>
    <tr><th>Dose (cigarettes a day)</th><th>Study 1</th><th>Study 2</th><th>Study 3</th></tr>
    <tr><td>Fewer than 10</td><td>1.3</td><td>1.8</td><td>1.4</td></tr>
    <tr><td>10&ndash;20</td><td>2.8</td><td>2.3</td><td>2.4</td></tr>
    <tr><td>More than 40</td><td>4.7</td><td>3.7</td><td>6.3</td></tr>
  </table>
  <p><strong>The prevailing wisdom</strong> (slide 53): most judgments of cause and effect are
  <strong>tentative, and open to change with new evidence</strong>.</p>

  <h3 class="sub" id="epi-terms">12.9 &middot; Objective 9 &mdash; Endemic, epidemic, pandemic, sporadic, herd immunity</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; &ldquo;these different kinds of epidemics can be graphed and show different patterns, which you should be able to identify&rdquo;</span>
  <p>Read each curve below by its shape: one sharp peak (point), cases over the exposure period (continuous), successive waves (propagated), a common source then person to person (mixed).</p></div>
  <table>
    <tr><th>Term</th><th>Definition</th></tr>
    <tr><td><strong>Endemic</strong></td><td>Diseases found at <strong>chronically low levels</strong> in a
    population</td></tr>
    <tr><td><strong>Sporadic</strong></td><td>Diseases that occur at <strong>irregular intervals</strong>, or
    as <strong>isolated incidents</strong></td></tr>
    <tr><td><strong>Epidemic</strong></td><td>Diseases occurring <strong>in excess of what might be
    expected</strong> in a population, or as an <strong>uncontrolled spread</strong> in a community</td></tr>
    <tr><td><strong>Pandemic</strong></td><td><strong>World-wide epidemics</strong></td></tr>
  </table>
  <p><strong>Types of epidemics</strong> (slides 55&ndash;58):</p>
  <ul>
    <li><strong>Common source</strong>: a group exposed to the same source. <strong>Point</strong>: the
    exposure is brief, <strong>within one incubation period</strong>. <strong>Continuous</strong>: exposure
    over a longer time. <strong>Intermittent</strong>.</li>
    <li><strong>Propagated</strong>: <strong>person-to-person</strong> transmission.</li>
    <li><strong>Mixed</strong>: may start as a common source and then be propagated.</li>
    <li><strong>Other</strong>: often <strong>zoonotic or vector-borne</strong>.</li>
  </ul>
  <p><strong>Reading the epidemic curves.</strong> Each figure plots cases by date of onset.</p>
  """ + fig("l12-s056-point-source-curve.png", 520, 355,
      "Bar chart of hepatitis A cases by date of onset in November and December: a single food-handler case early in November marked as the presumed index case, then one tall, narrow peak of cases a few weeks later with a smooth rise and fall, and a few secondary cases at the end.",
      "<b>Point source.</b> Hepatitis A traced to a food handler: one sharp peak, because everyone was "
      "exposed at about the same time (within one incubation period); the few late cases are secondary.", 56) + """
  """ + fig("l12-s056-continuous-source-curve.png", 484, 407,
      "Bar chart of diarrheal illness in city residents from mid December to mid January, bloody and nonbloody cases, with arrows marking water main breaks, a boil water order and chlorination; cases rise after the main breaks, stay high for weeks and fall after the boil water order and chlorination.",
      "<b>Continuous common source.</b> Diarrheal illness after water main breaks: cases keep coming for "
      "weeks because the exposure continues, until the boil-water order and chlorination remove it.", 56) + """
  """ + fig("l12-s057-propagated-curve.png", 531, 316,
      "Bar chart of measles cases by day of onset from October 1970 to January 1971: scattered early cases, then successive peaks in November and December, each larger than the one before.",
      "<b>Propagated.</b> Measles spreading person to person: a few scattered cases, then successive, "
      "larger peaks.", 57) + """
  """ + fig("l12-s057-mixed-curve.png", 541, 503,
      "Bar chart of Shigella cases at a music festival in August by day of onset, staff and attendees: a few staff cases before the festival, then a tall peak of attendee cases during the festival days, then smaller later bars.",
      "<b>Mixed.</b> <em>Shigella</em> at a music festival: staff cases before the festival, a tall peak "
      "among attendees during it, smaller bars after. A mixed epidemic may start as a common source and then "
      "be propagated.", 57) + """
  """ + fig("l12-s058-lyme-by-year.png", 547, 386,
      "Bar chart of reported Lyme disease cases in the United States by year from 1992 to 2003, rising gradually with year-to-year variation.",
      "<b>Other</b> (often zoonotic or vector-borne): reported Lyme disease cases in the United States by "
      "year. Slide 58 pairs it with West Nile encephalitis in New York City, 1999.", 58) + """
  <p><strong>Reproduction numbers</strong> (slide 59): <strong>R0, the basic reproduction number</strong>, is the
  number of cases directly generated by one case in a <strong>susceptible population without
  interventions</strong>; <strong>R, the effective reproduction number</strong>, is the number generated by one
  case <strong>with interventions or immunity</strong>.</p>
  <p><strong>Immunity</strong> is inherited, acquired or induced resistance to infection by a specific
  pathogen; acquired resistance after a previous infection comes from protective cellular and antibody
  responses. <strong>Herd immunity</strong> is the <strong>cumulative number of immune persons in a
  population, or the percentage of the population that is immune</strong>. It is often discussed in relation
  to <strong>vaccination</strong> against a particular pathogen, and is also affected by natural immunity gained
  by recovering from the infection.</p>

  <h3 class="sub" id="epi-applications">12.10 &middot; Objective 10 &mdash; Applications of epidemiology</h3>
  <p>Five applications (slide 61): <strong>outbreak investigation, policy development, social and behavioral
  issues, environmental issues, and occupational health and safety</strong>.</p>
  <p><strong>Outbreak investigation</strong> of a communicable disease, in order (slide 62):</p>
  <ol>
    <li>Establish the existence of an outbreak.</li>
    <li>Prepare for field work.</li>
    <li>Verify the diagnosis.</li>
    <li>Define and identify cases.</li>
    <li>Use descriptive epidemiology to describe and orient the data.</li>
    <li>Develop a focused hypothesis.</li>
    <li>Evaluate the hypothesis for validity.</li>
    <li>Refine the hypothesis as needed.</li>
    <li>Implement control and prevention methods.</li>
    <li>Communicate findings: determine who needs to know, how the information will be communicated, and why
    it needs to be communicated.</li>
  </ol>
  <p><strong>The worked outbreak: Legionnaires&rsquo; disease</strong> (slides 63&ndash;68). In late July 1976 an
  epidemic of fatal respiratory disease struck people attending an American Legion convention in
  Philadelphia, and some non-attendees, some within days of the convention. Doctors with the first cases
  tried to contact the state health department, but it was <strong>closed for the weekend</strong>, and deaths
  had already mounted by Monday; the CDC and the state health department then took on the investigation.
  <strong>Five months</strong> after the first cases, a <strong>case-control study</strong> showed that
  <strong>spending time in the lobby of Hotel A</strong> was a risk factor for illness, and in December 1976 a
  CDC laboratorian located the <strong>source bacteria</strong> by continuing to test specimens that had been
  thought to be dead. Then: implement control and prevention measures, and communicate the findings.</p>
  <p><strong>A public health approach</strong> (slide 71) runs from the problem to the response:</p>
  """ + fig("l12-s071-public-health-approach.png", 1405, 494,
      "Four boxes in a row: Surveillance, what is the problem; Risk factor identification, what is the cause; Intervention evaluation, what works; Implementation, how do you do it; an arrow beneath runs from Problem to Response.",
      "<b>From problem to response.</b> Surveillance (<em>what is the problem?</em>) &rarr; risk factor "
      "identification (<em>what is the cause?</em>) &rarr; intervention evaluation (<em>what works?</em>) &rarr; "
      "implementation (<em>how do you do it?</em>).", 71) + """
  <p><strong>Policy development</strong> (slides 72&ndash;73). Rigorously conducted, reported and communicated
  epidemiological studies can produce major health policy changes. Policy is built on <strong>values,
  ideology, politics and evidence</strong>; <strong>evidence is the main contribution of
  epidemiology</strong>, and it is <strong>not usually the main influence on policy</strong>, but it is worth
  fighting for. The <strong>policy cycle</strong>, in order:</p>
  <ol>
    <li><strong>Assessment of population health</strong>: identify the issue affecting population health.</li>
    <li><strong>Assessment of potential interventions</strong>: identify interventions and provide evidence of
    their efficacy.</li>
    <li><strong>Policy choices</strong>: made with tools such as computer modeling, then delivered for a
    consensus decision.</li>
    <li><strong>Policy implementation</strong>: set target goals and allocate the resources.</li>
    <li><strong>Policy evaluation</strong>: collect data on the results of the intervention, and plan future
    modeling.</li>
  </ol>
  <p><strong>Youth smoking</strong> (slide 74), the worked policy example. By the 1960s smoking had been linked
  to multiple health problems, and adult smoking fell by the 1980s, but youth smoking did not. The 1994
  Surgeon General&rsquo;s report recommended moving <strong>from campaigns aimed at individual young people to
  treating it as a community and population issue</strong>. The American Stop Smoking Intervention Study for
  Cancer Prevention used the epidemiological evidence that <strong>secondhand smoke</strong> is dangerous to
  reframe smoking as a <strong>societal rather than personal</strong> concern. The measures:
  <strong>eliminating tobacco smoke in public places</strong>, <strong>less advertising and promotion</strong>,
  <strong>less youth access</strong> to tobacco, and <strong>higher tobacco taxes</strong>.</p>
  <p><strong>Social and behavioral factors</strong> (slide 75) matter because they help explain how diseases
  spread and why health outcomes vary across populations. This work looks at how <strong>income inequality,
  poverty, race and discrimination</strong> affect health, including <strong>access to health care</strong>;
  at how <strong>behavioral risk factors</strong> contribute to disease; and it contributes to policy in these
  areas.</p>
  <p><strong>Environmental epidemiology</strong> (slide 76) studies how environmental factors affect human
  health: exposure to <strong>air and water pollution</strong>, or to <strong>hazardous waste disposal
  sites</strong>.</p>
  <p><strong>Occupational health</strong> epidemiology studies how <strong>workers&rsquo; health</strong> is
  affected by workplace conditions and exposure to hazardous substances: it monitors how often workers are
  injured or ill, identifies which groups of workers are most affected, determines the reasons, and uses the
  findings to <strong>reduce the risk through regulatory practice</strong>.</p>

  <h3 class="sub" id="epi-notes">12.11 &middot; Where the slides need a second look</h3>
  <p>Nothing in this deck contradicts current practice on a point the quizzes ask. A few details are worth
  knowing so they do not confuse you; <strong>none is the basis of a quiz question</strong>.</p>
  <ul>
    <li><strong>Snow&rsquo;s Table 1.1 (slide 42)</strong> prints the population served by both companies as
    &ldquo;1300,149&rdquo;, a typo for 300,149. The house-by-house Table 1.2 is the one that carries the
    argument.</li>
    <li><strong>The Legionnaires&rsquo; attack-rate table (slide 66)</strong> labels its three column groups
    Hotel A, Hotel B and Hotel C, but the third group is the <em>total</em> of the first two (62 + 63 = 125
    ill). The figures, like the case and death counts, are context rather than exam material.</li>
    <li><strong>Slide 21</strong> writes &ldquo;Center for Disease Control&rdquo;; the agency is the Centers
    for Disease Control and Prevention.</li>
    <li><strong>Infant and maternal mortality figures</strong> (slides 29&ndash;30) are given as context for the
    two rates; the numbers and the ranking are not asked.</li>
  </ul>
"""

SECTION_FOOT = """
  <button type="button" class="test-yourself-btn" onclick="window.openTestYourself('Test yourself &mdash; Epidemiology', TEST_YOURSELF.epidemiology)">Test yourself! &rarr;</button>
  <p class="src">Source: <em>Epidemiology</em> (Lecture 12 Dr. Webster - Epidemiology.pptx), Slides 1&ndash;76,
  and the PAJ 5200 syllabus instructional objectives.</p>
</section>
"""

TEST = """
    epidemiology: [
      {q:"Which study design belongs to descriptive rather than analytic epidemiology?",
       choices:["Case-control study","Community health survey","Cohort study","Experimental trial"],correct:1,
       explain:"The community health survey (cross-sectional) describes distribution by person, place and time and generates hypotheses. Cohort, case-control and experimental designs test them."},
      {q:"The numerator of prevalence counts which cases?",
       choices:["Only deaths","Only new cases","Only cured cases","All cases present"],correct:3,
       explain:"Prevalence counts every case present during the period (the odometer); incidence counts only new cases (the speedometer)."},
      {q:"Which of Hill's criteria says the exposure must come before the disease?",
       choices:["Temporal sequence","Specificity","Consistency","Biological gradient"],correct:0,
       explain:"Temporal sequence: exposure must precede the disease, and in diseases with a latency period it must precede the latent period."},
      {q:"Which surveillance type is the most accurate but the most expensive?",
       choices:["Passive","Syndromic","Active","Sentinel"],correct:2,
       explain:"Active surveillance uses staff to contact providers regularly; passive, the most common, relies on submitted reports and may under-report."},
      {q:"What does R0 count?",
       choices:["Deaths per total cases","Cases from one case in a susceptible population without interventions","Immune persons in a population","New cases per year"],correct:1,
       explain:"R0, the basic reproduction number, assumes no interventions; R, the effective number, is measured with interventions or immunity."}
    ],
"""


def section():
    return SECTION_HEAD + BODY + SECTION_FOOT


SECTION = None   # set by build(); build_micro_e2_guide.py reads SECTION after import


def build():
    global SECTION
    SECTION = section()
    return SECTION


build()
