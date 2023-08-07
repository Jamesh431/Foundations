height = int(input("How tall would you like your tree? "))


def tree_height(height):
    tree_character = "*"
    for i in range(height):
        print(f'{tree_character:^{height * 2}}')
        tree_character += " *"


tree_height(height)

for i in range(2):
    print(f'{"***":^{height * 2}}')

# Challenge given by john to those who finished dynamic calendar as some still needed to work on it. Challenge was to take the christmas tree we made and then put it into a function
