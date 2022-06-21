#  Lists and tuples are arguably Python’s most versatile, useful data types.

# Lists
# In short, a list is a collection of arbitrary objects, somewhat
# akin to an array in many other programming languages but more flexible.

a_list = ['foo', 'bar', 'baz', 'qux']

#   Lists are ordered. - Indexes and all
#   Lists can contain any arbitrary objects. - The elements can be of varying types (func, module, float, int).
#   List elements can be accessed by index.
#   Lists can be nested to arbitrary depth.
#   Lists are mutable.
#   Lists are dynamic.

a_list[2]
# baz

a_list[-3]
# bar

# If a is a list, the expression a[m:n] returns the portion of a from index m to, but not including, index n:

a_list[1:3]
# ['bar', 'baz']

# We can use stride

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

# 2 Stride
a[0:6:2]
# ['foo', 'baz', 'quux']


# The [:] syntax works for lists.
# However, there is an important difference between how this operation works with a list and how it works with a string.

# If s is a string, s[:] returns a reference to the same object:
  
s = 'foobar'
s[:]
# 'foobar'
s[:] is s
# True

# Conversely, if a is a list, a[:] returns a new object that is a copy of a:

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

# A new object that is copy of a
a[:]
# ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a[:] is a
# False


# Left at in and not operators
  

