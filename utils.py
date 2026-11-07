import cv2
import numpy as np
import matplotlib.pyplot as plt
import io
import streamlit as st

def tampil_histogram(img):
    """Tampilkan histogram gambar menggunakan matplotlib, mengembalikan figure."""
    # Pastikan gambar dalam format RGB
    if len(img.shape) == 2:
        # Grayscale
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        fig, ax = plt.subplots()
        ax.plot(hist, color='k')
        ax.set_xlim([0, 256])
    else:
        colors = ('r', 'g', 'b')
        fig, ax = plt.subplots()
        for i, col in enumerate(colors):
            hist = cv2.calcHist([img], [i], None, [256], [0, 256])
            ax.plot(hist, color=col)
        ax.set_xlim([0, 256])
    st.pyplot(fig)
    return fig

def ke_png_bytes(img):
    """Encode citra (RGB) ke PNG bytes untuk download."""
    # Konversi ke BGR karena cv2.imencode mengharapkan BGR
    if len(img.shape) == 3:
        img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    else:
        img_bgr = img
    success, buf = cv2.imencode('.png', img_bgr)
    if not success:
        raise RuntimeError('Failed to encode image to PNG')
    return buf.tobytes()