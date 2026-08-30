# -*- coding: utf-8 -*-
"""What Dr. Wood told the class to star -- Pharmacology I Exam 1.

Source is the LECTURE RECORDINGS, not the slides. That is the whole point of
this page: the decks do not say which facts he considers testable, and he told
the class outright, roughly fifty times.

Two fields per entry:
  quote   what he said, cleaned of transcription noise for reading
  verify  raw substrings that must appear in the transcript, checked by
          check_pharm_wood.py

They differ because the transcript has Whisper errors on exactly the words that
matter -- "tritogenic" for teratogenic, "pants" for PANCE, "read from head to
toe" for red, "into bivolol" for nebivolol, "carvetolol" for carvedilol. The
quote is corrected so it reads properly; the verify string keeps the raw text so
the check still matches the file on disk.

Transcripts live in the Desktop inbox and are NEVER copied into this repo.
"""
L1 = 1
L2 = 2
L3 = 3

# ---------------------------------------------------------------- the marker
MARKER = dict(
    quote="So anytime I say like, hey, note this, this is really notable &mdash; that&rsquo;s "
          "something you should probably be starring. Because again, think about those kinds of "
          "things and write test questions, right?",
    lec=L1, at="1:31:34",
    verify=["this is really notable", "something you should probably be starring",
            "write test questions"])

# ------------------------------------------------------------ standing rules
RULES = [
 dict(title="QT prolongation", said="twice",
      quote="Anytime we see QT prolongation, you should star that, underline it, whatever you "
            "need to do.",
      second="&hellip; that causes QT prolongation &mdash; star it, underline it, it&rsquo;s good to know.",
      lec=L1, at="1:13:45 and 1:16:26",
      body="It spans three classes on this exam: <b>macrolides</b> (worse with class Ia and III "
           "antiarrhythmics and with electrolyte abnormalities), <b>fluoroquinolones</b>, and "
           "<b>posaconazole</b> (whose QT risk runs mostly through the hypokalaemia and "
           "hypomagnesaemia it causes). He flagged it the first time it appeared and again three "
           "minutes later.<br><br>What he actually taught around it: the QT interval is how long "
           "the ventricle takes to <b>repolarise</b>, and it lengthens because the drug blocks the "
           "potassium channel that lets K<sup>+</sup> out of the cell &mdash; the slide names it the "
           "<b>hERG</b> channel. A long enough QT degenerates into <b>torsades de pointes</b>, "
           "French for &ldquo;twisting of the points&rdquo;, a ventricular arrhythmia he called "
           "<i>not compatible with life</i>. Three things multiply the risk: a <b>congenital long "
           "QT</b>, <b>several QT-prolonging drugs stacked together</b>, and <b>electrolyte "
           "disturbance</b> &mdash; a single Z-Pak in a healthy person did not worry him. The "
           "treatment of choice for torsades is <b>magnesium sulfate</b>, two grams, which he "
           "called the &ldquo;two gram slam&rdquo; and said was worth remembering.",
      verify=["Anytime we see QT prolongation", "you should star that", "underline it",
              "star it, underline it, it's good to know"]),
 dict(title="MRSA coverage", said="once, emphatically",
      quote="Again, anytime you see MRSA coverage &mdash; star it, highlight it, underline it, right? "
            "Pseudomonas, C. diff, those are all things you want to be thinking about. Kind of big "
            "notable bugs.",
      lec=L1, at="1:43:54",
      body="On this exam the agents with MRSA coverage are <b>vancomycin</b>, <b>linezolid</b>, "
           "<b>clindamycin</b>, <b>ceftaroline</b>, <b>tetracyclines</b> and <b>tigecycline</b> "
           "(not VRE), plus topical <b>mupirocin</b>. He introduced <i>Staphylococcus aureus</i> "
           "early as &ldquo;a very notable bug&hellip; especially when we talk about the dreaded "
           "MRSA.&rdquo;",
      verify=["anytime you see MRSA coverage", "star it, highlight it, underline it",
              "Kind of big notable bugs"]),
 dict(title="Teratogenic drugs", said="once, about itraconazole",
      quote="This is also an example of a drug that is teratogenic. That means it can cause harm to "
            "a fetus, and so you would need to check a pregnancy prior to giving this. So anytime we "
            "see a teratogenic drug, also note that, because it can be very significant &mdash; "
            "especially because a lot of patients, when they&rsquo;re first pregnant, may not know "
            "it, and they can go weeks before they know.",
      lec=L1, at="2:05:51",
      body="The teratogens on this exam are <b>itraconazole</b>, <b>fluconazole</b> and "
           "<b>voriconazole</b> (the last two &ldquo;teratogenic in animals&rdquo;), plus "
           "<b>isotretinoin</b>, which he called <i>extremely</i> teratogenic in Lecture 2 "
           "and placed in <b>pregnancy category X</b> &mdash; his definition: &ldquo;no situation "
           "in which the benefits of this drug outweigh the risk to a developing fetus,&rdquo; with "
           "effects running from malformation to fetal death. <b>Topical retinoids</b> are avoided "
           "in pregnancy as well, and <b>tetracyclines</b> in the second and third trimesters &mdash; "
           "stated as an outright contraindication when he restated it in Lecture 2. The action he "
           "wants is the same every time: check a pregnancy test before you prescribe to anyone of "
           "childbearing potential.",
      verify=["a drug that is tritogenic", "cause harm to a fetus", "check a pregnancy",
              "also note that because it can be very significant"]),
 dict(title="Rebound after three days", said="and he said students always miss it",
      quote="For whatever reason, even though I highlight it every time I talk about this drug, I "
            "always talk about which of these drugs can cause rebound nasal stuffiness, or rebound "
            "ocular redness, when used for more than three days. And for whatever reason, students "
            "have a really tough time with this one&hellip; if you get it wrong on the test, which I "
            "hope you don&rsquo;t, you&rsquo;ll be able to say, oh, he did warn me about that. I "
            "should have underlined it, starred it, whatever.",
      lec=L3, at="1:42:12",
      body="This is <b>oxymetazoline (Afrin)</b> and the condition is <b>rhinitis medicamentosa</b> "
           "&mdash; rebound congestion from overstimulated alpha receptors downregulating, so the "
           "congestion returns when the drug stops. He notes it needs a <b>taper</b>, not an abrupt "
           "stop. Worth noting: he flagged this harder than any other single fact in Lecture 3.",
      verify=["rebound nasal stuffiness", "rebound", "when used for more than three days",
              "students have a really tough time with this one",
              "I should have underlined it, starred it"]),
]

