import streamlit as st
import datetime

st.title('Mein Logbuch')

with st.expander("Trage deine Daten für heute ein."):
    if st.button("Smartwatch synchronisieren"):
        st.success("Smartwatchdaten für heute synchronisiert.")
    if st.button("Bildschirmzeitdaten synchronisieren"):
        st.success("Bildschirmzeitdaten für heute synchronisiert.")
    exercise_frequency = st.selectbox("Wie viel Wasser hast du heute getrunken?", ["<1 L", "1-1,5 L", "1,5-2 L", ">2 L"])
    hours_of_sleep = st.number_input("Wie viel Alkohol hast du heute getrunken? (Angabe in Menge an 3.5% Bier)", min_value=0, step=1, value=0)
    meals_per_day = st.number_input("How many meals do you have per day?", min_value=0, max_value=10, step=1)
    stress_level = st.slider("Wie gestresst warst du heute (1 - wenig gestresst, 10 - viel gestresst)", min_value=1, max_value=10, value=5)
    tiredness_level = st.slider("Wie müde warst du heute (1 - wenig müde, 10 - sehr müde)", min_value=1, max_value=10, value=5)
    cold_shower = st.checkbox(label="Hast du heute kalt geduscht?")
    st.file_uploader("Lade Bilder deiner Mahlzeiten hier hoch.", accept_multiple_files=True)
        
    if st.button("Daten speichern"):
        st.success("Deine Daten wurden gespeichert!")
        st.session_state['entered_logging_data'] = True


with st.expander("Trage deine Daten für einen vorherigen Tag ein."):
    selected_date = st.date_input("Pick a date", datetime.datetime.today())
    option = st.selectbox("Welche Daten möchtest du eintragen?",
                            ("Mahlzeiten", "Gewohnheiten", "Emotionen"))
    submit = st.button("Auswählen")
    if submit:
        if option == "Mahlzeiten":
            meal = st.text_input(label='Mahlzeit / Getränk')
            unit = st.selectbox('Welche Einheit?',
            options=['Gram', 'Milliliter', 'Stück'])
            if unit == 'Gram':
                number = st.number_input('Wie viel Gram?', step=10)
                amount = f'({number} Gram)'
            elif unit == 'Milliliter':
                number = st.number_input('Wie viel Milliliter?', step=50)
                amount = f'({number} Milliliter)'
            else:
                number = st.number_input('Wie viel Stück?', step=1)
                amount = f'({number} Stück)'
            submit_button = st.button(label='Submit')
            if submit_button:
                added_meal = f' {meal} {amount}, '
                st.session_state.stored_meals = st.session_state.stored_meals + added_meal
                stored_meals_string = f"Mahlzeit(en) am {selected_date}:{st.session_state.stored_meals}"
                st.write(stored_meals_string[:-2])
        elif option == "Gewohnheiten":
            pass
        else:
            stress = st.slider(
            'Wie ist dein selbst wahrgenommenes Stresslevel? (0: sehr entspannt, 100: sehr gestresst)',
            0, 100, 50)
            satisfaction = st.slider(
            'Wie zufrieden bist du mit dir?',
            0, 100, 50)