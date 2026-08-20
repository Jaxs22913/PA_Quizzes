# Principles of Diagnostic Medicine I, Lecture 2 (Principles of Medical Imaging) — pool B.
# Nuclear medicine, ultrasonography, magnetic resonance imaging and the
# angiographic studies. Syllabus objectives b(ii), b(iv)-(viii), c, f, h.
#
# Same two Reynolds rules as pool A, asserted in the partition script: a number
# never appears without the scale that makes it readable, and nothing asks the
# student to calculate.
#
# OBJECTIVE C WITHOUT SLIDE 34. Slide 34 pairs seventeen modality entries against
# six anatomical categories in two columns and the pairing does not survive text
# extraction. Every structure-to-modality claim below instead comes from a slide
# that states it in a sentence -- 23, 24, 27, 30, 41, 42, 43, 60 and 61.
#
# Every question carries slot="..." per the fact-slot standard.
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "2. svPrinciples of Medical Imaging.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOB = "Objective b — Describe the function and clinical applications of radiography, ultrasonography, computed tomography, magnetic resonance imaging, magnetic resonance angiography, positron emission tomography, single photon emission computed tomography and angiographic studies"
IOC = "Objective c — Discuss anatomical structures best visualized by each imaging modality"
IOF = "Objective f — Compare and contrast the risks and benefits associated with radiation exposure"
IOH = "Objective h — Discuss contraindications and safety considerations of commonly used imaging modalities"

