#!/usr/bin/env python3
"""Build the Physical Diagnosis 2, Exam 1 study guide.

Same skeleton-lift as build_cp_guide.py: head/CSS/scripts come from the PD1
Exam 3 guide, which carries the site's guide design system, and the TOC, body
and TEST_YOURSELF are spliced in. Retheme is the olive identity already
established for this exam by its quizzes.

Two sections, one per lecture delivered so far. Exam 1 covers Lectures 1-4
(the calendar says so: "PD II - EXAM #1 (1-4)", 2026-09-30), so Ophthalmology
and ENT sections get added when those decks are posted on 8/26 and 9/3.

Instructional Objectives are VERBATIM from the PD2 syllabus and each is
answered in order. Lecture 1's objectives (a), (e), (f) and (g) concern the
history and physical and the SOAP note, which the Lecture 1 deck does not
teach -- it assumes PD I. Those are answered here from the PD I material
rather than skipped, with a pointer to the PD I guide that covers them at
length.
"""
import os, re

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
DONOR = os.path.join(ROOT, "Physical Diagnosis 1 Exam 3/pd1-exam3-study-guide.html")
OUT = os.path.join(ROOT, "Physical Diagnosis 2 Exam 1/pd2-exam-1-study-guide.html")

TOC = '''<nav class="toc">
  <h2>Contents</h2>
  <a class="top-link" href="#clinical-reasoning">1 &middot; Clinical Reasoning, Documentation &amp; the Encounter</a>
  <a href="#cr-format">1.1 Objective a &mdash; Format &amp; components of the comprehensive history and physical</a>
  <a href="#cr-groups">1.2 Objectives b &amp; d &mdash; Small groups, simulation &amp; the OSCE</a>
  <a href="#cr-oral">1.3 Objective c &mdash; The oral case presentation</a>
  <a href="#cr-focused">1.4 Objective e &mdash; Comprehensive versus focused</a>
  <a href="#cr-soap">1.5 Objective f &mdash; History and physical versus SOAP</a>
  <a href="#cr-documentation">1.6 Objective g &mdash; Documenting the complete history and physical</a>
  <a href="#cr-communication">1.7 Objective h &mdash; Involving the patient</a>
  <a class="top-link" href="#dermatology">2 &middot; Dermatological History &amp; Examination</a>
  <a href="#derm-structure">2.1 Objective a &mdash; Structure &amp; function of the skin</a>
  <a href="#derm-vocabulary">2.2 Objective b &mdash; The descriptive vocabulary</a>
  <a href="#derm-primary">2.3 Objective b &mdash; Primary morphology</a>
  <a href="#derm-secondary">2.4 Objective b &mdash; Secondary morphology</a>
  <a href="#derm-history">2.5 Objective c &mdash; The dermatological history</a>
  <a href="#derm-abnormal">2.6 Objective d &mdash; Abnormal findings: skin</a>
  <a href="#derm-hairnails">2.7 Objective d &mdash; Abnormal findings: hair &amp; nails</a>
  <a href="#derm-technique">2.8 Objective e &mdash; Performing the examination</a>
</nav>'''

