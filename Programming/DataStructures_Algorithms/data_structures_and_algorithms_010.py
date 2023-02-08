# Scopes and Namespaces

# When computing a sum with the syntax x + y in Python, the names x and y must
# have been previously associated with objects that serve as values; a NameError
# will be raised if no such definitions are found. The process of determining the
# value associated with an identifier is known as name resolution.

# Whenever an identifier is assigned to a value, that definition is made with a
# specific scope. Top-level assignments are typically made in what is known as global
# scope. Assignments made within the body of a function typically have scope that is
# local to that function call. Therefore, an assignment, x = 5, within a function has
# no effect on the identifier, x, in the broader scope.

# Each distinct scope in Python is represented using an abstraction known as a
# namespace. A namespace manages all identifiers that are currently defined in a
# given scope. 

# Python implements a namespace with its own dictionary that maps each identifying
# string (e.g., n ) to its associated value. Python provides several ways to
# examine a given namespace. The function, dir, reports the names of the identifiers
# in a given namespace (i.e., the keys of the dictionary), while the function, vars,
# returns the full dictionary. By default, calls to dir( ) and vars( ) report on the most
# locally enclosing namespace in which they are executed.

# When an identifier is indicated in a command, Python searches a series of
# namespaces in the process of name resolution. First, the most locally enclosing
# scope is searched for a given name. If not found there, the next outer scope is
# searched, and so on. We will see that each object has its own namespace to store
# its attributes, and that classes each have a namespace as well.

# First-Class Objects

# In the terminology of programming languages, first-class objects are instances of
# a type that can be assigned to an identifier, passed as a parameter, or returned by
# a function. All of the data types we introduced in Section 1.2.3, such as int and
# list, are clearly first-class types in Python. In Python, functions and classes are also
# treated as first-class objects. For example, we could write the following:

scream = print # assign name ’scream’ to the function denoted as ’print’
scream( Hello ) # call that function

# In this case, we have not created a new function, we have simply defined scream
# as an alias for the existing print function. While there is little motivation for precisely
# this example, it demonstrates the mechanism that is used by Python to allow
# one function to be passed as a parameter to another. On page 28, we noted
# that the built-in function, max, accepts an optional keyword parameter to specify
# a non-default order when computing a maximum. For example, a caller can use
# the syntax, max(a, b, key=abs), to determine which value has the larger absolute
# value. Within the body of that function, the formal parameter, key, is an identifier
# that will be assigned to the actual parameter, abs.

# In terms of namespaces, an assignment such as scream = print, introduces the
# identifier, scream, into the current namespace, with its value being the object that
# represents the built-in function, print. The same mechanism is applied when a user-
# defined function is declared. For example, our count function from Section 1.5
# beings with the following syntax:

def count(data, target):
    # ...
    pass

# Such a declaration introduces the identifier, count, into the current namespace,
# with the value being a function instance representing its implementation. In similar
# fashion, the name of a newly defined class is associated with a representation of
# that class as its value. (Class definitions will be introduced in the next chapter.)

# Modules and the Import Statement

# We have already introduced many functions (e.g., max) and classes (e.g., list)
# that are defined within Python’s built-in namespace. Depending on the version of
# Python, there are approximately 130–150 definitions that were deemed significant
# enough to be included in that built-in namespace.

# Beyond the built-in definitions, the standard Python distribution includes perhaps
# tens of thousands of other values, functions, and classes that are organized in
# additional libraries, known as modules, that can be imported from within a program.
# As an example, we consider the math module. While the built-in namespace
# includes a few mathematical functions (e.g., abs, min, max, round), many more
# are relegated to the math module (e.g., sin, cos, sqrt). That module also defines
# approximate values for the mathematical constants, pi and e.
# Python’s import statement loads definitions from a module into the current
# namespace. One form of an import statement uses a syntax such as the following:

from math import pi, sqrt

# This command adds both pi and sqrt, as defined in the math module, into the 
# current namespace, allowing direct use of the identifier, pi, or a call of the function,
# sqrt(2). If there are many definitions from the same module to be imported, an
# asterisk may be used as a wild card, as in, from math import , but this form
# should be used sparingly. The danger is that some of the names defined in the module
# may conflict with names already in the current namespace (or being imported
# from another module), and the import causes the new definitions to replace existing ones.

