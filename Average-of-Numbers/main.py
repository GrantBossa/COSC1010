#
# Grant Bossa
# October 15, 2024
# Average of Numbers Programming Project
# COSC 1010
#
# Instructions
# Assume a file containing a series of integers is named `numbers.txt` and exists on the computer’s disk. 
# Write a program that calculates the average of all the numbers stored in the file.   
#
# Define Variables
number = 0
counter = 0
sum = 0
average = 0

# Open file
myfile = open("numbers.txt", "r")
# Read file
for line in myfile:
    number = int(line)
    sum += number
    counter += 1
    average =sum/counter
    # Display file contents
    print(number)
print('Numbers found',counter, '\nSum = ' , sum , '\nAverage = ' , average )


# Close file
myfile.close()

# End Program