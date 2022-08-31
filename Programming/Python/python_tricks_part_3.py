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
# some functions manually in order to retain the ability to call the un-
# decorated function as well.

# Manually:

greet = uppercase(greet)



