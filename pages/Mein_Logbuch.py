import streamlit as st
import datetime

st.title('Mein Logbuch')
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