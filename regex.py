from re import*

# Initialize pattern varible with regular expression object
pattern = \
    compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')

# Defines get_address function by requesting user input and attempt to match with that pattern
def get_address():
    address = input('Enter Your Email Address:')
    is_valid = pattern.match(address)

    # Displays messages based on attempt succeeded
    if is_valid: 
        print('Valid Address:' , is_valid.group())
    else:
        print('Invalid Address! Please Retry...\n')

# Calls the function
get_address()

