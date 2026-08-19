# URL QR Maker v0.1.0

**Status: BUILT / SELF-TESTED**

URL QR Maker is a small offline Windows utility for turning an exact URL into a QR code without using a website or cloud service.

```text
exact URL
→ URL QR Maker
→ SVG QR code
→ matching TXT record of encoded URL
```

## Why it belongs here

QR Command Bridge is not only a receiver. Sometimes the operator needs to manufacture a clean QR payload locally—for example an ArcGIS Earth service URL, local map-fountain URL, documentation link, or other exact endpoint.

This tool does that job without sending the URL to a third-party QR website.

## Operation

1. Double-click `START URL QR MAKER.bat`.
2. Paste the exact URL.
3. Give the QR a short name.
4. Choose a save folder.
5. Click **MAKE QR**.

Output:

```text
<name>_YYYYMMDD_HHMMSS.svg
<name>_YYYYMMDD_HHMMSS.txt
```

The SVG opens in the default browser after creation. The TXT file preserves the exact encoded URL for verification.

## Offline behavior

The original portable package bundles the Python `qrcode` library locally, so the tool does not require Internet access to generate the QR.

The core source and launcher are published in this folder for inspection. The preserved original portable archive is:

```text
URL_QR_MAKER_v0_1_0.zip
size: 128,299 bytes
SHA-256: f2f31ee0e12502734f46a6671516f6ce093e7d2b5b41dbaeb17cab2db5f97033
```

The original archive also contains the bundled `qrcode` package and its license. Do not reconstruct a different ZIP from this folder and call it the original archive.

## Boundary

URL QR Maker **creates** QR codes. QR Command Bridge **reads and interprets** QR codes. Those are separate jobs, and keeping them separate makes both tools easier to understand.
