# Principles of Diagnostic Medicine I, Lecture 2 — pool D.
#
# WHY THIS POOL EXISTS. Pools A, B and C were written from the deck's extracted
# TEXT. Building the guide's figures meant looking at all 56 images, and three
# slides turned out to carry examinable content that exists ONLY as a picture:
#
#   Slide 13  the Hounsfield number table -- air, fat, water, soft tissue, bone
#             and metal with their values. The extracted text of slide 13 has
#             the five density descriptions and not one number.
#   Slide 21  "Typical Organ Radiation Doses from Various Radiologic Studies."
#             The extraction reported slide 21 as EMPTY. It is a whole table,
#             and it is the only quantitative treatment of objective f.
#   Slide 36  a text block burned into the image: the standard chest examination,
#             how a posterior-anterior film is oriented, which way the patient
#             faces on the lateral, and the comparison-film habit.
#
# The lesson generalises: a text extraction reporting a slide as empty is not
# evidence that the slide is empty. Look at the images before deciding a deck
# has been covered.
#
# REYNOLDS' NUMBER RULE still holds. Hounsfield questions name the scale they
# are read against; the dose questions ask for ORDER rather than recall, so the
# figures sit in the options where they can be compared rather than in the stem
# where they would have to be remembered.
#
# Appended, never prepended -- pdm_l2_lengthfix indices are into A + B + C.
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "2. svPrinciples of Medical Imaging.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOB = "b — Describe the function and clinical applications of radiography, ultrasonography, computed tomography, magnetic resonance imaging, magnetic resonance angiography, positron emission tomography, single photon emission computed tomography and angiographic studies"
IOD = "d — Compare and contrast the concepts of radiographic density and contrast"
IOE = "e — Discuss the importance of patient positioning in medical imaging"
IOF = "f — Compare and contrast the risks and benefits associated with radiation exposure"

