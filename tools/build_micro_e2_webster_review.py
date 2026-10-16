#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Microbiology Exam 2 review guide from Professor Webster's own review.

On 16 October 2026 Professor Webster spent the last twenty minutes of the
Epidemiology lecture reviewing Exam 2 ("This is for the exam" [part 4, 0:00]).
The review is part 4 of that day's recording (20:33). She walked the three
lectures SHE taught, in order:

  * Lecture 7, Disorders in Immunity -- objective by objective
    (0:00-12:17);
  * Lecture 10, Gram-Positive Bacilli -- organism by organism, because "those
    learning objectives are really, really general, so let's go to the list of
    organisms" (12:18-19:32);
  * Lecture 12, Epidemiology -- a closing list of under a minute
    (19:38-20:26), because she had taught it that morning.

This is the Exam 1 pattern (tools/build_micro_webster_review.py) applied again,
with the same rules:

  1. The tier on each heading is HER weighting. Know cold = she asked the class
     to answer it, drilled it, or said "need to know / should know / should be
     able to" (for Lecture 12, in the lecture as well as the review). Know it =
     she walked it, or it is an objective she did not mention (the box says so,
     plainly -- her words are never invented). Light touch = she said not to
     memorize it.
  2. Her words are quoted ONLY where both transcripts of the recording agree
     (Whisper and Notability; minor ASR differences aside), with the Whisper
     timestamp. Lecture-part quotes for Lecture 12 are labeled as from the
     lecture, never as from the review.
  3. The recording decides WHAT is weighted; it is never the source of a fact.
     Every answer is taken from the decks (visible slide text and pictures; the
     speaker notes do not count) and cited to a slide.
  4. FLAG rather than follow silently: objectives her walk skipped, places where
     what she said differs from a slide (the slide wins, and the page says so),
     and things she said that are on no slide (noted as her aside, not taught).

Lecture numbering: the site and the calendar call the Gram-positive bacilli
lecture Lecture 10; its deck file is "Lecture 9 Dr. Webster Gram positive
Bacilli.pptx". Citations say "Lecture 10, Slide N" with that file's numbering.

