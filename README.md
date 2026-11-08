# PRD — Aplikasi Pengolahan Citra (Versi Sederhana, Berbasis OpenCV)

## 1. Ringkasan

Aplikasi Streamlit sederhana berisi 15 fitur pengolahan citra. User upload gambar, pilih fitur, atur parameter, lalu melihat **citra asli vs hasil** dan **histogram** keduanya, serta bisa **menyimpan hasil** lewat tombol save. Setiap fitur ada di **satu file Python sendiri**.

**Prinsip utama: kode harus simple, pendek, mudah dibaca, dan seluruh algoritma memakai library OpenCV (`cv2`).**

## 2. Aturan Kode

- Semua algoritma pengolahan citra memakai fungsi **OpenCV** (`cv2.threshold`, `cv2.GaussianBlur`, `cv2.Canny`, `cv2.filter2D`, `cv2.flip`, dst.). Tidak boleh menulis algoritma manual dengan loop piksel.
- NumPy hanya untuk hal dasar (membuat array kernel, indexing sederhana). Tanpa Pillow/scikit-image.
- Tanpa class, decorator, type hints, atau pola desain rumit.
- Satu file fitur maksimal ±30 baris. `app.py` maksimal ±70 baris.
- Satu fungsi per fitur: `run(image)`. Slider/pilihan ditaruh di dalam fungsi itu lewat `st.sidebar`.
- Komentar singkat Bahasa Indonesia di bagian penting saja.
- Helper hanya 1 file: `utils.py` (histogram dan konversi untuk tombol save).

## 3. Struktur Proyek

```
pengolahan_citra/
├── app.py
├── utils.py                 # tampil_histogram(image), ke_png_bytes(image)
├── requirements.txt         # streamlit, opencv-python-headless, numpy, matplotlib
└── fitur/
    ├── grayscale.py
    ├── brightness.py
    ├── contrast.py
    ├── negative.py
    ├── thresholding.py
    ├── thresholding_double.py
    ├── noise.py
    ├── smoothing.py
    ├── sharpening.py
    ├── edge_detection.py
    ├── emboss.py
    ├── convolution.py
    ├── equalization.py
    ├── mirroring.py
    └── rotation.py
```

## 4. Kontrak Setiap File Fitur

```python
import streamlit as st
import cv2

def run(image):
    # image: array RGB uint8
    # tampilkan slider/pilihan di sidebar dengan st.sidebar
    # kembalikan citra hasil (uint8)
    return hasil
```

`app.py` memanggil `hasil = fitur.run(image)` lalu menampilkan hasil, histogram, dan tombol save.

## 5. Daftar Fitur dan Algoritma (OpenCV)

| # | Fitur | Kontrol di sidebar | Fungsi OpenCV |
|---|-------|--------------------|---------------|
| 1 | Grayscale | — | `cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)` |
| 2 | Brightness | slider −100..100 | `cv2.convertScaleAbs(img, alpha=1, beta=nilai)` |
| 3 | Contrast | slider 0.1..3.0 | `cv2.convertScaleAbs(img, alpha=nilai, beta=0)` |
| 4 | Negative | — | `cv2.bitwise_not(img)` |
| 5 | Thresholding | slider T 0..255 | gray lalu `cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)` |
| 6 | Thresholding Double | slider T1 dan T2 (T1 < T2) | gray lalu `cv2.inRange(gray, T1, T2)` |
| 7 | Noise | pilihan Gaussian / Salt & Pepper, slider intensitas | Gaussian: `cv2.randn` + `cv2.add`. Salt & Pepper: `cv2.randu` untuk membuat mask acak, piksel mask diset 0 atau 255 |
| 8 | Smoothing | pilihan Mean / Gaussian / Median, kernel 3/5/7 | `cv2.blur`, `cv2.GaussianBlur`, `cv2.medianBlur` |
| 9 | Sharpening | — | `cv2.filter2D` dengan kernel sharpen `[[0,-1,0],[-1,5,-1],[0,-1,0]]` |
| 10 | Edge Detection | pilihan Sobel / Prewitt / Roberts / Laplacian / Canny | lihat tabel 5a |
| 11 | Emboss | — | `cv2.filter2D` dengan kernel emboss `[[-2,-1,0],[-1,1,1],[0,1,2]]`, lalu tambah offset 128 dengan `cv2.add` |
| 12 | Convolution | pilihan preset kernel (Identity, Box Blur, Sharpen, Edge) | `cv2.filter2D` |
| 13 | Equalization | — | gray: `cv2.equalizeHist`. Berwarna: `cv2.cvtColor` ke YCrCb, `cv2.split`, equalize kanal Y, `cv2.merge`, kembali ke RGB |
| 14 | Mirroring | pilihan Horizontal / Vertical / Keduanya | `cv2.flip(img, 1 / 0 / -1)` |
| 15 | Rotation | slider sudut −180..180 | `cv2.getRotationMatrix2D` + `cv2.warpAffine` |

