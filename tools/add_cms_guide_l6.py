#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Lecture 6 (Cutaneous Viral and Fungal Infections) section to the CMS I Exam 1 guide.

Lecture 6 sits BEFORE Lecture 7 in syllabus order, so it becomes section 6 and
everything after it shifts: Benign Skin Lesions 6 -> 7, Pigmented Skin Lesions
7 -> 8, and "How this course is built" 8 -> 9. The renumber is done by explicit,
asserted replacements rather than a blind regex, because a sloppy pass here
would silently renumber the Lecture 2 subsections too.

Instructional Objectives are quoted VERBATIM from the PAJ 5500 syllabus, per the
guide verbatim-IO rule -- including the syllabus's own duplicated "b." sub-item
letters, which are reproduced as written rather than tidied.

THE SLIDE IS AUTHORITATIVE (Jaxon, 2026-08-20): "especially Dr. Jaquith audio
because she says words wrong all the time, so go by the powerpoints unless told
otherwise." Everything below comes from the deck.

PHOTOGRAPH STRIPS. Per the standing rule that a visual subject gets pictures,
each subsection carries a `.figgrid` strip that reuses the comparison chart's
images IN PLACE -- no new bytes, and the two artifacts cannot drift. Every one
of those images was audited at full size first; see METAPHOR_IMAGES,
WRONG_DISEASE_IMAGES and MICROGRAPH_IMAGES in build_cms_derm_chart.py for the
four classes of picture that audit rejected in this deck.

Idempotent: fenced in <!--CMSL6--> and stripped before re-inserting.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
GUIDE = os.path.join(DIR, "cms-exam-1-study-guide.html")
IMGDIR = os.path.join(DIR, "cms-derm-chart-images")
OPEN, CLOSE = "<!--CMSL6-->", "<!--/CMSL6-->"
TOC_OPEN, TOC_CLOSE = "<!--CMSL6TOC-->", "<!--/CMSL6TOC-->"


def fig(stem, name, caption, slide):
    """One <figure>, resolving the real extension the extractor produced."""
    cand = [f for f in os.listdir(IMGDIR) if f.rsplit(".", 1)[0] == stem]
    assert cand, "no chart image for %r -- run build_cms_derm_chart.py first" % stem
    return ('<figure><img src="cms-derm-chart-images/%s" decoding="async" alt="%s &mdash; %s">'
            '<figcaption><span class="fg-name">%s</span>%s'
            '<span class="fg-cite">Lecture 6 &middot; Slide %d</span></figcaption></figure>'
            % (cand[0], name, caption, name, caption, slide))


def grid(items):
    return ('  <p class="figgrid-h">What these look like</p>\n  <div class="figgrid">'
            + "".join(fig(*i) for i in items) + "</div>\n")


