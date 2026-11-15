#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Microbiology Exam 3 review guide from Professor Webster's own review.

On 13 November 2026, at the end of the Lecture 18 (DNA Viruses of Medical Importance) class, Professor Webster
reviewed Exam 3. The recording of that day is three Notability parts; the review is the tail of part 2 plus the
whole of part 3 (32:18). She walked the three lectures SHE taught, in order:

  * Lecture 14, Gram-Negative Bacilli -- organism by organism (part 3, 0:00-15:01);
  * Lecture 17, Parasites (her deck file says "Lecture 16") -- organism by organism (part 3, 15:04-28:52),
    with the instruction that a picture may have to be identified;
  * Lecture 18, DNA Viruses -- taught that afternoon, so a closing list of what to know (part 3, 29:00-32:12).

The rules are the Exam 1 and Exam 2 pattern (tools/build_micro_webster_review.py,
tools/build_micro_e2_webster_review.py):

  1. The tier on each heading is HER weighting. Know cold = she asked the class to answer it, drilled it, or said
     "need to know / should know / be able to". Know it = she walked it without singling it out, or it is on her
     list without a question. Light touch = she said not to worry about it.
  2. Her words are quoted from OUR transcript only (faster-whisper). No Notability transcript exists for this
     recording (the dump tool finds no plist), so there is no second transcript to agree with; the page says so.
  3. The recording decides WHAT is weighted; it is never the source of a fact. Every answer is taken from the decks
     (visible slide text and pictures; the speaker notes do not count) and cited to a slide.
  4. FLAG rather than follow silently: places where what she said differs from a slide (the slide wins), what she
     said that is on no slide (an aside, not taught), and what her walk skipped.

Lecture numbering: the site and the calendar call the parasites lecture Lecture 17; its deck file is "Lecture 16
Dr. Webster Parasites of Medical Importance.pptx". Citations say "Lecture 17, Slide N" with that file's numbering.

