list = ["A", "B", "C", "D", "G", "E", "F", "G", "H", "I"]

############

list_1 = []
numbers_to_append = 1

for i in range(1, 101):
    list_1.append(i)
print(list_1)

############

my_list = ["a", "b", "c", "d", "b", "a", "e"]
vowels = ['a', 'e', 'i', 'o', 'u']
# vowels = str(vowels)
# vowels = vowels.lower()
# line above is code that that can be used to check a string, and convert the needed parts of said string to lowercase, to change them to uppercase you would do string_name = string_name.upper instead
# (THAT CODE CHECKS STRINGS NOT LISTS SO YOU HAVE TO CONVERT THE LIST TO A STR AS SEEN ON LINE 16)

for i in my_list:
    if i in vowels:
        print(i)

##############

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = []
even_list = []
for num in a_list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        new_list.append(num)

for num in even_list:
    new_list.append(num)

print(new_list)

###############

forward_list = [1, 2, 3, 4, 5, 6, 7, 8]
reverse_list = []
for num in forward_list:
    reverse_list.insert(0, num)
print(reverse_list)


#     1. Create a Python List with at least 10 elements.

#     2. Create an empty List, then using a for loop, append the numbers 1-100 to the list

#     3. Given the list: my_list = ["a", "b", "c", "d", "b", "a", "e"] write code to loop through the list and print only the vowels

#     4. Separate odds and evens. Write code that will take a list of positive integers and will create a new list with all of the odds at the beginning of the list and all of the evens at the end of the list. For example:
# a_list = [1,5,8,2,4,8,1,3,5,9]

# # ... your code goes here

# new_list = [1,5,1,3,5,9,8,2,4,8]

# print(new_list)

#     5. Manually reverse the elements in a list, without using "slicing". See the following example:
# my_list = [1,2,3,4,5,6,7,8]

# # After your code

# my_list = [8,7,6,5,4,3,2,1]
