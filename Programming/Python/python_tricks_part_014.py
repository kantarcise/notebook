 # Common Data Structures in Python - Records.

#  This part we'll see how to implement records, structs, and
# “plain old data objects” in Python, using only built-in data types and
# classes from the standard library.

# dict – Simple Data Objects

car1 = {
    'color': 'red',
    'mileage': 3812.4,
    'automatic': True,
}

car2 = {
    'color': 'blue',
    'mileage': 40231,
    'automatic': False,
}

# Dicts have a nice repr:
car2
# {'color': 'blue', 'automatic': False, 'mileage': 40231}

# Get mileage:
car2['mileage']
# 40231

# Dicts are mutable:
car2['mileage'] = 12
car2['windshield'] = 'broken'
car2
# {'windshield': 'broken', 'color': 'blue',
#  'automatic': False, 'mileage': 12}

# No protection against wrong field names,
# or missing/extra fields:

car3 = {
'colr': 'green',
'automatic': False,
'windshield': 'broken',
 }

# ------------------------------------------------------

# tuples - Immutable Groups of Objects

# Python’s tuples are simple data structures for grouping arbitrary objects.
# Tuples are immutable—they cannot be modified once they’ve been created.

# Performance-wise, tuples take up slightly less memory than lists in
# CPython,17 and they’re also faster to construct. But this is negligible.

# A potential downside of plain tuples is that the data you store in them
# can only be pulled out by accessing it through integer indexes. You
# can’t give names to individual properties stored in a tuple. This can
# impact code readability.

# Also, a tuple is always an ad-hoc structure: It’s difficult to ensure that
# two tuples have the same number of fields and the same properties stored on them.

# Fields: color, mileage, automatic
car1 = ('red', 3812.4, True)
car2 = ('blue', 40231.0, False)

# Tuple instances have a nice repr:
car1
# ('red', 3812.4, True)
car2
# ('blue', 40231.0, False)

# Get mileage:
car2[1]
# 40231.0

# Tuples are immutable:
car2[1] = 12
# TypeError:
# "'tuple' object does not support item assignment"

# No protection against missing/extra fields or a wrong order:
car3 = (3431.5, 'green', True, 'silver')

# ------------------------------------------------------

# Writing a Custom Class – More Work, More Control

# Using regular Python classes as record data types is feasible, but it also
# takes manual work to get the convenience features of other implementations.
# For example, adding new fields to the __init__ constructor is verbose and takes time.

# Also, the default string representation for objects instantiated from
# custom classes is not very helpful. To fix that you may have to add
# your own __repr__ method,18 which again is usually quite verbose
# and must be updated every time you add a new field.

# Fields stored on classes are mutable, and new fields can be added
# freely, which you may or may not like. It’s possible to provide more
# access control and to create read-only fields using the @property decorator,
# but once again, this requires writing more glue code.

# Writing a custom class is a great option whenever you’d like to add
# business logic and behavior to your record objects using methods.
# However, this means that these objects are technically no longer plain data objects.


class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic

car1 = Car('red', 3812.4, True)
car2 = Car('blue', 40231.0, False)

# Get the mileage:
car2.mileage
# 40231.0

# Classes are mutable:
car2.mileage = 12
car2.windshield = 'broken'

# String representation is not very useful
# (must add a manually written __repr__ method):
car1
# <Car object at 0x1081e69e8>

# ------------------------------------------------------

#  collections.namedtuple – Convenient Data Objects

# The namedtuple class available in Python 2.6+ provides an extension
# of the built-in tuple data type.20 Similar to defining a custom class,
# using namedtuple allows you to define reusable “blueprints” for your
# records that ensure the correct field names are used.

# Namedtuples are immutable, just like regular tuples. This means you
# cannot add new fields or modify existing fields after the namedtuple
# instance was created.

# Besides that, namedtuples are, well… named tuples. Each object stored
# in them can be accessed through a unique identifier. This frees you
# from having to remember integer indexes, or resort to
# workarounds like defining integer constants as mnemonics for your indexes.

# Namedtuple objects are implemented as regular Python classes internally.
# When it comes to memory usage, they are also “better” than
# regular classes and just as memory efficient as regular tuples:

from collections import namedtuple
from sys import getsizeof

p1 = namedtuple('Point', 'x y z')(1, 2, 3)
p2 = (1, 2, 3)
getsizeof(p1)
# 72
getsizeof(p2)
# 72

# Namedtuples can be an easy way to clean up your code and make it
# more readable by enforcing a better structure for your data.
# I find that going from ad-hoc data types, like dictionaries with a fixed
# format, to namedtuples helps me express the intent of my code more
# clearly. Often when I apply this refactoring, I magically come up with
# a better solution for the problem I’m facing.

# Using namedtuples over regular (unstructured) tuples and dicts can
# also make my coworkers’ lives easier: Namedtuples make the data
# that’s being passed around “self-documenting”, at least to a degree.

from collections import namedtuple
Car = namedtuple('Car' , 'color mileage automatic')
car1 = Car('red', 3812.4, True)

# Instances have a nice repr:
car1
# Car(color='red', mileage=3812.4, automatic=True)
# Accessing fields:
car1.mileage
# 3812.4

# Fields are immtuable:

car1.mileage = 12
# AttributeError: "can't set attribute"

car1.windshield = 'broken'
# AttributeError:
# "'Car' object has no attribute 'windshield'"

# ------------------------------------------------------

# typing.NamedTuple – Improved Namedtuples

# This class added in Python 3.6 is the younger sibling of the
# namedtuple class in the collections module.21 It is very similar
# to namedtuple, the main difference being an updated syntax for
# defining new record types and added support for type hints.

# Please note that type annotations are not enforced without a separate
# type-checking tool like mypy. But even without tool support, they
# can provide useful hints for other programmers (or be terribly confusing if the type hints become out-of-date.)

from typing import NamedTuple

class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool

car1 = Car('red', 3812.4, True)

# Instances have a nice repr:
car1
# Car(color='red', mileage=3812.4, automatic=True)

# Accessing fields:
car1.mileage
# 3812.4

# Fields are immutable:
car1.mileage = 12
# AttributeError: "can't set attribute"
car1.windshield = 'broken'
# AttributeError:
# "'Car' object has no attribute 'windshield'"

# Type annotations are not enforced without
# a separate type checking tool like mypy:
Car('red', 'NOT_A_FLOAT', 99)
# Car(color='red', mileage='NOT_A_FLOAT', automatic=99)


# ------------------------------------------------------