Scope: Lectures 7, 10 and 12 only. Exam 2 (Friday 23 October 2026) covers
Lectures 7-13; Dr. Fair's Lectures 8, 9, 11 and 13 are examinable and are not
here -- the page says so rather than leaving a silent gap.
"""
_REPO = __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__)))  # this checkout, never a hard-coded path
import os
import re

ROOT = _REPO
DONOR = os.path.join(ROOT, "Microbiology Exam 2/micro-exam-2-study-guide.html")
OUT = os.path.join(ROOT, "Microbiology Exam 2/micro-exam-2-webster-review.html")

REVIEW_LENGTH_S = 20 * 60 + 33   # part 4 is 20:33 long

# --------------------------------------------------------------------------
# Tiers. The label is hers; the wording under it is her actual instruction.
# --------------------------------------------------------------------------
COLD = ("cold", "Know cold")
KNOW = ("know", "Know it")
LIGHT = ("light", "Light touch")

ITEMS = []     # (lecture, anchor, num, toc title, tier class)
FLAGS = []     # (lecture, kind, one-line summary) -- printed in the build summary
LIGHTS = []    # (lecture, what) -- light-touch sub-items inside an objective


def item(lec, anchor, num, title, tier, review, body, lecture=None, toc=None):
    """One review item: her words (review, then lecture), then the slides."""
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
    """She said it one way, the slide says it another: the slide wins."""
    FLAGS.append((lec, "slide wins", summary))
    return ('<div class="callout"><p><strong>Her words and the slide differ; the slide '
            'wins.</strong> ' + html + '</p></div>')


def aside(lec, summary, html):
    """She said it; no slide says it. Noted, not taught."""
    FLAGS.append((lec, "aside", summary))
    return ('<div class="callout"><p><strong>Her aside, not on a slide.</strong> ' + html +
            '</p></div>')


def gap(lec, summary, html, kind="gap", lead="Not in her review, still examinable."):
    """The objective asks it; her review left it out (or the deck lacks what she asked for)."""
    FLAGS.append((lec, kind, summary))
    return ('<div class="callout"><p><strong>' + lead + '</strong> ' + html + '</p></div>')


def light(lec, what, title, quote, body):
    """A light-touch sub-item inside an objective: she said not to memorize it."""
    LIGHTS.append((lec, what))
    return ('<h4 class="subsub">' + title + ' <span class="tier tier-light">Light touch</span></h4>\n'
            '  <div class="asked"><span class="asked-label">In the lecture</span><p>' + quote +
            '</p></div>\n  ' + body)


def src(text):
    return '<span class="src">%s</span>' % text


def _cite(lec, slides):
    plural = any(t in slides for t in ("&ndash;", ",", " and "))
    return src("Lecture %d, Slide%s %s." % (lec, "s" if plural else "", slides))


def c7(s):
    return _cite(7, s)


def c10(s):
    return _cite(10, s)


def c12(s):
    return _cite(12, s)


def orgtable(rows):
    """Objective 1 field by field for one organism. Rows she raised are highlighted."""
    out = ['<table>', '  <tr><th>What the objective asks</th><th>What the slides say</th></tr>']
    for field, text, hers in rows:
        f = '<mark class="prof-highlight">%s</mark>' % field if hers else field
        out.append('  <tr><td><strong>%s</strong></td><td>%s</td></tr>' % (f, text))
    out.append('</table>')
    return "\n  ".join(out)


def objmap(text):
    return '<p class="obj-map">' + text + '</p>'


def iobox(title, objectives):
    lis = "\n".join("    <li>%s</li>" % o for o in objectives)
    return ('<div class="io-box">\n  <h3>%s</h3>\n  <ol>\n%s\n  </ol>\n</div>' % (title, lis))


# --------------------------------------------------------------------------
# Section 1 -- Lecture 7, Disorders in Immunity (her objective-by-objective walk)
# --------------------------------------------------------------------------
IO7 = [
    "Describe the types of immunopathologies.",
    "Compare and contrast the types of hypersensitivities and diseases caused by hypersensitivity conditions.",
    "Describe the primary methods of diagnosing, treating, and preventing allergies.",
    "Describe the mechanism of transfusion reactions.",
    "Explain the immunology of transplantations and tissue histocompatibility.",
    "Describe etiology autoimmune conditions.",
    "Differentiate between primary and secondary immunodeficiency conditions.",
    "Explain the mechanisms of carcinogenesis.",
    "Compare and contrast immunotherapy strategies.",
]

S1 = []

S1.append(item(7, "w7-types", "1.1", "Objective 1 &mdash; The types of immunopathologies", KNOW,
  "“My chapters on this are the immune disorders. … Different types of immunopathologies.” "
  "[part 4, 0:02–0:08] She read the objective and went straight on to the hypersensitivities; "
  "she asked nothing about it.",
  f"""<p>One slide answers this objective, and it is the frame for the whole lecture: every
  disorder is either the immune system doing <strong>too much</strong> or <strong>too
  little</strong>. {c7('3')}</p>
  <table>
    <tr><th>Immunopathology</th><th>What it is</th><th>Over or under</th></tr>
    <tr><td><strong>Allergy, hypersensitivity</strong></td><td>An exaggerated, misdirected expression of immune responses to an allergen (antigen), using the same mechanisms as protective immune reactions. Four types: I, II and III are B cell mediated; IV is T cell mediated</td><td>Overreaction</td></tr>
    <tr><td><strong>Autoimmunity</strong></td><td>Abnormal responses to self antigen</td><td>Typically overreaction</td></tr>
    <tr><td><strong>Immunodeficiency</strong></td><td>Deficiency or loss of immunity</td><td>Underreaction</td></tr>
    <tr><td><strong>Cancer</strong></td><td>Both a cause and an effect of immune dysfunction</td><td>Underreaction</td></tr>
  </table>
  <p>The overview picture draws the same split: overreaction leads to the four hypersensitivities
  (B cells for types I&ndash;III, T cells for type IV); underreaction or loss of immunity leads to
  immunodeficiency; lack of surveillance leads to cancer. {c7('4')}</p>
  <div class="pearl"><p>The rest of this section follows that split. Items 1.2&ndash;1.6 are
  overreactions; items 1.7&ndash;1.9 are underreactions and cancer.</p></div>"""))

S1.append(item(7, "w7-hyper", "1.2", "Objective 2 &mdash; The four hypersensitivities", COLD,
  "“The types of hypersensitivities and the diseases caused by them. Remember, we have four "
  "different hypersensitivity types. You need to be able to identify their mechanisms and example "
  "diseases.” [part 4, 0:13–0:23] Then she asked for each type in turn: “What is type one?” "
  "[0:30] … “What’s type two?” [1:24] … “What happens in a type three hypersensitivity? … But "
  "what’s the mechanism of action?” [5:15–5:23] … “And then what is a type four "
  "hypersensitivity?” [6:13]",
  f"""<p>“You need to be able to” is the strongest instruction she gave for this lecture, and she
  named the two things to be able to do: <strong>the mechanism</strong> and <strong>an example
  disease</strong>. The slide&rsquo;s table has exactly those columns.</p>
  <table>
    <tr><th>Type</th><th>Mechanism</th><th>Examples</th></tr>
    <tr><td><strong>I</strong></td><td>IgE (immunoglobulin E) mediated, <strong>immediate</strong>. Cell-bound antibody is crosslinked and releases inflammatory mediators; mast cells, basophils and eosinophils are involved</td><td>Hay fever, hives, anaphylactic shock</td></tr>
    <tr><td><strong>II</strong></td><td>Initiated by IgG (immunoglobulin G) and IgM (immunoglobulin M). Free antibody binds <strong>cell-surface</strong> antigens; complement is activated; cell lysis by the membrane attack complex, and phagocytosis</td><td>Transfusion reactions</td></tr>
    <tr><td><strong>III</strong></td><td>Initiated by IgG and IgM. Free antibody binds <strong>soluble</strong> antigens, forming immune complexes that embed in basement membranes and start an inflammatory condition (phagocytosis and complement activation)</td><td>Serum sickness; autoimmune conditions such as lupus</td></tr>
    <tr><td><strong>IV</strong></td><td><strong>Delayed</strong> hypersensitivity; <strong>T cell mediated</strong>; cytotoxic cells destroy tissue</td><td>Contact dermatitis</td></tr>
  </table>
  <p>{c7('9')}</p>
  {flag('''<p>Her one-line version of each type, which is the way to carry them into the exam:
  <strong>type I</strong> is IgE on mast cells; <strong>type II</strong> is IgG or IgM plus
  complement punching holes in a cell (“Complement has the membrane attack complex that will
  then punch holes into membranes” [part 4, 1:48]); <strong>type III</strong> is antigen-antibody
  complexes lodging in basement membranes and setting up inflammation; <strong>type IV</strong>
  is “no antibodies, T cells” [part 4, 6:23]. The question to ask of any example is whether there
  is an antibody, and if so whether it binds a cell (II) or a soluble antigen (III).</p>''')}

  <h4 class="subsub">Type I in more detail</h4>
  <p><strong>Sensitizing dose:</strong> on first contact with the allergen, specific B cells form
  IgE, which attaches to mast cells and basophils; generally no signs or symptoms.
  <strong>Provocative dose:</strong> later exposure to the same allergen binds the IgE&ndash;mast
  cell complex (each cell can bind 10,000&ndash;40,000 IgE) and the mast cells degranulate,
  releasing inflammatory cytokines. General targets are the skin, upper respiratory tract,
  gastrointestinal tract and conjunctiva (rashes, itching, redness, rhinitis, sneezing, diarrhea,
  tears); systemic targets are smooth muscle, mucous glands and nervous tissue (vascular dilation
  and constriction changing blood pressure and respiration). {c7('12')}</p>
  <p>The mediators drawn on the degranulation diagram are <strong>histamine, serotonin and
  bradykinin</strong>, <strong>prostaglandins</strong> and <strong>leukotrienes</strong>. {c7('14')}
  The <strong>wheal and flare</strong> skin reaction is cutaneous anaphylaxis and is used in
  diagnosis {c7('20')}; systemic anaphylaxis is sudden respiratory and circulatory disruption
  that can be fatal in minutes {c7('21')}. About six hours after the immediate reaction a
  <strong>late-phase reaction</strong> follows, mediated by synthesized products such as
  leukotrienes and drawing in eosinophils. {c7('23')}</p>
  {aside(7, "L7: heparin named as a type I mediator; the mosquito-bite wheal example", '''She
  named <em>heparin</em> with histamine and the prostaglandins, and gave a mosquito bite as a
  wheal-and-flare example [part 4, 0:51&ndash;1:05]. Neither is on a slide; the slide&rsquo;s
  mediators are the five named above.''')}

  <h4 class="subsub">Type II, type III and type IV in more detail</h4>
  <p><strong>Type II</strong> reactions lyse foreign cells: antibodies of the IgG or IgM class
  stimulate complement, leading to lysis. Examples: transfusion reactions (ABO blood groups; the
  Rh factor and hemolytic disease of the newborn) and some autoimmune diseases &mdash; autoimmune
  hemolytic anemia, and myasthenia gravis against acetylcholine receptors. {c7('32')}</p>
  <p><strong>Type III</strong>: antigen-antibody reaction of IgG and IgM (sometimes IgA,
  immunoglobulin A) with complement; the complexes deposit in the basement membranes of epithelial
  tissues, are trapped, and incite a damaging inflammatory response. It requires a large amount of
  antigen; symptoms are delayed by hours to days; joint, skin and kidney involvement are typical.
  {c7('38')} Examples: <strong>serum sickness</strong> (foreign animal proteins such as horse serum
  for tetanus, or animal hormones or drugs; complexes in the heart, kidneys, skin and joints); the
  <strong>Arthus reaction</strong> (localized dermal injury from inflamed blood vessels, a vasculitis,
  after a second injection of vaccine at a site; normally self-limiting); and autoimmune disorders
  &mdash; post-streptococcal glomerulonephritis, systemic lupus erythematosus and rheumatoid
  arthritis. {c7('39')}</p>
  <p><strong>Type IV</strong>: delayed hypersensitivity, T cell mediated &mdash; a delayed response
  to antigen involving activation of, and damage by, T cells. Infectious allergy: tuberculosis,
  leprosy, syphilis, histoplasmosis, toxoplasmosis, candidiasis. Skin responses: the tuberculin skin
  test, and contact dermatitis from plants, metals and cosmetics. And graft rejection. {c7('40')}
  In contact dermatitis the first contact is the sensitizing dose; later contact is the reactive
  dose, with tissue damage from macrophage cytokines and cytotoxic T cells. {c7('42')}</p>
  <div class="callout"><p><strong>Timing, and a word trap.</strong> The Lecture 7 slides give no
  hours for type IV. The hours are on the Lecture 10 tuberculosis slide: the Mantoux test is read
  for a red wheal (induration) at <strong>48&ndash;72 hours</strong> {c10('76')} &mdash; which is
  what she said (“48 to 72 hours after you’re exposed” [part 4, 6:53]). Note that the slides also
  call type III symptoms “delayed &mdash; hours to days” {c7('38')}; the <em>name</em> delayed
  hypersensitivity belongs to type IV, so do not let the word alone decide an answer.</p></div>
  {aside(7, "L7: type IV takes '48 hours or so to develop the new effector T cells'", '''Her reason
  for the delay, “it takes 48 hours or so to develop the new effector T cells” [part 4, 6:45], is
  not on a slide.''')}
  <div class="pearl"><p>One crossover worth knowing: allergic asthma starts as a type I response
  (crosslinking of IgE on mast cells by inhaled allergen) but leads to <strong>chronic asthma,
  which the slide labels type IV</strong>, mediated by cytokines and eosinophil granules.
  {c7('19')}</p></div>"""))

S1.append(item(7, "w7-allergy", "1.3", "Objective 3 &mdash; Diagnosing, treating and preventing allergies", COLD,
  "“If you wanted to treat a type one allergy, how do you treat type one allergies … You can also "
  "take different kinds of medications, but the medications are typically against some of those "
  "substances that are released. We’re talking about things like antihistamines. … But what can "
  "you do to try to really quell that? You go through the desensitization, the allergy shots, and "
  "what are you trying to do when you get allergy shots? You’re trying to train your body to "
  "produce what? Defensive IgG antibodies against the allergen.” [part 4, 3:42–4:47]",
  f"""<p>She asked two questions here, and both were about <em>treatment</em>. Management of type I
  hypersensitivity has three general methods: <strong>prevention, pharmacological control and
  desensitization</strong>. {c7('26')}</p>

  <h4 class="subsub">Prevention</h4>
  <p>Modify the environment, modify behaviors, avoid exposure to the allergen. {c7('27')}</p>

  <h4 class="subsub">Pharmacological control &mdash; drugs that block lymphocytes, mast cells or mediators</h4>
  <table>
    <tr><th>Drug</th><th>What it does</th></tr>
    <tr><td><strong>Antihistamines</strong></td><td>Bind to histamine receptors on target organs</td></tr>
    <tr><td>Corticosteroids</td><td>Inhibit lymphocytes to reduce IgE</td></tr>
    <tr><td>Cromolyn sodium</td><td>Blocks degranulation</td></tr>
    <tr><td>Montelukast sodium</td><td>Blocks synthesis of leukotriene</td></tr>
    <tr><td>Omalizumab</td><td>Monoclonal antibody against IgE</td></tr>
    <tr><td>Epinephrine</td><td>Reverses airway constriction, re-establishes tight junctions in the endothelium</td></tr>
  </table>
  <p>{c7('28')} In systemic anaphylaxis epinephrine also relaxes bronchial smooth muscle, prevents
  or decreases upper airway mucosal edema, stimulates the heart, and binds receptors on immune cells
  to suppress histamine release. {c7('22')}</p>

  <h4 class="subsub">Desensitization &mdash; her “allergy shots”</h4>
  <p>Allergen-specific immunotherapy. The most common form is <strong>subcutaneous
  immunotherapy</strong>: small amounts of the allergen are injected, which may stimulate high
  levels of <strong>allergen-specific IgG that block the allergen from the IgE, so the mast cells
  do not degranulate</strong>. It improves reactions in about 80% of those who go through it.
  {c7('29')} The slide adds that “it’s not that simple”: regulatory T cells are activated that
  inhibit T cell activation of B cells and release cytokines that reduce inflammation, and
  mediators are induced that damp local allergic inflammation. {c7('30')}
  <strong>Sublingual immunotherapy</strong> puts the allergen under the tongue as a dissolvable
  tablet or liquid extract; it is used more outside the United States, though tablets are approved
  in the United States for pollen and dust mite allergens, and trials show it effective for peanut,
  kiwi, hazelnut, milk and peach allergies. {c7('31')}</p>
  {differs(7, "L7 allergy shots: she said IgG means 'it can't make the IgE'; Slide 29: IgG blocks the allergen from the IgE", f'''She
  finished the point with “So you have more IgG defensive ones so that it can’t make the IgE that
  will cause the mast cells to rupture” [part 4, 4:47]. The slide&rsquo;s mechanism is that the
  blocking IgG intercepts the <em>allergen</em> before it reaches the IgE already on the mast
  cells, so the mast cells do not <em>degranulate</em>. {c7('29')} Learn the slide&rsquo;s
  version: the IgE is still there; the allergen never gets to it.''')}

  <h4 class="subsub">Diagnosing allergy</h4>
  {gap(7, "L7 objective 3: diagnosing allergy (Slide 25) not mentioned", f'''The objective asks
  for diagnosis as well as treatment and prevention, and she did not mention diagnosis. It is on
  one slide. {c7('25')}''')}
  <ul>
    <li>First, it is important to determine whether a person is experiencing allergy or infection.</li>
    <li><strong>Skin testing</strong> &mdash; wheal and flare reactions: skin prick testing and intradermal testing.</li>
    <li><strong>Blood tests</strong> &mdash; specific IgE; increased basophils.</li>
    <li><strong>Physician-supervised challenge</strong> &mdash; for food allergies when other tests are inconclusive.</li>
    <li><strong>Patch test</strong> &mdash; typically for contact dermatitis, which is type IV.</li>
  </ul>
  <p>{c7('25')}</p>"""))

S1.append(item(7, "w7-transfusion", "1.4", "Objective 4 &mdash; Transfusion reactions: ABO and Rh", COLD,
  "“So here we were talking about transfusion reactions. The ABO blood typing reactions. And so "
  "you should know, you know, what is compatible for donor and recipient … what is not compatible "
  "for donor and recipient.” [part 4, 1:59–2:18] Then Rh, as a question: “Rh incompatibility. "
  "When does that occur? … Mother is negative. Rh negative. Father is positive. And so first "
  "pregnancies are okay. But first pregnancies can sensitize the mother to the Rh factors.” "
  "[part 4, 2:33–3:04] … “But what can you do to prevent that from happening?” A student "
  "answered, and she confirmed: “Exactly right.” [part 4, 3:29–3:35]",
  f"""<p>“You should know” is a direct instruction, and it was about compatibility. Both of her
  examples are type II reactions: antibody binding a cell and complement lysing it.</p>

  <h4 class="subsub">ABO &mdash; the rule the slide gives</h4>
  <ul>
    <li>Donors and recipients are matched for the A, B, O system of blood group antigens. There are <strong>no major histocompatibility complex molecules on red blood cells</strong>, so ABO is what is critical to match.</li>
    <li><strong>You carry antibodies in your serum against the ABO antigens you lack.</strong></li>
    <li>Crossmatching confirms compatibility. Transfusions are temporary.</li>
    <li>ABO incompatibilities <strong>can be fatal</strong>, because of complement activation and cell lysis.</li>
  </ul>
  <p>{c7('33')}</p>
  <p><strong>The cross-match test:</strong> the recipient&rsquo;s serum is tested against the
  donor&rsquo;s red cells. The reverse is not done, because even with whole blood there is not
  enough donor antibody to coat the recipient&rsquo;s cells densely enough for a reaction. {c7('34')}
  What a reaction does: destruction of red cells, blockage of the glomeruli, fever and jaundice; and
  even if complement activation is incomplete, antibody-coated cells may attract natural killer
  cells or macrophages. {c7('35')}</p>
  {gap(7, "L7 objective 4: she said know what is compatible; the deck gives the rule, no compatibility chart", f'''She
  asked the class to know what is compatible for donor and recipient, but the deck has no
  compatibility chart; it gives the rule on Slide 33 (and a picture of red cells). The table below
  is that rule applied, nothing more: a donor&rsquo;s red cells are incompatible when they carry an
  ABO antigen the recipient&rsquo;s own cells lack, because the recipient&rsquo;s serum has antibody
  against it. {c7('33')}''', kind="deck gap", lead="What the deck gives.")}
  <table>
    <tr><th>Recipient&rsquo;s red cells carry</th><th>So the recipient&rsquo;s serum has antibody against</th><th>Donor red cells that are compatible</th></tr>
    <tr><td>A</td><td>B</td><td>O or A</td></tr>
    <tr><td>B</td><td>A</td><td>O or B</td></tr>
    <tr><td>A and B</td><td>Neither</td><td>O, A, B or AB</td></tr>
    <tr><td>Neither (type O)</td><td>A and B</td><td>O only</td></tr>
  </table>

  <h4 class="subsub">Rh and hemolytic disease of the newborn</h4>
  <ul>
    <li>The Rh antigen is present on Rh-positive red cells and not on Rh-negative cells. An Rh-negative person does not produce anti-Rh antibody <strong>unless sensitized</strong> &mdash; by a bad transfusion or an incompatible pregnancy.</li>
    <li><strong>Hemolytic disease of the newborn</strong> (erythroblastosis fetalis) occurs with an <strong>Rh-negative mother and an Rh-positive fetus</strong>.</li>
    <li>The <strong>first pregnancy</strong> is normally fine &mdash; it is the sensitization. <strong>Subsequent pregnancies</strong> have the potential to be hemolytic.</li>
    <li>Prevention is <strong>passive immunization with antibodies against the Rh antigen (Rhogam)</strong>, which prevents sensitization of the mother.</li>
  </ul>
  <p>{c7('36')} Rhogam is given at <strong>26&ndash;28 weeks</strong> of pregnancy, <strong>within
  72 hours after birth</strong>, and after prenatal invasive tests, abdominal injury or accidental
  exposure. {c7('37')}</p>
  {differs(7, "L7 Rh: she framed it as Rh-negative mother and Rh-positive father; Slide 36: Rh-negative mother and Rh-positive fetus", f'''She
  put the condition as “Mother is negative … Father is positive” [part 4, 2:46&ndash;2:50]. The
  slide states it as an Rh-negative mother with an <strong>Rh-positive fetus</strong>. {c7('36')}
  A positive father is how the fetus can be positive, but the fetus&rsquo;s type is what the
  slide&rsquo;s condition, and an exam stem, turns on.''')}
  {aside(7, "L7 Rh: anti-Rh antibody is IgG and crosses the placenta", '''She added that the
  mother&rsquo;s anti-Rh antibody “goes across, it’s an IgG, goes across the placenta”
  [part 4, 3:16&ndash;3:21]. The Rh slides do not say which class of antibody it is or that it
  crosses the placenta.''')}"""))

S1.append(item(7, "w7-transplant", "1.5", "Objective 5 &mdash; Transplantation and histocompatibility", KNOW,
  "“We talked about transplantations and tissue histocompatibility. … Remember that you are trying "
  "to match up the MHC [major histocompatibility complex] or HLA [human leukocyte antigen] antigens "
  "when you’re talking about donor versus recipient, and that there are different kinds of "
  "rejections that you can have. … So go back and look over those rejection types. The hyperacute "
  "is a type two. The acute is a type four. The chronic is a type three.” [part 4, 7:07–7:54] "
  "“Remember that the chronic was one that we often attribute … failures of heart and kidney "
  "grafts over a long period of time.” [part 4, 8:00–8:04]",
  f"""<p>She told the class to go back to the rejection types and then gave the answer herself.
  Her mapping matches the slide exactly.</p>
  <table>
    <tr><th>Problem with a solid organ transplant</th><th>Hypersensitivity type</th><th>What the slides add</th></tr>
    <tr><td><strong>Hyperacute rejection</strong></td><td><strong>Type II</strong></td><td>Pictured as a swollen, dark, failed kidney in surgery {c7('45')}</td></tr>
    <tr><td><strong>Acute rejection</strong></td><td><strong>Type IV</strong></td><td>Effector T cells respond to human leukocyte antigen differences between donor and recipient. The picture: dendritic cells in the kidney graft migrate to the spleen and activate effector T cells, which travel to the graft in the blood and destroy it {c7('46')}</td></tr>
    <tr><td><strong>Chronic rejection</strong></td><td><strong>Type III</strong></td><td>Occurs months or years after transplantation; thickening of the vessel wall makes the blood supply inadequate; causes failure of <strong>more than half of all kidney and heart transplants after 10 years or more</strong> {c7('47')}</td></tr>
    <tr><td>Graft versus host disease</td><td>Type IV</td><td>Not in her review: see below</td></tr>
  </table>
  <p>{c7('44')}</p>
  {flag('''<p><strong>Hyperacute II, acute IV, chronic III.</strong> The numbers do not run in
  order of speed, which is exactly why she told the class to go back and look. She did not ask
  the room for it; she said it, so it sits in the Know it tier, but it is the single most
  quotable fact in this objective.</p>''')}

  <h4 class="subsub">The rest of the objective</h4>
  <p>Graft or transplantation rejection runs both ways: the host may reject the graft, and the
  graft may reject the host. It is associated with the major histocompatibility complex, and
  different grafts succeed differently because of compatibility. <strong>Autograft</strong>: a
  self graft (skin, gum, vein). <strong>Isograft</strong>: from a genetically identical twin.
  <strong>Allograft</strong>: from a member of the same species. <strong>Xenograft</strong>: from
  another species. {c7('43')}</p>
  <table>
    <tr><th>Tissue</th><th>Matching requirement</th></tr>
    <tr><td>Cornea</td><td>The first organ successfully transplanted. The eye has evolved tolerance mechanisms (down-regulating T cells, macrophages, neutrophils and complement) so it succeeds <strong>even without a human leukocyte antigen match</strong></td></tr>
    <tr><td>Liver</td><td>Succeeds across human leukocyte antigen differences; human leukocyte antigen is not assessed but <strong>ABO blood group is</strong>; hepatocytes carry very little class I and no class II</td></tr>
    <tr><td>Bone marrow</td><td><strong>Most sensitive</strong> to human leukocyte antigen discrepancies, which can lead to <strong>graft versus host disease</strong>: donor cells attack host tissue, systemically (skin rash, muscle, liver, gastrointestinal tract), in about 30% of marrow recipients</td></tr>
  </table>
  <p>{c7('48, 49')} Rejection is minimized by tissue matching of human leukocyte antigens (mixed
  lymphocyte reaction, tissue typing) and by immunosuppressive drugs: purine analogs,
  corticosteroids, tacrolimus and cyclosporine, and rapamycin (sirolimus). {c7('51')}</p>
  {gap(7, "L7 objective 5: graft versus host disease, graft types, cornea/liver/marrow, immunosuppression not mentioned", '''Her
  review stopped at the three rejection speeds. Graft versus host disease (type IV), the four graft
  types, the cornea, liver and bone marrow contrast, and the immunosuppressive drugs above are
  still on the slides and still part of this objective.''')}"""))

S1.append(item(7, "w7-autoimmune", "1.6", "Objective 6 &mdash; The etiology of autoimmune conditions", KNOW,
  "“Autoimmune conditions, the mechanism of the attack, we’re dealing with all of the different "
  "hypersensitivity types except one. Except one. So there are type two, three, and four for "
  "autoimmune disorders.” [part 4, 8:18–8:38] Then the causes: “You can be dealing with what’s "
  "called that sequestered antigen, like when you’re dealing with the eye. You can be dealing with "
  "a normal immune response that goes wrong, like rheumatic fever.” [part 4, 8:47–9:00] … “We "
  "talked about the non-infectious autoimmunity. You injure the one eye. You let out antigens that "
  "the body hasn’t seen before, and then it not only goes after that eye but the other eye as "
  "well.” [part 4, 9:19–9:28] … “the thymus going through senescence can initiate autoimmunity.” "
  "[part 4, 9:35]",
  f"""<p>She repeated “except one” before giving the answer, and then walked the four origins in
  the slide&rsquo;s order.</p>
  <p><strong>What autoimmunity is:</strong> the immune system has lost tolerance to autoantigens and
  forms autoantibodies and sensitized T cells against them, destroying self tissue.
  <strong>It involves all hypersensitivity reactions except type I.</strong> There are genetic and
  gender predispositions: autoimmunities run in families, and women are more likely to have them
  than men. Disruption can be systemic or organ specific. {c7('52')}</p>

  <h4 class="subsub">The origins &mdash; her four, in the slide&rsquo;s order</h4>
  <table>
    <tr><th>Origin</th><th>What the slides say</th></tr>
    <tr><td><strong>Sequestered antigen</strong></td><td>During embryonic growth some tissues are immunologically privileged; if they are damaged later, the antigens are released and attacked: the <strong>central nervous system, the lens of the eye, the thyroid, the testes</strong> {c7('53')}</td></tr>
    <tr><td><strong>A normal immune response</strong> &mdash; molecular mimicry</td><td>Similarities between foreign and self antigens result in cross-reactivity. Examples: <strong>rheumatic fever</strong> (cross-reactive streptococcal antigen); Lyme disease arthritis (<em>Borrelia burgdorferi</em>); reactive arthritis (<em>Shigella</em>, <em>Salmonella</em>, <em>Campylobacter</em>); type I diabetes (Coxsackie virus A and B, echovirus, rubella) {c7('53, 54')}</td></tr>
    <tr><td><strong>A non-infectious response</strong></td><td>The picture: trauma to one eye releases sequestered intraocular protein antigens; they are carried to the lymph nodes and activate T cells; the effector T cells return in the bloodstream and attack the antigen <strong>in both eyes</strong> {c7('55')}</td></tr>
    <tr><td><strong>Thymus senescence</strong></td><td>The thymus is most active in fetal development and early neonatal life, then degenerates and is replaced with fat (involution). There may be a connection to autoimmunity, though the mechanism is unclear: premature aging of the thymus is characteristic of young people with autoimmune disorders, chronic inflammation may hasten it, and decreased thymic output may mean less efficient T cell development and more opportunistic infections, cancer and autoimmunity {c7('56, 57')}</td></tr>
  </table>
  {differs(7, "L7 autoimmunity: rheumatic fever 'leading to heart problems or reactive arthritis'; slides keep reactive arthritis as a separate example (Shigella, Salmonella, Campylobacter)", f'''She
  said rheumatic fever leads “to heart problems or reactive arthritis” [part 4, 9:16]. On the
  slides, acute rheumatic fever&rsquo;s consequences are <strong>arthritis, myocarditis and late
  scarring of the heart valves</strong> (antibodies to streptococcal cell wall antigens cross-react
  with cardiac muscle) {c7('58')}, while <strong>reactive arthritis</strong> is a separate molecular
  mimicry example caused by <em>Shigella</em>, <em>Salmonella</em> and <em>Campylobacter</em>
  {c7('54')}. Keep the two names apart.''')}

  <h4 class="subsub">Example diseases by hypersensitivity type</h4>
  <table>
    <tr><th>Type II (antibody against cell-surface or matrix antigens)</th><th>Type III (immune complexes)</th><th>Type IV (T cell mediated)</th></tr>
    <tr><td>Autoimmune hemolytic anemia; autoimmune thrombocytopenic purpura; Goodpasture&rsquo;s syndrome; pemphigus vulgaris and foliaceus; acute rheumatic fever; Graves&rsquo; disease (thyroid-stimulating hormone receptor &rarr; hyperthyroidism); myasthenia gravis (acetylcholine receptor &rarr; progressive weakness); insulin-resistant type 2 diabetes and hypoglycemia (insulin receptor)</td>
        <td>Subacute bacterial endocarditis; mixed essential cryoglobulinemia; systemic lupus erythematosus (DNA, histones, ribosomes &rarr; glomerulonephritis, vasculitis, arthritis)</td>
        <td>Type 1 diabetes (pancreatic beta-cell antigen); rheumatoid arthritis (unknown synovial joint antigen); multiple sclerosis (myelin basic protein, proteolipid protein &rarr; paralysis)</td></tr>
  </table>
  <p>{c7('58&ndash;60')} By organ: Graves&rsquo; disease (hyperthyroidism) and Hashimoto&rsquo;s
  thyroiditis (hypothyroidism), diabetes mellitus, myasthenia gravis, and multiple sclerosis, which
  may be associated with an earlier Epstein&ndash;Barr or retrovirus infection. {c7('61')}</p>
  <div class="callout"><p><strong>One deck inconsistency to know about.</strong> Rheumatoid
  arthritis is listed as a type III example on Slide 39 and as a type IV autoimmune disease on
  Slide 60. {c7('39, 60')} If a question hangs on it, read the stem for the mechanism it
  describes (immune complexes, or T cells).</p></div>"""))

S1.append(item(7, "w7-immunodef", "1.7", "Objective 7 &mdash; Primary versus secondary immunodeficiency", COLD,
  "“Immunodeficiencies, primary and secondary immunodeficiencies. What is a primary "
  "immunodeficiency? Well, you’re born with [it]. It’s genetic.” [part 4, 9:49–10:04] … “So what "
  "can cause a secondary immunodeficiency? HIV [human immunodeficiency virus], that’s absolutely "
  "right. Cancer, cancer chemotherapy. So … radiation, exposure to cannabis. So anything that "
  "happens after you’re born is a secondary immunodeficiency.” [part 4, 10:22–10:44]",
  f"""<p>She asked both halves of the objective as questions and took answers from the room.</p>
  <p>In an immunodeficiency, components of the immune response are absent; deficiencies involve B
  and T cells, phagocytes and complement. Two general categories: {c7('62')}</p>
  <table>
    <tr><th></th><th>Primary</th><th>Secondary</th></tr>
    <tr><td><strong>Definition</strong></td><td><strong>Congenital</strong>; usually genetic errors</td><td><strong>Acquired after birth</strong>; caused by natural or artificial agents</td></tr>
    <tr><td><strong>Examples on the slides</strong></td>
        <td><strong>B cell defect</strong>: agammaglobulinemia &mdash; the patient lacks antibodies; often more bacterial infections. <strong>T cell defect</strong> (thymus missing or abnormal): DiGeorge syndrome; often more fungal, protozoan, helminth and viral infections. <strong>Severe combined immunodeficiency</strong>: both limbs of the lymphocyte system missing or defective, so no adaptive immune response. Complement deficiencies; phagocyte deficiencies</td>
        <td>Infection and organic disease; <strong>human immunodeficiency virus</strong> (T helper cells are targeted, leading to overall immune suppression); <strong>chemotherapy or radiation</strong>; <strong>blood cell cancers</strong></td></tr>
  </table>
  <p>{c7('62, 63, 65')}</p>
  <div class="pearl"><p>The pattern the diagram is built to show: <strong>T cell deficiency
  &rarr; recurrent fungal, viral and protozoan infections; B cell deficiency &rarr; recurrent
  bacterial infections.</strong> The same picture marks where each primary defect blocks
  development: some forms of severe combined immunodeficiency at the lymphoid stem cell, DiGeorge
  syndrome at the thymus, adenosine deaminase deficiency on the way to working T cells, and
  congenital agammaglobulinemia on the B cell side. {c7('64')}</p></div>
  {differs(7, "L7 secondary immunodeficiency: she named 'cancer' and 'exposure to cannabis'; Slide 65: blood cell cancers, chemotherapy or radiation, HIV, infection, organic disease (no cannabis)", f'''Her
  list included “exposure to cannabis” [part 4, 10:37], which is not on the slide, and
  “cancer” in general, where the slide says <strong>blood cell cancers</strong>. Learn the
  slide&rsquo;s list: infection, organic disease, human immunodeficiency virus, chemotherapy or
  radiation, blood cell cancers. {c7('65')} Her rule of thumb does match the slide: secondary
  means acquired after birth. {c7('62')}''')}"""))

S1.append(item(7, "w7-carcino", "1.8", "Objective 8 &mdash; The mechanisms of carcinogenesis", KNOW,
  "She did not discuss this objective in the review. Her only words on cancer, “And then we "
  "talked about cancer, and we talked about different kinds of immune therapies for cancer” "
  "[part 4, 10:48–11:01], led straight into the therapies of Objective 9.",
  f"""{gap(7, "L7 objective 8: mechanisms of carcinogenesis (Slides 66-72) skipped entirely", '''This
  objective was skipped entirely. It is still on the exam&rsquo;s objective list, and the deck
  answers it in seven slides.''')}
  <p><strong>How a cancer arises.</strong> Cancer cells appear to have genetic alterations that
  disrupt the normal cell division cycle. Possible causes: errors in mitosis, genetic damage,
  activation of oncogenes, or retroviruses. The result is new growth of abnormal cells; tumors may
  be <strong>benign</strong> (nonspreading, self-contained) or <strong>malignant</strong> (spreading
  from the tissue of origin to other sites). <strong>Immune surveillance</strong> keeps cancer
  &ldquo;in check&rdquo;. {c7('66')}</p>
  <p><strong>Transformation:</strong> a cancer arises from a <strong>single cell that has
  accumulated multiple mutations</strong>; oncogenes are activated by exposure to radiation,
  chemicals or oncogenic viruses. The slide&rsquo;s diagram walks one tumor from normal epithelium
  through three lost tumor suppressor genes and one activated oncogene to an invasive tumor, rapid
  accumulation of mutations, and metastasis. {c7('67')}</p>
  <table>
    <tr><th>Oncogenic virus</th><th>Associated tumors</th></tr>
    <tr><td>Papillomavirus</td><td>Genital warts (benign); carcinoma of the uterine cervix</td></tr>
    <tr><td>Hepatitis B virus</td><td>Liver cancer (hepatocellular carcinoma)</td></tr>
    <tr><td>Epstein&ndash;Barr virus</td><td>Burkitt&rsquo;s lymphoma; nasopharyngeal carcinoma; B-cell lymphoproliferative disease</td></tr>
    <tr><td>Human T-cell leukemia virus type 1</td><td>Adult T-cell leukemia or lymphoma</td></tr>
    <tr><td>Human immunodeficiency virus and human herpesvirus 8</td><td>Kaposi&rsquo;s sarcoma</td></tr>
  </table>
  <p>{c7('68')}</p>
  <p><strong>The necessary characteristics of cancer cells:</strong> they stimulate their own
  growth; ignore growth-inhibiting signals; avoid death by apoptosis; develop a blood supply
  (angiogenesis); leave their site of origin to invade other tissues (metastasis); replicate
  constantly; and evade and outrun the immune response. {c7('69')}</p>
  <p><strong>Tumor antigens.</strong> Unique antigens develop during transformation &mdash; more
  than 1000 identified. <strong>Tumor-specific antigens</strong> are on tumor cells but not on
  normal cells; <strong>tumor-associated antigens</strong> are on tumor cells and on normal cells in
  smaller amounts. Both provide targets for immune defense in a healthy person. {c7('70')}</p>
  <p><strong>How successful tumors evade the immune response:</strong> tumor cells can secrete
  TGF-&beta; (transforming growth factor beta) to suppress the immune response and recruit
  regulatory T cells, which make more TGF-&beta; and interleukin-10 and suppress the T cells
  specific for tumor antigens. <strong>The more regulatory T cells in a tumor, the worse the
  prognosis.</strong> {c7('71, 72')}</p>"""))

S1.append(item(7, "w7-immunotherapy", "1.9", "Objective 9 &mdash; Immunotherapy strategies", COLD,
  "“… we talked about different kinds of immune therapies for cancer, the immune checkpoint "
  "therapy, the adoptive cell therapy, the CAR-T [chimeric antigen receptor T] cells, the CAR-NK "
  "[chimeric antigen receptor natural killer] cells, where you’re taking cells out of the body and "
  "then you’re engineering them … putting them back to go against a tumor.” [part 4, 10:52–11:17] "
  "… “But what else do we use monoclonal antibodies for in cancer therapy? … We can link them to "
  "chemotherapeutic drugs or radionuclides. And what is the benefit of doing that?” "
  "[part 4, 11:37–11:54] … to “target just the tumor” [part 4, 12:00] … “And then we talked "
  "about different kinds of cytokine therapies like interferon.” [part 4, 12:05]",
  f"""<p>The overview slide names <strong>six</strong> strategies: immune checkpoint inhibitors,
  adoptive cell therapies, monoclonal antibodies, cytokine therapies, oncolytic viruses and cancer
  vaccines. She walked the first four and asked one question, about monoclonal antibodies.
  {c7('73')}</p>
  <table>
    <tr><th>Strategy</th><th>What the slides say</th></tr>
    <tr><td><strong>Immune checkpoint inhibitors</strong></td><td>Immune checkpoints regulate the immune system and, when activated, can reduce the response to a pathogen or cancer cell. The inhibitors block checkpoint proteins from binding their partner and prevent the &ldquo;off&rdquo; signal, so T cells can kill cancer cells. They do not kill cancer cells directly, but help target them for other immune cells and stop the immune system turning off before the cancer is eliminated. Used for melanoma and some lung cancers {c7('74')}</td></tr>
    <tr><td><strong>Adoptive cell therapy</strong></td><td>The patient&rsquo;s cells are genetically engineered <em>ex vivo</em> and transferred back as therapeutic agents. Tumor-infiltrating lymphocytes (cytotoxic T cells activated and expanded) are in development, not yet approved. <strong>Chimeric antigen receptor T cells</strong>: T or natural killer cells engineered with a receptor gene specific for a cancer type; approved by the Food and Drug Administration for different blood cancers. <strong>Chimeric antigen receptor natural killer cells</strong>: the gene inserted into natural killer cells to make them more efficient killers; mostly in clinical trials, including trials on solid tumors {c7('75')}</td></tr>
    <tr><td><strong>Monoclonal antibodies</strong></td><td>More than 100 approved for cancer diagnosis and therapy; used in diagnosis and to eliminate cancer cells, across many cancer types {c7('76')}</td></tr>
    <tr><td><strong>Cytokine therapies</strong></td><td><strong>Interleukin therapy</strong>: aldesleukin (interleukin-2) increases proliferation of cytotoxic T cells and natural killer cells and enhances anti-tumor antibody production; used in metastatic kidney cancer and melanoma. <strong>Interferon therapy</strong>: interferon alpha activates natural killer and dendritic cells; used in melanoma, Kaposi&rsquo;s sarcoma and several blood cancers. Hematopoietic growth factors also appear: erythropoietin for red cell production, interleukin-11 for platelets {c7('78')}</td></tr>
  </table>
  {flag(f'''<p>Her question: <em>what is the benefit of linking a monoclonal antibody to a
  chemotherapy drug or a radionuclide?</em> Her answer was to “target just the tumor”, and the
  slide&rsquo;s two pictures show how. An antibody against CD30 (cluster of differentiation 30) is
  linked to the drug auristatin; it binds the lymphoma cell, is taken in and cut free inside, and
  the drug binds the cell&rsquo;s microtubules, so the cell cannot form a mitotic spindle and dies
  by apoptosis. An antibody against CD20 (cluster of differentiation 20) carries a radionuclide to
  the malignant B cells it binds and irradiates them, damaging their DNA. In both, the antibody
  delivers the killing agent to the cell carrying the tumor marker. {c7('77')}</p>''')}
  {gap(7, "L7 objective 9: oncolytic viruses, cancer vaccines, Coley's toxins not mentioned", f'''She
  named four of the six strategies. The other two, and a historical one, are still on the slides.''')}
  <ul>
    <li><strong>Coley&rsquo;s toxins</strong> &mdash; immunotherapy from the 1890s: bone sarcomas were noted to regress with streptococcal skin infections, and the treatment became a mix of killed streptococci and <em>Serratia marcescens</em>; it fell from favor with radiation and chemotherapy. {c7('79')}</li>
    <li><strong>Oncolytic viral therapy</strong> &mdash; the viruses attack both normal and cancer cells but have little effect on normal cells; some are naturally oncolytic (mumps), others are engineered; the challenge is that the immune system may clear them before they work; only one is approved in the United States, for melanoma. {c7('80')}</li>
    <li><strong>Cancer vaccines</strong> &mdash; <em>prophylactic</em>, to prevent the infection that leads to cancer (hepatitis B against hepatocellular carcinoma; human papillomavirus against reproductive system cancers); <em>therapeutic</em>, to activate the immune system against tumor antigens: bacillus Calmette&ndash;Gu&eacute;rin, a weakened form of tuberculosis that stimulates a general immune response, used in bladder cancer; and sipuleucel-T, approved for metastatic, castration-resistant prostate cancer. {c7('81')}</li>
  </ul>"""))

# --------------------------------------------------------------------------
# Section 2 -- Lecture 10, Gram-Positive Bacilli (her organism-by-organism walk)
# --------------------------------------------------------------------------
IO10 = [
    "Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases, "
    "clinical manifestations, methods of treatment, and prevention of Gram-positive bacilli of medical "
    "importance.",
    "Describe the modes of transmission by which humans acquire Gram-positive bacilli of medical importance.",
]
APPX10 = ["Bacillus", "Clostridium", "Bacillus anthracis", "Anthrax",
          "Clostridium perfringens myonecrosis", "Clostridioides difficile pseudomembranous colitis",
          "Clostridium tetani", "Listeria monocytogenes", "Corynebacterium diphtheriae",
          "Propionibacterium acnes", "Tuberculosis", "Actinomyces israelii", "Nocardia"]

S2 = []

S2.append(item(10, "w10-bacillus", "2.1", "<em>Bacillus</em> and <em>Bacillus anthracis</em> &mdash; anthrax", COLD,
  "“Bacillus, if you recall, is our aerobic spore-forming organism. Where do we find the spore in "
  "the bacillus? In the middle, it’s centrally located.” [part 4, 12:34–12:50] … “And we talked "
  "about different forms of anthrax. Cutaneous anthrax, which is the most common. Gastrointestinal "
  "anthrax. But what’s the really bad one? Pulmonary anthrax, the [woolsorters’] disease. So that’s "
  "the one which is most deadly.” [part 4, 12:59–13:21]",
  objmap("Answers Objective 1 (morphology, laboratory, biochemistry, diseases, manifestations, "
         "treatment, prevention) and Objective 2 (transmission). Appendix 2: <em>Bacillus</em>, "
         "<em>Bacillus anthracis</em>, Anthrax.") + "\n  " +
  orgtable([
    ("Morphology", f"Genus: Gram-positive, endospore-forming, motile rods {c10('7')}. <em>B. anthracis</em>: large, block-shaped rods with <strong>central spores</strong> {c10('8')}", True),
    ("Oxygen and biochemistry", f"<strong>Aerobic</strong> and <strong>catalase positive</strong>; versatile in degrading complex macromolecules; mostly saprobic, primary habitat soil; a source of antibiotics such as bacitracin {c10('7')}. The differentiation scheme places <em>Bacillus</em> under &ldquo;aerobic or facultative anaerobes&rdquo; {c10('5')}", True),
    ("Disease", f"Anthrax, a <strong>zoonotic</strong> infection; significant for Koch&rsquo;s postulates; a Category A priority pathogen, a weapon of bioterrorism (an accidental release from a Soviet bioweapon facility in 1979 had an 86% fatality rate) {c10('8')}", True),
    ("Virulence", f"A polypeptide capsule, and an exotoxin of three parts: <strong>protective antigen</strong> binds host cells and creates the receptor for the other two; <strong>edema factor</strong> impairs phagocytosis and inhibits monocyte production of tumor necrosis factor and interleukin-6; <strong>lethal factor</strong> at low levels inhibits cytokine release, and at high levels is cytolytic for macrophages, releasing large amounts of interleukin-1, tumor necrosis factor alpha and nitric oxide &mdash; a massive inflammatory response and shock cascade like septic shock {c10('9')}", False),
    ("Treatment and prevention", f"Penicillin, tetracycline or ciprofloxacin; pulmonary anthrax is also treated with antitoxin to neutralize toxins. Vaccines: live spores and toxoid for livestock; Biothrax, the only vaccine approved by the Food and Drug Administration, a purified toxoid for high-risk occupations and military personnel, not for those under 18 or over 65 {c10('16')}", False),
  ]) + f"""

  <h4 class="subsub">The forms of anthrax &mdash; her question was which is the most deadly</h4>
  <table>
    <tr><th>Form</th><th>How it is acquired (Objective 2)</th><th>What happens</th></tr>
    <tr><td><strong><mark class="prof-highlight">Cutaneous</mark></strong> &mdash; <strong>95% of all human cases</strong></td><td>Through cuts or incisions in the skin; spores germinate in the tissue and grow</td><td>A painless papule that rapidly becomes an ulcer surrounded by vesicles and finally a <strong>necrotic eschar</strong>; untreated mortality about 20% {c10('10')}</td></tr>
    <tr><td><strong>Injection</strong></td><td>Identified in heroin-injecting addicts in northern Europe; not so far identified in the United States</td><td>Like cutaneous anthrax but evident in the deep muscle where the drug was injected; can spread faster and be harder to recognize and treat {c10('12')}</td></tr>
    <tr><td><strong><mark class="prof-highlight">Pulmonary</mark></strong> &mdash; <strong>woolsorters&rsquo; disease</strong></td><td>Inhalation of spores from infected animal products or soil</td><td>May have an asymptomatic latent period of two months or more. Alveolar macrophages engulf the spores and the exotoxins cause massive macrophage death. Cough, headache, fever, chills, vomiting, chest and abdominal pain, progressing to edema, capillary thrombosis and cardiovascular shock; about half have symptoms of meningitis. <strong>99% of untreated cases die within about three days of the first symptoms &mdash; the most deadly form</strong> {c10('13')}</td></tr>
    <tr><td><strong><mark class="prof-highlight">Gastrointestinal</mark></strong></td><td>Ingestion of contaminated meat</td><td>Ulceration of the mouth and esophagus with local lymphadenopathy; nausea, vomiting and malaise if the upper intestine is invaded; rapid sepsis if the large intestine is invaded. Mortality 25&ndash;60% depending on treatment {c10('14')}</td></tr>
    <tr><td>Anthrax meningitis</td><td>A complication of all types</td><td>Found in up to half of all patients with pulmonary anthrax; altered mental status, headache, fever, nausea and vomiting, seizures {c10('15')}</td></tr>
  </table>
  {differs(10, "L10 anthrax: she named three forms (cutaneous, gastrointestinal, pulmonary); the slides add injection anthrax (Slide 12) and anthrax meningitis (Slide 15)", f'''Her
  two superlatives match the slides exactly: cutaneous is the most common (95%), pulmonary is the
  most deadly. But she named three forms, and the slides have a fourth, <strong>injection
  anthrax</strong> {c10('12')}, plus <strong>anthrax meningitis</strong> as a complication of all
  of them {c10('15')}. A &ldquo;which is not a form of anthrax&rdquo; item could use either.''')}"""))

S2.append(item(10, "w10-clostridium", "2.2", "Genus <em>Clostridium</em> &mdash; where the spore sits", COLD,
  "“We talked about clostridium as an anaerobic spore former. Where is this spore found? … It’s "
  "not centrally located like bacillus.” [part 4, 13:26–13:41]",
  objmap("Answers Objective 1 (morphology, oxygen, biochemistry). Appendix 2: <em>Clostridium</em>.") + "\n  " +
  orgtable([
    ("Morphology", f"Gram-positive, spore-forming rods; oval or spherical spores, <strong>produced only under anaerobic conditions</strong> {c10('19')}", True),
    ("Spore position", f"The deck&rsquo;s text gives no position for the genus. Its picture of <em>Clostridium tetani</em> shows a round spore <strong>at one end of the rod</strong>, swelling it {c10('28')}; contrast the <strong>central</strong> spores of <em>Bacillus anthracis</em> {c10('8')}", True),
    ("Oxygen and biochemistry", f"<strong>Anaerobic</strong> and <strong>catalase negative</strong>; 120 species; synthesize organic acids, alcohols and exotoxins, the exotoxins among the most toxic substances on earth {c10('19')}. The scheme calls them <strong>obligate anaerobes</strong> {c10('5')}", True),
    ("Disease", f"Opportunistic pathogens: wound and tissue infections, and food intoxications {c10('20')}", False),
  ]) + f"""
  <table>
    <tr><th></th><th><em>Bacillus</em></th><th><em>Clostridium</em></th></tr>
    <tr><td><strong>Oxygen</strong></td><td>Aerobic (aerobic or facultative anaerobes)</td><td>Anaerobic (obligate anaerobes)</td></tr>
    <tr><td><strong>Catalase</strong></td><td>Positive</td><td>Negative</td></tr>
    <tr><td><strong>Spore</strong></td><td>Central (<em>B. anthracis</em>)</td><td>At one end of the rod (the <em>C. tetani</em> picture)</td></tr>
  </table>
  <p>{c10('5, 7, 8, 19, 28')}</p>
  <div class="callout"><p><strong>Why her answer is not quoted in full.</strong> The two transcripts
  of the recording disagree on the word she used for where the clostridial spore sits (one reads
  &ldquo;internally&rdquo;, the other &ldquo;terminally&rdquo;), so only the part both agree on is
  quoted above. The slide picture settles it.</p></div>"""))

S2.append(item(10, "w10-perfringens", "2.3", "<em>Clostridium perfringens</em> &mdash; myonecrosis (gas gangrene)", COLD,
  "“We talked about clostridium perfringens, which causes gas gangrene, the myonecrosis. And in "
  "order for that to happen, we have to have what’s called a mixed infection. What did we mean by "
  "a mixed infection? Aerobic and anaerobic. So when you get the [aerobes] in the wound, they "
  "start using up all the oxygen. And then the oxygen tension goes low enough so that those "
  "anaerobic spores can germinate.” [part 4, 13:49–14:20]",
  objmap("Answers Objective 1 and Objective 2. Appendix 2: <em>Clostridium perfringens</em> myonecrosis.") + "\n  " +
  orgtable([
    ("Disease", f"<strong>Myonecrosis</strong> (anaerobic cellulitis), or gas gangrene: soft tissue and wound infections, caused by <em>C. perfringens</em> (most common) but also <em>C. novyi</em>, <em>C. septicum</em> and other species {c10('21')}", True),
    ("Why it needs a mixed infection", f"A <strong>mixed infection</strong>: aerobic bacteria use up the oxygen to produce the low oxygen tension the organism needs (30% oxygen allows growth, 70% inhibits). 90% of contaminated wounds have the organism but only 2% develop myonecrosis &mdash; host factors decide {c10('22')}. It is not highly invasive; it needs damaged and dead tissue and anaerobic conditions, which stimulate germination, growth and exotoxin release; fermentation of muscle carbohydrates forms gas and destroys more tissue {c10('23')}", True),
    ("Virulence", f"At least 17 toxins: <strong>alpha toxin</strong> (red cell rupture, edema, tissue destruction), <strong>theta toxin</strong> (destroys white cells), and the enzymes collagenase, hyaluronidase and DNase {c10('24')} &mdash; her &ldquo;enzymes and substances&rdquo; that break down connective tissue", True),
    ("Clinical manifestations", f"<strong>Anaerobic cellulitis</strong>: gas and tissue damage that stays localized. <strong>True myonecrosis</strong>: spreading tissue damage with fever, tachycardia and blackened necrotic tissue {c10('26')}. The picture shows the rods among muscle fibers with gas-filled spaces {c10('25')}. About 1000 cases a year in the United States; mortality 20&ndash;30% if treated, 100% if untreated {c10('24')}", False),
    ("Treatment and prevention", f"Immediate cleansing of dirty wounds, deep wounds, compound fractures and infected incisions; debridement; may require amputation; large doses of cephalosporin or penicillin; <strong>hyperbaric oxygen</strong>; <strong>no vaccine</strong> {c10('27')}", False),
    ("Transmission (Objective 2)", f"Spores are found in soil, on human skin, and in the intestine and vagina {c10('21')}; predisposing wounds are surgical incisions, compound fractures, diabetic ulcers, septic abortions, puncture wounds and gunshot wounds {c10('22')}", True),
    ("Also: food poisoning", f"<em>C. perfringens</em> is the second most common form of food poisoning worldwide, a mild intestinal illness {c10('33')}: spores in meat, fish or undercooked vegetables survive inadequate cooking and multiply (especially unrefrigerated); the toxin is made in the intestine, giving abdominal pain, diarrhea and nausea, with rapid recovery {c10('41')}", False),
  ])))

S2.append(item(10, "w10-tetani", "2.4", "<em>Clostridium tetani</em> &mdash; tetanus", KNOW,
  "“We talked about clostridium [tetani] also needing that mixed infection to use up that "
  "oxygen.” [part 4, 14:42–14:45]",
  objmap("Answers Objective 1 and Objective 2. Appendix 2: <em>Clostridium tetani</em>.") + "\n  " +
  orgtable([
    ("Morphology", f"The slide&rsquo;s picture shows rods with a round spore at one end {c10('28')}", False),
    ("Disease", f"<strong>Tetanus, or lockjaw</strong>, a neuromuscular disease. Most common among geriatric patients and intravenous drug users, and in neonates in developing countries {c10('28')}; neonatal tetanus is pictured {c10('31')}", False),
    ("Oxygen", f"<strong>Strict anaerobe</strong> &mdash; low oxygen tension is needed to germinate the spores and produce toxin {c10('29')}", True),
    ("Mechanism", f"<strong>Tetanospasmin</strong>, a neurotoxin, binds motor nerve endings and blocks the release of gamma-aminobutyric acid and glycine, the transmitters that inhibit muscular contraction, so <strong>muscles contract uncontrollably</strong>. The toxin goes to the spinal neuron and blocks its regulatory function {c10('29, 30')}", False),
    ("Clinical manifestations", f"Incubation 4&ndash;10 days, and the shorter, the more serious. Death is most often from paralysis of the respiratory muscles; mortality 10&ndash;70% depending on delayed attention, short incubation and head wounds {c10('29')}", False),
    ("Treatment and prevention", f"Aimed at the degree of toxemia and infection, and at maintaining homeostasis. <strong>Antitoxin</strong> (human tetanus immune globulin) <strong>inactivates circulating toxin but does not counteract toxin already bound</strong>. Penicillin or tetracycline, and muscle relaxants. Vaccine available; <strong>booster every 10 years</strong> {c10('32')}", False),
    ("Transmission (Objective 2)", f"A common resident of soil and the gastrointestinal tracts of animals {c10('28')}; spores usually enter through accidental <strong>puncture wounds, burns, umbilical stumps, frostbite and crushed body parts</strong> {c10('29')}", False),
  ]) + "\n  " +
  differs(10, "L10 tetanus: she said C. tetani also needs a mixed infection; the tetanus slides say strict anaerobe, low oxygen tension (mixed infection is the myonecrosis slide's term)", f'''She
  said <em>C. tetani</em> also needs “that mixed infection”. The tetanus slides do not say so: they
  call it a <strong>strict anaerobe that needs low oxygen tension</strong> and list the wounds the
  spores enter {c10('29')}. &ldquo;Mixed infection&rdquo; is the deck&rsquo;s term for myonecrosis
  only {c10('22')}. If an answer choice offers &ldquo;mixed infection&rdquo; for tetanus, the slide
  does not back it.''') + f"""
  <div class="pearl"><p>Two contrasts the slides set up and an exam can use. <strong>Tetanus versus
  botulism:</strong> tetanospasmin blocks the <em>inhibitory</em> transmitters, so muscles contract
  uncontrollably {c10('29')}; botulin blocks acetylcholine, so the paralysis is flaccid
  {c10('35, 38')}. <strong>Antitoxin</strong> works on circulating toxin, not toxin already bound,
  both here and in diphtheria {c10('32, 64')}.</p></div>"""))

S2.append(item(10, "w10-botulinum", "2.5", "<em>Clostridium botulinum</em> &mdash; botulism", COLD,
  "“We talked about clostridium botulinum, botulism. When you have improperly home-canned foods or "
  "you are feeding babies improperly made foods or honey, because remember honey has the spores in "
  "it. And what do you get when a baby gets those spores? Floppy baby syndrome, yes. That’s why you "
  "don’t feed little ones honey.” [part 4, 14:54–15:24]",
  objmap("Answers Objective 1 and Objective 2. <strong>Not on the Appendix 2 list</strong>, but it "
         "is in the deck (Slides 33&ndash;40) and she reviewed it, so treat it as examinable.") + "\n  " +
  orgtable([
    ("Organism", f"A spore-forming anaerobe that commonly inhabits soil and water {c10('34')}", False),
    ("Disease", f"<strong>Botulism</strong>, an intoxication associated with inadequate food preservation; rare but severe, usually from <strong>home-canned food</strong> {c10('33, 34')}", True),
    ("Mechanism", f"Spores are on food when it is gathered and processed; if reliable temperature and pressure are not reached, the air is evacuated but the spores remain, and the anaerobic conditions favor germination and growth. The toxin, botulin, is carried to neuromuscular junctions and <strong>blocks the release of acetylcholine</strong>, which muscle contraction needs {c10('35')}", False),
    ("Clinical manifestations", f"Double or blurred vision, difficulty swallowing, dizziness; sometimes nausea and vomiting; <strong>descending muscular paralysis</strong>; respiratory compromise. Mortality has fallen to about 10% because of ventilators {c10('37')}", False),
    ("Infant botulism", f"<strong>Ingested spores</strong> germinate and release toxin: flaccid paralysis, <strong>&ldquo;floppy baby syndrome&rdquo;</strong>, which may be associated with <strong>honey or homemade baby food</strong>; up to 80% of botulism cases each year {c10('38')}. Of 273 cases reported in a 2021 national survey, 66% were infant, 24% wound and 8% food-borne {c10('39')}", True),
    ("Other forms", f"<strong>Wound botulism</strong>: spores enter a wound (intravenous drug users, often black tar heroin) {c10('38')}. <strong>Iatrogenic</strong>: cosmetic or therapeutic botulinum toxin causing systemic intoxication. <strong>Intestinal colonization</strong> in a person over 1 year old {c10('39')}", False),
    ("Laboratory, treatment, prevention", f"Determine the presence of toxin in food, intestinal contents or feces. Antitoxin, with cardiac and respiratory support; infectious botulism is treated with penicillin. Prevention: proper preserving and handling of canned foods; preservatives (sodium nitrite, salt, vinegar); discard bulging cans; boil home-bottled foods for at least 10 minutes {c10('40')}", False),
    ("Transmission (Objective 2)", f"Food-borne: preformed toxin in poorly preserved food (low-acid home-canned foods such as green beans and corn, but also meats, fish and dairy; rarely commercial foods) {c10('34')}. Infant: ingested spores. Wound: spores in a wound {c10('38')}", True),
  ]) + f"""
  <div class="pearl"><p>The distinction her honey example turns on: food-borne botulism is
  poisoning by toxin <em>already made</em> in the food {c10('33, 35')}, whereas infant botulism is
  <em>spores</em> that germinate in the baby and make the toxin there {c10('38')}.</p></div>"""))

S2.append(item(10, "w10-difficile", "2.6", "<em>Clostridioides difficile</em> &mdash; pseudomembranous colitis", COLD,
  "“And individuals who are likely to have problems with C. diff [<em>Clostridioides difficile</em>] "
  "are who? People with long-term antibiotics, which is going to wipe out the normal flora. And then "
  "you might, and if it’s a mild case, you just cut back on the antibiotics and use fluid therapy. "
  "But you may have to go to more extensive measures if it’s a more severe case. And what is a fun "
  "alternative therapy for that?” [part 4, 15:37–16:02] … “the fecal transplant” [part 4, 16:06]",
  objmap("Answers Objective 1 and Objective 2. Appendix 2: <em>Clostridioides difficile</em> "
         "pseudomembranous colitis.") + "\n  " +
  orgtable([
    ("Classification", f"Formerly classified as <em>Clostridium</em>; differentiated by RNA sequencing {c10('42')}", False),
    ("Who gets it, and why", f"A <strong>normal resident of the colon in low numbers</strong>, relatively noninvasive: <strong>treatment with broad-spectrum antibiotics kills the other bacteria, allowing it to overgrow</strong>; its enterotoxins damage the intestine {c10('42')}. 70% of cases had used antibiotics in the prior 12 weeks {c10('44')}. Populations at risk: antibiotic exposure, gastrointestinal surgery or manipulation, long stays in healthcare settings, serious underlying illness, immunocompromising conditions, advanced age, gastric acid inhibitors, and consumption of trehalose sugar {c10('45')}", True),
    ("Disease", f"<strong>Antibiotic-associated (pseudomembranous) colitis</strong>, toxic megacolon, perforation of the colon; a major cause of diarrhea in hospitals and increasingly of community-acquired diarrhea; a strain found in 2005 makes 20 times the exotoxin; named one of the top three antibiotic-related threats {c10('43')}", False),
    ("Clinical manifestations", f"Watery diarrhea, fever, loss of appetite, nausea, abdominal pain and tenderness; necrosis of the intestinal wall, which sloughs off as the pseudomembrane; perforation of the wall {c10('46')}", False),
    ("Treatment", f"<strong>Mild, uncomplicated cases: fluid and electrolyte replacement and withdrawal of antimicrobials. Severe infections: oral vancomycin or metronidazole.</strong> <strong>Fecal microbiota transplant</strong>: donor cultures by colonoscope or nasogastric tube, as much as 90% effective, or &ldquo;poop pills&rdquo; &mdash; a donor sample centrifuged into pellets and taken as capsules {c10('48')}", True),
    ("Prevention and transmission (Objective 2)", f"Increased precautions to prevent spread {c10('48')}; the organism is already a colon resident and the disease follows disruption of the flora {c10('42')}", False),
  ]) + "\n  " +
  differs(10, "L10 C. difficile: she said 'long-term antibiotics'; Slide 42 says broad-spectrum antibiotics, and antibiotics are one of eight risks on Slide 45", f'''A
  small one. She said “long-term antibiotics”; the slide&rsquo;s mechanism is
  <strong>broad-spectrum</strong> antibiotics killing the competing flora {c10('42')}, and
  antibiotic exposure is one of eight risk groups, alongside gastric acid inhibitors, advanced age
  and the rest {c10('45')}.''')))

S2.append(item(10, "w10-listeria", "2.7", "<em>Listeria monocytogenes</em> &mdash; listeriosis", COLD,
  "“Then we had listeria monocytogenes. … this one is a tough one to deal with because tough to "
  "grow because it requires what in order to grow. … This is the one that needs cold. This is the "
  "one that can grow in your refrigerator and it needs cold enrichment in order to grow. … A lot of "
  "dairy.” [part 4, 16:15–16:57]",
  objmap("Answers Objective 1 and Objective 2. Appendix 2: <em>Listeria monocytogenes</em>.") + "\n  " +
  orgtable([
    ("Morphology", f"A <strong>regular</strong> non-spore-forming Gram-positive bacillus (stains uniformly, not pleomorphic) {c10('50')}; ranges from coccobacilli to long filaments; 1&ndash;4 flagella; no capsules {c10('53')}", False),
    ("Hardiness", f"<strong>Resistant to cold, heat, salt, pH extremes and bile</strong> {c10('53')}; <strong>can contaminate foods and grow during refrigeration</strong> {c10('55')}", True),
    ("Virulence", f"Replicates in the cytoplasm of cells after inducing phagocytosis, which lets it avoid the humoral immune system {c10('53')}; its multiplication cycle is pictured {c10('54')}", False),
    ("Disease and manifestations", f"<strong>Listeriosis</strong>: often mild or subclinical in normal adults (fever, diarrhea, sore throat); in <strong>immunocompromised patients, fetuses and neonates</strong> it affects the brain and meninges, with 20% fetal loss and a 3% death rate in newborns {c10('55')}", False),
    ("Laboratory", f"<strong>Culture requires a lengthy cold enrichment process</strong>; rapid diagnostic tests use ELISA (enzyme-linked immunosorbent assay), immunofluorescence and DNA analysis {c10('56')}", True),
    ("Treatment and prevention", f"Ampicillin and trimethoprim/sulfamethoxazole, erythromycin. <strong>Prevention: pasteurization and cooking</strong> {c10('56')}", False),
    ("Transmission (Objective 2)", f"Primary reservoir soil and water, and animal intestines. Most cases are associated with <strong>dairy products</strong>, poultry and meat (found in 12% of ground beef and 15% of chicken tested); the most recent outbreak was dairy {c10('55')}; recent recalls include soft cheeses and precooked pasta meals {c10('52')}", True),
  ]) + "\n  " +
  differs(10, "L10 Listeria: she said it 'needs cold' / 'needs cold enrichment in order to grow'; Slides 53, 55, 56: resistant to cold and grows during refrigeration; cold enrichment is the lab culture method", f'''She
  said <em>Listeria</em> “needs cold” and “needs cold enrichment in order to grow”. The slides
  say something narrower: it is <strong>resistant to</strong> cold (and to heat, salt, pH extremes
  and bile) {c10('53')} and <strong>can grow during refrigeration</strong> {c10('55')}; the cold
  enrichment is how the <em>laboratory</em> cultures it {c10('56')}. Nothing on a slide says it
  requires cold. What follows for an exam: refrigeration does not stop it, so prevention is
  pasteurization and cooking {c10('56')}, and an answer choice saying it &ldquo;requires cold to
  grow&rdquo; goes beyond the slides.''')))

S2.append(item(10, "w10-diphtheriae", "2.8", "<em>Corynebacterium diphtheriae</em> &mdash; diphtheria", COLD,
  "“Then we had [Corynebacterium] diphtheria. This is one that we’re seeing more of because people "
  "are not vaccinating. And how do you diagnose diphtheria? … What is characteristic for "
  "diphtheria? The pseudomembrane, the pseudomembrane. And you may have to use antitoxin which gets "
  "rid of the toxin that’s free in the body …” [part 4, 16:59–17:33]",
  objmap("Answers Objective 1 and Objective 2. Appendix 2: <em>Corynebacterium diphtheriae</em>.") + "\n  " +
  orgtable([
    ("Morphology and group", f"An <strong>irregular</strong> non-spore-forming Gram-positive bacillus: pleomorphic, stains unevenly; the irregular group all produce catalase and have mycolic acids and a unique peptidoglycan in the wall {c10('59')}. The scheme calls it non-acid-fast {c10('5')}", False),
    ("Epidemiology", f"A reservoir of healthy carriers, so the potential is always present, but <strong>respiratory diphtheria in the United States is rare</strong>; most cases occur in <strong>non-immunized children</strong> in crowded, unsanitary conditions. Respiratory (pharyngeal, tonsillar, laryngeal, nasal) or cutaneous (most common in the tropics) {c10('61')}", False),
    ("Disease and manifestations", f"Two stages. <strong>Local infection</strong>: upper respiratory inflammation, sore throat, nausea, vomiting, swollen lymph nodes, and the <strong>pseudomembrane</strong> &mdash; formed by solidification of inflammatory fluids &mdash; which can cause asphyxiation. <strong>Diphtherotoxin and toxemia</strong>: the heart (myocarditis and an abnormal electrocardiogram) and the nerves (weakness and paralysis) {c10('62')}", True),
    ("Laboratory and diagnosis", f"<strong>The pseudomembrane and swelling are indicative</strong>; alkaline methylene blue stain; conditions and history; serological assay {c10('63')}", True),
    ("Treatment", f"<strong>Antitoxin</strong>, in horse serum since the 1890s, not typically given in non-respiratory cases; it <strong>does not neutralize bound toxin, but does neutralize circulating toxin</strong> to prevent spread. Penicillin or erythromycin {c10('64')}", True),
    ("Prevention", f"Toxoid vaccine series and boosters, in infancy, at 15 months and at school age {c10('64')}", False),
    ("Transmission (Objective 2)", f"<strong>Respiratory droplets</strong> from carriers or actively infected people {c10('61')}", False),
  ]) + "\n  " +
  aside(10, "L10 diphtheria: 'seeing more of because people are not vaccinating'", f'''Her
  opening, “we’re seeing more of because people are not vaccinating”, is not on a slide. What the
  slide says is that respiratory diphtheria is rare in the United States and that most cases occur
  in non-immunized children {c10('61')}. Her antitoxin point matches the slide: it acts on the
  free, circulating toxin, not toxin already bound {c10('64')}.''')))

S2.append(item(10, "w10-cutibacterium", "2.9", "<em>Cutibacterium</em> (<em>Propionibacterium</em>) <em>acnes</em>", KNOW,
  "“Then we have the cutibacterium, also called [Propionibacterium] acnes. This is one that we "
  "thought was just associated with acne but we now know that it can also be very serious because "
  "it has been implicated in a lot of infections associated with implants and shunts. So it’s "
  "something that we worry about more now than we used to.” [part 4, 17:39–18:04]",
  objmap("Answers Objective 1 and Objective 2. Appendix 2: <em>Propionibacterium acnes</em> (now "
         "<em>Cutibacterium</em>).") + "\n  " +
  orgtable([
    ("Morphology and oxygen", f"Gram-positive rods; aerotolerant or anaerobic; <strong>slow growing, more than 6 days</strong>; nontoxigenic {c10('65')}", False),
    ("Disease", f"A common resident of the pilosebaceous glands that causes <strong>acne</strong> through inflammatory mediators {c10('65')}; more recently implicated in chronic invasive, <strong>implant</strong>, endovascular and central nervous system <strong>shunt</strong> infections {c10('66')}", True),
    ("Why it is hard", f"It forms a <strong>biofilm on prosthetics</strong>, which increases its tolerance to antibiotics and immune defense; it is difficult to diagnose because it grows so slowly, so prolonged incubation under strict anaerobic conditions is needed {c10('66')}", False),
    ("Treatment", f"Hardware may need to be removed and the area aggressively debrided; prolonged courses of antibiotics, often months, including weeks of an intravenous beta-lactam {c10('66')}", False),
    ("Transmission (Objective 2)", f"The slides give no route beyond its home on the skin, in the pilosebaceous glands {c10('65')}", False),
  ])))

S2.append(item(10, "w10-tb", "2.10", "<em>Mycobacterium tuberculosis</em> &mdash; the stages of tuberculosis", KNOW,
  "“Mycobacterium, the acid fast organisms. Mycobacterium tuberculosis. We’ve talked about the "
  "different stages of tuberculosis. Go review your stages of tuberculosis.” [part 4, 18:06–18:17]",
  objmap("Answers Objective 1 and Objective 2. Appendix 2: Tuberculosis.") + "\n  " +
  f"""<p>&ldquo;Go review&rdquo; is a direct instruction, but she did not put it to the room as a
  question, so by this page&rsquo;s rule it is Know it &mdash; weight it at the top of that tier.
  The stages are the answer she pointed at.</p>
  <table>
    <tr><th>Stage</th><th>What the slides say</th></tr>
    <tr><td><strong>Course of infection</strong></td><td><strong>5&ndash;10% of infected people develop clinical disease.</strong> <strong>Inactive</strong> tuberculosis is not contagious, can be detected by a blood or skin test, and may activate at any time. Untreated, the disease progresses slowly, and most cases are contained in the lungs. Clinical tuberculosis divides into primary, secondary (reactivation or reinfection), and disseminated (extrapulmonary) {c10('72')}</td></tr>
    <tr><td><strong><mark class="prof-highlight">Primary</mark></strong></td><td>Infectious dose 10 cells. Phagocytosed by alveolar macrophages, it multiplies inside them. After 3&ndash;4 weeks the immune system attacks, forming <strong>tubercles</strong>: granulomas of a central core of bacilli surrounded by white cells. If the center breaks down into necrotic <strong>caseous</strong> lesions, they gradually heal by <strong>calcification</strong>. Stimulates a cell-mediated response {c10('73')}</td></tr>
    <tr><td><strong><mark class="prof-highlight">Secondary</mark></strong> (reactivation or reinfection)</td><td>If the patient does not recover from primary tuberculosis, the bacilli can reactivate; tubercles expand and drain into the bronchial tubes and upper respiratory tract. Violent coughing, greenish or bloody sputum, fever, anorexia, weight loss and fatigue (&ldquo;consumption&rdquo;); untreated, 60% mortality {c10('74')}</td></tr>
    <tr><td><strong><mark class="prof-highlight">Extrapulmonary</mark></strong> (disseminated)</td><td>During secondary tuberculosis the bacilli disseminate to the regional lymph nodes, kidneys, long bones, genital tract, brain and meninges; tuberculosis of the meninges carries 30&ndash;50% mortality even when treated {c10('75')}</td></tr>
  </table>
  """ +
  orgtable([
    ("Genus", f"Gram-positive irregular bacilli; <strong>acid-fast</strong>; mycolic acids and waxes in the wall; <strong>strict aerobes</strong>; produce catalase; no capsules, flagella or spores; grow slowly. Nontuberculous mycobacteria are a problem in immunosuppressed patients {c10('67')}", True),
    ("Virulence", f"The tubercle bacillus makes no exotoxins or enzymes that contribute to infectiousness; its complex waxes and <strong>cord factor</strong> prevent destruction by lysosomes or macrophages {c10('70')}", False),
    ("Epidemiology", f"Predisposing factors: inadequate nutrition, a debilitated immune system, poor access to care, lung damage, genetics. An estimated one third of the world and 15 million in the United States carry it; the highest United States rate is in recent immigrants {c10('71')}", False),
    ("Laboratory and diagnosis", f"<strong>Mantoux test</strong>: intradermal purified protein derivative, read for a red wheal (induration) at 48&ndash;72 hours. <strong>QuantiFERON-TB Gold</strong>: blood incubated with mycobacterial proteins, measuring the release of gamma interferon. False positives from the bacillus Calmette&ndash;Gu&eacute;rin vaccine or other <em>Mycobacterium</em> species; false negatives too early in infection or in immunosuppressed patients {c10('76')}. Acid-fast staining of sputum (Ziehl&ndash;Neelsen, fluorescent), culture, DNA probes {c10('77')}", False),
    ("Treatment and prevention", f"6&ndash;24 months of at least two drugs from isoniazid, rifampin, ethambutol, streptomycin, pyrazinamide, thioacetazone and para-aminosalicylic acid; a one-pill combination of isoniazid, rifampin and pyrazinamide. A vaccine from the attenuated Calmette&ndash;Gu&eacute;rin strain of <em>M. bovis</em> is used in other countries. Preventive treatment for those at risk or possibly latent: 9 months of isoniazid or 4 months of rifampin {c10('79')}", False),
    ("Transmission (Objective 2)", f"<strong>Airborne respiratory droplets</strong>; the bacillus is very resistant {c10('71')}", False),
  ])))

S2.append(item(10, "w10-leprae", "2.11", "<em>Mycobacterium leprae</em> &mdash; leprosy", COLD,
  "“And then mycobacterium leprae, that’s your armadillos. … And remember it comes in two "
  "different forms, the tuberculoid form which is a little less serious and then the lepromatous "
  "which … the major disfiguration” [part 4, 18:24–18:36] … “in areas where we do not have a lot of "
  "healthcare … diagnose the leprosy … The feather test” [part 4, 18:43–18:53]",
  objmap("Answers Objective 1 and Objective 2. Appendix 2 lists Tuberculosis; <em>M. leprae</em> is "
         "on the deck&rsquo;s own organism list (Slide 3).") + "\n  " +
  orgtable([
    ("Organism", f"Hansen&rsquo;s bacillus (Hansen&rsquo;s disease). A strict parasite that <strong>has not been grown on artificial media or tissue culture</strong> &mdash; it is grown in armadillos. The slowest growing of all species; multiplies within host cells in large packets called globi {c10('80')}", True),
    ("Disease", f"<strong>Leprosy</strong>, a chronic disease that begins in the skin and mucous membranes and progresses into the nerves {c10('80')}. Macrophages phagocytize the bacilli, but a weakened macrophage or slow T cell response may not kill them; incubation 2&ndash;5 years; untreated, the bacilli grow slowly in skin macrophages and the Schwann cells of peripheral nerves {c10('83')}", False),
    ("The two forms", f"<strong>Tuberculoid</strong>: asymmetrical, shallow lesions that damage nerves, giving <strong>local loss of pain reception</strong>. <strong>Lepromatous</strong>: a deeply nodular infection causing <strong>severe disfigurement of the face and extremities</strong>, with widespread dissemination {c10('83')}. Which form develops seems to depend on the T helper response: <strong>T helper 1 favors tuberculoid, T helper 2 favors lepromatous</strong> {c10('84')}; both are pictured {c10('85, 86')}", True),
    ("Diagnosis", f"Symptoms, microscopic examination of lesions and history: numbness in the hands and feet, loss of heat and cold sensitivity, muscle weakness, thickened earlobes, chronic stuffy nose; acid-fast bacilli in skin lesions, nasal discharges and tissue samples {c10('87')}. The <strong>feather test</strong> is named and pictured: a feather touched to the skin {c10('88')}, which checks for the lost sensation on Slides 83 and 87", True),
    ("Treatment and prevention", f"Long-term combined therapy: tuberculoid, rifampin and dapsone for 6 months; lepromatous, rifampin, dapsone and clofazimine for up to 2 years, then dapsone. Prevention needs constant surveillance of high-risk populations; the bacillus Calmette&ndash;Gu&eacute;rin vaccine has limited efficacy, and a defined subunit vaccine is in trials {c10('89')}", False),
    ("Transmission (Objective 2)", f"<strong>The mechanism of transmission is not fully verified</strong>; there is a <strong>possibility of zoonotic transmission from armadillos</strong>. Not highly virulent; health and living conditions influence susceptibility. Most Florida cases are in Central Florida, along the Interstate 4 corridor {c10('82')}", True),
  ]) + "\n  " +
  differs(10, "L10 leprosy: 'that's your armadillos'; Slides 80, 82: armadillos are where it is grown and a possible zoonotic source; transmission not fully verified", f'''Her
  shorthand “that’s your armadillos” is true in two narrower senses on the slides: armadillos are
  where it is grown, since it will not grow on artificial media {c10('80')}, and zoonotic
  transmission from armadillos is a <em>possibility</em>, with the mechanism of transmission
  <strong>not fully verified</strong> {c10('82')}. Her ranking of the forms (tuberculoid less
  serious) fits the slide&rsquo;s descriptions, though the slide does not rank them.''') + "\n  " +
  aside(10, "L10 leprosy: the feather test is used 'in areas where we do not have a lot of healthcare'", '''The
  setting she gave for the feather test, areas without much healthcare, is not on the slide;
  Slide 88 names the test and pictures it.''')))

S2.append(item(10, "w10-actinomyces", "2.12", "<em>Actinomyces israelii</em> &mdash; actinomycosis", KNOW,
  "“And then we talked about actinomyces israelii and this is one that is normally harmless in the "
  "[oral] cavity but if you happen to get exposed to it through a penetrating wound where it’s not "
  "supposed to be, then you could be dealing with much more serious problems. If it gets in the gut, "
  "… cause appendicitis …” [part 4, 18:56–19:26]",
  objmap("Answers Objective 1 and Objective 2. Appendix 2: <em>Actinomyces israelii</em>.") + "\n  " +
  orgtable([
    ("Morphology", f"Actinomycetes: <em>Actinomyces</em> and <em>Nocardia</em> are <strong>nonmotile filamentous bacteria related to the mycobacteria</strong> that may cause chronic infection of skin and soft tissue {c10('92')}; the scheme lists them as filamentous, branching cells {c10('5')}", False),
    ("Disease", f"A <strong>normally harmless resident of the oral cavity, digestive tract and genital tract</strong> that can cause chronic, hard-to-diagnose infections <strong>if it gains access to deeper tissues</strong> {c10('93')}", True),
    ("Clinical manifestations", f"<strong>Cervicofacial</strong> disease, a complication of oral infection; <strong>thoracic</strong> actinomycosis, a necrotizing lung disorder; <strong>abdominal</strong> actinomycosis, a complication of a burst appendix, gunshot wounds or ulcers; <strong>uterine</strong> actinomycosis, a complication of intrauterine devices. <em>Actinomyces viscosus</em> causes dental caries and is associated with some endocarditis {c10('93')}", True),
    ("Treatment", f"Surgically, and with penicillin, erythromycin or sulfonamides {c10('93')}", False),
    ("Transmission (Objective 2)", f"From the body&rsquo;s own flora, when the organism reaches deeper tissue {c10('93')}", True),
  ]) + "\n  " +
  differs(10, "L10 Actinomyces: she said 'if it gets in the gut ... cause appendicitis'; Slide 93: abdominal actinomycosis is a complication OF a burst appendix", f'''Her
  direction is reversed. She said that if it gets into the gut it can cause appendicitis; the slide
  lists <strong>abdominal actinomycosis as a complication of a burst appendix</strong> (and of
  gunshot wounds and ulcers) {c10('93')}. The burst appendix is how a normally harmless resident
  reaches deeper tissue, not a disease the organism causes.''')))

S2.append(item(10, "w10-nocardia", "2.13", "<em>Nocardia</em> &mdash; nocardiosis", KNOW,
  "She did not mention <em>Nocardia</em> in the review. It is the last organism on the Appendix 2 "
  "list and the last slide of the deck, and her walk ended at <em>Actinomyces</em>.",
  objmap("Answers Objective 1. Appendix 2: <em>Nocardia</em>.") + "\n  " +
  gap(10, "L10: Nocardia (Appendix 2; Slides 92, 94) not mentioned", '''An Appendix 2 organism
  her walk left out. Two slides cover it.''') + "\n  " +
  orgtable([
    ("Morphology", f"A nonmotile filamentous bacterium related to the mycobacteria {c10('92')}", False),
    ("Disease and manifestations", f"<strong>Pulmonary, cutaneous or subcutaneous infections</strong>. <em>Nocardia brasiliensis</em> causes a <strong>pulmonary disease similar to tuberculosis</strong>, whose lesions may extend through the chest wall and disseminate to the brain and kidneys. Also involved in <strong>mycetoma</strong>, a granulomatous inflammatory response in the deep dermis and subcutaneous tissue {c10('94')}", False),
    ("Treatment", f"Often treated with cephalosporins {c10('94')}", False),
    ("Transmission (Objective 2)", f"No route is given on the slides {c10('94')}", False),
  ])))

S2.append(item(10, "w10-transmission", "2.14", "Objective 2 &mdash; How humans acquire them", KNOW,
  "She did not take this objective on its own. Some routes came up inside her organism walk: "
  "wounds for gas gangrene, home-canned food and honey for botulism, food in the refrigerator for "
  "<em>Listeria</em>, and a penetrating wound for <em>Actinomyces</em>.",
  gap(10, "L10 objective 2 (modes of transmission) never addressed as such", '''Objective 2
  stands on its own on the syllabus, and her organism walk only touched it. Here it is in one place,
  from the slides.''') + f"""
  <table>
    <tr><th>Organism</th><th>How humans acquire it</th></tr>
    <tr><td><em>Bacillus anthracis</em></td><td>A zoonosis {c10('8')}: spores through cuts or incisions (cutaneous) {c10('10')}; injected heroin (injection) {c10('12')}; inhaled spores from infected animal products or soil (pulmonary) {c10('13')}; contaminated meat (gastrointestinal) {c10('14')}</td></tr>
    <tr><td><em>Clostridium perfringens</em></td><td>Spores from soil, skin, intestine or vagina in a wound {c10('21, 22')}; spores surviving undercooking in food {c10('41')}</td></tr>
    <tr><td><em>Clostridium tetani</em></td><td>Spores from soil or animal gastrointestinal tracts entering puncture wounds, burns, umbilical stumps, frostbite or crushed body parts {c10('28, 29')}</td></tr>
    <tr><td><em>Clostridium botulinum</em></td><td>Preformed toxin in poorly preserved food; ingested spores (infants: honey, homemade baby food); spores in a wound {c10('34, 38')}</td></tr>
    <tr><td><em>Clostridioides difficile</em></td><td>Already a colon resident; disease follows broad-spectrum antibiotics; precautions against spread {c10('42, 48')}</td></tr>
    <tr><td><em>Listeria monocytogenes</em></td><td>Soil, water and animal intestines; contaminated food that grows during refrigeration &mdash; dairy, poultry, meat {c10('55')}</td></tr>
    <tr><td><em>Corynebacterium diphtheriae</em></td><td>Respiratory droplets from carriers or actively infected people {c10('61')}</td></tr>
    <tr><td><em>Cutibacterium acnes</em></td><td>A skin resident (pilosebaceous glands); no route given {c10('65')}</td></tr>
    <tr><td><em>Mycobacterium tuberculosis</em></td><td>Airborne respiratory droplets {c10('71')}</td></tr>
    <tr><td><em>Mycobacterium leprae</em></td><td>Not fully verified; possibly zoonotic from armadillos {c10('82')}</td></tr>
    <tr><td><em>Actinomyces israelii</em></td><td>The body&rsquo;s own flora reaching deeper tissue {c10('93')}</td></tr>
    <tr><td><em>Nocardia</em></td><td>No route given {c10('94')}</td></tr>
  </table>"""))

# --------------------------------------------------------------------------
# Section 3 -- Lecture 12, Epidemiology (her closing list, plus the lecture's own flags)
# --------------------------------------------------------------------------
IO12 = [
    "Distinguish between descriptive and analytic epidemiology.",
    "Describe the specific uses for epidemiology training.",
    "Describe key events in the history and development of epidemiology, including genomic epidemiology",
    "Identify common sources of epidemiologic data.",
    "Define the primary components of public health surveillance.",
    "Define reportable disease",
    "Describe selected measures of morbidity and mortality.",
    "Distinguish between the terms association and causation.",
    "Define the terms endemic, epidemic, pandemic, sporadic, and herd immunity.",
    "Compare and contrast applications of epidemiology, including policy development, outbreak "
    "investigation, social and behavioral issues, the environment and occupational health",
]

S3 = []

S3.append(item(12, "w12-descriptive", "3.1", "Objective 1 &mdash; Descriptive versus analytic epidemiology", COLD,
  "“So you need to know that difference between descriptive and analytic, those different "
  "factors.” [part 4, 19:38–19:41]",
  f"""<p>The one Lecture 12 item she said “need to know” about twice, once in the lecture and once
  in the review. “The basic components” are the two triads.</p>
  <table>
    <tr><th></th><th>Descriptive epidemiology</th><th>Analytic epidemiology</th></tr>
    <tr><td><strong>What it does</strong></td><td>Examines the distribution of a disease in a population and its basic features in terms of <strong>time, place and person</strong>; formulates hypotheses and examines associations</td><td><strong>Tests a specific hypothesis</strong> about the relationship of a disease to a specific cause, relating the exposure of interest to the outcome of interest; a <strong>cause-effect</strong> relationship</td></tr>
    <tr><td><strong>Typical designs</strong></td><td>Community health survey (also called cross-sectional or descriptive studies)</td><td><strong>Cohort, case-control, experimental</strong></td></tr>
    <tr><td><strong>Its triad</strong></td><td><strong>Person, place, time</strong> {c12('33')}</td><td><strong>Host, environment, agent</strong> {c12('37')}</td></tr>
  </table>
  <p>{c12('32')} Before any analytic study, the descriptive components have to be understood first.
  {c12('33')}</p>

  <h4 class="subsub">The components</h4>
  <ul>
    <li><strong>Person</strong> &mdash; age, gender, socioeconomic status (education, occupation, income), marital status, ethnicity, race or genetic profile, behavior and habits. {c12('34')}</li>
    <li><strong>Place</strong> &mdash; geographically restricted or widespread (outbreak, epidemic, pandemic); climate effects; urban, suburban or rural; relation to environmental exposure (water, food supply); one cluster or several. {c12('35')}</li>
    <li><strong>Time</strong> &mdash; changing or stable; clustered (epidemic) or evenly distributed (endemic); time trends: point source (localized and stationary), propagated (spreading, may be extended), seasonal, and secular (over a prolonged period, usually years). {c12('36')}</li>
    <li><strong>Agent</strong> &mdash; biological (microorganisms), physical (temperature, radiation, trauma), chemical (acids, alkalis, poisons, tobacco), environmental (nutrients, allergens), psychological experiences. {c12('38')}</li>
    <li><strong>Host</strong> &mdash; genetic endowment, immunologic status, personal characteristics, personal behavior, and definitive versus intermediate host in vector-borne disease. {c12('39')}</li>
    <li><strong>Environment</strong> &mdash; living conditions (housing, crowding, water supply, refuse, sewage), atmosphere and climate, and the modes of communication that bring host and agent together: vector, vehicle, reservoir. {c12('40')}</li>
  </ul>

  <h4 class="subsub">The worked example: John Snow and cholera</h4>
  <p><strong>Descriptive:</strong> during the Golden Square outbreak in London he marked where
  cholera cases lived and worked on a map (now called a spot map) along with the water pumps, found
  more cases near Pump A, questioned residents about their pump, noted few cases near a brewery with
  its own deep well, and found the common factor was Pump A; the pump was closed and the outbreak
  ended. {c12('41')} <strong>Analytic:</strong> re-examining data from different outbreaks, he
  found the highest death rates in districts served by the Lambeth and Southwark/Vauxhall companies,
  both drawing water downstream of London; after Lambeth moved its intake upstream in 1852 he
  hypothesized that water from below London was the source, and tested it by identifying the water
  source of every house with a cholera death. Without any knowledge of microbes &mdash; Koch&rsquo;s
  postulates came in 1884 &mdash; he established that water could transmit cholera. {c12('42')}</p>""",
  lecture="“you need to know the basic components of descriptive epidemiology versus analytic "
          "epidemiology.” [part 2, 6:51]"))

S3.append(item(12, "w12-uses", "3.2", "Objective 2 &mdash; The uses of epidemiology training", KNOW,
  "She did not mention this objective in the review; her closing list went from descriptive versus "
  "analytic straight to history.",
  gap(12, "L12 objective 2: uses of epidemiology training (Slides 7-8) not in her closing list", f'''Still
  an objective, answered by two slides. {c12('7, 8')}''') + f"""
  <p><strong>What epidemiology is:</strong> <em>epi</em> (upon), <em>demos</em> (people),
  <em>ology</em> (science) &mdash; the science of what falls upon people, a bridge between the
  biomedical, social and behavioral sciences {c12('4')}; the study of the occurrence and
  distribution of health-related diseases or events in specified populations, of their
  determinants, and the application of that knowledge to control the problem. The five W&rsquo;s
  frame every study: what (the health event or diagnosis), who, where, when, and why (causes, risk
  factors, modes of transmission). {c12('5')}</p>
  <table>
    <tr><th>Use of epidemiology training</th><th>What it involves</th></tr>
    <tr><td>Outbreak response</td><td>Identifying, reporting and investigating outbreaks in a timely manner</td></tr>
    <tr><td>Public health surveillance</td><td>Setting up, managing and evaluating surveillance systems</td></tr>
    <tr><td>Public health communication</td><td>Developing and delivering public health communications</td></tr>
    <tr><td>Disease prioritization</td><td>Evaluating and prioritizing diseases of concern, including the clinical picture: who gets the disease, who dies from it, what the outcome is</td></tr>
    <tr><td>Training and mentoring</td><td>Of health professionals</td></tr>
    <tr><td>Experimental epidemiology</td><td>Developing a hypothesis for a health concern and designing an experimental model to test it</td></tr>
    <tr><td>Program evaluation and management</td><td>Evaluating prevention and intervention programs, such as vaccine and clinical trials, and managing their staff and resources</td></tr>
  </table>
  <p>{c12('7, 8')} Its impacts reach public health (disease prevention), clinical medicine
  (classification and diagnosis), pathophysiology (biological mechanisms), biostatistics
  (quantifying disease frequency) and the social sciences (social context). {c12('6')}</p>"""))

S3.append(item(12, "w12-history", "3.3", "Objective 3 &mdash; History, including genomic epidemiology", COLD,
  "“Go back and look at the history and the people who are important in history that I mentioned "
  "a few times.” [part 4, 19:45–19:49]",
  f"""<p>Two halves with two weights. The history is a &ldquo;go back and look&rdquo;; genomic
  epidemiology is a &ldquo;need to know&rdquo; from the lecture, which is what puts the item in
  Know cold.</p>
  <table>
    <tr><th>Who or when</th><th>What for</th></tr>
    <tr><td><strong>Hippocrates</strong>, 400 BC</td><td>Attempted to explain disease from a rational rather than spiritual standpoint &mdash; environmental and host factors</td></tr>
    <tr><td><strong>John Graunt</strong>, 17th century</td><td>Pioneered tabulating population health and mortality in rates, ratios and proportions; noted disparities between males and females, high infant mortality, urban and rural differences, and seasonal variation</td></tr>
    <tr><td><strong>William Farr</strong>, 1800s</td><td>Systematically collected and analyzed Britain&rsquo;s mortality statistics; the <strong>father of modern vital statistics</strong>; developed life tables; reported to the authorities and the public</td></tr>
    <tr><td><strong>John Snow</strong>, mid-1800s</td><td>An anesthesiologist who used epidemiologic approaches on the London cholera epidemic; the <strong>father of field epidemiology</strong>; his studies show the method still used: descriptive and analytic epidemiology</td></tr>
    <tr><td>Mid to late 1800s; 1930s&ndash;1940s</td><td>A focus on acute infectious diseases; then methods extended to noninfectious diseases, with research methods developing after World War II</td></tr>
    <tr><td><strong>Doll and Hill</strong>, 1950</td><td>Smoking and lung cancer</td></tr>
    <tr><td><strong>Framingham Heart Study</strong>, from 1948</td><td>A multigenerational study of the common factors contributing to cardiovascular disease</td></tr>
    <tr><td>1960s&ndash;1970s; 1980s</td><td>Epidemiological methods used to eradicate smallpox worldwide; then extended to injuries and violence</td></tr>
    <tr><td>1990s, accelerating after 2001</td><td>Deliberate spread of disease: biological warfare and bioterrorism</td></tr>
    <tr><td>Continuing</td><td>New infectious agents (Ebola virus, human immunodeficiency virus, severe acute respiratory syndrome, COVID) and changed ones (drug-resistant tuberculosis, influenza variants)</td></tr>
  </table>
  <p>{c12('9&ndash;12')} The person the deck comes back to most is John Snow, three times
  {c12('11, 41, 42')}.</p>

  {flag(f'''<p><strong>Genomic epidemiology</strong>, in her words in the lecture “the really best
  tool we have now” [part 3, 24:00]. The deck calls its advent <strong>one of the most important
  developments in epidemiology</strong> and one of the most reliable tools in outbreak
  investigation {c12('12')}. What it is: monitoring the <strong>genetic makeup of pathogens</strong>,
  made possible by advances in sequencing. Its applications to public health:</p>
  <ul>
    <li><strong>Early outbreak detection and investigation</strong> &mdash; if the pathogens in different cases are closely related, they may be part of the same outbreak;</li>
    <li><strong>Identify transmission links</strong> &mdash; a common pathway of spread;</li>
    <li><strong>Identify or confirm sources of exposure</strong>;</li>
    <li><strong>Link cases or outbreaks in different locations</strong>, by understanding disease location and spatial distribution.</li>
  </ul>
  <p>Applying this information can help control health problems. {c12('69')}</p>''')}

  {light(12, "L12 Slide 13 graph (genetic susceptibility to cancer over the lifespan)",
         "The Slide 13 graph",
         "“This particular graph, which I’m not asking you to memorize, looks at genetic "
         "susceptibility to cancer over a lifespan” [part 1, 11:25]",
         f'''<p>The slide&rsquo;s point is the sentence, not the curve: epidemiological studies
  can impact personal health, through data on what affects long-term health, as well as public
  health. {c12('13')}</p>''')}""",
  lecture="“You need to know genomic epidemiology.” [part 3, 24:46]"))

S3.append(item(12, "w12-sources", "3.4", "Objective 4 &mdash; Common sources of epidemiologic data", KNOW,
  "She did not mention this objective in the review.",
  gap(12, "L12 objective 4: sources of epidemiologic data (Slide 18) not in her closing list", f'''One
  table answers it. {c12('18')}''') + f"""
  <table>
    <tr><th>Source</th><th>Method</th><th>Example</th></tr>
    <tr><td><strong>Individual persons</strong></td><td>Questionnaire, survey</td><td>A food-borne illness outbreak; the National Health and Nutrition Examination Survey of the CDC (Centers for Disease Control and Prevention), health data on United States residents</td></tr>
    <tr><td><strong>Environment</strong></td><td>Samples from the environment (river water, soil); sensors for environmental change</td><td>Water from area streams checked for chemical pollutants; air-quality ratings</td></tr>
    <tr><td><strong>Health care providers</strong></td><td>Notifications to the health department when cases of certain diseases are seen</td><td>Reporting cases of meningitis</td></tr>
    <tr><td><strong>Nonhealth-related sources</strong> (financial, legal)</td><td>Sales records, court records</td><td>Cigarette sales; intoxicated driver arrests</td></tr>
  </table>
  <p>{c12('18')} Social media can also be a valuable source for monitoring disease outbreaks and
  mental health issues. {c12('20')}</p>"""))

S3.append(item(12, "w12-surveillance", "3.5", "Objective 5 &mdash; Public health surveillance", KNOW,
  "“Public health surveillance, the different kinds of surveillances that we talked about.” "
  "[part 4, 19:52–19:54]",
  f"""<p>She named the kinds of surveillance specifically, so the table of kinds is the part to have
  firm.</p>
  <p><strong>What it is:</strong> a tool that systematically collects, analyzes and interprets data
  to facilitate the prevention and control of disease. It measures what is going on in the
  population, the need for interventions, and their effects, and informs decisions; how it is done
  may differ between developed and developing nations. {c12('14')}</p>
  <p><strong>The critical characteristics</strong>, once there is a clear objective for how data
  will be collected, consolidated and analyzed: <strong>timeliness</strong> (to implement control
  measures), <strong>representation</strong> (an accurate picture of the temporal trend),
  <strong>sensitivity</strong> (identifying individual persons with disease, for treatment or
  quarantine) and <strong>specificity</strong> (excluding persons without it). {c12('15')} The
  considerations for setting it up run from the case definition and the purpose to the legal
  authority, data sources, frequency, population, confidentiality, analysis and dissemination.
  {c12('16, 17')}</p>
  <p><strong>Case surveillance</strong> is foundational: local and state public health departments
  collect data about a case or person with a disease or condition that poses a serious threat
  (infectious diseases, food-borne outbreaks, noninfectious conditions like lead poisoning); if it is
  notifiable, it is reported to the CDC. An <strong>indicator</strong> is a measurable factor used to
  estimate the size of a problem and the effects of interventions. {c12('19')}</p>
  <table>
    <tr><th>Kind of surveillance</th><th>How it works</th><th>Trade-off</th></tr>
    <tr><td><strong>Active</strong></td><td>Staff regularly contact health care providers for data; often for specific purposes such as outbreaks or seasonal events</td><td><strong>Most accurate, but most expensive</strong></td></tr>
    <tr><td><strong>Passive</strong></td><td>Relies on reports submitted by health care facilities and providers (including routine health information systems)</td><td><strong>Most common</strong>, but less comprehensive; data quality is hard to control and it may lead to under-reporting</td></tr>
    <tr><td><strong>Sentinel</strong></td><td>A prearranged group of reporting sources, normally providers, agrees to report all cases of specific conditions; a smaller representative group tracking on behalf of a much larger population</td><td>Trying to get ahead of an outbreak</td></tr>
    <tr><td><strong>Syndromic</strong></td><td>Active or passive, with case definitions based <strong>entirely on clinical features</strong> (diarrhea instead of cholera, for example)</td><td><strong>Most frequently found in developing countries</strong></td></tr>
  </table>
  <p>{c12('19, 20')}</p>

  {light(12, "L12 Slide 25 list (uses of surveillance data)",
         "The Slide 25 list of uses of surveillance data",
         "“I don’t want you to memorize this list.” [part 1, 29:10]",
         f'''<p>Read it for the shape: surveillance data are used for immediate detection (of
  epidemics, newly emerging problems, changes in practice and resistance), for periodic
  dissemination (magnitude and cost, control activities, risk factors, planning) and as stored
  information (natural history, research). {c12('25')}</p>''')}"""))

S3.append(item(12, "w12-reportable", "3.6", "Objective 6 &mdash; Reportable disease", KNOW,
  "She did not mention this objective in the review.",
  gap(12, "L12 objective 6: definition of reportable disease (Slides 21-22) not in her closing list; only the Slide 23 list was waved off", f'''She
  told the class in the lecture not to pay attention to the long list of notifiable diseases (below),
  but the objective asks for the <em>definition</em>, and that is short. Do not let the one
  instruction swallow the other. {c12('21, 22')}''') + f"""
  <p><strong>A reportable (notifiable) disease is any disease that is required by law to be
  reported to government authorities.</strong> They are of public interest by reason of their
  <strong>contagiousness, severity or frequency</strong>: infectious diseases, bioterrorism agents,
  sexually transmitted diseases, and noninfectious conditions. Collecting the data lets authorities
  monitor the disease and gives early warning of outbreaks. In the United States collection is done
  through the CDC&rsquo;s National Notifiable Diseases Surveillance System. {c12('21')}</p>
  <table>
    <tr><th>Group of reportable disease</th><th>Slide&rsquo;s examples</th></tr>
    <tr><td>Mandatory written report</td><td>Gonorrhea, salmonellosis</td></tr>
    <tr><td>Mandatory report by telephone</td><td>Rubeola, pertussis</td></tr>
    <tr><td>Report of total number of cases</td><td>Chickenpox, influenza</td></tr>
    <tr><td>Cancer</td><td>Reported to state cancer registries</td></tr>
  </table>
  <p>A list of notifiable diseases is produced every year. {c12('22')}</p>

  {light(12, "L12 Slide 23 list (the notifiable diseases)",
         "The Slide 23 list of notifiable diseases",
         "“Here’s a list I’m absolutely not requiring you to pay attention to” [part 1, 27:48]",
         f'''<p>The full current list of notifiable diseases, from anthrax to Zika. {c12('23')}</p>''')}"""))

S3.append(item(12, "w12-measures", "3.7", "Objective 7 &mdash; Measures of morbidity and mortality", COLD,
  "“The different measures of morbidity and mortality.” [part 4, 19:58]",
  f"""<p>The review only named this objective; the lecture is where she said what to know, and it
  was the incidence-prevalence distinction.</p>
  <p><strong>Morbidity</strong> refers to having a disease or symptom of disease, the level of
  disease in a population, or sometimes the risk of a disease; it is measured by
  <strong>incidence</strong> and <strong>prevalence</strong>. <strong>Mortality</strong> is the
  death rate, the number of deaths in a group at a particular time, referenced by age, sex or cause.
  {c12('26')}</p>
  {flag(f'''<table>
    <tr><th></th><th>Incidence &mdash; the speedometer</th><th>Prevalence &mdash; the odometer</th></tr>
    <tr><td><strong>Definition</strong></td><td>The proportion or rate of persons who <strong>develop</strong> a condition during a particular time period</td><td>The proportion of persons who <strong>have</strong> a condition at or during a particular time period</td></tr>
    <tr><td><strong>Numerator</strong></td><td><strong>New cases</strong> that occurred during the period</td><td><strong>All cases present</strong> during the period</td></tr>
  </table>
  <p>Prevalence depends on <strong>both incidence and duration</strong>. High prevalence may reflect
  high incidence, or prolonged survival without cure, or both; low prevalence may mean low incidence,
  a rapidly fatal process, or rapid recovery. Prevalence rather than incidence is often measured for
  chronic diseases such as diabetes or osteoarthritis, which last long and have onsets that are hard
  to pinpoint. {c12('27')}</p>
  <p><strong>The slide&rsquo;s own test, worked.</strong> &ldquo;Number of women reported with heart
  disease in Town A in a recent health survey, over the number of women residents of Town A&rdquo;
  counts everyone who <em>has</em> it &mdash; <strong>prevalence</strong>. &ldquo;Number of women
  newly diagnosed with heart disease in 2020, over the number of women residents on 1 July
  2020&rdquo; counts <em>new</em> cases in a period &mdash; <strong>incidence</strong>.
  {c12('27, 28')}</p>''')}
  <table>
    <tr><th>Mortality rate</th><th>What it counts</th></tr>
    <tr><td>Crude</td><td>Deaths from all causes in a population in a given time period</td></tr>
    <tr><td>Cause-specific</td><td>Deaths from a specific cause in a population</td></tr>
    <tr><td>Age-specific</td><td>Deaths in a specific age group</td></tr>
    <tr><td>Infant</td><td>Infant deaths; used to compare health status between countries. The United States ranks 54th worldwide, much higher than most other developed nations, with considerable disparities by race and socioeconomic status</td></tr>
    <tr><td>Maternal</td><td>Mortality associated with pregnancy</td></tr>
  </table>
  <p>{c12('29')} The <strong>case fatality rate</strong> is deaths over total cases; it may be
  overestimated at first, when the sickest cases are the ones hospitalized, and then underestimated
  as testing of mild cases increases. {c12('59')}</p>""",
  lecture="“You should know the difference between incidence and prevalence.” [part 1, 30:33]"))

S3.append(item(12, "w12-causation", "3.8", "Objective 8 &mdash; Association versus causation", COLD,
  "“Association and causation, the [Hill’s] criteria.” [part 4, 20:04]",
  f"""<p>In the lecture she described the exact form of question to expect: a scenario, and a
  judgment on whether it shows association or causation.</p>
  <table>
    <tr><th>Association</th><th>Causation</th></tr>
    <tr><td>An identifiable relationship between an exposure and a disease. It <strong>implies that the exposure might cause the disease</strong>; exposures associated with a difference in disease risk are often called <strong>risk factors</strong>. Most often, public health interventions are designed on associations</td>
        <td>Implies there is a <strong>true mechanism</strong> leading from exposure to disease. <strong>Finding an association does not make it causal</strong></td></tr>
  </table>
  <p>Epidemiology does not determine the cause of a disease in a given individual; it determines the
  relationship between an exposure and the frequency of disease in populations, and causation is
  <em>inferred</em> from association and other factors. {c12('43')} An association can be due to
  chance, be spurious (an artifact), be confounded, be non-causal, or be causal {c12('44')}. A cause
  is an event or condition that plays a role in producing a disease, and most diseases come from an
  interplay of factors, not one. {c12('45')}</p>
  <table>
    <tr><th>Hill&rsquo;s criterion for causal inference</th><th>What it means</th></tr>
    <tr><td>Consistency of findings</td><td>Demonstrated in multiple studies, across different populations, in differing circumstances, with different study designs {c12('47')}</td></tr>
    <tr><td>Strength of association</td><td>Less likely to be due to chance or bias; a strong association has a relative risk that is very high or very low {c12('48')}</td></tr>
    <tr><td><strong>Biological gradient</strong></td><td>A <strong>dose-response</strong> relationship: changes in exposure are related to a trend in relative risk; <strong>one of the most reliable indicators of causality</strong> {c12('49')}</td></tr>
    <tr><td>Temporal sequence</td><td>Exposure must precede disease &mdash; and precede the latent period, in diseases that have one; chronic diseases often need long-term exposure {c12('50')}</td></tr>
    <tr><td>Plausibility and coherence</td><td>The mechanism should be biologically plausible and must not contradict the known natural history and biology &mdash; though the relationship may be indirect, the data may not yet exist, and understanding may need reinterpreting {c12('51')}</td></tr>
    <tr><td>Specificity of association</td><td>The exposure leads to a single or characteristic effect, or affects people with a specific susceptibility; easier to argue causation when specific, but many exposures cause several diseases {c12('52')}</td></tr>
  </table>
  <p>{c12('46')} The prevailing wisdom: most judgments of cause and effect are tentative and open to
  change with new evidence. {c12('53')}</p>
  {flag('''<p>How to answer her scenario. An exposure and a disease turning up together is an
  <strong>association</strong>. It moves toward <strong>causation</strong> as Hill&rsquo;s criteria
  are met &mdash; and the one she singled out in the lecture is the dose-response gradient: “And of
  course the best data would be something that gave you that biological gradient” [part 3, 11:34],
  which the slide calls one of the most reliable indicators of causality.</p>''')}""",
  lecture="“Now, if I were to by any chance give you a scenario that gave you some information, you "
          "should be able to tell me whether something is going to be more of an association or a "
          "causation.” [part 3, 11:10–11:25]"))

S3.append(item(12, "w12-epidemic", "3.9", "Objective 9 &mdash; Endemic, epidemic, pandemic, sporadic, herd immunity", COLD,
  "“And then know that endemic, epidemic, pandemic, sporadic, herd immunity” [part 4, 20:10–20:13]",
  f"""<p>Two instructions: know the five terms (the review), and be able to identify the epidemic
  curves (the lecture).</p>
  <table>
    <tr><th>Term</th><th>Definition</th></tr>
    <tr><td><strong>Endemic</strong></td><td>Diseases found at chronically low levels in a population</td></tr>
    <tr><td><strong>Sporadic</strong></td><td>Diseases that occur at irregular intervals, or are isolated incidents</td></tr>
    <tr><td><strong>Epidemic</strong></td><td>Diseases occurring in excess of what might be expected in a population, or as an uncontrolled spread in a community</td></tr>
    <tr><td><strong>Pandemic</strong></td><td>Worldwide epidemics</td></tr>
    <tr><td><strong>Herd immunity</strong></td><td>The cumulative number of immune persons in a population, or the percentage of the population immune; often discussed in relation to vaccination against a pathogen, but also affected by natural immunity from recovery {c12('60')}</td></tr>
  </table>
  <p>{c12('54')} Immunity itself is inherited, acquired or induced resistance to infection by a
  specific pathogen; resistance acquired from a previous infection comes from protective cellular
  and antibody responses. {c12('60')}</p>

  {flag(f'''<p><strong>The epidemic curves &mdash; “which you should be able to identify”.</strong>
  The types, then what each one looks like on the slides&rsquo; graphs of cases by date of onset.
  {c12('55')}</p>
  <table>
    <tr><th>Type</th><th>Definition</th><th>What the slide&rsquo;s graph shows</th></tr>
    <tr><td><strong>Common source: point</strong></td><td>A group exposed to the same source over a short time (one incubation period)</td><td>Hepatitis A, 1978: a presumed index case (a food handler), then a <strong>single sharp rise and fall</strong> {c12('56')}</td></tr>
    <tr><td><strong>Common source: continuous</strong></td><td>Exposure over a longer time (intermittent is the third common-source kind)</td><td>Diarrheal illness, 1989&ndash;1990: cases spread over weeks around water main breaks, <strong>falling only after a boil-water order and chlorination</strong> removed the source {c12('56')}</td></tr>
    <tr><td><strong>Propagated</strong></td><td>Person-to-person transmission</td><td>Measles, 1970&ndash;1971: <strong>successive waves of cases, each rising higher</strong> {c12('57')}</td></tr>
    <tr><td><strong>Mixed</strong></td><td>May start as a common source and then be propagated</td><td><em>Shigella</em> at a music festival, 1988: cases among staff first, then a large peak among attendees {c12('57')}</td></tr>
    <tr><td><strong>Other</strong></td><td>Often zoonotic or vector-borne</td><td>Lyme disease reported by year; West Nile encephalitis in New York City by week, falling after mosquito control began {c12('58')}</td></tr>
  </table>
  <p>The time slide gives the same distinction in words: a point source is localized and stationary;
  a propagated one reflects spreading infection and may be extended. {c12('36')}</p>''')}
  <p><strong>R<sub>0</sub>, the basic reproduction number</strong>, is the number of cases directly
  generated by one case in a susceptible population without interventions; <strong>R, the effective
  reproduction number</strong>, is the number generated by one case with interventions or immunity.
  {c12('59')}</p>""",
  lecture="“These different kinds of epidemics can be graphed and show different patterns, which you "
          "should be able to identify.” [part 3, 13:47–13:54]"))

S3.append(item(12, "w12-applications", "3.10", "Objective 10 &mdash; Applications of epidemiology", KNOW,
  "“and then the fact that epidemiology gives us the evidence for policy development.” "
  "[part 4, 20:16]",
  f"""<p>Her last words in the review were about policy, and they match the slide&rsquo;s phrase:
  <strong>evidence</strong> is one of four bases of policy (with values, ideology and politics),
  &ldquo;not usually the main influence on policy, but worth fighting for&rdquo; &mdash; and it is
  the main contribution of epidemiology. Epidemiological studies can bring major policy changes if
  they are rigorously conducted, reported and communicated. {c12('72')}</p>
  {gap(12, "L12 objective 10: outbreak investigation, social and behavioral, environmental and occupational applications not in her closing list (she named only policy)", f'''The
  objective names five applications; her list named one. The other four are on the slides.
  {c12('61')}''')}
  <table>
    <tr><th>Application</th><th>What the slides say</th></tr>
    <tr><td><strong><mark class="prof-highlight">Policy development</mark></strong></td><td>The <strong>policy cycle</strong>: assessment of population health; assessment of potential interventions and their evidence; policy choices (for example by computer modeling, then consensus); implementation with target goals and resources; evaluation {c12('73')}. Worked example, <strong>youth smoking</strong>: adult smoking fell by the 1980s but youth smoking did not, until a 1994 Surgeon General&rsquo;s report shifted the approach from individuals to the community; evidence that secondhand smoke was dangerous reframed it as a societal concern, leading to smoke-free public places, less advertising, less youth access and higher taxes {c12('74')}. A public health approach runs surveillance, risk factor identification, intervention, evaluation and implementation {c12('71')}</td></tr>
    <tr><td><strong>Outbreak investigation</strong></td><td>Establish the existence of an outbreak; prepare for field work; verify the diagnosis; define and identify cases; use descriptive epidemiology to orient the data; develop, evaluate and refine a hypothesis; implement control and prevention; communicate findings {c12('62')}. Worked example, <strong>Legionnaires&rsquo; disease</strong>, 1976: an American Legion convention in Philadelphia, 221 cases and 34 deaths; the case-control study found time in the <strong>lobby of Hotel A</strong> was the risk factor, and in December a CDC laboratorian located the bacterium {c12('64&ndash;68')}. Genomic epidemiology is now the critical tool here {c12('69')}</td></tr>
    <tr><td><strong>Social and behavioral issues</strong></td><td>How income inequality, poverty, race and discrimination affect health, including access to care; how behavioral risk factors contribute to disease; and policy in these areas {c12('75')}</td></tr>
    <tr><td><strong>Environment</strong></td><td>Environmental epidemiology: how environmental factors such as air and water pollution, or hazardous waste sites, affect human health {c12('76')}</td></tr>
    <tr><td><strong>Occupational health</strong></td><td>How workers&rsquo; health is affected by workplace conditions and hazardous substances: how often workers are injured or ill, which groups are most affected, why, and how to reduce the risk through regulation {c12('76')}</td></tr>
  </table>
  <p>For noncommunicable disease the slide lists the steps: define the population, measure
  exposures and health indicators, sample, estimate associations, evaluate whether they are causal,
  assess causes working together, and assess external validity. {c12('70')}</p>"""))


# --------------------------------------------------------------------------
# Page assembly
# --------------------------------------------------------------------------
def toc():
    out = ['<nav class="toc">', '  <h2>Contents</h2>',
           '  <a class="top-link" href="#how-to-use">How to use this page</a>']
    heads = {7: ("lec7", "1 &middot; Disorders in Immunity"),
             10: ("lec10", "2 &middot; Gram-Positive Bacilli"),
             12: ("lec12", "3 &middot; Epidemiology")}
    last = None
    for lec, anchor, num, title, _cls in ITEMS:
        if lec != last:
            out.append('  <a class="top-link" href="#%s">%s</a>' % heads[lec])
            last = lec
        short = re.sub(r"^Objective \d+ &mdash; ", "", title)
        out.append('  <a href="#%s">%s %s</a>' % (anchor, num, short))
    out.append('  <a class="top-link" href="#closing">What she said about the exam</a>')
    out.append('</nav>')
    return "\n".join(out)


HOWTO = """<h2 id="how-to-use">How to use this page</h2>
<p>This is not a second study guide. It is a record of what Professor Webster told the class to
study for Exam 2, on 16 October 2026, in the last twenty minutes of the Epidemiology lecture. It
opens “This is for the exam” [part 4, 0:00]. She walked her three Exam 2 lectures in order:
Disorders in Immunity objective by objective, the Gram-positive bacilli organism by organism, and
Epidemiology as a short closing list.</p>
<p>Each item carries her words and then the answer from the slides, cited to the slide. Her words
are quoted only where both transcripts of the recording agree, and the time in brackets says where
they are: [part 4, 13:17] is thirteen minutes into the review. For Epidemiology she had flagged
things during that morning&rsquo;s lecture itself, so those are quoted too, in a separate box marked
<em>In the lecture</em>, with their part of the recording. The recording only decides the
weighting. Every fact comes from the slides &mdash; the visible text and pictures, never the speaker
notes &mdash; and where what she said differs from a slide, the page says so and teaches the
slide.</p>
<table>
  <tr><th>Tier</th><th>What it means</th></tr>
  <tr><td><span class="tier tier-cold">Know cold</span></td>
      <td>She asked the class to answer it, drilled it, or said &ldquo;need to know&rdquo;, &ldquo;should know&rdquo; or &ldquo;should be able to&rdquo; (for Epidemiology, in the lecture as well as the review)</td></tr>
  <tr><td><span class="tier tier-know">Know it</span></td>
      <td>She walked it without singling it out &mdash; or it is an objective she did not mention, and its box says so plainly</td></tr>
  <tr><td><span class="tier tier-light">Light touch</span></td>
      <td>She said not to memorize it</td></tr>
