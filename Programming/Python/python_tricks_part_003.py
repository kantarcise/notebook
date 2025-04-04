# Lambdas Are Single-Expression Functions

# The lambda keyword in Python provides a shortcut for declaring
# small anonymous functions. Lambda functions behave just like
# regular functions declared with the def keyword. They can be used
# whenever function objects are required.

add_numbers = lambda x, y: x + y
add_numbers(5, 3)
# 8

# One difference between lambdas and regular function definitions.
# Lambda functions are restricted to a single expression. This means a lambda function can’t use statements or
# annotations—not even a return statement.

# One of the most frequent use case for lambdas is writing
# short and concise key funcs for sorting iterables by an alternate key:

tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
sorted(tuples, key=lambda x: x[1])
# [(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]

# We've sorted a list of tuples by the second value in each tuple.

sorted(range(-5, 6), key=lambda x: x * x)
# [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]

# the key basically returns the value after the colon

# Lambdas can be hard to understand, so might be better of using the readable & maintainable python that we all know.

# Harmful:
list(filter(lambda x: x % 2 == 0, range(16)))
# [0, 2, 4, 6, 8, 10, 12, 14]

# Better (just list comprehension)
[x for x in range(16) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14]


#
# Decorators
#

# Decorators allow you to extend and modify the behaviour of a callable (functions, methods and classes) 
# without permanently modifying the callable itself.

# Understanding decorators is a milestone for any serious Python programmer.

# Quick reminder: The most important “first-class functions” takeaways for understanding decorators are:
# - Functions are objects—they can be assigned to variables and passed to and returned from other functions
# - Functions can be defined inside other functions—and a child function can capture the parent function’s local state (lexical closures)

# Decorators “decorate” or “wrap” another function and let you execute code before and after the wrapped function runs.

# It's a callable that takes a callable as input and returns another callable.

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return 'Hello!'

greet()
# 'HELLO!'

# Note that using the @ syntax decorates the function immediately at
# definition time. This makes it difficult to access the undecorated 
# original without brittle hacks. Therefore you might choose to decorate
# some functions manually:

# Manually:
greet = uppercase(greet)

# in order to retain the ability to call the undecorated function as well.

# Applying Multiple Decorators to a Function

# Perhaps not surprisingly, you can apply more than one decorator to a
# function. This accumulates their effects and it’s what makes decorators
# so helpful as reusable building blocks.

def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return "Hello!"

greet()
# '<strong><em>Hello!</em></strong>'

# This clearly shows in what order the decorators were applied: from
# bottom to top. First, the input function was wrapped by the @emphasis
# decorator, and then the resulting (decorated) function got wrapped
# again by the @strong decorator.

# To help me remember this bottom to top order, I like to call this behavior
# decorator stacking. You start building the stack at the bottom
# and then keep adding new blocks on top to work your way upwards.

# If we don't use @, it simply looks like this:

decorated_greet = strong(emphasis(greet))

# What about decorators that takes arguments ?

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')

        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'

say('Jane', 'Hello, World')
# 'TRACE: calling say() with ("Jane", "Hello, World"), {}'
# 'TRACE: say() returned "Jane: Hello, World"'
# 'Jane: Hello, World'

# How to Write “Debuggable” Decorators

# When you use a decorator, really what you’re doing is replacing one
# function with another. One downside of this process is that it “hides”
# some of the metadata attached to the original (undecorated) function.

def greet():
    """Return a friendly greeting."""
    return 'Hello!'

decorated_greet = uppercase(greet)

# If we tried to access the metadata:

greet.__name__
# 'greet'
greet.__doc__
# 'Return a friendly greeting.'
decorated_greet.__name__
# 'wrapper'
decorated_greet.__doc__
# None

# This claimed to be making debugging awkward (?). A quick fix for this.
# functools!

import functools
    
defuppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    """Return a friendly greeting."""
    return 'Hello!'

greet.__name__
# 'greet'
greet.__doc__
# 'Return a friendly greeting.'

# As a best practice, I’d recommend that you use functools.wraps in  all of the decorators you write yourself. 

# It doesn’t take much time and it will save you (and others) debugging headaches down the road.
