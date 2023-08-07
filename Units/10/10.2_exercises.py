def numbers(num1, num2, num3, num4):
    x = max(num1, num2, num3, num4)
  # still confused as to why I couldn't make it work with max by having just variable numbers in there, why did I have to list out the num1, num2, num3, num4
    print(x)


numbers(5, 8, 2, 3)

###### SOLUTION #######


def numbers(num1):
    print(numbers)
    x = max(num1)

    # x=max(num1, num2, num3, num4)
    print(x)


numbers((5, 8, 2, 3))

# turned it to a touple named just num1. The touple was set in the last line by encasing the numbers in two parenthasees


def add_one(num):
    num += 1
    return num


num = 7

print(add_one(num))
print(num)

#############

uinput = input('Type something: ')


def userinput(uinput):
    count = 0
    vowels = "aeiou"
    for i in uinput:
        if i in vowels:
            count += 1
    return count


print(userinput(uinput))
# 1. Challenge: Write a function that will take input from the user and will count the number of vowels in the input string. Return that value


uinput2 = input('Type something: ')


def userinput2(uinput2):
    count_o = 0
    count_x = 0
    for i in uinput2:
        if i in "o" or i in "O":
            count_o += 1
    for i in uinput2:
        if i in "x" or i in "X":
            count_x += 1
    if count_x < count_o:
        print("There are more o\'s than x\'s")
    elif count_x > count_o:
        print("There are more x\'s than o\'s")
    elif count_x == 0 and count_o == 0:
        print("There are no x's or o's")
    else:
        print("The same")


userinput2(uinput2)

# 2. Challenge 2: Write a function that will take input from the user consisting of 'X' and 'O' characters such as, "XOOXOXOOXOXXXXOXOXOX". The program will Return the number of each letter, and print 'More X's' if there are more X's than O's, or 'More O's' if there are more O's than X's, or, 'The same' if the number of 'X's and 'O's is the same.

###############


def favorite_book(title):
    print(f'One of my favorite books is {title}')


favorite_book('Green eggs and ham')

# Create a function called favorite_book()
# It will accept 1 parameter, which we'll call title.
# have your function print out a message that says something along the lines of "One of my favorite books is <whatever the title of the book is>"


def describe_pet(breed, name):
    print(f'I have a {breed} and their name is {name}')


breed = input('Input breed: ')
name = input('Name: ')
describe_pet(breed, name)
# Create a function called describe_pet() that takes two parameters. One for the breed of the animal and one for their name.
# Your function should print out "I have a <breed>. Their name is <name>"
# Try swapping the order you put your parameters in. What happens? Why?
