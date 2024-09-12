#
# Grant Bossa
# Sept 11, 2024
# Areas of Rectangles Programming Project
# COSC 1010 NT
#
# Get rectangle length A and width A
lengthA = float(input("Enter the length of rectangle A: "))
widthA = float(input("Enter the width of rectangle A: "))

# Get rectangle length B and width B 
lengthB = float(input("Enter the length of rectangle B: "))
widthB = float(input("Enter the width of rectangle B: "))

# Calculate area A and area B
areaA = lengthA * widthA
areab = lengthB * widthB

# Print area comparison using if-elif-else statements
if areaA > areab:print("Rectangle A has a greater area.")
elif areaA < areab:print("Rectangle B has a greater area.")
else: print("Both rectangles have the same area.")

# end of program #
