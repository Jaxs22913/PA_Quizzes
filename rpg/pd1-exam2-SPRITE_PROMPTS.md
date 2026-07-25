# Sprite Prompts — "The Long Survey" (PD1 Exam 2 RPG)

Prompts to generate every art asset the game needs, in **Gemini** (or any image
generator). The game ships with simple placeholder art; each asset below has a
**key** that maps to a slot in the game's `ART_OVERRIDES` block — generate the
image, then paste it in (instructions at the bottom) and it replaces the
placeholder with zero code changes.

**Genre/world:** post-apocalyptic. One ruined region descended top-to-bottom,
sunlit ridge → drowned undercity. Cohesive earthy palette (dust tan, rust,
weathered olive, ash grey, murky teal water) with warm-dusk light from the
upper-left. Protagonist: **Wren Calder, "the Surveyor"** — a lone wanderer who
crosses the dead sprawl on foot.

---

## HOW TO USE

1. Generate each asset with its prompt below (Gemini image gen / "create an image").
2. Ask for a **transparent background** and the **exact pixel size** noted.
3. Download the PNG. (If the tool won't do transparency, generate on a flat
   magenta `#ff00ff` background and say "background pure magenta for keying".)
4. Plug it in — see **PLUGGING IN** at the bottom.

## PASTE THIS STYLE BLOCK INTO EVERY PROMPT (the house style)

> High-fidelity 16-bit SNES JRPG pixel art, Chrono-Trigger / Secret of Mana era.
> Hand-shaded with 4–6 tones per material (base, two shadow depths, one–two
> highlights), one consistent light source from the upper-left, bold dark
> *colored* outlines (not pure black) plus lighter interior separations between
> materials, a subtle rim-light on the lit edge, clean anti-aliased curves, no
> stray pixels. Earthy post-apocalyptic palette — dusty tan, rust, weathered
> olive, ash grey. Single subject centered, transparent background, no text, no
> logo, no border, no drop shadow. Crisp pixels (nearest-neighbor), not blurry.

**Rules for every prompt:** original character only — do **not** copy or imitate
any existing game character. Keep the light from the upper-left and the palette
earthy so all assets read as one world.

---

## 1 · HERO — Wren Calder, the Surveyor  (24×32 each, transparent)

Base description to reuse: *"an original lone post-apocalyptic surveyor: a lean
traveller in a weathered open duster over a canvas utility harness, a rust dust-
scarf at the neck, brass goggles pushed up on the forehead, a satchel and a
utility belt with pouches, worn trousers and scuffed boots, gloved hands,
determined calm face."*

| Key | Prompt (append the style block) |
|---|---|
| `hero_front_idle` | [base description], **facing the camera, standing idle**, full body, 24×32. |
| `hero_front_walk1` | [base description], facing camera, **mid-stride left foot forward**, 24×32 (walk frame A). |
| `hero_front_walk2` | [base description], facing camera, **mid-stride right foot forward**, 24×32 (walk frame B). |
| `hero_back_idle` | [base description], **seen from behind** (back of hood/hair, duster back, no face), standing, 24×32. |
| `hero_back_walk1` | back view, mid-stride left foot forward, 24×32. |
| `hero_back_walk2` | back view, mid-stride right foot forward, 24×32. |
| `hero_side_idle` | [base description], **strict side profile facing right**, standing, 24×32. |
| `hero_side_walk1` | side profile facing right, mid-stride, 24×32. |
| `hero_side_walk2` | side profile facing right, other mid-stride, 24×32. |
| `hero_battle_idle` | [base description], **side view facing right in a ready combat stance**, weight low, 24×32 (used in the fight screen). |
| `hero_battle_attack` | same character, **lunging forward striking with a scavenged tool/blade**, 24×32 (attack frame). |

*(Left-facing frames are auto-mirrored in-engine — you only need the right-facing side.)*

---

## 2 · ENEMIES — one per district  (24×28 each; give front idle + a battle idle)

Each is an original wasteland figure themed to its district. For each, generate
at least `<key>_front` (map roaming sprite) and `<key>_battle` (fight-screen,
facing left). Optional `<key>_walk1/2` for roaming animation.

| Key | District | Prompt subject (append style block) |
|---|---|---|
| `enemy_rise` | Vantage Rise | a ragged ridge lookout in a patched cloak with a spyglass and a tally-stick, wary posture. |
| `enemy_tannery` | The Tannery Rows | a hide-market toll-taker wrapped in stitched leather and drying-rack scraps, heavy gloves. |
| `enemy_hollow` | Echo Hollow | a ravine ambusher in muffled rags and a signal-horn, crouched and listening. |
| `enemy_lantern` | Lantern Watch | a glass-foundry crewman in a soot apron and cracked goggles, holding a glass shard tool. |
| `enemy_bellows` | The Bellows Yards | a soot-caked bellows-hand in a leather breather mask, gripping a stoking iron. |
| `enemy_pump` | The Pump Works | a pipe-bridge guard in oilskins and a valve-wrench, planted stance. |
| `enemy_provision` | The Provision Halls | a granary guard in a grain-dusted coat with a sealed satchel and a flail. |
| `enemy_outflow` | The Outflow | a sluice gatekeeper in waders and a rusted gate-key, dripping. |
| `enemy_cistern` | The Deep Cistern | an elite cistern sentry in dark waterproof plate with a pale lantern, imposing. |

---

## 3 · BOSSES — one per district, escalating  (40×48 each; battle-facing left)

