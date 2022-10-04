# Defining Your Own Exception Classes

# When I started using Python, I was hesitant to write custom exception
# classes in my code. But defining your own error types can be of great
# value. You’ll make potential error cases stand out clearly, and as a
# result, your functions and modules will become more maintainable.

# You can also use custom error types to provide additional debugging information.

def validate(name):
    if len(name) < 10:
        raise ValueError

# When a name fails to validate, it'll look like this ins the debug stack.

validate('joe')
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
#     validate('joe')
#   File "<input>", line 3, in validate
#     raise ValueError
# ValueError

# This is not really helpful. Your teammate can have a hard time with it.


class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)
        
# This is a self documenting exception. So that's better.

# The same is true even if you’re working on a code base all by yourself.
# A few weeks or months down the road you’ll have a much easier time
# maintaining your code if it’s well-structured.


# !
# A GOOD PRACTICE
# !

# Whenever you’re publicly releasing a Python package, or even if you’re
# creating a reusable module for your company, it’s good practice to 
# create a custom exception base class for the module and then derive all
# of your other exceptions from it.

# Here’s how to create a custom exception hierarchy for all exceptions
# in a module or package. The first step is to declare a base class that
# all of our concrete errors will inherit from:

class BaseValidationError(ValueError):
    pass

# Now, all of our “real” error classes can be derived from the base error
# class. This gives a nice and clean exception hierarchy with little extra effort:

class NameTooShortError(BaseValidationError):
    pass

class NameTooLongError(BaseValidationError):
    pass

class NameTooCuteError(BaseValidationError):
    pass

# Defining your own exception types will state your code’s intent more clearly and make it easier to debug.

# Derive your custom exceptions from Python’s built-in Exception class or from more specific exception classes like ValueError or KeyError.

# You can use inheritance to define logically grouped exception hierarchies.

#
# Cloning Objects for Fun and Profit
# 

# Assignment statements in Python do not create copies of objects, they
# only bind names to an object. For immutable objects, that usually doesn’t make a difference.

# But for working with mutable objects or collections of mutable objects,
# you might be looking for a way to create “real copies” or “clones” of these objects.

