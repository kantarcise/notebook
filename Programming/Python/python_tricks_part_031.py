# Dictionary Pretty-Printing

# Have you ever tried hunting down a bug in one of your programs by
# sprinkling a bunch of debug “print” statements to trace the execution
# flow? Or maybe you needed to generate a log message to print some
# configuration settings...

# I have—and I’ve often been frustrated with how difficult some data
# structures are to read in Python when they’re printed as text strings.
# For example, here’s a simple dictionary. Printed in an interpreter 
# session, the key order is arbitrary, and there’s no indentation to the resulting string:

mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
str(mapping)
# {'b': 42, 'c': 12648430, 'a': 23}

# Luckily there are some easy-to-use alternatives to a straight up to-
# str conversion that give a more readable result. One option is using
# Python’s built-in json module. You can use json.dumps() to pretty-
# print Python dicts with nicer formatting:

import json
json.dumps(mapping, indent=4, sort_keys=True)
# {
#     "a":"b":"c":23,
#     42,
#     12648430
# }


# These settings result in a nicely indented string representation that
# also normalizes the order of the dictionary keys for better legibility.
# While this looks nice and readable, it isn’t a perfect solution. 
# Printing dictionaries with the json module only works with dicts that 
# contain primitive types—you’ll run into trouble trying to print a dictionary
# that contains a non-primitive data type, like a function:

json.dumps({all: 'yup'})
# TypeError: "keys must be a string"

# Another downside of using json.dumps() is that it can’t stringify complex data types, like sets:

mapping['d'] = {1, 2, 3}
json.dumps(mapping)
# TypeError: "set([1, 2, 3]) is not JSON serializable"

# Also, you might run into trouble with how Unicode text is
# represented—in some cases you won’t be able to take the output
# from json.dumps and copy and paste it into a Python interpreter
# session to reconstruct the original dictionary object.

# The classical solution to pretty-printing objects in Python is the built-
# in pprint module. Here’s an example:

import pprint
pprint.pprint(mapping)
# {'a': 23, 'b': 42, 'c': 12648430, 'd': set([1, 2, 3])}

# You can see that pprint is able to print data types like sets, and it also
# prints the dictionary keys in a reproducible order. Compared to the
# standard string representation for dictionaries, what we get here is
# much easier on the eyes.

# However, compared to json.dumps(), it doesn’t represent nested
# structures as well visually. Depending on the circumstances, this can
# be an advantage or a disadvantage. I occasionally use json.dumps()
# to print dictionaries because of the improved readability and 
# formatting, but only if I’m sure they’re free of non-primitive data types.


# Key Takeaways
# • The default to-string conversion for dictionary objects in
# Python can be difficult to read.
# • The pprint and json module are “higher-fidelity” options built
# into the Python standard library.
# • Be careful with using json.dumps() and non-primitive keys
# and values as this will trigger a TypeError.

# Pythonic Productivity Techniques

# Exploring Python Modules and Objects

# You can interactively explore modules and objects directly from the
# Python interpreter. This is an underrated feature that’s easy to 
# overlook, especially if you’re switching to Python from another language.

# Many programming languages make it difficult to inspect a package or
# class without consulting online documentation or learning interface
# definitions by heart.

# Python is different—an effective developer will spend quite a bit of
# time in REPL sessions working interactively with the Python interpreter.
# For example, I often do this to work out little snippets of code
# and logic that I then copy and paste into a Python file I’m working on in my editor.

# In this chapter you’ll learn two simple techniques you can use to 
# explore Python classes and methods interactively from the interpreter.
# These techniques will work on any Python install—just start up the
# Python interpreter with the python command from the command-line
# and fire away. This is great for debugging sessions on systems
# where you don’t have access to a fancy editor or IDE, for example, 
# because you’re working over the network in a terminal session.

# Ready? Here we go! Imagine you’re writing a program that uses
# Python’s datetime module from the standard library. How can you
# find out what functions or classes this module exports, and which
# methods and attributes can you find on its classes?

# Consulting a search engine or looking up the official Python 
# documentation on the web would be one way to do it. But Python’s built-
# in dir() function lets you access this information directly from the

# Python REPL:
 
import datetime
dir(datetime)
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__',
# '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__', '_divide_and_round',
# 'date', 'datetime', 'datetime_CAPI', 'time',
# 'timedelta', 'timezone', 'tzinfo']

# In the example above, I first imported the datetime module from the
# standard library and then inspected it with the dir() function. 
# Calling dir() on a module gives you an alphabetized list of the names and
# attributes the module provides.

# Because “everything” is an object in Python, the same technique works
# not only on the module itself, but also on the classes and data 
# structures exported by the module.

# In fact, you can keep drilling down into the module by calling dir()
# again on individual objects that look interesting. For example, here’s
# how you’d inspect the datetime.date class:

