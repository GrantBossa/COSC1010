#
# Grant Bossa
# Sept 6, 2024
# Sales Tax Programming Project
# COSC 1010
#

# Variable declarations
purchase_amount = 0     # The amount of the purchase
state_sales_tax_amount = 0    # The state sales tax
county_sales_tax_amount = 0    # The county sales tax
total_sales_tax_amount = 0   # The total sales tax
total_sale_amount = 0  # The total of the sale

# Constants for the state and county tax rates
STATE_SALES_TAX_RATE = 0.05    # The state sales tax rate
COUNTY_SALES_TAX_RATE = 0.025    # The county sales tax rate

# Get the amount of the purchase.
purchase_amount = float(input("Enter the amount of the purchase: $"))

# Calculate the state sales tax. Assume 5 percent.
state_sales_tax_amount = purchase_amount * STATE_SALES_TAX_RATE

# Calculate the county sales tax. Assume 2.5 percent.
county_sales_tax_amount = purchase_amount * COUNTY_SALES_TAX_RATE

# Calculate the total tax.
total_sales_tax_amount = state_sales_tax_amount + county_sales_tax_amount

# Calculate the total of the sale.
total_sale_amount = purchase_amount + total_sales_tax_amount

# Print information about the sale.
print("Purchase Amount: $", purchase_amount) # The amount of the purchase
print("State Sales Tax: $", format(state_sales_tax_amount, ",.2f")) # The state sales tax
print("County Sales Tax: $", format(county_sales_tax_amount, ",.2f")) # The county sales tax
print("Total Sales Tax: $", format(total_sales_tax_amount, ",.2f")) # The total sales tax
print("Total Sale Amount: $", format(total_sale_amount, ",.2f")) # The total of the sale

