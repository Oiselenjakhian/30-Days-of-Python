from random import randint

# Generate a random number from 1 to 36
number = randint(1, 36)

# Initialize an empty list
numbers = []

# Generate 6 random unique numbers
while len(numbers) < 6:
    # Add a number to the list if it is not already in the list
    if number not in numbers:
        numbers.append(number)

    # Generate a random number from 1 to 36
    number = randint(1, 36)

# Display the generated numbers
for number in numbers:
    print(number)
