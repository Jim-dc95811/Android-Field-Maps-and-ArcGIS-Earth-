# Field Maps + ArcGIS Earth Mobile — District Map Card Reference

**Current checkpoint: late 2026-08-20**

> **STOP RATIONING THE MAP. Keep cellular data for communication. Put the heavy district imagery on the card.**

## Mission

A Field Maps user must be able to open the app with **zero public Internet** and immediately use a **district-wide Esri Hybrid map through Z17**. The same local map should prevent large basemap downloads when cellular service exists but the user does not want to burn data.

ArcGIS Earth Mobile remains the companion local-map viewer. Local project TPKX is already **LIVE-PROVEN on multiple ArcGIS Earth Mobile packages**.

---

## New controlling evidence — Field Maps TPKX path is proven

The same physical microSD `basemaps` folder and same Field Maps Designer map produced two different outcomes:

```text
project converter-built District 7 TPKX -> REJECTED
Esri official Usa.tpkx                  -> ACCEPTED
```

Field Maps reported the project-built package as spatial-reference incompatible.

Esri's official `Usa.tpkx` worked after Designer was pointed at the exact filename.

### What this proves

- Field Maps Designer configuration works;
- Offline + File on the device workflow works;
- public sharing of the test map works;
- physical microSD `basemaps` path works;
- Field Maps can consume a proper Esri TPKX through this workflow;
- the historical project converter output is the current defect.

See [Field Maps TPKX Conformance — 2026-08-20](FIELD_MAPS_TPKX_CONFORMANCE_2026-08-20.md).

---

## Current immediate test

Before rebuilding any large district product:

```text
small raster MBTiles
-> ESRI_CANONICAL_TPKX_TEST_v0_2_0
-> small new TPKX
-> physical microSD basemaps folder
-> Designer exact filename
-> Field Maps
```

The canonical v0.2.0 branch is **BUILT / SELF-TESTED**. Field Maps acceptance is pending.

If it passes, integrate the corrected converter, regenerate the district TPKX, and then rebuild the MMPK.

---

## ArcGIS Pro MMPK result — still valid, but not a repair mechanism

Minimal workflow previously proven:

```text
New Basemap
-> Add existing TPKX
-> Share
-> Mobile Map
-> Save package to file
-> Analyze
-> Package
```

Observed results:

- small specimen analyzer: **0 errors / 0 warnings / 0 messages**;
- MMPK version **3.0**;
- seven outer files;
- ArcGIS Pro preserved the original TPKX intact under `commondata/new_tpkx/`;
- `.mmap` referenced the packaged local TPKX directly;
- no HTTP/HTTPS URLs found in the small `.mmap` or `.mapx`;
- Pro-created MMPK rendered in Windows ArcGIS Earth while Earth showed **Not signed in**;
- approximately 52 GB district MMPK also packaged successfully from the approximately 52 GB district TPKX.

### Updated interpretation

Because Pro preserves the source TPKX intact, the existing district MMPK carries the same converter lineage that Field Maps rejected in the standalone TPKX control.

Therefore the current approximately 52 GB MMPK is **not** the next gold acceptance object. Rebuild it after the corrected district TPKX exists.

---

## Intended gold-card architecture after repair

```text
Prepared microSD (exFAT)
|
+-- Android\data\com.esri.fieldmaps\files\mappackages\
|     corrected District 7 ESRIHybrid Zoom 17 MMPK.mmpk
|
+-- Android\data\com.esri.fieldmaps\files\basemaps\
      corrected District 7 ESRIHybrid Zoom 17.tpkx
```

The duplication remains intentional.

- **MMPK** = complete on-device Field Maps map.
- **TPKX** = separate local basemap path and direct ArcGIS Earth Mobile content.
- Storage efficiency ranks below field reliability.
- Source MBTiles remains a manufacturing/master artifact.

---

## Hardware checkpoint

- physical 128 GB microSD;
- Windows reports approximately 119 GB usable;
- exFAT;
- historical district TPKX approximately 52 GB;
- historical district MMPK approximately 52 GB;
- these large files are evidence/test artifacts, not precious media;
- regenerate them after the small canonical conformance pass.

## Windows card mount recovery

If Windows detects the SD card but File Explorer does not show it and Disk Management shows a Healthy exFAT partition:

```text
Disk Management
-> right-click the SD partition
-> Change Drive Letter and Paths...
-> Add
-> accept an available drive letter
-> OK
```

Do not format or initialize a Healthy exFAT card merely because Windows did not assign a letter.

### Reader warning

The laptop's built-in SD reader produced apparent write-protection behavior on multiple cards/adapters. Another computer wrote successfully. Treat the reader as suspect.

---

## Why physical card remains the correct transport

Earlier Fire testing proved Android scoped storage blocks ordinary ADB/MTP-style injection into another app's protected `Android/data` tree.

Esri's documented physical-card sideload method avoids that barrier: populate the card on a computer while it is outside Android, then insert the completed card into the device.

---

## Full gold acceptance sequence — after converter repair

1. regenerate corrected district TPKX;
2. create new MMPK from the corrected TPKX in ArcGIS Pro;
3. populate the physical card in the two exact directories;
4. safely eject and insert the card into the Fire;
5. open Field Maps and go to **On Device**;
6. confirm the corrected district MMPK appears;
7. open and verify district imagery/labels through Z17;
8. remove public Internet and repeat pan/zoom;
9. close/reopen Field Maps while still disconnected;
10. later repeat on a GPS-capable personal Android phone and verify own position;
11. keep normal cellular service available but restrict Field Maps to Wi-Fi only where supported and verify the local map remains usable.

---

## Evidence state

| Capability | Status |
| --- | --- |
| Field Maps Designer + `basemaps` physical-card path | ✅ **LIVE-PROVEN** |
| Esri official `Usa.tpkx` in Field Maps | ✅ **LIVE-PROVEN** |
| Historical project converter TPKX in Field Maps | ❌ **FAILED / NEEDS REPAIR** |
| Canonical converter v0.2.0 | 🟡 **BUILT / SELF-TESTED — FIELD MAPS PENDING** |
| ArcGIS Earth Mobile local project TPKX | ✅ **LIVE-PROVEN on multiple packages** |
| ArcGIS Pro existing TPKX -> MMPK | ✅ **PASS** |
| Historical district MMPK | 🟡 **PACKAGED; HELD BEHIND TPKX REPAIR** |
| Corrected district TPKX/MMPK cold card | 🟡 **PENDING** |
| Fire protected-folder ADB/MTP injection | ❌ **REJECTED / proven permission barrier** |
| Map Fountain | ✅ **LIVE-PROVEN / PARKED reference** |

---

## User-facing vision

> **Field Maps for agency workflow. ArcGIS Earth Mobile for fast local maps. The district imagery already lives on the card.**

The selling proposition remains freedom from **map rationing**.

## Governing rule

> **Esri's working TPKX is the reference. Field Maps is the judge. Prove the tiny package before scaling back up.**
