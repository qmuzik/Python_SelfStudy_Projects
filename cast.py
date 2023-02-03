a = input( 'Enter A Number: ')
b = input( 'Now Enter Another Number: ')

sum = a + b # Display concatenated string value result
print( '\nData Type sum :' , sum , type( sum )) 

sum = int( a ) + int( b ) # Display integer value result 
print( 'Data Type sum :' , sum , type( sum ))

sum = float( sum ) # Display total float value
print( 'Data Type sum :' , sum ,type( sum ))

sum = chr( int( sum )) # Display a character string value 
print( 'Data Type sum :' , sum , type( sum ))