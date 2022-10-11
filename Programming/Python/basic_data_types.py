# You know the drill, download and install anaconda to be a tidy programmer.
# Python 3.8.8 or the latest works fine.

# This script is all about datatypes and built-in functions.

# Each time to assign a value to a python variable, the interpreter keeps a track of it
# and type is inferred from its value like quotes for string, decimal and integer values

# In Python 3, there is effectively no limit to how long an integer value can be.

decimal_int = 234123541234512534139847598012374587012903742134

# we can use binary, octal or decimal. All of them are integers for type() function.

# 0b (zero + lowercase letter 'b')	Binary 	2
# 0o (zero + lowercase letter 'o') Octal 	8
# 0x (zero + lowercase letter 'x') 	Hexadecimal 	16 	

binary_int =  0b10
octal_int = 0o10
hexadecimal_int = 0x1C

small_one = 3.2e-12

# Floats

float_zet = 4.2

complex_number = 2 + 3j

# Strings

string = "This is a string"
string_second = 'This also is a string'

# Suppressing Special Character

special_character_included = 'This has a special\' character in it.'

# Escape sequences

# \n \t \b

# Ignore Escape Sequences - start with r

`print(r"Hello\nWorld")`

# Booleans 

bool_first = True
bool_second = False


# Here is some of most used built in functions:

# Math

# abs() 	Returns absolute value of a number
# divmod() 	Returns quotient and remainder of integer division
# max() 	Returns the largest of the given arguments or items in an iterable
# min() 	Returns the smallest of the given arguments or items in an iterable
# pow() 	Raises a number to a power
# round() 	Rounds a floating-point value
# sum() 	Sums the items of an iterable

# Type Conversion

# ascii() 	Returns a string containing a printable representation of an object
# bin() 	Converts an integer to a binary string
# bool() 	Converts an argument to a Boolean value
# chr() 	Returns string representation of character given by integer argument
# complex() 	Returns a complex number constructed from arguments
# float() 	Returns a floating-point object constructed from a number or string
# hex() 	Converts an integer to a hexadecimal string
# int() 	Returns an integer object constructed from a number or string
# oct() 	Converts an integer to an octal string
# ord() 	Returns integer representation of a character
# repr() 	Returns a string containing a printable representation of an object
# str() 	Returns a string version of an object
# type() 	Returns the type of an object or creates a new type object

# Iterables and Iterators

# all() 	Returns True if all elements of an iterable are true
# any() 	Returns True if any elements of an iterable are true
# enumerate() 	Returns a list of tuples containing indices and values from an iterable
# filter() 	Filters elements from an iterable
# iter() 	Returns an iterator object
# len() 	Returns the length of an object
# map() 	Applies a function to every item of an iterable
# next() 	Retrieves the next item from an iterator
# range() 	Generates a range of integer values
# reversed() 	Returns a reverse iterator
# slice() 	Returns a slice object
# sorted() 	Returns a sorted list from an iterable
# zip() 	Creates an iterator that aggregates elements from iterables

# Composite Data Type

# bytearray() 	Creates and returns an object of the bytearray class
# bytes() 	Creates and returns a bytes object (similar to bytearray, but immutable)
# dict() 	Creates a dict object
# frozenset() 	Creates a frozenset object
# list() 	Creates a list object
# object() 	Creates a new featureless object
# set() 	Creates a set object
# tuple() 	Creates a tuple object

# Classes, Attributes, and Inheritance

# classmethod() 	Returns a class method for a function
# delattr() 	Deletes an attribute from an object
# getattr() 	Returns the value of a named attribute of an object
# hasattr() 	Returns True if an object has a given attribute
# isinstance() 	Determines whether an object is an instance of a given class
# issubclass() 	Determines whether a class is a subclass of a given class
# property() 	Returns a property value of a class
# setattr() 	Sets the value of a named attribute of an object
# super() 	Returns a proxy object that delegates method calls to a parent or sibling class

# Input/Output

# format() 	Converts a value to a formatted representation
# input() 	Reads input from the console
# open() 	Opens a file and returns a file object
# print() 	Prints to a text stream or the console

# Variables, References, and Scope

# dir() 	Returns a list of names in current local scope or a list of object attributes
# globals() 	Returns a dictionary representing the current global symbol table
# id() 	Returns the identity of an object
# locals() 	Updates and returns a dictionary representing current local symbol table
# vars() 	Returns __dict__ attribute for a module, class, or object

# Miscellaneous

# callable() 	Returns True if object appears callable
# compile() 	Compiles source into a code or AST object
# eval() 	Evaluates a Python expression
# exec() 	Implements dynamic execution of Python code
# hash() 	Returns the hash value of an object
# help() 	Invokes the built-in help system
# memoryview() 	Returns a memory view object
# staticmethod() 	Returns a static method for a function
# __import__() 	Invoked by the import statement
