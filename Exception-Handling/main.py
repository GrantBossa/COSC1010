#
# Grant Bossa
# October 21, 2024
# Exception Handling Programming Project
# COSC 1010
#
# Instructions
# -   Assume a file containing a series of integers is named `numbers.txt` and 
# exists on the computer’s disk. 
#
# -   Write a program that calculates the average of all the numbers stored in the file.
# 
# -   Modify the program that you wrote for `Average of Numbers` so it handles 
# the following exceptions:
# -   It should handle any `IOError` exceptions that are raised when the file 
#  is opened and data is read from it.
#
# -   It should handle any `ValueError` exceptions that are raised when the items 
# that are read from the file are converted to a number.   
#
def main():
   try:
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
      print('Numbers found',counter, '\tSum = ' , sum , '\tAverage = ' , average )
      
      # Close file
      myfile.close()
      
   except IOError:   # exceptions that are raised when the file is opened and data is read from it.
      print("An error occurred while opening the file." )
      exit()
   except ValueError as err:  # exceptions that are raised when the items that are read from the file are converted to a number.
      print("An error occurred while converting the data to a number." )
      exit()
   except:     # Default exception handler for any unaccounted for exceptions
      print("An unexpected error occurred.")
      exit()
      
main()
# End Program