Scope: Lectures 14, 17 and 18 only. Exam 3 (Wednesday 2 December 2026) covers Lectures 14-19; Dr. Fair's Lectures
15 (Fungi), 16 (Food Safety) and 19 (RNA Viruses, 20 November) are examinable and are not here.
"""
_REPO = __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import os
import re

ROOT = _REPO
DONOR = os.path.join(ROOT, "Microbiology Exam 3/micro-exam-3-study-guide.html")
OUT = os.path.join(ROOT, "Microbiology Exam 3/micro-exam-3-webster-review.html")
IMG = "micro-exam-3-study-guide-images/"

PART_LEN = {2: 56 * 60 + 10, 3: 32 * 60 + 18}   # recording part lengths (part 2 56:10, part 3 32:18)

COLD = ("cold", "Know cold")
KNOW = ("know", "Know it")
LIGHT = ("light", "Light touch")

ITEMS = []     # (lecture, anchor, num, toc title, tier class)
FLAGS = []     # (lecture, kind, one-line summary)
LIGHTS = []    # (lecture, what)


def item(lec, anchor, num, title, tier, review, body, lecture=None, toc=None):
    cls, label = tier
    ITEMS.append((lec, anchor, num, toc or title, cls))
    boxes = ""
    if review:
        boxes += ('<div class="asked"><span class="asked-label">In her review</span>'
                  '<p>' + review + '</p></div>\n  ')
    if lecture:
        boxes += ('<div class="asked"><span class="asked-label">In the lecture</span>'
                  '<p>' + lecture + '</p></div>\n  ')
    return ('<h3 class="sub" id="' + anchor + '">' + num + ' &middot; ' + title +
            ' <span class="tier tier-' + cls + '">' + label + '</span></h3>\n  ' +
            boxes + body + '\n')


def flag(body, label="Professor emphasized"):
    return ('<div class="prof-flag"><span class="prof-flag-label">&#9733; ' + label +
            '</span>\n  ' + body + '</div>\n')


def differs(lec, summary, html):
    FLAGS.append((lec, "slide wins", summary))
    return ('<div class="callout"><p><strong>Her words and the slide differ; the slide '
            'wins.</strong> ' + html + '</p></div>')


def aside(lec, summary, html):
    FLAGS.append((lec, "aside", summary))
    return ('<div class="callout"><p><strong>Her aside, not on a slide.</strong> ' + html + '</p></div>')


def gap(lec, summary, html, kind="gap", lead="Not in her review, still examinable."):
    FLAGS.append((lec, kind, summary))
    return ('<div class="callout"><p><strong>' + lead + '</strong> ' + html + '</p></div>')


def conflict(lec, summary, html):
    FLAGS.append((lec, "slides disagree", summary))
    return ('<div class="callout"><p><strong>Two slides disagree.</strong> ' + html + '</p></div>')


def src(text):
    return '<span class="src">%s</span>' % text


def _cite(lec, slides):
    plural = any(t in slides for t in ("&ndash;", ",", " and "))
    return src("Lecture %d, Slide%s %s." % (lec, "s" if plural else "", slides))


def c14(s):
    return _cite(14, s)


def c17(s):
    return _cite(17, s)


def c18(s):
    return _cite(18, s)


def fig(name, w, h, alt, caption, lec, slide):
    return ('<figure class="fig"><img width="%d" height="%d" loading="lazy" src="%s%s" alt="%s">'
            '<figcaption>%s <span class="src">Source: Lecture %d, Slide %s.</span></figcaption></figure>'
            % (w, h, IMG, name, alt, caption, lec, slide))


def iobox(title, objectives):
    lis = "\n".join("    <li>%s</li>" % o for o in objectives)
    return ('<div class="io-box">\n  <h3>%s</h3>\n  <ol>\n%s\n  </ol>\n</div>' % (title, lis))


IO_GENERIC = [
    "Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases, clinical "
    "manifestations, methods of treatment, and prevention of %s of medical importance.",
    "Describe the modes of transmission by which humans acquire %s of medical importance.",
]
IO14 = [o % "Gram-negative bacilli" for o in IO_GENERIC]
IO17 = [o % "parasites" for o in IO_GENERIC]
IO18 = [
    "Recall the steps of DNA virus replication.",
    "Compare and contrast the characteristics of a lytic viral infection versus a persistent chronic or persistent "
    "latent infection.",
    "Differentiate between oncogenic and teratogenic viruses.",
    "Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases, clinical "
    "manifestations, methods of treatment, and prevention of DNA viruses of medical importance.",
    "Compare and contrast the mode of transmission, clinical manifestations, and availability of a vaccine for DNA "
    "viruses of medical importance.",
]

# --------------------------------------------------------------------------
# Section 1 -- Lecture 14, Gram-Negative Bacilli (organism by organism)
# --------------------------------------------------------------------------
S1 = []

S1.append(item(14, "w14-pseudomonas", "1.1", "<em>Pseudomonas aeruginosa</em>", COLD,
  "“Pseudomonas aeruginosa. If you recall, these gram-negative organisms are very, very hard to control because "
  "they are resistant to most antibiotics, also resistant to a lot of chemical controls. How do you know you have "
  "Pseudomonas aeruginosa in the lab? How would you know?” [part 3, 0:13&ndash;0:45] … “we worry about this "
  "particularly when we're talking about patients who have respiratory conditions like cystic fibrosis … It can "
  "also be a problem for burn patients as well.” [1:01&ndash;1:22]",
  f"""<p><strong>How you know it in the lab:</strong> a <strong>grapelike odor</strong> and a <strong>greenish-blue
  pigment (pyocyanin)</strong>. {c14('18')} Many pseudomonads produce water-soluble pigments &mdash; blue-green,
  yellow-green, brown, red; they use aerobic respiration and do not ferment carbohydrates, and they produce oxidase
  and catalase. {c14('14')}</p>
  <p><strong>Why it is hard to control:</strong> resistant to soaps, dyes, quaternary ammonium disinfectants,
  drugs and drying, and able to survive in nutrient-poor environments; a major agent of nosocomial infections.
  {c14('16')} Multidrug resistance comes from restricted outer membrane permeability, antibiotic-inactivating
  enzymes, efflux pumps, horizontal transfer of resistance genes and biofilm formation; it contaminates ventilators,
  intravenous solutions and anesthesia equipment. {c14('17')}</p>
  <p><strong>Who gets it:</strong> a common cause of nosocomial infections in hosts with <strong>burns</strong>,
  neoplastic disease and <strong>cystic fibrosis</strong> (the slide&rsquo;s three asterisks); complications
  include pneumonia, urinary tract infection, abscesses, otitis and corneal disease. {c14('18')} In healthy people:
  skin rashes, urinary tract infection, otitis externa (swimmer&rsquo;s ear) and corneal ulcers in contact lens
  wearers. {c14('19')}</p>
  {fig('l14-s016-pseudomonas-pigment.jpg', 454, 800, 'Culture of Pseudomonas aeruginosa showing its blue-green pigment.', '<em>Pseudomonas aeruginosa</em> and its pigment.', 14, '16')}
  {differs(14, "L14: 'rotten grape odor' vs slide 'grapelike odor'", '''She said “very distinctive rotten grape
  odor” [part 3, 0:59]. The slide says <strong>grapelike odor</strong>; “rotten” is not on it. (She also said
  “yellow-green or blue-green”; Slide 18 names greenish-blue pyocyanin and Slide 14 lists yellow-green among the
  pseudomonad pigments, so both are on slides.)''')}
  <h4 class="subsub">The <em>Pseudomonas</em>-like opportunists <span class="tier tier-light">Light touch</span></h4>
  <div class="asked"><span class="asked-label">In her review</span><p>“And there were a number of other organisms
  that were similar to Pseudomonas that do these opportunistic infections, but don't worry about them so much. Okay,
  I'd rather know something about Pseudomonas aeruginosa.” [part 3, 1:22&ndash;1:36]</p></div>
  <p><em>Burkholderia</em>, <em>Acinetobacter</em> and <em>Stenotrophomonas</em>: similar to pseudomonads,
  obligate aerobes that do not ferment sugars, motile, oxidase positive, opportunistic pathogens. {c14('21')}
  They are on the syllabus list (item 2), so know that one line.</p>"""))
LIGHTS.append((14, "Pseudomonas-like opportunists (Burkholderia, Acinetobacter, Stenotrophomonas)"))

S1.append(item(14, "w14-brucella", "1.2", "<em>Brucella</em> and undulant fever", KNOW,
  "“Brucella causes Brucellosis or undulant fever. And it's called undulant fever, if you recall, because the "
  "fever undulates. It comes, it goes, at kind of regular intervals.” [part 3, 1:36&ndash;1:58]",
  f"""<p>Tiny gram-negative coccobacilli; <em>Brucella abortus</em> (cattle) and <em>Brucella suis</em> (pigs).
  Brucellosis is also called Malta fever, undulant fever and Bang disease. A zoonosis: animal handling or
  slaughtering, contact with blood, urine and placentas of infected animals, or unpasteurized dairy products; human
  to human transmission is rare. {c14('27')}</p>
  <p>It enters through damaged skin or mucous membranes; phagocytes carry it to the blood, with lesions in liver,
  spleen, bone marrow and kidneys. A severe febrile illness with a <strong>fluctuating pattern of fever, weeks to a
  year (undulant fever)</strong>; chills, sweating, headache, muscle pain, weight loss. Tested with an agglutination
  titer; animal vaccine available. {c14('28')}</p>"""))

S1.append(item(14, "w14-francisella", "1.3", "<em>Francisella tularensis</em> and rabbit fever", COLD,
  "“Francisella tularensis. What does this cause? Tularensis, but it's also commonly called rabbit fever. Why is it "
  "called rabbit fever? Because you can contract it from rabbits. So this you often get when you're dealing with, "
  "you're hunting wild rabbits and you have breaks in your skin.” [part 3, 1:58&ndash;2:34]",
  f"""<p><strong>Tularemia, rabbit fever</strong>: a zoonotic disease of mammals endemic to the northern hemisphere,
  particularly rabbits. <strong>Transmitted by contact with infected animals, water and dust, or bites by
  vectors</strong>; incubation days to 3 weeks. Headache, backache, fever,
  chills, malaise and weakness; <strong>ulcerative skin lesions, swollen lymph nodes</strong>; sore throat,
  intestinal involvement and respiratory infection. 10% death rate in the systemic and pulmonic forms. Attenuated
  vaccine. {c14('29')}</p>
  {fig('l14-s029-tularemia-ulcer.jpg', 220, 168, 'An ulcerated skin lesion of tularemia on a hand.', 'The ulcerative skin lesion of tularemia.', 14, '29')}
  {aside(14, "L14: tularemia from hunting wild rabbits through breaks in the skin", '''Hunting wild rabbits with
  breaks in the skin [part 3, 2:29&ndash;2:34] is her example; the slide gives the routes as contact with infected
  animals, water and dust, or vector bites.''')}"""))

S1.append(item(14, "w14-pertussis", "1.4", "<em>Bordetella pertussis</em> and its two stages", COLD,
  "“Bordetella pertussis. What does this cause? Pertussis, whooping cough, yes. And whooping cough, if you recall, it "
  "has two different stages. It has the catarrhal stage, which is basically just kind of like a cold. But then, "
  "what happens next?” [part 3, 2:34&ndash;3:06]",
  f"""<p>A minute, encapsulated coccobacillus causing pertussis (whooping cough), a communicable childhood
  affliction; often severe in babies; reservoir apparently healthy carriers; transmission by direct contact or
  inhaled aerosols. {c14('30')}</p>
  <table>
    <tr><th>Stage</th><th>What happens</th></tr>
    <tr><td><strong>Catarrhal</strong></td><td>Nasal drainage, congestion, sneezing, occasional cough</td></tr>
    <tr><td><strong>Paroxysmal</strong></td><td>Recurrent persistent cough, followed by deep inhalation &mdash; the <strong>whoop</strong></td></tr>
  </table>
  <p>Toxins destroy and dislodge ciliated cells; loss of the ciliary mechanism builds up mucus and blocks the airway;
  complications come from compromised respiration. Vaccine DTaP (acellular, toxoid plus other antigens), 5 doses
  between 2 months and 6 years; Boostrix for ages 10&ndash;18. {c14('31')}</p>
  {fig('l14-s032-pertussis-course.jpg', 599, 416, 'Graph of the course of pertussis through its stages.', 'The course of pertussis.', 14, '32')}"""))

S1.append(item(14, "w14-legionella", "1.5", "<em>Legionella</em>: the water reservoir", COLD,
  "“Legionella causes Legionnaires' disease. All right. And what's the reservoir of infection for Legionella? Water. "
  "This is the one that you are typically going to contract from standing water, like on the cooling towers of the "
  "hotels, you're breathing in the aerosols” [part 3, 3:38&ndash;4:09] … “particularly if they are smokers” [4:21] … "
  "“Or the vegetable sprayers.” [4:44]",
  f"""<p><em>Legionella pneumophila</em>: weakly Gram-negative, motile, pleomorphic; cannot be easily cultured.
  <strong>Widely distributed in water</strong>: tap water, cooling towers, spas, ponds, air conditioning systems,
  supermarket vegetable spraying systems; <strong>lives in close association with amoebas</strong>. {c14('39')}</p>
  <p><strong>Transmitted by aerosols.</strong> Legionnaires disease and Pontiac fever; prevalent in males over 50;
  nosocomial; elderly patients with diabetes, cancer, transplants, chronic alcoholism or chronic lung disease, and
  <strong>smokers</strong>. Fever, cough, diarrhea, abdominal pain, pneumonia. {c14('40')} A Florida outbreak came
  from the spray of a decorative fountain. {c14('42')}</p>
  {fig('l14-s041-legionella.jpg', 304, 590, 'Legionella growth on charcoal yeast extract agar and Legionella inside amoebas.', 'Growth on charcoal yeast extract agar, and <em>Legionella</em> inside amoebas.', 14, '41')}"""))

S1.append(item(14, "w14-diarrhea", "1.6", "Toxigenic versus invasive diarrheal disease", COLD,
  "“There are two kinds of diarrheal diseases. What are they? One is the toxigenic and the other one is the "
  "invasive. … And what can be one characteristic symptom that is invasive as opposed to toxigenic? The diarrhea is "
  "bloody.” [part 3, 5:14&ndash;6:11]",
  f"""<p>The Enterobacteriaceae are the most frequent cause of diarrheal disease, by <strong>enterotoxins</strong> or
  by <strong>invasive infection</strong>. {c14('43')} The slide&rsquo;s picture sets the two side by side:
  <strong>toxigenic</strong>, example ETEC (enterotoxigenic <em>Escherichia coli</em>); <strong>invasive</strong>,
  example <em>Shigella</em>. {c14('44')}</p>
  {fig('l14-s044-toxigenic-invasive.jpg', 860, 900, 'Diagram comparing toxigenic diarrhea, where toxin acts on the intestinal lining, with invasive diarrhea, where bacteria enter the mucosa.', 'Toxigenic (left) and invasive (right) diarrheal disease.', 14, '44')}
  <p>Bloody stool marks the invasive organisms in the deck: EIEC gives profuse bloody diarrhea with mechanical
  damage to the intestinal wall and no toxins {c14('57')}; <em>Shigella</em> invades the villus of the large
  intestine and gives watery stool with blood. {c14('78')}</p>"""))

S1.append(item(14, "w14-lactose", "1.7", "Coliform versus non-coliform: lactose", COLD,
  "“And how can you distinguish between the coliform enterobacteriaceae and the non-coliform enterobacteriaceae? In "
  "the lab, how do you distinguish them? We're looking at what carbohydrate can they or can't they ferment? Lactose. "
  "Okay. Remember, lactose fermenters, that's like E. coli. That's why we grew it on EMB and McConkie's.” "
  "[part 3, 6:20&ndash;7:13]",
  f"""<p>Enterics are facultative anaerobes; all ferment glucose, reduce nitrates to nitrites, are oxidase negative
  and catalase positive; <strong>coliforms are lactose fermenters, non-coliforms are non-lactose
  fermenters</strong>. {c14('46')}</p>
  <table>
    <tr><th>Medium</th><th>Selective for</th><th>Differential for</th></tr>
    <tr><td><strong>EMB</strong> (eosin and methylene blue) agar</td><td>Gram-negatives</td><td>Lactose fermenters</td></tr>
    <tr><td><strong>MacConkey&rsquo;s</strong> agar (crystal violet and bile salts)</td><td>Gram-negatives</td><td>Lactose fermenters</td></tr>
  </table>
  <p>{c14('48')} Coliforms in normal flora: <em>Escherichia coli</em>, <em>Enterobacter</em>, <em>Klebsiella</em>,
  <em>Hafnia</em>, <em>Citrobacter</em>, <em>Serratia</em>. Non-coliforms: <em>Proteus</em>, <em>Providencia</em>,
  <em>Morganella</em>, <em>Edwardsiella</em>. {c14('50')} <em>Salmonella</em> and <em>Shigella</em> are non-coliform
  (lactose-negative) true pathogens. {c14('69')}</p>
  {fig('l14-s048-emb-agar.jpg', 648, 643, 'EMB agar plate with colonies showing a metallic green sheen.', 'EMB agar: the lactose fermenter&rsquo;s colonies.', 14, '48')}
  {fig('l14-s048-macconkey-agar.jpg', 528, 291, 'MacConkey agar plate with a lactose-negative streak on one side and a pink lactose-positive Escherichia coli streak on the other.', 'MacConkey agar: lactose negative against lactose positive (<em>E. coli</em>).', 14, '48')}"""))

S1.append(item(14, "w14-ecoli", "1.8", "The four <em>Escherichia coli</em> types", COLD,
  "“The Escherichia coli types. Alright. We have four different E. coli types. ETEC, EIEC, EPEC, and EHEC. You need "
  "to know all four types and what they do.” [part 3, 7:13&ndash;7:45] … “But please review those four types of E. "
  "coli. I won't even tell you. There's multiple questions because it's important.” [8:33&ndash;8:51]",
  f"""{flag('''<p>This is the strongest instruction in her whole review: “You need to know all four types and what
  they do” and “There&rsquo;s multiple questions because it&rsquo;s important.” Expect more than one question on
  these four rows.</p>''')}
  <table>
    <tr><th>Type</th><th>What it does</th><th>Signature</th></tr>
    <tr><td><strong>ETEC</strong> &mdash; enterotoxigenic</td><td>Heat-labile (LT) and heat-stable (ST) toxins promote secretion of fluid and electrolytes in the intestinal epithelium: diarrhea, cramping, low-grade to no fever; fimbriae for adhesion to the small intestine {c14('56')}</td><td><strong>70% of traveler&rsquo;s diarrhea</strong>; toxigenic</td></tr>
    <tr><td><strong>EIEC</strong> &mdash; enteroinvasive</td><td>Inflammatory disease of the large intestine, similar to shigellosis; adhesin proteins bind the intestinal wall; mechanical cell damage; <strong>no toxins</strong>; very young and very old most susceptible {c14('57')}</td><td><strong>Profuse bloody diarrhea and high fever</strong>; invasive</td></tr>
    <tr><td><strong>EPEC</strong> &mdash; enteropathogenic</td><td>Adherence to the intestinal lining with destruction of microvilli; inhibits vitamin B1 (thiamin) uptake; prevention: breast feeding {c14('58')}</td><td><strong>Wasting infantile diarrhea</strong>; greatest single cause of infant mortality worldwide</td></tr>
    <tr><td><strong>EHEC</strong> &mdash; enterohemorrhagic, O157:H7</td><td>Diarrhea, hemorrhagic colitis and hemolytic uremic syndrome; Shiga toxin {c14('59')}; reservoir the intestines of cattle; contaminated beef, water, vegetables {c14('60')}</td><td><strong>Hemolytic uremic syndrome</strong> (item 1.9)</td></tr>
  </table>
  <div class="pearl"><p>The first letter after &ldquo;Entero&rdquo; is what it does: <strong>T</strong>oxin,
  <strong>I</strong>nvades, <strong>P</strong>ediatric wasting (sticks to and destroys microvilli),
  <strong>H</strong>emorrhage and hemolytic uremic syndrome.</p></div>"""))

S1.append(item(14, "w14-o157", "1.9", "O157:H7 and hemolytic uremic syndrome", COLD,
  "“What do we worry about with the O157H7? Why are we worried about that one? The enterohemorrhagic. … That's the "
  "one that can cause hemolytic uremic syndrome. … And what does that O157H7 even mean? What are we talking about? "
  "We're talking about surface antigens. It's how we identify them.” [part 3, 7:45&ndash;8:44]",
  f"""<p><strong>O157</strong> is the O (somatic) type antigen 157; <strong>H7</strong> is the H (flagellar) type
  antigen 7. {c14('59')} The enteric surface antigens are H (flagellar), K (capsule and/or fimbrial) and O (somatic
  or cell wall; all have it). {c14('52')}</p>
  {fig('l14-s053-enteric-antigens.png', 542, 483, 'Drawing of an enteric rod showing the flagellar H antigen, the capsular K antigen and the somatic O antigen.', 'The H, K and O antigens.', 14, '53')}
  <p>EHEC causes diarrhea, hemorrhagic colitis and <strong>hemolytic uremic syndrome</strong>; Shiga toxin binds
  ribosomes and disrupts protein synthesis, so endothelial cells detach, platelets meet the subendothelium and
  coagulation starts. {c14('59')} About <strong>10% of cases</strong> develop hemolytic uremic syndrome &mdash; toxins
  produce apoptosis of renal tubular epithelial cells, and coagulation. Reservoir: the intestines of cattle;
  infectious dose 100 cells. {c14('60')} Treatment includes dialysis, transfusions and plasmapheresis;
  <strong>antibiotic therapy may exacerbate hemolytic uremic syndrome</strong>. {c14('63')} On rainbow agar
  O157:H7 colonies are black (glucuronidase negative). {c14('64')}</p>"""))

S1.append(item(14, "w14-proteus", "1.10", "<em>Proteus</em>: swarming", COLD,
  "“Then when we have the ones which do not ferment lactose, like Proteus. Proteus, which we see as an agent of "
  "urinary tract infections. If we are growing Proteus on a plate of auger, what's it going to do? It, remember, is "
  "highly motile, so it swarms the plate.” [part 3, 8:51&ndash;9:34]",
  f"""<p>A non-coliform (lactose-negative) opportunist. {c14('69')} <em>Proteus</em>: urinary tract infection, wound
  infections, pneumonia, septicemia and infant diarrhea; nosocomial; related to bladder and kidney stones;
  <strong>highly motile</strong>. {c14('70')} Diagnostic growth pattern: the <strong>wavelike, swarming
  pattern</strong> of <em>Proteus vulgaris</em>, with peritrichous flagella. {c14('71')}</p>
  {fig('l14-s071-proteus-swarming.jpg', 325, 568, 'Agar plate covered by concentric waves of swarming growth.', 'The swarming growth of <em>Proteus</em>.', 14, '71')}"""))

S1.append(item(14, "w14-typhi", "1.11", "<em>Salmonella</em> Typhi and the carrier", COLD,
  "“We have salmonella typhi causes typhoid fever. Okay. Now, typhoid fever, we worry about that one because there "
  "are many individuals who are asymptomatic. Remember Typhoid Mary? … But where does the organism like to go hide? … "
  "It's in her gallbladder. … But it gets released with the bile, so it's in every bowel movement.” "
  "[part 3, 9:34&ndash;10:36]",
  f"""<p><em>Salmonella typhi</em> and <em>S. paratyphi</em> cause typhoid and paratyphoid fever; humans are the
  exclusive hosts; resistant to bile and dyes; enters with fecally contaminated food or water. <strong>Asymptomatic
  carriers; some chronic carriers shed bacilli from the gallbladder.</strong> {c14('73')} The bacilli adhere to the
  small intestine and cause invasive diarrhea that leads to septicemia; sustained fever of 103&ndash;104 degrees,
  a rash of rose-colored spots; two vaccines give temporary protection. {c14('74')}</p>
  {aside(14, "L14: Typhoid Mary; organism released with the bile into every bowel movement", '''Typhoid Mary and the
  bile carrying the organism “in every bowel movement” [part 3, 10:00&ndash;10:36] are her illustration; the
  slide&rsquo;s fact is that some chronic carriers shed bacilli from the gallbladder.''')}
  {fig('l14-s074-typhoid-route.jpg', 511, 687, 'Diagram of the route of Salmonella Typhi through the body.', 'The course of typhoid fever.', 14, '74')}"""))

S1.append(item(14, "w14-salmonelloses", "1.12", "The other salmonelloses", KNOW,
  "“And then we have the other salmonelloses, which are primarily gastrointestinal problems. We can get those from "
  "things like improperly cooked chicken, contaminate eggs, your pet turtles, your backyard chickens.” "
  "[part 3, 10:42&ndash;11:09]",
  f"""<p>Salmonelloses other than typhoid are enteric fevers, <em>Salmonella</em> food poisoning and gastroenteritis;
  less severe than typhoid but more prevalent. All zoonotic in origin. Acquired by ingestion: cattle, poultry and
  eggs, rodents, reptiles (pet turtles), animal and dairy products; fomites contaminated with animal intestinal flora.
  Gastroenteritis: vomiting, diarrhea, fluid loss. {c14('76')} Animal-borne sources on the next slide: backyard
  flocks, small turtles, bearded dragons. {c14('77')}</p>"""))

S1.append(item(14, "w14-shigella", "1.13", "<em>Shigella</em>: invasive and bloody", KNOW,
  "“And then we have Shigella. And Shigella is a GI organism, which is an invasive GI organism, because that one has "
  "a characteristic bloody diarrhea.” [part 3, 11:15&ndash;11:29]",
  f"""<p>Shigellosis is an incapacitating dysentery: abdominal cramps and watery stool with blood; 2&ndash;7% also
  cause hemolytic uremic syndrome. Transmitted by ingesting fecally contaminated food. It <strong>invades the villus
  of the large intestine</strong>, does not perforate the intestine or invade the blood; endotoxin initiates fever;
  enterotoxin damages mucosa and villi &mdash; bleeding and mucus secretion. {c14('78')} It is the slide&rsquo;s
  example of invasive diarrheal disease. {c14('44')}</p>"""))

S1.append(item(14, "w14-plague", "1.14", "<em>Yersinia pestis</em> and the three plagues", COLD,
  "“Then we have Yersinia pestis. What does Yersinia pestis cause? Plague … You can get bubonic plague. And "
  "typically, how do you acquire bubonic plague? From the flea, from a rat flea. … And it can form the buboes, the "
  "grossly enlarged lymph nodes. But it can also cause subcutaneous hemorrhaging, which is why it was also called "
  "what? The black death. And what is the most serious form of plague? The pneumonic form. And that is the one "
  "which can be directly transmitted from person to person.” [part 3, 11:45&ndash;12:55]",
  f"""<p>A tiny gram-negative rod with unusual bipolar staining and capsules. {c14('81')} Flea vectors: the bacteria
  replicate in the flea&rsquo;s gut, coagulase clots blood and blocks its esophagus, the ravenous flea bites more
  hosts and regurgitated material transmits the bacterium. Found in 200 species of mammals (rodents). {c14('83')}</p>
  <table>
    <tr><th>Form</th><th>Slide</th></tr>
    <tr><td><strong>Bubonic</strong></td><td>Bacillus multiplies in the flea bite, enters lymph, causes necrosis and swelling called a <strong>bubo</strong> in groin or axilla</td></tr>
    <tr><td><strong>Septicemic</strong></td><td>Massive bacterial growth; intravascular coagulation, subcutaneous hemorrhage and purpura degenerating into necrosis and gangrene &mdash; <strong>black plague</strong></td></tr>
    <tr><td><strong>Pneumonic</strong></td><td>Localized to the lungs, <strong>highly contagious by aerosol</strong>, fatal without treatment</td></tr>
  </table>
  <p>{c14('88')}</p>
  {fig('l14-s084-plague-cycle.jpg', 800, 397, 'Infection cycle of Yersinia pestis between rodents, fleas and humans.', 'The infection cycle of <em>Yersinia pestis</em>.', 14, '84')}
  {differs(14, "L14: 'which is why it was also called the black death' vs slide 'black plague' (septicemic)", '''She
  tied the subcutaneous hemorrhaging to “the black death” [part 3, 12:29&ndash;12:40]. Slide 88 calls that
  septicemic form <strong>black plague</strong>; “Black Death” on Slide 94 is the 1346&ndash;1350 pandemic. Use
  the slide&rsquo;s words.''')}
  {differs(14, "L14: pneumonic plague 'directly transmitted from person to person' vs slide 'highly contagious by aerosol'", '''She
  said the pneumonic form “can be directly transmitted from person to person” [part 3, 12:51&ndash;12:55]. Slide 88
  says it is <strong>highly contagious by aerosol</strong> and fatal without treatment; Slide 83 says plague caught
  from infected humans is rare. Her “rat flea” [12:12] is the slides&rsquo; flea vector of rodents. {c14('83')}''')}"""))

S1.append(item(14, "w14-haemophilus", "1.15", "<em>Haemophilus</em>", COLD,
  "“Hemophilus. What can hemophilus do? It doesn't cause influenza, even though it's named inappropriately. But it "
  "can cause a meningitis. It can cause chancery. We do have vaccinations against this one.” [part 3, 13:10&ndash;13:34]",
  f"""<p>Tiny gram-negative pleomorphic rods (“blood loving”); fastidious; none grow on blood agar without special
  techniques &mdash; <strong>chocolate agar</strong>; require hemin, NAD or NADP. {c14('97')}</p>
  <table>
    <tr><th>Species</th><th>Disease</th></tr>
    <tr><td><em>H. influenzae</em></td><td><strong>Misnamed</strong> as the cause of flu; acute bacterial <strong>meningitis</strong>, epiglottitis, otitis media, sinusitis, pneumonia, bronchitis; vaccine: subunit <strong>Hib</strong> {c14('98')}</td></tr>
    <tr><td><em>H. ducreyi</em></td><td><strong>Chancroid</strong>, a sexually transmitted disease; primarily tropics, primarily males {c14('100')}</td></tr>
    <tr><td><em>H. aegyptius</em></td><td>Conjunctivitis (pink eye), primarily children {c14('100')}</td></tr>
  </table>
  {conflict(14, "L14: slide 97 lists H. parainfluenzae with H. ducreyi as virulent (meningitis, chancroid); slide 100 calls H. parainfluenzae normal flora (endocarditis)", '''Slide 97 says “others (<em>H.
  parainfluenzae</em>, <em>H. ducreyi</em>) are virulent species responsible for childhood meningitis, and
  chancroid”; Slide 100 gives <em>H. parainfluenzae</em> as normal oral and nasopharyngeal flora that can cause
  infective endocarditis, and Slide 98 gives meningitis to <em>H. influenzae</em>. Safe pairing: meningitis &rarr;
  <em>H. influenzae</em> (Hib vaccine); chancroid &rarr; <em>H. ducreyi</em>.''')}"""))

S1.append(item(14, "w14-endotoxin", "1.16", "Endotoxin: the weapon they all have", COLD,
  "“Now, what do all of our gram-negative bacilli have as an offensive weapon? … How about endotoxin? Endotoxin. All "
  "gram-negatives have endotoxin. And where do they get endotoxin? It is part of the outer membrane of the "
  "gram-negative cell wall. And remember, it is released when the organism dies. That's why if you're being treated "
  "with antibiotics, then you may feel worse before you feel better. Because mild release just causes very general "
  "symptomology, like fever, aches, pains, malaise. But if you get a real heavy dose of it, it can actually cause a "
  "septic shock.” [part 3, 13:44&ndash;14:59]",
  f"""<p>Endotoxin is a <strong>structural component of the Gram-negative outer membrane</strong>; chemically a
  <strong>lipopolysaccharide</strong>; <strong>lipid A</strong> is the biologically active component. It is
  released <strong>on lysis of Gram-negative cells, including through antibiotic therapy</strong>, and <strong>as
  cells grow and divide, particularly when rapidly proliferating</strong>. {c14('5')} All the aerobic
  Gram-negative nonenteric bacilli use endotoxin as one of their offensive weapons. {c14('13')}</p>
  {fig('l14-s005-lipopolysaccharide.jpg', 900, 321, 'Gram-negative rods, the cell wall with the lipopolysaccharide on the outer membrane, and one lipopolysaccharide unit with lipid A.', 'Where endotoxin sits: the lipopolysaccharide of the outer membrane.', 14, '5')}
  <p><strong>Low levels</strong> give a low-level inflammatory response &mdash; fever, malaise, aches, pains.
  <strong>A large flood</strong> releases mediators that contribute to <strong>septic shock</strong>: TNF (tumor
  necrosis factor) and IL-1 (interleukin 1) drive neutrophil-endothelial adhesion and clotting, intravascular
  microthrombi, “warm shock” first, then falling cardiac output and blood pressure, tissue hypoxia and multisystem
  organ failure. {c14('11')}</p>
  {differs(14, "L14: endotoxin 'released when the organism dies' only; slide adds release during growth and division", '''She
  said it “is released when the organism dies” [part 3, 14:28]. True, and the slide adds a second release: as the
  bacteria grow and divide, particularly when rapidly proliferating. Know both.''')}"""))

# --------------------------------------------------------------------------
# Section 2 -- Lecture 17, Parasites (organism by organism)
# --------------------------------------------------------------------------
S2 = []

S2.append(item(17, "w17-entamoeba", "2.1", "<em>Entamoeba histolytica</em>; cyst and trophozoite", COLD,
  "“Entamoeba histolytica causes anemic dysentery. And in many of these, we have two different forms of the "
  "protozoan parasite. What are the two different forms of the protozoan parasite that you could have? ASSIST, and "
  "what's the other one called? Atrophozoite. And what does that mean? … It's the one that is actively moving and "
  "feeding.” [part 3, 15:23&ndash;15:57] (The transcript&rsquo;s “anemic” is “amebic”, and “ASSIST … Atrophozoite” "
  "is “a cyst … a trophozoite”.)",
  f"""<p><strong>The two forms.</strong> Most protozoa propagate by asexual division of the <strong>active feeding
  cell, the trophozoite</strong>; many also form a <strong>cyst</strong>. {c17('12')} <em>Entamoeba
  histolytica</em> alternates between a large trophozoite, motile by pseudopods, and a smaller nonmotile cyst.
  {c17('16')}</p>
  {fig('l17-s017-trophozoite-and-cyst.jpg', 581, 315, 'Micrographs of a trophozoite and a cyst of Entamoeba histolytica, labeled.', 'Trophozoite (a) and cyst (b).', 17, '17')}
  <p><strong>The disease.</strong> Humans are the primary hosts; it is ingested. {c17('16')} Swallowed cysts reach
  the small intestine, where alkaline pH and digestive juices release 4 trophozoites, which attach, multiply, move
  and feed; asymptomatic in 90%. {c17('19')} Intestinal amebiasis targets cecum, appendix, colon and rectum: the ameba
  dissolves tissue, causing <strong>dysentery</strong>, abdominal pain, fever, diarrhea and weight loss. {c17('20')}
  Extraintestinal: most commonly liver abscesses (amebic hepatitis), also lungs and other organs. {c17('21')}
  Diagnosis: fecal smear; ELISA with monoclonal antibodies. {c17('23')}</p>
  {fig('l17-s015-amebas-in-tissue.jpg', 286, 245, 'Stained tissue section with amebas.', 'Infective amebas in tissue.', 17, '15')}"""))

S2.append(item(17, "w17-naegleria", "2.2", "<em>Naegleria fowleri</em> and <em>Acanthamoeba</em>", COLD,
  "“Now, nigleria fowleri is also one of our infective amoebas. Why do we worry about this one? This is the one which "
  "you get by getting water up your nose, burrowing into the brain. And if you do not treat it within the first few "
  "days, it is almost invariably fatal. And we worry about this one, because we've got a lot of it here in Florida. "
  "Pretty much any of the little ponds, little lakes, fresh water. Acanthoepa caudicosa is the same thing, only a "
  "longer incubation time.” [part 3, 16:10&ndash;16:59]",
  f"""<p>Amebic meningoencephalitis is caused by <em>Naegleria fowleri</em> and <em>Acanthamoeba</em>, which inhabit
  standing water with a high bacterial count: hot springs, lakes, streams, unchlorinated swimming pools. {c17('24')}
  <em>Naegleria</em> is <strong>acquired through nasal contact with water</strong> &mdash; diving, waterskiing, jet
  skiing, rinsing sinuses even with tap water; most cases are children and young adults. {c17('28')}</p>
  <p><strong>Primary acute meningoencephalitis:</strong> the trophozoite burrows through the nasal mucosa and travels
  into the brain through the <strong>olfactory nerve</strong>; headache, fever, vomiting, stiff neck; rapid
  destruction of brain and spinal cord; <strong>coma, death in 3&ndash;7 days</strong>. Over 46% of lakes in Florida
  have <em>N. fowleri</em>. Treatment must be early. {c17('29')}</p>
  {fig('l17-s028-naegleria-trophozoites.jpg', 258, 204, 'Stained Naegleria fowleri trophozoites.', '<em>Naegleria fowleri</em> trophozoites.', 17, '28')}
  <p><strong><em>Acanthamoeba</em>:</strong> freshwater lakes, hot tubs, pools; amebic keratitis in contact lens
  wearers; granulomatous amebic encephalitis &mdash; enters through a break in the skin or the nasal passages,
  meningitis symptoms but a <strong>longer progression</strong>; survival only 2&ndash;3%. {c17('31')}</p>
  {differs(17, "L17: Acanthamoeba 'longer incubation time' vs slide 'longer progression'", '''She said
  <em>Acanthamoeba</em> is “the same thing, only a longer incubation time” [part 3, 16:56&ndash;16:59]; the slide says
  meningitis symptoms with a <strong>longer progression</strong>, and gives no incubation time.''')}"""))

S2.append(item(17, "w17-balantidium", "2.3", "<em>Balantidium coli</em>, the ciliate", LIGHT,
  "“Ballantinium coli is our ciliate. But unless you're working near a pig farm, I wouldn't worry about that one too "
  "much.” [part 3, 17:05&ndash;17:13]",
  f"""<p>One line to carry: the intestinal <strong>ciliate</strong>, an occupant of the intestines of domestic animals
  such as <strong>pigs</strong> and cattle; acquired by ingesting cyst-containing food or water. {c17('33')}</p>"""))
LIGHTS.append((17, "Balantidium coli"))

S2.append(item(17, "w17-giardia", "2.4", "<em>Giardia lamblia</em>", COLD,
  "“Giardia lamblia. How do you acquire Giardia lamblia? This is the one that you'll get if you're camping and you "
  "are not drinking decontaminated water … You get the cyst form, which will then grow into the trophozoite form. So "
  "you end up with gastrointestinal symptomology.” [part 3, 17:17&ndash;17:47]",
  f"""<p>A pathogenic flagellate with a unique symmetrical heart shape and a concave ventral surface that acts like a
  suction cup; cysts small, compact, multinucleate. Reservoirs include beavers, cattle, coyotes, cats and humans;
  cysts survive 2 months; <strong>usually ingested with water and food</strong>; infective dose 10&ndash;100 cysts.
  {c17('39')} Cysts enter the duodenum, germinate, travel to the jejunum to feed and multiply; giardiasis is diarrhea
  and abdominal pain. Microscopy is difficult because shedding is intermittent; PCR. Killed by boiling, ozone and
  iodine. {c17('41')}</p>
  {fig('l17-s040-giardia-trophozoite-smear.jpg', 300, 300, 'Stained pear-shaped Giardia trophozoite in a stool smear.', '<em>Giardia</em> trophozoite.', 17, '40')}
  {fig('l17-s040-giardia-cysts-smear.jpg', 300, 300, 'Two oval Giardia cysts in a stool smear.', '<em>Giardia</em> cysts.', 17, '40')}
  {aside(17, "L17: Giardia from camping and clear streams", '''Camping and the “beautifully nice, clear-looking
  stream” [part 3, 17:23&ndash;17:35] are her example; the slide&rsquo;s fact is ingestion with water and food, with
  beavers among the reservoirs.''')}"""))

S2.append(item(17, "w17-trichomonas", "2.5", "<em>Trichomonas vaginalis</em>", COLD,
  "“Trichomonas vaginalis. Why do we worry about this one? Very common STD. It is a flagellate. … And how will you "
  "diagnose this baby? You will look at secretions. You will look at vaginal secretions, or semen. … These little guys "
  "swimming around. And I know I gave you a picture on that one too.” [part 3, 18:03&ndash;18:37]",
  f"""<p>Trichomonads are small, pear-shaped, with 4 anterior flagella and an undulating membrane; they
  <strong>exist only in trophozoite form &mdash; no cyst</strong>. {c17('36')} <em>T. vaginalis</em> causes
  trichomoniasis, the <strong>most common curable sexually transmitted disease in young, sexually active
  women</strong>; reservoir the human urogenital tract; 60&ndash;70% asymptomatic; women: foul-smelling
  green-to-yellow discharge, vulvitis, cervicitis; men: urethritis, thin milky discharge. {c17('37')}
  <strong>Diagnosis by microscopic analysis of a vaginal smear</strong>; treated with metronidazole and tinidazole.
  {c17('38')}</p>
  {fig('l17-s038-trichomonas-smear.jpg', 300, 300, 'Two stained pear-shaped flagellates with flagella and an undulating membrane.', 'The picture she meant: <em>Trichomonas vaginalis</em>.', 17, '38')}
  {aside(17, "L17: Trichomonas seen in semen", '''She added semen [part 3, 18:27]; the slide names only the vaginal
  smear.''')}"""))

S2.append(item(17, "w17-brucei", "2.6", "<em>Trypanosoma brucei gambiense</em> and sleeping sickness", KNOW,
  "“Then we have other flagellates, trypanosoma. These are blood flagellates. And we will diagnose those by actually "
  "seeing those little flagellates swimming around in a blood smear. They are transmitted by insect vectors, "
  "trypanosoma brucei gambiense, African sleeping sickness, transmitted by the bite of the tsetse fly. … If not "
  "treated, the African sleeping sickness organism can ultimately cause coma and death.” [part 3, 18:44&ndash;19:46]",
  f"""<p>Hemoflagellates are obligate blood and tissue parasites spread by blood-sucking insects. {c17('42')}
  <em>T. brucei</em> causes African sleeping sickness; <em>T. cruzi</em> Chagas disease. {c17('44')} <em>T.
  brucei</em> is <strong>spread by tsetse flies</strong>; <em>T. b. gambiense</em> is the Gambian strain (West
  Africa), <em>T. b. rhodesiense</em> the Rhodesian (East Africa). {c17('45')} The bite inoculates trypomastigotes
  (primary chancre); they disseminate in blood and damage spleen, lymph nodes and brain; the Gambian form is chronic
  with brain symptoms years later. {c17('46')} Progression to sleep disturbances, tremors, seizures, paralysis and
  <strong>coma</strong>; trypanosomes are readily demonstrated in blood, spinal fluid or lymph nodes. {c17('47')}</p>
  {fig('l17-s046-trypanosomes-blood-smear.jpg', 220, 156, 'Blood smear with wavy flagellates between red blood cells.', 'Trypanosomes swimming between red blood cells.', 17, '46')}"""))

S2.append(item(17, "w17-cruzi", "2.7", "<em>Trypanosoma cruzi</em> and Chagas disease", COLD,
  "“The other trypanosoma, trypanosoma cruzi, causes what? Chagas disease. And what is the vector for that one? That "
  "one is the reduva beetle or kissing bug … And when it bites you, it defecates and you scratch the bite right and "
  "inoculate yourself. … Warming has caused the range of the reduva beetle to come up into our area. … And it can "
  "cause cardiac problems.” [part 3, 19:52&ndash;20:53]",
  f"""<p><em>T. cruzi</em> causes <strong>Chagas disease</strong> (American trypanosomiasis); millions of cases in
  Latin America, becoming more of an issue in the southern United States through <strong>vector migration</strong>
  (three asterisks on the slide); now considered by many to be endemic in the United States. {c17('48')}
  The <strong>reduviid bug (kissing bug)</strong> is the vector; infection occurs when <strong>bug feces is
  inoculated into a cutaneous portal</strong>; also congenital, transfusion, transplant and foodborne routes. Romaña
  sign (chagoma, a swelling of the eyelid with conjunctivitis); <strong>heart muscle</strong> and large intestine
  harbor amastigotes; chronic inflammation of heart and brain (30&ndash;40% of heart disease in endemic regions).
  {c17('49')}</p>
  {fig('l17-s050-chagas-cycle-and-map.jpg', 550, 432, 'Chagas disease transmission cycle with the kissing bug, and a distribution map.', 'American trypanosomiasis: the cycle and its range.', 17, '50')}
  {differs(17, "L17: 'reduva beetle' vs slide 'reduviid bug (kissing bug)'", '''She said “reduva beetle”; the
  slide&rsquo;s vector is the <strong>reduviid bug (kissing bug)</strong>.''')}"""))

S2.append(item(17, "w17-leishmania", "2.8", "<em>Leishmania</em>", KNOW,
  "“Lishmatii, this is the one that is transmitted by the sand fleas, alternate host the dog, causes things like kala "
  "azar.” [part 3, 20:53&ndash;21:18]",
  f"""<p>Leishmaniasis is a zoonosis transmitted among mammalian hosts by <strong>female sand flies</strong> that
  need a blood meal to produce eggs; endemic to equatorial regions; <strong>alternate hosts dogs</strong>.
  Promastigotes are injected with the bite and convert to amastigotes. {c17('52')} Forms: cutaneous (oriental sore,
  Baghdad boil), espundia (skin and mucous membranes of the head), systemic visceral &mdash; <strong>kala azar is the
  most severe and fatal form if untreated</strong>. {c17('53')}</p>
  {fig('l17-s054-leishmania-life-cycle.jpg', 477, 397, 'Life cycle of Leishmania between the sand fly and the human host.', 'The <em>Leishmania</em> life cycle.', 17, '54')}
  {differs(17, "L17: 'sand fleas' vs slide 'female sand flies'", '''She said “sand fleas”; the slide says
  <strong>sand flies</strong> (female). Fleas carry plague and murine typhus (Slide 130).''')}"""))

S2.append(item(17, "w17-plasmodium", "2.9", "<em>Plasmodium</em> and malaria", COLD,
  "“Plasmonium, what does it cause? Malaria. And plasmonium is transmitted by what arthropod vector? The anopheles "
  "mosquito. … goes into what organ first? Goes into your liver … and then cells are released from the liver to go "
  "into your blood cells. … It's like a little ring inside, a ring formation inside red blood cells that you should "
  "be able to recognize. … And what do you have when you have those bursts of the red blood cell? That's when you have "
  "fever and chills. And it happens at regular intervals” [part 3, 21:18&ndash;22:49]",
  f"""<p>The <strong>female <em>Anopheles</em> mosquito</strong> is the primary vector (also blood transfusion, mother
  to fetus); four species, <em>P. malariae</em>, <em>P. vivax</em>, <em>P. falciparum</em>, <em>P. ovale</em>.
  {c17('56')} The mosquito injects sporozoites, which <strong>localize in the liver</strong> and undergo schizogony;
  merozoites enter the circulation in 5&ndash;16 days (exoerythrocytic phase), enter red blood cells and
  <strong>convert to circular ring trophozoites</strong>; the red cell bursts, releasing merozoites (erythrocytic
  phase). {c17('58')} Regular episodes of chills, fever and sweating; <strong>symptoms at 48&ndash;72 hour intervals
  as red blood cells rupture</strong>; <em>P. falciparum</em> is the most malignant; <strong>diagnosis by the
  trophozoite in red blood cells</strong>. {c17('60')}</p>
  {fig('l17-s060-ring-trophozoites.jpg', 676, 482, 'Closely packed red blood cells, many containing a small dark ring, with pointers labeled ring trophozoites and red blood cell.', 'The picture to recognize: <b>ring trophozoites</b> inside red blood cells.', 17, '60')}
  {fig('l17-s059-plasmodium-life-cycle.jpg', 660, 705, 'The Plasmodium life cycle through mosquito, liver and red blood cells.', 'The <em>Plasmodium</em> life cycle.', 17, '59')}
  {differs(17, "L17: Plasmodium 'does not have a trophozoite form' vs slides 58 and 60 ring trophozoites", '''She said
  “It does not have a trophozoite form” [part 3, 21:33]. The slides say the opposite: merozoites “convert to circular
  ring trophozoites” in red cells {c17('58')}, and diagnosis is “by presence of trophozoite in RBCs” {c17('60')}.
  The ring she told you to recognize <em>is</em> the trophozoite. (The protozoan the slides give “only in trophozoite
  form &mdash; no cyst” is <em>Trichomonas</em>, {c17('36')})''')}"""))

S2.append(item(17, "w17-toxoplasma", "2.10", "<em>Toxoplasma gondii</em>", COLD,
  "“Then we have toxoplasma gondii, which causes toxoplasmosis. How do you get that one? From your cat, yeah. … And "
  "why are we worried about that one? Particularly for what group? Pregnant women because they can transmit it to "
  "their baby and it can be fatal.” [part 3, 22:54&ndash;23:26]",
  f"""<p>Lives naturally in <strong>cats</strong>, which harbor oocysts in the gastrointestinal tract and release them
  in feces; acquired by <strong>ingesting raw meats or substances contaminated by cat feces</strong>; most cases
  mild; serious in the immunocompromised (toxoplasma encephalitis). {c17('64')} <strong>Transplacental transmission
  to the fetus</strong> (33% chance) can result in spontaneous abortion, stillbirth, or severe neurological and ocular
  disease in the newborn &mdash; hydrocephalus, intracranial calcifications, chorioretinitis. {c17('65')}</p>
  {fig('l17-s066-toxoplasma-life-cycle.jpg', 370, 693, 'The Toxoplasma gondii life cycle from cat to food animals and humans, including a pregnant woman.', 'The <em>Toxoplasma</em> life cycle.', 17, '66')}"""))

S2.append(item(17, "w17-coccidia", "2.11", "<em>Cryptosporidium</em> and <em>Cyclospora</em>", COLD,
  "“Cryptosporidium. How do you get this one? Contaminated food or water. I wouldn't worry too much about isospora, "
  "but cyclospora you should know.” [part 3, 23:26&ndash;23:45]",
  f"""<p><strong><em>Cryptosporidium</em>:</strong> an intestinal pathogen of mammals, birds and reptiles with tissue
  and oocyst phases; infectious dose as little as 10 organisms; acquired from recreational water or contaminated
  water, ice and foodstuffs; <strong>tolerates chlorine in swimming pools</strong>. {c17('72')} Gastroenteritis;
  chronic persistent diarrhea in AIDS (acquired immunodeficiency syndrome) and other immunocompromised patients; few
  effective drugs; leading cause of recreational waterborne disease. {c17('73')}</p>
  <p><strong><em>Cyclospora cayetanensis</em>:</strong> an emerging protozoan; <strong>oral-fecal transmission, fresh
  produce and water</strong>; oocysts invade the small-intestinal mucosa; watery diarrhea, cramps, bloating, fever;
  diagnosis needs multiple stool samples. {c17('75')} A 2026 outbreak was linked to iceberg lettuce; seen in a fecal
  smear with <strong>acid-fast stain</strong>. {c17('76')}</p>
  {fig('l17-s076-cyclospora-acid-fast.jpg', 761, 552, 'Acid-fast stained fecal smear with pink-red round oocysts among blue debris, labeled oocysts and bacteria.', '<em>Cyclospora</em> oocysts, acid-fast stain.', 17, '76')}
  <h4 class="subsub"><em>Isospora belli</em> <span class="tier tier-light">Light touch</span></h4>
  <p>“I wouldn&rsquo;t worry too much about isospora.” One line: intracellular intestinal parasite with an oocyst
  stage, in fecally contaminated food or drink, mainly in immunocompromised hosts. {c17('74')}</p>"""))
LIGHTS.append((17, "Isospora belli"))

S2.append(item(17, "w17-worm-damage", "2.12", "What damage worms do", COLD,
  "“What kind of symptoms can worm infections give us? Think about their life cycle. … they migrate through your body. "
  "… And so as they are migrating through your tissues, what are they doing? They're feeding on you. They are causing "
  "damage to the tissues … Some of them have direct toxic substances that they produce. … they can cause blockages … "
  "like the tapeworms, they can hook onto your intestines and they can absorb all your nutrients. So you should know "
  "what damage worms can do.” [part 3, 23:54&ndash;25:24]",
  f"""<p>The slide answers her question in three lines. <strong>Pathology arises from worms feeding on and migrating
  through tissues; accumulation of worms in organs, causing blockages; toxic worm secretions.</strong> Effects:
  enlargement and swelling of organs, hemorrhage, weight loss, anemia. {c17('85')}</p>
  <p>The migration she described is life cycle A: larvae hatch and burrow through tissue, may go to the lungs and
  then the pharynx and are swallowed, and complete the cycle in the intestine. {c17('80')} Tapeworms have no mouth;
  nutrients are absorbed through the body, and a scolex grips the intestine. {c17('118')} Defense against worms is
  eosinophils; diagnosis by eosinophilia, serology, and eggs, larvae or worms in feces, sputum, urine, blood or
  tissue. {c17('86')}</p>"""))

S2.append(item(17, "w17-enterobius", "2.13", "<em>Enterobius vermicularis</em>, the pinworm", COLD,
  "“Enterobius vermiculares. What did that do? Which one is that? It's the scourge of the daycare center. That's the "
  "pinworm, right? With the scotch pig test” [part 3, 25:38&ndash;25:58] (“scotch tape test”)",
  f"""<p>Pinworm or seatworm; enterobiasis is the <strong>most common worm disease of children in temperate
  zones</strong> (starred on the slide). Eggs are picked up from surroundings and swallowed; adults develop in the
  intestine; <strong>anal itching</strong> when females emerge to release eggs; self-inoculation is common;
  <strong>tape test</strong>. {c17('94')}</p>
  {fig('l17-s095-pinworm-eggs.jpg', 184, 110, 'Three oval eggs flattened on one side.', 'Pinworm eggs.', 17, '95')}"""))

S2.append(item(17, "w17-trichinella", "2.14", "<em>Trichinella spiralis</em>", COLD,
  "“Trichinellis spiralis. What does that one do? … Where do you get that one? By eating undercooked pork. Because "
  "you are eating the insisted form in the muscle of the pig … And then it goes into your gut, multiplies, and then it "
  "wants to go find some more muscle to insist in. And causes damage to skeletal muscle, but also smooth muscle. Could "
  "go to the cardiac muscle, right?” [part 3, 25:51&ndash;26:34]",
  f"""<p>Life cycle entirely within mammals; life cycle C. <strong>Acquired from eating undercooked pork or bear
  meat.</strong> Larvae migrate from the intestine to blood vessels, <strong>muscle, heart and brain</strong>, where
  they form cysts. First symptoms flulike, diarrhea; second, muscle and joint pain, shortness of breath, pronounced
  eosinophilia; no cure after the larvae have encysted; occasional myocarditis. {c17('101')} Cycle C: a human
  consumes an encysted worm in undercooked meat; gastric passage releases the larva from the cyst. {c17('82')}</p>
  {fig('l17-s101-trichinella-muscle.jpg', 200, 200, 'Muscle section with coiled larvae in cysts.', 'Encysted larvae in muscle.', 17, '101')}
  {aside(17, "L17: Trichinella damages smooth muscle", '''“Smooth muscle” [part 3, 26:31] is not on the slide,
  which names muscle, heart and brain.''')}"""))

S2.append(item(17, "w17-tissue-nematodes", "2.15", "<em>Loa loa</em> and <em>Toxocara</em>", KNOW,
  "“We have the loa loa worm. Loa loa is what kind of worm? It's the eye worm. … So for each of these, you could kind "
  "of chug a little phrase to what they do. I'm not going to ask you a picky detail” [part 3, 26:42&ndash;27:10] … "
  "“The toxic hair, canis and cateye we get from our, from our dogs and cats.” [27:40&ndash;27:48]",
  f"""<p><strong><em>Loa loa</em>, the African eye worm:</strong> spread by the bite of small flies; life cycle D; a
  temperature-sensitive worm that migrates around and under the skin and may enter the eye; pulled from a small hole
  in the conjunctiva. {c17('107')}</p>
  {fig('l17-s107-loa-loa-eye.jpg', 240, 170, 'A thin worm being drawn from the surface of an eye.', 'The eye worm.', 17, '107')}
  <p><strong><em>Toxocara canis</em> and <em>T. cati</em>, dog and cat roundworms:</strong> humans are accidental
  hosts, infected by ingesting eggs from feces or undercooked meat of a transport host; larvae migrate; ocular
  toxocariasis can blind; visceral toxocariasis damages the liver. {c17('108')}</p>
  <div class="pearl"><p>Her own method, “a little phrase to what they do”: pinworm &mdash; daycare, tape test;
  <em>Trichinella</em> &mdash; undercooked pork, cysts in muscle; <em>Loa loa</em> &mdash; eye worm;
  <em>Toxocara</em> &mdash; dogs and cats; <em>Schistosoma</em> &mdash; snail, blood fluke; <em>Opisthorchis</em>
  &mdash; Chinese liver fluke, fish; <em>Taenia</em> &mdash; beef and pork, cysticercosis.</p></div>"""))

S2.append(item(17, "w17-flukes", "2.16", "<em>Schistosoma</em> and <em>Opisthorchis</em>", KNOW,
  "“Schistosoma. This is the one that's schistosomiasis. This is the one with the complex life cycle, where the "
  "alternate host is the snail in the water, okay? It's a blood fluke … That's why we don't put our hands in the water "
  "where the snails live.” [part 3, 27:14&ndash;27:33] … “Apisicorcus sinensis, that's the Chinese liver fluke. This "
  "is why you do not eat fresh water sushi.” [27:48&ndash;27:53]",
  f"""<p><strong>Blood flukes, schistosomes:</strong> life cycle D; adults in humans release eggs into water; the
  miracidium develops in a <strong>freshwater snail</strong> into a cercaria, which <strong>penetrates human
  skin</strong>, matures in the liver; adults migrate to intestine or bladder, feed on blood and shed eggs in urine
  and feces. {c17('112')} Prevention: snail control. {c17('113')}</p>
  {fig('l17-s114-schistosoma-cycle.jpg', 900, 768, 'The Schistosoma life cycle with snails, cercariae penetrating skin and adult worms in veins.', 'The <em>Schistosoma</em> life cycle.', 17, '114')}
  <p><strong><em>Opisthorchis</em> (<em>Clonorchis</em>) <em>sinensis</em>, the Chinese liver fluke:</strong>
  cycles between mammals, snails and fish; <strong>humans are infected by eating inadequately cooked fish</strong>
  containing cercariae; larvae crawl into the bile duct. {c17('116')}</p>"""))

S2.append(item(17, "w17-tapeworms", "2.17", "<em>Taenia</em> and <em>Echinococcus</em>", KNOW,
  "“And then we have our tapeworms. Tenia saginata, tenia solium, we're eating undercooked beef and pork. And solium "
  "can also give you the cysticercosis, little brain worms … And then the echinococcus, which is the little tiny "
  "worm.” [part 3, 28:03&ndash;28:34]",
  f"""<p><strong><em>Taenia saginata</em>, beef tapeworm:</strong> infection from eating raw beef with the encysted
  larva; few symptoms; proglottids in stool. {c17('119')} <strong><em>Taenia solium</em>, pork tapeworm:</strong>
  taeniasis if you ingest contaminated meat; <strong>cysticercosis if you ingest embryonated eggs</strong> &mdash;
  larvae migrate to all tissues and encyst, most damaging in heart, eye or brain (seizures, psychiatric
  disturbances). {c17('121')}</p>
  {fig('l17-s123-cysticercosis-brain-slice.jpg', 762, 481, 'Brain slice with many small cysts.', 'Cysticercosis in the brain.', 17, '123')}
  <p><strong><em>Echinococcus</em>:</strong> tiny tapeworms; cystic echinococcosis (hydatid disease), a 2&ndash;7 mm
  tapeworm of dogs, slowly enlarging cysts in liver and lungs {c17('124')}; acquired from handling infected dogs;
  treatment often surgical removal of the masses. {c17('125')}</p>
  {fig('l17-s125-hydatid-cyst-surgery.jpg', 553, 412, 'A large white cyst exposed at surgery.', 'A hydatid cyst at surgery.', 17, '125')}"""))

S2.append(item(17, "w17-drugs", "2.18", "Why so few drugs for parasites", COLD,
  "“Why don't we have as many drugs for all of these parasites as we do for bacteria? Because they're eukaryotic, and "
  "so we have a lot of a lot of chances for toxic side effects.” [part 3, 28:34&ndash;28:52]",
  f"""<p>Antiprotozoan drugs are <strong>relatively few in comparison with antibacterial agents</strong>; they
  <strong>work against eukaryotic cells</strong>, so there are <strong>toxicity problems and severe side
  effects</strong> (both lines starred on the slide). {c17('14')} Likewise many antihelminthic drugs have toxic side
  effects; they target a worm metabolic process that differs from the human one. {c17('86')}</p>"""))

# --------------------------------------------------------------------------
# Section 3 -- Lecture 18, DNA Viruses (her closing list)
# --------------------------------------------------------------------------
S3 = []

S3.append(item(18, "w18-replication", "3.1", "Animal virus replication versus phage replication", COLD,
  "“And what we talked about today, you should know the difference between animal virus replication and phage virus "
  "replication.” [part 3, 29:00&ndash;29:20]",
  f"""<table>
    <tr><th></th><th>Phage (bacterial virus)</th><th>Animal virus</th></tr>
    <tr><td><strong>Entry</strong></td><td>Adsorption, then penetration: viral lysozyme and the tail pin breach the wall and <strong>inject the DNA</strong> {c18('14')}</td><td><strong>Entire virion engulfed</strong> {c18('22')}</td></tr>
    <tr><td><strong>Uncoating</strong></td><td>Not needed: only the DNA enters</td><td><strong>Required</strong> to release the genetic material (pH of the cytoplasm against the extracellular fluid) {c18('22')}</td></tr>
    <tr><td><strong>Release</strong></td><td>Lytic: viral lysozyme bursts the cell wall {c18('14')}</td><td><strong>Budding</strong>, which may give the envelope {c18('22')}</td></tr>
  </table>
  <p>Phage replication methods: <strong>lytic</strong>, <strong>lysogenic</strong> and <strong>chronic</strong>
  (filamentous phages). {c18('13')} Lytic: adsorption, penetration, replication, assembly, maturation, release.
  {c18('14')} Lysogenic: the viral DNA integrates into the bacterial chromosome as a <strong>prophage</strong>; a shock
  induces a lytic cycle. {c18('15')} Chronic: filamentous phages are extruded without lysis, only slowing host growth.
  {c18('16')}</p>
  {fig('l18-s022-animal-virus-entry.jpg', 502, 600, 'Diagram of an enveloped animal virus attaching to receptors, entering by endocytosis, uncoating, synthesizing parts, assembling and budding out of the cell.', 'Animal virus: engulfed whole, uncoated, released by budding.', 18, '22')}
  {fig('l18-s017-phage-cycles.jpg', 887, 620, 'Diagram of the lytic, lysogenic and chronic phage cycles in bacteria.', 'Lytic, lysogenic and chronic cycles.', 18, '17')}
  <p>Steps for a DNA animal virus (papovavirus): attachment, entry and uncoating, early transcription, biosynthesis
  (DNA replicated), late translation of capsid proteins, maturation, release; note the necessity for uncoating and
  release by budding. {c18('23')} Most DNA viruses are budded off the nucleus. {c18('24')}</p>
  {fig('l18-s023-dna-virus-replication.jpg', 500, 314, 'Seven-step replication cycle of a DNA animal virus from attachment to release.', 'Non-phage DNA virus replication.', 18, '23')}"""))

S3.append(item(18, "w18-structure", "3.2", "Animal virus structure; where the envelope comes from", COLD,
  "“Basic structure of the animal viruses. Where do they get that envelope?” [part 3, 29:20&ndash;29:33]",
  f"""<p>All viruses have a <strong>capsid</strong>, a protein coat enclosing the nucleic acid (helical, icosahedral,
  or complex as in phage); they contain DNA or RNA; animal viruses may have an <strong>envelope</strong> or spikes.
  <strong>The envelope is obtained during budding of the virus through the cell membrane</strong>, and helps evade
  the immune system. {c18('9')} Animal viruses are categorized by nucleic acid, capsid and presence or absence of an
  envelope. {c18('8')}</p>
  {fig('l18-s030-dna-virus-groups.jpg', 459, 600, 'Chart of the DNA virus groups that infect humans: enveloped double-stranded (poxviruses, herpesviruses, hepadnaviruses), nonenveloped double-stranded (adenoviruses, polyomaviruses, papillomaviruses) and nonenveloped single-stranded (parvoviruses).', 'The DNA virus groups that infect humans.', 18, '30')}
  {fig('l18-s010-naked-and-enveloped.jpg', 900, 442, 'Drawings of a naked nucleocapsid virus and an enveloped virus with spikes, matrix, capsid and nucleic acid.', 'Naked nucleocapsid and enveloped viruses.', 18, '10')}"""))

S3.append(item(18, "w18-infections", "3.3", "Acute, persistent chronic and persistent latent infections", COLD,
  "“Viral infections, examples of the acute viral infections. Examples of the persistent chronic viral infections. And "
  "the persistent latent viral infections.” [part 3, 29:33&ndash;29:58]",
  f"""<table>
    <tr><th>Kind</th><th>What happens</th><th>Slide&rsquo;s examples</th></tr>
    <tr><td><strong>Acute</strong></td><td>Rapid course; lytic cycle</td><td>Colds, flu</td></tr>
    <tr><td><strong>Persistent chronic</strong></td><td>Virus detectable in tissue, multiplying slowly; symptoms mild or absent; may integrate into the host chromosome</td><td>HIV, hepatitis B virus</td></tr>
    <tr><td><strong>Persistent latent</strong></td><td>After a lytic cycle the virus goes dormant, generally not detectable, no symptoms; can reactivate as recurrent infection; viral DNA is an <strong>episome</strong> (in the nucleus, not integrated)</td><td>Herpesviruses</td></tr>
  </table>
  <p>{c18('26')} Note that the slides use hepatitis B as the chronic example, although most people infected show
  few symptoms and develop immunity {c18('88')}; it is chronic in the small number who go on to chronic liver
  disease.</p>
  {fig('l18-s027-effects-on-host-cells.jpg', 453, 533, 'Diagram of the possible effects of a viral infection on a host cell: lytic infection, chronic infection, latent infection with recurrence, and transformation.', 'Possible effects of viral infection on host cells (“think about the similarity of these cycles to the phage cycles”).', 18, '27')}"""))

S3.append(item(18, "w18-oncogenic", "3.4", "Oncogenic viruses", COLD,
  "“What is an oncogenic virus, and give an example of that.” [part 3, 29:58&ndash;30:03] … “Oncogenic viruses” "
  "[31:22]",
  f"""<p>Some <strong>persistent viruses are oncogenic</strong>: {c18('28')}</p>
  <table>
    <tr><th>Virus</th><th>Cancer</th></tr>
    <tr><td>Epstein-Barr virus</td><td>Burkitt lymphoma</td></tr>
    <tr><td>Herpesvirus 8</td><td>Kaposi sarcoma</td></tr>
    <tr><td>Hepatitis B virus</td><td>Hepatic carcinoma</td></tr>
    <tr><td>Papillomaviruses</td><td>Cervical and penile cancer</td></tr>
  </table>
  {fig('l18-s076-burkitt-lymphoma.jpg', 377, 401, 'A child with a grossly swollen jaw and cheek.', 'Burkitt lymphoma, the Epstein-Barr virus tumor that swells the jaw (Slide 77).', 18, '76')}
  <p>Adenoviruses are <strong>oncogenic in animals, not in humans</strong> {c18('93')}; polyomaviruses induce tumors in
  experimental animals. {c18('101')}</p>
  {conflict(18, "L18: chart (slide 5) puts 'cervical and penile cancer' on the herpes simplex 2 row; slide 28 gives it to papillomaviruses", '''Her
  chart&rsquo;s herpes simplex 2 row says “Association with Cervical and Penile cancer; often diagnosed with Pap
  smear” {c18('5')}, while the oncogenic list gives cervical and penile cancer to the <strong>papillomaviruses</strong>
  {c18('28')}. Learn the Slide 28 pairing; an exam item will not hinge on the chart row.''')}"""))

S3.append(item(18, "w18-teratogenic", "3.5", "Teratogenic viruses", COLD,
  "“What is a teratogenic virus, what is that?” [part 3, 30:03&ndash;30:11]",
  f"""<p>Several viruses can <strong>cross the placenta</strong>, causing developmental disturbances and permanent
  defects &mdash; <strong>teratogenic</strong>: <strong>rubella</strong> and <strong>cytomegalovirus</strong>.
  {c18('28')} Cytomegalovirus in newborns: enlarged liver and spleen, jaundice, capillary bleeding, microcephaly,
  ocular inflammation; survivors develop neurological sequelae, hearing and visual disturbances. {c18('72')}</p>
  <div class="pearl"><p>Oncogenic causes cancer; teratogenic causes birth defects across the placenta. Other DNA
  viruses on the slides that harm the fetus or newborn: parvovirus B19 (hydrops fetalis) {c18('104')}; herpes of the
  newborn (from the mother before or during birth). {c18('64')}</p></div>"""))

S3.append(item(18, "w18-herpes", "3.6", "The eight human herpesviruses", COLD,
  "“What do all of those delightful little herpes viruses do? 1 through 8, OK, what do each one of them do, are they "
  "associated with?” [part 3, 30:11&ndash;30:25]",
  f"""<p>All herpesviruses show <strong>latency</strong> and cause recurrent infection (viral DNA forms an episome);
  large enveloped icosahedral double-stranded DNA; replicate within the nucleus. {c18('55')}</p>
  <table>
    <tr><th>Virus</th><th>Disease (Slide 57)</th><th>Transmission and other facts</th></tr>
    <tr><td><strong>HSV-1</strong> (herpes simplex 1)</td><td>Fever blisters, cold sores</td><td>Oropharynx, early childhood {c18('58')}; latent in the <strong>trigeminal ganglion</strong> {c18('59')}; also gingivostomatitis, keratitis, whitlow {c18('60')}</td></tr>
    <tr><td><strong>HSV-2</strong> (herpes simplex 2)</td><td>Genital infections</td><td>Ages 14&ndash;29; can spread without visible lesions {c18('58')}; latent in <strong>lumbosacral</strong> ganglia {c18('59')}</td></tr>
    <tr><td><strong>VZV</strong> (varicella zoster virus)</td><td>Chickenpox and shingles</td><td>Item 3.10</td></tr>
    <tr><td><strong>CMV</strong> (cytomegalovirus)</td><td>Infects salivary glands and viscera</td><td>Giant cells with inclusions; saliva, breast milk, urine, semen, transplants {c18('71')}; teratogenic {c18('28')}</td></tr>
    <tr><td><strong>EBV</strong> (Epstein-Barr virus)</td><td>Lymphoid tissue &mdash; infectious mononucleosis</td><td>Saliva (“kissing disease”) {c18('75')}; Burkitt lymphoma, nasopharyngeal carcinoma {c18('77')}</td></tr>
    <tr><td><strong>HHV-6</strong> (human herpesvirus 6)</td><td>Roseola</td><td>Babies 2&ndash;12 months: fever, then a faint rash {c18('81')}</td></tr>
    <tr><td><strong>HHV-7</strong> (human herpesvirus 7)</td><td>Roseola</td><td>Closely related to HHV-6 {c18('83')}</td></tr>
    <tr><td><strong>HHV-8</strong> (human herpesvirus 8)</td><td>Kaposi sarcoma</td><td>Item 3.11</td></tr>
  </table>
  <p>{c18('57')}</p>
  {fig('l18-s056-herpesvirus.jpg', 810, 436, 'Drawing and electron micrograph of a herpesvirus with glycoprotein spikes, envelope, tegument, capsid and DNA core.', 'Herpesvirus structure.', 18, '56')}
  {fig('l18-s061-herpetic-whitlow.jpg', 852, 415, 'A finger with a painful vesicular lesion.', 'Herpetic whitlow (herpes simplex 1 or 2 through a break in the skin).', 18, '61')}
  {fig('l18-s082-roseola.jpg', 467, 512, 'A baby with a faint rash on the trunk.', 'Roseola infantum (human herpesvirus 6).', 18, '82')}"""))

S3.append(item(18, "w18-pox", "3.7", "What is unusual about poxvirus reproduction", COLD,
  "“What's unusual about reproduction in the pox viruses? They're the great big guys. They reproduce in the cytoplasm "
  "and not the nucleus.” [part 3, 30:25&ndash;30:38]",
  f"""<p>Poxviruses: the <strong>largest and most complex animal viruses</strong>, the largest genome, double-stranded
  DNA, and they <strong>multiply in the cytoplasm in factory areas</strong>; eruptive pustules (pocks) that scar.
  {c18('32')} Compare: most DNA viruses are budded off the nucleus {c18('24')}, and herpesviruses replicate within the
  nucleus. {c18('55')}</p>
  {fig('l18-s033-poxvirus.jpg', 796, 481, 'Cutaway drawing of a poxvirus with surface tubules, envelope, outer membrane, core membrane, lateral bodies and a 100 nanometer scale bar.', 'Poxviruses are larger and more complex than other viruses.', 18, '33')}"""))

S3.append(item(18, "w18-variola", "3.8", "Variola, smallpox", KNOW,
  "“We talked about variola, the small pox virus, which is, theoretically speaking, the first virus to be eliminated "
  "by vaccination.” [part 3, 30:41&ndash;30:54]",
  f"""<p>Her chart: smallpox; transmission inhalation, direct contact, fomites; fever, malaise, prostration, rash,
  possible toxemia, shock; vaccine <strong>yes &mdash; with vaccinia</strong>; “<strong>first disease to be eliminated
  by vaccine</strong>; no more routine vaccination except for front line”. {c18('4')} Transmission: airborne saliva,
  material from pustules or scabs, fomites; the early rash (spots on tongue and mouth) is the <strong>stage of greatest
  contagion</strong>. {c18('40')} Contagious until all scabs have fallen off. {c18('41')} Prevention: vaccination with
  vaccinia virus, not routinely given since 1972. {c18('43')} Declared eradicated by the World Health Organization in
  1980. {c18('45')}</p>
  {fig('l18-s045-smallpox.jpg', 900, 409, 'A child and an arm covered with smallpox pustules.', 'Smallpox infections.', 18, '45')}"""))

S3.append(item(18, "w18-mpox", "3.9", "Mpox and its vaccine", KNOW,
  "“We talked about the mpox virus, which is something that they're trying to wage war on right now, and even giving "
  "you, where do I find a vaccine against this one?” [part 3, 30:54&ndash;31:02]",
  f"""<p>Mpox (monkeypox): the virus enters through broken skin, the respiratory tract or mucous membranes, by contact
  with body fluids or fomites; fever, aches, chills, <strong>swollen lymph nodes</strong>; 1&ndash;3 days after fever a
  rash starting on the face, through macules, papules, vesicles, pustules and scabs; a 2&ndash;4 week illness.
  {c18('48')} <strong>Vaccination available</strong>, with a CDC (Centers for Disease Control and Prevention) vaccine
  locator tool: <strong>JYNNEOS</strong>, a 2-dose series 28 days apart; <strong>ACAM2000</strong>, approved against
  smallpox and made available to prevent monkeypox. {c18('52')} Jynneos is a smallpox and monkeypox vaccine.
  {c18('44')}</p>
  {conflict(18, "L18: JYNNEOS 'became available April 2024' (chart, slide 4) vs 'approved September 24, 2019' (slide 44)", '''The
  chart says JYNNEOS “became available April 2024” {c18('4')}; Slide 44 says approved September 24, 2019. Know the
  vaccine&rsquo;s name and dosing, not the date.''')}"""))

S3.append(item(18, "w18-vzv", "3.10", "Varicella zoster: when you are contagious", COLD,
  "“Varicella zoster, the chicken pox shingles virus, when you are contagious with that one.” [part 3, 31:22&ndash;31:40]",
  f"""<p>Varicella zoster virus causes chickenpox and shingles; humans the only natural host; transmitted by respiratory
  droplets and contact with fluid from active lesions; <strong>most infectious 24&ndash;48 hours prior to the
  development of lesions</strong>; the virus enters neurons and stays latent. {c18('68')} Reactivation gives shingles,
  vesicles along a dermatome, more common in older patients; <strong>shingles patients can infect unvaccinated people,
  particularly children, who get chickenpox, not shingles</strong>; live attenuated vaccine for chickenpox and
  shingles. {c18('69')}</p>
  {fig('l18-s070-varicella-zoster.jpg', 900, 320, 'Chickenpox rash on a child, the virus reactivating in a ganglion and traveling down a sensory nerve, and a shingles rash along one dermatome.', 'The relationship between varicella and zoster.', 18, '70')}"""))

S3.append(item(18, "w18-kaposi", "3.11", "The herpesvirus of Kaposi sarcoma", COLD,
  "“Which herpes virus is associated with Kaposi sarcoma?” [part 3, 31:48&ndash;31:58]",
  f"""<p><strong>Human herpesvirus 8</strong>, the Kaposi sarcoma-associated virus, is linked with the common tumor of
  AIDS patients; also possibly multiple myeloma, primary effusion lymphoma and some forms of Castleman disease. Kaposi
  sarcoma: small, painless, discolored lumps on the skin that may disseminate to internal organs. {c18('83')} Chart:
  saliva, sexual contact, blood transfusion, organ transplant; no vaccine. {c18('6')}</p>
  {fig('l18-s084-kaposi-sarcoma.jpg', 414, 150, 'A patient with many small discolored skin lumps.', 'Kaposi sarcoma lesions.', 18, '84')}"""))


def chart():
    rows = [
        ("Variola", "Smallpox", "Inhalation, direct contact, fomites", "Fever, malaise, prostration, rash, possible toxemia, shock", "Yes &mdash; with vaccinia", "First disease to be eliminated by vaccine; no more routine vaccination except for front line"),
        ("Molluscum contagiosum", "Molluscum contagiosum", "Direct contact and fomites", "Small, smooth waxy macules on genitals and thighs", "No", "Treatment typically by removal of individual lesions"),
        ("Monkeypox", "Monkeypox", "Contact with infected animals or humans", "Skin pocks, fever, swollen lymph nodes", "Yes &mdash; JYNNEOS", "Major outbreak US 2022&ndash;2023"),
        ("Vaccinia", "Cowpox", "Contact with infected animals (rarely humans)", "Skin pocks typically on hands", "Yes &mdash; used in Europe for animals", "Also found in rodents, cats, zoo and circus animals"),
        ("Herpes simplex 1", "Fever blisters, cold sores", "Direct contact", "Lesions near lips and genitals, herpetic gingivostomatitis, herpetic keratitis, encephalitis occasionally in neonates", "No, but candidate vaccines in trials", ""),
        ("Herpes simplex 2", "Genital herpes", "Direct contact", "Anorexia, fever, bilateral groin swelling and tenderness; clusters of sensitive vesicles on genitalia, perineum and buttocks; urethritis, painful urination, cervicitis, itching; vesicles ulcerate", "No, research ongoing", "See the flag in item 3.4"),
        ("Herpes simplex 1 and 2", "Herpetic whitlow; herpes of the newborn", "Direct contact; mother to child", "Pain and swelling of a finger or thumb, blisters, red streaks; lesions on mouth, skin, eyes, central nervous system where potentially fatal", "No", ""),
        ("Varicella zoster", "Chickenpox, shingles", "Respiratory droplets and contact with fluid from active skin lesions", "Filled vesicles, malaise, fever; reactivation as shingles, painful vesicles along a dermatome", "Yes, for both", "Shingles is infectious to those never immunized &mdash; manifests as chickenpox"),
        ("Cytomegalovirus", "Retinitis, encephalitis, intestinal tract inflammation", "Direct contact with infectious body fluids (saliva, blood, mucus, tears, breast milk, urine, semen, cervical secretions) or tissues", "Blind spots; encephalitis; enlarged liver and spleen, jaundice, capillary bleeding; fetal microcephaly; survivors with neurological, hearing and visual damage", "None currently; several in trials", "Severe in neonates, fetuses, transplant patients, HIV and other immunocompromised hosts; owl&rsquo;s eye inclusion"),
        ("Epstein-Barr virus", "Infectious mononucleosis; Burkitt lymphoma; nasopharyngeal carcinoma; chronic fatigue syndrome (possible link)", "Direct oral contact or fomites contaminated with saliva", "Sore throat, high fever, cervical lymphadenopathy, splenomegaly; Burkitt: swollen nodes, abdominal pain, night sweats; nasopharyngeal: neck lump, hearing loss, blocked nose", "No preventive vaccine; therapeutic vaccines in trials for its cancers", "Burkitt primarily African boys 5&ndash;7; nasopharyngeal cancer adults 30&ndash;60, family history, salt-cured foods"),
        ("Human herpesvirus 6", "Roseola", "Contact with saliva", "Acute febrile disease followed by rash", "None", "Possible connection with multiple sclerosis and cancers"),
        ("Human herpesvirus 7", "Roseola", "Contact with saliva", "Acute febrile disease followed by rash", "None", "Possible connection with multiple sclerosis and cancers"),
        ("Human herpesvirus 8", "Kaposi sarcoma", "Saliva, sexual contact, blood transfusion, organ transplant", "Small painless discolored skin lumps; may affect internal organs", "None", "Castleman disease, primary effusion lymphoma"),
        ("Hepatitis B", "Hepatitis B", "Contact with blood or serum, sexual contact", "Malaise, fever, chills, anorexia, abdominal discomfort, diarrhea, jaundice, rash, arthritis", "Yes", "Cirrhosis and hepatic cancer; great risk to health care workers from a very low infective dose"),
        ("Adenovirus", "50+ types: common cold, pharyngitis, conjunctivitis, cystitis, infantile gastroenteritis; some strains hepatitis in young children", "Droplets from respiratory and ocular secretions; ingestion", "Upper respiratory symptoms, congestion, cough, fever; gastrointestinal symptoms; hepatitis", "Types 4 and 7, for military in training", ""),
        ("Human papillomavirus", "Warts and genital warts", "Direct contact including sexual, or fomites", "Tiny flat bumps to branching cauliflower-like masses", "Vaccines available for genital warts", "Nine strains raise the risk of reproductive system cancers"),
        ("Polyomaviruses (JC, BK)", "JC: progressive multifocal leukoencephalopathy; BK: interstitial nephritis", "Body fluids, contaminated food or water; JC early childhood, BK adolescence", "JC: demyelination, progressive neurological symptoms; BK: after renal transplant, bloody urine", "None for humans", "Most prevalent in the immunosuppressed"),
        ("Parvovirus B19", "Fifth disease; hydrops fetalis; polyarthropathy; cessation of red cell production", "Droplet infection", "Slapped-face rash, low-grade fever; fatal fetal anemia from maternal transmission; massive joint swelling; anemia", "", ""),
    ]
    out = ['<div class="table-wrap"><table class="chart">',
           '  <tr><th>Virus</th><th>Disease</th><th>Transmission</th><th>Clinical manifestations</th>'
           '<th>Vaccine</th><th>Other</th></tr>']
    for r in rows:
        out.append('  <tr><td><strong>%s</strong></td>' % r[0] + "".join("<td>%s</td>" % x for x in r[1:]) + "</tr>")
    out.append("</table></div>")
    return "\n  ".join(out)


S3.append(item(18, "w18-chart", "3.12", "Her chart: the other DNA viruses", COLD,
  "“And again, for each of these, I've given you this chart to help clue you in on. If you can associate what the "
  "viruses are and what they do, you should be OK.” [part 3, 31:58&ndash;32:07]",
  f"""<p>The chart is Slides 4&ndash;7, under the instruction “For each of the viruses on the following tables, review
  disease states, modes of transmission, clinical manifestations, whether vaccines are available and any other
  pertinent information listed.” It is rebuilt here as text, row for row (spelling corrected). {c18('4&ndash;7')}</p>
  {chart()}
  <p>The viruses on it she did not name in the review get their own line from the slides. One of them she had
  flagged earlier that afternoon, in the lecture itself:</p>
  <div class="asked"><span class="asked-label">In the lecture</span><p>“Three principal viruses associated with
  hepatitis, hepatitis B, which is the DNA virus, you need to know that one, and then Dr. Fair will talk to you about
  hepatitis A and C next week because they are RNA viruses.” [part 2, 35:10&ndash;35:25]</p></div>
  <ul>
    <li><strong>Hepatitis B</strong> (enveloped, unusual partly double- and partly single-stranded genome, liver
    tropism {c18('86')}): multiplies exclusively in the liver, seeding the blood &mdash; chronic; minute amounts of
    blood transmit it, also sexual; raises the risk of hepatocellular carcinoma {c18('87')}; vaccine from yeast-cloned
    surface antigen, 3 doses; HBIG (hepatitis B immune globulin) for the exposed. {c18('91')}</li>
    <li><strong>Adenovirus</strong>: nonenveloped double-stranded DNA, acute infection; respiratory and ocular
    secretions; colds, pharyngitis, conjunctivitis, hemorrhagic cystitis, infantile gastroenteritis {c18('93')};
    type 41 is associated with hepatitis in children 1&ndash;6; oral vaccine for types 4 and 7 in the military.
    {c18('94')} (The slide calls that vaccine &ldquo;inactivated&rdquo;; the current military adenovirus vaccine is a
    live oral vaccine. Answer from the slide if asked.)</li>
    <li><strong>Human papillomavirus</strong>: warts (common, plantar, genital &mdash; the most common sexually
    transmitted disease in the United States) {c18('97')}; nine types raise reproductive cancer risk; Pap smear;
    vaccines Gardasil and Cervarix. {c18('99')}</li>
    <li><strong>Polyomaviruses</strong>: JC virus causes progressive multifocal leukoencephalopathy, destruction of
    myelin-producing cells in the immunosuppressed; BK virus lies dormant in the kidney and causes hemorrhagic
    cystitis and nephritis after renal transplant. {c18('102')}</li>
    <li><strong>Parvovirus B19</strong>: nonenveloped single-stranded DNA {c18('103')}; erythema infectiosum (fifth
    disease), fever and rash on the cheeks; hydrops fetalis if a pregnant woman passes it to the fetus. {c18('104')}</li>
    <li><strong>Molluscum contagiosum</strong>: direct contact and fomites; in the United States most commonly a
    sexually transmitted disease; small, smooth waxy lesions. {c18('46')}</li>
    <li><strong>Cowpox</strong>: rare in humans, usually on the hands; rodents are the main reservoir. {c18('53')}</li>
  </ul>
  {fig('l18-s105-fifth-disease.jpg', 691, 452, 'A child with a bright red rash on the cheek.', 'The “slapped face” rash of fifth disease (parvovirus B19).', 18, '105')}"""))


# --------------------------------------------------------------------------
# Page assembly
# --------------------------------------------------------------------------
def toc():
    out = ['<nav class="toc">', '  <h2>Contents</h2>',
           '  <a class="top-link" href="#how-to-use">How to use this page</a>']
    heads = {14: ("lec14", "1 &middot; Gram-Negative Bacilli"),
             17: ("lec17", "2 &middot; Parasites"),
             18: ("lec18", "3 &middot; DNA Viruses")}
    last = None
    for lec, anchor, num, title, _cls in ITEMS:
        if lec != last:
            out.append('  <a class="top-link" href="#%s">%s</a>' % heads[lec])
            last = lec
        out.append('  <a href="#%s">%s %s</a>' % (anchor, num, re.sub(r"<[^>]+>", "", title)))
    out.append('  <a class="top-link" href="#closing">What she said about the exam</a>')
    out.append('</nav>')
    return "\n".join(out)


HOWTO = """<h2 id="how-to-use">How to use this page</h2>
<p>This is not a second study guide. It is a record of what Professor Webster told the class to study for Exam 3, on
13 November 2026, at the end of the DNA Viruses lecture. %(OPENING)s She walked her three Exam 3 lectures in order: the
Gram-negative bacilli organism by organism, the parasites organism by organism, and DNA viruses as a closing list of
what to know.</p>
<p>Each item carries her words and then the answer from the slides, cited to the slide. The time in brackets says
where her words are in the recording: [part 3, 7:31] is seven and a half minutes into part 3. <strong>Her words come
from one transcript</strong> (ours; no Notability transcript exists for this recording), so a misheard word is
possible and is corrected in brackets where it matters. The recording only decides the weighting. Every fact comes
from the slides &mdash; the visible text and pictures, never the speaker notes &mdash; and where what she said differs
from a slide, the page says so and teaches the slide.</p>
<table>
  <tr><th>Tier</th><th>What it means</th></tr>
  <tr><td><span class="tier tier-cold">Know cold</span></td>
      <td>She asked the class to answer it, drilled it, or said &ldquo;need to know&rdquo; or &ldquo;should know&rdquo;</td></tr>
  <tr><td><span class="tier tier-know">Know it</span></td>
      <td>She walked it without singling it out</td></tr>
  <tr><td><span class="tier tier-light">Light touch</span></td>
      <td>She said not to worry about it</td></tr>
