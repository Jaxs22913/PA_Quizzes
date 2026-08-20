#!/usr/bin/env python3
"""Fold the 2026-08-20 Abnormal Cell Growth recording into the Clin Path I guide
and cram sheet.

THIS LECTURE IS DIFFERENT FROM THE CMS ONES, and the difference is worth stating
rather than hiding. Professor Rappa does not signpost the exam at all: 84
minutes, and the only cue either transcription found is a rhetorical question he
asked the room. Notability's transcript found none. So there is nothing here to
re-weight -- no slide flagged, nothing excluded.

What there IS, in quantity, is teaching that never reaches a slide. He explains
almost every term through a clinical example, and the examples are the part
worth keeping: Barrett's oesophagus for metaplasia, cervical dysplasia for
dysplasia, bodybuilding for hypertrophy, and the vascular anatomy of where a
cancer will go. He also states one link the slides do not make at all -- that
falling differentiation means a MORE AGGRESSIVE tumour.

Idempotent: fenced in <!--CPL3AUDIO--> and stripped before re-inserting.
"""
import os, re, sys, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 1")
GUIDE = os.path.join(DIR, "cp-exam-1-study-guide.html")
CRAM = os.path.join(DIR, "cp-exam-1-cram-sheet.html")
OPEN, CLOSE = "<!--CPL3AUDIO-->", "<!--/CPL3AUDIO-->"