</table>
<div class="callout">
  <p><strong>Scope.</strong> She reviewed <strong>only the three lectures she taught</strong>
  &mdash; Lecture 7 (Disorders in Immunity), Lecture 10 (Gram-Positive Bacilli of Medical
  Importance) and Lecture 12 (Epidemiology). Exam 2, on <strong>Friday 23 October 2026</strong>,
  covers <strong>Lectures 7&ndash;13</strong>, so Dr. Fair&rsquo;s four lectures are examinable and
  are <em>not</em> on this page: <strong>Lecture 8</strong> (Diagnosing Infections),
  <strong>Lecture 9</strong> (Cocci of Medical Importance), <strong>Lecture 11</strong> (Novel
  Antimicrobial Therapy) and <strong>Lecture 13</strong> (Miscellaneous Bacterial Agents of
  Disease). Use the full <a href="micro-exam-2-study-guide.html">Exam 2 study guide</a> and the
  <a href="micro-exam-2-cram-sheet.html">cram sheet</a> for those. The five
  <a href="micro-exam-2-master-exam-form-a.html">master exam forms</a> draw from all seven lectures
  by class time, and every form carries at least one question on each of her &ldquo;know cold&rdquo;
  items.</p>
  <p><strong>She also skipped parts of her own lectures, and they are still objectives:</strong>
  in Lecture 7, the mechanisms of carcinogenesis (Objective 8) and how allergy is diagnosed; in
  Lecture 10, <em>Nocardia</em> and the modes of transmission (Objective 2); in Lecture 12, the uses
  of epidemiology training, the sources of data and the definition of a reportable disease
  (Objectives 2, 4 and 6), and every application in Objective 10 except policy. Each has its place
  below, with a plain note that she did not mention it.</p>
