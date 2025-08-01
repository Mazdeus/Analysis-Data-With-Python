import streamlit as st

# Button
if st.button('Say Hello'):
    st.write('Hello, There!')

# Checkbox
agree = st.checkbox('I agree')

if agree:
    st.write('Well done!')

# Radio Button
genre = st.radio(
    label = "What's your favorite movie genre?",
    options = ('Action', 'Thriller', 'Superhero', 'Comedy', 'Drama'),
    horizontal = False
)

# Select Box
genre = st.selectbox(
    label = "What's your favorite movie genre?",
    options = ('Action', 'Thriller', 'Superhero', 'Comedy', 'Drama'),
)

# Multiselect
genre = st.multiselect(
    label = "What's your favorite movie genre?",
    options = ('Action', 'Thriller', 'Superhero', 'Comedy', 'Drama')
)

# Slider
values = st.slider(
    label = 'Select a range of values',
    min_value = 0,
    max_value = 100,
    value = (0,100)
)

st.write(f'Anda memilih: {values}')