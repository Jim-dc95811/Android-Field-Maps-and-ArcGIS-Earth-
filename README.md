# Android Field Maps + ArcGIS Earth

## Android offline maps + Windows ArcGIS Earth field features

**This repository is the deployment-to-the-user end of the four-project family.**

It owns the simple human-facing workflows: prepared local maps on Android, optional Windows ArcGIS Earth features such as PRAVE Live and QR Command Bridge, a standard AE System Check diagnostic map, and imagery-based terrain training.

**Keywords:** ArcGIS Field Maps, ArcGIS Earth, offline Android maps, TPKX, microSD, offline field mapping, GNSS, PRAVE, QR code, QR Command Bridge, MacroDroid, dispatch mapping, Windows field computer, cellular-data protection, offline GIS, wildland fire, terrain training, aerial imagery, topographic training, LOD calibration, tile diagnostics, system check map

**[Download the one-page printable Field Maps Offline TPKX Quick Guide](Field_Maps_Offline_TPKX_Quick_Guide.pdf)**

> **The manufacturing side can be complicated. The operator side should not be.**

---

## User feature 1 — Offline TPKX maps on Android

```text
Offline Map Factory
→ finished TPKX
→ microSD / local storage
→ Android
→ ArcGIS Field Maps or ArcGIS Earth Mobile
→ local imagery + own position
```

Current evidence state:

- ArcGIS Earth Mobile local TPKX: ✅ **LIVE-PROVEN on multiple project packages**.
- ArcGIS Field Maps TPKX on microSD: 🟡 **DOCUMENTED BY VENDOR / PROJECT LIVE TEST PENDING**.
- Android app-level Wi-Fi-only setting: used to protect personal cellular data from map-app consumption.

Current card-planning direction:

- **AE SYSTEM CHECK** — standard synthetic diagnostic TPKX
- District — Z17
- County — Z18
- State Forests / selected high-value areas — Z20
- Google Hybrid and Esri imagery/labels where useful and capacity permits
- optional Rasta deep-zoom products where spare capacity is useful

Do not freeze card tiers from theory. Real finished byte counts decide the menu.

### Field Maps basemap path

Esri documents sideloaded basemaps under:

```text
\Android\data\com.esri.fieldmaps\files\basemaps
```

Supported documented types include TPK / TPKX / VTPK and geospatial PDF.

### Protect the personal cellular plan

The Field Maps in-app Cellular Data option is not treated as a total app-level block. For a full practical block on Android, set **ArcGIS Field Maps → Wi-Fi only** in the phone’s app network settings.

Typical Samsung path:

```text
Settings
→ Connections
→ Data usage
→ Allowed networks for apps
→ ArcGIS Field Maps
→ Wi-Fi only
```

Menu names vary by Android manufacturer/version.

### Normal Field Maps handoff

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

## User feature 2 — PRAVE Live

### [Remote radio units in Windows ArcGIS Earth](features/prave-live/README.md)

**Status: ✅ LIVE-PROVEN**

```text
PRAVE radio reports
→ Windows serial input
→ PRAVE Live
→ ArcGIS Earth local Automation API
→ labeled remote units + RSSI fire-truck icons
```

Role separation is intentional:

```text
ArcGIS Earth native GNSS → ME / own-position blue dot
PRAVE Live              → remote PRAVE units
```

The exact original live-proven package is preserved in the feature folder.

The deeper parser/API engineering record remains in Offline GeoStack.

---

## User feature 3 — QR Command Bridge

### [Optical dispatch + approved local commands](features/qr-command-bridge/README.md)

**Status: ✅ LIVE-PROVEN FOUNDATION / 🟡 COMMAND EXPANSION DESIGNED**

```text
phone / printed QR
→ Windows camera
→ QR decoder
→ strict parser / hard-coded allowlist
→ dispatch result or approved local action
```

The Gold QR lineage already proved:

- camera QR decoding;
- MacroDroid SMS → clipboard JSON → QR;
- coordinate parsing and pin-drop behavior in the original Google Earth path;
- ordinary message display;
- strict `GMDS_CMD:<TOKEN>` recognition;
- `GMDS_CMD:TEST`;
- unknown-command blocking.

Hard rule:

> **QR text is data, never executable shell text.**

ArcGIS Earth API actions and Windows restart/shutdown/helper-process actions remain **DESIGNED until individually implemented and live-tested**.

The QR branch also preserves:

- the [Android Phone FireTextSender origin story](features/qr-command-bridge/origins/fire-text-sender/README.md);
- the [URL QR Maker v0.1.0](features/qr-command-bridge/tools/url-qr-maker/README.md) for local/offline QR creation;
- exact Gold package identities/hashes in the [Evidence and Lineage](features/qr-command-bridge/EVIDENCE_AND_LINEAGE.md) record.

---

## User feature 4 — Wildland Imagery University

### [Teaching terrain judgment before the emergency](training/WILDLAND_IMAGERY_UNIVERSITY.md)

**Status: 🟡 TRAINING CONCEPT / PROJECT-DEVELOPED MATERIAL**

This branch addresses the problem that software cannot solve by itself:

> **Give firefighters the imagery, then teach them what it means.**

The model is:

```text
SEE
→ recognize terrain / access / human patterns

THINK
→ understand why an experienced firefighter cares

DECIDE
→ make a better-informed choice before committing resources
```

Topics include strategic-to-detail viewing elevation, road-versus-trail interpretation, turnarounds, bridges, gates, swamps, clearcuts, drainage, shadows, seasonal change, human geometry, hybrid imagery, and the habit of zooming out for context and back in for confirmation.

