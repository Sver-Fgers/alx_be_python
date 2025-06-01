"""
This script will ask the user for a single task, its priority level, and if it is time-sensitive.
The program will then provide a customized reminder for that task, demonstrating control flow and loops
without relying on data structures to store multiple tasks.
"""

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to finish it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task with a deadline. Plan your time wisely.")
        else:
            print(f"Note: '{task}' is a medium priority task. Schedule it when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but time-sensitive. Don't leave it too late.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider doing it in your free time.")
    case _:
        print("Invalid priority entered. No reminder set.")
