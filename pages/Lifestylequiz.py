import streamlit as st

questions = [
    {
        "question": "Wie viele Minuten moderater körperlicher Aktivität sollten Erwachsene minimal jede Woche absolvieren?",
        "options": ["75 Minuten", "150 Minuten", "200 Minuten", "300 Minuten"],
        "weights": [0, 1, 0, 0]
    },
    {
        "question": "Welches ist KEINE gesunde Quelle für Nahrungsfett?",
        "options": ["Avocado", "Lachs", "Natives Olivenöl extra", "Transfette"],
        "weights": [0, 0, 1, 0]
    },
    {
        "question": "Wie hoch ist die empfohlene tägliche Wassermenge für einen Erwachsenen?",
        "options": ["1 Liter", "2 Liter", "3 Liter", "4 Liter"],
        "weights": [0, 1, 0, 0]
    },
]

# define a function to calculate the score
def calculate_score(answers):
    score = 0
    for i, answer in enumerate(answers):
        score += questions[i]['weights'][answer]
    return score / len(questions)

# display the quiz
st.title('Lifestyle Quiz')

answers = []
for i, question in enumerate(questions):
    with st.expander(f'Frage {i+1}: {question["question"]}'):
        answer = st.radio(' ', question['options'])
        answers.append(question['options'].index(answer))

if st.button("Antwort senden"):
    score = calculate_score(answers)
    if score < 0.5:
        st.write("Da ist noch viel Luft nach oben!")
    elif score < 0.8:
        st.write("Sehr gut! Du bist auf dem besten Weg alles über einen gesunden Lifestyle zu wissen.")
    else:
        st.write("Perfekt! Du weißt alles über einen gesunden Lifestyle!")
        st.balloons()
