# This function, perform_operation, takes two numbers and a string indicating the operation ('add', 'subtract', 'multiply', or 'divide').
# It performs the specified arithmetic operation and handles division by zero with a special return value or message for main.py to handle.

def perform_operation(num1, num2, operation):
    if operation == "add":
        add = num1 + num2
        return add
    elif operation == "subtract":
        subtract = num1 - num2
        return subtract
    elif operation == "multiply":
        multiply = num1 * num2
        return multiply
    elif operation == "divide":
        if num2 != 0:
            divide = num1 / num2
            return divide
        else:
            return "Error: Cannot divide by zero"
    else:
        print("Enter a valid operation")
