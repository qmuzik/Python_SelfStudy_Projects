from Bird import *

# Displays documentation string
print( 'nClass Instances Of:\n' , Bird.__doc__ )

# Creates a new instance of the bird class with a sound parameter
polly = Bird( 'Squawk!, squawk!' )

# Displays the instance varible and common class varible value 
print( '\nNumber of Birds: ' , polly.count )
print( 'Polly Says: ' , polly.talk() )

# Creates a new instance of the bird class with a sound parameter
harry = Bird( 'Tweet!, tweet!' )

# Displays the instance varible and common class varible value 
print( '\nNumber of Birds:' , harry.count )
print( 'Polly Says:' , harry.talk() )