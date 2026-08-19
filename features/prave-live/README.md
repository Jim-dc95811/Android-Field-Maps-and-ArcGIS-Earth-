# PRAVE Live — Remote Units in ArcGIS Earth

**Status: LIVE-PROVEN**

PRAVE Live is an optional ArcGIS Earth field feature for displaying remote `$PRAVE` unit positions directly on the operational map.

```text
PRAVE radio reports
→ Windows serial input
→ PRAVE Live
→ ArcGIS Earth local Automation API
→ live remote-unit markers
```

This feature belongs here because this repository is the deployment-to-the-user end of the project family. Offline Map Factory supplies prepared basemaps; PRAVE Live adds live field units to ArcGIS Earth.

## What the operator sees

Each valid remote unit is displayed with:

- district + three-digit unit ID, for example `7-101`;
- current latitude / longitude;
- the established RSSI fire-truck icon family;
- native ArcGIS Earth labeling;
- replacement of the same logical unit drawing when a new report arrives.

The path does not require public Internet access.

## Own position stays native

PRAVE Live deliberately does **not** draw ME / own-position from RMC.

```text
ArcGIS Earth native GNSS → own-position blue dot
PRAVE Live              → remote PRAVE units
```

The mixed Raveon stream may still contain `$GPRMC` / `$GNRMC`; those sentences are checksum-validated and logged by the program.

## Live proof

The controlled Windows / ArcGIS Earth run displayed six representative units:

```text
7-101
7-102
7-103
7-104
7-105
7-106
```

with RSSI states from unknown through 5 bars. Observed healthy state included:

```text
UNITS=6
API_OK=47
API_BAD=0
BAD_RMC=0
BAD_PRAVE=0
RMC=FRESH
```

Project evidence status: **LIVE-PROVEN**.

## Preserved original package

The original package is published here unchanged:

**[AE_PRAVE_LIVE_v0_1_0_TEST.zip](AE_PRAVE_LIVE_v0_1_0_TEST.zip)**

SHA-256:

```text
da46b1d13ea7bc608ec2681003545fe731cf87ff2cad029929520a83687d6415
```

It contains:

```text
AE_PRAVE_LIVE_v0_1_0_TEST.py
README.txt
Run_AE_PRAVE_LIVE_v0_1_0_TEST.bat
Run_AE_PRAVE_SELF_TEST.bat
```

The original README was written before the physical ArcGIS Earth acceptance run, so it still calls the combined live path a TEST awaiting acceptance. The later real-target test passed; the implementation path is now LIVE-PROVEN. The original package is preserved rather than rewritten after the fact.

The original `README.txt` and BAT launchers are also visible in this folder for quick inspection. The authoritative Python source remains inside the preserved ZIP so the evidence package stays exact.

## Original package assumptions

```text
Serial port: COM12
Serial:      19200 baud, 8-N-1, no flow control
ArcGIS Earth Automation API: http://localhost:8000
RSSI icons:  C:\MyData\PRAVE_ME\Icons
```

Windows may assign a different COM port. The original v0.1.0 test package stores that port near the top of the Python file.

The serial path requires `pyserial`.

## ArcGIS Earth setup

1. Download and extract the preserved ZIP.
2. Open ArcGIS Earth.
3. Open **Settings**.
4. Open **Advanced application settings**.
5. Enable **Automation API**.
6. Leave ArcGIS Earth running.
7. Run `Run_AE_PRAVE_SELF_TEST.bat` if desired.
8. Run `Run_AE_PRAVE_LIVE_v0_1_0_TEST.bat` for the live serial path.

## RSSI icon family

```text
firetruck_rssi_unknown.png
firetruck_rssi_1.png
firetruck_rssi_2.png
firetruck_rssi_3.png
firetruck_rssi_4.png
firetruck_rssi_5.png
```

Thresholds in the proven implementation:

```text
blank / invalid   unknown
< -110 dBm        1 bar
-110 .. -101      2 bars
-100 .. -91       3 bars
-90 .. -81        4 bars
>= -80 dBm        5 bars
```

## Product boundary

PRAVE Live is independent of map manufacturing:

```text
Offline Map Factory → prepared local basemap
PRAVE Live          → live remote units
ArcGIS Earth        → one operational view
```

That separation is intentional. The map remains available offline whether PRAVE is running or not, and PRAVE does not need to become a GIS renderer.

For the deeper engineering record, see **[PRAVE → ArcGIS Earth Integration](https://github.com/Jim-dc95811/Offline-GeoStack/blob/main/docs/PRAVE_ARCGIS_EARTH_INTEGRATION.md)** in Offline GeoStack.

---

**Prepared geography underneath. Live field units on top.**