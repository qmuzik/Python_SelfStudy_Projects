from Bird import *

# Creates a new instance of the class with an added attribute of age using dot notation and then displays them
chick = Bird('Cheep, Cheep')
chick.age = '1 week'

print('\nChick Says: ' , chick.talk())
print('Chicks Age: ', chick.age)

chick.age = '2 weeks'
print('Chick Now: ', chick.age)

# Changes the value via function
setattr(chick,'age','3 weeks')

# Displays all attributes about Chick
print('\nChick Attributes...')
for attrib in dir (chick):
    if attrib[0] != '_':
        print(attrib, ':', getattr(chick,attrib))

# Deletes chicks age attribute 
delattr(chick,'age')
print('\nChick Age attribute?' , hasattr(chick,'age'))        