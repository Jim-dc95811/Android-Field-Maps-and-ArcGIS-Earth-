# ArcGIS Field Maps — Offline TPKX Quick Guide

**Android + microSD — local imagery without burning cellular data**

> **Goal:** Field Maps reads the imagery from your SD card. Cellular data stays out of the map pipeline.

## 1. Put the TPKX maps on the SD card

1. Put the microSD card in a computer/card reader.
2. Browse to this folder. Create it if it does not exist:

```text
\Android\data\com.esri.fieldmaps\files\basemaps
```

3. Copy the supplied `.tpkx` files into `basemaps`.
4. Put the card back in the phone. Open or restart Field Maps.

## 2. Select your local TPKX basemap

1. Open the Field Maps map you normally use.
2. Tap the **Overflow (...)** menu.
3. Tap **Basemap**.
4. Choose the desired local TPKX.

**Important:** having a TPKX on the card is not enough. Select it as the basemap you are viewing.

### About the true offline default

A true offline default basemap belongs to the web-map configuration and is normally set by the map owner in Field Maps Designer:

```text
Offline
→ Basemap and tile package
→ Tile package on the device
→ enter the exact TPKX filename
→ Save
```

A normal phone user does not need that access just to select and view a local basemap.

## 3. Block Field Maps from cellular data

Typical Samsung/Android path:

```text
Settings
→ Connections
→ Data usage
→ Allowed networks for apps
→ ArcGIS Field Maps
→ Wi-Fi only
```

Menu wording can vary by phone.

**Use the Android app-level network restriction.** The Cellular Data switch inside Field Maps is not a complete cellular-data block.

Normal phone service can stay on. Field Maps gets Wi-Fi only.

## 4. The 30-second offline proof

1. Set **Field Maps = Wi-Fi only**.
2. Turn **Wi-Fi OFF**.
3. Leave normal cell service on if desired.
4. Open the selected local TPKX map.
5. Pan and zoom.

If the imagery keeps drawing, the map is coming from local storage instead of the cellular network.

## If the TPKX does not appear

- Confirm it is in the `basemaps` folder.
- Restart/refresh Field Maps.
- For downloaded offline map areas, the copied basemap must overlap the area and use the same spatial reference as the map's default basemap.

## Official Esri references

- [Copy a basemap — ArcGIS Field Maps](https://doc.arcgis.com/en/field-maps/android/use-maps/configure-field-maps.htm)
- [Download maps — ArcGIS Field Maps](https://doc.arcgis.com/en/field-maps/android/use-maps/download-maps.htm)
- [Tools and features — Overflow / Basemap](https://doc.arcgis.com/en/field-maps/android/use-maps/quick-reference.htm)
- [Sideload MMPKs and basemaps using Android / microSD](https://support.esri.com/en-us/knowledge-base/sideload-mobile-map-packages-mmpks-and-basemaps-to-arcg-000026920)
- [BUG-000164200 — use Android settings to block Field Maps cellular traffic](https://support.esri.com/en-us/bug/turning-off-the-cellular-data-option-in-the-arcgis-fiel-bug-000164200)

---

**Field procedure:** card in → local TPKX selected → Field Maps Wi-Fi only → Wi-Fi off → map still works.
