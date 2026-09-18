# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- ENT, topic 1: anti-infectives and antifungals.

Scope, corrected by Jaxon 2026-09-18: INDICATIONS and the ADVERSE EFFECTS OF
SPECIFIC AGENTS are examinable and are asked here. That reverses what the
ophthalmology build recorded -- pharm_oph_partition.py has Dr. Wood ruling out
the indications table and which agent causes which adverse effect -- so the
ophthalmology pools were written without them and this one was too, until the
correction. Dosing and formulations remain out.

What survives is the part worth knowing anyway: why amoxicillin is given at a
high dose rather than a standard one, what moves a patient off it, which single
otic agent is unsafe through a perforation, and why the antifungal that treats
thrush is the one that is NOT absorbed.
"""

D = "ENT Jax Pharmacology.pptx"
IO_CLASS = "Identify ENT drug classes and commonly prescribed ENT drugs"
IO_MOA = "Describe the mechanism of action of ENT drugs"
IO_IND = "Identify indications for commonly used ENT drugs"
IO_CONTRA = "Identify contraindications for ENT drugs"
IO_EDU = "Outline appropriate patient education for ENT drugs"
IO_INTERACT = "Discuss potential drug-drug, drug-food, and drug-herb interactions with ENT drugs"
IO_SE = "Summarize side effects and toxic manifestations of ENT drugs"

QUESTIONS = [

{"topic": "Acute otitis media", "io": IO_IND, "slot": "drug choice",
 "q": "A child has acute otitis media and has had no antibiotics in the last month. What is the mainstay of therapy?",
 "opts": [
  ["Amoxicillin, at a high dose", "Correct. High-dose amoxicillin is first line, and the dose is high for a reason rather than by habit: it is what overcomes the resistant pneumococcus."],
  ["Amoxicillin-clavulanate", "That is held for severe or resistant disease, or a child who has had antibiotics in the past month."],
  ["Azithromycin", "A penicillin-allergy alternative, and a weak one here, since up to half of pneumococci are resistant to macrolides."],
  ["Ceftriaxone by injection", "Reserved for failed therapy or a child who cannot keep oral medication down."]],
 "c": 0, "cite": D + ", Slide 5"},

{"topic": "Acute otitis media", "io": IO_MOA, "slot": "mechanism",
 "q": "Why is amoxicillin given at a high dose rather than a standard one in acute otitis media?",
 "opts": [
  ["It overcomes Streptococcus pneumoniae resistance", "Correct. Pneumococcal resistance here is a matter of degree rather than all-or-nothing, so raising the concentration restores activity. That is the whole argument for the higher dose."],
  ["It shortens the course to a single day", "Duration is not shortened by the higher dose; the course still runs several days."],
  ["It penetrates the middle ear only at high concentrations", "Penetration is not the stated problem. The higher dose exists to overcome pneumococcal resistance, which is a matter of degree rather than absolute."],
  ["It covers Pseudomonas, which standard doses miss", "Pseudomonas is not among the organisms causing acute otitis media."]],
 "c": 0, "cite": D + ", Slide 5"},

{"topic": "Acute otitis media", "io": IO_IND, "slot": "drug choice",
 "q": "A child with acute otitis media finished a course of antibiotics three weeks ago. How does that change the choice?",
 "opts": [
  ["Amoxicillin-clavulanate is used instead", "Correct. Recent antibiotic exposure selects for beta-lactamase producers, and that is exactly what the clavulanate is there to cover."],
  ["The same high-dose amoxicillin is used", "Recent exposure is one of the stated reasons to move off plain amoxicillin."],
  ["A macrolide is substituted", "Macrolides are a penicillin-allergy option, and pneumococcal resistance to them is common."],
  ["Antibiotics are withheld for a further week", "Watchful waiting is not the response to recent antibiotic exposure."]],
 "c": 0, "cite": D + ", Slide 5"},

{"topic": "Acute otitis media", "io": IO_IND, "slot": "drug choice",
 "q": "A child with acute otitis media has a penicillin allergy. Which agents are offered?",
 "opts": [
  ["Cefdinir or azithromycin", "Correct. Both are listed, though the macrolide is the weaker of the two here because pneumococcal resistance to macrolides runs high."],
  ["Ciprofloxacin or levofloxacin", "Fluoroquinolones are not the listed oral option for this infection in children."],
  ["Clindamycin or cefixime", "That pairing belongs to bacterial rhinosinusitis in a penicillin-allergic patient."],
  ["Vancomycin or linezolid", "These are not among the agents used for uncomplicated acute otitis media."]],
 "c": 0, "cite": D + ", Slide 5"},

{"topic": "Acute otitis media", "io": IO_IND, "slot": "drug choice",
 "q": "Why is a macrolide a weak choice in acute otitis media even when it is permitted?",
 "opts": [
  ["Up to half of pneumococci are resistant to macrolides", "Correct. It remains an option for the penicillin-allergic patient, but the resistance rate is the reason it is not a comfortable one."],
  ["Macrolides do not reach the middle ear", "Penetration is not the stated limitation. The problem is that up to half of pneumococci are resistant to macrolides outright."],
  ["Macrolides are contraindicated in children", "They are used in children; the problem is resistance, not age."],
  ["Macrolides have no activity against Haemophilus influenzae", "The stated resistance problem concerns Streptococcus pneumoniae rather than Haemophilus influenzae, and it is resistance rather than absent activity."]],
 "c": 0, "cite": D + ", Slide 5"},

{"topic": "Acute otitis media", "io": IO_IND, "slot": "next step",
 "q": "A child treated for acute otitis media has not improved after three days, and has had no antibiotics in the past three months. What is the next step?",
 "opts": [
  ["Amoxicillin-clavulanate", "Correct. Failure at three days is the trigger to step up, and this is the step. Or a third generation cephalosporin."],
  ["Continue the same agent for a further three days", "Three days without improvement is the stated point at which therapy is considered to have failed."],
  ["Move straight to injected ceftriaxone", "Injection is for failed therapy after stepping up, or for a child who cannot tolerate oral medication."],
  ["Stop antibiotics and observe", "Observation is not the response to a treatment failure. Failure at three days is the point at which therapy is stepped up rather than withdrawn."]],
 "c": 0, "cite": D + ", Slide 6"},

{"topic": "Acute otitis media", "io": IO_IND, "slot": "next step",
 "q": "When is injected ceftriaxone used in acute otitis media?",
 "opts": [
  ["For failed therapy", "Correct. Both routes to it are practical rather than microbiological: the oral agents have not worked, or they cannot be kept down. Or when oral medication is not tolerated."],
  ["As first line in any child under two", "Age alone does not move a child to injection. The triggers are failed oral therapy, or an inability to keep oral medication down."],
  ["Whenever the tympanic membrane has perforated", "Perforation is not the stated trigger. Escalation to injection follows failed therapy, or intolerance of oral medication."],
  ["Only after culture confirms a resistant organism", "Middle ear fluid is not routinely cultured before escalating."]],
 "c": 0, "cite": D + ", Slide 6"},

{"topic": "Acute otitis media", "io": IO_CLASS, "slot": "drug choice",
 "q": "Which organisms are named as the bacterial causes of acute otitis media?",
 "opts": [
  ["Streptococcus pneumoniae", "Correct. The same three run through otitis media and bacterial sinusitis, which is why the antibiotic reasoning for the two is so similar. Haemophilus influenzae and Moraxella catarrhalis."],
  ["Staphylococcus aureus, Pseudomonas and Proteus", "These are canal and chronic-infection organisms rather than the middle ear trio."],
  ["Group A Streptococcus and Epstein-Barr virus", "That pairing belongs to pharyngitis. The middle ear organisms are Streptococcus pneumoniae, Haemophilus influenzae and Moraxella catarrhalis."],
  ["Candida and Aspergillus", "Fungi are not among the causes of acute otitis media given here."]],
 "c": 0, "cite": D + ", Slide 4"},

{"topic": "Acute otitis media", "io": IO_IND, "slot": "mechanism",
 "q": "Most acute otitis media involves a virus. What does that fact change?",
 "opts": [
  ["It is one reason antibiotics are not automatic in every case", "Correct. A majority of cases are viral, or viral with bacteria alongside, which is the argument against reaching for an antibiotic reflexively."],
  ["It means an antiviral should be given in place of an antibiotic",
   "No antiviral is offered for acute otitis media. The viral majority argues against reaching for an antibiotic, not for reaching for an antiviral."],
  ["It means the causative bacterial organisms remain unidentified",
   "The bacterial causes are well described; the point is that many cases are not bacterial at all."],
  ["It means the condition resolves without treatment in every case",
   "Antibiotics are clearly indicated in a defined group; the point is that the group is not everyone."]],
 "c": 0, "cite": D + ", Slide 4"},

{"topic": "Acute otitis media", "io": IO_CLASS, "slot": "mechanism",
 "q": "What is changing the organisms that cause acute otitis media?",
 "opts": [
  ["Vaccination", "Correct. The aetiology is shifting on the back of vaccination, which is why the proportions attached to each organism are not fixed and why they keep being revised."],
  ["Rising antibiotic resistance alone", "Resistance changes which drug works, not which organism turns up."],
  ["Increasing use of tympanostomy tubes", "Tubes change management rather than which organisms appear. Vaccination is what is shifting the aetiology."],
  ["Climate and seasonal variation", "Seasonality is not offered as the reason the aetiology is moving."]],
 "c": 0, "cite": D + ", Slide 4"},

{"topic": "Acute bacterial rhinosinusitis", "io": IO_IND, "slot": "drug choice",
 "q": "What is the standard of therapy for acute bacterial rhinosinusitis?",
 "opts": [
  ["Amoxicillin-clavulanate", "Correct. Unlike otitis media, this one starts with the clavulanate already on board, because beta-lactamase producing Haemophilus influenzae is common here."],
  ["High-dose amoxicillin alone", "That is the otitis media starting point; sinusitis begins a step further along."],
  ["Azithromycin", "Not the standard of therapy for this infection. Amoxicillin-clavulanate is, because beta-lactamase producing Haemophilus influenzae is common here."],
  ["Doxycycline", "Not among the agents offered here. The standard is amoxicillin-clavulanate, with clindamycin plus cefixime or levofloxacin for penicillin allergy."]],
 "c": 0, "cite": D + ", Slide 7"},

{"topic": "Acute bacterial rhinosinusitis", "io": IO_MOA, "slot": "mechanism",
 "q": "Why does bacterial rhinosinusitis start with amoxicillin-clavulanate when otitis media does not?",
 "opts": [
  ["Beta-lactamase producing Haemophilus influenzae is common in sinusitis", "Correct. The clavulanate exists to inhibit that enzyme, so the frequency of the enzyme is what decides whether it is needed from the outset."],
  ["The sinuses are harder for antibiotics to penetrate", "Penetration is not the reason given. Beta-lactamase producing Haemophilus influenzae is common in sinusitis, and the clavulanate exists to defeat that enzyme."],
  ["Sinusitis is caused by entirely different organisms", "The organisms largely overlap with otitis media; the resistance pattern is what differs."],
  ["Clavulanate has independent antibacterial activity against these organisms",
   "Clavulanate protects the amoxicillin rather than acting as an antibiotic itself."]],
 "c": 0, "cite": D + ", Slide 7"},

{"topic": "Acute bacterial rhinosinusitis", "io": IO_IND, "slot": "diagnosis",
 "q": "What separates viral from bacterial rhinosinusitis, and so decides whether an antibiotic is given?",
 "opts": [
  ["Symptoms beyond ten days", "Correct. The timeline does the work, because nothing on examination reliably separates the two. Or worsening after five to six days."],
  ["The colour of the nasal discharge", "Discharge colour does not distinguish viral from bacterial. The timeline does: ten days, or worsening after an initial improvement."],
  ["The presence of fever at any point", "Fever appears in both, so it cannot separate them. What separates them is the duration and the pattern of worsening."],
  ["Tenderness over the maxillary sinuses", "Tenderness is common to both. The distinguishing feature is the time course rather than anything found on examination."]],
 "c": 0, "cite": D + ", Slide 7"},

{"topic": "Acute bacterial rhinosinusitis", "io": IO_IND, "slot": "drug choice",
 "q": "A patient with bacterial rhinosinusitis has a penicillin allergy. Which regimens are offered?",
 "opts": [
  ["Clindamycin with cefixime", "Correct. The first is a pairing rather than a single agent, which is easy to remember wrongly as clindamycin alone. Or levofloxacin."],
  ["Cefdinir or azithromycin", "That pair belongs to penicillin allergy in acute otitis media."],
  ["Clindamycin alone", "Clindamycin is given together with cefixime here rather than by itself; the alternative single agent is levofloxacin."],
  ["Nitrofurantoin or trimethoprim", "Neither is used for sinus infection. The penicillin-allergy options are clindamycin with cefixime, or levofloxacin."]],
 "c": 0, "cite": D + ", Slide 7"},

{"topic": "Acute bacterial rhinosinusitis", "io": IO_IND, "slot": "next step",
 "q": "What non-antibiotic measure is described as useful in bacterial rhinosinusitis?",
 "opts": [
  ["Saline irrigation", "Correct. It is the one adjunct named, and it costs nothing in resistance."],
  ["Oral antihistamines", "Antihistamines are for allergic rhinitis rather than bacterial sinus infection."],
  ["Systemic corticosteroids", "Not offered as an adjunct here. Saline irrigation is the one non-antibiotic measure described as useful."],
  ["Topical decongestant for ten days", "Topical decongestants are limited to a few days, and are not the named adjunct."]],
 "c": 0, "cite": D + ", Slide 7"},

{"topic": "Acute bacterial rhinosinusitis", "io": IO_CLASS, "slot": "drug choice",
 "q": "Beyond the organisms it shares with otitis media, what else causes bacterial rhinosinusitis?",
 "opts": [
  ["Streptococcus pyogenes", "Correct. The extra names are part of why the starting antibiotic is broader than it is for the ear. Staphylococcus aureus and gram negative bacilli."],
  ["Pseudomonas aeruginosa and Candida", "Neither is listed among the causes. The additional organisms are Streptococcus pyogenes, Staphylococcus aureus and gram negative bacilli."],
  ["Mycoplasma and Chlamydophila", "Atypicals are not named here. The extra organisms beyond the middle ear trio are S. pyogenes, S. aureus and gram negative bacilli."],
  ["Anaerobes exclusively", "Anaerobes are not given as the additional organisms; Streptococcus pyogenes, Staphylococcus aureus and gram negative bacilli are."]],
 "c": 0, "cite": D + ", Slide 7"},

{"topic": "Acute pharyngitis", "io": IO_IND, "slot": "mechanism",
 "q": "What is the stated goal of treating streptococcal pharyngitis?",
 "opts": [
  ["To prevent acute rheumatic fever and suppurative complications", "Correct. Note what is absent: shortening the sore throat is not the reason the antibiotic is given."],
  ["To shorten the duration of the sore throat", "Symptom duration is not the stated goal. The antibiotic is given to prevent acute rheumatic fever and suppurative complications."],
  ["To prevent transmission within the household", "Transmission is not the reason given. The goal is preventing acute rheumatic fever and suppurative complications."],
  ["To prevent the infection spreading to the sinuses and middle ear",
   "That is not among the complications named. The antibiotic is given to prevent acute rheumatic fever and suppurative complications."]],
 "c": 0, "cite": D + ", Slide 8"},

{"topic": "Acute pharyngitis", "io": IO_IND, "slot": "diagnosis",
 "q": "Why is a rapid streptococcal test used before treating a sore throat?",
 "opts": [
  ["To prevent over-prescribing, since most pharyngitis is viral", "Correct. Only a minority of sore throats are streptococcal, so testing is what keeps the antibiotic away from the rest."],
  ["To identify which antibiotic the organism is sensitive to", "The rapid test does not provide sensitivities. It establishes whether the organism is there at all, since most sore throats are viral."],
  ["To exclude infectious mononucleosis", "It tests for streptococcus rather than ruling out mononucleosis."],
  ["To decide the length of the course", "Course length does not depend on the test result. The test decides whether to treat at all, because most pharyngitis is viral."]],
 "c": 0, "cite": D + ", Slide 8"},

{"topic": "Acute pharyngitis", "io": IO_IND, "slot": "drug choice",
 "q": "Which single-dose option is offered for streptococcal pharyngitis in a patient unlikely to finish a course?",
 "opts": [
  ["Benzathine penicillin G by intramuscular injection", "Correct. One injection replaces the whole oral course, which is precisely its point when adherence is in doubt."],
  ["A ten-day course of oral azithromycin",
   "Azithromycin is a penicillin-allergy alternative and is not a single dose here."],
  ["A ten-day course of oral amoxicillin",
   "Amoxicillin is given as a course over several days rather than as a single dose; the single-dose option is injected benzathine penicillin G."],
  ["Intramuscular ceftriaxone given over three days",
   "Ceftriaxone is used in otitis media that has failed therapy, not for pharyngitis."]],
 "c": 0, "cite": D + ", Slide 8"},

{"topic": "Acute pharyngitis", "io": IO_IND, "slot": "drug choice",
 "q": "A patient with streptococcal pharyngitis is penicillin-allergic. Which agents are offered?",
 "opts": [
  ["Cephalexin, clindamycin or azithromycin", "Correct. Three alternatives rather than one, which is worth holding onto because the allergy lists differ between the ear, the sinuses and the throat."],
  ["Cefdinir, cefixime or ceftriaxone",
   "These are the alternatives listed for the ear and the sinuses."],
  ["Levofloxacin or moxifloxacin",
   "A fluoroquinolone is offered for sinusitis, not for pharyngitis."],
  ["Doxycycline or trimethoprim", "Not among the alternatives for streptococcal pharyngitis, which are cephalexin, clindamycin and azithromycin."]],
 "c": 0, "cite": D + ", Slide 8"},

{"topic": "Acute pharyngitis", "io": IO_CLASS, "slot": "mechanism",
 "q": "What proportion of acute pharyngitis is due to group A streptococcus?",
 "opts": [
  ["A minority of cases, with most being viral", "Correct. That imbalance is the entire argument for testing before prescribing."],
  ["The clear majority of cases", "Most pharyngitis is viral; group A streptococcus accounts for a minority of cases, which is why testing precedes treating."],
  ["Almost all cases in adults", "Streptococcal pharyngitis is more a disease of children and teenagers, and is a minority of sore throats at any age."],
  ["It is too rare to be worth testing for", "It is common enough that missing it matters, which is why the rapid test exists."]],
 "c": 0, "cite": D + ", Slide 8"},

{"topic": "Otic antibiotics", "io": IO_MOA, "slot": "mechanism",
 "q": "Otic preparations usually combine an anti-infective with a glucocorticoid. What does each component do?",
 "opts": [
  ["The anti-infective inhibits bacterial growth and the steroid reduces inflammatory cytokines", "Correct. Two separate jobs in one bottle, which is also why the combinations cost more than a plain antibiotic drop."],
  ["The steroid kills the organism and the anti-infective reduces swelling", "The roles are the other way round: the anti-infective inhibits bacterial growth and the steroid reduces inflammatory cytokines."],
  ["Both components are antibacterial and act synergistically", "The steroid has no antibacterial action. It is there to reduce inflammatory cytokines while the anti-infective inhibits bacterial growth."],
  ["The steroid improves penetration of the anti-infective through the tympanic membrane",
   "Penetration is not the stated reason for combining them. Each component has its own job: killing organisms, and damping inflammation."]],
 "c": 0, "cite": D + ", Slide 9"},

{"topic": "Otic antibiotics", "io": IO_CONTRA, "slot": "contraindication",
 "q": "Which otic ingredient is specifically not recommended when the tympanic membrane is perforated or tubes are in place?",
 "opts": [
  ["Polymyxin B", "Correct. With a route to the middle ear it risks cochlear damage and hearing loss, which makes an intact drum the thing to establish before prescribing it."],
  ["Ciprofloxacin", "The fluoroquinolone drops are the ones considered safe in this situation."],
  ["Dexamethasone", "The steroid component is not the part that carries this warning."],
  ["Ofloxacin", "Ofloxacin is offered as an alternative rather than restricted."]],
 "c": 0, "cite": D + ", Slide 10"},

{"topic": "Otic antibiotics", "io": IO_CONTRA, "slot": "adverse effect",
 "q": "What is the specific concern with polymyxin B reaching the middle ear?",
 "opts": [
  ["Cochlear damage and hearing loss", "Correct. The harm is permanent and the drug was given for an ear complaint, which is what makes checking the drum first worth the trouble."],
  ["Facial nerve palsy", "Not the stated risk. The specific concern with polymyxin B reaching the middle ear is cochlear damage and hearing loss."],
  ["Chronic perforation of the drum", "The perforation is the route of entry rather than the consequence."],
  ["Vestibular failure alone", "The named harm is cochlear, so it is hearing rather than balance that is at risk when polymyxin B reaches the middle ear."]],
 "c": 0, "cite": D + ", Slide 10"},

{"topic": "Otic antibiotics", "io": IO_CONTRA, "slot": "adverse effect",
 "q": "Which otic ingredient is singled out for causing hypersensitivity?",
 "opts": [
  ["Neomycin", "Correct. A patient whose ear gets worse rather than better on drops may be reacting to the neomycin rather than failing treatment."],
  ["Hydrocortisone", "The steroid is not the sensitising component. Neomycin is the ingredient singled out for causing hypersensitivity."],
  ["Ciprofloxacin", "Not flagged for hypersensitivity here; the fluoroquinolone drops are the ones considered safe. Neomycin carries that warning."],
  ["Ofloxacin", "Not flagged for hypersensitivity here. Ofloxacin is offered as an alternative, while neomycin is the sensitising ingredient."]],
 "c": 0, "cite": D + ", Slide 10"},

{"topic": "Otic antibiotics", "io": IO_IND, "slot": "drug choice",
 "q": "Ciprofloxacin with dexamethasone is effective but expensive. What alternative is suggested?",
 "opts": [
  ["Ofloxacin with an ophthalmic dexamethasone",
   "Correct. An eye preparation used in the ear, which is a deliberate substitution rather than an error, and it reproduces the same two actions for less. An eye preparation used in the ear, which is a deliberate substitution rather than an error."],
  ["Neomycin with polymyxin B and hydrocortisone drops",
   "That combination carries the perforation restriction and the hypersensitivity problem."],
  ["Oral ciprofloxacin in place of the drops",
   "Switching to an oral agent is not the suggested economy. The alternative is ofloxacin with an ophthalmic dexamethasone preparation."],
  ["Plain hydrocortisone drops without any anti-infective",
   "That loses the anti-infective half of the treatment. The suggested alternative keeps both actions by pairing ofloxacin with dexamethasone."]],
 "c": 0, "cite": D + ", Slide 10"},

{"topic": "Otic antibiotics", "io": IO_CLASS, "slot": "drug choice",
 "q": "Which agents are listed as available otic anti-infectives?",
 "opts": [
  ["Ciprofloxacin, ofloxacin, and two steroid combinations",
   "Correct. Two plain fluoroquinolones and two combinations, and the combinations are where the restrictions live. In full: ciprofloxacin, ciprofloxacin with dexamethasone, neomycin with polymyxin B and hydrocortisone, and ofloxacin."],
  ["Amoxicillin, azithromycin and cefdinir, as drops",
   "These are oral agents rather than ear drops. The otic list is ciprofloxacin, ciprofloxacin with dexamethasone, the neomycin combination, and ofloxacin."],
  ["Gentamicin and tobramycin, given as ear drops",
   "Neither aminoglycoside is on the list of available otic agents; neomycin is the aminoglycoside that appears, and only within a combination."],
  ["Nystatin and ketoconazole, given as ear drops",
   "These are antifungals rather than otic anti-infectives. Nystatin treats oral candidiasis and ketoconazole systemic fungal infection."]],
 "c": 0, "cite": D + ", Slide 9"},

{"topic": "Ketoconazole", "io": IO_MOA, "slot": "mechanism",
 "q": "How does ketoconazole work?",
 "opts": [
  ["It alters fungal cell wall permeability by inhibiting cytochrome P450", "Correct. The same enzyme family it acts on in the fungus explains its behaviour in the patient, which is where its interactions come from."],
  ["It binds to the sterols already present in the fungal cell membrane",
   "That is nystatin's mechanism: it binds sterols already in the membrane. Ketoconazole acts on the machinery instead, by inhibiting cytochrome P450."],
  ["It inhibits fungal DNA synthesis", "Not the stated mechanism. Ketoconazole alters fungal cell wall permeability by inhibiting cytochrome P450."],
  ["It blocks fungal cell wall glucan synthesis", "That is the echinocandin mechanism, which is not described here."]],
 "c": 0, "cite": D + ", Slide 12"},

{"topic": "Ketoconazole", "io": IO_INTERACT, "slot": "mechanism",
 "q": "Why does ketoconazole interact with so many other medicines?",
 "opts": [
  ["It inhibits CYP3A4", "Correct. It raises the level of anything cleared by that route, which makes the interaction list a property of the enzyme rather than of any one drug pairing."],
  ["It is highly protein bound and displaces other drugs", "Displacement from protein binding is not the mechanism given. Ketoconazole inhibits CYP3A4, raising the level of anything cleared by that route."],
  ["It induces its own metabolism over time", "Induction would lower levels rather than raise them, and is not described."],
  ["It is eliminated unchanged by the kidney", "Renal elimination of unchanged drug would not generate these interactions. They come from inhibition of CYP3A4."]],
 "c": 0, "cite": D + ", Slide 12"},

{"topic": "Ketoconazole", "io": IO_IND, "slot": "drug choice",
 "q": "What is ketoconazole indicated for here?",
 "opts": [
  ["Systemic fungal infection", "Correct, and the contrast with nystatin is the point: one treats infection throughout the body, the other never leaves the mouth and gut."],
  ["Oral candidiasis alone", "That is nystatin's indication. Ketoconazole is used for systemic fungal infection, which is why it has to be absorbed."],
  ["Fungal otitis externa", "Not the indication given for ketoconazole, which is used for systemic fungal infection."],
  ["Prophylaxis during antibiotic courses", "Prophylaxis is not among its indications here; it is used to treat established systemic fungal infection."]],
 "c": 0, "cite": D + ", Slide 12"},

{"topic": "Nystatin", "io": IO_MOA, "slot": "mechanism",
 "q": "How does nystatin work?",
 "opts": [
  ["It binds membrane sterols and increases permeability",
   "Correct. It acts on what is already in the membrane rather than on the machinery that builds it, which is why it works on contact."],
  ["It inhibits cytochrome P450 within the fungal cell",
   "That is ketoconazole's mechanism. Nystatin binds sterols already present in the fungal membrane and increases permeability."],
  ["It inhibits protein synthesis in the fungal cell",
   "Not the stated mechanism. Nystatin acts on the membrane itself by binding sterols, rather than on protein synthesis."],
  ["It prevents the fungus adhering to the oral mucosa",
   "Not the stated mechanism. Nystatin binds sterols in the fungal cell membrane and increases its permeability."]],
 "c": 0, "cite": D + ", Slide 13"},

{"topic": "Nystatin", "io": IO_CLASS, "slot": "mechanism",
 "q": "Nystatin is classified as a nonabsorbable antifungal. Why does that matter?",
 "opts": [
  ["It acts only where it touches, and not elsewhere",
   "Correct. Being nonabsorbable is both the safety of the drug and its limitation: it is why it is well tolerated and why it cannot treat anything beyond the mucosa."],
  ["It must be given with food to be absorbed", "It is not absorbed at all, so food does not help. Being nonabsorbable is what confines it to the surfaces it touches."],
  ["It accumulates in the liver with repeated use", "Accumulation is not a feature of a drug that is not absorbed."],
  ["It requires renal dose adjustment", "A nonabsorbable drug does not reach the kidney to need adjusting."]],
 "c": 0, "cite": D + ", Slide 13"},

{"topic": "Nystatin", "io": IO_IND, "slot": "drug choice",
 "q": "A patient using an inhaled steroid develops oral candidiasis. Which of these situations is NOT given as a setting for it?",
 "opts": [
  ["Recent tympanostomy tube placement", "Correct -- this is not one of them. The settings given are inhaled steroids, HIV infection and chemotherapy, all of which share suppressed local or general immunity."],
  ["Use of an inhaled steroid", "This is one of the named settings, along with HIV infection and chemotherapy, all of which share suppressed immunity."],
  ["Human immunodeficiency virus infection",
   "This is one of the named settings, alongside inhaled steroid use and chemotherapy."],
  ["Chemotherapy", "This is one of the named settings, alongside inhaled steroid use and HIV infection."]],
 "c": 0, "cite": D + ", Slide 13"},

# --- agent-specific indications and adverse effects (added after the scope
# --- correction of 2026-09-18)

{"topic": "Ketoconazole", "io": IO_SE, "slot": "adverse effect",
 "q": "Which cardiac adverse effect is associated with ketoconazole?",
 "opts": [
  ["QTc prolongation", "Correct. It matters most alongside its CYP3A4 inhibition, because the drugs whose levels it raises may prolong the QT interval too."],
  ["Atrial fibrillation", "Not among the described effects. The cardiac concern with ketoconazole is prolongation of the QTc interval."],
  ["Heart block", "Not among the described effects; the cardiac effect associated with ketoconazole is QTc prolongation."],
  ["Cardiomyopathy", "Not among the described effects. Ketoconazole is associated with QTc prolongation rather than with structural heart disease."]],
 "c": 0, "cite": D + ", Slide 12"},

{"topic": "Ketoconazole", "io": IO_SE, "slot": "adverse effect",
 "q": "Which hepatic adverse effects are described with ketoconazole?",
 "opts": [
  ["Hepatitis, cirrhosis and hepatic failure",
   "Correct. A full spectrum from a blood test abnormality through to organ failure, which is why liver monitoring belongs with this drug. Deranged liver enzymes appear before any of these."],
  ["Gallstones with episodes of biliary colic",
   "Not among the described effects. The hepatic effects run from abnormal enzymes and hepatitis through cirrhosis to hepatic failure."],
  ["Hepatic vein thrombosis and portal hypertension",
   "Not among the described effects. Ketoconazole's liver toxicity is hepatitis, enzyme derangement, cirrhosis and failure."],
  ["Fatty liver with no change in liver enzymes",
   "The described effects include abnormal enzymes and progression to failure."]],
 "c": 0, "cite": D + ", Slide 12"},

{"topic": "Ketoconazole", "io": IO_SE, "slot": "adverse effect",
 "q": "Besides liver and cardiac effects, what else is described with ketoconazole?",
 "opts": [
  ["Hyperlipidaemia and orthostatic hypotension", "Correct. Neither is obvious for an antifungal, and the orthostatic drop is the one a patient will actually notice."],
  ["Hyperkalaemia and hypertension", "Not among the described effects. Ketoconazole is associated with hyperlipidaemia and orthostatic hypotension."],
  ["Neutropenia and thrombocytopenia together",
   "Not among the described effects; the further effects listed are hyperlipidaemia and orthostatic hypotension."],
  ["Peripheral neuropathy", "Not among the described effects. The additional effects described are hyperlipidaemia and orthostatic hypotension."]],
 "c": 0, "cite": D + ", Slide 12"},

{"topic": "Nystatin", "io": IO_SE, "slot": "adverse effect",
 "q": "What adverse effects are described with oral nystatin?",
 "opts": [
  ["Diarrhoea, nausea, stomach pain and vomiting", "Correct. All gastrointestinal, which is exactly what you would predict for a drug that stays in the gut and is never absorbed."],
  ["QTc prolongation and hepatitis", "Those belong to ketoconazole, which is absorbed. Nystatin stays in the gut, so its effects are gastrointestinal."],
  ["Sedation and dry mouth", "These belong to first generation antihistamines. Nystatin's effects are gastrointestinal, as befits a drug that is never absorbed."],
  ["Nosebleed and perforation of the septum",
   "These belong to nasal sprays. Nystatin causes gastrointestinal upset because it remains in the gut."]],
 "c": 0, "cite": D + ", Slide 13"},

{"topic": "Antifungal comparison", "io": IO_IND, "slot": "drug choice",
 "q": "A patient on an inhaled steroid has oral thrush and takes several other medicines. Which antifungal is preferred, and why?",
 "opts": [
  ["Nystatin, because it is not absorbed",
   "Correct. The property that limits it to surface infection is the same one that keeps it out of the patient's other drugs. Not being absorbed is also why it cannot interact with the patient's other medicines."],
  ["Ketoconazole, because it is the more potent agent",
   "Ketoconazole is absorbed and inhibits CYP3A4, which is the problem in a patient on several medicines."],
  ["Either one, since neither is absorbed at all",
   "Ketoconazole is absorbed; nystatin is the nonabsorbable one."],
  ["Neither, since thrush resolves without treatment",
   "Oral candidiasis is a stated indication for treatment, and nystatin treats it without reaching the rest of the patient."]],
 "c": 0, "cite": D + ", Slide 13"},

]
