# Exception Handling

# Exceptions are unexpected events that occur during the execution of a program.
# An exception might result from a logical error or an unanticipated situation. In
# Python, exceptions (also known as errors) are objects that are raised (or thrown) by
# code that encounters an unexpected circumstance. The Python interpreter can also
# raise an exception should it encounter an unexpected condition, like running out of
# memory. A raised error may be caught by a surrounding context that “handles” the
# exception in an appropriate fashion. If uncaught, an exception causes the interpreter
# to stop executing the program and to report an appropriate message to the console.
# In this section, we examine the most common error types in Python, the mechanism
# for catching and handling errors that have been raised, and the syntax for raising
# errors from within user-defined blocks of code.

# Class             Description
Exception # A base class for most error types
AttributeError # Raised by syntax obj.foo, if obj has no member named foo
EOFError # Raised if “end of file” reached for console or file input
IOError # Raised upon failure of I/O operation (e.g., opening file)
IndexError # Raised if index to sequence is out of bounds
KeyError # Raised if nonexistent key requested for set or dictionary
KeyboardInterrupt # Raised if user types ctrl-C while program is executing
NameError # Raised if nonexistent identifier used
StopIteration # Raised by next(iterator) if no element; see Section 1.8
TypeError # Raised when wrong type of parameter is sent to a function
ValueError # Raised when parameter has invalid value (e.g., sqrt(−5))
ZeroDivisionError #  Raised when any division operator used with 0 as divisor

# An exception is thrown by executing the raise statement, with an appropriate 
# instance of an exception class as an argument that designates the problem

def sum(values):
    if not isinstance(values, collections.Iterable):
        raise TypeError( parameter must be an iterable type )
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError( elements must be numeric )
        total = total+ v
    return total
  
# TWO WAYS TO GO ABOUT EXCEPTIONS 

# ONe philosophy for managing exceptional cases is to “look before you leap.”
# The goal is to entirely avoid the possibility of an exception being raised through
# the use of a proactive conditional test. Revisiting our division example, we might
# avoid the offending situation by writing:

if y != 0:
    ratio = x / y
else:
    # ... do something else ... 


# A philosophy, often embraced by Python programmers, is that “it is
# easier to ask for forgiveness than it is to get permission.” This quote is attributed
# to Grace Hopper, an early pioneer in computer science. The sentiment is that we
# need not spend extra execution time safeguarding against every possible exceptional
# case, as long as there is a mechanism for coping with a problem after it
# arises. In Python, this philosophy is implemented using a try-except control structure.
# Revising our first example, the division operation can be guarded as follows:

try:
    ratio = x / y
except ZeroDivisionError:
    # ... do something else ...
    
# The relative advantage of using a try-except structure is that the non-exceptional
# case runs efficiently, without extraneous checks for the exceptional condition. However,
# handling the exceptional case requires slightly more time when using a try-
# except structure than with a standard conditional statement. For this reason, the
# try-except clause is best used when there is reason to believe that the exceptional
# case is relatively unlikely, or when it is prohibitively expensive to proactively evaluate
# a condition to avoid the exception.

# You can catch none or more Exceptions in the same block:

age = −1 # an initially invalid choice
while age <= 0:
    try:
        age = int(input( Enter your age in years: ))
        if age <= 0:
            print( Your age must be positive )
    except (ValueError, EOFError):
        print( Invalid response )


# In closing, we note two additional features of try-except structures in Python.
# It is permissible to have a final except-clause without any identified error types,
# using syntax except:, to catch any other exceptions that occurred. However, this
# technique should be used sparingly, as it is difficult to suggest how to handle an
# error of an unknown type. A try-statement can have a finally clause, with a body of
# code that will always be executed in the standard or exceptional cases, even when
# an uncaught or re-raised exception occurs. That block is typically used for critical
# cleanup work, such as closing an open file.