### 5a. Detail Edge Detection (semua dengan OpenCV)

Citra diubah ke grayscale dulu. Untuk metode berbasis gradien: hitung gradien arah x dan y dengan tipe `cv2.CV_16S`, ubah ke 8-bit dengan `cv2.convertScaleAbs`, lalu gabungkan dengan `cv2.addWeighted(gx, 0.5, gy, 0.5, 0)`.

| Metode | Cara dengan OpenCV |
|--------|--------------------|
| Sobel | `cv2.Sobel(gray, cv2.CV_16S, 1, 0)` dan `cv2.Sobel(gray, cv2.CV_16S, 0, 1)` |
| Prewitt | `cv2.filter2D(gray, cv2.CV_16S, kx)` dan `ky` dengan kernel: `kx = [[-1,0,1],[-1,0,1],[-1,0,1]]`, `ky = [[-1,-1,-1],[0,0,0],[1,1,1]]` |
| Roberts | `cv2.filter2D(gray, cv2.CV_16S, kx)` dan `ky` dengan kernel 2×2: `kx = [[1,0],[0,-1]]`, `ky = [[0,1],[-1,0]]` |
| Laplacian | `cv2.Laplacian(gray, cv2.CV_16S)` lalu `cv2.convertScaleAbs` |
| Canny | `cv2.Canny(gray, low, high)` dengan dua slider threshold |

## 6. Tampilan (app.py)

- Sidebar: upload gambar (jpg/png) dan pilih fitur (`selectbox`). Gambar dibaca dengan `cv2.imdecode` dari bytes upload, lalu `cv2.cvtColor` BGR → RGB.
- Halaman utama: dua kolom.
  - Kiri: "Citra Asli", gambar, histogram.
  - Kanan: "Citra Hasil", gambar, histogram, dan tombol **Simpan Hasil**.
- Histogram dihitung dengan `cv2.calcHist` dan digambar dengan matplotlib: citra gray satu garis; citra berwarna tiga garis R, G, B.
- **Tombol save:** `st.download_button("Simpan Hasil", data, file_name="hasil_<nama_fitur>.png", mime="image/png")`. Data PNG dibuat dengan `cv2.imencode(".png", ...)`; citra berwarna dikonversi RGB → BGR dulu sebelum di-encode.
- Belum upload gambar → tampilkan `st.info("Silakan upload gambar")`.

## 7. Kriteria Penerimaan

- [ ] 15 fitur muncul di pilihan dan berjalan tanpa error.
- [ ] Edge detection menyediakan Sobel, Prewitt, Roberts, Laplacian, dan Canny.
- [ ] Setiap fitur menampilkan citra asli, citra hasil, dan kedua histogram.
- [ ] Tombol Simpan Hasil mengunduh PNG yang sama dengan preview hasil (warna tidak tertukar).
- [ ] Semua algoritma memakai fungsi OpenCV, tanpa loop piksel manual.
- [ ] Setiap fitur ada di file terpisah dengan satu fungsi `run(image)`.
- [ ] Hasil 1 kanal (threshold, edge, grayscale) tampil dan tersimpan dengan benar.
- [ ] `pip install -r requirements.txt` lalu `streamlit run app.py` langsung jalan.

---
