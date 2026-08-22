# Android Field Maps + ArcGIS Earth

## Android offline maps + Windows ArcGIS Earth field features

**This repository is the deployment-to-the-user end of the four-project family.**

> **Stop rationing the map. Keep cellular data for communication. Put the heavy district imagery on the card.**

---

## User feature 1 — District offline map card

### Current mission

A Field Maps user must be able to open the app with **zero public Internet** and use a **district-wide Esri Hybrid map through Z17**. The same local imagery should prevent large basemap downloads when cellular service exists but the user does not want to burn data.

Two-app model:

```text
ArcGIS Field Maps   -> agency workflow / on-device map
ArcGIS Earth Mobile -> fast direct local TPKX viewer
```

ArcGIS Earth Mobile local project TPKX remains **LIVE-PROVEN on multiple packages**.

---

## Current Field Maps manufacturing path — 2026-08-21

The custom MBTiles -> TPKX converter is no longer the Field Maps production gate.

Strict target evidence:

```text
historical project TPKX -> Field Maps REJECTED
canonical v0.3.1 TPKX  -> Field Maps REJECTED
Esri official Usa.tpkx  -> Field Maps ACCEPTED
```

The current production chain is now:

```text
QGIS / GeoTIFF Factory
-> finished labeled GeoTIFF
-> ArcGIS Pro Create Map Tile Package
-> native TPKX
-> physical removable storage
-> Field Maps
```

This keeps the map rendering under QGIS and gives native TPKX package construction back to ArcGIS Pro.

---

## LIVE-PROVEN Field Maps pieces

- `District 7 Local Basemap Test` created in Field Maps Designer;
- Offline enabled;
- **File on the device** selected;
- map shared **Everyone (public)**;
- physical-card basemap path works:

```text
\Android\data\com.esri.fieldmaps\files\basemaps\
```

- Esri official `Usa.tpkx` works from that path.

Field Maps is therefore the final acceptance test, not the manufacturing tool.

See:

