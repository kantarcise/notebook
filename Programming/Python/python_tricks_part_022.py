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



