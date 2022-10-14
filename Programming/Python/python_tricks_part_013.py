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
