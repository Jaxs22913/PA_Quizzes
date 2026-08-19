# CMS I Lecture 8 (Pigmented Skin Lesions) — SET 2, vignette pool A.
# Ephelides, lentigines, solar lentigo, seborrheic keratosis, dermatosis
# papulosa nigrans, vitiligo.
#
# LEAD-INS ARE BALANCED AS WRITTEN. Lecture 5's vignette build FAILED the 40%
# skew guard at 15 of 30 diagnosis lead-ins, because a catalogue-of-lesions
# lecture invites "which is the diagnosis" on every topic. This deck has the
# same shape, so each topic here gets a mix: roughly one diagnosis question to
# one management, education, test or next-step question.
#
# Options drafted at matched lengths, with distractors given the same compound
# shape as the answer beside them.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "CMS I Pigmented Skin Lesions - Shahsv-2.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Objective a — Etiologies, epidemiology, risk factors, manifestations, differential diagnosis, testing, management, referrals, education and prognosis of pigmented skin lesions"
IOB = "Objective b — Medical care strategies for pigmented skin lesions in adult and elderly populations"

POOL_A = [
 dict(topic="Ephelides", io=IOA,
   q="A 9-year-old girl with red hair and fair skin has small light brown symmetric macules 3 to 5 mm across over her nose and cheeks. Her mother says they are darker every summer and almost invisible by February. Which is the most likely diagnosis?",
   opts=[
     ["Ephelides",
      "Correct — the seasonal fading is what separates them from lentigines, which do not fade."],
     ["Lentigo simplex",
      "Those are uniformly black or brown and do not fade when sun exposure stops."],
     ["Solar lentigines",
      "Those are strongly associated with older age and cumulative sun damage."],
     ["Naevus spilus",
      "That is a tan background patch carrying scattered darker macules."]],
   c=0, cite=c(4)),

 dict(topic="Ephelides", io=IOA,
   q="A 24-year-old woman with freckles across her cheeks asks what will reduce them. Which is the most appropriate treatment plan?",
   opts=[
     ["Sun protection and counselling first, then topical depigmenting agents, with intense pulsed light or laser if needed",
      "Correct — hydroquinone, retinoids, alpha-hydroxy acids and botanicals are the topical options."],
     ["Cryotherapy to each lesion with five to ten second freezes, repeated over several sessions as needed",
      "Cryotherapy is impractical because of the size of the lesions."],
     ["Excision with negative margins for the largest lesions, with observation of the remainder",
      "That is the management of pigmented spindle cell naevus."],
     ["Narrow band ultraviolet B phototherapy given three times weekly over a five week course",
      "That is preventive therapy for polymorphous light eruption."]],
   c=0, cite=c(7)),

 dict(topic="Ephelides", io=IOA,
   q="A 21-year-old man with freckles asks whether laser treatment will get rid of them permanently. Which is the most appropriate counselling point?",
   opts=[
     ["Laser and intense pulsed light are preferred over cryotherapy, but the lesions can relapse",
      "Correct — sun protection and education remain the foundation of management."],
     ["Laser removes the lesions permanently, so no further sun protection will be needed",
      "Sun protection remains key, and lesions can relapse."],
     ["Cryotherapy is the preferred option because it treats each lesion individually",
      "Cryotherapy is difficult given the size of these lesions."],
     ["No treatment exists, so the lesions must simply be accepted as they are",
      "Several treatment options are described."]],
   c=0, cite=c(7)),

 dict(topic="Lentigines", io=IOA,
   q="A 58-year-old man has several uniformly brown round macules 3 to 4 mm across, some on the forearms and some on the buttocks, unchanged through the winter. Which is the most likely diagnosis?",
   opts=[
     ["Lentigines",
      "Correct — they occur on both sun-exposed and sun-protected areas and do not fade."],
     ["Ephelides",
      "Those fade when sun exposure stops and are more pronounced in summer."],
     ["Dysplastic naevi",
      "Those are at least 5 mm with irregular indistinct borders and variable pigmentation."],
     ["Blue naevi",
      "Those are blue to blue-black and sit deep in the dermis."]],
   c=0, cite=c(10)),

 dict(topic="Lentigines", io=IOB,
   q="A 62-year-old woman with several lentigines on the hands asks whether they need treating. Which is the most appropriate response?",
   lead="treatment",
   opts=[
     ["No treatment is necessary; cosmetic removal by cryotherapy or quality-switched laser is an option if she prefers",
      "Correct — the diagnosis is clinical and the lesions are benign."],
     ["Excision with clear margins is needed on every lesion, because of the risk of transformation",
      "The lesions are benign and excision is not required."],
     ["Topical depigmenting agents are the only option, since cryotherapy cannot be used at all",
      "Cryotherapy is an option for lentigines."],
     ["Sun protection alone will make the lesions fade over the course of the following winter",
      "Lentigines do not fade when sun exposure stops."]],
   c=0, cite=c(12)),

 dict(topic="Lentigines", io=IOA,
   q="A 34-year-old man has generalised darkly pigmented lentigines over much of his body. Which additional consideration does this raise?",
   lead="next step",
   opts=[
     ["An inherited disorder should be considered, as with LAMB and myxoma syndrome",
      "Correct — a partial or generalised lentigo is what prompts that question."],
     ["Neurocutaneous melanosis should be considered, and brain imaging arranged",
      "That concern belongs to congenital naevi of the head and midline."],
     ["Dysplastic naevus syndrome should be considered, and every lesion biopsied",
      "That syndrome involves naevi rather than lentigines."],
     ["An internal malignancy should be considered, and urgent screening arranged",
      "That association belongs to acanthosis nigricans."]],
   c=0, cite=c(10)),

 dict(topic="Solar lentigo", io=IOA,
   q="A 66-year-old man who has worked outdoors for decades has light to dark brown macules with irregular borders on the shoulders, some coalescing where he recalls a severe sunburn. Which is the most likely diagnosis?",
   opts=[
     ["Solar lentigines",
      "Correct — they coalesce at sites of severe sunburn and 90% of people have them by fifty."],
     ["Lentigo simplex",
      "Those are well circumscribed, uniform and always under 5 mm."],
     ["Ephelides",
      "Those are small symmetric macules that fade with reduced sun exposure."],
     ["Dermatosis papulosa nigrans",
      "Those are papules on the face and neck in darker skin types."]],
   c=0, cite=c(14)),

 dict(topic="Solar lentigo", io=IOB,
   q="A 70-year-old woman with numerous solar lentigines asks what her lesions mean for her health. Which is the most appropriate counselling point?",
   opts=[
     ["The lesions themselves are benign, but they mark sun damage that is also associated with actinic keratosis and skin cancers",
      "Correct — the association includes squamous cell carcinoma, basal cell carcinoma and melanoma."],
     ["The lesions are premalignant and each one carries a measurable chance of becoming a melanoma",
      "The lesions themselves are benign."],
     ["The lesions indicate an underlying internal malignancy and warrant urgent systemic screening",
      "That association belongs to acanthosis nigricans."],
     ["The lesions will fade over the coming winter if she avoids further exposure to the sun",
      "Solar lentigines do not fade with cessation of sun exposure."]],
   c=0, cite=c(13)),

 dict(topic="Solar lentigo", io=IOA,
   q="A 55-year-old man who had photochemotherapy for psoriasis has brown-black irregular macules on his buttocks as well as his forearms. Which is the most likely explanation?",
   opts=[
     ["PUVA lentigines, which affect sun-protected as well as sun-exposed sites",
      "Correct — they relate to the total number of treatments, male sex, fair skin and older age."],
     ["Ordinary solar lentigines, which affect only chronically sun-exposed sites",
      "Buttock involvement is what points away from ordinary solar lentigines."],
     ["Ephelides, which appear on sun-exposed skin in fair-skinned individuals",
      "Those are small light brown symmetric macules that fade in winter."],
     ["Naevus spilus, which is present at birth or within the first years of life",
      "That is a congenital lesion with a tan background patch."]],
   c=0, cite=c(13)),

 dict(topic="Seborrheic keratosis", io=IOB,
   q="A 74-year-old woman has several beige to dark brown papules 5 to 15 mm on the trunk that feel warty and look pasted onto the skin. She is worried they are cancers. Which is the most appropriate response?",
   opts=[
     ["They are benign seborrheic keratoses, diagnosed clinically, and management is supportive",
      "Correct — they are common in older adults and easily mistaken for neoplasms."],
     ["They are premalignant lesions requiring biopsy of each one before any reassurance",
      "The diagnosis is clinical and the lesions are benign."],
     ["They are dysplastic naevi requiring excision because of the risk of melanoma",
      "Those are melanocytic lesions over 5 mm with irregular borders."],
     ["They are solar lentigines requiring cryotherapy for cosmetic improvement",
      "Those are macular rather than raised and velvety."]],
   c=0, cite=c(17)),

 dict(topic="Seborrheic keratosis", io=IOA,
   q="A 68-year-old man has one seborrheic keratosis on the back that has become itchy and inflamed where his belt rubs. Which is the most appropriate treatment?",
   opts=[
     ["Cryotherapy, though the lesion may recur afterwards",
      "Correct — asymptomatic lesions need no treatment at all."],
     ["Excision with negative margins to prevent it recurring",
      "That is the management of pigmented spindle cell naevus."],
     ["Topical depigmenting agents applied over several months",
      "Those are used for ephelides."],
     ["Observation alone, since no treatment exists for these",
      "Cryotherapy is the named option for symptomatic lesions."]],
   c=0, cite=c(17)),

 dict(topic="Dermatosis papulosa nigrans", io=IOA,
   q="A 46-year-old African American woman has dozens of smooth firm dark brown papules 1 to 3 mm across over both cheeks and the neck, present for years. Which is the most likely diagnosis?",
   opts=[
     ["Dermatosis papulosa nigrans",
      "Correct — identical to small seborrheic keratoses, commonest in this group, with females affected more than males."],
     ["Multiple blue naevi of the face",
      "Those are blue to blue-black and commonest in women in their twenties."],
     ["Dysplastic naevi of the face and neck",
      "Those are at least 5 mm with irregular borders and variable pigmentation."],
     ["Acquired lentigines of the face and neck",
      "Those are macular rather than smooth firm papules."]],
   c=0, cite=c(19)),

 dict(topic="Dermatosis papulosa nigrans", io=IOA,
   q="A 44-year-old woman with dermatosis papulosa nigrans asks about removing the lesions. Which is the most appropriate advice?",
   lead="treatment",
   opts=[
     ["They are best left untreated; excision, curettage or laser can be used, but cryotherapy is avoided",
      "Correct — cryotherapy risks post-inflammatory hyperpigmentation in this group."],
     ["Cryotherapy at the first visit is the treatment of choice, with laser reserved for recurrences",
      "Cryotherapy is specifically avoided in this condition."],
     ["Topical depigmenting agents should be tried first, since the lesions are pigmented macules",
      "The lesions are papules, and those agents are used for ephelides."],
     ["Wide excision is needed because these lesions can transform into melanoma over time",
      "The lesions are benign."]],
   c=0, cite=c(19)),

 dict(topic="Dermatosis papulosa nigrans", io=IOA,
   q="A 41-year-old man with facial papules typical of dermatosis papulosa nigrans has one lesion that looks different from the rest. Which is the most appropriate next step?",
   opts=[
     ["Biopsy that lesion, since biopsy is indicated where the diagnosis is uncertain",
      "Correct — the diagnosis is otherwise clinical."],
     ["Treat all the lesions with cryotherapy and review the atypical one afterwards",
      "Cryotherapy is avoided here, and treating an atypical lesion forfeits the diagnosis."],
     ["Reassure him, since every lesion in this condition is benign without exception",
      "An atypical lesion warrants biopsy rather than reassurance."],
     ["Arrange dermoscopy of the whole face and repeat it again in twelve months",
      "Biopsy is the named step where the diagnosis is uncertain."]],
   c=0, cite=c(19)),

 dict(topic="Vitiligo", io=IOA,
   q="A 19-year-old woman has asymptomatic white non-scaly patches with sharp margins around the mouth, on the fingertips and in the genital area, appearing symmetrically over six months. Which is the most likely diagnosis?",
   opts=[
     ["Non-segmental vitiligo",
      "Correct — symmetrical distribution with a preference for face, genitals and acral areas."],
     ["Segmental vitiligo",
      "That is unilateral, does not cross the midline, and follows block-like patterns."],
     ["Tinea versicolor of the face and trunk",
      "That produces scaly patches with hyphae on potassium hydroxide."],
     ["Post-inflammatory hypopigmentation",
      "That follows an inflammatory dermatosis and lacks these sharp margins."]],
   c=0, cite=c(23)),

 dict(topic="Vitiligo", io=IOA,
   q="A 22-year-old man has depigmented patches confined to the left side of the trunk in a block-like pattern that stops at the midline. Which is the most important consequence of this pattern?",
   lead="diagnosis",
   opts=[
     ["It is the segmental variant, which differs in both diagnostic tools and treatment",
      "Correct — segmental disease is characterised by unpredictable cycles of flare and stabilisation."],
     ["It is non-segmental disease, which is treated with phototherapy from the outset",
      "Non-segmental disease is symmetrical and does not respect the midline."],
     ["It is a post-inflammatory change, which resolves on its own within several months",
      "The block-like distribution and sharp margins point to segmental vitiligo."],
     ["It is a fungal infection, which is confirmed with a potassium hydroxide preparation",
      "Vitiligo lesions are non-scaly and fluoresce under a Wood's lamp."]],
   c=0, cite=c(23)),

 dict(topic="Vitiligo", io=IOA,
   q="A 27-year-old woman with newly diagnosed vitiligo is having her workup arranged. Which investigations are appropriate?",
   opts=[
     ["Wood's lamp examination in a dark room, with a complete blood count and antinuclear antibody",
      "Correct — the labs address the autoimmune diseases associated with vitiligo."],
     ["Punch biopsy of the leading edge sent for direct immunofluorescence and antigen mapping",
      "Biopsy is not the described approach for vitiligo."],
     ["Minimal erythema dose testing to ultraviolet A and to ultraviolet B before treatment",
      "That belongs to the photosensitivity workup."],
     ["Potassium hydroxide preparation of a skin scraping taken from the affected patches",
      "That would investigate a fungal cause, which these lesions are not."]],
   c=0, cite=c(23)),

 dict(topic="Vitiligo", io=IOA,
   q="A 24-year-old woman has vitiligo involving about 3% of her body surface, mostly on the face and neck. Which topical option best suits those sites?",
   opts=[
     ["A topical calcineurin inhibitor such as tacrolimus or pimecrolimus",
      "Correct — they suit areas where steroids cannot be applied, though they carry an increased cancer risk."],
     ["A high-potency topical corticosteroid applied twice daily to the face",
      "Steroids risk skin atrophy and raised intraocular pressure at these sites."],
     ["A topical depigmenting agent such as hydroquinone or an alpha-hydroxy acid",
      "Depigmenting agents would worsen rather than treat the problem."],
     ["A topical retinoid applied nightly to the affected areas of skin",
      "Retinoids are not among the described therapies for vitiligo."]],
   c=0, cite=c(24)),

 dict(topic="Vitiligo", io=IOA,
   q="A 31-year-old man has vitiligo affecting roughly 20% of his body surface. Which is the most appropriate first-line treatment?",
   opts=[
     ["Phototherapy with narrow band ultraviolet B, ideally combined with topical therapy",
      "Correct — narrow band ultraviolet B is preferred over PUVA, which raises skin cancer risk."],
     ["Topical corticosteroid alone applied twice daily to all the affected areas",
      "Topical therapy suits involvement below 5% of the body surface."],
     ["Surgical tissue or cellular grafting to repopulate the depigmented areas",
      "Grafting is reserved for highly stable disease."],
     ["PUVA phototherapy, which is preferred to narrow band ultraviolet B here",
      "PUVA carries adverse effects including increased skin cancer risk."]],
   c=0, cite=c(25)),

 dict(topic="Vitiligo", io=IOA,
   q="A 26-year-old man with vitiligo says he has stopped going out because of how his skin looks, and that his doctor called it purely cosmetic. Which is the most appropriate response?",
   opts=[
     ["The psychological and social impact is real, and psychological intervention is part of management",
      "Correct — low self-esteem and poor body image are named explicitly."],
     ["The condition is indeed cosmetic, so treatment is optional and reassurance is enough",
      "The lecture cautions specifically against dismissing it that way."],
     ["The condition indicates an underlying malignancy, which explains how unwell he feels",
      "That association belongs to acanthosis nigricans."],
     ["The condition will resolve spontaneously within a year, so no treatment is needed",
      "Spontaneous resolution is not described."]],
   c=0, cite=c(21)),
]
