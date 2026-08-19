#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import re
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk
import webbrowser

import qrcode
import qrcode.image.svg

APP = "URL QR MAKER"
VERSION = "v0.1.0"


def safe_file_stem(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9._-]+", "_", text.strip())
    text = re.sub(r"_+", "_", text).strip("._-")
    return text or "QR"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(f"{APP} {VERSION}")
        self.geometry("820x350")
        self.minsize(760, 330)

        self.url_var = tk.StringVar()
        self.name_var = tk.StringVar(value="QR")
        self.out_var = tk.StringVar(value=str(Path.home() / "Desktop"))
        self.status_var = tk.StringVar(
            value="Paste or type the exact URL. The generated QR is completely offline."
        )

        self._build()

    def _build(self):
        frame = ttk.Frame(self, padding=18)
        frame.pack(fill="both", expand=True)
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text=APP, font=("Segoe UI", 20, "bold")).grid(
            row=0, column=0, columnspan=3, sticky="w", pady=(0, 16)
        )

        ttk.Label(frame, text="Exact URL").grid(row=1, column=0, sticky="w", pady=6)
        ttk.Entry(frame, textvariable=self.url_var).grid(
            row=1, column=1, sticky="ew", padx=8, pady=6
        )
        ttk.Button(frame, text="PASTE", command=self.paste_url).grid(
            row=1, column=2, pady=6
        )

        ttk.Label(frame, text="QR name").grid(row=2, column=0, sticky="w", pady=6)
        ttk.Entry(frame, textvariable=self.name_var, width=28).grid(
            row=2, column=1, sticky="w", padx=8, pady=6
        )

        ttk.Label(frame, text="Save folder").grid(row=3, column=0, sticky="w", pady=6)
        ttk.Entry(frame, textvariable=self.out_var).grid(
            row=3, column=1, sticky="ew", padx=8, pady=6
        )
        ttk.Button(frame, text="BROWSE", command=self.choose_folder).grid(
            row=3, column=2, pady=6
        )

        ttk.Button(
            frame,
            text="MAKE QR",
            command=self.make_qr,
        ).grid(row=4, column=1, sticky="ew", padx=8, pady=(18, 10))

        ttk.Label(
            frame,
            textvariable=self.status_var,
            wraplength=740,
            justify="left",
        ).grid(row=5, column=0, columnspan=3, sticky="w", pady=(8, 0))

    def paste_url(self):
        try:
            text = self.clipboard_get().strip()
        except Exception:
            messagebox.showwarning(APP, "Clipboard does not contain text.")
            return
        self.url_var.set(text)
        if text:
            self.status_var.set(f"Loaded URL:\n{text}")

    def choose_folder(self):
        folder = filedialog.askdirectory(initialdir=self.out_var.get())
        if folder:
            self.out_var.set(folder)

    def make_qr(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning(APP, "Enter a URL first.")
            return

        out_dir = Path(self.out_var.get()).expanduser()
        if not out_dir.is_dir():
            messagebox.showerror(APP, "Choose an existing save folder.")
            return

        stem = safe_file_stem(self.name_var.get())
        stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
        svg_path = out_dir / f"{stem}_{stamp}.svg"
        txt_path = out_dir / f"{stem}_{stamp}.txt"

        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(image_factory=qrcode.image.svg.SvgPathImage)
        with open(svg_path, "wb") as f:
            img.save(f)

        txt_path.write_text(url + "\n", encoding="utf-8")

        self.status_var.set(
            f"COMPLETE\nQR: {svg_path}\nURL copy: {txt_path}\nEncoded URL:\n{url}"
        )

        try:
            webbrowser.open(svg_path.as_uri())
        except Exception:
            pass

        messagebox.showinfo(
            APP,
            f"QR created.\n\n{svg_path}\n\nEncoded URL:\n{url}"
        )


if __name__ == "__main__":
    App().mainloop()