- [Field Maps TPKX Conformance](docs/FIELD_MAPS_TPKX_CONFORMANCE_2026-08-20.md)
- [Offline GeoStack current status](https://github.com/Jim-dc95811/Offline-GeoStack/blob/main/docs/PROJECT_STATUS_2026-08-21.md)
- [QGIS GeoTIFF workflow](https://github.com/Jim-dc95811/Offline-GeoStack/blob/main/docs/QGIS_GEOTIFF_SOURCE_WORKFLOW_2026-08-21.md)
- [ArcGIS Pro native TPKX workflow](https://github.com/Jim-dc95811/Offline-GeoStack/blob/main/docs/ARCGIS_PRO_GEOTIFF_TO_TPKX_2026-08-21.md)

---

## Small native ArcGIS Pro package — build proven

A labeled QGIS GeoTIFF was successfully converted with ArcGIS Pro **Create Map Tile Package**.

```text
QGIS GeoTIFF
37,767,543 bytes
4096 x 3072 RGB
EPSG:3857
Z18 source detail

-> ArcGIS Pro

tiff test 66.tpkx
38,306,245 bytes
Z0-Z18
PNG24
19 bundles
creator: CreateMapTilePackage ArcGIS Pro
```

The native Pro TPKX build is proven. Field Maps runtime acceptance of this native-Pro branch is still **PENDING** until the real app opens it.

---

## District 7 current branch

A full District 7 Esri Satellite + Google Labels GeoTIFF build was started at:

```text
Z17
map units per pixel = 1.19432856685505
```

Status: **LIVE BUILD STARTED — COMPLETION PENDING.**

After it finishes:

```text
District 7 Z17 GeoTIFF
-> ArcGIS Pro native Z0-Z17 TPKX
-> physical card basemaps folder
-> Designer exact filename
-> Field Maps
```

---

## GeoTIFF Factory

Offline GeoStack has built a separate:

```text
GEOTIFF FACTORY 0.1.2 TEST
```

Its scope is intentionally simple:

- standard two-point extent workflow;
- four controlled map sources;
- target detail Z16-Z20;
- one finished GeoTIFF;
- no MBTiles;
- no custom TPKX converter.

Status: **BUILT / BENCH-CHECKED — WINDOWS/QGIS LIVE TEST PENDING.**

---

## Physical-card rule

Earlier Fire testing proved Android scoped storage blocks ordinary ADB/MTP-style injection into another app's protected `Android/data` directory.

Populate the physical removable storage on a computer while it is outside Android, then insert the completed media into the device.

The laptop's built-in SD reader previously showed suspect write-protection behavior; another computer wrote successfully. Treat that reader as suspect, not the card as precious media.

---

## Cellular-data protection

The user value is not merely offline operation. It is eliminating **map rationing**.

Where Android supports it, restrict ArcGIS Field Maps to Wi-Fi only at the app/network level while normal cellular service remains available for calls/texts and other communication.

---

## Custom converter disposition

The custom converter is preserved as research/backlog for a possible future Pro-free workflow.

v0.3.1:

```text
bench structural/tile tests -> PASS
Field Maps -> FAIL
```

A v0.3.2 PNG-metadata experiment exists, but it is not the active production gate.

A real ArcGIS Pro-generated raster TPKX is now the preferred future converter reference specimen.

---

## User feature 2 — PRAVE Live

### [Remote radio units in Windows ArcGIS Earth](features/prave-live/README.md)

**Status: ✅ LIVE-PROVEN**

```text
PRAVE radio reports
-> Windows serial input
-> PRAVE Live
-> ArcGIS Earth local Automation API
-> labeled remote units + RSSI fire-truck icons
```

ArcGIS Earth native GNSS owns ME / own-position. PRAVE Live owns remote PRAVE units.

---

## User feature 3 — QR Command Bridge

### [Optical dispatch + approved local commands](features/qr-command-bridge/README.md)

**Status: ✅ LIVE-PROVEN FOUNDATION / 🟡 COMMAND EXPANSION DESIGNED**

Hard rule:

> **QR text is data, never executable shell text.**

---

## User feature 4 — Wildland Imagery University

### [Teaching terrain judgment before the emergency](training/WILDLAND_IMAGERY_UNIVERSITY.md)

**Status: 🟡 TRAINING CONCEPT / PROJECT-DEVELOPED MATERIAL**

Core model:

```text
SEE -> THINK -> DECIDE
```

---

## User feature 5 — AE SYSTEM CHECK

### [Prove the viewer and storage before blaming the real map](features/ae-system-check/README.md)

**Status: ✅ LIVE-PROVEN — WINDOWS ARCGIS EARTH**

Exact historical accepted binary:

```text
AE_SYSTEM_CHECK_v0_1_0.tpkx
4,196,743 bytes
SHA-256 7843afedb94fdc3654be9eadd1c8d18d14bd2c70abd3d5a1d88f5278c1776390
```

Field Maps compatibility is a separate claim.

---

## Evidence discipline

| Capability | Status |
| --- | --- |
| Field Maps Designer + physical `basemaps` path | ✅ LIVE-PROVEN |
| Esri official `Usa.tpkx` in Field Maps | ✅ LIVE-PROVEN |
| Historical project converter TPKX in Field Maps | ❌ FAILED |
| Canonical v0.3.1 converter TPKX in Field Maps | ❌ FAILED |
| QGIS labeled GeoTIFF small build | ✅ LIVE-PROVEN |
| ArcGIS Pro GeoTIFF -> native TPKX build | ✅ PASS |
| Native ArcGIS Pro TPKX in Field Maps | 🟡 PENDING |
| GeoTIFF Factory 0.1.2 TEST | 🟡 BUILT / BENCH-CHECKED |
| District 7 Z17 GeoTIFF | 🟡 LIVE BUILD STARTED |
| ArcGIS Earth Mobile local project TPKX | ✅ LIVE-PROVEN |
| Fire scoped-storage ADB/MTP injection | ❌ REJECTED |
| PRAVE Live -> ArcGIS Earth | ✅ LIVE-PROVEN |
| AE SYSTEM CHECK v0.1.0 — Windows Earth | ✅ LIVE-PROVEN |

---

## Governing rules

- No operational dependence on public Internet for the prepared map itself.
- Do not make ordinary users learn the manufacturing stack.
- Reliability outranks storage elegance.
- Use the native vendor packaging path for production when available.
- Field Maps decides Field Maps compatibility.

---

# The simple version

> **QGIS makes the map image. ArcGIS Pro makes the native TPKX. Put it on the card and let Field Maps vote.**
