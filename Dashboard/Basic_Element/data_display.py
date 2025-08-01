# Digunakan untuk menampilkan data pada dashboard secara cepat dan interaktif
# dataframe(), table(), metric(), json(),  dll

# metric()
import streamlit as st

st.metric(label = "Temperature", value = "20 °C", delta = "1.5 °C")