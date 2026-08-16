#!/usr/bin/env python3
"""Build the Clinical Pathophysiology I, Exam 1 study guide (Inflammation).

Same skeleton-lift as build_cms_guide.py: head/CSS/scripts come from the PD1
Exam 3 guide, which carries the site's guide design system, and the TOC, body
and TEST_YOURSELF are spliced in. Retheme is the violet identity used by this
class's quizzes.

Scope note: this class is pathophysiology, so the guide stays on mechanism.
No management, no treatment — see the clin_path_exam_spec memory for why that
line matters against Clinical Medicine and Surgery I.
"""
import os, re

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
DONOR = os.path.join(ROOT, "Physical Diagnosis 1 Exam 3/pd1-exam3-study-guide.html")
OUT = os.path.join(ROOT, "Clinical Pathophysiology I Exam 1/cp-exam-1-study-guide.html")
IMGS = "cp-exam-1-study-guide-images"

FIG1 = ('<figure class="fig"><img width="1100" height="819" loading="lazy" src="%s/001.jpg" '
        'alt="Diagram of the sequence of events in inflammation, running left to right from a '
        'pre-capillary arteriole through a capillary to a post-capillary venule, labelled with '
        'neurologic, acute vascular, acute cellular, chronic cellular and healing phases.">'
        '<figcaption>The single most useful figure in this lecture, because it puts every objective '
        'on one timeline. Read it left to right: immediate vasoconstriction at the arteriole, then '
        'mediators from mast cell degranulation driving vasodilation and endothelial cell '
        'contraction, then increased vascular permeability producing transudate and exudate, then '
        'chemotaxis and emigration of neutrophils, and only later the lymphocytes and macrophages '
        'of the chronic phase, ending in fibrin deposition, fibrosis and scar. Note the '
        'vertical divisions: the vascular events happen at the arteriole and capillary, while the '
        'cellular emigration happens at the post-capillary venule — the anatomy changes as the '
        'response progresses, which is why objectives (d) and (e) are separated in the first place. '
        '<span class="src">Figure 12-1, reproduced from the lecture slides (Slide 13).</span>'
        '</figcaption></figure>\n  ') % IMGS

TOC = '''<nav class="toc">
  <h2>Contents</h2>
  <a class="top-link" href="#inflammation">1 &middot; Inflammation</a>
  <a href="#inf-mechanisms">1.1 Objective a &mdash; Molecular mechanisms</a>
  <a href="#inf-types">1.2 Objective b &mdash; Types &amp; etiologies</a>
  <a href="#inf-patterns">1.3 Objective b &mdash; Patterns of inflammation</a>
  <a href="#inf-leukocytes">1.4 Objective c &mdash; White blood cells</a>
  <a href="#inf-vascular">1.5 Objective d &mdash; Vascular changes</a>
  <a href="#inf-cellular">1.6 Objective e &mdash; Cellular changes</a>
  <a href="#inf-mediators">1.7 Objective f &mdash; Mediators &amp; opsonins</a>
</nav>'''

