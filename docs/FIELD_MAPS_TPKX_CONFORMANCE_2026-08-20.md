# ArcGIS Field Maps TPKX Conformance — Live Test 2026-08-20

## Decisive result

The physical-card / Field Maps workflow is now proven. The current failure is isolated to the project's historical MBTiles -> TPKX converter output.

Control test:

```text
same Android device
same physical microSD
same Field Maps Designer map
same basemaps directory
same general Web Mercator map setup

project converter TPKX -> REJECTED
Esri official Usa.tpkx -> ACCEPTED
```

Field Maps found the project-built TPKX but reported that the spatial reference of the file was not compatible with the map.

After `Usa.tpkx`, Esri's own official TPKX specimen, was copied to the same folder and Designer was changed to reference that filename, Field Maps accepted it.

## LIVE-PROVEN tonight

- `District 7 Local Basemap Test` exists in Field Maps Designer.
- Offline is enabled.
- Basemap is configured as **File on the device**.
- The map is shared **Everyone (public)**.
- Physical microSD basemap path works:

```text
\Android\data\com.esri.fieldmaps\files\basemaps\
```

- Esri official `Usa.tpkx` works from that path.

## What failed

The converter-built District 7 Esri Hybrid Z17 TPKX was discovered by Field Maps but rejected.

Inspection of that package showed expected-looking Web Mercator values:

- WKID 102100 / latestWKID 3857;
- 256 x 256 tiles;
- 96 DPI;
- standard Web Mercator origin;
- Z0-Z17 LOD sequence.

That means a quick `root.json` glance was not sufficient. Field Maps is enforcing package details more strictly than ArcGIS Earth / Earth Mobile / Pro did for this lineage.

## Why the existing MMPK is now held

ArcGIS Pro successfully created both small and district-scale MMPKs from the project TPKX. That remains a valid packaging proof.

However, ArcGIS Pro preserved the original TPKX intact inside the MMPK under `commondata/new_tpkx/`.

Therefore the current district MMPK contains the same TPKX lineage whose strict Field Maps compatibility is now under repair. Do not treat the old district MMPK as the next gold acceptance object until the underlying TPKX conformance test passes.

## Canonical repair branch

The manufacturing repository now contains the engineering record:

- [Offline GeoStack — TPKX / Field Maps Conformance](https://github.com/Jim-dc95811/Offline-GeoStack/blob/main/docs/TPKX_FIELD_MAPS_CONFORMANCE_2026-08-20.md)

A separate test converter has been built:

```text
ESRI_CANONICAL_TPKX_TEST_v0_2_0
```

It copies Esri's canonical Web Mercator LOD values and native metadata conventions rather than recalculating or creatively interpreting them.

Bench status: **BUILT / SELF-TESTED**.

Field Maps acceptance: **PENDING**.

## Immediate next test

```text
small MBTiles
-> ESRI_CANONICAL_TPKX_TEST_v0_2_0
-> small new TPKX
-> \Android\data\com.esri.fieldmaps\files\basemaps\
-> Designer exact filename
-> Field Maps
```

If that passes, regenerate the district TPKX with the corrected converter, then rebuild the MMPK around the corrected TPKX and resume the full cold/no-Internet district-card test.

## Evidence matrix

| Capability | Status |
| --- | --- |
| Field Maps Designer + public map + File on the device workflow | ✅ **LIVE-PROVEN** |
| Physical microSD `basemaps` path | ✅ **LIVE-PROVEN** |
| Esri official `Usa.tpkx` in Field Maps | ✅ **LIVE-PROVEN** |
| Project historical converter TPKX in Field Maps | ❌ **FAILED / NEEDS REPAIR** |
| Project historical converter TPKX in ArcGIS Earth Windows | ✅ **LIVE-PROVEN** |
| Project TPKX lineage in ArcGIS Earth Mobile | ✅ **LIVE-PROVEN on multiple packages** |
| ArcGIS Pro TPKX -> MMPK packaging bridge | ✅ **PASS** |
| Canonical test converter v0.2.0 | 🟡 **BUILT / SELF-TESTED; FIELD MAPS TEST PENDING** |
| Corrected district TPKX | 🟡 **PENDING SMALL-CONFORMANCE PASS** |
| Corrected district MMPK / full cold card | 🟡 **PENDING CORRECTED TPKX** |

## Governing rule

> **Esri's working TPKX is the reference. Field Maps is the judge.**
