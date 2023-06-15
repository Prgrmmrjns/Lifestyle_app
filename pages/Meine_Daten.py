import streamlit as st
import numpy as np
from Home import * 
import plotly.graph_objects as go
import pandas as pd
import datetime

def create_pa_graph():
    today = datetime.datetime.today()
    last_week_dates = [today - datetime.timedelta(days=i) for i in range(6, -1, -1)]
    step_count_df = pd.DataFrame({"Date": last_week_dates, "Schrittmenge": step_count_week, "Kalorien":cals_week})
    fig = go.Figure()
    fig.add_trace(go.Bar(x=step_count_df['Date'], y=step_count_df['Schrittmenge'], name='Schrittmenge'))
    fig.add_trace(go.Scatter(x=step_count_df['Date'], y=step_count_df['Kalorien'], name='Verbrannte Kalorien', yaxis='y2', line=dict(color='red')))
    fig.update_layout(title='Deine Schrittanzahl und verbrannte Kalorien in den letzten sieben Tagen', yaxis=dict(title='Schrittmenge'), yaxis2=dict(title='Verbrannte Kalorien', overlaying='y', side='right'))
    st.plotly_chart(fig)

def create_sleep_graph():
    today = datetime.datetime.today()
    last_week_dates = [today - datetime.timedelta(days=i) for i in range(6, -1, -1)]
    sleep_df = pd.DataFrame({"Date": last_week_dates, "Schlafdauer": sleep_duration_week, "Unruhiger Schlaf":restless_duration_week})
    fig = go.Figure()
    fig.add_trace(go.Bar(x=sleep_df['Date'], y=sleep_df['Schlafdauer'], name='Schlafdauer'))
    fig.add_trace(go.Scatter(x=sleep_df['Date'], y=sleep_df['Unruhiger Schlaf'], name='Unruhiger Schlaf', yaxis='y2', line=dict(color='red')))
    fig.update_layout(title='Deine Schlafdauer und die Menge an unruhigem Schlaf in den letzten sieben Tagen', yaxis=dict(title='Schlafdauer (Stunden)'), yaxis2=dict(title='Unruhiger Schlaf (Minuten)', overlaying='y', side='right'))
    st.plotly_chart(fig)

def create_nutrition_graph():
    today = datetime.datetime.today()
    last_week_dates = [today - datetime.timedelta(days=i) for i in range(6, -1, -1)]
    kcals_week = [3200, 2400, 2750, 3000, 2300, 2900, 2550]
    proteins_week = [45, 55, 51, 49, 32, 60, 58]
    nutrition_df = pd.DataFrame({"Date": last_week_dates, "kcals": kcals_week, "Proteine":proteins_week})
    fig = go.Figure()
    fig.add_trace(go.Bar(x=nutrition_df['Date'], y=nutrition_df['kcals'], name='kcals'))
    fig.add_trace(go.Scatter(x=nutrition_df['Date'], y=nutrition_df['Proteine'], name='Proteine', yaxis='y2', line=dict(color='red')))
    fig.update_layout(title='Deine geschätzt konsumierte kCals und die Menge an Proteinen pro Tag in den letzten sieben Tagen', yaxis=dict(title='Geschätzte konsumierte kCals'), yaxis2=dict(title='Geschätzte Menge an konsumierten Proteinen (g)', overlaying='y', side='right'))
    st.plotly_chart(fig)

st.title("Meine Lifestyle Daten")
option = st.selectbox(
    'Welche Daten möchtest du dir angucken?',
    options=[
        'Physikalische Aktivität', 
        'Schlaf',
        'Ernährung']
)
if option == 'Physikalische Aktivität':
    st.header("Physikalische Aktivität")
    create_pa_graph()
    days_step_count_reached =  len([x for x in step_count_week if x >= st.session_state.step_count_goal])
    st.markdown(f"Super! Du hast dein tägliches Schrittziel diese Woche an **{days_step_count_reached} Tagen** erreicht. Das ist ein guter Ansatz für dein Fitnessziel **{st.session_state.fitness_goal}**.")
    st.divider()
    data = {'Schrittzahl': step_count_week,
    'Verbrannte Kalorien': cals_week,
    'Passive Tätigkeiten (Min.)': sedentary_week}
    df = pd.DataFrame(data)
    st.dataframe(df)


elif option == 'Schlaf':
    st.header("Schlaf")
    create_sleep_graph()
    sleep_duration_reached =  len([x for x in sleep_duration_week if x >= st.session_state.sleep_duration_goal])
    st.markdown(f"Phänomenal! Du hast dein tägliches Schlafdauerziel diese Woche an **{sleep_duration_reached} Tagen** erreicht. Merkst du schon Verbesserungen in deiner Produktivität?")
else:
    st.header('Ernährung')
    create_nutrition_graph()
    kcals_week = [3200, 2400, 2750, 3000, 2300, 2900, 2550]
    kcals_divergence =  len([x for x in kcals_week if x >= np.mean(kcals_week) ])
    st.markdown(f"Sehr gut! Diese Woche hast du an **{kcals_divergence} Tagen** ungefähr genauso viel kcals konsumiert wie du verbrannt hast. Damit bist du auf einem guten Weg für dein Fitnessziel **{st.session_state.fitness_goal}.**")
