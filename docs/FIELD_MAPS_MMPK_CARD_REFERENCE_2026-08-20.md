# Field Maps + ArcGIS Earth Mobile — District Map Card Reference

**Current checkpoint: 2026-08-20**

> **STOP RATIONING THE MAP. Keep cellular data for communication. Put the heavy district imagery on the card.**

## Mission

A Field Maps user must be able to open the app with **zero public Internet** and immediately use a **district-wide Esri Hybrid map through Z17**. The same locally stored map should also prevent large basemap downloads when cellular service exists but the user does not want to burn data.

ArcGIS Earth Mobile remains the companion local-map viewer. Local TPKX on ArcGIS Earth Mobile is already **LIVE-PROVEN on multiple project packages**.

## Current gold-card architecture

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

- The **MMPK** is the complete on-device Field Maps map.
- The separate **TPKX** remains available as a sideloaded local basemap path.
- Storage efficiency ranks below field reliability.
- The source MBTiles is a manufacturing/master artifact and is not needed on this field card test.

## Gold-test hardware checkpoint

- physical **128 GB microSD**;
- Windows reports approximately **119 GB usable**;
- filesystem: **exFAT**;
- district TPKX: approximately **52 GB**;
- district MMPK: approximately **52 GB**;
- combined field payload: approximately **104 GB** plus filesystem overhead;
- first target: **Amazon Fire tablet** for map-path acceptance;
- GPS/own-position acceptance remains a later test on a GPS-capable Android phone.

## What ArcGIS Pro proved on 2026-08-20

Minimal supported workflow:

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
- modern Pro-created MMPK reports **version 3.0**;
- the small package contained only **7 files**;
- ArcGIS Pro preserved the original TPKX intact under `commondata/new_tpkx/`;
- Pro did **not** rebuild the raster pyramid into the old Yellowstone-style mobile geodatabase structure;
- the small specimen `.mmap` referenced the packaged local TPKX directly;
- no HTTP/HTTPS URLs were found in the small specimen `.mmap` or `.mapx`;
- the Pro-created MMPK opened and rendered in Windows ArcGIS Earth while Earth showed **Not signed in**;
- ArcGIS Pro also successfully created the district-wide approximately 52 GB MMPK from the existing approximately 52 GB TPKX.

Small specimen shape:

```text
MMPK_SMALL_TEST.mmpk
|
+-- commondata/new_tpkx/<original .tpkx>
+-- p20/MMPK_SMALL_TEST.mmap
+-- p20/MMPK_SMALL_TEST.mapx
+-- esriinfo/item.pkinfo
+-- esriinfo/iteminfo.xml
+-- esriinfo/thumbnail/thumbnail.png
+-- MMPK_SMALL_TEST.info
```

## Connectivity / authorization distinction

**File validity and user authorization are separate questions.**

Esri documents sideloading MMPKs and basemaps to Android/microSD and does not document a separate Internet activation or pre-exposure step that makes the local file itself valid.

The remaining real-target question is whether the standard Pro-created MMPK opens in Field Maps under the desired disconnected/sign-in state. Do not alter licensing metadata or attempt to bypass a control. Let the real Field Maps application decide acceptance.

## Why the physical card matters

Earlier Fire testing proved that Android scoped storage blocks ordinary ADB/MTP-style injection into another app's protected `Android/data` tree. Esri's documented physical-card sideload method avoids that barrier: populate the card on the computer while it is outside Android, then insert the prepared card into the device.

## Gold acceptance sequence

1. Finish both large-file copies to the physical microSD.
2. Verify the MMPK and TPKX are present in the two exact directories above.
3. Safely eject the card from Windows and insert it into the Fire.
4. Let Android mount the card and open ArcGIS Field Maps.
5. Go to **On Device**.
6. Confirm the district MMPK appears as a complete local map.
7. Open it and verify district-wide imagery/labels, pan, and zoom through Z17.
8. Remove public Internet and repeat pan/zoom.
9. Close Field Maps completely, reopen while still disconnected, and verify the map remains available.
10. After the Fire map-path passes, repeat on a GPS-capable personal Android phone and verify own position.
11. For the cell-data use case, keep normal cellular service available but restrict Field Maps to Wi-Fi only at the Android app level; verify the local map continues to work while calls/texts remain available.

## Evidence state

| Capability | Status |
| --- | --- |
| ArcGIS Earth Mobile local TPKX | ✅ **LIVE-PROVEN on multiple project packages** |
| ArcGIS Pro existing TPKX -> minimal MMPK | ✅ **PASS — small and district-scale packages created** |
| Pro-created MMPK in Windows ArcGIS Earth | ✅ **PASS — rendered while Earth showed Not signed in** |
| Field Maps MMPK on physical microSD | 🟡 **VENDOR-DOCUMENTED / PROJECT LIVE TEST PENDING** |
| Field Maps standalone TPKX basemap on physical microSD | 🟡 **VENDOR-DOCUMENTED / PROJECT LIVE TEST PENDING** |
| Fire scoped-storage ADB/MTP injection | ❌ **REJECTED / proven permission barrier** |
| Map Fountain | ✅ **LIVE-PROVEN / PARKED reference** |

## User-facing vision

> **Field Maps for agency workflow. ArcGIS Earth Mobile for fast local maps. The district imagery already lives on the card.**

The selling proposition is not merely "offline maps." It is freedom from **map rationing**: pan, zoom, explore, and keep cellular data for communications instead of repeatedly streaming a giant basemap.

## Official Esri references

- Field Maps sideloading MMPKs and basemaps on Android/microSD: https://support.esri.com/en-us/knowledge-base/sideload-mobile-map-packages-mmpks-and-basemaps-to-arcg-000026920
- ArcGIS Pro Create Mobile Map Package: https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-mobile-map-package.htm
- ArcGIS Pro mobile map package sharing: https://pro.arcgis.com/en/pro-app/latest/help/sharing/overview/mobile-map-package.htm
- ArcGIS Earth Mobile local files/offline content: https://doc.arcgis.com/en/arcgis-earth/mobile/browse-2d-and-3d-contents.htm

## Governing rule

> **The real target decides acceptance. Do not promote Field Maps behavior until the Fire/phone actually passes the cold disconnected test.**
