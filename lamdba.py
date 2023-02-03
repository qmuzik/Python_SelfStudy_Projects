def function_1( x ) : return x ** 2 # Defines three functions to return a passed argument to previous arguments
def function_2( x ) : return x ** 3
def function_3( x ) : return x ** 4

callbacks = [ function_1 , function_2 , function_3 ] # Creates a list of callbacks to call each function 

print( '\nNamed Functions:' )
for function in callbacks : print( 'Result:' , function( 3 )) # Display a heading and result of passing a value to each function

callbacks = \
[ lambda x : x ** 2 , lambda x : x ** 3 , lambda x : x ** 4 ] # Creates a list of callbacks to call each function 

print( '\nAnonymous Functions:' )
for function in callbacks : print( 'Result:' , function( 3 )) # Display a heading and result of passing a value to each function