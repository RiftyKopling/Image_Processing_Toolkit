import cv2
import streamlit as st
import numpy as np

def run(image):
    """Tambahkan noise Gaussian atau Salt & Pepper."""
    st.sidebar.write("Noise")
    tipe = st.sidebar.selectbox("Tipe Noise", ["Gaussian", "Salt & Pepper"])
    intensitas = st.sidebar.slider("Intensitas", 0.0, 1.0, 0.1)

    if tipe == "Gaussian":
        noise = np.zeros(image.shape, np.int16)
        cv2.randn(noise, 0, 255 * intensitas)
        noise = noise.astype(np.uint8)
        return cv2.add(image, noise)
    else:
        # Salt & Pepper
        out = image.copy()
        h, w = image.shape[:2]
        num_salt = int(h * w * intensitas / 2)
        num_pepper = num_salt
        # Salt (putih)
        coords = [np.random.randint(0, i-1, num_salt) for i in (h, w)]
        out[coords[0], coords[1]] = 255
        # Pepper (hitam)
        coords = [np.random.randint(0, i-1, num_pepper) for i in (h, w)]
        out[coords[0], coords[1]] = 0
        return out