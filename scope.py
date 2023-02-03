global_var = 1 # Declares the global varible as 1

def my_vars(): # Defines My Varibles as Global Varible and Local varible, then displays the output
	print( 'Global Varible:' , global_var)
	local_var = 2
	print( 'Local varible:' , local_var)
	global inner_var
	inner_var = 3

my_vars() # Displays the output of Coerced Global varible 
print( 'Coerced Global:' , inner_var )