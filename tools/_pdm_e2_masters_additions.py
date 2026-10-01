#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Guide lines for the PDM I Exam 2 MASTER-ONLY questions whose fact the guide did not state
(build_guide_links reported 15 with no passage after tools/pdm_e2_masters_partition.py ran).
Idempotent: items with id principles-of-diagnostic-medicine-i-exam-2-m*** are rebuilt from the
LINES table. Each line is composed only from the question's own vetted explanation
(tools/verify_guide_additions.py enforces it). Section placement is by the subject the line teaches
(guide_additions_section_placement). Run tools/apply_guide_additions.py afterwards.
"""
import json, os, re, sys, html
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import build_guide_links as B

FOLDER = "Principles of Diagnostic Medicine I Exam 2"
PATH = os.path.join(HERE, "guide_additions", "principles-of-diagnostic-medicine-i-exam-2.json")
GUIDE = os.path.join(ROOT, FOLDER, "pdm-exam-2-study-guide.html")
MASTERS = os.path.join(ROOT, FOLDER, "master-exams.json")

# stem prefix -> (section id, line)
LINES = [
 ("How does electrophysiological testing", "ci-angio",
  "<b>Electrophysiological testing.</b> The rhythm is recorded while different areas of the heart are stimulated with electrical impulses, revealing reproducible arrhythmias and their exact origin."),
 ("How are the catheters for electrophysiological", "ci-angio",
  "<b>Catheters for electrophysiological testing.</b> Three or four catheters pass from the internal jugular, subclavian or common femoral vein into the right atrium or right ventricle, so they are introduced through veins into the right heart."),
 ("What distinguishes a pseudoaneurysm", "ci-angio",
  "<b>Pseudoaneurysm at the puncture site.</b> Unlike a simple hematoma, it pulsates and still communicates with the artery: blood still moves in and out of it, which is why it can keep expanding and why the site is always checked."),
 ("On standard calibration", "ecg-principles",
  "<b>Standard calibration.</b> Two large boxes, a 10 millimeter deflection, equal 1 millivolt, so each small box is 0.1 millivolt."),
 ("A 64-year-old man has blood drawn", "co-secondary",
  "<b>International normalized ratio.</b> It adjusts the prothrombin time ratio so results can be standardized from laboratory to laboratory."),
 ("A six-second rhythm strip shows twelve", "ecg-rate",
  "<b>Atrial rate.</b> The atrial rate comes from counting P waves in six seconds and multiplying by ten, so twelve P waves in a six-second strip give 120 beats per minute."),
 ("How long does the absolute refractory", "ecg-refractory",
  "<b>Absolute refractory period.</b> It lasts about 180 milliseconds, running from phase 0 to the middle of phase 3; throughout that time the cell will not respond to another stimulus."),
 ("A 50-year-old has an elevated lipoprotein(a)", "bl-analyze",
  "<b>Elevated lipoprotein(a).</b> It is a largely fixed genetic risk factor measured once; elevation prompts earlier and more intensive management of every other modifiable risk factor, since statins do not lower it."),
 ("Why is an intravenous sedative", "ci-echo",
  "<b>Sedation before a transesophageal echocardiogram.</b> An intravenous sedative helps the patient relax and prevents vomiting while the probe is passed through the mouth and down the esophagus."),
 ("Besides diagnosing coronary", "ci-nuclear",
  "<b>Radionuclide myocardial perfusion imaging: prognosis.</b> Prognosis is a stated indication: the study identifies patients at increased risk of myocardial infarction and those who may need angiography or surgery, so it predicts future cardiac events."),
 ("Which is a stated indication for coronary", "ci-ct",
  "<b>Coronary computed tomography angiography indication.</b> Evaluating an equivocal or non-diagnostic stress test is a stated indication; it answers the question the stress test left open, alongside assessing chest pain and detecting or excluding stenosis and plaque."),
 ("A 74-year-old has an N-terminal", "bl-compare",
  "<b>N-terminal pro B-type natriuretic peptide.</b> Cardiomyocytes secrete pro B-type natriuretic peptide in response to stretch, and it is cleaved into biologically active B-type natriuretic peptide and the inert fragment N-terminal pro B-type natriuretic peptide."),
 ("A Q wave measures 0.08", "ecg-intervals",
  "<b>Q wave width.</b> A normal Q wave is under 0.04 seconds (one small box) and low in amplitude, so a Q wave of 0.08 seconds, two small boxes, is too wide."),
 ("In most leads, how far", "ecg-intervals",
  "<b>J point.</b> The J point, where the QRS complex ends and the ST segment begins, should be at the baseline, with one millimeter of variance allowed in most leads."),
 ("Why is cardiac computed tomography synchronized", "ci-ct",
  "<b>Cardiac computed tomography and the electrocardiogram.</b> Because the heart is constantly moving, tying the scan to the electrocardiogram tracing lets the heart be evaluated at chosen points in the cycle, to view different stages of the cardiac cycle."),
 # second round, after the independent judges returned PARTIAL/FAIL on the first pass
 ("Which is a recognized limitation of cardiovascular magnetic resonance", "ci-mri",
  "<b>Limitations of cardiovascular magnetic resonance.</b> Along with claustrophobia, a distorted electrocardiogram and the need for electrocardiographic and respiratory gating, the long scan, a lengthy acquisition time, is one of its recognized drawbacks."),
 ("A strip has no three-second markers", "ecg-rate",
  "<b>Six-second strip.</b> Each large box is 0.2 seconds, so fifteen large boxes make 3 seconds and thirty large boxes make 6 seconds."),
 ("A 62-year-old man has suspected thrombosis", "co-compare",
  "<b>Thrombotic workup.</b> The thrombotic workup is the prothrombin time, the activated partial thromboplastin time and D-dimer; these differ across thrombus types and most are abnormal in disseminated intravascular coagulation."),
 ("A 50-year-old man gets a standard lipid panel", "bl-measured",
  "<b>Measured and calculated lipid components.</b> Total cholesterol, HDL-C and triglycerides are measured; LDL-C (low-density lipoprotein cholesterol) and non-HDL-C are calculated, so the LDL-C on a standard report is an estimate. HDL-C is high-density lipoprotein cholesterol."),
 ("Which fascicle of the left bundle branch extends", "ecg-ap",
  "<b>Left anterior fascicle.</b> Of the left fascicles, the left anterior fascicle is the one that extends across the anterior wall of the left ventricle."),
 ("Which patient with syncope is an indication", "ci-angio",
  "<b>Syncope and electrophysiological testing.</b> A patient with syncope and ischemic or other structural heart disease is an indication for electrophysiological testing, alongside sick sinus syndrome, survivors of sudden cardiac arrest without an established cause, ectopic beats and a suspected aberrant pathway."),
 ("Which study is used to evaluate a patient with claudication", "ci-vascular",
  "<b>Claudication and suspected peripheral arterial disease.</b> Arterial vascular ultrasound is the study used to evaluate them: it is a listed indication, and the study is fast, portable and free of ionizing radiation."),
]


def heading(doc, sid):
    m = re.search(r'<h3[^>]*\bid="%s"[^>]*>(.*?)</h3>' % re.escape(sid), doc, re.S)
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()


def main():
    doc = open(GUIDE, encoding="utf-8").read()
    masters = json.load(open(MASTERS, encoding="utf-8"))
    allq = [q for f in masters.values() for q in f]
    data = json.load(open(PATH, encoding="utf-8"))
    data["items"] = [it for it in data["items"] if not re.search(r"-m\d{3}$", it["id"])]
    for n, (prefix, sid, line) in enumerate(LINES, 1):
        qs = [q for q in allq if q["q"].startswith(prefix)]
        assert len(qs) == 1, (prefix, len(qs))
        q = qs[0]
        key = q["opts"][q["c"]]
        data["items"].append({
            "id": "principles-of-diagnostic-medicine-i-exam-2-m%03d" % n,
            "section_id": sid, "section_title": heading(doc, sid), "html": line,
            "keys": [B.qkey(q)],
            "cites": [q["cite"]],
            "src": {"question": q["q"], "key": key[0], "explanation": key[1], "also": []}})
    json.dump(data, open(PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("additions file now has %d items (%d master-only)" % (len(data["items"]), len(LINES)))


if __name__ == "__main__":
    main()
