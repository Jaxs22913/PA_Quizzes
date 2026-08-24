#!/usr/bin/env python3
"""Pull the teaching figures from the PDM Lecture 4 (Complete Blood Count) deck.

Twenty-one, out of 50. This is the most image-dependent lecture in the course:
red cell morphology cannot be taught in prose, and SIX of these figures are the
ONLY source for their content -- the deck's extracted text does not contain them
at all, and slides 71 and 31 extract as completely empty.

The six that carry content found nowhere else:
  s021_1  neutropenia severity table (mild / moderate / severe by absolute count)
  s039_1  the four schistocyte types; the slide text names only two of them
  s047_1  Heinz bodies require a SUPRAVITAL stain -- they are invisible on the
          routine Wright stain used for the rest of the differential
  s063_1  the six-condition iron comparison table
  s071_1  the full anemia evaluation algorithm
  s072_1  the fishbone diagram's layout

What is left out: the decorative stock photo of blood tubes (slide 8), the
"Questions?" forest photograph (slide 75), the section-divider art, the labelled
smear on slide 15 whose percentages match neither of the deck's own reference
sets, and the duplicate reference table on slide 31 (identical to slide 7's).

Slide images are cleared for use provided the slide is cited, so each carries
its deck and slide number. Every one was viewed at full size before captioning.

NOT loading="lazy": a lazy figure is absent from the guide's own Download-as-PDF
unless the reader happened to scroll past it.
"""
import os, shutil
from PIL import Image, PngImagePlugin

PngImagePlugin.MAX_TEXT_CHUNK = 100 * 1024 * 1024
SRC = "/private/tmp/claude-501/-Users-jaxonluke/8623a091-045a-42b8-8052-ca7d2eb04188/scratchpad/pdm_l4_imgs"
OUT = ("/Users/jaxonluke/Developer/PA_Quizzes/Principles of Diagnostic Medicine I Exam 1/"
       "pdm-exam-1-l4-images")
MAXW = 900
DECK = "Complete Blood Count and Hematology Diagnostics - Shahsv.pptx"

