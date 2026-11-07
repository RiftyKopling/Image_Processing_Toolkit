import cv2
import streamlit as st

def run(image):
    """Histogram equalization."""
    st.sidebar.write("Equalization")
    if len(image.shape) == 2:
        return cv2.equalizeHist(image)
    # Berwarna: YCrCb
    ycrcb = cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)
    y, cr, cb = cv2.split(ycrcb)
    y_eq = cv2.equalizeHist(y)
    merged = cv2.merge([y_eq, cr, cb])
    return cv2.cvtColor(merged, cv2.COLOR_YCrCb2RGB)