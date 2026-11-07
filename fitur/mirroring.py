import cv2
import streamlit as st

def run(image):
    """Mirroring (flip) citra."""
    st.sidebar.write("Mirroring")
    mode = st.sidebar.selectbox("Arah", ["Horizontal", "Vertical", "Keduanya"])
    if mode == "Horizontal":
        return cv2.flip(image, 1)
    if mode == "Vertical":
        return cv2.flip(image, 0)
    # Keduanya: flip both axes
    return cv2.flip(image, -1)