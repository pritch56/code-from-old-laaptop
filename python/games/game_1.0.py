import random 

#credits 
credits = 100 
c_amount = input('how many credits do you play')



value = 0
value_2 = 0
value_3 = 0
x = random.randint(1,13)
if x<=10 and x>=2 :
    value = value + x

if x == 1:
    card_V = input('do u want it to be worth 11 or 1?')
    if card_V == '1':
        value = value + 1
    if card_V == '11':
        value = value + 11
if x<=13 and x > 11:
    value = value + 10 

print (value)


y = random.randint(1,13)
if y<=9 and x>=2 :
    value_2 = value_2 + x
if y == 1:
    card_V = input('do u want it to be worth 11 or 1?')
    if card_V == '1':
        value_2 = value_2 + 1
    if card_V == '11':
        value_2 = value_2 + 11
if y<=13 and y > 10:
    value_2 = value_2 + 10 
print (value_2)

total = value + value_2
print(total)
s_h = input('do you want to hit?')
if s_h == 'yes':
        x = random.randint(1,13)
        if x<10 and x>2:
            value = value + x
        if x == 1:
            card_V = input('do u want it to be worth 11 or 1?')
            if card_V == '1':
                value_3 = value_3 + float(1)
            if card_V == '11':
                value_3 = value_3 + 11
        if x<=13 or x > 10:
            value_3 = value_3 + 10 
total = value + value_2 + value_3
print('you have', total)
if total > 21 :
    print('you went bust')

#dealer
if total < 22 :
    dealer = random.randint(1, 21)
    while dealer < total :
        d_card2 = random.randint(1,10)
        dealer = dealer + d_card2
print('the dealer has', dealer)

if dealer>21:
    print('the dealer went bust')
    dealer = 0

if total < 22 and total > dealer :
    print('you win')
    credits = float(credits) + float(c_amount)
if total < dealer or total == dealer :
    print('you loss') 
    credits = float(credits) - float(c_amount)
print(credits)