The training page explicitly treats imagery as a tool—not the final authority—and preserves fieldcraft, local knowledge, agency policy, reconnaissance, and qualified on-scene judgment as primary.

The long-term idea is to capture experienced-firefighter reasoning from real imagery and teach it forward.

---

## User feature 5 — AE SYSTEM CHECK

### [Prove the viewer and storage before blaming the real map](features/ae-system-check/README.md)

**Status: ✅ LIVE-PROVEN — WINDOWS ARCGIS EARTH**

AE SYSTEM CHECK is a tiny synthetic TPKX intended to live on every prepared SD card beside the real operational maps.

```text
Z16 RED
→ Z17 BLUE
→ Z18 GREEN
→ Z19 ORANGE
→ Z20 PURPLE
```

Every tile identifies its level, row/column, XYZ address, and boundaries, with crosshairs and fine patterns that make unexpected blur or resampling visible.

v0.1.0 is a mathematically clean nested ladder:

```text
1 + 4 + 16 + 64 + 256 = 341 tiles
```

All 341 PNG tile byte hashes were verified identical between the source MBTiles and the finished Compact Cache V2 bundles.

On 2026-08-18, the exact package was opened on the real Windows ArcGIS Earth target. The operator verified **all five intended levels, Z16 through Z20, render correctly**. Z16 displayed the single red parent panel and Z20 displayed the ordered 16 × 16 purple child grid; the intermediate blue, green, and orange levels also passed.

Exact accepted binary:

```text
AE_SYSTEM_CHECK_v0_1_0.tpkx
4,196,743 bytes
SHA-256 7843afedb94fdc3654be9eadd1c8d18d14bd2c70abd3d5a1d88f5278c1776390
```

Recommended habit:

> **Open SYSTEM CHECK first. Make the gear prove itself. Then open the mission map.**

Windows ArcGIS Earth is LIVE-PROVEN. Mobile/microSD/network-hosted use remain separate acceptance paths for the same specimen.

---

## Why this repository exists

The target field user should not need to understand QGIS, projections, tile-pyramid internals, converter mechanics, or the history of every engineering branch.

This project separates the roles:

### Map maker / system builder

Manufactures, verifies, refreshes, and prepares the map products and optional field tools.

### Field user

Receives prepared geography and short instructions. Optional live features are added only when the field role actually benefits.

### Experienced trainer

Turns imagery into judgment by explaining what matters, what can mislead, and what must still be verified on the ground.

---

## Evidence discipline

Keep these states separate:

| Capability | Status |
| --- | --- |
| ArcGIS Earth Mobile local TPKX | ✅ **LIVE-PROVEN** |
| ArcGIS Field Maps TPKX on microSD | 🟡 **VENDOR-DOCUMENTED / PROJECT LIVE TEST PENDING** |
| PRAVE Live → ArcGIS Earth | ✅ **LIVE-PROVEN** |
| QR camera / SMS JSON / coordinate lineage | ✅ **LIVE-PROVEN lineage** |
| `GMDS_CMD:TEST` allowlist proof | ✅ **LIVE-PROVEN command proof** |
| QR → ArcGIS Earth API actions | 🟡 **DESIGNED / NOT YET LIVE-PROVEN** |
| QR → Windows destructive actions | 🟡 **DESIGNED / NOT YET LIVE-PROVEN** |
| Wildland Imagery University | 🟡 **TRAINING CONCEPT / PROJECT-DEVELOPED MATERIAL** |
| AE SYSTEM CHECK v0.1.0 — Windows ArcGIS Earth | ✅ **LIVE-PROVEN Z16–Z20** |
| AE SYSTEM CHECK — mobile/microSD/network paths | 🟡 **SEPARATE ACCEPTANCE PENDING** |

The real target decides acceptance.

---

## Four-project family

1. **[Offline GeoStack](https://github.com/Jim-dc95811/Offline-GeoStack)** — master map manufacturing + field-system integration. Its [Journey of Ideas](https://github.com/Jim-dc95811/Offline-GeoStack/blob/main/docs/JOURNEY_OF_IDEAS.md) and [Bridges We Had to Build](https://github.com/Jim-dc95811/Offline-GeoStack/blob/main/docs/THE_BRIDGES_WE_HAD_TO_BUILD.md) pages tell the larger story.
2. **[Rasta Pyramid Factory](https://github.com/Jim-dc95811/Rasta-Pyramid-Factory)** — giant-raster / deep-zoom pyramid manufacturing.
3. **[Map Fountain](https://github.com/Jim-dc95811/Map-Fountain)** — LIVE-PROVEN shared-storage/network delivery evidence; currently parked from the normal personal-phone path.
4. **Android Field Maps + ArcGIS Earth** — deployment to the user: Android offline maps + Windows ArcGIS Earth field features + imagery training.

---

## Governing rules

- No operational dependence on public Internet for the prepared map itself.
- Do not make ordinary users learn the Factory.
- Local files outrank streaming when the same useful imagery can already be on the device.
- Keep a known-good diagnostic TPKX on the card and prove the viewer/storage path before blaming an operational map.
- Do not add GIS or live-control features merely because they are technically possible.
- QR command inputs must remain explicit allowlisted data, never arbitrary executable text.
- Imagery training must reinforce fieldcraft, not substitute for current conditions or qualified judgment.
- Preserve exact package/source/zoom/build identities so deployments can be reproduced.
- Respect third-party imagery, basemap, attribution, caching, export, and redistribution terms.
- The real target application decides acceptance.

---

# The simple version

> **Prepared geography. Prove the gear. Own position. Live field units. Deliberate commands. Better terrain judgment. Go to work.**
