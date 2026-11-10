
import streamlit as st
import cv2
import numpy as np
import importlib
import av
import threading
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_webrtc import webrtc_streamer

st.set_page_config(
    page_title="Kamera Real-Time",
    layout="wide"
)

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

frame_lock = threading.Lock()

latest_frames = {
    "original": None,
    "result": None
}

class DummySidebar:
    def __init__(self, params):
        self.params = params
    def write(self, *args, **kwargs):
        pass
    def slider(self, label, *args, **kwargs):
        if label in self.params:
            return self.params[label]
        if "value" in kwargs:
            return kwargs["value"]
        if len(args) >= 3:
            return args[2]
        return 0
    def selectbox(self, label, options, *args, **kwargs):
        if label in self.params:
            return self.params[label]
        if "index" in kwargs:
            return options[kwargs["index"]]
        return options[0]


class DummyStreamlit:
    def __init__(self, params):
        self.sidebar = DummySidebar(params)

st.title("Pengolahan Citra - Real-Time")

if st.button("Kembali ke Menu"):
    st.switch_page("home.py")

fitur_nama = st.sidebar.selectbox(
    "Pilih Fitur",
    list(FEATURES.keys())
)

st.sidebar.divider()
st.sidebar.subheader("Pengaturan Fitur")

params = {}


if fitur_nama == "Brightness":
    params["Nilai Beta"] = st.sidebar.slider(
        "Nilai Beta", -100, 100, 0
    )
elif fitur_nama == "Contrast":
    params["Alpha (kontras)"] = st.sidebar.slider(
        "Alpha (kontras)", 0.1, 3.0, 1.0
    )
elif fitur_nama == "Convolution":
    params["Kernel"] = st.sidebar.selectbox(
        "Kernel",
        ["Identity", "Box Blur", "Sharpen", "Edge"]
    )
elif fitur_nama == "Edge Detection":
    params["Metode"] = st.sidebar.selectbox(
        "Metode",
        ["Sobel", "Prewitt", "Roberts", "Laplacian", "Canny"]
    )
    if params["Metode"] == "Canny":
        params["Threshold 1"] = st.sidebar.slider(
            "Threshold 1", 0, 255, 50
        )
        params["Threshold 2"] = st.sidebar.slider(
            "Threshold 2", 0, 255, 150
        )
elif fitur_nama == "Mirroring":
    params["Arah"] = st.sidebar.selectbox(
        "Arah",
        ["Horizontal", "Vertical", "Keduanya"]
    )
elif fitur_nama == "Noise":
    params["Tipe Noise"] = st.sidebar.selectbox(
        "Tipe Noise",
        ["Gaussian", "Salt & Pepper"]
    )
    params["Intensitas"] = st.sidebar.slider(
        "Intensitas", 0.0, 1.0, 0.1
    )
elif fitur_nama == "Rotation":
    params["Sudut (derajat)"] = st.sidebar.slider(
        "Sudut (derajat)", -180, 180, 0
    )
elif fitur_nama == "Smoothing":
    params["Tipe"] = st.sidebar.selectbox(
        "Tipe",
        ["Mean", "Gaussian", "Median"]
    )
    params["Kernel"] = st.sidebar.selectbox(
        "Kernel", [3, 5, 7]
    )
elif fitur_nama == "Thresholding":
    params["Threshold (T)"] = st.sidebar.slider(
        "Threshold (T)", 0, 255, 127
    )
elif fitur_nama == "Thresholding Double":
    params["T1 (batas bawah)"] = st.sidebar.slider(
        "T1 (batas bawah)", 0, 254, 50
    )
    params["T2 (batas atas)"] = st.sidebar.slider(
        "T2 (batas atas)",
        params["T1 (batas bawah)"] + 1,
        255,
        max(200, params["T1 (batas bawah)"] + 1)
    )

mod = importlib.import_module(FEATURES[fitur_nama])
mod.st = DummyStreamlit(params)

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    img = cv2.cvtColor(
        img,
        cv2.COLOR_BGR2RGB
    )
    hasil = mod.run(img)
    hasil = np.asarray(hasil)
    if hasil.ndim == 2:
        hasil = cv2.cvtColor(
            hasil,
            cv2.COLOR_GRAY2RGB
        )
    if hasil.dtype != np.uint8:
        hasil = np.clip(
            hasil, 0, 255
        ).astype(np.uint8)
    with frame_lock:
        latest_frames["original"] = img.copy()
        latest_frames["result"] = hasil.copy()
    hasil_bgr = cv2.cvtColor(
        hasil,
        cv2.COLOR_RGB2BGR
    )
    return av.VideoFrame.from_ndarray(
        hasil_bgr,
        format="bgr24"
    )

st.subheader("Kamera Real-Time")

webrtc_streamer(
    key="image-processing-camera",
    video_frame_callback=video_frame_callback,
    media_stream_constraints={
        "video": True,
        "audio": False
    },
    async_processing=True
)

st.divider()
st.subheader("Histogram Citra")

col1, col2 = st.columns(2)

def tampil_histogram(image, judul):
    if image is None:
        st.info("Menunggu frame kamera...")
        return
    fig, ax = plt.subplots(figsize=(6, 3))
    colors = [
        ("Red", "r"),
        ("Green", "g"),
        ("Blue", "b")
    ]
    for channel, color in enumerate(colors):
        name, plot_color = color
        hist = cv2.calcHist(
            [image],
            [channel],
            None,
            [256],
            [0, 256]
        )
        ax.plot(
            hist,
            color=plot_color,
            label=name
        )
    ax.set_xlim([0, 256])
    ax.set_xlabel("Intensitas Piksel")
    ax.set_ylabel("Jumlah Piksel")
    ax.set_title(judul)
    ax.legend()
    st.pyplot(fig)
    plt.close(fig)

@st.fragment(run_every="1s")
def update_histogram():
    with frame_lock:
        original = latest_frames["original"]
        result = latest_frames["result"]
        if original is not None:
            original = original.copy()
        if result is not None:
            result = result.copy()
    col1, col2 = st.columns(2)
    with col1:
        tampil_histogram(
            original,
            "Histogram Citra Asli"
        )
    with col2:
        tampil_histogram(
            result,
            "Histogram Citra Hasil"
        )

update_histogram()
