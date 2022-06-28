# Thid script is all about Python sets.

# Defining a Set
# Python’s built-in set type has the following characteristics:
#   Sets are unordered.
#   Set elements are unique. Duplicate elements are not allowed.
#   A set itself may be modified, but the elements contained in the set must be of an immutable type.

x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
x
# {'qux', 'foo', 'bar', 'baz'}

x = set(('foo', 'bar', 'baz', 'foo', 'qux'))
x
# {'qux', 'foo', 'bar', 'baz'}


# Alternately, a set can be defined with curly braces ({}):

x = {'foo', 'bar', 'baz', 'foo', 'qux'}
x
# {'qux', 'foo', 'bar', 'baz'}

x = {'q', 'u', 'u', 'x'}
x
# {'x', 'q', 'u'}

# We cannot define and empty set curly braces, gotta use set()

x = set()
type(x)
# <class 'set'>
x
# set()

# The elements in a set can be objects of different types:

x = {42, 'foo', 3.14159, None}


# Don’t forget that set elements must be immutable. For example, a tuple may be included in a set:

x = {42, 'foo', (1, 2, 3), 3.14159}
x
# {42, 'foo', 3.14159, (1, 2, 3)}

# But lists and dictionaries are mutable, so they can’t be set elements:

a = [1, 2, 3]
{a}
# Traceback (most recent call last):
#  File "<pyshell#70>", line 1, in <module>
#    {a}
# TypeError: unhashable type: 'list'

d = {'a': 1, 'b': 2}
{d}
# Traceback (most recent call last):
#   File "<pyshell#72>", line 1, in <module>
#    {d}
# TypeError: unhashable type: 'dict'

# Set Size and Membership

# The len() function returns the number of elements in a set
# the in and not in operators can be used to test for membership:

x = {'foo', 'bar', 'baz'}
len(x)
#3

'bar' in x
# True
'qux' in x
# False

# Operating on a Set

# Many of the operations that can be used for Python’s other composite data types 
# don’t make sense for sets. For example, sets can’t be indexed or sliced. However, Python provides 
# a whole host of operations on set objects that generally mimic the operations that are defined for mathematical sets.

# Operators vs. Methods

# Most, though not quite all, set operations in Python can be performed in two different ways: by operator or by method.
# Let’s take a look at how these operators and methods work, using set union as an example.

# In Python, set union can be performed with the | operator:

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1 | x2
# {'baz', 'quux', 'qux', 'bar', 'foo'}

# Set union can also be obtained with the .union() method.
# The method is invoked on one of the sets, and the other is passed as an argument:

# x1.union(x2)
{'baz', 'quux', 'qux', 'bar', 'foo'}

# The way they are used in the examples above, the operator and method 
# behave identically. But there is a subtle difference between them. When you
# use the | operator, both operands must be sets. The .union() method, on the
# other hand, will take any iterable as an argument, convert it to a set, and then perform the union.

# Observe the difference between these two statements:

x1 | ('baz', 'qux', 'quux')
# Traceback (most recent call last):
#   File "<pyshell#43>", line 1, in <module>
#     x1 | ('baz', 'qux', 'quux')
# TypeError: unsupported operand type(s) for |: 'set' and 'tuple'

x1.union(('baz', 'qux', 'quux'))
# {'baz', 'quux', 'qux', 'bar', 'foo'}

# Both attempt to compute the union of x1 and the tuple ('baz', 'qux', 'quux').
# This fails with the | operator but succeeds with the .union() method.


# Available Operators and Methods

# Below is a list of the set operations available in Python. Some are performed by 
# operator, some by method, and some by both. The principle outlined above generally 
# applies: where a set is expected, methods will typically accept
# any iterable as an argument, but operators require actual sets as operands.

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

a.union(b, c, d)
# {1, 2, 3, 4, 5, 6, 7}

a | b | c | d
# {1, 2, 3, 4, 5, 6, 7}


# x1.intersection(x2[, x3 ...])
# x1 & x2 [& x3 ...]

