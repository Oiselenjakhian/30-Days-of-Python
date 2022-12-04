import math

# Explain the purpose of the program
print("This is a program to find the area of a circle")

# Ask the user for the radius of the circle
radius = float(input("Please enter the radius of the circle: "))

# Multiply the radius by itself and the value of pi
area = radius * radius * math.pi

# Round up the area to 2 decimal places
area = round(area, 2)

# Display the area
print(area)
