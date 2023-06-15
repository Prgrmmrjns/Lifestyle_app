import streamlit as st
from streamlit_chat import message
import numpy as np
from langchain import OpenAI
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from init import *
import os

os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]

llm = OpenAI(temperature=0.9) 

# Lifestyle tip chain
lifestyle_tip_template = PromptTemplate(
        input_variables = ['name', 'age', 'gender', 'weight', 'nutrition_preference','query'], 
        template='''Du bist ein Chatbot mit dem Namen LiSA. Dein Ziel ist es Lifestyle Tipps zu geben. 
                    Berücksichtige dabei die soziodemographischen Daten, seine Präferenzen und die Anamnese des Users.
                    Der User hat den Namen {name}. Sein Alter ist {age} und sein Geschlecht ist {gender}.
                    Er wiegt {weight} und ernährt sich {nutrition_preference}.
                    Hier ist die Anfrage des Users: {query}'''
)
lifestyle_tip_chain = LLMChain(llm=llm, prompt=lifestyle_tip_template, verbose=True)

# Physical activity data analysis chain
pa_analysis_template = PromptTemplate(
        input_variables = ['name', 'age', 'gender', 'weight', 'step_count_mean','calories_mean', 'sedentary_mean', 'fat_burn_mean', 'cardio_mean', 'step_count_goal', 'fitness_goal'], 
        template='''Du bist ein Chatbot mit dem Namen LiSA. Dein Ziel ist es Lifestyle Tipps zu geben. 
                    Berücksichtige dabei die soziodemographischen Daten, seine Präferenzen und die Anamnese des Users.
                    Der User hat den Namen {name}. Sein Alter ist {age} und sein Geschlecht ist {gender}.
                    Er wiegt {weight}. In den letzten Tagen hat er durchschnittlich {step_count_mean} Schritte am Tag gemacht
                    und durchschnittlich {calories_mean} kalorien am Tag verbrannt.
                    Durchschnittlich hat er pro Tag {sedentary_mean} Minuten mit passiven Tätigkeiten, 
                    {fat_burn_mean} Minuten mit leichter Physikalischer Aktivität und {cardio_mean} Minuten 
                    mit hoher physikalischer Aktivität verbracht.
                    Der User hat folgende Ziele formuliert: mindestens {step_count_goal} Schritte täglich und das Fitnessziel {fitness_goal}.
                    Gib Feedback zu der physikalischen Aktivität des Users und benutze dabei wissenschaftliche Empfehlungen.'''
)
pa_analysis_chain = LLMChain(llm=llm, prompt=pa_analysis_template, verbose=True)

# Sleep data analysis chain
sleep_analysis_template = PromptTemplate(
        input_variables = ['name', 'age', 'gender', 'weight', 'sleep_duration_mean','restless_duration_mean', 'awake_mean', 
                           'start_time_week', 'end_time_week', 'bed_time', 'sleep_duration_goal'], 
        template='''Du bist ein Chatbot mit dem Namen LiSA. Dein Ziel ist es Lifestyle Tipps zu geben. 
                    Berücksichtige dabei die soziodemographischen Daten, seine Präferenzen und die Anamnese des Users.
                    Der User hat den Namen {name}. Sein Alter ist {age} und sein Geschlecht ist {gender}.
                    Er wiegt {weight}. In den letzten Tagen hat er durchschnittlich {sleep_duration_mean} Stunden am Tag geschlafen
                    und hatte dabei durchschnittlich {restless_duration_mean}  Minuten einen unruhigen Schlaf 
                    und war durchschnittlich {awake_mean} Minuten pro Nacht wach. 
                    Er ist zu folgenden Uhrzeiten ins Bett gegangen: {start_time_week}.
                    Er ist zu folgenden Uhrzeiten aus dem Bett aufgestanden: {end_time_week}.
                    Er hat sich als Ziel gesetzt um um {bed_time} zu schlafen und pro Nacht rund {sleep_duration_goal} Stunden zu schlafen.
                    Gib Feedback zum Schlaf des Users und benutze dabei wissenschaftliche Empfehlungen.'''
)
sleep_analysis_chain = LLMChain(llm=llm, prompt=sleep_analysis_template, verbose=True)