FIGURES = [
 ("s007_1.png", "cbc-reference-table", 7,
  "Table headed Complete Blood Count and Reference Range, listing white cell count, red cell count, hemoglobin, hematocrit, the four red cell indices, platelet count, mean platelet volume, and the five differential lines each with a percentage and an absolute range.",
  "<b>The whole reference table, which is on the slide only as a picture.</b> Note the three rows that DISAGREE with the individual teaching slides later in the deck &mdash; lymphocytes are 25&ndash;33% here and 24&ndash;44% there, platelets are 150,000&ndash;400,000 here and 150,000&ndash;450,000 there, and red cell distribution width is 11&ndash;15% here and 12&ndash;15% there. Section 4.2 sets all of them side by side."),

 ("s010_1.png", "wbc-morphology", 10,
  "Five panels of stained white blood cells labelled neutrophil, eosinophil, basophil, lymphocyte and monocyte, each captioned with its nucleus and cytoplasm description.",
  "<b>The five lines, and how to tell them apart down a microscope.</b> Read the nucleus first: the neutrophil is multilobed, the eosinophil and basophil are bilobed, the lymphocyte is a single large sphere and the monocyte is kidney-shaped. Then the granules &mdash; the eosinophil's are red, the basophil's purplish-black, and the two agranulocytes have none."),

 ("s020_1.png", "anc-formula", 20,
  "Formula reading absolute neutrophil count equals white blood cell count per microlitre multiplied by the sum of the percentage of neutrophils and the percentage of bands, divided by one hundred.",
  "<b>The formula, which exists only as this image.</b> The thing that catches people is that <b>bands are counted WITH the neutrophils</b>. Note also that the worked example on the next slide is mis-bracketed &mdash; it prints 6,000 &times; (40 + 5/100), which evaluates to 240,300, not the 2,700 it then gives. The printed answer is right; the brackets are a typo."),

 ("s021_1.png", "neutropenia-grades", 21,
  "Table headed Categorizing Neutropenia, Berlinger 2020, with three rows: mild 1,000 to less than 1,500 cells per microlitre, moderate 500 to less than 1,000, severe less than 500.",
  "<b>This table is not in the slide text at all.</b> It is what makes the absolute neutrophil count worth calculating &mdash; the number only means something once you can place it in a band. <b>Severe is under 500</b>, and that is the figure that changes management."),

 ("s016_1.png", "granulocyte-lifespans", 16,
  "Table of blood cell type against lifespan in blood: neutrophil seven hours, eosinophil eight to twelve days, basophil a few hours to a few days.",
  "<b>Lifespans, which appear only in this figure.</b> The <b>neutrophil's seven hours</b> is the one to hold: it is why the marrow has to keep releasing them continuously, and why an acute bacterial infection empties the mature pool fast enough to force out bands."),

 ("s017_1.png", "agranulocyte-lifespans", 17,
  "Table of blood cell type against lifespan and function: monocyte three days and immune surveillance, B-lymphocyte memory cells may live for years and antibody production, T-lymphocyte memory cells may live for years and cellular immune response.",
  "<b>The agranulocytes, with their functions.</b> The contrast with the figure above is the point &mdash; hours to days for the granulocytes against <b>years</b> for lymphocyte memory cells."),

 ("s034_1.png", "mcv-sizes", 34,
  "Three red circles of increasing size on a green background labelled microcytic with mean corpuscular volume under 80, normocytic 80 to 100, and macrocytic over 100.",
  "<b>The three bands the entire anemia workup turns on.</b> Hemoglobin tells you there is an anemia; <b>mean corpuscular volume tells you which algorithm to run</b>."),

 ("s036_1.png", "acanthocytes", 36,
  "Blood smear showing red cells with irregular thorn-like projections, with one cell magnified in an inset box.",
  "<b>Acanthocytes, or spur cells &mdash; liver disease.</b> Acantha means thorn. The spikes are <b>irregular in length and spacing</b>, and there is no central pallor. That irregularity is the whole difference from the echinocyte below."),

 ("s037_1.png", "echinocytes", 37,
  "Blood smear showing red cells with regularly spaced short blunt projections around the whole circumference, each retaining central pallor.",
  "<b>Echinocytes, or burr cells &mdash; renal disease.</b> Echino means sea urchin. The projections run right around the cell, are <b>evenly spaced with blunter tips</b>, and <b>central pallor is preserved</b>. Two features and two different diseases separate this from the acanthocyte."),

 ("s039_1.png", "schistocyte-types", 39,
  "Four panels labelled triangular cell, horn cell, helmet cell and microspherocyte, each showing the fragment type on a blood smear.",
  "<b>Four named schistocyte forms &mdash; and the slide text names only two of them.</b> Triangular cell and microspherocyte exist only in this picture. All four are fragments, so all four mean the same thing: something is shearing red cells apart."),

 ("s039_2.png", "schistocytes-smear", 39,
  "Blood smear with several fragmented red cells circled in blue, each an irregular piece lacking central pallor.",
  "<b>Schistocytes in the field.</b> Note how small they are &mdash; usually microcytic, lacking central pallor. That size is the reason for the deck's warning that <b>automated counters may report them as platelets</b>, which can make a platelet count look falsely reassuring."),

 ("s041_2.png", "sickle-cells", 41,
  "Blood smear showing several thin crescent-shaped red cells among normal ones.",
  "<b>Sickled cells, or drepanocytes.</b> Thin, crescent shaped, <b>no central pallor</b>, and normochromic to hyperchromic because the hemoglobin inside is dense. They form <b>under low oxygen tension</b> and cause sludging in tissues."),

 ("s042_1.png", "spherocytes", 42,
  "Blood smear with arrows pointing to several small, perfectly round, densely stained red cells with no central pallor.",
  "<b>Spherocytes &mdash; hereditary spherocytosis.</b> Perfectly round, <b>central pallor completely lost</b>, and often smaller than normal. These are the cells behind the mean corpuscular hemoglobin concentration screening flag: dense rather than large."),

 ("s043_1.png", "target-cells", 43,
  "Blood smear with a red arrow labelled target cell pointing to a red cell with a dark central spot inside its pale centre.",
  "<b>Target cells, or codocytes &mdash; post splenectomy and liver disease.</b> A dark circle sitting inside the central pallor gives the bullseye. The cause is <b>redundant cell membrane</b> &mdash; too much membrane for the volume of cell."),

 ("s044_1.png", "teardrop-cells", 44,
  "Blood smear with blue arrows pointing to red cells drawn out into a teardrop shape at one end.",
  "<b>Teardrop cells, or dacrocytes &mdash; bone marrow disease.</b> The shape records what happened to them: these formed in marrow <b>infiltrated by scar tissue or cancerous cells</b> and were deformed getting out."),

 ("s045_1.png", "basophilic-stippling", 45,
  "Blood smear with arrows pointing to red cells filled with fine blue-black dots spread evenly across the cytoplasm.",
  "<b>Basophilic stippling &mdash; lead poisoning.</b> Fragments of ribosomal RNA, and the diagnostic feature is that they are <b>evenly distributed throughout the cytoplasm</b>. Compare the single, solitary Howell-Jolly body below."),

 ("s046_1.png", "howell-jolly", 46,
  "Blood smear with a Howell-Jolly body circled in blue and a target cell boxed in pink, plus arrows to further examples.",
  "<b>Howell-Jolly body (blue circle) and target cell (pink box) &mdash; both post splenectomy.</b> A single dark purple dot of residual nuclear fragment. The spleen normally strips these out, so <b>finding one means the spleen is absent or not working</b> &mdash; and the target cells in the same field are the second consequence of the same thing."),

 ("s047_1.png", "heinz-bodies", 47,
  "Diagram headed Heinz Bodies showing a red cell with purple-blue inclusions at its edge, captioned that they appear after supravital staining with new methylene blue and are composed of denatured precipitated hemoglobin.",
  "<b>The most easily missed fact in this lecture, and it is only in this picture.</b> Heinz bodies need a <b>supravital stain &mdash; new methylene blue</b>. They are <b>invisible on the routine Wright stain</b> used for the rest of the differential, so they will not be reported unless someone asks for them. Denatured hemoglobin at the cell periphery; G6PD deficiency."),

 ("s048_1.png", "rouleaux", 48,
  "Blood smear annotated note the red cells in a coin-stacking formation, with arrows to several stacks of red cells lying face to face in chains.",
  "<b>Rouleaux &mdash; multiple myeloma and liver disease.</b> Rows of coins. Red cells normally repel each other because they carry a negative surface charge; <b>raised serum proteins neutralise that charge</b> and let them stack. Contrast agglutination, which is disorderly clumping from antibody bridging."),

 ("s063_1.png", "iron-comparison", 63,
  "Table of condition against mean corpuscular volume, iron, ferritin, total iron binding capacity, transferrin and transferrin saturation, with arrows for six conditions: iron deficiency, inflammatory anaemia, thalassaemia minor and major, sideroblastic anaemia and iron overload.",
  "<b>The single highest-yield table in the lecture, and the slide's only text is its title.</b> Read the first two rows against each other: <b>iron deficiency has LOW ferritin with HIGH binding capacity</b>, inflammatory anaemia has <b>HIGH ferritin with LOW binding capacity</b>. Ferritin is an acute phase reactant, so it rises in inflammation even while the iron is unavailable. <b>Thalassaemia minor is the row where everything except the cell size is normal.</b>"),

 ("s071_1.png", "anemia-algorithm", 71,
  "Flowchart beginning review the history, complete blood count, mean corpuscular volume and reticulocyte count, branching on mean corpuscular volume under 80, 80 to 100, and over 100, each branch listing common causes and next steps.",
  "<b>The full anemia algorithm. Slide 71 extracts as completely empty &mdash; this figure is the entire slide.</b> Two things worth noticing: <b>iron deficiency appears in BOTH the under-80 and the 80-to-100 branches</b>, which is why iron studies are obtained even when the cell size is normal; and in the microcytic branch you obtain iron studies <b>in all individuals</b>, because a coexisting iron deficiency can mask thalassaemia on hemoglobin analysis."),

 ("s072_1.png", "fishbone", 72,
  "The CBC fishbone shorthand: a horizontal line with white cell count at the left end, hemoglobin above the centre, hematocrit below the centre, and platelets at the right end.",
  "<b>The fishbone, which is how a complete blood count gets written on a whiteboard or a progress note.</b> <b>White cells left, hemoglobin above the line, hematocrit below it, platelets right.</b> Worth knowing cold &mdash; you will see it written this way long before you see it typed out."),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    missing = [f for f, *_ in FIGURES if not os.path.exists(os.path.join(SRC, f))]
    assert not missing, ("source image(s) not extracted -- re-run the deck extraction "
                         "before this script: %r" % missing)
    n = 0
    for fn, slug, slide, alt, caption in FIGURES:
        im = Image.open(os.path.join(SRC, fn)).convert("RGB")
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        dst = os.path.join(OUT, "%s.jpg" % slug)
        im.save(dst, "JPEG", quality=86, optimize=True)
        n += 1
    total = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT))
    print("wrote %d figure(s), %.2f MB total" % (n, total / 1e6))
    print("deck:", DECK)


if __name__ == "__main__":
    main()
