# Clinical Pathophysiology I, Lecture 2 (Dermatology) — pool part B
# Objective c: pathophysiology of common secondary skin lesions, including the
# three phases of wound healing and how keloids depart from them.
#
# Mechanism only. No management.
SRC = "Pathophys Dermatology - Gopal 2026 SV.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOC = "Objective c — Pathophysiology of secondary skin lesions"

POOL_B = [
 dict(topic="Secondary lesions", io=IOC,
   q="What defines a secondary skin lesion?",
   opts=[
     ["A modification or change of a primary lesion caused by infection, trauma or other factors",
      "Correct, which is why a secondary lesion may or may not still resemble what it came from."],
     ["Any lesion appearing on a second body site after the first",
      "Location has nothing to do with the classification."],
     ["Any lesion that is palpable rather than flat",
      "Palpability separates macules from papules within the primary group."],
     ["Any lesion arising from malignant rather than benign disease",
      "Neither category implies anything about malignancy."]],
   c=0, cite=c(33)),

 dict(topic="Scale", io=IOC,
   q="What tissue makes up a scale?",
   opts=[
     ["A compact portion of desquamating stratum corneum, varying in size and thickness",
      "Correct, and psoriasis is the example given — which follows from its epidermal hyperplasia and loss of the granular layer."],
     ["Dried sebum, cellular debris, blood or necrotic skin",
      "That is a crust."],
     ["Thickened epidermis induced by long-term scratching",
      "That is lichenification."],
     ["Focal loss of epidermis and dermis with collagen destruction",
      "That is an ulcer."]],
   c=0, cite=c(33)),

 dict(topic="Crust", io=IOC,
   q="What is a crust formed from?",
   opts=[
     ["Dried sebum, cellular debris, blood or necrotic skin, forming a hard rough surface",
      "Correct, and impetigo is the example given."],
     ["Desquamating stratum corneum in compact portions",
      "That is a scale."],
     ["Fluid containing inflammatory cells beneath the epidermis",
      "That is a vesicle, and it is a primary lesion."],
     ["Purulent material of leukocytes and cellular debris",
      "That is a pustule, also a primary lesion."]],
   c=0, cite=c(33)),

 dict(topic="Lichenification", io=IOC,
   q="What produces lichenification, and what changes occur in the tissue?",
   opts=[
     ["Long-term scratching or rubbing of a pruritic area in an itch-scratch cycle, producing hyperplasia and hyperkeratosis with solid, firm, thick plaques without scaling",
      "Correct, and lichen simplex chronicus is the named condition."],
     ["Loss of melanocytes across a circumscribed area",
      "That produces a hypopigmented macule such as vitiligo."],
     ["Separation of epidermis from dermis with fluid accumulation",
      "That is a bulla."],
     ["Slowing of keratinocyte division with elastin degradation",
      "That is atrophy, which thins rather than thickens the skin."]],
   c=0, cite=c(33)),

 dict(topic="Erosion and ulcer", io=IOC,
   q="What is the tissue distinction between an erosion and an ulcer?",
   opts=[
     ["An erosion is focal loss of epidermis that does not penetrate below the dermal-epidermal junction; an ulcer is focal loss of epidermis AND dermis, with destruction of collagen and infiltration of inflammatory cells",
      "Correct. The junction is the boundary that separates them, and crossing it is what brings collagen destruction into play."],
     ["An erosion involves epidermis and dermis; an ulcer is limited to the epidermis",
      "This reverses the two."],
     ["An erosion is fluid-filled and an ulcer is solid",
      "Neither is a fluid-filled lesion."],
     ["An erosion is a primary lesion and an ulcer is a secondary lesion",
      "Both are secondary lesions."]],
   c=0, cite=c(34)),

 dict(topic="Fissure", io=IOC,
   q="What is a fissure, and what conditions produce one?",
   opts=[
     ["A linear ulcer forming a crack in the epidermis, from loss of elasticity or flexibility, severe dryness and mechanical tension, with hyperkeratosis thickening the stratum corneum",
      "Correct. It is a linear form of ulceration rather than a distinct process."],
     ["A superficial loss of epidermis that spares the dermal-epidermal junction",
      "That is an erosion, and it is not linear by definition."],
     ["A thickened plaque produced by chronic rubbing",
      "That is lichenification."],
     ["A dilated superficial vessel without inflammatory infiltrate",
      "That is telangiectasia."]],
   c=0, cite=c(35)),

 dict(topic="Wound healing", io=IOC,
   q="What happens during the inflammatory phase of wound healing, and over what period?",
   opts=[
     ["Days 1 to 3: a fibrin haemostatic plug forms, neutrophils and macrophages remove dead tissue, and growth factors and cytokines are secreted to signal the next phase",
      "Correct. The phase both cleans the wound and issues the signal that starts proliferation."],
     ["Days 4 to 21: granulation tissue forms from macrophages, fibroblasts and endothelial cells",
      "That is the proliferative phase."],
     ["Days 21 to one year: type III collagen is replaced by type I",
      "That is the remodelling phase."],
     ["Days 1 to 3: type I collagen is laid down in basket-weave orientation",
      "Collagen replacement belongs to remodelling, much later."]],
   c=0, cite=c(36)),

 dict(topic="Wound healing", io=IOC,
   q="What forms during the proliferative phase, and what is it made of?",
   opts=[
     ["Granulation tissue, comprised of macrophages, fibroblasts and endothelial cells, over days 4 to 21",
      "Correct. Those three cell types supply clearance, matrix and new vessels respectively."],
     ["A fibrin haemostatic plug, over days 1 to 3",
      "That is the inflammatory phase."],
     ["Type I collagen in parallel bundles, over days 21 to one year",
      "That is remodelling."],
     ["Keratohyalin granules within the granular layer",
      "That is normal epidermal maturation, not wound healing."]],
   c=0, cite=c(36)),

 dict(topic="Wound healing", io=IOC,
   q="What happens to collagen during the remodelling phase, and how does the result differ from normal dermis?",
   opts=[
     ["Type III collagen is replaced with stronger type I collagen oriented in small parallel bundles, whereas normal dermis has a basket-weave orientation",
      "Correct. The scar is strong but architecturally different, which is why it never quite matches the surrounding skin."],
     ["Type I collagen is replaced with type III in basket-weave orientation",
      "This reverses both the collagen types and the resulting orientation."],
     ["Collagen is degraded entirely and replaced by elastin",
      "Elastin is not the replacement fibre in scar remodelling."],
     ["Collagen production continues to increase indefinitely",
      "The lecture notes that formation of granulation tissue ceases in this phase."]],
   c=0, cite=c(36)),

 dict(topic="Wound healing", io=IOC,
   q="Which phase of wound healing does the lecture single out as important, and what defines it?",
   opts=[
     ["The remodelling phase, days 21 to one year, in which formation of granulation tissue ceases",
      "Correct — the slide marks this phase specifically, and its collagen swap is what determines the final scar."],
     ["The inflammatory phase, days 1 to 3, in which the fibrin plug forms",
      "That phase is described but is not the one singled out."],
     ["The proliferative phase, days 4 to 21, in which granulation tissue forms",
      "Also described, but not the phase flagged as important."],
     ["A fourth maturation phase beginning after one year",
      "Only three phases are described."]],
   c=0, cite=c(36)),

 dict(topic="Keloids", io=IOC,
   q="How do hypertrophic scars and keloids depart from normal healing?",
   opts=[
     ["Fibroblast dysregulation prolongs the proliferative phase, collagen deposition and degradation become imbalanced during remodelling, and collagen bundles develop haphazardly and exceed the boundaries of the initial wound",
      "Correct. Two phases go wrong, and exceeding the original wound margin is the defining outcome."],
     ["Keratinocyte division slows and elastin degrades, thinning the tissue",
      "That is atrophy, the opposite direction of change."],
     ["The inflammatory phase never resolves, so granulation tissue never forms at all",
      "The problem is a prolonged proliferative phase, not an absent one."],
     ["Type I collagen is replaced by weaker type III in basket-weave orientation",
      "That reverses the normal remodelling swap and is not the keloid mechanism."]],
   c=0, cite=c(38)),

 dict(topic="Atrophy", io=IOC,
   q="What three tissue changes produce atrophy of the skin?",
   opts=[
     ["Keratinocyte cellular division slows, collagen synthesis slows, and elastin degrades",
      "Correct — one epidermal change and two dermal ones, which together thin the skin."],
     ["Keratinocyte division accelerates, collagen accumulates, and elastin is deposited",
      "Those changes would thicken rather than thin the skin."],
     ["Melanocytes are lost and melanin production ceases",
      "That produces hypopigmentation, not thinning."],
     ["Mast cells degranulate and plasma leaks into the dermis",
      "That produces a wheal."]],
   c=0, cite=c(40)),

 dict(topic="Secondary lesions", io=IOC,
   q="A patient has thick, leathery plaques on the neck and forearms with no scaling, after months of scratching. Which secondary lesion is this, mechanistically?",
   opts=[
     ["Lichenification, from hyperplasia and hyperkeratosis driven by the itch-scratch cycle",
      "Correct. The absence of scaling is what separates it from psoriasis, whose plaques do scale."],
     ["Scale, from desquamating stratum corneum",
      "Scaling is specifically absent in the description given."],
     ["Ulcer, from focal loss of epidermis and dermis",
      "There is no tissue loss described here; the tissue is thickened."],
     ["Atrophy, from slowed keratinocyte division",
      "Atrophy thins the skin, and this description is of thickening."]],
   c=0, cite=c(33)),

 dict(topic="Secondary lesions", io=IOC,
   q="Why does an ulcer scar while an erosion generally does not?",
   opts=[
     ["An ulcer destroys collagen in the dermis, so healing must lay down new collagen; an erosion spares the dermal-epidermal junction and the dermis beneath it",
      "Correct. Scarring is a dermal repair process, so a lesion confined above the junction has nothing to scar."],
     ["An ulcer is infected and an erosion is sterile",
      "Infection is not what defines either lesion."],
     ["An ulcer is larger, and size alone determines scarring",
      "Depth rather than size is the operative difference."],
     ["An ulcer involves melanocyte loss which cannot be reversed",
      "Melanocyte loss produces hypopigmentation and is not the ulcer mechanism."]],
   c=0, cite=c(34)),
]
