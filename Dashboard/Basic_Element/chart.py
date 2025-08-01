import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Membuat data acak dengan distribusi normal (mean=15, std dev=5) sebanyak 250 data
x = np.random.normal(15, 5, 250)

# Membuat figure dan axes untuk grafik menggunakan Matplotlib
fig, ax = plt.subplots()

# Membuat histogram dari data x dengan 15 bin
ax.hist(x=x, bins=15)

# Menampilkan grafik histogram di aplikasi Streamlit
st.pyplot(fig)