</div>
<p class="obj-map"><strong>Lecture numbering.</strong> The site and the class calendar call the
Gram-positive bacilli lecture Lecture 10, and so does this page; its deck file is named
&ldquo;Lecture 9 Dr. Webster Gram positive Bacilli.pptx&rdquo;. Slide numbers are that
file&rsquo;s.</p>
<div class="prof-flag"><span class="prof-flag-label">&#9733; The three she said not to memorize</span>
  <p>All three were said during the Epidemiology lecture, about slides, not objectives:</p>
  <ul>
    <li><strong>The Slide 13 graph</strong> of genetic susceptibility to cancer over the lifespan &mdash; &ldquo;which I&rsquo;m not asking you to memorize&rdquo; [part 1, 11:25]. <em>Item 3.3.</em></li>
    <li><strong>The Slide 23 list of notifiable diseases</strong> &mdash; &ldquo;a list I&rsquo;m absolutely not requiring you to pay attention to&rdquo; [part 1, 27:48]. <em>The definition of a reportable disease is still Objective 6; item 3.6.</em></li>
    <li><strong>The Slide 25 list of uses of surveillance data</strong> &mdash; &ldquo;I don&rsquo;t want you to memorize this list&rdquo; [part 1, 29:10]. <em>Item 3.5.</em></li>
  </ul>
