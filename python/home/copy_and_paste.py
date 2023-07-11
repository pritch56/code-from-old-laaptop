x = 0    #setting x
usernameset = input('what do you want your user name to be?') #setting username 
passwordset = input('what do you want your password to be?') #setting password 
passwordconfirm = input('please confirm your password?') #confirming pass word
if passwordset == passwordconfirm : #checking is the passwords you havce inpiuted arer the same
   login = input('thank you, whould you like to login?') # asking if you want to log in 
if login == 'yes': # if you say yes it runs program 
    while x < 3 : 
        username = input('what is your username?')
        if username == usernameset :
            password = input('what is your password')
            if password == passwordset :
                print('you are loged in')
            else : 
                print ('incorect')
        else :
            print ('incorect')
        if username == usernameset and password == passwordconfirm :
            x = 4 
        else : 
            x = x + 1


