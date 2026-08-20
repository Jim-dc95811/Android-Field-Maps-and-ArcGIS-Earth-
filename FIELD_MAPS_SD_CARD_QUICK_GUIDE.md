# ArcGIS Field Maps — Offline District Map Card Quick Guide

**Android + physical microSD — local imagery without burning cellular data**

> **Goal:** Stop rationing the map. Keep the district imagery on the card so Field Maps does not need to stream the heavy basemap over cellular service.

## 1. Prepare the card on a computer

Use a physical microSD formatted **exFAT**.

Create these two directories on the card:

```text
\Android\data\com.esri.fieldmaps\files\mappackages
```

```text
\Android\data\com.esri.fieldmaps\files\basemaps
```

Copy the prepared files:

```text
mappackages\DISTRICT.mmpk
basemaps\DISTRICT.tpkx
```

The duplication is intentional for the current gold test.

- `DISTRICT.mmpk` = complete on-device Field Maps map.
- `DISTRICT.tpkx` = separately available local basemap path / redundancy.
- The source MBTiles file is not required on the field card.

Esri documents the MMPK folder as `mappackages` and sideloaded TPK/TPKX/VTPK basemaps under `basemaps`.

## 2. Insert the prepared card

1. Safely eject the card from Windows.
2. Insert it into the Android device.
3. Let Android mount the card.
4. Open ArcGIS Field Maps.
5. Go to **On Device**.
6. Open the district MMPK if it appears.

For the current project, **Field Maps MMPK-on-microSD behavior is still awaiting live project acceptance**. Do not promote it until the real device passes.

## 3. Protect the personal cellular plan

The Field Maps in-app Cellular Data option is not treated as a complete app-level network block.

Use the Android app-level network restriction and set **ArcGIS Field Maps = Wi-Fi only** where the phone supports that control.

Typical Samsung path:

```text
Settings
-> Connections
-> Data usage
-> Allowed networks for apps
-> ArcGIS Field Maps
-> Wi-Fi only
```

Menu wording varies by Android manufacturer/version.

Normal phone service can remain available for calls and texts while the local map stays on the card.

## 4. Gold offline proof

1. Confirm the district MMPK appears under **On Device**.
2. Open it and verify district-wide imagery/labels.
3. Pan and zoom through the intended level, currently district Z17.
4. Remove public Internet.
5. Repeat pan/zoom.
6. Close Field Maps completely.
7. Reopen it while still disconnected.
8. Confirm the district map remains available.

After the map-path passes on the Fire test device, repeat on a GPS-capable personal Android phone and verify own-position behavior.

## 5. Current Pro packaging result

ArcGIS Pro 3.7 successfully created a modern minimal MMPK from an existing project TPKX.

Observed small-package behavior:

- analyzer: **0 errors / 0 warnings / 0 messages**;
- MMPK version 3.0;
- original TPKX preserved intact inside the MMPK;
- no HTTP/HTTPS references found in the small specimen `.mmap` / `.mapx`;
- Pro-created MMPK rendered in Windows ArcGIS Earth while Earth showed **Not signed in**;
- district-scale approximately 52 GB MMPK also packaged successfully from the approximately 52 GB district TPKX.

See the current engineering reference:

- [Field Maps + ArcGIS Earth Mobile — District Map Card Reference](docs/FIELD_MAPS_MMPK_CARD_REFERENCE_2026-08-20.md)

## Official Esri references

- [Sideload MMPKs and basemaps using Android / microSD](https://support.esri.com/en-us/knowledge-base/sideload-mobile-map-packages-mmpks-and-basemaps-to-arcg-000026920)
- [Create Mobile Map Package — ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-mobile-map-package.htm)
- [Mobile map package sharing — ArcGIS Pro](https://pro.arcgis.com/en/pro-app/latest/help/sharing/overview/mobile-map-package.htm)
- [BUG-000164200 — use Android settings to block Field Maps cellular traffic](https://support.esri.com/en-us/bug/turning-off-the-cellular-data-option-in-the-arcgis-fiel-bug-000164200)

---

**Field procedure:** prepared card in -> Field Maps On Device -> district MMPK -> Field Maps Wi-Fi only -> map keeps working without cellular basemap downloads.
