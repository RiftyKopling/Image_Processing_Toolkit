import cv2
import streamlit as st
import numpy as np

def run(image):
    """Smoothing: Mean, Gaussian, Median dengan kernel pilihan."""
    st.sidebar.write("Smoothing")
    tipe = st.sidebar.selectbox("Tipe", ["Mean", "Gaussian", "Median"])
    k = st.sidebar.selectbox("Kernel", [3,5,7])
    if tipe == "Mean":
        return cv2.blur(image, (k,k))
    if tipe == "Gaussian":
        return cv2.GaussianBlur(image, (k,k), 0)
    return cv2.medianBlur(image, k)