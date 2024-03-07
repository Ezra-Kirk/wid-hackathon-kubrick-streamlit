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

# st.map()

# st.chat_input()

if 'variables' not in st.session_state:
    st.session_state['variables'] = {}


with st.form("my_form"):
   st.write("Inside the form")
   st.text_input("Input some text")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)