</div>
<div class="prof-flag"><span class="prof-flag-label">&#9733; Where her words and the slides differ</span>
  <p>She was reviewing from memory at speed. In each of these the slide wins, and the item explains:</p>
  <ul>
    <li><a href="#w7-allergy">1.3</a> Allergy shots: the blocking IgG (immunoglobulin G) keeps the allergen away from the IgE (immunoglobulin E) on mast cells; it is not that the IgE can no longer be made.</li>
    <li><a href="#w7-transfusion">1.4</a> Rh disease: the slide&rsquo;s condition is an Rh-negative mother with an Rh-positive <em>fetus</em>.</li>
    <li><a href="#w7-autoimmune">1.6</a> Rheumatic fever gives arthritis, myocarditis and valve scarring; &ldquo;reactive arthritis&rdquo; is a different example (<em>Shigella</em>, <em>Salmonella</em>, <em>Campylobacter</em>).</li>
    <li><a href="#w7-immunodef">1.7</a> Secondary immunodeficiency: the slide&rsquo;s causes include blood cell cancers, not cannabis.</li>
    <li><a href="#w10-bacillus">2.1</a> Anthrax: the slides have four forms (injection too) and anthrax meningitis, not three.</li>
    <li><a href="#w10-tetani">2.4</a> Tetanus: the slides say strict anaerobe needing low oxygen tension; &ldquo;mixed infection&rdquo; is the myonecrosis slide&rsquo;s term.</li>
    <li><a href="#w10-listeria">2.7</a> <em>Listeria</em> is resistant to cold and grows in the refrigerator; it does not need cold. Cold enrichment is the laboratory culture method.</li>
    <li><a href="#w10-leprae">2.11</a> Leprosy: armadillo transmission is a possibility; the mechanism is not fully verified.</li>
    <li><a href="#w10-actinomyces">2.12</a> <em>Actinomyces</em>: abdominal actinomycosis is a complication <em>of</em> a burst appendix, not a cause of appendicitis.</li>
  </ul>
