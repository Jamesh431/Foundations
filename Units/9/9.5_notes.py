my_list = [1, 4, 7, 9, 2, 5, 3]
my_list.sort()

print(my_list)
# Output when this is ran is "[1, 2, 3, 4, 5, 7, 9]" as it was sorted numerically


def sort_by_odd_even(num):
    return num % 2 == 0


my_list = [1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 1, 18, 9]
print(my_list)

my_list.sort(key=sort_by_odd_even, reverse=True)
print(my_list)

# output is "[2, 4, 6, 18, 1, 3, 5, 7, 1, 1, 1, 1, 9]" as its another way to sort by odd and even

# sorted will perm change your list will sort will not


my_list = ['Doug', 'carrie', 'a', 'Z', 'garfield', 'A']

print(sorted(my_list))

# this results in "['A', 'Doug', 'Z', 'a', 'carrie', 'garfield']" because python does not recognize capiol letters as the same as lower case letters so it then does the capital letters first. If numbers are added in as the form of strings it will place them first, before the capital letters

print(sorted(my_list["Doug"]))
# this will just print the value as to what said key belongs to. Square brackets can be used for de-indexing, and finding key value pairs

my_list = ["1", "2", "3", "4", 'Doug', 'carrie', 'a', 'Z', 'garfield', 'A', "1", "2", "3", "4"]

print(sorted(my_list))

# If numbers are added in as the form of strings, it will result with "['1', '1', '2', '2', '3', '3', '4', '4', 'A', 'Doug', 'Z', 'a', 'carrie', 'garfield']" the numbers were placed first, before the capital letters. This is because on the ascii chart, numbers come first, then capital letters, then the lowercase numbers
