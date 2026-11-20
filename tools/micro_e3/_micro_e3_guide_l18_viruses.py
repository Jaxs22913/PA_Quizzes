# -*- coding: utf-8 -*-
"""Lecture 18 guide fragment (the viruses): 18.7-18.26, slides 30-106 of
"Lecture 18  Dr. Webster -  DNA viruses of medical importance.pptx".

Exports TOC, BODY, TEST, NOTES for _micro_e3_guide_l18.py. Objective 4 is answered virus by virus (18.7-18.25) and
objective 5 drawn together for every virus (18.26). Content is from the visible slides only; every slide 30-106 was
viewed as a 1920-pixel render and every placed picture at full size.

Pictures left out: slide 39 (an 18th-century cartoon of vaccination, decoration), slides 50-51's maps (case tallies,
not taught). Slide 40's two pictures and slide 47's inset are unlabeled on the slide; their captions say so and claim
nothing the slide does not. Credits: MH where the McGraw-Hill line is printed on the picture; printed credits as
printed (World Health Organization, Mayo Foundation, Kathy Park Talaro).
"""
from _micro_e3_guide_l18_figs import fig, MH  # noqa: F401

TOC = """
  <a class="sub-link" href="#dna-survey">18.7 Objective 4 &mdash; Survey of the DNA viruses: enveloped and nonenveloped</a>
  <a class="sub-link" href="#dna-pox">18.8 Objective 4 &mdash; Poxviruses: classification and structure</a>
  <a class="sub-link" href="#dna-variola">18.9 Objective 4 &mdash; Variola virus and smallpox</a>
  <a class="sub-link" href="#dna-vaccinia">18.10 Objective 4 &mdash; Vaccinia virus, the smallpox vaccine</a>
  <a class="sub-link" href="#dna-molluscum">18.11 Objective 4 &mdash; Molluscum contagiosum</a>
  <a class="sub-link" href="#dna-mpox">18.12 Objective 4 &mdash; Mpox (monkeypox)</a>
  <a class="sub-link" href="#dna-cowpox">18.13 Objective 4 &mdash; Cowpox and orf virus</a>
  <a class="sub-link" href="#dna-herpes">18.14 Objective 4 &mdash; The herpesviruses: eight that infect humans</a>
  <a class="sub-link" href="#dna-hsv">18.15 Objective 4 &mdash; Herpes simplex viruses 1 and 2</a>
  <a class="sub-link" href="#dna-vzv">18.16 Objective 4 &mdash; Varicella zoster virus: chickenpox and shingles</a>
  <a class="sub-link" href="#dna-cmv">18.17 Objective 4 &mdash; Cytomegalovirus</a>
  <a class="sub-link" href="#dna-ebv">18.18 Objective 4 &mdash; Epstein-Barr virus</a>
  <a class="sub-link" href="#dna-hhv">18.19 Objective 4 &mdash; Human herpesviruses 6, 7 and 8; Kaposi sarcoma</a>
  <a class="sub-link" href="#dna-hbv">18.20 Objective 4 &mdash; Hepatitis B virus</a>
  <a class="sub-link" href="#dna-adeno">18.21 Objective 4 &mdash; Adenoviruses</a>
  <a class="sub-link" href="#dna-hpv">18.22 Objective 4 &mdash; Papilloma and polyoma viruses; human papillomavirus</a>
  <a class="sub-link" href="#dna-polyoma">18.23 Objective 4 &mdash; Polyomaviruses: JC and BK viruses</a>
  <a class="sub-link" href="#dna-parvo">18.24 Objective 4 &mdash; Parvoviruses and parvovirus B19</a>
  <a class="sub-link" href="#dna-aav">18.25 Objective 4 &mdash; Adeno-associated virus</a>
  <a class="sub-link" href="#dna-obj5">18.26 Objective 5 &mdash; Transmission, clinical picture and vaccine for every virus</a>"""

