import cv2
import streamlit as st
import numpy as np

def run(image):
    """Efek emboss."""
    st.sidebar.write("Emboss")
    kernel = np.array([[-2,-1,0],[-1,1,1],[0,1,2]], dtype=np.float32)
    emboss = cv2.filter2D(image, -1, kernel)
    return cv2.add(emboss, 128)