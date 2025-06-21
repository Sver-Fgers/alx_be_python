# this script implements a division calculator that robustly handles errors like 
# division by zero and non-numeric inputs using command line arguments

def safe_divide(numerator, denominator):
    # try:
        
    #     division = int(numerator)/int(numerator)

    #     if denominator == 0:
    #         raise ZeroDivisionError
    #     else:
    #         return f"division successful: {numerator/denominator}"
    #     if float()
    # except ZeroDivisionError:
    #     print("division by zero is not allowed")
    # except ValueError:

    # try:
    #     num1 = int(numerator)
    #     num2 = int(denominator)

    #     # Try to divide the numbers
    #     result = num1 / num2
    #     print(f"The result of {num1} divided by {num2} is: {result}")

    # except ZeroDivisionError:
    #     print("Error: You cannot divide by zero!")

    # except ValueError:
    #     print("Error: Please enter valid numbers.")

    try:
        # First try converting inputs to floats
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        result = num / den
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."