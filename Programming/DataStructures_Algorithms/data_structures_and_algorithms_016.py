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

# For our examples
class CreditCard:
    __slots__ = _customer , _bank , _account , _balance , _limit

class PredatoryCreditCard(CreditCard):
    __slots__ = _apr             # in addition to the inherited members

# We could choose to use the slots declaration to streamline every class in
# this book. However, we do not do so because such rigor would be atypical for
# Python programs. With that said, there are a few classes in this book for which
# we expect to have a large number of instances, each representing a lightweight
# construct. For example, when discussing nested classes, we suggest linked lists
# and trees as data structures that are often comprised of a large number of individual
# nodes. To promote greater efficiency in memory usage, we will use an explicit
# slots declaration in any nested classes for which we expect many instances.

# In traditional object-oriented terminology, Python uses what is known as dynamic dispatch (or dynamic binding) to
# determine, at run-time, which implementation of a function to call based upon the
# type of the object upon which it is invoked. This is in contrast to some languages
# that use static dispatching, making a compile-time decision as to which version of
# a function to call, based upon the declared type of a variable.

#  Shallow and Deep Copying

# In Chapter 1, we emphasized that an assignment statement foo = bar makes the
# name foo an alias for the object identified as bar. In this section, we consider
# the task of making a copy of an object, rather than an alias. This is necessary in
# applications when we want to subsequently modify either the original or the copy
# in an independent manner.

# Consider a scenario in which we manage various lists of colors, with each color
# represented by an instance of a presumed color class. We let identifier warmtones
# denote an existing list of such colors (e.g., oranges, browns). In this application,
# we wish to create a new list named palette, which is a copy of the warmtones list.
# However, we want to subsequently be able to add additional colors to palette, or
# to modify or remove some of the existing colors, without affecting the contents of
# warmtones. If we were to execute the command

palette = warmtones

#  No new list is created; instead, the new identifier palette references the original list.

#                           palette            warmtones
#                                  \          / 
#                                     list()
#                                     /    \
#                               color       color       
#                               red         red
#                               green       green
#                               blue        blue

# Unfortunately, this does not meet our desired criteria, because if we subsequently
# add or remove colors from “palette,” we modify the list identified as warmtones.

# We can instead create a new instance of the list class by using the syntax:

palette = list(warmtones)

# In this case, we explicitly call the list constructor, sending the first list as a parameter.
# This causes a new list to be created, as shown in Figure 2.10; however, it is
# what is known as a shallow copy. The new list is initialized so that its contents are
# precisely the same as the original sequence. However, Python’s lists are referential
# (see page 9 of Section 1.2.3), and so the new list represents a sequence of references
# to the same elements as in the first.

#                           palette            warmtones
#                                  \             / 
#                                  list()      list()
#                                  /    \    /  /
#                                 /      \  /  /
#                                /        \/  /
#                               /        / \ /
#                              /       /   /\
#                              /      /    / \
#                             color       color       
#                             red         red
#                             green       green
#                             blue        blue


# This is a better situation than our first attempt, as we can legitimately add
# or remove elements from palette without affecting warmtones. However, if we
# edit a color instance from the palette list, we effectively change the contents of
# warmtones. Although palette and warmtones are distinct lists, there remains indirect
# aliasing, for example, with palette[0] and warmtones[0] as aliases for the same
# color instance.

# We prefer that palette be what is known as a deep copy of warmtones. In a
# deep copy, the new copy references its own copies of those objects referenced by
# the original version. (See Figure 2.11.)


#                           palette                     warmtones
#                               \                          / 
#                               list()                   list()
#                               /    \                   /    \
#                          color       color         color       color
#                          red         red           red         red
#                          green       green         green       green
#                          blue        blue          blue        blue

# Python’s copy Module
# To create a deep copy, we could populate our list by explicitly making copies of
# the original color instances, but this requires that we know how to make copies of
# colors (rather than aliasing). Python provides a very convenient module, named
# copy, that can produce both shallow copies and deep copies of arbitrary objects.

# This module supports two functions: the copy function creates a shallow copy
# of its argument, and the deepcopy function creates a deep copy of its argument.
# After importing the module, we may create a deep copy for our example, as shown
# in Figure 2.11, using the command:

import copy

palette = copy.deepcopy(warmtones)
