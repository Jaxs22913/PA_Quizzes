# -*- coding: utf-8 -*-
"""The pulmonary OSCE practice station's maneuver catalog (2026-11-06).

Every maneuver the Pulmonary OSCE run-sheet (tools/build_pd2_osce.py, PULM_EXAM) asks for, in its order
(general, inspection, palpation, percussion, auscultation, transmitted voice sounds, related), plus the heart,
which a respiratory encounter listens to when heart failure or a clot is on the differential. Each comes with
the finding shown when the patient is NORMAL there, worded from the Physical Diagnosis 2 thorax deck's normal
findings (resonant, symmetric fremitus, vesicular sounds, no adventitious sounds, trachea midline). A case
(tools/_osce_pulm_cases.py) overrides only what is abnormal for its condition. Other systems (abdomen,
neurologic, ...) are not listed: the patient model answers those as normal, in keeping with the case.

Percussion and auscultation are split by region, as the run-sheet grades them (posterior, lateral, anterior),
so a case can put its finding where the disease is and leave the other regions normal.

Each entry: id -> (name the student and the grader see, what the student would say to do it, normal finding).
"""

CATALOG = {
    # ------------------------------------------------------------------ general
    "position": ("Positions the patient",
                 "sits the patient up with the back exposed",
                 "The patient is sitting up on the edge of the exam table with the gown open at the back."),
    "general-survey": ("General survey",
                       "looks at the patient: distress, speaking in full sentences, audible wheeze, color",
                       "Alert and comfortable, in no respiratory distress. Speaks in full sentences. No audible "
                       "wheeze or stridor. Normal color."),
    # ------------------------------------------------------------------ inspection
    "thorax-inspect": ("Inspection of the thorax",
                       "looks at the shape and movement of the chest: symmetry, deformities, retractions, lag, "
                       "lesions, bruising",
                       "The chest is symmetric, with no deformities, lesions or bruising. Both sides rise together "
                       "with no lag, and there are no retractions."),
    "breathing-pattern": ("Respiratory rate, rhythm and effort",
                          "watches the rate, rhythm, depth and effort of breathing and the length of expiration",
                          "Breathing is quiet, regular and unlabored, with a normal depth and a normal expiratory "
                          "phase."),
    "accessory-muscles": ("Accessory muscle use",
                          "looks at the neck and abdominal muscles during breathing",
                          "No use of the sternocleidomastoid or scalene muscles on inspiration, and no "
                          "abdominal muscle use on expiration."),
    "lips-cyanosis": ("Lips and mouth for cyanosis",
                      "looks at the lips, tongue and inside of the mouth",
                      "Lips, tongue and oral mucosa are pink. No cyanosis."),
    "nails": ("Nail beds for cyanosis and clubbing",
              "inspects the fingernails and nail beds",
              "Nail beds are pink with no cyanosis. No clubbing: the normal angle at the nail base is kept, and "
              "the nail bed is firm."),
    "ap-diameter": ("Anterior-posterior diameter",
                    "compares the front-to-back depth of the chest with its width",
                    "The anterior-posterior diameter is normal, clearly smaller than the side-to-side width. No "
                    "barrel chest."),
    # ------------------------------------------------------------------ palpation
    "chest-wall-palp": ("Palpation of the chest wall",
                        "palpates the posterior, lateral and anterior chest wall for tenderness, deformity and "
                        "crepitus",
                        "No tenderness, deformity, masses or crepitus over the posterior, lateral or anterior "
                        "chest wall."),
    "expansion": ("Thoracic expansion",
                  "thumbs at the tenth ribs posteriorly, the patient breathes in deeply",
                  "Thoracic expansion is symmetric: both thumbs move apart equally with a deep breath."),
    "fremitus": ("Tactile fremitus",
                 "palpates while the patient says \"ninety-nine\", posteriorly, laterally and anteriorly, side to "
                 "side",
                 "Tactile fremitus is symmetric and normal posteriorly, laterally and anteriorly."),
    # ------------------------------------------------------------------ percussion
    "percuss-posterior": ("Percussion, posterior chest",
                          "percusses the back, alternating sides from the top down",
                          "Posterior chest: resonant and symmetric throughout."),
    "percuss-lateral": ("Percussion, lateral chest",
                        "percusses each side under the arms, alternating sides",
                        "Lateral chest: resonant and symmetric on both sides."),
    "percuss-anterior": ("Percussion, anterior chest",
                         "percusses the upper lobes and the front of the chest, alternating sides",
                         "Anterior chest: resonant and symmetric over both upper lobes."),
    "diaphragm-excursion": ("Diaphragmatic excursion",
                            "percusses the level of dullness on full expiration and on full inspiration, both "
                            "sides",
                            "Diaphragmatic excursion is about 4 centimeters on each side, with the diaphragm at "
                            "the same level on both sides."),
    # ------------------------------------------------------------------ auscultation
    "ausc-posterior": ("Auscultation, posterior chest",
                       "listens to the back in a ladder pattern, side to side, a full breath at each point",
                       "Posterior chest: vesicular breath sounds, equal on both sides. No crackles, wheezes, "
                       "rhonchi or pleural rub."),
    "ausc-lateral": ("Auscultation, lateral chest",
                     "listens under each arm in a ladder pattern, side to side",
                     "Lateral chest: vesicular breath sounds, equal on both sides. No crackles, wheezes, rhonchi "
                     "or pleural rub."),
    "ausc-anterior": ("Auscultation, anterior chest",
                      "listens to the upper lobes and the front of the chest in a ladder pattern, side to side",
                      "Anterior chest: vesicular breath sounds over both upper lobes, bronchovesicular near the "
                      "sternum. No crackles, wheezes, rhonchi or pleural rub."),
    # ------------------------------------------------------------------ transmitted voice sounds
    "egophony": ("Egophony",
                 "listens while the patient says \"ee\"",
                 "No egophony: \"ee\" sounds like a muffled \"ee\" over both lungs."),
    "bronchophony": ("Bronchophony",
                     "listens while the patient says \"ninety-nine\"",
                     "No bronchophony: \"ninety-nine\" is muffled and indistinct over both lungs."),
    "whispered-pectoriloquy": ("Whispered pectoriloquy",
                               "listens while the patient whispers \"ninety-nine\" or \"one-two-three\"",
                               "No whispered pectoriloquy: the whisper is faint and indistinct over both lungs."),
    # ------------------------------------------------------------------ related
    "trachea": ("Tracheal position",
                "inspects the front of the neck and palpates the trachea",
                "The trachea is midline."),
    "lymph-nodes": ("Cervical and supraclavicular lymph nodes",
                    "palpates the neck and above the collarbones for lymph nodes",
                    "No cervical or supraclavicular lymph nodes are palpable."),
    "legs": ("Lower extremities: edema and calves",
             "presses over the shins and ankles for pitting, looks at and feels both calves",
             "No pitting edema of the shins or ankles. Both calves are soft, nontender and equal in size."),
    "heart-ausc": ("Heart auscultation",
                   "listens over the aortic, pulmonic, tricuspid and mitral areas",
                   "Regular rhythm. Normal first and second heart sounds, with no murmur, rub or extra heart "
                   "sound."),
}
