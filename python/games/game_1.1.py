import random
value_n = 0


def card_1 ():
    card1_suit = random.randint(1,4)
    if card1_suit == 1:
        suit1 = 'of hearts'
    if card1_suit == 2:
        suit1 = 'of diamonds'
    if card1_suit == 3:
        suit1 = 'of spades'
    if card1_suit == 4:
        suit1 = 'of clubs'
    card1 = float(random.randint(1,13))
    if card1 == 1:
        print('your first card is the ace',suit1 )
    if card1 == 2:
        print('your first card is the 2', suit1)
    if card1 == 3:
        print('your first card is the 3',suit1 )
    if card1 == 4:
        print('your first card is the 4', suit1)
    if card1 == 5:
        print('your first card is the 5',suit1 )
    if card1 == 6:
        print('your first card is the 6',suit1 )
    if card1 == 7:
        print('your first card is the 7',suit1 )
    if card1 == 8:
        print('your first card is the 8',suit1 )
    if card1 == 9:
        print('your first card is the 9', suit1)
    if card1 == 10:
        print('your first card is the 10', suit1)
    if card1 == 11:
        print('your first card is the jack', suit1)
    if card1 == 12:
        print('your first card is the queen',suit1)
    if card1 == 13:
        print('your first card is the king', suit1)
      
    if card1 == 1:
        ace_value = input('do you want the ace to be 11 or 1?')
        if ace_value == '11':
           value_1 = 11.0 
        if ace_value == '1':
            value_1 = 1.0

    if card1 >= 2 and card1 <= 10 :
        value_1 = float(card1)

    if card1 >= 11 :
        value_1 = 10.0
    return value_1

def card_2 ():
    card2_suit = random.randint(1,4)
    if card2_suit == 1:
        suit2 = 'of hearts'
    if card2_suit == 2:
        suit2 = 'of diamonds'
    if card2_suit == 3:
        suit2 = 'of spades'
    if card2_suit == 4:
        suit2 = 'of clubs'
    card2 = float(random.randint(1,13))
    
    #print(card2)
    if card2 == 1:
        print('your second card is the ace',suit2 )
    if card2 == 2:
        print('your second card is the 2', suit2)
    if card2 == 3:
        print('your second card is the 3',suit2 )
    if card2 == 4:
        print('your second card is the 4', suit2)
    if card2 == 5:
        print('your second card is the 5',suit2 )
    if card2 == 6:
        print('your second card is the 6',suit2 )
    if card2 == 7:
        print('your second card is the 7',suit2 )
    if card2 == 8:
        print('your second card is the 8',suit2 )
    if card2 == 9:
        print('your second card is the 9', suit2)
    if card2 == 10:
        print('your second card is the 10', suit2)
    if card2 == 11:
        print('your second card is the jack', suit2)
    if card2 == 12:
        print('your second card is the queen',suit2)
    if card2 == 13:
        print('your second card is the king', suit2)
    if card2 == 1:
        ace_value = input('do you want the ace to be 11 or 1?')
        if ace_value == '11':
            value_2 = 11.0 
        if ace_value == '1':
            value_2 = 1.0

    if card2 >= 2 and card2 <= 10 :
        value_2 = float(card2)

    if card2 >= 11 :
        value_2 = 10.0

    return value_2



value_1 = card_1()
value_2 = card_2()
total = value_1 + value_2 



new_card = input('do you want another card')
if new_card == 'yes':
    new_card = 'yes'
    while new_card == 'yes':
        card3_suit = random.randint(1,4)
    if card3_suit == 1:
        suit3 = 'of hearts'
    if card3_suit == 2:
        suit3 = 'of diamonds'
    if card3_suit == 3:
        suit3 = 'of spades'
    if card3_suit == 4:
        suit3 = 'of clubs'
    card3 = float(random.randint(1,13))
    if card3 == 1:
        print('your second card is the ace',suit3)
    if card3 == 2:
        print('your second card is the 2', suit3)
    if card3 == 3:
        print('your second card is the 3',suit3)
    if card3 == 4:
        print('your second card is the 4', suit3)
    if card3 == 5:
        print('your second card is the 5',suit3)
    if card3 == 6:
        print('your second card is the 6',suit3)
    if card3 == 7:
        print('your second card is the 7',suit3)
    if card3 == 8:
        print('your second card is the 8',suit3)
    if card3 == 9:
        print('your second card is the 9', suit3)
    if card3 == 10:
        print('your second card is the 10', suit3)
    if card3 == 11:
        print('your second card is the jack', suit3)
    if card3 == 12:
        print('your second card is the queen',suit3)
    if card3 == 13:
        print('your second card is the king', suit3)
    if card3 == 1:
        ace_value = input('do you want the ace to be 11 or 1?')
        if ace_value == '11':
            value_3 = 11.0 
        if ace_value == '1':
            value_3 = 1.0

    if card3 >= 2 and card3 <= 10 :
        value_3 = float(card3)

    if card3 >= 11 :
        value_3 = 10.0
    
    value_n = value_n + value_3
    new_card = input('do you want another card')





#dealer 
def dealer_card ():
    dealer = random.randint (1,22)
    if dealer < 16 :
        dealer = float(dealer) + random.randint(1,10)
    print('the dealer has', dealer)
    if dealer > 21 :
        print('the dealear went bust')

dealer_card()


print(total)






