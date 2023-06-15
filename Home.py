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

with st.expander("Registrieren"):
    try:
        if authenticator.register_user('Registrieren', preauthorization=False):
            st.success('Du wurdest erfolgreich registriert. Melde dich über Login an.')
            authentication_status = True
            with open('config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
    except Exception as e:
        st.error(e)

# User login
with st.expander('Login'):
    name, authentication_status, username = authenticator.login('Login', 'main')


if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.title(':female-scientist: Lifestyle Assistent')
    get_user_data(username)
    st.write(f"Hallo {st.session_state['name']}.")

    # check if user submitted daily logging data
    if not st.session_state['entered_logging_data']:
        st.write("Trage deine Daten für heute ein")
    else:
        st.write("Super. Du hast deine Daten für heute eingetragen.")
    
    # check if user participated in daily quiz
    if not st.session_state['quiz_status']:
        st.write("Mache das tägliche Quiz, um dich weiterzubilden und Belohnungen zu bekommen.")
    else:
        st.write(f"Du hast beim heutigem Quiz {round(st.session_state['quiz_score']*100,1)}% aller Fragen richtig beantwortet.")

    # Meilensteine
    st.markdown("Halte dich ran. Du bist auf dem besten Weg den Meilenstein: **🎯 Quizmaster: Absolviere das tägliche Quiz für sieben ununterbrochene Tage** zu erreichen.")
    
elif authentication_status is False or None:
    st.error('Benutzername oder Passwort ist falsch.')
    