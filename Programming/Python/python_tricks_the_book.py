# Assertion Errors

# If your program is bug-free, these conditions will never occur. But if
# they do occur, the program will crash with an assertion error telling
# you exactly which “impossible” condition was triggered. This makes
# it much easier to track down and fix bugs in your programs. And I like
# anything that makes life easier—don’t you?

def apply_discount(product,discount):
    price = int(product["price"] * (1 - discount))
    assert 0 <= price <= product["price"]
    return price

# Single Leading Underscore: “_var”

# “Hey, this isn’t really meant to be a part of the
# public interface of this class. Best to leave it alone.”

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23

# Single Trailing Underscore: “var_”
 
# Sometimes the most fitting name for a variable is already taken by a
# keyword in the Python language. Therefore, names like class or def
# cannot be used as variable names in Python. In this case, you can
# append a single underscore to break the naming conflict:

def make_object(name, class_):
    pass

