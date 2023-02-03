def echo( user , lang , sys ): # Defines the echo function and displays output
	print ( 'User:', user, 'Language:', lang, 'Platform:', sys )

echo( 'Mike', 'Python' , 'Windows' ) # Displays output of string values in preferred order 
echo( lang = 'Python' , sys = 'Mac OS' , user = 'Anne' ) # Assigns argument values to string values 

def mirror( user = 'Carole' , lang = 'Python' ): # Defines the mirror function and displays output
	print( '\nUser:' , user , 'Language:' , lang )

mirror() # Calls the function and overrides the default values 
mirror( lang = 'Java' )
mirror( user = 'Tony' )
mirror( 'Susan' , 'C++' )