dir(datetime.date)
# ['__add__', '__class__', ..., 'day', 'fromordinal',
# 'isocalendar', 'isoformat', 'isoweekday', 'max',
# 'min', 'month', 'replace', 'resolution', 'strftime',
# 'timetuple', 'today', 'toordinal', 'weekday', 'year']

# As you can see, dir() gives you a quick overview of what’s available
# on a module or class. If you don’t remember the exact spelling for a
# particular class or function, then maybe that’s all you need to keep
# going without interrupting your coding flow.

# Sometimes calling dir() on an object will result in too much
# information—on a complex module or class you’ll get a long printout
# that’s difficult to read quickly. Here’s a little trick you can use to filter
# down the list of attributes to just the ones you’re interested in:


[_ for _ in dir(datetime) if 'date' in _.lower()]
# ['date', 'datetime', 'datetime_CAPI']

# Here, I used a list comprehension to filter down the results of the
# dir(datetime) call to only contain names that include the word
# “date.” Notice how I called the lower() method on each name to
# make sure the filtering is case-insensitive.

# Getting a raw listing of the attributes on an object won’t always be
# enough information to solve the problem at hand. So, how can you get
# more info and further details on the functions and classes exported by
# the datetime module?

# Python’s built-in help() function will come to your rescue. With it,
# you can invoke Python’s interactive help system to browse the auto-
# generated documentation for any Python object:

help(datetime)
# If you run the above example in a Python interpreter session, your 
# terminal will display a text-based help screen for the datetime module,
# looking somewhat like this:

# Help on module datetime:
# NAME datetime - Fast implementation of the datetime type.
# CLASSES builtins.object
# date
# datetime
# time

# You can use the cursor up and down keys to scroll through the 
# documentation. Alternatively you can also hit the space bar to scroll down
# a few lines at once. To leave this interactive help mode you’ll need
# to press the q key. This will take you back to the interpreter prompt.
# Nice feature, right?

# By the way, you can call help() on arbitrary Python objects, including
# other built-in functions and your own Python classes. The Python
# interpreter automatically generates this documentation from the 
# attributes on an object and its docstring (if available.) The examples
# below are all valid uses of the help function:

help(datetime.date)
help(datetime.date.fromtimestamp)
help(dir)

# Of course, dir() and help() won’t replace nicely formatted HTML
# documentation, the powers of a search engine, or a Stack Overflow
# search. But they’re great tools for quickly looking things up without
# having to switch away from the Python interpreter. They’re also 
# available offline and work without an internet connection—which can be
# very useful in a pinch.

# Key Takeaways
# • Use the built-in dir() function to interactively explore Python
# modules and classes from an interpreter session.
# • The help() built-in lets you browse through the documentation
# right from your interpreter (hit q to exit.)

# Isolating Project Dependencies With Virtualenv

# Python includes a powerful packaging system to manage the module
# dependencies of your programs. You’ve probably used it to install
# third-party packages with the pip package manager command.
# One confusing aspect of installing packages with pip is that it tries to
# install them into your global Python environment by default.
# Sure, this makes any new packages you install available globally on
# your system, which is great for convenience. But it also quickly turns
# into a nightmare if you’re working with multiple projects that require
# different versions of the same package.

# For example, what if one of your projects needs version 1.3 of a library
# while another project needs version 1.4 of the same library?
# When you install packages globally there can be only one version of a
# Python library across all of your programs. This means you’ll quickly
# run into version conflicts—just like the Highlander did.

# And it gets worse. You might also have different programs that need
# different versions of Python itself. For example, some programs
# might still run on Python 2 while most of your new development
# happens in Python 3. Or, what if one of your projects needs Python
# 3.3, while everything else runs on Python 3.6?

# Besides that, installing Python packages globally can also incur a secu-
# rity risk. Modifying the global environment often requires you to run
# the pip install command with superuser (root/admin) credentials.
# Because pip downloads and executes code from the internet when you
# install a new package, this is generally not recommended. Hopefully
# the code is trustworthy, but who knows what it will really do?

# Virtual Environments to the Rescue

# The solution to these problems is to separate your Python 
# environments with so-called virtual environments. They allow you to 
# separate Python dependencies by project and give you the ability to select
# between different versions of the Python interpreter.

# A virtual environment is an isolated Python environment. Physically,
# it lives inside a folder containing all the packages and other 
# dependencies, like native-code libraries and the interpreter runtime, that
# a Python project needs. (Behind the scenes, those files might not be
# real copies but symbolic links to save memory.)

# To demonstrate how virtual environments work, I’ll give you a quick
# walkthrough where we’ll set up a new environment (or virtualenv, as
# they’re called for short) and then install a third-party package into it.

# Let’s first check where the global Python environment currently re-
# sides. On Linux or macOS, we can use the which command-line tool
# to look up the path to the pip package manager:

