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
