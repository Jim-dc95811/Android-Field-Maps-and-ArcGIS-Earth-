# Android Field Maps + ArcGIS Earth

## Android offline maps + Windows ArcGIS Earth field features

**This repository is the deployment-to-the-user end of the four-project family.**

It owns the simple human-facing workflows: prepared local maps on Android, optional Windows ArcGIS Earth features such as PRAVE Live and QR Command Bridge, a standard AE System Check diagnostic map, and imagery-based terrain training.

**Keywords:** ArcGIS Field Maps, ArcGIS Earth, MMPK, TPKX, microSD, offline Android maps, cellular-data protection, map rationing, offline GIS, GNSS, PRAVE, QR code, wildland fire, terrain training

> **The manufacturing side can be complicated. The operator side should not be.**

> **Stop rationing the map. Keep cellular data for communication. Put the heavy district imagery on the card.**

---

## User feature 1 — District offline map card

### Current mission

A Field Maps user must be able to open the app with **zero public Internet** and immediately use a **district-wide Esri Hybrid map through Z17**. The same locally stored map should also prevent large basemap downloads when cellular service exists but the user does not want to burn data.

The current user-facing model is deliberately two-app:

```text
ArcGIS Field Maps   -> agency workflow / on-device district map
ArcGIS Earth Mobile -> fast local map viewer / direct TPKX
```

ArcGIS Earth Mobile local TPKX is already **LIVE-PROVEN on multiple project packages**.

### Current gold-card architecture

```text
Prepared microSD (exFAT)
|
+-- Android\data\com.esri.fieldmaps\files\mappackages\
|     District 7 ESRIHybrid Zoom 17 MMPK.mmpk
|
+-- Android\data\com.esri.fieldmaps\files\basemaps\
      Grid 1 Master zoom 17.tpkx
```

The duplication is intentional.

- **MMPK** = complete on-device Field Maps map.
- **TPKX** = separately available local basemap path and redundancy.
- Storage efficiency ranks below field reliability.
- The source MBTiles stays on the manufacturing side and is not required on the field card.

Current gold-test hardware checkpoint:

- physical **128 GB microSD**;
- exFAT;
- approximately **52 GB district TPKX**;
- approximately **52 GB district MMPK**;
- first target: **Amazon Fire tablet** for map-path acceptance;
- GPS/own-position remains a separate later phone acceptance test.

### ArcGIS Pro MMPK breakthrough — 2026-08-20

ArcGIS Pro 3.7 successfully created a minimal modern MMPK from an existing project TPKX using:

```text
New Basemap
-> Add existing TPKX
-> Share
-> Mobile Map
-> Save package to file
-> Analyze
-> Package
```

Observed small-package result:

- **0 errors / 0 warnings / 0 messages**;
- MMPK version 3.0;
- only seven files in the outer MMPK;
- original TPKX preserved intact under `commondata/new_tpkx/`;
- `.mmap` references the packaged local TPKX;
- no HTTP/HTTPS references found in the small specimen `.mmap` or `.mapx`;
- Pro-created MMPK opened and rendered in Windows ArcGIS Earth while Earth showed **Not signed in**.

ArcGIS Pro then successfully created the **district-scale approximately 52 GB MMPK** from the existing approximately 52 GB TPKX.

This proves the manufacturing bridge. **Field Maps on-device acceptance remains pending until the real Fire/phone passes.**

### Physical-card rule

Earlier Fire testing proved Android scoped storage blocks ordinary ADB/MTP-style injection into another app's protected `Android/data` directory. The current path follows Esri's documented physical-card sideload model: populate the card on a computer while it is outside Android, then insert the completed card into the device.

### Protect the personal cellular plan

The key selling point is not merely offline operation. It is eliminating **map rationing**.

A user should be able to keep normal cellular service available for calls and texts while Field Maps reads the heavy geography locally. Where Android supports it, set **ArcGIS Field Maps = Wi-Fi only** at the app/network level so the map app cannot consume the personal cellular plan.

### Current Field Maps acceptance gate

1. insert the prepared physical microSD;
2. open Field Maps;
3. go to **On Device**;
4. confirm the district MMPK appears;
5. open it and pan/zoom through Z17;
6. remove public Internet and repeat;
7. close/reopen Field Maps while still disconnected;
8. repeat later on a GPS-capable personal Android phone and verify own position;
9. verify the cell-data use case with Field Maps restricted to Wi-Fi only while normal phone service remains available.

Do not promote Field Maps behavior until the real device passes.

- **[Current Field Maps + Earth Mobile card reference](docs/FIELD_MAPS_MMPK_CARD_REFERENCE_2026-08-20.md)**
- [Current Markdown card quick guide](FIELD_MAPS_SD_CARD_QUICK_GUIDE.md)
- [Historical one-page TPKX-only PDF guide](Field_Maps_Offline_TPKX_Quick_Guide.pdf)

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

