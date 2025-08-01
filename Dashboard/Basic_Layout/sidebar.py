import streamlit as st

st.title('Alo haaaaaa')

with st.sidebar:
    st.text('Ini sidebar')
    
    values = st.slider(
        label = 'Select a range of values',
        min_value = 0,
        max_value = 100,
        value = (0,100)
    )

    st.write('Values : ', values)