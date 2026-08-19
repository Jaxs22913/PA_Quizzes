# CMS I Lecture 5 (Dermatological Infestations) — SET 2, vignette pool D.
#
# A corrective pool, and the skew guard is what found the problem. Pools A to C
# came out 30 diagnosis lead-ins out of 62 -- 48% -- against a single "which
# test". The cause is structural: this lecture is a catalogue of distinct
# organisms, so "which is the most likely diagnosis" is the question the content
# invites on nearly every topic. The build failed on SET 1 at 15/30 before this
# pool existed.
#
# Every question here uses a NON-diagnosis lead-in: next step, which test,
# treatment, or patient education.
#
# Options drafted at matched lengths. Correct answer is ALWAYS written first.
SRC = "CMS I Dermatological Infestations - Shahsv.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Objective a — Etiologies, epidemiology, risk factors, manifestations, differential diagnosis, testing, management, referrals, education and prognosis of dermatological infestations"
IOB = "Objective b — Differentiate primary from secondary skin lesions"
IOC = "Objective c — Medical care strategies across infant, child, adolescent, adult and elderly populations"

POOL_D = [
 dict(topic="Scabies", io=IOA,
   q="A 27-year-old woman with suspected scabies has heavily excoriated hands and no intact burrow visible. Which test is most appropriate?",
   opts=[
     ["The burrow ink test, looking for a zigzag line running across and away from the lesion",
      "Correct — blue or black ink is applied to a suspected lesion when scraping is difficult."],
     ["A potassium hydroxide wet mount of a plucked hair examined under the microscope",
      "That test identifies dermatophyte infection."],
     ["Serology for immunoglobulin M and immunoglobulin G against the causative mite",
      "Serology belongs to Lyme disease rather than scabies."],
     ["A bacterial culture taken from an excoriated area and sent for sensitivities",
      "Culture would only identify secondary infection."]],
   c=0, cite=c(14)),

 dict(topic="Scabies", io=IOA,
   q="A 30-year-old pregnant woman has been in contact with a household member diagnosed with scabies but has no symptoms and no lesions. Which is the most appropriate next step?",
   opts=[
     ["Withhold treatment, since pregnant patients are treated only where scabies is documented",
      "Correct — treating all infested persons in the group applies to those with documented infestation."],
     ["Treat her with permethrin now, since all household contacts are treated regardless",
      "The lecture qualifies treatment in pregnancy to documented cases."],
     ["Treat her with oral ivermectin now, since topical agents are avoided in pregnancy",
      "Ivermectin is reserved for hyperkeratotic or immunosuppressed cases."],
     ["Treat her only after delivery, whatever her symptoms or examination findings show",
      "Documented scabies in pregnancy is treated rather than deferred."]],
   c=0, cite=c(19)),

 dict(topic="Scabies", io=IOA,
   q="A 45-year-old man treated for scabies has scrubbed his skin with a strong antibacterial soap several times a day and now has widespread irritation. Which is the most appropriate counselling point?",
   opts=[
     ["Excessive washing with harsh soap can worsen the skin irritation and should be stopped",
      "Correct — the permethrin course itself is what treats the infestation."],
     ["Vigorous washing is essential to remove the mites from the surface of the skin",
      "Washing is not what kills the mites; the treatment is."],
     ["The irritation confirms the treatment has failed and a second agent is needed",
      "The irritation is from the washing rather than treatment failure."],
     ["The irritation indicates a secondary bacterial infection needing oral antibiotics",
      "There is no described fever, purulence or spreading erythema."]],
   c=0, cite=c(19)),

 dict(topic="Pediculosis", io=IOC,
   q="A 6-year-old girl has been treated for head lice and her mother asks what to do about the house. Which is the most appropriate advice?",
   opts=[
     ["Put clothing and bedding from the past week in the dryer or bag it for two weeks, wash combs and vacuum",
      "Correct — fumigation is specifically not recommended."],
     ["Have the home professionally fumigated and discard all pillows and soft furnishings",
      "Fumigation is specifically not recommended."],
     ["Wash everything at 60 degrees Celsius and treat every household member immediately",
      "That is the household measure for scabies."],
     ["Engage a professional exterminator to treat cracks and crevices around the beds",
      "That is the requirement for bedbugs."]],
   c=0, cite=c(30)),

 dict(topic="Pediculosis", io=IOA,
   q="A 10-year-old boy's parents want to avoid chemical treatment for head lice. Which physical approach can be offered, and with what caveat?",
   opts=[
     ["Combing nits out after two minutes of hair moisturiser every few days, though it is slow and needs adjuvant therapy",
      "Correct — head shaving is the other physical option named."],
     ["Applying mayonnaise or mineral oil weekly to smother the lice and their attached eggs",
      "Those occlusive agents may not be lethal to lice."],
     ["Washing the hair daily with an antibacterial shampoo until no live lice are seen",
      "That is not among the described physical methods."],
     ["Waiting without treatment, since head lice clear spontaneously within a few weeks",
      "Spontaneous clearance is not described here."]],
   c=0, cite=c(30)),

 dict(topic="Bedbugs", io=IOA,
   q="A 41-year-old woman with bedbug bites has scratched several open and one is now crusted and tender. Which is the most appropriate treatment?",
   opts=[
     ["Topical antiseptic lotion or antibiotic cream for the secondary infection, with local wound care",
      "Correct — topical steroids or oral antihistamines address the pruritus separately."],
     ["An oral antibiotic covering methicillin-resistant Staphylococcus aureus for ten days",
      "Systemic therapy is not the described first response here."],
     ["Overnight topical permethrin to the whole skin surface with a repeat dose at one week",
      "That is the treatment for scabies."],
     ["Surgical excision of the affected lesions followed by tetanus prophylaxis",
      "That is the treatment for tungiasis."]],
   c=0, cite=c(35)),

 dict(topic="Fleas and tungiasis", io=IOA,
   q="A 33-year-old man is travelling to Nigeria and asks how to avoid tungiasis. Which is the most appropriate advice?",
   opts=[
     ["Do not walk barefoot or in sandals on beaches, and do not sit directly on the sand",
      "Correct — Nigeria, the Caribbean, India and Brazil are the named endemic settings."],
     ["Use DEET-based repellent reapplied every two hours and perform daily body checks",
      "That advice prevents tick-borne illness."],
     ["Avoid contact with the bedding and underclothing of anyone who is infested",
      "That advice concerns scabies transmission."],
     ["Inspect hotel headboards and picture frames before unpacking any luggage",
      "That advice concerns bedbugs."]],
   c=0, cite=c(40)),

 dict(topic="Fleas and tungiasis", io=IOA,
   q="A 47-year-old man has a nodular lesion on the toe suspected to be tungiasis. Which test confirms it?",
   opts=[
     ["Dermoscopy, which visualises the ovoid eggs within the lesion",
      "Correct — treatment is then surgical excision or cryotherapy."],
     ["Skin scraping with mineral oil examined under the microscope",
      "That is the diagnostic method for scabies."],
     ["Light microscopy with mineral oil looking for live larvae",
      "That is used in cutaneous larva migrans folliculitis."],
     ["Indirect immunofluorescence assay for specific antibodies",
      "That is the gold standard for Rocky Mountain spotted fever."]],
   c=0, cite=c(40)),

 dict(topic="Hymenoptera", io=IOA,
   q="A 34-year-old woman has a mild local reaction to a bee sting with pain and a small area of redness. Which is the most appropriate treatment?",
   opts=[
     ["Cleaning, ice, and possibly injection of local anaesthetic for pain control",
      "Correct — management is graded to the severity of the reaction."],
     ["Intramuscular epinephrine with transfer to an emergency department",
      "That is reserved for anaphylaxis."],
     ["A systemic corticosteroid course tapered over the following week",
      "That is not the described treatment for a mild local reaction."],
     ["An epinephrine auto-injector prescription and desensitisation referral",
      "Those follow sting-induced anaphylaxis with a positive skin test."]],
   c=0, cite=c(44)),

 dict(topic="Caterpillars", io=IOA,
   q="A 15-year-old boy has severe pain after an asp caterpillar sting that is not controlled by an oral analgesic. Which additional options are described?",
   opts=[
     ["Oral or parenteral narcotic analgesia, with antivenom for certain categories",
      "Correct, alongside antihistamines, menthol or camphor, and corticosteroids."],
     ["Intravenous calcium gluconate with a muscle relaxant and a benzodiazepine",
      "That is envenomation treatment for a black widow spider bite."],
     ["Intramuscular epinephrine repeated at intervals until the pain has settled",
      "Epinephrine treats anaphylaxis rather than local pain."],
     ["A ten-day course of oral doxycycline to prevent secondary skin infection",
      "Antibiotics are not part of the described treatment."]],
   c=0, cite=c(48)),

 dict(topic="Cutaneous larva migrans", io=IOA,
   q="A 29-year-old man treated for hookworm folliculitis has persistent follicular pustules after one course of albendazole. Which is the most appropriate next step?",
   opts=[
     ["Repeat the course, since hookworm folliculitis may need repeated treatments",
      "Correct — the folliculitic form is specifically noted to be more resistant."],
     ["Switch to topical therapy, which is more effective for the follicular form",
      "Topical therapy is described as less effective."],
     ["Excise the affected follicles, since surgery clears resistant lesions",
      "Surgical excision is specifically not recommended."],
     ["Apply cryotherapy to each pustule, since freezing kills the larvae",
      "Cryotherapy is specifically not recommended."]],
   c=0, cite=c(54)),

 dict(topic="Black widow spider", io=IOA,
   q="A 38-year-old man with a black widow spider bite is being treated for envenomation. Which additional measure should be checked?",
   opts=[
     ["That his tetanus vaccination is up to date",
      "Correct, alongside calcium gluconate, narcotics, muscle relaxants and benzodiazepines."],
     ["That he has had a course of prophylactic antibiotics",
      "Antibiotics are not part of the described treatment."],
     ["That an antivenom skin test has been performed first",
      "Skin testing is not among the described measures."],
     ["That the wound has been debrided before he is admitted",
      "Debridement is not part of this envenomation's treatment."]],
   c=0, cite=c(58)),

 dict(topic="Hobo spider", io=IOA,
   q="A 42-year-old woman bitten by a hobo spider has fatigue, headache and difficulty concentrating a week later. Which is the most appropriate counselling point?",
   opts=[
     ["Headaches may persist for about a week and the symptoms are managed supportively",
      "Correct — death from severe systemic effects, including aplastic anaemia, is rare."],
     ["These symptoms indicate an evolving necrotic wound needing surgical review",
      "Systemic symptoms of this kind are part of the envenomation itself."],
     ["These symptoms indicate a secondary infection requiring an oral antibiotic",
      "There is no described fever, purulence or spreading erythema."],
     ["These symptoms indicate an allergic reaction needing an antihistamine course",
      "The described systemic effects are not allergic."]],
   c=0, cite=c(65)),

 dict(topic="Lyme disease", io=IOA,
   q="A 39-year-old man in Arizona, where Lyme disease is not endemic, has fatigue and joint aches and asks to be tested. Which is the most appropriate response?",
   opts=[
     ["Testing is most helpful in exactly this situation — outside an endemic region with possibly consistent symptoms",
      "Correct — enzyme-linked immunosorbent assay first, with Western blot more specific."],
     ["Testing is not indicated at all, since Lyme disease occurs only in the northeastern states",
      "The lecture names testing as most helpful in non-endemic patients."],
     ["Testing should be deferred until an erythema migrans lesion has actually appeared",
      "A patient with that lesion is diagnosed clinically without testing."],
     ["Testing should be replaced by an empirical course of doxycycline for two weeks",
      "Empirical treatment without assessment is not the described approach."]],
   c=0, cite=c(77)),

 dict(topic="Lyme disease", io=IOA,
   q="A 45-year-old woman finds an attached tick on her leg after gardening in Maine. Which is the most appropriate immediate action?",
   opts=[
     ["Remove the tick immediately, then watch for the rash and constitutional symptoms",
      "Correct — antibiotics are indicated once the disease is diagnosed, at all stages."],
     ["Leave the tick in place until it detaches, since removal can force in more organism",
      "Immediate removal is the described first step."],
     ["Start a ten to fourteen day course of doxycycline the same day as the bite",
      "Treatment follows diagnosis rather than every bite."],
     ["Send serology the same day and treat only if the result comes back positive",
      "Serology so early would not be informative."]],
   c=0, cite=c(79)),

 dict(topic="Rocky Mountain spotted fever", io=IOA,
   q="A 62-year-old man is being treated for Rocky Mountain spotted fever and asks how long the course will last. Which is the most appropriate answer?",
   opts=[
     ["Doxycycline 100 mg by mouth every twelve hours for five to ten days",
      "Correct — the same agent is used in pregnancy, and children get a weight-based dose."],
     ["Doxycycline 100 mg by mouth every twelve hours for four to six weeks",
      "That is longer than the described course."],
     ["Amoxicillin three times daily for a course of ten to fourteen days",
      "That regimen belongs to Lyme disease in children and pregnancy."],
     ["Azithromycin once daily for a course of five days, then reassessment",
      "Macrolides are not the treatment for this illness."]],
   c=0, cite=c(86)),

 dict(topic="Rocky Mountain spotted fever", io=IOC,
   q="A 5-year-old girl needs treatment for Rocky Mountain spotted fever but her parents raise the usual concerns about doxycycline in young children. Which is the most appropriate response?",
   opts=[
     ["Doxycycline is still used here, with a desensitisation protocol available where it is contraindicated",
      "Correct — the risk of untreated disease outweighs the concern about tooth staining."],
     ["Doxycycline must be avoided under eight years, so azithromycin is substituted instead",
      "Doxycycline is used in this illness in children."],
     ["Doxycycline must be avoided under eight years, so amoxicillin is substituted instead",
      "That substitution belongs to Lyme disease."],
     ["Doxycycline should be delayed until the child is confirmed positive on serology",
      "Treatment should start by day 5, before serology is informative."]],
   c=0, cite=c(86)),

 dict(topic="Cercarial dermatitis", io=IOA,
   q="A 17-year-old boy who swims in the same lake each summer asks how to reduce his risk of swimmer's itch. Which is the most appropriate advice?",
   opts=[
     ["Wash and dry the skin properly after leaving the water",
      "Correct — treatment otherwise is symptomatic when the eruption occurs."],
     ["Apply DEET-based repellent to the legs before entering the water",
      "That prevents tick and insect bites rather than this."],
     ["Wear closed footwear on the shore and avoid sitting on the sand",
      "That advice prevents tungiasis."],
     ["Take a prophylactic antiparasitic before each swimming session",
      "Prophylactic drug treatment is not described here."]],
   c=0, cite=c(91)),
]
