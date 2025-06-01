"""
This script will ask the user to enter a number,
then use a for loop to print the multiplication table for that number from 1 to 10.
"""

# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Print the multiplication table
for multiplier in range(1, 11):
    product = number * multiplier
    print(number, "x", multiplier, "=", product)
