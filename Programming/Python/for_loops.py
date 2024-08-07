# In this file:

#    You’ll learn about iterables and iterators, two concepts that form the basis of definite iteration in Python.
#    Finally, you’ll tie it all together and learn about Python’s for loops.

# Python only implements collection-based iteration. 

for <var> in <iterable>:
    <statement(s)>

# <iterable> is a collection of objects—for example, a list or tuple. 
# The <statement(s)> in the loop body are denoted by indentation, as with all
# Python control structures, and are executed once for each item in <iterable>. The loop 
# variable <var> takes on the value of the next element in <iterable> each time through the loop

a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

# foo
# bar
# baz

# Iterables 

# If an object is iterable, it can be passed to the built-in Python function iter(), which returns something called an iterator. 

# Each of the objects in the following example is an iterable and returns some type of iterator when passed to iter():

iter('foobar')                             # String
# <str_iterator object at 0x036E2750>

iter(['foo', 'bar', 'baz'])                # List
# <list_iterator object at 0x036E27D0>

iter(('foo', 'bar', 'baz'))                # Tuple
# <tuple_iterator object at 0x036E27F0>

iter({'foo', 'bar', 'baz'})                # Set
# <set_iterator object at 0x036DEA08>

iter({'foo': 1, 'bar': 2, 'baz': 3})       # Dict
# <dict_keyiterator object at 0x036DD990>


# How do we use iter() function?

a = ['foo', 'bar', 'baz']

itr = iter(a)
itr
# <list_iterator object at 0x031EFD10>

next(itr)
# 'foo'
next(itr)
# 'bar'
next(itr)
# 'baz'

#  Any further attempts to obtain values from the iterator will fail.

next(itr)
# Traceback (most recent call last):
#    File "<pyshell#10>", line 1, in <module>
#    next(itr)
# StopIteration

# To get all of them (also set(itr) and tuple(itr) works)

a = ['foo', 'bar', 'baz']
itr = iter(a)
list(itr)
# ['foo', 'bar', 'baz']

# All the relevant terms so far:

# Iteration 	The process of looping through the objects or items in a collection
#
# Iterable 	    An object (or the adjective used to describe an object) that can be iterated over
#
# Iterator 	    The object that produces successive items or values from its associated iterable
#
# iter() 	    The built-in function used to obtain an iterator from an iterable


# The Pythonic way to iterate through a dictionary,
# accessing both the keys and values looks like this:

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in d.items():
    print('k =', k, ', v =', v)

# k = foo , v = 1
# k = bar , v = 2
# k = baz , v = 3

# range()

x = range(5)

for n in x:
    print(n)

# 0
# 1
# 2
# 3
# 4

# A for loop can have an else clause as well.

for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execute

# foo
# bar
# baz
# qux
# Done.

# The else clause won’t be executed if the list is broken out of with a break statement:

for i in ['foo', 'bar', 'baz', 'qux']:
    if i == 'bar':
        break
    print(i)
else:
    print('Done.')  # Will not execute

# foo



