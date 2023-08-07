college_teams = {
    "UTAH".title(): "UTES".title(),
    "BYU".title(): "COUGARS".title(),
    "UTAH STATE".title(): "AGGIES".title(),
}
team_to_add = {}

while True:
    for key, value in college_teams.items():
        print(key.title(), value.title())
    # print(f'Current College teams: {college_teams.items()}')
    question = input('\nWould you like to: \n(A)dd new team \n(R)emove a team \n(Q)uit \n> ')
    if question == "a" or question == 'A':
        answer_a1 = input('What is the teams name?: ')
        answer_a1 = answer_a1.upper()
        answer_a2 = input('What is the teams mascot?: ')
        answer_a2 = answer_a2.upper()
        print(f'{answer_a1.title()} {answer_a2.title()} are being added')
        team_to_add[answer_a1] = answer_a2
        # print(team_to_add)
        college_teams.update(team_to_add)

    elif question == 'r' or question == 'R':
        answer_r1 = input('Which team name would you like to remove?: ')
        answer_r1 = answer_r1.upper()
        print(answer_r1 + '\n')
        if answer_r1 in college_teams:
            college_teams.pop(answer_r1)
            print('Team has been removed!\n')
            continue
        else:
            print('Team not found. Please check your spelling!\n')
            continue

    elif question == 'q' or question == 'Q':
        quit('Goodbye')


# RESTARTED as I wanted to instead have it add new team info to a new dictionary THEN merge the two dictionaries


# college_teams = {
#   "Utah" : "Utes",
#   "BYU" : "Cougars",
#   "Utah State" : "Aggies",
# }
# while True:
#   list_teams = list(college_teams)
#   print(f'Current College teams: {college_teams}')
#   question = input('\nWould you like to: \n(A)dd new team \n(R)emove a team \n(Q)uit \n> ')
#   answer_a1 = input('What is the teams name?: ')
#   answer_a2 = input('What is the teams mascot?: ')

#   if question == 'a' or 'A':
#     print(answer_a1)
#     print(answer_a2)
#     print(f'{answer_a1} {answer_a2} are being added')
#     list_teams[answer_a1] = [answer_a2]


# For this assignment, you will be writing a program to gather locations and names of sports teams and store them in a dictionary. You can pick any league or sport that you want.
# You can prepopulate your list with up to three initial key-value pairs.

# The program should:

# Print the Key-Value pairs, separated by a space
# Ask the user what to do next:
# a. (A)dd a new team
# b. (R)emove a team
# c. (Q)uit
# If the user enters Q, the program ends
# If the user enters R, the program should prompt the user for the 'key' of the team to remove. After removing the team, the program should return to #1 above
# If the user enters A, the program should prompt the user for the location of the team, then the mascot of the team. After receiving those inputs, the program should add the team to the dictionary and return to #1 above

# Hints
# You may consider using a while loop to surround the entire program that breaks when you enter a Q
# Keep in mind that the underlying data structure should be a dictionary, with key-value pairs, so adding and removing them should be straightforward.
# You may want to add some checking around the remove part of the code just in case the user enters a team that isn't in the dictionary
# Bonus Points
# Bonus points for allowing the user to enter a team without worrying about case-sensitivity when removing a team. For example, when removing a team, the user should be able to enter 'texas' and it would still remove 'Texas'.
