import sqlite3
import os
question = input('What is the questions?')
correct_answer = input('what is the correct answer?')
answer1 = input('what is an incorect answer?')
answer2 = input('what is an incorect answer?')
answer3 = input('what is an incorect answer?')
print('1 = geography')
print('2 = computing')
print('3 = physics')
print('4 = chemistry')
print('5 = biology')
subject = input('what is the subject of this question?')
print('1 = easy')
print('2 = medium')
print('3 = hard')
difficulty = input('what is the difficulty of the question?')
if os.path.isfile('question.db'):
    add_to_question = sqlite3.connect('question.db')
    c = add_to_question.cursor()
    c.execute('INSERT INTO questions(question, correct_answer, answer_1, answer_2, answer_3, subject, difficulty) VALUES (?, ?, ?, ?, ?, ?, ?)', [question, correct_answer, answer1, answer2, answer3, subject, difficulty])
    add_to_question.commit()
    add_to_question.close()