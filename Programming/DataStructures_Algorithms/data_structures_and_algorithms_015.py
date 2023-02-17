# Abstract Base Classes

# When defining a group of classes as part of an inheritance hierarchy, one technique
# for avoiding repetition of code is to design a base class with common functionality
# that can be inherited by other classes that need it. As an example, the hierarchy
# from Section 2.4.2 includes a Progression class, which serves as a base
# class for three distinct subclasses: ArithmeticProgression, GeometricProgression,
# and FibonacciProgression. Although it is possible to create an instance of the
# Progression base class, there is little value in doing so because its behavior is simply
# a special case of an ArithmeticProgression with increment 1. The real purpose
# of the Progression class was to centralize the implementations of behaviors that
# other progressions needed, thereby streamlining the code that is relegated to those
# subclasses.

# In classic object-oriented terminology, we say a class is an abstract base class
# if its only purpose is to serve as a base class through inheritance. More formally,
# an abstract base class is one that cannot be directly instantiated, while a concrete
# class is one that can be instantiated. By this definition, our Progression class is
# technically concrete, although we essentially designed it as an abstract base class.

# In statically typed languages such as Java and C++, an abstract base class serves
# as a formal type that may guarantee one or more abstract methods. This provides
# support for polymorphism, as a variable may have an abstract base class as its declared type, even 
# though it refers to an instance of a concrete subclass. Because
# there are no declared types in Python, this kind of polymorphism can be accomplished without the 
# need for a unifying abstract base class. For this reason, there
# is not as strong a tradition of defining abstract base classes in Python, although
# Python’s abc module provides support for defining a formal abstract base class.

# Our reason for focusing on abstract base classes in our study of data structures
# is that Python’s collections module provides several abstract base classes that assist
# when defining custom data structures that share a common interface with some of
# Python’s built-in data structures. These rely on an object-oriented software design
# pattern known as the template method pattern. The template method pattern is
# when an abstract base class provides concrete behaviors that rely upon calls to
# other abstract behaviors. In that way, as soon as a subclass provides definitions for
# the missing abstract behaviors, the inherited concrete behaviors are well defined.

# As a tangible example, the collections.Sequence abstract base class defines behaviors common to Python’s list, str, and tuple classes, as
# sequences that support element access via an integer index. More so, the collections.Sequence class
# provides concrete implementations of methods, count, index, and contains
# that can be inherited by any class that provides concrete implementations of both
# len and getitem . Lets write a Sequence abc.


from abc import ABCMeta, abstractmethod
# need these definitions
class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""
    
    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""
    
    def __contains__(self, val):
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:                              # found match 
                return True
        return False
    
    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val:                              # leftmost match
                return j
        raise ValueError( "Value not in sequence" )        # never found a match
    
    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:                              #found a match
                k += 1
        return k

# This implementation relies on two advanced Python techniques. The first is that
# we declare the ABCMeta class of the abc module as a metaclass of our Sequence
# class. A metaclass is different from a superclass, in that it provides a template for
# the class definition itself. Specifically, the ABCMeta declaration assures that the
# constructor for the class raises an error.

# The second advanced technique is the use of the @abstractmethod decorator
# immediately before the len and getitem methods are declared. That declares
# these two particular methods to be abstract, meaning that we do not provide
# an implementation within our Sequence base class, but that we expect any concrete
# subclasses to support those two methods. Python enforces this expectation, by disallowing
# instantiation for any subclass that does not override the abstract methods with concrete implementations.

