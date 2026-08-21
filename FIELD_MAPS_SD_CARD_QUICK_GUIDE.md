# ArcGIS Field Maps — Offline District Map Card Quick Guide

**Android + physical microSD — local imagery without burning cellular data**

> **Goal:** Stop rationing the map. Keep the district imagery on the card so Field Maps does not need to stream the heavy basemap over cellular service.

## Current status — read this first

The physical-card Field Maps path is now **LIVE-PROVEN**.

Using the same Field Maps Designer map and same card folder:

```text
project historical converter TPKX -> REJECTED
Esri official Usa.tpkx            -> ACCEPTED
```

So the current engineering problem is the project's TPKX converter output, not the SD-card directory.

The next test is a small TPKX built with `ESRI_CANONICAL_TPKX_TEST_v0_2_0`. Do not regenerate the district-scale products until that tiny specimen passes Field Maps.

See:

- [Field Maps TPKX Conformance — 2026-08-20](docs/FIELD_MAPS_TPKX_CONFORMANCE_2026-08-20.md)

## 1. Prepare the card on a computer

Use a physical microSD formatted **exFAT**.

Create:

```text
\Android\data\com.esri.fieldmaps\files\basemaps
```

For MMPKs later, also create:

```text
\Android\data\com.esri.fieldmaps\files\mappackages
```

### If Windows chimes but the card does not appear

If Disk Management already shows the card as a healthy exFAT partition, do **not** format or initialize it just because no drive letter appears.

Use:

```text
Disk Management
-> find the SD card's exFAT Healthy primary partition
-> right-click
-> Change Drive Letter and Paths...
-> Add
-> accept an available drive letter
-> OK
```

### Reader warning

The laptop's built-in SD reader produced write-protection behavior on multiple cards/adapters. Another computer wrote successfully.

Treat that reader as suspect. The card itself is disposable test media.

## 2. Proven Field Maps basemap setup

In Field Maps Designer:

1. create/open the map;
2. enable Offline;
3. choose **File on the device** for the basemap;
4. enter the **exact filename** that exists in the card `basemaps` folder;
5. save;
6. share the map as required.

The project proved this workflow with `District 7 Local Basemap Test`, shared **Everyone (public)**.

Esri's official `Usa.tpkx` worked from the physical card.

## 3. Current canonical-converter test

Run:

```text
small MBTiles
-> ESRI_CANONICAL_TPKX_TEST_v0_2_0
-> small new TPKX
```

Copy that output to:

```text
\Android\data\com.esri.fieldmaps\files\basemaps\
```

Set Designer to the exact filename and open Field Maps.

### Pass

If Field Maps opens the new TPKX, the canonical converter design can replace the historical converter in production branches.

### Fail

Do not guess at one metadata field. Continue package-wide conformance analysis against Esri's working `Usa.tpkx`.

## 4. District card after converter repair

Once the corrected district TPKX exists, the intended card layout is:

```text
\Android\data\com.esri.fieldmaps\files\mappackages\DISTRICT.mmpk
\Android\data\com.esri.fieldmaps\files\basemaps\DISTRICT.tpkx
```

The duplication is intentional.

- MMPK = complete on-device Field Maps map.
- TPKX = separate local basemap path / redundancy and direct ArcGIS Earth Mobile content.
- Source MBTiles stays on the manufacturing side.

## 5. Why the old district MMPK is held

ArcGIS Pro 3.7 successfully created small and approximately 52 GB district MMPKs.

But Pro preserved the original TPKX intact inside the MMPK under `commondata/new_tpkx/`.

Therefore the MMPK does **not** repair the current TPKX conformance defect. Rebuild the district MMPK after the corrected TPKX is proven.

## 6. Protect the personal cellular plan

Use the Android app-level network restriction and set **ArcGIS Field Maps = Wi-Fi only** where the phone supports it.

Typical Samsung path:

```text
Settings
-> Connections
-> Data usage
-> Allowed networks for apps
-> ArcGIS Field Maps
-> Wi-Fi only
```

Normal phone service can remain available for calls and texts while the heavy map stays local.

## 7. Full gold offline proof — after corrected district package exists

1. insert the prepared card;
2. open Field Maps;
3. verify the corrected district MMPK appears under **On Device**;
4. open it and verify district imagery/labels;
5. pan/zoom through Z17;
6. remove public Internet;
7. repeat pan/zoom;
8. close Field Maps completely;
9. reopen while still disconnected;
10. verify the map remains available;
11. later repeat on a GPS-capable personal Android phone and verify own position.

## Official Esri references

- [Sideload MMPKs and basemaps using Android / microSD](https://support.esri.com/en-us/knowledge-base/sideload-mobile-map-packages-mmpks-and-basemaps-to-arcg-000026920)
- [Create Mobile Map Package — ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-mobile-map-package.htm)
- [Mobile map package sharing — ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/help/sharing/overview/mobile-map-package.htm)
- [BUG-000164200 — use Android settings to block Field Maps cellular traffic](https://support.esri.com/en-us/bug/turning-off-the-cellular-data-option-in-the-arcgis-fiel-bug-000164200)

---

**Current field rule:** Esri's TPKX works from the card. Fix our package to conform, prove the tiny file, then scale back up.
