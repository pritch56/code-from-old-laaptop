import random
value = 0 #the value of the cards
card_1 = random.randint ('1,13')
if card_1 == '1':
    print('your card is the ace ')
    ace_1_11 = input('do you want the value to be 1 or 11')
    if ace_1_11 == '1':
      value = value + float(1)
    if ace_1_11 == '11':
        value = value + float(11)
     value = value + float(11)
if card_1 == '2':
    print('your card is the  2')
    value = value + float(2)
if card_1 =='3':
    print('your card is the 3')
    value = value + float(3)
if card_1 == '4':
    print('your card is the 4')
    value = value + float(4)
if card_1 == '5':
    print('your card is the  5')
    value = value + float(5)
if card_1 == '6':
    print('your card is the 6')
    value = value + float(6)
if card_1 == '7':
    print('your card is the 7')
    value = value + float(7)
if card_1 == '8':
    print('your card is the 8')
    value = value + float(8)
if card_1 == '9':
    print('your card is the 9')
    value = value + float(9)
if card_1 == '10':
    print('your cardis the 10')
    value = value + float(10)
if card_1 == '11':
    print('your card is the jack')
    value = value + float(10)
if card_1 == '12':
    print('your card is the queen')
    value = value + float(10)
if card_1 == '13':
    print('your card is the king')
    value = value + float(10)
print(value)


