dict = { 'name' : 'Bob' , 'ref' : 'Python' , 'sys' : 'Win' } # Initializes a dictionary and displays its key:value contents
print( 'Dictionary:' , dict )

print( '\nReference:' , dict[ 'ref' ] ) # Displays a single value referenced by its key
print( '\nKeys:' , dict.keys() ) # Displays all keys within the dictionary 

del dict[ 'name' ] # Delete one pair from dictionary and adds a replacement pair then display the new key:value contents
dict[ 'user' ] = 'Tom'
print( '\nDictionary:' , dict )

print( '\nls There A name Key?:' ,'name' in dict ) # Search the dictionary for a specific key and displays it 
