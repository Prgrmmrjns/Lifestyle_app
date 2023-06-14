import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st
import requests

# Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate('firebase_key.json')
    firebase_admin.initialize_app(cred)

db = firestore.client()

def get_user_data(username):
    doc_ref = db.collection('users').document(username)
    doc = doc_ref.get()
    data = doc.to_dict()

    # User data initialization
    if 'username' not in st.session_state:
        st.session_state['username'] = username
    if 'name' not in st.session_state:
        st.session_state['name'] = data['name']
    if 'age' not in st.session_state:
        st.session_state['age'] = data['age']
    if 'gender' not in st.session_state:
        st.session_state['gender'] = data['gender']
    if 'weight' not in st.session_state:
        st.session_state['weight'] = data['weight']
    if 'height' not in st.session_state:
        st.session_state['height'] = data['height']
    if 'nutrition_preference' not in st.session_state:
        st.session_state['nutrition_preference'] = data['nutrition_preference']

    # Goals initialization
    if 'step_count_goal' not in st.session_state:
        st.session_state['step_count_goal'] = 10000
    if 'fitness_goal' not in st.session_state:
        st.session_state['fitness_goal'] = "Fett verlieren"
    if 'bed_time' not in st.session_state:
        st.session_state['bed_time'] = "23:00"
    if 'sleep_duration_goal' not in st.session_state:
        st.session_state['sleep_duration_goal'] = 8.0

    # Lifestyle profile initialization
    if 'bmr' not in st.session_state:
        st.session_state['bmr'] = 2400
    if 'cardio_fitness' not in st.session_state:
        st.session_state['cardio_fitness'] = 82

    if 'stored_meals' not in st.session_state:
        st.session_state['stored_meals'] = ''

    # Storing the chat
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []

# Notion
NOTION_TOKEN = "secret_ACWipYLLkakKzVBGixKUEsaLcQjP8C1xMLuUAIGMztH"
DATABASE_ID = "b75f7a4060254eff93f28888448c0df9"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}
url = "https://api.notion.com/v1/pages"

# Fitbit data
url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
response = requests.post(url, headers=headers)
database_data = response.json()["results"]
step_count_week = []
cals_week = []
sleep_duration_week = []
restless_duration_week = []
start_time_week = []
end_time_week = []
sedentary_week = []
fat_burn_week = []
cardio_week = []
awake_week = []
nutrition_week = []
resting_hr_week = []
for day in database_data[:7]:
    props = day['properties']
    awake = props['Awake']['number']
    resting_hr = props['Resting HR']['number']
    sleep_duration = props['Sleep duration']['number'] / 60
    sedentary = props['Sedentary']['number']
    fat_burn = props['Fat burn']['number']
    cardio = props['Cardio']['number']
    calories = props['Calories']['number']
    step_count = props['Step count']['number']
    restless_duration = props['Restless duration']['number']
    start_time = props['Start time']['rich_text'][0]['text']['content']
    end_time = props['End time']['rich_text'][0]['text']['content']
    nutrition = props['Nutrition']['rich_text'][0]['text']['content']
    
    step_count_week.append(step_count)
    cals_week.append(calories)
    sedentary_week.append(sedentary)
    fat_burn_week.append(fat_burn)
    cardio_week.append(cardio)
    sleep_duration_week.append(sleep_duration)
    restless_duration_week.append(restless_duration)
    start_time_week.append(start_time)
    end_time_week.append(end_time)
    awake_week.append(awake)
    nutrition_week.append(nutrition)
    resting_hr_week.append(resting_hr)

st.session_state["step_count_week"] = step_count_week
st.session_state["cals_week"] = cals_week
st.session_state["sedentary_week"] = sedentary_week
st.session_state["fat_burn_week"] = fat_burn_week
st.session_state["cardio_week"] = cardio_week
st.session_state["sleep_duration_week"] = sleep_duration_week
st.session_state["restless_duration_week"] = restless_duration_week
st.session_state["start_time_week"] = start_time_week
st.session_state["end_time_week"] = end_time_week
st.session_state["nutrition_week"] = nutrition_week
st.session_state["awake_week"] = awake_week
st.session_state["resting_hr_week"] = resting_hr_week