Role separation remains intentional:

```text
ArcGIS Earth native GNSS -> ME / own-position blue dot
PRAVE Live               -> remote PRAVE units
```

The exact original live-proven package is preserved in the feature folder. The deeper parser/API engineering record remains in Offline GeoStack.

---

## User feature 3 — QR Command Bridge

### [Optical dispatch + approved local commands](features/qr-command-bridge/README.md)

**Status: ✅ LIVE-PROVEN FOUNDATION / 🟡 COMMAND EXPANSION DESIGNED**

The Gold lineage proves camera QR decode, MacroDroid SMS JSON, coordinate/message parsing, strict `GMDS_CMD:<TOKEN>` allowlisting, `GMDS_CMD:TEST`, and unknown-command blocking.

Hard rule:

> **QR text is data, never executable shell text.**

ArcGIS Earth API actions and Windows restart/shutdown/helper-process actions remain DESIGNED until individually implemented and live-tested.

---

## User feature 4 — Wildland Imagery University

### [Teaching terrain judgment before the emergency](training/WILDLAND_IMAGERY_UNIVERSITY.md)

**Status: 🟡 TRAINING CONCEPT / PROJECT-DEVELOPED MATERIAL**

Core model:

```text
SEE -> THINK -> DECIDE
```

The training branch teaches terrain/access interpretation from imagery while keeping fieldcraft, local knowledge, agency policy, reconnaissance, current conditions, and qualified on-scene judgment above remote imagery.

---

## User feature 5 — AE SYSTEM CHECK

### [Prove the viewer and storage before blaming the real map](features/ae-system-check/README.md)

**Status: ✅ LIVE-PROVEN — WINDOWS ARCGIS EARTH**

`AE_SYSTEM_CHECK_v0_1_0.tpkx` is the tiny synthetic Z16-Z20 diagnostic ladder intended to prove viewer/storage behavior before blaming a production map.

Exact accepted binary:

```text
AE_SYSTEM_CHECK_v0_1_0.tpkx
4,196,743 bytes
SHA-256 7843afedb94fdc3654be9eadd1c8d18d14bd2c70abd3d5a1d88f5278c1776390
```

Windows ArcGIS Earth is LIVE-PROVEN. Mobile/microSD/network-hosted use remain separate acceptance paths.

---

## Evidence discipline

| Capability | Status |
| --- | --- |
| ArcGIS Earth Mobile local TPKX | ✅ **LIVE-PROVEN** |
| ArcGIS Pro existing TPKX -> minimal MMPK | ✅ **PASS — small and district-scale packages created** |
| Pro-created MMPK in Windows ArcGIS Earth | ✅ **PASS — rendered while Earth showed Not signed in** |
| Field Maps MMPK on physical microSD | 🟡 **VENDOR-DOCUMENTED / PROJECT LIVE TEST PENDING** |
| Field Maps standalone TPKX basemap on physical microSD | 🟡 **VENDOR-DOCUMENTED / PROJECT LIVE TEST PENDING** |
| Fire scoped-storage ADB/MTP injection | ❌ **REJECTED / proven permission barrier** |
| PRAVE Live -> ArcGIS Earth | ✅ **LIVE-PROVEN** |
| QR camera / SMS JSON / coordinate lineage | ✅ **LIVE-PROVEN lineage** |
| AE SYSTEM CHECK v0.1.0 — Windows ArcGIS Earth | ✅ **LIVE-PROVEN Z16-Z20** |

The real target decides acceptance.

---

## Four-project family

1. **[Offline GeoStack](https://github.com/Jim-dc95811/Offline-GeoStack)** — master map manufacturing + field-system integration.
2. **[Rasta Pyramid Factory](https://github.com/Jim-dc95811/Rasta-Pyramid-Factory)** — giant-raster / deep-zoom pyramid manufacturing.
3. **[Map Fountain](https://github.com/Jim-dc95811/Map-Fountain)** — LIVE-PROVEN shared-storage/network delivery evidence; parked from the normal personal-phone path.
4. **Android Field Maps + ArcGIS Earth** — deployment to the user: local Android maps + Windows ArcGIS Earth field features + imagery training.

---

## Governing rules

- No operational dependence on public Internet for the prepared map itself.
- Do not make ordinary users learn the Factory.
- Local files outrank streaming when the useful geography can already live on the device.
- Reliability outranks storage elegance; duplicate the TPKX if that makes Field Maps deployment more robust.
- Preserve exact package/source/zoom/build identities so deployments can be reproduced.
- Respect third-party imagery, basemap, attribution, caching, export, and redistribution terms.
- The real target application decides acceptance.

---

# The simple version

> **Field Maps for workflow. ArcGIS Earth Mobile for fast local maps. The district imagery already lives on the card.**
