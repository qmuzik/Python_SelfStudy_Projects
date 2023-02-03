import cat

# Requests user to enter a name to overwrite the default argument value 
pet = input( 'Enter A Pet Name: ' )

# Calls each function and passes the user defined value as the argument 
cat.purr(pet)
cat.lick(pet)
cat.nap(pet)

