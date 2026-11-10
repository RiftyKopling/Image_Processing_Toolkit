
# Image Processing Toolkit

Aplikasi pengolahan citra digital berbasis Python, Streamlit, dan OpenCV. Aplikasi menyediakan 15 fitur pengolahan citra dengan antarmuka sederhana, dilengkapi visualisasi citra asli, citra hasil, histogram, dan fitur download hasil dalam format PNG.

## 1. Persyaratan Sistem

Pastikan perangkat sudah memiliki:

- Python 3.10 atau lebih baru.
- pip (Python Package Installer).
- Visual Studio Code (opsional).
- Browser seperti Google Chrome atau Microsoft Edge.

## 2. Struktur Proyek

Pastikan struktur folder proyek seperti berikut:

```text
Image_Processing_Toolkit/
│
├── app.py
├── utils.py
├── requirements.txt
│
└── fitur/
    ├── __init__.py
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

## 3. Membuka Direktori Proyek

Buka terminal VS Code, kemudian arahkan ke direktori proyek:

```powershell
cd "D:\Kuliah Semester 5\PengolahanCitra\Image_Processing_Toolkit"
```

## 4. Membuat Virtual Environment

Virtual environment digunakan untuk memisahkan library proyek dari instalasi Python global.

Buat virtual environment dengan perintah:

```powershell
python -m venv .venv
```

Aktifkan virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Jika berhasil, terminal akan menampilkan awalan `(.venv)`.

Contoh:

```text
(.venv) PS D:\Kuliah Semester 5\PengolahanCitra\Image_Processing_Toolkit>
```

Jika virtual environment sudah tersedia, tidak perlu membuatnya kembali. Cukup aktifkan.

## 5. Konfigurasi Requirements

Buat atau buka file `requirements.txt`, kemudian masukkan library berikut:

```text
streamlit
opencv-python-headless
numpy
matplotlib
```

Keterangan:

| Library | Fungsi |
|---|---|
| Streamlit | Membuat antarmuka aplikasi web |
| OpenCV | Melakukan pemrosesan citra digital |
| NumPy | Operasi array dan matriks |
| Matplotlib | Membuat visualisasi histogram |

## 6. Instalasi Library

Perbarui pip terlebih dahulu:

```powershell
python -m pip install --upgrade pip
```

Kemudian instal seluruh library dari `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
```

Tunggu sampai proses instalasi selesai.

## 7. Verifikasi Instalasi

Pastikan seluruh library berhasil terpasang dengan menjalankan:

```powershell
python -c "import streamlit, cv2, numpy, matplotlib; print('Streamlit:', streamlit.__version__); print('OpenCV:', cv2.__version__); print('NumPy:', numpy.__version__); print('Matplotlib:', matplotlib.__version__)"
```

Jika berhasil, terminal akan menampilkan versi masing-masing library tanpa pesan error.

## 8. Menjalankan Aplikasi

Pastikan virtual environment sudah aktif dan terminal berada di direktori utama proyek.

Jalankan aplikasi menggunakan perintah:

```powershell
streamlit run app.py
```

Setelah berhasil, Streamlit akan menampilkan alamat aplikasi:

```text
Local URL: http://localhost:8501
```

Buka alamat tersebut melalui browser:

http://localhost:8501

Aplikasi pengolahan citra siap digunakan.

## 9. Menggunakan Aplikasi

Langkah penggunaan aplikasi:

1. Upload gambar dengan format JPG atau PNG.
2. Pilih salah satu dari 15 fitur pengolahan citra melalui sidebar.
3. Atur parameter pengolahan jika fitur menyediakan slider atau pilihan.
4. Amati perbandingan citra asli dan citra hasil.
5. Perhatikan histogram untuk melihat distribusi intensitas piksel.
6. Klik tombol **Simpan Hasil** untuk mengunduh hasil pengolahan dalam format PNG.

## 10. Menghentikan Aplikasi

Untuk menghentikan aplikasi, kembali ke terminal dan tekan:

```text
Ctrl + C
```

Untuk menjalankan aplikasi kembali, gunakan:

```powershell
streamlit run app.py
```

Tidak perlu menginstal ulang library setiap kali aplikasi dijalankan.

## 11. Daftar Fitur

Aplikasi menyediakan 15 fitur pengolahan citra:

| No. | Fitur | Fungsi |
|---|---|---|
| 1 | Grayscale | Mengubah citra berwarna menjadi keabuan |
| 2 | Brightness | Mengatur tingkat kecerahan citra |
| 3 | Contrast | Mengatur tingkat kontras citra |
| 4 | Negative | Membalik nilai intensitas piksel |
| 5 | Thresholding | Mengubah citra menjadi biner berdasarkan ambang batas |
| 6 | Thresholding Double | Memisahkan intensitas berdasarkan dua ambang batas |
| 7 | Noise | Menambahkan Gaussian Noise atau Salt & Pepper |
| 8 | Smoothing | Mengurangi noise menggunakan Mean, Gaussian, atau Median Filter |
| 9 | Sharpening | Mempertajam detail citra |
| 10 | Edge Detection | Mendeteksi tepi menggunakan Sobel, Prewitt, Roberts, Laplacian, dan Canny |
| 11 | Emboss | Memberikan efek timbul pada citra |
| 12 | Convolution | Melakukan operasi konvolusi menggunakan kernel |
| 13 | Equalization | Meningkatkan pemerataan distribusi intensitas histogram |
| 14 | Mirroring | Membalik citra secara horizontal atau vertikal |
| 15 | Rotation | Memutar citra berdasarkan sudut tertentu |

## 12. Teknologi yang Digunakan

- Python
- Streamlit
- OpenCV
- NumPy
- Matplotlib

## Catatan

- Setiap fitur memiliki file Python tersendiri di dalam folder `fitur/`.
- Setiap fitur menggunakan satu fungsi utama bernama `run(image)`.
- Algoritma pengolahan citra menggunakan fungsi OpenCV.
- NumPy digunakan untuk kebutuhan array dan matriks dasar.
- Histogram ditampilkan menggunakan Matplotlib.
- Hasil pengolahan dapat diunduh dalam format PNG.
- File `__pycache__` dan bytecode Python tidak perlu dimasukkan ke repository Git.