Bigger, intimidating silhouettes, one memorable feature each. Generate
`<key>_battle` (idle, facing left); optional `<key>_attack` and `<key>_hit`.

| Key | Boss (district) | Prompt subject (append style block) |
|---|---|---|
| `boss_warden` | The Warden of the Rise (1) | an imposing checkpoint warden in a heavy plated coat, a brass tally-badge, holding a barrier staff. |
| `boss_baron` | The Patchwork Baron (2) | a scavenger-king cloaked in a hundred stitched hides, a crown of nails, broad and gaudy. |
| `boss_crier` | The Crier (3) | a wiry demagogue wired to a bank of salvaged loudspeakers, a horn-mask, cables trailing. |
| `boss_lamplighter` | The Lamplighter (4) | a gaunt figure atop a great cracked lens, hands on searchlight beams, glass-and-brass rig. |
| `boss_stoker` | The Stoker (5) | a hulking foundry master in fireproof leathers and a glowing bellows-iron, embers rising. |
| `boss_valvemaster` | The Valvemaster (6) | a barnacled figure fused to a giant pipe-junction wheel, dripping, many valves. |
| `boss_miller` | The Miller (7) | a bloated hoarder throned on a great grain-wheel, sacks and scales, a heavy ledger. |
| `boss_sluicewarden` | The Sluicewarden (8) | a tall drowned-looking warden of the gates in streaming waders, a huge sluice key. |
| `boss_reclaimer` | The Reclaimer (9, FINAL) | the calm, still mastermind on a causeway over black water — long coat, still water reflecting, quietly menacing, the most refined silhouette. |

---

## 4 · TILES — 16×16 each, must tile seamlessly

Ask for: *"a single seamless 16×16 top-down pixel-art terrain tile that tiles
edge-to-edge, [subject], "* + style block. Generate 2–3 **variants** of ground
tiles to break repetition.

| Key | Prompt subject |
|---|---|
| `tile_earth` | dry cracked wasteland earth with small pebbles and hairline cracks, dusty tan. |
| `tile_earth_b` | same cracked earth, a different scatter of pebbles/cracks (variant). |
| `tile_road` | broken asphalt road, cracked slabs, faded, ash grey. |
| `tile_road_edge` | broken asphalt with dry dirt intruding on one edge (road-to-earth transition). |
| `tile_wall` | ruined brick/concrete wall with rust streaks, top-down thickness. |
| `tile_water` | murky teal-grey standing water with faint highlights. |
| `tile_shore` | murky water meeting a jagged sandy/mud earth edge (water-to-earth transition). |
| `tile_cliff` | dark rocky cliff face / rubble edge, top-down. |
| `tile_rubble` | a pile of broken concrete rubble and rebar, walkable-blocking. |

## 5 · PROPS — small objects, transparent, various sizes

*"a single top-down 16-bit pixel-art [subject], transparent background,"* + style block.

| Key | Subject | Size |
|---|---|---|
| `prop_crate` | a weathered wooden scrap crate | 16×16 |
| `prop_barrel` | a rusted metal barrel | 16×16 |
| `prop_signpost` | a leaning wooden signpost with a blank board | 16×20 |
| `prop_lamppost` | a broken street lamp post, dark | 16×28 |
| `prop_campfire` | a small campfire in a ring of stones, warm glow | 16×16 |
| `prop_chest` | a battered lockbox / footlocker, closed | 16×14 |
| `prop_drying_rack` | a tanner's drying rack with hanging hides | 20×20 |
| `prop_pipe` | a large rusted pipe segment | 20×16 |

## 6 · BACKDROPS + FX

| Key | Prompt | Size |
|---|---|---|
| `backdrop_generic` | a wide 16-bit JRPG battle backdrop of ruined post-apoc ground under a dusk sky, dithered gradient, empty foreground for combatants | 320×180 |
| `portal_ring` | a glowing rust-orange circular portal/vortex ring on transparent background, concentric energy | 128×128 |
| `fx_slash` | a quick white-and-rust pixel slash effect, transparent | 32×32 |

*(One shared `backdrop_generic` is fine to start; later you can make one per
zone by recoloring to each district's palette.)*

---

## PLUGGING IN — no code editing, no base64

The game now has a built-in sprite loader on its start screen. **Name each PNG
exactly after its asset key** (the key from the tables above) and you're done:

| Asset key | File to save |
|---|---|
| `hero_front_idle` | `hero_front_idle.png` |
| `enemy_rise` | `enemy_rise.png` |
| `boss_warden` | `boss_warden.png` |
| …every key in this doc | `<key>.png` |

Then, on the game's launch screen (**The Long Survey** title screen):

1. Click **🎨 Load sprite folder** and pick the folder Gemini gave you — *or*
   just **drag the PNG files anywhere onto the screen**.
2. Every file whose name matches an asset key swaps in instantly; the status
   line shows `N / 53 sprites loaded`. Unmatched names are reported in a toast
   so you can spot typos.
3. Your sprites are **remembered** (saved in the browser), so they're still
   there next time you open the game. **Clear sprites** reverts to placeholders.

Notes:
- `.png`, `.jpg`, `.gif`, and `.webp` all work; matching ignores case and the
  file extension, so `Hero_Front_Idle.PNG` still maps to `hero_front_idle`.
- Any key you don't provide keeps its built-in placeholder, so you can drop art
  in a few at a time and the game always runs.
- Tell Gemini (per the folder instruction below) to name every exported file
  exactly by its asset key — that's the only thing the loader needs.
