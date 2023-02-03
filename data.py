import pickle,os

# Test if specific data file does not already exist 
if not os.path.isfile('pickle.dat'):

    # Create a list of two elements if the specified file is not found
    data = [0,1]

    # Request user data to be assigned to each of the list elements
    data[0] = input('Enter Topic: ')
    data[1] = input('Enter Series: ')

    # Create a binary file for writing to
    file = open('pickle.dat','wb')

    # Dump values contained in the varibles as data into the binary file 
    pickle.dump(data,file)

    # Closes the file
    file.close()

# Open an existing file to read from if a specific data file does already exist
else:
    file = open('pickle.dat','rb')

    # Load the data stored in that existing file into a varible then close the file
    data = pickle.load(file)
    file.close()

    # Display the restored data
    print('\nWelcome Back To:',data[0],data[1])