BODY = '''<main>

<section class="deck" id="clinical-reasoning">
  <h2 class="deck-title">1 &middot; Clinical Reasoning, Documentation &amp; the Encounter</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Topic Outline: Application of Clinical Reasoning and Problem-Solving Abilities and Effective Exchange of Information</p>
    <ol type="a">
      <li>Describe the format and components of a comprehensive patient history and physical examination to enhance clinical reasoning.</li>
      <li>Describe the role of small groups and simulations in fostering clinical reasoning and problem-solving skills.</li>
      <li>Discuss the application of clinical reasoning in crafting oral presentations that accurately reflect patient care scenarios.</li>
      <li>Discuss the importance of clinical reasoning during an Objective Structured Clinical Examination (OSCE).</li>
      <li>Differentiate between a comprehensive and focused patient history and physical examination.</li>
      <li>Differentiate between the documentation of a complete history and physical examination and a problem-focused subjective-objective assessment and plan (SOAP).</li>
      <li>Demonstrate documentation of a complete history and physical examination.</li>
      <li>Explain the importance in involving the patient in healthcare communication.</li>
    </ol>
  </div>
  <div class="callout"><strong>Where this material actually lives.</strong> Objectives (a), (e), (f)
  and (g) are documentation objectives, and the Lecture 1 deck does not teach them &mdash; it assumes
  you carry them forward from Physical Diagnosis I, and says so directly: <em>review the
  documentation content from PD I</em>. They are answered below, and the
  <a href="../Physical%20Diagnosis%201%20Exam%203/pd1-exam3-study-guide.html#hp-documentation">PD I
  Exam 3 guide</a> covers the same ground section by section if you want the long version.</div>

  <h3 class="sub" id="cr-format">1.1 &middot; Objective a &mdash; Format and components of the comprehensive history and physical</h3>
  <p>A comprehensive history and physical is the full record of an encounter, taken in a fixed order
  so that nothing is lost and so that anyone reading it later finds each piece where they expect it.
  The components, in the order they are gathered and written:</p>
  <table>
    <tr><th>Component</th><th>What it holds</th></tr>
    <tr><td>Chief complaint</td><td>Why the patient came, in their own words where possible</td></tr>
    <tr><td>History of present illness</td><td>The narrative of the current problem, built from the seven attributes of a symptom</td></tr>
    <tr><td>Past medical history</td><td>Previous illnesses, hospitalisations, surgery</td></tr>
    <tr><td>Medications and allergies</td><td>Prescription and over-the-counter, with the reaction for each allergy</td></tr>
    <tr><td>Family history</td><td>Heritable disease in first-degree relatives</td></tr>
    <tr><td>Social history</td><td>Habits, occupation, exposures, living situation</td></tr>
    <tr><td>Review of systems</td><td>System-by-system screening for symptoms not yet volunteered</td></tr>
    <tr><td>Physical examination</td><td>What you found, described rather than labelled</td></tr>
    <tr><td>Assessment and plan</td><td>Differential, working diagnosis, testing, treatment, education, follow-up</td></tr>
  </table>
  <div class="pearl">The reason the order is fixed is the reason it enhances clinical reasoning: the
  history narrows the differential before you touch the patient, and the examination is then aimed
  at what the history raised. A history taken out of order tends to produce an examination that
  wanders.</div>

  <h3 class="sub" id="cr-groups">1.2 &middot; Objectives b &amp; d &mdash; Small groups, simulation and the Objective Structured Clinical Examination</h3>
  <p>These three formats all exist to make you <em>reason out loud</em>, which is the one thing
  reading cannot teach.</p>
  <table>
    <tr><th>Format</th><th>What it trains</th></tr>
    <tr><td>Small groups</td><td>Justifying every information request. You must explain why a piece of information is needed and what it would tell you about the patient &mdash; the facilitator withholds it until you do. That constraint is deliberate, and it is the whole exercise: it converts &ldquo;order a complete blood count&rdquo; into a hypothesis with a reason attached.</td></tr>
    <tr><td>Simulation</td><td>Reasoning against a moving target. Vitals are monitored live, laboratory and imaging results arrive during the scenario, and the plan has to change as the mannequin changes. A debriefing with reflection and feedback closes each session.</td></tr>
    <tr><td>Objective Structured Clinical Examination</td><td>The whole chain end to end and under time: focused history, focused examination, differentials, studies, diagnosis, treatment plan with patient education, and a one-minute case presentation.</td></tr>
  </table>
  <div class="pearl">The common thread is that none of them rewards recall alone. The small group
  will not hand you data without a justification, the simulation changes underneath you, and the
  Objective Structured Clinical Examination asks for a plan rather than a list of findings.</div>

  <h3 class="sub" id="cr-oral">1.3 &middot; Objective c &mdash; The oral case presentation</h3>
  <p>A presentation is <strong>a well-organised vignette that describes the patient and the clinical
  problem</strong> &mdash; not the written note read aloud. The provider's goal is to help the
  listeners visualise the patient and understand the problem.</p>
  <table>
    <tr><th>Element</th><th>Rule</th></tr>
    <tr><td>Opening statement</td><td>Include the past medical history and the chief complaint</td></tr>
    <tr><td>Content</td><td>Pertinent positives and negatives, from both the history and the physical examination</td></tr>
    <tr><td>Order</td><td>Mostly the order in which you obtained the history and performed the examination</td></tr>
    <tr><td>Delivery</td><td>Try not to read your notes</td></tr>
  </table>
  <div class="pearl"><strong>The test of a good presentation:</strong> it leads your facilitator to
  the same differential you formulated. That is a functional test, not a stylistic one &mdash; and it
  is where the clinical reasoning shows. Selecting what counts as <em>pertinent</em> is the reasoning
  being assessed. A presentation that includes everything has made no decisions.</div>

  <h3 class="sub" id="cr-focused">1.4 &middot; Objective e &mdash; Comprehensive versus focused</h3>
  <p>The distinction that matters, and the one most often got wrong: a focused encounter narrows
  <strong>both</strong> the history and the examination. It is not a comprehensive encounter written
  up more briefly, and it is not a full history with a short examination.</p>
  <table>
    <tr><th></th><th>Comprehensive</th><th>Focused</th></tr>
    <tr><td>History of present illness</td><td>Full</td><td>Focused</td></tr>
    <tr><td>Review of systems</td><td>Complete, system by system</td><td>Focused</td></tr>
    <tr><td>Past medical history</td><td>Full</td><td>Focused</td></tr>
    <tr><td>Social history</td><td>Full</td><td>Focused</td></tr>
    <tr><td>Family history, medications, allergies</td><td>Full</td><td>Focused</td></tr>
    <tr><td>Physical examination</td><td>Head to toe</td><td>Systems pertinent to the complaint</td></tr>
  </table>
  <p>A focused encounter still has to produce the whole reasoning chain: <strong>differentials,
  laboratory and imaging studies, a diagnosis, and a treatment plan including patient
  education</strong>. Narrowing the data gathered does not narrow what you are expected to conclude
  from it.</p>
  <div class="pearl">How far does a focused examination reach? Examine the systems pertinent to the
  chief complaint and the positive history, and when in doubt go one system up and one system down.
  Two questions settle the rest: what must be examined to rule out the worst-case scenario, and what
  are your differentials and how do you rule each in or out?</div>

  <h3 class="sub" id="cr-soap">1.5 &middot; Objective f &mdash; The complete history and physical versus the SOAP note</h3>
  <p>Both document an encounter. They differ in scope and in purpose.</p>
  <table>
    <tr><th></th><th>Complete history and physical</th><th>SOAP note</th></tr>
    <tr><td>Scope</td><td>Comprehensive &mdash; the entire history and a head-to-toe examination</td><td>Problem-focused</td></tr>
    <tr><td>When used</td><td>New patient, admission, annual comprehensive visit</td><td>A visit addressing a defined problem, and follow-up</td></tr>
    <tr><td>Structure</td><td>Chief complaint, history of present illness, past medical history, medications, allergies, family history, social history, review of systems, examination, assessment, plan</td><td>Subjective, Objective, Assessment, Plan</td></tr>
    <tr><td>Examination</td><td>All systems</td><td>Focused, but always with a general assessment or impression</td></tr>
  </table>
  <table>
    <tr><th>SOAP section</th><th>Shorthand</th><th>What goes in it</th></tr>
    <tr><td>Subjective</td><td>What the patient said</td><td>Narrative history, pertinent positives and negatives, medical and surgical history, family and social history, review of systems, medications, allergies</td></tr>
    <tr><td>Objective</td><td>What you found</td><td>Observations, measurements and tests performed during the encounter; the focused examination; always a general assessment or impression</td></tr>
    <tr><td>Assessment</td><td>What you concluded</td><td>The diagnosis drawn from history, examination and testing, plus chronic and concurrent conditions</td></tr>
    <tr><td>Plan</td><td>What you will do</td><td>Disposition, testing, treatment, referrals, patient education, follow-up</td></tr>
  </table>

  <h3 class="sub" id="cr-documentation">1.6 &middot; Objective g &mdash; Documenting the complete history and physical</h3>
  <p>The rules that get marked against you, taken from the clinical assignment guidance:</p>
  <table>
    <tr><th>Rule</th><th>Why it exists</th></tr>
    <tr><td><strong>Describe findings</strong> rather than writing <em>normal</em>, <em>abnormal</em> or <em>unremarkable</em></td><td>A description communicates what you actually observed; a label communicates only that you formed an opinion</td></tr>
    <tr><td><strong>No abbreviations</strong></td><td>Stated without qualification &mdash; there is no &ldquo;once defined on first use&rdquo; allowance</td></tr>
    <tr><td>Keep <strong>subjective and objective information in their own sections</strong></td><td>Blending them is one of the commonest documentation errors, and it hides which claims are the patient's and which are yours</td></tr>
    <tr><td>If you did not do something, <strong>document why</strong></td><td>You may not invent a finding. This is the one rule treated as absolute</td></tr>
    <tr><td>You may not write your note <strong>with another student</strong></td><td>Even when you saw the same patient, the note is your own work</td></tr>
    <tr><td>Review the <strong>grading rubric</strong> and the <strong>comments on prior assignments</strong> before submitting</td><td>Prior feedback is the most direct guide to what still needs fixing</td></tr>
  </table>
  <div class="callout"><strong>You can plagiarise yourself.</strong> Per the Student Handbook, work
  submitted for academic credit must be the original work of the student, and <em>work is not
  original when it has been submitted previously by the author or by anyone else</em>. Reusing your
  own template from an earlier assignment is the trap being flagged.</div>

  <h3 class="sub" id="cr-communication">1.7 &middot; Objective h &mdash; Involving the patient in healthcare communication</h3>
  <p>Communication is a skill that is graded, and it is expected to <strong>adapt in style and
  content for each patient</strong> rather than follow one fixed script.</p>
  <div class="pearl"><strong>The rule stated most emphatically:</strong> when someone other than the
  patient is supplying the answers, you should <em>always</em> be looking at and interacting with the
  patient, not with whoever is speaking. The encounter is with the patient even when the words come
  from elsewhere. In the Objective Structured Clinical Examination the &ldquo;patient&rdquo; gives no
  verbal responses beyond identifying data and the facilitator answers for them &mdash; which is
  precisely the situation this rule is built for.</div>
  <p>A related expectation: <strong>accept constructive feedback and modify behaviour</strong>, and
  expect different facilitators to give different feedback. The variation is anticipated rather than
  a contradiction to be resolved.</p>
  <button type="button" class="test-yourself-btn" style="--acc:#4a5c24" onclick="window.openTestYourself('Test yourself — Clinical Reasoning &amp; Documentation', TEST_YOURSELF.clinicalreasoning)">Test yourself! &rarr;</button>
  <p class="guide-foot">Source: <em>Intro to PD II - Elwaya .pdf</em> (Professor Ayelet Elwaya), Pages 1&ndash;23,
  and the PAJ 5310 syllabus instructional objectives. Documentation content carried forward from
  Physical Diagnosis I.</p>
</section>

<section class="deck" id="dermatology">
  <h2 class="deck-title">2 &middot; Dermatological History &amp; Examination</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Topic Outline: Advanced Dermatological System Medical History and Examination</p>
    <ol type="a">
      <li>Review the anatomical structure and function of the skin.</li>
      <li>Review the terms used to describe lesion type (primary morphology), lesion configuration (secondary morphology), texture, distribution, and color of skin lesions.</li>
      <li>Describe the elements related to interviewing and eliciting a medical history that aid in identifying skin, hair, and nail disorders.</li>
      <li>Describe physical examination findings of abnormal conditions related to skin, hair, and nails.</li>
      <li>Demonstrate the proper clinical skills for a complete and focused physical examination of the skin.</li>
    </ol>
  </div>
  <div class="callout"><strong>Scope note.</strong> This is the <em>examination</em> lecture: how to
  take the history, how to perform the examination, and what to call what you see. Dermatology also
  appears in Clinical Pathophysiology I this term (mechanism) and in Clinical Medicine and Surgery I
  (diagnosis and management). The three do not conflict &mdash; they are three different questions
  about the same diseases.</div>

  <h3 class="sub" id="derm-structure">2.1 &middot; Objective a &mdash; Structure and function of the skin</h3>
  <p><strong>Five functions:</strong> protection of internal structures &middot; prevention of entry
  of microorganisms &middot; temperature regulation &middot; excretion &middot; production of
  vitamin D.</p>
  <table>
    <tr><th>Gland</th><th>Secretes</th><th>Notes</th></tr>
    <tr><td>Sudoriferous (eccrine)</td><td>Sweat</td><td>Maintains body temperature</td></tr>
    <tr><td>Apocrine</td><td>Pheromones</td><td><strong>Becomes active during puberty</strong></td></tr>
    <tr><td>Sebaceous</td><td>Sebum</td><td>Surrounds the hair follicle; keeps hair and skin moist</td></tr>
  </table>
  <table>
    <tr><th>Hair type</th><th>Character</th><th>Where</th></tr>
    <tr><td>Vellus</td><td>Short, fine</td><td>Covers the body</td></tr>
    <tr><td>Terminal</td><td>Coarse</td><td>Scalp, pubic, axillary, beard</td></tr>
  </table>

  <h3 class="sub" id="derm-vocabulary">2.2 &middot; Objective b &mdash; The descriptive vocabulary</h3>
  <p>Five features describe any lesion: <strong>distribution</strong> (location) &middot;
  <strong>configuration</strong> (shape) &middot; <strong>morphology</strong> (form and structure)
  &middot; <strong>colour</strong> &middot; <strong>texture</strong>.</p>
  <p><strong>Distribution</strong> &mdash; unilateral, bilateral, symmetric, asymmetric,
  photodistribution, intertriginous, flexural, extensor, palmar-plantar, hair-bearing areas.
  Distribution is often the fastest route to a diagnosis:</p>
  <table>
    <tr><th>Distribution</th><th>Suggests</th></tr>
    <tr><td>Generalised or diffuse</td><td>Allergic reactions</td></tr>
    <tr><td>Regional (confined to one body area)</td><td>Tinea capitis</td></tr>
    <tr><td>Sun-exposed (photodistribution)</td><td>Skin cancers</td></tr>
    <tr><td>Dermatome</td><td>Herpes zoster</td></tr>
    <tr><td>Extensor</td><td>Psoriasis</td></tr>
    <tr><td>Flexor</td><td>Intertrigo</td></tr>
    <tr><td>Intertriginous (creases and folds)</td><td>Involvement of skin folds</td></tr>
  </table>
  <p><strong>Configuration</strong> &mdash; the shape the lesions make together:</p>
  <table>
    <tr><th>Term</th><th>Meaning</th></tr>
    <tr><td>Annular</td><td>Shaped like a ring; round</td></tr>
    <tr><td>Arciform</td><td>Forms arcs or curves</td></tr>
    <tr><td>Confluent</td><td>Lesions run together</td></tr>
    <tr><td>Discrete</td><td>Lesions remain separate</td></tr>
    <tr><td>Grouped</td><td>A cluster of lesions</td></tr>
    <tr><td>Gyrate</td><td>Twisted, coiled, spiral, snakelike</td></tr>
    <tr><td>Herpetiform</td><td>Grouped papules or vesicles arranged as in herpes simplex</td></tr>
    <tr><td>Iris (target)</td><td>Shaped like a bull's eye</td></tr>
    <tr><td>Linear</td><td>Forms a line or stripe</td></tr>
    <tr><td>Reticular</td><td>Lacy or networked pattern</td></tr>
    <tr><td>Serpiginous</td><td>Snake-like</td></tr>
    <tr><td>Zosteriform</td><td>Clustered in a dermatomal distribution, as in herpes zoster</td></tr>
  </table>
  <div class="pearl"><strong>The pair most often confused:</strong> <em>herpetiform</em> is grouping
  like herpes <em>simplex</em>; <em>zosteriform</em> is a dermatomal band like herpes
  <em>zoster</em>. Both are named for an infection, which is what makes them easy to swap.</div>

  <h3 class="sub" id="derm-primary">2.3 &middot; Objective b &mdash; Primary morphology</h3>
  <p>A <strong>primary lesion</strong> forms first and results directly from the disease. Identifying
  it is the key to interpretation and description &mdash; every later description depends on getting
  this right.</p>
  <div class="pearl"><strong>One centimetre is the hinge.</strong> Four of the definitions below turn
  on it, in matched pairs: flat under and over (macule / patch), solid elevated under and over
  (papule / plaque), fluid-filled under and over (vesicle / bulla). Learn the three pairs and you
  have six of the terms. Bring a ruler &mdash; that is why one is on the equipment list.</div>
  <table>
    <tr><th>Lesion</th><th>Definition</th><th>Size</th><th>Example</th></tr>
    <tr><td><strong>Macule</strong></td><td>Circumscribed, flat discoloration &mdash; brown, blue, red or hypopigmented</td><td>&lt; 1 cm</td><td>Freckles</td></tr>
    <tr><td><strong>Patch</strong></td><td>Circumscribed, flat discoloration; a large macule, or macules that coalesce</td><td>&gt; 1 cm</td><td>Vitiligo, caf&eacute; au lait spots</td></tr>
    <tr><td><strong>Papule</strong></td><td>Palpable, elevated solid mass</td><td>&lt; 1 cm</td><td>Nevi, warts, lichen planus</td></tr>
    <tr><td><strong>Plaque</strong></td><td>Palpable, elevated solid mass, plateau-like; elevated, flat-topped, firm, rough; occupies a large area compared with its elevation; may be coalesced papules</td><td>&gt; 1 cm</td><td>Psoriasis</td></tr>
    <tr><td><strong>Nodule</strong></td><td>Elevated, firm, circumscribed; round or ellipsoid; <strong>deeper in the dermis than a papule</strong></td><td>1&ndash;2 cm <span class="tag">(Bates says larger than 0.5 cm)</span></td><td>Basal cell carcinoma, neurofibromatosis</td></tr>
    <tr><td><strong>Tumor</strong></td><td>Palpable, elevated solid mass</td><td>&gt; 2 cm</td><td>Neoplasms</td></tr>
    <tr><td><strong>Wheal</strong></td><td>Elevated irregular-shaped area of cutaneous edema; solid, <strong>transient</strong></td><td>Variable</td><td>Allergic reaction</td></tr>
    <tr><td><strong>Vesicle</strong></td><td>Superficial elevation filled with fluid</td><td>&lt; 1 cm</td><td>Blister, herpes simplex</td></tr>
    <tr><td><strong>Bulla</strong></td><td>Superficial elevation filled with fluid</td><td>&gt; 1 cm</td><td>Large blister</td></tr>
    <tr><td><strong>Pustule</strong></td><td>Superficial elevation filled with <strong>purulent</strong> material</td><td>Usually &lt; 1 cm</td><td>Acne, impetigo</td></tr>
    <tr><td><strong>Cyst</strong></td><td>Elevated, circumscribed, <strong>encapsulated</strong>; in the dermis or subcutaneous layer; liquid or semisolid contents</td><td>&mdash;</td><td>Sebaceous cyst</td></tr>
  </table>
  <div class="pearl">Two lesions are defined by something other than size. A <strong>wheal</strong> is
  the only transient one &mdash; if it is gone by the next visit, that is the finding, not a missed
  examination. A <strong>cyst</strong> is the only encapsulated one, which is what separates it from
  a nodule you can feel at the same depth.</div>

  <h3 class="sub" id="derm-secondary">2.4 &middot; Objective b &mdash; Secondary morphology</h3>
  <p>A <strong>secondary lesion</strong> is a change in a primary lesion over time &mdash; from
  disease progression, from treatment, or from <strong>manipulation</strong> such as picking or
  scratching. That third cause is worth holding on to: the patient's own hands change the
  examination.</p>
  <table>
    <tr><th>Lesion</th><th>Definition</th><th>Example</th></tr>
    <tr><td><strong>Crust</strong></td><td>Collection of cellular debris, dried serum and blood &mdash; a scab. The antecedent primary lesion is usually a vesicle, bulla or pustule</td><td>&mdash;</td></tr>
    <tr><td><strong>Erosion</strong></td><td>Loss of superficial epidermis, <strong>does not involve dermis</strong>; surface is moist but <strong>does not bleed</strong></td><td>The moist area after a bulla or vesicle ruptures</td></tr>
    <tr><td><strong>Ulcer</strong></td><td>Deeper loss of epidermis and/or dermis; <strong>may bleed and scar</strong></td><td>Stasis ulcer of venous insufficiency</td></tr>
    <tr><td><strong>Fissure</strong></td><td>Linear crack in skin</td><td>Athlete's foot</td></tr>
    <tr><td><strong>Scale</strong></td><td>Thin flake of exfoliated epidermis</td><td>Dandruff, cradle cap</td></tr>
    <tr><td><strong>Excoriation</strong></td><td>An abrasion or scratch mark; may be linear or rounded</td><td>Scratched insect bite</td></tr>
    <tr><td><strong>Scar (cicatrix)</strong></td><td>Replacement of destroyed tissue by fibrous tissue. Thick and pink (<strong>hypertrophic</strong>) or thin and white (<strong>atrophic</strong>); <strong>does not extend beyond the injured area</strong></td><td>&mdash;</td></tr>
    <tr><td><strong>Keloid</strong></td><td>Scar that <strong>grows beyond the wound</strong></td><td>&mdash;</td></tr>
    <tr><td><strong>Lichenification</strong></td><td>Thickening with <strong>skin line accentuation</strong>; roughening and thickening of epidermis; caused by chronic irritation</td><td>Atopic dermatitis</td></tr>
    <tr><td><strong>Collarette scale</strong></td><td>Fine scale, <strong>peripherally attached and centrally detached</strong>, on the edge of an inflammatory lesion</td><td>Pityriasis rosea</td></tr>
  </table>
  <div class="pearl"><strong>Erosion versus ulcer</strong> is the discrimination worth being certain
  about: an erosion stops at the epidermis, is moist, and does not bleed or scar; an ulcer reaches
  the dermis, may bleed, and may scar. Depth determines all three consequences at once.</div>
  <table>
    <tr><th>Also worth knowing</th><th>Detail</th></tr>
    <tr><td>Verrucae (warts)</td><td>Caused by <strong>human papillomavirus</strong>. Small harmless tumors of the skin; grey to flesh coloured nodules raised from the surface, sometimes with rough hornlike projections</td></tr>
    <tr><td>Corn</td><td>Smaller than a callus; usually over a <strong>non-weight-bearing</strong> area of the foot; conical structure of keratin pointing toward the dermis</td></tr>
    <tr><td>Callus</td><td>Thickening of epidermal keratin; usually on the sole of the foot, at the ball or heel</td></tr>
  </table>

  <h3 class="sub" id="derm-history">2.5 &middot; Objective c &mdash; The dermatological history</h3>
  <p><strong>The five core questions:</strong> where did the problem first appear &middot; what did it
  look like &middot; how has it progressed or changed &middot; any associated symptoms &middot; what
  treatment has been tried.</p>
  <div class="pearl"><strong>Think bugs, drugs, contact.</strong> Three exposure categories, and the
  fastest way to remember what else to ask: <em>bugs</em> &mdash; family members or contacts with the
  same, travel; <em>drugs</em> &mdash; systemic medications, both over-the-counter and prescription;
  <em>contact</em> &mdash; allergens and irritants from hobbies, occupation and environment.</div>
  <table>
    <tr><th>Area</th><th>What to ask</th></tr>
    <tr><td>Existing skin abnormalities</td><td>Changes in colour &middot; changes in shape (border, elevation, diameter) &middot; changes in size &middot; pain &middot; bleeds easily &middot; non-healing areas</td></tr>
    <tr><td>Onset</td><td>Duration; acute versus chronic</td></tr>
    <tr><td>Relationships</td><td>Season, travel history, heat or cold, previous reactions, drugs, menses</td></tr>
    <tr><td>Skin symptoms</td><td>Pruritus, pain, paresthesia</td></tr>
    <tr><td>Past medical history</td><td>Previous problems; systemic disease; personal dermatology history including disease and surgery</td></tr>
    <tr><td>Family history</td><td>Skin cancer, psoriasis, allergies, infestations, infections</td></tr>
    <tr><td>Psychosocial</td><td>Personal habits, exposures. Psychological stress is <strong>seldom the sole cause</strong> but <strong>can exacerbate many dermatoses</strong></td></tr>
  </table>
  <div class="callout"><strong>Pruritus is not a diagnosis.</strong> It is the sensation that causes
  the desire to scratch. Generalised itching with no obvious reason has a wide differential &mdash;
  dry skin, ageing, pregnancy, uremia, jaundice, lymphomas, leukemias, drug reaction and lice. Other
  sensations to ask about: burning, pain or tenderness, tingling, a creeping or crawling feeling, and
  whether it is intermittent or continuous.</div>
  <div class="pearl">Patients with cognitive problems may not attend to hygiene. If the hygiene of
  the skin, hair or nails appears inadequate, <strong>that is a finding</strong> &mdash; assess the
  social history, cognition, and ability to perform activities of daily living.</div>

  <h3 class="sub" id="derm-abnormal">2.6 &middot; Objective d &mdash; Abnormal findings: the skin</h3>
  <p><strong>Vascular lesions.</strong> The single manoeuvre that sorts them is
  <strong>diascopy</strong>: press a piece of clear glass or plastic against the skin and look at the
  lesion under pressure. <strong>If the colour fades, there is vascular engorgement; if it does not
  fade, it is hemorrhage in the skin.</strong></p>
  <table>
    <tr><th>Lesion</th><th>Appearance</th><th>Size</th><th>Blanches?</th></tr>
    <tr><td>Petechiae</td><td>Reddish-purple macules</td><td>&lt; 3 mm</td><td>No</td></tr>
    <tr><td>Purpura</td><td>Reddish-purple macules</td><td>3 mm &ndash; 1 cm</td><td>No</td></tr>
    <tr><td>Ecchymosis</td><td>Purple or purplish-blue macules, fade over time</td><td>&gt; 1 cm</td><td>No</td></tr>
    <tr><td>Cherry angioma (Campbell De Morgan spots)</td><td>Dome shaped, bright red to violet or black</td><td>&mdash;</td><td>Sometimes</td></tr>
    <tr><td>Telangiectasia</td><td>Fine, irregular blood vessels</td><td>&mdash;</td><td>Yes</td></tr>
    <tr><td>Spider angioma</td><td>Central red macule with radiating spider-like arms</td><td>&mdash;</td><td>Yes</td></tr>
  </table>
  <div class="pearl">Petechiae, purpura and ecchymosis are the same finding at three sizes, and none
  of them blanches &mdash; because the blood is outside the vessels. Under 3 mm, 3 mm to 1 cm, over
  1 cm.</div>
  <p><strong>Dermatographism</strong> &mdash; &ldquo;writing on skin&rdquo;, an urticarial type
  allergic reaction. Firm stroking produces the <strong>triple response of Lewis</strong>:</p>
  <table>
    <tr><th>Step</th><th>What appears</th><th>Mechanism</th></tr>
    <tr><td>1</td><td>Initial red line</td><td>Capillary dilatation</td></tr>
    <tr><td>2</td><td>Reflex flare with broadening erythema</td><td>Arteriolar dilatation</td></tr>
    <tr><td>3</td><td>Formation of a linear wheal</td><td>Transudation of fluid, that is, edema</td></tr>
  </table>
  <p><strong>Decubitus (pressure) ulcers.</strong> Staged by depth:</p>
  <table>
    <tr><th>Stage</th><th>Finding</th></tr>
    <tr><td>I</td><td>Alteration of <strong>intact</strong> skin: erythema that fails to blanch with pressure, plus change in temperature (warmth or coolness), consistency (firm or boggy), sensation (pain or itching), and colour</td></tr>
    <tr><td>II</td><td><strong>Partial</strong> thickness skin loss involving epidermis, dermis or both</td></tr>
    <tr><td>III</td><td><strong>Full</strong> thickness skin loss; necrosis of subcutaneous tissue; may extend to but <strong>not through</strong> underlying muscle</td></tr>
    <tr><td>IV</td><td>Full thickness skin loss; destruction of tissue, muscle and/or bone</td></tr>
  </table>
  <div class="pearl">The stage I / stage II line is whether the skin is broken; the stage III /
  stage IV line is whether muscle and bone are destroyed. &ldquo;Reaches muscle but does not go
  through it&rdquo; is still stage III.</div>
  <p><strong>Tinea infections</strong>, named by site: corporis (body) &middot; pedis (foot) &middot;
  barbae (beard) &middot; cruris (groin) &middot; capitis (scalp) &middot; unguium (nails).</p>
  <table>
    <tr><th>Infection</th><th>Appearance</th></tr>
    <tr><td>Tinea pedis</td><td>Dry, scaling, or macerated fissuring of the interdigital spaces of the feet</td></tr>
    <tr><td>Tinea corporis</td><td>Scaling, sharply demarcated round plaques with <strong>central clearing</strong></td></tr>
    <tr><td>Tinea capitis</td><td>Round scaling patches of alopecia with <strong>hairs broken off close to the scalp</strong></td></tr>
  </table>
  <p><strong>Malignancies of the skin.</strong></p>
  <table>
    <tr><th>Malignancy</th><th>Common site</th><th>Appearance</th></tr>
    <tr><td>Basal cell carcinoma</td><td>Face</td><td>Translucent, <strong>pearly</strong> nodule with a depressed center and raised borders; may ulcerate. A <strong>non-healing ulcer</strong> is the other presentation</td></tr>
    <tr><td>Squamous cell carcinoma</td><td>Face and other sun-exposed areas</td><td>Red scaling, crusting nodule or plaque that can ulcerate and bleed</td></tr>
    <tr><td>Malignant melanoma</td><td>Changing nevi</td><td>Irregularly coloured plaque with <strong>sharp notches</strong> and variation of pigment</td></tr>
    <tr><td>Kaposi's sarcoma</td><td>Widely disseminated &mdash; legs, trunk, arms, neck, head</td><td>Starts as light coloured lesions that coalesce into darker ones; dark blue-purple macules, papules, nodules and plaques. <strong>The most frequent neoplasm in patients with acquired immunodeficiency syndrome</strong></td></tr>
  </table>
  <table>
    <tr><th>Letter</th><th>Melanoma warning sign</th></tr>
    <tr><td>A</td><td>Asymmetry or shape</td></tr>
    <tr><td>B</td><td>Border irregularity</td></tr>
    <tr><td>C</td><td>Colour variation</td></tr>
    <tr><td>D</td><td>Diameter larger than 6 mm</td></tr>
    <tr><td>E</td><td>Evolving, elevation</td></tr>
    <tr><td>F</td><td>Family history</td></tr>
    <tr><td>G</td><td>Growing</td></tr>
  </table>

  <h3 class="sub" id="derm-hairnails">2.7 &middot; Objective d &mdash; Abnormal findings: hair and nails</h3>
  <table>
    <tr><th>Hair disorder</th><th>Findings</th></tr>
    <tr><td>Alopecia</td><td>Diffuse, patchy or total hair loss. <strong>Note the distribution on inspection</strong> &mdash; that is what separates the causes</td></tr>
    <tr><td>Androgenic alopecia</td><td>Male pattern baldness</td></tr>
    <tr><td>Alopecia areata</td><td>Chronic inflammatory disease of hair follicles, associated with <strong>autoimmune disorders</strong>. Hair loss in multiple round patches, with <strong>&ldquo;exclamation point&rdquo; hairs</strong></td></tr>
    <tr><td>Trichotillomania</td><td>Caused by an urge to pull out hair, producing bald patches. Single or multiple; from a few square centimetres to the entire scalp</td></tr>
    <tr><td>Hirsutism</td><td>Increased hair growth in women, in a <strong>male pattern of distribution</strong></td></tr>
    <tr><td>Lice</td><td>Tiny white ovoid granules &mdash; nits &mdash; adherent to hairs. A magnifying glass aids inspection</td></tr>
  </table>
  <div class="pearl"><strong>Three causes of patchy hair loss, told apart by what is left behind:</strong>
  tinea capitis leaves <em>scaling</em> patches with hairs broken close to the scalp; alopecia areata
  leaves smooth patches with <em>exclamation point</em> hairs; trichotillomania leaves patches from
  pulling, with neither scale nor exclamation point hairs.</div>
  <p><strong>Nails.</strong> Inspect for shape, size, colour, brittleness, hemorrhages, lines and
  grooves, clubbing, and pitting.</p>
  <table>
    <tr><th>Finding</th><th>Description</th><th>Points toward</th></tr>
    <tr><td>Koilonychia</td><td>Spoon-shaped concave nails; the nail plate thins and becomes inverted</td><td>&mdash;</td></tr>
    <tr><td>Onycholysis</td><td><strong>Painless</strong> separation of nail plate from nail bed, starting <strong>distally</strong>; several or all nails usually affected</td><td>Local irritation (chemical exposure, prolonged immersion in water), fungal infection, psoriasis, medications such as tetracycline, trauma</td></tr>
    <tr><td>Nail pitting</td><td>Dystrophy of the nail plate; areas of small depressions or &ldquo;pits&rdquo;</td><td>&mdash;</td></tr>
    <tr><td>Terry's nails</td><td>Proximal portion white, distal portion dark</td><td>&mdash;</td></tr>
    <tr><td>Green nail</td><td>&mdash;</td><td><strong>Pseudomonas</strong> infection</td></tr>
    <tr><td>Brown&ndash;black nail</td><td>&mdash;</td><td><strong>Melanoma</strong></td></tr>
    <tr><td>Subungual hematoma</td><td>Hemorrhage to the nail plate</td><td>&mdash;</td></tr>
    <tr><td>Splinter hemorrhages</td><td>Hemorrhage of the <strong>distal capillary loop</strong></td><td>&mdash;</td></tr>
    <tr><td>Beau's lines</td><td>Transverse <strong>depressions</strong></td><td>Halfway up the nail suggests an illness about <strong>3 months ago</strong></td></tr>
    <tr><td>Mee's lines</td><td>Transverse <strong>lines</strong></td><td>&mdash;</td></tr>
    <tr><td>Clubbing</td><td>Angle between nail base and finger <strong>greater than 180&deg;</strong>; end of finger becomes rounded and bulbous</td><td>&mdash;</td></tr>
    <tr><td>Paronychia</td><td>Soft tissue infection around the nail, at the cuticle or nail fold. <strong>Acute:</strong> painful and purulent. Also occurs in chronic form</td><td>&mdash;</td></tr>
  </table>
  <div class="pearl">Beau's lines are a clock. The nail grows out at a roughly known rate, so a
  transverse depression halfway up dates the insult to about three months before the visit &mdash;
  which is the sort of finding that sends you back to the history with a specific date in mind.</div>

  <h3 class="sub" id="derm-technique">2.8 &middot; Objective e &mdash; Performing the examination</h3>
  <p>The four principles are <strong>inspection, palpation, percussion and auscultation</strong>.
  That order holds for <em>every</em> body system except the abdominal examination, and some systems
  do not use all four.</p>
  <table>
    <tr><th>Set-up</th><th>Detail</th></tr>
    <tr><td>Equipment</td><td>Ruler &middot; light source &middot; magnifying lens &middot; gloves for any open lesions</td></tr>
    <tr><td>Patient</td><td>In a gown &mdash; so that hair, anterior and posterior body surfaces, palms and soles, nails and interdigital spaces can all be inspected</td></tr>
    <tr><td>Light</td><td>Inspect the entire skin surface in good light, preferably <strong>natural</strong> light or artificial light that resembles it. <strong>Artificial light may distort skin tone</strong></td></tr>
  </table>
  <p>Six characteristics are assessed by inspection, palpation, or both:</p>
  <table>
    <tr><th>Characteristic</th><th>Descriptive terms</th></tr>
    <tr><td>Colour</td><td>Increase or decrease in pigmentation &middot; erythema/rubor &middot; pallor &middot; jaundice &middot; cyanosis</td></tr>
    <tr><td>Moisture</td><td>Dryness &middot; sweating &middot; oiliness</td></tr>
    <tr><td>Temperature</td><td>Warmth &middot; coolness &mdash; <strong>use the dorsal aspect of the hands</strong></td></tr>
    <tr><td>Texture</td><td>Roughness &middot; smoothness</td></tr>
    <tr><td>Mobility and turgor</td><td>See below</td></tr>
    <tr><td>Lesions</td><td>Distribution, configuration, morphology, colour, texture</td></tr>
  </table>
  <table>
    <tr><th></th><th>Normal</th><th>Abnormal</th></tr>
    <tr><td><strong>Mobility</strong></td><td>Skin lifts up with ease</td><td><strong>Edema</strong> &mdash; reduced skin mobility</td></tr>
    <tr><td><strong>Turgor</strong></td><td>Skin quickly resumes its shape</td><td><strong>Dehydration</strong> &mdash; skin remains elevated</td></tr>
  </table>
  <div class="pearl"><strong>Central versus peripheral cyanosis</strong> is a two-organ distinction.
  Central cyanosis is often due to inadequate oxygenation <em>in the lungs</em>; peripheral cyanosis
  is usually due to inadequate <em>circulation</em>. Same colour, different organ.</div>
  <p><strong>Hair and scalp.</strong> Inspect colour, distribution and quantity; palpate for texture.
  Separate the hair into sections to observe the scalp, and inspect <strong>behind the ears and the
  occiput</strong>. The scalp should be clean, with no lesions, discolorations, flaking or
  parasites.</p>
  <button type="button" class="test-yourself-btn" style="--acc:#4a5c24" onclick="window.openTestYourself('Test yourself — Dermatology', TEST_YOURSELF.dermatology)">Test yourself! &rarr;</button>
  <p class="guide-foot">Source: <em>PD II Derm - Beck.pptx</em> (Valerie Beck, DMSc, PA-C), Slides 1&ndash;103,
  and the PAJ 5310 syllabus instructional objectives. Course texts: Bickley, <em>Bates' Guide to
  Physical Examination and History Taking</em>; Wolff &amp; Johnson, <em>Fitzpatrick's Color Atlas
  &amp; Synopsis of Clinical Dermatology</em>.</p>
</section>

</main>'''

