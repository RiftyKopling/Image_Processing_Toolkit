import cv2
import streamlit as st

def run(image):
    """Mengubah citra menjadi grayscale."""
    st.sidebar.write("Grayscale")
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # Kembalikan sebagai 3-channel agar konsisten tampilan
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)