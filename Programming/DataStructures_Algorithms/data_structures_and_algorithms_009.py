# Packing and Unpacking of Sequences

# Python provides two additional conveniences involving the treatment of tuples and
# other sequence types. The first is rather cosmetic. If a series of comma-separated
# expressions are given in a larger context, they will be treated as a single tuple, even
# if no enclosing parentheses are provided. For example, the assignment

data = 2, 4, 6, 8

# results in identifier, data, being assigned to the tuple (2, 4, 6, 8). This behavior
# is called automatic packing of a tuple. One common use of packing in Python is
# when returning multiple values from a function. If the body of a function executes
# the command,

return x, y

# it will be formally returning a single object that is the tuple (x, y).

# As a dual to the packing behavior, Python can automatically unpack a sequence, allowing 
# one to assign a series of individual identifiers to the elements of sequence. As an example, we can write

a, b, c, d = range(7, 11)

# which has the effect of assigning a=7, b=8, c=9, and d=10, as those are the four
# values in the sequence returned by the call to range. For this syntax, the right-hand
# side expression can be any iterable type, as long as the number of variables on the
# left-hand side is the same as the number of elements in the iteration.

# This technique can be used to unpack tuples returned by a function. For example,
# the built-in function, divmod(a, b), returns the pair of values (a // b, a % b)
# associated with an integer division. Although the caller can consider the return
# value to be a single tuple, it is possible to write

quotient, remainder = divmod(a, b)

# to separately identify the two entries of the returned tuple. This syntax can also be
# used in the context of a for loop, when iterating over a sequence of iterables, as in

for x, y in [ (7, 2), (5, 8), (6, 4) ]:

# In this example, there will be three iterations of the loop. During the first pass, x=7
# and y=2, and so on. This style of loop is quite commonly used to iterate through
# key-value pairs that are returned by the items( ) method of the dict class, as in:

for k, v in mapping.items():
  
# Simultaneous Assignments

# The combination of automatic packing and unpacking forms a technique known
# as simultaneous assignment, whereby we explicitly assign a series of values to a
# series of identifiers, using a syntax:

x, y, z = 6, 2, 5

# In effect, the right-hand side of this assignment is automatically packed into a tuple,
# and then automatically unpacked with its elements assigned to the three identifiers
# on the left-hand side.

# When using a simultaneous assignment, all of the expressions are evaluated
# on the right-hand side before any of the assignments are made to the left-hand
# variables. This is significant, as it provides a convenient means for swapping the
# values associated with two variables:

j, k = k, j

# With this command, j will be assigned to the old value of k, and k will be assigned
# to the old value of j. Without simultaneous assignment, a swap typically requires
# more delicate use of a temporary variable, such as

temp = j
j = k
k = temp

# With the simultaneous assignment, the unnamed tuple representing the packed values
# on the right-hand side implicitly serves as the temporary variable when performing such a swap.

# The use of simultaneous assignments can greatly simplify the presentation of
# code. As an example, we reconsider the generator on page 41 that produces the
# Fibonacci series. The original code requires separate initialization of variables a
# and b to begin the series. Within each pass of the loop, the goal was to reassign a
# and b, respectively, to the values of b and a+b. At the time, we accomplished this
# with brief use of a third variable. With simultaneous assignments, that generator
# can be implemented more directly as follows:

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a+b
