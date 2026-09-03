# -*- coding: utf-8 -*-
"""Content for the Dr. Wood exam review page -- Pharmacology I Exam 1.

Source: the 3 September 2026 review session, the evening before the paper.
Nothing here comes from the slides; the slides do not say what is examinable
and this recording does, repeatedly.

Every entry carries `verify` substrings that check_pharm_review.py must find in
the transcript before the page will build. `quote` is displayed in quotation
marks and is therefore verbatim, with only documented mis-hearings of drug
names repaired (see ASR_FIXES in the checker).

RULES  = the standing scope statements -- what he wants known, and what he says
         he is NOT asking.
ANSWERS = the individual questions the class put to him, with his answer.
"""

RULES = [
 dict(id="indications", at="0:53",
  title="Do not get hung up on indications &mdash; know the bugs instead",
  quote="I would not get so hung up on indications other than generally like what kind of "
        "bugs is it treating or if there's notable bugs that it treats",
  verify=["i would not get so hung up on indications",
          "what kind of bugs is it treating",
          "that's not really quite where we're at yet"],
  body="<p>Asked to go over the treatment of the conditions named under each antibiotic, he "
       "said that is <b>not where the course is yet</b>. The pneumonia and syphilis examples "
       "in the lectures were <b>context</b>, not content &mdash; he is not asking for the "
       "treatment of choice for syphilis, and he is not expecting aminoglycosides for "
       "pneumonia until the pulmonology block later in the year.</p>"
       "<p>What he does want off that axis: <b>the notable organisms</b> &mdash; he named "
       "<b>MRSA, Pseudomonas and Clostridioides difficile</b> &mdash; and the <b>broad "
       "strokes</b>, meaning does the agent cover anaerobes, does it cover atypicals.</p>"),

 dict(id="derm-exception", at="1:20",
  title="Dermatology is the exception: there, indications ARE fair game",
  quote="if we were doing a derm question about acne, for example, there you would want to "
        "know what kind of antibiotics you'd want to use and when",
  verify=["if we were doing a derm question about acne",
          "what kind of antibiotics you'd want to use and when",
          "topical versus like an oral antibiotic"],
  body="<p>He drew the line himself. The general antibiotic indications are out; the "
       "<b>dermatology ones are in</b>, because that material has been taught. The specific "
       "distinction he named is <b>topical against oral</b> &mdash; knowing which you reach "
       "for, and when.</p>"),

 dict(id="gram-coverage", at="3:40",
  title="Group gram-positive and gram-negative coverage BY CLASS, not by drug",
  quote="No, it'll be more, again, the broad strokes here",
  verify=["how much of gram-positive and gram-negative activity",
          "i would group those by classes where you can",
          "no, it'll be more, again, the broad strokes here"],
  body="<p>Asked how much gram-positive and gram-negative detail is needed, he said to "
       "<b>group by class</b>. The two comparisons he gave as the right level:</p>"
       "<ul><li><b>Cephalosporin generations.</b> Gram-positive coverage <b>diminishes</b> "
       "as you go up the generations; gram-negative coverage <b>improves</b>.</li>"
       "<li><b>Beta-lactamase inhibitors.</b> Adding one <b>opens up anaerobic coverage</b> "
       "for the aminopenicillins, which they do not have alone.</li></ul>"),

 dict(id="question-shape", at="4:20",
  title="The shape of the coverage question he WILL ask",
  quote="a patient has an infection, a skin infection. Do you think it's a gram-positive "
        "bacteria? Which one of these would be most likely to treat it?",
  verify=["a patient has an infection, a skin infection",
          "which one of these would be most likely to treat it",
          "my goal is not to be splitting hairs"],
  body="<p>He described the item outright, including how the distractors are built: "
       "<b>three agents with strictly gram-negative coverage and one good gram-positive "
       "agent</b>, and you identify it. That is the level of discrimination being asked "
       "for &mdash; not which single drug treats one named organism.</p>"),

 dict(id="no-tricks", at="5:35",
  title="He does not write trick questions, and he explained how he knows",
  quote="I'm never trying to trick you. It's just read the questions, see what I'm looking "
        "for and either know it or you don't",
  verify=["i'm never trying to trick you",
          "read the questions, see what i'm looking for"],
  body="<p>He explained the statistic he checks after a paper &mdash; the "
       "<b>point-biserial</b>, which asks whether the people who did well overall got a "
       "given question right and the people who did poorly got it wrong. A high value means "
       "the item is measuring knowledge rather than puzzle-solving, and he said his run "
       "well. <b>Read the stem for what it is asking; there is no second layer.</b></p>"),

 dict(id="mechanism-depth", at="9:42",
  title="General mechanism is enough &mdash; except where you need synergy",
  quote="As long as you know that it inhibits ergosterol synthesis and inhibits the ability "
        "for that cell wall or cell membrane to function and causes the cell to die, then "
        "that's good enough for my purposes",
  verify=["then that's good enough for my purposes",
          "i'm not one to split hairs",
          "is this an anti-fungal, anti-viral, or antibiotic"],
  body="<p>He does <b>not</b> want the exact binding target of each antifungal class. What he "
       "would rather you could do is <b>tell an antifungal from an antiviral from an "
       "antibiotic</b>, so you know what you are treating.</p>"
       "<p><b>The one place mechanism detail does matter is synergy.</b> When two drugs are "
       "used for the same problem you need to know their mechanisms differ, because "
       "<b>complementary mechanisms</b> are the point of combining them.</p>"),

 dict(id="brand-generic", at="10:57",
  title="Learn the generics &mdash; the board exam gives you nothing else",
  quote="on the PANCE, you will only get the generic",
  verify=["on the pance, you will only get the generic",
          "wherever possible, i will try to provide brand and generic"],
  body="<p>He gives both names wherever he can, deliberately, because in practice people say "
       "<i>Lasix</i> rather than furosemide and <i>Rocephin</i> rather than ceftriaxone, and "
       "he wants the association built early. But the board exam is generic-only, "
       "<b>so the generic is the one you must have</b>.</p>"),
 dict(id="by-class-then-back", at="31:30",
  title="Learn by class &mdash; but the paper asks you individual drug NAMES",
  quote="most my questions will ultimately come down to four individual drugs",
  verify=["please do as much as you can by classes",
          "most my questions will ultimately come down to four individual drugs",
          "you'll drive yourself crazy"],
  body="<p><b>Both halves of this matter, and they pull in opposite directions.</b></p>"
       "<p>Learn the material <b>by category</b>. His example: every cell-wall-active drug is "
       "bactericidal &mdash; penicillins, cephalosporins, carbapenems, vancomycin, the "
       "polymyxins &mdash; so there is no point memorising that fact drug by drug. Do the same "
       "for mechanism of action and the common contraindications. <i>&ldquo;Do big bins instead "
       "of individual agents.&rdquo;</i></p>"
       "<p><b>But the answer choices are individual drug names.</b> He said most of his "
       "questions come down to four named drugs. So the skill being tested is "
       "<b>seeing a drug name and placing it back in its bin</b> &mdash; you read "
       "<i>ceftriaxone</i>, you think <i>third-generation cephalosporin</i>, and everything you "
       "know about that class becomes available.</p>"
       "<p>That is exactly the drill the <a href=\"pharm-drill-classes.html\">Drug Classes "
       "Drill</a> and the other drills on this site are built to rehearse.</p>"),
 dict(id="no-numbers", at="29:40",
  title="Do not memorise numerical values &mdash; he gives them to you",
  quote="don't know specific values. If I'm using any values, I will tell you what those are "
        "in the question itself",
  verify=["if i'm using any values, i will tell you what those are in the question itself",
          "why would we look at a trough value"],
  body="<p>He is asking <b>why you look at a value</b>, never what the number is. His worked "
       "contrast, which is worth knowing in full:</p>"
       "<ul><li><b>Vancomycin</b> is a <b>time-dependent</b> killer. You want the trough "
       "<b>above the minimum inhibitory concentration for as long as possible</b>, so the "
       "trough is checked to confirm it is high enough &mdash; a level coming back at zero is "
       "cause for concern, because the infection is not being treated.</li>"
       "<li><b>Gentamicin</b> is a <b>concentration-dependent</b> killer with a "
       "<b>post-antibiotic effect</b>, so the level does <i>not</i> need to stay above that "
       "concentration. The trough is checked to confirm it is <b>undetectable</b> &mdash; "
       "because what accumulates causes <b>ototoxicity and nephrotoxicity</b>, and once the "
       "kidneys are harmed you accumulate still more.</li></ul>"
       "<p><b>Same test, opposite target, for opposite reasons.</b> That is the kind of "
       "question he is describing.</p>"),
 dict(id="why-not-what", at="28:20",
  title="&ldquo;Pharmacology is not a what class, it&rsquo;s a why class&rdquo;",
  quote="pharmacology is not a what class, it's a why class",
  verify=["pharmacology is not a what class, it's a why class",
          "i can read a drug reference if i wanted to know all the facts"],
  body="<p>He drew the contrast with anatomy, which he called closer to brute-force "
       "memorisation, and with physiology, which is a why class &mdash; how the body normally "
       "works, how it goes wrong, how you then treat it. Pharmacology sits with physiology.</p>"
       "<p><i>&ldquo;I can read a drug reference if I wanted to know all the facts. I want you "
       "to know: why am I selecting this drug? What are the things I need to look for? How do I "
       "communicate this to my patient?&rdquo;</i></p>"),
 dict(id="how-to-read", at="32:40",
  title="How to read his questions &mdash; and the habit he says wrecks scores",
  quote="if you ever find yourself asking did he mean this or this you're already in the weeds",
  verify=["keep it simple students",
          "sometimes it can be useful just to read the last sentence of the question",
          "i do not include a lot of superfluous information",
          "do not change your answers"],
  body="<p><b>Reading the stem.</b> His shortcut is to <b>read the last sentence first</b> to "
       "see what is being asked, then go back through the stem for the context you need. He "
       "does <b>not</b> pad questions &mdash; there is no patient's favourite colour in there, "
       "so every detail present is there for a reason. <i>&ldquo;Keep it simple, "
       "students.&rdquo;</i></p>"
       "<p><b>And the one he repeated hardest, twice, including as his closing line: do not "
       "change your answers.</b> He called it one of the worst habits, the one he hears "
       "constantly from students who struggle. Trust the gut instinct <b>unless you have a very "
       "obvious reason</b> to change it &mdash; you have had a week with this material and it "
       "is already in there.</p>"),
]

