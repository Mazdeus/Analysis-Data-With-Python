import streamlit as st
import pandas as pd

st.write(pd.DataFrame({
    'c1': [1, 2, 3],
    'c2': [4, 5, 6],
    'c3': [7, 8, 9]
}))