#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Clinical Pathophysiology I Exam 2 cram sheet (Lectures 6 and 7 so far).

Condensed ONLY from cp-exam-2-study-guide.html (cram_sheets_feature): nothing
here that the guide does not say, numbers kept verbatim. Rendered with the
shared tools/cram-sheet-template/render.py, never hand-edited. Lectures 8-10
append as further topics when their guide sections exist.

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
  ("Familial hypercholesterolemia", "Most common genetic hyperlipidemia. Defective LOW-DENSITY LIPOPROTEIN RECEPTOR on liver cells → liver cannot clear cholesterol."),
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
  ("Prinzmetal (variant)", "VASOSPASM (cause unknown). Unpredictable; NO relation to physical or emotional stress."),
  ("Unstable (crescendo)", "May progress to acute ischemia → counted with the ACUTE coronary syndromes."),
  ("Acute coronary syndrome", "Unstable angina + myocardial infarction (hard to tell apart clinically). Pain longer than typical angina; PLAQUE RUPTURE + ACUTE THROMBOSIS."),
  ("Infarction mechanism", "Prolonged/total loss of flow → NECROSIS or APOPTOSIS. Thrombus on a cracked plaque → platelet plug → clotting cascade → occlusion. Outcome depends on COLLATERALS, WORKLOAD, TIME."),
  ("Occlusion timeline", "Immediately: ATP depleted. Few minutes: cannot contract. AFTER 30 MINUTES: irreversible necrosis."),
  ("Location", "Nearly all in LEFT VENTRICLE. Left anterior descending 40–50% · right coronary 30–40% · left circumflex 15–20%."),
  ("Gross changes", "6 h: first visible · 18–24 h: paler · then yellow, soft, red vascular border · 1–2 weeks: necrotic tissue removed · by 6 weeks: fibrous scar."),
 ]},
 {"id": "l6-valves", "label": "L6 · Valve Disease", "color": "#2f5f6b", "rows": [
  ("Stenosis vs regurgitation", "STENOSIS = fails to OPEN → PRESSURE work, gradient across valve. REGURGITATION = fails to CLOSE → VOLUME work."),
  ("Stenosis facts", "Hemodynamics affected at 50% closure; slow → compensatory HYPERTROPHY. Causes: RHEUMATIC scarring, aging CALCIFICATION."),
  ("Regurgitation facts", "Acute: infection or PAPILLARY MUSCLE RUPTURE. Causes: rheumatic heart disease, infective endocarditis."),
  ("Mitral stenosis", "DIASTOLIC left atrial > left ventricular gradient. Left atrial congestion/pressure ↑, pulmonary pressure ↑, stroke volume ↓ → pulmonary hypertension → right heart failure. Late: ATRIAL FIBRILLATION, atrial enlargement, ATRIAL CLOTS."),
  ("Mitral regurgitation", "SYSTOLIC backflow into atrium. HIGH AFTERLOAD INCREASES it. Atrium AND ventricle dilate + hypertrophy; severe → left heart failure."),
  ("Mitral valve prolapse", "BALLOONING into left atrium in systole. Usually silent; sometimes some regurgitation."),
  ("Aortic stenosis", "Most often AGE-RELATED CALCIFICATION; common with BICUSPID valve (slide: clinically apparent over 79). Systolic left ventricle–aortic gradient → LEFT VENTRICULAR HYPERTROPHY → ischemia and ANGINA → failure."),
  ("Aortic regurgitation", "DIASTOLIC leak back into left ventricle. AORTIC ROOT DILATION common (aging, connective tissue disease). Left ventricle hypertrophies + dilates; DIASTOLIC PRESSURE FALLS."),
  ("Timing rule", "DIASTOLE: mitral stenosis, aortic regurgitation. SYSTOLE: mitral regurgitation, prolapse, aortic stenosis."),
 ]},
 {"id": "l6-myo", "label": "L6 · Infective, Myocardial & Pericardial", "color": "#5a3a6e", "rows": [
  ("Rheumatic heart disease", "After GROUP A BETA-HEMOLYTIC STREPTOCOCCUS. IMMUNE attack by CROSS-REACTIVITY; HLA (human leukocyte antigen) predisposition. All layers → carditis. Valves: swelling, erosions, platelets + fibrin, then SCARRING and SHORTENING."),
  ("Infective endocarditis", "Invasion + colonization of endocardium; BLOODSTREAM INVASION is a prerequisite. VEGETATIONS = organisms in FIBRIN → dysfunction + EMBOLI. Commonest: Streptococcus, Staphylococcus aureus."),
  ("Subacute endocarditis", "Insidious; needs a PREEXISTING valve lesion. LESS VIRULENT organisms (slide lists S. aureus, Streptococcus, Candida) cannot attack a healthy endocardium. (Textbook generally pairs S. aureus with the acute form.)"),
  ("Myocarditis", "Inflammation + leukocyte infiltration + necrosis. Microbes, immune disease, physical agents; COXSACKIEVIRUS most common in North America. Left ventricular dysfunction, ALL FOUR chambers dilated, edematous muscle, endocardium usually NORMAL."),
  ("Dilated cardiomyopathy", "Also 'congested'. Dilation of one or both ventricles → failure. ALCOHOL · GENETICS · PREGNANCY · POST-VIRAL."),
  ("Hypertrophic cardiomyopathy", "Thick, HYPERKINETIC muscle. OUTFLOW OBSTRUCTION + impaired DIASTOLIC FILLING."),
  ("Restrictive cardiomyopathy", "Stiff, FIBROTIC, noncompliant (e.g. AMYLOIDOSIS) → restricted filling → low stroke volume → failure."),
  ("Pericardial effusion types", "SEROUS transudate (heart failure, hypoproteinemia) · SEROSANGUINOUS (blunt trauma, heart surgery, cardiopulmonary resuscitation) · CHYLOUS (lymph obstruction) · BLOOD/hemopericardium (penetrating trauma)."),
  ("Tamponade", "Large effusion COMPRESSES chambers from outside → filling impaired. Life-threatening."),
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
  ("Size predicts disease", "LARGE elastic (aorta 2–3.5 cm) → ANEURYSM (elastic loss). MEDIUM muscular (coronary 3–4 mm, renal) → ATHEROSCLEROSIS. SMALL (≤2 mm) + ARTERIOLES (20–100 micrometers) → HYPERTENSION."),
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
  ("Atherosclerosis", "'Gruel' + 'hardening'. MOST clinically relevant. Coronary, cerebral, peripheral disease; about half of Western deaths."),
  ("Risk factors", "Hyperlipidemia · LIPOPROTEIN(a) (altered low-density lipoprotein, independent of total cholesterol) · smoking · hypertension · diabetes · METABOLIC SYNDROME · C-reactive protein · FAMILY HISTORY = MOST IMPORTANT · age · men + postmenopausal women."),
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
  ("Virchow triad", "VESSEL WALL DAMAGE · FLOW TURBULENCE · HYPERCOAGULABILITY."),
  ("Clot fate", "Neutrophils + macrophages infiltrate fibrin; COLLAGEN replaces fibrin over weeks → less flow. Dislodges → EMBOLUS → PULMONARY ARTERY = pulmonary embolus."),
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
        sub="Lecture 6 Cardiac and Lecture 7 Vascular, condensed. Lectures 8–10 are added as each is posted. Mechanism only, never management.",
        topics=T,
        guide_href="cp-exam-2-study-guide.html",
        footer_note="Condensed from the Clinical Pathophysiology I Exam 2 Study Guide (Class of 2028). For the full explanation and figures behind any of these, see the full guide.",
    )
    open(OUT, "w", encoding="utf-8").write(page)
    print("wrote", os.path.relpath(OUT, ROOT), sum(len(t["rows"]) for t in T), "rows,", len(T), "topics")


if __name__ == "__main__":
    main()
