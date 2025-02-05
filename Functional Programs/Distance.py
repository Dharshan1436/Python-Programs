import math

x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))

distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

print(f"Distance from ({x}, {y}) to (0, 0) is: {distance}")
