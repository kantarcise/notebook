# Abstract Base Classes Keep Inheritance in Check

# Abstract Base Classes (ABCs) ensure that derived classes implement
# particular methods from the base class. In this chapter you’ll learn
# about the benefits of abstract base classes and how to define them
# with Python’s built-in abc module.

#  So what are Abstract Base Classes good for? 
  
#   A while ago I had a discussion at work about which pattern to use for implementing a 
#   maintainable class hierarchy in Python. 
  
#   More specifically, the goal was
#   to define a simple class hierarchy for a service backend in the most
#   programmer-friendly and maintainable way.


# We had a BaseService class that defined a common interface and several
# concrete implementations. The concrete implementations do different 
# things but all of them provide the same interface (MockService,RealService, and so on). 
# To make this relationship explicit, the concrete implementations all subclass BaseService.

# To make this code as maintainable and programmer-friendly as possible we wanted to make sure that:
# • instantiating the base class is impossible; and
# • forgetting to implement interface methods in one of the subclasses raises an error as early as possible.

# Now why would you want to use Python’s abc module to solve this problem? The above 
# design is pretty common in more complex systems. To enforce
# that a derived class implements a number of methods from the base 
# class, something like this Python idiom is typically used:

class Base:
    def foo(self):
        raise NotImplementedError()
    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return 'foo() called'

    # Oh no, we forgot to override bar()...
    # def bar(self):
    # return "bar() called"

# So, what do we get from this first attempt at solving the problem?
# Calling methods on an instance of Base correctly raises NotImplementedError exceptions:

b = Base()
b.foo()

# NotImplementedError
# Furthermore, instantiating and using Concrete works as expected.
# And, if we call an unimplemented method like bar() on it, this also raises an exception:

c = Concrete()
c.foo()
# 'foo() called'
c.bar()
# NotImplementedError

# This is something but not perfect.
# Problems still:

# • We can instantiate Base just fine without getting an error.
# • provide incomplete subclasses—instantiating Concrete will not raise an error
# until we call the missing method bar().

# ABC module to the rescue.

from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass
    
    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass
    # We forget to declare bar() again...

# This still behaves as expected and creates the correct class hierarchy.

assert issubclass(Concrete, Base)
# This will pass.

# But now!

c = Concrete()
# TypeError:
# "Can't instantiate abstract class Concrete
# with abstract methods bar"


