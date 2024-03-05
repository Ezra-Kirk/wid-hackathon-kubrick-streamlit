'''Module containing functions for my streamlit app'''

import streamlit as st

def display_length():
    '''Display length with toast'''
    st.toast(f"Your word is {len(st.session_state.word)} characters long")
    