# -*- coding: utf-8 -*-
# PDM I Lecture 10 -- pool C: questions added AFTER the 30 September recording was read, to
# carry the topics she spent the most time on and flagged aloud. Every question still cites the
# slide that states its fact; the recording only chose WHICH deck facts to add weight to.
#   - "these three phases ... this is important" (primary hemostasis, coagulation, fibrinolysis)
#   - von Willebrand disease: "the most common inherited bleeding disorder ... lock that in"
#   - where to begin: an abnormal PTT means clotting factors, never platelets; normal PT and PTT
#     with bleeding means think platelets
#   - D-dimer earns its place only when a normal result is plausible; it never says where
#   - drugs that impair platelet function (aspirin, nonsteroidal anti-inflammatory drugs)
#   - bleeding time as a readout of platelet function
# KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
from pdm_l10_pool_a import Q, c, IOA, IOB, IOC, IOD, IOE, IOF

POOL_C = [

Q("Definitions", IOA, "define",
  "A 44-year-old woman is taught the three overlapping stages of hemostasis. Which set is correct?",
  ("Primary hemostasis, secondary hemostasis, fibrinolysis",
   "Correct. Hemostasis has three overlapping stages: the platelet plug (primary hemostasis), the fibrin clot built by the coagulation factors (secondary hemostasis) and the breakdown of the clot (fibrinolysis)."),
  [("Primary hemostasis, secondary hemostasis, thrombosis",
    "Thrombosis is a pathologic clot forming in a vessel, not a stage of normal hemostasis. The third stage is fibrinolysis, the breakdown of the clot."),
   ("Platelet plug, fibrin clot, embolism",
    "An embolism is a clot that has moved somewhere. The third stage of hemostasis is the dissolving of the clot by fibrinolysis."),
   ("Coagulation, thrombosis, embolism",
    "These describe clot behavior in disease. Normal hemostasis runs from platelet plug, through coagulation, to fibrinolysis.")],
  c(6)),

Q("von Willebrand studies", IOA, "phase",
  "A 22-year-old woman has von Willebrand disease. Which phase of hemostasis does the missing factor serve?",
  ("Primary hemostasis",
   "Correct. von Willebrand factor tethers platelets to exposed subendothelial collagen, so its deficiency impairs formation of the platelet plug."),
  [("Secondary hemostasis",
    "Secondary hemostasis is the coagulation cascade that makes cross-linked fibrin. von Willebrand factor acts earlier, at the platelet plug."),
   ("Fibrinolysis",
    "Fibrinolysis is the plasmin-mediated breakdown of a clot. von Willebrand factor helps platelets stick, which comes first."),
   ("Vasoconstriction",
    "Vasoconstriction narrows the injured vessel and is a separate component of hemostasis. von Willebrand factor tethers platelets to collagen.")],
  c(6)),

Q("Activated partial thromboplastin time", IOF, "where to begin",
  "A 52-year-old man has a prolonged partial thromboplastin time and a normal platelet count. Which phase of hemostasis is most likely affected?",
  ("Secondary hemostasis",
   "Correct. The partial thromboplastin time tests the intrinsic and common coagulation pathways, so a prolonged result points to the clotting factors, secondary hemostasis."),
  [("Primary hemostasis",
    "Primary hemostasis is the platelet plug, evaluated by the count, smear and function tests. A prolonged partial thromboplastin time does not test it."),
   ("Fibrinolysis",
    "Fibrinolysis is evaluated by breakdown-product tests such as D-dimer, not by the partial thromboplastin time."),
   ("Vasoconstriction",
    "Vasoconstriction is not measured by a clotting time. A prolonged partial thromboplastin time reflects clotting factors.")],
  c(18)),

Q("Pattern recognition", IOF, "where to begin",
  "A 34-year-old woman bleeds easily. Her platelet count, prothrombin time and partial thromboplastin time are all normal. Which should be investigated next?",
  ("Platelet function",
   "Correct. Normal prothrombin time and partial thromboplastin time with bleeding suggest platelet dysfunction, so platelet function testing and von Willebrand studies come next."),
  [("Intrinsic pathway factors",
    "The partial thromboplastin time is normal, which argues against an intrinsic pathway deficiency."),
   ("Extrinsic pathway factors",
    "The prothrombin time is normal, which argues against an extrinsic pathway deficiency."),
   ("Common pathway factors",
    "A common pathway deficiency would prolong the prothrombin time, the partial thromboplastin time or both, and both are normal here.")],
  c(32)),

Q("Platelet abnormalities", IOD, "history",
  "A 41-year-old woman bleeds easily. Her platelet count, prothrombin time and partial thromboplastin time are normal, and platelet function testing is abnormal. Which history best explains this?",
  ("Regular aspirin or nonsteroidal drug use",
   "Correct. Aspirin and other nonsteroidal anti-inflammatory drugs give a normal count, prothrombin time and partial thromboplastin time with abnormal platelet function, and patients may not realize an over-the-counter product contains them."),
  [("A diet very low in vitamin K",
    "Vitamin K deficiency prolongs the prothrombin time, which is normal here."),
   ("A family history of hemophilia",
    "Hemophilia prolongs the partial thromboplastin time and leaves platelet function normal."),
   ("Long-term heparin therapy",
    "Heparin prolongs the partial thromboplastin time and thrombin time, and it does not explain normal clotting times.")],
  c(29)),

Q("Bleeding time", IOD, "interpret",
  "A 27-year-old man has a normal platelet count and a bleeding time of 18 minutes (reference 3 to 10). What does this suggest?",
  ("Platelets are not working well",
   "Correct. With a normal platelet count a prolonged bleeding time signals a platelet function problem, a primary hemostasis defect."),
  [("Coagulation factors are deficient",
    "Factor deficiencies prolong the prothrombin time or partial thromboplastin time, not bleeding time as the primary finding."),
   ("Fibrinolysis is excessive",
    "Excess fibrinolysis is assessed by other tests, such as euglobulin clot lysis time. Bleeding time reflects the platelet plug."),
   ("The platelet count is falsely high",
    "The count is normal, and a falsely high count would not lengthen the bleeding time.")],
  c(16)),

Q("D-dimer", IOF, "interpret",
  "A 33-year-old woman has calf cramping and a low suspicion of thrombosis. In which situation does a D-dimer add the most value?",
  ("When a normal result is expected",
   "Correct. D-dimer is most useful for its negative predictive value: a normal result helps exclude thrombosis, so it adds value only when a normal result is plausible."),
  [("When a clot is already known to be present",
    "A raised D-dimer is expected when a clot is known to exist, so it adds no new information."),
   ("When the clot location is needed",
    "D-dimer is nonspecific and does not show where a clot is. Imaging locates it."),
   ("When platelet function is in doubt",
    "Platelet function is evaluated by aggregometry or platelet function analysis, not D-dimer.")],
  c(22)),

Q("D-dimer", IOF, "interpret",
  "A 58-year-old man has a raised D-dimer. Which question can this result NOT answer?",
  ("Where the clot is located",
   "Correct. D-dimer only tells you clotting and breakdown have occurred; it is a nonspecific marker of fibrin breakdown and cannot localize the clot."),
  [("Whether thrombin was generated",
    "A raised D-dimer does confirm thrombin generation, because fibrin had to form first."),
   ("Whether plasmin was generated",
    "A raised D-dimer does confirm plasmin generation, because plasmin is what degrades the cross-linked fibrin."),
   ("Whether fibrin was formed and broken down",
    "That is exactly what D-dimer shows: a cross-linked fibrin clot formed and was then degraded.")],
  c(22)),

]
