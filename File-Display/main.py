#
# Grant Bossa
# October 15, 2024
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
#
# Define Variables
number = 0

# Open file
myfile = open("numbers.txt", 'r')
# Read file
for line in myfile:
    number = int(line)
    # Display file contents
    print(number)

# Close file
myfile.close()

# End Program