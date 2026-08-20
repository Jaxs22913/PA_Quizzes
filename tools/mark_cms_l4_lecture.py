#!/usr/bin/env python3
"""Fold the 2026-08-19 Cutaneous Bacterial Infections recording into the CMS I
Exam 1 guide and cram sheet.

The single most useful thing in 73 minutes is not a fact but a heuristic the
professor gave out loud: "The staph aureus, it causes a lot of these conditions.
You don't know the answer, guess staph aureus." That is exam-taking advice from
the person writing the exam, and it goes at the top.

Idempotent: fenced in <!--CMSL4AUDIO--> and stripped before re-inserting.
"""
import os, re, sys, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
GUIDE = os.path.join(DIR, "cms-exam-1-study-guide.html")
CRAM = os.path.join(DIR, "cms-exam-1-cram-sheet.html")
OPEN, CLOSE = "<!--CMSL4AUDIO-->", "<!--/CMSL4AUDIO-->"

BLOCK = '''%s
  <div class="prof-flag"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 19 August 2026</span>
  <p>73 minutes of audio. One heuristic, one slide flagged out loud, and several prescribing details
  that are not on any slide.</p>
  <table>
    <tr><th>She said</th><th>What it means for you</th></tr>
    <tr><td><em>&ldquo;Staph aureus also for this is most common. If you guys know, this is the theme. The staph aureus, it causes a lot of these conditions. <mark class="prof-highlight">You don&rsquo;t know the answer, guess staph aureus.</mark>&rdquo;</em> [1:04:05]</td><td><b>Exam-taking advice from the person teaching the exam.</b> Across this whole lecture &mdash; folliculitis, furuncle, carbuncle, abscess, impetigo, cellulitis &mdash; <em>Staphylococcus aureus</em> is the recurring answer. Know the exceptions properly (erysipelas and ecthyma lean streptococcal, hot tub folliculitis is <em>Pseudomonas</em>), and let staph be the default everywhere else.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">These are really important slides right here. Okay, 32 and 33, make sure you know this.</mark>&rdquo;</em> [15:40]</td><td>The <b>acne treatment ladder</b>. She named these two slides specifically, which is as direct a flag as this lecture gives. Mild comedonal &rarr; topical retinoid, or azelaic acid if not tolerated. Mild mixed with pustules &rarr; topical antimicrobial (benzoyl peroxide) plus a topical retinoid, or benzoyl peroxide plus a topical antibiotic. Moderate &rarr; topical retinoid + <b>oral</b> antibiotic + benzoyl peroxide. Severe &rarr; the same three, or <b>oral isotretinoin</b>.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">Bactroban, something you should know this antibiotic</mark>, just because it&rsquo;s something that you&rsquo;re going to prescribe quite a bit&hellip; it has to be the <mark class="prof-highlight">ointment, don&rsquo;t write the cream</mark>, because the cream for some reason is like a hundred times the price&hellip; it&rsquo;s never covered.&rdquo;</em> [21:52]</td><td>Mupirocin is the prescription version of what patients buy over the counter. <b>Write the ointment, not the cream</b> &mdash; the ointment is covered by insurance and the cream is not. A prescribing detail that appears on no slide and will save a patient a phone call.</td></tr>
    <tr><td><em>&ldquo;Keflex, that&rsquo;s like the most common medication that we use, and MRSA suspected you will add on Bactrim&hellip; <mark class="prof-highlight">cephalexin plus Bactrim double strength is what we&rsquo;ll do if it&rsquo;s MRSA.</mark>&rdquo;</em> [23:16]</td><td>Her simplified default. <b>Cephalexin</b> as the standard oral agent; <b>add trimethoprim-sulfamethoxazole double strength</b> when methicillin-resistant <em>Staphylococcus aureus</em> is suspected, because the combination is broad enough to cover before susceptibilities return. Susceptibility testing then confirms.</td></tr>
    <tr><td><em>Nasal mupirocin <mark class="prof-highlight">twice a day for five days</mark> &ldquo;will kill the colonization within their nose&rdquo;</em> [22:56]</td><td>For <b>recurrent</b> folliculitis, check whether the patient is a <em>Staphylococcus aureus</em> carrier and decolonise the nares. She notes the pre-filled swabs were discontinued, so it is applied manually now.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">I ask them to come back 24 to 48 hours</mark> and make sure it&rsquo;s effective, because this spreads so fast.&rdquo;</em> [1:01:43]</td><td>On cellulitis. Non-purulent cellulitis over a small surface area is treated with outpatient oral antibiotics &mdash; but with a <b>mandatory 24-to-48-hour review</b>. That interval is the safety net, and it is the kind of thing a management question turns on.</td></tr>
    <tr><td><em>&ldquo;Have you guys ever heard of flesh-eating bacteria? &hellip; <mark class="prof-highlight">That&rsquo;s what this is.</mark>&rdquo;</em> [1:10:07]</td><td>Necrotizing fasciitis. She then gives the microbiology plainly: <b>polymicrobial</b>, aerobic or anaerobic from mixed flora, or <b>group A <em>Streptococcus</em></b>.</td></tr>
    <tr><td><em>&ldquo;You don&rsquo;t want to apply the topical tretinoin and benzoyl peroxide together&hellip; <mark class="prof-highlight">tretinoin is usually always done at night, benzoyl peroxide you can do during the day.</mark>&rdquo;</em> [16:30]</td><td>Acne patient education, none of it on a slide: separate the two because of irritation; <b>do not wash the face more than twice a day</b>; gentle cleanser with <b>warm, not hot</b> water because hot strips the barrier; avoid oil-based make-up; <b>four to six weeks to improve</b>; and <b>do not pick</b>, because picking is what scars.</td></tr>
    <tr><td><em>&ldquo;Pseudofolliculitis&hellip; <mark class="prof-highlight">most commonly occurs on black and brown males</mark>, or has curlier facial or body hair. This is what this normally &mdash; you will see this, very very common.&rdquo;</em> [26:14]</td><td>She was explicit about who gets it and why &mdash; hair curvature, not hygiene &mdash; and about how often you will see it.</td></tr>
    <tr><td><em>&ldquo;Shaving &mdash; that&rsquo;s where I see this by far most common&hellip; <mark class="prof-highlight">particularly the groin area</mark>&hellip; usually it&rsquo;s abrupt eruption, hot tubs too.&rdquo;</em> [17:37]</td><td>On folliculitis. Her clinical experience puts the groin and shaving first, and hot tubs second &mdash; and hot tub folliculitis is the one that is <em>Pseudomonas</em> rather than staph.</td></tr>
  </table>
  <p class="tag">Quoted from the 19 August 2026 lecture recording, with timestamps. Where the recording
  and a slide disagree on a fact, the slide wins; where the recording adds a prescribing detail the
  slide does not carry, it is recorded here as hers.</p>
  </div>
%s''' % (OPEN, CLOSE)

