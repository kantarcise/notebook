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



