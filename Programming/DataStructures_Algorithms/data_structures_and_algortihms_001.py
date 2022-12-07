# Python is formally an interpreted language. Commands are executed through a piece
#  of software known as the Python interpreter. The interpreter receives a command,
# evaluates that command, and reports the result of the command. While the
# interpreter can be used interactively (especially when debugging), a programmer
# typically defines a series of commands in advance and saves those commands in a
# plain text file known as source code or a script.

# Python is an object-oriented language and classes form the basis for all data types.
# In this section, we describe key aspects of Python’s object model, and we introduce
# Python’s built-in classes, such as the int class for integers, the float class
# for floating-point values, and the str class for character strings.

# There are 33 specially reserved words that cannot be used as identifiers, as shown down below.

#             Reserved Words
# False as continue else from in not return yield
# None assert def except global is or try
# True break del finally if lambda pass while
# and class elif for import nonlocal raise with

# Thank you for that reminder.

# Python’s Built-In Classes

# A class is immutable if each object of that class has a fixed value upon instantiation that
# cannot subsequently be changed. For example, the float class is immutable. Once
# an instance has been created, its value cannot be changed (although an identifier
# referencing that object can be reassigned to a different value)

# Class     Description                               Immutable?
# bool      Boolean value                                 +
# int       integer (arbitrary magnitude)                 +
# float     floating-point number                         +
# list      mutable sequence of objects 
# tuple     immutable sequence of objects                 +
# str       character string                              +
# set       unordered set of distinct objects
# frozenset immutable form of set class                   +
# dict      associative mapping (aka dictionary)

# The bool class

# Numbers evaluate to False if zero, and True if nonzero.
# Sequences and other container types, such as strings and lists,
# evaluate to False if empty and True if nonempty. An important application of this
# interpretation is the use of a nonboolean value as a condition in a control structure.

# Boolean is a SUBTYPE of the integer type!

# The int class

# The int and float classes are the primary numeric types in Python. The int class is
# designed to represent integer values with arbitrary magnitude. Unlike Java and
# C++, which support different integral types with different precisions (e.g., int,
# short, long), Python automatically chooses the internal representation for an in-
# teger based upon the magnitude of its value. 

# Typical literals for integers include 0, 137, and −23. In some contexts, it is convenient to express an integral value using
# binary, octal, or hexadecimal. That can be done by using a prefix of the number 0
# and then a character to describe the base. Example of such literals are respectively
# 0b1011, 0o52, and 0x7f.

test_integer = 23
another_test_integer = 0x7f


# The integer constructor, int( ), returns value 0 by default. But this constructor
# can be used to construct an integer value based upon an existing value of another
# type. For example, if f represents a floating-point value, the syntax int(f) produces
# the truncated value of f. For example, both int(3.14) and int(3.99) produce the
# value 3, while int(−3.9) produces the value −3.


int(3.99)
# 3

int(-2.4)
# 2

# The constructor can also be used to parse a string that is presumed to
# represent an integral value (such as one entered by a user).
# If s represents a string, then int(s) produces the integral value
# that string represents. For example, the expression int( 137 ) produces the inte-
# ger value 137. If an invalid string is given as a parameter, as in int( hello ), a
# ValueError is raised. By default, the string must use base 10. If conversion from a different base is desired, that
# base can be indicated as a second, optional, parameter. For example, the expression
# int( 7f , 16) evaluates to the integer 127.

# The float Class

# The float class is the sole floating-point type in Python, using a fixed-precision
# representation. Its precision is more akin to a double in Java or C++, rather than
# those languages’ float type. We have already discussed a typical literal form, 98.6.
# We note that the floating-point equivalent of an integral number can be expressed
# directly as 2.0. Technically, the trailing zero is optional, so some programmers
# might use the expression 2. to designate this floating-point literal. One other form
# of literal for floating-point values uses scientific notation. For example, the literal
# 6.022e23 represents the mathematical value 6.022 × 1023 .

# The constructor form of float( ) returns 0.0. When given a parameter, the constructor
# attempts to return the equivalent floating-point value. For example, the call
# float(2) returns the floating-point value 2.0. If the parameter to the constructor is
# a string, as with float( 3.14 ), it attempts to parse that string as a floating-point
# value, raising a ValueError as an exception.