SECTION = """
<section class="deck" id="viral-fungal">
  <h2 class="deck-title">6 &middot; Cutaneous Viral and Fungal Infections</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol type="a">
      <li>Interpret a potassium hydroxide (KOH) wet mount preparation</li>
      <li>Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic, including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis of the following cutaneous viral and fungal infections: <ol type="a"><li>Mycoses <ol><li>Dermatophyte infections (tinea)</li><li>Intertrigo</li><li>Id reaction</li><li>Pityriasis versicolor (tinea versicolor)</li><li>Candidiasis</li></ol></li><li>Verrucae (including plantar warts)</li><li>Varicella and herpes zoster</li><li>Molluscum contagiosum</li><li>Herpes simplex lesions, including. <ol><li>Herpetic Whitlow</li></ol></li><li>Onychomycosis</li></ol></li>
      <li>Identify medical care strategies for cutaneous viral and fungal infections in the lecture topic list for the following populations. <ol><li>infant</li><li>child</li><li>adolescent</li><li>adult</li><li>elderly</li></ol></li>
    </ol>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Before you start</span>
  <p><b>Where the lecture audio and a slide disagree on a fact, THE SLIDE WINS.</b> Every fact in this
  section, in the four Lecture 6 quizzes and in the Lecture 6 cram sheet entries comes from the
  PowerPoint. Nothing here was taken from the recording without being checked against a slide first.</p>
  </div>

  <h3 class="sub" id="vf-koh">6.1 &middot; Objective a &mdash; Reading a potassium hydroxide preparation</h3>
  <p>The whole point of the preparation is that potassium hydroxide <strong>dissolves keratin and leaves
  fungus behind</strong>, so what remains under the coverslip is the organism. What you are looking for
  depends on which organism you are chasing:</p>
  <table>
    <tr><th>Organism</th><th>What you see</th><th>Where to take the sample from</th></tr>
    <tr><td><b>Dermatophyte</b> (tinea)</td><td>Branching <b>hyphae</b></td><td>The <b>ACTIVE BORDER</b> of the lesion &mdash; not the cleared centre</td></tr>
    <tr><td><b><i>Malassezia</i></b> (pityriasis versicolor)</td><td><b>Short hyphae with clusters of yeast &mdash; &ldquo;spaghetti and meatballs&rdquo;</b></td><td>Fine scale, revealed by scraping or stretching the lesion</td></tr>
    <tr><td><b><i>Candida</i></b></td><td><b>Budding yeast and pseudohyphae</b></td><td>The affected fold, including a satellite lesion</td></tr>
    <tr><td><b>Onychomycosis</b></td><td>Fungal elements in nail material</td><td>The <b>most PROXIMAL accessible</b> diseased nail bed or subungual debris, after trimming the onycholytic nail</td></tr>
  </table>
  <p><strong>Three sampling rules carry most of the exam value here.</strong> Take dermatophyte samples
  from the <strong>advancing edge</strong>, because that is where the organism is and the centre is where
  it has already gone. Take nail samples <strong>proximally</strong>, not from the crumbling free edge.
  And in a suspected <strong>id reaction</strong>, sample <em>both</em> sites &mdash; the diagnosis is made
  by the <strong>pattern</strong>: positive at the primary infection, <strong>negative at the reaction</strong>.</p>
  <p>Two adjuncts, each with a limitation worth memorising. The <strong>Wood lamp</strong> may rapidly
  support <i>Microsporum</i> in tinea capitis, but <strong><i>Trichophyton tonsurans</i> &mdash; the
  commonest species in the United States &mdash; usually does not fluoresce</strong>, so a negative lamp
  excludes nothing. In pityriasis versicolor it may show <strong>yellow-gold</strong> fluorescence, but
  <strong>sensitivity is limited</strong>. Neither test is a substitute for the preparation.</p>

  <h3 class="sub" id="vf-tinea">6.2 &middot; Objective b &mdash; The dermatophytes, by body site</h3>
  <p><strong>Dermatophytes infect and survive only on DEAD KERATIN</strong> &mdash; the stratum corneum,
  hair and nails. They <strong>cannot survive on mucous membranes</strong>, which is the single fact that
  separates them from <i>Candida</i>. Three genera account for the majority:
  <strong><i>Microsporum</i>, <i>Trichophyton</i> and <i>Epidermophyton</i></strong>. The disease is then
  <strong>classified by body location</strong>, not by organism.</p>
  <table>
    <tr><th>Site</th><th>Name</th><th>The discriminating feature</th></tr>
    <tr><td>Scalp</td><td><b>Tinea capitis</b></td><td>Preadolescent children; broken hairs, <b>black dots</b>, lymphadenopathy. <b>Oral therapy required.</b></td></tr>
    <tr><td>Beard</td><td><b>Tinea barbae</b></td><td><b>Hairs are loose and easily removed</b> &mdash; unlike bacterial folliculitis. <b>Oral therapy required.</b></td></tr>
    <tr><td>Body</td><td><b>Tinea corporis</b></td><td><b>Central clearing</b> giving the annular &ldquo;ringworm&rdquo; outline</td></tr>
    <tr><td>Groin</td><td><b>Tinea cruris</b></td><td><b>The scrotum is typically SPARED</b></td></tr>
    <tr><td>Feet</td><td><b>Tinea pedis</b></td><td>Commonest dermatophyte infection <b>in adults</b>; three variants</td></tr>
    <tr><td>Hand</td><td><b>Tinea manuum</b></td><td><b>Two feet&ndash;one hand</b>: the hand used to scratch the foot</td></tr>
  </table>
  <p><strong>Why the scalp and beard are different.</strong> Both involve the <strong>hair shaft and
  follicle</strong>, and <strong>topical agents do not penetrate there</strong>. That is the entire reason
  those two sites demand oral therapy while a body or groin lesion does not. Pair the organism with the
  drug: <strong>terbinafine for <i>Trichophyton</i></strong>, <strong>griseofulvin for
  <i>Microsporum</i></strong>.</p>
  <p><strong>Tinea capitis is also a public-health problem, not just a scalp problem.</strong> Fungal
  particles stay <strong>viable for months</strong>, asymptomatic carriers exist, and transmission runs
  through people, <strong>pets</strong>, fallen hairs, clothing, combs, hats and furniture. Antifungal
  shampoo reduces spore shedding but <strong>never replaces the oral course</strong>. School exclusion is
  <strong>generally unnecessary once effective therapy has begun</strong>.</p>
  <p><strong>The three tinea pedis variants</strong> are worth separating, because the treatment differs
  for one of them:</p>
  <table>
    <tr><th>Variant</th><th>Appearance</th><th>Treatment note</th></tr>
    <tr><td><b>Interdigital</b> (most common)</td><td>Maceration and erosion, especially <b>3rd and 4th interspaces</b>, with fissures</td><td>Topical terbinafine, butenafine or an azole</td></tr>
    <tr><td><b>Hyperkeratotic</b></td><td>Plantar thickening in a <b>shoe distribution</b> &mdash; soles plus medial and lateral surfaces</td><td><b>Add a KERATOLYTIC</b> to the antifungal</td></tr>
    <tr><td><b>Vesiculobullous</b></td><td>The <b>moist acute</b> form &mdash; pruritic <b>and painful</b>, vesicles or bullae on erythema</td><td>Topical antifungal</td></tr>
  </table>
  <p><strong>Two traps in treatment.</strong> First, <strong>never use a corticosteroid&ndash;antifungal
  combination product</strong>: the steroid masks and worsens the dermatophytosis, producing tinea
  incognito. Second, treat tinea corporis <strong>1 to 2 cm beyond the visible border</strong>, because
  the advancing edge is where the organism is.</p>
@@FIG_TINEA@@
  <h3 class="sub" id="vf-nails">6.3 &middot; Objective b &mdash; Nails, distant reactions, and steroid-altered tinea</h3>
  <p><strong>Onychomycosis: confirm before you commit.</strong> The single most important sentence in this
  part of the deck is that <strong>many dystrophic nails are not fungal</strong> &mdash; the deck gives a
  whole slide of them &mdash; so <strong>confirm fungus before oral therapy</strong>. Confirmation can be
  potassium hydroxide microscopy, <strong>periodic acid&ndash;Schiff stain of clippings</strong>, culture,
  or polymerase chain reaction.</p>
  <p><strong>Oral terbinafine is first-line</strong> for most dermatophyte nail disease: usually
  <strong>6 weeks for fingernails, 12 weeks for toenails</strong>. Itraconazole is the alternative;
  <strong>fluconazole is off label in the United States</strong>. Limited disease can use topical
  efinaconazole, tavaborole or ciclopirox, at <strong>lower cure rates</strong>. Two counselling points
  follow directly: <strong>improvement requires nail growth</strong>, so appearance lags well behind
  treatment, and <strong>coexisting tinea pedis must be treated</strong> or the nail simply gets
  reinfected.</p>
  <p><strong>The id (dermatophytid) reaction</strong> is a dermatitis at a site <em>distant</em> from the
  infection &mdash; commonly the fingers, with tinea pedis as the primary. It appears
  <strong>1 to 2 weeks</strong> after the primary infection and is <strong>extremely pruritic</strong>. The
  mechanism is <strong>unknown</strong>, possibly delayed-type hypersensitivity. Three criteria establish it:</p>
  <table>
    <tr><td>1</td><td>A <b>dermatophyte infection on another part of the body</b></td></tr>
    <tr><td>2</td><td><b>Absence of fungal elements from the id reaction site</b></td></tr>
    <tr><td>3</td><td><b>Resolution of the id reaction when the primary infection is treated</b></td></tr>
  </table>
  <p>So the treatment is to <strong>treat the primary infection</strong> &mdash; and the examination point
  is to look for an <strong>asymptomatic fissure or maceration in the toe webs</strong> that the patient
  does not know about.</p>
  <p><strong>Tinea incognito</strong> is tinea whose appearance has been altered by inappropriate treatment,
  <strong>usually topical steroids</strong>. The cycle is recognisable: the steroid settles it, stopping the
  steroid flares it, and more steroid follows. Management is to <strong>stop the corticosteroid or
  calcineurin inhibitor</strong>, take potassium hydroxide and culture <strong>from an active edge</strong>,
  and <strong>warn that inflammation may rebound after withdrawal</strong> so the patient does not read the
  rebound as failure.</p>
@@FIG_NAILS@@
  <h3 class="sub" id="vf-yeast">6.4 &middot; Objective b &mdash; The yeasts: candidal intertrigo and pityriasis versicolor</h3>
  <p><strong>Yeasts are unicellular fungi that reproduce by budding</strong>, and both entities here behave
  quite differently from a dermatophyte.</p>
  <p><strong>Intertrigo</strong> is, first of all, <em>not</em> an infection: it is an inflammatory rash from
  <strong>friction, moisture and heat trapped in a body fold</strong>, which <strong><i>Candida</i> may then
  secondarily infect</strong>. That ordering matters, because it is why the first line of treatment is
  <strong>environmental</strong> &mdash; dry the folds gently, reduce friction and occlusion, use
  moisture-wicking or absorbent material, address incontinence or hyperhidrosis &mdash; and the antifungal
  comes second.</p>
  <p>Then the drug distinction the exam will want: <strong>topical nystatin treats <i>Candida</i> ONLY;
  topical azoles treat <i>Candida</i> AND many dermatophytes</strong>. A low-potency corticosteroid may be
  added <strong>briefly</strong> for marked inflammation, and <strong>only</strong> alongside adequate
  antifungal treatment.</p>
  <p><strong>Reading a fold rash:</strong> <strong>satellite papules or pustules support <i>Candida</i></strong>;
  <strong>malodor, erosions or drainage raise concern for bacterial coinfection</strong>. And in the groin
  specifically, <strong>scrotal involvement points away from tinea cruris</strong>, which typically spares
  it, and towards candidal intertrigo.</p>
  <p><strong>Pityriasis versicolor</strong> is an <strong>overgrowth of lipid-dependent <i>Malassezia</i>
  that normally lives on the skin</strong> &mdash; which is why it is <strong>NOT considered
  contagious</strong>, a counselling point patients need. It favours heat, humidity, oily skin, sweating,
  immunosuppression and corticosteroid exposure, and it recurs, especially in warm climates.</p>
  <p><strong>The pigment point.</strong> Lesions may be lighter, darker or pink.
  <strong>Hypopigmentation reflects altered melanocyte function and reduced tanning, and recovery can lag
  months behind clearance of the yeast.</strong> So <strong>colour change alone does not prove treatment
  failure</strong> &mdash; look for scale, or confirm with microscopy, before re-treating.</p>
  <p><strong>Treatment is topical first-line</strong> &mdash; ketoconazole, selenium sulfide, zinc
  pyrithione, ciclopirox or topical terbinafine; one common selenium sulfide approach is
  <strong>daily for 7 days with a 10-minute contact time</strong>. Systemic therapy is reserved for
  extensive, recurrent or refractory disease. Two drug facts are easy marks:</p>
  <table>
    <tr><td><b>Oral terbinafine is INEFFECTIVE</b></td><td>Adequate levels are not achieved <b>in sweat</b>. <b>Topical</b> terbinafine does work.</td></tr>
    <tr><td><b>Oral ketoconazole must NOT be used</b></td><td>Serious <b>hepatic and adrenal toxicity</b> outweighs the benefit in a superficial infection.</td></tr>
  </table>
@@FIG_YEAST@@
  <h3 class="sub" id="vf-vzv">6.5 &middot; Objective b &mdash; Varicella and herpes zoster</h3>
  <p><strong>Varicella</strong> is the primary infection. Its defining feature is
  <strong>lesions in multiple stages at once</strong> &mdash; macules, papules, vesicles and crusts
  present <em>simultaneously</em> &mdash; concentrated on the <strong>trunk, scalp and face</strong>.
  Management is supportive, and the drug rule is <strong>avoid aspirin in children</strong>, with caution
  around non-steroidal anti-inflammatories.</p>
  <p>Three prevention facts travel together. Contagiousness runs
  <strong>from 1 to 2 days BEFORE the rash until all lesions crust</strong> &mdash; and in breakthrough
  disease without crusts, until <strong>no new lesions for 24 hours</strong>. In healthcare settings use
  <strong>standard, airborne AND contact</strong> precautions. Primary prevention is
  <strong>two-dose varicella vaccination</strong>.</p>
  <p><strong>Herpes zoster</strong> is <strong>reactivation</strong> of virus that stayed latent in
  <strong>cranial-nerve or dorsal-root ganglia</strong>, travelling along a sensory nerve to the skin as
  cell-mediated immunity wanes. The eruption is confined to <strong>one or two adjacent dermatomes and
  STOPS ABRUPTLY AT THE MIDLINE</strong>. Distribution: <strong>thoracic 55%, cranial 20%, lumbar 15%,
  sacral 5%</strong>.</p>
  <table>
    <tr><th>Phase</th><th>What happens</th></tr>
    <tr><td><b>Pre-eruptive</b></td><td><b>Dysesthesia or pain within the dermatome</b>; lesions by <b>48&ndash;72 hours</b>. May have malaise, myalgia, headache, photophobia, rarely fever.</td></tr>
    <tr><td><b>Acute eruptive</b></td><td>Macules and papules, then <b>grouped herpetiform vesicles on an erythematous base</b> (the classic finding). New lesions over 3&ndash;5 days. <b>Infectious until lesions have dried.</b> Resolves over 10&ndash;15 days; complete healing may take a month. Some have <b>pain without eruption &mdash; zoster sine herpete</b>.</td></tr>
    <tr><td><b>Chronic</b></td><td><b>Postherpetic neuralgia</b> &mdash; see below.</td></tr>
  </table>
  <p><strong>The transmission point that gets missed:</strong> a susceptible contact does
  <strong>not &ldquo;catch shingles&rdquo;</strong>. Exposure to vesicular fluid, or airborne virus from
  disseminated disease, causes <strong>varicella</strong>. So cover the lesions and avoid susceptible
  pregnant people, premature infants and immunocompromised people until crusted.</p>
  <p><strong>Antiviral timing.</strong> Valacyclovir, famciclovir or acyclovir, started
  <strong>as soon as possible, ideally within 72 hours</strong>. But treat <strong>after</strong> 72 hours
  when <strong>new lesions are forming</strong>, or there is ophthalmic, neurologic, disseminated, severe or
  immunocompromised disease. Severe disseminated, visceral, central nervous system or sight-threatening
  disease gets <strong>intravenous acyclovir</strong> and specialist management.</p>
  <p><strong>Postherpetic neuralgia</strong> is the <strong>most common complication</strong>, defined as
  <strong>pain persisting 90 days or more after rash onset</strong>: burning, aching, stabbing, electric
  shock-like, or <strong>evoked by light touch (allodynia)</strong>. Risk rises with <strong>age, severe
  acute pain, severe rash, ophthalmic involvement and immunocompromise</strong>. First line is
  <strong>gabapentin or pregabalin, an appropriate tricyclic antidepressant, or topical lidocaine</strong>;
  a capsaicin patch may help; <strong>avoid routine long-term opioids</strong>.</p>
  <p><strong>Learn this one as a sentence:</strong> <strong>topical and systemic corticosteroids do NOT
  prevent postherpetic neuralgia, and must never replace antiviral therapy.</strong></p>
  <p>Two complications carry their own urgency:</p>
  <table>
    <tr><th></th><th>Herpes zoster ophthalmicus</th><th>Ramsay Hunt syndrome</th></tr>
    <tr><td>What</td><td>Ophthalmic division (V1) of cranial nerve V</td><td><b>Peripheral facial palsy</b> with painful vesicles of the ear canal, auricle or oropharynx; hearing loss, tinnitus or vertigo may occur</td></tr>
    <tr><td>The sign</td><td><b>Hutchinson sign</b> &mdash; lesions on the tip or side of the nose &mdash; raises ocular risk, but <b>its ABSENCE does NOT exclude eye involvement</b></td><td>&mdash;</td></tr>
    <tr><td>Do</td><td><b>Start systemic antiviral immediately</b>; <b>same-day ophthalmology</b> for eye pain, visual symptoms, red eye, photophobia, Hutchinson sign, or eyelid/ocular involvement</td><td><b>Antiviral PLUS systemic corticosteroid early</b> when not contraindicated; urgent ear, nose and throat or neurology; <b>protect the cornea</b> if eyelid closure is impaired</td></tr>
  </table>
  <p><strong>Prevention with Shingrix:</strong> <strong>two doses</strong> of recombinant zoster vaccine for
  immunocompetent adults <strong>50 and over</strong>, and <strong>two doses</strong> for adults
  <strong>19 and over</strong> who <strong>are or will be</strong> immunodeficient or immunosuppressed.
  Standard interval <strong>2 to 6 months</strong>; for immunocompromised patients the second dose may be
  given <strong>1 to 2 months</strong> after the first when faster completion helps.</p>
@@FIG_VZV@@
  <h3 class="sub" id="vf-hsv">6.6 &middot; Objective b &mdash; Herpes simplex and herpetic whitlow</h3>
  <p>Start with the fact that undoes the usual assumption: <strong>either type can cause oral or genital
  infection, so lesion location does NOT reliably determine type</strong>. What does differ is behaviour
  over time &mdash; <strong>HSV-1 genital infection generally recurs and sheds less often than HSV-2
  genital infection</strong>.</p>
  <p>Transmission occurs through contact with infected oral or genital secretions or lesions, and
  <strong>can occur during asymptomatic shedding</strong>. It is a double-stranded DNA
  <strong>Herpesviridae</strong> virus, <strong>neurovirulent</strong>, producing <strong>latent but
  lifelong infection</strong>.</p>
  <p><strong>First episodes are more prominent and longer; recurrences are milder and shorter.</strong>
  A prodrome of tenderness, pain, paresthesias or burning precedes the lesions &mdash; with localized pain,
  tender lymphadenopathy, headache, generalized aching and fever characteristic &mdash; though
  <strong>some patients have no prodrome</strong>. On examination: <strong>grouped vesicles on an
  erythematous base breaking down into a shallow painful ulcer</strong>, lasting about two weeks and
  <strong>healing without scarring</strong>. Reactivation triggers are <strong>stress, illness,
  menstruation and ultraviolet light</strong>.</p>
  <p><strong>Testing has four rules, and two of them are prohibitions.</strong></p>
  <table>
    <tr><td><b>Do</b></td><td>Swab a <b>fresh vesicle, ulcer base or crust</b> for <b>type-specific amplification testing</b> &mdash; the preferred test</td></tr>
    <tr><td><b>Know</b></td><td><b>Culture is less sensitive</b>, especially in healing or recurrent lesions, and a <b>negative result does not exclude</b>. A negative older-lesion swab does not exclude either, <b>because shedding is intermittent</b>.</td></tr>
    <tr><td><b>Do NOT</b></td><td><b>Use HSV immunoglobulin M.</b> Confirm a low-positive HSV-2 serology with a <b>second method</b>.</td></tr>
    <tr><td><b>Do NOT</b></td><td><b>Routinely screen asymptomatic adults serologically.</b></td></tr>
  </table>
  <p>And evaluate a genital ulcer for <strong>other causes including syphilis</strong>, by risk. The
  differential is worth holding as a contrast: <strong>chancroid</strong> (<i>Haemophilus ducreyi</i>,
  <strong>painful</strong> necrotizing ulcers, inguinal lymphadenopathy) against <strong>syphilis</strong>
  (solitary raised papules that erode, <strong>usually painless</strong>), plus trauma and candidiasis.</p>
  <p><strong>Treat every first clinical episode</strong> with oral acyclovir, valacyclovir or famciclovir.
  For recurrent genital disease, choose between <strong>patient-initiated episodic</strong> and
  <strong>daily suppressive</strong> therapy. <strong>Topical antivirals provide minimal benefit.</strong></p>
  <p>Counselling is where the honest wording matters: <strong>suppressive valacyclovir LOWERS HSV-2
  transmission, and condoms REDUCE but do not eliminate risk</strong> &mdash; neither abolishes it. Avoid
  sexual or direct lesion contact <strong>during the prodrome</strong> as well as while lesions are active.</p>
  <p><strong>Herpetic whitlow</strong> is HSV of the <strong>distal finger</strong>, often inoculated
  through broken skin: prodromal burning or tingling, then <strong>grouped vesicles on an erythematous,
  swollen digit</strong>, sometimes with fever or lymphangitis. It mimics <strong>bacterial felon or
  paronychia, contact dermatitis, and blistering dactylitis</strong>, which sets up the one instruction to
  carry out of this topic: <strong>DO NOT incise and drain &mdash; it does not treat HSV and can delay
  healing.</strong> Cover the lesions, use hand hygiene, avoid contact with mucosa or broken skin until
  healed, and treat bacterial superinfection <strong>only when it is present</strong>.</p>
@@FIG_HSV@@
  <h3 class="sub" id="vf-warts">6.7 &middot; Objective b &mdash; Molluscum contagiosum and warts</h3>
  <p><strong>Molluscum contagiosum</strong> is a benign <strong>poxvirus</strong> infection producing
  <strong>smooth, dome-shaped, centrally umbilicated papules</strong> &mdash; discrete, firm, flesh-coloured
  and pearly, averaging <strong>3 to 5 mm</strong>, with <strong>central umbilication characteristic</strong>.
  It spreads by direct skin contact, shared contaminated objects and <strong>autoinoculation</strong>.</p>
  <p><strong>Most immunocompetent patients clear spontaneously, though it may take months to several
  years</strong> &mdash; and that slow timeline is exactly why <strong>observation is appropriate for many
  patients: procedures may blister, pigment or scar</strong>. When treatment is chosen:</p>
  <table>
    <tr><th>Agent</th><th>Applied by</th><th>From age</th></tr>
    <tr><td><b>Berdazimer 10.3% gel (Zelsuvmi)</b>, once daily</td><td><b>At home</b></td><td><b>1 year</b></td></tr>
    <tr><td><b>Cantharidin 0.7% (Ycanth)</b></td><td><b>A clinician</b></td><td><b>2 years</b></td></tr>
    <tr><td>Curettage or cryotherapy</td><td>A clinician</td><td>&mdash;</td></tr>
    <tr><td>Topical retinoids</td><td colspan="2"><b>Off label</b></td></tr>
  </table>
  <p><strong>Three higher-risk presentations</strong> change what you do. Genital lesions in adolescents or
  adults <strong>may be sexually transmitted</strong>; assess for other infections as appropriate. Genital
  lesions <strong>in a child require context-sensitive assessment &mdash; location alone does NOT prove
  abuse</strong>. And <strong>extensive or giant facial lesions warrant evaluation for
  immunosuppression</strong>, including HIV where appropriate.</p>
  <p><strong>Warts</strong> are benign proliferations caused by <strong>human papillomavirus</strong>
  infecting <strong>keratinocytes</strong>, transmitted by skin-to-skin contact, autoinoculation and
  contaminated surfaces. The anatomy is a favourite point: a wart is
  <strong>confined to the EPIDERMIS</strong>, but it <strong>expands and displaces the dermis</strong>,
  giving the impression that it extends deeper. Turn one over and the underside is
  <strong>round and smooth &mdash; there are NO ROOTS</strong>.</p>
  <table>
    <tr><th>Type</th><th>Appearance</th><th>Where</th></tr>
    <tr><td><b>Verruca vulgaris</b></td><td>Under 1 cm, elevated round papules, <b>rough greyish surface</b>. <b>Tiny red or black dots are thrombosed dilated capillaries</b>; trimming the surface makes them more prominent.</td><td>Hands, favouring fingers and palms. <b>Periungual, lip and tongue in nail biters.</b> Ages <b>5&ndash;20</b>.</td></tr>
    <tr><td><b>Verruca plana</b> (flat)</td><td>Multiple smooth, slightly elevated, <b>flat-topped</b>, skin-coloured to light-brown papules</td><td>Face, forehead, dorsal hands, shins. <b>Shaving spreads them by autoinoculation.</b></td></tr>
    <tr><td><b>Verruca plantaris</b></td><td>On the <b>weight-bearing surface</b>; clustering produces a <b>mosaic wart</b></td><td>Soles. <b>Therapy only if PAINFUL.</b> Salicylic acid 40% or cryotherapy.</td></tr>
  </table>
  <p>Diagnosis is clinical; <strong>biopsy is generally unnecessary</strong> but may suit immunocompromised
  patients or <strong>lesions of uncertain etiology &mdash; that is, ruling out squamous cell
  carcinoma</strong>, which sits in the differential alongside molluscum contagiosum and seborrheic
  keratosis.</p>
  <p><strong>The treatment principle to state plainly to a patient:</strong> <strong>no therapy eradicates
  human papillomavirus with certainty, and recurrence can occur.</strong> Choose treatment by
  <strong>location, symptoms, age, pregnancy status, immune status, and risk of scarring or
  dyspigmentation</strong>. <strong>Avoid excessive freezing or destructive therapy for benign lesions
  likely to resolve spontaneously</strong> &mdash; cryotherapy every 2 to 3 weeks may cause pain, blistering
  and pigment change. <strong>Biopsy or refer atypical, bleeding, ulcerated, growing or refractory
  lesions</strong>, and refer <strong>periungual, facial, extensive, recalcitrant, diagnostically uncertain
  or immunocompromised</strong> cases.</p>
@@FIG_WARTS@@
  <h3 class="sub" id="vf-age">6.8 &middot; Objective c &mdash; Care strategies by age</h3>
  <p>Objective c asks you to apply all of the above across infant, child, adolescent, adult and elderly
  populations. The deck's age-specific content clusters as follows:</p>
  <table>
    <tr><th>Population</th><th>What changes</th></tr>
    <tr><td><b>Infant</b></td><td><b>Newborn age increases varicella complication risk</b>, and neonatal exposure warrants prompt consultation. Molluscum: <b>berdazimer is approved from age 1</b>. Intertrigo in the diaper area and folds.</td></tr>
    <tr><td><b>Child</b></td><td><b>Tinea capitis is predominantly a disease of preadolescent children</b> and the commonest fungal infection in children &mdash; oral therapy, adjunctive shampoo, contact and pet evaluation, and generally <b>no school exclusion once treated</b>. <b>Avoid aspirin</b> in varicella. Molluscum is common and usually self-limiting; <b>cantharidin from age 2</b>. <b>Genital molluscum requires context-sensitive assessment.</b> Common warts peak at <b>5&ndash;20</b>.</td></tr>
    <tr><td><b>Adolescent</b></td><td>After puberty, <b>sebum fatty acid changes inhibit scalp dermatophyte growth</b>, so tinea capitis falls away. Tinea cruris and tinea pedis rise with sport, occlusive footwear and communal showers. <b>Genital molluscum may be sexually transmitted</b> &mdash; assess accordingly. Flat warts spread by <b>shaving</b>. Zoster vaccine from <b>19</b> if immunosuppressed or about to be.</td></tr>
    <tr><td><b>Adult</b></td><td><b>Tinea pedis is the commonest dermatophyte infection in adults</b>; tinea cruris is commoner in men. <b>Adults and pregnancy increase varicella complication risk.</b> Herpes simplex counselling and suppressive therapy. <b>Shingrix two doses from 50</b> in the immunocompetent. Check <b>pregnancy status</b> before choosing a wart treatment.</td></tr>
    <tr><td><b>Elderly</b></td><td><b>Zoster risk rises with age</b>, and so does <b>postherpetic neuralgia</b> risk. Individualize neuropathic agents for <b>kidney function, falls, anticholinergic burden and interactions</b>. Onychomycosis risk rises with <b>age, diabetes and vascular disease</b>; check hepatic disease and interactions before oral terbinafine. Intertrigo risk rises with <b>immobility and incontinence</b>.</td></tr>
  </table>
  <p><strong>Immunocompromise cuts across every age</strong> and changes the answer in the same direction
  each time: more extensive disease, a lower threshold for systemic therapy, amplification testing rather
  than clinical diagnosis, and referral. It raises complication risk in varicella, drives atypical and
  disseminated zoster, produces more numerous or giant molluscum lesions, and moves warts and
  dermatophytosis towards oral therapy and specialist input.</p>
</section>

"""

