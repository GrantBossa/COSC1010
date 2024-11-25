#
# Grant Bossa
# November 13, 2024
# Capital Quiz Programming Project
# 24/FA COSC 1010 NT
#
# Use comments liberally throughout the program. 
# Instructions
# Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as values. 
# (Use the Internet to get a list of the states and their capitals.)
# The program should then randomly quiz the user by displaying the name of a state and asking the user to enter that state’s capital.
# The program should keep a count of the number of correct and incorrect responses. 
# (As an alternative to the U.S. states, the program can use the names of countries and their capitals.)

import random

def main():
    # Initialize dictionary
    capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

    # Local variables
    quitGame = False        # indicator for end of game loop
    promptState = ""        # variable for prompt
    answerCapital = ""      # variable for answer
    randomSelection = 0     # random selection index for list
    answersCorrect = 0      # accumulator for answers correct
    answersIncorrect = 0    # accumulator for answers incorrect
    myList = list(capitals) # workable list for indexing
    myAnswers = []          # list for end of game
    trackSelections = []    # Previous selections so random doesn't duplicate questions
    
    # Randomly quiz the user by displaying the name of a state and asking the user to enter that state’s capital.
    while not quitGame :
        # get random state records between 1 and length of dictionary
        randomSelection = random.randint(1, len(capitals))
        # if previous selection within 5 questions, get another random
        while randomSelection in trackSelections[-5:] :
            # duplicate random, trying again...
            randomSelection = random.randint(1, len(capitals))
        trackSelections.append(randomSelection)

        # Get the prompted state for the user.
        promptState = myList[randomSelection-1]

        # Display the prompt to the user.
        # Get the user's answer.
        answerCapital = input("What is the capital of "+ promptState + "? ").strip()
        # If no answer - quit game
        if answerCapital =="" :
            quitGame = True
        else :
            # do the answers match?
            # print congratulations and accumulate count of correct and incorrect responses.
            if answerCapital.lower() == capitals.get(promptState).lower() :
                print ("Correct!  "+ answerCapital +" is the capital of ", promptState)
                answersCorrect += 1
                myAnswers.append(f"{True} {answerCapital} = {capitals.get(promptState)}")
                
            else :
                print("Sorry, that's incorrect. The correct capital is ", capitals.get(promptState))
                answersIncorrect += 1
                myAnswers.append(f"{False} {answerCapital} != {capitals.get(promptState)}")
                
        # Continue messages until user quits the game. 
        if quitGame:
            print("You had: \n", answersCorrect, " answers Correct \n", answersIncorrect, " answers Incorrect")
            print("Your answers were: ", myAnswers ) # rough attempt at getting paired answers.
            print("Thank you for playing!")
        else:
            # print("You have: \n", answersCorrect, " answers Correct \n", answersIncorrect, " answers Incorrect\nLeave entry blank to quit.")
            print("Leave entry blank to quit.")

# Call the main function.
main()
