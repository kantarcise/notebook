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


