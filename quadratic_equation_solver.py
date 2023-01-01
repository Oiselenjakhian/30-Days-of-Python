import math

# Ask the user for the coefficient of x squared
coeff_a = float(input("Please enter the coefficient of x squared: "))

# Ask the user for the coefficient of x
coeff_b = float(input("Please enter the coefficient of x: "))

# Ask the user for the coefficient of the constant
coeff_c = float(input("Please enter the coefficient of the constant: "))

# Compute the discriminant
discriminant = (coeff_b * coeff_b) - (4 * coeff_a * coeff_c)

# If the discriminant is greater than zero, print "Distinct Roots", calculate the values of x1 and x2
if (discriminant > 0):
    # Print out the type of root
    print("Distinct Roots")
    
    # Find the values of the roots
    x1 = (-coeff_b + math.sqrt(discriminant)) / 2 * coeff_a
    x2 = (-coeff_b - math.sqrt(discriminant)) / 2 * coeff_a

    print(x1, x2)
    
# Else if the discriminant is equal to zero, print "Double Roots", calculate the value of x
elif (discriminant == 0):
    # Print out the type of root
    print("Double Roots")

    # Find the value of the root
    x = -coeff_b / 2 * coeff_a

    print(x)
    
# Else print "Complex Roots"
else:
    # Print out the type of root
    print("Complex Roots")
