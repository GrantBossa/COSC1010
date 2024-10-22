#
# Grant Bossa
# October 21, 2024
# Lottery Number Generator Programming Project
# COSC 1010
#
# Design a program that generates a seven-digit lottery number. 
# The program should generate seven random numbers, each in the range of 0 through 9, 
# and assign each number to a list element. (Random numbers were discussed in Chapter 5.) 
# Then write another loop that displays the contents of the list.
#
# # Define Variables
lottery_number_list = []
MAX_DIGITS = 7
RANDOM_BOTTOM = 0
RANDOM_TOP = 9

import random

def main():
   # Generate a 7 digit lottery number
   # generate seven random numbers, each in the range of 0 through 9,
   # assign each number to a list element
   for index in range(MAX_DIGITS):
      lottery_number_list.append(random.randint(RANDOM_BOTTOM, RANDOM_TOP))

   # write another loop that displays the contents of the list
   print('Here is your 7 digit lottery number: ', end='')
   for index in range(MAX_DIGITS):
      print(lottery_number_list[index], end='')
              
main()

# End Program