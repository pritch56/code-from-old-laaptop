import time
import os 
username=input('enter username:')
password=input('enter password:')
filename = r'C:\Users\Ben Pritchard\OneDrive\Desktop\marks.txt'
if os.path.isfile(filename):
    f=open(filename, 'r')
    lines=f.readlines()
    found=False 
    for i in range (0, len(lines)-1, 2):
        line = lines [i]
        if username == line.strip('\n'):
            found=True 
            print('matched username')
            if password == lines [i+1] .strip('\n'):
                print('matched password')
                found = True 
                break 
            else:
                print('invalid password')
                found = False 

    f.close 
    if found == False : 
        print('invalid user')
else:
    print('invalid filepath')
