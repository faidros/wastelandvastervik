# Västervik / Åhmans

## 2026-11-23 — first city and Åhmans model

- Built a 1 km square around the Åhmans OpenStreetMap point at 57.7553448, 16.6415434.
- The game uses Swedish text and Copernicus GLO-30 terrain. OpenStreetMap attribution remains in the game pack.
- The OSM point is mapped as a fast-food business, but there is no building footprint at that location. Added a standalone low, dark single-storey gatukök with glazing, red fascia and a kitchen vent, plus a matching gameplay collision footprint and Åhmans map label.
- Visual reference: Google Street View at Hallströmsgatan 1 (imagery dated August 2024), viewed only and not copied into the project. The official Åhmans site identifies it as the classic gatukök by the station and gives the address Hallströmsgatan 1: https://ahmans.nu/
- The approximate footprint and façade are inferred from the map and Street View; the model is not a survey-grade reconstruction. User requested further local refinement, especially around Åhmans and the centre.
- The first Overpass completion attempt timed out. The primary OSM API data built successfully; a later refresh can fill any missing outlying features.

## 2026-11-23 — central Street View sample

- Reviewed August 2024 Street View and a satellite view around Gösta Bernhards gata and Båtsmansgatan; source frames were kept outside the repository.
- Corrected `w1036831300` to a yellow timber building with white trim and a dark pitched roof.
- Corrected `w391945954` to a pale cream plaster building with red window frames and a red tiled roof.
- These are a small sample of the 71 surrounding buildings identified by the survey plan; other untagged facades remain generated estimates.

## 2026-11-23 — start moved to Hallströmsgatan

- Moved the game spawn to the southernmost in-bounds section of Hallströmsgatan, 22 m inward from its endpoint at the southern edge of the play area.
- Verified the spawn is on the mapped road, on land, 10.1 m from the nearest building footprint, and passes the installed-city route test.

## 2026-11-23 — alternate Hallströmsgatan start

- For comparison, moved the start to the opposite (northern) end of the in-bounds Hallströmsgatan, 22 m inward from its endpoint near Åhmans.

## 2026-11-23 — Åhmans sign

- Added raised, warm illuminated “Åhmans” lettering to the enlarged red storefront fascia using the shared housekit sign geometry, so it remains part of the streamed 3D building and reads clearly in-game.

## 2026-11-23 — prison, station and Sankt Petri

- Replaced the generic models of Hotell Fängelset, Västervik station and Sankt Petri kyrka with hand-built landmark models.
- Added the prison's three-storey facade rhythm, hipped roof, roof lantern and chimneys; the station's pale three-storey frontage, hipped roof, dormers, central gable and name sign; and Sankt Petri's red-brick Latin-cross body, pointed windows, crossing tower, high spire and smaller pinnacles.
- Corrected the three buildings' style, roof and height overrides. Existing OSM footprints remain the gameplay collision outlines.
- Used an openly licensed 2011 station photo and a public-domain historical church postcard. The hotel history image was viewed as a reference only and was not stored. Sources and notes are in `references/`.
- The models are visual interpretations of the supplied sources, not survey-grade reconstructions.

## 2026-11-23 — Ellen Key school

- Replaced the generated models of the two OSM buildings tagged as school with hand-built interpretations of the 1870 main building and the 1950s wing.
- Detailed the main building with three storeys, a granite plinth, neo-Romanesque arched windows and surrounds, string courses, a low green hipped metal roof and chimneys.
- Reworked the 1950s wing as pale rendered functionalist architecture with regular modern windows, a flat roof and a glazed stair bay.
- Used Kalmar County Museum's 2021 building-history survey for architectural facts; no report images were copied. The 1936 addition is not separately identifiable among the current OSM school footprints and was not assigned to a nearby non-school building.
- Models are visual interpretations, not survey-grade reconstructions; source and architectural notes are in `references/`.

## 2026-11-24 — Tjustgatan, Hagaholmsgatan and Allén shops