</div>"""

CLOSING = """<h2 id="closing">What she said about the exam</h2>
<p>Four things are worth taking from the review beyond its contents.</p>
<p><strong>The objectives are the blueprint &mdash; except in Lecture 10.</strong> For Disorders in
Immunity she read down the objective list, and her Epidemiology list follows that lecture&rsquo;s
objectives in order. For the Gram-positive bacilli she set the objectives aside in so many words
&mdash; &ldquo;those learning objectives are really, really general, so let&rsquo;s go to the list of
organisms&rdquo; [part 4, 12:24&ndash;12:28] &mdash; so expect that lecture organism by organism:
where the spore sits, what it needs to grow, what disease it causes, and what gives it away.</p>
<p><strong>She asked more than she told.</strong> Most Lecture 7 and Lecture 10 items were put to the
class as questions: which hypersensitivity, which form of anthrax, what a mixed infection is, what
<em>Listeria</em> needs, what is characteristic of diphtheria. The questions she put to the room
are the clearest signal of what she expects you to be able to answer, and they are the Know cold
items above.</p>
<p><strong>Lecture 12 was weighted in the lecture, not the review.</strong> It got under a minute at
the end because she had just taught it. The stronger instructions &mdash; know the difference
between incidence and prevalence, know genomic epidemiology, tell association from causation in a
scenario, identify the epidemic curves &mdash; came during the lecture, and they are quoted in the
items.</p>
<p><strong>The review was one-sided by design.</strong> She reviewed her own three lectures. Nothing
here says anything about the relative weight of Dr. Fair&rsquo;s Lectures 8, 9, 11 and 13 on the
exam &mdash; she was not the one who taught them.</p>
<div class="callout">
  <p><strong>Next steps:</strong> the <a href="micro-exam-2-study-guide.html">full Exam 2 study
  guide</a> covers all seven lectures, and the <a href="micro-exam-2-cram-sheet.html">cram
  sheet</a> condenses them.</p>
