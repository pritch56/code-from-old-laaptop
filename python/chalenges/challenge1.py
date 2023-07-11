distance = input('how far are you traveling today?') #input
distance = float(distance) #setting as a float 
distance = distance - 1 #minusing one from distace
price = distance * 2 + 3 #setting price as distance times two plus three
people = input('how many people are in the car') #input
people = float(people) # setting it as float 
if people > 5: # a selection
    price = price + price/2 # 

price2 = int(price) # making it an integere 
price2 = float(price2) # making it a float 
pence = price - price2  
pence = pence * 100 #making a whole number 
pence = int(pence) # setting as an integer 
print ('£' '{:,.2f}'.format(price)) #formating it to two decimal places 
print(price2,'pounds') #displaying it 
print(pence,'pence') #displayinh it 