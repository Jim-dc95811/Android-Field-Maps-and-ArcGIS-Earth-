# Android Field Maps + ArcGIS Earth

## Android offline maps + Windows ArcGIS Earth field features

**This repository is the deployment-to-the-user end of the four-project family.**

> **The manufacturing side can be complicated. The operator side should not be.**

> **Stop rationing the map. Keep cellular data for communication. Put the heavy district imagery on the card.**

---

## User feature 1 — District offline map card

### Current mission

A Field Maps user must be able to open the app with **zero public Internet** and use a **district-wide Esri Hybrid map through Z17**. The same local imagery should prevent large basemap downloads when cellular service exists but the user does not want to burn data.

The intended two-app model remains:

```text
ArcGIS Field Maps   -> agency workflow / on-device map
ArcGIS Earth Mobile -> fast direct local TPKX viewer
```

ArcGIS Earth Mobile local TPKX is already **LIVE-PROVEN on multiple project packages**.

### New decisive Field Maps result — 2026-08-20

The physical-card Field Maps path is now proven.

Using the same microSD directory and same Field Maps Designer workflow:

```text
project converter-built TPKX -> REJECTED
Esri official Usa.tpkx       -> ACCEPTED
```

Field Maps found the project-built District 7 TPKX but rejected it as spatial-reference incompatible. Esri's official `Usa.tpkx` worked after Designer was pointed to that exact filename.

That isolates the current defect to the project's historical MBTiles -> TPKX package construction.

### LIVE-PROVEN Field Maps pieces

- `District 7 Local Basemap Test` created in Field Maps Designer;
- Offline enabled;
- **File on the device** selected;
- map shared **Everyone (public)**;
- physical-card path works:

```text
\Android\data\com.esri.fieldmaps\files\basemaps\
```

- Esri official `Usa.tpkx` works in Field Maps.

See:

- **[Field Maps TPKX Conformance — Live Test 2026-08-20](docs/FIELD_MAPS_TPKX_CONFORMANCE_2026-08-20.md)**
- [Offline GeoStack TPKX engineering record](https://github.com/Jim-dc95811/Offline-GeoStack/blob/main/docs/TPKX_FIELD_MAPS_CONFORMANCE_2026-08-20.md)

### Immediate acceptance gate

The next test is intentionally small:

```text
small MBTiles
-> ESRI_CANONICAL_TPKX_TEST_v0_2_0
-> small new TPKX
-> physical microSD basemaps folder
-> Designer exact filename
-> Field Maps
```

The canonical v0.2.0 test converter is **BUILT / SELF-TESTED**. Field Maps acceptance is pending.

If it passes, the corrected converter is integrated into the manufacturing projects, then the District 7 TPKX and MMPK are rebuilt.

### MMPK bridge — useful, but currently held behind TPKX repair

ArcGIS Pro 3.7 successfully created a small modern MMPK and an approximately 52 GB district MMPK from existing project TPKX files.

Observed small-package result:

- 0 errors / 0 warnings / 0 messages;
- MMPK version 3.0;
- original TPKX preserved intact under `commondata/new_tpkx/`;
- `.mmap` references the packaged local TPKX;
- no HTTP/HTTPS references found in the small `.mmap` or `.mapx`;
- package rendered in Windows ArcGIS Earth while Earth showed **Not signed in**.

That proves the ArcGIS Pro packaging bridge. It also proves Pro is **not** a sanitizer: it preserves the source TPKX. Therefore the old district MMPK is not the next gold object until the underlying TPKX is corrected.

### Intended gold-card architecture after repair

```text
Prepared microSD (exFAT)
|
+-- Android\data\com.esri.fieldmaps\files\mappackages\
|     corrected District 7 MMPK.mmpk
|
+-- Android\data\com.esri.fieldmaps\files\basemaps\
      corrected District 7.tpkx
```

The duplication remains intentional. Reliability outranks storage elegance.

### Physical-card rule

Earlier Fire testing proved Android scoped storage blocks ordinary ADB/MTP-style injection into another app's protected `Android/data` directory.

Populate the physical microSD on a computer while it is outside Android, then insert the completed card into the device.

### SD-reader note

The laptop's built-in SD reader showed write-protection behavior with multiple cards/adapters. Another computer wrote successfully. Treat that reader as suspect.

The card itself is disposable test media; rewrite/reformat it whenever useful.

### Protect the personal cellular plan

The key selling point is not merely offline operation. It is eliminating **map rationing**.

Where Android supports it, restrict ArcGIS Field Maps to Wi-Fi only at the app/network level while normal phone cellular service remains available for calls/texts and other communication.

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

Exact accepted binary:

```text
AE_SYSTEM_CHECK_v0_1_0.tpkx
4,196,743 bytes
SHA-256 7843afedb94fdc3654be9eadd1c8d18d14bd2c70abd3d5a1d88f5278c1776390
```

---

## Evidence discipline

| Capability | Status |
| --- | --- |
| Field Maps Designer + physical `basemaps` path | ✅ **LIVE-PROVEN** |
| Esri official `Usa.tpkx` in Field Maps | ✅ **LIVE-PROVEN** |
| Project historical converter TPKX in Field Maps | ❌ **FAILED / NEEDS REPAIR** |
| Canonical converter v0.2.0 test | 🟡 **BUILT / SELF-TESTED — FIELD MAPS PENDING** |
| ArcGIS Earth Mobile local project TPKX | ✅ **LIVE-PROVEN** |
| ArcGIS Pro existing TPKX -> MMPK | ✅ **PASS** |
| Corrected district MMPK cold-card test | 🟡 **PENDING CORRECTED TPKX** |
| Fire scoped-storage ADB/MTP injection | ❌ **REJECTED / proven permission barrier** |
| PRAVE Live -> ArcGIS Earth | ✅ **LIVE-PROVEN** |
| QR camera / SMS JSON / coordinate lineage | ✅ **LIVE-PROVEN lineage** |
| AE SYSTEM CHECK v0.1.0 — Windows Earth | ✅ **LIVE-PROVEN Z16-Z20** |

The real target decides acceptance.

---

## Four-project family

1. **[Offline GeoStack](https://github.com/Jim-dc95811/Offline-GeoStack)** — master manufacturing/integration and current TPKX conformance repair.
2. **[Rasta Pyramid Factory](https://github.com/Jim-dc95811/Rasta-Pyramid-Factory)** — giant-raster manufacturing; TPKX branch inherits the converter repair boundary.
3. **[Map Fountain](https://github.com/Jim-dc95811/Map-Fountain)** — LIVE-PROVEN shared-storage/network reference; parked from normal personal-phone use.
4. **Android Field Maps + ArcGIS Earth** — deployment to the user and the real Field Maps acceptance record.

---

## Governing rules

- No operational dependence on public Internet for the prepared map itself.
- Do not make ordinary users learn the Factory.
- Local files outrank streaming when the useful geography can live on the device.
- Reliability outranks storage elegance.
- Esri's working TPKX is the reference implementation.
- Field Maps decides Field Maps compatibility.

---

# The simple version

> **Field Maps for workflow. ArcGIS Earth Mobile for fast local maps. Fix the package once, then put the district imagery on the card.**
