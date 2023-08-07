new_number = 150

if new_number > 100:
    print(new_number, "too big")
  # line 4 is indented as it is our action section. And all indentations have to line up! (not all langueges care about endenadations, some will care about brackets {})
if new_number < 100:
    print('pick another number: ')
else:
    print('pick another number: ')
# ----------------
password = input("please type in your password:")

# password = 'abc123'
# have to comment out line 3 so it would work

if password == "abc123":
    print("Welcome")

else:
    print("Access Denied")
# ----------------
role = "admin"

if role == "standard":
    print("User Dasboard")

elif role == "admin":
    print("Admin Panel")
  # multiple if statements will cause multiple if statements to all pop off at once. You can have multiple elifs as you want, but you can only have one if and one else in a chain
    print('Welcome')
  # needs to be at the same indentation level and under the right condition for it to work

else:
    print("Not Authorized")
# -------------
user_name = "John"
email = "john_wick@gmail.com"
password = "I'mBack"

if (user_name == "John" or email == "john_wick@gmail.com") and password == "I'mBack":
    print("Welcome duder!")
else:
    print("No business on Continental grounds!")
# ---------------
# == is equal to
# != not equal to
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to

score = input('Enter Score Here: ')

if int(score) >= 90:
    print('Grade: A')

elif int(score) >= 80:
    print('Grade: B')

elif int(score) >= 70:
    print('Grade: C')

elif int(score) >= 60:
    print('Grade: D')

else:
    print('Grade: F')

# Remember that when you capture input from a user, that input will always be stored as a string. You need to cast that value to an Integer if you would like to perform math on it
# Could have also put the int cast on line 2 "grade = int(grade)"
#  On line 1 also could have done "score = input(int('Enter score here)): '"
