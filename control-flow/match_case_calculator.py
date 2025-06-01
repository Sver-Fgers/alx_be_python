"""
This calculator will prompt the user to enter two numbers and select an operation
(addition, subtraction, multiplication, or division).
It uses a match-case statement to perform the operation and display the result.
"""

# Prompt the user for input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Choose the operation to perform
operation = input("Choose the operation (+, -, *, /): ")

# Perform the operation using match-case
match operation:
    case "+":
        addition = num1 + num2
        print("The result is", addition)
    case "-":
        subtract = num1 - num2
        print("The result is", subtract)
    case "*":
        multiply = num1 * num2
        print("The result is", multiply)
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            divide = num1 / num2
            print("The result is", divide)
    case _:
        print("Invalid operation selected.")
