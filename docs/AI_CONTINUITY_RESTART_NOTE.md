# Android Field Maps + ArcGIS Earth — AI / Maintainer Restart Note

## Project identity

This repository is the **deployment-to-the-user end** of the four-project family.

Its job is not to manufacture maps. Its job is to make finished map products and proven ArcGIS Earth field features usable without dragging the operator through the engineering stack.

## Current deployment doctrine

### Personal Android maps

```text
Offline Map Factory
→ finished TPKX
→ microSD / local storage
→ Android phone
→ ArcGIS Field Maps or ArcGIS Earth
```

Primary benefit:

- local imagery;
- no operational dependence on cellular basemap delivery;
- user can block Field Maps from cellular data while leaving ordinary phone service available;
- large prebuilt pyramids can respond from local storage instead of waiting on weak field connectivity.

### PRAVE Live — Windows ArcGIS Earth

```text
$PRAVE radio reports
→ Windows serial input
→ PRAVE Live
→ ArcGIS Earth local Automation API
→ remote units on the operational map
```

PRAVE Live is **LIVE-PROVEN** and its authoritative user-facing home is:

`features/prave-live/`

The exact original package is preserved there as `AE_PRAVE_LIVE_v0_1_0_TEST.zip`.

Do not silently modify that ZIP and continue calling it the original proof package.

Role split:

```text
ArcGIS Earth native GNSS → ME / own position
PRAVE Live              → remote PRAVE units
```

The deeper parser/API engineering record remains in Offline GeoStack.

## Current map-card plan

Do not freeze exact capacity tiers until real Factory sizes are measured.

Current menu direction:

- district Z17;
- county Z18;
- State Forests / selected high-value areas Z20;
- Google Hybrid and Esri imagery/labels where useful and capacity allows.

## Evidence status

- Offline Map Factory 1.0: BUILT / SELF-TESTED — live acceptance pending under the new product name.
- Historical TPKX Map Factory v1.0.0: RELEASE-ACCEPTED / frozen milestone.
- Local TPKX in ArcGIS Earth Mobile: LIVE-PROVEN on multiple packages.
- Esri documentation supports Field Maps Android TPKX basemaps on device/microSD: DOCUMENTED BY VENDOR.
- This project's own Field Maps + microSD TPKX test: PENDING LIVE TEST.
- PRAVE → ArcGIS Earth Automation API live display: LIVE-PROVEN.
- Field Maps Android app-level Wi-Fi-only cellular block: documented by Esri Support.

Do not silently promote vendor documentation or self-tests into this project's LIVE-PROVEN status.

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

The operator-facing workflow must stay short.

Do not turn the deployment repo into an encyclopedia of GIS features.

For Field Maps:

> card → cheat sheet → local basemap → Wi-Fi only → work

For PRAVE Live, preserve the proven path now; if it is later repackaged for normal users, automatic COM-port discovery should replace source editing.

Overlays, MMPKs, geofences, complex forms, and other GIS features are optional future branches only when a real field need appears.

## Relationship to sibling repositories

- Offline GeoStack — master map manufacturing and deeper integration engineering record.
- Rasta Pyramid Factory — general high-resolution raster-pyramid manufacturing.
- Map Fountain — proven router/network-storage experiments; parked from primary personal-phone deployment, possible future Starlink/NAS role.
- This repo — final Android deployment plus user-facing ArcGIS Earth field features.

## Do not regress

- Do not require a field server for the normal personal-phone map path.
- Do not require public Internet for the map itself.
- Do not make the user learn QGIS/Python/TPKX internals.
- Do not bury the one-page Field Maps procedure under advanced features.
- Do not claim Field Maps live acceptance until the actual phone test passes.
- Do not rewrite the preserved PRAVE Live proof ZIP by inertia.
- Do not distribute third-party imagery without respecting its terms.

## Cold-start reading order

1. `README.md`
2. `features/prave-live/README.md` when PRAVE/remote-unit display matters
3. `FIELD_MAPS_SD_CARD_QUICK_GUIDE.md`
4. `ROADMAP.md`
5. this file
6. the current Offline GeoStack README
7. sibling project READMEs only when deeper manufacturing/history is needed

## Governing principle

> **Put the finished capability where the user actually touches it.**
