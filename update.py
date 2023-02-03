text = 'The political slogan "Workers Of The World Unite!" is from The Communist Manifesto.'

# Write the text string into a file and displays the current status in the "with" block
with open('update.txt','w') as file:
    file.write(text)
    print('\nFile Now Closed?:',file.closed)

# Add a non-indented statement after the "with" code block to display the file's new status
print('File Now Closed?:',file.closed)

# Re-open the file and display its contents to confirm it now contains the text string 
with open('update.txt','r+') as file:
    text = file.read()
    print('\nString:',text)

# Display the current file position, then reposition and display in that new position
    print('\nPosition In File Now:',file.tell())
    position = file.seek(33)
    print('Position In File Now:',file.tell())

# Overwrite the text from the current file position
    file.write('All Lands')

# Reposition in the file once more and overwrite the text from the new position 
    file.seek(59)
    file.write('the tombstone of Karl Marx.')

# Return to the start of the file and display its entire updated contents
    file.seek(0)
    text  = file.read()
    print('\nString:',text)