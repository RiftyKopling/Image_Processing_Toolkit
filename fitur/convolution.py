import cv2
import streamlit as st
import numpy as np

def run(image):
    """Konvolusi dengan preset kernel."""
    st.sidebar.write("Convolution")
    preset = st.sidebar.selectbox("Kernel", ["Identity", "Box Blur", "Sharpen", "Edge"])

    kernels = {
        "Identity": np.array([[0,0,0],[0,1,0],[0,0,0]], dtype=np.float32),
        "Box Blur": np.ones((3,3), dtype=np.float32) / 9,
        "Sharpen": np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], dtype=np.float32),
        "Edge": np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]], dtype=np.float32),
    }
    return cv2.filter2D(image, -1, kernels[preset])