BODY = '''<main>

<section class="deck" id="inflammation">
  <h2 class="deck-title">1 &middot; Inflammation</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol type="a">
      <li>Describe the molecular mechanisms of inflammatory processes</li>
      <li>Describe the various types and etiologies of inflammation</li>
      <li>Compare and contrast the mechanism of white blood cells in the inflammatory response</li>
      <li>Describe the vascular changes associated with acute inflammation</li>
      <li>Describe the cellular changes associated with acute inflammation</li>
      <li>Compare and contrast mediators of inflammation and their functions</li>
    </ol>
  </div>
  <div class="callout"><strong>Objective (d) wording.</strong> The syllabus says <em>vascular
  changes</em>; the slide says <em>vascular effects</em>. The syllabus wording is the one used here
  and on the exams.</div>

  <h3 class="sub" id="inf-mechanisms">1.1 &middot; Objective a &mdash; Molecular mechanisms of inflammatory processes</h3>
  <p><strong>Inflammation is the reaction of vascularized living tissue to injury.</strong> The word
  <em>vascularized</em> is doing real work in that definition &mdash; tissue without a blood supply
  cannot mount the response at all. The process is a sequence of events that heals the injury or
  implant site, either by generating new tissue from native parenchymal cells or by forming
  fibroblastic scar tissue.</p>
  ''' + FIG1 + '''
  <p><strong>The five main processes</strong>, in order:</p>
  <table>
    <tr><th>#</th><th>Process</th></tr>
    <tr><td>I</td><td>Increased blood flow</td></tr>
    <tr><td>II</td><td>Increased permeability</td></tr>
    <tr><td>III</td><td>Migration of neutrophils</td></tr>
    <tr><td>IV</td><td>Chemotaxis</td></tr>
    <tr><td>V</td><td>Leucocyte recruitment &amp; activation</td></tr>
  </table>
  <div class="pearl">The three vascular mechanisms are a causal chain, not a list:
  <strong>vasodilation</strong> of the arterioles raises blood flow &rarr; <strong>endothelial
  contraction</strong> opens the capillaries to increased permeability &rarr; <strong>exudation</strong>,
  fluid and blood proteins moving into the interstitial spaces. Each step is what makes the next
  possible, which is why the order is examinable.</div>

  <h3 class="sub" id="inf-types">1.2 &middot; Objective b &mdash; Types and etiologies of inflammation</h3>
  <table>
    <tr><th></th><th>Acute</th><th>Chronic</th></tr>
    <tr><td>Timescale</td><td>Seconds, minutes, hours or days &mdash; begins <strong>within seconds</strong> of injury</td>
        <td>Longer &mdash; days, weeks, months</td></tr>
    <tr><td>Histology</td><td>Neutrophil-predominant exudate</td>
        <td>White blood cells (lymphocytes and macrophages), proliferation of blood vessels, fibrosis, tissue necrosis</td></tr>
    <tr><td>Nature of damage</td><td>May be purely physical, or may involve activation of an immune response (trauma versus a bee sting)</td>
        <td>Driven by persistence rather than by the initial insult</td></tr>
  </table>
  <p><strong>The three causes of chronic inflammation</strong>, each with the lecture's own examples:</p>
  <table>
    <tr><th>Cause</th><th>Examples</th></tr>
    <tr><td>Persistent infection</td><td>Bacteria, viruses, fungi, parasites</td></tr>
    <tr><td>Prolonged exposure to potentially toxic agents</td>
        <td><strong>Endogenous</strong> &mdash; atherosclerosis · <strong>Exogenous</strong> &mdash; particulates such as silica</td></tr>
    <tr><td>Autoimmunity</td><td>Rheumatoid arthritis, lupus</td></tr>
  </table>

  <h3 class="sub" id="inf-patterns">1.3 &middot; Objective b &mdash; Patterns of inflammation</h3>
  <p>Chronicity and pattern are two independent axes. A process is acute <em>or</em> chronic, and
  separately shows one of these patterns:</p>
  <table>
    <tr><th>Pattern</th><th>What defines it</th></tr>
    <tr><td>Serous</td><td>Largely plasma, low protein; occurs early or with mild inflammation</td></tr>
    <tr><td>Fibrinous</td><td>Large amounts of fibrinogen forming a thick meshwork; removable only by fibrolytic enzymes &mdash; failure of that results in scar tissue formation</td></tr>
    <tr><td>Suppurative (purulent)</td><td>Remnants of white blood cells, protein and tissue debris &mdash; that is, pus</td></tr>
    <tr><td>Hemorrhagic</td><td>Damage to blood vessels; occurs alongside other exudates</td></tr>
    <tr><td>Catarrhal</td><td>Mucus hypersecretion accompanying inflammation of a mucous membrane</td></tr>
    <tr><td>Ulcerative</td><td>Necrosis and sloughing of surface epithelium, exposing underlying connective tissue</td></tr>
    <tr><td>Pseudomembranous</td><td>Superficial necrotic layer of fibrin, inflammatory cells and debris forming a membrane-like covering over the affected mucosa</td></tr>
    <tr><td>Gangrenous</td><td>Severe necrosis with or without superimposed bacterial infection &mdash; <strong>dry</strong> is coagulative necrosis, <strong>wet</strong> is liquefactive necrosis from infection</td></tr>
  </table>
  <div class="pearl">Ulcerative versus pseudomembranous is the pair most often confused, and the
  distinction is directional: ulcerative <em>removes</em> the surface and exposes what is beneath;
  pseudomembranous <em>adds</em> a layer on top of the mucosa.</div>

  <h3 class="sub" id="inf-leukocytes">1.4 &middot; Objective c &mdash; Mechanism of white blood cells</h3>
  <table>
    <tr><th></th><th>Granulocytes (polymorphonuclear, PMN)</th><th>Agranulocytes (mononuclear)</th></tr>
    <tr><td>Defining feature</td><td>Differently staining granules in the cytoplasm on light microscopy &mdash; membrane-bound enzymes that digest phagocytized particles</td>
        <td>Apparent absence of granules &mdash; though they <em>do</em> contain non-specific azurophilic granules (lysosomes)</td></tr>
    <tr><td>Members</td><td>Neutrophils, basophils, eosinophils</td><td>Lymphocytes (B and T cells), monocytes, macrophages</td></tr>
  </table>
  <p><strong>Note the terminology trap:</strong> PMN refers to <em>all</em> granulocytes, not to
  neutrophils alone, even though neutrophils are the ones usually meant in conversation.</p>
  <table>
    <tr><th>Cell</th><th>Nucleus &amp; granules</th><th>Role</th></tr>
    <tr><td>Neutrophil</td><td>Multilobed nucleus that may look like multiple nuclei; cytoplasm appears transparent from fine pale lilac granules</td>
        <td>First responder to microbial infection; bacterial and fungal defence; very active phagocyte. <strong>Cannot renew its lysosomes</strong>, so dies after a few pathogens &mdash; their death in large numbers forms pus</td></tr>
    <tr><td>Basophil</td><td>Bi- or tri-lobed nucleus; coarse granules</td>
        <td>Allergic and antigen response via <strong>histamine</strong></td></tr>
    <tr><td>Eosinophil</td><td>Bi-lobed nucleus; granules a characteristic pink-orange</td>
        <td>Parasitic infections; predominant cell in allergic reactions &mdash; asthma, hay fever, hives</td></tr>
    <tr><td>B lymphocyte</td><td>Agranulocyte</td>
        <td>Humoral immunity: makes antibodies, acts as antigen-presenting cell, becomes memory B cells. Essential to adaptive immunity</td></tr>
    <tr><td>T lymphocyte</td><td>Matures in the <strong>T</strong>hymus; carries T cell receptors</td>
        <td>Cell-mediated immunity (subsets below)</td></tr>
    <tr><td>Monocyte</td><td>Kidney-shaped nucleus; abundant, usually agranulated cytoplasm</td>
        <td>Phagocytoses then presents pathogen fragments to T cells; leaves the bloodstream to become a tissue macrophage. <strong>Can replace its lysosomal contents</strong></td></tr>
  </table>
  <div class="callout"><strong>The neutrophil/monocyte contrast is the point of objective (c).</strong>
  Both phagocytose. The neutrophil cannot renew its lysosomes and dies after a few pathogens, which
  makes it a disposable first responder and explains pus. The monocyte can replace its lysosomal
  contents and keeps working, which is why it is the cell of the sustained, chronic phase.</div>
  <table>
    <tr><th>T cell subset</th><th>Function</th></tr>
    <tr><td>T helper cells</td><td>Activate and regulate T and B cells</td></tr>
    <tr><td>CD8+ cytotoxic T cells</td><td>Virus-infected and tumour cells</td></tr>
    <tr><td>Regulatory (suppressor) T cells</td><td>Return immune function to normal after infection; prevent autoimmunity</td></tr>
    <tr><td>Natural killer cells</td><td>Virus-infected and tumour cells</td></tr>
  </table>

  <h3 class="sub" id="inf-vascular">1.5 &middot; Objective d &mdash; Vascular changes in acute inflammation</h3>
  <p>The reviewed sequence opens with four vascular events, in this order:</p>
  <table>
    <tr><td>1</td><td>Vasoconstriction</td></tr>
    <tr><td>2</td><td>Vasodilation</td></tr>
    <tr><td>3</td><td>Increased vascular permeability</td></tr>
    <tr><td>4</td><td>Haemoconcentration and stasis</td></tr>
  </table>
  <div class="pearl">Vasoconstriction coming <em>first</em> catches people out, since the visible
  signs of inflammation are all dilation. Note also why stasis matters mechanistically: slowed flow
  is what lets leukocytes reach and stay against the endothelium, so it is the hinge between the
  vascular and cellular halves of the response.</div>

  <h3 class="sub" id="inf-cellular">1.6 &middot; Objective e &mdash; Cellular changes in acute inflammation</h3>
  <p>The sequence continues with five cellular events:</p>
  <table>
    <tr><td>5</td><td>Leukocyte adhesion</td></tr>
    <tr><td>6</td><td>Transmigration</td></tr>
    <tr><td>7</td><td>Chemotaxis</td></tr>
    <tr><td>8</td><td>Aggregation</td></tr>
    <tr><td>9</td><td>Phagocytosis</td></tr>
  </table>
  <p><strong>Acute inflammation in review:</strong> short term (minutes to days), with exudation of
  fluid, plasma, proteins and leukocytes (neutrophils), then phagocytosis and enzymatic release.
  Activated neutrophils and macrophages digest foreign material through four steps &mdash;
  <strong>recognition, attachment, engulfment, degradation</strong> &mdash; and recognition and
  attachment are enhanced when serum factors (opsonins) are present.</p>
  <p><strong>Chronic inflammation in review:</strong> long term (at least days), characterised by
  macrophages, monocytes and mononuclear cells including lymphocytes and plasma cells, accompanied
  by proliferation of blood vessels and connective tissue. Lymphocytes and plasma cells mediate
  antibody production; macrophages process and deliver antigen to immunocompetent cells.</p>

  <h3 class="sub" id="inf-mediators">1.7 &middot; Objective f &mdash; Mediators of inflammation and their functions</h3>
  <table>
    <tr><th>Mediator</th><th>Function</th></tr>
    <tr><td><strong>Histamine</strong></td><td><em>First</em> mediator of the initial inflammatory response. Dilates arterioles and increases permeability of capillaries and venules</td></tr>
    <tr><td><strong>Serotonin</strong></td><td>Vasodilation and increased vascular permeability</td></tr>
    <tr><td colspan="2"><em>Plasma proteins</em></td></tr>
    <tr><td><strong>Bradykinin</strong></td><td>Increases capillary permeability, <strong>causes pain</strong>, and may increase leukocyte chemotaxis</td></tr>
    <tr><td><strong>Complement components</strong></td><td>10% of circulating serum proteins; chemotactic to neutrophils and monocytes; the cascade may damage bacteria</td></tr>
    <tr><td><strong>Coagulation system</strong></td><td>Creates a fibrous network at the site to trap exudate, microorganisms and foreign bodies, and stops bleeding so repair can begin</td></tr>
  </table>
  <div class="pearl">Histamine, serotonin and bradykinin all raise permeability. <strong>Only
  bradykinin causes pain</strong> &mdash; that is the discriminating feature if a question gives you
  the effects and asks for the mediator.</div>
  <p><strong>Opsonins</strong> are proteins that adhere to foreign material and make it easier for
  immune cells to recognise and attach to it.</p>
  <table>
    <tr><th>Opsonin</th><th>What it is</th><th>Recognised by</th></tr>
    <tr><td>Immunoglobulin G (IgG)</td><td>An antibody</td><td><strong>Fc receptors</strong> on macrophages and neutrophils, which recognise the Fc portion</td></tr>
    <tr><td>Complement fragment C3b</td><td>Produced when the complement system is activated; binds microorganisms or foreign material</td><td><strong>Complement receptors</strong> on immune cells</td></tr>
  </table>
  <div class="callout"><strong>Clinical application worth remembering.</strong> A biomaterial &mdash;
  anything not human put into a human &mdash; becomes coated with immunoglobulin G and C3b. Immune
  cells recognise that coating and attach to the material, which is why <em>an implanted medical
  device can provoke an inflammatory response even when it is completely sterile</em>. The response
  is to the opsonised surface, not to infection.</div>
  <button type="button" class="test-yourself-btn" style="--acc:#6a4fa3" onclick="window.openTestYourself('Test yourself — Inflammation', TEST_YOURSELF.inflammation)">Test yourself! &rarr;</button>
  <p class="src">Source: <em>1. Inflammation.pptx</em> (Professor Lauren Reynolds), Slides 1&ndash;35, and the
  PAJ 5101 syllabus instructional objectives. Course text: Robbins &amp; Cotran <em>Pathologic Basis of
  Disease</em>, 10th edition &mdash; Chapter 3, &ldquo;Inflammation and Repair&rdquo;.</p>
</section>

</main>'''