BLOCK = OPEN + '''
  <div class="prof-flag"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 20 August 2026</span>
  <p><b>This lecture signposts nothing.</b> 84 minutes, cross-examined against Notability&rsquo;s
  independent transcript, and between them they contain <b>no statement about what is or is not on
  the exam</b> &mdash; the only cue either transcription flagged is a rhetorical question he asked
  the room. So unlike the dermatology lectures, there is nothing here to re-weight.</p>
  <p>What there is instead, in quantity, is <b>teaching that never reaches a slide</b>. Professor
  Rappa explains almost every term through a clinical example, and the examples are the part worth
  keeping.</p>
  <table>
    <tr><th>He said</th><th>Why it is worth having</th></tr>
    <tr><td><em>&ldquo;Someone with chronic gastro-oesophageal reflux&hellip; that acid that comes up, what do you think it does to the lower oesophagus?&hellip; it goes through a metaplasia. It turns from squamous to columnar cells. And that has a name. <mark class="prof-highlight">It&rsquo;s called Barrett&rsquo;s oesophagus</mark>&hellip; increased risk of oesophageal carcinoma.&rdquo;</em> [7:45]</td><td><b>The metaplasia example, and it is not on the slide.</b> The lower oesophagus is squamous and cannot resist acid, so chronic reflux drives it to columnar. Then the corollary he draws, which is the genuinely useful bit: in an oesophageal carcinoma, <b>squamous cells on the sample means a primary cancer; columnar cells means it is secondary to reflux.</b></td></tr>
    <tr><td><em>&ldquo;The best example I can give you is <mark class="prof-highlight">cervical dysplasia</mark>&hellip; usually caused by human papillomavirus. That might be archival one day because of the vaccine.&rdquo;</em> [10:47]</td><td>The dysplasia example. It also ties this lecture straight to the carcinogenesis section &mdash; human papillomavirus, E6 and E7, p53 and retinoblastoma protein.</td></tr>
    <tr><td><em>&ldquo;Striated muscle cells do not divide&hellip; you eat a lot of protein and then you increase your resistance&hellip; new actin and myosin&hellip; <mark class="prof-highlight">the muscle cell increases in size</mark>&hellip; so the skeletal muscles when they get bigger, it&rsquo;s because of hypertrophy.&rdquo;</em> [2:54]</td><td>Hypertrophy taught through weight training. Actin and myosin are proteins, proteins are built from amino acids, so more protein plus more resistance means <b>bigger fibres, not more fibres</b> &mdash; which is the whole distinction from hyperplasia.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">The more specialized the tissue is, the less it can proliferate.</mark> Do you think skeletal muscle is specialized? They don&rsquo;t proliferate&hellip; neurons don&rsquo;t replicate.&rdquo;</em> [6:08]</td><td><b>The organising principle behind &ldquo;permanent tissues&rdquo;.</b> Skeletal muscle and neurons are the two he named. It is also why hypertrophy is the only growth response available to them.</td></tr>
    <tr><td><em>&ldquo;As the degree of differentiation goes from well to anaplasia, <mark class="prof-highlight">the tumour becomes more aggressive</mark>. So an anaplastic carcinoma is very aggressive as opposed to a well differentiated carcinoma.&rdquo;</em> [24:08]</td><td><b>A link the slides do not make.</b> The deck gives grading as a scale of resemblance and stops there. He attaches the prognosis to it: <b>less differentiated means more aggressive.</b> He also notes anaplasia is <b>also called atypia</b>, and that differentiation is always judged against <b>the parent cell</b>.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">Who&rsquo;s the only one that can diagnose cancer? The pathologist.</mark> I don&rsquo;t care what type of symptoms you have, they&rsquo;re sending all the specimens to pathology.&rdquo;</em> [22:36]</td><td>Said twice, and it frames the whole grading section: grading is a histological judgement, made on tissue, by one person.</td></tr>
    <tr><td><em>&ldquo;Primary is gastrointestinal &mdash; where&rsquo;s the most common metastasis? Why? <mark class="prof-highlight">Because of the blood flow.</mark> Lung cancer, where do you think it&rsquo;s going to metastasize to? The brain. Why? Because from the lung goes to the left heart, and&hellip; to the internal carotid, right to the brain. <mark class="prof-highlight">So knowing the vasculature will tell you where there&rsquo;s possibly mets forming.</mark>&rdquo;</em> [53:20]</td><td><b>The slide says metastatic spread is not random and lists venous flow as a determinant. He shows you how to actually use that.</b> Gastrointestinal primary drains by the portal vein, so the liver. Lung cancer sits <em>downstream</em> of the pulmonary circulation, so its cells enter the left heart and go out the carotids &mdash; hence brain. Reason from the vessels and you can predict the site.</td></tr>
    <tr><td><em>&ldquo;Carcinoma in situ &mdash; <mark class="prof-highlight">the best way to think of that is carcinoma in SIGHT</mark>&hellip; the cancerous cells are there, but they have not broken through the basement membrane yet.&rdquo;</em> [13:41]</td><td>His mnemonic, and it lands on exactly the right feature: the basement membrane is the line, and once it is crossed the lesion is an <b>invasive</b> carcinoma.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">O-M-A is the suffix for tumour.</mark> And how do you pluralize that? Mistakenly most people put an S on it, like carcinomas. That&rsquo;s a misnomer. <mark class="prof-highlight">Carcinomata.</mark>&rdquo;</em> [34:36]; <em>&ldquo;adeno&hellip; means glandular&rdquo;</em> [35:49]; <em>&ldquo;leiomyosarcoma&hellip; smooth muscle. Rhabdo? Skeletal muscle.&rdquo;</em> [14:43]</td><td>The naming rule taken down to the morphemes, which is what makes it generalise: <b>-oma</b> = tumour, <b>adeno-</b> = glandular, <b>leio-</b> = smooth muscle, <b>rhabdo-</b> = skeletal muscle. He flags that full nomenclature comes later in the course.</td></tr>
    <tr><td><em>&ldquo;Epithelial tissue is avascular&rdquo;</em> [13:13]</td><td>Which is why the outermost layers slough off &mdash; they are the furthest from the nutrient supply. He uses it to explain what a normal epithelium looks like before showing what a dysplastic one looks like.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">Stop taking notes, just listen to me. Record me, and at home you can listen to me and pause.</mark>&rdquo;</em> [3:56]</td><td>His stated advice on how to take his lecture. Worth honouring &mdash; this guide exists partly so that is a workable strategy.</td></tr>
  </table>
  <p class="tag">Quoted from the 20 August 2026 lecture recording, with timestamps, and cross-examined
  against Notability&rsquo;s independent transcript. Where the recording and a slide disagree on a
  fact, the slide wins.</p>
  </div>
''' + CLOSE

