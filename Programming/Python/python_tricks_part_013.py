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

# ---------------------------------------------------------------

# bytes – Immutable Arrays of Single Bytes

# Bytes objects are immutable sequences of single bytes (integers in the
# range of 0 <= x <= 255). Conceptually, they’re similar to str objects,
# and you can also think of them as immutable arrays of bytes.

# Like strings, bytes have their own literal syntax for creating objects
# and they’re space-efficient. Bytes objects are immutable, but unlike
# strings, there’s a dedicated “mutable byte array” data type called
# bytearray that they can be unpacked into. You’ll hear more about that in the next section.

arr = bytes((0, 1, 2, 3))
arr[1]
# 1

# Bytes literals have their own syntax:
arr
# b'x00x01x02x03'
arr = b'x00x01x02x03'

# Only valid "bytes" are allowed:
bytes((0, 300))
# ValueError: "bytes must be in range(0, 256)"

# Bytes are immutable:
arr[1] = 23
# TypeError:
# "'bytes' object does not support item assignment"

del arr[1]
# TypeError:
# "'bytes' object doesn't support item deletion"

# ---------------------------------------------------------------

# bytearray – Mutable Arrays of Single Bytes

# The bytearray type is a mutable sequence of integers in the range
# 0 <= x <= 255.13 They’re closely related to bytes objects with the
# main difference being that bytearrays can be modified freely—you can
# overwrite elements, remove existing elements, or add new ones. The
# bytearray object will grow and shrink accordingly.

# Bytearrays can be converted back into immutable bytes objects but
# this involves copying the stored data in full—a slow operation taking O(n) time.

arr = bytearray((0, 1, 2, 3))
arr[1]
# 1

# The bytearray repr:
arr
# bytearray(b'x00x01x02x03')

# Bytearrays are mutable:
arr[1] = 23
arr
# bytearray(b'x00x17x02x03')

arr[1]
# 23

# Bytearrays can grow and shrink in size:
del arr[1]
arr
# bytearray(b'x00x02x03')

arr.append(42)
arr
# bytearray(b'x00x02x03*')

# Bytearrays can only hold "bytes"
# (integers in the range 0 <= x <= 255)
arr[1] = 'hello'
# TypeError: "an integer is required"

arr[1] = 300
# ValueError: "byte must be in range(0, 256)"

# Bytearrays can be converted back into bytes objects:
# (This will copy the data)
bytes(arr)
# b'x00x02x03*'

-----

# Takeaways:

# There are a number of built-in data structures you can choose from
# when it comes to implementing arrays in Python. In this chapter we’ve
# focused on core language features and data structures included in the standard library only.

# If you’re willing to go beyond the Python standard library, third-party
# packages like NumPy offer a wide range of fast array implementations
# for scientific computing and data science.

# By restricting ourselves to the array data structures included with
# Python, here’s what our choices come down to:

# You need to store arbitrary objects, potentially with mixed data types? 

# Use a list or a tuple, depending on whether you want an immutable data structure or not.

# You have numeric (integer or floating point) data and tight packing and performance is important? 

# Try out array.array and see if it does everything you need. Also, consider going beyond the
# standard library and try out packages like NumPy or Pandas.

# You have textual data represented as Unicode characters?

# Use Python’s built-in str. If you need a “mutable string,” use a list of characters.

# You want to store a contiguous block of bytes? Use the immutable bytes type, or bytearray if you need a mutable data structure.

# In most cases, I like to start out with a simple list. I’ll only specialize
# later on if performance or storage space becomes an issue. Most of
# the time, using a general-purpose array data structure like list gives
# you the fastest development speed and the most programming convenience.

# I found that this is usually much more important in the beginning
# than trying to squeeze out every last drop of performance right from the start.
