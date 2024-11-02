#
# Grant Bossa
# October 31, 2024
# Magic 8 Ball Programming Project
# COSC 1010 NT
#
# Instructions Write a program that simulates a Magic 8 Ball, which is a fortune telling toy that displays 
# a random response to a yes or no question. In the student sample programs for this book, you will find a 
# text file named 8_ball_responses.txt. The file contains 12 responses, such as “I don’t think so”, 
# “Yes, of course!”, “I’m not sure”, and so forth. 
# The program should read the responses from the file into a list. 
# It should prompt the user to ask a question, then display one of the responses, randomly selected from the list. 
# The program should repeat until the user is ready to quit.
#

import random

def main():
   try:
      # Define Variables
      counter = 0
      responses = []

      # read the responses from the file into a list
      # Open file
      myfile = open("COSC1010\Magic-8-Ball\8_ball_responses.txt", "r")
      for line in myfile:
         counter += 1
         responses.append(line)
      
      # prompt the user to ask a yes/no question
      # randomly select from the list then display one of the responses
      # repeat until the user is ready to quit
      print("This is a program that simulates a Magic 8 Ball, which is \na fortune telling toy that displays a random response to a yes or no question. \nI will prompt you to ask a question, then display a response. \nI will repeat until you are ready to quit.")
      while (input("Type 'quit' to stop the game, or Enter a yes/no question. ").lower() != "quit"):
         # generate a random number between 1 and the total number of responses
         random_index = random.randint(1, counter)
         print(responses[random_index-1].strip())
      # Be Polite
      print("Goodbye!")
      # Close file
      myfile.close()
      
   except IOError:   # exceptions that are raised when the file is opened and data is read from it.
      print("An error occurred while opening the file." )
      exit()
   except:     # Default exception handler for any unaccounted for exceptions
      print("An unexpected error occurred.")
      exit()
      
main()
# End Program