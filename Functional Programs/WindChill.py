import math

def calculate_wind_chill(t, v):
    if t > 50 or v > 120 or v < 3:
        print("Invalid input: Temperature should be <= 50 and Wind Speed should be between 3 and 120 miles per hour.")
        return

    # Wind chill formula
    wind_chill = 35.74 + 0.6215 * t - 35.75 * math.pow(v, 0.16) + 0.4275 * t * math.pow(v, 0.16)
    
    print(f"Wind chill: {wind_chill:.2f}")

# Get input from the user
t = float(input("Enter the temperature in Fahrenheit (t): "))
v = float(input("Enter the wind speed in miles per hour (v): "))

# Calculate the wind chill
calculate_wind_chill(t, v)
