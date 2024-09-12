#
# Grant Bossa
# Sept 11, 2024
# Hot Dog Cookout Calculator Programming Project
# COSC 1010 NT#

# Instructions for this program :
# 
# Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. 
# Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns 
# needed for a cookout, with the minimum amount of leftovers. 
# The program should ask the user for:
#   the number of people attending the cookout 
#   the number of hot dogs each person will be given
# 
# The program should display the following details:
#
#- The minimum number of packages of hot dogs required
#- The minimum number of packages of hot dog buns required
#- The number of hot dogs that will be left over
#- The number of hot dog buns that will be left over


# constants:

HOT_DOGS_PER_PKG = 10
HOT_DOGS_BUNS_PER_PKG = 8


# get user input for the number of people and the number of hot dogs each person will be given

number_of_people = int(input("Enter the number of people attending the cookout: "))
number_of_hot_dogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

# Number of hot dogs needed
nohdn=number_of_people * number_of_hot_dogs_per_person 

# calculate the number of hot dog packages needed
if(nohdn/HOT_DOGS_PER_PKG)>(int(nohdn/HOT_DOGS_PER_PKG)):   # if a decimal vs an integer
    nohdpn = int(nohdn/HOT_DOGS_PER_PKG)+1                  # then force rounding up 
else : nohdpn = int(nohdn/HOT_DOGS_PER_PKG)                 # else value is okay

# calculate the number of leftover hot dogs 
nolohd = nohdpn*HOT_DOGS_PER_PKG - nohdn

# Number of hot dog buns needed are the same as the number of hot dogs needed
nohdbn=nohdn 

if(nohdbn/HOT_DOGS_BUNS_PER_PKG)>(int(nohdbn/HOT_DOGS_BUNS_PER_PKG)):   # if a decimal vs an integer
    nohdbpn = int(nohdbn/HOT_DOGS_BUNS_PER_PKG)+1                       # then force rounding up 
else : nohdbpn = (nohdbn/HOT_DOGS_BUNS_PER_PKG)                         # else value is okay

# calculate the number of leftover hot dogs 
nolohdb = nohdbpn*HOT_DOGS_BUNS_PER_PKG - nohdbn


# display the results

print('......................')
print("Minimum number of hot dog packages needed:", int(nohdpn))

print("Minimum number of hot dog bun packages needed:", int( nohdbpn))

print('......................')

print("Number of left over hot dogs:", int(nolohd))

print("Number of left over hot dog buns:",int( nolohdb))

# end of program #