TEST_YOURSELF = '''  var TEST_YOURSELF = {
    clinicalreasoning: [
      {q:"What is the test of whether an oral case presentation was a good one?",
       choices:["It lasts under two minutes","It includes every element of the written note","It leads the listener to the same differential you formulated","It avoids all medical terminology"],correct:2,
       explain:"A functional test rather than a stylistic one. Choosing what counts as pertinent is the clinical reasoning being assessed — a presentation that includes everything has made no decisions."},
      {q:"In a FOCUSED encounter, what is narrowed?",
       choices:["Both the history and the physical examination","Only the physical examination","Only the history of present illness","Neither — only the write-up is shorter"],correct:0,
       explain:"History of present illness, review of systems, past medical history, social history, family history, medications and allergies are all focused, alongside the examination. A focused encounter is a targeted selection, not a shorter version of everything."},
      {q:"You are examining a patient whose answers are being supplied by someone else. Where should your attention be?",
       choices:["On whoever is supplying the answers","On the documentation form","Divided evenly between the two","On the patient"],correct:3,
       explain:"Stated emphatically: you should ALWAYS be looking at and interacting with your patient, not the person answering. The encounter is with the patient even when the words come from elsewhere."},
      {q:"Part of your examination was not performed. What must the note say?",
       choices:["Record the finding you would expect if it were normal","Document why it was not done","Leave the section blank","Copy the finding from a classmate who saw the same patient"],correct:1,
       explain:"You cannot make up history or physical examination findings. If you did not do something, document why — and a note may never be written with another student, even for the same patient."},
      {q:"How should physical examination findings be written?",
       choices:["Describe what you found","Write 'unremarkable' where nothing is wrong","Record only abnormal findings","Score each system on a standard scale"],correct:0,
       explain:"Describe findings instead of using normal, abnormal or unremarkable. A description says what you observed; a label says only that you formed an opinion."}
    ],
    dermatology: [
      {q:"A lesion is a circumscribed, FLAT discoloration measuring 2 cm. What is it?",
       choices:["A plaque","A patch","A macule","A papule"],correct:1,
       explain:"Flat and over 1 cm is a patch — a large macule, or macules that have coalesced. Vitiligo and café au lait spots are the examples. A plaque is elevated; a macule is the same flat lesion under 1 cm."},
      {q:"You press a glass slide against a purple lesion and the colour does NOT fade. What does this mean?",
       choices:["Vascular engorgement","Increased melanin pigmentation","Hemorrhage in the skin","An allergic reaction"],correct:2,
       explain:"Diascopy. Blood inside vessels can be pressed out, so engorgement blanches; blood outside the vessels cannot, so hemorrhage does not. This is why petechiae, purpura and ecchymosis all fail to blanch."},
      {q:"A bulla ruptures leaving a moist area that does not bleed. How is this described?",
       choices:["An ulcer","A fissure","An excoriation","An erosion"],correct:3,
       explain:"An erosion — loss of superficial epidermis that does not involve the dermis. Moist but not bleeding is the giveaway. An ulcer reaches the dermis, may bleed, and may scar."},
      {q:"A pressure ulcer shows full thickness skin loss with necrosis reaching but not penetrating muscle. What stage?",
       choices:["Stage III","Stage II","Stage IV","Stage I"],correct:0,
       explain:"Stage III: full thickness loss with necrosis of subcutaneous tissue, extending to but NOT through underlying muscle. Stage IV is destruction of tissue, muscle and bone."},
      {q:"A patient has round patches of hair loss with hairs that taper toward the scalp and no scaling. What is this?",
       choices:["Tinea capitis","Alopecia areata","Trichotillomania","Androgenic alopecia"],correct:1,
       explain:"Those are exclamation point hairs — alopecia areata, a chronic inflammatory disease of hair follicles associated with autoimmune disorders. Tinea capitis would scale and break hairs off close to the scalp."},
      {q:"Transverse DEPRESSIONS halfway up the fingernail suggest what?",
       choices:["Chronic hypoxia","Iron deficiency","Pseudomonas infection","An illness about three months ago"],correct:3,
       explain:"Beau's lines. The position on the nail dates the insult — halfway up corresponds to roughly three months before the visit."}
    ],'''

