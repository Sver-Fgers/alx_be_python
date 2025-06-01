"""
This script prompts the user to enter a number and then uses a for loop
to print the multiplication table for that number from 1 to 10.
"""

# Prompt user for input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print the multiplication table
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