TEST_YOURSELF = '''  var TEST_YOURSELF = {
    inflammation: [
      {q:"Which vascular event comes FIRST in the sequence of acute inflammation?",
       choices:["Vasodilation","Vasoconstriction","Increased vascular permeability","Haemoconcentration and stasis"],correct:1,
       explain:"The sequence opens with vasoconstriction, then vasodilation, then increased permeability, then haemoconcentration and stasis. Vasoconstriction first is the part most often missed, since every visible sign of inflammation is a dilation sign."},
      {q:"Why does a neutrophil die after phagocytosing only a few pathogens?",
       choices:["It lacks digestive enzymes","It cannot renew its lysosomes","It is consumed during opsonisation","It converts into a macrophage"],correct:1,
       explain:"The neutrophil cannot renew its lysosomes. The monocyte can replace its lysosomal contents, which is exactly why it is the cell of the sustained chronic phase."},
      {q:"Which mediator raises capillary permeability AND causes pain?",
       choices:["Histamine","Serotonin","Bradykinin","Complement C3b"],correct:2,
       explain:"All three of histamine, serotonin and bradykinin raise permeability. Pain is listed only for bradykinin, which also may increase leukocyte chemotaxis."},
      {q:"An implanted device provokes inflammation despite being sterile. Why?",
       choices:["Residual endotoxin from sterilisation","It is coated with immunoglobulin G and C3b, which immune cells recognise","It obstructs lymphatic drainage","Sterilisation is never complete"],correct:1,
       explain:"Biomaterials become coated with the opsonins immunoglobulin G and C3b. Immune cells recognise that coating and attach — the response is to the opsonised surface, not to infection."},
      {q:"Which pattern of inflammation ADDS a layer over the mucosa rather than removing one?",
       choices:["Ulcerative","Pseudomembranous","Catarrhal","Serous"],correct:1,
       explain:"Pseudomembranous inflammation forms a superficial necrotic layer of fibrin, inflammatory cells and debris over the mucosa. Ulcerative is the opposite — necrosis and sloughing that exposes the connective tissue beneath."}
    ],'''

