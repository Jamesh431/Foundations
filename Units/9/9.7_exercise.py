mascots = {
    'BYU': 'Cougars',
    'Utah': 'Utes',
    'Oregon': 'Ducks',
    'UCLA': 'Bruins',
    'UNLV': 'Rebels'
}

if 'BYU' in mascots:
    print(mascots['BYU'])

if 'Weber State' not in mascots:
    print('Weber State mascot is not in the dictionary')

# output:
# Cougars
# Weber State mascot is not in the dictionary

# The get() function provides a safer method of getting a value from a key in a dictionary. It works like bracket notation dict[<key>], but will NOT raise an error if the key does NOT exist.

print(len(mascots))
# this returns an output of '5'

# The syntax of the .get function is:

# dict.get(<key>[, <default>])
#########################################
# The items() function will return a dict_items object, which encapsulates a list of tuples containing the key-value pairs in the dictionary. The first item of each tuple is the key and the second item in the tuple is the key's value. We can easily convert the dict_items to a list by casting it as in the example below:
mascots = {
    'BYU': 'Cougars',
    'Utah': 'Utes',
    'Oregon': 'Ducks',
    'UCLA': 'Bruins',
    'UNLV': 'Rebels'
}
print(mascots.items())

# output is dict_items([('BYU', 'Cougars'), ('Utah', 'Utes'), ('Oregon', 'Ducks'), ('UCLA', 'Bruins'), ('UNLV', 'Rebels')])

mascots_as_list = list(mascots.items())

print(mascots_as_list)
# output is [('BYU', 'Cougars'), ('Utah', 'Utes'), ('Oregon', 'Ducks'), ('UCLA', 'Bruins'), ('UNLV', 'Rebels')]
# this is because it was converted to a list of tuples

new_dictionary = dict(mascots_as_list)

print(new_dictionary)
# output is {'BYU': 'Cougars', 'Utah': 'Utes', 'Oregon': 'Ducks', 'UCLA': 'Bruins', 'UNLV': 'Rebels'}
# this is because it was converted to a dictionary after being converted to a tuple
#########################################
# The keys() function returns a dict_keys object that wraps a list of the keys in the dictionary. We can easily cast the dict_keys to a list as in the example below

mascots = {
    'BYU': 'Cougars',
    'Utah': 'Utes',
    'Oregon': 'Ducks',
    'UCLA': 'Bruins',
    'UNLV': 'Rebels'
}

print(mascots.keys())
# output is dict_keys(['BYU', 'Utah', 'Oregon', 'UCLA', 'UNLV'])
mascot_keys_list = list(mascots.keys())
print(mascot_keys_list)
# output is ['BYU', 'Utah', 'Oregon', 'UCLA', 'UNLV']

# The values() function returns a dict_values obejct that wraps a list of the values in the dictionary. We can easily cast the dict_values to a list as below:

mascot_values_list = list(mascots.values())
print(mascot_values_list)
# output is ['Cougars', 'Utes', 'Ducks', 'Bruins', 'Rebels']

# The pop function removes a key, if it exists, and returns its value. The syntax of the pop() function is: dict.pop(<key>[, <default>])

print(mascots.pop('USC', 'Not Found'))
# output is Not Found

# The function popitem() removes the last added key-value pair and returns it as a tuple.

print(mascots.popitem())
('UNLV', 'Rebels')
print(mascots)
# output is {'BYU': 'Cougars', 'Utah': 'Utes', 'Oregon': 'Ducks', 'UCLA': 'Bruins'}
