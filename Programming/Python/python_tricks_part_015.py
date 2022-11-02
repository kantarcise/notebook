# Sets and Multisets

# In this chapter you’ll see how to implement mutable and immutable
# set and multiset (bag) data structures in Python, using built-in data
# types and classes from the standard library. First though, let’s do a
# quick recap of what a set data structure is:

# A set is an unordered collection of objects that does not allow duplicate
# elements. Typically, sets are used to quickly test a value for 
# membership in the set, to insert or delete new values from a set, and to
# compute the union or intersection of two sets.

# In a “proper” set implementation, membership tests are expected to
# run in fast O(1) time. Union, intersection, difference, and subset 
# operations should take O(n) time on average. The set implementations
# included in Python’s standard library follow these performance characteristics

# Just like dictionaries, sets get special treatment in Python and have
# some syntactic sugar that makes them easy to create. For example,
# the curly-braces set expression syntax and set comprehensions allow
# you to conveniently define new set instances:

vowels = {'a', 'e', 'i', 'o', 'u'}
squares = {x * x for x in range(10)}

# But be careful: To create an empty set you’ll need to call the set()
# constructor. Using empty curly-braces {} is ambiguous and will 
# create an empty dictionary instead.

# Python and its standard library provide several set implementations. Let’s have a look at them.

# ------------------------------------------------------------------

# set – Your Go-To Set

# This is the built-in set implementation in Python.26 The set type
# is mutable and allows for the dynamic insertion and deletion of elements.

# Python’s sets are backed by the dict data type and share the same performance
# characteristics. Any hashable object can be stored in a set.

vowels = {'a', 'e', 'i', 'o', 'u'}
'e' in vowels
# True

letters = set('alice')
letters.intersection(vowels)
# {'a', 'e', 'i'}

vowels.add('x')
vowels
# {'i', 'a', 'u', 'o', 'x', 'e'}

len(vowels)
# 6
