# Android Field Maps + ArcGIS Earth — Changelog

## 2026-08-18 — Wildland Imagery University added as training branch

- Recovered the earlier **Wildland Imagery University** concept from the project Library and promoted it into the public deployment-to-the-user story.
- Added `training/WILDLAND_IMAGERY_UNIVERSITY.md`.
- Preserved the core training model: **SEE → THINK → DECIDE**.
- Preserved the principle: **Maps tell you where things should be. Experience tells you what they are really like.**
- Added project-developed strategic / operational / tactical / detail viewing-elevation heuristics with an explicit warning that they are training heuristics, not agency doctrine.
- Added imagery-reading topics including road-versus-trail interpretation, turnarounds, gates, bridges, swamps, clearcuts, seasonal change, shadows, human geometry, and hybrid imagery cross-checking.
- Added the long-term teaching model: real imagery → student questions → experienced-firefighter reasoning → annotated lesson → teach the judgment forward.
- Explicitly kept fieldcraft, agency policy, current conditions, reconnaissance, road verification, and qualified on-scene judgment above remote imagery.
- Linked the training branch into the repository front door and the larger Offline GeoStack **Journey of Ideas** / **Bridges We Had to Build** showcase.

## 2026-08-18 — QR Command Bridge expanded with origin + QR maker utility

- Added **URL QR Maker v0.1.0** under `features/qr-command-bridge/tools/url-qr-maker/`.
- Published its core Python source, BAT launcher, self-test record, and QR-library license.
- Recorded the exact original portable archive identity: 128,299 bytes, SHA-256 `f2f31ee0e12502734f46a6671516f6ce093e7d2b5b41dbaeb17cab2db5f97033`.
- Added **Android Phone FireTextSender** as the documented origin of the QR dispatch lineage.
- Recorded the original FireTextSender archive identity: 3,375,142 bytes, SHA-256 `4a7990644f0da321f259e977ef16c7f20f45bb0ec2159df89afcb3abc541cf07`.
- Preserved the historical relationship: Windows map coordinates → Android SMS bridge → later MacroDroid SMS capture → phone QR → Windows QR receiver.
- Did not mirror the raw FireTextSender ZIP publicly because it contains deployment-specific phone numbers and machine paths; its exact original remains preserved in the canonical archive.

## 2026-08-18 — QR Command Bridge added as user feature

- Added **QR Command Bridge** beside PRAVE Live as the optical dispatch / command-input branch.
- Recovered and reviewed the original QR Gold lineage before documenting the modern branch.
- Preserved evidence for:
  - v1.0 Gold camera / JSON / coordinate receiver;
  - v1.0.1 Gold Hotfix live-test hardening;
  - v1.1.0 Gold Command Proof strict `GMDS_CMD:<TOKEN>` allowlist behavior;
  - the three-macro MacroDroid SMS → clipboard → QR bridge.
- Recorded exact canonical package names, byte sizes, and SHA-256 hashes in `features/qr-command-bridge/EVIDENCE_AND_LINEAGE.md`.
- Preserved the critical security rule: **QR text is data, never executable code.**
- Recorded `GMDS_CMD:TEST` + unknown-command blocking as the proven command proof.
- Kept ArcGIS Earth API actions and Windows restart/shutdown/helper-process actions at **DESIGNED / NOT YET LIVE-PROVEN** status.
- Established that destructive future actions require an additional confirmation/interlock rather than a single casual scan.

## 2026-08-18 — PRAVE Live added as ArcGIS Earth user feature

- Added **PRAVE Live** as a LIVE-PROVEN optional ArcGIS Earth field feature.
- Established this repository as the authoritative user-facing home for the PRAVE Live branch.
- Published the preserved original `AE_PRAVE_LIVE_v0_1_0_TEST.zip` package unchanged.
- Recorded its exact SHA-256 and original COM12 / 19200-baud assumptions.
- Preserved the original package README while separately recording that the later physical ArcGIS Earth acceptance run passed.
- Kept the deeper parser/API engineering record in Offline GeoStack and linked the two repositories.
- Clarified role separation: ArcGIS Earth native GNSS owns ME / own position; PRAVE Live owns remote `$PRAVE` units.

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

1. Offline GeoStack proved repeatable QGIS → MBTiles → native TPKX manufacturing and the PRAVE → ArcGIS Earth Automation API path.
2. Rasta Pyramid Factory generalized the pyramid machinery to giant rasters and deep-zoom imagery.
3. Map Fountain proved remote native TPKX access over SMB on Windows and router-only Static REST WMTS delivery to ArcGIS Earth Mobile.

The deployment lesson was simpler than the machinery:

> **Put the finished capability where the user actually touches it.**