CRAM_ROWS = [
 ("HER EXAM HEURISTIC", "“You don't know the answer, GUESS STAPH AUREUS.” Her words. Staph aureus is the recurring organism across folliculitis, furuncle, carbuncle, abscess, impetigo and cellulitis. Know the EXCEPTIONS properly — erysipelas and ecthyma lean STREPTOCOCCAL, hot tub folliculitis is PSEUDOMONAS — and default to staph everywhere else."),
 ("Slides she named out loud", "“These are really important slides right here. 32 and 33, MAKE SURE YOU KNOW THIS.” The ACNE TREATMENT LADDER. Mild comedonal → topical retinoid (azelaic acid if not tolerated). Mild mixed/pustular → benzoyl peroxide + topical retinoid, OR benzoyl peroxide + topical antibiotic. Moderate → topical retinoid + ORAL antibiotic + benzoyl peroxide. Severe → same three, or ORAL ISOTRETINOIN."),
 ("Bactroban: OINTMENT, not cream", "Mupirocin — the prescription version of over-the-counter triple antibiotic. WRITE THE OINTMENT: the cream is roughly a hundred times the price and is NEVER COVERED; the ointment is. Not on any slide."),
 ("Her default oral antibiotics", "CEPHALEXIN (Keflex) is the most common agent. IF MRSA IS SUSPECTED, ADD TRIMETHOPRIM-SULFAMETHOXAZOLE DOUBLE STRENGTH — the combination is broad enough to cover before susceptibilities return, and susceptibility testing then confirms."),
 ("Decolonising a staph carrier", "For RECURRENT folliculitis: check whether they carry staph aureus, then NASAL MUPIROCIN TWICE A DAY FOR FIVE DAYS. The pre-filled swabs were discontinued, so it is applied manually."),
 ("The cellulitis safety net", "Non-purulent cellulitis, small surface area → outpatient oral antibiotics. BUT “I ask them to come back 24 TO 48 HOURS and make sure it's effective, BECAUSE THIS SPREADS SO FAST.” That interval is the answer to a follow-up question."),
 ("Necrotizing fasciitis in one line", "“Flesh-eating bacteria.” POLYMICROBIAL — aerobic or anaerobic from mixed flora — or GROUP A STREPTOCOCCUS."),
 ("Acne education, none of it on a slide", "DON'T apply tretinoin and benzoyl peroxide TOGETHER (irritation): RETINOID AT NIGHT, BENZOYL PEROXIDE BY DAY. Don't wash the face more than TWICE a day. Gentle cleanser, WARM NOT HOT water (hot strips the barrier). Avoid oil-based make-up. FOUR TO SIX WEEKS to improve. DON'T PICK — picking is what scars."),
 ("Pseudofolliculitis barbae — who", "Most commonly BLACK AND BROWN MALES, or anyone with CURLIER facial or body hair. Hair curvature, not hygiene. “Very, very common.”"),
]


