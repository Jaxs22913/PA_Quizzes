# Principles of Diagnostic Medicine I, Lecture 2 (Principles of Medical Imaging) — pool A.
# Fundamental properties, conventional radiography, densities, and computed tomography.
# Syllabus objectives a, b(i), b(iii), d, f.
#
# PROFESSOR REYNOLDS' RULES, carried forward from the 2026-08-18 Lecture 1
# recording and asserted in the partition script:
#   - No question may present a numeric value without the context needed to
#     read it. Hounsfield numbers appear WITH their scale.
#   - "We're not gonna do math." No question asks the student to calculate.
#
# NO AUDIO EXISTED for this lecture when the pool was written, so nothing here
# is weighted by spoken emphasis -- only by what the deck spends slides on.
#
# Slide 34 ("Anatomical Structures Best Visualized by...") is DELIBERATELY NOT
# used. Its two columns extract as seventeen modality entries against six
# categories and the pairing cannot be reconstructed reliably from the text. The
# modality-to-structure claims here come from the slides that state them outright.
#
# Every question carries slot="..." per the fact-slot standard.
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "2. svPrinciples of Medical Imaging.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "a — Identify the fundamental properties of medical imaging"
IOB = "b — Describe the function and clinical applications of radiography, ultrasonography, computed tomography, magnetic resonance imaging, magnetic resonance angiography, positron emission tomography, single photon emission computed tomography and angiographic studies"
IOD = "d — Compare and contrast the concepts of radiographic density and contrast"
IOF = "f — Compare and contrast the risks and benefits associated with radiation exposure"

