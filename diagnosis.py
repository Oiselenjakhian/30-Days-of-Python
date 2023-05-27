# Explain the purpose of the program to the user
print('This is a BMI Calculator')

# Ask the user for their weight
weight = float(input('Please enter your weight: '))

# Ask the user for their height
height = float(input('Please enter your height: '))

# Calculate the BMI of the user
BMI = weight / (height * height)

# Round up the BMI to 1 decimal place
BMI = round(BMI, 1)

# Display the BMI
print(BMI)

# Evaluate the BMI based on the BMI table and give a diagnosis
if (BMI < 18.5):
    print('Underweight')
elif ((BMI >= 18.5) and (BMI < 25)):
    print('Healthy Weight')
elif ((BMI >= 25) and (BMI < 30)):
    print('Overweight')
else:
    print('Obese')
