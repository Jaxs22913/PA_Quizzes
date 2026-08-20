"""Length-bias remediation for Principles of Diagnostic Medicine I, Lecture 2.

The raw pool came out 4% gameable, already under the 10% bar, because this deck
is mostly discrete facts rather than compare-and-contrast enumerations. Four
questions still lead by a spottable margin and are repaired here.

Keys are (index into the concatenated pool A + B + C, index of the WRONG option
to rewrite). Writing the option index explicitly rather than matching by string
similarity means a fix cannot drift onto a different choice when a pool is
edited, and the applier asserts it never lands on the correct answer.

DELIBERATELY MAKING A DISTRACTOR LONGER THAN THE ANSWER. Padding every wrong
choice up to just under the correct one leaves the correct answer still the
single longest, which is the residual tell an earlier site-wide pass never
closed. Three of the four fixes below overshoot on purpose.

Pools are APPENDED, never prepended, so these indices stay valid.
"""
FIXES = {
 # [14] "What is a computed tomography image composed of..." -- correct is 135.
 (14, 1): "A matrix of thousands of tiny cubes called voxels, each assigned a greyscale signal intensity on a fixed scale running from zero to two hundred and fifty five",
 (14, 3): "A hydrogen map, each point assigned a relaxation time in milliseconds reflecting the local chemical environment of that tissue",

 # [25] "What equipment does fluoroscopy require?" -- correct is 114.
 (25, 1): "A gamma camera mounted on a rotating gantry that circles the patient, with a fixed table and a detector housing that does not move",
 (25, 3): "A handheld transducer connected to a portable processing unit, needing neither a tilting table nor a shielded examination room",

 # [84] "What are technetium-99's stated indications..." -- correct is 175.
 (84, 1): "Cancer staging, brain disorders and cardiac blood flow, together with tumour delineation and lesion characterisation; it concentrates wherever the glucose consumption of the tissue is highest",
 (84, 2): "Vasculopathy, emboli, thrombi, stenosis and aneurysm assessment, along with graft surveillance; it fills the vascular lumen and is imaged during the first pass through it",

 # [89] "What practical ordering point..." -- correct is 122.
 (89, 1): "Multiple body parts should be combined into one single order, so that the patient is scanned once and the radiologist reads the whole study together",
}