ANSWERS = [
 dict(id="zebras", at="19:40",
  title="Zebras &mdash; and the shortcut that saves you most of the work",
  q="Are there any adverse effects we should focus on specifically?",
  quote="whenever you hear hoofs beating, normally you should be thinking horses. Sometimes "
        "it's a zebra",
  verify=["sometimes it's a zebra",
          "the alcohol interaction with metronidazole",
          "no, they're all the same"],
  body="<p><b>Zebras</b> are the uncommon effects that are <b>unique to one particular "
       "drug</b>. His example is the <b>alcohol interaction with metronidazole</b> &mdash; most "
       "patients on it for an infection will not be drinking, but it costs nothing to warn "
       "them.</p>"
       "<p><b>The shortcut:</b> commons belong to the <b>group</b>, not the drug. Asked whether "
       "the common side effects of penicillins, cephalosporins and carbapenems need learning "
       "separately, he said <i>&ldquo;no, they're all the same&rdquo;</i> &mdash; do not spend "
       "the headspace. <b>Spend it where a class breaks the pattern instead</b>, and his "
       "example there is the <b>tetracyclines</b>: calcium binding, the bone effects, and "
       "photosensitivity that the patient genuinely needs advice about.</p>"
       "<p><b>Where to aim:</b> <i>&ldquo;Any time you see those killers or the zebras, those "
       "are always things you should look at.&rdquo;</i> The commons cover a good share of what "
       "he asks; the idiosyncratic ones are each worth about one question &mdash; he named "
       "<b>vancomycin infusion syndrome</b>, and slowing the infusion to two hours, as exactly "
       "that kind of one-off.</p>"),

 dict(id="ans-depth", at="24:10",
  title="Autonomic drugs: the mechanism tells you the indication",
  q="Should we focus on the categories, mechanism and adverse effects of the autonomic drugs, or what they are used for?",
  quote="what their mechanisms are will inform you on what they are used for in a lot of cases",
  verify=["will inform you on what they are used for",
          "which one of these would be most likely to slow down a rapid heart rate"],
  body="<p>He said you do not learn the indications separately &mdash; you <b>derive</b> them. "
       "The same antimuscarinic mechanism treats <b>chronic drooling</b> and <b>urinary "
       "incontinence</b>; it is one action in two organs. Glycopyrrolate tends to be used for "
       "the first and oxybutynin for the second, but that is marketing and licensing rather "
       "than a real pharmacological divide, and <i>either would work</i>.</p>"
       "<p><b>His example question:</b> <i>which of these would be most likely to slow a rapid "
       "heart rate?</i> There is more than one right road &mdash; a <b>beta blocker</b>, or a "
       "<b>muscarinic agonist</b>, or an <b>acetylcholinesterase inhibitor</b> raising "
       "acetylcholine. Recognise the category and what it does, and the answer follows.</p>"
       "<p><b>The reasoning chain he wants you running:</b> this drug is an antimuscarinic "
       "&rarr; what do muscarinic effects look like &rarr; I am blocking those &rarr; so what "
       "should I see? That is where the <i>mad as a hatter, dry as a bone</i> picture comes "
       "from, rather than being memorised as a list.</p>"),

 dict(id="bradycardia", at="34:40",
  title="The bradycardia question, and how he builds the wrong answers",
  q="For conditions treatable with multiple drugs, like bradycardia, will the answer be clear?",
  quote="I would not include both atropine and epinephrine. I would have like three drugs that "
        "lower the heart rate further and then like one that didn't",
  verify=["i would not include both atropine and epinephrine",
          "three drugs that lower the heart rate further",
          "i hate it when students challenge my question"],
  body="<p><b>He will not make you choose between two right answers.</b> Asked whether a "
       "condition with several valid treatments would be ambiguous, he described how he builds "
       "the item instead: <b>three drugs that would make the problem worse, and one that "
       "would not</b>. He said he writes them that clearly on purpose &mdash; "
       "<i>&ldquo;I hate it when students challenge my question&rdquo;</i> &mdash; so most "
       "distractors are <b>not even theoretically reasonable</b>.</p>"
       "<p><b>The clinical content he gave with it:</b> for symptomatic bradycardia he follows "
       "the advanced cardiac life support guidelines. <b>Atropine</b> first &mdash; an "
       "antimuscarinic, so blocking the muscarinic receptors on the heart raises the rate. If "
       "that is not enough, move to <b>beta-1 activation</b>: dobutamine, epinephrine, "
       "norepinephrine or isoproterenol, all sharing that one action. In the guidelines "
       "<b>epinephrine</b> is the usual next step after atropine.</p>"),

 dict(id="antifungal-organisms", at="39:10",
  title="Antifungals: you do NOT need which fungus each one covers",
  q="For the antifungals, do we need to know the exact organism &mdash; for example that posaconazole treats Aspergillus?",
  quote="I would not get hung up on memorizing each individual type of fungus that the drugs treat",
  verify=["i would not get hung up on memorizing each individual type of fungus",
          "they don't have nice broad"],
  body="<p><b>No.</b> He said the fungi do not sort into clean categories the way bacteria do "
       "with gram-positive and gram-negative, and that the organism lists were there to give a "
       "sense of what is being treated, not to be memorised.</p>"
       "<p><b>What he wants instead</b> is that you can identify the <b>type</b> of antifungal, "
       "and above all <b>tell an antifungal from an antiviral</b>. His example item: a patient "
       "is <b>influenza A positive</b>, which of these is the best treatment &mdash; with an "
       "antifungal sitting among the options for you to reject.</p>"),

 dict(id="exam-structure", at="41:00",
  title="How many questions, and where they come from",
  q="How many questions are there per lecture?",
  quote="There are five questions per technical hour of lecture",
  verify=["there are five questions per technical hour of lecture",
          "15 from the first powerpoint"],
  body="<p><b>Five questions per scheduled hour of lecture.</b> He does not set the hours "
       "&mdash; the course director does &mdash; but the ratio is fixed. Dermatology was "
       "scheduled three hours, which is more than he thinks it needs, and it still earns "
       "fifteen questions.</p>"
       "<p>His split: <b>15 from the first deck, 15 from the second</b>, and the remainder from "
       "the third. <b>He was not certain of the total</b>, talking himself between 40 and 45 "
       "and settling on <i>&ldquo;I think it's 45 &hellip; I need to double check&rdquo;</i>. "
       "It is written here as he said it rather than tidied into a figure he did not "
       "commit to.</p>"
       "<p>He also mentioned, unprompted, that his class averages usually land in the "
       "<b>upper eighties</b>.</p>"),

 dict(id="study-advice", at="26:00",
  title="What he told the student who said their brain was scrambled",
  q="Any tips on last-minute studying, or things we really should focus on?",
  quote="if you hear me spending like five minutes talking about something, chances are I "
        "think that's really important",
  verify=["if you hear me spending like five minutes talking about something",
          "don't just go off of what's on the slides",
          "being comfortable with being uncomfortable"],
  body="<p><b>Re-listen rather than re-read.</b> It is only three lectures. He said outright "
       "that <b>time spent is his own signal</b> &mdash; five minutes on something means he "
       "thinks it matters and probably wrote a question on it &mdash; and that the slides are "
       "not the whole picture, because the context, illustrations and stories are where the "
       "concepts lock in.</p>"
       "<p><b>Group study</b>, which he made the strongest case for: you cannot become fluent "
       "in a language through an app, you become fluent by talking to people who will catch "
       "what you have wrong. There is what you know, what you know you do not know, and "
       "<b>what you do not know you do not know</b> &mdash; and working alone is how that third "
       "category survives until the exam finds it.</p>"
       "<p><i>&ldquo;The first rule of PA school is being comfortable with being "
       "uncomfortable.&rdquo;</i></p>"),

 dict(id="acne-ladder", at="11:55",
  title="The acne ladder, in his own order",
  q="Can we go over the acne treatments in order for the different levels of acne?",
  quote="start easy, start simple stuff first and then kind of work your way up to the big guns",
  verify=["benzoyl peroxide is a great thing to try first",
          "topical minocycline or clindamycin or erythromycin",
          "the kind of end all therapy is going to be isotretinoin",
          "it's a marathon, it's not a race"],
  body="<p><b>Before anything: ask what the patient has already tried</b>, and what did and "
       "did not work. He was blunt about why &mdash; prescribe something they have already "
       "failed and they will conclude you were not listening.</p>"
       "<ol><li><b>Benzoyl peroxide.</b> The right first move, though most patients have "
       "tried it already.</li>"
       "<li><b>Topical retinoids</b> &mdash; tretinoin &mdash; and <b>azelaic acid</b>.</li>"
       "<li><b>Topical antibiotics</b> &mdash; minocycline, clindamycin or erythromycin.</li>"
       "<li><b>Systemic antibiotics</b> &mdash; doxycycline or minocycline. The trigger is "
       "the disease outgrowing topical therapy: a <b>larger area</b> where applying a topical "
       "is no longer practical, or disease that is more <b>severe or inflammatory</b>.</li>"
       "<li><b>Isotretinoin</b> &mdash; the most effective and the <b>last line</b>. He called "
       "it the nuclear option.</li></ol>"
       "<p><b>Maximise the dose before you add or switch.</b> If a product is partly working, "
       "go up in strength first.</p>"
       "<p><b>Why going systemic costs you something.</b> A topical works only where you put "
       "it, so the side effects stay local. Systemic antibiotics bring "
       "<b>gastrointestinal upset</b>, <b>photosensitivity</b> with the tetracyclines, and "
       "<b>food and drug interactions</b> &mdash; his example is a patient on a "
       "<b>prenatal vitamin</b> whose <b>calcium and iron bind up the doxycycline</b>.</p>"
       "<p><b>Isotretinoin's price:</b> heavy drying and <b>desquamation</b>, "
       "<b>photosensitivity</b>, light toxicity in the <b>eyes</b>, and <b>worsening "
       "depression with possible suicidal ideation</b>.</p>"
       "<p><b>Also available:</b> <b>intralesional steroids</b> for large inflammatory "
       "pustules, though he called that a specialty use.</p>"
       "<p><b>And the contrast worth remembering:</b> with an acute infection you do not "
       "hesitate &mdash; you go straight to what treats it. With a chronic condition like "
       "acne, <i>&ldquo;it's a marathon, it's not a race&rdquo;</i>, and you can work up the "
       "ladder finding what suits the patient.</p>"),

 dict(id="glaucoma-cholinergics", at="15:30",
  title="Why the cholinergic agents are not first choice in glaucoma",
  q="Would pilocarpine be preferable to carbachol because carbachol has more adverse effects?",
  quote="the cholinergic agents are not really preferred for management of glaucoma",
  verify=["the cholinergic agents are not really preferred for management of glaucoma",
          "it will cause that meiosis"],
  body="<p>He said he does not think either is clinically worse than the other, whatever the "
       "slide lists. <b>The real answer is that the whole class is not preferred</b> in "
       "glaucoma until you reach a third or fourth line agent.</p>"
       "<p><b>Why:</b> they cause <b>miosis</b> and impair the ability to re-accommodate the "
       "lens, so the patient gets poor vision and an induced short-sightedness, plus headaches "
       "from straining to see. He singled out <b>younger patients with full vision</b> as the "
       "worst fit. First-line is a <b>prostaglandin or a beta blocker</b> instead.</p>"),

 dict(id="adverse-framework", at="17:20",
  title="The three buckets he sorts every adverse effect into",
  quote="I typically break them up into three categories. There's the killers, the commons "
        "and the zebras",
  verify=["there's the killers, the commons and the zebras",
          "those are the things that require immediate discontinuation",
          "almost every antibiotic is going to cause nausea, vomiting, diarrhea"],
  body="<p>Asked which adverse effects to focus on, he gave a framework rather than a list. "
       "<b>Sort every side effect you have learned into one of these three, and you will know "
       "what he is asking for.</b></p>"
       "<ul><li><b>Killers</b> &mdash; dangerous, and they require <b>immediate "
       "discontinuation and evaluation</b>. His examples: <b>anaphylaxis</b>; "
       "<b>Stevens-Johnson syndrome</b> with agents such as "
       "<b>sulfamethoxazole and trimethoprim</b>; <b>suicidal ideation with isotretinoin</b>. "
       "These are not necessarily the commonest &mdash; they are the ones the patient must be "
       "<b>warned about in advance</b>, so that they do not assume skin sloughing off is a "
       "normal side effect.</li>"
       "<li><b>Commons</b> &mdash; what actually happens often. His example: <b>gastrointestinal "
       "upset with antibiotics</b>. Almost every antibiotic causes nausea, vomiting or "
       "diarrhoea in somebody. The patient is told these are expected; they may or may not "
       "warrant a change of therapy.</li>"
       "<li><b>Zebras</b> &mdash; the rare ones.</li></ul>"),

 dict(id="succinylcholine", at="2:34",
  title="Succinylcholine: flaccid paralysis is PHASE TWO",
  q="Does flaccid paralysis happen in phase one or phase two of the depolarizing agents?",
  quote="So that would be in phase two",
  verify=["so that would be in phase two",
          "succinylcholine is basically like two acetylcholines",
          "that's what causes the little fasciculations"],
  body="<p>Succinylcholine is <b>two acetylcholine molecules joined together</b>. In "
       "<b>phase one</b> it activates the nicotinic receptor at the neuromuscular end plate "
       "and depolarises it &mdash; which is what produces the <b>fasciculations</b>, and what "
       "makes it a <i>depolarizing</i> agent. It then keeps sitting on the receptor until the "
       "receptor <b>desensitises</b> from being over-activated, and that is <b>phase two</b>, "
       "when the <b>flaccid paralysis</b> appears.</p>"
       "<p><b>His mnemonic, back from the autonomic lecture:</b> the days of the week &mdash; "
       "<b>F</b>riday for <b>f</b>asciculations first, then <b>W</b>ednesday for "
       "<b>w</b>eakness. Fasciculations come first because they are phase one; the weakness, "
       "and then the paralysis, is phase two.</p>"),

 dict(id="anticholinesterases", at="6:10",
  title="Why physostigmine, neostigmine and pyridostigmine are not interchangeable",
  q="If they all inhibit acetylcholinesterase, why can't they be used interchangeably?",
  quote="I need something that's able to get across the blood brain barrier and actually be "
        "able to treat the CNS effects there",
  verify=["get across the blood brain barrier",
          "neostigmine we use a lot in surgery",
          "sometimes it's just clinical inertia"],
  body="<p><b>The real axis is whether the drug crosses into the brain.</b></p>"
       "<ul><li><b>Physostigmine</b> crosses the blood&ndash;brain barrier, so it is the one "
       "for <b>anticholinergic overdose</b> where the problem is central toxicity. He tied "
       "this to the anticholinergic toxidrome and the <b>Mad Hatter</b> mnemonic: mild "
       "sedation, then anxiety, hallucinations and agitation, with <b>seizures as the "
       "end point</b> of central toxicity.</li>"
       "<li><b>Neostigmine</b> and <b>pyridostigmine</b> cross less easily and act "
       "<b>peripherally</b>, on neuromuscular function.</li></ul>"
       "<p><b>Neostigmine in surgery</b> is his worked example. Rocuronium and vecuronium are "
       "<b>non-depolarizing</b> blockers &mdash; they sit on the nicotinic receptor and keep "
       "acetylcholine off it, which paralyses the patient. Neostigmine blocks "
       "acetylcholinesterase, acetylcholine builds up, <b>outcompetes</b> the blocker and "
       "knocks it off the receptor, and neuromuscular function returns so the patient "
       "breathes for themselves.</p>"
       "<p><b>And an honest caveat he added:</b> some of the choice is not pharmacology at "
       "all. A myasthenia clinic may simply prefer pyridostigmine. He called it "
       "<b>clinical inertia</b> &mdash; <i>&ldquo;this was how I was trained&rdquo;</i> "
       "&mdash; and said there is often no concrete reason.</p>"),

 dict(id="antifungal-mechanisms", at="8:40",
  title="Polyenes, azoles and allylamines: the difference in one line each",
  q="What is the difference in mechanism between the polyenes, azoles and allylamines?",
  quote="With the polyenes, for example, those are more so like kind of poking holes in the "
        "actual membrane itself to cause like leakage of contents",
  verify=["poking holes in the actual membrane",
          "azoles cause a lot of cyp3a4 interactions"],
  body="<ul><li><b>Polyenes</b> &mdash; punch holes in the membrane itself, so the cell's "
       "contents leak out.</li>"
       "<li><b>Azoles</b> &mdash; block the fungal enzyme that makes ergosterol. His own "
       "memory hook: <b>azoles cause a great many CYP3A4 interactions</b>, so remember that "
       "azoles block a CYP enzyme &mdash; in the fungus, that is the one making "
       "ergosterol.</li>"
       "<li><b>Allylamines</b> &mdash; also reduce ergosterol synthesis, at a different "
       "step.</li></ul>"
       "<p><b>He said the shared endpoint is enough:</b> ergosterol synthesis is inhibited, "
       "the membrane stops working, the cell dies.</p>"),
]
