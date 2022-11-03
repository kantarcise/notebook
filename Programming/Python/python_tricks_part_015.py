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

# ------------------------------------------------------------------

# frozenset – Immutable Sets

# The frozenset class implements an immutable version of set that
# cannot be changed after it has been constructed. Frozensets are
# static and only allow query operations on their elements (no inserts
# or deletions.) Because frozensets are static and hashable, they can be
# used as dictionary keys or as elements of another set, something that
# isn’t possible with regular (mutable) set objects.

vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
vowels.add('p')
# AttributeError:
# "'frozenset' object has no attribute 'add'"

# Frozensets are hashable and can be used as dictionary keys:
d = { frozenset({1, 2, 3}): 'hello' }
d[frozenset({1, 2, 3})]
# 'hello'

# ------------------------------------------------------------------

# collections.Counter – Multisets

# The collections.Counter class in the Python standard library implements
# a multiset (or bag) type that allows elements in the set to
# have more than one occurrence.

# This is useful if you need to keep track of not only if an element is part
# of a set, but also how many times it is included in the set:

from collections import Counter
inventory = Counter()

loot = {'sword': 1, 'bread': 3}
inventory.update(loot)
inventory
# Counter({'bread': 3, 'sword': 1})

more_loot = {'sword': 1, 'apple': 1}
inventory.update(more_loot)
inventory
# Counter({'bread': 3, 'sword': 2, 'apple': 1})

# Here’s a caveat for the Counter class: You’ll want to be careful when
# counting the number of elements in a Counter object. Calling len()
# returns the number of unique elements in the multiset, whereas the
# total number of elements can be retrieved using the sum function:

# Unique elements
len(inventory)
# 3

# Total no. of elements
sum(inventory.values())
# 6

# Key Takeaways
# • Sets are another useful and commonly used data structure included with Python and its standard library.
# • Use the built-in set type when looking for a mutable set.
# • frozenset objects are hashable and can be used as dictionary or set keys.
# • collections.Counter implements multiset or “bag” data structures.