CRAM_ROWS = [
 ("HE SIGNPOSTS NOTHING", "84 minutes, two independent transcriptions, and NO statement about what is or is not on the exam. Nothing was flagged and nothing was excluded. Study the twelve objectives evenly."),
 ("Metaplasia, his example", "CHRONIC GERD. The lower oesophagus is SQUAMOUS and cannot resist acid → metaplasia to COLUMNAR = BARRETT'S OESOPHAGUS → increased risk of oesophageal carcinoma. His corollary: in oesophageal carcinoma, SQUAMOUS cells on the sample = a PRIMARY cancer; COLUMNAR cells = SECONDARY TO REFLUX."),
 ("Dysplasia, his example", "CERVICAL DYSPLASIA, usually caused by HPV — which ties straight back to E6/E7, p53 and RB in the carcinogenesis section. “Might be archival one day because of the vaccine.”"),
 ("Hypertrophy, his example", "WEIGHT TRAINING. Striated muscle cells DO NOT DIVIDE. Protein + resistance → more ACTIN AND MYOSIN → each FIBRE gets bigger → the organ gets bigger. BIGGER FIBRES, NOT MORE FIBRES — that is the whole distinction from hyperplasia."),
 ("Why 'permanent tissues' matters", "“THE MORE SPECIALIZED THE TISSUE IS, THE LESS IT CAN PROLIFERATE.” Skeletal muscle and NEURONS are the two he named. Which is why hypertrophy is the only growth response available to them."),
 ("A LINK THE SLIDES DO NOT MAKE", "“As the degree of differentiation goes from well to anaplasia, THE TUMOUR BECOMES MORE AGGRESSIVE.” The deck gives grading as a scale of resemblance and stops. He attaches the prognosis. Also: ANAPLASIA = ATYPIA, and differentiation is always judged against THE PARENT CELL."),
 ("Who diagnoses cancer", "THE PATHOLOGIST — “the only one that can diagnose cancer”. Said twice. Grading is a histological judgement made on tissue."),
 ("How to PREDICT where mets go", "REASON FROM THE VESSELS. GI primary drains by the PORTAL VEIN → LIVER. LUNG cancer sits downstream of the pulmonary circulation, so its cells enter the LEFT HEART and go out the CAROTIDS → BRAIN. “Knowing the vasculature will tell you where there's possibly mets forming.”"),
 ("His carcinoma in situ mnemonic", "“Carcinoma in SIGHT.” The cancerous cells are THERE, but have NOT broken through the BASEMENT MEMBRANE. Once they do, it is an INVASIVE carcinoma."),
 ("Nomenclature down to the morphemes", "-OMA = tumour (plural CARCINOMATA, not carcinomas). ADENO- = glandular. LEIO- = smooth muscle (leiomyosarcoma). RHABDO- = skeletal muscle (rhabdomyosarcoma). Full nomenclature comes later in the course."),
 ("Why epithelium sloughs", "EPITHELIAL TISSUE IS AVASCULAR, so the outermost layers are furthest from the nutrient supply and slough off. That is what a NORMAL epithelium looks like, before you compare it with a dysplastic one."),
]


def main():
    g = open(GUIDE, encoding="utf-8").read()
    g = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), "", g, flags=re.S)
    i = g.index('id="abnormal-cell-growth"')
    j = g.index("</div>", g.index('<div class="io-box">', i))
    j = g.index("</div>", j + 6) + len("</div>")
    g = g[:j] + "\n\n  " + BLOCK + g[j:]
    assert g.count(OPEN) == g.count(CLOSE) == 1
    open(GUIDE, "w", encoding="utf-8").write(g)
    print("guide: Lecture 3 emphasis block added")

    c = open(CRAM, encoding="utf-8").read()
    if 'id="acg-lecture"' in c:
        print("cram: lecture rows already present")
        return
    rows = "\n".join('          <tr><td class="h">%s</td><td>%s</td></tr>' % (H.escape(a), H.escape(b))
                     for a, b in CRAM_ROWS)
    sec = ('\n  <section class="topic" id="acg-lecture" style="--acc:#8a3f4a;--acc-bg:#f3e3e6;'
           '--acc-zebra:#faf1f3;--acc-ink:#6d2f38">\n'
           '    <div class="shead"><span class="dot" style="background:#8a3f4a"></span>'
           '<h2>From the Abnormal Cell Growth Lecture Recording</h2></div>\n'
           '    <div class="scroll">\n      <table>\n'
           '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
           '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n' % rows)
    m = re.search(r'      <a href="#acg-staging"[^>]*>.*?</a>\n', c, re.S)
    assert m, "acg-staging jump link not found"
    link = ('      <a href="#acg-lecture" style="color:#6d2f38"><span class="dot" '
            'style="background:#8a3f4a"></span>From the Lecture Recording</a>\n')
    c = c[:m.end()] + link + c[m.end():]
    foot = "  <footer>"
    assert c.count(foot) == 1
    c = c.replace(foot, sec + "\n" + foot)
    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th"):
        o, cl = len(re.findall(r"<%s[ >]" % tag, c)), c.count("</%s>" % tag)
        assert o == cl, "%s: %d open, %d close" % (tag, o, cl)
    ids = set(re.findall(r'id="([^"]+)"', c))
    assert not [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', c) if a not in ids]
    assert "**" not in c
    open(CRAM, "w", encoding="utf-8").write(c)
    print("cram: %d lecture rows added" % len(CRAM_ROWS))


if __name__ == "__main__":
    main()
