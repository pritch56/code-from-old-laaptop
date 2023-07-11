import random
from random import randint
print('Ghost Game')
feeling_brave = True 
score = 0 
ghost_door = 1
while feeling_brave:
    ghost_door == random.randint(1,3)
    print ('three doors ahead...')
    print('which door do you open')
    door = input('1, 2, or 3?')
    door_num = int(door)
    if door_num == ghost_door:
        print('GHOST!')
        feeling_brave = False 
    else:
        print('No Ghost!')
        print('you enter the next room.')
        score = score + 1
print('RUN AWAY!')
print('Game over! you scored', score)