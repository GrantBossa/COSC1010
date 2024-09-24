#
# Grant Bossa
# Septemtber 24, 2024
# Feet to Inches Programming Project
# COSC 1010 NT
#
# Instructions:
# One foot equals 12 inches. 
# Write a function named feet_to_inches that accepts a number of feet as an argument and 
# returns the number of inches in that many feet. 
# Use the function in a program that prompts the user to enter a number of feet 
# then displays the number of inches in that many feet.
#
# Declare variables
INCHES_PER_FOOT = 12       # Constant for number of inches per FileNotFoundError
input_feet = 0             # Number of feet from user


# Write a function named feet_to_inches that accepts a number of feet as an argument and 
# returns the number of inches in that many feet. 
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT
# end of function feet_to_inches

# Prompts the user to enter a number of feet then displays the number of inches in that many feet.
def main():
    # Prompt the user to enter a number of feet
    input_feet = float(input("Enter a number of feet: "))   # Used a float so that decimals can be used

    # displays the number of inches in that many feet.
    print(f"{input_feet} feet is equal to {feet_to_inches(input_feet):.2f} inches.")
# end of function main

# Call the main function
main()

# End of Program
