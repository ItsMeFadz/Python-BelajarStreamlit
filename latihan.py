import streamlit as st

st.write("""
# Aplikasi luas Segitiga
Ini Adalah aplikasi untuk menghitung luas segitiga sederhana menggunakan streamlit           
""")

alas = st.number_input("Masukan Alas", 0)
tinggi = st.number_input("Masukan Tinggi", 0)
hitung = st.button("Hitung Luas")

if hitung :
    luas = 2 * alas + tinggi
    st.success(f"Luas segitinginya adalah {luas}")
    st.balloons()