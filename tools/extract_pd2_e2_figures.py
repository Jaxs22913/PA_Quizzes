#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the teaching figures out of the PD2 Lecture 5 deck (Advanced
Cardiovascular & Peripheral Vascular System, Reynolds) for the Exam 2 guide.

The deck carries 72 distinct pictures across 115 slides. All of them were
VIEWED before any was chosen ([[image_only_slides]]), and each is named for
what is IN it, never for its position in the relationship list, because .rels
order is arbitrary ([[lettered_slide_images]]). On slide 51, for instance, the
first relationship is the PANSYSTOLIC waveform even though the slide's first
caption says "Midsystolic".

Pictures are matched by an MD5 prefix of their bytes rather than by media
number, so a re-saved deck that renumbers its media fails loudly instead of
writing the wrong picture under the right name.

FOUR SLIDES WHOSE CONTENT EXISTS ONLY IN THE PICTURE (OCR'd, then read by eye):
  56  the Levine six-grade murmur table -- slide text is one line
  64  the Bates maneuver table (squatting / standing / Valsalva against
      mitral valve prolapse, hypertrophic cardiomyopathy, aortic stenosis)
  89  pitting edema grades 0 to 4+ with the depth in millimeters and how
      long the pit lasts
  110 the ankle brachial index formula as a fraction

LEFT OUT, and why:
  27  four crossed-out photographs of auscultation over clothing -- the point
      is one sentence, and the faces are partly visible
  36  a loudspeaker icon: slide 36 carries two EMBEDDED SOUND FILES (split and
      unsplit S2) that no picture or text extraction can see
  41, 43  "EXTRA HEART SOUNDS - S3/S4" strips that duplicate slides 40 and 42
  92/94/95 three Windows metafiles (.wmf/.emf) that cannot be rendered here
  105 a screenshot of a web browser playing a video
  115 a cartoon ("Never give up, Heart")

Licensing: [[media_asset_licensing]] clears a course-slide image provided the
slide is cited. Several carry publisher marks (Mayo Foundation, Lippincott
Williams & Wilkins, Healthwise, the Royal Children's Hospital Melbourne,
Osmosis) baked into the pixels; they stay visible and are not cropped.

    python3 tools/extract_pd2_e2_figures.py
"""
import hashlib, io, os, sys
from pptx import Presentation
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "Physical Diagnosis 2 Exam 2", "pd2-exam-2-study-guide-images")
DECK_NAME = "PD II Advanced Cardiovascular & Peripheral Vascular System - Fall 2026.pptx"
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Physical Diagnosis 2 Inbox/Exam 2/" + DECK_NAME)

# (slide, md5 prefix, stem, alt text, caption). Captions say what to LOOK AT
# and why it matters; they do not just restate the label.
FIGURES = [
 (21, "2a4b9c", "apical-impulse-anatomy",
  "Front view of a torso with the heart drawn in place behind the ribs, labeled aorta, pulmonary arteries, superior vena cava, right atrium, right ventricle and left ventricle, with a dashed outline marking the apical impulse at the lower left edge of the heart.",
  "Where the heart actually sits. The <b>right ventricle</b> makes up most of the front of the heart; the <b>left ventricle</b> only reaches the chest wall at its lower left tip, and that tip is the <b>apical impulse</b>. That is why the point of maximal impulse marks the heart's LEFT border, and why it moves when the left ventricle enlarges."),
 (32, "94d855", "surface-anatomy",
  "Two panels: a skeleton model with the angle of Louis, clavicles, manubrium, sternum and second rib labeled, and a man's chest marked with dots at the aortic, pulmonic, tricuspid and mitral areas beside the midclavicular and anterior axillary lines.",
  "Finding the rib spaces. The <b>angle of Louis</b> (the sternal-manubrial junction) sits beside the <b>second rib</b>, so the space just below it is the second intercostal space &mdash; count down from there to the fifth for the apex. The right-hand panel puts the four listening areas on a real chest."),
 (83, "f7e357", "arterial-tree",
  "Full-body line drawing of the arterial system labeled from the temporal and carotid arteries down through the subclavian, brachial, radial and ulnar arteries, the aorta and its abdominal branches, and the iliac, femoral, popliteal, tibial and peroneal arteries.",
  "The arterial map behind the peripheral vascular examination. Every pulse you palpate &mdash; carotid, brachial, radial, ulnar, femoral, popliteal, dorsalis pedis, posterior tibial &mdash; and every bruit site you auscultate is a named vessel on this tree."),
 (16, "3e1b81", "lub-dub",
  "Diagram of two tall red bars labeled S1 lub and S2 dub, with systole written between them and diastole on either side.",
  "The frame every other sound hangs on. <b>S1 (lub)</b> opens systole; <b>S2 (dub)</b> opens diastole. Systole is the shorter interval, between S1 and S2; diastole is the longer one, between S2 and the next S1."),
 (33, "f57d56", "cardiac-cycle",
  "Cardiac cycle diagram with an electrocardiogram trace across the top, pressure curves for the aorta, left ventricle, pulmonary artery, left atrium, right ventricle and right atrium, bars showing when each of the four valves is open or closed, and heart sounds M1 T1 at S1 and A2 P2 at S2 along the bottom.",
  "The whole cycle on one page. Read the valve bars at the bottom against the sounds: at <b>S1</b> the mitral and tricuspid valves close (M1, T1) and the aortic and pulmonic valves then open; at <b>S2</b> the aortic and pulmonic valves close (A2, P2) and the atrioventricular valves open. Every extra sound is interpreted by asking which valves are open at that moment."),
 (35, "59b04c", "split-physiologic",
  "Four vertical bars in sequence, S1, S2, S1, S2, where the first S2 is drawn as two bars labeled A2 and P2 and the second S2 is a single bar.",
  "<b>Physiologic splitting</b>: S2 separates into A2 and P2 on <b>inspiration</b> and fuses back into one sound on <b>expiration</b>. The split comes and goes with breathing, and that variation is what makes it normal."),
 (35, "d37307", "split-pathologic",
  "Text reading Pathologic Splitting, audible splitting occurs during expiration and suggests heart disease, beside four bars in which both S2 sounds are drawn doubled.",
  "<b>Pathologic splitting</b>: the split is still there on <b>expiration</b>. A split you can hear with the breath fully out suggests heart disease. The slide places both panels under the headings <i>inspiration</i> and <i>expiration</i>, which is the whole test."),
 (38, "1f00b7", "early-ejection-sound",
  "Short strip of three bars labeled S1, E1 drawn in red close after S1, and S2.",
  "<b>Early ejection sound</b> (E1): right after S1, high-pitched and clicking, from the aortic or pulmonic valve halting abruptly as it opens. It indicates cardiovascular disease."),
 (39, "140d58", "systolic-click",
  "Strip of bars labeled S1, a red bar C1 in mid-systole followed by fine red lines rising toward S2.",
  "<b>Mid-systolic click</b> (C1) followed by a late systolic murmur crescendoing up to S2 &mdash; the pattern of mitral valve prolapse with the regurgitation it causes."),
 (40, "cb2b53", "s3",
  "Strip of bars labeled S1, S2, then a red bar S3 close after S2, then S1.",
  "<b>S3</b> sits just <b>after S2</b>, early in diastole: Ken-TUC-ky, lub-dub-dee. Listen with the bell at the apex, patient in left lateral decubitus."),
 (42, "a0b708", "s4",
  "Strip of bars labeled S1, S2, then a red bar S4 immediately before the next S1.",
  "<b>S4</b> sits just <b>before S1</b>, late in diastole: Ten-nes-SEE, dee-lub-dub. Same bell-at-the-apex technique as S3; only the position in the cycle differs."),
 (44, "4f95ae", "opening-snap",
  "Strip of bars labeled S1, S2 with a red bar labeled OS, for opening snap, immediately after it, then S1.",
  "<b>Opening snap</b> (OS): very early in diastole, right after S2, from a <b>stenotic mitral valve</b> snapping open. High-pitched, so use the diaphragm &mdash; which is how you tell it apart from the low S3."),
 (51, "c4edfc", "timing-midsystolic",
  "Waveform between S1 and S2 in which red lines rise to a peak in mid-systole and fall away before S2, with a gap at each end.",
  "<b>Midsystolic</b>: the murmur starts after S1, peaks in the middle and ends before S2 &mdash; the diamond of the ejection murmurs."),
 (51, "6df8ff", "timing-pansystolic",
  "Waveform in which evenly spaced red lines fill the entire interval from S1 to S2 at constant height.",
  "<b>Pansystolic (holosystolic)</b>: starts with S1 and runs all the way to S2 &mdash; flow through something that should be shut for the whole of systole."),
 (51, "e02829", "timing-late-systolic",
  "Waveform in which red lines begin midway through systole and rise until they reach S2.",
  "<b>Late systolic</b>: begins after mid-systole and runs up to S2 &mdash; the murmur that follows the click of mitral valve prolapse."),
 (52, "207ec3", "timing-early-diastolic",
  "Waveform in which red lines start at S2 at full height and taper away through early diastole.",
  "<b>Early diastolic</b>: starts right after S2 and fades &mdash; the decrescendo of aortic or pulmonic regurgitation."),
 (52, "32dfcd", "timing-mid-diastolic",
  "Waveform in which a shorter band of red lines starts a little after S2 and tapers away in mid-diastole.",
  "<b>Mid-diastolic</b>: starts a short time after S2 &mdash; where the rumble of mitral stenosis sits."),
 (52, "ffb5bd", "timing-late-diastolic",
  "Waveform in which red lines rise in late diastole to reach the next S1.",
  "<b>Late diastolic</b>: starts late in diastole and runs up to S1."),
 (53, "2071df", "timing-continuous",
  "Waveform labeled systole and diastole in which red lines rise to S2 and continue past it, fading through diastole without a break.",
  "<b>Continuous</b>: starts in systole and runs <b>through S2</b> into diastole without stopping. A murmur you hear no matter where you are in the cycle."),
 (54, "bf4791", "shape-crescendo-decrescendo",
  "A red diamond of lines between S1 and S1, rising to a peak and falling away.",
  "<b>Crescendo-decrescendo</b>: the diamond. Rises, then falls off."),
 (54, "b5fcd7", "shape-decrescendo",
  "Red lines beginning at full height at S2 and tapering to nothing.",
  "<b>Decrescendo</b>: begins at maximum intensity and grows silent."),
 (54, "7d26b0", "shape-crescendo",
  "Red lines growing taller as they approach the next S1.",
  "<b>Crescendo</b>: grows louder."),
 (54, "50e42f", "shape-plateau",
  "Red lines of constant height filling the space from S1 to S2.",
  "<b>Plateau</b>: the intensity does not change. A holosystolic plateau murmur is the most precise description you can give."),
 (56, "85ab0c", "levine-grades",
  "Table of murmur grades one to six with descriptions, from very faint and heard only after tuning in, through loud with a palpable thrill at grade four, to audible with the stethoscope entirely off the chest at grade six.",
  "The Levine scale, written as a fraction of six. <b>This table exists only as a picture</b> &mdash; the slide text is a single line. The hinge is <b>grade 4: the first grade with a palpable thrill</b>. Grades 5 and 6 are defined by the stethoscope coming partly, then entirely, off the chest."),
 (64, "88999e", "maneuver-table",
  "Table with columns for maneuver, cardiovascular effect, mitral valve prolapse, hypertrophic cardiomyopathy and aortic stenosis, comparing squatting or Valsalva release against standing or Valsalva strain.",
  "The maneuver table, which also exists <b>only as a picture</b>. Squatting (or the release phase of Valsalva) FILLS the left ventricle: the click and murmur of mitral valve prolapse come later and shorten, the hypertrophic cardiomyopathy murmur softens, aortic stenosis gets louder. Standing (or the strain phase) EMPTIES it: every one of those reverses."),
 (67, "2e9f0e", "valve-aortic-stenosis",
  "Illustration of the heart with the aortic valve position marked, and two insets comparing a normal three-leaflet aortic valve open and closed with a stenotic valve whose thickened leaflets open only to a narrow slit.",
  "<b>Aortic stenosis</b>: thickened leaflets that open to a narrow slit. Forward flow in systole is forced through the gap, which is why the murmur is midsystolic and harsh."),
 (69, "8244f3", "valve-pulmonic-stenosis",
  "Paired diagrams of the heart and great vessels comparing a thickened, narrowed pulmonary valve with a hypertrophied right ventricular wall against a normal heart and healthy pulmonary valve.",
  "<b>Pulmonic stenosis</b>: the same obstruction on the right side, with the thickened right ventricular wall it produces &mdash; a right ventricular pressure load."),
 (70, "3d0424", "hypertrophic-cardiomyopathy",
  "Two cutaway hearts side by side, a normal heart and one with hypertrophic cardiomyopathy showing a markedly thickened interventricular septum and left ventricular wall narrowing the outflow tract.",
  "<b>Hypertrophic cardiomyopathy</b>: the thickening is in the <b>muscle</b>, most commonly the interventricular septum, not the valve. That is why this murmur is loudest at Erb's point and the tricuspid area rather than over the aortic area, and why it never radiates to the neck."),
 (73, "083e66", "valve-tricuspid-regurgitation",
  "Two cutaway views of the right heart, one normal and one with tricuspid valve regurgitation showing arrows of blood leaking back from the right ventricle into the right atrium.",
  "<b>Tricuspid regurgitation</b>: blood leaking back into the right atrium through a valve that should be shut all through systole &mdash; hence pansystolic."),
 (74, "25451b", "valve-mitral-regurgitation",
  "Two cutaway views of the left heart, one normal and one with mitral valve prolapse and regurgitation showing arrows of blood leaking back from the left ventricle into the left atrium.",
  "<b>Mitral regurgitation</b>, here from mitral valve prolapse: the powerful left ventricle drives blood back into the left atrium, which is why this pansystolic murmur is harsher than its tricuspid counterpart."),
 (77, "6c926b", "valve-aortic-regurgitation",
  "Two cutaway hearts, a normal heart and one with aortic valve regurgitation in which the abnormal aortic valve fails to close and blood leaks backward into the left ventricle.",
  "<b>Aortic regurgitation</b>: the aortic valve fails to close, so blood falls back into the left ventricle as soon as diastole begins &mdash; an early diastolic, decrescendo murmur."),
 (78, "494741", "valve-pulmonic-regurgitation",
  "Two cutaway hearts, normal and with pulmonary regurgitation, showing a jet of blood leaking back through the pulmonary valve into the right ventricle.",
  "<b>Pulmonic regurgitation</b>: the same early diastolic leak on the right side, heard over the pulmonic area."),
 (79, "cf1144", "valve-mitral-stenosis",
  "Two drawings comparing a normal mitral valve with a narrow mitral valve between the left atrium and left ventricle.",
  "<b>Mitral stenosis</b>: a narrow mitral valve that has to be forced open in diastole &mdash; the snap as it opens, then a low rumble as blood squeezes through."),
 (80, "646bee", "valve-tricuspid-stenosis",
  "Two cutaway hearts, normal and with tricuspid stenosis, showing a narrowed tricuspid valve between the right atrium and right ventricle.",
  "<b>Tricuspid stenosis</b>: the same diastolic obstruction on the right side, heard at the lower left sternal border near the xiphoid."),
 (31, "9193e7", "auscultation-areas",
  "Chest illustration with the aortic, pulmonary, tricuspid and mitral valves drawn in place and lines from each to an inset photograph of a stethoscope on the corresponding listening position.",
  "Where each valve IS versus where you LISTEN for it. The listening positions are not over the valves: each is the first place <b>downstream</b>, along the direction of blood flow, where no bone blocks the sound."),
 (88, "3b234a", "pitting-press",
  "A thumb pressing firmly into the swollen top of a foot.",
  "Checking for pitting: press firmly with the thumb for <b>at least 2 seconds</b> over the dorsum of the foot, behind the medial malleolus, or over the shin &mdash; places with bone beneath, so the pressure has something to push against."),
 (88, "781f07", "pitting-pit",
  "The same swollen foot after the thumb is removed, with a visible depression left in the skin.",
  "The <b>pit</b>: the depression the thumb leaves behind. Its depth, and how long it lasts, set the grade."),
 (89, "345072", "pitting-grades",
  "Five fingers pressing into skin at increasing depths labeled 0 to 4+ with 0, 2, 4, 6 and 8 millimeters, above a key describing each grade and how long the pit lasts.",
  "The pitting edema grades, <b>held only in this picture</b> &mdash; the slide's text is just its title. Every step is 2 mm deeper: 1+ is 2 mm and disappears rapidly, 2+ is 4 mm and gone in 10&ndash;15 seconds, 3+ is 6 mm and may last more than a minute, 4+ is 8 mm and can last more than 2 minutes."),
 (92, "3d8fb3", "arterial-insufficiency-legs",
  "Both lower legs and feet showing shiny, hairless skin with patchy discoloration over the shins.",
  "Chronic <b>arterial</b> insufficiency: loss of hair, discoloration and thin, shiny skin. Poor supply starves what the body does not need to survive first &mdash; the hair goes before anything else."),
 (92, "956659", "arterial-rubor-ulcer",
  "Two feet on a rough surface, one with a dusky red flush labeled rubor and a small dark ulcer on the tip of a toe labeled ischemic ulcer.",
  "Dependent <b>rubor</b> and an <b>ischemic ulcer</b> on the toe tip. The distal, most poorly perfused point is where the arterial ulcer forms, and it is painful unless neuropathy has taken the sensation away."),
 (94, "4bef82", "venous-insufficiency",
  "A lower leg and foot lying on a sheet, markedly swollen, with reddish-brown discoloration and a patch of broken skin above the ankle.",
  "Chronic <b>venous</b> insufficiency: heavy edema with brown hemosiderin staining around the ankle and skin breaking down over it. The problem is the flow BACK, so fluid stays distal and stretches the skin until it fails."),
 (97, "8611ec", "pulse-carotid",
  "Two fingers placed on the side of a man's neck beside the trachea to feel the carotid pulse.",
  "<b>Carotid</b>: lateral to the trachea, <b>one side at a time</b>, and <b>auscultate before you palpate</b> with the patient holding their breath."),
 (98, "f406a6", "pulse-brachial",
  "An examiner's fingers pressing into the inner elbow of a patient's extended arm.",
  "<b>Brachial</b>: medial to the biceps tendon at the antecubital fossa."),
 (99, "f9fcb3", "pulse-radial",
  "Two fingers on the thumb side of the inner wrist.",
  "<b>Radial</b>: the lateral (thumb) side of the wrist."),
 (100, "1aaac6", "pulse-ulnar",
  "An examiner's fingers pressing deep into the little-finger side of a patient's partly flexed wrist.",
  "<b>Ulnar</b>: deep on the flexor surface, medially. Partly flexing the wrist helps &mdash; and a normal ulnar pulse may not be palpable at all."),
 (101, "a46135", "pulse-femoral",
  "Examiner's hands pressing into the groin of a supine patient just below the fold of the hip.",
  "<b>Femoral</b>: below the inguinal ligament, midway between the anterior superior iliac spine and the pubic symphysis."),
 (102, "fe8ea2", "pulse-lag",
  "An examiner's hand pressing into the groin of a supine patient, with the other hand held beside it.",
  "<b>Pulse lag</b>: radial and femoral felt <b>simultaneously</b>. A femoral pulse arriving after the radial suggests <b>coarctation of the aorta</b>."),
 (103, "6eba9f", "pulse-popliteal-flexed",
  "Examiner's fingertips pressing into the back of a patient's flexed, relaxed knee.",
  "<b>Popliteal</b>, technique 1: knee flexed and relaxed, fingertips of both hands pressed deep into the midline of the fossa."),
 (103, "64a34a", "pulse-popliteal-prone",
  "Patient lying prone with the knee bent to ninety degrees while the examiner presses thumbs into the back of the knee.",
  "<b>Popliteal</b>, technique 2: patient prone, knee at 90 degrees, thumbs pressed deep. Often hard to feel &mdash; not a problem if the pulses beyond it are present."),
 (104, "f701d5", "pulse-dorsalis-pedis",
  "Examiner's fingers on the top of a bare foot, just lateral to the tendon running to the big toe.",
  "<b>Dorsalis pedis</b>: dorsum of the foot, lateral to the extensor tendon of the great toe."),
 (104, "b67cd6", "pulse-posterior-tibial",
  "Examiner's fingers curled behind the inner ankle bone of a patient's foot.",
  "<b>Posterior tibial</b>: behind the medial malleolus."),
 (105, "7d8518", "aorta-palpation",
  "Examiner's hands pressing deep into the upper abdomen of a supine patient, one on either side of the midline.",
  "Palpating the <b>abdominal aorta</b> with both hands deep in the upper abdomen. What matters is its <b>width</b>, whether or not it is easy to feel."),
 (106, "894160", "bruit-sites",
  "Abdomen of a supine man marked with red dots at the aorta in the upper midline, the renal arteries on either side of it, the iliac arteries beside the umbilicus, and the femoral arteries in each groin.",
  "The four places to listen for <b>bruits</b>: aorta (upper midline), renal (3&ndash;4 cm either side of it), iliac (3&ndash;4 cm lateral to the umbilicus and about 2 cm below) and femoral. A bruit is to a vessel what a murmur is to a valve."),
 (109, "83aa98", "allen-fist",
  "Examiner's two hands compressing a patient's wrist over both the radial and ulnar arteries while the patient makes a tight fist.",
  "<b>Allen test</b>, step 1: compress <b>both</b> the radial and ulnar arteries while the patient clenches a fist, squeezing the blood out of the hand."),
 (109, "cff6af", "allen-open",
  "The patient's hand opened with the palm pale while both arteries are still compressed at the wrist.",
  "Step 2: the patient opens the hand. It is <b>pale</b>, because both arteries are still occluded."),
 (109, "e3dda6", "allen-pallor",
  "An opened palm that remains pale although pressure over one artery has been released.",
  "Release one artery and watch. <b>Pallor that persists</b>, as here, means that artery is occluded; normally the pink returns promptly. Release the ulnar first, then repeat for the radial."),
 (110, "517273", "abi-formula",
  "Two fractions: right ankle brachial index equals highest pressure in right foot over highest pressure in both arms, and the same for the left.",
  "The ankle brachial index as a fraction, <b>one for each leg</b>: the higher of the two ankle pressures on that side, over the higher brachial systolic pressure."),
 (112, "0355a4", "abi-ankle",
  "Drawing of a lower leg with a blood pressure cuff above the ankle and Doppler probes over the dorsalis pedis and posterior tibial arteries.",
  "Ankle pressures: cuff <b>above the malleoli</b>, Doppler over the <b>dorsalis pedis</b>, then again over the <b>posterior tibial</b>, then the other leg."),
 (114, "2f52bb", "homans-sign",
  "Illustration of a patient's leg with the knee flexed while an examiner abruptly dorsiflexes the ankle, with numbered steps and pain marked behind the knee as a positive sign.",
  "<b>Homans sign</b>: knee flexed, foot dorsiflexed quickly and forcefully. <b>Pain behind the knee</b> is the positive result."),
]

MAX_W = 760


def _load():
    assert os.path.exists(DECK), "deck not found: %s" % DECK
    p = Presentation(DECK)
    blobs = {}
    for i, sl in enumerate(p.slides, 1):
        for rel in sl.part.rels.values():
            if "image" in rel.reltype and not rel.is_external:
                b = rel.target_part.blob
                blobs[(i, hashlib.md5(b).hexdigest()[:6])] = b
    return blobs


def _name(n, stem):
    return "%02d-%s.jpg" % (n, stem)


def main():
    os.makedirs(OUT, exist_ok=True)
    blobs = _load()
    missing = [(s, h, st) for s, h, st, _a, _c in FIGURES if (s, h) not in blobs]
    assert not missing, ("pictures not found by content hash -- the deck changed; view every "
                         "figure again before trusting this list: %r" % missing)
    stems = [st for _s, _h, st, _a, _c in FIGURES]
    assert len(stems) == len(set(stems)), "duplicate stem"
    total = 0
    for n, (s, h, stem, _a, _c) in enumerate(FIGURES, 1):
        im = Image.open(io.BytesIO(blobs[(s, h)]))
        if im.mode in ("RGBA", "LA", "P"):
            im = im.convert("RGBA")
            bg = Image.new("RGB", im.size, "white")
            bg.paste(im, mask=im.split()[-1])
            im = bg
        else:
            im = im.convert("RGB")
        if im.width > MAX_W:
            im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
        path = os.path.join(OUT, _name(n, stem))
        im.save(path, "JPEG", quality=86, optimize=True, progressive=True)
        total += os.path.getsize(path)
        print("  slide %3d  %-32s %4dx%-4d %6d bytes" % (s, stem, im.width, im.height, os.path.getsize(path)))
    print("wrote %d figures, %d KB, to %s" % (len(FIGURES), total // 1024, OUT))


def figure_html(dirname):
    """The <figure> blocks, keyed by stem, for the guide builder."""
    out = {}
    for n, (slide, _h, stem, alt, cap) in enumerate(FIGURES, 1):
        fn = _name(n, stem)
        path = os.path.join(OUT, fn)
        dims = ""
        if os.path.exists(path):
            with Image.open(path) as im:
                dims = ' width="%d" height="%d"' % im.size
        out[stem] = ('<figure class="fig"><img%s loading="lazy" src="%s/%s" alt="%s">'
                     '<figcaption>%s <span class="tag">Source: %s, Slide %d.</span>'
                     '</figcaption></figure>' % (dims, dirname, fn, alt, cap, DECK_NAME, slide))
    return out


if __name__ == "__main__":
    main()
