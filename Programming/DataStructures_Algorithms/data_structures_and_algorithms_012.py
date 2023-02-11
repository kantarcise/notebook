# Design Patterns

# The algorithm design patterns we discuss include the following:
# • Recursion (Chapter 4)
# • Amortization (Sections 5.3 and 11.4)
# • Divide-and-conquer (Section 12.2.1)
# • Prune-and-search, also known as decrease-and-conquer (Section 12.7.1)
# • Brute force (Section 13.2.1)
# • Dynamic programming (Section 13.3).
# • The greedy method (Sections 13.4.2, 14.6.2, and 14.7)

# Likewise, the software engineering design patterns we discuss include:
# • Iterator (Sections 1.8 and 2.3.4)
# • Adapter (Section 6.1.2)
# • Position (Sections 7.4 and 8.1.2)
# • Composition (Sections 7.6.1, 9.2.1, and 10.1.4)
# • Template method (Sections 2.4.3, 8.4.6, 10.1.3, 10.5.2, and 11.2.1)
# • Locator (Section 9.5.1)
# • Factory method (Section 11.2.1)

# Development 

# Traditional software development involves several phases. Three major steps are:
# 1. Design
# 2. Implementation
# 3. Testing and Debugging
# In this section, we briefly discuss the role of these phases, and we introduce 
# several good practices for programming in Python, including coding style, naming
# conventions, formal documentation, and unit testing.

# For object-oriented programming, the design step is perhaps the most important
# phase in the process of developing software. For it is in the design step that we
# decide how to divide the workings of our program into classes, we decide how
# these classes will interact, what data each will store, and what actions each will
# perform. Indeed, one of the main challenges that beginning programmers face is
# deciding what classes to define to do the work of their program. While general
# prescriptions are hard to come by, there are some rules of thumb that we can apply
# when determining how to design our classes:

# • Responsibilities: Divide the work into different actors, each with a different
# responsibility. Try to describe responsibilities using action verbs. These
# actors will form the classes for the program.

# • Independence: Define the work for each class to be as independent from
# other classes as possible. Subdivide responsibilities between classes so that
# each class has autonomy over some aspect of the program. Give data (as instance
# variables) to the class that has jurisdiction over the actions that require
# access to this data.

# • Behaviors: Define the behaviors for each class carefully and precisely, so
# that the consequences of each action performed by a class will be well understood
# by other classes that interact with it. These behaviors will define
# the methods that this class performs, and the set of behaviors for a class are
# the interface to the class, as these form the means for other pieces of code to
# interact with objects from the class.

# Defining the classes, together with their instance variables and methods, are key
# to the design of an object-oriented program. A good programmer will naturally
# develop greater skill in performing these tasks over time, as experience teaches
# him or her to notice patterns in the requirements of a program that match patterns
# that he or she has seen before.

# Overloaded operations, implemented with Python’s special methods.

# Common Syntax                      Special Method Form

a + b                               # a.__add__(b); alternatively b.__radd__(a)
a − b                               # a.__sub__(b);  alternatively b.__rsub__(a)
a * b                               # a.__mul__(b);  alternatively b.__rmul__(a)
a/b                                 # a.__truediv__(b); alternatively b.__rtruediv__(a)
a // b                              # a.__floordiv__(b); alternatively b.__rfloordiv__(a)
a % b                               # a.__mod__(b); alternatively b.__rmod__(a)
a ** b                              # a.__pow__(b); alternatively b.__rpow__(a)
a << b                              # a.__lshift__(b); alternatively b.__rlshift__(a)
a >> b                              # a.__rshift__(b); alternatively b.__rrshift__(a)
a & b                               # a.__and__(b); alternatively b.__rand__(a)
a ˆ b                               # a.__xor__(b); alternatively b.__rxor__(a)
a | b                               # a.__or__(b); alternatively b.__ror__(a)
a += b                              # a.__iadd__(b)
a −= b                              # a.__isub__(b)
a =b                                # a.__imul__(b)
+a                                  # a.__pos__()
−a                                  # a.__neg__()
 ̃a                                  # a.__invert__()
