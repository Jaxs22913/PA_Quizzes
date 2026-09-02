# Quiz template (exam-navigator engine)

This is the standard engine for every quiz on the site going forward. It replaced the
older "common engine" (`startBtn`/`checkAnswer()`, immediate per-question feedback with
no exam mode) in July 2026 — all 162 remaining common-engine files were converted to this
template. Do not build new quizzes on the old engine.

Features: timer, Exam Mode (flag questions, jump-to-question navigator, no feedback until
submit), shuffle-question-order toggle, cross-out wrong choices, pause/resume overlay,
results screen with score ring + "Performance by objective" breakdown + full missed-question
review, resume-in-progress via localStorage. Relies on shared `theme.js` helpers already
loaded site-wide: `window.openPauseOverlay`, `window.startExamModeTour`, `window.openQuestionNav`.

## Native question schema (preferred for new content)

```json
{
  "topic": "Short topic label",
  "io": "Objective/topic grouping used for the results breakdown",
  "q": "Question text",
  "opts": [
    ["Choice A text", "Explanation shown under this choice after answering"],
    ["Choice B text", "..."],
    ["Choice C text", "..."],
    ["Choice D text", "..."]
  ],
  "c": 2,
  "cite": "Source citation, e.g. lecture/PPT name"
}
```

`c` is the index (0-3) of the correct choice. Give every option its own real explanation —
don't reuse one generic "why" string across all wrong choices; that's only what the legacy
converter did because the old schema didn't have per-option text.

### Picture questions

Three optional fields put a photograph above the stem — added for "Guess that Disease"
(CMS I Exam 2), where the picture *is* the question:

```json
{
  "img": "cms-ophtho-chart-images/s012_1.jpg",
  "alt": "Lower eyelid with the margin turned inward against the globe",
  "slide": "Slide 12"
}
```

`img` is relative to the rendered quiz file. `alt` is the screen-reader description — write
what is visible, not the diagnosis, or you have given the answer away. `slide` is the caption
printed under the picture; keep the full deck citation in `cite` as usual.

The picture is rendered in the live question card, in the Exam Mode scroll column and in the
end-of-quiz review. `theme.js` arms it for click-to-enlarge automatically. Questions without
`img` are unaffected — the figure element stays hidden.

Note that `tools/build_group_quizzes.py` drops any quiz containing a picture question: Group
Study is text-only, and "name this photograph" without the photograph is not a question.

### Grouping by something other than an objective

`io` drives the results breakdown and the chip above the stem. It is normally an instructional
objective, and the engine prefixes "Objective " to it. A label starting with `Objective` or
`Region` is left as written — a picture quiz groups by anatomical region, and
"Objective Region — Cornea" reads as a mistake.

## Usage — building a brand-new quiz

```python
import sys
sys.path.insert(0, "/Users/jaxonluke/Developer/PA_Quizzes/tools/quiz-template")
from render import render

html = render(
    title="Page <title>",
    h1="On-page heading",
    sub="Subheading under the title",
    pill="30 questions",
    chips=["Topic A", "Topic B", "Topic C"],   # short list, shown as chips on the start screen
    intro="One or two sentences shown on the start screen before the quiz begins.",
    questions=questions,          # list of dicts in the native schema above
    already_converted=True,
    navy="#123456", indigo="#654321", gold="#abcdef", ice="#eef2ff",
)
open("path/to/output-quiz.html", "w", encoding="utf-8").write(html)
```

Pick `navy`/`indigo`/`gold`/`ice` to match the class/exam's established color identity where
one exists (see other quizzes in the same folder). For a brand-new class/exam, choose a fresh
4-color set with enough contrast (navy+indigo drive the header gradient and buttons; ice is
a light chip/tag background — should read as "light" against navy text).

## Converting legacy content

If you're starting from the old `{topic,q,choices,answer,correct,why,src}` schema, call
`render()` without `already_converted` (defaults to `False`) and pass `oxblood`/`brass`/`teal`
instead of the 4-slot palette — `derive_palette()` will map the 3-color scheme onto navy/
indigo/gold/ice automatically. This is a lossy path (every wrong choice shares one "why"
string) — prefer authoring directly in the native schema for new content.

## After building or regenerating any quiz

Run `tools/check_answer_distribution.py` against the new file(s) — see that script and the
`answer_position_bias_check` memory for why this is mandatory.
