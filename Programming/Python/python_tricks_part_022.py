# Beautiful Iterators

numbers = [1, 2, 3]
for n in numbers:
    print(n)

# But how do Python’s elegant loop constructs work behind the scenes?
# How does the loop fetch individual elements from the object it is 
# looping over? And, how can you support the same programming style in
# your own Python objects?

# You’ll find the answers to these questions in Python’s iterator 
# protocol: Objects that support the __iter__ and __next__ dunder 
# methods automatically work with for-in loops.

class Repeater:
    def __init__(self, value):
        self.value = value
    def__iter__(self):
        return RepeaterIterator(self)

# On first inspection, Repeater looks like a bog-standard Python class.
# But notice how it also includes the __iter__ dunder method.

# What’s the RepeaterIterator object we’re creating and returning
# from __iter__? It’s a helper class we also need to define for our
# for-in iteration example to work:

class RepeaterIterator:
    def __init__(self, source):
        self.source = source
    def__next__(self):
        return self.source.value
      
# 1. In the __init__ method, we link each RepeaterIterator instance
# to the Repeater object that created it. That way we can
# hold onto the “source” object that’s being iterated over.
# 2. In RepeaterIterator.__next__, we reach back into the
# “source” Repeater instance and return the value associated with it.

repeater = Repeater('Hello')

for item in repeater:
    print(item)
    
# Results in a forever loop

# Hello
# Hello
# Hello
# Hello
# Hello
# ...

# Next up, we’ll tease this example apart to understand how the
# __iter__ and __next__ methods work together to make a Python
# object iterable.

# These two, does the same thing:


# 1

repeater = Repeater('Hello')

for item in repeater:
    print(item)
    
# 2

repeater = Repeater('Hello')
iterator = repeater.__iter__()

while True:
    item = iterator.__next__()
    print(item)

# • It first prepared the repeater object for iteration by calling its
# __iter__ method. This returned the actual iterator object.
# • After that, the loop repeatedly called the iterator object’s
# __next__ method to retrieve values from it.

# Whether you’re dealing with a list of elements, a dictionary, an infinite
# sequence like the one provided by our Repeater class, or another sequence
# type—all of that is just an implementation detail. Every single
# one of these objects can be traversed in the same way with the power of iterators.

# In a Python Interpreter, you can actually do:

repeater = Repeater('Hello')
iterator = iter(repeater)
next(iterator)
# 'Hello'
next(iterator)
# 'Hello'
next(iterator)
# 'Hello'
...

# "Quick note on facades"

# By the way, I took the opportunity here to replace the calls to __iter__
# and __next__ with calls to Python’s built-in functions, iter() and next().

# Internally, these built-ins invoke the same dunder methods, but they
# make this code a little prettier and easier to read by providing a clean
# “facade” to the iterator protocol.

# Python offers these facades for other functionality as well. For
# example, len(x) is a shortcut for calling x.__len__. Similarly,
# calling iter(x) invokes x.__iter__ and calling next(x) invokes x.__next__.
