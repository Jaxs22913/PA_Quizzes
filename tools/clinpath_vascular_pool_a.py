# -*- coding: utf-8 -*-
"""Clinical Pathophysiology I, Lecture 7 -- Vascular Pathophysiology, part A.

Anatomy and function of the vascular system, the three wall layers, the
molecular behavior of endothelium and smooth muscle, intimal thickening, and
blood pressure regulation. Part B carries arteriosclerosis through venous
disease.

MECHANISM ONLY, per [[clin_path_exam_spec]]. The deck cooperates -- it is a
molecular-mechanism lecture throughout, and even where it names a disease it
names the process rather than what is done about it.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation, so the
correct answer is never the longest option.

The lecture WAS recorded (15 September) but sits behind the transcription
queue, which runs in exam-date order and has not reached Clin Path Exam 2 --
so every question comes off the slides for now and the lecturer's own
emphasis should be layered in once the transcript lands.
"""

D = "SV Vascular Pathophys I Fall 2026.pptx"
IO_ANAT = "Review the anatomy of the vascular system"
IO_FUNC = "Review the functions of the components of the vascular system"
IO_MOL = "Describe the molecular mechanisms of vascular pathologies"

def c(n): return D + ", Slide %d" % n

QUESTIONS = [

{"topic": "Function of the vascular system", "io": IO_FUNC, "slot": "function",
 "q": "Which four functions does the vascular system serve?",
 "opts": [
  ["Transport of nutrients, wastes, hormones; homeostasis",
   "Correct. Nutrients go to tissues, wastes come away from them, hormones travel from one part of the body to another, and fluid balance is maintained across all tissues so cells can function."],
  ["Gas exchange and the production of blood cells",
   "Gas exchange happens at the capillary interface, but cell production is a marrow function rather than one of the four named vascular roles."],
  ["Immune surveillance and antibody synthesis",
   "Antibody synthesis belongs to lymphoid tissue. The vascular system transports rather than manufactures."],
  ["Thermoregulation and acid production",
   "Neither is among the four functions named for the vascular system."]],
 "c": 0, "cite": c(5)},

{"topic": "Circulatory loops", "io": IO_ANAT, "slot": "anatomy",
 "q": "What does the pulmonary loop do?",
 "opts": [
  ["Carries deoxygenated blood from the right heart to the lungs",
   "Correct. The systemic loop is the mirror image: highly oxygenated blood from the left heart to the tissues, removing wastes and returning deoxygenated blood to the right heart."],
  ["Carries oxygenated blood from the left heart to the tissues",
   "That is the systemic loop, which begins on the left side of the heart rather than the right."],
  ["Returns deoxygenated blood from the tissues to the right heart",
   "That is the returning half of the systemic loop rather than the pulmonary circuit."],
  ["Supplies the heart muscle itself with blood",
   "Coronary supply is a branch of the systemic circulation rather than a loop in this scheme."]],
 "c": 0, "cite": c(6)},

{"topic": "Functional components", "io": IO_FUNC, "slot": "function",
 "q": "What characterizes the arteries?",
 "opts": [
  ["High pressure, strong walls, high flow velocity",
   "Correct, and the contrast with veins is instructive: veins are low pressure with thin walls and serve as the major reservoir of extra blood."],
  ["Low pressure, thin walls, and a role as a blood reservoir",
   "That describes the veins, which hold the reserve volume rather than delivering at pressure."],
  ["Control conduits releasing blood into the capillaries",
   "That is the arterioles, the regulating segment rather than the conducting one."],
  ["Collection of blood from capillaries into larger vessels",
   "Collecting blood emerging from the capillaries describes the venules, which coalesce gradually into larger veins."]],
 "c": 0, "cite": c(8)},

{"topic": "Functional components", "io": IO_FUNC, "slot": "function",
 "q": "What is the role of the arterioles?",
 "opts": [
  ["Control conduits for release of blood to the capillaries",
   "Correct, and it is the same property that makes them the regulators of vascular resistance, which is one of the two determinants of blood pressure."],
  ["Exchange of fluid, nutrients and wastes with the tissues",
   "That is the capillaries, whose thin walls and slow flow make exchange possible."],
  ["Transport of blood back toward the heart",
   "That is the veins, carrying blood in the returning direction."],
  ["Collection of blood emerging from the capillary bed",
   "That is the venules, immediately downstream of the capillaries."]],
 "c": 0, "cite": c(8)},

{"topic": "Functional components", "io": IO_FUNC, "slot": "function",
 "q": "What do the capillaries exchange?",
 "opts": [
  ["Fluid, nutrients, electrolytes and wastes",
   "Correct, and the exchange runs in both directions between blood and tissues, which is why this is the only segment where the vascular system does its actual work. Hormones cross the same way."],
  ["Oxygen alone",
   "The exchange is far broader, covering fluid, electrolytes, hormones and wastes as well as respiratory gases."],
  ["Blood cells into the interstitium",
   "Cells are not the exchanged material; diffusible substances are."],
  ["Nothing &mdash; capillaries only conduct blood",
   "Exchange is precisely what defines the capillary segment; conduction is what the arteries and veins do."]],
 "c": 0, "cite": c(8)},

{"topic": "Blood vessel layers", "io": IO_ANAT, "slot": "anatomy",
 "q": "What does the intima consist of?",
 "opts": [
  ["A single layer of endothelial cells on a basement membrane",
   "Correct, with a thin underlying layer of extracellular matrix beneath it. Everything that goes wrong in intimal thickening begins in this one cell layer."],
  ["Lamellar units of elastin fibers and smooth muscle cells",
   "That describes the media of an elastic artery, arranged in layers like tree rings."],
  ["Loose connective tissue with nerve fibers",
   "That describes the adventitia, which provides support rather than lining the lumen."],
  ["Several layers of stratified squamous epithelium",
   "The endothelial lining is a SINGLE layer of simple squamous epithelium rather than a stratified one."]],
 "c": 0, "cite": c(10)},

{"topic": "Blood vessel layers", "io": IO_ANAT, "slot": "anatomy",
 "q": "How is the media of an elastic artery such as the aorta arranged?",
 "opts": [
  ["In lamellar units of elastin and smooth muscle, like tree rings",
   "Correct, and the arrangement has a purpose: the layers expand during systole and recoil during diastole, which is what smooths pulsatile flow into continuous flow."],
  ["As a single layer of endothelial cells",
   "A single endothelial layer is the intima rather than the media."],
  ["As loose connective tissue carrying its own arterioles",
   "That is the adventitia, which in large vessels carries small arterioles to perfuse itself and part of the media."],
  ["As densely packed collagen with no elastic component",
   "Elastin is the defining component here, since recoil is what the layer exists to provide."]],
 "c": 0, "cite": c(10)},

{"topic": "Blood vessel layers", "io": IO_ANAT, "slot": "anatomy",
 "q": "What does the adventitia contain?",
 "opts": [
  ["Loose connective tissue, sometimes with nerve fibers",
   "Correct, and in large vessels it carries its own small arterioles, which perfuse the adventitia and part of the media &mdash; the wall is too thick to be fed from the lumen alone."],
  ["A single layer of endothelium on a basement membrane",
   "A single endothelial layer on a basement membrane is the intima, the innermost of the three layers."],
  ["Lamellar units of elastin and smooth muscle",
   "Lamellar units of elastin and smooth muscle describe the media of an elastic artery rather than the adventitia."],
  ["Nothing &mdash; it is a potential space",
   "It is a real layer of loose connective tissue providing structural support."]],
 "c": 0, "cite": c(10)},

{"topic": "Blood vessel layers", "io": IO_ANAT, "slot": "anatomy",
 "q": "Which vessels are excluded from the three-layer description?",
 "opts": [
  ["Capillaries",
   "Correct. A capillary lumen is lined with endothelial cells but has no media at all, which is what makes its wall thin enough for exchange."],
  ["Arterioles",
   "Arterioles retain a muscular media, which is what allows them to regulate resistance."],
  ["Venules",
   "Venules retain a wall structure and are not the exception named; capillaries, which have no media, are."],
  ["Elastic arteries",
   "Elastic arteries are the fullest expression of the three-layer structure rather than an exception to it."]],
 "c": 0, "cite": c(10)},

{"topic": "Capillaries", "io": IO_ANAT, "slot": "anatomy",
 "q": "How does capillary diameter compare with a red blood cell?",
 "opts": [
  ["Equal to or even slightly smaller",
   "Correct, and the consequence is that red cells must deform to pass, which brings their membranes into close contact with the endothelium."],
  ["About ten times larger",
   "A capillary is at most the width of a single red cell rather than many times it."],
  ["About a hundred times larger",
   "That scale belongs to the large elastic arteries rather than to a capillary."],
  ["Too variable to compare",
   "The comparison is specific: equal to or slightly smaller than a red blood cell."]],
 "c": 0, "cite": c(11)},

{"topic": "Capillaries", "io": IO_FUNC, "slot": "mechanism",
 "q": "Why does the capillary bed favor exchange?",
 "opts": [
  ["Thin walls combined with slow flow",
   "Correct, and the slow flow follows from the large cross-sectional area of the bed: the same volume spread across far more vessels moves more slowly through each."],
  ["Thick walls with rapid flow",
   "Both would work against exchange; the capillary has the opposite of each."],
  ["A muscular media generating turbulence",
   "Capillaries have no media, and exchange depends on slow laminar flow rather than turbulence."],
  ["Active pumping across the endothelium",
   "The exchange described is diffusion of substances rather than active pumping."]],
 "c": 0, "cite": c(11)},

{"topic": "Capillaries", "io": IO_ANAT, "slot": "anatomy",
 "q": "Which tissues have the highest density of capillaries?",
 "opts": [
  ["Myocardium and brain",
   "Correct, because capillary density tracks metabolic rate &mdash; tissues that consume the most oxygen need the shortest diffusion distances to reach it."],
  ["Skin and subcutaneous fat",
   "Both have comparatively low metabolic rates and correspondingly lower capillary density."],
  ["Tendon and ligament",
   "Dense connective tissue such as tendon and ligament is relatively poorly vascularized and has a low metabolic rate."],
  ["Cartilage",
   "Cartilage is avascular, at the opposite extreme from the tissues named."]],
 "c": 0, "cite": c(11)},

{"topic": "Endothelial cells", "io": IO_MOL, "slot": "mechanism",
 "q": "What kind of epithelium lines the vessel lumen?",
 "opts": [
  ["Specialized simple squamous epithelium",
   "Correct. The endothelium is a single flat layer, which is what allows it to be both a barrier and a rapid signaling interface with the blood."],
  ["Stratified squamous epithelium",
   "A stratified lining would be too thick for the metabolic and signaling roles the endothelium performs."],
  ["Pseudostratified columnar epithelium",
   "That lining belongs to the airway rather than the vascular lumen."],
  ["Transitional epithelium",
   "Transitional epithelium lines the urinary tract, where distension rather than exchange is the requirement."]],
 "c": 0, "cite": c(12)},

{"topic": "Endothelial cells", "io": IO_MOL, "slot": "mechanism",
 "q": "What does a nonthrombogenic endothelial surface achieve?",
 "opts": [
  ["It keeps blood in a fluid state",
   "Correct, and it is an active property rather than a passive one, which is why endothelial injury is the event that lets platelets adhere and a thrombus begin."],
  ["It accelerates clot formation at rest",
   "The healthy surface does the opposite, resisting thrombosis until it is injured."],
  ["It prevents leukocytes from entering tissues anywhere",
   "The endothelium regulates inflammation rather than blocking it outright."],
  ["It stops all molecules crossing the vessel wall",
   "Exchange across the wall is a central vascular function rather than something the endothelium prevents."]],
 "c": 0, "cite": c(12)},

{"topic": "Endothelial cells", "io": IO_MOL, "slot": "mechanism",
 "q": "Which of these is a named synthetic or metabolic property of endothelium?",
 "opts": [
  ["Metabolizing hormones such as angiotensin",
   "Correct, alongside modulating medial smooth muscle tone, regulating inflammation, and affecting the growth of other cell types, particularly smooth muscle cells."],
  ["Synthesizing hemoglobin",
   "Hemoglobin is produced in developing red cells rather than by endothelium."],
  ["Producing bile salts",
   "Bile salt synthesis is hepatic and has nothing to do with the vessel lining."],
  ["Generating action potentials for conduction",
   "Endothelium is not an excitable conducting tissue; its properties are synthetic, metabolic and regulatory."]],
 "c": 0, "cite": c(12)},

{"topic": "Endothelial cells", "io": IO_MOL, "slot": "mechanism",
 "q": "How does endothelium influence vascular resistance?",
 "opts": [
  ["By modulating medial smooth muscle cell tone",
   "Correct. It does not contract itself; it signals to the muscle layer that does, which is why endothelial dysfunction translates into abnormal vascular tone."],
  ["By contracting its own cells to narrow the lumen",
   "Endothelium is not a contractile tissue; the smooth muscle of the media provides the contraction."],
  ["By altering the thickness of the adventitia",
   "The adventitia provides support rather than setting resistance."],
  ["By changing the number of capillaries",
   "Resistance is regulated at the arterioles rather than by capillary number."]],
 "c": 0, "cite": c(12)},

{"topic": "Smooth muscle cells", "io": IO_MOL, "slot": "mechanism",
 "q": "Which layer are smooth muscle cells the predominant element of?",
 "opts": [
  ["The media",
   "Correct, and their dual role is the point: they are important in normal vascular repair AND play a large part in the development of atherosclerosis."],
  ["The intima",
   "The healthy intima is an endothelial monolayer; smooth muscle appears there only as pathology, in intimal thickening."],
  ["The adventitia",
   "The adventitia is loose connective tissue providing support."],
  ["The basement membrane",
   "The basement membrane supports the endothelium rather than being a cellular layer."]],
 "c": 0, "cite": c(12)},

{"topic": "Smooth muscle cells", "io": IO_MOL, "slot": "mechanism",
 "q": "What do vascular smooth muscle cells synthesize?",
 "opts": [
  ["Collagen, elastin, proteoglycans and cytokines",
   "Correct, which is why they are central to both repair and disease: the same synthetic capacity that rebuilds a wall also builds an atherosclerotic plaque. Growth factors too."],
  ["Immunoglobulins",
   "Antibody production belongs to plasma cells rather than to vascular smooth muscle."],
  ["Clotting factors for the plasma",
   "Most clotting factors are hepatic in origin rather than being synthesized by vascular smooth muscle."],
  ["Surfactant",
   "Surfactant is produced by type II pneumocytes in the lung and has no vascular smooth muscle origin."]],
 "c": 0, "cite": c(12)},

{"topic": "Smooth muscle cells", "io": IO_MOL, "slot": "mechanism",
 "q": "What are smooth muscle cells responsible for in response to stimuli?",
 "opts": [
  ["Vasoconstriction or vasodilation",
   "Correct, and they also proliferate when appropriately stimulated, which is the behavior that turns a repair response into a stenotic lesion."],
  ["Phagocytosis of lipid",
   "Lipid uptake is a macrophage behavior in the plaque rather than the named smooth muscle role."],
  ["Production of nitric oxide to relax the vessel",
   "Nitric oxide production is an endothelial function, and its loss is a feature of endothelial dysfunction."],
  ["Maintaining the nonthrombogenic surface",
   "That is an endothelial property, since the endothelium is what contacts the blood."]],
 "c": 0, "cite": c(12)},

{"topic": "Intimal thickening", "io": IO_MOL, "slot": "mechanism",
 "q": "What does vascular injury with endothelial dysfunction or loss stimulate?",
 "opts": [
  ["Smooth muscle recruitment and proliferation into the intima",
   "Correct, and this is the primary pathology of neointimal hyperplasia: cells that belong in the media migrate inward, multiply, and lay down extracellular matrix."],
  ["Complete regeneration of the original wall architecture",
   "The response remodels the wall rather than restoring it, and the remodelling costs lumen."],
  ["Loss of the media with thinning of the whole wall",
   "The intima thickens; the wall is not thinned by this process."],
  ["Immediate calcification of the adventitia",
   "Calcification appears late in atherosclerosis and in Monckeberg sclerosis, not as the initial injury response."]],
 "c": 0, "cite": c(13)},

{"topic": "Intimal thickening", "io": IO_MOL, "slot": "mechanism",
 "q": "Where do replacement endothelial cells come from after injury?",
 "opts": [
  ["Adjacent uninjured areas, or blood precursors",
   "Correct, and the repaired layer is not equivalent to the original: the consequence named is decreased production of nitric oxide."],
  ["Division of the underlying smooth muscle cells",
   "Smooth muscle migrates into the intima but does not become endothelium."],
  ["Transformation of adventitial fibroblasts",
   "The two named sources are adjacent endothelium and blood-borne precursors."],
  ["They are not replaced at all",
   "Replacement does occur, from adjacent uninjured endothelium or from precursor cells circulating in the blood."]],
 "c": 0, "cite": c(13)},

{"topic": "Intimal thickening", "io": IO_MOL, "slot": "mechanism",
 "q": "What is the consequence of endothelial repair for nitric oxide?",
 "opts": [
  ["Its production decreases",
   "Correct, and because nitric oxide is a vasodilator and an inhibitor of platelet adhesion, losing it shifts the vessel toward constriction and thrombosis."],
  ["Its production increases sharply",
   "The change described runs the other way, toward decreased production."],
  ["It is unchanged by injury",
   "Decreased nitric oxide production is specifically named as a consequence."],
  ["It is replaced by carbon monoxide signaling",
   "No such substitution is described; the named consequence is simply decreased nitric oxide production."]],
 "c": 0, "cite": c(13)},

{"topic": "Intimal thickening", "io": IO_MOL, "slot": "mechanism",
 "q": "Which two blood-borne events accompany the neointimal response?",
 "opts": [
  ["Platelet activation and leukocyte recruitment",
   "Correct: a thrombus forms and the inflammatory cascade begins at the injury site, so the response is simultaneously thrombotic and inflammatory."],
  ["Red cell aggregation and hemolysis",
   "Red cell aggregation and hemolysis are not among the named components of the neointimal response."],
  ["Eosinophil degranulation and mast cell activation",
   "The cells named are platelets and leukocytes generally rather than these allergic effectors."],
  ["Plasma cell infiltration with antibody deposition",
   "Immune complex deposition characterizes certain vasculitides rather than the general neointimal response."]],
 "c": 0, "cite": c(13)},

{"topic": "Intimal thickening", "io": IO_MOL, "slot": "consequence",
 "q": "What is the net result of the neointimal response?",
 "opts": [
  ["Intimal thickening that narrows the lumen",
   "Correct, compromising vascular flow. The process involves wall remodelling and loss of lumen patency."],
  ["Widening of the lumen with improved flow",
   "The lumen is narrowed rather than widened by intimal thickening."],
  ["Complete occlusion in every case",
   "Flow is compromised, but the response does not necessarily occlude the vessel outright."],
  ["Rupture of the vessel wall",
   "Rupture is one of the four principal mechanisms of vascular disease, but it is not the result of intimal thickening."]],
 "c": 0, "cite": c(13)},

{"topic": "Intimal thickening", "io": IO_MOL, "slot": "principle",
 "q": "In which forms of vascular damage does the neointimal response occur?",
 "opts": [
  ["Any vascular damage or dysfunction, whatever the cause",
   "Correct, which is what makes it a general principle rather than a feature of one disease &mdash; the wall has a limited repertoire of responses to injury."],
  ["Only in atherosclerosis",
   "Atherosclerosis is one setting, but the response is described as occurring with ANY vascular damage or dysfunction."],
  ["Only after surgical or catheter injury",
   "Procedural injury provokes it, as in in-stent restenosis, but so does damage of any cause."],
  ["Only in vessels already affected by hypertension",
   "No such restriction applies: the response follows any vascular damage or dysfunction, whatever its cause."]],
 "c": 0, "cite": c(14)},

{"topic": "Mechanisms of vascular disease", "io": IO_MOL, "slot": "classification",
 "q": "Which are the four principal mechanisms of vascular disease?",
 "opts": [
  ["Weakening, narrowing, dilation and rupture",
   "Correct, and narrowing itself can be progressive, as in atherosclerosis, or precipitous, as in thrombosis or embolism."],
  ["Inflammation, infection, infarction and ischemia",
   "These are processes that occur in vessels, but they are not the four structural mechanisms named."],
  ["Hypertrophy, atrophy, metaplasia and dysplasia",
   "Those are general cellular adaptations rather than the vascular mechanisms listed."],
  ["Thrombosis, embolism, stasis and reflux",
   "Thrombosis and embolism are routes to narrowing rather than separate principal mechanisms."]],
 "c": 0, "cite": c(16)},

{"topic": "Mechanisms of vascular disease", "io": IO_MOL, "slot": "mechanism",
 "q": "How can narrowing of a vessel lumen arise?",
 "opts": [
  ["Progressively or precipitously",
   "Correct, and the distinction matters because a gradual stenosis allows collateral supply to develop while a sudden one does not. Atherosclerosis narrows progressively; thrombosis or embolism precipitously."],
  ["Only progressively over years",
   "Thrombosis and embolism produce precipitous narrowing, so narrowing is not always a gradual process."],
  ["Only precipitously, as a sudden event",
   "Atherosclerosis narrows the lumen progressively over years, so narrowing is not always a sudden event."],
  ["Only as a consequence of external compression",
   "The mechanisms described are intrinsic to the vessel rather than compressive."]],
 "c": 0, "cite": c(16)},

{"topic": "Anatomic distribution", "io": IO_MOL, "slot": "principle",
 "q": "Why do vascular disorders affect specific types of vessel?",
 "opts": [
  ["Each vessel type is built for its own physiologic needs",
   "Correct, and the consequence is that pathophysiology has distinct anatomic distributions rather than occurring uniformly along the vascular tree."],
  ["Blood flow is identical throughout the circulation",
   "Flow characteristics differ markedly between vessel types, which is part of why the diseases differ."],
  ["All vessels share the same wall structure",
   "They do not: capillaries lack a media entirely, and elastic and muscular arteries differ in composition."],
  ["Disease distribution is random",
   "The distributions are described as distinct and structurally determined."]],
 "c": 0, "cite": c(17)},

{"topic": "Arterial types", "io": IO_ANAT, "slot": "classification",
 "q": "Which disease process affects the large elastic arteries?",
 "opts": [
  ["Aneurysm",
   "Correct, and the mechanism follows the structure: weakening of the vessel resulting from loss of elastic tissue, in vessels whose function depends on elasticity. The aorta is roughly 2 to 3.5 cm."],
  ["Atherosclerosis",
   "Atherosclerosis is assigned to the medium-sized muscular arteries, such as the coronary and renal arteries."],
  ["Hypertensive vessel change",
   "Hypertension acts on the small arteries and arterioles rather than on the aorta."],
  ["Fibromuscular dysplasia",
   "Fibromuscular dysplasia affects medium and large muscular arteries and causes stenosis rather than dilation."]],
 "c": 0, "cite": c(18)},

{"topic": "Arterial types", "io": IO_ANAT, "slot": "classification",
 "q": "Which vessels does atherosclerosis principally affect?",
 "opts": [
  ["Medium-sized muscular arteries",
   "Correct &mdash; the smaller branches of the aorta such as the coronary and renal arteries, roughly 3 to 4 mm. They combine elasticity with musculature to withstand high pulsatile forces and recoil to promote flow."],
  ["Large elastic arteries such as the aorta",
   "The aorta's characteristic lesion is aneurysm, through loss of elastic tissue."],
  ["Small arteries and arterioles within tissues",
   "Small arteries and arterioles within tissues are the vessels affected by hypertension rather than by aneurysm."],
  ["Capillaries",
   "Capillaries have no media and are not the site of atherosclerotic disease."]],
 "c": 0, "cite": c(18)},

{"topic": "Arterial types", "io": IO_MOL, "slot": "mechanism",
 "q": "What does hypertension do to small arteries and arterioles?",
 "opts": [
  ["Mechanical stress and endothelial dysfunction",
   "Correct: decreased elasticity and weakening of the vessel while the lumen stiffens and narrows. Arterioles run 20 to 100 micrometers, small arteries 2 mm or less. The lumen stiffens and narrows."],
  ["Dilation of the lumen with thinning of the wall",
   "The lumen stiffens and narrows under hypertension rather than dilating, and the wall weakens rather than thinning."],
  ["Formation of lipid-laden plaques projecting into the lumen",
   "Atheromas are the lesion of atherosclerosis in muscular arteries."],
  ["Loss of elastic tissue producing aneurysm",
   "Loss of elastic tissue producing aneurysm is the large elastic artery response, seen in the aorta."]],
 "c": 0, "cite": c(18)},

{"topic": "Blood pressure regulation", "io": IO_MOL, "slot": "mechanism",
 "q": "What two quantities determine blood pressure?",
 "opts": [
  ["Vascular resistance and cardiac output",
   "Correct. Resistance is regulated at the arterioles by neural and hormonal input; output is heart rate times stroke volume, with stroke volume influenced by blood volume."],
  ["Blood viscosity and vessel length",
   "Both influence flow in principle, but the two determinants named are resistance and cardiac output."],
  ["Heart rate and respiratory rate",
   "Heart rate contributes through cardiac output, but respiratory rate is not one of the determinants."],
  ["Hemoglobin concentration and oxygen saturation",
   "Hemoglobin concentration and oxygen saturation determine oxygen carriage rather than arterial pressure."]],
 "c": 0, "cite": c(19)},

{"topic": "Blood pressure regulation", "io": IO_MOL, "slot": "mechanism",
 "q": "What regulates vascular resistance?",
 "opts": [
  ["The arterioles, by neural and hormonal input",
   "Correct, and it is described as a delicate balance between vasoconstrictors and vasodilators rather than a single controlling signal."],
  ["The capillaries, by altering their permeability",
   "Capillaries exchange substances; they do not set systemic resistance."],
  ["The veins, by varying their capacitance",
   "Venous capacitance holds the reservoir volume rather than setting arterial resistance."],
  ["The adventitia, by contracting around the vessel",
   "The adventitia is supportive connective tissue and is not contractile."]],
 "c": 0, "cite": c(19)},

{"topic": "Blood pressure regulation", "io": IO_MOL, "slot": "mechanism",
 "q": "What determines stroke volume, and therefore part of cardiac output?",
 "opts": [
  ["Blood volume",
   "Correct &mdash; sodium excretion or resorption sets the volume, which is why renal sodium handling sits at the center of blood pressure regulation. It is regulated by sodium excretion or resorption."],
  ["The diameter of the arterioles",
   "Arteriolar diameter sets resistance rather than stroke volume."],
  ["The number of capillaries in the tissue",
   "Capillary density reflects metabolic demand rather than determining stroke volume."],
  ["The elasticity of the adventitia",
   "The adventitia is supportive tissue and does not determine ejected volume."]],
 "c": 0, "cite": c(19)},

{"topic": "Renin-angiotensin", "io": IO_MOL, "slot": "mechanism",
 "q": "What triggers renin secretion?",
 "opts": [
  ["A fall in pressure in the afferent arterioles",
   "Correct. The kidney senses the pressure drop at the afferent arteriole and responds, which is the first step of the sequence that restores it."],
  ["A rise in pressure in the afferent arterioles",
   "Renin is secreted in response to a DECREASE in blood pressure rather than an increase."],
  ["A rise in plasma sodium concentration",
   "The described trigger is the pressure change at the afferent arteriole."],
  ["Direct sympathetic stimulation of the adrenal medulla",
   "Renin comes from the kidney, and the named trigger is the afferent arteriolar pressure."]],
 "c": 0, "cite": c(19)},

{"topic": "Renin-angiotensin", "io": IO_MOL, "slot": "mechanism",
 "q": "What does renin act on, and to produce what?",
 "opts": [
  ["It cleaves angiotensinogen to angiotensin I",
   "Correct, and endothelial catabolism then produces angiotensin II from it &mdash; the endothelium is a participant in the pathway rather than a bystander."],
  ["It cleaves angiotensin I to angiotensin II",
   "That conversion is performed by endothelial catabolism rather than by renin itself."],
  ["It stimulates aldosterone directly from the adrenal cortex",
   "Aldosterone secretion is stimulated by angiotensin II, downstream of renin."],
  ["It converts angiotensin II into aldosterone",
   "Angiotensin II is a peptide that signals for aldosterone rather than being converted into it."]],
 "c": 0, "cite": c(19)},

{"topic": "Renin-angiotensin", "io": IO_MOL, "slot": "mechanism",
 "q": "By what two routes does angiotensin II raise blood pressure?",
 "opts": [
  ["Raising smooth muscle tone, and driving aldosterone",
   "Correct &mdash; one route acts on resistance immediately, the other on volume through increased renal sodium resorption, so both determinants of pressure are addressed."],
  ["Raising heart rate and respiratory rate",
   "Respiratory rate plays no part, and the described routes are vascular tone and aldosterone."],
  ["Increasing red cell mass and blood viscosity",
   "Increasing red cell mass and blood viscosity are not among the described actions of angiotensin II."],
  ["Dilating the efferent arteriole to raise filtration",
   "Angiotensin II is a vasoconstrictor, and the routes named are smooth muscle tone and aldosterone."]],
 "c": 0, "cite": c(19)},
]
