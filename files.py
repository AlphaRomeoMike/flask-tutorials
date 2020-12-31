# Pythin can create, read, update and delete

# Open a file
myFile = open('myfile.txt', 'w')

# Get info 
print('Name: ', myFile.name)
print('Is close: ', myFile.closed)
print('Mode: ', myFile.mode)

# Write in file
myFile.write("I love Python ")
myFile.write('and PHP')
myFile.close()

# Append to a file
myFile = open('myfile.txt', 'a')
myFile.write(' Also, I like JavaScript')

# Read from a file
myFile = open('myfile.txt', 'r+' )
text = myFile.read(100)
print(text)