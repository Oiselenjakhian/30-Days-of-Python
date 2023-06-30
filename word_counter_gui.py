from guizero import App, Text, TextBox, Box, PushButton

# Function to find the number of words in the text box
def find_words():
    # Get the text from the input box
    input_text = input_box.value
    
    # Use the split function to seperate the text into a list
    input_list = input_text.split()
    
    # Find the length of the list
    length_list = len(input_list)
    
    # Display the result in the instruction textbox
    instruction_text.value = "There are " + str(length_list) + " word(s)."

# Define the application window
app = App("Word Counter", width=480, height=480)

# Define the instruction to the user
instruction_text = Text(app, text="Paste you text in the textbox below")

# Define the input box
input_box = TextBox(app, width="fill", height="fill", multiline=True)

# Define a push button and add it to the bottom box
push_button = PushButton(app, text="Find the Number of Words", command=find_words)

# Disable resizing the GUI
app.tk.resizable(0, 0)

# Show the application window
app.display()





