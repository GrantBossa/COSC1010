#
# Grant Bossa
# Sept 19, 2024
# Bug Collector Programming Project
# COSC 1010 NT
#
# A bug collector collects bugs every day for five days. 
# Write a program that keeps a running total of the number of bugs collected during the five days. 
# The loop should ask for the number of bugs collected for each day, and 
# when the loop is finished, the program should display the total number of bugs collected.
#
# Initialize variables for bugs and total number of bugs collected.
total_running = 0               # running total of bugs collected.
bugs_collected_daily = 0    # total number of bugs collected.
counter_day = 0                 # counter for the day.

# Get number of bugs collected each day using a for loop.
for counter_day in range(5):
    print(f"Day {counter_day + 1}:", end=" " * 5)
    bugs_collected_daily = int(input("Enter the number of bugs collected: "))
    total_running +=  bugs_collected_daily  # add the daily bugs collected to the running total.

# Display the total number of bugs collected.
print(f"Total number of bugs collected over the five days: {total_running}")

# End of program.