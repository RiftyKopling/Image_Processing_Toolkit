import streamlit as st
import cv2
import numpy as np
import importlib
import utils

# Mapping nama fitur ke modul
FEATURES = {
    "Grayscale": "fitur.grayscale",
    "Brightness": "fitur.brightness",
    "Contrast": "fitur.contrast",
    "Negative": "fitur.negative",
    "Thresholding": "fitur.thresholding",
    "Thresholding Double": "fitur.thresholding_double",
    "Noise": "fitur.noise",
    "Smoothing": "fitur.smoothing",
    "Sharpening": "fitur.sharpening",
    "Edge Detection": "fitur.edge_detection",
    "Emboss": "fitur.emboss",
    "Convolution": "fitur.convolution",
    "Equalization": "fitur.equalization",
    "Mirroring": "fitur.mirroring",
    "Rotation": "fitur.rotation",
}

st.set_page_config(page_title="Aplikasi Pengolahan Citra", layout="wide")
st.title("Aplikasi Pengolahan Citra")

# Sidebar: upload & pilih fitur
uploaded = st.sidebar.file_uploader("Upload Gambar", type=["png", "jpg", "jpeg"])
fitur_nama = st.sidebar.selectbox("Pilih Fitur", list(FEATURES.keys()))

if uploaded is None:
    st.info("Silakan upload gambar")
    st.stop()

# Baca gambar
file_bytes = np.frombuffer(uploaded.read(), np.uint8)
img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Jalankan fitur
mod = importlib.import_module(FEATURES[fitur_nama])
hasil = mod.run(img)

# Tampilkan dua kolom
col1, col2 = st.columns(2)

with col1:
    st.subheader("Citra Asli")
    st.image(img, width="stretch")
    utils.tampil_histogram(img)

with col2:
    st.subheader("Citra Hasil")
    st.image(hasil, width="stretch")
    utils.tampil_histogram(hasil)

# Tombol simpan
png_bytes = utils.ke_png_bytes(hasil)
st.download_button(
    "Simpan Hasil",
    data=png_bytes,
    file_name=f"hasil_{fitur_nama.lower().replace(' ', '_')}.png",
    mime="image/png"
)