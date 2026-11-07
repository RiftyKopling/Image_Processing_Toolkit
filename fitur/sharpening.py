import cv2
import streamlit as st
import numpy as np

def run(image):
    """Sharpening dengan kernel tajam."""
    st.sidebar.write("Sharpening")
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)