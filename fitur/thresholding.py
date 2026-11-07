import cv2
import streamlit as st

def run(image):
    """Thresholding biner sederhana."""
    st.sidebar.write("Thresholding")
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    T = st.sidebar.slider("Threshold (T)", 0, 255, 127)
    _, thresh = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)
    return cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)