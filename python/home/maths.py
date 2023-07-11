pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
#area 
def regual_quadralatral ():
    height = input('what is the height?')
    width = input('what is the width?')
    area = float(height) * float(width) 
    print(area)

def triangle ():
    height = input('what is the height?')
    width = input('what is the width?')
    area = float(height) * float(width) * 0.5
    print(area)

def circle ():
    radius = input('what is the radius?')
    radius = float(radius)
    radius = radius * radius
    area = pi * float(radius)
    print(area)

#permiter
def regular_shape():
    what_shape = input('what is the shape')

print('1 = area')
print('2 = permiter')

function = input('what function do you want')
if function == '1':
    print('1 = quadralatral')
    print('2 = triangle')
    print('3 = circle')
    shape = input('what shape do you want?')
    if shape == '1':
        regual_quadralatral()
    if shape == '2':
        triangle()
    if shape == '3':
        circle()

