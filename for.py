chars = [ 'A' , 'B' , 'C' ] # Initializes a list, tuple, and dictionary 
fruit = ( 'Apple' , 'Banana' , 'Cherry' )
dict = { 'name' : 'Mike' , 'ref' : 'Python' , 'sys' : 'Win' }

print( '\nElements:\t' , end = ' ' ) # Displays all list elements  
for item in chars :
	print( item , end = ' ' )

print( '\nEnumerated:\t' , end = ' ' ) # Displays all list elements and relative index number 
for item in enumerate( chars ):
	print( item , end = ' ' )

print( '\nZipped:\t' , end = ' ' ) # Displays all list and tuple elements 
for item in zip( chars , fruit ):
	print( item , end = ' ' )

print( '\nPaired:' ) # Displays all key dictionary key names and associated element values 
for key , value in dict.items():
	print( key , '=' , value )