# QR Command Bridge — Evidence and Lineage

This file preserves the tested lineage behind the user-facing QR Command Bridge feature.

## Origin before QR — Android Phone FireTextSender

The dispatch-side precursor is preserved as:

```text
Android Phone FireTextSender.zip
size: 3,375,142 bytes
SHA-256: 4a7990644f0da321f259e977ef16c7f20f45bb0ec2159df89afcb3abc541cf07
```

Its core workflow was:

```text
Windows Google Maps
→ copy decimal coordinates
→ FireTextSender
→ ADB over USB
→ Android SMS composer
→ field recipient
```

The mature desktop-button version was deliberately simple: one unit, one button, one phone number. It detected copied decimal coordinates, built a timestamped Google Maps link, and handed the message to a USB-connected Android phone through ADB.

That work established the phone as a controlled bridge between the Windows dispatch computer and ordinary cellular messaging.

The later QR receiver inverted the receiving side:

```text
incoming SMS on Android
→ MacroDroid clipboard JSON
→ QR on phone
→ Windows camera
→ coordinate / message / command parser
```

That is why FireTextSender is the operational ancestor of the QR branch even though it did not itself generate QR codes.

The original FireTextSender archive contains deployment-specific phone numbers and machine paths. Its exact original is therefore preserved in the canonical project archive rather than mirrored raw to the public repository. See [`origins/fire-text-sender/`](origins/fire-text-sender/README.md).

---

## Canonical preserved QR receiver packages

The exact original ZIPs remain preserved in the project archive / canonical Library. Do not reconstruct them from this page and call the result the original package.

### GMDS QR Receiver v1.0 Gold Application

```text
GMDS_QR_Receiver_v1_0_Gold_Application.zip
size: 37,292 bytes
SHA-256: b2d75d2434149935ec4713dc7ba4b10cd0c25629c2a27040c7e53967797f7be5
```

Scope locked to:

- camera QR decode;
- MacroDroid JSON `name` / `message` parsing;
- direct decimal-coordinate extraction;
- local Google Earth Pro pin drop;
- sender/message display when no coordinates are present.

It did not include QR command execution.

### GMDS QR Receiver v1.0.1 Gold Hotfix Tester

```text
GMDS_QR_Receiver_v1_0_1_Gold_Hotfix_Tester.zip
size: 63,585 bytes
SHA-256: adc9b466ae204ffba186ab81d2512be1f3926262bbca1111fd8493519ef9ebe0
```

Live-test hardening added:

- persistent `PIN DROPPED` panel;
- Close / Scan Again controls;
- stronger two-tone acknowledgement;
- Darker / Brighter camera controls;
- correction for over-bright phone displays.

This did not broaden the original Version 1 mission.

### GMDS QR Receiver v1.1.0 Gold Command Proof Tester

```text
GMDS_QR_Receiver_v1_1_0_Gold_Command_Proof_Tester.zip
size: 27,749 bytes
SHA-256: c7659e4ca603ab750276e3d92aacc8b435c8ced51f3a7e85727f7abe9e353a61
```

This branch added the command-channel proof:

```text
GMDS_CMD:<COMMAND>
```

Proven command:

```text
GMDS_CMD:TEST
```

Behavior:

- exact token recognized;
- hard-coded allowlist checked;
- TEST produced a latched command-received / test-passed result;
- unknown command tokens were blocked.

The command proof did **not** execute Windows applications, keystrokes, scripts, shutdown, restart, or shell text.

Core security rule:

> QR text is data, never executable code.

Future functions must be individually named and explicitly implemented.

---

## MacroDroid phone-side archive

Canonical record:

```text
GMDS_MacroDroid_QR_Bridge_Configuration_Archive_2026-07-26.pdf
size: 1,885,589 bytes
SHA-256: 1b16597ea5ae2c5803e7e232d8b5a1d4321acedfc5e0d1916a8069b53185800e
```

It records three intentionally separate Android macros.

### Blue widget — fixed command / custom text

Proven example:

```text
GMDS_CMD:TEST
```

### Green widget — controlled optical release

```text
Clipboard Refresh
→ Generate QR Code from {clipboard}
→ Display QR immediately
```

### Incoming SMS capture

Writes the latest SMS sender/name and message to clipboard as:

```json
{"name":"{sms_name}","message":"{sms_message}"}
```

The operator then chooses when to display that clipboard payload as QR using the green widget.

This separation prevents every incoming text from automatically taking over the phone screen.

---

## New utility — URL QR Maker v0.1.0

The new local QR-generation utility is preserved as:

```text
URL_QR_MAKER_v0_1_0.zip
size: 128,299 bytes
SHA-256: f2f31ee0e12502734f46a6671516f6ce093e7d2b5b41dbaeb17cab2db5f97033
```

Purpose:

```text
exact URL
→ offline local QR generation
→ SVG QR image
→ matching TXT record of exact encoded URL
```

The portable archive bundles the Python `qrcode` library locally and includes its license, so QR generation itself does not require Internet access.

The core source, BAT launcher, self-test record, and third-party license are published under [`tools/url-qr-maker/`](tools/url-qr-maker/README.md).

Status: **BUILT / SELF-TESTED**.

This is a generator utility, not the receiver. It complements QR Command Bridge by creating exact QR payloads locally.

---

## Proven end-to-end lineage

```text
FireTextSender
→ phone becomes dispatch bridge
→ SMS carries coordinates
→ MacroDroid clipboard JSON
→ operator-controlled QR display
→ Windows camera / OpenCV
→ QR decode
→ JSON / coordinate / command parser
→ receiver result
```

Observed/proven behaviors included:

- camera opens;
- QR decodes;
- ordinary non-coordinate SMS displays correctly;
- coordinate SMS produces `PIN DROPPED` and a map pin in the original Google Earth path;
- `GMDS_CMD:TEST` produces a latched successful command result;
- unknown commands are blocked;
- tested Android restart preserved clipboard state and MacroDroid widgets returned usable.

The new URL QR Maker adds the opposite local utility direction:

```text
Windows text / URL
→ local QR generation
→ phone or other camera can scan it
```

---

## Historical command-card ideas — not implementation claims

The project archive records candidate cards/actions such as:

- display latest valid GPRMC coordinates;
- restart the computer;
- shutdown the computer;
- restart the map viewer;
- restart approved Python/helper components;
- restore an approved local map library.

Those were design ideas. They are **not** proven merely because they appear in historical notes.

The modern QR Command Bridge may reuse some of those intents with ArcGIS Earth and current Windows tools, but each action must be individually implemented and tested before its evidence status changes.

---

## Modern migration boundary

What carries forward unchanged:

- optical phone/card → camera transport;
- strict parsing;
- command-token namespace;
- hard-coded allowlist;
- unknown-command blocking;
- operator feedback;
- no public-Internet requirement for the optical hop.

What must earn new proof:

- ArcGIS Earth Automation API actions triggered by QR;
- current Windows restart/shutdown/helper-process actions;
- confirmation/interlock behavior for destructive actions;
- any two-way response-QR / optical-bus implementation.

The old Google Earth KML endpoint is lineage, not the modern target.
