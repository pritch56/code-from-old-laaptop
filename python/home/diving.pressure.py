

def calc_pressure():   
    a = 5
    water = input('salt or fresh?')
    depth = input('what depth will u go to?')
    a = float(depth)
    print(a, 'meters')
    if water == 'salt' :
       pressure = a/10 + 1
    else : 
        pressure = a/10.3 + 1
    print(pressure, 'bar')
    print(pressure * 14.5, 'psi' )

def temp_drop():
    air_temp = input('what is the air temperature?')
    air_temp_k = float(air_temp) + 273
    water_temp = input('what is the water temperature?')
    water_temp_k = float(water_temp) + 273
    tank_pressure = input('what is your tanks pressure?')
    w_tank_pressure = float(tank_pressure) * water_temp_k / air_temp_k
    print(w_tank_pressure)

def gas_consumption():
    bar_used = input('what bar did you use?')
    tank_size = input('what is your tank size in litres?') 
    bottom_time = input('what was your bottom time')
    pressure_at_depth = input('what is your pressure at depth?')
    consumption_1 = float(bar_used) * float(tank_size)
    consumption_2 = float(bottom_time) * float(pressure_at_depth)
    total_consumption = consumption_1/consumption_2
    print(total_consumption, 'liters per minute')

def weighting():
    print('1 = swim suit')
    print('2 = 3mm')
    print('3 = 5mm')
    print('4 = 7mm')
    print('5 = neoprene dry suit')
    print('6 = shell dry suit, light undergarment')
    print('7 = shell dry suit, heavy undergarments')
    suit = input('what are you wearing? ')
    weigth = input('what is your weight')
    weight = float(weigth)
    if suit == '1':
        print('0.5 - 2 kg')
    if suit == '2':
        weigth_needed = weight/25
    if suit == '3':
        weigth_needed =  weight/10 
    if suit == '4':
        weigth_needed =  weight/10 + 2.25
    if suit == '5': 
        weigth_needed =  weight/10 + 4
    if suit == '6':
        weigth_needed =  weight/10 + 2.25
    if suit == '7':
        weigth_needed =  weight/10 + 5
    water = input('is it salt or fresh ')
    if water == 'salt':
        print(weigth_needed, 'kg')
    if water == 'fresh':
        if weight > 45 and weight < 56:
            print(weigth_needed - 2, 'kg')
        if weight > 57 and weight < 70:
            print(weigth_needed - 2.3, 'kg')
        if weight > 71 and weight < 85 :
            print(weigth_needed - 3, 'kg')
        if weight > 86 and weight < 99 :
            print(weigth_needed - 3.2, 'kg')

    
       



print ('1 = pressure')
print ('2 = pressure drop')
print ('3 = gas consumption')
print ('4 = weight needed')
function = input('what function do you want')
if function == '1' :
    calc_pressure()
if function == '2' :
    temp_drop()
if function == '3':
    gas_consumption()
if function == '4':
    weighting()



