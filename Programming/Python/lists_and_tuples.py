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


a
# ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

'qux' in a
# True
'thud' not in a
# False


a + ["additional" , "members"]

a
# ['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'additional', 'members']

len(a)
# 8

min(a)
# 'bar'

max(a)
# 'qux'

# The smallest possible character is the capital letter A, since 
# all capital letters come first in Python. Our largest character is the lowercase letter z.

# Nested Lists
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']

x[1][1][-1]
# 'ddd'

# The list is the first mutable data type you have encountered. 
# Once a list has been created, elements can be added, deleted, 
# shifted, and moved around at will. Python provides a wide range of ways to modify lists.


# You can insert multiple elements in place of a single element—just use a slice that denotes only one element:


a = [1, 2, 3]
a[1:2] = [2.1, 2.2, 2.3]
a
# [1, 2.1, 2.2, 2.3, 3]

# You can also insert elements into a list without removing anything.

a = [1, 2, 7, 8]
a[2:2] = [3, 4, 5, 6]
a
# [1, 2, 3, 4, 5, 6, 7, 8]

# Methods That Modify a List

a = ['a', 'b']
a.append(123)
a
# ['a', 'b', 123]

# extend() also adds to the end of a list, but the argument is expected to be an iterable.

a = ['a', 'b']
a.extend([1, 2, 3])
a
# ['a', 'b', 1, 2, 3]

# Inserting an object to a specified index

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a.insert(3, 3.14159)
a[3]
# 3.14159
a
# ['foo', 'bar', 'baz', 3.14159, 'qux', 'quux', 'corge']

# Removing objects from lists

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
a.remove('baz')
a
# ['foo', 'bar', 'qux', 'quux', 'corge']

# Pop it!
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

a.pop()
# 'corge'
a
# ['foo', 'bar', 'baz', 'qux', 'quux']

a.pop()
# 'quux'
a
# ['foo', 'bar', 'baz', 'qux']

#
# Python Tuples
#


# Tuples are defined by enclosing the elements 
# in parentheses (()) instead of square brackets ([]).
# Tuples are immutable.


# Everything you’ve learned about lists—they are ordered, 
# they can contain arbitrary objects, they can be indexed and sliced, 
# they can be nested—is true of tuples as well. But they can’t be modified:

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
t
# ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')

t[0]
# 'foo'
t[-1]
# 'corge'
t[1::2]
# ('bar', 'qux', 'corge')

t[2] = 'Bark!'
# Traceback (most recent call last):
#   File "<pyshell#65>", line 1, in <module>
#     t[2] = 'Bark!'
# TypeError: 'tuple' object does not support item assignment

# Packing and Unpacking in a Tuple

t = ('foo', 'bar', 'baz', 'qux')

t[0]
# 'foo'
t[-1]
# 'qux'

(s1, s2, s3, s4) = t
s1
# 'foo'
s2
# 'bar'
s3
# 'baz'
s4
# 'qux'