TOC = """  <a class="top-link" href="#viral-fungal">6 &middot; Cutaneous Viral and Fungal Infections</a>
  <a href="#vf-koh">6.1 Objective a &mdash; Reading a potassium hydroxide preparation</a>
  <a href="#vf-tinea">6.2 Objective b &mdash; The dermatophytes, by body site</a>
  <a href="#vf-nails">6.3 Objective b &mdash; Nails, distant reactions &amp; steroid-altered tinea</a>
  <a href="#vf-yeast">6.4 Objective b &mdash; Candidal intertrigo &amp; pityriasis versicolor</a>
  <a href="#vf-vzv">6.5 Objective b &mdash; Varicella and herpes zoster</a>
  <a href="#vf-hsv">6.6 Objective b &mdash; Herpes simplex and herpetic whitlow</a>
  <a href="#vf-warts">6.7 Objective b &mdash; Molluscum contagiosum and warts</a>
  <a href="#vf-age">6.8 Objective c &mdash; Care strategies by age</a>
"""

FIGS = {
 "@@FIG_TINEA@@": grid([
   ("l6_s009_1", "Tinea capitis", "Scaly grey patches with broken hairs; preadolescent children", 9),
   ("l6_s011_1", "Black dot tinea capitis", "Hair fractured at the surface leaves visible black dots", 11),
   ("l6_s020_1", "Tinea barbae &mdash; inflammatory", "Boggy pustular kerion-like plaque; hairs pull out easily", 20),
   ("l6_s024_2", "Tinea corporis", "Sharply circumscribed plaque clearing centrally into a ring", 24),
   ("l6_s032_1", "Tinea cruris", "Crural fold plaque on the medial thigh; scrotum spared", 32),
   ("l6_s038_2", "Tinea pedis &mdash; interdigital", "Maceration and erosion in the toe web spaces", 38),
   ("l6_s040_2", "Tinea pedis &mdash; hyperkeratotic", "Diffuse plantar thickening in a shoe distribution", 40),
   ("l6_s054_1", "Tinea manuum", "Thickened dry scaly palm; often mistaken for manual labour", 54),
 ]),
 "@@FIG_NAILS@@": grid([
   ("l6_s048_1", "Onychomycosis", "Thickening, discoloration, onycholysis and crumbling", 48),
   ("l6_s060_1", "Id (dermatophytid) reaction", "Itchy papulovesicles on the hand, distant from the infection", 60),
   ("l6_s064_1", "Tinea incognito", "Tinea altered in appearance by topical corticosteroid", 64),
 ]),
 "@@FIG_YEAST@@": grid([
   ("l6_s069_2", "Candidal intertrigo", "Fold erythema with satellite papules and pustules", 69),
   ("l6_s076_1", "Pityriasis versicolor", "Finely scaling macules on the trunk, lighter or darker", 76),
 ]),
 "@@FIG_VZV@@": grid([
   ("l6_s084_1", "Varicella", "Lesions in several stages at once on the trunk", 84),
   ("l6_s100_1", "Herpes zoster", "Grouped vesicles in one dermatome, stopping at the midline", 100),
   ("l6_s103_1", "Herpes zoster ophthalmicus", "V1 distribution; check the nose tip for Hutchinson sign", 103),
   ("l6_s104_1", "Ramsay Hunt syndrome", "Vesicles of the ear canal and auricle with facial palsy", 104),
 ]),
 "@@FIG_HSV@@": grid([
   ("l6_s113_3", "Herpes simplex", "Grouped vesicles breaking down to a shallow painful ulcer", 113),
   ("l6_s127_1", "Herpetic whitlow", "Painful swollen distal finger &mdash; do NOT incise and drain", 127),
 ]),
 "@@FIG_WARTS@@": grid([
   ("l6_s131_1", "Molluscum contagiosum", "Pearly dome-shaped papules with central umbilication", 131),
   ("l6_s142_1", "Verruca vulgaris", "Rough greyish papule; black dots are thrombosed capillaries", 142),
   ("l6_s144_2", "Verruca plana", "Multiple smooth flat-topped papules; shaving spreads them", 144),
   ("l6_s146_1", "Verruca plantaris", "Weight-bearing surface; clusters form a mosaic wart", 146),
 ]),
}

