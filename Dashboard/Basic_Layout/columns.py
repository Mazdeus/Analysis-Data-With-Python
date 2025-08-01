import streamlit as st

st.title('Belajar Columns')
# col1, col2, col3 = st.columns(3)

# Mengatur ukuran dari kolom
col1, col2, col3 = st.columns([1, 2, 3])

with col1:
    st.header('Kolom 1')
    st.image("https://static.streamlit.io/examples/cat.jpg")
    
with col2:
    st.header('Kolom 2')
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header('Kolom 3')
    st.image("https://static.streamlit.io/examples/owl.jpg")