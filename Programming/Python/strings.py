# This script is all abouut strings & character operations.

string = "gratitude"
another_string = "empathy"
and_another_string = "happiness"

best_things_in life = string + " " + another_string + " " + and_another_string 

# gratitude empathy happiness

multiplication = "Can you do this?"

result = multiplication * 4

# Can you do this?Can you do this?Can you do this?Can you do this?

in_string = 'food'

in_string in 'That\'s food for thought.'
# True

in_string in 'That\'s good for now.'
# False


# Built-in String Functions

# Function 	           #Description
# chr() 	             Converts an integer to a character
# ord() 	             Converts a character to an integer
# len() 	             Returns the length of a string
# str() 	             Returns a string representation of an object


# String Indexing

string = "repetition is the key."

string[0]

# r

string[4]

# t

# String Slicing
# This also works in lists, so get it right.

another_string = "dreams do come true"

another_string[1:4]
# ream

another_string[0:7]
another_string[:7]
# dreams d
# Same result

# Built-in String Methods
# Case Conversion


s = 'foO BaR BAZ quX'
#  First character converted to uppercase and all other characters converted to lowercase.
s.capitalize()
#  'Foo bar baz qux'

s.upper()
# "FOO BAR BAZ QUX"

'foo goo moo'.count('oo')
# 3

# .join() - Concatantes Strings (Or add pieces between them)

':'.join('corge')
# 'c:o:r:g:e'

# .partition() -  Divides a string based on a separator.

'foo.bar'.partition('.')
#('foo', '.', 'bar')


# An f-string looks like an ordinary string, but it is
# prefixed with f or F. Interpolated variables in an f-string are enclosed in curly braces.

name = "Eric"
age = 74

f"Hello, {name}. You are {age}."

# 'Hello, Eric. You are 74.'


#   The f in f-strings may as well stand for “fast.”
# f-strings are faster than both %-formatting and str.format(). 
# As you already saw, f-strings are expressions evaluated at runtime rather than constant values.

# With Dictionaries
comedian = {'name': 'Eric Idle', 'age': 74}

f"The comedian is {comedian['name']}, aged {comedian['age']}."
# The comedian is Eric Idle, aged 74.


