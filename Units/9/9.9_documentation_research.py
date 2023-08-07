# extend()
# -------------------

# The extend() method extends the list by appending all the items from the iterable

# -------------------

# Syntex of extend() is list.extend([iterable])
# the iterable is required. It is any iterable type that you want to add to the list

# extend() returns none
# -------------------

# example of extend()
shopping_list = ['milk', 'eggs', 'bread']
shopping_list.extend(['flour'])


print(shopping_list)

output: ['milk', 'eggs', 'bread', 'flour']


# instead if you do shopping_list.extend('flour'), same as before but without the brackets, the output will be different. "['milk', 'eggs', 'bread', 'f', 'l', 'o', 'u', 'r']"

# -----------------------------------------------------------


copy()

# -------------------

# The copy() method returns a copy of a select list. Copies only the list, not the elements in the list as it is a shallow copy

# -------------------

# Syntex this function is just copy()
# The .copy() method has no parameters.

# Returns a new list, does not modify the original list
# -------------------

shopping_list = ['milk', 'eggs', 'bread']
copied_shopping_list = shopping_list.copy()


print(copied_shopping_list)
output: ['milk', 'eggs', 'bread']

# -----------------------------------------------------------


# index()

# -------------------

# The index() method returns the position of a specified list item

# -------------------

# Syntax of index() is index(item, start, end)

# item is required. It is the element whose lowest index will be returned
# start (optional)- the index position from where the search starts
# end (optional)- the indext position from where the search ends

# -------------------

# index() example:
# this example shows how to find the index of an element with the start and end parameters

list = [1, 2, 3, 4, 8, 1, 2, 3, 4, 5]

# Will print index of '4' in sublist
# having index from 5 to 9.
print(list.index(4, 5, 9))

output: 8
# this is because the 4 between index 5 and 9 is at the index position at 8

# -----------------------------------------------------------
