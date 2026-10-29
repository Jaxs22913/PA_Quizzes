# CMS I Exam 6, Lectures 35 (Asthma) and 36 (COPD): staged exam-level content

Built in worktree `PA_Quizzes-wt-cms6b` (branch `feat/cms-e6-l35-36`). Builder A owns every exam-level file;
nothing here is registered anywhere. Phase 2 (after A's branch is on main) splices these in.

| Staged file | Goes to (builder A's scaffold) |
|---|---|
| `l35/l35.html`, `l36/l36.html` | `tools/cms_e6_guide/l35.html`, `l36.html` (section numbers 3 and 4; ids `asthma`, `copd`; h3 ids start `l35-` / `l36-`). The objective-to-subsection table and "Answered in" cross-references are written at splice time. |
| `l35/l35_cram.py`, `l36/l36_cram.py` | `tools/cms_e6_cram/l35.py`, `l36.py` (same `TOPICS` row format as `l34.py`) |
| `l35/l35_arcade.json`, `l36/l36_arcade.json` | `tools/cms_e6_arcade/l35.json`, `l36.json` (same deck schema as `l34.json`; 70 + 76 atomic-fact cards) |
| `l35/l35_clinmedpro.json`, `l36/l36_clinmedpro.json` | lecture objects to append to the `lectures` list of `tools/clinmedpro/cms-e6.json` |
| `l35/l35_pip_cards_draft.json`, `l36/l36_pip_cards_draft.json` | drafts only (id, anchor `a`, title, keywords, questions, explanation); `u` and `h` are assigned by `tools/pip_explain.py` once the guide is built. Each card must be re-checked against the built guide. |

Quizzes (already rendered into `Clinical Medicine and Surgery I Exam 6/`): `asthma-quiz`, `asthma-quiz-version-2`,
`asthma-vignettes`, `asthma-vignettes-version-2`, `copd-quiz`, `copd-quiz-version-2`, `copd-vignettes`,
`copd-vignettes-version-2` (30 questions each, 240 total). To register: `index.html` entries, `scope.json`
globs (`Clinical Medicine and Surgery I Exam 6/asthma-*.html`, `copd-*.html`), group study, guide links
(`build_guide_links.py` then `check_guide_links.py --strict` once the guide has the passages).

Guide facts the quiz explanations rely on that the guide section must STATE (link audit): see the sections above;
extra lines added after review: wheeze can vanish because too little air moves; refractory asthma despite confirmed
adherence goes to a pulmonology or allergy specialist; meloxicam note; first-line controller note.

Sources: `tools/cms_e6l35_scope.py` and `cms_e6l36_scope.py` hold the lecturer, scope remarks, excluded slides and
contested items; pools are `cms_e6l3{5,6}_{pool,vig}_{a,b,c}.py`; partition `cms_e6l35_partition.py` (guards for both
lectures); renderer `render_cms_e6l35.py`.
