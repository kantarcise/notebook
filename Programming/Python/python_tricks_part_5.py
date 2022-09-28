# Returns:

# Python adds an implicit return None statement to the end of any
# function. Therefore, if a function doesn’t specify a return value, it returns None by default.

# This means you can replace return None statements with bare
# return statements or even leave them out completely and still get
# the same result:

def foo1(value):
    if value:
        return value
    else:
        return None

def foo2(value):
    """Bare return statement implies `return None`"""
    if value:
        return value
    else:
        return

def foo3(value):
    """Missing return statement implies `return None`"""
    if value:
        return value

# All three functions properly return None if you pass them a falsy value
# as the sole argument:

type(foo1(0))
# <class 'NoneType'>

type(foo2(0))
# <class 'NoneType'>

type(foo3(0))
# <class 'NoneType'>

      
# Key Takeaways
# • If a function doesn’t specify a return value, it returns None.
# Whether to explicitly return None is a stylistic decision.

# • This is a core Python feature but your code might communicate
# its intent more clearly with an explicit return None statement.


# ---------------------------------------------------------------------------------------------------- #

# Classes and OOP

#  Object Comparisons: “is” vs “==”

# The == operator compares by checking for equality: if these cats were
# Python objects and we compared them with the == operator, we’d get
# “both cats are equal” as an answer.

# The is operator, however, compares identities: if we compared our
# cats with the is operator, we’d get “these are two different cats” as an
# answer.

a = [1,2,3]
b = a

a == b
# True

a is b
# True

c = list(a)

c 
# [1,2,3]

a == c
# True

a is c 
# False

# They have the same content but they are not the same object.

# The result:

# An is expression evaluates to True if two variables point to the same (identical) object.

# An == expression evaluates to True if the objects referred to by the variables are equal (have the same contents).