# -------------------------------------------------------- test-question shapes
PATTERNS = [
 dict(title="Pneumonia + hotel + contaminated air conditioning &rarr; <i>Legionella</i>",
      quote="If you ever see a test question &mdash; ever, ever, ever, on the PANCE or anywhere else "
            "&mdash; where it says, hey, the patient was coming in for a pneumonia and they were at a "
            "hotel and the AC unit was contaminated, it&rsquo;s always <i>Legionella</i>.",
      lec=L1, at="1:11:29",
      body="He then gave the reason it is a stock stem: Legionnaires&rsquo; disease was discovered "
           "from <i>Legionella</i> contaminating an air-conditioning unit during an American Legion "
           "convention at a hotel. He called it a <b>classic scenario</b>. <i>Legionella</i> is an "
           "<b>atypical</b>, so the answer is a <b>macrolide</b>, a <b>tetracycline</b> or a "
           "<b>respiratory fluoroquinolone</b>.",
      verify=["If you ever see a test question", "the patient was coming in", "for a pneumonia",
              "the AC unit was contaminated, it's always Legionella", "Classic scenario"]),
 dict(title="Red head to toe + itching + infused over 30 minutes &rarr; vancomycin",
      quote="If I said, okay, test question &mdash; a patient was getting an antibiotic infused and "
            "all of a sudden they&rsquo;re red from head to toe and complaining of some itching, "
            "medication was infused over 30 minutes. What&rsquo;s most likely to cause that?",
      lec=L3, at="2:15:40",
      body="He answered it himself: <b>vancomycin infusion syndrome</b> &mdash; and gave the fix, "
           "which is <b>running it over about two hours</b> rather than 30 minutes. The infusion "
           "RATE is the whole answer; this is not an allergy.",
      verify=["test question, a patient was getting an antibiotic",
              "read from head to toe and complaining of some itching",
              "medication was infused over 30 minutes", "vancomycin infusion syndrome"]),
 dict(title="Toxic shock after a retained tampon &rarr; clindamycin",
      quote="This can also be used for things like toxin-mediated diseases, because the clindamycin "
            "can actually bind to the toxin. So if you ever hear of toxic shock syndrome &mdash; or "
            "the classic sort of presentation is, a girl left in a tampon for too long and then all "
            "of a sudden gets septic shock from that, due to toxins being released by bacteria "
            "&mdash; clindamycin can be utilised for that.",
      lec=L1, at="1:41:19",
      body="He calls it <b>&ldquo;a unique sort of point&rdquo;</b> for clindamycin. The mechanism "
           "is the thing to carry: it <b>binds the toxin</b>, which is why it beats an agent that "
           "merely kills the organism in a toxin-mediated illness.",
      verify=["toxin mediated diseases", "clindamycin can actually bind to the toxin",
              "toxic shock syndrome", "left in a tampon for too long"]),
 dict(title="Acne, benzoyl peroxide too irritating &rarr; topical retinoid",
      quote="If I say on a test question &mdash; hey, they&rsquo;re presenting for treatment for "
            "acne, they say they use benzoyl peroxide but it&rsquo;s just that their skin got so "
            "irritated they didn&rsquo;t want to continue it. What do you go to next? Topical "
            "retinoids kind of makes sense from that standpoint.",
      lec=L2, at="48:20",
      body="A <b>next-step</b> stem rather than a diagnosis one. He set it up by saying that if the "
           "patient has <b>not</b> tried anything yet, starting with benzoyl peroxide is perfectly "
           "reasonable &mdash; so the stem turns on <b>what they already failed and why</b>.",
      verify=["if i say on a test question", "presenting for treatment for acne",
              "they say they use benzoyl peroxide", "what do you go to next"]),
]

