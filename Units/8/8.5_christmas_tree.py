height = int(input("Enter tree height: "))
bottom_width = height*2
format = (bottom_width * height)
i = 1

while i <= int(height):
    print(f'{"* " * (2 * i - 1):^{format}}')
    i += 1

for i in range(2):
    print(f'{"***":^{format}}')


# how john did it

tree_height = int(input("How tall would you like your tree? "))
tree_character = "*"

for i in range(tree_height):
    print(f'{tree_character:^{tree_height * 2}}')
    tree_character = + " *"

for i in range(2):
    print(f'{"***":^{tree_height * 2}}')


##################


# height = int(input("Enter Tree Height: "))
# width = height*2 - 1

# i = 1

# while i <= height:
#   print("*"*(2*i-1))
#   i+=1


# height = int(input("Enter tree height: "))
# bottom_width = height*2
# format = (bottom_width * height)
# i = 1

# while i <= int(height):
#   print(f'{"* " * (2 * i - 1):^{format}}')
#   i+=1


# height = int(input("Enter tree height: "))
# bottom_width = height*2-1
# format= bottom_width - 1/2
# i = 1

# while i <= height:
#   print(f'{"*" * (2 * i - 1):^{format}}')
#   i+=1


# tree_height = input("Enter Tree Height: ")


# height = int(input("Enter tree height: "))
# bottom_width = height * 2 - 1
# spaces = int((bottom_width-1)/2)
# i=1

# while i <= height:
#     print(" "*(spaces - + 1), "*"*(2 * i-1))
#     i+=1


# height = input("Enter tree height: ")
# bottom_width = height*2
# i = 1

# while i <= int(height):
#   print(f'{"* " * (2 * i - 1):^20}')
#   i+=1