</div>"""

EXTRA_CSS = """
  /* Tier badges. The review's whole value is the weighting, so the tier has to
     be legible at a glance in the heading rather than buried in prose. */
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

  /* Her actual words, kept visually distinct from the slide-sourced answer so
     the two sources can never be confused for one another. */
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

  /* Professor-emphasized content -- same convention as the CMS and Clin Path
     guides so the star means the same thing site-wide. */
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

  /* Which objective an organism item answers (Lecture 10), and the numbering note. */
  .obj-map{font-size:.84rem;color:var(--soft);margin:-2px 0 10px;}

  /* Inline slide citations: about 300 of them, so muted to keep the prose readable. */
  span.src{color:var(--soft);font-size:.88em;}
"""


def build():
    if not os.path.exists(DONOR):
        raise SystemExit("donor guide missing: %s" % DONOR)
    donor = open(DONOR, encoding="utf-8").read()

    # Lift the head (theme includes, analytics, palette) and the page chrome.
    # The donor's first </style> closes its main style block; the dark-tokens
    # <style> after it is kept by taking the head up to </head>.
    old_title = "<title>Microbiology &middot; Exam 2 &mdash; Study Guide</title>"
    new_title = "<title>Microbiology &middot; Exam 2 &mdash; Professor Webster&rsquo;s Review</title>"
    head_end = donor.index("</style>")
    head = donor[:head_end]
    assert old_title in head, "donor title changed; update the replacement"
    head = head.replace(old_title, new_title)
    # Everything between the main style's close and </head> (the dark-tokens
    # block) is carried over unchanged, after the extra CSS.
    head_tail = donor[head_end + len("</style>"):donor.index("</head>")]
    head = head + EXTRA_CSS + "</style>" + head_tail + "</head>"

    # Chrome: everything from <body ...> up to the opening of the donor's header.
    body_start = donor.index("<body")
    header_start = donor.index('<header class="top">')
    chrome = donor[body_start:header_start]

    # Footer and tail, taken SEPARATELY and re-ordered.
    #
    # Do not slice from the footer to the end of the donor. In the Exam 1 guide
    # the footer was stranded in the middle of the document -- later lectures
    # were appended after it -- and `donor[foot_start:]` silently carried 90 KB
    # of another lecture's content into the review page. The Exam 2 guide is
    # built by several builders too, so take the footer element alone, then the
    # tail from </main>, and assert there is exactly one of each.
    assert donor.count('<footer class="guide-foot"') == 1, "donor has != 1 guide footer"
    assert donor.count("</main>") == 1, "donor has != 1 </main>"
    foot_start = donor.index('<footer class="guide-foot"')
    foot_end = donor.index("</footer>", foot_start) + len("</footer>")
    footer_el = donor[foot_start:foot_end]
    tail = donor[donor.index("</main>"):]

    # Say what this page was built from. Assert the swap happened: matching a
    # stale footer string once silently changed nothing (Exam 1, 2026-09-24).
    swapped = False
    for _donor_footer in ("Built from your PAJ 5200 lecture decks", "Built from your %s lecture decks"):
        if _donor_footer in footer_el:
            footer_el = footer_el.replace(
                _donor_footer,
                "Built from Professor Webster&rsquo;s Exam 2 review and her three lecture decks")
            swapped = True
    assert swapped, "donor footer text changed; update the replacement"
    footer = footer_el + "\n" + tail

    header = (
        '<header class="top">\n'
        '  <h1>Microbiology &middot; Exam 2 &mdash; Professor Webster&rsquo;s Review</h1>\n'
        '  <p>PAJ 5200 Microbiology &middot; Class of 2028</p>\n'
        '  <p>What she told the class to study on 16 October 2026 &middot; '
        'covers Lectures 7, 10 and 12 &mdash; the three she taught &middot; '
        'every answer cited to its slide &middot; Exam 2 is on Friday 23 October 2026</p>\n'
        '</header>\n')

    body = []
    body.append('<div class="layout wrap" data-readable>')
    body.append(toc())
    body.append('<main>')
    body.append(HOWTO)
    body.append('<h2 id="lec7">1 &middot; Lecture 7 &mdash; Disorders in Immunity</h2>')
    body.append(iobox("Instructional objectives &mdash; Disorders in Immunity", IO7))
    body.append('<p>She walked this lecture objective by objective, in order, asking the class '
                'for most of the answers. One item per objective follows.</p>')
    body.extend(S1)
    body.append('<h2 id="lec10">2 &middot; Lecture 10 &mdash; Gram-Positive Bacilli of Medical Importance</h2>')
    body.append(iobox("Instructional objectives &mdash; Gram Positive Bacilli of Medical Importance", IO10))
    body.append(iobox("Appendix 2 organisms for this lecture", APPX10))
    body.append(
        '<p>She set these objectives aside &mdash; &ldquo;those learning objectives are really, '
        'really general. So let&rsquo;s go to the list of organisms&rdquo; [part 4, 12:24&ndash;12:31] '
        '&mdash; and went organism by organism. This section follows her order. Every organism item '
        'answers <strong>Objective 1</strong>, field by field in its table, and its transmission row '
        'answers <strong>Objective 2</strong>. <mark class="prof-highlight">Highlighted</mark> rows '
        'are the ones she brought up; the rest are what the objective still asks.</p>')
    body.append(gap(10, "L10: walk gave diseases and identifying features; treatment, prevention, laboratory tests and biochemistry mostly not mentioned", '''Her
        walk gave each organism&rsquo;s disease and the feature that identifies it. Objective 1 also
        asks for medium, laboratory tests, biochemical reactions, treatment and prevention, which she
        mostly did not mention, and Objective 2 asks for transmission. Both are in each table. Two
        list notes: <em>Clostridium botulinum</em> is <strong>not on the Appendix 2 list</strong> but
        is in the deck and she reviewed it (item 2.5); the deck also covers <em>Bacillus cereus</em>,
        <em>Lactobacillus</em>, <em>Erysipelothrix rhusiopathiae</em> and the nontuberculous
        mycobacteria, which are not on Appendix 2 and which she did not mention (Lecture 10, Slides
        17&ndash;18, 50&ndash;51, 57&ndash;58, 90&ndash;91).'''))
    body.extend(S2)
    body.append('<h2 id="lec12">3 &middot; Lecture 12 &mdash; Epidemiology</h2>')
    body.append(iobox("Instructional objectives &mdash; Epidemiology", IO12))
    body.append(
        '<p>She had given this lecture that morning, so the review gave it under a minute: a list '
        '[part 4, 19:38&ndash;20:23] that follows the objectives in order but skips Objectives 2, 4 '
        'and 6. During the lecture she had flagged things directly &mdash; what to know, and what not '
        'to memorize &mdash; and those are quoted in the boxes marked <em>In the lecture</em>, with '
        'their part of the recording. One item per objective follows.</p>')
    body.extend(S3)
    body.append(CLOSING)

    html = head + "\n" + chrome + header + "\n".join(body) + "\n" + footer

    # The donor may link a Word export that does not exist for this page.
    html = re.sub(r'\s*<link rel="alternate"[^>]*\.docx"[^>]*>', "", html)

    # A citation ends with a full stop, which is right at the end of a sentence
    # but reads "Slide 50.; ranges" mid-sentence. Drop the stop when the cite is
    # followed by ; , ) . or a lowercase word.
    html = re.sub(r'(<span class="src">[^<]*?)\.</span>(?=[;,).:]|\s+[a-z])', r'\1</span>', html)

    open(OUT, "w", encoding="utf-8").write(html)

    # Loud, checkable summary rather than a bare success line.
    by = {}
    for lec, _a, _n, _t, cls in ITEMS:
        by.setdefault(lec, {"cold": 0, "know": 0, "light": 0})[cls] += 1
    tot = {t: sum(v[t] for v in by.values()) for t in ("cold", "know", "light")}
    print("wrote %s (%d KB)" % (os.path.basename(OUT), len(html) // 1024))
    print("  items: %d  |  cold %d / know %d / light %d"
          % (len(ITEMS), tot["cold"], tot["know"], tot["light"]))
    for lec in sorted(by):
        v = by[lec]
        print("    Lecture %-2d  %2d items  |  cold %d / know %d / light %d"
              % (lec, sum(v.values()), v["cold"], v["know"], v["light"]))
    print("  light-touch sub-items (said not to memorize): %d" % len(LIGHTS))
    print("  professor-emphasis blocks: %d" % html.count('class="prof-flag"'))
    print("  slide citations: %d" % html.count('class="src"'))
    print("  quoted prompts: %d  (review boxes %d, lecture boxes %d)"
          % (html.count('class="asked"'), html.count('asked-label">In her review<'),
             html.count('asked-label">In the lecture<')))
    kinds = {}
    for _l, k, _s in FLAGS:
        kinds[k] = kinds.get(k, 0) + 1
    print("  flags: %d  |  %s" % (len(FLAGS), ", ".join("%s %d" % kv for kv in sorted(kinds.items()))))
    for lec, k, s in FLAGS:
        print("    [%s] %s" % (k, s))

    # the masters link must point at a page that exists (it was held out until the forms were built)
    assert os.path.exists(os.path.join(os.path.dirname(OUT), "micro-exam-2-master-exam-form-a.html")), "masters not built"
    for probe in ("data-audio-dir", "<script>alert", "Lecture 9, Slide",
                  'rel="alternate"', "Study Guide</title>"):
        assert probe not in html, "unexpected %r in output" % probe
    assert html.count("<main>") == 1 and html.count("</main>") == 1
    assert html.count('<footer class="guide-foot"') == 1
    assert html.index('id="closing"') < html.index('<footer class="guide-foot"') < html.index("</main>")
    assert "Built from Professor Webster&rsquo;s Exam 2 review" in html
    for lec in (7, 10, 12):
        assert "Lecture %d, Slide" % lec in html, "no Lecture %d citations" % lec
    assert {lec for lec, *_ in ITEMS} == {7, 10, 12}
    assert len(S1) == len(IO7), "Lecture 7 must have one item per objective"
    assert len(S3) == len(IO12), "Lecture 12 must have one item per objective"
    # Every timestamp must exist in its recording part; part 4 is 20:33 long.
    stamps = re.findall(r"\[part (\d), ([0-9:–&ndash;]+)\]", html)
    assert len(stamps) > 40, "timestamp pattern matched only %d stamps" % len(stamps)
    print("  timestamps checked: %d" % len(stamps))
    for part, stamp in stamps:
        assert part in "1234", "bad part %s" % part
        if part == "4":
            for mm, ss in re.findall(r"(\d+):(\d\d)", stamp):
                assert int(mm) * 60 + int(ss) <= REVIEW_LENGTH_S, "part 4 timestamp past 20:33: %s" % stamp
    for a in set(re.findall(r'href="#([^"]+)"', html)):
        assert ('id="%s"' % a) in html, "dangling in-page link #%s" % a


if __name__ == "__main__":
    build()
