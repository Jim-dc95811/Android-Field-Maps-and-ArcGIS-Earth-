ARCGIS EARTH PRAVE LIVE v0.1.0 TEST
====================================

PURPOSE
-------
Modern ArcGIS Earth successor to the live PRAVE display portion of
PRAVE / ME Version 1.0 Gold.

OLD DISPLAY PATH
----------------
$PRAVE -> Python -> rewritten KML -> NetworkLink refresh -> Google Earth Pro

NEW TEST PATH
-------------
$PRAVE -> Python -> ArcGIS Earth local Automation API -> native point Drawing

Each PRAVE unit becomes one ArcGIS Earth drawing containing:
- the proven local RSSI fire-truck PNG
- the normal unit label (example 7-101)
- current latitude/longitude

On each new PRAVE sentence the same unit drawing is replaced directly.

ME / OWN POSITION
-----------------
This test intentionally does NOT plot ME from RMC.
ArcGIS Earth native GNSS/GPS is the intended modern own-position path.
RMC is still checksum-validated and logged so the mixed Raveon stream remains
fully observable.

REFERENCE AUTHORITY
-------------------
Decoder logic is carried forward from:
PRAVE_ME_v1_0_Gold.py
PRAVE_RMC_Field_Decoder_Tester_v1_0_Gold.py

Proven PRAVE fields:
3 latitude
4 longitude
8 district
12 RSSI
13 individual ID

Display ID:
district + three-digit individual
Example: 7 + 004 -> 7-004

RSSI ICONS
----------
The program uses the established folder:
C:\MyData\PRAVE_ME\Icons

Expected exact filenames:
firetruck_rssi_unknown.png
firetruck_rssi_1.png
firetruck_rssi_2.png
firetruck_rssi_3.png
firetruck_rssi_4.png
firetruck_rssi_5.png

If an exact numbered icon is missing, the unknown icon is used.
If no fire-truck icon is available, ArcGIS Earth may show its default point
symbol; the unit label and position can still prove the API path.

ARCGIS EARTH SETUP
------------------
1. Open ArcGIS Earth.
2. Open Settings.
3. Open Advanced application settings.
4. Enable Automation API.
5. Default API address is http://localhost:8000.
6. Leave ArcGIS Earth running.

SERIAL
------
Default:
COM12
19200 baud
8-N-1
flow control none

Edit INPUT_PORT near the top of AE_PRAVE_LIVE_v0_1_0_TEST.py if Windows
assigned another COM port.

BENCH TEST
----------
1. Enable ArcGIS Earth Automation API.
2. Run Run_AE_PRAVE_SELF_TEST.bat.
3. Connect the established PRAVE / RMC Gold field tester through the normal
   serial test path.
4. Run Run_AE_PRAVE_LIVE_v0_1_0_TEST.bat.
5. Expected: units 7-101 through 7-106 appear directly in ArcGIS Earth with
   unknown + 1-5 RSSI icon states and native text labels.

STATUS
------
TEST BUILD.
Gold PRAVE decoding is proven.
ArcGIS Earth Automation Drawing API is documented by Esri.
The new combined live path still requires physical Windows / ArcGIS Earth
acceptance.
