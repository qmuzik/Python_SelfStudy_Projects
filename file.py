poem = 'I never saw a man who looked\n'
poem += 'With such a wistful eye\n'
poem += 'Upon that little tent of blue\n'
poem += 'Which prisoners call the sky\n'

# Creates a file object for a new text file to write into 
file = open('poem.txt','w')

# Write the string contained in the varible into the text file, then closes that file
file.write(poem)
file.close()

# Creates a file object for the existing text file to read from 
file = open('poem.txt','r')

# Display the contents of the text file and closes it 
for line in file:
    print(line,end = '')
file.close()

# Append a citation to the text file 
file = open('poem.txt','a')
file.write('(Oscar Wilde)')
file.close()