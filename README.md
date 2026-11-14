# PCD — Transformasi Geometri Citra

Praktikum Pengolahan Citra Digital: implementasi transformasi geometri
pada satu citra (`contoh.jpeg`, 960 x 1280 piksel) menggunakan Python
dan OpenCV.

## Transformasi yang diimplementasikan

- **Translation** — geser tx = 150, ty = 75
- **Scaling** — faktor 0,5 (480 x 640) dan 2 (1920 x 2560)
- **Rotation** — sudut 45°, 90°, dan 180°
- **Horizontal Flip** dan **Vertical Flip**
- **Perspective Transformation** (tambahan)

## Isi repositori

- `contoh.jpeg` — citra asli
- `translation.py` — program Translation
- `scalling.py` — program Scaling
- `rotation.py` — program Rotation
- `flip.py` — program Horizontal Flip dan Vertical Flip
- `perspective.py` — program Perspective Transformation (interaktif)
- `hasil/` — gambar hasil tiap transformasi
- `Laporan_Praktikum_Transformasi_Geometri_Syarifudin.docx` — laporan
  hasil praktikum

## Cara menjalankan

```bash
py -m pip install opencv-python numpy matplotlib pillow
py translation.py
py scalling.py
py rotation.py
py flip.py
```
