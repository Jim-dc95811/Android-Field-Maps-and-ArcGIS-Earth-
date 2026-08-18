# Android Field Maps + ArcGIS Earth

## Offline maps on personal Android phones

**This repository is where the other three projects get deployed to normal field users.**

The manufacturing side can be complicated. The operator side should not be.

```text
Offline GeoStack / TPKX Map Factory
        ↓
finished TPKX maps
        ↓
microSD card
        ↓
Android phone
        ↓
ArcGIS Field Maps or ArcGIS Earth
        ↓
local imagery + GPS with no cellular basemap requirement
```

The practical goal is simple:

> **Put the maps on the card before you need them. Turn map-app cellular data off. The imagery is already in your pocket.**

---

## Why this project exists

Many field users already have ArcGIS Field Maps on personal Android phones but use only a small part of its capability. They do not want to become GIS technicians, install QGIS, learn projections, or manufacture their own tile pyramids.

They want to look down at the woods and roads from an aerial perspective, see where they are, and have the screen keep working when cellular service is weak, absent, expensive, or simply turned off.

This project deliberately separates the roles:

### Map maker

Uses the Factory and GIS tools to manufacture, verify, refresh, and load map products.

### Field user

Gets a prepared microSD card and a one-page cheat sheet.

That is the deployment model.

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

## The field handoff

For a normal user, the intended procedure is deliberately short:

```text
1. Get a prepared card.
2. Put it in the phone.
3. Open Field Maps.
4. Select the local basemap.
5. Set Field Maps to Wi-Fi only.
6. Turn Wi-Fi off and prove the local imagery still pans and zooms.
```

See [Field Maps SD-Card Quick Guide](FIELD_MAPS_SD_CARD_QUICK_GUIDE.md).

---

## Relationship to the other projects

### [Offline GeoStack](https://github.com/Jim-dc95811/Offline-GeoStack)

Master field-mapping and TPKX manufacturing project. QGIS manufactures raster MBTiles; the proven converter packages those tiles into native TPKX.

### [Rasta Pyramid Factory](https://github.com/Jim-dc95811/Rasta-Pyramid-Factory)

Turns giant flat images and georeferenced rasters into smooth multiscale pyramids. It can provide useful reference imagery and deep-zoom visual material in addition to ordinary map products.

### [Map Fountain](https://github.com/Jim-dc95811/Map-Fountain)

Proved that ArcGIS Earth on Windows can open a production-scale native TPKX directly from router-attached storage over SMB/Wi-Fi, and separately proved router-only Static REST WMTS delivery to ArcGIS Earth Mobile. It is now **proven engineering reference / parked from the primary personal-phone deployment path**. It may return as a Starlink-connected basecamp storage/NAS package.

### This repository

**Deployment to the human.**

The other projects make and prove the machinery. This one keeps the final user experience simple.

---

## Governing rules

- No operational dependence on public Internet for the map itself.
- Do not make ordinary users learn the Factory.
- Local files outrank streaming when the same useful imagery can already be on the phone.
- Do not fill cards with features merely because GIS software supports them.
- Add overlays or GIS extras only when real field users demonstrate a need.
- Preserve exact map/source/zoom/build information so card contents can be reproduced and refreshed.
- Respect all third-party imagery, basemap, attribution, caching, export, and redistribution terms.
- The real target application decides acceptance.

---

# The simple version

> **Call Gaddy for a card. Read the cheat sheet. Go to work.**

If you want to know how the maps are manufactured, follow the links above and have a drink from the firehose.
