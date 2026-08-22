# Android Field Maps + ArcGIS Earth — Roadmap

## Current mission

Deploy finished local map products and proven ArcGIS Earth / Windows field features to the user with the least possible operator complexity.

For personal Android maps, the preferred path remains prepared local removable storage, not a field server.

The user value remains cellular-data protection and freedom from map rationing.

---

## Immediate gate — native ArcGIS Pro TPKX in Field Maps

The custom converter is no longer the deployment gate.

Target evidence:

```text
historical project TPKX -> Field Maps REJECTED
canonical v0.3.1 TPKX  -> Field Maps REJECTED
Esri official Usa.tpkx  -> Field Maps ACCEPTED
```

Current manufacturing path:

```text
QGIS / GeoTIFF Factory
-> finished GeoTIFF
-> ArcGIS Pro Create Map Tile Package
-> native TPKX
-> physical card
-> Field Maps
```

### Next real acceptance

1. finish the District 7 Z17 GeoTIFF;
2. create the native Z0-Z17 TPKX in ArcGIS Pro;
3. copy it to `\Android\data\com.esri.fieldmaps\files\basemaps\`;
4. point Designer to the exact filename;
5. open the map in Field Maps;
6. record the real result.

Do not make custom converter research block this sequence.

---

## District 7 current run

Current source build:

```text
Esri Satellite + Google Labels
Z17
map units per pixel = 1.19432856685505
```

Status: **LIVE BUILD STARTED — COMPLETION PENDING.**

After completion, ArcGIS Pro should use:

```text
Tiling Format = PNG 24 bit
Minimum LOD = 0
Maximum LOD = 17
Extent = GeoTIFF layer extent
```

---

## GeoTIFF Factory acceptance

`GEOTIFF FACTORY 0.1.2 TEST` is built and bench-checked.

Next live test should verify a small controlled extent on the real Windows/QGIS machine after the current large manual build finishes.

Pass condition:

- BAT launches;
- QGIS 3.44.9 is found;
- two-point extent works;
- chosen Z16-Z20 resolution is correct;
- selected source/layer stack is correct;
- one finished GeoTIFF is produced;
- hybrid labels are visible;
- ArcGIS Pro accepts the TIFF normally.

---

## Native ArcGIS Pro small proof

Already completed:

```text
QGIS GeoTIFF
37,767,543 bytes
4096 x 3072 RGB
EPSG:3857
Z18

-> ArcGIS Pro

tiff test 66.tpkx
38,306,245 bytes
Z0-Z18
PNG24
19 bundles
```

This proves the build path. It does not yet prove Field Maps runtime acceptance.

---

## Gold-card architecture if native TPKX passes

```text
ArcGIS Pro native district TPKX
-> physical removable storage
   +-- Field Maps basemaps\DISTRICT.tpkx
-> Android
-> Field Maps
```

MMPK remains optional deployment packaging rather than a repair mechanism. If it is used, build it only around the native/correct TPKX.

---

## Physical-card transport rule

Populate the removable storage on a computer while it is outside Android. Earlier Fire testing already proved ordinary protected-folder ADB/MTP injection is blocked by scoped storage.

The laptop's built-in SD reader showed suspect write-protection behavior. Use another reader/computer when needed.

---

## ArcGIS Earth Mobile role

Local project TPKX remains **LIVE-PROVEN on multiple packages**.

```text
Field Maps          -> agency workflow
ArcGIS Earth Mobile -> fast direct local TPKX viewer
```

---

## Custom converter disposition

v0.3.1:

```text
bench -> PASS
Field Maps -> FAIL
```

v0.3.2 exists as a bench-only PNG metadata experiment.

Future converter research should compare against the real ArcGIS Pro-generated raster TPKX. Production should not wait for it.

---

## Card-menu direction

- District — Z17
- County — Z18
- State Forests / selected hotspots — Z20
- Google Hybrid and/or Esri imagery/labels as capacity permits

Real finished byte counts decide card tiers.

---

## Map Fountain relationship

Map Fountain remains **LIVE-PROVEN / PARKED** from the normal personal-phone path.

Do not re-add network infrastructure merely because the manufacturing branch changed.

---

## Governing rules

> **Use the native ArcGIS Pro package for the Field Maps production path.**

> **Field Maps decides Field Maps compatibility.**

> **Have the data and field capability ready before the user needs them.**
