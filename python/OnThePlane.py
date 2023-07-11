#Resteraunt ratings data base
#name 
#location 
#resteraunt 
#food 


#menu 
def menu():
    print('1 = Add New Resteraunt')
    print('2 = Show All Resteraunts')
    print('3 = Show Select Resteraunts')
    choice = input('What would you like to do?  ')
    if choice == '1':
        AddResteraunt()
    if choice == '2':
        ViewAll()
    if choice == '3':
        print('1 = Location')
        print('2 = Rating')
        print('3 = Name')


def AddResteraunt():
    print('hello')

def ViewAll(): 
    print('Test')


menu()