# Function that includes a docstring description
def display(s):
    # Multi Line Comment Below -- For Reference 
    '''Display an argument value'''
    print(s)

# Displays the function description 
display(display.__doc__)

# Displays a raw string value that contains the backslash character 
display(r'C:\Program Files')

# Displays a concatenation of two string values 
display('\nHello' + ' Python')

# Displays splice of specified strings within a range of element index numbers
display('Python In Easy Steps\n' [7:])

# Displays results of seeking characters
display('P' in 'Python')
display('p' in 'Python')