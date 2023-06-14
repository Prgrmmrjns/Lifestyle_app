import streamlit as st
from init import *
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# User login
with st.expander('Login'):
    name, authentication_status, username = authenticator.login('Login', 'main')


if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.title(':female-scientist: Lifestyle Assistent')
    get_user_data(username)
    st.write(f"Hallo {st.session_state['name']}.")
    
elif authentication_status is False or None:
    st.error('Benutzername oder Passwort ist falsch.')
    