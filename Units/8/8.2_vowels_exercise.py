# 1. Use a range to loop 10 times. (fill in the blank)

# for x in range(2,12):
#   print(x)


# CAN ALSO DO IT WITH VARIABLES

# phrase = "James is my name"
# for i in range(1,11):
#     print(phrase)

# ---

# 2. Print the even numbers from 2 to 100, with each number on its own line.
# for x in range(2,101,2):
#   print(x)

# ---

# 3. Iterate over a string and print only the consonants. Remember that consonants are any letter of the alphabet that are not vowels (a, e, i, o , u). Keep in mind that spaces and punctuation, are not consonants. Here is an example run of the program:

# phrase = "James is my name"

# vowels = "AEIOU"

# for letter in phrase:
#   if letter.lower()!= 'a' and letter.lower() != 'e' and letter.lower()!= 'i' and letter.lower()!= 'o' and letter.lower()!= 'u':
#     print()

#   else:
#     print(letter)

# could also do "letter.lower()!= 'a' and " or can do "letter.lower()== 'a' or"

# ---

# 4. Using a for loop, write the code to calculate x^y. For example, x^3 = x * x * x. Use your loop to calculate 2^7

# x = 2
# y = 7

# result = x
# for num in range(y-1):
#   result = result * x

# print(result)

# ## to change it to be based on input, you can do this on line 40 and 41
# x = int(input("Enter Base Number: "))
# y = int(input("Enter exponent value: "))
