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


        