- Expanded the playable map to a 1,600 m square and refreshed OSM and terrain data so Tjustgatan 1, Hagaholmsgatan 7, V-DATA and Corner are all included.
- Replaced the generic house models at Tjustgatan 1 and Hagaholmsgatan 7 with Street View-based timber-house interpretations, correcting their storeys, siding, roof forms and colours.
- Identified the small gabled shop beside the taller apartment block as V-DATA's storefront and modelled its display glazing and raised red “V-DATA” sign. The adjacent apartment block remains a separate generated building.
- Reworked Corner at Allén 1 as a low, pale restaurant with broad glazing, a dark shallow roof, green awning and prominent red “Corner” lettering with a smaller “BURGERS & GRILL” line.
- Street View imagery from August 2024 was viewed only and not copied. The official V-DATA contact page and Corner website confirm their addresses; see `references/SOURCES.md`.
- These are visual interpretations of the public street views, not survey-grade reconstructions.

## 2026-11-24 — Sillgatan and Stora torget expansion

- Expanded the playable map to a 3,200 m square centered at 57.75897, 16.63065, retaining the existing Åhmans and Hallströmsgatan start area while reaching Sillgatan.
- Added custom house models for Sillgatan 9 (white plaster with dark timber framing, a tiled roof and dormer) and Rådjursstigen 15 (light vertical timber siding, stone base and red tiled gable roof).
- Replaced the generic Stora torget town hall with a pale plaster landmark model featuring a mansard roof, central lantern and clock detail; added the RÅDHUSET map label.
- Used August 2024 Street View for the two houses and a public-domain historical photograph from DigitaltMuseum for the town hall. Street View imagery was viewed only; the town hall image, source details and architectural notes are kept under `references/`.
- The map prepared and exported successfully with 3,397 building footprints, 2,227 streamed tiles and no failed custom models. OSM's primary API supplied the map; Overpass mirrors were unavailable during this refresh. Copernicus GLO-30 supplies the terrain.
- The final custom scripts use explicit observed materials so these models render correctly in the exported city. Per-building override facts are saved in `overrides.json` and will also be applied to generated building metadata on the next `prepare` run.
- Visual interpretations, not survey-grade reconstructions.

## 2026-11-24 — Ljungheden expansion

- Expanded the playable map to a 4,800 m square centered at 57.76175, 16.62, preserving the previous play area while extending north and west to include Ljungheden and Västervik Speedway.
- Added Ljungheden as a label on the tactical map. Åhmans and the Hallströmsgatan spawn were shifted with the map origin so the existing start area remains in place.
- Rebuilt the city with Copernicus GLO-30 terrain: 4,788 OSM building footprints, 2,408 roads and paths, 4,860 streamed tiles, and 13 custom models with no failures. Other buildings remain OSM-based generated estimates.
- The game test suite passes (72/72); visual interpretations and generated building heights are not survey-grade.

## 2026-11-25 — Slottsholmen and Stegeholms slottsruin

- Added the SLOTTSHOLMEN tactical-map label and a collision footprint for the castle ruin, which OSM maps as a historic ruin rather than a building.
- Hand-modelled Stegeholms slottsruin with irregular surviving walls, a gated arch, courtyard remains, a well and the present-day lookout platform and stairs.
- Reworked four hotel volumes with brick and timber facades, windows, balconies and roof details; included a floating-hotel interpretation. The hotel identification and forms are interpreted from the mapped footprints and architectural references, not survey-grade measurements.
- Used Sandellsandberg's project material and official hotel information as visual references. Stored two Wikimedia Commons ruin photographs by AleWi under CC BY-SA 4.0 with attribution; sources and model notes are in `references/`.
- Re-exported and packed the full city: 6,998 building footprints, 2,408 roads and paths, 4,860 streamed tiles and 125 materials. The Hallströmsgatan spawn and OpenStreetMap attribution remain in place.
- Reviewed focused ruin and waterfront renders. The game test suite passes (72/72); Copernicus GLO-30 terrain and generated surrounding buildings remain as before.
