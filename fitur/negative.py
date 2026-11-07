import cv2
import streamlit as st

def run(image):
    """Membuat citra negatif (inverted)."""
    st.sidebar.write("Negative")
    return cv2.bitwise_not(image)