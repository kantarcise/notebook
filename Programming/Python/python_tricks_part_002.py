# Effective Functions

# Python’s Functions Are First-Class. What is that mean ?

# Python’s functions are first-class objects. You can assign them to variables,
# store them in data structures, pass them as arguments to other
# functions, and even return them as values from other functions.

def yell(text):
    return text.upper() + '!'

yell('hello')
# 'HELLO!'

bark = yell

bark("woof")
# "WOOF!"

del yell

yell("hello?")
# NameError: "name 'yell' is not defined"

bark("hey")
# "HEY!"

bark.__name__
# "yell"

# Since functions are first-class citizens, you can store them in data
# structures, just like you can with other objects. For example, you can
# add functions to a list:

funcs = [bark, str.lower, str.capitalize]

funcs
# [<function yell at 0x10ff96510>,
#  <method 'lower' of 'str' objects>,
#  <method 'capitalize' of 'str' objects>]


# This is weird but you can even do:

funcs[0]("heyho")
#"HEYHO!"

# Functions Can Be Passed to Other Functions

# Because functions are objects, you can pass them as arguments to
# other functions. Here’s a greet function that formats a greeting string
# using the function object passed to it and then prints it:

def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)

greet(bark)
# 'HI, I AM A PYTHON PROGRAM!'

# Functions that can accept other functions as arguments are also called
# higher-order functions. They are a necessity for the functional programming style.

# The classical example for higher-order functions in Python is the built-
# in map function. It takes a function object and an iterable, and then
# calls the function on each element in the iterable, yielding the results
# as it goes along.

list(map(bark, ['hello', 'hey', 'hi']))
# ['HELLO!', 'HEY!', 'HI!']

# Functions Can Be Nested

# Nested Functions or Inner Functions:

def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)
 
speak('Hello, World')
# 'hello, world...'

# Here’s the kicker though—whisper does not exist outside speak:

whisper("Yo")
# NameError:
# "name "whisper" is not defined" 

# But what if you really wanted to access that nested whisper function from outside speak? 
# Well, functions are objects—you can return the inner function to the caller of the parent function.

# For example, here’s a function defining two inner functions. Depending
# on the argument passed to top-level function, it selects and returns
# one of the inner functions to the caller:

def get_speak_func(volume):
    def whisper(text):
        return text.lower() + '...'
    def yell(text):
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

# Notice how get_speak_func doesn’t actually call any of its inner
# functions—it simply selects the appropriate inner function based on
# the volume argument and then returns the function object:

get_speak_func(0.3)
# <function get_speak_func.<locals>.whisper at 0x10ae18>
get_speak_func(0.7)
# <function get_speak_func.<locals>.yell at 0x1008c8>

# Of course, you could then go on and call the returned function, either
# directly or by assigning it to a variable name first:

speak_func = get_speak_func(0.7)
speak_func('Hello')
# 'HELLO!'

# Functions Can Capture Local State

# Not only can functions return other functions, these inner functions
# can also capture and carry some of the parent function’s state with
# them. Well, what does that mean?

def get_speak_func(text, volume):
    def whisper():
        return text.lower() + '...'
    def yell():
        return text.upper() + '!'
    if volume > 0.5:
        return yell
    else:
        return whisper

get_speak_func('Hello, World', 0.7)()
# 'HELLO, WORLD!'

# Whisper and Yell no longer has test parameter. What?

# Somehow they can still access the text parameter defined in the parent function. In fact,
# they seem to capture and “remember” the value of that argument.

# Functions that do this are called lexical closures (or just closures, for
# short). A closure remembers the values from its enclosing lexical
# scope even when the program flow is no longer in that scope.

#--------------------------------------------------------------------------------------------------#

# 
# Objects Can Behave Like Functions
#

# While all functions are objects in Python, the reverse isn’t true. Objects aren’t functions. 
# But they can be made callable, which allows you to treat them like functions in many cases.

# If an object is callable it means you can use the round parentheses function call syntax on it and even pass in function call arguments.
# This is all powered by the __call__ dunder method. Here’s an example of class defining a callable object:

class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x

plus_3 = Adder(3)
plus_3(4)
# 7

# Behind the scenes, this object calls it's __call__ method.

# Of course, not all objects will be callable. That’s why there’s a built-in
# callable function to check whether an object appears to be callable or not:

callable(plus_3)
# True
callable(yell)
# True
callable('hello')
# False
