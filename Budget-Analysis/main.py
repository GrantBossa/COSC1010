#
# Grant Bossa
# Sept 18, 2024
# Budget Analysis Programming Project
# COSC 1010 NT
#
# Instructions:
# Write a program that asks the user to enter the amount that he or she has budgeted for a month. 
# A loop should then prompt the user to enter each of his or her expenses for the month and keep a running total. 
# When the loop finishes, the program should display the amount that the user is over or under budget.
# Use comments liberally throughout the program. 
#
# Variables:
budget = 0  # budget amount
monthly_expense = 0   # total of expenses for the month
running_total = 0   # running total of expenses
keep_going = True   # loop control variable

# asks the user to enter the amount that he or she has budgeted for a month
budget = float(input("Enter your monthly budget: "))

# loop
# enter expenses for the month
while keep_going:
    monthly_expense = float(input("Enter your monthly expense: "))
    # keep a running total
    running_total += monthly_expense
    # ask the user if they want to enter another expense
    # if the user doesn't want to enter another expense, break the loop
    keep_going = input("Do you want to continue? (y/n): ").lower() == "y"
# end loop

# display the amount that the user is over or under budget
if running_total > budget:
    print(f"You are over budget by ${running_total - budget: .2f}.")
elif running_total < budget:
    print(f"You are under budget by ${budget - running_total: .2f}.")
else:
    print("You are exactly on budget.")



# end of program
