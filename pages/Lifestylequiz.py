import streamlit as st

questions = [
    {
        "question": "Wie viele Minuten moderater körperlicher Aktivität sollten Erwachsene minimal jede Woche absolvieren?",
        "options": ["75 Minuten", "150 Minuten", "200 Minuten", "300 Minuten"],
        "weights": [0, 1, 0, 0],
        "info": """Laut WHO Richtlinien  sollten Erwachsene im Alter von 18 bis 64 
        Jahren mindestens 150 Minuten moderate körperliche Aktivität pro Woche absolvieren. Moderate körperliche Aktivität umfasst Aktivitäten 
        wie schnelles Gehen, Radfahren, Schwimmen oder Tanzen, die den Herzschlag erhöhen und zu einer leichten Anstrengung führen. """,
        "source": "https://www.who.int/publications/i/item/9789241599979"
    },
    {
        "question": "Welches ist KEINE gesunde Quelle für Nahrungsfett?",
        "options": ["Avocado", "Lachs", "Natives Olivenöl extra", "Transfette"],
        "weights": [0, 0, 0, 1],
        "info": """Transfette sind ungesund, da sie den LDL-Cholesterinspiegel erhöhen und gleichzeitig den HDL-Cholesterinspiegel senken, 
        was das Risiko für Herzerkrankungen erhöht. Zudem sind Transfette mit einem erhöhten Risiko für Entzündungen, Insulinresistenz und 
        Fettleibigkeit verbunden. """,
        "source": "https://www.nejm.org/doi/full/10.1056/NEJMra054035"
    },
    {
        "question": "Wie hoch ist die empfohlene tägliche Wassermenge für einen Erwachsenen?",
        "options": ["1 Liter", "2 Liter", "3 Liter", "4 Liter"],
        "weights": [0, 1, 0, 0],
        "info": """Die empfohlene tägliche Wassermenge für einen Erwachsenen kann je nach verschiedenen Faktoren wie Alter, Geschlecht, 
        körperlicher Aktivität und Umgebung variieren. Eine allgemeine Empfehlung lautet, etwa 2 bis 3 Liter (ca. 8-12 Gläser) Wasser pro Tag zu trinken.""",
        "source": "https://www.nationalacademies.org/our-work/dietary-reference-intakes-for-electrolytes-and-water"
    },
    {
        "question": "Welcher Stoff der vorgeschlagenen Stoffe hat in wissenschaftlichen Studie einen Krebs-vorbeugenden Effekt gezeigt?",
        "options": ["Antioxidantien", "Aflatoxine", "Nitrosamin", "Asbest"],
        "weights": [1, 0, 0, 0],
        "info": """Antioxidantien können potenziell dazu beitragen, das Krebsrisiko zu verringern, da sie dazu beitragen, 
        Schäden durch freie Radikale im Körper zu reduzieren. Freie Radikale sind instabile Moleküle, die oxidative Schäden an Zellen und DNA 
        verursachen können, was wiederum das Risiko von Krebs erhöhen kann. Antioxidantien wirken, indem sie diese freien Radikale neutralisieren 
        und deren schädliche Auswirkungen reduzieren.""",
        "source": "https://link.springer.com/article/10.1007/s00204-011-0774-2"
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
st.subheader("Thema: Ernährung")

answers = []
for i, question in enumerate(questions):
    with st.expander(f'Frage {i+1}: {question["question"]}'):
        answer = st.radio(' ', question['options'])
        answers.append(question['options'].index(answer))

if st.button("Antwort senden"):
    st.session_state['quiz_status'] = True
    st.session_state['quiz_score'] = calculate_score(answers)
    st.write(f"Du hast {round(st.session_state['quiz_score'],1)*100} richtig beantwortet.")
    if st.session_state['quiz_score'] < 0.5:
        st.write("Da ist noch viel Luft nach oben!")
    elif st.session_state['quiz_score'] < 0.8:
        st.write("Sehr gut! Du bist auf dem besten Weg alles über einen gesunden Lifestyle zu wissen.")
    else:
        st.write("Perfekt! Du weißt alles über einen gesunden Lifestyle!")
        st.balloons()
    with st.expander("Ich will mehr drüber wissen"):
        st.write("Info")
        for i, question in enumerate(questions):
            st.write(f"Frage {i}")
            st.write(question["info"])
            st.markdown(question["source"])

