# Creates a file object for a new text file to write in
file  = open('example.txt','w')

# Displays the file name and mode
print('File Name:',file.name)
print('File Open Mode:',file.mode)

# Displays the file access permissions 
print('Readable:',file.readable())
print('Writable:',file.writable())

# Defines function to determine file status
def get_status(f):
    if(f.closed != False):
        return 'Closed'
    else:
        return 'Open'

# Display the current file status, closes the file, and display the file status once more 
print('File Status:',get_status(file))
file.close()
print('\nFile Status:',get_status(file))