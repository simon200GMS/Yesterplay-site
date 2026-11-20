"""Rebuild assets/Yesterplay-Catalog.pdf from catalog/catalog.html.

Usage:  python catalog/build.py ["path/to/Yesterplay Logos.ai"]
Needs Chrome (or Edge) installed; PyMuPDF only when re-exporting wordmarks.
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets", "Yesterplay-Catalog.pdf")

if len(sys.argv) > 1:  # re-export product wordmarks from the logo file (pages 4-6)
    import fitz
    doc = fitz.open(sys.argv[1])
    for page, name in [(3, "wm-tixxo"), (4, "wm-intellect"), (5, "wm-cubit")]:
        r = doc[page]
        svg = r.get_svg_image(text_as_path=True)
        open(os.path.join(HERE, name + ".svg"), "w", encoding="utf-8").write(svg)

# fonts are local static TTFs in catalog/fonts so Chrome embeds real fonts (a web/variable font becomes blurry Type 3)
browsers = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"]
exe = next(b for b in browsers if os.path.exists(b))
src = "file:///" + os.path.join(HERE, "catalog.html").replace("\\", "/")
subprocess.run([exe, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                "--virtual-time-budget=15000", "--run-all-compositor-stages-before-draw",
                f"--print-to-pdf={OUT}", src], check=True)
print("wrote", OUT, os.path.getsize(OUT) // 1024, "KB")

# shrink: Chrome embeds images at full resolution; recompress to print-friendly 150 dpi
import fitz
doc = fitz.open(OUT)
doc.rewrite_images(dpi_threshold=170, dpi_target=150, quality=82, lossy=True, lossless=True, bitonal=False, color=True, gray=True)
tmp = OUT + ".tmp"
doc.save(tmp, garbage=4, deflate=True, clean=True)
doc.close()
os.replace(tmp, OUT)
print("compressed", os.path.getsize(OUT) // 1024, "KB")
