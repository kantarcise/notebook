# What Namedtuples Are Good For

# Python comes with a specialized “namedtuple” container type that
# doesn’t seem to get the attention it deserves. It’s one of those amazing
# features in Python that’s hidden in plain sight.

# Namedtuples can be a great alternative to defining a class manually,
# and they have some other interesting features that I want to introduce
# you to in this chapter.

# Now, what’s a namedtuple and what makes it so special? A good way
# to think about namedtuples is to view them as an extension of the
# built-in tuple data type.

# Python’s tuples are a simple data structure for grouping arbitrary
# objects. Tuples are also immutable—they cannot be modified once
# they’ve been created. Here’s a brief example:

tuples_are_immutable = ('hello', object(), 42)

tuples_are_immutable
# ('hello', <object object at 0x105e76b70>, 42)
tuples_are_immutable[2]
# 42
tuples_are_immutable[2] = 23
# TypeError:
# "'tuple' object does not support item assignment"

# Problem 1

# One downside of plain tuples is that the data you store in them can only be pulled out by accessing it through integer indexes.
# You can’t give names to individual properties stored in a tuple. This can impact code readability.

# Problem 2

#  A tuple is always an ad-hoc structure. 

# Ad Hoc is: "created or done for a particular purpose as necessary."

# It’s hard to ensure that two tuples have the same
# number of fields and the same properties stored on them.

# Namedtuples to the Rescue

# Namedtuples were added to the standard library in Python 2.6. To use them, you need to
# import the collections module. 

# Here is a Car example, a Car data type with two fields: color and mileage.

from collections import namedtuple

Car = namedtuple('Car' , 'color mileage')

# Namedtuple’s factory function calls split() on the field names string 
# to parse it into a list of field names. So this is really just a shorthand for the following two steps:

'color mileage'.split()
# ['color', 'mileage']
Car = namedtuple('Car', ['color', 'mileage'])

# Whatever you decide, you can now create new “car” objects with the
# Car factory function. It behaves as if you had defined a Car class manually and given
# it a constructor accepting a “color” and a “mileage” value:

my_car = Car('red', 3812.4)
my_car.color
# 'red'
my_car.mileage
# 3812.4

my_car[0]
# 'red'

# What is this ??
tuple(my_car)
# ('red', 3812.4) 

# Tuple unpacking and the *-operator for function argument unpacking also work as expected:

color, mileage = my_car
print(color, mileage)
# red 3812.4
print(*my_car)
# red 3812.4

# Like tuples, namedtuples are immutable. 

my_car.color = "blue"
# AttributeError: "can't set attribute"

# SUMMARY

# A good way to view them is to think that namedtuples are a memory-
# efficient shortcut to defining an immutable class in Python manually.
