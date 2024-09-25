#
# Grant Bossa  
# September 24, 2024
# Kilometer Converter Programming Project
# COSC 1010 NT
#
# Instructions
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles. 
# The conversion formula is as follows: Miles = Kilometers x 0.6214
#
# Declare Variables
CONVERSION_FROM_KM_TO_MILES = 0.6214    # constant for the conversion rate from kilometers to miles
input_km = 0

# Prompts the user to enter a distance in kilometers then displays that distance in miles.
def main():
    # Prompt the user to enter a number of kilometers
    input_km = float(input("Enter a number of kilometers: "))   # Used a float so that decimals can be used
    # Display the distance in miles
    km_to_miles(input_km)
# end of function

# Function converts km distance to miles and displays the results
def km_to_miles(km):
    miles = km * CONVERSION_FROM_KM_TO_MILES
    # displays the kilometer distance in miles.
    print(f"{km} kilometers is equal to {miles: .4f} miles.")
# end of function 

# Call the main function
main()

# end of program