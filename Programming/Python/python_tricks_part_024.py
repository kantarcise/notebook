# Generator Expressions

# As I learned more about Python’s iterator protocol and the different
# ways to implement it in my own code, I realized that “syntactic sugar”
# was a recurring theme.

# You see, class-based iterators and generator functions are two expressions
# of the same underlying design pattern.

# Generator functions give you a shortcut for supporting the iterator
# protocol in your own code, and they avoid much of the verbosity of
# class-based iterators. With a little bit of specialized syntax, or 
# syntactic sugar, they save you time and make your life as a developer easier.

# This is a recurring theme in Python and in other programming 
# languages. As more developers use a design pattern in their programs,
# there’s a growing incentive for the language creators to provide 
# abstractions and implementation shortcuts for it.

# That’s how programming languages evolve over time—and as developers,
# we reap the benefits. We get to work with more and more powerful
# building blocks, which reduces busywork and lets us achieve more in less time.

# Earlier in this book you saw how generators provide syntactic sugar
# for writing class-based iterators. The generator expressions we’ll
# cover in this chapter add another layer of syntactic sugar on top.

# Generator expressions give you an even more effective shortcut for
# writing iterators. With a simple and concise syntax that looks like a
# list comprehension, you’ll be able to define iterators in a single line of code.

# Here’s an example:

iterator = ('Hello' for i in range(3))

# Careful about the paranthesis. it's circular.
# This is basically one line version of this:

def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value

iterator = bounded_repeater('Hello', 3)


# Back to what we've learned:

iterator = ("Hello" for i in range(3))

# We can use this generator with: 

for x in iterator:
    print(x)

# 'Hello'
# 'Hello'
# 'Hello'

# Generator Expressions vs List Comprehensions

listcomp = ['Hello' for i in range(3)]
genexpr = ('Hello' for i in range(3))

# Unlike list comprehensions, however, generator expressions don’t
# construct list objects. Instead, they generate values “just in time” like
# a class-based iterator or generator function would.

listcomp
# ['Hello', 'Hello', 'Hello']
genexpr
# <generator object <genexpr> at 0x1036c3200>

# To access the values produced by the generator we need to call next() on it.

next(genexpr)
# 'Hello'
next(genexpr)
# 'Hello'
next(genexpr)
# 'Hello'
next(genexpr)
# StopIteration

# Also we can call list() function on a generator to construct a list

list(genexpr)
# ['Hello', 'Hello', 'Hello']

# If you need a list object right away, you’d normally just write a
# list comprehension from the get-go.

# ---------------

# Generator General Expression

genexpr = (expression for item in collection)

# Which is:

def generator():
    for item in collection:
        yield expression

# We can filter values with conditions on generators as well

even_squares = (x * x for x in range(10)
                if x % 2 == 0)

for x in even_squares:
    print(x)

# 0
# 4
# 16
# 36
# 64

# With added if condition:
genexpr = (expression for item in collection
           if condition)

# In-line Generator Expressions
# Because generator expressions are, well...expressions, you can use
# them in-line with other statements. For example, you can define an
# iterator and consume it right away with a for -loop:

for x in ('Bom dia' for i in range(3)):
    print(x)

# Key Takeaways

# • Generator expressions are similar to list comprehensions.
# However, they don’t construct list objects. Instead, generator
# expressions generate values “just in time” like a class-based
# iterator or generator function would.
# • Once a generator expression has been consumed, it can’t be
# restarted or reused.
# • Generator expressions are best for implementing simple “ad
# hoc” iterators. For complex iterators, it’s better to write a 
# generator function or a class-based iterator.