POOL_D = [
 dict(topic="Hounsfield units", io=IOD, slot="manifestation",
   q="On the Hounsfield scale, where water is assigned zero, what value is air given?",
   opts=[
     ["Minus one thousand, the bottom of the scale",
      "Correct — air absorbs least, so it takes the most negative number."],
     ["Minus one hundred and twenty, the bottom of the scale",
      "That is the fat end of the fat range, not the value for air."],
     ["Plus one thousand, the top of the scale",
      "Plus one thousand and above is metal, which absorbs most."],
     ["Plus four hundred, the upper middle of the scale",
      "The four hundred to six hundred band is bone."]],
   c=0, cite=c(13)),

 dict(topic="Hounsfield units", io=IOD, slot="manifestation",
   q="On the Hounsfield scale, where water is zero, which tissue sits at roughly minus forty to minus one hundred and twenty?",
   opts=[
     ["Fat, which is why it reads darker than soft tissue but lighter than air",
      "Correct — fat is negative, but nowhere near as negative as air."],
     ["Soft tissue, which is why it reads darker than fat but lighter than water",
      "Soft tissue is positive, roughly plus twenty to plus one hundred."],
     ["Bone, which is why it reads brighter than soft tissue but darker than metal",
      "Bone is roughly plus four hundred to plus six hundred."],
     ["Air, which is why it reads darker than every other tissue on the scan",
      "Air is minus one thousand, the bottom of the scale."]],
   c=0, cite=c(13)),

 dict(topic="Hounsfield units", io=IOD, slot="manifestation",
   q="On the Hounsfield scale, where water is zero, what range is given for bone?",
   opts=[
     ["Roughly plus four hundred to plus six hundred",
      "Correct — high, but still below the plus one thousand of metal."],
     ["Roughly plus twenty to plus one hundred",
      "That is the soft tissue range."],
     ["Roughly minus forty to minus one hundred and twenty",
      "That is the fat range, and it is negative."],
     ["Roughly plus one thousand or higher",
      "Plus one thousand and above is metal."]],
   c=0, cite=c(13)),

 dict(topic="Hounsfield units", io=IOD, slot="differential",
   q="Ordered from the most negative Hounsfield number to the most positive, what is the sequence of tissues?",
   opts=[
     ["Air, fat, water, soft tissue, bone, metal",
      "Correct — and it runs blackest to whitest in exactly that order."],
     ["Air, water, fat, soft tissue, bone, metal",
      "Fat is negative and water is zero, so fat comes first."],
     ["Metal, bone, soft tissue, water, fat, air",
      "This is the correct sequence reversed."],
     ["Fat, air, water, bone, soft tissue, metal",
      "Air is more negative than fat, and bone is denser than soft tissue."]],
   c=0, cite=c(13)),

 dict(topic="Hounsfield units", io=IOD, slot="differential",
   q="How does the Hounsfield table refine the five basic radiographic densities?",
   opts=[
     ["It separates water from soft tissue, which a conventional radiograph cannot tell apart",
      "Correct — the deck's asterisk on “Five*” marks exactly that exception."],
     ["It separates calcium from metal, which a conventional radiograph cannot tell apart",
      "Calcium and metal are already distinct among the five basic densities."],
     ["It separates fat from air, which a conventional radiograph cannot tell apart",
      "Fat and air are already distinguishable on a plain film."],
     ["It merges bone and soft tissue, which a conventional radiograph shows separately",
      "The table separates tissues rather than merging them."]],
   c=0, cite=c(13)),

 dict(topic="Radiation dose", io=IOF, slot="differential",
   q="In the deck's table of typical organ radiation doses, which listed study delivers the highest dose?",
   opts=[
     ["Neonatal abdominal computed tomography, to the stomach",
      "Correct — twenty, the largest figure in the table."],
     ["Barium enema, to the colon",
      "Fifteen, which is high but is not the top of the table."],
     ["Adult abdominal computed tomography, to the stomach",
      "Ten, which is half the neonatal figure."],
     ["Screening mammography, to the breast",
      "Three, well below the abdominal tomography studies."]],
   c=0, cite=c(21)),

 dict(topic="Radiation dose", io=IOF, slot="differential",
   q="How does the organ dose of neonatal abdominal computed tomography compare with the adult study?",
   opts=[
     ["It is twice as high, twenty against ten",
      "Correct — the smaller the patient, the higher the organ dose."],
     ["It is half as high, ten against twenty",
      "This reverses them; the neonatal figure is the larger of the two."],
     ["It is the same, since the scanner protocol is identical",
      "The table gives two different numbers for the two studies."],
     ["It is a tenth as high, since paediatric protocols are dose-reduced",
      "Dose reduction is good practice, but it is not what this table shows."]],
   c=0, cite=c(21)),

 dict(topic="Radiation dose", io=IOF, slot="differential",
   q="In that same table, which listed study delivers the lowest organ dose?",
   opts=[
     ["Dental radiography, to the brain",
      "Correct — five thousandths, the smallest figure in the table."],
     ["Posterior-anterior chest radiography, to the lung",
      "One hundredth, which is low but is twice the dental figure."],
     ["Lateral chest radiography, to the lung",
      "Fifteen hundredths, higher than either of the two above it."],
     ["Screening mammography, to the breast",
      "Three, far above any of the plain radiographic studies."]],
   c=0, cite=c(21)),

 dict(topic="Radiation dose", io=IOF, slot="differential",
   q="How does the lung dose of a lateral chest radiograph compare with the posterior-anterior view?",
   opts=[
     ["It is higher, which is one reason the posterior-anterior view is the preferred projection",
      "Correct — the deck also credits the posterior-anterior view with lower dose to sensitive organs."],
     ["It is lower, which is one reason the lateral view is taken first in a standard series",
      "The lateral figure in the table is the larger of the two."],
     ["It is identical, because both views expose the same volume of lung tissue",
      "The table gives two different values for the two projections."],
     ["It is higher, but only in children, because the chest wall is thinner",
      "The table is not stratified by age for the chest views."]],
   c=0, cite=c(21)),

 dict(topic="Radiation dose", io=IOF, slot="manifestation",
   q="How is radiation dose defined and expressed?",
   opts=[
     ["Ionizing energy absorbed per unit of mass, in grays or milligrays, where one gray is one joule per kilogram",
      "Correct — and equivalent dose is then expressed in sieverts or millisieverts."],
     ["Ionizing energy emitted per unit of time, in grays or milligrays, where one gray is one joule per second",
      "Dose is absorbed energy per mass, not emitted energy per time."],
     ["Ionizing energy absorbed per unit of volume, in sieverts only, where one sievert is one joule per litre",
      "The unit of absorbed dose is the gray, and it is defined per kilogram."],
     ["Ionizing energy delivered per exposure, in millisieverts only, where one millisievert is one milliwatt",
      "A millisievert is not a unit of power and dose is not defined per exposure."]],
   c=0, cite=c(21)),

 dict(topic="Radiation dose", io=IOF, slot="manifestation",
   q="For the x-ray radiation used in computed tomography scanners, how do the millisievert and the milligray relate?",
   opts=[
     ["One millisievert equals one milligray",
      "Correct — which is why the table can label its column with either unit."],
     ["One millisievert equals ten milligrays",
      "There is no ten-fold conversion between the two for x-ray radiation."],
     ["One millisievert equals one hundred milligrays",
      "No such conversion factor is given."],
     ["One millisievert equals one thousand milligrays",
      "That would be a sievert-to-milligray relationship, and it is not stated."]],
   c=0, cite=c(21)),

 dict(topic="Radiodensity", io=IOD, slot="test finding",
   q="On the deck's labelled pelvic radiograph, how are bone, gas and the prosthesis described?",
   opts=[
     ["Bone is radiopaque, gas is radiolucent, and the metal prosthesis is very opaque",
      "Correct — one image showing three of the five densities at once."],
     ["Bone is radiolucent, gas is radiopaque, and the metal prosthesis is very lucent",
      "Each of the three labels is inverted here."],
     ["Bone is very opaque, gas is radiopaque, and the metal prosthesis is radiolucent",
      "Metal is the most opaque of the three, not the most lucent."],
     ["Bone is radiopaque, gas is very opaque, and the metal prosthesis is radiolucent",
      "Gas absorbs least of anything on the film, so it is lucent."]],
   c=0, cite=c(10)),

 dict(topic="Positioning", io=IOE, slot="first-line",
   q="What does the standard chest examination consist of?",
   opts=[
     ["A posterior-anterior and a lateral chest radiograph, read together",
      "Correct — the deck stresses that the films are read as a pair."],
     ["A posterior-anterior chest radiograph alone, with a lateral only if it is abnormal",
      "The lateral is part of the standard examination rather than a conditional extra."],
     ["An anterior-posterior and a lateral decubitus radiograph, read together",
      "The anterior-posterior view is the one taken when a patient cannot stand."],
     ["A posterior-anterior radiograph and a non-contrast computed tomography scan",
      "Tomography is not part of the standard chest examination described here."]],
   c=0, cite=c(36)),

 dict(topic="Positioning", io=IOE, slot="manifestation",
   q="How is a posterior-anterior chest film oriented when you look at it?",
   opts=[
     ["As if the patient were standing in front of you, with their right side on your left",
      "Correct — the same convention as facing a patient in the room."],
     ["As if the patient were standing behind you, with their right side on your right",
      "The convention places the patient's right on your left, not your right."],
     ["As if you were looking at the patient's feet, with their left side on your right",
      "That is the cross-sectional convention for tomography and magnetic resonance."],
     ["As if you were looking down from above, with their right side nearest the top",
      "No such overhead convention is described for chest radiography."]],
   c=0, cite=c(36)),

 dict(topic="Positioning", io=IOE, slot="manifestation",
   q="On the lateral chest view, which way is the patient facing?",
   opts=[
     ["Towards the left",
      "Correct — pairing it with the posterior-anterior film keeps the two consistent."],
     ["Towards the right",
      "The deck states the patient faces left on the lateral view."],
     ["Towards the viewer",
      "A lateral view is taken side-on, so the patient does not face the viewer."],
     ["Away from the viewer",
      "The orientation given is left, not front-to-back."]],
   c=0, cite=c(36)),

 dict(topic="Positioning", io=IOE, slot="education",
   q="What does the deck say about comparison films?",
   opts=[
     ["They can be invaluable — old gold — and the old film is displayed adjacent to the matching new one",
      "Correct — old posterior-anterior beside new, old lateral beside new."],
     ["They are rarely useful once a current study exists, and should be archived rather than displayed",
      "The deck takes the opposite view of their value."],
     ["They should be displayed only when the radiologist specifically requests them for a read",
      "No such condition is placed on using comparison films."],
     ["They must be matched by modality but not by projection, so any old film may be paired",
      "The pairing is projection-specific: old lateral goes beside new lateral."]],
   c=0, cite=c(36)),

 dict(topic="Computed tomography", io=IOB, slot="first-line",
   q="What does the deck's three-panel chest example illustrate about post-processing?",
   opts=[
     ["The same acquired data re-windowed to bring out different pathology, without re-scanning the patient",
      "Correct — that is the benefit digital imaging markedly advanced."],
     ["Three separate acquisitions at different dose settings, compared side by side for quality",
      "Post-processing works on one acquisition; it does not require three."],
     ["The same anatomy imaged on three different modalities, compared for their relative strengths",
      "The panels are computed tomography windows rather than different modalities."],
     ["Three consecutive time points after contrast, compared to show the pattern of enhancement",
      "Windowing is not a timing technique."]],
   c=0, cite=c(15)),
]