abs(a)                              # a.__abs__()
a < b                               # a.__lt__(b)
a <= b                              # a.__le__(b)
a > b                               # a.__gt__(b)
a >= b                              # a.__ge__(b)
a == b                              # a.__eq__(b)
a != b                              # a.__ne__(b)
v in a                              # a.__contains__(v)
a[k]                                # a.__getitem__(k)
a[k] = v                            # a.__setitem__(k,v)
del a[k]                            # a.__delitem__(k)
a(arg1, arg2, ...)                  # a.__call__(arg1, arg2, ...)
len(a)                              # a.__len__()
hash(a)                             # a.__hash__()
iter(a)                             # a.__iter__()
next(a)                             # a.__next__()
bool(a)                             # a.__bool__()
float(a)                            # a.__float__()
int(a)                              # a.__int__()
repr(a)                             # a.__repr__()
reversed(a)                         # a.__reversed__()
str(a)                              # a.__str__()

# Implied Methods
# As a general rule, if a particular special method is not implemented in a user-defined
# class, the standard syntax that relies upon that method will raise an exception. For
# example, evaluating the expression, a + b, for instances of a user-defined class
# without add or radd will raise an error.


# For example, the bool method, which supports the syntax if foo:, has default semantics so that every object other than
# None is evaluated as True. However, for container types, the len method is
# typically defined to return the size of the container.

# Quick tip, identity vs equivalent
# if ids if the two objects are the same they are identical (a is b)
# if the values of two objects referring are the same they are equivalent (a == b)

num = 1
num_two = num
num == num_two
# True

list_one = [1, 2, 3]
list_two = [1, 2, 3]
list_one == list_two
# True

num is num_two
# True
list_one is list_two
# False

# We should caution that some natural implications are not automatically 
# provided by Python. For example, the eq method supports syntax a == b, but
# providing that method does not affect the evaluation of syntax a != b. (The __ne__ 
# method should be provided, typically returning not (a == b) as a result.) Similarly,
# providing a lt method supports syntax a < b, and indirectly b > a, but
# providing both lt and eq does not imply semantics for a <= b.

# Example Multi Dimensional Vector Class

# We are expected to do

v = Vector(5)             # construct five-dimensional <0, 0, 0, 0, 0>
v[1] = 23                 # <0, 23, 0, 0, 0> (based on use of setitem )
v[−1] = 45                # <0, 23, 0, 0, 45> (also via setitem )
print(v[4])               # print 45 (via getitem )
u = v + v                 # <0, 46, 0, 0, 90> (via add )
print(u)                  # print <0, 46, 0, 0, 90>
total = 0
for entry in v:          # implicit iteration via len and getitem
    total += entry

# We implement many of the behaviors by trivially invoking a similar behavior
# on the underlying list of coordinates. However, our implementation of add
# is customized. Assuming the two operands are vectors with the same length, this
# method creates a new vector and sets the coordinates of the new vector to be equal
# to the respective sum of the operands’ elements.

# automatically supports the syntax u = v + [5, 3, 10, −2, 1], resulting in a new
# vector that is the element-by-element “sum” of the first vector and the list instance.
# This is a result of Python’s polymorphism. Literally, “polymorphism”
# means “many forms.” Although it is tempting to think of the other parameter of our
# __add__ method as another Vector instance, we never declared it as such.

# Within the body, the only behaviors we rely on for parameter other is that it sup-
# ports len(other) and access to other[j]. Therefore, our code executes when the
# right-hand operand is a list of numbers (with matching length).

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d dimensional vector of zeros"""
        self._coords = [0] * d
  
    def __len__(self):
       """Returns the dimension if the vector"""
       return len(self._coords)

    def __getitem__(self, j):
        """Returns the jth coordinate of the vector"""
        return self._coords[j]
    
    def __setitem__(self, j, val):
        """Set the jth coordinate of the vector to given value"""
        self._coords[j] = val
    
    def __add__(self, other):
        """Returns sum of the two vectors"""
        if len(self) != len(other):
            raise ValueError("Dimensions must agree")
        result = Vector(len(self))
        
        for j in range(len(self) - 1):
            result[j] = self[j] + other[j]
        
        return result

    def __eq__(self, other):
        """Returns true if the vectors has the same coordinates"""
        return self._coords == other._coords

    def __ne__(self,other):
        """Returns True if Vectors differ from each other"""
        return not self == other                # Relying on existing eq definition

    def __str__(self) -> str:
        """Produce string representation of the vector"""
        return '<' + str(self._coords[1:-1]) + '>'          # adapt list representation

