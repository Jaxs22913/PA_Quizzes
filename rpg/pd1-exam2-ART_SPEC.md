# THE LONG SURVEY — Game Art Specification
*A complete, self-contained art bible. Hand this whole document to the AI artist. It requires no prior conversation.*

> **How the art gets used:** every asset is a transparent PNG named **exactly after its Asset ID** (e.g. `hero_front_idle.png`). The game has a built-in loader — the player drops the finished sprite folder onto the title screen and each file swaps into its slot by filename. So filenames are contractual: match the Asset IDs in Section 13 precisely.

---

## 1. GAME OVERVIEW

- **Game title:** The Long Survey
- **Educational topic/exam:** Physical Diagnosis 1 — Exam 2 (the head-to-toe physical examination; nine topic areas).
- **Learning objectives:** Reinforce the sequence and content of a complete physical exam. Each of the nine districts corresponds to one exam topic in head-to-toe order; clearing a full run is a full comprehensive review. *(The fiction never makes medical claims — the teaching lives entirely in the battle questions, not the art or prose.)*
- **Genre:** Top-down 2D action-RPG / JRPG-style overworld with turn-based, question-driven battles.
- **Core gameplay loop:** Walk the single main road through a ruined region on foot → reach staged wasteland figures who challenge you → answer an exam question to strike (wrong answers cost health and show the rationale) → rest at a campfire (flip flashcards to heal) → defeat the district's boss to open the gate → descend to the next district. Repeat through all nine, top to bottom.
- **Story summary:** A cataclysm broke the world into one long ruined slope — sunlit ridge at the top, drowned undercity at the bottom. **Wren Calder, the Surveyor**, is the last person still walking the whole route to map it, district by district. Each district has fallen under a self-appointed warlord who seals the road behind a gate. To pass, Wren must survey (understand) each district and bring down its warlord. The journey ends at the bottom, in the black water of the Deep Cistern, facing the Reclaimer.
- **Tone and atmosphere:** Weathered, lonely, quietly determined. Not gory or grim-dark — a melancholy, sun-bleached, rusted-industrial world with pockets of warm firelight. Hope carried by one steady traveller.
- **Visual inspirations:** SNES-era JRPG overworlds (Chrono Trigger, Secret of Mana) crossed with a muted post-apocalyptic palette (think dust, rust, oxidized copper, bleached bone) — *original world, no real-world logos or franchises.*
- **Color palette (global):** Muted earth neutrals — dusty tan `#cbb894`, bone `#e6ddc8`, worn brown `#6b5a44`, iron grey `#5a5b5e`, deep shadow `#241f1a`. **One accent used sparingly across the whole game: rust-orange `#c2622e`** (the Surveyor's dust-scarf, the portal, key highlights). Each district then tints these neutrals toward its own hue (Section 2).
- **Camera perspective:** Two views. **Overworld** = classic 2.5D top-down JRPG — a top-down tile map with *upright, camera-facing* characters walking on it (front/back/side sprites, not true bird's-eye figures). **Battle** = side-view arena: hero on the left facing right, enemy/boss on the right facing left, against a painted backdrop.
- **Pixel-art resolution/style:** 16-bit. Characters are small sprites (hero 24×32 px) drawn at native res and upscaled with **nearest-neighbor (no smoothing)** — so art must be crisp, hand-placed pixels, not anti-aliased. Terrain tiles are 16×16 px, drawn on a 32-px world grid.
- **Lighting style:** Flat directional light from the upper-left; soft 1–2 tone shading with a single darker ambient-occlusion tone under overhangs. Warm glow sources (campfires, embers, lanterns) cast a small local bloom. Overall low-to-medium contrast, dusty and diffuse, growing darker and colder as the player descends toward the Cistern.

---

## 2. WORLD DESIGN

One continuous region descended top-to-bottom. A **single main road** threads all nine districts, sealed between them by boss-gates (a gold-banded barrier that opens when the district's warlord falls). Density is deliberate: exactly **3 staged enemies, 1 campfire, 1 chest per district**, placed at chokepoints and lairs — open stretches are intentionally empty.

Tile size everywhere: **16×16 px**. Each district reuses the shared tile set (Section 11) recolored to its palette, plus its own decorations and interactive objects.

### District 1 — Vantage Rise · *General Survey & Vital Signs*
- **Visual theme:** the last high, open ground before the sprawl; wide sky, long views, bleached light.
- **Terrain:** a ridge-top of dry cracked earth with a switchback road dropping from an observation deck to a checkpoint gate. Sheer cliff edges frame the drop.
- **Architecture:** a ruined **Observation Deck** (upper-left), a **Watch Station** (upper-right), and **The Checkpoint** gate. Skeletal steel railings, a collapsed antenna mast.
- **Vegetation:** almost none — a few dead scrub tufts and wind-bent dry grass in rock cracks.
- **Hazards:** cliff edges (impassable drop tiles); otherwise open.
- **Background elements:** a hazy panorama of the whole ruined region falling away below; distant broken towers on the horizon.
- **Ambient effects:** drifting dust motes, faint heat shimmer, an occasional wind gust of blown grit.
- **Tiles required:** dusty-tan cracked earth (+variant), pale broken road + switchback edges, cliff/rubble edges, low ruin walls.
- **Decorations:** dead scrub, a leaning antenna mast, broken railing segments, a survey marker post.
- **Interactive objects:** campfire (sheltered nook off the road), chest (inside the observation deck), boss-gate at the checkpoint.

### District 2 — The Tannery Rows · *Skin, Hair & Nails*
- **Visual theme:** a cramped shanty market of patched tarps and drying hides; ochre and leather tones, dried-maroon stains.
- **Terrain:** a central market street of packed dirt and duckboards funnelling past stalls.
- **Architecture:** lean-to **Tanner Shops**, a **Drying Racks** shed (left), the covered **Hide Market** (right, the Baron's lair). Patched fabric awnings on crooked poles.
- **Vegetation:** none live; hanging cured hides and rope read as "growth."
- **Hazards:** none terrain-based; a stall chokepoint funnels the player.
- **Background elements:** rows of hanging hides swaying, tarps billowing, hooks and chains.
- **Ambient effects:** drifting flies/dust, slow tarp sway, faint smoke from a tanning pit.
- **Tiles required:** packed-dirt ground (ochre-tinted earth), duckboard/plank floor, patched-tarp "wall" segments.
- **Decorations:** drying racks with hides, hanging pelts, stitched-tarp awnings, barrels of tanning fluid, coils of rope.
- **Interactive objects:** campfire (quiet stall at street's end), chest (back of the shed), boss-gate at the hide market.

### District 3 — Echo Hollow · *HENT (Head, Ears, Nose, Throat)*
- **Visual theme:** a narrowing ravine pass walled by cliffs and lined with leaning broadcast towers; grey stone, rust metal, deep shadow.
- **Terrain:** a winding, pinching ravine floor of rock and scree that climbs toward a perch; a 2-tile-wide "Narrows" throat chokepoint.
- **Architecture:** **Leaning Broadcast Towers**, cable-strung and precarious; **The Crier's Perch** platform at the head of the pass.
- **Vegetation:** lichen and moss in shaded cracks, a dead vine on a tower.
- **Hazards:** cliff walls (impassable); the Narrows squeeze.
- **Background elements:** towering ravine walls, tangled aerial cables, salvaged loudspeaker horns.
- **Ambient effects:** echoing dust falls from the cliffs, swaying cables, faint feedback shimmer near the perch.
- **Tiles required:** grey rocky ground (+scree variant), cliff-wall faces, rubble.
- **Decorations:** leaning towers, loudspeaker horns, cable bundles, fallen antenna dishes.
- **Interactive objects:** campfire (wide sheltered bend), chest (cliff alcove), boss-gate below the perch.

### District 4 — Lantern Watch · *Eye*
- **Visual theme:** a ruined lighthouse yard built on ground glass; teal-green glass, soot black, sharp glassy highlights.
- **Terrain:** crunching glass-gravel yards with ring-paths circling a central lens tower.
- **Architecture:** the **Glass Foundry** (left), the **Lens Works** (right), and **The Great Lens** tower (center, the Lamplighter's post) — a cracked Fresnel lens on a brass frame.
- **Vegetation:** none; glass shards catch light like frost.
- **Hazards:** none terrain-based; the tower ring-path routes movement.
- **Background elements:** the great cracked lens throwing broken light beams, foundry chimneys, racks of glass panes.
- **Ambient effects:** glints/sparkles on glass, a slow rotating light-beam sweep, drifting soot.
- **Tiles required:** teal glass-gravel ground (+variant), foundry brick floor, low glass-rack walls.
- **Decorations:** cracked lens segments, glass-pane racks, soot-stained furnaces, a searchlight rig.
- **Interactive objects:** campfire (sheltered yard corner), chest (locked lens-works drawer), boss-gate at the lens tower.

### District 5 — The Bellows Yards · *Lung & Thorax*
- **Visual theme:** an industrial air-works maze of vent walls feeding great stacks; ember orange, soot black, iron grey.
- **Terrain:** a working yard of iron grating and ash-dusted concrete, threaded by a **Vent Maze**.
- **Architecture:** **The Vent Maze** (upper yard) of tall vent walls, **The Stacks** (lower) — great smoke chimneys, and **Master Bellows** (center-bottom, the Stoker's lair) — a colossal leather-and-iron bellows.
- **Vegetation:** none; soot and ash instead.
- **Hazards:** hot vents (visual only) and the maze pinch-points.
- **Background elements:** looming stacks belching thin smoke, glowing furnace mouths, hanging chains.
- **Ambient effects:** rising embers, heat shimmer, drifting soot, pulsing furnace glow.
- **Tiles required:** iron-grating floor, ash-concrete ground, riveted-iron vent walls.
- **Decorations:** the master bellows, stoking irons in racks, coal piles, glowing furnace grates, chain hoists.
- **Interactive objects:** campfire (quiet dead-end vent), chest (behind the right furnace), boss-gate at the master bellows.

### District 6 — The Pump Works · *Cardiovascular & Peripheral Vascular*
- **Visual theme:** a half-drowned waterworks; teal water, oil-slick sheen, wet steel.
- **Terrain:** mostly **open water**; movement is over **pipe-bridges** — a top gallery walk, two cross-bridges, and a central spine bridge.
- **Architecture:** **The Flooded Galleries**, **Pipe Bridges** (great rusted pipes lashed into walkways), and **The Main Junction** (a dry control hall, the Valvemaster's post).
- **Vegetation:** algae mats and slime on the waterline.
- **Hazards:** deep water everywhere off the bridges (impassable); narrow bridge chokepoints.
- **Background elements:** submerged machinery, valve wheels, reflections rippling on the water.
- **Ambient effects:** gentle water ripples/reflections, dripping, occasional bubbling, oil-sheen shimmer.
- **Tiles required:** murky teal water (animated feel), pipe-bridge planking, wet-steel gallery floor, shore/waterline transitions.
- **Decorations:** giant valve wheels, pipe junctions, floating debris, drip stalactites.
- **Interactive objects:** campfire (dry landing above the junction), chest (isolated side platform across the water), boss-gate at the main junction.

### District 7 — The Provision Halls · *Abdominal*
- **Visual theme:** the granary quarter; golden grain, sackcloth, flour dust.
- **Terrain:** a broad mill/market lane of grain-dusted boards running between storehouses.
- **Architecture:** four **Silos** across the top, **Storehouse Row** (long buildings left and right), and **The Mills** (center, the Miller's great grain-wheel).
- **Vegetation:** spilled sprouting grain, a few weeds through the boards.
- **Hazards:** none terrain-based; sealed storehouse doors form a chokepoint.
- **Background elements:** towering silos, a turning grain-wheel, hanging scales, stacked sacks.
- **Ambient effects:** drifting flour dust in light shafts, slow grain-wheel turn, scattering chaff.
- **Tiles required:** grain-dusted plank floor, warm-dirt ground, silo/storehouse walls.
- **Decorations:** grain sacks, scales, the grain-wheel, sealed crates, scattered chaff, a ledger stand.
- **Interactive objects:** campfire (gap between silos), chest (sealed crate deep in the left storehouse), boss-gate at the mills.

### District 8 — The Outflow · *Anus & Rectum*
- **Visual theme:** the drainage works; sickly green sludge, rust, wet concrete.
- **Terrain:** **sludge channels** (hazard water) crossed by narrow **sluice-gate walkways**, with service walks beside the channels.
- **Architecture:** **The Sludge Channels**, **The Sluice Gates** (two crossing walkways with iron gate mechanisms), and **The Outfall** control (the Sluicewarden's gate).
- **Vegetation:** slime, scum mats, a crust of dried residue.
- **Hazards:** sludge channels (impassable/harmful water); narrow crossings.
- **Background elements:** great iron sluice gates, dripping outfall pipes, rusted chains and winches.
- **Ambient effects:** slow sludge flow, dripping, rising damp haze, bubbling.
- **Tiles required:** green sludge water, wet-concrete service-walk floor, iron sluice walls, sludge-shore transitions.
- **Decorations:** sluice-gate winches, outfall pipes, valve wheels, floating scum, warning posts.
- **Interactive objects:** campfire (dry right-side ledge), chest (dead-end side outfall), boss-gate at the outfall control.

### District 9 — The Deep Cistern · *Male GU & Prostate* (FINAL)
- **Visual theme:** the bottom of everything — a vast drowned chamber of still black water; near-black, with cold cyan lantern glow.
- **Terrain:** a **drowned stair** descends in; a narrow **causeway** snakes over deep black water to a central **Wellspring** platform (the Reclaimer's arena).
- **Architecture:** a cathedral-scale flooded cistern of columns and arches half-submerged; the **Wellspring** — a raised stone platform ringed by still water.
- **Vegetation:** pale drowned roots, faint bioluminescent scum.
- **Hazards:** deep black water off the causeway (impassable); the causeway's doglegs.
- **Background elements:** submerged columns, mirror-still reflections, a faint distant glow from the Wellspring.
- **Ambient effects:** near-motionless water with slow ripples, cold drifting mist, sparse dripping, faint cyan glimmer.
- **Tiles required:** black still water (reflective), wet dark-stone causeway/platform, drowned-stair steps, column bases.
- **Decorations:** submerged columns/arches, the wellspring structure, pale roots, a lone hanging lantern.
- **Interactive objects:** campfire (dry landing at the stair foot), chest (submerged side ledge via a thin spur), final boss arena at the Wellspring (no gate beyond — this is the end).

---

## 3. MAIN CHARACTER

**Wren Calder, the Surveyor.**

- **Appearance:** a lean, weathered lone traveller; determined, calm face; mid-tone weather-worn skin; short practical hair under a hood/wrap.
- **Clothing:** a weathered open long duster (worn brown `#6b5a44`) over a canvas utility harness; worn trousers; scuffed boots; gloved hands. A **rust dust-scarf** (`#c2622e`) at the neck — the character's single pop of accent color and their read-at-a-glance signature.
- **Equipment:** brass goggles pushed up on the forehead; a shoulder satchel; a utility belt with pouches; a scavenged multi-tool/short blade used in battle; a rolled survey chart tucked in the belt.
- **Personality shown visually:** self-reliant and steady — upright but relaxed posture, weight balanced, no swagger and no fear. Reads as a capable wanderer, not a soldier.
- **Color palette:** duster brown `#6b5a44` / shade `#4a3d2c` / light `#8a7658`; scarf rust `#c2622e`; skin `#c99a6e` / shade `#a67c52`; boots & belt `#3a2f22`; goggles brass `#b8893a`; harness canvas `#9c8a67`. Dark outline `#1c1610`.
- **Silhouette:** the open duster flaring slightly at the hem + the scarf at the neck + goggles-lump on the forehead make a distinctive outline readable at 24 px. Keep the hem, scarf, and goggles crisp — they are the recognizable shape.
- **Size / pixel dimensions:** **24×32 px**, full body, transparent background, feet at the bottom edge.

### Required animations (per direction unless noted)
The **engine currently consumes** idle + one walk frame per direction, plus a battle idle and battle attack. Provide at minimum those; extra frames listed are welcome polish.

| Animation | Frames | Notes |
|---|---|---|
| Idle | 1 (ideal 2 for a subtle breathe) | standing |
| Walk | 2 (`walk1`, `walk2`) | alternating stride; engine toggles idle↔walk1, so **walk1 must read clearly as mid-stride** |
| Run | optional 2 | not used by engine; skip unless polishing |
| Attack | 1 (`battle_attack`) | side view, lunging strike with the tool/blade |
| Hurt | optional 1 | recoil pose (engine flashes a red vignette instead) |
| Death | optional | not used (no death sprite; game shows a game-over screen) |
| Interact | optional 1 | reaching toward a chest/campfire; nice-to-have |
| Cast ability | n/a | no spellcasting |
| Jump | n/a | no jumping |

### Required viewing directions
- **Front** (facing camera), **Back** (facing away, no face — show hood/duster back), **Right side** (strict profile facing right).
- **Left is auto-mirrored in engine** — do **not** draw left-facing frames.
- **Battle** frames are a right-facing side view (hero stands on the left of the arena facing the enemy on the right).
- No diagonals required.

**Exact hero asset list:** `hero_front_idle`, `hero_front_walk1`, `hero_front_walk2`, `hero_back_idle`, `hero_back_walk1`, `hero_back_walk2`, `hero_side_idle`, `hero_side_walk1`, `hero_side_walk2`, `hero_battle_idle`, `hero_battle_attack`.

---

## 4. NPC DATABASE

**There are no friendly/neutral NPC characters in the current build.** Wren travels alone; every figure encountered is hostile (Section 5) or a boss (Section 6), and story is delivered in text beats and campfire rests rather than by talking to characters. **No NPC sprites or dialogue portraits are required for this game.**

*Optional future expansion (not needed now):* a single recurring **Wayfarer at the campfire** — a hooded fellow survivor who appears at each campfire as a resting companion (24×32, one idle, one seated pose, one small dialogue portrait ~48×48). Only build if the design later adds spoken NPC beats.

---

## 5. ENEMY DATABASE

One themed wasteland figure per district. Each is an **original** post-apocalyptic character (no real-world references). **Size: 24×28 px, transparent.** Difficulty rises district to district. All share the game's muted palette, tinted to their district and given one clear identifying prop.

For each enemy provide: `<key>_front` (upright, facing camera — the map roaming sprite) and a **battle pose facing left** (used on the right side of the fight screen, facing the hero). Optional `<key>_walk1/2` for roaming animation.

| Key | Name | District | Difficulty | Visual description | Palette tint | Identifying prop / weak read | Attack style | Idle behavior | Movement |
|---|---|---|---|---|---|---|---|---|---|
| `enemy_rise` | Ridge Lookout | Vantage Rise | 1 (easiest) | a wary lookout in a patched dust-cloak, hunched, watchful | dusty tan `#b8a074` | a brass spyglass + a notched tally-stick | quick jabs / thrown stones | shifts weight, scans the horizon | paces a short patrol line |
| `enemy_tannery` | Hide Toll-Taker | The Tannery Rows | 2 | a bulky figure wrapped in stitched leather and drying-rack scraps, heavy gloves | ochre/leather `#9c6b3a` | thick stitched-leather apron + a hide-hook | heavy swings with the hook | crosses arms, blocks the way | stands ground at a chokepoint |
| `enemy_hollow` | Ravine Ambusher | Echo Hollow | 3 | a lean, muffled figure in grey rags, crouched and listening | ravine grey `#7d7a72` | a small signal-horn at the belt | sudden lunge from cover | crouches, head cocked, listening | darts between towers |
| `enemy_lantern` | Foundry Crewman | Lantern Watch | 4 | a soot-aproned worker in cracked goggles gripping a glass-shard tool | teal-soot `#4f6b64` | cracked goggles + a jagged glass shard | slashing glass edge | works a bench, glances up | circles the tower ring-path |
| `enemy_bellows` | Bellows-Hand | The Bellows Yards | 5 | a soot-caked figure in a leather breather mask, gripping a stoking iron | ember-soot `#6e4a33` | leather breather mask + glowing iron tip | overhead iron swings | shoulders heaving, mask hissing | trudges a patrol through smoke |
| `enemy_pump` | Pipe-Bridge Guard | The Pump Works | 6 | a stocky guard in dripping oilskins with a valve-wrench, planted stance | wet teal-steel `#3f5f68` | slick oilskin hood + a big valve-wrench | wrench bludgeon | plants feet, guards the bridge | holds bridge chokepoints |
| `enemy_provision` | Granary Guard | The Provision Halls | 7 | a broad guard in a grain-dusted coat with a sealed satchel and a flail | grain gold `#a8843f` | bulging sealed satchel + a threshing flail | whirling flail arcs | pats the satchel, watchful | patrols the storehouse doors |
| `enemy_outflow` | Sluice Gatekeeper | The Outflow | 8 | a dripping figure in waders holding a heavy rusted gate-key | sludge green `#5f6e3a` | tall waders + an oversized rusted key | key-swing + shove | drips, shifts on the walkway | guards sluice crossings |
| `enemy_cistern` | Cistern Sentry | The Deep Cistern | 9 (elite) | an imposing sentry in dark waterproof plate carrying a pale lantern | near-black + cyan glow `#2b3a44` | dark plate armor + a cold cyan lantern | measured heavy strikes | stands utterly still, lantern raised | slow, deliberate advance |

### Enemy animations (each)
| Animation | Frames | Directions |
|---|---|---|
| Idle (map) `_front` | 1 (ideal 2) | front (camera-facing) |
| Battle idle `_battle` *(may reuse `_front` if not provided)* | 1 (ideal 2) | left-facing |
| Walk `_walk1/2` (optional) | 2 | front |
| Attack (optional) | 1 | left-facing |
| Hurt (optional) | 1 | left-facing |

*Engine minimum: one `_front` per enemy (it's used both roaming and in battle). Everything else is polish.*

---

## 6. BOSS DATABASE

One escalating boss per district, each at the gate. **Size: 40×48 px, transparent.** Bigger, more imposing silhouettes than enemies, each with **one memorable, instantly-readable feature**. Battle pose faces **left** (boss stands on the right of the arena). Palette matches the district but pushed richer/darker. Provide `<key>_battle` (idle); optional `<key>_attack` and `<key>_hit` frames.

| Key | Name (district) | Story role | Visual design | Scale | Phases / transform | Weak-point read | Arena |
|---|---|---|---|---|---|---|---|
| `boss_warden` | The Warden of the Rise (1) | first gatekeeper; holds the checkpoint | an imposing warden in a heavy plated coat, a brass tally-badge on the chest, holding a horizontal barrier-staff across the body | 40×48 | single phase | the tally-badge glints center-chest | the checkpoint gate |
| `boss_baron` | The Patchwork Baron (2) | scavenger-king of the hide market | broad and gaudy, cloaked in a hundred stitched hides, wearing a crown of nails; arms spread wide | 40×48 (broadest silhouette) | single phase | crown of nails on the head | the hide market |
| `boss_crier` | The Crier (3) | demagogue broadcasting over the pass | a wiry figure wired to a bank of salvaged loudspeakers, wearing a horn-mask, cables trailing off-frame | 40×48 (tall, spindly) | single phase | the horn-mask face | the crier's perch |
| `boss_lamplighter` | The Lamplighter (4) | keeper of the great lens | a gaunt figure posed atop a cracked Fresnel lens, hands on twin searchlight beams, a glass-and-brass rig on the back | 40×48 | single phase | the glowing lens at the base | the great lens tower |
| `boss_stoker` | The Stoker (5) | foundry master of the air-works | a hulking figure in fireproof leathers wielding a glowing bellows-iron, embers rising around the shoulders | 40×48 (bulkiest) | single phase | the white-hot iron tip | the master bellows |
| `boss_valvemaster` | The Valvemaster (6) | fused to the waterworks junction | a barnacled figure half-fused to a giant pipe-junction wheel, dripping, studded with many small valves | 40×48 (widest base) | single phase | the central junction wheel | the main junction hall |
| `boss_miller` | The Miller (7) | bloated hoarder of the granary | a heavy hoarder throned on a great grain-wheel, hung with sacks and scales, clutching a thick ledger | 40×48 (throned, imposing) | single phase | the ledger/scales he clutches | the mills |
| `boss_sluicewarden` | The Sluicewarden (8) | drowned warden of the last gate | a tall, drowned-looking warden in streaming waders holding a huge sluice-key like a staff | 40×48 (tallest) | single phase | the great sluice-key | the outfall control |
| `boss_reclaimer` | The Reclaimer (9, FINAL) | the calm mastermind at the bottom | a still, refined figure in a long coat standing on a causeway over black water, the water mirroring him; quietly menacing, minimal, the most elegant silhouette of all | 40×48 (most refined) | **narratively regenerates** — no separate sprite phase required, but give an optional `_hit` frame to sell resilience | the coat's clean silhouette against black water | the wellspring causeway |

### Boss animations (each)
| Animation | Frames | Directions |
|---|---|---|
| Battle idle `_battle` | 1 (ideal 2 for a menacing sway) | left-facing |
| Attack `_attack` (optional) | 1–2 | left-facing |
| Hit `_hit` (optional) | 1 | left-facing |

*Engine minimum: one `_battle` per boss. Attack/hit frames are polish.*

---

## 7. PROPS

Small top-down objects, transparent, upright-billboard style to match characters. **Engine currently uses `prop_crate`, `prop_campfire`, `prop_chest`, `prop_signpost`; the rest are optional set-dressing** the artist can add for richer districts.

| Key | Size | Visual description |
|---|---|---|
| `prop_crate` | 16×16 | A weathered wooden scrap-crate, mismatched planks, one cracked board, faint stenciled marks worn to illegibility. Reads clearly as "loot/cover." |
| `prop_chest` | 16×14 | A battered metal footlocker/lockbox, closed, a rust-pitted latch with a small brass keyhole and a faint gold glint on the lock so it reads as openable. |
| `prop_campfire` | 16×16 | A small fire in a ring of blackened stones, warm orange-yellow flame with a soft glow and a thin curl of smoke. The one warm, inviting object — a rest point. |
| `prop_signpost` | 16×20 | A leaning weathered wooden post with a blank cracked board, one rusted nail, listing to one side. Marks routes/gates. |
| `prop_barrel` | 16×16 | A rusted metal barrel, dented, a corroded rim, a faint chemical stain streak. |
| `prop_lamppost` | 16×28 | A broken street lamp on a bent pole, the glass housing shattered and dark, wires drooping. |
| `prop_drying_rack` | 20×20 | A tanner's A-frame rack hung with stretched, cured hides swaying slightly (District 2 flavor). |
| `prop_pipe` | 20×16 | A large rusted pipe segment, riveted seams, a slow drip at one end (Districts 6 & 8 flavor). |
| `prop_valve_wheel` | 16×16 | A round rusted valve hand-wheel on a stub of pipe (Districts 6 & 8). |
| `prop_grain_sack` | 16×16 | A plump sackcloth grain sack, tied top, a small spill of grain at the base (District 7). |
| `prop_glass_rack` | 20×20 | A rack of cracked glass panes catching a teal glint (District 4). |
| `prop_rubble_pile` | 16×16 | A pile of broken concrete chunks and bent rebar; blocks movement. |

---

## 8. ITEMS

The game is light on inventory — HP, XP, and a streak are the resources; chests and campfires are the reward/heal beats. Provide simple, readable **inventory-icon-style** sprites (roughly 16×16, transparent) where an artist wants to visualize them; most are currently represented by UI numbers rather than art, so treat this section as **optional icon polish**.

- **Weapon — Surveyor's Multi-tool:** the scavenged short blade/tool Wren strikes with; a taped grip, a chipped edge, rust-orange wrap. (~16×16 icon.)
- **Armor — none:** Wren wears only the duster; no separate armor pieces.
- **Consumable — Flashcard / Field Note:** a folded, hand-marked index card (campfire healing is themed as reviewing field notes). Warm off-white with a rust-orange corner. (~16×16 icon.)
- **Consumable — Ration Tin:** a dented tin (optional alternate heal pickup). (~16×16.)
- **Quest item — Survey Chart:** a rolled, marked map/chart of the region; the through-line object Wren carries. (~16×16 icon, or a larger ~48×32 "map" for a menu.)
- **Collectible — District Seal:** a small stamped token awarded per district cleared (nine total, each tinted to its district). Shown as a progress marker. (~12×12 icon.)
- **Chest loot glint:** a small sparkle/coin-glint used when a chest opens (see VFX). 

---

## 9. USER INTERFACE

The current UI is built in HTML/CSS, not sprites — so **UI art is optional**, but if the artist produces UI assets they must match the visual language below (weathered metal plates, stamped labels, rust-orange accent, dusty parchment for text). List of assets that *could* be arted:

- **Buttons:** answer-choice buttons (wide, four per battle), menu buttons — a riveted metal plate look, rust-orange highlight on hover/selected. (~ scalable; design at 96×28.)
- **Health bar:** a segmented gauge in a dented metal frame; fill is warm red-orange draining to dark. (~120×14.)
- **XP bar:** a thin gauge, rust-orange fill in a brass frame. (~120×8.)
- **Level / streak badge:** a small stamped brass roundel showing level; a "streak" flame pip. (~24×24.)
- **Mana bar:** **not needed** (no mana system).
- **Inventory slots:** riveted square metal slots (~28×28) — only if inventory is added.
- **Dialogue / question box:** a weathered parchment-on-metal panel for the exam question and story beats, dark border, dusty cream field. (~ scalable; design 320×120.)
- **Menus (pause):** the same weathered-panel style, a short stacked list.
- **Skill icons:** **not needed** (no skill tree).
- **Cursor:** a small rust-orange survey-reticle/crosshair (~16×16).
- **Minimap assets:** a slim vertical "descent" progress rail showing the nine districts as stamped seals, current one lit rust-orange (the game is one long top-to-bottom route, so a vertical progress rail fits better than a map). (~24×200.)

---

## 10. VISUAL EFFECTS

Small pixel FX, transparent, most as short frame sequences. **Engine currently uses `fx_slash` and `portal_ring`; the rest are optional polish** to enrich hits, healing, and level-ups.

| Key | Effect | Size | Frames | Description |
|---|---|---|---|---|
| `fx_slash` | Strike | 32×32 | 1 (ideal 3) | a quick white-and-rust diagonal slash arc that flashes when the hero lands a correct-answer hit |
| `portal_ring` | Portal / intro | 128×128 | 1 (ideal 4–6 loop) | a glowing rust-orange concentric vortex ring on transparent bg; the region-entry portal |
| `fx_hit_spark` | Enemy hit | 24×24 | 3 | a small burst of pale sparks + dust when a strike connects |
| `fx_heal` | Healing (campfire) | 32×32 | 4 | soft warm-gold rising motes/glow around the hero when a flashcard heals |
| `fx_levelup` | Level up | 48×48 | 5 | a rust-gold ring pulse rising off the hero with a few sparks |
| `fx_hurt_flash` | Take damage | full-screen tint | n/a | a red vignette flash (engine draws this; no sprite needed, listed for completeness) |
| `fx_smoke` | Ambient smoke | 24×24 | 4 loop | thin drifting soot/smoke for Bellows/Foundry districts |
| `fx_embers` | Ambient embers | 16×16 | 4 loop | rising orange embers for the Bellows Yards / Stoker |
| `fx_water_ripple` | Ambient water | 16×16 | 4 loop | a soft expanding ripple ring for Pump Works / Cistern surfaces |
| `fx_dust_gust` | Ambient wind | 32×16 | 3 | a blown streak of grit for the open Rise |
| `fx_loot_glint` | Chest opened | 16×16 | 3 | a small sparkle/star glint when a chest opens |

---

## 11. TILE SETS

**Tile size: 16×16 px, seamless (must tile edge-to-edge).** Provide **2–3 variants** of each ground tile to break repetition. The shared set below is recolored per district (Section 2). Directional edge tiles (road/shore corners and sides) are required because the engine composites transitions.

| Category | Keys | Description |
|---|---|---|
| **Ground** | `tile_earth`, `tile_earth_b` | dry cracked wasteland earth with pebbles/hairline cracks (`_b` is a second scatter variant), dusty tan; recolored per district |
| **Roads** | `tile_road`, `tile_road_edge`, `tile_road_E`, `tile_road_W` | broken ash-grey asphalt slabs; `_edge` = dirt intruding on one side (road↔earth transition); `_E`/`_W` = directional road-edge pieces |
| **Walls** | `tile_wall` | ruined brick/concrete wall with rust streaks, shown with top-down thickness; district-recolored (brick, iron, glass-rack, silo, sluice-iron, stone) |
| **Water** | `tile_water` | murky teal-grey standing water with faint highlights (recolor to sludge-green for District 8, near-black for District 9) |
| **Water edges / shores** | `tile_shore`, `tile_shore_N`, `tile_shore_S`, `tile_shore_E`, `tile_shore_W`, `tile_shore_NE`, `tile_shore_NW` | water-meets-land transition tiles for each side and outer corner, so pools read cleanly against ground |
| **Bridges** | *(use `tile_road`/plank recolor)* | pipe-bridge planking for the Pump Works — a plank/steel-grate recolor of the road tile spanning water |
| **Cliffs** | `tile_cliff` | dark rocky cliff face / rubble edge, top-down; frames the Rise and Echo Hollow |
| **Interior floors** | *(recolor `tile_road`/`tile_earth`)* | foundry brick, granary planks, wet-steel gallery, wet dark stone — recolors of the base ground/road tiles |
| **Roofs** | *(not required)* | the game is top-down open-air / walled, no roofed interiors to overprint |
| **Decorative tiles** | `tile_rubble` | a pile of broken concrete + rebar; movement-blocking scatter |

*Minimum engine set (must exist): `tile_earth`, `tile_earth_b`, `tile_road`, `tile_road_edge`, `tile_road_E`, `tile_road_W`, `tile_wall`, `tile_water`, `tile_shore` (+ the 6 directional shores), `tile_cliff`, `tile_rubble`.*

---

## 12. ART STYLE GUIDE
*Follow this so every asset looks like one game.*

- **Outline style:** a consistent **1-px dark outline** on characters, enemies, bosses, and props — not pure black; use the deep shadow tone `#1c1610` (or a district-darkened neutral). Tiles are **outline-less** (they must tile seamlessly) and rely on internal shading only.
- **Shading style:** flat cel shading, **2–3 tones per color** (base + one shadow + optional one highlight). No gradients, no dithered soft-shading on characters. Tiles may use light pixel-dithering for texture (cracks, gravel, water sparkle).
- **Lighting:** single directional key light from the **upper-left**; shadow tones fall lower-right. Warm local glow only from fire/embers/lanterns. Contrast stays low-to-medium and dusty; the world grows darker and cooler as districts descend.
- **Color limitations:** a tight, muted earth-neutral palette shared game-wide (Section 1), with **each district tinting** toward one hue and **rust-orange `#c2622e` reserved as the single accent** (Surveyor's scarf, portal, key highlights, UI selection). Avoid pure saturated primaries and pure white/black except as tiny highlights/outlines.
- **Animation style:** minimal, readable, low frame-count (1–3 frames typical). Motion is small and grounded — a stride, a breathe, a lunge — never rubbery or exaggerated. Idle poses are stable; walk1 must clearly read as mid-stride since it alternates with idle.
- **Texture detail:** medium — enough grit (rust streaks, cracks, patches, soot) to sell "weathered," but silhouettes stay clean and legible at small size. Don't over-noise small sprites.
- **Perspective:** overworld is **2.5D top-down** — tiles seen from above, characters/props drawn as **upright camera-facing billboards** with feet at the sprite's bottom. Battles are a flat **side view**. Keep a consistent implied ~30° down-angle so uprights and tiles agree.
- **Character proportions:** slightly stylized, roughly **1:3 head-to-body** (a chunky-cute-but-capable SNES-JRPG build) — head about a third of the body height, readable hands and feet, expressive silhouette over anatomical detail. Bosses use the same proportions scaled up and broadened for menace.
- **Environmental design philosophy:** every district must read as the same broken world seen at a new depth — reuse the shared tile/prop vocabulary, change only palette-tint, key architecture, and the one signature material (hides, glass, iron, water, grain, sludge, black stone). Silhouette and one identifying prop carry each district's and each character's identity; keep everything else quiet.

---

## 13. ASSET MANIFEST
*Production-ready. Filename = Asset ID + `.png`. All transparent unless noted. "Dir." = viewing directions. Priority: P1 = core gameplay, P2 = world, P3 = bosses/FX, P4 = polish.*

### Hero (24×32, transparent)
| Asset ID | Filename | Category | Description | Px | Tile | Transp. | Frames | Dir. | Priority |
|---|---|---|---|---|---|---|---|---|---|
| hero_front_idle | hero_front_idle.png | Character | Wren standing, facing camera | 24×32 | — | Yes | 1 | Front | P1 |
| hero_front_walk1 | hero_front_walk1.png | Character | front walk, left foot fwd | 24×32 | — | Yes | 1 | Front | P1 |
| hero_front_walk2 | hero_front_walk2.png | Character | front walk, right foot fwd | 24×32 | — | Yes | 1 | Front | P4 |
| hero_back_idle | hero_back_idle.png | Character | Wren from behind, standing | 24×32 | — | Yes | 1 | Back | P1 |
| hero_back_walk1 | hero_back_walk1.png | Character | back walk, left foot fwd | 24×32 | — | Yes | 1 | Back | P1 |
| hero_back_walk2 | hero_back_walk2.png | Character | back walk, right foot fwd | 24×32 | — | Yes | 1 | Back | P4 |
| hero_side_idle | hero_side_idle.png | Character | Wren profile, facing right | 24×32 | — | Yes | 1 | Right | P1 |
| hero_side_walk1 | hero_side_walk1.png | Character | side walk, mid-stride | 24×32 | — | Yes | 1 | Right | P1 |
| hero_side_walk2 | hero_side_walk2.png | Character | side walk, other stride | 24×32 | — | Yes | 1 | Right | P4 |
| hero_battle_idle | hero_battle_idle.png | Character | ready combat stance, facing right | 24×32 | — | Yes | 1 | Right | P1 |
| hero_battle_attack | hero_battle_attack.png | Character | lunging strike with tool | 24×32 | — | Yes | 1 | Right | P1 |

### Enemies (24×28, transparent — `_front` roaming + optional `_battle` facing left)
| Asset ID | Filename | Category | Description | Px | Transp. | Frames | Dir. | Priority |
|---|---|---|---|---|---|---|---|---|
| enemy_rise | enemy_rise.png | Enemy | Ridge Lookout, spyglass+tally | 24×28 | Yes | 1 | Front/Left | P1 |
| enemy_tannery | enemy_tannery.png | Enemy | Hide Toll-Taker, hook+apron | 24×28 | Yes | 1 | Front/Left | P2 |
| enemy_hollow | enemy_hollow.png | Enemy | Ravine Ambusher, signal-horn | 24×28 | Yes | 1 | Front/Left | P2 |
| enemy_lantern | enemy_lantern.png | Enemy | Foundry Crewman, glass shard | 24×28 | Yes | 1 | Front/Left | P2 |
| enemy_bellows | enemy_bellows.png | Enemy | Bellows-Hand, breather+iron | 24×28 | Yes | 1 | Front/Left | P2 |
| enemy_pump | enemy_pump.png | Enemy | Pipe-Bridge Guard, wrench | 24×28 | Yes | 1 | Front/Left | P2 |
| enemy_provision | enemy_provision.png | Enemy | Granary Guard, flail+satchel | 24×28 | Yes | 1 | Front/Left | P2 |
| enemy_outflow | enemy_outflow.png | Enemy | Sluice Gatekeeper, waders+key | 24×28 | Yes | 1 | Front/Left | P2 |
| enemy_cistern | enemy_cistern.png | Enemy | Cistern Sentry, plate+lantern | 24×28 | Yes | 1 | Front/Left | P2 |

### Bosses (40×48, transparent — `_battle` facing left)
| Asset ID | Filename | Category | Description | Px | Transp. | Frames | Dir. | Priority |
|---|---|---|---|---|---|---|---|---|
| boss_warden | boss_warden.png | Boss | Warden of the Rise, barrier-staff+tally-badge | 40×48 | Yes | 1 | Left | P3 |
| boss_baron | boss_baron.png | Boss | Patchwork Baron, hide-cloak+nail-crown | 40×48 | Yes | 1 | Left | P3 |
| boss_crier | boss_crier.png | Boss | The Crier, horn-mask+loudspeakers | 40×48 | Yes | 1 | Left | P3 |
| boss_lamplighter | boss_lamplighter.png | Boss | Lamplighter, cracked lens+searchlights | 40×48 | Yes | 1 | Left | P3 |
| boss_stoker | boss_stoker.png | Boss | The Stoker, bellows-iron+embers | 40×48 | Yes | 1 | Left | P3 |
| boss_valvemaster | boss_valvemaster.png | Boss | Valvemaster, fused pipe-wheel | 40×48 | Yes | 1 | Left | P3 |
| boss_miller | boss_miller.png | Boss | The Miller, grain-wheel throne+ledger | 40×48 | Yes | 1 | Left | P3 |
| boss_sluicewarden | boss_sluicewarden.png | Boss | Sluicewarden, waders+huge sluice-key | 40×48 | Yes | 1 | Left | P3 |
| boss_reclaimer | boss_reclaimer.png | Boss | The Reclaimer (final), long coat on black water | 40×48 | Yes | 1 | Left | P3 |

### Tiles (16×16, seamless — opaque except water edges)
| Asset ID | Filename | Category | Description | Px | Tile | Transp. | Priority |
|---|---|---|---|---|---|---|---|
| tile_earth | tile_earth.png | Tile/Ground | cracked wasteland earth | 16×16 | 1×1 | No | P1 |
| tile_earth_b | tile_earth_b.png | Tile/Ground | earth variant (2nd scatter) | 16×16 | 1×1 | No | P1 |
| tile_road | tile_road.png | Tile/Road | broken asphalt slabs | 16×16 | 1×1 | No | P1 |
| tile_road_edge | tile_road_edge.png | Tile/Road | road↔earth transition | 16×16 | 1×1 | No | P1 |
| tile_road_E | tile_road_E.png | Tile/Road | road edge, east side | 16×16 | 1×1 | No | P1 |
| tile_road_W | tile_road_W.png | Tile/Road | road edge, west side | 16×16 | 1×1 | No | P1 |
| tile_wall | tile_wall.png | Tile/Wall | ruined rust-streaked wall | 16×16 | 1×1 | No | P1 |
| tile_cliff | tile_cliff.png | Tile/Cliff | rocky cliff/rubble edge | 16×16 | 1×1 | No | P2 |
| tile_rubble | tile_rubble.png | Tile/Decor | concrete+rebar rubble (blocks) | 16×16 | 1×1 | Yes | P2 |
| tile_water | tile_water.png | Tile/Water | murky standing water | 16×16 | 1×1 | No | P2 |
| tile_shore | tile_shore.png | Tile/Water edge | water↔earth base transition | 16×16 | 1×1 | Yes | P2 |
| tile_shore_N | tile_shore_N.png | Tile/Water edge | shore, north side | 16×16 | 1×1 | Yes | P2 |
| tile_shore_S | tile_shore_S.png | Tile/Water edge | shore, south side | 16×16 | 1×1 | Yes | P2 |
| tile_shore_E | tile_shore_E.png | Tile/Water edge | shore, east side | 16×16 | 1×1 | Yes | P2 |
| tile_shore_W | tile_shore_W.png | Tile/Water edge | shore, west side | 16×16 | 1×1 | Yes | P2 |
| tile_shore_NE | tile_shore_NE.png | Tile/Water edge | shore, NE outer corner | 16×16 | 1×1 | Yes | P2 |
| tile_shore_NW | tile_shore_NW.png | Tile/Water edge | shore, NW outer corner | 16×16 | 1×1 | Yes | P2 |

### Props (transparent)
| Asset ID | Filename | Category | Description | Px | Transp. | Priority |
|---|---|---|---|---|---|---|
| prop_crate | prop_crate.png | Prop | weathered scrap crate | 16×16 | Yes | P1 |
| prop_chest | prop_chest.png | Prop | battered lockbox (gold latch glint) | 16×14 | Yes | P1 |
| prop_campfire | prop_campfire.png | Prop | fire in a stone ring, warm glow | 16×16 | Yes | P1 |
| prop_signpost | prop_signpost.png | Prop | leaning blank signpost | 16×20 | Yes | P2 |
| prop_barrel | prop_barrel.png | Prop | rusted dented barrel | 16×16 | Yes | P4 |
| prop_lamppost | prop_lamppost.png | Prop | broken dark street lamp | 16×28 | Yes | P4 |
| prop_drying_rack | prop_drying_rack.png | Prop | tanner's rack with hides (D2) | 20×20 | Yes | P4 |
| prop_pipe | prop_pipe.png | Prop | rusted pipe segment (D6/D8) | 20×16 | Yes | P4 |
| prop_valve_wheel | prop_valve_wheel.png | Prop | rusted valve hand-wheel (D6/D8) | 16×16 | Yes | P4 |
| prop_grain_sack | prop_grain_sack.png | Prop | sackcloth grain sack (D7) | 16×16 | Yes | P4 |
| prop_glass_rack | prop_glass_rack.png | Prop | rack of cracked glass panes (D4) | 20×20 | Yes | P4 |

### FX & backdrop (transparent except backdrop)
| Asset ID | Filename | Category | Description | Px | Transp. | Frames | Priority |
|---|---|---|---|---|---|---|---|
| fx_slash | fx_slash.png | FX | white-and-rust strike arc | 32×32 | Yes | 1 | P1 |
| portal_ring | portal_ring.png | FX | rust-orange vortex ring (intro) | 128×128 | Yes | 1 | P3 |
| backdrop_generic | backdrop_generic.png | Backdrop | ruined ground under dusk sky, empty foreground | 320×180 | No | 1 | P1 |
| fx_hit_spark | fx_hit_spark.png | FX | spark+dust burst on hit | 24×24 | Yes | 3 | P3 |
| fx_heal | fx_heal.png | FX | warm rising motes (campfire heal) | 32×32 | Yes | 4 | P3 |
| fx_levelup | fx_levelup.png | FX | rust-gold ring pulse | 48×48 | Yes | 5 | P3 |
| fx_loot_glint | fx_loot_glint.png | FX | sparkle on chest open | 16×16 | Yes | 3 | P4 |
| fx_smoke | fx_smoke.png | FX | drifting soot (D4/D5) | 24×24 | Yes | 4 | P4 |
| fx_embers | fx_embers.png | FX | rising embers (D5) | 16×16 | Yes | 4 | P4 |
| fx_water_ripple | fx_water_ripple.png | FX | expanding ripple (D6/D9) | 16×16 | Yes | 4 | P4 |

### Optional UI (only if arting the interface; match Section 9 & 12)
| Asset ID | Filename | Category | Description | Px | Transp. | Priority |
|---|---|---|---|---|---|
| ui_button | ui_button.png | UI | riveted metal answer/menu button | 96×28 | Yes | P4 |
| ui_healthbar | ui_healthbar.png | UI | dented metal health gauge frame+fill | 120×14 | Yes | P4 |
| ui_xpbar | ui_xpbar.png | UI | brass XP gauge frame+fill | 120×8 | Yes | P4 |
| ui_panel | ui_panel.png | UI | weathered parchment-on-metal question/dialogue panel | 320×120 | Yes | P4 |
| ui_cursor | ui_cursor.png | UI | rust-orange survey reticle | 16×16 | Yes | P4 |
| ui_progress_rail | ui_progress_rail.png | UI | vertical 9-district descent rail with seals | 24×200 | Yes | P4 |

---

## 14. ART PRODUCTION QUEUE
*Build in this order. Every asset has a 2–5 sentence visual description so it can be made without follow-up questions. Names are the Asset IDs from Section 13.*

### PHASE 1 — Core Gameplay (the game is playable and cohesive with just these)

1. **`hero_front_idle`** — Wren Calder standing, facing the camera, full body in 24×32. A lean traveller in a weathered open brown duster over a canvas harness, a **rust-orange dust-scarf** at the neck, brass goggles pushed up on the forehead, satchel and pouched belt, gloved hands, scuffed boots, calm determined face. Feet at the bottom edge, 1-px dark outline, upper-left light, 2–3 flat tones. This is the anchor asset — every other character should feel like it belongs beside this one.
2. **`hero_front_walk1`** — same character and view, clearly mid-stride with the **left foot forward** and the duster hem shifted; arms in a slight counter-swing. It must read as motion when alternated with the idle, so exaggerate the stride a touch.
3. **`hero_back_idle`** — Wren seen from directly behind: the back of the hood/hair, the duster back with a center seam, the satchel strap crossing, no face. Same palette and outline; the rust scarf peeks at the collar.
4. **`hero_back_walk1`** — back view, mid-stride left foot forward, hem and arms shifted to match the front walk's cadence.
5. **`hero_side_idle`** — strict right-facing profile, standing. The goggles-lump on the forehead, the scarf, the satchel on the near shoulder, and the flared duster hem make the silhouette. Left-facing is mirrored in-engine, so only draw right.
6. **`hero_side_walk1`** — right profile mid-stride, front leg extended, back leg pushing off, duster trailing slightly.
7. **`hero_battle_idle`** — right-facing combat-ready stance, weight low, the scavenged multi-tool/short blade in the lead hand. Reads as braced and capable, used on the left side of the battle screen.
8. **`hero_battle_attack`** — the same character lunging forward into a strike, tool swept ahead, front knee bent, scarf and hem flung by the motion. Pairs with `fx_slash`.
9. **`enemy_rise`** — Ridge Lookout, 24×28: a wary figure in a patched dust-cloak (dusty-tan tint), hunched and watchful, holding a **brass spyglass** and a notched **tally-stick**. Clearly weaker/scrappier than the hero — the gentle first foe. Provide a front idle usable both roaming and (facing left) in battle.
10. **`tile_earth`** — a seamless 16×16 top-down tile of dry cracked wasteland earth, dusty tan, scattered small pebbles and hairline cracks, light pixel-dither texture, **no outline**, tiles edge-to-edge with no visible seam.
11. **`tile_earth_b`** — the same cracked earth with a **different** scatter of pebbles/cracks so large fields don't visibly repeat; identical palette and tiling.
12. **`tile_road`** — a seamless 16×16 tile of broken ash-grey asphalt: cracked slabs, faded lane residue, small potholes; tiles cleanly in all directions.
13. **`tile_road_edge`** — broken asphalt with dry dirt intruding along **one edge**, for road-to-earth transitions; must line up with both `tile_road` and `tile_earth`.
14. **`tile_road_E`** / **15. `tile_road_W`** — directional road-edge pieces (dirt on the east / west side respectively) so road strips end cleanly against earth.
16. **`tile_wall`** — a seamless 16×16 ruined wall tile (brick/concrete with rust streaks), shown with a little top-down thickness/cap so walls read as solid from above.
17. **`prop_crate`** — a 16×16 weathered wooden scrap-crate, mismatched planks, one cracked board, faint worn stencil marks; 1-px outline, transparent. Reads as loot/cover.
18. **`prop_chest`** — a 16×14 battered metal footlocker, closed, rust-pitted, with a small **brass keyhole and a faint gold glint** on the latch so players know it opens.
19. **`prop_campfire`** — a 16×16 small fire in a ring of blackened stones, warm orange-to-yellow flame, a soft glow halo, a thin smoke curl. The one warm, inviting object in the game.
20. **`fx_slash`** — a 32×32 quick white-and-rust diagonal slash arc on transparent bg, bright core fading to rust edges; flashes on a correct-answer hit.
21. **`backdrop_generic`** — a 320×180 side-view battle backdrop: ruined post-apocalyptic ground under a dusky sky, a soft dithered gradient, low broken-silhouette ruins on the horizon, and an **empty foreground** where the hero (left) and enemy (right) stand. Muted, low-contrast, so sprites pop against it.

### PHASE 2 — World Expansion (fills out all nine districts)

22–29. **`enemy_tannery`, `enemy_hollow`, `enemy_lantern`, `enemy_bellows`, `enemy_pump`, `enemy_provision`, `enemy_outflow`, `enemy_cistern`** — the eight remaining district foes, 24×28 each, per the descriptions and district tints in Section 5. Escalate the sense of threat down the list: the Tannery toll-taker is a bulky brute; the Cistern sentry is dark-plated and imposing, edging toward boss-like. Each carries its one identifying prop (hook, signal-horn, glass shard, stoking iron, valve-wrench, flail, gate-key, cold lantern) and its district hue, but all share the hero's outline/shading language.
30. **`tile_water`** — seamless 16×16 murky teal-grey standing water with faint highlight glints; recolorable to sludge-green (D8) and near-black (D9).
31–37. **`tile_shore`, `tile_shore_N/S/E/W`, `tile_shore_NE`, `tile_shore_NW`** — the water-to-land transition set: a base shore plus four side edges and two outer corners, each a jagged wet mud/earth margin meeting the water, transparent where water shows, aligning with `tile_water` and the ground tiles so pools read cleanly.
38. **`tile_cliff`** — a 16×16 dark rocky cliff-face/rubble edge, top-down, to wall off the Rise and Echo Hollow; internal shading, no outline.
39. **`tile_rubble`** — a 16×16 pile of broken concrete chunks and bent rebar, transparent background, reads as a movement-blocking obstacle.
40. **`prop_signpost`** — a 16×20 leaning weathered wooden post with a blank cracked board and one rusted nail, listing to one side; marks routes and gates.
41–46. **District flavor props** — **`prop_barrel`** (rusted dented barrel), **`prop_drying_rack`** (20×20 A-frame hung with cured hides, D2), **`prop_pipe`** (20×16 rusted pipe segment with a drip, D6/D8), **`prop_valve_wheel`** (16×16 rusted hand-wheel, D6/D8), **`prop_grain_sack`** (16×16 plump tied sack with a grain spill, D7), **`prop_glass_rack`** (20×20 rack of cracked panes catching teal light, D4). Each transparent, outlined, in its district tint.

### PHASE 3 — Bosses & Effects

47–55. **`boss_warden`, `boss_baron`, `boss_crier`, `boss_lamplighter`, `boss_stoker`, `boss_valvemaster`, `boss_miller`, `boss_sluicewarden`, `boss_reclaimer`** — the nine gate-bosses, 40×48 each, battle pose facing **left**, per Section 6. Each needs a bigger, heavier silhouette than the enemies and **one unmistakable feature**: the Warden's barrier-staff and tally-badge; the Baron's nail-crown and mountain of stitched hides; the Crier's horn-mask and trailing loudspeaker cables; the Lamplighter gaunt atop a glowing cracked lens; the Stoker's white-hot bellows-iron and rising embers; the Valvemaster fused to a barnacled pipe-wheel; the Miller throned on a grain-wheel with sacks and a ledger; the Sluicewarden tall in streaming waders with a huge sluice-key; and the **Reclaimer** — the final boss — as the calmest, most refined silhouette of all, a long clean coat on a causeway with still black water mirroring him. Escalate palette richness/darkness down the list.
56. **`portal_ring`** — a 128×128 glowing rust-orange concentric vortex ring on transparent bg, energy rippling inward; the region-entry portal in the intro.
57–59. **`fx_hit_spark`** (24×24, 3 frames of pale sparks + dust on a connect), **`fx_heal`** (32×32, 4 frames of soft warm-gold motes rising around the hero at a campfire), **`fx_levelup`** (48×48, 5 frames of a rust-gold ring pulse with a few sparks rising off the hero).

### PHASE 4 — Polish (optional; the game is complete without these)

60. **`hero_front_walk2`, `hero_back_walk2`, `hero_side_walk2`** — the opposite-stride second walk frames for smoother 3-frame walk cycles per direction (same style as the Phase-1 walks, mirrored footing).
61. **Optional enemy/boss extra frames** — `<enemy>_walk1/2`, `<boss>_attack`, `<boss>_hit`: small motion and attack/recoil poses to animate roaming and fights.
62. **`prop_lamppost`** (16×28 broken dark street lamp, drooping wires) and any remaining decorative clutter to dress empty corners.
63. **Ambient FX loops** — **`fx_smoke`** (24×24, 4-frame drifting soot for D4/D5), **`fx_embers`** (16×16, 4-frame rising embers for D5), **`fx_water_ripple`** (16×16, 4-frame ripple for D6/D9), **`fx_loot_glint`** (16×16, 3-frame chest sparkle).
64. **Per-district backdrops** — recolors of `backdrop_generic` toward each district's palette (bleached Rise, ember Bellows, black Cistern, etc.), named `backdrop_<district>` if the engine is later extended to swap them.
65. **Optional UI set** — `ui_button`, `ui_healthbar`, `ui_xpbar`, `ui_panel`, `ui_cursor`, `ui_progress_rail`, per Section 9, only if replacing the current CSS interface; all in the weathered-metal + rust-orange language so they match the world.

---

*End of Game Art Specification — The Long Survey. Deliver every file named exactly as its Asset ID (`<AssetID>.png`), transparent unless the manifest says otherwise, then drop the folder onto the game's title screen to load it.*

---

## HOW SPRITES ARE SIZED & DELIVERED (read this before generating anything)

**One high-resolution master per character covers BOTH in-game sizes.** The game shows each character at two scales — a tiny sprite while walking the overworld, and a large close-up in the fight screen (which can display 1000–1700 px tall). **You do NOT need to make tiny pixel versions.** For EVERY character (the hero, each enemy, each boss) deliver **one clean high-resolution master at 768 × 1024 px** (bosses may go up to 1024 × 1024 for a bigger silhouette). The game derives both the small overworld sprite and the large battle close-up from that single master, so the two always match.

Character master files (768×1024, transparent, full body):
- Hero: `hero_battle_idle.png`, `hero_battle_attack.png`
- Enemies (×9): `enemy_<district>_battle.png` — `enemy_rise_battle.png`, `enemy_tannery_battle.png`, `enemy_hollow_battle.png`, `enemy_lantern_battle.png`, `enemy_bellows_battle.png`, `enemy_pump_battle.png`, `enemy_provision_battle.png`, `enemy_outflow_battle.png`, `enemy_cistern_battle.png`
- Bosses (×9): `boss_<name>_battle.png` — `boss_warden_battle.png`, `boss_baron_battle.png`, `boss_crier_battle.png`, `boss_lamplighter_battle.png`, `boss_stoker_battle.png`, `boss_valvemaster_battle.png`, `boss_miller_battle.png`, `boss_sluicewarden_battle.png`, `boss_reclaimer_battle.png`

Tiles (16×16, seamless), props, visual effects, and backdrops are delivered at their native small sizes as listed in the manifest above.

## CRITICAL RULES — every image MUST follow these (past batches failed on each one)

1. **Truly transparent background (alpha = 0).** Never paint a grey/white checkerboard pattern, never a solid color fill, never a card or frame, never scenery — just the character on real transparency.
2. **No text anywhere** — no filename, dimensions, label, or watermark on the image.
3. **No floating stray objects** beside the character (no separate lanterns, keys, batteries, glow orbs, panels). The character holds its own tool/weapon IN its hand.
4. **Draw exactly the character described** for each filename — never substitute a different character.
5. **Full body, centered, feet near the bottom**, one character per file, same weathered detailed pixel-art style throughout.
6. **Name each file exactly by its Asset ID**, and deliver everything in one downloadable folder.
7. **Generate fresh** — do not edit, trace, or upscale any earlier image.

## TITLE CARDS (optional but nice — drop-in scenic art)

Two kinds of wide title-card images. The game draws the title/name **text on top** in-engine, so these images should be **atmospheric scenes with no baked-in text** (follow the same "no text on the image" rule). Landscape, non-transparent (they fill the screen). Target **1280 × 720 px**.

- **`title_game.png`** — the game's splash: Wren Calder, the Surveyor, a small silhouette on the sunlit ridge at the top, looking down over the whole ruined region falling away below (broken towers, dust, rust) — the melancholy "one long descent" mood. Leave the upper-center relatively clear for the title text.
- **`title_<district>.png` (×9)** — a wide establishing shot of each district, shown for a beat when the player first crosses into it (behind the district name). One per district, matching its Section 2 theme and palette:
  - `title_rise.png` — Vantage Rise: the open, bleached ridge with the observation deck and the sprawl hazy below.
  - `title_tannery.png` — The Tannery Rows: the cramped ochre market street of patched tarps and hanging hides.
  - `title_hollow.png` — Echo Hollow: the grey ravine pass walled by cliffs and leaning broadcast towers.
  - `title_lantern.png` — Lantern Watch: the teal glass-strewn lighthouse yard with the great cracked lens.
  - `title_bellows.png` — The Bellows Yards: the ember-lit industrial air-works of vent walls and smoking stacks.
  - `title_pump.png` — The Pump Works: the half-drowned teal waterworks of pipe-bridges over open water.
  - `title_provision.png` — The Provision Halls: the golden granary quarter of silos, sacks, and the grain-wheel.
  - `title_outflow.png` — The Outflow: the sickly-green drainage works of sludge channels and iron sluice-gates.
  - `title_cistern.png` — The Deep Cistern: the vast near-black drowned chamber, still water and a distant cold glow.

Keep them consistent with the game's weathered post-apocalyptic style. The engine fades to black, shows this card + the district name for a moment, then fades into the new area.
