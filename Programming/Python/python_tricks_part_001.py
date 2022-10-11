# Assertion Errors

# If your program is bug-free, these conditions will never occur. But if
# they do occur, the program will crash with an assertion error telling
# you exactly which “impossible” condition was triggered. 

# This makes it much easier to track down and fix bugs in your programs.

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

# Double Leading and Trailing Underscore: “__var__”

# No mangling here

class PrefixPostfixTest:
    def __init__(self):
        self.__bam__ = 42

PrefixPostfixTest().__bam__
# 42

# However, names that have both leading and trailing double under-
# scores are reserved for special use in the language. This rule covers
# things like __init__ for object constructors, or __call__ to make objects callable.

# Single Underscore

# Per convention, a single stand-alone underscore is sometimes used as
# a name to indicate that a variable is temporary or insignificant.

for _ in range(32):
    print("Hello World!")


# Or a placeholder variable:

# In the following code example, we are unpacking a tuple into separate
# variables but we are only interested in the values for the color and
# mileage fields. However, in order for the unpacking expression to
# succeed, we need to assign all values contained in the tuple to variables.
# That’s where “_” is useful as a placeholder variable:


car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car
color
# 'red'
mileage
# 3812.4
_
# 12


# String Formatting

# There are 4 major ways to do string formatting in Python. Kinda unreal and go againts Zen of Python for sure.
# Anyway, here they come.

# 1- The old style:

# Strings in Python have a unique built-in operation that can be
# accessed with the %-operator. It’s a shortcut that lets you do simple
# positional formatting very easily.

errno = 50159747054
name = 'Bob'

print("Hello, %s", name)
# Hello, Bob

# You can control the output of the string aswell:

# Here, we areusing the %x format specifier to convert an int value to a
# string and to represent it as a hexadecimal number:

'%x' % errno
# 'badc0ffee'

# 2- The new style:

# You can use the format() function to do simple positional formatting,
# just like you could with “old style” formatting:

"Hello, {}".format(name)
# "Hello, Bob"

# 3 – Literal String Interpolation (Python 3.6+)

# Formatted String Literals. So the f-strings.

print(f'Hello, {name}!')
# 'Hello, Bob!'

# Behind the scenes, formatted string literals are a Python parser feature that converts 
# f-strings into a series of string constants and expressions. 
# They then get joined up to build the final string.

# f-strings are better, faster, stronger. So use them whenever you can.


