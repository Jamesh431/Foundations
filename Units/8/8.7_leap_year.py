while True:
    year = int(input("Input any year after 1752: "))

    if (year < 1753):
        print("Invalid year, please input year after 1752.")
    elif (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("True")
    else:
        print("False")


# how john said he would do it

while True:
    year = input("Input any year after 1752: ")

    if year.isnumeric():
        year = int(year)
        if year < 1752:
            print("That's not a valid year. Please try again.")
            continue
    else:
        print("Please input your year with only numbers.")
        continue
        # all of this above was shown by john as what we may need to do in the future as we will be working for people who won't be doing just numbers, theyll end up doing something odd

    leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 4 + + 0 and year % 100 == 0 and year % 400 == 0)
    print(leap_year)
