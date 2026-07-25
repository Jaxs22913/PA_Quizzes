## ⓪ SEND THIS MESSAGE FIRST (as its own message, before pasting the brief below)

> OK, I am about to give you a prompt to follow, Read it carefully and slowly because it is important you understand it and follow it throughly. Do not use previous memory or files in this chat only what is sent or made here. Are you ready and do you understand?

*(Wait for it to confirm it's ready, then paste everything below this line as the next message.)*

---

# THE LONG SURVEY — Game Art Brief

## 1. WHO YOU ARE / WHAT THIS IS

**You are the game's art director and artist. Your job is to CREATE and export the image assets described in this brief** — this is a request to *draw and deliver PNG image files*, not a document to review, rewrite, or summarize.

*The Long Survey* is a 2D top-down role-playing game. A developer will handle all the technical wiring (slicing sheets into frames, smoothing playback, loading files, placing them in the game). **You just create clean, correctly-named, correctly-formatted image files.**

**Do not start drawing yet.** Read this entire brief top to bottom. Then, as your **first action**, build the workflow plan described in Section 5 and wait for me to tell you to begin. Sections 2–4 tell you *how* to make the art, *what world* it lives in, and *exactly which files* to produce.

---

## 2. RULES FOR ART CREATION & FILE FORMAT

These rules apply to **every** asset. This is the part that usually goes wrong, so follow it exactly.

### 2a. One asset = one file (never a contact sheet)

**Each asset is its own standalone PNG, at its own listed dimensions, generated one at a time.** Do **NOT** pack multiple assets into a single picture — no contact sheet, no "texture atlas", no sample grid, no catalog page, no montage where different assets sit in one image separated by lines or cells.

**HOW TO ACTUALLY DO THIS (critical — this is where it keeps going wrong):**
- **Run a SEPARATE image generation for EVERY asset. One generation = one asset = one file.** If a batch has 7 tiles, that is **7 separate image generations producing 7 separate images**, NOT one image generation that draws all 7. Never place two different assets in the same generated image for any reason.
- **Do NOT create a "preview", "overview", "summary", or "here's what I made" image that shows several assets together.** Even as a preview or mockup, a grid of multiple assets is forbidden. Show me the individual images only.
- **Do NOT print the filename, a caption, a title, or any label under, over, or beside the image.** The Asset ID is the file's *name*, not text drawn on or around the picture. Zero text pixels.

- ✅ **Correct:** `tile_earth` is its own 64×64 image from its own generation. `tile_road` is a *different, separate* generation and file. Each character is its own file.
- ❌ **Wrong:** one image showing many tiles/characters arranged in a grid, or a labeled sheet with filenames printed under each thumbnail. That is unusable — the developer cannot cut a game out of a poster.
- ⚠️ **The one exception** is an animation **sprite sheet** — the frames of *ONE animation for ONE character* laid left-to-right (e.g. `hero_walk_side` = 4 poses of the same hero, in one strip). That counts as one asset. Different characters or different assets still never share an image.

**Name every file exactly by its Asset ID** (e.g. `hero_walk_side.png`, `backdrop_rise.png`) — as the file's name, never as text inside the image.

### 2b. Backgrounds — transparency where it belongs, otherwise a flat key color

The developer needs to cleanly separate characters and effects from their backgrounds, so backgrounds must be either **true transparency** or **one flat, uniform color** — **never** a painted checkerboard, gradient, card/frame, white fill, or scenery.

- **Character sprites & sprite sheets** (hero, enemies, bosses): **deliver a true transparent PNG (real alpha) if your image export genuinely supports transparency.** If it does not — if it would bake in any solid fill — then instead fill the whole background with **solid, uniform bright-magenta `#ff00ff`** (magenta appears nowhere in the earthy art, so the developer keys it out perfectly). Either a truly transparent background or flat magenta is fine; a baked white/grey/checkerboard background is not.
- **Glowing / energy effects** (`fx_portal`, `fx_transition`, `fx_slash`, `fx_hit`, `fx_heal`, `fx_levelup`): draw the effect on a **solid pure-black background `#000000`.** (Keep these on black even if you can do transparency — the developer composites them additively so the black vanishes and only the light shows, which makes glows look brighter than plain alpha would.)
- **Tiles & battle backdrops:** fully **opaque**, filling the whole image edge to edge. There is no background to remove.

### 2c. Animations = sprite sheets (never separate frames)

**Do NOT deliver animation frames as separate images** — drawn independently they jitter, because the character subtly changes between them.

**Instead, deliver each animation as ONE image: a horizontal strip ("sprite sheet") with every frame side by side, drawn together so the character stays identical frame to frame.** Only the pose changes.

- Frames laid **left → right**, evenly spaced, **equal-width cells**, same character size in every cell.
- **CONSISTENT ANCHOR (critical):** in every frame the character stays the **same size** and the **feet stay on the same baseline and the same horizontal spot**, so playback doesn't jitter or drift. Only the pose changes.
- Fill the whole strip's background with the one background rule for its type (2b): transparent-or-magenta behind characters, black behind effects — the same treatment across every frame.
- Example: a 4-frame walk at 256×256 per frame = **one 1024×256 PNG**.

**What each animation should show (so playback reads right):**
- **Walk (4 frames):** contact pose → passing pose → contact (opposite foot) → passing. Natural arm/leg swing, slight body bob.
- **Idle (2–3 frames):** very subtle — a breathing rise/fall or small weight shift. NOT big motion.
- **Attack (4 frames):** wind-up → strike (tool extended) → follow-through → return to stance.
- **Hit (2 frames):** a recoil/flinch, then back.
- **Effects (portal / transition / fx):** each frame is a clear step in the effect's progression; portal & ambient loops should read continuously start → end → start.

### 2d. Other hard rules

1. **No text** anywhere on any image — no filename, dimensions, label, or watermark.
2. **No floating stray objects** beside a character — tools/weapons go **in the hand**.
3. **Draw exactly** the subject described; never substitute a different character or object.
4. **Generate fresh** — don't trace, upscale, or edit an earlier image.

### 2e. RESOLUTION — deliver LARGE, crisp source images (never shrink to game size)

**Every pixel size listed in this brief is a generous SOURCE resolution — deliver each asset at that size, crisp, detailed, and full-quality.** The developer downscales each asset to its small in-game size later; that is not your job.

- **Do NOT downscale, shrink, or "optimize" the image to a tiny size yourself.** A 64-pixel tile or a shrunken sprite comes out blurry and low-quality and will be rejected.
- Export at **full quality** — no heavy compression, no thumbnail-sized output. When in doubt, deliver **bigger and sharper**, never smaller.
- This applies to the files you put in the `.zip` too — the downloadable files must be the full-resolution images, not small previews of them.

### 2f. Art style guide — make everything look like ONE game

**Quality bar:** every asset — tiles, backdrops, effects — must be as **detailed and polished as the character art**. Nothing should look lower-res or flatter than the rest. **Not** pixel art, **not** flat vector, **not** cartoony.

- **Style:** detailed, hand-illustrated, semi-realistic with clean, readable shapes — like high-end 2D console-RPG art.
- **Outline:** a subtle dark outline on characters and key objects so they read against busy backgrounds; softer or none on tiles and backdrops.
- **Shading:** soft painterly/cel shading, 3–4 tones, with a single directional light from the **upper-left**. Warm local glow only from fire, embers, and lanterns.
- **Palette (whole game):** muted earth neutrals — dusty tan `#cbb894`, bone `#e6ddc8`, worn brown `#6b5a44`, iron grey `#5a5b5e`, deep shadow `#241f1a` — with **one accent, rust-orange `#c2622e`**, used sparingly (Wren's scarf, the portal, key highlights). Each district tints these toward its own hue.
- **Proportions:** realistic-heroic (~6–7 heads tall), consistent across every character so they clearly belong to the same world.
- **Mood:** weathered, lonely, grounded post-apocalyptic — human and grounded, not grim or graphic.
- **Consistency:** same light direction, same palette, same rendering quality on **every** asset. A stranger should be able to tell all of it comes from one game.

---

## 3. THE WORLD & CAST (context for what you're drawing)

*The Long Survey* is set in a weathered, post-apocalyptic world. The player crosses a ruined region on foot as **Wren Calder, the Surveyor**, descending through **nine distinct districts**, fighting through them one at a time. The look is detailed and hand-illustrated, like a high-end 2D console RPG.

These descriptions fully define every character, so you can draw each one **new, in detail**, without any reference image. Same weathered world, muted earth palette + rust-orange accent throughout.

**Hero — Wren Calder, the Surveyor:** a lean, weathered lone traveller with a determined calm face and short practical hair under a hood/wrap. A weathered open long **brown duster** over a canvas utility harness, worn trousers, scuffed boots, gloved hands, and a **rust-orange dust-scarf at the neck (their signature accent)**. Brass goggles pushed up on the forehead, a shoulder satchel, a pouched utility belt, a rolled survey chart in the belt, and a scavenged multi-tool for battle. Capable wanderer, not a soldier.

**Enemies (one per district):**
- `enemy_rise` — **Ridge Lookout:** a wary figure in a patched dusty-tan cloak, hunched and watchful, with a brass spyglass and a notched tally-stick.
- `enemy_tannery` — **Hide Toll-Taker:** bulky, wrapped in stitched leather and drying-rack scraps, heavy gloves, a hide-hook.
- `enemy_hollow` — **Ravine Ambusher:** a lean figure in muffled grey rags, crouched and listening, a small signal-horn at the belt.
- `enemy_lantern` — **Foundry Crewman:** a soot-aproned worker in cracked goggles gripping a jagged glass-shard tool.
- `enemy_bellows` — **Bellows-Hand:** soot-caked, in a leather work mask, gripping a glowing stoking iron.
- `enemy_pump` — **Pipe-Bridge Guard:** a stocky guard in dripping oilskins with a big valve-wrench, planted stance.
- `enemy_provision` — **Granary Guard:** a broad guard in a grain-dusted coat with a bulging sealed satchel and a threshing flail.
- `enemy_outflow` — **Sluice Gatekeeper:** a dripping figure in tall waders holding an oversized rusted gate-key.
- `enemy_cistern` — **Cistern Sentry:** an imposing sentry in dark waterproof plate carrying a pale cold-cyan lantern.

**Bosses (one per district — bigger, more imposing than the enemies, each with one signature feature):**
- `boss_warden` — **The Warden of the Rise:** an imposing checkpoint warden in a heavy plated coat, a brass tally-badge on the chest, holding a horizontal barrier-staff.
- `boss_baron` — **The Patchwork Baron:** a broad, gaudy scavenger-king cloaked in a hundred stitched hides, wearing a crown of bent scrap, arms spread wide.
- `boss_crier` — **The Crier:** a wiry orator rigged with a bank of salvaged loudspeakers and a horn-shaped mask, cables trailing.
- `boss_lamplighter` — **The Lamplighter:** a gaunt keeper in a glass-and-brass diving-style helmet and rig, a cracked-lens motif, holding a bright glowing lamp.
- `boss_stoker` — **The Stoker:** a hulking foundry master in fireproof leathers wielding a glowing white-hot bellows-iron, embers rising.
- `boss_valvemaster` — **The Valvemaster:** a barnacled figure built into a giant rusted pipe-junction wheel, dripping, studded with valves.
- `boss_miller` — **The Miller:** a bloated hoarder throned on a great grain-wheel, hung with sacks and scales, clutching a thick ledger.
- `boss_sluicewarden` — **The Sluicewarden:** a tall, gaunt warden in streaming waders and a grille-mask, holding a huge iron sluice-key like a staff.
- `boss_reclaimer` — **The Reclaimer** (final boss): a still, refined figure in a long clean coat, quietly menacing — the most elegant, minimal silhouette of the whole cast.

---

## 4. THE ASSET LIST (exactly what to produce)

Everything below is what you will generate. Each entry's Asset ID is its filename; each has a fixed pixel size and the background treatment from Section 2b.

### 4.1 TILES — detailed, seamless, **512 × 512 px** source, opaque

Detailed top-down ground/wall tiles that tile seamlessly edge-to-edge. **Deliver each as a large 512×512 source image** (the developer downscales it to the small in-game tile — do NOT output a tiny 64px file). Give **2 variants** of each main ground type to break repetition.

| Asset ID | What |
|---|---|
| `tile_earth`, `tile_earth_b` | dry cracked wasteland earth (2 variants) |
| `tile_rock`, `tile_rock_b` | rocky/scree ground (ravine, cliffs) |
| `tile_road`, `tile_road_edge` | broken asphalt road + road-to-dirt edge |
| `tile_plank` | grain-dusted / duckboard plank floor (markets, granary, bridges) |
| `tile_wall_stone` | grey stone cliff/wall block (clearly impassable) |
| `tile_wall_iron` | riveted iron/industrial wall (bellows, pump, outflow) |
| `tile_water` | murky teal standing water |
| `tile_water_dark` | near-black deep water (cistern) |
| `tile_sludge` | sickly-green sludge (outflow) |
| `tile_shore` | water-meets-land edge |
| `tile_rubble` | broken concrete + rebar pile (blocks movement) |

### 4.2 OVERWORLD CHARACTER SHEETS — detailed, transparent-or-magenta bg, **~192 px per frame**

Crisp detailed walking-around sprites, **animated** (full body, feet at cell bottom). Left-facing is auto-mirrored from the side, so only make right-facing.

**Hero — Wren Calder** (6 sheets):
| Asset ID | Animation | Frames |
|---|---|---|
| `hero_walk_front` | walking toward camera | 4 |
| `hero_walk_back` | walking away (back view) | 4 |
| `hero_walk_side` | walking in profile (facing right) | 4 |
| `hero_idle_front` | standing, subtle breathe | 2 |
| `hero_idle_back` | standing from behind | 2 |
| `hero_idle_side` | standing, profile | 2 |

**Enemies (×9)** — one idle sheet each (they hold position), 3 frames (subtle sway/breathe):
`enemy_rise_idle`, `enemy_tannery_idle`, `enemy_hollow_idle`, `enemy_lantern_idle`, `enemy_bellows_idle`, `enemy_pump_idle`, `enemy_provision_idle`, `enemy_outflow_idle`, `enemy_cistern_idle` — 3 frames each.

**Bosses (×9)** — one idle sheet each, 3 frames (a menacing sway):
`boss_warden_idle`, `boss_baron_idle`, `boss_crier_idle`, `boss_lamplighter_idle`, `boss_stoker_idle`, `boss_valvemaster_idle`, `boss_miller_idle`, `boss_sluicewarden_idle`, `boss_reclaimer_idle` — 3 frames each.

### 4.3 BATTLE ANIMATION SHEETS — detailed, transparent-or-magenta bg, **~640 px per frame**

The close-up fight art, animated — the big, high-detail versions shown during battle. Right-facing for the hero; enemies and bosses face left (the developer mirrors as needed).

**Hero** (3 sheets):
| Asset ID | Animation | Frames |
|---|---|---|
| `hero_battle_idle` | ready stance, breathing sway | 3 |
| `hero_battle_attack` | wind-up → lunge strike → recover | 4 |
| `hero_battle_hit` | recoil from a hit | 2 |

**Enemies (×9)** — battle idle sheet each, 3 frames: `enemy_<district>_battle_idle`. *(Optional later: `_battle_attack` 3f, `_battle_hit` 2f.)*

**Bosses (×9)** — battle idle sheet each, 3 frames: `boss_<name>_battle_idle`. *(Optional later: `_battle_attack` 3–4f, `_battle_hit` 2f.)*

### 4.4 BATTLE BACKDROPS — detailed, **1600 × 900 px**, opaque, full-bleed (×9)

A high-detail establishing scene per district. **Compose each backdrop as a stage for the fight — deliberately plan where the two combatants will stand and leave those spots clear:**

- **The hero stands lower-LEFT; the enemy/boss stands lower-RIGHT** — the developer places the sprites at roughly **x ≈ 27% (hero)** and **x ≈ 73% (enemy)**, with both sets of **feet on the same ground line at about 78–85% of image height**. Draw a believable flat-ish standing ground plane there (road, floor, packed earth, a ledge) so the fighters look planted, not floating.
- **Keep those two lower-third standing zones open and uncluttered** — no large props/machinery/rubble/bright focal detail where a character will be. A combatant sprite is ~35–45% of the image height, so imagine two figures that tall standing there.
- **Push the detail and drama to the BACKGROUND and UPPER area** — landmarks, structures, sky, depth fill the top ⅔ and the edges. Think theatrical backdrop: rich scenery behind, an open apron up front.
- **Depth & grounding:** clear foreground → midground → background separation, a readable horizon, and **light from the upper-left** (matching the characters). Slightly darker/lower-contrast toward center-bottom seats the fighters.

One per district: `backdrop_rise`, `backdrop_tannery`, `backdrop_hollow`, `backdrop_lantern`, `backdrop_bellows`, `backdrop_pump`, `backdrop_provision`, `backdrop_outflow`, `backdrop_cistern`.
(Rise = bleached open ridge; Tannery = ochre market of hides; Hollow = grey ravine + towers; Lantern = teal glass yard + great lens; Bellows = ember industrial stacks; Pump = flooded teal waterworks; Provision = golden silos; Outflow = green sludge gates; Cistern = vast near-black drowned chamber.)

### 4.5 EFFECT ANIMATION SHEETS — on solid **black `#000000`** background

| Asset ID | What | Frames | Frame size |
|---|---|---|---|
| `fx_portal` | glowing rust-orange energy vortex ring (game-entry portal) | 8 | 256×256 |
| `fx_transition` | sweeping ink/dust/energy wipe overlay for entering fights & new districts (edge-to-edge streaks, mostly opaque mid-frames) | 6 | 640×360 |
| `fx_slash` | white-and-rust strike arc on an enemy hit | 4 | 256×256 |
| `fx_hit` | spark + dust burst on a connect | 4 | 256×256 |
| `fx_heal` | warm rising motes/glow (campfire & second wind) | 4 | 256×256 |
| `fx_levelup` | rust-gold ring pulse + sparks | 5 | 256×256 |

### 4.6 TITLE CARDS — **1600 × 900 px**, opaque (game title drawn on top in-engine)

- `title_game` — Wren silhouetted on the ridge overlooking the ruined descent (splash).
- `title_<district>` ×9 — a wide establishing shot per district (behind the district name during the transport transition): `title_rise`, `title_tannery`, `title_hollow`, `title_lantern`, `title_bellows`, `title_pump`, `title_provision`, `title_outflow`, `title_cistern`.

### Suggested priority (use this to order your batches)

1. **The new look, fast:** all tiles · all 9 battle backdrops · hero overworld + hero battle sheets · `fx_portal`, `fx_transition`.
2. **The cast:** 9 enemy overworld idles + 9 enemy battle idles · 9 boss overworld idles + 9 boss battle idles.
3. **Polish:** remaining `fx_*` (slash, hit, heal, levelup) · `title_game` + 9 district title cards · (optional) enemy/boss `_battle_attack` / `_battle_hit` sheets.

---

## 5. YOUR FIRST STEP — BUILD A WORKFLOW PLAN (do this before drawing anything)

Before you generate a single image, **re-read this whole brief once more** — the rules in Section 2, the cast in Section 3, and the full asset list in Section 4 — and then produce a **workflow plan**. In that plan:

1. **Confirm you understand the rules**, in your own words: one asset = one separate PNG (no contact sheets); the background rule per asset type (transparent-or-magenta for characters, black for effects, opaque for tiles/backdrops); animations delivered as single horizontal sprite sheets with a consistent anchor; exact pixel sizes; filenames = Asset IDs; no text, no floating objects.
2. **Inventory every asset** from Section 4 into a checklist, so you can see the whole job and track what's done.
3. **Break the whole job into small batches** — about **4–8 assets each**, grouped logically (e.g. all ground tiles together; the hero's sheets together; a district's enemy + boss + backdrop together) and ordered using the Suggested Priority above so the new look appears fast.
4. **Present the batch plan to me** as a numbered list of batches (Batch 1, Batch 2, …) with the assets in each, and briefly note how you'll confirm each file meets the rules before moving on.

Then **stop and wait.** Do not generate any art until I tell you to start.

---

## 6. HOW WE'LL WORK — BATCH BY BATCH

Once you've shown me the workflow plan and batches, we work one batch at a time. **These stop-and-ask rules are mandatory — follow them exactly, every time, with no exceptions:**

1. **Ask me to start Batch 1, and wait.** Do not generate anything until I reply.
2. When I say go, **generate that batch** — each asset as its own separate, correctly-named, correctly-formatted PNG, following every rule in Section 2.
3. **Bundle the finished batch into ONE downloadable `.zip` file** containing that batch's PNGs, named for the batch (e.g. `batch-01-ground-tiles.zip`), so I can download the whole batch in one click. (If you genuinely cannot produce a `.zip`, deliver the individual PNGs clearly named — but never merge multiple assets into one image.)
4. **Then STOP and explicitly ask me: "Continue to Batch N?" — and WAIT for my answer.** Do NOT begin, preview, or roll into the next batch on your own under any circumstances, even if it seems efficient or I seem ready. Every batch ends with a full stop and an explicit question, and you only proceed after I say so.
5. Repeat — generate → zip → stop → ask — until all 84 required assets are delivered.
6. **At the very end, also provide one final `.zip` containing all 84 completed PNGs together**, so I have the whole set in a single download.

This keeps quality high and lets me check each batch before we move on. Start by reading everything and giving me your workflow plan and batch breakdown, then ask to begin Batch 1.
