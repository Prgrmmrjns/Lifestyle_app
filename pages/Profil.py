import streamlit as st
from init import db

# Profile
st.title("Mein Profil")
st.write("Füge deine Profildaten hinzu oder bearbeite sie.")

new_name = st.text_input("Name:", value=st.session_state['name'])
new_age = st.text_input("Alter:", value=st.session_state['age'])
new_gender = st.text_input("Geschlecht:", value=st.session_state['gender'])
new_weight = st.text_input("Gewicht (kg):", value=st.session_state['weight'])
new_height = st.text_input("Größe (cm):", value=st.session_state['height'])
new_nutrition_preference = st.text_input("Ernährungspräferenz:", value=st.session_state['nutrition_preference'])


if st.button("Save"):
    doc_ref = db.collection('users').document(st.session_state['username'])
    if new_name != st.session_state['name']:
        doc_ref.update({'name': new_name})
        st.session_state.name = new_name
    if new_age != st.session_state['age']:
        doc_ref.update({'age': new_age})
        st.session_state.age = new_age
    if new_gender != st.session_state['gender']:
        doc_ref.update({'gender': new_gender})
        st.session_state.gender = new_gender
    if new_weight != st.session_state['weight']:
        doc_ref.update({'weight': new_weight})
        st.session_state.weight = new_weight
    if new_height != st.session_state['height']:
        doc_ref.update({'height': new_height})
        st.session_state.height = new_height
    if new_nutrition_preference != st.session_state['nutrition_preference']:
        doc_ref.update({'nutrition_preference': new_nutrition_preference})
        st.session_state.nutrition_preference = new_nutrition_preference

    st.success("Deine Profildaten wurden erfolgriech geändert.")

st.header("Mein Lifestyle Profil")
st.markdown(f"""**Ruheenergieverbrauch**: Basierend auf deinen Daten wird dein Ruheenergieverbrauch auf **{st.session_state.bmr} kcals** geschätzt.
                Der Ruheenergieverbrauch ist unter anderem abhängig von deinem Alter, Geschlecht, Figur und deiner Körperzusammensetzung.
                Menschen mit einem höheren Ruheenergieverbrauch können mehr kcals zu sich nehmen ohne Gewicht zuzunehmen. 
                Mit dem Alter verlangsamt sich dein Stoffwechsel und der Ruheenergieverbrauch sinkt.""")
st.markdown(f"""**Herzgesundheit**: Deine Herzgesundheit liegt bei  **{st.session_state.cardio_fitness}**.
                Ein hoher Score bedeutet zeugt von einem gesunden und leistungsfähigem Herzen (Score reicht von 0 bis 100).
                Der Herzgesundheitsscore ist abhängig von deiner Ruheherzfrequenz, deiner Ernährung und deiner physikalischen Aktivität.
                Bleibe in Bewegung, vermeide Stress und hab ausreichend Schlaf, um deine Herzgesundheit zu steigern.""")
