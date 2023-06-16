# Explain the purpose of the program
print("This is a quiz about Nigeria")

# Initialize the score variable
score = 0

# Display the first question
question1 = input("In what year did Nigeria gain independence?" +
                  "\na) 1957" +
                  "\nb) 1960" +
                  "\nc) 1963" +
                  "\nd) 1966" +
                  "\nPlease select an option: ")

# Process the result
if (question1.lower() == "b"):
    score = score + 1
    print("Your answer is correct!")
else:
    print("Your answer is wrong!")
    print("The correct answer is b 1960")

# Display the second question
question2 = input("In what year did the Nigerian civil war end?" +
                  "\na) 1967" +
                  "\nb) 1968" +
                  "\nc) 1969" +
                  "\nd) 1970" +
                  "\nPlease select an option: ")

# Process the result
if (question2.lower() == "d"):
    score = score + 1
    print("Your answer is correct!")
else:
    print("Your answer is wrong!")
    print("The correct answer is d) 1970")

# Display the third question
question3 = input("Who led the first war against Nigeria?" +
                  "\na) Gani Adam" +
                  "\nb) Ibrahim Babangida" +
                  "\nc) Adaka Boro" +
                  "\nd) Odumegwu Ojukwu" +
                  "\nPlease select and option: ")

# Process the result
if (question3.lower() == "c"):
    score = score + 1
    print("Your answer is correct!")
else:
    print("Your answer is wrong!")
    print("The correct answer is c) Adaka Boro")

# Display the score
print("You score:", score)
