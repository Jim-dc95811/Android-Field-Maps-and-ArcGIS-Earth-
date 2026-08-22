# ArcGIS Field Maps TPKX Conformance — Live Record 2026-08-20 to 2026-08-21

## Proven physical-card workflow

The Field Maps deployment path itself is proven:

```text
same Android device
same physical removable storage
same Field Maps Designer map
same basemaps directory
```

Known result:

```text
Esri official Usa.tpkx -> ACCEPTED
```

Field Maps Designer state proved:

- `District 7 Local Basemap Test` exists;
- Offline enabled;
- **File on the device** selected;
- map shared **Everyone (public)**;
- physical-card path works:

```text
\Android\data\com.esri.fieldmaps\files\basemaps\
```

---

## Custom package results

### Historical converter

```text
project converter TPKX -> REJECTED
```

Field Maps reported spatial-reference incompatibility.

### Canonical v0.3.1

The custom converter was heavily tightened and passed its local structural/tile audit, including byte-for-byte preservation of all 174 bench tiles.

Real Field Maps result:

```text
canonical v0.3.1 TPKX -> REJECTED
```

Therefore the custom converter remains **nonconformant for Field Maps** despite strong local package checks.

A v0.3.2 PNG metadata experiment exists, but the project did not make that experiment the next production gate.

---

## Production pivot

The deployment path now uses the vendor-native TPKX writer:

```text
QGIS / GeoTIFF Factory
-> finished labeled GeoTIFF
-> ArcGIS Pro Create Map Tile Package
-> native TPKX
-> physical card
-> Field Maps
```

This preserves QGIS as the rendering engine while ArcGIS Pro owns the TPKX package format.

---

## Small native ArcGIS Pro build proof

QGIS source:

```text
GeoTIFF
37,767,543 bytes
4096 x 3072 RGB
EPSG:3857
Z18 source detail
```

ArcGIS Pro output:

```text
tiff test 66.tpkx
38,306,245 bytes
Z0-Z18
PNG24
19 Compact Cache V2 bundles
creator: CreateMapTilePackage ArcGIS Pro
```

The native-Pro TPKX build is proven.

Field Maps runtime result for the native-Pro path is still:

**PENDING.**

Do not call it Field Maps LIVE-PROVEN until the real app opens it from the device-basemap workflow.

---

## District 7 next acceptance

A District 7 Esri Satellite + Google Labels GeoTIFF build was started at:

```text
Z17
map units per pixel = 1.19432856685505
```

After the GeoTIFF completes:

```text
District 7 GeoTIFF
-> ArcGIS Pro Create Map Tile Package Z0-Z17
-> copy native TPKX to basemaps folder
-> Designer exact filename
-> Field Maps
```

That is the next full district acceptance path.

---

## GeoTIFF Factory

`GEOTIFF FACTORY 0.1.2 TEST` has been built to automate the QGIS side with the established two-point extent workflow and Z16-Z20 detail choices.

Status:

**BUILT / BENCH-CHECKED — LIVE WINDOWS/QGIS TEST PENDING.**

It outputs only GeoTIFF and contains no custom TPKX converter.

---

## Evidence matrix

| Capability | Status |
| --- | --- |
| Field Maps Designer + File on the device | ✅ LIVE-PROVEN |
| Physical `basemaps` path | ✅ LIVE-PROVEN |
| Esri official `Usa.tpkx` in Field Maps | ✅ LIVE-PROVEN |
| Historical custom TPKX in Field Maps | ❌ FAILED |
| Canonical v0.3.1 custom TPKX in Field Maps | ❌ FAILED |
| QGIS labeled GeoTIFF build | ✅ LIVE-PROVEN |
| ArcGIS Pro GeoTIFF -> native TPKX build | ✅ PASS |
| ArcGIS Pro native TPKX in Field Maps | 🟡 PENDING |
| GeoTIFF Factory 0.1.2 TEST | 🟡 BUILT / BENCH-CHECKED |
| District 7 Z17 GeoTIFF | 🟡 LIVE BUILD STARTED |

## Governing rule

> **For production, let ArcGIS Pro write the native TPKX and let Field Maps make the final compatibility decision.**