POOL_B = [
 dict(topic="Nuclear medicine", io=IOB, slot="etiology",
   q="What does a positron emission tomography scanner use in place of an x-ray tube?",
   opts=[
     ["A gamma camera, recording emissions from an injected dye in two dimensions",
      "Correct — the radiation comes from the patient, not from the machine."],
     ["A rotating fan beam, recording transmission through the patient at thousands of points",
      "That describes computed tomography, which does transmit a beam through the patient."],
     ["A transducer, recording high-frequency sound waves reflected back from the tissue",
      "That describes ultrasonography, which uses no ionizing radiation at all."],
     ["A varying magnetic field, recording radio waves emitted as hydrogen atoms realign",
      "That describes magnetic resonance imaging, which is a hydrogen map."]],
   c=0, cite=c(16)),

 dict(topic="Nuclear medicine", io=IOB, slot="agent/regimen",
   q="Which tracer does positron emission tomography typically use, and why that one?",
   opts=[
     ["Fluorodeoxyglucose-18, a radioactive glucose, because tumours have a higher metabolic rate",
      "Correct — the scan asks which tissues are consuming more glucose."],
     ["Technetium-99, a metastable isotope, because tumours retain it far longer than normal tissue",
      "Technetium-99 is the usual single photon emission tomography agent, tracking blood flow."],
     ["Iodixanol, an iso-osmolal agent, because tumours take up iodine more avidly than muscle",
      "Iodixanol is an intravascular iodinated contrast for angiography, not a nuclear tracer."],
     ["Gadolinium, a paramagnetic metal, because tumours disrupt the local magnetic environment",
      "Gadolinium is the magnetic resonance contrast agent and emits no radiation."]],
   c=0, cite=c(55)),

 dict(topic="Nuclear medicine", io=IOB, slot="differential",
   q="What does single photon emission computed tomography measure, and what does it show?",
   opts=[
     ["Single photons on rotating gamma cameras, giving three-dimensional images of where blood flows",
      "Correct — the deck's stated indication is seeing where blood flows to."],
     ["Paired positrons on a stationary gamma camera, giving two-dimensional images of glucose uptake",
      "Positrons and glucose uptake are positron emission tomography, not this study."],
     ["Reflected sound on a hand-held transducer, giving real-time images of moving structures",
      "Reflected sound in real time is ultrasonography, which injects no tracer."],
     ["Attenuated x-rays on a rotating detector ring, giving cross-sectional images by density",
      "Attenuation by density is computed tomography, which measures the beam it transmits."]],
   c=0, cite=c(16)),

 dict(topic="Nuclear medicine", io=IOB, slot="differential",
   q="How do the stated indications for single photon emission tomography and positron emission tomography differ?",
   opts=[
     ["Single photon for heart disease, bone scans and brain evaluations; positron for cancer staging, brain disorders and cardiac blood flow",
      "Correct — both reach the heart and brain, but staging cancer is the positron study."],
     ["Single photon for cancer staging, brain disorders and cardiac blood flow; positron for heart disease, bone scans and brain evaluations",
      "This reverses the two lists; cancer staging is named under positron emission tomography."],
     ["Single photon for soft tissue masses, ligaments and tendons; positron for pleural effusion, free air and bowel obstruction",
      "Those are magnetic resonance and plain radiography indications, not nuclear medicine ones."],
     ["Single photon for obstetrics, vasculature and cardiac motion; positron for kidney stones, fractures and foreign bodies",
      "Those are ultrasound and plain radiography indications, and neither uses a tracer."]],
   c=0, cite=c(17)),

 dict(topic="Nuclear medicine", io=IOB, slot="manifestation",
   q="What is a positron?",
   opts=[
     ["A particle of roughly the same mass as an electron, but carrying the opposite, positive charge",
      "Correct — that is the deck's definition, and the reason for the name."],
     ["A photon of roughly the same energy as an x-ray, but emitted by the patient rather than a tube",
      "The emission is a particle rather than a photon; single photons are the other study."],
     ["A proton of roughly the same mass as a neutron, but bound within an unstable atomic nucleus",
      "A positron is far lighter than a proton and is not a nuclear constituent."],
     ["An isotope of roughly the same behaviour as technetium, but with a much shorter half-life",
      "A positron is a subatomic particle, not an isotope of any element."]],
   c=0, cite=c(17)),

 dict(topic="Nuclear medicine", io=IOF, slot="avoid",
   q="Which imaging devices does the deck flag as the highest-emitting currently in existence?",
   opts=[
     ["Computed tomography, positron emission tomography and single photon emission tomography",
      "Correct — the deck marks this IMPORTANT, and all three use ionizing radiation."],
     ["Conventional radiography, fluoroscopy and the angiographic studies performed with x-rays",
      "These do use ionizing radiation, but the deck calls plain films relatively low dose."],
     ["Magnetic resonance imaging, magnetic resonance angiography and magnetic resonance venography",
      "None of the magnetic resonance studies emit ionizing radiation at all."],
     ["Ultrasonography, colour Doppler ultrasonography and the hand-held bedside ultrasound units",
      "Ultrasound uses sound waves and is called the safest of these modalities."]],
   c=0, cite=c(17)),

 dict(topic="Nuclear medicine", io=IOF, slot="education",
   q="What is unique about radiation exposure in nuclear medicine compared with other modalities that use ionizing radiation?",
   opts=[
     ["The patient can briefly become the source of radiation exposure to other people",
      "Correct — the tracer is inside the patient, so the emission travels with them."],
     ["The exposure is delivered entirely in a single pulse rather than over a continuous scan",
      "Exposure duration is not the distinction the deck draws for nuclear medicine."],
     ["The exposure is confined to the organ being studied rather than reaching adjacent tissue",
      "A tracer distributes systemically; it is not confined to the target organ."],
     ["The exposure is measured in different units from those used for conventional radiography",
      "Radiation is measured in the same units, milli Sieverts and milli Grays, throughout."]],
   c=0, cite=c(61)),

 dict(topic="Nuclear medicine", io=IOB, slot="test finding",
   q="On a bone scan, why are the kidneys visible?",
   opts=[
     ["Uptake in the kidneys is normal, and the same is true of tracer on positron emission scans",
      "Correct — the deck labels renal uptake normal on both studies."],
     ["Uptake in the kidneys indicates the tracer dose given was higher than the study required",
      "Renal visibility is expected and says nothing about the dose administered."],
     ["Uptake in the kidneys suggests metastatic disease has reached the retroperitoneal organs",
      "Normal renal uptake is not a finding of metastasis on either study."],
     ["Uptake in the kidneys occurs only when renal function is impaired and clearance is slowed",
      "Normal kidneys take up and clear the tracer; impairment is not required."]],
   c=0, cite=c(18)),

 dict(topic="Ultrasonography", io=IOB, slot="etiology",
   q="How does ultrasonography generate an image?",
   opts=[
     ["High-frequency sound waves leave the transducer, bounce off tissue and return to it",
      "Correct — the transducer is both the source and the receiver."],
     ["High-energy x-ray photons leave the tube, pass through tissue and strike a detector",
      "That is radiography; ultrasound uses no ionizing radiation whatsoever."],
     ["High-strength magnetic fields align hydrogen, which emits radio waves on release",
      "That is magnetic resonance imaging, which images hydrogen rather than sound."],
     ["High-metabolism tissues concentrate injected tracer, which emits gamma radiation",
      "That is nuclear medicine, and it requires an injected radioactive agent."]],
   c=0, cite=c(23)),

 dict(topic="Ultrasonography", io=IOB, slot="first-line",
   q="What are ultrasonography's stated indications?",
   opts=[
     ["Assessment of moving structures, naming the heart, the vasculature and obstetrics",
      "Correct — it records in real time, which is what suits it to motion."],
     ["Assessment of bony structures, naming the skull, the vertebrae and the long bones",
      "Ultrasound cannot penetrate bone, so these are radiographic or tomographic studies."],
     ["Assessment of aerated structures, naming the lungs, the sinuses and the bowel gas pattern",
      "Large gas-filled structures disrupt the signal, which is a stated limitation."],
     ["Assessment of metabolic activity, naming tumour staging, brain function and perfusion",
      "Metabolic activity is what the nuclear medicine studies are indicated for."]],
   c=0, cite=c(23)),

 dict(topic="Ultrasonography", io=IOB, slot="test finding",
   q="What does the colour Doppler setting add to a standard ultrasound image?",
   opts=[
     ["Direction of flow and velocity, on an image otherwise made of white, grey and black",
      "Correct — colour is the flow overlay, and blood is what it is used for."],
     ["Depth of penetration and resolution, on an image otherwise limited to superficial planes",
      "Colour Doppler does not extend depth; poor deep visualisation remains a limitation."],
     ["Density in Hounsfield units and windowing, on an image otherwise showing five densities",
      "Hounsfield units and windowing belong to computed tomography, not to ultrasound."],
     ["Metabolic uptake and intensity, on an image otherwise showing only anatomical structure",
      "Uptake displayed by intensity is how the positron emission studies are read."]],
   c=0, cite=c(23)),

 dict(topic="Ultrasonography", io=IOH, slot="avoid",
   q="Which limitations are named for ultrasonography?",
   opts=[
     ["It cannot penetrate bone, large gas-filled structures disrupt the signal, deeper structures are hard to see, and it is operator-dependent",
      "Correct — all four are listed together as the disadvantages."],
     ["It cannot be made portable, the equipment cost is high, a dedicated room is required, and the study is time consuming",
      "Those are the magnetic resonance disadvantages; ultrasound is portable and inexpensive."],
     ["It cannot be used in pregnancy, the dose to the fetus is high, shielding is required, and exposure accumulates",
      "The opposite is true: no radiation, so it is the study of choice in pregnancy."],
     ["It cannot resolve soft tissue, only five densities are visible, structures overlap, and the range is limited",
      "Those are the limitations of conventional radiography, not of ultrasound."]],
   c=0, cite=c(24)),

 dict(topic="Ultrasonography", io=IOC, slot="initial test",
   q="In which patients is ultrasound named as often the first study of choice?",
   opts=[
     ["Female pelvis and paediatric patients, and it is also used to guide procedures",
      "Correct — no radiation is the reason it leads in both groups."],
     ["Adult chest and geriatric patients, and it is also used to screen for fractures",
      "Air in the lung and bone both defeat ultrasound; these are radiographic studies."],
     ["Head-injured and intoxicated patients, and it is also used to exclude a bleed",
      "Intracranial haemorrhage is a computed tomography question in the adult skull."],
     ["Oncology and post-operative patients, and it is also used to stage known disease",
      "Staging is a computed tomography and positron emission tomography role."]],
   c=0, cite=c(24)),

 dict(topic="Ultrasonography", io=IOH, slot="prognosis",
   q="How does the deck summarise ultrasound's safety?",
   opts=[
     ["Very safe, without any known major side effects at medically diagnostic levels",
      "Correct — it is called the safest of these modalities."],
     ["Broadly safe, though a cumulative dose limit applies across repeated examinations",
      "There is no cumulative dose, because there is no ionizing radiation."],
     ["Safe in adults, though it is avoided in pregnancy and in infants as a precaution",
      "That caution is stated for magnetic resonance imaging, not for ultrasound."],
     ["Safe once screened, though implanted metallic devices must be excluded beforehand",
      "Implanted-device screening is a magnetic resonance requirement."]],
   c=0, cite=c(24)),

 dict(topic="Magnetic resonance imaging", io=IOB, slot="etiology",
   q="How are magnetic resonance images generated?",
   opts=[
     ["A varying magnetic field aligns hydrogen atoms; releasing it produces radio waves the computer maps",
      "Correct — the deck calls the resulting images essentially hydrogen maps."],
     ["A varying magnetic field aligns iron atoms; releasing it produces heat the computer measures",
      "Hydrogen is the nucleus imaged, and the signal read out is radiofrequency, not thermal."],
     ["A rotating x-ray beam passes through tissue; detectors measure how much of it is absorbed",
      "That is computed tomography, which is why it uses ionizing radiation and this does not."],
     ["A pulse of sound leaves the transducer; the echo returning from tissue is timed and plotted",
      "That is ultrasonography, and it needs no magnetic field of any kind."]],
   c=0, cite=c(26)),

 dict(topic="Magnetic resonance imaging", io=IOB, slot="manifestation",
   q="What determines the frequency of the radio waves a magnetic resonance scanner reads?",
   opts=[
     ["The chemical environment of the hydrogen atoms, together with their location",
      "Correct — both, which is what lets the computer build a spatial map."],
     ["The strength of the magnet in Tesla, together with the duration of the scan",
      "Field strength changes image quality, but it is not what the deck names here."],
     ["The density of the tissue in Hounsfield units, together with the chosen window",
      "Hounsfield units and windows belong to computed tomography."],
     ["The metabolic rate of the tissue, together with the dose of tracer given",
      "Metabolic rate and tracer dose describe nuclear medicine studies."]],
   c=0, cite=c(26)),

 dict(topic="Magnetic resonance imaging", io=IOB, slot="test finding",
   q="On a T2-weighted image, how does tissue with high water content appear?",
   opts=[
     ["Bright, and the examples given are fat, oedema, infection, blood and cerebrospinal fluid",
      "Correct — remember T2 as the sequence where water is white."],
     ["Dark, and the examples given are fat, oedema, infection, blood and cerebrospinal fluid",
      "That is the T1-weighted image; the same list simply inverts between the two."],
     ["Bright, and the examples given are cortical bone, tendon, ligament and calcified plaque",
      "Those are low in water and in signal, and calcium emits no signal at all."],
     ["Dark, and the examples given are cortical bone, tendon, ligament and calcified plaque",
      "This is true of those tissues but does not answer what high water content does."]],
   c=0, cite=c(28)),

 dict(topic="Magnetic resonance imaging", io=IOB, slot="test finding",
   q="On a T1-weighted image, how does tissue with low water content appear?",
   opts=[
     ["Bright, which is the reverse of the same tissue on a T2-weighted image",
      "Correct — on T1, low water is white and high water is dark."],
     ["Dark, which is the same as that tissue would appear on a T2-weighted image",
      "Low water content is dark on T2, and T1 reverses it rather than repeating it."],
     ["Bright, which is the same as that tissue would appear on a T2-weighted image",
      "The two weightings invert; they do not agree on low water content."],
     ["Dark, which is the reverse of the same tissue on a T2-weighted image",
      "This inverts both halves of the answer and is wrong on each."]],
   c=0, cite=c(28)),

 dict(topic="Magnetic resonance imaging", io=IOC, slot="first-line",
   q="Which tissues is magnetic resonance imaging described as the best modality for?",
   opts=[
     ["Soft tissue, essentially anything other than bone, with extremely high anatomical detail",
      "Correct — the deck states it in exactly those terms."],
     ["Bone and calcified structures, essentially anything mineralised, with high spatial detail",
      "Calcium emits no signal on magnetic resonance, which is the opposite of this claim."],
     ["Air-containing structures, essentially the lungs and sinuses, with high contrast detail",
      "Aerated structures are a radiographic and tomographic strength, not this one."],
     ["Metabolically active tissue, essentially tumour and infection, with high functional detail",
      "Metabolic activity is what the nuclear medicine studies are indicated for."]],
   c=0, cite=c(27)),

 dict(topic="Magnetic resonance imaging", io=IOC, slot="first-line",
   q="Why can magnetic resonance imaging show tissues that are surrounded by bone better than computed tomography can?",
   opts=[
     ["Calcium emits no signal, so the bone does not obscure what sits inside it",
      "Correct — silence from calcium is an advantage rather than a gap."],
     ["Calcium emits a strong signal, so the bone can be subtracted from the image afterwards",
      "Calcium is silent on magnetic resonance; there is no strong signal to subtract."],
     ["Bone is windowed out during acquisition, so only the soft tissue range is displayed",
      "Windowing is a computed tomography display technique, not a magnetic resonance one."],
     ["Bone absorbs the radio waves, so the surrounding soft tissue returns a relatively brighter signal",
      "Bone does not absorb the radiofrequency signal in the way this describes."]],
   c=0, cite=c(30)),

 dict(topic="Magnetic resonance imaging", io=IOC, slot="first-line",
   q="Which programmable magnetic resonance technique is named as useful in stroke?",
   opts=[
     ["Diffusion-weighted imaging, which evaluates the diffusion of water within tissue",
      "Correct — the scanner can also be programmed to evaluate blood velocity."],
     ["Fat-suppressed imaging, which removes the signal from adipose tissue in the field",
      "Fat suppression is not the technique the deck names for stroke."],
     ["Post-processing windowing, which re-displays the raw data over a narrower range",
      "Post-processing and windowing are computed tomography techniques."],
     ["Gadolinium-enhanced imaging, which highlights vascular structures after injection",
      "Contrast enhancement is used for tumours and masses rather than for stroke here."]],
   c=0, cite=c(30)),

 dict(topic="Magnetic resonance imaging", io=IOH, slot="avoid",
   q="Which safety issues are named for magnetic resonance imaging?",
   opts=[
     ["Magnetic implanted devices and ferromagnetic projectiles, and it is still not recommended in pregnancy or infants",
      "Correct — no radiation is emitted, but the magnet itself creates hazards."],
     ["Cumulative ionizing dose and radiation-sensitive organs, and it is still not recommended in pregnancy or infants",
      "Magnetic resonance emits no ionizing radiation, so there is no dose to accumulate."],
     ["Nephrotoxicity and anaphylaxis to iodine, and it is still not recommended in renal impairment",
      "Iodinated contrast belongs to computed tomography; this study uses gadolinium."],
     ["Operator dependence and poor penetration of bone, and it is still not recommended in obesity",
      "Those are ultrasound limitations rather than magnetic resonance safety issues."]],
   c=0, cite=c(27)),

 dict(topic="Magnetic resonance imaging", io=IOB, slot="avoid",
   q="What is the stated trade-off of an open magnetic resonance scanner?",
   opts=[
     ["Decreased quality of imaging, which is the price paid for the open configuration",
      "Correct — it is available, but the deck flags the loss of quality."],
     ["Increased scan duration, which is the price paid for the open configuration",
      "Time is listed as a general disadvantage, not as the open scanner's trade-off."],
     ["Increased radiation dose, which is the price paid for the open configuration",
      "No magnetic resonance scanner emits ionizing radiation, open or closed."],
     ["Decreased soft tissue contrast only, with spatial resolution otherwise preserved",
      "The deck says quality generally, without limiting it to soft tissue contrast."]],
   c=0, cite=c(27)),

 dict(topic="Magnetic resonance imaging", io=IOC, slot="first-line",
   q="Where is magnetic resonance imaging described as most widely used?",
   opts=[
     ["Neuro-imaging, and the soft tissues of orthopaedics such as muscle, ligament and tendon",
      "Correct — the key points call it the cornerstone of neuroimaging."],
     ["Cross-sectional imaging generally, where it has become the foundation of practice",
      "That description belongs to computed tomography, not magnetic resonance."],
     ["Emergency imaging, where speed and portability determine the choice of modality",
      "It is time consuming and not portable, which rules it out of that role."],
     ["Screening imaging, where wide availability and low cost determine the choice",
      "It is expensive and not widely available, which is stated as a disadvantage."]],
   c=0, cite=c(30)),

 dict(topic="Angiographic studies", io=IOB, slot="manifestation",
   q="What is a vasculogram?",
   opts=[
     ["Not one specific test — any of the modalities can be used to image the vessels",
      "Correct — x-ray, ultrasound, computed tomography and magnetic resonance all can."],
     ["A specific x-ray study in which iodine is injected directly into a peripheral vein",
      "Angiographic studies are not confined to one modality or one route."],
     ["A specific nuclear study in which technetium is used to map perfusion to an organ",
      "Perfusion tracers are used in nuclear medicine, but that is not what this term means."],
     ["A specific ultrasound study in which the transducer is placed within the vessel",
      "Intravascular placement is not what the deck describes for these studies."]],
   c=0, cite=c(32)),

 dict(topic="Angiographic studies", io=IOB, slot="differential",
   q="How do computed tomography angiography and magnetic resonance angiography differ in their use of dye?",
   opts=[
     ["Computed tomography angiography injects iodine quickly; magnetic resonance angiography needs no dye",
      "Correct — magnetic resonance angiography images the arterial walls without contrast."],
     ["Computed tomography angiography needs no dye; magnetic resonance angiography injects gadolinium quickly",
      "This reverses them; the iodinated injection belongs to the computed tomography study."],
     ["Both inject iodine, but computed tomography angiography uses a much lower concentration",
      "Magnetic resonance angiography is performed without contrast, so both do not inject."],
     ["Neither injects dye, because both reconstruct the vessels from the raw data afterwards",
      "The computed tomography study does require a rapid iodinated injection."]],
   c=0, cite=c(32)),

 dict(topic="Angiographic studies", io=IOB, slot="manifestation",
   q="Which term names an angiographic study of the veins rather than the arteries?",
   opts=[
     ["Venogram, performed as either a magnetic resonance venogram or a computed tomography venogram",
      "Correct — the same modalities, aimed at the venous side."],
     ["Doppler study, performed as either a colour Doppler examination or a duplex examination",
      "Colour Doppler shows flow in either vessel type; it is not the venous-specific term."],
     ["Coronary angiogram, performed as either a diagnostic catheterisation or an intervention",
      "The coronary angiogram is the x-ray-based arterial study of the heart."],
     ["Arthrogram, performed as either a computed tomography arthrogram or a magnetic one",
      "An arthrogram is contrast injected into a joint, not a vascular study at all."]],
   c=0, cite=c(32)),

 dict(topic="Fluoroscopy", io=IOB, slot="manifestation",
   q="What does fluoroscopy let a clinician evaluate?",
   opts=[
     ["Motion of body parts and positioning changes of bones and joints, viewed in real time",
      "Correct — real-time visualisation is the point of the study."],
     ["Metabolic activity in organs and tissues, viewed as intensities after tracer injection",
      "Intensity mapping of uptake is a nuclear medicine study rather than fluoroscopy."],
     ["Water content in soft tissue and oedema, viewed on differently weighted sequences",
      "Weighted sequences and water content belong to magnetic resonance imaging."],
     ["Direction and velocity of blood flow, viewed as colour superimposed on grey scale",
      "Colour flow mapping is the Doppler setting on an ultrasound machine."]],
   c=0, cite=c(57)),
]
