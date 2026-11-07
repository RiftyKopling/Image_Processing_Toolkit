import cv2
import streamlit as st

def run(image):
    """Thresholding double (range)."""
    st.sidebar.write("Thresholding Double")
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    T1 = st.sidebar.slider("T1 (batas bawah)", 0, 254, 50)
    T2 = st.sidebar.slider("T2 (batas atas)", T1+1, 255, 200)
    mask = cv2.inRange(gray, T1, T2)
    return cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)