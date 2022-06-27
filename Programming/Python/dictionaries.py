# This file is about Dictionaries in Python.

a_dictionary = {a:"2", b:"3"}

# Dictionaries and lists share the following characteristics:

#    Both are mutable.
#    Both are dynamic. They can grow and shrink as needed.
#    Both can be nested. A list can contain another list. A dictionary can contain another dictionary. A dictionary can also contain a list, and vice versa.

# Dictionaries differ from lists primarily in how elements are accessed:

#    List elements are accessed by their position in the list, via indexing.
#    Dictionary elements are accessed via keys.


MLB_team = {
     'Colorado' : 'Rockies',
     'Boston'   : 'Red Sox',
     'Minnesota': 'Twins',
     'Milwaukee': 'Brewers',
     'Seattle'  : 'Mariners'
}

# Dictionary elements are not accessed by numerical index.

MLB_team[1]
# Traceback (most recent call last):
#  File "<pyshell#13>", line 1, in <module>
#    MLB_team[1]

>>> 'Toronto' not in MLB_team# Use the Keys
MLB_team["Colorado"]
# "Rockies"

# Adding new value with a key
>>> MLB_team['Kansas City'] = 'Royals'
>>> MLB_team
{'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
'Milwaukee': 'Brewers', 'Seattle': 'Mariners', 'Kansas City': 'Royals'}

# You can delete elements with del 
del MLB_team['Seattle']
MLB_team
# {'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins',
# 'Milwaukee': 'Brewers', 'Kansas City': 'Royals'}

# You cannot use index number to access the elements of the dictionary.
# Dictionary Keys vs. List Indices

# Cannot do:
# MLB_team[1]

# You can do all sort of things
person = {}
type(person)
# <class 'dict'>

person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}


person
# {'fname': 'Joe', 'lname': 'Fonebone', 'age': 51, 'spouse': 'Edna',
# 'children': ['Ralph', 'Betty', 'Joey'], 'pets': {'dog': 'Fido', 'cat': 'Sox'}}


# Restrictions on Dictionary Values
# By contrast, there are no restrictions on dictionary values. Literally none at all. 
# A dictionary value can be any type of object Python supports, including mutable types like
# lists and dictionaries, and user-defined objects, which you will learn about in upcoming tutorials.

# There is also no restriction against a particular value appearing in a dictionary multiple times:

d = {0: 'a', 1: 'a', 2: 'a', 3: 'a'}
d
# {0: 'a', 1: 'a', 2: 'a', 3: 'a'}
d[0] == d[1] == d[2]
# True

# in and not works

"Milwaukee" in MLB_team
# True
'Toronto' in MLB_team
# False
'Toronto' in not MLB_team
# True

# Also len works
MLB_team = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}

len(MLB_team)
# 5

d = {first: "1" , second: "2"}
# Clears a dictionary
d.clear()
d
# {}
 
# d.get()
# The Python dictionary .get() method provides a convenient way of getting the value of a 
# key from a dictionary without checking ahead of time whether the key exists, and without raising an error.

d = {'a': 10, 'b': 20, 'c': 30}

print(d.get('b'))
# 20
print(d.get('z'))
# None

# d.keys()
# Returns a list of keys in a dictionary.
d = {'a': 10, 'b': 20, 'c': 30}
d
# {'a': 10, 'b': 20, 'c': 30}
list(d.keys())
# ['a', 'b', 'c']


# d.values()
# Returns a list of values in a dictionary.
d = {'a': 10, 'b': 20, 'c': 30}
d
# {'a': 10, 'b': 20, 'c': 30}
list(d.values())
# [10, 20, 30]


# d.pop(<key>[, <default>])
# Removes a key from a dictionary, if it is present, and returns its value.
d = {'a': 10, 'b': 20, 'c': 30}
d.pop('b')
# 20
d
# {'a': 10, 'c': 30}


# d.popitem()
# Removes a key-value pair from a dictionary.
d = {'a': 10, 'b': 20, 'c': 30}
d.popitem()
# ('c', 30)
d
# {'a': 10, 'b': 20}


# d.update(<obj>)
# Merges a dictionary with another dictionary or with an iterable of key-value pairs.

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

d1.update(d2)
d1
# {'a': 10, 'b': 200, 'c': 30, 'd': 400}
