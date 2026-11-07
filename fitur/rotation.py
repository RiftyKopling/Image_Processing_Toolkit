import cv2
import streamlit as st

def run(image):
    """Rotasi citra."""
    st.sidebar.write("Rotation")
    angle = st.sidebar.slider("Sudut (derajat)", -180, 180, 0)
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, matrix, (w, h))