#!/usr/bin/env python3
"""Star the SECOND half of Professor Gopal's Dermatology lecture (Clin Path I, L2).

The post-break recording synced to the Mac later on 2026-08-18, 41:02 covering
sections 2.5 and 2.6 — the conditions and the skin cancers. Those two sections
were carrying a callout saying no audio existed for them; this pass removes it
and replaces it with the marks it was standing in for.

The most useful cue here is a DE-emphasis, which is worth as much as a star.
On the hedgehog signaling pathway in basal cell carcinoma she said: "that is
very complicated, I totally went into the weeds trying to read about that
preparing for today's lecture, and it's beyond what we need to know — so you
just know that it's associated with that, but we don't need to know all the ins
and outs." A guide that treats every mechanism as equally weighted would have
you memorise exactly the thing she told the class to skip.

She also restated the course's scope line while introducing psoriasis: "today
the focus is really just the underlying pathophysiology" — which is the same
mechanism-not-management boundary the class runs on.

Idempotent. Run after mark_cp_guide_l2.py.
"""
import io, sys

G = "/Users/jaxonluke/Developer/PA_Quizzes/Clinical Pathophysiology I Exam 1/cp-exam-1-study-guide.html"

def flag(label, body):
    return ('<div class="prof-flag"><span class="prof-flag-label">&#9733; %s</span>\n  %s</div>'
            % (label, body))

STALE = ('<div class="callout"><strong>No recording past this point.</strong> The stars above come '
         'from the 2026-08-18 lecture recording, which covers only up to the mid-lecture break '
         '&mdash; at 34:42 she said &ldquo;we&rsquo;re about halfway through&rdquo;. Sections 2.5 '
         'and 2.6 are unmarked because there is no audio for them, <em>not</em> because she passed '
         'over them quickly. Treat the absence of a star here as missing data.</div>\n  ')

REPLACEMENT = flag("Professor emphasized",
  '<p><strong>Allergic contact dermatitis is a <em>delayed</em> hypersensitivity reaction.</strong> '
  '<em>&ldquo;The important thing to remember about allergic contact dermatitis is that it&rsquo;s a '
  'delayed hypersensitivity reaction, and it develops after you have an initial exposure and then '
  'you&rsquo;re re-exposed to it.&rdquo;</em> She walked both phases by name: <strong>sensitization</strong>, '
  'where Langerhans cells present haptens &mdash; the nickel or the poison ivy &mdash; to T cells and '
  'build memory, then <strong>elicitation</strong> on re-exposure. Contrast it with irritant contact '
  'dermatitis in the row below, which needs no prior exposure at all. That pairing is the '
  'discrimination worth holding.</p>')


def main():
    s = io.open(G, encoding="utf-8").read()
    if "hedgehog" in s.lower() and "prof-flag" in s and "beyond what we need to know" in s:
        print("second-half marks already present — nothing to do")
        return 0
    assert s.count(STALE) == 1, "the no-recording callout is not where it was left"
    s = s.replace(STALE, REPLACEMENT + "\n  ")
    added = 1

    # Psoriasis — the scope restatement plus the one-line definition she gave.
    a = "<tr><td>Psoriasis</td>"
    if s.count(a) == 1:
        i = s.index("</table>", s.index(a))
        s = s[:i + len("</table>")] + "\n  " + flag("Professor emphasized",
          '<p><strong>Psoriasis, in one sentence.</strong> <em>&ldquo;We could probably do an entire '
          'lecture on psoriasis alone &mdash; today the focus is really just the underlying '
          'pathophysiology &hellip; the important thing to understand about psoriasis is that it&rsquo;s '
          'a chronic autoimmune inflammatory condition that causes rapid proliferation of cellular '
          'growth.&rdquo;</em></p>'
          '<p>She noted you will meet it again in your other courses, which is the mechanism-not-'
          'management line this class runs on. Findings she named: well-demarcated patches with a '
          'characteristic <strong>silvery scale</strong>, anywhere but often the elbows, knees, scalp '
          'and lower back.</p>') + s[i + len("</table>"):]
        added += 1

    # The de-emphasis, which matters as much as any star.
    b = "hedgehog"
    j = s.lower().find(b)
    assert j != -1, "hedgehog pathway not found in the cancers section"
    j = s.index("</table>", j) + len("</table>")
    s = s[:j] + "\n  " + flag("Professor said you do NOT need this",
      '<p><strong>The hedgehog signaling pathway &mdash; know the association, not the detail.</strong> '
      '<em>&ldquo;That is very complicated. I totally went into the weeds trying to read about that '
      'preparing for today&rsquo;s lecture, and it&rsquo;s beyond what we need to know. So you just know '
      'that it&rsquo;s associated with that, but we don&rsquo;t need to know all the ins and outs of it, '
      'because it&rsquo;s very complicated.&rdquo;</em></p>'
      '<p>Basal cell carcinoma is the <strong>most common</strong> skin cancer; squamous cell carcinoma '
      'is the <strong>second most common</strong>. For squamous cell she did name a histological feature '
      'as pathognomonic &mdash; <strong>keratin pearls</strong>, also called epithelial pearls: '
      'millimetre-sized concentric deposits of keratin and dead skin cells. That one is worth knowing.</p>') + s[j:]
    added += 1

    io.open(G, "w", encoding="utf-8").write(s)
    print("applied %d blocks; guide now has %d boxed marks"
          % (added, s.count('class="prof-flag"')))
    return 0


if __name__ == "__main__":
    sys.exit(main())
