chars = [ 'Alpha' , 'Beta' , 'Gamma' , 'Delta' , 'Epsilon' ]

def display( elem ) :

	assert type( elem ) is int , 'Argument Must Be Integer!'
	print( 'List Elements' , elem , '=' , chars[ elem ])

elem = 4
display( elem )

elem = elem / 2
display( elem )
