"""
This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).
"""

# prompt user for pattern
pattern = int(input("Enter the size of the pattern:"))

# initialize row counter
row = 0

while row < pattern:
# use for loop to print astericks in each row
    for column in range(pattern):
        print("*", end="")
        # move to the next line after one full row
    print()
    row += 1
