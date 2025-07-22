WATER_USAGE = 10  # This code defines a constant for water usage in liters.
CO2_MILE = 5  # This code defines a constant for CO2 emissions per mile in kg.
CO2_MEAL = 2  # This code defines a constant for CO2 emissions per meal in kg.

# List of input prompts 
prompts = [
    int(input("How many showers do you take per week? ")),
    int(input("How long is your average shower in minutes? ")),
    int(input("How many meals do you eat per week? ")),
    int(input("How many miles do you drive per week? "))
]
# Match the list values into one specific variable
showers_taken, shower_time, meals_eaten, miles_driven = prompts

# Print the collected data
print(f"\nYou take {showers_taken} showers per week.")
print(f"You spend {shower_time} minutes in the shower on average.")
print(f"You eat {meals_eaten} meals per week.")
print(f"You drive {miles_driven} miles per week.")

# Calculate total water usage per week
total_water_usage = showers_taken * WATER_USAGE * shower_time
print(f"You use {total_water_usage:} liters of water per week.")

# Calculate total CO2 emissions per week
total_co2_meals = meals_eaten * CO2_MEAL 
total_co2_miles = miles_driven * CO2_MILE
print(f"You produce {total_co2_meals + total_co2_miles:} kg of CO2 per week.")