# Renumbering: Lecture 6 takes slot 6, so everything after it moves up one.
# Explicit and asserted, never a blind regex -- a loose pass would renumber the
# Lecture 2 subsections too.
RENUMBER = [
 ('<h2 class="deck-title">6 &middot; Benign Skin Lesions</h2>',
  '<h2 class="deck-title">7 &middot; Benign Skin Lesions</h2>'),
 ('<h2 class="deck-title">7 &middot; Pigmented Skin Lesions</h2>',
  '<h2 class="deck-title">8 &middot; Pigmented Skin Lesions</h2>'),
 ('<h2 class="deck-title">8 &middot; How this course is built</h2>',
  '<h2 class="deck-title">9 &middot; How this course is built</h2>'),
 ('href="#benign-skin-lesions">6 &middot; Benign Skin Lesions</a>',
  'href="#benign-skin-lesions">7 &middot; Benign Skin Lesions</a>'),
 ('href="#pigmented-lesions">7 &middot; Pigmented Skin Lesions</a>',
  'href="#pigmented-lesions">8 &middot; Pigmented Skin Lesions</a>'),
 ('href="#how-course-works" style="color:#8a6508">8 &middot; How this course is built</a>',
  'href="#how-course-works" style="color:#8a6508">9 &middot; How this course is built</a>'),
]
for a, b in [("bsl-mechanical", 1), ("bsl-scars", 2), ("bsl-keratotic", 3), ("bsl-pressure", 4),
             ("bsl-nodules", 5), ("bsl-vascular", 6), ("bsl-other", 7)]:
    RENUMBER.append(('href="#%s">6.%d ' % (a, b), 'href="#%s">7.%d ' % (a, b)))
    RENUMBER.append(('id="%s">6.%d &middot;' % (a, b), 'id="%s">7.%d &middot;' % (a, b)))