</table>
<div class="prof-flag"><span class="prof-flag-label">&#9733; Pictures</span>
  <p>For the parasites she said it twice: &ldquo;if I showed you a picture of them, it&rsquo;s possible that you could
  need to identify the picture&rdquo; [part 3, 15:10&ndash;15:16], and at the end, &ldquo;if I give you a picture, be
  able to recognize it&rdquo; [part 3, 28:52]. The deck&rsquo;s pictures are on this page next to each organism; the
  one she named directly is the <strong>ring form inside red blood cells</strong> (item 2.9), and she reminded the class
  of the <em>Trichomonas</em> picture (item 2.5).</p>
</div>
<div class="callout">
  <p><strong>Scope.</strong> She reviewed <strong>only the three lectures she taught</strong> &mdash; Lecture 14
  (Gram-Negative Bacilli of Medical Importance), Lecture 17 (Parasites of Medical Importance) and Lecture 18 (DNA
  Viruses of Medical Importance). Exam 3, on <strong>Wednesday 2 December 2026</strong>, covers <strong>Lectures
  14&ndash;19</strong>, so Dr. Fair&rsquo;s lectures are examinable and are <em>not</em> on this page:
  <strong>Lecture 15</strong> (Fungi of Medical Importance), <strong>Lecture 16</strong> (Food Safety) and
  <strong>Lecture 19</strong> (RNA Viruses, 20 November). Use the full <a href="micro-exam-3-study-guide.html">Exam 3
  study guide</a> and the <a href="micro-exam-3-cram-sheet.html">cram sheet</a> for those.</p>
  <p><strong>Parts of her lectures she did not mention are still on the syllabus list:</strong> in Lecture 17, the
  intestinal roundworms <em>Ascaris</em>, <em>Trichuris</em>, the hookworm <em>Necator</em> and
  <em>Strongyloides</em>, the rat lungworm <em>Angiostrongylus</em>, the filarial worms <em>Wuchereria</em> and
  <em>Onchocerca</em>, and the flukes <em>Fasciola</em> and <em>Paragonimus</em>. In Lecture 18 she named the
  herpesviruses and poxviruses and left the rest to her chart (item 3.12). For Lecture 14 she gave diseases and
  identifying features; treatment and prevention she mostly did not mention.</p>
