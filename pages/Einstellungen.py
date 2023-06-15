import streamlit as st
st.title("Einstellungen")
option = st.selectbox(
    'Sprache',
    options=[
        'Deutsch', 
        'English',
        'Français']
)

st.button("Einstellungen speichern")