for a, b in [("psl-flat", 1), ("psl-keratoses", 2), ("psl-vitiligo", 3), ("psl-naevi", 4), ("psl-age", 5)]:
    RENUMBER.append(('href="#%s">7.%d ' % (a, b), 'href="#%s">8.%d ' % (a, b)))
    RENUMBER.append(('id="%s">7.%d &middot;' % (a, b), 'id="%s">8.%d &middot;' % (a, b)))


def main():
    src = open(GUIDE, encoding="utf-8").read()

    # idempotent: strip any previous run first
    for o, c in ((OPEN, CLOSE), (TOC_OPEN, TOC_CLOSE)):
        if o in src:
            src = re.sub(re.escape(o) + r".*?" + re.escape(c), "", src, flags=re.S)

    body = SECTION
    for token, html in FIGS.items():
        assert token in body, "figure token %s never used" % token
        body = body.replace(token, html)
    assert "@@" not in body, "an unreplaced token survived"

    # renumber, but only if not already done (so a re-run is safe)
    for old, new in RENUMBER:
        if new in src and old not in src:
            continue                      # already renumbered by an earlier run
        assert src.count(old) == 1, "renumber target not found exactly once: %r" % old
        src = src.replace(old, new, 1)

    # The header blurb lists the decks the guide covers, and it had gone stale
    # BEFORE this build: Benign Skin Lesions was already written as section 6 but
    # the header still advertised it as pending. Rewrite the whole pair of lines
    # rather than patching a number, so the list and the "still to come" note can
    # never disagree again. Idempotent -- skipped once it is already correct.
    OLD_HDR = ("""  <p><b>Lecture 1</b> clinical reasoning, then the dermatology block &mdash;\n"""
               """     <b>2</b> General Dermatology I &middot; <b>3</b> Dermatology II &middot;\n"""
               """     <b>4</b> Cutaneous Bacterial Infections &middot; <b>5</b> Dermatological Infestations &middot;\n"""
               """     <b>8</b> Pigmented Skin Lesions</p>\n"""
               """  <p style="opacity:.9">Sections 6, 7 and 9 are added when those decks are posted &middot;\n""")
    NEW_HDR = ("""  <p><b>Lecture 1</b> clinical reasoning, then the dermatology block &mdash;\n"""
               """     <b>2</b> General Dermatology I &middot; <b>3</b> Dermatology II &middot;\n"""
               """     <b>4</b> Cutaneous Bacterial Infections &middot; <b>5</b> Dermatological Infestations &middot;\n"""
               """     <b>6</b> Cutaneous Viral and Fungal Infections &middot; <b>7</b> Benign Skin Lesions &middot;\n"""
               """     <b>8</b> Pigmented Skin Lesions</p>\n"""
               """  <p style="opacity:.9">Pre-Malignant and Malignant Skin Lesions is added when that deck is posted &middot;\n""")
    if NEW_HDR not in src:
        assert src.count(OLD_HDR) == 1, "header blurb not found in its expected form"
        src = src.replace(OLD_HDR, NEW_HDR, 1)

    toc_anchor = "  <!--CMSL7TOC-->"
    assert src.count(toc_anchor) == 1
    src = src.replace(toc_anchor, TOC_OPEN + "\n" + TOC + TOC_CLOSE + "\n" + toc_anchor, 1)

    sec_anchor = '<section class="deck" id="benign-skin-lesions">'
    assert src.count(sec_anchor) == 1
    src = src.replace(sec_anchor, OPEN + body + CLOSE + "\n\n" + sec_anchor, 1)

    # Validate BEFORE writing -- a builder that writes then asserts leaves a bad
    # file behind and needs a git checkout to recover.
    assert src.count('id="viral-fungal"') == 1
    assert 'loading="lazy"' not in "".join(re.findall(r"<img\b[^>]*>", src)), \
        "lazy images will not survive Download as PDF"
    for stem in ("l6_s009_1", "l6_s142_1"):
        assert stem in src, "figure %s did not make it into the guide" % stem
    open(GUIDE, "w", encoding="utf-8").write(src)
    n_fig = len(re.findall(r'<figure><img src="cms-derm-chart-images/l6_', src))
    print("added section 6 (%d subsections, %d Lecture 6 photographs)"
          % (len(re.findall(r'<h3 class="sub" id="vf-', src)), n_fig))
    print("renumbered Benign Skin Lesions 6->7, Pigmented 7->8, How this course is built 8->9")


if __name__ == "__main__":
    main()
