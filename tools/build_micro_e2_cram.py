#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Microbiology Exam 2 cram sheet (Lectures 7 and 8 so far).

Condensed ONLY from the Exam 2 study guide (tools/_micro_e2_guide_l7.py and
_l8.py), which is itself built from the decks. Rows marked with a star carry
emphasis stated in the lecture recording; one row per lecture records what the
lecturer said NOT to memorize, because knowing what to skip is worth as much
the night before as any fact.

Split by objective group rather than slide range, the pattern of the Exam 1
sheet. Add a topic per later Exam 2 lecture as it lands.

    python3 tools/build_micro_e2_cram.py
"""
import io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

OUT = os.path.join(ROOT, "Microbiology Exam 2", "micro-exam-2-cram-sheet.html")
G7, G8 = "#1f4d2b", "#3f8a55"

topics = [
 {"id": "l7-scope", "label": "L7 · What the Lecturer Flagged", "color": G7, "rows": [
   ["★ Learn this table", "The four-hypersensitivity summary table (slide 9): “a chart you should pay attention to.”"],
   ["★ The one mechanism", "Desensitization works by raising allergen-specific immunoglobulin G that BLOCKS the allergen from the immunoglobulin E on mast cells."],
   ["★ No type I", "Type I plays NO part in graft rejection or in autoimmunity. Both use II, III and IV."],
   ["★ B cell vs T cell defect", "B cell defect (agammaglobulinemia) → recurrent BACTERIAL infections. T cell defect → fungal, viral, protozoan."],
   ["Not to memorize", "Helminth-allergen pairings (slide 6) · graft versus host grades (slide 50) · autoimmune disease charts (slides 58–60) · the order of the transformation sequence (slide 67). Oncogenic virus table (slide 68) deferred to the virus lectures."],
 ]},
 {"id": "l7-types", "label": "L7 · Immunopathologies & the Four Hypersensitivities", "color": G7, "rows": [
   ["Four immunopathologies", "OVER: allergy/hypersensitivity, autoimmunity (typically). UNDER: immunodeficiency, cancer (both a cause and an effect of immune dysfunction)."],
   ["Hypersensitivity", "Exaggerated, misdirected response to an allergen using the SAME mechanisms as protective immunity. I, II, III = B cell mediated; IV = T cell mediated."],
   ["Type I", "IMMEDIATE. Immunoglobulin E on mast cells, basophils, eosinophils is crosslinked → mediators. Hay fever, hives, anaphylactic shock."],
   ["Type II", "Immunoglobulin G/M against CELL SURFACE antigen → complement, lysis by membrane attack complex, phagocytosis. Transfusion reactions, Rh disease, autoimmune hemolytic anemia, myasthenia gravis."],
   ["Type III", "Immunoglobulin G/M against SOLUBLE antigen → immune complexes in basement membranes. Needs lots of antigen; delayed hours to days; joints, skin, kidney. Serum sickness, Arthus reaction, post-streptococcal glomerulonephritis, lupus, rheumatoid arthritis."],
   ["Type IV", "DELAYED, T cell mediated. Infectious allergy (tuberculosis, leprosy, syphilis, histoplasmosis, toxoplasmosis, candidiasis), tuberculin test, contact dermatitis, graft rejection."],
   ["Hygiene hypothesis", "Helminths give the allergic profile without allergy: nonspecific immunoglobulin E crowds Fc receptors and regulatory T cells suppress. Remove the worms and the immune system is underused and poorly regulated."],
   ["Asthma crosses types", "Acute = type I (bronchospasm, mucus). Chronic = TYPE IV (cytokines, eosinophil granules)."],
 ]},
 {"id": "l7-allergy", "label": "L7 · Type I in Detail, Diagnosis & Management", "color": G7, "rows": [
   ["Sensitizing vs provocative dose", "FIRST contact: immunoglobulin E made and parked on mast cells, no symptoms. LATER contact: allergen crosslinks it → degranulation. 10,000–40,000 immunoglobulin E per cell."],
   ["Skin", "Urticaria = skin mast cells + histamine. Angioedema = DEEPER mast cells. Eczema = PROLONGED response. Food urticaria: antigen carried to the skin in blood."],
   ["Anaphylaxis", "Cutaneous = wheal and flare (used in diagnosis). Systemic = fluid leaves blood → pressure falls → swelling → asphyxiation. 500–1000 deaths a year in the United States."],
   ["Epinephrine (5 actions)", "Reseals endothelial tight junctions · relaxes bronchi · reduces airway mucosal edema · stimulates heart · suppresses histamine release."],
   ["Late phase", "About 6 HOURS after the immediate reaction; synthesized mediators such as leukotrienes; eosinophils; tissue more sensitive next time."],
   ["Diagnosis", "Allergy or infection? Skin prick/intradermal (wheal and flare) · blood: specific immunoglobulin E, basophils · supervised food challenge · PATCH test = contact dermatitis (type IV)."],
   ["Drugs", "Corticosteroids ↓ immunoglobulin E via lymphocytes · cromolyn blocks degranulation · montelukast blocks leukotriene synthesis · omalizumab = anti-immunoglobulin E antibody · antihistamines block receptors."],
   ["Desensitization", "Subcutaneous immunotherapy most common; ~80% improve. Also regulatory T cells. Sublingual: under the tongue; peanut dose 1/75 of a kernel."],
 ]},
 {"id": "l7-transfusion", "label": "L7 · Transfusion Reactions & Rh", "color": G7, "rows": [
   ["Why ABO", "Red cells carry NO major histocompatibility complex molecules. You make antibody against the ABO antigens you LACK."],
   ["Cross-match", "RECIPIENT serum against DONOR red cells — never the reverse (too little donor antibody to react)."],
   ["Consequences", "Complement lysis → blocked glomeruli, fever, jaundice; coated cells also cleared by natural killer cells and macrophages."],
   ["Rh disease", "Rh-negative mother, Rh-positive fetus. First pregnancy sensitizes; later ones hemolytic (erythroblastosis fetalis)."],
   ["Rhogam timing", "Passive anti-Rh antibody prevents sensitization. 26–28 WEEKS · within 72 HOURS of birth · after invasive tests, abdominal injury, accidental exposure."],
 ]},
 {"id": "l7-transplant", "label": "L7 · Transplantation & Histocompatibility", "color": G7, "rows": [
   ["Graft types", "Autograft = self · isograft = identical twin · allograft = same species · xenograft = other species."],
   ["★ Rejection by type", "Hyperacute = II (preexisting antibody; engorged, purple graft) · acute = IV (T cells vs human leukocyte antigen differences) · chronic = III (thickened vessel walls) · graft versus host = IV."],
   ["Chronic rejection", "Months to years; fails MORE THAN HALF of kidney and heart transplants after 10+ years."],
   ["Acute rejection route", "Graft dendritic cells → SPLEEN → activate effector T cells → back via blood → graft destroyed."],
   ["Cornea", "First organ transplanted; succeeds WITHOUT a human leukocyte antigen match — eye downregulates T cells, macrophages, neutrophils, complement."],
   ["Liver", "Human leukocyte antigens NOT assessed; ABO IS. Hepatocytes: little class I, no class II."],
   ["Bone marrow", "MOST sensitive to mismatch → graft versus host disease (skin, muscle, liver, gut) in ~30%."],
   ["Preventing rejection", "Tissue typing, mixed lymphocyte reaction; purine analogs, corticosteroids, tacrolimus, cyclosporine, rapamycin (sirolimus)."],
 ]},
 {"id": "l7-auto-deficiency", "label": "L7 · Autoimmunity & Immunodeficiency", "color": G7, "rows": [
   ["Autoimmunity", "Lost tolerance → autoantibodies and sensitized T cells. All types EXCEPT I. Runs in families; WOMEN more often."],
   ["Sequestered antigen", "Privileged tissue (central nervous system, lens, thyroid, testes) damaged later releases unseen antigen. One injured eye → T cells attack BOTH."],
   ["Molecular mimicry", "Rheumatic fever (strep → heart) · Lyme arthritis (Borrelia) · reactive arthritis (Shigella, Salmonella, Campylobacter) · type 1 diabetes (coxsackie A/B, echovirus, rubella)."],
   ["Thymic senescence", "Thymus involutes to fat; premature aging in young people with autoimmunity; less output → infection, cancer, autoimmunity."],
   ["Slide 61 diseases", "Graves' (stimulates follicle cells → hyper) · Hashimoto's (destroys them → hypo) · myasthenia gravis (acetylcholine receptors) · multiple sclerosis (myelin; T cells + antibody; Epstein-Barr link)."],
   ["Primary vs secondary", "PRIMARY = congenital, genetic. SECONDARY = acquired after birth: human immunodeficiency virus (T helper cells), chemotherapy, radiation, blood cell cancers."],
   ["Primary examples", "Agammaglobulinemia (B, no antibody) · DiGeorge (T, no thymus) · severe combined immunodeficiency (both limbs, no adaptive response) · complement, phagocyte defects."],
 ]},
 {"id": "l7-cancer", "label": "L7 · Carcinogenesis & Immunotherapy", "color": G7, "rows": [
   ["Transformation", "ONE cell with MULTIPLE accumulated mutations; oncogenes activated by radiation, chemicals, oncogenic viruses. Benign = contained; malignant = spreads."],
   ["Cancer cell traits", "Self-stimulating · ignore stop signals · no apoptosis · angiogenesis · metastasis · constant replication · evade immunity."],
   ["Tumor antigens", "SPECIFIC = tumor only. ASSOCIATED = tumor + normal cells (less)."],
   ["Evasion", "Shed the natural killer stress ligand · secrete transforming growth factor beta → regulatory T cells (+ interleukin 10). More regulatory T cells = WORSE prognosis."],
   ["Checkpoint inhibitors", "Block the T cell OFF signal; do not kill directly. Melanoma, some lung cancers."],
   ["Adoptive cell therapy", "Patient's cells engineered and returned. CAR-T (chimeric antigen receptor T cells) APPROVED for blood cancers; tumor infiltrating lymphocytes in development; chimeric antigen receptor natural killer cells in trials."],
   ["Antibodies & cytokines", "100+ monoclonal antibodies, diagnosis AND therapy; conjugates carry drug or radionuclide. Interleukin 2 → T and natural killer cells (kidney, melanoma). Interferon alpha → natural killer and dendritic cells. Erythropoietin = red cells; interleukin 11 = platelets."],
   ["Coley · viruses · vaccines", "Coley's toxins (1890s; killed strep + Serratia; displaced by radiation and chemotherapy). Oncolytic viruses replicate only in tumor cells; mumps natural. Prophylactic: hepatitis B, papillomavirus. Therapeutic: bacillus Calmette-Guérin (bladder), sipuleucel-T (prostate)."],
 ]},
 {"id": "l8-categories", "label": "L8 · Diagnosing Infections: The Three Categories", "color": G8, "rows": [
   ["Scope note", "The objectives are the course-wide list; the lecture teaches diagnostic METHODS. Sort every technique into one of three."],
   ["Phenotypic", "Observable traits (phenotype = physical expression of genes): morphology, biochemistry, chemistry, drug sensitivity. Needs culture → SLOWER."],
   ["Genotypic", "Genetic makeup; NO culture needed — slow Mycobacterium, hard Legionella. Faster diagnosis → timely treatment."],
   ["Immunological", "Antigen-antibody specificity; culture optional. Rapid strep 10–15 minutes, but you need a hypothesis first."],
   ["Specimens", "ALL potentially infectious. Results depend on collection, handling, transport, storage. Universal precautions MITIGATE, not eliminate."],
   ["Results", "Direct tests or culture-isolation-identification; results PRESUMPTIVE or CONFIRMATORY."],
 ]},
 {"id": "l8-phenotypic", "label": "L8 · Phenotypic Methods & Sensitivity Testing", "color": G8, "rows": [
   ["Morphology", "Microscopic: shape, size, stain (Gram, flagellar, acid-fast), structures. Macroscopic: colony texture, size, shape, pigment."],
   ["Biochemical", "Presence or absence of enzymes/pathways: fermentation, amino acids, hydrolysis, catalase, oxidase, coagulase, hemolysins."],
   ["★ Blood agar", "Detects HEMOLYSIS — the lecturer's “take-home message”, especially for pathogenic Gram-positives."],
   ["Other media", "Chocolate agar: “mainly anaerobic culturing” (slide's wording) · mannitol salts: selects salt tolerance, differentiates mannitol · citrate: blue = pH up · urea: hot pink = urease."],
   ["Normal flora?", "Is the recovered organism the cause, or normal flora? Koch's postulates reasoning."],
   ["Kirby-Bauer", "Disk diffusion: WHICH drug and at WHAT dose; LARGER zone = more effective. Minimum inhibitory concentration strips give the concentration."],
 ]},
 {"id": "l8-genotypic-immuno", "label": "L8 · Genotypic & Immunological Methods", "color": G8, "rows": [
   ["Polymerase chain reaction", "Thermal cycler amplifies nucleic acid; Kary Mullis. Guanine + cytosine content = taxonomy, not specific identification."],
   ["Ribosomal ribonucleic acid", "16S for bacteria, 18S for eukaryotes → phylogenetic trees. Restriction fragment length polymorphism = “fingerprinting.”"],
   ["Serology", "In vitro testing of serum; titer in binding antibody units. Serotyping = known antibody identifies an unknown microbe."],
   ["Agglutination vs precipitation", "Agglutination = WHOLE-CELL/insoluble antigen, clumps, MORE sensitive (blood typing, syphilis, Weil-Felix, pregnancy, rapid strep). Precipitation = SOLUBLE antigen, needs gel/liquid (Ouchterlony, immunoelectrophoresis → antibody class)."],
   ["Blots", "Southern = deoxyribonucleic acid (the man's name) · Northern = ribonucleic acid · WESTERN = PROTEIN, second test for human immunodeficiency virus · Eastern = other epitopes."],
   ["Complement fixation", "4 parts: antigen, antibody, complement, sheep red cells. NO hemolysis = POSITIVE. Hemolysis = negative."],
   ["Fluorescent · immunoassay · in vivo", "Dye-labeled monoclonal antibody, direct or indirect. Immunoassays detect TRACE amounts (radioimmunoassay; enzyme-linked immunosorbent assay, 96-well). In vivo: tuberculin, allergy tests."],
   ["Viruses", "Not cells; need a host cell → labor intensive to culture; rapid antigen-antibody tests."],
 ]},
]

html = render(
    title="Cram Sheet — Microbiology Exam 2",
    kicker="Microbiology · Exam 2 · Class of 2028",
    h1="Microbiology Exam 2 Cram Sheet",
    sub="Lectures 7 and 8 so far — Disorders in Immunity and Diagnosing Infections. ★ = emphasized in the lecture recording. Exam 2 (Lectures 7–13) is Friday 23 October 2026.",
    topics=topics,
    guide_href="micro-exam-2-study-guide.html",
    footer_note="Condensed from the Microbiology Exam 2 Study Guide (Class of 2028). For the full explanation and figures behind any of these, see the full guide.",
)
io.open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB, %d topics, %d rows)" % (os.path.relpath(OUT, ROOT), len(html) // 1024,
      len(topics), sum(len(t["rows"]) for t in topics)))