#     Compute the intersection of two or more sets.
x1 = {'foo', 'bar', 'baz'}
# x2 = {'baz', 'qux', 'quux'}
x1.intersection(x2)
# {'baz'}
x1 & x2
# {'baz'}


# You can specify multiple sets with the intersection method and operator, just like you can with set union:

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

a.intersection(b, c, d)
# {4}
a & b & c & d
# {4}


# x1.difference(x2[, x3 ...])
# x1 - x2 [- x3 ...]

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

x1.difference(x2)
# {'foo', 'bar'}

x1 - x2
# {'foo', 'bar'}

# Once again, you can specify more than two sets:

a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}

# a.difference(b, c)
{1, 2, 3}
# a - b - c
{1, 2, 3}

# x1.symmetric_difference(x2)
# x1 ^ x2 [^ x3 ...]

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

x1.symmetric_difference(x2)
# {'foo', 'qux', 'quux', 'bar'}

x1 ^ x2
# {'foo', 'qux', 'quux', 'bar'}

# x1.isdisjoint(x2)
#    Determines whether or not two sets have any elements in common.

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}

x1.isdisjoint(x2)
# False



# x1.issubset(x2)
#    Determine whether one set is a subset of the other.

x1 = {'foo', 'bar', 'baz'}
x1.issubset({'foo', 'bar', 'baz', 'qux', 'quux'})
# True

x2 = {'baz', 'qux', 'quux'}
x1 <= x2
# False

# Proper Subset
x1 = {'foo', 'bar'}
x2 = {'foo', 'bar', 'baz'}
x1 < x2
# True

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar', 'baz'}
x1 < x2
False



# x1.issuperset(x2)
# x1 >= x2

x1 = {'foo', 'bar', 'baz'}
x1.issuperset({'foo', 'bar'})
# True

x2 = {'baz', 'qux', 'quux'}
x1 >= x2
# False


# x1 > x2
#   Determines whether one set is a proper superset of the other.

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar'}
x1 > x2
# True

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar', 'baz'}
x1 > x2
# False


# x1.update(x2[, x3 ...])
# x1 |= x2 [| x3 ...]

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 |= x2
x1
# {'qux', 'foo', 'bar', 'baz'}



# x1.intersection_update(x2[, x3 ...])
# x1 &= x2 [& x3 ...]

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 &= x2
x1
# {'foo', 'baz'}

# x1.difference_update(x2[, x3 ...])
# x1 -= x2 [| x3 ...]

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 -= x2
x1
# {'bar'}


x = {'foo', 'bar', 'baz'}
x.add('qux')
x
# {'bar', 'baz', 'foo', 'qux'}


x = {'foo', 'bar', 'baz'}
x.remove('baz')
x
# {'bar', 'foo'}

x.remove('qux')
# Traceback (most recent call last):
#   File "<pyshell#58>", line 1, in <module>
#     x.remove('qux')
# KeyError: 'qux'


x = {'foo', 'bar', 'baz'}
x.discard('baz')
x
# {'bar', 'foo'}


# x.pop()
#    Removes a random element from a set.

x = {'foo', 'bar', 'baz'}
x.pop()
# 'bar'
x
# {'baz', 'foo'}

# x.clear()

x = {'foo', 'bar', 'baz'}
x
# {'foo', 'bar', 'baz'}
x.clear()
x
# set()



# Frozen Sets

# Python provides another built-in type called a frozenset, which is in
# all respects exactly like a set, except that a frozenset is immutable. You can perform non-modifying operations on a frozenset:

x = frozenset(['foo', 'bar', 'baz'])
x
# frozenset({'foo', 'baz', 'bar'})
len(x)
# 3


# Likewise, recall from the previous tutorial on dictionaries that a 
# dictionary key must be immutable. You can’t use the built-in set type as a dictionary key:

# If you find yourself needing to use sets as dictionary keys, you can use frozensets:

x = frozenset({1, 2, 3})
y = frozenset({'a', 'b', 'c'})
 
d = {x: 'foo', y: 'bar'}
d
# {frozenset({1, 2, 3}): 'foo', frozenset({'c', 'a', 'b'}): 'bar'}