# Another approach that can be used to access many definitions from the same
# module is to import the module itself, using a syntax such as:

import math

# Formally, this adds the identifier, math, to the current namespace, with the module
# as its value. (Modules are also first-class objects in Python.) Once imported, individual
# definitions from the module can be accessed using a fully-qualified name,
# such as math.pi or math.sqrt(2).

# Creating a New Module

# To create a new module, one simply has to put the relevant definitions in a file
# named with a .py suffix. Those definitions can be imported from any other .py
# file within the same project directory. For example, if we were to put the definition
# of our count function (see Section 1.5) into a file named utility.py, we could
# import that function using the syntax, from utility import count.

# It is worth noting that top-level commands with the module source code are
# executed when the module is first imported, almost as if the module were its own
# script. There is a special construct for embedding commands within the module
# that will be executed if the module is directly invoked as a script, but not when
# the module is imported from another script. Such commands should be placed in a
# body of a conditional statement of the following form,

if name == __main__ :

# Using our hypothetical utility.py module as an example, such commands will
# be executed if the interpreter is started with a command python utility.py, but
# not when the utility module is imported into another context. This approach is often
# used to embed what are known as unit tests within the module; we will discuss unit
# testing further in Section 2.2.4

# Existing Modules

# Table 1.7 provides a summary of a few available modules that are relevant to a
# study of data structures. We have already discussed the math module briefly. In the
# remainder of this section, we highlight another module that is particularly important
# for some of the data structures and algorithms that we will study later in this book.

Existing Modules       # Module Name Description
array                  # Provides compact array storage for primitive types.
collections            # Defines additional data structures and abstract base classes involving collections of objects.
copy                   # Defines general functions for making copies of objects.
heapq                  # Provides heap-based priority queue functions (see Section 9.3.7).
math                   # Defines common mathematical constants and functions.
os                     # Provides support for interactions with the operating system.
random                 # Provides random number generation.
re                     # Provides support for processing regular expressions.
sys                    # Provides additional level of interaction with the Python interpreter.
time                   # Provides support for measuring time, or delaying a program.

# Pseudo-Random Number Generation

# Python’s random module provides the ability to generate pseudo-random numbers,
# that is, numbers that are statistically random (but not necessarily truly random).
# A pseudo-random number generator uses a deterministic formula to generate the
# next number in a sequence based upon one or more past numbers that it has generated.
# Indeed, a simple yet popular pseudo-random number generator chooses its
# next number based solely on the most recently chosen number and some additional
# parameters using the following formula.

next = (a*current + b) % n;

# where a, b, and n are appropriately chosen integers. Python uses a more advanced
# technique known as a Mersenne twister. It turns out that the sequences generated
# by these techniques can be proven to be statistically uniform, which is usually
# good enough for most applications requiring random numbers, such as games. For
# applications, such as computer security settings, where one needs unpredictable
# random sequences, this kind of formula should not be used. Instead, one should
# ideally sample from a source that is actually random, such as radio static coming
# from outer space.

# Since the next number in a pseudo-random generator is determined by the previous
# number(s), such a generator always needs a place to start, which is called its
# seed. The sequence of numbers generated for a given seed will always be the same.
# One common trick to get a different sequence each time a program is run is to use
# a seed that will be different for each run. For example, we could use some timed
# input from a user or the current system time in milliseconds.

# Python’s random module provides support for pseudo-random number generation
# by defining a Random class; instances of that class serve as generators with
# independent state. This allows different aspects of a program to rely on their own
# pseudo-random number generator, so that calls to one generator do not affect the
# sequence of numbers produced by another. For convenience, all of the methods
# supported by the Random class are also supported as stand-alone functions of the
# random module (essentially using a single generator instance for all top-level calls).

Syntax                             # Description
seed(hashable)                     # Initializes the pseudo-random number generator based upon the hash value of the parameter
random( )                          # Returns a pseudo-random floating-point value in the interval [0.0, 1.0).
randint(a,b)                       # Returns a pseudo-random integer in the closed interval [a, b].
randrange(start, stop, step)       # Returns a pseudo-random integer in the standard Python range indicated by the parameters.
choice(seq)                        # Returns an element of the given sequence chosen pseudo-randomly.
shuffle(seq)                       # Reorders the elements of the given sequence pseudo-randomly.
Table 1.8: Methods supported by instances of the Random class, and as top-level functions of the random module.
