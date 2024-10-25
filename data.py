import streamlit as st
import pandas as pd
import numpy as np

# Header
st.header("Menampilkan Data")

# buat data

# contoh membuat data array
a = np.array([1,2,3,4])
b = np.array([(1.2,1,2.2),(1.1,2,2.2)],dtype=np.float)

# membuat data series
u = pd.series([1,2,3,4,5,6,7])

# Cara mengambil dataset dari github

datset = pd.read_csv