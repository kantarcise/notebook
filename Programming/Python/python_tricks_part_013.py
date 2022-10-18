# Common Data Structures in Python - Arrays.

# Arrays consist of fixed-size data records that allow each element to be
# efficiently located based on its index.

# Performance-wise, it’s very fast to look up an element contained in
# an array given the element’s index. A proper array implementation
# guarantees a constant O(1) access time for this case.

# ---------------------------------------------------------------

# list – Mutable Dynamic Arrays
# Lists are a part of the core Python language.8 Despite their name,
# Python’s lists are implemented as dynamic arrays behind the scenes.
# This means a list allows elements to be added or removed, and the list
# will automatically adjust the backing store that holds these elements
# by allocating or releasing memory.

# Python lists can hold arbitrary elements—“everything” is an object in
# Python, including functions. Therefore, you can mix and match different kinds
# of data types and store them all in a single list.

# This can be a powerful feature, but the downside is that supporting
# multiple data types at the same time means that data is generally less
# tightly packed. And as a result, the whole structure takes up morespace.

arr = ['one', 'two', 'three']
arr[0]
# 'one'

# Lists have a nice repr:
arr
# ['one', 'two', 'three']

# Lists are mutable:
arr[1] = 'hello'
arr
# ['one', 'hello', 'three']

del arr[1]
arr
# ['one', 'three']

# Lists can hold arbitrary data types:
arr.append(23)
arr
# ['one', 'three', 23]


# ---------------------------------------------------------------

# tuple – Immutable Containers

# Just like lists, tuples are also a part of the Python core language. 
# Unlike lists, however, Python’s tuple objects are immutable. This means
# elements can’t be added or removed dynamically—all elements in a tuple must be defined at creation time.

# Just like lists, tuples can hold elements of arbitrary data types. Having
# this flexibility is powerful, but again, it also means that data is less
# tightly packed than it would be in a typed array.

arr = 'one', 'two', 'three'

arr[0]
# 'one'

# Tuples have a nice repr:
arr
# ('one', 'two', 'three')

# Tuples are immutable:
arr[1] = 'hello'
# TypeError:
# "'tuple' object does not support item assignment"

del arr[1]
# TypeError:
# "'tuple' object doesn't support item deletion"

# Tuples can hold arbitrary data types:
# (Adding elements creates a copy of the tuple)
arr + (23,)
# ('one', 'two', 'three', 23)

# ----------------------------------------------------------------

# array.array – Basic Typed Arrays
# IMPORTANT FOR OPTIMIZATION

# Python’s array module provides space-efficient storage of basic C-
# style data types like bytes, 32-bit integers, floating point numbers, and so on.

# Arrays created with the array.array class are mutable and behave
# similarly to lists, except for one important difference—they are “typed
# arrays” constrained to a single data type.

import array

arr = array.array('f', (1.0, 1.5, 2.0, 2.5))

arr[1]
1.5

# Arrays have a nice repr:
arr
# array('f', [1.0, 1.5, 2.0, 2.5])

# Arrays are mutable:
arr[1] = 23.0
arr
# array('f', [1.0, 23.0, 2.0, 2.5])

del arr[1]
arr
# array('f', [1.0, 2.0, 2.5])

arr.append(42.0)
arr
# array('f', [1.0, 2.0, 2.5, 42.0])

# Arrays are "typed":
arr[1] = 'hello'
# TypeError: "must be real number, not str"


# ----------------------------------------------------------------

# str – Immutable Arrays of Unicode Characters

# Python 3.x uses str objects to store textual data as immutable sequences
# of Unicode characters.11 Practically speaking, that means a str is an
# immutable array of characters. Oddly enough, it’s also a recursive data structure, 
# each character in a string is a str object of length 1 itself.

# String objects are space-efficient because they’re tightly packed and
# they specialize in a single data type. If you’re storing Unicode text, you
# should use them. Because strings are immutable in Python, modifying
# a string requires creating a modified copy. The closest equivalent to a
# “mutable string” is storing individual characters inside a list.

arr = 'abcd'
arr[1]
# 'b'
arr
# 'abcd'

# Strings are immutable:
arr[1] = 'e'
# TypeError:
# "'str' object does not support item assignment"

del arr[1]
# TypeError:
# "'str' object doesn't support item deletion"

# Strings can be unpacked into a list to
# get a mutable representation:
list('abcd')
# ['a', 'b', 'c', 'd']
''.join(list('abcd'))
# 'abcd'

# Strings are recursive data structures:
type('abc')
# "<class 'str'>"
type('abc'[0])
# "<class 'str'>"

