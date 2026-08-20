# Android Field Maps + ArcGIS Earth — Roadmap

## Current mission

Deploy finished local map products and proven ArcGIS Earth / Windows field features to the user with the least possible operator complexity.

For personal Android maps, the preferred path is **prepared local removable storage**, not a field server.

The current gold-card architecture is:

```text
Offline Map Factory
-> district TPKX
-> ArcGIS Pro minimal MMPK wrapper
-> physical microSD
   +-- Field Maps mappackages\DISTRICT.mmpk
   +-- Field Maps basemaps\DISTRICT.tpkx
-> Android
-> Field Maps + ArcGIS Earth Mobile
```

The duplication is intentional. Reliability outranks storage elegance.

## Primary user problem

The strongest adoption value is **cellular-data protection**.

Users should stop rationing map use because of expensive or weak cellular service. The district imagery should already be local so the phone can keep cellular service available for calls/texts without repeatedly streaming the heavy basemap.

## Immediate gold acceptance gate — 2026-08-20

Current prepared payload:

- district Esri Hybrid Z17 TPKX: approximately 52 GB;
- matching ArcGIS Pro MMPK: approximately 52 GB;
- physical 128 GB exFAT microSD selected;
- first target: Amazon Fire tablet for map-path acceptance;
- GPS/own-position acceptance follows on a GPS-capable personal Android phone.

### Field Maps MMPK acceptance

1. populate the physical card on Windows while it is outside Android;
2. place the MMPK under `Android\data\com.esri.fieldmaps\files\mappackages`;
3. place the matching TPKX under `Android\data\com.esri.fieldmaps\files\basemaps`;
4. safely eject and insert the card into the Fire;
5. open Field Maps and go to **On Device**;
6. confirm the district MMPK appears;
7. open it and verify district-wide imagery/labels, pan, and zoom through Z17;
8. remove public Internet and repeat;
9. close/reopen Field Maps while still disconnected;
10. repeat later on a GPS-capable personal Android phone;
11. test the personal-phone cell-data scenario with Field Maps restricted to Wi-Fi only while normal cellular service remains available.

Promote only after the real device passes.

## ArcGIS Pro packaging result

**Status: PASS on both small and district-scale packages.**

ArcGIS Pro 3.7 created a modern minimal MMPK from an existing TPKX using the supported Mobile Map packaging workflow.

Small specimen observations:

- 0 analyzer errors / 0 warnings / 0 messages;
- MMPK version 3.0;
- original TPKX preserved intact inside the package;
- no HTTP/HTTPS references found in the small specimen `.mmap` or `.mapx`;
- Pro-created MMPK rendered in Windows ArcGIS Earth while Earth showed **Not signed in**.

The district-scale approximately 52 GB MMPK also packaged successfully from the existing approximately 52 GB TPKX.

This proves the manufacturing bridge. It does **not** yet prove the Field Maps runtime path.

## Physical-card transport rule

Earlier Fire testing proved ordinary ADB/MTP-style writes into another app's protected `Android/data` tree are blocked by Android scoped storage.

Do not resume that dead end. The current route follows Esri's documented physical-card sideload method: populate the card on the computer while it is outside Android, then insert the prepared card into the device.

## ArcGIS Earth Mobile role

ArcGIS Earth Mobile local TPKX is already **LIVE-PROVEN on multiple project packages**.

Position it as the fast local map viewer, not merely a backup:

```text
Field Maps         -> agency workflow / on-device packaged map
ArcGIS Earth Mobile -> high-performance direct local TPKX viewer
```

## Current user features

### PRAVE Live

**Status: LIVE-PROVEN.**

The preserved original v0.1.0 package lives under `features/prave-live/`. Do not rewrite that evidence package.

### QR Command Bridge

**Status: LIVE-PROVEN FOUNDATION / COMMAND EXPANSION DESIGNED.**

Keep the hard-coded allowlist rule. QR payload text must never become generic shell or script input.

## Card-menu direction

The user-facing menu remains simple:

- District — Z17
- County — Z18
- State Forests / selected hotspots — Z20
- Google Hybrid and/or Esri imagery/labels as capacity permits

Real finished byte counts decide card tiers.

## Map Fountain relationship

Map Fountain remains **LIVE-PROVEN / PARKED** from the primary personal-phone path.

Reopen it only when shared storage solves a real problem better than local storage, including:

- Starlink/basecamp NAS role;
- genuine multi-client shared-map need;
- removable storage proving insufficient.

Do not re-add infrastructure merely because it is technically interesting.

## Current reference

- [Field Maps + ArcGIS Earth Mobile — District Map Card Reference](docs/FIELD_MAPS_MMPK_CARD_REFERENCE_2026-08-20.md)
- [Current SD-card quick guide](FIELD_MAPS_SD_CARD_QUICK_GUIDE.md)

## Governing rules

> **Have the data and the field capability ready before the user needs them.**

> **The real target decides acceptance.**
