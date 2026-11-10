import streamlit as st

st.set_page_config(
    page_title="Aplikasi Pengolahan Citra",
    layout="wide"
)

st.title("Aplikasi Pengolahan Citra")
st.write("Silakan pilih metode pengolahan citra.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Galeri Gambar")
    st.write("Upload gambar dari perangkat untuk diproses.")

    if st.button("Pilih Galeri", use_container_width=True):
        st.switch_page("galery.py")

with col2:
    st.subheader("Kamera Real-Time")
    st.write("Gunakan kamera untuk memproses gambar secara langsung.")

    if st.button("Pilih Real-Time", use_container_width=True):
        st.switch_page("realtime.py")