def main():
    g = open(GUIDE, encoding="utf-8").read()
    g = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), "", g, flags=re.S)
    anchor = 'id="cutaneous-bacterial"'
    i = g.index(anchor)
    j = g.index("</div>", g.index('<div class="io-box">', i))
    j = g.index("</div>", j + 6) + len("</div>")
    g = g[:j] + "\n\n  " + BLOCK + g[j:]
    assert g.count(OPEN) == g.count(CLOSE) == 1
    open(GUIDE, "w", encoding="utf-8").write(g)
    print("guide: Lecture 4 emphasis block added")

    c = open(CRAM, encoding="utf-8").read()
    if 'id="bacterial-lecture"' in c:
        print("cram: lecture rows already present")
        return
    rows = "\n".join('          <tr><td class="h">%s</td><td>%s</td></tr>' % (H.escape(a), H.escape(b))
                     for a, b in CRAM_ROWS)
    sec = ('\n  <section class="topic" id="bacterial-lecture" style="--acc:#8a3f4a;--acc-bg:#f3e3e6;'
           '--acc-zebra:#faf1f3;--acc-ink:#6d2f38">\n'
           '    <div class="shead"><span class="dot" style="background:#8a3f4a"></span>'
           '<h2>From the Bacterial Infections Lecture Recording</h2></div>\n'
           '    <div class="scroll">\n      <table>\n'
           '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
           '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n' % rows)
    m = re.search(r'      <a href="#bacterial-spreading"[^>]*>.*?</a>\n', c, re.S)
    assert m, "bacterial-spreading jump link not found"
    link = ('      <a href="#bacterial-lecture" style="color:#6d2f38"><span class="dot" '
            'style="background:#8a3f4a"></span>From the Bacterial Lecture</a>\n')
    c = c[:m.end()] + link + c[m.end():]
    j = c.index('<section class="topic" id="infestations-1"')
    j = c.rindex("\n", 0, j)
    c = c[:j] + sec + c[j:]

    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th"):
        o, cl = len(re.findall(r"<%s[ >]" % tag, c)), c.count("</%s>" % tag)
        assert o == cl, "%s: %d open, %d close" % (tag, o, cl)
    ids = set(re.findall(r'id="([^"]+)"', c))
    assert not [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', c) if a not in ids], "dangling jump link"
    assert "**" not in c
    open(CRAM, "w", encoding="utf-8").write(c)
    print("cram: %d lecture rows added" % len(CRAM_ROWS))


if __name__ == "__main__":
    main()