</div>
<p class="obj-map"><strong>Lecture numbering.</strong> The site and the class calendar call the parasites lecture
Lecture 17, and so does this page; its deck file is named &ldquo;Lecture 16 Dr. Webster Parasites of Medical
Importance.pptx&rdquo;. Slide numbers are that file&rsquo;s.</p>
%(DIFFERS)s"""

CLOSING = """<h2 id="closing">What she said about the exam</h2>
<p><strong>The four <em>E. coli</em> types are the surest question.</strong> &ldquo;You need to know all four types and
what they do&rdquo; and &ldquo;there&rsquo;s multiple questions because it&rsquo;s important&rdquo; [part 3,
7:41&ndash;8:51] are the most direct statements about the exam she made.</p>
<p><strong>Parasites: identity, source, and the picture.</strong> &ldquo;I&rsquo;m not going to ask you a picky
detail&rdquo; [part 3, 27:08] &mdash; know each organism by &ldquo;a little phrase to what they do&rdquo;: its vector or
source, its disease, and what it looks like.</p>
<p><strong>DNA viruses: the list, then the chart.</strong> She taught it that afternoon and closed with a list of what to
know &mdash; replication, structure and the envelope, the three kinds of infection, oncogenic and teratogenic viruses,
the eight herpesviruses, poxviruses, smallpox and mpox, varicella zoster&rsquo;s contagious period, Kaposi sarcoma
&mdash; and pointed to her chart for the rest: &ldquo;If you can associate what the viruses are and what they do, you
should be OK.&rdquo;</p>
<p><strong>The review was one-sided by design.</strong> It says nothing about the weight of Dr. Fair&rsquo;s Lectures
15, 16 and 19 on the exam.</p>
<div class="callout">
  <p><strong>Next steps:</strong> the <a href="micro-exam-3-study-guide.html">full Exam 3 study guide</a> covers the
  whole block, and the <a href="micro-exam-3-cram-sheet.html">cram sheet</a> condenses it. To test yourself on exactly
  this review, the two <a href="micro-exam-3-webster-review-master-exam-1.html">Webster Review master exams</a>
  (<a href="micro-exam-3-webster-review-master-exam-2.html">Exam 2</a>), 60 questions each, give every item above a
  question in each exam, with extra ones on the Know cold items and picture questions on the parasites.</p>
