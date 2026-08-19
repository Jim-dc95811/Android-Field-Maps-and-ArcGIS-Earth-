# Android Phone FireTextSender — Origin of the QR Dispatch Lineage

This is the dispatch-side precursor that led into the later SMS → MacroDroid → QR optical bridge.

Before the QR receiver existed, the project had already solved a key operational problem: take a location selected on a Windows dispatch computer and push it through a connected Android phone as a ready-to-send SMS.

```text
Windows Google Maps
→ copy decimal coordinates
→ FireTextSender
→ ADB over USB
→ Android SMS composer
→ field recipient
```

That established the phone as a deliberate bridge between a Windows field/dispatch computer and ordinary cellular messaging.

The later QR branch turned the flow around on the receiving side:

```text
incoming SMS on Android
→ MacroDroid clipboard JSON
→ QR on phone screen
→ Windows camera
→ QR receiver
→ coordinate / message / command parser
```

That is why FireTextSender belongs in the QR Command Bridge history even though it does not itself generate QR codes.

## Original package

Preserved archive:

```text
Android Phone FireTextSender.zip
size: 3,375,142 bytes
SHA-256: 4a7990644f0da321f259e977ef16c7f20f45bb0ec2159df89afcb3abc541cf07
```

The package includes the desktop-button sender, instructions, test variants, and visual workflow records.

Notable files include:

```text
Fire_Location_Sender_Desktop_Button_Instructions.pdf
Fire_Text_Sender_v1_Instructions.pdf
send_location.py
send_location.pyw
send_locationOG.py
send_location_group_test_v6.py
Jax_24.bat
Jax_24Invisible.bat
Google Maps Link Cell Phone Texter.png
Pushing Address Using Cellular without Tracking.png
```

## Operator model

The mature desktop-button workflow was intentionally simple:

1. Click a unit button.
2. Copy the desired decimal coordinate pair from Google Maps.
3. The Windows script detects the clipboard coordinates.
4. It builds a timestamped Google Maps location message.
5. ADB opens the SMS composer on the USB-connected Android phone.
6. The phone sends or presents the message for final send, depending on the tested mode.

The design target was one unit / one desktop button / one phone number so the dispatcher did not have to type or format a message under stress.

## Why the raw ZIP is not mirrored publicly here

The original archive contains deployment-specific phone numbers and machine paths. Those details are useful historical evidence but are not appropriate to dump onto a public repository by accident.

The exact original ZIP remains preserved in the canonical project archive under the SHA-256 above.

If a sanitized public source package is ever desired, build it as a clearly new derivative and do not relabel it as the untouched original.

## Lineage

```text
FireTextSender
→ phone becomes dispatch bridge
→ SMS carries coordinates
→ MacroDroid captures incoming SMS
→ QR becomes optical courier
→ Windows QR receiver decodes coordinates/messages
→ strict QR command proof
→ modern QR Command Bridge
```

This is the beginning of the branch, not obsolete clutter. It explains why the later QR system exists and what operational problem it was originally solving.
