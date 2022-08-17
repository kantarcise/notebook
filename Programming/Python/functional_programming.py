# What the functional programming paradigm entails
# What it means to say that functions are first-class citizens in Python
# How to define anonymous functions with the lambda keyword
# How to implement functional code using map(), filter(), and reduce()

# --------------------------------------------------------------------------------------------------------------

# To support functional programming, it’s useful if a function in a given programming language has two abilities:

#    To take another function as an argument
#    To return another function to its caller

# Python plays nicely in both these respects.

def func():
    print("I am function func()!")

print("cat", func, 42)
# cat <function func at 0x7f81b4d29bf8> 42

objects = ["cat", func, 42]
objects[1]
# <function func at 0x7f81b4d29bf8>
objects[1]()
# I am function func()!

d = {"cat": 1, func: 2, 42: 3}
d[func]
# 2

# You can pass a function to another function as an argument:

def inner():
    print("I am function inner()!")

def outer(function):
    function()

outer(inner)
# I am function inner()!

# Technical note: Python provides a shortcut notation called a "decorator" to facilitate wrapping one function inside another.

# A callback function

# When you pass a function to another function, the passed-in function sometimes is 
# referred to as a callback because a call back to the inner function can modify the outer function’s behavior.

animals = ["ferret", "vole", "dog", "gecko"]
sorted(animals)
# ['dog', 'ferret', 'gecko', 'vole']

# Defining an Anonymous Function With lambda

# Functional programming is all about calling functions and passing them around, so it
# naturally involves defining a lot of functions. You can always define a function
# in the usual way, using the def keyword.

# Sometimes, though, it’s convenient to be able to define an anonymous function on the fly, without having to give it a name. 
# In Python, you can do this with a lambda expression.

# The syntax looks like this:

# lambda <parameter_list>: <expression>

# There is no difference between these two below:

# 1

reverse = lambda s: s[::-1]
reverse("I am a string")
'gnirts a ma I'

# 2

def reverse(s):
    return s[::-1]

reverse("I am a string")
# 'gnirts a ma I'

# You can also call the function defined by a lambda expression directly:

(lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6)
# 7.0

# You can define a lambda function without parameters. The return value is then not dependent on any input parameters:

forty_two_producer = lambda: 42
forty_two_producer()
# 42

# The return value from a lambda expression can only be one single expression.

# In a function, If a return statement in a function contains several comma-separated values, then Python packs them and returns them as a tuple:

def func(x):
    return x, x ** 2, x ** 3

func(3)
# (3, 9, 27)

# Calling map() With a Single Iterable

# COOL STUFF:

# map(<f>, <iterable>) returns in iterator that yields the results of applying function <f> to each element of <iterable>.

# Suppose we have reverse():

>>> def reverse(s):
...     return s[::-1]
...
>>> reverse("I am a string")
'gnirts a ma I'

# If you have a list of strings, then you can use map() to apply reverse() to each element of the list:

>>> animals = ["cat", "dog", "hedgehog", "gecko"]

