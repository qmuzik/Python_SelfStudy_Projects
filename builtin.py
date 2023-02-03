from Bird import*

# Creates a new bird object 
zola = Bird('Beep, Beep!')

# Displays all built in instance attributes 
print('\nBuilt-in Instance Attributes...')
for attrib in dir (zola):
    if attrib[0] == '_':
        print(attrib)

# Displays all items in class dictionary
print('\nClass Dictionary...')
for item in Bird.__dict__:
    print(item,':',Bird.__dict__[item])

# Displays all items in instance dictionary
print('\nInstance Dictionary...')
for item in zola.__dict__:
    print(item,':',zola.__dict__[item])
    