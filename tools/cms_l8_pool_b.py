# CMS I Lecture 8 (Pigmented Skin Lesions) — SET 1 pool B (objective style).
# Melanocytic naevi: congenital, naevus spilus, common acquired, blue,
# pigmented spindle cell (Reed), Spitz and dysplastic.
#
# Options drafted at matched lengths. Pool A of this lecture came out 57% raw
# before repair, for the same structural reason as Lecture 5's pool C: the whole
# deck is compare-and-contrast across a catalogue of lesions, so the correct
# answer is a compound description and each distractor names a different lesion
# in fewer words. Every distractor here is written to the same compound shape as
# the answer it sits beside.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "CMS I Pigmented Skin Lesions - Shahsv-2.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "a — Etiologies, epidemiology, risk factors, manifestations, differential diagnosis, testing, management, referrals, education and prognosis of pigmented skin lesions"
IOB = "b — Medical care strategies for pigmented skin lesions in adult and elderly populations"

POOL_B = [
 dict(topic="Melanocytic naevi", io=IOA,
   q="How are melanocytic naevi divided by origin?",
   opts=[
     ["Acquired naevi arise from junctional melanocytes; congenital naevi arise from neural-crest derived precursors migrating along neurovascular bundles",
      "Correct — dysplastic naevi are the group displaying atypical architectural and cytologic features."],
     ["Acquired naevi arise from neural-crest derived precursors; congenital naevi arise from junctional melanocytes within the epidermis",
      "That reverses the two origins."],
     ["Acquired naevi arise from keratinocytes of the basal layer; congenital naevi arise from hair follicle precursor cells in the dermis",
      "Neither lesion arises from keratinocytes or follicular cells."],
     ["Acquired naevi arise from dermal fibroblasts; congenital naevi arise from vascular endothelium along the neurovascular bundles",
      "Neither lesion arises from fibroblasts or endothelium."]],
   c=0, cite=c(27)),

 dict(topic="Congenital melanocytic naevi", io=IOA,
   q="What determines melanoma risk in a congenital melanocytic naevus, and where do they most often occur?",
   opts=[
     ["The larger the lesion the higher the risk, and they occur most commonly on the trunk and extremities",
      "Correct — the scalp and face are also affected, and neurofibromatosis type I is a named risk."],
     ["The smaller the lesion the higher the risk, and they occur most commonly on the palms and the soles",
      "That reverses the size relationship and gives the wrong distribution."],
     ["The darker the pigment the higher the risk, and they occur most commonly on the face and the neck",
      "Size rather than pigment intensity is what the lecture ties to risk."],
     ["The number of lesions determines the risk, and they occur most commonly on sun-exposed surfaces",
      "Number of lesions is the risk relationship described for dysplastic naevi."]],
   c=0, cite=c(28)),

 dict(topic="Congenital melanocytic naevi", io=IOA,
   q="Describe the clinical appearance of congenital melanocytic naevi.",
   opts=[
     ["Flat brown patches or plaques with smooth or slightly uneven borders, sometimes pebbly, rugose, verrucous or lobular",
      "Correct — they are evident at birth or shortly after."],
     ["Sharply circumscribed jet-black papules under 7 mm across, sometimes with shades of blue, grey or brown",
      "That describes pigmented spindle cell naevus."],
     ["Solitary pink or red hairless dome-shaped firm papules that grow and then stabilise over time",
      "That describes Spitz naevus."],
     ["Deeply pigmented blue to blue-black macules under 1 cm across on the dorsal hands, scalp or sacrum",
      "That describes blue naevus."]],
   c=0, cite=c(29)),

 dict(topic="Congenital melanocytic naevi", io=IOA,
   q="What is neurocutaneous melanosis and which patients are at risk?",
   opts=[
     ["A related condition in patients with naevi on the head, neck or posterior midline, causing seizures, hydrocephalus, neurological deficits and vomiting",
      "Correct — the prognosis is poor once neurological symptoms appear, usually in the first few years of life."],
     ["A related condition in patients with naevi on the trunk and extremities, causing pigmented macules within a tan background patch",
      "That describes naevus spilus."],
     ["A related condition in patients with over one hundred naevi by adolescence, carrying a high risk of progression to melanoma",
      "That describes dysplastic naevus syndrome."],
     ["A related condition in patients with multiple Spitz naevi, associated with an underlying familial cancer syndrome",
      "That association belongs to multiple Spitz lesions."]],
   c=0, cite=c(29)),

 dict(topic="Congenital melanocytic naevi", io=IOA,
   q="Which imaging is indicated for a congenital melanocytic naevus on the cranium or axial midline?",
   opts=[
     ["Magnetic resonance imaging of the brain, with or without total spine, matched to the anatomic location of the naevus",
      "Correct — the concern is neurocutaneous melanosis."],
     ["Computed tomography of the affected area, to define the depth and the extent of the pigmented lesion",
      "That is not the described imaging for this concern."],
     ["Ultrasound of the lesion to assess the thickness of the pigmented tissue before any excision",
      "That is not the described imaging for this concern."],
     ["Whole-body positron emission tomography to screen for metastatic melanoma at presentation",
      "That is not the described imaging for this concern."]],
   c=0, cite=c(30)),

 dict(topic="Congenital melanocytic naevi", io=IOA,
   q="What determines management of a congenital melanocytic naevus?",
   opts=[
     ["Melanoma risk together with cosmetic and functional considerations, removing as much as possible while preserving function",
      "Correct — observation may be the better option where there is little skin for a graft site."],
     ["Lesion size alone, with every lesion over 5 mm excised regardless of its site or of graft availability",
      "Function, cosmesis and graft availability all enter the decision."],
     ["Patient age alone, with all lesions excised before the child reaches school age",
      "Age alone is not the determinant described."],
     ["Pigment intensity alone, with darker lesions excised and lighter ones observed",
      "Pigment intensity is not the determinant described."]],
   c=0, cite=c(31)),

 dict(topic="Naevus spilus", io=IOA,
   q="Describe naevus spilus and its melanoma risk.",
   opts=[
     ["A spotted naevus with a tan café-au-lait-like background carrying scattered darker macules or papules, which rarely progresses to melanoma",
      "Correct — the background patch ranges from under 1 cm to over 10 cm, most often on trunk and extremities."],
     ["A spotted naevus with a uniformly black background carrying scattered pale macules, which frequently progresses to melanoma",
      "That inverts both the appearance and the risk."],
     ["A group of deeply pigmented dermal lesions of spindle or epithelioid melanocytes, which rarely progresses to melanoma",
      "That describes blue naevus."],
     ["A collection of atypical naevi over 5 mm with irregular indistinct borders, which frequently progresses to melanoma",
      "That describes dysplastic melanocytic naevus."]],
   c=0, cite=c(32)),

 dict(topic="Naevus spilus", io=IOA,
   q="How is naevus spilus managed?",
   opts=[
     ["Observation with periodic clinical evaluation, plus sun protection counselling",
      "Correct — it rarely progresses to melanoma."],
     ["Excision with negative margins at the time it is first identified clinically",
      "That is the management of pigmented spindle cell naevus."],
     ["Cryotherapy or quality-switched laser for cosmetic removal if preferred",
      "That is the cosmetic management of lentigines."],
     ["Magnetic resonance imaging of the brain and total spine at presentation",
      "That is indicated for cranial or axial congenital melanocytic naevi."]],
   c=0, cite=c(34)),

 dict(topic="Naevus spilus", io=IOA,
   q="With what other anomalies can naevus spilus be associated?",
   opts=[
     ["Anomalies of vascular, central nervous system or connective tissue origin",
      "Correct — it is a variant of congenital naevus present at birth or in the first years of life."],
     ["Anomalies of the endocrine system with insulin resistance and hyperandrogenism",
      "Those associations belong to acanthosis nigricans."],
     ["Anomalies of the gastrointestinal tract with malabsorption and coeliac disease",
      "That association belongs to dermatitis herpetiformis."],
     ["Anomalies of the haematologic system with monoclonal gammopathy and myeloma",
      "That association belongs to pyoderma gangrenosum."]],
   c=0, cite=c(33)),

 dict(topic="Common acquired naevus", io=IOA,
   q="Describe the natural history of common acquired melanocytic naevi.",
   opts=[
     ["They develop slowly after birth, enlarge symmetrically, stabilise and regress, peaking in number in the thirties then declining",
      "Correct — melanoma risk rises with the number of lesions."],
     ["They are present at birth, enlarge in proportion to the child's own growth, and never regress at any stage",
      "That describes congenital melanocytic naevi."],
     ["They appear only after the age of fifty, enlarge steadily, and do not fade when sun exposure ends",
      "That describes solar lentigo."],
     ["They appear in early childhood, darken with ultraviolet exposure and fade during the winter months",
      "That describes ephelides."]],
   c=0, cite=c(35)),

 dict(topic="Common acquired naevus", io=IOA,
   q="Which risk factors are named for common acquired melanocytic naevi?",
   opts=[
     ["Ultraviolet radiation exposure, male sex, and a genetic component, with more lesions in light skin tones that sunburn",
      "Correct — the number of lesions peaks in the thirties."],
     ["Ultraviolet radiation exposure, female sex, and a purely environmental cause, with more lesions in darker skin tones",
      "That reverses the sex and skin-type relationships."],
     ["Autoimmune disease, immunosuppression, and a family history of thyroid or coeliac disease",
      "Those associations belong to vitiligo and dermatitis herpetiformis."],
     ["Neurofibromatosis type I, somatic mutation, and involvement of the posterior midline of the trunk",
      "Those belong to congenital melanocytic naevi."]],
   c=0, cite=c(35)),

 dict(topic="Common acquired naevus", io=IOA,
   q="Describe the typical appearance of a common acquired melanocytic naevus, and which feature is suspicious.",
   opts=[
     ["Usually under 6 mm with homogenous surface and colour, round to oval and sharply demarcated; very dark brown or black on light skin is suspicious",
      "Correct — they can occur anywhere on the body."],
     ["Usually over 10 mm with heterogeneous surface and colour, irregular and poorly demarcated; a uniform tan colour is suspicious",
      "That inverts the typical appearance and the suspicious feature."],
     ["Usually under 1 cm, deeply blue-black and confined to the dorsal hands, scalp or sacral region; any pink colour is suspicious",
      "That describes blue naevus."],
     ["Usually several millimetres to centimetres, pink or red, hairless and dome-shaped; rapid growth is suspicious",
      "That describes Spitz naevus."]],
   c=0, cite=c(36)),

 dict(topic="Common acquired naevus", io=IOB,
   q="How is a common acquired melanocytic naevus diagnosed and managed?",
   opts=[
     ["Clinically, with observation, removal for cosmetic or symptomatic reasons, and counselling on sun protection",
      "Correct — no routine excision is required."],
     ["By biopsy in all cases, with excision required because of the risk of malignant transformation",
      "The diagnosis is clinical and the lesions are benign."],
     ["By Wood's lamp examination, with phototherapy for extensive involvement of the body surface",
      "That is the approach to vitiligo."],
     ["By dermoscopy in all cases, with cryotherapy applied to every lesion that has been identified",
      "Cryotherapy is not the described management."]],
   c=0, cite=c(37)),

 dict(topic="Blue naevus", io=IOA,
   q="What is a blue naevus composed of, and who is most affected?",
   opts=[
     ["Deeply pigmented spindle or epithelioid melanocytes in the dermis, affecting women more than men, most commonly in the twenties",
      "Correct — the group includes common, cellular, combined and atypical cellular blue lesions."],
     ["Junctional melanocytes at the dermoepidermal junction, affecting men more than women, most commonly in the fifties",
      "That is neither the depth nor the epidemiology described."],
     ["Neural-crest derived precursors migrating along neurovascular bundles, present at birth or shortly afterwards",
      "That describes congenital melanocytic naevi."],
     ["Hypertrophic melanocytes with increased basal melanin, affecting fair-skinned children of both sexes equally",
      "That describes ephelides."]],
   c=0, cite=c(38)),

 dict(topic="Blue naevus", io=IOA,
   q="How do common and cellular blue naevi differ?",
   opts=[
     ["Common blue naevi are deeply pigmented lesions under 1 cm arising in adolescence; cellular blue naevi are larger plaques or nodules over 1 cm arising before age forty",
      "Correct — both occur on dorsal hands and feet, scalp, buttocks or sacral region."],
     ["Common blue naevi are larger plaques over 1 cm arising before age forty; cellular blue naevi are small lesions under 1 cm arising in adolescence",
      "That reverses the two descriptions."],
     ["Common blue naevi occur on the palms and soles; cellular blue naevi occur on the trunk and the extremities only",
      "Both occur on the same sites and neither is confined to palms and soles."],
     ["Common blue naevi are present at birth; cellular blue naevi develop only after the fifth decade of life",
      "Neither timing matches what the lecture describes."]],
   c=0, cite=c(39)),

 dict(topic="Blue naevus", io=IOA,
   q="How is a blue naevus diagnosed and managed?",
   opts=[
     ["Clinically for small lesions and by biopsy for larger ones, with observation and biopsy or excision if changes are noted",
      "Correct — the lesions are blue, blue-grey or blue-black."],
     ["By biopsy in all cases with immediate wide excision, since the lesions are premalignant",
      "Small lesions are diagnosed clinically and the lesions are benign."],
     ["Clinically in all cases with cryotherapy for cosmetic removal if the patient prefers",
      "That is the cosmetic management of lentigines."],
     ["By dermoscopy in all cases, with topical depigmenting agents applied over the course of several months",
      "Those agents are used for ephelides."]],
   c=0, cite=c(40)),

 dict(topic="Pigmented spindle cell naevus", io=IOA,
   q="Describe pigmented spindle cell naevus, also called Reed naevus.",
   opts=[
     ["A sharply circumscribed darkly pigmented papule usually under 7 mm, jet-black with shades of blue, grey or brown, on the extremities and mainly the thigh",
      "Correct — commonest in the thirties, with females affected more than males, and it is benign."],
     ["A solitary pink or red hairless firm dome-shaped papule several millimetres to centimetres across, on face, neck, trunk or extremities",
      "That describes Spitz naevus."],
     ["A lesion at least 5 mm with irregular indistinct borders and variable tan to brown pigmentation on sun-exposed skin",
      "That describes dysplastic melanocytic naevus."],
     ["A deeply pigmented blue-black macule under 1 cm on the dorsal hands and feet, scalp, buttocks or sacral region",
      "That describes blue naevus."]],
   c=0, cite=c(41)),

 dict(topic="Pigmented spindle cell naevus", io=IOA,
   q="How is pigmented spindle cell naevus diagnosed and managed?",
   opts=[
     ["Confirmed by biopsy, with excision and negative margins as management",
      "Correct — the lesion is benign despite its jet-black appearance."],
     ["Diagnosed clinically, with observation and periodic evaluation as management",
      "That is the management of naevus spilus."],
     ["Diagnosed clinically, with cryotherapy for cosmetic removal if preferred",
      "That is the cosmetic management of lentigines."],
     ["Confirmed by biopsy, with topical depigmenting agents as management",
      "Those agents are used for ephelides."]],
   c=0, cite=c(41)),

 dict(topic="Spitz naevus", io=IOA,
   q="Describe a Spitz naevus and its distribution.",
   opts=[
     ["A solitary asymptomatic pink or red hairless firm dome-shaped lesion on face, neck, trunk or extremities, sparing palms, soles and mucous membranes",
      "Correct — it has a growth phase, fast or slow, followed by a stable period."],
     ["A solitary asymptomatic jet-black sharply circumscribed papule under 7 mm on the lower extremities, mainly the thigh",
      "That describes pigmented spindle cell naevus."],
     ["A tan background patch with scattered darker macules or papules on the trunk and extremities, present in the first years of life",
      "That describes naevus spilus."],
     ["Multiple smooth firm black papules 1 to 5 mm confined to the face and the neck, identical to small keratoses",
      "That describes dermatosis papulosa nigrans."]],
   c=0, cite=c(42)),

 dict(topic="Spitz naevus", io=IOA,
   q="Why does Spitz naevus require particular care, and what does the presence of multiple lesions suggest?",
   opts=[
     ["It sometimes resembles melanoma, and multiple lesions can be associated with a familial cancer syndrome",
      "Correct — diagnosis is by biopsy or wide excision, and management is by excision."],
     ["It always transforms into melanoma, and multiple lesions indicate that transformation has occurred",
      "The lesion is usually benign rather than always transforming."],
     ["It resembles a seborrheic keratosis, and multiple lesions suggest an internal malignancy",
      "That association belongs to acanthosis nigricans."],
     ["It resembles a blue naevus, and multiple lesions suggest neurocutaneous melanosis is present",
      "That association belongs to congenital melanocytic naevi of the head and midline."]],
   c=0, cite=c(42)),

 dict(topic="Dysplastic naevus", io=IOA,
   q="Describe the appearance of a dysplastic melanocytic naevus.",
   opts=[
     ["At least 5 mm in diameter with irregular indistinct borders and variable tan to brown pigmentation, with a smooth or pebbly surface",
      "Correct — they are common on sun-exposed skin and may progress to melanoma."],
     ["Under 6 mm in diameter with sharp demarcation and homogenous colour, round to oval in shape",
      "That describes a common acquired melanocytic naevus."],
     ["Under 1 cm in diameter, deeply pigmented blue to blue-black, on dorsal hands, scalp or sacrum",
      "That describes blue naevus."],
     ["Beige to black papules and plaques 2 to 20 mm that feel velvety and appear stuck onto the surface of the skin",
      "That describes seborrheic keratosis."]],
   c=0, cite=c(43)),

 dict(topic="Dysplastic naevus", io=IOA,
   q="Who is at risk of dysplastic melanocytic naevi, and what does dysplastic naevus syndrome look like?",
   opts=[
     ["Commonest in Caucasians with a family history; in the syndrome there can be over one hundred naevi by adolescence",
      "Correct — the higher the number of naevi, the higher the risk of melanoma."],
     ["Commonest in African Americans and dark-skinned Asians; in the syndrome the lesions are confined to the face and neck",
      "That epidemiology belongs to dermatosis papulosa nigrans."],
     ["Commonest in patients over fifty with cumulative sun damage; in the syndrome the lesions coalesce at sunburn sites",
      "That describes solar lentigo."],
     ["Commonest in women in their twenties; in the syndrome the lesions are deeply pigmented and sit within the dermis",
      "That describes blue naevus."]],
   c=0, cite=c(43)),

 dict(topic="Dysplastic naevus", io=IOA,
   q="How is dysplastic melanocytic naevus diagnosed and managed?",
   opts=[
     ["Diagnosis is by biopsy; management is observation, biopsy of all changing or developing lesions, excision where melanoma is a concern, and sun protection",
      "Correct — melanoma risk rises with the number of naevi present."],
     ["Diagnosis is clinical; management is observation alone with sun protection, since these lesions never progress to melanoma",
      "They may progress to melanoma and the diagnosis is by biopsy."],
     ["Diagnosis is clinical; management is cryotherapy or quality-switched laser for cosmetic removal",
      "That is the cosmetic management of lentigines."],
     ["Diagnosis is by Wood's lamp; management is phototherapy for extensive body surface involvement",
      "That is the approach to vitiligo."]],
   c=0, cite=c(44)),
]
