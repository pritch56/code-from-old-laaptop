import sqlite3 #Python code library for SQL
import os
import random
if os.path.isfile('questions.db'):
        score = 0
        test_questions = sqlite3.connect('questions.db')
        c=test_questions.cursor()
        for i in range (10):
            display = random.randint(1,4):
            if display == 1:
                display_question = c.execute('SELECT question FROM questions WHERE question_difficulty = (?) AND question_subject = (?) ', [difficulty, topic])
                answer_1 = c.execute('SELECT answer_1 FROM questions WHERE question = (?) ', [display_question])
                print('1 =', answer_1)
                answer_2 = c.execute('SELECT answer_2 FROM questions WHERE question = (?) ', [display_question])
                print('2 =', answer_2)
                answer_3 = c.execute('SELECT answer_3 FROM questions WHERE question = (?) ', [display_question])
                print('3 =', answer_3)
                answer_4 = c.execute('SELECT correct_answer FROM questions WHERE question = (?) ', [display_question])
                print('4 =', answer_4)
                answer = input('what is the answer?')
                correct_answer = c.execute('SELECT correct_answer FROM questions WHERE question = (?) ', [display_question])
                if answer == correct_answer:
                    print('correct answer')
                    score = score + 10
                else:
                    print('incorrect')
            
            if display == 2:
                display_question = c.execute('SELECT question FROM questions WHERE question_difficulty = (?) AND question_subject = (?) ', [difficulty, topic])
                answer_1 = c.execute('SELECT answer_2 FROM questions WHERE question = (?) ', [display_question])
                print('1 =', answer_1)
                answer_2 = c.execute('SELECT answer_3 FROM questions WHERE question = (?) ', [display_question])
                print('2 =', answer_2)
                answer_3 = c.execute('SELECT correct_answer FROM questions WHERE question = (?) ', [display_question])
                print('3 =', answer_3)
                answer_4 = c.execute('SELECT answer_1 FROM questions WHERE question = (?) ', [display_question])
                print('4 =', answer_4)
                answer = input('what is the answer?')
                correct_answer = c.execute('SELECT correct_answer FROM questions WHERE question = (?) ', [display_question])
                if answer == correct_answer:
                    print('correct answer')
                    score = score + 10
                else:
                    print('incorrect')
            
            if display == 3:
                display_question = c.execute('SELECT question FROM questions WHERE question_difficulty = (?) AND question_subject = (?) ', [difficulty, topic])
                answer_1 = c.execute('SELECT corrct_answer FROM questions WHERE question = (?) ', [display_question])
                print('1 =', answer_1)
                answer_2 = c.execute('SELECT answer_1 FROM questions WHERE question = (?) ', [display_question])
                print('2 =', answer_2)
                answer_3 = c.execute('SELECT answer_2 FROM questions WHERE question = (?) ', [display_question])
                print('3 =', answer_3)
                answer_4 = c.execute('SELECT answer_3 FROM questions WHERE question = (?) ', [display_question])
                print('4 =', answer_4)
                answer = input('what is the answer?')
                correct_answer = c.execute('SELECT correct_answer FROM questions WHERE question = (?) ', [display_question])
                if answer == correct_answer:
                    print('correct answer')
                    score = score + 10
                else:
                    print('incorrect')
                
            if display == 4:
                display_question = c.execute('SELECT question FROM questions WHERE question_difficulty = (?) AND question_subject = (?) ', [difficulty, topic])
                answer_1 = c.execute('SELECT answer_3 FROM questions WHERE question = (?) ', [display_question])
                print('1 =', answer_1)
                answer_2 = c.execute('SELECT correct_answer FROM questions WHERE question = (?) ', [display_question])
                print('2 =', answer_2)
                answer_3 = c.execute('SELECT answer_2 FROM questions WHERE question = (?) ', [display_question])
                print('3 =', answer_3)
                answer_4 = c.execute('SELECT answer_1 FROM questions WHERE question = (?) ', [display_question])
                print('4 =', answer_4)
                answer = input('what is the answer?')
                correct_answer = c.execute('SELECT correct_answer FROM questions WHERE question = (?) ', [display_question])
                if answer == correct_answer:
                    print('correct answer')
                    score = score + 10
                else:
                    print('incorrect')


            print('you scored:', score)