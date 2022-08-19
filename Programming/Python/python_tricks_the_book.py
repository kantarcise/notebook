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

# Double Leading Underscore: “__var ”

# A double underscore prefix causes the Python interpreter to rewrite
# the attribute name in order to avoid naming conflicts in subclasses.

# This is also called name mangling—the interpreter changes the name
# of the variable in a way that makes it harder to create collisions when
# the class is extended later.

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 42
        
# If we check dir() :
t = Test()
dir(t)

# ['_Test__baz', '__class__', '__delattr__', '__dict__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', '_bar', 'foo']

# And if we inherit a class from Test, things get interesting

class ExtendedTest(Test):
    def __init__(self):
        self.foo = "overridden"
        self._bar = "overridden"
        self.__baz = "overridden"
        
# If we tried to check them:

t2 = ExtendedTest()
t2.foo
# "overridden"
t2._bar
# "overridden"
t2.__baz
# AttributeError:
# "'ExtendedTest' object has no attribute '__baz'"

# What in god's name ?!
# Let's check dir:

dir(t2)
# ['_ExtendedTest__baz', '_Test__baz', '__class__',
# '__delattr__', '__dict__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__le__', '__lt__',
# '__module__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__setattr__',
# '__sizeof__', '__str__', '__subclasshook__',
# '__weakref__', '_bar', 'foo', 'get_vars']

#  As you can see, __baz got turned into _ExtendedTest__baz to prevent
# accidental modification. But the original _Test__baz is also still around:

t2._ExtendedTest__baz
# 'overridden'
t2._Test__baz
# 42


# So, you cannot access dunder variables directly, gotta return them from somewhere or write explitcitly _Class__var .

class ManglingTest:
    def __init__(self):
        self.__mangled = 'hello'

    def get_mangled(self):
        return self.__mangled

ManglingTest().get_mangled()
# 'hello'
ManglingTest()_ManglingTest__mangled
# hello
ManglingTest().__mangled
# AttributeError:
# "'ManglingTest' object has no attribute '__mangled'"
