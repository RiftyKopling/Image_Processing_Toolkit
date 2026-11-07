import cv2
import streamlit as st
import numpy as np

def run(image):
    """Deteksi tepi: Sobel, Prewitt, Roberts, Laplacian, Canny."""
    st.sidebar.write("Edge Detection")
    tipe = st.sidebar.selectbox("Metode", ["Sobel", "Prewitt", "Roberts", "Laplacian", "Canny"])
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    if tipe == "Sobel":
        gx = cv2.Sobel(gray, cv2.CV_16S, 1, 0, ksize=3)
        gy = cv2.Sobel(gray, cv2.CV_16S, 0, 1, ksize=3)
        gx = cv2.convertScaleAbs(gx)
        gy = cv2.convertScaleAbs(gy)
        edge = cv2.addWeighted(gx, 0.5, gy, 0.5, 0)

    elif tipe == "Prewitt":
        kx = np.array([[-1,0,1],[-1,0,1],[-1,0,1]], dtype=np.float32)
        ky = np.array([[-1,-1,-1],[0,0,0],[1,1,1]], dtype=np.float32)
        gx = cv2.filter2D(gray, cv2.CV_16S, kx)
        gy = cv2.filter2D(gray, cv2.CV_16S, ky)
        gx = cv2.convertScaleAbs(gx)
        gy = cv2.convertScaleAbs(gy)
        edge = cv2.addWeighted(gx, 0.5, gy, 0.5, 0)

    elif tipe == "Roberts":
        kx = np.array([[1,0],[0,-1]], dtype=np.float32)
        ky = np.array([[0,1],[-1,0]], dtype=np.float32)
        gx = cv2.filter2D(gray, cv2.CV_16S, kx)
        gy = cv2.filter2D(gray, cv2.CV_16S, ky)
        gx = cv2.convertScaleAbs(gx)
        gy = cv2.convertScaleAbs(gy)
        edge = cv2.addWeighted(gx, 0.5, gy, 0.5, 0)

    elif tipe == "Laplacian":
        lap = cv2.Laplacian(gray, cv2.CV_16S, ksize=3)
        edge = cv2.convertScaleAbs(lap)

    else:  # Canny
        t1 = st.sidebar.slider("Threshold 1", 0, 255, 50)
        t2 = st.sidebar.slider("Threshold 2", 0, 255, 150)
        edge = cv2.Canny(gray, t1, t2)

    return cv2.cvtColor(edge, cv2.COLOR_GRAY2RGB)