$ which pip3
# /usr/local/bin/pip3

# I usually put my virtual environments right into my project folders
# to keep them nice and separate. But you could also have a dedicated
# “python-environments” directory somewhere to hold all of your envi-
# ronments across projects. The choice is yours.

# Let’s create a new Python virtual environment:

$ python3 -m venv ./venv

# This will take a moment and will create a new venv folder in the 
# current directory and seed it with a baseline Python 3 environment:

$ ls venv/
# bin include lib pyvenv.cfg

# If you check the active version of pip (with the which command),
# you’ll see it’s still pointing to the global environment,
# /usr/local/bin/pip3 in my case:

(venv) $ which pip3
# /usr/local/bin/pip3

# This means if you install packages now, they’d still end up in the
# global Python environment. Creating a virtual environment folder
# isn’t enough—you’ll need to explicitly activate the new virtual
# environment so that future runs of the pip command reference it:

$ source ./venv/bin/activate
(venv) $

# Running the activate command configures your current shell 
# session to use the Python and pip commands from the virtual environment instead.

# Notice how this changed your shell prompt to include the name of the
# active virtual environment inside parentheses: (venv). Let’s check
# which pip executable is active now:

(venv) $ which pip3
# /Users/dan/my-project/venv/bin/pip3

# As you can see, running the pip3 command would now run the version
# from the virtual environment and not the global one. The same
# is true for the Python interpreter executable. Running python from
# the command-line would now also load the interpreter from the venv
# folder:

(venv) $ which python
# /Users/dan/my-project/venv/bin/python

# Note that this is still a blank slate, a completely clean Python 
# environment. Running pip list will show an almost empty list of installed
# packages that only includes the baseline modules necessary to support pip itself:

(venv) $ pip list
# pip (9.0.1)
# setuptools (28.8.0)

# Let’s go ahead and install a Python package into the virtual environment
# now. You’ll want to use the familiar pip install command for that:

(venv) $ pip install schedule
# Collecting schedule
# Downloading schedule-0.4.2-py2.py3-none-any.whl
# Installing collected packages: schedule
# Successfully installed schedule-0.4.2

# You’ll notice two important changes here. First, you won’t need admin
# permissions to run this command any longer. And second, installing
# or updating a package with an active virtual environment means that
# all files will end up in a subfolder in the virtual environment’s directory.

# Therefore, your project dependencies will be physically separated
# from all other Python environments on your system, including the
# global one. In effect, you get a clone of the Python runtime that’s
# dedicated to one project only.

# By running pip list again, you can see that the schedule library was
# installed successfully into the new environment:

(venv) $ pip list
# pip (9.0.1)
# schedule (0.4.2)
# setuptools (28.8.0)

# If we spin up a Python interpreter session with the python command,
# or run a standalone .py file with it, it will use the Python interpreter
# and the dependencies installed into the virtual environment—as long
# as the environment is still active in the current shell session.
# But how do you deactivate or “leave” a virtual environment again?
# Similar to the activate command, there’s a deactivate command
# that takes you back to the global environment:

(venv) $ deactivate
$ which pip3
# /usr/local/bin

# Using virtual environments will help keep your system uncluttered
# and your Python dependencies neatly organized. As a best practice,
# all of your Python projects should use virtual environments to keep
# their dependencies separate and to avoid version conflicts.
# Understanding and using virtual environments also puts you on the
# right track to use more advanced dependency management methods
# like specifying project dependencies with requirements.txt files.

# Key Takeaways
# • Virtual environments keep your project dependencies 
# separated. They help you avoid version conflicts between packages
# and different versions of the Python runtime.
# • As a best practice, all of your Python projects should use virtual
# environments to store their dependencies. This will help avoid headaches.

# Peeking Behind the Bytecode Curtain

# When the CPython interpreter executes your program, it first translates
# it into a sequence of bytecode instructions. Bytecode is an in-
termediate language for the Python virtual machine that’s used as a
performance optimization.
Instead of directly executing the human-readable source code, com-
pact numeric codes, constants, and references are used that represent
the result of compiler parsing and semantic analysis.
This saves time and memory for repeated executions of programs or
parts of programs. For example, the bytecode resulting from this com-
pilation step is cached on disk in .pyc and .pyo files so that executing
the same Python file is faster the second time around.
All of this is completely transparent to the programmer. You don’t
have to be aware that this intermediate translation step happens, or
how the Python virtual machine deals with the bytecode. In fact, the
bytecode format is deemed an implementation detail and not guaran-
teed to remain stable or compatible between Python versions.
And yet, I find it very enlightening to see how the sausage is made and
to peek behind the abstractions provided by the CPython interpreter.
Understanding at least some of the inner workings can help you write
more performant code (when that’s important). And it’s also a lot of
fun.
Let’s take this simple greet() function as a lab sample we can play
with and use to understand Python’s bytecode:
def greet(name):
return 'Hello, ' + name + '!'
>>> greet('Guido')
'Hello, Guido!'