# ----------------------------------------------------- how he writes the test
STRATEGY = [
 dict(title="Time spent is the signal",
      quote="If I spend a lot of time talking about something, I&rsquo;m probably thinking about "
            "that when writing test questions. So you can use that sometimes to get clues on what "
            "maybe I&rsquo;m thinking about for specific questions.",
      lec=L3, at="2:16:29",
      verify=["if I spend a lot of time talking about something",
              "when writing test questions", "get clues on what maybe"]),
 dict(title="Learn the band, not the member",
      quote="Focus on categorizing these meds into as big of a band as you can for each group. "
            "Don&rsquo;t memorize each individual side effect for every individual penicillin. Just "
            "know that all penicillins have the same side effects, they all have the same mechanism. "
            "The differences between them would be things like, which one has anti-pseudomonal "
            "coverage? Which ones are specifically for MSSA?",
      lec=L3, at="2:16:38",
      verify=["categorizing these meds", "as big of a band as you can",
              "don't memorize each individual side effect", "anti-pseudomonal coverage"]),
 dict(title="The beta blocker letter rule",
      quote="For the beta blockers, generally speaking, if the beta blocker starts with the letter N "
            "through Z, it is considered a non-selective beta blocker&hellip; A through M as in Mary "
            "are generally going to be considered the cardioselective beta blockers.",
      lec=L3, at="2:17:38",
      verify=["if the beta", "blocker starts with the letter N through Z",
              "considered a non-selective beta blocker", "are generally going to be considered the cardio-selective"]),
 dict(title="What he said he will NOT do",
      quote="Am I going to be so mean on the test that I would have you differentiate nebivolol? No, "
            "that&rsquo;s kind of an exception to the rule. I&rsquo;d rather you get the rule down "
            "first and then we can focus on the exceptions&hellip; I&rsquo;m not going to try to be "
            "sneaky with you.",
      lec=L3, at="2:17:54",
      body="But he did name the two exceptions he <em>would</em> focus on: <b>labetalol and "
           "carvedilol</b>, because they carry additional alpha-1 blockade and are also "
           "non-selective.",
      verify=["am I going to be so mean on the test", "differentiate into bivolol",
              "I'd rather you get the rule down first", "not going to like try to be sneaky",
              "labetalol and carvetolol"]),
]

