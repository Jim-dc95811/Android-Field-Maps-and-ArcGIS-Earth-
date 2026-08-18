# Android Field Maps + ArcGIS Earth — AI / Maintainer Restart Note

## Project identity

This repository is the **deployment end** of the four-project family.

Its job is not to manufacture maps. Its job is to make the finished products useful to normal Android field users, especially people using personal phones who do not want to become GIS technicians.

## Current deployment doctrine

```text
Offline GeoStack / TPKX Map Factory
→ finished TPKX
→ microSD card
→ Android phone
→ ArcGIS Field Maps or ArcGIS Earth
```

Primary benefit:

- local imagery;
- no operational dependence on cellular basemap delivery;
- user can block Field Maps from cellular data while leaving ordinary phone service available;
- large prebuilt pyramids can respond from local storage instead of waiting on weak field connectivity.

## Current map-card plan

Do not freeze exact capacity tiers until real Factory sizes are measured.

Current menu direction:

- district Z17;
- county Z18;
- State Forests / selected high-value areas Z20;
- Google Hybrid and Esri imagery/labels where useful and capacity allows.

## Evidence status

- TPKX Map Factory v1.0.0: RELEASE-ACCEPTED / frozen.
- Local TPKX in ArcGIS Earth Mobile: LIVE-PROVEN on multiple packages.
- Esri documentation supports Field Maps Android TPKX basemaps on device/microSD: DOCUMENTED BY VENDOR.
- This project's own Field Maps + microSD TPKX test: PENDING LIVE TEST.
- Field Maps Android app-level Wi-Fi-only cellular block: documented by Esri Support.

Do not silently promote vendor documentation into this project's LIVE-PROVEN status.

## Field Maps sideload path

```text
\Android\data\com.esri.fieldmaps\files\basemaps
```

Supported vendor-documented basemap types include TPK/TPKX/VTPK and geospatial PDF.

A true default offline basemap is configured by the web-map owner in Field Maps Designer. An ordinary phone user can still select an available basemap from the Field Maps Overflow/Basemap control.

## Personal-phone cellular rule

The Field Maps in-app Cellular Data setting is not a total app-level block.

For full cellular blocking on Android, use the device network setting and set ArcGIS Field Maps to Wi-Fi only.

This is important because the target audience may be using personal phones and personal data plans.

## Human-factors rule

The operator-facing workflow must stay very short.

Do not turn the deployment repo into an encyclopedia of Field Maps features.

Default posture:

> card → cheat sheet → local basemap → Wi-Fi only → work

Overlays, MMPKs, geofences, complex forms, and other GIS features are optional future branches only when a real field need appears.

## Relationship to sibling repositories

- Offline GeoStack — master field mapping / TPKX manufacturing.
- Rasta Pyramid Factory — general high-resolution raster-pyramid manufacturing.
- Map Fountain — proven router/network-storage experiments; parked from primary personal-phone deployment, possible future Starlink/NAS role.
- This repo — final Android deployment and user procedure.

## Do not regress

- Do not require a field server for the normal personal-phone map path.
- Do not require public Internet for the map itself.
- Do not make the user learn QGIS/Python/TPKX internals.
- Do not bury the one-page field procedure under advanced features.
- Do not claim Field Maps live acceptance until the actual phone test passes.
- Do not distribute third-party imagery without respecting its terms.

## Cold-start reading order

1. `README.md`
2. `FIELD_MAPS_SD_CARD_QUICK_GUIDE.md`
3. `ROADMAP.md`
4. this file
5. the current Offline GeoStack README
6. sibling project READMEs only when deeper manufacturing/history is needed

## Governing principle

> **The complicated work belongs on the map-maker side. The field user gets a card and a map that works.**
