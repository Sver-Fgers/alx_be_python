#This script demonstrates how to use the datetime module for handling dates and times in Python

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)

    days_input = input("Enter number of days to add: ")
    
    def calculate_future_date(number_of_days):
        # Simple error handling
        future_date = current_date + timedelta(days=number_of_days)
        formatted = future_date.strftime("%Y-%m-%d")
        return formatted
    
    if days_input.isdigit():
        days = int(days_input)
        print("Future date:", calculate_future_date(days))
    else:
        print("Invalid input. Please enter a positive whole number.")
        
        
        
display_current_datetime()

        

        