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

