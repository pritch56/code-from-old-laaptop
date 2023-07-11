import sqlite3 #Python code library for SQL
import os

def create_questions_database(database_name):
    question_db = sqlite3.connect(database_name)
    c = question_db.cursor()

    c.execute('''CREATE TABLE questions(
        question TEXT,
        correct_answer TEXT,
        answer_1 TEXT,
        answer_2 TEXT,
        answer_3 TEXT,
        subject TEXT,
        difficulty INTEGER
    )''')

    question_db.commit()
    question_db.close()

def create_users_database():
    pass

def Initialise_Databases():
    if not os.path.isfile('question.db'):
        create_questions_database('question.db')
        print("successfully created database 'question.db'")
