#   <key>: <value>,

nba_teams = {
    "new_orleans": "Pelicans",
    "New York": "knicks",
    "Chicago": "Bulls",
    "Philadelphia": "76ers",
    "Miami": "Heat",
}
print(nba_teams)

# this prints {'new_orleans': 'Pelicans', 'New York': 'knicks', 'Chicago': 'Bulls', 'Philadelphia': '76ers', 'Miami': 'Heat'}

print(nba_teams["Miami"])
# # this will just print the value as to what said key belongs to. Square brackets can be used for de-indexing, and finding key value pairs

# below is how to append items to a dictionary list (dictionaries are unordered so when you add things you are good to go. )

my_dictionary["Utah"] = "Jazz"

print(nba_teams)

# this results with {'new_orleans': 'Pelicans', 'New York': 'knicks', 'Chicago': 'Bulls', 'Philadelphia': '76ers', 'Miami': 'Heat', 'miami': 'basketballing'}


#########################################

user = {}

user['first_name'] = 'Michael'
user['last_name'] = 'Scott'
user['employer'] = 'Dunder Mifflin'
user['age'] = 42
user['email'] = 'michael.scott@dundermifflin.com'

print(user)
# line 32 was added myself, when printing this will result with "{'first_name': 'Michael', 'last_name': 'Scott', 'employer': 'Dunder Mifflin', 'age': 42, 'email': 'michael.scott@dundermifflin.com'}"

# Here is an example of a dictionaries as elements of a List:
users_list = [
    {
        "first_name": "Jim",
        "last_name": "Halpert",
        "age": 29,
    },
    {
        "first_name": "Pam",
        "last_name": "Beesley",
        "age": 28,
    },
    {
        "first_name": "Dwight",
        "last_name": "Schrute",
        "age": 33
    }
]

print(users_list[1])
# result is {'first_name': 'Pam', 'last_name': 'Beesley', 'age': 28}


users_list = [
    {
        "first_name": "Jim",
        "last_name": "Halpert",
        "age": 29
    },
    {
        "first_name": "Pam",
        "last_name": "Beesley",
        "age": 28
    },
    {
        "first_name": "Dwight",
        "last_name": "Schrute",
        "age": 33
    }
]

# print(users_list)


for user in users_list:
    print(f'First Name: {user["first_name"]}\nLast Name: {user["last_name"]}\nAge: {user["age"]}\n')

#########################################

user = {
    "username": "cigano",
    "active": True,
    "meta_data": {
        "external_id": "xdefjsjaf22ks",
        "last_login": "09/10/2021 07:33PM",
        "acct_type": "manager"
    }
}

user['meta_data']['acct_type'] = 'user'
# code above is for the second list of instructions
print('Last login: ' + user['meta_data']['last_login'])
#  could have done this with an f function
print(user)


#   1. given the following dictionary, write a line of code to print the last_login datetime for the user 'cigano':

#   2. Using the dictionary from the previous exercise, write a line of code to change the acct_type from manager to user