# Nutrition data analysis chain
nutrition_analysis_template = PromptTemplate(
        input_variables = ['name', 'age', 'gender', 'weight', 'nutrition_preference', 'nutrition_week'], 
        template='''Du bist ein Chatbot mit dem Namen LiSA. Dein Ziel ist es Lifestyle Tipps zu geben. 
                    Berücksichtige dabei die soziodemographischen Daten, seine Präferenzen und die Anamnese des Users.
                    Der User hat den Namen {name}. Sein Alter ist {age} und sein Geschlecht ist {gender}.
                    Er wiegt {weight} und er hat folgende Ernährungspräferenzen: {nutrition_preference}.
                    Diese Woche hat er folgendes gegessen: {nutrition_week}.
                    Gib Feedback zur Ernährung des Users und benutze dabei wissenschaftliche Empfehlungen.'''
)
nutrition_analysis_chain = LLMChain(llm=llm, prompt=nutrition_analysis_template, verbose=True)

st.title(':female-scientist: LiSA')
st.write("Hallo ich heiße LiSA und ich bin dein persönlicher LifeStyle Assistent.")
st.write("Ich möchte dir helfen einen gesünderen Lifestyle zu pflegen, indem ich dir evidenzbasierte Tipps rundum deine physikalische Aktivität, Ernährung und Schlaf gebe.")

# Options
option = st.selectbox(
    'Wie kann ich dir helfen?',
    options=[
        'Analysiere meine Lifestyle Daten', 
        'Gib mir wissenschaftliche Tipps rundum einen gesunden Lifestyle']
)

# Ask for lifestype tips
if option == 'Gib mir wissenschaftliche Tipps rundum einen gesunden Lifestyle':
    user_input = st.text_area("Was genau möchtest du wissen?", height = 100)
    send_button = st.button("Senden")
    if send_button and user_input:
        with st.spinner("Hmm... lass mich kurz nachdenken..."):
            st.session_state.past.append(user_input)
            response = lifestyle_tip_chain.run(name=st.session_state.name, age=st.session_state.age, 
                                                gender=st.session_state.gender, weight=st.session_state.weight, 
                                                nutrition_preference=st.session_state.nutrition_preference, query=user_input)
            st.session_state.generated.append(response)

# Fitbit data analysis
elif option == 'Analysiere meine Lifestyle Daten':
    option = st.selectbox(
    'Welche Daten möchtest du analysiert haben?',
    options=[
        'Physikalische Aktivität', 
        'Schlaf',
        'Ernährung']
    )
    send_button = st.button("Senden")
    if send_button:
        if option == 'Physikalische Aktivität':
            with st.spinner("Ok ich analysiere jetzt deine körperliche Aktivität"):
                st.session_state.past.append('Analysiere meine Lifestyle Daten rundum meine Physikalische Aktivität.')
                step_count_mean = int(np.mean(step_count_week))
                calories_mean = int(np.mean(cals_week))
                sedentary_mean = int(np.mean(sedentary_week))
                fat_burn_mean = int(np.mean(fat_burn_week))
                cardio_mean = int(np.mean(cardio_week))            
                response = pa_analysis_chain.run(name=st.session_state.name, age=st.session_state.age, 
                    gender=st.session_state.gender, weight=st.session_state.weight, 
                    step_count_mean=step_count_mean, calories_mean=calories_mean,
                    sedentary_mean=sedentary_mean, fat_burn_mean=fat_burn_mean,
                    cardio_mean=cardio_mean, 
                    step_count_goal=st.session_state.step_count_goal,fitness_goal=st.session_state.fitness_goal)
                st.session_state.generated.append(response)
        elif option == 'Schlaf':
            with st.spinner("Ok ich analysiere jetzt deinen Schlaf"):
                st.session_state.past.append('Analysiere meine Lifestyle Daten rundum meinen Schlaf.')
                sleep_duration_mean = round(np.mean(sleep_duration_week),2)
                restless_duration_mean = int(np.mean(restless_duration_week))
                awake_mean = int(np.mean(awake_week))
                response = sleep_analysis_chain.run(name=st.session_state.name, age=st.session_state.age, 
                    gender=st.session_state.gender, weight=st.session_state.weight, 
                    sleep_duration_mean=sleep_duration_mean, restless_duration_mean=restless_duration_mean, awake_mean=awake_mean,
                    start_time_week=start_time_week, end_time_week=end_time_week,
                    bed_time=st.session_state.bed_time, sleep_duration_goal=st.session_state.sleep_duration_goal)
                st.session_state.generated.append(response)
        else:
            with st.spinner("Ok ich analysiere jetzt deine Ernährung"):
                st.session_state.past.append('Analysiere meine Lifestyle Daten rundum meine Ernährung.')
                response = nutrition_analysis_chain.run(name=st.session_state.name, age=st.session_state.age, 
                    gender=st.session_state.gender, weight=st.session_state.weight, 
                    nutrition_preference=st.session_state.nutrition_preference,
                    nutrition_week = nutrition_week)
                st.session_state.generated.append(response)


# Display messages
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')