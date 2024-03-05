import streamlit as st
from utils import funcs

st.markdown('Hello World')

st.text_input(
    label='Enter your word here',       # the text which will appear above the box
    key='word',                         # how it's saved in session_state
    on_change=funcs.display_length,     # callback function
)

# useful to see the session state while developing:
st.session_state
