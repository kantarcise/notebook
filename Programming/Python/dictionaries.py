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

# Use the Keys
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

