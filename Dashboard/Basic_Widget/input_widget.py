import streamlit as st

# 1. Teks Input
name = st.text_input(label = "Nama Lengkap", value = '')
st.write('Nama : ', name)

# 2. Teks Area
text = st.text_area('Feedback')
st.write('Feedback : ', text)

# 3. Number Input
number =  st.number_input(label = "Umur")
st.write('Umur : ', int(number), 'tahun')

# 4. Date Input
import datetime

date  = st.date_input(label = "Tanggal lahir", min_value = datetime.date(1900, 1, 1))
st.write('Tanggal lahir : ', date)

# 5. File Uploader
import pandas as pd

uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

# 6. Cameera Input
picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)