donor = open(DONOR, encoding="utf-8").read()
head = donor[:donor.index('<div class="layout wrap"')]
tail = donor[donor.index("</main>") + len("</main>"):]
ty_start = tail.index("var TEST_YOURSELF = {")
ty_end = tail.index("\n  };", ty_start)
tail = tail[:ty_start] + TEST_YOURSELF.lstrip() + tail[ty_end:]

for old, new in (("#8a3f5c", "#3b2a5e"), ("#b8842f", "#c08a2e"), ("#5c4a7d", "#6a4fa3"),
                 ("#5e2a41", "#241a3d"), ("#ac5c78", "#8f74c9"),
                 ("#231d22", "#221c2b"), ("#e0a8bd", "#c4b0e8")):
    head = head.replace(old, new)
head = re.sub(r"<title>.*?</title>",
              "<title>Clinical Pathophysiology I &middot; Exam 1 &mdash; Study Guide</title>",
              head, count=1, flags=re.S)
head = re.sub(r"<header class=\"top\">.*?</header>",
  '<header class="top">\n'
  '  <h1>Clinical Pathophysiology I &middot; Exam 1 &mdash; Study Guide</h1>\n'
  '  <p>PAJ 5101 Clinical Pathophysiology I &middot; Class of 2028</p>\n'
  '  <p>Covers Lecture 1, Inflammation &middot; further sections are added as each Exam 1 lecture is '
  'posted &middot; Instructional Objectives (IOs) taken verbatim from the syllabus &middot; mechanism '
  'throughout, not management</p>\n'
  '</header>', head, count=1, flags=re.S)

html = head + '<div class="layout wrap" data-readable>' + "\n" + TOC + "\n\n" + BODY + tail
open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB)" % (os.path.basename(OUT), len(html) // 1024))
print("audio dir attr:", "data-audio-dir" in html, "| donor palette left:",
      [c for c in ("#8a3f5c", "#b8842f", "#5c4a7d") if c in html])
