# Android Field Maps + ArcGIS Earth

## Offline maps + ArcGIS Earth field features

**This repository is where the other three projects get deployed to normal field users.**

**[Download the one-page printable Field Maps Offline TPKX Quick Guide](Field_Maps_Offline_TPKX_Quick_Guide.pdf)**

The manufacturing side can be complicated. The operator side should not be.

```text
Offline Map Factory
        ↓
finished TPKX maps
        ↓
microSD / local storage
        ↓
ArcGIS Field Maps or ArcGIS Earth
        ↓
local geography + field position
```

The practical goal is simple:

> **Put the maps where the user needs them before showtime, then add only the live field features that earn their place.**

---

## User features

### Offline TPKX on Android

Prepared TPKX maps can be carried on local phone storage / microSD for ArcGIS Field Maps and ArcGIS Earth Mobile.

- ArcGIS Earth Mobile local TPKX: **LIVE-PROVEN on multiple project packages**.
- ArcGIS Field Maps TPKX on microSD: **DOCUMENTED BY VENDOR / PROJECT LIVE TEST PENDING**.
- Personal-data protection: set Field Maps to **Wi-Fi only** at the Android app level.

### [PRAVE Live — remote units in ArcGIS Earth](features/prave-live/README.md)

**LIVE-PROVEN.** On Windows ArcGIS Earth, PRAVE Live takes the established `$PRAVE` radio position reports and places remote units directly into ArcGIS Earth through the local Automation API.

```text
PRAVE radio reports
→ serial input
→ PRAVE Live
→ ArcGIS Earth
→ labeled remote units + RSSI fire-truck icons
```

ArcGIS Earth native GNSS continues to own the operator's own-position blue dot. PRAVE Live owns the remote units.

The preserved original package is published in the feature folder.

### [QR Command Bridge — optical dispatch + approved commands](features/qr-command-bridge/README.md)

**LIVE-PROVEN FOUNDATION / COMMAND EXPANSION DESIGNED.** The QR branch uses a phone screen or printed QR as a deliberately narrow optical input to the Windows field computer.

```text
phone / QR card
→ Windows camera
→ QR decoder
→ strict parser / hard-coded allowlist
→ dispatch result or approved local action
```

The Gold lineage already proved camera decode, MacroDroid SMS JSON, coordinate parsing, normal message display, `GMDS_CMD:TEST`, and blocking of unknown command tokens.

The modern ArcGIS Earth API and Windows command actions are the next branch. They remain **DESIGNED until individually implemented and live-tested**.

Hard rule: **QR text is data, never executable shell text.**

---

## Why this project exists

Many field users already have ArcGIS Field Maps or ArcGIS Earth but use only a small part of their capability. They do not want to become GIS technicians, install QGIS, learn projections, or manufacture their own tile pyramids.

They want to look down at useful geography, see where they are, and have the screen keep working when cellular service is weak, absent, expensive, or simply turned off.

This repository also owns optional user-facing ArcGIS Earth / Windows features such as PRAVE Live and QR Command Bridge when they belong at the deployment-to-the-human end of the system.

This project deliberately separates the roles:

### Map maker

Uses Offline Map Factory and GIS tools to manufacture, verify, refresh, and load map products.

### Field user

Gets prepared geography and a short procedure. Optional live features are added only when the field role needs them.

---

## Current map-card concept

The exact sizes are being measured with real Factory builds before capacity tiers are frozen.

Current menu direction:

- **District — Z17**: broad everyday operating-area imagery.
- **County — Z18**: wider-area coverage with more detail.
- **State Forests / selected high-value areas — Z20**: maximum local detail where it matters most.
- **Google Hybrid and Esri imagery/labels**: both are useful choices when card capacity allows.
- **Rasta Pyramid Factory products**: optional deep-zoom imagery or other large single-raster pyramids can use spare card capacity.

Do not guess storage requirements from theory alone. Finished byte counts from real builds decide the card menu.

---

## ArcGIS Field Maps — documented Android TPKX path

Esri documents direct sideloading of `.tpk`, `.tpkx`, `.vtpk`, and geospatial PDF basemaps to Android storage or a microSD card.

Android basemap folder:

```text
\Android\data\com.esri.fieldmaps\files\basemaps
```

Official references:

