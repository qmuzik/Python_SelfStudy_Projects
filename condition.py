a = 1 # Varible 1
b = 2 # Varible 2 

print( '\nVarible a Is :' , 'One' if ( a == 1 ) else 'Not One' ) # Displays results of condition for varible a 
print( 'Varible a Is :' , 'Even' if ( a % 2 == 0 ) else 'Odd' )

print( '\nVarible b Is :' , 'One' if ( b == 1 ) else 'Not One' ) # Displays results of condition for varible b 
print( 'Varible b Is :' , 'Even' if ( b % 2 == 0 ) else 'Odd' )

max = a if ( a > b ) else b # Assigns the result of the conition to a new varible 

print( '\nGreater Value is:' , max ) # Displays the result of "The greater value" of both varibles 
