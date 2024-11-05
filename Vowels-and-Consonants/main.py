#
# Grant Bossa
# November 4, 2024
# Vowels and Consonants Programming Project
# COSC 1010
#
# Instructions: 
# Write a program with a function that accepts a string as an argument and 
# returns the number of vowels that the string contains. 

# The application should have another function that accepts a string as an argument and 
# returns the number of consonants that the string contains. 

# The application should let the user enter a string, and should 
# display the number of vowels and the number of consonants it contains.
#
# Use comments liberally throughout the program. 

# The count_vowels function returns the number of vowels in the string passed as an argument,
def count_vowels(string):
   # Variables 
   vowels = ['a', 'e', 'i', 'o', 'u']  # List of vowels
   vowel_count = 0                     # variable to keep track of the number of vowels
   
   # Test each character in the string to see if it is a vowel
   for char in string:
      # Check if the character is a vowel (ignoring case)
      if char.lower() in vowels:
         # If it is, increment the vowel count
         vowel_count += 1
   # Return the count of vowels
   return vowel_count

# The count_consonants function returns the number of consonants in the string passed as an argument,
def count_consonants(string):
   # Variables 
   vowels = ['a', 'e', 'i', 'o', 'u']  # List of vowels
   consonant_count = 0                 # variable to keep track of the number of consonants
    
   # Test each character in the string to see if it is a consonant
   for char in string:
      # Check if the character is alphabetic and a consonant (ignoring case)
      if char.isalpha() and char.lower() not in vowels:
         # If it is, increment the consonant count
         consonant_count += 1
   # Return the count of consonants
   return consonant_count

# main function
def main():
   # Prompt the user to enter a string
   user_input = input("Enter a string: ")

   # Display the number of vowels and consonants in the string
   print("That string has ", count_vowels(user_input), " vowels and ",count_consonants(user_input), " consonants.")

main()

# End of Program