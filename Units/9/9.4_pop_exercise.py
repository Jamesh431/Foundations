#   1. Try to determine what happens when a List has multiple elements with the same value and you call remove(). For example:
my_list = [1, 2, 3, 4, 1, 1]
my_list.remove(1)

print(my_list)
# # What is printed?
# # It takes the value not the index number and targets the first one in the string it finds. If you do .remove(1+1) it will target the first 2 it sees because 1+1=2. If you do 1-1 it will give an error because there is no number in the list with the value of 0, but if you were to do pop(0) it would take out the first number due to .pop targeting the index not the value

my_list = [1, 2, 3, 4, 1, 1]
for num in my_list:
    if 1 in my_list:
        my_list.remove(1)

print(my_list)

# The example above shows how you can use it to remove multiple values that are the same by using a for loop
