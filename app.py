
import streamlit as st

# Daftarkan halaman aplikasi
pages = {
    "Menu Utama": [
        st.Page("home.py", title="Beranda", default=True)
    ],
    "Pengolahan Citra": [
        st.Page("galery.py", title="Galeri Gambar"),
        st.Page("realtime.py", title="Kamera Real-Time")
    ]
}

# Jalankan navigasi
pg = st.navigation(pages)
pg.run()
