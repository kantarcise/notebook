#  Fun With *args and **kwargs

# *args and **kwargs allow a function to accept optional arguments, s owe can make flexible API's in modules and classes.

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

foo()
# TypeError: "foo() missing 1 required positional arg: 'required'"
foo('hello')
# hello
foo('hello', 1, 2, 3)
# hello
# (1, 2, 3)
foo('hello', 1, 2, 3, key1='value', key2=999)
# hello
# (1, 2, 3)
# {'key1': 'value', 'key2': 999}

#   *args and **kwargs let you write functions with a variable
# number of arguments in Python.
#   *args collects extra positional arguments as a tuple. **kwargs
# collects the extra keyword arguments as a dictionary.
#   The actual syntax is * and **. Calling them args and kwargs is
# just a convention (and one you should stick to).

# Function Argument Unpacking

# The * and ** operators can be used to “unpack” function 
# arguments from sequences and dictionaries.
# Using argument unpacking effectively can help you write more
# flexible interfaces for your modules and functions.

def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))
    
print_vector(0, 1, 0)
# <0, 1, 0>

# What if our vector is a tuple or list, even a dictionary.

tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]

print_vector(tuple_vec[0],
             tuple_vec[1],
             tuple_vec[2])
# <1, 0, 1>

# Thankfully, there’s a better way to handle this situation in Python with
# Function Argument Unpacking using the * operator:

print_vector(*tuple_vec)
# <1, 0, 1>
print_vector(*list_vec)
# <1, 0, 1>

# To unpack keyword arguments from dicts:

dict_vec = {'y': 0, 'z': 1, 'x': 1}

print_vector(**dict_vec)
# <1, 0, 1>

# If you were to use the single asterisk (*) operator to unpack the 
# dictionary, keys would be passed to the function in random order instead:

print_vector(*dict_vec)
# <y, x, z>

        
