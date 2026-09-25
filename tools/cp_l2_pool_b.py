# Clinical Pathophysiology I, Lecture 2 (Dermatology) — pool part B
# Objective c: pathophysiology of common secondary skin lesions, including the
# three phases of wound healing and how keloids depart from them.
#
# Mechanism only. No management.
SRC = "Pathophys Dermatology - Gopal 2026 SV.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOC = "c — Pathophysiology of secondary skin lesions"

POOL_B = [
 dict(topic="Secondary lesions", io=IOC,
   q="What defines a secondary skin lesion?",
   opts=[
     ["A modification or change of a primary lesion caused by infection, trauma or other factors",
      "Correct, which is why a secondary lesion may or may not still resemble what it came from."],
     ["Any lesion appearing on a second body site after the first",
      "Location is not the criterion; a secondary lesion is a primary lesion that has been modified or changed by infection, trauma or other factors."],
     ["Any lesion that is palpable rather than flat",
      "Palpability separates papules and nodules from flat macules within the primary group; a secondary lesion is a modified primary lesion."],
     ["Any lesion arising from malignant rather than benign disease",
      "Malignancy plays no part in the definition; a secondary lesion is a primary lesion modified by infection, trauma or other factors."]],
   c=0, cite=c(33)),

 dict(topic="Scale", io=IOC,
   q="What tissue makes up a scale?",
   opts=[
     ["A compact portion of desquamating stratum corneum, varying in size and thickness",
      "Correct. A scale is a compact portion of desquamating stratum corneum that varies in size and thickness, and psoriasis is an example."],
     ["Dried sebum, cellular debris, blood or necrotic skin",
      "Dried sebum, cellular debris, blood or necrotic skin form a crust, as in impetigo; a scale is desquamating stratum corneum."],
     ["Thickened epidermis induced by long-term scratching",
      "Epidermal thickening from long-term scratching is lichenification; a scale is a compact portion of desquamating stratum corneum."],
     ["Focal loss of epidermis and dermis with collagen destruction",
      "Focal loss of epidermis and dermis with collagen destruction is an ulcer; a scale is a compact portion of desquamating stratum corneum."]],
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
   q="Which description of lichenification is accurate?",
   opts=[
     ["Long-term scratching or rubbing of a pruritic area in an itch-scratch cycle, producing hyperplasia and hyperkeratosis with solid, firm, thick plaques without scaling",
      "Correct. The itch-scratch cycle drives hyperplasia and hyperkeratosis into firm, thick plaques without scaling, as in lichen simplex chronicus."],
     ["Loss of melanocytes across a circumscribed area",
      "Loss of melanocytes produces a hypopigmented macule such as vitiligo; lichenification is epidermal thickening from long-term scratching or rubbing."],
     ["Separation of epidermis from dermis with fluid accumulation",
      "Epidermis separating from dermis with fluid between them forms a bulla; lichenification is hyperplasia and hyperkeratosis from the itch-scratch cycle."],
     ["Slowing of keratinocyte division with elastin degradation",
      "Slowed keratinocyte division with elastin degradation is atrophy, which thins the skin; lichenification thickens it through hyperplasia."]],
   c=0, cite=c(33)),

 dict(topic="Erosion and ulcer", io=IOC,
   q="What is the tissue distinction between an erosion and an ulcer?",
   opts=[
     ["An erosion is focal loss of epidermis that does not penetrate below the dermal-epidermal junction; an ulcer is focal loss of epidermis AND dermis, with destruction of collagen and infiltration of inflammatory cells",
      "Correct. The junction is the boundary that separates them, and crossing it is what brings collagen destruction into play."],
     ["An erosion involves epidermis and dermis; an ulcer is limited to the epidermis",
      "This reverses the two: an erosion stops above the dermal-epidermal junction, while an ulcer loses epidermis and dermis with collagen destruction."],
     ["An erosion is fluid-filled and an ulcer is solid",
      "Neither lesion is fluid-filled; an erosion is superficial epidermal loss and an ulcer is loss of epidermis and dermis."],
     ["An erosion is a primary lesion and an ulcer is a secondary lesion",
      "Both erosion and ulcer are secondary lesions; they differ in depth, with an ulcer extending through the dermis and destroying collagen."]],
   c=0, cite=c(34)),

 dict(topic="Fissure", io=IOC,
   q="Which description of a fissure is accurate?",
   opts=[
     ["A linear ulcer forming a crack in the epidermis, from loss of elasticity or flexibility, severe dryness and mechanical tension, with hyperkeratosis thickening the stratum corneum",
      "Correct. A fissure is a linear ulcer cracking the epidermis where lost elasticity, severe dryness and mechanical tension act on a thickened stratum corneum."],
     ["A superficial loss of epidermis that spares the dermal-epidermal junction",
      "Superficial epidermal loss sparing the dermal-epidermal junction is an erosion; a fissure is a linear, crack-shaped ulcer in the epidermis."],
     ["A thickened plaque produced by chronic rubbing",
      "A thickened plaque from chronic rubbing is lichenification; a fissure is a linear crack in the epidermis from dryness, lost elasticity and mechanical tension."],
     ["A dilated superficial vessel without inflammatory infiltrate",
      "A dilated superficial vessel without infiltrate is telangiectasia; a fissure is a linear ulcer that cracks the epidermis under mechanical tension."]],
   c=0, cite=c(35)),

 dict(topic="Wound healing", io=IOC,
   q="Which description of the inflammatory phase of wound healing is accurate?",
   opts=[
     ["Days 1 to 3: a fibrin hemostatic plug forms, neutrophils and macrophages remove dead tissue, and growth factors and cytokines are secreted to signal the next phase",
      "Correct. The phase both cleans the wound and issues the signal that starts proliferation."],
     ["Days 4 to 21: granulation tissue forms from macrophages, fibroblasts and endothelial cells",
      "Granulation tissue forming over days 4 to 21 is the proliferative phase; the inflammatory phase, days 1 to 3, forms a fibrin plug and clears dead tissue."],
     ["Days 21 to one year: type III collagen is replaced by type I",
      "Replacement of type III collagen by type I is the remodeling phase, days 21 to one year; the inflammatory phase spans days 1 to 3."],
     ["Days 1 to 3: type I collagen is laid down in basket-weave orientation",
      "Collagen replacement happens in remodeling, days 21 to one year, when type I collagen lies in parallel bundles; days 1 to 3 bring the fibrin plug and clearance."]],
   c=0, cite=c(36)),

 dict(topic="Wound healing", io=IOC,
   q="Which description of the proliferative phase of wound healing is accurate?",
   opts=[
     ["Granulation tissue, comprised of macrophages, fibroblasts and endothelial cells, over days 4 to 21",
      "Correct. Over days 4 to 21, granulation tissue forms, comprised of macrophages, fibroblasts and endothelial cells, before remodeling begins."],
     ["A fibrin hemostatic plug, over days 1 to 3",
      "A fibrin hemostatic plug forms in the inflammatory phase, days 1 to 3; the proliferative phase, days 4 to 21, forms granulation tissue."],
     ["Type I collagen in parallel bundles, over days 21 to one year",
      "Type I collagen in parallel bundles belongs to remodeling, day 21 to one year; the proliferative phase forms granulation tissue."],
     ["Keratohyalin granules within the granular layer",
      "Keratohyalin granules belong to the normal stratum granulosum; the proliferative phase of wound healing forms granulation tissue over days 4 to 21."]],
   c=0, cite=c(36)),

 dict(topic="Wound healing", io=IOC,
   q="Which description of collagen in the remodeling phase of wound healing is accurate?",
   opts=[
     ["Type III collagen is replaced with stronger type I collagen oriented in small parallel bundles, whereas normal dermis has a basket-weave orientation",
      "Correct. In remodeling, from day 21 to one year, type III collagen gives way to stronger type I in small parallel bundles, unlike the basket-weave of normal dermis."],
     ["Type I collagen is replaced with type III in basket-weave orientation",
      "This reverses both: weaker type III is replaced by stronger type I, laid in parallel bundles rather than the basket-weave of normal dermis."],
     ["Collagen is degraded entirely and replaced by elastin",
      "Elastin does not replace collagen in a scar; remodeling swaps type III collagen for stronger type I collagen in parallel bundles."],
     ["Collagen production continues to increase indefinitely",
      "Production does not rise indefinitely: granulation tissue formation ceases in remodeling while type III collagen is replaced by type I."]],
   c=0, cite=c(36)),

 dict(topic="Wound healing", io=IOC,
   q="Which phase of wound healing is singled out as important, and what defines it?",
   opts=[
     ["The remodeling phase, days 21 to one year, in which formation of granulation tissue ceases",
      "Correct — remodeling determines the final scar, as type III collagen is replaced by type I and cross-linked, which is why strength keeps increasing for months without ever reaching that of normal dermis."],
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
     ["Fibroblast dysregulation prolongs the proliferative phase, collagen deposition and degradation become imbalanced during remodeling, and collagen bundles develop haphazardly and exceed the boundaries of the initial wound",
      "Correct. Two phases go wrong, and exceeding the original wound margin is the defining outcome."],
     ["Keratinocyte division slows and elastin degrades, thinning the tissue",
      "Slowed keratinocyte division and elastin degradation describe atrophy, which thins the skin; keloids come from a prolonged proliferative phase and excess collagen."],
     ["The inflammatory phase never resolves, so granulation tissue never forms at all",
      "Hypertrophic scars and keloids do progress through healing; fibroblast dysregulation prolongs the proliferative phase rather than preventing it."],
     ["Type I collagen is replaced by weaker type III in basket-weave orientation",
      "Remodeling normally replaces type III collagen with stronger type I; in keloids the defect is an imbalance of collagen deposition and degradation during remodeling."]],
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
      "Scale is desquamating stratum corneum, and these plaques have none; lichenification forms thick plaques without scaling."],
     ["Ulcer, from focal loss of epidermis and dermis",
      "An ulcer is loss of epidermis and dermis, but these plaques are thickened, not eroded; long-term scratching produces lichenification."],
     ["Atrophy, from slowed keratinocyte division",
      "Atrophy thins the skin through slowed division and collagen synthesis; thick leathery plaques after scratching reflect lichenification."]],
   c=0, cite=c(33)),

 dict(topic="Secondary lesions", io=IOC,
   q="Why does an ulcer scar while an erosion generally does not?",
   opts=[
     ["An ulcer destroys collagen in the dermis, so healing must lay down new collagen; an erosion spares the dermal-epidermal junction and the dermis beneath it",
      "Correct. Scarring is a dermal repair process, so a lesion confined above the junction has nothing to scar."],
     ["An ulcer is infected and an erosion is sterile",
      "Infection does not define either lesion; the difference is depth, since an ulcer destroys dermal collagen and an erosion stays above the junction."],
     ["An ulcer is larger, and size alone determines scarring",
      "Size is not the operative difference; depth is, because an ulcer loses dermis and its collagen while an erosion spares the dermal-epidermal junction."],
     ["An ulcer involves melanocyte loss which cannot be reversed",
      "Melanocyte loss causes hypopigmentation such as vitiligo; an ulcer is focal loss of epidermis and dermis with destruction of collagen."]],
   c=0, cite=c(34)),
]
