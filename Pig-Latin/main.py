#
# Grant Bossa
# November 4, 2024
# Pig Latin Programming Project
# COSC 1010
#
# Instructions:
# Write a program that reads a sentence as input and converts each word to “Pig Latin.” 
# In one version, to convert a word to Pig Latin, you 
# remove the first letter and place that letter at the end of the word. 
# Then you append the string “ay” to the word. Here is an example: 
# ```
# English: I SLEPT MOST OF THE NIGHT 
# Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY
# ```
def main():
   # Variables
   sentence=""             # Input Sentence
   words=[]                # Used to keep track of the words in the sentence
   first_letter = ""       # First letter of each word
   pig_latin_word = []     # Empty list to create the Pig Latin word
   pig_latin_words = []    # Initialize an empty list to store the Pig Latin words
   pig_latin_sentence = [] # Empty list to store the Pig Latin Sentence

   # Input a sentence
   sentence = input("Enter a sentence to convert to Pig Latin: ")

   # Split the sentence into a list of words
   words = sentence.split()

   # Step through each word and convert it to Pig Latin
   for word in words:
      # take the first letter and place it last in the word
      first_letter = word[0].lower()
   
      # remove the first letter and append it to the end of the word
      pig_latin_word = word[1:].lower() + first_letter + "ay"
   
      # append the Pig Latin word to the list
      pig_latin_words.append(pig_latin_word)

   # Join the Pig Latin words back into a sentence
   pig_latin_sentence = " ".join(pig_latin_words)

   # Output the Pig Latin sentence
   print("Here is your sentence in pig Latin: " +pig_latin_sentence)


# Call the main function

main()

# End of Program