POOL_A = [
 dict(topic="History", io=IOA, slot="etiology",
   q="Who discovered x-rays, and what recognition followed?",
   opts=[
     ["Wilhelm Roentgen, in Germany in 1895, awarded the first Nobel Prize for Physics in 1901",
      "Correct — the technique is still called roentgenography after him."],
     ["Godfrey Hounsfield, in Britain in 1972, awarded the Nobel Prize for Medicine in 1979",
      "He developed the first computed tomography scanner, with Allan Cormack."],
     ["Allan Cormack, in South Africa in 1963, awarded the first Nobel Prize for Physics",
      "He shared the 1979 Medicine prize for computed tomography."],
     ["Marie Curie, in France in 1898, awarded the Nobel Prize for Physics in 1903",
      "Her work was on radioactivity rather than the discovery of x-rays."]],
   c=0, cite=c(4)),

 dict(topic="Diagnostic approach", io=IOA, slot="first-line",
   q="Which four questions frame the choice of an imaging modality?",
   opts=[
     ["Which modality best rules the diagnosis in or out, is there a lower-radiation alternative, what is the risk against benefit for this patient, and is contrast needed",
      "Correct — those are the four the lecture opens with."],
     ["Which modality is cheapest, which is fastest, which is closest, and which the patient prefers",
      "Cost and availability matter but are not the framing questions given."],
     ["Which modality the radiologist prefers, which is available today, which the insurer covers, and which is quickest",
      "Those are practical constraints rather than the diagnostic framing."],
     ["Which modality gives the highest resolution, the largest field of view, the thinnest slices, and the fastest overall scan time for the patient",
      "Technical parameters are not the framing questions given."]],
   c=0, cite=c(3)),

 dict(topic="Conventional radiography", io=IOB, slot="etiology",
   q="How is a conventional radiograph produced?",
   opts=[
     ["Ionizing radiation and light strike a photosensitive surface, producing a latent image that is then processed to become visible",
      "Correct — it requires a source, a method to record the image, and a way to process it."],
     ["High-frequency sound waves bounce off the tissue and return to a transducer, which then builds up the whole image",
      "That describes ultrasound."],
     ["A magnetic field aligns hydrogen atoms, which emit radio waves when the field is released",
      "That describes magnetic resonance imaging."],
     ["A gamma camera detects photons emitted by an injected radioisotope within the patient",
      "That describes nuclear medicine imaging."]],
   c=0, cite=c(6)),

 dict(topic="Conventional radiography", io=IOB, slot="manifestation",
   q="What defines a conventional radiograph as distinct from other x-ray studies?",
   opts=[
     ["It uses ionizing radiation without any added contrast material such as barium or iodine",
      "Correct — adding contrast makes it a different study."],
     ["It uses ionizing radiation together with an intravenous iodinated contrast agent",
      "Added contrast is what a conventional radiograph lacks."],
     ["It uses no ionizing radiation at all and relies on acoustic properties instead",
      "That describes ultrasound."],
     ["It uses a rotating fan beam and computer reconstruction into cross-sections",
      "That describes computed tomography."]],
   c=0, cite=c(6)),

 dict(topic="Conventional radiography", io=IOB, slot="first-line",
   q="Which advantages are named for conventional radiography?",
   opts=[
     ["Quick, inexpensive, and obtainable anywhere — the most widely obtained imaging studies",
      "Correct. Machines can also be made portable."],
     ["The widest range of densities of any modality, with excellent soft tissue detail",
      "Its range of densities is limited, which is one of its disadvantages."],
     ["No ionizing radiation, making it the safest of the imaging modalities",
      "That describes ultrasound."],
     ["Three-dimensional reconstruction from multiple sections with digital processing",
      "That describes computed tomography."]],
   c=0, cite=c(7)),

 dict(topic="Conventional radiography", io=IOF, slot="avoid",
   q="Which disadvantages are named for conventional radiography?",
   opts=[
     ["A limited range of densities and reliance on ionizing radiation, though at relatively low dose",
      "Correct — the dose is low compared with other radiographic modalities."],
     ["Operator dependence and an inability to penetrate bone or large gas-filled structures",
      "Those are the disadvantages of ultrasound."],
     ["Long scan times and safety problems with magnetic implanted devices",
      "Those are the disadvantages of magnetic resonance imaging."],
     ["Very high radiation dose and an inability to be made portable at all",
      "The dose is described as relatively low and the machines can be portable."]],
   c=0, cite=c(7)),

 dict(topic="Densities", io=IOD, slot="manifestation",
   q="What are the five basic radiographic densities, ordered from whitest to blackest?",
   opts=[
     ["Metal, calcium (bone), fluid (soft tissue), fat, air",
      "Correct — metal usually absorbs all x-rays and air absorbs the least."],
     ["Air, fat, fluid (soft tissue), calcium (bone), metal",
      "That is the same list reversed — blackest to whitest."],
     ["Calcium, metal, fat, fluid (soft tissue), air",
      "Metal is whiter than calcium, and fat is darker than fluid."],
     ["Metal, fluid (soft tissue), calcium (bone), air, fat",
      "Calcium is denser than fluid, and fat is lighter than air on the scale."]],
   c=0, cite=c(60)),

 dict(topic="Densities", io=IOD, slot="manifestation",
   q="Which density appears blackest on a conventional radiograph, and why?",
   opts=[
     ["Air, because it absorbs the least x-rays",
      "Correct — greater passage of photons means a darker image."],
     ["Metal, because it absorbs the most x-rays of any material",
      "Metal usually absorbs all x-rays and appears whitest."],
     ["Calcium, because it is the densest naturally occurring material",
      "Calcium absorbs most x-rays and appears near-white."],
     ["Fat, because it is less dense than the surrounding soft tissue",
      "Fat is grey and somewhat darker than soft tissue, but not blackest."]],
   c=0, cite=c(8)),

 dict(topic="Densities", io=IOD, slot="differential",
   q="Which two of the five basic densities cannot be distinguished from one another on a conventional radiograph?",
   opts=[
     ["Fluid and soft tissue, which have the same density",
      "Correct — that limitation is one reason computed tomography expands the grey scale."],
     ["Fat and air, which both appear black on the image",
      "Fat is grey and somewhat darker than soft tissue, while air is blackest."],
     ["Calcium and metal, which both absorb all of the beam",
      "Metal usually absorbs all x-rays while calcium absorbs most; they are distinguishable."],
     ["Fat and calcium, which occupy adjacent points on the scale",
      "They sit at opposite ends of the middle range and are distinguishable."]],
   c=0, cite=c(8)),

 dict(topic="Densities", io=IOD, slot="manifestation",
   q="Which density is described as the most dense naturally occurring material?",
   opts=[
     ["Calcium",
      "Correct — it absorbs most x-rays, though metal absorbs essentially all of them."],
     ["Metal",
      "Metal is denser but is not naturally occurring in the body."],
     ["Fluid",
      "Fluid and soft tissue share a middle density."],
     ["Fat",
      "Fat is less dense than soft tissue."]],
   c=0, cite=c(8)),

 dict(topic="Radiodensity", io=IOD, slot="manifestation",
   q="What do the terms radiolucent and hypodense describe?",
   opts=[
     ["A darker image, from greater passage of x-ray photons through the tissue and therefore less absorption",
      "Correct — radiopaque and hyperdense describe the opposite."],
     ["A whiter image, from less passage of x-ray photons through the tissue and therefore greater absorption",
      "That describes radiopaque or hyperdense tissue."],
     ["A brighter signal on a T2-weighted magnetic resonance image of the same tissue",
      "That terminology belongs to magnetic resonance imaging."],
     ["A region of increased uptake of an injected radioisotope on nuclear imaging",
      "That terminology belongs to nuclear medicine."]],
   c=0, cite=c(9)),

 dict(topic="Radiodensity", io=IOD, slot="manifestation",
   q="Which term describes tissue that appears white because it absorbs more of the beam?",
   opts=[
     ["Radiopaque, also called hyperdense or radiodense",
      "Correct — less passage of x-ray photons produces the whiter appearance."],
     ["Radiolucent, also called hypodense",
      "That describes darker tissue with greater photon passage."],
     ["Isodense, matching the density of the surrounding tissue",
      "That term is not the one for a white appearance."],
     ["Attenuated, meaning the beam has been scattered away",
      "Increased attenuation is a computed tomography term for the same idea."]],
   c=0, cite=c(9)),

 dict(topic="Radiation units", io=IOF, slot="manifestation",
   q="In which units is radiation measured?",
   opts=[
     ["Millisieverts and milligrays",
      "Correct — x-ray radiation is low compared with other radiographic modalities."],
     ["Hounsfield units and pixels",
      "Hounsfield units measure computed tomography attenuation rather than radiation dose."],
     ["Tesla and gauss",
      "Those measure magnetic field strength in magnetic resonance imaging."],
     ["Hertz and decibels",
      "Those describe sound waves in ultrasound."]],
   c=0, cite=c(9)),

 dict(topic="Computed tomography", io=IOB, slot="etiology",
   q="How does a computed tomography scanner acquire its data?",
   opts=[
     ["Powerful x-ray beams pass through the patient via a rotating fan beam, measuring transmission at thousands of data points",
      "Correct — a computer then processes the data through algorithms into diagnostic images."],
     ["A gamma camera mounted on a rotating gantry detects the photons that are emitted from an injected isotope",
      "That describes single photon emission computed tomography."],
     ["High-frequency sound waves released from a transducer bounce off tissue and return",
      "That describes ultrasound."],
     ["A varying magnetic field aligns hydrogen atoms which then emit radio waves",
      "That describes magnetic resonance imaging."]],
   c=0, cite=c(16)),

 dict(topic="Computed tomography", io=IOB, slot="manifestation",
   q="What is a computed tomography image composed of, and what is each unit assigned?",
   opts=[
     ["A matrix of thousands of tiny squares called pixels, each assigned a computed tomography number from −1000 to +1000 in Hounsfield units",
      "Correct — water is assigned a Hounsfield number of zero by convention."],
     ["A matrix of voxels, each assigned a signal intensity from 0 to 255 in greyscale units",
      "That is not how the lecture describes the image."],
     ["A series of two-dimensional projections, each one assigned its own radiodensity value as measured in millisieverts",
      "Millisieverts measure radiation dose rather than image density."],
     ["A hydrogen map, each point assigned a relaxation time in milliseconds",
      "That describes magnetic resonance imaging."]],
   c=0, cite=c(12)),

 dict(topic="Computed tomography", io=IOB, slot="manifestation",
   q="Which substance is assigned a Hounsfield number of zero by convention?",
   opts=[
     ["Water",
      "Correct — other tissues take a range of Hounsfield numbers according to their density."],
     ["Air",
      "Air sits at the low, negative end of the scale."],
     ["Bone",
      "Bone sits at the high, positive end of the scale."],
     ["Fat",
      "Fat sits below water on the scale but is not the zero reference."]],
   c=0, cite=c(12)),

 dict(topic="Computed tomography", io=IOB, slot="etiology",
   q="Who is credited with developing the first computed tomography scanner, and what recognition followed?",
   opts=[
     ["Sir Godfrey Hounsfield, who won the 1979 Nobel Prize in Medicine along with Allan Cormack",
      "Correct — the unit of attenuation is named after him."],
     ["Wilhelm Roentgen, who won the first Nobel Prize for Physics in 1901",
      "He discovered x-rays rather than computed tomography."],
     ["Allan Cormack alone, who won the 1979 Nobel Prize for Physics",
      "He shared the 1979 Medicine prize with Hounsfield."],
     ["Paul Lauterbur, who won the Nobel Prize for developing magnetic resonance imaging",
      "That work was on magnetic resonance rather than computed tomography."]],
   c=0, cite=c(12)),

 dict(topic="Computed tomography", io=IOD, slot="manifestation",
   q="What is the window in computed tomography?",
   opts=[
     ["The range of Hounsfield numbers pre-selected for display, spread over the available grey scale",
      "Correct — for example only those densities between −100 and +300."],
     ["The physical aperture of the gantry through which the patient passes",
      "That is the bore rather than the window."],
     ["The interval during which the contrast sits at its peak concentration in the vessel",
      "That is a timing concept rather than the display window."],
     ["The slice thickness selected before the scan is acquired",
      "Slice thickness is a separate acquisition parameter."]],
   c=0, cite=c(14)),

 dict(topic="Computed tomography", io=IOD, slot="differential",
   q="What does increased attenuation mean on a computed tomography image, and how does it appear?",
   opts=[
     ["A denser substance with a high computed tomography number, appearing whiter",
      "Correct — the same substances would be radiopaque on a conventional radiograph."],
     ["A less dense substance with a low computed tomography number, appearing blacker",
      "That describes decreased attenuation."],
     ["A substance producing no signal at all, appearing as a signal void",
      "That describes calcium on magnetic resonance imaging."],
     ["A region taking up more injected radioisotope than surrounding tissue",
      "That describes uptake on nuclear imaging."]],
   c=0, cite=c(14)),

 dict(topic="Computed tomography", io=IOD, slot="differential",
   q="Which substances show decreased attenuation on computed tomography?",
   opts=[
     ["Air and fat, which absorb fewer x-rays and appear blacker",
      "Correct — on a conventional radiograph they would show decreased density or increased lucency."],
     ["Metal and calcium, which absorb more x-rays and appear whiter",
      "Those show increased attenuation."],
     ["Fluid and soft tissue, which sit at exactly zero Hounsfield units",
      "Water is zero by convention; soft tissue takes a range above it."],
     ["Gadolinium and iodine, which are used as contrast agents",
      "Contrast agents increase attenuation where they collect."]],
   c=0, cite=c(14)),

 dict(topic="Computed tomography", io=IOB, slot="first-line",
   q="What is post-processing, and what does it avoid?",
   opts=[
     ["Manipulating the raw data after acquisition to best demonstrate an abnormality, without repeating the study or re-exposing the patient",
      "Correct — digital imaging markedly advanced this ability."],
     ["Reformatting the printed film after it has been developed, in order to improve the contrast that is seen on the hard copy",
      "The benefit described is digital rather than photographic."],
     ["Giving a second dose of contrast to improve the visibility of a lesion",
      "Post-processing specifically avoids re-exposing the patient."],
     ["Repeating the scan at a different slice thickness to improve resolution",
      "Post-processing specifically avoids repeating the study."]],
   c=0, cite=c(15)),

 dict(topic="Computed tomography", io=IOB, slot="first-line",
   q="Which advantages are named for computed tomography?",
   opts=[
     ["It expands the grey scale beyond the five basic densities, reduces overlapping of structures, works with implantable devices, and allows three-dimensional reconstruction",
      "Correct — it is described as the cornerstone of cross-sectional imaging."],
     ["It uses no ionizing radiation at all and is described as being the safest of all of the imaging modalities that are currently available anywhere",
      "That describes ultrasound."],
     ["It is fully portable, inexpensive, and can be brought to the patient's bedside",
      "It is described as not truly portable."],
     ["It is superior to magnetic resonance imaging for differentiating soft tissues",
      "Magnetic resonance imaging is superior for soft tissue."]],
   c=0, cite=c(20)),

 dict(topic="Computed tomography", io=IOF, slot="avoid",
   q="Which disadvantages are named for computed tomography?",
   opts=[
     ["Not truly portable, uses a lot of ionizing radiation, and requires space and sophisticated computer processing",
      "Correct — the radiation burden is the major clinical trade-off."],
     ["Operator dependent, cannot penetrate through bone, and large gas-filled structures disrupt the signal",
      "Those are the disadvantages of ultrasound."],
     ["Time consuming, with safety problems around magnetic implanted devices",
      "Those are the disadvantages of magnetic resonance imaging."],
     ["Limited range of densities, with reliance on relatively low-dose radiation",
      "Those are the disadvantages of conventional radiography."]],
   c=0, cite=c(20)),

 dict(topic="Computed tomography", io=IOB, slot="prognosis",
   q="How is computed tomography's place among imaging modalities described?",
   opts=[
     ["It is the cornerstone of cross-sectional imaging",
      "Correct — magnetic resonance imaging is described as the cornerstone of neuroimaging."],
     ["It is the safest of all the radioimaging modalities",
      "That description belongs to ultrasound."],
     ["It is the cornerstone of neuroimaging specifically",
      "That description belongs to magnetic resonance imaging."],
     ["It is the most widely obtained imaging study performed",
      "That description belongs to conventional radiographs."]],
   c=0, cite=c(20)),

 dict(topic="Fluoroscopy", io=IOB, slot="etiology",
   q="What does fluoroscopy allow that a conventional radiograph does not?",
   opts=[
     ["Real-time visualisation, allowing evaluation of motion and of positional change in bones and joints",
      "Correct — images can be viewed live and captured as stills or video."],
     ["Imaging without any ionizing radiation at all, making it entirely safe to use in pregnancy",
      "Fluoroscopy does use ionizing radiation."],
     ["Cross-sectional imaging in any geometric plane after acquisition",
      "That describes computed tomography."],
     ["Differentiation of soft tissues superior to computed tomography",
      "That describes magnetic resonance imaging."]],
   c=0, cite=c(57)),

 dict(topic="Fluoroscopy", io=IOB, slot="agent/regimen",
   q="What equipment does fluoroscopy require?",
   opts=[
     ["An x-ray unit fitted for controlled motion of the source, the imaging sensor and the patient, with a tilting table",
      "Correct — the tube moves freely back and forth to image the patient."],
     ["A gamma camera mounted on a rotating gantry around the patient",
      "That describes single photon emission computed tomography."],
     ["A superconducting magnet requiring dedicated site construction beforehand and high ongoing cost",
      "That describes magnetic resonance imaging."],
     ["A handheld transducer connected to a portable processing unit",
      "That describes ultrasound."]],
   c=0, cite=c(57)),
]