# --------------------------------------------------------- everything starred
# (drug or topic, what he flagged, timestamp, lecture, verify)
STARRED = [
 ("<i>Staphylococcus aureus</i>", "&ldquo;A very notable bug&hellip; especially when we talk about the dreaded MRSA.&rdquo;",
  "28:40", L1, ["a very notable bug", "the dreaded MRSA"]),
 ("<i>Pseudomonas</i>", "&ldquo;A really important bug from the gram-negative category&rdquo; &mdash; watch for which agents carry anti-pseudomonal cover.",
  "42:41", L1, ["another notable bacteria", "pseudomonas is a really important bug"]),
 ("Aztreonam", "Notable because there is <b>no documented cross-sensitivity with beta-lactams</b> &mdash; usable in a true penicillin allergy.",
  "57:45", L1, ["no documented cross sensitivity with beta lactams"]),
 ("Imipenem", "&ldquo;A very notable unique side effect just for imipenem&rdquo; &mdash; <b>seizures</b>, and the first time seizures appear in the lecture.",
  "1:00:16", L1, ["very notable unique side effect just for imipenem",
                  "first time we've seen seizures pop up"]),
 ("Vancomycin, route", "&ldquo;So note that, star that&rdquo; &mdash; <b>oral vancomycin for <i>C. difficile</i></b>; IV only treats systemic infection and will not touch gut C. diff.",
  "1:02:25", L1, ["oral vancomycin for C. Diff", "note that star that",
                  "IV only treats systemic infections"]),
 ("Macrolides", "First appearance of <b>QT prolongation</b> &mdash; &ldquo;this is notable, this is the first time we&rsquo;re seeing this too.&rdquo;",
  "1:13:38", L1, ["this is notable", "first time we're seeing this too", "QT prolongation"]),
 ("Macrolides", "They <b>inhibit CYP3A4</b> &mdash; he calls 3A4 the one that matters for this exam.",
  "1:16:30", L1, ["inhibit CYP3A4"]),
 ("Tetracyclines", "&ldquo;Good gram positive coverage that actually does cover MRSA, so that&rsquo;s notable.&rdquo;",
  "1:19:18", L1, ["that actually does cover MRSA, so that's notable"]),
 ("Tetracyclines", "They <b>chelate cations</b> &mdash; iron and calcium. Separate the doses.",
  "1:20:07", L1, ["couple notable things", "chelate with certain types of cat ions"]),
 ("Tetracyclines", "<b>Photosensitivity</b> &mdash; &ldquo;particularly notable for Florida.&rdquo;",
  "1:20:56", L1, ["photosensitivity", "particularly notable for Florida"]),
 ("Tetracyclines", "<b>Teeth discoloration and skeletal effects</b>, because it binds calcium in developing bone &mdash; avoid under 8 and in later pregnancy.",
  "1:21:19", L1, ["discoloration of the teeth", "This is notable because again, it binds to calcium"]),
 ("Tigecycline", "Adjust for <b>hepatic</b> dysfunction &mdash; the opposite of most drugs in this lecture.",
  "1:23:07", L1, ["watch out if they have hepatic dysfunction"]),
 ("Aminoglycosides", "&ldquo;A very good example of a <b>concentration dependent killer</b>&rdquo; &mdash; which is why dosing moved from every 8 hours to every 24.",
  "1:24:37", L1, ["these are notable because", "concentration dependent killer"]),
 ("Aminoglycosides", "&ldquo;The first example we&rsquo;re seeing of a <b>bactericidal protein synthesis inhibitor</b>&rdquo; &mdash; the exception to the rule that protein synthesis inhibitors are static.",
  "1:24:59", L1, ["also notable because these are a protein synthesis inhibitors",
                  "first example we're seeing of a bactericidal"]),
 ("Drug levels", "Give <b>three or four doses before checking a level</b>, so you are at steady state.",
  "1:27:33", L1, ["give three or four doses before you check it", "steady state"]),
 ("Linezolid", "&ldquo;Notable toxicity&hellip; <b>thrombocytopenia</b>&rdquo;, plus interactions with antidepressants.",
  "1:28:31", L1, ["Notable toxicity", "thrombocytopenias"]),
 ("Daptomycin", "&ldquo;Notable toxicity&hellip; <b>myalgias, muscle pain</b>.&rdquo;",
  "1:30:21", L1, ["Notable toxicity", "myalgia's muscle pain"]),
 ("Daptomycin", "&ldquo;Notable toxicity there, we haven&rsquo;t really seen anywhere else yet&rdquo; &mdash; and <b>it cannot be used in pneumonia</b>.",
  "1:31:08", L1, ["notable toxicity there", "cannot be used with patients with pneumonia"]),
 ("Fluoroquinolones", "They <b>worsen cognition in elderly patients</b> &mdash; &ldquo;one notable set of antibiotics which can worsen that cognition.&rdquo;",
  "1:35:42", L1, ["one notable set of antibiotics", "worsen that cognition"]),
 ("Fluoroquinolones", "Tendon injury is &ldquo;more notable <b>in children</b>, so like less than 16.&rdquo;",
  "1:36:42", L1, ["more notable", "in children, so like less than like 16"]),
 ("Moxifloxacin", "&ldquo;The notable unique thing about moxifloxacin compared to the others&rdquo; &mdash; no pseudomonal cover, and not for urinary tract infection.",
  "1:39:19", L1, ["notable kind of unique thing", "about moxifloxacin compared to the others"]),
 ("Clindamycin", "&ldquo;This one in particular is notable for being the <b>most likely to cause</b>&rdquo; <i>C. difficile</i>.",
  "1:41:58", L1, ["this one in particular is notable", "for being the most likely to cause this"]),
 ("Trimethoprim/sulfamethoxazole", "&ldquo;This is notable&rdquo; &mdash; <b>PJP pneumonia</b>, the <i>Pneumocystis</i> indication.",
  "1:44:47", L1, ["This is notable", "PJP pneumonia"]),
 ("Trimethoprim/sulfamethoxazole", "<b>Rash</b> &mdash; &ldquo;this one is much more likely to cause rash&hellip; very notable from that standpoint.&rdquo;",
  "1:45:17", L1, ["much more likely to cause rash", "very notable from that standpoint"]),
 ("Trimethoprim/sulfamethoxazole", "The notable interactions run through <b>CYP2C9 inhibition</b> &mdash; above all warfarin.",
  "1:46:26", L1, ["Some of the notable ones", "CYP2C9 inhibition"]),
 ("Metronidazole", "&ldquo;Really notable for having <b>mostly just anaerobic coverage</b>.&rdquo;",
  "1:47:49", L1, ["This is really notable", "mostly just anaerobic coverage"]),
 ("Metronidazole", "&ldquo;The other really notable thing&hellip; is there&rsquo;s an interaction here with <b>alcohol or ethanol</b>.&rdquo;",
  "1:48:34", L1, ["The other really notable thing with metronidazole",
                  "there's an interaction here with alcohol"]),
 ("Amphotericin B", "&ldquo;A pretty notable one&rdquo; &mdash; it forms a <b>pore</b> in the ergosterol membrane.",
  "1:58:30", L1, ["amphotericin B as a pretty notable one"]),
 ("Azoles", "&ldquo;Anytime you see the azole&hellip; you kind of know it fits in&rdquo; &mdash; the naming tells you the class.",
  "2:08:46", L1, ["anytime you see the azole"]),
 ("Ceftaroline", "&ldquo;Just notable about it&rdquo; &mdash; it <b>does</b> carry MRSA coverage, but he would <b>not start with it</b> for known MRSA when tried-and-true options exist.",
  "56:29", L1, ["actually does have MRSA coverage", "just notable about it there"]),
 ("Polymyxins", "&ldquo;It&rsquo;s just a <b>nasty set of drugs</b>. Really rough on the kidneys too&rdquo; &mdash; nephrotoxicity, neurotoxicity, and neuromuscular blockade interacting with paralytics. &ldquo;Don&rsquo;t use it too often.&rdquo;",
  "1:52:42", L1, ["nephrotoxicity, neurotoxicity issues with neuromuscular",
                  "It's just a nasty set of drugs", "don't use it too often"]),
 ("Fluconazole", "&ldquo;Watch out for <b>CYP3A4</b> interactions for sure&rdquo; &mdash; 3A4 being the interaction he says matters for this exam.",
  "2:07:24", L1, ["watch out for CYP3-4 interactions for sure"]),
 ("Acyclovir", "The crystals <b>pierce the renal tubules</b> &mdash; &ldquo;good hydration, really critical there.&rdquo; Then <b>CNS seizures and delirium</b>, and <b>bone marrow suppression</b> because it hits rapidly dividing cells.",
  "2:18:28", L1, ["those little crystals can start to pierce through the renal tubules",
                  "good hydration, really critical there", "seizures, delirium"]),
 ("Isotretinoin", "&ldquo;One of the <b>most notable examples of a REMS program</b>&rdquo; &mdash; this is iPledge, and he ties it straight to the pregnancy contraindication.",
  "39:36", L2, ["most notable examples of a rems program", "eye pledged"]),
 ("Topical corticosteroids", "The <b>gold standard</b> for atopic dermatitis &mdash; selection then turns on the product, and the <b>severity and site</b> of disease.",
  "54:20", L2, ["topical corticosteroids are gonna be kind of the gold standard",
                "severity and site of the disease"]),
]
