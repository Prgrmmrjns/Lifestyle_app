import streamlit as st
st.title("Meine Ziele und Meilensteine")
st.write("Definiere deine Ziele rundum einen gesunden Lifestyle oder bearbeite sie.")
st.markdown("**Allgemeine Ziele**")
fitness_goal = st.selectbox(
    'Was ist dein Fitnessziel?',
    ('Fett verlieren', 'Muskeln aufbauen', 'Ausdauer verbessern', 'Etwas anderes'))
if fitness_goal == 'Etwas anderes':
        fitness_goal = st.text_area("Formuliere dein Fitnessziel:", height = 100)

st.write("**Ziele rundum meine physikalische Aktivität**")
step_count_goal = st.number_input(label='Tagesschrittziel:', value=10000, step=500)

st.write("**Ziele rundum meinen Schlaf**")
bed_time = st.text_input("Wann möchtest du zu Bett gehen?")
sleep_duration_goal = st.number_input(label='Wie lange möchtest du schlafen?', value=8.0, step=0.5)

save_button = st.button("Save")

if save_button:
    st.session_state.step_count_goal = step_count_goal
    st.session_state.fitness_goal = fitness_goal
    st.session_state.bed_time = bed_time
    st.session_state.sleep_duration_goal = sleep_duration_goal
    st.success("Deine Lifestyleziele wurden erfolgreich geändert.")

st.title("Meine Meilensteine")
st.markdown(":hiking_boot: **Wochen-Wanderer**: Lege 100000 Schritte in einer Woche zurück (Freigeschaltet am 05.05.2023)")
st.markdown(":bear: **Schlafnasenbär**: Gehe eine ganze Woche ununterbrochen rechtzeitig zu Bett (Freigeschaltet am 08.05.2023)")
