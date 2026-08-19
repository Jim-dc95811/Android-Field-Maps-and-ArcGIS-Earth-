# QR Command Bridge — Optical Command and Dispatch Input

**Status: LIVE-PROVEN FOUNDATION / COMMAND EXPANSION DESIGNED**

QR Command Bridge is the optical input branch of the ArcGIS Earth / Windows field system.

It moves small, deliberate payloads from a phone or printed QR card into an offline Windows field computer using only a screen and camera.

```text
phone / printed QR
→ Windows camera
→ QR Command Bridge
→ strict parser / command allowlist
→ ArcGIS Earth action or approved Windows action
```

The original QR receiver lineage was developed against Google Earth Pro. The proven camera, JSON, coordinate, message, and command-recognition work is carried forward. The modern direction is to keep that optical front end and route approved actions into ArcGIS Earth Automation API or explicitly coded Windows functions.

---

## What is already proven

The Gold QR receiver lineage proved:

- Windows camera QR decoding with OpenCV;
- MacroDroid JSON parsing using `name` and `message`;
- direct decimal-coordinate extraction;
- ordinary non-coordinate message display;
- a latched **PIN DROPPED** operator confirmation;
- brighter/darker camera controls and bright-phone-screen decode hardening;
- a strict `GMDS_CMD:<TOKEN>` command format;
- one hard-coded proof command: `GMDS_CMD:TEST`;
- a latched **COMMAND RECEIVED / TEST PASSED** result;
- explicit blocking of command tokens not present in the allowlist.

The command proof did **not** execute Windows commands. That distinction is important.

---

## Safety rule

> **QR text is data, never executable code.**

The proven v1.1.0 command branch uses a hard-coded allowlist. Unknown command tokens are blocked.

The modern branch keeps that rule.

There will be no generic `cmd.exe`, PowerShell, shell-text, Python `eval`, or arbitrary command execution from QR payloads.

A QR may request a named action. The local program decides whether that exact action exists and exactly what code it is allowed to run.

---

## Modern command direction

Candidate user actions include:

```text
SHOW_LAST_GPRMC
RESTART_EARTH
RESTART_PRAVE
RESTART_QR
SHUTDOWN_PC
RESTART_PC
```

ArcGIS Earth-specific actions may use the local Automation API where appropriate.

Windows actions will be individually implemented and allowlisted.

**These actions are design targets unless a later package explicitly proves them.** The only command token proven by the preserved v1.1.0 package is `GMDS_CMD:TEST`.

Destructive commands such as shutdown, restart, reset, or data restoration should use an additional confirmation/interlock rather than one casual scan.

---

## Proven phone-side bridge

The preserved Android / MacroDroid architecture is:

```text
Incoming SMS
→ MacroDroid writes JSON to clipboard
→ operator presses the green widget
→ Clipboard Refresh
→ Generate QR Code from {clipboard}
→ phone displays QR
→ Windows camera decodes it
```

Exact SMS clipboard structure:

```json
{"name":"{sms_name}","message":"{sms_message}"}
```

The original design intentionally used three separate MacroDroid macros:

1. **Blue widget** — static/custom QR text such as `GMDS_CMD:TEST`.
2. **Green widget** — clipboard refresh → clipboard-to-QR display.
3. **Incoming SMS capture** — writes sender/name and message into clipboard JSON.

That separation was deliberate and should not be collapsed without a new reason and new testing.

---

## Preserved evidence

The exact Gold package identities, byte sizes, SHA-256 hashes, version boundaries, MacroDroid configuration record, and command-proof history are recorded here:

**[Evidence and Lineage](EVIDENCE_AND_LINEAGE.md)**

The canonical binary archives remain preserved in the project archive rather than being reconstructed or altered for this page.

---

## Relationship to PRAVE Live

These are separate user features that meet in the same operational viewer:

```text
PRAVE Live
→ remote radio units

QR Command Bridge
→ dispatch coordinates / messages / approved commands

ArcGIS Earth
→ operational map and local API target
```

Neither feature needs to become the map renderer. Offline Map Factory supplies the prepared geography.

---

## Why QR remains valuable

The optical bridge can move a small command or dispatch payload without requiring the Windows field computer and the phone to share:

- Wi-Fi;
- Bluetooth;
- USB data;
- an account;
- a cloud service;
- public Internet connectivity.

That makes QR useful as a deliberately narrow air-gap-friendly input path rather than merely a novelty barcode reader.

---

## Evidence discipline

Use these labels literally:

- Camera / QR decode: **LIVE-PROVEN lineage**.
- SMS JSON → QR phone workflow: **LIVE-PROVEN lineage**.
- Coordinate pin-drop path in the original Google Earth receiver: **LIVE-PROVEN lineage**.
- `GMDS_CMD:TEST` recognition + allowlist blocking: **LIVE-PROVEN command proof**.
- ArcGIS Earth Automation API command actions: **DESIGNED / NOT YET LIVE-PROVEN in this QR branch**.
- Windows restart/shutdown/recovery actions: **DESIGNED / NOT YET LIVE-PROVEN**.

Do not promote a planned command merely because the command name exists in documentation.

---

**Phone or card shows the code. Windows accepts only the actions we explicitly permit.**
