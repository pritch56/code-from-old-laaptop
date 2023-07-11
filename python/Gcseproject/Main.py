import sqlite3 #Python code library for SQL
import os
import random
from databasecreator import Initialise_Databases


def startup():
    print('1 = login')
    print('2 = create account')

    Initialise_Databases()

    choice = input('what would you like to do?')
    if choice == '1':
        login()
    if choice == '2':
        createaccount()
    else:
        print('selection invalid')
        startup()

def createaccount():
    add_to_account = sqlite3.connect('revison.db')
    c = add_to_account.cursor()
    Account_name = input('Enter username?')
    Account_password = input('Enter password?')
    Account_age = input('What is your age?')
    c.execute('INSERT INTO account (account_name, account_password, account_age) VALUES (?, ?, ?)', (Account_name, Account_password, Account_age))

    print ('\nData was been stored')
    menu()

def login():
    username = input('what is your username?')
    password = input('what is your password?')
    account_db = sqlite3.connect('revison.db')
    c=account_db.cursor()
    c.execute ('SELECT * FROM account WHERE account_name = ? AND account_password = ?', [username, password])
    accounts = c.fetchall()
    if accounts == []:
        print("incorect username or password")
        startup()
    else:
        print('you are logged in')
        menu()

def viewscores():
    if os.path.isfile('scores.db'):
        score_db = sqlite3.connect('scores.db')
        c = score_db.cursor()
        c.execute ('SELECT * FROM score ORDERBY game_score')
        score_library = c.fetchall
        print(score_library)

def settings():
    print('1 = change difficulty')
    print('2 = change topic')
    print('3 = back to menu')
    decision = input('what would you like to do?')
    if decision == '1':
        print('1 = easy')
        print('2 = medium')
        print('3 = hard')
        difficulty_setting = input('what difficulty would you like?')
        if difficulty_setting == '1':
            difficulty = 1

        if difficulty_setting == '2':
            difficulty = 2 

        if difficulty_setting == '3':
            difficulty = 3
        settings()
    if decision == '2':
        print('1 = Geography')
        print('2 = Computing')
        print('3 = Science')
        topic_setting = input('What subject would you like to be tested on?')
        if topic_setting == '1':
            topic = 1

        if topic_setting == '2': 
            topic = 2

        if topic_setting == '3':
            print('1 = Physics')
            print('2 = Chemistry')
            print('3 = Biology :(')
            print('4 = All')
            science_choice = input('What science would you like to do?')
            if science_choice == '1':
                topic = 3

            if science_choice == '2':
                topic = 4

            if science_choice == '3':
                topic = 5

            if science_choice == '4':
                topic = 3 and 4 and 5

            else:
                print('selection invalid')
                settings() 
    print(topic)
    print(difficulty)
    if decision == '3':
        menu() 
    
    menu()

def starttest():
    if os.path.isfile('questions.db'):
        score = 0
        test_questions = sqlite3.connect('questions.db')
        c=test_questions.cursor()
        for i in range (10):
            display = random.randint(1,4)
            print(display)
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
        if os.path.isfile('scores.db'):
            name = input('what is your account name?')
            age= input('what is your account age?')
            modify_db = sqlite3.connect('scores.db')
            c = modify_db.cursor() 
            c.execute('INSERT INTO score (game_score, account_name, account_age, game_difficulty, game_topic) VALUES (?, ?, ?, ?, ?)', (score, name, age))
            modify_db.commit()
            modify_db.close()
            print ('\nScore added to database')


def menu():
    print('1 = start test')
    print('2 = view scores')
    print('3 = settings')
    menuchoice = input('what would you like to do? ')
    if menuchoice == '1':
        print(menuchoice)
        starttest()
    if menuchoice == '2':
        viewscores()
    if menuchoice == '3':
        settings()

topic = 1
difficulty = 1

menu()