</div>"""

# The review begins near the end of recording part 2 (56:10 long): "Do you want to break before I start your review,
# or do you want me to just plunge into the review? ... I will plunge. If you want to get out where you have your
# learning objectives, we're going to review." [part 2, 55:10-55:18]; part 3 then opens on the Lecture 14 objectives
# ("this is so general") and the organisms.
OPENING = ("It begins in the last minute of part 2 of that day&rsquo;s recording &mdash; &ldquo;Do you want to break "
           "before I start your review, or do you want me to just plunge into the review? &hellip; I will plunge. If you "
           "want to get out where you have your learning objectives, we&rsquo;re going to review&rdquo; [part 2, "
           "55:10&ndash;55:18] &mdash; and runs through all of part 3 (32 minutes): about 15 minutes on Lecture 14, 14 on "
           "Lecture 17 and 3 on Lecture 18.")

EXTRA_CSS = """
  .tier{
    display:inline-block;vertical-align:middle;margin-left:8px;
    font-size:.62rem;font-weight:700;letter-spacing:.4px;text-transform:uppercase;
    padding:3px 9px;border-radius:999px;border:1px solid;white-space:nowrap;
  }
  .tier-cold{background:#fdecec;color:#8f2020;border-color:#e0a5a5;}
  .tier-know{background:#eaf3ec;color:#1f4d2b;border-color:#a8c9b3;}
  .tier-light{background:#f1efe9;color:#6a6152;border-color:#cfc7b6;}
  :root[data-theme="dark"] .tier-cold{background:#3a1717;color:#f2b8b8;border-color:#7d3636;}
  :root[data-theme="dark"] .tier-know{background:#16301d;color:#a6d9b5;border-color:#3c6a4b;}
  :root[data-theme="dark"] .tier-light{background:#2a2721;color:#cdc4b2;border-color:#554e3f;}
  .asked{
    border-left:3px solid var(--accent);background:#f2f5f2;
    padding:10px 14px 10px 16px;margin:10px 0 14px;border-radius:0 8px 8px 0;
  }
  .asked-label{
    display:block;font-size:.66rem;font-weight:700;letter-spacing:.5px;
    text-transform:uppercase;color:var(--accent);margin-bottom:4px;
  }
  .asked p{margin:0;font-style:italic;color:#3f4a42;}
  :root[data-theme="dark"] .asked{background:#18211b;border-left-color:#a6d9b5;}
  :root[data-theme="dark"] .asked-label{color:#a6d9b5;}
  :root[data-theme="dark"] .asked p{color:#c8d3cb;}
  .prof-flag{
    border:2px solid #d4a017;border-radius:10px;padding:16px 14px 6px;
    margin:22px 0 14px;position:relative;background:#fffdf5;
  }
  .prof-flag-label{
    position:absolute;top:-13px;left:14px;background:#fef3d4;color:#8a6205;
    font-size:.72rem;font-weight:700;padding:2px 10px;border-radius:8px;
    border:1px solid #d4a017;letter-spacing:.3px;
  }
  .prof-flag table{margin:6px 0 8px;}
  .prof-flag .callout,.prof-flag .pearl{margin-bottom:10px;}
  mark.prof-highlight{
    background:#fef3d4;color:#3a2c05;padding:0 3px;border-radius:3px;
    box-shadow:inset 0 0 0 1px #e8c766;
  }
  :root[data-theme="dark"] .prof-flag{background:#241f10;border-color:#a8801a;}
  :root[data-theme="dark"] .prof-flag-label{
    background:#3a2f12;color:#f0d98a;border-color:#a8801a;
  }
  :root[data-theme="dark"] mark.prof-highlight{
    background:#4a3a12;color:#f7ecc8;box-shadow:inset 0 0 0 1px #7a6220;
  }
  h4.subsub{margin:16px 0 6px;font-size:1rem;}
  .obj-map{font-size:.84rem;color:var(--soft);margin:-2px 0 10px;}
  span.src{color:var(--soft);font-size:.88em;}
  .table-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:10px 0 14px;}
  table.chart{font-size:.84rem;min-width:760px;}
"""


DIFFERS_LIST = [
    ("w14-pseudomonas", "1.1", "<em>Pseudomonas</em> has a <strong>grapelike</strong> odor; &ldquo;rotten&rdquo; is not on the slide."),
    ("w14-plague", "1.14", "Plague: the septicemic form is the slide&rsquo;s <strong>black plague</strong>; pneumonic plague is <strong>highly contagious by aerosol</strong> (caught from humans rarely)."),
    ("w14-endotoxin", "1.16", "Endotoxin is released on lysis <em>and</em> as the cells grow and divide, not only when they die."),
    ("w17-naegleria", "2.2", "<em>Acanthamoeba</em> encephalitis has a <strong>longer progression</strong>; the slide gives no incubation time."),
    ("w17-cruzi", "2.7", "Chagas disease&rsquo;s vector is the <strong>reduviid bug (kissing bug)</strong>."),
    ("w17-leishmania", "2.8", "<em>Leishmania</em> is carried by female <strong>sand flies</strong>, not fleas."),
    ("w17-plasmodium", "2.9", "<em>Plasmodium</em> <strong>does</strong> have a trophozoite: the ring inside the red cell is the ring trophozoite, and it is how malaria is diagnosed."),
]


def differs_box():
    n = sum(1 for _l, k, _s in FLAGS if k == "slide wins")
    assert n == len(DIFFERS_LIST) + 1, "differs() calls (%d) vs DIFFERS_LIST (%d): plague has two" % (n, len(DIFFERS_LIST))
    lis = "\n".join('    <li><a href="#%s">%s</a> %s</li>' % d for d in DIFFERS_LIST)
    return ('<div class="prof-flag"><span class="prof-flag-label">&#9733; Where her words and the slides differ</span>\n'
            '  <p>She was reviewing from memory at speed. In each of these the slide wins, and the item explains:</p>\n'
            '  <ul>\n' + lis + '\n  </ul>\n</div>')


def build():
    donor = open(DONOR, encoding="utf-8").read()
    old_title = "<title>Microbiology &middot; Exam 3 &mdash; Study Guide</title>"
    new_title = "<title>Microbiology &middot; Exam 3 &mdash; Professor Webster&rsquo;s Review</title>"
    head_end = donor.index("</style>")
    head = donor[:head_end]
    assert old_title in head, "donor title changed; update the replacement"
    head = head.replace(old_title, new_title)
    head_tail = donor[head_end + len("</style>"):donor.index("</head>")]
    head = head + EXTRA_CSS + "</style>" + head_tail + "</head>"

    body_start = donor.index("<body")
    header_start = donor.index('<header class="top">')
    chrome = donor[body_start:header_start]

    assert donor.count('<footer class="guide-foot"') == 1, "donor has != 1 guide footer"
    assert donor.count("</main>") == 1, "donor has != 1 </main>"
    foot_start = donor.index('<footer class="guide-foot"')
    foot_end = donor.index("</footer>", foot_start) + len("</footer>")
    footer_el = donor[foot_start:foot_end]
    tail = donor[donor.index("</main>"):]
    dfoot = "Built from your PAJ 5200 lecture decks"
    assert dfoot in footer_el, "donor footer text changed; update the replacement"
    footer_el = footer_el.replace(dfoot, "Built from Professor Webster&rsquo;s Exam 3 review and her three lecture decks")
    footer = footer_el + "\n" + tail

    header = (
        '<header class="top">\n'
        '  <h1>Microbiology &middot; Exam 3 &mdash; Professor Webster&rsquo;s Review</h1>\n'
        '  <p>PAJ 5200 Microbiology &middot; Class of 2028</p>\n'
        '  <p>What she told the class to study on 13 November 2026 &middot; covers Lectures 14, 17 and 18 &mdash; the '
        'three she taught &middot; every answer cited to its slide &middot; Exam 3 is on Wednesday 2 December 2026</p>\n'
        '</header>\n')

    body = ['<div class="layout wrap" data-readable>', toc(), '<main>',
            HOWTO % {"OPENING": OPENING, "DIFFERS": differs_box()}]
    body.append('<h2 id="lec14">1 &middot; Lecture 14 &mdash; Gram-Negative Bacilli of Medical Importance</h2>')
    body.append(iobox("Instructional objectives &mdash; Gram Negative Bacilli of Medical Importance", IO14))
    body.append('<p>She set the objectives aside &mdash; &ldquo;of course this is so general, it&rsquo;s not going to be '
                'any use for us&rdquo; [part 3, 0:00&ndash;0:05] &mdash; and went organism by organism, in the deck&rsquo;s '
                'order, asking the class for most answers. Every '
                'item answers <strong>Objective 1</strong> for its organism and, where transmission is given, '
                '<strong>Objective 2</strong>.</p>')
    body.extend(S1)
    body.append('<h2 id="lec17">2 &middot; Lecture 17 &mdash; Parasites of Medical Importance</h2>')
    body.append(iobox("Instructional objectives &mdash; Parasites of Medical Importance", IO17))
    body.append('<p>Organism by organism again, protozoa then worms, with the picture warning at the start. The '
                'pictures beside each organism are the deck&rsquo;s.</p>')
    body.extend(S2)
    body.append('<h2 id="lec18">3 &middot; Lecture 18 &mdash; DNA Viruses of Medical Importance</h2>')
    body.append(iobox("Instructional objectives &mdash; DNA Viruses that Infect Humans", IO18))
    body.append('<p>She had taught this lecture that afternoon, so the review is a list of what to know [part 3, '
                '29:00&ndash;32:07], which follows the objectives: replication (Objective 1), the three kinds of '
                'infection (Objective 2), oncogenic and teratogenic viruses (Objective 3), and the viruses themselves '
                '(Objectives 4 and 5). One item per thing she listed.</p>')
    body.extend(S3)
    body.append(CLOSING)

    html = head + "\n" + chrome + header + "\n".join(body) + "\n" + footer
    html = re.sub(r'\s*<link rel="alternate"[^>]*\.docx"[^>]*>', "", html)
    html = re.sub(r'(<span class="src">[^<]*?)\.</span>(?=[;,).:]|\s+[a-z])', r'\1</span>', html)
    open(OUT, "w", encoding="utf-8").write(html)

    by = {}
    for lec, _a, _n, _t, cls in ITEMS:
        by.setdefault(lec, {"cold": 0, "know": 0, "light": 0})[cls] += 1
    tot = {t: sum(v[t] for v in by.values()) for t in ("cold", "know", "light")}
    print("wrote %s (%d KB)" % (os.path.basename(OUT), len(html) // 1024))
    print("  items: %d  |  cold %d / know %d / light %d" % (len(ITEMS), tot["cold"], tot["know"], tot["light"]))
    for lec in sorted(by):
        v = by[lec]
        print("    Lecture %-2d  %2d items  |  cold %d / know %d / light %d"
              % (lec, sum(v.values()), v["cold"], v["know"], v["light"]))
    print("  light-touch: %d  %s" % (len(LIGHTS), [w for _l, w in LIGHTS]))
    print("  figures: %d   slide citations: %d" % (html.count('<figure class="fig">'), html.count('class="src"')))
    kinds = {}
    for _l, k, _s in FLAGS:
        kinds[k] = kinds.get(k, 0) + 1
    print("  flags: %d  |  %s" % (len(FLAGS), ", ".join("%s %d" % kv for kv in sorted(kinds.items()))))
    for lec, k, s in FLAGS:
        print("    [%s] %s" % (k, s))

    for probe in ("data-audio-dir", "<script>alert", "Lecture 16, Slide", 'rel="alternate"', "Study Guide</title>"):
        assert probe not in html, "unexpected %r in output" % probe
    assert html.count("<main>") == 1 and html.count("</main>") == 1
    assert html.count('<footer class="guide-foot"') == 1
    assert html.index('id="closing"') < html.index('<footer class="guide-foot"') < html.index("</main>")
    for lec in (14, 17, 18):
        assert "Lecture %d, Slide" % lec in html, "no Lecture %d citations" % lec
    for m in re.findall(r'src="(micro-exam-3-study-guide-images/[^"]+)"', html):
        assert os.path.exists(os.path.join(os.path.dirname(OUT), m)), "missing image " + m
    stamps = re.findall(r"\[part (\d), ([0-9:–&ndash;]+)\]", html)
    assert len(stamps) > 40, "timestamp pattern matched only %d stamps" % len(stamps)
    for part, stamp in stamps:
        assert int(part) in PART_LEN, "bad part %s" % part
        for mm, ss in re.findall(r"(\d+):(\d\d)", stamp):
            assert int(mm) * 60 + int(ss) <= PART_LEN[int(part)], "part %s timestamp too late: %s" % (part, stamp)
    print("  timestamps checked: %d" % len(stamps))
    for a in set(re.findall(r'href="#([^"]+)"', html)):
        assert ('id="%s"' % a) in html, "dangling in-page link #%s" % a


if __name__ == "__main__":
    build()
