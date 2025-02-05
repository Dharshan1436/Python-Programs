import math


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant (delta)
delta = b * b - 4 * a * c

# Check if delta is non-negative (i.e., real roots exist)
if delta >= 0:
    # Calculate the two roots
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)
    
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
else:
    print("The equation has no real roots.")