Remember how I said that CPython first translates our source code
into an intermediate language before it “runs” it? Well, if that’s true,
we should be able to see the results of this compilation step. And we
can.
Each function has a __code__ attribute (in Python 3) that we can use
to get at the virtual machine instructions, constants, and variables
used by our greet function:
>>> greet.__code__.co_code
b'dx01|x00x17x00dx02x17x00Sx00'
>>> greet.__code__.co_consts
(None, 'Hello, ', '!')
>>> greet.__code__.co_varnames
('name',)
You can see co_consts contains parts of the greeting string our func-
tion assembles. Constants and code are kept separate to save memory
space. Constants are, well, constant—meaning they can never be mod-
ified and are used interchangeably in multiple places.
So instead of repeating the actual constant values in the co_code in-
struction stream, Python stores constants separately in a lookup ta-
ble. The instruction stream can then refer to a constant with an in-
dex into the lookup table. The same is true for variables stored in the
co_varnames field.
I hope this general concept is starting to become more clear. But
looking at the co_code instruction stream still makes me feel a little
queasy. This intermediate language is clearly meant to be easy to work
with for the Python virtual machine, not humans. After all, that’s what
the text-based source code is for.
The developers working on CPython realized that too. So they gave
us another tool called a disassembler to make inspecting the bytecode
easier.

Python’s bytecode disassembler lives in the dis module that’s part of
the standard library. So we can just import it and call dis.dis() on
our greet function to get a slightly easier-to-read representation of
its bytecode:
>>> import dis
>>> dis.dis(greet)
2
 0 LOAD_CONST
2 LOAD_FAST
4 BINARY_ADD
6 LOAD_CONST
8 BINARY_ADD
10 RETURN_VALUE
1 ('Hello, ')
0 (name)
2 ('!')
The main thing disassembling did was split up the instruction stream
and give each opcode in it a human-readable name like LOAD_CONST.
You can also see how constant and variable references are now inter-
leaved with the bytecode and printed in full to spare us the mental
gymnastics of a co_const or co_varnames table lookup. Neat!
Looking at the human-readable opcodes, we can begin to understand
how CPython represents and executes the 'Hello, ' + name + '!'
expression in the original greet() function.
It first retrieves the constant at index 1 ('Hello, ') and puts it on the
stack. It then loads the contents of the name variable and also puts
them on the stack.
The stack is the data structure used as internal working storage for the
virtual machine. There are different classes of virtual machines and
one of them is called a stack machine. CPython’s virtual machine is an
implementation of such a stack machine. If the whole thing is named
after the stack, you can imagine what a central role this data structure
plays.
By the way—I’m only touching the surface here. If you’re interested in

this topic you’ll find a book recommendation at the end of this chapter.
Reading up on virtual machine theory is enlightening (and a ton of
fun).
What’s interesting about a stack as an abstract data structure is that,
at the bare minimum, it only supports two operations: push and pop.
Push adds a value to the top of the stack and pop removes and returns
the topmost value. Unlike an array, there’s no way to access elements
“below” the top level.
I find it fascinating that such a simple data structure has so many uses.
But I’m getting carried away again...
Let’s assume the stack starts out empty. After the first two opcodes
have been executed, this is what the contents of the VM stack look
like (0 is the topmost element):
0: 'Guido' (contents of "name")
1: 'Hello, '
The BINARY_ADD instruction pops the two string values off the stack,
concatenates them, and then pushes the result on the stack again:
0: 'Hello, Guido'
Then there’s another LOAD_CONST to get the exclamation mark string
on the stack:
0: '!'
1: 'Hello, Guido'
The next BINARY_ADD opcode again combines the two to generate the
final greeting string:

  0: 'Hello, Guido!'
The last bytecode instruction is RETURN_VALUE which tells the virtual
machine that what’s currently on top of the stack is the return value
for this function so it can be passed on to the caller.
And voila, we just traced back how our greet() function gets executed
internally by the CPython virtual machine. Isn’t that cool?
There’s much more to say about virtual machines, and this isn’t the
book for it. But if this got you interested, I highly recommend that
you do some more reading on this fascinating subject.
It can be a lot of fun to define your own bytecode languages and to
build little virtual machine experiments for them. A book on this topic
that I’d recommend is Compiler Design: Virtual Machines by Wilhelm
and Seidl.
Key Takeaways
•••CPython executes programs by first translating them into an in-
termediate bytecode and then running the bytecode on a stack-
based virtual machine.
You can use the built-in dis module to peek behind the scenes
and inspect the bytecode.
Study up on virtual machines—it’s worth it.


