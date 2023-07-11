import random
username = True 
again = True 
logout = False 
correct = 0
incorrect = 0
username = input('what do you want your username to be?')
password = input('what do you want your password to be?')
while logout == False:
    checkusername = input('what is your username?')
    if username == checkusername:
        checkpassword = input('what is your password?')
        if password == checkpassword:
            play = input ('would you like to play?')
            while play == 'yes': 
                number = random.randint (1,1000)
                guess = input('choose a number between 1 and 1000')
                if number == guess : 
                    print('you got it correct')
                    correct = correct + 1
                else:
                    print('you got it wrong')
                    incorrect = incorrect + 1
                print('you have', correct, 'right answers')
                print('you have', incorrect, 'wrong answers')
                play = input ('would you like to play again?')
                if play == 'no':
                    login = input('would you like to log out?')
                    if login == 'yes' :
                        logout = True 