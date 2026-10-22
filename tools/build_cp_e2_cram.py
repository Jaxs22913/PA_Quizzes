#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Clinical Pathophysiology I Exam 2 cram sheet (Lectures 6 to 9 so far).

Condensed ONLY from cp-exam-2-study-guide.html (cram_sheets_feature): nothing
here that the guide does not say, numbers kept verbatim. Rendered with the
shared tools/cram-sheet-template/render.py, never hand-edited. Lecture 10
appends as further topics when its guide section exists.

Mechanism only (clin_path_exam_spec) -- asserted. The one Lecture 7 row marked
with a star is the one thing the presenter said "do know".
"""
import html, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

OUT = os.path.join(ROOT, "Clinical Pathophysiology I Exam 2", "cp-exam-2-cram-sheet.html")

T = [
 {"id": "l6-chd", "label": "L6 · Coronary Heart Disease & Ischemia", "color": "#6e1f2f", "rows": [
  ("Coronary heart disease", "Insufficient delivery of oxygenated blood to the myocardium because of ATHEROSCLEROTIC coronary arteries. About 50% of cardiovascular deaths. Also called ischemic heart disease, coronary artery disease."),
  ("Ischemia = supply vs demand", "Begins when oxygen SUPPLY < DEMAND → less ATP (adenosine triphosphate). Causes abnormal function AND abnormal rhythms; prolonged → irreversible damage."),
  ("Supply falls", "Large plaques · acute platelet aggregation then thrombosis · VASOSPASM · abnormal microcirculation · poor perfusion pressure."),
  ("Demand rises", "Workload = HEART RATE · PRELOAD · AFTERLOAD · CONTRACTILITY. Raise any one → more oxygen demand."),
  ("Etiologies", "ATHEROSCLEROSIS behind almost all → predisposes to thrombosis, vasospasm, endothelial dysfunction. Microcirculation: small-vessel endothelium regulates flow abnormally. Uncommon: low blood oxygen content (respiratory); poor perfusion (hypotension, hypovolemia)."),
  ("Major risk factors", "Age · family history · abnormal lipids · smoking · hypertension · diabetes mellitus · obesity."),
  ("Probable risk factors", "Male sex · HOMOCYSTEINE · high-sensitivity C-reactive protein."),
  ("Collateral circulation", "Develops when plaque builds over YEARS — why slow occlusion is tolerated better than sudden."),
  ("Flow tracks demand", "Myocardial oxygen consumption and blood flow correspond NEARLY LINEARLY; METABOLIC SIGNALS are the principal determinants of delivery."),
  ("Coronary anatomy", "LEFT MAIN → left anterior descending (anterior interventricular) + CIRCUMFLEX. RIGHT CORONARY → marginal + posterior interventricular."),
  ("Frank–Starling", "More diastolic filling → more ejected. Force ∝ initial sarcomere length (preload). Maximal force at 2.6 micrometers, rarely exceeded in the normal heart."),
 ]},
 {"id": "l6-plaque", "label": "L6 · Lipoproteins, Atherosclerosis & Plaque", "color": "#8a5a14", "rows": [
  ("Low-density lipoprotein", "Cholesterol-rich → HIGHEST risk."),
  ("Very-low-density lipoprotein", "Triglyceride-rich → INCREASES risk."),
  ("High-density lipoprotein", "DECREASES risk — carries cholesterol BACK TO THE LIVER, away from plaque."),
  ("Familial hypercholesterolemia", "Common single-gene hyperlipidemia (classically taught as the most common). Defective LOW-DENSITY LIPOPROTEIN RECEPTOR on liver cells → liver cannot clear cholesterol."),
  ("Homocysteine", "Amino acid from METHIONINE → CYSTEINE. Atherogenic + prothrombotic: intimal thickening, elastic lamina disruption, smooth muscle hypertrophy, platelet accumulation, platelet-rich occlusive thrombus."),
  ("Plaque sequence", "ENDOTHELIAL INJURY (wall stress, toxins, inflammation, hyperlipidemia) → permeable endothelium, leukocytes recruited → low-density lipoprotein leaks in and is OXIDIZED → FOAM CELLS → mediators + growth factor → smooth muscle proliferation → LIPID CORE → collagen/fibrin CAP."),
  ("75%", "Occlusion at which blood flow is COMPROMISED."),
  ("Vulnerable plaque (slide 24, image only)", "LARGE lipid core · THIN fibrous cap · rich in MACROPHAGES · increased MMPs (matrix metalloproteinases) · POOR in smooth muscle · LOW-GRADE stenosis."),
  ("Stable vs vulnerable", "Stable: thick cap, small core, many smooth muscle cells. Vulnerable: thin cap, large core, many macrophages. Smooth muscle BUILDS the cap; macrophages DIGEST it."),
  ("Why plaques rupture", "Composition + mechanical stress. Trigger: SHEAR from high-velocity flow through a severe stenosis. VASA VASORUM capillaries hemorrhage → pressure builds inside the plaque."),
  ("Rupture consequences", "Exposed subendothelial proteins → platelet aggregation → THROMBUS; EMBOLI block smaller vessels downstream."),
 ]},
 {"id": "l6-acs", "label": "L6 · Angina & Acute Coronary Syndrome", "color": "#a23a4c", "rows": [
  ("Coronary syndromes", "CHRONIC: stable angina, ischemic cardiomyopathy. ACUTE: unstable angina, myocardial infarction. Classified by severity and onset."),
  ("Angina pectoris", "Intermittent ischemia NOT enough to kill cells; when demand rises; may cause pulmonary congestion."),
  ("Stable (typical)", "MOST COMMON. Fixed stenosis → ischemia only under increased WORKLOAD."),
  ("Prinzmetal (variant)", "VASOSPASM (cause unknown). Unpredictable; typically at REST, not with exertion."),
  ("Unstable (crescendo)", "May progress to acute ischemia → counted with the ACUTE coronary syndromes."),
  ("Acute coronary syndrome", "Unstable angina + myocardial infarction (hard to tell apart clinically). Pain longer than typical angina; PLAQUE RUPTURE + ACUTE THROMBOSIS."),
  ("Infarction mechanism", "Prolonged/total loss of flow → NECROSIS or APOPTOSIS. Thrombus on a cracked plaque → platelet plug → clotting cascade → occlusion. Outcome depends on COLLATERALS, WORKLOAD, TIME."),
  ("Occlusion timeline", "Immediately: ATP depleted. Few minutes: cannot contract. AFTER 30 MINUTES: irreversible necrosis."),
  ("Location", "Nearly all in LEFT VENTRICLE. Left anterior descending 40–50% · right coronary 30–40% · left circumflex 15–20%."),
  ("Gross changes", "First several hours: hard to see by eye (slide: 6 h) · 18–24 h: paler · then yellow, soft, red vascular border · 1–2 weeks: necrotic tissue removed · by 6 weeks: fibrous scar."),
 ]},
 {"id": "l6-valves", "label": "L6 · Valve Disease", "color": "#2f5f6b", "rows": [
  ("Stenosis vs regurgitation", "STENOSIS = fails to OPEN → PRESSURE work, gradient across valve. REGURGITATION = fails to CLOSE → VOLUME work."),
  ("Stenosis facts", "Hemodynamics affected at 50% closure; slow → compensatory HYPERTROPHY. Causes: RHEUMATIC scarring, aging CALCIFICATION."),
  ("Regurgitation facts", "Acute: infection or PAPILLARY MUSCLE RUPTURE. Important causes: rheumatic heart disease, infective endocarditis, degenerative valve changes, aortic root dilation."),
  ("Mitral stenosis", "DIASTOLIC left atrial > left ventricular gradient. Left atrial congestion/pressure ↑, pulmonary pressure ↑, stroke volume ↓ → pulmonary hypertension → right heart failure. Late: ATRIAL FIBRILLATION, atrial enlargement, ATRIAL CLOTS."),
  ("Mitral regurgitation", "SYSTOLIC backflow into atrium. HIGH AFTERLOAD INCREASES it. Atrium AND ventricle dilate + hypertrophy; severe → left heart failure."),
  ("Mitral valve prolapse", "BALLOONING into left atrium in systole. Usually silent; sometimes some regurgitation."),
  ("Aortic stenosis", "Most often AGE-RELATED CALCIFICATION; common with BICUSPID valve (slide: clinically apparent over 79). Systolic left ventricle–aortic gradient → LEFT VENTRICULAR HYPERTROPHY → ischemia and ANGINA → failure."),
  ("Aortic regurgitation", "DIASTOLIC leak back into left ventricle. AORTIC ROOT DILATION common (aging, connective tissue disease). Left ventricle hypertrophies + dilates; AORTIC DIASTOLIC PRESSURE FALLS (blood leaks back)."),
  ("Timing rule", "DIASTOLE: mitral stenosis, aortic regurgitation. SYSTOLE: mitral regurgitation, prolapse, aortic stenosis."),
 ]},
 {"id": "l6-myo", "label": "L6 · Infective, Myocardial & Pericardial", "color": "#5a3a6e", "rows": [
  ("Rheumatic heart disease", "After GROUP A BETA-HEMOLYTIC STREPTOCOCCUS. IMMUNE attack by CROSS-REACTIVITY; HLA (human leukocyte antigen) predisposition. All layers → carditis. Valves: swelling, erosions, platelets + fibrin, then SCARRING and SHORTENING."),
  ("Infective endocarditis", "Invasion + colonization of endocardium; BLOODSTREAM INVASION is a prerequisite. VEGETATIONS = organisms in FIBRIN → dysfunction + EMBOLI. Commonest: Streptococcus, Staphylococcus aureus."),
  ("Subacute endocarditis", "Insidious; needs a PREEXISTING valve lesion. LESS VIRULENT organisms (typically Streptococcus) cannot attack a healthy endocardium. S. aureus is ACUTE, not subacute (the slide lists it here; Robbins pairs it with the acute form)."),
  ("Myocarditis", "Inflammation + leukocyte infiltration + necrosis. Microbes (most often viruses, classically COXSACKIEVIRUS), immune disease, physical agents. Left ventricular dysfunction, chambers sometimes dilated, edematous muscle, endocardium usually NORMAL."),
  ("Dilated cardiomyopathy", "Also 'congested'. Dilation of one or both ventricles → failure. ALCOHOL · GENETICS · PREGNANCY · POST-VIRAL."),
  ("Hypertrophic cardiomyopathy", "Thick, HYPERKINETIC muscle. OUTFLOW OBSTRUCTION + impaired DIASTOLIC FILLING."),
  ("Restrictive cardiomyopathy", "Stiff, FIBROTIC, noncompliant (e.g. AMYLOIDOSIS) → restricted filling → low stroke volume → failure."),
  ("Pericardial effusion types", "SEROUS transudate (heart failure, hypoproteinemia) · SEROSANGUINOUS (blunt trauma, heart surgery, cardiopulmonary resuscitation) · CHYLOUS (lymph obstruction) · BLOOD/hemopericardium (penetrating trauma)."),
  ("Tamponade", "Fluid, especially if it collects quickly, COMPRESSES chambers from outside → filling impaired. Life-threatening."),
  ("Pericarditis", "ACUTE: mostly idiopathic, mostly VIRAL. CHRONIC: ADHESIVE mediastinopericarditis (heart stuck to mediastinum → workload ↑) or CONSTRICTIVE (dense scarred sac = STIFF CAGE → impaired diastolic filling)."),
  ("Not in the deck", "Objective m (blood pressure regulation) → see Lecture 7. Objective n (conduction system): no slide; only ischemia → abnormal rhythms, mitral stenosis → atrial fibrillation."),
 ]},
 {"id": "l7-structure", "label": "L7 · Vessel Anatomy & Function", "color": "#1f5a73", "rows": [
  ("Five components", "ARTERIES high pressure, strong walls, fast flow → ARTERIOLES control release into capillaries (main resistance, 'small but mighty') → CAPILLARIES exchange → VENULES collect → VEINS return blood, RESERVOIR, low pressure, thin walls."),
  ("Three layers", "INTIMA: endothelium on basement membrane + thin matrix. MEDIA: elastin + smooth muscle 'like tree rings', expand in systole, recoil in diastole. ADVENTITIA: loose connective tissue, nerves, its own small arterioles in large vessels."),
  ("Capillaries", "NO MEDIA. ≈ red cell diameter. Large cross-section, LOW flow → easy exchange. Densest in MYOCARDIUM and BRAIN. Pericytes around them."),
  ("Capillary types", "CONTINUOUS (least permeable; blood–brain barrier) · FENESTRATED (kidney glomeruli, small intestine) · SINUSOIDAL (leakiest; liver, marrow, spleen, endocrine)."),
  ("Functions", "Nutrients in · wastes out · hormones carried · HOMEOSTASIS of tissue fluid."),
  ("Loops", "PULMONARY: right heart → lungs. SYSTEMIC: left heart → tissues → right heart. Artery = AWAY from heart, so pulmonary artery carries deoxygenated blood."),
  ("Veins hold", "About 66% of total blood volume."),
 ]},
 {"id": "l7-wall", "label": "L7 · Wall Injury, Vessel Size & Blood Pressure", "color": "#2e6b4f", "rows": [
  ("Healthy endothelium", "NONTHROMBOGENIC; modulates medial tone (resistance); METABOLIZES ANGIOTENSIN; regulates inflammation; controls smooth muscle growth."),
  ("Smooth muscle cells", "Predominant media cell. Proliferate; make collagen, elastin, proteoglycans, growth factors, cytokines; constrict/dilate."),
  ("Neointimal hyperplasia", "Injury → smooth muscle MIGRATES INTO INTIMA, proliferates, makes matrix; endothelium regrows with LESS NITRIC OXIDE; platelets activate; leukocytes recruited → thick intima, NARROW LUMEN. Same response to ANY injury."),
  ("The twofold problem", "Thicker intima narrows the lumen AND lost nitric oxide (a vasodilator) lets it constrict."),
  ("Two mechanisms", "NARROWING (progressive: atherosclerosis; precipitous: thrombosis, embolism) or WEAKENING (dilation, rupture)."),
  ("Size tends to predict disease", "Tendencies, not rules (atherosclerosis also affects the aorta). LARGE elastic (aorta 2–3.5 cm) → ANEURYSM (elastic loss). MEDIUM muscular (coronary 3–4 mm, renal) → ATHEROSCLEROSIS. SMALL (≤2 mm) + ARTERIOLES (20–100 micrometers) → HYPERTENSION."),
  ("Blood pressure", "= CARDIAC OUTPUT × VASCULAR RESISTANCE. Resistance set at ARTERIOLES (constrictors vs dilators). Output = rate × stroke volume; volume set by SODIUM (water follows sodium)."),
  ("Low pressure response", "Kidney RENIN (low afferent arteriolar pressure) → angiotensinogen → ANGIOTENSIN I → endothelial catabolism → ANGIOTENSIN II → smooth muscle tone ↑ + ALDOSTERONE ↑ (sodium resorption)."),
  ("Hypertension risks", "Atherosclerosis, congestive heart failure, renal failure, CEREBRAL HEMORRHAGE, AORTIC DISSECTION."),
  ("Essential hypertension", "90–95%, idiopathic. Genetic + environmental. INSUFFICIENT RENAL SODIUM EXCRETION → volume ↑ → output ↑ → constriction → pressure ↑."),
  ("Secondary hypertension", "RENOVASCULAR: renal artery stenosis → low afferent pressure → RENIN. PRIMARY HYPERALDOSTERONISM: a common cause."),
 ]},
 {"id": "l7-athero", "label": "L7 · Arteriosclerosis & Atherosclerosis", "color": "#7a4a1f", "rows": [
  ("Arteriosclerosis", "'Hardening of the arteries': wall thickening + LOSS OF ELASTICITY. Four patterns below."),
  ("Arteriolosclerosis", "Small arteries/arterioles; HYPERTENSION. HYALINE = protein-thickened glassy wall, narrow lumen. HYPERPLASTIC = ONION SKINNING (concentric smooth muscle)."),
  ("Fibromuscular intimal hyperplasia", "Muscular arteries; inflammation or mechanical injury; a healing response → IN-STENT RESTENOSIS; limits solid-organ transplants."),
  ("Mönckeberg medial sclerosis", "CALCIFICATION OF THE MEDIA of muscular arteries; usually NOT clinically significant."),
  ("Atherosclerosis", "'Gruel' + 'hardening'. MOST clinically relevant. Coronary, cerebral, peripheral disease; slide: about half of Western deaths (an older figure; roughly a third of United States deaths today)."),
  ("Risk factors", "Hyperlipidemia · LIPOPROTEIN(a) (altered low-density lipoprotein, independent of total cholesterol) · smoking · hypertension · diabetes · METABOLIC SYNDROME · C-reactive protein · FAMILY HISTORY = strong risk, classically taught as the most important · age · men + postmenopausal women."),
  ("Sequence", "Injury → LOW-DENSITY LIPOPROTEIN accumulates → MONOCYTE adhesion → PLATELET adhesion → smooth muscle RECRUITED → proliferation, matrix, T cells → lipid → CALCIFICATION."),
  ("Atheroma", "Intimal plaque into the lumen: SOFT LIPID CORE + FIBROUS CAP. Stable → ischemia; unstable → rupture, thrombosis, embolism."),
  ("★ Peripheral arterial disease", "'Do know': stenosis → ischemia → CLAUDICATION when working muscle's demand rises."),
 ]},
 {"id": "l7-aneurysm", "label": "L7 · Aneurysm & Dissection", "color": "#6b2d5c", "rows": [
  ("Aneurysm vs dissection", "ANEURYSM = localized abnormal DILATION. DISSECTION = blood enters a wall defect and TUNNELS through the MEDIA."),
  ("Shapes", "TRUE saccular (focal bulge, 'berry') · TRUE fusiform (whole circumference) · FALSE (ruptured wall, hematoma held by extravascular tissue) · DISSECTION (intimal tear splits media)."),
  ("Weakening ≠ rupture", "An aneurysm is a WEAK wall, not a ruptured one; rupture risk rises with SIZE (in lecture: under 4 cm rarely, over 5.5 cm very high)."),
  ("Pathogenesis", "Poor connective tissue (defective collagen; abnormal transforming growth factor signaling = MARFAN) · collagen degradation > synthesis (inflammation, proteases) · smooth muscle LOSS (ischemia, hypertension, TERTIARY SYPHILIS)."),
  ("Predisposing", "Atherosclerosis · hypertension · smoking."),
  ("Abdominal aortic aneurysm", "ATHEROSCLEROTIC; abdominal aorta + common iliac arteries."),
  ("Thoracic aortic aneurysm", "HYPERTENSION; also Marfan, inflammation."),
  ("Aortic dissection", "Laminar planes of MEDIA SPLIT → blood channel in the wall. HYPERTENSION = major risk factor."),
  ("Cerebral saccular (berry)", "Thin/absent media; absent or fragmented internal elastic lamina. LACK OF ELASTIC LAMINA = main feature. Usually acquired."),
  ("Fusiform / mycotic", "Fusiform: whole circumference (atherosclerosis). MYCOTIC: infected emboli from INFECTIVE ENDOCARDITIS (rare)."),
 ]},
 {"id": "l7-other", "label": "L7 · Other Arterial Disease & Veins", "color": "#3d4f7a", "rows": [
  ("Fibromuscular dysplasia", "Focal irregular thickening (hyperplasia + fibrosis of MEDIA and INTIMA) of medium/large muscular arteries → stenosis. RENAL arteries. 'STRING OF BEADS' on angiography; may dilate and rupture."),
  ("Vasculitis", "Vessel wall inflammation, mostly SMALL vessels. Mechanisms: IMMUNE-MEDIATED or DIRECT INFECTIOUS INVASION. Large: giant cell arteritis. Medium: polyarteritis nodosa, Kawasaki. Small: ANCA (anti-neutrophil cytoplasmic antibody) necrotizing; immune complex (lupus, rheumatoid arthritis). Said to go light."),
  ("Raynaud phenomenon", "EXAGGERATED VASOCONSTRICTION to COLD + STRESS, extremities. WHITE (spasm) → BLUE (anoxia) → RED (oxygenated blood returns)."),
  ("Arteriovenous fistula", "Direct artery–vein link BYPASSING CAPILLARIES: developmental, aneurysm rupturing into a vein, penetrating injury, inflammatory necrosis, surgical (hemodialysis access)."),
  ("Veins", "Larger lumen, THINNER MEDIA (capacitance), VALVES stop gravitational backflow."),
  ("Varicose veins", "Dilated, tortuous; VALVE INSUFFICIENCY; chronic high intraluminal pressure + weak wall. Superficial (saphenous), legs; also pelvis/rectum."),
  ("Esophageal varices / hemorrhoids", "Varices: submucosal distal esophageal veins from CIRRHOSIS + PORTAL HYPERTENSION. Hemorrhoids: varicose venous plexus at the ANORECTAL junction."),
  ("Deep vein thrombosis", "Deep veins (femoral, popliteal, tibial); STASIS in a dilated vein. THIRD most common cardiovascular cause of death."),
  ("Deep vein thrombosis risks", "Reduced flow (IMMOBILITY) · raised venous pressure · mechanical injury · raised viscosity (dehydration, thrombocytosis) · anatomy · hypercoagulable (cancer, sepsis, lupus, ORAL ESTROGEN)."),
  ("Virchow triad", "VESSEL WALL DAMAGE · ABNORMAL BLOOD FLOW (turbulence or stasis) · HYPERCOAGULABILITY."),
  ("Clot fate", "Neutrophils + macrophages infiltrate fibrin; COLLAGEN replaces fibrin over weeks → less flow. Dislodges → EMBOLUS → PULMONARY ARTERY = pulmonary embolus."),
 ]},
 {"id": "l8-basics", "label": "L8 · Immunity Basics & Blood Cells", "color": "#4a2f6e", "rows": [
  ("Immunity: 3 functions", "DEFENSE (resistance to invaders) · SURVEILLANCE (of self, for mutant or cancerous cells) · HOMEOSTASIS (removing cellular debris)."),
  ("Memory & specificity", "Memory = faster, stronger adaptive response on RE-EXPOSURE. B- and T-cell receptors recognize particular EPITOPES; innate receptors recognize patterns shared by groups of organisms."),
  ("Active vs passive", "ACTIVE: the body's own response after antigen exposure (natural = met naturally; artificial = VACCINATION). PASSIVE: PREFORMED antibodies transferred; immediate protection that declines."),
  ("Passive examples", "Natural: maternal IgG through the PLACENTA, IgA in BREAST MILK. Artificial: tetanus and rabies immune globulin."),
  ("Innate immunity", "Acts WITHOUT prior sensitization: skin and mucosal barriers, phagocytes, complement, interferons. Natural killer cells ≈ 5–15% of circulating lymphocytes."),
  ("Granulocytes", "NEUTROPHIL: phagocytosis, first responders, most numerous. EOSINOPHIL: allergy and parasites. BASOPHIL: like tissue mast cells (★ 'Baso B blood', mast cells in tissue)."),
  ("Monocyte → macrophage", "Monocytes enter tissues during inflammation and become macrophages (tissue macrophage = HISTIOCYTE); they remove material and coordinate inflammation."),
  ("Lymphocytes", "B: humoral, matures in BONE MARROW, becomes the plasma cell. T: cellular, matures in the THYMUS (★ 'T cells, thymus'). Natural killer: needs NO specific antigen; kills tumor and infected cells."),
  ("Markers", "T: CD3 (CD4 or CD8). B: CD19, CD20; surface immunoglobulin LOST as a plasma cell. Natural killer: CD56, CD16."),
  ("Phagocytosis", "Adhere → pseudopods engulf (PHAGOSOME) → fuse with lysosome (PHAGOLYSOSOME) → acid hydrolases digest → residual body → EXOCYTOSIS."),
  ("Lymph flow", "No pump: SKELETAL MUSCLE movement, THORACIC pressure changes in breathing, pulsing ARTERIES; valves keep it one-way."),
 ]},
 {"id": "l8-antibodies", "label": "L8 · B Cells & Antibodies", "color": "#6a4fa3", "rows": [
  ("B cell → plasma cell", "Antigen-INDEPENDENT phase: surface IgM. Antigen-DEPENDENT phase (started by antigen exposure): becomes a PLASMA CELL secreting specific antibody. Antigen SELECTS the matching B cell → clonal expansion → plasma + memory cells."),
  ("Primary response", "After FIRST exposure; develops over days; IgM rises first; memory cells form."),
  ("Secondary response", "After RE-EXPOSURE; memory cells → FASTER, STRONGER (★); class-switched antibody, often IgG, higher and longer. ★ High IgM = first exposure; low IgM + high IgG = earlier exposure."),
  ("Antibody unit", "2 HEAVY + 2 LIGHT chains (light = KAPPA or LAMBDA). Heavy + light VARIABLE regions = antigen-binding site. Heavy-chain CONSTANT region decides the CLASS."),
  ("Fab vs Fc", "Fab = antigen-binding arms. Fc = constant stem → EFFECTOR functions (complement-binding site on CH2). Papain cuts IgG into 2 Fab + Fc."),
  ("IgM", "5–10%. PENTAMER (J chain) when secreted. Often FIRST in a new response; AGGLUTINATION; efficient classical complement."),
  ("IgG", "75–80%, the largest share. Monomer, 4 subclasses. CROSSES THE PLACENTA (★ how maternal immunity reaches the baby); prominent in secondary responses."),
  ("IgA · IgD · IgE", "IgA 10–15%: secretory DIMER (saliva, tears, colostrum), blocks microbial attachment. IgD <1%: B-cell receptor with IgM. IgE <1%: on MAST CELLS and BASOPHILS → allergy, anaphylaxis, parasites."),
  ("Antibody functions", "AGGLUTINATION (clumps cells) · NEUTRALIZATION (blocks without destroying ★) · LYSIS (with complement) · PRECIPITATION (cross-links soluble antigen) · OPSONIZATION (coats for phagocytes)."),
  ("ABO", "O red cells carry neither A nor B → O is the universal red-cell donor (★); AB recipients have neither antibody → take O, A, B, AB."),
 ]},
 {"id": "l8-tcells", "label": "L8 · T Cells & Hypersensitivity", "color": "#7a2f5a", "rows": [
  ("★ CD4 vs CD8", "'Four letters in HELP': CD4 = HELPER, reads MHC (major histocompatibility complex) CLASS II. CD8 = CYTOTOXIC, reads CLASS I."),
  ("Helper T cell", "COORDINATES cellular and humoral responses by cytokines and contact; supports B-cell antibody production; IFN-γ (interferon gamma) activates macrophages."),
  ("Cytotoxic T cell", "Kills virus-infected, tumor and transplanted cells: PERFORIN + GRANZYMES → target-cell APOPTOSIS."),
  ("Regulatory T cell", "LIMITS immune activation, maintains SELF-TOLERANCE; many are CD4 expressing FOXP3."),
  ("ADCC", "Antibody-dependent cellular cytotoxicity: the natural killer cell's CD16 binds the Fc of IgG coating a target."),
  ("Hypersensitivity", "Humoral or cellular immune reactions that INJURE the body. Numbered by MECHANISM, not severity (★)."),
  ("Type I", "IgE fixed on MAST CELLS/basophils after a sensitizing exposure; re-exposure → HISTAMINE release. Local allergy or ANAPHYLAXIS (bronchospasm, laryngeal edema, hypotension)."),
  ("Type II", "IgG or IgM binds antigen ON cells or tissue → phagocytosis, complement, ADCC; can STIMULATE or BLOCK receptors. ABO incompatibility, anti-glomerular basement membrane disease."),
  ("Type III", "Antigen–antibody COMPLEXES deposit in tissue or vessel walls. Arthus (local), serum sickness (systemic), LUPUS."),
  ("Type IV", "Sensitized CD4 or CD8 T CELLS; delayed 24–72 h; granulomas. Contact dermatitis, tuberculosis reactions, transplant rejection."),
 ]},
 {"id": "l8-complement", "label": "L8 · Complement, Immunodeficiency & Age", "color": "#2f4f6e", "rows": [
  ("Complement", "Proteins made mostly by the LIVER, circulating as INACTIVE precursors; activation = a regulated CASCADE."),
  ("3 pathways (★)", "CLASSICAL: C1 binds antigen-bound IgM or IgG. LECTIN: mannose-binding lectin binds microbial carbohydrate. ALTERNATIVE: C3 on permissive surfaces (factor B, factor D, properdin). All CONVERGE ON C3."),
  ("3 outcomes", "OPSONIZATION (C3b coat) · INFLAMMATION (C3a, C4a, C5a: vasodilation, attraction of phagocytes) · MEMBRANE ATTACK COMPLEX (C5b + C6–C9 pore → lysis). ★ Lysis is only ONE outcome."),
  ("Autoimmunity (deck)", "No slide of its own: regulatory T cells keep self-tolerance; anti-self antibody can destroy or stimulate/block (type II); lupus is type III; autoantibodies rise with age."),
  ("Primary immunodeficiency", "INTRINSIC, often GENETIC. X-linked agammaglobulinemia: no B-cell maturation → recurrent PYOGENIC infections. DiGeorge: thymic/T-cell development. Severe combined: T AND B."),
  ("Secondary immunodeficiency", "From disease, medications, malignancy or poor nutrition."),
  ("Age", "Neonates: protected by maternal IgG and milk IgA, which wane. Older adults: weaker responses to NEW antigens; more autoantibodies."),
 ]},
 {"id": "l9-arf", "label": "L9 · Respiratory Failure, Pulmonary Hypertension & Cancer", "color": "#1f5a73", "rows": [
  ("Hypoxemia vs hypoxia", "Hypoxemia = low BLOOD oxygen (PaO2, arterial oxygen tension; saturation). Hypoxia = low TISSUE oxygenation."),
  ("Acute respiratory failure", "On room air: PaO2 < 60 mmHg · PaCO2 (arterial carbon dioxide tension) > 50 mmHg · pH < 7.30."),
  ("Hypoxic failure", "Low oxygen, NORMAL or LOW carbon dioxide: V/Q (ventilation/perfusion) mismatch · SHUNT · decreased diffusion · alveolar hypoventilation · altitude."),
  ("Hypercapnic failure", "Carbon dioxide not removed: low ventilation or rate · cannot signal (Guillain-Barré, cord injury) · DEAD SPACE (pulmonary embolism, low output) · more carbon dioxide made (fever, burns) · cannot sense it (drugs)."),
  ("★ Dead space vs shunt", "Dead space = ventilation without perfusion. Shunt = perfusion without ventilation."),
  ("Pulmonary circulation", "HIGH FLOW, LOW PRESSURE: 22/8–25/8 mmHg, mean 15. Pulmonary arteries carry DEOXYGENATED blood (★ names = direction, not oxygen)."),
  ("Pulmonary hypertension ⚠", "Slide: sustained > 30 mmHg. Recording: resting MEAN > 20 mmHg by right heart catheterization. Know both."),
  ("Routes to it", "More FLOW (left-to-right shunt, polycythemia) · more RESISTANCE (hypoxic vasoconstriction, EMBOLISM, fibrosis) · higher LEFT ATRIAL pressure (mitral stenosis)."),
  ("Vessel changes", "MEDIA thickens (more muscle), INTIMA fibroses, PLEXIFORM lesions."),
  ("Lung cancers", "SQUAMOUS 20–30%, central, sputum cytology. ADENO 35–40% (largest), peripheral. LARGE CELL 5–10%, peripheral. SMALL CELL 15–20%, central, doubles in ~33 days, PARANEOPLASTIC."),
 ]},
 {"id": "l9-obstructive", "label": "L9 · Obstructive Disease & Asthma", "color": "#2e6b4f", "rows": [
  ("Obstructive disease", "Increased airflow RESISTANCE: in the WALL (asthma, bronchitis) · LOST PARENCHYMA (emphysema) · in the LUMEN (bronchiectasis, cystic fibrosis, foreign body)."),
  ("Test pattern", "Low FEV1/FVC (forced expiratory volume in 1 second / forced vital capacity) = airflow limitation · high RESIDUAL VOLUME = incomplete emptying · low DLCO (diffusing capacity for carbon monoxide) = a separate gas-transfer question."),
  ("Asthma", "REVERSIBLE obstruction + airway inflammation + HYPER-RESPONSIVENESS."),
  ("Allergic (extrinsic)", "IgE on MAST CELLS → histamine, LEUKOTRIENES (slow-reacting substances of anaphylaxis), prostaglandins, bradykinins, eosinophil chemotactic factor, serotonin."),
  ("Non-allergic (intrinsic)", "Exercise, stress, irritants, aspirin; NEGATIVE skin tests, NORMAL IgE; middle age; worse prognosis."),
  ("Asthma airway", "Epithelium DENUDED → goblet cells · COLLAGEN under basement membrane · edema · mucus plugs · VAGAL → mucus + bronchoconstriction · REMODELING."),
  ("Acute bronchitis", "Inflamed trachea/bronchi, mostly VIRAL; more mucus, lost cilia; lasting HYPERIRRITABILITY explains the lingering cough."),
  ("Chronic bronchitis (type B)", "Productive cough > 3 months a year for 2+ years; smoking 90%; gland + GOBLET hypertrophy; cilia → SQUAMOUS; plugs → V/Q mismatch. BLUE BLOATER = cyanosis + right-heart edema."),
  ("Emphysema (type A)", "Alveolar wall DESTRUCTION WITHOUT FIBROSIS. PROTEASES from neutrophils/macrophages; smoking inactivates ALPHA-1 ANTITRYPSIN. Lost RADIAL TRACTION → more resistance, less airflow; air trapped → BULLAE. PINK PUFFER."),
  ("Emphysema types", "CENTRIACINAR: respiratory bronchioles (with chronic bronchitis). PANACINAR: alveoli. PARASEPTAL: peripheral lobules."),
  ("Bronchiectasis", "Wall DESTRUCTION → DILATED bronchi; congenital (50% related to cystic fibrosis) or acquired; children at risk (soft bronchi). Dilations = infection POCKETS → foul purulent sputum. Shapes: cylindrical, saccular, fusiform."),
  ("Cor pulmonale", "Hypoxia → pulmonary VASOCONSTRICTION → pulmonary hypertension → RIGHT VENTRICULAR DILATION → right heart failure."),
 ]},
 {"id": "l9-restrictive", "label": "L9 · Restrictive Disease & Acute Respiratory Distress Syndrome", "color": "#7a4a1f", "rows": [
  ("Restrictive = expansion", "DECREASED EXPANSION from parenchyma, pleura, chest wall or neuromuscular disease. LOW TOTAL LUNG CAPACITY confirms it (low FVC alone does not)."),
  ("Interstitial lung disease", "Starts with INJURY to alveolar epithelium or capillary endothelium → immune reaction → thick interstitium, COLLAGEN."),
  ("3 alveolar patterns", "INFLAMMATION (early, REVERSIBLE) → FIBROSIS (fibroblasts, collagen) → DESTRUCTION (end stage: STIFF, NONCOMPLIANT lungs)."),
  ("Sarcoidosis", "ALVEOLAR MACROPHAGES activated by an unknown trigger; NONCASEATING epithelioid GRANULOMAS (lymph nodes, lung); ASTEROID BODIES; abnormal T cells."),
  ("Hypersensitivity pneumonitis", "Inhaled ORGANIC agents (birds, fungi, wheat weevil); TYPE III immune complexes; nonsmokers. 'Extrinsic allergic alveolitis'."),
  ("Pneumoconiosis", "Inhaled INORGANIC dust (coal, silica, asbestos); macrophages cannot clear it → FIBROSIS. Smoking depresses ciliary clearance."),
  ("ARDS (acute respiratory distress syndrome)", "ATELECTATIC disorder. Alveolar-capillary membrane DAMAGE → LEAKY capillaries → protein-rich NONCARDIOGENIC edema; complement + neutrophil sequestration."),
  ("ARDS: 3 processes", "Noncardiogenic EDEMA (leaky capillaries) · ATELECTASIS (no SURFACTANT) · HYALINE MEMBRANES (protein deposits)."),
  ("Pulmonary edema (gathered)", "Starling: hydrostatic OUT vs oncotic IN. More capillary pressure or less oncotic pressure → more filtration. Leaky capillaries → noncardiogenic edema."),
 ]},
 {"id": "l9-pleura", "label": "L9 · Pleura, Sleep Apnea & Pneumonia", "color": "#3d4f7a", "rows": [
  ("Primary pneumothorax", "TALL, THIN MEN 20–40; SUBPLEURAL BLEBS at the apices rupture; smoking raises risk."),
  ("Secondary pneumothorax", "Complication of lung disease: asthma, emphysema, cystic fibrosis, pneumonia, tuberculosis."),
  ("Tension pneumothorax", "Trauma; air ENTERS but cannot LEAVE → lung collapses, mediastinum shifts AWAY → less VENOUS RETURN and CARDIAC OUTPUT."),
  ("Pleural effusion causes", "Raised HYDROSTATIC pressure (heart failure) · lowered ONCOTIC pressure (nephrotic syndrome, cirrhosis) · lowered pleural pressure (lung collapse). Normal 5–15 mL."),
  ("Transudate", "Protein ratio < 0.5 · LDH (lactate dehydrogenase) ratio < 0.6 · specific gravity < 1.016. PRESSURE problem: heart failure, cirrhosis, nephrotic syndrome."),
  ("Exudate", "Protein ratio > 0.5 or LDH ratio > 0.6 (ONE criterion is enough). PERMEABILITY or LYMPHATIC problem: cancer, infection, PULMONARY EMBOLISM, sarcoidosis."),
  ("Chylothorax", "CHYLE leaking from the THORACIC DUCT (trauma, lymphoma)."),
  ("Obstructive sleep apnea", "≥ 5 events/hour; collapsible PHARYNX closes. APNEA: no airflow ≥ 10 s WITH effort. HYPOPNEA: reduced flow + desaturation or arousal. No flow + NO effort = CENTRAL."),
  ("Pneumonia sources", "ASPIRATION (gross aspiration → ANAEROBES, abscess) · inhalation (virus, Mycoplasma) · BLOOD-BORNE (right-sided endocarditis, intravenous drug use)."),
  ("Community vs hospital", "Community: at home, or hospitalized < 48 h. Hospital: early (≤ 4 days) susceptible bacteria; LATE = MULTIDRUG-RESISTANT."),
  ("Pulmonary embolism (gathered)", "Raises DEAD SPACE (hypercapnia) · causes pulmonary hypertension by OBSTRUCTION · causes ARDS and acute respiratory failure · EXUDATIVE effusion."),
 ]},
]

BANNED = ["first-line", "drug of choice", "treatment of choice", "next step", "surgically repaired"]


def main():
    for t in T:
        rows = []
        for term, fact in t["rows"]:
            for w in BANNED:
                assert w not in (term + fact).lower(), (t["id"], w)
            rows.append((html.escape(term, quote=False), html.escape(fact, quote=False)))
        t["rows"] = rows
    page = render(
        title="Cram Sheet — Clinical Pathophysiology I Exam 2",
        kicker="Clinical Pathophysiology I · Exam 2 · Class of 2028",
        h1="Clinical Pathophysiology I Exam 2 Cram Sheet",
        sub="Lectures 6 Cardiac, 7 Vascular, 8 Immunity and 9 Pulmonary, condensed. Lecture 10 is added when it is posted. Mechanism only, never management.",
        topics=T,
        guide_href="cp-exam-2-study-guide.html",
        footer_note="Condensed from the Clinical Pathophysiology I Exam 2 Study Guide (Class of 2028). For the full explanation and figures behind any of these, see the full guide.",
    )
    open(OUT, "w", encoding="utf-8").write(page)
    print("wrote", os.path.relpath(OUT, ROOT), sum(len(t["rows"]) for t in T), "rows,", len(T), "topics")


if __name__ == "__main__":
    main()
