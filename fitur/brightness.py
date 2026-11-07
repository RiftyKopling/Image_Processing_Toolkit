import cv2
import streamlit as st
import numpy as np

def run(image):
    """Mengubah kecerahan citra."""
    st.sidebar.write("Brightness")
    beta = st.sidebar.slider("Nilai Beta", -100, 100, 0)
    return cv2.convertScaleAbs(image, alpha=1, beta=beta)