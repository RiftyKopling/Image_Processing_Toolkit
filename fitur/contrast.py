import cv2
import streamlit as st

def run(image):
    """Ubah kontras citra."""
    st.sidebar.write("Contrast")
    alpha = st.sidebar.slider("Alpha (kontras)", 0.1, 3.0, 1.0)
    return cv2.convertScaleAbs(image, alpha=alpha, beta=0)