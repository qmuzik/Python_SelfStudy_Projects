for i in range( 1, 4 ): # Creates a loop that iterates 3 times

	for j in range( 1, 4 ): # Creates a nested loop that iterates 3 times 

		if i == 2 and j == 1 :# Creates a break  
			print( 'Breaks inner loop at i=2 and j=1' )
			break

		if i == 1 and j == 1 : # Creates a Continue
			print( 'Continue inner loop at i=1 j=1' )
			continue

		print( 'Running i =' , i , 'j =' , j ) # Displays the counter numbers 