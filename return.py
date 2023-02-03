num = input( 'Enter An Integer:' ) # Requests integer input from user

def square( num ):
	
	if not num.isdigit(): # Displays message if entry is invalid 
		return 'Invalid Entry'

	num = int( num ) # Mulitplies the integer by itself 
	return num * num

print( num , 'Sqaured Is:' , square( num )) # Displays the output 