def getPword():   
    length = False 
    while length == False:
        atempt1 = input('what is your password?')
        if len(atempt1) <= 8 and len(atempt1)>= 6:
            atempt2 = input('confirm your password?')
            if atempt1 == atempt2:
                print(atempt2)
                length = True
            if atempt1 != atempt2:
                print('passwords dont match!')
                length = False
        else:
            print('password not long enough or too long!')
            length = False
getPword()