# 0,1, 2, 3, 4, 5
# 0 based index
my_array = [5, 23, 12, 55, -1, 0]
# arrays are like ranges in the fact that you start counting from zero

### 9.3 ###
# example from 9.3
my_list = []

my_family = ["Mom", "Nick", "Corbie", "Buster"]

my_family.append("Another name")

my_family.insert(0, "Insert Name")
# insert needs a number as it needs to know where it needs to be placed

my_family[0] = "Name overwritten"
# this overrites the list spot that is specified


# print(my_family)

print(my_family[2])  # this will print out "Corbie" as lists start from 0 when counting

print(my_family[-2])  # this would also print out "Corbie" because when you use a negetive number it goes to the back of the list and counts towards the front of the list. When using negative numbers it does not start from 0 as there is no -0

print(my_family[-1], my_family[1], my_family[0])

# looping through a list
for i in my_family:
    print(i)


# Getting the Index AND the Value
for index, i in enumerate(my_family):
    print(f'[{index}]: {i}')
    # this is super useful, it numbers everything in the list when printing it out
