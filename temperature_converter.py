def celsius_to_fahrenheit(temp_C):
    temp_f = (temp_C * 9/5) + 32
    return temp_f

def fahrenheit_to_celsius(temp_F):
    temp_c = (temp_F - 32) * 5/9
    return temp_c

def kelvin_to_celsius(temp_K):
    temp_c = temp_K - 273.15
    return temp_c

# Display the options
options = int(input("\n1. Celsius to Fahrenheit"
                    + "\n2. Fahrenheit to Celsius"
                    + "\n3. Kelvin to Celsius"
                    + "\nPlease select an option: "))

# Process the options
if (options == 1):
    temp_c = float(input("\nPlease enter the temperature in Celsius: "))
    temp_f = celsius_to_fahrenheit(temp_c)
    print("The temperature in Fahrenheit is:", round(temp_f, 2))
elif(options == 2):
    temp_f = float(input("\nPlease enter the temperature in Fahrenheit: "))
    temp_c = fahrenheit_to_celsius(temp_f)
    print("The temperature in Celsius is:", round(temp_c, 2))
elif (options == 3):
    temp_k = float(input("\nPlease enter the temperature in Kelvin: "))
    temp_c = kelvin_to_celsius(temp_k)
    print("The temperature in Celsius is:", round(temp_c, 2))
else:
    print("Invalid input!")
