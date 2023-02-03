import sys , keyword

# Displays Python version 
print( 'Python Version: ', sys.version)

# Display the location of the Python Interpreter on the System 
print( 'Python Interpreter Location:', sys.executable)

# Display list of all directories where interpreter looks for modulues 
print( 'Python Module Search Path:' )
for dir in sys.path:
    print( dir )

# Display all Python Keywords
print('Python Keywords: ')
for word in keyword.kwlist:
    print(word)