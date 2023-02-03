# Initializes a non-ASCII varible and displays it value, data type , and string length
s = 'Röd'
print('\nRed String:',s)
print('Type:',type(s),'\tLength:',len(s))

# Encode the string and display its value, data type, and string length
s = s.encode('utf-8')
print('\nEncoded String:',s)
print('Type:',type(s),'\tLength:',len(s))

# Decode the string and display its value, data type, and string length - to reveal that hexadecimal code point of the non-ASCII character 
s = s.decode('utf-8')
print('\nDecoded String:',s)
print('Type:',type(s),'\tLength:',len(s))

# Makes 'unicodedata' available and loop to reveal the unicode name of each character in the string 
import unicodedata
for i in range(len(s)):
    print(s[i],unicodedata.name(s[i]),sep = ':')

# Assign the varible a new value that includes a hexadecimal code point for a non-ASCII character then display the decoded string value
s = b'Gr\xc3\xb6n'
print('\nGreen String:',s.decode('utf-8'))

# Assign the varible another new value that includes a Unicode character for a non-ASCII character then display the string value
s = 'Gr\N{LATIN SMALL LETTER O WITH DIAERESIS}n'
print('Green String:',s)