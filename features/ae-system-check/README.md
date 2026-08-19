# AE SYSTEM CHECK

## A synthetic TPKX that tells you whether the map gear is behaving

**Current status: ✅ LIVE-PROVEN — WINDOWS ARCGIS EARTH**

This is a deliberately artificial ArcGIS Earth diagnostic map intended to ride on the same SD card as the real field maps.

Its first job is simple:

> **Before blaming the imagery, prove the viewer, storage, package, and zoom ladder are working correctly.**

The map contains no operational geography and is marked **TEST ONLY — NOT NAVIGATION**.

---

## Live acceptance — 2026-08-18

The exact v0.1.0 binary was opened on the real Windows ArcGIS Earth target.

The operator verified that **every intended level, Z16 through Z20, rendered correctly**.

Observed ladder:

```text
Z16 = RED      PASS
Z17 = BLUE     PASS
Z18 = GREEN    PASS
Z19 = ORANGE   PASS
Z20 = PURPLE   PASS
```

The Z16 parent rendered as the intended single red calibration panel. At the opposite end of the ladder, Z20 rendered the expected 16 × 16 purple child grid with ordered row/column identities visible across the screen. The operator subsequently confirmed the intermediate Z17, Z18, and Z19 levels also work.

This promotes the exact Windows ArcGIS Earth specimen from **BUILT / SELF-TESTED** to **LIVE-PROVEN**.

Separate deployment gates remain separate: ArcGIS Earth Mobile, microSD behavior, and network-hosted use can be tested with this same specimen without changing the Windows evidence state.

---

## Exact accepted package

```text
AE_SYSTEM_CHECK_v0_1_0.tpkx
4,196,743 bytes
SHA-256 7843afedb94fdc3654be9eadd1c8d18d14bd2c70abd3d5a1d88f5278c1776390
```

**Freeze rule:** do not silently rebuild a different file under this version name. The accepted hash above is the v0.1.0 Windows LIVE-PROVEN specimen.

---

## Why it exists

Normal imagery is a poor diagnostic instrument. If ArcGIS Earth resamples a parent tile, delays a child tile, crosses a bundle boundary, serves stale cached material, or loads the wrong level, ordinary aerial imagery can make the change hard to identify by eye.

AE SYSTEM CHECK makes the renderer identify itself.

```text
Z16 = RED
Z17 = BLUE
Z18 = GREEN
Z19 = ORANGE
Z20 = PURPLE
```

Every tile also contains:

- a heavy intentional tile boundary;
- `AE SYSTEM CHECK`;
- the exact zoom level;
- row / column identity inside that level;
- XYZ tile coordinates;
- center crosshairs and concentric rings;
- high-frequency black/white bars and checker patterns for blur/resampling inspection;
- `TEST ONLY — NOT NAVIGATION`.

If the display changes from green to orange, there is no argument about which source level is on screen.

---

## Mathematical layout

v0.1.0 uses exactly **one complete Web Mercator Z16 tile** as its footprint in synthetic test space near 30°N, 80°W.

That one tile subdivides cleanly through Z20:

```text
Z16     1 tile      1 × 1
Z17     4 tiles     2 × 2
Z18    16 tiles     4 × 4
Z19    64 tiles     8 × 8
Z20   256 tiles    16 × 16
-------------------------
TOTAL 341 tiles
```

This is intentional. There are no guessed partial-parent relationships in the calibration ladder.

Bounds:

```text
West  -80.002441406250
South  29.997759725579
East  -79.996948242188
North  30.002516938571
```

The location is synthetic display space, not an operational destination.

---

## Internal self-test

The specimen was manufactured as raster MBTiles, then converted with the project's proven raster MBTiles → Esri Compact Cache V2 / TPKX converter.

Self-test verified:

- exact MBTiles level counts: `1 / 4 / 16 / 64 / 256`;
- PNG raster format;
- TPKX ZIP CRC integrity;
- required `root.json`, `iteminfo.json`, and `thumbnail.png`;
- `minLOD=16`, `maxLOD=20`;
- Compact Cache V2 with packet size 128;
- exactly five represented Compact Cache bundles;
- exact non-zero bundle-index counts for all five levels;
- **all 341 PNG tile byte hashes matched between the MBTiles source and the finished Compact Cache V2 bundles**.

The self-test proved the calibration artwork survived the package bridge byte-for-byte. The live Windows run then proved ArcGIS Earth actually consumed and rendered that ladder correctly.

---

## Field / SD-card use

Recommended card lineup:

```text
AE SYSTEM CHECK
District map
County map
State Forest / high-value maps
Specialty / Rasta products as useful
```

Suggested operator check:

1. Open **AE SYSTEM CHECK** first.
2. Zoom to the layer.
3. Confirm the Z16 red panel appears.
4. Zoom inward deliberately.
5. Watch the level colors progress RED → BLUE → GREEN → ORANGE → PURPLE.
6. Check that tile rows/columns are present, ordered, and not blank.
7. Look at borders, rings, fine bars, and checker patterns for unexpected blur/resampling.
8. Pan across tile boundaries.
9. If SYSTEM CHECK behaves normally but a real imagery package does not, investigate the imagery/package before blaming the device.

The same specimen is intended for comparison across:

- ArcGIS Earth Windows — **LIVE-PROVEN**;
- ArcGIS Earth Mobile — separate acceptance pending;
- internal storage;
- microSD / removable storage — separate acceptance pending;
- network-hosted TPKX when that path is being tested.

---

## What it can diagnose

This map is designed to make otherwise subtle behavior obvious:

- level-of-detail transitions;
- parent/child substitution;
- missing or misaddressed tiles;
- tile-order errors;
- bundle-boundary problems;
- stale-cache suspicion;
- local-storage versus network-storage differences;
- unexpected image resampling or blur;
- viewer/device problems versus a bad real-world map package.

It is not a benchmark of geographic accuracy because it deliberately contains no operational geography.

---

## Where the idea came from

This is a modern ArcGIS Earth reincarnation of an older project laboratory technique.

During the Google Earth / Network Earth experiments, conspicuous color-coded and labeled spatial cells were manufactured so the viewer could not hide which mathematical region or level it was actually displaying.

The old laboratory trick now has a practical user job:

> **Keep a known-good synthetic map on the card and make the gear prove itself before the mission map gets blamed.**

The larger engineering pattern is recorded in Offline GeoStack's **The Bridges We Had to Build**.

---

# Acceptance statement

**AE SYSTEM CHECK v0.1.0 is LIVE-PROVEN on Windows ArcGIS Earth for the complete Z16–Z20 synthetic calibration ladder.**
