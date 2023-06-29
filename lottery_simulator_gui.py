from guizero import App, TitleBox, PushButton, Text
from random import randint

# Define the application window
app = App("Lottery Simulator", layout="grid", width=480, height=120)

# Define the first titlebox and its content
titlebox_one = TitleBox(app, text="1st Number", grid=[0, 0])
text_one = Text(titlebox_one, text="", size=14, font="Times New Roman")

# Define the second titlebox and its content
titlebox_two = TitleBox(app, text="2nd Number", grid=[1, 0])
text_two = Text(titlebox_two, text="", size=14, font="Times New Roman")

# Define the third titlebox and its content
titlebox_three = TitleBox(app, text="3rd Number", grid=[2, 0])
text_three = Text(titlebox_three, text="", size=14, font="Times New Roman")

# Define the fourth titlebox and its content
titlebox_four = TitleBox(app, text="4th Number", grid=[3, 0])
text_four = Text(titlebox_four, text="", size=14, font="Times New Roman")

# Define the fifth titlebox and its content
titlebox_five = TitleBox(app, text="5th Number", grid=[4, 0])
text_five = Text(titlebox_five, text="", size=14, font="Times New Roman")

# Define the sixth titlebox and its content
titlebox_six = TitleBox(app, text="6th Number", grid=[5, 0])
text_six = Text(titlebox_six, text="", size=14, font="Times New Roman")

# Generate random numbers
def generate_random_numbers():
    # Generate a number from 1 to 36
    number = randint(1, 36)

    # Define an empty list
    numbers = []

    # Create a generator
    while len(numbers) < 6:
        # Check if the generated number is in the list if it is add it
        if number not in numbers:
            numbers.append(number)

        # Generate a number from 1 to 36
        number = randint(1, 36)

    # Assign the generated numbers to the respective text widgets
    text_one.value = numbers[0]
    text_two.value = numbers[1]
    text_three.value = numbers[2]
    text_four.value = numbers[3]
    text_five.value = numbers[4]
    text_six.value = numbers[5]

# Define a pushbutton
button = PushButton(app, text="Generate Numbers",
                    command=generate_random_numbers, grid=[2, 1, 2, 1])

# Disable resizing the GUI
app.tk.resizable(0, 0)

# Show the application window
app.display()
