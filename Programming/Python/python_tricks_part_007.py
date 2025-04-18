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

# Essentially, you’ll sometimes want copies that you can modify without
# automatically modifying the original at the same time. 

# This part will focus on how to copy or "clone" objects in Pyhton.

# The built-in mutable collections can ve copied with their factory functions, on an existing collection

# PS: Mutable collections - lists, dicts, sets.

new_list = list(original_list)
new_dict = dict(original_dict)
new_set = set(original_set)

# However, this method won’t work for custom objects and, on top of
# that, it only creates shallow copies. For compound objects like lists,
# dicts, and sets, there’s an important difference between shallow and deep copying:

# Shallow copies point to the same child objects so change in them, effects them both.

# Here is an example.

class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
           self.bottomright = bottomright
    
    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
                f'{self.bottomright!r})')


import copy
    
rect = Rectangle(Point(0, 1), Point(5, 6))
# A shallow copy:
srect = copy.copy(rect)

rect
# Rectangle(Point(0, 1), Point(5, 6))
srect
# Rectangle(Point(0, 1), Point(5, 6))
rect is srect
# False

# When we modify one of the child objects in original, this modification will be reflected in
# shallow copy as well—that’s because both share the same child objects. 
# The copy is only a shallow, one level deep copy:

rect.topleft.x = 999
rect
# Rectangle(Point(999, 1), Point(5, 6))
srect
# Rectangle(Point(999, 1), Point(5, 6))

# 
# A deep Copy
#

drect = copy.deepcopy(srect)
drect.topleft.x = 222
drect
# Rectangle(Point(222, 1), Point(5, 6))
rect
# Rectangle(Point(999, 1), Point(5, 6))
srect
# Rectangle(Point(999, 1), Point(5, 6))

# Voila! This time the deep copy (drect) is fully independent of the
# original (rect ) and the shallow copy (srect).
    