- [ArcGIS Field Maps — Configure the mobile app / Copy a basemap](https://doc.arcgis.com/en/field-maps/android/use-maps/configure-field-maps.htm)
- [ArcGIS Field Maps — Download maps](https://doc.arcgis.com/en/field-maps/android/use-maps/download-maps.htm)
- [Esri Support — Sideload MMPKs and basemaps using Android / microSD](https://support.esri.com/en-us/knowledge-base/sideload-mobile-map-packages-mmpks-and-basemaps-to-arcg-000026920)

### Evidence status

- Esri documentation for Android/microSD TPKX sideloading: **DOCUMENTED BY VENDOR**.
- This project's own TPKX → ArcGIS Field Maps Android acceptance run: **PENDING LIVE TEST**.
- Local TPKX → ArcGIS Earth Mobile: **LIVE-PROVEN on multiple project packages**.

Do not promote the Field Maps path to LIVE-PROVEN until the real phone test passes.

---

## Protect the personal cellular data plan

The point is not merely that a local map *can* work offline. The user should be able to prevent Field Maps from silently using a personal cellular data plan for imagery and other network activity.

Esri states that the **Cellular Data** setting inside Field Maps does not block every cellular-data use by the app. To block Field Maps cellular traffic entirely on Android, use the phone's app-level network setting and set ArcGIS Field Maps to **Wi-Fi only**.

Typical Samsung/Android path:

```text
Settings
→ Connections
→ Data usage
→ Allowed networks for apps
→ ArcGIS Field Maps
→ Wi-Fi only
```

Menu names vary by manufacturer/version.

Official Esri support record:

- [BUG-000164200 — Field Maps cellular-data behavior and Android Wi-Fi-only workaround](https://support.esri.com/en-us/bug/turning-off-the-cellular-data-option-in-the-arcgis-fiel-bug-000164200)

This lets normal phone service remain available while the map app is prevented from consuming the user's cellular data plan.

---

## The Field Maps handoff

For a normal Field Maps user, the intended procedure is deliberately short:

```text
1. Get a prepared card.
2. Put it in the phone.
3. Open Field Maps.
4. Select the local basemap.
5. Set Field Maps to Wi-Fi only.
6. Turn Wi-Fi off and prove the local imagery still pans and zooms.
```

- [Read the Markdown quick guide](FIELD_MAPS_SD_CARD_QUICK_GUIDE.md)
- [Download the one-page printable PDF](Field_Maps_Offline_TPKX_Quick_Guide.pdf)

---

## Relationship to the other projects

### [Offline GeoStack](https://github.com/Jim-dc95811/Offline-GeoStack)

Master field-mapping and map-manufacturing project. QGIS manufactures raster MBTiles; the proven converter packages those tiles into native TPKX. It also retains the deeper engineering record for PRAVE → ArcGIS Earth integration.

### [Rasta Pyramid Factory](https://github.com/Jim-dc95811/Rasta-Pyramid-Factory)

Turns giant flat images and georeferenced rasters into smooth multiscale pyramids. It can provide useful reference imagery and deep-zoom visual material in addition to ordinary map products.

### [Map Fountain](https://github.com/Jim-dc95811/Map-Fountain)

Proved that ArcGIS Earth on Windows can open a production-scale native TPKX directly from router-attached storage over SMB/Wi-Fi, and separately proved router-only Static REST WMTS delivery to ArcGIS Earth Mobile. It is now **proven engineering reference / parked from the primary personal-phone deployment path**. It may return as a Starlink-connected basecamp storage/NAS package.

### This repository

**Deployment to the human.**

The other projects make and prove the machinery. This one presents the finished user workflows and live ArcGIS Earth / Windows features.

---

## Governing rules

- No operational dependence on public Internet for the map itself.
- Do not make ordinary users learn the Factory.
- Local files outrank streaming when the same useful imagery can already be on the device.
- Do not fill cards or screens with features merely because GIS software supports them.
- Add live overlays or GIS extras only when real field users demonstrate a need.
- QR command inputs must remain explicit allowlisted data, never arbitrary executable text.
- Preserve exact source/zoom/build and feature-package information so deployments can be reproduced.
- Respect all third-party imagery, basemap, attribution, caching, export, and redistribution terms.
- The real target application decides acceptance.

---

# The simple version

> **Prepared geography. Own position. Live field units and deliberate commands when needed. Go to work.**

If you want to know how the maps are manufactured, follow the links above and have a drink from the firehose.
