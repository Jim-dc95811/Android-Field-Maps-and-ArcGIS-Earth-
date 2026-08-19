# Android Field Maps + ArcGIS Earth — Roadmap

## Current mission

Deploy finished local map products and proven ArcGIS Earth / Windows field features to the user with the least possible operator complexity.

For personal Android maps, the preferred path is **local removable storage**, not a field server.

```text
Offline Map Factory
→ TPKX
→ microSD card
→ Android
→ Field Maps / ArcGIS Earth
```

For optional Windows live positioning:

```text
PRAVE radio reports
→ PRAVE Live
→ ArcGIS Earth Automation API
→ remote units on the map
```

For optical dispatch / command input:

```text
phone / QR card
→ QR Command Bridge
→ strict parser / allowlist
→ approved ArcGIS Earth or Windows action
```

## Current user features

### PRAVE Live

**Status: LIVE-PROVEN.**

The preserved original v0.1.0 package lives under `features/prave-live/`.

Do not rewrite that evidence package. Future usability improvements, such as automatic COM-port discovery or cleaner novice packaging, should be treated as a new controlled version and must earn their own live acceptance.

### QR Command Bridge

**Status: LIVE-PROVEN FOUNDATION / COMMAND EXPANSION DESIGNED.**

The recovered Gold lineage proves camera QR decode, MacroDroid SMS JSON, coordinate/message parsing, `GMDS_CMD:TEST`, and blocking of unknown command tokens.

The modern branch must keep the hard-coded allowlist rule. QR payload text must never become generic shell or script input.

Next controlled QR gates:

1. build a modern ArcGIS Earth action using the existing command-token front end;
2. prove it against the ArcGIS Earth local Automation API;
3. add Windows/helper actions one at a time only when useful;
4. require an additional confirmation/interlock for destructive actions such as restart/shutdown/reset;
5. promote each action only after real-target testing.

## Immediate map acceptance gates

### 1. Measure real card payloads

Finish controlled map builds and record exact finished sizes for:

- district-wide Z17;
- county-level Z18;
- selected State Forest / high-value Z20 areas;
- Google Hybrid versus Esri imagery/labels equivalents where both are useful.

Do not freeze card tiers until real byte counts exist.

### 2. Field Maps local-TPKX acceptance

Esri documents TPKX sideloading to Android/microSD. This project still needs its own live proof.

Acceptance test:

1. place a known-good Factory TPKX in the Field Maps `basemaps` folder on microSD;
2. open Field Maps;
3. select the local basemap;
4. set Field Maps to Wi-Fi only at the Android level;
5. turn Wi-Fi off;
6. keep normal phone cellular service on;
7. verify local imagery continues to pan/zoom;
8. verify phone GPS / own-position behavior;
9. close/reopen Field Maps and confirm the local map remains usable.

Promote only after the real phone passes.

### 3. ArcGIS Earth microSD acceptance

Local TPKX has already been LIVE-PROVEN in ArcGIS Earth Mobile on multiple project packages. Repeat the test using the intended card layout and representative production-size maps.

## Card-menu direction

The user-facing menu should remain simple:

- District — Z17
- County — Z18
- State Forests / selected hotspots — Z20
- Google Hybrid and/or Esri imagery/labels as capacity permits

Smaller cards get the highest-value coverage first. Larger cards get broader coverage and more high-resolution areas.

## User-experience rule

Do not turn this into GIS or computer-administration training.

The desired handoff is:

> Prepared map or proven feature → short instructions → work.

## Optional later additions

Only after real users ask for them:

- one or two high-value overlays;
- additional TPKX themes;
- local MMPK reference packages;
- Rasta deep-zoom reference imagery;
- improved card inventory/version labeling;
- a novice-friendly successor to PRAVE Live v0.1.0 with automatic serial-port discovery;
- additional individually allowlisted QR actions;
- a two-way response-QR / optical-bus branch after the one-way command path is mature.

Do not add features because they are technically possible. Add them because the field user actually benefits.

## Map Fountain relationship

Map Fountain is no longer the primary personal-phone deployment direction. Preserve it as a LIVE-PROVEN engineering reference for:

- Windows ArcGIS Earth direct TPKX over SMB;
- router-only Static REST WMTS to ArcGIS Earth Mobile.

Possible future return: Starlink-connected basecamp storage / poor-man's NAS.

## Governing rule

> **Have the data and the field capability ready before the user needs them.**
