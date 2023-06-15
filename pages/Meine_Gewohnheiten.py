import streamlit as st
import pandas as pd

st.title("Meine Gewohnheiten")
st.markdown("""Gewohnheiten sind automatisierte Verhaltensweisen, die erheblichen Einfluss auf unsere Gesundheit haben. 
                Gute Gewohnheiten, wie ausreichend Schlaf und regelmäßige Bewegung, fördern unser Wohlbefinden und stärken unsere Abwehrkräfte. 
                Schlechte Gewohnheiten, wie Rauchen und ungesunde Ernährung, können hingegen zu chronischen Krankheiten führen. 
                Daher ist es entscheidend, gesunde Gewohnheiten zu entwickeln und schädliche Gewohnheiten zu überwinden, um ein langes und gesundes Leben zu führen. """)


chart_data = pd.DataFrame.from_dict(
    {"Kalt duschen":[1, 1, 1, 0, 0, 1, 1], "Morgens laufen gehen": [0, 1, 1, 0, 1, 1, 0], "Um 23:00 schlafen gehen": [1, 0, 0, 0, 0, 0, 1]})

st.bar_chart(chart_data)

with st.expander("Gewohnheiten hinzufügen"):
    custom_habit = st.text_input(label="Füge eine eigene Gewohnheit hinzu")
    suggest_habit_button = st.button("Lass dir basierend auf deinen persönlichen Daten eine Gewohnheit vorschlagen")
    if suggest_habit_button:
        st.write("Selber kochen")
    if st.button("Gewohnheit hinzufügen"):
        st.success("Gewohnheit wurde hinzugefügt.")

with st.expander("Gewohnheit entfernen"):
    if st.button("Kalt duschen") or st.button("Morgens laufen gehen") or st.button("Um 23:00 schlafen gehen"):
        st.success("Gewohnheit wurde entfernt.")



