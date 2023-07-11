import sqlite3 #Python code library for SQL
import os
if os.path.isfile('questions.db'):
        test_questions = sqlite3.connect('questions.db')
        c=test_questions.cursor()
        display_question = c.execute('SELECT * FROM questions')
        print(display_question)