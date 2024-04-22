import streamlit as st

import sqlite3
conn = sqlite3.connect('recommender_feedback.db')
c = conn.cursor()
    

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS feedback(date_submitted DATE, Q1 TEXT, Q2 TEXT, Q3 TEXT, Q4 TEXT, Q5 TEXT, Q6 TEXT)')

def add_feedback(date_submitted, Q1, Q2, Q3, Q4, Q5, Q6):
    c.execute('INSERT INTO feedback (date_submitted,Q1, Q2, Q3, Q4, Q5, Q6) VALUES (?,?,?,?,?,?,?)',(date_submitted,Q1, Q2, Q3, Q4, Q5, Q6))
    conn.commit()

def main():

    st.title("Recommender Feedback")

    d = st.date_input("Today's date",None, None, None, None)
    
    question_1 = st.text_input('Enter your name:')
    
    question_2 = st.text_input('Enter your Phone Number:')

    question_3 = st.text_input('Enter your E-mail:')
    
    question_4 = st.slider('Overall, how satisfied are you with the recommendations? (5 being very satisfied and 1 being very dissapointed)', 1,5,2)
    st.write('You selected:', question_4)

    question_5 = st.selectbox('Was the application user interface user-friendly?',('Yes', 'No'))
    st.write('You selected:', question_5)

    question_6 = st.text_input('What could have been better?', max_chars=50)

    if st.button("Submit feedback"):
        create_table()
        add_feedback(d, question_1, question_2, question_3, question_4, question_5, question_6)
        st.success("Feedback submitted. Thank you for the feedback")

if __name__ == '__main__':
    main()