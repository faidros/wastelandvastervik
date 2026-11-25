# cities/

One folder per generated place (git-ignored — they are large and rebuildable):

| file | made by | edit? |
|---|---|---|
| `place.json` | `wasteland.py new` | yes: centre, size |
| `osm.json` | `fetch` (OSM API / Overpass, ODbL) | no |
| `city.json` | `prepare` | no — regenerated |
| `city.blend` | `blender` | in Blender if you like, then `build --from export` (a rebuild overwrites it) |
| `build/raw/` | `export` | no |
| `pack/` | `tiles`, `pack` — what the game loads | no |
| `theme.json` | `theme` | **yes**: title, texts, voice lines, prompts |
| `overrides.json` | you / refine-city | **yes**: corrected buildings, areas, roads, spawn, and extra collision footprints |
| `custom/<id>.py` | you / refine-city | **yes**: hand-modelled buildings |
| `media/` | imagegen, voices, music | **yes**: splash.jpg, voice-*.mp3, music/ |
| `references/` | you | your own photos, drawings, openly licensed pictures (+ `SOURCES.md`) for refinement rounds |
| `refinements.md` | refine-city | log of improvement rounds |
| `renders/` | `render` | review images |

To share a city without the big files, share `place.json`, `theme.json`, `overrides.json`,
`custom/` and `media/`; anyone can rebuild the rest with `python3 wasteland.py build <slug>`.

For a hand-modelled building that has no OpenStreetMap footprint, add its local-metre polygon
(`x` east, `y` north) to `overrides.json` as a `collision_footprints` entry. The game uses it for
vehicle collision and spawn clearance; a Blender custom model alone is only visual geometry.
To place the start near an end of a named drivable street, set `spawn` to
`{"road": "Street name", "end": "north", "offset_m": 22}` (`end` may be `north` or `south`).
The pack measures inward from that end of the street's in-bounds portion and checks the chosen
point for building and land clearance. An optional `heading_offset_deg` rotates the starting
direction relative to the street (positive values turn left).
