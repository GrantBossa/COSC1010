#
# Grant Bossa
# November 24, 2024
# File Encryption and Decryption Programming Project
# COSC 1010 NT
#
# # Instructions  

# Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. 
# For example: codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, ... }
# Using this example, the letter `A` would be assigned the symbol `%`, the letter `a` would 
# be assigned the number `9`, the letter `B` would be assigned the symbol `@`, and so forth.
# The program should open a specified text file (text.txt is provided), read its contents, 
# then use the dictionary to write an encrypted version of the file’s contents to a second 
# file (encrypted.txt). Each character in the second file should contain the code for the 
# corresponding character in the first file.
# Write a second program that opens an encrypted file and displays its decrypted contents 
# on the screen. Use encrypted.txt.
#

def main():
   try:
      #  Open text.txt and Output file encrypted.txt
      myfile = open("text.txt", 'r' )
      writeFile = open("encrypted.txt",'w')

      textDict = {}     # create a dictionary of used characters in file
      buildList = []    # used for building the encrypted text
      # Read file into dictionary
      for line in myfile:  # read line
         for each in line:    # replace each character with its code
            if each == '\n':  # sparing the end of line marker as it was giving an error when I replaced it.
               writeString = "".join(buildList)       # convert to string
               writeFile.writelines(writeString+'\n') # write a line as it is encrypted
               buildList = []                         # reset for next line
            else:
               if each not in textDict:               # if char is not in dictionary, add it
                  textDict[each] = chr(ord(each)+1)   # add 1 to the base for each char. for future use random generator to create substitution list
               buildList += chr(ord(each)+1)         #  for each char in dictionary, write its complement char into another list

      #  close both files
      myfile.close()
      writeFile.close()
   except IOError:   # exceptions that are raised when the file is opened and data is read from it.
      print("An error occurred while opening the file." )
      exit()
   except:     # Default exception handler for any unaccounted for exceptions
      print("An unexpected error occurred.")
      exit()
      
main()
# End Program