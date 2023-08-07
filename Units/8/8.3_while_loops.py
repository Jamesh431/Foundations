import random

ans = True

while ans:
    question = input('What is your favorite movie?: (press enter to quit): ')

    answers = random.randint(1, 4)

    if not question:
        quit("Goodbye!")

    elif answers == 1:
        print(question + "? Oooh! Good choice! I liked that one!")

    elif answers == 2:
        print(question + "? That one was alright")

    elif answers == 3:
        print(question + "? I haven't seen that one yet.")

    elif answers == 4:
        print(question + "? Really? That one sucks!")

# ended up having to combine what I learned before unit 5.1 I belive. Had to combine a defined variable with some string text

# Can also do it differently as follows

user_response = ''
while user_response.lower() != "quit":
    user_response = input("What is your favorite food? (or type quit to exit): ")
    print(f'I too enjoy {user_response}.')

# Or you can do

user_response = ''
while True:
    user_response = input("What is your favorite food? (or type quit to exit): ")

    if user_response.lower() == 'quit':
        print("Goodye!")
        break
    else:
        print(f'I too enjoy {user_response}.')

# ended up having to combine what I learned before unit 5.1 I belive. Had to combine a defined variable with some string text

# ---------

# 2. Write a simple program that will:

# a. Ask the user a questions and assign the response to a variable

# b. If the response is NOT quit, then feel free to respond as you ssee fit AND ask the question again.

# c. The the response IS quit, then end the program

# for example

# What is your favorite color ('quit' to end)? Blue
# Oh, blue is nice!

# What is your favorite color('quit' to end)? Purple
# Now that is an excellent choice!

# What is your favorite color('quit' to end)? quit
# Goodbye
