# Common Data Structures in Python

# What’s something that every Python developer should practice and learn more about?
# Data Structures

# You see, the trouble is that Python ships with an extensive set of data
# structures in its standard library. However, sometimes the naming for them is a bit “off”.

# The goal here is to clarify how the most common abstract data types
# map to Python’s naming scheme and to provide a brief description
# for each. This information will also help you shine in Python coding interviews.

# Dictionaries, Maps, and Hashtables

# In Python, dictionaries (or “dicts” for short) are a central data structure.
# Dicts store an arbitrary number of objects, each identified by a unique dictionary key.

squares = {x: x * x for x in range(6)}

squares
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Python’s dictionaries are indexed by keys that can be of any hashable
# type: A hashable object has a hash value which never changes during
# its lifetime (see __hash__), and it can be compared to other objects
# (see __eq__). In addition, hashable objects which compare as equal must have the same hash value.

# For most use cases, Python’s built-in dictionary implementation will
# do everything you need. Dictionaries are highly optimized and underlie many parts of the language, for 
# example class attributes and variables in a stack frame are both stored internally in dictionaries.

# IMPORTANT

# Python dictionaries are based on a well-tested and finely tuned hash
# table implementation that provides the performance characteristics
# you’d expect: O(1) time complexity for lookup, insert, update, and delete operations in the average case.

# Besides “plain” dict objects, Python’s standard library also includes a
# number of specialized dictionary implementations. These specialized
# dictionaries are all based on the built-in dictionary class (and share
# its performance characteristics), but add some convenience features on top of that.

# Let’s take a look at them.

# ------------------------------------------

# collections.OrderedDict – Remember the Insertion Order of Keys,

# If the key order is important for the algorithm, it's best to use OrderedDict:

import collections
d = collections.OrderedDict(one=1, two=2, three=3)

d
# OrderedDict([('one', 1), ('two', 2), ('three', 3)])
d['four'] = 4
d
# OrderedDict([('one', 1), ('two', 2),
#              ('three', 3), ('four', 4)])

d.keys()
# odict_keys(['one', 'two', 'three', 'four'])

# ------------------------------------------

# collections.defaultdict – Return Default Values for Missing Keys

# The defaultdict class is another dictionary subclass that accepts
# a callable in its constructor whose return value will be used if a requested key cannot be found.

from collections import defaultdict
dd = defaultdict(list)

# Accessing a missing key creates it and
# initializes it using the default factory,
# i.e. list() in this example:
dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')
dd['dogs']
# ['Rufus', 'Kathrin', 'Mr Sniffles']

# ------------------------------------------

# collections.ChainMap – Search Multiple Dictionaries as a Single Mapping

# The collections.ChainMap data structure groups multiple dictionaries into a
# single mapping. Lookups search the underlying mappings one by one until a
# key is found. Insertions, updates, and deletions only affect the first mapping added to the chain.

from collections import ChainMap
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}
chain = ChainMap(dict1, dict2)
chain
# ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})

# ChainMap searches each collection in the chain
# from left to right until it finds the key (or fails):
chain['three']
# 3
chain['one']
# 1
chain['missing']
# KeyError: 'missing'

# ------------------------------------------

# types.MappingProxyType – A Wrapper for Making Read-Only Dictionaries

# MappingProxyType is a wrapper around a standard dictionary that
# provides a read-only view into the wrapped dictionary’s data. This
# class was added in Python 3.3, and it can be used to create immutable proxy versions of dictionaries.

from types import MappingProxyType
writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

# The proxy is read-only:
read_only['one']
# 1
read_only['one'] = 23
# TypeError:
# "'mappingproxy' object does not support item assignment"

# Updates to the original are reflected in the proxy:
writable['one'] = 42
read_only
# mappingproxy({'one': 42, 'two': 2})

# Takeaways:

# • Dictionaries are the central data structure in Python.
# • The built-in dict type will be “good enough” most of the time.
# • Specialized implementations, like read-only or ordered dicts,
# are available in the Python standard library.
