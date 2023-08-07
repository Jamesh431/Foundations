# import random

# while True:
#   # number = input("Input a number between 1 and 100: ")
#   number = random.randint(1,101)
#   i = True
#   counter = 0
#   while i:
#     # print(number)
#     number_guess=int(input("Guess a number between 1 and 100: "))

#     if number_guess == number:
#       counter += 1
#       if counter == 1:
#         print("Wow!!! It only took you 1 try to guess my number!")
#       if counter > 1:
#           print("That's correct! It only took you " + str(counter) + " tries to guess my number!")
#       break

#     elif number_guess < number:
#       counter += 1
#       print("Too low")
#       continue

#     elif number_guess > number:
#       counter += 1
#       print("Too high")
#       continue


# # in order to get it to repeat after the number is guessed correctly it all has to be nested under the line 1 "while True:" loop. Then after the correct guess response it has to break, after the wrong ones it has to have continue


import random

# griffendor = 0
# hufflepuff = 0
# slytherin = 0
# ravenclaw = 0


def house_questions():
    griffendor = 0
    hufflepuff = 0
    slytherin = 0
    ravenclaw = 0

    q1 = input(
        "Does pineapple belong on pizza? \na. Yes \nb.no \nc. Sometimes \nd. I don't care \ne. no, you are horrible for asking \n>"
    )
    if q1 == "e":
        hufflepuff += 99999999999999
    elif q1 == "a":
        hufflepuff += 1
    elif q1 == "b":
        slytherin += 1
    elif q1 == "c":
        ravenclaw += 1
    elif q1 == "d":
        griffendor += 1

    q2 = input(
        "Do you think John is the coolest? \na. Sure \nb.Yes, but not today. \nc. He certainly thinks so. \nd. Absolutely! \n>"
    )
    q3 = input(
        "What's the best meal of these foods \na. Pizza \nb. Burgers \nc. tacos \nd. grilled cheese \n>"
    )
    q4 = input(
        "Do you like speeding? \nA.Yes \nB.No \nC.Speeding is dangrous \nD.I love poking death"
    )
    q5 = input(
        "Are you scared of dementors? \nA.Yes \nB.No \nC.Absolutely \nD.I welcome them"
    )

    if q1 == "e":
        hufflepuff += 99999999999999
    elif q1 == "a":
        hufflepuff += 1
    elif q1 == "b":
        slytherin += 1
    elif q1 == "c":
        ravenclaw += 1
    elif q1 == "d":
        griffendor += 1
    else:
        q1 = input(
            "invaild option \nDoes pineapple belong on pizza? \na. Yes \nb.no \nc. Sometimes \nd. I don't care \ne. no, you are horrible for asking \>n"
        )

    if q2 == "a":
        hufflepuff += 1
    elif q2 == "b":
        slytherin += 1
    elif q2 == "c":
        ravenclaw += 1
    elif q2 == "d":
        griffendor += 1
    else:
        q2 = input(
            "invaild option \n Do you think John is the coolest? \na. Sure \nb.Yes, but not today. \nc. He certainly thinks so. \nd. Absolutely! \n>"
        )

    if q3 == "a":
        hufflepuff += 1
    elif q3 == "b":
        slytherin += 1
    elif q3 == "c":
        ravenclaw += 1
    elif q3 == "d":
        griffendor += 1
    else:
        q3 = input(
            "invaild option: \n What's the best meal of these foods \na. Pizza \nb. Burgers \nc. tacos \nd. grilled cheese \n>"
        )

    if q4 == "a":
        ravenclaw += 5
    elif q4 == "b":
        hufflepuff += 15
    elif q4 == "c":
        griffendor += 5
    elif q4 == "d":
        slytherin += 15
    else:
        q4 = input(
            "Ivalid Option!\n Do you like speeding? \nA.Yes \nB.No \nC.Speeding is dangrous \nD.I love poking death"
        )

    if q5 == "a":
        ravenclaw += 5
    elif q5 == "b":
        griffendor += 15
    elif q5 == "c":
        hufflepuff += 5
    elif q5 == "d":
        slytherin += 15
    else:
        q5 = input(
            "Invalid Option!\n Are you scared of dementors? \nA.Yes \nB.No \nC.Absolutely \nD.I welcome them"
        )

    if (
        griffendor > hufflepuff
        and griffendor > slytherin
        and griffendor > ravenclaw
    ):
        house = "Your house is Griffendor"
        return house
    elif (
        hufflepuff > griffendor
        and hufflepuff > slytherin
        and hufflepuff > ravenclaw
    ):
        house = "Your house is Hufflepuff"
        return house
    elif (
        slytherin > hufflepuff and slytherin > griffendor and slytherin > ravenclaw
    ):
        house = "Your house is Slytherin"
        return house
    elif (
        ravenclaw > hufflepuff and ravenclaw > griffendor and ravenclaw > slytherin
    ):
        house = "Your house is Ravenclaw"
        return house


print(house_questions())


# def ran_house():
#     house = ["Griffendor", "Hufflepuff", "Slytherin", "Ravenclaw"]
#     return random.choice(house)


# print(ran_house())