BODY = """
  <h3 class="sub" id="dna-survey">18.7 &middot; Objective 4 &mdash; Survey of the DNA viruses: enveloped and nonenveloped (slides 30&ndash;31, 92)</h3>
  <table>
    <tr><th>Group</th><th>Families</th><th>Viruses in this lecture</th></tr>
    <tr><td><strong>Enveloped, double-stranded</strong> (slide 31)</td><td>Poxviruses<br>Herpesviruses<br>Hepadnaviruses</td>
    <td>Variola, vaccinia, molluscum contagiosum, mpox, cowpox, orf (18.8&ndash;18.13)<br>Herpes simplex 1 and 2,
    varicella zoster, cytomegalovirus, Epstein-Barr, human herpesviruses 6, 7, 8 (18.14&ndash;18.19)<br>Hepatitis B
    (18.20)</td></tr>
    <tr><td><strong>Nonenveloped, double-stranded</strong> (slide 92)</td><td>Adenoviruses<br>Polyomaviruses<br>Papillomaviruses</td>
    <td>Adenovirus (18.21), human papillomavirus (18.22), JC and BK viruses (18.23)</td></tr>
    <tr><td><strong>Nonenveloped, single-stranded</strong> (slide 92)</td><td>Parvoviruses</td><td>Parvovirus B19 (18.24),
    adeno-associated virus (18.25)</td></tr>
  </table>
  """ + fig(30, 1, "l18-s030-dna-virus-groups.jpg",
      "A textbook chart titled DNA Virus Groups That Infect Humans: DNA viruses branch into enveloped and nonenveloped; enveloped double-stranded are the poxviruses, herpesviruses and hepadnaviruses; nonenveloped double-stranded are the adenoviruses and the polyomaviruses and papillomaviruses; nonenveloped single-stranded are the parvoviruses.",
      "<b>Table 24.1, DNA virus groups that infect humans.</b> Look for the two splits: <b>enveloped or "
      "not</b>, then <b>double- or single-stranded</b>. Only the parvoviruses are single-stranded; hepatitis B&rsquo;s "
      "hepadnavirus genome is the oddity, partly double- and partly single-stranded (slide 86).", MH) + """

  <h3 class="sub" id="dna-pox">18.8 &middot; Objective 4 &mdash; Poxviruses: classification and structure (slides 32&ndash;33)</h3>
  <ul>
    <li>Poxviruses produce <strong>eruptive skin pustules called pocks or pox, that leave scars</strong>.</li>
    <li>The <strong>largest and most complex animal viruses</strong>, with the <strong>largest genome of all
    viruses</strong>; <strong>double-stranded DNA</strong>.</li>
    <li><mark class="prof-highlight"><strong>They multiply in the cytoplasm, in factory areas.</strong></mark> &#9733; Dr.
    Webster: &ldquo;most of the DNA viruses multiply in the nucleus. But the pox viruses multiply in the
    cytoplasm.&rdquo; Her Exam 3 review asked what is unusual about their reproduction.</li>
    <li>A <strong>specificity for the cytoplasm of epidermal cells and subcutaneous connective tissues</strong> leads to
    the development of the pustules, or can stimulate tumor formation.</li>
  </ul>
  """ + fig(33, 1, "l18-s033-poxvirus.jpg",
      "A cutaway drawing of a brick-shaped poxvirus covered in surface tubules, with an envelope, an outer membrane, a core membrane around the nucleosome, and two lateral bodies, beside a 100-nanometer scale bar.",
      "<b>Poxviruses are larger and more complex than other viruses.</b> Look for the layers from outside in: "
      "<b>surface tubules</b>, <b>envelope</b>, <b>outer membrane</b>, then the <b>core membrane</b> around the "
      "nucleosome, with <b>lateral bodies</b> beside the core; the scale bar is 100 nanometers.") + """

  <h3 class="sub" id="dna-variola">18.9 &middot; Objective 4 &mdash; Variola virus and smallpox (slides 34&ndash;42, 45)</h3>
  <h4 class="subsub">History: from quarantine to variolation to vaccination (slides 34&ndash;38; background)</h4>
  <ul>
    <li>Smallpox was recognized as a major health threat for centuries, described in Africa, Asia and Europe since
    400 BC, spread along world-wide trade routes and reached the Americas in the 16th century. It <strong>requires a
    human host</strong>, so it tended to be present in densely populated areas, with epidemics at regular intervals.
    Most medical traditions focused on prevention rather than a cure, with <strong>quarantine</strong> a prevalent method
    (slide 34).</li>
    <li><strong>Variolation</strong>: the <strong>deliberate introduction of smallpox as a preventive measure</strong>.
    First documented in China in the 15th century, by <strong>nasal insufflation</strong> (powdered smallpox material
    blown up the nose); also practiced in the Middle East and much of Africa. Western medicine ignored a letter
    describing it by Dr. Emmanuel Timoni of Constantinople, published in 1714, until it was noticed by Lady Mary Wortley
    Montagu and the Boston preacher Cotton Mather (slide 35).</li>
    <li>Lady Mary Wortley Montagu, who had lost her brother to smallpox and survived it herself, had her son and her
    daughter variolated; the practice spread despite deaths from the bloodletting and deep incisions done with it. The
    Sutton family of English physicians developed a milder method and by 1770 had treated over 300,000 patients (slide
    36). John Williamson (&ldquo;Johnnie Notions&rdquo;), self-taught in Scotland, reduced the virulence of the material
    and was reputed never to have lost a patient. England was the international center of variolation. Cotton Mather
    learned of it from Onesimus, a man he enslaved; in 1775 George Washington ordered the Continental Army variolated
    (slide 37).</li>
    <li><strong>Transition to vaccination</strong>, Edward Jenner and James Phipps, 1796: variolation did not always work
    and sometimes failed to protect from an epidemic; collateral smallpox cases spread by variolated people began to
    outweigh the benefits; <strong>vaccination was a less harmful method</strong>, and variolation was made illegal in
    some countries (slide 38).</li>
  </ul>
  """ + fig(34, 1, "l18-s034-smallpox-quarantine-placard.jpg",
      "An old printed placard reading SMALLPOX, KEEP OUT OF THIS HOUSE, by order of the board of health.",
      "<b>Quarantine, the old prevention.</b> A board of health placard (&ldquo;Smallpox. Keep out of this "
      "house&rdquo;) beside slide 34&rsquo;s line that most traditions focused on prevention, with quarantine a "
      "prevalent method.") + """
  <h4 class="subsub">The disease (slides 40&ndash;42)</h4>
  <table>
    <tr><th>Feature</th><th>Smallpox</th></tr>
    <tr><td><strong>Transmission</strong></td><td>Person to person by <strong>inhalation of airborne saliva</strong>;
    <strong>contact with material from smallpox pustules or scabs</strong>; contact with <strong>fomites</strong>
    contaminated with that material</td></tr>
    <tr><td><strong>Incubation</strong></td><td>7&ndash;10 days</td></tr>
    <tr><td><strong>Initial symptoms</strong></td><td>High fever, head and body aches, vomiting</td></tr>
    <tr><td><strong>Early rash</strong></td><td><mark class="prof-highlight"><strong>The stage of greatest
    contagion</strong></mark> (the slide&rsquo;s asterisk): small red spots on the tongue and mouth that break open,
    releasing large amounts of virus into the mouth and throat. &#9733; Dr. Webster: &ldquo;that&rsquo;s when you are
    most contagious. That&rsquo;s when you are most contagious.&rdquo;</td></tr>
    <tr><td><strong>Skin rash</strong></td><td>Starts on the <strong>face</strong>, spreads to the arms and legs, then the
    hands and feet, with <strong>total body coverage in 24 hours</strong>; the fever then declines. By the 4th day the
    skin sores fill with fluid, and the fever may rise again and stay high until scabs form over the bumps</td></tr>
    <tr><td><strong>Contagious until</strong></td><td>The patient remains contagious; <strong>once all scabs have fallen
    off</strong> (they may leave scars) the patient is no longer contagious</td></tr>
    <tr><td><strong>Forms</strong></td><td><strong>Variola major</strong>: highly virulent, causing toxemia, shock and
    intravascular coagulation. <strong>Variola minor</strong>: less virulent</td></tr>
    <tr><td><strong>Treatment</strong> (not tested)</td><td>July 2018: the Food and Drug Administration approved
    tecovirimat for smallpox, effective in lab animals with similar disorders but not tested on humans. Cidofovir and
    brincidofovir were effective against the virus in animals in lab settings, not tested on sick humans.
    Tecovirimat and cidofovir are stockpiled by the Centers for Disease Control and Prevention&rsquo;s Strategic National
    Stockpile, medical supplies for a public health emergency</td></tr>
  </table>
  """ + fig(40, 2, "l18-s040-variola-micrograph.jpg",
      "A black-and-white electron micrograph of several large oval, textured virus particles packed together.",
      "<b>Beside slide 40&rsquo;s transmission text</b> (unlabeled on the slide): an electron micrograph of large oval "
      "virions, the size and shape of the poxviruses, the largest animal viruses (slides 32&ndash;33).") + """
  """ + fig(40, 1, "l18-s040-stained-tissue.jpg",
      "A stained tissue section: pale blue-stained cells in the upper half and a dense band of red-stained material below.",
      "<b>Beside slide 40&rsquo;s signs and symptoms</b> (unlabeled on the slide): a stained tissue section from the "
      "smallpox slide; the slide gives no label or explanation.") + """
  """ + fig(41, 1, "l18-s041-smallpox-pustules.jpg",
      "A close-up of skin covered in raised, round, fluid-filled bumps.",
      "<b>By the 4th day, the skin sores fill with fluid</b> (slide 41): raised, round pustules.") + """
  """ + fig(41, 2, "l18-s041-smallpox-scabs.jpg",
      "A close-up of darker skin with many small crusted, scabbing lesions.",
      "<b>Scabs form over the bumps</b> (slide 41). The patient stays contagious until <b>all</b> of them have "
      "fallen off.") + """
  <p><strong>Eradication</strong> (slide 45): the <strong>last case of natural smallpox was in 1977 in
  Somalia</strong>; it was <strong>declared eradicated by the World Health Organization in 1980</strong>. Her chart:
  <mark class="prof-highlight"><strong>&ldquo;First disease to be eliminated by vaccine&rdquo;</strong></mark>; no more
  routine vaccination except for the front line. &#9733; Dr. Webster: &ldquo;this was really the first disease that was
  eradicated through vaccination efforts.&rdquo;</p>
  """ + fig(45, 1, "l18-s045-smallpox.jpg",
      "Two photographs: (a) a young child whose face and body are covered with raised pustules, and (b) an arm and hand covered with many round, raised pustules.",
      "<b>Smallpox infections.</b> Look for the pustules covering the <b>face</b> and the <b>arms and hands</b>, the "
      "areas the rash reaches first and next.", "Images: &copy; World Health Organization; &copy; World Health "
      "Organization/Peter Arnold.") + """

  <h3 class="sub" id="dna-vaccinia">18.10 &middot; Objective 4 &mdash; Vaccinia virus, the smallpox vaccine (slides 43&ndash;44)</h3>
  <ul>
    <li><strong>Prevention of smallpox is vaccination with vaccinia virus</strong> (slide 43).</li>
    <li>It is <strong>no longer routinely given</strong>; routine vaccination ended in 1972. The vaccine was
    <strong>reintroduced in 2002 for military and medical personnel</strong>.</li>
    <li>A <strong>live virus vaccine</strong>, good for about 3 years.</li>
    <li><strong>Bioterrorism</strong>: smallpox is a potential weapon because people are no longer routinely vaccinated;
    the Centers for Disease Control and Prevention keeps vaccines and treatments in the Strategic National
    Stockpile.</li>
    <li>Slide 44 (she said these are not needed): the stockpile has 3 vaccines, ACAM2000 (live vaccinia virus), Jynneos
    (a smallpox and monkeypox vaccine, live virus) and the Aventis Pasteur smallpox vaccine (investigational). Only 2
    labs work with smallpox, the Centers for Disease Control and Prevention in Atlanta and one lab in Russia; on November
    15, 2019 the Food and Drug Administration issued final guidance for developing smallpox treatments.</li>
  </ul>
  """ + fig(43, 1, "l18-s043-vaccination-site-reaction.jpg",
      "Four photographs of the same arm titled Primary Vaccination Site Reaction: on day 4 a small red bump, on day 7 a white blister with a red rim, on day 14 a larger crusting sore, and on day 21 a dark scab, each with a 1-centimeter scale bar.",
      "<b>Primary vaccination site reaction</b> to the live vaccinia vaccine. Look for the course over three weeks: a "
      "red bump (day 4), a blister (day 7), a crusting sore (day 14), a scab (day 21).") + """
  <p>Her chart files a &ldquo;Cowpox&rdquo; disease under &ldquo;Vaccinia&rdquo;; slides 43 and 53 keep them apart
  (18.27).</p>

  <h3 class="sub" id="dna-molluscum">18.11 &middot; Objective 4 &mdash; Molluscum contagiosum (slide 46)</h3>
  <ul>
    <li>In endemic areas (Pacific islands) it is primarily an <strong>infection of children</strong>.</li>
    <li><strong>Transmitted by direct contact and fomites.</strong> In the United States, it is most commonly a sexually
    transmitted disease.</li>
    <li><strong>Atopic dermatitis</strong> may be a risk factor, from breaks in the skin.</li>
    <li>Lesions are <strong>small, smooth, waxy</strong> macules in the genital area and thighs, normally
    <strong>self-limiting</strong>.</li>
    <li>Patients with acquired immunodeficiency syndrome suffer an <strong>atypical form</strong> that attacks the skin
    of the face and forms <strong>tumor-like growths</strong>.</li>
    <li>Treatment: freezing, electric cautery, chemical agents; her chart: <strong>removal of individual
    lesions</strong>. <strong>No vaccine</strong> (chart).</li>
  </ul>
  """ + fig(46, 1, "l18-s046-molluscum-lesions.jpg",
      "Two photographs of a child: small, smooth, dome-shaped, flesh-colored bumps on the skin of a limb, some with a central dimple, and two similar bumps near the eye.",
      "<b>Molluscum contagiosum in a child.</b> Look for the <b>small, smooth, waxy</b> dome-shaped lesions, here on a "
      "limb and the face.", "&copy; Mayo Foundation for Medical Education and Research.") + """
  """ + fig(46, 2, "l18-s046-molluscum-atypical-face.jpg",
      "The side of a man's face and neck covered with many clustered, raised, tumor-like growths.",
      "<b>The atypical form</b> in acquired immunodeficiency syndrome: it attacks the skin of the face and forms "
      "<b>tumor-like growths</b>.") + """

  <h3 class="sub" id="dna-mpox">18.12 &middot; Objective 4 &mdash; Mpox (monkeypox) (slides 47&ndash;52)</h3>
  <p><strong>Other poxviruses</strong> (slide 47): many mammalian groups host some poxvirus (cowpox, rabbitpox,
  mousepox, elephantpox). <strong>Humans are susceptible to cowpox and monkeypox.</strong> Mpox (monkeypox) was
  discovered in 1958; the first human case was recorded in 1970; <strong>most cases are in Africa</strong>. Outbreaks
  outside Africa before 2022: the United States 2003 (47 cases), the United Kingdom 2018 (3), Israel 2018 (1), the
  United States 2021 (2, travel related).</p>
  <table>
    <tr><th>Mpox in humans (slide 48)</th><th></th></tr>
    <tr><td><strong>Transmission</strong></td><td>The virus <strong>enters through broken skin, the respiratory tract or
    mucous membranes</strong>; may be through <strong>contact with body fluids or fomites</strong>. Her chart: contact
    with infected animals or humans</td></tr>
    <tr><td><strong>Initial stages</strong></td><td>Fever, head and body aches, chills, <strong>swollen lymph
    nodes</strong>, exhaustion</td></tr>
    <tr><td><strong>Rash</strong></td><td><strong>1&ndash;3 days after the fever</strong>, a skin rash often beginning on
    the <strong>face</strong> and spreading; it goes through <strong>macules, papules, vesicles, pustules,
    scabs</strong></td></tr>
    <tr><td><strong>Course</strong></td><td>A <strong>2&ndash;4 week illness</strong></td></tr>
  </table>
  <p><strong>Outbreaks</strong> (slides 49&ndash;51; background): the <strong>2003 United States outbreak</strong> (cases
  in Illinois, Indiana, Kansas, Missouri, Ohio, Wisconsin) was traced to <strong>pet prairie dogs</strong> housed at an
  animal vendor facility with rodents from Africa (African giant pouched rats, dormice, rope squirrels); the virus was
  recovered from a patient and the patient&rsquo;s prairie dog, and importation of African rodents is no longer
  permitted. The 2021 cases were both in travelers from Nigeria. The 2022 outbreak: 87,314 global cases and 145 deaths
  in 109 countries; United States cases 29,821 (2022), 1,204 (2023), 2,358 (2024).</p>
  <p><strong>Now</strong> (slide 52): United States cases show spread within the defined subpopulation of gay,
  bisexual and other men who have sex with men. <mark class="prof-highlight"><strong>Vaccination is
  available</strong></mark>, and the Centers for Disease Control and Prevention provides a link to a <strong>vaccine
  locator tool</strong>. &#9733; Her review: &ldquo;where do I find a vaccine against this one?&rdquo;</p>
  <ul>
    <li><strong>JYNNEOS vaccine</strong>: a <strong>2-dose series given 28 days apart</strong>.</li>
    <li><strong>ACAM2000 vaccine</strong>: approved to protect against smallpox, made available to prevent monkeypox; a
    <strong>single dose with multiple needle pricks</strong>.</li>
  </ul>
  """ + fig(47, 2, "l18-s047-mpox-rash.jpg",
      "Four photographs of a child with many raised, round, firm pustules spread over the chest, arms, back, buttocks, legs and hands.",
      "<b>Mpox in a child</b> (slide 47). Look for pustules over the trunk, limbs and <b>hands</b>; the rash runs "
      "macules, papules, vesicles, pustules, scabs (slide 48).") + """
  """ + fig(47, 1, "l18-s047-mpox-lesion.jpg",
      "A small photograph of a single raised pustule with a white center on reddened skin, with an inset electron micrograph of oval virus particles.",
      "<b>A single pustule</b> with an inset micrograph of the virus (unlabeled on slide 47).") + """
  """ + fig(51, 2, "l18-s051-mpox-lips.jpg",
      "A close-up of a man's lips and chin labeled Day 9, with several small round sores around the mouth.",
      "<b>Mpox lesions around the lips, day 9</b> (slide 51): the virus enters through broken skin and mucous "
      "membranes.") + """

  <h3 class="sub" id="dna-cowpox">18.13 &middot; Objective 4 &mdash; Cowpox and orf virus (slides 53&ndash;54)</h3>
  <h4 class="subsub">Cowpox in humans (slide 53)</h4>
  <ul>
    <li>Found not only in cows but in <strong>rodents, cats and zoo animals</strong>.</li>
    <li><strong>Human infections are rare</strong>, usually <strong>confined to the hands</strong>; other cutaneous
    sites can be involved.</li>
    <li>Cases are re-emerging worldwide, thought perhaps to be related to <strong>loss of herd immunity from smallpox
    vaccination</strong>.</li>
    <li><strong>Rodents seem to be the primary reservoirs.</strong> From rodents, humans can get it by <strong>handling
    cats that interacted with rodents</strong>; cases are also reported after traumatic injury.</li>
    <li><strong>A vaccine only for animals</strong>, used in Europe for circus and zoo animals.</li>
  </ul>
  """ + fig(53, 1, "l18-s053-cowpox.jpg",
      "Two photographs, A and B: A, a reddened, swollen patch of skin with a small dark central crust on a forearm; B, scattered small red lesions and one round sore on pale skin.",
      "<b>Cowpox in humans</b>, panels A and B: localized skin lesions with a small dark crust (A). Slide 53: human "
      "infections are usually confined to the hands; other cutaneous sites can be involved.") + """
  <h4 class="subsub">Orf virus (slide 54)</h4>
  <ul>
    <li>A <strong>parapox virus</strong>.</li>
    <li>Primarily a virus of <strong>ruminant animals, sheep and goats</strong>: it causes sores on the mouth; in animals
    the disease is called <strong>sore mouth, scabby mouth or contagious ecthyma</strong>.</li>
    <li>It can be transmitted to humans through <strong>handling of animals</strong>: feeding, shearing, bites.</li>
    <li><strong>More serious in the immunocompromised.</strong></li>
  </ul>
  """ + fig(54, 1, "l18-s054-orf-animal-mouth.jpg",
      "The dark muzzle of a goat or sheep held in a hand, with a small sore at the corner of the mouth.",
      "<b>Orf in its animal host</b>: a sore on the mouth of a sheep or goat (&ldquo;sore mouth&rdquo;).") + """
  """ + fig(54, 2, "l18-s054-orf-hand.jpg",
      "The back of a person's hand with a large, raised, crusted, weeping sore surrounded by red swollen skin.",
      "<b>Orf in a human</b>: a raised, crusted sore on the <b>hand</b>, from handling the animals.") + """

  <h3 class="sub" id="dna-herpes">18.14 &middot; Objective 4 &mdash; The herpesviruses: eight that infect humans (slides 55&ndash;57)</h3>
  <p><strong>The herpesviruses: common, persistent human viruses</strong> (slide 55):</p>
  <ul>
    <li><strong>All members show latency and cause recurrent infection; the viral DNA forms an episome.</strong></li>
    <li>Most people are infected with members of this family, with few symptoms.</li>
    <li>Clinical complications of latency and recurrent infections become <strong>more severe with advancing age, cancer
    chemotherapy, or other conditions that compromise the immune defenses</strong>.</li>
    <li>Common and serious <strong>opportunists</strong> among patients with acquired immunodeficiency syndrome; may be
    associated with cancers.</li>
    <li><strong>Large, enveloped, icosahedral, double-stranded DNA</strong>; they <strong>replicate within the
    nucleus</strong>.</li>
  </ul>
  """ + fig(56, 1, "l18-s056-herpesvirus.jpg",
      "A drawing of a round herpesvirus with glycoprotein spikes on its envelope around an icosahedral capsid holding a DNA core, beside an electron micrograph of a herpesvirus with the same parts and the tegument labeled.",
      "<b>Herpesvirus structure.</b> Look for the parts from outside in: <b>glycoprotein spikes</b> on the "
      "<b>envelope</b>, the <b>tegument</b> beneath it, the icosahedral <b>capsid</b> and the <b>DNA core</b>.",
      "&copy; Kathy Park Talaro.") + """
  <div class="prof-flag"><span class="prof-flag-label">&#9733; &ldquo;Put a star on this little slide.&rdquo; &mdash; Dr. Webster on slide 57 [part 2, 11:15]</span>
  <p><strong>Herpesviruses: a large family; 8 infect humans</strong> (slide 57). Her review: &ldquo;What do all of
  those delightful little herpes viruses do? 1 through 8&rdquo;.</p>
  <table>
    <tr><th>Virus</th><th>What it does (slide 57)</th><th>Where in this guide</th></tr>
    <tr><td><strong>Herpes simplex 1</strong></td><td><mark class="prof-highlight">Fever blisters</mark></td><td>18.15</td></tr>
    <tr><td><strong>Herpes simplex 2</strong></td><td><mark class="prof-highlight">Genital infections</mark></td><td>18.15</td></tr>
    <tr><td><strong>Varicella zoster virus</strong></td><td><mark class="prof-highlight">Chickenpox and shingles</mark></td><td>18.16</td></tr>
    <tr><td><strong>Cytomegalovirus</strong></td><td><mark class="prof-highlight">Infects salivary glands and viscera</mark></td><td>18.17</td></tr>
    <tr><td><strong>Epstein-Barr virus</strong></td><td><mark class="prof-highlight">Lymphoid tissue &mdash; infectious mononucleosis</mark></td><td>18.18</td></tr>
    <tr><td><strong>Human herpesvirus 6</strong></td><td><mark class="prof-highlight">Roseola</mark></td><td>18.19</td></tr>
    <tr><td><strong>Human herpesvirus 7</strong></td><td><mark class="prof-highlight">Roseola</mark></td><td>18.19</td></tr>
    <tr><td><strong>Human herpesvirus 8</strong></td><td><mark class="prof-highlight">Kaposi&rsquo;s sarcoma</mark></td><td>18.19</td></tr>
  </table></div>

  <h3 class="sub" id="dna-hsv">18.15 &middot; Objective 4 &mdash; Herpes simplex viruses 1 and 2 (slides 58&ndash;67)</h3>
  <table>
    <tr><th></th><th>Herpes simplex 1</th><th>Herpes simplex 2</th></tr>
    <tr><td><strong>Usual lesions</strong> (slide 58)</td><td>On the <strong>oropharynx</strong>: cold sores, fever
    blisters</td><td>On the <strong>genitalia</strong>, possibly oral</td></tr>
    <tr><td><strong>When acquired</strong></td><td>Early childhood</td><td>Ages 14&ndash;29; 1&ndash;1.5 million cases a
    year in the United States</td></tr>
    <tr><td><strong>Where it hides</strong> (slide 59)</td><td>Enters the <strong>5th cranial nerve</strong>; latent in
    the <strong>trigeminal ganglion</strong></td><td>Enters the <strong>lumbosacral spinal nerve trunk
    ganglia</strong></td></tr>
    <tr><td><strong>Diseases</strong></td><td>Herpes labialis, gingivostomatitis, keratitis, whitlow, gladiatorum,
    meningoencephalitis</td><td>Genital herpes; whitlow</td></tr>
    <tr><td><strong>Vaccine</strong> (chart)</td><td>No, but candidate vaccines in trials</td><td>No, research
    ongoing</td></tr>
  </table>
  <p><strong>Shared facts</strong> (slides 58&ndash;59): <strong>humans are the only natural reservoir</strong>, and
  humans are susceptible to 2 varieties. <mark class="prof-highlight"><strong>It can be spread without visible
  lesions.</strong></mark> &#9733; Dr. Webster: &ldquo;here&rsquo;s the fun part. It can be spread even if you cannot
  see visible lesions.&rdquo; Transmission is by <strong>direct exposure to secretions containing the virus</strong>;
  <strong>active lesions are the most significant source</strong>, but <strong>genital herpes can be transmitted in
  the absence of lesions</strong>. The virus multiplies in <strong>sensory neurons and moves to the ganglia</strong>.
  <strong>Recurrent infection is triggered</strong> by fever, ultraviolet radiation, stress and mechanical injury; the
  newly formed viruses migrate to the body surface and produce a local skin or membrane lesion.</p>
  <h4 class="subsub">Herpes simplex 1 in children and adults (slides 60&ndash;62)</h4>
  <ul>
    <li><strong>Herpes labialis</strong> (fever blisters, cold sores): the <strong>most common recurrent herpes simplex 1
    infection</strong>; vesicles on the <strong>mucocutaneous junction of the lips</strong> or adjacent skin;
    <strong>itching and tingling before the vesicles form</strong>; the lesion crusts over in 2&ndash;3 days and heals.</li>
    <li><strong>Herpetic gingivostomatitis</strong>: infection of the oropharynx in <strong>young children</strong>;
    fever, sore throat, swollen lymph nodes.</li>
    <li><strong>Herpetic keratitis</strong> (ocular herpes): inflammation of the eye; a <strong>gritty feeling</strong>,
    conjunctivitis, sharp pain and sensitivity to light.</li>
    <li><strong>Herpetic whitlow</strong>: herpes simplex 1 <strong>or 2</strong> penetrates a <strong>break in the
    skin</strong> and causes a localized infection, usually on <strong>one finger</strong>; extremely painful and
    itchy.</li>
    <li><strong>Herpes gladiatorum</strong> (mat herpes): a skin infection common in people playing sports like
    <strong>wrestling, basketball or rugby</strong>; may be prevented by showering immediately after practice or games,
    and by not sharing razors, deodorants or towels.</li>
    <li><strong>Herpetic meningoencephalitis</strong>: may occur during the initial infection or from reactivation of a
    previous infection; <strong>if not treated it may be fatal</strong>.</li>
    <li>Those with underlying immunodeficiency are prone to <strong>severe, disseminated herpes</strong>.</li>
  </ul>
  """ + fig(60, 1, "l18-s060-herpes-labialis.jpg",
      "A close-up of a lip with a cluster of small crusting blisters at its edge.",
      "<b>Herpes labialis</b>: vesicles at the <b>mucocutaneous junction of the lip</b>, crusting over.") + """
  """ + fig(60, 2, "l18-s060-herpetic-keratitis.jpg",
      "A child's eye with a cluster of red crusted blisters on the eyelids and skin around the eye.",
      "<b>Ocular herpes</b> (slide 60&rsquo;s herpetic keratitis): blisters around a child&rsquo;s inflamed eye.") + """
  """ + fig(61, 1, "l18-s061-herpetic-whitlow.jpg",
      "A swollen fingertip with purple-red, blistered and peeling skin around the nail.",
      "<b>Herpetic whitlow</b>: a localized infection of <b>one finger</b> through a break in the skin; extremely "
      "painful and itchy.") + """
  """ + fig(62, 1, "l18-s062-herpes-gladiatorum.jpg",
      "A close-up of a patch of skin covered in clustered small red blisters and crusts.",
      "<b>Herpes gladiatorum</b> (mat herpes): clustered vesicles, the skin infection of contact sports.") + """
  <h4 class="subsub">Herpes simplex 2: genital herpes (slide 63)</h4>
  <p><strong>Genital herpes</strong> (herpes genitalia) starts with <strong>malaise, anorexia, fever, and bilateral
  swelling and tenderness in the groin</strong>; then <strong>clusters of sensitive vesicles on the genitalia, perineum
  and buttocks</strong>; urethritis, painful urination, cervicitis, itching; the vesicles ulcerate.
  <strong>Recurrent bouts are usually less severe</strong>, triggered by menstruation, stress and concurrent bacterial
  infection.</p>
  """ + fig(63, 1, "l18-s063-genital-herpes.jpg",
      "A close-up of skin with a cluster of small, clear, fluid-filled blisters on a reddened base.",
      "<b>Type 2 herpes</b>: a <b>cluster of sensitive vesicles</b> on a red base, which will ulcerate.") + """
  <h4 class="subsub">Herpes of the newborn (slides 64&ndash;65)</h4>
  <ul>
    <li>Caused by <strong>herpes simplex 1 and 2</strong>; <strong>potentially fatal in the neonate and fetus</strong>.</li>
    <li>The infant is <strong>contaminated by the mother before or during birth</strong>; also hand transmission from
    mother to infant.</li>
    <li>Infection of the mouth, skin, eyes and central nervous system. Mortality: 30% if confined to the skin, eyes and
    mouth; 50&ndash;80% if the central nervous system is involved.</li>
    <li>Prevention: <strong>preventive screening of pregnant women</strong>; <strong>delivery by cesarean section if
    there is an outbreak at the time of birth</strong>.</li>
  </ul>
  """ + fig(65, 1, "l18-s065-neonatal-herpes.jpg",
      "A newborn with a tube taped to its face, its scalp and face covered with scattered blisters and raw red sores.",
      "<b>Neonatal herpes</b>: vesicles and sores on the skin of the head and face of a newborn, the mouth-skin-eyes "
      "form that can reach the central nervous system.") + """
  <h4 class="subsub">Diagnosis, treatment and control (slides 66&ndash;67)</h4>
  <ul>
    <li><strong>Vesicles and exudate</strong> are the typical diagnostic signs; <strong>scrapings from the base of
    lesions show giant multinucleated cells and inclusion bodies</strong>; culture and specific tests for severe or
    disseminated herpes simplex; <strong>direct fluorescent antibody tests</strong>.</li>
    <li>Treatment (not tested): acyclovir, famciclovir, valacyclovir; topical medications.</li>
  </ul>
  """ + fig(67, 1, "l18-s067-pap-smear-giant-cell.jpg",
      "A stained Pap smear: among normal blue-green cells lies one large pink cell with many dark nuclei packed in a row, labeled Giant cell with multiple nuclei, with an Inclusion labeled.",
      "<b>Diagnosis of herpes virus infection from a stained specimen, a Pap smear.</b> Look for the <b>giant cell "
      "with multiple nuclei</b> and its <b>inclusion</b>, beside normal cells.") + """

  <h3 class="sub" id="dna-vzv">18.16 &middot; Objective 4 &mdash; Varicella zoster virus: chickenpox and shingles (slides 68&ndash;70)</h3>
  <ul>
    <li>Causes <strong>chickenpox and shingles</strong>; <strong>humans are the only natural host</strong>.</li>
    <li>Transmitted by <strong>respiratory droplets and contact with fluid from active skin lesions</strong>.</li>
    <li><mark class="prof-highlight"><strong>Most infectious 24&ndash;48 hours prior to the development of
    lesions.</strong></mark> &#9733; Dr. Webster: &ldquo;most infectious in the 24 to 48 hours before you ever see
    lesions&rdquo;; &ldquo;again it is most infectious before the lesions ever hit.&rdquo;</li>
    <li><strong>Primary infection is chickenpox</strong>, with characteristic vesicles. The virus <strong>enters neurons
    and remains latent</strong>.</li>
    <li>Later, <strong>reactivation results in shingles</strong>, with vesicles localized to <strong>dermatomes</strong>
    (areas of skin along specific nerve pathways); inflammation of the ganglia gives pain down the nerve pathways. More
    common in <strong>older patients</strong>.</li>
    <li><mark class="prof-highlight"><strong>Shingles patients can infect unvaccinated individuals, particularly
    children, causing chickenpox, not shingles.</strong></mark> &#9733; Dr. Webster: &ldquo;they will not get shingles,
    they will get chicken pox.&rdquo;</li>
    <li>There may be issues with secondary infections.</li>
    <li>Treatment: treat symptoms in uncomplicated infections; acyclovir, famciclovir, interferon for systemic disease
    (drugs not tested).</li>
    <li><strong>A live attenuated vaccine for chickenpox and shingles.</strong></li>
  </ul>
  """ + fig(70, 1, "l18-s070-varicella-zoster.jpg",
      "Three panels: a crying child covered with red spots of chickenpox; a drawing of herpes zoster virus activated in a ganglion by stress, the viruses migrating down a sensory nerve from the spinal cord to the skin of one band of the chest; and a red band of shingles rash across a man's shoulder and back.",
      "<b>The relationship between varicella and zoster.</b> Look for the sequence: chickenpox everywhere (the primary "
      "infection), the virus latent in a <b>ganglion</b> and <b>activated by stress</b>, then migrating <b>down a "
      "sensory nerve</b> to the skin, giving shingles along <b>one dermatome</b>.") + """

  <h3 class="sub" id="dna-cmv">18.17 &middot; Objective 4 &mdash; Cytomegalovirus (slides 71&ndash;74)</h3>
  <ul>
    <li>Cytomegaloviruses <strong>produce giant cells with nuclear and cytoplasmic inclusions</strong>; also called the
    salivary gland virus or cytomegalic inclusion virus.</li>
    <li><strong>Transmitted in saliva, respiratory mucus, breast milk, urine, semen, cervical secretions, or in tissues
    (transplants).</strong></li>
    <li><strong>Commonly latent in various tissues.</strong></li>
    <li>It establishes persistent infections by <strong>interfering with antigen presentation to CD8 T cells</strong>.
    It reduces cell-surface major histocompatibility complex class I, so infected cells are vulnerable to attack by
    natural killer cells; selection results in a population of natural killer cells designed to work when
    cytomegalovirus comes out of latency.</li>
    <li><strong>Most infections are asymptomatic</strong> (50% of women and 10% of newborns have been exposed) (slide
    72).</li>
    <li><strong>3 groups develop a more virulent form</strong>: <strong>fetuses, newborns and immunodeficient
    adults</strong>.</li>
    <li><strong>Newborns</strong> may show an <strong>enlarged liver and spleen, jaundice, capillary bleeding,
    microcephaly and ocular inflammation</strong>; it may be fatal. <strong>Babies who survive develop neurological
    sequelae, hearing and visual disturbances and mental retardation.</strong> This is the teratogen of 18.6.</li>
    <li>Perinatal infection: mostly asymptomatic, or pneumonitis and a mononucleosis-like syndrome.</li>
    <li><strong>Patients with acquired immunodeficiency syndrome</strong>: cytomegalovirus mononucleosis, disseminated
    infection, <strong>retinitis</strong>. <strong>Most transplant patients</strong>: pneumonitis, hepatitis,
    myocarditis, meningoencephalitis (slide 74).</li>
    <li>Before treatment it must be differentiated from other infections: <strong>microscopic analysis, monoclonal
    antibodies, enzyme-linked immunosorbent assay</strong>.</li>
    <li><strong>Treatment is reserved for the immunocompromised</strong> (ganciclovir, foscarnet; not tested).</li>
    <li><strong>No vaccine yet</strong>: many are at different stages of development, but it is difficult because of
    the <strong>lack of an animal model</strong>.</li>
  </ul>
  """ + fig(71, 1, "l18-s071-cytomegalovirus-structure.jpg",
      "A drawing of a round cytomegalovirus: double-stranded DNA inside a nucleocapsid, surrounded by the tegument and a lipid envelope studded with glycoprotein B and the pentamer complex, with a 150 to 200 nanometer scale.",
      "<b>Cytomegalovirus structure</b>, a herpesvirus: <b>double-stranded DNA</b> in a nucleocapsid, the "
      "<b>tegument</b>, a <b>lipid envelope</b> with glycoproteins; 150&ndash;200 nanometers across.") + """
  """ + fig(73, 1, "l18-s073-owls-eye-inclusion.jpg",
      "A pink-stained smear: a normal lung cell beside a much larger infected lung cell whose nucleus holds a large dark inclusion ringed by a pale halo, labeled Owl's eye effect.",
      "<b>Identifying cytomegaloviruses: the owl&rsquo;s eye.</b> Look for the <b>infected lung cell</b>, far "
      "larger than the normal one, with a <b>nucleus with a large inclusion</b>: the &ldquo;owl&rsquo;s eye "
      "effect&rdquo;. &#9733; Dr. Webster: &ldquo;They call it an owl&rsquo;s eye effect.&rdquo;") + """

  <h3 class="sub" id="dna-ebv">18.18 &middot; Objective 4 &mdash; Epstein-Barr virus (slides 75&ndash;80)</h3>
  <ul>
    <li>A <strong>ubiquitous virus</strong>; it infects <strong>lymphoid tissue and salivary glands</strong>.</li>
    <li>Transmission: <strong>direct, oral contact and contamination with saliva</strong>.</li>
    <li>In industrialized countries, the <strong>college-age population</strong> is vulnerable to <strong>infectious
    mononucleosis</strong> (mono, or the kissing disease). By mid-life, 90&ndash;95% of all people are infected.</li>
    <li><strong>Infectious mononucleosis</strong>: <strong>sore throat, high fever, cervical lymphadenopathy,
    splenomegaly</strong>; develops after a <strong>30&ndash;50 day incubation</strong>.</li>
    <li><strong>Dormancy in B cells</strong>; it can be reactivated; may be asymptomatic.</li>
  </ul>
  """ + fig(76, 1, "l18-s076-mononucleosis-throat.jpg",
      "A photograph of an open mouth showing the back of the throat: a rash on the palate and white exudate on the tonsils.",
      "<b>Epstein-Barr virus: infectious mononucleosis.</b> Look for the labels: the <b>exudate</b> on the "
      "<b>tonsil</b> and a <b>rash</b> on the palate, the sore throat of mono.") + """
  <h4 class="subsub">Tumors and other complications (slides 77&ndash;78)</h4>
  <ul>
    <li><strong>Burkitt lymphoma</strong>: a <strong>B cell malignancy</strong>; it usually develops in the
    <strong>jaw</strong> and grossly swells the cheek; <strong>central African children 5&ndash;7 years old</strong>; may
    be associated with chronic coinfections with malaria.</li>
    <li><strong>Nasopharyngeal carcinoma</strong>: a malignancy of <strong>epithelial cells</strong>; occurs in adults
    30&ndash;60, older Chinese and African men, those with a family history and those who eat <strong>salt-cured
    foods</strong>.</li>
    <li>Anyone with an immune deficiency is highly susceptible to Epstein-Barr virus; patients with acquired
    immunodeficiency syndrome get <strong>hairy leukoplakia</strong>.</li>
    <li><strong>Chronic fatigue syndrome: a possible link</strong> (slide 78; also called myalgic encephalomyelitis or
    systemic exertion intolerance disease, names she said you do not need). Symptoms: disabling fatigue, memory loss,
    sore throat, tender muscles, swollen lymph glands, joint pain, headaches, abnormal levels of CD4 T cells, low levels
    of natural killer cells, an overactive inflammatory response.</li>
  </ul>
  """ + fig(76, 2, "l18-s076-burkitt-lymphoma.jpg",
      "A young child whose jaw and cheek are grossly swollen.",
      "<b>Burkitt lymphoma</b> (pictured on slide 76; described on slide 77): a B cell tumor that develops in the "
      "<b>jaw</b> and grossly swells the cheek, in a central African child.") + """
  """ + fig(77, 1, "l18-s077-hairy-leukoplakia.jpg",
      "A small photograph of a tongue with white, ridged, hair-like patches along its side.",
      "<b>Hairy leukoplakia</b> in a patient with acquired immunodeficiency syndrome (slide 77): white, ridged "
      "patches.") + """
  <h4 class="subsub">Diagnosis, treatment and prevention (slides 79&ndash;80)</h4>
  <ul>
    <li>A <strong>differential blood count shows lymphocytosis, neutropenia and large atypical lymphocytes</strong>;
    serological assays detect antibodies and antigen.</li>
    <li>Treatment is directed at relief of the symptoms of fever and sore throat; disseminated disease may be treated
    with intravenous gamma globulin, interferon, acyclovir and monoclonal antibodies (drugs not tested).</li>
    <li><strong>No vaccines are available for prevention</strong>, but several therapeutic vaccines exist for
    Epstein-Barr virus related cancers (slide 79 says available; the chart says in clinical trials: 18.27).</li>
  </ul>
  """ + fig(80, 1, "l18-s080-ebv-lymphocyte.jpg",
      "Two blood smear photographs: (a) a normal small round lymphocyte with a dark nucleus among red blood cells; (b) a much larger lymphocyte with abundant pale blue cytoplasm spreading around neighboring red blood cells, marked by arrows.",
      "<b>Histology of lymphocytes infected with Epstein-Barr virus.</b> Compare the <b>normal lymphocyte</b> (a, "
      "small, round, mostly nucleus) with the <b>Epstein-Barr virus lymphocyte</b> (b): large and atypical, with "
      "abundant cytoplasm.") + """

  <h3 class="sub" id="dna-hhv">18.19 &middot; Objective 4 &mdash; Human herpesviruses 6, 7 and 8; Kaposi sarcoma (slides 81&ndash;84)</h3>
  <h4 class="subsub">Human herpesvirus 6 (slides 81&ndash;83)</h4>
  <ul>
    <li>Also called the human B-lymphotropic virus.</li>
    <li>Transmitted by <strong>close contact with saliva and other secretions</strong>; very common (95% of the
    population).</li>
    <li>Causes <strong>roseola</strong>, an <strong>acute febrile disease in babies</strong> 2&ndash;12 months old: it
    <strong>begins with fever, followed by a faint maculopapular rash</strong>; usually self-limited.</li>
    <li>Adults may get mononucleosis-like symptoms, lymphadenopathy and hepatitis.</li>
    <li>Over 70% of multiple sclerosis patients show signs of infection, with active viruses in the lesions. An
    <strong>association (not causation)</strong> with Hodgkin&rsquo;s lymphoma, oral carcinoma and certain T-cell
    leukemias.</li>
    <li><strong>No vaccine</strong> (chart).</li>
  </ul>
  """ + fig(82, 1, "l18-s082-roseola.jpg",
      "A baby's bare chest and belly covered with a faint, fine pink rash.",
      "<b>Roseola infantum in a 12-month-old baby</b> (slide 82). Look for the <b>faint maculopapular rash</b> on the "
      "trunk, which comes after the fever.") + """
  <h4 class="subsub">Human herpesvirus 7 (slide 83)</h4>
  <p><strong>Closely related to human herpesvirus 6</strong>; it causes similar diseases (her chart: roseola, by contact
  with saliva) and is also associated with cancers. No vaccine (chart).</p>
  <h4 class="subsub">Human herpesvirus 8 and Kaposi sarcoma (slides 83&ndash;84)</h4>
  <ul>
    <li><mark class="prof-highlight"><strong>Kaposi&rsquo;s sarcoma-associated virus, or human herpesvirus 8, is linked
    with the common tumor of patients with acquired immunodeficiency syndrome</strong></mark>; it may also be involved
    in multiple myeloma, primary effusion lymphoma and some forms of Castleman&rsquo;s disease. &#9733; Dr. Webster:
    &ldquo;probably the one that you&rsquo;d be most familiar with because it causes Kaposi&rsquo;s sarcoma&rdquo;.</li>
    <li><strong>Kaposi&rsquo;s sarcoma</strong>: <strong>small, painless, discolored lumps on the skin</strong>, but it
    may <strong>disseminate to internal organs</strong>.</li>
    <li>Her chart: transmitted by <strong>saliva, sexual contact, blood transfusion, organ transplant</strong>; no
    vaccine.</li>
  </ul>
  """ + fig(84, 1, "l18-s084-kaposi-sarcoma.jpg",
      "A patient lying in a hospital bed with many small, dark, discolored spots scattered over the chest and abdomen.",
      "<b>Kaposi&rsquo;s sarcoma lesions</b>: many <b>small, painless, discolored lumps</b> on the skin of the "
      "trunk.") + """
  """ + fig(84, 2, "l18-s084-kaposi-sarcoma-mouth.jpg",
      "An open mouth with dark purple patches on the inside of the cheek and gums.",
      "<b>Kaposi&rsquo;s sarcoma in the mouth</b>: dark purple lesions on the oral mucosa.") + """
  """ + fig(84, 3, "l18-s084-kaposi-sarcoma-face.jpg",
      "The face and ear of a patient covered with large, dark purple, raised and ulcerating lesions.",
      "<b>Extensive Kaposi&rsquo;s sarcoma of the face</b>, the lesions grown large and confluent.") + """
  """ + fig(84, 4, "l18-s084-kaposi-sarcoma-liver.jpg",
      "An internal organ, smooth and brown, speckled with many small dark spots.",
      "<b>Disseminated to an internal organ</b>: dark lesions speckling an internal organ (slide 83: it may "
      "disseminate to internal organs).") + """

  <h3 class="sub" id="dna-hbv">18.20 &middot; Objective 4 &mdash; Hepatitis B virus (slides 85&ndash;91)</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Lecturer emphasized &mdash; &ldquo;you need to know that one&rdquo;</span>
  <p>&ldquo;Three principal viruses associated with hepatitis, hepatitis B, which is the DNA virus, you need to know that
  one, and then Dr. Fair will talk to you about hepatitis A and C next week because they are RNA viruses.&rdquo; [part 2,
  35:10&ndash;35:25]</p></div>
  <p><strong>The viral agents of hepatitis</strong> (slide 85): <strong>hepatitis</strong> is an inflammatory disease of
  liver cells that may result from several viruses: <strong>necrosis of hepatocytes</strong> and a mononuclear
  response that disrupts liver structure. It interferes with the liver&rsquo;s excretion of bile pigments, so
  <strong>bilirubin accumulates</strong> in blood and tissues, causing <strong>jaundice</strong>, a yellow tinge in the
  skin and eyes. Three principal viruses: <strong>hepatitis B (a DNA virus)</strong>, hepatitis A and hepatitis C (ribonucleic acid
  viruses).</p>
  <h4 class="subsub">The hepadnaviruses (slide 86)</h4>
  <ul>
    <li><strong>Enveloped DNA viruses.</strong></li>
    <li><strong>Difficult to culture in the lab</strong>: the DNA must be isolated from hepatitis B and injected into
    <strong>human liver cancer cells</strong> (the medium).</li>
    <li>An <strong>unusual genome containing both double- and single-stranded DNA</strong>.</li>
    <li><strong>Tropism for the liver</strong>; may be involved in liver cell carcinoma.</li>
  </ul>
  """ + fig(86, 1, "l18-s086-hepadnavirus-micrograph.jpg",
      "A blue-stained electron micrograph of many small round and rod-shaped particles, three of them marked with numbered arrows.",
      "<b>Hepadnaviruses</b> (slide 86): an electron micrograph of the round and rod-shaped particles; the slide does "
      "not explain the numbered arrows.") + """
  <h4 class="subsub">Hepatitis B virus and disease (slides 87&ndash;89)</h4>
  <ul>
    <li><strong>It multiplies exclusively in the liver, which continuously seeds the blood with viruses</strong>
    (chronic): 10<sup>7</sup> virions per milliliter of blood.</li>
    <li><strong>Minute amounts of blood and blood products can transmit infection</strong>; it is also <strong>sexually
    transmitted</strong>.</li>
    <li><mark class="prof-highlight"><strong>An issue for health care workers.</strong></mark> &#9733; Dr. Webster:
    &ldquo;for healthcare workers, this is why you have to avoid the needle sticks&rdquo;. Her chart: a great risk to
    health care workers because of a <strong>very low infective dose</strong>.</li>
    <li>A high incidence among the same population as human immunodeficiency virus.</li>
    <li><strong>It can become a chronic infection</strong> and <strong>increases the risk of liver cancer,
    hepatocellular carcinoma</strong> (the oncogenic example of 18.6).</li>
    <li><strong>Pathogenesis</strong> (slide 88): the virus enters through a <strong>break in the skin or mucous
    membrane, or by injection into the bloodstream</strong>; it reaches the liver cells, multiplies and releases viruses
    into the blood; an <strong>average 7-week incubation</strong>.</li>
    <li><strong>Most show few overt symptoms and eventually develop immunity.</strong> Some have malaise, fever, chills,
    anorexia, abdominal discomfort and diarrhea. In more severe disease: <strong>fever, jaundice, rash and
    arthritis</strong>, which may be worsened by co-infection with <strong>hepatitis D</strong> (the delta agent, a
    circular RNA virus). A small number develop <strong>chronic liver disease: necrosis and cirrhosis</strong>.</li>
  </ul>
  """ + fig(89, 1, "l18-s089-hepatitis-b-clinical-features.jpg",
      "A drawing of a woman lying on her side with a reddish rash, an enlarged liver drawn over her abdomen, and labels for fever, low white cell count, arthritis, rash, pain and tenderness, jaundice and enlarged liver.",
      "<b>The clinical features of hepatitis B.</b> Look for the labels: <b>fever</b>, <b>low white cell count</b>, "
      "<b>arthritis</b>, <b>rash</b>, pain and tenderness, <b>jaundice</b> and an <b>enlarged liver</b>.") + """
  <h4 class="subsub">Diagnosis, management and prevention (slides 90&ndash;91)</h4>
  <ul>
    <li><strong>Diagnosis</strong>: examination of risk factors; <strong>serological tests to detect viral antibodies or
    antigen</strong>; radioimmunoassay and enzyme-linked immunosorbent assay tests for <strong>surface
    antigens</strong>.</li>
    <li><strong>Screening</strong> of blood for transfusion, semen for sperm banks, organs for transplant, and
    <strong>routine prenatal testing of all pregnant women</strong>.</li>
    <li>Mild cases are managed by treating symptoms and supportive care; chronic infections are treated with
    interferon.</li>
    <li><strong>Passive immunization</strong> with hepatitis B immune globulin for persons exposed or possibly exposed,
    including <strong>health care workers</strong> or <strong>neonates born to infected mothers</strong>.</li>
    <li><strong>Primary prevention is vaccination</strong>, for high-risk individuals and encouraged for <strong>all
    newborns and infants</strong>.
      <ul>
        <li>Vaccines derived from <strong>surface antigen from cloned yeast</strong>: 3 doses with boosters.</li>
        <li>A vaccine derived from purified, sterile antigen extracted from carrier blood, mainly for people with
        <strong>yeast allergies</strong>.</li>
      </ul></li>
  </ul>

  <h3 class="sub" id="dna-adeno">18.21 &middot; Objective 4 &mdash; Adenoviruses (slides 92&ndash;95)</h3>
  <ul>
    <li><strong>Nonenveloped, double-stranded DNA</strong>; an <strong>acute infection</strong>.</li>
    <li><strong>Over 50 types</strong> are associated with human disease.</li>
    <li>They infect <strong>lymphoid tissue, respiratory and intestinal epithelia and the conjunctiva</strong>.</li>
    <li><strong>Oncogenic in animals, not in humans.</strong></li>
    <li><strong>Spread by respiratory and ocular secretions</strong> (her chart adds ingestion).</li>
    <li>Cause <strong>colds, pharyngitis, conjunctivitis, keratoconjunctivitis, acute hemorrhagic cystitis, infantile
    gastroenteritis</strong>.</li>
    <li>Severe cases may be treated with interferon or antivirals.</li>
    <li><strong>Type 41 adenovirus is associated with hepatitis in children aged 1&ndash;6</strong> (slide 94): liver
    enzymes are remarkably increased; the children have vomiting, diarrhea, jaundice and abdominal pain; some advanced
    to acute liver failure. Some of the most serious cases show a <strong>co-infection with adeno-associated
    virus</strong> (a parvovirus); at this time only an association, with more data needed for causation (18.25).</li>
    <li><strong>Vaccine</strong>: a polyvalent vaccine against <strong>types 4 and 7</strong>, which the slide calls
    inactivated; some <strong>military personnel are vaccinated in training environments</strong>; given as an
    <strong>oral vaccine</strong> to personnel 17&ndash;50 years old (18.27 on &ldquo;inactivated&rdquo;).</li>
  </ul>
  """ + fig(95, 1, "l18-s095-adenovirus-structures.jpg",
      "Three panels: (a) an orange-stained cell with its nucleolus, nuclear membrane and dark viral inclusions labeled; (b) a magenta field labeled Mass of virions; (c) an electron micrograph of a regular array of many round, many-sided virus particles.",
      "<b>Distinctive adenovirus structures.</b> Look for the <b>viral inclusions</b> inside the nucleus (a), the "
      "<b>mass of virions</b> (b) and, at high magnification, the <b>regular array</b> of icosahedral virions "
      "(c).") + """

  <h3 class="sub" id="dna-hpv">18.22 &middot; Objective 4 &mdash; Papilloma and polyoma viruses; human papillomavirus (slides 96&ndash;100)</h3>
  <p><strong>Papilloma and polyoma viruses</strong> (slide 96): <strong>small, nonenveloped, double-stranded
  DNA</strong>; <strong>circular DNA</strong>; they <strong>cause persistent infections and tumors</strong>.</p>
  <h4 class="subsub">Human papillomavirus (slides 97&ndash;99)</h4>
  <ul>
    <li><strong>Papilloma</strong>: a squamous epithelial growth, <strong>wart, or verruca</strong>; caused by 100
    different strains of human papillomavirus.</li>
    <li><strong>Common seed warts</strong>: painless, elevated, rough growths, on the fingers and elsewhere.</li>
    <li><strong>Plantar warts</strong>: deep, painful, on the soles of the feet.</li>
    <li><strong>Genital warts</strong>: the slide calls them the most common sexually transmitted disease in the United
    States; they range from <strong>tiny, flat, inconspicuous bumps to extensive, branching, cauliflower-like
    masses</strong>.</li>
    <li><strong>Transmissible through direct contact or contaminated fomites</strong> (her chart: including sexual
    contact); incubation 2 weeks to more than a year.</li>
    <li><strong>Nine human papillomavirus types increase the risk of reproductive cancer</strong>; 2 account for 70% of
    metastatic tumors. Slide 28: papillomaviruses cause <strong>cervical and penile cancer</strong> (18.6).</li>
    <li><mark class="prof-highlight"><strong>Early detection</strong></mark> through inspection of the genitals and, for
    women, a <strong>Pap smear to screen for abnormal cervical cells</strong>. &#9733; Dr. Webster: &ldquo;this is why
    early detection is really important&rdquo;.</li>
    <li>Most common warts <strong>regress over time</strong>; they can be removed by direct chemical application
    (podophyllin) and physical removal by cauterization, freezing or laser surgery. <strong>Warts can
    recur.</strong></li>
    <li><strong>Two effective human papillomavirus vaccines</strong>, Gardasil and Cervarix (her chart: vaccines
    available for genital warts).</li>
  </ul>
  """ + fig(98, 1, "l18-s098-warts.jpg",
      "Two photographs: (a) a hand with several rough, raised warts on the fingers, labeled Common wart; (b) a genital area examined with gloved hands, with small growths labeled Condylomata acuminata, labeled Genital warts.",
      "<b>Human papillomas.</b> Compare the <b>common wart</b> (a: rough, elevated growths on the fingers) with "
      "<b>genital warts</b> (b: condylomata acuminata).") + """
  """ + fig(100, 1, "l18-s100-koilocyte.jpg",
      "A Pap smear with a cluster of dark blue-stained cervical cells, one marked Koilocyte with a clear halo around its nucleus, beside a large pale normal cervical cell.",
      "<b>Pap smear of the cervix in a patient with human papillomavirus infection.</b> Look for the <b>koilocyte</b>, "
      "a cell with a clear halo around its nucleus, against the <b>normal cervical cell</b>.") + """

  <h3 class="sub" id="dna-polyoma">18.23 &middot; Objective 4 &mdash; Polyomaviruses: JC and BK viruses (slides 101&ndash;102)</h3>
  <ul>
    <li>Polyomaviruses <strong>induce tumors in experimental animals</strong>.</li>
    <li>The <strong>JC and BK viruses</strong> (named for the patients from whom they were first isolated: John
    Cunningham and Brookfield Kidney) are the most important human polyomaviruses. Common throughout the world; the
    <strong>majority of infections are asymptomatic or mild</strong>.</li>
    <li>Up to 80% of all adults have been exposed to JC virus, possibly as children; BK virus seroprevalence rates are up
    to 91%, typically exposed in early adolescence.</li>
  </ul>
  <table>
    <tr><th></th><th>JC virus</th><th>BK virus</th></tr>
    <tr><td><strong>Disease</strong></td><td><strong>Progressive multifocal leukoencephalopathy</strong>: an uncommon,
    often fatal infection</td><td><strong>Interstitial nephritis</strong> (chart); hematuria, hemorrhagic
    cystitis</td></tr>
    <tr><td><strong>Course</strong></td><td>Initial infection via the <strong>tonsils or gastrointestinal tract</strong>,
    then latent in the gastrointestinal tract and the tubular epithelial cells of the kidneys, shedding viruses in the
    urine; may laterally infect human semen and chorionic villi tissues. It <strong>can cross the blood-brain
    barrier</strong></td><td>Initial symptoms like a <strong>cold</strong>, then it lies <strong>dormant in the kidney
    and the lining of the ureters and bladder</strong>, controlled by the immune system</td></tr>
    <tr><td><strong>Who</strong></td><td>Seen in <strong>immunosuppressed patients</strong></td><td>Seen <strong>after
    renal transplants and immunosuppressive drugs</strong></td></tr>
    <tr><td><strong>What it does</strong></td><td><strong>Destruction of the cells that produce myelin</strong> (chart:
    demyelination of nerves, progressive neurological symptoms)</td><td>Complications in urinary function:
    <strong>hematuria, hemorrhagic cystitis and interstitial nephritis</strong>; some studies show a link to systemic
    lupus</td></tr>
    <tr><td><strong>Vaccine</strong> (chart)</td><td colspan="2">None for humans</td></tr>
  </table>

  <h3 class="sub" id="dna-parvo">18.24 &middot; Objective 4 &mdash; Parvoviruses and parvovirus B19 (slides 103&ndash;105)</h3>
  <ul>
    <li>Parvoviruses: <strong>nonenveloped, single-stranded DNA</strong>; a <strong>small diameter and genome
    size</strong>.</li>
    <li>In animals they cause distemper in cats, enteric disease in dogs and fatal cardiac infection in puppies.</li>
    <li><strong>B19 causes erythema infectiosum (fifth disease)</strong>, a rash of childhood: children may have
    <strong>fever and a rash on the cheeks</strong>. It is the <strong>fifth rash disease of childhood</strong>; the other
    4 are chickenpox, measles, rubella and roseola.</li>
    <li><mark class="prof-highlight"><strong>Severe fatal anemia can result if a pregnant woman transmits the virus to
    the fetus, which can result in hydrops fetalis.</strong></mark> &#9733; Dr. Webster: &ldquo;if a pregnant woman gets
    it, it can be very, very serious&rdquo;.</li>
    <li>In adults it can cause a <strong>polyarthropathy syndrome</strong> with massive swelling of the joints, or
    <strong>cessation of red blood cell production</strong>; most common in the immunocompromised.</li>
    <li>Her chart: spread by <strong>droplet infection</strong>; the vaccine cell is blank.</li>
  </ul>
  """ + fig(105, 1, "l18-s105-fifth-disease.jpg",
      "A close-up of a young child's face in profile with a bright red flush over the cheek.",
      "<b>Typical &ldquo;slapped face&rdquo; rash of human parvovirus B19, fifth disease.</b> Look for the bright red "
      "rash on the <b>cheek</b>.") + """

  <h3 class="sub" id="dna-aav">18.25 &middot; Objective 4 &mdash; Adeno-associated virus (slides 94, 106)</h3>
  <ul>
    <li><strong>Adeno-associated virus is a defective parvovirus</strong>: it <strong>cannot replicate in the host cell
    without adenovirus</strong>.</li>
    <li>It is now used as a <strong>viral vector for human gene therapy</strong>: currently approved to treat
    <strong>lipoprotein lipase deficiency</strong>, with multiple clinical trials for cystic fibrosis, genetic eye
    diseases, macular degeneration, hemophilia and neurodegenerative diseases.</li>
    <li><strong>By itself it is not known to cause disease</strong>, but some evidence suggests that as a
    <strong>coinfection with an adenovirus that causes hepatitis</strong> it makes the infection more severe (slide 94:
    only an association so far).</li>
  </ul>

  <h3 class="sub" id="dna-obj5">18.26 &middot; Objective 5 &mdash; Transmission, clinical picture and vaccine for every virus</h3>
  <p>Objective 5 asks three things of every virus: how it spreads, what it looks like, and whether a vaccine exists.
  Drawn together from the text slides and her chart (the slide numbers are the source; where the chart and a text
  slide differ, the text slide is given and 18.27 explains).</p>
  <div class="table-scroll" style="overflow-x:auto;-webkit-overflow-scrolling:touch"><table style="min-width:720px">
    <tr><th>Virus</th><th>Mode of transmission</th><th>Clinical manifestations</th><th>Vaccine available?</th></tr>
    <tr><td><strong>Variola</strong> (smallpox)</td><td>Inhalation of airborne saliva; contact with pustule or scab
    material; fomites (40)</td><td>High fever, aches, vomiting; early rash in the mouth (most contagious); face-first
    rash, pustules, scabs (40&ndash;41)</td><td><strong>Yes: vaccinia</strong>, a live virus vaccine; no longer
    routine (43)</td></tr>
    <tr><td><strong>Vaccinia</strong></td><td>&mdash; (the vaccine virus itself, 43)</td><td>A vaccination site reaction:
    bump, blister, crust, scab (43)</td><td>It <strong>is</strong> the smallpox vaccine (43)</td></tr>
    <tr><td><strong>Molluscum contagiosum</strong></td><td>Direct contact and fomites; in the United States mostly
    sexual (46)</td><td>Small, smooth, waxy lesions on the genital area and thighs; tumor-like growths of the face in
    acquired immunodeficiency syndrome (46)</td><td><strong>No</strong> (chart)</td></tr>
    <tr><td><strong>Mpox</strong></td><td>Broken skin, respiratory tract or mucous membranes; body fluids or fomites
    (48); infected animals or humans (chart)</td><td>Fever, aches, chills, <strong>swollen lymph nodes</strong>; a rash
    from the face, macules to scabs; 2&ndash;4 weeks (48)</td><td><strong>Yes</strong>: JYNNEOS (2 doses, 28 days
    apart), ACAM2000 (single dose, multiple needle pricks); a vaccine locator tool (52)</td></tr>
    <tr><td><strong>Cowpox</strong></td><td>Rodents the main reservoir; handling cats that met rodents; traumatic injury
    (53)</td><td>Rare; lesions usually confined to the hands (53)</td><td>Only for animals, in Europe (53)</td></tr>
    <tr><td><strong>Orf</strong></td><td>Handling sheep and goats: feeding, shearing, bites (54)</td><td>Sores; more
    serious in the immunocompromised (54)</td><td>Not stated</td></tr>
    <tr><td><strong>Herpes simplex 1</strong></td><td>Direct exposure to secretions; spread without visible lesions
    (58&ndash;59)</td><td>Cold sores, gingivostomatitis, keratitis, whitlow, gladiatorum, meningoencephalitis
    (60&ndash;62)</td><td><strong>No</strong>; candidate vaccines in trials (chart)</td></tr>
    <tr><td><strong>Herpes simplex 2</strong></td><td>Direct contact; genital herpes even without lesions (59); mother to
    newborn (64)</td><td>Groin swelling, clusters of genital vesicles that ulcerate; milder recurrences (63)</td>
    <td><strong>No</strong>; research ongoing (chart)</td></tr>
    <tr><td><strong>Varicella zoster</strong></td><td>Respiratory droplets and lesion fluid; <strong>most infectious
    24&ndash;48 hours before lesions</strong>; shingles gives the unvaccinated chickenpox (68&ndash;69)</td><td>Chickenpox
    vesicles; shingles along a dermatome, painful (68&ndash;69)</td><td><strong>Yes</strong>: live attenuated, for
    chickenpox and shingles (69)</td></tr>
    <tr><td><strong>Cytomegalovirus</strong></td><td>Saliva, respiratory mucus, breast milk, urine, semen, cervical
    secretions, transplanted tissue (71); across the placenta (28)</td><td>Mostly asymptomatic; newborn liver and spleen
    enlargement, jaundice, microcephaly; retinitis in acquired immunodeficiency syndrome (72, 74)</td><td><strong>No</strong>;
    in development, hard without an animal model (74)</td></tr>
    <tr><td><strong>Epstein-Barr virus</strong></td><td>Direct oral contact and saliva (75)</td><td>Mononucleosis: sore
    throat, high fever, cervical lymphadenopathy, splenomegaly (75); Burkitt lymphoma, nasopharyngeal carcinoma (77)</td>
    <td><strong>No preventive vaccine</strong> (79)</td></tr>
    <tr><td><strong>Human herpesvirus 6</strong></td><td>Close contact with saliva and secretions (81)</td><td>Roseola:
    fever, then a faint rash, in babies (81)</td><td><strong>No</strong> (chart)</td></tr>
    <tr><td><strong>Human herpesvirus 7</strong></td><td>Contact with saliva (chart)</td><td>Roseola, like human herpesvirus 6
    (83)</td><td><strong>No</strong> (chart)</td></tr>
    <tr><td><strong>Human herpesvirus 8</strong></td><td>Saliva, sexual contact, blood transfusion, organ transplant
    (chart)</td><td>Kaposi sarcoma: small painless discolored skin lumps, may spread to internal organs (83)</td>
    <td><strong>No</strong> (chart)</td></tr>
    <tr><td><strong>Hepatitis B</strong></td><td>Minute amounts of blood and blood products; sexual (87); breaks in skin
    or mucous membrane, injection (88)</td><td>Most few symptoms, then immunity; malaise, fever, jaundice, rash,
    arthritis; chronic liver disease in a few (88)</td><td><strong>Yes</strong>: yeast-cloned surface antigen, 3 doses
    with boosters; hepatitis B immune globulin for the exposed (91)</td></tr>
    <tr><td><strong>Adenovirus</strong></td><td>Respiratory and ocular secretions (93); ingestion (chart)</td><td>Colds,
    pharyngitis, conjunctivitis, hemorrhagic cystitis, infantile gastroenteritis (93); type 41 hepatitis in children
    (94)</td><td><strong>Yes</strong>, for the military: types 4 and 7, oral (94)</td></tr>
    <tr><td><strong>Human papillomavirus</strong></td><td>Direct contact or contaminated fomites (97); sexual contact
    (chart)</td><td>Common, plantar and genital warts (97); reproductive cancers (99)</td><td><strong>Yes</strong>:
    Gardasil and Cervarix (99)</td></tr>
    <tr><td><strong>Polyomavirus</strong> (JC, BK)</td><td>Body fluids, contaminated food or water (chart); JC via tonsils
    or gastrointestinal tract (102)</td><td>JC: progressive multifocal leukoencephalopathy; BK: hematuria, hemorrhagic
    cystitis, nephritis after renal transplant (102)</td><td><strong>No</strong>, none for humans (chart)</td></tr>
    <tr><td><strong>Parvovirus B19</strong></td><td>Droplet infection (chart); mother to fetus (104)</td><td>Fifth disease
    (slapped-face rash, fever); hydrops fetalis; polyarthropathy; stopped red cell production (104)</td><td>None stated
    (the chart cell is blank)</td></tr>
    <tr><td><strong>Adeno-associated virus</strong></td><td>Not stated (needs adenovirus to replicate, 106)</td><td>Not
    known to cause disease alone; may worsen adenovirus hepatitis (106)</td><td>&mdash; (used as a gene therapy vector,
    106)</td></tr>
  </table></div>
  <div class="pearl"><p><strong>The vaccines in one line.</strong> Yes: variola (vaccinia), mpox, varicella zoster,
  hepatitis B, adenovirus (military, types 4 and 7), human papillomavirus. Animals only: cowpox. No: molluscum
  contagiosum, herpes simplex 1 and 2, cytomegalovirus, Epstein-Barr virus (no preventive vaccine), human herpesviruses
  6, 7 and 8, the polyomaviruses.</p></div>
"""

TEST = []
NOTES = []
