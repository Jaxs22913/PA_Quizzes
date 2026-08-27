# -*- coding: utf-8 -*-
"""Strengthen thin distractor refutations.

29 explanations said only what the option belongs to ("Permethrin is used for
scabies.") without saying why it fails for THIS patient. Every reference item
does both. These rewrites add the second half.
"""

EXPL = {
("l10",7,2): "These are general morphological terms rather than features of a pigmented lesion, and none of them describes asymmetry, border, colour, diameter, or evolution. A mnemonic built from them would not direct attention to any of the changes that identify a melanoma.",
("l4",41,3): "Those are the predisposing factors for acute paronychia, a localised infection of the soft tissue around a fingernail. None involves the deep fascial planes, and none appears among the trauma, burn, surgical, or immunosuppressive exposures that precede necrotizing fasciitis.",
("l6",19,4): "The lesions rather than the temperature define the infectious period, and a child may become afebrile while vesicles are still forming and shedding virus. Using fever as the endpoint would return a still-contagious child to school.",
("l6",32,3): "An annular plaque with an advancing scaly border and central clearing describes tinea corporis, a dermatophyte infection. Molluscum lesions are discrete dome-shaped papules with a central dimple rather than expanding rings.",
("l6",45,2): "Sacral involvement occurs but is not the leading distribution, and quoting it as the majority would misdirect where zoster is expected. Thoracic dermatomes account for about 55 percent and cranial for about 20 percent.",
("l7",10,2): "Those are the birth history factors associated with infantile hemangiomas, which are congenital vascular lesions of infancy. Pilonidal disease arises in young adults from hair and debris drawn into a natal cleft pit, so a neonatal history has no bearing on it.",
("l7",28,4): "Lipid-laden macrophages form xanthelasma, the soft yellow plaques of the medial eyelids that prompt screening for hyperlipidaemia. The contents here are mucin extruded from the adjacent joint, which is why this lesion is translucent rather than yellow.",
("l7",36,2): "Growth in proportion to the child describes café au lait macules, which are flat pigmented lesions rather than tumours. A plexiform neurofibroma is a soft tissue mass in the covering of a nerve and is not a pigmentary change at all.",
("l7",36,3): "Intertriginous freckling under 5 mm is Crowe's sign, another cutaneous marker of neurofibromatosis type 1. It is a pigmentary finding of the axillae and groin rather than a nerve sheath tumour, and it carries no risk of local invasion.",
("l7",36,4): "Plexiform neurofibromas occur anywhere except the brain and spinal cord, so this names the one location from which they are excluded. Confining them intracranially would also remove the local invasiveness that makes clinical evaluation necessary.",
("l7",39,3): "Excising benign lesions prophylactically causes scarring without benefit and does nothing about future ultraviolet exposure. The opportunity this visit creates is counselling, not surgery.",
("l8",5,4): "Scabies is an infestation of the stratum corneum with no described malignant potential. The complications actually to anticipate are staphylococcal superinfection, which may progress to sepsis, and persistent post-scabietic papules.",
("l8",7,3): "Burrows in the finger webs are the pathognomonic lesion of scabies, produced by a mite tunnelling through the stratum corneum. Body lice live in clothing and feed on the skin without burrowing, so they leave linear excoriations rather than tunnels.",
("l8",7,4): "Direct head-to-head contact is the primary route for head lice. Body lice are carried in the seams of clothing and bedding, which is why that infestation is associated with crowding and infrequent laundering rather than with close head contact.",
("l8",12,2): "Whole-body overnight permethrin is the treatment for scabies, where the target is a mite living within the stratum corneum across the entire skin surface. In tungiasis a single flea is embedded in the foot and must be physically removed.",
("l8",13,3): "Topical treatment cannot address a systemic reaction, and a cream applied to the sting site does nothing for bronchospasm or hypotension. This patient needs intramuscular or subcutaneous epinephrine immediately.",
("l8",15,3): "The delta-wing jet is a dermoscopic sign of the scabies mite sitting within its burrow. It is a magnified finding in an infestation rather than a bedside appearance of a bite, and it has no violaceous or blanched zones.",
("l8",15,4): "Crowe's sign is intertriginous freckling in neurofibromatosis type 1, a genetic condition unrelated to envenomation. It describes small pigmented macules of the axillae and groin rather than a necrotic lesion at a bite site.",
("l8",16,4): "That course describes a hobo spider bite, which is painless with induration and paraesthesia within 30 minutes and vesicles by 36 hours. A brown recluse bite is painful from the outset and evolves toward necrosis and eschar over days.",
("l8",18,3): "Crampy abdominal pain and muscle spasms follow black widow envenomation rather than a hobo spider bite, and the Southwest is not the region in question. Hobo spider bites are painless and produce local induration rather than systemic neurotoxicity.",
("l8",19,3): "A serpentine advancing track is cutaneous larva migrans, caused by animal hookworm larvae migrating through the skin after soil contact. Tarantula hairs embed where they land and provoke a local inflammatory or granulomatous response rather than migrating.",
("l8",20,3): "Tungiasis is flea penetration of the skin producing enlarging nodules on the feet after barefoot soil contact. It does not follow contact with a caterpillar and does not produce papules arranged in linear streaks.",
("l8",23,1): "Erythema migrans is the stage 1 early localised finding, appearing at the site of the tick bite within days to weeks. By the late persistent stage, months to years later, the skin lesion has long resolved and the disease has moved to the joints.",
("l8",25,2): "Erythema migrans and arthritis belong to Lyme disease, a different tick-borne infection. Substituting them here would point toward the wrong illness and away from the rash that begins on the ankles and wrists.",
("l8",25,3): "The second element of the triad is headache rather than cough, and the 60 percent figure attaches to the correct triad. Respiratory symptoms are not part of the classic presentation.",
("l8",25,4): "This omits fever, which presents first and is central to the illness, appearing in the first three days with the rash following 2 to 4 days later. The eruption is also not characteristically pruritic.",
("l8",28,2): "Permethrin is used for scabies, where a living mite must be killed within the skin. In cercarial dermatitis the human is not a viable host and the organism dies in the skin unaided, so what remains to treat is the inflammatory reaction.",
("l8",28,3): "Doxycycline treats rickettsial infection and is first line for Lyme disease. Cercarial dermatitis is caused by a flatworm larva rather than a bacterium, and there is no organism left to treat by the time the rash appears.",
("l9",14,3): "The depigmenting agents used are topical rather than systemic — hydroquinone, retinoids, alpha-hydroxy acids, and botanicals. Systemic depigmentation would act on the whole skin surface rather than on the freckles, which is neither available nor desirable.",
}
