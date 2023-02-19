# Namespaces and Object-Orientation

# A namespace is an abstraction that manages all of the identifiers that are defined in
# a particular scope, mapping each name to its associated value. In Python, functions,
# classes, and modules are all first-class objects, and so the “value” associated with
# an identifier in a namespace may in fact be a function, class, or module.

#  We begin by exploring what is known as the instance namespace, which manages
# attributes specific to an individual object.

# There is a separate class namespace for each class that has been defined. This
# namespace is used to manage members that are to be shared by all instances of
# a class, or used without reference to any particular instance.


# Class Data Members

# A class-level data member is often used when there is some value, such as a constant,
# that is to be shared by all instances of a class. In such a case, it would
# be unnecessarily wasteful to have each instance store that value in its instance namespace.

class MyClass:
    LIMIT_FEE = 20            # This is a Class Data Member
    
    def __init__(self):
        pass
      
      
# Nested Classes

class A:        # the outer class
    class B:    # the nested class
        ...

# For example, we will later introduce a data structure known as a linked list and will
# define a nested node class to store the individual components of the list.

# Dictionaries and the __slots__ Declaration

# By default, Python represents each namespace with an instance of the built-in dict
# class (see Section 1.2.3) that maps identifying names in that scope to the associated
# objects. While a dictionary structure supports relatively efficient name lookups,
# it requires additional memory usage beyond the raw data that it stores.

# The special attribute __slots__ allows you to explicitly state which instance attributes you expect your object instances to have, with the expected results:
#        faster attribute access.
#        space savings in memory.

# The space savings is from
#       Storing value references in slots instead of __dict__.
#       Denying __dict__ and __weakref__ creation if parent classes deny them and you declare __slots__.

