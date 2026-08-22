# Android Field Maps + ArcGIS Earth — Changelog

## 2026-08-21 — production pivot to QGIS GeoTIFF -> ArcGIS Pro native TPKX

Field Maps rejected the custom canonical v0.3.1 TPKX even after its local structural/tile audit passed.

Target evidence now reads:

```text
historical project TPKX -> REJECTED
canonical v0.3.1 TPKX  -> REJECTED
Esri official Usa.tpkx  -> ACCEPTED
```

### Production decision

The deployment branch no longer waits on the custom MBTiles -> TPKX converter.

Current chain:

```text
QGIS / GeoTIFF Factory
-> finished labeled GeoTIFF
-> ArcGIS Pro Create Map Tile Package
-> native TPKX
-> physical card
-> Field Maps
```

### Small GeoTIFF + ArcGIS Pro build proof

QGIS produced a labeled hybrid GeoTIFF:

```text
37,767,543 bytes
4096 x 3072 RGB
EPSG:3857
Z18 source detail
```

Critical live rule: Google Labels must render above ESRI Satellite.

ArcGIS Pro then produced:

```text
tiff test 66.tpkx
38,306,245 bytes
Z0-Z18
PNG24
19 Compact Cache V2 bundles
creator: CreateMapTilePackage ArcGIS Pro
```

The native-Pro TPKX build is proven; Field Maps runtime acceptance is pending.

### GeoTIFF Factory

Offline GeoStack created `GEOTIFF FACTORY 0.1.2 TEST` as a separate product with:

- the established two-point extent workflow;
- four controlled map sources;
- Z16-Z20 source detail;
- one `.tif` output;
- no MBTiles;
- no custom TPKX converter.

Status: BUILT / BENCH-CHECKED — live Windows/QGIS test pending.

### District 7

A full District 7 Z17 Esri Satellite + Google Labels GeoTIFF build was started with map units per pixel `1.19432856685505`.

Completion and final size remain pending.

---

## 2026-08-20 — Field Maps physical-card path LIVE-PROVEN; project TPKX converter failure isolated

A decisive control test was completed on the real Field Maps path.

### Field Maps Designer workflow proven

- Created `District 7 Local Basemap Test`.
- Enabled Offline.
- Selected **File on the device**.
- Shared the map **Everyone (public)**.
- Used the physical-card basemap directory:

```text
\Android\data\com.esri.fieldmaps\files\basemaps\
```

### Control result

The project converter-built District 7 Esri Hybrid Z17 TPKX was found by Field Maps but rejected as spatial-reference incompatible.

Esri's official `Usa.tpkx` was copied into the same directory and Designer was changed to reference its exact filename.

**Result: `Usa.tpkx` opened successfully in Field Maps.**

This proves the physical-card path, Field Maps Designer configuration, public web map, and general Web Mercator map setup are good. The current failure is isolated to the project's historical MBTiles -> TPKX package construction.

### Existing project TPKX evidence preserved

The converter lineage remains proven to open in ArcGIS Earth Windows, ArcGIS Earth Mobile on multiple packages, and ArcGIS Pro.

The correct status is therefore:

**Earth-compatible / Field Maps nonconformant until repaired.**

### MMPK consequence

ArcGIS Pro 3.7 previously proved the MMPK bridge, but it preserves the original TPKX intact inside the MMPK.

Therefore the approximately 52 GB district MMPK built from the old converter lineage is held behind the TPKX repair. It is not treated as a sanitizer or next gold acceptance object.

### Canonical repair branch

Offline GeoStack created `ESRI_CANONICAL_TPKX_TEST_v0_2_0`.

It copies Esri's canonical Web Mercator LOD values and native metadata conventions. Bench/package tests passed; Field Maps acceptance is pending.

Immediate next gate:

```text
small MBTiles -> canonical v0.2.0 TPKX -> physical card -> Field Maps
```

Added:

- `docs/FIELD_MAPS_TPKX_CONFORMANCE_2026-08-20.md`

---

## 2026-08-20 — ArcGIS Pro MMPK bridge proven; district physical-card gold test prepared

- Installed and activated ArcGIS Pro 3.7 trial.
- Created a new basemap and added an existing project TPKX directly.
- Used **Share -> Mobile Map -> Save package to file**.
- Small specimen analyzer returned **0 errors / 0 warnings / 0 messages**.
- ArcGIS Pro successfully produced `MMPK_SMALL_TEST.mmpk`.
- Forensic inspection showed:
  - MMPK version 3.0;
  - seven outer files;
  - original TPKX preserved intact under `commondata/new_tpkx/`;
  - local `.mmap` / `.mapx` wiring with no HTTP/HTTPS references found.
- The Pro-created MMPK opened and rendered in Windows ArcGIS Earth while Earth showed **Not signed in**.
- Repeated the workflow with the approximately 52 GB district TPKX and successfully created a matching approximately 52 GB MMPK.
- Selected a physical 128 GB exFAT microSD.
- The duplicate MMPK + TPKX card concept was retained because reliability outranks storage elegance.

Later the same day, the direct Field Maps control test above showed that the source TPKX lineage itself needs conformance repair before the district MMPK becomes a valid gold-runtime candidate.

---

## 2026-08-18 — AE SYSTEM CHECK v0.1.0 LIVE-PROVEN on Windows ArcGIS Earth

- Opened the exact `AE_SYSTEM_CHECK_v0_1_0.tpkx` specimen on the real Windows ArcGIS Earth target.
- Verified Z16, Z17, Z18, Z19, and Z20 render correctly.
- Exact accepted binary: 4,196,743 bytes; SHA-256 `7843afedb94fdc3654be9eadd1c8d18d14bd2c70abd3d5a1d88f5278c1776390`.
- Mobile/Field Maps compatibility remains a separate acceptance claim.

## 2026-08-18 — Wildland Imagery University added

- Added the training branch and preserved the **SEE -> THINK -> DECIDE** model.
- Kept fieldcraft, agency policy, reconnaissance, current conditions, and qualified on-scene judgment above remote imagery.

## 2026-08-18 — QR Command Bridge expanded

- Added URL QR Maker v0.1.0.
- Preserved FireTextSender origin and QR Gold lineage.
- Preserved security rule: **QR text is data, never executable code.**

## 2026-08-18 — PRAVE Live added

- Added PRAVE Live as a LIVE-PROVEN ArcGIS Earth field feature.
- Preserved the exact original package lineage.
- Kept role separation: native GNSS = ME; PRAVE Live = remote units.

## 2026-08-18 — deployment repository defined

- Established the personal Android / physical microSD direction.
- Added card-menu concept: district Z17, county Z18, selected State Forest/high-value Z20.
- Protecting personal cellular data became a first-class deployment requirement.
- Repositioned Map Fountain as proven reference / parked from normal personal-phone deployment.

## Project origin

1. Offline GeoStack — map manufacturing + ArcGIS Earth integration.
2. Rasta Pyramid Factory — giant-raster/deep-zoom manufacturing.
3. Map Fountain — shared-storage/network delivery proofs.
4. This repository — the real user/deployment endpoint.

> **Put the finished capability where the user actually touches it, and let that real application decide acceptance.**
