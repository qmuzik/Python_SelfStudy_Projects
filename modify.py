string = 'python in easy steps'

# Display the string capitalized, titled, and centered
print('\nCapitalized:\t',string.capitalize())
print('\nTitled:\t\t',string.title())
print('\nCentered:\t',string.center(30,'*'))

# Display the string uppercased and merged with a sequence of two asterisks
print('\nUppercase:\t',string.upper())
print('\nJoined:\t\t',string.join('**'))

# Display the string padded with asterisks on the left
print('\nJustified:\t',string.rjust(30,'*'))

# Display the string with all occurances of 's' replaced by asterisks
print('\nReplaced:\t',string.replace('s','*'))