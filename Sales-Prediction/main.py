#
# Grant Bossa
# Sept 6, 2024
# Sales Prediction Programming Project
# COSC 1010 
#

# Variables to hold the sales total and the profit
projectedSalesTotal = 0
projectedProfit = 0

# Get the amount of projected sales.
projectedSalesTotal = float(input('Please enter the Projected Sales Total : $'))

# Calculate the projected profit.
projectedProfit= .23*projectedSalesTotal

# Print the projected prof0it.
print('With sales of $', format(projectedSalesTotal,',.2f'),'\n' , 'The projected profit will be $', format(projectedProfit,',.2f'))
