# -*- coding: utf-8 -*-
"""Rapid-drill bank: ear, nose and throat drugs (Lecture 5, ENT Jax Pharmacology.pptx, deck key ENT).

One fact, four names, no doses. One drug per choice; a class name is offered only when the
stem itself asks for a class (or a receptor type), and then every choice is one. Every wrong
choice is another real agent (or class) from the same family: other cephalosporins, other ear-drop
components, other antifungals, other analgesics, other antihistamines, other nasal steroids,
other cough and mucus agents ([[pharmacology_exam_spec]], Rapid Drills 2026-09-02).

Added 2026-10-03 (Jaxon: "separate the drill quiz by lecture also"). Exam 2 had no Lecture 5 drill.

Every item was checked against the slide text (tools/pharm_e2_lib.py dump L5) and, for picture-only
slides, tools/pharm_e2/ocr.json (slide 37, the antihistamine table; slide 28, the receptor table).

Left out on purpose:
  * every dose, regimen, duration range and maximum (Dr. Wood: no dosages);
  * slide 29's "endothelium-dependent nitric oxide release (increased cyclic AMP)": nitric oxide acts
    through cyclic GMP, so the deck is wrong there and it is not asked;
  * slide 59 calls guaifenesin a "mucolytic"; it is an expectorant, so the stems say expectorant;
  * slide 22 says ibuprofen "decreases the secretion of lithium": the truth is that it lowers the
    kidney's clearance of lithium, so lithium LEVELS RISE. Keyed on the truth (stem says "raises");
  * neomycin is never offered as a wrong choice for "avoid with a ruptured eardrum": the deck lists
    only polymyxin B, but neomycin is itself toxic to the cochlea, so it would be a defensible answer;
  * other NSAIDs are never offered where the fact is shared (reversible enzyme block, ulcers, asthma,
    lithium), and aspirin is never offered for facts that NSAIDs and aspirin share;
  * phenylephrine (slide 53 is a title only), cefixime as a wrong choice for the oral cephalosporin
    (it is also an oral third-generation agent), and "over-the-counter" status of nasal steroids
    (it has changed since the deck).
"""
ITEMS = [
# ---- antibiotics for ear, sinus and throat infections ----
dict(q="Which antibiotic is the MAINSTAY of acute otitis media therapy, given in a higher dose to overcome Streptococcus pneumoniae resistance?",
     ans="Amoxicillin", src=("ENT", 5),
     why="Amoxicillin is the mainstay for acute otitis media; the higher dose is what overcomes Streptococcus pneumoniae resistance.",
     wrong=[("Azithromycin", "Azithromycin is a penicillin-allergy alternative, and up to half of Streptococcus pneumoniae is resistant to macrolides."),
            ("Cefdinir", "Cefdinir is the penicillin-allergy and failed-therapy alternative, not the mainstay; amoxicillin is first line."),
            ("Ceftriaxone", "Ceftriaxone is an injection kept for failed therapy or intolerance of oral drugs, not the first-line mainstay.")]),

dict(q="Which ORAL antibiotic is used for SEVERE or RESISTANT otitis media, or when the child had antibiotics in the previous month?",
     ans="Amoxicillin-clavulanate", src=("ENT", 5),
     why="Amoxicillin-clavulanate is the step up for severe or resistant disease or recent antibiotic exposure.",
     wrong=[("Amoxicillin", "Plain amoxicillin is the first-line mainstay for otitis media; the step up for severe or resistant disease adds clavulanate."),
            ("Ampicillin-sulbactam", "Ampicillin-sulbactam is an injectable combination, not the oral step-up for severe otitis media, which is amoxicillin-clavulanate."),
            ("Piperacillin-tazobactam", "Piperacillin-tazobactam is a hospital intravenous combination, not the oral step-up for severe otitis media.")]),

dict(q="Which ORAL antibiotic is the STANDARD therapy for acute bacterial rhinosinusitis, because Haemophilus influenzae often makes beta-lactamase?",
     ans="Amoxicillin-clavulanate", src=("ENT", 7),
     why="Clavulanate protects the penicillin from beta-lactamase, which Haemophilus influenzae often produces in sinusitis.",
     wrong=[("Amoxicillin", "Plain amoxicillin is broken down by the beta-lactamase that Haemophilus influenzae often makes; clavulanate is what protects it."),
            ("Penicillin V potassium", "Penicillin V is also broken down by beta-lactamase and is too narrow for Haemophilus influenzae in sinusitis."),
            ("Dicloxacillin", "Dicloxacillin resists staphylococcal penicillinase but is narrow and does not cover Haemophilus influenzae.")]),

dict(q="Which fluoroquinolone is the single-drug alternative to clindamycin plus cefixime for sinusitis in a penicillin-allergic patient?",
     ans="Levofloxacin", src=("ENT", 7),
     why="Levofloxacin is the fluoroquinolone named as the alternative for penicillin-allergic sinusitis; it has good activity against Streptococcus pneumoniae.",
     wrong=[("Ciprofloxacin", "Ciprofloxacin has weak activity against Streptococcus pneumoniae; levofloxacin is the respiratory fluoroquinolone used for sinusitis."),
            ("Ofloxacin", "Ofloxacin is weaker against Streptococcus pneumoniae than levofloxacin, which is the respiratory fluoroquinolone used for sinusitis."),
            ("Azithromycin", "Azithromycin is a macrolide, not a fluoroquinolone, and Streptococcus pneumoniae is often resistant to macrolides.")]),

dict(q="Which cephalosporin is escalated to by injection when oral therapy for otitis media fails or is not tolerated?",
     ans="Ceftriaxone", src=("ENT", 6),
     why="Ceftriaxone is given by injection, either intramuscular or intravenous, for failed therapy or when oral drugs are not tolerated.",
     wrong=[("Cefdinir", "Cefdinir is an oral third-generation cephalosporin for failed therapy, not the injection used when oral drugs are not tolerated."),
            ("Cephalexin", "Cephalexin is an oral first-generation cephalosporin used for penicillin-allergic pharyngitis, not an injection for otitis media."),
            ("Cefixime", "Cefixime is an oral cephalosporin paired with clindamycin for penicillin-allergic sinusitis, not an injection for otitis media.")]),

dict(q="Which third-generation cephalosporin is the oral choice for otitis media in a penicillin-allergic patient or after failed therapy?",
     ans="Cefdinir", src=("ENT", 5),
     why="Cefdinir is the third-generation oral cephalosporin named for penicillin allergy and for failed therapy.",
     wrong=[("Cephalexin", "Cephalexin is a first-generation cephalosporin, used for penicillin-allergic pharyngitis rather than otitis media."),
            ("Ceftriaxone", "Ceftriaxone is a third-generation agent but an injection, kept for failure of oral therapy or intolerance of oral drugs."),
            ("Cefazolin", "Cefazolin is a first-generation intravenous cephalosporin, not a third-generation oral choice for otitis media.")]),

dict(q="Which antibiotic's use for otitis media is limited because up to half of Streptococcus pneumoniae resists its class?",
     ans="Azithromycin", src=("ENT", 5),
     why="Azithromycin is a macrolide, and up to 50 percent of Streptococcus pneumoniae resists macrolides, so it is a less reliable penicillin-allergy alternative.",
     wrong=[("Amoxicillin", "Amoxicillin is a penicillin, so the macrolide resistance does not apply; Streptococcus pneumoniae resistance to it is overcome with a higher dose."),
            ("Amoxicillin-clavulanate", "Amoxicillin-clavulanate is a penicillin combination, so macrolide resistance does not apply to it."),
            ("Ceftriaxone", "Ceftriaxone is a cephalosporin, so macrolide resistance does not apply to it.")]),

dict(q="Which penicillin can be given as a SINGLE INTRAMUSCULAR INJECTION for group A streptococcal pharyngitis?",
     ans="Benzathine penicillin G", src=("ENT", 8),
     why="Benzathine penicillin G is a single intramuscular injection that replaces the full oral course for group A strep pharyngitis.",
     wrong=[("Penicillin V potassium", "Penicillin V is taken by mouth for a full course; the single injection is benzathine penicillin G."),
            ("Ampicillin", "Ampicillin is an aminopenicillin given by mouth or intravenously over a course, not as a single long-acting injection."),
            ("Dicloxacillin", "Dicloxacillin is an oral penicillinase-resistant penicillin for staphylococci, not a single-injection strep regimen.")]),

dict(q="Which first-generation cephalosporin is a penicillin-allergy alternative for group A streptococcal pharyngitis?",
     ans="Cephalexin", src=("ENT", 8),
     why="Cephalexin is the narrow first-generation cephalosporin named for penicillin-allergic group A strep pharyngitis.",
     wrong=[("Cefdinir", "Cefdinir is a third-generation cephalosporin, broader than pharyngitis needs; the first-generation choice is cephalexin."),
            ("Ceftriaxone", "Ceftriaxone is a third-generation injection, broader than pharyngitis needs; the first-generation choice is cephalexin."),
            ("Cefixime", "Cefixime is a third-generation oral agent, broader than pharyngitis needs; the first-generation choice is cephalexin.")]),

dict(q="Which antibiotic is paired with cefixime for sinusitis in a penicillin-allergic patient?",
     ans="Clindamycin", src=("ENT", 7),
     why="Clindamycin plus cefixime is one of the penicillin-allergy regimens for sinusitis, and clindamycin is also a pharyngitis alternative.",
     wrong=[("Amoxicillin-clavulanate", "Amoxicillin-clavulanate is a penicillin, so it is the standard therapy for patients who are not penicillin-allergic."),
            ("Levofloxacin", "Levofloxacin is the alternative to the clindamycin and cefixime pair, so it is a separate regimen, not a partner."),
            ("Azithromycin", "Azithromycin is a macrolide for otitis media and pharyngitis; it is not paired with cefixime for sinusitis.")]),

dict(q="Which ear drop component is the classic cause of ALLERGIC CONTACT SENSITIVITY (hypersensitivity)?",
     ans="Neomycin", src=("ENT", 10),
     why="Neomycin, in the Cortisporin drops, carries a chance of hypersensitivity and is the classic cause of contact allergy in ear drops.",
     wrong=[("Ciprofloxacin", "Ciprofloxacin ear drops can carry an allergy warning, but they rarely sensitize the skin; neomycin is the classic cause of contact allergy."),
            ("Ofloxacin", "Ofloxacin ear drops can carry an allergy warning, but they rarely sensitize the skin; neomycin is the classic cause of contact allergy."),
            ("Polymyxin B", "Polymyxin B is listed for cochlear damage with a ruptured eardrum, and it sensitizes the skin far less often than neomycin.")]),

dict(q="Which ear drop is NOT recommended with a RUPTURED EARDRUM or tubes in place, because of cochlear damage and hearing loss?",
     ans="Neomycin/polymyxin B/hydrocortisone", src=("ENT", 10),
     why="The polymyxin B in these Cortisporin drops can reach the inner ear through a ruptured eardrum or tubes, causing cochlear damage and hearing loss.",
     wrong=[("Ciprofloxacin/dexamethasone", "Ciprofloxacin/dexamethasone (Ciprodex) is a fluoroquinolone and steroid drop with no polymyxin B, and it is used with tubes in place."),
            ("Ofloxacin", "Ofloxacin is a fluoroquinolone drop with no polymyxin B or neomycin, so it does not carry the cochlear warning."),
            ("Ciprofloxacin", "Ciprofloxacin is a fluoroquinolone drop with no polymyxin B or neomycin, so it does not carry the cochlear warning.")]),

dict(q="Which antifungal is a CYTOCHROME P450 3A4 INHIBITOR that prolongs the corrected QT interval?",
     ans="Ketoconazole", src=("ENT", 12),
     why="Ketoconazole inhibits cytochrome P450 3A4 and prolongs the corrected QT interval (QTc).",
     wrong=[("Nystatin", "Nystatin is a nonabsorbable antifungal whose side effects stay in the gut; it does not inhibit cytochrome P450 3A4."),
            ("Terbinafine", "Terbinafine is an allylamine that blocks squalene epoxidase, not an azole cytochrome P450 3A4 inhibitor."),
            ("Caspofungin", "Caspofungin is an intravenous echinocandin that blocks cell wall glucan synthesis; it is not a cytochrome P450 inhibitor.")]),

dict(q="Which antifungal can cause HEPATITIS, cirrhosis and hepatic failure along with high cholesterol and orthostatic hypotension?",
     ans="Ketoconazole", src=("ENT", 12),
     why="Ketoconazole's listed adverse effects include hepatitis, abnormal liver tests, cirrhosis, hepatic failure, hyperlipidemia and orthostatic hypotension.",
     wrong=[("Nystatin", "Nystatin is not absorbed, so its side effects are only diarrhea, nausea, stomach pain and vomiting."),
            ("Terbinafine", "Terbinafine can injure the liver, but it is not the azole that also causes hyperlipidemia and orthostatic hypotension."),
            ("Caspofungin", "Caspofungin is an intravenous echinocandin without that profile of cirrhosis, hyperlipidemia and orthostatic hypotension.")]),

dict(q="Which antifungal binds to sterols in the fungal cell membrane, raising its permeability?",
     ans="Nystatin", src=("ENT", 13),
     why="Nystatin, a nonabsorbable polyene, binds sterols in the fungal cell membrane and raises its permeability.",
     wrong=[("Ketoconazole", "Ketoconazole is an azole that blocks ergosterol synthesis by inhibiting a cytochrome P450 enzyme rather than binding membrane sterols."),
            ("Terbinafine", "Terbinafine is an allylamine that blocks squalene epoxidase, an enzyme in sterol synthesis, rather than binding membrane sterols."),
            ("Caspofungin", "Caspofungin is an echinocandin that blocks cell wall glucan synthesis rather than binding membrane sterols.")]),

dict(q="Which NONABSORBABLE antifungal treats ORAL CANDIDIASIS (thrush) in a patient on inhaled steroids, with human immunodeficiency virus infection or on chemotherapy?",
     ans="Nystatin", src=("ENT", 13),
     why="Nystatin oral suspension is a nonabsorbable antifungal for oral candidiasis, which is seen with inhaled steroids, human immunodeficiency virus (HIV) infection and chemotherapy.",
     wrong=[("Ketoconazole", "Ketoconazole is a systemic azole whose liver and corrected QT interval risks make it a poor choice for thrush."),
            ("Terbinafine", "Terbinafine is for nail and skin fungal infections, not for thrush."),
            ("Caspofungin", "Caspofungin is an intravenous drug for invasive fungal infection, not the nonabsorbable suspension for thrush.")]),

dict(q="Which antifungal causes only stomach upset (diarrhea, nausea, vomiting) because it is NOT ABSORBED?",
     ans="Nystatin", src=("ENT", 13),
     why="Nystatin is not absorbed, so its listed side effects are limited to diarrhea, nausea, stomach pain and vomiting.",
     wrong=[("Ketoconazole", "Ketoconazole is absorbed and causes liver injury, corrected QT interval prolongation and low blood pressure on standing."),
            ("Terbinafine", "Terbinafine is absorbed from the gut, so it can cause liver injury and taste change beyond stomach upset."),
            ("Caspofungin", "Caspofungin is given intravenously and can cause infusion reactions and liver test changes, not just stomach upset.")]),

dict(q="Which drug is an IRREVERSIBLE, noncompetitive inhibitor of platelets?",
     ans="Aspirin", src=("ENT", 15),
     why="Aspirin irreversibly inhibits platelets and does not select between cyclooxygenase 1 and 2.",
     wrong=[("Ibuprofen", "Ibuprofen reversibly inhibits cyclooxygenase 1 and 2, so its platelet effect wears off with the drug."),
            ("Naproxen", "Naproxen is a reversible cyclooxygenase inhibitor with a longer half-life, not an irreversible platelet inhibitor."),
            ("Acetaminophen", "Acetaminophen's mechanism is not fully elucidated and it has no meaningful antiplatelet action.")]),

dict(q="Which drug is linked to REYE SYNDROME in a child with a viral fever such as chickenpox or influenza?",
     ans="Aspirin", src=("ENT", 17),
     why="Aspirin in children with fever from a viral illness raises the incidence of Reye syndrome.",
     wrong=[("Ibuprofen", "Ibuprofen is a different nonsteroidal anti-inflammatory drug whose listed cautions are ulcers, kidney injury and asthma, not Reye syndrome."),
            ("Acetaminophen", "Acetaminophen is the usual fever reducer for a child with a viral illness; Reye syndrome follows aspirin."),
            ("Naproxen", "Naproxen is not the drug tied to Reye syndrome; that risk belongs to aspirin and the other salicylates.")]),

dict(q="Very low doses of which drug may benefit hypertensive disorders of pregnancy (preeclampsia)?",
     ans="Aspirin", src=("ENT", 17),
     why="Aspirin is avoided in pregnancy at ordinary doses, but very low doses may benefit preeclampsia.",
     wrong=[("Ibuprofen", "Ibuprofen has no antiplatelet low-dose role in preeclampsia; the exception belongs to aspirin."),
            ("Naproxen", "Naproxen has no low-dose benefit in preeclampsia; that exception belongs to aspirin."),
            ("Acetaminophen", "Acetaminophen has no antiplatelet action, so there is no low-dose preeclampsia role; that belongs to aspirin.")]),

dict(q="Which drug's toxicity causes hyperventilation with alkalosis, then fever, dehydration and metabolic acidosis, then shock and coma?",
     ans="Aspirin", src=("ENT", 16),
     why="Aspirin toxicity (salicylism) runs from hyperventilation and alkalosis to fever and metabolic acidosis, then shock and coma.",
     wrong=[("Ibuprofen", "Ibuprofen toxicity is mainly stomach ulcers and kidney injury, not the salicylism sequence of alkalosis then acidosis."),
            ("Naproxen", "Naproxen is not a salicylate, so it does not cause salicylism; its toxicity is the stomach and kidney effects of its class."),
            ("Acetaminophen", "Acetaminophen overdose damages the liver; the alkalosis-then-acidosis sequence is the toxic syndrome of aspirin.")]),

dict(q="Which drug should NOT be taken with anticoagulants, because it inhibits platelet function?",
     ans="Aspirin", src=("ENT", 20),
     why="Patients are told not to take aspirin with anticoagulants because aspirin inhibits platelet function.",
     wrong=[("Acetaminophen", "Acetaminophen does not inhibit platelet function, so it is the safer fever and pain choice in an anticoagulated patient."),
            ("Guaifenesin", "Guaifenesin is an expectorant with no antiplatelet effect and no anticoagulant warning."),
            ("Dextromethorphan", "Dextromethorphan is a cough suppressant whose caution is serotonin syndrome, not platelet inhibition.")]),

dict(q="Which drug raises LITHIUM and methotrexate levels and weakens angiotensin-converting enzyme (ACE) inhibitors?",
     ans="Ibuprofen", src=("ENT", 22),
     why="Ibuprofen cuts the kidney's clearance of lithium and methotrexate, so their levels rise, and it blunts angiotensin-converting enzyme inhibitors.",
     wrong=[("Acetaminophen", "Acetaminophen does not interfere with lithium, methotrexate or angiotensin-converting enzyme inhibitors; its caution is alcohol and liver damage."),
            ("Guaifenesin", "Guaifenesin does not change lithium or methotrexate clearance; its listed side effects are only nausea and vomiting."),
            ("Dextromethorphan", "Dextromethorphan interacts with serotonin-raising drugs and monoamine oxidase inhibitors, not with lithium or methotrexate clearance.")]),

dict(q="Which drug causes gastric or duodenal ULCERS, edema, fluid retention and acute renal failure?",
     ans="Ibuprofen", src=("ENT", 21),
     why="Ibuprofen's listed adverse effects are gastric or duodenal ulcers, perforation and bleeding, edema and fluid retention, and acute renal failure.",
     wrong=[("Acetaminophen", "Acetaminophen is very well tolerated at therapeutic doses, with no notable side effects of that kind."),
            ("Guaifenesin", "Guaifenesin's listed side effects are only nausea and vomiting."),
            ("Pseudoephedrine", "Pseudoephedrine's listed side effects are tachycardia, hypertension and headache, not ulcers or kidney failure.")]),

dict(q="Which over-the-counter pain reliever has a LONGER HALF-LIFE than ibuprofen, so it is taken less often?",
     ans="Naproxen", src=("ENT", 23),
     why="Naproxen (Aleve) has a longer half-life, so it is dosed less often than ibuprofen.",
     wrong=[("Acetaminophen", "Acetaminophen has a short half-life of about two hours, shorter than naproxen's, so it is taken more often."),
            ("Aspirin", "Aspirin's analgesic effect is short-lived, unlike naproxen's longer half-life, so it is taken more often."),
            ("Diclofenac", "Diclofenac has a short half-life of about two hours, so it is taken more often than naproxen.")]),

dict(q="Which analgesic and antipyretic has NO notable side effects at therapeutic doses?",
     ans="Acetaminophen", src=("ENT", 24),
     why="Acetaminophen is very well tolerated, with no notable side effects at therapeutic doses.",
     wrong=[("Ibuprofen", "Ibuprofen causes gastric ulcers, fluid retention and acute renal failure, so it has notable side effects."),
            ("Aspirin", "Aspirin causes bleeding, stomach upset and hypersensitivity, and it is linked to Reye syndrome in children."),
            ("Naproxen", "Naproxen is a nonsteroidal anti-inflammatory drug with the stomach, bleeding and kidney risks of the class.")]),

dict(q="Which drug raises the risk of LIVER DAMAGE (chronically) when combined with alcohol?",
     ans="Acetaminophen", src=("ENT", 25),
     why="Alcohol with acetaminophen increases the risk of liver damage, especially with chronic use.",
     wrong=[("Ibuprofen", "Ibuprofen's listed risks are ulcers, bleeding and kidney injury; the alcohol-linked liver damage belongs to acetaminophen."),
            ("Aspirin", "Aspirin's listed risks are bleeding, stomach upset and Reye syndrome; the alcohol-linked liver damage belongs to acetaminophen."),
            ("Naproxen", "Naproxen's risks are the stomach, bleeding and kidney effects of its class; the alcohol-linked liver damage belongs to acetaminophen.")]),

# ---- mucus agents and acetaminophen toxicity ----
dict(q="Which drug is traditionally used for ACETAMINOPHEN TOXICITY and, inhaled, splits the disulfide bonds in mucus?",
     ans="N-acetylcysteine", src=("ENT", 63),
     why="N-acetylcysteine treats acetaminophen toxicity and, nebulized, splits disulfide bonds that link mucoproteins.",
     wrong=[("Guaifenesin", "Guaifenesin is an oral expectorant that loosens mucus; it is not the acetaminophen toxicity drug."),
            ("Dornase alfa", "Dornase alfa is a DNA (deoxyribonucleic acid) enzyme that thins cystic fibrosis sputum; it does not treat acetaminophen toxicity."),
            ("Hypertonic saline", "Hypertonic saline draws water into the airway surface; it does not split disulfide bonds or treat acetaminophen toxicity.")]),

dict(q="Which inhaled mucus-thinning drug leaves a ROTTEN EGG smell because of its high sulfur content?",
     ans="N-acetylcysteine", src=("ENT", 63),
     why="Inhaled N-acetylcysteine smells of rotten eggs because of its sulfur content, and it can cause nausea, vomiting and bronchospasm.",
     wrong=[("Guaifenesin", "Guaifenesin is a plain oral expectorant whose listed side effects are only nausea and vomiting, with no sulfurous odor."),
            ("Dornase alfa", "Dornase alfa is a nebulized enzyme with no sulfurous odor, so it is not the rotten egg drug."),
            ("Hypertonic saline", "Hypertonic saline is salt water with no sulfur content, so it has no rotten egg smell.")]),

dict(q="Which nebulized drug is a DNA (deoxyribonucleic acid) enzyme that thins cystic fibrosis sputum?",
     ans="Dornase alfa", src=("ENT", 61),
     why="Dornase alfa cleaves DNA (deoxyribonucleic acid) released from degenerating neutrophils, which lowers the viscosity of cystic fibrosis sputum.",
     wrong=[("N-acetylcysteine", "N-acetylcysteine thins mucus by splitting disulfide bonds, not by cleaving DNA (deoxyribonucleic acid)."),
            ("Guaifenesin", "Guaifenesin is an oral expectorant, not a nebulized enzyme that cleaves DNA (deoxyribonucleic acid)."),
            ("Hypertonic saline", "Hypertonic saline hydrates the airway surface; it is not an enzyme and does not cleave DNA (deoxyribonucleic acid).")]),

dict(q="Which inhaled solution improves AIRWAY HYDRATION and mucociliary clearance?",
     ans="Hypertonic saline", src=("ENT", 62),
     why="Inhaled hypertonic saline improves mucus flow properties, airway hydration, mucociliary clearance and lung function.",
     wrong=[("Dornase alfa", "Dornase alfa works by cleaving DNA (deoxyribonucleic acid) in sputum rather than by hydrating the airway surface."),
            ("N-acetylcysteine", "N-acetylcysteine thins mucus by splitting disulfide bonds rather than by hydrating the airway surface."),
            ("Guaifenesin", "Guaifenesin is a swallowed expectorant, not an inhaled solution that hydrates the airway surface.")]),

# ---- antihistamines ----
dict(q="Which first-generation antihistamine is sold over the counter as a SLEEP AID?",
     ans="Doxylamine", src=("ENT", 32),
     why="Doxylamine is the first-generation antihistamine sold over the counter as a sleep aid, because sedation is the major side effect.",
     wrong=[("Cetirizine", "Cetirizine is a second-generation antihistamine with low sedation, so it is not used as a sleep aid."),
            ("Fexofenadine", "Fexofenadine is a second-generation antihistamine with very low sedation, so it is not a sleep aid."),
            ("Loratadine", "Loratadine is a second-generation antihistamine with very low sedation, so it is not a sleep aid.")]),

dict(q="Which first-generation antihistamine is rated HIGH for sedative, antiemetic and anticholinergic effects alike?",
     ans="Promethazine", src=("ENT", 37),
     why="Promethazine is the first-generation antihistamine rated high for sedative, antiemetic and anticholinergic effects, with the strongest antimuscarinic actions against motion sickness.",
     wrong=[("Chlorpheniramine", "Chlorpheniramine is rated medium for sedation and anticholinergic effect and has no antiemetic effect."),
            ("Meclizine", "Meclizine is rated high only for antiemetic effect, with medium sedative and anticholinergic effects."),
            ("Loratadine", "Loratadine is a second-generation agent rated very low for sedative and anticholinergic effects, with no antiemetic effect.")]),

dict(q="Which ORAL second-generation antihistamine is rated LOW, rather than very low, for sedation?",
     ans="Cetirizine", src=("ENT", 37),
     why="Cetirizine is rated low for sedation, while the other oral second-generation agents, fexofenadine and loratadine, are rated very low.",
     wrong=[("Fexofenadine", "Fexofenadine is rated very low for sedation, which is less than cetirizine's low rating."),
            ("Loratadine", "Loratadine is rated very low for sedation, which is less than cetirizine's low rating."),
            ("Chlorpheniramine", "Chlorpheniramine is a first-generation agent with a medium sedative effect, not a low one.")]),

dict(q="Which intranasal antihistamine causes a BITTER TASTE and nosebleeds?",
     ans="Azelastine", src=("ENT", 38),
     why="Azelastine (Astelin) is the intranasal histamine-1 (H1) antagonist whose side effects are a bitter taste and epistaxis.",
     wrong=[("Cetirizine", "Cetirizine is an oral second-generation antihistamine, not a nasal spray with a bitter taste."),
            ("Fexofenadine", "Fexofenadine is an oral second-generation antihistamine, not a nasal spray with a bitter taste."),
            ("Loratadine", "Loratadine is an oral second-generation antihistamine, not a nasal spray with a bitter taste.")]),

dict(q="Which histamine receptor type increases postcapillary permeability, mucus secretion and bronchoconstriction?",
     ans="Histamine-1 (H1) receptors", src=("ENT", 29),
     why="Histamine-1 (H1) receptors raise postcapillary permeability and mucus secretion and cause bronchoconstriction.",
     wrong=[("Histamine-2 (H2) receptors", "Histamine-2 (H2) receptors raise gastric acid secretion and the force of heart contraction and relax bronchial smooth muscle."),
            ("Histamine-3 (H3) receptors", "Histamine-3 (H3) receptors are presynaptic autoreceptors that reduce histamine release; they are not the allergy receptors."),
            ("Histamine-4 (H4) receptors", "Histamine-4 (H4) receptors work on immune cells, not on the vessels and airways that produce the allergic response.")]),

dict(q="Which histamine receptor type increases GASTRIC ACID secretion and the force of heart contraction?",
     ans="Histamine-2 (H2) receptors", src=("ENT", 30),
     why="Histamine-2 (H2) receptors raise gastric acid and pepsin secretion and the force of heart contraction.",
     wrong=[("Histamine-1 (H1) receptors", "Histamine-1 (H1) receptors raise permeability, mucus secretion and bronchoconstriction; they do not drive gastric acid."),
            ("Histamine-3 (H3) receptors", "Histamine-3 (H3) receptors are presynaptic autoreceptors that reduce histamine release, not gastric acid."),
            ("Histamine-4 (H4) receptors", "Histamine-4 (H4) receptors work on immune cells, not on gastric acid secretion.")]),

dict(q="Which class of drugs causes MAJOR SEDATION that is additive with alcohol?",
     ans="First-generation antihistamines", src=("ENT", 32),
     why="First-generation histamine-1 (H1) blockers cross into the central nervous system, so sedation is the major side effect.",
     wrong=[("Second-generation antihistamines", "Second-generation histamine-1 (H1) blockers hardly enter the central nervous system, so they cause much less sedation."),
            ("Nasal corticosteroids", "Nasal corticosteroids cause nosebleeds, septal perforation and an unpleasant taste, not sedation."),
            ("Oral decongestants", "Oral decongestants cause tachycardia, hypertension and headache rather than sedation.")]),

dict(q="Which class of drugs HARDLY enters the central nervous system, so it causes much LESS SEDATION?",
     ans="Second-generation antihistamines", src=("ENT", 32),
     why="Second-generation histamine-1 (H1) blockers largely stay out of the central nervous system, so they cause much less sedation.",
     wrong=[("First-generation antihistamines", "First-generation histamine-1 (H1) blockers cross into the central nervous system, so sedation is their major side effect."),
            ("Nasal corticosteroids", "Nasal corticosteroids are not antihistamines; they cause nosebleeds, septal perforation and an unpleasant taste."),
            ("Oral decongestants", "Oral decongestants are not antihistamines; they constrict nasal vessels and raise heart rate and blood pressure.")]),

dict(q="Which nasal corticosteroid is sold as FLONASE?",
     ans="Fluticasone", src=("ENT", 42),
     why="Fluticasone is sold as Flonase; Flovent is the inhaled asthma version, so the names must not be mixed up.",
     wrong=[("Mometasone", "Mometasone is sold as Nasonex, so it is not the nasal corticosteroid sold as Flonase."),
            ("Triamcinolone", "Triamcinolone is sold as Nasacort, so it is not the nasal corticosteroid sold as Flonase."),
            ("Beclomethasone", "Beclomethasone is sold as Beconase AQ, so it is not the nasal corticosteroid sold as Flonase.")]),

dict(q="Which nasal corticosteroid is sold as NASONEX?",
     ans="Mometasone", src=("ENT", 42),
     why="Mometasone is the nasal corticosteroid sold as Nasonex.",
     wrong=[("Flunisolide", "Flunisolide is sold as Nasalide, so it is not the nasal corticosteroid sold as Nasonex."),
            ("Budesonide", "Budesonide is sold as Rhinocort, so it is not the nasal corticosteroid sold as Nasonex."),
            ("Triamcinolone", "Triamcinolone is sold as Nasacort, so it is not the nasal corticosteroid sold as Nasonex.")]),

dict(q="Which nasal corticosteroid is sold as BECONASE AQ?",
     ans="Beclomethasone", src=("ENT", 42),
     why="Beclomethasone is the nasal corticosteroid sold as Beconase AQ.",
     wrong=[("Fluticasone", "Fluticasone is sold as Flonase, so it is not the nasal corticosteroid sold as Beconase AQ."),
            ("Budesonide", "Budesonide is sold as Rhinocort, so it is not the nasal corticosteroid sold as Beconase AQ."),
            ("Flunisolide", "Flunisolide is sold as Nasalide, so it is not the nasal corticosteroid sold as Beconase AQ.")]),

dict(q="Which class of drugs causes NOSEBLEEDS, septal perforation and an unpleasant taste?",
     ans="Nasal corticosteroids", src=("ENT", 43),
     why="Nasal corticosteroids mostly cause local effects: epistaxis, septal perforation and an unpleasant taste.",
     wrong=[("Oral decongestants", "Oral decongestants cause tachycardia, hypertension and headache, not local nasal damage."),
            ("Expectorants", "Expectorants such as guaifenesin cause only nausea and vomiting."),
            ("Antitussives", "Antitussives cause effects such as mouth numbness from chewing benzonatate or agitation from dextromethorphan, not nasal damage.")]),

dict(q="Prednisone is converted in the liver to which active glucocorticoid, sold as the oral liquid Orapred?",
     ans="Prednisolone", src=("ENT", 47),
     why="Prednisolone (Orapred) is the active form of prednisone and is the liquid formulation, while prednisone (Deltasone) is the tablet.",
     wrong=[("Dexamethasone", "Dexamethasone (Decadron) is a separate synthetic steroid, not the liver product of prednisone."),
            ("Methylprednisolone", "Methylprednisolone is a separate steroid; the active form of prednisone is prednisolone."),
            ("Hydrocortisone", "Hydrocortisone is the natural cortisol form, not the active form that prednisone becomes.")]),

dict(q="Which class causes hypokalemia, TENDON RUPTURE, cataracts and glaucoma?",
     ans="Systemic corticosteroids", src=("ENT", 47),
     why="Systemic steroids such as prednisone and dexamethasone cause low potassium, tendon rupture, cataracts, glaucoma and weakened immunity.",
     wrong=[("Nasal corticosteroids", "Nasal corticosteroids mostly cause local nosebleeds, septal perforation and an unpleasant taste at usual doses."),
            ("Oral decongestants", "Oral decongestants cause tachycardia, hypertension and headache rather than tendon rupture or cataracts."),
            ("Expectorants", "Expectorants such as guaifenesin cause only nausea and vomiting.")]),

dict(q="Which class of drugs carries the counseling to avoid LIVE VACCINES and exposure to chickenpox and measles?",
     ans="Systemic corticosteroids", src=("ENT", 48),
     why="A patient on a systemic steroid such as prednisone is immunocompromised at immunosuppressive doses, so live vaccines and exposure to chickenpox and measles are avoided.",
     wrong=[("Nasal corticosteroids", "Nasal corticosteroids act locally at usual doses and carry no live-vaccine counseling."),
            ("Oral decongestants", "Oral decongestants do not weaken immunity, so their counseling covers blood pressure and heart rate instead."),
            ("Antitussives", "Antitussives do not weaken immunity, so no live-vaccine counseling applies to them.")]),

dict(q="Which nasal spray causes REBOUND RHINITIS (rhinitis medicamentosa) if used for more than a few days?",
     ans="Oxymetazoline", src=("ENT", 50),
     why="Oxymetazoline (Afrin) causes rebound rhinitis (rhinitis medicamentosa) if used for more than 3 to 5 days.",
     wrong=[("Azelastine", "Azelastine is an antihistamine spray whose side effects are a bitter taste and nosebleeds, not rebound congestion."),
            ("Mometasone", "Mometasone is a nasal corticosteroid whose side effects are nosebleeds, septal perforation and an unpleasant taste."),
            ("Pseudoephedrine", "Pseudoephedrine is an oral tablet decongestant, not a nasal spray, and its side effects are tachycardia, hypertension and headache.")]),

dict(q="Which nasal spray interacts with MONOAMINE OXIDASE INHIBITORS and antidepressants?",
     ans="Oxymetazoline", src=("ENT", 51),
     why="Oxymetazoline's listed interactions are with monoamine oxidase inhibitors and antidepressants.",
     wrong=[("Azelastine", "Azelastine does not interact with monoamine oxidase inhibitors; its counseling covers spray technique and nosebleeds."),
            ("Mometasone", "Mometasone acts locally in the nose and does not interact with monoamine oxidase inhibitors."),
            ("Fluticasone", "Fluticasone acts locally in the nose; its interaction concern is strong cytochrome P450 3A4 inhibitors, not monoamine oxidase inhibitors.")]),

dict(q="Which drug can cause TACHYCARDIA, hypertension and headache, and weaken the effect of blood pressure medicines?",
     ans="Pseudoephedrine", src=("ENT", 52),
     why="Pseudoephedrine (Sudafed) is an oral sympathomimetic decongestant; it can cause tachycardia and hypertension and decreases the effect of antihypertensives.",
     wrong=[("Benzonatate", "Benzonatate is a cough suppressant that numbs stretch receptors; it has no effect on blood pressure medicines."),
            ("Guaifenesin", "Guaifenesin is an expectorant whose listed side effects are only nausea and vomiting, with no effect on blood pressure medicines."),
            ("Dextromethorphan", "Dextromethorphan is a cough suppressant whose interaction is serotonin syndrome, not blood pressure medicines.")]),

dict(q="Which antitussive ANESTHETIZES the stretch receptors in the lungs?",
     ans="Benzonatate", src=("ENT", 57),
     why="Benzonatate (Tessalon) anesthetizes the stretch receptors in the lungs to relieve a non-productive cough.",
     wrong=[("Dextromethorphan", "Dextromethorphan suppresses the cough center in the medulla instead of anesthetizing lung stretch receptors."),
            ("Guaifenesin", "Guaifenesin is an expectorant that loosens mucus rather than a drug that numbs lung stretch receptors."),
            ("N-acetylcysteine", "N-acetylcysteine thins mucus by splitting disulfide bonds; it does not numb lung stretch receptors.")]),

dict(q="Which cough drug is contraindicated with an allergy to TETRACAINE or related products?",
     ans="Benzonatate", src=("ENT", 57),
     why="Benzonatate is contraindicated in allergy to the product or related products such as tetracaine.",
     wrong=[("Dextromethorphan", "Dextromethorphan's contraindication is a monoamine oxidase inhibitor taken now or within two weeks, not tetracaine allergy."),
            ("Guaifenesin", "Guaifenesin's only listed contraindication is allergy to the product itself, not to tetracaine."),
            ("N-acetylcysteine", "N-acetylcysteine's concern is bronchospasm with the inhaled route, not tetracaine allergy.")]),

dict(q="Which antitussive numbs the mouth if its capsule is CHEWED?",
     ans="Benzonatate", src=("ENT", 57),
     why="Benzonatate is swallowed whole; chewing the capsule causes local anesthesia of the mouth.",
     wrong=[("Dextromethorphan", "Dextromethorphan's side effects are confusion, excitement and agitation, and chewing it does not numb the mouth."),
            ("Codeine", "Codeine is an opioid antitussive acting in the medulla; chewing it does not numb the mouth."),
            ("Guaifenesin", "Guaifenesin is an expectorant, not an antitussive, and chewing it does not numb the mouth.")]),

dict(q="Which antitussive is related to codeine and suppresses the cough center in the medulla through sigma receptor activation?",
     ans="Dextromethorphan", src=("ENT", 58),
     why="Dextromethorphan (Robitussin, Delsym) is related to codeine and suppresses the medullary cough center through sigma receptors.",
     wrong=[("Benzonatate", "Benzonatate acts peripherally by anesthetizing lung stretch receptors, not in the medulla."),
            ("Guaifenesin", "Guaifenesin is an expectorant that loosens mucus; it does not suppress the cough center."),
            ("Dornase alfa", "Dornase alfa is a nebulized enzyme that thins cystic fibrosis sputum; it does not act on the cough center.")]),

dict(q="Which cough drug is contraindicated within 2 weeks of taking a MONOAMINE OXIDASE INHIBITOR?",
     ans="Dextromethorphan", src=("ENT", 58),
     why="Dextromethorphan raises the risk of serotonin syndrome, so it is contraindicated during or within 2 weeks of a monoamine oxidase inhibitor.",
     wrong=[("Benzonatate", "Benzonatate's contraindication is allergy to the product or to related products such as tetracaine."),
            ("Guaifenesin", "Guaifenesin's only listed contraindication is allergy to the product."),
            ("N-acetylcysteine", "N-acetylcysteine's caution is bronchospasm with the inhaled route, not a monoamine oxidase inhibitor.")]),

dict(q="Which drug's counseling is to drink plenty of fluid and expect INCREASED DRAINAGE?",
     ans="Guaifenesin", src=("ENT", 60),
     why="Guaifenesin loosens mucus and decreases its viscosity, so patients drink plenty of fluid and expect more drainage.",
     wrong=[("Dextromethorphan", "Dextromethorphan suppresses cough rather than loosening mucus, so no increase in drainage is expected."),
            ("Benzonatate", "Benzonatate numbs lung stretch receptors rather than loosening mucus, so no increase in drainage is expected."),
            ("Dornase alfa", "Dornase alfa is a nebulized enzyme for cystic fibrosis sputum, not an oral drug counseled with fluids and drainage.")]),

]
