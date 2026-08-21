# Android Field Maps + ArcGIS Earth — Roadmap

## Current mission

Deploy finished local map products and proven ArcGIS Earth / Windows field features to the user with the least possible operator complexity.

For personal Android maps, the preferred path remains **prepared local removable storage**, not a field server.

The user value remains **cellular-data protection** and freedom from map rationing.

---

## Immediate gate — small canonical TPKX in Field Maps

A live control test changed the order of operations.

Using the same physical microSD and Field Maps Designer workflow:

- project historical converter TPKX -> **REJECTED**;
- Esri official `Usa.tpkx` -> **ACCEPTED**.

The physical `basemaps` path, Designer configuration, and public map are therefore proven good. The manufacturing converter is the current defect.

### Next test

```text
small MBTiles
-> ESRI_CANONICAL_TPKX_TEST_v0_2_0
-> small new TPKX
-> \Android\data\com.esri.fieldmaps\files\basemaps\
-> Designer exact filename
-> Field Maps
```

Promote only after Field Maps opens that new specimen.

- [Field Maps TPKX Conformance — 2026-08-20](docs/FIELD_MAPS_TPKX_CONFORMANCE_2026-08-20.md)

---

## After the small TPKX passes

1. integrate the corrected converter into Offline GeoStack / Offline Map Factory;
2. integrate the same corrected TPKX stage into Rasta;
3. regenerate the District 7 Esri Hybrid Z17 TPKX;
4. rebuild the MMPK from the corrected district TPKX;
5. populate the physical card;
6. run Field Maps cold/no-Internet district acceptance;
7. repeat later on a GPS-capable personal Android phone;
8. test the personal-cellular plan with Field Maps restricted to Wi-Fi only.

Do not spend hours regenerating the approximately 52 GB district products before the tiny conformance gate passes.

---

## Intended gold-card architecture

After converter repair:

```text
corrected district TPKX
-> ArcGIS Pro minimal MMPK wrapper
-> physical microSD
   +-- Field Maps mappackages\DISTRICT.mmpk
   +-- Field Maps basemaps\DISTRICT.tpkx
-> Android
-> Field Maps + ArcGIS Earth Mobile
```

The duplication remains intentional. Reliability outranks storage elegance.

---

## ArcGIS Pro packaging result

**PASS on both small and district-scale packages.**

ArcGIS Pro 3.7 created a modern minimal MMPK from an existing TPKX.

Small specimen observations:

- 0 analyzer errors / 0 warnings / 0 messages;
- MMPK version 3.0;
- original TPKX preserved intact inside the package;
- no HTTP/HTTPS references found in the small `.mmap` or `.mapx`;
- package rendered in Windows ArcGIS Earth while Earth showed Not signed in.

### Updated meaning

Because ArcGIS Pro preserves the TPKX intact, the approximately 52 GB MMPK built from the historical converter does not repair the Field Maps compatibility defect.

Hold the full MMPK acceptance test until the source TPKX is corrected.

---

## Physical-card transport rule

Earlier Fire testing proved ordinary ADB/MTP-style writes into another app's protected `Android/data` tree are blocked by Android scoped storage.

Do not resume that dead end. Populate the physical card on a computer while it is outside Android.

### Reader note

The laptop's built-in SD reader produced write-protection behavior on multiple cards/adapters; another computer wrote successfully. Treat the reader as suspect.

The card is disposable test media.

---

## ArcGIS Earth Mobile role

ArcGIS Earth Mobile local project TPKX is already **LIVE-PROVEN on multiple packages**.

Position it as the fast local map viewer:

```text
Field Maps          -> agency workflow
ArcGIS Earth Mobile -> fast direct local TPKX viewer
```

The Field Maps strict-conformance failure does not erase Earth Mobile evidence.

---

## Current user features

### PRAVE Live

**LIVE-PROVEN.** Preserve the original v0.1.0 evidence package.

### QR Command Bridge

**LIVE-PROVEN FOUNDATION / COMMAND EXPANSION DESIGNED.** Keep the hard-coded allowlist rule; QR text must never become generic shell/script input.

### AE SYSTEM CHECK

**LIVE-PROVEN on Windows ArcGIS Earth.** Mobile/Field Maps compatibility is a separate claim.

---

## Card-menu direction

After the package-conformance problem is solved, the user-facing card menu remains:

- District — Z17
- County — Z18
- State Forests / selected hotspots — Z20
- Google Hybrid and/or Esri imagery/labels as capacity permits

Real finished byte counts decide card tiers.

---

## Map Fountain relationship

Map Fountain remains **LIVE-PROVEN / PARKED** from the normal personal-phone path.

A converter defect is not a reason to re-add network infrastructure. Reopen Map Fountain only for a genuine shared-storage use such as Starlink/basecamp NAS or multi-client map access.

---

## Governing rules

> **Esri's working TPKX is the reference.**

> **Field Maps decides Field Maps compatibility.**

> **Have the data and field capability ready before the user needs them.**