donor = open(DONOR, encoding="utf-8").read()
head = donor[:donor.index('<div class="layout wrap"')]
tail = donor[donor.index("</main>") + len("</main>"):]
ty_start = tail.index("var TEST_YOURSELF = {")
ty_end = tail.index("\n  };", ty_start)
tail = tail[:ty_start] + TEST_YOURSELF.lstrip() + tail[ty_end:]

# Olive retheme. Each replacement was picked to land within ~0.1 of the donor
# hex's own contrast ratio against white, so the design system's contrast
# relationships survive the recolour rather than being re-guessed.
for old, new in (("#8a3f5c", "#4a5c24"), ("#b8842f", "#b3872e"), ("#5c4a7d", "#485a22"),
                 ("#5e2a41", "#333f1a"), ("#ac5c78", "#697d33"),
                 ("#231d22", "#1c2014"), ("#e0a8bd", "#adc172")):
    head = head.replace(old, new)
head = re.sub(r"<title>.*?</title>",
              "<title>Physical Diagnosis 2 &middot; Exam 1 &mdash; Study Guide</title>",
              head, count=1, flags=re.S)
head = re.sub(r"<header class=\"top\">.*?</header>",
  '<header class="top">\n'
  '  <h1>Physical Diagnosis 2 &middot; Exam 1 &mdash; Study Guide</h1>\n'
  '  <p>PAJ 5310 Physical Diagnosis II &middot; Class of 2028</p>\n'
  '  <p>Covers Lectures 1 and 2 &middot; Ophthalmology and ENT sections are added as those decks are '
  'posted &middot; Instructional Objectives (IOs) taken verbatim from the syllabus</p>\n'
  '</header>', head, count=1, flags=re.S)

html = head + '<div class="layout wrap" data-readable>' + "\n" + TOC + "\n\n" + BODY + tail
open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB)" % (os.path.basename(OUT), len(html) // 1024))
print("audio dir attr:", "data-audio-dir" in html, "| donor palette left:",
      [c for c in ("#8a3f5c", "#b8842f", "#5c4a7d", "#5e2a41", "#ac5c78", "#e0a8bd") if c in html])
