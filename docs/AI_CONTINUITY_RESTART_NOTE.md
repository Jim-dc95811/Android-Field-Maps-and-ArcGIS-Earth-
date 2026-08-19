# Android Field Maps + ArcGIS Earth — AI / Maintainer Restart Note

## Project identity

This repository is the **deployment-to-the-user end** of the four-project family.

Its job is not to manufacture maps. Its job is to make finished map products and proven ArcGIS Earth / Windows field features usable without dragging the operator through the engineering stack.

## Current deployment doctrine

### Personal Android maps

```text
Offline Map Factory
→ finished TPKX
→ microSD / local storage
→ Android phone
→ ArcGIS Field Maps or ArcGIS Earth
```

Primary benefit:

- local imagery;
- no operational dependence on cellular basemap delivery;
- user can block Field Maps from cellular data while leaving ordinary phone service available;
- large prebuilt pyramids can respond from local storage instead of waiting on weak field connectivity.

### PRAVE Live — Windows ArcGIS Earth

```text
$PRAVE radio reports
→ Windows serial input
→ PRAVE Live
→ ArcGIS Earth local Automation API
→ remote units on the operational map
```

PRAVE Live is **LIVE-PROVEN** and its authoritative user-facing home is:

`features/prave-live/`

The exact original package is preserved there as `AE_PRAVE_LIVE_v0_1_0_TEST.zip`.

Do not silently modify that ZIP and continue calling it the original proof package.

Role split:

```text
ArcGIS Earth native GNSS → ME / own position
PRAVE Live              → remote PRAVE units
```

The deeper parser/API engineering record remains in Offline GeoStack.

### QR Command Bridge — optical dispatch / command input

Authoritative feature home:

`features/qr-command-bridge/`

Current evidence boundary:

- camera QR decode: **LIVE-PROVEN lineage**;
- MacroDroid SMS JSON → QR: **LIVE-PROVEN lineage**;
- coordinate/message parser: **LIVE-PROVEN lineage**;
- `GMDS_CMD:TEST` + unknown-command blocking: **LIVE-PROVEN command proof**;
- ArcGIS Earth API commands triggered by QR: **DESIGNED / NOT YET LIVE-PROVEN**;
- Windows restart/shutdown/helper actions: **DESIGNED / NOT YET LIVE-PROVEN**.

Hard security rule:

> **QR text is data, never executable code.**

The modern branch must preserve explicit hard-coded action names / allowlists. Never pass QR text directly to `cmd.exe`, PowerShell, Python `eval`, shell execution, or another generic command interpreter.

Destructive actions require an additional confirmation/interlock before they are accepted as a field feature.

The exact historical QR package identities and hashes are preserved in:

`features/qr-command-bridge/EVIDENCE_AND_LINEAGE.md`

Do not claim historical command-card ideas were implemented merely because they were documented.

## Current map-card plan

Do not freeze exact capacity tiers until real Factory sizes are measured.

Current menu direction:

- district Z17;
- county Z18;
- State Forests / selected high-value areas Z20;
- Google Hybrid and Esri imagery/labels where useful and capacity allows.

## Evidence status

- Offline Map Factory 1.0: BUILT / SELF-TESTED — live acceptance pending under the new product name.
- Historical TPKX Map Factory v1.0.0: RELEASE-ACCEPTED / frozen milestone.
- Local TPKX in ArcGIS Earth Mobile: LIVE-PROVEN on multiple packages.
- Esri documentation supports Field Maps Android TPKX basemaps on device/microSD: DOCUMENTED BY VENDOR.
- This project's own Field Maps + microSD TPKX test: PENDING LIVE TEST.
- PRAVE → ArcGIS Earth Automation API live display: LIVE-PROVEN.
- QR Gold optical receiver / TEST allowlist lineage: LIVE-PROVEN as recorded above.
- Field Maps Android app-level Wi-Fi-only cellular block: documented by Esri Support.

Do not silently promote vendor documentation, self-tests, or design notes into this project's LIVE-PROVEN status.

## Field Maps sideload path

```text
\Android\data\com.esri.fieldmaps\files\basemaps
```

Supported vendor-documented basemap types include TPK/TPKX/VTPK and geospatial PDF.

A true default offline basemap is configured by the web-map owner in Field Maps Designer. An ordinary phone user can still select an available basemap from the Field Maps Overflow/Basemap control.

## Personal-phone cellular rule

The Field Maps in-app Cellular Data setting is not a total app-level block.

For full cellular blocking on Android, use the device network setting and set ArcGIS Field Maps to Wi-Fi only.

This is important because the target audience may be using personal phones and personal data plans.

## Human-factors rule

The operator-facing workflow must stay short.

Do not turn the deployment repo into an encyclopedia of GIS features.

For Field Maps:

> card → cheat sheet → local basemap → Wi-Fi only → work

For PRAVE Live, preserve the proven path now; if it is later repackaged for normal users, automatic COM-port discovery should replace source editing.

For QR Command Bridge, the operator sees a result or an approved named action—not a scripting language.

Overlays, MMPKs, geofences, complex forms, and other GIS features are optional future branches only when a real field need appears.

## Relationship to sibling repositories

- Offline GeoStack — master map manufacturing and deeper integration engineering record.
- Rasta Pyramid Factory — general high-resolution raster-pyramid manufacturing.
- Map Fountain — proven router/network-storage experiments; parked from primary personal-phone deployment, possible future Starlink/NAS role.
- This repo — final Android deployment plus user-facing ArcGIS Earth / Windows field features.

## Do not regress

- Do not require a field server for the normal personal-phone map path.
- Do not require public Internet for the map itself.
- Do not make the user learn QGIS/Python/TPKX internals.
- Do not bury the one-page Field Maps procedure under advanced features.
- Do not claim Field Maps live acceptance until the actual phone test passes.
- Do not rewrite the preserved PRAVE Live proof ZIP by inertia.
- Do not allow arbitrary executable text through QR.
- Do not promote planned QR restart/shutdown/API actions before real target tests.
- Do not distribute third-party imagery without respecting its terms.

## Cold-start reading order

1. `README.md`
2. `features/prave-live/README.md` when PRAVE/remote-unit display matters
3. `features/qr-command-bridge/README.md` and `EVIDENCE_AND_LINEAGE.md` when QR matters
4. `FIELD_MAPS_SD_CARD_QUICK_GUIDE.md`
5. `ROADMAP.md`
6. this file
7. the current Offline GeoStack README
8. sibling project READMEs only when deeper manufacturing/history is needed

## Governing principle

> **Put the finished capability where the user actually touches it.**
