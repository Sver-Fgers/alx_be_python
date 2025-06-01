"""
This script prompts the user for the current weather and provides clothing
recommendations using if, elif, and else statements.
"""

# Prompt the user for weather condition
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide clothing advice based on weather
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
