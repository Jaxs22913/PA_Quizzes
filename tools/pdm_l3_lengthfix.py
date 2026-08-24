"""Length-bias remediation for Principles of Diagnostic Medicine I, Lecture 3.

Pools A to D came out clean, but pool E ran 43% gameable -- by far the worst of
this build -- for a structural reason worth recording. Pool E is head and neck
IMAGING, and this deck teaches imaging by enumeration: "which five strengths
does computed tomography have", "which findings does orbital computed tomography
show", "which three things does contrast computed tomography evaluate". A
correct answer that must name five items is unavoidably longer than a wrong one
that names three, so the length tell is created by the question type rather than
by careless writing. Padding is the right repair here; trimming would delete the
very items the question is asking the student to recall.

Keys are (index into the concatenated pool A + B + C + D + E, index of the WRONG
option to rewrite). Indices rather than string matching, because several of
these option strings occur verbatim in more than one question -- "Magnetic
resonance imaging with contrast" is a distractor in one question and the CORRECT
answer in another, and a string replace hit both. The applier asserts a fix
never lands on the correct answer, which is what makes that safe.

Pools are APPENDED, never prepended, so these indices stay valid.
"""
# Pool sizes at time of writing: A=21, B=30, C=31, D=33 -> pool E starts at 115.
E = 115

FIXES = {
 # Which five strengths does the deck give computed tomography? correct=125
 (E + 2, 1): "Superior soft-tissue contrast, no ionizing radiation, orbital extension, perineural spread, and skull base tumours",
 # Which five strengths does the deck give magnetic resonance? correct=130
 (E + 3, 3): "No ionizing radiation, cystic versus solid character, vascularity, size and the depth of a neck mass on ultrasound",
 # The two clinical pearls. correct=139
 (E + 4, 3): "Think computed tomography whenever iodinated contrast is contraindicated; think magnetic resonance whenever contrast is safe",
 # Complicated sinusitis or orbital cellulitis. correct=54
 (E + 8, 2): "Magnetic resonance imaging of the orbits with contrast",
 # Orbital computed tomography findings. correct=95
 (E + 14, 1): "Mucosal thickening, air-fluid levels and complete sinus opacification on the affected side",
 # Neck computed tomography findings. correct=81
 (E + 15, 3): "Dermal thickening, increased echogenicity and a cobblestoning pattern",
 # Blow-out fracture. correct=133
 (E + 16, 1): "Diastasis of the frontozygomatic suture, and a fracture through the lateral wall of a maxillary sinus filled with blood",
 # Tripod fracture. correct=159 -- the longest correct answer in the build, so
 # this distractor is padded hardest.
 (E + 17, 1): "A fracture of the orbital floor alone, with orbital fat herniating inferiorly into the top of the maxillary sinus and no suture involvement",
 # Escalation after ultrasound of a neck mass. correct=62
 (E + 19, 2): "For any mass with increased vascularity on Doppler imaging",
 # The four framing questions. correct=133
 (E + 23, 2): "What is its sensitivity, what is its specificity, what is its predictive value, and what is its positive likelihood ratio",
 # The closing rule. correct=72
 (E + 24, 2): "Always choose the fastest test that the radiology department can provide",
 # Scaly rash case. correct=111
 (E + 26, 3): "Point-of-care ultrasound, because it is non-invasive and immediately available at the patient bedside",
}
