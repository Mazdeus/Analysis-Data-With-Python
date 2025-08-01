import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

with st.container():
    st.write("Inside the container")

    x = np.random.normal(15, 5, 250)

    fig, ax = plt.subplots()
    ax.hist(x, bins=20, color='blue', alpha=0.7)
    st.pyplot(fig)

st.write("Outside the container")