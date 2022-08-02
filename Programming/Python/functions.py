# How functions work in Python and why they’re beneficial
# How to define and call your own Python function
# Mechanisms for passing arguments to your function
# How to return data from your function back to the calling environment

# Here is a unusual intro:

# In life, you do this sort of thing all the time, even if you don’t explicitly think of it that way. If you wanted to move 
# some shelves full of stuff from one side of your garage to the other, then you 
# hopefully wouldn’t just stand there and aimlessly think, 
# “Oh, geez. I need to move all that stuff over there! How do I do that???”
# You’d divide the job into manageable steps:

#     Take all the stuff off the shelves.
#     Take the shelves apart.
#    Carry the shelf parts across the garage to the new location.
#     Re-assemble the shelves.
#     Carry the stuff across the garage.
#     Put the stuff back on the shelves.

# Breaking a large task into smaller, bite-sized sub-tasks helps 
# make the large task easier to think about and manage. As programs become more 
# complicated, it becomes increasingly beneficial to modularize them in this way.



# The usual syntax for defining a Python function is as follows:

# def <function_name>([<parameters>]):
#     <statement(s)>

# Positional Arguments
  
# The most straightforward way to pass arguments to a Python function is with
# positional arguments (also called required arguments). In the
# function definition, you specify a comma-separated list of parameters inside the parentheses:

def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')

# When the function is called, you specify a corresponding list of arguments:

f(6, 'bananas', 1.74)
# 6 bananas cost $1.74

# Using keyword arguments lifts the restriction on argument order.

f(item='bananas', price=1.74, qty=6)
# 6 bananas cost $1.74

# You can give default paramaters aswell.

def f(qty=6, item='bananas', price=1.74):
    print(f'{qty} {item} cost ${price:.2f}')

  
# In summary:

#  Positional arguments must agree in order and number with the parameters declared in the function definition.
#  Keyword arguments must agree with declared parameters in number, but they may be specified in arbitrary order.
#  Default parameters allow some arguments to be omitted when the function is called.



# Argument Passing Summary

# Python’s argument-passing mechanism has been called pass-by-assignment. 

# Passing an immutable object, like an int, str, tuple, or frozenset, to 
# a Python function acts like pass-by-value. The function can’t modify the object in the calling environment.



def f(fx):
    print('fx =', fx, '/ id(fx) = ', id(fx))
    fx = 10
    print('fx =', fx, '/ id(fx) = ', id(fx))

x = 5
print('x =', x, '/ id(x) = ', id(x))
# x = 5 / id(x) =  1357924048

f(x)

# fx = 5 / id(fx) =  1357924048
# fx = 10 / id(fx) =  1357924128

print('x =', x, '/ id(x) = ', id(x))
# x = 5 / id(x) =  1357924048


# Passing a mutable object such as a list, dict, or set acts somewhat—but not exactly—like pass-by-reference. The
# function can’t reassign the object wholesale, but it can change items in place within the object, and
# these changes will be reflected in the calling environment.

def f(x):
    x[0] = '---'

my_list = ['foo', 'bar', 'baz', 'qux']

f(my_list)
my_list
# ['---', 'bar', 'baz', 'qux']


# The return Statement

# A return statement in a Python function serves two purposes:
#  It immediately terminates the function and passes execution control back to the caller.
#  It provides a mechanism by which the function can pass data back to the caller.


# You can return a function at any time:

# This sort of paradigm can be useful for error checking in a function.
# You can check several error conditions at the start of the function, with return statements
# that bail out if there’s a problem:

def f():
    if error_cond1:
        return
    if error_cond2:
        return
    if error_cond3:
        return

    <normal processing>

# A function can return any type of object. In Python, that means pretty much anything whatsoever. 

def double_list(x):
    r = []
    for i in x:
        r.append(i * 2)
    return r

a = [1, 2, 3, 4, 5]
double_list(a)
a
# [2, 4, 6, 8, 10]

# Variable-Length Argument Lists

# In some cases, when you’re defining a function, you may not know beforehand how many arguments you’ll want it to take.

# For example, how would you describe an average function. Whwat kind of arguments does it take, how many of them?

def avg(a, b, c):
    return (a + b + c) / 3

# LOL NO, this will not work for obvious reasons.

# To save us, Python provides a way to pass a function a
# variable number of arguments with argument tuple packing and unpacking using the asterisk (*) operator.

# Makes everything in a Tuple.

def f(*args):
    print(args)
    print(type(args), len(args))
    for x in args:
            print(x)

f(1, 2, 3)
# (1, 2, 3)        
# <class 'tuple'> 3
# 1
# 2
# 3

f('foo', 'bar', 'baz', 'qux', 'quux')
# ('foo', 'bar', 'baz', 'qux', 'quux')
# <class 'tuple'> 5
# foo
# bar
# baz
# qux
# quux

# Now we can write the average function as:

def avg (*args):
    sum = 0
    for i in args:
        sum +=i
    return sum / len(args)
  
# Or:

def avg(*args):
    return sum(args) / len(args)

# Still, depending on how this code will be used, there may still be work to do. 
# As written, avg() will produce a TypeError exception if any arguments are non-numeric:

avg(1, 'foo', 3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in avg
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# To be as robust as possible, you should add code to check that the arguments are of the proper type. 
# Later in this tutorial series, you’ll learn how to catch exceptions like TypeError and handle them appropriately.


# Argument Tuple Unpacking

# An analogous operation is available on the other side of the equation in a Python function call. 
# When an argument in a function call is preceded by an asterisk (*), it indicates that the argument
# is a tuple that should be unpacked and passed to the function as separate values:

def f(x, y, z):
    print(f'x = {x}')
    print(f'y = {y}')
    print(f'z = {z}')

f(1, 2, 3)
# x = 1
# y = 2
# z = 3

t = ('foo', 'bar', 'baz')
f(*t)
# x = foo
# y = bar
# z = baz

# Here, f(*a) indicates that list a should be unpacked
# and the items passed to f() as individual values. The parameter
# specification *args causes the values to be packed back up into the tuple args.

# Argument Dictionary Packing

def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, val in kwargs.items():
            print(key, '->', val)

f(foo=1, bar=2, baz=3)
# {'foo': 1, 'bar': 2, 'baz': 3}
# <class 'dict'>
# foo -> 1
# bar -> 2
# baz -> 3

# In this case, the arguments foo=1, bar=2, and baz=3 are packed into 
# a dictionary that the function can reference by the name kwargs. 


