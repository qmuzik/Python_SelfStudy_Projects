zoo = ( 'Kangaroo' , 'Leopard' , 'Moose' ) # Initializes a tuple and displays contents, length, and type 
print( 'Tuple:' , zoo , '\tLength:' , len( zoo ) )
print( type( zoo ) )

bag = { 'Red' , 'Green' , 'Blue' } # Initializes a set and displays contents, length, and type 
bag.add( 'Yellow' )
print( '\nSet:' , bag , '\tLength' , len( bag ) )
print( type( bag ) )

print( '\nls Green In bag Set?:' , 'Green' in bag ) # Adds elements to seek two values in set 
print( 'Is Orange In bag Set?:' , 'Orange' in bag )

box = { 'Red' , 'Purple' , 'Yellow' } # Initializes a second set and displays contents, length, and type 
print( '\nSet:' , box , '\t\tLength' , len( box ) )
print( 'Common to Both Sets:' , bag.intersection( box ) )

  
