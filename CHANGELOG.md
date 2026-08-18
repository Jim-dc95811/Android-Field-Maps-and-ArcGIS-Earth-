# Android Field Maps + ArcGIS Earth — Changelog

## 2026-08-18 — deployment repository defined

- Defined this repository as the deployment endpoint for the Offline GeoStack / Rasta / Map Fountain project family.
- Established the personal-Android-phone / microSD-card direction.
- Added the current card-menu concept:
  - district Z17;
  - county Z18;
  - selected State Forest / high-value Z20 areas;
  - Google Hybrid and Esri imagery/labels where useful.
- Added the lean Field Maps SD-card quick guide.
- Recorded Esri's documented Android/microSD TPKX sideload path.
- Preserved evidence discipline: Field Maps TPKX support is vendor-documented, but this project's own Field Maps microSD acceptance test is still pending.
- Added the Android app-level Wi-Fi-only rule to protect personal cellular data plans.
- Repositioned Map Fountain as proven engineering reference / parked from the primary personal-phone deployment path, with possible future Starlink/basecamp NAS use.

## Project origin

This deployment branch grew out of three preceding projects:

1. Offline GeoStack proved repeatable QGIS → MBTiles → native TPKX manufacturing.
2. Rasta Pyramid Factory generalized the pyramid machinery to giant rasters and deep-zoom imagery.
3. Map Fountain proved remote native TPKX access over SMB on Windows and router-only Static REST WMTS delivery to ArcGIS Earth Mobile.

The deployment lesson was simpler than the machinery:

> **Most field users do not want the factory. They want the filled card.**
